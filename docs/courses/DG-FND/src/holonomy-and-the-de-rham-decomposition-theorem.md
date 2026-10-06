# Holonomy and the de Rham decomposition theorem

This chapter proves the local and global decomposition theorems, including products without simple connectivity and finite-rank metric products. It develops the algebraic and representation-theoretic arguments needed to classify irreducible Riemannian holonomy when curvature is not parallel.

Parallel transport compares tangent spaces along a path. When a subspace survives transport around every loop, it determines a distribution throughout the manifold. For a Riemannian metric, two orthogonal parallel distributions then give product coordinates in which each block of the metric depends only on its own coordinates. We establish that chain of implications below, including the topology and completeness of the leaves.

All manifolds are finite-dimensional, Hausdorff, second countable and without boundary. A Riemannian manifold has a smooth positive definite metric \(g\) and its Levi-Civita connection \(\nabla\). The existence, uniqueness and transport identities for this connection are proved in [Riemannian connections and convex neighbourhoods, Theorem A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1).

We use the complete inverse-function and flow proofs in [Local tools for bundles and transport, Theorems 1.2 and 2.1](local-tools-for-bundles-and-transport.md), the coordinate bracket calculation in [Principal bundles and associated bundles, Lemma C.3](principal-bundles-and-associated-bundles.md#lemma-c-3), and the transport constructions in [Linear and affine connections, Theorems A.2 and B.2](linear-and-affine-connections.md#theorem-b-2). Paths have a finite subdivision into \(C^1\) pieces, with continuous one-sided derivatives at the endpoints of each piece; the corresponding transport and parameter dependence are proved in [Curvature and holonomy groups, Lemma C.2](curvature-and-holonomy-groups.md#lemma-c-2).

## A. From invariant subspaces to distributions

For a finite-dimensional real inner-product space \(V\), write \(O(V)\) for its group of linear isometries. An \(H\)-invariant subspace, for \(H\subset O(V)\), is a linear subspace \(W\) such that \(hW=W\) for every \(h\in H\). A nonzero representation is **irreducible** when its only invariant subspaces are zero and the whole space. These definitions do not require \(H\) to be closed or connected.

**Lemma A.1 (orthogonal invariant summands).** For any subgroup \(H\subset O(V)\), there is an orthogonal decomposition into irreducible invariant subspaces. The fixed subspace
\[
V^H=\{v\in V:hv=v\text{ for every }h\in H\}
\]
is intrinsic, and its orthogonal complement has no nonzero fixed vector. One can write
\[
V=V^H\mathbin{\perp}W_1\mathbin{\perp}\cdots\mathbin{\perp}W_s
\]
with each \(W_i\) nonzero and irreducible. Arbitrary irreducible summands need not be uniquely determined.

**Proof.** If \(W\) is invariant, \(z\perp W\) and \(w\in W\), then
\[
\langle hz,w\rangle=\langle z,h^{-1}w\rangle=0.
\]
Thus \(W^\perp\) is invariant. The orthogonal direct-sum assertion \(V=W\oplus W^\perp\) follows directly by choosing an orthonormal basis \(e_1,\ldots,e_r\) of \(W\) and subtracting \(\sum_i\langle v,e_i\rangle e_i\) from \(v\). Such a basis is obtained successively from any basis of \(W\) by subtracting the preceding projections and dividing by the positive length of the remainder. The remainder is nonzero at each step by linear independence.

If \(V\ne0\), choose a nonzero invariant subspace of least positive dimension. It is irreducible, since a proper nonzero invariant subspace would have smaller dimension. Apply the same argument to its invariant orthogonal complement. Dimension drops at each step, so after finitely many steps this gives an orthogonal sum of irreducibles. For \(V=0\) use the empty sum.

The fixed vectors form a subspace, since every \(h\) is linear. Its definition involves no choice of decomposition, and \(H\) acts on it as the identity. Apply the preceding construction to its invariant orthogonal complement. A fixed vector in that complement would also belong to \(V^H\), and hence have zero squared length. It is zero.

Finally, for the trivial subgroup acting on \(\mathbb R^2\), every line is invariant and irreducible. Any line and its perpendicular give an irreducible decomposition; rotating that line changes the summands. This proves the failure of general uniqueness without making any uniqueness claim about holonomy factors. □

Let \(M\) now be connected and nonempty and fix \(p\in M\). For a path \(\gamma\), let \(P_\gamma\) denote parallel transport in \(TM\). The **full holonomy group** at \(p\) consists of the maps \(P_\ell:T_pM\to T_pM\) for all loops \(\ell\) based at \(p\). Reversal gives inverses and concatenation gives products, so it is a subgroup of \(O(T_pM)\). No orientation hypothesis is needed.

A smooth subbundle \(E\subset TM\) is **parallel** if \(\nabla_Xs\) is a section of \(E\) whenever \(s\) is a local section of \(E\) and \(X\) is any local vector field.

**Theorem A.2 (the invariant-subspace correspondence).** Evaluation at \(p\) gives a bijection between parallel smooth subbundles of \(TM\) and subspaces invariant under the full holonomy group at \(p\). The subbundle associated to \(W\subset T_pM\) is
\[
E_q=P_\gamma W,\qquad \gamma:p\longrightarrow q.
\tag{A.1}
\]
Its orthogonal complement is parallel. An orthogonal invariant splitting at \(p\) therefore extends to a smooth orthogonal parallel splitting of \(TM\).

**Proof.** First, any point of \(M\) can be joined to \(p\) by a finite piecewise smooth path. The set of reachable points is open: append a straight coordinate segment in a small coordinate ball. Every other reachability class is open for the same reason. Connectedness excludes more than one class.

If \(\gamma,\eta\) both run from \(p\) to \(q\), then \(P_\eta^{-1}P_\gamma\) is holonomy at \(p\). Invariance of \(W\) gives \(P_\gamma W=P_\eta W\), proving that (A.1) is well defined. It has constant dimension because transport is invertible.

To see smoothness, fix a coordinate ball about \(q_0\), a path from \(p\) to \(q_0\), and a basis of the resulting subspace \(E_{q_0}\). Transport this basis along the coordinate radial segments from \(q_0\) to \(q\). Their endpoints and first time derivatives depend smoothly on \(q\); the parameter theorem in Curvature C.2 gives smooth transported vector fields. They are independent at every point because transport is invertible, and they span (A.1). They are local bundle frames for \(E\).

Appending a path \(\sigma:q\to q'\) to one from \(p\) shows \(P_\sigma E_q=E_{q'}\). For a local section \(s\) of \(E\), a curve \(c\) with \(c(0)=q\), and small \(t\), it follows that \(P_{c|[0,t]}^{-1}s(c(t))\) belongs to the fixed subspace \(E_q\). Differentiating at zero leaves it in \(E_q\); the transport derivative identity of Linear B.2 identifies this derivative with \(\nabla_{\dot c(0)}s\). Every tangent vector is the initial velocity of a coordinate straight curve. Hence \(E\) is parallel.

Conversely suppose \(E\) is a parallel subbundle. Near any point, choose a smooth frame \(e_1,\ldots,e_r\) of \(E\), and complete it to a frame of \(TM\). To justify the completion locally, add fixed coordinate vectors whose values complete the basis at the point. The determinant is nonzero there, and remains nonzero after shrinking the chart. In the resulting frame, parallelness says that the columns for \(\nabla e_i\), \(i\leq r\), have zero entries in the complementary rows. Along a path, the complementary coordinates \(z(t)\) of a parallel vector thus satisfy a homogeneous equation
\[
z'(t)=-B(t)z(t).
\]
If they start at zero, uniqueness for the transport equation gives \(z=0\) on that chart interval. Cover the path by finitely many such intervals and compose. Transport maps \(E_q\) into \(E_{q'}\); reversal proves equality. In particular \(E_p\) is invariant under every loop, and (A.1) recovers \(E\), proving both directions and uniqueness.

Metric compatibility makes \(P_\gamma\) an isometry. Consequently it also preserves the orthogonal complements. These complements form a smooth subbundle: in a smooth local frame of \(E\), its Gram matrix is positive and invertible, and the formula
\[
\pi_E v=\sum_{i,j}e_i(G^{-1})_{ij}g(e_j,v),\qquad G_{ij}=g(e_i,e_j)
\]
is a smooth projection. Smoothness of matrix inversion is Local tools 0.4; its kernel is locally spanned by a frame completed and orthogonalized against the \(e_i\). The already proved transport-to-derivative argument makes this complement parallel. Transporting all the summands of a splitting preserves orthogonality, their dimensions and their direct sum. □

## B. Coordinates and the topology of leaves

A smooth distribution \(D\) of rank \(r\) is a rank \(r\) subbundle of \(TM\). It is **involutive** if \([X,Y]\) is a section of \(D\) for all local sections \(X,Y\) of \(D\). A **plaque** in coordinates \((x,y)\in U_x\times U_y\subset\mathbb R^r\times\mathbb R^{n-r}\) is a set \(U_x\times\{y_0\}\). We take the coordinate factors to be open balls or boxes, so plaques are connected.

**Lemma B.1 (commuting local flows).** If two smooth vector fields \(X,Y\) satisfy \([X,Y]=0\), their local flows commute wherever a sufficiently small flow rectangle is defined. The flow of \(X\) carries \(Y\) to \(Y\).

**Proof.** Write \(\phi_t\) for the local flow of \(X\), whose existence, uniqueness and smoothness are Local tools 2.1. Differentiating its ODE in the starting point gives
\[
\frac{d}{dt}\bigl(d\phi_t|_q\,Y(q)\bigr)
 =DX(\phi_t(q))\,d\phi_t|_q\,Y(q).
\]
This differentiation is legitimate by the smooth parameter conclusion of that theorem. The coordinate bracket formula of Principal bundles C.3 says \([X,Y]=DY\,X-DX\,Y\). Thus \([X,Y]=0\) also gives
\[
\frac{d}{dt}Y(\phi_t(q))
 =DY(\phi_t(q))X(\phi_t(q))
 =DX(\phi_t(q))Y(\phi_t(q)).
\]
These two vectors have the same initial value \(Y(q)\) and solve the same linear ODE. Uniqueness implies \(d\phi_t(Y(q))=Y(\phi_t(q))\).

If \(\psi_s\) is the flow of \(Y\), the curve \(s\mapsto\phi_t(\psi_s(q))\) therefore solves the \(Y\)-equation and starts at \(\phi_t(q)\). Uniqueness identifies it with \(\psi_s(\phi_t(q))\). Smooth local existence allows both compositions on a common small open rectangle of \((s,t,q)\) after shrinking the starting neighbourhood. This proves exactly the local assertion; no completeness of either vector field is assumed. □

**Theorem B.2 (Frobenius coordinates).** A smooth constant-rank distribution is involutive if and only if every point has coordinates \((x^1,\ldots,x^r,y^1,\ldots,y^{n-r})\) in which
\[
D=\operatorname{span}\{\partial_{x^1},\ldots,\partial_{x^r}\}.
\tag{B.1}
\]

**Proof.** In coordinates satisfying (B.1), the coordinate bracket formula shows that the bracket of two fields with only \(x\)-components again has only \(x\)-components. Thus this normal form implies involutivity.

For the converse choose initial coordinates \((u,v)\) centred at a given point such that projection onto the first \(r\) coordinates restricts to an isomorphism on \(D\) at that point. This is possible by choosing a basis of the tangent space whose first \(r\) vectors span \(D\) and applying the corresponding invertible linear change of coordinates. In a smooth local frame of \(D\), the relevant \(r\) by \(r\) matrix remains invertible on a neighbourhood. Its smooth inverse gives unique smooth sections
\[
Y_i=\partial_{u^i}+\sum_{\alpha=1}^{n-r}a_i^\alpha(u,v)\partial_{v^\alpha},
\qquad 1\leq i\leq r,
\]
which span \(D\) and project to the constant coordinate basis. The \(u\)-components of \([Y_i,Y_j]\) are zero. Involutivity puts this bracket in \(D\), where coordinate projection is injective. Hence \([Y_i,Y_j]=0\).

Let \(\phi_i^t\) be the local flow of \(Y_i\). On a sufficiently small product neighbourhood of \((0,0)\), form
\[
\Phi(x,y)=\phi_r^{x^r}\circ\cdots\circ\phi_1^{x^1}(0,y).
\tag{B.2}
\]
All intermediate flows exist on one common neighbourhood by their smooth local existence and the fact that only finitely many compositions occur. Lemma B.1 lets us interchange adjacent flows there; each preserves every \(Y_j\). Differentiating (B.2) therefore gives \(d\Phi(\partial_{x^i})=Y_i\circ\Phi\). At \((0,0)\), the remaining derivatives \(d\Phi(\partial_{y^\alpha})\) are the coordinate \(v\)-vectors. Together these columns are independent: projection onto \(u\) first annihilates only the \(v\)-columns, after which their coefficients must also be zero.

The inverse-function theorem, Local tools 1.2, makes \(\Phi\) a diffeomorphism on a smaller neighbourhood. Restrict that neighbourhood further to a product of coordinate balls or boxes. In these new coordinates \(D\) is (B.1). For \(r=0\) every chart works; for \(r=n\) the same construction has no \(y\)-variables. □

**Theorem B.3 (maximal integral leaves).** For an involutive distribution \(D\), let \(L_p\) be the set of endpoints of finite piecewise \(C^1\) paths starting at \(p\) and tangent to \(D\). There is a canonical connected Hausdorff second-countable smooth manifold structure on \(L_p\) for which its inclusion into \(M\) is an injective immersion with tangent image \(D\). It is the unique maximal integral leaf through \(p\). The leaf topology is the topology defined by its plaques.

**Proof.** Reachability is an equivalence relation: use the constant path, reversal and concatenation. In a chart from B.2, every tangent path has \(y'(t)=0\) on each smooth piece. The fundamental theorem of calculus, Local tools 0.3, makes \(y\) constant there and continuity keeps the same value across the junctions. Conversely any two points in one plaque can be connected inside it by the coordinate straight segment. A plaque meeting \(L_p\) therefore lies in \(L_p\).

Give \(L_p\) the topology generated by open subsets of all such plaques that lie in \(L_p\). We check the chart overlaps. If plaques \(P,Q\) meet at \(q\), restrict their ambient chart overlap to a small connected neighbourhood of \(q\) in \(P\). The transverse coordinates of the chart for \(Q\) have differential zero on \(D\). Along coordinate segments in this neighbourhood of \(P\) they are constant, so the neighbourhood lies in \(Q\). The same argument with \(P,Q\) reversed shows that their intersection is open in both plaques. Their coordinate transitions are restrictions of the smooth ambient change of coordinates. Their derivatives are isomorphisms because both tangent spaces map isomorphically onto the same \(D_q\). Alternatively differentiating the two inverse transition maps gives the identity. Thus plaques define a compatible smooth atlas of dimension \(r\). Ambient open sets meet every plaque openly, so the inclusion \(L_p\to M\) is continuous. Distinct points can be separated by disjoint ambient open sets because \(M\) is Hausdorff. The leaf is therefore Hausdorff, and its inclusion is a smooth injective immersion with tangent image \(D\).

Here is the countability argument. There is a countable atlas of Frobenius charts covering \(M\). Indeed a second-countable space is Lindelöf: from an open cover, for each member of a countable base that is contained in a member of the cover, choose one such cover member. These countably many chosen members cover every point. Apply this to the Frobenius charts. In a fixed plaque \(P\) of one chosen chart, intersection with any other chart is an open subset of \(P\), hence has at most countably many connected components. To verify this last fact, open subsets of Euclidean space are locally connected, since small open balls are connected by straight segments. Their connected components are open: the component containing a point contains every sufficiently small such ball. Each component contains a distinct element of a countable Euclidean base. There are consequently countably many components, each path connected by the same open-reachability argument as in A.2. Transverse coordinates for the second chart are constant on each component, by differentiation along coordinate paths. Thus \(P\) meets at most countably many plaques of that chart.

Start with one chosen plaque containing \(p\). Add all plaques in the countable atlas that intersect it, then all plaques intersecting one already added, and repeat finitely many steps at a time. Each stage adds at most countably many plaques by the preceding paragraph, and the union of all stages is countable. These plaques cover \(L_p\). To see this, a finite tangent path has a finite chart subdivision by compactness of its parameter interval, and each subpath lies in one plaque. The resulting finite chain starts in the plaque of \(p\). More explicitly, a finite open cover of a compact interval has a positive subdivision scale: otherwise intervals of lengths tending to zero that lie in no cover member have a convergent sequence of points, contradicting openness of a member containing the limit. This supplies the subdivision even for an arbitrary continuous path. Since any two plaque charts through the same point have open overlap, the countably many plaques just constructed give the same topology as all plaques. A countable Euclidean base in each one gives a countable base for \(L_p\).

Every tangent path is continuous into this leaf topology: locally it stays in one plaque and its coordinate expression is continuous there. Hence \(L_p\) is path connected. If \(i:N\to M\) is any connected immersed integral manifold through \(p\), points of \(N\) can be joined by finite coordinate paths; their images are tangent paths, so \(i(N)\subset L_p\). Locally the transverse coordinates composed with \(i\) have zero differential and hence are constant on a connected coordinate ball. The map therefore factors smoothly through a plaque of \(L_p\). Its derivative has rank \(r\), so when \(N\) is an integral manifold of dimension \(r\) the inverse-function theorem makes this factorization a local diffeomorphism. These facts prove maximality and uniqueness of the leaf with its integral-manifold structure.

Finally our topology is defined using plaques, which are required to be open in the leaf. We have proved continuity of inclusion, not that an entire plaque is the intersection of the leaf with an ambient open set. The construction and the completeness arguments below use this plaque topology throughout; they do not impose an embedding hypothesis on the inclusion. □

## C. Orthogonal parallel distributions give a local product

Assume \(TM=E\mathbin{\perp}F\) is a smooth orthogonal splitting into parallel subbundles of ranks \(r,s\). Let \(L_E(p)\) and \(L_F(p)\) be the corresponding leaves when their existence has been established.

**Theorem C.1 (the local Riemannian product).** Both distributions are involutive. Every point has a neighbourhood isometric to a product \(U_E\times U_F\), where \(U_E\) and \(U_F\) are open neighbourhoods in the respective leaves through that point with their induced metrics. The coordinate tangent distributions of the product are exactly \(E,F\).

**Proof.** Zero torsion gives \([X,Y]=\nabla_XY-\nabla_YX\). If \(X,Y\) are sections of \(E\), parallelness puts both derivatives in \(E\). The same argument applies to \(F\). Thus B.2–B.3 supply their charts and leaves.

Choose transverse coordinate maps \(\eta:U\to\mathbb R^s\) for \(E\) and \(\xi:U\to\mathbb R^r\) for \(F\), on a common ambient neighbourhood. In other words \(\ker d\eta=E\) and \(\ker d\xi=F\), by B.2. The derivative of \((\xi,\eta)\) has kernel \(E\cap F=0\); source and target have the same dimension, so it is invertible. Local tools 1.2 makes this a coordinate map near the point. Restrict its image to a product and write these coordinates as \((x,y)\). Then \(\partial_{x^i}\in E\) and \(\partial_{y^\alpha}\in F\), since the respective transverse coordinates are constant in those directions.

Set \(X_i=\partial_{x^i}\) and \(Y_\alpha=\partial_{y^\alpha}\). Their bracket vanishes. Since \(F\) is parallel, \(\nabla_{X_i}Y_\alpha\in F\); since \(E\) is parallel, \(\nabla_{Y_\alpha}X_i\in E\). Zero torsion equates these two vectors, and \(E\cap F=0\) forces
\[
\nabla_{X_i}Y_\alpha=\nabla_{Y_\alpha}X_i=0.
\tag{C.1}
\]
Metric compatibility now gives
\[
\partial_{y^\alpha}g(X_i,X_j)=0,\qquad
\partial_{x^i}g(Y_\alpha,Y_\beta)=0.
\tag{C.2}
\]
The cross terms \(g(X_i,Y_\alpha)\) vanish by orthogonality. Since the coordinate factors are connected boxes, (C.2) and the fundamental theorem on coordinate segments say that
\[
g=\sum_{i,j}g^E_{ij}(x)\,dx^i\,dx^j
  +\sum_{\alpha,\beta}g^F_{\alpha\beta}(y)\,dy^\alpha\,dy^\beta.
\tag{C.3}
\]
Here each sum denotes the corresponding symmetric bilinear tensor. The slices \(y=y(p)\) and \(x=x(p)\) are plaques and hence open neighbourhoods in the two leaves. Their induced metrics are exactly the two blocks of (C.3). The coordinate product map from these plaques to the ambient neighbourhood pulls \(g\) back to their product metric. If a rank is zero, its plaque is a point and the same argument has an empty block. □

**Theorem C.2 (totally geodesic and complete leaves).** Each leaf of \(E\) or \(F\), with its induced Riemannian metric and its leaf topology, is totally geodesic. If \(M\) is complete, every such leaf is intrinsically complete.

**Proof.** Work first with an \(E\)-leaf \(L\) and its inclusion \(i\). Locally a plaque is embedded and tangent to \(E\). Extend tangent fields on the plaque to sections of \(E\) in an ambient chart. Covariant differentiation in a tangent direction is independent of the extension: in a local frame its formula differentiates only along that direction, so a section vanishing on the plaque has zero derivative along any curve in the plaque. Since \(E\) is parallel, the derivative remains tangent to \(L\). These local derivatives agree on overlapping plaques, and define a connection on \(TL\). The chain rule for derivatives along maps (Linear B.2) and the ambient identities show that it is metric compatible and has zero torsion. By the uniqueness part of Riemannian A.1 it is the Levi-Civita connection of the induced metric. Consequently the immersion has zero normal derivative of tangent fields: it is totally geodesic, and its geodesics map to ambient geodesics with the same parameter.

Conversely an ambient geodesic starting at a point of \(L\) with velocity in \(E\) stays tangent to \(E\), because its velocity is parallel and A.2 says transport preserves \(E\). Every compact portion is a tangent path, so B.3 places it in \(L\), and its coordinate expression in plaques is smooth for the leaf topology. Thus it is a geodesic of \(L\). Existence and uniqueness for these geodesics are [Geodesics, normal coordinates and curvature, Theorem A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1).

If \(M\) is metrically complete, [Completeness and the Hopf–Rinow theorem, Theorem B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) makes all its geodesics exist for every real time. The preceding paragraph gives a leaf geodesic for every real time for each initial tangent vector of \(L\). B.3 proved that \(L\) is connected, Hausdorff and second countable, so Hopf–Rinow applies to \(L\) itself and proves completeness of its intrinsic distance. The \(F\)-case is identical with the names of the distributions interchanged. No closedness or embeddedness of a leaf is required. □

**Corollary C.3 (mixed curvature and flat transverse connections).** With the convention
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z,
\]
for \(u,u'\in E_p\) and \(v,v'\in F_p\) one has
\[
R(u,v)=0,\qquad R(u,u')v=0,\qquad R(v,v')u=0.
\tag{C.4}
\]
The connection induced on \(F\) along an \(E\)-leaf is flat, and the connection induced on \(E\) along an \(F\)-leaf is flat.

**Proof.** Use the product coordinates in C.1. The coordinate formula in Riemannian A.1 and the metric (C.3) show that the coefficients of \(\nabla_{X_i}X_j\) are entirely in the \(X\)-frame and depend only on \(x\). Indeed the inverse metric has the same two blocks, and its \(E\)-block is the inverse of \(g^E(x)\). Each derivative in the formula for these coefficients is an \(x\)-derivative of that block. The coefficients of \(\nabla_{Y_\alpha}Y_\beta\) likewise depend only on \(y\) and have only \(Y\)-components. Mixed derivatives of coordinate fields are zero by (C.1).

It follows that
\[
\begin{aligned}
R(X_i,Y_\alpha)X_j
 &=-\nabla_{Y_\alpha}\left(\sum_k\Gamma^k_{ij}(x)X_k\right)=0,\\
R(X_i,Y_\alpha)Y_\beta
 &=\nabla_{X_i}\left(\sum_\gamma
                   \Gamma^\gamma_{\alpha\beta}(y)Y_\gamma\right)=0.
\end{aligned}
\]
The omitted first or second terms in these two formulas vanish by (C.1), and the bracket terms vanish because coordinate fields commute. Similarly both iterated derivatives in \(R(X_i,X_j)Y_\alpha\) vanish, as do those in \(R(Y_\alpha,Y_\beta)X_i\). Curvature is a tensor in all three arguments by [Linear and affine connections, Theorem B.3](linear-and-affine-connections.md#theorem-b-3). Expanding arbitrary vectors in these coordinate bases proves (C.4).

The restriction of the connection to \(F\) along an \(E\)-leaf is well defined since \(F\) is parallel. In a product plaque its frame \(Y_\alpha\) has zero derivatives in all leaf directions by (C.1); its curvature is therefore zero. Equivalently it is the restriction of \(R(u,u')\) to \(F\), which vanishes by (C.4). The other statement is the same calculation with \(E,F\) interchanged. Flatness here means zero curvature; it does not assert trivial transport around every loop of a non-simply-connected leaf. □

## D. From local products to a global covering

Assume throughout this section that \(M\) is connected and complete and that \(TM=E\perp F\) is a parallel orthogonal splitting. Put \(r=\operatorname{rank}E\), \(s=\operatorname{rank}F\). An **adapted orthonormal frame** at \(q\) is an isometry \(u:\mathbb R^r\oplus\mathbb R^s\to T_qM\) taking the two summands to \(E_q,F_q\). Denote their bundle by \(Q\), its projection by \(\pi\), and its right structure group by \(O(r)\times O(s)\).

This is a smooth principal bundle. Indeed, apply the smooth orthogonalization proved in [Riemannian connections and convex neighbourhoods, Theorem F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2) separately to local frames of \(E,F\). Each adapted orthonormal frame is uniquely one resulting frame multiplied by a block diagonal orthogonal matrix. These local charts have smooth transition functions in \(O(r)\times O(s)\).

Write \(\theta\) for the solder form and \(\omega\) for the frame connection form, as constructed in [Linear and affine connections, Theorem H.2](linear-and-affine-connections.md#theorem-h-2). The connection restricts to \(Q\): transport preserves the metric and both subbundles by A.2. Equivalently its matrix in an adapted frame is block diagonal and skew-symmetric. For \(a\in\mathbb R^r\), \(b\in\mathbb R^s\), let \(B_E(a)\), \(B_F(b)\) be the horizontal fields on \(Q\) with solder values \((a,0)\), \((0,b)\), respectively.

**Lemma D.1 (complete commuting controlled motions).** A control \(a:[0,A]\to\mathbb R^r\) continuous on each piece of a finite subdivision, with continuous endpoint values on each piece, defines a global endpoint diffeomorphism \(\Phi_a^E:Q\to Q\) by
\[
U'(t)=B_E(a(t))_{U(t)}.
\tag{D.1}
\]
There is an analogous map \(\Phi_b^F\). They satisfy
\[
\Phi_a^E\Phi_b^F=\Phi_b^F\Phi_a^E.
\tag{D.2}
\]
Furthermore \(\Phi_b^F\) preserves every constant field \(B_E(v)\) and commutes with right multiplication by \(\operatorname{diag}(h,I_s)\), \(h\in O(r)\). The corresponding assertions hold with \(E,F\) interchanged. Endpoint maps depend smoothly on initial frames and on finite-dimensional parameters in the controls when all parameter derivatives are jointly continuous on a common finite time subdivision.

**Proof.** The integral \(\delta(t)=u_0\int_0^t(a(\tau),0)\,d\tau\) is a finite piecewise \(C^1\) curve in the initial tangent space. [Completeness and the Hopf–Rinow theorem, Theorem D.3](completeness-and-the-hopf-rinow-theorem.md#theorem-d-3) constructs its horizontal frame lift on the entire interval for every initial orthonormal frame \(u_0\). Because \(E,F\) are parallel, that lift stays adapted. The uniqueness assertion there identifies its equation with (D.1). This proves global existence and uniqueness for every control under consideration.

We record why its endpoint map is smooth even though the control need not be differentiable in time. In a frame chart the equation is \(z'=V(t,z,\lambda)\), where every derivative in \((z,\lambda)\) is jointly continuous. On a compact chart rectangle the integral operator
\[
T(w,z_0,\lambda)(t)=z_0+\int_0^t V(\tau,w(\tau),\lambda)\,d\tau
\]
is a contraction on a closed supremum-norm ball of continuous curves on a sufficiently short interval, takes its values in the ball's interior, and has contraction constant \(\epsilon L<1\). Here \(L\) bounds the spatial derivative and the interval length \(\epsilon\) is also chosen so the velocity bound leaves a positive spatial margin. Its derivatives of every order in the curve and the parameters are obtained by integrating the corresponding derivatives of \(V\). The segment formula in Local tools 0.3 bounds the error for differentiating each preceding derivative by
\[
\epsilon\,\eta(\|\Delta w\|_\infty+|\Delta\lambda|)
              (\|\Delta w\|_\infty+|\Delta\lambda|),
\qquad \eta(\rho)\longrightarrow0,
\]
using uniform continuity of the next coefficient derivative on a slightly larger compact rectangle. The same estimate proves continuity in the relevant multilinear operator norm. This is the detailed integral-operator argument of [Curvature and holonomy groups, Lemma C.2](curvature-and-holonomy-groups.md#lemma-c-2); it applies to the present smooth chart fields with precisely these coefficient hypotheses. Local tools Lemma 2.A then proves smooth dependence of the fixed point. Endpoint evaluation is linear and bounded, hence smooth. A finite chart subdivision of the compact reference trajectory composes these smooth local endpoint maps; shrinking the parameter neighbourhood at each of the finitely many steps keeps subsequent endpoints in their required charts. Thus the whole endpoint map is smooth.

The reversed control \(\bar a(t)=-a(A-t)\), with reversed subdivision, takes every solution back to its initial value, by the chain rule and uniqueness on each piece. It supplies a smooth inverse. The same statements hold for \(F\).

By Linear H.2, the horizontal and vertical components of a bracket of standard fields are minus torsion and minus curvature evaluated on their projections. Torsion is zero here. Corollary C.3 gives \(R(E,F)=0\), so
\[
[B_E(v),B_F(w)]=0
\tag{D.3}
\]
for all constant \(v,w\). The pair \((\theta,\omega)\) is injective on the tangent space of the full frame bundle, hence also on \(TQ\), so these vanishing components prove the bracket identity.

Let \(\Psi_t\) be the \(F\)-motion up to time \(t\). In coordinates, differentiating in the starting frame gives the variational equation
\[
\frac{d}{dt}\bigl(d\Psi_t\,B_E(v)\bigr)
 =D B_F(b(t))|_{\Psi_t}\bigl(d\Psi_t\,B_E(v)\bigr).
\]
On each time piece the smooth parameter result just proved justifies this derivative. Identity (D.3) implies that \(B_E(v)_{\Psi_t}\) satisfies the same linear equation and has the same initial value. Uniqueness for continuous time coefficients, Hopf–Rinow Lemma D.1, proves \((\Psi_t)_*B_E(v)=B_E(v)\). The identity passes across finitely many junctions by continuity.

Fix the complete endpoint map \(\Phi_b^F\). The curve \(t\mapsto\Phi_b^F(\Phi_{a|[0,t]}^E(u))\) solves the \(E\)-controlled equation with initial frame \(\Phi_b^F(u)\), because the endpoint map preserves every \(B_E(v)\). Uniqueness gives (D.2).

Finally Linear H.2 proves \(dR_k B(w)_u=B(k^{-1}w)_{uk}\). If \(k=\operatorname{diag}(h,I_s)\), then \(k^{-1}(0,b)=(0,b)\). Thus right multiplication by \(k\) carries an \(F\)-controlled solution to the solution with the same control starting at \(uk\). Uniqueness gives the claimed equivariance. Interchanging the two blocks proves the remaining assertions. □

Fix \(p\in M\), write \(L_E=L_E(p)\), \(L_F=L_F(p)\), and give these leaves their intrinsic metrics and topologies. Theorem C.2 makes both complete. Let \(q_E:\widetilde L_E\to L_E\) and \(q_F:\widetilde L_F\to L_F\) be their based smooth universal covers. Their existence, smoothness and path-class description are proved in [Flat connections and infinitesimal holonomy, Theorems D.2–D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2).

**Theorem D.2 (the product map on universal covers).** There is a smooth local isometry
\[
\mathcal P:\widetilde L_E\times\widetilde L_F\longrightarrow M
\tag{D.4}
\]
whose restrictions to the two based axes are \(i_Eq_E\) and \(i_Fq_F\), where \(i_E,i_F\) are the leaf inclusions. Its differential takes the tangent spaces of the two factors to \(E,F\), respectively.

**Proof.** Choose an adapted frame \(u_0\) at \(p\). Represent a point of \(\widetilde L_E\) by a finite piecewise smooth path \(\alpha\) in \(L_E\) starting at \(p\). Such representatives exist for every continuous path class by the coordinate-segment replacement in Flat E.1. Transport \(u_0\) along its image in \(M\), writing the resulting frame as \(U_\alpha(t)\). Since the path is tangent to \(E\), its frame coordinates satisfy
\[
U_\alpha(t)^{-1}\dot\alpha(t)=(a(t),0).
\]
Thus \(U_\alpha(1)=\Phi_a^E(u_0)\). A path \(\beta\) in \(L_F\) similarly gives a control \(b\) and frame \(U_\beta(1)=\Phi_b^F(u_0)\). Define
\[
\mathcal P([\alpha],[\beta])
 =\pi\bigl(\Phi_b^F\Phi_a^E(u_0)\bigr).
\tag{D.5}
\]
The endpoint maps exist globally by D.1.

We first prove independence of representatives; this is the essential global step. The connection on \(F\) restricted to \(L_E\) is flat by C.3. Its orthonormal frame connection is flat as well: in every product plaque the transverse coordinate fields are parallel along the leaf, so the connection matrix in that frame is zero. [Flat connections and infinitesimal holonomy, Theorem E.1](flat-connections-and-infinitesimal-holonomy.md#theorem-e-1) therefore makes its transport identical along endpoint-fixed homotopic paths in \(L_E\). If \(\alpha'\) represents \([\alpha]\), the frames \(U_{\alpha'}(1)\) and \(U_\alpha(1)\) lie over the same point and have identical \(F\)-columns. Their \(E\)-columns are two orthonormal bases of the same subspace. Hence
\[
U_{\alpha'}(1)=U_\alpha(1)\operatorname{diag}(h,I_s)
\]
for some \(h\in O(r)\). The equivariance in D.1 now gives the same value of (D.5) after applying \(\pi\). Notice that the two \(E\)-controls themselves need not be equal and their endpoint maps need not agree on all of \(Q\); only their values at \(u_0\) were used. To replace \(\beta\), write (D.5) in the order \(\pi\Phi_a^E\Phi_b^F(u_0)\) using (D.2), and apply the identical argument to the flat connection on \(E\) along \(L_F\). This proves well-definedness on both universal covers.

Here is both smoothness and the metric computation. Near \([\alpha]\), a sheet of the universal cover is parametrized by \(x\) in a small coordinate ball of \(L_E\), using \(\alpha\) followed by the coordinate radial path from \(x_0=\alpha(1)\) to \(x\). Let \(u(x)\) be the endpoint adapted frame transported along these concatenated paths. It is smooth by Curvature C.2. Its \(F\)-columns are parallel as sections over this ball: the flat transport theorem makes transport inside the ball independent of the path, so transport along any further short curve agrees with the same section. The transport derivative formula in Linear B.2 then makes its covariant derivative zero in every leaf direction.

Similarly near \([\beta]\), radial appended paths give \(F\)-controls \(b_y\) depending smoothly on \(y\) on a fixed finite subdivision. Their dependence follows by applying Curvature C.2 to the transported frame, then multiplying the smoothly varying path velocity by its inverse. D.1 gives smoothness of
\[
(x,y)\longmapsto \pi\Phi^F_{b_y}(u(x)),
\tag{D.6}
\]
which is (D.5) in these sheet coordinates. Such sheets cover the domain, proving smoothness everywhere.

Fix \(y\), abbreviate \(\Phi^F_{b_y}\) by \(\Psi\), and let \(v\in T_xL_E\). The tangent \(du(v)\in T_{u(x)}Q\) has solder value \((a_v,0)\), where \(u(x)(a_v,0)=di_E(v)\). Its connection value has zero \(F\)-block because the \(F\)-columns of \(u(x)\) are parallel. The horizontal-plus-vertical splitting therefore writes it uniquely as
\[
du(v)=B_E(a_v)_{u(x)}+\zeta_{\operatorname{diag}(A_v,0)}|_{u(x)},
\qquad A_v\in\mathfrak o(r).
\tag{D.7}
\]
Here \(\zeta\) is the fundamental vertical vector for the right action, as in Linear H.2. Lemma D.1 preserves the first term. Its right \(O(r)\)-equivariance preserves the second fundamental vector, by differentiating the right-action identity along \(\exp(t\operatorname{diag}(A_v,0))\). After projection the vertical term vanishes, leaving
\[
d\mathcal P(v,0)=\Psi(u(x))(a_v,0).
\tag{D.8}
\]
Thus \(d\mathcal P\) takes the first tangent summand isometrically onto \(E\).

For the second tangent summand, use the reversed order in (D.5) and the same argument with \(E,F\) interchanged. It is taken isometrically onto \(F\). These images are orthogonal and together have dimension \(\dim M\). Consequently the differential is an isometry on the whole product tangent space. The inverse-function theorem makes \(\mathcal P\) a local diffeomorphism, so it is a local isometry.

If \(\beta\) is the constant path, its control is zero and its endpoint map is the identity. Formula (D.5) then equals \(\alpha(1)=i_Eq_E[\alpha]\). The other axis follows in the same way. This completes the construction, including rank-zero factors, whose frames, controls and covering spaces have just the corresponding zero or one-point data. □

**Theorem D.3 (global two-factor splitting).** The local isometry (D.4) is a surjective smooth covering. If \(M\) is also simply connected, the leaves \(L_E,L_F\) through \(p\) are complete and simply connected, and there is a global isometry
\[
L_E\times L_F\longrightarrow M
\tag{D.9}
\]
restricting on each based axis to the leaf inclusion. Its differential respects the two given parallel distributions.

**Proof.** Equip each universal cover with the pullback leaf metric. Each covering map is a local isometry by its definition. The leaves are complete by C.2, and [Completeness and the Hopf–Rinow theorem, Corollary E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4) proves their universal covers complete.

The product of the two covers is connected and is a Hausdorff second-countable manifold: products of the two countable coordinate bases give a countable base, disjoint neighbourhoods in a differing coordinate separate distinct points, and coordinate charts are products. Paths in each factor combine to paths in the product, proving connectedness. It is geodesically complete. Indeed, the coordinate Levi-Civita formula of Riemannian A.1, applied to a block product metric, has no mixed Christoffel symbols and has the coefficients of each individual factor in its own block. The geodesic equation therefore separates into the two geodesic equations, each defined for all real times by Hopf–Rinow B.2. Another application of that theorem makes the product metrically complete. Corollary E.4 applied to D.2 now makes \(\mathcal P\) surjective and a smooth covering.

For clarity, any connected covering of a simply connected manifold is one-to-one. If two points over \(q\) were joined by a path upstairs, its projection would be a based loop at \(q\). Contract that loop keeping its endpoints fixed. The path-and-square lifting theorem, Flat D.1, lifts this contraction starting with the given path. The two side edges stay at its two endpoints. The top edge lifts a constant path and must itself be constant, so those endpoints are equal. A connected manifold is path connected by the coordinate-path argument in A.2, so this applies to every pair over \(q\). A bijective smooth covering has a smooth inverse given by its inverse branches.

When \(M\) is simply connected, \(\mathcal P\) is consequently a diffeomorphism and, being a local isometry, a global Riemannian isometry. Its restriction to a based axis is injective. The axis formula in D.2 then makes \(q_E\) injective, since \(i_E\) is an injective map of sets; it is already surjective. The same is true of \(q_F\). These are therefore diffeomorphisms and isometries from the simply connected covers to the leaves. Replacing the covers by the leaves in (D.4) yields (D.9), with the claimed axis and tangent properties. In particular these leaves are embedded in this case, as the images of product axes under a diffeomorphism. □

## E. The classical de Rham theorem

The **restricted holonomy group** is the subgroup obtained from loops homotopic to the constant loop with their base point fixed. The definitions and its Lie-group construction are in [Curvature and holonomy groups, Theorem C.5](curvature-and-holonomy-groups.md#theorem-c-5). The product and uniqueness arguments below only use its description by transport; no closed-subgroup assertion is needed.

**Lemma E.1 (holonomy of a Riemannian product).** For a finite product of connected Riemannian manifolds, full holonomy is the direct product of the full holonomy groups of the factors, acting separately on the tangent summands. Restricted holonomy is likewise the product of the restricted holonomy groups.

**Proof.** The block metric calculation in D.3 gives the factorwise connection. Along a path \(\gamma(t)=(\gamma_1(t),\ldots,\gamma_k(t))\), its parallel-vector equation separates into the factor equations. By transport uniqueness, the resulting map is
\[
P_\gamma=P_{\gamma_1}\oplus\cdots\oplus P_{\gamma_k}.
\tag{E.1}
\]
For a based loop this belongs to the product of the factor holonomies, proving one inclusion. Conversely, realize a given element of each factor holonomy by a loop in that factor while keeping all other coordinates constant. Concatenating these finitely many product loops gives the prescribed block tuple and proves the reverse inclusion.

A null homotopy of a product loop projects to null homotopies in every factor, so (E.1) proves one inclusion for restricted holonomy. For the other inclusion take a null-homotopic loop in one factor and contract it in that factor while keeping the other coordinates fixed. It is null-homotopic in the product. Concatenating such contractions gives the required product elements; explicitly, use the respective contraction in each successive time subinterval, whose endpoints all remain the base point. This proves the restricted assertion. An empty or point factor contributes the identity group. □

**Theorem E.2 (complete simply connected trivial holonomy).** A nonempty connected complete simply connected Riemannian manifold with trivial full holonomy is isometric to a Euclidean space of the same dimension.

**Proof.** Fix an orthonormal basis at \(p\). Transport each basis vector to \(q\) along any path from \(p\). Trivial loop holonomy makes the transported vector independent of the path. Radial paths in coordinate balls and Curvature C.2 make the resulting fields \(e_1,\ldots,e_n\) smooth. Appending a short path and using the derivative identity of Linear B.2 shows that every \(e_i\) is parallel. They remain an orthonormal frame by metric compatibility.

Torsion zero gives \([e_i,e_j]=0\). Each integral curve of \(e_i\) is a geodesic, since \(\nabla_{e_i}e_i=0\). Conversely the geodesic with initial velocity \(e_i(q)\) has that velocity field along it: both its velocity and \(e_i\) are parallel and have the same initial value, so transport uniqueness equates them. Completeness and Hopf–Rinow B.2 therefore make the flow \(\phi_i^t\) of each field defined for every real \(t\) and every initial point.

These complete flows commute for all real times. The variational identity in B.1 is valid along every finite portion of a flow: its proof solves the same linear variational equation in successive charts. Hence \((\phi_i^t)_*e_j=e_j\) for arbitrary finite \(t\); uniqueness for the \(e_j\)-equation then gives \(\phi_i^t\phi_j^s=\phi_j^s\phi_i^t\) for arbitrary finite \(s,t\). Define
\[
\mathcal E:\mathbb R^n\longrightarrow M,\qquad
\mathcal E(t_1,\ldots,t_n)=
\phi_n^{t_n}\circ\cdots\circ\phi_1^{t_1}(p).
\tag{E.2}
\]
It is smooth by the smooth flow theorem. Flow commutation gives \(d\mathcal E(\partial_{t_i})=e_i\), so the differential is an isometry. Local tools 1.2 makes it a local isometry. Euclidean space is complete by Local tools 0.1; its Riemannian distance is the usual Euclidean distance because a path has length at least its endpoint displacement by the integral triangle inequality of Local 0.3, while a straight segment attains equality. Hopf–Rinow E.4 now makes \(\mathcal E\) a surjective smooth covering. The simply connected target makes it injective by the lifting argument in D.3, and hence an isometry. If \(n=0\), connectedness makes \(M\) a point and the conclusion is immediate. □

**Theorem E.3 (de Rham decomposition and uniqueness).** Every nonempty connected complete simply connected Riemannian manifold is isometric to
\[
\mathbb R^d\times M_1\times\cdots\times M_k,
\tag{E.3}
\]
where the \(M_i\) have positive dimension, are complete and simply connected, and have nontrivial irreducible holonomy representations. Zero-dimensional factors are omitted. The Euclidean dimension and the isometry types of the non-Euclidean factors are unique up to permutation. At a fixed base point the Euclidean tangent subspace and the non-Euclidean tangent summands are intrinsic; their parallel distributions and foliations are therefore intrinsic up to the same permutation.

**Proof.** At \(p\), let \(H\) be full holonomy. Lemma A.1 gives
\[
T_pM=V_0\perp V_1\perp\cdots\perp V_k,
\qquad V_0=(T_pM)^H,
\tag{E.4}
\]
with the nonzero \(V_i\), \(i>0\), irreducible and with no fixed vectors. Their actions are nontrivial: an identity action would fix every vector in that nonzero subspace. Theorem A.2 extends (E.4) to parallel orthogonal distributions.

Apply D.3 first to one summand and its orthogonal complement. Both factors are complete and simply connected. Every remaining distribution is tangent to the complementary leaf; it restricts there to a parallel distribution for its induced connection, since C.2 identified that connection with ambient differentiation in tangent directions. The remaining restrictions still give its full orthogonal splitting. Repeat this operation a finite number of times. This yields a product of complete simply connected leaves with tangent spaces \(V_i\). By E.1 the holonomy of the product is exactly the product of their holonomies, each acting only on its own tangent summand. Thus the factor corresponding to \(V_0\) has trivial holonomy, and E.2 identifies it with \(\mathbb R^d\), \(d=\dim V_0\). On the other factors the holonomy representation is precisely the restriction of \(H\) in (E.4), hence is nontrivial and irreducible.

We give the uniqueness argument because an arbitrary orthogonal representation can have nonunique irreducible summands, as A.1 showed. For the decomposition just constructed, E.1 supplies subgroups \(H_i\subset H\) that act as the full holonomy on \(V_i\) and act as the identity on every other summand. Let \(W\subset T_pM\) be a nonzero irreducible \(H\)-invariant subspace on which \(H\) acts nontrivially. Orthogonal projection \(\pi_i:W\to V_i\) is \(H\)-equivariant: the summands and their complements are invariant, so applying an element of \(H\) commutes with the direct-sum projection.

The kernel of every \(\pi_i|_W\) is invariant. Irreducibility of \(W\) says that a nonzero projection is injective. The projection to \(V_0\) must be zero: otherwise injectivity and the identity action on \(V_0\) would force the action on \(W\) to be the identity. For \(i>0\), a nonzero projection has nonzero invariant image in the irreducible \(V_i\), so it is also surjective.

There must be a nonzero projection to some \(V_i\), since a vector whose every projection vanishes is zero. Suppose there were also a nonzero projection to \(V_j\), \(j\ne i\). Because \(H_i\) acts nontrivially on \(V_i\) and \(\pi_i(W)=V_i\), choose \(h\in H_i\) and \(w\in W\) such that \(h\pi_i(w)\ne\pi_i(w)\). Then \(hw-w\ne0\). But \(H_i\) fixes \(V_j\), so
\[
\pi_j(hw-w)=0,
\]
contradicting injectivity of \(\pi_j|_W\). Therefore \(W\) projects nontrivially onto exactly one \(V_i\) and is contained in it. Irreducibility of \(V_i\) then gives \(W=V_i\).

For any other product (E.3), E.1 shows that its Euclidean tangent space is exactly the fixed subspace of \(H\): each nontrivial irreducible factor has no fixed vector, since a nonzero fixed subspace would be invariant and force the entire irreducible action to be trivial. Its other tangent summands are irreducible nontrivial \(H\)-modules and so, by the preceding argument, are exactly the \(V_i\), in some order. This proves equality of the Euclidean dimensions and of the tangent splittings.

Theorem A.2 gives a unique parallel distribution from each invariant tangent subspace, and B.3 gives its unique maximal leaves. In a global product the leaf through \(p\) of one factor distribution is exactly its based axis: every tangent path has constant other coordinates, and every point on the axis can be reached by a path in that connected factor. The factor's metric is the induced leaf metric. Thus equality of distributions identifies the two sets of factor isometry types. If the comparison is through an isometry between two differently presented manifolds, pull one splitting back to the other: isometries preserve Levi-Civita connections and transport by [Riemannian connections and convex neighbourhoods, Theorem A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). The same argument applies. This proves all the stated uniqueness assertions. □

## F. Closedness of restricted Riemannian holonomy

Completeness was essential for the global product in D.3. The closedness result in this section needs only the local product identities C.3. We first prove the finite-dimensional group fact that supplies its algebraic step. An **immersed subgroup** is a subgroup with a Lie-group structure for which its inclusion is a smooth injective immersion; its topology is not initially assumed to be the subspace topology.

**Lemma F.1 (irreducible orthogonal subgroups).** Let \(V\ne0\) be a finite-dimensional real inner-product space. If a connected immersed Lie subgroup \(H\subseteq\mathrm O(V)\) acts irreducibly on \(V\), then its image is closed. Its given Lie-group structure agrees with the embedded subgroup structure, and it is compact.

**Proof.** The orthogonal group and its skew-adjoint Lie algebra were constructed in [Riemannian connections and convex neighbourhoods, Theorem F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2). Put \(K=\overline H\), with closure in \(\mathrm O(V)\). It is a subgroup: for sequences \(a_j\to a\), \(b_j\to b\) from \(H\), continuity gives \(a_jb_j^{-1}\to ab^{-1}\). Every point of the closure is such a sequential limit, by taking a point of \(H\) in each ball of radius \(1/j\). Thus \(ab^{-1}\in K\). By [Invariant connections on homogeneous bundles, Theorem A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1), this closed subgroup is embedded. Write
\[
\mathfrak h\subseteq\mathfrak k\subseteq\mathfrak{so}(V)
\]
for the two Lie algebras. The first inclusion holds because the image of every smooth curve in \(H\) is a curve in \(K\); in the embedded charts of \(K\) it is smooth, since the transverse coordinates vanish.

We use explicitly that a connected Lie group \(L\) is generated by \(\exp(\mathfrak l)\). The local exponential chart of [Local tools, Proposition 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) puts an open identity neighbourhood in this generated subgroup. Its translates show that the subgroup is open; all other cosets are open too, so it is also closed. Connectedness forces it to be all of \(L\). Exponentials commute with a smooth group homomorphism: applying its derivative to the left-invariant differential equation and using uniqueness, Local tools 2.1, gives the same equation in the target. Hence the exponentials of \(\mathfrak h\), regarded as matrices, generate the image \(H\).

Conjugation by \(H\) preserves \(\mathfrak h\), by differentiating its conjugation maps. Every finite-dimensional linear subspace is closed: after extending a basis, it is the common zero set of the complementary coordinate functions. Taking limits from \(H\) to \(K\) therefore gives
\[
\operatorname{Ad}(k)\mathfrak h=\mathfrak h
\quad(k\in K).
\tag{F.1}
\]
The reverse inclusion uses \(k^{-1}\). Differentiation along \(\exp(tY)\), \(Y\in\mathfrak k\), gives \([Y,\mathfrak h]\subseteq\mathfrak h\).

On skew-adjoint matrices the bilinear form
\[
(A,B)_*=-\operatorname{tr}_{\mathbb R}(AB)
\tag{F.2}
\]
is positive definite and invariant under orthogonal conjugation. In an orthonormal basis,
\(-\operatorname{tr}(A^2)=\sum_{i,j}A_{ij}^2\); and
\(\operatorname{tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=\operatorname{tr}(BA)\), which also proves the conjugation invariance by taking successive cyclic permutations of factors. Let \(\mathfrak m\) be the orthogonal complement of \(\mathfrak h\) inside \(\mathfrak k\). Finite-dimensional orthogonal projection gives
\(\mathfrak k=\mathfrak h\oplus\mathfrak m\). By (F.1) and invariance of (F.2), \(\mathfrak m\) is also \(\operatorname{Ad}(K)\)-invariant, so \([\mathfrak k,\mathfrak m]\subseteq\mathfrak m\). Both summands are ideals. In particular
\[
[\mathfrak h,\mathfrak m]\subseteq
\mathfrak h\cap\mathfrak m=\{0\}.
\tag{F.3}
\]
If \(Z\in\mathfrak m\) and \(X\in\mathfrak h\), differentiation of
\(\exp(tX)Z\exp(-tX)\) gives zero by (F.3). The expression is therefore \(Z\). Since these exponentials generate \(H\), every element of \(H\) commutes with \(Z\). This equality passes to the closure \(K\), and differentiating once more shows that \(Z\) commutes with every element of \(\mathfrak k\).

Suppose that \(\mathfrak m\ne0\), and choose nonzero \(Z\in\mathfrak m\). We need the following consequence of irreducibility. Any self-adjoint operator \(S\) commuting with \(H\) is scalar. Indeed its quadratic form attains a maximum \(\lambda=\langle Sv,v\rangle\) on the unit sphere, by the finite-dimensional compactness proved in Local tools 0.1. For \(w\perp v\), differentiate this quadratic form along \((v+tw)/\|v+tw\|\) at zero. Its derivative is \(2\langle Sv,w\rangle\), hence is zero. It follows that \(Sv=\lambda v\). The nonzero eigenspace \(\ker(S-\lambda I)\) is \(H\)-invariant; irreducibility makes it all of \(V\).

Apply this to \(S=Z^2\), which is self-adjoint and commutes with \(H\). Its scalar value is negative: for every \(v\),
\(\langle Z^2v,v\rangle=-\|Zv\|^2\), and for some \(v\) the right side is strictly negative because \(Z\ne0\). Thus
\[
Z^2=-c^2I,\qquad c>0,\qquad J=c^{-1}Z,\qquad J^2=-I.
\tag{F.4}
\]
Existence of the positive square root used here is Local tools 0.0. The map \(J\) is orthogonal and skew-adjoint and commutes with \(K\). Declare multiplication by \(i\) on \(V\) to be \(J\). This makes \(V\) a complex vector space of some positive complex dimension \(d\). For completeness, its compatible orthonormal basis can be constructed directly: choose a real unit vector \(e_1\); \(e_1,Je_1\) are orthonormal. Their orthogonal complement is \(J\)-invariant, since \(J\) is skew-adjoint. Repeat there. Each step removes two dimensions; a one-dimensional remainder cannot carry \(J^2=-I\). Hence the process ends with a real orthonormal basis \(e_1,Je_1,\ldots,e_d,Je_d\), and \(e_1,\ldots,e_d\) is a complex basis.

For a complex-linear real operator \(X\), its real matrix in these pairs has the blocks representing the real and imaginary parts of its complex matrix. In particular
\[
\operatorname{tr}_{\mathbb R}X
 =2\operatorname{Re}\operatorname{tr}_{\mathbb C}X,\qquad
\operatorname{tr}_{\mathbb R}(JX)
 =-2\operatorname{Im}\operatorname{tr}_{\mathbb C}X.
\tag{F.5}
\]
For \(X\in\mathfrak h\), the operator is complex-linear because it commutes with \(J\). Its real skew-adjointness says in this basis that its complex conjugate transpose is \(-X\), so its complex diagonal entries are purely imaginary. Orthogonality to \(Z=cJ\) in (F.2) gives \(\operatorname{tr}_{\mathbb R}(JX)=0\). Equation (F.5) therefore proves
\[
\operatorname{tr}_{\mathbb C}X=0\qquad(X\in\mathfrak h).
\tag{F.6}
\]

Here the determinant supplies a contradiction without any classification of real division algebras or compact Lie algebras. We include its required differential identity. Define the complex determinant by the signed permutation polynomial. It is the alternating multilinear function of the columns taking value one on the standard basis. Expanding columns in that basis proves that any alternating multilinear function is this determinant times its value on the standard basis. Applied to the columns after a fixed linear map \(A\), this proves \(\det(AB)=\det(A)\det(B)\). The same polynomial gives
\[
\det(I+sX+o(s))=1+s\operatorname{tr}_{\mathbb C}X+o(s):
\tag{F.7}
\]
the identity permutation contributes the sum of the diagonal linear terms, and every other nonzero term contains at least two off-diagonal entries.

For \(a(t)=\exp(tX)\), the exponential law and (F.7) imply
\[
\frac d{dt}\det_{\mathbb C}a(t)
 =\det_{\mathbb C}a(t)\operatorname{tr}_{\mathbb C}X.
\]
If \(X\in\mathfrak h\), (F.6) makes this derivative zero, and \(\det_{\mathbb C}a(0)=1\). Thus every generator of \(H\) has complex determinant one. Multiplicativity proves this for all of \(H\), and continuity of the determinant proves it for all of \(K\). But \(J\in\mathfrak m\subseteq\mathfrak k\), so \(\exp(tJ)\in K\) for every real \(t\). Its determinant is identically one, whereas (F.7) gives derivative at zero
\[
\operatorname{tr}_{\mathbb C}J=id\ne0.
\]
This contradiction proves \(\mathfrak m=0\), and hence \(\mathfrak h=\mathfrak k\).

The inclusion \(H\to K\) is smooth in the embedded charts of \(K\), as explained above. Its differential at the identity is now an isomorphism. Local tools 1.2 gives a diffeomorphism of a neighbourhood in \(H\) onto an open neighbourhood in \(K\). In particular \(H\) contains a \(K\)-open identity neighbourhood, so it is an open subgroup of \(K\), and hence closed in \(K\), since the other cosets are open. Its defining density forces \(H=K\). The same local inverse, translated around the group, shows that the given and embedded Lie-group structures agree. Finally \(\mathrm O(V)\) is a closed bounded set of real matrices: its defining equation is \(A^TA=I\), and every column has norm one. Local tools 0.1 makes it compact. Its closed subset \(H\) is compact too. This also covers a one-dimensional representation with the identity group. □

**Theorem F.2 (restricted holonomy is compact and closed).** Let \(M\) be any nonempty connected Riemannian manifold, without a completeness assumption. Its restricted Levi-Civita holonomy at \(p\) is a compact connected embedded Lie subgroup of \(\mathrm{SO}(T_pM)\). Its intrinsic holonomy Lie-group topology agrees with the subspace topology.

**Proof.** Take the smooth universal cover \(q:\widetilde M\to M\) constructed in [Flat connections and infinitesimal holonomy, Theorem D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2), and equip it with \(q^*g\). This is a positive smooth metric because \(q\) is a local diffeomorphism. Its Levi-Civita connection is locally the pullback of the one on \(M\): Riemannian A.3 proves preservation of the connection by a local isometry, and every covering chart is such an isometry. Thus parallel transport upstairs corresponds to transport downstairs under \(dq\).

Choose \(\widetilde p\) over \(p\). The full holonomy \(H\) of \(\widetilde M\), identified through \(dq_{\widetilde p}\), equals the restricted holonomy downstairs. A loop upstairs has a contraction, and projecting it gives a contraction downstairs. Conversely a null-homotopic loop downstairs lifts to a loop upstairs: lift its based null homotopy by [Flat connections, Lemma D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1); its endpoint, constrained to the discrete fibre and continuous through the homotopy, is the starting point. Smooth covering charts preserve the finite piecewise \(C^1\) regularity of these lifted loops. Transport correspondence proves both group inclusions. By Curvature C.5, \(H\) is a connected immersed Lie subgroup, since \(\widetilde M\) is simply connected. Nothing here asserts completeness of either manifold.

Apply A.1 to the orthogonal representation of \(H\) on \(V=T_{\widetilde p}\widetilde M\), and A.2 to transport its summands. This gives parallel orthogonal distributions
\[
T\widetilde M=E_0\perp E_1\perp\cdots\perp E_k,
\qquad
V_i=(E_i)_{\widetilde p},
\tag{F.8}
\]
where \(V_0=V^H\), and every \(V_i\), \(i>0\), is nonzero and irreducible. The action on each such \(V_i\) is nontrivial. Every vector of \(V_0\) extends to a global parallel vector field: transport it from \(\widetilde p\), with path independence because each based loop fixes that vector. The radial-chart smoothness and transport-derivative arguments of A.2 prove that this field is smooth and parallel. Transporting a basis gives a parallel frame for \(E_0\). Substituting a parallel field into the defining curvature formula shows
\[
R(u,v)|_{E_0}=0.
\tag{F.9}
\]

For each \(i\), apply C.3 to \(E_i\) and its parallel orthogonal complement. It gives zero mixed curvature and says that \(R(u_i,v_i)\), for \(u_i,v_i\in E_i\), annihilates every other summand. It preserves \(E_i\), since the connection does. For \(i=0\), (F.9) makes that operator zero on \(E_0\) too, and hence zero everywhere. Consequently for arbitrary tangent vectors decomposed along (F.8),
\[
R(u,v)=\sum_{i=1}^k R(u_i,v_i),
\qquad
R(u_i,v_i)\text{ acts only on }E_i.
\tag{F.10}
\]
These are local-product identities, valid on every chart of C.1; no global product or complete leaf is needed.

Write \(\mathfrak h\) for the actual holonomy algebra of \(H\). The complete curvature-generation theorem [Curvature, Theorem G.3](curvature-and-holonomy-groups.md#theorem-g-3), in the tangent form explicitly computed in [Theorem G.5](curvature-and-holonomy-groups.md#theorem-g-5), gives
\[
\mathfrak h=
\operatorname{span}_{\mathbb R}\{
P_\gamma^{-1}R_y(u,v)P_\gamma:
\gamma:\widetilde p\to y,\ u,v\in T_y\widetilde M\}.
\tag{F.11}
\]
This is equality of finite-dimensional linear spans, without a closure. Transport preserves (F.8). Each individual term obtained by taking both inputs in \(E_i\) is itself among the generators of (F.11), and acts only on \(V_i\). Formula (F.10) decomposes every other generator into these individual ones. It follows that
\[
\mathfrak h=\bigoplus_{i=1}^k\mathfrak h_i,\qquad
\mathfrak h_i=\{A\in\mathfrak h:
A|_{V_0\oplus\bigoplus_{j\ne i}V_j}=0\}.
\tag{F.12}
\]
Indeed the span of generators supported on each block is contained in the displayed \(\mathfrak h_i\); their sum is all of \(\mathfrak h\), and different supports have zero intersection. Each \(\mathfrak h_i\) is a Lie subalgebra: the commutator stays in \(\mathfrak h\) and has the same support. Distinct subalgebras commute because their matrix products in either order vanish.

Let \(H_i\) be the subgroup of \(\mathrm O(V_i)\) generated by all \(\exp(tA|_{V_i})\), \(A\in\mathfrak h_i\). These one-parameter maps are smooth, have connected domain \(\mathbb R\) and contain the identity. The complete subgroup-generation theorem [Curvature, Theorem C.1](curvature-and-holonomy-groups.md#theorem-c-1) makes \(H_i\) a connected immersed Lie subgroup. When extended by the identity on all other summands, it lies in \(H\), because its generators are exponentials of elements of \(\mathfrak h\).

Conversely any \(A\in\mathfrak h\) has a unique sum \(A=\sum_i A_i\) as in (F.12). Commutation gives
\(\exp(tA)=\prod_i\exp(tA_i)\): differentiation of the product yields the matrix equation \(U'=AU\), with \(U(0)=I\), whose uniqueness is Local tools 2.1. The connected-group generation argument proved in F.1 now gives
\[
H=\{I_{V_0}\}\times H_1\times\cdots\times H_k
\quad\text{as subgroups of }\mathrm O(V).
\tag{F.13}
\]
The action of \(H_i\) on \(V_i\) is irreducible. A subspace invariant under \(H_i\) is invariant under the entire \(H\) by (F.13), and A.1 made the latter action on \(V_i\) irreducible. Lemma F.1 thus makes every \(H_i\) closed in \(\mathrm O(V_i)\).

Equation (F.13) is a closed subgroup of \(\mathrm O(V)\). To check closedness directly, a convergent sequence of its matrices has zero off-diagonal blocks and identity \(V_0\)-block in the limit, while each \(V_i\)-block remains in the closed set \(H_i\). Since matrix space is a metric space this sequential test proves closedness. Compactness follows from compactness of \(\mathrm O(V)\), proved in F.1. Invariant connections A.1 gives the embedded subgroup structure. The identity from the intrinsic holonomy group to this embedded group is a bijective smooth homomorphism with injective differential: smoothness follows by restricting ambient coordinates to the embedded slice, and the differential remains injective because its composition with the ambient inclusion is the original immersion. [Curvature, Lemma G.1](curvature-and-holonomy-groups.md#lemma-g-1) proves that such a map between these second-countable Lie groups is a diffeomorphism. This also proves the asserted equality of topologies and embedded connectedness.

Finally an orthogonal matrix has real determinant in \(\{1,-1\}\), by determinant multiplicativity applied to \(A^TA=I\). The determinant is continuous and \(H\) is connected; a continuous map into these two separated points is constant, since their inverse images are disjoint open-and-closed sets. Its value at the identity is one, so \(H\subseteq\mathrm{SO}(V)\). If \(k=0\), (F.11)–(F.12) give \(\mathfrak h=0\) and connected exponential generation gives \(H=\{I\}\), with all the same conclusions. A zero-dimensional manifold is included in this case. Transport by \(dq_{\widetilde p}\) returns the stated result at \(p\). □

## G. Affine transport, fixed points and completeness

We use the **normalized affine connection** associated to the Levi-Civita connection. Its construction is [Linear and affine connections, Theorems E.2–E.3](linear-and-affine-connections.md#theorem-e-2). In particular its translational connection form is the solder form; it is not an arbitrary connection on the affine-frame bundle.

For a path \(\gamma:[0,1]\to M\), write \(P_{st}\) for linear transport along it from time \(s\) to time \(t\). The affine transport between its tangent spaces is
\[
\mathcal F_\gamma(v)
 =P_{01}\left(v-\int_0^1P_{t0}\dot\gamma(t)\,dt\right).
\tag{G.1}
\]
The integral is taken separately on the finitely many smooth pieces. [Linear, Theorem F.1](linear-and-affine-connections.md#theorem-f-1) proves this formula and its inverse, concatenation and parameter identities. Equivalently, affine transport along the path solves \(D_t w=-\dot\gamma\). Denote by \(A_p\) the group of the maps (G.1) for all loops at \(p\), and by \(A_p^0\) the subgroup for null-homotopic loops. They act on the affine space underlying \(T_pM\). Their linear parts are respectively \(H_p\) and \(H_p^0\), by Linear E.3. These definitions distinguish normalized affine holonomy from linear holonomy throughout this section.

**Lemma G.1 (fixed affine points and vector fields).** Evaluation at \(p\) gives a bijection between smooth vector fields \(V\) satisfying
\[
\nabla_XV=-X\qquad\text{for every vector field }X
\tag{G.2}
\]
and points of \(T_pM\) fixed by every element of \(A_p\). No completeness or simple-connectivity assumption is needed.

**Proof.** Suppose \(v\in T_pM\) is fixed by \(A_p\). For \(q\in M\) choose a finite piecewise smooth path \(\gamma:p\to q\), whose existence was proved in A.2, and define \(V(q)=\mathcal F_\gamma(v)\). If \(\eta\) is another such path, then \(\mathcal F_\eta^{-1}\mathcal F_\gamma\) is the transport of the loop obtained by traversing \(\gamma\) and then \(\eta^{-1}\). It fixes \(v\), so the two definitions agree.

This field is smooth. On a coordinate ball, use a fixed stem to its centre followed by the radial coordinate segment to its variable endpoint. Smooth dependence of principal transport on these endpoints, [Curvature, Lemma C.2](curvature-and-holonomy-groups.md#lemma-c-2), applies to the affine-frame connection as to any finite-dimensional structure group. Evaluation of the transported affine frame on the fixed initial point is smooth by Linear F.1. This gives a smooth local formula for \(V\) on each such ball.

Append any path starting at \(q\) to a path used to define \(V(q)\). Path independence and concatenation show that \(V\) is carried to its new value by affine transport. By [Linear, Theorem F.2](linear-and-affine-connections.md#theorem-f-2), this is exactly (G.2).

Conversely (G.2) makes \(V\) parallel as an affine point field by that same theorem, or directly by uniqueness for \(D_t w=-\dot\gamma\). Every loop at \(p\) therefore fixes \(V(p)\). Transport from \(p\) determines every value of any such field, proving injectivity, and the construction from \(v\) proves surjectivity. □

**Theorem G.2 (a complete manifold with a fixed affine point).** If \(M\) is complete, \(A_p\) has a fixed point if and only if \(M\) is globally isometric to Euclidean space. Simple connectivity is a conclusion, not a hypothesis.

**Proof.** In dimension zero, a nonempty connected manifold is a point, and the assertion holds. Suppose its dimension is positive and \(A_p\) fixes a point. Lemma G.1 gives \(V\) satisfying (G.2). We prove the global conclusion directly.

Along a geodesic \(c\), the velocity is parallel, and the transport derivative formula in Linear B.2 integrates (G.2) to
\[
V(c(s))=P_{0s}\bigl(V(c(0))-s\dot c(0)\bigr).
\tag{G.3}
\]
Here all geodesics are defined for every real \(s\), by [Hopf–Rinow, Theorem B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2). In particular the geodesic from any point \(z\) with initial velocity \(V(z)\), denoted \(c_z\), satisfies \(V(c_z(1))=0\). Choose one such zero \(q\).

The vector field \(V\) has a flow for every real time. Indeed (G.3) for \(c_z\) says \(V(c_z(s))=(1-s)\dot c_z(s)\). Consequently
\[
\phi_t(z)=c_z(1-e^{-t})
\tag{G.4}
\]
satisfies \(\partial_t\phi_t(z)=V(\phi_t(z))\) and \(\phi_0(z)=z\), for all \(t\in\mathbb R\). The exponential function and its derivative and multiplication laws are proved in Local tools 0.5. Smooth dependence of the complete geodesics on their initial vector, [Geodesics, Theorem A.2](geodesics-normal-coordinates-and-curvature.md#theorem-a-2), makes (G.4) smooth in \(t,z\). ODE uniqueness, Local tools 2.1, gives \(\phi_{t+s}=\phi_t\phi_s\) and \(\phi_{-t}=\phi_t^{-1}\). Thus these are global diffeomorphisms, and \(\phi_t(q)=q\).

The flow scales the metric by an exact factor. If \(a(s)\) is a curve with \(a(0)=z\) and \(a'(0)=u\), differentiate the variation \(\phi_t(a(s))\) in \(s\). Its field \(J(t)=d\phi_t(u)\) obeys
\[
D_tJ=\nabla_JV=-J.
\tag{G.5}
\]
The first equality follows from zero torsion and the commuting parameters \(s,t\), in the precise along-map formula of [Linear, Lemma D.3](linear-and-affine-connections.md#lemma-d-3). For another initial vector \(w\), metric compatibility and (G.5) give
\[
\frac d{dt}g_{\phi_t(z)}(d\phi_tu,d\phi_tw)
 =-2g_{\phi_t(z)}(d\phi_tu,d\phi_tw).
\]
Multiplying by \(e^{2t}\) and differentiating proves
\[
\phi_t^*g=e^{-2t}g.
\tag{G.6}
\]

Let \(E:T_qM\to M\) be the global exponential \(E(v)=\exp_q(v)\), available by geodesic completeness. Along \(c(s)=\exp_q(sv)\), (G.3) starts with \(V(q)=0\), so \(V(c(s))=-s\dot c(s)\). For any fixed positive initial parameter, \(t\mapsto c(e^{-t})\) is therefore the \(V\)-trajectory through \(c(1)=E(v)\); this calculation is valid for every \(v\), including zero. Flow uniqueness proves
\[
\phi_t(E(v))=E(e^{-t}v).
\tag{G.7}
\]
Surjectivity of \(E\) follows from Hopf–Rinow B.2, which provides a geodesic from \(q\) to any prescribed point, reparametrized to time one by Geodesics A.2.

To prove injectivity, suppose \(E(v)=E(w)\). For sufficiently large \(t\), both \(e^{-t}v\) and \(e^{-t}w\) lie in the normal-coordinate ball on which \(E\) is injective, provided by [Geodesics, Theorem B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). Equation (G.7) gives equality of their images, hence \(e^{-t}v=e^{-t}w\) and \(v=w\).

It remains to identify the metric; bijectivity alone would not suffice. Put \(h=E^*g\), a smooth symmetric tensor on the vector space \(T_qM\), without yet assuming that \(dE\) is invertible away from zero. For \(a=e^{-t}>0\), (G.6)–(G.7), with \(D_a(v)=av\), give
\[
D_a^*h=a^2h.
\]
Because \(dD_a=aI\), this identity reads
\[
h_{av}(u,w)=h_v(u,w)
\qquad(v,u,w\in T_qM).
\tag{G.8}
\]
Let \(a\downarrow0\). Smoothness makes the left side tend to \(h_0(u,w)\). Geodesics B.1 proves \(dE_0=I\), so \(h_0=g_q\). Thus (G.8) proves that \(h\) is the constant Euclidean inner product \(g_q\) everywhere. In particular \(dE_v\) is an isometry at every \(v\), and is invertible because the dimensions agree. The inverse-function theorem makes \(E\) a local diffeomorphism. Its already proved bijectivity makes the local inverses one global smooth inverse. Hence \(E\) is a global Riemannian isometry from the Euclidean space \((T_qM,g_q)\) onto \(M\). Euclidean space is simply connected: its straight homotopy to the origin contracts every loop, so \(M\) is also simply connected.

Conversely, in Euclidean coordinates \(V(x)=-x\) satisfies (G.2), since the Levi-Civita connection of the constant metric has zero coefficients by Riemannian A.1. Lemma G.1 gives a fixed affine point. A global isometry preserves the Levi-Civita connection by Riemannian A.3, so this also proves the converse for any manifold isometric to Euclidean space. □

**Corollary G.3 (restricted fixed points).** For complete \(M\), the group \(A_p^0\) has a fixed point if and only if the universal Riemannian cover of \(M\) is Euclidean. In that case \(M\) is locally Euclidean. Conversely, every locally Euclidean Riemannian manifold, complete or incomplete, has trivial restricted normalized affine holonomy.

**Proof.** Take the smooth universal cover with the pullback metric, as in F.2. It is complete when \(M\) is complete, by [Hopf–Rinow, Corollary E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4). Formula (G.1) commutes with a Riemannian covering: its differential intertwines linear transports and path velocities, and hence also their integrals. The loop-lifting argument of F.2 therefore identifies full affine holonomy upstairs with \(A_p^0\) downstairs, by the differential at the chosen lift of \(p\). A fixed point is carried to a fixed point under this linear identification. Theorem G.2 makes the complete cover Euclidean, and its local isometry charts make \(M\) locally Euclidean.

For the converse statement, suppose \(M\) is locally Euclidean. Its Levi-Civita curvature is zero in each Euclidean chart, because the connection coefficients there vanish, so curvature is zero globally. Torsion is zero for a Levi-Civita connection. Linear E.3 identifies the curvature of the normalized affine connection in a zero-origin frame as
\[
\widehat\Omega=
\begin{pmatrix}\Omega&\Theta\\0&0\end{pmatrix}.
\tag{G.9}
\]
Both entries vanish. Curvature equivariance extends this zero value from the zero-origin frames to every affine frame, so this principal connection is flat. [Curvature, Theorem G.6](curvature-and-holonomy-groups.md#theorem-g-6) makes its restricted holonomy trivial, without any completeness hypothesis. If the universal Riemannian cover is Euclidean, its covering charts make \(M\) locally Euclidean and the same conclusion supplies the remaining direction of the equivalence. □

**Theorem G.4 (the irreducible affine alternative).** Suppose \(\dim M>1\) and \(H_p^0\) acts irreducibly on \(T_pM\). Exactly one of the following holds: \(A_p^0\) contains every translation of \(T_pM\), or \(A_p^0\) fixes a point of that affine space. In the first case
\[
A_p^0=H_p^0\ltimes T_pM.
\tag{G.10}
\]
If \(M\) is complete, only the translation case occurs.

**Proof.** Put \(V=T_pM\), \(H=H_p^0\) and \(A=A_p^0\), using a zero-origin orthonormal affine frame to identify their actions with matrices. Curvature C.5 gives connected immersed Lie-group structures to both groups. F.2 makes \(H\) compact and embedded. The projection to the linear part maps \(A\) onto \(H\), by Linear E.3.

We also need surjectivity on the Lie algebras; surjectivity on sets will not be used as an unproved substitute for it. Let \(\mathfrak a\) and \(\mathfrak h\) be their algebras, and \(\rho(B,v)=B\). Linear E.3 proves on all affine frames that the upper-left block of the connection form is the pullback of the linear-frame connection. Taking exterior derivatives and block products proves the same statement for curvature. Every linearly reachable frame has an affinely reachable lift, by transporting the initial affine frame along the same path. Moreover, tangent inputs to the curvature downstairs can be lifted through the linear-part map on the frame bundles: in the coordinates of Linear E.1 that map is \((x,a,c)\mapsto(x,a)\), a submersion. Thus the linear parts of the curvature values at affinely reachable frames are exactly the curvature values at linearly reachable frames. Apply Curvature G.3's complete curvature-span theorem to both principal connections. Since a linear map commutes with finite linear spans, it gives
\[
\rho(\mathfrak a)=\mathfrak h.
\tag{G.11}
\]

Let
\[
W=\{w\in V:(0,w)\in\mathfrak a\}
\]
be the vector space of infinitesimal translations. It is \(H\)-invariant. Indeed conjugation of the affine infinitesimal matrix \((0,w)\) by an affine element \((h,b)\in A\) is \((0,hw)\), by the block multiplication in Linear E.1. Conjugation preserves \(\mathfrak a\), and every \(h\in H\) has such a lift. Irreducibility gives \(W=V\) or \(W=0\).

If \(W=V\), the exponential of \((0,w)\) is translation by \(w\), as follows directly by solving the affine matrix equation. Every such exponential belongs to \(A\), so all translations occur. For any \(h\in H\), choose \((h,b)\in A\). Left composition with translation by \(v-b\) gives \((h,v)\) for any \(v\in V\). This proves (G.10).

Suppose instead that \(W=0\). By (G.11), the restriction \(\rho:\mathfrak a\to\mathfrak h\) is then a linear isomorphism. There is a linear map \(f:\mathfrak h\to V\) such that
\[
\mathfrak a=\{(X,f(X)):X\in\mathfrak h\}.
\]
The affine bracket computed in Linear E.1 shows exactly that
\[
f([X,Y])=Xf(Y)-Yf(X).
\tag{G.12}
\]
We prove directly that this particular cocycle has a fixed affine origin.

Equip \(\mathfrak h\subseteq\mathfrak{so}(V)\) with the positive conjugation-invariant inner product \(-\operatorname{tr}(XY)\) proved in F.1, and choose an orthonormal basis \(E_1,\ldots,E_m\). The group \(H\) is nontrivial: an identity action in dimension greater than one leaves a nonzero proper line invariant. Its Lie algebra is nonzero too, by connected exponential generation from F.1. Thus \(m>0\). Define
\[
C=\sum_{j=1}^m E_j^2,\qquad
s=\sum_{j=1}^m E_j f(E_j).
\tag{G.13}
\]
Conjugation by \(h\in H\) changes the \(E_j\)'s by an orthogonal basis matrix. Expanding the sum of the squares and using \(\sum_j b_{ij}b_{kj}=\delta_{ik}\) shows \(hCh^{-1}=C\). Each \(E_j\) is skew-adjoint, so \(C\) is self-adjoint. The self-adjoint commutant argument proved inside F.1 therefore gives \(C=-\lambda I\) for a scalar \(\lambda\). In fact
\[
\langle Cv,v\rangle=-\sum_j\|E_jv\|^2.
\]
Since some \(E_j\ne0\), there is \(v\) for which this is strictly negative; hence \(\lambda>0\).

For \(X\in\mathfrak h\), invariance of the trace inner product says that \(\operatorname{ad}X\) is skew-adjoint: differentiate conjugation by \(\exp(tX)\) in the equality of inner products. Write
\[
[X,E_j]=\sum_i b_{ij}E_i,\qquad b_{ij}=-b_{ji}.
\]
Using (G.12) in \(Xs=\sum_j X E_j f(E_j)\) gives
\[
\begin{aligned}
Xs
&=\sum_j[X,E_j]f(E_j)
 +\sum_jE_j f([X,E_j])
 +\sum_jE_j^2 f(X)\\
&=C f(X)=-\lambda f(X).
\end{aligned}
\tag{G.14}
\]
For clarity, the first two sums cancel: their sum is
\(\sum_{i,j}b_{ij}\bigl(E_i f(E_j)+E_j f(E_i)\bigr)\), which is zero on interchanging \(i,j\) and using skew-symmetry. Thus the point \(v_*=s/\lambda\) satisfies
\[
Xv_*+f(X)=0\qquad(X\in\mathfrak h).
\tag{G.15}
\]
The one-parameter affine group generated by \((X,f(X))\) solves \(y'=Xy+f(X)\) on \(V\). The constant curve \(y=v_*\) solves this equation by (G.15); ODE uniqueness makes that entire one-parameter group fix \(v_*\). Every element of the connected group \(A\) is a finite product of its exponentials, by the argument in F.1. Hence all of \(A\) fixes \(v_*\).

These alternatives are mutually exclusive: on nonzero \(V\), translation by any nonzero \(w\) fixes no point. Finally, if \(M\) is complete and the fixed-point case held, G.3 would make its universal Riemannian cover Euclidean. Parallel transport in a Euclidean constant frame is the identity around every loop. F.2's covering correspondence would then make \(H_p^0\) trivial, contradicting irreducibility in dimension greater than one. This leaves precisely the translation case in the complete setting. □

## H. Recovering factors from parallel symmetric forms

Throughout this section \(M\) is nonempty, connected, complete and simply connected. By E.3 it has a de Rham splitting with Euclidean distribution \(E_0\) of rank \(r\) and nontrivial irreducible distributions \(E_1,\ldots,E_k\). Put \(F=E_0^\perp\). Let \(P_i\) be orthogonal projection onto \(E_i\), and extend the metric of each non-Euclidean factor by zero on the other distributions:
\[
g_i(u,v)=g(P_i u,P_i v),\qquad 1\le i\le k.
\tag{H.1}
\]
The reconstruction by parallel symmetric forms is described in Anton S. Galaev's [exact arXiv:1611.01554v1, §3, Proposition 1](https://arxiv.org/abs/1611.01554v1). We prove the tensor correspondence, factor separation and spectral steps needed here.

**Theorem H.1 (parallel vectors and symmetric tensors).** Evaluation at a point identifies the space of parallel vector fields with the holonomy-fixed tangent subspace \((E_0)_p\). Every parallel self-adjoint endomorphism of \(TM\) has exactly the form
\[
S=S_0\oplus\lambda_1 I_{E_1}\oplus\cdots\oplus\lambda_k I_{E_k},
\qquad \lambda_i\in\mathbb R,
\tag{H.2}
\]
where \(S_0\) is an arbitrary constant self-adjoint operator in a parallel orthonormal frame of \(E_0\). Conversely every such choice gives a parallel self-adjoint field. Parallel symmetric bilinear forms are exactly \(b(u,v)=g(Su,v)\) for these \(S\). Their dimension is \(r(r+1)/2+k\); on \(F\) their space has basis \(g_1|_F,\ldots,g_k|_F\).

**Proof.** A parallel vector field is preserved by transport, by Linear A.2, so its value at \(p\) is fixed by every holonomy loop and determines all its other values. Conversely transport a fixed vector from \(p\) along any path. The fixed-vector condition makes the result independent of the path, and the radial-chart smoothness and derivative argument in A.2 makes it a smooth parallel field. Thus evaluation is a linear bijection onto the fixed subspace. By E.3 this is exactly \((E_0)_p\). Transporting an orthonormal basis gives a global parallel orthonormal frame of \(E_0\).

We establish the corresponding endomorphism statement explicitly. [Linear and affine connections, Theorem C.1](linear-and-affine-connections.md#theorem-c-1) proves that endomorphism transport is
\[
T\longmapsto P_\gamma T P_\gamma^{-1}.
\tag{H.3}
\]
If \(T\) is parallel, its value at \(p\) therefore commutes with every holonomy element. Conversely, if \(T_p\) commutes with all holonomy, (H.3) defines \(T_q\) independently of the path from \(p\) to \(q\): the two transports differ by holonomy at \(p\). Radial paths make it smooth by Curvature C.2. Appending any path transports it to its new value; the induced derivative and the transport derivative formula in Linear C.1 and B.2 then give \(\nabla T=0\). This proves the bijection between parallel endomorphisms and the commutant of holonomy. Metric transport also shows that self-adjointness at \(p\) is equivalent to self-adjointness everywhere.

Write \(V_i=(E_i)_p\). By E.1–E.3 the holonomy group acts as
\[
H=\{I_{V_0}\}\times H_1\times\cdots\times H_k,
\tag{H.4}
\]
where \(H_i\) is nontrivial and irreducible on \(V_i\), and is the identity on every other summand. A commuting operator \(S_p\) sends every fixed vector to a fixed vector, so preserves \(V_0\). If it is self-adjoint, it also preserves \(V_0^\perp\): for \(u\perp V_0\) and \(v\in V_0\), \(\langle Su,v\rangle=\langle u,Sv\rangle=0\).

Consider a block \(T_{ji}:V_i\to V_j\) of \(S_p\) with distinct \(i,j>0\). Commutation with the independent \(H_i\)-action gives
\[
T_{ji}h=T_{ji}\qquad(h\in H_i).
\]
Its kernel is \(H_i\)-invariant. If \(T_{ji}\ne0\), irreducibility would force this kernel to be zero, so the displayed equality would make every \(h\in H_i\) the identity, contrary to nontriviality. Thus all such blocks vanish. The block on each \(V_i\) is self-adjoint and commutes with \(H_i\). The maximization and invariant-eigenspace argument in F.1 proves that this block is \(\lambda_i I\). On \(V_0\) the identity action imposes no commutation restriction, so every self-adjoint block \(S_0\) is allowed. The values of \(\lambda_i\) are constants because (H.3) carries each scalar block to the same scalar block at every point. In the transported frame of \(E_0\), (H.3) likewise keeps the matrix of \(S_0\) constant. This proves necessity in (H.2).

The orthogonal projections \(P_i\) are parallel. Indeed write a field as the sum of its sections in the parallel distributions; differentiation preserves each summand by A.2, and therefore commutes with its projection. Constant matrix coefficients in the parallel frame of \(E_0\), together with these parallel projections, now construct every field in (H.2) and prove its parallelness. Its blocks are self-adjoint, proving sufficiency.

For every bilinear form \(b\) there is a unique field \(S\) with \(b(u,v)=g(Su,v)\): in a local basis this follows by solving with the invertible Gram matrix of \(g\). Its inverse is smooth by Local tools 0.4, so smooth \(b\) gives smooth \(S\), and conversely. Symmetry of \(b\) is exactly self-adjointness of \(S\). Applying Linear C.1's tensor and contraction rules and \(\nabla g=0\) gives
\[
(\nabla_Xb)(u,v)=g((\nabla_XS)u,v).
\]
Nondegeneracy of \(g\) proves that one field is parallel exactly when the other is. A real symmetric \(r\)-by-\(r\) matrix has \(r\) freely chosen diagonal entries and \(r(r-1)/2\) freely chosen entries above the diagonal, with the others determined. Equation (H.2) consequently gives dimension \(r(r+1)/2+k\).

The same argument applies to the induced connection on \(F\). More explicitly, a parallel form on \(F\) extends to \(TM\) by
\(b(u,v)=b_F(P_Fu,P_Fv)\). Since \(P_F\) is parallel, this extension is parallel and zero on the Euclidean block. Its classification is therefore precisely \(\sum_i\lambda_i g_i\). These forms are independent: evaluating a linear combination on a nonzero vector of \(E_j\) leaves only \(\lambda_j g(v,v)\), so its vanishing forces \(\lambda_j=0\). They span by (H.2), proving the final assertion. □

**Theorem H.2 (spectral reconstruction at one point).** The space of parallel vector fields determines \(E_0\). Given any complete basis \(b_1,\ldots,b_k\) of the parallel symmetric bilinear forms on \(F=E_0^\perp\), finite-dimensional linear algebra at one point recovers all the nontrivial de Rham distributions, up to permutation, and their factor metrics.

**Proof.** H.1 identifies the evaluations of all parallel vector fields with \(E_0\) at every point. Thus their span determines this bundle and its orthogonal complement \(F\). If \(F=0\), there are no nontrivial factors and the assertion is immediate. Otherwise fix \(p\), put \(W=F_p\), and form the self-adjoint operators \(S_\alpha\) defined by
\[
b_\alpha(u,v)=g(S_\alpha u,v)
\quad(u,v\in W),\qquad 1\le\alpha\le k.
\tag{H.5}
\]
Only the values of the forms and metric at \(p\) are needed for these linear equations.

We first prove the needed real spectral theorem. A self-adjoint operator \(T\) on a nonzero finite-dimensional real inner-product space has an eigenvector: maximize \(\langle Tv,v\rangle\) on the unit sphere, using Local tools 0.1. At a maximizing unit vector \(v\), differentiation along \((v+tw)/\|v+tw\|\), \(w\perp v\), gives \(\langle Tv,w\rangle=0\). Hence \(Tv=\lambda v\), with \(\lambda=\langle Tv,v\rangle\in\mathbb R\). Self-adjointness makes \(v^\perp\) invariant, because \(\langle Tw,v\rangle=\langle w,Tv\rangle=0\). Induction on dimension gives an orthonormal basis of eigenvectors. Eigenspaces with distinct eigenvalues are orthogonal, since
\((\lambda-\mu)\langle u,v\rangle=\langle Tu,v\rangle-\langle u,Tv\rangle=0\).
Grouping the basis vectors by their eigenvalues proves the orthogonal eigenspace decomposition. The zero-dimensional case uses an empty basis.

By H.1 the operators in (H.5) have expressions
\[
S_\alpha=\sum_{i=1}^k c_{\alpha i}P_i|_W.
\tag{H.6}
\]
Although the \(P_i\)'s are the unknowns to be recovered, this proves that the known operators \(S_\alpha\) commute. Start with the single subspace \(W\). Decompose it into eigenspaces of \(S_1\). Next, on each resulting subspace take the eigenspaces of \(S_2\), and continue through \(S_k\). Each restriction is legitimate: if \(S_\beta v=\lambda v\) and \(S_\alpha\) commutes with \(S_\beta\), then \(S_\beta(S_\alpha v)=\lambda S_\alpha v\). Thus every earlier joint eigenspace is invariant under the next operator. The restriction remains self-adjoint, so the just-proved spectral theorem applies. There are \(k\) stages and at most \(\dim W\) nonzero summands at any stage; the procedure is finite.

Every original factor space \(V_i=(E_i)_p\) stays in one joint eigenspace, because each \(S_\alpha\) acts on it by the scalar \(c_{\alpha i}\). Distinct factors cannot remain in the same final subspace. Indeed \(g_1|_F,\ldots,g_k|_F\) and \(b_1,\ldots,b_k\) are both bases by H.1, so the coefficient matrix \(C=(c_{\alpha i})\) is invertible. If its \(i\)-th and \(j\)-th columns agreed, then \(C(e_i-e_j)=0\), contradicting invertibility. Some operator therefore has different eigenvalues on \(V_i,V_j\), and its stage separates them. Conversely, a vector decomposed into the \(V_i\)'s is a joint eigenvector with a prescribed eigenvalue tuple only when all its nonzero components have that tuple, by (H.6). The final nonzero joint eigenspaces are consequently exactly the \(V_i\)'s, up to their order.

Recover the factor forms at \(p\) as \(g(P_{V_i}\,\cdot,P_{V_i}\,\cdot)\), where the projections are obtained from this orthogonal splitting. Restricting each known \(S_\alpha\) to \(V_i\) gives the numbers \(c_{\alpha i}\). Inverting their matrix gives constants \(d_{i\alpha}\) such that
\[
g_i=\sum_{\alpha=1}^k d_{i\alpha}b_\alpha
\quad\text{on }F.
\tag{H.7}
\]
These equalities first hold at \(p\). Both sides are parallel, and a parallel tensor is determined by its value at one point by (H.3) and H.1. They therefore hold globally. Extend each side by zero on \(E_0\); the resulting global forms satisfy
\[
E_i=(\ker g_i)^{\perp_g},
\qquad
\ker g_i=\{u:g_i(u,v)=0\text{ for every }v\}.
\tag{H.8}
\]
To verify this formula, decompose \(u\) into its \(E_j\)-components. Pairing against the \(E_i\)-component itself shows that \(g_i(u,\cdot)=0\) exactly when that component is zero, since the metric is positive. Hence its kernel is precisely the sum of the other distributions. Formula (H.8) recovers each distribution everywhere from the known forms and the constants found at \(p\). Its restriction \(g_i|_{E_i}\) is the factor metric. Their maximal leaves and the global product are then the ones already proved in B.3 and E.3.

The eigenvalue requirement in this procedure is essential. For \(T=\operatorname{diag}(1,3)\) and \(v=(1,1)\), the Rayleigh quotient is \(\langle Tv,v\rangle/\langle v,v\rangle=2\), but \(T-2I=\operatorname{diag}(-1,1)\) is invertible, with determinant \(-1\). Thus choosing an arbitrary vector's quotient does not necessarily produce a kernel or a finer decomposition. The eigenspace procedure above uses the proved spectral theorem and has the stated separation property. □

## I. Worked tests of the decomposition

**Exercise I.1 (a fixed line between two curved factors).** On \(S^2\times\mathbb R\times S^2\), use the metric \(4g_{S^2}+dt^2+9g_{S^2}\). Determine full and restricted linear holonomy, the holonomy-fixed subspace, and whether a commuting linear map can mix the two sphere tangent spaces.

**Solution.** Multiplication of a metric by a positive constant does not change its Levi-Civita connection. The original torsion-free connection preserves the new metric because the constant differentiates to zero; uniqueness in Riemannian A.1 proves the assertion. Thus both scaled sphere factors have the full and restricted holonomy \(\mathrm{SO}(2)\) proved in [Geodesics, Example F.3](geodesics-normal-coordinates-and-curvature.md#example-f-3). Rescaling an orthonormal basis by \(1/2\) or \(1/3\) only rescales both vectors of that tangent plane equally, so it does not change their holonomy matrices. The line has zero connection coefficients and identity transport in the frame \(\partial_t\).

By E.1, in the tangent splitting \(V_1\perp\mathbb R\partial_t\perp V_2\), both groups are
\[
\{\operatorname{diag}(R_\alpha,1,R_\beta):
R_\alpha,R_\beta\in\mathrm{SO}(2)\}.
\tag{I.1}
\]
The two rotations vary independently. A vector fixed by all of them has zero \(V_1\)-component, by taking \(R_\alpha=-I\), and zero \(V_2\)-component, by taking \(R_\beta=-I\). Hence the fixed subspace is precisely \(\mathbb R\partial_t\), of dimension one.

For any linear map commuting with (I.1), a block \(T:V_1\to V_2\) satisfies \(T(-I)=T\), by taking the first rotation to be \(-I\) and the second to be \(I\). Thus \(-T=T\) and \(T=0\). The reverse block vanishes by interchanging the rotations. This argument does not assume the whole map is self-adjoint. Equal dimensions of the two tangent planes do not permit their mixing while commuting with every independent holonomy action. □

**Exercise I.2 (complete leaves on a diagonal cylinder).** Let \(M=\mathbb R^2/\mathbb Z(1,1)\) with its quotient Euclidean metric. Let \(E,F\) be the descended horizontal and vertical distributions. Determine their leaves through \([0,0]\), their intrinsic metrics, and the product covering, and prove that \(M\) is not their product.

**Solution.** The orthogonal coordinates
\[
u=(x-y)/\sqrt2,\qquad v=(x+y)/\sqrt2
\]
turn translation by \((1,1)\) into translation by \((0,\sqrt2)\). Thus \(M\) is the flat cylinder \(\mathbb R\times(\mathbb R/\sqrt2\mathbb Z)\) whose smooth quotient, covering charts and completeness are proved in [Hopf–Rinow, Exercise F.3](completeness-and-the-hopf-rinow-theorem.md#exercise-f-3). The descended coordinate fields are parallel because the covering is a local isometry and the Euclidean coordinate fields are parallel. Hence \(E,F\) are the orthogonal parallel distributions in C.1.

The based horizontal leaf is
\[
L_E=\{[s,0]:s\in\mathbb R\},
\]
with parametrization \(s\mapsto[s,0]\). It is injective: \([s,0]=[s',0]\) would give \((s-s',0)=m(1,1)\) for an integer \(m\), whose second coordinate forces \(m=0\). Every finite piecewise smooth \(E\)-tangent path from the base point lifts through the covering to a path starting at \((0,0)\), by Flat D.1. Its second coordinate has derivative zero on every piece and is therefore constantly zero, by Local tools 0.3 and continuity at the joins. Conversely the horizontal segment reaches every displayed point. The maximal-leaf construction in B.3 therefore gives exactly this set. In a small quotient chart, the parametrization and its inverse are the horizontal coordinate on the plaque, so it is a diffeomorphism from \(\mathbb R\) onto the leaf with its intrinsic plaque topology. The induced metric is \(ds^2\). Interchanging the coordinates gives
\[
L_F=\{[0,t]:t\in\mathbb R\}
\]
with intrinsic metric \(dt^2\). Both leaves are consequently complete and simply connected.

The horizontal and vertical Euclidean motions commute, so the product map constructed in D.2–D.3 is here explicitly
\[
\Phi:L_E\times L_F\cong\mathbb R^2\longrightarrow M,
\qquad
\Phi(s,t)=[s,t].
\tag{I.2}
\]
It is the quotient covering and a local isometry. Its fibres are exactly the translates by the diagonal integer vectors \((m,m)\); in particular it is not injective.

To distinguish \(M\) from the product even as a manifold, consider the based loop \(c(t)=[t,t]\), \(0\le t\le1\). Its lift to \(\mathbb R^2\) from \((0,0)\) ends at \((1,1)\). A based null homotopy would lift by Flat D.1 to a square whose endpoint edge is a continuous path in the discrete fibre. That edge is constant, but at the constant-loop side its endpoint is \((0,0)\), contradicting the endpoint \((1,1)\). Thus this loop is not null-homotopic. In \(\mathbb R^2\) every based loop \(a\) contracts by \((s,t)\mapsto(1-s)a(t)+s a(0)\). A homeomorphism transports such contractions, so \(M\) is not homeomorphic, and in particular not isometric, to \(L_E\times L_F\). □

**Exercise I.3 (a contracting centre outside the manifold).** On \(\mathbb R^2\setminus\{0\}\) with the Euclidean metric, take \(V(x)=-x\). Verify (G.2), compute full normalized affine holonomy and the all-time flow, and identify the failed step of G.2.

**Solution.** The constant metric has zero Levi-Civita coefficients, so \(\nabla_XV=dV(X)=-X\). Linear transport is the identity in the global coordinate frame. Therefore the development in (G.1) along any path is
\[
\int_0^1\dot\gamma(t)\,dt=\gamma(1)-\gamma(0),
\]
by the fundamental theorem of calculus on its pieces. For a loop this is zero, so every full affine holonomy element is the identity. The full group, and consequently its restricted group, is trivial.

The vector-field equation \(x'=-x\) has solution
\[
\phi_t(x)=e^{-t}x,\qquad t\in\mathbb R.
\tag{I.3}
\]
It never reaches zero at finite time and stays in the punctured plane, so the vector field is complete. Uniqueness is Local tools 2.1, and the formula also verifies the flow law directly.

The manifold itself is incomplete, as proved in [Hopf–Rinow, Example F.1](completeness-and-the-hopf-rinow-theorem.md#example-f-1). More specifically, the geodesic \(c_x(s)=x+sV(x)=(1-s)x\) starting at nonzero \(x\) cannot be evaluated at \(s=1\) as a point of the manifold. G.2 used geodesic completeness at exactly this step to obtain a point \(q\) with \(V(q)=0\). Here the limit lies at the removed origin, and the field has no zero on the manifold. Formula (I.3) tends to that missing point as \(t\to+\infty\); an all-time contracting flow alone does not supply the centre required in G.2. □

**Exercise I.4 (eigenspaces and the unique nontrivial factors).** For the de Rham product \(\mathbb R^r\times M_1\times\cdots\times M_k\), classify parallel self-adjoint endomorphism fields and determine whether their eigenspaces can produce a different nontrivial irreducible parallel decomposition.

**Solution.** By H.1 these fields are exactly (H.2), with an arbitrary constant real symmetric operator \(S_0\) on the Euclidean tangent space and arbitrary real constants \(\lambda_i\) on the nontrivial factors. For any real number \(\lambda\), the eigenspace at \(p\) is explicitly
\[
\ker(S_p-\lambda I)=\ker(S_0-\lambda I_{V_0})
\oplus\bigoplus_{\{i:\lambda_i=\lambda\}}V_i.
\tag{I.4}
\]
Indeed the operator is block diagonal; setting \((S_p-\lambda I)v=0\) independently sets each block equation to zero, and the scalar blocks vanish precisely at the displayed indices. The spectral theorem proved in H.2 gives an orthogonal decomposition of \(V_0\) into its \(S_0\)-eigenspaces. Formula (I.4) then describes all eigenvalues and their full eigenspaces.

These eigenspaces are holonomy-invariant because \(S_p\) commutes with holonomy. They extend to parallel distributions by A.2. Repeated constants may therefore group several nontrivial factors, and Euclidean eigenspaces may occur with that same eigenvalue. However, E.3 proves that every nontrivial irreducible holonomy-invariant subspace is one of the original \(V_i\)'s. Thus no further irreducible parallel splitting of these eigenspaces can replace those nontrivial factors by different ones. Linear combinations of vectors from two blocks with equal eigenvalue are still eigenvectors, but the lines or mixed subspaces they span need not be holonomy-invariant, so eigenvector choice alone does not produce a new parallel decomposition.

The Euclidean part has a different freedom: its holonomy is the identity, so every subspace is invariant and gives a parallel constant distribution. Irreducible subspaces for this trivial action are the lines, since a higher-dimensional space has a nonzero proper line. Every orthogonal decomposition of the Euclidean space into lines is allowed, and symmetric matrices can have different such eigendirections. The de Rham theorem makes the entire Euclidean factor intrinsic, not a preferred collection of axes within it. □

## J. Deck transformations and the global Euclidean factor

The universal cover can have more Euclidean directions than the manifold itself. A translation can prevent a direction from being a global line factor even though its derivative fixes that direction. The displacement criterion in J.2 is due to Jost-Hinrich Eschenburg and Ernst Heintze; see [their freely accessible institutional postprint, §2, Lemma 1, printed page 3076](https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/deliver/index/docId/25299/file/25299.pdf). We prove the isometry splitting, quotient construction and maximality needed to apply it.

**Lemma J.1 (isometries of the Euclidean and non-Euclidean product).** Let \(\widetilde M\) be a nonempty complete connected simply connected Riemannian manifold. Write the product supplied by E.3 as
\[
\widetilde M=E\times N,\qquad E=\mathbb R^r,
\tag{J.1}
\]
where \(N\) has no Euclidean de Rham factor. Every isometry \(\phi\) has the form
\[
\phi(x,y)=(Ax+b,\psi(y)),
\qquad A\in O(E),\quad b\in E,\quad\psi\in\operatorname{Isom}(N).
\tag{J.2}
\]
The assertion includes \(r=0\) and a point factor \(N\).

**Proof.** Isometries preserve the Levi-Civita connection by [Riemannian connections, Theorem A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Thus pushforward by \(\phi\) takes parallel vector fields to parallel vector fields; its inverse has the same property. H.1 identifies the values of all such fields with \(TE\) at every point of (J.1). Consequently \(d\phi\) carries \(TE\) onto \(TE\). Since it preserves the metric, it also carries the orthogonal complement \(TN\) onto \(TN\).

Write \(\phi=(a,\psi)\) temporarily allowing both components to depend on \((x,y)\). The derivative of \(a\) in every \(N\)-direction is zero. Two points of a connected manifold can be joined by a finite piecewise smooth path: the set reachable from a point is open using coordinate balls, and its complement is open by the same argument, so connectedness makes it the whole manifold. The chain rule on each segment of such a path in \(N\) makes \(a(x,y)\) independent of \(y\). Likewise \(d\psi\) is zero in \(E\)-directions, so \(\psi(x,y)\) is independent of \(x\). Hence \(\phi(x,y)=(a(x),\psi(y))\).

Bijectivity of this product map implies bijectivity of both factors. For example, surjectivity onto a chosen pair supplies a preimage of either coordinate; if \(a(x)=a(x')\), comparison at any fixed \(y\) and injectivity of \(\phi\) give \(x=x'\). The same argument works for \(\psi\). Applying the preceding splitting argument to the smooth inverse shows that both inverse factor maps are smooth. Restricting the metric identity for \(\phi\) to \(TE\) and \(TN\) shows that \(a\) and \(\psi\) are isometries of their factors.

An isometry preserves affinely parametrized geodesics, again by Riemannian A.3. Put \(b=a(0)\) and \(A=da_0\). The Euclidean geodesic \(t\mapsto tx\) must therefore be sent to the Euclidean geodesic with initial value \(b\) and velocity \(Ax\), namely \(t\mapsto b+tAx\). At \(t=1\) this gives \(a(x)=Ax+b\). The derivative metric identity at zero gives \(A^*A=I\), proving (J.2). These arguments also apply to the unique maps on a zero-dimensional point factor. □

**Theorem J.2 (maximal global Euclidean factor).** Let \(M\) be a nonempty complete connected Riemannian manifold, without a simple-connectivity assumption. Equip its universal cover \(q:\widetilde M\to M\) with the lifted metric and write its de Rham product as (J.1). Let \(\Gamma\) be its full deck group. By J.1 write
\[
\gamma(x,y)=(A_\gamma x+b_\gamma,\gamma_N(y)).
\]
Choose an origin in \(E\), and define the linear subspaces
\[
W=\operatorname{span}\{A_\gamma x+b_\gamma-x:
                   \gamma\in\Gamma,\ x\in E\},
\qquad V=W^\perp.
\tag{J.3}
\]
There is a complete connected Riemannian manifold \(B\) and a global product isometry
\[
M\cong V\times B.
\tag{J.4}
\]
The manifold \(B\) has no positive-dimensional global Euclidean factor. Every global Euclidean factor of \(M\) has tangent distribution contained in that of \(V\); hence the maximal Euclidean factor distribution and its foliation are unique. Its dimension is \(\dim V\).

**Proof.** The universal covering construction and its deck group, free action, orbit fibres and disjoint-sheet neighborhoods are proved in [Flat connections, Lemma D.1 and Theorems D.2–D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2). The pulled-back metric makes \(q\) a local isometry. Completeness of the cover follows from [Hopf–Rinow, Corollary E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4), so E.3 applies to \(\widetilde M\). Every deck transformation is an isometry because
\(\gamma^*q^*g=(q\circ\gamma)^*g=q^*g\). Thus J.1 applies to each \(\gamma\).

Let \(\pi_V\) denote orthogonal projection onto \(V\). Definition (J.3) gives
\[
\pi_V(A_\gamma x+b_\gamma)=\pi_Vx\qquad(x\in E).
\tag{J.5}
\]
Taking \(x=0\) gives \(b_\gamma\in W\), and subtraction yields \(\pi_VA_\gamma=\pi_V\). For \(v\in V\) and \(x\in E\), the latter identity says
\[
\langle A_\gamma^*v,x\rangle
=\langle v,A_\gamma x\rangle
=\langle v,x\rangle.
\]
Thus \(A_\gamma^*v=v\), and orthogonality gives \(A_\gamma v=v\). Moreover \(A_\gamma W=W\), since for \(w\perp V\) one has
\(\langle A_\gamma w,v\rangle=\langle w,A_\gamma^*v\rangle=0\);
equality follows from invertibility, or by applying the same argument to \(\gamma^{-1}\). Relative to \(E=V\oplus W\), the action therefore is
\[
\gamma(v,w,y)=(v,A_\gamma w+b_\gamma,\gamma_N(y)).
\tag{J.6}
\]
Put \(P=W\times N\). Formula (J.6) defines an action of \(\Gamma\) on \(P\) by isometries. It is free: an element fixing \(p\in P\) would fix \((0,p)\in\widetilde M\), and a deck transformation fixing one point is the identity by Flat D.1.

We construct \(B=P/\Gamma\) with its quotient topology and prove the required manifold and metric properties. Write \(\pi:P\to B\) for the orbit map. This map is open, since for open \(U\subset P\) the set
\(\pi^{-1}(\pi(U))=\bigcup_{\gamma\in\Gamma}\gamma U\) is open. The rule
\[
\iota:B\longrightarrow M,\qquad \iota([p])=q(0,p)
\tag{J.7}
\]
is well-defined and continuous by the definition of the quotient topology. It is injective because the fibres of \(q\) are the \(\Gamma\)-orbits. Distinct points of \(B\) therefore have disjoint open neighborhoods, obtained by pulling back disjoint neighborhoods of their images in the Hausdorff manifold \(M\). Thus \(B\) is Hausdorff. The manifold \(P\) is second countable, and the images under the open map \(\pi\) of a countable base form a countable base for \(B\): given an open set containing \([p]\), choose a base set containing \(p\) inside its open inverse image. Hence \(B\) is second countable as well.

For each \(p\in P\), take a neighborhood of \((0,p)\) in \(\widetilde M\) disjoint from all its nonidentity deck translates, using Flat D.2. It contains a product \(U_V\times U_P\), where \(0\in U_V\), \(p\in U_P\), and \(U_P\) is a coordinate neighborhood in \(P\). Equation (J.6) implies
\[
U_P\cap\gamma U_P=\varnothing\qquad(\gamma\ne1);
\tag{J.8}
\]
otherwise \(U_V\times U_P\) would meet its corresponding deck translate. Thus \(\pi|_{U_P}\) is a homeomorphism onto the open set \(\pi(U_P)\), and
\(\pi^{-1}(\pi(U_P))=\coprod_{\gamma\in\Gamma}\gamma U_P\).
These sets give covering charts. Their transition maps are locally restrictions of a fixed element of \(\Gamma\): if \(z\in U_P\) and \(\gamma z\in U'_P\), shrink to \(U_P\cap\gamma^{-1}U'_P\); the unique representatives there are related by \(\gamma\). Consequently they are smooth isometries for the metric of \(P\). The quotient charts define a smooth structure on \(B\) and a Riemannian metric for which \(\pi\) is a smooth local-isometry covering.

The factors \(W\) and \(N\) are complete. Product geodesics solve the two separate factor equations, by D.3 and E.1, so geodesics of \(P\) exist for all real times. Hopf–Rinow B.2 makes \(P\) metrically complete. Hopf–Rinow E.4 then makes \(B\) complete. Both factors of \(P\) are connected, so \(P\) is connected, and its continuous image \(B\) is connected.

Now define
\[
\Phi:V\times B\longrightarrow M,\qquad
\Phi(v,[p])=q(v,p).
\tag{J.9}
\]
Equation (J.6) makes this well-defined. Surjectivity follows from surjectivity of \(q\). If two inputs have the same image, their lifts differ by a deck transformation; (J.6) forces their \(V\)-coordinates to agree and their \(P\)-coordinates to be in the same orbit. Thus \(\Phi\) is injective. In the quotient charts just constructed it is locally \(q\) applied to the product coordinates of \(V\times P=\widetilde M\). Since \(q\) is a local isometry, so is \(\Phi\). A bijective local diffeomorphism has a smooth inverse: its local smooth inverses agree wherever both are defined. Thus (J.9) is the global product isometry (J.4).

To prove maximality, suppose any other global product isometry expresses \(M\) as \(\mathbb R^s\times C\). Denote its Euclidean coordinate functions by \(f_1,\ldots,f_s\). Their gradients are orthonormal parallel vector fields, as follows directly from the product connection in D.3 and E.1. Pulling back by the local isometry \(q\) gives orthonormal parallel gradients of \(\widetilde f_j=f_j\circ q\). By H.1 each of these is a constant vector \(a_j\in E\), with zero \(N\)-component. Hence
\[
\widetilde f_j(x,y)=\langle a_j,x\rangle+c_j.
\tag{J.10}
\]
Indeed the difference of the two sides has zero differential; integration along the finite piecewise smooth paths used in J.1 makes it constant on the connected product, and its value at one point fixes \(c_j\).

Deck invariance of \(\widetilde f_j\) and (J.10) give
\[
\langle a_j,A_\gamma x+b_\gamma-x\rangle=0
\quad\hbox{for every }x\in E,\ \gamma\in\Gamma.
\]
By (J.3), every \(a_j\) lies in \(V\). The tangent directions of the other Euclidean factor are the span of these gradients, so they are contained in the distribution obtained from \(TV\) by \(dq\). In particular \(s\le\dim V\), and (J.4) attains this bound. When equality holds, the tangent distributions coincide. Their leaves coincide by the maximal-leaf characterization B.3, proving uniqueness of the Euclidean foliation. If \(B\) had a positive-dimensional Euclidean product factor, (J.4) would give a larger Euclidean factor of \(M\), contradicting the bound. Finally, changing the chosen origin in \(E\) changes coordinate representatives but not the geometric displacement vectors in (J.3); the resulting distribution is also intrinsic by the maximality argument. No finite-generation assumption on \(\Gamma\) was used. □

**Exercise J.3 (the maximal line in the diagonal cylinder).** For the flat quotient
\[
M=\mathbb R^2/\langle(x,y)\mapsto(x+1,y+1)\rangle,
\]
compute the subspaces \(W,V\), give its global Euclidean product decomposition, and determine the length of its circle factor.

**Solution.** I.2 and [Hopf–Rinow, Exercise F.3](completeness-and-the-hopf-rinow-theorem.md#exercise-f-3) give the complete smooth quotient and its Euclidean universal covering. Its deck transformations are the translations by \(m(1,1)\), \(m\in\mathbb Z\). Thus
\[
W=\mathbb R(1,1),\qquad V=\mathbb R(1,-1).
\]
The orthonormal change of coordinates
\[
u=\frac{x-y}{\sqrt2},\qquad v=\frac{x+y}{\sqrt2}
\]
takes the metric to \(du^2+dv^2\) and the generator to
\((u,v)\mapsto(u,v+\sqrt2)\). It therefore induces the product isometry
\[
M\cong\mathbb R_u\times(\mathbb R_v/\sqrt2\mathbb Z).
\tag{J.11}
\]
More explicitly, the quotient coordinate map is well-defined because it has precisely the displayed identification, is bijective on orbits, and is a local isometry in the quotient charts; its local inverse proves that it is a global isometry. The unit-speed interval \(v\in[0,\sqrt2]\) traverses the circle once, so integration of its constant speed gives circle length \(\sqrt2\). J.2 shows that the \(u\)-direction is the unique maximal Euclidean distribution. The coordinate lines from I.2 were parallel totally geodesic leaves, but their pair did not descend to two global Euclidean factors; (J.11) gives the actual global line factor. □

**Exercise J.4 (a screw quotient with a parallel direction but no line factor).** Let \(R_\theta\in SO(2)\) be a planar rotation different from the identity, and let
\[
\gamma(x,t)=(R_\theta x,t+1),\qquad (x,t)\in\mathbb R^2\times\mathbb R.
\]
Construct the complete flat quotient \(M=\mathbb R^3/\langle\gamma\rangle\). Compute its full and restricted linear holonomy, and show that it has no positive-dimensional global Euclidean factor despite having a nonzero parallel vector field.

**Solution.** Induction for positive and negative integers gives
\[
\gamma^n(x,t)=(R_{n\theta}x,t+n).
\tag{J.12}
\]
These are Euclidean isometries, and none with \(n\ne0\) fixes a point, because it changes \(t\) by \(n\). Every open Euclidean ball of radius less than \(1/3\) is disjoint from all its nonidentity translates: its \(t\)-coordinate interval has length less than \(2/3\), whereas translating that interval adds a nonzero integer.

We verify that the orbit space is a manifold rather than assuming a quotient theorem. Its orbit map \(q\) is open, since saturations of open sets are unions of open translates. To prove Hausdorffness, choose points \(z=(x,t)\) and \(z'=(x',t')\) in distinct orbits. Choose an integer \(K>|t-t'|+2\). For \(|n|>K\), the distance \(|z-\gamma^n z'|\) is greater than \(2\), by its \(t\)-component. For the finitely many \(|n|\le K\), these distances are all positive because the orbits are distinct. Choose
\[
0<\varepsilon<
\min\left\{\frac14,\frac14\min_{|n|\le K}|z-\gamma^n z'|\right\}.
\]
If \(q(B_\varepsilon(z))\) met \(q(B_\varepsilon(z'))\), there would be \(a\in B_\varepsilon(z)\), \(b\in B_\varepsilon(z')\), and an integer \(n\) with \(a=\gamma^n b\). The isometry and triangle inequalities would give
\(|z-\gamma^n z'|<2\varepsilon\), contradicting either the finite minimum or the bound for \(|n|>K\). Thus these two open images are disjoint. Images of a countable Euclidean base give a countable base of the quotient, just as in J.2. The disjoint-translate balls give coordinate charts, their transitions are restrictions of the isometries (J.12), and these charts make \(q\) a Riemannian local-isometry covering. The local metric is Euclidean, hence flat. Completeness follows from completeness of \(\mathbb R^3\) and Hopf–Rinow E.4.

Straight-line homotopies contract every based loop in \(\mathbb R^3\), so this is a simply connected covering and is the universal cover by Flat D.3. Its full deck group is exactly the displayed cyclic group: any deck map takes a chosen point to a point in its orbit, hence agrees there with one \(\gamma^n\); uniqueness of lifts in Flat D.1 makes the two deck maps equal everywhere.

The Euclidean factor of the universal cover is all of \(\mathbb R^3\). The generator's displacement vectors are
\[
\gamma(x,t)-(x,t)=((R_\theta-I)x,1).
\tag{J.13}
\]
The choice \(x=0\) puts \((0,1)\) in their span. Subtracting this vector shows that the span contains
\(\operatorname{im}(R_\theta-I)\times\{0\}\). A nonidentity planar rotation fixes no nonzero vector: in an oriented orthonormal basis beginning with a proposed fixed unit vector, its rotation matrix would have first column \((1,0)\), forcing \(\cos\theta=1\) and \(\sin\theta=0\), and hence the identity matrix. Thus \(R_\theta-I\) is injective; finite-dimensional linear algebra makes it surjective on \(\mathbb R^2\). Equation (J.13) therefore spans \(\mathbb R^3\), so \(W=\mathbb R^3\) and \(V=0\). J.2 rules out a positive-dimensional global Euclidean factor.

For completeness compute the holonomy with its identifications. Fix \(z\in\mathbb R^3\) over \(p\in M\) and identify \(T_pM\) with \(\mathbb R^3\) using \(dq_z\). Any based piecewise smooth loop has a unique lift beginning at \(z\), ending at \(\gamma^n z\) for some integer \(n\), by Flat D.1. Local isometries preserve parallel transport by Riemannian A.3, and upstairs Euclidean parallel transport keeps a vector \(w\) constant. Since \(q\circ\gamma^n=q\), its endpoint represents the vector
\[
(dq_z)^{-1}dq_{\gamma^n z}w
=d\gamma^{-n}w
=\operatorname{diag}(R_{-n\theta},1)\,w.
\tag{J.14}
\]
Conversely the straight segment from \(z\) to \(\gamma^n z\) projects to a based loop, so every matrix in (J.14) occurs. Hence
\[
\operatorname{Hol}_p(M)
=\{\operatorname{diag}(R_{n\theta},1):n\in\mathbb Z\}.
\tag{J.15}
\]
For a null-homotopic loop, square lifting of its based contraction in Flat D.1 makes the lifted endpoint equal to \(z\); (J.14) is then the identity. Therefore restricted holonomy is trivial. The fixed subspace of (J.15) is exactly the \(t\)-axis, by the nonidentity-rotation argument above.

The constant unit field \(\partial_t\) is invariant under every \(d\gamma^n\), so it descends through the covering charts to a smooth unit parallel vector field on \(M\). Nevertheless \(t\) itself does not descend to a real coordinate, since \(t\circ\gamma=t+1\). The orbit of this field through \(q(0,0)\) is already periodic with period \(1\), as \(q(0,s+1)=q(0,s)\); equality at two parameters forces their difference to be an integer by (J.12). The full displacement condition (J.3) detects this translation and correctly gives no line factor, even though linear holonomy fixes the direction. □

## K. Global decomposition without simple connectivity

A connected positive-dimensional Riemannian manifold is **globally indecomposable** if it is not isometric to a product of two positive-dimensional connected Riemannian manifolds. This condition concerns a global product; it need not be equivalent to irreducibility of holonomy. We will distinguish them explicitly in K.7.

The theorem in this section is due to Jost-Hinrich Eschenburg and Ernst Heintze. Their [Augsburg institutional postprint](https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/deliver/index/docId/25299/file/25299.pdf), §2, Lemmas 2–3 and the ensuing proof, supplies the common-refinement and short-generator method. We establish all covering, metric, intersection and quotient assertions used by that method.

For a product \(X=\prod_{i=1}^sX_i\), write \(X_i(z)\) for the factor leaf through \(z\): all coordinates except the \(i\)-th remain fixed. An isometry is **supported on \(X_i\)** if it has the form
\[
(x_1,\ldots,x_s)\longmapsto
(x_1,\ldots,x_{i-1},a_i(x_i),x_{i+1},\ldots,x_s)
\]
for an isometry \(a_i\) of \(X_i\). An identity map is supported on any factor. The following proofs allow point factors and empty products, the latter interpreted as a point.

**Lemma K.1 (product distance, universal covers and quotient products).** The following assertions hold.

1. A finite Riemannian product of nonempty connected manifolds is complete if and only if all its factors are complete. For complete factors its distance satisfies
\[
d_{\prod X_i}(x,y)^2=\sum_i d_{X_i}(x_i,y_i)^2.
\tag{K.1}
\]
2. The product of the Riemannian universal covers of the factors of a connected product \(M=\prod_iM_i\) is a Riemannian universal cover of \(M\). Under this identification its deck group is the product of the factor deck groups; each individual factor deck group acts only on its own factor.
3. Suppose \(q:X\to M\) is a Riemannian universal cover, \(M\) is complete and connected, and \(X=\prod_iX_i\) is a finite Riemannian product. This product descends to a global product of \(M\), with these lifted factor foliations, if and only if the deck group \(\Gamma\) is generated by elements each supported on a single \(X_i\). In that case, with
\[
\Gamma_i=\{\gamma\in\Gamma:\gamma\text{ is supported on }X_i\},
\]
one has
\[
\Gamma=\prod_i\Gamma_i,\qquad
M\cong\prod_i(X_i/\Gamma_i),
\tag{K.2}
\]
and every quotient factor is a complete connected Riemannian manifold.

**Proof.** The product connection and geodesic equations separate, as proved in D.3 and E.1. If all factors are complete, each component geodesic exists for all time, so every product geodesic does. Conversely, a geodesic in one factor combined with constants in the others is a product geodesic. Completeness of the product extends it for all time, and projection gives an extension in that factor. Hopf–Rinow B.2 converts these assertions about geodesics to metric completeness.

For a piecewise smooth product path \(\eta\) on \([0,1]\), put \(v_i(t)=|\dot\eta_i(t)|\) on each smooth piece and \(L_i=\int_0^1v_i(t)\,dt\). The product metric and the integral triangle inequality give
\[
L(\eta)=\int_0^1\left(\sum_i v_i(t)^2\right)^{1/2}dt
\ \ge\ \left(\sum_iL_i^2\right)^{1/2}
\ \ge\ \left(\sum_i d_{X_i}(x_i,y_i)^2\right)^{1/2}.
\tag{K.3}
\]
The integral inequality here is the finite-dimensional vector integral inequality of Local tools 0.3, applied to the vector of nonnegative speeds. In each complete factor, Hopf–Rinow B.2 supplies a minimizing geodesic from \(x_i\) to \(y_i\). Parametrize it on \([0,1]\) with constant speed \(d_{X_i}(x_i,y_i)\), using a constant path if the endpoints coincide. Their product attains equality in (K.3), proving (K.1).

For assertion 2, let \(q_i:\widetilde M_i\to M_i\) be the covers constructed in [Flat connections, Theorems D.2–D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2). The product map \(\prod_iq_i\) is a smooth covering: products of evenly covered neighborhoods are evenly covered by products of sheets. Product metrics make it a local isometry. It is connected since paths in the factors combine. It is simply connected because a loop projects to a loop in every factor, each has a based contraction, and the tuple of these contractions contracts the product loop. Flat D.3 identifies it with the universal cover. The based covering identification with any other Riemannian universal cover is an isometry, since both covering metrics are the pullback of the metric on \(M\).

Every tuple of factor deck maps is a product deck map. Conversely, a deck map is determined by its value at one point by Flat D.1. Its value there is a tuple of points in the factor fibres; in each factor there is a unique deck map taking the chosen starting point to that coordinate, by Flat D.2. The tuple of these maps has the prescribed value and hence is the given deck map. This proves the exact product description of the deck group.

For assertion 3, completeness of \(X\) follows from Hopf–Rinow E.4, and assertion 1 makes its factors complete. Each factor is simply connected: include a based factor loop into \(X\), contract it there, and project the contraction back to the factor. The factors are connected because they are projections of the connected product.

Assume first that \(\Gamma\) is generated by supported elements. The subgroups \(\Gamma_i\) commute with one another when their indices differ, because their coordinate actions are separate. Every word in the generators can therefore be collected into a product \(\gamma_1\cdots\gamma_s\), with \(\gamma_i\in\Gamma_i\). Such an expression is unique: if the product is the identity, its action in each coordinate is the identity, so every \(\gamma_i\), as a map of \(X\), is the identity. This proves the group identity in (K.2). It does not assert that any \(\Gamma_i\) is finitely generated.

We verify the quotient geometry. Fix a base tuple \(o\). The action of \(\Gamma_i\) on \(X_i\) is free; otherwise the corresponding supported deck map would fix a tuple and would be the identity by Flat D.1. Let \(B_i=X_i/\Gamma_i\) with its quotient topology and orbit map \(\pi_i\). This map is open because the inverse image of the image of an open set is the union of its translates. The rule
\[
\iota_i:B_i\longrightarrow M,\qquad
[x_i]\longmapsto q(o_1,\ldots,o_{i-1},x_i,o_{i+1},\ldots,o_s)
\tag{K.4}
\]
is continuous. It is injective: if two such tuples have the same image, they differ by a tuple \((\gamma_j)_j\) of deck maps. For \(j\ne i\), \(\gamma_j\) fixes \(o_j\), and hence is the identity by freeness. The remaining relation says exactly that the two \(i\)-coordinates have the same \(\Gamma_i\)-orbit. Pulling back disjoint neighborhoods in the Hausdorff manifold \(M\) now proves that \(B_i\) is Hausdorff. Images of a countable base of \(X_i\) under the open \(\pi_i\) form a countable base of \(B_i\).

At a point of \(X\), Flat D.2 supplies a neighborhood disjoint from its nonidentity deck translates. Shrink it to a product of coordinate neighborhoods. Its \(i\)-th neighborhood \(U_i\) is disjoint from all its nonidentity \(\Gamma_i\)-translates: an intersection would give an intersection of the corresponding product neighborhoods, since these maps fix every other coordinate. Consequently \(\pi_i|_{U_i}\) is a homeomorphism onto an open set, and the full inverse image of that set is the disjoint union of its translates. The resulting quotient chart transitions are locally fixed elements of \(\Gamma_i\), hence smooth isometries. They define a smooth manifold and a metric on \(B_i\) for which \(\pi_i\) is a local-isometry covering, exactly as in J.2. It is connected as the image of \(X_i\), and complete by completeness of \(X_i\) and Hopf–Rinow E.4.

The product orbit relation just proved makes
\[
\prod_i B_i\longrightarrow M,\qquad ([x_i])_i\longmapsto q((x_i)_i)
\]
a well-defined bijection. In product quotient charts it is a local isometry. Its local smooth inverses therefore form a global inverse, proving the isometry in (K.2). The image of every \(X_i\)-leaf is the corresponding \(B_i\)-leaf.

Conversely, if a global product of \(M\) has the specified lifted foliations, assertion 2 describes its universal cover and deck group. The covering isometry takes each factor leaf onto the specified \(X_i\)-leaf. Each factor deck map therefore sends every point into its own \(X_i\)-leaf and fixes all other factor coordinates. Such an isometry is supported on \(X_i\): write its only potentially changing component as \(a(x_i,z)\), where \(z\) denotes the other coordinates. For a vector \(v\) in those other directions, the isometry identity gives
\[
|v|^2=|d a(0,v)|^2+|v|^2,
\]
so that derivative is zero. Integration along paths in the connected complementary product makes \(a\) independent of \(z\). Restricting the metric identity and using the inverse map proves that \(a\) is a factor isometry. The product deck group is generated by these supported maps, establishing the converse. □

**Lemma K.2 (one sequence of short generators for every product).** Let \(M\) be nonempty, complete and connected, let \(q:\widetilde M\to M\) be its Riemannian universal cover, and fix \(o\in\widetilde M\). There is a finite or countable sequence of nonidentity deck transformations \(\sigma_1,\sigma_2,\ldots\) generating \(\Gamma\), obtained successively by minimizing
\[
|\gamma|=d_{\widetilde M}(o,\gamma o)
\]
outside the subgroup generated by the preceding choices. For every finite global product decomposition of \(M\), each \(\sigma_j\) is supported on exactly one lifted factor. The same chosen sequence works simultaneously for all such decompositions. For the trivial group the sequence is empty.

**Proof.** The fibre \(q^{-1}(q(o))\) is closed, since points in \(M\) are closed and \(q\) is continuous. It is discrete, since the restriction of \(q\) to a sheet is injective. The universal cover is complete by Hopf–Rinow E.4, and its closed bounded balls are compact by Hopf–Rinow B.2. The intersection of such a ball with this closed fibre is compact and discrete, hence finite: its isolating open neighborhoods cover it, and a finite subcover contains only finitely many fibre points. The deck action is free and its orbit is that fibre, by Flat D.2. Consequently
\[
\{\gamma\in\Gamma:|\gamma|\le R\}\quad\hbox{is finite for every }R<\infty.
\tag{K.5}
\]
Also \(|\gamma|=0\) implies \(\gamma=1\).

Let \(\Gamma_0=\{1\}\). Whenever \(\Gamma_{j-1}\ne\Gamma\), choose any element outside it. If this element has displacement \(R\), (K.5) gives a finite nonempty set of outside elements of displacement at most \(R\). A minimum over that set is also a minimum over the entire complement, so a choice \(\sigma_j\) exists. Put
\(\Gamma_j=\langle\sigma_1,\ldots,\sigma_j\rangle\).
One may break ties using a fixed enumeration of the countable group from Flat D.2. Stop if the subgroup is all of \(\Gamma\).

If the construction does not stop, it still generates \(\Gamma\). Indeed, an element \(\gamma\) outside every \(\Gamma_j\) would be an eligible competitor at every step, forcing \(|\sigma_j|\le|\gamma|\) for all \(j\). The \(\sigma_j\)'s are distinct because each lies outside the subgroup containing its predecessors. This would contradict (K.5). Thus every element belongs to some \(\Gamma_j\).

Now fix any global product \(M=\prod_{i=1}^sM_i\). By K.1 its lifted deck group has independent factor subgroups. At a given step write the chosen generator uniquely as
\(\sigma_j=\gamma_1\cdots\gamma_s\), with \(\gamma_i\) supported on the \(i\)-th lifted factor. The product-distance formula gives
\[
|\sigma_j|^2=\sum_{i=1}^s|\gamma_i|^2.
\tag{K.6}
\]
If every \(|\gamma_i|<|\sigma_j|\), minimality of \(\sigma_j\) outside \(\Gamma_{j-1}\) would put every \(\gamma_i\) in \(\Gamma_{j-1}\), and hence their product there, a contradiction. At least one term therefore satisfies \(|\gamma_i|\ge|\sigma_j|\). Equation (K.6) makes it equal and all other terms zero. Freeness makes those other deck maps identities, so \(\sigma_j=\gamma_i\). Nonidentity of \(\sigma_j\) makes this supporting index unique. The construction of the sequence involved only \(o\) and the metric; the proof applies to each product without changing any choice. This is the simultaneous assertion. □

**Lemma K.3 (common refinement of two simply connected products).** Suppose \(X\) is a nonempty complete connected simply connected Riemannian manifold with two finite products
\[
X=\prod_{i=1}^pX_i=\prod_{j=1}^qY_j.
\tag{K.7}
\]
There are complete connected simply connected factors \(Z_{ij}\), possibly points, and a Euclidean space \(F\) such that
\[
X\cong\left(\prod_{i,j}Z_{ij}\right)\times F.
\tag{K.8}
\]
For every \(z\in X\), the \(Z_{ij}\)-leaf is exactly \(X_i(z)\cap Y_j(z)\). An isometry supported on \(X_i\) and on \(Y_j\) is supported on \(Z_{ij}\) in (K.8), and fixes the \(F\)-coordinate at every point.

**Proof.** Fix a point \(o\) and write the canonical simply connected decomposition E.3 as
\[
X=E\times N_1\times\cdots\times N_h,
\qquad E=\mathbb R^r,
\tag{K.9}
\]
choosing the Euclidean origin above \(o\). Let \(P_i\) be the orthogonal projection onto the tangent distribution of \(X_i\) in (K.7). The product connection in E.1 shows that it is parallel; it is self-adjoint and satisfies \(P_i^2=P_i\). H.1 therefore gives its form on (K.9): its Euclidean part is a constant orthogonal projection onto a subspace \(A_i\subset E\), and on each nontrivial irreducible factor \(TN_a\) it is a constant scalar \(\lambda_{ia}I\). The identity \(P_i^2=P_i\) gives \(\lambda_{ia}\in\{0,1\}\). Since the \(P_i\)'s have mutually orthogonal images and sum to the identity, the \(A_i\)'s form an orthogonal decomposition of \(E\), and every \(a\) belongs to exactly one set
\[
I_i=\{a:\lambda_{ia}=1\}.
\]
Thus the \(I_i\)'s partition \(\{1,\ldots,h\}\). Apply the same argument to the \(Y_j\)-projections, obtaining an orthogonal Euclidean decomposition \(E=\bigoplus_j B_j\) and a partition into sets \(J_j\).

At a point \(z=(e,n_1,\ldots,n_h)\) in (K.9), the \(X_i\)-leaf is precisely
\[
(e+A_i)\times\prod_{a\in I_i}N_a
\quad\hbox{with every coordinate }a\notin I_i\hbox{ fixed at }n_a.
\tag{K.10}
\]
To verify this equality, a path tangent to its distribution has constant complementary Euclidean projection and constant complementary \(N_a\)-coordinates. It therefore remains in the displayed set. Conversely the displayed set is connected by factorwise paths and all its tangent spaces are the prescribed distribution. The maximal-leaf property B.3, or the same path characterization of a product leaf, identifies it with \(X_i(z)\). The identical description holds for \(Y_j(z)\), with \(B_j,J_j\).

Their intersection is accordingly
\[
(e+(A_i\cap B_j))\times\prod_{a\in I_i\cap J_j}N_a,
\tag{K.11}
\]
with all other curved coordinates fixed. Define \(C_{ij}=A_i\cap B_j\) and
\[
Z_{ij}=C_{ij}\times\prod_{a\in I_i\cap J_j}N_a
\]
with the product metric and base point specified by \(o\). Distinct \(C_{ij}\)'s are orthogonal: if the first indices differ, use orthogonality of the \(A_i\)'s; if only the second indices differ, use that of the \(B_j\)'s. Set
\[
F=\left(\bigoplus_{i,j}C_{ij}\right)^\perp\subset E.
\tag{K.12}
\]
Every curved index \(a\) lies in exactly one \(I_i\cap J_j\). Splitting the Euclidean coordinates by (K.12) and regrouping these curved factors in (K.9) therefore gives the isometry (K.8). Each factor is complete by K.1 and simply connected by the product contraction argument there. Formula (K.11) proves the stated equality of leaves at every point; in particular these intersections really are connected embedded submanifolds with the claimed tangent spaces.

If \(\phi\) is supported on both old factors, then for every \(z\),
\(\phi(z)\in X_i(z)\cap Y_j(z)\). The leaf equality implies that \(\phi\) fixes every coordinate of (K.8) except possibly \(Z_{ij}\), including the entire \(F\)-coordinate. The derivative norm argument at the end of K.1 makes its \(Z_{ij}\)-component independent of all the other coordinates. Restricting the metric and using bijectivity shows that this component is an isometry of \(Z_{ij}\). This proves the support assertion. □

**Theorem K.4 (Eschenburg–Heintze decomposition and uniqueness).** Every nonempty complete connected Riemannian manifold has a finite global product
\[
M\cong\mathbb R^k\times M_1\times\cdots\times M_p,
\tag{K.13}
\]
where the \(M_i\) have positive dimension, are complete and connected, are globally indecomposable, and are not Euclidean. The Euclidean factor is maximal. Its factor foliation is unique, and the other factor foliations are unique up to permutation. Consequently their isometry types and \(k\) are unique. Simple connectivity, compactness and finite generation of the fundamental group are not assumed.

**Proof.** J.2 supplies \(M\cong\mathbb R^k\times B\), with \(B\) complete and connected and with no positive-dimensional global Euclidean factor. If a positive-dimensional factor of \(B\) splits into two positive-dimensional factors, perform that splitting. K.1 makes each resulting factor complete and connected. The sum of their dimensions is \(\dim B\), so at most \(\dim B\) positive-dimensional factors can occur; every further nontrivial splitting increases their number. This process must terminate with globally indecomposable factors. None can be Euclidean, since then \(B\) would have a positive-dimensional global Euclidean factor. This gives existence, with no factors if \(B\) is a point.

For uniqueness first assume \(M\) has no positive-dimensional global Euclidean factor, and suppose
\[
M=\prod_iM_i=\prod_jM'_j
\tag{K.14}
\]
are decompositions into positive-dimensional globally indecomposable factors. On the Riemannian universal cover these give two products by K.1. Apply K.3 to obtain
\[
\widetilde M=\left(\prod_{i,j}Z_{ij}\right)\times F.
\tag{K.15}
\]
Choose the single short-generator sequence of K.2. Each generator is supported on one lifted \(M_i\) and one lifted \(M'_j\), simultaneously. By K.3 it is supported on their \(Z_{ij}\) and fixes the \(F\)-coordinate. Thus the whole deck group fixes \(F\), and is generated by maps supported on individual \(Z_{ij}\)'s. K.1 applied to (K.15) gives
\[
M\cong\left(\prod_{i,j}B_{ij}\right)\times F,
\qquad B_{ij}=Z_{ij}/\Gamma_{ij},
\tag{K.16}
\]
where \(\Gamma_{ij}\) is the subgroup supported on that factor. The \(F\)-subgroup is trivial. Since \(M\) has no positive-dimensional Euclidean factor, \(F\) is a point.

With \(F=0\), the Euclidean spaces \(C_{ij}\) in K.3 span the entire Euclidean part upstairs. For each \(i\), their sum over \(j\) equals \(A_i\): decompose a vector in \(A_i\) into all the mutually orthogonal \(C_{uv}\)'s; components with \(u\ne i\) are orthogonal to \(A_i\) and must vanish. The analogous assertion holds for each \(B_j\). Together with the curved index partitions in K.3, this proves that the old lifted \(M_i\)-foliation is exactly the product of the \(Z_{ij}\)-foliations over \(j\), and the old lifted \(M'_j\)-foliation is their product over \(i\).

The same is true downstairs in (K.16). Indeed \(q\) maps each old lifted factor leaf onto its original factor leaf, by the product-cover description K.1. In the quotient product (K.16), the image of that lifted leaf is precisely the product of the indicated \(B_{ij}\)-leaves. The metrics are the induced leaf metrics, since all the covering and quotient charts are local isometries. Consequently each original \(M_i\) is isometric to \(\prod_jB_{ij}\), and each \(M'_j\) is isometric to \(\prod_iB_{ij}\).

Global indecomposability now implies that each row has exactly one positive-dimensional \(B_{ij}\); there cannot be none because \(M_i\) has positive dimension, and two would give a nontrivial product. Likewise each column has exactly one. A connected zero-dimensional quotient factor is a point. The unique positive entries therefore define a bijection between the row and column indices, and the corresponding old factor leaves both equal that single \(B_{ij}\)-leaf. This proves uniqueness of foliations and their isometry types in the case with no Euclidean factor.

In general J.2 identifies the maximal Euclidean distribution intrinsically. Any two decompositions (K.13) have this same distribution and hence the same orthogonal complement. Through a fixed base point, the complementary leaves in the two decompositions are therefore the same leaf, by B.3, with the same induced metric. It is a complete connected manifold with no Euclidean factor by J.2. Apply the uniqueness just proved to its two decompositions. Product coordinates extend the resulting leaf and distribution equality over all Euclidean coordinates, or equivalently the parallel distributions are determined by their values at the base point by A.2. The Euclidean foliation is already unique by J.2. This proves all assertions of (K.13). □

**Corollary K.5 (isometries and the identity component).** An isometry between complete connected Riemannian manifolds sends their maximal Euclidean factor foliations to one another and permutes their non-Euclidean indecomposable factor foliations. After this permutation it is a product of factor isometries. For (K.13),
\[
\operatorname{Isom}_0(M)\cong
\operatorname{Isom}_0(\mathbb R^k)
\times\prod_{i=1}^p\operatorname{Isom}_0(M_i)
\tag{K.17}
\]
as topological groups. Here the isometry groups have their usual compact-open topology, and the subscript \(0\) denotes the connected component of the identity. If \(M\) is compact, then \(k=0\).

**Proof.** Pull a product decomposition back by the given isometry. Riemannian A.3 shows that its factor distributions are parallel orthogonal distributions, and the pulled-back leaves and metrics form a global product of the same complete factor isometry types. K.4 identifies its maximal Euclidean foliation and matches its non-Euclidean foliations with those of the domain by one permutation. After that permutation, the derivative of the \(i\)-th output component is zero in every other factor direction. Integration along paths in the connected other factors proves that this output component depends only on the \(i\)-th input. Bijectivity gives bijectivity of each component; the inverse splits in the same way. Restricting the metric identity gives factor isometries. This also proves the assertion for a map between different manifolds.

Let \(G=\operatorname{Isom}(M)\) and let \(H\) be the subgroup preserving every factor foliation without permutation. The preceding argument gives the group bijection
\[
\prod_{i=0}^p\operatorname{Isom}(M_i)\longrightarrow H,
\qquad (a_i)_i\longmapsto\prod_i a_i,
\tag{K.18}
\]
where \(M_0=\mathbb R^k\). Omit a point Euclidean factor if desired.

We supply the topology details. On maps between these manifolds, the compact-open topology agrees with uniform convergence on each compact subset. In one direction, for a compact set \(C\) and an open target set \(U\) containing \(f(C)\), compactness supplies an \(\varepsilon>0\) whose \(\varepsilon\)-neighborhood of \(f(C)\) lies in \(U\): cover \(f(C)\) by finitely many sufficiently small balls inside \(U\) and take the smallest of their radii after shrinking once. Uniform closeness on \(C\) then puts \(g(C)\) in \(U\).

For the other direction, fix \(C,\varepsilon\). For every \(x\in C\), choose a sufficiently small open ball around \(x\) with compact closure \(K_x\) and with
\(f(K_x)\subset B(f(x),\varepsilon/3)\).
Such balls exist by continuity and compactness of closed bounded balls from Hopf–Rinow B.2. Finitely many of their interiors cover \(C\). The finitely many compact-open requirements
\[
g(K_x)\subset B(f(x),2\varepsilon/3)
\]
form a neighborhood of \(f\) and give \(d(g(y),f(y))<\varepsilon\) at every \(y\in C\), by the triangle inequality. This proves the claimed equivalence of topologies in the present complete setting.

These topologies make the isometry groups topological groups. For composition, if \(a,b\) vary near \(a_0,b_0\), the isometry and triangle identities give, for \(x\in C\),
\[
d(abx,a_0b_0x)
\le d(bx,b_0x)+d(a(b_0x),a_0(b_0x)).
\]
Uniform closeness of \(b\) on \(C\) and of \(a\) on the compact set \(b_0(C)\) therefore controls the composition uniformly on \(C\). For inversion,
\[
d(a^{-1}y,a_0^{-1}y)
=d(y,a(a_0^{-1}y))
=d(a_0(a_0^{-1}y),a(a_0^{-1}y)),
\]
so uniform closeness of \(a\) on the compact set \(a_0^{-1}(C)\) controls its inverse on \(C\). These inequalities prove continuity of both operations.

Map (K.18) is continuous: for a compact subset of the product, its finitely many coordinate projections are compact, and (K.1) bounds uniform displacement of the product maps by the square root of the sum of their squared coordinate displacements on those compact projections. Its inverse is continuous as well. To recover \(a_i\), restrict the product map to the \(i\)-th based axis and project to \(M_i\); the image of a compact set in that axis is compact and the projection is distance nonincreasing by (K.1). Thus (K.18) is a homeomorphism.

The permutation of the non-Euclidean factor foliations is locally constant. To see this at the identity, fix a base point \(o\), and for each \(i>0\) choose \(z_i\in M_i(o)\) with \(z_i\ne o\). Put \(\delta_i=d(o,z_i)>0\). Consider isometries \(a\) satisfying, for every such \(i\),
\[
d(a(o),o)<\delta_i/3,\qquad
d(a(z_i),z_i)<\delta_i/3.
\tag{K.19}
\]
These conditions define an open neighborhood of the identity. If \(a\) sent the \(i\)-th foliation to a different \(j\)-th one, the \(i\)-coordinates of \(a(o)\) and \(a(z_i)\) would coincide. Projecting to \(M_i\) and using (K.1) would give
\[
\delta_i
\le d(o_i,(a(o))_i)+d((a(z_i))_i,(z_i)_i)
<2\delta_i/3,
\]
a contradiction. Thus (K.19) lies in \(H\). If there are no non-Euclidean factors, \(H=G\) and no conditions are needed. Left composition by a fixed isometry is a homeomorphism for uniform convergence on compact sets, because it preserves the target distances. Therefore all cosets of \(H\) are open. Every connected subset of \(G\) containing the identity must lie in \(H\): otherwise its intersection with \(H\) and with the union of the other open cosets would separate it.

It follows that \(G_0=H_0\). Under (K.18), the identity component of the finite product is the product of the identity components. For one inclusion, each coordinate projection takes a connected set containing the identity to such a set, hence into that coordinate's identity component. For the reverse inclusion, a finite product of connected spaces is connected. Explicitly, for two connected spaces the union of the horizontal slice through a base point with each vertical slice is connected, because each such union consists of two connected sets meeting at a point; their union over all vertical slices is the entire product and they all contain that horizontal slice. The union principle used here follows directly from a separation: a connected member cannot meet both open parts, and a common point forces all members into the same part. This proves connectedness for two factors and then for finitely many by induction. Applying it to the coordinate identity components proves the reverse inclusion and (K.17).

Finally the projection of a compact product (K.13) onto its Euclidean factor is compact and surjective. A positive-dimensional Euclidean space is not compact, since its continuous norm is unbounded whereas a continuous real function on a compact space is bounded by Local tools 0.1. Hence compactness of \(M\) forces \(k=0\). □

**Corollary K.6 (cancellation of complete Riemannian products).** If \(M,N,B\) are nonempty complete connected Riemannian manifolds and
\[
M\times B\cong N\times B
\tag{K.20}
\]
isometrically, then \(M\cong N\) isometrically. Repeated factor isometry types are allowed.

**Proof.** First, maximal global Euclidean dimensions add under products. To verify this rather than assume it, write the canonical Euclidean parts of the universal covers of two factors as \(E_1,E_2\). K.1 gives the product universal cover and independent deck groups. E.1, or the fixed-vector description H.1, identifies its canonical Euclidean part as \(E_1\oplus E_2\). If \(W_1,W_2\) are the displacement spans in J.2, the product displacement span is
\[
W=W_1\oplus W_2.
\tag{K.21}
\]
Indeed any product displacement is a pair of displacements and belongs to that sum; conversely deck maps acting in just one factor supply every generator of each summand. Taking orthogonal complements and applying J.2 gives \(k(M\times B)=k(M)+k(B)\), and the analogous equality for \(N\).

Decompose all three manifolds by K.4. Concatenating their non-Euclidean indecomposable factors and combining their Euclidean blocks therefore gives decompositions of the two products of the precise form (K.13), with maximal Euclidean blocks by (K.21). Uniqueness in K.4 applied to (K.20) gives
\[
k(M)+k(B)=k(N)+k(B),
\]
so \(k(M)=k(N)\).

For each non-Euclidean factor isometry type \(Q\) appearing in any of the three finite lists, let \(m_Q(C)\) be its multiplicity in the decomposition of \(C\). The same uniqueness gives the equality of integers
\[
m_Q(M)+m_Q(B)=m_Q(N)+m_Q(B).
\tag{K.22}
\]
Subtracting \(m_Q(B)\) proves \(m_Q(M)=m_Q(N)\). There are only finitely many types in these lists. Match their factors type by type, choose an isometry for each matched pair, and choose a Euclidean isometry between the equal-dimensional Euclidean factors. Their product, composed with the decomposition isometries, gives \(M\cong N\). The argument cancels multiplicities; it does not require the given isometry in (K.20) to preserve the displayed \(B\)-block. □

**Exercise K.7 (a globally indecomposable flat torus).** In the Euclidean plane set
\[
L=\mathbb Z(1,0)+\mathbb Z(\sqrt2,1),\qquad T=\mathbb R^2/L.
\tag{K.23}
\]
Prove that \(T\) is a compact complete flat Riemannian manifold with trivial full holonomy, and that it is globally indecomposable.

**Solution.** Let \(A:\mathbb R^2\to\mathbb R^2\) be the invertible linear map
\[
A(u,v)=(u+\sqrt2\,v,v);
\]
its inverse is \((x,y)\mapsto(x-\sqrt2\,y,y)\). Thus \(L=A\mathbb Z^2\). There is a constant \(C>0\) with
\(|A^{-1}w|\le C|w|\) for all \(w\): bound the two coordinates in the explicit inverse by the triangle inequality and then their Euclidean norm. Hence every nonzero \(\ell\in L\) has \(|\ell|\ge 1/C\). Moreover each bounded set contains only finitely many lattice points, since their inverse images have bounded integer coordinates.

Translations by \(L\) act freely and isometrically. Balls of radius less than \(1/(3C)\) are disjoint from their nonzero lattice translates. The orbit map is open. Its quotient is Hausdorff: for points \(x,y\) in different orbits, the distances \(|x-y-\ell|\) have a positive minimum. To justify this, only finitely many \(\ell\)'s can have distance at most \(1+|x-y|\), by the bounded-lattice assertion; this finite set is nonempty because it contains \(0\), and all its distances are positive. Every other distance is larger. Balls about \(x,y\) of radius less than one third of this minimum have disjoint quotient images, by the triangle inequality and translation invariance. Images of a countable Euclidean base give second countability. The disjoint-translate ball charts have translation transition maps, so they define a smooth quotient metric and a local-isometry covering \(q:\mathbb R^2\to T\), by the chart argument in J.2.

The compact parallelogram \(A([0,1]^2)\) maps onto \(T\): subtract the integer parts of the two coordinates of \(A^{-1}x\) to choose a representative in it. Therefore \(T\) is compact. It is connected as the image of \(\mathbb R^2\), and complete either by compactness and Hopf–Rinow B.3 or by the covering and Hopf–Rinow E.4. Its metric is locally Euclidean; in these charts the metric coefficients are constant, so Riemannian A.1 gives zero Christoffel symbols and Linear B.3 gives zero curvature.

Straight-line contractions make \(\mathbb R^2\) simply connected. Thus \(q\) is the universal cover by Flat D.3, and its full deck group consists exactly of the translations by \(L\): these realize every image of one point, and Flat D.1 determines a deck map by that image. Every lifted loop ends at \(x+\ell\) for some \(\ell\in L\). Euclidean transport is the identity on coordinate vectors and the derivative of a translation is the identity. The endpoint-identification calculation in J.4 therefore makes all full holonomy trivial. In particular the two constant coordinate vector fields descend to a global parallel orthonormal frame.

We next prove that \(L\) has no pair of nonzero orthogonal vectors. The numbers \(\sqrt2\) and \(\sqrt3\) are irrational. For either prime \(d=2\) or \(3\), a hypothetical rational square root gives integers \(a,b\), \(b>0\), with \(a^2=db^2\); choose one with the least positive \(b\). The possible squares modulo \(d\) are \(0,1\), so \(d\mid a\); substitution then gives \(d\mid b\). Dividing both integers by \(d\) yields the same equation with a smaller positive denominator, a contradiction.

Write lattice vectors as
\[
v=A(m,n),\qquad w=A(p,q),\qquad m,n,p,q\in\mathbb Z.
\]
Expanding their dot product gives
\[
\langle v,w\rangle=mp+3nq+\sqrt2\,(np+mq).
\tag{K.24}
\]
Irrationality of \(\sqrt2\) shows that orthogonality would imply
\[
\begin{pmatrix}m&3n\\ n&m\end{pmatrix}
\begin{pmatrix}p\\q\end{pmatrix}=0.
\tag{K.25}
\]
If \(v\ne0\), then \((m,n)\ne(0,0)\). The determinant \(m^2-3n^2\) is nonzero: if \(n=0\) it is \(m^2>0\); otherwise its vanishing would make \(m/n\) a rational square root of \(3\) up to sign. Thus the matrix in (K.25) is invertible by Local tools 0.2, forcing \(p=q=0\) and \(w=0\). This proves the obstruction.

Suppose \(T\) nevertheless had a product of two positive-dimensional connected manifolds. Each would have dimension one. By K.1 the product lifts to an orthogonal product foliation of \(\mathbb R^2\) by its two factor directions. The projections onto these lifted tangent distributions are parallel. In Euclidean coordinates a parallel endomorphism has constant coefficients, by the transport formula H.1, so these rank-one orthogonal distributions are two fixed perpendicular lines. Their leaves are the corresponding affine lines, by the tangent-path characterization B.3.

Choose the short generators of K.2 for this product. Each is a nonzero lattice translation supported on one of these two line foliations; hence its translation vector lies in that line, since it sends the origin into the line leaf through the origin. The generators generate all lattice translations, so their vectors span the real span of \(L\), which is the whole plane. Consequently at least one nonzero generator vector lies in each of the two perpendicular lines. These would be two nonzero orthogonal vectors in \(L\), contradicting (K.25). Thus \(T\) is globally indecomposable. Its trivial holonomy proves that global indecomposability in K.4 cannot be replaced by holonomy irreducibility. □

**Exercise K.8 (cancellation when factor types repeat).** Let \(M,N,B\) be nonempty compact connected Riemannian manifolds. Suppose a complete indecomposable-factor decomposition of \(B\) includes three factors isometric to a fixed positive-dimensional globally indecomposable manifold \(Q\). If \(M\times B\cong N\times B\), show that \(M,N\) have the same number of factors of type \(Q\), even if the isometry exchanges factors across the two displayed blocks. Complete the cancellation argument.

**Solution.** Compactness gives completeness by Hopf–Rinow B.3. K.4 therefore supplies the finite factor decompositions, and K.5 gives zero Euclidean dimension for all three manifolds. Put \(b=m_Q(B)\). The hypothesis gives \(b\ge3\), with \(b=3\) if the named three are all the factors of that type. The product decompositions and K.4's uniqueness give
\[
m_Q(M)+b=m_Q(N)+b.
\]
Thus \(m_Q(M)=m_Q(N)\), irrespective of how the particular isometry permutes the factors. If \(b=3\), this is the explicit cancellation of the three copies; any additional copies cancel by exactly the same integer equality.

For each other factor type \(R\), uniqueness gives
\(m_R(M)+m_R(B)=m_R(N)+m_R(B)\), and subtraction again gives equal multiplicities. Match the finitely many factors with these equal multiplicities and take the product of their isometries. Composing with the decompositions proves \(M\cong N\). The factors are matched by their types after counting, so no preservation of the original \(M\)-, \(N\)- or \(B\)-blocks is required. □

## L. Products of metric spaces

We now work with arbitrary metric spaces. A finite metric product has the distance
\[
d((x_i),(y_i))=\left(\sum_i d_i(x_i,y_i)^2\right)^{1/2}.
\tag{L.1}
\]
A constant-speed minimizing segment is a map \(\gamma:[a,b]\to X\), with \(a<b\), satisfying
\(d(\gamma(s),\gamma(t))=c|s-t|\) for a constant \(c\ge0\). A space is geodesic if every pair of its points can be joined by such a segment. A subset is totally convex if every minimizing segment whose endpoints lie in it stays in it.

Thomas Foertsch and Alexander Lytchak's [exact arXiv:math/0605419v1](https://arxiv.org/abs/math/0605419v1), §2, develops the metric-product tools used below. The arguments in this section do not assume completeness, a manifold structure or finite dimension.

**Lemma L.1 (geodesics, speeds and fibres in a metric product).** Projections from a finite metric product are distance nonincreasing. Every constant-speed minimizing segment in the product has constant-speed minimizing projections, with speeds \(c_i\) satisfying
\[
c^2=\sum_i c_i^2.
\tag{L.2}
\]
Conversely the product of constant-speed minimizing segments on a common parameter interval is such a segment. A nonempty finite product is geodesic if and only if all its factors are geodesic. In a geodesic product, every factor fibre is totally convex.

**Proof.** Formula (L.1) is indeed a metric: symmetry and positive definiteness follow coordinatewise, and coordinate triangle inequalities followed by the Euclidean norm triangle inequality of Local tools 0.0 give its triangle inequality. The same formula dominates each one of its summands' square roots, proving the projection assertion. For a product segment and \(s<t<u\), define the vectors of nonnegative coordinate distances
\[
A_i=d_i(\gamma_i(s),\gamma_i(t)),\quad
B_i=d_i(\gamma_i(t),\gamma_i(u)),\quad
C_i=d_i(\gamma_i(s),\gamma_i(u)).
\]
The factor triangle inequalities give \(C_i\le A_i+B_i\). Hence the Euclidean norm satisfies
\[
|C|\le |A+B|\le |A|+|B|.
\tag{L.3}
\]
The constant-speed assumption makes the first and last quantities equal to \(c(u-s)\). Thus both inequalities are equalities. Since all coordinates are nonnegative, the first equality forces \(C=A+B\): a strict coordinate inequality would strictly increase the sum of the squares unless the two coordinates were equal, contrary to strictness. If \(c>0\), the vectors \(A,B\) have positive norms. Squaring equality in the second inequality gives
\(\langle A,B\rangle=|A||B|\), and therefore
\[
\left|A/|A|-B/|B|\right|^2=0.
\]
Consequently \(A/(t-s)=B/(u-t)=C/(u-s)\).

Apply this first with the interval endpoints \(a,b\) and an interior point \(t\). The coordinate distance from \(\gamma_i(a)\) to \(\gamma_i(t)\) equals
\((t-a)d_i(\gamma_i(a),\gamma_i(b))/(b-a)\).
The already proved coordinate equality \(C=A+B\), applied to \(a<s<t\), then gives
\[
d_i(\gamma_i(s),\gamma_i(t))
=\frac{t-s}{b-a}\,d_i(\gamma_i(a),\gamma_i(b)).
\]
The endpoint cases follow from the preceding formula directly. These are constant-speed minimizing projections, and (L.1) at the two endpoints gives (L.2). If \(c=0\), the product segment and all its projections are constant, giving the same conclusions.

Conversely insert the distance formulas for the coordinate segments into (L.1); the resulting product distance is \(|t-s|(\sum_i c_i^2)^{1/2}\). Thus geodesic factors give a geodesic product. If the product is geodesic, join two tuples differing only in coordinate \(i\). Projection gives a minimizing segment in that factor. Finally, a segment between points of one factor fibre has zero endpoint displacement in every other coordinate. The formula for \(c_i\) above makes all those coordinates constant, so the segment remains in the fibre. □

For a two-factor product \(X=Y\times\bar Y\), write \(Y_x\) for the fibre through \(x\) obtained by varying only the \(Y\)-coordinate. Let \(P^{Y_x}:X\to Y_x\) keep that coordinate and replace the other by that of \(x\). The product formula gives, for \(u\in Y_x\),
\[
d(u,z)^2=d(u,P^{Y_x}z)^2+d(P^{Y_x}z,z)^2.
\tag{L.4}
\]
This is an identity of the given product metric.

**Lemma L.2 (recognizing a metric product).** Suppose a nonempty metric space is a union \(X=\bigcup_{i\in J}E_i\) of nonempty subsets. Suppose maps \(T_{ij}:E_i\to E_j\) satisfy
\[
T_{ii}=\operatorname{id},\qquad
T_{ji}T_{ij}=\operatorname{id},\qquad
T_{jk}T_{ij}=T_{ik},
\tag{L.5}
\]
and, for every \(u\in E_i\) and \(v\in E_j\),
\[
d(u,v)^2=d(u,T_{ij}u)^2+d(T_{ij}u,v)^2.
\tag{L.6}
\]
Then every \(T_{ij}\) is an isometry. The number
\(\delta(i,j)=d(u,T_{ij}u)\) is independent of \(u\in E_i\) and defines a pseudometric on \(J\). Its zero classes are exactly the indices defining equal subsets; unequal subsets are disjoint. After identifying equal subsets, \(J\) is a metric space, and for any \(o\in J\) the map
\[
E_o\times J\longrightarrow X,\qquad (u,i)\longmapsto T_{oi}u
\tag{L.7}
\]
is a surjective isometry for the product metric.

**Proof.** Fix \(i,j\), and take \(u\in E_i,v\in E_j\). Set \(u'=T_{ij}u\), \(v'=T_{ji}v\), and abbreviate
\[
a=d(u,u')^2,\quad b=d(v,v')^2,\quad
c=d(u',v)^2,\quad e=d(u,v')^2.
\]
Applying (L.6) in both directions to \(u,v\) gives \(a+c=b+e\). Applying it in both directions to \(u',v'\), using (L.5), gives \(b+c=a+e\). Subtraction yields \(a=b\), and then \(c=e\). Since \(u,v\) were arbitrary and both sets are nonempty, \(d(u,T_{ij}u)\) is independent of \(u\), and equals \(d(v,T_{ji}v)\). This defines a symmetric nonnegative \(\delta(i,j)\).

For \(w\in E_i\), take \(v=T_{ij}w\); then \(v'=w\). The equality \(c=e\) gives
\[
d(T_{ij}u,T_{ij}w)=d(u,w).
\]
The inverse in (L.5) makes this an isometry onto \(E_j\). For \(u\in E_i\), let \(v=T_{ij}u\) and \(w=T_{jk}v=T_{ik}u\). The triangle inequality for \(u,v,w\) gives
\(\delta(i,k)\le\delta(i,j)+\delta(j,k)\); also \(\delta(i,i)=0\). Thus \(\delta\) is a pseudometric.

If \(\delta(i,j)=0\), then \(T_{ij}u=u\) for every \(u\), so \(E_i\subset E_j\); the inverse gives equality. Conversely if the two subsets meet at \(u\), (L.6) with \(v=u\) gives \(d(u,T_{ij}u)=0\), hence \(\delta(i,j)=0\) and equality of the subsets. In particular equal subsets have \(T_{ij}\) equal to the identity on that set. The composition rule in (L.5) then shows that all maps \(T\) and distances \(\delta\) are unchanged on replacing an index by an equal-subset index. They therefore descend to the stated quotient of \(J\), on which \(\delta\) is a metric and the sets \(E_i\) are disjoint.

Map (L.7) is onto because the subsets cover \(X\) and each \(T_{oi}\) is onto. For \(u,v\in E_o\), (L.6), its constant displacement and (L.5) give
\[
\begin{aligned}
d(T_{oi}u,T_{oj}v)^2
&=\delta(i,j)^2+d(T_{ij}T_{oi}u,T_{oj}v)^2\\
&=\delta(i,j)^2+d(T_{oj}u,T_{oj}v)^2\\
&=\delta(i,j)^2+d(u,v)^2.
\end{aligned}
\tag{L.8}
\]
Thus it preserves product distances; in particular it is injective. This proves the product recognition assertion with all identifications accounted for. □

**Lemma L.3 (an intersection Pythagorean identity).** Let
\(X=Y\times\bar Y=Z\times\bar Z\) be two metric products. Fix \(x\in X\), put \(F_x=Y_x\cap Z_x\), and take \(p\in\bar Y_x\), \(q\in F_x\). With \(z=P^{Z_x}p\), one has
\[
d(z,q)^2=d(z,x)^2+d(x,q)^2.
\tag{L.9}
\]
No geodesic or dimension assumption is needed for this identity.

**Proof.** Both \(q\) and \(x\) lie in \(Z_x\). Applying (L.4) in the \(Z\)-product gives
\[
d(q,p)^2=d(q,z)^2+d(z,p)^2,\qquad
d(x,p)^2=d(x,z)^2+d(z,p)^2.
\]
Since \(q\in Y_x\) and \(p\in\bar Y_x\), the \(Y\)-product gives
\(d(q,p)^2=d(q,x)^2+d(x,p)^2\).
Substitute the second equality into this one and then into the first, and cancel \(d(z,p)^2\). The result is (L.9). □

## M. Affine images and the seminorm prerequisite

An affine metric space is a space isometric to a linearly convex subset \(C\) of a real normed vector space. Such a representation chooses segments
\(\sigma_{xy}(t)=(1-t)x+ty\), \(0\le t\le1\). These are constant-speed minimizing segments. When the norm is not strictly convex, other minimizing segments can also exist; the chosen linear ones are the segments used in this section.

The affine-image result in [Foertsch–Lytchak, arXiv:math/0605419v1, §3.3](https://arxiv.org/abs/math/0605419v1) builds on the norm-characterization argument in [Petra Hitzelberger and Alexander Lytchak, *Spaces with many affine functions*, arXiv:math/0511583v1, §§4–5](https://arxiv.org/abs/math/0511583v1). We prove below the continuous pseudometric version needed here, including its regularization and variation steps.

A pseudometric has symmetry, nonnegativity, a zero diagonal and the triangle inequality, but distinct points may have distance zero. The precise straight-segment condition will be
\[
D((1-s)x+sy,(1-t)x+ty)=|s-t|D(x,y)
\quad(0\le s,t\le1).
\tag{M.1}
\]

**Lemma M.1 (regularization preserving straight-segment distances).** Let \(O\subset\mathbb R^n\), \(n\ge1\), be open and convex, and let \(D:O\times O\to[0,\infty)\) be a continuous pseudometric satisfying (M.1). Around each point of \(O\) there is an open ball \(U\), with closure contained in \(O\), and a family \(D_\varepsilon\) of continuous pseudometrics on \(U\) such that:

1. Each \(D_\varepsilon\) satisfies (M.1) on \(U\).
2. \(D_\varepsilon(p,q)\) is smooth jointly in \(p,q\) when \(p\ne q\).
3. \(D_\varepsilon\to D\) uniformly on \(\overline U\times\overline U\) as \(\varepsilon\to0\), taking the same formulas on the closure.

**Proof.** We use finite-dimensional integrals of continuous functions with compact support. The one-variable integration and uniform-limit facts are proved in [Local tools, Lemma 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Their finite-dimensional forms follow by iteration: on a compact box, uniform continuity makes every rectangular-grid Riemann sum approach the same iterated integral, because the upper-minus-lower grid sum is at most the box volume times the maximal oscillation on a grid cell. The oscillation tends to zero with the mesh. Reordering finite sums shows that the integral is independent of the order of the one-variable integrations. The integral is linear, preserves inequalities, and is bounded by the box volume times the supremum norm; these facts pass from the finite sums to the limit. Thus it also commutes with uniform limits.

Differentiation in a parameter can be passed under such an integral whenever the integrand and its parameter derivatives are continuous and supported in a common compact box. Indeed the one-variable segment formula in Local tools 0.3 writes each parameter difference quotient as the integral of its corresponding derivative over a short parameter interval. Uniform continuity of that derivative on the compact box makes these difference quotients converge uniformly to it. The preceding uniform-limit bound permits taking the integral. Repetition proves the assertion for all derivative orders. We will use only this elementary compact-support version.

Let \(h(s)=\eta(1-s^2)\), where the smooth function \(\eta\) of [Local tools, Lemma 0.5](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) is zero for nonpositive inputs and positive otherwise. Then \(h\) is smooth, nonnegative, supported in \([-1,1]\), and positive on \((-1,1)\). Its integral is positive and finite; divide by that integral to make it \(1\). Taking products of scaled copies of \(h\) in the \(n^2+n\) entries of a matrix and a vector gives a smooth nonnegative kernel
\(\rho_\varepsilon(S,b)\) of total integral \(1\), supported where all entries of \(S,b\) have absolute value at most \(\varepsilon\).

Choose concentric balls around the point under consideration, with the closure of the largest still in \(O\). Take \(U\) to be the smallest. For all sufficiently small \(\varepsilon>0\), every affine map
\[
T_{A,b}(p)=Ap+b,\qquad A=I+S,
\]
with \((S,b)\) in the kernel support takes \(\overline U\) into the middle ball. This follows from the coordinate bounds on \(S,b\), which make
\(|Sp+b|\le n\varepsilon|p|+\sqrt n\,\varepsilon\), uniformly for \(p\in\overline U\). Define
\[
D_\varepsilon(p,q)
=\int D(Ap+b,Aq+b)\rho_\varepsilon(A-I,b)\,dA\,db.
\tag{M.2}
\]
All arguments of \(D\) lie in a fixed compact subset of \(O\). Its continuity therefore gives continuity of (M.2). For each fixed \(A,b\), pullback of \(D\) by the affine map is a pseudometric. Integrating its triangle inequality, symmetry, zero diagonal and nonnegativity proves the same properties for \(D_\varepsilon\). Affine maps preserve the combinations in (M.1), so integrating that equality proves property 1. Invertibility of \(A\) is not required.

We prove smoothness without differentiating \(D\). Fix \(p\ne q\), set \(v=q-p\), and choose \(j\) with \(v_j\ne0\). Keep as free variables the columns \(A_k\) for \(k\ne j\), collectively denoted \(R\), and make the change of integration variables
\[
a=Ap+b,\qquad w=Av.
\tag{M.3}
\]
The missing column and translation are recovered by
\[
A_j=\frac{w-\sum_{k\ne j}A_kv_k}{v_j},
\qquad b=a-Ap.
\tag{M.4}
\]
For fixed \(A\), replacing \(b\) by \(a\) is a translation in each coordinate. For fixed \(R\), replacing the \(n\) entries of \(A_j\) by \(w\) scales each coordinate by \(v_j\) and translates it. The one-variable substitution rule for translations and nonzero scalings follows directly by transforming interval partitions in the Riemann sums; iterating it gives the factor \(|v_j|^{-n}\). The reordering of these integrations is justified by the grid-sum argument above. Thus (M.2) becomes
\[
\int D(a,a+w)\,
\rho_\varepsilon(A(p,v,w,R)-I,\ a-A(p,v,w,R)p)
\,|v_j|^{-n}\,da\,dw\,dR.
\tag{M.5}
\]
Here the matrix \(A(p,v,w,R)\) is given by its columns in (M.4); writing \(p\) as an argument keeps track of all parameters, although the recovered column itself only depends on \(v,w,R\).

For \((p,q)\) in a sufficiently small neighborhood of the fixed pair, \(v_j\) stays nonzero. The kernel in (M.5) is therefore smooth in \((p,q)\) and all integration variables. Its support, and the supports of all its parameter derivatives, lie in one compact set: \(R\) consists of bounded matrix columns near those of \(I\), \(a=Ap+b\) stays bounded, and \(w=A(q-p)\) stays bounded. Also \(a,a+w\) remain in the fixed middle ball whenever the kernel or its derivatives can be nonzero.

To place the integrand on one fixed box, choose a continuous radial cutoff equal to \(1\) on that middle ball and \(0\) outside the largest ball. For example, a piecewise linear function of the distance from its center with these two values has the required properties. Multiply \(D(x,y)\) by the two cutoffs and extend by zero outside \(O\times O\). This gives a globally continuous bounded function equal to \(D\) at every pair that can contribute to (M.5). The vanishing near the boundary of \(O\) makes the extension continuous there. After this replacement the factor depending on \(D\) in (M.5) is a fixed continuous function of \(a,w\), independent of \(p,q\). All parameter derivatives of the remaining kernel are continuous and have common compact support, so the differentiation-under-the-integral argument already proved applies at every order. This proves property 2.

Finally \(Ap+b\to p\) uniformly on \(\overline U\) over the shrinking kernel supports, and likewise for \(q\). Uniform continuity of \(D\) on the relevant compact set gives
\[
\sup_{p,q\in\overline U}|D_\varepsilon(p,q)-D(p,q)|
\le
\sup_{\substack{p,q\in\overline U\\(A-I,b)\in\operatorname{supp}\rho_\varepsilon}}
|D(Ap+b,Aq+b)-D(p,q)|\longrightarrow0.
\]
The integral bound uses the nonnegative kernel of total mass \(1\). This proves property 3 and the lemma. □

**Theorem M.2 (constant-speed pseudometrics are seminorm distances).** Let \(C\) be a nonempty linearly convex subset of a finite-dimensional real vector space. Suppose \(D\) is a pseudometric on \(C\), continuous in the ordinary finite-dimensional topology, and satisfies (M.1). Then there is a unique seminorm \(N\) on \(V=\operatorname{span}(C-C)\) such that
\[
D(x,y)=N(y-x)\qquad(x,y\in C).
\tag{M.6}
\]
No openness, closedness or nondegeneracy of \(D\) is assumed.

**Proof.** We first work on a nonempty open convex set \(O\subset\mathbb R^n\). For \(p\in O\) and \(v\in\mathbb R^n\), set
\[
F(p,v)=\frac{D(p,p+hv)}h
\tag{M.7}
\]
for sufficiently small \(h>0\), and set \(F(p,0)=0\). Condition (M.1) makes (M.7) independent of \(h\). More generally, the intersection of \(O\) with a straight line is an interval, and applying (M.1) to a segment containing any two of its subsegments shows that the distance per unit linear parameter is the same along the whole interval. Therefore
\[
F(p+tv,v)=F(p,v),\qquad
F(p,\lambda v)=|\lambda|F(p,v)
\tag{M.8}
\]
whenever the indicated points lie in \(O\). For negative \(\lambda\), symmetry of \(D\) and the first identity give the second one. For any fixed \((p,v)\), a common sufficiently small \(h\) can be used in (M.7) throughout a neighborhood of that pair. Continuity of \(D\) thus proves joint continuity of \(F\), including at \(v=0\).

The triangle inequality gives, for sufficiently small \(t>0\),
\[
\begin{aligned}
F(p,u+v)
&=\frac{D(p,p+t(u+v))}{t}\\
&\le F(p,u)+F(p+tu,v).
\end{aligned}
\]
Letting \(t\to0\) proves \(F(p,u+v)\le F(p,u)+F(p,v)\). Together with (M.8) and nonnegativity, this shows that \(F(p,\cdot)\) is a seminorm at each point. The remaining issue is its independence of \(p\).

First assume \(D\) is smooth off the diagonal. Then (M.7) makes \(F\) smooth on the set \(v\ne0\). We prove the needed variation identity directly. If \(c:[a,b]\to O\) is continuously differentiable, its endpoint distance is bounded by
\[
D(c(a),c(b))\le\int_a^b F(c(t),c'(t))\,dt.
\tag{M.9}
\]
Indeed, on any partition the triangle inequality bounds the left side by the sum of the successive distances. If \(\Delta t=t_{i+1}-t_i\), the corresponding summand equals
\[
\Delta t\,F\left(c(t_i),
          \frac{c(t_{i+1})-c(t_i)}{\Delta t}\right),
\]
by (M.7), (M.8) and the constant-speed condition on the straight segment between the two points. The mean velocities converge uniformly to \(c'(t_i)\) as the mesh tends to zero: the segment integral formula in Local tools 0.3 bounds the error by the oscillation of \(c'\) on the subinterval. Joint continuity of \(F\), uniform on the compact position and bounded-velocity sets involved, makes these sums converge to the integral in (M.9). This proves the inequality.

Fix \(p\in O\) and \(v\ne0\), and choose a short interval \([a,b]\) for which the line \(c_0(t)=p+tv\) lies in \(O\). The straight-line identities make equality hold in (M.9) for \(c_0\). Let \(\eta\) be a continuously differentiable real function vanishing near the endpoints of this interval, and vary the line in coordinate direction \(e_j\):
\[
c_s(t)=p+tv+s\eta(t)e_j.
\]
For all sufficiently small positive and negative \(s\), these curves remain in \(O\), have the same endpoints, and have nonzero velocities. Thus their integrals on the right of (M.9) have a minimum at \(s=0\). Smoothness of \(F\) near their compact position-velocity sets permits differentiation under the one-variable integral, by the uniform difference-quotient argument from M.1. The derivative at zero is
\[
0=\int_a^b
\left(F_{p_j}(p+tv,v)\eta(t)
      +F_{v_j}(p+tv,v)\eta'(t)\right)dt.
\]
Integration by parts, which follows by integrating the product derivative in Local tools 0.3, gives
\[
\int_a^b
\left(F_{p_j}(p+tv,v)
      -\sum_i v_iF_{p_i v_j}(p+tv,v)\right)\eta(t)\,dt=0.
\tag{M.10}
\]
The continuous coefficient of \(\eta\) must vanish. To justify that step, if it were positive at one point, it would be positive on a smaller closed interval. On that interval take a nonnegative function
\((t-\alpha)^2(\beta-t)^2\), extended by zero outside; it is continuously differentiable, positive in the interior, and supported away from \(a,b\). Its integral against that coefficient is positive, a contradiction. A negative value is treated by reversing the sign. Hence, since the short line can pass through any \(p\) with any \(v\ne0\),
\[
F_{p_j}(p,v)=\sum_i v_iF_{p_i v_j}(p,v).
\tag{M.11}
\]

Mixed derivatives can be interchanged in these smooth expressions. For completeness, apply the one-variable fundamental theorem twice to the increment of a \(C^2\) function around a coordinate rectangle. It equals the iterated integral of either ordering of its mixed derivative. Dividing these two equal expressions by the rectangle area and shrinking the rectangle gives equality of the mixed derivatives by continuity. This applies to the position and velocity coordinates of \(F\).

On the other hand the first identity of (M.8), differentiated in \(t\), says \(\sum_i v_iF_{p_i}(p,v)=0\). Differentiating this identity in \(v_j\), where \(v\ne0\), gives
\[
F_{p_j}(p,v)+\sum_i v_iF_{p_i v_j}(p,v)=0.
\tag{M.12}
\]
Combining (M.11) and (M.12) yields \(2F_{p_j}(p,v)=0\) for every \(j\). Thus \(F(\cdot,v)\) is constant on the convex set \(O\), by integrating its zero derivative along segments. The case \(v=0\) is already zero. Therefore \(D(p,q)=F(p,q-p)\) is the distance of a single seminorm when \(D\) is smooth off the diagonal.

Return to merely continuous \(D\). Around any point choose the ball \(U\) and pseudometrics \(D_\varepsilon\) of M.1. The smooth case just proved applies to each \(D_\varepsilon\) on \(U\), so its speed \(F_\varepsilon(p,v)\) is independent of \(p\in U\). For \(p,q\in U\) and fixed \(v\), choose one \(h>0\) such that \(p+hv,q+hv\in U\). Uniform convergence in M.1, or just convergence at these four points, gives
\[
F(p,v)=\lim_{\varepsilon\to0}
       \frac{D_\varepsilon(p,p+hv)}h
       =\lim_{\varepsilon\to0}
       \frac{D_\varepsilon(q,q+hv)}h
       =F(q,v).
\]
Consequently \(F(\cdot,v)\) is locally constant on \(O\). A locally constant function on a connected set is constant: the preimage of one of its values and its complement are both open, and a nontrivial such partition would contradict connectedness. The convex set \(O\) is connected, since its line segments connect its points and intervals are connected by Local tools 0.0. Thus the seminorm is independent of \(p\) throughout \(O\). Denote it by \(N\). We have proved (M.6) on open convex sets.

For a general \(C\), translate a chosen point to zero and identify its affine span with \(V=\mathbb R^n\). If \(n=0\), \(C\) is a point and the unique seminorm on \(V=0\) proves the result. Suppose \(n>0\). There are \(x_0,\ldots,x_n\in C\) whose differences \(x_i-x_0\), \(i>0\), are a basis of \(V\): choose a basis from the spanning set \(C-x_0\). Their convex hull lies in \(C\). In these basis coordinates, the set of combinations with all barycentric coordinates strictly positive is open and nonempty, and contains a small Euclidean ball. Hence \(C\) has nonempty interior \(O\) relative to its affine span.

That interior is convex. For example, if \(B(o,r)\subset C\) and \(x\in C\), then for every \(0<t\le1\) convexity gives
\[
B((1-t)x+to,\ tr)\subset C.
\tag{M.13}
\]
The same observation with two interior points shows that their intervening segment consists of interior points. It also shows that each \(x\in C\) is a limit of interior points \((1-t)x+to\) as \(t\downarrow0\). The open-set argument gives a seminorm \(N\) on \(V\) representing \(D\) on \(O\).

For \(x,y\in C\), let \(x_t=(1-t)x+to\), \(y_t=(1-t)y+to\), with \(o\) as in (M.13). Both lie in \(O\) for \(0<t\le1\), so
\[
D(x_t,y_t)=N((1-t)(y-x))=(1-t)N(y-x).
\]
Continuity of \(D\) gives (M.6) on letting \(t\downarrow0\). Finally any seminorm satisfying (M.6) must obey
\[
N(v)=D(o,o+hv)/h
\]
for every \(v\in V\) and sufficiently small \(h>0\), since \(o\) is an interior point. This determines it uniquely. All seminorms obtained above are finite and continuous in finite dimension: for a basis \(e_i\), the triangle inequality gives
\(N(\sum_i a_i e_i)\le\sum_i|a_i|N(e_i)\), and
\(|N(v)-N(w)|\le N(v-w)\).
This also verifies the usual finite-dimensional meaning of the seminorm conclusion. □

**Corollary M.3 (affine images and product projections).** Let \(C\) be a nonempty linearly convex subset of a real normed vector space, possibly infinite-dimensional. Suppose \(f:C\to Y\) is continuous and sends every chosen linear segment to a constant-speed minimizing segment with the same normalized parameter, allowing a constant image. Then \(f(C)\), with the induced metric, is affine. Its chosen image segment depends only on its two image endpoints, and it is the unique segment selection that makes \(f\) preserve the chosen segments.

In particular, the projection of an affine subset of a metric product onto either factor is affine with the induced selection. Two parallel chosen segments in that affine subset, with the same displacement vector and parameter interval, have the same projected speed.

**Proof.** Put \(D(x,y)=d_Y(f(x),f(y))\). This is a continuous pseudometric and the assumed parametrization gives exactly (M.1). Fix \(o\in C\). For every finite subset \(S\subset C\) containing \(o\), let \(C_S\) be its convex hull and \(V_S=\operatorname{span}(S-o)\). The finite-dimensional parametrization of \(V_S\) into the original normed space is continuous: for chosen basis vectors \(e_i\), the norm inequality
\(\|\sum_i a_i e_i\|\le\sum_i|a_i|\|e_i\|\) proves this directly. Consequently the restriction of \(D\) to \(C_S\) is continuous in finite-dimensional coordinates. M.2 gives a unique seminorm \(N_S\) on \(V_S\) representing that restricted pseudometric.

If \(S\subset T\), the restriction \(N_T|_{V_S}\) represents \(D\) on \(C_S\), so uniqueness in M.2 makes it equal to \(N_S\). Two arbitrary finite sets have the common finite enlargement \(S\cup T\), so these seminorms agree on all overlapping vector subspaces. Every vector in
\[
V=\operatorname{span}(C-o)=\operatorname{span}(C-C)
\]
belongs to some \(V_S\), because its expression is a finite linear combination. We can therefore define \(N(v)=N_S(v)\) whenever \(v\in V_S\). This is well-defined. Homogeneity and the triangle inequality follow by placing any finitely many vectors involved into one common \(V_S\). Thus \(N\) is a seminorm on \(V\), and \(D(x,y)=N(y-x)\) for all \(x,y\in C\).

Let \(K=\{v\in V:N(v)=0\}\). Homogeneity and the triangle inequality make \(K\) a linear subspace. The two triangle inequalities
\(N(v+k)\le N(v)\) and \(N(v)\le N(v+k)\), for \(k\in K\), make
\[
\|[v]\|=N(v)
\]
a well-defined norm on the vector-space quotient \(V/K\): its only zero vector is the zero coset, and the other norm axioms descend from \(N\). No completeness of this normed space is asserted or needed.

Define
\[
I:f(C)\longrightarrow V/K,\qquad I(f(x))=[x-o].
\tag{M.14}
\]
This is well-defined and injective because
\[
f(x)=f(y)
\quad\Longleftrightarrow\quad D(x,y)=0
\quad\Longleftrightarrow\quad [x-o]=[y-o].
\]
Moreover
\(\|I(f(y))-I(f(x))\|=N(y-x)=d_Y(f(x),f(y))\), so it is an isometric embedding. Its image is linearly convex, since it is the image of the convex set \(C-o\) under a linear quotient map. This proves that \(f(C)\) is affine.

Under (M.14), the point \(f((1-t)x+ty)\) is the affine combination
\((1-t)[x-o]+t[y-o]\). It therefore depends only on \(f(x),f(y)\) and \(t\), independent of their chosen preimages. These combinations give the stated image segments, compatible with reversal and restriction to any subsegment. Any segment selection preserved by \(f\) must assign these same points at every \(t\), since the image points have preimages in \(C\); this proves uniqueness.

For a factor projection of a metric product, distance nonincrease in L.1 gives continuity, and the same lemma sends each chosen source segment to a constant-speed minimizing segment. The result just proved applies. For two source segments with the same displacement vector \(v\), the representing seminorm of this projection gives
\[
d_Y(f(x+sv),f(x+tv))=|t-s|N(v).
\tag{M.15}
\]
The right side is independent of \(x\). Thus the projected speeds are equal, as asserted. □

## N. Compatible affine subsets and product structure

A **consistent segment selection** on a metric space \(X\) assigns a constant-speed minimizing segment
\(\sigma_{xy}:[0,1]\to X\) to each ordered pair, with
\[
\sigma_{yx}(t)=\sigma_{xy}(1-t),\qquad
\sigma_{\sigma_{xy}(s),\sigma_{xy}(t)}(u)
 =\sigma_{xy}((1-u)s+ut).
\tag{N.1}
\]
Here \(s,t,u\in[0,1]\); a repeated endpoint gives the constant segment. A subset is compatible with the selection when it contains every selected segment between its points, with the restricted selection. It is **compatibly affine** if it has an isometric embedding into a real normed vector space whose image is linearly convex and whose selected segments become the ordinary linear segments. No finite-dimensionality or completeness is part of this definition.

The three-point construction and maximal-subset arguments originate in [Foertsch–Lytchak, arXiv:math/0605419v1, §3.2](https://arxiv.org/abs/math/0605419v1). We give the cone, vector-space and norm constructions explicitly, including the translation identity needed to make the norm well-defined.

**Theorem N.1 (three-point recognition).** Suppose a metric space has a consistent segment selection, and each three points lie in a compatibly affine subset. Then the whole space is compatibly affine.

**Proof.** The empty space is the empty convex subset of the zero vector space, so suppose \(X\ne\varnothing\). Fix \(o\in X\) and, for \(0<r\le1\), put \(h_r(x)=\sigma_{ox}(r)\). Compute in a compatible affine subset containing \(o,x,y\), translating its image so that \(o\) goes to zero. There \(h_r\) is multiplication by \(r\). Consequently
\[
\begin{aligned}
d(h_r x,h_r y)&=r\,d(x,y),\\
h_r(\sigma_{xy}(t))&=\sigma_{h_r x,h_r y}(t),\\
h_rh_s&=h_{rs}\qquad(0<r,s\le1).
\end{aligned}
\tag{N.2}
\]
The last equality also follows directly from (N.1). In particular every \(h_r\) is injective. Although the compatible subsets used for different pairs can differ, all three identities are identities between the specified points of \(X\), and therefore hold globally.

First adjoin all positive dilations about \(o\). Use pairs \((x,a)\in X\times(0,\infty)\). Declare
\[
(x,a)\sim(y,b)
\quad\Longleftrightarrow\quad
h_{\varepsilon a}x=h_{\varepsilon b}y
\quad\text{for some }\varepsilon>0
\text{ with }\varepsilon a,\varepsilon b\le1.
\tag{N.3}
\]
If the equality holds for one admissible \(\varepsilon\), it holds for every smaller one by applying \(h_r\). It also holds for every larger admissible one: applying the injective contraction from that larger scale to the known smaller scale makes the two points equal. Thus “some” can be replaced by “every” admissible scale. Reflexivity and symmetry follow at once; for transitivity, shrink to one scale admissible for all three pairs and use equality in \(X\). This proves that (N.3) is an equivalence relation.

Let \(Z\) be its quotient. All pairs \((o,a)\) represent one point, denoted \(0\). Define
\[
\delta([(x,a)],[(y,b)])
 =\varepsilon^{-1}d(h_{\varepsilon a}x,h_{\varepsilon b}y)
\tag{N.4}
\]
at any admissible scale. The first and third identities of (N.2) show that changing the scale leaves the answer unchanged. Replacing either representative also leaves it unchanged, by (N.3) at a common smaller scale. It is symmetric and nonnegative. Its zero pairs are exactly (N.3), so it is positive definite on \(Z\). For three points choose a common scale and apply the triangle inequality in \(X\), multiplied by \(\varepsilon^{-1}\). Hence \(\delta\) is a metric.

For \(\lambda>0\) put \(S_\lambda[(x,a)]=[(x,\lambda a)]\), and put \(S_0z=0\). Formula (N.3) makes these maps well-defined, and (N.4) gives
\[
S_\lambda S_\mu=S_{\lambda\mu},\qquad
\delta(S_\lambda z,S_\lambda w)=\lambda\delta(z,w).
\tag{N.5}
\]
This holds also at zero, with the stated convention; positive dilations are bijections with inverse \(S_{1/\lambda}\). The map \(I:X\to Z\), \(I(x)=[(x,1)]\), is isometric by using scale \(1\) in (N.4).

Every finite set of points of \(Z\) lies in one dilated copy \(S_L I(X)\). Indeed, for representatives \((x_j,a_j)\) choose \(L\ge\max_j a_j\); then
\[
[(x_j,a_j)]=S_L I(h_{a_j/L}x_j).
\tag{N.6}
\]
These copies are nested as \(L\) increases. Give \(Z\) a segment selection as follows: for \(z=S_L I(x)\) and \(w=S_L I(y)\), set
\[
\sigma^Z_{zw}(t)=S_L I(\sigma_{xy}(t)).
\tag{N.7}
\]
If \(L'\ge L\), the representatives in the larger copy are \(h_{L/L'}x,h_{L/L'}y\). The second identity of (N.2) makes (N.7) unchanged. Two arbitrary choices of \(L\) can be compared in a still larger copy, so this defines a single segment. It is minimizing with constant speed by (N.5), and is consistent and reversible because these statements can be checked in one copy of \(X\). Dilations preserve this selection. Moreover
\[
\sigma^Z_{0z}(t)=S_tz.
\tag{N.8}
\]
Each triple of points in \(Z\) lies in a compatibly affine subset: put the triple in \(S_L I(X)\), take the assumed compatible affine subset in \(X\), and dilate it. Its normed-space model is rescaled by \(L\). Thus the original three-point property holds in \(Z\) as well.

Write \(m(z,w)=\sigma^Z_{zw}(1/2)\) and define
\[
z+w=S_2m(z,w),\qquad \lambda z=S_\lambda z\quad(\lambda\ge0).
\tag{N.9}
\]
Commutativity follows from reversal, and \(z+0=z\) follows from (N.8). Since dilations preserve selected midpoints, they distribute over this addition. On a selected ray, midpoint and dilation computations give
\[
az+bz=(a+b)z\qquad(a,b\ge0).
\tag{N.10}
\]
For clarity, choose \(L\ge a,b\), regard \(az,bz\) as points on the segment from \(0\) to \(Lz\), and use (N.1) to identify their midpoint with \(((a+b)/2)z\); (N.9) then proves (N.10).

More generally,
\[
(1-t)z+tw=\sigma^Z_{zw}(t)\qquad(0\le t\le1).
\tag{N.11}
\]
To prove this, take an affine subset containing \(0,z,w\) and send \(0\) to the origin of its model. It contains \((1-t)z\), \(tw\), their midpoint, and \(\sigma^Z_{zw}(t)\). In that model the midpoint of the first two points is half of the last point. This means intrinsically that it is \(S_{1/2}\sigma^Z_{zw}(t)\), by (N.8). Apply \(S_2\) and (N.9).

Addition is associative. For \(x,y,z\in Z\), the distribution of positive dilations over addition and (N.11) give
\[
\begin{aligned}
\tfrac13((x+y)+z)
 &=\sigma^Z_{m(x,y),z}(1/3),\\
\tfrac13(x+(y+z))
 &=\sigma^Z_{x,m(y,z)}(2/3).
\end{aligned}
\tag{N.12}
\]
Both right sides belong to any compatible affine subset containing \(x,y,z\). In its model they are the same average of those three points. Injectivity of \(S_{1/3}\) proves associativity. Addition is also cancellative: if \(x+y=x+z\), then \(m(x,y)=m(x,z)\); in an affine subset containing \(x,y,z\), equality of these midpoints implies \(y=z\).

The metric is invariant under addition:
\[
\delta(x+z,y+z)
 =2\delta(m(x,z),m(y,z))
 =\delta(x,y).
\tag{N.13}
\]
The first equality is (N.5) and (N.9). For the second, use an affine subset containing \(x,y,z\): the difference of the two midpoint images is half the difference of the images of \(x,y\). This is the needed translation identity, proved without assuming a norm on \(Z\).

We now form differences. On \(Z\times Z\) put
\[
(x,y)\approx(u,v)\quad\Longleftrightarrow\quad x+v=u+y.
\tag{N.14}
\]
It is an equivalence relation. Only transitivity needs a calculation: if \(x+v=u+y\) and \(u+b=a+v\), then
\(x+v+b=a+v+y\), so cancellation gives \(x+b=a+y\). Denote the quotient by \(W\), with classes \([x,y]\). Set
\[
[x,y]+[u,v]=[x+u,y+v],\quad
-[x,y]=[y,x],\quad 0_W=[0,0].
\tag{N.15}
\]
Adding the two equalities (N.14) shows that addition does not depend on representatives; reversal of that equality does the same for negatives. Associativity and commutativity descend from \(Z\), \([x,x]=0_W\), and (N.15) gives additive inverses. Thus \(W\) is an abelian group. The map \(j:Z\to W\), \(j(z)=[z,0]\), is injective by cancellation and preserves addition.

For \(\lambda\ge0\), define \(\lambda[x,y]=[\lambda x,\lambda y]\); for negative \(\lambda\), define it by applying a positive scalar and then the negative in (N.15). Distribution of dilations over addition makes this independent of representatives and distributive over vector addition. Products of scalars act as their product by (N.5). Addition of nonnegative scalars is respected by (N.10). For opposite signs, it suffices to check \(a\ge b\ge0\):
\[
a[x,y]-b[x,y]
 =[ax+by,ay+bx]
 =[(a-b)x,(a-b)y].
\tag{N.16}
\]
The last equality follows because the first pair is obtained from the second by adding the same point \(b(x+y)\) to both entries, using (N.10). The case \(b>a\) follows by taking the negative. These checks prove all scalar distributive identities, so \(W\) is a real vector space.

Define
\[
\|[x,y]\|=\delta(x,y).
\tag{N.17}
\]
If \(x+v=u+y\), then (N.13) gives
\[
\delta(x,y)
 =\delta(x+v,y+v)
 =\delta(u+y,v+y)
 =\delta(u,v).
\]
Thus (N.17) is well-defined. It is zero exactly for \(x=y\), which is exactly the zero class. It is absolutely homogeneous by (N.5) and symmetry. Finally,
\[
\begin{aligned}
\|[x,y]+[u,v]\|
 &=\delta(x+u,y+v)\\
 &\le\delta(x+u,y+u)+\delta(y+u,y+v)\\
 &=\delta(x,y)+\delta(u,v).
\end{aligned}
\tag{N.18}
\]
It is therefore a norm. Since \(j(z)-j(w)=[z,w]\), \(j\) is an isometric embedding. Formula (N.11) makes \(j(Z)\) linearly convex and takes its selected segments to linear segments. The same is true of \(jI(X)\) by (N.7). This is the required compatible affine model of \(X\). □

**Corollary N.2 (maximal compatible affine extensions).** Every affine subset \(Y\) of a metric space \(X\), with a specified compatible segment selection on \(Y\), is contained in a maximal affine subset whose selection extends that of \(Y\). Maximality is with respect to both inclusion and extension of the selected segments.

**Proof.** We use ordinary set theory with choice, in its well-ordering formulation. We spell out the maximality argument. Consider all pairs \((A,\sigma^A)\) consisting of a subset \(Y\subset A\subset X\) and a consistent selection making \(A\) compatibly affine and agreeing with the given selection on \(Y\). These pairs form a set: their selections are functions on subsets of \(X^2\times[0,1]\) with values in \(X\). Order them by inclusion of the subsets and agreement of the selections on the smaller subset. This is a partially ordered set and is nonempty, since it contains \(Y\) with its original selection.

Every nonempty chain has an upper bound. Take the union \(A\) of its subsets. For any two points of \(A\), one member of the chain contains both; use its selected segment. Agreement on nested members makes the definition independent of the member. The consistency identities can be checked in a single member containing the two endpoints, so this is a consistent selection on \(A\). Each triple of points lies in a single member, which is affine and compatible with the union selection. Theorem N.1 makes \(A\) compatibly affine. It is an upper bound in the stated partially ordered set. The empty chain has the initial pair \(Y\) as an upper bound.

Here is why this chain property gives a maximal pair. Well-order the set of pairs, and scan it in that order, retaining a pair exactly when it is comparable with every previously retained pair. To justify the scan, consider all partial assignments of “retain” or “discard” on initial segments of this well-order satisfying that rule. Any two partial assignments agree on their common domain: a least point of disagreement would have identical earlier decisions and hence identical required decisions. Their union is therefore an assignment on an initial segment and satisfies the rule. If a least unassigned point remained, its decision could be appended according to the rule, producing a larger partial assignment than the union of all of them. This contradiction shows that the union is a scan of the entire well-ordered set.

The retained set is a chain. Any discarded pair was incomparable with a retained pair at its turn and remains so; hence no discarded pair can be added to the final chain. Let \(u\) be an upper bound of the final chain, whose existence was just proved. It is comparable with every retained pair, so it was itself retained: otherwise its earlier reason for exclusion would still be an incomparable retained pair. If \(v\ge u\), then \(v\) too is comparable with every retained pair and hence retained. Since \(u\) is an upper bound of all retained pairs, \(v\le u\), and therefore \(v=u\). Thus \(u\) is maximal. Its subset and selection give the claimed extension. No metric completeness or dimension bound enters the argument. □

A subset \(C\subset Y\times Z\) is **rectangular** if it equals \(P_Y(C)\times P_Z(C)\) under the given product identification.

**Corollary N.3 (rectangularity of maximal affine subsets).** A maximal compatible affine subset of a metric space is rectangular for every finite metric-product decomposition of that space. The product selections on its projections agree with its given selection.

**Proof.** It suffices first to treat \(X=Y\times Z\). If \(C\) is empty, both projections are empty and the assertion holds. Otherwise let \(C\) have its given affine model. Corollary M.3 makes \(A=P_Y(C)\) and \(B=P_Z(C)\) affine and gives them the unique selections preserved by the two projections. Choose compatible isometric models \(A\subset V\), \(B\subset W\) in real normed spaces. The formula
\[
\|(v,w)\|_\oplus=(\|v\|_V^2+\|w\|_W^2)^{1/2}
\tag{N.19}
\]
is a norm: definiteness and homogeneity are immediate; the two component triangle inequalities and then the Euclidean norm triangle inequality prove its triangle inequality, as in L.1. The set \(A\times B\) is linearly convex in \(V\oplus W\) with this norm, and its metric agrees with the one induced from \(Y\times Z\). It is therefore an affine subset of \(X\).

It contains \(C\). Each of its selected segments between two points of \(C\) has coordinate segments equal to the projections of the selected segment of \(C\), by M.3. Equality of both coordinates proves that the product selection extends the given one on \(C\). Maximality thus gives \(C=A\times B\), with the stated compatibility. For finitely many factors, apply M.3 to every projection and the same construction with the norm \((\sum_i\|v_i\|^2)^{1/2}\); the identical inclusion and extension argument proves the result. An empty subset again has empty projections if there is at least one factor. A product of no factors is a point; its only maximal affine subset is that point, so that case also agrees with the conclusion. □

**Corollary N.4 (transport of projected speeds).** Let a nonempty geodesic metric space have two product decompositions
\[
X=Y\times\bar Y=Z\times\bar Z.
\]
Fix a constant-speed minimizing segment \(\gamma:[a,b]\to Y\), \(a<b\). The speeds of the projections of \(t\mapsto(\gamma(t),\bar y)\) to \(Z\) and to \(\bar Z\) do not depend on \(\bar y\in\bar Y\). In particular, if \(Y_x\subset Z_x\) for one point \(x\in X\), then \(Y_{x'}\subset Z_{x'}\) for every \(x'\in X\).

**Proof.** Lemma L.1 makes all four factors geodesic and makes the indicated projections constant-speed minimizing segments. If \(\gamma\) has speed zero, its lifts and projections are constant, so all the asserted speeds are zero. Suppose its speed is \(c>0\). For \(\bar y_0,\bar y_1\in\bar Y\), choose a constant-speed minimizing segment \(\eta:[0,1]\to\bar Y\) between them, with speed \(d=d_{\bar Y}(\bar y_0,\bar y_1)\). If \(d=0\), the two points coincide and there is nothing to compare. If \(d>0\), the map
\[
[a,b]\times[0,1]\longrightarrow X,\qquad
(t,s)\longmapsto(\gamma(t),\eta(s))
\tag{N.20}
\]
is an isometric embedding when the rectangle is given the norm distance
\[
\|(u,v)\|=(c^2u^2+d^2v^2)^{1/2}.
\]
Indeed its squared distance between \((t,s)\) and \((t',s')\) is \(c^2|t-t'|^2+d^2|s-s'|^2\), by the first product decomposition. Its image is an affine subset with the selection obtained from the linear segments of this rectangle. The two sides \(s=0\) and \(s=1\) are parallel chosen segments with the same displacement and parameter interval. Apply M.3 to the projections for the second product decomposition. Their projected speeds agree. This proves the assertion for both projections and for arbitrary \(\bar y_0,\bar y_1\).

For the final assertion, write \(x=(y_0,\bar y_0)\) in the first product. Any two points of \(Y\times\{\bar y_0\}\) lie in the same \(Z\)-fibre, so their \(\bar Z\)-coordinates agree. Given any two \(y_1,y_2\in Y\), join them by a geodesic in \(Y\). Its lift at \(\bar y_0\) has zero \(\bar Z\)-projected speed because its projected endpoints coincide. The proved transport statement makes the projected speed zero at every other \(\bar y\). Thus the \(\bar Z\)-coordinate is constant on each whole fibre \(Y\times\{\bar y\}\). That fibre is contained in the \(Z\)-fibre through any of its points, proving the conclusion. □

## O. A common inner product for norm-product splittings

Different product decompositions of an affine space lead to different linear projections. We will need a single auxiliary inner product for which all the relevant projections are orthogonal. The reduction from a norm to such an inner product appears in [Foertsch–Lytchak, arXiv:math/0605419v1, §6.2](https://arxiv.org/abs/math/0605419v1). The proof here constructs a unique maximizing quadratic form and proves its required invariance directly.

**Lemma O.1 (simultaneous canonical orthogonality).** A finite-dimensional real normed vector space \(V\) has an inner product \(g\) such that every vector-space splitting \(V=U\oplus W\) satisfying
\[
\|u+w\|^2=\|u\|^2+\|w\|^2
\qquad(u\in U,\ w\in W)
\tag{O.1}
\]
is \(g\)-orthogonal. The same \(g\) works for all such splittings.

**Proof.** The zero-dimensional case has its unique inner product. Otherwise fix temporary coordinates \(V=\mathbb R^n\), with Euclidean norm \(|\cdot|\), and let \(K=\{x:\|x\|\le1\}\). For the coordinate basis, the norm triangle inequality gives
\[
\|x\|\le\sum_i|x_i|\|e_i\|\le C|x|
\]
for a finite positive \(C\), by the Euclidean Cauchy inequality of Local tools 0.0. Thus \(\|\cdot\|\) is Euclidean-continuous, since
\(|\|x\|-\|y\||\le\|x-y\|\le C|x-y|\).
On the compact Euclidean unit sphere it attains a positive minimum \(c\), by Local tools 0.1. The minimum is positive because a norm vanishes only at zero, which is not on the sphere. Homogeneity now gives
\[
c|x|\le\|x\|\le C|x|,\qquad
\{x:|x|\le C^{-1}\}\subset K
\subset\{x:|x|\le c^{-1}\}.
\tag{O.2}
\]

Consider the set \(\mathcal Q\) of real symmetric positive semidefinite matrices \(A\) such that
\[
x^{\mathsf T}Ax\le1\qquad\text{for every }x\in K.
\tag{O.3}
\]
Positive semidefiniteness means \(x^{\mathsf T}Ax\ge0\) for all \(x\). This and (O.3) are closed conditions on the finitely many matrix entries, and they are preserved by convex combinations. The first inclusion in (O.2) gives \(0\le a_{ii}\le C^2\). Positivity on vectors \(s e_i+t e_j\) gives
\[
|a_{ij}|^2\le a_{ii}a_{jj}\le C^4.
\tag{O.4}
\]
To see the first inequality, if \(a_{ii}>0\), substitute \(s=-a_{ij}t/a_{ii}\) in the nonnegative quadratic expression; if \(a_{ii}=0\), varying \(s\) with \(t=1\) forces \(a_{ij}=0\). Thus \(\mathcal Q\) is bounded and closed in a finite-dimensional coordinate space, hence compact by Local tools 0.1. It contains \(c^2I\), by the second inclusion in (O.2).

The determinant is a polynomial in the entries and therefore attains a maximum on \(\mathcal Q\). Let \(A_*\) be a maximizer. Its determinant is at least \(c^{2n}>0\). The real spectral theorem proved in H.2 diagonalizes a symmetric matrix in an orthonormal basis. Its eigenvalues here are nonnegative by positive semidefiniteness; their product is the determinant. Positivity of that product makes all eigenvalues positive, so \(A_*\) is positive definite.

We show uniqueness. We use the elementary determinant identities
\(\det(AB)=\det A\,\det B\) and \(\det A^{\mathsf T}=\det A\). They can be checked directly from the alternating multilinear column formula: when the columns of \(AB\) are expanded as combinations of the columns of \(A\), repeated-column terms vanish, and the remaining permutation terms sum to \(\det B\) times \(\det A\). Transposition leaves the permutation formula unchanged after replacing each permutation by its inverse.

Let \(A,B\) be positive definite. By H.2 and positive square roots of their eigenvalues, \(A^{1/2}\) and \(A^{-1/2}\) exist as symmetric positive definite matrices. Put
\[
T=A^{-1/2}BA^{-1/2}.
\]
It is positive definite, since
\(x^{\mathsf T}Tx=(A^{-1/2}x)^{\mathsf T}B(A^{-1/2}x)>0\) for \(x\ne0\).
Let its positive eigenvalues be \(\lambda_1,\ldots,\lambda_n\). The determinant identities and diagonalization give
\[
\begin{aligned}
\det\bigl((A+B)/2\bigr)
 &=\det A\prod_i\frac{1+\lambda_i}{2}\\
 &\ge\det A\prod_i\sqrt{\lambda_i}
 =\sqrt{\det A\,\det B}.
\end{aligned}
\tag{O.5}
\]
For each factor, \((1+\lambda)/2\ge\sqrt\lambda\) is equivalent to
\((\sqrt\lambda-1)^2\ge0\); equality holds exactly for \(\lambda=1\).
Equality throughout (O.5) therefore forces every \(\lambda_i=1\). Diagonalization then makes \(T=I\), hence \(A=B\). If two distinct members of \(\mathcal Q\) maximized the determinant, their midpoint would still belong to \(\mathcal Q\), and (O.5) would give a strictly larger determinant. This is impossible. The positive definite maximizer \(A_*\) is unique.

The associated inner product is
\[
g(x,y)=x^{\mathsf T}A_*y.
\tag{O.6}
\]
It does not depend on the temporary choice of coordinates. Under an invertible coordinate change \(x=Sy\), the same quadratic form has matrix \(S^{\mathsf T}AS\). This gives a bijection between the two feasible sets (O.3), and multiplies all determinants by the same positive constant \((\det S)^2\). It therefore takes the unique maximizer to the unique maximizer. This proves coordinate independence of the quadratic form, and hence of its polarization (O.6).

Now fix any splitting satisfying (O.1), and define the linear reflection
\[
R(u+w)=u-w.
\]
It is an involution and a norm isometry: (O.1) and \(\|-w\|=\|w\|\) give \(\|R(u+w)\|=\|u+w\|\). Hence it maps \(K\) onto \(K\). The matrix \(R^{\mathsf T}A_*R\) belongs to \(\mathcal Q\). Also \(R^2=I\), so determinant multiplication gives \((\det R)^2=1\), and
\[
\det(R^{\mathsf T}A_*R)=\det A_*.
\]
Uniqueness forces \(R^{\mathsf T}A_*R=A_*\), which says that \(R\) is a \(g\)-isometry. For \(u\in U\) and \(w\in W\),
\[
g(u,w)=g(Ru,Rw)=g(u,-w)=-g(u,w).
\]
Thus \(g(u,w)=0\). The construction of \(A_*\) used only the norm ball \(K\), not the chosen splitting. It therefore proves the assertion simultaneously for every splitting satisfying (O.1). □

## P. Linear products, convex refinement and transverse rigidity

The affine-to-linear reduction and the intersection mechanism below are needed for the metric decomposition theorem. The free source is [Foertsch–Lytchak, arXiv:math/0605419v1, §§6 and8](https://arxiv.org/abs/math/0605419v1). We prove the linear and convex prerequisites explicitly, keeping arbitrary convex subsets, including ones that are neither open nor closed.

**Lemma P.1 (linear extension of an affine metric product).** Let \(C\) be a nonempty convex subset of a finite-dimensional real normed vector space, with \(0\in C\), and put \(V=\operatorname{span}(C-C)\). Suppose its induced metric is a product of two metric spaces. Identify their fibres through \(0\) with subsets \(A,\bar A\subset C\), and their based projections with \(p,\bar p:C\to C\). Then \(A,\bar A\) are linearly convex. The projections extend uniquely to complementary linear projections \(P,I-P\) on \(V\), and
\[
C=A+\bar A,\qquad
V=U\oplus\bar U,\qquad
U=\operatorname{span}A,\quad \bar U=\operatorname{span}\bar A.
\tag{P.1}
\]
The sum representing each point is unique. Moreover,
\[
\|u+\bar u\|^2=\|u\|^2+\|\bar u\|^2
\qquad(u\in U,\ \bar u\in\bar U).
\tag{P.2}
\]
For any two such products, their extended projections are orthogonal projections for the same inner product supplied by O.1.

**Proof.** The set \(C\) is geodesic because its straight segments are minimizing. Lemma L.1 makes its factor fibres totally convex. Hence the straight segment between two points of \(A\), or two points of \(\bar A\), stays in that fibre. They are linearly convex, and both contain \(0\).

The based projection \(p:C\to A\) is distance nonincreasing and takes every straight source segment to a constant-speed minimizing segment by L.1. Corollary M.3 gives a unique image selection such that \(p\) preserves the selected source segments. For endpoints \(a,b\in A\), their straight segment already lies in \(A\), and \(p\) is the identity on it. Therefore the induced selection on \(A\) is precisely its straight-segment selection. Applying M.3 to arbitrary source endpoints gives
\[
p((1-t)x+ty)=(1-t)p(x)+tp(y)\qquad(x,y\in C,\ 0\le t\le1).
\tag{P.3}
\]
The identical conclusion holds for \(\bar p\), and both maps send \(0\) to \(0\).

We give the linear extension argument, including when \(0\) is a boundary point of \(C\). A map \(f:C\to V\) satisfying (P.3) and \(f(0)=0\) preserves every finite convex combination: combine the last term with the normalized combination of the preceding terms and induct on their number, omitting zero coefficients. If
\(\sum_{i=1}^k a_i x_i=0\), with \(x_i\in C\) and real \(a_i\), separate its positive and negative coefficients. Choose \(T>0\) at least as large as both sums of coefficient magnitudes. Dividing by \(T\) and adding the remaining weight at \(0\) gives two equal convex combinations in \(C\). Applying \(f\), with \(f(0)=0\), gives
\(\sum_i a_i f(x_i)=0\). Thus
\[
F\Bigl(\sum_i a_i x_i\Bigr)=\sum_i a_i f(x_i)
\tag{P.4}
\]
is independent of the representation. It is linear by combining finite sums. Since \(0\in C\), \(\operatorname{span}C=V\), so this defines a linear extension on all of \(V\), and spanning proves its uniqueness.

Extend \(p,\bar p\) to \(P,\bar P\) by (P.4). The product-coordinate identities on \(C\) give \(p^2=p\), \(\bar p^2=\bar p\), \(p\bar p=\bar p p=0\); their linear extensions satisfy the same identities because they agree on a spanning set. We also have \(p(x)+\bar p(x)=x\). To check this in the original vector space, compare the two points
\[
z=\tfrac12(p(x)+\bar p(x)),\qquad w=\tfrac12 x.
\]
Both belong to \(C\) by convexity. Equation (P.3) and the product-coordinate identities give
\(p(z)=p(w)=p(x)/2\) and \(\bar p(z)=\bar p(w)=\bar p(x)/2\).
The pair of product coordinates determines a point of \(C\), so \(z=w\). This proves the asserted sum, and hence \(P+\bar P=I\) on \(V\).

The image of \(P\) is \(\operatorname{span}p(C)=U\), and that of \(\bar P\) is \(\bar U\). The complementary projection identities prove the direct sum in (P.1). Every \(x\in C\) is \(p(x)+\bar p(x)\). Conversely, for \(a\in A\), \(\bar a\in\bar A\), the given metric product supplies a point \(x\in C\) with these two coordinates; the proved identity makes it \(a+\bar a\). Thus all combinations occur and the sum is unique.

For \(u\in U,\bar u\in\bar U\), choose a common \(h>0\) such that
\[
hu=a-b,\qquad h\bar u=\bar a-\bar b
\tag{P.5}
\]
for points \(a,b\in A\), \(\bar a,\bar b\in\bar A\). Such a choice is possible because a finite-dimensional convex set has nonempty interior in its affine span, as proved in the final part of M.2. More explicitly, choose an interior point of \(A\) in \(U\); a small ball about it lies in \(A\), so \(A-A\) contains a ball about zero in \(U\). Do the same for \(\bar A\) and shrink \(h\) for both specified vectors. A zero-dimensional factor uses only its zero vector. Product distance between \(a+\bar a\) and \(b+\bar b\) now gives
\[
\|h(u+\bar u)\|^2
 =\|a-b\|^2+\|\bar a-\bar b\|^2
 =h^2(\|u\|^2+\|\bar u\|^2).
\]
Divide by \(h^2\) to obtain (P.2). Lemma O.1 makes every such vector-space splitting orthogonal for a single inner product on \(V\). The linear projection along an orthogonal complement is exactly the orthogonal projection, so its restriction to \(C\) is still the original based projection. □

**Lemma P.2 (the two-projection normal form).** Let \(P,Q\) be orthogonal projections on a finite-dimensional real inner-product space \(V\). For \(i,j\in\{0,1\}\), set
\[
V_{ij}=\{v:Pv=iv,\ Qv=jv\}.
\]
There is an orthogonal decomposition
\[
V=V_{00}\oplus V_{01}\oplus V_{10}\oplus V_{11}\oplus W,
\qquad W=W_1\oplus W_0,
\tag{P.6}
\]
preserved by \(P,Q\), with \(P|_W\) the projection onto \(W_1\). The dimensions of \(W_1,W_0\) are equal. In suitable orthonormal bases \(e_1,\ldots,e_m\) of \(W_1\) and \(f_1,\ldots,f_m\) of \(W_0\),
\[
Q|_W=
\begin{pmatrix}\Lambda&D\\ D&I-\Lambda\end{pmatrix},
\quad
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_m),
\quad
D=\operatorname{diag}\bigl(\sqrt{\lambda_j(1-\lambda_j)}\bigr),
\quad 0<\lambda_j<1.
\tag{P.7}
\]
In particular \(D\) is invertible, and all four intersections of the two factor subspaces within \(W\) are zero.

The following are orthonormal bases of the image and kernel of \(Q|_W\), respectively:
\[
b_j=\sqrt{\lambda_j}\,e_j+\sqrt{1-\lambda_j}\,f_j,\qquad
\bar b_j=-\sqrt{1-\lambda_j}\,e_j+\sqrt{\lambda_j}\,f_j.
\tag{P.8}
\]
The maps \(Q:W_1\to QW\) and \(Q:W_0\to QW\) are both isomorphisms; the analogous assertions hold for \(I-Q\).

**Proof.** Distinct \(V_{ij}\)'s are orthogonal: at least one of \(P,Q\) has different eigenvalues on the two spaces, and self-adjointness gives
\((i-i')\langle v,w\rangle=0\) or \((j-j')\langle v,w\rangle=0\).
Each \(V_{ij}\) is invariant under both projections. Its orthogonal complement is invariant as well, since a self-adjoint map preserving a subspace preserves its orthogonal complement. Let \(W\) be the orthogonal complement of their sum. On \(W\), the image and kernel of \(P\) give the orthogonal splitting \(W_1\oplus W_0\). The restriction of \(Q\) has a block matrix
\[
Q=\begin{pmatrix}A&B\\ B^*&C\end{pmatrix},
\]
where \(A,C\) are self-adjoint and \(B:W_0\to W_1\). Its equation \(Q^2=Q\) gives
\[
BB^*=A-A^2,\qquad
AB+BC=B,\qquad
B^*B=C-C^2.
\tag{P.9}
\]

An orthogonal projection satisfies
\(\langle Qv,v\rangle=|Qv|^2\) and
\(|v|^2=|Qv|^2+|(I-Q)v|^2\).
For \(v\in W_1\), these identities imply
\(0\le\langle Av,v\rangle\le|v|^2\).
Diagonalize \(A\) by the real spectral theorem H.2. An eigenvector for eigenvalue \(0\) would have \(Qv=0\), and would belong to \(W\cap V_{10}=0\). An eigenvector for eigenvalue \(1\) would have \((I-Q)v=0\), and would belong to \(W\cap V_{11}=0\). Thus all its eigenvalues are strictly between \(0\) and \(1\). The same argument for \(v\in W_0\) excludes eigenvalues \(0,1\) for \(C\), using \(V_{00},V_{01}\).

It follows that \(A-A^2\) is positive definite on \(W_1\), and \(C-C^2\) is positive definite on \(W_0\). The first and third equations of (P.9) make \(B\) surjective and injective, respectively. To see surjectivity explicitly, \(BB^*\) is invertible on \(W_1\), so \(u=B(B^*(BB^*)^{-1}u)\) for every \(u\in W_1\). For injectivity, if \(Bv=0\), then
\(\langle(C-C^2)v,v\rangle=|Bv|^2=0\), so \(v=0\).
Hence \(\dim W_1=\dim W_0=m\).

Choose an orthonormal eigenbasis \(e_j\) for \(A\), with \(Ae_j=\lambda_j e_j\), and put
\[
d_j=\sqrt{\lambda_j(1-\lambda_j)},\qquad
f_j=d_j^{-1}B^*e_j.
\]
The numbers \(d_j\) are positive. The first equation of (P.9) gives
\[
\langle f_i,f_j\rangle
 =(d_i d_j)^{-1}\langle e_i,BB^*e_j\rangle
 =\delta_{ij}.
\]
Thus the \(f_j\)'s are an orthonormal basis of \(W_0\). We have
\(Bf_j=d_j e_j\).
Taking the adjoint of the middle equation of (P.9) gives
\(CB^*=B^*(I-A)\), so \(Cf_j=(1-\lambda_j)f_j\).
Together these are precisely the block formula (P.7).

Every intersection of an image or kernel of \(P|_W\) with an image or kernel of \(Q|_W\) is a joint \(0\)-\(1\) eigenspace. It is contained in \(W\cap V_{ij}\) and hence is zero. Alternatively this follows at once from the positive numbers \(d_j\).

Direct substitution in (P.7) gives \(Qb_j=b_j\) and \(Q\bar b_j=0\). For each \(j\), (P.8) is an orthogonal change of basis of the plane spanned by \(e_j,f_j\), and different such planes are perpendicular. Thus these vectors form the asserted bases. Finally
\[
Qe_j=\sqrt{\lambda_j}\,b_j,\qquad
Qf_j=\sqrt{1-\lambda_j}\,b_j,
\]
and the coefficients are nonzero. This proves both image isomorphisms; replacing \(Q\) by \(I-Q\) gives the other two. If \(m=0\), all of these statements are the corresponding zero-space assertions. □

**Theorem P.3 (common refinement of possibly nonclosed convex products).** Let \(C\subset V\) be linearly convex, contain \(0\), and span the finite-dimensional real inner-product space \(V\). Suppose it is rectangular for two orthogonal projections \(P,Q\):
\[
C=PC+(I-P)C=QC+(I-Q)C.
\tag{P.10}
\]
Each equality here asserts that every combination of the two projected coordinates occurs. In the decomposition (P.6), put \(C_{ij}=C\cap V_{ij}\). Then
\[
C=W+C_{00}+C_{01}+C_{10}+C_{11},
\tag{P.11}
\]
with independent choices in all five summands and unique representation. In particular, if
\(A=PC\), \(\bar A=(I-P)C\), \(B=QC\), \(\bar B=(I-Q)C\), then
\[
Q\bigl((A\cap B)+\bar A\bigr)=B.
\tag{P.12}
\]
If \(B\cap A=B\cap\bar A=\{0\}\), the whole subset \(B\) is a vector subspace. No closedness assumption on \(C\) is made.

**Proof.** Use the normal form P.2. We first establish translation invariance in \(W\) for the closure \(K=\overline C\), then prove it for \(C\) itself.

The set \(K\) is convex: approximate any two of its points by sequences in \(C\), take their convex combinations and pass to the limit. It is rectangular for both projections. For example the orthogonal-coordinate map
\(V\to PV\times(I-P)V\) is a linear isometry, and (P.10) identifies \(C\) with the Cartesian product \(PC\times(I-P)C\). Closure of a product of two subsets of metric spaces is the product of their closures: one inclusion follows by projecting a convergent sequence; for the other choose, for each positive integer \(n\), a point of each subset within \(1/n\) of the desired coordinate. Their pairs converge. Thus \(K\) is a product for \(P\), and the same argument applies to \(Q\). In particular, for \(p,z\in K\) and any
\[
R\in\{P,I-P,Q,I-Q\},
\]
the point \(p+R(z-p)\) belongs to \(K\).

At \(p\in K\), define its cone of supporting normals by
\[
\mathcal N_p=\{v:\langle v,z-p\rangle\le0
                         \text{ for every }z\in K\}.
\tag{P.13}
\]
This is a convex cone: the inequalities are preserved by addition and multiplication by nonnegative scalars. It is pointed, meaning that \(v,-v\in\mathcal N_p\) forces \(v=0\). Indeed those two inequalities make \(\langle v,z-p\rangle=0\) for every \(z\in K\). Taking \(z=0\) gives \(\langle v,p\rangle=0\); then \(v\) is orthogonal to all of \(K\). Since \(K\) contains the spanning subset \(C\), \(v=0\).

The cone is preserved by all four maps \(R\). If \(v\in\mathcal N_p\), the preceding rectangular point gives
\[
\langle Rv,z-p\rangle
 =\langle v,R(z-p)\rangle\le0,
\]
using self-adjointness. Hence \(Rv\in\mathcal N_p\).

These invariances and pointedness imply
\[
\mathcal N_p\subset W^\perp.
\tag{P.14}
\]
First, if \(w\in\mathcal N_p\cap W_0\), both \(PQw\) and \(P(I-Q)w=-PQw\) belong to the cone. Pointedness makes \(PQw=0\). In the block form (P.7), this is \(Dw=0\); invertibility of \(D\) gives \(w=0\). Similarly, for \(w\in\mathcal N_p\cap W_1\), the two cone elements \((I-P)Qw\) and \((I-P)(I-Q)w=-(I-P)Qw\) force \(w=0\).

For arbitrary \(v\in\mathcal N_p\), the vector
\((I-P)QPv\) also belongs to \(\mathcal N_p\). This composition kills every \(V_{ij}\), and takes \(W\) into \(W_0\). Therefore it is zero by the preceding paragraph. Its action on the \(W_1\)-component of \(v\) is the invertible off-diagonal map \(D\), so that component vanishes. Applying the same argument to \(PQ(I-P)v\) kills the \(W_0\)-component. This proves (P.14).

We claim that \(K+W=K\). Fix \(x\in K\), \(w\in W\), and suppose \(y=x+w\notin K\). There is a point \(p\in K\) minimizing \(|y-p|\). To prove attainment, take a sequence with distances decreasing to the infimum; its points eventually lie in a closed ball about \(y\) of radius \(|y-x|+1\). That ball is compact by Local tools 0.1, and \(K\) is closed, so a subsequence converges in \(K\) to a minimizer. Since \(y\notin K\), \(v=y-p\ne0\). For \(z\in K\), the points \(p+t(z-p)\) belong to \(K\) for \(0\le t\le1\). Minimality yields
\[
0\le |y-p-t(z-p)|^2-|y-p|^2
 =-2t\langle v,z-p\rangle+t^2|z-p|^2.
\]
Divide by \(t>0\) and let \(t\downarrow0\); then \(v\in\mathcal N_p\). By (P.14), \(v\perp W\). On the other hand, \(x\in K\) gives \(\langle v,x-p\rangle\le0\), whereas
\[
\langle v,x-p\rangle
 =\langle v,v-w\rangle=|v|^2>0.
\]
This contradiction proves \(K+W=K\).

We need an interior fact to return to the original set:
\[
\operatorname{int}C=\operatorname{int}\overline C.
\tag{P.15}
\]
Here the interior is in \(V\), and it is nonempty: a convex set spanning \(V\) and containing \(0\) contains a full-dimensional simplex, by the basis and simplex argument in M.2. The inclusion from left to right in (P.15) is immediate. To prove the other, let \(z\in\operatorname{int}K\) and choose coordinates with orthonormal basis \(e_1,\ldots,e_n\). If \(n=0\), both sets are the one-point space. Otherwise choose \(r>0\) small enough that all the points
\[
v_0=z-r\sum_{i=1}^n e_i,\qquad
v_i=z+r e_i\quad(1\le i\le n)
\]
lie in an open ball about \(z\) contained in \(K\). They are affinely independent and \(z=(v_0+\cdots+v_n)/(n+1)\). Affine independence follows, for example, by solving
\(\sum_{i=1}^n a_i(v_i-v_0)=0\): the coordinate equations give \(a_i+\sum_j a_j=0\), and summing gives \((n+1)\sum_j a_j=0\), hence all \(a_i=0\).

Since \(K=\overline C\), approximate each \(v_i\) by a point \(c_i\in C\), as closely as desired. The augmented matrix whose columns are \((v_i,1)\) is invertible; determinant continuity and the cofactor inverse formula in Local tools 0.4 show that the matrix with columns \((c_i,1)\) remains invertible and that the solution of
\[
\sum_i \alpha_i c_i=z,\qquad \sum_i\alpha_i=1
\]
stays close to \(\alpha_i=1/(n+1)\). For sufficiently close choices every \(\alpha_i\) is positive. The same inverse formula makes these barycentric coordinates continuous as \(z\) varies nearby, so they remain positive on a neighborhood of \(z\). That whole neighborhood lies in the convex hull of the \(c_i\)'s, hence in \(C\). Thus \(z\in\operatorname{int}C\), proving (P.15).

Translations by \(W\) take \(K\) onto itself and are homeomorphisms, so they take its interior onto itself. Equation (P.15) consequently gives
\[
\operatorname{int}C+W=\operatorname{int}C.
\tag{P.16}
\]
We now remove the interior restriction. Fix \(x\in C\) and choose \(y\in\operatorname{int}C\). Rectangularity of \(C\) says that each of the four maps \(R\) preserves \(C-x\), because
\(x+R(z-x)=Rz+(I-R)x\in C\) for \(z\in C\).
Therefore the compositions
\[
T=(I-P)QP,\qquad S=PQ(I-P)
\tag{P.17}
\]
preserve \(C-x\). For every \(w\in W\), (P.16) gives \(y+w\in C\), so
\[
x+T(y+w-x)\in C,\qquad x+S(y+w-x)\in C.
\]
Both \(T,S\) kill the four joint eigenspaces. By (P.7), \(T(W)=W_0\) and \(S(W)=W_1\), since their nonzero off-diagonal blocks are invertible. As \(w\) varies through \(W\), the two displayed sets are therefore \(x+W_0\) and \(x+W_1\). Thus both are contained in \(C\). For any \(w_1\in W_1,w_0\in W_0\), rectangularity for \(P\) combines \(x+w_1\) and \(x+w_0\) to give
\[
P(x+w_1)+(I-P)(x+w_0)=x+w_1+w_0\in C.
\]
We have proved
\[
C+W=C
\tag{P.18}
\]
for every point of \(C\), including its boundary points.

It remains to separate the four joint components. Set \(P_1=P,P_0=I-P\), and \(Q_1=Q,Q_0=I-Q\). Because \(0\in C\), each of these maps takes \(C\) into \(C\). For \(z\in C\), the joint-eigenspace component of \(P_iQ_jz\) is exactly the \(V_{ij}\)-component \(z_{ij}\) of \(z\); all other joint components are zero. Its remaining component lies in \(W\). By (P.18) this remaining component can be subtracted while staying in \(C\). Hence \(z_{ij}\in C\cap V_{ij}=C_{ij}\).

Conversely, choose any \(c_{ij}\in C_{ij}\). Rectangularity for \(Q\) gives \(c_{00}+c_{01}\in C\) and \(c_{10}+c_{11}\in C\). Rectangularity for \(P\) then combines the first of these, which is in \(\ker P\), with the second, which is in \(\operatorname{im}P\). Their sum belongs to \(C\). Equation (P.18) permits adding every \(w\in W\). This proves (P.11); its uniqueness is the vector-space direct sum (P.6).

Under (P.11) the based factors are
\[
\begin{aligned}
A&=W_1+C_{10}+C_{11},&
\bar A&=W_0+C_{00}+C_{01},\\
B&=QW+C_{01}+C_{11},&
A\cap B&=C_{11}.
\end{aligned}
\tag{P.19}
\]
The first three formulas follow by applying the projections to (P.11). The last uses that \(\operatorname{im}P\cap\operatorname{im}Q=V_{11}\), since their intersection in \(W\) is zero. By (P.8), \(Q(W_0)=QW\); \(Q\) kills \(C_{00}\) and fixes \(C_{01},C_{11}\). Applying \(Q\) to \((A\cap B)+\bar A\) therefore gives exactly \(QW+C_{01}+C_{11}=B\), proving (P.12).

Likewise \(B\cap\bar A=C_{01}\). If the two intersections in the final hypothesis are both \(\{0\}\), then \(C_{11}=C_{01}=\{0\}\), and (P.19) gives \(B=QW\), a vector subspace. This proves every conclusion without replacing \(C\) by its closure in the final answer. □

**Theorem P.4 (transverse squared-norm rigidity).** Let a finite-dimensional real normed vector space have two squared-norm product splittings
\[
V=U\oplus\bar U=Z\oplus\bar Z.
\]
If all four intersections \(U\cap Z,U\cap\bar Z,\bar U\cap Z,\bar U\cap\bar Z\) are zero, then the norm comes from an inner product and \(\dim V\) is even.

**Proof.** Lemma O.1 supplies an auxiliary inner product \(g\) making both splittings orthogonal. Let \(P,Q\) be their orthogonal projections onto \(U,Z\). The intersection hypothesis makes all four \(V_{ij}\) of P.2 zero. Thus \(V=W=W_1\oplus W_0\), \(\dim V=2m\), and \(Q\) has the form (P.7) with invertible \(D\). If \(m=0\), \(V=0\) and the conclusion is immediate. We assume \(m>0\) and use orthonormal coordinates for \(g\).

Put \(F(v)=\|v\|^2\). Norm continuity in these coordinates follows from the basis estimate in O.1. The two squared-norm splitting assumptions say
\[
F(v)=F(Pv)+F((I-P)v)
    =F(Qv)+F((I-Q)v).
\tag{P.20}
\]
We will prove that \(F\) is a positive definite quadratic form.

Choose smooth, nonnegative, even functions \(\rho_\varepsilon\) on \(V\) of integral \(1\), with support in coordinate boxes shrinking to \(0\). Such kernels are constructed as products of the one-variable normalized functions in the proof of M.1, using the explicit smooth cutoff of Local tools 0.5. Define
\[
F_\varepsilon(v)=\int F(v-a)\rho_\varepsilon(a)\,da.
\tag{P.21}
\]
These finite-dimensional integrals, their reordering and their uniform-limit properties were proved from rectangular Riemann sums in M.1. After the coordinate substitutions \(b=v-a\), formula (P.21) becomes
\(\int F(b)\rho_\varepsilon(v-b)\,db\).
For \(v\) in a neighborhood of any fixed point, the kernel and all its \(v\)-derivatives have support in one compact box of \(b\)'s. The same differentiation-under-the-integral proof in M.1 applies, differentiating only the smooth kernel. Hence \(F_\varepsilon\) is smooth. Evenness of \(F\) and of the kernel, with the substitution \(a\mapsto-a\), makes \(F_\varepsilon\) even. Uniform continuity of \(F\) on a larger compact box gives
\[
F_\varepsilon\longrightarrow F
\quad\text{uniformly on every compact subset of }V:
\tag{P.22}
\]
the difference from \(F(v)\) is bounded by the maximum of
\(|F(v-a)-F(v)|\) over the shrinking support, since the kernel is nonnegative and has integral \(1\).

Integrating the first equality of (P.20) shows that
\[
F_\varepsilon(u+w)=a_\varepsilon(u)+c_\varepsilon(w)
\qquad(u\in W_1,\ w\in W_0),
\tag{P.23}
\]
where
\[
a_\varepsilon(u)=\int F(u-Pa)\rho_\varepsilon(a)\,da,\qquad
c_\varepsilon(w)=\int F(w-(I-P)a)\rho_\varepsilon(a)\,da.
\]
These functions are smooth: for instance
\(a_\varepsilon(u)=F_\varepsilon(u)-c_\varepsilon(0)\), and similarly for \(c_\varepsilon\). Integrating the second equality of (P.20) likewise expresses \(F_\varepsilon\) as the sum of a function of \(Qv\) and a function of \((I-Q)v\).

Let \(H_\varepsilon(v)\) denote the Hessian of \(F_\varepsilon\), as a self-adjoint operator for \(g\). In coordinates this is the matrix of second partial derivatives; their symmetry follows from the mixed-derivative proof in M.2. Equation (P.23) gives
\[
H_\varepsilon(u+w)=
\begin{pmatrix}A_\varepsilon(u)&0\\0&C_\varepsilon(w)\end{pmatrix},
\tag{P.24}
\]
where each diagonal block depends only on its indicated variable. The corresponding separation for \(Q\) says that the Hessian also has zero mixed blocks between \(QV\) and \((I-Q)V\). Equivalently it commutes with \(Q\): an operator with those two invariant orthogonal blocks commutes with their projection, and conversely.

Multiply (P.24) and the block matrix (P.7) in both orders. Equality of the upper-right blocks gives
\[
A_\varepsilon(u)D=D C_\varepsilon(w)
\qquad\text{for every }u\in W_1,\ w\in W_0.
\tag{P.25}
\]
Since \(D\) is invertible, fixing \(w=0\) makes \(A_\varepsilon(u)\) independent of \(u\); fixing \(u=0\) makes \(C_\varepsilon(w)\) independent of \(w\). Thus the entire Hessian \(H_\varepsilon\) is constant on \(V\).

Integrating along straight lines twice, by Local tools 0.3, gives
\[
F_\varepsilon(v)
 =F_\varepsilon(0)+dF_\varepsilon|_0(v)
      +\tfrac12 g(H_\varepsilon v,v).
\]
Evenness forces \(dF_\varepsilon|_0=0\): its value at a vector is the derivative at zero of an even function on that line. Therefore
\[
q_\varepsilon(v):=F_\varepsilon(v)-F_\varepsilon(0)
 =\tfrac12 g(H_\varepsilon v,v)
\tag{P.26}
\]
is a quadratic form.

By (P.22) and \(F(0)=0\), \(q_\varepsilon(v)\to F(v)\) at every point. This limit is again a quadratic form, as can be seen without any compactness assertion about Hessians. For a fixed coordinate basis \(e_i\), write
\(q_\varepsilon(v)=\sum_{i,j}s^\varepsilon_{ij}v_i v_j\) with a symmetric coefficient matrix. Its diagonal entries are \(q_\varepsilon(e_i)\); for \(i\ne j\), its off-diagonal entries are
\[
s^\varepsilon_{ij}
 =\tfrac12\bigl(q_\varepsilon(e_i+e_j)
                    -q_\varepsilon(e_i)-q_\varepsilon(e_j)\bigr).
\]
All these finitely many entries converge. Let \(S=(s_{ij})\) be their symmetric limit. For arbitrary fixed \(v\), taking the limit in the finite sum yields
\[
F(v)=\sum_{i,j}s_{ij}v_i v_j.
\tag{P.27}
\]
The right side is positive for every nonzero \(v\), because the left side is the square of a norm. Consequently
\(g_N(u,v)=\sum_{i,j}s_{ij}u_i v_j\)
is a positive definite symmetric bilinear form, with
\(g_N(v,v)=\|v\|^2\). This is an inner product inducing the original norm. The even dimension was already established from P.2, completing the proof. □

## Q. Covering dimension and the finite affine-rank bound

The metric decomposition hypothesis concerns topological dimension. We must connect it to the dimensions of the normed vector spaces in which affine subsets are realized. The free source for the simplex and covering arguments is [Nikolai V. Ivanov, *The lemmas of Alexander and Sperner*, arXiv:1909.00940v1](https://arxiv.org/html/1909.00940v1), §3, §7 and Appendix A.1. We give the subdivision, incidence, parity and covering proofs here.

The standard \(n\)-simplex is
\[
\Delta^n=\{(t_0,\ldots,t_n):t_i\ge0,\ \sum_{i=0}^n t_i=1\}.
\tag{Q.1}
\]
Its vertices are the coordinate vectors \(e_0,\ldots,e_n\). A face is the convex hull of a nonempty subset of these vertices; equivalently, some specified coordinates vanish. A geometric \(d\)-simplex is the convex hull of \(d+1\) affinely independent points. Its barycentric coordinates are the unique nonnegative coefficients summing to one in that representation. Its relative interior consists of points with all those coefficients positive.

A finite triangulation of a simplex means a finite collection of geometric simplices, including all their faces, whose union is the given simplex and whose pairwise intersections are empty or common faces. Its mesh is the largest diameter of a member. We use Euclidean distance for this construction.

**Lemma Q.1 (small subdivisions and their facet incidences).** The simplex \(\Delta^n\) has finite triangulations \(T_k\), \(k=0,1,\ldots\), restricting to triangulations of every face, with mesh tending to zero. For \(n\ge1\) they can be chosen so that
\[
\operatorname{mesh}(T_k)\le
\left(\frac{n}{n+1}\right)^k\operatorname{diam}(\Delta^n).
\tag{Q.2}
\]
Every \((n-1)\)-simplex of \(T_k\) is a face of exactly one \(n\)-simplex if it lies in the boundary of \(\Delta^n\), and exactly two otherwise. The corresponding assertion holds in each face, with its own dimension and relative boundary.

**Proof.** Begin with the simplex and all its faces. For any nonempty face \(F\) of any member of a triangulation, let \(b_F\) be the average of its vertices. The barycentric subdivision consists of the convex hulls
\[
[b_{F_1},\ldots,b_{F_r}]
\quad\text{for all strict chains }\quad
F_1\subsetneq\cdots\subsetneq F_r
\tag{Q.3}
\]
of nonempty faces, and their faces. We verify both the geometry and the incidence count of this construction.

First work within a single \(d\)-simplex with vertices \(v_0,\ldots,v_d\). Fix a permutation \(\pi\) of \(\{0,\ldots,d\}\), and take the full chain with vertex sets
\[
\{v_{\pi(0)}\},\
\{v_{\pi(0)},v_{\pi(1)}\},\
\ldots,\
\{v_{\pi(0)},\ldots,v_{\pi(d)}\}.
\]
Write its barycenters as \(b_0,\ldots,b_d\). For a point with old barycentric coordinates \(t_i\), membership in their convex hull is equivalent to
\[
t_{\pi(0)}\ge t_{\pi(1)}\ge\cdots\ge t_{\pi(d)}\ge0.
\tag{Q.4}
\]
Indeed, on putting \(t_{\pi(d+1)}=0\), the coefficients in the new hull must be, and are,
\[
\lambda_j=(j+1)(t_{\pi(j)}-t_{\pi(j+1)})
\quad(0\le j\le d).
\tag{Q.5}
\]
Their sum telescopes to \(\sum_i t_i=1\), and the old coefficient of \(v_{\pi(i)}\) in \(\sum_j\lambda_jb_j\) is
\(\sum_{j=i}^d\lambda_j/(j+1)=t_{\pi(i)}\).
The same equations, applied to arbitrary affine coefficients, show that the \(b_j\)'s are affinely independent. Every shorter chain extends to a full chain by inserting missing vertex subsets, so its barycenters are affinely independent as well.

Sorting the \(t_i\)'s proves that these new simplices cover the old simplex. Their intersections are common faces. To see this precisely, in (Q.5) a positive coefficient occurs exactly at a strict drop between consecutive levels of the ordered coordinates. The corresponding set of the largest coordinates is uniquely determined by the point, independently of how coordinates tied at the same level are ordered. Thus, if the point belongs to two full-chain simplices, every new vertex with a positive coefficient in either representation is a vertex of both simplices. The point lies in the convex hull of their common vertices. The reverse inclusion is immediate; this hull is a face of each. The same assertion for faces of full-chain simplices follows by setting their missing coefficients equal to zero.

This construction agrees on shared old faces. More explicitly, a point of an old face has zero old coordinates outside that face. All barycentric coefficients of every \(b_F\) are nonnegative. Therefore a convex combination of new vertices lies in that old face only when every vertex with positive coefficient is itself in it. The intersection of a new simplex with an old face is consequently the face generated by its vertices in that face. These are exactly the chains constructed inside the face. Applying this observation on both sides of any shared old face proves the intersection property for the subdivided complex. It also proves compatibility with every face of the original simplex.

Here is the mesh estimate. The diameter of the convex hull of finitely many points is at most the largest pairwise distance between those points: for two convex combinations,
\[
\left|\sum_i a_iv_i-\sum_jc_jv_j\right|
\le\sum_{i,j}a_ic_j|v_i-v_j|
\le\max_{i,j}|v_i-v_j|,
\]
where \(a_i,c_j\ge0\) and both sums of coefficients are one. Equality holds for a pair realizing that maximum. If \(F\subsetneq G\) have \(a\) and \(b\) vertices, respectively, then
\[
b_G=\frac ab\,b_F+\frac{b-a}{b}\,b_{G\setminus F}.
\]
Both averages on the right belong to the old simplex. Consequently
\[
|b_G-b_F|\le\frac{b-a}{b}\operatorname{diam}(\text{old simplex})
\le\frac d{d+1}\operatorname{diam}(\text{old simplex}).
\tag{Q.6}
\]
Every pair of vertices in (Q.3) comes from nested faces. The diameter observation gives the same bound for the whole new simplex. Since \(d\le n\), one subdivision reduces the mesh by at least the factor \(n/(n+1)\). Repeated subdivision gives (Q.2), whose right side tends to zero. In dimension zero the simplex is a point, and its mesh is already zero.

It remains to prove the facet incidence assertion; it is not an assumption about the pictures of a triangulation. The initial complex has the required incidences, as does its restriction to each face. Suppose an old triangulation has these properties and every member is a face of an \(n\)-simplex, as is true initially. Every new simplex extends to a full chain in some old \(n\)-simplex, so this last property persists.

A new \((n-1)\)-simplex is a chain of \(n\) nonempty old faces. Their vertex counts are strictly increasing and belong to \(\{1,\ldots,n+1\}\), so precisely one count is missing. If the missing count is \(j\le n\), the chain already ends in an old \(n\)-simplex. The missing face must be inserted between a set of size \(j-1\) and one of size \(j+1\), taking the lower set to be empty when \(j=1\). There are exactly two choices, obtained by adding either of the two missing vertices. Hence the new facet belongs to exactly two new \(n\)-simplices.

Such a facet contains the barycenter of an old \(n\)-simplex, and so is not contained in the original boundary. Indeed every coordinate of that barycenter in (Q.1) is positive: if one coordinate vanished, its nonnegativity would force that coordinate to vanish at every old vertex, putting a full-dimensional old simplex in a proper face, which is impossible.

If instead the missing count is \(n+1\), the chain ends in an old \((n-1)\)-simplex \(\tau\). Its extensions are in bijection with the old \(n\)-simplices having \(\tau\) as a face. There is one or two by the inductive hypothesis. Furthermore the new facet is in the original boundary exactly when \(\tau\) is. One direction is inclusion. For the other, the new facet contains \(b_\tau\). If \(b_\tau\) is in the boundary, some original coordinate of this average is zero; nonnegativity makes that coordinate zero at every vertex of \(\tau\), so \(\tau\) lies in that boundary face. This proves both the incidence count and its boundary characterization after subdivision. Running the same argument in each original face proves all the asserted relative versions. Induction completes the proof. □

**Lemma Q.2 (Sperner parity and a balanced image).** Label every vertex \(v\) of \(T_k\) by an index \(i\in\{0,\ldots,n\}\), with the requirement that \(v_i>0\). Then the number of \(n\)-simplices whose labels are all \(0,\ldots,n\) is odd.

Consequently, if a continuous map \(f:\Delta^n\to\Delta^n\) satisfies
\[
x_i=0\ \Longrightarrow\ f_i(x)=0,
\tag{Q.7}
\]
its image contains the barycenter \((1/(n+1),\ldots,1/(n+1))\).

**Proof.** Prove the parity assertion by induction on \(n\). For \(n=0\) there is one vertex and its only possible label is zero. Suppose \(n\ge1\). Count pairs \((\tau,\sigma)\) for which \(\sigma\) is a top-dimensional small simplex and \(\tau\) is one of its facets with labels exactly \(0,\ldots,n-1\).

By Q.1 each interior such facet is counted twice and each boundary such facet once. A simplex contained in the boundary lies in one original boundary face: some coordinate of the average of its vertices is zero, and nonnegativity makes that coordinate zero at every vertex. A boundary facet with the specified labels must therefore lie in the original face \(x_n=0\), since lying in \(x_i=0\) for \(i<n\) would forbid the required label \(i\). Its labels on \(x_n=0\) satisfy the same boundary rule in dimension \(n-1\). The restriction of \(T_k\) there is its iterated barycentric subdivision, by Q.1. Induction therefore says that the number of these boundary facets is odd. The total pair count is odd.

Now count the pairs by their top simplex. A simplex carrying all \(n+1\) labels has exactly one qualifying facet, obtained by deleting the vertex labelled \(n\). A simplex carrying precisely the \(n\) labels \(0,\ldots,n-1\) has exactly two qualifying facets: among its \(n+1\) vertices exactly one of these labels occurs twice, and one may delete either occurrence. Every other simplex has no qualifying facet. Thus the parity of the total count is the parity of the number of fully labelled simplices. The latter is odd, proving the induction step.

For the continuous-map assertion, at every vertex of \(T_k\) choose a label \(i\) for which \(f_i(v)\) is maximal. Since the coordinates of \(f(v)\) are nonnegative and sum to one, this maximum is at least \(1/(n+1)>0\). Condition (Q.7) ensures \(v_i>0\), so the labelling is allowed.

Choose a fully labelled small simplex, and denote its vertex with label \(i\) by \(v_{k,i}\). Then
\[
f_i(v_{k,i})\ge\frac1{n+1}
\quad(0\le i\le n).
\tag{Q.8}
\]
The set \(\Delta^n\) is closed and bounded, hence compact by Local tools 0.1. A subsequence of \(v_{k,0}\) converges to a point \(x\in\Delta^n\). Along the same subsequence,
\[
|v_{k,i}-v_{k,0}|\le\operatorname{mesh}(T_k)\longrightarrow0,
\]
so every \(v_{k,i}\) tends to \(x\). Continuity and (Q.8) imply \(f_i(x)\ge1/(n+1)\) for every \(i\). Their sum is one, so each is exactly \(1/(n+1)\). For \(n=0\) this conclusion is immediate from the one-point domain and codomain. □

For a metric space \(S\), we use the following definition of its **covering dimension**. The empty space has dimension \(-1\). For a nonempty space, \(\dim S\le d\), where \(d\) is a nonnegative integer, means that every finite open cover has a finite open refinement in which each point belongs to at most \(d+1\) members. A refinement still covers \(S\), and each of its members is contained in a member of the original cover. The dimension is the least such integer, or infinity if there is none. Empty cover members may always be discarded.

**Theorem Q.3 (simplex dimension and closed subsets).** A normed \(n\)-simplex has covering dimension at least \(n\). If \(A\) is a closed subset of a metric space \(S\), then
\[
\dim A\le\dim S.
\tag{Q.9}
\]
Covering dimension is unchanged by homeomorphisms.

**Proof.** First consider \(\Delta^n\), with \(n\ge1\), and the open cover
\[
U_i=\{x\in\Delta^n:x_i>0\},\qquad 0\le i\le n.
\tag{Q.10}
\]
Suppose it had a finite open refinement \(V_1,\ldots,V_N\) such that each point belongs to at most \(n\) members. Choose \(i(j)\) with \(V_j\subset U_{i(j)}\). Every \(V_j\) is proper, since the corresponding \(U_{i(j)}\) omits a vertex. Define
\[
w_j(x)=\operatorname{dist}(x,\Delta^n\setminus V_j).
\]
The complement is nonempty, so these functions are finite. The triangle inequality gives
\[
|w_j(x)-w_j(y)|\le |x-y|:
\]
bound \(|x-z|\) by \(|x-y|+|y-z|\), take the infimum over the complement, and exchange \(x,y\). Thus \(w_j\) is continuous. It is zero outside \(V_j\), and positive inside: a sufficiently small ball about an interior point misses the complement. Since the \(V_j\)'s cover, \(w(x)=\sum_jw_j(x)>0\) everywhere.

Put
\[
f_i(x)=\frac{\sum_{j:\,i(j)=i}w_j(x)}{w(x)}.
\tag{Q.11}
\]
These are continuous nonnegative functions summing to one. If \(x_i=0\), then \(x\notin U_i\), hence every summand in the numerator is zero. Thus they define a map satisfying (Q.7). At each point at most \(n\) of the \(w_j\)'s are nonzero. Therefore at most \(n\) of the \(n+1\) coordinates \(f_i\) are positive. The image misses the barycenter, contradicting Q.2. The cover (Q.10) has no such refinement, so \(\dim\Delta^n\ge n\). For \(n=0\) the conclusion says only that a point has nonnegative dimension, which follows from the definition.

An affine bijection from \(\Delta^n\) onto the convex hull of \(n+1\) affinely independent points in a normed space is a homeomorphism onto that hull. Here no infinite-dimensional norm comparison is needed: restrict to the finite-dimensional span of their differences. The norm/coordinate comparison proved in O.1 gives positive constants \(c,C\) bounding its norm between \(c\) and \(C\) times the Euclidean coordinate norm. Applying these bounds to differences proves continuity of the affine map and of its inverse. Homeomorphism invariance of covering dimension follows directly by carrying open covers and refinements in both directions; the numbers of members containing a point are preserved. This transfers the lower bound to every normed \(n\)-simplex and proves the last assertion of the theorem.

Finally suppose \(A\subset S\) is closed. The assertion is immediate if \(A\) is empty or \(\dim S=\infty\); if \(S\) is empty, so is \(A\). Otherwise let \(\dim S=d<\infty\), and let \(U_1,\ldots,U_m\) be a finite cover of \(A\) by sets open in \(A\). Choose open \(O_i\subset S\) with \(O_i\cap A=U_i\). Then
\[
O_1,\ldots,O_m,\ S\setminus A
\]
is a finite open cover of \(S\). Choose a finite open refinement of multiplicity at most \(d+1\). Intersect its members with \(A\) and discard empty intersections. The remaining sets cover \(A\), have multiplicity at most \(d+1\), and each refines some \(U_i\): a member contained in \(S\setminus A\) has empty intersection with \(A\). This is the required refinement. Since the original cover of \(A\) was arbitrary, (Q.9) follows. □

An affine metric space is, as in M–N, a metric space isometric to a convex subset of a real normed vector space; its realization supplies the selected straight segments. Following [Foertsch–Lytchak, arXiv:math/0605419v1, introduction](https://arxiv.org/abs/math/0605419v1), define the **affine rank**
\[
\operatorname{rank}_{\mathrm{aff}}X
=\sup\{\dim C:C\text{ is an affine metric space
admitting an isometric embedding into }X\}.
\tag{Q.12}
\]
The dimension inside this supremum is covering dimension. All spaces \(X\) considered from here on are nonempty.

For the proof it is useful to have an integer defined by vector-space dimension. Define \(a(X)\) to be the supremum of the finite integers
\[
\dim\operatorname{span}(C-C)
\tag{Q.13}
\]
over all nonempty finite-dimensional normed convex realizations \(C\) admitting an isometric embedding into \(X\). The supremum ranges over realizations as well as subsets, so no invariance of a chosen realization is presupposed. A point supplies the value zero.

**Theorem Q.4 (the finite affine-rank bridge).** If \(\operatorname{rank}_{\mathrm{aff}}X\) is finite, then \(a(X)\) is a finite nonnegative integer, its defining supremum is attained, and
\[
a(X)\le\operatorname{rank}_{\mathrm{aff}}X.
\tag{Q.14}
\]
Every normed convex realization of every affine subset of \(X\), including an initially infinite-dimensional realization, has finite-dimensional span of differences of dimension at most \(a(X)\).

**Proof.** Let \(C\) be any such realization, and fix \(c_0\in C\). We have
\[
\operatorname{span}(C-C)=\operatorname{span}\{c-c_0:c\in C\},
\tag{Q.15}
\]
because each difference is the difference of two vectors on the right, and every generator on the right belongs to \(C-C\). If this span has dimension at least \(n\), choose \(c_1,\ldots,c_n\in C\) for which \(c_i-c_0\) are linearly independent. They can be chosen successively: if the vectors already chosen do not span the whole space, (Q.15) supplies another generator outside their span.

The convex hull \(K=[c_0,\ldots,c_n]\) lies in \(C\). It is a normed \(n\)-simplex and is compact: the continuous affine parametrization from the compact \(\Delta^n\) maps onto it. A continuous image of a compact set is compact, since the inverse images of an open cover admit a finite subcover. In a metric space every compact set is closed. Indeed, for a point \(x\notin K\), the positive continuous function \(y\mapsto d(x,y)\) on \(K\) has a positive minimum, so an open ball about \(x\) misses \(K\). The minimum assertion follows, for example, by taking a sequence approaching the infimum and a convergent subsequence in the compact simplex parametrizing \(K\). Thus \(K\) is closed in \(C\), whether or not \(C\) itself is closed.

Theorem Q.3 now gives
\[
n\le\dim K\le\dim C\le\operatorname{rank}_{\mathrm{aff}}X.
\tag{Q.16}
\]
If the span of differences of \(C\) were infinite-dimensional, the construction would work for every finite \(n\), contradicting finite affine rank. If it has finite dimension \(m\), apply the same construction with \(n=m\) to get \(m\le\operatorname{rank}_{\mathrm{aff}}X\).

It follows that all integers in (Q.13) belong to a finite set of nonnegative integers. That set is nonempty, since it contains zero, so it has a largest element and the supremum is attained. This proves finiteness and (Q.14). We have also proved that every initially arbitrary realization can be restricted, after translation by \(c_0\), to a finite-dimensional normed span. Its dimension is therefore among the values admitted in (Q.13), and is at most \(a(X)\). This proves the last assertion. □

**Theorem Q.5 (additive working rank and maximal affine subsets).** Suppose \(X=Y\times Z\) is a nonempty metric product of finite affine rank. Then its factors have finite affine rank, and
\[
a(X)=a(Y)+a(Z).
\tag{Q.17}
\]
Every nonpoint geodesic space of finite affine rank has \(a\ge1\). Every maximal compatible affine subset of \(X\) has finite-dimensional span and is rectangular for every metric product decomposition of \(X\).

Moreover, in the geodesic case the parallel-fibre inclusion of N.4 is available without any further finite-dimensional, completeness or closedness assumption: if one \(Y\)-fibre is contained in a \(W\)-fibre for two products \(X=Y\times Z=W\times\bar W\), the same containment holds at every point.

**Proof.** Fix a point in each factor. The based factor fibres are isometric copies of \(Y,Z\) inside \(X\). Every affine space embedding into either factor therefore embeds into \(X\), so its covering dimension is bounded by \(\operatorname{rank}_{\mathrm{aff}}X\). Both factors have finite affine rank, and Q.4 applies to all three spaces.

Choose convex normed models \(A,B\) realizing the largest integers \(a(Y),a(Z)\), whose existence is Q.4. Their product, with the squared-sum norm
\[
\|(u,v)\|_\oplus=(\|u\|_A^2+\|v\|_B^2)^{1/2},
\]
is a convex normed model embedding isometrically into \(Y\times Z\). This is a norm by the product-norm proof in N.3: apply the two factor triangle inequalities and then the Euclidean triangle inequality to the pairs of their nonnegative lengths. Its span of differences is the direct sum of the two spans. To check equality rather than just inclusion, fix \(a_0\in A,b_0\in B\); the differences of \((a,b_0),(a_0,b_0)\) span the first summand, and those of \((a_0,b),(a_0,b_0)\) span the second. Thus
\[
a(X)\ge a(Y)+a(Z).
\tag{Q.18}
\]

For the reverse inequality take any convex normed model \(C\) embedding isometrically into \(X\), and let \(f:C\to X\) be the embedding. Translate the model so that \(0\in C\), and put \(V=\operatorname{span}(C-C)\). By Q.4 this is finite-dimensional. Compose \(f\) with the two coordinate projections. These maps are continuous and take each straight source segment to a constant-speed minimizing segment, including a constant segment when its projected speed is zero, by L.1. Corollary M.3 realizes their images as normed convex sets \(C_Y,C_Z\), with induced selected straight segments, in such a way that the two maps
\[
p:C\to C_Y,\qquad q:C\to C_Z
\]
preserve all convex combinations of two points. Translate these target models so that \(p(0)=q(0)=0\). Their spans \(V_Y,V_Z\) are finite-dimensional by Q.4, since the models embed into the respective factors.

The linear extension argument (P.4), which requires only preservation of convex combinations and a zero basepoint, extends \(p,q\) to linear maps
\[
P:V\to V_Y,\qquad Q:V\to V_Z.
\]
For clarity, it works with these different codomains in exactly the stated way: split any real linear relation among points of \(C\) into positive and negative parts, normalize by a common total and pad with the point zero. Preservation of the resulting equal convex combinations gives the same relation among their images. Hence the extension formula is independent of representation and is linear.

The combined map \(T=(P,Q)\) is injective. The isometric embedding and the product distance first give, for \(c,d\in C\),
\[
\|c-d\|^2
=\|p(c)-p(d)\|_Y^2+\|q(c)-q(d)\|_Z^2.
\tag{Q.19}
\]
As proved in M.2, a finite-dimensional convex set has nonempty relative interior in its affine span. Since \(0\in C\) and it spans \(V\), choose a small ball about an interior point contained in \(C\). Its difference with its centre shows that \(C-C\) contains a neighborhood of zero in \(V\). For each \(v\in V\), therefore, some \(h>0\) satisfies \(hv=c-d\) for points \(c,d\in C\). Substitute in (Q.19), use linearity and divide by \(h^2\). This yields
\[
\|v\|^2=\|Pv\|_Y^2+\|Qv\|_Z^2.
\tag{Q.20}
\]
If \(Tv=0\), then \(v=0\), proving injectivity. The image of a basis under an injective linear map is linearly independent, so finite-dimensional linear algebra gives
\[
\dim V\le\dim V_Y+\dim V_Z\le a(Y)+a(Z).
\]
This holds for every realization in the definition of \(a(X)\). Taking its maximum and combining with (Q.18) proves (Q.17). Point factors and zero-dimensional spans satisfy the same equations.

If a geodesic space contains distinct points at distance \(\ell>0\), a minimizing constant-speed segment between them is an isometric copy of the normed interval \([0,\ell]\). Indeed the distance between two points on that segment is the difference of their arclength parameters. This affine subset has one-dimensional span, so \(a\ge1\).

Every affine subset extends to a maximal compatible one by N.2. Theorem Q.4 makes its normed span finite-dimensional. Theorem N.3 makes it rectangular for every product decomposition: its coordinate images, with the induced selections of M.3, have an affine product whose selection extends the original one, and maximality forces equality. Thus finite-dimensional linear product extension P.1 applies to these maximal subsets whenever needed.

Finally, the last assertion is exactly the fibre-inclusion propagation proved in N.4. Its proof uses an affine rectangle obtained from one geodesic in each factor and equality of projected speeds on parallel sides, proved in M.3. Factors of a geodesic product are geodesic by L.1. These hypotheses hold here, and the argument imposes neither completeness nor closedness. This proves the assertion with its full stated scope. □

## R. Intersecting factors and transverse metric rigidity

We use the free [Foertsch–Lytchak preprint, arXiv:math/0605419v1, §§5–6 and8.1](https://arxiv.org/abs/math/0605419v1), together with the complete finite-dimensional results P.1–P.4. The next two arguments first describe a projected subset as a product and then prove that the subset is the whole factor. Keeping these steps separate makes the role of finite affine rank explicit.

Throughout this section,
\[
X=Y\times\bar Y=Z\times\bar Z
\tag{R.1}
\]
are two product decompositions of a nonempty geodesic metric space. Fix \(x=(o,\bar o)\) in the first product. Based fibres and based projections have the meanings given in L. In particular \(P^{Z_x}\) takes its values in the actual subset \(Z_x\subset X\).

**Lemma R.1 (the product inside a projection image).** Put
\[
F_x=Y_x\cap Z_x,\qquad F=P^Y(F_x)\subset Y,\qquad
T=F\times\bar Y\subset X,
\]
and
\[
S=P^{Z_x}(T),\qquad G=P^{Z_x}(\bar Y_x).
\tag{R.2}
\]
Then there is a surjective product isometry
\[
F_x\times G\longrightarrow S
\tag{R.3}
\]
which identifies the two axes through \((x,x)\) with the subsets \(F_x\) and \(G\) themselves. No dimension or completeness assumption is required for this assertion.

**Proof.** First we prove the translation property of the intersections. For \(y,y'\in Y\), the equality
\[
P^{\bar Z}(y,\bar y)=P^{\bar Z}(y',\bar y)
\tag{R.4}
\]
is independent of the chosen \(\bar y\in\bar Y\). Choose a geodesic in \(Y\) between \(y,y'\), which exists by L.1. At a value of \(\bar y\) where (R.4) holds, its lifted segment has zero \(\bar Z\)-projected speed, since that speed is its projected endpoint distance divided by the parameter interval length. Corollary N.4 makes that speed zero at every other value of \(\bar y\), giving (R.4) there. Reversing the roles of the two values proves the equivalence. If \(y=y'\), the assertion holds directly.

At any fixed \(\bar y\), equality of the \(\bar Z\)-coordinates is an equivalence relation on \(Y\). The preceding argument shows that this relation is the same for every \(\bar y\). Its class containing \(o\) is exactly \(F\). Consequently, for every \(p=(y,\bar y)\in T\),
\[
Y_p\cap Z_p=F\times\{\bar y\}.
\tag{R.5}
\]
Indeed its \(Y\)-coordinate must be in the equivalence class of \(y\), which is the class \(F\) of \(o\).

For each \(\bar y\in\bar Y\), define
\[
\phi_{\bar y}:F\to Z_x,\qquad
\phi_{\bar y}(y)=P^{Z_x}(y,\bar y),\qquad
E_{\bar y}=\phi_{\bar y}(F).
\tag{R.6}
\]
All points of \(F\times\{\bar y\}\) lie in the same \(Z\)-fibre by (R.5). Their \(\bar Z\)-coordinates are equal, so the second product metric says that \(P^{Z_x}\) preserves their mutual distances. The first product metric identifies those distances with distances in \(F\subset Y\). Thus \(\phi_{\bar y}\) is an isometry onto \(E_{\bar y}\); it is in particular injective. These nonempty subsets cover \(S\).

For \(\bar y,\bar v\in\bar Y\), set
\[
T_{\bar y\bar v}=\phi_{\bar v}\phi_{\bar y}^{-1}
:E_{\bar y}\to E_{\bar v}.
\tag{R.7}
\]
Their identity, inverse and composition rules in (L.5) follow by cancellation of the bijections \(\phi\). We verify the distance condition as well.

Take \(y,y'\in F\) and put
\[
p=(y,\bar y),\qquad r=(y,\bar v),\qquad q=(y',\bar v).
\]
Then \(p\in\bar Y_r\) and \(q\in Y_r\cap Z_r\) by (R.5). Lemma L.3, based at \(r\), gives
\[
d(P^{Z_r}p,q)^2
=d(P^{Z_r}p,r)^2+d(r,q)^2.
\tag{R.8}
\]
All points in this equation belong to \(Z_r\). Replacing their common \(\bar Z\)-coordinate by that of \(x\) is an isometry from \(Z_r\) to \(Z_x\). Under it the three points \(P^{Z_r}p,r,q\) become
\(\phi_{\bar y}(y),\phi_{\bar v}(y),\phi_{\bar v}(y')\), respectively. Hence (R.8) becomes
\[
\begin{aligned}
d(\phi_{\bar y}(y),\phi_{\bar v}(y'))^2
&=d(\phi_{\bar y}(y),\phi_{\bar v}(y))^2\\
&\quad+d(\phi_{\bar v}(y),\phi_{\bar v}(y'))^2.
\end{aligned}
\tag{R.9}
\]
This is precisely condition (L.6) for (R.7).

Apply the product-recognition lemma L.2 to the sets \(E_{\bar y}\) covering \(S\). It gives \(S\cong E_{\bar o}\times J\), where \(J\) identifies indices defining the same subset and has distance
\[
\delta([\bar y],[\bar v])
=d(\phi_{\bar y}(o),\phi_{\bar v}(o)).
\tag{R.10}
\]
Here we used the constant-displacement conclusion of L.2 and evaluated it at the common \(F\)-coordinate \(o\). Thus
\[
[\bar y]\longmapsto\phi_{\bar y}(o)
\]
is an isometry of \(J\) onto \(G\): its image is \(P^{Z_x}(\{o\}\times\bar Y)\), which is \(G\), and (R.10) gives both well-definedness and injectivity on zero-distance classes.

Finally \(E_{\bar o}=F_x\), since \(P^{Z_x}\) fixes every point of \(F_x\). The product-recognition map takes \(((y,\bar o),[\bar y])\) to \(\phi_{\bar y}(y)\). If \([\bar y]=[\bar o]\), it fixes \((y,\bar o)\); if \(y=o\), it gives the corresponding point \(\phi_{\bar y}(o)\) of \(G\). These are exactly the axis identifications in (R.3). Repeated indices or point factors cause no difficulty, because L.2 already proved that its equal-subset quotient is a metric space. □

**Theorem R.2 (intersections are metric factors).** If \(X\) in (R.1) has finite affine rank, then the projection in (R.2) is onto the entire factor:
\[
P^{Z_x}(T)=Z_x.
\tag{R.11}
\]
Consequently \(F_x=Y_x\cap Z_x\) is a metric product factor of both \(Z_x\) and \(Y_x\). More precisely, (R.3) is an isometry
\[
F_x\times P^{Z_x}(\bar Y_x)\longrightarrow Z_x
\tag{R.12}
\]
with the same based-axis identifications.

**Proof.** Let \(z\in Z_x\). Choose a geodesic from \(x\) to \(z\). Its image lies in \(Z_x\) by the total convexity of product fibres, L.1. This image is an affine interval with its chosen geodesic selection, or a point if \(z=x\). Corollary N.2 extends it to a maximal compatible affine subset \(C\subset X\).

Theorem Q.4 makes the span of a normed convex model of \(C\) finite-dimensional. Translate that model so that \(x\) is zero. Corollary N.3 makes \(C\) rectangular for both decompositions in (R.1), with compatible selections. Its based factor fibres are exactly
\[
A=C\cap Y_x,\quad \bar A=C\cap\bar Y_x,\quad
B=C\cap Z_x,\quad \bar B=C\cap\bar Z_x.
\tag{R.13}
\]
For example, because \(x\in C\), rectangularity implies \(P^{Y_x}(C)\subset C\), and this image is \(C\cap Y_x\); the other assertions follow in the same way.

Lemma P.1 extends these two products of \(C\) to linear squared-norm splittings of its finite-dimensional span. Lemma O.1 makes both pairs of projections orthogonal for one inner product, so Theorem P.3 applies to this actual convex model, including when it is not closed. Its conclusion (P.12) says
\[
P^{B}\bigl((A\cap B)+\bar A\bigr)=B.
\tag{R.14}
\]
Here \(P^B\) is the extended linear based projection, whose restriction to \(C\) is \(P^{Z_x}\), by P.1. In particular, since \(z\in B\), there are \(a\in A\cap B\) and \(\bar a\in\bar A\) for which
\[
t=a+\bar a\in C,\qquad P^{Z_x}t=z.
\]
The addition describes the product coordinates proved in P.1: \(t\) combines the \(Y\)-coordinate of \(a\) with the \(\bar Y\)-coordinate of \(\bar a\). Since \(a\in Y_x\cap Z_x=F_x\), its \(Y\)-coordinate belongs to \(F\). Thus \(t\in F\times\bar Y=T\).

We have proved \(z\in P^{Z_x}(T)\) for every \(z\in Z_x\); the reverse inclusion is the definition of that projection. This proves (R.11). Lemma R.1 now gives (R.12). Interchanging the names of the two products gives the corresponding factorization of \(Y_x\) with the same intersection \(F_x\). All metrics on the intersection are the induced metric from \(X\), so these are factorizations by the same metric space. No global completeness assumption was used. □

We now assume that the products (R.1) are transverse at the chosen point, in the following precise sense:
\[
Y_x\cap Z_x=Y_x\cap\bar Z_x
=\bar Y_x\cap Z_x=\bar Y_x\cap\bar Z_x=\{x\}.
\tag{R.15}
\]
These are intersections of whole based fibres, rather than tangent spaces; the metric space need not have tangent spaces.

**Lemma R.3 (maximal affine subsets through a transverse point).** Suppose \(X\) has finite affine rank and (R.15) holds. Every maximal compatible affine subset \(C\) containing \(x\), with \(x\) as origin, is an entire finite-dimensional Euclidean vector space of even dimension. Write its based fibres as \(A,\bar A,B,\bar B\) in (R.13). Each is a vector subspace, and the based projections restrict to isomorphisms
\[
P^{Z_x}:A\longrightarrow B,\qquad
P^{Z_x}:\bar A\longrightarrow B,\qquad
P^{\bar Y_x}:B\longrightarrow\bar A,\qquad
P^{Y_x}:B\longrightarrow A.
\tag{R.16}
\]
In particular, any subset of \(X\) which is rectangular for both products and contains either \(A\) or \(\bar A\) must contain \(C\).

**Proof.** By N.3 and Q.4, \(C\) is rectangular for both products and has a convex model with finite-dimensional span \(V\). Translate its model so that \(x=0\). Lemmas P.1 and O.1 supply the two linear orthogonal projections on \(V\) representing its based fibre projections.

Condition (R.15) gives
\[
A\cap B=\bar A\cap B=A\cap\bar B=\bar A\cap\bar B=\{0\}.
\tag{R.17}
\]
The final conclusion of P.3 makes \(B\) a vector subspace of \(V\), since it has zero intersections with both \(A,\bar A\). Apply that same conclusion with the second projection replaced by its complement to see that \(\bar B\) is a vector subspace. By P.1, \(C=B+\bar B\); it is therefore a vector subspace. Since its span of differences is \(V\), it follows that \(C=V\).

The first pair of based projections now gives \(A=PV,\bar A=(I-P)V\), and the second gives \(B=QV,\bar B=(I-Q)V\). Thus (R.17) is the zero-intersection hypothesis on whole linear subspaces required by P.4. That theorem proves that the original norm comes from an inner product and that \(\dim V=2m\) for an integer \(m\ge0\). Choosing an orthonormal basis, by successive subtraction of projections and normalization as in A.1, identifies \(C\) isometrically with \(\mathbb R^{2m}\).

The isomorphisms in (R.16) also follow from the proved normal form. In P.2 all four joint eigenspaces are zero, so its transverse part \(W\) is all of \(V\). Its last conclusion makes \(Q:A\to B\) and \(Q:\bar A\to B\) isomorphisms. Interchanging \(P,Q\) gives the isomorphisms from \(B\) to \(A\) and to \(\bar A\). These linear maps are the actual based projections on \(C\), as established in P.1. The assertions include zero-dimensional spaces.

Let \(D\subset X\) be rectangular for both products and contain \(A\). Since \(x\in A\), it contains \(x\); hence it is preserved by every based projection at \(x\). Indeed a based projection combines one coordinate of a point of \(D\) with the other coordinate of \(x\), which lies in \(D\) by rectangularity. The first isomorphism in (R.16) gives \(B=P^{Z_x}(A)\subset D\), and the third gives \(\bar A=P^{\bar Y_x}(B)\subset D\). Rectangularity for the first product then gives every combination \(A\times\bar A=C\) inside \(D\). If \(D\) instead contains \(\bar A\), the second and fourth isomorphisms give \(B\subset D\) and \(A\subset D\), and the same conclusion follows. □

**Theorem R.4 (transverse metric rigidity).** If a nonempty geodesic metric space \(X\) of finite affine rank has two product decompositions satisfying (R.15) at one point, then
\[
X\cong\mathbb R^{2m}
\tag{R.18}
\]
isometrically for some \(m\ge0\). The case \(m=0\) means that \(X\) is a point. No completeness assumption is needed.

**Proof.** Use N.2 to choose a maximal compatible affine subset \(C\) containing \(x\). The one-point subset with its constant selection is an allowed starting subset. By R.3, \(C\) is an entire Euclidean vector space, with the two pairs of vector-subspace fibres \(A,\bar A,B,\bar B\).

We first justify a compatibility fact that will be needed when applying maximality. In a Euclidean space every constant-speed minimizing segment is the straight segment with that parameter. To prove it, at an intermediate parameter \(t\in(0,1)\) of a segment \(\gamma\), set \(u=\gamma(t)-\gamma(0)\) and \(v=\gamma(1)-\gamma(t)\). The segment distances give
\[
|u+v|=|u|+|v|,\qquad |u|=t\ell,\quad |v|=(1-t)\ell,
\]
where \(\ell=|\gamma(1)-\gamma(0)|\). If \(\ell>0\), squaring the first equality and using the inner-product formula yields
\(\langle u,v\rangle=|u||v|\), whence
\[
\left|u/|u|-v/|v|\right|^2=0.
\]
The two vectors therefore have the same direction with the specified lengths, and \(\gamma(t)=(1-t)\gamma(0)+t\gamma(1)\). If \(\ell=0\), the segment is constant. Endpoint parameters follow directly.

Consequently, if \(C\subset C_0\subset X\) and both subsets are Euclidean for their induced metrics, the chosen straight segment of \(C\) is the chosen straight segment of \(C_0\) between those endpoints. Its inclusion is still a constant-speed minimizing segment because the two metrics are restrictions of the same metric on \(X\), and uniqueness in \(C_0\) gives the assertion. Thus such an inclusion automatically preserves the affine selections.

Now take any \(z\in\bar Y_x\). By L.1 the factor \(\bar Y\) is geodesic, so choose a minimizing segment \(\gamma\) from \(x\) to \(z\) inside \(\bar Y_x\). Form the subset
\[
\widetilde C
=P^Y(A)\times P^{\bar Y}(\gamma)
\subset Y\times\bar Y=X.
\tag{R.19}
\]
It is affine: \(A\) is a Euclidean vector space by R.3, and the geodesic image is isometric to a closed interval, or a point if \(z=x\). Their product is a convex subset of a normed vector space with the squared-sum norm, as proved in N.3. Give \(\widetilde C\) that product selection. It contains the actual subsets \(A\) and \(\gamma\), with the selection on \(A\) equal to its Euclidean one.

By N.2 there is a maximal compatible affine extension \(C_0\) of \(\widetilde C\). It is also maximal among all affine pairs: any larger compatible extension would still extend the given selection on \(\widetilde C\). It contains \(x\), so R.3 applies to \(C_0\), making it an entire Euclidean vector space. It is rectangular by N.3 and contains \(A\); the last assertion of R.3 for \(C\) therefore gives \(C\subset C_0\).

The compatibility fact just proved shows that the selection on \(C_0\) extends the selection on \(C\). Maximality of the affine pair \(C\) now applies and gives \(C_0=C\). In particular \(z\in\gamma\subset C\), so \(z\in C\cap\bar Y_x=\bar A\). Since \(z\) was arbitrary and the opposite inclusion holds by definition,
\[
\bar Y_x=\bar A.
\tag{R.20}
\]

For the other fibre, take any \(z\in Y_x\), choose a geodesic there from \(x\) to \(z\), and form its product with \(\bar A\). A maximal compatible extension is again Euclidean and rectangular, and now contains \(\bar A\). The other case of R.3 gives that it contains \(C\). The same segment-compatibility argument and maximality give equality with \(C\), proving
\[
Y_x=A.
\tag{R.21}
\]
Since \(X=Y\times\bar Y\), every point of \(X\) is the combination of one coordinate from \(Y_x=A\) and the other from \(\bar Y_x=\bar A\). The subset \(C\) is rectangular and contains both axes, so it contains every such point. Hence \(X=C\). Lemma R.3 identifies this space with \(\mathbb R^{2m}\), proving (R.18). All arguments, including the maximality comparison, also cover the point case. □

## S. The metric decomposition and its isometries

We now assemble the decomposition argument from the free [Foertsch–Lytchak preprint, arXiv:math/0605419v1, §7](https://arxiv.org/abs/math/0605419v1). The proof keeps track of the factors as subsets of the given space. This matters when two decompositions contain isometric factors: an abstract isometry between those factors alone does not identify their fibres.

A nonempty metric space is **irreducible** if every metric product decomposition of it has a one-point factor. All products in this section have the squared-sum metric of L. The integer \(a(X)\) is defined by the finite-dimensional convex realizations in (Q.13). Its finiteness is sufficient for the argument; finite affine rank implies that finiteness by Q.4.

**Lemma S.1 (the finite-span form of the rank tools).** If \(a(X)<\infty\), every normed convex realization of an affine subset of \(X\) has span of differences of dimension at most \(a(X)\), even if its ambient normed space was initially infinite-dimensional. For nonempty metric spaces \(Y,Z\) with finite \(a(Y),a(Z)\),
\[
a(Y\times Z)=a(Y)+a(Z).
\tag{S.1}
\]
Conversely, finite \(a(Y\times Z)\) implies finite \(a(Y),a(Z)\). A nonpoint geodesic space has \(a\ge1\). The conclusions of R.2–R.4 remain valid if their finite-affine-rank hypothesis is replaced by \(a(X)<\infty\).

**Proof.** Suppose a convex realization \(C\) has span of differences of dimension at least \(n\). The generator argument (Q.15) chooses \(c_0,\ldots,c_n\in C\) affinely independent. Their convex hull is a finite-dimensional normed realization embedding into \(X\), and its span has dimension \(n\). Thus \(n\le a(X)\) directly from the definition. An infinite-dimensional span would permit every finite \(n\), which is impossible when \(a(X)\) is finite. All spans therefore have the asserted bound. The nonempty set of finite integers defining \(a(X)\) then has a maximum, so that maximum is attained.

The based fibres of \(Y\times Z\) embed each factor isometrically; this proves \(a(Y),a(Z)\le a(Y\times Z)\) whenever the latter is finite. In the other direction, choose convex realizations attaining \(a(Y),a(Z)\). Their product, with the norm (N.19), is a convex realization in \(Y\times Z\). Its span of differences is the direct sum of the two spans, by the fixed-coordinate differences used in Q.5. This proves the lower bound in (S.1).

For the upper bound let \(C\) be any convex normed realization in \(Y\times Z\), translate it so that \(0\in C\), and write \(V=\operatorname{span}C\). Do not yet assume that \(V\) is finite-dimensional. By L.1 the coordinate projections preserve selected segments as constant-speed geodesics. Corollary M.3 gives normed convex models for their images and makes the maps \(p,q\) preserve convex combinations. Translate both image models so that \(p(0)=q(0)=0\). The first paragraph puts their spans \(V_Y,V_Z\) in dimensions at most \(a(Y),a(Z)\).

The linear-relation argument (P.4) extends \(p,q\) to linear maps \(P:V\to V_Y\), \(Q:V\to V_Z\). That argument does not require finite dimension: a linear relation is a finite sum, whose positive and negative coefficients are normalized to two convex combinations, with the remaining weight at zero.

Every \(v\in V\) can also be written
\[
v=t(c-d),\qquad t>0,\quad c,d\in C.
\tag{S.2}
\]
Indeed write \(v=\sum_j b_jc_j\), choose \(t>0\) at least as large as each of \(\sum_{b_j>0}b_j\) and \(\sum_{b_j<0}|b_j|\), and form the positive and negative convex combinations divided by \(t\), padding both with zero. For \(v=0\) one can use \(c=d=0\). The product distance on \(C\), linearity and (S.2) give
\[
\|v\|^2=\|Pv\|_Y^2+\|Qv\|_Z^2.
\tag{S.3}
\]
Consequently \((P,Q)\) is injective into the finite-dimensional space \(V_Y\oplus V_Z\). More than \(\dim V_Y+\dim V_Z\) linearly independent vectors in \(V\) would have linearly dependent images, contradicting injectivity. Thus \(V\) is finite-dimensional and its dimension is at most \(a(Y)+a(Z)\). Taking the supremum proves the upper bound. The geodesic assertion follows from a nonconstant segment, an isometric normed interval of one-dimensional span, as in Q.5.

Finally we check precisely the use of the rank hypothesis in R. Theorem R.2 extends a geodesic to a maximal compatible affine subset by N.2. The first paragraph here supplies the finite-dimensional span for which R.2 previously invoked Q.4. Rectangularity N.3, linear extension P.1, simultaneous orthogonality O.1 and convex refinement P.3 then prove its projection is onto; R.1 supplies the factorization. None of those arguments uses covering dimension.

In R.3 the same first paragraph supplies the finite span of each maximal affine subset. The zero-intersection hypothesis and P.3 make it a whole vector space; P.4 makes its norm Euclidean; P.2 gives the stated projection isomorphisms. These steps again require only that finite span. R.4 then uses N.2–N.3, these conclusions of R.3, and its proved uniqueness of Euclidean segments. Its maximality comparison and conclusion \(X=\mathbb R^{2m}\) therefore remain valid. This proves all the stated extensions, without adding a completeness hypothesis. □

**Lemma S.2 (intrinsic complements and Euclidean factors).** For a product \(X=F\times H\) and \(x=(f_0,h_0)\), its based complementary fibre is determined by the based fibre \(F_x\) alone:
\[
H_x=\{z\in X:d(z,F_x)=d(z,x)\}.
\tag{S.4}
\]
Every metric factor of a finite-dimensional Euclidean space, based at its origin, is a whole linear subspace, and the factors are orthogonal. In particular, a nonpoint irreducible Euclidean space is a line. If the based fibres of two decompositions of a geodesic space agree at one point, the corresponding fibres agree at every point.

**Proof.** If \(z=(f,h)\), then for \(u\in F\)
\[
d(z,(u,h_0))^2=d_F(f,u)^2+d_H(h,h_0)^2.
\]
The minimum over \(u\) is attained uniquely at \(u=f\); its value is \(d_H(h,h_0)^2\). On the other hand,
\[
d(z,x)^2=d_F(f,f_0)^2+d_H(h,h_0)^2.
\]
The two distances are equal exactly when \(f=f_0\). This proves (S.4), including point factors. It also proves that the based projection onto \(F_x\) is the unique closest point in that fibre.

For a product of the entire Euclidean vector space \(E\), apply P.1 to \(C=E\) with \(0\) as basepoint. Its based projections extend linearly, but their domain was already the whole \(E\). Their images are therefore precisely the based factors \(U=PE\), \(W=(I-P)E\), which are entire subspaces. The squared-norm identity (P.2) and the original Euclidean inner product give
\[
|u+w|^2=|u|^2+|w|^2
 \quad\Longrightarrow\quad \langle u,w\rangle=0
\]
for \(u\in U,w\in W\). Thus the factors are orthogonal Euclidean subspaces. Repeating this argument handles any finite product. A Euclidean space of dimension at least two splits into the line through a nonzero vector and its nonzero orthogonal complement, using the orthonormal-basis construction of A.1. In dimension one, the two complementary subspaces must have dimensions zero and one; hence a line is irreducible.

The dimension of a Euclidean space is intrinsic to its metric. To verify this without a dimension theorem, an isometry \(f:\mathbb R^k\to\mathbb R^l\), after subtracting \(f(0)\), preserves inner products by
\[
2\langle u,v\rangle=|u|^2+|v|^2-|u-v|^2.
\]
The images of the \(k\) standard unit vectors are orthonormal, giving \(k\le l\). Apply the same argument to the inverse isometry to obtain \(l\le k\). This includes the point case.

For the last assertion, group each selected factor against the product of the others. Equality of the two based fibres at \(x\) gives both inclusions there. Corollary N.4 propagates each inclusion to every point of the geodesic space, proving equality there. The factor pairing used at \(x\) is unchanged in this argument. □

**Theorem S.3 (Foertsch–Lytchak decomposition).** Every nonempty geodesic metric space \(X\) of finite affine rank has a product decomposition
\[
X=E\times X_1\times\cdots\times X_s,\qquad E\cong\mathbb R^k,
\tag{S.5}
\]
where each \(X_i\) is nonpoint, irreducible and not isometric to the real line. The Euclidean factor may be a point, and \(s\) may be zero. Given any two such decompositions, one permutation matches their non-Euclidean factor fibres at every point of \(X\); their Euclidean fibres also agree. In particular \(s\), \(k\), and the isometry classes of the non-Euclidean factors with multiplicity are uniquely determined.

The same conclusions hold under the weaker hypothesis \(a(X)<\infty\). There is no completeness, local compactness, simple-connectivity, curvature or smoothness assumption.

**Proof.** We prove the assertion under \(a(X)=N<\infty\). This implies the stated finite-affine-rank case by Q.4. By S.1 every factor has finite \(a\), this integer is additive under products, and every nonpoint geodesic factor contributes at least one. Consequently a product decomposition of \(X\) has at most \(N\) nonpoint factors.

If \(X\) is a point, take \(k=s=0\). Otherwise there is at least the one-factor decomposition \(X=X\). Among the possible numbers of nonpoint factors choose the largest and a decomposition attaining it. Each factor is geodesic by L.1 and irreducible: splitting a reducible factor into two nonpoint factors would increase that number. Collect all factors isometric to \(\mathbb R\) into one Euclidean factor, using the squared-sum metric, and leave the other factors separate. This gives (S.5). It also supplies such a decomposition for every geodesic space with finite \(a\).

We prove uniqueness by induction on \(N\). When \(N=0\), the positive-rank assertion of S.1 makes \(X\) a point. More generally, two cases have immediate uniqueness for any \(N\). If \(X\) is Euclidean, S.2 makes every factor Euclidean. An irreducible nonpoint such factor is a line, so no non-Euclidean \(X_i\) can occur in (S.5); its Euclidean fibre is all of \(X\), and its dimension is fixed by S.2. If \(X\) is irreducible and not Euclidean, the only nonpoint factor in either decomposition is \(X\) itself, and the Euclidean factor is a point.

For the induction step, assume uniqueness for all smaller values of \(a\), and consider two normalized decompositions
\[
X=Y_0\times Y_1\times\cdots\times Y_n
 =Z_0\times Z_1\times\cdots\times Z_t.
\tag{S.6}
\]
Here \(Y_0,Z_0\) are Euclidean and the other factors satisfy the nonpoint irreducibility and non-line requirements. We may assume \(X\) is neither Euclidean nor irreducible. In particular \(n,t\ge1\). Fix \(x\in X\), and regard all fibres below as actual subsets through this same point.

Suppose first that \((Y_i)_x=(Z_j)_x=F_x\) for some \(i,j\ge1\). Relabel these as \(i=j=1\). Formula (S.4) makes their complementary fibres the same subset \(H_x\) of \(X\). It has two decompositions
\[
H_x\cong Y_0\times Y_2\times\cdots\times Y_n
 \cong Z_0\times Z_2\times\cdots\times Z_t,
\tag{S.7}
\]
with exactly the original remaining based fibres, now regarded inside \(H_x\). Because \(X\cong F_x\times H_x\) and \(a(F_x)\ge1\), S.1 gives \(a(H_x)<N\). Apply the induction hypothesis to the two decompositions of this geodesic factor. It gives \(n=t\) and one matching of all remaining based non-Euclidean fibres, together with equality of the Euclidean fibres at \(x\). Include the already matched factor \(F_x\). The last assertion of S.2 propagates every equality to every point of \(X\), with this single matching of indices. This proves uniqueness in the shared-factor case.

Next suppose that
\[
G_x=(Y_0)_x\cap(Z_0)_x
\tag{S.8}
\]
is nonpoint. The intersection theorem R.2, in its S.1 form, makes \(G_x\) a factor of both Euclidean fibres and hence a factor of \(X\). By S.2 it is a Euclidean subspace in each of them. Split
\[
(Y_0)_x=G_x\times \widetilde Y_0,\qquad
(Z_0)_x=G_x\times \widetilde Z_0
\]
as the orthogonal Euclidean products supplied by S.2. Both nested decompositions of \(X\) have the same based factor \(G_x\); therefore (S.4) identifies their complements with one subset \(H_x\). The two products on that subset are
\[
H_x\cong \widetilde Y_0\times Y_1\times\cdots\times Y_n
 \cong \widetilde Z_0\times Z_1\times\cdots\times Z_t.
\tag{S.9}
\]
Since \(G_x\) is nonpoint, \(a(H_x)<N\). Induction identifies the non-Euclidean based fibres and the Euclidean based fibres \(\widetilde Y_0,\widetilde Z_0\) in \(H_x\).

Recombining the latter common fibre with \(G_x\) gives equality of \((Y_0)_x,(Z_0)_x\). This recombination is independent of the two descriptions: the closest-point projections onto the common axes \(G_x,H_x\) are unique by S.2, so their pair determines the same coordinates and the same point of \(X\) in either product. The non-Euclidean fibres were already identified by induction. Propagate these equalities by S.2 as before. Thus uniqueness also holds in case (S.8) is nonpoint.

It remains to exclude the case where there is no shared non-Euclidean based fibre and (S.8) is a point. We first obtain
\[
(Y_i)_x\cap(Z_j)_x=\{x\}
 \quad(0\le i\le n,\ 0\le j\le t).
\tag{S.10}
\]
For \(i,j\ge1\), R.2 makes the intersection a factor of both irreducible fibres. If nonpoint, it is the whole of each, giving the shared factor already excluded. For \(i=0,j\ge1\), a nonpoint intersection would be all of \((Z_j)_x\) by irreducibility and a Euclidean factor of \((Y_0)_x\) by S.2. It would then be an irreducible nonpoint Euclidean space, hence a line, contradicting the requirement on \(Z_j\). The case \(i\ge1,j=0\) is identical with \(Y,Z\) interchanged. The remaining case \(i=j=0\) is our current assumption. This proves (S.10).

Group the products as
\[
Y=Y_n,\quad \bar Y=Y_0\times\cdots\times Y_{n-1},
\qquad
Z=Z_t,\quad \bar Z=Z_0\times\cdots\times Z_{t-1}.
\tag{S.11}
\]
Both \(Y,Z\) are nonpoint and non-Euclidean. Both complements are nonpoint: otherwise \(X\) would equal the corresponding irreducible factor, a case already settled. All four factors have \(a<N\), by additivity and positivity.

We show that any nonpoint factor \(G_x\) of one of these lower-rank factors can be located in its displayed normalized decomposition whenever \(G_x\) is irreducible. Take the complement of \(G_x\), decompose it by the existence assertion, and combine its Euclidean factor with \(G_x\) if \(G_x\) is a line. This gives a normalized decomposition of that lower-rank factor. Apply inductive uniqueness between it and the displayed normalized decomposition. If \(G_x\) is not a line, it must equal one of the displayed non-Euclidean based fibres. If \(G_x\) is a line, it must lie in the displayed Euclidean based fibre, since it was included in the combined Euclidean factor. The assertion concerns the actual subsets through \(x\), because induction asserts equality of those fibres. It applies to \(Y,Z\) as well, whose displayed Euclidean factors are points and whose displayed non-Euclidean decompositions each have just one factor.

Now consider any of
\[
Y_x\cap\bar Z_x,\qquad
\bar Y_x\cap Z_x,\qquad
\bar Y_x\cap\bar Z_x.
\tag{S.12}
\]
If one is nonpoint, R.2 makes it a factor of each of the two intersecting spaces. It is geodesic by L.1, has finite \(a\) as a factor of \(X\), and has a decomposition into nonpoint irreducibles by the existence proof. Choose one irreducible factor and call its based fibre \(G_x\). Composing its factorization with the complementary factorizations makes this same actual \(G_x\) a factor of both spaces in that intersection.

Apply the preceding lower-rank observation on both sides. If \(G_x\) is not a line, it equals \((Y_i)_x=(Z_j)_x\) for some \(i,j\ge1\), contradicting (S.10). If it is a line, it lies in both \((Y_0)_x\) and \((Z_0)_x\), again contradicting (S.10). When one side is \(Y\) or \(Z\), the displayed Euclidean factor there is a point, so even that one containment already rules out a line. Therefore each intersection in (S.12) is \(\{x\}\). The fourth intersection \(Y_x\cap Z_x\) is already a point by (S.10).

The two products \(X=Y\times\bar Y=Z\times\bar Z\) thus satisfy the four zero-intersection hypotheses of R.4, in the finite-\(a\) version established by S.1. That theorem makes \(X\) Euclidean, contrary to our standing assumption. The remaining case is impossible.

Induction proves the claimed equality of fibres after one permutation. The corresponding fibres are isometric to their abstract factors, so the non-Euclidean isometry classes with multiplicity coincide. The Euclidean fibres are equal as metric spaces; S.2 gives equality of their dimensions. All uses of induction were on a factor with strictly smaller \(a\), and none of the arguments added a completeness or regularity assumption. □

**Corollary S.4 (the isometry exact sequence).** For (S.5), let \(\mathcal P\) be the group of permutations of \(\{1,\ldots,s\}\) that exchange only isometric factors. There is an exact sequence of groups
\[
\begin{aligned}
1&\longrightarrow
\operatorname{Iso}(\mathbb R^k)\times
\prod_{i=1}^{s}\operatorname{Iso}(X_i)\\
&\longrightarrow \operatorname{Iso}(X)
\overset{\pi}{\longrightarrow}\mathcal P
\longrightarrow1 .
\end{aligned}
\tag{S.13}
\]
The first homomorphism acts separately on the coordinates. Here \(\operatorname{Iso}\) means surjective distance-preserving maps, with composition as group law.

**Proof.** Apply S.3 to the given decomposition and its image under \(g\in\operatorname{Iso}(X)\). There is a permutation \(\pi(g)\), independent of the basepoint, such that \(g\) carries each \(X_i\)-fibre onto the \(X_{\pi(g)(i)}\)-fibre through the image point, and carries Euclidean fibres onto Euclidean fibres. The restriction to a fibre is a surjective isometry, so the permutation belongs to \(\mathcal P\).

It is unique. Two different nonpoint factor fibres at one point intersect only in that point by the product coordinates, so they cannot be equal; hence the image of a nonpoint \(X_i\)-fibre identifies its target index uniquely. Composition of two isometries composes these uniquely specified permutations, proving that \(\pi\) is a homomorphism.

The coordinate action in (S.13) is a homomorphism and preserves the squared-sum distance. It is bijective on \(X\) because each coordinate action is bijective, and it is injective as a map of groups: if it fixes all tuples, hold every coordinate but one fixed to see that the corresponding factor map is the identity. Its image is contained in \(\ker\pi\).

Conversely take \(g\in\ker\pi\). Write its output coordinates as \(g_0,\ldots,g_s\), initially functions of the entire input tuple. Changing only input coordinate \(j\) moves inside a \(j\)-fibre, and its image stays in a \(j\)-fibre. Thus it leaves every output coordinate \(i\ne j\) unchanged. Change the finitely many input coordinates other than \(i\), one at a time. It follows that output coordinate \(i\) depends only on input coordinate \(i\); call the resulting map \(h_i\). Therefore
\[
g(e,x_1,\ldots,x_s)
   =(h_0(e),h_1(x_1),\ldots,h_s(x_s)).
\]
Tuples differing only in coordinate \(i\) show that \(h_i\) preserves distances. Surjectivity of \(g\) implies surjectivity of each \(h_i\): choose any target coordinate value and complete it to a target tuple. Hence each \(h_i\) is a factor isometry, and \(g\) lies in the image of the first map. This proves exactness at \(\operatorname{Iso}(X)\).

For \(\sigma\in\mathcal P\), choose a surjective isometry \(f_i:X_i\to X_{\sigma(i)}\) for each \(i\). Define a map fixing the Euclidean coordinate and sending input coordinate \(x_i\) to output coordinate \(f_i(x_i)\) in position \(\sigma(i)\). Reindexing the squared-distance sum shows this is an isometry, and the inverses \(f_i^{-1}\) give its inverse. Its factor permutation is \(\sigma\), proving surjectivity of \(\pi\). When \(s=0\), \(\mathcal P\) is the one-element group and the argument reduces to \(\operatorname{Iso}(X)=\operatorname{Iso}(\mathbb R^k)\); point Euclidean factors cause no change. □

## T. Examples and boundary cases

**Exercise T.1 (an incomplete product).** Let \(T\) be the tree formed from three unit intervals by identifying their zero endpoints, with the path metric. Determine the decomposition of
\[
X=(0,1)\times T
\]
and its Euclidean factor.

**Solution.** Denote the common endpoint by \(o\), and a point at distance \(t>0\) on arm \(i\in\{1,2,3\}\) by \((i,t)\). The distance is
\[
d_T((i,s),(j,t))=
\begin{cases}|s-t|,&i=j,\\s+t,&i\ne j,\end{cases}
\qquad d_T(o,(i,t))=t.
\tag{T.1}
\]
Along one arm use the interval segment; between two arms move to \(o\) and then out along the other arm, with arclength parameter. These curves realize (T.1), so \(T\) is geodesic. Formula (T.1) is the path metric: a path changing arms must meet \(o\), since away from \(o\) the three arms are disjoint open components, and a continuous path cannot leave one without reaching its boundary \(o\). The sum of the distances traversed on the two arms is at least \(s+t\). On a single arm, variation of the distance coordinate gives a lower bound \(|s-t|\). These bounds and the exhibited curves prove the assertion.

These geodesics are unique. More explicitly, for \(p,q\) on the same arm, the points satisfying
\[
d_T(p,r)+d_T(r,q)=d_T(p,q)
\]
are exactly the closed interval between them on that arm: the absolute-value formula gives that interval, while a point at positive distance \(v\) on another arm adds \(2v\) to the sum through \(o\). For \(p,q\) on different arms, the equality set is exactly the two intervals from them to \(o\). On the arm of \(p=(i,s)\), the formula permits \(0\le v\le s\), on the arm of \(q=(j,t)\) it permits \(0\le v\le t\), and on the third arm a positive \(v\) again adds \(2v\). In either equality set there is exactly one point at each distance between zero and \(d_T(p,q)\) from \(p\). Every minimizing constant-speed segment has to occupy that point at the corresponding time, proving uniqueness.

We verify a finite-rank hypothesis directly. Every convex normed realization embedding into \(T\) has span of differences at most one. Otherwise it contains three affinely independent points \(a,b,c\), by the generator argument in Q.4. Their straight segments map to the unique tree geodesics just described.

If their three images lie on one tree arc, one image lies on the geodesic between the other two. The corresponding point must lie on the straight segment between the other two preimages, by uniqueness and injectivity, contradicting affine independence. The only other possibility is that the three images are at positive distances on the three different arms. The geodesics from the first image to the other two then share a nontrivial interval from that image to \(o\). Their preimages would give an intersection of \([a,b]\) and \([a,c]\) containing a point other than \(a\). But an equality \(a+u(b-a)=a+v(c-a)\) with \(u,v>0\) contradicts independence of \(b-a,c-a\). This too is impossible. Thus every such span has dimension at most one. A whole arm is a nonconstant normed interval, so \(a(T)=1\).

The same argument on the real interval \(I=(0,1)\) is simpler: three distinct images can be ordered, and the middle image lies on the unique segment between the other two. Three affinely independent preimages are impossible. Since \(I\) itself is a nonconstant convex normed interval, \(a(I)=1\). Lemma S.1 now gives \(a(X)=2\), so the finite-\(a\) form of S.3 applies.

Both \(I\) and \(T\) are irreducible. If either were a product of two nonpoint spaces, both factors would be geodesic by L.1 and have \(a\ge1\); S.1 would make its rank at least two, a contradiction. Both are bounded and hence are not isometric to \(\mathbb R\). Therefore the displayed product already has the normalized factors
\[
X_1=(0,1),\qquad X_2=T,\qquad E=\mathbb R^0.
\]
The uniqueness conclusion of S.3 determines them as fibres up to permutation. Boundedness also independently rules out any nonpoint Euclidean factor: such a factor would contain an unbounded line, whereas \(d_X\le\sqrt{1+2^2}\).

Finally \(X\) is incomplete. The sequence \((1/n,o)\), \(n\ge2\), is Cauchy by the product metric. If it converged in \(X\), its first coordinate would converge to a point of \((0,1)\), since projection is distance nonincreasing. But the real first coordinates converge to zero, and a real sequence cannot have two distinct limits by the triangle inequality. There is no such point in \((0,1)\). This example uses neither completeness nor a covering-dimension upper bound in its application of S.3. □

**Exercise T.2 (rotated fibres).** Compare the coordinate-axis and diagonal products of \(\mathbb R^2\). Write their projection matrices and verify the four zero intersections.

**Solution.** In standard coordinates the projection onto the first coordinate axis and its complement are
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad I-P=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\tag{T.2}
\]
The diagonal lines have unit direction vectors
\(u=(1,1)/\sqrt2\), \(v=(1,-1)/\sqrt2\), with inner product zero. Projection onto \(\mathbb Ru\) and onto \(\mathbb Rv\) gives
\[
Q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad I-Q=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\tag{T.3}
\]
These follow from \(Qz=\langle z,u\rangle u\) and its \(v\)-analogue. Direct multiplication gives \(Q^2=Q\) and \(Q(I-Q)=0\), and both matrices are symmetric. Thus both pairs are complementary orthogonal projections, and Pythagoras gives the squared-sum product metric.

A vector \((a,0)\) on the first axis lies on either diagonal only if its second coordinate equals \(a\) or \(-a\); hence \(a=0\). A vector \((0,b)\) on the second axis lies on either diagonal only if its first coordinate equals \(b\) or \(-b\); hence \(b=0\). These are exactly the four zero intersections at the origin. Translation proves the corresponding statement for the four based fibres at every point.

For completeness, \(a(\mathbb R^2)=2\). The whole plane gives the lower bound. For any convex normed realization \(C\) embedding in the plane, its straight segments must map to the unique Euclidean segments, whose uniqueness was proved in R.4. After translation at one point, the embedding preserves convex combinations and extends linearly by (P.4). Formula (S.2) and preservation of distances on \(C\) make that linear extension an isometric injection of its span into \(\mathbb R^2\). Its span therefore has dimension at most two, giving the upper bound. This verifies the hypothesis of the finite-\(a\) transverse rigidity theorem in S.1.

The two decompositions are different decompositions into lines, as the four intersections show. They do not give different normalized decompositions in S.3: that theorem groups all Euclidean directions into a single Euclidean factor. In this example that factor is the whole plane, and there are no non-Euclidean factors. □

**Exercise T.3 (a nonclosed convex boundary).** Consider
\[
C=\{(u,v):0\le v<1\}
 \ \cup\ \{(u,1):u\ge0\}\subset\mathbb R^2.
\tag{T.4}
\]
Prove that \(C\) is convex and contains the whole horizontal line through the origin, but does not split as that line times its vertical projection.

**Solution.** Take \(p,q\in C\) and \(0<t<1\). Their convex combination has second coordinate in \([0,1]\). If that coordinate is less than one, it satisfies the first condition in (T.4), regardless of its first coordinate. If it equals one, both endpoint second coordinates must equal one: a strict convex combination of two numbers at most one equals one only when both equal one. The endpoint first coordinates are then nonnegative, so their combination is nonnegative. The combination lies in the second part of (T.4). For \(t=0,1\) it is an endpoint. Thus \(C\) is convex.

The entire horizontal line \(L=\mathbb R\times\{0\}\) lies in the first part. The vertical projection of \(C\) is \([0,1]\): every \((0,v)\), \(0\le v\le1\), belongs to \(C\), and no other vertical value occurs. Yet \((-1,1)\) is in \(L\times[0,1]\) in these coordinates and is absent from \(C\). Thus the two coordinates cannot be chosen independently.

There is also no metric-product decomposition having this actual line \(L\) as the based factor at \(0\). For \(z=(u,v)\in C\), the unique closest point on \(L\) is \((u,0)\), with distance \(v\). Formula (S.4) would force the complementary based factor to be
\[
H=\{z\in C:d(z,L)=d(z,0)\}
 =\{(0,v):0\le v\le1\}.
\]
The unique closest point of \((u,v)\in C\) on \(H\) is \((0,v)\), since this point belongs to \(H\) and minimizes \(u^2+(v-w)^2\) over \(0\le w\le1\). In a product these two closest-point projections are the two coordinates, by S.2. Surjectivity of the product would supply a point whose projections are \((-1,0)\in L\) and \((0,1)\in H\). The two explicit projection formulas force that point to be \((-1,1)\), which is not in \(C\). This contradiction proves the stronger assertion.

The missing boundary cannot be filled merely because \(C\) contains a line: \((-1,1-1/n)\in C\) for \(n\ge2\) tends to the missing point \((-1,1)\). This also verifies that \(C\) is not closed. The example explains why the convex refinement theorem P.3 needed its full rectangularity hypotheses, in addition to convexity. □

**Exercise T.4 (a full lattice and affine holonomy).** Let \(A:\mathbb R^n\to\mathbb R^n\) be an invertible real linear map, \(n\ge1\), and let \(\Lambda=A\mathbb Z^n\). Construct the flat torus \(M=\mathbb R^n/\Lambda\). Determine its linear and affine holonomy, parallel symmetric forms, and Euclidean product factor.

**Solution.** The boundedness of \(A^{-1}\), proved for finite-dimensional linear maps in Local tools 0.2, gives a constant \(c>0\) with
\[
|Ak|\ge c|k|\qquad(k\in\mathbb R^n).
\tag{T.5}
\]
For example choose a positive upper bound \(C\) for the operator norm of \(A^{-1}\) and take \(c=1/C\). Nonzero lattice vectors therefore have length at least \(c\), and any bounded set meets only finitely many lattice vectors: its preimages are integer vectors in a bounded coordinate box.

On the set of translation classes define
\[
d([u],[v])=\min_{\lambda\in\Lambda}|u-v-\lambda|.
\tag{T.6}
\]
The minimum exists. The candidate \(\lambda=0\) has length \(|u-v|\); any candidate no larger than \(|u-v|+1\) must satisfy \(|\lambda|\le2|u-v|+1\), leaving only finitely many possibilities. Translation of either representative reindexes the candidates, so the formula is well-defined. Its zero value means exactly that the representatives differ by a lattice vector. Symmetry follows by negating \(\lambda\). For the triangle inequality, add minimizing lattice vectors for the pairs \(u,v\) and \(v,w\) and apply the Euclidean triangle inequality to the resulting candidate for \(u,w\). Thus (T.6) is a metric.

Let \(q:\mathbb R^n\to M\) be the quotient map. For a Euclidean ball \(B(u,r)\), with \(0<r<c/4\), any two points in it have distance less than \(2r<c/2\). Subtracting a nonzero lattice vector gives distance at least \(c-2r>2r\). Therefore \(q\) is an isometry on that ball. Its translates by \(\Lambda\) are disjoint, and they are exactly the inverse image of \(q(B(u,r))\). That image is open for (T.6): if \([v]\) is sufficiently near the class of a point in \(B(u,r)\), a minimizing representative lies in the same ball. The same argument shows that \(q\) is open on every open subset of \(\mathbb R^n\).

These balls provide covering charts. Their transition maps are locally translations by lattice vectors: on an overlap the two inverse representatives differ by a lattice vector, which is locally constant because of (T.5). They therefore define a smooth manifold with a Euclidean metric in every chart, and \(q\) is a smooth local isometry and covering map. The metric (T.6) makes it Hausdorff. Images of a countable Euclidean basis give a countable basis, proving second countability. Projected straight paths connect any two classes.

The Riemannian distance agrees with (T.6). Choose a minimizing \(\lambda\) and project the straight segment from \(u\) to \(v+\lambda\), obtaining a curve of length \(|u-v-\lambda|\), after replacing \(\lambda\) by its negative if necessary. Conversely, lift any piecewise smooth curve starting at \(u\), using the proved covering path-lifting theorem Flat D.1. Its endpoint lies in \(v+\Lambda\), its length is unchanged by the local isometry, and its Euclidean length is at least the displacement between its endpoints, because the fundamental theorem and integral triangle inequality in Local tools 0.3 give |endpoint difference| at most the integral of the speed. Its length is at least (T.6). Taking the infimum gives equality.

Every translation class has a representative \(At\) with \(t\in[0,1]^n\): subtract the integer part of each coordinate of \(A^{-1}u\). The closed cube is compact by Local tools 0.1, so its continuous image under \(qA\) is all of \(M\) and is compact. The compactness-to-completeness result Hopf B.3 makes \(M\) complete. Equivalently, any sequence has a convergent subsequence by lifting to that cube and using Euclidean compactness, and a Cauchy sequence with a convergent subsequence converges by the triangle inequality.

The constant coordinate vectors of \(\mathbb R^n\) descend, because translations have identity derivative. They give a global parallel orthonormal frame: the Euclidean Levi-Civita coefficients vanish, by Riemannian A.1, and the covering charts have translation transitions. Parallel transport keeps the frame coordinates fixed, so both full and restricted linear holonomy are trivial.

Fix a frame over \([u_0]\). A loop lifts to a path from \(u_0\) to \(u_0+\lambda\) for a unique \(\lambda\in\Lambda\), by Flat D.1. In the parallel frame its development has displacement \(\lambda\), since integrating its coordinate velocity gives its endpoint difference by Local tools 0.3. The affine-transport formula in Linear F.1 is therefore the translation
\[
v\longmapsto v-\lambda.
\tag{T.7}
\]
Every \(\lambda\) occurs, by projecting the straight path from \(u_0\) to \(u_0+\lambda\). Thus full affine holonomy is exactly the discrete translation group \(-\Lambda\). A nullhomotopic loop has a closed lift by Flat D.1 and therefore \(\lambda=0\); restricted affine holonomy is trivial. Formula (T.7) uses the sign convention of the earlier programme affine-transport formula.

In the global parallel frame, a symmetric tensor \(h\) is parallel exactly when all its matrix entries are constant. Indeed covariant differentiation is ordinary differentiation of those entries in each covering chart. Zero derivatives make an entry constant along each piecewise smooth path, by the one-variable fundamental theorem of calculus, and \(M\) is connected. Conversely constant entries have zero covariant derivative. The parallel symmetric forms are therefore all constant symmetric real matrices, a vector space of dimension \(n(n+1)/2\): choose the \(n\) diagonal entries and the \(n(n-1)/2\) entries above the diagonal.

Despite trivial linear holonomy, the global Euclidean product factor of \(M\) is a point. The compact space \(M\) is bounded: the continuous distance to a fixed point is bounded on a compact metric space, and the triangle inequality then bounds all pairwise distances. A nonpoint Euclidean factor would contain an isometrically embedded whole line, which is unbounded. This is impossible. The deck-displacement description J.2 gives the same answer: \(\Lambda\) spans \(\mathbb R^n\), so its displacement span has zero orthogonal complement. □

**Exercise T.5 (a Euclidean ball with a missing boundary).** Let \(B=\{x\in\mathbb R^n:|x|<1\}\), \(n\ge1\), with its Euclidean metric. Determine its linear and affine holonomy and its completeness.

**Solution.** The ball is convex: for \(0<t<1\), the Euclidean triangle inequality gives
\[
|(1-t)x+ty|\le(1-t)|x|+t|y|<1
\]
for \(x,y\in B\), and the endpoints are already in \(B\). Straight segments thus realize Euclidean distance inside the ball. The fundamental theorem and integral triangle inequality in Local tools 0.3 show that no curve has length smaller than its endpoint distance, so its intrinsic Riemannian distance is exactly the ambient Euclidean distance.

The Levi-Civita coefficients are zero in the standard coordinates, by Riemannian A.1. The constant coordinate frame is parallel, its curvature is zero by the coordinate formula in Linear B.3, and full linear holonomy is trivial. For a loop, the development displacement is the integral of its coordinate velocity, which is its endpoint difference and hence zero by Local tools 0.3. Linear F.1 then makes full affine holonomy trivial as well. The corresponding restricted groups are subgroups of these trivial groups and hence are trivial.

Choose a unit vector \(e\). The curve \(\gamma(t)=te\), \(-1<t<1\), is a unit-speed geodesic, since it solves the zero-coefficient geodesic equation proved in Geodesics A.1. It has no continuous extension in \(B\) to \(t=1\): such an extension would have coordinate value \(e\), which is outside \(B\). The sequence \((1-1/j)e\), \(j\ge2\), is Cauchy but has the same missing limit, proving metric incompleteness directly. Since Euclidean space is complete by Local tools 0.1, \(B\) is not isometric to \(\mathbb R^n\); an isometry would transfer this Cauchy sequence and its Euclidean limit back to a limit in \(B\).

The field \(V(x)=-x\) satisfies \(\nabla V=-I\), by differentiating its coordinate functions. It has its zero at the origin. Its existence and the trivial affine holonomy therefore do not imply that \(B\) is an entire Euclidean space: the completeness assumption in G.2–G.3 is essential. Likewise the global Euclidean conclusion E.2 cannot be drawn from trivial holonomy after dropping completeness. □

**Exercise T.6 (two round spheres).** On \(S^2\times S^2\) take
\[
g=a\,g_{S^2}\oplus b\,g_{S^2},\qquad a,b>0.
\]
Determine full and restricted linear holonomy and all parallel symmetric bilinear forms. Explain what changes when \(a=b\).

**Solution.** As proved in I.1, multiplying a metric by a positive constant leaves its Levi-Civita connection unchanged, and Geodesics F.3 gives both holonomy groups of the round sphere as \(\mathrm{SO}(2)\). The product-holonomy theorem E.1 therefore gives both groups of this product as
\[
\{\operatorname{diag}(R_\alpha,R_\beta):
R_\alpha,R_\beta\in\mathrm{SO}(2)\}.
\tag{T.8}
\]
The rotations vary independently. Each tangent plane is irreducible over \(\mathbb R\): a nonzero proper subspace of a plane is a line, and rotation by a right angle does not preserve that line. There is no fixed tangent vector, because \(-I\) occurs independently on each tangent plane.

Raise an index of a parallel symmetric form using \(g\), obtaining a parallel self-adjoint endomorphism \(S\), as in H.1. Parallel transport makes \(S\) commute with (T.8), and the same independent \(-I\) argument in I.1 kills both off-diagonal blocks. A self-adjoint block on either plane commuting with all rotations is scalar: H.2 decomposes it into real orthogonal eigenspaces, each invariant under the rotations, so irreducibility permits just one eigenvalue. Its scalar is constant over the connected manifold because parallel transport preserves \(S\). Thus
\[
h=\lambda_1\,a\,g_{S^2}\oplus
  \lambda_2\,b\,g_{S^2},
\qquad \lambda_1,\lambda_2\in\mathbb R,
\tag{T.9}
\]
and conversely every displayed tensor is parallel by the product connection. This is a two-dimensional space.

When \(a=b\), the map \((p,q)\mapsto(q,p)\) is an isometry, as follows directly from the product metric. It exchanges the two factor distributions. It does not produce off-diagonal parallel endomorphisms: (T.8) still contains the two rotations independently, so the preceding vanishing argument is unchanged. In particular equality of the two scale constants does not collapse the two independent holonomy actions into one diagonal action. □

## U. Algebraic curvature and parallel curvature

Fix a nonzero finite-dimensional real inner-product space \(V\). An **algebraic curvature tensor** is an alternating bilinear map \(Q:V\times V\to\mathfrak{so}(V)\) whose four-tensor
\[
Q(x,y,z,t)=\langle Q_{x,y}z,t\rangle
\]
satisfies pair symmetry \(Q(x,y,z,t)=Q(z,t,x,y)\) and the first Bianchi identity
\[
Q_{x,y}z+Q_{y,z}x+Q_{z,x}y=0.
\tag{U.1}
\]
Write \(\mathcal R(V)\) for their real vector space. These conditions are linear, so this is a finite-dimensional subspace of the space of four-tensors. In this section \(Q\) denotes an algebraic tensor. In U.5 we specify its sign relative to the geometric curvature convention used earlier.

**Lemma U.1 (curvature operators, their action and sectional determination).** Give \(\mathfrak{so}(V)\) the inner product
\[
(A,B)_*=-\tfrac12\operatorname{tr}_V(AB)
\]
and identify the alternating square \(\Lambda^2V\) with \(\mathfrak{so}(V)\) by
\[
(x\wedge y)z=\langle y,z\rangle x-\langle x,z\rangle y.
\tag{U.2}
\]
Then \(\widehat Q(x\wedge y)=-Q_{x,y}\) defines a self-adjoint operator on \(\mathfrak{so}(V)\). The orthogonal group acts on curvature tensors by
\[
(g\cdot Q)_{x,y}=gQ_{g^{-1}x,g^{-1}y}g^{-1}.
\tag{U.3}
\]
The derivative of this action at \(B\in\mathfrak{so}(V)\) is
\[
\begin{aligned}
(B\cdot Q)_{x,y}
 &=[B,Q_{x,y}]-Q_{Bx,y}-Q_{x,By},\\
(B\cdot Q)(x,y,z,t)
 &=-Q(Bx,y,z,t)-Q(x,By,z,t)\\
 &\quad-Q(x,y,Bz,t)-Q(x,y,z,Bt).
\end{aligned}
\tag{U.4}
\]
For the tensor inner product obtained by summing components in an orthonormal basis this action is skew-adjoint. In particular
\[
\|B\cdot Q\|^2=-\langle B\cdot(B\cdot Q),Q\rangle.
\tag{U.5}
\]
Finally the values \(Q(x,y,x,y)\), for all \(x,y\), determine \(Q\).

**Proof.** Take an orthonormal basis \(e_1,\ldots,e_n\). One can define \(\Lambda^2V\) as the vector space with basis \(e_i\wedge e_j\), \(i<j\), and set
\[
x\wedge y=\sum_{i<j}(x_i y_j-x_j y_i)e_i\wedge e_j.
\]
The matrix in (U.2) is \(xy^T-yx^T\), so it is skew-adjoint. The matrices \(e_i\wedge e_j\) have the two respective entries \(1,-1\) in positions \(ij,ji\). They are a basis of all skew-adjoint matrices and are orthonormal for \((\, ,\,)_*\). This proves the asserted identification and positivity. Alternation of \(Q\) gives a unique linear extension defining \(\widehat Q\). Direct matrix multiplication, or the component sum, gives
\[
(A,x\wedge y)_*=-\langle Ax,y\rangle,\qquad
(\widehat Q(x\wedge y),z\wedge t)_*=Q(x,y,z,t).
\tag{U.6}
\]
Pair symmetry therefore makes \(\widehat Q\) self-adjoint, since the wedges span.

Orthogonal change of variables preserves alternation, pair symmetry and (U.1), so (U.3) preserves \(\mathcal R(V)\). Substitution twice verifies the group action law. Differentiating \(g=\exp(sB)\) and \(g^{-1}=\exp(-sB)\) proves the first equation of (U.4). Pairing its commutator term with \(t\), and using \(\langle Bu,t\rangle=-\langle u,Bt\rangle\), proves the second.

For clarity, the tensor inner product is
\(\langle Q,P\rangle=\sum_{i,j,k,l}Q(e_i,e_j,e_k,e_l)P(e_i,e_j,e_k,e_l)\).
If \(e_i'=\sum_a o_{ai}e_a\) is another orthonormal basis, expansion in each of the four slots reduces this sum to the original one: each index sum uses \(\sum_i o_{ai}o_{bi}=\delta_{ab}\). This proves independence of the basis and invariance under (U.3). Differentiate the inner-product identity along \(\exp(sB)\); it gives
\(\langle B\cdot Q,P\rangle+\langle Q,B\cdot P\rangle=0\).
Taking \(P=B\cdot Q\) proves (U.5). In operator language, conjugation on \(\mathfrak{so}(V)\) is the induced action on wedges, because \(g(x\wedge y)g^{-1}=gx\wedge gy\). Consequently (U.4) also says
\[
\widehat{B\cdot Q}=\operatorname{ad}_B\widehat Q-\widehat Q\operatorname{ad}_B,
\qquad \operatorname{ad}_B(A)=[B,A].
\tag{U.7}
\]
Trace cyclicity, proved directly in F.1, makes \(\operatorname{ad}_B\) skew-adjoint for \((\, ,\,)_*\).

For the final assertion, subtract two tensors having the same sectional values; it suffices to suppose all these values are zero. Substitution of \(y+z\) for \(y\), and pair symmetry, give \(Q(x,y,x,z)=0\). Substitution of \(x+u\) in the two repeated \(x\)-slots now gives
\[
Q(x,y,u,z)+Q(u,y,x,z)=0.
\]
Skewness of the first pair implies
\(Q(x,y,u,z)=Q(y,u,x,z)\).
Applying the same identity once more makes this also \(Q(u,x,y,z)\). Bianchi says that the sum of these three equal quantities is zero. Each vanishes, for all four vectors, proving \(Q=0\). □

Let \(G\subseteq\mathrm{SO}(V)\) be a connected compact Lie subgroup with Lie algebra \(\mathfrak g\). A **holonomy system** here means a triple \((V,R,G)\) with \(R\in\mathcal R(V)\) and every \(R_{x,y}\in\mathfrak g\). The terminology does not assume that the tensor arises from a manifold. Put
\[
\mathcal M_R=\operatorname{span}_{\mathbb R}\{g\cdot R:g\in G\},
\qquad
\mathfrak g^R=\operatorname{span}_{\mathbb R}
\{Q_{x,y}:Q\in\mathcal M_R,\ x,y\in V\}.
\tag{U.8}
\]
Both are ordinary finite-dimensional spans, with no closure operation.

**Lemma U.2 (the ideal generated by curvature).** The space \(\mathfrak g^R\) is an ideal of \(\mathfrak g\). Its orthogonal complement \(\mathfrak g_R\) inside \(\mathfrak g\) is also an ideal, and
\[
[\mathfrak g_R,\mathfrak g^R]=0,\qquad
B\cdot Q=0\quad(B\in\mathfrak g_R,\ Q\in\mathcal M_R).
\tag{U.9}
\]
If \(T\in\mathcal M_R\), then \(\mathcal M_T\subseteq\mathcal M_R\) and \(\mathfrak g^T\subseteq\mathfrak g^R\).

**Proof.** Conjugation by \(G\) preserves its own Lie algebra, by differentiating its conjugation maps. Hence every tensor in \(\mathcal M_R\) takes values in \(\mathfrak g\). The group action preserves \(\mathcal M_R\). Differentiation preserves it too, since a finite-dimensional subspace is closed, as proved in F.1. For \(B\in\mathfrak g\), (U.4) gives
\[
[B,Q_{x,y}]=(B\cdot Q)_{x,y}+Q_{Bx,y}+Q_{x,By}\in\mathfrak g^R.
\]
This proves the ideal assertion. If \(C\perp\mathfrak g^R\) inside \(\mathfrak g\), then
\(([B,C],A)_*=-(C,[B,A])_*=0\) for \(A\in\mathfrak g^R\).
Thus the complement is an ideal. A bracket of the two ideals belongs to their intersection, which is zero.

For \(B\) in the complement, \(\widehat Q\) has image in \(\mathfrak g^R\), which commutes with \(B\). Therefore \(\operatorname{ad}_B\widehat Q=0\). Taking adjoints and using U.1 gives \(\widehat Q\operatorname{ad}_B=0\). Equation (U.7) proves \(B\cdot Q=0\). Finally \(T\in\mathcal M_R\) and invariance of that space give \(\mathcal M_T\subseteq\mathcal M_R\); taking the spans of their values proves the other inclusion. □

**Lemma U.3 (ideals integrate to compact subgroups in an irreducible action).** Suppose \(G\) above acts irreducibly on \(V\). Every ideal \(\mathfrak h\) of \(\mathfrak g\) is the Lie algebra of a unique connected immersed subgroup of \(G\), and this subgroup is embedded, closed and compact. In particular the subgroup with Lie algebra \(\mathfrak g^R\) is compact.

**Proof.** First \(\mathfrak h\) is preserved by \(\operatorname{Ad}(G)\). For \(A\in\mathfrak g\), the curve \(\operatorname{Ad}(\exp(tA))X\) solves \(Y'=[A,Y]\). The right side preserves \(\mathfrak h\), so uniqueness of the finite-dimensional linear ODE, [Local tools, Proposition 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters), shows that \(X\in\mathfrak h\) implies \(Y(t)\in\mathfrak h\). Connected exponential generation, proved in F.1, extends this invariance from the exponentials to \(G\).

Let \(H\) be the subgroup generated by \(\exp(tX)\), \(X\in\mathfrak h\), \(t\in\mathbb R\). [Curvature, Theorem C.1](curvature-and-holonomy-groups.md#theorem-c-1) supplies its connected immersed Lie-group structure. Its Lie algebra is exactly \(\mathfrak h\), as can be checked from that theorem's word charts. Indeed the right-translated differential of a word
\(\exp(t_1X_1)\cdots\exp(t_kX_k)\)
is a sum of conjugates of the \(X_i\)'s, all in \(\mathfrak h\) by the preceding paragraph. All its differential ranks are at most \(\dim\mathfrak h\). Choosing a basis \(X_1,\ldots,X_d\) and differentiating this word at zero gives image exactly \(\mathfrak h\) and rank \(d\). The maximal-rank construction in C.1 thus has that tangent space. Every other connected immersed subgroup with this Lie algebra is generated by the same exponentials, again by F.1, so has the same image; its smooth structure will also be identified below. Adjoint invariance shows \(H\) is normal in \(G\).

Put \(K=\overline H\) inside \(G\). This is a compact normal subgroup. Its embedded Lie-group structure follows from [Invariant connections, Theorem A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). It is connected: a separation of \(K\) into two nonempty relatively open disjoint sets would meet the dense connected image of \(H\) on both sides, separating that image. Write \(\mathfrak k=\operatorname{Lie}(K)\). Normality gives that \(\mathfrak k\), like \(\mathfrak h\), is invariant under \(\operatorname{Ad}(G)\). Hence
\[
\mathfrak k=\mathfrak h\oplus\mathfrak m,\qquad
\mathfrak m=\mathfrak k\cap\mathfrak h^\perp
\tag{U.10}
\]
is an orthogonal decomposition into \(\mathfrak g\)-ideals. Here invariance of the trace inner product gives the assertion for \(\mathfrak m\), exactly as in U.2.

The ideals \(\mathfrak h,\mathfrak m\) commute. Thus each \(Z\in\mathfrak m\) commutes with every exponential generating \(H\), and then with \(K\) by continuity. Differentiation gives \([Z,\mathfrak k]=0\); in particular \(\mathfrak m\) is abelian. For \(A\in\mathfrak g\) and \(Z,W\in\mathfrak m\), trace invariance gives
\[
([A,Z],W)_*=(A,[Z,W])_*=0.
\]
But \([A,Z]\in\mathfrak m\), so positivity gives \([A,Z]=0\). We have proved that \(\mathfrak m\) is central even in \(\mathfrak g\).

Suppose \(0\ne Z\in\mathfrak m\). Its square is self-adjoint and commutes with \(G\). The self-adjoint commutant argument of F.1, using a maximum of the quadratic form and irreducibility, proves \(Z^2=-c^2I\) with \(c>0\). Thus \(J=Z/c\) is an orthogonal complex structure commuting with \(G\). The complex basis construction and trace identities (F.5) give, for every \(X\in\mathfrak h\),
\[
\operatorname{Re}\operatorname{tr}_{\mathbb C}X=0,\qquad
-2\operatorname{Im}\operatorname{tr}_{\mathbb C}X
 =\operatorname{tr}_{\mathbb R}(JX)=0.
\]
The first identity uses skew-adjointness; the second uses \(J\in\mathfrak m\perp\mathfrak h\). Consequently every such \(X\) has complex trace zero. The determinant calculation (F.7) proves that \(\det_{\mathbb C}\exp(tX)=1\). Multiplicativity gives this on \(H\) and continuity on \(K\). On the other hand \(J\in\mathfrak k\), so \(\exp(tJ)\in K\), and its determinant derivative at zero is \(\operatorname{tr}_{\mathbb C}J=i\dim_{\mathbb C}V\ne0\). This contradicts its being identically one. Therefore \(\mathfrak m=0\).

Now \(H\hookrightarrow K\) is smooth with an isomorphism on tangent spaces; smoothness in the embedded charts follows since all transverse coordinates of its ambient smooth inclusion vanish. The inverse-function theorem, [Local tools, Theorem 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), gives an open identity neighbourhood of \(K\) contained in \(H\). The subgroup \(H\) is open, and its other cosets make it closed in \(K\). Density implies \(H=K\). Translates of the local inverse show agreement of the immersed and embedded structures. For any other immersed structure with the same Lie algebra the same argument applies, proving uniqueness as a Lie subgroup. Compactness follows from \(K\subseteq G\) closed. The zero ideal gives \(H=\{I\}\) and is included. Applying this to U.2 proves the last assertion. □

Call a holonomy system **symmetric** when \(g\cdot Q=Q\) for every \(g\in G\). This is an algebraic definition; U.5 explains its geometric consequence under an additional hypothesis.

**Theorem U.4 (the curvature tensor of a symmetric irreducible system).** Suppose \((V,Q,G)\) is symmetric and \(G\) acts irreducibly. Define
\[
\begin{aligned}
B_{\mathfrak g}(A,C)
 &=\operatorname{tr}_{\mathfrak g}(\operatorname{ad}_A\operatorname{ad}_C)
       -2(A,C)_*,\\
(TA,C)_*&=B_{\mathfrak g}(A,C),\qquad
\pi_{\mathfrak g}:\mathfrak{so}(V)\longrightarrow\mathfrak g
\end{aligned}
\tag{U.11}
\]
where \(\pi_{\mathfrak g}\) is orthogonal projection. The operator \(T\) is self-adjoint, negative definite and invertible. There is a uniquely determined real number \(\lambda\) such that
\[
Q_{x,y}=-\lambda T^{-1}\pi_{\mathfrak g}(x\wedge y),\qquad
\operatorname{Ric}_Q=-\frac{\lambda}{2}\langle\, ,\,\rangle,
\quad
\operatorname{Ric}_Q(x,y)=\sum_jQ(e_j,x,e_j,y).
\tag{U.12}
\]
If \(Q\ne0\), then \(\lambda\ne0\), the \(Q_{x,y}\)'s span \(\mathfrak g\), and
\[
Q(x,y,z,t)=\lambda^{-1}B_{\mathfrak g}(Q_{x,y},Q_{z,t}),
\qquad
Q(x,y,x,y)=0\ \Longleftrightarrow\ Q_{x,y}=0.
\tag{U.13}
\]

**Proof.** Trace invariance makes \(\operatorname{ad}_A\) skew-adjoint on \(\mathfrak g\). In an orthonormal basis its squared trace is minus the sum of the squares of its matrix entries, as in F.1. Hence
\[
B_{\mathfrak g}(A,A)
=-\sum_{r,s}(\operatorname{ad}_A)_{rs}^{\,2}-2\|A\|_*^2<0
\]
for \(A\ne0\). Symmetry follows from trace cyclicity. The matrix of the bilinear form in an orthonormal basis defines the self-adjoint \(T\); negative definiteness makes its kernel zero. Rank and nullity then imply invertibility. These statements also have their usual empty-dimensional meaning when \(\mathfrak g=0\).

On the vector space \(\mathfrak j=\mathfrak g\oplus V\) define the alternating bilinear bracket by
\[
[A,C]_{\mathfrak j}=[A,C],\qquad
[A,x]_{\mathfrak j}=Ax,\qquad
[x,y]_{\mathfrak j}=Q_{x,y}.
\tag{U.14}
\]
Here the Jacobi identity has four types of inputs. Three elements of \(\mathfrak g\) give the matrix commutator identity, verified by cancellation of the six triple products. Two such elements and \(x\in V\) give \(ACx-CAx-[A,C]x=0\). For \(A,x,y\), the required identity is
\([A,Q_{x,y}]=Q_{Ax,y}+Q_{x,Ay}\), which is (U.4) and symmetry. For three vectors it is (U.1). Trilinearity thus proves Jacobi on all of \(\mathfrak j\).

Write \(B_{\mathfrak j}(a,b)=\operatorname{tr}_{\mathfrak j}(\operatorname{ad}_a\operatorname{ad}_b)\). We need no structural theorem about this bilinear form. Jacobi gives \(\operatorname{ad}_{[a,b]}=[\operatorname{ad}_a,\operatorname{ad}_b]\), and trace cyclicity gives directly
\[
B_{\mathfrak j}([a,b],c)=B_{\mathfrak j}(a,[b,c]).
\tag{U.15}
\]
For \(A\in\mathfrak g\), \(\operatorname{ad}_A\) is block diagonal on \(\mathfrak g\oplus V\), with blocks \(\operatorname{ad}_A|_{\mathfrak g}\) and \(A|_V\). For \(x\in V\), \(\operatorname{ad}_x\) is block off diagonal. Their product has zero trace, while two diagonal blocks give
\[
B_{\mathfrak j}|_{\mathfrak g\times\mathfrak g}=B_{\mathfrak g},
\qquad B_{\mathfrak j}(\mathfrak g,V)=0.
\tag{U.16}
\]
The action \(A+x\mapsto gAg^{-1}+gx\) preserves (U.14), by symmetry of \(Q\). It conjugates adjoint operators, so preserves \(B_{\mathfrak j}\). Its restriction to \(V\) is consequently a \(G\)-invariant symmetric bilinear form. Represent it by its self-adjoint operator using an orthonormal basis. Invariance says this operator commutes with \(G\), so the self-adjoint commutant argument of F.1 gives
\[
B_{\mathfrak j}(x,y)=\lambda\langle x,y\rangle
\tag{U.17}
\]
for a scalar \(\lambda\).

For \(Q\ne0\) this scalar cannot vanish. Otherwise (U.15)–(U.17) give
\[
B_{\mathfrak g}(Q_{x,y},Q_{x,y})
=B_{\mathfrak j}(x,[y,[x,y]])=0.
\]
Negative definiteness would give every \(Q_{x,y}=0\). Another application of invariance gives
\[
\lambda\langle Q_{x,y}z,t\rangle
=B_{\mathfrak j}([[x,y],z],t)
=B_{\mathfrak g}(Q_{x,y},Q_{z,t}).
\tag{U.18}
\]
This proves (U.13), including the equivalence, since a negative definite form has no nonzero vector of zero square.

We also need the full spanning assertion. If \(A\in\mathfrak g\) is \(B_{\mathfrak g}\)-orthogonal to all \(Q_{x,y}\), then for every \(y\)
\[
\lambda\|Ay\|^2
=B_{\mathfrak j}([A,y],[A,y])
=B_{\mathfrak j}(A,[y,[A,y]])
=B_{\mathfrak g}(A,Q_{y,Ay})=0.
\]
Since \(\lambda\ne0\), \(Ay=0\) for every \(y\), hence \(A=0\) as a matrix. The positive definite inner product \(-B_{\mathfrak g}\) admits orthogonal projection onto any subspace by a finite orthonormal basis. Thus a subspace with zero orthogonal complement is the whole space. The \(Q_{x,y}\)'s therefore span \(\mathfrak g\). By (U.6), (U.11) and (U.18),
\[
(Q_{x,y},TQ_{z,t})_*
 =-\lambda(Q_{x,y},\pi_{\mathfrak g}(z\wedge t))_*.
\]
Spanning and positivity imply \(TQ_{z,t}=-\lambda\pi_{\mathfrak g}(z\wedge t)\), proving the first formula of (U.12).

It remains to compute the scalar without an omitted trace identity. The two off-diagonal blocks of \(\operatorname{ad}_x\) are
\[
\alpha_x:\mathfrak g\to V,\quad A\mapsto-Ax,
\qquad
\beta_x:V\to\mathfrak g,\quad z\mapsto Q_{x,z}.
\]
For any maps \(\alpha:E\to F,\beta:F\to E\), expansion in bases gives
\(\operatorname{tr}_E(\beta\alpha)=\sum_{i,j}\beta_{ij}\alpha_{ji}
=\operatorname{tr}_F(\alpha\beta)\).
Therefore
\[
\begin{aligned}
\lambda\|x\|^2
 &=B_{\mathfrak j}(x,x)
 =2\operatorname{tr}_V(\alpha_x\beta_x)\\
 &=-2\sum_j\langle Q_{x,e_j}x,e_j\rangle
 =-2\sum_j Q(e_j,x,e_j,x).
\end{aligned}
\]
The last equality uses skewness in both pairs. The bilinear form \(\operatorname{Ric}_Q\) is symmetric by pair symmetry, so polarization proves its formula in (U.12). It uniquely determines \(\lambda\) because \(V\ne0\). If \(Q=0\), take \(\lambda=0\); both formulas of (U.12) hold and the same Ricci formula proves uniqueness. □

**Theorem U.5 (algebraic invariance forces parallel curvature).** Let \(M\) be a connected Riemannian manifold of dimension \(n\ge3\) whose restricted holonomy action is irreducible. At one point \(p\), suppose every algebraic curvature tensor with values in its restricted holonomy algebra \(\mathfrak h_p\) is invariant under the restricted holonomy group \(H_p^0\). Then \(\nabla R=0\) everywhere. No completeness assumption is required.

**Proof.** Keep the earlier convention
\(R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}\).
For the algebraic calculations put \(Q=-R\). [Geodesics, Theorem C.2 and Corollary C.3](geodesics-normal-coordinates-and-curvature.md#theorem-c-2) prove the first Bianchi identity, pair symmetry and skew-adjointness. Thus \(Q_q\in\mathcal R(T_qM)\) for every \(q\).

Restricted holonomy is compact and connected by F.2. [Curvature, Theorem G.3](curvature-and-holonomy-groups.md#theorem-g-3) proves that every transported curvature value lies in \(\mathfrak h_p\). Moreover parallel transport along any path from \(p\) to \(q\) conjugates restricted holonomy, by [Curvature, Theorem C.5](curvature-and-holonomy-groups.md#theorem-c-5). It preserves the metric, hence transports algebraic curvature tensors and their invariance condition. It follows that the stated hypothesis holds at every \(q\), that \(Q_q\) has values in \(\mathfrak h_q\), and that the action there is irreducible. These paths exist because a connected manifold is piecewise smoothly path connected, as proved in A.2. Theorem U.4 therefore gives
\[
\operatorname{Ric}_Q=f\,g,\qquad f=-\lambda/2.
\tag{U.19}
\]
This \(f\) is smooth: it is \(1/n\) times the metric trace of the smooth tensor \(\operatorname{Ric}_Q\).

We prove that \(f\) is constant, including the needed contraction of the second Bianchi identity. All following indices refer to an orthonormal basis at the point of evaluation; repeated indices are summed only when a sum is written. Write \(Q_{bcde}=Q(e_b,e_c,e_d,e_e)\) and \(\nabla_a Q\) for the covariant derivative in direction \(e_a\). Torsion vanishes, so Geodesics C.2 gives
\[
(\nabla_aQ)_{bcde}
+(\nabla_bQ)_{cade}
+(\nabla_cQ)_{abde}=0.
\]
Set \(d=a\) and sum over \(a\). Covariant differentiation commutes with metric contraction because \(\nabla g=0\), by the tensor product and contraction rules in [Linear connections, Theorem C.1](linear-and-affine-connections.md#theorem-c-1). The definitions and first-pair skewness give
\[
\sum_a(\nabla_aQ)_{bcae}
= (\nabla_b\operatorname{Ric}_Q)_{ce}
 -(\nabla_c\operatorname{Ric}_Q)_{be}.
\tag{U.20}
\]
Now set \(e=b\) and sum over \(b\). Pair symmetry and skewness give
\(\sum_b Q_{bcab}=\sum_b Q_{abbc}=-\operatorname{Ric}_{Q,ac}\).
Using also symmetry of Ricci, (U.20) becomes
\[
2\sum_a(\nabla_a\operatorname{Ric}_Q)_{ac}
 =\nabla_c(\operatorname{tr}_g\operatorname{Ric}_Q).
\tag{U.21}
\]
Substitute (U.19). Since \(\nabla g=0\), this says \(2\,df=n\,df\). As \(n\ge3\), \(df=0\). Along each smooth piece of a path the derivative of \(f\) is zero; the fundamental theorem of calculus, Local tools 0.3, and connectedness make \(f\), hence \(\lambda\), constant on \(M\).

Finally let \(\tau:T_pM\to T_qM\) be parallel transport along any such path. Conjugation \(A\mapsto\tau A\tau^{-1}\) is an isometric Lie-algebra isomorphism from \(\mathfrak h_p\) to \(\mathfrak h_q\). It preserves both traces in (U.11), since it conjugates the corresponding linear operators. It therefore intertwines \(T_p,T_q\), their inverses and the orthogonal projections onto the two algebras. It also carries \(x\wedge y\) to \(\tau x\wedge\tau y\), directly from (U.2). The first formula of (U.12), with the now constant scalar, proves
\[
Q_q(\tau x,\tau y)\tau z=\tau\bigl(Q_p(x,y)z\bigr).
\]
Thus \(Q\) is invariant under transport along every path. Its components in a parallel frame along any curve are constant; the tensor derivative formula in Linear C.1 then gives \(\nabla Q=0\). Since \(R=-Q\), the conclusion follows. □

## V. Flats and curvature centralizers

Let \((V,R,G)\) be a holonomy system in the sense of U.8, with \(\dim V\ge2\), and suppose \(G\) acts irreducibly. Write
\(\mathcal M=\mathcal M_R\), \(\mathfrak h=\mathfrak g^R\), and let \(H\subseteq G\) be the compact connected subgroup with Lie algebra \(\mathfrak h\), given by U.3. Throughout this section assume that \(H\) is **not transitive** on the unit sphere: its action does not carry every unit vector to every other unit vector.

A linear subspace \(W\subseteq V\) is **flat** if
\[
Q_{u,v}=0\qquad(u,v\in W,\ Q\in\mathcal M).
\]
This is a condition on every tensor in the orbit span, not merely on \(R\). A subspace \(E\subseteq V\) is called **geodesic for \(\mathcal M\)** if
\[
Q_{x,y}z\in E\qquad(x,y,z\in E,\ Q\in\mathcal M).
\]
The latter term is an algebraic condition here.

**Lemma V.1 (a flat through every vector).** Every vector of \(V\) belongs to a flat of dimension at least two. Such a flat is contained in a maximal flat.

**Proof.** Pair symmetry gives an equivalent test:
\[
W\text{ is flat}\quad\Longleftrightarrow\quad
\mathfrak h(W)\subseteq W^\perp.
\tag{V.1}
\]
Indeed the right-hand condition says
\(\langle Q_{x,y}u,v\rangle=0\) for every \(x,y\in V\), \(u,v\in W\), \(Q\in\mathcal M\), since these operators span \(\mathfrak h\). Pair symmetry converts this to
\(\langle Q_{u,v}x,y\rangle=0\) for all \(x,y\), which is exactly the left-hand condition. The action (U.3), together with invariance of \(\mathcal M\), also shows that \(gW\) is flat whenever \(W\) is flat and \(g\in G\).

If \(R=0\), then \(\mathcal M=0\) and \(W=V\) suffices. Suppose \(R\ne0\). Some \(R_{x,y}\ne0\), so \(\mathfrak h\ne0\) and \(H\ne\{I\}\). The subgroup \(H\) is normal in \(G\), as proved in U.3. Its fixed subspace
\[
V^H=\{v:hv=v\text{ for all }h\in H\}
\]
is \(G\)-invariant: \(h(gv)=g(g^{-1}hg)v=gv\) when \(v\in V^H\). Irreducibility makes it zero or \(V\). The latter would make every matrix in \(H\) the identity, contrary to \(H\ne\{I\}\). Thus \(V^H=0\).

Fix a unit vector \(u\). Its \(H\)-orbit is not the whole sphere, for such an orbit would make the action transitive. Choose a unit vector \(v\notin H u\). Compactness of \(H\) makes the continuous real function \(h\mapsto\langle u,hv\rangle\) attain a maximum at some \(h_0\). Here one can apply the compact maximum principle of Local tools 0.1 to its compact real image. Put \(w=h_0v\). Differentiating along \(\exp(tB)h_0\), \(B\in\mathfrak h\), gives
\[
\langle u,Bw\rangle=0.
\]
For \(B=Q_{x,y}\) pair symmetry yields
\[
0=Q(x,y,w,u)=Q(w,u,x,y)\qquad(x,y\in V).
\]
Hence \(Q_{u,w}=0\) for every \(Q\in\mathcal M\).

The unit vectors \(u,w\) are linearly independent. Equality \(w=u\) would give \(v\in H u\), which was excluded. If \(w=-u\), the maximum would be \(-1\). Every unit vector \(hv\) has inner product at least \(-1\) with \(u\), as follows from \(\|hv+u\|^2\ge0\). Thus all would have inner product exactly \(-1\), and that same squared-norm identity would give \(hv=-u\) for all \(h\). Taking \(h=I\) gives \(v=-u\), and then every \(h\) fixes the nonzero vector \(u\), contradicting \(V^H=0\).

Alternation and bilinearity now make \(\operatorname{span}\{u,w\}\) flat. It contains every scalar multiple of \(u\); the zero vector belongs to any such flat. To extend it maximally, choose a containing flat of largest dimension. The possible dimensions are integers between two and \(\dim V\), and the set of possible dimensions is nonempty, so its maximum is attained. Any strictly larger containing flat would have larger dimension. This proves maximality without a closure or limiting argument. □

**Lemma V.2 (the zero-pair identity and commuting Jacobi operators).** If \(u,v\in V\) obey \(P_{u,v}=0\) for every \(P\in\mathcal M\), then
\[
P_{Bu,v}+P_{u,Bv}=0
\qquad(B\in\mathfrak g,\ P\in\mathcal M).
\tag{V.2}
\]
For a flat \(W\), define
\[
T_Q^{u,v}z=Q_{u,z}v
\qquad(u,v\in W,\ Q\in\mathcal M).
\tag{V.3}
\]
These operators are self-adjoint and satisfy \(T_Q^{u,v}=T_Q^{v,u}\). They kill \(W\), and
\[
T_Q^{u,v}T_P^{s,t}=T_Q^{s,t}T_P^{u,v}
\qquad(u,v,s,t\in W,\ P,Q\in\mathcal M).
\tag{V.4}
\]
For each fixed \(Q\), all the operators \(T_Q^{u,v}\) admit a common orthonormal eigenbasis. For a unit common eigenvector \(X\), its eigenvalues form a symmetric bilinear form \(\Lambda\) on \(W\):
\[
T_Q^{u,v}X=\Lambda(u,v)X.
\tag{V.5}
\]
If \(\Lambda\ne0\), then \(X\perp W\).

**Proof.** The module \(\mathcal M\) is preserved by the infinitesimal action, as proved in U.2. Hence both \(P_{u,v}\) and \((B\cdot P)_{u,v}\) vanish under the assumed zero-pair condition. Formula (U.4) gives (V.2).

For \(u,v\in W\), Bianchi and \(Q_{u,v}=0\) give \(Q_{u,z}v=Q_{v,z}u\); this is symmetry of (V.3) in \(u,v\). Pair symmetry then gives
\[
\langle T_Q^{u,v}z,t\rangle
=Q(u,z,v,t)=Q(v,t,u,z)
=\langle z,T_Q^{v,u}t\rangle
=\langle z,T_Q^{u,v}t\rangle,
\]
proving self-adjointness. If \(z\in W\), flatness gives \(Q_{u,z}=0\), so the operators kill \(W\).

We verify the mixed identity on an arbitrary \(z\in V\):
\[
\begin{aligned}
T_Q^{u,v}T_P^{s,t}z
 &=Q_{u,P_{s,z}t}v\\
 &=-Q_{P_{s,z}u,t}v\\
 &=-Q_{P_{u,z}s,t}v\\
 &=Q_{t,P_{u,z}s}v\\
 &=Q_{v,P_{u,z}s}t\\
 &=-Q_{P_{u,z}v,s}t\\
 &=Q_{s,P_{u,z}v}t
 =T_Q^{s,t}T_P^{u,v}z.
\end{aligned}
\]
The second and sixth lines use (V.2) on the pairs \((u,t)\) and \((v,s)\), respectively, with the curvature operators \(P_{s,z},P_{u,z}\in\mathfrak g\). The third and fifth use the symmetry in (V.3). The fourth and seventh use skewness of the first pair. This proves (V.4).

Take \(P=Q\). The resulting identity says all \(T_Q^{u,v}\), for this fixed \(Q\), commute. For a basis \(w_1,\ldots,w_r\) of \(W\), bilinearity expresses every one as a linear combination of the finite collection \(T_Q^{w_i,w_j}\). Diagonalize the first member by the complete real spectral proof in H.2. Each remaining operator preserves its eigenspaces, because it commutes with the first. Diagonalize the next operator on those eigenspaces, and continue through the finite collection. The restrictions are still self-adjoint. This is exactly the finite joint-eigenspace construction proved in H.2, and gives a common orthonormal basis for all their linear combinations.

For a unit basis vector \(X\), the eigenvalue is
\(\Lambda(u,v)=\langle T_Q^{u,v}X,X\rangle\), which is bilinear and symmetric. If this form is nonzero, choose \(u,v\) with \(\Lambda(u,v)\ne0\). For \(w\in W\), self-adjointness and \(T_Q^{u,v}w=0\) imply
\[
\Lambda(u,v)\langle X,w\rangle
=\langle T_Q^{u,v}X,w\rangle
=\langle X,T_Q^{u,v}w\rangle=0.
\]
Thus \(X\perp W\). No simultaneous diagonalization for different \(Q\)'s has been claimed or used. □

**Lemma V.3 (rank-one eigenvalue forms).** In (V.5), if \(\Lambda\ne0\), its kernel
\[
U=\{s\in W:\Lambda(s,t)=0\text{ for every }t\in W\}
\]
is a hyperplane, and
\[
P_{s,X}=0\qquad(s\in U,\ P\in\mathcal M).
\tag{V.6}
\]
For a unit vector \(e\in U^\perp\cap W\) there is a nonzero real \(\lambda\) such that
\[
\Lambda(u,v)=\lambda\langle u,e\rangle\langle v,e\rangle.
\tag{V.7}
\]

**Proof.** There is \(a\in W\) with \(\Lambda(a,a)\ne0\). Otherwise expansion of \(\Lambda(u+v,u+v)\) would give \(2\Lambda(u,v)=0\) for all \(u,v\), contrary to nonzero \(\Lambda\). Initially set
\[
U'=\{s\in W:\Lambda(a,s)=0\}.
\]
The functional defining it is nonzero at \(a\), so \(U'\) is a hyperplane. One can see this directly by decomposing
\(s=(s-\Lambda(a,s)a/\Lambda(a,a))+\Lambda(a,s)a/\Lambda(a,a)\)
into \(U'\) and \(\mathbb R a\).

For \(s\in U'\), use (V.2) on \((s,a)\), with \(B=Q_{a,X}\) and arbitrary \(P\in\mathcal M\). The two eigenvector identities for \(Q\) give
\[
\begin{aligned}
\Lambda(a,a)P_{s,X}
 &=P_{s,Q_{a,X}a}
 =-P_{Q_{a,X}s,a}\\
 &=-\Lambda(a,s)P_{X,a}=0.
\end{aligned}
\]
Thus \(P_{s,X}=0\) for every \(P\), proving (V.6) first on \(U'\). In particular
\(\Lambda(s,t)X=Q_{s,X}t=0\) for all \(t\in W\), so \(U'\subseteq U\). The reverse inclusion follows by taking \(t=a\) and using symmetry. Hence \(U=U'\) is a hyperplane.

Choose a unit vector \(e\) in its one-dimensional orthogonal complement in \(W\). Every \(u\in W\) has decomposition \(u=u_0+\langle u,e\rangle e\) with \(u_0\in U\). Applying this in both slots yields (V.7) with \(\lambda=\Lambda(e,e)\). This scalar cannot vanish, or the whole form would be zero. Its sign is unrestricted. □

For any subspace \(U\subseteq W\), define its curvature centralizer by
\[
C(U)=\{z\in V:P_{u,z}=0
           \text{ for all }u\in U,\ P\in\mathcal M\}.
\tag{V.8}
\]
It is a linear subspace, by bilinearity. For a maximal flat \(W\), a nonzero eigenvalue form \(\Lambda\) as above, and its kernel \(U\), call \(E=C(U)\) a **root centralizer**. This name refers to the hyperplane arising in V.3; no Lie root system is being assumed. We consider all such common unit eigenvectors and all \(Q\in\mathcal M\), so the definition does not require a simultaneous choice of eigenbases.

**Lemma V.4 (proper geodesic centralizers and their intersections).** Let \(W\) be a maximal flat, and suppose \(R\ne0\) and \(\dim W\ge2\). Every centralizer \(C(U)\) is geodesic for \(\mathcal M\). Every root centralizer \(E=C(U)\) satisfies
\[
U\subsetneq W\subsetneq E\subsetneq V,
\tag{V.9}
\]
and the restriction of \(\mathcal M\) to \(E^4\) is nonzero. Furthermore
\[
C(W)=W,\qquad
U=\{u\in W:P_{u,z}=0
        \text{ for all }z\in E,\ P\in\mathcal M\}.
\tag{V.10}
\]
Any two distinct root centralizers have intersection exactly \(W\).

**Proof.** Linearity gives, for any \(U_1,U_2\subseteq W\),
\[
C(U_1+U_2)=C(U_1)\cap C(U_2).
\tag{V.11}
\]
Flatness implies \(W\subseteq C(W)\). If \(z\in C(W)\), expand \(P_{w+az,w'+bz}\) using bilinearity and alternation: its four terms vanish by flatness, the definition of \(C(W)\), and \(P_{z,z}=0\). Thus \(W+\mathbb Rz\) is flat. Maximality gives \(z\in W\), proving the first assertion in (V.10).

To prove geodesy, set \(E=C(U)\) and take \(a,b,z\in E\). For \(u\in U\) and \(P\in\mathcal M\), the operators \(P_{u,a}\) and \(P_{u,b}\) are zero. Bianchi gives \(P_{a,b}u=0\). Now apply (V.2) to the universal zero pair \((u,z)\), with \(B=P_{a,b}\). For every \(Q\in\mathcal M\) it gives
\[
Q_{u,P_{a,b}z}=-Q_{P_{a,b}u,z}=0.
\]
Therefore \(P_{a,b}z\in C(U)\), as required.

For a root centralizer, V.3 makes \(U\) a hyperplane in \(W\), and flatness gives \(W\subseteq C(U)\). The associated common eigenvector \(X\) lies in \(C(U)\) by (V.6). It is a unit vector perpendicular to \(W\) by V.2. This proves the first two strict containments in (V.9).

For the last one define the common nullity
\[
N_0=\{u\in V:P_{u,v}=0
         \text{ for every }v\in V,\ P\in\mathcal M\}.
\]
This is \(G\)-invariant. Indeed for \(g\in G\),
\[
P_{gu,v}
=g\,\bigl((g^{-1}\cdot P)_{u,g^{-1}v}\bigr)\,g^{-1}=0
\]
when \(u\in N_0\), since \(g^{-1}\cdot P\in\mathcal M\). If \(C(U)=V\), its definition gives \(U\subseteq N_0\). The hyperplane \(U\) has dimension \(\dim W-1\ge1\), so \(N_0\ne0\). Irreducibility would imply \(N_0=V\), making every \(P\), including \(R\), zero. This contradicts \(R\ne0\). Hence \(E\subsetneq V\).

For the \(Q,X,e,\lambda\) producing this root, (V.5) and (V.7) give
\[
Q_{e,X}e=\lambda X,\qquad Q(e,X,e,X)=\lambda\ne0.
\tag{V.12}
\]
All four vectors belong to \(E\), so the restriction of \(\mathcal M\) there is nonzero.

The inclusion from left to right in the second equality of (V.10) is the definition of \(C(U)\). If \(u\in W\setminus U\), then
\[
Q_{u,X}e=\Lambda(u,e)X
 =\lambda\langle u,e\rangle X\ne0.
\]
Since \(X\in E\), this excludes \(u\) from the right side. Equality follows. In particular \(E\) determines its hyperplane \(U\).

If root centralizers \(E=C(U)\) and \(E'=C(U')\) differ, their hyperplanes differ. Two distinct hyperplanes in \(W\) have sum \(W\): choose \(u'\in U'\setminus U\); the one-dimensional quotient by \(U\) is spanned by its nonzero class, so \(U+\mathbb R u'=W\). Equation (V.11) now gives
\[
E\cap E'=C(U+U')=C(W)=W.
\]
This proves the final assertion. □

## W. Restriction kernels and a trace calculation

The first result below applies to a holonomy system with compact connected \(G\), without irreducibility or a nontransitivity assumption. Let \(\mathcal M=\mathcal M_R\). If a subspace \(E\subseteq V\) is geodesic for every tensor in \(\mathcal M\), restriction defines a linear map
\[
r_E:\mathcal M\longrightarrow\mathcal R(E),\qquad
r_E(Q)=Q|_{E^4}.
\]
Geodesy identifies the restricted endomorphisms with endomorphisms of \(E\); all curvature symmetries remain valid there. Set
\[
K_E=\ker r_E,\qquad
J_E=\{B\in\mathfrak g:B\cdot Q\in K_E
                  \text{ for every }Q\in\mathcal M\}.
\tag{W.1}
\]

**Theorem W.1 (invariant restriction kernels and cross curvature).** The subspace \(K_E\) is \(G\)-invariant, even if \(E\) is not. The subspace \(J_E\) is an ideal of \(\mathfrak g\). If \(B\in\mathfrak g\) satisfies \(B(E)\subseteq E^\perp\), then \(B\in J_E\). In particular,
\[
P_{x,y}\in J_E
\qquad(x\in E,\ y\in E^\perp,\ P\in\mathcal M).
\tag{W.2}
\]
For \(B\in J_E\), the whole orbit span \(\mathcal M_{B\cdot R}\) is contained in \(K_E\).

**Proof.** If \(Q\in K_E\), then for \(x,y,z\in E\), geodesy puts \(Q_{x,y}z\) in \(E\), while restriction being zero makes it perpendicular to all of \(E\). Hence
\[
Q_{x,y}z=0\qquad(x,y,z\in E).
\tag{W.3}
\]
Consequently any component of \(Q\) with three arguments in \(E\) is zero, regardless of the fourth argument. To see all four placements explicitly, for \(x,y,z,t\in E\) and arbitrary \(a\in V\),
\[
\begin{aligned}
Q(a,y,z,t)&=Q(z,t,a,y)=-\langle a,Q_{z,t}y\rangle=0,\\
Q(x,a,z,t)&=-Q(a,x,z,t)=0,\\
Q(x,y,a,t)&=-\langle a,Q_{x,y}t\rangle=0,\\
Q(x,y,z,a)&=\langle Q_{x,y}z,a\rangle=0.
\end{aligned}
\]
The four-slot formula (U.4) therefore shows that \(B\cdot Q\in K_E\) for every \(B\in\mathfrak g\).

Infinitesimal invariance implies group invariance here as follows. On the finite-dimensional tensor space, \(Q(t)=\exp(tB)\cdot Q\) solves the linear equation \(Q'(t)=B\cdot Q(t)\), by the action law and differentiation. The operator on the right preserves \(K_E\), so its solution starting in \(K_E\) stays in \(K_E\), by uniqueness of the linear ODE in Local tools 2.1. The exponential-generation argument in F.1 then gives invariance under all of connected \(G\).

For the ideal assertion, denote \(B\cdot Q\) by \(\rho(B)Q\). The four-slot formula also proves
\[
\rho([A,B])=\rho(A)\rho(B)-\rho(B)\rho(A).
\tag{W.4}
\]
In expanding the right side, operations on distinct slots commute and cancel. On the same slot the difference inserts \(BA-AB=-[A,B]\), which is exactly that slot's contribution to the left side. If \(B\in J_E\) and \(A\in\mathfrak g\), then \(\rho(A)\rho(B)Q\in K_E\) because \(K_E\) is invariant, while \(\rho(B)\rho(A)Q\in K_E\) by the definition of \(J_E\). Thus \([A,B]\in J_E\).

Now let \(Q\in\mathcal M\), without assuming it belongs to \(K_E\), and let \(a\in E^\perp\). Each of the four component expressions above still vanishes: in the first and third, geodesy puts \(Q_{z,t}y\) or \(Q_{x,y}t\) in \(E\), and in the fourth it puts \(Q_{x,y}z\) in \(E\). Orthogonality to \(a\) suffices. If \(B(E)\subseteq E^\perp\), every term of (U.4) on four vectors in \(E\) is of this form, proving \(B\cdot Q\in K_E\) and \(B\in J_E\).

For \(B=P_{x,y}\) as in (W.2), and \(z,t\in E\), pair symmetry gives
\[
\langle Bz,t\rangle
=P(x,y,z,t)=P(z,t,x,y)
=\langle P_{z,t}x,y\rangle=0.
\]
The last equality uses geodesy and \(y\perp E\). Thus \(B(E)\subseteq E^\perp\), proving (W.2). Finally \(B\cdot R\in K_E\) by definition, and invariance of \(K_E\) puts its entire orbit and linear orbit span there. □

**Lemma W.2 (trace vanishing for an ideal of symmetries).** Let \(\mathfrak g\subseteq\mathfrak{so}(V)\) be any Lie subalgebra and let \(Q\) be an algebraic curvature tensor taking values in \(\mathfrak g\). Suppose \(\mathfrak n\) is an ideal in \(\mathfrak g\) and
\[
B\cdot Q=0\qquad(B\in\mathfrak n).
\]
If \(A=Q_{x,y}\in\mathfrak n\) and \(Ax=0\), then \(A=0\).

**Proof.** Work on the vector space \(\mathcal L=\mathfrak g\oplus V\). For \(B\in\mathfrak g\) and \(x\in V\), define linear operators on it by
\[
L_B(C+z)=[B,C]+Bz,\qquad
L_x(C+z)=Q_{x,z}-Cx.
\tag{W.5}
\]
We only use these as linear operators; a Lie algebra structure on \(\mathcal L\) is unnecessary. Define a further linear operator
\[
F_{x,y}(C+z)=(C\cdot Q)_{x,y}\in\mathfrak g.
\]
It vanishes on the \(V\)-summand. A calculation on each summand gives
\[
[L_x,L_y]=L_{Q_{x,y}}+F_{x,y}.
\tag{W.6}
\]
Indeed for \(C\in\mathfrak g\),
\[
[L_x,L_y]C=-Q_{x,Cy}-Q_{Cx,y}
 =[Q_{x,y},C]+(C\cdot Q)_{x,y},
\]
where the last identity is (U.4). For \(z\in V\), Bianchi gives
\[
[L_x,L_y]z=-Q_{y,z}x+Q_{x,z}y=Q_{x,y}z.
\]
This proves (W.6) on all of \(\mathcal L\).

The ideal condition now has a precise role. Because \(A\in\mathfrak n\), for every \(C\in\mathfrak g\) we have \([A,C]\in\mathfrak n\), so
\[
F_{x,y}L_A(C+z)=([A,C]\cdot Q)_{x,y}=0.
\tag{W.7}
\]
Also \(A\cdot Q=0\). On the two summands (W.5) therefore gives
\[
\begin{aligned}
[L_A,L_x]C&=-ACx+[A,C]x=-C(Ax),\\
[L_A,L_x]z&=[A,Q_{x,z}]-Q_{x,Az}=Q_{Ax,z}.
\end{aligned}
\]
Thus
\[
[L_A,L_x]=L_{Ax}=0,
\tag{W.8}
\]
using the hypothesis \(Ax=0\).

Combine (W.6) with \(A=Q_{x,y}\), multiply on the right by \(L_A\), and use (W.7). Cyclicity of the finite matrix trace, proved in F.1, gives
\[
\begin{aligned}
\operatorname{tr}_{\mathcal L}(L_A^2)
 &=\operatorname{tr}_{\mathcal L}([L_x,L_y]L_A)\\
 &=\operatorname{tr}_{\mathcal L}
       (L_A L_x L_y-L_x L_A L_y)\\
 &=\operatorname{tr}_{\mathcal L}([L_A,L_x]L_y)=0.
\end{aligned}
\tag{W.9}
\]
On the other hand \(L_A\) is block diagonal, with blocks \(\operatorname{ad}_A\) on \(\mathfrak g\) and \(A\) on \(V\). The trace inner product \((\, ,\,)_*\) of U.1 is positive definite on \(\mathfrak g\), and its invariance makes \(\operatorname{ad}_A\) skew-adjoint there. In orthonormal bases on the two summands, the elementary squared-trace calculation of F.1 yields
\[
\operatorname{tr}_{\mathcal L}(L_A^2)
=-\sum_{i,j}(\operatorname{ad}_A)_{ij}^{\,2}
 -\sum_{r,s}A_{rs}^{\,2}.
\tag{W.10}
\]
Equations (W.9)–(W.10) make every entry of \(A\) zero. This proves the conclusion without assuming irreducibility, compactness of an integrating group, or invariance of \(Q\) under the whole of \(\mathfrak g\). □

## X. The Berger–Simons transitivity theorem

**Theorem X.1 (algebraic holonomy and transitivity).** Let \((V,R,G)\) be a holonomy system, with \(\dim V\ge2\), compact connected \(G\subseteq\mathrm{SO}(V)\), and irreducible action. Let \(H=G^R\) be the connected subgroup with Lie algebra \(\mathfrak g^R\), as in U.8 and U.3. If \(H\) is not transitive on the unit sphere, then
\[
g\cdot R=R\qquad(g\in G).
\tag{X.1}
\]
Moreover the maximal dimension of a flat is at least two. In particular, nontransitivity of \(G\) itself implies (X.1).

**Proof.** Write \(\mathcal M=\mathcal M_R\). We prove the assertion by strong induction on the nonnegative integer \(k=\dim\mathcal M\), simultaneously for all finite ambient dimensions at least two. This lets us apply induction to a different tensor on the same \(V\) while keeping the original irreducible action of \(G\).

If \(k=0\), then \(R=0\), which is fixed, and the whole of \(V\) is flat. If \(k=1\), \(G\) acts orthogonally on the real line \(\mathcal M\), by U.1. The coefficient of its action on a unit vector of that line is \(1\) or \(-1\), and is continuous in \(g\). Connectedness makes it constant, since the inverse images of these separated values are both open and closed. At the identity it is \(1\). Thus \(G\) fixes \(R\). In this case V.1 supplies a flat of dimension at least two.

Fix \(k\ge2\) and suppose the result is proved for every smaller orbit-span dimension. Define the annihilator
\[
\mathfrak n=\{B\in\mathfrak g:B\cdot P=0
                         \text{ for every }P\in\mathcal M\}.
\tag{X.2}
\]
The commutator identity (W.4) makes this an ideal: if \(B\) annihilates \(\mathcal M\), then
\([A,B]\cdot P=A\cdot(B\cdot P)-B\cdot(A\cdot P)=0\).
It is also \(\operatorname{Ad}(G)\)-invariant. To check this directly, differentiate the group action after conjugating \(\exp(tB)\) by \(g\); it gives
\[
(\operatorname{Ad}_g B)\cdot P
 =g\cdot\bigl(B\cdot(g^{-1}\cdot P)\bigr).
\tag{X.3}
\]
Since \(\mathcal M\) is \(G\)-invariant, this is zero for \(B\in\mathfrak n\). Applying the same argument to \(g^{-1}\) gives equality of the transformed ideals.

We first prove the consequence of induction that will be used throughout the rest of the argument. Suppose \(E\subsetneq V\) is geodesic for \(\mathcal M\) and \(r_E\ne0\). Then
\[
K_E\subseteq\mathcal M^G,\qquad J_E=\mathfrak n,
\tag{X.4}
\]
where \(\mathcal M^G\) denotes the tensors fixed by every element of \(G\). In fact W.1 makes \(K_E\) invariant, and \(r_E\ne0\) makes it a proper subspace of \(\mathcal M\). For \(T\in K_E\) we have
\[
\mathcal M_T\subseteq K_E,\qquad
\dim\mathcal M_T<k,\qquad
\mathfrak g^T\subseteq\mathfrak g^R.
\]
The first two assertions use invariance and the dimension inequality; the third is U.2. By U.3, the two ideals integrate to the connected compact subgroups \(G^T,H\). The first is contained in the second, because it is generated by exponentials of its smaller Lie algebra. A subgroup of a nontransitive group cannot be transitive: its orbit is contained in the corresponding orbit of the larger group. Consequently \((V,T,G)\) satisfies the induction hypotheses, including the same irreducible action of \(G\) and a nontransitive curvature-generated subgroup. Induction makes \(T\) fixed by \(G\). This proves \(K_E\subseteq\mathcal M^G\).

If \(B\in J_E\) and \(P\in\mathcal M\), then \(B\cdot P\in K_E\), hence is fixed by \(G\). Differentiating its invariance gives \(B\cdot(B\cdot P)=0\). The skew-action identity (U.5) now yields
\[
\|B\cdot P\|^2
=-\langle B\cdot(B\cdot P),P\rangle=0.
\]
Thus \(B\) annihilates all of \(\mathcal M\), so \(J_E\subseteq\mathfrak n\). The reverse inclusion follows immediately from the definition of \(J_E\). This finishes (X.4). Combined with (W.2), it gives
\[
P_{E,E^\perp}\subseteq\mathfrak n
\quad\text{whenever }E\subsetneq V
\text{ is geodesic and }r_E\ne0.
\tag{X.5}
\]

We next produce enough subspaces to use this conclusion. Since \(k\ge2\), \(R\ne0\). By sectional determination in U.1 there are \(a,b\in V\) with \(R(a,b,a,b)\ne0\). Lemma V.1 supplies a flat of dimension at least two through \(a\), and extends it to a maximal flat \(W\). The operator \(T_R^{a,a}\) is nonzero, because
\[
\langle T_R^{a,a}b,b\rangle=R(a,b,a,b)\ne0.
\]
Its common eigenbasis from V.2 therefore has at least one nonzero eigenvalue form on \(W\). The family \(\mathscr E\) of all root centralizers associated to this \(W\), all \(Q\in\mathcal M\), and all their nonzero common eigenvalue forms is consequently nonempty. Lemma V.4 says that every \(E\in\mathscr E\) is proper, geodesic, contains \(W\), and has \(r_E\ne0\). Thus (X.5) applies to each:
\[
P_{E,E^\perp}\subseteq\mathfrak n
\qquad(E\in\mathscr E,\ P\in\mathcal M).
\tag{X.6}
\]

We claim that these centralizers span \(V\). Let
\(F=\sum_{E\in\mathscr E}E\), where a sum of subspaces means the set of finite sums of their vectors, and take \(z\in F^\perp\). For a fixed \(Q\in\mathcal M\), use a common orthonormal eigenbasis for the \(T_Q^{u,v}\)'s. Every basis vector with nonzero eigenvalue form lies in its root centralizer by V.3, and hence lies in \(F\). It is perpendicular to \(z\). Expanding \(z\) in this basis leaves only basis vectors whose eigenvalue forms are zero. Therefore
\[
Q_{w,z}w=T_Q^{w,w}z=0
\qquad(w\in W,\ Q\in\mathcal M).
\tag{X.7}
\]
This argument is made separately for each \(Q\); it does not assume a common eigenbasis for different tensors.

Fix \(w,Q\) and set \(A=Q_{w,z}\). Choose any \(E\in\mathscr E\), which is possible because the family is nonempty. Since \(w\in W\subset E\) and \(z\in F^\perp\subseteq E^\perp\), (X.6) gives \(A\in\mathfrak n\). The ideal \(\mathfrak n\) annihilates \(Q\), and (X.7) says \(Aw=0\). Lemma W.2, applied with \(x=w,y=z\), implies \(A=0\). This holds for every \(w,Q\), so \(z\in C(W)=W\) by V.4. But \(W\subset F\) and \(z\perp F\), forcing \(\|z\|^2=0\). Hence \(F^\perp=0\), and finite-dimensional orthogonal decomposition gives \(F=V\).

There must now be two distinct members \(E_1,E_2\) of \(\mathscr E\). Otherwise its sum would be a single proper subspace. By V.4,
\[
E_1\cap E_2=W,\qquad
E_1^\perp+E_2^\perp=W^\perp.
\tag{X.8}
\]
For completeness, the second identity follows without a topological closure: a vector is perpendicular to \(E_1^\perp+E_2^\perp\) exactly when it lies in both \(E_1\) and \(E_2\). Taking orthogonal complements again gives the result, since every finite-dimensional subspace equals its double orthogonal complement by the orthonormal-basis projection formula.

For \(P\in\mathcal M\), \(w\in W\), and arbitrary \(z\in V\), decompose
\[
z=z_W+z_1+z_2,\qquad
z_W\in W,\quad z_i\in E_i^\perp,
\]
using (X.8) and \(V=W\oplus W^\perp\). Flatness makes \(P_{w,z_W}=0\), and (X.6) puts both other terms in \(\mathfrak n\). Thus
\[
P_{W,V}\subseteq\mathfrak n
\qquad(P\in\mathcal M).
\tag{X.9}
\]
For \(g\in G\), the action law (U.3) gives
\[
P_{gw,z}
=\operatorname{Ad}_g
 \bigl((g^{-1}\cdot P)_{w,g^{-1}z}\bigr)\in\mathfrak n,
\]
by (X.9), invariance of \(\mathcal M\), and (X.3). The span of all \(gW\) is a nonzero \(G\)-invariant subspace: it contains the nonzero \(W\), and multiplication by any group element permutes the collection of translates. Irreducibility makes that span \(V\). Linearity in the first argument therefore gives
\[
P_{x,y}\in\mathfrak n
\qquad(x,y\in V,\ P\in\mathcal M).
\]
Their span is \(\mathfrak g^R\), so \(\mathfrak g^R\subseteq\mathfrak n\). By U.2 its orthogonal complementary ideal \(\mathfrak g_R\) also annihilates every tensor in \(\mathcal M\). The decomposition
\(\mathfrak g=\mathfrak g^R\oplus\mathfrak g_R\)
thus gives \(\mathfrak n=\mathfrak g\).

Every infinitesimal action on \(R\) is consequently zero. Along \(\exp(tB)\cdot R\) the linear action equation has the constant solution \(R\); uniqueness and connected exponential generation, as in W.1, give \(g\cdot R=R\) for all \(g\). The flat \(W\) has dimension at least two. This completes the induction. Finally \(H\subseteq G\); if \(G\) is nontransitive, so is \(H\), proving the last assertion. □

**Theorem X.2 (the geometric transitivity conclusion).** Let \(M\) be a nonempty connected Riemannian manifold of dimension \(n\ge2\) whose restricted holonomy action is irreducible. If \(\nabla R\) is not identically zero, its restricted holonomy group acts transitively on the unit sphere at every point. Equivalently, if the group is nontransitive at even one point, then \(\nabla R=0\) everywhere. Completeness and simple connectivity are not required.

**Proof.** First assume \(n\ge3\), and suppose the group at \(p\) is nontransitive. By F.2, \(G=H_p^0\) is compact, connected and embedded in \(\mathrm{SO}(T_pM)\). For every algebraic curvature tensor \(Q\) with values in \(\mathfrak h_p\), the triple \((T_pM,Q,G)\) satisfies the hypotheses of X.1. Its curvature-generated subgroup is contained in nontransitive \(G\). Hence X.1 says \(g\cdot Q=Q\) for every \(g\in G\). This is precisely the algebraic-invariance hypothesis of U.5, which gives \(\nabla R=0\) throughout \(M\).

We include the two-dimensional case, for which the scalar-constancy argument in U.5 was deliberately not asserted. Here every compact connected irreducible subgroup \(G\subseteq\mathrm{SO}(2)\) is \(\mathrm{SO}(2)\) itself. Indeed its Lie algebra is a subspace of the one-dimensional space of \(2\)-by-\(2\) skew matrices. If that subspace were zero, connected exponential generation from F.1 would make \(G=\{I\}\), which preserves every line and is reducible. Its Lie algebra must therefore be the full \(\mathfrak{so}(2)\). The inverse-function theorem, Local tools 1.2, applied to the embedded inclusion gives an open identity neighbourhood of \(\mathrm{SO}(2)\) in \(G\). Thus \(G\) is an open subgroup.

Here is the needed connectedness of the ambient group explicitly. Every matrix in \(\mathrm{SO}(2)\) is
\[
\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
\qquad a^2+b^2=1:
\]
its first column is a unit vector \((a,b)\), its orthogonal unit second column is one of \(\pm(-b,a)\), and the positive determinant selects the indicated choice. Two nonopposite unit vectors are joined on the unit circle by normalizing their straight segment; that segment never passes through zero. If the target is opposite \((1,0)\), first join \((1,0)\) to \((0,1)\) and then to the target. Thus every first column is joined continuously to \((1,0)\), and the displayed matrices give a continuous path to the identity. This proves connectedness of \(\mathrm{SO}(2)\). An open subgroup has open complementary cosets, so connectedness makes it the whole group.

Finally these matrices act transitively on the unit circle: for unit vectors \(u,v\), let \(A_u,A_v\) be the displayed matrices with those first columns. Then \(A_vA_u^{-1}\in\mathrm{SO}(2)\) sends \(u\) to \(v\). Thus nontransitivity is impossible in dimension two. The conclusions of the theorem follow in all the stated dimensions. □

Theorem X.2 supplies a transitivity condition for irreducible holonomy with nonparallel curvature. Sections Y–AG construct and classify the transitive representations, then apply the curvature exclusions to obtain the holonomy list.

## Y. Classical and quaternionic representations

The names of matrix groups in a holonomy statement specify their real representations, not just abstract groups. We construct the classical representations and the quaternionic product action here.

**Lemma Y.1 (quaternion arithmetic and its complex matrices).** There is an associative real division algebra \(\mathbb H\) with real basis \(1,i,j,k\), satisfying
\[
i^2=j^2=k^2=-1,\qquad
ij=k=-ji,\quad jk=i=-kj,\quad ki=j=-ik.
\tag{Y.1}
\]
Writing its elements as \(q=z+w j\), \(z,w\in\mathbb C\), an injective real algebra homomorphism is
\[
\chi(q)=
\begin{pmatrix}z&w\\-\overline w&\overline z\end{pmatrix}.
\tag{Y.2}
\]
Its conjugation and norm are
\[
\overline q=\overline z-wj,\qquad
|q|^2=|z|^2+|w|^2,\qquad
q^{-1}=\overline q/|q|^2\quad(q\ne0).
\tag{Y.3}
\]
Conjugation reverses products, the norm is multiplicative, and the centre of \(\mathbb H\) is \(\mathbb R\).

**Proof.** Define \(\mathbb H=\mathbb C^2\) as a real vector space, and set
\[
(z,w)(u,v)=(zu-w\overline v,\ zv+w\overline u).
\tag{Y.4}
\]
Multiplying the two matrices in (Y.2) gives exactly the matrix of (Y.4): its first row is the displayed pair, and its second row is minus the conjugate of the second entry followed by the conjugate of the first. Thus \(\chi\) preserves multiplication and is injective, since its first row recovers the pair. Associativity follows from associativity of complex matrix multiplication and injectivity. The element \((1,0)\) is the identity. Put \(i=(i,0)\), \(j=(0,1)\), \(k=(0,i)\); substitution into (Y.4) gives every relation in (Y.1).

Conjugate transpose satisfies
\(\chi(q)^*=\chi(\overline z,-w)\).
Because it reverses matrix products and \(\chi\) is injective, the indicated quaternion conjugation reverses products too. Direct multiplication gives
\[
\chi(q)^*\chi(q)=\chi(q)\chi(q)^*
=(|z|^2+|w|^2)I_2.
\]
This proves \(q\overline q=\overline q q=|q|^2\), and gives the inverse in (Y.3). The scalar is strictly positive unless \(q=0\), so division is valid. For products,
\[
\overline{pq}(pq)=\overline q\,\overline p\,p q
=|p|^2\overline q q=|p|^2|q|^2,
\]
proving \(|pq|=|p||q|\) by the positive square root.

For the centre, (Y.4) shows that \(z+w j\) commutes with \(i\) only when \(w=0\): the second components of its products with \(i\) are \(-wi\) and \(iw\), respectively. If \(z\in\mathbb C\) also commutes with \(j\), comparison of \(zj\) and \(jz=\overline z j\) gives \(z=\overline z\), hence \(z\in\mathbb R\). Real scalars commute with every element by (Y.4). This proves the centre assertion. In particular a quaternion commuting with both \(i,j\) is real.

We will also use \(\operatorname{Re}(pq)=\operatorname{Re}(qp)\). It follows from
\(\operatorname{tr}_{\mathbb C}\chi(q)=2\operatorname{Re}q\)
and the elementary trace cyclicity of F.1. Finally for imaginary quaternions \(u,v\in\operatorname{span}_{\mathbb R}\{i,j,k\}\), expansion using (Y.1) gives
\[
uv=-\langle u,v\rangle+u\times v,
\tag{Y.5}
\]
where the inner product makes \(i,j,k\) orthonormal and the cross product is the bilinear alternating operation with \(i\times j=k\), \(j\times k=i\), \(k\times i=j\). Thus (Y.5) is an explicit multiplication identity, not an additional assumption. □

For \(\mathbb F=\mathbb R,\mathbb C,\mathbb H\), use columns in \(\mathbb F^m\), with scalar multiplication on the right and
\[
h(v,w)=\sum_{\ell=1}^m\overline{v_\ell}w_\ell,\qquad
g(v,w)=\operatorname{Re}h(v,w).
\]
A matrix over \(\mathbb F\) acts on the left. Write \(A^*=\overline A^{\,T}\). Define
\[
\begin{aligned}
\mathrm O(m)&=\{A\in M_m(\mathbb R):A^*A=I\},&
\mathrm{SO}(m)&=\{A\in\mathrm O(m):\det_{\mathbb R}A=1\},\\
\mathrm U(m)&=\{A\in M_m(\mathbb C):A^*A=I\},&
\mathrm{SU}(m)&=\{A\in\mathrm U(m):\det_{\mathbb C}A=1\},\\
\mathrm{Sp}(m)&=\{A\in M_m(\mathbb H):A^*A=I\}.&&
\end{aligned}
\tag{Y.6}
\]
No quaternionic determinant is used in this definition of \(\mathrm{Sp}(m)\).

**Theorem Y.2 (the classical compact actions).** For \(m\ge1\), the groups in (Y.6) are compact embedded real matrix Lie groups. The groups \(\mathrm{SO}(m)\), \(\mathrm U(m)\), \(\mathrm{SU}(m)\), and \(\mathrm{Sp}(m)\) are path connected. Their real dimensions are, respectively,
\[
\frac{m(m-1)}2,\qquad m^2,\qquad m^2-1,\qquad m(2m+1).
\tag{Y.7}
\]
Their displayed real representations have dimensions \(m,2m,2m,4m\). The actions on their unit spheres are transitive for \(\mathrm{SO}(m)\) and \(\mathrm{SU}(m)\) when \(m\ge2\), and for \(\mathrm U(m)\) and \(\mathrm{Sp}(m)\) when \(m\ge1\). Each of these transitive actions is irreducible over \(\mathbb R\). All four connected groups preserve real orientation.

**Proof.** Quaternion associativity and conjugation from Y.1 give \((AB)^*=B^*A^*\), just as for the other two fields, by expanding the matrix entries in their indicated order. We have
\[
h(Av,Aw)=h(v,A^*Aw).
\tag{Y.8}
\]
Thus \(A^*A=I\) implies real norm preservation, so \(A\), as an endomorphism of the finite-dimensional real space \(\mathbb F^m\), is injective and hence invertible. Its left inverse \(A^*\) is therefore its inverse, giving \(AA^*=I\) as well. The adjoint identity proves closure under products and inverses. The determinant-one conditions give subgroups by determinant multiplicativity, proved in F.1.

These are closed bounded sets of real matrices. The equations \(A^*A=I\) and the determinant conditions are continuous polynomial equations in real coordinates. Every column has norm one, bounding every real component of every entry. Local tools 0.1 gives compactness. They are closed subgroups of real general linear groups and hence embedded Lie groups by [Invariant connections, Theorem A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). For the quaternion case, the identification with real matrices is faithful: a right-linear map is determined by its columns, its values on the standard basis. Its image is a closed real linear subspace, alternatively characterized by commuting with right multiplication by \(i\) and \(j\). This justifies applying that closed-subgroup theorem in the same way.

We give explicit paths and transitivity arguments, avoiding an unproved complex spectral theorem. First, the unit spheres in \(\mathbb C\) and \(\mathbb H\) are path connected. The normalized straight segment joins any two nonopposite unit vectors. For an opposite pair, insert a unit vector perpendicular to them and use two such segments. The denominators are nonzero; continuity follows from the Euclidean norm. This is the circle argument of X.2 in real dimensions two and four.

Let \(v\in\mathbb F^m\) have unit norm. For \(\mathbb F=\mathbb C,\mathbb H\), write each nonzero coordinate as \(v_\ell=q_\ell r_\ell\), where \(r_\ell=|v_\ell|>0\) and \(q_\ell\) is a unit scalar; for a zero coordinate put \(q_\ell=1,r_\ell=0\). Multiplication by the diagonal matrix with entries \(q_\ell^{-1}\) sends \(v\) to a vector of nonnegative real coordinates. It is joined to the identity within \(\mathrm U(m)\) or \(\mathrm{Sp}(m)\), by the scalar paths just proved.

For a real vector of unit norm and \(m\ge2\), eliminate its coordinates \(2,\ldots,m\) successively by rotations in the \((1,j)\)-plane. If its current first and \(j\)-th coordinates are \(a,b\), and \(r=\sqrt{a^2+b^2}>0\), use the block
\[
\begin{pmatrix}a/r&b/r\\-b/r&a/r\end{pmatrix},
\tag{Y.9}
\]
which sends \((a,b)\) to \((r,0)\). If \(a=b=0\), skip that step. These blocks lie in \(\mathrm{SO}(2)\) and can each be joined to the identity there by the circle proof of X.2. Extend each by identity on the other coordinates. For an initial vector \((-1,0,\ldots,0)\), the \(j=2\) block is \(-I_2\), so this case also ends with positive first coordinate. Because the original norm is one, the final vector is \(e_1\). Concatenating the finitely many paths, translating each later path by the earlier matrices, produces a path \(P(t)\) from the identity with \(P(1)v=e_1\). The real blocks also belong to the complex and quaternionic groups. When \(m=1\) in those groups, the scalar diagonal step already sends \(v\) to \(e_1\). Consequently the same construction works for all the asserted \(\mathrm{SO}\), \(\mathrm U\), and \(\mathrm{Sp}\) cases.

For \(\mathrm{SU}(m)\), \(m\ge2\), take the just-constructed unitary path \(P(t)\) and replace it by
\[
\widetilde P(t)
=\operatorname{diag}\bigl(1,\det_{\mathbb C}P(t)^{-1},1,\ldots,1\bigr)P(t).
\tag{Y.10}
\]
The determinant of a unitary matrix has modulus one: apply the determinant polynomial to \(P^*P=I\), using \(\det P^*=\overline{\det P}\), which follows term by term from that polynomial. Thus (Y.10) is a path in \(\mathrm{SU}(m)\), starts at the identity, and still sends \(v\) to \(e_1\) at its endpoint. The diagonal correction fixes \(e_1\).

These paths prove sphere transitivity, since paths with endpoints sending \(v\) and \(w\) to \(e_1\) give a group element sending \(v\) to \(w\). They also prove path connectedness of the groups by induction on \(m\). Given \(A\), apply the suitable path on the left to its first column. At the endpoint \(P(1)A\) has first column \(e_1\). Orthogonality of columns gives first row \((1,0,\ldots,0)\), so it is \(\operatorname{diag}(1,B)\), with \(B\) in the corresponding group of size \(m-1\); in the special groups its determinant is still one. Induction joins this block to the identity. The initial cases are \(\mathrm{SO}(1)=\mathrm{SU}(1)=\{1\}\), and the unit scalar spheres for \(\mathrm U(1)\), \(\mathrm{Sp}(1)\). Hence every element is connected to the identity by a path in its group. Since the real determinant of an orthogonal matrix is \(1\) or \(-1\), continuity along these paths proves orientation preservation for every connected group listed.

To calculate dimensions, differentiate \(A(t)^*A(t)=I\) at the identity. Its tangent matrices satisfy \(X^*+X=0\), and in \(\mathfrak{su}(m)\) also \(\operatorname{tr}_{\mathbb C}X=0\), by the determinant derivative (F.7). Conversely these conditions suffice: the real matrix exponential \(E(t)\) of \(X\), constructed in Local tools 2.3, remains right-linear and satisfies
\[
\frac d{dt}(E(t)^*E(t))
=E(t)^*(X^*+X)E(t)=0.
\]
Right-linearity follows by uniqueness of its linear ODE, since \(X\) commutes with right scalar multiplication. Thus \(E(t)^*E(t)=I\). In the real case its continuous determinant is \(1\); in the special unitary case the determinant ODE in F.1 makes it identically one when the complex trace is zero. This proves that the conditions characterize the full Lie algebras.

A real skew matrix has one independent real entry for each pair \(i<j\), giving \(m(m-1)/2\). A complex skew-Hermitian matrix has \(m\) imaginary diagonal entries and one arbitrary complex entry for each such pair, giving \(m+2\binom m2=m^2\). The purely imaginary trace imposes one independent real linear condition, giving \(m^2-1\). A quaternionic skew-Hermitian matrix has three real parameters on each diagonal and four per pair \(i<j\), giving \(3m+4\binom m2=m(2m+1)\). This proves (Y.7).

Finally a nonzero invariant real subspace contains a unit vector. Sphere transitivity makes it contain every unit vector, hence all their real multiples, so it is the entire representation space. This proves irreducibility in precisely the transitive cases asserted. □

**Theorem Y.3 (the complex and tensor descriptions of \(\mathrm{Sp}(m)\)).** The quaternionic representation in Y.6 is, after a real isometry \(\Phi:\mathbb H^m\to\mathbb C^{2m}\), the compact complex symplectic representation
\[
\mathrm{Sp}(m)\ \cong\
\{B\in\mathrm U(2m):B^T\mathcal J B=\mathcal J\}
\ \subseteq\ \mathrm{SU}(2m),
\qquad
\mathcal J=\operatorname{diag}(J_0,\ldots,J_0),\quad
J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{Y.11}
\]
On \(\mathbb H^m\), put
\[
I_1v=-vi,\quad I_2v=-vj,\quad I_3v=-vk,\qquad
\omega_s(v,w)=g(I_s v,w).
\tag{Y.12}
\]
Then \(I_s^2=-I\), \(I_1I_2=I_3\) and the cyclic analogues hold. The \(\omega_s\) are alternating real two-forms. The common stabilizer of \(g,\omega_1,\omega_2,\omega_3\) in the real general linear group is exactly \(\mathrm{Sp}(m)\).

**Proof.** For one quaternion \(q=z+w j\), set
\(\Phi(q)=(z,-\overline w)^T\); use this coordinate pair for each component. This is a real-linear isometry by (Y.3). For \(c\in\mathbb C\), (Y.4) gives
\(\Phi(qc)=\Phi(q)c\).
The vector \(\Phi(q)\) is the first column of \(\chi(q)\), so
\(\Phi(pq)=\chi(p)\Phi(q)\).
For a quaternionic matrix \(A=(a_{\ell r})\), replace each entry by its \(2\)-by-\(2\) block \(\chi(a_{\ell r})\) to obtain \(\chi_m(A)\). Then
\[
\Phi(Av)=\chi_m(A)\Phi(v),\quad
\chi_m(AB)=\chi_m(A)\chi_m(B),\quad
\chi_m(A^*)=\chi_m(A)^*.
\]
All follow by the entry sums, preserving their order. Thus \(\chi_m\) is injective, and takes \(A^*A=I\) exactly to unitarity of its image.

Right multiplication by \(j\) takes these complex coordinates to \(\mathcal J\overline{\Phi(v)}\), since
\(\Phi((z+w j)j)=(-w,-\overline z)^T=J_0\overline{\Phi(q)}\).
Right-linearity of \(A\) therefore gives
\[
B\mathcal J=\mathcal J\overline B,\qquad B=\chi_m(A).
\tag{Y.13}
\]
For a unitary \(B\), (Y.13) is equivalent to \(B^T\mathcal J B=\mathcal J\). Indeed multiplication of (Y.13) by \(B^*\) on the left gives \(\mathcal J=B^*\mathcal J\overline B\); complex conjugation gives the symplectic equation. Conversely multiply that equation on the left by \(\overline B\), use \(\overline B B^T=I\), and conjugate to recover (Y.13).

Every \(2\)-by-\(2\) block \(C\) satisfying \(CJ_0=J_0\overline C\) is of the form (Y.2): writing \(C=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), the equation says \(c=-\overline b,d=\overline a\). Consequently every \(B\) on the right of (Y.11) equals \(\chi_m(A)\) for a unique quaternionic matrix \(A\). Its unitarity implies \(\chi_m(A^*A)=I\), hence \(A^*A=I\). This proves equality of the groups in (Y.11), not only an inclusion. The correspondence and inverse are linear in real entries, hence smooth.

The determinant of \(B^T\mathcal J B=\mathcal J\) gives \((\det_{\mathbb C}B)^2=1\), since \(\mathcal J\) is invertible. The group is path connected by Y.2, so this determinant is constantly \(1\), its value at the identity. This proves the special-unitary inclusion without a determinant theorem for general complex symplectic groups.

Composition of right multiplications reverses their order. Thus the three minus signs in (Y.12) give
\[
I_1I_2v=(v j)i=-v k=I_3v,
\]
and the remaining identities follow from (Y.1). Each \(I_s\) is orthogonal by the multiplicative norm, and \(I_s^{-1}=-I_s\), so it is skew-adjoint. This proves that \(\omega_s\) is alternating. Every \(A\in\mathrm{Sp}(m)\) preserves \(g\) and commutes with right multiplication, hence preserves all three forms.

Conversely, an invertible real \(A\) preserving \(g\) and \(\omega_s\) satisfies
\[
g(I_sAv,Aw)=g(I_sv,w)=g(AI_sv,Aw).
\]
Surjectivity and nondegeneracy give \(I_sA=AI_s\). Hence \(A\) commutes with right multiplication by \(i,j,k\), and by real linearity with right multiplication by every quaternion. It is a quaternionic matrix in the standard basis. It preserves the whole \(h\), not only its real part: for \(t=1,i,j,k\),
\[
\operatorname{Re}\bigl(h(Av,Aw)t\bigr)
=g(Av,(Aw)t)=g(Av,A(wt))
=g(v,wt)=\operatorname{Re}\bigl(h(v,w)t\bigr).
\]
These four real numbers determine a quaternion, since for \(q=a+bi+cj+dk\) they are \(a,-b,-c,-d\). Therefore \(h(Av,Aw)=h(v,w)\). Testing (Y.8) on standard basis pairs gives \(A^*A=I\), which proves the stabilizer assertion. □

**Theorem Y.4 (the quaternionic product representation and its kernel).** For \(m\ge1\), the formula
\[
\rho(A,q)v=Avq^{-1},
\qquad A\in\mathrm{Sp}(m),\ q\in\mathrm{Sp}(1),\ v\in\mathbb H^m
\tag{Y.14}
\]
defines a smooth orthogonal real representation of \(\mathrm{Sp}(m)\times\mathrm{Sp}(1)\). Its kernel is exactly
\[
N=\{(I_m,1),(-I_m,-1)\}.
\tag{Y.15}
\]
Its image, denoted \(\mathrm{Sp}(m)\mathrm{Sp}(1)\), is a compact connected embedded subgroup of \(\mathrm{SO}(4m)\), isomorphic as a Lie group to
\[
(\mathrm{Sp}(m)\times\mathrm{Sp}(1))/N.
\tag{Y.16}
\]
It has dimension \(m(2m+1)+3\), and its action on the unit sphere is transitive and irreducible.

Restricting \(q\) to the unit complex numbers in \(\operatorname{span}_{\mathbb R}\{1,i\}\) gives \(\mathrm{Sp}(m)\mathrm U(1)\), with the same kernel, dimension \(m(2m+1)+1\), and a compact connected transitive image. This image commutes with \(I_1\) from (Y.12).

**Proof.** Right-linearity of \(A\) and quaternion associativity give
\[
\rho(A,q)\rho(B,r)v
=A(Bv r^{-1})q^{-1}
=ABv(qr)^{-1}=\rho(AB,qr)v.
\]
The identity acts as the identity, so this is a representation. All maps are smooth in real coordinates; on unit quaternions the inverse is conjugation by (Y.3). The matrix \(A\) preserves the norm, as does right multiplication by a unit quaternion, so polarization of the squared real norm proves orthogonality.

If \(\rho(A,q)=I\), then \(A\), as a real operator, is right multiplication by \(q\). But a quaternionic matrix commutes with right multiplication by every scalar. Thus this right-multiplication operator must commute with right multiplication by \(i\) and \(j\). Evaluating these commutation relations on a standard basis vector with entry \(1\) gives \(iq=qi\) and \(jq=qj\). Lemma Y.1 makes \(q\) real. Its norm is one, so \(q=1\) or \(-1\); correspondingly \(A=I_m\) or \(-I_m\). Both pairs do act trivially. This proves (Y.15) from the established scalar algebra.

The domain is compact and path connected by Y.2. Its continuous image is therefore compact, hence closed in the real matrix space, and path connected. A compact subset of a Hausdorff space is closed: for a point outside it, separate that point from each point of the compact set, take finitely many of the latter neighbourhoods, and intersect the corresponding former ones. By [Invariant connections, Theorem A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1), the image is an embedded Lie subgroup. Its orthogonal matrices have positive determinant by connectedness and the value at the identity, so it lies in \(\mathrm{SO}(4m)\).

We justify the smooth quotient assertion too. The two-element kernel \(N\) is a central embedded closed subgroup. [Local tools, Theorem 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) gives a Hausdorff second-countable smooth quotient with local sections and quotient dimension equal to the domain dimension, since \(\operatorname{Lie}(N)=0\). Normality gives the quotient its group law. In local sections it is expressed as \(q(s(u)s(v))\), and inversion as \(q(s(u)^{-1})\), where \(q\) is the quotient map; these formulas prove that both operations are smooth.

The induced map from this quotient to the image is a smooth bijective homomorphism, by its kernel calculation and the local sections. Its differential is injective. Indeed if \((X,a)\) in the Lie algebra of the product has zero derivative under \(\rho\), the exponential identity for Lie homomorphisms proved in F.1 gives
\(\rho(\exp(tX),\exp(ta))=I\) for all \(t\).
The path \((\exp(tX),\exp(ta))\) then lies in the two separated points of \(N\), and must be constant at \((I,1)\). Differentiation gives \(X=a=0\). Since the quotient map has isomorphic differential in this discrete-kernel case, its induced differential is injective as well. [Curvature, Lemma G.1](curvature-and-holonomy-groups.md#lemma-g-1) now proves that the induced bijection is a diffeomorphism. This proves (Y.16), and Y.2 gives its dimension.

The image contains every \(\rho(A,1)=A\), so Y.2 supplies sphere transitivity. The invariant-subspace argument at the end of Y.2 gives real irreducibility. With \(q\) restricted to the unit complex circle, the kernel calculation is unchanged. The compactness, connectedness, quotient and dimension proofs apply with its one-dimensional factor \(\mathrm U(1)\). It still contains \(\mathrm{Sp}(m)\), hence is transitive. Since complex \(q\) commutes with \(i\), right multiplication by \(q^{-1}\) commutes with \(I_1=-R_i\); so does every quaternionic matrix \(A\). This proves the last assertion. □

**Theorem Y.5 (the normalizer of the quaternionic structure).** Let
\(\mathcal Q=\operatorname{span}_{\mathbb R}\{I_1,I_2,I_3\}\)
inside the real endomorphisms of \(\mathbb H^m\). Then
\[
\{A\in\mathrm O(4m):A\mathcal Q A^{-1}=\mathcal Q\}
=\mathrm{Sp}(m)\mathrm{Sp}(1).
\tag{Y.17}
\]
Its conjugation action on \(\mathcal Q\), in the displayed ordered basis, takes values in \(\mathrm{SO}(3)\). All of \(\mathrm{SO}(3)\) is obtained. More specifically, the quaternionic conjugation map
\[
\mathrm{Sp}(1)\longrightarrow\mathrm{SO}(\operatorname{Im}\mathbb H),
\qquad q\longmapsto(u\mapsto quq^{-1})
\tag{Y.18}
\]
is a surjective smooth homomorphism with kernel \(\{1,-1\}\).

**Proof.** Write \(I_u=-R_u\) for \(u\in\operatorname{Im}\mathbb H\). Formula (Y.5), with the order reversal of right multiplication, gives
\[
I_uI_v=-\langle u,v\rangle I+I_{u\times v}.
\tag{Y.19}
\]
The map \(u\mapsto I_u\) is injective, since evaluation on a standard coordinate vector with entry \(1\) recovers \(-u\).

First consider (Y.18). It preserves imaginary quaternions: for unit \(q\),
\(\overline{quq^{-1}}=q\overline u q^{-1}\),
so \(\overline u=-u\) is preserved. Norm multiplicativity proves it is orthogonal. The homomorphism law is associativity; smoothness follows from the real polynomial formulas for multiplication and unit inversion. Connectedness of \(\mathrm{Sp}(1)\) makes its real determinant on \(\operatorname{Im}\mathbb H\) equal to \(1\). Its kernel consists of unit quaternions commuting with \(i,j,k\), hence is exactly \(\{1,-1\}\) by Y.1.

We prove surjectivity instead of assuming a description by rotation angles. The tangent algebra of \(\mathrm{Sp}(1)\) is \(\operatorname{Im}\mathbb H\), by Y.2, and differentiating quaternionic conjugation at the identity gives
\[
a\longmapsto\bigl(u\mapsto au-ua=2a\times u\bigr).
\]
This is injective: if it vanishes on \(i,j\), Y.1 makes \(a\) real, while it is also imaginary, hence zero. Both source and target Lie algebras have real dimension three, by Y.2. Its differential is therefore an isomorphism. The inverse-function theorem, Local tools 1.2, puts an open identity neighbourhood of \(\mathrm{SO}(3)\) in the image. A subgroup containing such a neighbourhood is open, and all its cosets are open. Since \(\mathrm{SO}(3)\) is connected by Y.2, the image is the entire group.

Now suppose \(A\in\mathrm O(4m)\) normalizes \(\mathcal Q\). It induces an invertible real map \(\varphi\) on \(\operatorname{Im}\mathbb H\) characterized by
\[
AI_uA^{-1}=I_{\varphi(u)}.
\]
Conjugating \(I_u^2=-|u|^2I\) gives \(|\varphi(u)|=|u|\); polarization gives preservation of inner products. Conjugating (Y.19) then gives
\(\varphi(u\times v)=\varphi(u)\times\varphi(v)\).
In particular the images of \(i,j,k\) are an orthonormal frame whose third vector is the cross product of the first two. It has positive determinant: the coordinate cross-product formula from (Y.5) gives
\(\det[x,y,z]=\langle x\times y,z\rangle\),
and this determinant is one for that frame. Thus \(\varphi\in\mathrm{SO}(3)\).

Choose \(q\in\mathrm{Sp}(1)\) realizing \(\varphi\) by (Y.18), and put \(B=\rho(I_m,q)\). Direct evaluation gives
\[
BI_uB^{-1}v
=-vquq^{-1}=I_{quq^{-1}}v.
\tag{Y.20}
\]
Thus \(B^{-1}A\) commutes with all three \(I_s\). It is orthogonal, so the stabilizer result in Y.3 puts it in \(\mathrm{Sp}(m)\). A quaternionic matrix commutes with \(B\), which is right scalar multiplication; consequently \(A=\rho(C,q)\) for that matrix \(C\in\mathrm{Sp}(m)\).

Conversely any \(\rho(C,q)\) normalizes \(\mathcal Q\), because \(C\) commutes with all \(I_u\) and (Y.20) describes the conjugation by its second factor. This proves (Y.17), with all its conjugation assertions. □

**Theorem Y.6 (commutants and low-dimensional identifications).** The commutant of \(\mathrm{Sp}(m)\) in \(\operatorname{End}_{\mathbb R}(\mathbb H^m)\) is precisely the space of right scalar multiplications \(R_a:v\mapsto va\), \(a\in\mathbb H\). The commutant of \(\mathrm{Sp}(m)\mathrm{Sp}(1)\) consists only of real scalar multiples of the identity. In particular the latter group fixes no complex structure on its representation space.

The following identifications hold in the displayed real representations:
\[
\mathrm U(1)=\mathrm{SO}(2),\qquad
\mathrm{Sp}(1)\cong\mathrm{SU}(2),\qquad
\mathrm{Sp}(1)\mathrm{Sp}(1)=\mathrm{SO}(4),\qquad
\mathrm{Sp}(1)\mathrm U(1)=\mathrm U(2).
\tag{Y.21}
\]
The complex identifications use \(\Phi\) of Y.3. The equality with \(\mathrm{SO}(4)\) concerns the product's image; its map from \(\mathrm{Sp}(1)\times\mathrm{Sp}(1)\) has the two-element kernel (Y.15).

**Proof.** Let a real-linear \(T\) commute with every element of \(\mathrm{Sp}(m)\). For \(m>1\), that group contains the diagonal sign change which is \(-1\) on coordinate \(\ell\) and \(1\) on the others. Its \(-1\)-eigenspace is exactly that quaternionic coordinate line. Commutation makes \(T\) preserve that line, for every \(\ell\). When \(m=1\) the same conclusion requires no sign changes because the whole space is that line. Thus \(T\) has real-linear diagonal blocks \(T_\ell:\mathbb H\to\mathbb H\).

The group also contains left multiplication by any unit quaternion on a single coordinate, with identity on the other coordinates. Hence each \(T_\ell\) commutes with these left multiplications. Put \(a_\ell=T_\ell(1)\). For nonzero \(t=rq\), where \(r=|t|>0\) and \(|q|=1\), real linearity and commutation give
\[
T_\ell(t)=rT_\ell(q)=rq\,T_\ell(1)=t a_\ell.
\]
The same formula holds at zero. Real permutation matrices belong to \(\mathrm{Sp}(m)\), since their columns are orthonormal also for \(h\). Commuting with the transposition of any two coordinates gives \(a_\ell=a_r\). Thus a single \(a\) works on every coordinate, and \(T=R_a\). Conversely every \(R_a\) commutes with all quaternionic matrices by right-linearity, proving the first commutant assertion.

If \(T=R_a\) also commutes with all \(\rho(I_m,q)=R_{q^{-1}}\), \(q\in\mathrm{Sp}(1)\), then \(a\) commutes with the unit quaternions \(i,j\). By Y.1 it is real. Every real scalar clearly does commute with the product group, proving the second assertion. A fixed complex structure would be an operator \(J\) commuting with the group and satisfying \(J^2=-I\). A real scalar operator cannot satisfy that equation. This proves the stated obstruction; it does not depend on a choice of orthogonal complex coordinates.

For the first equality in (Y.21), multiplication by \(z=a+bi\), \(|z|=1\), on \(\mathbb C\cong\mathbb R^2\) has real matrix
\(\left(\begin{smallmatrix}a&-b\\b&a\end{smallmatrix}\right)\).
The column calculation in X.2 proves that these are exactly all of \(\mathrm{SO}(2)\).

For \(\mathrm{Sp}(1)\), the block description in Y.3 identifies its image with the unitary \(2\)-by-\(2\) matrices satisfying \(B^TJ_0B=J_0\). If \(B=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), direct multiplication gives
\[
B^TJ_0B=(ad-bc)J_0=(\det_{\mathbb C}B)J_0.
\]
Thus that condition is exactly complex determinant one. The image is \(\mathrm{SU}(2)\), and \(\chi\), with its real-linear inverse on the image, is the stated Lie-group isomorphism. It intertwines the real representations by Y.3.

The compact embedded image \(\mathrm{Sp}(1)\mathrm{Sp}(1)\) has dimension \(3+3=6\) by Y.4, and lies in \(\mathrm{SO}(4)\), of dimension \(4\cdot3/2=6\) by Y.2. Its inclusion has injective differential and the dimensions agree. The inverse-function theorem makes its image contain an open identity neighbourhood in \(\mathrm{SO}(4)\). As an open subgroup of this connected group it is the whole group. Its kernel on the product remains exactly (Y.15); no direct-product identification has been made.

Finally \(\mathrm{Sp}(1)\mathrm U(1)\) commutes with right multiplication by \(i\) and preserves the real norm, by Y.4. Under \(\Phi\), right multiplication by \(i\) is ordinary complex scalar multiplication. Hence its matrices are complex-linear and unitary. To verify the latter from real norm preservation, real polarization gives preservation of \(\operatorname{Re}h_{\mathbb C}\), and applying it also to \((v,iw)\) gives preservation of \(-\operatorname{Im}h_{\mathbb C}\); together they give preservation of \(h_{\mathbb C}\). Thus the image lies in \(\mathrm U(2)\). Its dimension is \(3+1=4\), equal to that of \(\mathrm U(2)\). The same open-subgroup argument using Y.2 gives equality. □

## Z. Exceptional real representations

We construct the seven-dimensional representation of the compact group \(G_2\) and the eight-dimensional spin representation of \(\mathrm{Spin}(7)\). Their underlying vector spaces will be the imaginary octonions and all the octonions, respectively. Products of octonions and products of their multiplication operators must be distinguished: the former need not associate, whereas the latter always do.

**Lemma Z.1 (octonions, norm and multiplication operators).** On the real vector space \(\mathbb O=\mathbb H\oplus\mathbb H\), define
\[
(a,b)(c,d)=(ac-\overline d\,b,\ da+b\overline c),
\qquad
\overline{(a,b)}=(\overline a,-b).
\tag{Z.1}
\]
Its identity is \(1=(1,0)\), and its Euclidean squared norm is
\[
| (a,b)|^2=|a|^2+|b|^2.
\]
Conjugation reverses products,
\[
x\overline x=\overline x x=|x|^2\,1,\qquad
|xy|=|x||y|,\qquad
x^2-2\operatorname{Re}(x)x+|x|^2\,1=0,
\tag{Z.2}
\]
where \(\operatorname{Re}(a,b)=\operatorname{Re}a\). Every nonzero left or right multiplication is invertible. The algebra is alternative in the identities
\[
x(xy)=(x^2)y,\qquad (yx)x=y(x^2),\qquad (xy)x=x(yx).
\tag{Z.3}
\]
Its associator \([x,y,z]=(xy)z-x(yz)\) is alternating.

Let \(V=1^\perp=\operatorname{Im}\mathbb O\), with its Euclidean inner product, and let \(L_x(y)=xy\), \(R_x(y)=yx\). Then
\[
L_x^*=L_{\overline x},\qquad R_x^*=R_{\overline x},
\qquad
L_u^2=R_u^2=-|u|^2 I\quad(u\in V).
\tag{Z.4}
\]
In particular,
\[
L_uL_v+L_vL_u=-2\langle u,v\rangle I
\quad(u,v\in V).
\tag{Z.5}
\]

**Proof.** Every computation in a component of (Z.1) takes place in the associative quaternion algebra proved in Y.1. The identity is immediate. If \(x=(a,b)\), \(y=(c,d)\), the conjugate of their product is
\[
(\overline c\,\overline a-\overline b\,d,\ -da-b\overline c).
\]
Substitution of \(\overline y=(\overline c,-d)\) and \(\overline x=(\overline a,-b)\) into (Z.1) gives exactly the same pair. This proves reversal of products. Substitution of \(y=\overline x\), in either order, gives \((|a|^2+|b|^2,0)\). Also \(x+\overline x=2\operatorname{Re}(x)1\); multiplying this identity by \(x\) proves the quadratic identity in (Z.2).

Here is the norm calculation, including the mixed terms. Quaternion norm multiplicativity and the real inner product give
\[
\begin{aligned}
|ac-\overline d\,b|^2
 &=|a|^2|c|^2+|d|^2|b|^2
   -2\operatorname{Re}(ac\overline b\,d),\\
|da+b\overline c|^2
 &=|d|^2|a|^2+|b|^2|c|^2
   +2\operatorname{Re}(dac\overline b).
\end{aligned}
\]
The two mixed real parts agree by the trace identity of Y.1, applied to the quaternion factors \(ac\overline b\) and \(d\). Adding gives
\[
|xy|^2=(|a|^2+|b|^2)(|c|^2+|d|^2).
\]
Positive square roots prove multiplicativity. If \(x\ne0\), the identity \(|xy|=|x||y|\) makes \(L_x\) injective, and the right-hand version makes \(R_x\) injective. On the finite-dimensional real vector space both are invertible. Thus division here means that the equations \(xy=z\) and \(yx=z\) have unique solutions; the existence of a two-sided inverse alone would not have established this for a nonassociative algebra.

For \(u\in V\), we have \(\overline u=-u\). Norm multiplicativity, applied to \((1+tu)y\) for real \(t\), yields
\[
|y+tuy|^2=(1+t^2|u|^2)|y|^2.
\]
Equality of the linear coefficients gives \(\langle y,L_uy\rangle=0\). Apply this to \(y+z\) and subtract the equations for \(y,z\); the result is
\(\langle y,L_uz\rangle=-\langle L_uy,z\rangle\).
Thus \(L_u^*=-L_u\). Polarizing \(|L_uy|^2=|u|^2|y|^2\) gives
\(L_u^*L_u=|u|^2I\), hence \(L_u^2=-|u|^2I\). The same argument with \(y(1+tu)\) proves the two assertions for \(R_u\).

Write \(x=s1+u\), with \(s\in\mathbb R\), \(u\in V\). Then \(L_x=sI+L_u\), so \(L_x^*=sI-L_u=L_{\overline x}\); the right multiplication formula follows identically. Moreover
\[
L_x^2=(s^2-|u|^2)I+2sL_u=L_{x^2}.
\]
This proves left alternativity. The corresponding equation \(R_x^2=R_{x^2}\) proves right alternativity. The associator is trilinear by bilinearity of the product. Left alternativity says \([x,x,z]=0\), whose polarization makes it change sign on exchanging the first two entries. Right alternativity says \([x,y,y]=0\), whose polarization gives the sign change on exchanging the last two. These two exchanges also give the sign change on exchanging the first and third entries. Thus it is alternating, and in particular \([x,y,x]=0\), which is the remaining identity in (Z.3). Finally polarize \(L_u^2=-|u|^2I\) to obtain (Z.5). No reassociation of three arbitrary octonions was used. □

**Lemma Z.2 (the cross product, three-form and automorphisms).** For \(u,v\in V\), define
\[
u\times v=\tfrac12(uv-vu),\qquad
\varphi(u,v,w)=\langle u\times v,w\rangle.
\tag{Z.6}
\]
Then \(u\times v\in V\), \(\varphi\) is an alternating three-form, and
\[
uv=-\langle u,v\rangle\,1+u\times v,\qquad
u\times v\perp u,v,\qquad
|u\times v|^2=|u|^2|v|^2-\langle u,v\rangle^2.
\tag{Z.7}
\]
On \(u^\perp\cap V\), for a unit \(u\), the map \(J_u(v)=u\times v\) is an orthogonal complex structure.

Use the orthonormal basis
\[
\begin{aligned}
e_1&=(i,0),& e_2&=(j,0),&e_3&=(k,0),\\
e_4&=(0,1),& e_5&=(0,i),&e_6&=(0,j),&e_7&=(0,k).
\end{aligned}
\tag{Z.8}
\]
Writing \(e^r\) for its dual covectors and \(e^{rst}=e^r\wedge e^s\wedge e^t\), the three-form is
\[
\varphi=e^{123}+e^{145}-e^{167}
       +e^{246}+e^{257}+e^{347}-e^{356}.
\tag{Z.9}
\]
The group of real algebra automorphisms of \(\mathbb O\), denoted \(G\) for now, is compact and an embedded matrix Lie group. Each automorphism fixes \(1\) and preserves the norm. Restriction to \(V\) identifies it with
\[
G=\{A\in\mathrm O(V):\varphi(Au,Av,Aw)=\varphi(u,v,w)\}.
\tag{Z.10}
\]

**Proof.** Polarizing \(u^2=-|u|^2\,1\) for imaginary \(u\) gives
\(uv+vu=-2\langle u,v\rangle1\).
Conjugation reversal shows \(\overline{uv}=vu\), so the antisymmetric part is imaginary. This proves the first identity in (Z.7). The adjoint identities in Z.1 give
\[
\langle uv,u\rangle
 =\langle v,\overline u\,u\rangle
 =|u|^2\langle v,1\rangle=0,
\qquad
\langle uv,v\rangle
 =\langle u,v\overline v\rangle=0.
\]
The scalar part is orthogonal to \(V\), so these are the stated orthogonality relations for the cross product. The real and imaginary parts of \(uv\) are orthogonal; combine this with norm multiplicativity to prove its squared norm in (Z.7).

Antisymmetry gives the sign change in the first two slots of \(\varphi\). Since \(w\) is imaginary,
\[
\varphi(u,v,w)=\langle uv,w\rangle
=-\langle v,uw\rangle=-\varphi(u,w,v).
\]
These two sign changes make the form alternating. If \(v\perp u\) and \(|u|=1\), then \(J_uv=uv\), which is again imaginary and perpendicular to \(u\). Left alternativity gives \(J_u^2v=u(uv)=-v\), and the norm identity gives \(|J_uv|=|v|\). Polarization proves orthogonality of \(J_u\).

The coordinate calculation for (Z.9) can be read directly from the four component rules
\[
\begin{aligned}
(a,0)(c,0)&=(ac,0),&
(a,0)(0,d)&=(0,da),\\
(0,b)(c,0)&=(0,b\overline c),&
(0,b)(0,d)&=(-\overline d\,b,0).
\end{aligned}
\tag{Z.11}
\]
Together with the quaternion table of Y.1, these give the following seven oriented triples:
\[
(1,2,3),\quad(1,4,5),\quad(1,7,6),\quad
(2,4,6),\quad(2,5,7),\quad(3,4,7),\quad(3,6,5).
\tag{Z.12}
\]
For a listed triple \((r,s,t)\), the products in cyclic order are \(e_re_s=e_t\), \(e_se_t=e_r\), \(e_te_r=e_s\); reversal changes the sign. Also \(e_r^2=-1\). Every unordered pair of distinct indices occurs in exactly one of the triples: their three pairs are all different, and there are \(7\cdot3=21=\binom72\) of them. Thus (Z.11)–(Z.12) specify every product of basis vectors, and there are no other nonzero coefficients of \(\varphi\). Reordering their indices increasingly gives exactly (Z.9). The same table exhibits nonassociativity explicitly: \((e_1e_2)e_4=e_7\), whereas \(e_1(e_2e_4)=-e_7\).

An invertible multiplicative real-linear map \(A\) fixes \(1\): its image \(A1\) acts as an identity on every element in the surjective image of \(A\), so \(A1=1\). It therefore fixes all real scalars. If \(x\) is nonreal, \(1,x\) are linearly independent, as are \(1,Ax\). Apply \(A\) to the quadratic identity in (Z.2), then compare it with that identity for \(Ax\). Independence implies
\(\operatorname{Re}(Ax)=\operatorname{Re}x\) and \(|Ax|^2=|x|^2\). For real \(x\) these conclusions already hold. Polarization gives preservation of the Euclidean inner product, and \(A\) preserves \(V=1^\perp\). Its restriction is faithful because \(A\) is fixed on \(\mathbb R1\).

Every such restriction preserves the cross product and hence \(\varphi\). Conversely, let \(A\in\mathrm O(V)\) preserve \(\varphi\). For all \(u,v,w\in V\),
\[
\langle (Au)\times(Av),Aw\rangle
=\varphi(u,v,w)=\langle A(u\times v),Aw\rangle.
\]
Surjectivity and nondegeneracy imply
\((Au)\times(Av)=A(u\times v)\).
Formula (Z.7) now shows that extending \(A\) by the identity on \(\mathbb R1\) preserves multiplication of imaginary elements. Bilinearity then proves preservation of all products. This establishes (Z.10).

The equations preserving \(\varphi\) need only be checked on the finitely many triples of basis vectors; they are polynomial in the real entries of \(A\). Thus (Z.10) is a closed subgroup of the compact group \(\mathrm O(7)\), so is compact. It is an embedded Lie group by [Invariant connections, Theorem A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). We have not yet assumed its connectedness or its dimension. □

**Theorem Z.3 (the Clifford algebra and its faithful even action).** There is a \(128\)-dimensional real associative algebra \(\mathrm{Cl}_{0,7}\), generated by a copy of \(V\) with relations
\[
uv+vu=-2\langle u,v\rangle\,1.
\tag{Z.13}
\]
Its even subalgebra has dimension \(64\). The assignment \(u\mapsto L_u\) extends to a homomorphism
\[
\Gamma:\mathrm{Cl}_{0,7}\longrightarrow
\operatorname{End}_{\mathbb R}(\mathbb O),
\]
whose restriction
\[
\Gamma:\mathrm{Cl}_{0,7}^{\,0}
\longrightarrow \operatorname{End}_{\mathbb R}(\mathbb O)
\tag{Z.14}
\]
is an isomorphism of real associative algebras. In particular a real endomorphism of \(\mathbb O\) commuting with every \(L_u\), \(u\in V\), is a real scalar.

**Proof.** We construct the algebra by a basis and an explicit multiplication rule. For each subset \(I\subseteq\{1,\ldots,7\}\), introduce one basis symbol \(c_I\). In particular \(c_\varnothing=1\). If \(i_r,j_r\in\{0,1\}\) are the characteristic functions of \(I,J\), set
\[
\epsilon(I,J)=\sum_{r\ge s}i_rj_s\pmod2,\qquad
c_Ic_J=(-1)^{\epsilon(I,J)}c_{I\triangle J},
\tag{Z.15}
\]
and extend multiplication real-bilinearly. The exponent is bilinear in the characteristic vectors over arithmetic modulo two. Consequently
\[
\epsilon(I,J)+\epsilon(I\triangle J,K)
=\epsilon(J,K)+\epsilon(I,J\triangle K)\pmod2.
\]
Both parenthesizations of \(c_Ic_Jc_K\) therefore give the same sign and the same symbol \(c_{I\triangle J\triangle K}\). Bilinearity proves associativity for all elements, and (Z.15) makes \(c_\varnothing\) the identity.

Put \(c_r=c_{\{r\}}\). The formula gives \(c_r^2=-1\) and \(c_rc_s=-c_sc_r\) for \(r\ne s\). For \(I=\{i_1<\cdots<i_k\}\) it gives
\(c_I=c_{i_1}\cdots c_{i_k}\).
Thus the map \(e_r\mapsto c_r\) identifies \(V\) with a generating subspace satisfying (Z.13). It has the usual universal property: in any associative unital real algebra with elements \(C_r\) satisfying these square and anticommutation rules, moving factors into increasing order, and eliminating each repeated pair with \(C_r^2=-1\), gives exactly the sign in (Z.15). Hence \(c_I\mapsto C_{i_1}\cdots C_{i_k}\) defines a unique algebra homomorphism. This proves both existence and the asserted presentation. There are \(2^7=128\) subsets. Parity of their cardinalities is additive under symmetric difference, so the span of the \(64\) even subsets is the even subalgebra.

By (Z.5), the operators \(L_{e_r}\) obey precisely these relations. The universal property defines \(\Gamma\). For increasing \(I\), write
\[
T_I=L_{e_{i_1}}\cdots L_{e_{i_k}},\qquad T_\varnothing=I.
\]
Each factor is orthogonal by Z.1, so every \(T_I\) is orthogonal. If \(K\) is a nonempty even subset, choose \(j\in K\). Moving \(L_{e_j}\) through the other \(|K|-1\) factors shows that it anticommutes with \(T_K\). Since it is invertible, conjugation by it sends \(T_K\) to \(-T_K\). Trace is invariant under conjugation by the trace identity of F.1, so
\(\operatorname{tr}T_K=0\).

For even \(I,J\), the same relations give
\(T_I^*T_J=\pm T_{I\triangle J}\) if \(I\ne J\). If \(I=J\), orthogonality gives \(T_I^*T_I=I\). Therefore
\[
\operatorname{tr}(T_I^*T_J)=
\begin{cases}8,&I=J,\\0,&I\ne J.\end{cases}
\tag{Z.16}
\]
Taking this trace pairing with each \(T_J\) proves that the \(64\) even operators are linearly independent. The real endomorphisms of an eight-dimensional space have dimension \(8^2=64\), so these operators form a basis. This proves (Z.14).

An operator commuting with all \(L_u\) commutes with all even products, and hence with every real endomorphism by that basis. In a real basis, commuting with the coordinate projections forces the operator to be diagonal; commuting with every map taking one basis vector to another forces all its diagonal entries to agree. It is a real scalar, as asserted. □

**Theorem Z.4 (the compact spin group and its double cover).** Define \(\mathrm{Spin}(7)\) inside the units of \(\mathrm{Cl}_{0,7}^{\,0}\) to consist of all products of an even number of unit vectors in \(V\), including the empty product. Under the faithful representation (Z.14), its image \(H\) is a compact connected embedded subgroup of \(\mathrm{SO}(\mathbb O)\), of dimension \(21\). Conjugation on the multiplication operators defines a smooth surjective homomorphism
\[
\pi:H\longrightarrow\mathrm{SO}(V),\qquad
hL_wh^{-1}=L_{\pi(h)w}.
\tag{Z.17}
\]
Its kernel is \(\{I,-I\}\), and it is a smooth double covering. The Lie algebra of \(H\) has real basis
\[
B_{rs}=L_{e_r}L_{e_s},\qquad 1\le r<s\le7,
\tag{Z.18}
\]
and
\[
d\pi(B_{rs})w
=2\bigl(\langle e_r,w\rangle e_s-\langle e_s,w\rangle e_r\bigr).
\tag{Z.19}
\]
The faithful action of \(H\) on \(\mathbb O\cong\mathbb R^8\) is the spin representation considered here.

**Proof.** A unit vector \(u\) in the Clifford algebra has inverse \(-u\), since \(u^2=-1\). Products of even length are closed under products and inverses, so the definition gives a group. It contains \(-1=uu\). Its image \(H\) consists exactly of the even operator products \(L_{u_1}\cdots L_{u_{2r}}\); injectivity of (Z.14) identifies the abstract group with this image.

For unit \(u\), relation (Z.5) gives, as an identity of associative operators,
\[
L_uL_wL_u^{-1}
=L_{\,2\langle u,w\rangle u-w}.
\tag{Z.20}
\]
The orthogonal map on the subscript is \(-r_u\), where
\[
r_u(w)=w-2\langle u,w\rangle u
\]
is reflection in \(u^\perp\). Its determinant is \(-1\), because it sends \(u\) to \(-u\) and fixes the perpendicular space. For an even word, the minus signs in (Z.20) cancel, giving the product of its even number of reflections. This lies in \(\mathrm{SO}(V)\). Since \(w\mapsto L_w\) is injective (evaluate at \(1\)), conjugation defines \(\pi\) uniquely, independently of the chosen word. It is a homomorphism. Its coefficients are smooth functions of the entries of \(h,h^{-1}\): for example the \(e_i\)-component of \(\pi(h)e_j\) is
\(\langle(hL_{e_j}h^{-1})1,e_i\rangle\).

We supply the reflection argument for surjectivity and a word bound. Given an orthogonal \(A\) on \(\mathbb R^n\), suppose its first \(k-1\) standard basis vectors have already been fixed. If \(Ae_k=e_k\), no change is needed. Otherwise reflection in the hyperplane perpendicular to
\[
a=\frac{Ae_k-e_k}{|Ae_k-e_k|}
\]
sends \(Ae_k\) to \(e_k\). Indeed
\[
|Ae_k-e_k|^2=2(1-\langle Ae_k,e_k\rangle),
\]
and substitution into the reflection formula gives that conclusion. The vector \(a\) is perpendicular to the first \(k-1\) basis vectors, so this reflection preserves the earlier fixes. Induction uses at most \(n\) reflections and ends at the identity. Reversing the sequence expresses \(A\) as their product. When \(\det A=1\), the number of reflections is even. For \(n=7\) it is consequently at most six. Replacing each reflection in such an even word by its \(L_u\) gives a preimage under \(\pi\). This proves surjectivity and the word bound.

If \(\pi(h)=I\), then \(h\) commutes with all \(L_w\), so Z.3 makes it a real scalar. Each \(L_u\) for unit \(u\) is orthogonal by Z.1, and hence so is \(h\); its scalar is therefore \(1\) or \(-1\). Both occur, proving the kernel assertion.

For any \(h\in H\), choose a lift \(k\) of \(\pi(h)\) of even length at most six, as just proved. Then \(k^{-1}h=\pm I\). Since \(-I=L_uL_u\), every \(h\) has a word of even length at most eight. Thus \(H\) is the union of the continuous images of
\[
\{*\},\quad (S^6)^2,\quad(S^6)^4,\quad(S^6)^6,\quad(S^6)^8
\]
under the corresponding operator products. These spaces are compact by Local tools 0.1, so the finite union is compact. Each sphere is path connected by the normalized-segment argument in Y.2; their finite products are path connected by taking paths in each coordinate. Each word image contains \(I\), by choosing successive pairs \(u,-u\). The union is therefore path connected. Its orthogonal matrices have determinant \(1\) by continuity from the identity.

A compact matrix subgroup is closed, so [Invariant connections, Theorem A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1) gives \(H\) its embedded Lie-group structure. The differential of \(\pi\) is injective: if \(X\in\operatorname{Lie}(H)\) satisfies \(d\pi(X)=0\), the exponential identity for smooth Lie homomorphisms in F.1 gives \(\pi(\exp(tX))=I\). The continuous path \(\exp(tX)\) lies in the separated two-point kernel, starts at \(I\), and hence is constant. Differentiating at zero gives \(X=0\).

For orthogonal unit \(u,v\), the curve
\[
t\longmapsto
L_u L_{\,(-u+tv)/\sqrt{1+t^2}}
=\frac{I+tL_uL_v}{\sqrt{1+t^2}}
\tag{Z.21}
\]
lies in \(H\), starts at \(I\), and has derivative \(L_uL_v\). Thus the operators in (Z.18) belong to its Lie algebra. Relation (Z.5) computes their commutators with \(L_w\):
\[
[L_uL_v,L_w]
=2\langle u,w\rangle L_v-2\langle v,w\rangle L_u
\quad(u\perp v).
\]
This proves (Z.19). Those \(21\) images are a basis of the real skew matrices on \(V\), whose dimension and tangent description were proved in Y.2. The injective differential is therefore an isomorphism, the \(B_{rs}\) form a basis, and \(\dim H=21\).

Finally the inverse-function theorem, Local tools 1.2, gives an identity neighbourhood \(U\subset H\) on which \(\pi\) is a diffeomorphism onto an open neighbourhood \(W\subset\mathrm{SO}(V)\). Shrink \(U\) so that \(U\cap(-U)=\varnothing\). Every preimage of a point of \(W\) is the unique representative in \(U\) or its negative, by the kernel calculation. Hence
\(\pi^{-1}(W)=U\sqcup(-U)\), with both restrictions diffeomorphisms. Translation proves the same near every point of the target. This is exactly a smooth double covering. □

**Theorem Z.5 (the spin sphere and its stabilizer).** The group \(H\) acts transitively on the unit sphere \(S^7\subset\mathbb O\) and irreducibly on the real space \(\mathbb O\). Its stabilizer
\[
K=\{h\in H:h1=1\}
\tag{Z.22}
\]
is a compact embedded Lie group of dimension \(14\), and every element of \(K\) is an octonion algebra automorphism. Its Lie algebra is
\[
\operatorname{Lie}(K)
=\{X\in\operatorname{Lie}(H):X1=0\}.
\tag{Z.23}
\]

**Proof.** Let \(q=s1+w\) have norm one, where \(w\in V\). Choose a unit \(u\in V\) perpendicular to \(w\), which is possible in the seven-dimensional space also when \(w=0\). Put \(v=-uq\). The expression
\[
v=-su-uw
\]
is imaginary: \(u,w\) are perpendicular, so (Z.7) makes \(uw\) imaginary. Also \(|v|=1\) by norm composition. Left alternativity gives
\[
(L_uL_v)1=uv=-u(uq)=q.
\]
Thus a word of length two sends \(1\) to every point of the unit sphere. Products and inverses then give sphere transitivity. A nonzero invariant real subspace contains a unit vector and hence the whole sphere, proving irreducibility as in Y.2.

The stabilizer is a closed subgroup of \(H\), hence compact and embedded by the same closed-subgroup theorem. Differentiating \(h(t)1=1\) gives \(X1=0\). Conversely, for \(X\in\operatorname{Lie}(H)\) with \(X1=0\), uniqueness of the linear ODE gives \(\exp(tX)1=1\); thus \(X\) is tangent to \(K\). This proves (Z.23).

The derivative at the identity of \(h\mapsto h1\) is \(X\mapsto X1\). It maps into \(V=T_1S^7\). It is surjective: the operators \(L_{e_r}L_{e_s}\) belong to \(\operatorname{Lie}(H)\), and the products \(e_re_s\) in (Z.12) span \(V\). Explicitly the seven pairs
\[
(2,3),\ (3,1),\ (1,2),\ (5,1),\ (1,4),\ (2,4),\ (2,5)
\]
give \(e_1,e_2,e_3,e_4,e_5,e_6,e_7\), respectively. Equation (Z.23) and rank-nullity therefore give
\(\dim K=21-7=14\).

For \(h\in K\), equation (Z.17), evaluated on \(1\), gives
\[
hu=hL_u1=L_{\pi(h)u}h1=\pi(h)u
\quad(u\in V).
\]
For \(x\in\mathbb O\) the same operator identity gives
\[
h(ux)=hL_ux=L_{\pi(h)u}hx=(hu)(hx).
\]
Write an arbitrary \(y\in\mathbb O\) as \(s1+u\). Real linearity and \(h1=1\) then imply \(h(yx)=(hy)(hx)\). Thus \(K\subseteq G\), with \(G\) as in Z.2. □

**Theorem Z.6 (the unit-imaginary stabilizer).** Let \(G=\operatorname{Aut}_{\mathbb R}(\mathbb O)\) and fix \(u=e_1\). Its stabilizer \(G_u\), acting on
\[
W=u^\perp\cap V,\qquad Jv=u\times v,
\]
is exactly \(\mathrm{SU}(3)\) in a complex three-dimensional orthonormal coordinate system. In particular \(G_u\) is connected and has real dimension \(8\).

**Proof.** Use the following real orthonormal basis of \(W\):
\[
\begin{array}{lll}
x_1=e_2,&x_2=e_4,&x_3=e_6,\\
y_1=e_3,&y_2=e_5,&y_3=-e_7.
\end{array}
\tag{Z.24}
\]
The multiplication table (Z.12) gives \(Jx_r=y_r\) and \(Jy_r=-x_r\). Regard \(J\) as multiplication by \(i\). If \(x^r,y^r\) are the real dual covectors, the complex coordinates are
\(\zeta^r=x^r+i y^r\). Put
\[
\omega=\sum_{r=1}^3x^r\wedge y^r,\qquad
\Omega=\zeta^1\wedge\zeta^2\wedge\zeta^3.
\]
Extend these forms to vanish whenever one slot is \(u\). Formula (Z.9), expanded in (Z.24), is exactly
\[
\varphi=u^*\wedge\omega+\operatorname{Re}\Omega,
\qquad u^*(v)=\langle u,v\rangle.
\tag{Z.25}
\]
Indeed \(u^*\wedge\omega\) gives \(e^{123}+e^{145}-e^{167}\); the four terms of \(\operatorname{Re}\Omega\) give \(e^{246}+e^{257}+e^{347}-e^{356}\). Thus this decomposition has been checked with its signs.

An element \(A\in G_u\) preserves the metric, \(u\) and the cross product by Z.2. It preserves \(W\) and commutes with \(J\). Hence its restriction is complex-linear and unitary in the coordinates \(\zeta^r\). One can check unitarity directly: the standard complex Hermitian form has real part the given metric, and imaginary part \(\langle Jv,w\rangle\); both are preserved.

For a complex-linear \(B\) on \(W\), the alternating determinant expansion gives
\(B^*\Omega=(\det_{\mathbb C}B)\Omega\).
This is the determinant polynomial of F.1 evaluated on three columns. Since \(A\) preserves \(\varphi\) and \(W\), it preserves \(\operatorname{Re}\Omega\). Write \(d=\det_{\mathbb C}(A|_W)\). Evaluation on \((x_1,x_2,x_3)\) gives \(\operatorname{Re}d=1\); evaluation on \((y_1,x_2,x_3)\), on which \(\Omega=i\), gives \(\operatorname{Im}d=0\). Therefore \(d=1\), and \(A|_W\in\mathrm{SU}(3)\).

Conversely every \(B\in\mathrm{SU}(3)\) preserves the real metric, \(J\), \(\omega\), and \(\Omega\). Extend it to \(V\) by fixing \(u\). Equation (Z.25) shows that this extension preserves \(\varphi\), so Z.2 extends it further by fixing \(1\) to an octonion automorphism. These restriction and extension operations are mutually inverse, and linear in their real matrix entries; they give a Lie-group isomorphism \(G_u\cong\mathrm{SU}(3)\). Connectedness and dimension \(3^2-1=8\) now follow from the full classical-group proof in Y.2. □

**Theorem Z.7 (the compact \(G_2\) representation and the two sphere quotients).** The full automorphism group \(G\) of \(\mathbb O\) is connected and equals the stabilizer \(K\) of \(1\) in the spin representation of \(H=\mathrm{Spin}(7)\). This is the compact octonion group \(G_2\). Its restriction to \(V\cong\mathbb R^7\) is a faithful irreducible representation by special orthogonal matrices, transitive on \(S^6\), and \(\dim G_2=14\). There are diffeomorphisms
\[
G_2/\mathrm{SU}(3)\ \cong\ S^6,\qquad
\mathrm{Spin}(7)/G_2\ \cong\ S^7,
\tag{Z.26}
\]
given by the respective orbit maps. Its Lie algebra consists exactly of the real derivations of \(\mathbb O\):
\[
\mathfrak g_2
=\{D\in\operatorname{End}_{\mathbb R}(\mathbb O):
D(xy)=(Dx)y+x(Dy)\text{ for all }x,y\}.
\tag{Z.27}
\]
Every such derivation annihilates \(1\) and is skew-adjoint.

**Proof.** We first prove transitivity using operators whose values and derivatives are explicit. Let \(K^0\) be the identity component of the compact Lie group \(K\) from Z.5. Connected coordinate balls show that the components of a manifold are open and path connected: each path component is open, and a connected component cannot be partitioned into more than one such open set. A connected component is also closed, since the closure of a connected set is connected. In a topological group, products and inverses of paths from the identity are again paths from the identity, so \(K^0\) is a subgroup. It is consequently a compact open Lie subgroup of \(K\), with the same Lie algebra.

Fix any unit \(u\in V\) and any unit \(w\in V\) perpendicular to it. Put \(t=uw\). By Z.1–Z.2, \(t\) is a unit imaginary octonion perpendicular to \(u,w\), and \(ut=-w\). Choose a unit
\[
a\perp\operatorname{span}_{\mathbb R}\{1,u,w,t\}
\quad\text{in }\mathbb O,
\qquad b=-at.
\]
There is such an \(a\), because the indicated span has dimension at most four in the eight-dimensional space. It is imaginary. Since \(a\perp t\), formula (Z.7) makes \(b\) imaginary, and norm composition gives \(|b|=1\). The adjoint identities of Z.1 and \(ut=-w\) give
\[
\langle b,u\rangle
=\langle a,ut\rangle
=-\langle a,w\rangle=0.
\]
Also
\[
\langle a,b\rangle
=-\langle L_a1,L_at\rangle
=-\langle1,t\rangle=0.
\]
Thus \(a,b\) are orthogonal unit vectors in \(u^\perp\cap V\), and left alternativity gives \(ab=-a(at)=t\).

The curve construction in Z.4 shows that both \(L_uL_w\) and \(L_aL_b\) belong to \(\operatorname{Lie}(H)\). Set
\[
B=L_uL_w-L_aL_b.
\tag{Z.28}
\]
Then \(B1=uw-ab=0\), so Z.5 places \(B\) in \(\operatorname{Lie}(K)=\operatorname{Lie}(K^0)\). For elements of \(K\), restriction to \(V\) equals \(\pi\), as proved in Z.5. Differentiating this equality and using (Z.19) therefore gives
\[
Bu=d\pi(B)u=2w,
\tag{Z.29}
\]
because \(a,b,w\) are perpendicular to \(u\).

Allowing \(w\) to range over an orthonormal basis of \(u^\perp\cap V\) gives six elements of \(\operatorname{Lie}(K^0)\) whose infinitesimal action at \(u\) spans \(T_uS^6\). For these \(B_1,\ldots,B_6\), the map
\[
(s_1,\ldots,s_6)\longmapsto
\exp(s_1B_1)\cdots\exp(s_6B_6)u
\]
has invertible differential at zero in a sphere chart. The inverse-function theorem of Local tools 1.2 gives an open neighbourhood of \(u\) in its \(K^0\)-orbit. Translation shows that this orbit is open at every one of its points. It is also closed, as the continuous image of compact \(K^0\) in the Hausdorff sphere. The sphere \(S^6\) is connected by the normalized-segment argument in Y.2. Its nonempty open and closed orbit is therefore all of \(S^6\).

We now show that there are no further components of \(G\). By Z.5, \(K^0\subseteq K\subseteq G\). At \(u=e_1\), the infinitesimal action of \(\operatorname{Lie}(G)\) has rank six, because it contains the just-constructed directions and its values are tangent to \(S^6\). Its kernel is \(\operatorname{Lie}(G_u)\): differentiating the condition of fixing \(u\) gives one inclusion, and if \(Xu=0\), the linear exponential satisfies \(\exp(tX)u=u\), giving the other. By Z.6 that kernel has dimension eight. Rank-nullity proves
\[
\dim G=6+8=14=\dim K^0.
\]
The inclusion \(K^0\to G\) has injective differential between spaces of this same dimension. The inverse-function theorem and translation make \(K^0\) an open subgroup of \(G\); its other cosets are open as well.

The stabilizer \(G_u\cong\mathrm{SU}(3)\) is connected and contains the identity. It must lie in the open and closed subgroup \(K^0\). Given any \(g\in G\), transitivity supplies \(k\in K^0\) with \(ku=gu\). Then \(k^{-1}g\in G_u\subseteq K^0\), so \(g\in K^0\). This proves
\[
G=K^0=K.
\tag{Z.30}
\]
In particular the full automorphism group is connected, has dimension fourteen, and is the full spin stabilizer, not merely its identity component.

Its restriction to \(V\) was proved faithful and orthogonal in Z.2. Connectedness makes its determinant \(1\), so it lies in \(\mathrm{SO}(7)\). The established sphere transitivity implies real irreducibility by the invariant-subspace argument of Y.2.

For (Z.26), the stabilizers are closed and have already been identified exactly. [Local tools, Theorem 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) supplies their smooth quotient manifolds, local sections and quotient submersions. The orbit maps on the quotients are well-defined smooth bijections by transitivity and the stabilizer calculations. At the identity cosets, their differentials are the infinitesimal action modulo its kernel; they are isomorphisms, with dimensions \(14-8=6\) and \(21-14=7\). Equivariance proves the same at every coset. The inverse-function theorem therefore makes each orbit map a local diffeomorphism. A bijective local diffeomorphism has smooth inverse by its local inverse charts, proving both asserted diffeomorphisms.

Finally differentiating \(h(xy)=(hx)(hy)\) along a curve of automorphisms gives the derivation identity. Conversely let \(D\) satisfy that identity. Substituting \(x=y=1\) gives \(D1=2D1\), hence \(D1=0\). Let \(E(t)=\exp(tD)\), the real linear exponential from Local tools 2.3. For fixed \(x,y\), bilinearity and the derivation identity give
\[
\frac d{dt}\bigl((E(t)x)(E(t)y)\bigr)
=D\bigl((E(t)x)(E(t)y)\bigr).
\]
At zero this product equals \(xy\). Uniqueness for the linear ODE in Local tools 2.1 gives
\((E(t)x)(E(t)y)=E(t)(xy)\).
The exponential is invertible and fixes \(1\), so it belongs to \(G\); differentiating at zero places \(D\) in \(\operatorname{Lie}(G)\). Every automorphism is orthogonal by Z.2, so differentiation also gives \(D^*+D=0\). This proves (Z.27) and the remaining claims. □

## AA. Eliminating the quaternionic circle extension

Sphere transitivity by itself does not guarantee that a representation can be a Riemannian holonomy representation. We now exclude the circle extension from Y.4 in quaternionic dimension at least two.

**Lemma AA.1 (a conformally symplectic symmetric product).** Let \(W\) be a complex vector space of dimension \(2m\ge4\), with a nondegenerate alternating complex-bilinear form \(\Omega\). Suppose \(x\mapsto A_x\) is complex-linear, \(A_xz=A_zx\), and
\[
\Omega(A_xz,w)+\Omega(z,A_xw)=\lambda(x)\Omega(z,w)
\tag{AA.1}
\]
for a complex-linear functional \(\lambda\). Then \(\lambda=0\). The trilinear form
\(T(x,z,w)=\Omega(A_xz,w)\) is completely symmetric. Conversely every completely symmetric complex trilinear form determines a unique such family with \(\lambda=0\).

**Proof.** Symmetry of the product makes \(T\) symmetric in its first two entries. Since \(\Omega\) is alternating, (AA.1) reads
\[
T(x,z,w)-T(x,w,z)=\lambda(x)\Omega(z,w).
\]
Add the three equations obtained by cyclically permuting \(x,z,w\). Each term on the left cancels another by the first-two-entry symmetry. Hence
\[
\lambda(x)\Omega(z,w)+\lambda(z)\Omega(w,x)
 +\lambda(w)\Omega(x,z)=0.
\tag{AA.2}
\]
If \(\lambda\ne0\), choose \(x\) with \(\lambda(x)=1\), and let \(L=\ker\lambda\), of dimension \(2m-1\). Substituting \(z,w\in L\) in (AA.2) gives \(\Omega|_{L\times L}=0\). Nondegeneracy makes the map \(v\mapsto\Omega(v,\cdot)\) an isomorphism \(W\to W^*\), so
\[
L^\Omega=\{v:\Omega(v,L)=0\}
\]
has dimension one: it corresponds to the one-dimensional space of functionals vanishing on the hyperplane \(L\). The asserted vanishing would give \(L\subseteq L^\Omega\), contradicting \(2m-1\ge3\). Thus \(\lambda=0\). Equation (AA.1) now makes \(T\) symmetric in its last two entries as well, and the two adjacent transpositions generate all permutations of three entries.

Conversely nondegeneracy gives a unique vector \(A_xz\) for the functional \(w\mapsto T(x,z,w)\). The inverse of \(W\to W^*\) is linear, so these vectors are bilinear in \(x,z\). Symmetry gives \(A_xz=A_zx\), and symmetry of the last two entries gives (AA.1) with zero right-hand side. This proves both existence and uniqueness. □

**Theorem AA.2 (the circle factor cannot be generated by Riemannian curvature).** On \(\mathbb H^m\), \(m\ge2\), put
\[
\mathfrak k=\mathfrak{sp}(m)\oplus\mathbb RI,
\qquad I(v)=vi.
\]
Every algebraic curvature tensor taking values in \(\mathfrak k\) takes values in \(\mathfrak{sp}(m)\). Consequently, if a Riemannian restricted holonomy group is contained in the representation \(\mathrm{Sp}(m)\mathrm U(1)\) of Y.4, it is already contained in \(\mathrm{Sp}(m)\). In particular it cannot equal \(\mathrm{Sp}(m)\mathrm U(1)\).

**Proof.** Let \(V=\mathbb H^m\) and extend its real metric, \(I\), and a tensor \(R\) complex-bilinearly to \(V_{\mathbb C}\). The two eigenspaces of \(I\) are
\[
W=\{v-iIv:v\in V\},\qquad
\overline W=\{v+iIv:v\in V\}.
\]
They have eigenvalues \(i,-i\), respectively. The projections \((1\mp iI)/2\) show that their sum is direct and is all of \(V_{\mathbb C}\). Orthogonality of \(I\) gives \(g_{\mathbb C}|_{W\times W}=g_{\mathbb C}|_{\overline W\times\overline W}=0\). The pairing between \(W\) and \(\overline W\) is nondegenerate: a vector in either space annihilating the other annihilates their direct sum, and is therefore zero.

Every element of \(\mathfrak k_{\mathbb C}\) commutes with \(I\), so preserves both eigenspaces. Apply Bianchi to \(x,z\in W\), \(\eta\in\overline W\):
\[
R(x,z)\eta+R(z,\eta)x+R(\eta,x)z=0.
\]
The first term is in \(\overline W\), and the other two are in \(W\). Thus \(R(x,z)\) vanishes on \(\overline W\). Its metric skew-adjointness then makes it vanish on \(W\) too, using the nondegenerate pairing just established. We have proved \(R(W,W)=0\); interchanging the eigenspaces proves \(R(\overline W,\overline W)=0\).

For fixed \(\eta\in\overline W\), set \(A_x=R(x,\eta)|_W\). The same Bianchi equation now gives \(A_xz=A_zx\). The complex-linear identification \(v\mapsto v-iIv\) from \((V,I)\) to \(W\) carries the nondegenerate complex symplectic form of Y.3 to a form \(\Omega\) on \(W\). Elements of \(\mathfrak{sp}(m)\), and hence their complex span, preserve this form infinitesimally. The operator \(I|_W=i\,\mathrm{Id}\) instead satisfies
\[
\Omega(Iz,w)+\Omega(z,Iw)=2i\Omega(z,w).
\]
The direct sum defining \(\mathfrak k\) follows also from the injective differential of the product action in Y.4. If the coefficient of \(I\) in \(R(x,\eta)\) is \(t(x,\eta)\), the family \(A_x\) satisfies AA.1 with \(\lambda(x)=2i\,t(x,\eta)\). Lemma AA.1 applies because \(\dim_{\mathbb C}W=2m\ge4\). It gives \(t(x,\eta)=0\). The pure eigenspace pairs were already zero, so complex bilinearity proves that the \(I\)-coefficient of every curvature value vanishes. In particular every real value lies in \(\mathfrak{sp}(m)\).

For the geometric conclusion fix a tangent frame in which the actual restricted holonomy algebra \(\mathfrak h\) lies in \(\mathfrak k\). The complete curvature-span theorem in [Curvature and holonomy groups, Theorem G.3](curvature-and-holonomy-groups.md#theorem-g-3) identifies \(\mathfrak h\) with the span of all curvature values transported to this frame. Each transported tensor is metric, has pair symmetry and Bianchi, and takes values in \(\mathfrak h\subseteq\mathfrak k\). The algebraic conclusion therefore puts that entire span in \(\mathfrak{sp}(m)\).

The restricted holonomy group is connected, as proved in [Curvature and holonomy groups, Theorem C.5](curvature-and-holonomy-groups.md#theorem-c-5). The exponential and connected-generation argument of F.1 shows that a connected matrix Lie group with Lie algebra contained in \(\mathfrak{sp}(m)\) is contained in \(\mathrm{Sp}(m)\): its identity exponential neighbourhood lies in that closed group, and the subgroup generated by the neighbourhood is open and closed in the connected group. This proves the assertion. The dimension hypothesis is essential here; Y.6 identifies the quaternionic one-dimensional circle extension with \(\mathrm U(2)\). □

## AB. The sixteen-dimensional spin action and its curvature

We construct one more sphere-transitive representation and prove that it cannot be the restricted holonomy representation of a Riemannian metric with nonparallel curvature. Write \(e_0=1,e_1,\ldots,e_7\) for the octonion basis of Z.2.

**Theorem AB.1 (the real spin representation in dimension sixteen).** On \(S=\mathbb O\oplus\mathbb O\), define nine operators
\[
P_a=\begin{pmatrix}0&L_{e_a}\\L_{\bar e_a}&0\end{pmatrix}
\quad(0\le a\le7),\qquad
P_8=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{AB.1}
\]
They are symmetric orthogonal involutions and satisfy \(P_aP_b=-P_bP_a\) for \(a\ne b\). For \(v=(v_0,\ldots,v_8)\in\mathbb R^9\), set \(P(v)=\sum_a v_aP_a\). The group
\[
H=\{P(v_1)\cdots P(v_{2r}):|v_j|=1,\ r\ge0\}
\tag{AB.2}
\]
is a compact connected subgroup of \(\mathrm{SO}(S)\). It is the positive-Clifford model of \(\mathrm{Spin}(9)\), with a two-sheeted covering
\[
\pi:H\longrightarrow\mathrm{SO}(9),\qquad
hP(v)h^{-1}=P(\pi(h)v),\qquad\ker\pi=\{1,-1\}.
\tag{AB.3}
\]
Its Lie algebra has the orthogonal basis
\[
B_{ab}=P_aP_b\quad(0\le a<b\le8),
\qquad
\operatorname{tr}(B_{ab}^{T}B_{cd})=16\,\delta_{(a,b),(c,d)}.
\tag{AB.4}
\]
In particular \(\dim H=36\). Its faithful action on \(S\) is irreducible and transitive on \(S^{15}\).

**Proof.** By Z.1, \(L_x^*=L_{\bar x}\) and \(L_xL_{\bar x}=L_{\bar x}L_x=|x|^2\mathrm{Id}\). Block multiplication gives symmetry of (AB.1), and
\[
P(v)^2=|v|^2\mathrm{Id}.
\tag{AB.5}
\]
Indeed the first eight coordinates give \(L_x,L_{\bar x}\), while the ninth contributes opposite real scalars on the diagonal, making the off-diagonal terms cancel. Polarizing (AB.5) gives all the stated Clifford relations.

For an explicit algebraic model take one basis symbol \(c_A\) for each subset \(A\subseteq\{0,\ldots,8\}\), and multiply by
\[
c_Ac_D=(-1)^{\sum_{r>s}1_A(r)1_D(s)}c_{A\triangle D}.
\tag{AB.6}
\]
The exponent is bilinear modulo two in the two indicator vectors. Expanding it verifies the associative law, exactly as in Z.3, and \(c_\varnothing\) is the identity. The singleton generators square to \(1\) and anticommute. Reordering a word in these generators proves that any other nine operators satisfying these relations determine a unique homomorphism from this algebra. This is the real positive Clifford algebra; its even subalgebra has the \(256\) symbols with even cardinality as a basis.

Send \(c_a\) to \(P_a\). For an even subset \(A\), denote its increasing matrix product by \(P_A\). Each is orthogonal. If \(A\) is nonempty and even, conjugation by \(P_j\), \(j\in A\), changes \(P_A\) to \(-P_A\); its trace is therefore zero. For different even subsets \(A,D\), the matrix \(P_A^TP_D\) is a signed product for the nonempty even subset \(A\triangle D\), so it has trace zero. For \(A=D\), the trace is \(16\). The \(256\) even products are thus linearly independent in the \(256\)-dimensional space \(\operatorname{End}_{\mathbb R}(S)\); they give an algebra isomorphism from the even Clifford algebra to this full matrix algebra. In particular the action of its subgroup (AB.2) is faithful. Every matrix commuting with all \(P_a\) is scalar, since it commutes with all even products and hence every matrix; the matrix-unit proof of this last assertion was given in Z.3.

For unit \(u\), the Clifford relations give
\[
P(u)P(v)P(u)^{-1}=P(2\langle u,v\rangle u-v).
\tag{AB.7}
\]
The linear map on the right is the negative of reflection in \(u^\perp\). Even products therefore define the homomorphism \(\pi\) into \(\mathrm{SO}(9)\). It is onto: the basis-fixing reflection algorithm proved in Z.4 works in dimension nine, fixes one further basis vector at each step, and uses at most nine reflections. An element of determinant one uses an even number, hence at most eight. Taking the corresponding even product in (AB.7) gives a lift. The kernel commutes with all \(P_a\) and is scalar orthogonal, so is contained in \(\{\pm1\}\). Both occur, since \((P_0P_1)^2=-1\).

Every element of \(H\) differs by a sign from a lift with at most eight unit factors. The expression for \(-1\) just given uses four factors, so every element is a word of even length at most twelve. Thus \(H\) is a finite union of continuous images of the compact spaces \((S^8)^{2r}\), \(0\le2r\le12\). Each such space is path connected by Y.2, and each word image contains the identity, by taking successive equal factors. Their union is compact and path connected. It is consequently a closed matrix subgroup and an embedded Lie group by [Invariant connections on homogeneous bundles, Theorem A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). Its orthogonal determinants are one by connectedness.

The coefficients of \(P(\pi(h)v)\) can be recovered by the trace pairings with \(P_a\), so \(\pi\) is smooth. Its differential is injective: a tangent vector in its kernel exponentiates to the discrete group \(\{\pm1\}\), hence its whole one-parameter subgroup is the identity. For orthogonal unit \(u,v\), the curve
\[
P(u)P\left(\frac{u+tv}{\sqrt{1+t^2}}\right)
=\frac{1+tP(u)P(v)}{\sqrt{1+t^2}}
\]
has tangent \(P(u)P(v)\) at the identity. Direct commutation gives
\[
[P(u)P(v),P(w)]
 =2\langle v,w\rangle P(u)-2\langle u,w\rangle P(v).
\tag{AB.8}
\]
The \(36\) coordinate tangents therefore map to a basis of \(\mathfrak{so}(9)\). This proves the dimension and Lie-algebra assertions, and the trace calculation already made gives (AB.4). The inverse-function theorem makes \(\pi\) a local diffeomorphism. Take a small identity neighbourhood \(U\) disjoint from \(-U\), on which it is injective. Every lift of \(\pi(U)\) differs from its unique lift in \(U\) by a kernel element; thus its inverse image is \(U\sqcup(-U)\). Translation supplies two-sheeted covering charts everywhere.

Finally let \(s_0=(1,0)\in S\). For \(1\le i\le7\) and \(0\le a\le7\),
\[
B_{0i}s_0=(-e_i,0),\qquad
B_{a8}s_0=(0,\bar e_a).
\tag{AB.9}
\]
These are a basis of \(T_{s_0}S^{15}\). The map obtained by multiplying the corresponding fifteen exponentials and applying them to \(s_0\) has invertible differential at zero in a sphere chart. The inverse-function theorem makes the orbit open; group translation makes it open at every orbit point. It is closed by compactness of \(H\). Since \(S^{15}\) is connected, it is the whole sphere. Any nonzero invariant real subspace contains one unit vector, hence its whole sphere orbit, so equals \(S\). This proves irreducibility. □

**Theorem AB.2 (at most one spin curvature parameter).** Let \(\mathfrak h=\operatorname{span}\{B_{ab}\}\subset\mathfrak{so}(S)\) be the algebra in AB.1, and put
\[
\omega_{ab}(x,y)=\langle B_{ab}x,y\rangle,\qquad
Q_0(x,y,z,t)=\sum_{a<b}\omega_{ab}(x,y)\omega_{ab}(z,t).
\tag{AB.10}
\]
Every \(\mathfrak h\)-valued algebraic curvature tensor is a real multiple of \(Q_0\). The tensor \(Q_0\) is nonzero and invariant under \(H\). In particular the space of such curvature tensors has dimension at most one, and every one is \(H\)-invariant.

**Proof.** Lemma U.1 identifies a pair-symmetric curvature tensor with a self-adjoint operator on \(\mathfrak{so}(S)\). If its image is in \(\mathfrak h\), it kills \(\mathfrak h^\perp\): for \(v\in\mathfrak h^\perp\), self-adjointness gives \((Av,w)_*=(v,Aw)_*=0\) for every \(w\). Consequently its four-tensor is a linear combination of
\(\omega_A\odot\omega_D\), where \(A,D\) are two-element subsets of \(\{0,\ldots,8\}\) and
\[
(\alpha\odot\beta)(x,y,z,t)
=\tfrac12\bigl(\alpha(x,y)\beta(z,t)+\beta(x,y)\alpha(z,t)\bigr).
\]
The \(36\) forms \(\omega_A\) are independent by AB.4. These symmetric products are therefore an independent basis of the relevant symmetric tensors. Expanding the three cyclic terms in Bianchi shows that, for this combination, Bianchi is equivalent to the vanishing of the same linear combination of the four-forms \(\omega_A\wedge\omega_D\). Each wedge is twice the cyclic sum, so the factor is the same for diagonal and off-diagonal products.

Conjugation by \(P_r\) negates \(B_{ab}\) if \(r\in\{a,b\}\) and fixes it otherwise. These nine conjugation actions commute on tensors, since \(P_rP_s=-P_sP_r\) and the scalar sign disappears in conjugation. They preserve \(\mathfrak h\) and all algebraic curvature identities. On \(\omega_A\odot\omega_D\) their simultaneous signs are indexed by \(A\triangle D\). Applying the commuting projections
\[
\prod_{r=0}^8\frac{1+\epsilon_r\tau_r}{2},
\tag{AB.11}
\]
where \(\tau_r\) is conjugation on tensors and \(\epsilon_r=\pm1\), separates each set of simultaneous signs. Each separated part of a curvature tensor still satisfies Bianchi.

There are exactly three types of parts: diagonal products, with \(A\triangle D=\varnothing\); seven products sharing one index, for each fixed two-element symmetric difference; and three products on disjoint pairs, for each fixed four-element symmetric difference. We show that the last two types have zero Bianchi kernel. Any permutation of the nine coordinates, adjusted by one coordinate sign if necessary, is in \(\mathrm{SO}(9)\) and lifts through AB.3. Conjugation by a lift permutes the \(B_{ab}\), up to sign. It is therefore enough to consider the symmetric differences \(\{0,1\}\) and \(\{0,1,2,3\}\).

Here is the full finite calculation for these two parts. Number the orthonormal basis of \(S\) as
\[
s_i=(e_i,0),\quad s_{8+i}=(0,e_i)\qquad(0\le i\le7).
\]
For skew matrices \(A,D\), the coefficient of their two-form wedge on the increasing quadruple \((i,j,k,l)\) is
\[
A_{ij}D_{kl}-A_{ik}D_{jl}+A_{il}D_{jk}
+D_{ij}A_{kl}-D_{ik}A_{jl}+D_{il}A_{jk}.
\tag{AB.12}
\]
The matrix entries of a two-form \(\langle A\,\cdot,\cdot\rangle\) are \(-A_{ij}\); the two minus signs cancel in this formula. All matrices used below are the products in (AB.1), with the seven oriented multiplication triples of (Z.12).

For symmetric difference \(\{0,1\}\), order the columns as
\[
\omega_{02}\wedge\omega_{12},\
\omega_{03}\wedge\omega_{13},\
\omega_{04}\wedge\omega_{14},\
\omega_{05}\wedge\omega_{15},\
\omega_{06}\wedge\omega_{16},\
\omega_{07}\wedge\omega_{17},\
\omega_{08}\wedge\omega_{18}.
\]
Evaluating (AB.12) gives the following seven rows:

| Quadruple | Column coefficients |
| --- | --- |
| \((0,2,4,7)\) | \((-1,-1,-1,-1,-1,-1,0)\) |
| \((0,2,8,11)\) | \((1,1,0,0,0,0,1)\) |
| \((0,2,12,15)\) | \((-1,1,0,0,0,0,0)\) |
| \((0,4,8,13)\) | \((0,0,1,1,0,0,1)\) |
| \((0,4,10,15)\) | \((0,0,1,-1,0,0,0)\) |
| \((0,6,8,15)\) | \((0,0,0,0,-1,-1,-1)\) |
| \((0,6,10,13)\) | \((0,0,0,0,1,-1,0)\) |

These entries involve only multiplication of the displayed signed-permutation matrices. For example, on \((0,2,12,15)\), the column for \(\omega_{02}\wedge\omega_{12}\) has its only nonzero term \( (B_{02})_{02}(B_{12})_{12,15}=-1\); the column for \(\omega_{03}\wedge\omega_{13}\) has its only nonzero term \((B_{13})_{02}(B_{03})_{12,15}=1\). Equivalently each entry can be obtained by applying the two operators successively to the indicated \(s_i\); formula (AB.12) fixes all signs and six terms.

If the coefficient vector is \((q_2,\ldots,q_8)\), rows three, five and seven first give
\[
q_2=q_3=a,\qquad q_4=q_5=b,\qquad q_6=q_7=c.
\]
Rows two, four and six give \(2a+q_8=2b+q_8=2c+q_8=0\), so \(a=b=c\). Row one then gives \(6a=0\). Every coefficient is zero.

For symmetric difference \(\{0,1,2,3\}\), order the three columns as
\[
\omega_{01}\wedge\omega_{23},\quad
\omega_{02}\wedge\omega_{13},\quad
\omega_{03}\wedge\omega_{12}.
\]
The same entry formula gives

| Quadruple | Column coefficients |
| --- | --- |
| \((0,1,2,3)\) | \((2,-2,2)\) |
| \((0,1,12,13)\) | \((-2,0,0)\) |
| \((0,2,12,14)\) | \((0,2,0)\) |

The last two rows force the first two coefficients to vanish, and the first row then forces the third to vanish. Thus every off-diagonal part of a curvature tensor is zero.

It remains to handle a diagonal tensor
\[
Q=\sum_{a<b}\lambda_{ab}\,\omega_{ab}\odot\omega_{ab}.
\]
Conjugate by a lift of a rotation through angle \(\theta\) in the coordinate plane \(a,b\). For \(c\ne a,b\), the two forms for \(ac,bc\), with consistently oriented indices, rotate into one another. Their squared terms acquire a mixed coefficient
\[
2(\lambda_{ac}-\lambda_{bc})\sin\theta\cos\theta.
\]
The conjugated tensor still satisfies Bianchi, and we just proved that all its off-diagonal coefficients are zero. Taking \(\theta=\pi/4\) gives \(\lambda_{ac}=\lambda_{bc}\). This holds for every three distinct indices. All edges of the complete graph on nine indices can be connected by edges sharing a vertex, so all \(36\) coefficients are equal. This proves the asserted inclusion in \(\mathbb RQ_0\); no assumption that \(Q\) was initially invariant has been made.

Finally \(H\) preserves \(\mathfrak h\) by conjugation and preserves its trace inner product. The \(B_{ab}/\sqrt8\) are an orthonormal basis for that inner product. An orthogonal change among them leaves the sum of their tensor squares unchanged, proving invariance of \(Q_0\). It is nonzero: \(B_{08}s_0=s_8\), so
\(Q_0(s_0,s_8,s_0,s_8)=\sum_{a<b}\omega_{ab}(s_0,s_8)^2\ge1\).
This proves all the stated assertions. □

**Corollary AB.3 (the spin-nine holonomy exclusion).** A Riemannian manifold whose restricted holonomy is \(\mathrm{Spin}(9)\) in the real sixteen-dimensional representation of AB.1 has parallel curvature. Thus that representation cannot occur as the restricted holonomy of a metric with nonparallel curvature.

**Proof.** The representation is irreducible by AB.1. Every algebraic curvature tensor valued in its holonomy algebra is invariant under the restricted holonomy group by AB.2. All hypotheses of Theorem U.5 hold, with dimension \(16\ge3\). That theorem, including its contracted-Bianchi argument and transport comparison, gives \(\nabla R=0\). Neither this argument nor U.5 assumes completeness or simple connectivity. □

## AC. Reducing sphere actions to semisimple representations

Let \(V\) be a nonzero finite-dimensional real inner-product space. For a group \(H\subseteq\mathrm O(V)\), write
\[
D_H=\{A\in\operatorname{End}_{\mathbb R}(V):Ah=hA\text{ for every }h\in H\}.
\tag{AC.1}
\]
This is an associative real algebra, with multiplication given by composition. The next two lemmas establish the real, complex and quaternionic alternatives used in representation theory. They apply to any irreducible orthogonal action, without a connectedness assumption.

**Lemma AC.1 (the full real commutant).** If \(H\) acts irreducibly on \(V\), then \(D_H\), with its adjoint operation, is isomorphic to precisely one of
\[
\begin{gathered}
(\mathbb R,\text{identity}),\\
(\mathbb C,\text{complex conjugation}),\\
(\mathbb H,\text{quaternionic conjugation}).
\end{gathered}
\tag{AC.2}
\]
More explicitly, its self-adjoint part is \(\mathbb RI\). Its skew-adjoint part has dimension \(0\), \(1\) or \(3\). In the one-dimensional case it is \(\mathbb RJ\), where \(J^2=-I\). In the three-dimensional case it has an orthonormal basis \(J,K,JK\), where
\[
J^2=K^2=-I,\qquad JK=-KJ.
\tag{AC.3}
\]
Here the inner product on the skew-adjoint part is
\(-\operatorname{tr}(AB)/\dim_{\mathbb R}V\). The orthogonal elements of \(D_H\) are respectively the real scalars \(\{\pm I\}\), a unit circle, and the unit quaternions.

**Proof.** If \(A\in D_H\) is nonzero, its kernel and image are \(H\)-invariant. Irreducibility makes its kernel zero and its image all of \(V\), so \(A\) is invertible. Its inverse commutes with \(H\), by multiplying \(Ah=hA\) on both sides. Also \(A^*\in D_H\): take adjoints in the same equation and use \(h^*=h^{-1}\). Thus the symmetric and skew parts of \(A\) both belong to \(D_H\).

The self-adjoint commutant argument proved in F.1 makes the symmetric part scalar. Write
\[
D_H=\mathbb RI\oplus E,\qquad E=\{A\in D_H:A^*=-A\}.
\tag{AC.4}
\]
For \(A\in E\), the self-adjoint operator \(A^2\) is scalar. Taking traces and using the component formula in F.1 gives
\[
A^2=-\|A\|_E^2I,\qquad
AB+BA=-2(A,B)_E I\quad(A,B\in E).
\tag{AC.5}
\]
The second identity follows by applying the first to \(A+B\) and subtracting. The trace form is positive definite on \(E\), again by its sum-of-squares formula.

If \(E\ne0\), normalize any nonzero element to obtain \(J^2=-I\). If \(E\ne\mathbb RJ\), choose a unit \(K\in E\) perpendicular to \(J\). Equation (AC.5) gives \(JK=-KJ\). The product \(L=JK\) is skew-adjoint, since \(L^*=KJ=-JK\), and \(L^2=-I\). It anticommutes with each of \(J,K\), so (AC.5) says that it is perpendicular to each. It has norm one.

There cannot be a nonzero \(A\in E\) perpendicular to \(J,K,L\). Such an \(A\) would anticommute with all three by (AC.5), but associativity gives
\[
AL=AJK=-JAK=JKA=LA.
\]
Consequently \(LA=0\). The invertibility of \(L\) gives \(A=0\), a contradiction. Orthogonal projection now proves that \(E=\operatorname{span}_{\mathbb R}\{J,K,JK\}\) whenever its dimension exceeds one. It follows that the only dimensions are \(0,1,3\).

In the three-dimensional case (AC.3), associativity and \(L=JK\) give
\(KL=J\), \(LJ=K\), and the negatives in the reversed orders. Together with the three squares \(-I\), these are exactly the quaternion multiplication rules of Y.1. The map taking \(1,i,j,k\) to \(I,J,K,L\) is therefore an algebra isomorphism. The one-dimensional case similarly identifies \(a+bi\) with \(aI+bJ\). The three algebras have distinct real dimensions, so the alternatives are disjoint.

For \(T=aI+A\), \(A\in E\), equations (AC.4)–(AC.5) give
\[
T^*=aI-A,\qquad T^*T=(a^2+\|A\|_E^2)I.
\tag{AC.6}
\]
This proves both the stated adjoint and the description of the orthogonal elements.

The quaternionic alternative also forces \(\dim_{\mathbb R}V\) to be divisible by four. For a unit vector \(v\), the four vectors \(v,Jv,Kv,Lv\) are orthonormal: diagonal norms follow from orthogonality, and every mixed inner product reduces to \(\langle v,Av\rangle=0\) for one of the skew operators \(J,K,L\). Their span is stable under these operators by the multiplication rules, and its orthogonal complement is stable because the operators are skew-adjoint. Induction decomposes \(V\) into such four-dimensional subspaces. The analogous two-dimensional argument for \(J\) was proved in F.1. □

**Lemma AC.2 (real, complex and quaternionic representation types).** Let \(H\) act irreducibly and orthogonally on \(V\). Exactly the following three alternatives occur.

1. If \(D_H=\mathbb RI\), then the complexification \(V_{\mathbb C}\) is complex irreducible and has its usual \(H\)-invariant conjugation with square \(I\).
2. If \(D_H\cong\mathbb C\), choose \(J\) as in AC.1 and let \(W=(V,J)\). Then \(W\) is complex irreducible, its conjugate representation \(\overline W\) is inequivalent to it, and
\[
V_{\mathbb C}\cong W\oplus\overline W.
\tag{AC.7}
\]
3. If \(D_H\cong\mathbb H\), choose \(J,K\) as in AC.1 and again put \(W=(V,J)\). Then \(W\) is complex irreducible, \(K\) is an \(H\)-invariant conjugate-linear operator on \(W\) with \(K^2=-I\), and
\[
V_{\mathbb C}\cong W\oplus W.
\tag{AC.8}
\]
There is no \(H\)-invariant conjugate-linear involution on this \(W\). In either of the last two alternatives, the complex-linear commutant of \(W\) consists of the complex scalars.

**Proof.** Equip \(V_{\mathbb C}\) with the Hermitian inner product extending a real orthonormal basis of \(V\). The complex orthonormal-basis construction in Y.2 gives orthogonal complements and their projections. Since every \(h\in H\) has a real orthogonal matrix, it is unitary for this product. If \(U\subset V_{\mathbb C}\) is a complex invariant subspace, so is \(U^\perp\): for \(u\in U\) and \(w\perp U\), the identity
\(\langle hw,u\rangle=\langle w,h^{-1}u\rangle=0\)
proves this. Thus the Hermitian orthogonal projection \(P\) onto \(U\) commutes with \(H\).

Write its complex matrix in that real basis as \(P=A+iB\), with \(A,B\) real. Commutation with the real matrices of \(H\) gives \(A,B\in D_H\). If \(D_H=\mathbb RI\), write \(A=aI\), \(B=bI\). The equation \(P^*=P\) forces \(b=0\), and \(P^2=P\) forces \(a=0\) or \(a=1\). Hence \(U=0\) or \(V_{\mathbb C}\). This proves complex irreducibility. The ordinary conjugation fixes \(V\), commutes with every real matrix, and squares to \(I\).

In either remaining case, \(J\) commutes with \(H\), so \(W=(V,J)\) is a complex representation. Any nonzero complex invariant subspace would also be a nonzero real invariant subspace of \(V\), hence would be all of \(V\). This proves complex irreducibility without an appeal to a complex Schur lemma.

Extend \(J\) complex-linearly to \(V_{\mathbb C}\). Its two eigenspaces have eigenvalues \(i,-i\), and the projections onto them are
\(\frac12(I-iJ)\), \(\frac12(I+iJ)\). Their sum is \(I\), their product is zero, and their images exhaust \(V_{\mathbb C}\). The maps
\[
v\longmapsto v-iJv,\qquad
v\longmapsto v+iJv
\tag{AC.9}
\]
identify these two eigenspaces with \(W\) and \(\overline W\), respectively. To verify surjectivity, write an \(i\)-eigenvector as \(a+ib\), with \(a,b\in V\). Comparing real and imaginary parts gives \(b=-Ja\); the other eigenspace has \(b=Ja\). The first map is complex-linear because its value at \(Jv\) is \(i(v-iJv)\); the second has the corresponding property for multiplication by \(i\) equal to \(-J\) on \(\overline W\). Both commute with \(H\). This proves (AC.7) in both cases.

A complex-linear endomorphism of \(W\) commuting with \(H\) is exactly an element \(A\in D_H\) satisfying \(AJ=JA\). In \(\mathbb C\) every element has this property. In \(\mathbb H\), write \(A=aI+bJ+cK+dJK\) and use (AC.3); the equation forces \(c=d=0\). In both cases this commutant is \(\mathbb RI+\mathbb RJ\), the complex scalars.

A complex-linear map \(W\to\overline W\) commuting with \(H\), regarded as a real map on \(V\), instead satisfies \(AJ=-JA\). In the complex alternative, substituting \(A=aI+bJ\) forces \(a=b=0\). Thus no isomorphism \(W\cong\overline W\) exists there. In the quaternionic alternative, every such map is \(cK+dJK\). The particular map \(K\) is invertible, commutes with \(H\), anticommutes with \(J\), and has square \(-I\). It identifies \(\overline W\) with \(W\), converting (AC.7) into (AC.8). Finally
\[
(cK+dJK)^2=-(c^2+d^2)I
\tag{AC.10}
\]
by the quaternion rules, so no such map squares to \(I\). This proves all the stated distinctions. □

**Lemma AC.3 (the semisimple subgroup and the central circle).** Suppose now that \(H\subseteq\mathrm O(V)\) is a connected compact Lie subgroup acting irreducibly, with Lie algebra \(\mathfrak h\). Then
\[
\mathfrak h=\mathfrak s\oplus\mathfrak z,\qquad
\mathfrak s=[\mathfrak h,\mathfrak h],\qquad
\mathfrak z=\{Z\in\mathfrak h:[Z,\mathfrak h]=0\}
\tag{AC.11}
\]
is an orthogonal direct sum for the positive trace form \(-\operatorname{tr}(XY)\). The algebra \(\mathfrak s\) is a direct sum of nonabelian simple ideals. The centre \(\mathfrak z\) has dimension at most one.

There is a connected closed compact subgroup \(S\triangleleft H\) with Lie algebra \(\mathfrak s\). If \(\mathfrak z=0\), then \(H=S\). Otherwise \(\mathfrak z=\mathbb RJ\), where \(J^2=-I\), and
\[
Z=\{\cos t\,I+\sin t\,J:t\in\mathbb R\},\qquad
H=SZ,\qquad SZ=ZS.
\tag{AC.12}
\]
In both cases \(S=[H,H]\), where the right side means the group generated by all commutators, without taking its closure.

**Proof.** In this proof the bracket of two linear subspaces means the linear span of all brackets of their elements. Jacobi shows that \(\mathfrak s=[\mathfrak h,\mathfrak h]\) is an ideal. Trace cyclicity, established in F.1, gives
\[
([X,Y],T)_*=(X,[Y,T])_*.
\tag{AC.13}
\]
It follows that \(X\perp\mathfrak s\) exactly when \([X,Y]=0\) for every \(Y\in\mathfrak h\): apply (AC.13) for all \(Y,T\), and use nondegeneracy. Thus \(\mathfrak s^\perp=\mathfrak z\), proving (AC.11).

The centre of \(\mathfrak s\) is zero. Indeed an element commuting with \(\mathfrak s\) and belonging to it also commutes with \(\mathfrak z\), hence lies in \(\mathfrak s\cap\mathfrak z=0\). Every ideal \(\mathfrak a\subseteq\mathfrak s\) has an orthogonal complementary ideal, by (AC.13), and the two ideals commute because their bracket belongs to their intersection. If \(\mathfrak a\) is abelian, then for \(X\in\mathfrak s\) and \(A,B\in\mathfrak a\),
\[
([X,A],B)_*=(X,[A,B])_*=0.
\]
Since \([X,A]\in\mathfrak a\), it is zero, making \(\mathfrak a\) central in \(\mathfrak s\); therefore \(\mathfrak a=0\).

If \(\mathfrak s\ne0\), choose a nonzero ideal of least positive dimension and split off its orthogonal complement. It is nonabelian by the preceding paragraph. Any ideal inside it is also an ideal of \(\mathfrak s\), since the complementary ideal commutes with it; minimality therefore says that it is simple. Repeat on the orthogonal complement. The dimension strictly decreases, so this gives a finite direct sum of nonabelian simple ideals, including the empty sum when \(\mathfrak s=0\).

An element of \(\mathfrak z\) commutes with the exponentials of \(\mathfrak h\), and hence with \(H\) by F.1. Thus \(\mathfrak z\) is an abelian subspace of the skew-adjoint part of \(D_H\). AC.1 shows that such a subspace has dimension at most one. In the quaternionic case, for example, if two independent imaginary elements commute, subtract a multiple of one from the other to make them nonzero and orthogonal. Equation (AC.5) then makes them anticommute too. Their product would be zero, contrary to invertibility. The other two cases are immediate from their dimensions.

Lemma U.3 integrates the ideal \(\mathfrak s\) to a connected closed compact normal subgroup \(S\) of \(H\). If \(\mathfrak z\ne0\), normalize its generator by AC.5 to get \(J^2=-I\). The matrix exponential series, or the matrix ODE with its initial value, gives
\(\exp(tJ)=\cos t\,I+\sin t\,J\).
Its image \(Z\) is a compact connected circle: its coordinates relative to \(I,J\) are exactly the unit circle in \(\mathbb R^2\). It commutes with \(H\). Every \(X\in\mathfrak h\) is \(X_s+tJ\); commutation and uniqueness for the matrix ODE give
\(\exp X=\exp X_s\,\exp(tJ)\).
Connected exponential generation therefore gives \(H=SZ\). If \(\mathfrak z=0\), that same generation gives \(H=S\).

It remains to verify the assertion about the group commutator, so that no closedness convention is hidden in it. First \(H=SZ\) with \(Z\) central implies \([H,H]\subseteq S\). For the reverse inclusion consider
\[
E=\operatorname{span}_{\mathbb R}\{\operatorname{Ad}(g)X-X:g\in S,\ X\in\mathfrak s\}.
\]
An element of \(\mathfrak s\) perpendicular to \(E\) is fixed by every \(\operatorname{Ad}(g)\), by invariance of the trace form. Differentiating at \(\exp(tX)\) makes it central in \(\mathfrak s\), hence zero. Therefore \(E=\mathfrak s\). Choose pairs \(g_j,X_j\) such that \(\operatorname{Ad}(g_j)X_j-X_j\), \(1\le j\le d=\dim\mathfrak s\), are a basis. The smooth map
\[
(t_1,\ldots,t_d)\longmapsto
\prod_{j=1}^d\bigl(g_j\exp(t_jX_j)g_j^{-1}\exp(-t_jX_j)\bigr)
\tag{AC.14}
\]
has invertible differential at zero as a map into \(S\). The inverse-function theorem of Local tools 1.2 puts an open identity neighbourhood of \(S\) in \([S,S]\). A subgroup containing such a neighbourhood is open, and its other cosets are open, so connectedness makes it all of \(S\), as in F.1. Hence \(S=[S,S]\subseteq[H,H]\). If \(d=0\), \(S=\{I\}\) and the conclusion is immediate. □

**Lemma AC.4 (the tangent test for sphere transitivity).** Let \(K\subseteq\mathrm O(V)\) be a compact Lie subgroup, let \(\mathfrak k\) be its Lie algebra, and suppose \(n=\dim_{\mathbb R}V\ge2\). The following are equivalent:
\[
\begin{array}{ll}
\text{(i)}&K\text{ is transitive on }S(V),\\
\text{(ii)}&\mathfrak k v=v^\perp\text{ for every unit }v,\\
\text{(iii)}&\mathfrak k v=v^\perp\text{ for some unit }v.
\end{array}
\tag{AC.15}
\]
Under these conditions the orbit map \(K\to S(V)\), \(k\mapsto kv\), has smooth local sections.

**Proof.** The derivative of the orbit map at the identity sends \(X\) to \(Xv\). Skew-adjointness gives \(Xv\perp v\). Its rank is the same at every point \(k\in K\), since its derivative on the translated tangent vector \(kX\) is \(kXv\). Write this constant rank as \(r\).

Suppose first that the orbit map is onto but \(r<n-1\). The constant-rank theorem, [Local tools, Corollary 1.4](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), gives source and target charts in which each local image lies in an \(r\)-dimensional coordinate plane. Around every point of the compact manifold \(K\), choose a smaller coordinate ball with compact closure inside such a source chart. A finite number of these smaller balls cover \(K\). The image of each closure is compact, hence closed in the sphere by Local tools 0.1, and lies in a coordinate plane of dimension less than \(n-1\). It has empty interior in the sphere: in the target chart any nonempty open ball has a point with a nonzero coordinate normal to that plane.

A finite union of closed sets with empty interior cannot cover a nonempty manifold. Indeed start with a nonempty open set. Removing the first closed set leaves a nonempty open set, since otherwise the first set had interior. Repeat with each of the finitely many sets. The final nonempty open set misses their union. This contradicts surjectivity. Therefore \(r=n-1\), proving (i) implies (ii). Implication (ii) to (iii) is immediate.

If (iii) holds, choose \(X_1,\ldots,X_{n-1}\in\mathfrak k\) whose values at \(v\) are a basis of \(v^\perp\). The map
\[
(t_1,\ldots,t_{n-1})\longmapsto
\exp(t_1X_1)\cdots\exp(t_{n-1}X_{n-1})v
\tag{AC.16}
\]
has invertible differential at zero in a sphere chart. Local tools 1.2 makes its image contain a neighbourhood of \(v\). Group translation does the same at every point of the orbit. The orbit is closed because \(K\) is compact. The sphere is connected for \(n\ge2\), by the normalized-segment paths of Y.2. This nonempty open and closed orbit is thus the whole sphere, proving (i).

The local inverse of (AC.16), followed by its product of exponentials in \(K\), is a smooth local section of the orbit map near \(v\). Translating this section by any \(k\in K\) gives one near \(kv\). These points exhaust the sphere. □

**Theorem AC.5 (the semisimple subgroup stays transitive).** Let \(H\subseteq\mathrm{SO}(V)\) be connected and compact and transitive on \(S(V)\), with \(n=\dim_{\mathbb R}V\ge3\). Then its connected compact commutator subgroup \(S\) from AC.3 is also transitive on \(S(V)\). In particular the action of \(S\) is real irreducible.

**Proof.** Transitivity makes \(H\) irreducible: any nonzero invariant subspace contains a unit vector, hence its whole orbit, the unit sphere. AC.3 therefore applies. If \(\mathfrak z=0\), then \(H=S\) and there is nothing to prove. Suppose \(\mathfrak z=\mathbb RJ\) and write \(H=SZ\) as in (AC.12).

Assume for contradiction that \(S\) is not transitive. Fix a unit \(v\). By AC.4, \(\mathfrak s v\ne v^\perp\), whereas
\[
v^\perp=\mathfrak h v=\mathfrak s v+\mathbb RJv.
\]
Thus \(\mathfrak s v\) has codimension one in \(v^\perp\) and \(Jv\notin\mathfrak s v\). If \(X+tJ\in\mathfrak h\) fixes \(v\), with \(X\in\mathfrak s\), then \(Xv+tJv=0\), forcing \(t=0\). Define the linear functional
\[
\phi:\mathfrak h\longrightarrow\mathbb R,\qquad \phi(X+tJ)=t.
\tag{AC.17}
\]
It vanishes on the stabilizer algebra at \(v\), and it vanishes on every bracket by (AC.11). It is invariant under \(\operatorname{Ad}(H)\), since \(\mathfrak s\) is invariant and \(J\) is central.

There is consequently a well-defined \(H\)-invariant smooth one-form \(\alpha\) on \(S(V)\), specified at \(v\) by
\[
\alpha_v(Av)=\phi(A)\qquad(A\in\mathfrak h).
\tag{AC.18}
\]
Well-definedness follows because the kernel of \(A\mapsto Av\) is annihilated by \(\phi\). To extend to \(kv\), set \(\alpha_{kv}(kw)=\alpha_v(w)\). If \(k\) is changed by a stabilizer element \(a\), then
\(aAv=(\operatorname{Ad}(a)A)v\); invariance of \(\phi\) proves independence of that choice, even if the stabilizer is disconnected. Smoothness follows from the local sections in AC.4, which make this formula smooth in a neighbourhood of each point.

We check that \(\alpha\) is closed. Pull it back by the orbit map \(f:H\to S(V)\). On a left-translated tangent vector \(kA\),
\[
(f^*\alpha)_k(kA)=\alpha_{kv}(kAv)=\phi(A).
\tag{AC.19}
\]
Thus \(f^*\alpha\) is the left-invariant one-form with value \(\phi\) at the identity. For left-invariant vector fields \(A^L,B^L\), the defining formula for exterior differentiation gives
\[
d(f^*\alpha)(A^L,B^L)
=A^L(\phi(B))-B^L(\phi(A))-\phi([A,B])=0.
\tag{AC.20}
\]
Here their bracket is the left-invariant field with value \([A,B]\): the fields have matrix values \(kA,kB\), and their bracket is \(kAB-kBA\) by differentiating these linear functions. The two scalar functions in (AC.20) are constant. These fields span every tangent space, so the pulled-back exterior derivative is zero. Pullback commutes with exterior differentiation directly in coordinates: for a one-form \(\sum_i a_i(y)\,dy_i\) the pullback is \(\sum_i a_i(f(x))\,d f_i\); differentiation gives \(\sum_{i,j}(\partial_j a_i)(f(x))\,d f_j\wedge d f_i\), since the symmetric second derivatives of \(f_i\) cancel in \(d(d f_i)\). This is the pullback of the original exterior derivative. Since \(f\) has local sections, pulling back along a section gives \(d\alpha=0\) on each sphere chart.

For clarity we prove the exactness fact needed on this sphere. Any smooth closed one-form \(\beta=\sum_{j=1}^{d}b_j(x)\,dx_j\) on \(\mathbb R^d\) has potential
\[
F(x)=\int_0^1\sum_j b_j(tx)x_j\,dt.
\tag{AC.21}
\]
Closedness is the equation \(\partial_k b_j=\partial_j b_k\). Differentiation under this integral is justified on each compact coordinate neighbourhood by uniform continuity of the derivatives and the difference-quotient estimate of Local tools 0.3. Hence
\[
\begin{aligned}
\partial_k F(x)
&=\int_0^1\left(b_k(tx)+t\sum_j x_j\partial_k b_j(tx)\right)\,dt\\
&=\int_0^1\frac d{dt}\bigl(t\,b_k(tx)\bigr)\,dt
=b_k(x).
\end{aligned}
\tag{AC.22}
\]
Repeated differentiation also makes \(F\) smooth. This proves \(dF=\beta\).

Put \(d=n-1\ge2\). The two stereographic charts on \(S^d\), obtained by deleting the north or south pole, are each diffeomorphic to \(\mathbb R^d\). Explicitly one inverse chart is
\[
x\longmapsto
\left(\frac{2x}{1+|x|^2},\frac{|x|^2-1}{1+|x|^2}\right);
\tag{AC.23}
\]
its inverse is \(x=y/(1-t)\) for a sphere point \((y,t)\) with \(t\ne1\). The other chart changes the sign of the last coordinate. Their overlap is connected: deleting both poles gives the explicit product coordinates
\((u,t)\mapsto(\sqrt{1-t^2}\,u,t)\), with \(u\in S^{d-1}\) and \(-1<t<1\). The sphere \(S^{d-1}\) is path connected by Y.2, as \(d-1\ge1\).

Apply (AC.21)–(AC.22) to the pullback of \(\alpha\) in each chart. The two resulting potentials differ by a constant on the overlap, since their difference has zero derivative and integration along piecewise smooth paths makes it constant there. Adjust one by that constant. They then glue to a smooth real function \(F\) on \(S^d\) satisfying \(dF=\alpha\).

The compact sphere has a maximum point of \(F\), by Local tools 0.1. Differentiation along each tangent direction in a local chart gives \(dF=0\) at that point. But (AC.18) gives \(\alpha_v(Jv)=1\), and \(H\)-invariance and transitivity make \(\alpha\) nonzero at every point. This contradiction proves that \(S\) is transitive. Its real irreducibility follows from the same invariant-subspace argument used for \(H\). The restriction \(n\ge3\) is essential: the connected rotation group of a plane has trivial commutator subgroup. □

**Corollary AC.6 (recovering the central extensions).** Let \(n\ge3\). The classification of connected compact subgroups of \(\mathrm{SO}(n)\) transitive on the unit sphere reduces to the classification of their transitive semisimple subgroups \(S=[H,H]\), together with the following alternatives:

- If \(D_S\cong\mathbb R\), then \(H=S\).
- If \(D_S\cong\mathbb C\), then \(H=S\) or \(H=S\{\cos t\,I+\sin t\,J\}\), where \(J\) spans the imaginary part of \(D_S\).
- If \(D_S\cong\mathbb H\), then \(H=S\) or \(H=S\{\cos t\,I+\sin t\,J\}\), where \(J\) is any unit imaginary element of \(D_S\). All choices of this circle give orthogonally conjugate groups by conjugations that fix \(S\) elementwise.

Each displayed extension is a compact connected transitive matrix group. In a nontrivial circle extension the multiplication map \(S\times S^1\to H\) has finite central kernel. For \(n=2\) the only connected sphere-transitive subgroup is \(\mathrm{SO}(2)\).

**Proof.** By AC.5, \(S\) is transitive and hence real irreducible, so AC.1 describes \(D_S\). AC.3 writes \(H=SZ\) with \(\dim Z\le1\). If \(Z\ne\{I\}\), its generator is a skew-adjoint element \(J\in D_S\), normalized to square to \(-I\). This is impossible in the real case, unique up to sign in the complex case, and a unit imaginary quaternion in the quaternionic case. This gives every asserted alternative without assuming a classification of the semisimple possibilities.

We verify the conjugacy assertion explicitly. In the quaternion algebra \(D_S\), let \(a,b\) be unit imaginary elements. If \(b\ne-a\), put \(u=1-ba\). Then \(u\ne0\), because \(ba=1\) would imply \(b=a^{-1}=-a\), and
\[
ua=a+b=bu.
\]
Normalize \(u\) by its positive norm from (AC.6); the resulting orthogonal operator \(q\in D_S\) satisfies \(qaq^{-1}=b\). If \(b=-a\), choose a unit imaginary \(c\perp a\), possible in the three-dimensional space of AC.1. Anticommutation gives \(cac^{-1}=-a=b\), so take \(q=c\). In both cases \(q\) commutes with \(S\), conjugates the first circle onto the second, and thus conjugates the extensions. These are orthogonal conjugacies, which suffice to identify the representations.

Conversely any circle in \(D_S\) commutes with \(S\). Multiplication is a homomorphism from the compact connected product \(S\times S^1\). Its image is compact and connected, hence closed in the matrix group, and contains the transitive subgroup \(S\); it is therefore transitive. Its orthogonal determinant is one by connectedness, as in F.2.

The kernel consists of \((s,z)\) with \(s=z^{-1}\in S\cap S^1\). This intersection is central in \(S\). Its Lie algebra is zero: any element of its Lie algebra belongs to \(\mathfrak s\) and commutes with \(\mathfrak s\), whereas the latter has zero centre by AC.3. The closed-subgroup theorem in Invariant connections A.1 makes the intersection an embedded zero-dimensional Lie group, thus discrete. It is compact as a closed subset of the circle, so its isolating neighbourhoods have a finite subcover and it is finite. The kernel is consequently finite and central.

Finally a matrix in \(\mathrm{SO}(2)\) has, in an oriented orthonormal basis, the form \(\left(\begin{smallmatrix}a&-b\\ b&a\end{smallmatrix}\right)\), with \(a^2+b^2=1\), as follows by choosing its first column and the unique positively oriented perpendicular second column. There is exactly one such matrix taking the first basis vector to each unit vector. Any subgroup transitive on that circle must contain every such matrix, so equals \(\mathrm{SO}(2)\). □

## AD. Compact root spaces and highest weights

The semisimple subgroup in AC.5 acts by orthogonal matrices. Its Lie algebra therefore has a positive invariant inner product. This allows the root and highest-weight arguments needed below to be proved directly with adjoints. The free author notes of Kirillov listed in Further reading supply the rank-one and highest-weight constructions. All proof prerequisites are established below or in the earlier sections cited explicitly.

All complex Hermitian products in this section are linear in the first variable. The adjoint convention is \(\langle Ax,y\rangle=\langle x,A^*y\rangle\). A unitary representation of a real Lie algebra means a finite-dimensional complex representation in which its real elements act by skew-adjoint operators.

**Lemma AD.1 (Hermitian linear algebra and complete reducibility).** A Hermitian operator on a finite-dimensional complex inner-product space has an orthonormal basis of eigenvectors, with real eigenvalues. Any finite family of commuting Hermitian operators has a common such basis. A unitary representation of a real Lie algebra is an orthogonal sum of irreducible complex representations. The complex endomorphisms commuting with an irreducible unitary representation are exactly the complex scalars. Between two irreducible unitary representations, a nonzero intertwiner is an isomorphism; the space of intertwiners is then one-dimensional.

**Proof.** Regard the complex space \(W\) as a real space with product \(\operatorname{Re}\langle\cdot,\cdot\rangle\) and complex structure \(Jx=ix\). A Hermitian operator is real symmetric and commutes with \(J\). The real spectral theorem, proved in H.2 by maximizing the Rayleigh quotient and inducting on the orthogonal complement, decomposes \(W\) into real orthogonal eigenspaces with real eigenvalues. Each eigenspace is \(J\)-invariant. Complex Gram–Schmidt, whose subtraction and normalization are proved in Y.2, gives a complex orthonormal basis in each. Distinct real eigenspaces are also Hermitian orthogonal: real orthogonality to both \(y\) and \(iy\) forces both parts of \(\langle x,y\rangle\) to vanish.

For a commuting family, every operator preserves every eigenspace of the first. Apply the same argument on those spaces for the second operator and continue through the finite family. A commuting vector space of Hermitian operators is covered by choosing a finite basis of that vector space.

If \(U\subset W\) is invariant under skew-adjoint operators, so is \(U^\perp\), since
\[
\langle Xv,u\rangle=-\langle v,Xu\rangle=0
\quad(v\in U^\perp,\ u\in U).
\tag{AD.1}
\]
Choose a nonzero invariant subspace of least positive dimension and repeat on its orthogonal complement. This terminates and proves complete reducibility.

If \(T\) commutes with all the skew-adjoint operators, then \(T^*\) does too. Both
\[
A=\frac{T+T^*}{2},
\qquad B=\frac{T-T^*}{2i}
\tag{AD.2}
\]
are commuting endomorphisms of the representation and are Hermitian. Each eigenspace of either is invariant, so irreducibility makes \(A\) and \(B\) real scalar operators. Hence \(T\) is complex scalar. Finally, the kernel and image of an intertwiner are invariant. A nonzero intertwiner between irreducibles is therefore invertible, and composing any other intertwiner with its inverse proves the last assertion. □

**Lemma AD.2 (the unitary rank-one calculation).** Suppose operators \(E,F,H\) on a finite-dimensional Hermitian space satisfy
\[
[H,E]=2E,\qquad [H,F]=-2F,\qquad [E,F]=H,
\qquad E^*=F,\quad H^*=H.
\tag{AD.3}
\]
The space is an orthogonal sum of invariant strings. A string has, for a unique integer \(m\geq0\), a basis \(v_0,\ldots,v_m\) on which
\[
\begin{aligned}
Hv_j&=(m-2j)v_j,\\
Fv_j&=v_{j+1}\quad(0\leq j<m),\qquad Fv_m=0,\\
Ev_0&=0,\qquad Ev_j=j(m-j+1)v_{j-1}\quad(1\leq j\leq m).
\end{aligned}
\tag{AD.4}
\]
Its weight spaces are one-dimensional and the string is irreducible. In particular all eigenvalues of \(H\) are integers. Up to isomorphism there is exactly one irreducible string for each \(m\).

**Proof.** By AD.1, \(H\) has a largest eigenvalue \(m\) and a nonzero eigenvector \(v_0\). The first relation in (AD.3) makes \(Ev_0\) an eigenvector of eigenvalue \(m+2\), unless it is zero. Maximality therefore gives \(Ev_0=0\). Put \(v_j=F^jv_0\). Induction using the commutators gives
\[
Hv_j=(m-2j)v_j,\qquad
EF^jv_0=j(m-j+1)F^{j-1}v_0.
\tag{AD.5}
\]
For the second formula, commute the leftmost \(E\) past one \(F\), use \(EF=FE+H\), and use the first formula on \(F^{j-1}v_0\). The coefficient changes from \((j-1)(m-j+2)\) to that number plus \(m-2j+2\), which equals \(j(m-j+1)\).

Different nonzero \(v_j\) have distinct real eigenvalues and are independent. Finite dimension gives a largest \(N\) with \(v_N\ne0\), followed by \(v_{N+1}=0\). Substitution into (AD.5) yields
\[
0=(N+1)(m-N)v_N,
\]
so \(m=N\) is a nonnegative integer. The vectors \(v_0,\ldots,v_m\) are all nonzero: an earlier zero would force all subsequent vectors to be zero. Moreover
\[
\|v_j\|^2
=\langle Fv_{j-1},v_j\rangle
=j(m-j+1)\|v_{j-1}\|^2.
\tag{AD.6}
\]
Their span is invariant under \(E,F,H\). Any invariant subspace of this span is invariant under polynomials in \(H\). For each of its finitely many distinct eigenvalues, the polynomial that is one there and zero at the others projects onto that weight line. A nonzero invariant subspace consequently contains a \(v_j\); repeated \(E\), with the nonzero coefficients in (AD.4), reaches \(v_0\), and repeated \(F\) reaches every \(v_j\). This proves irreducibility.

The orthogonal complement of the string is invariant, because the adjoints of the three operators belong to their span. Induction on dimension proves the decomposition. The displayed matrices prove uniqueness. Conversely these matrices for any \(m\geq0\), with orthogonal basis and the positive norms prescribed by (AD.6), satisfy (AD.3), so every asserted string exists. □

**Lemma AD.3 (root spaces of a compact centreless algebra).** Let \(\mathfrak k\) be a nonzero real Lie algebra of skew-adjoint endomorphisms with zero centre. Choose a maximal abelian subalgebra \(\mathfrak t\), set
\[
\mathfrak g=\mathfrak k\otimes_{\mathbb R}\mathbb C,
\qquad \mathfrak a=i\mathfrak t,
\qquad \mathfrak h=\mathfrak t\otimes_{\mathbb R}\mathbb C
                  =\mathfrak a\otimes_{\mathbb R}\mathbb C,
\tag{AD.7}
\]
and let \(\sigma\) denote conjugation with fixed real space \(\mathfrak k\). There is a finite spanning set \(R\subset\mathfrak a^*\setminus\{0\}\) such that
\[
\mathfrak g=\mathfrak h\oplus\bigoplus_{\alpha\in R}\mathfrak g_\alpha,
\qquad
\mathfrak g_\alpha=\{X:[H,X]=\alpha(H)X\ \text{for all }H\in\mathfrak a\}.
\tag{AD.8}
\]
Every \(\mathfrak g_\alpha\) is one-dimensional. The form
\(\kappa(X,Y)=\operatorname{tr}_{\mathfrak g}(\operatorname{ad}X\operatorname{ad}Y)\)
is positive definite on the real space \(\mathfrak a\); it identifies \(\mathfrak a^*\) with a Euclidean space. Write \((\alpha,\beta)\) for the induced product and \(T_\alpha\in\mathfrak a\) for the vector dual to \(\alpha\). One can choose
\[
E_\alpha\in\mathfrak g_\alpha,\qquad
F_\alpha=-\sigma E_\alpha\in\mathfrak g_{-\alpha},
\qquad
H_\alpha=\frac{2T_\alpha}{(\alpha,\alpha)}
\tag{AD.9}
\]
so that they satisfy the three commutators in (AD.3). On every unitary \(\mathfrak k\)-module their operators satisfy the adjoint identities there as well. Finally, if \(c\alpha\in R\) for a real \(c\), then \(c=\pm1\).

**Proof.** The given skew-adjoint realization gives \(\mathfrak k\) the positive product
\[
b(X,Y)=-\operatorname{tr}_V(XY).
\tag{AD.10}
\]
It is positive because \(b(X,X)=\operatorname{tr}(X^*X)\), and it is invariant because cyclically moving factors under the trace gives
\(b([X,Y],Z)=-b(Y,[X,Z])\).
Thus \(\operatorname{ad}X\) is \(b\)-skew-adjoint. Its squared trace is
\[
\kappa(X,X)=-\|\operatorname{ad}X\|_{\mathrm{HS},b}^2.
\tag{AD.11}
\]
Zero centre makes this strictly negative for \(X\ne0\). Polarization and complexification now show that
\[
\langle X,Y\rangle_{\mathfrak g}=-\kappa(X,\sigma Y)
\tag{AD.12}
\]
is a positive Hermitian product. For example, in a real \((-\kappa)\)-orthonormal basis it is the usual sum of a coordinate times the conjugate coordinate. The trace definition gives symmetry and the identity
\[
\kappa([X,Y],Z)=\kappa(X,[Y,Z])
\tag{AD.13}
\]
by expanding commutators and cycling factors. Consequently
\((\operatorname{ad}X)^*=-\operatorname{ad}(\sigma X)\).
For \(H\in\mathfrak a\), \(\sigma H=-H\), so \(\operatorname{ad}H\) is Hermitian. Also \(\kappa(iT,iT)=-\kappa(T,T)>0\) for real nonzero \(T\in\mathfrak t\).

A maximal abelian \(\mathfrak t\) exists by choosing one of maximal dimension. Its centralizer in \(\mathfrak k\) is precisely \(\mathfrak t\): otherwise adjoining an element that centralizes it enlarges the abelian subalgebra. The same assertion after complexification gives centralizer \(\mathfrak h\) in \(\mathfrak g\). Apply simultaneous diagonalization in AD.1 to a real basis of \(\mathfrak a\). The eigenvalues are real linear functionals on \(\mathfrak a\), the common zero space is \(\mathfrak h\), and (AD.8) follows. Conjugating its defining equation gives
\(\sigma\mathfrak g_\alpha=\mathfrak g_{-\alpha}\). Jacobi gives
\[
[\mathfrak g_\alpha,\mathfrak g_\beta]\subseteq
\mathfrak g_{\alpha+\beta},
\tag{AD.14}
\]
where \(\mathfrak g_0=\mathfrak h\) and a missing nonzero weight denotes zero. Invariance gives
\((\alpha+\beta)(H)\kappa(X,Y)=0\) for \(X\in\mathfrak g_\alpha\), \(Y\in\mathfrak g_\beta\).
Thus only opposite spaces pair. Their pairing is nondegenerate by (AD.12). If \(H\in\mathfrak a\) is annihilated by every root, it commutes with all of (AD.8). The complex centre is zero, since its real and imaginary parts would be central in \(\mathfrak k\). Hence \(H=0\), proving that \(R\) spans \(\mathfrak a^*\).

Choose \(E\ne0\) in \(\mathfrak g_\alpha\) and initially put \(F=-\sigma E\). Then \(\kappa(E,F)=\langle E,E\rangle_{\mathfrak g}>0\). For \(H\in\mathfrak h\), (AD.13) gives
\[
\kappa([E,F],H)=\kappa(E,[F,H])
=\alpha(H)\kappa(E,F).
\tag{AD.15}
\]
Here roots and \(\kappa|_{\mathfrak a}\) are extended complex linearly to \(\mathfrak h\). The bracket is in \(\mathfrak h\), where the form is nondegenerate, so
\([E,F]=\kappa(E,F)T_\alpha\).
Rescale \(E\) by a positive real number and \(F\) by the same number to make
\(\kappa(E,F)=2/(\alpha,\alpha)\). This gives (AD.9) and all three commutators. For any unitary representation \(\rho\), complex linear extension of skew-adjointness says
\[
\rho(X)^*=-\rho(\sigma X).
\tag{AD.16}
\]
It proves the required adjoint identities, including for the adjoint representation itself.

To prove both dimension and reducedness without assuming either, fix \(\alpha\) and consider the invariant subspace
\[
M=\mathfrak h\oplus
\bigoplus_{\substack{\gamma\in R\\\gamma\in\mathbb R\alpha}}\mathfrak g_\gamma
\tag{AD.17}
\]
for its rank-one triple. The \(H_\alpha\)-zero space is exactly \(\mathfrak h\). The map
\(\operatorname{ad}E_\alpha:\mathfrak h\to M\)
has rank one, since it sends \(H\) to \(-\alpha(H)E_\alpha\). By AD.2, each nontrivial even string contributes one to this rank: its zero-weight vector raises nontrivially. Odd strings have no zero weight, and trivial strings contribute zero. The subspace spanned by \(F_\alpha,H_\alpha,E_\alpha\) is already an even string with highest weight two. Hence it is the only nontrivial even string. In particular the weight-two space of \(M\) is precisely \(\mathfrak g_\alpha\) and has dimension one, and its weight-four space is zero. Thus \(2\alpha\notin R\).

If \(c\alpha\in R\), replace it by its negative to assume \(c>0\). Apply the integral-eigenvalue conclusion of AD.2 first to the \(\alpha\) triple and then to the \(c\alpha\) triple, acting on \(\mathfrak g\). It gives
\[
2c\in\mathbb Z_{>0},
\qquad
2/c\in\mathbb Z_{>0}.
\tag{AD.18}
\]
Their product is four, so \(c\) is \(1/2\), \(1\) or \(2\). The last case has just been excluded. The first would say that \(\alpha\) is twice the root \(\alpha/2\), also excluded by the same argument for that root. This proves reducedness and completes the proof. □

**Lemma AD.4 (root strings and reflection symmetry).** For distinct nonproportional roots \(\alpha,\beta\), the roots on \(\beta+\mathbb Z\alpha\) are exactly
\[
\begin{gathered}
\beta-r\alpha,\ \ldots,\ \beta,\ \ldots,\ \beta+q\alpha,
\qquad r,q\in\mathbb Z_{\geq0},\\
r-q=\beta(H_\alpha)=\frac{2(\beta,\alpha)}{(\alpha,\alpha)}.
\end{gathered}
\tag{AD.19}
\]
Whenever \(\alpha+\beta\) is a root, the bracket
\([\mathfrak g_\alpha,\mathfrak g_\beta]=\mathfrak g_{\alpha+\beta}\)
is nonzero. The reflection
\[
s_\alpha(\mu)=\mu-\mu(H_\alpha)\alpha
\tag{AD.20}
\]
is an orthogonal reflection of \(\mathfrak a^*\) and permutes \(R\). The group \(W_R\) generated by these reflections is finite.

For any unitary \(\mathfrak k\)-module \(W\), write \(W_\mu\) for the common \(\mathfrak a\)-eigenspace of weight \(\mu\). Its weights are real, satisfy \(\mu(H_\alpha)\in\mathbb Z\), and have reflection-invariant multiplicities:
\[
\dim W_\mu=\dim W_{s_\alpha\mu}.
\tag{AD.21}
\]

**Proof.** The subspace
\[
M_{\alpha,\beta}=\bigoplus_{\beta+j\alpha\in R}
\mathfrak g_{\beta+j\alpha}
\tag{AD.22}
\]
is invariant under the \(\alpha\) triple. All its \(H_\alpha\)-eigenvalues have the same parity, because they differ by \(2j\) and are integers by AD.2. Each eigenspace has dimension one by AD.3. An even irreducible string contains weight zero, and an odd one contains weight one. Two strings of the same parity would therefore give multiplicity at least two at that weight. AD.2 consequently makes (AD.22) a single string. Its consecutive weights are symmetric about zero, so the end weights
\(\beta(H_\alpha)-2r\) and \(\beta(H_\alpha)+2q\) sum to zero. This proves (AD.19). Within the string, raising is nonzero except at the upper end; hence the bracket assertion follows whenever \(\alpha+\beta\) exists. The assertion has no omitted proportional case: reducedness excludes a root \(2\alpha\), and \(\alpha+(-\alpha)\) is zero, not a root.

The string symmetry sends \(\beta\) to
\(\beta-(r-q)\alpha=s_\alpha\beta\).
For \(\beta=\pm\alpha\), the same formula interchanges \(\alpha\) and \(-\alpha\). Formula (AD.9) makes (AD.20) the usual reflection perpendicular to \(\alpha\); expansion of its inner product verifies that it is orthogonal and has square one. Thus each reflection permutes the finite set \(R\). The resulting permutation action is faithful because \(R\) spans the space: a linear map fixing each root fixes a basis. Hence \(W_R\) is a subgroup of a finite permutation group.

For the module assertion, the operators \(\rho(H)\), \(H\in\mathfrak a\), are commuting Hermitian operators by (AD.16). AD.1 gives the weight decomposition with real weights, and the rank-one restriction gives the integrality assertion. Fix a weight \(\mu\) and take the sum of spaces whose weights belong to \(\mu+\mathbb Z\alpha\). This sum is invariant under the rank-one triple. On this sum, a weight is determined by its \(H_\alpha\)-eigenvalue, since successive candidates have eigenvalues differing by two. Decompose this sum into rank-one strings by AD.2. Each string has symmetric eigenvalue multiplicities. The weight corresponding to the negative of \(\mu(H_\alpha)\) is exactly \(s_\alpha\mu\); its shift is integral. Summing the string multiplicities proves (AD.21). □

**Lemma AD.5 (simple roots and an element reversing positive roots).** Choose \(\xi\in\mathfrak a^*\) such that \((\xi,\alpha)\ne0\) for every root. Define
\[
R^+=\{\alpha\in R:(\xi,\alpha)>0\}.
\tag{AD.23}
\]
Let \(\Pi\) be the roots in \(R^+\) which are not sums of two members of \(R^+\). Then \(\Pi\) is a basis of \(\mathfrak a^*\). Every positive root is a sum of members of \(\Pi\) with nonnegative integer coefficients. Distinct members of \(\Pi\) have nonpositive inner product. Reflections in members of \(\Pi\) generate \(W_R\). There exists \(w_-\in W_R\) with
\[
w_-(R^+)=R^-=-R^+.
\tag{AD.24}
\]

**Proof.** A suitable \(\xi\) exists because finitely many proper linear hyperplanes do not cover a real vector space. Here is an elementary verification of that fact. For the defining nonzero linear functionals \(\ell_1,\ldots,\ell_N\), choose a vector avoiding the first \(N-1\) kernels by induction. If it is in \(\ker\ell_N\), choose \(u\) with \(\ell_N(u)\ne0\) and vary the vector along \(tu\). Each earlier nonzero affine function has at most one forbidden \(t\), and the last excludes \(t=0\). Choose any other real \(t\).

If a positive root is not in \(\Pi\), split it into two positive roots. Each summand has strictly smaller value against \(\xi\). Repeated splitting terminates, because the finite set of positive root values has no infinite strictly decreasing sequence. This proves the asserted nonnegative integral expansion.

If two distinct simple roots \(\alpha,\beta\) had positive inner product, (AD.19) would give \(r-q>0\), so \(\beta-\alpha\) would be a root. It is either positive or negative. In the first case \(\beta=\alpha+(\beta-\alpha)\) contradicts simplicity of \(\beta\); in the second the corresponding decomposition of \(\alpha\) contradicts simplicity of \(\alpha\). Thus \((\alpha,\beta)\leq0\).

To prove independence, suppose a nonzero real relation among simple roots is separated into its positive and negative coefficients:
\[
x=\sum_{i\in I}a_i\alpha_i
 =\sum_{j\in J}b_j\alpha_j,
\qquad a_i,b_j>0,\quad I\cap J=\varnothing.
\tag{AD.25}
\]
If one side is empty, pairing with \(\xi\) contradicts the positivity on the nonempty side. Otherwise
\(\|x\|^2=\sum_{i,j}a_ib_j(\alpha_i,\alpha_j)\leq0\).
It follows that \(x=0\), again contradicting its positive pairing with \(\xi\). Hence there is no relation. The expansions and the spanning assertion in AD.3 prove that \(\Pi\) is a basis.

Fix a simple root \(\alpha_i\). The reflection \(s_i=s_{\alpha_i}\) sends every positive root other than \(\alpha_i\) to a positive root. Indeed, it changes only the coefficient of \(\alpha_i\) in the simple-root expansion. Such a root has at least one positive coefficient at another simple root, since reducedness excludes a different positive multiple of \(\alpha_i\). Its image is a root by AD.4, and cannot be negative: all coefficients of a negative root are nonpositive, by the already proved expansion applied to its negative. Thus \(s_i\) permutes \(R^+\setminus\{\alpha_i\}\) and sends \(\alpha_i\) to \(-\alpha_i\).

For a positive nonsimple root \(\beta=\sum n_i\alpha_i\), the identity
\(\|\beta\|^2=\sum n_i(\beta,\alpha_i)>0\)
gives an \(i\) with \((\beta,\alpha_i)>0\). The positive integer
\(c=\beta(H_{\alpha_i})\)
makes \(s_i\beta=\beta-c\alpha_i\) a positive root of strictly smaller height \(\sum n_i\). Induction sends every positive root to a simple root by simple reflections. Orthogonal conjugation satisfies
\(u s_\beta u^{-1}=s_{u\beta}\), as follows directly from (AD.20). The reflection in every root is consequently a product of simple reflections. This proves the generating assertion.

Lastly choose \(w\in W_R\) minimizing \((w\xi,\xi)\), possible by finiteness. If \((w\xi,\alpha_i)>0\), then
\[
(s_iw\xi,\xi)
=(w\xi,\xi)
-\frac{2(w\xi,\alpha_i)(\xi,\alpha_i)}{(\alpha_i,\alpha_i)}
<(w\xi,\xi),
\tag{AD.26}
\]
a contradiction. Equality \((w\xi,\alpha_i)=0\) is impossible because \(w^{-1}\alpha_i\) is a root and \(\xi\) is regular. Thus all these pairings are negative. The positive-root expansions imply
\((w\xi,\beta)<0\) for every \(\beta\in R^+\), which is equivalent to \(w^{-1}\beta\in R^-\). There are equally many positive and negative roots, so \(w^{-1}R^+=R^-\) and \(w^{-1}R^-=R^+\). Taking \(w_-=w^{-1}\) proves (AD.24). No assertion about uniqueness of this element is needed here. □

**Lemma AD.6 (highest weights and uniqueness of the irreducible module).** Use the positive roots of AD.5. Let \(W\ne0\) be an irreducible unitary \(\mathfrak k\)-module, extended complex linearly to \(\mathfrak g\). There is a weight \(\lambda\), with one-dimensional space \(W_\lambda=\mathbb Cv_\lambda\), such that every positive root operator kills \(v_\lambda\). The space \(W\) is spanned by words in negative root operators applied to \(v_\lambda\). Every weight has the form
\[
\mu=\lambda-\sum_{\alpha\in R^+}n_\alpha\alpha,
\qquad n_\alpha\in\mathbb Z_{\geq0}.
\tag{AD.27}
\]
The line \(\mathbb Cv_\lambda\) is the full common kernel of all positive root operators. Moreover
\[
\lambda(H_\alpha)\in\mathbb Z_{\geq0}
\quad(\alpha\in R^+).
\tag{AD.28}
\]
Two irreducible unitary modules with the same \(\lambda\) are isomorphic.

If \(\Pi=\{\alpha_1,\ldots,\alpha_r\}\), define \(\omega_j\) by
\(\omega_j(H_{\alpha_i})=\delta_{ij}\). Then
\[
\lambda=\sum_{j=1}^r m_j\omega_j,
\qquad m_j\in\mathbb Z_{\geq0}.
\tag{AD.29}
\]
This is a necessary parametrization of the modules that occur, with uniqueness for each parameter; existence for every parameter is not asserted by this lemma. Finally \(w_-\lambda\), for any \(w_-\) in (AD.24), is a weight of multiplicity one and is a lowest weight: every other weight is it plus a nonnegative integral sum of positive roots.

**Proof.** Choose a weight \(\lambda\) maximizing \((\xi,\lambda)\) among the finite set of weights. If \(X\in\mathfrak g_\alpha\), then
\[
\rho(H)\rho(X)v
=\rho(X)\rho(H)v+\alpha(H)\rho(X)v
\tag{AD.30}
\]
makes \(\rho(X)v\) a vector of weight \(\lambda+\alpha\) for \(v\in W_\lambda\). For positive \(\alpha\) this is incompatible with maximality unless the vector is zero. Thus every vector in this top weight space is killed by all positive root operators. Fix \(v_\lambda\ne0\).

We supply the word-reordering argument. Choose a basis of \(\mathfrak g\) consisting, in this order, of negative root vectors, a basis of \(\mathfrak h\), and positive root vectors; fix an order within each part. Every product of basis operators is a linear combination of ordered products. To prove this, induct first on the word length and then on the number of inverted pairs. For an adjacent inverted pair replace \(XY\) by \(YX+[X,Y]\). The swapped word has one fewer inversion. The bracket is a linear combination of basis vectors, so every resulting bracket word has smaller length and is covered by the first induction. This proves the spanning statement; linear independence of ordered words is not required.

The span of all words applied to \(v_\lambda\) is a nonzero invariant subspace, hence all of \(W\). In an ordered word a positive factor on the right kills \(v_\lambda\); if no such factor occurs, every \(\mathfrak h\) factor on the right acts as its scalar \(\lambda(H)\). Only words in negative root vectors remain. Their weights are exactly of the form (AD.27) when the vectors are nonzero. A nonempty such word strictly lowers the pairing with \(\xi\), so the top weight space is precisely \(\mathbb Cv_\lambda\).

More generally the common kernel \(K\) of the positive root operators is \(\mathfrak h\)-invariant by (AD.30), and splits into weight spaces. For clarity, this last assertion needs no general theorem about invariant subspaces: choose \(H\in\mathfrak a\) separating the finitely many distinct weights, by the finite-hyperplane argument in AD.5. Polynomial spectral projections for \(\rho(H)\) preserve \(K\) and isolate each weight component. Any nonzero weight vector \(u\in K\cap W_\nu\) is cyclic by irreducibility. The same ordered-word argument says that all weights are \(\nu\) minus sums of positive roots. Comparing this assertion for \(\lambda\) and for \(\nu\) and pairing with \(\xi\) gives \(\nu=\lambda\): both differences are positive-root sums, and a nonempty such sum has strictly positive pairing. Therefore \(K=\mathbb Cv_\lambda\).

Restrict to the triple for a positive root \(\alpha\). In the orthogonal string decomposition of AD.2, a vector killed by \(E_\alpha\) is a sum of top vectors, whose \(H_\alpha\)-eigenvalues are nonnegative integers. Since \(v_\lambda\) has the single eigenvalue \(\lambda(H_\alpha)\), (AD.28) follows.

Here is a complete uniqueness argument. Form the tensor algebra \(T(\mathfrak g)=\bigoplus_{d\geq0}\mathfrak g^{\otimes d}\), with concatenation and unit, and quotient by the two-sided ideal generated by
\[
X\otimes Y-Y\otimes X-[X,Y].
\tag{AD.31}
\]
Denote this associative algebra by \(U\). Every Lie representation extends to \(T(\mathfrak g)\) by composing its operators and factors through \(U\). Conversely left multiplication by \(\mathfrak g\) on a left \(U\)-module satisfies the Lie brackets because of (AD.31). These statements follow directly from the definitions.

Let \(I_\lambda\) be the left ideal of \(U\) generated by all positive root vectors and by all \(H-\lambda(H)1\), \(H\in\mathfrak h\), and put \(M_\lambda=U/I_\lambda\) with distinguished vector \(v=1+I_\lambda\). The module \(W\) gives a surjection \(M_\lambda\to W\), sending \(v\) to \(v_\lambda\), so \(v\ne0\). The same reordering argument in \(U\) shows that \(M_\lambda\) is spanned by ordered negative-root words applied to \(v\). Commuting \(H\) through a word shows that it is an eigenvector of weight (AD.27). Thus \(M_\lambda\) is the algebraic direct sum of its weight spaces: any finite collection of distinct weight components can be separated by an \(H\in\mathfrak a\) and its polynomial projections as above, proving their independence. Its weight-\(\lambda\) space is exactly \(\mathbb Cv\).

Every submodule \(N\subset M_\lambda\) splits into its weight components, because each of its vectors is a finite sum and the same finite polynomial projections preserve \(N\). If \(N\) is proper it cannot contain \(v\), which generates \(M_\lambda\). It therefore has zero weight-\(\lambda\) component. The algebraic sum \(J\) of all proper submodules also has zero weight-\(\lambda\) component and is itself proper. It contains every proper submodule and is consequently the unique maximal proper submodule. The kernel of any surjection from \(M_\lambda\) to an irreducible module is maximal proper: a strictly larger proper submodule would give a nonzero proper submodule in the quotient. Such a kernel must equal \(J\). Hence every irreducible module with this highest weight is \(M_\lambda/J\), proving uniqueness. This argument does not invoke linear independence of ordered words or existence of a module for an arbitrary proposed parameter.

The \(H_{\alpha_i}\) form a basis of \(\mathfrak a\), because the simple roots form a basis of its dual and their positive rescalings under the Euclidean identification preserve independence. The dual basis \(\omega_i\) therefore exists, and (AD.28) gives (AD.29).

By AD.4, the multiset of weights is invariant under \(W_R\); hence \(w_-\lambda\) occurs with multiplicity one. For any weight \(\mu\), apply (AD.27) to the weight \(w_-^{-1}\mu\) and then apply \(w_-\). Equation (AD.24) makes each image of a positive root negative, so \(\mu\) is \(w_-\lambda\) plus a nonnegative integral sum of positive roots. This is the stated lowest-weight property. □

**Lemma AD.7 (the factors of an irreducible semisimple representation).** Suppose
\(\mathfrak k=\mathfrak k_1\oplus\cdots\oplus\mathfrak k_s\)
is an orthogonal direct sum of compact centreless ideals, as supplied by AC.3. Every irreducible unitary complex \(\mathfrak k\)-module is a tensor product
\[
W\cong W_1\otimes_{\mathbb C}\cdots\otimes_{\mathbb C}W_s
\tag{AD.32}
\]
of irreducible unitary modules, where \(\mathfrak k_i\) acts on its own factor. Conversely every such tensor product is irreducible. The factors are unique up to isomorphism. Maximal abelian subalgebras can be chosen as sums of maximal abelian subalgebras in the factors; their root sets are disjoint unions, and the highest weight of (AD.32) is the sum of the factor highest weights, each extended by zero on the other factors.

**Proof.** Split \(W\) orthogonally into irreducible \(\mathfrak k_1\)-modules by AD.1, and choose one, denoted \(E\). Put
\[
M=\operatorname{Hom}_{\mathfrak k_1}(E,W).
\tag{AD.33}
\]
In the chosen orthogonal decomposition, the projection to each summand is an intertwiner. AD.1 says that its composition with an element of \(M\) is zero on a summand inequivalent to \(E\), and is a scalar multiple of a fixed isomorphism on an equivalent summand. Those fixed isomorphisms can be made unitary: for an isomorphism \(T\), the positive operator \(T^*T\) commutes with \(\mathfrak k_1\), hence is a positive scalar by AD.1, and rescaling \(T\) suffices. Thus evaluation identifies
\[
E\otimes M\longrightarrow W,\qquad e\otimes T\longmapsto T(e)
\tag{AD.34}
\]
isomorphically with the sum of the summands equivalent to \(E\). Injectivity and surjectivity onto that sum follow explicitly by projecting to each orthogonal summand and comparing its scalar coefficient. Equip \(M\) with the Hermitian product in which these fixed unitary inclusions are an orthonormal basis; evaluation is then unitary for the tensor product inner product.

Every other ideal commutes with \(\mathfrak k_1\) and acts on \(M\) by \(X\cdot T=\rho(X)T\). Consequently the image of (AD.34) is invariant under all of \(\mathfrak k\). Irreducibility makes it all of \(W\). The induced action on \(M\) is unitary, since under the unitary evaluation map the action is \(I_E\otimes\rho_M(X)\) and is skew-adjoint. If \(M\) had a nonzero proper invariant subspace for the remaining ideals, its tensor product with \(E\) would contradict irreducibility of \(W\). Thus \(M\) is irreducible for their sum. Induction proves (AD.32).

For the converse, first consider \(E\otimes F\) with \(E\) irreducible for the first ideal and \(F\) irreducible for the remaining sum. Relative to any orthonormal basis of \(F\), the matrix entries of an operator on \(E\otimes F\) commuting with the first ideal are endomorphisms of \(E\) commuting with it. By AD.1 they are scalars, so the operator is \(I_E\otimes A\). Commuting also with the remaining ideals forces \(A\) scalar. A proper invariant subspace would have an orthogonal projection commuting with all ideals, since its orthogonal complement is invariant; a scalar projection is only zero or the identity. Hence the tensor product is irreducible. Induction proves the general case. The construction also proves uniqueness: restriction to the first ideal recovers its unique irreducible isomorphism type \(E\), and its multiplicity space (AD.33) recovers the remaining representation; continue inductively.

Choose maximal abelian \(\mathfrak t_i\subset\mathfrak k_i\). The centralizer of \(\bigoplus_i\mathfrak t_i\) is the sum of their centralizers, hence exactly that sum by AD.3. Thus it is maximal abelian. The adjoint action on each ideal depends only on its own abelian factor, giving precisely the disjoint union of root sets, each extended by zero elsewhere. Choose positive roots in each factor. Tensoring their highest vectors gives a vector killed by all positive root operators, of weight the sum of the highest weights. Uniqueness of the highest line in AD.6 for the irreducible tensor product proves the last assertion. □

## AE. The finite root-system list

We now determine every root system that can occur in AD.3. Kirillov's free notes, §§7.8 and 7.10, describe the diagram method and its simply laced argument. The coordinate tables in the free Gorodski–Thorbergsson preprint give the exceptional bases used below. We prove the full diagram restriction, including multiple edges, and verify the coordinate models and highest roots.

A **reduced crystallographic root system** in a Euclidean space \(E\) is a finite spanning set \(R\) of nonzero vectors such that each reflection
\[
s_\alpha x=x-\frac{2(x,\alpha)}{(\alpha,\alpha)}\alpha
\tag{AE.1}
\]
permutes \(R\), the numbers \(2(\beta,\alpha)/(\alpha,\alpha)\) are integers for all roots, and the only scalar multiples of a root in \(R\) are that root and its negative. AD.3–AD.4 establish these properties for the compact Lie-algebra roots.

**Lemma AE.1 (diagrams determine roots and their components).** Every such root system has a simple basis \(\Pi=\{\alpha_1,\ldots,\alpha_r\}\), and every root is an image of a simple root under the group generated by their reflections. Use the Cartan convention
\[
a_{ij}=\frac{2(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)},
\qquad
k_{ij}=a_{ij}a_{ji}.
\tag{AE.2}
\]
Thus the denominator belongs to the column. For \(i\ne j\), the entries are nonpositive integers and \(k_{ij}\in\{0,1,2,3\}\). Form a graph with one vertex per simple root, an edge of multiplicity \(k_{ij}\) when it is nonzero, and an arrow on a multiple edge toward the shorter root. This graph determines the root system up to an orthogonal similarity on each connected component. Its components give precisely the orthogonal irreducible components of \(R\).

For the roots of AD.3, these components correspond to simple ideals in \(\mathfrak g\), stable under compact conjugation. In particular the root diagram of a compact simple real Lie algebra is connected.

**Proof.** The simple-basis proof in AD.5 applies to these axioms once its root-difference step is justified. If nonproportional roots \(\alpha,\beta\) have positive inner product, the two positive integers
\[
p=\frac{2(\alpha,\beta)}{(\alpha,\alpha)},\qquad
q=\frac{2(\alpha,\beta)}{(\beta,\beta)}
\]
have product \(4\cos^2\angle(\alpha,\beta)<4\). One of \(p,q\) is therefore one. Reflecting in the corresponding root makes either \(\beta-\alpha\) or \(\alpha-\beta\) a root; the negative is also a root because \(s_\gamma\gamma=-\gamma\). This is exactly the difference fact used in AD.5. Choose a regular vector by that lemma's finite-hyperplane argument. Splitting decomposable positive roots terminates by decreasing positive values against it. Distinct indecomposable roots have nonpositive inner product by the difference fact. The positive-and-negative separation of a hypothetical linear relation, as in (AD.25), proves independence; the expansions prove spanning. Thus the same proof supplies a simple basis and nonnegative integral expansions.

The remainder of AD.5's descent uses only these expansions, reflection preservation and integrality: reflection in a simple root preserves all positive roots other than itself; a positive nonsimple root \(\beta=\sum n_i\alpha_i\) has \((\beta,\alpha_i)>0\) for some \(i\), and that reflection strictly decreases \(\sum n_i\). Induction reaches a simple root. This proves the orbit assertion for the present abstract axioms as well.

For distinct simple roots, their nonpositive inner product and integrality give \(a_{ij},a_{ji}\leq0\). Independence makes their angle different from zero and \(\pi\), so
\[
k_{ij}=4\cos^2\angle(\alpha_i,\alpha_j)<4.
\tag{AE.3}
\]
Zero occurs in both positions together. Otherwise the integer pair, in the order long root then short root, is \((-1,-1)\), \((-2,-1)\) or \((-3,-1)\). The multiplicity and arrow consequently recover every entry in (AE.2).

If two simple bases have equal Cartan matrices, the linear map \(T\) between the bases intertwines their simple reflections, since
\[
s_i(\alpha_j)=\alpha_j-a_{ji}\alpha_i.
\tag{AE.4}
\]
The orbit assertion then gives \(T(R)=R'\). Along each edge, the ratio of squared lengths is \(a_{ij}/a_{ji}\); hence the Gram matrices differ by one positive scalar on a connected component. Their zero cross-component entries show that \(T\) is a similarity on each component, as asserted.

Partition the simple roots by graph components. Their spans are orthogonal, and the reflections of one component fix the others. The orbit assertion puts every root in exactly one such span. Each resulting set is a root system and cannot split further: an orthogonal splitting would partition its simple roots with no edges between the parts. This also shows that any orthogonal irreducible decomposition has these same components.

For the compact algebra let \(R_j\) be a component, let \(\mathfrak h_j\) be the complex span of its dual vectors \(T_\alpha\), and set
\[
\mathfrak g_j=\mathfrak h_j\oplus
\bigoplus_{\alpha\in R_j}\mathfrak g_\alpha.
\tag{AE.5}
\]
These subspaces sum directly to \(\mathfrak g\). The bracket rule (AD.14), the opposite-root bracket (AD.15), and the orthogonality of components prove that each is an ideal and that different ones commute. Indeed a sum of roots from different components cannot be a root, because every root lies in a single component span. Conjugation sends each root space to its negative and sends \(\mathfrak h_j\) to itself, so each ideal is \(\sigma\)-stable.

To prove simplicity of \(\mathfrak g_j\), let \(I\ne0\) be a complex ideal in it. Choose \(H\in\mathfrak a\) which separates its finitely many root weights and zero. Polynomial projections in \(\operatorname{ad}H\), as in AD.6, show that \(I\) contains a nonzero root vector or a nonzero vector \(Z\in\mathfrak h_j\). In the latter case some \(\alpha(Z)\ne0\), since the component roots span the dual of \(\mathfrak h_j\); bracketing with \(\mathfrak g_\alpha\) supplies a root vector. One-dimensionality of root spaces then gives \(\mathfrak g_\alpha\subset I\), and bracketing with its opposite gives \(H_\alpha\in I\).

Some simple root \(\beta\) has \((\alpha,\beta)\ne0\), since the simple roots span the component. Bracketing \(H_\alpha\) with both \(\mathfrak g_\beta\) and \(\mathfrak g_{-\beta}\) puts both spaces and then \(H_\beta\) in \(I\). Repeat across every edge of the connected simple graph. All simple coroots enter \(I\), so \(\mathfrak h_j\subset I\). Every root evaluates nontrivially on some element of this Cartan space; another bracket then puts every root space in \(I\). Thus \(I=\mathfrak g_j\).

The fixed real spaces \(\mathfrak k_j=\mathfrak g_j^\sigma\) sum to \(\mathfrak k\). Each has complexification \(\mathfrak g_j\): write \(X=(X+\sigma X)/2+i(X-\sigma X)/(2i)\). A nonzero proper real ideal would complexify to a nonzero proper complex ideal, which has just been excluded. These are the asserted simple ideals, and a simple \(\mathfrak k\) has only one component. □

**Theorem AE.2 (restrictions on connected diagrams).** Every connected root diagram belongs to the following list:

| Type | Underlying graph and edge lengths |
|---|---|
| \(A_n,\ n\geq1\) | A chain of \(n\) vertices, all edges single |
| \(B_n,\ n\geq2\) | A chain with a double edge at one end; the singleton end is short |
| \(C_n,\ n\geq3\) | A chain with a double edge at one end; the singleton end is long |
| \(D_n,\ n\geq4\) | One branch with three single-edge arms of lengths \(1,1,n-3\) |
| \(E_6,E_7,E_8\) | One branch with single-edge arm lengths \(1,2,2\), \(1,2,3\), \(1,2,4\) |
| \(F_4\) | A four-vertex chain with its middle edge double |
| \(G_2\) | Two vertices joined by a triple edge |

Arm lengths count edges from the branch. Reversing all labels identifies the two drawings of \(F_4\) and of \(G_2\). At rank two, the \(B_2,C_2\) descriptions are the same diagram after exchanging vertices. The coordinate constructions in AE.3–AE.5 will establish occurrence.

**Proof.** Let \(u_i=\alpha_i/\|\alpha_i\|\). Twice their Gram matrix has entries
\[
Q_{ii}=2,\qquad Q_{ij}=-\sqrt{k_{ij}}\quad(i\ne j),
\tag{AE.6}
\]
and is positive definite. The same holds on every subset of its vertices.

There can be no cycle. Put coefficient one at every vertex of a cycle and zero elsewhere. A cycle with \(m\) vertices contributes \(2m\) on the diagonal and at most \(-2m\) from its edges; any additional internal edges only decrease this value. This contradicts positivity. Thus the graph is a tree.

The neighbours of a vertex are now pairwise orthogonal. The orthogonal projection of its unit vector onto their span has squared norm
\[
\frac14\sum_{j\sim i}k_{ij}<1.
\tag{AE.7}
\]
The inequality is strict because the simple roots are independent. Since the sum is an integer, it is at most three. A vertex has at most three neighbours; a vertex with three neighbours has only single edges. An endpoint of a triple edge has no other neighbour, so a connected graph containing a triple edge is \(G_2\).

There is at most one branching vertex. Otherwise take a shortest path between two branching vertices, put coefficient two at its \(m\) vertices, and coefficient one at two additional neighbours of each endpoint. The four additional vertices are distinct, by the absence of cycles. The quadratic value on this set is at most
\[
(8m+8)-8(m-1)-16=0.
\tag{AE.8}
\]
Here the three terms are the diagonal, the path edges and the four extra edges. This is impossible.

Two double edges are likewise impossible. Choose a path whose first and last edges are double and whose intervening edges are single. Adjacent double edges already contradict (AE.7). Put coefficient one at the two outer endpoints and coefficient \(\sqrt2\) at every interior vertex. For \(m\) path vertices the value is
\[
(4m-4)-8-4(m-3)=0.
\tag{AE.9}
\]
A branch and a double edge cannot coexist either. Take the path from the branch through the first double edge to its far endpoint. Put coefficient two at the \(m\) vertices before that endpoint, coefficient \(\sqrt2\) at the far endpoint, and coefficient one at two other neighbours of the branch. The value is
\[
(8m+8)-8(m-1)-8-8=0.
\tag{AE.10}
\]
All these are contradictions to positive definiteness.

It remains to bound the three arm lengths of one branch or the position of one double edge. Let \(T_l\) be the \(l\)-vertex chain matrix with diagonal two and adjacent entries \(-1\). Direct expansion gives
\[
x^tT_lx=x_1^2+x_l^2+\sum_{i=1}^{l-1}(x_i-x_{i+1})^2>0
\quad(x\ne0).
\tag{AE.11}
\]
For \(l=1\), the two endpoint terms mean \(2x_1^2\). The solution of \(T_lz=e_1\) is \(z_i=(l+1-i)/(l+1)\), obtained by substituting in its endpoint and interior equations. Therefore
\[
(T_l^{-1})_{11}=\frac{l}{l+1}.
\tag{AE.12}
\]
The elimination used here requires only completing the square: for a positive definite \(B\),
\[
d t^2+2t b^ty+y^tBy
=(y+B^{-1}bt)^tB(y+B^{-1}bt)
 +(d-b^tB^{-1}b)t^2.
\tag{AE.13}
\]

For single-edge arms of lengths \(1\leq p\leq q\leq r\), eliminate the three positive chain blocks. Positivity of the remaining central coefficient is exactly
\[
\begin{gathered}
2-\frac{p}{p+1}-\frac{q}{q+1}-\frac{r}{r+1}>0,\\
\text{equivalently}\qquad
\frac1{p+1}+\frac1{q+1}+\frac1{r+1}>1.
\end{gathered}
\tag{AE.14}
\]
If \(p\geq2\), the sum is at most one. Thus \(p=1\). For \(q=1\), every \(r\geq1\) works, giving \(D_{r+3}\). For \(q\geq3\), the sum is at most \(1/2+1/4+1/4=1\). For \(q=2\), the remaining inequality is \(r<5\), giving precisely \(E_6,E_7,E_8\).

A double edge lies in a chain. Removing it leaves chains with \(p,q\geq1\) vertices. Eliminate the first chain. The second quadratic form becomes
\[
y^tT_qy-\frac{2p}{p+1}y_1^2.
\tag{AE.15}
\]
Let \(u=T_q^{-1}e_1\) and \(a=u_1=q/(q+1)>0\). Write \(y=t u+z\) with \(z_1=0\), where \(t=y_1/a\). Since \(u^tT_qz=z_1=0\), (AE.15) equals
\[
z^tT_qz+t^2a\left(1-\frac{2p}{p+1}a\right).
\]
It is positive for all nonzero \(y\) exactly when
\[
1-\frac{2pq}{(p+1)(q+1)}>0,
\quad\text{equivalently}\quad
(p-1)(q-1)<2.
\tag{AE.16}
\]
The possibilities are \(p=1\), \(q=1\), or \(p=q=2\). They give \(B_n,C_n,F_4\) with the length orientations stated in the table. A tree with neither a branch nor a multiple edge is \(A_n\). This proves necessity, with all equality cases excluded. The coordinate constructions that follow prove occurrence, rather than inferring it from positive definiteness alone. □

**Lemma AE.3 (classical root coordinates and fundamental weights).** Use the rank ranges in AE.2, and let the \(e_i\) be orthonormal. The classical systems and simple bases are as follows:
\[
\begin{gathered}
A_n:\quad R=\{e_i-e_j:i\ne j\},\\
E=\{x\in\mathbb R^{n+1}:\textstyle\sum x_i=0\},
\qquad \alpha_i=e_i-e_{i+1}\quad(1\leq i\leq n).
\end{gathered}
\tag{AE.17a}
\]
\[
\begin{gathered}
B_n:\quad R=\{\pm e_i,\ \pm e_i\pm e_j:i<j\}\subset\mathbb R^n,\\
\alpha_i=e_i-e_{i+1}\quad(i<n),\qquad \alpha_n=e_n.
\end{gathered}
\tag{AE.17b}
\]
\[
\begin{gathered}
C_n:\quad R=\{\pm2e_i,\ \pm e_i\pm e_j:i<j\}\subset\mathbb R^n,\\
\alpha_i=e_i-e_{i+1}\quad(i<n),\qquad \alpha_n=2e_n.
\end{gathered}
\tag{AE.17c}
\]
\[
\begin{gathered}
D_n:\quad R=\{\pm e_i\pm e_j:i<j\}\subset\mathbb R^n,\\
\alpha_i=e_i-e_{i+1}\quad(i<n),\qquad \alpha_n=e_{n-1}+e_n.
\end{gathered}
\tag{AE.17d}
\]
Their root counts are respectively \(n(n+1)\), \(2n^2\), \(2n^2\), and \(2n(n-1)\). Put \(s_i=e_1+\cdots+e_i\). The fundamental weights, dual to the simple coroots as in AD.6, are
\[
\begin{aligned}
A_n:&\quad \omega_i=s_i-\frac{i}{n+1}s_{n+1};\\
B_n:&\quad \omega_i=s_i\ (i<n),\quad \omega_n=\tfrac12s_n;\\
C_n:&\quad \omega_i=s_i\ (i\leq n);\\
D_n:&\quad \omega_i=s_i\ (i\leq n-2),\\
&\quad \omega_{n-1}=\tfrac12(s_{n-1}-e_n),\quad
\omega_n=\tfrac12s_n .
\end{aligned}
\tag{AE.18}
\]
For \(A_n\) the reflection group consists of all coordinate permutations. For \(B_n,C_n\) it consists of all signed permutations; for \(D_n\) it consists of signed permutations with an even number of sign changes. An element reversing all positive roots is, respectively: coordinate reversal for \(A_n\); \(-I\) for \(B_n,C_n\); and for \(D_n\), \(-I\) when \(n\) is even, or negation of the first \(n-1\) coordinates when \(n\) is odd.

**Proof.** Reflection in \(e_i-e_j\) swaps coordinates \(i,j\). Reflection in \(e_i+e_j\) swaps and negates those coordinates; reflection in \(e_i\) or \(2e_i\) changes just that sign. These formulas follow by substituting in (AE.1), and prove reflection preservation of every displayed set. The sets are reduced by their explicit supports and lengths. Cartan integrality follows from the coroots: the coroot of \(e_i\) is \(2e_i\), that of \(2e_i\) is \(e_i\), and that of \(e_i\pm e_j\) is itself. In \(A_n\), all coroots are difference roots. Every pairing with the appropriate displayed roots is an integer.

The first \(n\) difference roots in \(A_n\) are independent and span the coordinate-sum-zero hyperplane, as can be seen by solving their coefficients successively from the first coordinate. For \(B_n,C_n\), the differences span that hyperplane in \(\mathbb R^n\), and the last root has nonzero coordinate sum. For \(D_n\) the same argument uses the last root's coordinate sum two. Thus the displayed vectors are bases of the stated spaces.

For \(A_n\), every positive difference with \(i<j\) is \(\alpha_i+\cdots+\alpha_{j-1}\). For \(B_n\), the identities
\[
e_i=\sum_{k=i}^{n}\alpha_k,\qquad
e_i+e_j=\sum_{k=i}^{j-1}\alpha_k+2\sum_{k=j}^{n}\alpha_k
\quad(i<j)
\tag{AE.19}
\]
give all positive axial and sum roots. For \(C_n\), use
\[
2e_i=2\sum_{k=i}^{n-1}\alpha_k+\alpha_n,\qquad
e_i+e_j=\sum_{k=i}^{j-1}\alpha_k+
2\sum_{k=j}^{n-1}\alpha_k+\alpha_n.
\tag{AE.20}
\]
For \(D_n\),
\[
e_i+e_j=
\begin{cases}
\displaystyle\sum_{k=i}^{j-1}\alpha_k+
2\sum_{k=j}^{n-2}\alpha_k+\alpha_{n-1}+\alpha_n,&j<n,\\
\displaystyle\sum_{k=i}^{n-2}\alpha_k+\alpha_n,&j=n.
\end{cases}
\tag{AE.21}
\]
Difference roots have the consecutive-sum expression in all four cases. Empty sums are zero. These formulas and their negatives express every root with coefficients of one sign. They identify the displayed bases as simple bases: choose a vector pairing positively with each basis vector. All displayed basis roots are positive; a decomposition of one into two positive roots would split its unit coefficient vector into two nonzero nonnegative integral vectors, which is impossible. Any other positive root is not an additional simple root, since AE.1 says the indecomposable positive roots form a basis and already include the displayed basis.

Their inner products give the indicated diagrams: only consecutive roots pair in \(A,B,C\), with the last edge doubled in \(B,C\). In \(D_n\), both roots \(n-1,n\) pair with \(n-2\) and are orthogonal to each other. Counting ordered differences, axes and the four sign choices for each pair gives the stated root counts.

Substitution of each vector in (AE.18) into
\[
\frac{2(\omega_i,\alpha_j)}{(\alpha_j,\alpha_j)}=\delta_{ij}
\tag{AE.22}
\]
verifies the fundamental weights. For instance the difference coroots test consecutive-coordinate jumps; the last coroot is \(2e_n\) in \(B_n\), \(e_n\) in \(C_n\), and \(e_{n-1}+e_n\) in \(D_n\). In \(A_n\), subtracting the common coordinate \(i/(n+1)\) both preserves those jumps and imposes coordinate sum zero. This verifies all entries of the formulas.

Consecutive swaps generate any permutation: move its desired first entry into the first position by consecutive swaps and induct on the remaining positions. These swaps are the difference-root reflections. The axial reflections in \(B,C\) give every individual sign change. In \(D\), a sum-root reflection followed by the corresponding difference-root reflection changes exactly two signs; pairing up the negative positions gives every even sign pattern. Every generating reflection in \(D\) has an even number of sign changes, so no other patterns occur. This proves the group descriptions. Lastly substitute the displayed reversing maps into the positive differences, sums and axes described by (AE.19)–(AE.21). Every positive root becomes negative. In the odd \(D_n\) case a root involving \(e_n\) becomes \(-e_i\pm e_n=-(e_i\mp e_n)\); the others have both signs reversed. The proposed map belongs to the group because \(n-1\) is even. □

**Lemma AE.4 (the three exceptional simply laced systems).** In \(\mathbb R^8\), let
\[
\begin{gathered}
L_0=\{d\in\mathbb Z^8:\textstyle\sum d_i\ \text{is even}\},\qquad
h=\tfrac12(1,\ldots,1),\\
L=L_0\cup(L_0+h),\qquad R_8=\{x\in L:\|x\|^2=2\}.
\end{gathered}
\tag{AE.23}
\]
The set \(R_8\) is a root system of type \(E_8\). Explicitly it consists of
\[
\{\pm e_i\pm e_j:i<j\}
\quad\text{and}\quad
\{\tfrac12(\varepsilon_1,\ldots,\varepsilon_8):
\varepsilon_i=\pm1,\ \textstyle\prod_i\varepsilon_i=1\}.
\tag{AE.24}
\]
A simple basis is
\[
\begin{aligned}
\alpha_1&=\tfrac12(e_1+e_8-e_2-e_3-e_4-e_5-e_6-e_7),\\
\alpha_2&=e_1+e_2,\qquad \alpha_3=e_2-e_1,\\
\alpha_4&=e_3-e_2,\qquad \alpha_5=e_4-e_3,\\
\alpha_6&=e_5-e_4,\qquad \alpha_7=e_6-e_5,\qquad
\alpha_8=e_7-e_6.
\end{aligned}
\tag{AE.25}
\]
The intersections
\[
R_7=R_8\cap\{x:x_7=-x_8\},\qquad
R_6=R_8\cap\{x:x_6=x_7=-x_8\}
\tag{AE.26}
\]
are of types \(E_7,E_6\), with simple bases the first seven or six vectors in (AE.25). Their root counts are
\[
|R_6|=72,\qquad |R_7|=126,\qquad |R_8|=240.
\tag{AE.27}
\]

**Proof.** The set \(L\) is an additive group: \(L_0\) is one, \(2h\in L_0\), and \(-h=h-2h\). Its dot products are integers, since those on \(L_0\) are integers,
\((h,d)=\sum d_i/2\in\mathbb Z\), and \((h,h)=2\).
Every squared norm in \(L\) is even. For \(d\in L_0\) use \(d_i^2\equiv d_i\pmod2\); for \(d+h\) use
\[
\|d+h\|^2=\sum_i d_i(d_i+1)+2.
\tag{AE.28}
\]
A norm-two integral vector has two nonzero coordinates, each \(\pm1\), giving \(4\binom82=112\) roots. A half-integral vector has every absolute coordinate at least \(1/2\); norm two forces equality in all eight places. Subtracting \(h\) shows that membership in \(L\) is exactly even minus parity, giving \(2^7=128\) half roots. This proves (AE.24) and the count 240.

For \(\alpha\in R_8\), the reflection is \(x\mapsto x-(x,\alpha)\alpha\). It preserves \(L\), by integral dot products, and preserves the norm; hence it permutes \(R_8\). The same integral products give Cartan integrality. All roots have squared norm two, so the system is reduced. It spans because the difference roots span the coordinate-sum-zero hyperplane and, for example, \(e_1+e_2\) is outside that hyperplane. Thus all axioms are verified.

Every vector in (AE.25) belongs to \(R_8\). The coefficients of \(x=\sum n_i\alpha_i\), solved successively from its coordinates, are
\[
\begin{aligned}
n_1&=2x_8,&n_8&=x_7+x_8,\\
n_7&=x_6+x_7+2x_8,&
n_6&=x_5+x_6+x_7+3x_8,\\
n_5&=x_4+x_5+x_6+x_7+4x_8,&
n_4&=x_3+x_4+x_5+x_6+x_7+5x_8,\\
n_2&=(x_1+x_2+n_4)/2,&
n_3&=(-x_1+x_2+n_4+2x_8)/2.
\end{aligned}
\tag{AE.29}
\]
Substitution in (AE.25) verifies the solution and proves independence. These coefficients are integers on \(L\). Indeed \(S=\sum x_i\) is an even integer there. The numerators for \(n_2,n_3\) are respectively \(S+4x_8\) and \(S-2x_1+6x_8\), which are even integers whether all coordinates are integral or half integral. The other formulas visibly have an even total number of half-coordinate contributions.

We check signs for every root, not merely for the basis vectors. If \(x_8\ne0\), choose the root's sign so \(x_8>0\). An integral root then has \(x_8=1\) and only one further nonzero coordinate \(\pm1\). Each expression in (AE.29) is nonnegative. A half root has \(x_8=1/2\). All expressions except possibly \(n_2\) have lower bound zero, using \(-1/2\leq x_i\leq1/2\); the lower bound for \(n_2\) is \(-1/2\), and its integrality improves that bound to zero. If \(x_8=0\), the root is integral on the first seven coordinates. Choose its greatest-index nonzero coordinate positive. Every tail sum in \(n_4,\ldots,n_8\) is then nonnegative: the only possible other nonzero coordinate is earlier and has size one. For \(n_2,n_3\), either both supported coordinates are among the first two, giving directly the values zero or one, or their tail contribution gives those same nonnegative values. Thus every root expansion has coefficients of one sign. The indecomposability argument in AE.3 proves that (AE.25) is the simple basis.

All simple roots have squared norm two. Their only nonzero off-diagonal products are \(-1\) along
\[
1-3-4-5-6-7-8,\qquad 2-4.
\tag{AE.30}
\]
This follows by taking the coordinate products in (AE.25). The branch is vertex four, with arm lengths \(1,2,4\), so this is \(E_8\).

Equation (AE.29) shows that \(n_8=0\) is the first subspace in (AE.26), and \(n_7=n_8=0\) is the second. Thus they are exactly the spans of the proposed truncated bases. Their intersection root sets inherit reflection preservation, since reflection in a vector of a subspace preserves that subspace. They inherit reducedness and integral Cartan numbers and are spanned by their simple roots. The already established one-sign expansions have their last one or two coefficients zero, so the truncated bases are simple. Their graphs have arm lengths \(1,2,3\) and \(1,2,2\).

For \(R_7\), the integral roots are the 60 two-coordinate roots on the first six coordinates and the two roots \(\pm(e_7-e_8)\). A half root has opposite last signs. For either of these two sign choices, the first six must have odd minus parity, giving \(2^5\) choices. Therefore \(|R_7|=60+2+64=126\).
For \(R_6\), the integral roots are the 40 two-coordinate roots on the first five coordinates. The last three signs of a half root are \((-,-,+)\) or \((+,+,-)\). In each case exactly half of the \(2^5\) first-five sign choices have the required total parity. Hence \(|R_6|=40+16+16=72\). This proves all assertions. □

**Lemma AE.5 (the remaining exceptional systems).** In \(\mathbb R^4\) put
\[
\begin{aligned}
R(F_4)={}&\{\pm e_i\pm e_j:i<j\}\ \cup\ \{\pm e_i\}\\
&{}\cup\{\tfrac12(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4):
\varepsilon_i=\pm1\}.
\end{aligned}
\tag{AE.31}
\]
It has 48 roots and simple basis
\[
\alpha_1=e_2-e_3,\quad \alpha_2=e_3-e_4,\quad
\alpha_3=e_4,\quad
\alpha_4=\tfrac12(e_1-e_2-e_3-e_4).
\tag{AE.32}
\]
Its fundamental weights are
\[
\begin{aligned}
\omega_1&=e_1+e_2,&\omega_2&=2e_1+e_2+e_3,\\
\omega_3&=\tfrac12(3e_1+e_2+e_3+e_4),&
\omega_4&=e_1 .
\end{aligned}
\tag{AE.33}
\]
In the coordinate-sum-zero plane of \(\mathbb R^3\), the twelve vectors
\[
R(G_2)=\{e_i-e_j:i\ne j\}\ \cup\
\{\pm(2e_i-e_j-e_k):\{i,j,k\}=\{1,2,3\}\}
\tag{AE.34}
\]
form a root system with simple roots
\(\alpha_1=e_1-e_2\), \(\alpha_2=-2e_1+e_2+e_3\).
Its positive roots and fundamental weights are
\[
\begin{gathered}
R^+=\{\alpha_1,\alpha_2,\alpha_1+\alpha_2,
2\alpha_1+\alpha_2,3\alpha_1+\alpha_2,3\alpha_1+2\alpha_2\},\\
\omega_1=2\alpha_1+\alpha_2,\qquad
\omega_2=3\alpha_1+2\alpha_2 .
\end{gathered}
\tag{AE.35}
\]
Together with AE.3–AE.4, these constructions realize every diagram allowed by AE.2, completing the classification of reduced crystallographic root systems.

**Proof.** For \(F_4\), the three disjoint parts have respectively 24, 8 and 16 elements. Their squared norms are two, one and one, so spanning and reducedness follow from the explicit vectors. Signed coordinate permutations preserve the set and include all reflections in axial and two-coordinate roots. Every half-root reflection is a signed-coordinate conjugate of reflection in \(v=(1,1,1,1)/2\), namely
\[
s_vx=x-\tfrac12\left(\sum_i x_i\right)(1,1,1,1).
\tag{AE.36}
\]
This takes an axial root to a half root. It fixes a two-coordinate root with coordinate sum zero; when that sum is \(2\) or \(-2\), the result is a two-coordinate root on the complementary pair of positions. For a half root, count its minus signs. Zero or four minus signs give its negative, one or three give an axial root, and two give a fixed root. Thus all reflections preserve the set.

The coroots of axial roots are \(\pm2e_i\), those of two-coordinate roots are the same vectors, and those of half roots are four-sign vectors \((\varepsilon_i)\). Each pairs integrally with (AE.31): in the only less immediate case, pairing a four-sign vector with a half root is half a sum of four signs, an integer. The axioms follow.

Solving \(x=\sum n_i\alpha_i\) in (AE.32) gives
\[
\begin{aligned}
n_4&=2x_1,&n_1&=x_2+x_1,\\
n_2&=x_3+x_2+2x_1,&n_3&=x_4+x_3+x_2+3x_1.
\end{aligned}
\tag{AE.37}
\]
These equations prove independence and integral coefficients for every displayed root. If \(x_1\ne0\), choose \(x_1>0\). For an integral root \(x_1=1\) and at most one further coordinate is nonzero; for a half root \(x_1=1/2\). Both cases give nonnegative coefficients in (AE.37). If \(x_1=0\), choose the first nonzero coordinate among \(x_2,x_3,x_4\) positive. Their successive partial sums are nonnegative, since there are at most two nonzero entries, of absolute value one. Thus all root expansions have one sign, and AE.3's indecomposability argument proves the simple-basis assertion.

The only edges are \(1-2\), \(2-3\), \(3-4\). Their multiplicities are one, two and one; roots 1 and 2 have squared norm two, roots 3 and 4 squared norm one. This is \(F_4\), with arrow toward vertex 3. Pairing (AE.33) with the four simple coroots verifies (AE.22), proving the fundamental-weight formulas.

For \(G_2\), the six difference roots have squared norm two and the six remaining roots squared norm six. They span the plane and are reduced. Difference reflections permute coordinates. Let \(l_i=2e_i-e_j-e_k\). On the sum-zero plane, \((x,l_i)=3x_i\), so reflection in \(l_i\) sends its three coordinates, in the order \(i,j,k\), to
\[
(-x_i,-x_k,-x_j).
\tag{AE.38}
\]
This also preserves both displayed sets. The difference coroots are the difference vectors themselves. The long coroot is \(l_i/3\); it pairs with \(e_j-e_k\) as \(\delta_{ij}-\delta_{ik}\), and with \(l_j\) as \(3\delta_{ij}-1\). Thus all Cartan integers are integral.

The two proposed simple roots are independent, with squared norms two and six and inner product \(-3\). Expanding the six roots in (AE.35) in coordinates gives exactly one root from each opposite pair of (AE.34); their negatives give the other six. Their coefficients are nonnegative integers, so they are a simple basis by the same indecomposability argument. The Cartan matrix in convention (AE.2) is
\[
\begin{pmatrix}2&-1\\-3&2\end{pmatrix},
\tag{AE.39}
\]
which is \(G_2\) with arrow toward the first root. Multiplying the coefficients of the two proposed weights by the coroot-pairing matrix verifies their fundamental-weight equations.

There are no further identifications among the root systems in the stated rank ranges. Rank, root count and the counts at each length distinguish them. For the simply laced classical families, \(n(n+1)=2n(n-1)\) only at \(n=3\), which is outside the range for \(D_n\). The exceptional simply laced counts in AE.4 differ from the classical simply laced counts at the same ranks. The coincidence of the \(E_6\) count with \(B_6,C_6\) causes no identification because only the latter have two root lengths. Types \(F_4,G_2\) have different counts from all other systems at their ranks. Finally, \(B_n\) has \(2n\) short roots and \(2n(n-1)\) long roots, whereas \(C_n\) has those counts reversed. They differ for \(n\geq3\); their rank-two diagrams were already identified in AE.2. This proves both occurrence and uniqueness of the listed root-system types. □

**Lemma AE.6 (highest roots and adjoint weights).** For the bases above, every irreducible root system has a highest root \(\theta\): a positive root such that \(\theta-\beta\) is a nonnegative integral sum of simple roots for every positive root \(\beta\). It is unique. For the \(E_6\) row, abbreviate
\[
v_6=\tfrac12(e_1+e_2+e_3+e_4+e_5-e_6-e_7+e_8).
\tag{AE.39a}
\]
The following are the exact vectors and their simple-root coefficients:

| Type | Highest root \(\theta\) | Coefficient vector |
|---|---|---|
| \(A_n\) | \(e_1-e_{n+1}\) | \((1,\ldots,1)\) |
| \(B_n\) | \(e_1+e_2\) | \((1,2,\ldots,2)\) |
| \(C_n\) | \(2e_1\) | \((2,\ldots,2,1)\) |
| \(D_n\) | \(e_1+e_2\) | \((1,2,\ldots,2,1,1)\) |
| \(E_6\) | \(v_6\) | \((1,2,2,3,2,1)\) |
| \(E_7\) | \(e_8-e_7\) | \((2,2,3,4,3,2,1)\) |
| \(E_8\) | \(e_7+e_8\) | \((2,3,4,6,5,4,3,2)\) |
| \(F_4\) | \(e_1+e_2\) | \((2,3,4,2)\) |
| \(G_2\) | \(3\alpha_1+2\alpha_2\) | \((3,2)\) |

For a compact simple algebra with this root system, its complex adjoint module is irreducible, has highest weight \(\theta\), has zero-weight multiplicity \(r\), and has multiplicity one at every root. Its complex dimension is \(r+|R|\).

**Proof.** Each proposed vector belongs to its coordinate root set. Substitution in (AE.19)–(AE.21), (AE.29), (AE.37), or (AE.35) gives the displayed coefficients. We verify that those coefficients dominate every positive root.

For \(A_n\), all positive roots are consecutive sums, with coefficients zero or one. In \(B_n\), the axial, difference and sum formulas in AE.3 have first coefficient at most one and all subsequent coefficients at most two. For \(C_n\), those formulas have coefficients at most two except at the last position, where the bound is one. Formula (AE.21) bounds the first and both fork-end coefficients in \(D_n\) by one, and all others by two.

For \(E_8\), a positive integral root with \(x_8=1\) has only one further coordinate \(\pm1\). In (AE.29) this bounds \(n_1,\ldots,n_8\) by
\[
(2,3,4,6,5,4,3,2).
\tag{AE.40}
\]
If \(x_8=0\), the tail sums \(n_4,\ldots,n_8\) are at most two, and \(n_2,n_3\leq1\); all are within (AE.40). For a positive half root, substitute \(x_8=1/2\) and \(-1/2\leq x_i\leq1/2\) into (AE.29). In order, the bounds are
\[
(1,3,3,5,4,3,2,1).
\tag{AE.41}
\]
For \(n_3\), the direct real upper bound is \(7/2\), improved to three by integrality; the other entries follow directly. These bounds too are within (AE.40).

For \(E_7\), a positive integral root with nonzero \(x_8\) is \(e_8-e_7\) itself. The other integral roots lie on the first six coordinates. In (AE.29) they have \(n_1=0\), \(n_2,n_3\leq1\), the middle tail sums at most two, and \(n_7=x_6\leq1\). A positive half root has \(x_8=1/2\), \(x_7=-1/2\), and
\[
\begin{aligned}
n_7&=x_6+x_8\leq1,&
n_6&=x_5+x_6+2x_8\leq2,\\
n_5&=x_4+x_5+x_6+3x_8\leq3,&
n_4&=x_3+x_4+x_5+x_6+4x_8\leq4.
\end{aligned}
\tag{AE.42}
\]
Also \(n_1=1\), \(n_2\leq\lfloor(1+4)/2\rfloor=2\), and
\(n_3\leq(1+4+1)/2=3\). These prove the \(E_7\) row.

For \(E_6\), the integral roots lie on the first five coordinates, giving \(n_1=0\), \(n_2,n_3\leq1\), \(n_4,n_5\leq2\), and \(n_6\leq1\). A positive half root has \(x_6=x_7=-x_8=-1/2\), so
\[
\begin{aligned}
n_6&=x_5+x_8\leq1,\\
n_5&=x_4+x_5+2x_8\leq2,\\
n_4&=x_3+x_4+x_5+3x_8\leq3.
\end{aligned}
\tag{AE.43}
\]
Here \(n_1=1\), \(n_2\leq(1+3)/2=2\), and
\(n_3\leq\lfloor(1+3+1)/2\rfloor=2\). These are the required bounds.

For \(F_4\), a positive root with \(x_1=1\) has at most one further nonzero coordinate, of size one. Formula (AE.37) then bounds \((n_1,n_2,n_3,n_4)\) by \((2,3,4,2)\). A half root has \(x_1=1/2\) and gives the smaller bounds \((1,2,3,1)\). For \(x_1=0\), the first three partial sums are at most two and \(n_4=0\). Finally, inspection of the six explicitly proved positive roots in (AE.35) gives the \(G_2\) bounds.

Thus each proposed \(\theta\) dominates every positive root. Two highest roots would dominate one another, forcing equality in every coefficient, so the highest root is unique.

For the adjoint assertion, AE.1 proves that the complexification of the compact simple algebra is simple. An invariant subspace of its adjoint module is an ideal, hence that module is irreducible. The root decomposition (AD.8) has zero space \(\mathfrak h\) of dimension \(r\) and one-dimensional nonzero root spaces by AD.3. No \(\theta+\alpha\) with positive \(\alpha\) can be a root: its simple coefficients would exceed those of the dominating \(\theta\). Therefore every positive root operator kills \(\mathfrak g_\theta\), and AD.6 identifies \(\theta\) as the adjoint highest weight. Counting the root spaces and the Cartan space gives \(r+|R|\). □

## AF. Root cascades and the weights of sphere actions

The first-order tangent space of an orbit puts a strong restriction on its highest weight. We develop that restriction using the strongly orthogonal roots and lowering-degree argument of Gorodski–Thorbergsson, in the exact free version listed in Further reading. The root calculations and all representation-theoretic steps used here have proofs below. Throughout, \(\mathfrak k\) is a compact centreless Lie algebra, \(\mathfrak g=\mathfrak k_{\mathbb C}\), and the roots, positive roots, Cartan space \(\mathfrak a=i\mathfrak t\), and normalized triples \((E_\alpha,F_\alpha,H_\alpha)\) have the conventions of AD.3. A highest vector is always nonzero. Products of operators act on the rightmost vector first.

**Lemma AF.1 (the recursive root cascade).** In a finite reduced crystallographic root system \(R\), fix a positive system \(R^+\). Start with its irreducible components. Choose the highest root of one component, retain the roots perpendicular to it, and repeat on any of the remaining nonempty components. This ends with positive roots
\[
\mathcal B=(\beta_1,\ldots,\beta_s).
\tag{AF.1}
\]
They are pairwise orthogonal, neither sum nor difference of two of them is a root, and
\[
w=s_{\beta_1}\cdots s_{\beta_s}
\quad\hbox{satisfies}\quad wR^+=-R^+.
\tag{AF.2}
\]
It acts as minus the identity on \(L=\operatorname{span}_{\mathbb R}\mathcal B\) and as the identity on \(L^\perp\). At each stage the chosen highest root has nonnegative inner product with every positive root still present.

**Proof.** A perpendicular subsystem
\[
R\cap T^\perp
\tag{AF.3}
\]
is a reduced crystallographic root system in its own span: reflection in one of its roots preserves both \(R\) and \(T^\perp\); the other axioms are inherited. Its positive system is the restriction of the original one. AE.1 supplies its simple basis and orthogonal irreducible components. The highest roots in AE.6 and the coordinate root lengths in AE.3–AE.5 show that the highest root of every irreducible system is long, of maximal root length, and dominates every positive root in the simple-root order.

For its highest root \(\theta\), one has \((\theta,\alpha_i)\geq0\) for each simple root. Indeed, a negative pairing, together with the root-string calculation of AD.4, would make \(\theta+\alpha_i\) a root. To see this without using a Lie algebra for an abstract subsystem, the integral angle-product argument in AE.1 applied to \(\theta,-\alpha_i\) gives the same root. It contradicts the highest-root coefficient bounds. Positive expansion now gives \((\theta,\gamma)\geq0\) for every positive root \(\gamma\) of that component; the other components are perpendicular.

The retained span loses at least one dimension each time, so the procedure terminates. A later \(\beta_j\) is perpendicular to every earlier \(\beta_i\). If \(\beta_i\pm\beta_j\) were a root, it would lie in the subsystem present when \(\beta_i\) was chosen and in the same component as \(\beta_i\): distinct component spans contain no root crossing between them, by AE.1. Its squared length would be
\[
|\beta_i|^2+|\beta_j|^2>|\beta_i|^2,
\tag{AF.4}
\]
contradicting the maximal length of \(\beta_i\) in that component. This proves strong orthogonality.

We prove (AF.2) by induction along the procedure. Suppose a positive root \(\gamma\) has positive pairing with the current highest root \(\theta\). Its reflection \(s_\theta\gamma\) has negative pairing with \(\theta\). Every positive root of the current subsystem has nonnegative pairing with \(\theta\), so \(s_\theta\gamma\) is negative. All subsequent reflections preserve its pairing with \(\theta\), hence keep it negative. If instead \(\gamma\perp\theta\), then \(s_\theta\gamma=\gamma\), and the induction in the retained subsystem makes its eventual image negative. This treats every positive root. Orthogonal reflections commute; their product negates each \(\beta_i\) and fixes the orthogonal complement of their span. □

**Lemma AF.2 (unitary representatives and the extreme vector).** Let \(W\) be an irreducible unitary \(\mathfrak k\)-module of highest weight \(\lambda\), and choose a highest vector \(v\). Set
\[
n_i=\lambda(H_{\beta_i})=\frac{2(\lambda,\beta_i)}{|\beta_i|^2},
\qquad k(\lambda)=\sum_i n_i,\qquad
v_-=\prod_i F_{\beta_i}^{\,n_i}v.
\tag{AF.5}
\]
Then \(n_i\) are nonnegative integers and \(v_-\ne0\). It spans the lowest-weight space, of weight
\[
w\lambda=\lambda-\sum_i n_i\beta_i.
\tag{AF.6}
\]
The commuting unitary operators
\[
u_i=\exp\!\left(\frac{\pi}{2}(E_{\beta_i}-F_{\beta_i})\right),
\qquad U=\prod_i u_i
\tag{AF.7}
\]
represent the reflections on weights and satisfy
\[
Uv=\frac{(-1)^{k(\lambda)}}{\prod_i n_i!}\,v_-,
\qquad U^2v=(-1)^{k(\lambda)}v.
\tag{AF.8}
\]
For \(0\leq j_i\leq n_i\), the vector \(\prod_iF_{\beta_i}^{j_i}v\) is nonzero. If \(\lambda\ne0\), then \(k(\lambda)>0\).

**Proof.** AD.6 gives the nonnegative integral values \(n_i\). Strong orthogonality and the bracket rule in AD.3 imply that the triples belonging to distinct \(\beta_i\) commute with each other. For one triple, AD.2 gives
\[
\|F^jv\|^2=\frac{j!\,n!}{(n-j)!}\,\|v\|^2
\quad(0\leq j\leq n),\qquad F^{n+1}v=0.
\tag{AF.9}
\]
Applying another commuting lowering operator leaves the other highest-vector equations and highest eigenvalues unchanged. Repeated use of (AF.9) proves all the nonvanishing assertions and gives
\[
\left\|\prod_iF_{\beta_i}^{j_i}v\right\|^2
=\prod_i\frac{j_i!\,n_i!}{(n_i-j_i)!}\,\|v\|^2.
\tag{AF.10}
\]
The weight calculation and the formula for commuting reflections give (AF.6). Since \(w\) reverses positive roots, AD.6 says that this is the lowest weight and that its space is one-dimensional.

Here is the exponential calculation, including its sign. On the homogeneous polynomials of degree \(n\) in two variables put
\[
E=x\partial_y,\qquad F=y\partial_x,\qquad
H=x\partial_x-y\partial_y.
\tag{AF.11}
\]
The vectors \(F^jx^n\) satisfy exactly AD.2's string formulas and form a basis. Thus this string is isomorphic to the string generated by \(v\), with \(x^n\) mapped to \(v\). The derivation \(E-F\) sends \(x\) to \(-y\) and \(y\) to \(x\). Solving these two constant-coefficient differential equations and using the product rule gives
\[
\exp(t(E-F))x^n=(\cos t\,x-\sin t\,y)^n.
\tag{AF.12}
\]
At \(t=\pi/2\) this equals \((-1)^ny^n=(-1)^nF^nx^n/n!\); at \(t=\pi\) it equals \((-1)^nx^n\). This proves (AF.8), first for each string and then for their commuting product.

For completeness, these operators implement the reflections on every weight, not only on \(v\). For a fixed triple \(T=E-F\),
\[
[T,H]=-2(E+F),\qquad [T,E+F]=2H.
\tag{AF.13}
\]
The corresponding two-dimensional exponential rotates \(H\) to \(-H\) at time \(\pi/2\). Every Cartan element in \(\ker\beta\) commutes with \(T\), and
\[
H_0=\left(H_0-\frac{\beta(H_0)}2H_\beta\right)
       +\frac{\beta(H_0)}2H_\beta
\tag{AF.14}
\]
separates the fixed and reversed parts. Conjugation by the exponential therefore acts on the Cartan by \(s_\beta\), and hence acts on weights by the same reflection. The matrix exponential and its conjugation equation are justified in F.1. Since \(F=E^*\), \(T\) is skew-adjoint, so the exponential is unitary. Moreover \(\sigma(E)=-F\) gives \(\sigma(T)=T\): it is the exponential of an element of the compact real algebra.

Finally, if all \(n_i\) vanish, then \(w\lambda=\lambda\). The highest vector is also lowest, by the one-dimensionality just proved. Every positive and negative root operator kills it. Their brackets show \(\lambda(H_\alpha)=0\) for every root \(\alpha\). The roots span the Cartan dual by AD.3, so \(\lambda=0\). This proves the final assertion. □

**Theorem AF.3 (type and exact lowering degree).** In the notation of AF.2, the irreducible module is self-dual if and only if \(\lambda\in L\). In that case it has real type for even \(k(\lambda)\) and quaternionic type for odd \(k(\lambda)\). Otherwise it has complex type.

Let \(\mathcal U^m(\mathfrak g)v\) mean the span of products of at most \(m\) elements of \(\mathfrak g\) applied to \(v\), including the empty product. Then
\[
v_-\in\mathcal U^{k(\lambda)}(\mathfrak g)v,\qquad
v_-\notin\mathcal U^{k(\lambda)-1}(\mathfrak g)v
\quad\hbox{if }k(\lambda)>0.
\tag{AF.15}
\]
The integer \(k\) is additive over the simple factors and linear in the highest weight.

**Proof.** The conjugate unitary module has the negatives of the weights of \(W\). Indeed, for \(H=iX\in\mathfrak a\) with \(X\in\mathfrak t\), complex extension of the conjugate compact action gives
\[
\overline{\rho}(H)\,\bar z=-\overline{\rho(H)z}.
\tag{AF.16}
\]
Its highest weight is therefore \(-w\lambda\). The Hermitian form identifies the conjugate module with the dual. The uniqueness theorem AD.6 shows that self-duality is equivalent to \(\lambda=-w\lambda\), which by AF.1 is precisely \(\lambda\in L\).

In that case an isomorphism with the conjugate module gives an invertible antilinear map \(\epsilon:W\to W\) commuting with \(\mathfrak k\). The positive Hermitian form \((x,y)\mapsto\langle\epsilon y,\epsilon x\rangle\) is invariant. Its positive comparison operator with the given Hermitian form commutes with the representation, so AD.1 makes it a positive scalar. Rescale \(\epsilon\) to be antiunitary. Its square is a complex scalar by AD.1. If \(\epsilon^2=cI\), then \(\epsilon\epsilon^2=\epsilon^2\epsilon\) implies \(\bar c=c\), and antiunitarity implies \(|c|=1\). Thus \(c=1\) or \(-1\), the alternatives proved and interpreted in AC.2.

Normalize \(v\) to unit length. Both \(\epsilon v\) and \(Uv\) are unit vectors of lowest weight \(-\lambda=w\lambda\). Write \(\epsilon v=aUv\), where \(|a|=1\). The map \(\epsilon\) commutes with each real compact exponential \(u_i\), so
\[
\epsilon^2v=\bar a\,U\epsilon v
           =|a|^2U^2v=(-1)^{k(\lambda)}v.
\tag{AF.17}
\]
This proves the type assertion. With our normalization the complex root operators obey
\[
\epsilon H_\alpha=-H_\alpha\epsilon,\qquad
\epsilon E_\alpha=-F_\alpha\epsilon.
\tag{AF.18}
\]
These signs follow by writing a complex element as \(X+iY\) with \(X,Y\in\mathfrak k\), and using \(\epsilon i=-i\epsilon\) and \(\sigma(E_\alpha)=-F_\alpha\).

We next prove the degree assertion. We need the following balanced-word fact. If \(\delta_1,\ldots,\delta_N\) belong to the cascade, repetitions allowed, and \(\gamma_1,\ldots,\gamma_M\in R^+\), then
\[
N>M,\quad \sum_{a=1}^N\delta_a=\sum_{b=1}^M\gamma_b
\quad\Longrightarrow\quad
E_{\delta_N}\cdots E_{\delta_1}
F_{\gamma_1}\cdots F_{\gamma_M}v=0.
\tag{AF.19}
\]
The equality of weights is part of the hypothesis.

First record explicitly the word-reordering fact needed for induction. Order negative root vectors before Cartan vectors and positive root vectors. Interchanging neighbouring factors uses \(XY=YX+[X,Y]\), whose bracket term has one fewer factor. Induction first on word length and then on the number of out-of-order pairs expresses every word of length at most \(q\) in that order, without increasing its length. On a highest vector, positive factors at the right kill the vector and Cartan factors become scalars. Thus only negative words of length at most \(q\) remain. This is the spanning argument of AD.6 and does not require linear independence of ordered words. If a word of length \(q\) already contains a Cartan or positive-root factor, while all its other factors are negative-root factors, every surviving negative word has length at most \(q-1\): a term with no bracket retains that nonnegative factor and either vanishes or loses it on evaluation; every bracket term has already lost a factor. All terms retain the total Cartan weight of the original word.

We prove (AF.19) by induction on \(N\). For \(M=0\) the positive operators kill \(v\), so in particular the starting case \(N=1\) holds. Since the cascade raising operators commute, arrange that \(\delta_1=\beta_i\) has the earliest index occurring among them. Each \(\gamma_b\) lies in the subsystem perpendicular to all \(\beta_j\) with \(j<i\). To prove this, proceed successively through those earlier indices. The sum of the \(\delta_a\) is perpendicular to \(\beta_j\). By the balance hypothesis so is the sum of the \(\gamma_b\). In the subsystem retained so far, all the nonnegative numbers \((\beta_j,\gamma_b)\) sum to zero, by AF.1, so each vanishes.

Consequently, whenever \(\beta_i-\gamma_b\) is a root it is positive. A root in the same remaining component as \(\beta_i\) is bounded by that highest root; a root in another remaining component has no root difference with it. Thus
\[
[E_{\beta_i},F_{\gamma_b}]
\quad\hbox{is zero, a Cartan element, or a positive-root vector.}
\tag{AF.20}
\]
Commute \(E_{\beta_i}\) to the right through the \(M\) negative factors. The term in which it reaches \(v\) vanishes. Each other term is a product of the \(N-1\) remaining cascade raising operators followed by a word of length \(M\), with exactly one of its slots replaced as in (AF.20). The reordering fact expresses that latter word on \(v\) as negative words of length \(M'\leq M-1\). Their total root weight is
\[
-\sum_b\gamma_b+\beta_i=-\sum_{a=2}^N\delta_a.
\tag{AF.21}
\]
Therefore each satisfies the balance hypothesis for \(N-1\) raising factors, and \(N-1>M'\). The induction hypothesis kills every term. This proves (AF.19).

AF.2 already puts \(v_-\) in degree \(k\). An arbitrary vector of degree at most \(k-1\) is a sum of negative words of that length by the reordering argument. For any such word, adjoints give
\[
\left\langle F_{\gamma_1}\cdots F_{\gamma_M}v,v_-\right\rangle
=\left\langle
\prod_iE_{\beta_i}^{\,n_i}
F_{\gamma_1}\cdots F_{\gamma_M}v,v
\right\rangle .
\tag{AF.22}
\]
If the weights do not balance, the last inner product is zero by orthogonality of distinct Cartan weights. If they do, (AF.19), with \(N=k>M\), makes it zero. Hence \(v_-\) is orthogonal to the whole space of degree at most \(k-1\), proving (AF.15). The formula (AF.5) is linear in \(\lambda\), and the cascade of an orthogonal union is the union of its component cascades. Together with AD.7 this proves additivity for tensor factors. □

**Lemma AF.4 (first-order sphere tests).** Let \(K\) be a compact connected semisimple matrix group. Suppose first that its nontrivial irreducible complex unitary module \(W\) has real type, with invariant real form \(V=\{z:\epsilon z=z\}\). Then \(K\) is transitive on the unit sphere of \(V\) if and only if
\[
W=\mathcal U^1(\mathfrak g)v+\mathcal U^1(\mathfrak g)\epsilon v.
\tag{AF.23}
\]
Suppose instead that \(W\) has complex or quaternionic type. Then \(K\) is transitive on the unit sphere of its underlying real space if and only if
\[
W=\mathcal U^1(\mathfrak g)v.
\tag{AF.24}
\]

**Proof.** A nontrivial highest weight is nonzero: if \(\lambda=0\), AD.2 makes every negative-root operator kill the highest vector, and AD.6 then gives the trivial module. For a real form, normalize \(v\) to unit length. The vectors \(v\) and \(\epsilon v\) have the distinct weights \(\lambda,-\lambda\), so they are perpendicular. Put \(p=v+\epsilon v\in V\).

Complexifying the real orbit tangent \(\mathfrak k p\) gives exactly \(\mathfrak g p\). Cartan elements yield the line \(\mathbb C(v-\epsilon v)\), because \(Hp=\lambda(H)(v-\epsilon v)\) and some \(\lambda(H)\ne0\). Positive-root operators kill \(v\) and negative-root operators kill the lowest vector \(\epsilon v\). Consequently
\[
\mathfrak g p=
\operatorname{span}_{\mathbb C}
\{v-\epsilon v,\ F_\alpha v,\ E_\alpha\epsilon v:
  \alpha\in R^+\}.
\tag{AF.25}
\]
The complexification of the real orthogonal decomposition at \(p\) is
\[
W=\mathbb Cp\oplus(p^\perp_V)_{\mathbb C},
\qquad \mathfrak g p\subset(p^\perp_V)_{\mathbb C}.
\tag{AF.26}
\]
Here the complex bilinear extension of the real metric is nondegenerate, and its value at \((p,p)\) is the positive real number \(\|p\|^2\); thus the sum is direct. The right side of (AF.23) is exactly \(\mathbb Cp+\mathfrak g p\). Equality with \(W\) is therefore equivalent to the full real tangent condition \(\mathfrak k p=p^\perp_V\). The equivalence of that condition at one nonzero point with sphere transitivity was fully proved in AC.4.

For the underlying real space of \(W\), use the actual highest vector \(v\) as the real point. The compact root-space generators are
\[
iH,\qquad E_\alpha-F_\alpha,\qquad
i(E_\alpha+F_\alpha).
\tag{AF.27}
\]
The Cartan part gives \(\mathbb R\,iv\), while the last two generators applied to \(v\) give \(-F_\alpha v\) and \(iF_\alpha v\). Thus, if \(A=\sum_{\alpha>0}\mathbb C F_\alpha v\),
\[
\mathfrak k v=\mathbb R\,iv\oplus A_{\mathbb R},
\qquad
\mathcal U^1(\mathfrak g)v=\mathbb Cv\oplus A.
\tag{AF.28}
\]
Each summand in \(A\) has weight different from \(\lambda\), so \(A\perp v\) in the Hermitian sense. It follows that the real tangent is the full real hyperplane perpendicular to \(v\) precisely when \(\mathbb Cv+A=W\). Apply AC.4 again. □

**Lemma AF.5 (degree, factor and zero-weight restrictions).** For a nontrivial irreducible module satisfying (AF.23), one has \(k(\lambda)\leq3\). If it has real type, then \(k(\lambda)=2\). If it satisfies (AF.24), then \(k(\lambda)=1\).

For a self-dual module satisfying (AF.23), the zero-weight space has dimension at most one. In particular, an adjoint module of a compact simple algebra of rank at least two cannot satisfy (AF.23).

For a faithful sphere action of a compact connected semisimple group, a complex or quaternionic irreducible realification has only one simple Lie-algebra factor. A real-form action has at most two simple factors. If there are two, each complex tensor factor is self-dual of quaternionic type and has \(k=1\).

**Proof.** Suppose \(k\geq4\), and choose integers \(0\leq j_i\leq n_i\) with \(\sum_i j_i=2\). This is possible by taking two of the \(k\) lowering factors. AF.2 gives a nonzero vector
\[
z=\prod_iF_{\beta_i}^{j_i}v.
\tag{AF.29}
\]
It is orthogonal to \(\mathcal U^1(\mathfrak g)v\): reorder any word of length at most one, take adjoints against \(z\), and use exactly (AF.19) with \(N=2>M\), or weight orthogonality if unbalanced.

On the other hand, the commuting rank-one formulas show that \(z\) is a nonzero scalar multiple of
\[
\prod_iE_{\beta_i}^{\,n_i-j_i}v_-.
\tag{AF.30}
\]
Use the opposite positive system, whose cascade is \(-\beta_1,\ldots,-\beta_s\), and whose highest vector is \(v_-\). Its highest coroot eigenvalues along that cascade are still \(n_i\). Since \(\sum_i(n_i-j_i)=k-2\geq2\), the same balanced-word argument makes (AF.30) orthogonal to \(\mathcal U^1(\mathfrak g)v_-\). Self-duality identifies the line of \(v_-\) with the line of \(\epsilon v\). Thus \(z\) is orthogonal to both summands of (AF.23), a contradiction. This proves \(k\leq3\). For real type, AF.3 gives even \(k\), and AF.2 gives positive \(k\), so \(k=2\). In (AF.24), \(v_-\) must be of degree at most one; AF.3 and positivity give \(k=1\).

For the zero-weight assertion, the only possible zero-weight vectors among the generators of (AF.23) are
\[
F_\lambda v,\qquad E_\lambda\epsilon v,
\tag{AF.31}
\]
and these are present only if \(\lambda\) is a root. It would then be positive: a negative expansion \(\lambda=-\sum c_i\alpha_i\), with \(c_i\geq0\), would contradict \(|\lambda|^2=-\sum c_i(\lambda,\alpha_i)\leq0\), since \(\lambda\) is dominant and nonzero. Its rank-one highest eigenvalue is \(\lambda(H_\lambda)=2\). The rank-one formulas give \(F_\lambda^2v\ne0\), of weight \(-\lambda\). That lowest-weight space is one-dimensional, so \(\epsilon v\) is a scalar multiple of \(F_\lambda^2v\). Applying \(E_\lambda\) makes the two vectors in (AF.31) proportional. The zero space is consequently at most one-dimensional. AE.6 identifies the adjoint zero-weight multiplicity with the rank, proving the exclusion.

Finally AD.7 decomposes an irreducible complex module over the simple factors. Faithfulness implies that none is trivial. Each contributes a positive integer to \(k\), by AF.2–AF.3. Hence there is only one factor in (AF.24), and at most two in the real-form case. If there are two, both have \(k=1\). The highest-weight spaces of the different ideals are orthogonal summands, and the cascade span is their direct sum; self-duality of the full module therefore implies self-duality of each factor by AF.3. Odd \(k=1\) makes each quaternionic. □

**Lemma AF.6 (explicit cascade degrees and duality).** Use exactly the simple-root numbering in AE.3–AE.5, and let \(\omega_i\) denote its fundamental weights. Then
\[
\begin{array}{c|c|c}
\text{root type}&k(\omega_i)&\text{duality on the indices}\\ \hline
A_n&\min(i,n+1-i)&i\longmapsto n+1-i\\
B_n,\ i<n&2\lceil i/2\rceil&\text{identity}\\
B_n,\ i=n&\lceil n/2\rceil&\text{identity}\\
C_n&i&\text{identity}\\
D_n,\ i\leq n-2&2\lceil i/2\rceil&
 \text{identity except as below}\\
D_n,\ i=n-1,n&\lfloor n/2\rfloor&
 (n-1\ n)\text{ if }n\text{ is odd}\\
G_2&(2,2)&\text{identity}\\
F_4&(2,6,4,2)&\text{identity}\\
E_6&(2,2,4,6,4,2)&(1\ 6)(3\ 5)\\
E_7&(2,5,6,8,7,4,3)&\text{identity}\\
E_8&(4,8,10,14,12,8,6,2)&\text{identity}
\end{array}
\tag{AF.32}
\]
An entry giving a tuple lists the values in increasing order of the node index. For \(\lambda=\sum_i a_i\omega_i\), compute \(k\) by linearity. The module is self-dual exactly when its coefficients \(a_i\) are unchanged by the indicated permutation.

**Proof.** We verify the cascades and the arithmetic, rather than assuming a table of representations. In \(A_n\), put \(N=n+1\). Successively removing the highest root \(e_1-e_N\) leaves the roots on the middle coordinates. Thus the cascade is
\[
e_j-e_{N+1-j}\quad(1\leq j\leq\lfloor N/2\rfloor).
\tag{AF.33}
\]
Its reflections reverse the coordinate order. Its coroot sum has coefficient \(1\) on the first \(\lfloor N/2\rfloor\) coordinates, coefficient \(-1\) on the last that many, and coefficient \(0\) on a middle coordinate if present. Pairing with the fundamental weights in AE.3 gives \(\min(i,N-i)\). Negative coordinate reversal sends \(\omega_i\) to \(\omega_{N-i}\).

For \(B_n\) and \(D_n\), take the successive pairs
\[
e_1+e_2,\ e_1-e_2,\ e_3+e_4,\ e_3-e_4,\ \ldots.
\tag{AF.34}
\]
After \(e_1+e_2\), the perpendicular roots consist of the isolated pair \(\pm(e_1-e_2)\) and the same coordinate root system on indices \(3,\ldots,n\). This follows immediately from the root lists in AE.3. In \(B_n\) with \(n\) odd, append the short root \(e_n\); in \(D_n\) with \(n\) odd, the remaining single coordinate contains no root. This proves that (AF.34) follows AF.1, including the terminal one- and two-pair cases. Each complete pair contributes \(2e_{2j-1}\) to the coroot sum. The appended short root in odd \(B_n\) contributes \(2e_n\). Pairing with the partial sums and half-sums in AE.3 gives the displayed ceilings and floors. The product reflection is \(-I\) in \(B_n\) and even \(D_n\); in odd \(D_n\) it changes the sign of the first \(n-1\) coordinates and fixes the last. Its negative therefore interchanges exactly the two half-sum weights.

In \(C_n\), the successive highest roots are \(2e_1,\ldots,2e_n\); their coroot sum is \(\sum e_i\), giving \(k(\omega_i)=i\), and their reflection product is \(-I\).

The exceptional cascades are as follows. Write \(T=e_8-e_7-e_6\) in the \(E_6\) row.
\[
\begin{array}{c|l}
G_2&3\alpha_1+2\alpha_2,\ \alpha_1\\
F_4&e_1+e_2,\ e_1-e_2,\ e_3+e_4,\ e_3-e_4\\
E_6&\begin{aligned}
 &\tfrac12(T+e_1+e_2+e_3+e_4+e_5),\\
 &\tfrac12(T-e_1-e_2-e_3-e_4+e_5),\
 e_4-e_1,\ e_3-e_2
\end{aligned}\\
E_7&\begin{aligned}
 &e_8-e_7,\ e_6+e_5,\ e_6-e_5,\\
 &e_4+e_3,\ e_4-e_3,\ e_2+e_1,\ e_2-e_1
\end{aligned}\\
E_8&\begin{aligned}
 &e_8+e_7,\ e_8-e_7,\ e_6+e_5,\ e_6-e_5,\\
 &e_4+e_3,\ e_4-e_3,\ e_2+e_1,\ e_2-e_1
\end{aligned}
\end{array}
\tag{AF.35}
\]
Here is a verification of the successive highest-root property in each exceptional case. In \(G_2\), the positive-root list in AE.5 leaves only \(\alpha_1\) perpendicular to \(3\alpha_1+2\alpha_2\). In \(F_4\), the positive roots perpendicular to \(e_1+e_2\) are
\[
e_1-e_2,\ e_3\pm e_4,\ e_3,\ e_4,\
\tfrac12(e_1-e_2\pm e_3\pm e_4).
\tag{AF.36}
\]
They have the \(C_3\) simple basis
\[
u_1=\tfrac12(e_1-e_2-e_3-e_4),\quad u_2=e_4,\quad
u_3=e_3-e_4.
\tag{AF.37}
\]
Indeed, their nine positive vectors, in this basis, are \(u_1,u_2,u_3,u_1+u_2,u_2+u_3,u_1+u_2+u_3,u_1+2u_2+u_3,2u_2+u_3,2u_1+2u_2+u_3\), as direct substitution shows. The last one is \(e_1-e_2\) and dominates the others. Its perpendicular subsystem is \(B_2\) on coordinates \(3,4\), followed by the remaining root \(e_3-e_4\).

For \(E_8\), the roots perpendicular to \(e_8+e_7\) are the \(E_7\) subsystem of AE.4. The roots of that subsystem perpendicular to its highest root \(e_8-e_7\) are exactly the \(D_6\) roots \(\pm e_i\pm e_j\) on indices \(1,\ldots,6\). Its inherited positives are \(\pm e_i+e_j\) for \(i<j\), so its highest root is \(e_6+e_5\). The \(D\)-pair argument above gives the remaining entries. This also verifies the \(E_7\) row.

For \(E_6\), its positive roots are \(e_j\pm e_i\) for \(1\leq i<j\leq5\), together with
\[
\tfrac12(T+\textstyle\sum_{i=1}^5\varepsilon_i e_i),
\quad \varepsilon_i=\pm1,\quad \prod_i\varepsilon_i=1.
\tag{AF.38}
\]
This is precisely the coordinate list and positivity proved in AE.4. The first entry \(\theta\) in its row is the highest root from AE.6. A coordinate difference \(e_j-e_i\) is perpendicular to it, a coordinate sum is not, and a half-root with \(m\) minus signs has pairing \(2-m/2\) with it. Thus the positive perpendicular roots are the ten differences and the five vectors
\[
r_i=\tfrac12(T+2e_i-e_1-e_2-e_3-e_4-e_5).
\tag{AF.39}
\]
These are the positive roots of an \(A_5\) chain with simple basis
\[
r_1,\ e_2-e_1,\ e_3-e_2,\ e_4-e_3,\ e_5-e_4.
\tag{AF.40}
\]
Consecutive sums give all ten differences and all five \(r_i\), so its highest root is \(r_5\), the second entry of (AF.35). Perpendicularity to \(r_5\) leaves just the \(A_3\) differences on indices \(1,\ldots,4\). Their highest root is \(e_4-e_1\), followed by \(e_3-e_2\). This proves the \(E_6\) cascade.

To verify the degree arithmetic efficiently, put \(h=\sum_{\beta\in\mathcal B}2\beta/|\beta|^2\). Then \(k(\omega_i)=(\omega_i,h)\). The exceptional coordinate sums are
\[
\begin{aligned}
h_{G_2}&=\alpha_1+(3\alpha_1+2\alpha_2)/3,\\
h_{F_4}&=2e_1+2e_3,\\
h_{E_6}&=T-e_1-e_2+e_3+e_4+e_5,\\
h_{E_7}&=e_8-e_7+2e_6+2e_4+2e_2,\\
h_{E_8}&=2e_8+2e_6+2e_4+2e_2.
\end{aligned}
\tag{AF.41}
\]
In the \(G_2\) convention \(|\alpha_1|^2=2\), \(|\alpha_2|^2=6\); in \(E_6,E_7,E_8\) every simple root has squared length \(2\); the two long simple \(F_4\) roots have squared length \(2\) and the two short ones squared length \(1\). Substitution of the simple-root coordinates in AE.4–AE.5 into (AF.41) gives, respectively,
\[
\begin{gathered}
h=\sum_i c_i\alpha_i^\vee,\\
\begin{array}{c|l}
G_2&(c_i)=(2,2)\\
F_4&(c_i)=(2,6,4,2)\\
E_6&(c_i)=(2,2,4,6,4,2)\\
E_7&(c_i)=(2,5,6,8,7,4,3)\\
E_8&(c_i)=(4,8,10,14,12,8,6,2)
\end{array}
\end{gathered}
\tag{AF.42}
\]
Since \((\omega_j,\alpha_i^\vee)=\delta_{ij}\), these are exactly the five exceptional degree rows of (AF.32).

The cascades span the full root space in \(G_2,F_4,E_7,E_8\), so \(w=-I\) there. In \(E_6\), apply the four orthogonal reflection formulas \(s_\beta x=x-(x,\beta)\beta\), since their squared lengths are \(2\), to its six simple roots. They give
\[
-w(\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6)
=(\alpha_6,\alpha_2,\alpha_5,\alpha_4,\alpha_3,\alpha_1).
\tag{AF.43}
\]
The same permutation acts on the dual fundamental-weight basis. The already computed classical actions and AF.3 now prove every duality assertion and the coefficient criterion. □

**Corollary AF.7 (the remaining highest weights for a sphere action).** Assume the real sphere action is faithful and irreducible and the acting compact connected group is semisimple.

If it is the realification of a complex irreducible module of complex or quaternionic type, its algebra has one simple factor. The only possible highest weights are
\[
A_n:\ \omega_1,\omega_n;\qquad
B_2:\ \omega_2;\qquad
C_n\ (n\geq3):\ \omega_1.
\tag{AF.44}
\]
The \(A_1\) row contains just \(\omega_1\); it and the \(B_2,C_n\) entries are quaternionic. For \(A_n\), \(n\geq2\), the two entries are of complex type.

If it is a real-form action and the algebra is simple, the only possible highest weights, after excluding the adjoint representations of rank at least two, are
\[
\begin{array}{c|l}
A_1&2\omega_1\\
A_3&\omega_2\\
B_n\ (n\geq2)&\omega_1\\
B_3,\ B_4&\omega_n\\
C_n\ (n\geq3)&\omega_2\\
D_n\ (n\geq4)&\omega_1\\
D_4&\omega_3,\omega_4\\
G_2&\omega_1\\
F_4&\omega_4
\end{array}
\tag{AF.45}
\]
There are no other simple cases. A nonsimple real-form action has exactly two simple factors, each chosen from the quaternionic entries of (AF.44). These are necessary highest-weight restrictions; the identification of their matrix images is a further step.

**Proof.** By AD.6 a highest weight has nonnegative integral coefficients in the fundamental-weight basis. AF.5 says that the realification case has \(k=1\). All coefficients in (AF.32) are positive. The only entries equal to \(1\) are the two ends of \(A_n\), the last node of \(B_2\), and the first node of \(C_n\). Thus exactly one of those fundamental weights can occur, and no sum or multiple can occur. AF.3 and the duality column give their stated types. The number of factors is given by AF.5.

For a simple real-form action, \(k=2\) and the coefficients must satisfy the duality symmetry. In \(A_1\) this gives \(2\omega_1\). For \(A_n\), \(n\geq2\), a sum of the two end weights \(\omega_1+\omega_n\) is always possible at this stage; it is the highest root and hence the adjoint highest weight by AE.6 and AD.6. A single degree-two fundamental weight is self-dual only at the middle node of \(A_3\), namely \(\omega_2\). Twice an end weight is not self-dual for \(n\geq2\). These exhaust \(A\).

In \(B_2\), the degree-two possibilities are \(\omega_1\) and \(2\omega_2\), the latter the highest root \(e_1+e_2\). In \(B_n\), \(n\geq3\), they are \(\omega_1,\omega_2\), and also the last weight only for \(n=3,4\). Here \(\omega_2=e_1+e_2\) is adjoint. In \(C_n\) they are \(2\omega_1\) and \(\omega_2\), the former the highest root \(2e_1\). In \(D_n\) the first two weights have degree two, with \(\omega_2=e_1+e_2\) adjoint; the two end weights have degree two only for \(n=4,5\), and in \(D_5\) they are exchanged by duality, so neither alone is self-dual. In \(D_4\) both are self-dual.

The exceptional rows can be read without any representation-dimension formula. In \(G_2\), the two degree-two weights are \(\omega_1,\omega_2\), with \(\omega_2\) the highest root. In \(F_4\) they are \(\omega_1,\omega_4\), with \(\omega_1\) the highest root. In \(E_6\), the degree-two entries are \(\omega_1,\omega_2,\omega_6\), and duality leaves only \(\omega_2\). In \(E_7\) only \(\omega_1\) has degree two; in \(E_8\) only \(\omega_8\) does. These last three weights are the highest roots: pairing the highest-root vectors of AE.6 with the simple coroots gives respectively the single nonzero entry at nodes \(2,1,8\). AD.6 identifies each with its adjoint module.

AF.5 excludes all those adjoint modules except \(A_1\). This leaves (AF.45). Finally, AF.5 gives two self-dual degree-one factors in the nonsimple real case. The self-dual entries of (AF.44) are precisely its stated quaternionic entries. □

**Lemma AF.8 (the highest short-root modules).** Suppose the irreducible root system has type \(B_n,C_n,F_4\), or \(G_2\), and an irreducible unitary module has as its highest weight the highest short root. Its nonzero weights are exactly the short roots, each with multiplicity one. The multiplicity of zero and the complex dimension are
\[
\begin{array}{c|c|c}
 \text{type}&\dim W_0&\dim_{\mathbb C}W\\ \hline
B_n&1&2n+1\\
C_n&n-1&n(2n-1)-1\\
F_4&2&26\\
G_2&1&7
\end{array}
\tag{AF.46}
\]
In particular, the \(C_n\) entries with \(n\geq3\) and the \(F_4\) entry in (AF.45) do not give sphere actions.

**Proof.** The highest short roots in the four coordinate systems are respectively
\[
e_1,\qquad e_1+e_2,\qquad e_1,\qquad 2\alpha_1+\alpha_2.
\tag{AF.47}
\]
They are dominant, as direct pairing with the simple coroots shows. The Weyl group is transitive on the short roots. For \(B_n,C_n\), this follows from the signed permutations in AE.3. In \(G_2\), the coordinate reflections in AE.5 permute its six short roots transitively. In \(F_4\), signed coordinate permutations are available by its axis and long-root reflections. They are transitive separately on the eight axis roots and the sixteen half-roots; reflection in \((e_1+e_2+e_3+e_4)/2\) sends \(e_1\) to \((e_1-e_2-e_3-e_4)/2\), joining the two sets. Thus every short root is an extremal weight \(w\lambda\), whose weight line is one-dimensional by AD.4 and AD.6.

Consider the action of any root operator on such a line. Conjugate it by the unitary reflection representatives of AF.2 to the line of the highest weight \(\lambda\). The root operator becomes a nonzero scalar multiple of another root operator: conjugation preserves its Cartan weight and that root space is one-dimensional by AD.3. A positive raising operator kills the highest vector. A lowering operator for a positive root \(\gamma\) starts a rank-one string of length
\[
m=\lambda(H_\gamma)
  =\frac{2(\lambda,\gamma)}{|\gamma|^2}\in\mathbb Z_{\geq0}.
\tag{AF.48}
\]
Because \(\lambda\) is short, Cauchy–Schwarz, proved in [Local tools for bundles and transport, Lemma 0.0](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), gives \(m\leq2\), and equality can hold only if \(\gamma=\lambda\). Indeed it is strict if \(\gamma\) is long; if both are short, equality forces them equal. For \(m=0\) the lowering operator vanishes. For \(m=1\) its output is on the reflected extremal line of weight \(s_\gamma\lambda=\lambda-\gamma\). For \(m=2\), \(\gamma=\lambda\), and the string has weights \(\lambda,0,-\lambda\). We have proved: a root operator on an extremal short-root line gives another such line, zero, or a vector of weight zero; the latter occurs only for the opposite root direction.

Let \(Q\) be the direct sum of the short-root lines, and let \(Z\) be the span of \(F_\beta v_\beta\) for short roots \(\beta\), where \(v_\beta\) spans the line of weight \(\beta\) and \(F_\beta\) means an operator in the root space \(-\beta\). We show that \(Q+Z\) is invariant. Cartan operators preserve \(Q\) and kill \(Z\); root operators preserve \(Q+Z\) on \(Q\) by the preceding paragraph. For a root operator \(X_\alpha\) and \(z_\beta=F_\beta v_\beta\), write
\[
X_\alpha z_\beta
=[X_\alpha,F_\beta]v_\beta+F_\beta X_\alpha v_\beta.
\tag{AF.49}
\]
If \(\alpha=\beta\) or \(-\beta\), the rank-one string puts the result in the line of weight \(\alpha\). Otherwise \(X_\alpha v_\beta\), if nonzero, lies on an extremal short-root line; applying \(F_\beta\) to it again stays in \(Q+Z\). The bracket is zero or a root operator, so its action on \(v_\beta\) also lies there. Both terms have weight \(\alpha\ne0\), so in fact they belong to \(Q\). This proves invariance. It contains the highest vector, and irreducibility gives \(W=Q\oplus Z\). Thus there are no additional nonzero weights and no additional multiplicities.

We next bound \(\dim Z\) from above by the number of short simple roots. The simple negative root vectors generate the whole negative-root algebra. To verify this, let \(\gamma\) be a nonsimple positive root. The descent argument in AD.5 supplies a simple \(\alpha_i\) with \(\gamma-\alpha_i\) positive and a root. AD.4 says the bracket of the two root lines \(-\alpha_i\) and \(-(\gamma-\alpha_i)\) is the nonzero line \(-\gamma\). Induction on the positive integral height proves the generation assertion. AD.6's negative-word spanning therefore becomes spanning by words in the simple negative generators.

A word that ends at weight zero has a leftmost factor \(F_{\alpha_i}\) whose input has weight \(\alpha_i\). That input space is zero unless \(\alpha_i\) is short, and is one-dimensional when it is short. Sorting all words by that leftmost factor gives
\[
W_0=\sum_{\alpha_i\ \mathrm{short}} F_{\alpha_i}W_{\alpha_i},
\qquad \dim W_0\leq\#\{\text{short simple roots}\}.
\tag{AF.50}
\]
There is at least one zero vector: the rank-one string of the highest short root has highest eigenvalue two. For \(B_n\) and \(G_2\) there is only one short simple root, so their multiplicity is exactly one.

For \(C_n\), consider the closed subsystem
\[
R'=\{e_i-e_j:i\ne j\},
\tag{AF.51}
\]
of type \(A_{n-1}\). Its root spaces and coroot span form a compact complexified subalgebra: the bracket rule in AD.3 and the coordinate root list show closure, and compact conjugation preserves it. Its root-space description and simple-ideal proof are those of AE.1. The extremal line of weight \(e_1-e_n\) is a highest-vector line for this subalgebra. Raising by any positive root \(e_i-e_j\), \(i<j\), gives neither zero nor a short root in the \(C_n\) weight set just proved: cancellation to a difference would require \(j=1\) or \(i=n\), both impossible. Hence every such raising operator kills that line. Its restricted highest weight is the highest root of \(A_{n-1}\).

Decompose the restricted unitary module into irreducibles by AD.1. A nonzero component of this highest vector generates an irreducible module of that highest weight. By AD.6 it is isomorphic to the adjoint module of this very subalgebra, whose highest weight and zero multiplicity \(n-1\) were proved in AE.6. More explicitly, the cyclic module generated by the chosen vector is one copy even if several identical summands occur: choose one nonzero component, identify all other nonzero components with it by AD.6 with their highest vectors matched, and the generated module is the image of the resulting diagonal intertwiner.

Every full Cartan weight of that cyclic module is \(e_1-e_n\) plus an integral combination of roots in (AF.51), so it lies in their real span. A weight in that span vanishing on its coroot span is zero, by positive definiteness. The \(n-1\) restricted zero-weight vectors therefore have full weight zero. This proves \(\dim W_0\geq n-1\), and (AF.50) gives equality.

For \(F_4\), its two short simple roots
\[
\alpha_3=e_4,\qquad
\alpha_4=\tfrac12(e_1-e_2-e_3-e_4)
\tag{AF.52}
\]
span a closed \(A_2\) root subsystem with roots
\(\pm\alpha_3,\pm\alpha_4,\pm(\alpha_3+\alpha_4)\).
To check that these are all roots in their plane, note that the first three coordinates of a vector in it are proportional to \((1,-1,-1)\). Among the \(F_4\) coordinate roots, an axis vector in that plane must be \(\pm e_4\), no long root can have that pattern, and a half-root must be \(\pm\alpha_4\) or \(\pm(\alpha_3+\alpha_4)\). All six are short. The extremal line of weight \(\alpha_3+\alpha_4\) is killed by the positive-root operators of this subsystem, since adding any of its three positive roots gives neither zero nor a short root. Its cyclic module is the adjoint \(A_2\) module by the same complete-reducibility and highest-weight uniqueness argument. Its two restricted zero vectors have full weight zero, because all generated weights lie in this two-dimensional root plane. Thus \(\dim W_0\geq2\), matching (AF.50).

Finally count the short roots in AE.3 and AE.5: \(2n\) for \(B_n\), \(2n(n-1)\) for \(C_n\), \(24\) for \(F_4\), and \(6\) for \(G_2\). Adding the zero multiplicities proves (AF.46). The \(C_n\) weight \(\omega_2=e_1+e_2\) and \(F_4\) weight \(\omega_4=e_1\) in (AF.45) are exactly these highest short roots. Their zero multiplicities exceed one in the indicated ranks, contrary to AF.5, so they are excluded. □

## AG. The matrix representations and the holonomy list

We now identify the remaining representations from AF. This completes the first-order sphere-action argument in the free Gorodski–Thorbergsson article cited in Further reading. The identifications use the matrix groups and Clifford representations already constructed in Y–AB. We work with the actual acting Lie algebras and their modules; no existence theorem for arbitrary highest weights or isomorphism theorem for abstract simple Lie algebras is needed.

**Lemma AG.1 (weights with rank-one strings of length at most one).** Let \(W\) be an irreducible unitary module of a compact centreless algebra, with highest weight \(\lambda\). Suppose
\[
\lambda(H_\alpha)\in\{0,1\}\quad(\alpha\in R^+).
\tag{AG.1}
\]
Then its weights are precisely the Weyl orbit of \(\lambda\), all with multiplicity one. In the coordinate systems of AE, the following highest weights satisfy this condition and have the indicated dimensions:
\[
\begin{array}{c|c|c}
\text{root type}&\lambda&\dim_{\mathbb C}W\\ \hline
A_n&\omega_1,\omega_n&n+1\\
A_3&\omega_2&6\\
B_n&\omega_n&2^n\\
C_n&\omega_1&2n\\
D_n&\omega_1&2n\\
D_4&\omega_3,\omega_4&8
\end{array}
\tag{AG.2}
\]
These statements describe any module with the displayed highest weight; they do not assume that a module exists for every dominant weight.

**Proof.** AD.4 and AD.6 show that every weight in the orbit is present and that its weight space is a line. The unitary reflection representatives calculated in AF.2 carry the highest line to each of these lines. Conjugation carries a root operator to a nonzero scalar multiple of the appropriate reflected root operator: its Cartan weight is reflected, and its root space is one-dimensional by AD.3.

It is therefore enough to examine root operators on a highest vector \(v\). Positive root operators kill it. For a negative root operator \(F_\alpha\), AD.2 gives a string of length \(\lambda(H_\alpha)\). If that length is zero the operator kills \(v\); if it is one, its image has weight \(\lambda-\alpha=s_\alpha\lambda\). Thus every root operator takes every orbit line into another orbit line or zero. Cartan operators preserve these lines. Their sum is a nonzero invariant subspace, hence all of \(W\).

For the dimension assertions, use the explicit root lists and reflection groups of AE.3. In \(A_n\), put \(N=n+1\). The weight \(\omega_j\) has coordinate \(1-j/N\) on its first \(j\) indices and \(-j/N\) on the others. Pairing with a positive coroot \(e_r-e_s\), \(r<s\), gives zero or one. Its permutation orbit is indexed by the \(j\)-element subsets of the \(N\) indices: equal coordinates within each block make those choices distinct and exhaustive. For \(j=1,N-1\) this gives \(N\) weights, and for \(N=4,j=2\) it gives six.

For the \(B_n\) half-sum \(\omega_n=\frac12(e_1+\cdots+e_n)\), positive long coroots are \(e_r\pm e_s\), \(r<s\), and positive short coroots are \(2e_r\). Their pairings are zero or one. Signed permutations give exactly all \(2^n\) half-sums with arbitrary signs. In \(C_n\), the weight \(e_1\) pairs by zero or one with the coroots \(e_r\) and \(e_r\pm e_s\); its signed-permutation orbit is \(\{\pm e_r\}\). In \(D_n\), the same assertion for \(e_1\) uses the coroots \(e_r\pm e_s\) and the even-sign permutation group; it is still transitive on the \(2n\) signed coordinate vectors, since an unwanted second sign change can be placed on another, zero coordinate.

Finally, each half-sum weight of \(D_4\) pairs by zero or one with its positive coroots. This is immediate for all four plus signs. For the half-sum with its last sign negative, a positive root involving the last index gives either zero or one, and the other pairings are unchanged. Even sign changes give exactly the eight sign patterns of each fixed parity. This proves every orbit count and (AG.2). □

**Lemma AG.2 (unitary coordinates and invariant real structures).** An antiunitary map \(J\) with \(J^2=-I\) on a finite-dimensional complex Hermitian space has an orthonormal basis
\[
u_1,\ldots,u_m,\ Ju_1,\ldots,Ju_m.
\tag{AG.3}
\]
The unitary operators commuting with \(J\) form, in suitable ordering of this basis, exactly the compact group \(\mathrm{Sp}(m)\) of Y.3.

If two complex irreducible unitary representations are isomorphic and have invariant antiunitary involutions, there is a unitary intertwiner that restricts to a real orthogonal isomorphism of their fixed real spaces. A connected matrix Lie group's image is determined by its image Lie algebra.

**Proof.** Antiunitarity gives \(\langle Jx,Jy\rangle=\langle y,x\rangle\). Taking \(x=u,y=Ju\) and using \(J^2u=-u\) shows \(\langle Ju,u\rangle=-\langle Ju,u\rangle\), hence \(u\perp Ju\). Their complex span is \(J\)-invariant and its orthogonal complement is too: apply the antiunitary identity to test orthogonality to \(u,Ju\). Choose a unit vector in that complement and continue. This proves (AG.3) and even complex dimension. On each ordered pair \(u,Ju\), \(J\) has the antilinear coordinate expression
\[
(z,w)\longmapsto(-\bar w,\bar z).
\tag{AG.4}
\]
Its centralizer is unchanged if this matrix is replaced by its negative. Interleaving the pairs therefore gives exactly the unitary commutation relation (Y.13), whose equivalence with the compact symplectic group was proved in Y.3.

Let \(T\) be an invertible complex intertwiner between two irreducible unitary representations. Then \(T^*T\) is a positive Hermitian intertwiner. AD.1 makes it a positive scalar, so rescale \(T\) to be unitary. Transport the first antiunitary involution by \(T\), obtaining \(C_1\) on the second space, and write its given one as \(C_2\). The complex-linear intertwiner \(C_2C_1^{-1}\) is scalar, so
\[
C_2=aC_1,\qquad |a|=1.
\tag{AG.5}
\]
Choose \(|b|=1\) with \(b^2=a\). Explicitly, if \(a\ne-1\) take \(b=(1+a)/|1+a|\), for which \(b/\bar b=a\); if \(a=-1\) take \(b=i\). Then \(bT\) intertwines the involutions because \(b=a\bar b\). Its restriction to their fixed real spaces is an orthogonal isomorphism.

Those fixed spaces have real dimension equal to the complex dimension: for any antiunitary involution \(C\),
\[
z=\frac{z+Cz}{2}
  +i\,\frac{z-Cz}{2i}
\tag{AG.6}
\]
has both displayed components fixed by \(C\), and their intersection with their imaginary multiples is zero. The Hermitian form is real on fixed vectors, by antiunitarity. Real Gram–Schmidt from Y.2 consequently supplies the required real orthonormal coordinates.

Finally F.1 proves that a connected Lie group is generated by its identity exponential neighbourhood, and that a representation carries exponentials to matrix exponentials of its differential. Two connected matrix images with the same image algebra are therefore both generated by those same exponentials, and are equal. This applies also when the original representation has a discrete kernel. □

**Lemma AG.3 (the classical matrix images).** The candidates in AF.44 have the following underlying real matrix images: the two end weights of \(A_n\) give \(\mathrm{SU}(n+1)\); the \(B_2\) weight \(\omega_2\) gives \(\mathrm{Sp}(2)\); and \(C_n\)'s \(\omega_1\) gives \(\mathrm{Sp}(n)\). The \(A_1\) entry is also \(\mathrm{Sp}(1)=\mathrm{SU}(2)\).

Among the real-form candidates of AF.45, the images are
\[
\begin{array}{c|c|c}
\text{type and weight}&\dim_{\mathbb R}V&\text{matrix image}\\ \hline
A_1,\ 2\omega_1&3&\mathrm{SO}(3)\\
A_3,\ \omega_2&6&\mathrm{SO}(6)\\
B_n,\ \omega_1&2n+1&\mathrm{SO}(2n+1)\\
D_n,\ \omega_1&2n&\mathrm{SO}(2n)\\
D_4,\ \omega_3\text{ or }\omega_4&8&\mathrm{SO}(8).
\end{array}
\tag{AG.7}
\]
Every identification is by an orthogonal change of real coordinates.

**Proof.** A nontrivial representation of a simple Lie algebra is faithful: its kernel is an ideal and is not the whole algebra. AE.1 and AE.3 give the dimensions of the compact algebras from their Cartan and root spaces:
\[
\begin{aligned}
\dim A_n&=n(n+2),\\
\dim B_n=\dim C_n&=n(2n+1),\\
\dim D_n&=n(2n-1).
\end{aligned}
\tag{AG.8}
\]
For an \(A_n\) end weight, AG.1 gives a complex space of dimension \(N=n+1\). The compact algebra acts by skew-Hermitian matrices. Its trace is zero: a nonabelian simple algebra equals its derived algebra, and \(\operatorname{tr}[A,B]=0\) by the trace identity of F.1. Thus its faithful image is contained in \(\mathfrak{su}(N)\). Both dimensions are \(N^2-1\), by (AG.8) and Y.2, so the inclusion is equality. AG.2 then identifies the connected group image with \(\mathrm{SU}(N)\). This proves the assertion for either end weight without choosing an outer automorphism.

For \(B_2\)'s \(\omega_2\), \(C_n\)'s \(\omega_1\), and \(A_1\)'s \(\omega_1\), AF.3–AF.7 give an invariant antiunitary \(J\) squaring to \(-I\). AG.1 gives complex dimensions \(4,2n,2\), respectively. AG.2 puts the compact algebra in \(\mathfrak{sp}(2),\mathfrak{sp}(n),\mathfrak{sp}(1)\), whose dimensions in Y.2 agree with (AG.8). Faithfulness gives equality, and connected exponential generation gives the asserted group images. Y.6 identifies the last one with \(\mathrm{SU}(2)\).

For the real forms, the real dimension equals the complex dimension by AG.2. The \(A_1\) module \(2\omega_1\) is its adjoint module by AE.6 and AD.6, so has dimension three. AG.1 gives dimensions six for \(A_3\)'s \(\omega_2\), \(2n\) for \(D_n\)'s \(\omega_1\), and eight for the \(D_4\) half-sums. AF.8 gives dimension \(2n+1\) for \(B_n\)'s highest short root \(\omega_1=e_1\). Each real compact image lies in the skew matrices of that dimension. Formula (AG.8) agrees in each case with \(\dim\mathfrak{so}(d)=d(d-1)/2\), proved in Y.2. The algebra and connected group image are therefore the full orthogonal ones in (AG.7). All coordinates used are orthonormal, so these are orthogonal identifications. □

**Lemma AG.4 (uniqueness of the even-dimensional complex Clifford matrices).** Suppose \(2r\) Hermitian operators \(\Gamma_1,\ldots,\Gamma_{2r}\) on a complex Hermitian space of dimension \(2^r\) satisfy
\[
\Gamma_a\Gamma_b+\Gamma_b\Gamma_a=2\delta_{ab}I.
\tag{AG.9}
\]
Any two such ordered systems are simultaneously unitarily conjugate. Their \(2^{2r}\) ordered subset products are a basis of the full complex endomorphism algebra. In particular their common complex commutant is scalar.

**Proof.** Each \(\Gamma_a\) is unitary and Hermitian. A nonempty ordered subset product \(\Gamma_A\) has trace zero. If \(|A|\) is even, conjugation by a generator in \(A\) changes its sign. If \(|A|\) is odd, choose a generator outside \(A\), which is possible because \(2r\) is even; conjugation again changes its sign. Trace is unchanged by conjugation, by F.1, so the trace vanishes. For distinct subsets \(A,B\), the product \(\Gamma_A^*\Gamma_B\) is, up to sign, the product belonging to the nonempty symmetric difference. Therefore
\[
\operatorname{tr}(\Gamma_A^*\Gamma_B)=
\begin{cases}
2^r,&A=B,\\
0,&A\ne B.
\end{cases}
\tag{AG.10}
\]
These \(2^{2r}\) matrices are independent and equal in number to the dimension of all endomorphisms. They are a basis. Commuting with them all is commuting with all matrix units, which forces a scalar by the elementary argument in Z.3.

We prove the unitary conjugacy explicitly. Define
\[
E_j=\tfrac12(\Gamma_{2j-1}-i\Gamma_{2j}),\quad
F_j=E_j^*,\quad H_j=E_jF_j-F_jE_j
                 =i\Gamma_{2j-1}\Gamma_{2j}.
\tag{AG.11}
\]
Expansion of (AG.9) gives
\[
E_j^2=F_j^2=0,\quad E_jF_j+F_jE_j=I,\quad H_j^2=I,
\tag{AG.12}
\]
and all \(E_j,F_j\) anticommute with \(E_\ell,F_\ell\) when \(j\ne\ell\). The \(H_j\) are commuting Hermitian involutions. Their joint \(+1\) projection is
\[
P=2^{-r}\prod_{j=1}^r(I+H_j).
\tag{AG.13}
\]
Each nonconstant product in its expansion has trace zero by the subset-product calculation. Hence \(\operatorname{tr}P=1\). A Hermitian projection has only eigenvalues zero and one by AD.1, so its image is a line. Choose a unit vector \(v\) on it. Then \(E_jv=0\), since
\(\|E_jv\|^2=\langle F_jE_jv,v\rangle=0\) by \(F_jE_j=(I-H_j)/2\).

For each subset \(A=\{a_1<\cdots<a_s\}\), put
\[
v_A=F_{a_1}\cdots F_{a_s}v.
\tag{AG.14}
\]
These vectors have norm one: \(F_j\) is an isometry on the \(H_j=+1\) eigenspace because \(E_jF_j=(I+H_j)/2\), and each other \(F_\ell\) preserves that eigenspace. Their joint \(H\)-eigenvalues are \(-1\) exactly on \(A\), so the \(2^r\) vectors are mutually orthogonal by AD.1 and are a basis. In that basis \(F_j\) inserts \(j\), with sign \((-1)^{|\{a\in A:a<j\}|}\), if \(j\notin A\), and is zero otherwise. The operator \(E_j\) removes \(j\) with the same sign if it is present, and is zero otherwise; this follows by anticommuting it through the preceding factors and using (AG.12). These rules are independent of the original matrices. Sending one such orthonormal basis to the other intertwines every \(E_j,F_j\), and hence every \(\Gamma_a\) by (AG.11). □

**Theorem AG.5 (identifying the two remaining spin images).** The real-form \(B_3\) module of highest weight \(\omega_3\) has the eight-dimensional \(\mathrm{Spin}(7)\) matrix image of Z.4. The real-form \(B_4\) module of highest weight \(\omega_4\) has the sixteen-dimensional \(\mathrm{Spin}(9)\) matrix image of AB.1. Both identifications are orthogonal conjugacies.

**Proof.** We first work with the complex half-sum module for \(B_n\), for \(n=3\) or \(4\). AG.1 gives all weights
\[
\tfrac12(\varepsilon_1e_1+\cdots+\varepsilon_ne_n),
\qquad \varepsilon_i\in\{1,-1\},
\tag{AG.15}
\]
each once. For its short roots \(e_i\), write \(E_i,F_i,H_i\) for the normalized triples of AD.3. Each \(H_i\) has only the eigenvalues \(1,-1\). The rank-one decomposition AD.2 therefore consists entirely of strings of length one, and gives on the whole module
\[
E_i^2=F_i^2=0,\qquad E_iF_i+F_iE_i=I.
\tag{AG.16}
\]

We must prove the anticommutation relations for different indices. Fix \(i\ne j\). The roots in the coordinate plane of \(e_i,e_j\) are precisely
\[
\pm e_i,\ \pm e_j,\ \pm e_i\pm e_j.
\tag{AG.17}
\]
Their root spaces and their two-dimensional coroot span form a complex subalgebra stable under compact conjugation. Closure follows from the bracket rule in AD.3 and the coordinate list; its centre is zero, since its roots span the Cartan dual. Its Cartan centralizer and root spaces are exactly the displayed ones. AE.1 consequently makes its compact real algebra simple of type \(B_2\).

Restrict the given unitary module to it and decompose by AD.1. The only restricted weights are the four half-sums \((\pm e_i\pm e_j)/2\), with possible multiplicities from the other coordinates. For the positive system with simple roots \(e_i-e_j,e_j\), the only dominant one among these four is \((e_i+e_j)/2\): pairing with those simple coroots requires first \(\varepsilon_i\geq\varepsilon_j\), and then \(\varepsilon_j\geq0\). Every irreducible summand therefore has that highest weight. AG.1 gives its complex dimension four. The \(B_2\) cascade degree is one by AF.6, so AF.3 gives its quaternionic type.

On one such summand choose unit weight vectors \(u_1,u_2\) of weights \((+,+)/2,(+,-)/2\). Its invariant antiunitary quaternionic structure \(J\) gives the remaining unit vectors \(v_1=Ju_1,v_2=Ju_2\), of weights \((-,-)/2,(-,+)/2\). Distinct weights are orthogonal. In the ordered basis \(u_1,u_2,v_1,v_2\),
\[
H_i=\operatorname{diag}(1,1,-1,-1),\qquad
H_j=\operatorname{diag}(1,-1,-1,1).
\tag{AG.18}
\]
The complex bilinear form \(\Omega(x,y)=\langle x,Jy\rangle\) is alternating and nondegenerate. For example, antiunitarity and \(J^2=-I\) give
\(\langle y,Jx\rangle=-\langle x,Jy\rangle\).
It is invariant under the complexified algebra: for a compact skew-Hermitian \(X\) commuting with \(J\), the two terms in
\(\Omega(Xx,y)+\Omega(x,Xy)\) cancel by the adjoint identity, and complex linearity extends the conclusion.

Its matrix in this basis is the negative of
\(\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)\).
Thus a complex infinitesimal symplectic matrix has block form
\(\left(\begin{smallmatrix}A&B\\C&-A^T\end{smallmatrix}\right)\),
with \(B,C\) symmetric, as follows by multiplying \(X^T\Omega+\Omega X=0\). The weight shifts by \(e_i,e_j\) now leave exactly
\[
E_i=a(E_{14}+E_{23}),\qquad
E_j=b(E_{12}-E_{43}),
\tag{AG.19}
\]
where \(E_{ab}\) is the matrix sending the \(b\)-th basis vector to the \(a\)-th and killing the others. Neither coefficient is zero, by the length-one strings. The identities \([E_i,E_i^*]=H_i\), \([E_j,E_j^*]=H_j\) give \(|a|=|b|=1\).

The matrix-unit rule \(E_{ab}E_{cd}=\delta_{bc}E_{ad}\) explicitly gives
\[
\begin{aligned}
E_iE_j&=-abE_{13},&E_jE_i&=abE_{13},\\
E_iF_j&=-a\bar bE_{24},&F_jE_i&=a\bar bE_{24}.
\end{aligned}
\tag{AG.20}
\]
Taking adjoints gives the two remaining pairs. All cross anticommutators vanish on this summand, and hence on every summand of the restriction. We have proved them on the original module for every \(i\ne j\).

Define
\[
\Gamma_{2i-1}=E_i+F_i,\qquad
\Gamma_{2i}=i(E_i-F_i).
\tag{AG.21}
\]
They are Hermitian, and (AG.16), (AG.20) give exactly (AG.9). The compact image contains \(E_i-F_i=-i\Gamma_{2i}\) and \(i(E_i+F_i)=i\Gamma_{2i-1}\). Their commutators contain every \(\Gamma_a\Gamma_b\), \(a<b\). By AG.4 these degree-one and degree-two Clifford products are complex-linearly independent. Their \(2n+\binom{2n}{2}=n(2n+1)\) skew-Hermitian matrices are therefore real-linearly independent. The original compact simple algebra is faithful and has that same dimension by (AG.8). Its image is exactly
\[
\operatorname{span}_{\mathbb R}
\{\,i\Gamma_a,\ \Gamma_a\Gamma_b: a<b\,\}.
\tag{AG.22}
\]

For \(n=3\), let \(c_a=L_{e_a}\), \(1\leq a\leq7\), be the real skew octonion multiplication matrices of Z.3. They satisfy \(c_ac_b+c_bc_a=-2\delta_{ab}I\). Put
\[
A_a=c_ac_7,\qquad \widetilde\Gamma_a=-iA_a
\quad(1\leq a\leq6)
\tag{AG.23}
\]
on the complexification of their real eight-dimensional space. These \(\widetilde\Gamma_a\) are Hermitian and satisfy (AG.9). For \(a\ne b\leq6\), \(A_aA_b=c_ac_b\), so their span (AG.22) is exactly the span of all \(c_ac_b\), \(1\leq a<b\leq7\). This is the \(\mathrm{Spin}(7)\) algebra established in Z.4.

For \(n=4\), use the nine symmetric real matrices \(P_0,\ldots,P_8\) from AB.1, with \(P_aP_b+P_bP_a=2\delta_{ab}I\). Put
\[
A_a=P_aP_8,\qquad \widetilde\Gamma_{a+1}=-iA_a
\quad(0\leq a\leq7).
\tag{AG.24}
\]
Again these are eight Hermitian Clifford matrices on the complexification of a real sixteen-dimensional space. Here \(A_aA_b=-P_aP_b\) for distinct \(a,b<8\), and (AG.22) is precisely the span of all \(P_aP_b\), \(0\leq a<b\leq8\). AB.1 identifies it as the \(\mathrm{Spin}(9)\) algebra.

AG.4 supplies a unitary conjugacy between each pair of ordered Clifford systems, hence between their compact image algebras. Both complex modules are irreducible: the original one is so by hypothesis, and in each constructed one the compact algebra contains all \(i\widetilde\Gamma_a\), whose associative algebra is all endomorphisms by AG.4. The given real forms and the ordinary real structures of the constructed matrices are invariant antiunitary involutions. AG.2 adjusts the unitary conjugacy by a scalar phase to intertwine these real structures, without changing conjugation on matrices. Its restriction is real orthogonal. Connected exponential generation then identifies the group images, proving both assertions. □

**Theorem AG.6 (identifying the seven-dimensional exceptional image).** A compact simple algebra of type \(G_2\), acting in its real-form module of highest weight \(\omega_1\), has as its connected matrix image the octonion group \(G_2\subset\mathrm{SO}(7)\) constructed in Z.7, up to orthogonal conjugacy.

**Proof.** AF.8 gives real dimension seven, with complex weights zero once and the six short roots once each. Faithfulness embeds the actual compact algebra \(\mathfrak k\) in \(\mathfrak{so}(V)\). Choose an orthogonal identification \(V=\operatorname{Im}\mathbb O\). The differential isomorphism
\[
d\pi:\mathfrak{spin}(7)\longrightarrow\mathfrak{so}(7)
\tag{AG.25}
\]
proved in Z.4 lifts \(\mathfrak k\) to a compact Lie algebra of skew operators on the real eight-dimensional spin space \(\mathbb O\). We determine the weights of this restriction directly.

A Cartan algebra of \(\mathfrak k\) acts on \(V\) as three mutually orthogonal rotation planes and a fixed real axis. To justify these real planes, diagonalize its commuting Hermitian operators on \(V_{\mathbb C}\) by AD.1. Conjugation pairs each nonzero weight line with the opposite line. A unit vector on one line and its conjugate give an orthogonal real two-plane by their real and imaginary parts; the zero line is the complexification of a real axis by (AG.6). Orient the three planes so that their positive weights are
\[
\mu_1=e_1-e_2,\qquad
\mu_2=e_2-e_3,\qquad
\mu_3=e_3-e_1,\qquad \mu_1+\mu_2+\mu_3=0.
\tag{AG.26}
\]
These are one representative from each opposite pair of short \(G_2\) roots in AE.5.

In a real orthonormal basis adapted to the planes, let \(B_j=c_{2j-1}c_{2j}\) for \(j=1,2,3\), using the Clifford multiplication operators of Z.3. Formula (Z.19) shows that \(d\pi(B_j)\) is twice the rotation generator in the \(j\)-th plane. If \(H=iX\) is in the Cartan space and \(\mu_j(H)\) is its Hermitian weight on that plane, its lift therefore acts on the complex spin space as
\[
\frac12\sum_{j=1}^3\mu_j(H)\,T_j,
\qquad T_j=iB_j.
\tag{AG.27}
\]
The \(T_j\) are commuting Hermitian involutions. For every sign triple \(\varepsilon\), their joint projection is
\[
P_\varepsilon=\frac18\prod_{j=1}^3(I+\varepsilon_jT_j).
\tag{AG.28}
\]
Every nonconstant term in its expansion is a scalar multiple of a nonempty even Clifford product of length two, four or six. Z.3 proves its trace zero. Consequently \(\operatorname{tr}P_\varepsilon=8/8=1\), and AD.1 makes its eigenspace one-dimensional. The eight spin weights are exactly
\[
\frac12(\varepsilon_1\mu_1+\varepsilon_2\mu_2+\varepsilon_3\mu_3).
\tag{AG.29}
\]
When all signs agree this is zero. Otherwise it is one of \(\pm\mu_1,\pm\mu_2,\pm\mu_3\), each exactly once. Thus the restricted spin module has zero weight twice and each short root once.

Decompose this unitary module into complex irreducibles by AD.1. Its only possible nonzero dominant highest weight is the highest short root \(2\alpha_1+\alpha_2=\omega_1\). Explicitly, the three positive short roots \(\alpha_1,\alpha_1+\alpha_2,2\alpha_1+\alpha_2\) have simple-coroot pairings
\[
(2,-1),\qquad(-1,1),\qquad(1,0),
\tag{AG.30}
\]
respectively. A negative root cannot be a nonzero dominant weight, by the norm argument in AF.5. Hence only the last positive one is dominant. A highest weight zero gives the trivial module, by the rank-one and highest-vector argument in AF.4. AF.8 says that an irreducible summand of highest weight \(\omega_1\) has dimension seven. There must be one because nonzero weights occur, and there can be only one because their multiplicities are one. The remaining one-dimensional summand is trivial.

It follows that the real spin representation has a nonzero fixed vector for the lifted algebra. Indeed a nonzero fixed vector in its complexification has a nonzero real or imaginary part, and the real matrices kill both. Normalize that real vector to length one. Z.5 gives an element of \(\mathrm{Spin}(7)\) carrying it to \(1\in\mathbb O\). After this conjugation the lifted algebra lies in the stabilizer algebra of \(1\). By Z.7 that is the octonion automorphism algebra of dimension fourteen. The lifted algebra also has dimension \(2+12=14\), by AE.5 and the root-space decomposition. Thus the two algebras are equal.

Project the conjugating element by \(\pi\). On the spin stabilizer, \(\pi\) is exactly the restriction of an octonion automorphism to \(\operatorname{Im}\mathbb O\), as proved in Z.5–Z.7. We obtain an orthogonal conjugacy of the original algebra with the standard seven-dimensional \(G_2\) algebra. Both connected group images are generated by its exponentials, so AG.2 proves equality of those images as well. □

**Theorem AG.7 (the two-factor image).** A faithful irreducible real-form sphere action of a compact connected semisimple group with more than one simple Lie-algebra factor has, up to orthogonal conjugacy, the image
\[
\mathrm{Sp}(m)\mathrm{Sp}(1)\quad\hbox{on }\mathbb H^m,\qquad m\geq1.
\tag{AG.31}
\]
Its action, kernel and low-dimensional identification are exactly Y.4 and Y.6.

**Proof.** AF.5 gives exactly two quaternionic complex factors, both of degree one. By AF.7 and AG.3 their actual image algebras are the compact symplectic algebras on their standard modules \(W_a=\mathbb C^{2a}\), \(W_b=\mathbb C^{2b}\). AD.7 identifies the complexification of the real-form module with \(W_a\otimes W_b\).

In the standard symplectic algebra choose the diagonal Cartan operators with weights \(\pm e_1,\ldots,\pm e_a\); this follows directly from the diagonal quaternionic matrices in Y.3. These operators form a maximal abelian algebra: an operator commuting with them preserves their distinct complex weight lines, and the skew-Hermitian and quaternionic commutation conditions leave exactly the same diagonal operators. Choose a Cartan element satisfying \(e_1(H)>e_2(H)>\cdots>e_a(H)>0\), avoiding the finitely many root hyperplanes by a small perturbation within these strict inequalities. The resulting positive system has highest module weight \(e_1\) and lowest weight \(-e_1\), by AD.6 and the strict maximum and minimum among the displayed weights. This argument applies also in ranks one and two. If \(a,b\geq2\), each standard module has an intermediate weight \(e_2\), different from these highest and lowest weights. Their tensor product therefore has a nonzero weight vector of weight \((e_2,e_2)\). But the first-order space of the highest tensor is contained in
\[
W_a\otimes\mathbb C v_b+\mathbb C v_a\otimes W_b,
\tag{AG.32}
\]
whose weights have at least one coordinate equal to its highest weight. The first-order space of the lowest tensor has at least one coordinate equal to its lowest weight. The weight \((e_2,e_2)\) is in neither space. The direct weight decomposition contradicts the necessary equality (AF.23). Thus one of \(a,b\) is one. Relabel the other as \(m\).

We identify the real representation, not only its dimensions. Complexify the real space \(\mathbb H^m\) in the action of Y.4. The map
\[
\Psi:\mathbb H^m\longrightarrow M_{2m,2}(\mathbb C),
\qquad
(q_1,\ldots,q_m)\longmapsto
\begin{pmatrix}\chi(q_1)\\ \vdots\\ \chi(q_m)\end{pmatrix}
\tag{AG.33}
\]
extends to a complex-linear isomorphism from that complexification. For one block, the four matrices \(\chi(1),\chi(i),\chi(j),\chi(k)\) are complex-linearly independent: their two diagonal coefficients distinguish \(1,i\), and their two off-diagonal coefficients distinguish \(j,k\), using the explicit matrices (Y.2). They form a basis of \(M_2(\mathbb C)\). Taking the \(m\) blocks proves the assertion.

The quaternion multiplication formulas of Y.1–Y.3 give
\[
\Psi(Avq^{-1})=\chi_m(A)\Psi(v)\chi(q)^{-1}.
\tag{AG.34}
\]
Thus this complexified representation is the tensor product of the standard \(\mathbb C^{2m}\) and the dual of the standard \(\mathbb C^2\). The alternating determinant form \(x^TJ_0y\) is preserved by \(\mathrm{SU}(2)=\mathrm{Sp}(1)\), as calculated in Y.6; its nondegeneracy identifies that dual with the standard module itself. This proves that (AG.33) gives exactly the same complex tensor representation as \(W_m\otimes W_1\).

The standard modules are complex irreducible: a nonzero complex invariant subspace is a real invariant subspace, and the standard symplectic action is real irreducible by Y.2. Their tensor product is complex irreducible by AD.7. Both the given real form and the real form coming from \(\mathbb H^m\) have invariant positive metrics. AG.2 therefore turns the complex equivalence into an orthogonal equivalence of real representations. The connected images are equal by exponential generation. Y.4 already proves the kernel \(\{(I,1),(-I,-1)\}\), compactness and transitivity, and Y.6 identifies the case \(m=1\) with \(\mathrm{SO}(4)\). □

**Theorem AG.8 (all connected linear sphere actions).** Let \(H\subseteq\mathrm{SO}(V)\) be a compact connected matrix group, where \(n=\dim_{\mathbb R}V\geq2\). It is transitive on the unit sphere if and only if, after an orthogonal change of coordinates, it is one of the following matrix groups in the stated real representation:

| Group | Real dimension | Representation |
| --- | --- | --- |
| \(\mathrm{SO}(n)\), \(n\geq2\) | \(n\) | Standard orthogonal action |
| \(\mathrm{SU}(m)\), \(m\geq2\) | \(2m\) | Standard complex action, regarded as real |
| \(\mathrm U(m)\), \(m\geq2\) | \(2m\) | Standard complex action, regarded as real |
| \(\mathrm{Sp}(m)\), \(m\geq2\) | \(4m\) | Standard quaternionic action |
| \(\mathrm{Sp}(m)\mathrm U(1)\), \(m\geq2\) | \(4m\) | \(v\mapsto Avz^{-1}\), \(\lvert z\rvert=1\), \(z\in\mathbb C\) |
| \(\mathrm{Sp}(m)\mathrm{Sp}(1)\), \(m\geq2\) | \(4m\) | \(v\mapsto Avq^{-1}\), \(\lvert q\rvert=1\), \(q\in\mathbb H\) |
| \(G_2\) | \(7\) | Octonion automorphisms on \(\operatorname{Im}\mathbb O\) |
| \(\mathrm{Spin}(7)\) | \(8\) | The real spin action of Z.4 |
| \(\mathrm{Spin}(9)\) | \(16\) | The real spin action of AB.1 |

The parameter ranges use the equal-image identifications of Y.6. The assertion classifies the matrix images, so it also classifies effective linear actions; a presentation by a larger group is reduced to its image by factoring out its kernel.

**Proof.** For \(n=2\), AC.6 proves that the only transitive connected image is \(\mathrm{SO}(2)\). Suppose \(n\geq3\). Sphere transitivity makes the representation real irreducible, since an invariant subspace containing one unit vector must contain its whole orbit and hence all of \(V\). AC.3–AC.5 show that the connected compact semisimple commutator subgroup \(S\) is still transitive.

Apply the complete representation-type alternatives of AC.2 to \(S\). In the realification cases, AF.5–AF.7 give exactly the highest weights in (AF.44); AG.3 identifies their images as the standard special unitary or symplectic ones. In the real-form case with simple algebra, AF.7 gives (AF.45), and AF.8 excludes its \(C_n\), \(n\geq3\), and \(F_4\) entries. AG.3 identifies all remaining classical images, AG.5 the \(B_3,B_4\) spin images, and AG.6 the \(G_2\) image. If the algebra is nonsimple, AG.7 gives the quaternionic product image. Thus every possible semisimple image has been identified, using the exhaustive root and highest-weight arguments of AE–AF.

It remains to restore the centre of \(H\). All the real-form cases have real scalar commutant. One can see this directly from their irreducible complexifications: extend a real commuting endomorphism complex-linearly, use AD.1 to make it a complex scalar, and commute it with the invariant real conjugation to make that scalar real. For \(\mathrm{Sp}(m)\mathrm{Sp}(1)\) the same conclusion is also proved directly in Y.6. AC.6 allows no additional connected central circle in these cases.

For the \(A_{m-1}\) end representations with \(m\geq3\), AF.6 says the two ends are distinct dual weights. Thus they have complex type, and AC.2 makes the real commutant exactly the complex scalars. AC.6 gives either \(\mathrm{SU}(m)\) or its product with the scalar unit circle. The latter is exactly \(\mathrm U(m)\): its Lie algebra contains \(\mathfrak{su}(m)\) and \(i\mathbb RI\), whose direct sum is all skew-Hermitian matrices, and both groups are connected by Y.2 and AC.6. Equality follows from AG.2.

For a standard symplectic image, Y.6 computes the full real commutant as the right quaternionic scalar multiplications. AC.6 says that any extra circle in it is conjugate, by an orthogonal map commuting with \(S\), to right multiplication by the unit complex numbers. Its product image is exactly \(\mathrm{Sp}(m)\mathrm U(1)\) of Y.4. When \(m=1\), Y.6 gives \(\mathrm{Sp}(1)=\mathrm{SU}(2)\), \(\mathrm{Sp}(1)\mathrm U(1)=\mathrm U(2)\), and \(\mathrm{Sp}(1)\mathrm{Sp}(1)=\mathrm{SO}(4)\). These account for every low-dimensional overlap used in the table.

This proves necessity, including every possible central extension. Conversely Y.2 proves compactness, connectedness and sphere transitivity for the classical groups; Y.4 proves them for both quaternionic products; Z.5 and Z.7 prove them for the spin-seven and octonion groups; and AB.1 proves them for the spin-nine action. Every row therefore has the asserted property. □

**Theorem AG.9 (the irreducible nonsymmetric Riemannian holonomy list).** Let \(M\) be a nonempty connected Riemannian manifold whose restricted holonomy representation is irreducible. If its curvature is not parallel, then at every point its restricted holonomy representation is orthogonally conjugate to one of the following:

| Group | Real dimension | Representation |
| --- | --- | --- |
| \(\mathrm{SO}(n)\), \(n\geq2\) | \(n\) | Standard orthogonal representation |
| \(\mathrm U(m)\), \(m\geq2\) | \(2m\) | Standard complex representation, regarded as real |
| \(\mathrm{SU}(m)\), \(m\geq2\) | \(2m\) | Standard complex representation, regarded as real |
| \(\mathrm{Sp}(m)\), \(m\geq2\) | \(4m\) | Standard representation on \(\mathbb H^m\) |
| \(\mathrm{Sp}(m)\mathrm{Sp}(1)\), \(m\geq2\) | \(4m\) | \(v\mapsto Avq^{-1}\) on \(\mathbb H^m\) |
| \(G_2\) | \(7\) | The real representation on \(\operatorname{Im}\mathbb O\) |
| \(\mathrm{Spin}(7)\) | \(8\) | The real eight-dimensional spin representation |

No completeness or simple-connectivity assumption is required. Here “locally symmetric” means \(\nabla R=0\); the theorem gives the stated restriction when that condition fails. It is a statement about restricted holonomy and its linear representation.

**Proof.** In dimension at most one, curvature is zero by antisymmetry in its first two tangent arguments, so the nonparallel-curvature hypothesis forces dimension at least two. F.2 proves that irreducible Riemannian restricted holonomy is a compact connected embedded subgroup of the special orthogonal group. The fully proved Berger–Simons conclusion X.2 makes it transitive on the tangent unit sphere when \(\nabla R\) is not identically zero. Hence AG.8 applies.

Of its nine rows, the circle extension \(\mathrm{Sp}(m)\mathrm U(1)\), \(m\geq2\), cannot be the restricted holonomy image: AA.2 proves by Bianchi and the curvature-span theorem that its curvature-generated algebra is contained in \(\mathfrak{sp}(m)\). The sixteen-dimensional \(\mathrm{Spin}(9)\) row would give parallel curvature by AB.3, contrary to the hypothesis. These are exactly the two removed rows. The remaining seven are precisely the displayed list.

The case \(\mathrm{Sp}(1)\mathrm U(1)=\mathrm U(2)\) is retained, since AA.2 explicitly requires quaternionic dimension at least two. The other small equal-image identifications are those in Y.6, and justify the parameter ranges. The quaternionic product has the two-element kernel and the actual real action proved in Y.4; the exceptional real actions are the constructions of Z.4 and Z.7.

Finally parallel transport conjugates the restricted holonomy groups at different points and is an isometry, by the proved transport and holonomy results used in D.1 and F.2. Thus the conclusion holds in an orthonormal frame at every point. Neither X.2 nor either exclusion uses completeness or simple connectivity, so neither does this argument. □

## Further reading

- Andrew Clarke and Bianca Santoro, [*Holonomy Groups in Riemannian Geometry*, arXiv:1206.3170v1](https://arxiv.org/abs/1206.3170v1), §4.2, especially Propositions 4.2.1 and 4.2.3, for the relation between invariant subspaces and local metric products; the chapter “Irreducible Riemannian Groups”, sections on Sp(n) and Sp(n)Sp(1), for the quaternionic representations. Section Y gives their scalar arithmetic, matrix models, actions, kernels and identifications.
- Tomasz Mrowka, [*Geometry of Manifolds*, MIT OpenCourseWare, Fall 2004, Lecture 30](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/resources/lecture30/), Theorem 21.4 and §21.3, for involutive distributions and foliations.
- Anton S. Galaev, [*On the de Rham-Wu decomposition for Riemannian and Lorentzian manifolds*, arXiv:1611.01554v1](https://arxiv.org/abs/1611.01554v1), §3, pages 2–4, for the holonomy description and reconstruction from parallel symmetric forms. H.1–H.2 give complete tensor and spectral proofs.
- Peter W. Michor, [*Topics in Differential Geometry*, author manuscript](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §5.5 for the closed-subgroup construction proved in the earlier programme lesson used in F.1.
- Bang-Yen Chen and Sharief Deshmukh, [*Some Results About Concircular Vector Fields on Riemannian Manifolds*, Filomat 34:3 (2020), 835–842](https://www.pmf.ni.ac.rs/filomat-content/2020/34-3/34-3-11-12274.pdf), Lemma 4.1, page 840, for the concurrent-field characterization of Euclidean space. G.2 supplies a complete contracting-flow proof.
- Jost-Hinrich Eschenburg and Ernst Heintze, [*Unique decomposition of Riemannian manifolds*, Augsburg institutional postprint](https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/deliver/index/docId/25299/file/25299.pdf), §2, Lemmas 1–3 and the theorem proof, with the introduction’s two corollaries. Sections J–K prove the maximal Euclidean factor, short-generator and refinement arguments, full global uniqueness, and isometry and cancellation consequences.
- Thomas Foertsch and Alexander Lytchak, [*The de Rham decomposition theorem for metric spaces*, arXiv:math/0605419v1](https://arxiv.org/abs/math/0605419v1), §§2–8, for metric-product tools, compatible affine subsets, convex refinement, intersection factors, transverse rigidity, decomposition and isometries. Sections L–S prove the full metric decomposition and isometry theorem, including their affine-image, dimension, convex-refinement and rigidity prerequisites. Section T gives worked examples.
- Petra Hitzelberger and Alexander Lytchak, [*Spaces with many affine functions*, arXiv:math/0511583v1](https://arxiv.org/abs/math/0511583v1), §§4–5, for the norm-characterization problem. M.1–M.2 prove the continuous pseudometric form by affine averaging and a complete variation argument.
- Nikolai V. Ivanov, [*The lemmas of Alexander and Sperner*, arXiv:1909.00940v1](https://arxiv.org/html/1909.00940v1), §3, §7 and Appendix A.1, for simplex subdivisions, Sperner counting and dimension bounds. Q.1–Q.4 prove the required subdivision incidences, parity, covering-dimension and finite-span conclusions.
- Lei Ni, [*A single induction proof of Simons' Riemannian holonomy theorem*, arXiv:2610.03409v1](https://arxiv.org/abs/2610.03409v1), §§2–6, for the algebraic holonomy argument. Sections U–X prove the curvature-operator and closedness prerequisites, the flat and centralizer constructions, the restriction and trace lemmas, the induction on the curvature-orbit span, and its geometric consequence.

- Brian C. Hall, [*An Elementary Introduction to Groups and Representations*, arXiv:math-ph/0005032v1](https://arxiv.org/abs/math-ph/0005032v1), the matrix-group definitions, compactness and connectedness sections, quaternionic rotation example, and classical Lie-algebra calculations. Section Y supplies the explicit paths, quaternion arithmetic, determinant and quotient arguments.

- John C. Baez, [*The Octonions*, arXiv:math/0105155v4](https://arxiv.org/abs/math/0105155v4), §§2.2–2.3 and 4.1, for octonion multiplication, its Clifford action and the compact octonion automorphism group. Z.1–Z.3 give the complete scalar and matrix constructions.

- Cristina Draper, [*Notes on G2: The Lie algebra and the Lie group*, arXiv:1704.07819v2](https://arxiv.org/abs/1704.07819v2), §§5.1 and 6, for the unit-imaginary stabilizer and the spin representation. Z.3–Z.7 prove the Clifford basis and faithful even action, reflection decomposition, compact double cover, sphere transitivity, connectedness and both smooth quotient identifications.

- Lorenz J. Schwachhöfer, [*Connections with Irreducible Holonomy Representations*, author manuscript of 10 June 2003](https://wwwold.mathematik.tu-dortmund.de/~lschwach/papers/Advances/HoloClass.pdf), §3.1, for complex eigenspaces and the Bianchi identity. AA.1–AA.2 supply the full conformally symplectic argument and the quaternionic-circle exclusion.

- Marco Castrillón López, Pedro M. Gadea and Ihor Mykytyuk, [*The canonical 8-form on manifolds with holonomy group Spin(9)*, arXiv:0911.1079v1](https://arxiv.org/abs/0911.1079v1), §§2.1 and 4, for the octonionic Clifford operators and the curvature expression. AB.1–AB.3 prove the group construction, the required curvature-space bound and the parallel-curvature conclusion.

- Claudio Gorodski and Gudlaugur Thorbergsson, [*Representations of compact Lie groups and the osculating spaces of their orbits*, arXiv:math/0203196v1](https://arxiv.org/abs/math/0203196v1), §4, the representation-type, lowering-degree and first-order tangent arguments; Appendices A–B, root cascades and degrees; and §8, transitive actions. AC.1–AC.2 give full algebraic proofs of the three representation-type alternatives. AE verifies all the root coordinates used here, their axioms, simple bases and highest-root bounds. AF gives the complete cascade, type, exact-degree and tangent proofs, derives all necessary highest weights, and proves the zero-weight multiplicities used to exclude the remaining highest-short-root cases. AG identifies every remaining matrix image, including both real spin representations and the seven-dimensional octonion representation, and proves the connected sphere-action classification and its Riemannian holonomy consequence.

- Linus Kramer, [*Two-transitive Lie groups*, author-hosted article](https://www.uni-muenster.de/AGKramer/linuspub/23.pdf), Corollary 6.2. AC.3–AC.6 prove the semisimple-transitivity reduction and the central-extension alternatives; AC.5 gives the sphere exactness argument in full.

- Alexander Kirillov, Jr., [*Introduction to Lie Groups and Lie Algebras*, author lecture notes](https://www.math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf), §§4.8, 6.5–6.6, 7.8, 7.10 and 8.1–8.3. AD.1–AD.7 give complete compact-algebra, root-string and highest-weight proofs, including the word-reordering and uniqueness arguments. AE proves the full finite root-system classification, including the multiple-edge cases and all exceptional coordinate models.
