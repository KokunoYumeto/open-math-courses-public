# The partial Legendre kernel and its adjoint shift

The partial Legendre transformation exchanges some position coordinates with ratios of covector coordinates. Its kernel is supported on a smooth incidence equation. We will derive both the contact map and the shift that makes its right adjoint carry one coordinate subspace to a hypersurface. Calculating the right adjoint is essential: the unshifted transposed kernel and the relative dual kernel initially have different degrees.

Use the [contact-kernel criterion and its identity condition](../../sheaf-proof-readings/src/SH03/when-a-kernel-quantizes-a-contact-transformation.md#the-correspondence-and-the-identity-condition) and the [relative-dual adjunction comparison](../../sheaf-proof-readings/src/SH03/dual-kernels-and-an-unchanged-parameter.md#relative-duals-point-to-different-adjoints). We verify the criterion on the full regions in (1)–(2), identify its actual identity map, and retain the orientation line and evaluation map in the right adjoint. The [closed-submanifold Hom comparison](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-submanifold--recovering-microlocalization-from-hom), [supported-coefficient microlocalization](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-examples--three-checks-with-arbitrary-coefficient-modules), and closed-embedding orientation formula are used in their stated ranges. Their deeper sheaf-operation prerequisites remain in force.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## The coordinate transformation and its inverse

Let \(X=Y=\mathbb R^n\), with \(n\geq1\), and choose \(0\leq p<n\). Put
\(I=\{1,\ldots,p\}\), \(J=\{p+1,\ldots,n-1\}\), and \(r=|J|=n-p-1\). Empty sums are zero. On
\(\Omega_X=\{\xi_n\ne0\}\) define

\[
\begin{aligned}
y_k&=x_k,&\eta_k&=\xi_k &&(k\in I),\\
y_j&=\xi_j/\xi_n,&\eta_j&=-x_j\xi_n &&(j\in J),\\
y_n&=x_n+\sum_{j\in J}x_j\xi_j/\xi_n,&\eta_n&=\xi_n.
\end{aligned}
\qquad\text{(1)}
\]

Thus the last base coordinate is also
\(y_n=(\sum_{j=p+1}^n x_j\xi_j)/\xi_n\); its sum includes \(j=n\). The image lies in \(\Omega_Y=\{\eta_n\ne0\}\). Solving these equations gives

\[
\begin{aligned}
x_k&=y_k,&\xi_k&=\eta_k &&(k\in I),\\
x_j&=-\eta_j/\eta_n,&\xi_j&=y_j\eta_n &&(j\in J),\\
x_n&=y_n+\sum_{j\in J}\eta_jy_j/\eta_n,&\xi_n&=\eta_n.
\end{aligned}
\qquad\text{(2)}
\]

Substitution in either direction gives the identity. Both maps are smooth on the indicated open sets. Their base coordinates are unchanged by positive cotangent scaling, and their output covectors scale by the same factor. Hence (1) defines a homogeneous diffeomorphism \(\chi:\Omega_X\to\Omega_Y\).

It preserves the tautological form exactly. In fact, using \(y_j=\xi_j/\xi_n\),

\[
\begin{aligned}
\sum_i\eta_i\,dy_i
&=\sum_{k\in I}\xi_k\,dx_k
-\sum_{j\in J}x_j\xi_n\,dy_j
+\xi_n\,d\left(x_n+\sum_{j\in J}x_jy_j\right)\\
&=\sum_{k\in I}\xi_k\,dx_k+\xi_n\,dx_n
+\sum_{j\in J}\xi_n y_j\,dx_j
=\sum_i\xi_i\,dx_i.
\end{aligned}
\qquad\text{(3)}
\]

The terms in \(dy_j\) cancel before taking an exterior derivative. Thus \(\chi^*\theta_Y=\theta_X\), and \(\chi\) is a contact transformation in the homogeneous symplectic convention used by the course.

## Deriving the conormal graph

In \(P=X\times Y\), set

\[
S=\left\{x_k-y_k=0\ (k\in I),\quad
h=x_n-y_n+\sum_{j\in J}x_jy_j=0\right\}.
\qquad\text{(4)}
\]

The differentials of these \(p+1\) equations are linearly independent: the \(dy_k\) coordinates distinguish the first \(p\), and the \(dy_n\) coefficient of \(dh\) is \(-1\). This proves that \(S\) is closed and smooth of codimension \(p+1\). A conormal is
\(\sum_{k\in I}a_k\,d(x_k-y_k)+b\,dh\).
Its physical components are

\[
\begin{array}{c|ccc}
&k\in I&j\in J&n\\\hline
\xi& a_k&b y_j&b\\
\zeta&-a_k&b x_j&-b.
\end{array}
\qquad\text{(5)}
\]

The input convention for a kernel on \(X\times Y\) is \(\eta=-\zeta\). For \(b\ne0\), (5) is exactly (1), including \(\eta_j=-x_j\xi_n\). The equation \(h=0\) supplies its last base coordinate. Conversely (1) satisfies (4) and (5) with \(a_k=\xi_k\), \(b=\xi_n\). Therefore the selected conormal relation is the graph of \(\chi\), viewed as a correspondence whose forward kernel direction is from \(Y\) to \(X\). The transformation of \(\Phi_K\) is \(\chi^{-1}\); the transformation of \(\Psi_K\) is \(\chi\).

Let \(\Lambda\) be the part of \(T_S^*P\) with \(b\ne0\). In (5), \(\xi_n=b\) and the twisted input component is \(\eta_n=b\). Hence selecting either \(\Omega_X\) or \(\Omega_Y\) selects exactly this same \(\Lambda\); all covectors with \(b=0\), including those with nonzero \(a_k\), miss both regions. This proves the required union condition, rather than only its restriction to a product of selected regions. The set \(\Lambda\) is relatively closed in that product, as the graph of the continuous map (1). Its two projections are diffeomorphisms by (1)–(2) and therefore proper homeomorphisms. Explicitly, above a compact set in either cotangent region the denominator \(|\xi_n|=|\eta_n|\) is bounded away from zero, and the relevant inverse formulas bound every other base and covector coordinate. This compactness is on the selected cotangent relation; the ordinary projection of the entire support \(S\) need not be proper.

For any integer \(d\), let \(K_d=k_S[d]\). Here \(k\) is a commutative ring with identity and finite global dimension, and all input complexes are bounded. We check the precise cohomological constructibility required by the criterion. In an adapted product chart, \(S\) is a coordinate subspace. A cofinal family of small product balls has ordinary coefficient cohomology \(k[d]\) on its intersection with \(S\), and compact-support cohomology \(k[d-\dim S]\) after a local orientation choice. The coordinate-ball calculation and its support maps identify the actual restriction and extension maps with the corresponding identity maps. Thus the formal ordinary and compact-support systems are represented by these perfect complexes, with the required stalk and costalk comparisons. Off \(S\) both systems are zero. The constructibility condition is imposed on this rank-one kernel, not on the arbitrary objects to which it is applied. The [smooth-submanifold support calculation](../../sheaf-proof-readings/src/SH02/subset-microsupport.md#sh02-sub-smooth-models--submanifolds-and-regular-boundaries) also gives \(\operatorname{SS}(K_d)\subset T_S^*P\). For the zero ring \(K_d=0\), so the inclusion is immediate as well.

To compute its endomorphisms, the [submanifold Hom comparison](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-submanifold--recovering-microlocalization-from-hom) identifies \(\mu\operatorname{hom}(k_S,k_S)\) on the conormal with \(\mu_S(k_S)\). In normal deformation coordinates the support of the positive lift is the zero normal vector at every positive parameter. Its specialization is therefore the constant coefficient on the zero section of \(N_SP\). In the negative Fourier kernel, pairing with that vector is zero for every dual normal covector, and the supported projection has a single point as fibre. The [supported-coefficient calculation](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-examples--three-checks-with-arbitrary-coefficient-modules) consequently gives the constant coefficient on all of \(T_S^*P\), with no fibre dimension shift. Shifting both Hom arguments by \(d\) cancels the shifts. Hence

\[
\mu\operatorname{hom}(k_S[d],k_S[d])|_{T_S^*P}
\simeq k_{T_S^*P}.
\qquad\text{(6)}
\]

The object calculation alone does not verify the contact criterion. Its [microlocal unit](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-composition--directional-composition-identities-and-associativity) is the microlocalization of the diagonal Hom-kernel morphism adjoint to \(\operatorname{id}_{K_d}\). Under closed-embedding Hom adjunction in the preceding comparison, this identity becomes the identity of the constant coefficient on \(S\). Specialization keeps that identity on the zero normal section, and the single-point Fourier projection keeps its value \(1\). Thus the actual map \(e_{K_d}\) is identified in (6) with \(1\mapsto\operatorname{id}_{k[d]}\), and is an isomorphism. The projection orientation and its inverse have already cancelled in the submanifold Hom comparison. The local maps therefore agree on overlaps without a choice of normal orientation.

We have checked cohomological constructibility, both selected-region containments, properness on the same graph, and the identity-induced map. The [contact-kernel theorem](../../sheaf-proof-readings/src/SH03/when-a-kernel-quantizes-a-contact-transformation.md#the-correspondence-and-the-identity-condition) now applies for every \(d\). Its [kernel-unit proof](../../sheaf-proof-readings/src/SH03/when-a-kernel-quantizes-a-contact-transformation.md#the-kernel-unit-is-invertible) identifies the actual adjunction unit with this identity section; constructible duality gives the other fully faithful adjoint and the invertible counit. Consequently these are inverse equivalences through their adjunction maps:

\[
\Phi_{K_d}:\mathcal D_Y(\Omega_Y)\rightleftarrows
\mathcal D_X(\Omega_X):\Psi_{K_d}.
\qquad\text{(7)}
\]

The shift we calculate next normalizes particular objects under these equivalences.

## The two subspaces correspond

Let

\[
M=\{x_{p+1}=\cdots=x_n=0\}\subset X,\qquad
N=\{y_n=0\}\subset Y.
\qquad\text{(8)}
\]

At a point of \(T_M^*X\cap\Omega_X\), the base coordinates \(x_J,x_n\) and the tangent covectors \(\xi_I\) vanish. Formula (1) gives \(y_n=0\), \(\eta_I=\eta_J=0\), and \(\eta_n\ne0\). These are exactly the conditions for \(T_N^*Y\cap\Omega_Y\). Conversely (2) recovers the stated vanishing coordinates from any such point of \(T_N^*Y\). Thus

\[
\chi(T_M^*X\cap\Omega_X)=T_N^*Y\cap\Omega_Y.
\qquad\text{(9)}
\]

The free coordinates \(y_J\) encode the ratios of the normal covectors to \(M\); they are not additional tangent covectors to \(N\).

## The right adjoint and the required degree

Let \(q_Y:P\to Y\). The right relative dual kernel is

\[
Q_d=\mathrm tR\mathcal Hom_P(k_S[d],q_Y^{-1}\omega_Y)
\simeq\mathrm t\left(k_S\otimes\operatorname{or}_{S/P}
\otimes q_Y^{-1}\operatorname{or}_Y\right)[n-(p+1)-d].
\qquad\text{(10)}
\]

Here is the closed-support comparison in (10). For \(i:S\hookrightarrow P\) and the locally constant invertible complex \(W=q_Y^{-1}\omega_Y\), internal adjunction gives

\[
R\mathcal Hom_P(i_*k_S,W)=i_*i^!W.
\]

Locally trivializing \(W\), the normal local-cohomology formula computes \(i^!W=i^{-1}W\otimes\operatorname{or}_{S/P}[-(p+1)]\). The comparison is induced by coefficient multiplication with the normal support class; its transition maps glue as the displayed orientation line. This assertion uses the locally constant target \(W\), rather than asserting that exceptional restriction has this form for every sheaf. Since \(\omega_Y=\operatorname{or}_Y[n]\), dualizing the shift \([d]\) gives the total degree \(n-(p+1)-d=r-d\). Transposing the two base factors is ordinary pullback by a diffeomorphism and introduces no further cohomological degree.

We retain the intrinsic tensor of orientation lines in (10) before choosing generators. The ordered defining functions \((x_1-y_1,\ldots,x_p-y_p,h)\) globally trivialize the normal orientation, and the standard coordinates orient \(Y\). Fix these choices. Reversing one choice changes the resulting line trivialization by its determinant sign, while the intrinsic kernel and its adjunction remain the same. These choices give

\[
Q_d\simeq k_{S^{\mathsf t}}[r-d].
\qquad\text{(11)}
\]

We identify the actual adjunction comparison. Write \(q_X:P\to X\), put \(Q'_d=R\mathcal Hom_P(K_d,W)\), so that \(Q_d=\mathrm tQ'_d\), and let \(F\in D^b(k_X)\) be arbitrary. The submersion orientation formula gives \(q_X^!F=q_X^{-1}F\otimes W\). Evaluation \(Q'_d\otimes^LK_d\to W\), with the derived tensor symmetry, gives the map

\[
Q'_d\otimes^Lq_X^{-1}F
\longrightarrow R\mathcal Hom_P(K_d,q_X^!F).
\]

Apply \(Rq_{Y*}\) and precede it by the forget-support map from \(Rq_{Y!}\) of the left side. This is the natural arrow from convolution by \(Q_d\) to the ordinary right-adjoint formula for \(K_d\). The [relative-dual theorem and Corollary 2](../../sheaf-proof-readings/src/SH03/dual-kernels-and-an-unchanged-parameter.md#relative-duals-point-to-different-adjoints) prove that this arrow is invertible on \(\Omega_Y\) under the constructibility and reverse-admissibility hypotheses already checked.

Its compactness mechanism can be checked directly here. The evaluation comparison can fail only on the escaping sum of \(\operatorname{SS}(q_X^{-1}F)\) and \(\operatorname{SS}(K_d)^a\). The first summand has zero \(Y\)-covector. If their sum converges over \(\Omega_Y\), the \(Y\)-covector of the second summand converges there too. The reciprocal graph, whose coordinates are (1)–(2), bounds its entire covector over a compact \(Y\)-cotangent neighborhood. The convergent sum then bounds the first summand. Neither can escape. The comparison cone therefore has no microsupport over that selected region, and the dual-kernel theorem's proper/ordinary image comparison kills its image there. The same graph admissibility makes the forget-support map invertible there. These are the evaluation and support-forgetting maps used by the adjunction, with their orientation factors retained. Only the kernel's constructibility enters; \(F\) may have arbitrary bounded coefficient modules.

Let \(A\) be any bounded complex of \(k\)-modules. We calculate this convolution on \(A_M\), the constant coefficient complex supported on \(M\). The tensor support is \(S\cap(M\times Y)\). Its equations reduce to

\[
x_k=y_k\ (k\in I),\qquad x_J=x_n=0,\qquad y_n=0.
\qquad\text{(12)}
\]

Call the closed set in (12) \(C\), and let \(j:C\hookrightarrow P\). Restriction followed by multiplication defines \(k_S\otimes k_{M\times Y}\to k_C\). On \(C\) its stalk is the identity of \(k\); off \(C\) both stalks vanish. Both factors are flat sheaves because their stalks are \(0\) or \(k\), so this is also their derived tensor comparison. For arbitrary bounded \(A\), choose a bounded flat coefficient resolution, possible over a ring of finite global dimension, with no finite-generation requirement on its terms. The same comparison in each degree gives the actual natural isomorphism

\[
k_S\otimes^Lq_X^{-1}A_M\simeq j_*A_C.
\]

The coefficient differentials are retained. This calculation uses flat support factors; it does not impose a transversality or perfection condition on \(A\).

The projection \(q_Y|_C:C\to N\) has inverse \(y\mapsto((y_I,0,\ldots,0),y)\), so it is a diffeomorphism. Since \(N\) is closed in \(Y\), this projection is proper on the whole support \(C\). Proper direct-image composition sends \(j_*A_C\) to \(A_N\) by this actual inverse identification. The fibres are points, so there is no compact-support degree or additional orientation line to insert. The line already present in \(Q'_d\) is trivialized by the fixed choices preceding (11). Consequently (11) yields

\[
Q_d\circ_X A_M\simeq A_N[r-d],\qquad
\Psi_{K_d}(A_M)\simeq A_N[r-d]
\quad\text{in }\mathcal D_Y(\Omega_Y).
\qquad\text{(13)}
\]

The first is an ordinary convolution calculation with the chosen line trivialization; the second uses the localized dual-kernel comparison. No perfection assumption on \(A\) was used.

The required normalization is therefore

\[
\boxed{d=n-p-1=r,\qquad
\Psi_{k_S[r]}(A_M)\simeq A_N\text{ on }\Omega_Y.}
\qquad\text{(14)}
\]

For \(k\ne0\), this degree is forced already by \(A=k\). Choose \(v\in T_N^*Y\cap\Omega_Y\), which is nonempty even when \(n=1\). Applying the submanifold Hom comparison and the supported-coefficient microlocalization used in (6) gives

\[
\mu\operatorname{hom}(k_N,k_N[r-d])_v=k[r-d],\qquad
\mu\operatorname{hom}(k_N,k_N)_v=k.
\]

The [microlocal-Hom support bound](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-microlocal-support--where-directional-sheaves-can-live) makes this probe invert denominators at \(v\), so an isomorphism in the localized category would identify these two complexes. Their nonzero cohomology lies in degrees \(d-r\) and zero, respectively; hence \(d=r\). The zero coefficient complex imposes no normalization by itself. If the coefficient ring is the zero ring, all its coefficient objects are zero and this uniqueness assertion is likewise vacuous.

The equivalence (7) then gives \(\Phi_{k_S[r]}(A_N)\simeq A_M\) on \(\Omega_X\). The map is the composite of \(\Phi_{k_S[r]}\) applied to the inverse of the adjoint identification in (13), followed by the invertible counit \(\Phi_{k_S[r]}\Psi_{k_S[r]}(A_M)\to A_M\).

Here is the ordinary forward fibre calculation for comparison. Put \(H=Rq_{X!}(k_S[r]\otimes^Lq_Y^{-1}A_N)\). Its fibre over \(x\) has \(y_I=x_I\), \(y_n=0\), and

\[
\sum_{j\in J}x_jy_j=-x_n.
\]

For \(r\geq1\), proper-support fibre comparison and the compact-support coefficient calculation give the following ordinary stalks, with affine orientation lines locally trivialized:

| Base point | Fibre in the \(y_J\) coordinates | Stalk \(H_x\) |
| --- | --- | --- |
| \(x_J\ne0\) | An affine \(\mathbb R^{r-1}\) | \(A[1]\) |
| \(x_J=0,\ x_n=0\) | \(\mathbb R^r\) | \(A\) |
| \(x_J=0,\ x_n\ne0\) | Empty | \(0\) |

On a patch where one coordinate \(x_j\ne0\), solve the displayed equation for \(y_j\); the remaining \(r-1\) coordinates give an explicit affine-bundle trivialization. Thus the first contribution is locally constant there, with its orientation line, and its microsupport on that patch lies in the zero section. It misses \(\xi_n\ne0\), despite its nonzero ordinary stalk when \(A\ne0\). Near the remaining base points the global localized conclusion is supplied by the same counit, whose cone is invisible throughout \(\Omega_X\). A pointwise stalk list alone would not establish that microlocal assertion.

For \(r=0\), including \(n=1,p=0\), the exchange block is empty and (4) defines the diagonal. Its ordinary projection formula gives \(\Phi_{K_d}(F)=F[d]\), and diagonal Hom adjunction gives \(\Psi_{K_d}(F)=F[-d]\), for every bounded \(F\). Here \(M=N\) in the two copies, \(d=r=0\), and both operators are the identity even before localization. Thus no positive-dimensional affine-fibre formula is being used in the empty-block case.

## Exercises with complete solutions

### An explicit three-dimensional transformation

*Difficulty: Introductory.*

Take \(n=3\), \(p=0\), \(x=(1,2,3)\), and \(\xi=(4,5,2)\). Calculate \(y,\eta\), recover \(x,\xi\), and give the normalized kernel shift.

**Solution.** Here \(J=\{1,2\}\) and \(r=2\). Formula (1) gives \(y=(2,5/2,10)\), since \(3+1\cdot2+2\cdot(5/2)=10\), and \(\eta=(-2,-4,2)\). Formula (2) gives \(x_1=1\), \(x_2=2\), \(x_3=10+((-2)2+(-4)(5/2))/2=3\), and \(\xi=(4,5,2)\). The normalized kernel is \(k_S[2]\); its right dual is the unshifted transposed support sheaf after the specified orientation trivializations.

### The empty exchange block

*Difficulty: Introductory.*

What happens when \(p=n-1\)? Include \(n=1\) in the answer.

**Solution.** The set \(J\) is empty and \(r=0\). Equations (1) are \(y=x\), \(\eta=\xi\). Equations (4) say \(x_i=y_i\) for every \(i\), so \(S\) is the diagonal. Also \(M\) and \(N\) are the same coordinate hyperplane in their respective copies. The shift in (14) is zero and the two localized operators are the identity. When \(n=1\), necessarily \(p=0\), and the same calculation gives the diagonal and the point hyperplanes \(\{0\}\), on the regions with nonzero sole covector.

### Transposition does not perform relative duality

*Difficulty: Intermediate.*

For \(r>0\), the ordinary convolution \(k_{S^{\mathsf t}}\circ_X k_M\) is unshifted \(k_N\). Why does this calculation not give the desired right-adjoint normalization for \(K_0=k_S\)? Calculate \(\Psi_{K_0}(k_M)\).

**Solution.** Transposition exchanges the two support factors but contributes no duality complex. The right adjoint uses the relative dual in (10). The exceptional normal degree is \(-(p+1)\), and the input dualizing degree is \(n\), whose sum is \(r\). Hence its kernel is \(k_{S^{\mathsf t}}[r]\) after orientation choices, and \(\Psi_{K_0}(k_M)\simeq k_N[r]\) on \(\Omega_Y\). The unshifted transposed kernel becomes the right relative dual only after shifting the original kernel by \(r\). Keeping track of which operator the question asks for determines the sign and value of the normalization.

### An ordinary forward contribution away from the subspace

*Difficulty: Advanced.*

Assume \(r\geq1\) and \(k\ne0\). At \(x\) with \(x_J\ne0\), compute the fibre of \(S\cap(X\times N)\to X\) and the ordinary stalk of \(\Phi_{k_S[r]}(k_N)\). Reconcile it with the localized conclusion after (14).

**Solution.** The conditions fix \(y_I=x_I\), \(y_n=0\), and impose \(\sum_{j\in J}x_jy_j=-x_n\) on the \(r\) remaining coordinates. Since \(x_J\ne0\), this is an affine space of dimension \(r-1\). Its compactly supported cohomology is \(k[-(r-1)]\), with the affine orientation line understood and locally trivialized. The kernel shift gives the stalk \(k[1]\), whereas \((k_M)_x=0\). On the open set \(x_J\ne0\), these affine fibres form a smooth locally trivial affine bundle, so this contribution is locally constant, up to its orientation line and degree. Its microsupport there lies in the zero section and misses \(\xi_n\ne0\). Thus its nonzero ordinary stalk is consistent with the equivalence on \(\Omega_X\). The global ordinary sheaf need not equal \(k_M\).

### Coefficients and the identity condition

*Difficulty: Intermediate.*

Let \(A=[A^{-1}\to A^0]\) be a bounded coefficient complex whose modules need not be projective or finitely generated. Explain why (13) still applies, and why this does not weaken the constructibility hypothesis on the kernel in (7).

**Solution.** Resolve \(A\) by a bounded flat complex, possible because the coefficient ring has finite global dimension. The two constant support factors have stalks \(0\) or the flat module \(k\), so their tensor produces exactly the intersection support. The support projection (12) is an isomorphism onto \(N\), and its pushforward carries each coefficient differential to the same differential. Thus the result is \(A_N[r-d]\), with the stated orientation choices. The contact criterion is imposed on \(K_d=k_S[d]\), whose coefficients are locally rank-one perfect, not on the arbitrary input \(A_M\). Its identity map in (6) remains \(1\mapsto\operatorname{id}_k\); allowing arbitrary bounded inputs neither changes that map nor replaces the kernel's constructibility requirement.

## References

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Theorem 6.3.4, printed pp. 111–113 (PDF pp. 114–116), is the general contact-kernel equivalence used here. Theorem 6.3.9 and Corollary 6.3.11, printed pp. 115–117 (PDF pp. 118–120), identify the actual microlocal-Hom comparison. Corollary 7.4.2, printed p. 139 (PDF p. 142), explains transport of conormal models by a simple contact kernel, with its degree determined by the kernel type and the specified index.

The source's \(Y\)-to-\(X\) operator is an ordinary-image Hom action, with its physical antipode on \(X\). In this lesson \(\Phi\) is a proper-support tensor action, the input antipode is on \(Y\), and \(\Psi\) is its right adjoint. Thus the general source statement is applied through the convention-fixed programme criterion and its relative-dual comparison, not by identifying the two notations for \(\Phi\).

The coordinate relation (1), support (4), physical conormal (5), and conormal test (12) are derived above. The calculation of the right kernel keeps the intrinsic normal and target orientation lines, then fixes their ordered generators. Closed-support tensor multiplication and projection along an isomorphism give the actual coefficient map with degree \(r-d\). This direct computation determines the normalization for arbitrary bounded coefficient complexes. The source's general conormal transport principle does not replace that degree calculation. The ordinary forward fibres and empty exchange block separately explain the range of the localized conclusion.
