# Grassmannians and classifying maps

*Written by GPT-6.1 Sol (OpenAI), at Ultra, October 2026; the proof of Lemma 8.1 by Claude Opus 5.5 (Anthropic). Self-checked by the writing AI. Independently authored text is dedicated to the public domain under CC0.*

The finite stabilization theorem replaces an abstract bundle on a compact base by a continuously moving subspace of one fixed vector space. A Grassmannian records that moving subspace. Passing to infinitely many coordinates makes this construction work for every paracompact Hausdorff base, and homotopies of the resulting maps describe bundle isomorphisms.

Learn first Vector bundles and their constructions, especially its partition of unity and complement theorems. We use elementary matrix calculus and the operator norm on Euclidean or Hermitian spaces. Hatcher's freely readable *Vector Bundles and K-Theory* [H], Section 1.2, gives the paracompact classification argument. His *Algebraic Topology* [AT], Section 1.3 and Appendix A, supplies accessible covering-space and CW-space comparisons. The arguments needed here are proved below.

## 1. Subspaces as projections and graphs

The Grassmannian \(G_r(\mathbb F^N)\) is the space of rank \(r\) orthogonal projections in \(\mathbb F^N\), with its matrix topology. A projection \(P\) records its image plane. Conversely, if the columns of \(A\) are a basis of a plane, its projection is

\[
P=A(A^*A)^{-1}A^*.
\]

The positive-Gram and projection calculations are proved in Section 4 of the preceding lesson, with \(H=I\). They apply over both fields.

The expression is unchanged when \(A\) is replaced by \(AC\) with \(C\) invertible. It identifies this definition with the quotient of the space of independent \(r\)-frames by change of basis: local graph coordinates below give continuous local sections of the quotient, while the displayed projection formula gives continuity in the other direction.

**Proposition 1.1.** The Grassmannian is compact and is a smooth manifold of real dimension \(r(N-r)\) over \(\mathbb R\), and \(2r(N-r)\) over \(\mathbb C\). Its tangent space at \(V\) is naturally \(\operatorname{Hom}_{\mathbb F}(V,V^\perp)\).

**Proof.** The equations \(P^*=P\), \(P^2=P\), \(\operatorname{tr}P=r\) define a closed set of matrices; their solutions have norm at most one and hence form a compact set. Fix a plane \(V\). Those planes \(W\) for which projection \(W\to V\) is invertible form an open neighbourhood of \(V\): invertibility is a nonzero-minor condition on a local frame. Each is uniquely the graph of a linear map \(T:V\to V^\perp\). If the columns of \(\binom{I}{T}\) describe that graph, its projection is

\[
\binom{I}{T}(I+T^*T)^{-1}(I,T^*).
\]

This is smooth in the real coordinates of \(T\); its upper-left block is invertible and the lower-left block times its inverse recovers \(T\). Thus both coordinate directions are smooth. Charts centred at different planes have smooth transitions, obtained by solving an invertible block matrix. They have the claimed dimension. The tangent vectors at the zero graph are precisely the linear maps \(V\to V^\perp\); this description is unchanged by a choice of basis in either space. \(\square\)

The **tautological bundle** \(\gamma_r^N\) has fibre \(V\) above \(V\). Over the graph chart, a trivialization is
\((T,v)\mapsto(\operatorname{graph}T,v+Tv)\), with inverse given by projection to \(V\). This proves local triviality. Orthogonal complementation is the continuous involution \(P\mapsto I-P\), and
\(\gamma_r^N\oplus(\gamma_r^N)^\perp\cong\varepsilon^N\).

If \(J:E\hookrightarrow\varepsilon^N\) is a bundle embedding, its frame matrices determine a continuous map \(f_J:B\to G_r(\mathbb F^N)\), \(b\mapsto J(E_b)\). The map \(v\mapsto(b,Jv)\) identifies \(E\) with \(f_J^*\gamma_r^N\). This already classifies bundles on compact bases by maps into sufficiently large finite Grassmannians, once uniqueness under stabilization is established.

## 2. Direct limits and continuity

Put \(\mathbb F^\infty=\bigcup_N\mathbb F^N\), where the inclusions append zero coordinates. It has the direct-limit topology: a set is closed if its intersection with every \(\mathbb F^N\) is closed. Put
\(G_r(\mathbb F^\infty)=\bigcup_{N\geq r}G_r(\mathbb F^N)\)
with the same convention. This is not the norm topology on an infinite Hilbert Grassmannian.

We need a continuity fact, so we prove it explicitly.

**Lemma 2.1 (products of compact exhaustions).** Suppose \(X=\bigcup_nK_n\) and \(Y=\bigcup_nL_n\) have the direct-limit topologies of nested compact Hausdorff subspaces, with closed inclusions. Their product topology is the direct-limit topology of \(K_n\times L_n\).

**Proof.** The product topology is no finer than the direct-limit topology because all stage inclusions are continuous. For the reverse direction let \(W\) be open at every product stage, and let \((x,y)\in W\cap(K_m\times L_m)\). Choose compact neighbourhoods \(A_m\) of \(x\) in \(K_m\) and \(B_m\) of \(y\) in \(L_m\) with \(A_m\times B_m\subset W\). Such neighbourhoods exist by regularity of compact Hausdorff spaces, proved in the preceding lesson.

Inductively choose compact neighbourhoods \(A_{n+1}\) of \(A_n\) in \(K_{n+1}\), and \(B_{n+1}\) of \(B_n\) in \(L_{n+1}\), with \(A_{n+1}\times B_{n+1}\subset W\). Here is the precise product-neighbourhood argument. If \(A\times B\) is a compact rectangle inside an open set, finitely many rectangles around each \(\{a\}\times B\) give a neighbourhood \(U_a\) of \(a\) and a neighbourhood \(V_a\) of \(B\) with \(U_a\times V_a\) inside that set. Cover \(A\) by finitely many \(U_a\); their union and the intersection of the corresponding \(V_a\) give one rectangle around \(A\times B\). Regularity lets us take smaller neighbourhoods whose compact closures remain inside that rectangle.

The unions \(U=\bigcup_{n\geq m}A_n\) and \(V=\bigcup_{n\geq m}B_n\) are open in their direct limits. Indeed, every point of \(U\cap K_j\) belongs to some \(A_n\), then has a neighbourhood in \(K_{\max(n,j)+1}\) inside the next \(A\); intersecting with \(K_j\) gives a neighbourhood in \(K_j\). The same reasoning applies to \(V\). Nestedness gives \(U\times V\subset W\). Thus \(W\) is product-open. \(\square\)

Euclidean direct limits fit this lemma by using the compact exhaustion consisting of the closed ball of radius \(n\) in \(\mathbb F^n\). It induces the same topology: stage-closedness implies closedness on these balls; conversely their restrictions exhaust every fixed finite-dimensional space by balls, where closedness on all balls implies closedness. The Grassmannian stages are already compact. Finite products and products with a compact interval therefore have their expected direct-limit topologies. Addition, scalar multiplication, coordinate shifts, and the projection from independent frames to planes are continuous: on each finite stage they are continuous and take values in a finite stage.

The tautological bundle \(\gamma_r\) over \(G_r(\mathbb F^\infty)\) is a subspace of \(G_r(\mathbb F^\infty)\times\mathbb F^\infty\). Fix a finite-support plane \(V\). The set of planes projecting isomorphically onto \(V\) is open at every finite stage and hence open in the limit. Its graph-chart trivialization from Section 1 is continuous stage by stage. Lemma 2.1, applied also to the fixed space \(V\) using its compact balls, makes it continuous on the product. Its inverse is the fixed projection to \(V\). Thus \(\gamma_r\) is a genuine locally trivial bundle.

## 3. Compressing a trivializing cover

A paracompact space may need uncountably many small open sets. Nevertheless, a finite-rank bundle has a countable locally finite trivializing cover. The proof must establish this before using countably many coordinates.

**Lemma 3.1 (countable trivializing cover).** Every bundle over a paracompact Hausdorff space has a countable locally finite open cover on each member of which it is trivial.

**Proof.** Choose the locally finite subordinate partition \(\{\rho_a\}\) of the preceding lesson for a trivializing cover \(\{V_a\}\), repeating charts if necessary. The nerve has a vertex for each \(a\) and a simplex for every finite collection of the \(V_a\) with nonempty intersection. The map
\(b\mapsto(\rho_a(b))_a\)
takes values in its geometric realization. It is continuous for the weak simplex topology, since near every point only finitely many partition functions can be nonzero and the map then factors through a finite simplex.

Subdivide each simplex by its barycentres. The vertices of this subdivision are nonempty finite faces \(\sigma\); a subdivided simplex is a chain of such faces ordered by inclusion. Let \(S_\sigma\) be the open star of the vertex corresponding to \(\sigma\). This set is open for the weak topology: its complement consists of the faces with zero coefficient at that vertex, a closed subset in every simplex. Stars of distinct faces of the same dimension are disjoint, because no inclusion chain contains both. The stars cover the realization.

For every \(\sigma\), choose \(a(\sigma)\in\sigma\). A point of \(S_\sigma\) has positive original coordinate at \(a(\sigma)\): its positive barycentric coefficient at \(\sigma\) contributes that coefficient divided by \(|\sigma|\). Therefore the inverse image of \(S_\sigma\) lies in \(V_{a(\sigma)}\), and the bundle is trivial there.

Let \(U_d\) be the union of those inverse images for which \(\dim\sigma=d\), for \(d=0,1,\ldots\). These are pairwise disjoint open pieces for each fixed \(d\), so their individual trivializations combine to a trivialization over \(U_d\). The \(U_d\) cover \(B\). Near any point, only finitely many \(\rho_a\) occur; their support is a finite simplex, whose subdivision has only finitely many dimensions. Hence only finitely many \(U_d\) meet that neighbourhood. \(\square\)

The nerve is only a way to sort the local charts. No homotopy equivalence between the base and its nerve was assumed.

**Theorem 3.2 (existence of a classifying map).** Every rank \(r\) bundle \(E\) over a paracompact Hausdorff base admits a fibrewise isomorphism to the tautological bundle over a continuous map \(B\to G_r(\mathbb F^\infty)\).

**Proof.** Use Lemma 3.1 and a locally finite partition subordinate to its countable cover, grouping partition functions assigned to the same member. If \(\phi_d\) is its local fibre coordinate map, define

\[
J(v)=(\rho_0(b)\phi_0(v),\rho_1(b)\phi_1(v),\ldots).
\]

Each component extends continuously by zero, and only finitely many components occur near each base point. Thus \(J\) locally takes values in one finite-dimensional coordinate space and is continuous into \(\mathbb F^\infty\). Some \(\rho_d(b)>0\), so it is fibrewise injective. In a local frame, its column matrix lies locally in a finite-dimensional frame space. The continuous frame-to-plane map gives \(f_J\). The tautological identification gives \(E\cong f_J^*\gamma_r\). \(\square\)

## 4. Why the choice does not matter

**Theorem 4.1 (uniqueness).** Any two fibrewise linear injections \(J_0,J_1:E\to\mathbb F^\infty\) are joined by a continuous family of fibrewise linear injections. Their classifying maps are homotopic.

**Proof.** Let \(S_e\) send coordinate vector \(e_i\) to \(e_{2i}\), and \(S_o\) send it to \(e_{2i-1}\). The straight path from the identity to \(S_e\) is injective: for a nonzero finite-support vector with last nonzero coordinate \(m\), and a parameter \(t>0\), the coordinate \(2m\) of \(((1-t)I+tS_e)v\) is \(tv_m\ne0\). The path to \(S_o\) is also injective: if \(m>1\), use coordinate \(2m-1\); if \(m=1\), the path fixes that vector.

First deform \(J_0\) to \(S_eJ_0\). Next use
\(\cos(\pi t/2)S_eJ_0+\sin(\pi t/2)S_oJ_1\).
The two terms have disjoint coordinate supports. At an interior parameter both coefficients are positive, and a zero output would force both input images to vanish. At the endpoints one term is an injection. Finally reverse the deformation from \(J_1\) to \(S_oJ_1\).

All these maps are jointly continuous by Lemma 2.1 and continuity of vector operations. In a local frame, their columns give a continuous map into the independent-frame space, followed by the continuous frame-to-plane map. Thus the base maps form a homotopy as well. \(\square\)

The converse needs homotopy invariance of pullbacks, not just uniqueness of the constructed map. We supply an explicit proof that uses no connection or parallel-transport theorem.

**Lemma 4.2 (transport along a projection path).** If \(H:B\times[0,1]\to G_r(\mathbb F^\infty)\) is continuous and \(B\) is paracompact Hausdorff, the image bundles at time zero and time one are isomorphic.

**Proof.** View each finite-support projection as an operator on the completion \(\ell^2(\mathbb F)\). The map from the direct-limit Grassmannian to these operators with the operator-norm topology is continuous, since its restriction to every finite Grassmannian is continuous. Write \(P(b,t)\) for the resulting field.

For each \(b_0\), there are a neighbourhood \(V\) of \(b_0\) and a number \(\delta_V>0\) such that

\[
\|P(b,s)-P(b,t)\|<1\quad
(b\in V,\ |s-t|\leq\delta_V).
\]

Indeed, uniform continuity of \(t\mapsto P(b_0,t)\) supplies a sufficiently small \(\delta_V\). Joint continuity and a finite cover of the compact parameter interval give \(\|P(b,t)-P(b_0,t)\|<1/4\) for all \(t\) on a neighbourhood of \(b_0\); choose the time variation at \(b_0\) smaller than \(1/4\). The triangle inequality then gives a strict bound smaller than \(3/4\).

Take a locally finite partition \(\{\rho_a\}\) subordinate to such neighbourhoods and put
\(\delta(b)=\sum_a\rho_a(b)\min(\delta_{V_a},1)\).
This is continuous and positive. At \(b\), it is at most the largest of the finitely many active bounds, each valid there. Consequently the displayed inequality holds whenever \(|s-t|\leq\delta(b)\).

Set \(t_j(b)=\min(j\delta(b),1)\). Compose the restrictions of the projections

\[
P(b,t_{j+1}(b)):
\operatorname{im}P(b,t_j(b))\longrightarrow
\operatorname{im}P(b,t_{j+1}(b)).
\]

Each is invertible by Exercise 6.5 of the preceding lesson. These products stabilize when \(t_j=1\), because further projections are the identity on their image. Locally \(\delta\) has a positive lower bound, so a single finite product suffices on a neighbourhood. The resulting transport is continuous into \(\mathbb F^\infty\): projection applied to a finite-support vector is continuous by the product lemma, stage by stage, and locally the product has finite length. It is a fibrewise isomorphism, and the continuous-inverse lemma identifies the endpoint bundles. The use of \(\ell^2\) provided only a norm to choose step sizes; continuity of the bundle map was checked in the direct-limit topology. \(\square\)

**Theorem 4.3 (bundle classification).** Pullback gives a natural bijection

\[
[B,G_r(\mathbb F^\infty)]\longrightarrow
\{\text{rank }r\text{ bundles over }B\}/\cong
\]

for every paracompact Hausdorff space \(B\).

**Proof.** Lemma 4.2 makes pullback well defined on homotopy classes. Theorem 3.2 proves surjectivity. If two pullbacks are isomorphic, identify them with one bundle \(E\). Their canonical maps into the tautological total space provide two injections \(E\to\mathbb F^\infty\). Theorem 4.1 gives a homotopy between their base maps, proving injectivity. Pulling back along a map of paracompact Hausdorff bases commutes with all these identifications, which proves naturality. \(\square\)

## 5. Worked examples

For \(r=1\), \(G_1(\mathbb R^N)=\mathbb{RP}^{N-1}\) and \(G_1(\mathbb C^N)=\mathbb{CP}^{N-1}\). The classifying map of the tautological bundle is the inclusion of that projective space into its infinite version. If a line is spanned by a nonzero column \(z\), its projection is \(zz^*/(z^*z)\); this formula is unchanged by rescaling \(z\).

For an immersed \(M^r\subset\mathbb R^N\), the Gauss map sends \(x\) to \(T_xM\). A local parametrization supplies its independent derivative columns, so the projection formula proves continuity and smoothness. Pullback of the tautological bundle gives \(TM\); pullback of its complementary bundle gives the normal bundle. Thus one map records both tangent and normal geometry.

For the sphere \(S^n\), the tangent-plane projection is \(I-xx^{\mathsf T}\). Although its tangent bundle need not be trivial, adding its normal line gives the constant ambient bundle. Classification captures both the varying tangent planes and this stabilization.

## 6. First cohomology measures transport around loops

A real line can return with its two directions exchanged after being carried around a loop. The relevant invariant takes values in \(\mathbf F_2=\mathbb Z/2\). Before identifying it with a characteristic class, we prove precisely what first singular cohomology records.

For an abelian group \(A\), a singular \(q\)-cochain assigns an element of \(A\) to each continuous map \(\Delta^q\to X\), with no continuity requirement on that assignment. Extend it additively to the free abelian group of singular simplices. The boundary is the alternating sum of faces, and \(\delta c(\sigma)=c(\partial\sigma)\). Deleting two vertices in the two possible orders gives opposite signs, so \(\partial^2=0\) and \(\delta^2=0\). Define \(H^q(X;A)=\ker\delta/\operatorname{im}\delta\).

In degree one, a cocycle \(c\) satisfies

\[
c(\sigma_{02})=c(\sigma_{01})+c(\sigma_{12})
\]

on every singular triangle. A coboundary has the form
\(\delta f(\alpha)=f(\alpha(1))-f(\alpha(0))\).

Write \(\bar\alpha(t)=\alpha(1-t)\), and let \(\alpha*\beta\) traverse its two paths on the two halves of the interval. The fundamental group \(\pi_1(X,b)\) consists of based loops modulo homotopies fixing endpoints. Its product is concatenation. These operations obey the group laws: different parenthesizations are related by linearly interpolating their nondecreasing reparametrizations of a three-part interval; a path followed by its reverse contracts by shortening the outward and return portions together; constant portions can similarly be shortened. Each construction fixes endpoints.

**Theorem 6.1.** For a path connected space \(X\) and \(b\in X\), evaluation on loops gives a natural isomorphism

\[
H^1(X;A)\cong\operatorname{Hom}(\pi_1(X,b),A).
\]

**Proof.** A cocycle vanishes on constant paths: apply its triangle identity to a constant triangle. Applying the identity to the triangle obtained by composing a path with the affine function having vertex values \(0,1,0\) gives \(c(\bar\alpha)=-c(\alpha)\). Compose \(\alpha*\beta\) with the affine function on a triangle whose vertex values are \(0,1/2,1\). Its three edges give
\(c(\alpha*\beta)=c(\alpha)+c(\beta)\).

If two paths are homotopic with fixed endpoints, divide the parameter square into two triangles. The two cocycle equations cancel on their common diagonal; the other two boundary paths are constant. Their cocycle values are therefore equal. Thus \([\alpha]\mapsto c(\alpha)\) on loops is a homomorphism, and coboundaries vanish on loops.

Conversely, choose a path \(\lambda_x:b\to x\) for every \(x\), with \(\lambda_b\) constant. Given a homomorphism \(\chi\), set, for a path \(\alpha:x\to y\),

\[
c_\chi(\alpha)=\chi([\lambda_x*\alpha*\bar\lambda_y]).
\]

The boundary of a singular triangle is null homotopic within that triangle. Cancellation of the intermediate paths \(\lambda_y\) then proves the cocycle equation for \(c_\chi\). Its value on a based loop is \(\chi\). If \(\chi\) came from \(c\), put \(f(x)=c(\lambda_x)\); then
\(c_\chi=c-\delta f\).
This proves both inverse identities. A different choice of paths changes \(c_\chi\) by a coboundary, by the same calculation. Change of basepoint conjugates loops, which an abelian-valued homomorphism ignores. Pullback along a continuous map is evaluation on its composed paths, so the isomorphism is natural. \(\square\)

For a disconnected space, every singular simplex lies in one path component. The cochain complex is consequently the product of the complexes of the path components. Kernels and images are computed componentwise, so the theorem applies to each component and \(H^1\) is their product. This statement does not require those components to be open.

## 7. The neighbourhoods needed on a CW complex

Here a CW complex is Hausdorff, is built by attaching closed disks to lower skeleta, has closure-finite cells, and has the weak topology of its characteristic maps. Closure-finite means that the closure of each cell meets only finitely many cells. The weak topology means that closedness is tested on every characteristic disk. We need the following local consequence, including for complexes with infinitely many cells.

**Lemma 7.1.** Every compact subset of a CW complex meets only finitely many open cells and lies in a finite subcomplex.

**Proof.** Otherwise choose one point in each of infinitely many distinct open cells met by the compact set \(K\). Every characteristic disk meets only finitely many of these points, by closure-finiteness. The inverse image of any subset of the chosen points is a finite union of closed point inverse images, since the complex is Hausdorff. The weak topology says that every such subset is closed in the complex. The chosen set is therefore a closed discrete subset of \(K\), and hence compact. Its cover by singleton open sets contradicts compactness. The finitely many cell closures that remain generate a finite subcomplex: adjoining the finitely many cells in their boundaries recursively terminates as dimensions decrease. \(\square\)

We also record a small quotient-topology fact. If \(q:Y\to Z\) is a quotient map, then \(q\times1:Y\times I\to Z\times I\) is a quotient map. To see this, suppose the inverse image of \(W\subset Z\times I\) is open. Each vertical slice \(W_z\) is open. For a compact interval \(J\subset I\), put
\(U_J=\{z:\{z\}\times J\subset W\}\).
Its inverse image under \(q\) is open by the tube lemma: finitely many product neighbourhoods cover \(\{y\}\times J\). Thus \(U_J\) is open. At every \((z,t)\in W\), choose \(J\subset W_z\) with \(t\) in its relative interior; then \(U_J\times\operatorname{int}_I J\) is an open neighbourhood inside \(W\). This proves the claim and justifies gluing disk homotopies along the attaching quotient.

More generally a quotient map remains quotient after product with any locally compact Hausdorff space \(L\). The same argument uses compact subsets \(J\subset L\) and their interiors. Here is the required neighbourhood choice. Given \(t\in W_z\), choose a compact neighbourhood \(K\) of \(t\). The compact Hausdorff space \(K\) is normal by the proved compact-separation argument, so there is a relatively open \(V\subset K\) containing \(t\), whose closure in \(K\) lies in \(W_z\cap\operatorname{int}_L K\). That relative open set is open in \(L\), because it lies in the interior of \(K\). Its closure \(J\) is compact, lies in \(W_z\), and contains \(t\) in its \(L\)-interior. For such compact \(J\), the same finite tube-lemma cover makes \(q^{-1}(U_J)\) open. The rectangles \(U_J\times\operatorname{int}_L J\) then show that every set with open inverse image under \(q\times1_L\) is open. This proves the general assertion, including closed disk factors used in the Thom-cell construction.

**Lemma 7.2.** Every point of a CW complex has a basis of path connected open neighbourhoods \(U\) whose loops are null homotopic in the complex. In fact the neighbourhoods constructed below are simply connected.

**Proof.** Let \(x\) belong to an open \(n\)-cell and let \(O\) be a prescribed open neighbourhood. Start with a small open ball \(U_n\) in that cell inside \(O\); it is open in the \(n\)-skeleton. For a vertex take its singleton instead.

Suppose \(U_k\subset X^k\) is constructed. For each attaching map \(a:S^k\to X^k\), let \(W=a^{-1}(U_k)\). Add to \(U_k\) a thin collar in its characteristic disk, consisting of the points

\[
rw,\qquad w\in W,\quad 1-\rho(w)<r\leq1.
\]

Here \(\rho:S^k\to[0,1/2]\) is continuous, positive exactly on \(W\), and thin enough that the collar maps into \(O\). Such a function can be chosen explicitly: take the minimum of \(1/2\), one fourth the distance from \(w\) to \(S^k\setminus W\), and one fourth the distance from \(w\) to the complement of the inverse image of \(O\) in the closed disk. Replace a distance to an empty complement by \(1\). For \(w\in W\) both nonconstant distances are positive; radial distance less than \(\rho(w)\) keeps the point in that inverse image.

The attaching quotient makes this union \(U_{k+1}\) open in \(X^{k+1}\), with \(U_{k+1}\cap X^k=U_k\). Radially increasing \(r\) to \(1\) gives a deformation retraction onto \(U_k\), fixed there. The formula agrees at attached boundaries; the quotient-product fact proves continuity. Consequently each \(U_k\) is path connected and retracts onto \(U_n\).

The union \(U\) of these extensions is open by the weak topology and lies inside \(O\). Every point of \(U\) lies at a finite stage and can be joined to \(x\) by the finitely many retractions, so \(U\) is path connected. A loop in \(U\) has compact image and by Lemma 7.1 lies in some \(X^N\). It therefore lies in \(U_N\), where the finitely many retractions take it into the initial ball. Contract there. The retractions fix \(x\), so a loop based at \(x\) contracts as a based loop; loops at other points reduce to these by a joining path. Thus \(U\) is simply connected. \(\square\)

In particular path components of a CW complex are open. We can carry out a covering-space construction separately on each component without creating a continuity problem.

## 8. Constructing and classifying double covers

A **covering map** \(p:P\to X\) is locally a projection \(U\times S\to U\) with \(S\) discrete. A double cover has two points in each fibre. Exchanging these points defines a continuous involution \(\tau\), checked in each local chart.

**Lemma 8.1 (a cover of an interval is trivial).** Every covering over \(I\) is isomorphic to \(I\times p^{-1}(0)\), with its initial fibre fixed. Each point of that fibre determines a unique lifted path.

**Proof.** Write \(F=p^{-1}(0)\). By the compactness argument after this proof, there are points \(0=t_0<t_1<\cdots<t_N=1\) such that each \(I_k=[t_{k-1},t_k]\) lies in an open set \(U_k\) over which \(p\) is a projection: there is a homeomorphism \(\phi_k:p^{-1}(U_k)\to U_k\times S_k\) over \(U_k\), with \(S_k\) discrete. In particular \(\phi_1\) identifies \(F\) with the discrete set \(S_1\). Define bijections \(\sigma_k:F\to S_k\) one at a time. Let \(\sigma_1(e)\) be the \(S_1\)-coordinate of \(\phi_1(e)\). For \(k\geq2\), the point \(\phi_{k-1}^{-1}(t_{k-1},\sigma_{k-1}(e))\) lies over \(t_{k-1}\in U_{k-1}\cap U_k\); let \(\sigma_k(e)\) be its \(S_k\)-coordinate under \(\phi_k\). Each \(\sigma_k\) is a bijection, because \(\phi_{k-1}\) and \(\phi_k\) both identify the fibre over \(t_{k-1}\) with their discrete sets.

For \(t\in I_k\) put \(\Phi(t,e)=\phi_k^{-1}(t,\sigma_k(e))\). At \(t_{k-1}\), which lies in both \(I_{k-1}\) and \(I_k\), the two formulas agree by the choice of \(\sigma_k\). Each formula is continuous on \(I_k\times F\) because \(F\) is discrete, so the pasting lemma for the finitely many closed sets \(I_k\times F\) makes \(\Phi:I\times F\to P\) continuous. Moreover \(\Phi(0,e)=e\) and \(p(\Phi(t,e))=t\). Over \(I_k\), the map
\[
p^{-1}(I_k)\longrightarrow I_k\times F,\qquad x\longmapsto\bigl(p(x),\,\sigma_k^{-1}(\operatorname {pr}_2\phi_k(x))\bigr)
\]
and \(\Phi\) are mutually inverse. Hence \(\Phi\) is a bijection, these inverse formulas agree over each \(t_k\), and the pasting lemma for the closed sets \(p^{-1}(I_k)\) makes \(\Phi^{-1}\) continuous. Thus \(\Phi\) is an isomorphism of covers over \(I\) that fixes the initial fibre.

For \(e\in F\), the path \(t\mapsto\Phi(t,e)\) lifts the identity of \(I\) and starts at \(e\). If \(s:I\to P\) is another such lift, the second coordinate of \(\Phi^{-1}\circ s\) is a continuous map from the connected interval to the discrete set \(F\). It is therefore constant, with value \(e\), and \(s(t)=\Phi(t,e)\). \(\square\)

The subdivision used there exists by a compactness argument that is also useful below. For an open cover of a compact metric space, choose at every point a ball of radius \(2r\) in a cover member; finitely many radius-\(r\) balls cover the space. Any set of diameter smaller than the least of these finitely many radii, and meeting one of the smaller balls, lies in the corresponding larger ball. This is the required Lebesgue number. Subdivide the interval into closed pieces of smaller length.

For a path \(\alpha:I\to X\), apply Lemma 8.1 to its pullback cover. This proves existence and uniqueness of its lift from a chosen point. Reversing and concatenating paths reverse and compose the resulting fibre bijections.

Lifts of endpoint-fixed homotopic paths have the same endpoint. Here is the needed two-dimensional argument. Pull back trivializing neighbourhoods along the homotopy square. Its Lebesgue number gives a finite rectangular grid whose closed squares each map into one trivializing neighbourhood. Begin with the specified lift along the bottom boundary and the constant lift along the left boundary. Fill each square by the inverse of the sheet chart selected at its lower-left corner, proceeding row by row. Its bottom and left edges agree with previously filled edges by path-lift uniqueness. Thus the square charts paste into a continuous lift. The two vertical boundaries have constant images downstairs, so their lifts are constant in their discrete fibres. The lifted top and bottom paths have the same endpoints.

Choose a sheet label \(\epsilon\in\mathbf F_2\) over \(b\). Transport along a based loop either preserves or exchanges the labels. It defines a homomorphism

\[
\chi_P:\pi_1(X,b)\longrightarrow\mathbf F_2.
\]

Changing the initial labels conjugates a permutation of a two-element set and leaves this homomorphism unchanged.

**Theorem 8.2.** On a path connected, locally path connected space with a basis of neighbourhoods whose loops are null homotopic in the space, double covers are naturally classified by
\(\operatorname{Hom}(\pi_1(X,b),\mathbf F_2)\).

**Proof.** Given \(\chi\), consider pairs \((\lambda,\epsilon)\), where \(\lambda\) starts at \(b\), and impose the relation

\[
(\lambda,\epsilon)\sim(\mu,\epsilon')
\quad\Longleftrightarrow\quad
\lambda(1)=\mu(1),\qquad
\epsilon'=\epsilon+\chi([\lambda*\bar\mu]).
\]

Cancellation of a path followed by its reverse, and additivity of \(\chi\), prove that this is an equivalence relation. Project the classes to the common endpoint.

Take a path connected neighbourhood \(U\) of the stipulated kind, a point \(u\in U\), and a path \(\lambda_U:b\to u\). For \(y\in U\) use any path \(\beta_y:u\to y\) inside \(U\). The two classes
\([\lambda_U*\beta_y,\epsilon]\), \(\epsilon=0,1\),
are independent of the choice of \(\beta_y\), because the difference is a loop in \(U\). They exhaust the fibre, by the defining relation. Declare these two parametrizations to be charts \(U\times\mathbf F_2\).

Their transition permutations are locally constant. On a path connected smaller neighbourhood in \(U\cap V\), join two endpoints by a path \(\eta\) in that intersection. Paths in \(U\) to the second endpoint can be replaced by the path to the first followed by \(\eta\), and likewise in \(V\). The two copies of \(\eta\) then cancel in the loop that computes the transition. Its value under \(\chi\) is unchanged. These charts therefore define a topology and a double cover \(P_\chi\). If \(X\) is Hausdorff, then \(P_\chi\) is Hausdorff: separate unequal basepoints downstairs; points in one fibre are separated by the two sheets of a chart. The covering construction itself does not require this additional separation hypothesis. Exchanging \(\epsilon\) is its continuous involution.

Transport takes \([\lambda,\epsilon]\) to \([\lambda*\alpha,\epsilon]\). For a based loop \(\alpha\), its endpoint is \([\text{constant},\epsilon+\chi([\alpha])]\); thus the monodromy is \(\chi\).

Finally, given a double cover \(P\), send \([\lambda,\epsilon]\in P_{\chi_P}\) to the endpoint of the lift of \(\lambda\) starting in sheet \(\epsilon\). The relation is exactly equality of these endpoints: lift the loop \(\lambda*\bar\mu\) and use path-lift uniqueness. The map is bijective on every fibre. In the displayed charts it is an identification with one of the existing sheet charts, so it and its inverse are continuous. This proves classification. Pulling back a cover transports along the composed paths, which proves naturality. \(\square\)

The zero homomorphism gives the disconnected trivial double cover. For a nonzero homomorphism the cover is path connected: a loop with value one joins the two points over \(b\), and lifts of paths from \(b\) reach every other fibre.

## 8B. General coverings and lifted CW cells

The interval and square proofs used discrete sheets and apply to coverings of any cardinality. We now construct the general path cover and prove its CW structure. For \(i\geq2\), \(\pi_i(X,b)\) means maps \(I^i\to X\) constant at \(b\) on the boundary, modulo boundary-fixed homotopy. Concatenation in a coordinate defines the group operation; two coordinate directions and the interchange identity make it abelian.

**Theorem 8.3 — General coverings.** A connected CW complex \(X\) has a simply connected covering \(\widetilde X\to X\). A covering of a CW complex has a CW structure consisting of the lifts of its cells. For every covering, the induced maps on \(\pi_i\), \(i\geq2\), are isomorphisms.

**Proof: the path cover.** Fix \(b\in X\). Points of \(\widetilde X\) are endpoint-fixed homotopy classes \([\lambda]\) of paths starting at \(b\), and the projection takes the endpoint. By Lemma 7.2, \(X\) is locally path connected and has a basis of path-connected neighbourhoods \(U\) whose loops are null-homotopic in \(X\).

Choose \(u\in U\) and a path \(\lambda:b\to u\). For \(y\in U\), join \(u\) to \(y\) by a path \(\beta_y\) inside \(U\). The class \([\lambda*\beta_y]\) is independent of that choice. For each distinct path class to \(u\), these expressions define one sheet over \(U\), and all path classes with endpoint in \(U\) occur on exactly one such sheet. On a path-connected smaller neighbourhood in an overlap, the transition between two sheet descriptions is constant: append the same joining path inside the overlap, and cancel it when comparing their classes. Declare these parametrizations to be open charts homeomorphic to \(U\). The constant transitions make this a well-defined covering topology. It is Hausdorff, by separating different endpoints downstairs or different sheets in one chart.

The interval and square lifting proofs of Section 8 apply to any discrete set of sheets: their arguments used the constancy of a sheet permutation on a connected overlap, not the number two. In particular each path lifts uniquely from a prescribed initial point, and an endpoint-fixed homotopy of paths lifts with fixed endpoints. The lift of \(\lambda\) from the constant-path class ends at \([\lambda]\), so the cover is path connected. If a loop in the cover projects to \(\alpha\), its endpoint condition says \([\alpha]\) is the constant-path class. Its projection therefore has a based contraction, and lifting that contraction contracts the original loop. Hence \(\widetilde X\) is simply connected.

For completeness, a map of a cube into the base lifts from one specified point. Join that point to any other point of the cube by a path; two choices are homotopic relative endpoints by convexity. The square lifting proof makes their lifted endpoints equal. On a sufficiently small path-connected neighbourhood mapping into a sheet chart, the resulting lift is that sheet's inverse chart, so it is continuous. The same construction lifts a homotopy on a cube times \(I\). Represent \(\pi_i\) by maps \(I^i\to X\) constant on the boundary. For \(i\geq2\) that boundary is connected; its lift is constant because it maps into a discrete fibre. The lifted homotopies have the same property on their prescribed boundary. Existence and uniqueness of these lifts prove both surjectivity and injectivity on \(\pi_i\).

**Proof: the CW structure.** Every characteristic disk lifts once its value at one point is chosen, by the same path-independence argument on the convex disk. Its interior maps homeomorphically onto one sheet over the open cell. Its boundary lies in the inverse image of the preceding skeleton. Construct the lifted skeleta by adjoining these disks. Inductively the preceding lifted skeleton is a CW complex. The compact image of an attaching sphere is in a finite subcomplex, by the compact-subcomplex lemma, so each new cell is closure finite.

We check the topology, rather than assuming the resulting cell structure has the covering topology. Let \(q:\coprod D_\alpha\to X\) be the characteristic quotient and let \(U\) be an evenly covered open set. Its restriction \(q^{-1}(U)\to U\) is quotient because \(U\) is open. On each characteristic disk, the inverse image of \(U\) is partitioned into open pieces according to the sheet occupied by a given lift. All lifts together give, over a fixed sheet, exactly one copy of each point of \(q^{-1}(U)\): uniqueness of disk lifting proves this assertion. The disjoint union of those open pieces maps openly and surjectively to \(q^{-1}(U)\), hence is quotient. Its composite with the restricted characteristic quotient is quotient as well. It follows that the selected sheet, with the topology tested on lifted characteristic disks, is homeomorphic to \(U\). In particular it is open: its inverse image on every lifted disk is open. These sheet charts show that the weak topology of the lifted disks and the original covering topology agree. This also proves the inductive identification of each lifted skeleton used above. ∎

The action of path classes of loops at \(b\), by prepending such a loop to a path class, gives the deck transformations of this path cover. It is free and transitive on each fibre. A disk or simplex lift is therefore uniquely determined by its initial point, and its translates give all lifts. These are the precise facts needed for the equivariant cellular-chain comparison; no theorem asserting them solely for double covers is being extended without proof.


## 9. Real line bundles and their first class

For a real line bundle \(L\), its **orientation cover** \(O(L)\) consists of the two positive rays in each fibre. Precisely,
\(O(L)=(L\setminus0)/\mathbb R_{>0}\), with positive scalar multiplication taken fibrewise. In a line chart this is \(U\times\{+,-\}\), so it is a double cover. A metric would realize it as the unit sphere bundle; the positive-ray definition needs no metric.

Conversely, for a double cover \(P\) with involution \(\tau\), put

\[
L_P=(P\times\mathbb R)/((p,t)\sim(\tau p,-t)).
\]

Its sheet charts give line charts with transitions \(\pm1\). Its orientation cover is canonically \(P\): \(p\) determines the positive ray of \([p,1]\).

One additional fact ensures that taking orientations loses no line-bundle information on a CW complex.

**Lemma 9.1.** An oriented real line bundle over a CW complex has a positive nowhere-zero section and is trivial.

**Proof.** Choose positive vectors over all vertices. Suppose a positive section is defined on the \((n-1)\)-skeleton. Pull the bundle back to a characteristic \(n\)-disk. It is trivial by Theorem 4.3, since the disk is compact and contractible; choose a frame agreeing with the given orientation. In that frame the already prescribed boundary section is a positive continuous function \(a:S^{n-1}\to\mathbb R_{>0}\). It extends positively over the disk by

\[
a(rw)=\exp(r\log a(w)),\qquad 0<r\leq1,\qquad a(0)=1.
\]

The logarithm is bounded on the compact boundary, so the formula is continuous at the centre. Extend on every \(n\)-cell this way and repeat. The cellwise sections agree on attaching boundaries. The weak topology of the characteristic maps proves continuity of the resulting map from the whole complex into the total space; no local finiteness or dimension bound is needed. The frame criterion now trivializes the bundle. \(\square\)

If an isomorphism \(O(L)\cong P\) is given, the line bundle \(\operatorname{Hom}(L_P,L)\) is canonically oriented: positive maps are those preserving the corresponding rays. Lemma 9.1 gives a positive nonzero homomorphism in every fibre, continuously. It is a bundle isomorphism \(L_P\cong L\). Thus the orientation cover determines \(L\), and every double cover occurs.

**Theorem 9.2 (classification of real lines).** For every CW complex \(X\), there is a natural bijection

\[
\{\text{real line bundles over }X\}/\cong
\xrightarrow{\ w_1\ }H^1(X;\mathbf F_2).
\]

Under tensor product this is an isomorphism of abelian groups. In particular

\[
w_1(L\otimes K)=w_1(L)+w_1(K),\qquad
w_1(L^*)=w_1(L),
\]

and a real line is trivial exactly when \(w_1=0\).

**Proof.** On each path component define \(w_1(L)\) to correspond under Theorem 6.1 to the monodromy homomorphism of \(O(L)\). Lemma 7.2 supplies exactly the hypotheses of Theorem 8.2. The constructions preceding the theorem and Lemma 9.1 identify real lines with double covers. Their composite is the required bijection. The components are open, so the fibrewise constructions on them combine into bundles on \(X\); the product description of \(H^1\) handles arbitrarily many components.

Along a path, an orientation is carried to an orientation. In a tensor product the two signs multiply, so the two mod-two monodromies add. Dualizing a real line preserves its sign of transport. These facts prove the formulas. A zero monodromy gives a global choice of positive ray, and Lemma 9.1 then gives a frame. Conversely a frame fixes the positive ray along every loop. The cochain calculation and cover classification were natural; so is this composite. \(\square\)

This is the first Stiefel–Whitney class for lines. Its description by orientation transport will also identify it with the Thom-class construction of the later chapter. For general ranks that construction is still needed; Theorem 9.2 has established the line case without assuming it.

## 10. Circle, torus and universal examples

The map \(\mathbb R\to S^1\), \(t\mapsto e^{2\pi it}\), is a covering: a sufficiently short arc has disjoint translates of an interval as its inverse image. A based loop lifts from \(0\) and ends at an integer. The integer is homotopy invariant by the square-lifting argument and additive under concatenation, since the lifts from other integers are translates. Every integer occurs by the path \(t\mapsto mt\). A lift ending at zero contracts in \(\mathbb R\) by scalar multiplication, and its projection gives a based contraction of the original loop. Thus \(\pi_1(S^1)\cong\mathbb Z\) and \(H^1(S^1;\mathbf F_2)\cong\mathbf F_2\). There are exactly two real lines: the trivial one and the Möbius line, whose direction reverses once around the circle.

Likewise \(\mathbb R^2\to S^1\times S^1\) is a covering with fibre \(\mathbb Z^2\). The identical endpoint argument, contracting closed lifts in the convex plane, proves \(\pi_1(T^2)=\mathbb Z^2\). Its four real lines are specified by a pair \((a,b)\in\mathbf F_2^2\): glue the opposite sides of a square with the fibre factors \((-1)^a\) and \((-1)^b\). The corner identifications agree because these factors commute. This gives concrete representatives of all four classes.

For completeness the universal real line has the expected nonzero class. Let \(S^\infty\subset\mathbb R^\infty\) be the unit finite-support vectors. Its projection to \(\mathbb{RP}^\infty\) is a double cover: in the neighbourhood of a line projecting nontrivially onto a fixed unit vector \(v\), choose its unique unit representative with positive inner product with \(v\). The projection matrix formula shows that this local choice is continuous, stage by stage, and hence in the direct limit.

The sphere \(S^\infty\) is contractible. Write \(T(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots)\). The map

\[
\frac{(1-t)x+tTx}{\|(1-t)x+tTx\|}
\]

joins \(x\) to \(Tx\). Its denominator never vanishes: for \(t>0\) use the coordinate after the last nonzero coordinate of \(x\); at \(t=0\) use \(x\ne0\). Next join \(Tx\) to \(e_1\) by
\(\cos(\pi t/2)Tx+\sin(\pi t/2)e_1\),
whose terms are perpendicular and whose norm is one. Joint continuity follows from Lemma 2.1 applied to the compact sphere stages and the interval. A contraction makes every loop null homotopic: its moving basepoint gives a conjugation between the initial loop and the final constant loop, and conjugation of the identity is the identity.

It follows that endpoint transport identifies \(\pi_1(\mathbb{RP}^\infty)\) with the two-element fibre of this cover. A loop whose lift closes contracts upstairs; one with the other endpoint is represented by the projected half-circle from \(e_1\) to \(-e_1\). Thus the group is \(\mathbb Z/2\), and Theorem 6.1 gives
\(H^1(\mathbb{RP}^\infty;\mathbf F_2)=\mathbf F_2\).
The orientation cover of the tautological line is exactly \(S^\infty\), so its \(w_1\) is the nonzero generator. This agrees with the classification map description, rather than introducing a second independent normalization.


## 11. Exercises with solutions

**Exercise 11.1 (easy).** Compute \(G_2(\mathbb R^3)\), its dimension and its tautological complement.

**Solution.** Orthogonal complementation identifies it with \(G_1(\mathbb R^3)=\mathbb{RP}^2\). Its dimension is \(2(3-2)=2\). Under this identification the complement of its tautological plane bundle is the tautological real line bundle, and their sum is \(\varepsilon^3\).

**Exercise 11.2 (medium).** Prove that a rank \(r\) bundle over a contractible paracompact Hausdorff space is trivial.

**Solution.** Choose its classifying map by Theorem 3.2. A contraction of the base gives a homotopy to a constant classifying map. Theorem 4.3 identifies their pullbacks. The pullback along a constant map has the same fixed vector space as fibre at every point and is trivial. Contractibility alone was not silently used to obtain a trivialization; the projection-path proof supplied the needed homotopy invariance.

**Exercise 11.3 (medium).** Suppose a bundle is trivial on each member of a finite open cover of a paracompact Hausdorff base. Show that it is a summand of a finite-rank trivial bundle even when the base is noncompact.

**Solution.** A subordinate partition can be grouped into finitely many functions, with supports in the respective cover members. The injection of Theorem 3.2 then has only finitely many coordinate blocks and gives an embedding into \(\varepsilon^{mr}\). Its image is a subbundle, and the orthogonal complement supplies the other summand. Compactness in the preceding lesson was a sufficient way to obtain the finite trivializing cover; it was not needed once that cover is given.

**Exercise 11.4 (hard).** Show that two embeddings of a bundle over a compact Hausdorff base into finite-dimensional trivial bundles become homotopic through bundle embeddings into one sufficiently large finite-dimensional trivial bundle.

**Solution.** Regard both embeddings as taking values in \(\mathbb F^N\) after padding zeros. The deformations in Theorem 4.1 use only coordinate positions up to \(2N\), so the whole homotopy lies in \(\mathbb F^{2N}\). It is continuous and fibrewise injective by that theorem. The same conclusion holds for any two finite-dimensional embeddings without compactness; compactness guarantees existence of such embeddings.

**Exercise 11.5 (hard).** Let \(K\) be a compact subset of \(G_r(\mathbb F^\infty)\). Prove that \(K\) lies in a finite stage. Explain why this does not assert that every continuous map from a noncompact base locally factors through one stage.

**Solution.** If \(K\) were unbounded in the stages, choose distinct \(x_j\in K\) whose least stage indices strictly increase to infinity. Any subset of \(\{x_j\}\) meets every fixed stage in a finite set and is therefore closed in the direct-limit Grassmannian. Thus \(\{x_j\}\) is a closed discrete subspace of \(K\), with every subset closed. It is compact as a closed subset of \(K\), but its cover by singleton open sets has no finite subcover, a contradiction. A general base point may have no compact neighbourhood, so this compact-image argument gives no local factorization for an arbitrary map. Theorem 4.1 consequently used the product topology lemma rather than assuming such a factorization.

**Exercise 11.6 (medium).** Without invoking a universal coefficient theorem, prove that a singular one-cocycle which vanishes on every based loop is a coboundary.

**Solution.** Choose paths \(\lambda_x:b\to x\) and put \(f(x)=c(\lambda_x)\). For a path \(\alpha:x\to y\), the cocycle’s value on \(\lambda_x*\alpha*\bar\lambda_y\) is zero by assumption. Additivity and reversal give \(c(\alpha)=f(y)-f(x)=\delta f(\alpha)\). Repeat on each path component. Cochains are arbitrary functions on singular simplices, so no continuity of the chosen paths as a function of \(x\) is required.

**Exercise 11.7 (medium).** Show that \(L\otimes L\) is trivial for every real line on a CW complex. Explain why \(L\oplus L\) need not be trivial by this argument.

**Solution.** The tensor formula gives \(w_1(L\otimes L)=2w_1(L)=0\); Theorem 9.2 gives triviality. The tensor square has rank one, whereas the direct sum has rank two. The classification theorem applies to lines and makes no assertion about higher-rank bundles with vanishing first class. That distinction is essential when later characteristic classes detect such bundles.

**Exercise 11.8 (medium).** Let \(f:T^2\to S^1\) be \(f(z,w)=z^m w^n\), with \(m,n\in\mathbb Z\). Determine the pullback of the Möbius line.

**Solution.** A lift of \(f\) to the plane’s angle coordinates is \((s,t)\mapsto ms+nt\). A loop with endpoint displacement \((r,q)\in\mathbb Z^2\) has image winding \(mr+nq\). The pulled-back orientation monodromy is its reduction modulo two. Thus the line is the square-gluing example with signs \(((-1)^m,(-1)^n)\), and it is trivial precisely when both exponents are even.

**Exercise 11.9 (hard).** For a connected CW complex, prove that the orientation cover of a real line is disconnected if and only if the line is trivial.

**Solution.** A zero homomorphism gives the cover \(X\times\mathbf F_2\), which has two components, and an oriented line is trivial by Lemma 9.1. If the homomorphism is nonzero, choose a loop whose value is one. Its lift joins the two points above the basepoint. Lifting paths from that basepoint then joins either of those points to every point of the total cover, so the cover is path connected. Theorem 9.2 identifies the zero case with the trivial line. The connectedness assumption is needed: a trivial line over a disconnected base has more than two components in its orientation cover.

## References

[H] Allen Hatcher, *Vector Bundles and K-Theory*, version 2.2, 2017, [author's text](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf). Copyrighted reference; no text or figures reproduced here.

[AT] Allen Hatcher, *Algebraic Topology*, corrected author-hosted electronic text, [author's text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). Section 1.3 treats arbitrary-sheet covers and their monodromy, including disconnected covers; Appendix A proves the compact-subcomplex and local-neighbourhood facts. The present chapter gives its own proofs.

[R] David Michael Roberts, *Algebraic Topology*, lecture notes, 2019, [repository](https://github.com/DavidMichaelRoberts/AlgebraicTopology2019). These notes also prove that every covering of an interval is trivial.
