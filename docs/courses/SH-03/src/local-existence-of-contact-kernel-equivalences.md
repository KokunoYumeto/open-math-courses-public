# Local existence of contact kernel equivalences

The kernel criterion tells us when a sheaf operator is an equivalence over a cotangent graph. We now obtain such operators locally for an arbitrary homogeneous contact transformation. A common transverse plane in the radial symplectic quotient gives two hypersurface factors. We then check the identity conditions of their sheaf kernels and compose the resulting equivalences.

Use When a kernel quantizes a contact transformation and the localized composition and parameter identities in the preceding kernel lessons. For the geometry, the programme's Clean Lagrangian pairs and common transversals proves the linear common-transversal lemma in Section 4. Prescribed canonical coordinates and isotropic fibers proves the alternating-subspace extension in Lemma 1.1, homogeneous coordinates with their marked tangent-map construction in Theorem 3.1, and constant-rank conormal recognition in Theorem 5.1. These are written AN-04 lessons, with their stated smooth-calculus prerequisites. The two-factor consequence needed here is proved below; no clean-intersection hypothesis on the original contact graph is added.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## The exact geometric input

Let \(X,Y\) have the same dimension \(n\), and let
\(\chi:\Omega_Y\to\Omega_X\)
be a homogeneous contact transformation between open subsets of the punctured real cotangent bundles. Fix \(p_Y\in\Omega_Y\) and \(p_X=\chi(p_Y)\). Its physical kernel graph is

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

The mathematical source for this factorization is the symplectic appendix's Corollary A.2.8. The related normal form for one Lagrangian is A.2.7. The distinction matters: normalizing one Lagrangian alone does not yet give two hypersurface factors for a prescribed contact transformation.

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

## One chart can normalize finitely many conic Lagrangians

The same radial construction can respect several Lagrangians and a transverse auxiliary test plane. Suppose \(\Lambda_1,\ldots,\Lambda_s\) are smooth conic Lagrangian germs through a nonzero \(p\in T^*Y\). Let \(\mu_1,\ldots,\mu_t\) be Lagrangian planes at \(p\) with \(R\notin\mu_j\); a plane transverse to the original vertical plane has this property. There is a single homogeneous contact chart \(\chi_1\) such that its physical graph is a hypersurface conormal germ, every \(\chi_1\Lambda_i\) is a hypersurface conormal germ, and every \(d\chi_1(\mu_j)\) is transverse to the target vertical plane. These are local assertions at the specified nonzero covectors.

**Proof.** In the radial quotient \(\overline E\) above, the original vertical plane and every \(T_p\Lambda_i\) descend to Lagrangian planes. For each \(\mu_j\), the restriction of \(\theta=\omega(R,\cdot)\) to \(\mu_j\) is nonzero: otherwise \(R\in\mu_j^\omega=\mu_j\). Thus \(\mu_j\cap H\) has dimension \(n-1\) and does not contain \(R\). Its injective image in \(\overline E\) is isotropic of dimension \(n-1\), hence Lagrangian.

Choose a common Lagrangian complement to this finite collection. Existence is proved, in the more general countable case, by Proposition 1.2 of the written programme lesson Gaussian lines, densities and invariant symbols. In that proof, each nontransverse locus is a finite union of positive-codimension smooth strata in the real Lagrangian Grassmannian; a finite union cannot cover a chart. Only a finite collection is used here.

Lift the chosen complement to \(L\subset H\) and realize it as the inverse image of the target vertical plane by the same radial-compatible homogeneous chart construction. We have

\[
L\cap V_Y=\mathbb R R,\qquad
L\cap T_p\Lambda_i=\mathbb R R,\qquad
L\cap\mu_j=0.
\]

For the last equality, a vector in the intersection maps to the intersection of the two reduced planes and therefore belongs to \(\mathbb R R\); that line meets \(\mu_j\) only in zero. The first equality gives a hypersurface conormal physical graph, exactly as in the preceding proof. The second gives base-projection rank \(n-1\) for \(\chi_1\Lambda_i\) at the marked point. A nonzero minor and the persistent radial kernel make that rank constant nearby. The written constant-rank conormal-recognition theorem therefore supplies an embedded hypersurface conormal germ for each image. The third equality is precisely the requested auxiliary-plane transversality. Finitely many restrictions of the chart preserve all these conditions at once. In dimension one the radial quotient is zero and the same conclusions follow with \(L=\mathbb R R\). \(\square\)

This also applies to the positive conormal germs of finitely many smooth test level hypersurfaces. Their images have the specified nonzero covector on their conormal ray; rescaling a local defining function by a nonzero constant makes its differential equal that covector. The original test graph is transverse to another conic Lagrangian exactly when their level-conormal tangents intersect only in the radial line. To verify the equivalence, write the level-conormal tangent as the graph-test tangent over base vectors annihilated by \(p\), with the radial line adjoined. The graph-test plane meets the radial line in zero. Any common graph-test vector has base component annihilated by \(p\), because the canonical form vanishes on the conic Lagrangian. Adjoining or removing the radial component gives the asserted equivalence. Homogeneous symplectic maps preserve this quotient condition, so both transformed tests remain transverse. No clean intersection of the several nonlinear Lagrangians is assumed.

## A hypersurface kernel realizes one factor

Suppose a physical graph \(\Lambda\subset T^*(A\times B)\) is an open conormal piece of a smooth hypersurface \(H\), and both projections to the nonzero selected covectors are local diffeomorphisms. Shrink the ordinary base neighborhoods so that \(H\) is closed in their product and given by a defining function \(f\) with \(df\ne0\). Let

\[
K_H=k_H.
\tag{3}
\]

This kernel is cohomologically constructible: locally it is a constant perfect coefficient complex on a smooth closed submanifold. Its microsupport is contained in the full conormal. For nonzero coefficients it equals the full conormal. Its identity-induced self microlocal Hom map is the constant identity on that conormal, by the closed-submanifold formula. Thus the identity condition is satisfied on the chosen piece.

We must still exclude other pieces over either selected region. At the chosen covector, the conormal is \(\lambda\,df\), with \(\lambda\ne0\). Both partial differentials \(d_Af\) and \(d_Bf\) are nonzero there, because the output and twisted input covectors are nonzero. On smaller base neighborhoods their norms have positive lower bounds. An output covector near the specified output direction determines the sign and bounds the magnitude of \(\lambda\) on a normalized cotangent slice. The same assertion holds for an input covector near the specified input direction. Therefore, after shrinking the base neighborhoods and directional regions, every conormal selected by either projection lies in the original local graph piece. A convergent offending sequence would have bounded normalized \(\lambda\), a limit at the chosen base point, and the chosen sign, contradicting the local graph chart.

Within that chart choose output and input regions corresponding under its contact map. Their conormal graph satisfies

\[
\operatorname{SS}(K_H)\cap
\bigl(p_A^{-1}\Omega_A'\cup(p_B^a)^{-1}\Omega_B'\bigr)
\subset\Lambda\cap(\Omega_A'\times(\Omega_B')^a).
\tag{4}
\]

Zero conormal covectors cannot enter these punctured regions. The two projections of this selected graph are homeomorphisms and hence proper. All hypotheses of the contact-kernel criterion are now checked, including the union in (4) and the actual identity map. Consequently \(\Phi_{K_H}\) and its right adjoint are inverse equivalences on these local regions, and they transport microlocal Hom by the corresponding contact map.

## Composition gives the general local equivalence

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

## Exercises with complete solutions

### Why a full conormal has to be cut down

*Difficulty: Introductory.*

For a hypersurface conormal \(\lambda\,df\), explain why choosing only small ordinary base neighborhoods does not select the desired sign of the contact graph. Identify where the proof excludes the unwanted branch.

**Solution.** Every base point of the hypersurface carries both positive and negative nonzero multiples of \(df\). Shrinking the base keeps both signs. The chosen punctured output and input directional neighborhoods select the sign of \(\lambda\), using the nonzero partial differentials. The local graph chart and lower bounds on those partial differentials then exclude other conormals over either selected region. This is the step proving (4); it cannot be replaced by base restriction alone.

### A forward check does not check the input region

*Difficulty: Intermediate.*

Which convolution argument proves each of the two parts of (6)? Why is proving forward containment alone insufficient for the inverse operator?

**Solution.** The ordinary forward microsupport estimate for \(K_2\circ K_1\) proves containment over \(\Omega_X'\). Transpose the factors, reverse their order, and use their forward conditions on antipodal regions to prove containment over \(\Omega_Y'\) after untransposing. The latter is the reverse condition for the right operator. Forward admissibility alone gives the left operator on the selected quotient, but can leave input covectors from outside the chosen input region contributing to it. The inverse/right operator needs its own containment and properness. Both are inherited here from the two factors.

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

The local existence of kernels quantizing a contact transformation is a theorem of Kashiwara and Schapira; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §6.3, and P. Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) (2016). The factorization argument, hypersurface checks, sheaf-composition argument and exercises use the lessons linked above.
