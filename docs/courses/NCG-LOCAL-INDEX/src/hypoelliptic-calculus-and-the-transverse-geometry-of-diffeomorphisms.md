# Symbol calculus, transverse geometry and geometric index formulas

*Written by GPT-6.1 Sol (OpenAI), September–October 2026, at Ultra. Self-checked by the writing AI. Separate Codex sessions checked the earlier numbered arguments and solutions under explicit imports. The transferred classical and geometric arguments retain those bounded checks; the current arrangement and domain adaptations are author checked. Exact reviewer models unverified. Original text: public domain (CC0).*

A diffeomorphism need not preserve a Riemannian metric. We can nevertheless give its action a metric description by enlarging the space: a point of the enlarged space remembers both a point of the manifold and a metric on its tangent space. The resulting invariant structure measures directions along the metric fiber and directions on the original manifold separately. Its analytic scaling assigns weight one to the first group of directions and weight two to the second.

We use the operator conventions of [Spectral triples and dimension spectrum](spectral-triples-and-dimension-spectrum.md), the logarithmic trace construction of [Singular values and the Dixmier trace](singular-values-and-the-dixmier-trace.md), and the distinction between an ordinary elliptic symbol and an adapted symbol explained below. References for the geometric and analytic construction are [Connes–Moscovici 1995], [Ponge 2008], and [Hilsum–Skandalis 1987].

## 1. Metrics on a subbundle and on its quotient

**Definition.** A triangular structure on a smooth manifold \(M\) consists of an integrable smooth subbundle \(V\subset TM\), a positive definite metric \(g_V\) on \(V\), and a positive definite metric \(g_N\) on \(N=TM/V\). Integrable means that the bracket of two smooth sections of \(V\) is again a section of \(V\). It gives a foliation locally; a choice of complementary subbundle is additional data.

Here is the linear algebra behind the terminology. Choose a complement temporarily, so that a tangent vector is written as \((v,n)\). A linear map preserving \(V\) has matrix

\[
\begin{pmatrix}A&C\\0&B\end{pmatrix}.
\tag{1.1}
\]

It preserves the two specified metrics precisely when \(A\) and \(B\) are orthogonal in those metrics. The off-diagonal map \(C:N\to V\) is unconstrained. Thus triangular isometries can shear transverse directions into leaf directions. This is why the structure need not determine a metric on all of \(TM\).

**Theorem 1.1 (the bundle of tangent-space metrics).** Let \(W\) be a smooth manifold of dimension \(n\). Let

\[
\pi:P\to W,\qquad P_x=\{g:\ g\text{ is a positive definite symmetric form on }T_xW\}.
\tag{1.2}
\]

Then \(P\) has a canonical triangular structure. With \(V=\ker d\pi\), its vertical metric at \((x,g)\) is

\[
\langle h,k\rangle_{V,g}
=\operatorname{tr}(g^{-1}h\,g^{-1}k),
\qquad h,k\in\operatorname{Sym}^2T_x^*W,
\tag{1.3}
\]

and its quotient metric is \(g\) through the isomorphism
\(T_{(x,g)}P/V_{(x,g)}\simeq T_xW\).
Every diffeomorphism of \(W\) lifts to a diffeomorphism of \(P\) preserving both metrics.

**Proof.** In a local frame, \(P\) is the open cone of positive definite matrices in the vector bundle of symmetric forms. Thus a vertical tangent vector is a symmetric form \(h\). The expression in (1.3) is independent of the frame: under a change \(g\mapsto A^tgA\) and \(h\mapsto A^thA\), the endomorphism \(g^{-1}h\) is conjugated by \(A^{-1}\). The trace of a product is unchanged. It is positive definite because

\[
\operatorname{tr}(g^{-1}h\,g^{-1}h)
=\operatorname{tr}\bigl((g^{-1/2}hg^{-1/2})^2\bigr)>0
\quad(h\neq0).
\]

The vertical subbundle is integrable: its leaves are the fibers of the smooth submersion \(\pi\). The map \(d\pi\) is surjective with kernel \(V\), giving the quotient identification in the statement.

For \(\varphi:W\to W\), let \(A=d\varphi_x\). Its lift sends \((x,g)\) to \((\varphi(x),g')\), where

\[
g'(u,w)=g(A^{-1}u,A^{-1}w),
\qquad g'=A^{-t}gA^{-1}.
\tag{1.4}
\]

A vertical variation transforms as \(h'=A^{-t}hA^{-1}\). Consequently
\((g')^{-1}h'=A(g^{-1}h)A^{-1}\), which proves invariance of (1.3). On the quotient, \(d\pi\) intertwines the lifted derivative with \(A\), and
\(g'(Au,Aw)=g(u,w)\). This proves quotient-metric invariance. Smoothness follows in each local matrix chart. \(\square\)

The fiber dimension is \(v=n(n+1)/2\). No connection on \(W\) entered the construction.

On a one-dimensional coordinate chart, write \(g=e^r\,dx^2\). In the normalization (1.3), the vertical metric is \(dr^2\), the quotient metric is \(e^r\,dx^2\), and the lifted action is

\[
(x,r)\longmapsto
\bigl(\varphi(x),\,r-2\log|\varphi'(x)|\bigr).
\tag{1.5}
\]

Indeed, (1.4) gives \(e^{r'}=e^r/|\varphi'|^2\). The density
\(e^{r/2}|dx\,dr|\) is invariant: the Jacobian of (1.5) has absolute determinant \(|\varphi'|\), which cancels the factor \(e^{r'/2}/e^{r/2}=|\varphi'|^{-1}\). If \(r=2s\), the vertical metric becomes \(4ds^2\). A choice of scale for the invariant metric on the fiber can change that factor; it cannot change the transformation law for the actual quadratic form.

In general, a triangular structure also determines a density without a complement. The exact sequence
\(0\to V\to TM\to N\to0\)
gives a canonical determinant-line identification

\[
|\det T^*M|\simeq|\det V^*|\otimes|\det N^*|.
\tag{1.6}
\]

The product of the two metric densities is therefore a density on \(M\). To verify independence of a splitting, change the splitting by a shear as in (1.1) with \(A=B=I\). Its determinant is one, so the product volume is unchanged. If \(V\) and \(N\) are oriented, the same argument gives a volume form.

## 2. Replacing a signature operator by a second-order operator

The following operator identity explains why a longitudinal derivative will receive a different weight. It also fixes the treatment of harmonic forms.

Let \(X\) be a closed oriented Riemannian manifold of even dimension. On complex differential forms let \(d\) be the exterior derivative and \(d^*\) its \(L^2\) adjoint. Use the signature involution \(\gamma\), with
\(\gamma^2=I\), \(\gamma^*=\gamma\), and
\(d^*=-\gamma d\gamma\).
We use the closed elliptic realization of the Hodge operator

\[
S=d+d^*,\qquad
\Delta=S^2=dd^*+d^*d.
\tag{2.1}
\]

The domain facts follow from the ordinary, weight-one form of our parametrix argument in Theorem 10.4. The principal symbol of \(S\) is \(i(\xi\wedge-\iota_{\xi^\sharp})\), whose square is \(|\xi|^2I\). The theorem therefore gives a parametrix of order \(-1\) and the estimate \(\|u\|_{H^1}\leq C(\|Su\|_2+\|u\|_2)\). Smooth approximation in \(H^1\) identifies the closure domain with \(H^1\). If \(u\) is in the adjoint domain, then \(Su\in L^2\) distributionally; the same parametrix puts \(u\) in \(H^1\). Formal symmetry now proves equality of the operator and adjoint domains, hence selfadjointness. This is exactly the domain mechanism of Corollary 10.5, with order one in place of order two.

The inclusion \(H^1\hookrightarrow L^2\) is compact: in finitely many chart tori, Fourier truncation leaves operator-norm tail \(O(R^{-1})\), while the retained Fourier maps have finite rank. Thus \((S-i)^{-1}\) is compact. Lemma 9.2 of [Singular values and the Dixmier trace](singular-values-and-the-dixmier-trace.md) gives the spectral core and finite-dimensional kernel; repeated parametrix regularity makes every eigenform smooth. On smooth forms, \(d\Delta=\Delta d\) and \(d^*\Delta=\Delta d^*\), directly from \(d^2=(d^*)^2=0\). Consequently both maps preserve each finite-dimensional eigenspace of \(\Delta=S^2\). The identities below can first be checked there and then extended on the graph domains.

Set

\[
A=d-d^*,\qquad B=dd^*-d^*d,\qquad
U_\lambda=\Delta^{1/2}+\lambda A,\quad 0\leq\lambda\leq1.
\tag{2.2}
\]

**Proposition 2.1.** The operators \(U_\lambda\) commute with \(\gamma\), and

\[
U_\lambda U_\lambda^*=U_\lambda^*U_\lambda
=(1+\lambda^2)\Delta,
\tag{2.3}
\]

\[
U_\lambda S U_\lambda^*
=(1-\lambda^2)\Delta S
+2\lambda\Delta^{1/2}B.
\tag{2.4}
\]

In particular \(U_1 S U_1^*=2\Delta^{1/2}B\).

**Proof.** The relations \(d^2=(d^*)^2=0\) give

\[
A^*=-A,\quad A^2=-\Delta,\quad
AS=B,\quad SA=-B,\quad A S A=\Delta S.
\tag{2.5}
\]

For example,
\[
ASA=(dd^*-d^*d)(d-d^*)=dd^*d+d^*dd^*=\Delta S.
\]
The operators \(A,S,B\) commute with \(\Delta\) on the common core. Therefore multiplying
\((\Delta^{1/2}+\lambda A)(\Delta^{1/2}-\lambda A)\)
gives (2.3). Expanding the product with \(S\) in the middle gives
\(\Delta S+\lambda(AS-SA)\Delta^{1/2}-\lambda^2ASA\),
which is (2.4). Finally, conjugating \(d\) by \(\gamma\) gives \(-d^*\), and conjugating \(d^*\) gives \(-d\). Hence \(\gamma A\gamma=A\), whereas \(\gamma S\gamma=-S\). Thus \(\gamma\) commutes with \(\Delta\), its positive square root, and \(U_\lambda\). \(\square\)

Let \(P_0\) be the projection onto \(\ker\Delta\). All of \(d,d^*,S,A,B\) vanish there. Define

\[
V_\lambda
=\frac1{\sqrt{1+\lambda^2}}\,
U_\lambda\Delta^{-1/2}(I-P_0)+P_0,
\tag{2.6}
\]

where the inverse square root is taken on \((I-P_0)H\).

**Corollary 2.2.** The family \(V_\lambda\) is a norm-continuous family of unitaries commuting with \(\gamma\) and \(\Delta\), with \(V_0=I\), and

\[
V_1SV_1^*=B\Delta^{-1/2}(I-P_0).
\tag{2.7}
\]

The right side is the selfadjoint operator \(D_L\) determined by
\(D_L|D_L|=B\), including value zero on \(\ker\Delta\).

**Proof.** On \((I-P_0)H\), put \(J=A\Delta^{-1/2}\). Equation (2.5) gives \(J^*=-J\) and \(J^2=-I\). Thus \((I+\lambda J)/\sqrt{1+\lambda^2}\) is unitary and depends continuously on \(\lambda\) in norm. On the kernel, (2.6) is the identity. Commutation with \(\gamma\) and \(\Delta\) follows from the same properties of \(A\). Equation (2.4) at \(\lambda=1\), divided by \(2\Delta\), gives (2.7).

On each positive eigenspace of \(\Delta\), multiplication shows \(B^2=\Delta^2\). Thus \(|B|=\Delta\) and
\(D_L=B\Delta^{-1/2}\) has \(|D_L|=\Delta^{1/2}\). The product \(D_L|D_L|\) is \(B\). Scalar functional calculus gives uniqueness, since the real function \(x\mapsto x|x|\) is bijective. The zero eigenspace was retained throughout. \(\square\)

In particular, the bounded transforms of the operators in (2.7) are related by a norm-continuous unitary conjugation commuting with the signature grading. This supplies the operator homotopy behind the second-order replacement; the kernel has not been discarded.

## 3. Longitudinal and transverse differentiation

Return to a triangular manifold \(M\). For the signature construction, assume \(V\) and \(N\) are oriented and have even ranks \(v,n\). Its bundle of forms is

\[
E=\Lambda^\bullet V_\mathbb C^*
\otimes\Lambda^\bullet N_\mathbb C^*.
\tag{3.1}
\]

The metrics and (1.6) define \(L^2(M,E)\) without a complement.

The quotient bundle has a canonical flat connection along the leaves. For \(X\in\Gamma(V)\), and a vector field \(Y\) representing \(\bar Y\in\Gamma(N)\), set

\[
\nabla_X^{\mathrm B}\bar Y=\overline{[X,Y]}.
\tag{3.2}
\]

This is the Bott connection. If \(Y\) is replaced by \(Y+Z\) with \(Z\in\Gamma(V)\), integrability gives \([X,Z]\in\Gamma(V)\), so the definition is independent of the representative. It is linear over functions in \(X\), because the extra term in \([fX,Y]\) is vertical, and it satisfies the connection rule in \(\bar Y\). Jacobi's identity gives

\[
[\nabla_X^{\mathrm B},\nabla_Z^{\mathrm B}]
=\nabla_{[X,Z]}^{\mathrm B}.
\tag{3.3}
\]

The induced connection on \(\Lambda^\bullet N^*\) is consequently flat along every leaf. Its covariant leafwise exterior derivative \(d_L\) on (3.1) satisfies \(d_L^2=0\).

For completeness, the formula on a coefficient-valued leafwise \(r\)-form is

\[
\begin{aligned}
(d_L\omega)(X_0,\ldots,X_r)
={}&\sum_i(-1)^i\nabla^{\mathrm B}_{X_i}
\omega(X_0,\ldots,\widehat X_i,\ldots,X_r)\\
&+\sum_{i<j}(-1)^{i+j}
\omega([X_i,X_j],X_0,\ldots,\widehat X_i,\ldots,\widehat X_j,\ldots,X_r).
\end{aligned}
\tag{3.4}
\]

Applying it twice, the second derivatives combine into the curvature in (3.3), and the remaining bracket terms cancel by Jacobi. Thus the asserted square-zero property follows from the displayed connection, rather than from an assumption that the transverse metric is constant along a leaf.

Choose a splitting \(TM=V\oplus H\) and the induced identification \(j_H:E\to\Lambda^\bullet T_\mathbb C^*M\). Define \(d_H\) as the component of \(j_H^{-1}dj_H\) increasing transverse form degree by one and preserving vertical form degree. It is a first-order differential operator. Unlike \(d_L\), its square need not vanish.

If \(f\) is locally constant along each leaf, then \(df\) is canonically a section of \(N^*\), and

\[
[d_H,f]\omega=df\wedge\omega.
\tag{3.5}
\]

Indeed, \(d(fj_H\omega)=df\wedge j_H\omega+f\,d(j_H\omega)\); taking the required bidegree gives (3.5). This identity is independent of the splitting.

Let \(d_L^*,d_H^*\) be formal adjoints in the already specified density, and put

\[
Q_L=d_Ld_L^*-d_L^*d_L,\qquad
Q_H=d_H+d_H^*,\qquad
Q=Q_L\varepsilon_N+Q_H,
\quad\varepsilon_N=(-1)^{\deg_N}.
\tag{3.6}
\]

Since \(Q_L\) preserves transverse degree, it commutes with \(\varepsilon_N\); since \(Q_H\) changes it by one, it anticommutes with \(\varepsilon_N\). The operator \(Q\) is formally selfadjoint on compactly supported smooth sections. Formal selfadjointness alone does not specify a selfadjoint realization on a noncompact manifold.

## 4. The quartic principal symbol

In a foliation chart write the covector as \(\xi=(\xi_V,\xi_N)\), and dilate it by

\[
\delta_\lambda\xi=(\lambda\xi_V,\lambda^2\xi_N).
\tag{4.1}
\]

Define its homogeneous length and homogeneous dimension by

\[
\rho(\xi)=\bigl(|\xi_V|^4+|\xi_N|^2\bigr)^{1/4},
\qquad Q_{\mathrm{dim}}=v+2n.
\tag{4.2}
\]

Then \(\rho(\delta_\lambda\xi)=\lambda\rho(\xi)\), and the Jacobian of the dilation is \(\lambda^{Q_{\mathrm{dim}}}\). A vertical differential operator has weight one; a transverse differential operator has weight two. Thus both summands of \(Q\) in (3.6) have weighted order two.

Here is its symbol calculation with the exterior-algebra signs specified. Let \(e_\eta\) be exterior multiplication by a real covector and \(\iota_\eta=e_\eta^*\). They satisfy

\[
e_\eta^2=\iota_\eta^2=0,\qquad
e_\eta\iota_\eta+\iota_\eta e_\eta=|\eta|^2I.
\tag{4.3}
\]

Put
\(b_V(\eta)=e_\eta\iota_\eta-\iota_\eta e_\eta\)
and
\(c_N(\zeta)=i(e_\zeta-\iota_\zeta)\).
The first is selfadjoint and degree-preserving; the second is selfadjoint and transverse-degree-reversing. If vertical forms precede transverse forms in \(j_H\), wedge multiplication by a transverse covector includes \(\varepsilon_V=(-1)^{\deg_V}\). In that convention the principal symbol is

\[
q_2(\xi)
=b_V(\xi_V)\otimes\varepsilon_N
+\varepsilon_V\otimes c_N(\xi_N).
\tag{4.4}
\]

The factor \(\varepsilon_V\) is the usual tensor sign for exterior forms. It can instead be included in the notation for transverse Clifford multiplication; it must be kept consistent with \(j_H\).

**Proposition 4.1.** The weighted principal symbol in (4.4) is independent of the complement, and

\[
q_2(\xi)^2
=\bigl(|\xi_V|^4+|\xi_N|^2\bigr)I.
\tag{4.5}
\]

Hence it is invertible for every nonzero graded covector.

**Proof.** In a leafwise chart, \(d_L\) has symbol \(ie_{\xi_V}\) and \(d_L^*\) has symbol \(-i\iota_{\xi_V}\). Their second-order difference has symbol \(b_V\). Formula (3.5), or direct differentiation of the de Rham operator, gives the transverse part of (4.4).

Changing the complement replaces a transverse lift by that lift plus a vertical vector field. Such an additional derivative has weight one. Thus it cannot change the weight-two transverse principal symbol. The vertical operator was defined without a complement, so its principal symbol is unchanged as well.

Let \(X=e_\eta\iota_\eta\) and \(Y=\iota_\eta e_\eta\). Equation (4.3) gives \(XY=YX=0\) and \(X+Y=|\eta|^2I\). Hence
\((X-Y)^2=(X+Y)^2=|\eta|^4I\).
Likewise \(c_N(\zeta)^2=|\zeta|^2I\).
The two terms in (4.4) anticommute: \(b_V\) commutes with \(\varepsilon_V\), whereas \(c_N\) anticommutes with \(\varepsilon_N\). The cross terms in their square therefore cancel. This proves (4.5), whose scalar factor is positive when \(\xi\neq0\). \(\square\)

The degree-two symbol is elliptic for the dilation (4.1), although its vertical and transverse pieces have different ordinary differential orders. Sections 10–12 use it to construct a parametrix, identify the spectral powers and prove regularity. The closed manifold has a canonical selfadjoint closure; the noncompact statement specifies a selfadjoint realization as a hypothesis.

## 5. Adapted symbols and their operator estimates

Write \(d=v+n\) for the ordinary coordinate dimension. A smooth length at all frequencies is
\[
r(\xi)=\bigl(1+|\xi_V|^4+|\xi_N|^2\bigr)^{1/4}.
\tag{5.1}
\]
For a multi-index \(\beta=(\beta_V,\beta_N)\), its weighted length is
\[
|\beta|_w=|\beta_V|+2|\beta_N|.
\tag{5.2}
\]

**Definition.** A matrix symbol \(a(x,\xi)\) belongs locally to \(S_w^q\) if, for every compact base set \(K\), and every \(\alpha,\beta\), it satisfies
\[
\|\partial_x^\alpha\partial_\xi^\beta a(x,\xi)\|
\leq C_{K,\alpha,\beta}\,
r(\xi)^{q-|\beta|_w},
\qquad x\in K.
\tag{5.3}
\]
It is classical for the adapted dilation if it has an expansion
\[
a\sim a_q+a_{q-1}+a_{q-2}+\cdots,
\qquad
a_{q-j}(x,\delta_\lambda\xi)=\lambda^{q-j}a_{q-j}(x,\xi)
\quad(\xi\neq0),
\tag{5.4}
\]
where a fixed cutoff near zero is understood and the remainder after \(N\) terms belongs to \(S_w^{q-N}\), with every differentiated estimate in (5.3). The quantization is
\[
(\operatorname{Op}(a)u)(x)
=(2\pi)^{-d}\int e^{i(x-y)\cdot\xi}
a(x,\xi)u(y)\,dy\,d\xi.
\tag{5.5}
\]
As usual, the integral for nonintegrable orders is defined by distributional Fourier transformation or by oscillatory regularization. A smoothing remainder is allowed.

This defines the local adapted class. The weighted estimates govern its composition in Theorem 5.4, coordinate transport in Theorem 10.2 and complex powers in Theorem 11.1. The ordinary order of a symbol need not equal its weighted order.

A homogeneous function in (5.4) has exactly the derivative degree in (5.3). To see this, differentiate its dilation identity in a vertical covariable: the chain rule contributes a factor \(\lambda\), so that derivative has degree \(q-j-1\). A transverse covariable contributes \(\lambda^2\) and lowers degree by two. Iteration gives \(q-j-|\beta|_w\). Smoothness on the compact surface \(\rho=1\), with compact \(x\)-support, then gives the estimate at large frequencies.

**Theorem 5.1 (local Sobolev mapping).** Suppose \(a\in S_w^q\) has compact support in its base variable. Define
\[
\|u\|_{H_w^s}
=\|r(\xi)^s\widehat u(\xi)\|_{L^2_\xi},
\tag{5.6}
\]
using the unitary Fourier transform, and use completion for negative \(s\). Then, for every real \(s\),
\[
\operatorname{Op}(a):H_w^s\longrightarrow H_w^{s-q}
\quad\text{is bounded}.
\tag{5.7}
\]
In particular, symbols of nonpositive weighted order give bounded \(L^2\) operators.

**Proof.** Fourier transformation in \(x\), and integration by parts there, give
\[
\|\widehat a(\eta-\xi,\xi)\|
\leq C_M r(\xi)^q(1+|\eta-\xi|)^{-M}.
\tag{5.8}
\]
The \(x\)-derivatives used are integrable because their support is in a fixed compact set. Their bounds are exactly (5.3) with \(\beta=0\).

For all \(\eta,\xi\), the elementary inequalities for sums of fourth and second powers imply
\[
r(\eta)\leq C\,r(\xi)(1+|\eta-\xi|),\qquad
r(\xi)\leq C\,r(\eta)(1+|\eta-\xi|).
\tag{5.9}
\]
For example, \(|\eta_V|^4\leq8(|\xi_V|^4+|\eta_V-\xi_V|^4)\) and
\(|\eta_N|^2\leq2(|\xi_N|^2+|\eta_N-\xi_N|^2)\).
Taking fourth roots bounds \(r(\eta)\) by a constant times
\(r(\xi)+|\eta-\xi|+|\eta-\xi|^{1/2}\), and \(r(\xi)\geq1\) gives (5.9).

The Fourier kernel conjugated by the two Sobolev weights has norm at most
\[
C_M
\left(\frac{r(\eta)}{r(\xi)}\right)^{s-q}
(1+|\eta-\xi|)^{-M}
\leq C'_M(1+|\eta-\xi|)^{-M+|s-q|}.
\tag{5.10}
\]
Choose \(M>d+|s-q|\). The right side is integrable in either variable with a uniform bound. The integral Schur test gives (5.7), first on Schwartz functions and then on the indicated completions. Finally, if \(q\leq0\), the inclusion \(H_w^{-q}\subset L^2\) has norm at most one because \(r\geq1\), giving the \(L^2\) assertion. \(\square\)

The same proof is valid for torus symbols, using a Fourier series in \(x\) and a sum over input frequencies. It then uses the summable bound
\((1+|j-k|)^{-M+|s-q|}\).

**Proposition 5.2 (compactness after localization).** Under the compact base-support hypothesis, a symbol of strictly negative weighted order defines a compact operator on \(L^2(\mathbb R^d)\).

**Proof.** Write \(q=-a\), \(a>0\). Right multiplication by the Fourier multiplier \(r(D)^a\) changes its left symbol exactly to \(a(x,\xi)r(\xi)^a\), which has order zero and is bounded by Theorem 5.1. Thus
\(P=Br(D)^{-a}\) with \(B\) bounded. Choose a smooth frequency cutoff \(\chi_R\), equal to one for \(r(\xi)\leq R\) and zero for \(r(\xi)\geq2R\). Then
\[
\|P(I-\chi_R(D))\|
\leq \|B\|R^{-a}.
\tag{5.11}
\]
The operator \(P\chi_R(D)\) is Hilbert–Schmidt. Indeed its kernel, Fourier transformed in \(y\) at each fixed \(x\), has squared norm proportional to
\(\int\!\int\|a(x,\xi)\chi_R(\xi)\|_{\mathrm{HS}}^2\,d\xi\,dx\).
Both supports in this integral are compact. Hence \(P\) is a norm limit of compact operators. \(\square\)

On a closed manifold the resulting localized negative-order operators and smoothing kernels are compact after a finite partition. On a noncompact manifold, the localization hypothesis is essential, as in the ordinary trace theorem in the first lesson.

**Theorem 5.3 (the critical singular-value bound).** Let \(P\) be an adapted operator of weighted order \(-Q_{\mathrm{dim}}\) on a closed triangular manifold, represented in every foliation chart by the symbol estimates (5.3), with smooth off-diagonal kernel. Then
\[
\mu_j(P)=O\bigl((j+1)^{-1}\bigr).
\tag{5.12}
\]
The same holds for an operator with compact kernel support on a noncompact triangular manifold.

**Proof.** First use a periodic foliation chart on a flat torus. There are at most \(CR^{Q_{\mathrm{dim}}}\) lattice points with \(r(k)\leq R\): each vertical coordinate has absolute value at most \(R\), and each transverse coordinate at most \(R^2\). Thus the multiplier
\(r(D)^{-Q_{\mathrm{dim}}}\)
has singular values \(O((j+1)^{-1})\), including any fixed finite matrix multiplicity.

Right multiplication of \(P\) by \(r(D)^{Q_{\mathrm{dim}}}\) gives a bounded order-zero operator by the torus form of Theorem 5.1. Hence
\[
P=Br(D)^{-Q_{\mathrm{dim}}}
\]
has the same singular-value bound, by the ideal estimate (1.5) in the first lesson.

For localization, cut the kernel into finitely many diagonal chart pieces and a smooth part separated from the diagonal. The chart pieces extend into flat tori by the local symbol representation; bounded coordinate and bundle transfers preserve the singular-value bound. Smooth compact kernels satisfy the same assertion with any negative order. A finite sum of such bounds remains a bound of the form (5.12). To verify the last point directly, approximate each of \(m\) summands by an operator of rank at most \(N\), with error at most \(C_j/(N+1)\). Their sum has rank at most \(mN\) and error at most \(\sum_jC_j/(N+1)\). The approximation-number formula (1.1) then gives (5.12), after changing its constant by a fixed factor depending on \(m\). \(\square\)

The theorem concerns an operator represented by compatible local adapted symbols. Sections 10–12 place the mixed signature operator, its complex powers and its transported commutators in that class. The estimate above then supplies its summability bound.

**Theorem 5.4 (local composition).** For symbols \(a\in S_w^q\) and \(b\in S_w^t\) with compact base support, the composition has a left symbol in \(S_w^{q+t}\), with expansion
\[
a\# b\sim
\sum_\alpha\frac{i^{-|\alpha|}}{\alpha!}
(\partial_\xi^\alpha a)(\partial_x^\alpha b).
\tag{5.13}
\]
After retaining the terms with \([\alpha]<N\), the remainder is in \(S_w^{q+t-N}\). The symbols may be matrices, and the order of their factors in (5.13) is as displayed. If both symbols are classical, their product is classical.

**Proof.** Write
\(\widehat b(\eta,\xi)=\int e^{-iy\cdot\eta}b(y,\xi)\,dy\).
Fourier transformation of \(\operatorname{Op}(b)u\), followed by substitution in \(\operatorname{Op}(a)\), gives the exact symbol
\[
(a\#b)(x,\xi)
=(2\pi)^{-d}\int e^{ix\cdot\eta}
a(x,\xi+\eta)\widehat b(\eta,\xi)\,d\eta.
\tag{5.14}
\]
For a Schwartz input all these integrations are justified by absolute convergence: \(\widehat b\) decays faster than any power of \(\eta\), with polynomial growth in \(\xi\), and the Fourier transform of the input decays faster than every power of \(\xi\). Compact base support ensures that the intermediate output is a compactly supported smooth function.

Integration by parts in the base variable gives, for every \(M,\beta\),
\[
\|\partial_\xi^\beta\widehat b(\eta,\xi)\|
\leq C_{M,\beta}r(\xi)^{t-[\beta]}(1+|\eta|)^{-M}.
\tag{5.15}
\]
The two-sided comparison (5.9) gives, uniformly for \(0\leq s\leq1\) and every real \(h\),
\[
r(\xi+s\eta)^h
\leq C_h r(\xi)^h(1+|\eta|)^{|h|}.
\tag{5.16}
\]
These estimates, differentiated in \(x,\xi\), prove that (5.14) has order \(q+t\).

Apply ordinary Taylor's theorem to \(a(x,\xi+\eta)\) through degree \(N-1\). Each term integrates to
\(i^{-|\alpha|}(\partial_\xi^\alpha a)(\partial_x^\alpha b)/\alpha!\).
The remainder is a finite sum of integrals containing
\[
\eta^\alpha\int_0^1
\frac{N(1-s)^{N-1}}{\alpha!}
\partial_\xi^\alpha a(x,\xi+s\eta)\,ds,
\qquad |\alpha|=N.
\]
After any specified \(x,\xi\)-derivatives, (5.15) and (5.16) bound its integrand by a constant times
\(r(\xi)^{q+t-[\alpha]-[\beta]}\)
times an integrable power of \(1+|\eta|\); choose \(M\) after those derivatives and \(N\) have been specified. Since \([\alpha]\geq|\alpha|=N\), the remainder satisfies every estimate for \(S_w^{q+t-N}\). Terms with \(|\alpha|<N\) but \([\alpha]\geq N\) have that same lower order and may be moved into the remainder. This gives the stated weighted truncation.

Finally insert the homogeneous expansions of \(a,b\). For any desired remainder order only finitely many homogeneous terms and indices can contribute. Covariable differentiation lowers degree by \([\alpha]\), while base differentiation preserves it, so their products give homogeneous terms in descending integer degrees. The estimates just proved control the remaining terms. \(\square\)

In particular, if an order-one symbol has a scalar principal part, its commutator with an order-zero symbol has order at most zero. The undifferentiated degree-one matrix commutator vanishes, and every differentiated product in (5.13) loses at least one weighted degree. Iterating gives order zero at every stage. Corollary 11.3 constructs the required scalar principal part of \(|D|\), and Section 12 verifies the closed commutator domains.

## 6. Extending homogeneous symbols through the origin

The trace coefficient has two descriptions: an integral over high frequencies, and a logarithm in the kernel near the diagonal. We now prove their relation. The weights in this calculation are the weights of the dilation, including the weight two of each transverse coordinate.

Let \(w_i=1\) in the vertical coordinates and \(w_i=2\) in the transverse coordinates. Write
\[
[\alpha]=\sum_iw_i\alpha_i,\qquad
E=\sum_iw_i\xi_i\partial_{\xi_i},\qquad
S_\rho=\{\xi:\rho(\xi)=1\},\qquad
d\mu_\rho=(i_E\,d\xi)|_{S_\rho}.
\tag{6.1}
\]
Orient \(S_\rho\) so that this measure is positive. The map
\((r,\theta)\mapsto\delta_r\theta\) gives the polar integration formula
\[
d\xi=r^{Q_{\mathrm{dim}}-1}\,dr\,d\mu_\rho(\theta).
\tag{6.2}
\]
Indeed, the dilation has Jacobian \(r^{Q_{\mathrm{dim}}}\), and its radial derivative is \(r^{-1}E\); contraction by that derivative proves (6.2).

**Theorem 6.1 (homogeneous extension and its obstruction).** Suppose \(a\) is smooth away from zero and
\[
a(\delta_r\xi)=r^q a(\xi),\qquad q\in\mathbb C,\ r>0.
\tag{6.3}
\]
It has a tempered homogeneous distributional extension of degree \(q\), unless \(q=-Q_{\mathrm{dim}}-k\) for a weighted degree \(k=[\alpha]\) and at least one of the moments
\[
m_\alpha(a)=\int_{S_\rho}\theta^\alpha a(\theta)\,d\mu_\rho(\theta),
\qquad [\alpha]=k,
\tag{6.4}
\]
is nonzero. At a nonexceptional degree the extension is unique. At an exceptional degree it exists exactly when all the moments in (6.4) vanish, and then its ambiguity consists of the derivatives \(\partial^\alpha\delta_0\) with \([\alpha]=k\).

Here homogeneous means that, for
\(f_\lambda(\xi)=f(\delta_{\lambda^{-1}}\xi)\),
\[
T(f_\lambda)=\lambda^{q+Q_{\mathrm{dim}}}T(f).
\tag{6.5}
\]
These statements hold entry by entry for a matrix symbol.

**Proof.** Begin with the analytic family
\[
A(z)(f)=\int \rho(\xi)^z a(\xi)f(\xi)\,d\xi,
\qquad
\operatorname{Re}(q+z)>-Q_{\mathrm{dim}},
\tag{6.6}
\]
on Schwartz test functions. Its behavior at infinity causes no difficulty: on any compact set of \(z\)'s the symbol has at most a fixed polynomial growth, which a Schwartz function dominates.

At zero use the weighted Taylor expansion, uniformly for \(\theta\in S_\rho\):
\[
f(\delta_r\theta)
=\sum_{[\alpha]\leq N}
\frac{\partial^\alpha f(0)}{\alpha!}\theta^\alpha r^{[\alpha]}
+O(r^{N+1}),\qquad 0<r\leq1.
\tag{6.7}
\]
To justify this with ordinary Taylor's theorem, expand to ordinary degree \(N\). Its remainder is \(O(|\delta_r\theta|^{N+1})=O(r^{N+1})\). Each discarded term of weighted degree greater than \(N\) is also \(O(r^{N+1})\), since the weights are positive integers. This proves (6.7), including bounds by finitely many Schwartz seminorms.

Split (6.6) at \(r=1\), subtract the sum in (6.7) in its inner integral, and integrate the subtracted monomials explicitly. This continues \(A(z)\) to
\(\operatorname{Re}(q+z)>-Q_{\mathrm{dim}}-N-1\), with possible simple poles
\[
z=-q-Q_{\mathrm{dim}}-[\alpha],
\]
whose contributions are
\[
\frac{m_\alpha(a)}{\alpha!}\,
\frac{\partial^\alpha f(0)}
{z+q+Q_{\mathrm{dim}}+[\alpha]}.
\tag{6.8}
\]
The remainder is holomorphic in the stated half-plane by dominated convergence, also after differentiating in \(z\). Increasing \(N\) gives a meromorphic family on the whole plane.

Change variables \(\xi=\delta_\lambda\eta\) first in the region of convergence. Meromorphic continuation then gives
\[
A(z)(f_\lambda)
=\lambda^{q+Q_{\mathrm{dim}}+z}A(z)(f).
\tag{6.9}
\]
If \(A\) is regular at zero, \(T=A(0)\) is the desired extension.

Suppose \(q=-Q_{\mathrm{dim}}-k\). The residue at zero is the point-supported distribution
\[
R_k(f)=\sum_{[\alpha]=k}
\frac{m_\alpha(a)}{\alpha!}\partial^\alpha f(0).
\tag{6.10}
\]
Put \(T=\operatorname{FP}_{z=0}A(z)\). Comparing constant coefficients in (6.9) gives the exact defect
\[
T(f_\lambda)
=\lambda^{-k}\bigl(T(f)+(\log\lambda)R_k(f)\bigr).
\tag{6.11}
\]
Distinct derivatives of \(\delta_0\) are linearly independent, so \(R_k=0\) exactly when every moment in (6.4) vanishes.

It remains to check that a different extension cannot remove a nonzero obstruction. Two extensions differ by a distribution supported at zero, hence by a finite linear combination of derivatives of \(\delta_0\). This elementary distribution fact follows by Taylor expanding a test function at zero to an order exceeding the finite local order of the distribution; the Taylor remainder is annihilated after shrinking a cutoff to zero. A derivative with multi-index \(\alpha\) transforms by \(\lambda^{-[\alpha]}\). Differentiate the scaling equation at \(\lambda=1\). On these point-supported distributions, the resulting operator is diagonal, with eigenvalues \(k-[\alpha]\). Its image has no component of weighted degree \(k\), whereas the right side required to cancel (6.11) is precisely \(R_k\) of that degree. Cancellation is therefore impossible when \(R_k\neq0\).

The same diagonal calculation proves the uniqueness assertions: a homogeneous point-supported difference of degree \(q\) can contain only indices with \(-[\alpha]=q+Q_{\mathrm{dim}}\). At a nonexceptional degree there are none; at an exceptional degree they are exactly those in the statement. \(\square\)

If \(v=0\), only even weighted degrees occur. Thus the exceptional degrees are \(-2n-2j\), rather than every negative integer below \(-2n\). Listing extra possible degrees is harmless only if their obstruction is understood to be zero. Replacing \([\alpha]\) by ordinary \(|\alpha|\) in the moments would change the actual obstruction.

## 7. The logarithmic term in a kernel

**Theorem 7.1 (the critical kernel coefficient).** Let \(a\) have degree \(-Q_{\mathrm{dim}}\), and let \(b(\xi)\) be smooth everywhere, equal to \(a(\xi)\) for large \(\rho(\xi)\). Define its inverse Fourier transform by the convention in (5.5). Away from \(y=0\), it is smooth and, as \(y\to0\),
\[
\check b(y)=
(2\pi)^{-d}c(a)\log\frac1{\rho(y)}+O(1),
\qquad
c(a)=\int_{S_\rho}a(\theta)\,d\mu_\rho(\theta).
\tag{7.1}
\]
The bounded remainder may depend on the direction of approach. The sign in (7.1) corresponds to \(\log(1/\rho)\); the coefficient of \(\log\rho\) is its negative.

**Proof.** At the critical degree, (6.10) is \(R_0=c(a)\delta_0\). Let \(T\) be the finite-part extension and \(H=\check T\). The inverse Fourier transform of \(\delta_0\) is the constant \((2\pi)^{-d}\). Transforming (6.11) therefore gives
\[
H(\delta_\lambda y)
=H(y)-(2\pi)^{-d}c(a)\log\lambda.
\tag{7.2}
\]
This is initially a distribution identity. It is also a function identity outside zero. To see the asserted smoothness there, cut \(T\) into a compactly supported distribution and a symbol smooth at zero. The first has a smooth Fourier transform. For the second, integration by parts in \(\xi\) makes its oscillatory integral and every \(y\)-derivative convergent on compact sets disjoint from zero: sufficiently many covariable derivatives lower weighted degree past \(-Q_{\mathrm{dim}}\), even after the polynomial factors from \(y\)-differentiation. The integrations by parts are justified with a frequency cutoff and then by the integrable derivative bounds.

With \(y=\delta_{\rho(y)}\theta\), (7.2) gives
\[
H(y)=H(\theta)-(2\pi)^{-d}c(a)\log\rho(y),
\qquad \theta\in S_\rho.
\tag{7.3}
\]
The angular function \(H|_{S_\rho}\) is smooth and bounded. The right side is locally integrable by (6.2). It represents the entire distribution \(H\): their difference would be supported at zero and homogeneous of degree zero, because both have the same constant scaling defect. A point-supported homogeneous distribution has degree \(-Q_{\mathrm{dim}}-[\alpha]<0\), so that difference is zero.

Finally, \(T-b\) is compactly supported as a distribution in the covariable. Its Fourier transform is smooth, and bounded on a neighborhood of \(y=0\). Subtracting it from (7.3) proves (7.1). \(\square\)

The integral defining \(c(a)\) is independent of the transverse surface used to meet every dilation ray once. Indeed, the top-degree form \(a\,d\xi\) has dilation degree zero. Cartan's formula gives
\[
d\bigl(i_E(a\,d\xi)\bigr)
=\mathcal L_E(a\,d\xi)=0
\tag{7.4}
\]
away from zero. Stokes' theorem on the annulus between two such surfaces proves equality of their integrals. Replacing \(\rho\) by another positive smooth length homogeneous for the same dilation changes \(\log\rho\) by a bounded angular function. It therefore cannot change the coefficient in (7.1).

**Corollary 7.2 (the local classical kernel expansion).** Suppose a classical adapted symbol has an integer order \(q\), and expansion (5.4). Off the diagonal its kernel, for fixed \(x\), has the form
\[
k(x,x-y)
=\sum_{\substack{p=q,q-1,\ldots\\p>-Q_{\mathrm{dim}}}}
h_p(x,y)
+c(x)\log\frac1{\rho(y)}+O(1),
\tag{7.5}
\]
where \(h_p(x,\delta_\lambda y)=
\lambda^{-p-Q_{\mathrm{dim}}}h_p(x,y)\), and
\[
c(x)=(2\pi)^{-d}
\int_{S_\rho}a_{-Q_{\mathrm{dim}}}(x,\theta)\,d\mu_\rho(\theta).
\tag{7.6}
\]
If the expansion has no term of degree \(-Q_{\mathrm{dim}}\), set \(c(x)=0\). The statement is entrywise for a bundle-valued kernel. It describes the kernel outside the diagonal; differential operators may also have distributions supported on the diagonal.

**Proof.** Retain the finitely many homogeneous terms with degree at least \(-Q_{\mathrm{dim}}\), cutting them off near zero. Each term of degree \(p>-Q_{\mathrm{dim}}\) has a unique homogeneous tempered extension by Theorem 6.1. Its inverse Fourier transform is homogeneous of degree \(-p-Q_{\mathrm{dim}}\), by a change of variables in the Fourier transform, and smooth outside zero by the integration-by-parts argument above. Cutting the original term off changes that transform by a smooth function.

For the degree \(-Q_{\mathrm{dim}}\) term use Theorem 7.1. The remaining symbol has order at most \(-Q_{\mathrm{dim}}-1\), so it is integrable in \(\xi\), locally uniformly in \(x\). Its inverse Fourier transform is continuous and bounded by its \(L^1\) norm. Adding the finitely many terms gives (7.5). \(\square\)

The same argument handles a complex order: retain terms with real degree greater than \(-Q_{\mathrm{dim}}\); a term with real degree equal to that number and nonzero imaginary part has a bounded homogeneous Fourier transform of real degree zero. A logarithm occurs at the exact degree \(-Q_{\mathrm{dim}}\). Thus (7.6) isolates the critical coefficient without assigning a logarithm to an oscillatory complex degree.

The kernel coefficient becomes global once its coordinate transformation is known. We establish that transformation next, and then prove the trace property using the local product formula.

**Proposition 7.3 (the intrinsic logarithmic density).** Suppose an operator is represented by classical adapted symbols in foliation charts. Write its kernel in each chart relative to coordinate Lebesgue measure in the input variable. The endomorphism coefficient \(c(x)\) of \(\log(1/\rho(x-y))\) defines a global endomorphism-valued density. Its fiber trace is independent of the bundle frame.

**Proof.** A change of foliation coordinates has the form
\[
x'_V=f(x_V,x_N),\qquad x'_N=g(x_N).
\tag{7.7}
\]
At a fixed base point \(x\), set \(F_x(y)=\varphi(x)-\varphi(x-y)\). For \(y=\delta_r\theta\), Taylor's theorem gives
\[
\delta_{1/r}F_x(\delta_r\theta)
=(A\theta_V,B\theta_N)+O(r),
\quad A=\partial_Vf(x),\ B=dg(x_N).
\tag{7.8}
\]
More precisely, the left side extends smoothly in \(r\) to \(r=0\), with a Taylor expansion to any specified order, uniformly on \(S_\rho\). The transverse expression depends only on the transverse variables, which proves its required divisibility by \(r^2\). The vertical expression is divisible by \(r\). Both \(A,B\) are invertible, so their graded image of \(S_\rho\) stays away from zero.

Consequently \(\rho(F_x(y))/\rho(y)\) and its reciprocal are bounded near zero. The logarithm of this ratio is bounded. An old logarithmic term therefore contributes the same scalar logarithm in new coordinates, with its coefficient multiplied by the input Jacobian at the diagonal and conjugated by the bundle-frame change at \(x\). The difference between those factors at \(x-y\) and at \(x\) is \(O(r)\); multiplied by \(\log r\), it remains bounded.

No term preceding the logarithm in (7.5) creates an additional logarithm under this substitution. A homogeneous term of negative integer degree \(j\) becomes \(r^j\) times a smooth function of \(r,\theta\), by (7.8). Expand that smooth function beyond degree \(-j\). The result has finitely many homogeneous powers and a bounded remainder, without a logarithm. Smooth Jacobian and frame factors have the same property. Terms of complex degree give powers of complex degree in the same way, and still do not create a logarithm. The bounded remainder stays bounded because the two adapted lengths are comparable.

Along each ray a finite sum of powers with negative real degree, bounded terms, and a constant multiple of \(\log r\) has a unique logarithmic coefficient. Comparing the kernel expansions in the two charts thus gives exactly the density transformation stated. Conjugation does not change its matrix trace. \(\square\)

## 8. Critical traces and the residue of arbitrary order

In this section \(d>0\), hence \(Q_{\mathrm{dim}}>0\). On a closed triangular manifold, assume the operator under consideration has the compatible classical local representations used above. On a noncompact manifold we impose compact kernel support when taking the global integral.

**Theorem 8.1 (the adapted critical trace formula).** If \(P\) has weighted order \(-Q_{\mathrm{dim}}\), then it is measurable for every logarithmic trace constructed in the first lesson, and
\[
\operatorname{Tr}_\omega(P)
=\frac1{Q_{\mathrm{dim}}(2\pi)^d}
\int_M\int_{S_{\rho,x}}
\operatorname{tr}a_{-Q_{\mathrm{dim}}}(x,\theta)
\,d\mu_{\rho,x}(\theta)\,dx.
\tag{8.1}
\]
No positivity or scalar-symbol hypothesis is required. Equivalently, the right side is
\(Q_{\mathrm{dim}}^{-1}\int_M\operatorname{tr}c(x)\),
using the density of Proposition 7.3.

**Proof.** The singular-value bound is Theorem 5.3. A symbol of order \(-Q_{\mathrm{dim}}-1\) is trace class locally. On a flat torus factor its operator as \(Br(D)^{-Q_{\mathrm{dim}}-1}\), with \(B\) bounded by Theorem 5.1. A dyadic lattice decomposition gives
\[
\sum_{k\in\mathbb Z^d}r(k)^{-Q_{\mathrm{dim}}-1}
\leq C\sum_{j\geq0}2^{jQ_{\mathrm{dim}}}
2^{-j(Q_{\mathrm{dim}}+1)}<\infty.
\tag{8.2}
\]
Finite chart localization gives the same conclusion globally. Thus only the critical homogeneous symbol matters, since a logarithmic trace vanishes on trace-class operators.

We compute first on the torus with periods \(2\pi\). Consider a positive semidefinite matrix symbol \(a(\xi)\), independent of \(x\), homogeneous of degree \(-Q_{\mathrm{dim}}\) away from zero. Assign any finite matrix value at zero. If \(\lambda_j(a(\theta))\) are its ordered eigenvalues, the bounded sets
\[
\Omega_j=\{\delta_r\theta:
0<r<\lambda_j(a(\theta))^{1/Q_{\mathrm{dim}}}\}
\tag{8.3}
\]
have volume
\[
|\Omega_j|=\frac1{Q_{\mathrm{dim}}}
\int_{S_\rho}\lambda_j(a(\theta))\,d\mu_\rho(\theta).
\tag{8.4}
\]
They are Jordan measurable. Their boundary away from zero is a radial graph of a continuous nonnegative function; by polar integration it has measure zero. The origin adds a set of measure zero.

Let \(N(t)\) count the eigenvalues of the Fourier multiplier \(a(D)\) greater than \(t>0\). The counts in (8.3) occur in the dilated lattice domains
\(\delta_{t^{-1/Q_{\mathrm{dim}}}}\Omega_j\).
After rescaling, lattice cells have side lengths
\(t^{1/Q_{\mathrm{dim}}}\) in the vertical variables and
\(t^{2/Q_{\mathrm{dim}}}\) in the transverse variables. Their diameter tends to zero and their volume is \(t\). Jordan measurability therefore gives
\[
tN(t)\longrightarrow C(a),\qquad
C(a)=\frac1{Q_{\mathrm{dim}}}
\int_{S_\rho}\operatorname{tr}a(\theta)\,d\mu_\rho(\theta).
\tag{8.5}
\]
If \(C(a)>0\), inversion of the two-sided counting bounds yields
\(\mu_j(a(D))\sim C(a)/(j+1)\); summing them gives
\(S_N(a(D))/\log N\to C(a)\).
If \(C(a)=0\), continuity and positivity make \(a\) identically zero on the sphere, leaving only a finite-rank multiplier. In both cases the ordinary limit proves measurability and the value \(C(a)\).

For a general complex matrix symbol, split it into Hermitian real and imaginary parts. A Hermitian homogeneous symbol becomes positive after adding
\(C\rho^{-Q_{\mathrm{dim}}}I\), with \(C\) at least its uniform norm on \(S_\rho\). Subtract that positive symbol again. Linearity now proves (8.5)'s trace value for every matrix symbol.

For the \(x\)-dependent symbol, expand on the torus:
\[
a(x,\xi)=\sum_{\ell\in\mathbb Z^d}
e^{i\ell\cdot x}a_\ell(\xi).
\tag{8.6}
\]
The coefficients on \(S_\rho\) decay faster than every power of \(|\ell|\), by integration by parts in \(x\). The critical multiplier estimate also gives, uniformly in \(\ell\),
\[
\|a_\ell(D)\|_{\mathcal M_{1,\infty}}
\leq C_d\sup_{S_\rho}\|a_\ell\|.
\tag{8.7}
\]
Indeed, the pointwise bound by
\(\sup\|a_\ell\|\rho(k)^{-Q_{\mathrm{dim}}}\)
and the box count in Theorem 5.3 bound its singular values by that constant divided by \(j+1\). The harmonic sum bounds the logarithmic ideal norm. Hence (8.6) converges absolutely in that ideal, after discarding a trace-class low-frequency correction.

Translation by \(z\) conjugates
\(e^{i\ell\cdot x}a_\ell(D)\) to
\(e^{i\ell\cdot z}e^{i\ell\cdot x}a_\ell(D)\).
Unitary invariance forces its logarithmic trace to vanish when \(\ell\neq0\): choose \(z\) for which the phase differs from one. Only the mean coefficient remains. Its value from (8.5) is precisely (8.1) on this torus, because
\[
a_0(\theta)=(2\pi)^{-d}\int_{\mathbb T^d}a(x,\theta)\,dx.
\]

Finally choose a finite smooth partition with \(\sum_i\psi_i^2=1\), each \(\psi_i\) supported in a foliation chart. Trace cyclicity gives
\[
\operatorname{Tr}_\omega(P)
=\sum_i\operatorname{Tr}_\omega(\psi_iP\psi_i).
\tag{8.8}
\]
Each diagonal chart piece transfers to a flat torus; the part away from its diagonal is smoothing and trace class. Use the square root of the coordinate density and a local orthonormal bundle frame for this Hilbert-space transfer. The principal symbol is conjugated in the frame and multiplied by \(\psi_i^2\). The local calculation above, and Proposition 7.3, therefore sum to the intrinsic density integral in (8.1). The same finite localization applies to compact kernel support on a noncompact manifold. Every value obtained is independent of \(\omega\), which completes the proof. \(\square\)

When \(n=0\), this is the ordinary trace theorem with dimension \(v\). When \(v=0\), set \(s=r^2\) in the dilation: its generator becomes twice the ordinary Euler field, and \(Q_{\mathrm{dim}}=2n\). The two factors of two cancel in (8.1), giving the ordinary dimension-\(n\) formula. A different transverse surface has no effect by (7.4); a different homogeneous length has no effect on the logarithmic coefficient by (7.3).

**Theorem 8.2 (the residue trace).** For a classical adapted operator of any complex order, put
\[
\mathcal R(P)=\frac1{Q_{\mathrm{dim}}(2\pi)^d}
\int_M\int_{S_{\rho,x}}
\operatorname{tr}a_{-Q_{\mathrm{dim}}}(x,\theta)
\,d\mu_{\rho,x}(\theta)\,dx.
\tag{8.9}
\]
A missing critical homogeneous term contributes zero. This defines a trace on the algebra of these operators on a closed manifold, and on the algebra with compact kernel support in the noncompact case. It agrees with every \(\operatorname{Tr}_\omega\) on order \(-Q_{\mathrm{dim}}\). It is an extension by the kernel's intrinsic logarithmic density, rather than an ordinary operator trace on positive orders.

**Proof.** Proposition 7.3 proves that the integral is intrinsic; smoothing operators have zero value. Agreement with the logarithmic traces is Theorem 8.1. We must prove the trace property.

First work in one coordinate chart with compact supports. Write \(\operatorname{res}(h)\) for the integral over the base and \(S_\rho\) of the trace of the degree \(-Q_{\mathrm{dim}}\) part of a symbol \(h\). Besides ordinary base integration by parts, this functional has the covariable rule
\[
\int_{S_\rho}\partial_{\xi_i}f\,d\mu_\rho=0
\quad\text{if }f\text{ has degree }-Q_{\mathrm{dim}}+w_i.
\tag{8.10}
\]
To prove it, integrate \(\partial_{\xi_i}f\) on \(1<\rho<R\). Polar integration gives \(\log R\) times the left side. The divergence theorem gives the difference of its fluxes through the two boundary surfaces. The form \(f\,i_{\partial_{\xi_i}}d\xi\) has dilation degree
\((-Q_{\mathrm{dim}}+w_i)+(Q_{\mathrm{dim}}-w_i)=0\),
so those fluxes are equal. Their difference is zero, proving (8.10). The argument is entrywise and applies to complex symbols.

A term in (5.13) can contribute only when the degrees \(p,t\) of its two homogeneous factors satisfy
\[
p+t-[\alpha]=-Q_{\mathrm{dim}}.
\tag{8.11}
\]
For such a term apply (8.10) repeatedly, then integrate by parts in \(x\). The two signs cancel:
\[
\begin{aligned}
\operatorname{res}\bigl(
(\partial_\xi^\alpha a_p)(\partial_x^\alpha b_t)\bigr)
&=(-1)^{|\alpha|}
\operatorname{res}\bigl(
a_p\,\partial_\xi^\alpha\partial_x^\alpha b_t\bigr)\\
&=\operatorname{res}\bigl(
(\partial_x^\alpha a_p)(\partial_\xi^\alpha b_t)\bigr)\\
&=\operatorname{res}\bigl(
(\partial_\xi^\alpha b_t)(\partial_x^\alpha a_p)\bigr).
\end{aligned}
\tag{8.12}
\]
At each covariable step the undifferentiated product has the degree required in (8.10). The last equality is finite-dimensional matrix-trace cyclicity. The coefficients \(i^{-|\alpha|}/\alpha!\) in the two compositions are identical. Only finitely many terms satisfy (8.11), so Theorem 5.4 and (8.12) give \(\mathcal R(PQ)=\mathcal R(QP)\) locally.

For the global statement, decompose \(P\), modulo a smoothing kernel, into finitely many pieces \(P_i\) whose output and input supports lie in the same chart. Such a decomposition is obtained by a partition near the diagonal and input cutoffs equal to one near the corresponding output supports; the omitted kernel is separated from the diagonal and is smooth. Choose a chart cutoff \(\chi_i\) equal to one near both supports of \(P_i\). In the diagonal kernel germs of \(P_iQ\) and \(QP_i\), the operator \(Q\) can be replaced by \(\chi_iQ\chi_i\): wherever either diagonal germ can be nonzero, both variables interacting with \(P_i\) lie in the region where \(\chi_i=1\). Thus
\[
\mathcal R([P_i,Q])
=\mathcal R([P_i,\chi_iQ\chi_i])=0
\]
by the local result. Smoothing errors and their products with pseudodifferential operators are smoothing. Summing proves the asserted global trace identity. Compact kernel support makes the same decomposition finite on a noncompact manifold. \(\square\)

The construction does not assert that every order-zero adapted symbol already lies in the regular operator calculus for the mixed signature operator. That separate conclusion still depends on its selfadjoint realization and on the symbol construction of \(|D|\). Theorems 8.1 and 8.2 concern operators for which the local calculus has been supplied.

## 9. A canonical trace away from integer orders

An ordinary trace integrates the kernel on the diagonal. At larger orders the kernel is singular there, but a noninteger order permits a canonical continuous remainder after its homogeneous singular terms have been removed. We first construct its value directly from the symbol.

Let \(a\) be a classical symbol of complex order \(q\notin\mathbb Z\), with homogeneous terms \(a_{q-j}\). Put
\[
M_j(a)=\int_{S_\rho}a_{q-j}(\theta)\,d\mu_\rho(\theta).
\tag{9.1}
\]
This is a matrix when the symbol is a matrix. Choose an integer \(N\geq0\) with
\(\operatorname{Re}q-N-1<-Q_{\mathrm{dim}}\).

**Theorem 9.1 (the finite-part symbol integral).** The expression
\[
\begin{aligned}
\widetilde L(a)=(2\pi)^{-d}\Bigg\{
&\int_{\rho\leq1}a(\xi)\,d\xi\\
&+\int_{\rho\geq1}
\left(a(\xi)-\sum_{j=0}^Na_{q-j}(\xi)\right)\,d\xi\\
&-\sum_{j=0}^N\frac{M_j(a)}{q-j+Q_{\mathrm{dim}}}
\Bigg\}
\end{aligned}
\tag{9.2}
\]
is independent of \(N\), agrees with the ordinary integral for integrable orders, and is holomorphic on holomorphic classical symbol families whose orders avoid the integers. Among functionals with those holomorphic-family and agreement properties, it is unique.

The uniformity meant here is explicit. A parameter family has pointwise holomorphic symbols and homogeneous terms; on compact parameter sets its differentiated remainders have uniform weighted bounds of the required decreasing orders, allowing an arbitrarily small positive order margin for parameter derivatives. This margin accommodates the factors \(\log\rho\) obtained by differentiating a complex power.

**Proof.** Both displayed integrals converge. The first is on a bounded set with a smooth symbol; the second has order less than \(-Q_{\mathrm{dim}}\). None of the denominators is zero, since \(q\notin\mathbb Z\) and \(j,Q_{\mathrm{dim}}\) are integers.

If one more term of degree \(p=q-N-1\) is subtracted, its integral on \(\rho\geq1\) is
\[
\int_1^\infty r^{p+Q_{\mathrm{dim}}-1}\,dr\,M_{N+1}(a)
=-\frac{M_{N+1}(a)}{p+Q_{\mathrm{dim}}},
\quad \operatorname{Re}p<-Q_{\mathrm{dim}}.
\tag{9.3}
\]
The change in the second integral and the new rational term in (9.2) cancel. This proves independence of \(N\). When \(\operatorname{Re}q<-Q_{\mathrm{dim}}\), all the homogeneous terms used are integrable at infinity, so (9.3) also proves agreement with the ordinary integral.

On a compact parameter set choose \(N\) uniformly large, with a strictly positive integrability margin. All differentiated remainders and their parameter difference quotients then have integrable majorants. The sphere integrals are holomorphic by their smooth uniform bounds; the rational terms are holomorphic where the order avoids integers. Differentiating under the two integrals, or applying Morera's theorem with these majorants, proves holomorphy.

For uniqueness fix \(a\) and use the holomorphic path
\[
a_s(\xi)=a(\xi)r(\xi)^{-s},
\tag{9.4}
\]
where \(r\) is (5.1). This is classical of order \(q-s\). At infinity,
\(r^{-s}=\rho^{-s}(1+\rho^{-4})^{-s/4}\);
the binomial expansion has holomorphic coefficients, decreasing degrees by four, and differentiated remainders uniform on compact sets of \(s\). Thus it is an allowed path.

For sufficiently large \(\operatorname{Re}s\), the path has integrable order, so any proposed extension equals \(\widetilde L(a_s)\). Both functions are holomorphic on the connected domain
\(\{s:q-s\notin\mathbb Z\}\), the complex plane with a discrete set removed. The identity theorem extends their equality throughout that domain, including \(s=0\). This proves uniqueness. \(\square\)

There is an equivalent description using Theorem 6.1. Let \(T_{q-j}\) be the unique homogeneous extension of \(a_{q-j}\). Then
\[
\widetilde L(a)
=\left(\mathcal F^{-1}
\left(a-\sum_{j=0}^NT_{q-j}\right)\right)(0).
\tag{9.5}
\]
The expression on the right is well defined. At large frequencies the difference is integrable; near zero it is a compactly supported distribution, whose Fourier transform is smooth. Its transform is consequently continuous near \(y=0\). A homogeneous term that has already become integrable at infinity has a Fourier transform of positive real degree, smooth away from zero, whose continuous value at zero is zero. This also proves the independence asserted in (9.5).

To check (9.5)'s value, the analytically continued integral of \(T_p\) on \(\rho\leq1\) is \(M/(p+Q_{\mathrm{dim}})\). This is first the ordinary polar integral where \(\operatorname{Re}p>-Q_{\mathrm{dim}}\), and then its continuation from (6.8). Splitting the integral in (9.5) at \(\rho=1\) gives exactly (9.2). A smooth cutoff can be used around that surface; it gives the same answer by cancellation of the two boundary pieces.

The angular functional \(a\mapsto M_j(a)\) is itself holomorphic, but it cannot be added to (9.2) while preserving agreement at integrable orders. For a prescribed \(j\), let a smooth radial cutoff be zero near zero and one for \(\rho\geq1\), and multiply it by \(\rho^{q-j}I\), with noninteger \(\operatorname{Re}q<-Q_{\mathrm{dim}}\). View it as a symbol of order \(q\), with the earlier homogeneous terms zero. Its \(j\)-th angular integral is the nonzero matrix
\(\left(\int_{S_\rho}d\mu_\rho\right)I\).
An added nonzero multiple changes its prescribed ordinary integral. Holomorphy alone is therefore insufficient for the extension property.

**Theorem 9.2 (the global canonical trace).** For a classical adapted operator \(P\) of noninteger complex order, represented in compatible foliation charts, the local values
\[
\operatorname{tr}\widetilde L(a(x,\cdot))\,dx
\tag{9.6}
\]
form an intrinsic density. Its integral, denoted \(\operatorname{TR}(P)\), agrees with the ordinary operator trace in the trace-class range. On a closed manifold, or with compact kernel support, it is holomorphic on the compatible symbol families specified in Theorem 9.1.

**Proof.** By (9.5), subtract finitely many homogeneous kernel distributions from the local kernel, sufficiently far to make the remainder continuous. Each subtracted term has degree
\[
-q+j-Q_{\mathrm{dim}}.
\tag{9.7}
\]
Its degree is never an integer, hence never zero. The continuous remainder's value at the diagonal is \(\widetilde L(a(x,\cdot))\).

Under a coordinate change use (7.8). A homogeneous kernel term of degree \(\nu\) becomes \(r^\nu\) times a smooth angular and radial function. Taylor expansion to any required finite order gives powers \(r^{\nu+k}\), with integer \(k\geq0\), and a remainder tending to zero if the expansion is sufficiently long. None of those powers has exact degree zero: \(\nu+k=0\) would force \(q\) to be an integer. Terms of real degree zero with a nonzero imaginary part are retained among the homogeneous terms being removed; they do not supply a continuous constant. The same argument applies to smooth Jacobian and bundle factors. Consequently the continuous value left after removal transforms only by the input Jacobian at the diagonal and bundle conjugation. Taking the matrix trace proves the density law in (9.6).

If the order has real part less than \(-Q_{\mathrm{dim}}\), the symbol is integrable and the localized operator is trace class, by the factorization and lattice sum in (8.2), with the strictly larger negative exponent used here. Its kernel is continuous. Its trace is the integral of the matrix trace of that kernel on the diagonal. One way to verify this last equality directly is to transfer a compact chart piece into a torus and use the finite Fourier multipliers with Fejér weights. They converge strongly to the identity, have norm at most one, and therefore their products with a trace-class operator converge in trace norm. This follows first for finite-rank operators and then by trace-norm approximation. Their finite-dimensional traces are integrals against the corresponding Fejér kernel. The approximate-identity property and uniform continuity of the kernel make those integrals converge to its diagonal integral. Chart summation proves the global equality.

The continuous diagonal kernel is
\((2\pi)^{-d}\int a(x,\xi)\,d\xi\)
in that range. Theorem 9.1 gives agreement with \(\operatorname{TR}\). For a holomorphic family, a finite chart partition gives a finite sum of (9.2)'s holomorphic local integrals and the traces of any holomorphic smoothing remainders. The uniform remainder estimates also give trace-norm holomorphy for those remainders. This proves the asserted holomorphy. \(\square\)

The notation “canonical trace” in Theorem 9.2 denotes this intrinsic finite-part integral on noninteger orders. A general trace identity requires that the relevant products have allowed noninteger orders; the theorem does not assign a canonical finite part to an integer-order pole.

**Proposition 9.3 (zeta continuation from an actual complex-power family).** Let \(W\) be a positive invertible operator on a closed triangular manifold. Assume its spectral powers \(W^{-z}\) are a globally compatible holomorphic family of classical adapted order \(-z\). Let \(P\) have integer order \(q\). Then
\[
\zeta_P(z)=\operatorname{Tr}(PW^{-z}),
\qquad \operatorname{Re}z>q+Q_{\mathrm{dim}},
\tag{9.8}
\]
has a unique meromorphic continuation to the plane, with at most simple poles in
\[
\{q+Q_{\mathrm{dim}}-j:j=0,1,2,\ldots\}.
\tag{9.9}
\]
At zero,
\[
\operatorname*{Res}_{z=0}\zeta_P(z)
=Q_{\mathrm{dim}}\mathcal R(P).
\tag{9.10}
\]
For order-zero \(P\), the continued function is jointly holomorphic in \(P\) and \(z\) away from the integers, in the classical symbol topology.

**Proof.** The product calculus makes \(PW^{-z}\) a holomorphic family of order \(q-z\), and at \(z=0\) it is exactly \(P\). In a local chart denote its homogeneous term of degree \(q-z-j\) by \(a_j(x,\xi,z)\), and its angular integral by \(M_j(x,z)\). On a compact parameter set take \(N\) sufficiently large to make the remaining symbol uniformly integrable. Formula (9.2) gives holomorphic integral terms together with
\[
\frac{(2\pi)^{-d}M_j(x,z)}
{z-(q+Q_{\mathrm{dim}}-j)}.
\tag{9.11}
\]
This formula is meromorphic even when \(q-z\) is integer. Its only possible poles on that parameter set are the simple denominators in (9.11). It agrees with the ordinary trace in the initial half-plane, by Theorem 9.2. Different local decompositions agree away from the possible poles by the identity theorem, since their values agree in that half-plane; their meromorphic continuations agree as well. Increasing the compact parameter set yields a continuation on the whole plane. This also proves uniqueness.

At zero only \(j=q+Q_{\mathrm{dim}}\) can contribute. If that index is negative there is no contribution. Otherwise its numerator at zero is the angular integral of \(P\)'s degree \(-Q_{\mathrm{dim}}\) symbol. Summing the charts gives
\((2\pi)^{-d}\int_M M_{q+Q_{\mathrm{dim}}}(x,0)\,dx\),
which is exactly \(Q_{\mathrm{dim}}\mathcal R(P)\) by (8.9).

For the joint assertion, on a compact pole-free parameter set the product and integral bounds above use finitely many continuous symbol seminorms of \(P\). The function is linear and continuous in \(P\). Cauchy's formula in \(z\), with those uniform bounds, gives locally convergent power series whose coefficients are continuous linear functionals of \(P\). This proves joint holomorphy. \(\square\)

The Fourier factor in (9.11) involves the ordinary dimension \(d=v+n\). The pole locations and the factor in (9.10) involve the homogeneous dimension \(Q_{\mathrm{dim}}=v+2n\). They have different roles.

Corollary 11.3 constructs the actual family \(\Lambda^{-z}\), where \(\Lambda=|D|+P_0\). Proposition 9.3 therefore gives the continuation and residue theorem for the mixed signature operator on a closed manifold. The finite-dimensional kernel completion affects constant trace terms as described after that corollary.

## 10. Coordinate changes, parametrices and operator domains

We now assemble the local estimates into a calculus on a triangular manifold. The integrability of \(V\) supplies the foliation charts used in the construction.

**Lemma 10.1 (reducing an amplitude).** Suppose \(c(x,y,\xi)\) has compact support in \((x,y)\), and satisfies (5.3) with arbitrary derivatives in both base variables and order \(m\). The operator with kernel
\[
(2\pi)^{-d}\int e^{i(x-y)\cdot\xi}c(x,y,\xi)\,d\xi
\tag{10.1}
\]
has a left symbol of order \(m\), with expansion
\[
a(x,\xi)\sim
\sum_\alpha\frac{i^{-|\alpha|}}{\alpha!}
\left.\partial_\xi^\alpha\partial_y^\alpha
c(x,y,\xi)\right|_{y=x}.
\tag{10.2}
\]
The remainder after \([\alpha]<N\) satisfies every estimate of order \(m-N\).

**Proof.** Applying the operator to a plane wave, whose restriction to the compact input support is a valid smooth test input, gives its exact left symbol:
\[
a(x,\xi)=(2\pi)^{-d}\iint
e^{-it\cdot\eta}c(x,x+t,\xi+\eta)\,dt\,d\eta.
\tag{10.3}
\]
Integrate in \(t\) first. Repeated integration by parts in that compactly supported variable bounds the resulting Fourier transform by
\(C_Mr(\xi+\eta)^m(1+|\eta|)^{-M}\).
After each specified \(x,\xi\)-derivative, its order changes by precisely the covariable weight. Comparison (5.16) makes the remaining \(\eta\)-integral converge and proves the symbol bounds.

Taylor expand the last covariable argument through ordinary degree \(N-1\). The integral of its term \(\eta^\alpha/\alpha!\) is
\(i^{-|\alpha|}\partial_y^\alpha/\alpha!\) on the diagonal, giving (10.2). For the integral remainder, first integrate by parts in \(t\). Its compact support is unchanged, while its covariable derivative of ordinary length \(N\) lowers weighted order by at least \(N\). Estimate (5.16), uniformly along \(\xi+s\eta\), supplies exactly the differentiated remainder bound in the proof of Theorem 5.4. Terms of weighted degree at least \(N\) among the finite Taylor terms also have order at most \(m-N\).

To justify (10.3) and the kernel identity, first put compact frequency cutoffs in both integrals. Fourier inversion gives the identity for the resulting distributions. The integrable bounds just proved identify their limits and every derivative of the symbol. This proves the assertion for the original oscillatory kernel. \(\square\)

**Theorem 10.2 (transport through foliation charts).** A smooth change of foliation coordinates preserves \(S_w^m\) and the classical adapted operators. The principal symbol is transported by the induced graded cotangent map on \(V^*\oplus N^*\), with bundle conjugation. It is consequently independent of a complement to \(V\).

**Proof.** Let \(\varphi(x)=(f(x_V,x_N),g(x_N))\). Near the diagonal write
\[
\varphi(x)-\varphi(y)=F(x,y)(x-y),\qquad
F(x,y)=\int_0^1D\varphi(y+s(x-y))\,ds.
\tag{10.4}
\]
After making the diagonal neighborhood smaller, \(F\) is invertible. It is block upper triangular, and its transverse diagonal block depends only on \(x_N,y_N\).

Pull back a kernel in the \(\varphi\)-coordinates. The input density contributes \(|\det D\varphi(y)|\). Change frequency from \(\eta\) to \(\xi=F(x,y)^t\eta\). The resulting amplitude, before smooth bundle factors, is
\[
c(x,y,\xi)=
a\bigl(\varphi(x),F(x,y)^{-t}\xi\bigr)
\frac{|\det D\varphi(y)|}{|\det F(x,y)|}.
\tag{10.5}
\]
The phase is now \(e^{i(x-y)\cdot\xi}\).

Set \(L=F^{-t}\). Its action on covectors has the form
\[
L\xi=(A\xi_V,C\xi_V+B\xi_N),
\tag{10.6}
\]
with \(A,B\) invertible and all coefficients bounded on the compact chart piece. Both \(L\) and its inverse preserve this form. The elementary power inequalities used in (5.9) therefore give \(r(L\xi)\asymp r(\xi)\), uniformly there.

The chain rule proves the full amplitude estimates. A vertical covariable derivative produces either an \(A\)-multiple of a vertical derivative, lowering degree by one, or a \(C\)-multiple of a transverse derivative, lowering it by two. A transverse covariable derivative produces only transverse derivatives, lowering degree by two. Base derivatives of \(L\) produce either \(\xi_V\partial_{\eta_V}\), \(\xi_V\partial_{\eta_N}\), or \(\xi_N\partial_{\eta_N}\). Their net degree changes are zero, minus one, and zero. No term \(\xi_N\partial_{\eta_V}\) occurs. Repeated product and chain rules thus preserve every required derivative budget. The smooth determinant and bundle factors have degree zero. Lemma 10.1 now proves membership in the local operator class.

For classicality, split \(L=L_0+\) its shear, where
\(L_0\xi=(A\xi_V,B\xi_N)\).
For a homogeneous term expand in the transverse shift \(C\xi_V\):
\[
a_p(L\xi)\sim
\sum_\alpha\frac{(C\xi_V)^\alpha}{\alpha!}
(\partial_{\eta_N}^\alpha a_p)(L_0\xi).
\tag{10.7}
\]
The term indexed by \(\alpha\) has degree \(p-|\alpha|\): its derivative loses \(2|\alpha|\), and its polynomial gains \(|\alpha|\). The Taylor remainder has order \(p-N\) after ordinary length \(N\). Indeed all intermediate triangular maps \(L_0+s(L-L_0)\) are uniformly invertible, and the preceding chain-rule estimates apply to the integral remainder and every derivative. Expanding all the original homogeneous terms, and then applying (10.2), gives a classical expansion in descending integer degrees.

On the diagonal the determinant quotient in (10.5) equals one. The leading term in (10.7) uses only \(L_0\), and every correction from (10.2) has lower order. Thus the principal symbol transforms by the graded cotangent map and the bundle conjugation at \(x\). That graded map is exactly the natural map on \(V^*\oplus N^*\), proving the final statements. \(\square\)

The same proof applies to holomorphic families: its coefficients are holomorphic, and its differentiated remainder estimates are uniform on compact parameter sets. Frequency logarithms from parameter differentiation can be bounded by an arbitrarily small positive order margin.

An adjoint also belongs to the calculus. In coordinates with Lebesgue density its amplitude is \(a(y,\xi)^*\); Lemma 10.1 gives its symbol. A smooth positive density and a bundle metric merely add the smooth factors in (10.5). Its principal symbol is the adjoint of the original principal symbol.

**Lemma 10.3 (asymptotic summation).** Given symbols \(a_j\) of orders \(m-j\), all supported in a fixed compact base set, there is a symbol \(a\) with
\[
a-\sum_{j<N}a_j\in S_w^{m-N}
\quad\text{for every }N.
\tag{10.8}
\]
The result holds for locally uniform holomorphic families and patches over a finite chart cover.

**Proof.** Choose a smooth frequency cutoff which is zero for \(\rho\leq1\) and one for \(\rho\geq2\). Multiply \(a_j\) by its rescaling with radius \(R_j\), and sum. Choose \(R_j\to\infty\) sufficiently fast that the \(j\)-th cut-off term has norm at most \(2^{-j}\) in the first \(j\) symbol seminorms of order \(m-j/2\). This is possible because it has order \(m-j\): increasing \(R_j\) gains a factor \(R_j^{-j/2}\); covariable derivatives of the cutoff obey the same weighted estimates. Enumerate the derivative seminorms so that every fixed one eventually appears.

The resulting series converges in every seminorm needed for order \(m\). For (10.8), the finitely many terms with \(N\leq j<2N\) have order at most \(m-N\); the subsequent tail converges in that order by the same bounds. The cutoff changes each fixed \(a_j\) only on a bounded frequency set, hence by a smoothing symbol. This proves the asymptotic assertion. For holomorphic families impose the \(j\)-th choice uniformly on the first \(j\) compact parameter sets in an exhaustion. The normally convergent sums are holomorphic, and the argument applies to every compact parameter set. A finite base partition patches the construction. \(\square\)

We call an operator of positive weighted order \(m\) elliptic when its principal matrix symbol is invertible away from the zero graded covector.

**Theorem 10.4 (elliptic parametrix and regularity).** On a closed triangular manifold, every classical elliptic operator \(T\) of positive order \(m\) has a two-sided parametrix \(B\) of order \(-m\):
\[
BT=I-R,\qquad TB=I-S,
\tag{10.9}
\]
with smooth kernels \(R,S\). For every real \(s\),
\[
Tu\in H_w^s,\quad u\in\mathcal D'(M,E)
\quad\Longrightarrow\quad u\in H_w^{s+m}.
\tag{10.10}
\]
The spaces \(H_w^s\) are defined by finite chart localization of (5.6), with equivalent norms for different choices.

**Proof.** The inverse of the principal symbol is homogeneous of degree \(-m\). Choose local quantizations, cut them off near zero, and patch using Theorem 10.2. This gives \(B_0\) with \(TB_0=I-S_1\), where \(S_1\) has order at most minus one. The finite correction
\[
B_0(I+S_1+\cdots+S_1^{N-1})
\]
has right error \(S_1^N\), of order at most \(-N\). Lemma 10.3 sums these corrections to a right parametrix. Construct a left parametrix in the same way. If \(C\) is that left parametrix, then
\[
C-B=C(I-TB)+(CT-I)B
\]
shows that \(C-B\) is smoothing. Thus the same \(B\) is two-sided modulo smooth kernels. A symbol of all negative orders has a smooth kernel: every kernel derivative is an absolutely convergent frequency integral after taking its order sufficiently low; the off-diagonal integrations by parts give the same assertion for properly localized kernels.

For equivalence of Sobolev norms it suffices to consider one coordinate transfer with compact cutoffs. It is bounded on \(L^2\), using its smooth density and bundle factors. Conjugating the multiplier \(r(D)^s\) by it gives an adapted operator of order \(s\), by Theorem 10.2. Theorem 5.1 then bounds the transferred \(H_w^s\) norm by the original one. Apply the inverse coordinate transfer for the reverse estimate. Smooth partitions preserve these norms by Theorem 5.4.

When the local norm is evaluated outside the diagonal chart neighborhood, its kernel is smooth and rapidly decreasing in the Euclidean output variable. Repeated frequency integration by parts proves that fact and all its derivatives. Such pieces are bounded between any of the localized Sobolev spaces and do not affect the norm comparison.

A distribution on a compact manifold belongs to \(H_w^{-k}\) for some \(k\): localized Fourier transforms have polynomial growth, and sufficiently large negative weighted powers dominate it. From (10.9),
\(u=BTu+Ru\).
The first term is in \(H_w^{s+m}\) by Theorem 5.1; the second is smooth. This proves (10.10). The same equality gives the estimate
\[
\|u\|_{H_w^{s+m}}
\leq C_{s,L}\bigl(\|Tu\|_{H_w^s}+\|u\|_{H_w^{-L}}\bigr)
\tag{10.11}
\]
for any fixed \(L\), wherever the right side is defined. \(\square\)

**Corollary 10.5 (the closed mixed-signature domain).** On a closed triangular manifold the formal operator \(Q\) in (3.6) has a selfadjoint realization with
\[
\operatorname{Dom}Q=H_w^2(M,E).
\tag{10.12}
\]
Smooth sections are a core. Its resolvent is compact, and every eigenvector is smooth. The positive operator
\[
A=Q^2+I
\tag{10.13}
\]
has domain \(H_w^4\), and
\(\operatorname{Dom}A^k=H_w^{4k}\) for integers \(k\geq0\), with equivalent graph and Sobolev norms.

**Proof.** The principal symbol of \(Q\) is the elliptic matrix (4.4). Estimate (10.11) with \(s=0,m=2,L=0\) makes the graph norm of \(Q\) on smooth sections equivalent to the \(H_w^2\) norm. Smooth sections are dense in that Sobolev space by local Fourier truncation and a partition. Hence the closure of the formal operator has domain \(H_w^2\).

An element of the adjoint domain is a vector \(u\in L^2\) for which the distribution \(Qu\) is in \(L^2\), by formal selfadjointness and the definition of a distributional derivative. Theorem 10.4 makes it an element of \(H_w^2\). Conversely every such vector is in the adjoint domain, since the differential operator maps \(H_w^2\) continuously to \(L^2\) and the smooth-section integration identity extends by approximation. Thus the closed domain and the adjoint domain are equal.

The embedding \(H_w^{s+a}\to H_w^s\), \(a>0\), is compact on a closed manifold. In each torus chart its frequency tail has norm at most \(R^{-a}\); its bounded-frequency part is finite rank. A finite partition and the norm equivalence above give a norm limit of finite-rank approximations globally. The resolvent of \(Q\) maps \(L^2\) boundedly into \(H_w^2\) by (10.11), so it is compact on \(L^2\). The spectral theorem for compact resolvent gives finite-dimensional eigenspaces and a complete eigenbasis. Applying (10.10) repeatedly to \(Qu=\lambda u\) makes each eigenvector smooth.

For \(A=Q^2+I\), its principal symbol is \(\rho_x^4I\), by (4.5). Its spectral domain is the domain of \(Q^2\). If \(u\) lies in that domain then \(Au\in L^2\), so elliptic regularity gives \(u\in H_w^4\). Conversely \(Q:H_w^4\to H_w^2\), so every \(H_w^4\) vector lies in the domain of \(Q^2\). Induction applies the same reasoning to \(A^k\), an elliptic differential operator of order \(4k\), and proves its asserted domain and norm equivalence. Since \(A\geq I\), \(\|A^ku\|_2\) already controls \(\|u\|_2\). \(\square\)

The closed-manifold argument uses no choice of a boundary condition at infinity. On a noncompact manifold, (10.10) remains a local statement with compact chart cutoffs; a selfadjoint realization and estimates for its global spectral functions require separate hypotheses.

### Coordinate transport for the classical trace

The referenced AN03-GEO-001–004 calculus contains more general kernel and wavefront assertions. The classical trace uses only explicit symbol kernels, their leading coordinate change, and finite compact localization. The following adapter verifies that part directly; it uses no theorem representing arbitrary maps by kernels.

**Lemma 10.6.** For explicit classical symbol kernels, the principal symbol transforms by the cotangent coordinate map and bundle conjugation. Changing a symbol without changing its principal part loses one order. A smooth compactly supported kernel has arbitrarily negative order. Finite density and bundle transfers preserve these statements.

**Proof.** Away from the diagonal, repeated integration by parts in the phase of
\((2\pi)^{-d}\int e^{i(x-y)\cdot\xi}a(x,\xi)\,d\xi\)
makes every derivative integrable, so that kernel is smooth there. The same argument holds with compact coordinate cutoffs.

Let \(z=\kappa(x)\), \(w=\kappa(y)\) be a smooth change of coordinates. Near the diagonal write
\[
\kappa(x)-\kappa(y)=L(x,y)(x-y),\qquad
L(x,y)=\int_0^1\kappa'(y+t(x-y))\,dt.
\tag{10.13}
\]
The matrix is invertible on a sufficiently small diagonal neighborhood, and \(L(x,x)=\kappa'(x)\). Change the frequency to \(\xi=L(x,y)^T\eta\). For operators acting on coordinate functions the transformed amplitude is
\[
c(z,w,\eta)
=a(x,L(x,y)^T\eta)
  \frac{|\det L(x,y)|}{|\det\kappa'(y)|}.
\tag{10.14}
\]
A finite cover handles a compact diagonal support. At \(z=w\) the determinant ratio is one. On each compact set, the chain rule shows that this is a classical amplitude of order \(m\): a derivative in a base variable introduces a factor \(O(|\eta|)\) together with a frequency derivative of \(a\), so it costs no order; each frequency derivative lowers order by one.

Taylor expansion in \(w\), followed by integration by parts in \(\eta\), converts this amplitude to a left symbol,
\[
b(z,\eta)\sim
\left.\sum_\alpha\frac1{\alpha!}
\partial_\eta^\alpha D_w^\alpha c(z,w,\eta)\right|_{w=z}.
\tag{10.15}
\]
After retaining terms with \(|\alpha|<N\), the remainder has order \(m-N\), with every differentiated estimate. The exact amplitude-reduction statement is Lemma 10.1 of the fourth lesson, using the comparison estimate (5.16) and the Taylor remainder bounds in its Theorem 5.4, with every direction assigned weight one. To recall its mechanism, Fourier transform the compactly supported difference variable of \(c(z,z+t,\eta+\theta)\). Integration by parts in \(t\) gives arbitrary decay in \(\theta\). Taylor expansion in the last frequency variable gives the diagonal terms in (10.15); the \(N\) frequency derivatives in its integral remainder lower order by \(N\). The estimate \(\langle\eta+s\theta\rangle^h\leq C_h\langle\eta\rangle^h\langle\theta\rangle^{|h|}\), uniformly for \(0\leq s\leq1\), makes that remainder integrable after sufficiently many integrations by parts, including every prescribed base and frequency derivative. Frequency cutoffs and the resulting integrable majorants justify passage to the oscillatory kernel. This uses the Fourier foundations above, not the coordinate-transfer conclusion being proved here.
Thus the leading term of (10.15) is
\(a_m(x,\kappa'(x)^T\eta)\), and every other term has lower degree. This proves the stated coordinate rule and order loss.

Multiplication on the left and right by smooth bundle matrices has leading term their pointwise product with \(a_m\), by the same Taylor calculation. A bundle frame change therefore conjugates the principal endomorphism. Transferring \(L^2\) densities is multiplication by their smooth positive square roots, whose two leading factors cancel under conjugation. These assertions include rectangular bundle maps where required.

For a smooth kernel supported in a compact coordinate product, its left symbol is the Fourier transform in \(x-y\) of that kernel. Every derivative is rapidly decreasing in frequency, by integration by parts on the compact support, so its order is arbitrarily negative. Extending a localized kernel into a torus cube and summing its periodic translates introduces only smooth off-diagonal terms near the chosen diagonal; its principal symbol is unchanged. Finite partitions and bundle trivializations then give exactly the transfers used in Theorem 7.1 of the first lesson. \(\square\)

These lemmas provide the precise analytic entry contracts of the operator and symbol proofs. They do not impose a spectral basis on the noncompact application, or a meromorphic continuation on any coefficient.

## 11. Complex powers from a parameter-dependent inverse

The spectral theorem defines complex powers of a positive operator. To use them in the symbol calculus, we identify those spectral powers with operators having controlled symbols. The argument below uses the positive real resolvent parameter; the scalar Mellin integral supplies the complex exponent.

**Theorem 11.1 (powers of \(Q^2+I\)).** On a closed triangular manifold let \(A=Q^2+I\), with the realization in Corollary 10.5. Its spectral powers form a holomorphic family of classical adapted operators:
\[
A^{-z}\in\Psi_w^{-4z},\qquad
\sigma_{-4z}(A^{-z})(x,\xi)=\rho_x(\xi)^{-4z}I.
\tag{11.1}
\]
Holomorphy here has the uniform symbol-family meaning in Theorem 9.1, and gives holomorphic operators between sufficiently separated Sobolev spaces on each compact parameter set.

**Proof.** For \(t\geq0\) use the joint frequency length
\[
R_t(\xi)=\bigl(1+|\xi_V|^4+|\xi_N|^2+t\bigr)^{1/4}.
\tag{11.2}
\]
A parameter symbol of order \(h\) has bounds
\[
\|\partial_x^\alpha\partial_\xi^\beta\partial_t^\ell b\|
\leq C_{\alpha,\beta,\ell}
R_t^{h-[\beta]-4\ell}.
\tag{11.3}
\]
The symbol of \(A+t\) has leading part \(p_4(x,\xi)+t\), where \(p_4=\rho_x^4I\); its remaining differential symbols have weighted degrees at most three. On compact base sets the scalar \(p_4+t\) is bounded below by a positive multiple of \(\rho^4+t\). Its inverse, cut off near the joint origin \((\xi,t)=(0,0)\), satisfies (11.3) with \(h=-4\).

The composition proof in Theorem 5.4 applies uniformly with \(r\) replaced by \(R_t\): the quotient comparison (5.16) remains true with \(t\) fixed. Parameter differentiation lowers degree by four and commutes with the integral. Patch the leading inverses and perform the successive corrections of Theorem 10.4. Lemma 10.3 also applies to the joint length, imposing its cutoff choices on the \(\xi,t\) derivative seminorms. This constructs \(B(t)\) with
\[
(A+t)B(t)=I-E(t),
\tag{11.4}
\]
where \(E(t)\) satisfies (11.3) with every negative order. The symbol of \(B(t)\) has homogeneous terms \(b_{-4-j}\) under
\[
(\xi,t)\longmapsto(\delta_\lambda\xi,\lambda^4t).
\tag{11.5}
\]
They have degree \(-4-j\), and \(b_{-4}=(p_4+t)^{-1}\). The recursive correction uses only products, covariable derivatives and division by \(p_4+t\). Since the symbols of \(A\) are polynomials in \(\xi\), each term is smooth on the closed half-space \(t\geq0\) away from the joint origin. Its differentiated estimates follow by homogeneity on the compact joint unit surface. Cutoffs at the joint origin and the off-diagonal chart pieces have the required uniform smoothing estimates; frequency integration by parts proves this for the latter.

We must compare this asymptotic inverse with the actual resolvent. A parameter symbol bounded by \(R_t^{-N}\) satisfies, for \(h\geq0\) and \(N>h\),
\[
\|E(t)\|_{H_w^s\to H_w^{s+h}}
\leq C_{s,h,N}(1+t)^{-(N-h)/4}.
\tag{11.6}
\]
In the Fourier-kernel proof of Theorem 5.1 the extra Sobolev weight is bounded by \(r(\xi)^h\), times a harmless power of the frequency difference. Use
\(r^hR_t^{-N}\leq R_t^{h-N}\leq(1+t)^{-(N-h)/4}\),
and take sufficiently many base derivatives for the Schur bound. This proves (11.6), also for every required localized seminorm.

For integer \(k\), the graph norm equivalences in Corollary 10.5 identify \(H_w^{4k}\) with the scale defined by \(A^k\). Negative integers follow by duality. The resolvent commutes with those spectral powers, so
\[
\|(A+t)^{-1}\|_{H_w^{4k}\to H_w^{4k}}
\leq C_k(1+t)^{-1}.
\tag{11.7}
\]
From (11.4),
\[
(A+t)^{-1}-B(t)=(A+t)^{-1}E(t).
\tag{11.8}
\]
For any \(k\geq0\), apply (11.6) from \(H_w^{-4k}\) to \(H_w^{4k}\), then (11.7). Since \(N\) is arbitrary, (11.8) is smoothing with norms decreasing faster than any prescribed power of \(1+t\). Bounds between all these Sobolev pairs imply bounds for every smooth-kernel seminorm: in local Fourier bases they give arbitrarily rapid decay in both frequency indices; Sobolev embedding then controls each kernel derivative.

For \(0<\operatorname{Re}z<1\), the spectral theorem gives the operator-norm integral
\[
A^{-z}=\frac{\sin\pi z}{\pi}
\int_0^\infty t^{-z}(A+t)^{-1}\,dt.
\tag{11.9}
\]
For completeness, the scalar identity behind it is
\[
\int_0^\infty\frac{s^{-z}}{1+s}\,ds
=\frac{\pi}{\sin\pi z}.
\tag{11.10}
\]
Integrate \(\zeta^{-z}/(1+\zeta)\), with \(0<\arg\zeta<2\pi\), around a keyhole contour. The circular contributions tend to zero in the stated strip. The two positive-ray contributions differ by the factor \(1-e^{-2\pi iz}\); the residue at \(\zeta=-1\) is \(e^{-i\pi z}\). Hence their integral is \(2\pi i e^{-i\pi z}/(1-e^{-2\pi iz})\), which is (11.10). Scaling \(t\) by a positive spectral value proves (11.9). Norm convergence follows from \(\|(A+t)^{-1}\|\leq(1+t)^{-1}\).

Substitute (11.8) in (11.9). Its smoothing correction is holomorphic with values in the smooth-kernel space: near zero it is bounded and \(t^{-\operatorname{Re}z}\) is integrable; at infinity it decreases faster than every power, also after multiplying by any powers of \(\log t\).

Integrate the symbol of \(B(t)\) term by term asymptotically. For large \(\xi\), the coefficient is
\[
a_{-4z-j}(x,\xi)=\frac{\sin\pi z}{\pi}
\int_0^\infty t^{-z}b_{-4-j}(x,\xi,t)\,dt.
\tag{11.11}
\]
It converges in the strip: at \(t=0\) the fixed nonzero \(\xi\) keeps the denominator bounded away from zero, and at infinity the joint estimate gives decay at least \(t^{-1-j/4}\). Change variables \(t=\lambda^4s\) to see its degree \(-4z-j\).

The differentiated remainder of joint order \(-4-N\) integrates to a symbol of order \(-4\operatorname{Re}z-N\). Indeed, at high frequency its majorant is a constant times
\[
\int_0^\infty t^{-\operatorname{Re}z}
(\rho^4+t)^{-(4+N+[\beta])/4}\,dt
=C_z\rho^{-4\operatorname{Re}z-N-[\beta]}.
\tag{11.12}
\]
The constants are locally uniform in the strip. Parameter derivatives add logarithms and are controlled by the permitted arbitrarily small order margin. Low frequencies are smooth because the joint-origin cutoff was made before integration. This proves the full classical expansion and holomorphy. Formula (11.10) applied to \(b_{-4}\) gives its principal term \(\rho_x^{-4z}I\).

Finally, for any \(z\) in a small complex neighborhood choose integers \(k\geq0,M\geq1\) so that \(0<\operatorname{Re}(z+k)/M<1\). On smooth spectral vectors,
\[
A^{-z}=\bigl(A^{-(z+k)/M}\bigr)^M A^k.
\tag{11.13}
\]
The right side is a holomorphic classical family by the product calculus, of degree \(-4z\), with the asserted principal symbol. The equality is the spectral power identity. Smooth eigenvectors form a core in every integral Sobolev scale, so the identities determine the same operators on their appropriate domains and on distributions. They agree on overlapping neighborhoods. This proves (11.1) on the whole plane. \(\square\)

**Proposition 11.2 (retaining the harmonic space).** Let \(P_0\) be the orthogonal projection onto \(\ker Q\), and set
\[
A_0=Q^2+P_0.
\tag{11.14}
\]
This is positive and invertible. Its powers \(A_0^{-z}\) are holomorphic classical adapted operators of degree \(-4z\), with the same principal symbols as in (11.1).

**Proof.** The kernel is finite dimensional and consists of smooth vectors by Corollary 10.5. Thus \(P_0\) has a smooth kernel. Put
\[
B'=(I-P_0)A^{-1}.
\]
The nonzero spectrum of \(Q\) is separated from zero, so \(\|B'\|<1\). Moreover \(B'\) has order minus four and commutes with \(A\). Spectrally,
\[
A_0=A(I-B'),\qquad
A_0^{-z}=A^{-z}(I-B')^{-z}.
\tag{11.15}
\]
The last factor has the norm-convergent expansion
\[
(I-B')^{-z}=\sum_{j=0}^\infty
\frac{z(z+1)\cdots(z+j-1)}{j!}(B')^j,
\tag{11.16}
\]
with constant term \(I\). On compact \(z\)-sets the coefficients grow at most polynomially in \(j\), while \(\|(B')^j\|\) decreases geometrically. The same norm convergence holds on each \(H_w^{4k}\), since the factors commute with \(A\) and the graph norms are equivalent.

The remainder after \(N\) terms is \((B')^Nh_{N,z}(B')\), where \(h_{N,z}\) is uniformly bounded on the spectral interval of \(B'\) for \(z\) in a compact set. It consequently gains \(4N\) Sobolev orders on the integral scales just used. Lemma 10.3 sums the corresponding classical operator expansion. The difference between its sum and the actual operator in (11.16) is smoothing: compare both with the same finite sum, then choose \(N\) arbitrarily large to control any pair of Sobolev orders. Normal convergence and the holomorphic summation version give holomorphy of that smoothing difference as well. The classical sum has principal symbol \(I\). Multiplication by \(A^{-z}\) in (11.15) proves the claim. \(\square\)

**Corollary 11.3 (the first-order mixed signature operator).** Define spectrally
\[
D=\operatorname{sign}(Q)|Q|^{1/2},
\quad \operatorname{sign}(0)=0,
\qquad \Lambda=|D|+P_0.
\tag{11.17}
\]
Then
\[
D=QA_0^{-1/4},\qquad
|D|=A_0^{1/4}-P_0,\qquad
\Lambda=A_0^{1/4}.
\tag{11.18}
\]
The operator \(D\) is selfadjoint with domain \(H_w^1\), has compact resolvent, and satisfies \(D|D|=Q\). Both \(D\) and \(|D|\) have weighted order one, with principal symbols
\[
\sigma_1(D)=q_2/\rho,\qquad
\sigma_1(|D|)=\rho I.
\tag{11.19}
\]
In particular, \(\Lambda^{-z}\) is the actual holomorphic family of order \(-z\) required in Proposition 9.3.

**Proof.** On a \(Q\)-eigenvector of eigenvalue \(\lambda\neq0\), both sides of (11.18) have the scalar values indicated by (11.17); on its kernel, \(A_0=I\) and \(P_0=I\), so the values are respectively zero, zero and one. This proves the identities and \(D|D|=Q\), with their spectral domains. The spectral function in (11.17) is real, hence defines a selfadjoint operator.

Proposition 11.2 and the product calculus give the operator orders and (11.19). Their elliptic order-one symbols and Theorem 10.4 identify the maximal \(L^2\) domain with \(H_w^1\). Finite sums of the smooth eigenvectors are a core for the spectral operator, and smooth sections complete in that graph norm to \(H_w^1\), so this is also its stated domain. Negative-order localization makes \(\Lambda^{-1}\) compact. The resolvent of \(D\) is then compact by the graph estimate and the compact embedding \(H_w^1\to L^2\). The final assertion is \(\Lambda^{-z}=A_0^{-z/4}\). \(\square\)

For a generalized inverse which vanishes on the kernel, the zeta function differs from \(\operatorname{Tr}(P\Lambda^{-z})\) by the entire constant \(\operatorname{Tr}(PP_0)\). Every residue in Proposition 9.3 is therefore unchanged. The constant term can change; harmonic vectors must remain explicit in an even index pairing.

## 12. Regular spectral triples and the noncompact local statement

We use the derivation \(\delta(T)=[|D|,T]\), with the closed-commutator meaning in the second lesson. The natural action of a triangular isometry \(\varphi\) on forms is
\(U_\varphi=(\varphi^{-1})^*\).
It is unitary because it preserves the two bundle metrics and their product density. The convention gives
\[
U_\varphi U_\psi=U_{\varphi\psi},\qquad
U_\varphi fU_\varphi^{-1}=f\circ\varphi^{-1}.
\tag{12.1}
\]
The crossed product consists of finite sums of \(fU_\varphi\), with multiplication determined by (12.1).

**Theorem 12.1 (the closed mixed-signature triple).** On a closed triangular manifold the operator \(D\) in (11.17) gives a regular spectral triple for \(C^\infty(M)\rtimes\Gamma\), where \(\Gamma\) is any group of triangular isometries. More explicitly:

1. Every \([D,fU_\varphi]\) is bounded, and both \(fU_\varphi\) and \([D,fU_\varphi]\) belong to all domains of \(\delta\).
2. The resolvent of \(D\) is compact. Moreover
   \(\mu_j(\Lambda^{-1})=O((j+1)^{-1/Q_{\mathrm{dim}}})\).
3. Changing the complement used to construct \(d_H\) changes \(D\) and \(|D|\) by bounded operators.

**Proof.** An order-zero adapted operator preserves \(H_w^1=\operatorname{Dom}|D|\). Its commutator with \(|D|\) has order zero, by the scalar principal symbol in (11.19) and Theorem 5.4. The bounded symbol commutator is therefore the actual closed commutator on the domain. Repeating this argument proves membership in every domain of \(\delta\).

Multiplication by \(f\) has order zero. The degree-one symbol commutator of \(D\) with it vanishes because \(f\) is scalar. All differentiated product terms lose at least one degree, so \([D,f]\) has order zero. Both it and \(f\) are thus regular.

The coordinate and bundle transformations of a triangular isometry preserve \(q_2\) and \(\rho\). Theorem 10.2 and the spectral definition show that \(U_\varphi DU_\varphi^{-1}\) and \(U_\varphi|D|U_\varphi^{-1}\) have the same principal symbols as \(D,|D|\). Their differences have order zero. Put
\[
S=(|D|U_\varphi-U_\varphi|D|)U_\varphi^{-1},
\qquad
T=(DU_\varphi-U_\varphi D)U_\varphi^{-1}.
\]
They are regular order-zero operators. The identity \(\delta(U_\varphi)=SU_\varphi\) and the Leibniz rule give inductively
\[
\delta^k(U_\varphi)=S_kU_\varphi,\qquad
S_{k+1}=\delta(S_k)+S_kS.
\tag{12.2}
\]
All \(S_k\) have order zero. Also \([D,U_\varphi]=TU_\varphi\) is regular by the same induction. Apply the Leibniz rule to
\([D,fU_\varphi]=[D,f]U_\varphi+f[D,U_\varphi]\)
to prove the first assertion.

Compact resolvent is Corollary 11.3. The operator \(\Lambda^{-Q_{\mathrm{dim}}}\) has critical negative order, so Theorem 5.3 gives singular values \(O((j+1)^{-1})\). Positivity and spectral calculus take their \(Q_{\mathrm{dim}}\)-th roots and give the claimed bound for \(\Lambda^{-1}\).

Finally, changing the complement leaves \(q_2\) unchanged by Proposition 4.1. Thus it also leaves the two symbols in (11.19) unchanged. The differences of the resulting operators have order zero and are bounded. \(\square\)

Applying Proposition 9.3 with the actual family \(\Lambda^{-z}\) now gives its full continuation and residue conclusions for classical adapted \(P\) on the closed manifold. For a term involving \(U_\varphi\), continuation also involves the fixed-set geometry of \(\varphi\); it is not inferred from the ordinary pseudodifferential statement alone.

Here is the local version with no compactness assumption on \(M\). A selfadjoint realization is part of its hypotheses; formal selfadjointness on compactly supported sections alone does not specify one.

**Lemma 12.2 (localized spectral powers).** Let \(M\) be a possibly noncompact triangular manifold. Choose a selfadjoint realization of its formal \(Q\) which extends \(Q\) on \(C_c^\infty(M,E)\), and put \(A=Q^2+I\). For every compactly supported smooth multiplier \(\chi\) and every complex \(z\),
\[
A^{-z}\chi=P_\chi(z)+S_\chi(z).
\tag{12.3}
\]
Here \(P_\chi(z)\) has compact kernel support and is classical adapted of order \(-4z\). The remainder is smoothing in the spectral scale of \(A\): for all integers \(k\geq0\) it is bounded from the completion in \(\|A^{-k}u\|_2\) to \(\operatorname{Dom}A^k\). All these bounds and the symbol-family estimates are locally uniform and holomorphic in \(z\).

**Proof.** Take a compact neighborhood of the support of \(\chi\), and construct the parameter inverse there by (11.2)-(11.5). Choose output and input cutoffs with the output cutoff equal to one near the input support. The differential operator \(A+t\) applied to this localized inverse gives
\[
(A+t)B_\chi(t)=\chi+E_\chi(t).
\tag{12.4}
\]
The error has compact kernel support and is smoothing, with all smooth-kernel seminorms decreasing faster than any power of \(1+t\). The commutator with the output cutoff is separated from the input support; the frequency integrations by parts in Theorem 11.1 give exactly those estimates. The interior error is the asymptotic error already constructed there. This argument uses only coefficients in the chosen compact neighborhood.

Every smooth compactly supported section belongs to \(\operatorname{Dom}A^k\): \(Q\) and all its differential iterates preserve that test space, and the realization agrees with them there. For a smooth compact kernel \(E\), apply the differential \(A^k\) in each variable. The resulting kernel is still smooth and compactly supported, and defines a bounded Hilbert–Schmidt operator. Selfadjointness, pairing against these compactly supported test sections, then shows that \(A^kEA^k\) is bounded. Thus \(E\) is smoothing in the stated spectral scale. No condition at infinity enters those integrations by parts.

In that scale \((A+t)^{-1}\) has norm at most \((1+t)^{-1}\), since it commutes with \(A\) and \(A\geq I\). Equation (12.4) therefore gives
\[
(A+t)^{-1}\chi
=B_\chi(t)-(A+t)^{-1}E_\chi(t).
\tag{12.5}
\]
The second term is spectrally smoothing with rapid parameter decrease. The Mellin integral (11.9), its symbol calculation (11.11)-(11.12), and the same holomorphic estimates prove (12.3) first for \(0<\operatorname{Re}z<1\).

We record the scale comparisons needed to extend it. Let \(H_A^s\) be the spectral scale defined by \(A^s\), with completions for negative \(s\). Local elliptic parametrices give
\[
\|\chi u\|_{H_w^{4k}}\leq C_{\chi,k}\|u\|_{H_A^k}
\quad(k\geq0).
\tag{12.6}
\]
Indeed a left local parametrix of the differential \(A^k\) expresses \(\chi u\) as an order-\(-4k\) compactly supported operator applied to \(A^ku\), plus a smooth compact kernel applied to \(u\). Conversely, a compactly supported \(H_w^{4k}\) vector belongs to \(\operatorname{Dom}A^k\), by approximation with compact test sections and the local differential estimate. Negative-index comparisons follow by duality.

For \(0<s<1\), the adjoint form of (12.3) in the initial strip gives \(\chi A^{-s}:L^2\to H_w^{4s}\), using (12.6) to control the spectrally smoothing output. The positive localized power follows from
\(A^s\chi=A(A^{-(1-s)}\chi)\):
the first term is a compactly supported operator of order \(4s\), and the second is spectrally smoothing. It maps compactly supported \(H_w^{4s}\) vectors into \(L^2\). These are the two comparisons between the local weighted and spectral scales at index \(s\). Combining them with a local parametrix of \(A^k\) gives the comparisons at \(k+s\); duality gives all negative indices. Hence a compact-kernel adapted operator of order \(h\) maps \(H_A^s\) to \(H_A^{s-h/4}\).

Use (11.13) to reach any complex \(z\). Successive localized factors in its initial strip can be composed using larger compact cutoffs around each intermediate support. Their proper symbols compose by Theorem 5.4; their remainders stay spectrally smoothing by the scale comparisons just proved. Spectral powers themselves shift the spectral scale by their real exponents, so their products with smoothing remainders also stay smoothing. This proves (12.3) everywhere. All steps have locally uniform estimates; logarithmic parameter derivatives are absorbed by additional smoothing orders or a small symbol-order margin. This proves the holomorphic assertions. \(\square\)

The same proof, with two chosen realizations, defines a mixed smoothing remainder from the second spectral scale to the first. Compactly supported operators compare the two scales through their common local weighted spaces.

**Theorem 12.3 (compactly supported coefficients on a noncompact manifold).** With the realization in Lemma 12.2, set \(D=\operatorname{sign}(Q)|Q|^{1/2}\). For every \(f\in C_c^\infty(M)\):

1. \([D,f]\) is bounded, and \(f,[D,f]\) belong to every domain of \(\delta=[|D|,\cdot]\).
2. \(f(D-\lambda)^{-1}\) is compact for \(\lambda\notin\mathbb R\).
3. A change of complement changes \(D,|D|\) by locally bounded operators, for any selfadjoint realizations extending the corresponding compact test operators.
4. If \(\varphi\) is a triangular isometry, then \([D,fU_\varphi]\) is bounded, and both \(fU_\varphi,[D,fU_\varphi]\) are regular for \(\delta\).

**Proof.** Although \(Q\) may have spectrum accumulating at zero, its high spectral part gives the same symbols as in (11.19). To justify this without a gap, choose a smooth spectral cutoff \(\theta(A)\) which is zero for \(A\leq1+\epsilon\) and one for \(A\geq1+2\epsilon\). On its support expand
\((1-A^{-1})^{1/4}\) and \((1-A^{-1})^{-1/4}\) by their binomial series. The norm of \(A^{-1}\) on that spectral support is at most \((1+\epsilon)^{-1}<1\). The remainder after \(N\) terms gains \(N\) orders in the \(A\)-scale, just as in (11.16). Lemma 12.2 and asymptotic summation therefore give the localized classical symbols of
\[
|D|\theta(A)=A^{1/4}(1-A^{-1})^{1/4}\theta(A),
\]
\[
D\theta(A)=QA^{-1/4}(1-A^{-1})^{-1/4}\theta(A).
\tag{12.7}
\]
Their principal symbols are \(\rho I\) and \(q_2/\rho\).

Every bounded spectral function supported in a bounded interval of \(A\) is spectrally smoothing: \(A^k g(A)A^k\) is bounded for each \(k\). The low parts of \(D\) and \(|D|\) have exactly this property. Thus \(D\chi\) and \(|D|\chi\) are compact-kernel operators of order one plus spectrally smoothing remainders; adjoints give the corresponding left localizations. This holds without a lower bound on \(|Q|\).

The scalar inequalities
\[
1+|\lambda|^{1/2}\asymp(1+\lambda^2)^{1/4}
\]
identify the graph domains of \(D,|D|\) with \(H_A^{1/4}\). A compact-kernel operator of order zero preserves that domain by Lemma 12.2's scale comparisons. Its commutator with \(|D|\) is again an order-zero compact-kernel operator plus a spectrally smoothing remainder: localize \(|D|\) on the two supports, use its scalar principal symbol to cancel the order-one term, and use the product formula. Products of \(D,|D|\) with smoothing remainders stay smoothing, since these spectral functions shift the \(A\)-scale by at most \(1/4\). This class is therefore stable under every repeated commutator with \(|D|\).

The order-one commutator of \(D\) with the scalar \(f\) cancels in the same way. Consequently \([D,f]\) has order zero plus such a remainder, proving assertion 1 with the actual graph domains.

For assertion 2, first set \(t=0\) in (12.5). The operator \(B_\chi(0)\) has negative order and compact kernel support, so it is compact by Proposition 5.2. The error \(E_\chi(0)\) has a smooth compact kernel and is Hilbert–Schmidt. Multiplication by the bounded \(A^{-1}\) preserves its compactness. Thus \(A^{-1}\chi\) is compact.

For every \(s>0\), approximate the scalar function \(a^{-s}\), \(a\geq1\), uniformly by \(a^{-1}h_R(a)\), where \(h_R\) is bounded and agrees with \(a^{1-s}\) for \(a\leq R\). The error tends to zero uniformly as \(R\to\infty\), by a smooth cutoff and the decay of \(a^{-s}\). Consequently \(A^{-s}\chi\) is compact, as a norm limit of the compact operators \(h_R(A)A^{-1}\chi\).

Define the spectral function
\[
g_\lambda(q)=
\frac{(1+q^2)^{1/4}}
{\operatorname{sign}(q)|q|^{1/2}-\lambda}.
\]
It is bounded because \(\lambda\notin\mathbb R\), and the quotient stays bounded at infinity. Therefore
\((D-\lambda)^{-1}\chi=g_\lambda(Q)A^{-1/4}\chi\)
is compact. Taking adjoints gives the stated left localization \(f(D-\lambda)^{-1}\).

For assertion 3, the two localized symbols of degree one agree, independently of their global realizations. Their difference has order zero; each smoothing remainder is bounded on \(L^2\). Both left and right compact localizations of the difference therefore extend boundedly from the common compact test space. On a closed manifold this gives the global bounded difference of Theorem 12.1.

Finally put \(Q_2=U_\varphi Q U_\varphi^{-1}\), \(D_2=U_\varphi D U_\varphi^{-1}\), and \(A_2=U_\varphi A U_\varphi^{-1}\). This transported realization extends the corresponding formal compact test operator. Its principal symbols are the same as those of \(D,|D|\), because \(\varphi\) is a triangular isometry. Multiplication by \(f\) maps \(H_{A_2}^s\) into \(H_A^s\) for every \(s\), through the common local weighted spaces.

For an order-zero compact-kernel operator \(T\), with a mixed smoothing remainder allowed, define
\[
\partial_{\mathrm{mix}}T=|D|T-T|D_2|.
\tag{12.8}
\]
The same scalar principal-symbol cancellation proves that this is again of that class. Mixed smoothing terms remain smoothing by the two spectral-scale bounds. Also \(Df-fD_2\) is in this order-zero class, since its degree-one symbols cancel. The domain comparisons make these identities actual operator commutators on their graph domains. Since \(U_\varphi\) maps the first spectral scale to the transported second one,
\[
\delta^k(fU_\varphi)
=(\partial_{\mathrm{mix}}^k f)U_\varphi,\qquad
[D,fU_\varphi]=(Df-fD_2)U_\varphi.
\tag{12.9}
\]
Apply (12.8) repeatedly to the second expression as well. All resulting operators are bounded on \(L^2\), proving assertion 4. The domain assertion uses \(U_\varphi:H_A^s\to H_{A_2}^s\), followed by the localized comparison back to \(H_A^s\). \(\square\)

Thus the closed case supplies a selfadjoint realization directly, and the noncompact case has the stated local properties for any realization satisfying the explicit hypothesis. Specifying such a realization on a particular noncompact metric bundle is a separate domain problem.

## 13. The trace of a classical pseudodifferential operator

For an operator of critical negative order, the logarithmic trace has a local formula. We use classical pseudodifferential operators: in a coordinate chart their left symbols have expansions in smooth functions homogeneous in the covariable, with successive degrees differing by one. The Fourier convention is \(D=-i\partial\), with inverse factor \((2\pi)^{-n}\).

The coordinate and localization facts used here are the principal-symbol and smooth-kernel results in Detecting regularity without choosing coordinates. Precisely, a localized classical kernel can be represented by a left symbol; its principal symbol transforms by the cotangent coordinate map and bundle conjugation; operators with zero principal symbol lose one order; and a smooth kernel on a compact manifold has arbitrarily negative symbol order. We reference those calculus results and prove the trace calculation below.

**Theorem 13.1 (the classical trace formula).** Let \(X\) be a closed smooth manifold of dimension \(n\geq1\), and let \(E\to X\) be a finite-rank Hermitian bundle. If \(P\) is a classical pseudodifferential operator of order at most \(-n\) on \(L^2(X,E)\), with degree-\(-n\) symbol \(p_{-n}\), then \(P\) belongs to the weak ideal \(\mathcal L_{1,\infty}\), is measurable for the traces in (4.2), and

\[
\operatorname{Tr}_\omega(P)
=\frac1{n(2\pi)^n}\int_{S^*X}
\operatorname{tr}_E p_{-n}(x,\xi)\,\iota_{\mathcal E}(dx\,d\xi).
\tag{13.1}
\]

Here \(\mathcal E=\sum_j\xi_j\partial_{\xi_j}\) is the radial vector field, and \(S^*X\) is any smooth unit-cosphere section of the positive radial rays. In local Euclidean coordinates the measure in (13.1) is \(dx\,dS(\xi)\). The degree-\(-n\) symbol is zero if the order is strictly smaller. The formula is complex linear and does not require \(P\) to be positive.

The same conclusion holds on a noncompact manifold for an operator whose kernel has compact support in \(X\times X\). A global order bound on an arbitrary noncompact manifold alone does not imply compactness.

**Proof, first on a torus.** Work on \(\mathbb T^n=\mathbb R^n/(2\pi\mathbb Z)^n\) in a trivial bundle of rank \(r\). Write a homogeneous principal symbol as

\[
p_{-n}(x,\xi)=|\xi|^{-n}a(x,\xi/|\xi|).
\tag{13.2}
\]

Extend it smoothly through zero by a frequency cutoff. Its quantization on the torus is characterized by its action on Fourier vectors:
\(P_0(e^{ikx}v)=e^{ikx}p_{-n}(x,k)v\).
The cutoff changes only finitely many Fourier inputs. Local symbol representation and periodic extension give \(P-P_0\) of order at most \(-n-1\), plus a smooth-kernel operator. We show directly that this difference is trace class.

We need an elementary boundedness estimate for periodic symbols. If a matrix symbol \(b(x,k)\) and sufficiently many of its \(x\)-derivatives are bounded uniformly in \(k\), then integration by parts in its \(x\)-Fourier coefficients gives

\[
\|\widehat b(\ell,k)\|\leq C_L(1+|\ell|)^{-L}.
\tag{13.3}
\]

The Fourier matrix of its operator has entry
\(\widehat b(j-k,k)\).
For \(L>n\), both the sum of the norms along any row and along any column are bounded by
\(C_L\sum_{\ell\in\mathbb Z^n}(1+|\ell|)^{-L}\).
The Schur test proves \(L^2\) boundedness. One can verify that test by applying Cauchy–Schwarz to each row with weights equal to the entry norms, then summing columns.

If \(R\) has symbol of order \(-n-1\), its right product with the Fourier multiplier
\(\langle D\rangle^{n+1}\)
has symbol \(r(x,k)\langle k\rangle^{n+1}\), with the bounds needed in (13.3). Thus
\(R=B\langle D\rangle^{-n-1}\)
for a bounded \(B\). The last factor is trace class because
\(\sum_{k\in\mathbb Z^n}\langle k\rangle^{-n-1}<\infty\).
The same argument applies to a smooth kernel. These errors therefore have zero Dixmier trace by the trace construction in the first lesson.

Next consider a principal symbol independent of \(x\), with \(a(\theta)\) a positive semidefinite Hermitian matrix. Its quantization \(B_a\) is a positive Fourier multiplier with matrix blocks
\(|k|^{-n}a(k/|k|)\), apart from finitely many inputs. Let \(\lambda_j(a(\theta))\), \(1\leq j\leq r\), be its nonnegative matrix eigenvalues. The number of eigenvalues of \(B_a\) greater than \(t\) satisfies

\[
\lim_{t\downarrow0}t\,N_{B_a}(t)
=\frac1n\int_{S^{n-1}}\operatorname{tr}a(\theta)\,dS(\theta)
=C_a.
\tag{13.4}
\]

Here is a lattice-counting proof of (13.4). Put \(R=t^{-1/n}\). For each \(j\), the relevant lattice points \(k/R\) lie in the bounded radial set
\[
\Omega_j=\{s\theta:\ 0<s<\lambda_j(a(\theta))^{1/n}\}.
\]
Its volume is
\(\frac1n\int_{S^{n-1}}\lambda_j(a(\theta))\,dS\).
The functions \(\lambda_j\), in decreasing order, are continuous, by the finite-dimensional variational eigenvalue inequalities. The boundary of \(\Omega_j\) has Lebesgue measure zero: away from zero, every fixed radial ray meets the possible boundary at at most one radius, so polar-coordinate Fubini gives zero measure. Zero contributes no measure either. Hence the indicator is Riemann integrable in a large enclosing cube. The grid Riemann sums give
\(R^{-n}\#(\mathbb Z^n\cap R\Omega_j)\to|\Omega_j|\).
Summing the \(r\) branches proves (13.4).

The blocks also give the uniform bound
\(\mu_j(B_a)\leq C\|a\|_\infty/(j+1)\):
there are \(O(R^n)\) lattice points with \(|k|\leq R\), and all remaining blocks have norm at most \(\|a\|_\infty R^{-n}\).
If \(C_a>0\), the counting limit in (13.4) implies
\[
\mu_j(B_a)\sim \frac{C_a}{j},
\qquad j\to\infty.
\]
Indeed, the inequalities
\((C_a-\epsilon)/t\leq N_{B_a}(t)\leq(C_a+\epsilon)/t\)
at small \(t\), applied just above and below the \(j\)-th eigenvalue, squeeze \(j\mu_j\) between \(C_a-\epsilon\) and \(C_a+\epsilon\), with an immaterial one-index shift. It follows by summing and comparison with the harmonic series that \(S_N(B_a)/\log N\to C_a\). If \(C_a=0\), continuity and positivity force \(a=0\), leaving only a finite-rank cutoff. Thus in all cases

\[
\operatorname{Tr}_\omega(B_a)
=\frac1n\int_{S^{n-1}}\operatorname{tr}a(\theta)\,dS.
\tag{13.5}
\]

This proof also gives
\(\|B_a\|_{\mathcal M}\leq C\|a\|_\infty\)
for a general matrix symbol \(a\), by the same singular-value estimate. To obtain (13.5) for such an \(a\), decompose it into its Hermitian real and imaginary parts. For a Hermitian part \(h\), choose \(c>\|h\|_\infty\) and write \(h=(h+cI)-cI\), a difference of smooth positive matrix symbols. Complex linearity then proves (13.5) without positivity.

Now expand the \(x\)-dependence in (13.2):

\[
a(x,\theta)=\sum_{\ell\in\mathbb Z^n}e^{i\ell x}a_\ell(\theta),
\qquad
a_0(\theta)=\frac1{(2\pi)^n}\int_{\mathbb T^n}a(x,\theta)\,dx.
\tag{13.6}
\]

Smoothness and compactness give
\(\sum_\ell\|a_\ell\|_\infty<\infty\),
by applying sufficiently many \(x\)-derivatives before taking the Fourier coefficient. Therefore
\(P_0=\sum_\ell M_{e^{i\ell x}}B_{a_\ell}\)
converges in the \(\mathcal M\)-norm. Its identity as an operator follows first on finite Fourier sums, and then by bounded convergence.

Let \(T_yu(x)=u(x+y)\). Conjugating a summand gives

\[
T_yM_{e^{i\ell x}}B_{a_\ell}T_y^*
=e^{i\ell y}M_{e^{i\ell x}}B_{a_\ell}.
\]

Unitary invariance of \(\operatorname{Tr}_\omega\) forces the trace of every \(\ell\neq0\) summand to vanish: choose \(y\) with \(e^{i\ell y}\neq1\). Continuity in the \(\mathcal M\)-norm permits summation. Applying (13.5) to \(a_0\) gives

\[
\operatorname{Tr}_\omega(P)
=\frac1{n(2\pi)^n}
\int_{\mathbb T^n}\int_{S^{n-1}}
\operatorname{tr}p_{-n}(x,\theta)\,dS\,dx.
\tag{13.7}
\]

The same estimates, before taking the trace, prove weak-\(\mathcal L_1\) membership of \(P\). One can also see this by writing its full symbol times \(\langle k\rangle^n\): (13.3) factors \(P\) as a bounded operator times \(\langle D\rangle^{-n}\), whose singular values are \(O(1/(j+1))\).

**Localization on a manifold.** Choose a finite real smooth square partition
\(\sum_j\chi_j^2=1\), with each \(\chi_j\) supported compactly in a bundle-trivializing coordinate chart. We first establish ideal membership; cyclicity cannot be applied before that step. Choose \(\psi_j\) supported in the same chart and equal to one on a neighborhood of \(\operatorname{supp}\chi_j\). On smooth sections,
\[
P=\sum_j\chi_j^2P\psi_j+R,
\qquad R=\sum_j\chi_j^2P(1-\psi_j).
\]
The first summands have both kernel variables supported inside one chart. Transfer them isometrically into flat tori, incorporating the square-root density and an orthonormal bundle frame. The torus estimate already proved gives bounded extensions with singular values \(O((k+1)^{-1})\); composing with the bounded transfer maps preserves this estimate by the singular-value approximation formula (1.1) in the first lesson. The kernel of each summand of \(R\) is smooth, since its two supports are separated from the diagonal. On a compact manifold a smooth kernel is trace class: localize its two variables in finitely many pairs of charts, transfer to pairs of tori, and expand in the two Fourier bases. Smoothness makes the matrix coefficients absolutely summable, giving a trace-norm convergent sum of rank-one operators. This argument does not use a logarithmic trace.

Finite sums preserve the weak-ideal estimate. Indeed (1.1), applied to the sum of rank-\(k\) approximants of \(m\) compact operators, gives
\[
\mu_{mk}\!\left(\sum_{j=1}^m A_j\right)
\leq\sum_{j=1}^m\mu_k(A_j).
\]
Monotonicity fills the indices between multiples of \(m\). Trace-class operators have the same weak estimate, since \((k+1)\mu_k(R)\leq\|R\|_1\). Thus the displayed decomposition proves \(P\in\mathcal L_{1,\infty}\subset\mathcal M_{1,\infty}\), including its bounded extension from smooth sections, before any trace is taken. Now cyclicity and \(\sum_j\chi_j^2=1\) legitimately give

\[
\operatorname{Tr}_\omega(P)
=\sum_j\operatorname{Tr}_\omega(\chi_jP\chi_j).
\tag{13.8}
\]

The compactly supported kernel of each summand can be transferred into a cube in a flat torus and extended by zero. Incorporate the square root of the smooth density and an orthonormal bundle frame into this transfer, so it is an isometry on the local \(L^2\) space. It does not change the principal symbol except by bundle conjugation and the two scalar factors \(\chi_j\). Thus its principal symbol is \(\chi_j^2p_{-n}\).

To justify equality of the traces under this transfer, one can work on the direct sum of the two Hilbert spaces. The two rectangular transfer maps become bounded off-diagonal block operators. Cyclicity of the trace on that direct sum gives the same trace for the two localized products. Appending a zero block changes no nonzero singular values and no logarithmic trace value. Hence the torus calculation applies to each summand in (13.8). Global weak-ideal membership was proved before (13.8); it is not inferred from an identity \(P=\sum_j\chi_jP\chi_j\), which generally fails.

It remains to verify that the integral just obtained is intrinsic. For fixed \(x\), a degree-\(-n\) symbol has

\[
\int_{1\leq|\xi|\leq R}\operatorname{tr}p_{-n}(x,\xi)\,d\xi
=\log R\int_{|\theta|=1}\operatorname{tr}p_{-n}(x,\theta)\,dS.
\tag{13.9}
\]

Changing the unit sphere to any smooth positive radial section changes the radial limits on each ray by fixed positive factors. Their logarithms are bounded on a compact base set, so the coefficient of \(\log R\) is unchanged. A cotangent coordinate change preserves \(dx\,d\xi\), because its base and fiber Jacobians are reciprocal. Changing the bundle frame conjugates \(p_{-n}\) and preserves its matrix trace. These observations prove that the coefficient in (13.9), integrated over \(x\), is exactly the intrinsic integral in (13.1). Summing \(\chi_j^2\) completes the proof.

For compact kernel support on a noncompact manifold, use finitely many charts around its projection onto the diagonal. The part of the kernel separated from the diagonal is smooth with compact support. After transfer into finitely many torus products it is trace class by the preceding negative-order argument. The diagonal part is treated by the same localized proof. \(\square\)

The factor \(1/n\) measures radial logarithmic growth. The factor \((2\pi)^{-n}\) comes from Fourier quantization. They should not be combined with a different residue-variable convention without checking the change of variable.

## 14. Geometric Dirac operators and their index formulas

Let \(M\) be a closed Riemannian spin manifold of dimension \(d\), let \(S\) be its Hermitian spinor bundle, and let \(D\) be the geometric Dirac operator on \(L^2(M,S)\). Its commutator with a smooth function is Clifford multiplication by its differential. Fix the Clifford convention when choosing an orientation and a grading; the spectral assertion below does not depend on that sign choice. Use \(\Lambda=|D|+P_0\) if a kernel is present.

**Proposition 14.1 (the full coefficient spectrum).** The Dirac triple is regular and weakly \(d\)-summable. The dimension spectrum for its order-zero coefficient algebra is simple and is contained in

\[

\{d-j:j=0,1,2,\ldots\}.

\tag{14.1}

\]

This assertion includes negative integers. The actual spectrum need not be contained in the finite set of positive integers at most \(d\).

**Proof.** If \(d=0\), the manifold is a finite set: the Hilbert space is finite dimensional, all coefficient zeta functions are entire, and regularity and summability are immediate. In the following symbol and singular-value argument assume \(d>0\). Use the weight-one parametrix construction in Theorem 10.4 above. The Dirac principal symbol is invertible away from zero and has square \(|\xi|^2I\). Its order-one parametrix gives \(\|u\|_{H^1}\leq C(\|Du\|_2+\|u\|_2)\); smooth approximation gives the closure domain \(H^1\). An adjoint-domain vector satisfies \(Du\in L^2\) distributionally, hence belongs to \(H^1\) by that parametrix. Formal symmetry then proves selfadjointness. Finite chart Fourier truncations prove compactness of \(H^1\hookrightarrow L^2\), so the resolvent is compact. This is the proof of Corollary 10.5 with order one instead of order two.

For the positive order-two operator \(D^2+P_{\ker D}=\Lambda^2\), use the parameter-inverse construction of Theorem 11.1 above with every weight one and degree two in place of four. Its leading inverse is \((|\xi|^2+t)^{-1}\); Taylor composition, asymptotic summation and the actual resolvent remainder are unchanged, with joint radius \((\langle\xi\rangle^2+t)^{1/2}\). The convergent Mellin integral first constructs powers with exponent in \((-1,0)\), and multiplication by integer powers supplies all exponents with the proved remainder estimates. It follows that \(\Lambda^z\) is classical of order \(z\) with scalar principal symbol \(|\xi|^z\). The finite-rank kernel correction is smoothing and does not change that symbol. Since \([D,f]\) is a smooth multiplication operator, it is bounded and preserves smooth sections.

Commuting a classical order-zero operator with \(\Lambda\) leaves order zero: the order-one leading product terms cancel because the principal symbol of \(\Lambda\) is scalar. Iteration therefore puts \(f,[D,f]\) and every required \(\delta\)-commutator in the bounded order-zero class, with their graph-domain identities. This proves regularity. The compact-manifold singular-value estimate for an operator of order \(-1\), also obtained in the ordinary case of Theorem 5.3 in this lesson, gives

\(\mu_j(\Lambda^{-1})=O((j+1)^{-1/d})\).

For any coefficient \(b\), the product \(b\Lambda^{-z}\) is a holomorphic classical family of order \(-z\). In a localized symbol integral, the radial integral of its degree \(-z-j\) term has denominator \(z+j-d\). Its angular and spatial integral is holomorphic in \(z\). Truncate below trace-class order on a chosen compact \(z\)-set; the remainder trace is holomorphic there. Thus there are only simple possible poles at \(d-j\), as asserted. This is the ordinary version of the joint-family continuation proof in Proposition 9.3 of [The local index formula](the-local-index-formula.md) of this lesson. There is no argument in that proof discarding the negative \(d-j\). \(\square\)

This spectrum convention agrees with [Ponge 2003, Example 3.5]. The following direct calculation shows why the negative part cannot be removed even on a flat manifold.

**Example 14.2 (a negative Dirac pole on a two-torus).** On

\(M=(\mathbb R/2\pi\mathbb Z)^2\), use the periodic spin structure and

\[

D=-i\sigma_1\partial_{x_1}-i\sigma_2\partial_{x_2},

\qquad \gamma=\sigma_3,

\tag{14.2}

\]

where the Pauli matrices are Hermitian, satisfy \(\sigma_j^2=1\), and anticommute in distinct directions. Each nonzero Fourier mode \(k\in\mathbb Z^2\) has \(|D|=|k|I_2\). Complete its two-dimensional kernel as above. Let \(U=e^{ix_1}\), and put

\[

b=U^{-1}\delta(U).

\]

This belongs already to the smaller coefficient algebra generated by functions and their \(\delta\)-commutators. On all sufficiently large Fourier modes it is the scalar multiplier

\[

b(k)=|k+(1,0)|-|k|.

\tag{14.3}

\]

The kernel completion changes only finitely many terms and hence contributes an entire function to \(\operatorname{Tr}(b\Lambda^{-z})\).

Write \(r=|\xi|\) and \(c=\xi_1/r\). Expansion of

\(r(1+2c/r+1/r^2)^{1/2}-r\) gives

\[

b(\xi)\sim

c+\frac{1-c^2}{2r}

+\frac{c^3-c}{2r^2}

+\frac{-1+6c^2-5c^4}{8r^3}+\cdots.

\tag{14.4}

\]

Every differentiated remainder has the corresponding lower classical order: the square root is analytic in \(1/r\) uniformly on the circle for \(r\) sufficiently large, and differentiation preserves these symbol estimates.

At \(z=-1\), the degree \(-3\) coefficient of \(b\), multiplied by \(|\xi|^{-z}\), has the critical degree \(-2\). The local radial-integral proof of Proposition 14.1 gives

\[

\begin{aligned}

\operatorname*{Res}_{z=-1}\operatorname{Tr}(b\Lambda^{-z})

&=2\int_0^{2\pi}

\frac{-1+6\cos^2\theta-5\cos^4\theta}{8}\,d\theta\\

&=\frac{\pi}{16}\ne0.

\end{aligned}

\tag{14.5}

\]

The factor two is the spinor rank. The factor \((2\pi)^{-2}\) from quantization cancels the torus volume \((2\pi)^2\). The elementary angular integrals are

\(\int\cos^2\theta\,d\theta=\pi\) and

\(\int\cos^4\theta\,d\theta=3\pi/4\).

Thus \(-1\) is an actual simple pole in the Dirac dimension spectrum, not merely an allowed symbol degree.

The finite residue index formula still uses only finitely many positive spectral degrees. Its coefficient operators have negative order as in Section 3 of [The local index formula](the-local-index-formula.md), and a pole at residue parameter zero can come only from a positive argument of a coefficient zeta function. The full dimension spectrum and the part relevant to that index are different sets.

We now compute those index coefficients. The argument uses a local heat inverse and its Clifford filtration, following the mechanism of Getzler rescaling discussed in [Ponge 2003, Sections 1–2, 4–5]. We give the analytic remainder argument as well as the curvature calculation, since a formal rescaling alone would not justify taking a residue.

Fix the Clifford convention

\(c(v)c(w)+c(w)c(v)=-2\langle v,w\rangle\).

In dimension \(d=2m\), take

\(\gamma=i^m c(e^1)\cdots c(e^{2m})\).

In dimension \(d=2m+1\), choose the irreducible spin representation with

\(c(e^1)\cdots c(e^{2m+1})=(-i)^{m+1}I\).

The latter convention gives \(D=-i\partial_x\) on an oriented circle.

Write \(\operatorname{Tr}_*\) for the supertrace in even dimension and the ordinary trace in odd dimension. In the odd case below, all inserted Clifford expressions have odd parity.

Let \(\mathcal R\) be the matrix of tangent curvature two-forms, with entries

\[

\mathcal R_{ij}

=\frac12\sum_{k,l}

\langle R^{TM}(e_k,e_l)e_i,e_j\rangle\,e^k\wedge e^l.

\tag{14.6}

\]

Here \(R^{TM}(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}\).

The transpose choice in (14.6) does not affect the even power series defining

\[

\widehat A_{\rm raw}(\mathcal R)

=\det{}^{1/2}\left(\frac{\mathcal R/2}{\sinh(\mathcal R/2)}\right),

\qquad

\widehat A(M)

=\widehat A_{\rm raw}\left(\frac{\mathcal R}{2\pi i}\right).

\tag{14.7}

\]

The square root is the formal branch with constant term one; equivalently use

\(\exp(\tfrac12\operatorname{tr}\log(\cdot))\).

All these series terminate in each exterior algebra.

For a unitary bundle connection of curvature \(F^E\), our Chern form is

\(\operatorname{Ch}(E)=\operatorname{Tr}\exp(-F^E/(2\pi i))\).

This sign is consistent with the Clifford and index orientations just fixed.

**Lemma 14.3 (a heat inverse with controlled diagonal coefficients).**

Let \(L\) be a nonnegative selfadjoint Laplace-type operator on a finite bundle over a closed \(d\)-manifold. Its principal symbol is \(|\xi|_g^2I\).

In a coordinate trivialization, write its differential symbol as

\(p=p_2+p_1+p_0\), and use \(D_x=(1/i)\partial_x\).

Define symbols of parabolic degrees \(-2-j\) recursively by

\[

\begin{aligned}

q_{-2}&=(p_2+i\tau)^{-1},\\

q_{-2-j}

&=-(p_2+i\tau)^{-1}

\sum_{\substack{l+|\alpha|+r=j\\0\leq l\leq2,\ 0\leq r<j}}

\frac1{\alpha!}

(\partial_\xi^\alpha p_{2-l})

(D_x^\alpha q_{-2-r}).

\end{aligned}

\tag{14.8}

\]

The dilation is \((\xi,\tau)\mapsto(\lambda\xi,\lambda^2\tau)\).

Each term has a unique distributional extension whose inverse Fourier transform vanishes at negative time. The diagonal heat kernel has, with every spatial derivative, the expansion

\[

K_L(x,x,t)\sim

\sum_{j\geq0}\check q_{-2-j}(x,0,t),

\qquad t\downarrow0.

\tag{14.9}

\]

Here \(\check q\) includes the \((2\pi)^{-d-1}\) Fourier normalization.

Terms of odd parabolic degree vanish on the spatial diagonal. Multiplying the formal heat inverse on the left by any differential operator gives the analogous differentiated expansion.

**Proof.**

The recursion follows by setting

\((p+i\tau)\#q=1\) degree by degree. Because \(p\) is a differential symbol, its left composition formula has only the terms \(|\alpha|\leq2\); thus it is exact before truncation. The omitted leading term at degree \(j\) is

\((p_2+i\tau)q_{-2-j}\), giving (14.8).

Differentiating its denominator shows that each summand is a polynomial in \(\xi\), with smooth matrix coefficients, divided by an integer power of \(p_2+i\tau\).

These rational expressions have a concrete causal inverse. For integer \(a\geq1\),

\[

(p_2+i\tau)^{-a}

=\frac1{(a-1)!}\int_0^\infty

s^{a-1}e^{-sp_2}e^{-is\tau}\,ds.

\tag{14.10}

\]

Fourier inversion in \(\tau\) therefore gives

\(1_{\{t>0\}}t^{a-1}e^{-tp_2}/(a-1)!\).

Polynomial factors in \(\xi\) become derivatives of a positive-definite Gaussian in the spatial difference. This defines tempered distributions even when the rational function is not locally integrable at \((0,0)\).

Two extensions could differ only by a distribution supported at that frequency point. Its inverse Fourier transform is a polynomial in space and time, and a polynomial vanishing for \(t<0\) is zero. This proves uniqueness.

A term of parabolic degree \(k\) obeys

\[

\check q_k(x,0,t)

=t^{-(d+k+2)/2}\check q_k(x,0,1).

\tag{14.11}

\]

The same Gaussian formulas give, on compact coordinate subsets, derivative bounds by a power of \(t\) times

\(\exp(-c|x-y|^2/t)\); each spatial difference derivative costs at most \(t^{-1/2}\). Parameter derivatives in \(x\) give polynomial Gaussian factors with the same type of bound.

The recursion also gives

\(q_k(x,-\xi,\tau)=(-1)^kq_k(x,\xi,\tau)\).

Thus an odd \(k\) has zero inverse Fourier value at spatial difference zero, for \(t>0\).

For clarity, the remainder in (14.9) concerns the actual heat kernel.

Truncate at \(j=J\), use coordinate cutoffs equal to one near the diagonal, and sum over a finite bundle cover. The resulting causal kernel \(Q_J(t)\) has initial value the identity: the \(j=0\) Gaussian has this limit, while every higher term has zero initial value as a distribution, by (14.10) and its degree.

Its heat-equation defect

\[

R_J(t)=(\partial_t+L)Q_J(t)

\]

is a finite sum of inverse rational symbols of degrees at most \(-J-1\), together with cutoff terms off the diagonal.

For any fixed integers \(a,b,K\), choosing \(J\) sufficiently large makes

\[

\|R_J(t)\|_{H^{-a}\to H^b}=O(t^K).

\tag{14.12}

\]

Indeed, Gaussian scaling bounds every prescribed kernel derivative; the finite cover and integration in the second variable give (14.12). Cutoff derivatives away from the diagonal are \(O(t^K)\) for every \(K\), by their Gaussian factor.

The elliptic Sobolev estimates and domain construction in Sections 10–11 of this lesson, in the ordinary-weight case, identify the required Sobolev norms with powers of \(1+L\). Spectral calculus makes \(e^{-sL}\) uniformly bounded on each such space for \(0\leq s\leq1\).

Duhamel's formula now gives

\[

e^{-tL}-Q_J(t)

=-\int_0^t e^{-(t-s)L}R_J(s)\,ds.

\tag{14.13}

\]

It holds first on smooth sections by differentiation and the initial value, and then between the stated Sobolev spaces. The right side is \(O(t^{K+1})\) between those spaces. Taking \(a,b\) large and applying Sobolev embedding gives any desired number of kernel derivatives. Increasing \(J\) proves the full expansion.

Left application of a differential operator costs finitely many of these derivatives, so the same proof covers the last assertion. No merely formal inverse or unspecified smoothing remainder is used. \(\square\)

**Lemma 14.4 (Clifford filtration and the curvature heat model).**

Use normal coordinates at a point and parallel orthonormal frames along radial geodesics. Assign degrees

\[

\deg\partial_{x_i}=1,\quad

\deg c(e^i)=1,\quad

\deg x_i=-1,\quad

\deg\partial_t=2.

\tag{14.14}

\]

For the Dirac operator on \(S\otimes E\), the associated leading model of \(D_E^2\) is

\[

H_{\mathcal R}+F^E(0),\qquad

H_{\mathcal R}

=-\sum_i\left(\partial_i-\frac14\mathcal R_{ij}(0)x_j\right)^2.

\tag{14.15}

\]

Clifford multiplication in the leading model is exterior multiplication.

The leading heat inverse has filtration degree \(-2\).

For an inserted differential operator \(P\) of filtration degree at most \(G\), whose Clifford parity is \(d\bmod2\), its trace has the following bounds:

\[

\begin{cases}

\operatorname{Tr}_*(Pe^{-tD_E^2})

=t^{-G/2}L_P+O(t^{1-G/2}),&G\equiv d\pmod2,\\

\operatorname{Tr}_*(Pe^{-tD_E^2})

=O(t^{(1-G)/2}),&G\not\equiv d\pmod2.

\end{cases}

\tag{14.16}

\]

In the first line \(L_P\) is obtained by applying the leading model of \(P\) to the model heat kernel, extracting exterior degree \(d\), and taking its Clifford trace. A vanishing leading model permits using the degree \(G-1\) bound instead.

The even spinor trace and oscillator are the spin specialization of Measured foliation index, Lemmas 6.24–6.25: take a trivial spin-c determinant line and one closed leaf. Its curvature matrix is \(\Omega=-\mathcal R\), so its connection model with \(+\Omega x/4\) is precisely (14.15). Its chirality equals our \(\gamma\), and its normalized twisting form \(\operatorname{Tr}\exp(iF^E/(2\pi))\) equals ours. We use this local algebraic model. The argument below also treats odd spinors and proves the differentiated insertion and diagonal-parity estimates needed for the residues.

**Proof.**

For exterior forms, the leading part of \(c(\alpha)c(\beta)\) is

\(\alpha\wedge\beta\); contractions reduce Clifford degree by two.

When symbols are composed, a derivative in \(\xi\) lowers degree by one and its paired derivative in \(x\) raises it by one. Thus leading models compose as polynomial-coefficient differential operators with exterior coefficients; every Taylor or contraction error has strictly smaller filtration degree.

Here is the curvature computation, including its factor of two.

For a connection in radial gauge, \(x_iA_i(x)=0\), differentiation and the curvature identity give

\[

A_i(x)=\int_0^1 s\,x_jF_{ji}(sx)\,ds

=-\frac12x_jF_{ij}(0)+O(|x|^2).

\tag{14.17}

\]

The spin curvature is

\(\frac14\sum_{k,l}R_{ij\,kl}c(e^k)c(e^l)\).

The curvature pair symmetry identifies

\(\frac12\sum_{k,l}R_{ij\,kl}e^k\wedge e^l\)

with \(\mathcal R_{ij}\) in (14.6).

Hence the degree-one part of the spin covariant derivative is

\(\partial_i-\mathcal R_{ij}x_j/4\).

The bundle \(E\)'s connection terms have lower degree; its curvature contributes the constant two-form \(F^E(0)\) to the degree-two model.

To verify the squared operator, expand \(D_E^2\) in an orthonormal frame. The symmetric part of \(c(e^i)c(e^j)\nabla_i\nabla_j\) is the connection Laplacian. The antisymmetric part is

\(\frac12c(e^i)c(e^j)F^{S\otimes E}_{ij}\).

Its spin term contracts the Riemann tensor: the four-form component vanishes by the first Bianchi identity, the two-form component vanishes by symmetry of the Ricci tensor, and the scalar component is \(\operatorname{scal}/4\).

The other term is \(\frac12c(e^i)c(e^j)F^E_{ij}\).

Consequently

\[

D_E^2

=-g^{ij}(\nabla_i\nabla_j-\Gamma_{ij}^k\nabla_k)

+\frac{\operatorname{scal}}4+c(F^E).

\tag{14.18}

\]

Since \(g^{ij}=\delta^{ij}+O(|x|^2)\) and

\(\Gamma_{ij}^k=O(|x|)\), all corrections to the connection Laplacian's Euclidean leading model have smaller degree. The scalar curvature also has degree zero. This gives (14.15).

Apply (14.8) with this filtration. Its formal inverse has degree at most \(-2\): invert the scalar Euclidean heat symbol first, and expand in the remaining Taylor and exterior terms. Every factor respects this bound, and any product containing sufficiently many positive exterior degrees vanishes. Terms with a smaller degree cannot raise it under composition.

Taking the degree-zero part of

\((D_E^2+\partial_t)Q=1\) shows that the leading inverse is exactly

\((H_{\mathcal R}+F^E(0)+\partial_t)^{-1}\).

One may also obtain this identity from the finite exterior Neumann inverse; it supplies uniqueness of the leading inverse.

We spell out why the filtration gives the trace estimates, including the improvement from parity.

For a heat-inverse symbol term of ordinary parabolic degree \(k\), exterior degree \(h\), and Taylor monomial \(x^\alpha\), the filtration degree is \(k+h-|\alpha|\).

At the center only \(\alpha=0\) survives.

If the inverse with insertion \(P\) has degree at most \(G-2\), its exterior degree \(h\) coefficient there therefore has \(k\leq G-2-h\).

By (14.11) this term contributes

\(t^{-(d+k+2)/2}\).

Only even \(k\) can contribute on the diagonal. If \(G-h\) is even, the largest possible \(k\) is \(G-2-h\), and the next surviving \(k\) is smaller by two. If \(G-h\) is odd, the largest possible even \(k\) is \(G-3-h\).

The even supertrace vanishes on Clifford monomials of degree less than \(d\).

For odd \(d\), the ordinary spin trace on the odd Clifford part also vanishes below degree \(d\). To see both statements, conjugate a proper monomial by a suitable Clifford generator; its relevant trace changes sign. On the volume monomial the values are

\[

\operatorname{Str}c(e^1)\cdots c(e^{2m})=(-2i)^m,

\qquad

\operatorname{Tr}c(e^1)\cdots c(e^{2m+1})=(-i)^{m+1}2^m.

\tag{14.19}

\]

These follow directly from the chosen grading or odd volume relation and the spinor rank \(2^m\).

In odd dimension the formal computation can be made in the full Clifford algebra and then represented on spinors; its odd parity is what excludes the scalar trace component.

Set \(h=d\) in the preceding degree bounds. They give precisely (14.16). Lemma 14.3 supplies the differentiated remainders and allows integration over the closed manifold. \(\square\)

The remaining model is explicitly solvable:

\[

\begin{aligned}

G_{\mathcal R}(x,t)

={}&(4\pi t)^{-d/2}

\det{}^{1/2}\left(\frac{t\mathcal R/2}{\sinh(t\mathcal R/2)}\right)\\

&\quad\cdot

\exp\left(-\frac1{4t}

\left\langle (t\mathcal R/2)\coth(t\mathcal R/2)x,x\right\rangle\right).

\end{aligned}

\tag{14.20}

\]

It is the positive-time fundamental solution of \(H_{\mathcal R}\) with pole at \(x=0\). The apparent singular functions of \(\mathcal R\) are regular power series: \(w/\sinh w\) and \(w\coth w\) both have constant term one.

Here is a direct verification of (14.20).

For the scalar oscillator

\(-\partial_x^2+a^2x^2/4\), set

\[

G_a(x,t)=(4\pi t)^{-1/2}

\left(\frac{at}{\sinh at}\right)^{1/2}

\exp\left(-\frac{a\coth(at)}4x^2\right).

\]

Writing it as \(C(t)e^{-\alpha(t)x^2}\), the heat equation reduces to

\(\alpha'=a^2/4-4\alpha^2\) and \(C'/C=-2\alpha\).

The displayed \(\alpha\) and \(C\) satisfy both equations, and Gaussian scaling gives the initial distribution \(\delta_0\).

For a real antisymmetric matrix \(A\), orthogonal two-plane decomposition and products of these scalar solutions treat the potential

\(-A^2/4\). The additional infinitesimal rotation term in

\(-\sum(\partial_i-iA_{ij}x_j/2)^2\)

annihilates this Gaussian, since its quadratic matrix commutes with \(A\).

Its solution is therefore (14.20) with \(\mathcal R=2iA\).

Both sides of the heat equation are analytic power series in the matrix entries near zero. Their identities extend to a skew matrix of commuting two-forms, where only finitely many terms remain. The same initial-value verification applies degree by degree. This proves (14.20), rather than assuming a heat coefficient formula.

The twisting curvature commutes with this scalar exterior operator, so the full model kernel is

\(G_{\mathcal R}(x,t)\wedge e^{-tF^E(0)}\).

**Theorem 14.5 (Dirac residues and the commutator cancellation).**

Let \(D\) be the untwisted spin Dirac operator. For \(n\geq1\) of the same parity as \(d\), put

\[

\begin{aligned}

P_{n,k}

&=f_0\,\nabla^{k_1}([D,f_1])\cdots

\nabla^{k_n}([D,f_n]),\\

I_n^{\rm raw}

&=\int_M f_0\,df_1\wedge\cdots\wedge df_n

\wedge\widehat A_{\rm raw}(\mathcal R)_{d-n},

\qquad \nabla(T)=[D^2,T].

\end{aligned}

\tag{14.21}

\]

Components of negative degree are zero.

Then every \(k\neq0\) has zero residue:

\[

\operatorname*{Res}_{z=0}

\operatorname{Tr}_*(P_{n,k}\Lambda^{-n-2|k|-2z})=0.

\tag{14.22}

\]

For \(k=0\) the residue is

\[

\frac{I_n^{\rm raw}}{\Gamma(n/2)}

\begin{cases}

(2\pi i)^{-m},&d=2m,\\

\sqrt\pi\,(2\pi i)^{-m-1},&d=2m+1.

\end{cases}

\tag{14.23}

\]

In particular, the gamma denominator and the spectral variable in this formula are specified.

**Proof.**

The operator \([D,f]\) is \(c(df)\), of filtration degree one, with leading model the constant form \(df(0)\).

An iterated commutator has degree at most \(1+2k\). For \(k\geq1\), its putative leading model is

\[

\operatorname{ad}_{H_{\mathcal R}}^{\,k}(df(0))=0.

\]

Indeed \(H_{\mathcal R}\) is an even exterior operator with constant curvature coefficients, and differentiation does not change the constant \(df(0)\).

Thus if \(|k|>0\), \(P_{n,k}\) has degree at most \(n+2|k|-1\).

Its parity is \(n\bmod2=d\bmod2\). The second line of (14.16), with \(G=n+2|k|-1\), gives

\[

\operatorname{Tr}_*(P_{n,k}e^{-tD^2})

=O(t^{\,1-n/2-|k|}).

\tag{14.24}

\]

The full extra power of \(t\) uses both the lost filtration degree and the diagonal parity; losing only a half power would be an incomplete count.

For \(k=0\), the leading model of \(P_{n,0}\) is multiplication by

\(f_0(0)df_1(0)\wedge\cdots\wedge df_n(0)\).

At \(x=0\), (14.20) is

\((4\pi t)^{-d/2}\widehat A_{\rm raw}(t\mathcal R)\).

Extraction of degree \(d\) after multiplication by the degree-\(n\) form supplies \(t^{(d-n)/2}\).

Together with (14.19), this gives

\[

\operatorname{Tr}_*(P_{n,0}e^{-tD^2})

=t^{-n/2}L_n+O(t^{1-n/2}),

\tag{14.25}

\]

where

\[

L_n=I_n^{\rm raw}

\begin{cases}

(-2i)^m(4\pi)^{-m}=(2\pi i)^{-m},&d=2m,\\

(-i)^{m+1}2^m(4\pi)^{-m-1/2}

=\sqrt\pi(2\pi i)^{-m-1},&d=2m+1.

\end{cases}

\]

If \(n>d\), the leading model has zero degree-\(d\) part; the same formulas give zero.

Every harmonic spinor is smooth by elliptic regularity. Replacing \(D^2\) by

\(\Lambda^2=D^2+P_0\) changes the inserted heat trace by

\((e^{-t}-1)\operatorname{Tr}_*(P_{n,k}P_0)=O(t)\).

For large real \(z\), spectral calculus therefore gives

\[

\operatorname{Tr}_*(P_{n,k}\Lambda^{-n-2|k|-2z})

=\frac1{\Gamma(z+n/2+|k|)}

\int_0^\infty

t^{z+n/2+|k|-1}

\operatorname{Tr}_*(P_{n,k}e^{-t\Lambda^2})\,dt.

\tag{14.26}

\]

It can be justified in the initial trace half-plane by the smoothing bounds or by an eigenbasis, and then continued by splitting the integral at one.

The large-time integral is entire near zero since \(\Lambda^2\geq cI>0\).

For \(k\neq0\), (14.24) makes the small-time integral holomorphic for \(\operatorname{Re}z>-1\). For \(k=0\), (14.25) gives \(L_n/z\) plus a holomorphic remainder. The reciprocal gamma factor is regular at \(n/2>0\).

This proves (14.22)–(14.23). The factor \(1/z\), with no additional two, is a consequence of using \(\Lambda^{-2z}\) in (14.26). \(\square\)

**Theorem 14.6 (the geometric residue cocycle).**

For the converted cocycle of Section 5 of [The local index formula](the-local-index-formula.md) on scalar smooth functions, the even components are

\[

\Phi'_n(f_0,\ldots,f_n)

=\frac1{n!(2\pi i)^{n/2}}

\int_M f_0\,df_1\wedge\cdots\wedge df_n

\wedge\widehat A(M)_{d-n},

\quad n=0,2,\ldots,2m.

\tag{14.27}

\]

The odd components are

\[

\Phi'_n(f_0,\ldots,f_n)

=\frac{\sqrt{2\pi i}}{n!(2\pi i)^{(n+1)/2}}

\int_M f_0\,df_1\wedge\cdots\wedge df_n

\wedge\widehat A(M)_{d-n},

\tag{14.28}

\]

Here \(n=1,3,\ldots,2m+1\). All higher components vanish.

**Proof.**

Theorem 14.5 leaves only \(k=0\), for which

\(A_{n,0}=1/n!\).

The coefficient zeta function has only a simple possible pole at zero; hence every higher Laurent residue is zero.

The gamma value in the raw cocycle cancels the denominator \(\Gamma(n/2)\) of (14.23).

The conversion factors have value one at zero, so they preserve this simple residue.

The remaining prefactor is \(L_n/n!\) in the even case and

\(\sqrt{2i}L_n/n!\) in the odd case.

The raw form of degree \(d-n\) differs from its normalized form by

\((2\pi i)^{(d-n)/2}\). This proves the stated positive-degree constants.

For even degree zero, (14.16) and (14.20) give

\[

\operatorname{Tr}(\gamma f_0e^{-t\Lambda^2})

=\int_M f_0\,\widehat A(M)_d+O(t).

\]

The Mellin transform now contains \(1/\Gamma(z)\).

Its simple zero at zero cancels the \(1/z\) from this constant heat coefficient. Thus the completed degree-zero zeta function is holomorphic there and its value, hence its finite part, is that integral. This proves (14.27) also for \(n=0\), including the kernel completion.

The degree convention gives the vanishing of the other components. \(\square\)

**Theorem 14.7 (classical geometric index pairings).**

For a smooth Hermitian bundle \(E\) on a closed even-dimensional spin manifold, the Dirac operator coupled to any unitary connection satisfies

\[

\operatorname{Index}D_E^+

=\int_M\widehat A(M)\wedge\operatorname{Ch}(E).

\tag{14.29}

\]

For a smooth unitary matrix function \(U\) on a closed odd-dimensional spin manifold, with the positive spectral projection \(P\), put \(A=U^{-1}dU\). Then

\[

\operatorname{Index}(PUP)

=-\sum_{j=0}^{m}

\frac{j!}{(2j+1)!(2\pi i)^{j+1}}

\int_M\widehat A(M)_{d-2j-1}

\wedge\operatorname{Tr}(A^{2j+1}).

\tag{14.30}

\]

Products in this formula are exterior products with matrix multiplication.

**Proof.**

First take a smooth orthogonal projection \(e\) in a trivial finite bundle. Its image has the Grassmann connection \(e\,d\), with curvature

\(F^E=e(de)^2\) on the image bundle. Compression of the untwisted Dirac operator is exactly the Dirac operator for this connection, since

\(e\,c\circ\nabla(e\psi)=c\circ(e\nabla)(e\psi)\).

Theorem 10.4 of [The local index formula](the-local-index-formula.md) and (14.27) evaluate its index as the integral of

\[

\widehat A(M)\wedge

\sum_{j\geq0}\frac{(-1)^j}{j!(2\pi i)^j}

\operatorname{Tr}\bigl(e(de)^{2j}\bigr).

\tag{14.31}

\]

For \(j\geq1\), the half shift in the even Chern cycle does not change this expression:

\(\operatorname{Tr}((de)^{2j})=0\).

Moving the first degree-one factor through the other \(2j-1\) factors in the matrix trace multiplies it by \(-1\); thus this trace equals its own negative.

Differentiating \(e^2=e\) shows that \(de\) is off diagonal relative to the image and its complement, so \((de)^2\) commutes with \(e\). Consequently

\(\operatorname{Tr}(e(de)^{2j})=\operatorname{Tr}_E((F^E)^j)\).

The \(j=0\) term is the rank, and (14.31) is precisely the Chern form in (14.29).

Every smooth Hermitian bundle over a compact manifold occurs as such an image. One construction uses a finite trivializing cover, local orthonormal frames, and smooth functions \(\rho_\alpha\) subordinate to it with

\(\sum\rho_\alpha^2=1\).

The map sending a vector to all its local coordinates multiplied by

\(\rho_\alpha\) embeds each fiber isometrically into one fixed finite-dimensional space. Its smooth orthogonal image projection is \(e\).

An arbitrary unitary connection differs from the induced connection by a smooth endomorphism-valued one-form. The two coupled Dirac operators therefore differ by a bounded zero-order operator. Their common Sobolev domain has compact inclusion in \(L^2\); the difference is compact as a map from that domain to \(L^2\). Fredholm stability preserves the index.

The corresponding Chern forms have the same integrals in (14.29).

For a connection path with derivative \(a\), differentiating curvature gives

\(\dot F=\nabla a\); cyclic trace and the Bianchi identity \(\nabla F=0\) give

\[

\frac d{dt}\operatorname{Tr}e^{-F_t/(2\pi i)}

=-\frac1{2\pi i}\,

d\,\operatorname{Tr}\left(a\,e^{-F_t/(2\pi i)}\right).

\tag{14.32}

\]

The tangent-curvature form \(\widehat A(M)\) is closed for the same reason: it is a power series in traces of even curvature powers.

Stokes' theorem on the closed manifold makes the integrated derivative zero.

This proves (14.29) for every stated connection.

It also explains the use of closed forms, rather than merely asserting connection independence.

For the odd formula, insert (14.28) into the pairing (10.3) in [The local index formula](the-local-index-formula.md). In matrix exterior notation,

\[

U^{-1}dU\,dU^{-1}dU\cdots dU^{-1}dU

=(-1)^j A^{2j+1}.

\tag{14.33}

\]

This follows from \(dU^{-1}=-U^{-1}(dU)U^{-1}\), one factor at a time.

The sign \((-1)^j\) cancels that of the odd Chern-cycle coefficient

\((-1)^jj!\). The factor \(\sqrt{2\pi i}\) cancels the pairing normalization. The leading minus in Theorem 10.2 of [The local index formula](the-local-index-formula.md) remains, giving (14.30).

For \(d=1\), the formula is

\(-\frac1{2\pi i}\int U^{-1}dU\), exactly the compression index in Section 2 of [The local index formula](the-local-index-formula.md).

This checks the orientation on a concrete geometric operator.

If \(D\) has a kernel, the proof uses \(D+P_0\), assigning that finite-dimensional space to the positive phase. Using instead the strictly positive projection changes the compression by adjoining a finite-dimensional square block and finite-rank off-diagonal blocks. The square block has index zero and the off-diagonal blocks do not change the index. Thus (14.30) also holds for the strictly positive projection. \(\square\)

## 15. Exercises with complete solutions

**Exercise 1 (basic).** On the one-dimensional metric bundle, take a local diffeomorphism \(\varphi(x)=3x\). Compute its lift in the coordinate \(r\), and check preservation of the quotient metric and density.

**Solution.** The lift is \(x'=3x\), \(r'=r-2\log3\). Thus \(e^{r'}(dx')^2=(e^r/9)(3dx)^2=e^r dx^2\). Its Jacobian is three, while \(e^{r'/2}=e^{r/2}/3\), so the product density is unchanged.

**Exercise 2 (intermediate).** In (1.1), let \(A=B=I\) and \(C\neq0\). Show that the map preserves a triangular structure but need not preserve the orthogonal direct-sum metric associated with the chosen complement.

**Solution.** Its restriction to \(V\) and its map on \(N\) are identities, so it preserves the specified metrics. If \(Cn\neq0\), it sends \((0,n)\) to \((Cn,n)\). The orthogonal direct-sum squared norm increases from \(|n|^2\) to \(|Cn|^2+|n|^2\). Thus that additional metric is not preserved.

**Exercise 3 (intermediate).** In the signature construction, compute the bounded transform of \(V_1SV_1^*\), and prove that the transforms along the unitary path are norm continuous.

**Solution.** Since \(V_\lambda\) commutes with \(\Delta\),
\[
V_\lambda S(1+\Delta)^{-1/2}V_\lambda^*
=\bigl(V_\lambda S V_\lambda^*\bigr)(1+\Delta)^{-1/2}.
\]
At \(\lambda=1\) this is
\(B\Delta^{-1/2}(I-P_0)(1+\Delta)^{-1/2}\).
The fixed bounded operator \(S(1+\Delta)^{-1/2}\) has norm at most one. Norm continuity of \(V_\lambda\) and \(V_\lambda^*\) therefore proves norm continuity of their conjugations. Their value on the harmonic space is zero, and that space remains present.

**Exercise 4 (advanced).** Let \(v=2,n=2\). Compute the homogeneous dimension, the dilation factor for Lebesgue measure, and the inverse of the principal symbol in (4.4).

**Solution.** The homogeneous dimension is six. The two vertical coordinates contribute \(\lambda^2\), and the two transverse coordinates contribute \(\lambda^4\), giving \(\lambda^6\) overall. By (4.5),
\[
q_2(\xi)^{-1}
=\frac{q_2(\xi)}{|\xi_V|^4+|\xi_N|^2}
\qquad(\xi\neq0).
\]
Its weighted degree is \(2-4=-2\). This is an inverse principal symbol; the inverse of a variable-coefficient differential operator also requires lower-order corrections.

**Exercise 5 (intermediate).** For a compactly supported symbol of weighted order \(-1\), prove boundedness from \(H_w^{-2}\) to \(H_w^{-1}\). Does Proposition 5.2 require its kernel to be compactly supported in the input variable as well?

**Solution.** Put \(s=-2,q=-1\) in (5.7): the target is \(H_w^{s-q}=H_w^{-1}\). In Proposition 5.2 only compact output support and the symbol bounds were used. A bounded frequency cutoff makes the kernel Hilbert–Schmidt because its squared integral over all input variables is evaluated by Plancherel; that integral does not require compact input support. Proper support is a separate condition used when assembling an operator on a manifold.

**Exercise 6 (advanced).** On \(\mathbb T^v\times\mathbb T^n\), determine the summability threshold of the multiplier \(r(D)^{-a}\), with \(a>0\).

**Solution.** Upper lattice counting gives \(N(R)\leq CR^{v+2n}\). Conversely, the integer box
\[
|k_V|\leq cR,\qquad |k_N|\leq cR^2
\]
lies in \(r(k)\leq R\) when \(c>0\) is fixed sufficiently small and \(R\) is large. Its number of lattice points is at least \(c'R^{v+2n}\). Thus, up to fixed positive constants,
\(\mu_j(r(D)^{-a})=(j+1)^{-a/(v+2n)}\).
The power series \(\sum_j\mu_j^s\) converges precisely when \(as>v+2n\). At \(as=v+2n\), the positive operator \(r(D)^{-as}\) has logarithmically growing eigenvalue partial sums and belongs to weak \(\mathcal L_1\), while its ordinary trace diverges. The original multiplier \(r(D)^{-a}\) lies at the weak Schatten-\(s\) endpoint; it is the \(s\)-th power whose weak-\(\mathcal L_1\) membership is asserted here. This locates the threshold but does not compute a leading residue coefficient.

**Exercise 7 (advanced).** Take \(v=n=1\), so \(Q_{\mathrm{dim}}=3\). At degree \(q=-5\), list every moment which obstructs a homogeneous extension. Explain why ordinary derivatives of total degree two give the wrong list.

**Solution.** Here \(k=2\) and \([\alpha]=\alpha_V+2\alpha_N\). The possible indices are \((2,0)\) and \((0,1)\). Thus the obstructions are the integrals of \(\theta_V^2a\) and \(\theta_Na\) over \(S_\rho\). Their residue distribution is
\[
R_2(f)=\tfrac12m_{(2,0)}(a)\partial_V^2f(0)
+m_{(0,1)}(a)\partial_Nf(0).
\]
Ordinary total degree two would include \((1,1)\) and \((0,2)\), whose weighted degrees are three and four, and would omit the actual transverse first derivative.

For an explicit test, take \(a(\xi)=\xi_N\rho(\xi)^{-7}\). Its degree is \(-5\). All three ordinary-degree-two moments vanish by reflection symmetry. But
\(m_{(0,1)}(a)=\int_{S_\rho}\theta_N^2\,d\mu_\rho>0\).
Thus its actual obstruction is nonzero, and it has no homogeneous extension. This tests the weighted criterion independently of notation.

**Exercise 8 (intermediate).** Let \(a=\rho^{-Q_{\mathrm{dim}}}\). Determine the sign of the leading logarithm in its smoothed inverse Fourier transform, and explain what can change when the extension of \(a\) at zero changes.

**Solution.** The moment \(c(a)=\int_{S_\rho}d\mu_\rho\) is strictly positive. Formula (7.1) gives a positive coefficient of \(\log(1/\rho(y))\), equivalently a negative coefficient of \(\log\rho(y)\). Within the finite-part extensions satisfying the defect (6.11), an extension changes by a multiple of \(\delta_0\). Its inverse Fourier transform changes by a constant. It cannot change the logarithm. An arbitrary extension could add further derivatives of \(\delta_0\), whose transforms are polynomials; those too are bounded near zero and leave the logarithmic coefficient unchanged.

**Exercise 9 (advanced).** On the flat torus let \(P=\operatorname{Op}(a)\) have order \(-Q_{\mathrm{dim}}\), and suppose its leading homogeneous term \(a_{-Q_{\mathrm{dim}}}(x,\theta)\) has zero mean in \(x\) for every \(\theta\in S_\rho\). Prove that every logarithmic trace of \(P\) vanishes, including when \(a\) is a complex matrix symbol.

**Solution.** Every nonzero Fourier mode in (8.6) has zero trace by translation invariance. The zero mode vanishes by hypothesis. Absolute convergence in (8.7) permits termwise evaluation by the continuous logarithmic trace. Lower-order terms are trace class by (8.2) and also have zero logarithmic trace. No positivity is used in this argument.

**Exercise 10 (advanced).** Let \(f\) have degree \(-Q_{\mathrm{dim}}+2\), and let \(\xi_i\) be a transverse covariable. Prove (8.10) in this case and explain why replacing its degree hypothesis by \(-Q_{\mathrm{dim}}+1\) would invalidate the flux calculation.

**Solution.** A transverse derivative has weight two. Its contraction form \(i_{\partial_{\xi_i}}d\xi\) has degree \(Q_{\mathrm{dim}}-2\). Multiplying by \(f\) makes the boundary flux have degree zero, so it has identical integrals on \(\rho=1\) and \(\rho=R\). Meanwhile \(\partial_{\xi_i}f\) has degree \(-Q_{\mathrm{dim}}\), and its annular integral is logarithmic. The divergence theorem proves its sphere integral is zero. If \(f\) instead had degree \(-Q_{\mathrm{dim}}+1\), the flux would have degree minus one and the derivative degree \(-Q_{\mathrm{dim}}-1\). The two fluxes would have different scaling and the annular integral would no longer be the logarithmic integral used in (8.10).

**Exercise 11 (advanced).** Let \(\chi(\rho)\) be smooth, zero for \(\rho\leq1/2\), and one for \(\rho\geq1\). For \(a_q(\xi)=\chi(\rho(\xi))\rho(\xi)^q\), with \(q\notin\mathbb Z\), compute \(\widetilde L(a_q)\), and check its agreement with the ordinary integral when \(\operatorname{Re}q<-Q_{\mathrm{dim}}\).

**Solution.** Write \(B=\int_{S_\rho}d\mu_\rho\). The exterior remainder in (9.2) is zero, and its only homogeneous term is \(\rho^q\). Therefore
\[
\widetilde L(a_q)=(2\pi)^{-d}B
\left(\int_0^1\chi(r)r^{q+Q_{\mathrm{dim}}-1}\,dr
-\frac1{q+Q_{\mathrm{dim}}}\right).
\]
The inner integral is entire in \(q\), since its integrand vanishes near zero. In the integrable range the exterior ordinary integral is
\(\int_1^\infty r^{q+Q_{\mathrm{dim}}-1}dr
=-1/(q+Q_{\mathrm{dim}})\), proving agreement. At \(q=-Q_{\mathrm{dim}}\), the meromorphic expression has residue \(-(2\pi)^{-d}B\) as a function of \(q\). For the zeta variable \(q=-z-Q_{\mathrm{dim}}\), that sign reverses: the residue at \(z=0\) is \(+(2\pi)^{-d}B\).

**Exercise 12 (advanced).** Suppose \(P\) has order \(q=-Q_{\mathrm{dim}}-1\), and \(W\) satisfies Proposition 9.3. Can \(\zeta_P\) have a pole at zero? What is its value there?

**Solution.** Its possible poles are \(-1,-2,\ldots\), by (9.9), so zero is regular. The operator \(P\) is trace class. In the region near zero, the symbol order of \(PW^{-z}\) remains strictly below \(-Q_{\mathrm{dim}}\). The trace is therefore the ordinary trace there, and \(W^0=I\) gives \(\zeta_P(0)=\operatorname{Tr}(P)\). This need not be zero. Its residue is zero, agreeing with \(\mathcal R(P)=0\); the residue trace and the finite trace value are different coefficients.

**Exercise 13 (intermediate).** Let \(v=n=1\) and \(L(\xi_V,\xi_N)=(\xi_V,\xi_N+c\xi_V)\), with \(c\neq0\). Transform the homogeneous symbol \(a(\eta)=\eta_N\), and explain which derivative produces its lower-order correction.

**Solution.** Its exact transform is
\[
a(L\xi)=\xi_N+c\xi_V.
\]
The first term has weighted degree two, and the second has degree one. The Taylor correction is \(c\xi_V\partial_{\eta_N}a=c\xi_V\). A vertical derivative of \(a\) is zero and cannot produce it. This also illustrates why the shear preserves the leading graded symbol while adding lower degrees.

**Exercise 14 (advanced).** In Proposition 11.2, determine every eigenvalue of \(B'\), prove its strict norm bound, and compute the change in \(\zeta_P(0)\) caused by using an inverse which vanishes on \(\ker Q\).

**Solution.** On a kernel vector, \(B'=0\). On a \(Q\)-eigenvector with nonzero eigenvalue \(\lambda\), it is multiplication by \((1+\lambda^2)^{-1}\). Compact resolvent gives a smallest positive absolute nonzero eigenvalue \(c>0\), so \(\|B'\|\leq(1+c^2)^{-1}<1\). If there are no nonzero eigenvalues the norm is zero. The binomial expansion therefore converges in norm locally uniformly in its exponent. The generalized inverse zeta function is the completed-inverse function minus \(\operatorname{Tr}(PP_0)\). Wherever the former is regular at zero, its value is smaller by that constant; its residues at every point agree. If there is a pole, the same statement holds for the constant Laurent coefficient.

**Exercise 15 (advanced).** On \(\mathbb R\), take \(V=0\), \(Q=-i\,d/dx\) on its Fourier selfadjoint domain, and \(D=\operatorname{sign}(Q)|Q|^{1/2}\). Show that \(Q\) has no spectral gap and that \(f(D-i)^{-1}\) is compact for every \(f\in C_c^\infty(\mathbb R)\). Explain why a nonzero bounded spectral cutoff of \(Q\) need not be compact.

**Solution.** Fourier transformation makes \(Q\) multiplication by \(\xi\); its spectrum is all of \(\mathbb R\). Thus the closed-manifold argument using a positive least nonzero eigenvalue is unavailable.

The multiplier \(A^{-1}=(1+Q^2)^{-1}\) has square-integrable Fourier symbol. Its inverse Fourier kernel \(k\) is therefore in \(L^2\). The kernel \(f(x)k(x-y)\) satisfies
\[
\iint |f(x)k(x-y)|^2\,dx\,dy
=\|f\|_2^2\|k\|_2^2<\infty.
\]
Hence \(fA^{-1}\), and by adjoints \(A^{-1}\bar f\), are compact. The norm approximation in Theorem 12.3 gives \(fA^{-1/4}\) compact. The bounded spectral factor \(g_i(Q)\) then gives \(f(D-i)^{-1}=fA^{-1/4}g_i(Q)\) compact.

For contrast, choose \(g\) nonzero on an interval of positive measure. In Fourier space, multiplication by \(g(\xi)\) is not compact: on a positive-measure subset where \(|g|\geq c>0\), choose an infinite orthonormal sequence. Its images have norm at least \(c\), while the sequence converges weakly to zero. A compact operator would send that sequence to zero in norm. Bounded spectral support alone therefore provides smoothing in the spectral scale, but not global compactness.

**Exercise 16 (advanced).** For the transported realization \(D_2=UDU^{-1}\), derive the formula for \(\delta^2(fU)\), using the mixed derivative in (12.8), and state the domain map which makes the calculation valid.

**Solution.** Set \(L=|D|\), \(L_2=ULU^{-1}\). Since \(L_2U=UL\), first
\[
[L,fU]=(Lf-fL_2)U.
\]
Applying the same identity again gives
\[
\delta^2(fU)=
(L^2f-2LfL_2+fL_2^2)U
=(\partial_{\mathrm{mix}}^2 f)U.
\]
These products can first be computed on the domain of \(L^2\). The map \(U:H_A^s\to H_{A_2}^s\) is an isometry in spectral norms, and compact multiplication compares \(H_{A_2}^s\) back to \(H_A^s\). Lemma 12.2 then extends the mixed commutators as bounded operators and proves the domain preservation needed at each closed-commutator step.

**Exercise 17 (advanced).** On the \(2\pi\)-periodic \(n\)-torus, let
\(P=M_f(1-\Delta_{\mathrm{flat}})^{-n/2}\), where
\(\Delta_{\mathrm{flat}}=\sum_j\partial_{x_j}^2\) and \(f\) is a smooth complex function. Compute its Dixmier trace. What happens for \(f(x)=e^{ix_1}\)?

**Solution.** Its principal symbol is \(f(x)|\xi|^{-n}\). Formula (13.1) gives
\[
\operatorname{Tr}_\omega(P)
=\frac{|S^{n-1}|}{n(2\pi)^n}\int_{\mathbb T^n}f(x)\,dx.
\]
For \(f=e^{ix_1}\), the integral is zero. This also follows directly from translation conjugation in the proof. The trace is zero even though the operator has nonzero singular values: singular values determine the trace on positive operators, and the general trace is obtained by linear extension.

**Exercise 18 (intermediate).** Compute the residue at \(z=1\) of the coefficient zeta function in Example 14.2.

**Solution.** At \(z=1\), the coefficient of order \(-1\) in \(b\) becomes critical. It is \((1-\cos^2\theta)/2\) on the unit circle. Including the spinor rank gives

\[

\operatorname*{Res}_{z=1}\operatorname{Tr}(b\Lambda^{-z})

=2\int_0^{2\pi}\frac{\sin^2\theta}{2}\,d\theta

=\pi.

\]

Thus this single coefficient has both a positive pole at one and a negative pole at minus one.

**Exercise 19 (advanced).** Use the arbitrary-order expansion in the second lesson to explain why a residue index term can involve only positive coefficient-spectrum arguments, even though the full Dirac spectrum can have negative poles.

**Solution.** The coefficient operator \(T_{n,k}\) has order \(q=-n-|k|<0\). Its classical or abstract regular expansion has powers \(\Lambda^\ell\) with integers \(\ell\leq q\). Multiplication by \(\Lambda^{-2z}\) makes their traces \(\zeta_{b_\ell}(2z-\ell)\). At \(z=0\), the coefficient argument is \(-\ell\geq n+|k|>0\). Only arguments at most the summability bound can have a singularity there; all larger ones lie in the initial trace convergence half-plane. Consequently the finite local index formula sees a positive finite interval of the full coefficient spectrum. It does not imply that all other coefficient zeta functions have no negative poles.

**Exercise 20 (advanced).** In dimension four take \(n=2\) and \(k=(1,0)\). Give the filtration degree before and after cancellation, the improved heat estimate, and the half-plane where the small-time Mellin remainder is holomorphic.

**Solution.** The initial degree is \(n+2|k|=4\). The leading commutator with the constant form vanishes, so the degree is at most three. It is now odd, whereas the trace selects exterior degree four. Diagonal parity in Lemma 14.4 gives

\(\operatorname{Str}(P_{2,(1,0)}e^{-tD^2})=O(t^{-1})\).

The Mellin weight in (14.26) is \(t^{z+1}\). Their product is \(O(t^{\operatorname{Re}z})\), integrable for \(\operatorname{Re}z>-1\). Hence there is no residue at zero. The original degree-four bound would have allowed \(t^{-2}\) and a pole; the cancellation and parity remove it.

**Exercise 21 (intermediate).** Compute the degree-four term of \(\widehat A(M)\) using (14.7).

**Solution.** The scalar expansion is

\(w/\sinh w=1-w^2/6+O(w^4)\).

Taking the logarithm and then half the matrix trace gives

\(-\operatorname{tr}(\mathcal R^2)/48\) in exterior degree four for the raw form. Therefore

\[

\widehat A(M)_4

=-\frac{\operatorname{tr}(\mathcal R^2)}

{48(2\pi i)^2}

=\frac{\operatorname{tr}(\mathcal R^2)}{192\pi^2}.

\]

For an untwisted closed spin four-manifold this is the integrand for \(\operatorname{Index}D^+\). There is no degree-two component.

**Exercise 22 (intermediate).** Let \(U:S^1\to U(r)\) be smooth. Express (14.30) through the scalar winding number of \(\det U\), and check a diagonal example.

**Solution.** Differentiating the determinant gives

\((\det U)^{-1}d(\det U)=\operatorname{Tr}(U^{-1}dU)\).

Since \(\widehat A(S^1)=1\),

\[

\operatorname{Index}(PUP)=-\operatorname{wind}(\det U).

\]

For \(U(x)=\operatorname{diag}(e^{2ix},e^{-5ix},1)\), the determinant is \(e^{-3ix}\), so the index is three. The three scalar compressions have indices \(-2,5,0\), whose sum is three.

**Exercise 23 (advanced).** Prove that

\(\operatorname{Tr}(A^{2j+1})\), where \(A=U^{-1}dU\), is a closed form. Explain why its even analogue vanishes.

**Solution.** The Maurer–Cartan identity is \(dA=-A^2\). The graded product rule gives

\[

d(A^{2j+1})

=\sum_{r=0}^{2j}(-1)^r A^r(dA)A^{2j-r}

=-A^{2j+2}.

\]

The alternating sum is one. In the matrix trace, moving one degree-one \(A\) through the other \(2j+1\) factors changes the sign, so \(\operatorname{Tr}(A^{2j+2})=0\). This proves closedness and also the vanishing of every positive even-power trace. The degree-one case includes \(d\operatorname{Tr}A=0\).

**Exercise 24 (intermediate).** On a closed spin surface let a Hermitian line bundle have curvature \(F=-i\omega\), with \(\int_M\omega=2\pi\). Evaluate the twisted index and identify which part of the residue cocycle can supply it.

**Solution.** The tangent form has only its degree-zero component in dimensions at most two, since the first nonconstant \(\widehat A\) term has degree four. Thus

\[

\operatorname{Index}D_E^+

=-\frac1{2\pi i}\int_M F

=1.

\]

The untwisted degree-zero cocycle is zero on a surface. The degree-two cocycle paired with a projection representing the line bundle supplies the index through its Grassmann curvature. This illustrates why a vanishing untwisted degree-zero density does not force all twisted indices to vanish.

## References

- [Connes–Moscovici 1995] Alain Connes and Henri Moscovici, *The local index formula in noncommutative geometry*, Geometric and Functional Analysis 5 (1995), 174–243; [IHÉS preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_19/M_95_19.pdf).
- [Ponge 2008] Raphaël Ponge, [*Heisenberg calculus and spectral theory of hypoelliptic operators on Heisenberg manifolds*](https://arxiv.org/abs/math/0509300), Memoirs of the American Mathematical Society 194, no. 906 (2008).
- [Hilsum–Skandalis 1987] Michel Hilsum and Georges Skandalis, *Morphismes K-orientés d'espaces de feuilles et fonctorialité en théorie de Kasparov*, Annales scientifiques de l'École Normale Supérieure 20 (1987), 325–390; [journal archive](https://www.numdam.org/item/ASENS_1987_4_20_3_325_0/).
- [Carey–Phillips–Rennie–Sukochev 2006] Alan L. Carey, John Phillips, Adam Rennie, and Fedor A. Sukochev, *The local index formula in semifinite von Neumann algebras I: spectral flow*, Advances in Mathematics 202 (2006), 451–516; [open preprint](https://arxiv.org/abs/math/0411019).
- [Jaffe–Lesniewski–Osterwalder 1988] Arthur Jaffe, Andrzej Lesniewski, and Konrad Osterwalder, *Quantum K-theory I. The Chern character*, Communications in Mathematical Physics 118 (1988), 1–14; [journal archive](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-118/issue-1/Quantum-K-theory-I-The-Chern-character/cmp/1104161905.full).
- [Higson 2006] Nigel Higson, *The residue index theorem of Connes and Moscovici*, in Nigel Higson and John Roe (eds.), *Surveys in Noncommutative Geometry*, Clay Mathematics Proceedings 6, American Mathematical Society, 2006, 71–126; [publisher edition](https://www.claymath.org/wp-content/uploads/2022/03/cmip06.pdf).
- [Ponge 2003] Raphaël Ponge, *A new short proof of the local index formula and some of its applications*, Communications in Mathematical Physics 241 (2003), 215–234; [open author preprint](https://arxiv.org/abs/math/0211333).
- [Higher traces](../../NCG-CYCLIC/public/reader/cyclic-cohomology.html#1-what-a-higher-trace-must-satisfy) Open Mathematics Courses, *Cyclic cohomology: traces, differentials and symmetry*, draft lesson, September 2026, Sections 1, 3 and 6–9 (CC0).
- Measured foliation index Open Mathematics Courses, *The index theorem for measured foliations*, draft lesson, September 2026, Lemmas 6.24–6.25 and Theorem 6.26 (CC0).
- [Carey–Rennie–Sedaev–Sukochev 2006] Alan L. Carey, Adam Rennie, Aleksandr Sedaev, and Fedor A. Sukochev, *The Dixmier trace and asymptotics of zeta functions*, [open preprint](https://arxiv.org/abs/math/0611629).
- [Dixmier 1966] Jacques Dixmier, *Existence de traces non normales*, Comptes Rendus de l’Académie des Sciences de Paris, Série A–B 262 (1966), A1107–A1108.
- [Positive spectral calculus](../../elliptic-boundary-reduction/lower-bounded-spectral-calculus.html#the-full-calculus-of-a-bounded-positive-contraction) *Spectral measures with the original operator domain retained*, Elliptic Operators & Boundary Problems, AN03-P005, especially AN03-SPC-001–004; [proof source](../../elliptic-boundary-reduction/src/lower-bounded-spectral-calculus.md). Independently written programme proof, CC0. Sections 1–4 retain the full spectral measure and operator-domain statements.
- [Banach foundations](../../elliptic-boundary-reduction/banach-foundation-bridges.html#hahnbanach-and-scalar-norm-tests) *Banach estimates, quotient spaces and compact parameter arguments*, Elliptic Operators & Boundary Problems, AN03-P004, Sections 4–8, reader-facing draft dated September 2026. Independently written programme proof, CC0. Sections 4–8 include the complete-metric Baire theorem and the full Banach-space consequences.
