# The index theorem for measured foliations

*Written by GPT-6.1 Sol (OpenAI), September 2026, with Ultra reasoning effort. Author self-check in progress; no independent review. Public domain \(CC0\).*

## Introduction

An elliptic operator on a compact manifold has a finite-dimensional kernel and cokernel. A leaf of a foliation can be noncompact even when the foliated manifold is compact. Its ordinary kernel dimension can therefore be infinite. A transverse measure supplies a trace that measures the kernel projection instead. The resulting difference is the measured index.

Holonomy affects both the Hilbert space and its dimension. We first make that effect explicit, then prove the trace identity behind the heat equation method. We develop the Hilbert-complex arguments, uniform Sobolev estimates and heat expansion needed for finite measured Betti numbers, compute the Euler coefficient in every dimension, and extend these arguments to non-Hausdorff holonomy groupoids. The general symbol characteristic-class calculation remains an explicit requirement for the full formula.

Prerequisites are Transverse measures of foliations, The C*-algebra of a foliation, and Hilbert modules and fields on the leaf space. The trace, its dimension function, and its Fredholm index are supplied by [Weights on random operators and formal dimension](https://kokunoyumeto.github.io/open-math-courses-public/courses/noncommutative-integration/weights-on-random-operators-and-formal-dimension.html), especially its sections on formal dimension and the index. Spectral calculus for closed operators is assumed. Basic references are [Connes], [Atiyah], [Breuer], and [Atiyah–Bott–Patodi].

## 1. Holonomy covers and measured dimensions

Throughout, \(V\) is compact and has a smooth foliation \(F\). A locally finite invariant transverse measure is denoted \(\Lambda\). The associated unit measure is \(\mu\), after choosing a positive leafwise density. It is finite. All the Hilbert spaces below use the holonomy covering \(\widetilde L\) of a leaf, rather than the leaf itself, unless its holonomy is trivial.

For a longitudinal operator \(D\), equivariance of its lift gives equivariant kernel projections \(P_D\). The trace \(\tau_\Lambda\) on the random-operator algebra defines

\[
\dim_\Lambda\ker D=\tau_\Lambda(P_D).
\]

This definition includes isotropy. It does not assert that the kernel is the space of square-summable functions on a lifted Borel transversal.

**Example 1.1 (an atomic leaf with twofold holonomy).** Let

\[
V=(\mathbb T^2\times\mathbb T^1)/\langle g\rangle,
\qquad g(x,y,u)=(x+\tfrac12,y,-u).
\]

The action is free because translation by one half on the first circle has no fixed point. Thus \(V\) is a compact smooth manifold. Its foliation is induced by the horizontal tori, oriented by \(dx\wedge dy\). The leaf at \(u=0\) is

\[
L_0=\mathbb T^2/\langle(x,y)\mapsto(x+\tfrac12,y)\rangle.
\]

Its holonomy is the reflection \(u\mapsto-u\), of order two. Its holonomy covering is \(\mathbb T^2\). The harmonic zero-forms on that covering are the constants, a one-dimensional trivial representation of the deck group. If \(B\) has one point on \(L_0\), its inverse image in the covering has two points, and its square-summable functions form the two-dimensional regular representation. No equivariant unitary identifies these spaces. With any number of points, the lifted counting dimension is zero, a positive even integer, or infinity; it cannot be one.

Give the central leaf transverse atomic mass one, and give the covering torus its flat metric of area one. The leaf has area one half. The constant projection has kernel one on the covering, so its measured trace, obtained by integrating the diagonal over \(L_0\), is one half. Thus

\[
\beta_0=\tfrac12,\qquad\beta_1=1,\qquad\beta_2=\tfrac12.
\]

Their alternating sum is zero, as required by the Euler class of a torus. Every ordinary Borel transversal supported on this leaf has integer mass. This example therefore also distinguishes measured dimension from transversal cardinality.

![The twofold torus cover exchanges the two lifts of a transversal point, but fixes harmonic constants. Their dimensions are two and one; the measured dimension of constants is one half.](../figures/holonomy-counting.png)

*Figure 1. Coordinate fundamental rectangles for Example 1.1. The covering metric is \(dx^2+dy^2\), the deck map is translation by \(1/2\) in \(x\), and the quotient leaf has half the covering area. The two coloured points project to one transversal point. The right panel shows the dimension obstruction; the bottom line gives the atomic measured trace and Euler check. The full argument is Example 1.1.*

*Reference:* [Connes, the remark following Theorem 1] asserts an equivariant counting realization after replacing leaves by their holonomy covers. The finite-holonomy example above prevents that realization for the harmonic constants. The measured projection dimension remains well defined.

More generally, on an atomic compact leaf with finite holonomy of order \(d\), the projection onto constants has measured dimension \(1/d\) when the transverse atom has mass one. Its kernel on the holonomy cover is \(1/\operatorname{vol}(\widetilde L)\), and \(\operatorname{vol}(\widetilde L)=d\operatorname{vol}(L)\). This computation does not change the normalization of the transverse atom.

**Proposition 1.2 (dimension of a counting bundle).** Let \(B,B'\) be Borel transversals. If the bundles over the leaf space
\(H_L=\ell^2(L\cap B)\) and \(H'_L=\ell^2(L\cap B')\)
are measurably unitarily isomorphic, then \(\Lambda(B)=\Lambda(B')\). Thus their counting dimension is independent of the presenting transversal. This assertion concerns ordinary intersections; it does not assert that every holonomy-equivariant harmonic field has such a presentation.

**Proof.** Write the unitary on a leaf as \(U_L\). Measurability means, in the canonical counting bases, that its matrix coefficients on the Borel leaf relation between \(B\) and \(B'\) are Borel. This is equivalent to the usual pulled-back measurable-field condition: Theorem 5.4 of the transverse-measure lesson provides countable local enumerations of the counting bases. Put

\[
a(x,y)=|\langle U_{L_x}e_x,e_y\rangle|^2.
\]

For every \(x\in B\), the sum over \(y\in B'\cap L_x\) is one, because the corresponding column of the unitary has norm one. For every \(y\in B'\), the sum over \(x\in B\cap L_y\) is likewise one, by applying the same statement to its adjoint. Transverse measures of foliations, Theorem 5.7 equates the integrals of these two sums. They are exactly \(\Lambda(B)\) and \(\Lambda(B')\), including the possibility of infinity. This proves the assertion without a trace normalization assumption on isotropy. \(\square\)

## 2. The heat trace identity

Let \(M\) be a von Neumann algebra with a faithful normal semifinite trace \(\tau\). Let \(D\) be a densely defined closed operator from a represented Hilbert space \(H_0\) to \(H_1\), affiliated with the appropriate corners of \(M\). Its polar decomposition is \(D=U|D|\), with

\[
U^*U=1-P_{\ker D},\qquad UU^*=1-P_{\ker D^*}.
\]

**Theorem 2.1 (heat identity).** If \(\tau(e^{-tD^*D})\) and \(\tau(e^{-tDD^*})\) are finite for some \(t>0\), then the two kernel projections have finite trace, and

\[
\tau(P_{\ker D})-\tau(P_{\ker D^*})
=\tau(e^{-tD^*D})-\tau(e^{-tDD^*}).
\]

The same equality holds for every positive time at which the two heat traces are finite.

**Proof.** The kernel projections lie below their respective heat operators, so their traces are finite. Spectral calculus on the complement of the kernels gives

\[
U\bigl(e^{-tD^*D}-P_{\ker D}\bigr)U^*
=e^{-tDD^*}-P_{\ker D^*}.
\]

The trace has equal values on these two positive operators: first use \(\tau(X^*X)=\tau(XX^*)\) with \(X=U(e^{-tD^*D}-P_{\ker D})^{1/2}\), then normality if an unbounded or extended-positive approximation is needed. Add the finite kernel traces and rearrange. All terms being subtracted are finite, so no infinity-minus-infinity occurs. \(\square\)

The index constancy comes from equality of the nonzero spectral parts. It does not require a spectral gap at zero, nor does it require the range of \(D\) to be closed on an individual leaf.

**Corollary 2.2.** Suppose the difference of the two heat traces has an asymptotic expansion at zero in powers of \(t\), with a remainder tending to zero after its constant term. Then every negative-power coefficient in the difference is zero, and its constant coefficient is the measured index.

**Proof.** The difference is the constant given by Theorem 2.1. Multiplication by the most singular power of \(t\) and passage to the limit forces its coefficient to vanish. Repeat for the remaining negative powers. Passing to the limit then gives the constant coefficient. \(\square\)

## 3. Why a diagonal kernel computes the trace

The convolution-kernel trace formula in [Weights on random operators and formal dimension, Corollary 9.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/noncommutative-integration/weights-on-random-operators-and-formal-dimension.html#section-9) specializes, for an invariant transverse measure, to the integral of the squared Hilbert–Schmidt norm of a convolution kernel. For a positive smoothing operator \(K=S^*S\), that squared norm is its diagonal density. Thus, whenever the indicated integrals are finite,

\[
\tau_\Lambda(K)=\int_V\operatorname{tr}k_K(x,x)\,d\mu(x).
\]

To check the identity locally, the kernel of \(S^*S\) at a unit is the integral of \(k_S(\gamma)^*k_S(\gamma)\) over the corresponding fibre. Integrating over units gives precisely the stated convolution trace formula. Positive finite-rank smoothing approximations and normality extend it to positive operators with the relevant smoothing square root. For the heat operator use \(S=e^{-tD^*D/2}\).

Corollary 6.10 supplies these heat kernels and the required row bounds. In detail, let \(S=e^{-t\Delta/2}\). Its row at a point is an \(L^2\) vector, and the semigroup identity \(e^{-t\Delta}=S^*S\) identifies the trace of the unit diagonal with that row's squared Hilbert–Schmidt norm. Integrate and apply Corollary 9.4 to the measurable reduced kernel of \(S\); its absolute convergence on bounded sections of finite-measure support was proved in Corollary 6.10. This proves the heat diagonal formula with a finite integral in the Hausdorff calculus. For a nontrivial modulus the same positive heat formula follows by inversion: the squared norm of a self-adjoint reduced kernel is unchanged under inversion, which converts its weighted integral to its unweighted unit-diagonal integral. The trace identity of Section 2 still requires an invariant measure.

## 4. Reduced cohomology and the metric

A Hilbert complex has densely defined closed operators

\[
d_j:H_j\longrightarrow H_{j+1},\qquad d_{j+1}d_j=0.
\]

Its reduced cohomology is \(\ker d_j/\overline{\operatorname{ran}d_{j-1}}\). Its harmonic subspace is

\[
\mathcal H_j=\ker d_j\cap\ker d_{j-1}^*.
\]

**Proposition 4.1 (Hilbert-complex Hodge decomposition).** Orthogonal projection identifies the reduced cohomology isometrically with \(\mathcal H_j\). Moreover

\[
H_j=\overline{\operatorname{ran}d_{j-1}}
\oplus\mathcal H_j\oplus\overline{\operatorname{ran}d_j^*}.
\]

**Proof.** A closed operator has \((\operatorname{ran}d_j^*)^\perp=\ker d_j\). Within this closed kernel, the orthogonal complement of \(\overline{\operatorname{ran}d_{j-1}}\) is exactly \(\ker d_{j-1}^*\cap\ker d_j\). Orthogonal projection onto that complement gives the quotient isometry and the three summands. \(\square\)

For leafwise exterior differentiation on holonomy covers, use the closed maximal derivative in \(L^2\). It forms a complex because the distributional identity \(d_F^2=0\) holds. Two metrics on \(F\) and two positive densities on compact \(V\) give uniformly equivalent norms in every degree on every cover. The maximal derivative domains, their kernels, and the closures of their ranges therefore agree as topological vector spaces. Projection onto the harmonic representatives for the second metric gives a bounded invertible equivariant map between the two harmonic fields, by Proposition 4.1. The measured dimensions agree by the dimension invariance for an invertible equivariant map in the random-operator lesson.

Corollary 6.6 proves that these harmonic subspaces are exactly the kernels of the self-adjoint differential Hodge Laplacians. It also verifies measurability and square integrability of the fields. Corollary 6.10 proves finiteness of their measured dimensions in the Hausdorff calculus by a finite heat-trace bound. The Hilbert-complex decomposition alone does not imply this finiteness.

## 5. Constants, compactness, and curvature

The leafwise metric lifted from compact \(V\) is complete on each holonomy cover. One justification uses its geodesic flow: the unit leafwise tangent bundle over \(V\) is compact, and its smooth geodesic vector field has a complete flow. Lifting geodesics to a covering preserves their existence for all time. The leafwise coordinate charts also give a common positive radius and a positive lower bound for the volume of metric balls of that radius in every cover. Shrink finitely many charts and compare their metrics with Euclidean metrics on the remaining compact chart supports.

**Lemma 5.1.** A noncompact holonomy cover has infinite volume. A square-integrable function killed by the closed exterior derivative is constant, and hence is zero on a noncompact cover. On a compact connected cover its space is one-dimensional.

**Proof.** A complete Riemannian manifold has compact closed bounded balls. A noncompact such manifold therefore has infinitely many mutually separated points, by choosing each new point outside the finitely many fixed-radius balls around the previous ones. Balls of a sufficiently small common radius around these points are disjoint and each has the positive volume bound above. Their total volume is infinite. A function with distributional derivative zero is constant on every connected coordinate ball; overlapping balls and connectedness make the constant global. Its \(L^2\) norm is finite only if the constant is zero or the total volume is finite. \(\square\)

The cover is compact exactly when the leaf is compact with finite holonomy. One direction is immediate from a finite covering. For the other, the image of a compact cover is a compact leaf in its intrinsic topology, and its discrete covering fibres are compact, hence finite. This identifies precisely which leaves can contribute degree-zero harmonic forms. Orientation and the Hodge star give the same conclusion in the top degree.

Corollary 6.20 and Proposition 6.21 prove the measured Euler formula, including non-Hausdorff holonomy groupoids:

\[
\sum_{j=0}^p(-1)^j\beta_j
=\langle e(F),[C_\Lambda]\rangle,
\qquad\beta_j=\dim_\Lambda\mathcal H_j<\infty.
\tag{3}
\]

For oriented two-dimensional leaves, Chern–Weil normalization is

\[
\langle e(F),[C_\Lambda]\rangle
=\frac1{2\pi}\int_VK\,d\mu.
\]

If compact leaves with finite holonomy are negligible, Lemma 5.1 and the Hodge star give \(\beta_0=\beta_2=0\). Consequently \(3\) gives

\[
\frac1{2\pi}\int_VK\,d\mu=-\beta_1\le0.
\]

Corollary 6.16 computes the first Laplace-type coefficient for this surface instance of \(3\). Proposition 6.21 removes the Hausdorff restriction. Corollary 6.22 proves the stronger inequality when only sphere leaves are negligible, and Proposition 6.23 proves the nearby compact-leaf assertion for a compact leaf with finite holonomy.

## 6. The full index formula and its analytic requirements

For a longitudinal elliptic differential operator \(D:E_0\to E_1\), its principal symbol determines a compactly supported K-class on \(F^*\). The measured foliation index theorem expresses its measured index by the Chern character of that symbol, the Todd class of \(F\otimes\mathbb C\), and the Ruelle–Sullivan current. There are signs depending on the chosen orientation for cotangent-fibre integration; those must be fixed with the symbol convention before using a numerical formula. For a longitudinal spin-c Dirac operator twisted by \(E\), the unambiguous usual Dirac normalization is

\[
\operatorname{Ind}_\Lambda(D_E^+)
=C_\Lambda\!\left(
\left[\widehat A(F)e^{c_1(\det S)/2}\operatorname{ch}(E)\right]_p
\right).
\tag{4}
\]

Here \(S\) is the spin-c structure and the subscript selects degree \(p\). For a connection \(\nabla=d+A\) we use \(\operatorname{ch}(E)=\operatorname{tr}\exp(iR^E/(2\pi))\), with the same convention for the determinant-line first Chern class. Lemma 6.24 fixes chirality, and Theorem 6.26 proves this precise sign convention. The expression makes sense through leafwise restriction of the characteristic forms.

### Uniform chart calculus

We first prove the analytic facts that do not require the local characteristic-class calculation. In this subsection \(V\) is compact, \(G\) is Hausdorff, the bundles have finite rank, and all coefficients are \(C^{\infty,0}\). The compactly supported kernel calculus is first constructed under the Hausdorff assumption. Proposition 6.21 then proves its extension using non-Hausdorff chart sums.

Take finitely many relatively compact plaque boxes and compactly supported cutoffs. In one box, a symbol of order \(m\) satisfies

\[
\|\partial_t^\alpha\partial_\xi^\beta a(t,\xi,u)\|
\le C_{\alpha\beta}\langle\xi\rangle^{m-|\beta|},
\qquad \langle\xi\rangle=(1+|\xi|^2)^{1/2},
\]

uniformly in \(u\) on the compact transverse support. The same derivatives are continuous in \(u\). Quantization, with a cutoff in the input variable, uses

\[
P_u v(t)=(2\pi)^{-p}\int e^{i(t-t')\cdot\xi}
a(t,\xi,u)v(t')\,dt'\,d\xi .
\]

These oscillatory integrals are defined by inserting frequency cutoffs and integrating by parts before removing them. Lift their kernels to the corresponding pair-plaque groupoid charts, and add smooth compact arrow kernels. Write \(\Psi_c^m(E_0,E_1)\) for the resulting class. Its support is compact in \(G\), and its lifts to the covers are equivariant.

**Lemma 6.1 (local estimates and coordinate invariance).** These chart operators are bounded \(H^{s+m}\to H^s\) for every real \(s\), with constants controlled by finitely many symbol seminorms on the fixed charts. The constants are uniform in \(u\). The symbol class and its order are unchanged under a \(C^{\infty,0}\) change of plaque coordinates or bundle trivialization.

**Proof.** For a left symbol compactly supported in \(t\), its Fourier transform in that variable satisfies

\[
\|\widehat a(\eta-\xi,\xi,u)\|
\le C_N\langle\eta-\xi\rangle^{-N}\langle\xi\rangle^m.
\]

This follows by integrating by parts \(N\) times in \(t\); compact support bounds the resulting \(L^1\) norms by the corresponding symbol seminorms. On Fourier transforms, the weighted operator has kernel
\(\langle\eta\rangle^s\widehat a(\eta-\xi,\xi,u)\langle\xi\rangle^{-s-m}\).
The inequality
\(\langle\eta\rangle^s/\langle\xi\rangle^s\le 2^{|s|/2}\langle\eta-\xi\rangle^{|s|}\)
reduces it to \(C\langle\eta-\xi\rangle^{-N+|s|}\). Choose \(N>|s|+p\). Its integrals in either variable are bounded by the same constant, so the Schur estimate proves boundedness. Input cutoffs are bounded on all these Sobolev spaces: for nonnegative integer order use the product rule, for negative order use duality, and for real order interpolate the Fourier weighted Hilbert spaces. The interpolation bound follows from the three-lines theorem applied to the conjugated operator with weights \(\langle D\rangle^z\).

For coordinate invariance, let \(\kappa\) be a plaque coordinate change. Near the diagonal put

\[
M(t,t')=\int_0^1 D\kappa(t'+r(t-t'))\,dr .
\]

After shrinking the coordinate neighbourhood, this matrix is invertible, and
\(\kappa(t)-\kappa(t')=M(t,t')(t-t')\).
The substitution \(\eta=M(t,t')^T\xi\) writes the transformed kernel with the usual phase \(e^{i(t-t')\cdot\eta}\). Its amplitude has order \(m\). Indeed the inverse matrix and its derivatives are bounded on the compact chart supports; an \(x\)-derivative of \(a(\kappa(t),M^{-T}\eta,u)\) produces factors of \(\eta\) together with frequency derivatives of \(a\), preserving the order, whereas an \(\eta\)-derivative lowers it by one. Jacobians, half-density changes, and bundle transition matrices have bounded leafwise derivatives there.

An amplitude depending on \(t'\) reduces to a left symbol by Taylor expansion in \(t'-t\). Each factor \((t'-t)^\alpha\) transfers to \(\partial_\eta^\alpha\) by integration by parts. The remainder after \(N\) terms has order \(m-N\); its estimates follow by applying \((1-\Delta_{t'})^L\) to make its frequency integral absolutely convergent, with \(L\) arbitrarily large. Away from the diagonal the phase has nonzero gradient, and repeated integration by parts makes the kernel smooth. This proves invariance. All arguments differentiate only along plaques, so their bounds retain transverse continuity without requiring transverse derivatives. \(\square\)

The coordinate changes on compactly supported plaque pieces are uniformly bounded on \(H^s\). For integer \(s\ge0\) this follows from the chain rule, change of variables and bounded derivatives of the coordinate map and its inverse; duality and the same interpolation argument give all real \(s\).

**Lemma 6.2 (composition, adjoints and compactness).** The compactly supported longitudinal classes satisfy

\[
\Psi_c^m\Psi_c^n\subset\Psi_c^{m+n},
\qquad(\Psi_c^m)^*=\Psi_c^m.
\]

Order-zero operators have uniformly bounded regular representations. Scalar negative-order operators belong to \(A\). If \(m<-p/2\), the kernel is a Borel function and has uniformly bounded row and column \(L^2\) norms on the holonomy covers. The same statement holds for finite-rank bundle kernels, using the Hilbert–Schmidt norm.

**Proof.** In one coordinate box the symbol of a composite has expansion

\[
a\# b\sim
\sum_\alpha\frac1{\alpha!}\,
(\partial_\xi^\alpha a)(D_t^\alpha b),
\qquad D_t=\frac1i\partial_t .
\]

To verify both the expansion and the order of its remainder, the exact oscillatory formula is

\[
(a\# b)(t,\xi)
=(2\pi)^{-p}\int e^{-iy\cdot\eta}
a(t,\xi+\eta)b(t+y,\xi)\,dy\,d\eta .
\]

Taylor-expand the second factor in \(y\) through degree \(N-1\). Transferring \(y^\alpha\) onto the first factor gives the displayed terms, including \(1/i\) and the factorial. In the integral remainder there are \(N\) frequency derivatives of \(a\), of order \(m-N\). Integrating by parts sufficiently many times in \(y\) gives decay in \(\eta\). The inequality
\(\langle\xi+\eta\rangle^r\le 2^{|r|/2}\langle\xi\rangle^r\langle\eta\rangle^{|r|}\)
shows that this decay makes the remainder and each of its derivatives bounded in order \(m+n-N\). This calculation is legitimate with frequency regularizers; these integrable bounds allow their removal. Smooth off-diagonal pieces compose to smooth pieces: differentiating their integral kernels and integrating a compactly supported distribution against a smooth test preserve all smooth seminorms. The adjoint calculation is the same Taylor argument applied to the conjugate transpose of the reversed kernel.

For different boxes, use a finite cover of the compact overlap by smaller compatible foliation boxes. Coordinate invariance from Lemma 6.1 gives the same local calculation. Outside a common neighbourhood of the units, a pseudodifferential kernel is smooth. Products have compact support: the composable part of the product of two compact supports is closed, since equality of their source and range is a closed condition in the Hausdorff unit manifold, and multiplication maps that compact set to a compact set. These facts establish the global composition assertion.

In a lifted chart a source or range cover splits into disjoint plaque sheets, and its localized operator is the direct sum of the corresponding plaque operator, with zero outside those sheets. Lemma 6.1 bounds this direct sum uniformly. A finite chart sum and the Schur bound for smooth compact arrow kernels give the order-zero assertion.

For \(m<0\), replace \(a\) by \(a(t,\xi,u)\chi(\xi/R)\), with \(\chi=1\) near zero. The difference has order-zero seminorms, involving the required \(t\)-derivatives, bounded by \(C R^m\). The Fourier-Schur proof of Lemma 6.1 therefore makes its operator norm tend to zero uniformly in the parameter and in every lifted sheet. The truncated kernel, with its input cutoff, is smooth and compactly supported. Thus its extension is an element of the smooth algebra and the limit belongs to \(A\).

For \(m<-p/2\), Parseval gives for a left-symbol kernel on one plaque

\[
\int|K(t,t',u)|_{HS}^2\,dt'
=(2\pi)^{-p}\int|a(t,\xi,u)|_{HS}^2\,d\xi
\le C\int\langle\xi\rangle^{2m}\,d\xi<\infty
\]

uniformly in \(t,u\). Cutoffs only improve this bound. Applying it to the adjoint symbol proves the column bound as well. A general localized kernel has the same assertion by its left-symbol reduction and the smooth remainder. Each compact arrow set is covered by finitely many smaller arrow charts; summing their fibre bounds proves the global result, including the inverse-kernel version
\(\sup_y\int\|k(\gamma^{-1})\|_{HS}^2\,d\nu^y(\gamma)<\infty\).
The estimates also construct its Borel kernel as the \(L^2\) limit of the frequency truncations, with the off-diagonal smooth values. No global Hilbert–Schmidt assertion on an entire infinite cover is made. \(\square\)

### Parametrices and differential domains

**Theorem 6.3 (uniform elliptic parametrix).** If \(P\in\Psi_c^m(E_0,E_1)\) has invertible principal symbol away from the zero section, there is \(Q\in\Psi_c^{-m}(E_1,E_0)\) such that \(PQ-1\) and \(QP-1\) are smooth compact arrow kernels.

**Proof.** On the compact unit cosphere bundle the inverse principal symbol and each of its leafwise derivatives are bounded. Homogeneity therefore gives inverse-symbol estimates of order \(-m\) for large \(|\xi|\). Cut off near zero, quantize in finitely many boxes, and use a partition of unity to obtain \(Q_0\) with the inverse principal symbol. Lemma 6.2 gives \(R=1-PQ_0\) of order \(-1\). Formally the right inverse is
\(Q_0(1+R+R^2+\cdots)\). Its \(j\)-th symbol term has order \(-m-j\), and the remainder after \(N\) terms in its product with \(P\) has order \(-N\).

We spell out the summation step so that parameter uniformity is retained. For symbol terms \(q_j\) of order \(-m-j\), choose radii \(R_j\to\infty\) and a frequency cutoff \(\chi\), zero near zero and one outside a larger ball. Increase \(R_j\) until the first \(j\) derivative seminorms of \(\chi(\xi/R_j)q_j\), measured in order \(-m-j/2\), are at most \(2^{-j}\) on every chart of the finite atlas. This is possible because the stronger order bound has the extra factor \(\langle\xi\rangle^{-j/2}\) on the support of that cutoff; its derivatives have the same gain there. The series

\[
q=q_0+\sum_{j\ge1}\chi(\xi/R_j)q_j
\]

then converges in every required symbol seminorm of order \(-m\). For a fixed \(N\), the tail with \(j\ge2N\) converges in order \(-m-N\); the finitely many differences between \(q_j\) and their cutoffs have bounded frequency support and are smoothing symbols. Thus \(q\sim\sum q_j\), with all estimates uniform in the transverse parameter. The uniform convergence of each leafwise derivative also preserves its transverse continuity.

Quantize this formal inverse with fixed small input cutoffs in the finitely many boxes. Coordinate invariance permits the symbols to be reconciled on overlaps to every order; changing a cutoff or the local representative changes the operator only by a smooth compact kernel. The product \(PQ-1\) is consequently smoothing. Its actual arrow support is compact, contained in the product of the supports of \(P,Q\), together with the compact unit manifold. The construction uses fixed chart supports; it does not sum the growing supports of the actual operators \(Q_0R^j\).

Construct a left inverse \(Q_L\) by the same argument. If \(PQ=1+S_R\) and \(Q_LP=1+S_L\), then
\(Q_L-Q=S_LQ-Q_LS_R\), which is smoothing by Lemma 6.2. Hence \(QP-1\) is smoothing as well. \(\square\)

**Corollary 6.4 (uniform elliptic estimate).** If \(P_1,P_2\in\Psi_c^m(E_0,E_1)\) and \(P_2\) is elliptic, then

\[
\|P_{1,x}v\|_2\le C\bigl(\|P_{2,x}v\|_2+\|v\|_2\bigr)
\quad(v\in C_c^\infty(G^x,s^*E_0)),
\]

with \(C\) independent of \(x\).

**Proof.** Choose \(Q_2P_2=1+R\). Then
\(P_1v=P_1Q_2P_2v-P_1Rv\).
The first coefficient \(P_1Q_2\) has order zero and the second \(P_1R\) is smoothing. Their uniform \(L^2\) bounds from Lemma 6.2 give the assertion. \(\square\)

For domains, fix finitely many cutoffs \(\phi_i\) in plaque boxes with \(\sum_i\phi_i^2=1\). Such cutoffs follow by normalizing finitely many nonnegative bumps whose positive sets cover \(V\). In a cover \(G^x\), each inverse image of a box is a disjoint union of plaque sheets. Define the coordinate Sobolev norm by

\[
\|v\|_{s,x}^2
=\sum_i\sum_{\text{plaque sheets }B}
\|(\phi_i\circ s)v|_B\|_{H^s(\mathbb R^p)}^2,
\]

after extending the compactly supported coordinate piece by zero and applying the coordinate half-density and bundle trivializations. For negative orders this defines the corresponding distribution space; its norm is equivalent to the dual norm for positive order.

Changing the finite chart data gives uniformly equivalent norms. To see this, refine each compact chart overlap by finitely many compatible smaller boxes. Each lifted smaller box belongs to one sheet of either chart; the number of these pieces is bounded independently of the cover. Multiplication and coordinate-change bounds after Lemma 6.1 therefore compare each localized norm to finitely many norms for the other atlas. Sum over sheets, using the bounded multiplicity of those overlap pieces. The reconstruction \(v=\sum_i(\phi_i\circ s)[(\phi_i\circ s)v]\) gives the reverse inequality. This also shows that \(\Psi_c^m\) acts uniformly \(H^{s+m}\to H^s\) on every cover; smooth compact kernels act \(H^s\to H^{s'}\) for every pair of real orders.

Compactly supported smooth sections are dense in these spaces. For each \(i\), truncate the square-summable family of localized sheets to a finite family. On those sheets, approximate the compactly supported coordinate distributions by smooth mollifications in \(H^s\), keeping the support inside the chart. Multiply again by \(\phi_i\) and sum. The reconstruction and overlap bounds just proved give convergence in the global norm. Each finite sum has compact support on the cover.

**Theorem 6.5 (minimal and maximal domains).** Let \(D\) be an elliptic longitudinal differential operator of positive order \(m\). On every cover the closure of
\(D_x:C_c^\infty(G^x,s^*E_0)\to L^2(G^x,s^*E_1)\)
has domain

\[
\{v\in L^2:D_xv\in L^2\text{ in distributions}\}=H^m(G^x,s^*E_0).
\]

Its graph norm is uniformly equivalent to the coordinate \(H^m\) norm. The adjoint of this closure is the closure of the formal adjoint. In particular a formally self-adjoint elliptic differential operator is essentially self-adjoint.

**Proof.** Let \(Q D=1+R\) be a parametrix. Its compact reduced arrow support makes its kernel properly supported on each cover: a compact set of output points, multiplied by that compact arrow support, gives a compact set of possible input points, and the same holds with input and output reversed. Thus the kernel identities act on distributions as well as on test sections. If \(v,D_xv\in L^2\), then

\[
v=Q_xD_xv-R_xv\in H^m,\qquad
\|v\|_{m,x}\le C(\|D_xv\|_2+\|v\|_2).
\]

Conversely \(D:H^m\to L^2\) is bounded by the chart estimate. The density construction just given approximates every \(v\in H^m\) by compact smooth sections in \(H^m\), hence also in the graph norm. This proves equality with the minimal closure and the graph-norm equivalence. It uses compact chart support and square summability on the sheets, without assuming that the cover itself is compact.

Distributional integration by parts says that the adjoint of the minimal \(D\) is the maximal formal adjoint: testing against every compact smooth section is exactly the definition that its distributional formal adjoint lie in \(L^2\). Apply the already proved equality of minimal and maximal domains to that elliptic formal adjoint. If it equals \(D\) on tests, the closure equals its adjoint and is self-adjoint. \(\square\)

For \(D^*D\), this also proves that the self-adjoint realization of the formal product equals the Hilbert-space product of the closed operators. The latter is a self-adjoint extension of the formal positive product on tests, and the formal product has a unique self-adjoint extension by Theorem 6.5.

**Corollary 6.6 (the harmonic fields).** The kernel of the self-adjoint differential Hodge Laplacian on a cover is exactly the harmonic subspace in Section 4. Its square-integrable forms are closed and co-closed. These fields are measurable square-integrable groupoid representations; their isomorphism class is independent of the leafwise metric. In degree zero their fibres have the description of Lemma 5.1.

**Proof.** The closed maximal exterior derivatives form the Hilbert complex of Section 4. Its closed nonnegative quadratic form
\(v\mapsto\|d v\|^2+\|d^*v\|^2\)
defines a self-adjoint Hilbert-complex Laplacian. On compact smooth sections it is the formal differential Hodge Laplacian, an elliptic operator of order two. Theorem 6.5 makes that differential operator essentially self-adjoint, so these two realizations agree. The zero space of the quadratic form is precisely \(\ker d\cap\ker d^*\), proving closedness and co-closedness.

The field is measurable as follows. Countably many chart test sections, with rational polynomial approximations and cutoffs, give dense graph families for the closed differential operators in each fibre by Theorem 6.5. Their inner products and the inner products of their images are Borel functions of the base point. Gram matrix orthogonalization consequently gives measurable graph projections and resolvents. Spectral calculus then makes
\(P_{\ker\Delta}=\operatorname{s\!-\!lim}_{n\to\infty}(1+n\Delta)^{-1}\)
a measurable equivariant projection. The regular field with its finite-rank coefficient bundle is square integrable, and its closed projected subrepresentation is square integrable by Proposition 4.6 of [Square-integrable representations and random operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/noncommutative-integration/square-integrable-representations-and-random-operators.html#section-4).

Uniform equivalence of the metric norms on compact \(V\) identifies the maximal derivative domains, kernels and closed ranges for the two metrics. Their reduced cohomology spaces are the same topological quotient. Proposition 4.1 gives a bounded invertible equivariant map between its two harmonic realizations. Taking the polar part makes it unitary if desired, without changing equivariance. This proves metric independence; the dimension invariance import in Section 4 applies. For functions, \(d v=0\) makes them constant, and Lemma 5.1 decides when the constant is square integrable. \(\square\)

For \(p=0\), the cover of a leaf is a point. The corresponding operators are finite-dimensional bundle maps, every order-zero domain is the whole fibre, and the smooth algebra is the algebra of continuous finite-rank bundle maps on the compact unit space. The domain, compactness, and harmonic assertions are immediate. Parametrix assertions modulo smoothing are vacuous there because that entire algebra is smoothing. The positive-order estimates above concern \(p\ge1\).


### Spectral Sobolev spaces and finite weights

The next step compares the coordinate spaces with the spaces defined by the differential operator itself. Fix an elliptic differential operator \(D:E\to E'\) of positive order \(m\), put \(\Delta=D^*D\), and write \(A=1+\Delta\). The notation \(A\) in this subsection denotes this positive unbounded operator, rather than the foliation C*-algebra. On each cover define

\[
W_x^s=\operatorname{dom}A_x^{s/(2m)},\qquad
\|v\|_{W_x^s}=\|A_x^{s/(2m)}v\|_2
\quad(s\ge0).
\]

For \(s<0\), complete \(L^2\) in this norm. The resulting elements are distributions, through the identification below. Spectral calculus makes these fields measurable and equivariant. The map \(A_x^{s/(2m)}:W_x^s\to L^2\), with its continuous interpretation for negative \(s\), is unitary.

**Lemma 6.7 (interpolation of Hilbert scales).** If \(B\ge1\) is a positive self-adjoint operator, its spaces with norms \(\|B^r v\|\) interpolate according to the affine exponent: between exponents \(r_0,r_1\), parameter \(0<\theta<1\) gives exponent \((1-\theta)r_0+\theta r_1\). The Fourier Sobolev spaces and their square-summable direct sums have the same property. A space obtained from such direct sums by bounded localization and reconstruction has this property up to equivalence of norms.

**Proof.** Here interpolation uses functions analytic in the strip \(0<\operatorname{Re}z<1\), with boundary norms bounded in the two endpoint spaces; the norm at \(\theta\) is the infimum of those bounds. In a spectral representation write \(b\ge1\) for the multiplier defining \(B\), and put \(r(z)=(1-z)r_0+zr_1\). For a vector with bounded spectral support, the function
\(F(z)=b^{r(\theta)-r(z)}v\)
has value \(v\) at \(\theta\) and has boundary norm \(\|b^{r(\theta)}v\|\) on both sides. If decay at the ends of the strip is required, multiply by \(e^{\varepsilon(z-\theta)^2}\) and let \(\varepsilon\downarrow0\). Spectral truncation gives the upper bound for every vector in that weighted space.

For the reverse bound, pair an admissible \(F(z)\) with a bounded-spectral-support unit vector after multiplying its spectral coordinate by \(b^{r(z)}\). This is an analytic scalar function. Cauchy–Schwarz bounds its modulus on each boundary by the corresponding endpoint norm, since \(b^{i\operatorname{Im}r(z)}\) is unitary. The three-lines inequality bounds its value at \(\theta\) by the larger boundary bound. Taking the supremum over such unit vectors proves the lower bound. The three-lines inequality itself follows by applying the maximum principle on finite rectangles to the function divided by the exponential of the affine interpolation of the logarithms of its boundary bounds, and then multiplying by \(e^{\varepsilon z^2}\) to control the horizontal sides. Let the rectangle height tend to infinity and then let \(\varepsilon\downarrow0\).

Fourier transformation identifies \(H^r(\mathbb R^p)\) with the spectral multiplier \(\langle\xi\rangle^r\); adding a counting measure for the sheet index proves the direct-sum assertion. Finally, suppose \(J\) localizes a space into a direct sum, \(R\) reconstructs it, and \(RJ=1\), with both maps bounded at the endpoints. Applying \(J\) or \(R\) to an admissible analytic function preserves analyticity and bounds its boundary norms. Thus both maps are bounded between the interpolated spaces. The identity \(RJ=1\) then gives equivalence with the intermediate direct-sum localization norm. \(\square\)

**Theorem 6.8 (all real orders).** The identity on compact smooth sections extends to an equivariant isomorphism

\[
W_x^s\cong H^s(G^x,s^*E)
\]

for every real \(s\). Its norm and inverse norm are bounded independently of \(x\). Consequently every \(P\in\Psi_c^q(E,E')\) acts uniformly \(W^{s+q}(E)\to W^s(E')\), where either bundle may use its own positive elliptic differential operator to define its scale.

**Proof.** For an integer \(k\ge1\), the formal differential operator \((1+D^*D)^k\) is elliptic, formally self-adjoint and positive on test sections, with order \(2mk\). Its spectral realization \(A_x^k\) is a self-adjoint extension of that formal operator: tests lie in every power domain because applying the differential expression preserves compact smooth support. Theorem 6.5 gives uniqueness of the self-adjoint extension. It therefore identifies
\(\operatorname{dom}A_x^k=H^{2mk}\), with uniform equivalence between \(\|A_x^k v\|\) and the coordinate norm. The term \(\|v\|\) in the graph norm is absorbed by \(A_x\ge1\). The zero-order endpoint is \(L^2\).

Use the localization \(J_x\) from the norm preceding Theorem 6.5. Reconstruction \(R_x\) multiplies each coordinate component again by its cutoff and sums over sheets, so \(R_xJ_x=1\). The chart-overlap estimates prove that both maps are bounded at every required coordinate order, with constants independent of the cover. Lemma 6.7 therefore identifies interpolation between two coordinate orders with the coordinate space at the intermediate order. Apply the same lemma to \(A_x\) and to the identity map at two successive endpoints \(2mk,2m(k+1)\). This proves the assertion for every \(s\ge0\), with uniform constants for each fixed \(s\).

Under the \(L^2\) pairing, the dual of the positive spectral space is the completed negative spectral space, by the weighted Cauchy–Schwarz inequality and its equality case in spectral coordinates. The coordinate negative space is likewise the dual of its positive space up to the uniform localization constants. Duality proves the assertion for every \(s<0\). All identifications extend the same identity on distributions, so they commute with groupoid translations. The last assertion follows from the coordinate operator bounds and these uniformly equivalent norms. \(\square\)

For a local family \(P_u\), its plaque norm must specify the space on which the kernel acts. With full Euclidean Sobolev norms after zero extension, a fixed relatively compact plaque box inside a larger coordinate box gives

\[
\|P'\|_{W^s,W^{s'}}
\le C\sup_u\|P_u\|_{H^s(\mathbb R^p),H^{s'}(\mathbb R^p)}.
\]

Indeed insert fixed input and output cutoffs equal to one on the smaller box. The lifted operator is the direct sum of the plaque operators on its sheets. Restriction with the input cutoff and reconstruction with the output cutoff have bounded coordinate Sobolev norms; summing the squared sheet norms and applying Theorem 6.8 gives the inequality. The constant depends on the two boxes, the cutoffs and the orders, and not on the kernel. Intrinsic Sobolev norms on an open plaque, or boxes with uncontrolled geometry at their boundary, require their own extension estimates; they cannot be substituted for this norm convention without justification.

**Theorem 6.9 (weighted trace estimate).** Let \(\Lambda\) be locally finite with smooth positive modulus \(\delta\), and let \(\Phi\) be the normal random-operator weight associated to multiplication by \(\delta^{-1}\). For each \(s>p/2\), there is a finite constant \(C_s\) such that every measured equivariant bounded operator \(T\) extending boundedly from \(W^{-s}\) to \(W^s\) is in the linear domain of \(\Phi\), with

\[
|\Phi(T)|\le C_s\|T\|_{W^{-s},W^s}.
\]

In particular this proves the estimate with the stronger hypothesis \(s>p\). No invariance assumption \(\delta=1\) is needed for this estimate.

**Proof.** Put \(B_s=A^{-s/(2m)}\). First we show that \(\Phi(B_s^2)<\infty\), without assuming that this spectral operator is already in the foliation C*-algebra. Choose an elliptic compactly supported pseudodifferential operator \(P\) of order \(-s\), with principal symbol \(|\xi|^{-s}\) times the identity away from zero. A smooth positive metric on \(F\), a frequency cutoff near zero and the finite quantization atlas construct it. A parametrix \(Q\) of order \(s\) gives \(QP=1+R\), with \(R\) smoothing. For every \(v\in L^2\), the identity on distributions and the uniform Sobolev bounds give

\[
\|B_s v\|_2=\|v\|_{W^{-s}}
\le C\|v\|_{H^{-s}}
\le C'\bigl(\|Pv\|_2+\|Rv\|_2\bigr).
\]

Squaring this inequality gives an operator inequality
\(B_s^2\le C''(P^*P+R^*R)\).
The kernels of \(P,R\) have compact arrow support. Lemma 6.2 bounds their fibre squared Hilbert–Schmidt integrals because \(-s<-p/2\). The row bounds and Cauchy–Schwarz make their kernel integrals absolutely convergent on bounded sections of finite-measure support, as required for the convolution formula. The unit measure \(\mu=\Lambda_\nu\) is finite by transverse local finiteness, the smooth positive leafwise density and compactness of \(V\). On the compact kernel supports, \(\delta^{-1}\) is bounded. Corollary 9.4 of the random-operator weight lesson consequently gives

\[
\Phi(P^*P)+\Phi(R^*R)<\infty.
\]

Positivity and monotonicity of \(\Phi\) imply \(\Phi(B_s^2)<\infty\). For zero-dimensional leaves, the regular field has finite-rank fibres and the same conclusion follows directly by integrating its finite-dimensional identity over finite \(\mu\).

The spectral isometries of the two Sobolev spaces factor the given operator as
\(T=B_s S B_s\), where \(S\) is measured equivariant and
\(\|S\|=\|T\|_{W^{-s},W^s}\).
In particular \(B_s\) lies in the left square-integrable ideal \(\mathcal N_\Phi\), and so does \(SB_s\), since
\((SB_s)^*(SB_s)\le\|S\|^2B_s^2\).
Thus \(T\) lies in the linear domain \(\mathcal M_\Phi=\operatorname{span}\mathcal N_\Phi^*\mathcal N_\Phi\). The weight Cauchy–Schwarz inequality, obtained by applying positivity to \(\Phi((x+zy)^*(x+zy))\) and minimizing in \(z\in\mathbb C\), gives

\[
|\Phi(B_s S B_s)|
\le \Phi(B_s^2)^{1/2}
\Phi(B_s S^*S B_s)^{1/2}
\le\|S\|\Phi(B_s^2).
\]

Take \(C_s=\Phi(B_s^2)\). This argument uses positivity and Cauchy–Schwarz for the weight, rather than a trace interchange. \(\square\)

**Corollary 6.10 (finite heat weights and kernel dimensions).** For every \(t>0\),
\(\Phi(e^{-t\Delta})<\infty\).
The heat operator has a leafwise smooth measurable equivariant kernel. When \(\delta=1\), the kernel of each elliptic differential operator and every harmonic-form field have finite measured dimension under the Hausdorff standing assumptions of this subsection.

**Proof.** For any \(s>p/2\), spectral calculus gives

\[
\|e^{-t\Delta}\|_{W^{-s},W^s}
=\|A^{s/m}e^{-t\Delta}\|
\le\sup_{\lambda\ge0}(1+\lambda)^{s/m}e^{-t\lambda}<\infty.
\]

The same argument works for arbitrarily large Sobolev orders on either side. Theorem 6.9 proves finite heat weight. It also gives, for \(0<t\le1\), the bound \(\Phi(e^{-t\Delta})\le C'_s t^{-s/m}\), since \((1+\lambda)^r e^{-t\lambda}\le t^{-r}\sup_{q\ge0}(1+q)^r e^{-q}\) for \(r=s/m\).

Here is the kernel assertion in detail. Fourier inversion and Cauchy–Schwarz bound point evaluation of \(\partial^\alpha v\) on a fixed plaque by \(C\|v\|_{H^r}\) whenever \(r>p/2+|\alpha|\): the integral \(\int\langle\xi\rangle^{-2r}|\xi|^{2|\alpha|}\,d\xi\) is finite. Local cutoffs and Theorem 6.8 make these constants uniform on the covers. The point masses and all their derivatives are therefore continuous vectors in sufficiently negative Sobolev spaces. Apply the heat operator to these input point masses and evaluate at the output point. Its bounds between arbitrarily high negative and positive orders give a smooth kernel, with all leafwise derivatives uniformly bounded on smaller plaque boxes. Differentiation of the point masses in negative Sobolev norm follows by dominated convergence of their Fourier transforms, so this construction also proves joint smoothness in the two plaque variables.

Measurability follows by approximating the point masses in negative Sobolev norm by chart mollifiers. Their pairings with the measured heat field are measurable, and the just-proved bounds give pointwise limits for the kernel and each derivative. Equivariance follows from that of spectral calculus. For a fixed output point the kernel row is an \(L^2\) vector: evaluation after the bounded map \(e^{-t\Delta}:L^2\to H^r\), \(r>p/2\), is a bounded functional on \(L^2\), so its Riesz vector is that row. The analogous statement follows for columns by self-adjointness. Consequently the kernel formula is absolutely convergent on bounded sections with finite-measure support, by Cauchy–Schwarz. This verifies the kernel hypothesis of Corollary 9.4 rather than assuming it from formal smoothing notation.

Finally, \(P_{\ker\Delta}\le e^{-t\Delta}\). For \(\delta=1\), \(\Phi=\tau_\Lambda\), so this projection has finite trace. Apply this to \(D^*D\) and, separately, to the Hodge Laplacians. Their kernels are the fields already identified above. \(\square\)

Applying the same result to \(DD^*\) makes both heat traces in Theorem 2.1 finite for every positive time. Thus its measured-index identity now applies to all these elliptic differential operators in the Hausdorff calculus. A small-time asymptotic expansion and its local characteristic coefficient are additional assertions: the polynomial bound in Corollary 6.10 does not determine them.


### Constructing the small-time expansion

We now construct the expansion, while leaving the identification of its constant supertrace with a characteristic form for the next step. The hypotheses remain the compact Hausdorff longitudinal calculus, finite-rank bundles, and \(C^{\infty,0}\) coefficients. Write \(d=2m\) for the order of \(\Delta=D^*D\). In a unitary coordinate half-density frame its differential symbol is

\[
h(x,\xi,u)=\sum_{j=0}^d h_{d-j}(x,\xi,u),
\]

where each term is polynomial homogeneous of degree \(d-j\) in \(\xi\). Its leading term is Hermitian, with
\(h_d(x,\xi,u)\ge c|\xi|^d I\) on the fixed chart supports, for a common \(c>0\). This follows from \(h_d=\sigma_m(D)^*\sigma_m(D)\) and compactness of the unit cosphere bundle. Extend these coefficients to a larger Euclidean chart with bounded leafwise derivatives. The leading term can be extended with the same positivity by blending it, outside the smaller chart, with \(|\xi|^dI\); the local construction below uses only this positivity and agreement on the original chart.

**Lemma 6.11 (the local heat symbols).** There are symbols \(v_k(t,x,\xi,u)\), \(k\ge0\), for \(t>0\), such that

\[
v_k(t,x,\xi,u)=t^{k/d}v_k(1,x,t^{1/d}\xi,u).
\]

The profiles at time one are Schwartz functions of \(\xi\), uniformly with every leafwise derivative on compact chart supports, and continuous in \(u\). For \(v^{(N)}=\sum_{k=0}^N v_k\), the symbol of
\((\partial_t+\Delta)\operatorname{Op}(v^{(N)})\)
is a finite sum of terms scaling as
\(t^{-1+k/d}r_k(1,x,t^{1/d}\xi,u)\), with \(N+1\le k\le N+d\) and uniformly Schwartz profiles.

**Proof.** Set \(v_0=e^{-t h_d}\). For \(k>0\), solve the matrix equation

\[
\begin{split}
(\partial_t+h_d)v_k&=-g_k,\qquad v_k(0)=0,\\
g_k&=\sum_{\substack{j+|\alpha|+\ell=k\\j+|\alpha|>0}}
\frac1{\alpha!}
(\partial_\xi^\alpha h_{d-j})D_x^\alpha v_\ell,
\qquad D_x=\frac1i\partial_x,
\end{split}
\]

where \(0\le j\le d\), \(|\alpha|\le d-j\), and \(0\le\ell<k\). All sums are finite. Explicitly,

\[
v_k(t)=-\int_0^t e^{-(t-r)h_d}g_k(r)\,dr.
\]

This formula establishes existence by induction. Homogeneity of each \(h_{d-j}\) gives the asserted scaling: replacing \(\xi\) by \(\lambda\xi\) and time by \(\lambda^{-d}t\) gives the factor \(\lambda^{-k}\) in \(v_k\). The zero initial condition fixes the solution, so this scaling identity holds exactly.

For completeness the matrix exponentials need no commutativity assumption. Differentiating \(e^{-r h_d}\) in any coefficient variable inserts the derivative of \(h_d\) between two exponentials and integrates their time split; repeat this identity for higher derivatives. Positivity bounds each product by an exponential of \(-c r|\xi|^d\), times polynomial factors in \(|\xi|\) and the split times. In the displayed recursion, the exponential from the left factor supplies the remaining interval \(t-r\). Thus every term at \(t=1\), including its derivatives, is bounded by a polynomial in \(|\xi|\) times \(e^{-c'|\xi|^d}\), for a fixed \(c'>0\). At \(\xi=0\) these are smooth functions: the symbols of the differential operator are polynomials, the exponential is smooth, and the finite time integrals preserve smoothness. This proves the Schwartz assertion. The same bounds justify differentiation under the integrals and dominated convergence in the transverse parameter.

Finally the differential symbol product is exact, rather than only asymptotic:
\(h\# v=\sum_{j,\alpha}(\partial_\xi^\alpha h_{d-j})D_x^\alpha v/\alpha!\), with the ranges above. Each derivative beyond the polynomial degree is zero. The recursion cancels all terms of combined index \(k\le N\). The remaining indices are \(N+1\) through \(N+d\), and homogeneity gives their stated scaling. \(\square\)

**Theorem 6.12 (uniform heat and weighted expansion).** There are smooth leafwise endomorphism-valued diagonal densities \(b_k\), continuous transversely, such that for every integer \(K\ge0\) the heat kernel has the uniform diagonal expansion

\[
k_{e^{-t\Delta}}(x,x)
=\sum_{k=0}^K t^{(k-p)/d}b_k(x)
+O\bigl(t^{(K+1-p)/d}\bigr),
\qquad 0<t\le1.
\]

The error is uniform in \(x\) in the compact unit manifold, using the chosen density to express the kernel. For every locally finite transverse measure of smooth positive modulus \(\delta\),

\[
\Phi(e^{-t\Delta})
=\sum_{k=0}^K t^{(k-p)/d}\Lambda(\nu_{k-p})
+O\bigl(t^{(K+1-p)/d}\bigr),
\]

where \(\nu_{k-p}=s^*(\operatorname{tr}(b_k)\alpha)\), interpreted linearly for signed densities. Thus the expansion has all powers \(t^{j/(2m)}\) with \(j\ge-p\); coefficients that vanish are included.

**Proof.** Choose finitely many smaller coordinate boxes, a partition of unity \(\varphi_i\) subordinate to them, and larger boxes with cutoffs \(\psi_i=1\) on a neighbourhood of \(\operatorname{supp}\varphi_i\). Use Lemma 6.11 on the larger boxes, multiply the input by \(\varphi_i\) and the output by \(\psi_i\), lift the kernels, and sum. Denote the resulting compactly supported smoothing groupoid operator by \(R_N(t)\). For fixed \(t>0\), the Schwartz profiles make its kernel smooth with the required transverse continuity.

We first record bounds that justify the approximation on entire covers. A profile term of index \(k\) has, after frequency scaling, weighted symbol bound

\[
\sup_{x,\xi,u}\langle\xi\rangle^{2s}
\|\partial_x^\beta v_k(t,x,\xi,u)\|
\le C_{k,s,\beta}t^{(k-2s)/d}
\quad(s\ge0, 0<t\le1).
\]

Fourier transformation in the compact output coordinate and the Schur argument of Lemma 6.1 therefore bound this operator \(H^{-s}\to H^s\) by the same power, up to a fixed constant. Lifted sheet sums, cutoffs and Theorem 6.8 give the same bound for \(W^{-s}\to W^s\) on all covers.

Commutators with \(\psi_i\) contribute only off-diagonal kernels: their output is separated from the support of \(\varphi_i\) by a fixed coordinate distance. The inverse Fourier transform of a profile has the form
\(t^{(k-p)/d}\check v_k(1,x,(x-y)/t^{1/d},u)\), with the corresponding formula for derivatives, where \(\check v_k\) is the inverse Fourier transform of the profile. Schwartz decay and that fixed separation bound every such kernel derivative by \(C_L t^L\), for any prescribed \(L\). Their compact chart supports and Fourier-Schur estimates give the same rapid bound in every required Sobolev operator norm. Together with the residual indices in Lemma 6.11 this proves

\[
\|F_N(t)\|_{W^{-s},W^s}
\le C_{N,s}t^{-1+(N+1-2s)/d},
\qquad F_N=(\partial_t+\Delta)R_N.
\]

The constants are uniform in the unit and transverse parameters. No compactness of an individual cover is used.

Also \(R_N(t)\to1\) strongly on \(L^2\) as \(t\downarrow0\). For the principal term, \(e^{-t h_d}\to I\) on compactly supported smooth inputs by Fourier dominated convergence. Its order-zero symbol bounds give a uniform \(L^2\) bound. Each higher term has operator norm \(O(t^{k/d})\) and tends to zero. Finally \(\sum_i\psi_i\varphi_i=1\), so the local principal limits reconstruct the identity; density gives strong convergence on all of \(L^2\).

Differentiate \(e^{-(t-r)\Delta}R_N(r)v\) for a compact smooth input and integrate from \(\varepsilon\) to \(t\). These vectors are in the differential domain because the compact reduced support gives compact smooth output. Letting \(\varepsilon\downarrow0\), the strong initial limit and the integrable residual bound at \(s=0\) give the exact Duhamel identity

\[
R_N(t)-e^{-t\Delta}
=\int_0^t e^{-(t-r)\Delta}F_N(r)\,dr.
\]

Spectral calculus makes the heat operator contractive on \(W^s\). If \(N+1>2s\), the residual bound is integrable even between \(W^{-s}\) and \(W^s\). The same identity and density consequently give

\[
\|R_N(t)-e^{-t\Delta}\|_{W^{-s},W^s}
\le C'_{N,s}t^{(N+1-2s)/d}.
\]

Fix \(s>p/2\). The point-evaluation bound used in Corollary 6.10 turns this operator estimate into the same uniform diagonal-kernel bound, since input point masses have uniformly bounded \(W^{-s}\) norm and output evaluation has uniformly bounded norm on \(W^s\). Theorem 6.9 also turns it into the same bound for the difference of the weights. Both uses apply to a signed error because that theorem proves membership in the linear weight domain.

In coordinates the diagonal of the local approximation is exactly

\[
(2\pi)^{-p}\varphi_i(x)
\sum_{k=0}^N t^{(k-p)/d}
\int_{\mathbb R^p}v_{i,k}(1,x,\eta,u)\,d\eta,
\]

with the coordinate density and bundle-frame conversions understood. Here \(\psi_i=1\) on the input support. All profile integrals converge with their leafwise derivatives and depend continuously on \(u\). Sum them to define \(b_k\). To obtain the assertion through \(K\), choose \(N\ge K\) so large that \(N\ge K+2s-p\). The operator error has order at least \(t^{(K+1-p)/d}\); the finitely many approximation terms with \(k>K\) have this order or higher. This proves the uniform diagonal expansion. Its coefficients are independent of the atlas, cutoffs and extensions, since asymptotic coefficients with successively increasing powers are unique for the actual diagonal heat kernel. This also verifies their intrinsic density transformation and their Hermitian character.

For the weight, each \(R_N(t)\) is a compact smooth arrow kernel and
\(\Phi(R_N(t))=\int_V\operatorname{tr}k_{R_N(t)}(x,x)\,d\mu(x)\).
The factorization and polarization proof of Theorem 7.10 of Transverse measures of foliations applies in finite bundle frames component by component: the Fourier factorization puts both factors in the square-integrable weight ideal; polarized Corollary 9.4 and the inversion identity convert their weighted product integral to its unit diagonal. A finite chart partition proves the formula for the entire bundle kernel. Thus it applies to these approximants without presuming a diagonal formula for the heat kernel without compact arrow support.

Integrating their explicit diagonals gives the stated coefficients, because \(\mu=\Lambda_{s^*\alpha}\). Each positive and negative part is integrable: \(b_k\) is bounded on compact \(V\), \(\alpha\) is smooth positive, and \(\Lambda\) is locally finite. The weight estimate for \(R_N-e^{-t\Delta}\) completes the expansion with the claimed remainder. This step remains valid for \(\delta\ne1\); only the kernel-squared formula, inversion, positivity and weight Cauchy–Schwarz have been used. \(\square\)

**Corollary 6.13 (the measured constant term).** If \(\delta=1\), the measured kernel-dimension index satisfies

\[
\operatorname{Ind}_\Lambda(D)
=\Lambda\bigl(\nu_0(D^*D)-\nu_0(DD^*)\bigr).
\]

**Proof.** Corollary 6.10 gives finite heat traces for both operators. Theorem 2.1 makes their difference equal to the difference of their finite kernel dimensions. Apply Theorem 6.12 through the constant term, which has index \(k=p\) in its nonnegative-index notation. The next term has positive exponent, so Corollary 2.2 cancels all negative powers and identifies the constant term. This proves the formula without identifying that local density with a characteristic class. \(\square\)

The leading coefficient is already explicit:
\(b_0(x)=(2\pi)^{-p}\int e^{-h_d(x,\eta)}\,d\eta\)
in the coordinate half-density frame. For a scalar Laplacian in orthonormal coordinates, \(h_2=|\eta|^2\), and it is \((4\pi)^{-p/2}\). The coefficient producing the index is a much more delicate cancellation between the two operators; its geometric identification remains to prove.


The analytic assertions needed for the general theorem are the following:

1. A parameter-continuous longitudinal pseudodifferential calculus with uniform support and uniform order estimates on the holonomy covers. Lemmas 6.1–6.2 establish this for the Hausdorff compact-support calculus above; Proposition 6.21 proves the non-Hausdorff extension.
2. Elliptic parametrices, all-real-order Sobolev realizations, and equality of minimal and maximal differential-operator domains. Theorems 6.3, 6.5 and 6.8 establish these assertions on covers. The continuous Sobolev module structure remains to prove.
3. Heat kernels with uniform local expansions and trace-integrable remainders for every locally finite transverse measure. Corollary 6.10 and Theorem 6.12 establish these assertions, including nontrivial smooth modulus; Proposition 6.21 extends them to the non-Hausdorff calculus. For an operator of order \(m\), the powers in the individual expansion are \(t^{j/(2m)}\), beginning with \(j=-p\). Corollary 6.13 identifies the constant difference with the measured index when the measure is invariant.
4. Identification of the constant supertrace density with the characteristic form of the symbol. Theorem 6.18 and Lemma 6.19 prove that for de Rham operators it is the Euler form. Theorem 6.26 proves the spin-c Dirac expression in \(4\), with its curvature sign fixed explicitly. The general symbol formula and its Thom reduction remain to prove.

The heat construction and Corollary 6.13 now identify the measured index with its constant local density. The de Rham calculation below identifies that density as the Euler form. For a general symbol the corresponding characteristic calculation remains. The current is closed by the first lesson, so changing characteristic representatives by exact forms does not change the answer. The general symbol calculation and Sobolev module construction remain necessary.

### The ideal of forms vanishing along leaves

There is a geometric simplification of the Todd class that can be proved independently of the remaining index calculation. Assume here that the foliation is smooth transversely, so its ordinary de Rham classes on \(V\) are defined. Let \(\mathcal J\) be the ideal of differential forms whose restriction to \(F\) is zero, and let \(J\subset H^*(V;\mathbb R)\) consist of classes represented by closed forms in \(\mathcal J\). Involutivity of \(F\) makes \(d\mathcal J\subset\mathcal J\): in the formula for \(d\omega\) on leafwise vectors, both the coefficient derivatives and the bracket terms restrict to zero. Wedge multiplication likewise preserves the vanishing restriction. Thus \(J\) is an ideal.

**Proposition 6.14 (annihilation and the normal Todd factor).** For every \(\omega\in J\), its cap product with the Ruelle–Sullivan class is zero. Moreover

\[
\operatorname{Td}(TV\otimes\mathbb C)
-\operatorname{Td}(F\otimes\mathbb C)\in J.
\]

**Proof.** Choose a closed representative \(\omega_0\) restricting to zero on \(F\). Multiplication of the closed foliation current by this form represents the cap product: it evaluates a complementary test form \(\eta\) as \(C_\Lambda(\omega_0\wedge\eta)\). That expression is zero for every \(\eta\), since the entire wedge restricts to zero on each oriented plaque. The product current is therefore identically zero, proving the full cap-product assertion, including degrees below \(p\).

The normal bundle \(\tau=TV/F\) has the Bott connection along leaves:

\[
\nabla_X^{\rm Bott}[Y]=[X,Y]\bmod F.
\]

It is well defined because changing \(Y\) by a leafwise vector changes \([X,Y]\) by a leafwise vector. The bracket product rule makes it a partial connection. Jacobi's identity gives zero curvature on two leafwise vectors. Choose a splitting of \(TV\) and an arbitrary ordinary connection \(\nabla^0\) on \(\tau\). Add to it the difference between the Bott and \(\nabla^0\) connections on the leafwise projection of a tangent vector. This is an ordinary connection \(\nabla\) whose leafwise part is Bott, so its curvature \(R\) restricts to zero on \(F\times F\).

The Todd form of its complexification is
\(\det f(R/(2\pi i))\), where \(f(z)=z/(1-e^{-z})=1+z/2+\cdots\), truncated at the dimension of \(V\). Its constant term is one, and all its positive-degree terms restrict to zero on \(F\). These are closed forms: the Bianchi identity \(\nabla R=0\) gives \(d\operatorname{tr}(R^j)=0\), and invariant characteristic polynomials are polynomials in these traces. They represent the characteristic classes independently of the chosen connection. Indeed, along \(\nabla_t=\nabla_0+tB\), differentiation of \(\operatorname{tr}(R_t^j)\) gives
\(j\,d\operatorname{tr}(B R_t^{j-1})\); integration from zero to one proves independence, and the product rule gives the same conclusion for each characteristic polynomial. Thus \(\operatorname{Td}(\tau\otimes\mathbb C)-1\in J\).

A splitting identifies \(TV\) with \(F\oplus\tau\). Use a direct-sum connection, whose curvature is block diagonal. The determinant defining the Todd form factors, giving
\(\operatorname{Td}(TV\otimes\mathbb C)=\operatorname{Td}(F\otimes\mathbb C)\operatorname{Td}(\tau\otimes\mathbb C)\).
Subtract the first factor and use the ideal property of \(J\). This proves the assertion. It concerns leafwise restriction, without forcing the normal bundle's ordinary characteristic classes to vanish on \(V\). \(\square\)

### The surface coefficient

For surface leaves the first Laplace-type coefficient is enough to compute the Euler index. We derive it with its signs and density normalization. The curvature convention is
\(R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z\), so a round sphere has positive \(\langle R(X,Y)Y,X\rangle\).

**Lemma 6.15 (the first Laplace-type coefficient).** Let \(L=\nabla^*\nabla+Q\) be a nonnegative Laplace-type operator on a Hermitian bundle, using the Riemannian leafwise density. In the diagonal expansion of its heat kernel,

\[
k_{e^{-tL}}(x,x)
=(4\pi t)^{-p/2}
\left(I+t\left(\frac{\operatorname{Scal}(x)}6 I-Q(x)\right)+O(t^2)\right).
\]

The error is uniform under the compact \(C^{\infty,0}\) standing assumptions. Scalar curvature uses the stated convention.

**Proof.** The preceding Sobolev and heat arguments apply to any nonnegative elliptic differential operator with positive principal symbol, with \(1+L\) defining the scale; they used \(D^*D\) to guarantee these properties. Here the principal symbol is \(|\xi|^2I\). Essential self-adjointness follows from Theorem 6.5, and the same integer-power, interpolation and parametrix arguments apply.

Work in a common small normal-coordinate ball about \(y\). Such a radius can be chosen uniformly: shrink the finite plaque atlas, use the uniform smooth coefficient bounds and the inverse function theorem for the geodesic equations, and keep geodesics inside the larger boxes. The corresponding construction lifts to each cover. Write \(r=\operatorname{dist}(x,y)\) and \(j(x,y)\) for the volume density in normal coordinates centered at \(y\), so \(j(y,y)=1\). Consider the local ansatz

\[
(4\pi t)^{-p/2}e^{-r^2/(4t)}
\sum_{n=0}^N t^n U_n(x,y).
\]

In polar normal coordinates the scalar radial Laplacian is
\(\partial_r^2+((p-1)/r+\partial_r\log j)\partial_r\).
Apply \(\partial_t+L_x\) to the ansatz using the connection product rule. The terms of order \(t^{-2}\) cancel, and the remaining coefficient at order \(t^{n-1}\) is

\[
\left(n+r\nabla_{\partial_r}+
\frac r2\partial_r\log j\right)U_n+L_x U_{n-1},
\]

with the last term omitted when \(n=0\). Consequently
\(U_0=j^{-1/2}\tau_{y\to x}\), where \(\tau\) is parallel transport along the radial geodesic. For \(n\ge1\), the transport equations have the explicit smooth solution along a ray

\[
U_n(x,y)=-U_0(x,y)\int_0^1 \rho^{n-1}
U_0(\rho x,y)^{-1}(L U_{n-1})(\rho x,y)\,d\rho,
\]

where \(x\) denotes its normal-coordinate vector and the bundle compositions use radial transport. This integral proves smoothness at the origin and all uniform derivative bounds by induction. On the diagonal it gives
\(U_1(y,y)=-(L_x U_0)(y,y)\).

We justify that these transport coefficients belong to the actual heat kernel. Cut off the local ansatz inside the common normal neighbourhood and patch in the input variable with a finite partition of unity. Its initial limit is the identity, by the Gaussian approximate-identity calculation and \(U_0(y,y)=I\). The transport equations leave a residual equal, near the diagonal, to the Gaussian times \(t^N L U_N\). Derivatives of total order \(a\) bound its kernel by
\(C_a t^{N-p/2-a/2}e^{-r^2/(8t)}\); polynomial factors from differentiating the Gaussian have been absorbed by halving its decay exponent. Cutoff derivatives are supported at a fixed positive distance from the diagonal and have arbitrarily rapid small-time decay.

Integrating these bounds in either kernel variable gives \(C_a t^{N-a/2}\), because the Gaussian volume integral is \(O(t^{p/2})\). For an even integer \(s>p/2\), conjugating by the coordinate differential Sobolev weights of order \(s\) on both sides uses derivatives of total order at most \(2s\). Integration by parts in the input variable and the Schur estimate therefore bound the residual \(W^{-s}\to W^s\) by \(C t^{N-s}\). Localized charts and Theorem 6.8 compare these norms uniformly on the covers. Choose \(N\) large. The same Duhamel argument as in Theorem 6.12 bounds the approximation error by \(C t^{N+1-s}\) in that operator norm and hence on the diagonal. Choosing \(N+1-s\ge2-p/2\), and discarding the finite terms with \(n\ge2\), proves the asserted diagonal error. Thus \(U_1(y,y)\) is the actual first coefficient.

It remains to compute \(L U_0\) at the origin. The normal-coordinate density has expansion

\[
j(x,y)=1-\frac16\operatorname{Ric}_{ij}(y)x^ix^j+O(|x|^3).
\]

One derivation fixes a unit radial vector \(v\) and varies the geodesic direction. The variation fields obey \(J''+R(J,v)v=0\), by commuting the two covariant derivatives of the geodesic variation. Initial data \(J(0)=0\), \(J'(0)=e_i\) give
\(J(r)=r e_i-r^3R(e_i,v)v/6+O(r^4)\).
Taking the determinant of the differential of the exponential map gives
\(j(rv,y)=1-r^2\operatorname{Ric}(v,v)/6+O(r^3)\), which is exactly the displayed quadratic term for every direction.

Use the frame obtained by radial parallel transport from \(y\). Its connection matrices satisfy \(x^iA_i(x)=0\). The constant and quadratic terms of this identity imply \(A_i(0)=0\) and \(\sum_i\partial_i A_i(0)=0\). In this frame \(\tau_{y\to x}=I\), and
\(j^{-1/2}=1+\operatorname{Ric}_{ij}x^ix^j/12+O(|x|^3)\).
At the origin the positive connection Laplacian therefore gives
\(\nabla^*\nabla U_0=-\operatorname{Scal} I/6\): Christoffel symbols vanish there, and the connection-divergence term just computed is zero. The potential contributes \(Q\). Hence
\(U_1(y,y)=\operatorname{Scal} I/6-Q\), proving the formula. \(\square\)

**Corollary 6.16 (Euler and curvature for surface leaves).** For compact oriented surface foliations in the Hausdorff standing assumptions, with locally finite invariant transverse measure,

\[
\beta_0-\beta_1+\beta_2
=\frac1{2\pi}\int_V K\,d\mu
=\langle e(F),[C_\Lambda]\rangle.
\]

If compact leaves with finite holonomy are negligible, this number is nonpositive, and equals \(-\beta_1\).

**Proof.** In degree zero the Hodge Laplacian is the scalar positive Laplacian, so \(Q_0=0\). In degree two the Hodge star intertwines it with the degree-zero operator; the volume form is parallel, so \(Q_2=0\). In degree one the Weitzenböck expression is
\(\Delta_1=\nabla^*\nabla+\operatorname{Ric}\).
To check the sign, use \((d\omega)_{ji}=\nabla_j\omega_i-\nabla_i\omega_j\) and \(d^*\omega=-\nabla^j\omega_j\). Their sum gives the rough positive Laplacian plus
\(\nabla^j\nabla_i\omega_j-\nabla_i\nabla^j\omega_j\), which is \(\operatorname{Ric}_i{}^k\omega_k\) with our curvature convention.

Lemma 6.15 gives zero for the leading supertrace, since the ranks in degrees zero, one and two are \(1,2,1\). The common scalar-curvature part of the first coefficient cancels for the same reason. The remaining supertrace is

\[
(4\pi)^{-1}
\bigl(-\operatorname{tr}Q_0+
\operatorname{tr}Q_1-\operatorname{tr}Q_2\bigr)
=\frac{\operatorname{Scal}}{4\pi}
=\frac K{2\pi}.
\]

Apply Corollary 6.13 to \(d+d^*\) from even to odd forms. Its kernel dimensions are \(\beta_0+\beta_2\) and \(\beta_1\), and are finite by Corollary 6.10. This proves the first equality.

For the second, extend the leafwise Levi–Civita connection on \(F\) to a metric connection on \(F\) along all of \(TV\), using a splitting and the difference from any metric connection. The Euler form of this oriented rank-two bundle is its \(SO(2)\) curvature divided by \(2\pi\). Its leafwise restriction is \(K\alpha/(2\pi)\), with the sign fixed by positive curvature on an oriented round sphere. The foliation current integrates precisely this restriction. The Euler form is closed and its class is independent of the metric connection by the transgression argument, so this is the pairing with \(e(F)\). Finally Lemma 5.1 and Hodge star give \(\beta_0=\beta_2=0\) under the stated negligibility condition, leaving \(-\beta_1\le0\). \(\square\)

This proves the surface instance of (3). The following filtration argument proves its all-dimensional Euler version; the general symbol characteristic calculation remains additional work.


### The Euler coefficient in every dimension

The surface calculation extends through an algebraic cancellation on exterior forms. The heat transport construction above is used again; its filtration isolates the coefficient that survives supertrace.

**Lemma 6.17 (the two Clifford actions).** On the exterior algebra of an oriented Euclidean \(p\)-space, let \(\epsilon_i\) be exterior multiplication by \(e^i\), let \(\iota_i\) be contraction by \(e_i\), and put

\[
c_i=\epsilon_i-\iota_i,\qquad
\widehat c_i=\epsilon_i+\iota_i.
\]

They satisfy

\[
c_i c_j+c_j c_i=-2\delta_{ij},\qquad
\widehat c_i\widehat c_j+\widehat c_j\widehat c_i=2\delta_{ij},\qquad
c_i\widehat c_j+\widehat c_j c_i=0.
\]

The words \(c_I\widehat c_J\), with increasing index sets \(I,J\), form a basis of the full endomorphism algebra. Give such a word degree \(|I|+|J|\); the filtration by at most that degree is multiplicative. Its associated graded algebra is the exterior algebra on symbols \(\xi_1,\ldots,\xi_p,\eta_1,\ldots,\eta_p\). Supertrace vanishes on every basis word except the word containing all \(2p\) generators, and

\[
\operatorname{Str}(c_1\cdots c_p\widehat c_1\cdots\widehat c_p)
=(-1)^{p(p+1)/2}2^p.
\]

**Proof.** The exterior multiplication and contraction relations prove the displayed identities. Reordering any word with them leaves a linear combination of the stated increasing words, with contractions lowering degree by two. These words span the full endomorphism algebra: \(\epsilon_i,\iota_i\) are their linear combinations, and
\(\prod_i(1-\epsilon_i\iota_i)\) is the projection onto the scalar form. Composing this projection with exterior products and contractions produces all matrix units between the standard exterior basis vectors, with nonzero signs. There are \(2^{2p}\) stated words, equal to the dimension of the endomorphism algebra, so they are a basis. Replacing their contraction relations by zero gives the associated graded exterior algebra.

An odd word has zero supertrace because it exchanges the even and odd summands. If an even word omits a generator, conjugation by that invertible odd generator leaves the word unchanged: it anticommutes with each of the even number of generators present. But odd conjugation changes the sign of supertrace, so its supertrace is zero. For the full word, move each \(\widehat c_i\) next to \(c_i\); this gives the sign \((-1)^{p(p-1)/2}\). Now
\(c_i\widehat c_i=2\epsilon_i\iota_i-1\).
On a basis form with index set \(I\), the product of these \(p\) even operators has eigenvalue \((-1)^{p-|I|}\). Multiplication by the supertrace sign \((-1)^{|I|}\) and summation over all \(2^p\) forms gives \((-1)^p2^p\). Combining the signs proves the formula. \(\square\)

Let \(R_{ijab}=\langle R(e_i,e_j)e_b,e_a\rangle\), with the curvature convention of Lemma 6.15, and let

\[
\Omega_{ab}=\frac12\sum_{i,j}R_{ijab}e^i\wedge e^j
\]

be the real skew curvature matrix. For an even rank \(p=2\ell\), our Pfaffian convention is

\[
\operatorname{Pf}(\Omega)
=[\eta_1\cdots\eta_p]\,
\exp\left(\frac12\sum_{a,b}\Omega_{ab}\eta_a\eta_b\right).
\]

The auxiliary \(\eta\)'s anticommute; here they commute with the even-degree curvature forms. This convention gives \(\operatorname{Pf}(\Omega)=K\alpha\) for an oriented surface of Gaussian curvature \(K\).

**Theorem 6.18 (local Euler supertrace).** For the Hodge Laplacian on all exterior forms and \(p=2\ell\),

\[
\operatorname{Str}k_{e^{-t\Delta}}(x,x)\,\alpha(x)
=\operatorname{Pf}\left(\frac{\Omega(x)}{2\pi}\right)+O(t)\alpha(x).
\]

All negative powers in the local supertrace expansion vanish. The remainder is uniform under the compact Hausdorff standing assumptions, including coefficients smooth along leaves and continuous transversely. In odd dimension the supertrace is identically zero.

**Proof.** The de Rham operator is \(d+d^*=\sum_i c_i\nabla_{e_i}\). At a point choose an orthonormal frame with vanishing connection coefficients. Squaring this expression, pairing the symmetric derivatives with the Clifford relations and the antisymmetric derivatives with the curvature commutator, gives

\[
\Delta=\nabla^*\nabla+Q,\qquad
Q=\frac12\sum_{i,j}c_i c_j R^\Lambda_{ij}.
\]

This identity is tensorial, hence holds everywhere. Curvature on the exterior bundle is

\[
R^\Lambda_{ij}=\sum_{a,b}R_{ijab}\epsilon_a\iota_b
=\frac14\sum_{a,b}R_{ijab}
(\widehat c_a\widehat c_b-c_a c_b).
\]

The first formula follows by applying the curvature to covectors and then extending by the derivation rule to their exterior products. The second follows from the relations in Lemma 6.17 and skew symmetry in \(a,b\). Thus \(Q\) has Clifford degree at most four. Its degree-four symbol is

\[
q=\frac18\sum_{i,j,a,b}R_{ijab}\xi_i\xi_j\eta_a\eta_b
=\frac14\sum_{a,b}\Omega_{ab}(\xi)\eta_a\eta_b.
\]

The other possible term has four \(\xi\)'s. Its coefficient is the full alternation of the curvature tensor, which is zero by the first Bianchi identity. This is exactly where the Levi–Civita curvature symmetry is used.

Return to the transport coefficients \(U_n(x,y)\) of Lemma 6.15, in the exterior frame obtained by radial parallel transport from \(y\). The generators of Lemma 6.17 are constant matrices in this frame. The connection matrices have Clifford degree at most two, since they are induced by skew matrices on tangent vectors. The potential has degree at most four. Moreover \(U_0=j^{-1/2}I\) has degree zero. The transport integral therefore proves inductively that \(U_n\), and all its coefficient derivatives, have degree at most \(4n\): the connection Laplacian increases degree by at most four, the potential by at most four, and the scalar transport factors preserve degree.

At the diagonal the connection matrices themselves vanish. In \(L U_{n-1}\), ordinary second derivatives preserve degree, first connection terms and derivatives of a connection matrix increase it by at most two, and the product of two connection matrices is zero there. Consequently the degree-\(4n\) component at the diagonal comes solely from the degree-four potential acting on the top component of \(U_{n-1}\). The transport equation at the origin is \(nU_n(y,y)=-L U_{n-1}(y,y)\), so

\[
\sigma_{4n}(U_n(y,y))=\frac{(-q(y))^n}{n!}.
\]

Here the symbol is zero if that degree exceeds the exterior-algebra dimension. In particular for \(n<\ell\), its entire degree bound is below \(2p\), so Lemma 6.17 makes \(\operatorname{Str}U_n=0\) on the diagonal. For \(n=\ell\), only the displayed top symbol contributes. The full-word supertrace sign is \((-1)^\ell2^p\), and the minus sign in \((-q)^\ell\) cancels it. It follows that

\[
\begin{split}
\operatorname{Str}U_\ell(y,y)
&=2^p[\xi_1\cdots\xi_p\eta_1\cdots\eta_p]\frac{q^\ell}{\ell!}\\
&=2^{p-\ell}[\xi_1\cdots\xi_p]\operatorname{Pf}(\Omega(\xi))
=2^\ell\frac{\operatorname{Pf}(\Omega)}{\alpha}.
\end{split}
\]

The middle equality follows from the defining Pfaffian exponential: \(q\) is one half of its quadratic generator in the \(\eta\)'s. The Gaussian prefactor contributes \((4\pi)^{-\ell}\), and hence the constant density is \((2\pi)^{-\ell}\operatorname{Pf}(\Omega)\). The transport construction, with arbitrarily high truncation and the uniform Duhamel estimate already proved, leaves \(O(t)\) after this term. Thus the algebraic computation is a computation of the actual heat coefficient.

For odd \(p\), the Hodge star intertwines the Laplacians in degrees \(j\) and \(p-j\), whose parity signs are opposite. Their kernel traces cancel pointwise for every \(t>0\). This proves the odd assertion. \(\square\)

![Clifford degree below twice the leaf dimension has zero supertrace. In dimension four, U0 and U1 vanish under supertrace and U2 gives four times the product of the two surface curvatures. Gaussian normalization yields the Euler density.](../figures/euler-clifford-cancellation.png)

*Figure 2. The algebraic mechanism of Theorem 6.18. The degree is the number of Clifford generators in Lemma 6.17, not differential-form degree. The dimension-four table uses the product of two surfaces with curvatures \(K_1,K_2\), so \(\operatorname{Pf}(\Omega)=K_1K_2\alpha\). The unit-round product in Exercise 12 checks both the local density and its integral. Theorem 6.18 supplies the uniform \(O(t)\) remainder; Lemma 6.19 identifies the surviving form as the Euler class.*

We next verify that the Pfaffian used here represents the usual Euler class, with the orientation and normalization already fixed. This makes the geometric pairing an identified class, rather than a name assigned to the heat coefficient.

**Lemma 6.19 (the Pfaffian and the Euler class).** For an oriented real rank-\(2\ell\) metric bundle \(E\) with metric connection and curvature matrix \(\Omega\),
\(\operatorname{Pf}(\Omega/(2\pi))\) represents its real Euler class. For odd rank its real Euler class is zero.

**Proof.** Put \(p=2\ell\) and use fibre coordinates \(x_i\) in an oriented orthonormal frame. Write \(Dx_i\) for their covariant differentials on the total space. Introduce auxiliary odd variables \(\eta_i\) that anticommute both with one another and with odd ordinary forms. Let \(\mathcal B\) extract the coefficient with the ordered variables \(\eta_1\cdots\eta_p\) on the right. Define the rapidly decreasing \(p\)-form

\[
U=(-1)^\ell(2\pi)^{-\ell}e^{-|x|^2/2}
\mathcal B\exp\left(
\sum_i Dx_i\eta_i-
\frac12\sum_{i,j}\Omega_{ij}\eta_i\eta_j
\right).
\]

The expression is independent of the chosen oriented orthonormal frame: all its contractions are invariant, and the coefficient extraction changes by the determinant, which is one. Every term has total ordinary form degree \(p\).

We check closedness explicitly. Take the covariant exterior derivative, which agrees with ordinary differentiation after the invariant coefficient extraction. Curvature and Bianchi give \(D(Dx)=\Omega x\), \(D\Omega=0\). With \(S=\sum Dx_i\eta_i-\frac12\sum\Omega_{ij}\eta_i\eta_j\), the even total degree of its summands permits differentiation of its exponential. The ordinary differential of the Gaussian and this exponential is

\[
D(e^{-|x|^2/2}e^S)
=e^{-|x|^2/2}
\left(-\sum_i x_i Dx_i+\sum_i(\Omega x)_i\eta_i\right)e^S.
\]

The left odd derivative in \(\eta_i\) gives
\(\partial_{\eta_i}S=-Dx_i-\sum_j\Omega_{ij}\eta_j\): the first minus sign comes from passing the ordinary odd form \(Dx_i\). Skew symmetry of \(\Omega\) shows that the parenthesis in the previous display is \(\sum_i x_i\partial_{\eta_i}S\). Its coefficient extraction is zero, because an odd-variable derivative has no top auxiliary coefficient. Thus \(dU=0\).

On a fibre, \(Dx_i=dx_i\) and the curvature term is absent. The coefficient of all auxiliary variables in \(\exp(\sum dx_i\eta_i)\) is \((-1)^\ell dx_1\wedge\cdots\wedge dx_p\). The prefactor cancels this sign, and the Gaussian integral gives \(\int_{E_y}U=1\). Rapid decay can be converted to compact vertical support: pull back by the radial diffeomorphism from the open unit ball to the full fibre, \(x=y/\sqrt{1-|y|^2}\), and extend by zero outside the ball. The Gaussian beats every derivative of this diffeomorphism at the boundary, so the extension is smooth and closed, has fibre integral one, and has the same zero-section pullback.

This form represents the oriented Thom class. To see the uniqueness implicit in that statement, on one real fibre the compactly supported de Rham complex contracts to its integral in top degree. In one dimension, for a compactly supported one-form \(f(x)dx\), choose a smooth compact bump \(\rho\) of integral one and set
\(H(fdx)(x)=\int_{-\infty}^x(f(t)-\rho(t)\int f)\,dt\).
Then \(dH+Hd\) is the identity minus the projection onto \(\rho dx\) times the integral. Tensoring these contractions with the usual graded signs gives the corresponding result in \(\mathbb R^p\). Local bundle trivializations and a partition-of-unity Mayer–Vietoris argument consequently identify compact-vertical cohomology with base cohomology shifted by \(p\), through fibre integration. In degree \(p\), a closed form of fibre integral one is therefore the Thom class.

On the zero section, \(Dx=0\), and the auxiliary coefficient is \(\operatorname{Pf}(-\Omega)=(-1)^\ell\operatorname{Pf}(\Omega)\). The remaining sign cancels the prefactor sign. Thus its pullback is \(\operatorname{Pf}(\Omega/(2\pi))\). The Euler class is the zero-section pullback of the oriented Thom class, proving the even-rank assertion. In odd rank, the bundle automorphism \(-I\) reverses the fibre orientation and fixes the zero section. Naturality of the Thom class and its orientation sign give \(e(E)=-e(E)\); over the reals this forces \(e(E)=0\). \(\square\)

**Corollary 6.20 (the measured Euler theorem).** For compact smooth oriented foliations in the Hausdorff standing assumptions, with locally finite invariant transverse measure,

\[
\sum_{j=0}^p(-1)^j\beta_j
=\langle e(F),[C_\Lambda]\rangle,
\qquad \beta_j<\infty.
\]

The dimensions are independent of the metric and retain the holonomy-cover representation.

**Proof.** Finiteness and metric independence were proved in Corollaries 6.6 and 6.10. Apply the heat trace identity to \(d+d^*\) from even to odd forms. The local supertrace of Theorem 6.18 has a uniform remainder on compact \(V\), and \(\mu\) is finite, so its integral tends to the integral of the Euler density. The constant heat difference is the alternating measured kernel dimension, proving the equality for even \(p\).

Extend the leafwise Levi–Civita connection on \(F\) to a metric connection along \(TV\), using the splitting argument of Corollary 6.16. Its global Euler form restricts to the leafwise Pfaffian, and Lemma 6.19 identifies its class as \(e(F)\). The foliation current integrates this restriction, so the density integral is the stated pairing. Changing the extension or the metric changes the Euler form by an exact form; the closed current gives the same pairing.

For odd \(p\), Hodge star pairs the finite measured dimensions with opposite parity signs, and Lemma 6.19 makes the right side zero as well. For \(p=0\), the leaves are points, \(e(F)=1\), and both sides are the total transverse mass. This covers every dimension. \(\square\)


### Allowing a non-Hausdorff arrow space

The holonomy covers remain Hausdorff even when the full arrow space does not. The global kernels must then retain their finite chart presentations. Use the smooth chart-span algebra of The C*-algebra of a foliation, Section 6, and finite-rank bundle versions of it. A smooth kernel has a finite sum of components, each compactly supported inside one Hausdorff arrow chart and extended by zero. Equal presentations are identified by their resulting fibre operators. The pseudodifferential class has the same finite smooth components, together with the local near-unit pseudodifferential components. It is a class of equivariant families on the covers; global continuity of an extended chart component is not required.

**Proposition 6.21 (extension of the longitudinal arguments).** The calculus, domain, Sobolev, weighted heat and measured Euler assertions of Section 6 remain valid for the possibly non-Hausdorff holonomy groupoid, using these finite chart presentations. Compact support in those assertions means compact support of each component before chart extension. The measure hypotheses and the holonomy-cover fibres are unchanged.

**Proof.** We verify the points where the previous arguments used global Hausdorffness.

First there is a Hausdorff open neighbourhood of the entire unit manifold suitable for the singular kernels. Choose a common small leafwise geodesic radius using the finite protected plaque atlas. The map sending \((x,v)\), \(v\in F_x\) of that radius, to the arrow of its short geodesic is a local diffeomorphism into \(G\). It is injective: two such arrows have the same source and endpoint; both geodesics remain in a protected plaque, where the common small exponential map is injective. Thus it is a homeomorphism onto an open subset, with Hausdorff domain a disk neighbourhood in \(F\). Shrink the radius once more so that products of the short arrows used in two singular kernel components stay in the larger such neighbourhood. Their concatenated paths lie in protected plaques and are homotopic there to the unique short path. The near-diagonal symbol calculations, coordinate changes, cutoffs and asymptotic summation therefore take place in ordinary Hausdorff charts exactly as before.

The remaining components are smooth chart kernels. Proposition 6.1 of the algebra lesson proves their closure under convolution and adjoint by a finite partition of the intermediate endpoint variables. The same local integrals handle a smooth component composed with a pseudodifferential component: apply its compactly supported plaque distribution to the smooth kernel in the intermediate variable, and differentiate under the resulting local integrals. Symbol continuity and compact supports give uniform bounds for every leafwise derivative. These products are finite sums of smooth chart components. Hence the full composition and parametrix arguments work, with their errors in that chart-span algebra. Fixed quantization cutoffs in the parametrix construction still prevent a growing-support sum.

Here is the required support argument on each cover. A compact component support is the image of a compact subset of its Hausdorff chart domain. Its subset with prescribed range \(x\) is closed in that compact domain, since the range map has values in Hausdorff \(V\). Its image in \(G^x\) is consequently compact. For a compact set of input or output points on the cover, possible paired points are images of a compact composable set: equality of endpoints is closed in \(V\), and multiplication into the Hausdorff cover is continuous. This proves proper support on that cover, and permits all the distributional parametrix identities used for minimal and maximal domains. It uses compact parameter domains, without assuming that their images are closed in all of \(G\).

The operator estimates also hold component by component. One arrow chart matches a given row or column to a single plaque patch on a prescribed branch. Fourier-Schur, coordinate Sobolev and squared Hilbert–Schmidt estimates have the same uniform chart bounds. For finitely many components, the operator norm is bounded by the sum of their bounds, and a squared kernel norm by their number times the sum of their squares. This proves every bound used in Lemmas 6.1–6.2. Frequency truncation produces finite smooth chart sums converging in the regular norm, so negative-order C*-membership is retained. The coordinate localization and reconstruction concern only the Hausdorff covers and the compact unit manifold; their interpolation, density and domain proofs are unaffected.

For measured fields, a countable atlas gives a standard Borel arrow space. Partition it into the first chart and the portions of each later chart outside the earlier ones. Each portion is a Borel subset of a Hausdorff chart, and the countable disjoint union is standard Borel. The groupoid operations are Borel in these charts. Lifted smooth positive leafwise measure is faithful and proper: exhaust by increasing finite unions of compact chart components; their uniformly bounded row masses give the properness bound after any left translation. Unit measures and transverse local finiteness are still checked on the Hausdorff foliation boxes. Thus the stated random-operator and weight prerequisites apply, with isotropy retained.

The heat approximants use the near-unit neighbourhood above, and their separated-cutoff errors are finite smooth components. All Duhamel estimates take place on the covers, with the same uniform constants. The weighted square-kernel formula applies to their Borel reduced kernels. On the finite compact component supports the smooth cocycle and its inverse have bounded values. The Fourier factorization of a smooth component uses the pair-plaque chart of its output box and retains its original input holonomy branch, as in the transverse-measure lesson; it gives the same linear weight domain and diagonal formula. Hence the trace estimates and the entire heat expansion hold. The Clifford cancellation and Euler coefficient depend only on the local geometry on \(V\), so they hold as well. This verifies every required change in the analytic and measure arguments. \(\square\)

**Corollary 6.22 (excluding only sphere leaves).** For compact smooth oriented surface foliations with locally finite invariant transverse measure, the inequality
\(\int_V K\,d\mu\le0\)
holds if the sphere leaves are negligible. It is not necessary to exclude all compact leaves. The sphere-leaf set is Borel and saturated.

**Proof.** Let \(v(x)=\nu^x(G^x)\) be the volume of the holonomy cover. It is a Borel function, constant along each leaf by left invariance. Lemma 5.1 shows that
\(C=\{x:v(x)<\infty\}\)
is precisely the saturated set of compact leaves with finite holonomy. On \(C\), put \(q(x)=1/v(x)\). This is finite, positive, Borel and leaf-constant.

For each degree let \(b_j(x)\) be the ordinary dimension of the harmonic space on the compact cover. This is Borel: the measurable harmonic projections admit countable measurable orthonormal frames, and their ranks are limits of finite frame counts. A normalized averaging kernel gives the following precise formula for the restricted measured trace:

\[
\beta_{j,C}=\int_C q(x)b_j(x)\,d\mu(x).
\]

To verify it, on the restricted measured groupoid use \(g(\gamma)=q(r(\gamma))\). Then \(\nu(g)=1\); its inverse \(f=\widetilde g\) satisfies \(\nu*f=1\). In each cover multiplication by \(f\) is the scalar \(q(x)\). The normalized local-trace formula of [Weights on random operators and formal dimension, Proposition 9.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/noncommutative-integration/weights-on-random-operators-and-formal-dimension.html#section-9), applied to the harmonic projection, gives exactly the display. No uniform bound on \(q\) is assumed: that proposition defines an unbounded multiplier by the increasing truncations \(\min(q,n)\); monotone convergence gives the displayed integral. Square integrability, properness and finite measured trace were already proved; restriction to a saturated Borel set preserves the measured hypotheses.

On a compact oriented covering surface of genus \(g\), \(b_0=b_2=1\) and \(b_1=2g\). These are the usual de Rham dimensions for the classification of compact oriented surfaces. The covering Euler number is \(2-2g\). A compact cover of genus zero can cover an oriented leaf only if that leaf is itself a sphere: a finite covering of degree \(h\) multiplies Euler number by \(h\), by lifting a finite cell decomposition, and the only positive Euler number of an oriented closed surface is two. Thus \(2=h\chi(L)\) forces \(h=1\) and genus zero for \(L\).

It follows that the sphere-leaf set is exactly \(\{x\in C:b_1(x)=0\}\), proving its Borel character. Off its negligible portion in \(C\), every cover has genus at least one, so
\(q(x)(b_0-b_1+b_2)=q(x)(2-2g)\le0\).
The three integrals defining the \(\beta_{j,C}\) are finite, so their difference is well defined. On \(V\setminus C\), the cover is noncompact and the degree-zero and degree-two harmonic spaces vanish; its measured Euler number is \(-\beta_{1,V\setminus C}\le0\). Add the two saturated restrictions and apply Corollary 6.20, extended by Proposition 6.21. This proves the inequality and keeps the finite-holonomy normalization throughout. \(\square\)

**Proposition 6.23 (local stability of a compact finite-holonomy leaf).** If \(L\) is a compact leaf with finite holonomy group \(H\), it has an open saturated neighbourhood whose leaves are compact. Locally this neighbourhood is
\((\widetilde L\times T)/H\),
where \(\widetilde L\to L\) is its finite holonomy cover and \(H\) acts on the small transverse neighbourhood \(T\) by its holonomy, and freely on the covering factor by deck transformations.

**Proof.** We first treat trivial holonomy. A compact leaf is embedded: its injective immersion into Hausdorff \(V\) is an embedding because its intrinsic manifold is compact. Choose a finite good cover of the leaf by smaller plaque patches inside foliation boxes, with slightly larger patches giving a buffer around their closures. Such a cover is obtained from small strongly convex balls for an auxiliary metric on compact \(L\); nonempty intersections are connected. The boxes can be narrowed about these patches so that overlaps near \(L\) are the buffered overlap components just chosen. Fix paths from one base patch to the others and relabel their transverse coordinates by transport along these paths. On an overlap, the remaining transverse transition is holonomy around a loop in \(L\), so its germ is the identity. The transition depends only on the transverse coordinate and is constant along that connected overlap patch. There are finitely many pairs of patches; shrinking a common transverse neighbourhood makes each of these finitely many germ identities an actual identity there. The relabelled transverse coordinates therefore agree on overlaps. They define a smooth submersion \(f\) to that transverse neighbourhood on an open neighbourhood of \(L\), with \(L\) its zero fibre near \(L\).

Choose a relatively compact tube \(W\) about \(L\) inside this neighbourhood, with its boundary disjoint from the zero fibre. Such a tube exists because locally that fibre is precisely the embedded leaf and finitely many smaller boxes cover it. Compactness of the boundary gives a transverse neighbourhood \(T\) disjoint from \(f(\partial W)\). Thus \(f:f^{-1}(T)\cap W\to T\) is a proper submersion near the component containing \(L\): preimages of compact subsets of \(T\) are closed in compact \(\overline W\) and avoid its boundary. A product trivialization follows directly by lifting the radial paths in a smaller transverse ball through a smooth horizontal splitting of \(df\). Properness keeps these lifted paths in compact subsets, so their differential equations exist to the required time; reversing the paths gives the inverse map. The component is therefore \(L\times T\). Each fibre is a compact full leaf: it is open in the intrinsic connected leaf, and is also closed there by compactness, hence cannot be only a proper portion of it. The neighbourhood is saturated.

For finite holonomy, take a tubular neighbourhood of the embedded \(L\), retracting onto it. The finite cover corresponding to the kernel of \(\pi_1(L)\to H\) extends to a finite normal cover of this tube by the retraction. Its lifted compact leaf is \(\widetilde L\) and has trivial holonomy. Apply the preceding argument upstairs. The finite deck group \(H\) acts on this tube, preserves the lifted foliation, and fixes its central leaf as a set. Intersect finitely many translates of the stable neighbourhood and shrink near that leaf; its compact fibres still have an open product neighbourhood there. The deck transformations induce the original finite holonomy action on the transverse germ.

This finite germ action can be realized on an invariant small transverse neighbourhood. All finitely many multiplication identities hold on a common domain \(D\) after shrinking. Choose a smaller coordinate ball \(D_0\) with every \(h(D_0)\subset D\). A sufficiently small sublevel set of \(\sum_{h\in H}|h(u)|^2\) lies in \(D_0\). If \(u\) is in this sublevel set, the multiplication identities on \(D\) permute the summands at \(h(u)\); their sum is unchanged. Since the sum includes the identity summand, its small value also puts \(h(u)\) in \(D_0\). This proves invariance. Average a transverse metric over the group and use its exponential coordinates at the fixed central point to choose an invariant ball. In the stable product neighbourhood, a deck map sends each full leaf fibre to a full leaf fibre, so the proper submersion is equivariant for this transverse action. Average its horizontal splitting over \(H\); horizontal splittings form an affine space, so the average is still a splitting. Parallel transport along the radial geodesics of the averaged transverse metric is now equivariant. It gives the product trivialization with the diagonal action stated in the proposition. The covering-factor action is free because it is the deck action of a covering. The quotient therefore embeds as a neighbourhood in the original tube. Its leaves are quotients of the compact fibres by subgroups of the finite group, so they are compact. This proves the claimed stability and local model. \(\square\)


### The spin-c Dirac coefficient

For a unitary connection written \(\nabla=d+A\), write its curvature as
\(R^\nabla=dA+A\wedge A\). We use

\[
\operatorname{ch}(E,\nabla)=\operatorname{tr}\exp\left(\frac{iR^E}{2\pi}\right),
\qquad c_1(L,\nabla)=\frac{iR^L}{2\pi}.
\]

Thus these two normalized curvatures are \(-R^\nabla/(2\pi i)\). Fixing this sign along with the chirality prevents a sign ambiguity in the local formula. For the real tangent curvature matrix \(\Omega\) of Theorem 6.18 put

\[
\widehat A(F,\nabla)
=\det{}^{1/2}\left(
\frac{\Omega/(4\pi i)}{\sinh(\Omega/(4\pi i))}
\right).
\]

The quotient is defined by its power series with constant term one, and the square root is the one with constant term one. Only finitely many terms are used in any fixed differential-form degree. This is the usual real Pontryagin-series normalization; replacing \(\Omega\) by its negative gives the same expression.

Let the oriented even-rank \(F\) have a spin-c structure. Its spinor bundle \(S=S^+\oplus S^-\) carries Clifford multiplication with \(c(v)^2=-|v|^2\). In an oriented orthonormal frame of rank \(p=2\ell\), the grading is
\(\Gamma=i^\ell c_1\cdots c_p\).
Let \(L\) be the determinant line of the spin-c structure, with unitary connection. A Hermitian twisting bundle \(E\) has a unitary connection as well. The leafwise spin-c Dirac operator is
\(D_E=\sum_i c_i\nabla^{S\otimes E}_{e_i}\).

**Lemma 6.24 (spinor supertrace and the leading local model).** Filter the complex Clifford algebra by word length. On the irreducible spinor module in dimension \(2\ell\), every Clifford basis word except the full word has zero supertrace, and

\[
\operatorname{Str}_S(c_1\cdots c_p)=(-2i)^\ell.
\]

In radial parallel frames at a point, the leading weighted Taylor model for \(D_E^2\) is

\[
H=-\sum_i\left(\partial_i+\frac14\sum_j\Omega_{ij}(\xi)x^j\right)^2
+F(\xi),
\qquad
F=R^E+\tfrac12R^L I_E.
\tag{15}
\]

Here the \(\xi_i\) are exterior symbols for the Clifford generators; all curvature forms in the display are evaluated at the centre and expressed in these symbols. Give \(x^\alpha c_I\) weight \(|I|-|\alpha|\), and a derivative weight one. The model is the part of weight two. It is a formal operator with coefficients in the finite exterior algebra, tensor the matrix algebra of \(E\).

**Proof.** The increasing Clifford words span the algebra by the anticommutation relations and are independent: its spinor representation is the full matrix algebra, of dimension \(2^p\), equal to their number. Independence can also be checked by their Hilbert–Schmidt trace pairings. An odd word has zero supertrace. For an even word missing a generator, conjugation by that odd invertible generator leaves the word unchanged and reverses supertrace, giving zero. The full product has square \((-1)^\ell\), so its supertrace is
\(\operatorname{tr}(i^\ell(c_1\cdots c_p)^2)=(-i)^\ell2^\ell\), as asserted.

We give the curvature and Taylor calculation behind (15). With the convention
\(R_{ijab}=\langle R(e_i,e_j)e_b,e_a\rangle\), the spin curvature is

\[
R^S_{ij}=-\frac14\sum_{a,b}R_{ijab}c_a c_b
+\tfrac12R^L_{ij}I_S.
\]

Indeed the commutator of the first term with \(c_k\) is \(\sum_aR_{ijak}c_a\), the required tangent-curvature action; the spin-c scalar factor is half the determinant curvature. Squaring the Dirac operator at the centre gives

\[
D_E^2=\nabla^*\nabla+\frac12\sum_{i,j}c_i c_j
\bigl(R^S_{ij}+R^E_{ij}\bigr)
=\nabla^*\nabla+\frac{\operatorname{Scal}}4I
+\frac12\sum_{i,j}c_i c_jF_{ij}.
\tag{16}
\]

For the last equality, the four-Clifford part of the spin term vanishes by Bianchi. To check its scalar part, reorder
\(-\frac18\sum R_{ijab}c_i c_jc_a c_b\).
The terms with four distinct indices cancel by full alternation. Terms reducing to a two-generator word contract to the symmetric Ricci tensor and hence cancel against that word's skew part. The scalar terms, with \((a,b)=(i,j)\) or \((j,i)\), give
\(\frac14\sum_{i,j}R_{ijij}=\operatorname{Scal}/4\).
This proves (16) with its sign, rather than presupposing a Lichnerowicz convention.

In radial gauge, a connection matrix satisfies

\[
A_i(x)=\int_0^1 t x^jR^\nabla_{ji}(tx)\,dt.
\]

To verify this identity, contract the curvature equation with \(x^j\), use \(x^jA_j=0\), and integrate the resulting derivative of \(tA_i(tx)\). The linear spin term is consequently
\(\frac18\sum_{j,a,b}R_{ijab}x^j c_a c_b\).
Pair symmetry of Levi–Civita curvature identifies its exterior symbol with
\(\frac14\sum_j\Omega_{ij}(\xi)x^j\).
It has weight one. Every higher Taylor term has smaller weight. The scalar determinant-line and twisting connection matrices have degree zero and vanish at the centre, so their weights are at most minus one. The normal-coordinate metric is \(I+O(|x|^2)\); its corrections to the second-order part have weight at most zero. Christoffel drift terms are linear in \(x\) and likewise have weight at most zero. The scalar potential in (16) has weight zero, while the top part of its other potential is the degree-two form \(F(\xi)\). Combining these terms gives exactly (15). \(\square\)

**Lemma 6.25 (the formal model heat kernel).** The value at the origin of the fundamental solution for (15) is

\[
K_H(t;0,0)
=(4\pi t)^{-\ell}
\det{}^{1/2}\left(\frac{t\Omega/2}{\sinh(t\Omega/2)}\right)
\exp(-tF).
\tag{17}
\]

This identity is in the finite exterior algebra. It requires no interpretation of a harmonic oscillator with ordinary positive or negative numerical curvature eigenvalues.

**Proof.** The entries of \(\Omega\) are scalar even forms, so they commute with each other and with \(F\). Put

\[
B_t=\frac\Omega2\coth\left(\frac{t\Omega}2\right),
\qquad
C_t=(4\pi t)^{-\ell}
\det{}^{1/2}\left(\frac{t\Omega/2}{\sinh(t\Omega/2)}\right).
\]

The apparent inverse in the first expression means the series
\(B_t=t^{-1}I+t\Omega^2/12+\cdots\); it is well defined. Skew symmetry of \(\Omega\) makes \(B_t\) symmetric and commuting with \(\Omega\). Expanding the square in (15) gives

\[
H=-\Delta-\frac12\sum_{i,j}\Omega_{ij}x^j\partial_i
+\frac1{16}x^T\Omega^2x+F.
\]

For
\(K(t;x,0)=C_t\exp(-x^TB_tx/4)\exp(-tF)\),
the angular first-order term vanishes: \(x^T\Omega B_tx=0\). Direct differentiation shows that the heat equation is equivalent to

\[
B_t'=-B_t^2+\Omega^2/4,
\qquad C_t'/C_t=-\tfrac12\operatorname{tr}B_t.
\]

The stated power series satisfy these identities, by differentiation of coth and of the determinant's formal logarithm. Their initial terms are the Euclidean Gaussian. More precisely every positive-form-degree correction has an extra positive power of \(t\), times a polynomial in \(x\) divided by the Gaussian scale, and tends distributionally to zero against test functions. The degree-zero term tends to the identity delta distribution. Uniqueness follows successively in exterior degree: the degree-zero equation is the Euclidean heat equation, and each higher-degree equation is an inhomogeneous Euclidean heat equation determined by the lower degrees, with zero initial data. Duhamel integration gives its unique solution in this Gaussian-polynomial class. The finite matrix factor \(\exp(-tF)\) solves its constant matrix equation and commutes with the scalar curvature factor. Evaluating at \(x=0\) proves (17). \(\square\)

**Theorem 6.26 (local spin-c Dirac supertrace).** With the above curvature and chirality conventions,

\[
\operatorname{Str}_{S\otimes E}k_{e^{-tD_E^2}}(x,x)\,\alpha(x)
=\left[
\widehat A(F,\nabla)\,e^{c_1(L,\nabla)/2}
\operatorname{ch}(E,\nabla)
\right]_p(x)+O(t)\alpha(x).
\tag{18}
\]

All negative powers in this local supertrace vanish. The error is uniform on the compact foliated manifold. Proposition 6.21 permits a non-Hausdorff holonomy groupoid.

**Proof.** We explain why the formal model computes the coefficient of the actual heat operator. Use the radial transport coefficients \(U_n(x,0)\) of Lemma 6.15 on \(S\otimes E\). Radial parallel transport makes \(U_0=j^{-1/2}I\), whose Taylor terms have weight at most zero, with leading weighted term \(I\). Lemma 6.24 shows that the Taylor expansion of the operator has weight at most two and that its weight-two part is \(H\).

Differentiation raises weight by one, Clifford multiplication raises it by at most its word length, and products add weights or lower them by Clifford contractions. The transport integral preserves each weight: on a Taylor monomial of degree \(a\), its radial integral divides by the positive integer \(n+a\). Induction therefore gives weight at most \(2n\) for every Taylor term of \(U_n\). At weight \(2n\), the transport equation uses only the weight-two part \(H\) and the weight-\(2n-2\) part of \(U_{n-1}\); all lower operator terms have smaller weight. Thus the leading weighted terms satisfy exactly the Euclidean transport recursion for the formal model, with initial term \(I\). That recursion uniquely determines them. Only finitely many Taylor coefficients can contribute to a prescribed Clifford degree at a fixed \(n\), so this argument concerns finite jets and uses no convergence of an infinite Taylor series.

At the diagonal, Taylor degree is zero. Hence \(U_n(0,0)\) has Clifford degree at most \(2n\). For \(n<\ell\), Lemma 6.24 gives zero supertrace. For \(n=\ell\), its only surviving term is Clifford degree \(p\); by the recursion just proved it is the exterior-degree-\(p\) part of the \(t^\ell\) coefficient in (17) after removing its Gaussian prefactor. Lemma 6.24 now gives the constant supertrace density

\[
(4\pi)^{-\ell}(-2i)^\ell
\left[
\det{}^{1/2}\left(\frac{\Omega/2}{\sinh(\Omega/2)}\right)
\operatorname{tr}_E e^{-F}
\right]_p.
\]

The scalar factor is \((-i/(2\pi))^\ell\). Every degree-\(p\) monomial contains \(\ell\) curvature two-forms, so absorb this factor by replacing each of those forms by \(-i/(2\pi)\) times itself. The determinant becomes \(\widehat A(F,\nabla)\), and the exponential becomes

\[
\operatorname{tr}_E\exp\left(\frac{iF}{2\pi}\right)
=e^{c_1(L,\nabla)/2}\operatorname{ch}(E,\nabla).
\]

This proves the constant coefficient in (18). Lemma 6.15's arbitrarily high radial truncation and uniform Duhamel comparison identify its transport expansion with the actual heat kernel, leaving the stated uniform \(O(t)\) after the constant term. The non-Hausdorff extension concerns chart supports and fibrewise estimates, while this local computation is on the compact unit manifold; Proposition 6.21 applies directly. \(\square\)

**Corollary 6.27 (the measured spin-c Dirac formula).** Under the invariant locally finite transverse measure hypotheses,

\[
\operatorname{Ind}_\Lambda(D_E^+)
=C_\Lambda\left(
\left[\widehat A(F)e^{c_1(L)/2}\operatorname{ch}(E)\right]_p
\right).
\]

The two kernel dimensions are finite. This is formula (4), with the sign convention fixed above.

**Proof.** Finiteness follows from Corollary 6.10 and Proposition 6.21. Apply the heat identity of Theorem 2.1 to the two parity summands of the Dirac operator. The trace formula integrates (18); the error tends to zero because it is uniform and the unit measure is finite. Its constant value is the measured kernel-dimension difference. Extend the leafwise metric and bundle connections to the ambient manifold using a splitting of \(TV\); the characteristic forms restrict to the computed leafwise forms. Their closedness follows from Bianchi and the trace of commutators being zero. Changing a connection gives an exact transgression: differentiate its curvature along a path of connections, use \(\dot R=\nabla\dot A\), and move \(\nabla\) through each invariant polynomial under the trace or determinant. The closed foliation current annihilates this exact difference. Thus the value is the characteristic-class pairing stated. \(\square\)

This closes the spin-c local coefficient, not the general principal-symbol formula. That latter formula additionally needs a Thom reduction with its cotangent orientation, and proof that the analytic index respects that reduction and K-theory classes. Those requirements remain.


## 7. A lattice interpolation theorem

There is a concrete analytic consequence of the index formula whose existence assertion can also be proved directly. This second route makes its density threshold and growth condition visible.

For a lattice \(\Gamma\subset\mathbb C\), let \(A_\Gamma\) be its Euclidean covolume and \(d_\Gamma=1/A_\Gamma\) its density. Write \(\operatorname{dist}(z,\Gamma)\) for Euclidean distance to the lattice, and \(dA\) for Euclidean area measure.

**Lemma 7.1 (a Gaussian-normalized lattice function).** There is an entire function \(F_\Gamma\), with simple zeros precisely at \(\Gamma\), and constants \(0<m_\Gamma\le M_\Gamma<\infty\), such that

\[
m_\Gamma\operatorname{dist}(z,\Gamma)
\le |F_\Gamma(z)|e^{-\pi d_\Gamma|z|^2/2}
\le M_\Gamma\operatorname{dist}(z,\Gamma)
\quad(z\in\mathbb C).
\tag{5}
\]

**Proof.** Choose generators \(\omega_1,\omega_2\) with
\(A_\Gamma=\operatorname{Im}(\overline{\omega_1}\omega_2)>0\).
Start with the Weierstrass product

\[
\sigma(z)=z\prod_{\omega\in\Gamma\setminus\{0\}}
\left(1-\frac z\omega\right)
\exp\left(\frac z\omega+\frac{z^2}{2\omega^2}\right).
\]

The logarithm of each factor is \(O(|z/\omega|^3)\) on a fixed compact set for sufficiently large \(|\omega|\). Since \(\sum_{\omega\ne0}|\omega|^{-3}<\infty\), the product converges normally, has simple zeros precisely at the lattice, and can be differentiated away from them. Pairing \(\omega\) and \(-\omega\) shows that \(\sigma\) is odd. Its logarithmic derivative and its negative derivative are

\[
\begin{aligned}
\zeta(z)&=\frac1z+
\sum_{\omega\ne0}\left(
\frac1{z-\omega}+\frac1\omega+\frac z{\omega^2}\right),\\
\wp(z)&=-\zeta'(z)=\frac1{z^2}
+\sum_{\omega\ne0}\left(
\frac1{(z-\omega)^2}-\frac1{\omega^2}\right).
\end{aligned}
\]

The function \(\wp\) is even, and
\(\wp'(z)=-2\sum_{\omega\in\Gamma}(z-\omega)^{-3}\)
is periodic by absolute convergence and reindexing. Consequently
\(\wp(z+\omega_j)-\wp(z)\) is constant. Evaluate at
\(z=-\omega_j/2\), which is not a lattice point for a basis generator. Evenness makes that constant zero. Thus \(\wp\) is periodic, and
\(\zeta(z+\omega_j)-\zeta(z)=\eta_j\) is constant.

Integrate \(\zeta\) counterclockwise around a translated fundamental parallelogram with no zero on its boundary. Its one enclosed simple pole has residue one. Comparing opposite edges gives

\[
\eta_1\omega_2-\eta_2\omega_1=2\pi i.
\tag{6}
\]

Integrating the logarithmic-derivative identity gives

\[
\sigma(z+\omega_j)=
-\exp\left(\eta_j(z+\omega_j/2)\right)\sigma(z).
\]

The sign follows by evaluating the ratio at \(-\omega_j/2\) and using oddness. These elementary identities also fix our full-period convention; the generators here are full periods. A reference for the Weierstrass functions is [NIST, Definitions and periodic properties](https://dlmf.nist.gov/23.2).

Put \(c=\pi/A_\Gamma\). Equation (6), and
\(\overline{\omega_1}\omega_2-\overline{\omega_2}\omega_1=2iA_\Gamma\),
show that a single complex number \(a\) satisfies

\[
\eta_j-a\omega_j=c\overline{\omega_j},
\qquad j=1,2.
\]

Define \(F_\Gamma(z)=e^{-az^2/2}\sigma(z)\). The exponential has no zeros. The preceding identities give

\[
|F_\Gamma(z+\omega_j)|
=e^{c\operatorname{Re}(z\overline{\omega_j})+c|\omega_j|^2/2}
|F_\Gamma(z)|.
\]

It follows that \(Q(z)=|F_\Gamma(z)|e^{-c|z|^2/2}\) is periodic on \(\Gamma\). Away from its zeros, the ratio \(Q(z)/\operatorname{dist}(z,\Gamma)\) is positive and continuous. At each lattice point it has a positive limit, since that zero is simple and distance agrees with \(|z-\omega|\) in a small neighbourhood of \(\omega\). Thus the ratio extends to a strictly positive continuous function on the compact torus \(\mathbb C/\Gamma\). Its minimum and maximum give (5). \(\square\)

**Theorem 7.2 (weighted lattice interpolation and the sharp threshold).** Suppose \(d_{\Gamma_1}>d_{\Gamma_2}\). For every
\[
p\notin\Gamma_2-\Gamma_1
\]
there is a nonzero meromorphic function \(\varphi_p\) with simple poles precisely at \(p+\Gamma_1\), simple zeros precisely at \(\Gamma_2\), and

\[
\int_{\mathbb C}
\left(\frac{\operatorname{dist}(z-p,\Gamma_1)}
{\operatorname{dist}(z,\Gamma_2)}\right)^2
|\varphi_p(z)|^2\,dA(z)<\infty.
\tag{7}
\]

The exceptional set is countable, so this holds for almost every \(p\). If \(d_{\Gamma_1}\le d_{\Gamma_2}\), no nonzero meromorphic function with at most simple poles on \(p+\Gamma_1\), zeros at every point of \(\Gamma_2\), and (7) exists, for any \(p\).

**Proof.** Let \(c_j=\pi d_{\Gamma_j}\), and use the functions of Lemma 7.1. For a nonexceptional \(p\), the two lattices do not intersect. Set

\[
\varphi_p(z)=
e^{-c_1\overline p\,z}
\frac{F_{\Gamma_2}(z)}{F_{\Gamma_1}(z-p)}.
\tag{8}
\]

The zeros and poles have the asserted locations and orders. The exponential has neither zeros nor poles. By the two bounds (5), the weighted absolute value in (7) is bounded above by a constant times

\[
\exp\left(
\frac{c_2|z|^2-c_1|z-p|^2}{2}
-c_1\operatorname{Re}(\overline p\,z)\right)
=e^{-c_1|p|^2/2}e^{-(c_1-c_2)|z|^2/2}.
\tag{9}
\]

At a zero or pole the weighted expression has a finite limit, so the omitted points do not affect integration. The square of (9) is integrable because \(c_1-c_2>0\); its area integral is
\(e^{-c_1|p|^2}\pi/(c_1-c_2)\). This proves existence and its growth estimate.

For the converse, suppose \(\varphi\) has the asserted poles and zeros. Then

\[
u(z)=\varphi(z)\frac{F_{\Gamma_1}(z-p)}{F_{\Gamma_2}(z)}
\]

is entire. The numerator cancels each allowed pole, and the zeros of \(\varphi\) cancel the denominator. If the lattices intersect, the same order count still proves regularity. Let \(v(z)=e^{c_1\overline p\,z}u(z)\), also entire. The lower bounds as well as the upper bounds in (5) show that (7) is equivalent, up to fixed positive comparison constants, to

\[
\int_{\mathbb C}|v(z)|^2e^{(c_2-c_1)|z|^2}\,dA(z)<\infty.
\tag{10}
\]

If \(c_2\ge c_1\), the weight in (10) is at least one. Therefore \(v\) is an entire \(L^2(\mathbb C,dA)\) function. The mean-value inequality on every disk about \(w\) gives

\[
|v(w)|^2\le\frac1{\pi R^2}\int_{|z-w|<R}|v(z)|^2\,dA(z)
\le\frac{\|v\|_2^2}{\pi R^2}.
\]

Letting \(R\to\infty\) proves \(v(w)=0\). Since \(w\) is arbitrary, \(\varphi=0\). This proves the sharp threshold, including equality. \(\square\)

The construction explains why the pole lattice must have the larger density. The quadratic growth of its entire lattice function appears in the denominator of (8). Its excess cancels all but a decaying Gaussian. For a nonexceptional \(p\), the full weighted meromorphic space is obtained by replacing the constant one in (8) by an arbitrary entire function \(v\) with
\(\int|v(z)|^2e^{-(c_1-c_2)|z|^2}\,dA<\infty\).

The existence theorem is proved directly. The following construction proves the measured-dimension assertion with its groupoid and trace normalization explicit.

### The measured dimension of the meromorphic field

The ordinary dimension found in Exercise 6 is infinite. A measured dimension requires a specified equivariant field and trace. We now construct the natural lattice field and compute its trace directly, including lattices with nontrivial common periods.

Put \(T_j=\mathbb C/\Gamma_j\), \(V=T_1\times T_2\), \(c_j=\pi d_j\), and \(a=c_1-c_2>0\). The additive group \(\mathbb C\) acts diagonally by
\(([z_1],[z_2])+t=([z_1+t],[z_2+t])\).
Use the action groupoid with

\[
r(v,t)=v,\qquad s(v,t)=v+t,
\qquad (v,t)(v+t,t')=(v,t+t').
\]

Its range fibre is \(\mathbb C\) with Euclidean area measure. Stabilizers \(\Gamma_1\cap\Gamma_2\) are retained; the range fibres remain \(\mathbb C\) when these stabilizers are nontrivial. Give \(V\) normalized product Haar measure \(\mu(V)=1\). Inversion \((v,t)\mapsto(v+t,-t)\) preserves \(d\mu(v)dA(t)\), so the unit-measure theorem defines an invariant transverse measure \(\Lambda\).

The Haar transverse function is faithful and proper: \(V\times\{|t|\le n\}\) exhausts the groupoid, and its fibre mass after any left translation is \(\pi n^2\). All the standard Borel and \(\sigma\)-finite hypotheses hold. This specifies the measured groupoid whose formal dimension is used below.

The normalization also agrees with the counting densities. On the transversal \(N_1=\{0\}\times T_2\), use coordinates \(t=z_1,u=z_2-z_1\) near \(z_1=0\). The real Jacobian is one, and
\(d\mu=(A_{\Gamma_1}A_{\Gamma_2})^{-1}dA(t)dA(u)\).
Thus \(\Lambda(N_1)=1/A_{\Gamma_1}=d_1\). Similarly the transversal \(N_2=T_1\times\{0\}\) has mass \(d_2\).

**Lemma 7.3 (the lattice line bundles).** Each \(F_{\Gamma_j}\) in Lemma 7.1 is a holomorphic section of a Hermitian line bundle \(L_j\) on \(T_j\), with one simple zero at the lattice point. In its lifted coordinate frame the squared metric is \(e^{-c_j|z|^2}\).

**Proof.** For \(\omega\in\Gamma_j\), the ratio
\(J_\omega(z)=F_{\Gamma_j}(z+\omega)/F_{\Gamma_j}(z)\)
extends to a nonvanishing entire function: both numerator and denominator have the same simple zero set. Periodicity of the normalized absolute value, proved in Lemma 7.1, gives

\[
|J_\omega(z)|
=\exp\bigl(c_j\operatorname{Re}(\overline\omega z)+c_j|\omega|^2/2\bigr).
\]

The entire function obtained by dividing \(J_\omega\) by
\(\exp(c_j\overline\omega z+c_j|\omega|^2/2)\)
has constant absolute value one and is constant by the open mapping theorem. Hence
\(J_\omega(z)=\epsilon_\omega\exp(c_j\overline\omega z+c_j|\omega|^2/2)\), with \(|\epsilon_\omega|=1\).
The ratio definition gives the cocycle identity
\(J_{\omega+\omega'}(z)=J_\omega(z+\omega')J_{\omega'}(z)\).
These are the bundle transition functions. Moreover

\[
e^{-c_j|z+\omega|^2}|J_\omega(z)|^2=e^{-c_j|z|^2},
\]

so the stated metric descends. The transformation law for \(F_{\Gamma_j}\) makes it a section, and its simple lattice zeros descend to the single zero at \(0\in T_j\). \(\square\)

Let \(E=\operatorname{pr}_1^*L_1\otimes(\operatorname{pr}_2^*L_2)^*\) on \(V\). For \(v=([z_1],[z_2])\), pull it back to the action fibre \(t\mapsto v+t\). Let \(H_v\) be its square-integrable holomorphic sections. Choice of lifts \(z_1,z_2\) gives an entire coefficient \(u(t)\) with norm

\[
\int_{\mathbb C}|u(t)|^2
\exp\bigl(-c_1|z_1+t|^2+c_2|z_2+t|^2\bigr)\,dA(t).
\tag{11}
\]

Changes of lifts use precisely the transition functions in Lemma 7.3, so this norm and Hilbert space are intrinsic.

For almost every \(v\), the two translated lattices
\(-z_1+\Gamma_1\) and \(-z_2+\Gamma_2\) are disjoint. The exceptional set is saturated and Haar-null: in local lifts the coincidence equations are \(z_1-z_2=\omega_1-\omega_2\), a countable union of real codimension-two affine subsets. Let \(W_v\) be the meromorphic space with the pole, zero and weighted norm conditions for these two translated lattices. On this full-measure set, the map

\[
\varphi(t)\longmapsto
u(t)=\varphi(t)\frac{F_{\Gamma_1}(z_1+t)}{F_{\Gamma_2}(z_2+t)}
\tag{12}
\]

is a bounded invertible map onto \(H_v\). Indeed the simple zeros cancel precisely the allowed poles and prescribed zeros; its inverse is \(uF_{\Gamma_2}/F_{\Gamma_1}\). The two sides of Lemma 7.1 bound the norm in (11) above and below by fixed positive multiples of

\[
\int_{\mathbb C}|\varphi(t)|^2
\frac{\operatorname{dist}(z_1+t,\Gamma_1)^2}
{\operatorname{dist}(z_2+t,\Gamma_2)^2}\,dA(t).
\]

The constants are independent of \(v\). Changing \(dA\) to \(2dA=|dz\wedge d\bar z|\) merely changes this Hilbert norm by a fixed positive factor and gives an equivalent unitary field after rescaling.

The maps (12) are equivariant. An arrow \((v,b)\) sends a section in the fibre at \(v+b\) to the fibre at \(v\) by \(t\mapsto t-b\); the lifted bundle point and the two lattice-function arguments are unchanged. For \(W\) this is exactly translation of the meromorphic function, which preserves its weighted norm. The bundle transition functions make this statement independent of the chosen lifts. Set \(W\) to zero on the negligible exceptional set if a field defined everywhere is desired. Its measurable structure can be transported from \(H\) through (12), and its square integrability follows from the bounded equivariant isomorphism and the projected regular realization of \(H\) below.

**Theorem 7.4 (the density difference as formal dimension).** For this measured action groupoid and normalization,

\[
\dim_\Lambda W=d_1-d_2.
\tag{13}
\]

In particular the complete transverse family over \(N_2\), parameterized by \(p=-z_1\) with \(z_2=0\), gives the meromorphic spaces of Theorem 7.2. Their measured dimension means (13), and their ordinary Hilbert-space dimension is infinite.

**Proof.** Put \(\ell=c_1\overline{z_1}-c_2\overline{z_2}\). Multiplication of the entire coefficient \(u(t)\) by \(e^{-\ell t}\), and by the constant
\(e^{(-c_1|z_1|^2+c_2|z_2|^2)/2}\),
turns (11) into the Gaussian holomorphic norm
\(\int|h(t)|^2e^{-a|t|^2}\,dA(t)\).
The Gaussian holomorphic space is closed: on every bounded disk the mean-value inequality bounds evaluation on a smaller disk by its weighted \(L^2\) norm; a Cauchy sequence therefore converges uniformly on compact sets to an entire function, with its \(L^2\) limit the same function.

If \(h(t)=\sum_{n\ge0}h_nt^n\), Parseval on circles and Tonelli in the radius give

\[
\|h\|^2=\sum_{n\ge0}|h_n|^2\frac{\pi n!}{a^{n+1}}.
\]

Thus the normalized monomials
\((a^{n+1}/(\pi n!))^{1/2}t^n\)
are a complete orthonormal basis. Summing their coefficient kernels gives
\(K_a(t,t')=(a/\pi)e^{a t\overline{t'}}\).
In the unitary, unweighted \(L^2(dA)\) frame, the orthogonal projection kernel is consequently

\[
P_a(t,t')=\frac a\pi
\exp\bigl(-a(|t|^2+|t'|^2)/2+a t\overline{t'}\bigr),
\qquad
|P_a(t,t')|=\frac a\pi e^{-a|t-t'|^2/2}.
\tag{14}
\]

For the bundle frame in (11), the additional factor is the unit phase
\(\exp(i\operatorname{Im}(\ell(t-t')))\), which changes no norm in (14). These local formulas define measurable fibre projections compatible with the transition functions, and translation preserves the intrinsic holomorphic subspaces. Hence \(H\) is an equivariant closed subfield of the regular field \(L^2(\mathbb C;s^*E)\), with projection \(P\) in its measured endomorphism algebra. The regular field and its projected subfield are square integrable by the random-operator prerequisite, including when the action has stabilizers.

In unitary local bundle frames, the reduced convolution kernel is obtained by setting the output coordinate to zero in (14). It therefore has magnitude
\((a/\pi)e^{-a|t|^2/2}\).
Its absolute value is integrable on each fibre, so it satisfies the bounded finite-support test condition of Corollary 9.4 of [Weights on random operators and formal dimension](https://kokunoyumeto.github.io/open-math-courses-public/courses/noncommutative-integration/weights-on-random-operators-and-formal-dimension.html#section-9). With \(\delta=1\) and \(P^*P=P\), that corollary gives

\[
\tau(P)
=\int_V\int_{\mathbb C}
\left(\frac a\pi\right)^2e^{-a|t|^2}\,dA(t)\,d\mu(v)
=\left(\frac a\pi\right)^2\frac\pi a
=\frac a\pi=d_1-d_2.
\]

The factor \(\mu(V)=1\) is part of the specified normalization. By Definition 10.1 and Proposition 10.2 of that lesson, this trace is \(\dim_\Lambda H\), and the bounded equivariant isomorphism (12) preserves dimension. It is therefore \(\dim_\Lambda W\), proving (13). Countably many orthogonal monomials at each nonexceptional parameter prove the ordinary infinite dimension. \(\square\)

![The lattice meromorphic field becomes a Gaussian projection whose trace is the density difference](../figures/lattice-projection-trace.png)

*Figure 7.1. The domains, bundle metric, equivariant map and trace normalization are those of Lemma 7.3 and Theorem 7.4. The curve is the exact normalized magnitude \(e^{-x^2/2}\), with dimensionless horizontal coordinate \(x=\sqrt a\,|t-t'|\). The action fibres are \(\mathbb C\), retaining stabilizers \(\Gamma_1\cap\Gamma_2\). The trace is the integrated squared kernel, rather than a count of the ordinary infinite basis.*

Reference for the measured-dimension assertion: [Connes], the lattice corollary and its density-difference discussion. The direct Gaussian projection computation above also specifies the groupoid and measure normalization.


## 8. Examples and exercises

**Example 8.1 (a product of spheres).** For \(V=S^2\times S^1\), with spherical leaves and transverse measure of total mass \(a\), the harmonic fields have measured dimensions \(\beta_0=\beta_2=a\), \(\beta_1=0\). Hence their alternating sum is \(2a\). With unit-round leaf metrics, \((2\pi)^{-1}\int Kd\mu=(2\pi)^{-1}4\pi a=2a\). This checks the normalization in Corollaries 6.16 and 6.20.

**Exercise 1 (basic).** For a linear map \(D:\mathbb C^3\to\mathbb C^2\) of rank two, verify Theorem 2.1 for every \(t>0\).

**Solution.** There is one zero eigenvalue in \(D^*D\) and none in \(DD^*\). The two nonzero eigenvalues agree with multiplicity by polar decomposition. Thus the heat traces differ by one, equal to the difference of the kernel dimensions. Their actual nonzero eigenvalues need not be calculated.

**Exercise 2 (intermediate).** In Example 1.1, show directly that no Borel transversal can realize the harmonic constants as the square-summable functions on its full inverse image in the holonomy cover.

**Solution.** A transversal meets the central leaf in zero, a positive finite number \(n\), or countably infinitely many points. Its full inverse image has respectively zero, \(2n\), or infinitely many points. The square-summable space has those dimensions, while the harmonic constants have dimension one. Thus even a nonequivariant unitary is impossible. Equivariance would impose a further obstruction through the regular permutation action.

**Exercise 3 (intermediate).** Prove that metric equivalence preserves the closure of an exact-form space even if that space is not closed.

**Solution.** Uniformly equivalent norms have the same convergent and Cauchy sequences and the same topology. A vector is in the closure of a subspace precisely when every norm ball about it meets that subspace. Equivalent norms give mutually containing balls, so the closures agree. This is why reduced cohomology, with closure of the exact forms, is used in Proposition 4.1.

**Exercise 4 (advanced).** Under the Hausdorff hypotheses of Corollary 6.16, let the oriented surface leaves with compact finite-holonomy leaves be negligible. Prove the integrated curvature inequality and determine when equality holds.

**Solution.** The calculation of Section 5 gives the integrated curvature as \(-2\pi\beta_1\). It is nonpositive because the trace of a projection is nonnegative. Equality holds exactly when the harmonic one-form projection has measured trace zero. Faithfulness of the measured trace makes that projection zero in the random-operator algebra, meaning that the harmonic space vanishes off a transverse-null saturated set.

**Exercise 5 (advanced).** Explain why a KMS weight for a nontrivial cocycle cannot simply replace the trace in the proof of Theorem 2.1.

**Solution.** The proof uses equality of the weight on \(X^*X\) and \(XX^*\) for the operator transporting the two nonzero spectral parts. A general KMS weight does not satisfy this trace identity. Its modular automorphisms enter instead. Hence the invariant-measure condition is substantive for this measured index proof, even though individual weighted heat expansions can be considered for a nontrivial cocycle.

**Exercise 6 (advanced).** In Theorem 7.2, replace the constant numerator in (8) by a polynomial in \(z\). Prove that this still satisfies (7), and compute the squared Gaussian norm of \(z^n\).

**Solution.** Put \(a=c_1-c_2>0\). The bounds (5) reduce the norm to a constant comparison with \(\int_{\mathbb C}|z|^{2n}e^{-a|z|^2}\,dA\). Polar coordinates give
\[
2\pi\int_0^\infty r^{2n+1}e^{-ar^2}\,dr
=\frac{\pi n!}{a^{n+1}}.
\]
Every polynomial consequently gives a finite norm. The monomials are orthogonal by angular integration, so the resulting weighted meromorphic space has infinitely many linearly independent elements. This ordinary Hilbert-space dimension is different from the measured dimension in a foliation.

**Exercise 7 (intermediate).** On the flat \(p\)-torus, \(p\ge1\), let \(B_m=(1-\Delta)^{m/2}\). Prove that \(B_m\) is Hilbert–Schmidt exactly when \(m<-p/2\), including the failure at equality.

**Solution.** The Fourier eigenvalues are \((1+4\pi^2|n|^2)^{m/2}\), \(n\in\mathbb Z^p\). Their squares sum to \(\sum_n(1+4\pi^2|n|^2)^m\). In a dyadic annulus of radius \(R\), there are upper and lower bounds proportional to \(R^p\) for the lattice count, obtained by enclosing and inscribing unions of unit cubes. Its contribution is therefore bounded above and below by positive constants times \(R^{p+2m}\), for all sufficiently large dyadic \(R\). The geometric series converges exactly when \(p+2m<0\). At equality every annulus contributes a fixed positive lower bound, so the sum diverges. The square root of the convergent sum is the Hilbert–Schmidt norm; it is an ordinary torus norm, not a measured dimension of an infinite-cover field.

**Exercise 8 (advanced).** Show that the threshold \(s>p/2\) in Theorem 6.9 is sharp among uniform assertions of this form. Use the flat \(p\)-torus as one compact leaf, with \(\delta=1\) and transverse atomic mass one.

**Solution.** Take the positive Laplacian with eigenvalues \(4\pi^2|n|^2\), and set \(T=(1+\Delta)^{-s}\). It maps the Fourier space \(H^{-s}\) to \(H^s\) with norm one: multiplying its output coefficients by \(\langle2\pi n\rangle^s\) gives exactly the input norm with multiplier \(\langle2\pi n\rangle^{-s}\). The trace is \(\sum_{n\in\mathbb Z^p}(1+4\pi^2|n|^2)^{-s}\). The dyadic annulus calculation of Exercise 7 makes this finite exactly when \(2s>p\), and infinite at equality as well as below it. Since there is one compact leaf with trivial holonomy and atomic mass one, the measured trace is this ordinary trace. Thus a bounded map between those Sobolev spaces need not be in the weight domain when \(s\le p/2\).

**Exercise 9 (intermediate).** In Theorem 6.8, explain why knowing the domain of \(A\) alone does not immediately prove the domain formula for every real power. Identify the two additional steps used in the proof.

**Solution.** The domain of one closed operator does not determine how its powers compare to a coordinate scale. First, each integer power \(A^k\) extends the formal elliptic differential expression of order \(2mk\), whose essential self-adjointness identifies its domain and gives uniform graph estimates. Second, localization and reconstruction make the coordinate spaces an interpolation retract of Fourier spaces. Spectral interpolation then compares both scales at intermediate positive exponents, and duality gives negative exponents. These steps also preserve constants uniformly across the covers.

**Exercise 10 (advanced).** For the flat torus \(\mathbb R^p/\mathbb Z^p\), compute the entire local diagonal expansion of the positive Laplacian plus a constant potential \(q\ge0\). Check the powers and the normalization in Theorem 6.12.

**Solution.** On \(\mathbb R^p\), Fourier inversion of \(e^{-t|\xi|^2}\) gives \((4\pi t)^{-p/2}e^{-|x-y|^2/(4t)}\); the one-variable Gaussian integral and its product establish the factor. The constant potential multiplies this by \(e^{-qt}\). Periodizing in \(y\) gives the torus kernel: its differentiated series converges for each \(t>0\), it solves the heat equation, and its Fourier coefficient at \(n\) is \(e^{-t(4\pi^2|n|^2+q)}\), so spectral calculus identifies it with the heat operator. On the diagonal it equals

\[
(4\pi t)^{-p/2}e^{-qt}
\sum_{\ell\in\mathbb Z^p}e^{-|\ell|^2/(4t)}.
\]

The sum over \(\ell\ne0\) is \(O(e^{-1/(8t)})\) for \(0<t\le1\): split each exponential into two equal factors, bound one by \(e^{-1/(8t)}\), and sum the other using \(t\le1\). Thus only the \(\ell=0\) term contributes to any power expansion. Taylor's formula gives
\(b_{2n}=(4\pi)^{-p/2}(-q)^n/n!\) and \(b_{2n+1}=0\). The powers are \(t^{n-p/2}=t^{(2n-p)/2}\), as asserted for order two. The local symbol recursion gives the same answer, since its only lower coefficient is \(h_0=q\), and its terms are \(v_{2n}=(-qt)^n e^{-t|\xi|^2}/n!\). This example checks both the factor \((4\pi)^{-p/2}\) and the negative sign of the first potential coefficient.

**Exercise 11 (intermediate).** For a unit-round oriented two-sphere, check every rank and sign in the supertrace calculation of Corollary 6.16.

**Solution.** Here \(K=1\), \(\operatorname{Scal}=2\), and the bundle ranks are \(1,2,1\). The endomorphism in the first coefficient of Lemma 6.15 is \(1/3\) in degree zero and degree two. In degree one, \(\operatorname{Ric}=I\), so it is \(-2I/3\). Its alternating fibre trace is \(1/3-2(-2/3)+1/3=2\). The common factor \((4\pi)^{-1}\) gives \(1/(2\pi)\), and integration over area \(4\pi\) gives two. This agrees with the dimensions of harmonic constants and volume forms, while the harmonic one-form space is zero. The negative potential term in Lemma 6.15 is essential to this check.

**Exercise 12 (advanced).** For the product of two oriented unit-round two-spheres, compute the constant local supertrace in Theorem 6.18 and its integral. Check it against the harmonic dimensions.

**Solution.** The product curvature has two skew blocks, \(\Omega_{12}=\alpha_1\) and \(\Omega_{34}=\alpha_2\), with all mixed blocks zero. Hence \(\operatorname{Pf}(\Omega/(2\pi))=\alpha_1\wedge\alpha_2/(4\pi^2)\). Each sphere has area \(4\pi\), so the integral is four. In dimension four the relevant Clifford degree is eight; the top symbol of \(U_2\) gives supertrace four, while \(U_0,U_1\) have zero supertrace. Multiplication by \((4\pi)^{-2}\) gives the density \(1/(4\pi^2)\), agreeing with the Pfaffian.

Each two-sphere has one harmonic constant and one harmonic volume form. Its degree-one harmonic space is zero, since the surface formula gives Euler number two and these two other dimensions already contribute two. On the product the Hodge Laplacian is the sum of the two nonnegative factor Laplacians on the tensor exterior algebra. Its zero space is the tensor product of their zero spaces: the sum's quadratic form can vanish only if both factor terms vanish. The harmonic dimensions are therefore \((1,0,2,0,1)\), whose alternating sum is four.

**Exercise 13 (intermediate).** Expand the Thom form in Lemma 6.19 for rank two. Verify directly its vertical integral and zero-section pullback, keeping the auxiliary-variable sign.

**Solution.** Because the auxiliary variables anticommute with the ordinary one-forms, the coefficient of \(\eta_1\eta_2\) in \(\exp(Dx_1\eta_1+Dx_2\eta_2-\Omega_{12}\eta_1\eta_2)\) is \(-Dx_1\wedge Dx_2-\Omega_{12}\). The prefactor sign is also minus. Thus
\[
U=(2\pi)^{-1}e^{-(x_1^2+x_2^2)/2}
(Dx_1\wedge Dx_2+\Omega_{12}).
\]
On a fibre this is the normalized two-dimensional Gaussian volume form and has integral one. On the zero section the covariant coordinate differentials vanish, leaving \(\Omega_{12}/(2\pi)\). This checks the sign and normalization of the Euler representative. Closedness follows directly as well: \(D(Dx_1\wedge Dx_2)=\Omega_{12}(x_1Dx_1+x_2Dx_2)\), which cancels the Gaussian derivative wedged with the curvature term.

**Exercise 14 (advanced).** A compact oriented leaf \(L\) has genus \(g\), finite holonomy of order \(h\), and transverse atomic mass one. Find its measured harmonic dimensions. Check that its Euler contribution agrees with the leaf's Euler number, and explain why its degree-zero measured dimension is \(1/h\).

**Solution.** The holonomy cover has genus \(\widetilde g\), with \(2-2\widetilde g=h(2-2g)\); lift a finite cell decomposition to prove the covering formula. Its harmonic dimensions are \((1,2\widetilde g,1)\). In Corollary 6.22, \(q=1/\operatorname{vol}(\widetilde L)\), while the unit measure of the atomic leaf is \(\operatorname{vol}(L)\). The multiplier therefore contributes \(1/h\), giving \((\beta_0,\beta_1,\beta_2)=(1/h,2\widetilde g/h,1/h)\). Their alternating sum is \((2-2\widetilde g)/h=2-2g\). Degree zero illustrates why measured dimension must retain the covering normalization even when the ordinary harmonic space has dimension one.

**Exercise 15 (advanced).** In the neighbourhood \((\widetilde L\times T)/H\) of Proposition 6.23, describe the leaf through a transverse point \(u\), its holonomy, and its covering degree over the central leaf in the transverse projection model.

**Solution.** Put \(H_u=\{h:h(u)=u\}\). The leaf is \(\widetilde L/H_u\): the components \(\widetilde L\times\{h(u)\}\) are identified by the diagonal action, and equivalence within the component at \(u\) is exactly the deck action of \(H_u\). It is compact and covers \(L=\widetilde L/H\) with degree \(|H|/|H_u|\), since the cover's fibre is the finite coset set \(H/H_u\). Its holonomy is the image of \(H_u\) in germs at \(u\); elements acting identically on a neighbourhood contribute the identity germ, so it can be a quotient of \(H_u\). Thus both covering multiplicity and finite holonomy are accounted for, and the statement does not assume every nearby leaf has the same holonomy as the central one.

**Exercise 16 (advanced).** On a flat oriented surface, let the twisting line have constant curvature \(R^E=iB\alpha\), and give the spin structure the trivial determinant line. Verify the local sign in Theorem 6.26 directly from the curvature potential, using \(\Gamma=i c_1c_2\).

**Solution.** The product \(c_1c_2\) has eigenvalues \(-i,i\) in the positive and negative grading spaces, respectively. The potential in (16) is \(c_1c_2 iB\), so these two eigenvalues are \(B,-B\). The first nonzero supertrace coefficient is therefore \(-B-B=-2B\). Multiplication by \((4\pi)^{-1}\) gives \(-B/(2\pi)\). The characteristic expression is \(iR^E/(2\pi)=-B\alpha/(2\pi)\), agreeing with that density. The determinant factor contributes no degree-two term because the tangent curvature is zero. This check concerns the local coefficient; on a compact torus a line bundle and constant curvature connection must also satisfy the integral quantization condition on \(iR^E/(2\pi)\).

## References

- [Connes] Alain Connes, *A survey of foliations and operator algebras*, in *Operator Algebras and Applications, Part I*, Proceedings of Symposia in Pure Mathematics 38, American Mathematical Society, 1982. [Author's text](https://alainconnes.org/wp-content/uploads/foliationsfine.pdf).
- [Connes 1979] Alain Connes, *Sur la théorie non commutative de l'intégration*, in *Algèbres d'opérateurs*, Lecture Notes in Mathematics 725, Springer, 1979. [IHÉS preprint](https://omeka.ihes.fr/files/original/f1e66a7f4de4523e6937af152ff16092.pdf).
- [NIST] Frank W. J. Olver and collaborators, editors, *NIST Digital Library of Mathematical Functions*, Chapter 23, Weierstrass elliptic and modular functions. [Definitions and periodic properties](https://dlmf.nist.gov/23.2).
- [Atiyah] Michael F. Atiyah, *Elliptic operators, discrete groups and von Neumann algebras*, Astérisque 32–33 \(1976\). [Numdam record](https://www.numdam.org/item/AST_1976__32-33__43_0/).
- [Breuer] Manfred Breuer, *Fredholm theories in von Neumann algebras I*, Mathematische Annalen 178 \(1968\), and *II*, Mathematische Annalen 180 \(1969\). [Original article I](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0178/LOG_0053.pdf); [original article II](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0180/LOG_0056.pdf).
- [Atiyah–Bott–Patodi] Michael F. Atiyah, Raoul Bott, and Vijay K. Patodi, *On the heat equation and the index theorem*, Inventiones Mathematicae 19 \(1973\). [Original article](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0019/LOG_0022.pdf).
