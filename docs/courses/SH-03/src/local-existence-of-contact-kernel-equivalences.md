# Local existence of contact kernel equivalences

A contact transformation specifies how cotangent directions move. To obtain an operator on sheaves, we also need a coefficient complex and the maps that make its two transforms inverse. We construct these data near any chosen nonzero covector, using the coefficient ring and bounded sheaf categories of the contact-kernel criterion.

The argument has three separate tasks. First we factor the contact map into two maps whose physical graphs are hypersurface conormals. Then a constant sheaf on each hypersurface gives a kernel, and we check its identity map and both selected cotangent regions. Finally we compose the two kernels and verify the inverse order and directional-morphism transport. The simultaneous-normalization result at the end extends the geometric construction to finitely many Lagrangians and test planes; it is not needed for the main existence argument.

**Local-existence theorem.** Near a specified nonzero covector, every homogeneous contact transformation admits a bounded sheaf kernel whose microsupport over either selected cotangent region lies in its physical graph. The proper-support transform is an equivalence with inverse its right adjoint, and the equivalence carries microlocal Hom by the contact map. Both cotangent regions and the ordinary base neighborhoods may be restricted in constructing the kernel. The theorem asserts existence, without fixing a unique cohomological shift.

Use [When a kernel quantizes a contact transformation](../../sheaf-proof-readings/src/SH03/when-a-kernel-quantizes-a-contact-transformation.md) together with [localized convolution and its microsupport estimate](../../sheaf-proof-readings/src/SH03/kernels-that-preserve-chosen-cotangent-directions.md#the-localized-composition-theorem) and the [reverse-order identity for right adjoints](../../sheaf-proof-readings/src/SH03/adjoints-of-localized-sheaf-kernels.md#the-order-of-a-composite-right-adjoint). The geometric construction uses four proved linear and coordinate inputs. [Common transverse planes](../../AN-04/reconstructions/20261005-restored-clean-pairs/clean-lagrangian-pairs-and-common-transversals.md#4-linear-pairs-and-a-common-transverse-lagrangian-plane), Corollary 4.2, applies to arbitrary pairs of linear Lagrangian planes. [Alternating-subspace extension](../../AN-04/reconstructions/20261005-restored-prescribed-coordinates/prescribed-canonical-coordinates-and-isotropic-fibers.md#1-extend-an-isometry-of-alternating-subspaces), Lemma 1.1, extends the chosen map on the new vertical plane. The proof of [homogeneous prescribed coordinates](../../AN-04/reconstructions/20261005-restored-prescribed-coordinates/prescribed-canonical-coordinates-and-isotropic-fibers.md#3-retain-degrees-marked-values-and-the-radial-vector), Theorem 3.1, retains its full radial-compatible differential, including through the last coordinate correction. Finally, [constant-rank conormal recognition](../../AN-04/reconstructions/20261005-restored-prescribed-coordinates/prescribed-canonical-coordinates-and-isotropic-fibers.md#5-recognize-conormal-germs-where-the-base-projection-has-constant-rank), Theorem 5.1, identifies the resulting local graphs. Their smooth-calculus prerequisites remain explicit in those proofs. No clean-intersection condition on the original contact graph is needed.

*Original text by GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra, September–October 2026. New original text is public domain (CC0).*

## The exact geometric input

We first solve the geometric task. The intermediate chart must work for both sides of the given contact map, so its vertical tangent plane has to be chosen relative to both original vertical planes.

Let \(X,Y\) have the same dimension \(n\), and let
\(\chi:\Omega_Y\to\Omega_X\)
be a homogeneous contact transformation between conic open subsets of the punctured real cotangent bundles. Fix \(p_Y\in\Omega_Y\) and \(p_X=\chi(p_Y)\). Its physical kernel graph is

\[
\Lambda_\chi=\{(x,y;\xi,-\eta):(x;\xi)=\chi(y;\eta)\}.
\tag{1}
\]

After shrinking around these covectors, there are an \(n\)-manifold \(Z\), a nonzero intermediate covector \(p_Z\), and two contact transformations

\[
\chi_1:\Omega_Y'\longrightarrow\Omega_Z',
\qquad \chi_2:\Omega_Z'\longrightarrow\Omega_X',
\qquad \chi=\chi_2\chi_1,
\tag{2}
\]

whose physical graphs are open conormal pieces of smooth hypersurfaces in \(Z\times Y\) and \(X\times Z\), respectively. Both graph projections are local diffeomorphisms. The domains may be chosen around the specified covectors and then saturated under positive scaling within the original domains.

The factorization requires simultaneous control of the source and output vertical planes. We choose a new vertical plane in their radial quotient, realize it by a homogeneous chart with prescribed differential, and use constant rank to obtain both hypersurfaces. This explains why the construction must control two planes even though each individual conormal normal form concerns one Lagrangian.

## Why two hypersurface factors exist

Write \(R\) for the radial vector at \(p_Y\), \(E=T_{p_Y}T^*Y\), and \(\theta=\iota_R\omega\), where \(\omega=d\theta\). A homogeneous symplectomorphism preserves both \(\omega\) and \(R\), hence also \(\theta\). Set

\[
H=\ker\theta=R^\omega,\qquad
\overline E=H/\mathbb R R.
\]

The radical of \(\omega|_H\) is exactly \(\mathbb R R\): taking the symplectic orthogonal of \(R^\omega\) gives \(\mathbb R R\), which is contained in \(H\). Thus \(\overline E\) is symplectic of dimension \(2n-2\).

Let \(V_Y=\ker d\pi_Y\) at \(p_Y\), and pull the output vertical plane back to this same tangent space:

\[
A=V_Y,\qquad B=(d\chi)^{-1}V_X.
\]

These are Lagrangian \(n\)-planes. Both contain \(R\), because covector dilation is vertical and \(d\chi(R)=R_X\). Therefore both lie in \(H\); their images \(\overline A,\overline B\) in \(\overline E\) are Lagrangian \((n-1)\)-planes. The linear common-transversal lemma gives a Lagrangian \(\overline L\) transverse to both. Lift it to its entire inverse image \(L\subset H\). Then \(L\) has dimension \(n\), is isotropic and hence Lagrangian, and

\[
L\cap A=L\cap B=\mathbb R R.
\]

This uses the linear lemma for arbitrary pairs of planes; it requires neither a clean nonlinear pair nor a constant dimension for their intersection nearby. For \(n=1\), the reduced space is zero and \(L=\mathbb R R\), so the same argument applies.

We next realize \(L\) as the vertical tangent plane of a homogeneous coordinate chart. Choose a linear isomorphism from \(L\) to the vertical plane at \((0,e_1)\in T^*\mathbb R^n\), taking \(R\) to its radial vector \(\partial_{\zeta_1}\). Both restricted alternating forms are zero, so the alternating-subspace extension lemma extends this map to a symplectic isomorphism \(D:E\to T_{(0,e_1)}T^*\mathbb R^n\). The homogeneous-coordinate construction retains any such compatible marked differential: start with no prescribed functions, use \(D\) as the full tangent system in the first step of Theorem 3.1, and retain it in the subsequent flow constructions and final position correction. It gives a homogeneous symplectomorphism \(\chi_1\) near the marked ray with

\[
\chi_1(p_Y)=(0,e_1)=p_Z,\qquad
d\chi_1=D,\qquad Z\subset\mathbb R^n.
\]

Set \(\chi_2=\chi\chi_1^{-1}\). Both maps have nonzero marked covectors and, after restriction, open conic domains. Their physical graphs are embedded conic Lagrangians: the pullback of the product canonical form to either graph is the difference of the output and input canonical forms, which is zero.

The base projection of the first physical graph has kernel

\[
\ker d(\pi_Z\chi_1,\pi_Y)=L\cap A=\mathbb R R.
\]

Its rank is consequently \(2n-1\) at the marked point. A nonzero minor keeps the rank at least \(2n-1\) nearby. The radial direction remains a nonzero kernel vector at every nearby graph point, so its rank is at most \(2n-1\) there. Thus it has constant rank \(2n-1\) on a neighborhood. Constant-rank conormal recognition in the cotangent bundle of \(Z\times Y\) identifies this graph germ with an open conormal piece of an embedded hypersurface \(H_1\).

For the second graph, pull its base-projection kernel back by \(d\chi_1\). It is

\[
\ker d(\pi_X\chi,\pi_Z\chi_1)=B\cap L=\mathbb R R.
\]

The same minor and radial-kernel argument gives constant rank \(2n-1\), hence a hypersurface \(H_2\subset X\times Z\). Conormal recognition asserts a germ near each specified nonzero covector, rather than equality with all signs of the full conormal. The two cotangent projections of each graph are local diffeomorphisms because \(\chi_1,\chi_2\) are local symplectomorphisms. Finally restrict around the specified rays and saturate the resulting charts under positive dilation, as in the homogeneous-coordinate construction. Restrict the three cotangent regions further so that \(\chi_1\) and \(\chi_2\) have the same intermediate region. This proves (2) with all its stated conditions. \(\square\)

## A hypersurface kernel realizes one factor

The factorization has supplied two geometric graphs. We now check what is required to turn either graph into a sheaf equivalence. Conormal shape supplies a candidate kernel; the identity map and the restrictions over both cotangent regions still have to be verified.

Suppose a physical graph \(\Lambda\subset T^*(A\times B)\) is an open conormal piece of a smooth hypersurface \(H\), and both projections to the nonzero selected covectors are local diffeomorphisms. Shrink the ordinary base neighborhoods so that \(H\) is closed in their product and given by a defining function \(f\) with \(df\ne0\). Let

\[
K_H=k_H.
\tag{3}
\]

This kernel is cohomologically constructible: locally it is a constant perfect coefficient complex on a smooth closed submanifold. Its microsupport is contained in the full conormal. For nonzero coefficients it equals the full conormal. Its identity-induced self microlocal Hom map is the constant identity on that conormal, by the closed-submanifold formula. Thus the identity condition is satisfied on the chosen piece.

We must still exclude other pieces over either selected region. At the chosen covector, the conormal is \(\lambda\,df\), with \(\lambda\ne0\). Both partial differentials \(d_Af\) and \(d_Bf\) are nonzero there, because the output and twisted input covectors are nonzero. On smaller base neighborhoods their norms have positive lower bounds. An output covector near the specified output direction determines the sign and bounds the magnitude of \(\lambda\) on a normalized cotangent slice. The same assertion holds for an input covector near the specified input direction. Therefore, after shrinking the base neighborhoods and directional regions, every conormal selected by either projection lies in the original local graph piece. A convergent offending sequence would have bounded normalized \(\lambda\), a limit at the chosen base point, and the chosen sign, contradicting the local graph chart.

Within that chart choose an open input region contained in the safe input region just obtained, small enough that the contact map is defined on it and its image lies in the safe output region. Take the output region to be precisely that image. Any conormal selected over either region lies in the local graph chart by the preceding exclusion argument. Injectivity of its projections then forces its other end to lie in the matching region. Their conormal graph satisfies

\[
\operatorname{SS}(K_H)\cap
\bigl(p_A^{-1}\Omega_A'\cup(p_B^a)^{-1}\Omega_B'\bigr)
\subset\Lambda\cap(\Omega_A'\times(\Omega_B')^a).
\tag{4}
\]

Zero conormal covectors cannot enter these punctured regions. The two projections of this selected graph are homeomorphisms and hence proper. All hypotheses of the contact-kernel criterion are now checked, including the union in (4) and the actual identity map. Consequently \(\Phi_{K_H}\) and its right adjoint are inverse equivalences on these local regions, and they transport microlocal Hom by the corresponding contact map.

## Composition gives the general local equivalence

The two factors can now be assembled. There are three conclusions to keep track of: the microsupport condition over both ends, the inverse functor, and the induced map on directional morphisms.

Apply this construction to the two hypersurfaces in (2), using compatible ordinary base neighborhoods \(X',Z',Y'\) and intermediate cotangent region. Let the resulting kernels be \(K_2\) on \(X'\times Z'\) and \(K_1\) on \(Z'\times Y'\). Form the ordinary proper-support convolution

\[
K=K_2\circ_{Z'}K_1.
\tag{5}
\]

It is a bounded complex by the kernel dimension and coefficient bounds. Both factors are admissible in both directions. Forward closure under convolution and its microsupport estimate put the selected output relation of \(K\) in the graph of \(\chi_2\chi_1\). Applying the same argument to the transposed kernels on the antipodal regions gives the selected input containment too. Hence

\[
\operatorname{SS}(K)\cap
\bigl(p_1^{-1}\Omega_X'\cup(p_2^a)^{-1}\Omega_Y'\bigr)
\subset\Lambda_\chi\cap(\Omega_X'\times(\Omega_Y')^a).
\tag{6}
\]

The localized composition identity gives

\[
\Phi_K\simeq\Phi_{K_2}\Phi_{K_1}.
\tag{7}
\]

Each factor is an equivalence, so the composite is an equivalence. The reverse-order identity for right adjoints gives its inverse
\(\Psi_K\simeq\Psi_{K_1}\Psi_{K_2}\).
For two inputs \(G_1,G_2\), apply directional-morphism transport first for \(K_1\), then for \(K_2\). Composition of the two homeomorphism direct images yields

\[
\chi_*\mu\operatorname{hom}(G_2,G_1)|_{\Omega_X'}
\simeq
\mu\operatorname{hom}(\Phi_KG_2,\Phi_KG_1)|_{\Omega_X'}.
\tag{8}
\]

On the left, \(\chi_*\) is applied to the microlocal Hom restricted to \(\Omega_Y'\). This proves local existence, including both selected microsupport conditions, inverse equivalence and directional-morphism transport.

Only the two hypersurface factors were required to be cohomologically constructible for application of the criterion. The conclusion for their convolution follows from (7) and transport through the two equivalences. This proof does not invoke preservation of constructibility by an arbitrary nonproper direct image, and does not assert it as a general fact.

An inverse pair furnished by the contact-kernel criterion is called an **extended contact transformation** above its cotangent map. The word “extended” refers to its action on sheaf categories and directional morphisms. Its cotangent graph alone does not specify the coefficient complex or cohomological normalization of the operator.

## One chart can normalize finitely many conic Lagrangians

The local-existence theorem is proved. We return to its radial-quotient construction to obtain a useful additional choice of chart when several conic Lagrangians or test planes are prescribed.

The same radial construction can respect several Lagrangians and a transverse auxiliary test plane. Suppose \(\Lambda_1,\ldots,\Lambda_s\) are smooth conic Lagrangian germs through a nonzero \(p\in T^*Y\). Let \(\mu_1,\ldots,\mu_t\) be Lagrangian planes at \(p\) with \(R\notin\mu_j\); a plane transverse to the original vertical plane has this property. There is a single homogeneous contact chart \(\chi_1\) such that its physical graph is a hypersurface conormal germ, every \(\chi_1\Lambda_i\) is a hypersurface conormal germ, and every \(d\chi_1(\mu_j)\) is transverse to the target vertical plane. These are local assertions at the specified nonzero covectors.

**Proof.** In the radial quotient \(\overline E\) above, the original vertical plane and every \(T_p\Lambda_i\) descend to Lagrangian planes. For each \(\mu_j\), the restriction of \(\theta=\omega(R,\cdot)\) to \(\mu_j\) is nonzero: otherwise \(R\in\mu_j^\omega=\mu_j\). Thus \(\mu_j\cap H\) has dimension \(n-1\) and does not contain \(R\). Its injective image in \(\overline E\) is isotropic of dimension \(n-1\), hence Lagrangian.

Choose a common Lagrangian complement to this finite collection. Proposition 1.2 of [Gaussian lines, densities and invariant symbols](../../AN-04/reconstructions/20261005-restored-gaussian-symbols/gaussian-lines-and-invariant-symbols.md#1-charts-and-intersection-strata-of-lagrangian-planes) proves the stronger countable statement: symmetric-matrix charts identify the fixed-intersection strata by Schur-complement equations, and the proof shows that the union of the nontransverse strata has measure zero in a chart. A plane outside that union is a common complement. Only the finite case is used here, and the zero-dimensional reduced space has its unique zero plane as complement.

Lift the chosen complement to \(L\subset H\) and realize it as the inverse image of the target vertical plane by the same radial-compatible homogeneous chart construction. We have

\[
L\cap V_Y=\mathbb R R,\qquad
L\cap T_p\Lambda_i=\mathbb R R,\qquad
L\cap\mu_j=0.
\]

For the last equality, a vector in the intersection maps to the intersection of the two reduced planes and therefore belongs to \(\mathbb R R\); that line meets \(\mu_j\) only in zero. The first equality gives a hypersurface conormal physical graph, exactly as in the preceding proof. The second gives base-projection rank \(n-1\) for \(\chi_1\Lambda_i\) at the marked point. A nonzero minor and the persistent radial kernel make that rank constant nearby. The written constant-rank conormal-recognition theorem therefore supplies an embedded hypersurface conormal germ for each image. The third equality is precisely the requested auxiliary-plane transversality. Finitely many restrictions of the chart preserve all these conditions at once. In dimension one the radial quotient is zero and the same conclusions follow with \(L=\mathbb R R\). \(\square\)

This also applies to the positive conormal germs of finitely many smooth test level hypersurfaces. Their images have the specified nonzero covector on their conormal ray; rescaling a local defining function by a nonzero constant makes its differential equal that covector. The original test graph is transverse to another conic Lagrangian exactly when their level-conormal tangents intersect only in the radial line. To verify the equivalence, write the level-conormal tangent as the graph-test tangent over base vectors annihilated by \(p\), with the radial line adjoined. The graph-test plane meets the radial line in zero. Any common graph-test vector has base component annihilated by \(p\), because the canonical form vanishes on the conic Lagrangian. Adjoining or removing the radial component gives the asserted equivalence. Homogeneous symplectic maps preserve this quotient condition, so both transformed tests remain transverse. No clean intersection of the several nonlinear Lagrangians is assumed.

## Exercises with complete solutions

### Why a full conormal has to be cut down

*Difficulty: Introductory.*

For a hypersurface conormal \(\lambda\,df\), explain why choosing only small ordinary base neighborhoods does not select the desired sign of the contact graph. Identify where the proof excludes the unwanted branch.

**Solution.** Every base point of the hypersurface carries both positive and negative nonzero multiples of \(df\). Shrinking the base keeps both signs. The chosen punctured output and input directional neighborhoods select the sign of \(\lambda\), using the nonzero partial differentials. The local graph chart and lower bounds on those partial differentials then exclude other conormals over either selected region. This is the step proving (4); it cannot be replaced by base restriction alone.

### A forward check does not check the input region

*Difficulty: Intermediate.*

Which convolution argument proves each of the two parts of (6)? Why is proving forward containment alone insufficient for the inverse operator?

**Solution.** The ordinary forward microsupport estimate for \(K_2\circ K_1\) proves containment over \(\Omega_X'\). Transpose the factors, reverse their order, and use their forward conditions on antipodal regions to prove containment over \(\Omega_Y'\) after untransposing. The latter is the reverse condition for the right operator. Forward admissibility alone gives the left operator on the selected quotient. It does not exclude pairs whose input lies in the chosen input region but whose output lies outside the chosen output region. The right operator could then depend on output data discarded by localization. The inverse/right operator needs its own containment and properness. Both are inherited here from the two factors.

### The order of the inverse

*Difficulty: Intermediate.*

Suppose the two factors act by \(L_1,L_2\) with inverses \(R_1,R_2\). Compute the inverse of \(L_2L_1\), including both identity composites, and compare with the order in (7).

**Solution.** The inverse is \(R_1R_2\). Its composite after \(L_2L_1\) is \(R_1(R_2L_2)L_1\simeq R_1L_1\simeq1\). Its composite before it is \(L_2(L_1R_1)R_2\simeq L_2R_2\simeq1\). The kernel convolution is ordered as \(K_2\circ K_1\), so its input first passes through \(K_1\). Its right operator first returns through \(\Psi_{K_2}\), then through \(\Psi_{K_1}\), exactly the functor \(\Psi_{K_1}\Psi_{K_2}\).

### A shift is invisible to the cotangent graph

*Difficulty: Advanced.*

Replace \(K_1\) and \(K_2\) by \(K_1[a]\) and \(K_2[b]\). Determine the composite operator, its inverse and its directional-morphism transport. Explain why this does not contradict the local-existence theorem.

**Solution.** Derived tensor and proper-support image give composite kernel \(K[a+b]\) and operator \(\Phi_K[a+b]\). Its inverse is \(\Psi_K[-a-b]\). Shifts leave all microsupports and graph projections unchanged. Simultaneously shifting both arguments of microlocal Hom cancels the degree difference, so (8) remains the same directional transport isomorphism. The theorem asserts existence of an equivalence above the contact map; it does not prescribe a unique shift. Identifying the possible coefficient and shift changes belongs to the further study of quantizations above the identity.

### An auxiliary plane must avoid the radial line

*Difficulty: Advanced.*

At \(p=(0;(1,0))\in T^*\mathbb R^2\), use tangent coordinates \((x_1,x_2;\xi_1,\xi_2)\). Let \(V\) be vertical, let \(A=\operatorname{span}(\partial_{\xi_1},\partial_{x_2})\), and let \(\mu\) be horizontal. In the radial quotient choose the line \(\xi_2=t x_2\). Which values of \(t\) are allowed, what is its lift \(L\), and why is the condition \(R\notin\mu\) necessary in the simultaneous-normalization theorem?

**Solution.** The radial vector is \(R=\partial_{\xi_1}\), and \(R^\omega=\{x_1=0\}\). The quotient has coordinates \((x_2,\xi_2)\), form \(d\xi_2\wedge dx_2\), and reduced planes \(\overline V=\{x_2=0\}\), \(\overline A=\{\xi_2=0\}\), and \(\overline\mu=\{\xi_2=0\}\). Every finite \(t\ne0\) gives a line transverse to all three. Its lift is
\(L=\operatorname{span}(\partial_{\xi_1},\partial_{x_2}+t\partial_{\xi_2})\).
It is Lagrangian, satisfies \(L\cap V=L\cap A=\mathbb R R\), and meets \(\mu\) in zero. At \(t=0\), it equals \(A\) and meets \(\mu\) in the \(x_2\) line, so the required normalization fails. If an auxiliary plane contained \(R\), every radial-compatible inverse vertical plane would meet it in that same nonzero vector. No homogeneous chart could then make it transverse to the target vertical. Avoiding the radial line is therefore necessary, rather than a convenient extra assumption.

## References

The local-existence theorem and its construction through two hypersurface conormals are classical: see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Theorem 6.3.5, printed pp. 113–114. Its proof states the geometric factorization and then composes the hypersurface kernels. Proposition 6.3.3 and Theorem 6.3.4, printed pp. 110–113, supply the composition and equivalence antecedents; the latter requires the Lagrangian graph, constructibility and identity-induced microlocal endomorphism conditions checked here for each factor. Theorem 6.3.9 and Corollary 6.3.11, printed pp. 115–117, give directional-morphism transport. P. Schapira’s [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) (2016), Corollary 5.13 on p. 29, repeats the two-factor reduction without its full geometric proof. Here that geometric proof is supplied through the linked symplectic constructions and the written radial quotient argument; the finite-family extension additionally uses the linked common-complement proof. Those providers retain their own human-source credit. The two separate support checks, marked-differential calculation, inverse-order calculation and worked exercises explain the classical construction in the programme’s bounded coefficient scope. Human sources retain their own terms; CC0 applies to the independently expressed programme text.