# Uniform metric bounds on Hilbert-valued Weyl operators

This companion proves the metric \(L^2\) estimate with constants independent of the coefficient Hilbert spaces. The argument includes the ordered norm-valued calculus, both interaction matrices, the full neighborhood count and all differentiated separated-center estimates. It then proves the symplectic normal form needed for scalar positivity. The source's converse and compactness results and its unrestricted Banach distribution extension are separate selections.

This is a modified selection of AN03-U018, *When a moving symbol scale controls an operator*, from *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Original principal author: AN-03 course-writing task. Original publisher: AN-03 local course project. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Selection, exact prerequisite connections and identified additions: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0. See the rights notice.

## B0. Complete current prerequisites

The [metric Weyl product](../20261005-metric-weyl-calculus/metric-weyl-products.md) proves the compatible-metric calculus and every finite remainder, with the exact phase factor \(16\). The [Schwartz action and covariance proof](../20261005-metric-weyl-calculus/weyl-action-and-covariance.md) supplies all localization, affine division and polynomial counting estimates. The [Gaussian multiplier proof, Sections 2–4 and 7–8](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) gives the compact frozen estimates and all restricted derivatives. Its local off-support estimate has constants independent of the frozen form and phase and does **not** assume a small Planck parameter; this is the estimate used for the mixed frozen forms in Section 6.

[Integration and duality, Section 5 and Sections 17.1–17.3](../20261005-cauchy-foundations/integration-and-duality.md) proves complex Hahn–Banach norm separation, strong measurability, the Bochner integral and complete Bochner \(L^2\), including nonseparable Hilbert spaces. [Hilbert facts T1](../20261004-free-canonical-composition/compactness-and-essential-norms.md#t1-the-hilbert-space-facts-with-proofs) proves representation, bounded adjoints and \(\|A^*A\|=\|A\|^2\). The [measure proofs M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) and [Fourier proofs L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) supply integration, density, Plancherel and tempered distributions. All finite-dimensional and calculus inputs have exact earlier locators in the [proof map](proof-map.json).

**The coefficient spaces and density.** If \(B_2\) is Banach, \(\mathcal L(B_1,B_2)\) is Banach: an operator-norm Cauchy sequence \(T_j\) has pointwise limits \(Tv\), which are linear, bounded by the common norm bound, and satisfy \(\|(T-T_j)v\|\le\liminf_k\|T_k-T_j\|\|v\|\). Taking the supremum over unit vectors proves norm convergence. The space \(\ell^2(I;H)\), for countable \(I\), is complete: a Cauchy sequence has coordinate limits by completeness of \(H\); finite partial square sums give the same norm bound for the limit and for each difference by passage to the limit, and then taking their supremum proves norm convergence. Its inner product is the absolutely convergent coordinate sum, by finite Cauchy–Schwarz and limits:
\[
\|(v_j)\|^2=\sum_j\|v_j\|_H^2,\qquad
((v_j),(w_j))=\sum_j(v_j,w_j)_H.
\tag{MP1}
\]
Finite-valued functions on finite-measure sets are dense in Bochner \(L^2(\mathbb R^n;H)\), by the stated integral construction. For each term \(1_Ev\), scalar compact smooth density replaces \(1_E\) in \(L^2\); the error is exactly \(\|v\|\) times the scalar error. Thus finite sums of compact smooth scalar functions times vectors are dense. This argument uses no countable basis of the ambient \(H\). On their finite-dimensional vector span, Gram–Schmidt and scalar Plancherel show that the Fourier transform is unitary with the stated scalar normalization. Density extends it and its scalar inverse to the whole Bochner space. The explicit symplectic generators (translations, modulations, linear coordinate changes, quadratic phases and Fourier transform) therefore act unitarily there. Their Schwartz continuity follows either from their formulas or by norm separation and the already proved scalar estimates.

We retain the conventions of [Two measuring scales, one Weyl product](../20261005-metric-weyl-calculus/metric-weyl-products.md): \(W=\mathbb R_x^n\times\mathbb R_\xi^n\), \(n\ge1\), \(D=-i\partial\), inverse Fourier factor \((2\pi)^{-n}\), and
\[
 \sigma((x,\xi),(y,\eta))=\xi\cdot y-x\cdot\eta.
 \tag{B1}
\]
A metric is a field of positive quadratic forms \(g_X\), not necessarily a differentiable field. Put \(q_X=g_X^\sigma\). Unless a statement explicitly uses only a frozen form, the metric is slowly varying as in Section 1 of [Localizing symbols with moving metrics](../20261004-free-intrinsic-graph/prerequisites/metric-localization.md) and symplectically temperate:
\[
 q_X(T)\le Cq_Y(T)(1+q_Y(X-Y))^N,
 \qquad g_X\le q_X.
 \tag{B2}
\]
The structural constants include the local comparison radius and constant and the constants in (B2). A weight \(m>0\) is locally \(g\)-continuous and satisfies
\[
 m(Y)\le C_m m(X)(1+q_Y(X-Y))^{N_m}.
 \tag{B3}
\]
For a Banach space \(E\), \(S(m,g;E)\) uses norm derivatives, with
\[
 p_k(a;m,g)=\sup_X m(X)^{-1}
 \sup_{g_X(T_j)\le1}\|\partial_{T_1}\cdots\partial_{T_k}a(X)\|_E.
 \tag{B4}
\]
These spaces have the countable seminorm topology. Here \(p_{\le J}=\max_{0\le j\le J}p_j\), as in the localization lesson; a specified finite range likewise means its maximum. No derivative of \(g\) or \(m\) is part of the definition.

## 1. Coefficient calculus and its domains

Let \(B_1,B_2,B_3\) be complex Banach spaces. Coefficient multiplication from \(\mathcal L(B_2,B_3)\times\mathcal L(B_1,B_2)\) to \(\mathcal L(B_1,B_3)\) has norm at most the product of the input norms. The whole compatible-metric theorem Section 7 of [Two measuring scales, one Weyl product](../20261005-metric-weyl-calculus/metric-weyl-products.md) consequently has the following coefficient version. For this calculus statement use exactly its assumptions on \(g_1,g_2,m_1,m_2\), rather than imposing (B2) separately on the two metrics: neither individual uncertainty nor uncertainty for their mean is added. Set \(g=(g_1+g_2)/2\) and retain its cross parameter \(H\le1\). Then
\[
 a\# b\in S(m_1m_2,g;\mathcal L(B_1,B_3)),
 \quad
 a\# b-\sum_{j<K}C_j(a,b)
 \in S(H^K m_1m_2,g;\mathcal L(B_1,B_3))
 \tag{B5}
\]
for every integer \(K\ge0\). Each target seminorm is bounded by a constant times one finite seminorm of each input. The constants are independent of the Banach spaces. Every \(C_j\) retains the displayed coefficient order; scalar odd-term cancellation cannot be asserted for noncommuting coefficients.

Here is the extension proof, including existence. For compactly supported smooth \(E\)-valued functions, Fourier transforms and inverse transforms are Bochner integrals. Integration by parts gives rapid Fourier decay in the norm of \(E\). Every \(\ell\in E'\), \(\|\ell\|\le1\), commutes with these integrals. Apply Sections 2–4 of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) to \(\ell u\) and take the supremum over \(\ell\). Hahn–Banach gives the norm bounds for the quadratic multiplier, its full finite remainders and its off-support tails. This estimates an already defined Banach vector; no Banach-valued Plancherel identity is assumed.

The localized series in Section 7 of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) converges absolutely in \(E\), since its scalar majorant is summable and \(E\) is complete. The same holds after each prescribed finite collection of derivatives. Its seminorm estimates, bounded-set local-smooth continuity and uniqueness therefore extend to \(E\). For (B5), apply that construction to \(a(Y)b(Z)\), with \(E=\mathcal L(B_1,B_3)\). The derivative norm is bounded by the finite product-rule sum of input derivative norms. The product-metric and weight comparisons of Sections 2–3 of [Two measuring scales, one Weyl product](../20261005-metric-weyl-calculus/metric-weyl-products.md) are unchanged scalar inequalities. Section 8 of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) supplies every remainder with its actual factor \(H^K\). Bounded compactly supported approximation identifies the product with the Schwartz Weyl product. Polynomial termination holds in the membership-qualified form of Section 7 of [Two measuring scales, one Weyl product](../20261005-metric-weyl-calculus/metric-weyl-products.md).

Under (B2)–(B3), these symbols also act continuously as
\[
 a^w:\mathcal S(\mathbb R^n;B_1)\longrightarrow
       \mathcal S(\mathbb R^n;B_2).
 \tag{B6}
\]
The proof Sections 3–4 of [From Weyl symbols to operators and changes of coordinates](../20261005-metric-weyl-calculus/weyl-action-and-covariance.md) uses localized Fourier integrals, division by nonvanishing affine functions, and polynomial counting. Its local Fourier \(L^1\) bound extends to coefficients by the preceding integration-by-parts argument. Plane-wave Weyl operators are translations and scalar modulations, preserving the norm in Bochner \(L^2(B)\), so its localized integral estimates hold there too. The Schwartz topology is equivalent to the increasing norms \(\sum_{|\alpha|+|\beta|\le r}\|x^\alpha D^\beta u\|_{L^2(B)}\). The direct bound follows from rapid decay. For the reverse bound apply scalar Sobolev sup-norm control to \(\ell(x^\alpha D^\beta u)\), use \(\|\ell v\|_2\le\|v\|_{L^2(B)}\), and take the norm-separating supremum. This replaces the scalar Fourier-to-supremum step. The polynomial quotient estimates and convergent localization series now prove (B6), with finite seminorm bounds and bounded-set continuity.

For compactly supported coefficient symbols, Fourier inversion and Fubini give the ordered identity
\[
(a\# b)^w u=a^w b^wu,\qquad
((a^w)^*v,u)=(v,a^wu)
\tag{MP2}
\]
on Hilbert-valued Schwartz vectors, with the adjoint symbol \(a(X)^*\); the second equality states the adjoint relation with the inner product linear in its first entry. These integrals are justified by the norm decay of the Fourier transforms and scalar plane-wave isometries. For general symbols in the stated compatible calculus, the bounded compact approximants converge locally smoothly with uniform symbol seminorms. The action estimate just proved gives convergence on each fixed Schwartz vector. Uniform finite-seminorm estimates give equicontinuity, so products converge on that vector as well: subtract the limit product and split the difference into the changed right input and the changed left operator. The symbol remainders converge by the preceding norm-valued construction. This proves the first identity on Schwartz space. Testing two Schwartz vectors and taking the same limit proves the adjoint-symbol assertion. These are the domains needed below; no general Banach-valued distribution-dual identification is being used.

## 2. A local bound without a preferred ellipsoid

For \(c\in\mathcal S(W;\mathcal L(H_1,H_2))\), with Hilbert coefficient spaces, the plane-wave representation gives
\[
 \|c^w\|\le (2\pi)^{-2n}\int_{W^*}\|\widehat c(\Theta)\|\,d\Theta.
 \tag{B9}
\]
Each wave acts isometrically on spatial \(L^2\), and the coefficient acts with its operator norm. The Bochner integral therefore obeys (B9). Pairing with simple Hilbert-valued Schwartz functions identifies it with quantization; density extends it to all inputs.

The right side is invariant under every invertible affine change of phase variables: the Fourier Jacobian cancels the integration Jacobian. This is a symbol-norm invariance; a nonsymplectic change need not give unitary equivalence of Weyl operators.

For a positive form \(Q\), center \(Z\), and integer \(r>n\), integration by parts in coordinates making \(Q\) Euclidean yields
\[
 \|c^w\|\le C_{n,r}\max_{j\le2r}\sup_X
 (1+Q(X-Z))^{n+1}|c|_{j,Q}(X).
 \tag{B10}
\]
Indeed \(\|\widehat c(\Theta)\|\le(1+|\Theta|^2)^{-r}\|(1-\Delta)^r c\|_{L^1}\). Both \((1+|\Theta|^2)^{-r}\) and \((1+|X|^2)^{-n-1}\) are integrable in dimension \(2n\). Expand the differential operator, bound each derivative by the weighted supremum and integrate. Affine invariance gives (B10) without a determinant, eccentricity or Hilbert dimension in its constant. Fixed-radius compact support is a special case. No uncertainty inequality is needed here.

## 3. Summation with two interaction matrices

Let countably many bounded maps \(A_j:\mathcal H_1\to\mathcal H_2\) satisfy
\[
 \sup_j\sum_k\|A_j^*A_k\|^{1/2}\le M,
 \qquad \sup_j\sum_k\|A_jA_k^*\|^{1/2}\le M.
 \tag{B11}
\]
Then
\[
 \sum_{j,k}|\langle A_ku,A_ju\rangle|\le M^2\|u\|^2.
 \tag{B12}
\]
Finite-subset sums \(\sum_{j\in F}A_ju\) converge in norm, independently of enumeration, to an operator of norm at most \(M\). The assertion holds for every subfamily and for scalar multipliers of modulus at most one.

First restrict to a set of \(d\) indices, choose \(|\alpha_{jk}|\le1\), and put \(T=\sum\alpha_{jk}A_j^*A_k\). A term of \((T^*T)^r\) has \(4r\) letters alternating \(A^*\) and \(A\). One estimate groups them into \((A^*A)\) pairs. Another leaves the first and last letters and groups the interior into \((AA^*)\) pairs. Their geometric mean bounds the word by \(M\) times the square roots of the norms of all \(4r-1\) consecutive paired products. Here \(\|A_j\|\le M\) follows from the diagonal terms of (B11).

Sum from the last index backwards. The two interaction matrices are symmetric, since taking adjoints preserves norm. Each sum contributes at most \(M\); the remaining index has \(d\) choices. Hence
\[
 \|(T^*T)^r\|\le dM^{4r}.
 \tag{B13}
\]
Take \(r\) through powers of two. Iterating \(\|S^*S\|=\|S\|^2\) for the selfadjoint operator \(T^*T\) gives \(\|(T^*T)^r\|=\|T\|^{2r}\). Taking roots and letting \(r\) increase yields \(\|T\|\le M^2\). No unbounded spectral theorem is used.

Choose the finite coefficient matrix to make every quadratic-form term nonnegative. This proves (B12) on finite rectangles; increasing rectangles gives the double-series estimate. The squared norm of a difference of nested finite operator sums is bounded by the tail of that absolutely convergent series with both indices outside the smaller set. Thus the sums are a Cauchy net. Each has norm at most \(M\|u\|\), proving the limit and its bound. The hypotheses survive restrictions and bounded scalar multipliers, proving the remaining statements.

## 5. Counting metric neighborhoods

Choose centers and radii \(0<a<b<c<r_*\), with \(\sqrt2a<b\), such that a partition has support in the \(a\)-balls and the \(b\)- and \(c\)-balls have bounded multiplicity. Sections 2–4 of [Localizing symbols with moving metrics](../20261004-free-intrinsic-graph/prerequisites/metric-localization.md) supplies these gaps by shrinking the initial covering radius. Set
\[
 g_\nu=g_{X_\nu},\quad U_\nu=\{Y:g_\nu(Y-X_\nu)<b^2\},
 \quad d_{\nu\mu}=\inf_{Y\in U_\nu,Z\in U_\mu}q_Y(Y-Z).
 \tag{B17}
\]
The distance is not declared symmetric. Structural constants \(C,L\) satisfy
\[
 1+d_{\mu\nu}\le C(1+d_{\nu\mu})^L,
 \qquad\#\{\mu:d_{\nu\mu}\le t\}\le Ct^L\quad(t\ge1).
 \tag{B18}
\]
Thus, for a sufficiently large exponent, both row and column sums of \((1+d_{\nu\mu})^{-K}\) are uniformly bounded.

For reversal, choose points within a factor two of the infimum after adding one. Temperateness gives \(q_Z(Y-Z)\le Cq_Y(Y-Z)(1+q_Y(Y-Z))^N\). Reverse the ball roles and take infima. Attainment is unnecessary.

For counting fix \(\nu\) and make \(g_\nu\) Euclidean. For every counted \(\mu\), choose \(Y_\mu\in U_\nu,Z_\mu\in U_\mu\) with \(q_{Y_\mu}(Y_\mu-Z_\mu)\le2(t+1)\). Slow variation compares \(q_{Y_\mu}\) to \(q_\nu\). Since \(g_\nu\le q_\nu\), all \(Z_\mu\) lie in a ball of radius \(C\sqrt t\) about \(X_\nu\). Distance-base conversion followed by primal temperateness and local comparison gives
\[
 g_\mu\le Ct^{N(N+1)}g_\nu,
 \tag{B19}
\]
enlarging structural constants if needed. A Euclidean ball about \(Z_\mu\) of radius \(\kappa t^{-N(N+1)/2}\) lies in the \(c\)-ball about \(X_\mu\), for small structural \(\kappa\) depending on \(c-b\). The small balls have bounded multiplicity. Volume comparison in dimension \(2n\) bounds their number by \(Ct^{n(1+N(N+1))}\). Apply this first to finite subcollections to bound the whole set. Dyadic summation proves the row estimate; reversal converts it to the column estimate after increasing the exponent.

The same metric comparisons at points nearly minimizing (B17) give
\[
 g_\mu(T)\le Cg_\nu(T)(1+d_{\nu\mu})^L.
 \tag{B20}
\]
All constants depend only on the fixed radii and structural data.

## 6. Products with separated centers

Let \(a_\nu\in C_c^\infty(W;\mathcal L(H_1,H_2))\) be supported in the \(a\)-ball about \(X_\nu\), with all frozen derivative seminorms uniformly bounded. Then for every \(K\),
\[
 \|(a_\nu^w)^*a_\mu^w\|+\|a_\nu^w(a_\mu^w)^*\|
 \le C_K(1+d_{\nu\mu})^{-K}.
 \tag{B21}
\]
The constant uses finitely many of these seminorms. The same holds for two different controlled families with matching coefficient spaces.

The mixed symbol is the diagonal restriction of the quadratic multiplier applied to \(a_\nu(Y)^*a_\mu(Z)\). For the frozen product form \(g_\nu\oplus g_\mu\), its phase dual is \(16(q_\mu(T)+q_\nu(S))\), by Section 3 of [Two measuring scales, one Weyl product](../20261005-metric-weyl-calculus/metric-weyl-products.md) and the factor \(1/4\) in the actual Weyl phase. The support lies in the product ellipsoid of radius \(\sqrt2a\); its radius-\(b\) enlargement lies inside \(U_\nu\times U_\mu\). The coefficient version of Section 4 of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md), and slow variation within the balls, give arbitrary inverse powers of
\[
 1+\inf_{Y\in U_\nu,Z\in U_\mu}
       \{q_Z(X-Y)+q_Y(X-Z)\}.
 \tag{B22}
\]
For fixed \(Y,Z\), put \(P=Y+Z-X\), and let \(E\) be one plus the expression in braces. The identities \(P-Z=Y-X\), \(P-Y=Z-X\) bound \(q_P(X-Y)\) and \(q_P(X-Z)\) by \(CE^{N+1}\). Comparing the forms at \(Y,Z\) to the form at \(P\), using those controlled distances, bounds \(q_Y(X-Y)+q_Z(X-Z)\) by a fixed power of \(E\). Compare \(q_X\) to these forms once more. Thus
\[
 1+q_X(X-Y)+q_X(X-Z)\le CE^{L_0}.
 \tag{B23}
\]
This is the crossed-distance argument with every distance base retained.

Let \(M(X)=\inf_{Y\in U_\nu}q_X(X-Y)+\inf_{Z\in U_\mu}q_X(X-Z)\). Equation (B23) converts (B22) to arbitrary inverse powers of \(1+M(X)\). Choose points nearly minimizing its two independent infima. The quadratic triangle inequality and temperateness give
\[
 1+d_{\nu\mu}\le C(1+M(X))^{N+1},
 \quad 1+g_\nu(X-X_\nu)\le C(1+M(X))^{N+1}.
 \tag{B24}
\]
For the first use \(q_X(Y-Z)\le2M(X)\), then \(q_Y\le Cq_X(1+q_X(X-Y))^N\). For the second use the triangle inequality through \(Y\), slow variation \(g_\nu\le Cg_Y\), uncertainty \(g_Y\le q_Y\), and the same comparison of \(q_Y\) to \(q_X\). Near-minimizers with an added one cover zero infima.

Each derivative on the diagonal splits between the inputs. A direction normalized by \(g_\nu\) costs a bounded factor on \(a_\nu\) and a fixed power of \(1+d_{\nu\mu}\) on \(a_\mu\), by (B20). At a fixed derivative order the finite loss is absorbed by increasing the off-support exponent. Consequently \(c_{\nu\mu}=a_\nu^*\#a_\mu\) satisfies, for every \(j,K,R\),
\[
 |c_{\nu\mu}|_{j,g_\nu}(X)
 \le C_{j,K,R}(1+d_{\nu\mu})^{-K}
       (1+g_\nu(X-X_\nu))^{-R}.
 \tag{B25}
\]
Apply (B10) with \(R=n+1\) and enough derivatives. This proves the first term of (B21). Apply the identical norm argument to \(a_\nu\#a_\mu^*\), reversing coefficient spaces, for the second. Decay and summability have been established before any global metric \(L^2\) theorem is used.

## 7. Uniform Hilbert-space boundedness

For every metric satisfying (B2), there are \(J,C\), depending only on dimension and structural constants, such that
\[
 \|a^w\|_{L^2(H_1)\to L^2(H_2)}
 \le Cp_{\le J}(a;1,g),\qquad
 a\in S(1,g;\mathcal L(H_1,H_2)).
 \tag{B26}
\]
The Hilbert spaces can be infinite dimensional or nonseparable. Bochner \(L^2\) uses strongly measurable functions; its density and completeness are proved in B0 and the linked integral construction. No countable basis of an entire coefficient space is assumed.

Write \(a=\sum\phi_\nu a\) using Section 4 of [Localizing symbols with moving metrics](../20261004-free-intrinsic-graph/prerequisites/metric-localization.md). Frozen derivative bounds of the pieces are controlled by symbol seminorms. Their individual operators are bounded by (B10). Apply (B21), and then (B18) with an exponent large enough to sum the square roots. This gives (B11) with \(M\le Cp_{\le J}(a;1,g)\). The operator sum converges strongly and obeys (B26). On Schwartz inputs its distributional value is \(a^w\): the finite symbol sums converge locally smoothly in a bounded symbol set, and Section 1 identifies the limit. Density gives the unique extension.

The constants remain uniform over metrics with common structural bounds. In particular they are uniform over all constant positive forms \(Q\le Q^\sigma\), whose local and temperateness constants can be chosen independently of eigenvalues. Some symplectic eigenvalues may tend to zero. For bounded \(m\), the inclusion \(S(m,g)\subset S(1,g)\), with \(p_j(a;1,g)\le\|m\|_\infty p_j(a;m,g)\), gives the corresponding bound.

Taking \(H_2=\ell^2(I;H)\) is allowed. If an operator-valued column \(v(X):H\to\ell^2(I;H)\) and all its derivatives satisfy (B4), then its Weyl operator obeys (B26). A locally finite scalar family with uniformly bounded derivatives and bounded overlap defines such a column: each squared derivative norm is a sum of component squared norms. This coefficient-norm statement does not presume an interchange of infinitely many oscillatory integrals.

## 8. Symplectic axes of a positive form

For every positive quadratic form \(Q\) on \(W\), there is a real symplectic linear map \(T\) and positive numbers \(\lambda_1,\ldots,\lambda_n\), unique up to order, such that
\[
 Q(T(x,\xi))=\sum_j\lambda_j(x_j^2+\xi_j^2),
 \qquad \sup_{V\ne0}\frac{Q(V)}{Q^\sigma(V)}=\max_j\lambda_j^2.
 \tag{B27}
\]
An additional symplectic rescaling gives instead \(\sum_j(x_j^2+\lambda_j^2\xi_j^2)\).

Write \(Q(V)=V^tGV\), \(G>0\), and let \(J\) be the matrix of (B1), so \(J^t=-J\), \(J^2=-I\). The matrix \(K=G^{-1/2}JG^{-1/2}\) is skew-symmetric and invertible. The symmetric positive matrix \(-K^2\) has a unit eigenvector \(e\) with eigenvalue \(\mu^2>0\). Set \(f=Ke/\mu\). Then \(e,f\) are orthonormal, \(Ke=\mu f\), and \(Kf=-\mu e\). Their orthogonal complement is \(K\)-invariant: pairing \(Kv\) with either vector equals minus the pairing of \(v\) with its image. Induction gives an orthogonal matrix \(O\) with
\[
 O^tKO=\begin{pmatrix}0&-D\\D&0\end{pmatrix},
 \qquad D=\operatorname{diag}(\mu_1,\ldots,\mu_n)>0.
 \tag{B28}
\]
Put \(R=\operatorname{diag}(D^{-1/2},D^{-1/2})\), \(T=G^{-1/2}OR\). Direct multiplication gives \(T^tJT=J\) and \(T^tGT=\operatorname{diag}(D^{-1},D^{-1})\), proving the form with \(\lambda_j=\mu_j^{-1}\). The eigenvalues of the intrinsic map \(G^{-1}J\) are \(\pm i\mu_j\), and symplectic coordinate change conjugates this map. This proves uniqueness of the unordered list. In diagonal coordinates \(Q^\sigma=\sum_j\lambda_j^{-1}(x_j^2+\xi_j^2)\), giving the ratio in (B27). Finally the canonical dilation \((x_j,\xi_j)\mapsto(\lambda_j^{-1/2}x_j,\lambda_j^{1/2}\xi_j)\) gives the alternate form. If \(Q\le Q^\sigma\), each \(\lambda_j\le1\).

## B9. Sources and selected scope

The retained AN03-U018 selection contains B1–B6, B9–B13 and B17–B28, with the actual coefficient norm, derivative orders, metric bases and uniform constants unchanged. B0 and MP2 provide explicit current receivers for the functional-analytic steps. The approved mathematical antecedents are Hörmander, *The Analysis of Linear Partial Differential Operators III*, 2007 eBook, ISBN 978-3-540-49938-1, §18.6: the sufficient direction of Theorem 18.6.3, Lemmas 18.6.4–5 and the Hilbert-valued extension (printed 164–169; PDF 179–184). The full proof of the neighborhood count and norm-valued construction is included above. The converse boundedness and compactness theorems are not claimed in this selection.
