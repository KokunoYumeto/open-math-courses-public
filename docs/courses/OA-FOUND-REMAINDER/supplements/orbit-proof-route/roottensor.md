<span id="tensor-weight-transport-and-cancellation-of-the-common-factor"></span>
# Tensor weight transport and cancellation of the common factor

*Written by GPT-6.1 Sol (OpenAI), Ultra, 5 October 2026. CC0.*

The two tensor-weight identities used in FLOW10 follow from the Hilbert-algebra construction. They use HA/RD, WH03–11, MF05–06, TG01–05, and SI05/12/14 with their stated hypotheses and domains. The existing closed tensor domain is explicitly instantiated in [The tensor-domain formulas and their graph core](../../reader/orbit-proof-route/rootdomain.html). The arguments use precisely those operator-domain, weight and modular results. Hilbert spaces, algebras and indexing sets remain arbitrary. All weights below are normal, semifinite and faithful.

The human antecedents are Takesaki, *Theory of Operator Algebras II*, VIII.3's balanced matrix construction and VIII.4, Definition 4.2 and Proposition 4.3. The tensor product means the weight associated with the **full completion** of the algebraic tensor of the two weight Hilbert algebras, as proved in TG04–05. Matching elementary positive values alone will not be used to identify weights.

<span id="orbit-tensor-transport--naturality-on-the-entire-positive-cone"></span>
## ORBIT-TENSOR-TRANSPORT — Naturality on the entire positive cone

Let \(\beta:M\to\widetilde M\) and \(\gamma:N\to\widetilde N\) be normal unital *-isomorphisms, and let \(\varphi,\mu\) be nsf weights on \(\widetilde M,\widetilde N\). Then for every \(X\in(M\bar\otimes N)_+\), including infinite values,

\[
((\varphi\circ\beta)\otimes(\mu\circ\gamma))(X)
=(\varphi\otimes\mu)((\beta\bar\otimes\gamma)(X)).
\tag{OT.1}
\]

**Proof.** The map

\[
B\Lambda_{\varphi\circ\beta}(x)=\Lambda_\varphi(\beta(x))
\]

is an isometry on the entire finite left ideal, by its GNS norm. It has dense range because \(\beta\) bijects the two finite left ideals, and therefore extends to a unitary. It transports the finite-star algebra bijectively, respecting multiplication, involution and the Hilbert inner product. It intertwines the bounded left multipliers and transports the closed involution with its whole domain, since it transports its graph core. The corresponding map \(C\) for \(\gamma\) has the same properties.

Consequently \(B\otimes C\) is an isomorphism of the two algebraic tensor Hilbert algebras used by TG04. An isomorphism of these algebras transports their full left completions: the definition of a left-bounded vector is a bounded multiplier test, and the adjoint-domain and graph-closure tests are preserved by the unitary. The generated left algebras are related by \(\beta\bar\otimes\gamma\), the normal spatial isomorphism proved in TG03.

WH's finite-positive criterion for the associated weight says that \(A\geq0\) has finite weight exactly when \(A^{1/2}\) is the bounded left multiplier of a vector in the completed left-bounded domain; the value is that vector's squared norm. Transport sends precisely such multiplier vectors to such multiplier vectors, with the same norm, in both directions. Thus it preserves every finite positive value and also which positive elements have infinite value. This proves (OT.1) on the entire positive cone. ∎

In FLOW10 one takes \(\beta\) to be an automorphism of \(M\) and \(\gamma=\mathrm{id}\). This proof includes the full finite domain and all infinite values.

<span id="orbit-tensor-diagonal--a-diagonal-tensor-weight-has-the-prescribed-two-corners"></span>
## ORBIT-TENSOR-DIAGONAL — A diagonal tensor weight has the prescribed two corners

Let \(\varphi_1,\varphi_2\) be nsf on \(M\), let \(\mu\) be nsf on \(N\), and put

\[
\rho([x_{ij}])=\varphi_1(x_{11})+\varphi_2(x_{22})
\quad([x_{ij}]\in M_2(M)_+).
\]

Under the normal spatial identification \(M_2(M)\bar\otimes N=M_2(M\bar\otimes N)\),

\[
(\rho\otimes\mu)(X)
=(\varphi_1\otimes\mu)(X_{11})+(\varphi_2\otimes\mu)(X_{22})
\quad(X\geq0).
\tag{OT.2}
\]

**Proof.** We establish the completed multiplication-domain identity and both directions of the corner-completion test before comparing the positive values.

<span id="the-right-column-acts-on-the-whole-completed-multiplication-domain"></span>
### The right column acts on the whole completed multiplication domain

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
### A graph core inside a full weight algebra has the same full completion

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
### Apply the lemma to the diagonal tensor corners

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

<span id="orbit-tensor-cocycle--cancellation-of-the-common-second-factor"></span>
## ORBIT-TENSOR-COCYCLE — Cancellation of the common second factor

Use the intrinsic balanced-matrix definition of the cocycle proved in SI14. For every real \(t\),

\[
\boxed{[D(\varphi_2\otimes\mu):D(\varphi_1\otimes\mu)]_t
=[D\varphi_2:D\varphi_1]_t\otimes I_N.}
\tag{OT.3}
\]

**Proof.** Set \(\Theta_j=\varphi_j\otimes\mu\). By (OT.2), the diagonal weight \(\Theta_1\oplus\Theta_2\) on \(M_2(M\bar\otimes N)\) is the tensor weight \(\rho\otimes\mu\), under the spatial matrix identification. TG04's full closed-polar construction and MF06 therefore give

\[
\sigma_t^{\Theta_1\oplus\Theta_2}
=\sigma_t^\rho\bar\otimes\sigma_t^\mu.
\]

Apply this equality to \(E_{21}\otimes I_N\). Since the unital modular automorphism fixes \(I_N\), SI14's defining matrix-unit identity gives

\[
\sigma_t^{\Theta_1\oplus\Theta_2}(E_{21}\otimes I_N)
=([D\varphi_2:D\varphi_1]_tE_{21})\otimes I_N.
\]

The same SI14 identity on the left defines \([D\Theta_2:D\Theta_1]_t\) as its unique (21) coefficient. Equality of that coefficient is exactly (OT.3). This proves the same-second-factor tensor law needed in FLOW10, without importing a general tensor cocycle law or an analytic/KMS converse. ∎

For Haar multiplication in FLOW10, \(\mu\) is the nsf integration weight with the GNS map and conjugation proved in `ORBIT-BRIDGE-HAAR-MASA`. Its modular operator is \(I\). This is a particular valid instantiation of (OT.1–3); no sigma-finiteness, invariant original weight or countability hypothesis is added to \(M\) or its Hilbert space.
