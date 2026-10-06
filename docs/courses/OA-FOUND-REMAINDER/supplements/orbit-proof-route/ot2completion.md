<span id="explicit-completion-lemma-for-the-diagonal-tensor-weight-proof"></span>
# Explicit completion lemma for the diagonal tensor-weight proof

This page verifies the root module's application of OT.2. The target equality is valid by the following exact application proof. This supplies the converse completion test that the first version of the root module compressed into a sentence. It uses the existing WH03–08 construction and **WH11**, the actual full finite-ideal/fullness/recovery proof. WH10 proves closability; it does not by itself prove fullness or recovery of the original weight.

<span id="the-right-column-acts-on-the-whole-completed-multiplication-domain"></span>
## The right column acts on the whole completed multiplication domain

Let \(\mathcal C=\mathcal A_\rho\odot\mathcal A_\mu\) be the tensor Hilbert algebra in TG04. On its Hilbert completion write \(p_j\) for left multiplication by \(E_{jj}\otimes1\), \(q_j=Q_j\otimes1\) for the right column projection, and \(r_j=p_jq_j\). SI05 and TG01–04 give, on the entire closed domains,

\[
S q_j=p_jS,\qquad S p_j=q_jS,\qquad
F p_j=q_jF,\qquad F q_j=p_jF.
\tag{C1}
\]

These follow first on the compressed finite-star core, and then by its graph closure; taking adjoints gives the last two identities. Both \(p_j\) and \(q_j\) preserve the appropriate closed domains. On \(\mathcal C\),

\[
L_{q_ja}=L_a p_j.\tag{C2}
\]

Let \(\eta\in\mathcal A_r\), the completed right Hilbert algebra of WH03. For \(a\in\mathcal C\),

\[
L_a(p_j\eta)=L_{q_ja}\eta=R_\eta(q_ja).
\]

The last expression is bounded in \(\|a\|\) by \(\|R_\eta\|\); thus \(p_j\eta\) is right bounded, with

\[
R_{p_j\eta}=R_\eta q_j.
\]

It is in \(D(F)\) by (C1), so it is in \(\mathcal A_r\), not just in the Hilbert completion. Now let \(\xi\in\mathcal B_l\), with bounded left multiplier \(a=\lambda_\xi\). For every \(\eta\in\mathcal A_r\), WH03–04 gives

\[
R_\eta(q_j\xi)=R_{p_j\eta}\xi
=\lambda_\xi(p_j\eta)=a p_j\eta.
\]

The boundedness test defining \(\mathcal B_l\) therefore proves

\[
q_j\xi\in\mathcal B_l,\qquad
\lambda_{q_j\xi}=a p_j.
\tag{C3}
\]

This proves the exact right-column identity for every vector of the completed multiplication domain. It uses neither formal extension of tensor symbols nor a claimed right-ideal property of \(\mathfrak n_\theta\). That finite left ideal need not be a right ideal under arbitrary coefficients.

<span id="a-graph-core-inside-a-full-weight-algebra-has-the-same-full-completion"></span>
## A graph core inside a full weight algebra has the same full completion

The following precise lemma justifies the corner-completion step.

**Lemma.** Let \(\psi\) be an nsf weight in a faithful normal GNS realization. Let \(\mathcal A_\psi=\Lambda_\psi(\mathfrak n_\psi\cap\mathfrak n_\psi^*)\), which is full by WH11. Suppose a left Hilbert algebra \(\mathcal C_0\subseteq\mathcal A_\psi\) has the same product and bounded left action as the ambient algebra, is Hilbert dense, and is a graph core for \(S_\psi\). Then its full completion is \(\mathcal A_\psi\), with the same multiplier map. The associated weight is \(\psi\) on every positive element, including infinite values.

**Proof.** Since the closed sharp operators agree, their adjoints \(F\) agree. Write \(\mathcal A_r^0\) for the completed right algebra obtained from \(\mathcal C_0\), and \(\mathcal A_r^\psi\) for that of the ambient full algebra. Restricting the right-boundedness inequality shows \(\mathcal A_r^\psi\subseteq\mathcal A_r^0\), and their right operators agree on the dense core.

For the other inclusion take \(\eta\in\mathcal A_r^0\), with bounded operator \(R_\eta^0\). Fix \(a\in\mathcal A_\psi\). Choose \(a_n\in\mathcal C_0\) with

\[
a_n\to a,\qquad a_n^\sharp\to S_\psi a
\]

in Hilbert norm. The original right-boundedness test gives

\[
L_{a_n}\eta=R_\eta^0a_n\to R_\eta^0a.
\]

For every \(b\in\mathcal A_r^\psi\), the ambient mixed-product identity WH04 and the adjoint identity give

\[
\begin{aligned}
\langle L_{a_n}\eta,b\rangle
&=\langle\eta,L_{a_n^\sharp}b\rangle
=\langle\eta,R_b^\psi a_n^\sharp\rangle\\
&\longrightarrow\langle\eta,R_b^\psi S_\psi a\rangle
=\langle\eta,L_a^*b\rangle
=\langle L_a\eta,b\rangle.
\end{aligned}
\]

The ambient right algebra is Hilbert dense by RD/WH. Hence \(R_\eta^0a=L_a\eta\). Its norm is at most \(\|R_\eta^0\|\|a\|\). This proves right boundedness for the entire ambient algebra. The common adjoint-domain condition was already satisfied, so \(\eta\in\mathcal A_r^\psi\). The right algebras and their operators coincide exactly. Their left duals, the \(\mathcal B_l\) boundedness tests, and the multiplier maps therefore coincide by WH03. Since the ambient algebra is full, this is precisely its full completion. WH05–06 and WH11's finite-positive criterion now recover every finite value and every infinite value of \(\psi\). No equality inferred only from elementary tensor values is involved. \(\square\)

<span id="apply-the-lemma-to-the-diagonal-tensor-corners"></span>
## Apply the lemma to the diagonal tensor corners

Let \(\theta=\rho\otimes\mu\) be the weight constructed from \(\mathcal C\) by TG04–05, and define the actual restriction

\[
\psi_j(X)=\theta(X),\qquad X\in(p_jM_2(M\bar\otimes N)p_j)_+.
\]

This restriction is faithful and normal. It is semifinite: let \(u_\alpha\uparrow1_M\), \(v_\beta\uparrow1_N\) be the finite positive contraction nets for \(\varphi_j\) and \(\mu\) from WG. Then

\[
E_{jj}u_\alpha\otimes v_\beta\uparrow p_j,
\quad
\theta(E_{jj}u_\alpha\otimes v_\beta)
=\varphi_j(u_\alpha)\mu(v_\beta)<\infty.
\]

Only TG05's already proved elementary positive tensor formula is used here to establish semifiniteness of this restriction. It is not used to identify the restriction on arbitrary positives.

The GNS map of \(\psi_j\) is \(\Lambda_\theta\) restricted to its finite left ideal in the corner. For such a corner element \(x\), left covariance gives \(p_j\Lambda_\theta(x)=\Lambda_\theta(x)\), and (C3) gives \(q_j\Lambda_\theta(x)=\Lambda_\theta(xp_j)=\Lambda_\theta(x)\). Thus its GNS vectors lie in \(r_jH_\theta\). They have dense range there: the original compressed tensor core \(r_j\mathcal C\) is already dense and lies in this GNS range by TG19. The corner representation is faithful and normal, and agrees with the spatial representation of \(M\bar\otimes N\) on \(H_{\varphi_j}\otimes H_\mu\), by SI05/12 and TG03.

The sharp operator of this GNS algebra is a restriction of \(S_\theta\). SI05's exact diagonal corner graph and TG01–04's full tensor graph identify \(r_j\mathcal C\) as a graph core for \(S_\theta|_{r_jH_\theta}\). It follows that this is exactly the closed sharp operator for \(\psi_j\). Under the same Hilbert and algebra identification, \(r_j\mathcal C\) is the algebraic tensor of the finite-star GNS Hilbert algebras for \(\varphi_j\) and \(\mu\), with their actual multiplication and inner product. It is therefore the defining algebraic core of \(\varphi_j\otimes\mu\).

Apply the lemma to \(\mathcal C_0=r_j\mathcal C\subseteq\mathcal A_{\psi_j}\). Its full completion is exactly \(\mathcal A_{\psi_j}\), and hence exactly the completed tensor algebra used to define \(\varphi_j\otimes\mu\). WH's full finite-ideal criterion yields

\[
\theta|_{p_jM_2(M\bar\otimes N)p_j}
=\varphi_j\otimes\mu
\]

on the entire positive cone, including infinite values. This establishes the missing completion identification with both directions of the multiplier test proved.

The rest of OT.2 then follows as written. If \(X\geq0\) has finite \(\theta(X)\), let \(X^{1/2}=\lambda_\xi\). Equation (C3) puts \(X^{1/2}p_j\) in the finite left ideal with vector \(q_j\xi\), so

\[
\theta(p_jXp_j)=\|q_j\xi\|^2,
\qquad \theta(X)=\|q_1\xi\|^2+\|q_2\xi\|^2.
\]

Conversely, finite diagonal values put \(p_jXp_j\) in the finite cone. The bounded polar decomposition of \(X^{1/2}p_j\) and WH06 then put \(X^{1/2}p_j\) in the finite left ideal. If \(\xi_j\) is its unique multiplication vector, (C3) and injectivity give \(q_j\xi_j=\xi_j\). The orthogonal sum \(\xi_1+\xi_2\) is the multiplication vector of \(X^{1/2}\); it has finite norm and the indicated sum of squared norms. Thus \(\theta(X)\) is finite exactly when both diagonal values are finite. If either diagonal value is infinite, the finite case rules out finite \(\theta(X)\); if both diagonal values are finite, the converse rules out infinite \(\theta(X)\). This proves OT.2 without a hidden finite-value restriction.

OT.1 is valid by unitary transport of both multiplication-domain tests and the WH finite-positive criterion. OT.3 is then valid: identify the diagonal tensor weight by OT.2, use TG20–21 on its full polar decomposition, and take the unique \(21\) coefficient of SI65. The orientation is \([D\varphi_2:D\varphi_1]_t\), matching SI14. No analytic/KMS converse or general tensor-cocycle theorem is required for this common-factor law.
