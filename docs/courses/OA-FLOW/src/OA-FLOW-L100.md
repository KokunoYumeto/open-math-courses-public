# Invariant weights realize the action spectrum

An invariant faithful normal semifinite weight gives a strongly continuous unitary implementation of an LCA action on its entire GNS space. We prove continuity from the closed GNS graph, pass every integrable filter through that graph, and identify the actual annihilator ideals.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.stdwt.contract"></a>

## The complete GNS implementation and its continuity

Let \(G\) be an arbitrary locally compact Hausdorff abelian group, written additively, and let \(\alpha:G\to\operatorname{Aut}(M)\) be a point-ultraweakly continuous action by normal automorphisms of a von Neumann algebra. Suppose \(\varphi\) is faithful, normal and semifinite and
\[
 \varphi\circ\alpha_s=\varphi\quad(s\in G).
 \tag{W1}
\]
Use [GW1–4](OA-FLOW-GW.md#oa-flow.gw.1) for the full GNS construction:
\[
 N_\varphi=\{x:\varphi(x^*x)<\infty\},\qquad
 \Lambda:N_\varphi\to H_\varphi,\qquad
 \overline{\Lambda(N_\varphi)}=H_\varphi .
 \tag{W2}
\]
Faithfulness makes \(\Lambda\) injective. Semifiniteness makes \(N_\varphi\) ultraweakly dense, by GW4 and \(\mathfrak m_\varphi\subset N_\varphi\). Invariance preserves \(N_\varphi\) and its GNS norm. Polarization therefore gives a well-defined linear isometry on its dense image by
\[
 U_s\Lambda(x)=\Lambda(\alpha_s(x)).
 \tag{W3}
\]
It extends to a unitary, since the map for \(-s\) is its inverse. The group law follows on this dense image and hence on the whole Hilbert space.

We prove strong continuity without assuming an implementation theorem. Fix \(x\in N_\varphi\) and a net \(s_i\to0\). The operators \(\alpha_{s_i}(x)\) converge ultraweakly to \(x\), with the common norm bound \(\|x\|\). The vectors \(\Lambda(\alpha_{s_i}(x))\) have constant norm \(\|\Lambda(x)\|\). The Hilbert ball is weakly compact by [CV3](OA-FLOW-CV.md#cv-3). Every weak cluster subnet thus has a weak limit \(\eta\). The bounded graph
\[
 \{(y,\Lambda(y)):y\in N_\varphi,\ \|y\|\leq\|x\|\}
\]
is closed for ultraweak times Hilbert weak topology by [EW3](OA-FLOW-EW.md#ew-3), so necessarily \(\eta=\Lambda(x)\). Consequently the whole vector net converges weakly to \(\Lambda(x)\): otherwise a subnet outside a fixed weak neighborhood would, by compactness, have a cluster point outside that neighborhood's interior, contradicting uniqueness. Equivalently, take the closed complement of the neighborhood before extracting the subnet. The constant norms then give
\[
 \|U_{s_i}\Lambda(x)-\Lambda(x)\|^2
 =2\|\Lambda(x)\|^2-2\operatorname{Re}
       \langle U_{s_i}\Lambda(x),\Lambda(x)\rangle\longrightarrow0.
 \tag{W4}
\]
Density and the unitary norm bound extend this to every Hilbert vector. The group law gives continuity at every \(s\). This proves the full strongly continuous unitary representation for arbitrary \(G\), without separability or a finite total weight.

This is also the canonical standard implementation. First, on the dense GNS vectors,
\[
 U_s\pi_\varphi(a)U_s^*\Lambda(x)=\Lambda(\alpha_s(a)x)
                              =\pi_\varphi(\alpha_s(a))\Lambda(x).
 \tag{W4a}
\]
The finite-star algebra \(N_\varphi\cap N_\varphi^*\) is invariant under \(\alpha_s\) in both directions, and \(U_s\Lambda(x^*)=\Lambda(\alpha_s(x)^*)\). Consequently \(U_s\) commutes on that core with the Tomita involution. Passing to its closed graph, supplied by [WR4](OA-FLOW-WR.md#oa-flow.wr.4), gives commutation with the full closed \(S=J\Delta^{1/2}\). Conjugating its adjoint by \(U_s\) gives commutation with \(S^*\), hence with \(S^*S=\Delta\). The spectral and polar decomposition uniqueness proved in the earlier weight construction and [SF](OA-FLOW-SF.md#oa-flow.sf.sf1) then give commutation with \(J\) and the full spectral powers of \(\Delta\).

The cone \(C_l=\overline{\{\Lambda(a):a\geq0,\ \varphi(a)<\infty\}}\) from [NC2](OA-FLOW-NC.md#oa-flow.nc.2) is preserved in both directions by \(U_s\). [NC3–4](OA-FLOW-NC.md#oa-flow.nc.3) identifies the natural cone as \(P=\overline{\Delta^{1/4}C_l}\) with the indicated full spectral domains and proves the standard-form axioms. Thus \(U_sP=P\). Together with (W4a) and commutation with \(J\), these are precisely the canonical implementation conditions of [NR1](OA-FLOW-NR.md#oa-flow.nr.1). Its uniqueness identifies this GNS implementation with the standard one. Invariance of the weight, rather than a choice of cyclic vector, produced the implementation.

<a id="oa-flow.stdwt.filter"></a>

## Every integrable filter preserves the full finite ideal

Use the positive convention \(f(p)=\int_G a(s)p(s)\,ds\) for \(a\in L^1(G)\), as in [AF0](OA-FLOW-AF.md#af-0). Define
\[
 \alpha_f(x)=\int_Ga(s)\alpha_s(x)\,ds,\qquad
 U_f\xi=\int_Ga(s)U_s\xi\,ds .
 \tag{W5}
\]
[AT3](OA-FLOW-AT.md#oa-flow.at.3) proves norm-continuous predual orbits for \(\alpha\); [BS1](OA-FLOW-BS.md#bs-1) supplies its normal integrated map. [L24](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) supplies the Hilbert vector integral. Both operators have norm at most \(\|a\|_1\). We claim
\[
 \alpha_f(x)\in N_\varphi,\qquad
 \Lambda(\alpha_f(x))=U_f\Lambda(x)\quad(x\in N_\varphi).
 \tag{W6}
\]

First let \(a\in C_c(G)\), with compact support \(C\), and fix \(x\in N_\varphi\). For any finite set of normal functionals and any positive error, continuity gives a finite open cover of \(C\) on whose individual sets all chosen scalar orbits \(s\mapsto\omega(\alpha_s(x))\) and the one Hilbert orbit \(s\mapsto U_s\Lambda(x)\) have oscillation below that error. This follows by taking small neighborhoods at each point and a finite subcover. Make a disjoint Borel partition \(E_j\) subordinate to that cover, omitting empty cells, and choose \(s_j\in E_j\). Set
\[
 c_j=\int_{E_j}a(s)\,ds,\qquad
 x_{\mathcal P}=\sum_jc_j\alpha_{s_j}(x).
 \tag{W7}
\]
The norm bound is \(\|x_{\mathcal P}\|\leq\|a\|_1\|x\|\), and every such finite sum belongs to \(N_\varphi\). By (W3),
\[
 \Lambda(x_{\mathcal P})=\sum_jc_jU_{s_j}\Lambda(x).
\]
The scalar and vector errors against their respective integrals are each bounded by the oscillation times \(\|a\|_1\). Direct these choices by enlarging the finite set of functionals and decreasing the error. Thus \(x_{\mathcal P}\to\alpha_f(x)\) ultraweakly and
\(\Lambda(x_{\mathcal P})\to U_f\Lambda(x)\) in Hilbert norm. EW3's bounded graph closedness proves (W6).

For an arbitrary \(a\in L^1(G)\), choose \(a_n\in C_c(G)\) converging in \(L^1\), by the Haar approximation theorem in [L24](OA-FLOW-L24.md#oa-flow.grp.translations). The integrals satisfy
\[
 \|\alpha_{\widehat{a_n}}x-\alpha_fx\|
 \leq\|a_n-a\|_1\|x\|,\qquad
 \|U_{\widehat{a_n}}\Lambda(x)-U_f\Lambda(x)\|
 \leq\|a_n-a\|_1\|\Lambda(x)\|.
 \tag{W8}
\]
Their operator norms remain bounded. Apply EW3 once more, now using norm convergence on both sides. This proves (W6) on the entire finite ideal and gives
\[
 \|\Lambda(\alpha_f(x))\|\leq\|a\|_1\|\Lambda(x)\|.
 \tag{W9}
\]
Every application of the unbounded GNS map has been justified by its closed graph.

<a id="oa-flow.stdwt.ideals"></a>

## Equality of annihilator ideals and spectra

Let
\[
 I_\alpha=\{f:\alpha_f=0\},\qquad I_U=\{f:U_f=0\}
 \tag{W10}
\]
be the closed annihilator ideals in \(A(\widehat G)\), with the same transform convention. If \(\alpha_f=0\), (W6) makes \(U_f\) vanish on the dense set \(\Lambda(N_\varphi)\), so \(U_f=0\). Conversely, if \(U_f=0\), (W6) and faithfulness give \(\alpha_f(x)=0\) on \(N_\varphi\). This ideal is ultraweakly dense and \(\alpha_f\) is normal, so \(\alpha_f=0\) on \(M\). Therefore
\[
 I_U=I_\alpha,\qquad
 \boxed{\operatorname{Sp}(U)=\operatorname{Sp}(\alpha)} .
 \tag{W11}
\]
The spectral equality follows by taking hulls, according to the definitions and integrated-action results of BS. No identification of an arbitrary closed ideal with all the functions vanishing on its hull is used.

For \(G=\mathbb R\), [RF5](OA-FLOW-RF.md#rf-5) also gives the unique full self-adjoint generator \(A\) of \(U_t=e^{itA}\). The domain and scalar interchange there identify \(U_f=f(A)\); together with (W6) this locates every integrable spectral filter on the GNS space. For \(M=0\), the GNS space is zero and both action spectra are empty.

**Example.** Let \(M=M_2(\mathbb C)\), \(\varphi=\operatorname{Tr}\), and \(\alpha_t=\operatorname{Ad}\operatorname{diag}(1,e^{i\omega t})\). The GNS Hilbert space is the matrix space with the Hilbert–Schmidt norm. Its vectors \(e_{11},e_{22},e_{12},e_{21}\) have frequencies \(0,0,-\omega,\omega\), respectively. For a filter \(f\), both actions multiply these four vectors by \(f(0),f(0),f(-\omega),f(\omega)\). Smooth cutoffs detect each distinct frequency, so both spectra are \(\{0,-\omega,\omega\}\), with repetitions removed. The formulas remain valid at \(\omega=0\).

The mathematical source is Takesaki, *Theory of Operator Algebras II*, Proposition XI.1.24, printed p.329 ([edition](https://doi.org/10.1007/978-3-662-10451-4)). The precise weight hypotheses and full-domain GNS argument are stated and proved above.
