# Expanding subspaces and hyperbolic Lefschetz cutoffs

A local Lefschetz contribution can be computed by compact cohomology on an expanding subspace. “Expanding” here is a condition on positive real eigenvalues. It does not mean that every vector in the subspace grows in a chosen Euclidean metric. The proof first separates directions by modulus, constructs a metric suited to that separation, and then removes the extra directions by their action on positive rays.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The [ordinary local cutoff theorem](homotopies-and-local-cutoffs-for-lefschetz-contributions.md#the-ordinary-cutoff-has-a-closed-entrance-and-an-open-exit) constructs the closed entrance and open exit used in the mixed box. Its [family class comparison](homotopies-and-local-cutoffs-for-lefschetz-contributions.md#a-family-class-has-no-parameter-integration-shift) applies to the one normalized scalar family of coefficient maps. The [compact-coefficient correspondence trace](lefschetz-traces-of-constructible-correspondences.md#a-finite-rank-trace-does-not-require-a-finite-vector-space) allows every analytic self-map, and hence the fixed-point-free map on the positive-ray sphere.

The scaling input consists of the [normalized transport](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-comparison--canonical-transport-and-its-normalization), its [cocycle and uniqueness](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cocycle--what-the-canonical-transport-actually-proves), [ordinary contraction](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-radial-star--ordinary-contraction-to-the-zero-section), [proper-support contraction](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-radial-support--proper-support-contraction), and the [actual comparisons through sheaf operations](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-functors--transport-through-sheaf-operations). [Perfect inverse images, tensors and internal Hom](../../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom), together with [proper image on coefficient support](../../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks), give the required finite complexes. Below we check the compactification, stabilization and induced operators through these particular maps.

Let \(V\) be a finite-dimensional real vector space, \(k\) a characteristic-zero field, and \(F\) a bounded positively conic, real constructible complex with perfect stalks. Conicity means local constancy along parametrized positive scaling orbits. On a vector space the nonzero orbits are embedded rays. Fix a real linear endomorphism and a degree-zero coefficient morphism
\[
 u:V\longrightarrow V,\qquad
 \phi:u^{-1}F\longrightarrow F,\qquad
 1\notin\operatorname{Ev}(u).
 \qquad\text{(1)}
\]
The fixed set of \(u\) is \(\{0\}\). Its normalized local contribution is \(C_0(\phi)\). If the coefficient vanishes near zero this number is zero. Traces below are alternating traces on perfect complexes, written \(\operatorname{str}\).

## Spectral intervals define the two kinds of subspace

Write \(V^\mathbb C_\lambda\) for the generalized \(\lambda\)-eigenspace of the complexification of \(u\). An invariant real subspace \(S\) is a **shrinking space** when the restriction has no real eigenvalue greater than one and the quotient has no real eigenvalue in \([0,1)\). An invariant real subspace \(E\) is an **expanding space** when the restriction has no real eigenvalue in \([0,1)\) and the quotient has no real eigenvalue greater than one. Equivalently,
\[
 \begin{aligned}
 \bigoplus_{\lambda\in[0,1)}V^\mathbb C_\lambda
 &\subset S^\mathbb C
 \subset\bigoplus_{\lambda\notin(1,\infty)}V^\mathbb C_\lambda,\\
 \bigoplus_{\lambda\in(1,\infty)}V^\mathbb C_\lambda
 &\subset E^\mathbb C
 \subset\bigoplus_{\lambda\notin[0,1)}V^\mathbb C_\lambda.
 \end{aligned}
 \qquad\text{(2)}
\]
The intervals in this display are subsets of the real axis in \(\mathbb C\); their complements include nonreal eigenvalues. Invariance is still required.

**Proof of the equivalence.** The primary decomposition projections are polynomials in \(u\): the pairwise relatively prime powers of \(z-\lambda\) give the projections by the polynomial Bezout identity. They therefore preserve every invariant subspace. The restriction and quotient decompose into their intersections and images in the primary blocks. A nonzero invariant part of a \(\lambda\)-block has eigenvalue \(\lambda\); a nonzero quotient of that block does too. Thus excluding an eigenvalue from the restriction forces the intersection to vanish, whereas excluding it from the quotient forces the entire block into the subspace. These are exactly the two inclusions in each line of (2). Conjugate blocks occur together because the subspace is real. This proves both directions.

In particular,
\[
 u^{-1}S=S,\qquad u|_E:E\longrightarrow E
 \text{ is an isomorphism}.
 \qquad\text{(3)}
\]
Indeed, the quotient by \(S\) has no zero eigenvalue, while the restriction to \(E\) has none. The first equality does not assert \(uS=S\): zero eigenvalues may occur inside \(S\).

The smallest expanding space is
\[
 W=\left(\bigoplus_{\lambda>1}V^\mathbb C_\lambda\right)\cap V.
 \qquad\text{(4)}
\]
Every expanding space contains \(W\). A negative eigenvalue of large modulus is allowed in an expanding space but is not forced into it.

For such an \(E\), define \(C_E=R\Gamma_c(E;F|_E)\). Its operator \(U_E\) is compactly supported pullback by the linear isomorphism \(u_E=u|_E\), followed by \(\phi|_E\):
\[
 C_E\xrightarrow{u_E^*}
 R\Gamma_c(E;u_E^{-1}(F|_E))
 \xrightarrow{\phi|_E}C_E.
 \qquad\text{(5)}
\]
The linear isomorphism \(u_E\) is a proper homeomorphism. Its ordinary inverse-image unit, with ordinary and proper direct image identified for this homeomorphism, defines the first arrow and takes a compact support to its compact inverse image. It includes the induced action on an orientation generator; no orientation scalar is removed from it. Ordinary restriction to the linear subspace makes \(F|_E\) bounded conic constructible with perfect stalks. The proper-support contraction map from its zero costalk to \(C_E\) is an isomorphism, and the point costalk is perfect by exceptional inverse-image closure. This proves finiteness without compact support of \(F\) on \(V\), and also covers \(E=0\).

We will prove
\[
 \boxed{C_0(\phi)=\operatorname{str}(U_E)
 \quad\text{for every expanding space }E.}
 \qquad\text{(6)}
\]

## Conic projections and the actual contraction maps

We need constructibility for a projection \(q:A\oplus B\to B\), although this map is not proper. For a conic perfect constructible \(K\), both \(Rq_!K\) and \(Rq_*K\) are conic perfect constructible.

**Proof.** Compactify \(A\) by the sphere
\[
 Y=\{(t,v)\in\mathbb R\oplus A:t^2+|v|^2=1\},\qquad
 a\longmapsto\frac{(1,a)}{\sqrt{1+|a|^2}}.
 \qquad\text{(7)}
\]
The image is the open positive hemisphere. Let \(j:A\oplus B\hookrightarrow Y\times B\) be this embedding and put \(m(t,v,b)=(v,tb)\). On the positive hemisphere, write \(a=v/t\); then \(m(t,v,b)=t(a,b)\). Pull the normalized transport back along the analytic map \((a,b)\mapsto((a,b),(1+|a|^2)^{-1/2})\). Its inverse identifies \(j^{-1}m^{-1}K\) with \(K\). This uses one specified transport morphism, natural in \(K\), even though the positive scalar varies with \(a\). Open extension and open internal-Hom adjunction consequently give
\[
 j_!K\simeq k_{\{t>0\}}\otimes m^{-1}K,\qquad
 Rj_*K\simeq R\mathcal Hom(k_{\{t>0\}},m^{-1}K).
 \qquad\text{(8)}
\]
The second identity is ordinary open internal-Hom adjunction applied to \(m^{-1}K\); the first is extension by zero from that same open restriction. The map \(m\) is analytic on all of \(Y\times B\), and the positive hemisphere is subanalytic. The constructible inverse-image, tensor and internal-Hom theorems therefore make both objects in (8) bounded with perfect stalks. Projection \(\pi:Y\times B\to B\) is proper because \(Y\) is compact. Proper constructible direct image then applies. Ordinary composition gives \(R\pi_*Rj_*K=Rq_*K\); proper-support composition and \(R\pi_!=R\pi_*\) give \(R\pi_*j_!K=Rq_!K\). These are identifications of the natural direct-image functors and preserve coefficient morphisms.

Conicity follows from the actual equivariant direct-image comparisons for \(q\). For \(q_!\) they are proper-support base change, even though \(q\) itself is not proper. For \(q_*\), product base change with the scaling parameter is checked on rectangles using interval descent; conjugation by the action homeomorphism gives the action square. The normalized transport in both cases restricts to the identity at parameter one. No general theorem that arbitrary nonproper images preserve constructibility is being used.

For a conic \(H\) on \(B\), the following specified maps are isomorphisms:
\[
 R\Gamma(B;H)\xrightarrow{\mathrm{restriction}}H_0,
 \qquad
 R\Gamma_{\{0\}}(B;H)
 \xrightarrow{\mathrm{support\ inclusion}}R\Gamma_c(B;H).
 \qquad\text{(9)}
\]
These are the ordinary and proper-support contraction maps. Ordinary restriction also gives \(R\Gamma(\overline B_b;H)\simeq H_0\) for every closed ball of positive radius. To see the last assertion, restriction to each open ball is an isomorphism by the scaling restriction criterion: the parameter set carrying a vector into that ball is a nonempty interval. For a compact closed ball, neighbourhood continuity computes its sections from the slightly larger open balls. Their restrictions are all the same isomorphism to the germ at zero. Thus the induced closed-ball restriction is that isomorphism. No orientation shift occurs in these maps.

## An adapted metric produces the correct mixed box

First suppose that no eigenvalue has modulus one. The real primary decomposition gives
\[
 V=V_+\oplus V_-,\qquad
 V_+^\mathbb C=\bigoplus_{|\lambda|>1}V^\mathbb C_\lambda,\quad
 V_-^\mathbb C=\bigoplus_{|\lambda|<1}V^\mathbb C_\lambda.
 \qquad\text{(10)}
\]
There is an inner product for which, with \(0<c_1<1<c_2\),
\[
 |u_-b|\le c_1|b|,\qquad |u_+a|\ge c_2|a|.
 \qquad\text{(11)}
\]

**Proof.** If a linear map \(A\) has spectral radius less than \(q<1\), define
\[
 |v|_P^2=\sum_{j\ge0}q^{-2j}|A^jv|_0^2.
 \qquad\text{(12)}
\]
A Jordan block estimate bounds \(|A^j|\) by a polynomial in \(j\) times \(r^j\), with \(r<q\), so the series converges and is a positive definite quadratic form. Shifting its sum gives
\[
 |Av|_P^2=q^2(|v|_P^2-|v|_0^2)\le q^2|v|_P^2.
 \qquad\text{(13)}
\]
Choose \(\operatorname{spr}(u_-)<q_-<1\) and \(\operatorname{spr}(u_+^{-1})<q_+<1\) for the nonzero summands and apply (12) to each. In the convergent-series estimate one may choose \(r\) strictly between the relevant spectral radius and \(q_\pm\); the polynomial Jordan factor is then summable against \((r/q_\pm)^{2j}\), also when the original map has a zero eigenvalue. The orthogonal sum gives \(c_1=q_-\) and \(c_2=q_+^{-1}\): apply the inverse estimate to \(u_+a\) to obtain the lower bound in (11). A zero summand imposes no condition on its constant and can be omitted. Thus no invertibility of \(u_-\) is assumed.

For \(a,b>0\) set
\[
 Z_{a,b}=B_a^+\times\overline B_b^-.
 \qquad\text{(14)}
\]
The plus ball is open and the minus ball closed. Since \(u_+^{-1}B_a^+\subset B_a^+\) and \(\overline B_b^-\subset u_-^{-1}\overline B_b^-\),
\[
 u^{-1}Z_{a,b}\cap Z_{a,b}
 =u_+^{-1}B_a^+\times\overline B_b^-.
 \qquad\text{(15)}
\]
Call this intersection \(M_{a,b}\). It is open in \(Z_{a,b}\), because its plus factor is open in \(B_a^+\), and closed in \(u^{-1}Z_{a,b}\), because its minus factor is closed in \(u_-^{-1}\overline B_b^-\). These are the two map-existence conditions of the ordinary cutoff theorem. The set \(Z_{a,b}\) is a locally closed subanalytic neighborhood of zero with compact closure, and \(u\) has no other fixed point anywhere. The coefficient \(F_{Z_{a,b}}=k_{Z_{a,b}}\otimes F\) is constructible with closed support contained in that compact closure. Its ordinary global complex is consequently its compact global complex, identified by locally closed extension with \(R\Gamma_c(Z_{a,b};F|_{Z_{a,b}})\). The cutoff morphism is the ordinary pullback coefficient on \(u^{-1}Z_{a,b}\), closed restriction to \(M_{a,b}\), and open extension into \(Z_{a,b}\). The theorem gives
\[
 C_0(\phi)=\operatorname{str}(U_{a,b}),
 \quad U_{a,b}\text{ on }R\Gamma_c(Z_{a,b};F|_{Z_{a,b}}).
 \qquad\text{(16)}
\]
This operator is ordinary pullback on the ambient compact coefficient \(F_{Z_{a,b}}\), followed by closed restriction on the entrance and open extension on the exit. It is not pullback of arbitrary compactly supported sections by a possibly singular \(u\).

## A large cutoff stabilizes by extension by zero

Fix \(b>0\) and write \(Z_{\infty,b}=V_+\times\overline B_b^-\). For sufficiently large \(a\), the **forward open-extension map**
\[
 R\Gamma_c(Z_{a,b};F)
 \longrightarrow R\Gamma_c(Z_{\infty,b};F)
 \qquad\text{(17)}
\]
is an isomorphism.

**Proof.** Use (7) with \(A=V_+\), \(B=V_-\), and the same adapted norms that define the balls in (14). On \(Y\times V_-\) retain \(x_-\) as the unchanged minus coordinate. Let
\[
 F'=j_!(F_{\{|x_-|\le b\}}),
 \qquad\text{(18)}
\]
where \(x_-\) denotes the minus coordinate. Equivalently, \(F'=k_{\{t>0\}}\otimes m^{-1}F\otimes k_{\{|x_-|\le b\}}\). The last factor cuts off the unchanged minus coordinate of \(Y\times V_-\); it is not the pullback of a cutoff on the scaled coordinate \(t x_-\). The variable-scalar transport used in (8), tensored with this closed cutoff, proves the displayed equivalence. The tensor and inverse-image theorems make \(F'\) constructible, and its closed support is contained in compact \(Y\times\overline B_b^-\). The closed support can meet \(t=0\), but the ordinary restriction of \(F'\) to that fibre is zero, because it is an open extension by zero.

Push \(F'\) by \(g(t,v,x_-)=t\). Although \(g\) need not be proper on its entire domain, it is proper on this compact closed coefficient support. Thus \(H=Rg_*F'=Rg_!F'\) is bounded constructible with perfect stalks. Proper base change on the coefficient support identifies \(H_0\) with cohomology of the ordinary fibre restriction, which is zero. Constructibility on the line supplies \(0<\epsilon_0<1\) such that the cohomology sheaves of \(H\) are locally constant on both \((-\epsilon_0,0)\) and \((0,\epsilon_0)\). The point zero itself need not be a regular point.

For \(0<\epsilon<\epsilon_0\),
\[
 R\Gamma([-\epsilon,\epsilon];H)\simeq H_0=0.
 \qquad\text{(19)}
\]
Here is the endpoint argument. On the compact interval, localize at zero. The complementary arms are \([-\epsilon,0)\) and \((0,\epsilon]\). Each carries a constant complex. Its open extension across zero has zero ordinary sections: the triangle from the constant complex on the corresponding closed half interval to its value at zero has restriction map the identity, hence zero fibre. For bounded complexes, apply the same localization to the finite truncation filtration, or use the [derived interval-gluing calculation](../../sheaf-proof-readings/src/SH03/constructible-gluing-on-an-interval.md#cohomology-of-the-whole-interval). The arm cohomology complexes vanish, so the restriction map to the zero stalk is an isomorphism. This proves (19) as the actual restriction map, with the outside endpoints included. It does not compute compact cohomology of the open arms as if both endpoints were deleted.

The finite plus ball corresponds to
\[
 t>\tau(a),\qquad \tau(a)=(1+a^2)^{-1/2}.
 \qquad\text{(20)}
\]
Use the localization triangle with first term the open extension from \(\{t>\tau(a)\}\) and third term the ordinary closed restriction \(F'_{\{t\le\tau(a)\}}\). The latter is a tensor cutoff, not the supported functor \(R\Gamma_{\{t\le\tau(a)\}}F'\). Projection formula for the closed constant sheaf, or closed proper base change on the coefficient support, gives \(Rg_*F'_{\{t\le\tau(a)\}}\simeq H_{\{t\le\tau(a)\}}\). Since \(H\) vanishes on \(t\le0\), its remaining closed support lies in \([0,\tau(a)]\). Its global complex is therefore \(R\Gamma([-\tau(a),\tau(a)];H)\), which is zero when \(0<\tau(a)<\epsilon_0\), by (19).

All coefficient supports in this triangle are compact. Under (18), proper-support composition identifies the full term with \(R\Gamma_c(Z_{\infty,b};F)\), and (20) identifies its open-cutoff term with \(R\Gamma_c(Z_{a,b};F)\). Its first arrow is the forward open-extension map (17), not a restriction in the opposite direction. The vanishing third term proves that this particular arrow is an isomorphism for every sufficiently large \(a\).

If \(V_+=0\), the plus ball and plus cylinder are both a point, and (17) is the identity. The proof needs no fictitious sphere in that case.

## The stabilized operator is compact pullback on the expanding fibre

Let \(q:V_+\oplus V_-\to V_-\), \(H=Rq_!F\). Proper-support base change and (9) give
\[
 \begin{aligned}
 R\Gamma_c(Z_{a,b};F)
 &\xrightarrow{\sim}R\Gamma_c(Z_{\infty,b};F)\\
 &\simeq R\Gamma(\overline B_b^-;H)
 \xrightarrow{\sim}H_0
 \simeq R\Gamma_c(V_+;F|_{V_+}).
 \end{aligned}
 \qquad\text{(21)}
\]
The middle identity integrates along the plus fibres. The minus base is compact, so ordinary and compact sections agree there.

We check the operators in (21). The square with \(q\), \(u\), and \(u_-\) is Cartesian: for a target plus coordinate \(a'\) and a source minus coordinate \(b\), the unique source plus coordinate is \(u_+^{-1}a'\). Hence proper-support base change gives the actual comparison
\[
 u_-^{-1}H\xrightarrow{\sim}Rq_!u^{-1}F
 \xrightarrow{Rq_!\phi}H.
 \qquad\text{(22)}
\]
At zero it is the compact pullback and coefficient map (5) for \(E=V_+\). Invertibility of \(u_+\) supplies the proper fibre map, while no invertibility of \(u_-\) is needed.

On the closed minus ball, (22) acts by ordinary \(u_-\)-pullback followed by restriction from \(u_-^{-1}\overline B_b^-\) to \(\overline B_b^-\). Restriction to its zero germ intertwines this operator with the operator on \(H_0\): both restrictions are the counit for the same point inclusion, and \(u_-(0)=0\).

We verify finite-cutoff compatibility before taking traces. On \(V_+\oplus V_-\) put
\[
 K_a=F_{B_a^+\times V_-},\qquad Q_a=Rq_!K_a,\qquad
 \iota_a:Q_a\longrightarrow H=Rq_!F.
\]
The map \(\iota_a\) is induced by the open-extension counit. The closed support of \(K_a\) lies in \(\overline B_a^+\times V_-\), on which \(q\) is proper. Thus \(Q_a\) is perfect constructible by proper image on coefficient support; no conicity of this finite cutoff is claimed. Closed-base proper-support base change and composition identify \(R\Gamma(\overline B_b^-;Q_a)\) with \(R\Gamma_c(Z_{a,b};F)\), and identify \(R\Gamma(\overline B_b^-;\iota_a)\) with \(\beta_a\), the map (17).

The Cartesian square already checked gives \(u_-^{-1}Q_a\simeq Rq_!u^{-1}K_a\). Its input cutoff is \(u_+^{-1}B_a^+\times V_-\). Apply \(\phi\) there and then open extension into \(B_a^+\times V_-\). After \(Rq_!\) this defines \(d_a:u_-^{-1}Q_a\to Q_a\). If \(d:u_-^{-1}H\to H\) denotes (22), transitivity of open extension and naturality of proper-support base change give the sheaf-morphism identity
\[
 \iota_a d_a=d\,(u_-^{-1}\iota_a).
\]
Indeed, both routes extend the same coefficient map from \(u_+^{-1}B_a^+\times V_-\) directly to all of \(V\). The first extends in two open steps and the second in one; their counits compose.

Now apply ordinary sections on the closed minus ball. For both \(Q_a\) and \(H\), pullback by \(u_-\) first goes to its inverse-image ball and then restricts to \(\overline B_b^-\subset u_-^{-1}\overline B_b^-\), before applying \(d_a\) or \(d\). These natural restriction maps preserve the last displayed square. Under the closed-base comparison, the \(Q_a\) path is exactly the ordinary cutoff operator: the plus map is its open exit, and the minus restriction is its closed entrance. The \(H\) path defines \(U_{\infty,b}\). We obtain
\[
 \beta_a U_{a,b}=U_{\infty,b}\beta_a,
 \qquad
 H_0\text{ carrying }U_{V_+}.
 \qquad\text{(23)}
\]
This is an equality of natural morphisms before stabilization. Once \(a\) is large, \(\beta_a\) is an isomorphism. Equations (16), (21) and (23) prove (6) for \(E=V_+\) under the modulus assumption. They also prove finiteness of every complex used in (21).

## Positive scalar transport removes eigenvalues of unit modulus

Choose \(\eta>0\) smaller than \(1/2\) and than half of each positive number \(|\lambda^{-1}-1|\) for a positive real eigenvalue \(\lambda\) of \(u\). The latter list is finite and none of its entries is zero; if it is empty, impose only the first bound. Put \(I=[1-\eta,1+\eta]\). An eigenvalue \(t\lambda=1\) would require \(\lambda>0\) and \(t=\lambda^{-1}\), which this choice excludes. It also keeps every positive real eigenvalue on its original side of one for every \(t\in I\). Pulling back the inverse of the normalized transport \(p^{-1}F\to\mathrm{scaling}^{-1}F\) along \((v,t)\mapsto(u(v),t)\) gives one morphism on \(V\times I\),
\[
 (tu)^{-1}F\simeq u^{-1}F
 \xrightarrow{\phi}F,
 \qquad\text{(24)}
\]
where the notation on the right includes pullback from \(V\). At \(t=1\) the transport is the identity. The linear-family theorem proves that \(C_0(\phi_t)\) is constant.

The primary subspaces of \(tu\) are the same as those of \(u\). On this single interval every positive real eigenvalue retains its side of one, zero remains zero, and negative or nonreal eigenvalues stay outside the positive forbidden intervals. Thus every fixed expanding space \(E\) remains expanding throughout \(I\); no spectral splitting by modulus is required to stay fixed.

To compare the compact operators, write \(r:E\times I\to I\) and \(N=\mathrm{pr}_E^{-1}(F|_E)\). Proper-support base change for the map \(E\to\mathrm{pt}\) identifies \(Rr_!N\) with the constant complex \((C_E)_I\), including its slice identifications. The map \(a_E(e,t)=(tu_Ee,t)\) is a homeomorphism over \(I\), with inverse \((e,t)\mapsto(t^{-1}u_E^{-1}e,t)\), hence is proper. Its ordinary inverse-image unit identifies \(N\) with \(Ra_{E!}a_E^{-1}N\). Proper-support composition, followed by the restricted family coefficient map (24), therefore gives an endomorphism of \(Rr_!N\). Its slice is exactly the compact pullback and coefficient map \(U_{E,t}\), by proper-support base change.

Ordinary interval descent is fully faithful on constant bounded complexes: under its evaluation identifications an endomorphism of \((C_E)_I\) comes from one endomorphism of \(C_E\). Consequently all these slice operators, and hence their supertraces, agree. This comparison retains any orientation action in compact pullback. Independent coefficient morphisms on separate slices would not give this family endomorphism.

The finitely many values \(t=|\lambda|^{-1}\) for nonzero eigenvalues are the only ones for which \(tu\) has an eigenvalue of modulus one. Choose a nearby value avoiding them. We may therefore apply the hyperbolic proof to \(tu\) and return to \(u\). What remains is to compare the expanding spaces.

## A quotient with no positive eigenvalue has zero ray trace

We first prove a useful trace identity. Let \(A:L\to L\) have no real eigenvalue in \([0,\infty)\), and let \(G\) be conic perfect constructible with \(\psi:A^{-1}G\to G\). Then \(A\) is invertible and
\[
 \operatorname{str}R\Gamma_c(L;\psi)
 =\operatorname{str}(\psi_0).
 \qquad\text{(25)}
\]
The left operator includes proper compact pullback by \(A\).

**Proof.** For \(L=0\), both sides are the same point trace. Suppose \(\dim L>0\). Let \(L^\times=L\setminus\{0\}\) and
\[
 \gamma:L^\times\to S(L)=L^\times/\mathbb R_{>0},
 \qquad \sigma([v])=[Av].
 \qquad\text{(26)}
\]
The sphere \(S(L)\) is compact, and \(\sigma\) is an analytic diffeomorphism. It has no fixed point: a fixed positive ray would give \(Av=cv\) for a real \(c>0\).

Choose a positive definite norm and represent \(S(L)\) by its unit sphere. The maps \(v\mapsto(v/|v|,|v|)\) and \((s,r)\mapsto rs\) are analytic inverse polar coordinates on \(L^\times\). Conicity gives local constancy along the radial parameter. The cylinder theorem identifies \(M=R\gamma_*(G|_{L^\times})\) with the ordinary restriction of \(G\) to the unit sphere and makes the counit \(\gamma^{-1}M\to G|_{L^\times}\) an isomorphism. This proves that \(M\) is bounded perfect constructible by analytic inverse-image closure, without an arbitrary nonproper direct-image finiteness claim. No radial shift occurs.

The linear map sends \((s,r)\) to \((\sigma s,r|As|)\). Here \(\sigma(s)=As/|As|\), so \(\sigma\) and its inverse defined by \(A^{-1}\) are analytic. Pull back the radial counit by \(A\) and use \(\gamma A=\sigma\gamma\). Through the two counits, \(\psi\) becomes a morphism \(\gamma^{-1}\sigma^{-1}M\to\gamma^{-1}M\). Full faithfulness of ordinary radial descent gives one uniquely determined map \(\sigma^{-1}M\to M\). Its evaluation on the unit sphere is precisely the original coefficient map after the positive radius \(|As|\) is identified by normalized transport. Thus the descent retains the induced map, not just the coefficient objects.

It follows that
\[
 R\Gamma(L^\times;G)\simeq R\Gamma(S(L);M)
 \qquad\text{(27)}
\]
intertwines the ordinary pullback operators. The compact-coefficient Lefschetz formula on \(S(L)\), applied to this descended map, gives trace zero: its supported coincidence class has empty support because \(\sigma\) has no fixed point. The closed coefficient support is compact as a closed subset of the sphere, including when \(S(L)=S^0\). Thus the theorem applies to the ordinary endomorphism in (27), not to an unproved trace formula on the noncompact punctured vector space.

The localization triangle \(R\Gamma_{\{0\}}(L;G)\to R\Gamma(L;G)\to R\Gamma(L^\times;G)\xrightarrow{+1}\) has an endomorphism induced by ordinary \(A\)-pullback and \(\psi\). This is a morphism of the actual localization triangle because \(A^{-1}(0)=0\) and \(A\) preserves the complementary open set. Its middle term is \(G_0\) by the ordinary restriction in (9), which intertwines the operator with \(\psi_0\); its last is perfect by (27), so the first is perfect too. Alternating trace is additive on this triangle: in the finite long exact cohomology sequence, image and quotient traces cancel in adjacent degrees. The zero ray trace consequently gives
\[
 \operatorname{str}R\Gamma_{\{0\}}(L;G)
 =\operatorname{str}R\Gamma(L;G)
 =\operatorname{str}(\psi_0).
 \qquad\text{(28)}
\]
Finally the support-inclusion isomorphism in (9) commutes with \(A\)-pullback, since \(A\) is a proper isomorphism preserving zero. It identifies the first trace in (28) with the compact trace in (25). This proves the identity.

## Every expanding space gives the same trace

Let \(E\) be any expanding space and let \(W\) be (4). Set \(L=E/W\), and let \(A\) be the induced map. It has no real eigenvalue in \([0,\infty)\): positive eigenvalues greater than one have been removed with their full primary blocks, eigenvalues in \([0,1)\) were excluded from \(E\), and one is absent throughout. Put \(p:E\to L\), \(K=F|_E\), and \(G=Rp_!K\).

Choose a real linear splitting of \(p\) to identify \(E\) with \(W\oplus L\) for the projection lemma. This splitting commutes with positive scalar multiplication and need not be preserved by \(u_E\). The lemma proves that \(G\) is conic perfect constructible; the induced comparison is the canonical proper direct image and does not depend on the auxiliary splitting.

The square with horizontal map \(p\) and vertical maps \(u_E,A\) is Cartesian. Explicitly, given \(z\in E\) and \(\ell\in L\) with \(p(z)=A\ell\), the unique point above them is \(u_E^{-1}z\): its quotient is \(A^{-1}p(z)=\ell\), since \(u_E\) and \(A\) are invertible. Proper-support base change followed by the restricted coefficient map therefore gives \(A^{-1}G\to G\). Composition of proper-support images identifies its compact pullback operator with \(U_E\). Fibre base change at zero identifies its stalk operator with compact pullback on \(W\) followed by \(\phi|_W\), because \(u_E^{-1}W=W\) and \(u|_W\) is a proper linear isomorphism. Thus the actual operator comparisons are
\[
 R\Gamma_c(L;G)\simeq R\Gamma_c(E;K),
 \qquad
 G_0\simeq R\Gamma_c(W;F|_W).
 \qquad\text{(29)}
\]
The first is the compact operator \(U_E\). The second is \(U_W\), since the fibre over zero is \(W\) and its inverse under \(u_E\) is \(W\). Applying (25) proves
\[
 \operatorname{str}(U_E)=\operatorname{str}(U_W).
 \qquad\text{(30)}
\]

In the hyperbolic case \(V_+\) is itself an expanding space, so (30) compares it and \(E\) through \(W\). The proof of (6) for \(V_+\) consequently proves it for every \(E\). The scalar-family argument then proves (6) without the modulus assumption. This completes the expanding-space theorem.

The comparison is an equality of traces, not an isomorphism between all the complexes \(C_E\). Negative or nonreal directions can change their grading and dimension while contributing no discrepancy in trace. The shrinking-space theorem requires its own supported-cohomology argument and will be proved next.

## Exercises with complete solutions

### Positive intervals include zero

*Difficulty: Introductory.*

For \(u=\operatorname{diag}(3,\tfrac12,-2,0)\), find the smallest and largest expanding and shrinking spaces. Check (3), and decide whether \(uS=S\) for the smallest shrinking space.

**Solution.** Name the coordinate lines \(L_3,L_{1/2},L_{-2},L_0\). The smallest expanding space is \(L_3\), and the largest is \(L_3\oplus L_{-2}\). The smallest shrinking space is \(L_{1/2}\oplus L_0\), and the largest adds \(L_{-2}\). The positive interval \([0,1)\) includes the zero block. The quotient by either shrinking space is invertible, so its inverse image is that space. But \(u(L_{1/2}\oplus L_0)=L_{1/2}\), which is smaller. The restrictions to both expanding spaces are invertible.

### A Jordan block needs another metric

*Difficulty: Intermediate.*

Let \(A(x,y)=(x/2+y,y/2)\). Show that its spectral radius is \(1/2\), although it expands one Euclidean unit vector. Find a norm for which its operator norm is at most \(3/5\).

**Solution.** The matrix is one Jordan block with eigenvalue \(1/2\). It sends \((0,1)\) to \((1,1/2)\), of Euclidean norm \(\sqrt5/2>1\). Put \(|(x,y)|_P^2=x^2/100+y^2\). In coordinates \((x/10,y)\), the matrix is \(\tfrac12 I+N\), where \(N\) has its only nonzero entry \(1/10\) in the upper right. The triangle inequality for operator norms gives \(\|A\|_P\le1/2+1/10=3/5\). Thus the contracting metric is compatible with the spectrum, not with the original coordinate length.

### Orientation remains inside compact pullback

*Difficulty: Intermediate.*

For \(u(x,y)=(-2x,y/2)\) on \(\mathbb R^2\), take \(F=k_{\mathbb R^2}[r]\) and the canonical coefficient map. Compute \(C_0(\phi)\) using \(E=\mathbb R\times\{0\}\).

**Solution.** This \(E\) is expanding: its only eigenvalue is negative, so none lies in \([0,1)\), and the quotient eigenvalue \(1/2\) is not greater than one. Its compact complex is \(k[r-1]\). The reflection \(x\mapsto-2x\) acts by \(-1\) on the compact orientation generator of the line. Therefore the trace is \((-1)^{r-1}(-1)=(-1)^r\). Formula (6) gives this local contribution. Omitting the orientation action would give the wrong sign.

### The stabilization map has a direction

*Difficulty: Intermediate.*

For constant coefficients on \(V_+\oplus V_-\), with dimensions \(d_+,d_-\), calculate both sides of (17). Explain why an open half interval at infinity contributes zero in its proof.

**Solution.** The open plus ball has compact cohomology \(k[-d_+]\), while the compact closed minus ball has ordinary and compact cohomology \(k\). Both the finite box and infinite cylinder consequently have compact complex \(k[-d_+]\). The forward open-extension map preserves the consistently oriented plus generator and is the identity on the minus factor, hence is an isomorphism. In the compactification proof, an arm such as \((0,\epsilon]\) is open inside \([0,\epsilon]\). Its extension by zero fits into the triangle from the constant closed-interval complex to its value at zero. Their ordinary section map is the identity, so the arm term is zero. Compact cohomology of the open interval \((0,\epsilon)\), which is \(k[-1]\), is a different calculation.

### A negative eigenvalue removes the ray contribution

*Difficulty: Advanced.*

Apply (25) to \(A(x)=-2x\) on \(\mathbb R\) with \(G=k_{\mathbb R}\). Calculate the action on each term of localization at zero and on the positive-ray sphere.

**Solution.** The sphere is the two-point set \(S^0\); \(A\) swaps its points. Its ordinary section complex is \(k^2\) in degree zero and has trace zero. Ordinary sections on the line are \(k\), with action \(+1\). The zero costalk is \(k[-1]\), and reflection acts by \(-1\) on its orientation generator, giving alternating trace \(+1\). Its support-inclusion map identifies it with \(R\Gamma_c(\mathbb R;k)=k[-1]\), with the same action. Thus localization has traces \(1=1+0\), and the compact trace equals the stalk trace as asserted. The two complexes are not isomorphic.

### Rotation can be deformed across modulus one

*Difficulty: Advanced.*

Let \(u\) be rotation by \(\pi/2\) on \(\mathbb R^2\), \(F=k_{\mathbb R^2}\), and \(\phi\) canonical. Explain why (6) applies even though both eigenvalues have modulus one, and compute the contribution.

**Solution.** The eigenvalues are \(i,-i\), so one is absent and the zero subspace is expanding. Its compact complex is \(k\) with the identity operator; the contribution is one. For the intermediate proof, the family \(tu\), for positive \(t\) close to one, never has eigenvalue one. For \(t<1\) both directions are contracting, while for \(t>1\) both are expanding by modulus. In the latter case compact cohomology is \(k[-2]\), and the orientation-preserving rotation/dilation acts by \(+1\), still giving trace one. The normalized scalar family gives the same local class on both sides and at \(t=1\).

### Different expanding spaces can have different complexes

*Difficulty: Advanced.*

For \(u=-\mathrm{id}\) on \(\mathbb R^n\), \(n>0\), and constant \(F\), compare the expanding spaces \(0\) and \(\mathbb R^n\). Verify (30) without claiming their compact complexes are isomorphic.

**Solution.** Both spaces are expanding because the eigenvalue \(-1\) belongs to neither positive forbidden interval. The point space gives \(k\) in degree zero with trace one. The entire space gives \(k[-n]\). The proper pullback acts on its compact orientation generator by \(\operatorname{sgn}\det(-I)=(-1)^n\). Its alternating trace is \((-1)^n(-1)^n=1\). For \(n>0\), their nonzero cohomology occurs in different degrees, so they are not isomorphic. Equality of trace is exactly the conclusion of the quotient argument.

## Source context and the next localization theorem

Y. Ike, Y. Matsui and K. Takeuchi, [*Hyperbolic localization and Lefschetz fixed point formulas for higher-dimensional fixed point sets*](https://arxiv.org/abs/1504.04185v2), arXiv 1504.04185v2, 25 May 2015, §5, Definitions 5.2–5.4, define expanding subbundles and the compact-fibre operator. Proposition 5.5 states the associated component trace formula; its proof is omitted there. These constructions form part of Kashiwara's Lefschetz theory. The point proof above supplies the mixed-box stabilization, its operator comparison, the normalized scalar family and the positive-ray trace argument.

The next lesson proves the shrinking-space formula using supported cohomology, then derives the complex stalk and local-isomorphism costalk formulas. Compact pullback on an expanding space and ordinary supported pullback on a shrinking space are different operations, even when their alternating traces agree.
