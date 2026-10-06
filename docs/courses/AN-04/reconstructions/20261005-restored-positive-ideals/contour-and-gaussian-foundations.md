# Contour deformation and the complex Gaussian branch

These proofs supply the finite algebra and integration steps in the [complex stationary-phase companion](complex-stationary-contract.md). The [main lesson](positive-lagrangian-ideals-and-distributions.md) proves complex graph division and its uniform flat errors before invoking that companion. The [proof map](proof-map.json) records this order and the exact earlier calculus, integration and Gaussian providers.

## A0. Complex transversals and actual cotangent coordinates

The linear pair proof in [U023, Lemma 4.1 and Corollary 4.2](../20261005-restored-clean-pairs/clean-lagrangian-pairs-and-common-transversals.md) works over \(\mathbb C\). Indeed it uses a basis of the intersection, the perfect bilinear pairing of the two quotient spaces, dual bases, and extension of an alternating-form isometry. The extension in [U022, Lemma 1.1](../20261005-restored-prescribed-coordinates/prescribed-canonical-coordinates-and-isotropic-fibers.md) consists of solving linear equations and correcting the remaining pairings by one-half their alternating matrix. Those operations work over \(\mathbb C\), with no conjugation, order or positive definiteness. They give the same two model planes and the same common transversal \(P'=0,\ P''=Q''\). Complex elimination and basis extension are proved in [U027 A0](../20261005-restored-quadratic-forms/spectral-algebra-and-contour-projections.md).

Apply this to a complex Lagrangian plane and the vertical plane. A common transversal is a graph \(\delta\xi=B\delta x\), and the Lagrangian condition says \(B=B^t\). Its transversality determinant is a polynomial in the independent symmetric entries of \(B\), nonzero at this complex choice. A nonzero polynomial cannot vanish at every real tuple. For one variable, successive division by distinct real linear factors bounds the number of roots by its degree. Induct on the number of variables: fix all but one real variable; if the resulting polynomial vanishes for all real values, each coefficient vanishes for every real tuple of the other variables and hence, inductively, is the zero polynomial. Thus some real symmetric \(B\) gives the required transversal.

Here is the promised base change, rather than an arbitrary symplectic transformation. Center the base at zero, let the marked covector be \(\xi_0\ne0\), and choose \(a\) with \(\xi_{0a}\ne0\). Set
\[
 y_a=x_a+\frac{1}{2\xi_{0a}}x^tBx,\qquad y_j=x_j\quad(j\ne a).
 \tag{A1}
\]
Its derivative at zero is the identity, so the proved real inverse function theorem makes it a local base chart. Its cotangent lift is \(\xi=(D_xy)^t\eta\). At the mark its derivative is \(\delta\xi=\delta\eta+B\delta x\). Therefore the new horizontal plane \(\delta\eta=0\) is exactly the chosen graph. Both the map and its full cotangent inverse are actual local coordinate maps.

## A1. Symmetric complex square factorization

Every invertible complex symmetric matrix \(Q_*\) has a factorization \(Q_*=S^tS\) with \(S\) invertible. To prove this, consider the nondegenerate bilinear form \(b(v,w)=v^tQ_*w\). Some \(v\) has \(b(v,v)\ne0\), since otherwise
\(2b(v,w)=b(v+w,v+w)-b(v,v)-b(w,w)=0\).
A complex square root of this nonzero number exists by the polynomial-root proof [U027 A1](../20261005-restored-quadratic-forms/spectral-algebra-and-contour-projections.md). Normalize \(v\) to have square one. Every vector splits uniquely into its multiple of \(v\) and its \(b\)-orthogonal complement. The complement is nondegenerate: a vector in its radical is orthogonal to that complement and to \(v\), hence to the entire space, and must vanish. Induction constructs a basis matrix \(V\) with \(V^tQ_*V=I\). Take \(S=V^{-1}\).

For a symmetric matrix \(K=I+E\) with \(\|E\|<1\), define
\[
 C(E)=\sum_{k\ge0}c_kE^k,\qquad
 c_0=1,\quad c_{k+1}=\frac{1/2-k}{k+1}c_k.
 \tag{A2}
\]
The ratio test gives absolute convergence for every \(\|E\|<1\), uniformly on each smaller closed norm ball. The scalar coefficient identity
\(2(1+z)C'(z)=C(z)\) follows from the recurrence. If \(H(z)=C(z)^2\), the product rule gives \((1+z)H'=H\) and \(H(0)=1\); comparison of coefficients gives \(H=1+z\). Absolute convergence permits the same coefficient convolution for powers of one matrix, so \(C(E)^2=I+E\). Transposition preserves the series and gives \(C(E)^t=C(E)\).

A derivative of order \(l\) of \(E^k\) is a sum of at most \(k^l\) ordered products with \(l\) inserted increments. On \(\|E\|\le r<1\) its norm is bounded by \(k^l r^{k-l}\) times the increment norms. These bounds are summable for each \(l\). Termwise differentiation, proved by uniform derivative convergence in the earlier calculus lessons, makes \(C\) smooth with every derivative bounded on the smaller ball. This argument allows noncommuting increments. Finally \(C^2=K\) and invertibility of \(K\) imply invertibility of \(C\).

Thus the companion's \(K=S^{-t}\widetilde Q S^{-1}\), near \(I\), has the asserted smooth symmetric square root. This proves its exact quadratic coordinate map; it does not choose the Gaussian orientation by itself.

## A2. The contour identity from the fundamental theorem of calculus

The contour arguments need only the following identity on a fixed real box. Let \(Z(s,x)\in\mathbb C^d\) be smooth for \(0\le s\le1\), and let \(w(z,\bar z)\) be smooth. Write
\[
 c_j=\partial_{x_j}Z,\quad v=\partial_sZ,\quad
 D=\det(c_1,\ldots,c_d),\quad
 D_j=\det(c_1,\ldots,c_{j-1},v,c_{j+1},\ldots,c_d).
 \tag{A3}
\]
The real chain rule and the product rule for determinants give
\[
 \partial_s(w(Z)D)-\sum_j\partial_{x_j}(w(Z)D_j)
 =\sum_k w_{\bar z_k}(Z)
       \left(\bar v_kD-\sum_j\bar c_{j,k}D_j\right).
 \tag{A4}
\]
Here parameters not being integrated are held fixed.

For completeness, the derivatives of \(w\) in \(z\) cancel because
\(vD=\sum_jc_jD_j\). For an invertible column matrix this is Cramer's rule; after multiplication by the determinant it is a polynomial identity, so it holds at singular matrices too. The remaining determinant derivatives cancel because
\(\partial_sc_j=\partial_{x_j}v\) and
\(\partial_{x_j}c_k=\partial_{x_k}c_j\).
The term differentiating the inserted column in \(D_j\) cancels the corresponding term in \(\partial_sD\). Every term differentiating another column has a partner with the two affected columns interchanged and opposite determinant sign. This proves (A4) without an assumed Stokes theorem.

Integrate (A4) first in \(x\) and then in \(s\). The proved Fubini and fundamental theorems give the difference between the two oriented contour integrals, a lateral-boundary term, and the integral of its displayed right side. If \(w(Z)\) vanishes near the lateral boundary, that term is zero. If an auxiliary cutoff is inserted, its derivative has precisely the same boundary role and can be estimated on its transition support. The determinant is complex and oriented, never its absolute value.

For \(w=e^{-t\Phi}B\),
\[
 w_{\bar z_k}
 =e^{-t\Phi}\bigl(B_{\bar z_k}-tB\Phi_{\bar z_k}\bigr).
 \tag{A5}
\]
Suppose the homotopy has bounded derivatives and volume,
\(\operatorname{Re}\Phi(Z)\ge c\rho^2\), and each antiholomorphic defect and each fixed parameter derivative is \(O(\rho^M)\) for every \(M\). Then its integrated error is bounded by a constant times
\[
 (1+t)t^a\sup_{\rho\ge0}\rho^M e^{-ct\rho^2}
 \le C_{M,a}(1+t)t^{a-M/2}.
 \tag{A6}
\]
The integer \(a\) accounts for a prescribed finite number of parameter derivatives. The bound follows by the substitution \(r=\sqrt t\,\rho\); the maximum of \(r^Me^{-cr^2}\) is finite, by differentiation or the exponential-series bounds. Taking \(M\) arbitrarily large proves rapid errors with all those derivatives. On a cutoff transition where \(\operatorname{Re}\Phi\ge c_0>0\), the same conclusion follows from \(t^ae^{-tc_0}\).

For the companion's first homotopy use \(\rho=|\operatorname{Im}Z_s|\); its (C2) supplies the uniform lower bound even at \(s=0\). For its second use \(\rho=(|u|^2+|\operatorname{Im}T|^2)^{1/2}\) and (C9). Choose nested boxes and real-direction amplitude support so the first lateral boundary is disjoint from the support. In the second homotopy a fixed cutoff equal to one near \(u=0\) has its transition away from zero; (C9) makes its boundary contribution exponentially small. These are exactly the boundary and uniformity assertions used there.

## A3. The Gaussian branch without an analytic-continuation theorem

Let \(M=M^t\) be complex with \(\operatorname{Re}M>0\), and put
\[
 I(M)=\int_{\mathbb R^d}e^{-x^tMx/2}\,dx.
 \tag{A7}
\]
The real symmetric diagonalization and Gaussian integral are the proved U001 Q5 and Q2 inputs; Q6 supplies the real Fresnel normalization. They give \(I(I)=(2\pi)^{d/2}\). On each compact set of these complex matrices, the integrand and every prescribed matrix derivative are dominated by a polynomial times \(e^{-c|x|^2}\). The earlier dominated-integration theorem therefore permits differentiation in each real and imaginary matrix entry.

The matrix \(M\) is invertible: for a complex vector \(z\), \(\operatorname{Re}(z^*Mz)=z^*(\operatorname{Re}M)z>0\) unless \(z=0\). Integration by parts, with vanishing Gaussian boundary terms, gives
\[
 \int x_jx_k e^{-x^tMx/2}\,dx=(M^{-1})_{jk}I(M).
 \tag{A8}
\]
Indeed integrate \(\partial_{x_j}(x_k e^{-x^tMx/2})\), obtaining the matrix equation \(MJ=I(M)I_d\) for the second-moment matrix \(J\).

Along any smooth path \(M(s)\) in this domain, (A8) gives
\[
 \frac{d}{ds}I(M(s))
 =-\tfrac12\operatorname{tr}(M^{-1}M')I(M(s)).
 \tag{A9}
\]
Expansion of a determinant one differentiated column at a time gives
\((\det M)'=(\det M)\operatorname{tr}(M^{-1}M')\).
The scalar linear equation (A9) has the nonzero solution obtained by multiplying its initial value by the exponential of the integral of its coefficient. Hence \(I(M)^2\det M=(2\pi)^d\) along every path from \(I\). Such a path exists inside the domain because positive real part is preserved by the straight segment. The integral itself is single valued, so it defines one unambiguous continuous inverse square root:
\[
 I(M)=(2\pi)^{d/2}\det(M)^{-1/2}.
 \tag{A10}
\]
Thus no identity theorem in several complex variables or assumed analytic continuation is needed.

Now let \(A=A^t\), \(\operatorname{Im}A\ge0\), and \(\det A\ne0\). Apply (A10) to \(M_\epsilon=\epsilon I-iA\), \(\epsilon>0\). The determinant is nonzero also at \(\epsilon=0\). Near that endpoint, the coefficient \(-\tfrac12\operatorname{tr}(M_\epsilon^{-1})\) in (A9) is bounded and smooth. Its integral converges as \(\epsilon\downarrow0\); the Gaussian value therefore has a finite nonzero limit. This is the Abel-regularized Gaussian. It has a smooth local branch, because the same scalar equation or the square-root series (A2) gives a smooth root in a neighborhood of its nonzero determinant.

Equivalently one follows \(M_s=(1-s)(A/i)+sI\) from \(s=1\) to \(s=0\). For \(s>0\) its real part is positive definite, and at zero it is invertible. This gives exactly the same branch, since (A10) fixes the value at every interior point and continuity fixes the endpoint. For real symmetric \(A\), diagonalization reduces the limit to the one-dimensional factors; a positive eigenvalue contributes \(e^{i\pi/4}|\lambda|^{-1/2}\), and a negative one contributes \(e^{-i\pi/4}|\lambda|^{-1/2}\), as in the proved real Fresnel formula.

This also fixes the oriented determinant in the companion. At its marked parameter replace the phase by its exact quadratic part. Apply the two contour identities (A4) with a compact cutoff equal to one near zero. Their errors are rapid, and the final real Gaussian in the quadratic coordinates has leading constant \((2\pi)^{d/2}\det(q_z)^{-1}\), with the inherited orientation. The Abel-regularized original quadratic integral has the constant (A10). Its cutoff complement is rapidly small: outside a fixed ball the invertible linear gradient gives integration-by-parts coefficients of order \(|x|^{-1}\), whose derivatives lose further powers. A derivative of order \(l\) of \(e^{-\epsilon|x|^2/2}\) is bounded there by \(C_l|x|^{-l}\), uniformly in \(\epsilon>0\), by bounding the resulting polynomials in \(\sqrt\epsilon x\) times their Gaussian. After \(k\) integrations the tail is bounded by \(C_kt^{-k}|x|^{-2k}\); choose \(2k>d\), then increase \(k\) to any requested decay. Compact transition terms obey the same nonstationary bound. Thus the tail estimate is integrable and uniform under Abel regularization. Comparison of the leading constants fixes the sign. Continuity preserves it on the small parameter patch. This does not permit choosing an unrelated principal scalar root.

For the normal-phase block \(A=\left(\begin{smallmatrix}0&I\\I&-B\end{smallmatrix}\right)\), \(B=B^t\), \(\operatorname{Im}B\le0\), its determinant after division by \(i\) is one. Replace \(B\) by \(sB\), \(0\le s\le1\). The matrices remain invertible and have nonnegative imaginary part. At \(s=0\) their real eigenvalues are \(+1\) and \(-1\), each \(d/2\) times, so the Gaussian factor is \(+1\). Its continuous square is always one, hence its value remains \(+1\). This supplies the branch in the main lesson's normal-phase model.

## A4. Residues of products, inverses and quadratic-coordinate jets

For the graph ideal \(I=(x-T(p))\), main-lesson Sections 2–3 prove exact division and flatness of parameter-only elements of \(I\). If \(a-a^0\in I\) and \(b-b^0\in I\), then \(ab-a^0b^0\in I\) by subtraction and the ideal property. If \(a,a^0\) are nonzero, their inverse difference is \(-(a-a^0)/(aa^0)\in I\). Matrix inversion obeys the corresponding identity
\(A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}\).
For two nearby choices of a scalar square root on the same branch,
\[
 \sqrt a-\sqrt{a^0}
   =\frac{a-a^0}{\sqrt a+\sqrt{a^0}},
 \tag{A11}
\]
whose denominator stays nonzero. Determinants, products, inverses and these local roots therefore pass to residues. The same conclusions hold uniformly for bounded families on fixed smaller patches.

Differentiate the inverse identity \(q(G(u),p)=u\). At \(u=0\), \(G=T\), \(q_{\bar z}(T)=0\), and \(q_z(T)\) is invertible. The first derivative is \(q_z(T)^{-1}\). For each higher real derivative, the chain rule gives the same invertible real derivative of \(q\) times the highest derivative of \(G\), plus a finite sum of lower inverse derivatives and derivatives of \(q\). Induction determines every jet with smooth bounded coefficients. Antiholomorphic derivatives of the matrix factor and of the amplitude are flat in \(|\operatorname{Im}T|\). Differentiating the almost-analytic Taylor construction shows that each holomorphic amplitude jet at \(T\) is a residue of the corresponding real amplitude derivative, up to such a flat term.

Consequently a derivative of order \(2j\) of the pulled-back amplitude uses residues of real amplitude derivatives of order at most \(2j\), with smooth phase-dependent coefficients. Fixed choices of cutoff radii for a given bounded amplitude family make the extension linear on its linear span; the resulting residue operations are linear there. Different choices have only the proved flat ambiguity. They are not pointwise evaluation of the original smooth amplitude at a complex argument.

Every flat error, after any fixed number of parameter derivatives, is \(O(|Y|^M)\) for arbitrary \(M\), \(Y=\operatorname{Im}T\). Multiplication by \(e^{itf_0}\), where \(\operatorname{Im}f_0\ge c|Y|^2\), makes it absolutely rapid by (A6). This justifies discarding those terms in the asymptotic expansion while retaining exact ideal identities before integration.

Original supporting proofs: GPT-6 Astra (OpenAI), Ultra, 5 October 2026, CC0. The preceding programme proofs retain their own attribution and component licences.
