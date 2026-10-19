# Reducing Gaussian symbols and composing linear relations

Clean composition retains a density along the middle fiber. Its linear model comes from restricting a quadratic phase to the symplectic constraint and integrating the variables eliminated by the quotient. A phase radical records the directions in which that integration has no oscillation. Keeping its density makes the construction finite and invariant, even when the corresponding unweighted integral would diverge.

The exact earlier programme proofs are:

- The restored [phase-space lesson](../20261005-restored-phase-space/phase-space-and-generating-families.md), Sections 2, 5 and 7: symplectic bases, common complements, linear reduction, critical maps and canonical relations.
- The restored [Gaussian-symbol lesson](../20261005-restored-gaussian-symbols/gaussian-lines-and-invariant-symbols.md), Sections 2–5: Gaussian lines, critical densities, the integer Maslov cocycle and exact quadratic normalization. The restored [tangent-zoom lesson](../20261005-restored-tangent-zoom/tangent-zoom-and-quadratic-models.md), Section 5, supplies the singular Gaussian and delta formula. The [Gaussian companion, Z2](../20261004-free-tangent-zoom/prerequisites/gaussian-symbol-line.md#z2-nonzero-gaussian-frames-including-changes-of-rank), proves smooth dependence through changes of Hessian rank.
- [Quadratic stationary phase, Q1–Q6](../20261004-free-stationary-phase/quadratic-stationary-phase.md), proves the limiting integrals, Fourier inversion, diagonalization and Fresnel constants. [Finite calculus and inverse maps](../20261004-free-stationary-phase/prerequisite-completions.md) supplies smooth matrix inversion; [compact bumps and density integration, Appendix A.4–A.6](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md), supplies the compact tests and exact-sequence density conventions.
- The existing [canonical-composition component, C1–C4](../20261004-free-canonical-composition/clean-canonical-composition.md), and [Maslov-composition component, G1–G5](../20261004-free-canonical-composition/maslov-composition-and-gaussian-factors.md), retain their full alternative proofs of the matching sequence, quadratic presentations, coordinate invariance and associativity. Their geometric density map is unscaled; the Gaussian normalization here multiplies it by \((2\pi)^{-e/2}\). Their frames \(s_\phi\), rather than the dimension-shifted frames \(e_\phi\), give the Gaussian phase convention used here.

The [proof map](proof-map.json) binds the results to these exact programme proofs. The primary source for this restoration is the reprint of Hörmander III, corrected second printing (1994), Section 21.6 including Theorems 21.6.6–21.6.7. The lesson retains its own explanations, density-first organization, calculations and six solved exercises. It proves the linear symbol maps; analytic composition of variable phases and amplitudes requires the additional estimates and support hypotheses proved in the [analytic-composition component](../20261004-free-canonical-composition/analytic-clean-composition.md).

Let \(\Omega(V)\) denote the complex line of translation-invariant densities on a real vector space \(V\). Its positive real ray determines its real powers \(\Omega^s(V)\), including \(s=\pm1/2\). We use \(\Omega(0)=\mathbb C\) with positive unit one. The symplectic form is \(\omega=\sum d\xi_j\wedge dx_j\), with vertical distinguished plane \(\lambda_0=\{x=0\}\). Write
\[
\mathscr G(\lambda)=M(\lambda)\otimes\Omega^{1/2}(\lambda)
\tag{0.1}
\]
for the intrinsic Gaussian symbol line constructed in the preceding lesson.

## 1. A quadratic phase with a radical gives a density-valued Gaussian

Let \(Q(x,\theta)\) be any real quadratic form, with \(x\in\mathbb R^n\) and \(\theta\in F=\mathbb R^N\). Set
\[
R=\{r\in F:Q_{x\theta}r=0,\ Q_{\theta\theta}r=0\},
\qquad e=\dim R.
\tag{1.1}
\]
Thus \(\{0\}\times R\) is the pure phase-variable part of the full Hessian radical. For every \(r\in R\),
\[
Q(x,\theta+r)=Q(x,\theta).
\tag{1.2}
\]
The critical space and its image are
\[
C_Q=\{Q_\theta=0\},\qquad
\lambda_Q=\{(x,Q_x):Q_\theta=0\}.
\tag{1.3}
\]

**Proposition 1.1.** The space \(\lambda_Q\) is Lagrangian. The critical map \(C_Q\to\lambda_Q\) is onto with kernel \(\{0\}\times R\); hence \(C_Q/R\to\lambda_Q\) is an isomorphism. On any complement \(F=W\oplus R\), the restriction \(Q|_{\mathbb R^n\times W}\) is a nondegenerate phase parametrizing this same plane.

**Proof.** The transpose of the linear map \((x,\theta)\mapsto Q_\theta\) has kernel \(R\): its components are exactly the two matrices in (1.1). Its rank is therefore \(N-e\), so \(\dim C_Q=n+e\). A vector in the kernel of the critical map has \(x=0\), \(Q_{x\theta}\theta=0\) and \(Q_{\theta\theta}\theta=0\), hence lies in \(R\). The image has dimension \(n\).

For two vectors \((v,w),(\widetilde v,\widetilde w)\in C_Q\), the critical equations are
\[
Q_{\theta x}v+Q_{\theta\theta}w=0,
\qquad Q_{\theta x}\widetilde v+Q_{\theta\theta}\widetilde w=0.
\]
Symmetry of the Hessian gives
\[
\omega\big((v,Q_{xx}v+Q_{x\theta}w),
(\widetilde v,Q_{xx}\widetilde v+Q_{x\theta}\widetilde w)\big)=0:
\]
the \(Q_{xx}\) terms cancel, and the remaining difference is zero by the two critical equations and symmetry of \(Q_{\theta\theta}\). Thus the \(n\)-dimensional image is isotropic and is Lagrangian.

On a complement \(W\), a pure phase radical vector would also be a vector of \(R\), so is zero. This proves nondegeneracy of the restricted phase. Equation (1.2) shows that it has the same critical image. ∎

The integral of \(e^{iQ}\) over all of \(F\) has an infinite volume factor when \(e>0\). Its appropriate replacement is an element of
\[
\mathcal I(\lambda_Q,H)\otimes\Omega(R),
\tag{1.4}
\]
where \(H\) is the horizontal reference. Fix Lebesgue measure \(d\theta\), a scalar \(a\), and any linear projection \(T:F\to R\) that is the identity on \(R\). For \(\chi\in C_c^\infty(R)\), consider
\[
\mathcal U_Q[\chi](x)
=a(2\pi)^{-(n+2N)/4}
\int_F e^{iQ(x,\theta)}\chi(T\theta)\,d\theta\ |dx|^{1/2}.
\tag{1.5}
\]
The integration in the quotient directions is the Fresnel/delta evaluation of the preceding lesson; the radical direction has compact support.

**Lemma 1.2.** Formula (1.5) is independent of \(T\) and is the pairing of a well-defined translation-invariant \(\mathcal I(\lambda_Q,H)\)-valued density on \(R\) with \(\chi\).

**Proof.** Use a splitting \(\theta=w+r\). The density exact sequence identifies \(d\theta\) with a product \(\mu_W\mu_R\); any reciprocal rescaling of those two factors leaves their product unchanged. By (1.2), the phase is independent of \(r\). Since \(T(w+r)=Tw+r\), translation invariance gives
\[
\int_R\chi(Tw+r)\,\mu_R(r)=\int_R\chi(r)\,\mu_R(r).
\]
Thus (1.5) is
\[
\left[a(2\pi)^{-(n+2N)/4}
\int_W e^{iQ(x,w)}\,\mu_W(w)\ |dx|^{1/2}\right]
\int_R\chi(r)\,\mu_R(r).
\tag{1.6}
\]
The first bracket belongs to the nonzero Gaussian line unless \(a=0\), by Proposition 1.1 and the previous lesson. Changing the complement replaces each \(w\) by \(w+Lw\), with \(Lw\in R\), which leaves the phase unchanged. The density exact sequence accounts for its measure change. Therefore the bracket tensored with \(\mu_R\) is independent of the splitting as well as of \(T\). This proves the claim. One may justify the displayed integrations by inserting a damping factor in \(W\), performing the compact radical integration first, then taking the proved Fresnel boundary value. ∎

With the same quotient measure, the normalized nondegenerate Gaussian for \(Q|_W\) would use \(N-e\) phase variables. Consequently (1.6) is that Gaussian tensored with \(\mu_R\), multiplied by
\[
(2\pi)^{-e/2}.
\tag{1.7}
\]
Here we retain the normalization with the original count \(N\). Later it is the actual integral over eliminated variables that determines that count. An adjusted clean-phase normalization can absorb (1.7), but that adjustment must be explicit.

## 2. The density map supplied by symplectic reduction

Let \(S\) have dimension \(2n\), let \(\Delta\subset S\) be isotropic, and set
\[
d=\dim\Delta,\qquad K=\lambda\cap\Delta,\qquad e=\dim K.
\]
Define
\[
S_\Delta=\Delta^\omega/\Delta,
\qquad
\lambda_\Delta=(\lambda\cap\Delta^\omega)/K,
\qquad
\lambda_{0\Delta}=(\lambda_0\cap\Delta^\omega)/(\lambda_0\cap\Delta).
\tag{2.1}
\]
The images implicit in these quotient formulas are Lagrangian in \(S_\Delta\), by the proved linear reduction proposition. Their dimensions are \(n-d\).

There is a canonical positive isomorphism
\[
\mathfrak d_\Delta:
\Omega^{1/2}(\lambda)
\longrightarrow
\Omega^{1/2}(\lambda_\Delta)
\otimes\Omega(K)\otimes\Omega^{-1/2}(\Delta).
\tag{2.2}
\]

**Proof.** Put \(B=\lambda\cap\Delta^\omega\). The two exact sequences give
\[
\Omega^{1/2}(\lambda)
\simeq\Omega^{1/2}(B)\otimes\Omega^{1/2}(\lambda/B),
\qquad
\Omega^{1/2}(B)
\simeq\Omega^{1/2}(K)\otimes\Omega^{1/2}(\lambda_\Delta).
\tag{2.3}
\]
For completeness, the density isomorphism of an exact sequence is obtained by lifting a basis of the quotient and adjoining a basis of the kernel. Changing a lift adds kernel columns and has determinant one. The absolute determinant of a block change of basis is the product of the two diagonal absolute determinants. This proves canonicity and positivity.

The pairing
\[
(\lambda/B)\times(\Delta/K)\longrightarrow\mathbb R,
\qquad([v],[w])\longmapsto\omega(v,w)
\tag{2.4}
\]
is well-defined and perfect. Its left kernel is \(B\); its right kernel before quotienting is \(\Delta\cap\lambda^\omega=K\). Both quotients have dimension \(d-e\). Duality therefore identifies
\[
\Omega^{1/2}(\lambda/B)
\simeq\Omega^{-1/2}(\Delta/K)
\simeq\Omega^{1/2}(K)\otimes\Omega^{-1/2}(\Delta).
\tag{2.5}
\]
Combine (2.3) and (2.5). The two factors \(\Omega^{1/2}(K)\) become the full density \(\Omega(K)\), proving (2.2). ∎

This density map uses only exact sequences and the symplectic pairing. It has no Fresnel phase and no factor of \(2\pi\). The Gaussian construction below has the same positive Jacobians, with an additional normalization factor.

## 3. Adapted coordinates and the quadratic reduction operation

Set
\[
k=\dim(\Delta\cap\lambda_0),\quad j=d-k,\quad l=n-d.
\tag{3.1}
\]
Choose symplectic coordinates split as
\[
x=(x',y,z),\qquad\xi=(\xi',\eta,\zeta),
\quad\dim x'=k,\quad\dim y=l,\quad\dim z=j,
\tag{3.2}
\]
such that
\[
\lambda_0=\{x=0\},\qquad
\Delta=\{x'=y=\eta=\zeta=0\}.
\tag{3.3}
\]
Thus \((\xi',z)\) are coordinates on \(\Delta\),
\[
\Delta^\omega=\{x'=\zeta=0\},
\tag{3.4}
\]
and \((y,\eta)\) are symplectic coordinates on the quotient.

Such coordinates exist with the specified distinguished vertical plane. Choose a basis of \(\Delta\cap\lambda_0\), extend it to \(\Delta^\omega\cap\lambda_0\), then to \(\lambda_0\). The dimensions of these successive spaces are \(k,k+l,n\): restriction of the symplectic pairing of \(\Delta\) with \(\lambda_0\) has rank \(j\). Choose \(j\) vectors of \(\Delta\) dual to the last vertical basis vectors; they complete \(\Delta\cap\lambda_0\) to \(\Delta\) and are mutually isotropic. Here is a completion that keeps those prescribed vectors fixed. Write the vertical basis as \(e_i\), and call the prescribed horizontal vectors \(f_j\), with indices in the last block \(J\), so \(\omega(e_i,f_j)=\delta_{ij}\). For each remaining index choose a vector \(g_i\) dual to all \(e_a\); this is possible since the pairing identifies \(S/\lambda_0\) with \(\lambda_0^*\). Replace \(g_i\) by \(g_i-\sum_{j\in J}\omega(g_i,f_j)e_j\). It stays dual to the vertical basis and is now orthogonal to every prescribed \(f_j\). Finally replace each such \(g_i\) by \(g_i+\tfrac12\sum_{a\notin J}\omega(g_a,g_i)e_a\), using the vectors before this last replacement in the coefficients. The new pairing between indices \(i,b\notin J\) is \(\omega(g_i,g_b)-\tfrac12\omega(g_i,g_b)+\tfrac12\omega(g_b,g_i)=0\). This last correction preserves the pairings with prescribed vectors. Together with the \(e_i\) and fixed \(f_j\), the resulting vectors form the required symplectic basis. This gives (3.2)–(3.3), including empty blocks.

Represent an element of \(\mathscr G(\lambda)\) in the horizontal reference by a nondegenerate quadratic phase:
\[
u(x)=a(2\pi)^{-(n+2N)/4}
\int e^{iQ(x,\theta)}\,d\theta\ |dx|^{1/2}.
\tag{3.5}
\]
Such a phase exists: complete the nonzero vertical constraints of \(\lambda\), and write it as \(q(x)+x\cdot T\theta\) with \(T\) injective and \(q\) quadratic, as in the previous lesson's signature proof.

Form the new quadratic phase
\[
q_\Delta(y,z,\theta)=Q(0,y,z,\theta),
\tag{3.6}
\]
with base variable \(y\) and phase variables \((z,\theta)\). Interpret
\[
g(y)=a(2\pi)^{-(n+2N)/4}
\iint e^{iq_\Delta(y,z,\theta)}\,dz\,d\theta\ |dy|^{1/2}
\tag{3.7}
\]
by Lemma 1.2, as a density-valued Gaussian. Equation (3.7) is a quadratic phase operation. It does not assert that an arbitrary distribution admits ordinary restriction to \(x'=0\) followed by an unweighted pushforward.

**Lemma 3.1.** The pure phase radical of (3.6) is naturally isomorphic to \(K\), and its critical image is \(\lambda_\Delta\). Hence (3.7) belongs to
\[
\mathcal I(\lambda_\Delta,H_\Delta)\otimes\Omega(K).
\tag{3.8}
\]

**Proof.** Its critical equations are \(Q_z=Q_\theta=0\), evaluated at \(x'=0\). In the original critical map, these are precisely \(x'=\zeta=0\), so the original covector lies in \(\lambda\cap\Delta^\omega\). Projection to \((y,\eta)\) gives the reduced plane in (2.1).

For a pure radical vector \((z,\theta)\), set \(x'=y=0\). All derivatives of (3.6), including its \(y\) derivative, vanish. Thus its image in the original critical map has \(x'=y=\eta=\zeta=0\), and lies in \(\lambda\cap\Delta=K\). Conversely every vector of \(K\) has a unique preimage under the original nondegenerate critical map; that preimage is a pure radical vector for (3.6). This is the claimed isomorphism. Lemma 1.2 and Proposition 1.1 now prove (3.8). ∎

Tensor (3.8) with the inverse half density
\[
|d\xi'\,dz|^{-1/2}\quad\text{on }\Delta,
\tag{3.9}
\]
and pass to the intrinsic Gaussian symbol lines. This is the candidate map
\[
\mathfrak R_\Delta:
\mathscr G(\lambda)\longrightarrow
\mathscr G(\lambda_\Delta)\otimes\Omega(K)
\otimes\Omega^{-1/2}(\Delta).
\tag{3.10}
\]

## 4. Why the reduction operation is independent of its choices

**Theorem 4.1 (Gaussian reduction).** The map (3.10) is a canonical nonzero linear map. It depends on \((S,\lambda_0,\Delta)\) and \(\lambda\), and is invariant under symplectic isomorphisms preserving those data. For fixed \((S,\lambda_0,\Delta)\), on any smooth family of \(\lambda\)'s with \(\dim(\lambda\cap\Delta)\) constant, it is a smooth bundle map. Its positive density factor is
\[
(2\pi)^{(d-2k-2e)/4}\mathfrak d_\Delta,
\tag{4.1}
\]
and its unit-modulus factor gives a canonical map
\[
M(\lambda)\longrightarrow M_\Delta(\lambda_\Delta).
\tag{4.2}
\]

**Proof of independence.** First change the phase representing the same input Gaussian. Complete squares in the nonzero block of \(Q_{\theta\theta}\). Eliminating \(h\) variables by the exact Fresnel formula multiplies the amplitude by
\[
e^{i\pi\operatorname{sgn}D/4}|\det D|^{-1/2}
\]
and changes the normalization from \(N\) to \(N-h\), because the Gaussian factor \((2\pi)^{h/2}\) supplies exactly that change. The same elimination, with the same factor, can be performed in (3.7); setting \(x'=0\) does not change the eliminated pure phase block. Thus both operations reduce to a phase linear in its remaining phase variables,
\[
Q(x,\theta)=q(x)+x\cdot T\theta,
\tag{4.3}
\]
where \(T\) is injective. Its constraint subspace \(V=\ker T^T\) is the base projection of \(\lambda\), and \(q|_V\) is determined by \(\lambda\), since \(q(x)=\xi\cdot x/2\) there. Two such injective \(T\)'s with the same range differ by an invertible phase-basis change. Two such \(q\)'s differ by a quadratic polynomial vanishing on \(V\). In linear coordinates \(V=\{x_1=\cdots=x_s=0\}\), every monomial of that polynomial has a constrained coordinate as a factor. Consequently the difference is \(x\cdot T Lx\) for a linear map \(L\), and can be absorbed by the translation \(\theta\mapsto\theta+Lx\). These changes preserve the integral and its measure, both before and after (3.6). The scalar amplitudes agree after the measure changes because the resulting nonzero input Gaussian is fixed. This proves phase independence, including unequal original variable counts.

Next keep the base coordinates and change the horizontal reference by \(\xi\mapsto\xi-Ax\), \(A=A^T\), preserving (3.3). This preservation requires \(A(0,0,z)\) to have only a \(\xi'\) component. Hence the \(yz\) and \(zz\) blocks of \(A\) vanish. On \(x'=0\), its quadratic form is independent of \(z\) and is \(y^TA_{yy}y\). The input chirp \(e^{-ix^TAx/2}\) in the preceding lesson therefore changes (3.7) by precisely \(e^{-iy^TA_{yy}y/2}\), the induced chirp on the reduced space. Its shear on \(\Delta\) has determinant one. Thus (3.10) respects the intrinsic Gaussian-line identifications.

Finally keep the horizontal reference, and change dual bases by \(x=Pv\), \(\xi=P^{-T}\nu\), preserving the two flags \(x'=0\) and \(x'=y=0\). The matrix has the block form
\[
P=\begin{pmatrix}P_{11}&0&0\\P_{21}&P_{22}&0\\P_{31}&P_{32}&P_{33}\end{pmatrix}.
\tag{4.4}
\]
At \(v'=0\), the remaining base is \(y=P_{22}v_y\), and the integrated variable is \(z=P_{32}v_y+P_{33}v_z\). Pullback of the input half density and integration over \(v_z\) give the factor
\[
|\det P|^{1/2}|\det P_{33}|^{-1}
=|\det P_{22}|^{1/2}
|\det P_{11}|^{1/2}|\det P_{33}|^{-1/2}.
\tag{4.5}
\]
The first factor is the reduced half-density Jacobian. The other factors are exactly the transformation of \(\Omega^{-1/2}(\Delta)\): on \(\Delta\), the old coordinates \((\xi',z)\) are \((P_{11}^{-T}\nu',P_{33}v_z)\). The radical density is transported to \(K\) by the critical-map isomorphism in Lemma 3.1. Equations (4.5) and (3.9) therefore cancel all remaining basis dependence. A general adapted coordinate change is the composition of this dual-basis change and the preceding shear: a symplectic map preserving the vertical plane has precisely a dual linear base change followed by a symmetric frequency shear. This proves intrinsic independence.

For smoothness, work near one parameter value. Choose a fixed horizontal Lagrangian transverse to both the distinguished vertical and the input plane there. Transversality persists nearby, so in the associated coordinates the input planes have the smooth graph form \(x=B(p)\theta\), with \(B(p)=B(p)^T\). Returning to the fixed adapted coordinates only adds a fixed quadratic base form and an invertible base change. Thus they admit a smooth family of nondegenerate quadratic phases with the same number of variables, \(N=n\). The matrix of the reduced critical equations has constant rank because its transpose kernel has dimension \(e\), by Lemma 3.1. An invertible matrix minor expresses its kernel as a smooth graph: the remaining rows impose no additional condition since that minor already has the full rank. Applying the same argument to the transpose gives a smooth frame and complement for the radical. Quotienting by it gives a smooth nondegenerate phase \(\bar q_p\). Its critical map is injective, and a fixed nonzero minor selects a smooth basis for its image \(\lambda_\Delta(p)\).

Choose in the reduced space a fixed horizontal plane transverse to that image and to its distinguished vertical at the central parameter. It remains transverse nearby. In this horizontal reference the full Hessian of \(\bar q_p\), including its base variables, is invertible: a vector in its kernel lies in the phase critical space and maps to a vector in the intersection of the reduced plane with that horizontal; transversality makes the image zero and nondegeneracy then makes the vector zero. The determinant is therefore nonzero nearby, its signature is locally constant, and its inverse and critical-density Jacobians are smooth. The exact Gaussian formula in the preceding lesson now gives smooth nonzero symbol coefficients in this frame. The density identification with \(K\) is a smooth linear isomorphism by Lemma 3.1. The transition laws already proved transport these coefficients to any other frame.

This argument does not require the pure phase Hessian to have constant rank. The distributional smoothness of the corresponding Gaussian frames, even when that rank changes, is proved by Fourier-test differentiation in the linked Gaussian companion Z2. It follows that (3.10) is a smooth bundle map on the stated constant-\(e\) family. At a jump of \(e\), the radical spaces no longer form a vector bundle of one rank; the theorem makes no smoothness assertion across that jump.

The map is nonzero because removing its radical leaves a nondegenerate quadratic phase, whose Gaussian is nonzero. Its phase and positive factor separate uniquely: the positive-density rays specify the positive factor, and the Maslov transitions have modulus one. It remains to compute that positive factor; Sections 5–6 do so and prove (4.1). ∎

## 5. Compute the factor when the constraint lies in the plane

Assume first that \(\Delta\subset\lambda\), so \(e=d=k+j\). In adapted coordinates, choose reduced horizontal coordinates making \(\lambda_\Delta\) the graph \(y=B\eta\), \(B=B^T\). This is possible by a common complement to \(\lambda_{0\Delta}\) and \(\lambda_\Delta\), lifted to a horizontal complement preserving (3.3).

Then \(\lambda\) is represented by
\[
Q(x',y,z;\theta',\eta)
=x'\cdot\theta'+y\cdot\eta-\tfrac12\eta^TB\eta.
\tag{5.1}
\]
Indeed inclusion of \(\Delta\) forces \(x'=\zeta=0\) on \(\lambda\); reduction gives \(y=B\eta\), and the remaining \(\xi'\) and \(z\) variables are free. Here the phase-variable count is \(N=k+l\). Its critical density is
\[
|d\theta'\,d\eta\,dz|,
\]
so the positive input symbol is \(|a||d\theta'\,d\eta\,dz|^{1/2}\).

After setting \(x'=0\), the variables \((\theta',z)\) are the radical and identify with \(K=\Delta\). The remaining reduced Gaussian has coefficient \(a\) times
\[
(2\pi)^{-(n+2k+2l)/4+3l/4}
=(2\pi)^{-(3k+j)/4}.
\tag{5.2}
\]
Thus, apart from its unit phase, the output of (3.10) is
\[
|a|(2\pi)^{-(3k+j)/4}|d\eta|^{1/2}
\otimes|d\theta'\,dz|\otimes|d\xi'\,dz|^{-1/2}.
\tag{5.3}
\]
The exact-sequence map (2.2) has exactly these positive density frames without the scalar factor. Since
\[
-3k-j=d-2k-2e,
\]
this proves (4.1) in the contained case.

## 6. Compute the factor when the intersection is zero

Now assume \(\lambda\cap\Delta=0\). We need a horizontal complement \(H\) transverse to both \(\lambda_0\) and \(\lambda\), preserving the adapted form of \(\Delta\), whose induced reduced horizontal plane is transverse to \(\lambda_\Delta\). Here is a construction that keeps all those requirements.

Choose \(V\subset\Delta\) complementary to \(\Delta\cap\lambda_0\). It is transverse to both \(\lambda_0\) and \(\lambda\). Reduce first by \(V\). In that quotient, the remaining constraint \(D=\Delta/V\) lies in the distinguished vertical plane and is transverse to the reduced \(\lambda\). In the further quotient by \(D\), choose a common horizontal complement to the two reduced Lagrangians. Lift it into a symplectic decomposition of the quotient by \(V\) with coordinates \((x',y;\xi',\eta)\), where \(D\) is the \(\xi'\) plane and the selected horizontal plane in the further quotient is \(\eta=0\).

For the reduced \(\lambda\), its subspace \(\eta=0\) projects bijectively to the \(x'\) coordinates. To check this, a vector there with \(x'=0\) projects to the intersection with the selected reduced horizontal plane, so its projection is zero; it then belongs to \(\lambda\cap D=0\). Also the \(\eta\) map on this Lagrangian has rank \(l\): its transpose kernel is its intersection with the \(y\)-horizontal plane, which has just been seen to be zero. Therefore its kernel has dimension \(k\), equal to the number of \(x'\) coordinates. On this kernel, \(\xi'=Cx'\) for a symmetric \(C\), by isotropy. The plane \(\xi'=t x'\), \(\eta=0\) is transverse to it if \(C-tI\) is invertible; choose real \(t\) outside the finite eigenvalue set. This plane is a Lagrangian complement to the vertical plane, is transverse to the reduced \(\lambda\), and induces the previously selected horizontal plane after reduction by \(D\). Its preimage under reduction by \(V\) contains \(V\) and is a horizontal complement with all the stated properties in \(S\).

With that choice, write
\[
\lambda=\{x=B\xi\},\qquad B=B^T,
\quad \xi=(\xi',\eta,\zeta).
\tag{6.1}
\]
The block \(B_{11}\) is invertible. Indeed, the constrained equations are \(\zeta=0\), \((B\xi)'=0\); a solution with \(\eta=0\) gives a vector of \(\lambda_\Delta\) in its horizontal complement, hence is zero there and then lies in \(K=0\). Thus \(B_{11}\xi'=0\) implies \(\xi'=0\).

The normalized input is
\[
u(x)=c(2\pi)^{-3n/4}
\int e^{i(x\cdot\xi-\xi^TB\xi/2)}\,d\xi\ |dx|^{1/2}.
\tag{6.2}
\]
In (3.7), integration over \(z\) gives \((2\pi)^j\delta_0(\zeta)\). Completing squares in \(\xi'\) then gives the reduced graph matrix
\[
B_\Delta=B_{22}-B_{21}B_{11}^{-1}B_{12}
\tag{6.3}
\]
and the reduced Gaussian coefficient
\[
c_\Delta=c(2\pi)^{(j-k)/4}
e^{-i\pi\operatorname{sgn}B_{11}/4}|\det B_{11}|^{-1/2}.
\tag{6.4}
\]
All constants follow directly: the \(z\) integral contributes \((2\pi)^j\), the \(k\)-variable Fresnel integral contributes \((2\pi)^{k/2}\), and converting from the input coefficient \((2\pi)^{-3n/4}\) to the reduced coefficient \((2\pi)^{-3l/4}\) gives \((2\pi)^{(j-k)/4}\). The negative signature is due to the Hessian \(-B_{11}\).

To compare with (2.2), change coordinates on \(\lambda\) from \((\xi',\eta,\zeta)\) to \((x',\eta,\zeta)\). The determinant is \(|\det B_{11}|\), so
\[
c|d\xi'\,d\eta\,d\zeta|^{1/2}
=c|\det B_{11}|^{-1/2}|dx'\,d\eta\,d\zeta|^{1/2}.
\tag{6.5}
\]
The coordinates on \(\lambda/B\) are \((x',\zeta)\). In the symplectic pairing (2.4) they are dual to \((\xi',z)\) on \(\Delta\), up to a sign in the first block, irrelevant to a positive density. The geometric map therefore sends (6.5) to
\[
c|\det B_{11}|^{-1/2}|d\eta|^{1/2}
\otimes|d\xi'\,dz|^{-1/2}.
\tag{6.6}
\]
Comparison with (6.4) proves (4.1), since \(j-k=d-2k\) and \(e=0\). It also gives the explicit Maslov map in these graph frames: multiplication by \(e^{-i\pi\operatorname{sgn}B_{11}/4}\). A map between symbol lines of different dimensions can have an eighth-root coefficient in these frames; the geometric Maslov bundles themselves retain their fourth-root transition groups.

For a general intersection \(K\), reduce first by \(K\subset\lambda\), then by \(\Delta/K\). The second reduced intersection is zero. If \(k_1=\dim(K\cap\lambda_0)\), the second vertical intersection has dimension \(k-k_1\): a vector of \(\Delta/K\) in the reduced vertical plane lifts to a vector of \((\Delta\cap\lambda_0)+K\). The two exponents already computed add to
\[
\frac{e-2k_1-2e}{4}
+\frac{(d-e)-2(k-k_1)}4
=\frac{d-2k-2e}{4}.
\tag{6.7}
\]
The agreement with direct reduction can be checked without interchanging divergent integrals. We prove the slightly more general assertion for any isotropic flag \(\Delta_1\subset\Delta\). Choose a vertical basis starting with \(\Delta_1\cap\lambda_0\), extend it through \(\Delta\cap\lambda_0\) and \(\Delta^\omega\cap\lambda_0\), and then to \(\lambda_0\). In \(\Delta/(\Delta\cap\lambda_0)\), start with the image of \(\Delta_1\) and extend a basis; choose representatives of the first vectors in \(\Delta_1\). Choose the remaining vertical basis dual to these representatives. The completion in Section 3 fixes these isotropic representatives. Thus the adapted coordinates can be split as \(x'=(a,b)\) and \(z=(s,t)\), so that \(\Delta_1\) uses precisely the \(\xi_a\) and \(s\) coordinates, and \(\Delta\) uses all of \((\xi',z)\).

The first reduction sets \(a=0\) and treats \((s,\theta)\) as phase variables, with remaining base \((b,y,t)\). Its radical \(R_1\) identifies with \(\lambda\cap\Delta_1\). Every vector of \(R_1\) annihilates the full Hessian after \(a=0\), so it also annihilates the final restricted phase after \(b=0\), where \((t,s,\theta)\) are phase variables. Hence \(R_1\subset R\), the final radical. Choose a complement to \(R_1\) in the first phase-variable space and retain its density by Lemma 1.2. Before any Fresnel evaluation, keep the first quotient phase itself as the nondegenerate representation of the first output. Applying the second reduction sets \(b=0\) and adds \(t\) to the phase variables. Its radical is exactly \(R/R_1\): the restricted phase is already independent of \(R_1\), and a vector annihilates the descended full Hessian precisely when any lift annihilates the original restricted full Hessian. The final quotient is consequently the same quadratic form on the same quotient space as direct reduction.

The measures agree by the determinant-one lift rule for density exact sequences. In particular \(\Omega(R_1)\otimes\Omega(R/R_1)\simeq\Omega(R)\), and these identifications coincide under the critical maps with the corresponding intersections in \(\lambda\). The original prefactor is unchanged while a radical density is split off. If one instead rewrites the intermediate Gaussian with the normalized prefactor for its new base and phase-variable counts, its scalar coefficient acquires the ratio of the old prefactor to the new one; at the next step these ratios telescope to the direct ratio. The inverse half densities of the two constraint spaces likewise combine to \(\Omega^{-1/2}(\Delta)\). Thus direct and staged operations are equal as density-valued Gaussian symbols. This proves the phase assertion as well as the absolute factor; neither equality assumes an unweighted integral over a radical.

The same basis-lift construction combines the geometric maps (2.2): the successive exact sequences are refinements of the direct sequences, and their dual quotient bases pair by the same symplectic form. Taking \(\Delta_1=K\), the first intersection is all of \(K\) and the second is zero. The scalar computation (6.7) therefore completes Theorem 4.1 for every \(K\).

## 7. Apply reduction to composition of linear canonical relations

Let \(S_i\) be symplectic of dimension \(2n_i\), with distinguished Lagrangian \(\lambda_{i0}\), \(i=1,2,3\). Let
\[
G_1\subset S_1\times S_2,\qquad G_2\subset S_2\times S_3
\]
be Lagrangian for \(\omega_1-\omega_2\) and \(\omega_2-\omega_3\), respectively. Their composition and excess space are
\[
G=G_1\circ G_2
=\{(s_1,s_3): (s_1,s_2)\in G_1,
(s_2,s_3)\in G_2\text{ for some }s_2\},
\]
\[
N=\{s_2:(0,s_2)\in G_1,\ (s_2,0)\in G_2\},
\qquad e=\dim N.
\tag{7.1}
\]
All intersections here are linear and hence clean. The linear reduction proof shows that \(G\) is Lagrangian, and that the matching space
\[
F=\{(s_1,s_2,s_2,s_3)\in G_1\times G_2\}
\]
fits into \(0\to N\to F\to G\to0\).

**Theorem 7.1 (linear symbol composition).** There are canonical bilinear maps
\[
M(G_1)\times M(G_2)\longrightarrow M(G),
\tag{7.2}
\]
\[
\Omega^{1/2}(G_1)\times\Omega^{1/2}(G_2)
\longrightarrow\Omega^{1/2}(G)\otimes\Omega(N).
\tag{7.3}
\]
The second map is \((2\pi)^{-e/2}\) times the positive exact-sequence/duality map. These maps are smooth on constant-excess families and are compatible with the tensor product Gaussian model.

**Proof.** In
\[
S=S_1\times S_2\times S_2\times S_3,
\qquad \omega=\omega_1-\omega_2+\omega_2-\omega_3,
\]
take \(\lambda=G_1\times G_2\) and the middle diagonal constraint
\[
\Delta=\{(0,s_2,s_2,0):s_2\in S_2\}.
\tag{7.4}
\]
It is isotropic. Its orthogonal imposes matching middle vectors, so \(\lambda\cap\Delta^\omega=F\); the quotient is \(S_1\times S_3\), the reduced distinguished plane is \(\lambda_{10}\times\lambda_{30}\), and \(K=\lambda\cap\Delta\) identifies with \(N\). Also
\[
d=2n_2,\qquad k=n_2.
\tag{7.5}
\]
The density factor (4.1) is consequently \((2\pi)^{-e/2}\).

Trivialize the residual factor \(\Omega^{-1/2}(\Delta)\) by the positive symplectic volume
\[
\rho_2=|\omega_2^{n_2}/n_2!|
\tag{7.6}
\]
on \(S_2\simeq\Delta\). This contraction is intrinsic; no choice of a Euclidean middle measure enters. Density lines on the product identify with tensor products, and the Gaussian line of a direct sum is the tensor product of its Gaussian lines: add the two quadratic phases, multiply their amplitudes, and observe that their normalized powers of \(2\pi\) add. Apply Theorem 4.1 to this product. Its unit phase gives (7.2), and its positive factor gives (7.3). Smoothness follows from the constant-intersection assertion of Theorem 4.1. ∎

The output is a half density on \(G\) with a full density on the excess space \(N\). This is the linear source of the fiber density integrated in analytic clean composition. A translation-invariant density on \(N\ne0\) does not have a finite total integral; the subsequent analytic theorem must supply properness or compact fiber support and amplitudes.

## 8. A graph factor removes the excess density

Suppose \(G_1\) is the graph of a symplectic isomorphism \(\kappa:S_2\to S_1\), so \(n_1=n_2\). Then \(N=0\), and
\[
G_2\longrightarrow G,\qquad(s_2,s_3)\longmapsto(\kappa s_2,s_3)
\tag{8.1}
\]
is an isomorphism. Lift \(\rho_2\) to a density \(\rho_{G_1}\) on the graph. If \(d_1=c\rho_{G_1}^{1/2}\) and \(d_2\in\Omega^{1/2}(G_2)\), the positive map (7.3) is
\[
(d_1,d_2)\longmapsto c\,(8.1)_*d_2.
\tag{8.2}
\]

**Proof.** A vector of \(G_1\times G_2\) has the unique decomposition
\[
(\kappa s_2,s_2,s_2',s_3)
=(\kappa(s_2-s_2'),s_2-s_2',0,0)
+(\kappa s_2',s_2',s_2',s_3).
\tag{8.3}
\]
The second term is in \(F\); the first identifies the quotient by \(F\) with the graph \(G_1\). Pairing that quotient with the middle diagonal is the symplectic self-duality of \(S_2\), up to a sign, which does not affect positive densities. The contraction in (7.6) therefore contracts \(d_1\) with \(\rho_{G_1}^{-1/2}\), leaving precisely \(c\). There is no excess factor because \(e=0\). This proves (8.2). The Maslov map (7.2) still transports its line coefficient; (8.2) describes the positive density factor. ∎

For the identity relation, its natural Gaussian phase \((x-y)\cdot\theta\) has normalization \((2\pi)^{-n_2}\). It represents \(\delta(x-y)|dx\,dy|^{1/2}\), with unit critical amplitude. Composing two such identity models gives the same model, so the identity Maslov unit is also preserved. This checks both the no-excess constant and the reflected middle-frequency convention.

## 9. Exercises with complete solutions

**Exercise 9.1 (find the radical; introductory).** On \(\mathbb R_x\times\mathbb R^3_\theta\), take
\[
Q=x\theta_1+\tfrac12(\theta_2-a\theta_3)^2,
\qquad a\in\mathbb R.
\]
Determine \(R\), the Lagrangian image, and the density-valued Gaussian (1.5) when the scalar amplitude is one.

**Solution.** The radical is \(R=\{(0,ar,r):r\in\mathbb R\}\), so \(e=1\). The critical equations give \(x=0\), \(\theta_2=a\theta_3\), and the output covector is \(\theta_1\); hence \(\lambda_Q=\{x=0\}\). Put \(w=\theta_2-a\theta_3\) and \(r=\theta_3\). This change has determinant one. The \(\theta_1\) integral is \(2\pi\delta_0(x)\), and the \(w\) integral is \((2\pi)^{1/2}e^{i\pi/4}\). With the original normalization \((2\pi)^{-7/4}\), the density-valued Gaussian is
\[
(2\pi)^{-1/4}e^{i\pi/4}\delta_0(x)|dx|^{1/2}\otimes|dr|.
\]
Thus (1.5) is this Gaussian multiplied by \(\int_R\chi\,|dr|\). A projection with radical coordinate \(r+b\theta_1+cw\) gives the same integral: the \(r\) integration is a translation. The quotient phase has two variables and its normalized Gaussian is \((2\pi)^{1/4}e^{i\pi/4}\delta_0\); their ratio is the factor \((2\pi)^{-1/2}\) in (1.7).

**Exercise 9.2 (vertical and horizontal reduction; intermediate).** In a two-dimensional symplectic space, compare the positive factors in (4.1) for each of the following: \(\Delta=\lambda=\lambda_0\); \(\Delta=\lambda=H\), where \(H\) is horizontal; and \(\Delta=\lambda_0\), \(\lambda=\{x=b\xi\}\), \(b\ne0\).

**Solution.** The reduced symplectic space is zero-dimensional in all three cases. In the first, \(d=k=e=1\), giving \((2\pi)^{-3/4}\). The normalized input point mass is \((2\pi)^{-3/4}\int e^{ix\theta}d\theta=(2\pi)^{1/4}\delta_0\); its quadratic reduction sets \(x=0\) and retains \(|d\theta|\), with coefficient \((2\pi)^{-3/4}\). This is not ordinary evaluation of \(\delta_0\) at zero.

In the second, \(d=e=1\), \(k=0\), giving \((2\pi)^{-1/4}\). The normalized input is the constant \((2\pi)^{-1/4}|dx|^{1/2}\); eliminating \(x\) retains \(|dx|\), and the inverse half density of \(\Delta\) gives exactly the stated factor. In the third, \(d=k=1\), \(e=0\), giving \((2\pi)^{-1/4}\). The reduced coefficient from (6.4) is
\[
(2\pi)^{-1/4}e^{-i\pi\operatorname{sgn}b/4}|b|^{-1/2}.
\]
The determinant factor belongs to the geometric density map, and the remaining Fresnel factor is the Maslov map. These examples distinguish the two sources of normalization.

**Exercise 9.3 (a coupled Gaussian; intermediate).** Let \(n=2\), \(\Delta\) be the \(\xi_1\) axis, and
\[
\lambda=\{x=B\xi\},\qquad
B=\begin{pmatrix}2&3\\3&5\end{pmatrix}.
\]
Reduce the normalized Gaussian with coefficient \(c\). Give its reduced graph matrix, coefficient and inverse density factor.

**Solution.** Here \(k=1,j=0,l=1\), \(B_{11}=2\), and \(K=0\). The Schur complement is \(5-9/2=1/2\). Formula (6.4) gives
\[
c_\Delta=c(2\pi)^{-1/4}e^{-i\pi/4}/\sqrt2.
\]
The reduced distribution is
\[
c_\Delta(2\pi)^{-3/4}
\int e^{i(y\eta-\eta^2/4)}\,d\eta\ |dy|^{1/2},
\]
and its symbol is tensored with \(|d\xi_1|^{-1/2}\). The factor \(1/\sqrt2\) is the exact-sequence density Jacobian for \(x_1=2\xi_1+3\xi_2\); the phase \(e^{-i\pi/4}\) and factor \((2\pi)^{-1/4}\) come from Gaussian reduction.

**Exercise 9.4 (stage the constraints; advanced).** Suppose \(\Delta_1\subset\Delta\) are isotropic. Let \(d_i,k_i,e_i\) denote the constraint dimension, vertical-intersection dimension and plane-intersection dimension for the first reduction. Express the corresponding dimensions for the second reduction by \(\Delta/\Delta_1\), and check that the normalization exponents add to that for direct reduction by \(\Delta\).

**Solution.** Write \(d=\dim\Delta\), \(k=\dim(\Delta\cap\lambda_0)\), \(e=\dim(\Delta\cap\lambda)\). The second dimensions are \(d-d_1,k-k_1,e-e_1\). For either plane, a vector of the second intersection lifts to a vector of \(\Delta\) differing by an element of \(\Delta_1\) from a vector in the original plane; its quotient is therefore the quotient of the original intersection by the first intersection. This proves the dimension statements. Then
\[
\frac{d_1-2k_1-2e_1}{4}
+\frac{d-d_1-2(k-k_1)-2(e-e_1)}4
=\frac{d-2k-2e}{4}.
\]
The two radical-density factors combine to \(\Omega(\lambda\cap\Delta)\) by the density exact sequence, and the two inverse constraint half densities combine to \(\Omega^{-1/2}(\Delta)\). Compatible quadratic coordinates give the same Fresnel/delta integration, as in Section 6, so the phase factors compose as well. The arithmetic alone checks the normalization, rather than replacing that invariant phase argument.

**Exercise 9.5 (an excess-one constant model; intermediate).** Take \(S_i=T^*\mathbb R\), let \(L_i\) be the horizontal plane, and compose \(G_1=L_1\times L_2\) with \(G_2=L_2\times L_3\). Compute (7.3) on the coordinate half densities and verify it with constant Gaussian kernels.

**Solution.** The composition is \(L_1\times L_3\), and \(N=L_2\), with coordinate \(y\) and excess one. The geometric density map sends
\[
|dx\,dy|^{1/2}\otimes|dy\,dz|^{1/2}
\quad\text{to}\quad |dx\,dz|^{1/2}\otimes|dy|.
\]
The Gaussian map multiplies this by \((2\pi)^{-1/2}\). Each normalized no-phase kernel has constant coefficient \((2\pi)^{-1/2}\), since its base dimension is two. Their product integrated formally over the middle variable has coefficient \((2\pi)^{-1}|dy|\). The reduced normalized no-phase kernel has coefficient \((2\pi)^{-1/2}\); dividing yields exactly the additional factor \((2\pi)^{-1/2}|dy|\). Pairing the retained density with a compact \(\chi(y)\) gives a finite value. Integrating it over all of \(\mathbb R\) without a cutoff would diverge.

**Exercise 9.6 (identity graph; advanced).** For \(S_i=T^*\mathbb R^q\), compose two identity relations. Verify the excess, positive density map and Maslov unit using their delta kernels.

**Solution.** Matching identity relations forces all three vectors equal, so \(N=0\). The graph half densities are the square roots of the symplectic volume \(|dx\,d\xi|\), and the graph-case rule (8.2) sends their units to the same unit. The normalized phase \((x-y)\cdot\theta\) gives \(\delta(x-y)|dx\,dy|^{1/2}\), with unit critical amplitude. Its composition satisfies
\[
\int\delta(x-y)\delta(y-z)\,dy=\delta(x-z).
\]
This equality is interpreted by the proper identity operators, or by testing the two kernels successively; it does not multiply unrelated delta distributions on the same variable. No Fresnel factor is introduced by these linear phases, so the identity Maslov unit is preserved. This also checks that the canonical input covector is reflected when relating kernel Lagrangians to operator relations.

## References

- [Hörmander III, §21.6] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing, Springer, 1994, §21.6 clean quadratic discussion and Theorems 21.6.6–21.6.7.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Restoration and exact prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Self-checked by the writing AI. Original text: public domain (CC0).*
