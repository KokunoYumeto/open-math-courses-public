# Half an order from the full boundary form defect

*AN04-U059. Receiving exposition by GPT-6.1 Sol (OpenAI), Ultra; original eligible new expression is CC0-1.0. The writer has checked the stated arguments. Independent review has not occurred.*

The [form-domain lesson](../20261007-restored-boundary-form/boundary-form-localization.md) gave an exact localization defect. Its first estimate used the full energy of the localized solution. We now bound that defect by information half an order below the target. The mechanism is to distribute pseudodifferential orders while keeping ordinary normal derivatives at most once on each factor. We move actual pseudodifferential adjoints across the pairing; we never move an ordinary normal derivative across the boundary.

The [uniform microsupport lesson](../20261007-restored-uniform-microsupport/uniform-microsupport-and-dual-sources.md) supplies the family topology, fixed parametrices and source estimates. The current complete [local boundary action and normal-jet proof](../20261005-local-boundary-calculus/boundary-tests-and-lacunary-symbols.md), [adjoint and ordered composition proof](../20261005-local-boundary-calculus/boundary-adjoints-composition-and-distributions.md), and [L2 and Sobolev bounds](../20261005-local-boundary-calculus/boundary-bounds-and-conormal-action.md) retain AN03-U032 with exact current prerequisite connections. The [positive-order half-space proof](../20261005-positive-boundary-orders/positive-order-halfspace-bounds.md), especially the full integer decomposition (PS4)–(PS5), supplies the order-one map from H1 to L2. The [proper global calculus](../20261005-global-boundary-operators/global-boundary-operator-calculus.md), Sections 2.2–2.4 and 4.1, supplies realization, complete remainders and both ordered parametrices. We use these existing proofs directly.

The proof map binds the exact versions. Elementary inputs are the complete [L2, integration and Cauchy–Schwarz proofs](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md), [Fourier inversion and distributional compatibility](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), [compact smooth cutoffs](../20261004-free-stationary-phase/proof-map.html#U001-A4), and [differential rules and the fundamental theorem](../20261004-free-stationary-phase/proof-map.html#FTC-TAYLOR-COMPACT-PARAMETERS). The periodic example uses the preceding lesson's complete circle H1/antidual proof and its uniform symbol-periodization argument. Every linked component retains its own terms.

## 1. The full form and the scalar localizer hypothesis

Let \(X=[0,\infty)_x\times\mathbb R^{n-1}_z\), with Lebesgue measure, \(D=-i\partial\), and normal index \(n\). Functions may take values in \(\mathbb C^d\), with \(d\) fixed finite. The L2 inner product is linear in the first argument. Choose either \(V=H^1_0(X;\mathbb C^d)\) or \(V=H^1(X;\mathbb C^d)\), with the usual energy norm. Use the complete form

\[
 q(u,w)=\sum_{i,j}(g_{ij}D_ju,D_iw)
       +\sum_j(\ell_jD_ju,w)
       +\sum_i(m_iu,D_iw)+(cu,w),
 \tag{SF1}
\]

where all coefficients are fixed smooth matrices with bounded derivatives on the compact neighborhoods used. They may be complex, and the principal form need not be positive or Hermitian. Their matrix multiplication order is retained throughout.

Let \(\mathcal A=\{A_\lambda\}\) be a family of scalar b-operators acting componentwise on \(\mathbb C^d\), bounded of order \(s\), with common compact kernel support and uniform microsupport in a fixed compact set \(K\). Each individual operator has nonpositive order. This makes all its form-domain and adjoint tests legal, even if its individual order-zero norm grows with the parameter. Fix an elliptic scalar tester \(Q\) of order

\[
 k=s-\tfrac12,\qquad
 \operatorname{WF}'_b(Q)\subset U,
 \quad K\subset U,
 \qquad
 X_k(u)=\|u\|_V+\|Qu\|_V,
 \tag{SF2}
\]

and assume \(u\in V\) and \(Qu\in V\). Here \(U\) is a fixed open cosphere neighborhood. Uniform microsupport has the full meaning established in the preceding lesson: every required off-microsupport rapid-decay and residual seminorm is bounded uniformly. Constants below depend on finitely many of those bounds, finitely many ordinary symbol seminorms, the fixed tester/parametrices, coefficients and support geometry.

### 1.1. The actual distribution actions and fixed support geometry

The weak-H1 identification in U057 and the antidual/density proof in U058 apply componentwise to \(\mathbb C^d\). For the Neumann form space, all ordinary derivatives in this lesson are intrinsic derivatives in the restricted distribution space: differentiate a whole-space extension and then restrict. Two extensions differ by a distribution vanishing in the open half-space, and its derivatives still vanish there, so this is independent of the extension. In particular \(D_xu\) is the L2 weak derivative when \(u\in H^1\). It is not the derivative of an arbitrarily chosen zero extension.

For the Dirichlet form space one may instead use the supported H1 zero extension, established in U058. Its ordinary derivatives are the supported L2 extensions of the intrinsic derivatives: this is true for every compact interior smooth approximant, and convergence of both the functions and their derivatives in L2 proves the identity in the limit. After any higher-order derivative or parametrix, use the exact supported distribution action, retaining all boundary terms. The local quotient-action proof guarantees consistency with the restricted action on the interior. For the L2 outputs occurring here restriction identifies a supported L2 function uniquely, since the boundary has Lebesgue measure zero.

All estimates are made in the fixed compact localization of U058. Localizers and mixed coefficient families have common fixed compact input and output projections there. Auxiliary parametrices have proper support, and \(I\) has its full diagonal support. Properness makes the input/output projections of each finite composition with these localized operators compact. Choose once a smooth cutoff equal to one near their union; the same cutoff works for the entire family. Derivatives hitting it produce only fixed smooth multiplication terms and do not increase the ordinary derivative count. Thus each local norm below is a norm after a fixed cutoff. The proof also gives global norms for proper families when the finite global operator seminorms it uses are uniformly bounded. Properness alone is not a bound on those seminorms.

The scalar hypothesis is consequential. For a matrix coefficient \(h\), the leading symbols of \(hA_\lambda\) and \(A_\lambda h\) agree, giving

\[
 K_{h,\lambda}:=[h,A_\lambda]\in\Psi_b^{s-1}
 \quad\hbox{uniformly},\qquad
 \operatorname{WF}'_b(\{K_{h,\lambda}\})\subset K.
 \tag{SF3}
\]

The complete composition expansion proves this: its order-s multiplication terms cancel; every subsequent term and the exact remainder have order at most \(s-1\), with continuous seminorm bounds. Uniform rapid decay away from \(K\) is preserved by the same expansion. An arbitrary matrix principal localizer need not have this cancellation. Exercise 2 shows that simply dropping this hypothesis makes the conclusion false, even for a positive constant principal form.

## 2. A localization estimate with one ordinary derivative

We use a class of expressions with a b-operator coefficient before each ordinary derivative. For a real number \(r\), write \(T_\lambda\in\mathcal M_r\) to mean a displayed finite expression

\[
 T_\lambda=\sum_{j=1}^n B_{j,\lambda}D_j+C_\lambda,
 \qquad B_{j,\lambda}\in\Psi_b^r,
 \quad C_\lambda\in\Psi_b^{r+1},
 \tag{SF4}
\]

whose coefficient families are bounded at these orders, have common proper supports and uniform microsupport in \(K\). This notation describes ordinary derivatives on the right; it is not an assertion that \(D_x\) is a b-derivative. A lower-order coefficient is allowed. A zero-derivative operator of order \(r+1\) belongs to this class by taking all \(B_j=0\).

**Mixed localization lemma.** If \(T_\lambda\in\mathcal M_k\), then it acts on the distribution \(u\) in (SF2), its value is in L2, and

\[
 \|T_\lambda u\|_{L^2}\leq C_T X_k(u)
 \quad\hbox{uniformly in }\lambda.
 \tag{SF5}
\]

**Proof.** Use the fixed parametrix \(G\in\Psi_b^{-k}\) of \(Q\), with \(GQ=I+E\), where \(E\) has order zero and microsupport disjoint from \(K\). Thus \(u=GQu-Eu\). For a coefficient term,

\[
 B_{j,\lambda}D_jG
 =B_{j,\lambda}G D_j+B_{j,\lambda}[D_j,G].
 \tag{SF6}
\]

The first coefficient is uniformly order zero. The exact tangential commutator has order \(-k\). The exact normal commutator is \(M_G+N_GD_x\), where \(M_G\) has order \(-k\) and \(N_G\) has order \(-k-1\). These are the adopted normal commutator formulas, patched with fixed compact cutoffs if necessary. Consequently the second term in (SF6) has order-zero coefficients, or order-minus-one coefficients before one \(D_x\). All these expressions map \(H^1\) to L2 uniformly, using the order-zero L2 theorem and \(D_j:H^1\to L^2\).

**Patching the normal commutator.** In a localized piece \(\varphi T_a\psi\), apply the product rule on both sides of the exact local identity \([D_x,T_a]=-iT_{\partial_xa}-iT_{\partial_\zeta a}D_x\). Terms differentiating \(\varphi\) or \(\psi\) have order \(m\); the extra term produced by expanding \(D_x\psi\) after \(T_{\partial_\zeta a}\) has order \(m-1\). The sole remaining normal derivative is on the far right with coefficient \(-i\varphi T_{\partial_\zeta a}\psi\) of order \(m-1\). Finite patching on the fixed supports proves the stated \(M_G+N_GD_x\) form, including all cutoff terms. Symbol differentiation and composition with these fixed multipliers preserve rapid decay off the original microsupport. They also preserve the required bounds for all seminorms. The same calculation applies to \(E,A_\lambda,A_\lambda^*\) and retains their individual-order bounds. The identities pass from the correct dense smooth tests to their supported or restricted distribution actions by the earlier transpose/quotient theorem.

The term \(C_\lambda G\) is uniformly of order one. The adopted integer-order identity (PS5) at order one writes it as a sum of order-zero operators before \(D_j\), an order-zero coefficient before \(D_x\) with its actual factor \(x\), and an order-zero remainder. Hence it too maps \(H^1\) to L2 uniformly. This is the positive order-one loss, not an invented regularity gain for a negative b-order.

For the error, expand \(D_jE=ED_j+[D_j,E]\). Separated microsupport makes \(B_{j,\lambda}E\) uniformly residual. It makes the products with the tangential commutator coefficient uniformly residual as well. In the normal direction \([D_x,E]=M_E+N_ED_x\), with the microsupports of both coefficients contained in that of \(E\); both products with \(B_{n,\lambda}\) are therefore uniformly residual. Also \(C_\lambda E\) is uniformly residual. Thus \(T_\lambda E\) has residual b-coefficients before at most one ordinary derivative and maps \(H^1\) to L2 uniformly. Applying these statements to the exact identity \(T_\lambda u=T_\lambda G(Qu)-T_\lambda Eu\) proves (SF5), including membership. No differential adjoint or boundary integration has been used.

The same proof applies to either form space because it only uses the H1 values of \(u\) and \(Qu\). It also proves that a bounded residual-coefficient expression of the form (SF4) maps H1 to L2 using the bare norm \(\|u\|_V\). It does not cover two ordinary normal derivatives on one factor. Exercise 3 shows why the latter distinction cannot be erased by calling a b-coefficient residual.

## 3. Balance the two factors by half an order

Suppose \(F_\lambda\in\mathcal M_{s-1}\) and \(H_\lambda\in\mathcal M_s\). Require every displayed coefficient in their expressions (SF4) to have individual nonpositive order, although the family is measured in its stated uniform order. Thus the individual expressions map \(V\) to L2 and their initial pairing is defined. This individual condition follows automatically from the specified localizers in our application. Then

\[
 |(F_\lambda u,H_\lambda u)|\leq C_{F,H}X_k(u)^2,
 \qquad k=s-\tfrac12.
 \tag{SF7}
\]

**Proof.** Take fixed scalar \(L\) of order \(-\tfrac12\), elliptic near \(K\), and its right parametrix \(L_+\) of order \(\tfrac12\). Write

\[
 LL_+=I+E_L,\qquad
 \operatorname{WF}'_b(E_L)\cap K=\varnothing.
 \tag{SF8}
\]

Left composition changes only the coefficient orders in (SF4), so \(L_+F_\lambda\) and \(L^*H_\lambda\) both belong to \(\mathcal M_k\). The mixed localization lemma bounds their L2 norms by \(C_F X_k\) and \(C_H X_k\). Substituting \(I=LL_+-E_L\) in the first factor gives the exact identity

\[
 (F_\lambda u,H_\lambda u)
 =(L_+F_\lambda u,L^*H_\lambda u)
  -(F_\lambda u,E_L^*H_\lambda u).
 \tag{SF9}
\]

The first term is at most \(C_FC_H X_k^2\). To estimate the second without falsely bounding a higher-order factor separately, write \(F_\lambda=\sum_i B_{i,\lambda}D_i+C_\lambda\). Then

\[
 (F_\lambda u,E_L^*H_\lambda u)
 =\sum_i(D_i u,B_{i,\lambda}^*E_L^*H_\lambda u)
   +(u,C_\lambda^*E_L^*H_\lambda u).
 \tag{SF10}
\]

These adjoint moves are legal L2 identities for each parameter, because the displayed coefficient operators have individual nonpositive order, as required in the lemma. That condition is separate from their formal uniform orders.

Each coefficient of \(E_L^*H_\lambda\) is bounded residual by separated microsupport. Composition on the left with the finite-order families \(B_{i,\lambda}^*\) and \(C_\lambda^*\) keeps all these coefficients uniformly residual. The resulting expressions contain at most one ordinary derivative on their input. The last conclusion of Section 2 bounds their outputs by constants times \(\|u\|_V\). The bare \(D_i u\) and \(u\) in (SF10) are in L2; Cauchy–Schwarz therefore bounds the error by \(C_R\|u\|_V^2\). Taking \(C_{F,H}=C_FC_H+C_R\) proves (SF7). The negative sign in (SF9) is retained. No ordinary derivative has moved to the other factor.

![Figure SF-F1. The two operator paths in SF7–SF10. This is an order and norm diagram, not a Hamilton trajectory. Both balanced expressions have coefficients in M_(s−1/2) and receive the same X_k bound; the separate negative residual correction has a bare energy bound.](figures/sharp-form-half-order.svg)

*Figure SF-F1.* The arrows state the maps used in the complete proof (SF5)–(SF10), with \(k=s-\tfrac12\), \(u\in V\) and \(Qu\in V\). The derivative count in \(\mathcal M_r\) is exactly (SF4). The diagram does not assert ordinary smoothing of a residual b-operator. Vasy's free paper, [PDF pages 24–25](https://math.stanford.edu/~andras/psmcrrb.pdf), motivates the distribution of orders; this form argument and diagram are newly written.

## 4. Every principal and lower-term defect has that form

For the exact commutators of the scalar localizer write

\[
 [D_i,A_\lambda]=M_{i,\lambda}
                  +\mathbf1_{i=n}N_\lambda D_x,
 \quad M_{i,\lambda}\in\Psi_b^s,
 \quad N_\lambda\in\Psi_b^{s-1}.
 \tag{SF11}
\]

In a quantization chart their exact symbols are \(-i\partial_{z_i}a_\lambda\), or \(-i\partial_xa_\lambda\) and \(-i\partial_\zeta a_\lambda\) in the normal direction. The last variable is the compressed normal momentum before quantization. The same formula holds for \(A_\lambda^*\); denote its coefficients by \(\widetilde M_{i,\lambda}\) and \(\widetilde N_\lambda\). These families have the indicated uniform orders and microsupport in \(K\). For every individual parameter, \(M_i,\widetilde M_i\) have nonpositive order and \(N,\widetilde N\) have order at most minus one.

The expansions immediately give

\[
 D_iA_\lambda\in\mathcal M_s,
 \qquad [D_i,A_\lambda]\in\mathcal M_{s-1},
 \qquad A_\lambda\in\mathcal M_{s-1}\subset\mathcal M_s.
 \tag{SF12}
\]

For the last inclusion the zero-derivative coefficient has order \(s\); this is allowed in \(\mathcal M_{s-1}\). All individual expressions just displayed map V to L2. The scalar localizer and its actual adjoint preserve the selected form domain, as proved in the form lesson.

Let \(v=A_\lambda u\). The full defect is the exact expression

\[
 \begin{aligned}
 \Delta_\lambda={}&\sum_{i,j}\big[
 (K_{g_{ij},\lambda}D_ju,D_iv)
 +(g_{ij}[D_j,A_\lambda]u,D_iv)
 -(g_{ij}D_ju,[D_i,A_\lambda^*]v)\big]\\
 &+\sum_j\big[(K_{\ell_j,\lambda}D_ju,v)
                  +(\ell_j[D_j,A_\lambda]u,v)\big]\\
 &+\sum_i\big[(K_{m_i,\lambda}u,D_iv)
                  -(m_iu,[D_i,A_\lambda^*]v)\big]
 +(K_{c,\lambda}u,v).
 \end{aligned}
 \tag{SF13}
\]

We classify all its terms; none of the complex lower coefficients is omitted.

For the finite system, the exact defect identity is valid with the matrix order displayed in (SF13). To check the extension from the preceding scalar notation, use \((v,w)=\sum_a(v_a,w_a)\), expand each matrix product by its finite entry sum, and apply the scalar localizer and its actual adjoint to each entry. The identity \((hAv,w)-(h v,A^*w)=([h,A]v,w)\) uses only the actual L2 adjoint identity, not commutation of \(h\) with any matrix coefficient. The product rule gives the other two terms in each principal summand. The same entry expansion gives both first-order sums and the zero-order term. Every finite interchange is justified by the L2 bounds; Cauchy–Schwarz applies to the full vector norm. Thus all constants can depend on the fixed finite dimension, and no Hermitian or positivity assumption has been added.


For the first principal term, \(K_gD_j\) belongs to \(\mathcal M_{s-1}\) by (SF3), and \(D_iA\) belongs to \(\mathcal M_s\). For the second, multiplication by fixed \(g\) leaves \([D_j,A]\) in \(\mathcal M_{s-1}\); the other factor is again \(D_iA\). Both are covered by (SF7).

For the third principal term, first split its commutator using (SF11), then move only its coefficient adjoint:

\[
 \begin{aligned}
 (gD_ju,\widetilde M_iAu)
     &=(\widetilde M_i^*gD_ju,Au),\\
 (gD_ju,\widetilde N D_xAu)
     &=(\widetilde N^*gD_ju,D_xAu).
 \end{aligned}
 \tag{SF14}
\]

The second line occurs only for \(i=n\). In the first line, the first factor belongs to \(\mathcal M_s\) and the second to \(\mathcal M_{s-1}\); conjugate the pairing to apply (SF7) in its stated orientation. In the second line the orders are already \(\mathcal M_{s-1}\) and \(\mathcal M_s\). Each coefficient adjoint is an actual L2 adjoint. No \(D_x\) is transposed, so no boundary term is lost.

For the \(\ell_j\) terms the first factors \(K_\ell D_j\) and \(\ell[D_j,A]\) lie in \(\mathcal M_{s-1}\); \(A\) is an allowed second factor in \(\mathcal M_s\). For the first \(m_i\) term, \(K_m\) is a zero-derivative coefficient of order \(s-1\), hence is in \(\mathcal M_{s-1}\); pair with \(D_iA\). The remaining \(m_i\) term has the two exact forms

\[
 (mu,\widetilde M_iAu)=(\widetilde M_i^*mu,Au),
 \qquad
 (mu,\widetilde N D_xAu)=(\widetilde N^*mu,D_xAu).
 \tag{SF15}
\]

Their first factors have zero-derivative orders \(s\) and \(s-1\), respectively, so both lie in \(\mathcal M_{s-1}\); their second factors lie in \(\mathcal M_s\). Finally \((K_cu,Au)\) has the same required orders. All coefficient families are bounded with uniform microsupport in \(K\), by composition, differentiation and adjoints. All their individual coefficient operators have nonpositive order, so every adjoint move used above and in (SF10) is legal.

Summing the finitely many balanced-pair constants proves the full sharp defect estimate

\[
 |\Delta_\lambda(u)|\leq C_\Delta X_k(u)^2,
 \qquad k=s-\tfrac12,
 \quad C_\Delta\text{ independent of }\lambda.
 \tag{SF16}
\]

This proof works for Dirichlet and weak Neumann form domains and for the fixed matrix coefficients in (SF1), with the scalar componentwise localizer specified. The estimate controls the complete complex defect, not only its real part.

If \(q(u,w)=\langle f,w\rangle\) for every \(w\in V\), the already legal weak test gives \(q(A_\lambda u,A_\lambda u)=S_\lambda+\Delta_\lambda\). Combine (SF16) with the two complete source bounds of U058. With its notation, one obtains

\[
 |q(A_\lambda u,A_\lambda u)|
 \leq (C_\Delta+C_S/2)X_k^2+(C_S/2)Y_{s+1/2}^2,
 \tag{SF17}
\]

or, under the source-order-s hypothesis, for every \(\epsilon>0\),

\[
 |q(A_\lambda u,A_\lambda u)|
 \leq\epsilon\|A_\lambda u\|_V^2
       +C_\Delta X_k^2+\frac{C_A^2}{4\epsilon}Y_s^2.
 \tag{SF18}
\]

For \(f=0\) the exact source term vanishes, and one obtains the sharper bound \(|q(A_\lambda u,A_\lambda u)|\leq C_\Delta X_k^2\) directly. These inequalities do not assert coercivity of an indefinite wave form; positivity and the justified regularization limit remain separate steps.

## 5. Three graded exercises and full solutions

**Exercise 1 — A nonzero imaginary defect (foundation, 4 points).** On the half-line take \(q(u,w)=\int u'\overline{w'}\), a nonzero real \(\chi\in C_c^\infty((1,2))\), and multiplication \(A=\chi\). Let \(a,t\) be nonzero real numbers. Choose real smooth compact \(\theta\) equal to one near \(\operatorname{supp}\chi\), supported in the interior, and set \(u=\theta e^{(a+it)x}\). Compute the complete complex defect. Explain why a bound only for its real part would miss information in (SF16).

**Solution.** Expanding the two weak derivatives gives the exact identity

\[
 \Delta_A(u)=\int(\chi')^2|u|^2
 +\int\chi\chi'(u\overline{u'}-u'\overline u).
 \tag{SF19}
\]

Every term is supported where \(\theta=1\), so \(u'\overline u=(a+it)e^{2ax}\) there. Compact support of \(\chi\) gives \(\int\chi\chi'e^{2ax}=-a\int\chi^2e^{2ax}\). Hence

\[
 \Delta_A(u)=\int(\chi')^2e^{2ax}
             +2iat\int\chi^2e^{2ax}.
 \tag{SF20}
\]

The second integral is positive, and \(at\ne0\), so the imaginary part is nonzero. The input is compactly supported in the interior and belongs to either form space. All expansions and integrations here concern smooth compact functions, with no boundary contribution. A real-part estimate records the first integral but discards the actual imaginary term. The full coefficient-and-adjoint proof of (SF16) retains both.

**Exercise 2 — Why the leading matrix commutator matters (advanced, 6 points).** On the circle with normalized measure let \(V=H^1(S^1;\mathbb C^2)\), \(q(u,w)=(GDu,Dw)\), and

\[
 G=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
 C=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 A_N=C\langle D\rangle^s\chi(D/N),
 \tag{SF21}
\]

where \(\chi\) is smooth compactly supported in positive frequencies and equal to one near 1. Each \(A_N\) is finite rank and the family is bounded of order \(s\). Test \(u_N=e^{iNy}(1,0)^T\). Compute its defect and show that the conclusion (SF16), with a scalar elliptic tester of order \(s-\tfrac12\), fails for this matrix localizer when \(s=1\).

**Solution.** Put \(w_N=\langle N\rangle\). The matrix \(C\) is self-adjoint and unitary, so \(A_Nu_N=w_N^s e^{iNy}(0,1)^T\) and \(A_N^*A_Nu_N=w_N^{2s}u_N\). Consequently

\[
 q(A_Nu_N,A_Nu_N)=2N^2w_N^{2s},\qquad
 q(u_N,A_N^*A_Nu_N)=N^2w_N^{2s},\qquad
 \Delta_N=N^2w_N^{2s}.
 \tag{SF22}
\]

Take \(Q=\langle D\rangle^{s-1/2}I\). Its energy tester norm gives \(X_k=w_N+w_N^{s+1/2}\). At \(s=1\),

\[
 \frac{|\Delta_N|}{X_k^2}
 =\frac{N^2}{(1+w_N^{1/2})^2}\longrightarrow\infty.
 \tag{SF23}
\]

Thus no uniform \(C_\Delta\) works in this interior periodic model. The exact missing cancellation is \([G,C]\ne0\); it leaves an order-s principal coefficient commutator. All individual localizers here are smoothing and the principal form is positive. Neither fact restores the scalar cancellation. This tests the leading interior matrix algebra, rather than a separate boundary phenomenon. The example does not exclude systems with scalar localizers, which are covered in Section 4; it shows why arbitrary matrix leading symbols require additional hypotheses.

**Exercise 3 — A residual b-operator does not pay for two normal derivatives (advanced, 8 points).** In one normal dimension choose nonzero nonnegative \(h\in C_c^\infty((-1/4,1/4))\), nonzero nonnegative \(\phi\in C_c^\infty((1,2))\), and a smooth compact \(\theta\) equal to one near zero. Let \(R\) have compressed symbol \(\theta(x)\widehat h(\zeta)\), and take \(u_\varepsilon(x)=\varepsilon^{1/2}\phi(x/\varepsilon)\). Prove that \(R\) is a residual lacunary b-operator, that the inputs have bounded energy norm, and that \(\|D_x^2Ru_\varepsilon\|_{L^2}\) diverges.

**Solution.** The Fourier transform of a compact smooth function is Schwartz, by repeated integration by parts. Therefore the compressed symbol has order minus infinity. Its normal Fourier transform is supported in \((-1/4,1/4)\), up to the harmless sign reversal of the double transform; this lies in the lacunary permitted interval. For \(x>0\) the exact inverse Fourier kernel is

\[
 Rv(x)=\theta(x)\int h(t)v(x(1-t))\,dt.
 \tag{SF24}
\]

Indeed the kernel before the substitution is \(x^{-1}h(1-y/x)\), with inverse factor \((2\pi)^{-1}\) in quantization; putting \(t=1-y/x\) cancels the factor \(x^{-1}\). The support of \(h\) keeps \(y=x(1-t)>0\). Proper support is compact here: \(\theta\) bounds \(x\) and \(3x/4<y<5x/4\) bounds the input as well.

Define the fixed smooth compact function

\[
 \psi(r)=\int h(t)\phi(r(1-t))\,dt.
 \tag{SF25}
\]

Its support lies in \([4/5,8/3]\). It is nonnegative and nonzero: choose \(t_0\) and \(v_0\) with \(h(t_0)>0\) and \(\phi(v_0)>0\), and set \(r_0=v_0/(1-t_0)\). Continuity makes the integrand at \(r_0\) positive on an interval about \(t_0\). Differentiation under the compact integral proves smoothness. For all sufficiently small \(\varepsilon\), \(\theta=1\) on the whole output support and

\[
 Ru_\varepsilon(x)=\varepsilon^{1/2}\psi(x/\varepsilon),\qquad
 \|u_\varepsilon\|_{H^1}^2
   =\varepsilon^2\|\phi\|_{L^2}^2+\|\phi'\|_{L^2}^2,
 \qquad
 \|D_x^2Ru_\varepsilon\|_{L^2}
   =\varepsilon^{-1}\|\psi''\|_{L^2}.
 \tag{SF26}
\]

The last norm is nonzero. Otherwise \(\psi''=0\), making \(\psi\) affine on the line, and compact support would force \(\psi=0\), a contradiction. The inputs are interior compact smooth functions for every parameter, hence belong to both form spaces. Their H1 norms stay bounded while the displayed second-derivative norm diverges. This is exactly why the proof keeps ordinary normal derivatives once on each factor and uses residual order-zero bounds rather than an ordinary smoothing claim.

## 6. The remaining propagation steps

The complete form defect now has its lower-order bound (SF16), with every principal and complex lower term included. Together with U058 this proves the full quadratic-form estimates (SF17) and (SF18) at the stated individual regularizer scope, for scalar componentwise localizers on either form domain. The argument also identifies a precise obstruction for noncommuting matrix principal localizers.

The next analytic work must obtain compensated bounds for the actual shrinking glancing symbols, prove a positive normal-energy or commutator estimate in the required region, and justify passage from a chosen family to its limit. Mere boundedness at fixed scales does not control constants as those scales shrink. The analytic empty-window criterion RW4 in [the geometric window lesson](../20261007-restored-parabolic-windows/parabolic-wavefront-windows-and-rays.md) remains unproved here, and the course's full systems, crossings, higher-contact and complex-phase obligations remain active.

## Sources and contribution

The primary route is [András Vasy, Propagation of singularities for the wave equation on manifolds with corners](https://math.stanford.edu/~andras/psmcrrb.pdf), Section 4, especially PDF pages 24–25 within the full Lemmas 4.2 and 4.4 on pages 23–26. The exact admitted copy was read, including those two complete page images. Its argument distributes normal derivatives between two factors. This lesson gives an independent full form-domain argument using only coefficient adjoints, for both form spaces and the fixed complex matrix coefficients with scalar componentwise localizers. The paper's further propagation statements are not used as substitute programme proofs.

The local and global AN-03 components retain their separate CC0 routes and original Claude Opus 5.5 (Anthropic) and Codex contributions. Their approved mathematical antecedent, Hörmander III, 2007 eBook, Section 18.3, remains a valid source and citation. The receiving proof, three complete solutions and original order diagram are by GPT-6.1 Sol (OpenAI), Ultra. The exact current proof connections, explicit distribution/support conventions, patched normal commutator and finite-system identity check are by GPT-6 Astra (OpenAI), Ultra, October 2026. The restored diagram adds absolute-value bars to the bound for the complex pairing; its operator paths, orders and negative residual identity are retained. This independent exposition and diagram are CC0-1.0; linked components retain their own terms. No external book or paper expression or page image is distributed.
