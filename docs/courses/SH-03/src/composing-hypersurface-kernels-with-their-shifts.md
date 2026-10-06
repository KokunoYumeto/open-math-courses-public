# Composing hypersurface kernels with their shifts

Two hypersurfaces can define sheaf operators whose composite is again supported on a submanifold. The output coefficient complex is easy to predict: tensor the two input coefficients. The degree is subtler. It depends on the intermediate dimension, the codimension of the output submanifold, and an ordered inertia index of three Lagrangian planes.

Use Normal forms and the shift of a submanifold transform and Microlocal composition at prescribed covectors. Coefficients lie in \(D^b(k)\) for a commutative ring \(k\) of finite global dimension. All statements concern local germs at the indicated covectors. Ordinary global convolution requires its own support and admissibility checks.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

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

Here is why the stronger assertion follows from the same calculation. The diagonal cotangent correspondence imposes equality of the two middle base components and then sums their physical middle covectors. An obstruction to regularity of its first restriction is a vertical middle tangent vector \(v\) in the kernel just tested. The subsequent zero-middle-covector restriction has an obstruction which is a horizontal middle vector in that kernel. Both vanish because the entire kernel is zero. These are the usual annihilator criteria for the two linear transversality statements. Thus the successive cotangent restrictions are regular and have no residual middle tangent direction. Their symplectic reductions yield exactly the Lagrangian image already calculated. \(\square\)

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

The linear Lagrangian-relation composition theorem makes both subspaces Lagrangian; it applies also when these endpoint-plane intersections have excess. That precise linear statement is a geometric prerequisite. All middle planes in (5) are viewed in \(E_Y\), with its original symplectic form. The index in (4) is

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

Nonzero \(p_Y\) also gives \(d_Yh_1\ne0\), making \(f\) a submersion near the chosen base point. This uses the middle covector as well as the endpoints. The cotangent transversality proved above descends through the closed embedding of \(W\): the pulled-back target cotangent bundle meets \(T_N^*W\) transversely, and its conormal image is (3). Its selected covector in \(T^*W\) is nonzero, since its ambient lift has a nonzero \(Z\) component whereas the normal of \(W\) has zero \(Z\) component.

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

We must identify (9) with kernel-germ composition. Product base neighborhoods form a basis in \(B\), and their intersections with \(W\) form a basis in \(W\). For such a neighborhood the closed-embedding projection formula identifies its ordinary image in (9) with the ordinary convolution of the two restricted kernels, restricted to the endpoint base neighborhoods. The local conormal projection in the first part of this lesson is injective, so the chosen middle covector is isolated. Apply the refined cutoff and formal-comparison theorem of pointwise kernel composition. It makes the comparisons from these restricted images to the denominator convolution system invertible in the output germ category. As in that theorem, the identification is established after tensor and direct image, using common refinements; no false cofinality of ordinary base restrictions among all microlocal denominators is required. Thus (9) is precisely the left side of (4).

At this stage the normal-form formula already gives

\[
\delta=\frac12[1+\dim S-\dim W-\tau_W]
=1-\frac12[\dim Y+\operatorname{codim}S+\tau_W],
\qquad\text{(10)}
\]

since \(\dim W=\dim X+\dim Y+\dim Z-1\). Here \(\tau_W\) is the ordered vertical/conormal/pulled-target-vertical index in \(T^*W\). The absence of null directions removed the excess term in that formula. It remains to prove \(\tau_W=\tau\). \(\square\)

## Keeping the index order through reduction

Use the inertia-index reduction rule: an isotropic subspace contained in the sum of the three pairwise intersections may be reduced without changing the index. We also use its additivity under orthogonal sums and its sign change under reversal of the symplectic form. These are the exact index prerequisites, rather than a free choice of a Maslov sign convention.

First lift the three planes defining \(\tau_W\) to the cotangent tangent space of \(B\). The isotropic line generated by the normal of the embedding \(W\hookrightarrow B\) lies in the vertical plane and in the conormal tangent of \(N\): it is the radial multiplier direction for the first hypersurface. It is consequently contained in one of the required pairwise intersections. Reducing it gives the three planes on \(T^*W\), so the index agrees before and after this reduction.

Next lift to the space

\[
E_X\oplus E_Y^a\oplus E_Y\oplus E_Z^a
\qquad\text{(11)}
\]

at the physical point \((p_X,p_Y^a,p_Y,p_Z^a)\). The middle diagonal cotangent correspondence is the other isotropic reduction. Its normal subspace lies in the vertical plane and in the lifted target-point/diagonal plane, which already suffices for the pairwise-intersection condition. The reduced triple is exactly the ambient triple just described on \(B\). Before reduction its planes can be written

\[
V_X\oplus V_Y^a\oplus V_Y\oplus V_Z^a,
\qquad \lambda_1\oplus\lambda_2,
\qquad V_X\oplus\Delta_Y\oplus V_Z^a,
\qquad\text{(12)}
\]

in that order. Here \(\Delta_Y\) is the diagonal Lagrangian of \(E_Y^a\oplus E_Y\). The first is vertical; the second is the product conormal tangent; the third represents the pulled-back endpoint vertical plane with the middle equality constraint.

Reduce the endpoint vertical subspaces \(V_X\) and \(V_Z^a\). They are common to the first and third planes, so the index rule applies. Formula (5) identifies the middle reduction of the second plane. We obtain

\[
\tau_W=\tau_{E_Y^a\oplus E_Y}
(V_Y^a\oplus V_Y,\alpha_1^a\oplus\alpha_2,\Delta_Y).
\qquad\text{(13)}
\]

The diagonal identity for the inertia index transforms this into the four-plane index
\(\tau_{E_Y}(V_Y,V_Y,\alpha_2,\alpha_1)\).
By its definition as the sum of two triangle indices, the first triangle with two equal planes is zero. The result is \(\tau_{E_Y}(V_Y,\alpha_2,\alpha_1)\), which is (6). This completes the proof of (4), with the index order unchanged through every reduction.

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

A local graph kernel satisfies the fixed-output condition of the universal kernel class, so these are identities of composable kernel germs and give inverse functors on the two point-localized sheaf categories. On sufficiently small paired cotangent regions, the two selected-region containment and properness conditions of the contact-kernel criterion also hold. The constant hypersurface kernel is cohomologically constructible there and its actual microlocal identity map is the conormal coefficient identity. That criterion then supplies regional inverse equivalences and microlocal-Hom transport. This last extension uses the additional regional checks, rather than converting a point-germ statement into a global claim. \(\square\)

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

The composition of hypersurface kernels and the shift given by the inertia index are part of Kashiwara and Schapira's theory of simple sheaves; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §7.1 (the index of three Lagrangian planes) and §§7.2–7.4. The linear Lagrangian-composition and inertia-index reductions used here are proved in Appendix A.
