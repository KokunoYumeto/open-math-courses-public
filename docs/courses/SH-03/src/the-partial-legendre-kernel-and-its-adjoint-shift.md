# The partial Legendre kernel and its adjoint shift

The partial Legendre transformation exchanges some position coordinates with ratios of covector coordinates. Its kernel is supported on a smooth incidence equation. We will derive both the contact map and the shift that makes its right adjoint carry one coordinate subspace to a hypersurface. Calculating the right adjoint is essential: the unshifted transposed kernel and the relative dual kernel initially have different degrees.

Use When a kernel quantizes a contact transformation and Dual kernels and an unchanged parameter. Their closed-submanifold, constructible-duality and localized adjunction prerequisites remain the inputs to the sheaf argument. The geometry and fibre calculation below are explicit.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

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

One selected component is present if and only if \(b\ne0\), if and only if the other selected component is present. This verifies the union of the selected regions. The two relation projections are diffeomorphisms by (1)–(2), and hence proper homeomorphisms on that relation.

For any integer \(d\), let \(K_d=k_S[d]\). Here \(k\) is a commutative ring with identity and finite global dimension, and all input complexes are bounded. The smooth closed-submanifold model makes \(K_d\) cohomologically constructible and places its microsupport in \(T_S^*P\). The submanifold microlocal Hom formula and the zero-section Fourier computation give

\[
\mu\operatorname{hom}(k_S[d],k_S[d])|_{T_S^*P}
\simeq k_{T_S^*P}.
\qquad\text{(6)}
\]

The two shifts cancel in Hom. Under (6) the actual identity-induced map sends \(1\) to \(\operatorname{id}_k\), and is invertible. The local identity normalizations glue, without an orientation choice. The contact-kernel theorem therefore proves, for every \(d\), inverse equivalences

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

This uses exceptional degree \(-(p+1)\) for the closed embedding, degree \(n\) for \(\omega_Y\), and degree \(-d\) for dualizing the kernel shift. The total is \(r-d\). We retain the intrinsic line in (10) before choosing its trivialization. The ordered defining functions in (4) trivialize the normal orientation system, and the standard coordinates orient \(Y\). Fix these choices. They give

\[
Q_d\simeq k_{S^{\mathsf t}}[r-d].
\qquad\text{(11)}
\]

The exact constructible dual-kernel theorem identifies \(\Psi_{K_d}\) with convolution by \(Q_d\) on the selected cotangent regions. This is its adjunction comparison, not an identification inferred just from the support of a kernel.

Let \(A\) be any bounded complex of \(k\)-modules. We calculate this convolution on \(A_M\), the constant coefficient complex supported on \(M\). The tensor support is \(S\cap(M\times Y)\). Its equations reduce to

\[
x_k=y_k\ (k\in I),\qquad x_J=x_n=0,\qquad y_n=0.
\qquad\text{(12)}
\]

The projection of (12) to \(Y\) is an isomorphism onto \(N\): every \(y\in N\) has the unique preimage \(x=(y_I,0,\ldots,0)\). This projection is proper on the support. The tensor of the two closed constant support sheaves is the constant sheaf on their intersection; this statement follows on stalks from the flat coefficients \(0\) and \(k\). Tensoring further with a flat resolution of \(A\) gives the same statement for arbitrary bounded derived coefficients. Proper pushforward along the displayed isomorphism has no fibre degree or additional orientation factor. Consequently (11) yields

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

For a nonzero ring \(k\), this degree is forced already by \(A=k\): at any selected conormal point of \(N\), the exact submanifold test detects \(k[r-d]\). A nonzero module concentrated in degree zero cannot be isomorphic to its nonzero shift. When the coefficient complex is zero, the normalization assertion is of course vacuous for that object.

The equivalence (7) then also gives \(\Phi_{k_S[r]}(A_N)\simeq A_M\) on \(\Omega_X\). It gives this by the invertible counit. An ordinary forward fibre calculation can have contributions away from \(M\); the localization in this last assertion is essential.

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
