# Tensor and Hom types at independent covectors

External products put two independent directional problems on one product manifold. Their types tensor and their normalized shifts add. External internal Hom reverses the first covector, takes derived module Hom of the coefficient types, and subtracts the first shift from the second. We prove both assertions, including the first-factor orientation degree and the case of coefficient modules of infinite rank.

Use [How simple-sheaf shifts change along a Lagrangian](how-simple-sheaf-shifts-change-along-a-lagrangian.md#follow-a-transverse-auxiliary-plane) for transport along auxiliary planes. The [conormal coefficient model](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-supported--replacing-a-complex-by-one-on-a-submanifold) and the [normalized conormal type formula](../../microlocal-composition-and-pure-sheaves/src/pure-and-simple-sheaves-from-directional-tests.md#type-purity-and-simplicity) supply the local representatives and their ordinary degrees. Let \(k\) be a commutative ring of finite global dimension and \(X_i\) finite-dimensional real smooth manifolds. The input sheaves and their coefficient complexes are arbitrary bounded objects. The proofs below use the [derived tensor–Hom adjunction](../../sheaf-proof-readings/src/SH02/open-prerequisite-proofs.md#sh02-prp-df-c--currying-and-the-derived-closed-structure), the [exceptional-operation identities](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-diagonal--diagonals-and-product-tests), and [duality and cohomological dimension on manifolds](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-homological-dimension--bounds-for-derived-hom). The constant-coefficient and closed-support comparisons needed here are given explicitly below.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## The two product statements

Suppose \(F_i\in D^b(k_{X_i})\) has microsupport contained near \(p_i\) in a smooth conic Lagrangian \(\Lambda_i\), and has type \(L_i\in D^b(k)\) with allowed shift \(d_i\) there. Let \(q_i:X_1\times X_2\to X_i\) be projection and write \(a\) for the cotangent-fibre antipode. Then

\[
F_1\boxtimes^L F_2
\text{ has type }L_1\otimes_k^L L_2
\text{ with shift }d_1+d_2
\text{ at }(p_1,p_2)\text{ along }\Lambda_1\times\Lambda_2,
\qquad\text{(1)}
\]

and

\[
R\mathcal Hom(q_1^{-1}F_1,q_2^{-1}F_2)
\text{ has type }R\operatorname{Hom}_k(L_1,L_2)
\text{ with shift }d_2-d_1
\text{ at }(p_1^a,p_2)\text{ along }\Lambda_1^a\times\Lambda_2.
\qquad\text{(2)}
\]

These are local statements near the specified covectors, including zero covectors. The bounds proved below place both outputs and both coefficient types in the bounded derived category. No finite-rank coefficient hypothesis is added.

The [external tensor estimate](../../sheaf-proof-readings/src/SH03/limiting-covectors-at-open-boundaries.md#a-fixed-cut-can-test-several-directions-external-product-microsupport), (Q5)–(Q9), and [external Hom estimate](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-external-hom--reversing-the-second-direction), (MO6)–(MO7), give, in the displayed argument order,

\[
\begin{split}
\operatorname{SS}(F_1\boxtimes^LF_2)
&\subset\operatorname{SS}(F_1)\times\operatorname{SS}(F_2),\\
\operatorname{SS}\bigl(R\mathcal Hom(q_1^{-1}F_1,q_2^{-1}F_2)\bigr)
&\subset\operatorname{SS}(F_1)^a\times\operatorname{SS}(F_2).
\end{split}
\qquad\text{(3)}
\]

For the Hom estimate the first input is the contravariant one: use the external Hom theorem with the factors interchanged and then permute the product factors. This places the antipode on the first covector. If an excluded covector is zero, the zero-section support property makes the corresponding factor vanish on a base neighborhood; both external operations then vanish on the relevant product neighborhood. Thus the estimates also include zero covector components.

They also let us replace each factor by an isomorphic point-localized representative. For example a replacement cone in the first factor avoids \(p_1\); the tensor cone avoids \((p_1,p_2)\) by the first bound, and the contravariant Hom cone avoids \((p_1^a,p_2)\) by the second. The exact triangles give the corresponding denominator arrows. This justifies the conormal computations that follow.

## Why both outputs remain bounded

Put \(g=\operatorname{gldim}k\). For coefficient complexes \(A\in D^{[a,b]}(k)\) and \(B\in D^{[c,d]}(k)\),

\[
R\operatorname{Hom}_k(A,B)\in D^{[c-b,\,d-a+g]}(k).
\tag{H1}
\]

Indeed, every module has a projective resolution of length at most \(g\), with no restriction on the cardinalities of its terms. Hence \(\operatorname{Ext}^e_k(M,N)=0\) unless \(0\le e\le g\). The finite cohomology truncation triangles of \(A\) and \(B\) reduce the assertion to the pairs \(H^i(A)[-i]\), \(H^j(B)[-j]\). Their derived Hom is \(R\operatorname{Hom}_k(H^i(A),H^j(B))[i-j]\), whose possible degrees are \(j-i+e\). They lie in the interval in (H1). The long exact cohomology sequences preserve that interval when the finitely many pieces are assembled. In particular, (H1) concerns the full derived module Hom, including infinite modules.

For sheaves on an \(n\)-manifold the corresponding sufficient bound is

\[
E\in D^{[a,b]}(k_X),\quad F\in D^{[c,d]}(k_X)
\quad\Longrightarrow\quad
R\mathcal Hom(E,F)\in D^{[c-b,\,d-a+3n+g+1]}(k_X).
\tag{H2}
\]

The [manifold Hom theorem](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-homological-dimension--bounds-for-derived-hom), (M38)–(M44), proves this for arbitrary sheaves. Here is its argument with the two kinds of Hom distinguished. It uses the dimension theorem in the same lesson and the [exceptional-operation rectangle and diagonal identities](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-diagonal--diagonals-and-product-tests), (EX.27)–(EX.28). Those identities are proved for a bounded first Hom input and a bounded-below second input, so they can be used before an upper bound for sheaf Hom has been established.

First let \(E,F\) be sheaves in degree zero and work in an \(n\)-dimensional coordinate neighborhood \(W\). This neighborhood and all its open subsets are countable at infinity. Write \(q_1,q_2:W\times W\to W\), and set

\[
K=R\mathcal Hom(q_2^{-1}E,q_1^!F).
\]

The submersion formula \(q_1^!F\simeq q_1^{-1}F\otimes\operatorname{or}_{q_1}[n]\) puts its target in degree \(-n\). The usual bounded-below injective construction therefore gives \(K\in D^{\ge -n}\); it does not yet give an upper bound. For each open rectangle \(U\times V\subset W\times W\), the rectangle identity gives

\[
R\Gamma(U\times V;K)
\simeq R\operatorname{Hom}_k
  \bigl(R\Gamma_c(V;E),R\Gamma(U;F)\bigr).
\tag{H3}
\]

Both coefficient complexes on the right have cohomology in \([0,n]\), by the ordinary and compact-support dimension bounds. Formula (H1) consequently makes (H3) vanish above \(n+g\). Rectangles form a neighborhood basis. For a bounded-below complex, the filtered colimit of its degree-\(r\) derived sections over neighborhoods is its degree-\(r\) cohomology stalk: use a bounded-below injective representative and exactness of filtered colimits of modules. Thus \(\mathcal H^r(K)=0\) for \(r>n+g\).

Let \(\delta:W\hookrightarrow W\times W\) be the closed diagonal. The diagonal identity gives \(\delta^!K\simeq R\mathcal Hom(E,F)\), and therefore

\[
\operatorname{Ext}_{k_W}^r(E,F)
\simeq H_\Delta^r(W\times W;K).
\tag{H4}
\]

These are sections **supported on the diagonal**. Ordinary cohomology of any sheaf on the \(2n\)-manifold \(W\times W\), and on its open complement of \(\Delta\), vanishes above \(2n\). The closed-support localization sequence therefore bounds the supported degree by \(2n+1\). Applying this bound to the finitely many cohomology sheaves of \(K\), which vanish above \(n+g\), makes (H4) zero above \(3n+g+1\). Repeating on smaller coordinate neighborhoods and sheafifying the local Ext groups gives the same upper bound for internal Ext. The lower bound is zero for sheaf inputs. Finally the finite cohomology truncation triangles of \(E,F\) give (H2), just as for (H1). This also explains why the finite dimension bound is uniform. No constructibility, finite generation or orientation choice enters the proof.

For the external Hom in (2), take \(n=\dim X_1+\dim X_2\). Exact inverse image preserves the two input cohomology intervals, and (H2) supplies the required bounded sheaf object on the product. Formula (H1) separately bounds its claimed coefficient type. Existence of a bounded-below injective Hom model alone would prove neither of these upper bounds.

The same truncation argument also gives

\[
A\otimes_k^L B\in D^{[a+c-g,\,b+d]}(k).
\tag{T1}
\]

For modules, a projective resolution of length at most \(g\) makes the possible tensor degrees \(-g,\ldots,0\). The pieces \(H^i(A)[-i]\) and \(H^j(B)[-j]\) therefore contribute only in degrees \(i+j-e\), where \(0\le e\le g\); finite truncation triangles give the displayed interval. Derived tensor commutes with stalks, since stalks are exact and take flat sheaves to flat modules. The same uniform interval consequently bounds the external sheaf tensor after applying the exact inverse images \(q_i^{-1}\).

## Tensor at a conormal chart

First suppose \(\Lambda_i=T_{M_i}^*X_i\) near the points, with \(c_i=\operatorname{codim}M_i\). Replace the inputs by their conormal coefficient models using (3). Equalities involving the original inputs in (4)–(6) are interpreted in the appropriate point-localized categories. The subsequent tensor and support calculations are ordinary sheaf computations for those chosen models. The coefficient-object model and its normalized type formula give

\[
F_i\simeq (L_i)_{M_i}[s_i],
\qquad s_i=d_i-c_i/2\in\mathbb Z.
\qquad\text{(4)}
\]

Tensoring the two supported constant complexes on the product gives

\[
F_1\boxtimes^LF_2
\simeq (L_1\otimes_k^L L_2)_{M_1\times M_2}[s_1+s_2].
\qquad\text{(5)}
\]

For a closed embedding \(i:S\hookrightarrow Y\), write \(C_S=i_*i^{-1}C_Y\) for the constant coefficient complex \(C\) supported on \(S\). More generally, for \(E\in D^b(k_Y)\), the canonical projection map gives

\[
E\otimes_k^L k_S\xrightarrow{\sim}i_*i^{-1}E.
\]

Indeed \(k_S\) has stalk \(k\) on \(S\) and zero off \(S\), so it is flat. On \(S\) the displayed map is the identity of \(E_y\); off \(S\) both stalks are zero. Closed extension is exact, so this stalk calculation proves the derived assertion. It does not identify ordinary restriction with exceptional restriction.

Inverse image preserves this tensor calculation. It is exact, its stalk at \(x\) is the original stalk at \(f(x)\), and it preserves flat sheaves. Applying it to flat models therefore gives the natural isomorphism

\[
f^{-1}(E\otimes_k^L G)
\simeq f^{-1}E\otimes_k^L f^{-1}G.
\]

The same stalk comparison identifies the pullback of a closed-support constant with the constant on its inverse-image support. Put \(Y=X_1\times X_2\), \(S=M_1\times X_2\), \(T=X_1\times M_2\), and \(M=S\cap T\). Restriction followed by multiplication gives \(k_S\otimes k_T\to k_M\). It is the identity of \(k\) on the intersection and zero elsewhere, hence an isomorphism. Thus, for arbitrary bounded coefficient complexes,

\[
\begin{aligned}
q_1^{-1}(L_1)_{M_1}\otimes_k^L q_2^{-1}(L_2)_{M_2}
&\simeq (L_1)_Y\otimes_k^L(L_2)_Y\otimes k_S\otimes k_T\\
&\simeq (L_1\otimes_k^L L_2)_M.
\end{aligned}
\]

The supported geometric factors are flat; the coefficient tensor retains every Tor degree. Restoring the two shifts proves (5).

The output submanifold has codimension \(c_1+c_2\), so its normalized shift is
\(s_1+s_2+(c_1+c_2)/2=d_1+d_2\).
This proves (1) on a conormal chart.

## Hom at the same chart retains a relative orientation

Let \(M=M_1\times M_2\) and write
\(\mathcal O_1=q_1^{-1}\operatorname{or}_{M_1/X_1}|_M\)
for the pulled-back, unshifted relative orientation line. On the same chart the actual Hom calculation is

\[
R\mathcal Hom(q_1^{-1}F_1,q_2^{-1}F_2)
\simeq i_{M*}\Bigl(
R\operatorname{Hom}_k(L_1,L_2)_M\otimes\mathcal O_1
\Bigr)[s_2-s_1-c_1].
\qquad\text{(6)}
\]

The orientation is a local rank-one line; in a coordinate chart it can be trivialized when naming the point's coefficient type. Formula (6) preserves it before that local choice.

**Proof.** Temporarily omit the shifts in (4). The tensor–Hom adjunction gives

\[
R\mathcal Hom\bigl((L_1)_{X_1\times X_2}\otimes
q_1^{-1}k_{M_1},q_2^{-1}(L_2)_{M_2}\bigr)
\simeq
R\mathcal Hom\bigl((L_1)_{X_1\times X_2},
R\mathcal Hom(q_1^{-1}k_{M_1},q_2^{-1}(L_2)_{M_2})\bigr).
\qquad\text{(7)}
\]

We compute the inner supported Hom and the outer coefficient Hom separately.

### Constant coefficients and the evaluation map

For a manifold \(M\) and arbitrary \(A,B\in D^b(k)\), there is a natural isomorphism

\[
R\operatorname{Hom}_k(A,B)_M
\xrightarrow{\sim} R\mathcal Hom(A_M,B_M).
\tag{H5}
\]

To define the map, put \(C=R\operatorname{Hom}_k(A,B)\), which is bounded by (H1). Apply the exact constant-sheaf functor to the coefficient evaluation \(C\otimes_k^L A\to B\), using its monoidal comparison, and curry the resulting map \(C_M\otimes^L A_M\to B_M\). This produces the displayed comparison without identifying a sheaf-Hom stalk with the Hom of two stalks.

For a contractible coordinate ball \(U\subset M\), constant-sheaf/global-section adjunction gives

\[
R\Gamma\bigl(U;R\mathcal Hom(A_U,B_U)\bigr)
\simeq R\operatorname{Hom}_k(A,R\Gamma(U;B_U)).
\qquad\text{(8)}
\]

This adjunction can be checked on resolutions. Choose a bounded representative of \(A\) and a bounded-below injective sheaf resolution \(I\) of \(B_U\). Constant inverse image is exact, so its right adjoint \(\Gamma(U;-)\) sends injective sheaves to injective modules. For an injective sheaf \(J\), the sheaf \(\mathcal Hom(A_U^i,J)\) is flabby: a map on a smaller open extends by injectivity from the open extension of its source into the source on the larger open. Each degree of \(\mathcal Hom^\bullet(A_U,I)\) is a finite product of such sheaves. This bounded-below complex therefore computes its derived sections termwise. The ordinary constant-sheaf adjunction identifies its section complex with \(\operatorname{Hom}_k^\bullet(A,\Gamma(U;I))\), which computes the right side of (8). This uses no finite-rank hypothesis.

The [constant-section computation on a coordinate ball](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-euclidean--the-compact-support-generator), (M5), identifies the actual units \(B\to R\Gamma(U;B_U)\) and \(C\to R\Gamma(U;C_U)\) as isomorphisms. Under (8), the map induced by (H5), precomposed with the latter unit, is exactly \(R\operatorname{Hom}_k(A,-)\) applied to the former unit: this follows by evaluating the defining curried map. It is therefore an isomorphism. These identifications commute with restriction to smaller balls because the units and evaluation do. Passing to cohomology stalks over this basis proves (H5).

This argument never moves Hom from an infinite module through a filtered colimit: the comparison is already an isomorphism on derived sections over each ball. For the orientation line \(\mathcal O_1\) in (6), apply (H5) on its local trivializations. Changing a trivialization multiplies both sides by the same orientation transition function, by naturality in \(B\). The local comparisons thus glue to

\[
R\mathcal Hom(A_M,B_M\otimes\mathcal O_1)
\simeq R\operatorname{Hom}_k(A,B)_M\otimes\mathcal O_1.
\tag{H7}
\]

### The normal orientation in the support calculation

Continue with \(Y,S,T,M\) as above and write \(j:T\hookrightarrow Y\) and \(h:M\hookrightarrow T\). For every bounded constant coefficient complex \(C\) on \(T\),

\[
R\Gamma_M^T(C_T)
\simeq h_*(C_M\otimes\operatorname{or}_{M/T})[-c_1].
\tag{G1}
\]

To see the coefficient content of this formula, choose a product chart \(U\times V\subset T\) in which \(M\) is \(U\times\{0\}\), \(U\) is a ball in \(M\), and \(V\) is a normal ball of dimension \(c_1\). Sections with support in \(U\times\{0\}\) are the fibre of restriction from \(U\times V\) to \(U\times(V\setminus\{0\})\). Contracting the \(U\)-coordinate supplies a homotopy of this pair over \(V\), so its relative constant-coefficient cohomology is the local cohomology of \(C_V\) at zero. The [proper-interval homotopy](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#homotopy-invariance-from-a-proper-interval-proper-interval-homotopy), [point-to-compact comparison](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-actual-point-to-compact-comparison-point-to-compact-comparison) and [constant-coefficient relative-ball calculation](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#constant-coefficients-on-relative-balls-constant-relative-balls), (O1)–(O4) and (O11), compute the actual coefficient map as

\[
C\otimes_k H^{c_1}_{\{0\}}(V;k)[-c_1]
\xrightarrow{\sim}R\Gamma_{\{0\}}(V;C_V).
\tag{G2}
\]

Those formulas are proved for arbitrary bounded \(C\). They use the endpoint difference on an interval, compact-support integration in ordered normal coordinates, and excision; they do not require a finite-rank Künneth formula. The normal local-cohomology group is a free rank-one module, and a normal coordinate change acts on it by its local degree. The [orientation transition calculation](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#coordinate-changes-and-their-signs-orientation-coordinate-signs) identifies that degree with the sign of the normal determinant. Hence these normal lines glue as \(\operatorname{or}_{M/T}\).

For clarity, the global morphism checked by this calculation is the coefficient multiplication comparison
\(C_M\otimes h^!k_T\to h^!C_T\).
The [closed-embedding orientation formula](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-closed--the-closed-embedding-comparison) identifies \(h^!k_T\) with \(\operatorname{or}_{M/T}[-c_1]\). On the product chart its stalk comparison is precisely (G2), including its coefficient-first tensor order. It is an isomorphism at every point. Closed extension then proves (G1), with no assertion about this tensor comparison for a nonconstant sheaf on \(T\).

Closed support is compatible with closed extension in this square:

\[
R\mathcal Hom_Y(k_S,j_*C_T)
=R\Gamma_S^Y(j_*C_T)
\simeq j_*R\Gamma_M^T(C_T).
\tag{G3}
\]

One can derive the last isomorphism directly from the localization triangle. On an open \(W\subset Y\), the restriction map defining its left side is the restriction from \(W\cap T\) to \((W\setminus S)\cap T\); these are exactly the two opens defining support in \(M\) on \(T\). The equality of these maps persists on injective resolutions: \(j_*\) preserves injectives because it is right adjoint to exact \(j^{-1}\), and it is exact for a closed embedding. Thus (G3) identifies the actual support morphisms, rather than using an inverse-image comparison for arbitrary internal Hom.

The normal bundle of \(M=M_1\times M_2\) in \(T=X_1\times M_2\) is the pullback of the normal bundle of \(M_1\) in \(X_1\). Consequently \(\operatorname{or}_{M/T}=\mathcal O_1\). Taking \(C=L_2\) in (G1)–(G3) gives exactly

\[
R\mathcal Hom_Y(q_1^{-1}k_{M_1},q_2^{-1}(L_2)_{M_2})
\simeq i_{M*}\bigl((L_2)_M\otimes\mathcal O_1\bigr)[-c_1].
\tag{G4}
\]

Finally, ordinary closed-embedding adjunction and the tensor projection map give

\[
R\mathcal Hom_Y(A_Y,i_{M*}E)
\simeq i_{M*}R\mathcal Hom_M(A_M,E).
\tag{G5}
\]

For example, test against any complex \(P\) on \(Y\). The successive adjunctions identify both sides' morphisms from \(P\) with
\(\operatorname{Hom}_{D(k_M)}(i_M^{-1}P\otimes^L A_M,E)\).
This proves the isomorphism and its naturality without a finite-rank assumption. Apply (G5) to (G4) inside (7), then use the constant-coefficient Hom comparison with the rank-one line \(\mathcal O_1\). Restoring the shift \(s_2-s_1\) yields

\[
R\mathcal Hom(q_1^{-1}F_1,q_2^{-1}F_2)
\simeq i_{M*}\bigl(R\operatorname{Hom}_k(L_1,L_2)_M\otimes\mathcal O_1\bigr)
[s_2-s_1-c_1],
\]

which is (6). The local orientation line stays in the sheaf formula, while a choice of normal orientation identifies the point's coefficient object with \(R\operatorname{Hom}_k(L_1,L_2)\). Codimension zero gives the identity support operation and shift zero throughout. All arguments preserve arbitrary bounded coefficients, including modules of infinite rank.

At the product conormal, formula (6) has normalized shift

\[
s_2-s_1-c_1+\frac12(c_1+c_2)
=d_2-d_1.
\qquad\text{(9)}
\]

The first covector is antipodal by (3). In a full conormal fibre the antipode preserves the set, which can hide this sign if one checks only supporting submanifolds. It is visible for a general Lagrangian branch.

## Move from regular projection points to every point

We now prove (1)–(2) on general smooth conic \(\Lambda_i\). Points where the base projection has locally constant rank form an open dense subset. To see density, choose in any nonempty coordinate patch the largest integer rank attained there. A nonzero minor at a point of that rank stays nonzero on a smaller neighborhood, while maximality in the patch prevents a larger rank. The rank is therefore constant there. Rank zero causes no exception: if that is the maximum, every derivative in the patch is zero.

Here is the actual conormal geometry at a nonzero point of constant rank \(r\), as in [constant-rank conormal recognition, Theorem 5.1](../../AN-04/reconstructions/20261005-restored-prescribed-coordinates/prescribed-canonical-coordinates-and-isotropic-fibers.md#5-recognize-conormal-germs-where-the-base-projection-has-constant-rank). Write \(n=\dim X\). Use an invertible \(r\)-by-\(r\) minor of the projection to take its first \(r\) output coordinates and the remaining domain coordinates as coordinates \((u,v)\) on \(\Lambda\). The inverse function theorem gives

\[
\pi(u,v)=(u,h(u,v)).
\]

Since the first derivative block is \((I,0)\), constant rank \(r\) forces \(\partial_v h=0\). On a small coordinate product, integration along a segment in the \(v\)-variables gives \(h(u,v)=h(u,v_0)\). The image is therefore the embedded base germ \(M=\{(u,h(u,v_0))\}\), and \(d\pi(T\Lambda)=TM\). For \(r=0\), the same segment argument makes \(\pi\) constant and \(M\) is a point.

The fibre-radial vector \(R\) is tangent to \(\Lambda\) by conicity. Since \(\omega=d\theta\) and \(\iota_R\omega=\theta\), isotropy gives \(\theta|_{T\Lambda}=0\). For \((x,\xi)\in\Lambda\) and \(v\in T_xM\), choose \(w\in T_{(x,\xi)}\Lambda\) with \(d\pi(w)=v\); then \(\xi(v)=\theta(w)=0\). Thus \(\Lambda\subset T_M^*X\) locally. Both embedded manifolds have dimension \(n\); the inclusion has an invertible derivative and is an open embedding after shrinking. This proves equality of germs near the selected covector. It asserts no equality with all conormal directions or with a global conormal bundle. At a nonzero point \(R\ne0\) lies in the projection kernel, so \(r<n\).

At a zero covector use the [smooth-conic zero-covector proof](../../microlocal-composition-and-pure-sheaves/src/pure-and-simple-sheaves-from-directional-tests.md#a-smooth-conic-lagrangian-at-the-zero-covector-is-conormal). To recall its essential step, dilation invariance splits the tangent Lagrangian as \(P\oplus P^\perp\). In adapted coordinates, projection to tangential base coordinates \(a\) and normal covectors \(\beta\) is invertible, so the germ is \(b=g(a,\beta)\), \(\alpha=h(a,\beta)\). Dilation gives \(g(a,t\beta)=g(a,\beta)\) and \(h(a,t\beta)=t h(a,\beta)\). Smoothness at \(\beta=0\) makes \(g=g_0(a)\) and \(h\) linear in \(\beta\); the vanishing tautological form gives \(h=-dg_0(a)^T\beta\). These are exactly the conormal equations of \(b=g_0(a)\), including zero covectors. Thus this case also supplies the conormal chart needed for (4)–(9).

Take a small connected coordinate neighborhood \(P_i\subset\Lambda_i\) of each chosen \(p_i\). The [real common-complement construction](how-simple-sheaf-shifts-change-along-a-lagrangian.md#a-common-complement-over-the-reals) gives at \(p_i\) a Lagrangian plane transverse to both \(V_i\) and \(A_i=T\Lambda_i\), in every possible intersection dimension. Extend that plane as a constant Lagrangian plane in a local symplectic frame. After shrinking \(P_i\), openness of transversality gives a continuous family \(\mu_i\) transverse to both varying planes. The rank of their intersection need not be locally constant. Define

\[
d_i(q)=d_i+\frac12\bigl[
\tau(V_i(q),A_i(q),\mu_i(q))
-\tau(V_i(p_i),A_i(p_i),\mu_i(p_i))
\bigr].
\qquad\text{(10)}
\]

These shifts have the required parity even where the projection rank jumps. Put \(n_i=\dim X_i\) and \(r_i(q)=\dim(V_i(q)\cap A_i(q))\). Since the other two pairwise intersections with \(\mu_i\) vanish, the [degenerate ordered-index parity formula](normal-forms-and-the-shift-of-a-submanifold-transform.md#the-ordered-index-degeneracy-parity-and-the-cocycle) gives

\[
\tau(V_i(q),A_i(q),\mu_i(q))\equiv n_i+r_i(q)\pmod2.
\]

Subtract the same congruence at \(p_i\) and use \(d_i-r_i(p_i)/2\in\mathbb Z\). Formula (10) then gives \(d_i(q)-r_i(q)/2\in\mathbb Z\), as required. It also makes \(d_i(q)-\tau(V_i(q),A_i(q),\mu_i(q))/2\) constant. The [continuous-family type theorem](how-simple-sheaf-shifts-change-along-a-lagrangian.md#follow-a-transverse-auxiliary-plane) consequently gives type \(L_i\) with shift \(d_i(q)\) throughout the connected \(P_i\). This uses local constancy of type; it does not require the half-integer-valued shifts in (10) themselves to be continuous.

For the tensor output, use \(\mu_1\oplus\mu_2\). Its inertia is the sum of the two input inertias, because the product symplectic space is the direct sum. Hence
\(d_1(q_1)+d_2(q_2)-\tau_{\mathrm{product}}/2\)
is constant on \(P_1\times P_2\). Its allowed parity follows by adding the two input parity conditions: the product vertical intersection has dimension \(r_1+r_2\). The output is bounded by (T1), and (3) contains its microsupport in the smooth product Lagrangian on this chart. The continuous-family theorem therefore makes its type constant there. Each \(P_i\) contains a regular projection point by the density just proved. At one such pair, the conormal calculation (5) gives type \(L_1\otimes^LL_2\). Constancy gives this same type at the selected pair, where (10) recovers the original shifts \(d_i\). This proves (1). No limit of coefficient complexes at regular points is taken.

For Hom, let \(\bar a(q_1,q_2)=(q_1^a,q_2)\) act on the two cotangent factors. Its first tangent map reverses the first symplectic form. Thus the auxiliary plane \(a_*\mu_1\oplus\mu_2\) is transverse to the product vertical and \(T(\Lambda_1^a\times\Lambda_2)\), with index

\[
\tau_{\mathrm{Hom}}=-\tau(V_1,A_1,\mu_1)
+\tau(V_2,A_2,\mu_2).
\qquad\text{(11)}
\]

The corrected candidate shift \(d_2(q_2)-d_1(q_1)-\tau_{\mathrm{Hom}}/2\) is constant. Its allowed parity is again \((r_1+r_2)/2\): the difference between \((r_2-r_1)/2\) and \((r_1+r_2)/2\) is the integer \(-r_1\). The output is bounded by the arbitrary-input internal-Hom estimate (H2), and (3) gives the required microsupport containment. Its type is therefore constant on the antipodal product chart. At a regular pair (6)–(9) compute it as \(R\operatorname{Hom}_k(L_1,L_2)\), with the local orientation choice specified there. This gives (2) at the original antipodal pair. The proof covers zero covectors and does not require globally orientable manifolds. \(\square\)

## Pure inputs can have several product degrees

If both inputs are simple, their types are locally \(k\). The two derived coefficient operations give \(k\) again, so the external tensor and external Hom are simple with the shifts in (1)–(2). Local relative orientation lines in (6) remain part of the sheaf object.

Purity alone has a different outcome over general rings. For \(k=\mathbb Z\), resolving \(\mathbb Z/2\) by multiplication by two gives
\(\mathbb Z/2\otimes^L_\mathbb Z\mathbb Z/2\)
with nonzero cohomology in degrees \(-1\) and zero. Both inputs can be pure while their product fails to be pure at every shift. Likewise
\(R\operatorname{Hom}_\mathbb Z(\mathbb Z\oplus\mathbb Z/2,\mathbb Z)\)
has a \(\mathbb Z\) in degree zero and a \(\mathbb Z/2\) in degree one. An integer change of normalized shift translates those degrees together and does not combine them into a single degree.

## Exercises with complete solutions

### Codimensions and ordinary degrees

*Difficulty: Introductory.*

Let \(c_1=2,c_2=3\), and use models \((L_1)_{M_1}[1]\), \((L_2)_{M_2}[-2]\). Compute the input normalized shifts, the tensor shift and the Hom shift from both the model degrees and (1)–(2).

**Solution.** The input shifts are \(d_1=1+2/2=2\) and \(d_2=-2+3/2=-1/2\). Tensor has model degree \(-1\) and product codimension five, giving \(-1+5/2=3/2=d_1+d_2\). Hom has model degree \(-2-1-2=-5\), including the first-codimension orientation shift. Adding \(5/2\) gives \(-5/2=d_2-d_1\).

### Tor prevents purity

*Difficulty: Intermediate.*

On a point, regard two copies of \(\mathbb Z/2\) as pure complexes with normalized shift zero. Compute their derived tensor and determine whether a normalized shift can make it pure.

**Solution.** The free resolution \([\mathbb Z\xrightarrow{2}\mathbb Z]\) in degrees \(-1,0\) becomes \([\mathbb Z/2\xrightarrow{0}\mathbb Z/2]\) after tensor. Its two nonzero cohomology degrees remain two under every shift. Thus the derived tensor is not pure at any normalized shift. The theorem asserts its coefficient type and degree rule, rather than concentration of the derived tensor of two modules.

### Ext prevents purity too

*Difficulty: Intermediate.*

Compute the coefficient Hom type for \(L_1=\mathbb Z\oplus\mathbb Z/2\) and \(L_2=\mathbb Z\), and explain whether it can be pure.

**Solution.** The free summand contributes \(\mathbb Z\) in degree zero. The multiplication-by-two resolution of \(\mathbb Z/2\), after Hom into \(\mathbb Z\), has cokernel \(\mathbb Z/2\) in degree one and zero in degree zero. The total coefficient Hom therefore has the two specified nonzero degrees and is not pure under any integer shift.

### Infinite coefficients need actual Hom

*Difficulty: Advanced.*

Over a field take \(A=\bigoplus_{j\geq1}k\) and \(B=\bigoplus_{j\geq1}k\). Show that the natural map \(A^*\otimes B\to\operatorname{Hom}_k(A,B)\) need not be surjective, and explain why (8) still applies.

**Solution.** An element of \(A^*\otimes B\) is a finite sum of elementary tensors, so its associated map has image in the finite-dimensional span of the finitely many chosen vectors of \(B\). The map sending the \(j\)-th basis vector of \(A\) to the \(j\)-th basis vector of \(B\) has infinite-dimensional image and is not in that range. Formula (8) uses constant-sheaf adjunction and an invertible coefficient unit on each contractible neighborhood. It computes the full module Hom without replacing it by \(A^*\otimes B\) or requiring finite-dimensional \(A\).

### The sign in auxiliary-plane transport

*Difficulty: Advanced.*

The first auxiliary inertia changes from one to three and the second from minus two to zero. Keeping each corrected input degree fixed, calculate the tensor and Hom shift changes. Compare with their auxiliary index changes.

**Solution.** Each input shift increases by \(2/2=1\). The tensor shift increases by two, and its index increases by \(2+2=4\), giving the same half-index correction. The Hom shift changes by \(1-1=0\), and its index change is \(-2+2=0\), because the first symplectic form is reversed. Using a sum for Hom would give the wrong correction.

## References

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Proposition 7.2.9, printed p. 129 (PDF p. 132), gives the tensor and external Hom rules for pure module types. Its tensor statement assumes finite weak global dimension and vanishing higher Tor; its Hom statement assumes vanishing higher Ext and a bounded first sheaf input. Its first covector is antipodal in the Hom formula. Definition 7.2.5 and Examples 7.2.6(i)–(ii), printed pp. 127–128, give the normalization in which a constant codimension-\(c\) submanifold has shift \(c/2\).

Here the types are bounded coefficient complexes over a ring of finite global dimension. The coefficient bounds, evaluation comparison and normal-orientation calculation prove the full derived formulas (1)–(2). The Tor and Ext examples show exactly why those formulas need not produce pure objects from pure inputs. The linked programme lessons prove the external microsupport estimates and auxiliary-plane transport; the conormal geometry and common-complement arguments above explain how the local coefficient computations reach every selected covector.
