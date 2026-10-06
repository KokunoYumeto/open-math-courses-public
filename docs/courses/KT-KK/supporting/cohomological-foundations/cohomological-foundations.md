# Cohomological foundations for the complex Thom comparison

*Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The comparison in Lesson 13 uses the even character of relative bundle classes, its products and its line normalization, injectivity of a splitting pullback, and the ordinary cohomological Thom class. The proofs below supply those results. The ordinary Thom theorem retains every Hausdorff base, including noncompact and non-CW bases, integral orientations with arbitrary abelian coefficient groups, and the unoriented mod-two case. The character comparison retains finite CW bases and compact Hausdorff bases of finite CW homotopy type. None of these restrictions is imposed on the analytic KK Thom theorem.

The bundle constructions, finite embeddings, cylinder transport and the identification of relative bundle classes with operator \(K^0\) used below are proved in [Relative difference bundles, radial pairs and the planar normalization, RK.0–RK.7a](../relative-k-foundations/relative-k-foundations.html#rk-topology). All additional singular-cohomology results required for the comparison are proved here. The Chern character constructed below is a natural even character; a rational isomorphism theorem for the two full graded theories is not needed in this comparison.

<a id="cf-chains"></a>

## CF.0. Singular chains, exactness and products

For a space \(T\), let \(C_n(T)\) be the free abelian group on continuous maps from the ordered standard simplex \(\Delta^n\) to \(T\), zero for \(n<0\). Set
\[
\partial s=\sum_{i=0}^n(-1)^i s[0,\ldots,\widehat i,\ldots,n].
\]
Twice-deleted faces cancel in pairs, proving \(\partial^2=0\). For \(A\subset T\), the quotient \(C_*(T,A)=C_*(T)/C_*(A)\) is free on the simplices not contained in \(A\). With coefficients \(G\), homology uses \(C_*\otimes G\), and cohomology uses \(\operatorname{Hom}(C_*,G)\), with \(\delta f=f\partial\). These definitions fix the signs of all connecting maps.

**CF.0a (chain tools).** Homotopies of pairs induce identical maps; excision holds when the closure of the removed subset lies in the interior of the relative subspace; open two-set covers have absolute and relative Mayer–Vietoris sequences, with all coefficients.

**Proof.** A homotopy \(H:T\times I\to T'\) defines the prism operator by applying \(H(s(-),-)\) to the sum
\[
\sum_{i=0}^n(-1)^i
[(v_0,0),\ldots,(v_i,0),(v_i,1),\ldots,(v_n,1)].
\]
Internal faces cancel, and the remaining faces give
\(\partial P+P\partial=H_{1*}-H_{0*}\).
For a homotopy of pairs this descends to quotient complexes. Tensoring or dualizing proves the coefficient assertions.

Here is the small-chain argument, including the cohomological strength needed for gluing. Barycentric subdivision \(S\) is defined recursively in each affine simplex by coning the already subdivided boundary to its barycentre. The identity \(\partial(b*c)=c-b*(\partial c)\), in the augmented complex in degree zero, proves \(\partial S=S\partial\). Recursively fill the cycle \(s-Ss-T\partial s\) by a cone inside the original simplex to construct \(T\) with \(\partial T+T\partial=1-S\). Compose the affine chains with a singular simplex. Both operations keep their support inside that simplex. The vertices of a subdivided simplex are barycentres of nested faces; their distances are at most \(n/(n+1)\) times the previous diameter. Iteration therefore makes the mesh tend to zero. The inverse image of any open cover covers the compact Euclidean simplex. It has a Lebesgue number: otherwise sets of diameter tending to zero not contained in any cover member have points with a convergent subsequence, contradicting openness of a member containing the limit. Thus sufficiently subdivided finite chains are small.

For an open cover \(\mathcal U\), write \(C^{\mathcal U}\) for its small-chain subcomplex. We construct a retraction \(\rho:C\to C^{\mathcal U}\) and a homotopy \(D\) with
\[
\rho\iota=1,\qquad 1-\iota\rho=\partial D+D\partial.
\tag{CF.1}
\]
Proceed on simplex dimension. Suppose the construction is made on the faces of \(s\), and put \(z=s-D\partial s\); then \(\partial z=\rho\partial s\) is small. Put \(T_N=\sum_{k=0}^{N-1}S^kT\). Choose \(N\) making \(S^Nz\) small, and define
\[
\rho s=S^Nz+T_N(\rho\partial s),\qquad Ds=T_Nz.
\]
The identity \(\partial T_N+T_N\partial=1-S^N\) gives (CF.1) and \(\partial\rho s=\rho\partial s\). If \(s\) is small, choose \(N=0\), so \(Ds=0\) and \(\rho s=s\). Every term is in the image of \(s\); consequently the construction preserves every subspace, and descends to every relative complex. In particular these are chain homotopy equivalences, which remain equivalences after dualizing, not merely homology comparisons.

If \(Z\subset A\) and \(\overline Z\subset\operatorname{int}A\), use the cover \(\operatorname{int}A,T\setminus\overline Z\). Its small complex modulo \(C(A)\) is the relative complex for \(T\setminus\overline Z,A\setminus\overline Z\). The restricted cover of \(T\setminus Z\) has the same quotient: its chains in \((\operatorname{int}A)\setminus Z\) disappear. The two instances of (CF.1) prove excision, including cohomology with every \(G\).

The sequence of complexes for a pair is degreewise split on simplex bases. The open-cover sequence is also degreewise split:
\[
0\longrightarrow C_*(U\cap V)
\xrightarrow{c\mapsto(c,-c)} C_*(U)\oplus C_*(V)
\xrightarrow{(a,b)\mapsto a+b} C_*^{\{U,V\}}(T)
\longrightarrow0.
\tag{CF.2}
\]
Dividing by chains in a subspace gives the relative version, again split on the simplices outside that subspace. A split exact sequence stays exact on tensoring or dualizing. Its connecting map is obtained by lifting a cycle, taking its differential, and regarding that differential in the kernel complex. Independence follows because a different lift changes it by a boundary. Exactness follows from three corrections: a cycle whose projected class is zero can be corrected by a lifted boundary to lie in the kernel; a projected cycle with zero connecting class has a lift correctable to a cycle; and a kernel cycle bounding upstairs is the connecting image of the projected bounding chain. These corrections, applied to coboundaries, also prove cohomological exactness and naturality. This proves all the sequences asserted. \(\square\)

We use the following explicit five-term diagram argument. Write the exact rows as \(A_1\xrightarrow{d_1}A_2\xrightarrow{d_2}A_3\xrightarrow{d_3}A_4\xrightarrow{d_4}A_5\) and \(B_1\xrightarrow{e_1}B_2\xrightarrow{e_2}B_3\xrightarrow{e_3}B_4\xrightarrow{e_4}B_5\), with commuting vertical maps \(u_i:A_i\to B_i\) that are isomorphisms for \(i=1,2,4,5\). To prove injectivity of \(u_3\), take \(x\in A_3\) with \(u_3x=0\). Then \(u_4d_3x=e_3u_3x=0\), so injectivity of \(u_4\) gives \(d_3x=0\). Exactness gives \(x=d_2a\) for some \(a\in A_2\). Since \(e_2u_2a=u_3x=0\), write \(u_2a=e_1b\) with \(b\in B_1\). Lift \(b=u_1c\). Commutativity gives \(u_2(a-d_1c)=0\); injectivity of \(u_2\) gives \(a=d_1c\), and therefore \(x=d_2d_1c=0\).

For surjectivity, take \(y\in B_3\), and choose \(z\in A_4\) with \(u_4z=e_3y\). Then \(u_5d_4z=e_4u_4z=e_4e_3y=0\); injectivity of \(u_5\) gives \(d_4z=0\). Exactness gives \(z=d_3x\) for some \(x\in A_3\). Now \(e_3(y-u_3x)=0\), so write \(y-u_3x=e_2b\). Lift \(b=u_2a\), obtaining \(y=u_3(x+d_2a)\). Thus \(u_3\) is an isomorphism.

**CF.0b (cup and external products).** With a commutative ring \(R\), the cup product is natural, associative and graded commutative in cohomology. Absolute classes act on relative groups. For two open relative subspaces, relative products take values relative to their union. Product chains are naturally equivalent to tensor-product chains, including these relative versions.

**Proof.** Define
\[
(a\smile b)(s)=a(s[0,\ldots,p])\,b(s[p,\ldots,p+q]).
\]
Expanding faces, the two terms at the joining vertex cancel and the others give
\(\delta(a\smile b)=\delta a\smile b+(-1)^p a\smile\delta b\).
Naturality and associativity follow from the same face intervals in each expression; the constant zero-cochain one is the unit. If one factor vanishes on a subspace, the product does also. With \(a\) valued in an abelian group \(G\) and \(b\) integral, use integer multiplication in this formula.

On tensor chains use
\(\partial(c_p\otimes d_q)=\partial c_p\otimes d_q+(-1)^p c_p\otimes\partial d_q\).
The front/back map
\[
A(s)=\sum_{p+q=n}s_T[0,\ldots,p]\otimes s_W[p,\ldots,n],
\qquad s:\Delta^n\to T\times W,
\]
and the shuffle map \(B\) in the other direction are chain maps. Explicitly, \(B(c_p\otimes d_q)\) is the sum of the affine simplices in \(\Delta^p\times\Delta^q\) traced by all paths of \(p\) horizontal and \(q\) vertical unit steps, with the permutation sign relative to all horizontal steps first. Compose with \(c\times d\). Two paths exchanging adjacent unlike steps have their common interior face with opposite signs; exterior faces give the stated tensor differential. In \(A\), faces away from the split give tensor boundaries, and split faces telescope. These verify the chain-map assertions.

For completeness, the inverse homotopies have the following inductive construction. Chains in a convex simplex or a convex product have an augmented contraction \(K\) to a fixed vertex, obtained by joining that vertex to a singular simplex by straight lines; its boundary formula is \(\partial K+K\partial=1-i\epsilon\). The tensor product of two such contractions has contraction
\(K\otimes1+(i\epsilon)\otimes L\), with the tensor sign in the second term. Its boundary sum is \(1-(i\epsilon)\otimes(j\epsilon)\). On a universal simplex in \(\Delta^n\times\Delta^n\), after a homotopy is defined on its faces, the residual for \(1-BA\) is an augmented cycle. Fill it by the convex-product contraction, and push the filling forward by \(s_T\times s_W\). This induction proves \(1-BA=\partial h+h\partial\). On a universal tensor generator in \(C(\Delta^p)\otimes C(\Delta^q)\), fill the residual for \(1-AB\) by the tensor contraction, and push forward by \(c\otimes d\). Induction on \(p+q\) gives the other homotopy. The constructions commute with maps of spaces because the universal fillings are fixed before pushforward. If a factor lies in a subspace, so do all its fillings.

The same tensor contraction inductively compares \(A\) with \(A\) after exchanging the product factors and using the signed tensor exchange \(c_p\otimes d_q\mapsto(-1)^{pq}d_q\otimes c_p\). The maps agree on augmentation; at each dimension fill the residual cycle just as above. Evaluation on cocycles after the diagonal proves graded commutativity. This proves the claimed sign without imposing commutativity on cochains.

Modulo \(C(A)\otimes C(W)+C(T)\otimes C(B)\), these equivalences give the complex \(C(T,A)\otimes C(W,B)\) and the product complex modulo \(C(A\times W)+C(T\times B)\). When \(A,B\) are open, (CF.1) on their union identifies the latter with the relative complex for \(A\times W\cup T\times B\). If either is empty no smallness step is necessary. Evaluation of \(a\otimes b\) on \(A(s)\) gives \(a\times b=\operatorname{pr}_T^*a\smile\operatorname{pr}_W^*b\). Pulling back by the diagonal proves the analogous relative cup assertion. \(\square\)

**CF.0c (coefficients and finite free factors).** For a free integral chain complex \(K\) there is a natural exact sequence
\[
0\longrightarrow \operatorname{Ext}(H_{n-1}K,G)
\longrightarrow H^n(\operatorname{Hom}(K,G))
\longrightarrow \operatorname{Hom}(H_nK,G)\longrightarrow0.
\tag{CF.3}
\]
If \(K\) has free homology, it is chain homotopy equivalent to its homology with zero differential. In particular, if that homology has finitely many finite-rank free groups, tensoring with \(K\) and dualizing computes a finite direct sum of shifted groups, with no Künneth or inverse-limit assumption.

**Proof.** A subgroup \(J\) of a free group is free. Well-order a basis and filter by its initial segments. Each successive quotient of \(J\) embeds in the successive quotient \(\mathbb Z\); choose a lift of its least positive generator when nonzero. These lifts form a basis: remove the last nonzero coordinate of any finite-support element successively; the ordinal indices strictly decrease, so this process terminates. The same last-coordinate argument proves independence.

For a free presentation \(0\to J\to F\to M\to0\), define \(\operatorname{Ext}(M,G)\) as the cokernel of \(\operatorname{Hom}(F,G)\to\operatorname{Hom}(J,G)\). Maps of quotients lift by choosing images of a free basis. Two lifts differ by a map into the target kernel, which induces zero in that cokernel. Identity maps between presentations thus give inverse induced maps; this proves independence and functoriality.

Write \(Z_n=\ker\partial\), \(B_n=\operatorname{im}\partial\). The surjection \(K_n\to B_{n-1}\) splits, so \(K_n=Z_n\oplus L_n\). A functional on \(H_n=Z_n/B_n\) extends by zero on \(L_n\) to a cocycle, proving surjectivity in (CF.3). A cocycle evaluating to zero on homology vanishes on \(Z_n\) and factors through \(B_{n-1}\). It is a coboundary exactly when that functional extends to \(K_{n-1}\), equivalently to \(Z_{n-1}\). The resulting quotient is the Ext group for \(0\to B_{n-1}\to Z_{n-1}\to H_{n-1}\to0\). Evaluation and the preceding presentation comparison prove naturality. Over a field the same splitting argument gives \(H^n(K^\vee)=H_n(K)^\vee\), since a functional on a subspace extends by a basis.

When all \(H_n\) are free, split \(Z_n\to H_n\) as well. Then
\(K_n=B_n\oplus H_n\oplus L_n\), with \(\partial:L_n\to B_{n-1}\) an isomorphism. Projection to \(H\) and inclusion from it are inverse up to the homotopy carrying \(B_n\) to its inverse image in \(L_{n+1}\) and zero on the other summands. Tensoring this homotopy with another complex uses the usual tensor sign, and preserves a homotopy equivalence. If \(H\) is finite free in finitely many degrees, \(\operatorname{Hom}(C\otimes H,G)\) is a finite direct sum of the shifted complexes \(\operatorname{Hom}(C,G)\). This proves the final assertion. \(\square\)

<a id="cf-thom"></a>

## CF.1. The ordinary Thom theorem with the original base scope

**CF.1a (fibre orientations).** The pair \((\mathbb R^r,\mathbb R^r\setminus0)\) has free homology \(\mathbb Z\) in degree \(r\) and zero otherwise. Let \(u_r\) be the integral cohomology class evaluating to one on the product of the \(r\) positively directed real intervals, in the listed coordinate order. An invertible real linear map acts on it by the sign of its determinant.

**Proof.** The point complex has one generator in each degree, with differential alternating zero and identity; hence its homology is \(\mathbb Z\) in degree zero alone. The prism argument gives the same for a contractible space. In degree zero, path boundaries equate precisely the points in a path component, so \(H_0\) is free on those components. The pair sequence for the line and its two punctured half-lines gives \(\mathbb Z\) in degree one, represented by the interval from \(-1\) to \(1\), with boundary the positive endpoint minus the negative endpoint. CF.0c contracts its relative chain complex to that generator. Take the \(r\)-fold relative product from CF.0b: the exceptional union is exactly the punctured vector space. Tensoring gives \(\mathbb Z[r]\), with the indicated orientation.

A positive determinant matrix contracts to the identity inside \(GL^+(r,\mathbb R)\). Gram–Schmidt gives \(QR\), where \(R\) is upper triangular with positive diagonal; linear interpolation from \(R\) to \(1\) stays invertible. In \(SO(r)\), rotate its first unit vector to the first coordinate vector in their plane, using a half-turn in a coordinate plane for an antipodal vector, then repeat on the orthogonal complement. This constructs a path to \(1\), starting with \(SO(1)=\{1\}\). Reflection of the first axis exchanges the line endpoints and changes its relative generator by \(-1\); tensoring gives the same sign in every \(r\). Every negative determinant matrix is a reflection times a positive one. Homotopy invariance proves the assertion. Modulo two the sign disappears. \(\square\)

**Theorem CF.1b (ordinary Thom isomorphism).** Let \(E\to B\) be a real rank-\(r\) vector bundle over any Hausdorff base and \(E_0=E\setminus B\) its punctured total space. In the oriented integral case there is a unique \(U_E\in H^r(E,E_0;\mathbb Z)\) restricting to the positive generator on every fibre, and
\[
H^j(B;G)\xrightarrow{\ \cong\ }H^{j+r}(E,E_0;G),
\qquad a\longmapsto\pi^*a\smile U_E
\tag{CF.4}
\]
for every abelian group \(G\). Also \(H^i(E,E_0;G)=0\) for \(i<r\). Without an orientation, the same statements hold with the canonical fibre generator and \(\mathbf F_2\) coefficients. The cap map gives the corresponding homological Thom isomorphism. Rank zero gives \(U_E=1\) and the identity.

**Proof.** For an integral cocycle \(u\) of degree \(r\) define
\[
R_u(s)=u(s[m-r,\ldots,m])\,s[0,\ldots,m-r]\quad(m\geq r),
\]
zero in smaller degrees. Face expansion with \(\delta u=0\) gives \(\partial R_u=R_u\partial\). It descends from relative chains when \(u\) vanishes on the relative subspace. Moreover \(a(R_us)=(a\smile u)(s)\). If \(u\) changes by \(\delta v\), the map \(h_m=(-1)^{m-r+1}R_v\) satisfies \(\partial h+h\partial=R_{\delta v}\), again by face expansion. The cap map on homology consequently depends only on the class.

For a trivial bundle over any space \(V\), CF.0b and CF.1a identify its relative complex with \(C(V)\otimes\mathbb Z[r]\). The map \((1\otimes u_r)A\) is precisely \(\pi_*R_{u_r}\): its front face is projected to \(V\), and its last face is evaluated on the fibre cocycle. Thus it is a homology isomorphism. Dualizing proves (CF.4) with every \(G\) and its low-degree vanishing. In degree \(r\), the class is uniquely determined by its fibre values.

Suppose the assertions hold over open \(V,W,V\cap W\). The two degree-\(r\) classes agree on the intersection by their fibre restrictions and uniqueness. Relative Mayer–Vietoris glues them to one class over \(V\cup W\), uniquely because the preceding degree-\(r-1\) intersection group vanishes. Multiplication on the right by its cocycle maps the base Mayer–Vietoris sequence to the relative total-space sequence: restrictions commute, and the cup differential identity makes the connecting squares commute. The five-term argument proves (CF.4) in all degrees, and the same argument with \(G\) in the first factor proves the coefficient assertion. For homology, the cap map preserves the supports over \(V,W,V\cap W\), so it maps (CF.2) to the base sequence and commutes with its connecting maps. The five-term argument proves its isomorphism. A change of cocycle has the cap homotopy above. Induct on the number of trivializing sets: the intersection of the last set with the previous union is itself covered by fewer trivializing sets. This proves all assertions for every finite trivializing cover, without requiring the sets or their intersections to be contractible.

For the unrestricted Hausdorff base, every compact subset \(C\subset B\) has such a finite relative-open trivializing cover. Let \(U_C\) be its class. For \(C\subset C'\), uniqueness gives restriction \(U_{C'}|_C=U_C\), so the cap maps are compatible. Every finite singular chain and every bounding chain projects to a compact subset. Finite unions of compact subsets are compact. It follows directly on cycles and boundaries that
\[
H_m(E,E_0;R)=\underset{C\subset B\ {\rm compact}}{\operatorname{colim}}
H_m(E|_C,E_0|_C;R),\qquad
H_j(B;R)=\underset C{\operatorname{colim}}H_j(C;R),
\tag{CF.5}
\]
for \(R=\mathbb Z\) or \(\mathbf F_2\). The compatible cap isomorphisms give isomorphisms \(T_j:H_{j+r}(E,E_0;R)\to H_j(B;R)\), taking each positive fibre generator to its path-component generator. In particular the relative homology below \(r\) vanishes.

For \(R=\mathbb Z\), compose \(T_0\) with \(H_0(B)\to\mathbb Z\) sending every path-component generator to one. Since \(H_{r-1}(E,E_0)=0\), (CF.3) realizes this functional as a unique class \(U_E\) in degree \(r\). Its restriction to any compact \(C\) is \(U_C\), because their evaluations coincide and (CF.3) is an isomorphism in that degree on \(C\) too. Thus it has the required fibre values, which determine it uniquely. The field version proves the mod-two assertion. The global cap map agrees with \(T_j\) on all cycles because each has compact projected support, so it is an isomorphism. Its reindexed map of free complexes also induces a homology isomorphism after tensoring with any abelian group: its cone, with differential \((y,x)\mapsto(\partial y+Rx,-\partial x)\), is free and acyclic by its degreewise split sequence of complexes. CF.0c contracts this acyclic free complex, and its contraction remains a contraction after tensoring. This proves the homological coefficient assertion. Apply the natural coefficient sequences (CF.3) to this map of free complexes, reindexed by \(r\). Its homology isomorphisms give isomorphisms of the Hom and Ext terms; the exact five-term argument gives the cohomology isomorphisms for all \(G\). The cap evaluation identity identifies that dual map with (CF.4). Over \(\mathbf F_2\) use field duality. This construction used a filtered limit for homology alone, never an inverse-limit assertion for integral cohomology. For \(r=0\), the formula and the fibre requirement directly give one. \(\square\)

<a id="cf-thom-naturality"></a>
**CF.1c (naturality, orientation, products and Euler classes).** Thom classes pull back under bundle isomorphisms over base maps, with the specified orientation in the integral case. Reversing orientation negates the integral class. For ordered direct sums,
\[
U_{E\oplus F}=U_E\smile U_F,\qquad
e(E)=s^*jU_E,\qquad e(E\oplus F)=e(E)\smile e(F).
\tag{CF.6}
\]
Here the first product is the relative product on the total sum bundle, pulled back from the external product, \(s\) is the zero section and \(j\) forgets the relative condition. The order of the factors is the order of the oriented bases. A nowhere-zero section in positive rank implies \(e(E)=0\).

**Proof.** Pullback has the stated generator on each fibre, so uniqueness in CF.1b proves naturality and the orientation reversal statement. The relative exceptional set in the external product is \(E_0\times F\cup E\times F_0\), a union of open sets. CF.0b defines the product there; CF.1a shows its fibre value is the positive ordered product generator. Uniqueness proves the external Thom product. Pullback along the base diagonal proves the sum formula, and zero-section pullback proves the Euler formula. Fibre contraction \((b,v,t)\mapsto(b,tv)\) makes \(s,\pi\) homotopy inverse, so \(jU_E=\pi^*e(E)\). A nowhere-zero section \(t:B\to E_0\) has \(t^*jU_E=0\) and is homotopic in \(E\) to \(s\), giving \(e(E)=0\). All arguments also apply modulo two. \(\square\)

<a id="cf-good-pairs"></a>

## CF.2. Quotients, discs and finite CW degree bounds

For a compact Hausdorff pair \((T,A)\), or a finite CW pair, call the pair good if \(A\) is closed and has an open neighborhood \(N\) with a strong deformation retraction to \(A\). Then collapse induces
\[
\widetilde H^*(T/A;G)\cong H^*(T,A;G).
\tag{CF.7}
\]
For \(A=\varnothing\) use \(T_+=T\amalg\{*\}\); reduced means the kernel of restriction to that base point.

**Proof.** The homotopy of \(N\) fixing \(A\) makes \(H^*(N,A)=0\), hence the triple sequence identifies \(H^*(T,N)\) with \(H^*(T,A)\). The same homotopy descends to a contraction of \(N/A\) onto its base point, so \(H^*(T/A,N/A)\cong H^*(T/A,*)\). The two excision maps remove \(A\) and \(*\), respectively, from these two pairs; the excision condition holds since these closed sets lie in the indicated open neighborhoods. The remaining pairs are the identical \((T\setminus A,N\setminus A)\). For compact Hausdorff \(T\), \(T/A\) is Hausdorff by the separation argument in RK.0, \(N/A\) is open, and the descended homotopy is continuous: its product quotient is a quotient map because a closed quotient from a compact space stays closed after product with compact \(I\). Alternatively continuity is checked before and after collapse in the two excision charts. In the finite CW applications the same continuity follows cell by cell. This proves (CF.7) and its naturality. \(\square\)

**CF.2a (an invariant finite CW neighborhood).** For every finite CW pair \((T,A)\) there are a continuous \(u:T\to[0,1]\), with \(u^{-1}(0)=A\), and a homotopy \(H:T\times I\to T\) such that
\[
H_0=1,\qquad H_t|_A=1,\qquad
t\longmapsto u(H_t x)\text{ is nonincreasing},\qquad
H_t x\in A\ \text{if }u(x)<1\text{ and }t\geq u(x).
\]
Consequently \(N=\{u<1\}\) is an open neighborhood of \(A\) which \(H\) strongly deformation retracts to \(A\) inside itself.

**Proof.** Start with the subcomplex \(A\), taking \(u=0\) and the identity homotopy. Attach the remaining finitely many cells in increasing dimension. A new zero-cell has \(u=1\) and the identity homotopy. Suppose \(u_0,H^0\) have been constructed on the old stage \(Z\), and a positive-dimensional cell is attached by \(f:S^{n-1}\to Z\), with characteristic map \(\chi:D^n\to Z\cup_fD^n\). For \(v=rz\), \(r>0\), \(z\in S^{n-1}\), put \(c(z)=u_0(f(z))\) and define
\[
u(\chi(rz))=\min\{1,\,2-r(2-c(z))\},\qquad u(\chi(0))=1.
\]
It matches \(u_0\) at \(r=1\) and is identically one for \(r\leq1/2\), hence is continuous at the centre. Extend the old homotopy by
\[
H_t(\chi(rz))=
\begin{cases}
\chi\!\left(\dfrac{2rz}{2-t}\right),& r\leq1-t/2,\\
H^0_{\,2-(2-t)/r}(f(z)),&r\geq1-t/2.
\end{cases}
\]
Use the first case at the centre. At the dividing radius the two formulas give \(f(z)=H^0_0(f(z))\). On the boundary the second gives \(H^0_t(f(z))\). They therefore glue to a continuous homotopy on the attached space and agree with the old homotopy; compact quotient maps remain quotient after product with \(I\), as used above. The first case is the bottom face, and the second the lateral face, of the cylinder retraction by rays from the point \((0,2)\).

In the first case the radius \(2r/(2-t)\) increases, so the displayed function \(u\) cannot increase. At the dividing radius its value is \(c(z)\). Thereafter the parameter \(2-(2-t)/r\) increases and the induction hypothesis makes \(u_0(H^0_{\,2-(2-t)/r}(f(z)))\) nonincreasing. If \(u(\chi(rz))<1\), then \(c(z)<1\). For \(t\geq u(\chi(rz))=2-r(2-c(z))\), the point is in the second case and its homotopy parameter is at least \(c(z)\); the induction hypothesis sends it into \(A\). The only zero values occur on the old zero set \(A\), since for \(r<1\) the expression \(2-r(2-c(z))\) is positive. Thus all four properties persist after attaching the cell. Finite induction proves them globally. Since \(u(H_t x)\leq u(x)\), the homotopy preserves \(N\); its time-one map lands in \(A\) and fixes \(A\). This proves the strong deformation retraction. \(\square\)

The required CW degree bound now follows from these chain tools and CF.2a. Each skeletal pair is good by CF.2a, and its quotient is a finite wedge of the spheres \(D^n/\partial D^n\). A sphere has reduced groups \(G\) in degree \(n\) only: cover it by the complements of opposite poles, use their contractibility and the equatorial deformation retraction of their intersection in CF.0a, and induct from \(S^0\). A finite wedge has the direct sum of those reduced groups by small-chain Mayer–Vietoris with the invariant base-point neighborhoods from CF.2a. The stage pair thus has groups only in degree \(n\); exactness inductively gives \(H^j(X;G)=0\) above the largest cell dimension. Homotopy invariance gives the same bound for a space of finite CW homotopy type. Positive-degree classes are consequently nilpotent.

For a metric bundle over compact Hausdorff \(X\), the sphere \(S(E)\) has the neighborhood \(\{\|v\|>1/2\}\) in the disc bundle, retracting by \(v\mapsto v/\|v\|\) with radial interpolation. Thus \((D(E),S(E))\) is good. The map \(D(E)\to E\) is a homotopy equivalence by fibre contraction to zero. Also \(S(E)\to E_0\) is a homotopy equivalence by the same normalization map; the pair exact sequences and the five-term argument give
\[
H^*(D(E),S(E);G)\cong H^*(E,E_0;G).
\tag{CF.8}
\]
These identifications preserve positive fibre generators. With CF.1b they also show that the reduced cohomology of \(D(E)/S(E)\) is bounded when that of \(X\) is bounded. Rank zero uses the disjoint-base-point convention throughout.

<a id="cf-projective-space"></a>

## CF.3. Projective space and the first Chern class

For a complex line \(L\), orient its underlying real plane by \((v,iv)\), and define
\[
c_1(L)=e(L_{\mathbb R})\in H^2(X;\mathbb Z).
\tag{CF.9}
\]
This definition uses CF.1, and is natural for every bundle pullback. On a compact Hausdorff base, [RK.7a](../relative-k-foundations/relative-k-foundations.html#rk-line-classification) realizes \(L\) as the pullback of the tautological line from a finite projective space.

**CF.3a (projective ring and normalization).** For the tautological line \(\mathcal S_n\to\mathbb{CP}^n\), put \(h=-c_1(\mathcal S_n)\). Then
\[
H^*(\mathbb{CP}^n;\mathbb Z)=\mathbb Z[h]/(h^{n+1}),\qquad |h|=2,
\tag{CF.10}
\]
and \(h\) evaluates to \(+1\) on the complex-oriented \(\mathbb{CP}^1\). With any abelian coefficient group \(G\), the powers \(1,h,\ldots,h^n\) give the corresponding shifted copies of \(G\). Standard linear projective inclusions preserve \(h\).

**Proof.** First recall why the line Euler number agrees with the boundary obstruction. Take a section nonzero outside a disc in an oriented two-sphere. Pulling the Thom class back by that section gives a relative class supported in the disc; forgetting the relative condition gives the Euler class, because the section is homotopic to zero. In an oriented fibre frame, its value is the degree of its boundary map to \(\mathbb C\setminus0\). This follows by naturality of the connecting homomorphism in the two disc/punctured-disc pair sequences: each connecting map takes the positive circle generator to the positive relative plane generator of CF.1a. A map \(z\mapsto z^k\) has degree \(k\); subdivide the circle into \(|k|\) arcs and compare their oriented paths to see that it sends its one-dimensional homology generator to \(k\) times that generator. Lifting a circle map's argument along the parametrizing interval gives endpoint difference \(2\pi k\); linear interpolation of this lift with \(2\pi kt\) descends to a homotopy to \(z\mapsto z^k\), proving the same assertion for a boundary map of winding \(k\).

On \(\mathbb{CP}^1\), the tautological frames are \((1,z)\) and \((w,1)\), where \(w=1/z\). A vector with coefficient one in the first frame has coefficient \(z=w^{-1}\) in the second frame on their common circle. Extend that boundary coefficient to the second disc by \(\overline w\). It has one zero, with local degree \(-1\) in the complex coordinate \(w\). The preceding relative-class argument gives \(c_1(\mathcal S_1)[\mathbb{CP}^1]=-1\). This also verifies directly that the Euler definition agrees with the first-Chern sign of [RK.6a](../relative-k-foundations/relative-k-foundations.html#rk-line-sign).

For the whole ring, \(n=0\) is the point calculation of CF.1a. For \(n\geq1\), the unit sphere bundle of \(\mathcal S_n\) is \(S^{2n+1}\): a unit vector \(v\in\mathbb C^{n+1}\) corresponds to \((\mathbb Cv,v)\). The disc bundle contracts onto \(\mathbb{CP}^n\). Apply the pair sequence for its disc and sphere and use CF.1b and CF.8. Under these identifications its relative-to-absolute map is multiplication by \(c_1(\mathcal S_n)\), by CF.1c. Since a sphere has only its degree-zero and top-degree cohomology, multiplication by this class gives isomorphisms
\[
H^{k-2}(\mathbb{CP}^n;G)\longrightarrow H^k(\mathbb{CP}^n;G)
\qquad(2\leq k\leq2n).
\]
Also \(H^1(\mathbb{CP}^n;G)=0\), by the same sequence, and \(H^0=G\) since projective space is path connected. There is one cell in each dimension \(0,2,\ldots,2n\): represent a line by a unit vector whose last coordinate is nonnegative real. Where that coordinate is positive the first \(n\) coordinates give the open \(2n\)-disc; on its boundary the quotient is \(\mathbb{CP}^{n-1}\). Iteration gives the stated cells. CF.2 therefore makes the groups above degree \(2n\) vanish. In integral homology each stage adds \(\mathbb Z\) in its new even degree: both adjacent odd groups in its pair sequence are zero, and the other groups stay unchanged. Induction gives free integral homology \(\mathbb Z\) in precisely degrees \(0,2,\ldots,2n\). This verifies the finite free hypothesis of CF.0c used in product calculations below. Induction by the displayed multiplication isomorphisms proves (CF.10) and the coefficient assertion. Naturality for the tautological line proves compatibility under inclusions. \(\square\)

**CF.3b (line tensor and dual rules).** On a compact Hausdorff base,
\[
c_1(L\otimes M)=c_1(L)+c_1(M),\qquad
c_1(L^*)=-c_1(L),\qquad c_1(\mathbf1)=0.
\tag{CF.11}
\]
In particular \(c_1(L)\) is nilpotent.

**Proof.** Realize \(L,M\) as pullbacks of tautological lines over \(\mathbb{CP}^a,\mathbb{CP}^b\), enlarging the finite embeddings so that \(a,b\geq1\). Over their product, CF.0b–CF.0c and CF.3a identify degree-two cohomology with the two copies of \(\mathbb Z\) detected by restriction to the factors. The tensor line restricts to the first tautological line on the first factor and to the second on the second factor; a fixed one-dimensional vector space from the other factor is a trivial line. Naturality of the Euler class therefore determines its degree-two class as the sum of the two classes. Pull back along the pair of classifying maps. The trivial plane has a nonzero section, so its Euler class is zero. The evaluation isomorphism \(L\otimes L^*\cong\mathbf1\) now proves the dual rule. Nilpotence follows by pullback from (CF.10), including when the base has unbounded singular cohomology. \(\square\)

<a id="cf-splitting"></a>

## CF.4. Projective bundles, injectivity and Chern classes

**Theorem CF.4a (the cohomological projective-bundle formula).** Let \(E\to X\) have constant complex rank \(r\geq1\), with \(X\) compact Hausdorff. Write \(p:P(E)\to X\) for its bundle of complex lines, \(\mathcal S\) for the tautological line in \(p^*E\), and \(t=c_1(\mathcal S)\). For every abelian group \(G\),
\[
\bigoplus_{i=0}^{r-1}H^{k-2i}(X;G)\xrightarrow{\ \cong\ }H^k(P(E);G),
\qquad (a_i)\longmapsto\sum_i p^*a_i\smile t^i.
\tag{CF.12}
\]
In particular \(p^*\) is injective. A finite tower of such projective bundles gives a compact Hausdorff flag base \(f:F(E)\to X\) with \(f^*E=L_1\oplus\cdots\oplus L_r\), and \(f^*\) is injective with every coefficient group. Several bundles can be split simultaneously by successive towers. If base cohomology vanishes above \(d\), that of the tower vanishes above \(d+r(r-1)\).

**Proof.** A finite isometric embedding of \(E\) in a trivial bundle, proved in RK.1, realizes \(P(E)\) as the closed subset of \(X\times\mathbb{CP}^{N-1}\) consisting of lines contained in the projection range. It is compact Hausdorff. In any trivializing open set \(V\subset X\), it is \(V\times\mathbb{CP}^{r-1}\), with \(\mathcal S\) pulled back from the projective factor. CF.0b–CF.0c and CF.3a show that (CF.12) is an isomorphism over \(V\), for all \(G\) and without a condition on the topology or cohomology of \(V\).

Choose a finite trivializing open cover. If the formula holds over \(V,W,V\cap W\), map the direct sum of the shifted base Mayer–Vietoris sequences into the sequence for their projective preimages by the formula in (CF.12). Cup multiplication by the globally defined even cocycles \(t^i\) commutes with connecting homomorphisms, by the cup differential calculation in CF.0b. The five-term diagram argument proves the isomorphism over \(V\cup W\). Induct on the size of the cover: the intersection of its last set with the union of its predecessors is covered by fewer trivializing sets. This proves the formula globally. Its first summand proves injectivity.

Choose a Hermitian metric as in RK.1. Orthogonal complement splits \(p^*E=\mathcal S\oplus E'\). Projectivize \(E'\), then repeat. Each base remains compact Hausdorff by the preceding closed-subset construction, and each pullback is injective by (CF.12). After \(r-1\) steps all summands are lines. Composition proves the assertion for the flag map, and repeating the construction for other pulled-back bundles proves simultaneous splitting. The degree bound increases at a rank-\(s\) projective step by \(2(s-1)\); summing gives \(r(r-1)\). A locally constant rank on a compact base has only finitely many values; apply these assertions on its finitely many clopen rank subsets, using the identity map and the empty sum of lines on a rank-zero subset. \(\square\)

**CF.4b (construction and rules of Chern classes).** There are natural classes \(c_j(E)\in H^{2j}(X;\mathbb Z)\), with \(c_0=1\) and \(c_j=0\) for \(j>r\), characterized by
\[
t^r-p^*c_1(E)t^{r-1}+p^*c_2(E)t^{r-2}
-\cdots+(-1)^r p^*c_r(E)=0
\tag{CF.13}
\]
in \(P(E)\). After splitting, they are the elementary symmetric polynomials in \(x_i=c_1(L_i)\). Thus
\[
c(E\oplus F)=c(E)c(F),\quad
c_1(E)=c_1(\det E),\quad c_r(E)=e(E_{\mathbb R}).
\tag{CF.14}
\]
Here \(c(E)=\sum_jc_j(E)\), and the orientation in the last formula is the ordered complex orientation.

**Proof.** The unique expansion of \(t^r\) in the basis (CF.12), in integral cohomology, defines the coefficients in (CF.13) with those signs. Degree forces the coefficient of \(t^{r-j}\) to lie in degree \(2j\). Pullback of the projective bundle and its tautological line preserves the relation; uniqueness proves naturality, including pullbacks whose total base is another compact Hausdorff space. For a line \(E=L\), \(P(L)=X\) and \(\mathcal S=L\), so this construction gives (CF.9).

Suppose \(E=\bigoplus_iL_i\). The bundle \(p^*E\otimes\mathcal S^*\) on \(P(E)\) has the nonzero section given by the inclusion \(\mathcal S\hookrightarrow p^*E\). Its Euler class is zero by CF.1c. It splits into the lines \(p^*L_i\otimes\mathcal S^*\), whose Euler classes are \(p^*x_i-t\), by CF.3b. The Euler product in CF.1c gives
\[
0=\prod_i(p^*x_i-t),\qquad \text{hence}\quad \prod_i(t-p^*x_i)=0.
\]
Comparing this monic relation with the unique relation (CF.13) proves the elementary symmetric formula. For general \(E,F\), split both by CF.4a. On that base their sum is the sum of all the lines, so its elementary symmetric formula is the product of their two elementary symmetric formulas. Injectivity of the pullback gives the first identity of (CF.14). Tensoring the split lines gives \(\det E\), so CF.11 gives the second. The third follows from the Euler product of the same complex lines. Again injectivity brings the equality to \(X\). No characteristic-class construction has been presumed in these proofs. \(\square\)

<a id="cf-character"></a>

## CF.5. The even Chern character and its relative products

**Theorem CF.5a (even bundle character).** For every compact Hausdorff space there is a natural ring map
\[
\operatorname{ch}:K^0(X)\longrightarrow\bigoplus_{j\geq0}H^{2j}(X;\mathbb Q),
\qquad \operatorname{ch}(L)=e^{c_1(L)}.
\tag{CF.15}
\]
It sends rank to degree zero and respects homotopy, direct sums, tensor products and pullback. Each individual character has finitely many nonzero components. For a pointed space it restricts to a reduced character. This statement asserts a map, not an isomorphism for arbitrary compact spaces.

**Proof.** Set \(c_j=0\) beyond the rank and define the integral Newton polynomials recursively by \(s_1=c_1\) and
\[
s_k-c_1s_{k-1}+c_2s_{k-2}-\cdots
 +(-1)^{k-1}c_{k-1}s_1+(-1)^k k c_k=0.
\tag{CF.16}
\]
The polynomial identity \(s_k=\sum_i x_i^k\), when \(c_j\) are the elementary symmetric polynomials, follows by differentiating \(\prod_i(1+x_i z)\) formally and multiplying its logarithmic derivative by that product: its coefficient of \(z^{k-1}\) is exactly (CF.16). This is an identity of integral polynomials and does not require division in cohomology. Define degree \(2k\) of the character as \(s_k(E)/k!\) and its degree-zero term as rank. Each is natural by CF.4b. On a splitting base it is \(\sum_i e^{x_i}\).

The flag base is compact Hausdorff. Each of its line summands is pulled back from some finite projective space by RK.7a, so each \(x_i\) is nilpotent by CF.3b. Consequently \(s_k\) is zero on the splitting base for all sufficiently large \(k\). Its injectivity in rational cohomology implies the same on \(X\). Thus the series defines the direct-sum target in (CF.15), even when the full cohomology of \(X\) is unbounded.

Split \(E,F\) simultaneously. Their direct sum has roots \(x_i\) and \(y_j\), and their tensor product has line summands with roots \(x_i+y_j\), by CF.11. The finite exponentials therefore give
\[
\operatorname{ch}(E\oplus F)=\sum_i e^{x_i}+\sum_j e^{y_j},\qquad
\operatorname{ch}(E\otimes F)=\sum_{i,j}e^{x_i+y_j}
=\left(\sum_i e^{x_i}\right)\left(\sum_j e^{y_j}\right).
\]
Injectivity gives these identities on the original base. They pass to bundle differences in the Grothendieck group, which RK.1 identifies with operator \(K^0\). A cylinder bundle has equal endpoint characters by homotopy invariance in CF.0a, so the asserted homotopy rule holds. Pullback to the base point identifies degree zero with rank and kills all positive degrees; taking kernels gives the reduced character. \(\square\)

For compact pairs below, relative \(K^0(T,A)\) is the bundle-triple group of RK.3, identified by RK.4 with \(\widetilde K^0(T/A)\). For an empty relative subset use the disjoint base point. The cohomological quotient comparison requires the good-pair hypothesis in CF.2; the K-theory quotient comparison does not. These are separate hypotheses.

<a id="cf-relative-character"></a>
**Theorem CF.5b (relative character in the used pairs).** For a good compact Hausdorff pair there is a natural even map
\[
\operatorname{ch}_{T,A}:K^0(T,A)\longrightarrow
\bigoplus_{j\geq0}H^{2j}(T,A;\mathbb Q)
\tag{CF.17}
\]
given by reduced character on the quotient and CF.7. Forgetting the comparison of a triple gives
\[
j\operatorname{ch}_{T,A}[E^+,E^-,\sigma]
=\operatorname{ch}(E^+)-\operatorname{ch}(E^-).
\tag{CF.18}
\]
For finite CW pairs and for disc/sphere bundle pairs over compact Hausdorff bases, this map respects the absolute bundle action and the relative external and cup products. These are the product and action hypotheses in this theorem; its construction and forgetful rule require only a good compact Hausdorff pair. The radial products include the ordered complex spinor symbols. Their induced compact-support character is natural for bundle pullback, respects multiplication by base classes, and is normalized to \(-1\) on the positive planar class of RK.6.

**Proof: construction and normalization.** RK.3 gives an actual difference of projections constant on \(A\), hence actual bundles on \(T/A\) whose rank difference at the base point is zero. Apply CF.15 on this compact Hausdorff quotient and use CF.7. Both comparisons are natural, so maps of good compact pairs preserve (CF.17). The quotient pullback of the bundle difference forgets its comparison by RK.3; CF.15 proves (CF.18). On the compactified complex plane, RK.6–RK.6a identify its positive class as \([\mathcal S_1]-[\mathbf1]\). CF.3a and (CF.15) give \(e^{-h}-1=-h\), hence character value \(-1\) on the positive plane orientation.

**Proof: products.** We give the quotient argument with its topological requirement. The quotient of a finite CW pair has a finite CW structure with the collapsed subcomplex as its base-point zero-cell: retain the interiors of the other cells, and compose their boundary attaching maps with the collapse. Its topology is the finite attaching-space quotient topology. Apply CF.2a to this pointed pair. It supplies a function \(u\), vanishing precisely at the base point, and a homotopy fixing it with \(u(H_t y)\leq u(y)\) and \(H_1\{u<1\}=\{*\}\).

For \(D(E)/S(E)\), use the explicit radial data: take \(u(r)=1\) for \(r\leq1/2\) and \(u(r)=2(1-r)\) for \(r\geq1/2\). Choose a continuous \(\psi\) equal to zero for \(r\leq1/4\) and to one for \(r\geq1/2\). The homotopy replaces the radius by \(r+t\psi(r)(1-r)\) without changing its unit direction; it fixes the centre and descends continuously to the collapsed sphere. The radius is nondecreasing, so \(u\) is nonincreasing along this homotopy, and its time-one map sends \(u<1\) to the base point. A rank-zero disc quotient, or an empty-relative-subset quotient, has an isolated base point; use the identity homotopy and the function zero there and one elsewhere. Thus all the stated pointed spaces have invariant data. The same constructions before collapse give invariant data for the original finite CW and disc/sphere pairs with their closed relative subsets as zero sets.

Here is a direct check of the needed product pair. Given such data for \(Y,Z\), write \(a=u(y),b=u(z)\). Near their wedge, where \(\min(a,b)<1\), apply the two homotopies with final times
\[
\theta_Y=\min(1,b/a),\qquad \theta_Z=\min(1,a/b)
\]
and interpolate these times from zero. For \(a=0<b\) set \((\theta_Y,\theta_Z)=(1,0)\); for \(b=0<a\) set them to \((0,1)\); at \(a=b=0\) use \((0,0)\). The homotopies fix their zero sets pointwise. Continuity of their composed maps at a zero coordinate follows from joint continuity and compactness of the time interval: for any neighborhood of that fixed point, finitely many time neighborhoods give a single point neighborhood whose entire homotopy lies there. Thus no continuity of the time ratios at \((0,0)\) is required. At every intermediate time, a coordinate initially having value less than one still has value less than one, because its own homotopy makes that value nonincreasing. Hence the entire deformation stays inside the open set \(\min(a,b)<1\), for two CW factors, two radial factors, or a mixed CW/radial pair. The same observation applies before collapse to the relative product union. They fix the wedge pointwise and finish on the wedge: the smaller positive coordinate receives time one and is sent to the base point. Thus \(Y\vee Z\) is a closed subspace with a retracting open neighborhood in \(Y\times Z\). CF.7 applies to its quotient \(Y\wedge Z\).

Restriction \(H^k(Y\times Z;\mathbb Q)\to H^k(Y\vee Z;\mathbb Q)\) is surjective in every degree. In positive degrees the target is the direct sum of the two reduced groups, and their classes extend via the two projections. This direct-sum assertion follows from CF.0a using the two neighborhoods in the wedge obtained by adding a contracting base-point neighborhood in the other factor. In degree zero the same extensions, and a common constant, give every class: on the path component containing the base point its value must be constant, and on the other path components the two projection functions can be chosen independently. The pair sequence consequently makes
\[
q^*:\widetilde H^k(Y\wedge Z;\mathbb Q)\longrightarrow H^k(Y\times Z;\mathbb Q)
\tag{CF.19}
\]
injective, including degree zero.

For clarity, the relative tensor product itself can be constructed directly. Polarize each boundary comparison and view it as an odd self-adjoint invertible matrix on \(E^+\oplus E^-\). Embed the bundles into trivial bundles by RK.1, extend its matrix entries from the closed relative subspace by RK.0, and compress and symmetrize. This gives an odd self-adjoint endomorphism \(c_E\) on the whole bundle with the specified boundary value; do the same for \(F\). The operator \(c_E\widehat\otimes1+1\widehat\otimes c_F\) has square \(c_E^2\otimes1+1\otimes c_F^2\). It is invertible wherever either boundary comparison is invertible. Its even part is \(E^+\otimes F^+\oplus E^-\otimes F^-\), and its odd part is \(E^+\otimes F^-\oplus E^-\otimes F^+\). Its off-diagonal map defines the relative tensor triple. Different extensions are joined by linear interpolation fixing the boundary, so give the same class; polarization, sums and cylinder homotopies preserve the class. If a comparison extends invertibly over its whole factor, choose that extension and the tensor comparison is globally invertible, giving the zero class. Thus this construction respects all the relations in RK.3. For disc spinor symbols it is exactly the sum of their Clifford operators, so fixes the product convention used here.

Now represent two classes as reduced differences on their pair quotients \(Y,Z\). The construction just given on \((Y,*),(Z,*)\) produces a relative triple on \((Y\times Z,Y\vee Z)\), hence by RK.4 a class on the smash quotient. Pulling back by \(q\) forgets the comparison and gives the ordinary external product of the two differences, by the displayed even and odd parts. Naturality back to the original pair quotients identifies this with the original external symbol product. Formula (CF.18), naturality and CF.15 identify its character after \(q^*\) with the external product of the two characters. Injectivity in (CF.19) proves equality on the smash quotient. CF.0b and CF.7 transport it to the relative cohomology external product. For the closed relative subsets, first replace them by their retracting open neighborhoods. Their pair sequences identify the relative groups, and the neighborhood deformation of the product union is the same two-coordinate construction above. The open-subspace product in CF.0b therefore induces this closed-pair product. Pullback along a map of pairs, including the base diagonal, gives the cup and balanced-symbol products.

For the absolute action in the stated finite CW or radial disc/sphere pairs, \(T/A\) has the neighborhood-deformation data constructed above. Use the second pointed space \(T_+\), which has an isolated base point, and extend an absolute bundle there by the zero bundle at that point. The smash-product argument therefore applies to these two pointed spaces. The map
\[
T/A\longrightarrow (T/A)\wedge T_+,\qquad [t]\longmapsto[t]\wedge t
\]
is continuous: it descends from the diagonal followed by quotient, which is constant on \(A\). Pulling back the external product gives the tensor action on the relative triple. The same argument therefore proves
\(\operatorname{ch}_{T,A}(b\alpha)=\operatorname{ch}(b)\smile\operatorname{ch}_{T,A}(\alpha)\).

Finally RK.4 identifies \(K^0_c(E)\) with the relative disc/sphere group over a compact base. CF.7–CF.8 identify its character target with \(H^*(E,E_0;\mathbb Q)\). The radial comparisons are natural under isometric bundle pullback; changing a Hermitian metric is an interpolation through positive metrics and gives the same maps by the cylinder and prism arguments. This proves all the compact-support assertions. \(\square\)

<a id="cf-thom-character"></a>

## CF.6. The exact complex Thom comparison

**Theorem CF.6 (the outward symbol and Todd factor).** Let \(E\) be a complex rank-\(r\) bundle over a compact Hausdorff base. Let \(\tau_E\in K_c^0(E)\) be the outward complex spinor symbol with spinors \(\Lambda^*E\) and comparison \(c(v)^+\). Its zero-section difference is \(\lambda_{-1}(E)=\sum_j(-1)^j[\Lambda^jE]\). With \(U_E\) the complex-oriented cohomological Thom class,
\[
\operatorname{ch}_c(\tau_E)
=(-1)^r\pi^*\!\left(e^{c_1(E)}\operatorname{Td}(E)^{-1}\right)\smile U_E,
\qquad
\operatorname{Td}(E)=\prod_{i=1}^r\frac{x_i}{1-e^{-x_i}}.
\tag{CF.20}
\]
The factors are their power-series values at zero. They define natural base classes through symmetric polynomials in the Chern classes. All the series here terminate after evaluation. In particular this supplies the comparison on finite CW bases and compact Hausdorff bases of finite CW homotopy type without adding such a hypothesis to the analytic KK Thom theorem.

**Proof.** For a line \(L\), the Thom isomorphism CF.1b uniquely writes its character as \(\pi^*g_L\smile U_L\). The action and zero-section rules in CF.5b and CF.1c give
\[
c_1(L)g_L=1-e^{c_1(L)}.
\tag{CF.21}
\]
This equation alone does not allow division by a zero divisor. Work first with \(\mathcal S_n\to\mathbb{CP}^n\) and \(x=-h\). CF.3a says every even coefficient \(g_n\) is a polynomial of degree at most \(n\) in \(x\). Equation (CF.21) determines all coefficients except the coefficient of \(x^n\). Inclusion in \(\mathbb{CP}^{n+1}\) pulls the identical line symbol and its Thom class back, by CF.5b and CF.1c. Its next equation determines that final coefficient. Thus for every \(n\),
\[
g_n=\left.\frac{1-e^x}{x}\right|_{\mathbb Q[x]/(x^{n+1})}
=-\sum_{k=0}^{n}\frac{x^k}{(k+1)!}.
\tag{CF.22}
\]
Any line on a compact Hausdorff base is pulled back from a finite projective space by RK.7a. Naturality of its symbol, character and ordinary Thom class therefore gives the same coefficient \(g_L=(1-e^{c_1(L)})/c_1(L)\). At zero this means the value \(-1\), agreeing with the independently verified planar normalization in CF.5b.

Apply the splitting map \(f:F(E)\to X\) of CF.4a. Naturality of CF.1b identifies its map on relative bundle cohomology with its map on base cohomology shifted by \(2r\). It is consequently injective. On the splitting base the spinor symbol is the ordered tensor product of its line symbols: the graded exterior identification \(\Lambda^*(\bigoplus L_i)=\widehat\bigotimes_i\Lambda^*L_i\) identifies its operator with the sum of their odd Clifford operators. Their squares add and their cross terms cancel. CF.5b preserves this actual symbol product, and CF.1c preserves the ordered complex Thom product. Their characters therefore multiply to
\[
\pi^*\prod_i\frac{1-e^{x_i}}{x_i}\smile U_{f^*E}
=(-1)^r\pi^*\!\left(e^{\sum_i x_i}\prod_i\frac{1-e^{-x_i}}{x_i}\right)\smile U_{f^*E}.
\]
Each homogeneous piece of the symmetric product is a polynomial in the elementary symmetric polynomials. To see this without an additional algebraic premise, order its monomials lexicographically: the leading monomial of a symmetric polynomial has exponents \(a_1\geq\cdots\geq a_r\). Subtract its coefficient times \(c_1^{a_1-a_2}c_2^{a_2-a_3}\cdots c_r^{a_r}\); this has exactly that leading monomial. Repetition terminates among the finitely many monomials of the fixed degree. Thus CF.4b constructs the base class in every degree. On the compact flag base the roots are individually nilpotent; every product series is a finite polynomial there. Pullback injectivity makes all sufficiently high base components zero too. The same applies to the inverse factors, whose constant terms are one. Equation (CF.14) identifies \(\sum_i x_i\) with \(f^*c_1(E)\). Relative injectivity now gives (CF.20) on \(X\).

For a line, its Hermitian dual vector \(v^*\in L^*\) gives the triple \((\mathbf1,\pi^*L^*,\lambda\mapsto\lambda v^*)\), with fibre comparison \(\overline z\). Tensor these line triples in the graded order to obtain the dual Koszul symbol. Its zero-section difference is \(\lambda_{-1}(E^*)\). Replacing the line numerator in (CF.21) by \(1-e^{-x}\) gives coefficient \((1-e^{-x})/x\), with fibre value \(+1\). The same proof therefore gives \(\operatorname{Td}(E)^{-1}U_E\). These formulas keep both the symbol and its fibre sign specified. \(\square\)

## What has been proved

CF.0 proves the chain, product and coefficient tools. CF.1 proves the ordinary singular-cohomology Thom theorem on every Hausdorff base, with integral orientations and arbitrary abelian coefficients, and with mod-two coefficients without orientation. CF.2 proves the quotient comparison in the good compact pairs and finite CW pairs, the radial disc/sphere comparison and the needed degree bounds. CF.3–CF.4 prove the projective ring, line normalization and tensor law, the cohomological splitting injection and the Chern classes. CF.5 constructs the exact even relative character, its action and its products in the used pairs. CF.6 proves the full outward-symbol Todd formula.

The bundle embeddings, homotopy transport and relative bundle/operator correspondence are the earlier local proofs RK.0–RK.7a cited at their point of use. A full odd character, its suspension compatibility and the rational-isomorphism theorem for finite CW pairs are not used or asserted here. No comparison isomorphism between vector-bundle K-theory and singular cohomology on all compact Hausdorff spaces is asserted.

## Free source comparison

- A. Hatcher, [*Algebraic Topology*, author-posted text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Sections 2.1 and 3.1–3.2 for chains, coefficient sequences and products; Theorem 4D.1, printed pp. 432–434, for the cohomological Leray–Hirsch formulation; Corollary 4D.9, printed p. 441, for the ordinary Thom formulation. The chain and compact-subset proofs above supply these used inputs locally, including the arbitrary Hausdorff base and all integral coefficient groups. The text is freely readable on the [author's book page](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html); it retains the copyright and terms on the [copyright page](https://pi.math.cornell.edu/~hatcher/AT/ATcopyright.html).
- A. Hatcher, [*Vector Bundles and K-Theory*, author-posted draft](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), Section 3.1, printed pp. 78–81, for the projective-bundle construction of Chern classes, and Section 4.1, printed pp. 109–110, especially Proposition 4.2, for the Newton-polynomial even character and its tensor rule. CF.3–CF.6 give independent proofs of the exact results used here. The freely readable [author's book page](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html) describes the draft's scope; free access does not change the external text's copyright.

