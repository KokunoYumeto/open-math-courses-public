# Symmetric spaces

A point symmetry reverses every geodesic through its centre. The decisive property is that it preserves the connection. This connects a geometric reflection to parallel curvature, and then to a Lie-group involution and a bracket formula for curvature.

Manifolds are nonempty, smooth, Hausdorff, second countable and without boundary. Throughout the geometric results they are connected. Completeness of a connection means that every affinely parametrized geodesic is defined for all real time. A pseudo-Riemannian metric is a smooth nondegenerate symmetric form of constant signature; a Riemannian metric is positive definite. The curvature convention is
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
\]
The freely accessible notes of Vincent Pecastaing motivate the geometric questions; the free notes of Alexander Kirillov, Jr. and Pavel Etingof guide the algebraic structure theory. Exact versions and sections are listed at the end. All proof providers used here are within this lesson or the linked earlier programme lessons.

## A. Reflections and global motion

At \(p\), choose a normal neighbourhood on which the exponential map is a diffeomorphism and its domain is invariant under \(v\mapsto-v\). Its **local geodesic reflection** is
\[
s_p(\exp_p v)=\exp_p(-v).
\tag{A.1}
\]
Normal neighbourhoods and smooth dependence of the exponential are proved in [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). The connection is **locally symmetric** if (A.1) is affine near every \(p\). It is **globally symmetric** if at each \(p\) there is a global affine diffeomorphism fixing \(p\) with differential \(-I\). These maps, when they exist, restrict to (A.1) by [Affine transformations A.1](affine-transformations-and-the-isometry-group.md#lemma-a-1).

**Theorem A.1 (The smooth local test).** An affine connection is locally symmetric exactly when
\[
T=0,\qquad \nabla R=0.
\tag{A.2}
\]
For a Levi-Civita connection, including an indefinite one, the test is \(\nabla R=0\), and the resulting local reflections are local isometries. No analyticity assumption is required.

**Proof.** An affine diffeomorphism preserves torsion, curvature and their covariant derivatives, by the tensor rules of [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) and the definitions as commutators. At its fixed point, \(ds_p=-I\). Naturality of torsion therefore gives
\[
-T_p(X,Y)=T_p(-X,-Y)=T_p(X,Y),
\]
so \(T_p=0\). Applied to \(\nabla R\), whose output is one vector and whose inputs are four vectors, the same parity calculation gives
\(-(\nabla R)_p=(\nabla R)_p\).
As this holds at every \(p\), (A.2) follows.

Conversely, (A.2) implies \(\nabla T=0\). The map \(-I:T_pM\to T_pM\) preserves \(T_p=0\) and \(R_p\): the three input signs in \(R_p\) have the same product as its single output sign. [Killing fields C.1](holonomy-killing-fields-and-analytic-extension.md#theorem-c-1), with its complete smooth radial reconstruction proof, gives a local affine map fixing \(p\) with differential \(-I\). Its exponential naturality makes it precisely (A.1). That earlier theorem derives any analytic coordinates it needs from the smooth parallel tensors; analyticity is not an extra premise.

If \(\nabla g=0\), an affine local diffeomorphism \(F\) satisfies \(\nabla(F^*g-g)=0\), by [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). For this reflection the difference is zero at \(p\), because \(-I\) preserves any symmetric bilinear form. Its components in parallel frames along paths are constant, so it vanishes throughout a connected neighbourhood. Thus \(s_p\) is a local isometry.

The Levi-Civita uniqueness argument used here needs nondegeneracy, not positivity: adding the three metric-derivative identities and using zero torsion gives the Koszul formula
\[
\begin{aligned}
2g(\nabla_XY,Z)={}&Xg(Y,Z)+Yg(Z,X)-Zg(X,Y)\\
&-g(X,[Y,Z])+g(Y,[Z,X])+g(Z,[X,Y]).
\end{aligned}
\]
Nondegeneracy uniquely solves for \(\nabla_XY\). The same formula in coordinates defines a smooth connection, and direct substitution gives zero torsion and metric compatibility, exactly as in [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). This proves the metric assertion for all signatures. □

**Theorem A.2 (Completeness, simple connectivity and transvections).** A complete simply connected locally symmetric affine manifold is globally symmetric. Every globally symmetric affine manifold is complete and homogeneous under the identity component of its affine group. In the metric case its point symmetries are isometries; in the Riemannian case the identity component of the isometry group acts transitively. The completeness assertion also holds for indefinite metrics.

Along any complete geodesic \(\gamma\), the maps
\[
\tau_t=s_{\gamma(t/2)}s_{\gamma(0)}
\tag{A.3}
\]
form a smooth one-parameter group. They satisfy
\[
\tau_t(\gamma(u))=\gamma(u+t),\qquad
(d\tau_t)_{\gamma(u)}=P_{u\to u+t},
\tag{A.4}
\]
where \(P\) denotes parallel transport along that geodesic.

**Proof.** Under completeness and simple connectivity, [Killing fields C.1](holonomy-killing-fields-and-analytic-extension.md#theorem-c-1) extends the local map of A.1 to a global affine isomorphism, using the initial curvature-preserving map \(-I\). This proves the first assertion. In the metric case the parallel-tensor argument at the end of A.1 shows that the global extension preserves the metric.

Now assume global symmetry. A global affine map is determined by its value and differential at one point, by [Affine transformations A.1](affine-transformations-and-the-isometry-group.md#lemma-a-1). Thus each \(s_p\) is unique, its square is the identity, and for every affine transformation \(F\),
\[
F s_p F^{-1}=s_{F(p)}.
\tag{A.5}
\]
Suppose a geodesic starting at time \(0\) has a finite maximal positive endpoint \(b\). Choose \(a\) with \(b/2<a<b\). The formula
\[
\widetilde\gamma(t)=s_{\gamma(a)}\bigl(\gamma(2a-t)\bigr)
\quad(a\leq t\leq 2a)
\]
defines a geodesic whose value and velocity at \(a\) equal those of \(\gamma\): the velocity has one minus sign from time reversal and one from the point symmetry. Geodesic uniqueness, [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1), makes the two agree on their common interval. It extends \(\gamma\) beyond \(b\), a contradiction. Reversing time excludes a finite negative endpoint. The connection is complete.

The dependence \(p\mapsto s_p\) is smooth as a map into the affine group. Locally near \(p_0\), its value and differential at \(p_0\) are smooth in \(p\), from the jointly smooth normal-coordinate formula
\(\exp_p(-\exp_p^{-1}x)\).
Apply the inverse theorem [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) to the map \((p,v)\mapsto(p,\exp_p v)\); its differential is invertible at \((p_0,0)\) by [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). This justifies the jointly smooth inverse near \((p_0,p_0)\). The frame-value embedding in [Affine transformations D.3](affine-transformations-and-the-isometry-group.md#theorem-d-3) then gives the asserted smooth dependence into the group. In the Riemannian case the corresponding assertion follows from the isometry frame embedding of [Affine transformations C.2](affine-transformations-and-the-isometry-group.md#theorem-c-2).

For \(v\) small and \(\gamma(u)=\exp_p(uv)\), the path
\(t\mapsto s_{\gamma(t/2)}s_p\) starts at the identity and carries \(p\) to \(\gamma(t)\). Consequently the identity-component orbit of \(p\) contains a normal neighbourhood. The same holds at every point. The orbits are disjoint open subsets; connectedness makes there be just one. In the Riemannian case all the path's maps are isometries, giving transitivity of its isometry identity component. For a pseudo-Riemannian metric the symmetries still preserve the metric by A.1, and the same paths give a transitive group of global isometries, with no positive-metric completeness argument used.

It remains to establish all of (A.4), including its differential, and the group law. Affine naturality and uniqueness give
\[
s_{\gamma(a)}(\gamma(u))=\gamma(2a-u)
\]
on the whole complete geodesic. An affine map takes parallel fields to parallel fields. Its differential at \(\gamma(a)\) is \(-I\), so, by uniqueness of parallel transport,
\[
(ds_{\gamma(a)})_{\gamma(u)}
=-P_{u\to 2a-u}.
\tag{A.6}
\]
Here both sides are compared by transporting through parameter \(a\); composition and reversal of transport along the same parameterized geodesic give the displayed expression even when the geodesic meets itself. Apply (A.6) to the two factors of (A.3). Their minus signs cancel and their transports compose to \(P_{u\to u+t}\), proving (A.4).

Finally \(\tau_t\tau_r\) and \(\tau_{t+r}\) have the same value at \(\gamma(0)\) and the same differential there, namely transport to \(\gamma(t+r)\). Affine one-jet uniqueness makes them equal globally. The already proved smooth dependence makes this a smooth one-parameter group. □

**Example A.3 (Why completeness alone does not suffice).** Flat tori are globally symmetric, but a flat Klein bottle is complete and locally symmetric without having a global point symmetry at every point.

**Proof.** On \(\mathbb R^n/\Lambda\), where \(\Lambda\) is a full lattice, the map
\([x]\mapsto[2a-x]\) is well-defined for every centre \([a]\): replacing \(x\) by \(x+\lambda\) changes its image by \(-\lambda\). It is an isometry for the quotient Euclidean metric, fixes \([a]\), and has differential \(-I\).

For an explicit different outcome use the Euclidean plane and the group generated by
\[
\alpha(x,y)=(x+1,y),\qquad
\beta(x,y)=(-x,y+1).
\tag{A.7}
\]
Its elements are \(\alpha^m\beta^n\), \(m,n\in\mathbb Z\), because
\(\beta\alpha\beta^{-1}=\alpha^{-1}\). For even \(n\) they are translations \((x,y)\mapsto(x+m,y+n)\); for odd \(n\) they are \((x,y)\mapsto(-x+m,y+n)\). This action is free: if \(n\ne0\) the \(y\)-coordinate changes, and if \(n=0,m\ne0\) the \(x\)-coordinate changes. For any compact set, only finitely many integers \(n,m\) can make its image intersect itself, by coordinate boundedness. It is therefore properly discontinuous. The quotient is a smooth flat manifold by [Sectional curvature D.3](sectional-curvature-and-space-forms.md#theorem-d-3), and is compact because the image of \([0,1]\times[0,1]\) covers it. [Hopf–Rinow B.3](completeness-and-the-hopf-rinow-theorem.md#corollary-b-3) makes it complete. Its zero curvature and torsion make it locally symmetric by A.1.

If a global affine point symmetry existed at the image of \((a,b)\), lift it to a diffeomorphism of the simply connected plane fixing that lift, using the covering construction and uniqueness in [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3). The lifted map is affine for the Euclidean connection, by local covering charts, and has differential \(-I\). [Affine transformations E.3](affine-transformations-and-the-isometry-group.md#proposition-e-3) therefore makes it
\[
S(x,y)=(2a-x,2b-y).
\]
Every lift of a quotient diffeomorphism normalizes the deck group, as proved in [Affine transformations E.1](affine-transformations-and-the-isometry-group.md#theorem-e-1). Direct calculation gives
\[
S\beta S^{-1}(x,y)=(4a-x,y-1).
\]
By the explicit deck formulas this is a deck transformation exactly when \(4a\in\mathbb Z\). Choose \(a=1/8\). The condition fails, so that point has no global affine symmetry. This complete example explains the simple-connectivity qualification in A.2. □

## B. A group involution and its connection

A **symmetric presentation** consists of a connected Lie group \(G\), a smooth involutive automorphism \(\sigma:G\to G\), and a closed subgroup \(H\) satisfying
\[
(G^\sigma)^0\subseteq H\subseteq G^\sigma,\qquad
G^\sigma=\{g:\sigma(g)=g\}.
\tag{B.1}
\]
Here the superscript \(0\) denotes the identity component. This condition permits disconnected stabilizers. We write \(o=eH\) and \(\theta=d\sigma_e\).

**Lemma B.1 (The two eigenspaces).** For a symmetric presentation,
\[
\mathfrak g=\mathfrak h\oplus\mathfrak m,\quad
\mathfrak h=\ker(\theta-I),\quad
\mathfrak m=\ker(\theta+I),
\tag{B.2}
\]
and
\[
[\mathfrak h,\mathfrak h]\subseteq\mathfrak h,\qquad
[\mathfrak h,\mathfrak m]\subseteq\mathfrak m,\qquad
[\mathfrak m,\mathfrak m]\subseteq\mathfrak h .
\tag{B.3}
\]
The splitting is invariant under all of \(\operatorname{Ad}(H)\). The quotient \(G/H\) is smooth, and the differential of its orbit map identifies \(T_o(G/H)\) with \(\mathfrak m\).

**Proof.** The fixed group \(G^\sigma\) is closed and hence an embedded Lie subgroup by [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). A vector fixed by \(\theta\) has its full one-parameter subgroup fixed by \(\sigma\), since
\(\sigma(\exp tX)=\exp(t\theta X)\);
this follows from uniqueness of the invariant ODE, [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Conversely a curve in the fixed group has derivative fixed by \(\theta\). Thus its Lie algebra is \(\ker(\theta-I)\). The inclusions (B.1) make this also the Lie algebra of \(H\).

Since \(\theta^2=I\), each vector splits uniquely as
\(\frac12(X+\theta X)+\frac12(X-\theta X)\), giving (B.2). Differentiation of a group automorphism preserves the Lie bracket, by [Curvature and holonomy A.3](curvature-and-holonomy-groups.md#lemma-a-3). Therefore the bracket of vectors of signs \(\epsilon,\delta\) has sign \(\epsilon\delta\), proving (B.3). For \(h\in H\), \(\sigma(h)=h\), and differentiation of
\(\sigma(hgh^{-1})=h\sigma(g)h^{-1}\)
shows that \(\theta\) commutes with \(\operatorname{Ad}(h)\). This proves invariance of both eigenspaces for the full stabilizer. The quotient and tangent identification are [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) and [Invariant connections A.2](invariant-connections-on-homogeneous-bundles.md#theorem-a-2). □

**Theorem B.2 (Canonical symmetric geometry).** The canonical connection for (B.2) on \(G/H\) is complete, torsion-free and has parallel curvature. At \(o\), with tangent vectors identified with \(\mathfrak m\),
\[
R(X,Y)Z=-[[X,Y],Z].
\tag{B.4}
\]
The geodesic of initial vector \(X\) and its parallel transport are
\[
\gamma_X(t)=\exp(tX)H,\qquad
P_{0\to t}=(dL_{\exp(tX)})_o .
\tag{B.5}
\]
It is globally symmetric, with
\[
s_o(gH)=\sigma(g)H,\qquad
s_{gH}=L_gs_oL_{g^{-1}}.
\tag{B.6}
\]
It is the unique connection invariant under all these point symmetries. Every \(G\)-invariant tensor is parallel. Every \(\operatorname{Ad}(H)\)-invariant nondegenerate symmetric form on \(\mathfrak m\) defines a \(G\)-invariant metric whose Levi-Civita connection is this canonical connection.

**Proof.** [Homogeneous spaces A.2](homogeneous-spaces-and-invariant-connections.md#theorem-a-2) and [Homogeneous spaces B.2](homogeneous-spaces-and-invariant-connections.md#theorem-b-2) construct the canonical connection, whose bilinear product on \(\mathfrak m\) is zero. They prove completeness, (B.5), and parallelism of invariant tensors, torsion and curvature. Their formulas read
\[
T(X,Y)=-[X,Y]_{\mathfrak m},\qquad
R(X,Y)=-\operatorname{ad}([X,Y]_{\mathfrak h})|_{\mathfrak m}.
\]
The bracket inclusions (B.3) give zero torsion and (B.4).

The first map in (B.6) is well-defined because \(\sigma\) fixes each element of \(H\), and is smooth in the quotient charts of [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup). Its square is the identity. It preserves the canonical connection: on \(G\) that connection has horizontal subspaces \(dL_g\mathfrak m\), as constructed in [Invariant connections C.2](invariant-connections-on-homogeneous-bundles.md#theorem-c-2), and
\[
d\sigma_g(dL_g X)=dL_{\sigma(g)}(\theta X).
\]
Thus \(\sigma\) maps horizontal subspaces to horizontal subspaces, and the associated tangent connection is preserved. This associated-connection description and its transport rule are [Linear connections D.1](linear-and-affine-connections.md#theorem-d-1) and [Homogeneous spaces A.2](homogeneous-spaces-and-invariant-connections.md#theorem-a-2). At \(o\) the differential is \(\theta|_{\mathfrak m}=-I\). Translations are affine, so conjugating gives point symmetries at all points. If \(g\) is replaced by \(gh\), \(h\in H\), then \(L_h\) commutes with \(s_o\), directly from \(\sigma(h)=h\). Hence the second map of (B.6) depends only on \(gH\).

For uniqueness, the difference of any two connections is a tensor \(D(X,Y)\), as proved in [Linear connections A.3](linear-and-affine-connections.md#theorem-a-3). If both connections are invariant under every point symmetry, then at its centre,
\[
-D_p(X,Y)=D_p(-X,-Y)=D_p(X,Y).
\]
It follows that \(D=0\). This does not assume that the second connection is \(G\)-invariant.

An invariant form \(B\) on \(\mathfrak m\) defines a smooth tensor by translating it with \(dL_g\); independence of the representative follows from its \(\operatorname{Ad}(H)\)-invariance. This is the tensor construction in [Homogeneous spaces C.1](homogeneous-spaces-and-invariant-connections.md#theorem-c-1), and nondegeneracy is preserved by translation. The invariant tensor is parallel for the canonical connection. Its zero torsion and the Koszul uniqueness proved in A.1 identify it with the metric's Levi-Civita connection for any signature. □

**Theorem B.3 (Recovering a presentation).** Every connected globally symmetric affine manifold has a symmetric presentation with
\[
G=\operatorname{Aff}(M,\nabla)^0,\qquad H=G_o,\qquad
\sigma(g)=s_o g s_o.
\tag{B.7}
\]
Its original connection is the canonical connection of that presentation. For a Riemannian symmetric space one may instead use \(G=\operatorname{Isom}(M)^0\); its stabilizer \(H\) is compact.

**Proof.** The affine group is a Lie group with smooth action by [Affine transformations D.3](affine-transformations-and-the-isometry-group.md#theorem-d-3), and its identity component acts transitively by A.2. The stabilizer is closed. [Invariant connections A.2](invariant-connections-on-homogeneous-bundles.md#theorem-a-2) proves that the orbit map identifies \(G/H\) diffeomorphically with \(M\).

Conjugation by \(s_o\) preserves the identity component and is a smooth group automorphism, by the Lie-group operations and \(s_o^2=1\). It is involutive. If \(h\in H\), then \(hs_oh^{-1}\) fixes \(o\) with differential \(-I\); one-jet uniqueness makes it \(s_o\). Thus \(H\subseteq G^\sigma\).

Conversely every member of \(G^\sigma\) commutes with \(s_o\), hence maps its fixed set to itself. The point \(o\) is isolated in that fixed set, since in its normal neighbourhood \(s_o(\exp_o v)=\exp_o(-v)\), and injectivity of the exponential forces a fixed vector there to be zero. The orbit of \(o\) under the connected group \((G^\sigma)^0\) is a connected subset of the fixed set containing \(o\). The singleton \(\{o\}\) is both open and closed in that fixed set, so this orbit is just \(\{o\}\). Consequently \((G^\sigma)^0\subseteq H\), proving (B.1). No assertion that all other fixed points are isolated was needed.

On the quotient, the action of the original \(s_o\) is \(gH\mapsto\sigma(g)H\), because
\(s_o(g(o))=\sigma(g)(o)\).
Its translates are all the original point symmetries, by (A.5). The canonical connection from B.2 and the given connection are therefore both invariant under this same family. Uniqueness in B.2 makes them equal.

For a Riemannian metric, A.2 supplies transitivity of the isometry identity component, [Affine transformations C.2](affine-transformations-and-the-isometry-group.md#theorem-c-2) supplies its Lie structure and compact stabilizers, and the same argument applies unchanged. □

## C. Integrating maps and tangent subspaces

**Lemma C.1 (Integrating a homomorphism, with parameters).** Let \(K,L\) be Lie groups, with \(K\) connected and simply connected. Every Lie-algebra homomorphism \(\varphi:\mathfrak k\to\mathfrak l\) integrates to a unique smooth group homomorphism \(F:K\to L\). A smooth finite-dimensional family of such \(\varphi\)'s gives a smooth family of the resulting maps. In particular a Lie-algebra involution on a simply connected Lie group integrates to a group involution.

**Proof.** The graph
\[
\mathfrak a=\{(X,\varphi X):X\in\mathfrak k\}
\subseteq\mathfrak k\oplus\mathfrak l
\]
is a subalgebra. [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1) integrates it to a connected immersed subgroup \(A\) of the already existing group \(K\times L\), with its Hausdorff second-countable intrinsic Lie structure. Projection \(p:A\to K\) has invertible differential at the identity and hence everywhere, by translation. Its image is an open subgroup, so is all of connected \(K\). Its kernel is discrete.

Such a surjective local-diffeomorphism homomorphism is a covering. Indeed choose an identity neighbourhood \(U\subset A\) on which \(p\) is a diffeomorphism onto an open set, shrinking so that \(U^{-1}U\) meets \(\ker p\) only at the identity. Every point over \(p(U)\) is uniquely \(u\gamma\) with \(u\in U,\gamma\in\ker p\), so
\[
p^{-1}(p(U))=\coprod_{\gamma\in\ker p}U\gamma .
\]
Each piece maps diffeomorphically onto \(p(U)\). Translates give this property everywhere. Since \(A\) is connected and \(K\) simply connected, [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) makes \(p\) a diffeomorphism. Set \(F=\operatorname{pr}_L\circ p^{-1}\). It is a homomorphism with derivative \(\varphi\).

Any homomorphism with that derivative satisfies
\(F(\exp X)=\exp(\varphi X)\), by uniqueness of one-parameter subgroups in [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). These exponentials generate a connected group, as proved in [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1). This gives uniqueness.

For a family \(\varphi_a\), the formula
\[
F_a(\exp X_1\cdots\exp X_r)
=\exp(\varphi_a X_1)\cdots\exp(\varphi_a X_r)
\tag{C.1}
\]
proves smooth dependence: near a fixed \(k_0\), express \(k_0\) as one fixed finite product of exponentials, and write each nearby point as \(k_0\exp X\) in an exponential chart. The right side of (C.1), with that additional factor, is smooth jointly in \(a,X\). It is the unique previously constructed \(F_a\), so the local formulas agree. If \(\varphi^2=I\), the integrated map's square has identity derivative and therefore is the identity homomorphism by uniqueness; it is an involutive automorphism. □

**Proposition C.2 (The curvature Lie algebra).** At a point \(o\) of a locally symmetric affine manifold put \(\mathfrak m=T_oM\) and
\[
\mathfrak h_R=\operatorname{span}_{\mathbb R}\{R_o(X,Y):X,Y\in\mathfrak m\}
\subseteq\operatorname{End}(\mathfrak m).
\]
On \(\mathfrak h_R\oplus\mathfrak m\), the formulas
\[
[A,B]=AB-BA,\qquad [A,X]=AX,\qquad [X,Y]=-R_o(X,Y)
\tag{C.2}
\]
define a Lie algebra with involution \((A,X)\mapsto(A,-X)\). Its tangent-generated even part is exactly \(\mathfrak h_R\), and the bracket expression \(-[[X,Y],Z]\) is \(R_o(X,Y)Z\).

**Proof.** The curvature of a tensor connection acts on each input and output by the curvature on vectors, by expansion of the tensor-derivative rule in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). Since \(R\) is parallel, applying the curvature commutator to it gives zero. Expanded at \(o\), this is
\[
[R(U,V),R(X,Y)]
=R(R(U,V)X,Y)+R(X,R(U,V)Y).
\tag{C.3}
\]
One can see the two sides directly by applying the tensor curvature to \(R(X,Y)Z\): its output contribution is \(R(U,V)R(X,Y)Z\), and its three input contributions subtract
\(R(R(U,V)X,Y)Z\), \(R(X,R(U,V)Y)Z\), and \(R(X,Y)R(U,V)Z\).
This proves (C.3) for every \(Z\). It makes \(\mathfrak h_R\) closed under commutators. By linearity every \(A\in\mathfrak h_R\) satisfies the same derivation identity with \(A\) in place of \(R(U,V)\).

The Jacobi identity for three even elements is the matrix commutator identity, obtained by cancelling its six associative products. For two even and one odd element it is the defining commutator action on vectors. For one even and two odd elements it is precisely (C.3). For three odd elements it is
\[
R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=0,
\]
the first Bianchi identity for \(T=0\), proved in [Geodesics C.2](geodesics-normal-coordinates-and-curvature.md#theorem-c-2). These four cases give Jacobi by trilinearity. The signs of the two summands in (C.2) show directly that the displayed involution preserves brackets. Its odd-odd brackets span \(\mathfrak h_R\), and substituting \([X,Y]=-R(X,Y)\) into the second formula of (C.2) gives the claimed curvature expression. □

**Theorem C.3 (The local totally geodesic correspondence).** At a point \(o\) of a locally symmetric affine manifold, germs of totally geodesic submanifolds through \(o\) correspond bijectively to subspaces \(V\subseteq T_oM\) satisfying
\[
R_o(V,V)V\subseteq V.
\tag{C.4}
\]
For a symmetric presentation these are exactly the subspaces of \(\mathfrak m\) with
\([[V,V],V]\subseteq V\), called **Lie triple systems**.

**Proof.** Because \(T=0\), a totally geodesic submanifold is autoparallel by [Submanifolds G.1](submanifolds-and-hypersurfaces.md#proposition-g-1). [Submanifolds G.2](submanifolds-and-hypersurfaces.md#proposition-g-2) identifies its curvature with the ambient curvature on tangent vectors, so its tangent space satisfies (C.4).

We prove sufficiency with an explicit local distribution. In a frame identify \(T_oM\) with \(\mathbb R^n\), and use the intrinsic reachable holonomy bundle \(Q\) and its constant-bracket frame from [Geodesics D.3](geodesics-normal-coordinates-and-curvature.md#theorem-d-3). Since torsion is zero and curvature is parallel, its bracket on frame coefficients is (C.2), with the holonomy algebra in the even slot. Each \(R_o(X,Y)\) belongs to that holonomy algebra by [Curvature and holonomy G.3](curvature-and-holonomy-groups.md#theorem-g-3).

Let \(\mathfrak h_V\) be the span of \(R_o(v,w)\) with \(v,w\in V\). Condition (C.4) makes each element of \(\mathfrak h_V\) preserve \(V\). Equation (C.3) then shows that \(\mathfrak h_V\) is closed under commutators. Thus
\(\mathfrak h_V\oplus V\)
is a subalgebra of the frame algebra. The constant-coefficient frame fields with these values span a smooth distribution of constant rank \(\dim\mathfrak h_V+\dim V\) on \(Q\), and the bracket formula makes it involutive. [De Rham decomposition B.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-b-2) gives a local integral submanifold through the selected frame \(u_o\).

Projection of this integral submanifold to \(M\) has constant rank \(\dim V\): its solder values are exactly \(V\), while its kernel has connection-form values \(\mathfrak h_V\). The constant-rank and submersion coordinate theorems, [Local tools 1.4](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) and [Local tools 1.3](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), give a local embedded image \(N\) through \(o\) and a smooth section \(u:N\to Q\) of this projection taking values in the integral submanifold. Its frames satisfy
\[
T_xN=u_xV,\qquad u^*\omega(TN)\subseteq\mathfrak h_V.
\]
If a tangent field has frame coefficient \(v(x)\in V\), the ambient derivative along \(N\) has coefficient
\[
dv+u^*\omega\,v\in V.
\]
This is the connection formula of [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2); the inclusion uses invariance of \(V\) under \(\mathfrak h_V\). Hence \(N\) is autoparallel, and therefore totally geodesic.

Uniqueness is local: any such submanifold's geodesics through \(o\) are the ambient geodesics with initial vectors in \(V\). Its own exponential is a local diffeomorphism at zero by [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). Consequently its image near \(o\) is exactly \(\exp_o(V)\) on a small neighbourhood of zero. This determines the germ. Finally (B.4) identifies (C.4) with the Lie triple system condition in a symmetric presentation. □

**Theorem C.4 (The complete immersed image).** In a globally symmetric affine manifold, every Lie triple system \(V\subseteq T_oM\) has a connected complete injectively immersed totally geodesic image through \(o\). It is unique with its intrinsic orbit topology. The image need not be closed or embedded; different covering parametrizations are not different immersed images.

**Proof.** Use the presentation \(G/H\) of B.3 and set
\[
\mathfrak l=[V,V]\oplus V\subseteq\mathfrak h\oplus\mathfrak m.
\tag{C.5}
\]
The Lie triple system condition gives \([[V,V],V]\subseteq V\). Jacobi gives
\[
[[x,y],[z,w]]
=[[[x,y],z],w]+[z,[[x,y],w]],
\]
so \([[V,V],[V,V]]\subseteq[V,V]\). Thus (C.5) is a subalgebra, stable under \(\theta\).

Let \(L\) be its connected immersed subgroup in \(G\), with the intrinsic Lie structure provided by [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1). Write \(i:L\to G\) for the injective immersion. The automorphism \(\sigma\) preserves this subgroup and is smooth in its intrinsic structure: it sends each exponential word to the word obtained by applying \(\theta\), and those word charts are the construction in that lemma. Put \(H_L=i^{-1}(H)\), closed in \(L\). Its Lie algebra is \([V,V]\). The restricted involution has this as its positive eigenspace and \(V\) as its negative eigenspace. Its connected fixed group is generated by the exponentials of \([V,V]\), hence is contained in \(H_L\), while \(H_L\) is itself fixed by the involution. We therefore have a symmetric presentation for \(L/H_L\).

The induced map
\[
j:L/H_L\longrightarrow G/H,\qquad \ell H_L\longmapsto i(\ell)H
\tag{C.6}
\]
is injective by the definition of \(H_L\). Its derivative at the origin is the injection \(V\hookrightarrow\mathfrak m\), and translation gives injectivity everywhere. Thus it is an injective immersion. The horizontal spaces defining its canonical connection, \(dL_\ell V\), map into the ambient canonical horizontal spaces \(dL_{i(\ell)}\mathfrak m\). The associated tangent connections therefore agree along (C.6), by the construction used in B.2. It is autoparallel and totally geodesic, and B.2 makes its induced connection complete.

For the uniqueness assertion, suppose \(f:N\to M\) is another connected complete injectively immersed totally geodesic submanifold with the same point and tangent space. Its induced torsion is zero and its curvature is parallel, by [Submanifolds G.2](submanifolds-and-hypersurfaces.md#proposition-g-2). These properties also hold for \(L/H_L\). Their local germs agree by C.3, giving a local affine isomorphism. Pass to the connected universal covers of both. [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) constructs the covers, and [Hopf–Rinow E.3](completeness-and-the-hopf-rinow-theorem.md#theorem-e-3) proves that covering an affine complete manifold preserves geodesic completeness. [Killing fields C.1](holonomy-killing-fields-and-analytic-extension.md#theorem-c-1) extends the lifted local isomorphism to a global affine isomorphism of the simply connected covers.

The two compositions of this isomorphism with the immersions into \(M\) have the same initial value and differential. [Affine transformations A.1](affine-transformations-and-the-isometry-group.md#lemma-a-1) makes these maps equal on the connected cover. Hence their images coincide. Moreover two covering points have the same projection to \(N\) exactly when their common images in \(M\) are equal, because \(f\) is injective; the same holds for (C.6). Thus the isomorphism of covers identifies exactly the same fibres and descends to a bijective local affine isomorphism \(N\to L/H_L\), which is a diffeomorphism. This verifies equality of the intrinsic topologies as well as the images. Allowing covering parametrizations before taking the injective image gives the same conclusion about the image, as stated.

To exhibit the possible failure of embeddedness, take the flat torus \(\mathbb R^2/\mathbb Z^2\) and an irrational real number \(a\). The map
\[
\mathbb R\longrightarrow\mathbb R^2/\mathbb Z^2,\qquad
t\longmapsto[(t,at)]
\tag{C.7}
\]
is an injective geodesic immersion: equality of two images would make \(t-s\) and \(a(t-s)\) integers, forcing \(t=s\). Its induced metric is \((1+a^2)\,dt^2\), hence complete.

Its image is dense. For any positive integer \(N\), the \(N+1\) fractional parts of \(0,a,\ldots,Na\) occupy \(N\) equal subintervals of \([0,1]\). Two have distance at most \(1/N\); their difference yields a nonzero integer \(q\) and an integer \(p\) with \(0<|qa-p|\leq1/N\). Changing the sign makes \(qa-p=\delta>0\). Multiples of \(\delta\), up to the last one below \(1\), approximate every number in \([0,1]\) within \(\delta\), and modulo \(1\) they are fractional parts of integer multiples of \(a\). This proves density of those fractional parts. To approximate a prescribed torus point \([(x,y)]\), use \(t=x+m\), \(m\in\mathbb Z\), and approximate \(y-ax\) modulo \(1\) by \(ma\).

The image is proper: over first coordinate zero it has only the countable set \([ma]\) of second coordinates, whereas a circle has uncountably many points. For the latter elementary fact one may use the binary-sequence diagonal argument: no listing includes the sequence differing in its \(j\)-th digit from the \(j\)-th listed sequence, and binary sequences inject into the ternary expansion \(\sum 2b_j3^{-j}\) in \([0,1]\). An embedded one-dimensional submanifold of a surface is locally a coordinate line, by the immersion chart theorem [Local tools 1.4](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), so cannot have a dense image: a small ambient coordinate ball would contain open points off that line. Thus (C.7) is neither closed nor embedded, although its intrinsic orbit is a complete line. □

## D. Compact spaces and every invariant metric

**Lemma D.1 (An invariant positive form by integration).** A compact Lie group \(G\) has an \(\operatorname{Ad}(G)\)-invariant positive definite inner product on its Lie algebra. If \(\sigma\) is an involutive automorphism, the inner product can also be chosen invariant under \(\theta=d\sigma_e\).

**Proof.** Choose a positive inner product at the identity and translate it on the left to a smooth Riemannian metric. Its volume density \(\mu\) is left invariant. Integration of densities, positivity and the change-of-variables formula on a compact manifold were proved in [Killing fields F.1](holonomy-killing-fields-and-analytic-extension.md#lemma-f-1); no orientation is needed. For each \(h\in G\), \(R_h^*\mu\) is also left invariant, because right and left translations commute. Two positive left-invariant densities differ by one positive constant, determined at the identity. Write \(R_h^*\mu=c(h)\mu\). Change of variables gives
\[
c(h)\int_G\mu=\int_G R_h^*\mu=\int_G\mu.
\]
The integral is finite and strictly positive, so \(c(h)=1\). Normalize \(\mu\) to have integral one.

For any positive inner product \(\langle\, ,\,\rangle\) on \(\mathfrak g\), set
\[
Q_0(X,Y)=\int_G\langle\operatorname{Ad}(g)X,\operatorname{Ad}(g)Y\rangle\,\mu(g).
\tag{D.1}
\]
This is symmetric bilinear and positive definite: for \(X\ne0\) its squared integrand is everywhere positive. Right invariance of \(\mu\), with the substitution \(g\mapsto gh\), proves
\(Q_0(\operatorname{Ad}(h)X,\operatorname{Ad}(h)Y)=Q_0(X,Y)\).
Finally set
\[
Q(X,Y)=\tfrac12\bigl(Q_0(X,Y)+Q_0(\theta X,\theta Y)\bigr).
\tag{D.2}
\]
It is positive and \(\theta\)-invariant. The identity
\(\theta\operatorname{Ad}(h)=\operatorname{Ad}(\sigma(h))\theta\)
shows that the second summand is also \(\operatorname{Ad}(G)\)-invariant. This proves the lemma without assuming an integration theorem for compact groups beyond the proved density calculus. □

**Theorem D.2 (Curvature for every compact symmetric metric).** Let \(M\) be a compact connected Riemannian symmetric space with its given metric. In the presentation of B.3 use \(G=\operatorname{Isom}(M)^0\) and \(T_oM=\mathfrak m\). Let \(Q\) be as in D.1, and write the given inner product as
\[
B(X,Y)=Q(SX,Y)\quad(X,Y\in\mathfrak m).
\]
The positive \(Q\)-self-adjoint operator \(S\) has orthogonal eigenspaces \(E_a\), with distinct eigenvalues \(c_a>0\). They satisfy
\[
[E_a,E_b]=0\quad(a\ne b).
\tag{D.3}
\]
For \(X=\sum_a X_a\), \(Y=\sum_aY_a\) with \(X_a,Y_a\in E_a\),
\[
B(R(X,Y)Y,X)=\sum_a c_a\,Q([X_a,Y_a],[X_a,Y_a]).
\tag{D.4}
\]
Thus all sectional curvatures are nonnegative, and a two-plane is flat exactly when every bracket \([X_a,Y_a]\) vanishes. This includes flat factors and arbitrary invariant metric scales.

**Proof.** [Affine transformations C.2](affine-transformations-and-the-isometry-group.md#theorem-c-2) proves that the isometry group of a compact Riemannian manifold is compact. Hence its closed identity component \(G\) is compact, so D.1 applies. As \(\theta\) preserves \(Q\), its positive and negative eigenspaces are \(Q\)-orthogonal. The positive form \(B\) on \(\mathfrak m\) determines \(S\) by solving the finite-dimensional linear system for its matrix in a \(Q\)-orthonormal basis. Symmetry and positivity of \(B\) make \(S\) self-adjoint and positive. The spectral theorem, [De Rham decomposition H.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-h-2), gives the asserted eigenspaces.

Invariance of \(B\) and \(Q\) under \(H\) implies that \(S\) commutes with \(\operatorname{Ad}(H)|_{\mathfrak m}\). Differentiating shows that it commutes with \(\operatorname{ad}(A)|_{\mathfrak m}\) for \(A\in\mathfrak h\). By (B.4), every \(R(X,Y)\) therefore preserves each \(E_a\). Differentiating the \(\operatorname{Ad}(G)\)-invariance of \(Q\) also gives
\[
Q([A,U],V)+Q(U,[A,V])=0 .
\tag{D.5}
\]
Consequently (B.4) gives, for any \(X,Y\in\mathfrak m\),
\[
Q(R(X,Y)Y,X)
=-Q([[X,Y],Y],X)
=Q([X,Y],[X,Y]).
\tag{D.6}
\]
If \(X\in E_a,Y\in E_b\) with \(a\ne b\), the left side is zero: \(R(X,Y)Y\in E_b\), which is orthogonal to \(E_a\). Positive definiteness of \(Q\) proves (D.3).

Now expand \([X,Y]=\sum_a[X_a,Y_a]\). If \(a\ne b\), Jacobi and (D.3) imply
\[
[[X_a,Y_a],Y_b]
=[X_a,[Y_a,Y_b]]-[Y_a,[X_a,Y_b]]=0.
\]
For a fixed \(a\), the remaining vector \(-[[X_a,Y_a],Y_a]\) belongs to \(E_a\), since it is \(R(X_a,Y_a)Y_a\). The eigenspaces are orthogonal for \(B\) as well as \(Q\). Pairing the resulting curvature sum with \(X\), and then using (D.6), gives exactly (D.4). Each summand is nonnegative and each \(c_a\) positive, proving its equality criterion. For independent \(X,Y\), division by
\(B(X,X)B(Y,Y)-B(X,Y)^2>0\)
gives the sectional assertion; positivity of that denominator is the Gram-matrix argument in [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). No assertion that \(B\) itself extends to an invariant form on all of \(\mathfrak g\) was used. □

## E. Matrix models and normalizations

**Example E.1 (Spheres and real projective spaces).** The unit sphere \(S^n\), \(n\geq1\), and real projective space \(\mathbb{RP}^n\) with its quotient round metric are symmetric. Their curvature tensor, under the natural tangent identification, is
\[
R(v,w)z=\langle w,z\rangle v-\langle v,z\rangle w.
\tag{E.1}
\]
For \(n\geq2\) their sectional curvature is one.

**Proof.** Take \(G=SO(n+1)\) and conjugate it by the orthogonal matrix
\(J=\operatorname{diag}(1,-I_n)\).
This defines an involution even when \(J\notin SO(n+1)\). The closed-subgroup theorem [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1) and differentiation of \(A^TA=I\) identify the Lie algebra as the skew-symmetric matrices; conversely the exponential of a skew-symmetric matrix is orthogonal with determinant one, so every such tangent vector occurs. Connectedness follows from the plane-rotation construction in [Affine transformations G.1](affine-transformations-and-the-isometry-group.md#theorem-g-1). The negative eigenspace consists of
\[
X(v)=
\begin{pmatrix}0&-v^T\\v&0\end{pmatrix}.
\]
The subgroup \(H=\operatorname{diag}(1,SO(n))\) lies between the identity component and the full fixed group of the involution. Completing a unit vector to an oriented orthonormal basis proves transitivity on \(S^n\); its stabilizer at the first coordinate vector is \(H\). The orbit theorem [Invariant connections A.2](invariant-connections-on-homogeneous-bundles.md#theorem-a-2) therefore identifies \(G/H\) with \(S^n\), and \(X(v)\) differentiates to \(v\). The metric \(v\cdot w\) is \(H\)-invariant. Its homogeneous extension is the usual induced round metric, since orthogonal matrices preserve the Euclidean inner product.

Matrix multiplication gives
\[
[X(v),X(w)]=
\begin{pmatrix}0&0\\0&-vw^T+wv^T\end{pmatrix}.
\]
The lower left block of its bracket with \(X(z)\) is
\(-v\langle w,z\rangle+w\langle v,z\rangle\).
Formula (B.4) proves (E.1), and its inner product with \(v\) when \(z=w\) proves the curvature value. The symmetry at \(p\in S^n\) is the ambient orthogonal map
\[
x\longmapsto 2\langle p,x\rangle p-x:
\]
it fixes \(p\), has differential \(-I\) on its tangent space, and preserves the round metric.

For projective space take instead the full fixed group
\(H'=S(O(1)\times O(n))\), the stabilizer of an unoriented line. The same transitive action identifies \(G/H'\) with the space of real lines, whose smooth graph charts are [Submanifolds A.4](submanifolds-and-hypersurfaces.md#proposition-a-4) with rank one. Its tangent data and curvature formula are unchanged. The map \(S^n\to\mathbb{RP}^n\) identifies precisely \(p\) and \(-p\); in a neighbourhood where a fixed coordinate has a chosen nonzero sign it is a diffeomorphism onto a projective chart. These charts make it a double covering and define the quotient metric by local isometry. The displayed point reflection commutes with \(x\mapsto-x\), so descends to the required projective symmetry. In dimension one there are no two-dimensional tangent planes; (E.1) still holds, with zero curvature tensor. □

For the next example, \(Z^*\) denotes transpose in the real case and conjugate transpose in the complex case. All tangent spaces and metrics in the complex case are considered as real.

**Example E.2 (Real and complex Grassmannians).** Let \(k,l\geq1\). On the Grassmannian of \(k\)-planes in \(\mathbb F^{k+l}\), with \(\mathbb F=\mathbb R\) or \(\mathbb C\), identify a tangent vector at the standard \(k\)-plane with a matrix \(Z:\mathbb F^k\to\mathbb F^l\). The invariant metric
\[
B(Z,W)=\operatorname{Re}\operatorname{tr}(Z^*W)
\tag{E.2}
\]
is symmetric and complete. Put
\[
A=-Z^*W+W^*Z,\qquad D=-ZW^*+WZ^*.
\]
Its curvature is
\[
R(Z,W)U=UA-DU,\qquad
B(R(Z,W)W,Z)=\tfrac12(\|A\|_{\mathrm{HS}}^2+\|D\|_{\mathrm{HS}}^2).
\tag{E.3}
\]
For complex lines, this normalizes \(\mathbb{CP}^{l}\) so that a real orthonormal pair \(z,w\) has sectional curvature
\[
K(z,w)=1+3\bigl(\operatorname{Im}(z^*w)\bigr)^2.
\tag{E.4}
\]

**Proof.** Use \(G=SO(k+l)\) in the real case and \(G=U(k+l)\) in the complex case. These are closed matrix Lie groups by [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). Their Lie algebras consist of skew-adjoint matrices: differentiation gives this condition, and the matrix exponential supplies the converse. The real group is connected by [Affine transformations G.1](affine-transformations-and-the-isometry-group.md#theorem-g-1). A unitary matrix has an orthonormal eigenbasis by [Sectional curvature I.1](sectional-curvature-and-space-forms.md#lemma-i-1), and its eigenvalues are \(e^{it_j}\) with real \(t_j\), by [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). Conjugating \(\operatorname{diag}(e^{ist_j})\), \(0\leq s\leq1\), by that eigenbasis gives a path from the identity to the matrix. Thus the complex group is connected too.

Conjugation by \(\operatorname{diag}(I_k,-I_l)\) is an involution. Its full fixed subgroup is
\[
H=S(O(k)\times O(l))\quad\hbox{or}\quad H=U(k)\times U(l),
\]
respectively. The action on planes is transitive: choose orthonormal bases of a plane and its orthogonal complement. In the real case one may change the sign of a basis vector to ensure determinant one, without changing the plane. The stabilizer is precisely \(H\). To specify the smooth structure explicitly, near the standard plane each transverse plane is the graph of a unique matrix \(Z\). With \(J_Z=\binom{I_k}{Z}\), its orthogonal projection is
\[
P_Z=J_Z(J_Z^*J_Z)^{-1}J_Z^* .
\]
Indeed this matrix is self-adjoint, has square itself, and is the identity on the image of \(J_Z\). Conversely a nearby rank-\(k\) projection has invertible upper block on that image, which recovers its graph matrix. The entries and inverse depend smoothly on real and imaginary parts. This is the graph-chart construction of [Submanifolds A.4](submanifolds-and-hypersurfaces.md#proposition-a-4), with the same verification over \(\mathbb C\). [Invariant connections A.2](invariant-connections-on-homogeneous-bundles.md#theorem-a-2) now identifies this manifold with \(G/H\).

Its odd tangent matrices are
\[
X(Z)=\begin{pmatrix}0&-Z^*\\Z&0\end{pmatrix}.
\]
Their derivatives as graphs are \(Z\), and direct multiplication gives
\([X(Z),X(W)]=\operatorname{diag}(A,D)\).
The lower left block of
\([\operatorname{diag}(A,D),X(U)]\) is \(DU-UA\); this proves the first equation in (E.3) by B.2. The form (E.2) is invariant under the stabilizer action \(Z\mapsto h_lZh_k^{-1}\), since the two factors are orthogonal or unitary and the trace is cyclic. It therefore defines a complete symmetric metric by B.2.

On the full skew-adjoint Lie algebra use
\[
Q(U,V)=-\tfrac12\operatorname{Re}\operatorname{tr}(UV).
\]
It is an invariant positive inner product: cyclicity proves invariance, while
\(Q(U,U)=\frac12\operatorname{tr}(U^*U)\)
is positive for \(U\ne0\). Its restriction to the odd matrices is (E.2), as multiplication of the two block matrices verifies. Formula (D.6) makes the curvature numerator the squared \(Q\)-norm of \(\operatorname{diag}(A,D)\), which is the second equation in (E.3).

For complex lines \(k=1\), real orthonormality means
\(z^*z=w^*w=1\) and \(\operatorname{Re}(z^*w)=0\).
Write \(z^*w=ia\), \(a\in\mathbb R\). Then \(A=-2ia\), so \(\|A\|^2=4a^2\). Also
\[
\begin{aligned}
\|D\|_{\mathrm{HS}}^2
&=-\operatorname{tr}\bigl((-zw^*+wz^*)^2\bigr)\\
&=-\bigl((w^*z)^2-1-1+(z^*w)^2\bigr)
=2+2a^2.
\end{aligned}
\]
This proves (E.4). The complex Cauchy–Schwarz inequality follows by expanding
\(\|w-(z^*w)z\|^2\geq0\), and gives \(|a|\leq1\).
Thus \(1\leq K\leq4\). A complex line, represented by \(w=iz\), has curvature four. When \(l\geq2\), choosing \(z,w\) complex orthogonal gives curvature one. For \(l=1\) every real tangent two-plane is the complex line, so only curvature four occurs. □

**Example E.3 (A compact group with a bi-invariant metric).** Every compact connected Lie group \(K\) has bi-invariant Riemannian metrics. For any such metric with identity inner product \(B\),
\[
\begin{aligned}
\nabla_{X^L}Y^L&=\tfrac12[X,Y]^L,\\
R(X,Y)Z&=-\tfrac14[[X,Y],Z],\\
B(R(X,Y)Y,X)&=\tfrac14\|[X,Y]\|_B^2 .
\end{aligned}
\tag{E.5}
\]
It is a complete symmetric metric, with \(s_p(q)=pq^{-1}p\).

**Proof.** An \(\operatorname{Ad}(K)\)-invariant positive inner product exists by D.1. Translate it on the left. Right translation also preserves this metric, because its differential in left trivialization is the appropriate adjoint map. Conversely a bi-invariant metric has an \(\operatorname{Ad}(K)\)-invariant identity inner product by conjugating left and right translations.

Use \(G=K\times K\), \(\sigma(a,b)=(b,a)\) and \(H=\operatorname{diag}K\). The action \((a,b)\cdot q=aqb^{-1}\) is transitive with stabilizer \(H\). Its odd tangent vector \((X/2,-X/2)\) differentiates at the identity to \(X\). The metric \(B\) is \(H\)-invariant, so B.2 identifies its Levi-Civita connection with the canonical one and proves completeness and symmetry. Its point symmetry at the identity is inversion, directly from swapping the two factors; conjugating by left translation gives \(s_p(q)=pq^{-1}p\).

The bracket of \((X/2,-X/2)\) and \((Y/2,-Y/2)\) is
\(( [X,Y]/4,[X,Y]/4)\).
Its bracket with \((Z/2,-Z/2)\) is
\(( [[X,Y],Z]/8,-[[X,Y],Z]/8)\),
which differentiates to \([[X,Y],Z]/4\). Formula (B.4) therefore gives the curvature factor \(1/4\). The identity for the connection on left-invariant fields follows from [Homogeneous spaces C.3](homogeneous-spaces-and-invariant-connections.md#example-c-3), or by substituting the adjoint-skew identity (D.5) into the Koszul formula of A.1. Finally that same adjoint-skew identity gives the last formula in (E.5). If \(K\) is abelian all the brackets vanish, so this includes flat compact groups. □

## F. A neutral metric on the tangent bundle

**Example F.1 (The tangent-group construction).** Let \(G/H\) be a symmetric presentation, and let \(B\) be a positive \(\operatorname{Ad}(H)\)-invariant form on \(\mathfrak m\). If \(n=\dim\mathfrak m\), its tangent bundle has a complete symmetric pseudo-Riemannian metric of signature \((n,n)\). At the zero vector over \(o\), identify its tangent space with \(\mathfrak m\oplus\mathfrak m\); the metric is
\[
\widehat B((X,U),(Y,V))=B(X,V)+B(U,Y).
\tag{F.1}
\]

**Proof.** Form the semidirect-product Lie group
\[
\widehat G=G\ltimes_{\operatorname{Ad}}\mathfrak g,\qquad
(g,u)(h,v)=(gh,u+\operatorname{Ad}(g)v).
\tag{F.2}
\]
Associativity follows by substituting \(\operatorname{Ad}(gh)=\operatorname{Ad}(g)\operatorname{Ad}(h)\); the identity is \((e,0)\), and the inverse of \((g,u)\) is \((g^{-1},-\operatorname{Ad}(g^{-1})u)\). These formulas are smooth on the product manifold. Connectedness follows from connectedness of \(G\) and of the vector space. Differentiating the two adjoint actions in the group commutator gives its Lie bracket
\[
[(X,U),(Y,V)]=([X,Y],[X,V]-[Y,U]).
\tag{F.3}
\]
For clarity, the mixed term can be obtained without a commutator expansion: conjugating \((e,tV)\) by \((\exp sX,0)\) gives \((e,t\operatorname{Ad}(\exp sX)V)\); differentiating first in \(t\) and then in \(s\) gives \([X,V]\). The vector subgroup is abelian, and the bracket of the first factors is the bracket of \(G\), proving all terms in (F.3).

The involution is
\(\widehat\sigma(g,u)=(\sigma(g),\theta u)\).
It respects (F.2) by \(\theta\operatorname{Ad}(g)=\operatorname{Ad}(\sigma(g))\theta\). Its fixed group is \(G^\sigma\ltimes\mathfrak h\). Thus the closed subgroup
\(\widehat H=H\ltimes\mathfrak h\)
lies between that fixed group's identity component and full fixed group. The even and odd Lie-algebra spaces are respectively
\(\mathfrak h\oplus\mathfrak h\) and \(\mathfrak m\oplus\mathfrak m\).

Here is an explicit identification of \(\widehat G/\widehat H\) with \(T(G/H)\). Write \(u_M(x)\) for the velocity at zero of \(\exp(tu)\cdot x\). Define
\[
(g,u)\cdot(x,v)=\bigl(gx,(dL_g)_xv+u_M(gx)\bigr).
\tag{F.4}
\]
The identity
\((dL_g)v_M(x)=(\operatorname{Ad}(g)v)_M(gx)\)
follows by differentiating
\(g\exp(tv)=\exp(t\operatorname{Ad}(g)v)g\).
It makes successive applications of (F.4) equal the multiplication (F.2), so this is a smooth action. It is transitive: first move \(o\) to any prescribed \(x\), then use the surjection \(\mathfrak g\to T_x(G/H)\), established by the transitive orbit theorem [Invariant connections A.2](invariant-connections-on-homogeneous-bundles.md#theorem-a-2), to add any tangent vector. Its stabilizer at \((o,0)\) consists exactly of \(g\in H\) and \(u\in\mathfrak h\). The same orbit theorem gives the claimed diffeomorphism. At \((o,0)\), the differential of the orbit map on the odd space is \((X,U)\), where the first component moves the zero section and the second moves the vertical vector. This is the splitting used in (F.1).

It remains to check invariance of the proposed metric under the full stabilizer. Conjugation by \((h,0)\), \(h\in H\), acts on the odd space by
\((X,U)\mapsto(\operatorname{Ad}(h)X,\operatorname{Ad}(h)U)\),
which preserves (F.1). For \(a\in\mathfrak h\), conjugation by \((e,a)\) in (F.2), differentiated at the identity, gives
\[
(X,U)\longmapsto(X,U+[a,X]).
\tag{F.5}
\]
The change in (F.1) under (F.5) is
\(B(X,[a,Y])+B([a,X],Y)\).
This is zero by differentiating the \(H\)-invariance of \(B\) along \(\exp(ta)\). These elements generate \(\widehat H\), since \((h,a)=(e,a)(h,0)\), so full stabilizer invariance is proved.

The form is nondegenerate: pairing \((X,U)\) against every \((0,V)\) forces \(X=0\), and pairing against every \((Y,0)\) then forces \(U=0\). The subspaces \(\{(X,X)\}\) and \(\{(X,-X)\}\) are orthogonal, each has dimension \(n\), and their restricted forms are \(2B\) and \(-2B\). Hence its signature is \((n,n)\). The symmetric-presentation theorem B.2 now makes the homogeneous metric's Levi-Civita connection canonical, complete and globally symmetric. In particular every positive-dimensional compact example of Part E produces a concrete complete indefinite symmetric space on its tangent bundle. □

## G. Exercises with solutions

**Exercise G.1 (The group normalization).** Starting with a compact connected group and a bi-invariant positive metric, identify its symmetric quotient and derive the curvature coefficient, including its numerical factor.

**Solution.** The quotient is \((K\times K)/\operatorname{diag}K\), with factor-swap involution. Under the action \((a,b)q=aqb^{-1}\), its tangent map is \((U,V)\mapsto U-V\). Therefore the tangent vector corresponding to \(X\) is \((X/2,-X/2)\), rather than \((X,-X)\). Two brackets give
\[
\left[\left[\left(\frac X2,-\frac X2\right),
                      \left(\frac Y2,-\frac Y2\right)\right],
                      \left(\frac Z2,-\frac Z2\right)\right]
=\left(\frac{[[X,Y],Z]}8,-\frac{[[X,Y],Z]}8\right).
\]
The tangent map subtracts the components, giving \([[X,Y],Z]/4\). B.2 puts a minus sign in front for curvature, so the answer is \(-[[X,Y],Z]/4\). Example E.3 proves that the given metric is exactly the invariant quotient metric and that its Levi-Civita connection is canonical. Its point symmetry is \(q\mapsto pq^{-1}p\). Invariance of the identity metric makes the curvature numerator \(\|[X,Y]\|^2/4\), also proved there. □

**Exercise G.2 (Where zero torsion enters).** Prove the local reflection criterion without assuming analyticity. Separate the roles of torsion and parallel curvature, and give a complete locally symmetric manifold where some local point reflection does not extend.

**Solution.** At a centre with differential \(-I\), naturality of the torsion tensor compares one output sign with two input signs and gives \(-T=T\). Naturality of \(\nabla R\) compares one output sign with four input signs and gives \(-\nabla R=\nabla R\). Thus affine reflections force both \(T=0\) and \(\nabla R=0\); no zero-torsion assumption is used in taking these naturality identities.

For the converse, \(T=0\) supplies both \(\nabla T=0\) and preservation of \(T\) by \(-I\). Parallel curvature supplies \(\nabla R=0\), while its three inputs and one output make \(-I\) preserve \(R\). These are exactly the hypotheses of [Killing fields C.1](holonomy-killing-fields-and-analytic-extension.md#theorem-c-1). Its smooth reconstruction proves the local affine map, and exponential naturality identifies it with the geodesic reflection. This is the complete argument of A.1; it does not assume analytic Christoffel symbols. With a Levi-Civita connection, torsion is already zero by its construction, so only parallel curvature must be tested. The parallel-metric argument in A.1 works for any signature.

Finally use the flat Klein bottle of A.3. It is complete and has \(T=R=0\). A point symmetry at the image of \((a,b)\) would lift to \((x,y)\mapsto(2a-x,2b-y)\). Conjugation of its glide-reflection deck transformation gives \((x,y)\mapsto(4a-x,y-1)\), which belongs to the deck group only if \(4a\in\mathbb Z\). At \(a=1/8\) it does not. Completeness alone therefore cannot replace simple connectivity in A.2. □

**Exercise G.3 (A tangent subspace and its complete orbit).** Characterize tangent subspaces of totally geodesic germs in a symmetric space, identify the Lie algebra generated by such a subspace, and explain the intrinsic topology of an irrational geodesic in a flat two-torus.

**Solution.** By C.3 the condition is \(R(V,V)V\subseteq V\), or equivalently \([[V,V],V]\subseteq V\) using B.2. The generated algebra is
\(\mathfrak l=[V,V]\oplus V\).
The odd-odd brackets give its even summand, the triple condition gives its even-odd closure, and the Jacobi expansion in C.4 gives its even-even closure. Hence it is a subalgebra containing \(V\); every subalgebra containing \(V\) must contain \([V,V]\), so it is precisely the generated algebra.

Its connected analytic subgroup \(L\) yields the injectively immersed complete image \(L/(L\cap H)\), with the intersection taken in the intrinsic group topology. C.4 proves both completeness and uniqueness of that topology among complete injective totally geodesic images with this tangent space. For the flat torus and a line of irrational slope \(a\), the parametrization \(t\mapsto[(t,at)]\) is injective, since a nonzero period would make \(a\) rational. Its induced metric is \((1+a^2)dt^2\). The pigeonhole argument in C.4 proves that its image is dense and proper. Thus its intrinsic manifold is a complete copy of \(\mathbb R\), while the subspace topology of its dense image is not the topology of an embedded one-dimensional submanifold. A covering parametrization would not define an additional immersed image. □

**Exercise G.4 (All compact metric scales).** Obtain a bracket formula for the sectional curvature of a compact Riemannian symmetric space with its given metric, permitting unequal invariant scales and flat factors.

**Solution.** D.1 supplies a positive adjoint- and involution-invariant form \(Q\) on the compact isometry algebra. Express the given tangent metric as \(B=Q(S\,\cdot,\cdot)\). D.2 proves the orthogonal spectral splitting \(S|_{E_a}=c_aI\), \(c_a>0\), and the cross-bracket identity \([E_a,E_b]=0\) for \(a\ne b\). Its proof uses only isotropy invariance of \(B\), not adjoint invariance on the full algebra. For independent tangent vectors the required value is therefore
\[
K(X,Y)=
\frac{\sum_a c_a\|[X_a,Y_a]\|_Q^2}
{B(X,X)B(Y,Y)-B(X,Y)^2}.
\]
The denominator is positive, and every numerator summand is nonnegative. The plane is flat exactly when all its summand brackets vanish. A flat factor contributes zero brackets and hence zero to the numerator, with its lengths still present in the denominator. This establishes the assertion for the given metric and all its invariant scales. □

## H. The algebra behind the decomposition

All Lie algebras and modules in Parts H–J are finite dimensional over \(\mathbb R\) or \(\mathbb C\). Brackets of subspaces mean their linear span. An ideal \(I\) satisfies \([\mathfrak g,I]\subseteq I\). Write
\[
D^0\mathfrak g=\mathfrak g,\quad D^{j+1}\mathfrak g=[D^j\mathfrak g,D^j\mathfrak g],
\qquad
C^1\mathfrak g=\mathfrak g,\quad C^{j+1}\mathfrak g=[\mathfrak g,C^j\mathfrak g].
\]
The algebra is **solvable** if some \(D^j\mathfrak g\) is zero, and **nilpotent** if some \(C^j\mathfrak g\) is zero. It is **semisimple** if it has no nonzero solvable ideal, and **simple** if it is nonabelian and has no nonzero proper ideal. The following proofs supply the algebraic prerequisites without an appeal to a classification or to an unproved representation theorem.

**Lemma H.1 (Polynomial splitting and Jordan parts).** Every endomorphism \(A\) of a finite-dimensional complex vector space has a unique decomposition
\[
A=S+N,\qquad [S,N]=0,
\]
where \(S\) is diagonalizable and \(N\) nilpotent. Both are polynomials in \(A\). The endomorphism \(\operatorname{ad}A\) of \(\operatorname{End}(V)\) has semisimple part \(\operatorname{ad}S\). If \(\overline S_{\mathrm{eig}}\) has the same eigenspaces as \(S\), with conjugate eigenvalues, then
\[
\operatorname{ad}S=P(\operatorname{ad}A),\qquad
\operatorname{ad}\overline S_{\mathrm{eig}}=Q(\operatorname{ad}A),
\quad P(0)=Q(0)=0.
\tag{H.1}
\]
Here conjugating the eigenvalues does not mean conjugating matrix entries in an arbitrary basis. For real \(A\), its Jordan parts are real. If \(A\) is a derivation of a Lie algebra, so are its Jordan parts.

**Proof.** We include the polynomial facts needed in this argument. A nonconstant complex polynomial has a root. Indeed its modulus tends to infinity at infinity, by its leading term, so it attains a global minimum on a closed disk, using compactness from [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). If its value at a minimizing point \(z_0\) were nonzero, write
\[
\frac{p(z_0+w)}{p(z_0)}=1+aw^k+O(|w|^{k+1}),\quad a\ne0,\quad k\geq1.
\]
The remainder bound follows directly from the finite polynomial sum. By the circle parametrization in [Connections E.1](connections-and-parallel-transport.md#lemma-e-1) choose \(|\xi|=1\) with \(a\xi^k=-|a|\). For sufficiently small \(r>0\), the remainder at \(w=r\xi\) has modulus at most \(|a|r^k/2\), and \(|a|r^k<1\). The displayed modulus is then at most \(1-|a|r^k/2<1\), a contradiction. Division by a linear factor and induction split any complex polynomial into linear factors.

The characteristic polynomial annihilates \(A\): expand the cofactor identity
\(\operatorname{adj}(tI-A)(tI-A)=\det(tI-A)I\)
in powers of \(t\), then replace a matrix coefficient times \(t^j\) by that coefficient times \(A^j\). The left side cancels term by term, giving the claim. The cofactor identity itself follows by expanding a determinant along a row, with a repeated row giving zero.

Polynomial division is obtained by successively cancelling leading terms. Its Euclidean algorithm gives a Bézout identity for coprime polynomials. Applied to the distinct factors \((t-\lambda)^{m_\lambda}\) of the characteristic polynomial, these identities give polynomials \(e_\lambda\) which are one modulo the factor indexed by \(\lambda\) and zero modulo every other factor. Their sum is one modulo the characteristic polynomial. It follows that
\[
V=\bigoplus_\lambda V_\lambda,\qquad
V_\lambda=\ker(A-\lambda I)^{m_\lambda},
\tag{H.2}
\]
with projections \(e_\lambda(A)\): on each kernel the stated congruences give the identity or zero, and their sum gives every vector. Equivalently, applying the product factors to the Bézout identities directly shows that their images lie in these kernels, establishing existence of the decomposition as well as directness.

Set \(S|_{V_\lambda}=\lambda I\) and \(N=A-S\). A polynomial congruent to \(\lambda\) modulo each \((t-\lambda)^{m_\lambda}\), constructed by the same \(e_\lambda\)'s, gives \(S=p(A)\). Thus \(N\) is polynomial too; it is nilpotent on each summand, and commutes with \(S\).

A commuting pair of diagonalizable operators is simultaneously diagonalizable: the eigenspaces of the first are stable under the second, and polynomial spectral projections of the second decompose each such subspace into its intersections with the second eigenspaces. Hence a sum or difference of commuting diagonalizable operators is diagonalizable. A sum of commuting nilpotents with powers \(r,s\) equal to zero has power \(r+s-1\) equal to zero, by the binomial expansion. If \(A=S'+N'\) were a second decomposition, both \(S',N'\) commute with \(A\), hence with its polynomial parts \(S,N\). Consequently \(S-S'=N'-N\) is both diagonalizable and nilpotent, so zero. This proves uniqueness.

The operators \(\operatorname{ad}S\) and \(\operatorname{ad}N\) commute. In an eigenbasis of \(S\), the matrix unit \(E_{ij}\) is an eigenvector for \(\operatorname{ad}S\), of eigenvalue \(\lambda_i-\lambda_j\). If \(N^r=0\), then
\[
(\operatorname{ad}N)^m(B)=
\sum_{j=0}^m(-1)^j\binom mj N^{m-j}BN^j
\]
is zero for \(m\geq2r-1\). This proves that the Jordan parts of \(\operatorname{ad}A\) are \(\operatorname{ad}S,\operatorname{ad}N\). Its polynomial construction yields the first formula in (H.1), with zero constant term since zero is an eigenvalue of \(\operatorname{ad}A\) when \(V\ne0\). On its finitely many distinct eigenvalues choose by the same interpolation a polynomial \(f\) with
\(f(\lambda_i-\lambda_j)=\overline{\lambda_i-\lambda_j}\) and \(f(0)=0\).
Then \(\operatorname{ad}\overline S_{\mathrm{eig}}=f(\operatorname{ad}S)=f(P(\operatorname{ad}A))\), proving the second formula. The zero-dimensional case is immediate.

For real \(A\), conjugation of the complexified decomposition gives another decomposition of \(A\), so uniqueness makes both parts real. Finally suppose \(A\) is a derivation. For generalized eigenvectors \(u\in V_\lambda,v\in V_\mu\), the derivation rule gives
\[
(A-(\lambda+\mu)I)^m[u,v]
=\sum_{j=0}^m\binom mj[(A-\lambda I)^ju,(A-\mu I)^{m-j}v].
\]
This is zero for large \(m\). Thus \([V_\lambda,V_\mu]\subseteq V_{\lambda+\mu}\), interpreted as zero when the latter is absent. The operator \(S\), acting by the indicated scalar on each summand, therefore satisfies the derivation rule; \(N=A-S\) does too. Complexifying proves the same conclusion over \(\mathbb R\). □

**Lemma H.2 (The radical and elementary extensions).** Every Lie algebra has a largest solvable ideal \(\mathfrak r\), its **radical**. It is preserved by every automorphism, and \(\mathfrak g/\mathfrak r\) is semisimple. If a solvable ideal \(I\) has semisimple quotient, then \(I=\mathfrak r\). Solvability and nilpotence are preserved by subalgebras and quotients and are detected by complexification of a real algebra.

**Proof.** Jacobi says that the operation \(z\mapsto[x,z]\) is a derivation. Hence sums, intersections and brackets of ideals are ideals. Kernels of homomorphisms are ideals, and their images carry the bracket induced from the quotient by that kernel, since changing a representative changes a bracket by an element of the kernel. These observations also make every term of the two series above an ideal.

For a subalgebra, each term of either series is contained in the corresponding ambient term. A surjective homomorphism takes each term onto the corresponding quotient term, by induction on its defining brackets. This proves preservation. Complexification commutes with each bracket span, so every complexified term is exactly the complexification of the real term. This proves detection. Also \(D^j\mathfrak g\subseteq C^{j+1}\mathfrak g\), by induction, so nilpotence implies solvability.

If \(I\) and \(\mathfrak g/I\) are solvable, some \(D^a\mathfrak g\) is contained in \(I\), and then \(D^{a+b}\mathfrak g\subseteq D^b I=0\) for large \(b\). Thus an extension of solvable algebras is solvable. If \(I,J\) are solvable ideals, \((I+J)/I\) is a quotient of \(J\), so \(I+J\) is solvable by this extension argument. The sum of all solvable ideals is a finite such sum: take a finite basis of their sum and, for each basis vector, the finitely many ideals used to express it. Their sum is therefore solvable and contains all of them. This proves existence and uniqueness of \(\mathfrak r\).

An automorphism takes solvable ideals to solvable ideals and its inverse reverses this inclusion, so preserves \(\mathfrak r\). The preimage of a solvable ideal in \(\mathfrak g/\mathfrak r\) would be an extension of solvable algebras and hence a solvable ideal in \(\mathfrak g\). Maximality makes that preimage just \(\mathfrak r\). The quotient is therefore semisimple. Finally, if \(I\) is as stated, \(I\subseteq\mathfrak r\), and the image of \(\mathfrak r\) in the semisimple quotient is a solvable ideal, hence zero. This gives the reverse inclusion. □

**Theorem H.3 (Lie's theorem).** Every complex representation of a solvable real or complex Lie algebra has a basis in which all operators are upper triangular. In particular, every nonzero irreducible complex representation of such an algebra is one dimensional. A Lie algebra is solvable if and only if its derived algebra is nilpotent.

**Proof.** Complexifying the algebra when necessary reduces the first assertion to a complex algebra, by H.2. We first prove existence of a common eigenvector by induction on \(\dim\mathfrak g\). It is immediate for the zero algebra. If \(\mathfrak g\ne0\) is solvable, \([\mathfrak g,\mathfrak g]\ne\mathfrak g\). Choose a hyperplane \(\mathfrak h\) containing the derived algebra. It is an ideal, since all brackets lie in that derived algebra, and is solvable by H.2. Write \(\mathfrak g=\mathfrak h\oplus\mathbb Cx\). Induction gives a nonzero \(v\) with \(hv=\lambda(h)v\) for all \(h\in\mathfrak h\), where \(\lambda\) is linear.

Let \(W\) be the span of \(v,xv,x^2v,\ldots\). The identity
\[
hx^jv=x(hx^{j-1}v)+[h,x]x^{j-1}v
\tag{H.3}
\]
shows inductively, for all \(h\) at once, that
\(hx^jv-\lambda(h)x^jv\) belongs to the span of the earlier powers. The first powers up to the first dependence form a basis of \(W\); the relation propagates under \(x\), so \(W\) is \(x\)-stable and hence \(\mathfrak g\)-stable. In this basis every \(h\) has diagonal entries \(\lambda(h)\). Since a commutator has trace zero,
\[
0=\operatorname{tr}_W[x,h]=(\dim W)\lambda([x,h]).
\]
The characteristic is zero, so \(\lambda([x,h])=0\). Apply (H.3) again, inducting on \(j\) for every \(h\); its second term now has coefficient \(\lambda([h,x])=0\). It follows that \(h\) acts on all of \(W\) by the scalar \(\lambda(h)\). By H.1 the operator \(x|_W\) has an eigenvector, which is therefore a common eigenvector for \(\mathfrak g\).

Its line is invariant. Apply the common-eigenvector result to the quotient by that line and continue by induction on dimension. Lifting a basis at each step gives an invariant full flag and the asserted upper-triangular matrices. Irreducibility then forces dimension one.

For upper-triangular matrices the diagonal of a commutator is zero. Strictly upper-triangular matrices lower the full coordinate flag by at least one step, so every product of \(\dim V\) such matrices is zero. Apply this to the adjoint representation of a solvable complex algebra. Every element of \([\mathfrak g,\mathfrak g]\) acts by a strictly upper-triangular matrix. A sufficiently long nested bracket of its elements with any last vector is consequently zero, proving nilpotence of the derived algebra. Complexification gives the real case. Conversely, if the derived algebra is nilpotent it is solvable by H.2; the quotient by it is abelian, so the extension argument in H.2 proves solvability of \(\mathfrak g\). □

**Theorem H.4 (Engel's theorem).** If a Lie subalgebra \(\mathfrak a\subseteq\operatorname{End}(V)\) consists of nilpotent operators and \(V\ne0\), there is a nonzero vector killed by every member of \(\mathfrak a\). There is consequently a basis making every member strictly upper triangular. A Lie algebra is nilpotent exactly when each \(\operatorname{ad}x\) is nilpotent.

**Proof.** We prove the common-kernel assertion by induction on \(\dim\mathfrak a\), for all representations of nilpotent-operator subalgebras simultaneously. The zero algebra is immediate. Choose a proper subalgebra \(\mathfrak b\) of maximal dimension. For \(b\in\mathfrak b\), the binomial formula in H.1 shows that \(\operatorname{ad}b\) is nilpotent on \(\operatorname{End}(V)\), hence on \(\mathfrak a\) and the \(\mathfrak b\)-module \(\mathfrak a/\mathfrak b\). The image of \(\mathfrak b\) on this quotient has dimension at most \(\dim\mathfrak b<\dim\mathfrak a\), so induction gives a nonzero class \(x+\mathfrak b\) killed by it. Thus \([\mathfrak b,x]\subseteq\mathfrak b\). The strictly larger subspace \(\mathfrak b+\mathbb Kx\) is a subalgebra, so maximality makes it all of \(\mathfrak a\). In particular \(\mathfrak b\) is a codimension-one ideal.

Induction applied to \(\mathfrak b\subseteq\operatorname{End}(V)\) gives \(W=V^{\mathfrak b}\ne0\). It is \(\mathfrak a\)-stable: for \(w\in W\) and \(b\in\mathfrak b\),
\(b(xw)=x(bw)+[b,x]w=0\).
Since \(x|_W\) is nilpotent, its kernel in this nonzero space is nonzero. A vector in that kernel is killed by \(x\) and by \(\mathfrak b\), proving the assertion.

Repeat it on the quotient by this vector's line; all quotient operators are still nilpotent. Induction on \(\dim V\) produces the strict triangular flag. If \(\mathfrak g\) is nilpotent, sufficiently long repeated brackets show directly that each \(\operatorname{ad}x\) is nilpotent. Conversely the strict flag applied to \(\operatorname{ad}\mathfrak g\) says that every product of \(\dim\mathfrak g\) adjoint operators is zero. Such products span the corresponding lower-central-series term, which is therefore zero. This proves the equivalence over both fields. □

**Theorem H.5 (Trace and Killing criteria).** A complex matrix Lie algebra \(\mathfrak a\subseteq\operatorname{End}(V)\) is solvable if
\[
\operatorname{tr}(XY)=0\quad\text{for }X\in[\mathfrak a,\mathfrak a],\ Y\in\mathfrak a.
\tag{H.4}
\]
For a real or complex Lie algebra, its Killing form
\[
K_{\mathfrak g}(x,y)=\operatorname{tr}_{\mathfrak g}(\operatorname{ad}x\,\operatorname{ad}y)
\]
vanishes on \([\mathfrak g,\mathfrak g]\times\mathfrak g\) exactly when \(\mathfrak g\) is solvable. It is nondegenerate exactly when \(\mathfrak g\) is semisimple.

**Proof.** Let \(X\in[\mathfrak a,\mathfrak a]\), with Jordan parts \(S,N\), and let \(S^\dagger=\overline S_{\mathrm{eig}}\) be the eigenvalue-conjugate operator from H.1. A nilpotent operator lowers the filtration by kernels of its successive powers; a basis adapted to that filtration makes its matrix strictly triangular, so its trace is zero. Apply this to \(N\) on each generalized eigenspace. Thus
\[
\operatorname{tr}(XS^\dagger)=\sum_j|\lambda_j|^2,
\tag{H.5}
\]
where eigenvalues are counted with multiplicity. Write \(X=\sum_i[U_i,V_i]\). Cyclicity of trace, proved by the entry sum \(\operatorname{tr}(AB)=\sum_{i,j}a_{ij}b_{ji}=\operatorname{tr}(BA)\), gives
\[
\operatorname{tr}(XS^\dagger)
=-\sum_i\operatorname{tr}\bigl(U_i[S^\dagger,V_i]\bigr).
\]
By (H.1), \([S^\dagger,V_i]=Q(\operatorname{ad}X)V_i\), with zero constant term. Since \(X\in[\mathfrak a,\mathfrak a]\), every positive power of \(\operatorname{ad}X\) maps \(\mathfrak a\) into its derived ideal. Each trace on the right is therefore zero by (H.4). Equation (H.5) forces every \(\lambda_j=0\); hence \(X\) is nilpotent. Engel's theorem H.4 makes the derived algebra nilpotent, and H.2 makes \(\mathfrak a\) solvable.

If \(\mathfrak g\) is solvable over \(\mathbb C\), H.3 triangularizes its adjoint representation. The derived algebra acts by strictly upper-triangular matrices, whose product with an upper-triangular matrix has trace zero. This proves the vanishing Killing condition. Conversely that condition is (H.4) for \(\operatorname{ad}\mathfrak g\), so this image is solvable. Its kernel is the abelian centre, and H.2 proves that \(\mathfrak g\) is solvable. Complexification, which extends the same matrix traces and derived series, proves the real equivalence.

Trace cyclicity also gives invariance:
\[
K([x,y],z)+K(y,[x,z])=0 .
\tag{H.6}
\]
Thus \(\ker K\) is an ideal. For any ideal \(I\) and \(x,y\in I\), their adjoint actions on \(\mathfrak g/I\) vanish. A basis adapted to \(I\) makes their product block triangular, with zero quotient block, and gives
\[
K_I(x,y)=K_{\mathfrak g}(x,y).
\tag{H.7}
\]
If \(\mathfrak g\) is semisimple, apply this to \(I=\ker K\). Its own Killing form is zero, so the already proved solvability criterion makes it solvable. It must be zero.

For the converse suppose \(K\) is nondegenerate and there is a nonzero solvable ideal \(I\). Its last nonzero derived term \(A\) is an abelian ideal of \(\mathfrak g\): the derivation identity keeps all terms invariant under \(\operatorname{ad}\mathfrak g\). For \(a\in A,y\in\mathfrak g\), the operator \(\operatorname{ad}a\,\operatorname{ad}y\) takes \(\mathfrak g\) into \(A\) and is zero on \(A\), because \(A\) is abelian and \([y,A]\subseteq A\). Its trace in an adapted basis is zero. Thus \(K(a,y)=0\) for every \(y\), contrary to nondegeneracy and \(A\ne0\). No nonzero solvable ideal exists. □

**Theorem H.6 (Simple summands and inner derivations).** A semisimple real or complex Lie algebra is a direct sum of simple ideals. Every ideal is a sum of these summands; ideals and quotients are semisimple, and
\[
[\mathfrak g,\mathfrak g]=\mathfrak g,\qquad Z(\mathfrak g)=0.
\]
Every derivation of \(\mathfrak g\) is \(\operatorname{ad}a\) for a unique \(a\in\mathfrak g\). Each \(x\in\mathfrak g\) has unique commuting parts \(x=x_s+x_n\) whose adjoint operators are the Jordan parts of \(\operatorname{ad}x\). A real algebra is semisimple exactly when its complexification is semisimple.

**Proof.** The centre is an abelian ideal, hence zero. The last assertion follows from H.5: the complex Killing matrix is the same real Killing matrix extended to complex scalars, so its determinant is nonzero over one field exactly when it is nonzero over the other.

For an ideal \(I\), its orthogonal complement \(I^\perp\) for the nondegenerate Killing form is an ideal by (H.6). The intersection \(J=I\cap I^\perp\) is an ideal whose Killing form is zero by (H.7), since \(K(J,J)=0\). H.5 makes \(J\) solvable, and semisimplicity gives \(J=0\). Nondegeneracy gives \(\dim I+\dim I^\perp=\dim\mathfrak g\), so
\(\mathfrak g=I\oplus I^\perp\).
The two ideals commute because their bracket lies in their intersection.

Choose a nonzero ideal \(I\) of minimal dimension. Every ideal inside it is an ideal in \(\mathfrak g\), since its complementary ideal commutes with it. Hence it has no nonzero proper ideal, and it is not abelian by semisimplicity. It is simple. The complementary ideal is semisimple: each of its solvable ideals is again an ideal of the full direct sum. Induction proves the decomposition into simple ideals.

A simple nonabelian algebra equals its derived algebra, since the latter is a nonzero ideal. Thus every semisimple algebra is perfect. Conversely a direct sum of simple algebras has no nonzero solvable ideal: the projection of such an ideal to each simple factor is a solvable ideal in that factor, hence zero. If \(J\) is any ideal of \(\bigoplus_i\mathfrak g_i\), its projection to a factor is either zero or all of that factor. In the second case
\[
[\mathfrak g_i,J]=[\mathfrak g_i,\operatorname{pr}_iJ]=\mathfrak g_i
\]
as subspaces of the direct sum, so \(\mathfrak g_i\subseteq J\). This proves that \(J\) is exactly a sum of factors, and proves the ideal and quotient assertions.

It remains to prove the derivation assertion independently of cohomology. Let \(\mathfrak d=\operatorname{Der}(\mathfrak g)\subseteq\operatorname{End}(\mathfrak g)\). It is closed under commutators by expanding the derivation rule. For \(D\in\mathfrak d\),
\[
[D,\operatorname{ad}x]=\operatorname{ad}(Dx),
\tag{H.8}
\]
so \(\operatorname{ad}\mathfrak g\) is an ideal in \(\mathfrak d\). The trace form \(\operatorname{tr}_{\mathfrak g}(DE)\) is invariant under commutators and restricts to the nondegenerate Killing form on that ideal. Consequently its orthogonal complement \(\mathfrak j\) inside \(\mathfrak d\) is an ideal, and linear algebra gives
\(\mathfrak d=\operatorname{ad}\mathfrak g\oplus\mathfrak j\).
Their bracket is zero. For \(D\in\mathfrak j\), (H.8) now gives \(\operatorname{ad}(Dx)=0\) for every \(x\). The centre is zero, so \(Dx=0\) for all \(x\), and \(D=0\). Therefore \(\mathfrak d=\operatorname{ad}\mathfrak g\), with uniqueness again from the zero centre.

By H.1, the Jordan parts of the derivation \(\operatorname{ad}x\) are derivations. The just-proved assertion therefore writes them uniquely as \(\operatorname{ad}x_s,\operatorname{ad}x_n\). Their sum and commutator give respectively \(\operatorname{ad}(x-x_s-x_n)=0\) and \(\operatorname{ad}[x_s,x_n]=0\). The zero centre proves both asserted element identities. H.1 also makes these parts real when \(x\) and the algebra are real. □

**Theorem H.7 (Semisimple symmetric blocks).** An involution \(\theta\) of a semisimple real or complex Lie algebra splits it into a direct sum of \(\theta\)-stable ideals, each either a simple ideal preserved by \(\theta\), or a pair of isomorphic simple ideals interchanged by \(\theta\). On an interchanged pair the positive eigenspace is a graph, which becomes the diagonal after identifying the factors.

**Proof.** H.6 identifies the simple summands intrinsically as the minimal nonzero ideals. An automorphism must permute them. An involution has permutation orbits of size one or two, whose sums give the stated stable blocks. On a pair \(\mathfrak a\oplus\mathfrak b\), write \(\varphi=\theta|_{\mathfrak a}:\mathfrak a\to\mathfrak b\). Its inverse is \(\theta|_{\mathfrak b}\), and
\[
\theta(x,y)=(\varphi^{-1}y,\varphi x).
\]
Thus the positive and negative eigenspaces are respectively
\(\{(x,\varphi x)\}\) and \(\{(x,-\varphi x)\}\).
The isomorphism \((x,y)\mapsto(x,\varphi^{-1}y)\) turns \(\theta\) into the factor swap and its positive space into the diagonal. This treats real simple factors as real; it does not assume that a real simple algebra has simple complexification. □

## I. Cocycles and an involution-preserving Levi factor

Write \(\rho(x)v=xv\) for a module action, so
\([\rho(x),\rho(y)]=\rho([x,y])\).
For a vector \(v\), a linear map \(f:\mathfrak g\to V\), and an alternating bilinear map \(\omega:\mathfrak g^2\to V\), define
\[
\begin{aligned}
(\delta v)(x)&=xv,\\
(\delta f)(x,y)&=xf(y)-yf(x)-f([x,y]),\\
(\delta\omega)(x,y,z)&=x\omega(y,z)-y\omega(x,z)+z\omega(x,y)\\
&\quad-\omega([x,y],z)+\omega([x,z],y)-\omega([y,z],x).
\end{aligned}
\tag{I.1}
\]
A map with zero \(\delta\) is a **cocycle**; a map of the form \(\delta\) of a lower-degree map is a **coboundary**. The proof below checks all differential identities needed here, without assuming a theory of derived functors.

**Lemma I.1 (The Casimir calculation in degrees one and two).** Let \(\mathfrak g\) be a complex semisimple algebra and \(V\) a nontrivial irreducible module. There is an invertible operator \(C\) commuting with \(\rho(\mathfrak g)\), and a finite sum of pairs \(u_i,v_i\in\mathfrak g\), such that
\[
C=\sum_i\rho(u_i)\rho(v_i).
\]
Every one-cocycle \(f\) and two-cocycle \(\omega\) then have the explicit primitives
\[
f=\delta\left(C^{-1}\sum_i u_i f(v_i)\right),\qquad
\omega=\delta\eta,\quad
\eta(x)=C^{-1}\sum_i u_i\omega(v_i,x).
\tag{I.2}
\]

**Proof.** The trace form \(\beta(x,y)=\operatorname{tr}_V(\rho(x)\rho(y))\) is symmetric and invariant, by cyclicity of trace. Its kernel \(I\) is an ideal. It is not all of \(\mathfrak g\): otherwise H.5 would make \(\rho(\mathfrak g)\) solvable, whereas H.6 makes that quotient semisimple; it would be zero, contrary to nontriviality. By H.6 choose a complementary ideal \(J\), so \(\mathfrak g=I\oplus J\). The restriction of \(\beta\) to \(J\) is nondegenerate: a vector in its kernel pairs to zero with \(J\), and also with \(I\), hence lies in \(I\cap J=0\).

Choose a basis \(u_i\) of \(J\) and its \(\beta\)-dual basis \(v_i\). The tensor
\[
\Omega=\sum_i u_i\otimes v_i
\]
is independent of the basis: under the identification \(J\otimes J\to\operatorname{End}(J)\) sending \(u\otimes v\) to \(w\mapsto\beta(v,w)u\), it is the identity. The same identification is equivariant under \(\mathfrak g\), because \(\beta\) is invariant and \(I\) commutes with \(J\). Thus
\[
\sum_i[x,u_i]\otimes v_i+\sum_i u_i\otimes[x,v_i]=0
\quad(x\in\mathfrak g).
\tag{I.3}
\]
Applying multiplication of representation operators to (I.3) proves \([\rho(x),C]=0\). Moreover
\[
\operatorname{tr}_V C=\sum_i\beta(u_i,v_i)=\dim J\ne0.
\]
Thus \(C\ne0\). Its kernel is an invariant subspace, so irreducibility makes that kernel zero. Finite dimensionality makes \(C\) invertible. This argument requires neither a choice of compact real form nor an assumed complete-reducibility theorem.

Put \(b=\sum_i u_i f(v_i)\). The one-cocycle identity gives
\[
\begin{aligned}
\rho(x)b
&=\sum_i\rho([x,u_i])f(v_i)+\sum_i\rho(u_i)\rho(x)f(v_i)\\
&=\sum_i\rho([x,u_i])f(v_i)+\sum_i\rho(u_i)f([x,v_i])
   +\sum_i\rho(u_i)\rho(v_i)f(x)\\
&=Cf(x).
\end{aligned}
\]
The first two sums cancel by (I.3). Since \(C^{-1}\) commutes with \(\rho(x)\), this proves the first formula in (I.2).

For the second, set \(a(x)=\sum_i\rho(u_i)\omega(v_i,x)\). Expanding (I.1) gives
\[
\begin{aligned}
&(\delta a)(x,y)+\sum_i\rho(u_i)(\delta\omega)(v_i,x,y)\\
&\quad=C\omega(x,y)\\
&\qquad+\sum_i\rho([x,u_i])\omega(v_i,y)
 +\sum_i\rho(u_i)\omega([x,v_i],y)\\
&\qquad-\sum_i\rho([y,u_i])\omega(v_i,x)
 -\sum_i\rho(u_i)\omega([y,v_i],x).
\end{aligned}
\tag{I.4}
\]
To check this expansion, the terms containing \(\rho(x)\rho(u_i)\) and \(\rho(u_i)\rho(x)\) combine into their commutator; likewise for \(y\). The two terms involving \(\omega(v_i,[x,y])\) cancel by alternation. The remaining two bracket-input terms are exactly those displayed. Equation (I.3), first paired with \(\omega(\,\cdot,y)\) and then with \(\omega(\,\cdot,x)\), cancels both pairs of sums. For a cocycle the left side is just \(\delta a\). Therefore \(\delta a=C\omega\), and commuting \(C^{-1}\) through (I.1) gives \(\delta(C^{-1}a)=\omega\), as required. □

**Theorem I.2 (The two Whitehead lemmas).** For every finite-dimensional module \(V\) of a real or complex semisimple algebra, every one-cocycle and every two-cocycle is a coboundary. In particular, if
\[
\begin{aligned}
0={}&x\omega(y,z)-y\omega(x,z)+z\omega(x,y)\\
&-\omega([x,y],z)+\omega([x,z],y)-\omega([y,z],x),
\end{aligned}
\]
there is a linear \(\eta:\mathfrak g\to V\) with
\[
\omega(x,y)=x\eta(y)-y\eta(x)-\eta([x,y]).
\tag{I.5}
\]

**Proof.** First check that coboundaries are cocycles in the degrees used. For \(v\in V\),
\[
(\delta\delta v)(x,y)
=\bigl([\rho(x),\rho(y)]-\rho([x,y])\bigr)v=0.
\]
For a linear \(f\), expansion of (I.1) gives
\[
\begin{aligned}
(\delta\delta f)(x,y,z)
={}&\sum_{\mathrm{cyc}}
\bigl([\rho(x),\rho(y)]-\rho([x,y])\bigr)f(z)\\
&+f([[x,y],z]+[[y,z],x]+[[z,x],y])=0.
\end{aligned}
\tag{I.6}
\]
The mixed terms \(\rho(x)f([y,z])\) cancel in this expansion; the displayed terms vanish by the representation identity and Jacobi. These computations also show directly that homomorphisms of modules commute with \(\delta\).

Work first over \(\mathbb C\). For a nontrivial irreducible module, I.1 gives both assertions. For the one-dimensional trivial module, a one-cocycle kills all brackets, so is zero because \(\mathfrak g\) is perfect by H.6. For a two-cocycle with trivial coefficients use the nondegenerate Killing form to define \(D\) by
\[
\omega(x,y)=K(Dx,y).
\]
Alternation says that \(D\) is skew for \(K\). The cocycle equation reads
\[
\omega([x,y],z)=\omega(x,[y,z])-\omega(y,[x,z]).
\]
Invariance of \(K\) turns this into
\[
K(D[x,y],z)=K([Dx,y]+[x,Dy],z).
\]
Nondegeneracy makes \(D\) a derivation. H.6 supplies \(D=\operatorname{ad}a\), so
\(\omega(x,y)=K(a,[x,y])\).
For \(\eta(x)=-K(a,x)\), the trivial-action formula in (I.1) gives \(\delta\eta=\omega\). This proves both assertions for all irreducible modules, including the trivial one.

Now induct on \(\dim V\). A nonzero finite-dimensional module has an irreducible submodule \(W\): choose a nonzero invariant subspace of least dimension. If \(W=V\) the result is already proved. Otherwise let \(\pi:V\to V/W\) be the quotient. For a one-cocycle \(f\), induction gives \(\pi f(x)=x\bar v\). Lift \(\bar v\) to \(v\in V\). The difference \(f-\delta v\) takes values in \(W\) and is a cocycle by (I.6); induction in \(W\) writes it as \(\delta w\). Hence \(f=\delta(v+w)\).

For a two-cocycle \(\omega\), induction gives \(\pi\omega=\delta\bar\eta\). Lift \(\bar\eta\) to a linear map \(\eta:\mathfrak g\to V\), by choosing lifts of its values on a basis. Then \(\omega-\delta\eta\) takes values in \(W\); it is still a cocycle by (I.6). Induction in \(W\) gives \(\omega-\delta\eta=\delta\xi\), so \(\omega=\delta(\eta+\xi)\). This proves the assertion for all complex modules without assuming that the original extension \(V\) splits.

For a real semisimple algebra, H.6 makes its complexification semisimple. Complexify the real module and cocycle, apply the complex result, and restrict the primitive to real arguments. Taking its real part gives a real primitive, since all matrices and the differential (I.1) are real on those arguments. The zero module or zero algebra is covered by the same empty formulas. □

**Corollary I.3 (Complete reducibility with an explicit correction).** Every invariant subspace of a finite-dimensional module of a real or complex semisimple Lie algebra has an invariant complement.

**Proof.** Let \(W\subseteq V\) be invariant, let \(U=V/W\), and choose a linear section \(j:U\to V\). The defect
\[
f(x)=\rho_V(x)j-j\rho_U(x)
\]
takes values in \(\operatorname{Hom}(U,W)\), since its composition with the quotient map is zero. On this Hom space the action is
\[
x\cdot A=\rho_W(x)A-A\rho_U(x).
\]
Expanding two such operations shows their commutator equals the operation for \([x,y]\), so this is a module. Expanding \(f([x,y])\), using the representation identities in \(U,V\), gives
\(f([x,y])=x\cdot f(y)-y\cdot f(x)\).
It is a one-cocycle. By I.2 it has the form \(f(x)=x\cdot A\) for one \(A:U\to W\). Replace \(j\) by \(j-A\); its defect is zero, so it is equivariant. It is still a section because \(A\) takes values in the quotient kernel. Its image is the desired invariant complement. Repeating in the two smaller summands gives a direct sum of irreducible submodules if desired. □

**Theorem I.4 (Levi decomposition respecting an involution).** Let \(\theta\) be an involutive automorphism of a real or complex Lie algebra with radical \(\mathfrak r\). There is a \(\theta\)-stable semisimple subalgebra \(\mathfrak s\) such that
\[
\mathfrak g=\mathfrak r\rtimes\mathfrak s
\tag{I.7}
\]
as a vector-space direct sum with \(\mathfrak r\) an ideal. The positive and negative eigenspaces split into those of the two summands. Taking \(\theta=I\) gives an ordinary Levi decomposition. If \(\mathfrak r=Z(\mathfrak g)\), this is a direct sum of commuting ideals.

**Proof.** Induct on \(\dim\mathfrak r\). If the radical is zero, choose \(\mathfrak s=\mathfrak g\). Otherwise let \(\mathfrak a\) be the last nonzero term of the radical's derived series. It is a nonzero abelian ideal of \(\mathfrak g\), by the derivation argument in H.2, and is \(\theta\)-stable because \(\mathfrak r\) is characteristic and brackets are preserved. The radical of \(\mathfrak g/\mathfrak a\) is \(\mathfrak r/\mathfrak a\), by H.2. Its dimension is smaller. Induction gives a stable semisimple complement \(\overline{\mathfrak s}\) there.

Let \(\mathfrak e\subseteq\mathfrak g\) be the preimage of \(\overline{\mathfrak s}\). It is stable under \(\theta\), and
\[
0\longrightarrow\mathfrak a\longrightarrow\mathfrak e
\overset{p}{\longrightarrow}\overline{\mathfrak s}\longrightarrow0
\tag{I.8}
\]
has abelian kernel. Choose a linear section \(j_0\) of \(p\). If \(\bar\theta\) is the induced involution on \(\overline{\mathfrak s}\), then
\[
j(x)=\tfrac12\bigl(j_0(x)+\theta j_0(\bar\theta x)\bigr)
\]
is again a section and is equivariant. Define \(xv=[j(x),v]\) on \(\mathfrak a\). This action is independent of the section because \(\mathfrak a\) is abelian. Jacobi and the fact that \([j(x),j(y)]-j([x,y])\in\mathfrak a\) show that it is a representation. It is compatible with both involutions.

Set
\[
\omega(x,y)=[j(x),j(y)]-j([x,y])\in\mathfrak a.
\]
The Jacobi identity of \(\mathfrak e\), expanded for \(j(x),j(y),j(z)\), says
\[
0=\sum_{\mathrm{cyc}}\bigl(x\omega(y,z)+\omega(x,[y,z])\bigr)
=(\delta\omega)(x,y,z).
\]
Thus I.2 gives \(\omega=\delta\eta\). The equivariance of \(j\) makes \(\omega\) invariant under the cochain operation
\[
(\Theta\eta)(x)=\theta\eta(\bar\theta x),\qquad
(\Theta\omega)(x,y)=\theta\omega(\bar\theta x,\bar\theta y).
\]
Compatibility of the action with the involutions shows, by substituting in (I.1), that \(\delta\Theta=\Theta\delta\). Replace \(\eta\) by \((\eta+\Theta\eta)/2\). It is now equivariant and still has \(\delta\eta=\omega\).

The corrected section \(j'=j-\eta\) has zero bracket defect: expansion gives
\[
[j'(x),j'(y)]-j'([x,y])
=\omega(x,y)-x\eta(y)+y\eta(x)+\eta([x,y])=0,
\]
since the bracket of the two \(\eta\)-values in \(\mathfrak a\) is zero. Thus \(j'\) is an equivariant Lie-algebra embedding. Its image \(\mathfrak s\) is semisimple and stable. Since \(\overline{\mathfrak s}\) complements \(\mathfrak r/\mathfrak a\), every element of \(\mathfrak g\) is a sum from \(\mathfrak r+\mathfrak s\). If \(j'(x)\in\mathfrak r\), projection to \(\mathfrak g/\mathfrak a\) puts \(x\) in \(\overline{\mathfrak s}\cap(\mathfrak r/\mathfrak a)=0\), so \(j'(x)=0\). This proves the direct sum (I.7).

Both summands are stable under \(\theta\), so uniqueness of the vector-space decomposition makes the two projections commute with \(\theta\). Applying \((I\pm\theta)/2\) proves the eigenspace assertion. Finally a central radical commutes with \(\mathfrak s\); in that case \([\mathfrak g,\mathfrak s]\subseteq\mathfrak s\), so both summands are ideals and their cross brackets vanish. □

## J. The global radical fibre and section

The groups in this part are real Lie groups; their Lie algebras are real. Completeness and total geodesy refer to the canonical connections of Part B.

**Theorem J.1 (The radical subgroup is closed).** In a connected Lie group \(G\), the connected subgroup \(R\) with Lie algebra \(\mathfrak r=\operatorname{rad}(\mathfrak g)\) is closed and normal. The quotient \(Q=G/R\) is a connected Lie group with semisimple Lie algebra \(\mathfrak g/\mathfrak r\). Every automorphism of \(G\) preserves \(R\).

**Proof.** [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1) constructs the unique connected analytic subgroup for \(\mathfrak r\). Every Lie-algebra automorphism preserves \(\mathfrak r\), by H.2; exponential naturality and the generation of the connected subgroup by exponentials then show that conjugations and group automorphisms preserve \(R\). This proves normality and the last assertion before any closedness is assumed.

The adjoint action of \(G\) preserves \(\mathfrak r\), so induces a smooth homomorphism
\[
\Phi:G\longrightarrow GL(\mathfrak g/\mathfrak r).
\]
Its differential sends \(x\) to the map \(y+\mathfrak r\mapsto[x,y]+\mathfrak r\). Since the quotient algebra is semisimple by H.2 and has zero centre by H.6,
\[
\ker(d\Phi_e)=\mathfrak r.
\]
The kernel \(K=\Phi^{-1}(I)\) is a closed embedded Lie subgroup by [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). Its Lie algebra is the displayed differential kernel: one inclusion follows by differentiation, and the other because
\(\Phi(\exp tx)=\exp(t\,d\Phi_e x)=I\)
for every kernel vector. Its identity component \(K^0\) therefore has Lie algebra \(\mathfrak r\), so uniqueness in [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1) makes \(K^0=R\) as a subgroup. Connected components are closed: the closure of a connected set is connected, as a separation of the closure would also separate the dense set. Thus \(R\) is closed in \(K\) and in \(G\).

[Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) gives the smooth quotient and local sections. Normality makes multiplication and inversion descend; local sections show that the descended maps are smooth. The quotient projection has differential kernel \(\mathfrak r\), so its Lie algebra is \(\mathfrak g/\mathfrak r\), with the quotient bracket from H.2. It is connected as a continuous image of \(G\), and its Lie algebra is semisimple. □

**Theorem J.2 (The radical bundle of a symmetric space).** For a symmetric presentation \((G,H,\sigma)\), let \(R\) be its radical subgroup and \(\pi:G\to Q=G/R\). Then \(K=\pi(H)\) is closed, and
\[
G/H\longrightarrow Q/K
\tag{J.1}
\]
is a smooth fibre bundle of symmetric spaces. The base is presented by a group with semisimple Lie algebra; its fibre at the origin is the complete totally geodesic symmetric space
\[
R/(R\cap H).
\tag{J.2}
\]

**Proof.** By J.1, \(\sigma\) preserves \(R\), so induces an involution \(\sigma_Q\) on \(Q\). The subgroup \(K\) is contained in \(Q^{\sigma_Q}\), because every element of \(H\) is fixed by \(\sigma\). At the Lie-algebra level the projection of the positive eigenspace \(\mathfrak h=\mathfrak g^+\) onto \((\mathfrak g/\mathfrak r)^+\) is surjective: lift a fixed quotient vector arbitrarily and replace its lift \(x\) by \((x+\theta x)/2\). The connected fixed subgroup \((Q^{\sigma_Q})^0\) is generated by exponentials of this positive eigenspace, by B.1 and [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1). Each such exponential lifts to an exponential in \(H\). Hence
\[
(Q^{\sigma_Q})^0\subseteq K\subseteq Q^{\sigma_Q}.
\tag{J.3}
\]
The fixed group is a Lie group by [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). Its identity component is open: a connected coordinate ball at the identity lies in that component, and its translates give openness at each of its points. Every connected component is a coset of it, because translating a component to the identity component preserves connectedness and maximality. A subgroup containing the identity component is therefore a union of open components, with open complementary union. Thus \(K\) is closed in the fixed group and consequently in \(Q\). This proves both closedness and the symmetric-presentation condition for the base.

The inverse image \(\pi^{-1}(K)\) equals \(RH\). Indeed if \(\pi(g)=\pi(h)\), then \(gh^{-1}\in R\), and the reverse inclusion is immediate. The fibre of (J.1) at \(eK\) is therefore exactly the orbit \(RH/H\) of \(R\), with stabilizer \(R\cap H\). This orbit is a smooth embedded fibre: the differential of the map between quotients is the surjection
\(\mathfrak g/\mathfrak h\to(\mathfrak g/\mathfrak r)/d\pi(\mathfrak h)\),
so [Local tools 1.3](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives its fibre charts. The transitive orbit theorem [Invariant connections A.2](invariant-connections-on-homogeneous-bundles.md#theorem-a-2) identifies that fibre with (J.2).

For local triviality choose a smooth local section \(s:U\to Q\) of \(Q\to Q/K\), and shrink \(U\) so that its image lifts smoothly to \(\widetilde s:U\to G\) under \(G\to Q\). Both sections exist by [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup). The map
\[
U\times R/(R\cap H)\longrightarrow (J.1)^{-1}(U),\qquad
(b,r(R\cap H))\longmapsto\widetilde s(b)rH
\tag{J.4}
\]
is well-defined and bijective. Its inverse sends \(gH\) first to \(b=\pi(g)K\), then to the origin fibre represented by \(\widetilde s(b)^{-1}gH\); use the just-proved diffeomorphism of that fibre with (J.2). All operations are smooth in quotient charts, proving that (J.4) is a bundle chart.

The group \(R\) is invariant under \(\sigma\), and \(R\cap H\) lies between the identity component and the full fixed group of its restricted involution: this follows from the positive Lie algebra \(\mathfrak r\cap\mathfrak h\) and exponential generation, as in B.1. Thus (J.2) is symmetric and complete by B.2. Its odd tangent space is \(\mathfrak r\cap\mathfrak m\). Its horizontal spaces inside \(R\), defined by this odd space, map into the canonical horizontal spaces of \(G\) defined by \(\mathfrak m\). The induced tangent connections therefore agree, by the associated-connection construction in B.2. The fibre is autoparallel and totally geodesic, by [Submanifolds G.1](submanifolds-and-hypersurfaces.md#proposition-g-1). The projection in (J.1) likewise takes canonical horizontal spaces to canonical horizontal spaces and intertwines the quotient involutions, proving the asserted compatibility of symmetric geometries. □

**Theorem J.3 (A global totally geodesic section).** If in J.2 the group \(G\) is simply connected and \(H\) is connected, every \(\theta\)-stable Levi subalgebra supplied by I.4 integrates to a closed connected subgroup \(S\subseteq G\). Projection identifies \(S\) with \(Q=G/R\), and it gives a global totally geodesic section of (J.1).

**Proof.** First \(Q\) is simply connected. Every loop in \(Q\) based at the identity lifts to a path in \(G\) starting at the identity, by covering its compact parameter interval with finitely many quotient-section neighbourhoods from [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) and adjusting each new lift by an element of \(R\) to match the previous endpoint. Its final point is in \(R\). Because \(R\) is connected and a manifold, it is path connected: coordinate balls are path connected, so path components are open and connectedness leaves only one. Join the final point back to the identity by a path in \(R\). This closes the lifted path into a loop in \(G\), which contracts since \(G\) is simply connected. Projecting the contraction contracts the original loop with an appended constant interval; rescaling that interval gives a contraction of the original loop. Thus \(Q\) is simply connected.

Projection restricts to a Lie-algebra isomorphism
\(\mathfrak s\to\mathfrak g/\mathfrak r\).
Integrate its inverse by C.1, with the now simply connected domain \(Q\), to obtain a homomorphism \(j:Q\to G\). The homomorphism \(\pi j:Q\to Q\) has identity derivative, so uniqueness in C.1 gives \(\pi j=I\). In particular \(j\) is injective, with inverse \(\pi\) on its image. Its image is closed, since
\[
j(Q)=\{g\in G:j(\pi(g))=g\},
\]
the equalizer of two continuous maps into a Hausdorff space. It is an embedded subgroup: \(dj\) is injective, and the continuous inverse \(\pi\) makes the immersion a homeomorphism onto its image; its local immersion charts are [Local tools 1.4](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion). Its connected Lie algebra is \(\mathfrak s\), so uniqueness in [Flat connections A.1](flat-connections-and-infinitesimal-holonomy.md#lemma-a-1) identifies it with the connected analytic subgroup \(S\) specified in the statement.

The two homomorphisms \(\sigma j\) and \(j\sigma_Q\) have the same derivative, because \(\mathfrak s\) is stable under the involution. C.1 gives \(\sigma j=j\sigma_Q\). Multiplication defines a diffeomorphism
\[
R\times Q\longrightarrow G,\qquad(r,q)\longmapsto rj(q),
\quad
g\longmapsto\bigl(gj(\pi(g))^{-1},\pi(g)\bigr)
\tag{J.5}
\]
as its inverse. Under it, \(\sigma\) acts componentwise as \(\sigma|_R\) and \(\sigma_Q\).

The connectedness of \(H\), together with the symmetric-presentation inclusions, implies \(H=(G^\sigma)^0\). The fixed set in (J.5) is \(R^\sigma\times Q^{\sigma_Q}\). A product's identity component is the product of its identity components: projection puts any connected subset in those components, and their product is connected. Therefore
\[
H=(R^\sigma)^0\rtimes j((Q^{\sigma_Q})^0),\qquad
K=(Q^{\sigma_Q})^0 .
\tag{J.6}
\]
It follows that
\[
Q/K\longrightarrow G/H,\qquad qK\longmapsto j(q)H
\tag{J.7}
\]
is well-defined and smooth, and is a section of (J.1). Its differential identifies the base's odd tangent space with \(\mathfrak s\cap\mathfrak m\). The horizontal spaces for these symmetric presentations map into one another under \(j\), exactly as in J.2. Hence (J.7) preserves their canonical connections along tangent vectors and is totally geodesic. This proves the global section for each chosen stable Levi subalgebra, without assuming that an arbitrary immersed Levi subgroup in an arbitrary connected group is closed. □

## K. Solvable and indefinite algebraic examples

**Example K.1 (The tangent group and its radical).** Right trivialization identifies the tangent group of a Lie group \(G\) with the semidirect product \(\widehat G\) of F.1. For a symmetric presentation its tangent presentation is
\[
(TG,TH,T\sigma),\qquad TG/TH\cong T(G/H).
\]
If \(\mathfrak g\) is semisimple, the radical of its tangent Lie algebra is the second, abelian copy of \(\mathfrak g\), and its first copy is an involution-stable Levi factor.

**Proof.** Identify \(u\in T_gG\) with \((dR_{g^{-1}})_g u\in\mathfrak g\). This is a smooth global trivialization, with inverse \(a\mapsto(dR_g)_e a\). The derivative of multiplication at \((g,h)\), evaluated on tangent vectors of right coefficients \(a,b\), has right coefficient \(a+\operatorname{Ad}(g)b\): the derivative varying the first factor is \(dR_h dR_g a=dR_{gh}a\), and varying the second is \(dL_g dR_h b=dR_{gh}\operatorname{Ad}(g)b\). Thus tangent multiplication is exactly (F.2); tangent inversion and identity consequently have the group formulas proved there. Naturality of right translation under \(\sigma\) gives the involution \((g,a)\mapsto(\sigma(g),\theta a)\). The subgroup \(TH\) corresponds to \(H\ltimes\mathfrak h\). F.1 supplies the full quotient diffeomorphism and its symmetric structure.

The Lie algebra bracket is (F.3). Its second summand \(0\oplus\mathfrak g\) is an abelian ideal, and the quotient by it is the first copy of \(\mathfrak g\), semisimple by hypothesis. H.2 therefore identifies that second summand as the whole radical. The first copy is a complementary semisimple subalgebra and is stable under the tangent involution \((X,U)\mapsto(\theta X,\theta U)\). For a nonzero semisimple \(\mathfrak g\), this gives a symmetric presentation whose acting algebra has a nonzero radical. The complete neutral metric on the tangent bundle, when the original odd space has a positive invariant form, is the metric already proved in F.1. □

**Example K.2 (A real ideal inside a complexification).** If \(\mathfrak b\) is an ideal of a real Lie algebra \(\mathfrak a\), then
\[
\mathfrak l=\mathfrak a+i\mathfrak b\subseteq\mathfrak a\otimes_{\mathbb R}\mathbb C
\]
is a real Lie algebra with involution given by complex conjugation. Its positive and negative spaces are \(\mathfrak a\) and \(i\mathfrak b\). If \(\mathfrak a\) is solvable, so is \(\mathfrak l\); one may in particular take \(\mathfrak b=[\mathfrak a,\mathfrak a]\).

**Proof.** For \(x,y\in\mathfrak a\) and \(u,v\in\mathfrak b\), expand by complex bilinearity:
\[
[x+iu,y+iv]=[x,y]-[u,v]+i([x,v]+[u,y]).
\]
The real part belongs to \(\mathfrak a\), and both imaginary brackets belong to \(\mathfrak b\) by the ideal condition. This proves closure. Conjugation respects this formula, has square one, and fixes exactly the first real summand while reversing the second. H.2 proves that the complexification of a solvable algebra is solvable. Its underlying real algebra is also solvable: each real derived-series term is contained in the corresponding complex one, simply by the same brackets. The real subalgebra \(\mathfrak l\) is therefore solvable by H.2. The derived algebra is always an ideal, also proved in H.2, giving the last example. These are algebraic symmetric pairs; no global integration theorem for arbitrary abstract Lie algebras is being assumed here. □

**Example K.3 (Isotropic pieces for a simple real algebra).** For positive integers \(p,q\), put \(n=p+q\). The simple real algebra \(\mathfrak{sl}(n,\mathbb R)\), with involution conjugating by \(\operatorname{diag}(I_p,-I_q)\), has an odd space consisting of two invariant isotropic summands of dimension \(pq\). Its Killing form restricts there to a nondegenerate form of signature \((pq,pq)\). It gives a complete symmetric pseudo-Riemannian space with this tangent metric.

**Proof.** We first establish simplicity, so the assertion does not depend on an unproved matrix-algebra classification. The off-diagonal matrix units \(E_{ij}\), together with the diagonal differences \(E_{ii}-E_{jj}\), span \(\mathfrak{sl}(n,\mathbb R)\). Choose a traceless diagonal matrix \(D\) whose entries are \(2^1,\ldots,2^n\) minus their mean. The nonzero weights of \(\operatorname{ad}D\) are the distinct numbers \(2^i-2^j\), \(i\ne j\): for positive differences \(i>j\), the highest power of two dividing the difference determines \(j\), and the remaining odd factor determines \(i-j\); negative differences follow by sign. The zero weight is the diagonal space.

If a nonzero ideal contains a matrix with a nonzero off-diagonal entry, a polynomial spectral projection in \(\operatorname{ad}D\) isolates a nonzero multiple of some \(E_{ij}\). Such a projection is the product of the linear factors for all other distinct weights, divided by their nonzero values at the selected weight, as in H.1. The ideal is stable under it. If instead a nonzero ideal element is diagonal, its trace-zero entries are not all equal, and bracketing it with an appropriate \(E_{ij}\) again puts \(E_{ij}\) in the ideal.

Then \([E_{ij},E_{ji}]=E_{ii}-E_{jj}\) is in the ideal. Bracketing this diagonal difference with \(E_{ik}\) and \(E_{ki}\), for every \(k\ne i\), produces nonzero multiples of those matrix units, so all of them are in the ideal. For \(k,l\ne i\), \(k\ne l\), the bracket \([E_{ki},E_{il}]=E_{kl}\) supplies every remaining off-diagonal unit. Their opposite-unit brackets give all diagonal differences. The ideal is therefore the whole algebra, proving simplicity.

We also compute the Killing form. On all \(n\times n\) matrices let \(L_X(Z)=XZ\), \(R_Y(Z)=ZY\). In the basis \(E_{ij}\), the diagonal coefficients of \(L_A\), \(R_A\), and \(L_XR_Y\) sum respectively to
\[
n\operatorname{tr}A,\qquad n\operatorname{tr}A,\qquad
(\operatorname{tr}X)(\operatorname{tr}Y).
\]
Since \(\operatorname{ad}X=L_X-R_X\), multiplication and these three sums give
\[
\operatorname{tr}_{\operatorname{End}(\mathbb R^n)}
(\operatorname{ad}X\,\operatorname{ad}Y)
=2n\operatorname{tr}(XY)-2(\operatorname{tr}X)(\operatorname{tr}Y).
\]
The full matrix space is the direct sum of scalar matrices and traceless matrices; all adjoint operators vanish on the first summand and preserve the second. For traceless \(X,Y\) the displayed trace is therefore exactly their Killing form:
\[
K(X,Y)=2n\operatorname{tr}(XY).
\tag{K.1}
\]

The involution has block-diagonal even space and odd matrices
\[
X(P,Q)=\begin{pmatrix}0&P\\Q&0\end{pmatrix},
\qquad
P\in\operatorname{Mat}_{p\times q}(\mathbb R),\quad
Q\in\operatorname{Mat}_{q\times p}(\mathbb R).
\]
The upper and lower block spaces are separately preserved by every block-diagonal stabilizer. Brackets inside each are zero, while
\[
[X(P,0),X(0,Q)]=\operatorname{diag}(PQ,-QP).
\]
By (K.1),
\[
K(X(P,Q),X(P',Q'))
=2n\bigl(\operatorname{tr}(PQ')+\operatorname{tr}(P'Q)\bigr).
\tag{K.2}
\]
Each block space is thus isotropic, and the two are paired nondegenerately: individual opposite matrix units have pairing \(2n\), and all other basis pairings vanish. Their sums and differences give \(pq\) positive and \(pq\) negative directions, proving the signature.

For the actual symmetric space take \(G=SL(n,\mathbb R)^0\) and \(H=G^\sigma\). The determinant-one group is a closed Lie subgroup by [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1). Its Lie algebra is the traceless algebra: differentiating the determinant at the identity gives trace; conversely, for traceless \(X\), the determinant of \(\exp(tX)\) has derivative \((\operatorname{tr}X)\det(\exp(tX))=0\) and initial value one. The derivative formula follows by cofactor expansion at an invertible matrix, and the exponential ODE is [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). This whole exponential path lies in the identity component. Conjugation by the indicated diagonal matrix preserves \(G\), and \(H\) is the full closed fixed subgroup, so B.1 applies. Formula (K.1) is invariant under conjugation by cyclicity of trace; hence its nondegenerate odd restriction is invariant under all of \(H\). B.2 now gives the complete globally symmetric pseudo-Riemannian metric. The existence of the two isotropic invariant tangent pieces therefore occurs even for a simple acting algebra; it does not contradict D.2, whose metric is positive definite. □

## Further reading

- Vincent Pecastaing, *Lie groups and Riemannian symmetric spaces*, author notes dated 28 July 2023, [freely accessible author-hosted PDF](https://math.univ-cotedazur.fr/~pecastaing/symmetric_spaces.pdf), §2.1 and the opening of Chapter 5, on reflections and symmetric presentations.
- Alexander Kirillov, Jr., *Introduction to Lie Groups and Lie Algebras*, [freely accessible author-hosted notes](https://www.math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf), §§5.3–5.9, 6.1 and 6.3, on solvability, trace forms, Jordan decomposition, semisimple structure and the Casimir operator.
- Pavel Etingof, *Lie Groups and Lie Algebras I & II*, MIT 18.755, Spring 2024, [freely accessible MIT lecture notes](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §15.5 and §§48.1–48.2, on Engel's theorem, cocycles and Levi decomposition.

The local and global extension arguments, the algebraic prerequisites, and the degree-one and degree-two cocycle calculations used here are proved in this lesson or the linked earlier programme lessons.
