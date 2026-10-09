<span id="the-commutant-action-and-its-modular-prerequisite"></span>
# The commutant action and its modular prerequisite

The standard coefficient-Hilbert-algebra proof computes the commutant of a standard regular crossed product. Its decisive input is the closed polar decomposition of the coefficient Hilbert algebra and the general Hilbert-algebra commutant theorem. We apply that theorem directly, retain the separate identification of the associated weight, and then turn the commutant itself into a regular crossed product. Two elementary unitaries make the passage explicit: inversion exchanges the right and left regular actions, and pointwise canonical implementation untwists the coefficient algebra.

*Written in Codex (OpenAI), September 2026. This lesson is dedicated under CC0.*

<span id="binding-the-modular-correspondence-contract"></span>
## Transporting the closed modular involution

Let \(\mathcal A\subseteq\mathcal H\) be a left Hilbert algebra with closed involution \(S=\overline{a\mapsto a^\sharp}\), left von Neumann algebra \(N\), and associated n.s.f. weight \(\Phi\). The weight identification in (A6) of lesson 14 is stronger than an isometry between two spaces of initial vectors: it requires a unitary \(I:H_\Phi\to\mathcal H\) intertwining both the whole representation and the **closed** Tomita operators, with their domains.

OA-MOD-WH-03 proves that the original algebra is a graph core for the involution on its full left completion. OA-MOD-WH-05–07 constructs the associated n.s.f. weight with its exact finite ideal. OA-MOD-WH-08 gives the surjective canonical GNS unitary, identifies the full finite-star algebra under it, and identifies the closure of that algebra's involution with \(S\). For this associated weight, WH-08 and the graph-core preservation in WH-03 already identify the closure of the transported finite-star involution. Thus the two operators have the same transported graph, not merely the same action on a smaller algebra:

$$I\pi_\Phi(y)I^*=y\quad(y\in N),\qquad
  IS_\Phi I^*=S. \tag{C1}$$

OA-MOD-MF-05 proves \(JNJ=N'\) for the polar conjugation \(J\) of \(S\), and OA-MOD-MF-06 constructs the modular automorphism group with

$$\pi_\Phi(\sigma_t^\Phi(y))
   =\Delta_\Phi^{it}\pi_\Phi(y)\Delta_\Phi^{-it}
   \quad(y\in N,\ t\in\mathbb R). \tag{C2}$$

Thus (C1) binds the exact content of (A6), while (C2) binds (A7) of lesson 14. For the commutant calculation of lesson 75, one can apply MF-05 directly to the coefficient left Hilbert algebra: `OA-FLOW.DW.LEFTHILBERT` identifies its generated algebra as P, and `OA-FLOW.DW.INVARIANTCORE`, M25, identifies its closed polar conjugation as \(\mathcal J\). WH-03–04 are the full-completion inputs internal to MF-05. This route gives \(\mathcal J P\mathcal J=P'\) before reconstructing the associated dual weight. WH-05–08 and (C1) remain the separate weight/GNS identification; WH-10 remains relevant where an arbitrary original weight is converted to its full Hilbert algebra. MF-06 is needed for the modular *action* formulas in lesson 14.

The arguments use the stated arbitrary-Hilbert-space and n.s.f.-weight hypotheses. The operator, graph-core and weight constructions are proved in [Building the two multiplication actions of a Hilbert algebra](../../reader/orbit-proof-route/ha.html), [Recovering the commutant from right-bounded vectors](../../reader/orbit-proof-route/rd.html), [Weights and the Hilbert spaces of multiplication](../../reader/orbit-proof-route/wh.html) and [The modular group and its analytic algebra](../../reader/orbit-proof-route/mf.html).

<span id="inversion-converts-right-translations-to-left-translations"></span>
## Inversion converts right translations to left translations

Keep the notation of lesson 75. On \(L^2(G,K)\), define the unitary inversion operator

$$[C\xi](s)=\Delta_G(s)^{-1/2}\xi(s^{-1}). \tag{C3}$$

The inversion formula for a left Haar measure gives \(C^2=1\) and \(\|C\xi\|_2=\|\xi\|_2\). It acts on the group coordinate only, so it commutes with every constant coefficient \(y\otimes1\). The modular factor in (C3) is needed when \(G\) is nonunimodular. Applying \(C\), then the right regular operator \(R_g\) of (I1), then \(C\) again gives

$$\begin{aligned}
[CR_gC\xi](s)
 &=\Delta_G(s)^{-1/2}\Delta_G(g)^{1/2}
   \Delta_G(s^{-1}g)^{-1/2}\xi(g^{-1}s)\\
 &=\xi(g^{-1}s)=[\lambda_g\xi](s).
\end{aligned}\tag{C4}$$

The second equality uses \(\Delta_G(s^{-1}g)=\Delta_G(s)^{-1}\Delta_G(g)\). In particular, inversion exchanges the right and left regular representations with the same group label \(g\); no inverse label remains. Apply \(C\) to the commutant formula (I5):

$$C P'C
  =\bigl(M'\otimes1\ \cup\ \{U_g\otimes\lambda_g:g\in G\}\bigr)''.
  \tag{C5}$$

<span id="untwisting-the-commutant-action"></span>
## Untwisting the commutant action

The canonical standard-form implementers \(U_g\) preserve \(M'\). They define a point-ultraweakly continuous action

$$\alpha'_g(y)=U_g y U_g^*\qquad(y\in M'). \tag{C6}$$

Strong continuity of \(U\) proves the asserted continuity by testing matrix coefficients. Let \(\pi_{\alpha'}\) be the regular coefficient representation of this action, and define a multiplication unitary on \(L^2(G,K)\) by

$$[W\xi](s)=U_s\xi(s). \tag{C7}$$

The inverse is pointwise multiplication by \(U_s^*\). For \(y\in M'\), the regular coefficient at \(s\) is \(U_s^*yU_s\). Directly,

$$W\pi_{\alpha'}(y)W^*=y\otimes1. \tag{C8}$$

For \(g\in G\), the group representation law gives \(U_sU_{g^{-1}s}^*=U_g\). Hence

$$[W\lambda_g W^*\xi](s)=U_g\xi(g^{-1}s)
     =[(U_g\otimes\lambda_g)\xi](s). \tag{C9}$$

Equations (C5), (C8), and (C9) now identify the standard commutant with the regular crossed product of the commutant action:

$$\boxed{\displaystyle
  W^*CP'CW=M'\rtimes_{\alpha'}G.} \tag{C10}$$

The isomorphism is concrete and generator-level. It sends \(y\otimes1\) in (I5) to \(\pi_{\alpha'}(y)\), and \(U_g\otimes R_g\) to \(\lambda_g\). This proves the standard-form case of the source's Corollary X.1.22(i). 

**Example.** If \(M=\mathbb C\) and its action is trivial, \(P=\operatorname{VN}_\ell(G)\) and \(P'=\operatorname{VN}_r(G)\). Formula (C10) becomes the explicit inversion equivalence \(C\operatorname{VN}_r(G)C=\operatorname{VN}_\ell(G)\). For a nonunimodular \(G\), omitting either modular square root in (C3) or (I1) would destroy the unitary identity (C4).

**Problem.** Suppose \(V_g\) is another strongly continuous unitary implementation of the same action on the same standard representation \(M\subseteq B(K)\). Does replacing \(U_g\) by \(V_g\) change the algebra in (I5)?

**Solution.** Each \(v_g=V_gU_g^*\) commutes with \(M\), so \(v_g\in M'\). Therefore \(V_g\otimes R_g=(v_g\otimes1)(U_g\otimes R_g)\). The generator set already contains \(M'\otimes1\), hence it generates the same von Neumann algebra with either implementation. This resolves the implementation choice on the fixed faithful representation. Extending the formula to every other normal covariant representation still requires the representation-amplification and corner argument.

The source locators are Takesaki, *Theory of Operator Algebras II*, Theorem X.1.21 and Corollary X.1.22(i). The direct commutant inputs are `OA-FLOW.DW.LEFTHILBERT`, `OA-FLOW.DW.INVARIANTCORE` M25, and OA-MOD-MF-05 with its WH-03–04 full-completion inputs. The separate weight identification uses WH-05–08; the modular action uses MF-06. The general GNS, standard-form, relative-operator, continuity and spectral prerequisites are used with their stated hypotheses. The argument proves the standard-form commutant-action isomorphism from these modular results. The arbitrary covariant-representation extension is supplied in the accompanying regular-commutant proof.
