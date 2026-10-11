# Fixed modular corners from the whole finite-star graph

New exposition and diagram: GPT-6.1 Sol (OpenAI), Ultra, 2026-10-07. Dedicated under CC0-1.0 to the extent of rights held. Human sources cited below retain their own rights.

Let \(M\ne0\) be any von Neumann algebra, \(\varphi\) a faithful normal semifinite weight, and \(e\ne0\) a projection fixed by \(\sigma^\varphi\). No countability assumption is imposed and \(\varphi(e)\) may be infinite. We prove that the restriction \(\varphi_e\) to \(eMe\) is faithful normal semifinite and
\[
 \sigma_t^{\varphi_e}=\sigma_t^\varphi|_{eMe}.
\]
We identify its entire GNS space and closed modular-operator domains, rather than only an analytic subalgebra.

<svg xmlns="http://www.w3.org/2000/svg" width="1140" height="630" viewBox="0 0 1140 630">
  <rect width="1140" height="630" fill="#f9fbff"/>
  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#254b6d"/></marker></defs>
  <g font-family="Arial, sans-serif" fill="#17344c">
    <text x="50" y="48" font-size="27" font-weight="bold">A fixed corner retains the complete closed modular graph</text>
    <text x="50" y="81" font-size="19">Any faithful normal semifinite weight; e ≠ 0 fixed; φ(e) may be infinite</text>
    <g fill="#e4eef9" stroke="#254b6d" stroke-width="2">
      <rect x="60" y="130" width="350" height="110" rx="10"/>
      <rect x="730" y="130" width="350" height="110" rx="10"/>
      <rect x="60" y="315" width="350" height="110" rx="10"/>
      <rect x="730" y="315" width="350" height="110" rx="10"/>
    </g>
    <g text-anchor="middle" font-size="21">
      <text x="235" y="163">Whole core Λ(A)</text>
      <text x="235" y="194">S₀Λ(x) = Λ(x*)</text>
      <text x="235" y="222">x ∈ N ∩ N*</text>
      <text x="905" y="163">Exact corner core Λ(Aₑ)</text>
      <text x="905" y="194">S₀Λ(exe) = Λ(ex*e)</text>
      <text x="905" y="222">Aₑ = eMe ∩ A</text>
      <text x="235" y="350">Closed S on H</text>
      <text x="235" y="387">Whole D(S) and D(S*)</text>
      <text x="905" y="350">Closed S restricted to qH</text>
      <text x="905" y="387">V Sφₑ V* = S | qH</text>
    </g>
    <g stroke="#254b6d" stroke-width="2.5" marker-end="url(#arrow)" fill="none">
      <path d="M420 185H714"/>
      <path d="M420 369H714"/>
      <path d="M235 246V301"/>
      <path d="M905 246V301"/>
    </g>
    <g text-anchor="middle" font-size="19">
      <text x="570" y="148">q = π(e) Jπ(e)J</text>
      <text x="570" y="174">qΛ(x) = Λ(exe)</text>
      <text x="570" y="219">S₀q = qS₀  (FC2–4)</text>
      <text x="570" y="346">Projected graph cores</text>
      <text x="570" y="409">q reduces S and S*  (FC4)</text>
      <text x="338" y="282">closure</text>
      <text x="1010" y="282">closure</text>
    </g>
    <rect x="60" y="473" width="1020" height="113" rx="10" fill="#e9f3e8" stroke="#3a6a48" stroke-width="2"/>
    <text x="570" y="507" text-anchor="middle" font-size="22">V Δφₑ V* = Δ | qH, with D(Δ | qH) = D(Δ) ∩ qH</text>
    <text x="570" y="541" text-anchor="middle" font-size="22">The implemented group on eMe is exactly σφ restricted to eMe (FC5)</text>
    <text x="570" y="570" text-anchor="middle" font-size="18">Subspace reduction, not equality of the ambient and corner spectra</text>
    <text x="50" y="615" font-size="15">Proof: FC1–5 below. Context: Hiai v1, Lemmas 7.4–7.5, pp.65–67. New figure: CC0.</text>
  </g>
</svg>

The four boxes are actual Hilbert subspaces and closed domains. FC2–4 construct their maps and prove every graph and adjoint reduction. FC5 proves the implemented group identity. The hypotheses allow an infinite corner weight and arbitrary Hilbert space.

The prerequisites are [finite ideals and the complete weight GNS construction, GW1–5](../../OA-FLOW/OA-FLOW-GW.html#oa-flow.gw.1), [ultraweak continuity of normal-weight GNS representations, NF5](../../OA-FLOW/OA-FLOW-NF.html#oa-flow.nf.5), [the finite-star involution and full bounded-vector identity, WR3–5](../../OA-FLOW/OA-FLOW-WR.html#oa-flow.wr.3), [modular implementation for every faithful normal semifinite weight, MW4](../../OA-FLOW/OA-FLOW-MW.html#oa-flow.mw.4), [full closed-involution polar data, CI3](../../OA-FLOW/OA-FLOW-CI.html#oa-flow.ci.3), [uniqueness of the self-adjoint generator, RF5](../../OA-FLOW/OA-FLOW-RF.html#oa-flow.rf.5), and [full spectral covariance, SF](../../OA-FLOW/OA-FLOW-SF.html#oa-flow.sf1.spectral-calculus). The pure Hilbert-algebra normalization and fullification used in this route are proved in [BG1–6](bounded-graph-modular-foundations.md#bg1), including the exact bounded-vector domain identities.

Write \((H,\pi,\Lambda)\) for the complete GNS construction, \(N=\mathfrak n_\varphi\), \(A=N\cap N^*\), \(S=\overline{[\Lambda(x)\mapsto\Lambda(x^*)]_{x\in A}}=J\Delta^{1/2}\), and \(U_t=\Delta^{it}\). Inner products are linear in the first variable. The exact WR4 identity is \(B_l\cap D(S)=\Lambda(A)\), and a vector \(\Lambda(x)\), \(x\in N\), has left multiplier \(\pi(x)\). MW4 and BG1–6 give \(J\pi(M)J=\pi(M)'\).

<a id="fc1"></a>

## FC1. Spectral commutation for the fixed projection

Put \(P=\pi(e)\). Faithful implementation and fixedness give \(U_tPU_t^*=P\). To include the domain implication explicitly, the self-adjoint unitary \(w=2P-I\) commutes with every \(U_t\). If \(L=\log\Delta\), then \(wLw\), with domain \(wD(L)\), is self-adjoint and generates the same group, by full spectral covariance. RF5's uniqueness therefore gives \(wLw=L\), with equality of domains. Spectral covariance now gives commutation of \(w\), and hence \(P\), with every spectral projection of \(L\). Since \(\Delta=\exp L\), \(P\) preserves \(D(\Delta^r)\) and commutes there with \(\Delta^r\) for every real \(r\). In particular it preserves \(D(S)=D(\Delta^{1/2})\).

<a id="fc2"></a>

## FC2. Right multiplication on the whole finite ideal

Let \(x\in A\). The vector \(P\Lambda(x^*)=\Lambda(ex^*)\) is left bounded and lies in \(D(S)\), by FC1 and the left-ideal property. WR4's exact intersection, and injectivity of both the left multiplier and the faithful GNS map, imply \(ex^*\in A\). Its adjoint \(xe\) is therefore in \(A\). On the actual domains,
\[
 \Lambda(xe)=SP\Lambda(x^*)
 =JP\Delta^{1/2}\Lambda(x^*)
 =JPJ\Lambda(x).
 \tag{FC1}
\]
The last step uses \(S\Lambda(x^*)=\Lambda(x)\), so \(\Delta^{1/2}\Lambda(x^*)=J\Lambda(x)\).

For every finite positive \(a\), its square root belongs to \(A\). Equation (FC1) and the projection norm give
\[
 \varphi(eae)=\|\Lambda(a^{1/2}e)\|^2
 \leq \|\Lambda(a^{1/2})\|^2=\varphi(a).
 \tag{FC2}
\]
If \(x\in N\), apply this to \(a=x^*x\). It proves \(xe\in N\), with \(\|\Lambda(xe)\|\leq\|\Lambda(x)\|\). Thus right multiplication by \(e\) extends to a bounded operator on the whole GNS space.

To identify that operator, let \(u_i\uparrow1\) be GW's finite positive contractions. Then \(u_ix\in m_\varphi\subset A\), \(\Lambda(u_ix)\to\Lambda(x)\), and, since \(xe\in N\), \(\Lambda(u_i(xe))\to\Lambda(xe)\). Apply (FC1) to \(u_ix\) and take these Hilbert-norm limits. It follows that
\[
 \Lambda(xe)=R\Lambda(x),\qquad R=JPJ,
 \quad x\in N.
 \tag{FC3}
\]
Here \(R\) is a self-adjoint projection in \(\pi(M)'\). In particular \(P\) and \(R\) commute. This proof of the right-domain statement uses no KMS uniqueness, entire-element core, centralizer trace, or unbounded centralizer-density theorem.

<a id="fc3"></a>

## FC3. The exact corner weight and GNS space

Normality and faithfulness of \(\varphi_e\) follow from restriction: increasing bounded positive corner nets have the same ambient strong supremum. Its precise finite and finite-star domains are
\[
 N_e=eMe\cap N,\qquad A_e=eMe\cap A.
\]
For every \(x\in N\), FC3 and the left ideal give \(exe\in N_e\). GW's semifiniteness proof makes \(N\) ultraweakly dense in \(M\). Compression is ultraweakly continuous: in each summable vector-series coefficient, replace the two vector sequences by their images under e; their squared-norm sums remain finite. Hence compression carries ultraweakly convergent nets to ultraweakly convergent nets. Normal compression therefore makes \(eNe\) ultraweakly dense in \(eMe\). Since \(eNe\subseteq N_e\), GW's finite-ideal criterion proves semifiniteness of \(\varphi_e\). This does not assert that \(e\) itself has finite weight.

Set \(q=PR\). For every \(x\in N\),
\[
 q\Lambda(x)=\Lambda(exe).
 \tag{FC4}
\]
The image of the dense GNS range under \(q\) is therefore exactly \(\Lambda(N_e)\), which is dense in \(qH\). The finite linear extensions of \(\varphi\) and \(\varphi_e\) agree on \(\operatorname{span}N_e^*N_e\), by uniqueness of their extensions from the same finite positive values. Thus
\[
 V\Lambda_e(a)=\Lambda(a),\qquad a\in N_e,
\]
extends to a unitary \(V:H_{\varphi_e}\to qH\). For \(a\in eMe\), \(q\) commutes with \(\pi(a)\) and
\[
 V\pi_e(a)V^*=\pi(a)|_{qH}.
 \tag{FC5}
\]

<a id="fc4"></a>

## FC4. Full graph and adjoint reduction

The projection \(q\) maps the entire initial finite-star domain \(\Lambda(A)\) onto \(\Lambda(A_e)\): FC2 gives the forward inclusion, and \(a=eae\) gives the converse. On that domain,
\[
 S_0q\Lambda(x)=\Lambda(ex^*e)=qS_0\Lambda(x).
\]
Both \(q\) and \(I-q\) preserve the core. Approximating in the graph norm of \(S\) proves \(qD(S)\subseteq D(S)\) and \(Sq=qS\) on \(D(S)\). Projection of the same approximating pairs shows that \(\Lambda(A_e)\) is a graph core for the part of \(S\) on \(qH\). Hence
\[
 VS_{\varphi_e}V^*=S|_{qH}
 \tag{FC6}
\]
with equality of the complete closed domains.

For \(\eta\in D(S^*)\) and \(\xi\in D(S)\), the conjugate-linear adjoint definition gives
\[
 \langle S\xi,q\eta\rangle
 =\langle Sq\xi,\eta\rangle
 =\langle S^*\eta,q\xi\rangle
 =\langle qS^*\eta,\xi\rangle.
\]
Thus \(q\eta\in D(S^*)\) and \(S^*q=qS^*\). The complementary projection gives the second reducing summand. The adjoint of \(S|_{qH}\) is precisely \(S^*|_{qH}\): an adjoint pairing bounded only on \(qD(S)\) is bounded on all \(D(S)\), because its pairing on \((I-q)D(S)\) vanishes. This proves the converse domain inclusion as well.

Taking adjoint products in (FC6), with those full domains, gives
\[
 V\Delta_{\varphi_e}V^*=\Delta|_{qH},\qquad
 D(\Delta|_{qH})=D(\Delta)\cap qH.
 \tag{FC7}
\]
The same identities show \(q\) reduces \(\Delta\). Resolvents and spectral calculus consequently restrict to \(qH\), so
\[
 V\Delta_{\varphi_e}^{it}V^*=U_t|_{qH}
\]
on the whole Hilbert space \(qH\), and all real powers have the corresponding restricted spectral domains. No statement about equality of the ambient and corner spectra is made here.

<a id="fc5"></a>

## FC5. The actual restricted modular group

For \(a\in eMe\), fixedness of \(e\) makes \(\sigma_t^\varphi(a)\in eMe\). Under (FC5) and (FC7), faithful implementation gives
\[
 V\pi_e(\sigma_t^\varphi(a))V^*
 =U_t|_{qH}\,V\pi_e(a)V^*\,U_t^*|_{qH}
 =V\pi_e(\sigma_t^{\varphi_e}(a))V^*.
\]
The corner weight is faithful normal semifinite by FC3, so MW4 applies with exactly the same generality. Faithfulness of \(\pi_e\) proves the claimed equality of groups for every \(t\in\mathbb R\).

For the balanced matrix weight of BC1, its diagonal fixed projection is \(E_{ii}\), and its restricted weight is exactly \(\varphi_i\), on the whole positive cone. BC2 already identifies the part of its closed involution on coordinate \((i,i)\) with \(S_{\varphi_i}\) and its modular operator with \(\Delta_{\varphi_i}\). Applying the same implemented identity, or FC5 directly, gives \(\sigma_t^\Theta(xE_{ii})=\sigma_t^{\varphi_i}(x)E_{ii}\). This supplies BC14 at arbitrary-weight scope. More generally BC13 follows for every finite submatrix, since BC1 identifies its restricted weight with the corresponding balanced weight.

## Human sources and mathematical applications

[Rieffel and Van Daele, 1977, §5 and appendix](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf) provide the freely readable general Hilbert-algebra method developed in BG1–6. [Hiai, arXiv:2004.02383v1, Lemmas 7.4–7.5, pp.65–67](https://arxiv.org/pdf/2004.02383v1#page=65) provides the balanced diagonal spectral implementation context. [Combes, Theorems 2.11 and 2.13, pp.53–57](https://www.numdam.org/item/CM_1971__23_1_49_0.pdf#page=6) provides the canonical-weight and reverse Hilbert-algebra context; the corresponding full finite-ideal and bounded-vector statements are proved in the GW/NF/WR/MW prerequisites above.

For the modular comparison in [MG2](../../OA-FLOW/OA-FLOW-MG.html#oa-flow.mg.2), FC1–5 supply the fixed-corner restriction step. For [balanced weights, BC1–3](../../OA-FLOW/OA-FLOW-BC.html#oa-flow.bc.1), FC5 supplies the exact diagonal and finite-submatrix restrictions. The [all-weight intersection in MG0–4](../../OA-FLOW/OA-FLOW-MG.html#oa-flow.mg.4) also uses its finite-ideal filters, every-weight comparison and type III corner transport; it retains all faithful normal semifinite weights and its stated separable-predual factor scope.

Return to the periodic CAR application.
