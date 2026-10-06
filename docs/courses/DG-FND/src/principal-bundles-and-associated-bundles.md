# Principal bundles and associated bundles

Differential geometry foundations

A frame identifies an abstract vector space with one particular fibre. Changing that frame changes coordinates, while the vector itself stays fixed. A principal bundle records the possible frames; an associated bundle uses those frames to carry vectors, tensors or points of another manifold. We construct both objects from their coordinate changes and then interpret metrics and orientations as restrictions on the allowed frames.

All manifolds and Lie groups here are finite dimensional, Hausdorff, second countable, smooth and without boundary. A Lie group has smooth multiplication and inversion. Its identity is \(e\). Vector bundles have constant finite rank; rank zero is allowed. Unless a complex bundle is specified, vector spaces are real. We use the usual real and complex number systems and the axiom of choice.

The earlier programme lesson [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md), abbreviated **Local tools**, proves the analytic facts used below: finite linear algebra and norms in 0.2, differentiation and the fundamental theorem of calculus in 0.3, smooth matrix inversion in 0.4, inverse and implicit functions in 1.2–1.3, partitions of unity in 3.1, and the quotient by a closed embedded Lie subgroup in 4.1. Its 0.0 proves existence of positive square roots; smoothness on the positive real axis follows from 1.2 applied to \(t\mapsto t^2\), whose derivative is \(2t\ne0\). These are programme proofs, not external references in place of proofs.

## A. Coordinates, gluing and a distinguished point in each fibre

If \(U\subset M\) is open, write \(P|_U=\pi^{-1}(U)\). A **principal right \(G\)-bundle** is a smooth manifold \(P\), a smooth map \(\pi:P\to M\), and a smooth right action \(p\mapsto pa\), with an open cover on which there are diffeomorphisms
\[
\Phi_i:U_i\times G\longrightarrow P|_{U_i},
\qquad \pi\Phi_i(x,a)=x,\qquad
\Phi_i(x,ab)=\Phi_i(x,a)b.
\]
In particular the action is free and transitive on each fibre: in these coordinates it is right multiplication on \(G\). The projection is a surjective submersion because it is the product projection in every chart. A section on \(U\) is a smooth \(s:U\to P\) with \(\pi s(x)=x\).

**Theorem A.1 (constructing the total space).** Let \((U_i)\) be an open cover of \(M\), and let smooth maps \(g_{ij}:U_i\cap U_j\to G\) satisfy
\[
g_{ii}=e,\qquad g_{ij}g_{jk}=g_{ik}.
\tag{A.1}
\]
There is a principal \(G\)-bundle with local sections \(s_i\) satisfying \(s_j=s_i g_{ij}\). Its total space has the quotient topology obtained by identifying
\[
(j,x,a)\sim(i,x,g_{ij}(x)a)
\quad\hbox{in}\quad\bigsqcup_i\{i\}\times U_i\times G.
\tag{A.2}
\]

**Proof.** The relations in (A.1) imply \(g_{ji}=g_{ij}^{-1}\). Reflexivity, symmetry and transitivity of (A.2) follow respectively from \(g_{ii}=e\), this inverse identity, and the triple identity. Let \(P\) be the set of classes and define \(\pi[i,x,a]=x\). For \(x\in U_i\) each class over \(x\) has exactly one representative with index \(i\); hence \(\Phi_i(x,a)=[i,x,a]\) is a bijection onto \(P|_{U_i}\).

The quotient map is open. Indeed, if \(W\) is open in the disjoint union, its saturation in the \(i\)-th component is the union over \(j\) of the images of \(W\cap(\{j\}\times(U_i\cap U_j)\times G)\) under
\((x,a)\mapsto(x,g_{ij}(x)a)\). These maps are diffeomorphisms of the corresponding open products, with inverses given by \(g_{ji}\), so that union is open. The definition of the quotient topology now proves the assertion. Thus every \(\Phi_i\) is a homeomorphism onto an open set. The projection \(\pi\) is continuous, since its composite with the quotient map is continuous on each component.

Two total-space points over different base points have disjoint neighbourhoods pulled back from disjoint base neighbourhoods. Two distinct points over the same base point lie in one open product \(P|_{U_i}\); disjoint product neighbourhoods there are also open in \(P\). This proves that \(P\) is Hausdorff.

For countability, a second countable space has a countable subcover of any open cover: from a countable basis, keep the members contained in at least one cover member and choose one such cover member for each; these choices cover every point. Apply this to \((U_i)\). Each resulting \(U_i\times G\) is second countable, using products of the two countable bases. The union of those countably many bases, transported by the open homeomorphisms \(\Phi_i\), is a countable basis for \(P\). The countability of a countable union is proved explicitly after Local tools 2.3.

Finally
\[
\Phi_i^{-1}\Phi_j(x,a)=(x,g_{ij}(x)a)
\tag{A.3}
\]
is smooth. Combining these product charts with the ordinary manifold charts on \(U_i\) and \(G\) supplies a smooth atlas. The right action \([i,x,a]b=[i,x,ab]\) is well defined because the identifications multiply on the left; it is smooth in these charts. The sections \(s_i(x)=[i,x,e]\) have \(s_j=s_i g_{ij}\), as claimed. □

**Theorem A.2 (sections, division and changes of coordinates).** In a principal bundle there is a smooth division map
\[
\delta:P\times_M P\longrightarrow G,\qquad q=p\,\delta(p,q).
\tag{A.4}
\]
Every smooth local section gives a principal trivialization \((x,a)\mapsto s(x)a\). A global section exists exactly when \(P\) is isomorphic, over \(M\) and equivariantly, to \(M\times G\). If \(s_j=s_i g_{ij}\) and \(s_i'=s_i h_i\), then
\[
g_{ij}'=h_i^{-1}g_{ij}h_j.
\tag{A.5}
\]
The construction in A.1 recovers every principal bundle, and cocycles related by (A.5) give isomorphic bundles.

**Proof.** The fibre product in (A.4) has local coordinates \((x,a,b)\) from any bundle chart; the transition maps use the same base coordinate on the two factors, so these are smooth compatible charts. They agree with its subspace topology in \(P\times P\): in product charts the only restriction is equality of the two base points, whose diagonal is parametrized by \(x\mapsto(x,x)\). In these coordinates \(\delta=a^{-1}b\). This is smooth, is independent of the chart, and is the unique element satisfying (A.4). It also gives
\[
\delta(pa,qb)=a^{-1}\delta(p,q)b.
\tag{A.6}
\]

In an existing chart \(\Phi_i\), a section has the form \(s(x)=\Phi_i(x,c(x))\) with smooth \(c\). Its proposed trivialization is \((x,a)\mapsto\Phi_i(x,c(x)a)\), with inverse \(p\mapsto(\pi(p),c(\pi(p))^{-1}a_i(p))\), where \(a_i(p)\) is the original group coordinate. Both maps are smooth. A global section therefore gives the asserted product isomorphism; conversely an equivariant product isomorphism transports \((x,e)\) to a section.

For sections on a cover, \(g_{ij}(x)=\delta(s_i(x),s_j(x))\) is smooth and uniqueness of division proves (A.1). Equation \(s_j'=s_i'g_{ij}'\) becomes \(s_i g_{ij}h_j=s_i h_i g_{ij}'\), proving (A.5) by freeness. For a bundle given in advance, the maps \([i,x,a]\mapsto s_i(x)a\) are well defined by its transitions and are diffeomorphisms in every local chart; they give the claimed recovery. If (A.5) holds between two cocycles, the map from the primed gluing to the unprimed gluing is
\[
[i,x,a]'\longmapsto[i,x,h_i(x)a].
\]
On an overlap, \(h_i g_{ij}'=g_{ij}h_j\), so it is well defined. Its chart inverse uses \(h_i^{-1}\); it is smooth and equivariant. Passing to an intersection cover handles different initial covers, because the recovery map just constructed also identifies any restricted gluing with the original one. □

**Lemma A.3 (pullback and maps over the base).** For smooth \(f:N\to M\), the set
\[
f^*P=\{(y,p)\in N\times P:f(y)=\pi(p)\}
\]
is a principal \(G\)-bundle over \(N\), with action on \(p\). Its transitions are \(g_{ij}\circ f\). Any smooth equivariant map \(T:P\to Q\) covering the identity of \(M\) is a principal-bundle isomorphism.

**Proof.** Above \(f^{-1}(U_i)\) the parametrization \((y,a)\mapsto(y,s_i(f(y))a)\) has inverse obtained by the group coordinate of \(p\). It is a homeomorphism for the subspace topology: both directions are restrictions of continuous maps in the ambient product charts. These charts have precisely the stated smooth transitions; they cover the set and give the action its required product form. Hausdorffness follows either from the subspace topology or the separation argument of A.1; second countability follows by restriction of a countable ambient basis. The projection to \(P\) is smooth in these coordinates.

For the final assertion, choose sections \(s\) of \(P\) and \(t\) of \(Q\) on a common neighbourhood. There is a unique smooth \(c(x)\) with \(T(s(x))=t(x)c(x)\), by A.2. Equivariance says \(T(s(x)a)=t(x)c(x)a\); hence the chart formula for \(T\) is \((x,a)\mapsto(x,c(x)a)\). The inverse \((x,b)\mapsto(x,c(x)^{-1}b)\) is smooth. Such inverses agree on overlaps by uniqueness and give a global inverse. □

## B. Moving a model fibre with the frames

Let \(F\) be a nonempty manifold with a smooth left action of \(G\). On \(P\times F\) use the right action
\[
(p,v)a=(pa,a^{-1}v),
\]
and write \([p,v]\) for its orbit. The relation can also be written \([pa,v]=[p,av]\). This convention fixes every transition and equivariance sign below.

**Theorem B.1 (associated bundles and their quotient maps).** The orbit space
\(P\times_G F\), with its quotient topology, is a smooth fibre bundle over \(M\) with fibre \(F\). If \(s_j=s_i g_{ij}\), its coordinates are
\[
\Psi_i(x,v)=[s_i(x),v],\qquad
\Psi_i^{-1}\Psi_j(x,v)=(x,g_{ij}(x)v).
\tag{B.1}
\]
The quotient map \(q:P\times F\to P\times_G F\) is smooth and a submersion. In fact it is itself a principal \(G\)-bundle for the displayed right action. If the action on a finite dimensional vector space \(V\) is a smooth linear representation, \(P\times_G V\) is a vector bundle.

**Proof.** If \(p=s_i(x)a\), then \([p,v]=[s_i(x),av]\). The coordinate \(av\) is unique, since two orbit representatives whose first entries equal \(s_i(x)\) can be related only by \(e\), by freeness on \(P\). This proves the bijectivity and transition formula in (B.1).

The orbit map \(q\) is open: the saturation of any open \(W\subset P\times F\) is the union of its images under the diffeomorphisms \((p,v)\mapsto(pa,a^{-1}v)\), for \(a\in G\). The inverse image of the part of the orbit space over \(U_i\) is the open set \(P|_{U_i}\times F\), so the restricted map is again a quotient map. In coordinates on that set its proposed quotient coordinate is
\[
(x,a,v)\longmapsto(x,av).
\]
It is continuous and constant on orbits, and therefore induces a continuous inverse for \(\Psi_i\). The map \(\Psi_i\) itself is continuous by its definition through \(q\). Consequently its image is an open product chart for the actual quotient topology. The separation and countability proofs in A.1 apply with \(F\) in place of \(G\), giving a Hausdorff, second countable smooth total space with atlas (B.1).

There is a particularly useful change of coordinates before quotienting:
\[
(x,a,v)\longmapsto(x,w=av,a).
\tag{B.2}
\]
It is a diffeomorphism, with inverse \((x,w,a)\mapsto(x,a,a^{-1}w)\). Under (B.2), \(q\) is \((x,w,a)\mapsto(x,w)\), proving smoothness and the submersion claim. The right action becomes \((x,w,a)b=(x,w,ab)\), proving the principal-bundle assertion without requiring a general theorem about free actions.

For a representation, transitions \(v\mapsto g_{ij}v\) are invertible linear maps. Thus the local additions and scalar multiplications agree on overlaps and define the vector operations on the fibres. They are smooth in the displayed charts. This is the definition of a smooth vector bundle. □

**Theorem B.2 (sections and equivariant functions).** Smooth sections of \(P\times_G F\) correspond bijectively to smooth functions \(u:P\to F\) satisfying
\[
u(pa)=a^{-1}u(p).
\tag{B.3}
\]
The section associated with \(u\) is \(x\mapsto[p,u(p)]\) for any \(p\in P_x\). A smooth equivariant map \(r:F\to F'\) induces a smooth map \([p,v]\mapsto[p,r(v)]\) of associated bundles.

**Proof.** Equation (B.3) makes \([pa,u(pa)]=[p,a\,u(pa)]=[p,u(p)]\). In the \(i\)-th chart the proposed section is \(x\mapsto(x,u(s_i(x)))\), so it is smooth. Conversely write a section in that chart as \([s_i(x),v_i(x)]\). Every \(p=s_i(x)a\) has a unique \(u(p)\) with the same section value equal to \([p,u(p)]\), namely
\[
u(s_i(x)a)=a^{-1}v_i(x).
\tag{B.4}
\]
This is smooth, satisfies (B.3), and gives the same function in another chart because it was characterized uniquely by the section value. The two constructions undo one another pointwise. Finally \(r(av)=a\,r(v)\) ensures \([pa,r(v)]=[p,r(av)]\), so the proposed bundle map is well defined. In (B.1) its formula is \((x,v)\mapsto(x,r(v))\), which proves smoothness. □

## C. Vector frames, tensors and the adjoint fibre

A vector bundle can be specified by charts \(E|_{U_i}\cong U_i\times\mathbb R^r\) whose changes are \((x,v)\mapsto(x,t_{ij}(x)v)\) for smooth \(t_{ij}:U_i\cap U_j\to\mathrm{GL}(r,\mathbb R)\). Equivalently a local frame is a smoothly varying isomorphism \(e_i(x):\mathbb R^r\to E_x\). Its chart sends \((x,v)\) to \(e_i(x)v\); hence \(e_j=e_i t_{ij}\).

**Theorem C.1 (the frame bundle recovers the vector bundle).** Let
\[
\operatorname{Fr}(E)_x=\{\text{linear isomorphisms }p:\mathbb R^r\to E_x\}.
\]
With right action \(pa=p\circ a\), this is a principal \(\mathrm{GL}(r,\mathbb R)\)-bundle. Its associated standard vector bundle is canonically isomorphic to \(E\) by
\[
[p,v]\longmapsto p(v).
\tag{C.1}
\]
Smooth sections of \(\operatorname{Fr}(E)\) are exactly smooth frames of \(E\).

**Proof.** A frame over \(U_i\) has a unique expression \(e_i(x)a\), where \(a\) is invertible. This gives its smooth product chart; on overlaps its coordinates change by \((x,a)\mapsto(x,t_{ij}(x)a)\). A.1 therefore supplies its topology and principal-bundle structure. This topology also agrees with that obtained as the open subset of the bundle of \(r\)-tuples of vectors consisting of bases: in a vector chart the tuple is a square matrix, and invertible matrices form an open set by the Neumann argument in Local tools 0.4. The group operations are matrix multiplication and the smooth inverse proved there. Local tools 0.2 proves the finite dimensional basis and inverse criteria used here.

The map (C.1) respects \([pa,v]=[p,av]\). In a frame chart it is \([e_i(x),v]\mapsto e_i(x)v\), exactly the original vector-bundle chart, so it is a smooth fibrewise linear bijection with a smooth inverse. A section of \(\operatorname{Fr}(E)\) is locally a smooth invertible matrix \(a(x)\); its columns under \(e_i(x)\) are a smooth basis in every fibre. Conversely such columns give a smooth matrix in \(\mathrm{GL}(r)\), hence a section. Rank zero uses the unique empty basis and the one-element group \(\mathrm{GL}(0)\); the same conclusions hold. □

**Lemma C.2 (tensor coordinates and the tangent frame).** Duals, tensor products, mixed tensors and exterior powers of \(E\) are associated to \(\operatorname{Fr}(E)\) by their natural representations. For \(E=TM\), the coordinate tangent bases give precisely these frame-bundle transitions; consequently cotangent vectors and differential forms are associated tensors.

**Proof.** For a vector space \(V\), define \(V^*\) as its linear functionals. In a basis \(v_1,\dots,v_r\), the functionals \(v^j(v_i)=\delta_i^j\) form a basis: linearity says every functional is uniquely the sum of its values on \(v_i\) times \(v^i\). An invertible \(a:V\to V\) acts on \(V^*\) by \(\lambda\mapsto\lambda\circ a^{-1}\); two successive actions by \(b\) and \(a\) give \(\lambda\circ b^{-1}a^{-1}=\lambda\circ(ab)^{-1}\), the action by \(ab\). Its matrix is the inverse transpose, a smooth function of \(a\).

For clarity, the algebraic tensor space \(V\otimes W\) may be constructed as the vector space with formal basis \(v_i\otimes w_j\), with the bilinear symbol
\((\sum_i x_iv_i)\otimes(\sum_j y_jw_j)=\sum_{i,j}x_i y_j(v_i\otimes w_j)\). Any bilinear map has a unique linear extension from these basis values; this proves that a change of basis gives a unique isomorphism independent of the chosen presentation. The same construction with lists of indices gives every finite tensor power. A map \(a\otimes b\) acts separately on each factor. Its entries are products of matrix entries and its inverse is \(a^{-1}\otimes b^{-1}\); composition on pure tensors proves the composition law on the whole space, since those tensors span.

For \(\Lambda^k V\), use the basis \(v_{i_1}\wedge\cdots\wedge v_{i_k}\) indexed by strictly increasing \(k\)-tuples. Define the wedge of \(k\) arbitrary vectors by multilinear expansion, discarding repeated indices and using the sign of the permutation that orders the distinct indices. An adjacent swap reverses the sign, so the map is alternating. Conversely, the values of an alternating multilinear map on the increasing basis tuples determine all its values by these same rules. This proves the universal property and independence of the basis construction. When \(k>r\) the space is zero; for \(k=0\) it is the scalar field. Define \(\Lambda^k a\) by applying \(a\) to every factor. The just-proved universal property makes it a linear map. Composition and inversion are checked on wedges, which span, and its entries are finite polynomials in entries of \(a\).

It follows that \(a\) acts smoothly on each mixed tensor
\[
(\mathbb R^r)^{\otimes p}\otimes((\mathbb R^r)^*)^{\otimes q}
\]
and on each exterior power. A frame \(p:\mathbb R^r\to E_x\) transports vectors by \(p\), covectors by composition with \(p^{-1}\), and the other tensors factor by factor. The composition laws just proved say that replacing \(p\) by \(pa\) transports a tensor exactly as first applying the representation of \(a\) and then \(p\). Thus these maps descend from the associated bundles. In each frame chart they are the identity on tensor coordinates, so they and their inverses are smooth. This proves the assertions about the bundles.

Finally, define a tangent vector at \(x\) by its coordinate velocity, with velocities related under a chart change \(y=y(z)\) by \(v_y=D y(z)v_z\). The chain rule in Local tools 0.3 proves the cocycle identities for these invertible Jacobians; the derivative of the inverse chart proves invertibility. A.1 and B.1 therefore construct \(TM\) from these vector transitions. The \(z\)-coordinate tangent basis, expressed in the \(y\)-basis, has columns \(\partial y^i/\partial z^j\), so its frame transition is that same Jacobian. The covector bundle is its dual and the bundle of \(k\)-forms is \(\Lambda^k T^*M\), with the transformations already proved. □

**Lemma C.3 (the Lie bracket and its adjoint action).** The vector space \(\mathfrak g=T_eG\) has a Lie bracket defined by left invariant vector fields. The maps
\[
\operatorname{Ad}(a)=d(c_a)_e,\qquad c_a(b)=aba^{-1},
\tag{C.2}
\]
form a smooth linear representation of \(G\) preserving that bracket. Hence \(\operatorname{ad}(P)=P\times_G\mathfrak g\) is a vector bundle with a smooth fibrewise Lie bracket.

**Proof.** We include the differential facts needed to define the bracket. For a smooth scalar function \(f\) in a coordinate rectangle, apply the one-variable fundamental theorem twice to its rectangular increment
\[
f(x+he_i+ke_j)-f(x+he_i)-f(x+ke_j)+f(x).
\]
Computing the two successive increments in either order writes this same number as the respective iterated integral of \(\partial_j\partial_i f\) and \(\partial_i\partial_j f\). Divide by \(hk\), for \(h,k>0\), and let both tend to zero. Continuity makes each average tend to the derivative at \(x\): the error is at most the maximum deviation of that continuous derivative from its value at \(x\) on the shrinking rectangle. Thus the two mixed partials agree. This uses only Local tools 0.3 and continuity, not an interchange theorem for integrals.

For vector fields \(X=\sum X^i\partial_i\) and \(Y=\sum Y^i\partial_i\), the product rule and this equality show that their operator commutator on smooth functions is
\[
(XY-YX)f
=\sum_j\left(\sum_i X^i\partial_iY^j-Y^i\partial_iX^j\right)\partial_j f.
\tag{C.3}
\]
This is a smooth vector field. It is independent of the chart because the expression \(X(Yf)-Y(Xf)\) is independent of it, and a vector is determined by its values on the local coordinate functions. Denote it by \([X,Y]\). Bilinearity and antisymmetry are immediate from the commutator. Its Jacobi identity follows by expanding
\([X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]\): each of the six products of three operators occurs once with each sign and cancels. Applying this identity to local coordinate functions proves it as an identity of vector fields.

A diffeomorphism \(T\) preserves this bracket under pushforward. Indeed the chain rule gives
\[
((T_*X)f)\circ T=X(f\circ T);
\]
applying it twice gives
\(( [T_*X,T_*Y]f)\circ T=[X,Y](f\circ T)\).
Again coordinate functions determine the fields. For \(v\in T_eG\), let \(X_v(b)=d(L_b)_e v\). It is smooth because multiplication is smooth. Differentiating \(L_aL_b=L_{ab}\) proves left invariance. Every left invariant field has this form, by evaluating its invariance at \(e\); consequently the bracket of two such fields is left invariant, by the pushforward identity for \(L_a\). Define
\([v,w]=X_v,X_w\). The bijection \(v\mapsto X_v\) transports bilinearity, antisymmetry and Jacobi to this bracket.

The identities \(c_{ab}=c_a c_b\) and \(c_{a^{-1}}=c_a^{-1}\) imply that (C.2) is a representation into invertible linear maps. It is smooth: in coordinate charts near each \((a,e)\), its matrix entries are the partial derivatives in the second variable of the jointly smooth conjugation map. These matrices transform by fixed tangent-coordinate changes at \(e\). Differentiating \(c_a L_b=L_{c_a(b)}c_a\) gives \((c_a)_*X_v=X_{\operatorname{Ad}(a)v}\). Bracket preservation by the diffeomorphism \(c_a\) therefore yields
\[
\operatorname{Ad}(a)[v,w]=[\operatorname{Ad}(a)v,\operatorname{Ad}(a)w].
\tag{C.4}
\]

B.1 gives the associated vector bundle. If two elements in one fibre are written as \([p,v]\) and \([p,w]\), define their bracket to be \([p,[v,w]]\). They can always be expressed using the same \(p\), by transitivity of the principal action. Replacing \(p\) by \(pa\) replaces both coordinates by \(\operatorname{Ad}(a^{-1})\); (C.4) proves independence of this choice. In every trivialization the operation has the fixed bilinear structure coefficients of \(\mathfrak g\), so it is smooth and satisfies the Lie algebra identities. □

## D. Reductions: restricting the allowed frames

Let \(H\subset G\) be a **closed embedded Lie subgroup**. The embedded hypothesis is explicit; no closed-subgroup theorem is being used without proof. Local tools 4.1 supplies the smooth quotient \(G/H\), its quotient topology, the smooth left \(G\)-action, and smooth local sections of \(G\to G/H\).

An **\(H\)-reduction** of \(P\) is an embedded submanifold \(Q\subset P\), preserved by the right \(H\)-action, for which \(Q\to M\) is a principal \(H\)-bundle with this action. In particular, each \(Q_x\) is one right \(H\)-orbit inside \(P_x\).

**Theorem D.1 (reductions and sections of the quotient bundle).** The space \(P/H\) of right \(H\)-orbits is naturally the associated bundle \(P\times_G(G/H)\). Its smooth sections correspond bijectively to \(H\)-reductions of \(P\), by
\[
\sigma\longmapsto Q_\sigma=\{p\in P:pH=\sigma(\pi(p))\},
\qquad
Q\longmapsto\bigl(x\mapsto Q_x\bigr).
\tag{D.1}
\]

**Proof.** The map \([p,aH]\mapsto paH\) is well defined: replacing \((p,aH)\) by \((pb,b^{-1}aH)\) leaves \(paH\) unchanged. It is bijective, with inverse \(pH\mapsto[p,H]\). On the \(i\)-th principal chart the quotient by \(H\) is \(U_i\times(G/H)\). To see this with the quotient topology, \(G\to G/H\) is open, since the saturation of an open set is its union of right translates by \(H\); hence its product with \(U_i\) is open on basic open products and therefore on every open set. It is a continuous open surjection, so a quotient map. The orbit map \(P\to P/H\) is also open by the same saturation argument. Thus these local product identifications describe the actual quotient topology. They identify our bijection with the identity in the B.1 charts, proving it is a diffeomorphism.

In a principal chart, a section \(\sigma\) is a smooth \(c:U\to G/H\). For every \(x_0\in U\), take a local section \(\ell:W\to G\) of \(G\to G/H\) around \(c(x_0)\), and shrink \(U\) to \(c^{-1}(W)\). The map \(a(x)=\ell(c(x))\) is a smooth lift. In these coordinates
\[
Q_\sigma|_U=\{s(x)a(x)h:x\in U,\ h\in H\}.
\tag{D.2}
\]
The diffeomorphism \((x,g)\mapsto(x,a(x)^{-1}g)\) of \(U\times G\) carries this subset to \(U\times H\). Because \(H\) is embedded, (D.2) is an embedded submanifold with its subspace topology, and \((x,h)\mapsto s(x)a(x)h\) is a principal \(H\)-trivialization. If two such local sections are used, their relative group element is smooth into \(G\) by A.2 and takes values in \(H\); it is smooth as an \(H\)-valued map. Here is the embedded-submanifold fact just used: in a submanifold chart a map with image in \(H\) has coordinates \((h_1,\dots,h_k,0,\dots,0)\); its first \(k\) coordinates are smooth, and continuity for the subspace topology places its image locally in that chart. This proves the fact without another quotient theorem. It follows that all the local \(H\)-charts agree smoothly. Thus \(Q_\sigma\) is a reduction.

Conversely, choose a local section \(t:U\to Q\) of an \(H\)-reduction. The coset \(t(x)H\) is independent of the chosen section, since all elements of \(Q_x\) differ by right multiplication in \(H\). It is smooth as a map to \(P/H\), by the smooth inclusion \(Q\to P\) and the quotient charts. These local maps glue to a section. Its inverse image in \(P\) is exactly \(Q\), since each \(Q_x\) is one entire \(H\)-orbit. Conversely the coset of \(Q_{\sigma,x}\) is \(\sigma(x)\). This proves both inverse identities in (D.1). □

**Theorem D.2 (metrics and orthonormal reductions).** A smooth positive definite inner product on a real rank-\(r\) bundle \(E\) determines an \(\mathrm O(r)\)-reduction of \(\operatorname{Fr}(E)\), namely its orthonormal frames. Every such reduction determines a unique metric, and the constructions are inverse. Every smooth vector bundle over \(M\) has a smooth positive definite metric.

**Proof.** First \(\mathrm O(r)=\{a:a^{\mathsf T}a=I\}\) is a closed embedded Lie subgroup of \(\mathrm{GL}(r)\). Closedness follows by continuity. To verify embeddedness, consider \(F(a)=a^{\mathsf T}a\) valued in the vector space of symmetric matrices. Its derivative is \(dF_a(b)=a^{\mathsf T}b+b^{\mathsf T}a\), by the product rule. At \(a\in\mathrm O(r)\), every symmetric \(S\) is attained by \(b=aS/2\); thus this derivative is surjective. Choose a linear complement of its kernel by Local tools 0.2. The map which lists the kernel coordinate together with \(F\) has an invertible derivative, so Local tools 1.2 makes these local coordinates; the level \(F=I\) is therefore an embedded submanifold. Multiplication and inverse restrict smoothly, since \(a^{-1}=a^{\mathsf T}\). For \(r=0\) the assertion describes the one-point manifold and requires no derivative argument.

Given a metric \(\langle\, ,\,\rangle_x\) and a local frame \(e_1,\dots,e_r\), define successively
\[
v_j=e_j-\sum_{k<j}\langle e_j,u_k\rangle\,u_k,\qquad
u_j=\frac{v_j}{\sqrt{\langle v_j,v_j\rangle}}.
\tag{D.3}
\]
Induction shows that the preceding \(u_k\) are orthonormal, that \(v_j\) is perpendicular to them, and that \(u_1,\dots,u_{j-1}\) span \(e_1,\dots,e_{j-1}\). Thus \(v_j\ne0\), by independence of the original frame, and its norm is positive. The positive square root is smooth as proved in the introduction, so the \(u_j\) are smooth. Formula (D.3) gives a smooth orthonormal local frame \(u\). Every other orthonormal frame is uniquely \(ua\) with \(a^{\mathsf T}a=I\), because the inner products of its columns are the entries of \(a^{\mathsf T}a\). In the frame-bundle chart based on \(u\), the orthonormal subset is \(U\times\mathrm O(r)\). It is therefore an embedded principal \(\mathrm O(r)\)-subbundle.

Conversely, if \(Q\) is an \(\mathrm O(r)\)-reduction, declare \(p:\mathbb R^r\to E_x\) to be an isometry for any \(p\in Q_x\):
\[
\langle v,w\rangle_x=(p^{-1}v)^{\mathsf T}(p^{-1}w).
\tag{D.4}
\]
Another choice is \(pa\) for \(a\in\mathrm O(r)\); multiplication of both coordinates by \(a^{-1}\) preserves this expression. Local sections of \(Q\) make (D.4) smooth. It is positive definite, and its orthonormal frames are exactly \(Q_x\), because every frame is \(pb\) and (D.4) makes it orthonormal exactly when \(b^{\mathsf T}b=I\). This also proves uniqueness and the inverse assertions.

For existence, put the Euclidean metric on each local vector chart. Take a smooth partition of unity \((\phi_i)\) subordinate to a locally finite refinement of these charts, provided by Local tools 3.1. Define
\(\langle v,w\rangle_x=\sum_i\phi_i(x)\langle v,w\rangle_{i,x}\).
Each summand extends by zero outside its chart: near a point outside that chart its coefficient has support disjoint from a neighbourhood of the point. Locally only finitely many summands occur, so the sum is smooth. At any \(x\), the coefficients are nonnegative and sum to one; for \(v\ne0\), at least one positive coefficient multiplies a strictly positive \(\langle v,v\rangle_{i,x}\). The sum is therefore positive. In rank zero the zero bilinear form is the unique metric, with positivity understood for nonzero vectors, of which there are none. □

**Theorem D.3 (orientation and positive orthonormal frames).** For \(r\ge1\), orientations of \(E\) correspond to \(\mathrm{GL}^+(r,\mathbb R)\)-reductions of its frame bundle. A metric and an orientation together correspond to an \(\mathrm{SO}(r)\)-reduction. For rank zero there is one frame, one canonical orientation, and all these groups are trivial.

**Proof.** We specify the determinant facts used here. For a square matrix \(a\), define
\[
\det(a)=\sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)
 \prod_{j=1}^r a_{\sigma(j),j}.
\tag{D.5}
\]
The permutation sign is the parity of its number of inversions. Adjacent interchanges reverse that parity; sorting a permutation into increasing order proves both that this sign is well defined and that signs multiply under composition. Formula (D.5) is multilinear in columns. Interchanging two columns reverses its sign by reindexing the permutations, and repeated columns give zero by pairing the terms. Any alternating multilinear function of \(r\) columns is its value at the standard ordered basis times (D.5): expand every column in that basis, discard repeated indices, and order the remaining indices. Apply this uniqueness to the alternating multilinear function \((v_1,\dots,v_r)\mapsto\det(av_1,\dots,av_r)\); its value on the standard basis is \(\det a\). It follows that \(\det(ab)=\det(a)\det(b)\). An invertible matrix therefore has nonzero determinant, since \(\det I=1\); a noninvertible matrix has dependent columns by Local tools 0.2 and its determinant vanishes by multilinearity. Triangular matrices have determinant the product of diagonal entries, because only the identity permutation can give a nonzero term, successively from the first constrained row or column.

Reindexing (D.5) by \(\sigma^{-1}\), which has the same sign, also gives \(\det(a^{\mathsf T})=\det(a)\). The group \(\mathrm{GL}^+(r)=\{a:\det a>0\}\) is an open embedded subgroup of \(\mathrm{GL}(r)\) and also closed there, since its complement is \(\{\det a<0\}\), which is open. There are exactly two equivalence classes of bases under positive-determinant changes: relative to a fixed basis every basis is given by an invertible matrix, and its determinant is either positive or negative; multiplication by \(\operatorname{diag}(-1,1,\dots,1)\) switches the two. An orientation of a fibre means a choice of one class. A smooth orientation means that locally a smooth frame lies in the chosen class at every point. This does not assume a theorem identifying connected components of \(\mathrm{GL}(r)\).

The positive frames of such an orientation form \(U\times\mathrm{GL}^+(r)\) in every positive local frame chart. This is an embedded principal reduction. Conversely a reduction supplies positive local sections; all changes between them have positive determinant, so they define a consistent smooth orientation. The two constructions are inverse fibre by fibre.

For a metric and an orientation, apply (D.3) to a positive local frame. Each \(u_j\) is a linear combination of \(e_1,\dots,e_j\), with coefficient \(1/\sqrt{\langle v_j,v_j\rangle}>0\) on \(e_j\). Thus the change matrix is triangular with positive diagonal and positive determinant. The resulting orthonormal frame remains positive. Its changes are in
\(\mathrm{SO}(r)=\mathrm O(r)\cap\mathrm{GL}^+(r)\).
For an orthogonal matrix, determinant multiplicativity gives \((\det a)^2=1\), so this is precisely \(\{a\in\mathrm O(r):\det a=1\}\). It is an open and closed embedded subgroup of \(\mathrm O(r)\), hence an embedded subgroup of \(\mathrm{GL}(r)\); it is closed there by the equations \(a^{\mathsf T}a=I,\det a=1\). The positive orthonormal frames give its principal reduction, just as in D.2. Conversely an \(\mathrm{SO}(r)\)-reduction defines the metric by (D.4), independently of the chosen frame, and the orientation by its determinant sign. Its fibre is exactly all positive orthonormal frames, so the constructions are inverse. For \(r=0\), use determinant \(1\) for the empty matrix and the empty basis, which verifies the stated convention directly. □

## E. One bundle with two coordinate descriptions

**Example E.1 (the Hopf bundle and its associated line).** The unit vectors in \(\mathbb C^2\) form a principal \(U(1)\)-bundle over \(\mathbb {CP}^1\). With the convention \(s_1=s_0 g_{01}\), its transition is
\[
g_{01}(w)=\frac{|w|}{w},\qquad w\ne0.
\tag{E.1}
\]
The base is diffeomorphic to the unit sphere \(S^2\), and the associated standard complex line is the tautological line.

**Proof.** Regard \(\mathbb C^n\) as \(\mathbb R^{2n}\); conjugation, real and imaginary parts, and complex multiplication are real polynomial maps. The derivative of \(\sum |z_i|^2\) at a unit vector is nonzero (evaluate it on that vector). The implicit-function argument of Local tools 1.3 therefore makes its level set \(S^{2n-1}\) an embedded smooth manifold. In particular \(S^3\) and \(U(1)=\{a\in\mathbb C:|a|=1\}\) are smooth, Hausdorff and second countable. On \(U(1)\), multiplication and inverse \(a^{-1}=\bar a\) are smooth.

Define \(\mathbb {CP}^1\) as the complex lines in \(\mathbb C^2\), with the quotient topology from \(\mathbb C^2\setminus\{0\}\) under nonzero complex scaling. The lines with \(z_0\ne0\) have coordinate \(w=z_1/z_0\); those with \(z_1\ne0\) have coordinate \(v=z_0/z_1\). These are actual topological charts: the quotient map is open by taking the union of nonzero scalar translates of an open set; the coordinate maps on each saturated part are continuous, and their inverse maps are \(w\mapsto[1:w]\), \(v\mapsto[v:1]\), the composites of continuous maps with the quotient. Their change \(v=1/w\) is smooth off zero.

To verify separation and the full smooth structure directly, set
\[
\Theta([z_0:z_1])=
\frac{(2\operatorname{Re}(\bar z_0z_1),\
2\operatorname{Im}(\bar z_0z_1),\
|z_0|^2-|z_1|^2)}{|z_0|^2+|z_1|^2}.
\tag{E.2}
\]
Scaling numerator and denominator by the same \(|a|^2\) proves well-definedness. The identity
\(4|z_0|^2|z_1|^2+(|z_0|^2-|z_1|^2)^2=(|z_0|^2+|z_1|^2)^2\)
puts its image on \(S^2\). In the first chart its formula is
\[
w\longmapsto\frac{(2\operatorname{Re}w,2\operatorname{Im}w,1-|w|^2)}
 {1+|w|^2},
\]
with inverse \(w=(X+iY)/(1+Z)\) on the sphere minus \((0,0,-1)\). In the second chart it is
\[
v\longmapsto\frac{(2\operatorname{Re}v,-2\operatorname{Im}v,|v|^2-1)}
 {1+|v|^2},
\]
with inverse \(v=(X-iY)/(1-Z)\) off \((0,0,1)\). Substitution verifies both inverse identities, using \(X^2+Y^2=1-Z^2\). These maps cover the sphere and agree on the overlap. Thus \(\Theta\) is a homeomorphism and a diffeomorphism in the displayed charts. In particular the base is Hausdorff and second countable.

The projection \(\pi:S^3\to\mathbb {CP}^1\) sends a unit vector to its line. Define
\[
s_0(w)=\frac{(1,w)}{\sqrt{1+|w|^2}},
\qquad
s_1(v)=\frac{(v,1)}{\sqrt{1+|v|^2}}.
\tag{E.3}
\]
Both are smooth unit vectors. For \(z_0\ne0\), the equations
\[
(z_0,z_1)=s_0(w)a,\qquad
w=z_1/z_0,\quad a=z_0/|z_0|
\]
follow from \(|z_0|^2(1+|w|^2)=1\); they give smooth mutually inverse maps between \(\pi^{-1}(U_0)\) and \(U_0\times U(1)\). For \(z_1\ne0\) the same verification uses \(v=z_0/z_1\), \(a=z_1/|z_1|\). They are equivariant for right scalar multiplication on \(S^3\). This proves the principal-bundle assertion, including smoothness and submersion of its projection. On the overlap,
\[
s_1(1/w)
=\frac{(|w|/w,\ |w|)}{\sqrt{1+|w|^2}}
=s_0(w)\frac{|w|}{w},
\]
which proves (E.1). On the equator \(|w|=1\) the transition is \(w\mapsto\bar w\). Orient the circle by the positive tangent \(iw\) at \(w\). The derivative of conjugation sends \(iw\) to \(-i\bar w\), the negative tangent at the image. Conjugation is a diffeomorphism with itself as inverse, so it traverses that circle once with reversed orientation. This proves the negative transition sign without invoking a classification by winding numbers.

The tautological line has fibre the line \(\ell\) itself over \(\ell\). Its local vector charts are \((w,\xi)\mapsto(\ell_w,\xi s_0(w))\) and the analogous second chart. They are smooth, with inverse coefficient recovered by the ordinary Hermitian inner product with the unit vector \(s_i\). The map from the associated line is
\[
[(z_0,z_1),\xi]\longmapsto
\bigl([z_0:z_1],\,\xi(z_0,z_1)\bigr).
\tag{E.4}
\]
The relation \((z,\xi)a=(za,a^{-1}\xi)\) preserves the product \(\xi z\), proving it is well defined. In the two vector charts it is the identity on \(\xi\), so it is a smooth linear isomorphism. Its first Chern number, with the complex orientation of this base, is \(-1\); a complete curvature computation and integration proof is [DG-CHAR-17, Exercise V.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-17.md). That earlier programme computation uses the same local spanning vector \((1,w)\), hence the same tautological bundle. □

## F. Exercises with complete solutions

**Exercise F.1 (two choices of origin).** Given two global sections \(s,t\) of a principal bundle, determine the unique \(h:M\to G\) with \(t=sh\), and the coordinate change between their product trivializations.

**Solution.** A.2 gives \(h(x)=\delta(s(x),t(x))\), smooth and unique. If a point has coordinates \(a\) using \(s\) and \(b\) using \(t\), then \(s(x)a=t(x)b=s(x)h(x)b\). Freeness implies \(a=hb\), so \(b=h^{-1}a\). Conversely these formulas reconstruct the same point, proving both directions of the coordinate change. □

**Exercise F.2 (adjoint-valued functions).** Describe a section of \(\operatorname{ad}(P)\) by a function on \(P\), by its functions in local sections, and by its fibrewise bracket with another section.

**Solution.** C.3 supplies the representation and bracket, and B.2 gives exactly the functions \(u:P\to\mathfrak g\) with \(u(pa)=\operatorname{Ad}(a^{-1})u(p)\). Put \(u_i(x)=u(s_i(x))\). From \(s_j=s_i g_{ij}\) follows \(u_j=\operatorname{Ad}(g_{ij}^{-1})u_i\), or equivalently \(u_i=\operatorname{Ad}(g_{ij})u_j\). Conversely such functions define \(u(s_i(x)a)=\operatorname{Ad}(a^{-1})u_i(x)\), and the transition equation proves agreement between charts. For a second such function \(v\), (C.4) gives
\[
[u(pa),v(pa)]
=\operatorname{Ad}(a^{-1})[u(p),v(p)].
\]
Thus the bracket function is equivariant and corresponds to the smooth fibrewise bracket of the sections. Jacobi and bilinearity hold in every fibre by C.3. □

**Exercise F.3 (a varying metric with a global orthonormal frame).** In the coordinate tangent frame on \(\mathbb R^2\), take the metric matrix
\[
Q(x)=
\begin{pmatrix}e^{2x_1}&0\\0&e^{-2x_1}\end{pmatrix}.
\]
Find its full orthonormal-frame reduction and describe its embedding in the coordinate frame bundle.

**Solution.** The scalar exponential is positive and smooth, and \(e^{t}e^{-t}=1\), by Local tools 0.5. The frame
\[
u_1=e^{-x_1}\partial_{x_1},\qquad
u_2=e^{x_1}\partial_{x_2}
\]
has squared norms \(e^{-2x_1}e^{2x_1}=1\) and \(e^{2x_1}e^{-2x_1}=1\), and inner product zero. In the coordinate frame write \(D(x)=\operatorname{diag}(e^{-x_1},e^{x_1})\). Then \(D^{\mathsf T}QD=I\). A general frame matrix \(B\) is orthonormal precisely when \(B^{\mathsf T}QB=I\). Writing \(B=DA\), which is possible and unique since \(D\) is invertible, transforms this equation to \(A^{\mathsf T}A=I\). Hence the entire reduction is
\[
(x,A)\longmapsto(x,D(x)A),\qquad
\mathbb R^2\times\mathrm O(2)\longrightarrow
\mathbb R^2\times\mathrm{GL}(2,\mathbb R).
\]
Its inverse onto its image is \((x,B)\mapsto(x,D(x)^{-1}B)\), smooth and equivariant. D.2 proves it is the metric reduction. It is a trivial principal bundle, but the matrices \(D(x)\mathrm O(2)\) describing its fibre inside the coordinate frame bundle vary with \(x_1\). □

**Exercise F.4 (combine orientation and metric).** Prove that a rank-\(r\) vector bundle admits a reduction to \(\mathrm{GL}^+(r)\) exactly when it is orientable. For a specified metric and orientation, identify the reduction that preserves both.

**Solution.** If a smooth orientation is specified, the positive frames form a \(\mathrm{GL}^+(r)\)-reduction by D.3. Conversely local sections of such a reduction choose positive bases with positive-determinant changes, which is exactly a consistent smooth orientation; the proof and both inverse identities are in D.3. For the specified metric, take its orthonormal frames from D.2 and intersect with the positive frames. D.3 verifies, using the explicit triangular change in Gram–Schmidt, that this intersection has local smooth sections, is embedded, and has fibre \(\mathrm{SO}(r)\). It is therefore the required reduction. Conversely an \(\mathrm{SO}(r)\)-reduction reconstructs both structures by declaring its frames orthonormal and positive; D.2–D.3 prove that its entire fibre, not merely its chosen sections, is recovered. Rank zero uses the canonical orientation and the trivial group, as in D.3. □

## Free construction source

Peter W. Michor, [*Topics in Differential Geometry*, freely accessible author draft](https://www.mat.univie.ac.at/~michor/dgbook.pdf), Sections 3.4, 4.11, 4.13 and 4.24 for the bracket and adjoint action; 8.3, 8.5 and 8.8 for gluing and vector constructions; 18.1–18.2, 18.7–18.9, 18.11–18.12 and 18.14 for principal bundles, associated bundles, frames, sections and reductions. The proofs above include the topology, smoothness and algebra needed for these constructions. The closed-subgroup theorem, a general quotient theorem for free actions, and classification theorems are not prerequisites. The Hopf coordinates are computed directly, and the stated Chern number is proved in the linked earlier programme lesson.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. The human construction source is credited above. No source prose, diagrams or PDFs are reproduced; earlier programme lessons retain their own source credits and licences.
