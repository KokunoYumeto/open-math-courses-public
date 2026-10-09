# Composing hypersurface kernels with their shifts

Two hypersurfaces can define sheaf operators whose composite is again supported on a submanifold. The output coefficient complex is easy to predict: tensor the two input coefficients. The degree is subtler. It depends on the intermediate dimension, the codimension of the output submanifold, and an ordered inertia index of three Lagrangian planes.

Use [Normal forms and the shift of a submanifold transform](normal-forms-and-the-shift-of-a-submanifold-transform.md) and the [formal kernel-composition proof](../../microlocal-composition-and-pure-sheaves/src/microlocal-composition-at-prescribed-covectors.md#why-the-formal-composition-is-a-bounded-germ). Coefficients lie in \(D^b(k)\) for a commutative ring \(k\) of finite global dimension. All statements concern local germs at the indicated covectors. Ordinary global convolution requires its own support and admissibility checks.

*Written by GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra, September–October 2026. Independently written exposition is public domain (CC0); cited human works retain their own terms.*

## Transverse cotangent projections give a local composition

Let \(\Lambda_1\subset T^*(X\times Y)\) and \(\Lambda_2\subset T^*(Y\times Z)\) be smooth conic Lagrangian submanifolds through \((p_X,p_Y^a)\) and \((p_Y,p_Z^a)\). Use the twisted input convention, so that matching uses the maps

\[
p_2^a:\Lambda_1\to T^*Y,
\qquad p_1:\Lambda_2\to T^*Y.
\qquad\text{(1)}
\]

Assume these maps are transverse at the chosen pair: their derivative images together span \(T_{p_Y}T^*Y\). Their fibre product is then a submanifold. After shrinking around the chosen covectors, projection onto the endpoint cotangent bundles identifies it with a smooth Lagrangian germ \(\Lambda\subset T^*(X\times Z)\).

**Proof.** Let \(E_X,E_Y,E_Z\) be the tangent cotangent symplectic spaces at the three selected points, and let
\(\lambda_1\subset E_X\oplus E_Y^a\),
\(\lambda_2\subset E_Y\oplus E_Z^a\)
be the corresponding tangent Lagrangian planes. The superscript on a space changes the sign of its symplectic form; the antipodal derivative gives the identification with the physical input tangent space. The matching linear space has dimension

\[
\dim\lambda_1+\dim\lambda_2-\dim E_Y
=\dim X+\dim Z.
\qquad\text{(2)}
\]

A vector in the kernel of endpoint projection has the form
\((0,v)\in\lambda_1\), \((v,0)\in\lambda_2\).
Isotropy of \(\lambda_1\) makes \(v\) orthogonal to its middle projection; isotropy of \(\lambda_2\) makes it orthogonal to the other middle projection. Transversality says their sum is all of \(E_Y\), hence \(v=0\). The endpoint projection is therefore injective on tangents. The middle symplectic contributions cancel for matched vectors, so its image is isotropic. By (2) it is Lagrangian. The constant-rank theorem makes the projection a local embedding, proving the assertion after shrinking.

We will also use the following consequence in the ambient product. Let
\(\delta:X\times Y\times Z\hookrightarrow X\times Y\times Y\times Z\)
be the middle diagonal. Pullback of \(\Lambda_1\times\Lambda_2\) through its cotangent correspondence is a smooth Lagrangian \(\Lambda_{12}\). The zero-middle-covector lift for \(q_{13}:X\times Y\times Z\to X\times Z\) is transverse to \(\Lambda_{12}\), and its projection gives \(\Lambda\).

To verify both regular restrictions, put \(L=\lambda_1\oplus\lambda_2\) and use one middle cotangent chart. The linear map

\[
m:L\longrightarrow E_Y,\qquad
\bigl((u,v_1),(v_2,w)\bigr)\longmapsto v_2-v_1
\]

is onto by (1). Its base component is therefore onto and imposes equality of the two middle base points regularly. The normal constraint for that cotangent restriction is \(I_D=0\oplus\Delta(V_Y)\oplus0\); its symplectic orthogonal imposes the same base equality. A vector in \(L\cap I_D\) has zero endpoints and equal middle components, so the preceding hidden-middle-kernel argument makes it zero. Thus the quotient map on \(L\cap I_D^\omega\) has injective derivative. After shrinking, its image is the smooth Lagrangian \(\Lambda_{12}\).

On the kernel of the base component of \(m\), its fibre component remains onto \(V_Y\): for any vertical vector, surjectivity of \(m\) supplies a preimage with that fibre difference and zero base difference. This fibre component is unchanged by adding \(I_D\). In the physical cotangent quotient it is the sum of the two middle covectors, since the first middle factor was identified antipodally. Consequently the zero-middle-covector equation is regular on \(\Lambda_{12}\). Its endpoint reduction is the Lagrangian already calculated, with no residual middle tangent direction. \(\square\)

This defines the local composition \(\Lambda_1\circ\Lambda_2\). Shrinking selects one germ of the projection; no global injectivity, properness or absence of distant branches has been asserted.

## The hypersurface composition theorem

Take smooth closed hypersurfaces \(S_1\subset X\times Y\) and \(S_2\subset Y\times Z\). Choose **nonzero** \(p_X,p_Y,p_Z\), and let \(\Lambda_i\) be the appropriate conormal pieces. Assume (1) is transverse and their composed germ is

\[
\Lambda_1\circ\Lambda_2=T_S^*(X\times Z)
\quad\text{near }(p_X,p_Z^a)
\qquad\text{(3)}
\]

for a smooth submanifold \(S\subset X\times Z\). In this equality only the germ around the specified conormal is meant.

Let \(L',L''\in D^b(k)\), put \(L=L'\otimes_k^LL''\), and extend the constant coefficients on the two hypersurfaces by zero. Then their germs are microlocally composable, and

\[
L'_{S_1}\circ_\mu L''_{S_2}
\simeq L_S[\delta],
\qquad
\delta=1-\frac12\bigl[\dim Y+\operatorname{codim}S+\tau\bigr].
\qquad\text{(4)}
\]

To define \(\tau\) precisely, let \(V_X,V_Y,V_Z\) be the vertical Lagrangian tangent planes in the three cotangent spaces. Propagate the endpoint vertical planes to the middle space:

\[
\begin{split}
\alpha_1&=\{v\in E_Y:\text{some }u\in V_X
\text{ has }(u,v)\in\lambda_1\},\\
\alpha_2&=\{v\in E_Y:\text{some }w\in V_Z
\text{ has }(v,w)\in\lambda_2\}.
\end{split}
\qquad\text{(5)}
\]

Both spaces in (5) are Lagrangian, including excess endpoint intersections. Here is the exact quotient calculation. For a Lagrangian \(A\) in a \(2n\)-dimensional symplectic space and an isotropic \(I\) of dimension \(d\), put \(e=\dim(A\cap I)\). The map \(A\to I^*\), \(a\mapsto\omega(a,\cdot)|_I\), has rank \(d-e\), since its transpose has kernel \(I\cap A^\omega=I\cap A\). Hence \(A\cap I^\omega\) has dimension \(n-d+e\), and its isotropic image in \(I^\omega/I\) has dimension \(n-d\). It is therefore Lagrangian. This is [linear symplectic reduction, Proposition 2.3](../../AN-04/reconstructions/20261005-restored-phase-space/phase-space-and-generating-families.md#2-linear-geometry-and-reduction), with its rank argument retained.

For \(\lambda_1\subset E_X\oplus E_Y^a\), use \(I=V_X\oplus0\). Then \(I^\omega=V_X\oplus E_Y^a\), the quotient is \(E_Y^a\), and the image is exactly \(\alpha_1^a\). For \(\lambda_2\subset E_Y\oplus E_Z^a\), use \(I=0\oplus V_Z^a\); its quotient is \(E_Y\), and the image is exactly \(\alpha_2\). These identifications require no zero-excess assumption. View both resulting middle planes in \(E_Y\) with its original symplectic form. The index in (4) is

\[
\tau=\tau_{E_Y}(V_Y,\alpha_2,\alpha_1),
\qquad\text{(6)}
\]

where \(\tau\) is the signature index defined in the preceding lesson. The order is \(\alpha_2\) before \(\alpha_1\).

## Reducing the sheaf calculation to a single hypersurface

**Proof of the theorem, apart from the final index identification.** Let \(B=X\times Y\times Z\), and set

\[
W=q_{12}^{-1}S_1,
\qquad N=q_{12}^{-1}S_1\cap q_{23}^{-1}S_2,
\qquad f=q_{13}|_W.
\qquad\text{(7)}
\]

If \(S_i\) is given by a local defining function \(h_i\), nonzero endpoint covectors imply \(d_Xh_1\ne0\) and \(d_Zh_2\ne0\). The two lifted hypersurfaces in \(B\) meet transversely, since a relation between their normals would first vanish in the \(X\) component and then in the \(Z\) component. Thus \(W\) is a hypersurface in \(B\) and \(N\) a hypersurface in \(W\).

Nonzero \(p_Y\) also gives \(d_Yh_1\ne0\), making \(f\) a submersion near the chosen base point. This uses the middle covector as well as the endpoints. We check that the conormal transversality survives passage to \(W\). At the selected ambient cotangent point, let \(I_W\) be the vertical line generated by \(dh_1\). Its orthogonal is the tangent of \(T^*B|_W\). The ambient conormal plane \(A_N=T(T_N^*B)\) lies in \(I_W^\omega\) and contains \(I_W\), because \(N\subset W\); its reduction is \(T(T_N^*W)\).

Let \(C_B\) be the tangent pulled-back target cotangent bundle for \(q_{13}\), defined by zero middle covector. Since \(d_Yh_1\ne0\), \(I_W\cap C_B=0\). The image of \(C_B\cap I_W^\omega\) in the quotient is precisely the pulled-back target cotangent bundle \(C_f\) for \(f\), with unique representatives in \(C_B\). Thus

\[
(A_N/I_W)\cap C_f \simeq A_N\cap C_B.
\]

Indeed, a representative in \(C_B\) of a class from \(A_N/I_W\) differs from a vector of \(A_N\) by \(I_W\subset A_N\), so belongs to \(A_N\) itself; injectivity uses \(I_W\cap C_B=0\). The ambient transversality already proved gives the right side dimension \(\dim X+\dim Z\). In \(T(T^*W)\), the plane \(C_f\) has codimension \(\dim Y-1\), whereas \(A_N/I_W\) has dimension \(\dim W=\dim X+\dim Y+\dim Z-1\). Their intersection has exactly the transverse dimension. This verifies the normal-form theorem's transverse hypothesis on \(W\), and the conormal image remains (3). Its selected covector is nonzero: the ambient lift has a nonzero \(Z\) component, while the normal of \(W\) has zero \(Z\) component.

The constant sheaf on a closed subset is stalkwise flat as a \(k\)-module sheaf. Consequently the tensor of the two lifted hypersurface coefficients is

\[
q_{12}^{-1}L'_{S_1}\otimes^L
q_{23}^{-1}L''_{S_2}\simeq L_N
\quad\text{on }B.
\qquad\text{(8)}
\]

For clarity, this statement does not require \(L'\) or \(L''\) themselves to be flat: their derived coefficient tensor is retained in \(L\). The tensor of the two constant closed-support factors is the constant on their intersection, and then associativity gives (8).

Apply the previous normal-form and direct-image calculation to \(N\subset W\), \(f:W\to X\times Z\), and its conormal image \(T_S^*(X\times Z)\). The intersection here is transverse, so there are no null quadratic directions. The resulting represented formal proper-support image is

\[
\text{“}\!\lim_{U\ni(x_0,y_0,z_0)}\!\text{”}\ Rf_!L_{N\cap U}
\simeq L_S[\delta]
\quad\text{at }(p_X,p_Z^a).
\qquad\text{(9)}
\]

The same selected conormal branch permits replacement of a boundary coefficient by its closed upper-side coefficient, as proved there.

We must identify (9) with kernel-germ composition. Product base neighborhoods form a basis in \(B\), and their intersections with \(W\) form a basis in \(W\). For such a neighborhood the [closed-embedding projection formula](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-projection-proof-projection-arbitrary-coefficients) and [proper-image composition](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#composing-proper-images-and-preserving-c-softness-proper-image-composition) identify its ordinary image in (9) with the ordinary convolution of the two restricted kernels, restricted to the endpoint base neighborhoods. The local conormal projection in the first part of this lesson is injective, so the chosen middle covector is isolated. The isolated-incidence theorem, (MC.26)–(MC.28), supplies a confined representative with the actual direct-image comparisons. Applying the [formal kernel-composition proof, (7)–(9)](../../microlocal-composition-and-pure-sheaves/src/microlocal-composition-at-prescribed-covectors.md#why-the-formal-composition-is-a-bounded-germ), makes the comparisons from these restricted images to the denominator convolution system invertible in the output germ category. This identification is established after tensor and direct image, using common refinements; no cofinality of ordinary base restrictions among all microlocal denominators before those operations is assumed. Thus (9) is precisely the left side of (4).

At this stage the normal-form formula already gives

\[
\delta=\frac12[1+\dim S-\dim W-\tau_W]
=1-\frac12[\dim Y+\operatorname{codim}S+\tau_W],
\qquad\text{(10)}
\]

since \(\dim W=\dim X+\dim Y+\dim Z-1\). Here \(\tau_W\) is the ordered vertical/conormal/pulled-target-vertical index in \(T^*W\). The absence of null directions removed the excess term in that formula. It remains to prove \(\tau_W=\tau\). \(\square\)

## Keeping the index order through reduction

Use the [full reduction rule proved in the preceding lesson](normal-forms-and-the-shift-of-a-submanifold-transform.md#reduction-by-an-isotropic-plane-contained-in-two-arguments): a subspace of the sum of the three pairwise intersections may be reduced without changing the index. Its proof includes the common-pair cases used below. The [ordered-index calculation](normal-forms-and-the-shift-of-a-submanifold-transform.md#the-ordered-index-degeneracy-parity-and-the-cocycle) also proves orthogonal-sum additivity, sign reversal and the four-plane cocycle. All reductions retain the convention \(\omega=d\theta\).

First lift the three planes defining \(\tau_W\) to \(T(T^*B)\). They are the ambient vertical plane, \(A_N=T(T_N^*B)\), and \(A_Z=T(T_{Z_B}^*B)\), where \(Z_B=q_{13}^{-1}(x_0,z_0)\) is the middle fibre. The plane \(A_Z\) fixes the endpoint bases and has free middle base, zero middle momentum and free endpoint momenta. The normal line \(I_W\) belongs to the first and second planes: it is the radial multiplier direction for the first hypersurface. The common-pair rule therefore preserves the index.

The first two reductions are the vertical plane of \(T^*W\) and \(T(T_N^*W)\). For the third, \(Z_B\) is transverse to \(W\) because \(d_Yh_1\ne0\). Restricting its conormal to \(W\) gives the conormal of \(Z_B\cap W=f^{-1}(x_0,z_0)\), with tangent

\[
\bigl((A_Z\cap I_W^\omega)+I_W\bigr)/I_W.
\]

This is exactly the pulled-back target vertical plane in the normal-form triple. To see that the restriction is regular, the two defining base constraints are transverse, and \(I_W\cap A_Z=0\) because a vector in \(A_Z\) has zero middle momentum whereas \(dh_1\) does not. Thus its cotangent quotient has no kernel. The third plane need not contain \(I_W\); membership in the first two is all the index proof requires.

Next lift to the space

\[
E_X\oplus E_Y^a\oplus E_Y\oplus E_Z^a
\qquad\text{(11)}
\]

at the physical point \((p_X,p_Y^a,p_Y,p_Z^a)\). The middle-diagonal constraint is \(I_D=0\oplus\Delta(V_Y)\oplus0\). Before its reduction, the three planes are the vertical, the product conormal tangent, and the conormal tangent to \(\{x=x_0,\ y_1=y_2,\ z=z_0\}\). In the twisted middle coordinates, equality of the bases and cancellation of physical middle momenta both become equality in \(E_Y^a\oplus E_Y\). Thus they are

\[
V_X\oplus V_Y^a\oplus V_Y\oplus V_Z^a,
\qquad \lambda_1\oplus\lambda_2,
\qquad V_X\oplus\Delta_Y\oplus V_Z^a,
\qquad\text{(12)}
\]

in that order. Here \(\Delta_Y\) is the diagonal Lagrangian of \(E_Y^a\oplus E_Y\). The constraint \(I_D\) lies in the first and third planes, so their common-pair reduction preserves the index. The first reduces to the vertical of \(T^*B\). The second reduces to \(A_N\), by the regular cotangent pullback established above and the transverse intersection of the two hypersurfaces. The third reduces to \(A_Z\): after imposing middle base equality, quotienting the opposite physical middle momenta leaves precisely zero middle momentum and arbitrary middle base. Hence this is the ambient triple used in the preceding reduction to \(W\).

Finally reduce \(V_X\oplus0\oplus0\oplus V_Z^a\). It is common to the first and third planes, and its symplectic quotient is \(E_Y^a\oplus E_Y\). The first plane reduces to \(V_Y^a\oplus V_Y\), the second to \(\alpha_1^a\oplus\alpha_2\) by the explicit quotients proving (5), and the third to \(\Delta_Y\). The index rule therefore gives

\[
\tau_W=\tau_{E_Y^a\oplus E_Y}
(V_Y^a\oplus V_Y,\alpha_1^a\oplus\alpha_2,\Delta_Y).
\qquad\text{(13)}
\]

For completeness, prove the diagonal identity in exactly this order. Let \(V,A,B\) be Lagrangians of \(E\), and in \(F=E^a\oplus E\) set

\[
P=V^a\oplus V,\qquad Q=A^a\oplus B,\qquad
H=A^a\oplus V,\qquad D=\Delta_E.
\]

The ordered cocycle gives

\[
\tau_F(P,Q,D)=\tau_F(P,Q,H)+\tau_F(P,H,D)-\tau_F(Q,H,D).
\]

The first term is zero by orthogonal-sum additivity: its two summands are \(\tau_{E^a}(V,A,A)\) and \(\tau_E(V,B,V)\). For the second, reduce by \(0\oplus V\), common to \(P,H\). Its orthogonal is \(E^a\oplus V\), its quotient is \(E^a\), and the reduced triple is \((V^a,A^a,V^a)\), with zero index. For the last term, reduce by \(A^a\oplus0\), common to \(Q,H\). Its orthogonal is \(A^a\oplus E\), its quotient is \(E\), and its three planes reduce to \((B,V,A)\): the diagonal contributes \(A\). Hence

\[
\tau_{E^a\oplus E}(V^a\oplus V,A^a\oplus B,\Delta_E)
=-\tau_E(B,V,A)=\tau_E(V,B,A).
\]

These quotients and the cocycle do not require transverse intersections. Apply the identity with \(V=V_Y\), \(A=\alpha_1\), \(B=\alpha_2\). Formula (13) becomes exactly (6), completing the proof of (4) with its index order unchanged through every reduction.

The shift is an integer because it is the integer compact-support shift in the normal form. Thus the half in (4) does not allow arbitrary half-integer shifts of complexes. The geometrically realizable dimensions and index satisfy the corresponding parity relation.

## The transpose needs the dimension shift

Let \(X,Y\) have dimension \(n\), and let \(S\subset X\times Y\) be a smooth hypersurface. Suppose its conormal projections to output and twisted input cotangent bundles are local diffeomorphisms at a selected pair of nonzero covectors. Let \(r:X\times Y\to Y\times X\) transpose the factors. In the germ kernel categories, set

\[
K=k_S,\qquad K^{-1}=(r_*k_S)[n-1].
\qquad\text{(14)}
\]

Then

\[
K\circ_\mu K^{-1}\simeq k_{\Delta_X},
\qquad K^{-1}\circ_\mu K\simeq k_{\Delta_Y}.
\qquad\text{(15)}
\]

**Proof.** The two local graph correspondences compose to the diagonal, and their middle maps are transverse because they are local diffeomorphisms. Transposing a physical conormal first gives the opposite selected physical pair; the full conormal is invariant under simultaneous antipodal reversal, so the desired inverse branch is present too. We select that branch in (14).

For the first composition, the two planes \(\alpha_1,\alpha_2\) are identical: both are obtained by transporting the vertical plane at \(p_X\) through the inverse graph to \(E_Y\). Alternation therefore makes (6) zero. The middle dimension is \(n\), and the output diagonal has codimension \(n\). Formula (4) gives \(1-n\). The explicit shift \([n-1]\) in (14) cancels it. Reversing the roles of \(X,Y\) gives the other identity.

A local graph kernel satisfies the [fixed-output condition (14) of the universal kernel class](../../microlocal-composition-and-pure-sheaves/src/microlocal-composition-at-prescribed-covectors.md#kernels-that-act-on-every-incoming-germ), so it acts on every incoming sheaf germ. To use (15) for inverse functors, we also verify the required associativity of these graph actions.

Let \(K\) be a graph kernel from \(Y\) to \(X\), \(H\) a graph kernel from \(Z\) to \(Y\), and \(F\) any bounded sheaf germ at \(p_Z\). Fixing \(p_X\), the first graph forces its middle witness to be \(p_Y\), and the second forces the next witness to be \(p_Z\). No smoothness or size condition on \(\operatorname{SS}(F)\) is needed. If \(F\) is invisible there, germ functoriality makes both actions zero. Otherwise the adjacent pairs and the pairs involving their composites have isolated witnesses at the fixed output covectors; the confined estimate (7) in the [formal composition proof](../../microlocal-composition-and-pure-sheaves/src/microlocal-composition-at-prescribed-covectors.md#why-the-formal-composition-is-a-bounded-germ) preserves this uniqueness for the composites.

Use that proof's incoming replacements and common refinements simultaneously for the three factors. Both parenthesizations are compared, after tensor and proper-support image, with the joint system over the three denominators and neighborhoods of the two selected middle basepoints. Its ordinary terms integrate the three pulled-back factors on the same product. Tensor associativity, the [projection map](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-projection-proof-projection-arbitrary-coefficients), and [proper-image composition](../../constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#composing-proper-images-and-preserving-c-softness-proper-image-composition) identify their two iterated integrals. These ordinary maps commute with every denominator and neighborhood refinement.

Testing against an output germ therefore identifies both formal objects with the same filtered colimit over the joint choices: every finite set of choices has a common refinement. Representability gives the natural comparison

\[
(K\circ_\mu H)\circ_\mu F
\simeq K\circ_\mu(H\circ_\mu F).
\]

Its identity coherence is inherited from the same ordinary maps. In particular the diagonal action is the identity, since restriction to the diagonal and projection from it compose to the identity map. Taking \(H=K^{-1}\) and using the two kernel identities (15) now proves that the two point-localized actions are inverse functors. This is the graph-action case needed here, proved with the output covector fixed.

 For the regional assertion, first choose sufficiently small base neighborhoods and a confined representative of the selected conormal germ. Choose paired cotangent regions on which that representative satisfies both selected-region containments and the corresponding properness conditions in the [contact-kernel criterion, (1)–(3)](../../sheaf-proof-readings/src/SH03/when-a-kernel-quantizes-a-contact-transformation.md#the-correspondence-and-the-identity-condition). The two projections of the retained graph are inverse homeomorphisms, so their restricted projections are proper. The local constant hypersurface representative is cohomologically constructible there, and its actual identity-induced microlocal map is the conormal coefficient identity. The criterion supplies regional inverse equivalences and microlocal-Hom transport. These hypotheses apply to the confined representative; local graph projections at the chosen pair alone would not remove other branches of the original global hypersurface kernel. \(\square\)

Coordinate orientations trivialize the coefficient lines locally in (14). A globally defined inverse on a larger manifold may retain a nontrivial relative orientation line, as in the dual-kernel lesson. The statement here concerns the normalized local constant hypersurface kernel and its selected germ.

## Exercises with complete solutions

### Transversality kills the hidden middle tangent

*Difficulty: Introductory.*

Complete the tangent argument preceding (2): why does a common kernel vector \(v\) pair to zero with both middle projection images, and why must it vanish?

**Solution.** For \((u',v')\in\lambda_1\), pairing it with \((0,v)\in\lambda_1\) gives \(-\omega_Y(v,v')=0\), since \(\lambda_1\) is isotropic. For \((v'',w')\in\lambda_2\), pairing with \((v,0)\) gives \(\omega_Y(v,v'')=0\). The two projection images span \(E_Y\) by transversality. Hence \(v\) pairs to zero with every vector of \(E_Y\), and nondegeneracy of its symplectic form gives \(v=0\).

### The inverse of a local sphere kernel in dimension two

*Difficulty: Intermediate.*

On two copies of \(\mathbb R^2\), take a small hypersurface patch of \(S=\{|x-y|=1\}\) around a selected pair whose conormal defines one contact graph. What is the inverse germ kernel? Compute the composite with the unshifted transpose.

**Solution.** The middle dimension and output diagonal codimension are both two, while the inverse graph makes the index zero. Thus the composite of \(k_S\) and its unshifted transpose is \(k_\Delta[-1]\). The inverse germ is the transpose shifted by \([1]\), exactly \([n-1]\). The small patch and selected branch are part of the question; using the full sphere relation without its local branch selection would require checking other contributing middle points separately.

### A coefficient tensor can annihilate a geometric composition

*Difficulty: Intermediate.*

Take \(k=\mathbb Z\), \(L'=\mathbb Z/2\), and \(L''=\mathbb Z/3\). For any hypersurfaces satisfying the theorem's geometric conditions, compute their coefficient-kernel composition. Does its zero answer contradict (3)?

**Solution.** Resolve \(\mathbb Z/2\) by \([\mathbb Z\xrightarrow{2}\mathbb Z]\). Tensoring with \(\mathbb Z/3\) makes the differential an isomorphism, so \(L'\otimes^L L''=0\). Formula (4) gives the zero kernel. Condition (3) describes the composition of the full geometric conormal relations, not an assertion that every coefficient tensor has that entire set as microsupport. Vanishing coefficients can make the actual microsupport smaller, including empty.

### The index order changes the degree

*Difficulty: Advanced.*

In a normal-form model satisfying the theorem, suppose \(\dim Y=3\), \(\operatorname{codim}S=2\), and the ordered index (6) is one. Calculate \(\delta\). What incorrect degree would result from exchanging \(\alpha_1\) and \(\alpha_2\)?

**Solution.** Formula (4) gives \(\delta=1-(3+2+1)/2=-2\). Exchanging the last two planes negates the index to \(-1\), giving \(1-(3+2-1)/2=-1\). Both expressions are integers, so parity alone would not catch the wrong order. The ordered reduction (12)–(13), rather than an unordered reference to a Maslov index, determines the correct degree.

### A zero middle covector is outside this theorem

*Difficulty: Advanced.*

For \(S_1=\{x=y^2\}\subset\mathbb R_x\times\mathbb R_y\), examine its conormal over \((0,0)\). Can a nonzero output covector there be used in this theorem with a nonzero middle covector? Which part of the reduction fails?

**Solution.** The conormal is \(\lambda(dx-2y\,dy)\), so at \((0,0)\) a nonzero output covector has zero middle covector. The required triple of nonzero selected covectors is absent. In particular \(S_1\to X\) is not a submersion at that point; for \(W=q_{12}^{-1}S_1\), the map \(q_{13}|_W\) cannot supply the submersion used in (7). Such a fold may still have a sheaf-theoretic transform, but its treatment requires the appropriate hypotheses and normal form rather than this hypersurface-composition theorem.

## References

The index and simple-sheaf methods originate in Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985). Definition 7.1.1 and Proposition 7.1.2, printed pp. 121–122 (PDF pp. 124–125), give the ordered signature, cocycle and isotropic-reduction law. Lemma 7.3.2, printed pp. 131–132, proves a general transport identity for Lagrangian relations. Here the endpoint planes are obtained by explicit isotropic reduction, and the diagonal identity is proved directly in the order required by (6).

For the classical sheaf-operation statements, compare Theorem 7.3.1, printed pp. 129–131, and Corollaries 7.3.4–7.3.5, printed pp. 135–138. The latter distinguish a derived-Hom transform with an Ext-vanishing hypothesis from a tensor transform with a Tor-vanishing hypothesis. Both impose their stated support and isolated-incidence conditions. Their degrees use purity normalized so that a constant hypersurface has degree \(1/2\), and their antipodal convention must be retained when comparing index signs.

This lesson instead computes the coefficient complex \(L'\otimes_k^L L''\) without Tor vanishing. Its shift is obtained by reducing the actual tensor convolution to the preceding lesson's compact-support normal form, then following the ordered planes through the middle diagonal. This proves the local statement (4), including coefficient tensors that vanish, with the exact denominator comparisons specified above.

Theorem 7.4.1 and Corollary 7.4.2, printed pp. 138–139 (PDF pp. 141–142), give the classical simple-kernel equivalence and its action on conormal sheaves under the contact-transform hypotheses. The transpose formula here follows from (4) applied to the two inverse graph germs; the paragraph after (15) states the additional conditions used for its regional form.
