# Relative tensor products and fusion

This unit constructs fusion for arbitrary normal unital modules over a von Neumann algebra. Module actions may have kernels, and Hilbert spaces and direct-sum index sets may have any cardinality. A reference weight is faithful, normal and semifinite whenever GNS coordinates or a modular endpoint occur. Inner products are linear in their first variable. Limits of approximating operators are nets, with the topology specified at each use.

The core construction starts with bounded right-module intertwiners \(T:L^2(N)\to H\). Their coefficients \(S^*T\in N\) give a positive semidefinite form on finite sums \(\sum T\odot\eta\). Fusion is the Hilbert completion after quotienting by its *whole* radical. This order matters: balancing relations lie in that radical, and other relations can occur when the two module actions have kernels. The construction is then identified with a rectangular corner of a standard form, which makes the two bounded-vector coordinate systems and their comparison precise.

The proof route is construction and the linking corner (FU-01–04), normal outer actions and units (FU-05–06), associativity and coherence (FU-07–08), modular balancing on its full endpoint domain (FU-08 companion), reference-weight comparison (FU-09), conjugate reversal (FU-10), computations with solved problems (FU-11), the full operator GNS dictionary and normal right action (FU-12), and the nonfaithful linking-weight columns and duality (FU-13). The direct-integral theorem with its measurable-field hypotheses, principal-graph classification, crossed-product cocycles and general operator-valued weights require separate units.

**Main result.** For every normal unital right \(N\)-module \(H\) and left \(N\)-module \(K\), the coefficient form (FU.10) is positive semidefinite and its full-radical quotient completes to \(H\boxtimes_NK\). The construction is independent of the chosen standard form through the canonical comparisons (FW.2). It is functorial in bounded module maps; its commuting outer actions are separately normal (AU.4–16). Standard modules give two-sided unit maps (AU.19–20), and arbitrary Hilbert direct sums distribute over fusion (AU.30–38). For composable correspondences, (F.21) defines a unitary associator satisfying the pentagon and triangle (F.37–38), and (CF.8) reverses fusion under conjugation. Faithful normal semifinite weights provide the equivalent bounded-vector coordinates (FU.15–26); the corrected balancing law on the full stated modular endpoint domain is (BD.6). Each assertion is proved in its cited section, including zero fusion and nonfaithful module actions.

Two small cases show what the quotient does. For \(N=\mathbb C\) with its usual weight and \(H=K=\mathbb C\), \(T_\xi(z)=\xi z\) and the form gives \([T_\xi\odot\eta]\mapsto\xi\eta\), a one-dimensional completion. For \(N=\mathbb C^2\), let \(H=\mathbb C\) use the first coordinate and \(K=\mathbb C\) use the second. Every coefficient of a right intertwiner into \(H\) is supported in the first coordinate, which acts as zero on \(K\). The entire algebraic tensor space is then the radical, so fusion is zero. FU-11 computes these cases and the distinct phenomenon of a joint outer-action kernel even when both module actions are faithful.

## Construction through a linking corner

**Source correspondence for the construction.** M. Takesaki, *Theory of Operator Algebras II*, IX.3.15–3.17, printed 200–202 / one-based PDF 220–222, gives the positive forms, relative tensor-product definition and balanced linking-corner identification. The complete source statements and proofs were compared with the independently written arguments below.

| Source clause | Argument in this lesson |
| --- | --- |
| IX.3.15(i): positive, possibly degenerate right-bounded form | FU02 (FU.10–11), specialized through FU03 (FU.17–22) |
| IX.3.15(ii): two-sided bounded-vector coefficient identity | FU04 (FU.31–33), with both bounded domains and the adjoint reversal |
| IX.3.15(i′): dual positive form and agreement | FU04 (FU.29–33), with its onto left-intertwiner model |
| IX.3.16: the full null quotient and the two completions | FU02–04 (FU.11, FU.22, FU.28–30); the quotient uses the whole radical |
| IX.3.17: the specified balanced standard linking corner | FU01 and FU04 (FU.27–28, FU.34–37), including the actual bounded-vector domain and onto generator map |

The source uses faithful modules. FU01’s full middle projection also treats normal unital modules with kernels; that extension is justified by the proof here. The auxiliary weight on the third corner is the opposite weight described in FU04. These are classical constructions with human source attribution. The writing AI checked these arguments relative to the declared inputs; the proofs of those inputs are not given here.

**Source correspondence for the actions and balancing.** Takesaki II, IX.3.18, printed 202–203 / one-based PDF 222–223, states the natural endomorphism actions and the weight-labelled balancing relation. The source uses faithful modules. The separate actions are faithful in that case, as FU05 proves below. Two additional printed assertions require correction.

| Source clause | Exact course statement and proof |
| --- | --- |
| IX.3.18(i): commuting normal endomorphism actions | FU05 (AU.4–15, AU.17–18), including both weight-bounded symbol domains and the opposite algebra for the right action |
| IX.3.18(i): the faithful-module convention | FU05, “Faithfulness of the separate factor actions”; each factor is faithful when the opposite module action is faithful |
| IX.3.18(ii): the bounded tensor operator and algebraic homomorphism | FU05 (AU.4–10, AU.16–18), with its norm bound, adjoint and uniqueness |
| IX.3.18(ii): the printed injectivity assertion | False in general; FU05 gives a nonzero kernel tensor for faithful coordinate modules over the two-dimensional diagonal algebra |
| IX.3.18(iii): the printed positive half-modular parameter | The corrected theorem uses \(D(\sigma^\psi_{-i/2})\) and its negative-half multiplier; the FU08 endpoint companion (BD.4–21) proves all product and bounded-vector domains |
| IX.3.18(iii): the sign and domain discrepancy | The companion’s finite matrix calculation maps the negative-half expression to half of the first coordinate vector, and the printed positive-half expression to twice that vector; the two endpoint domains are not assumed comparable |

These corrections retain the valid action clauses and state exactly which source assertions fail. The full endpoint proof and the counterexamples remain alongside the correspondence; a finite sign calculation does not replace the endpoint-domain argument.

**Source correspondence for units, sums and associativity.** Takesaki II, IX.3.19 and its adjacent display (29), printed 203 / one-based PDF 223, give the two standard-module units and the two binary direct-sum comparisons. IX.3.20, printed 203–204 / PDF 223–224, gives the associator and its outer-bounded coordinate formula. The complete original statements and the associator proof were compared with FU06–08.

| Source clause or proof step | Exact course statement and proof |
| --- | --- |
| IX.3.19(i): the left unit, its specified map and bimodule actions | FU06 (AU.19, AU.21, AU.26, AU.29), including the whole null quotient, onto range and both bounded-vector descriptions |
| IX.3.19(ii): the right unit for an arbitrary first vector and an opposite GNS second vector | FU06 (AU.20, AU.22–28); the left-bounded model proves the formula for every first vector, using the exact opposite finite ideal |
| Display (29): a direct sum in the right-module variable | FU06 (AU.30–35, AU.38), specialized to a singleton second family |
| Display (29): a direct sum in the left-module variable | The same proof, specialized to a singleton first family; all coordinate symbols and the inverse are proved eligible |
| IX.3.20: the typed unitary between the two completed bracketings | FU07–08 (F.10–23), including a bounded common cutoff, density in the subsequent fusion norm and every finite-sum cross term |
| The source's outer-bounded formula with an arbitrary middle vector | FU08 (F.24–30); the first outer vector is right-bounded, the last is left-bounded, and the middle vector need not be bounded for both actions |
| The source's coefficient comparison on that core | FU08 (F.26–29), with the precise reversed coefficient for the right action and both commuting actions on the middle module |
| Extension to the whole spaces, rather than just an isometry on displayed symbols | FU07 (F.10–19) and FU08 (F.23–30): total creation families, complete null relations and dense image in both bracketings |
| The full endomorphism bimodule assertion | FU08 (F.31–32), proved first for arbitrary bounded module maps and then for the outside actions |
| Further coherence consequences proved in this course | FU08 (F.33–38) supplies one common fourfold quotient core, the pentagon and the triangle with the specified units |

The direct-sum proof permits arbitrary index sets and uses the net of all finite subsets. Its column criterion (AU.36–38) separates membership in the completed sum from boundedness of a vector's intertwiner. The source's faithful-module convention is included; the proved statements also permit normal unital module actions with kernels and literal zero spaces.

The creation cutoff has three precise bounded-operator inputs: BK04 proves strong suprema of bounded increasing positive nets; BK05 proves inverse order without commutativity; BK06 proves the support cutoff and domination by a projection. BK01 states the underlying Hilbert-space and continuous functional-calculus contracts. Normal transport of bounded strong* limits uses NP06 and WH02; finite-weight contractions and their coordinates use WG008 and WH11. These are declared inputs, whose remaining transitive obligations are not replaced by this source comparison.

**Source correspondence for changing the reference weight.** Takesaki II, IX.3.21 and Remark 3.22, printed 205–206 / one-based PDF 225–226, give the canonical comparison, its testing diagram, uniqueness, the chain law and the warning about unchanged vector symbols. FU09 proves the complete comparison through standard-form intertwiners and a separating family of bounded tests.

| Source clause or proof step | Exact course statement and proof |
| --- | --- |
| IX.3.21: the first pair of reference-weight classes | The source prints a faithful first weight and a possibly nonfaithful second weight; FU09 explicitly proves the two-faithful-weight statement. Its zero-weight example disproves an extension using the raw bounded-vector completion |
| The prescribed bimodule isomorphism | FU09 (FW.1–4) preserves every finite-sum pairing and null relation, gives an explicit inverse and intertwines both full outside actions |
| The transported test maps before diagram (31) | FU09 (FW.8) uses the standard comparison for the first test and its inverse for the second. The printed second composition has the wrong domain direction |
| Diagram (31), with the adjoint of the left-module test | FU09 (FW.6–9) defines both bounded vertical composites and verifies the complete diagram on a total intertwiner core |
| Uniqueness from all transported tests | FU09 (FW.10) proves that their adjoint ranges have total span, so the diagram determines the comparison even among bounded maps |
| Chain law (32) for faithful reference weights | FU09 (FW.11), using the unique cone-preserving standard comparisons and the actual precomposition order |
| Remark 3.22: unchanged vector symbols need not give the comparison | The scalar computation (FE.1–2) changes the symbol by the square root of the reference-weight ratio |
| Remark 3.22: a construction independent of reference weights | FU02’s full-radical intertwiner completion and FU09’s coherent standard-form comparisons specify the construction without equating weight-dependent vectors |

Both printed discrepancies are explicit. The class definitions on printed 154 / PDF 174 distinguish semifinite normal weights from their faithful members, and Definition 3.16 on printed 201 / PDF 221 requires a faithful reference weight. The printed second test-map direction also fails the concrete weighted-adjoint check following (FW.8). The corrected comparison is proved at its declared inputs; it does not promote the broader quantifier or the mistyped composition.

The first four steps give a model that does not require a faithful action on either module.

A normal action need not be faithful. This construction allows kernels in either module action, arbitrary Hilbert spaces and arbitrary von Neumann algebras. Every approximation below is a net. The reference weights are faithful, normal and semifinite. Their existence follows from WH-13. The zero algebra is allowed; its unital modules are zero Hilbert spaces, and all maps below are then the unique maps between zero spaces.

## Standard modules and a full linking corner

Inner products are linear in their first variable. A right \(N\)-module \(H\) has a normal unital linear *-antirepresentation \(\rho_H:N\to B(H)\); write \(\xi b=\rho_H(b)\xi\). Thus \((\xi b)c=\xi(bc)\). A left module has a normal unital representation \(\lambda_H\).

\(N^{\mathrm{op}}\) is the same involutive vector space with reversed product \(b^{\mathrm{o}}c^{\mathrm{o}}=(cb)^{\mathrm{o}}\). Thus a right action is a representation of \(N^{\mathrm{op}}\).

**Adapted open definition: commuting actions.** An \(M\)-\(N\) bimodule is a Hilbert space \(H\) carrying the two normal unital actions

\[
 \begin{aligned}
 \lambda_H &:M\longrightarrow B(H),\\
 \rho_H &:N\longrightarrow B(H).
 \end{aligned}
\]

with \(\lambda_H\) a *-representation, \(\rho_H\) a *-antirepresentation, and \(\lambda_H(x)\rho_H(y)=\rho_H(y)\lambda_H(x)\). Put \(x\xi y=\lambda_H(x)\rho_H(y)\xi\). This commutation is equivalent to \(x(\xi y)=(x\xi)y\) for every vector and every \(x,y\).

Adapted from Peter Kristel and Konrad Waldorf, *Connes fusion of spinors on loop space*, Compositio Mathematica 160 (2024), 1596–1650, [Appendix A.1, p.1641](https://doi.org/10.1112/S0010437X24007188), © 2024 the authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). GPT-6.1 Sol (OpenAI), Ultra, October 2026, changed notation and explicitly imposed this course's unital convention. **End of adapted definition.** This marked component, including its adaptation, is CC BY 4.0; the surrounding material retains its separate licence.

Takesaki II IX.3.1 restricts attention to faithful actions. The present construction also permits kernels. A *full bimodule* satisfies \(\lambda_H(M)'=\rho_H(N)\). Taking commutants gives \(\rho_H(N)'=\lambda_H(M)''\); identifying the latter with \(\lambda_H(M)\) uses that the represented image is a von Neumann algebra. For the standard module below this follows directly from the standard-form axioms and BK-02. No general image-closure theorem is inferred from normal continuity alone. Fullness is not assumed for the modules being fused, and differs from the full projection \(e\) constructed below.

**Conjugates and the action order.** For the conjugate Hilbert space \(\overline H\), let \(C_H:H\to\overline H\) be the canonical antiunitary. The Riesz identification sends \(C_H\xi\) to the complex-linear functional \(h\mapsto\langle h,\xi\rangle\). This is the Hilbert realization of the Banach dual used in IX.3.1. For an \(M\)-\(N\) bimodule, its conjugate is an \(N\)-\(M\) bimodule with

\[
 \begin{gathered}
 a(C_H\xi)b=C_H\bigl(b^*\xi a^*\bigr),\\
 a\in N,\qquad b\in M.
 \end{gathered}
\]

Indeed, its left and right operators are \(C_H\rho_H(a^*)C_H^{-1}\) and \(C_H\lambda_H(b^*)C_H^{-1}\). The adjoint and \(C_H\) conjugate scalars twice, so these operators depend complex-linearly on \(a,b\). The adjoint reverses products; it cancels the reversal in \(\rho_H\) for the left action and introduces the required reversal for the right action. Conjugation by an antiunitary preserves operator adjoints and positivity. Thus both actions preserve *, their units are identities, and they commute because the original actions commute. For an increasing bounded positive net, the original action converges strongly to its supremum by normality and BK-04. Antiunitary conjugation transports that strong limit and its order supremum. NP-04 therefore gives normality of both conjugate actions. Each conjugate action has the same kernel as its corresponding original action, after identifying the underlying algebra. These checks apply without a dimension or countability restriction.

In particular, if \(K\) is only a left \(N\)-module, its conjugate is a right module with

\[
 (C_K\eta)b=C_K(b^*\eta).
 \tag{FU.1}
\]

**The full standard bimodule and its self-duality.** Choose a standard form \((N,L,J,P)\) with its faithful normal left action \(\lambda\), as in SE-01, and put

\[
 \rho(b)=J\lambda(b^*)J.
 \tag{FU.2}
\]

The scalar conjugations again show complex linearity, and direct multiplication gives \(\rho(bc)=\rho(c)\rho(b)\). Also \(\rho(b^*)=\rho(b)^*\), \(\rho(1)=1\), and \(\rho(b)=0\) forces \(\lambda(b^*)=0\), hence \(b=0\). If \(0\le b_i\uparrow b\), the normal action \(\lambda\) and BK-04 give \(\lambda(b_i)\to\lambda(b)\) strongly. Applying \(J\) on both sides gives the strong increasing limit \(\rho(b_i)\to\rho(b)\). NP-04 proves normality as a map on the opposite von Neumann algebra. The standard-form axiom says \(\lambda(N)'=J\lambda(N)J=\rho(N)\). This both proves commutation and makes the standard bimodule full. Since \(\lambda(N)\) is a concrete von Neumann algebra, BK-02 gives the reverse commutant equality \(\rho(N)'=\lambda(N)\).

Define

\[
 \begin{gathered}
 U:\overline L\longrightarrow L,\\
 U(C_L\zeta)=J\zeta.
 \end{gathered}
 \tag{FU.3}
\]

Both \(C_L\) and \(J\) are antiunitary, so \(U=JC_L^{-1}\) is linear, preserves the inner product and is onto. To check both actions, use the conjugate formula and the right action (FU.2):

\[
 \begin{aligned}
 U\bigl(a(C_L\zeta)b\bigr)
   &=J\lambda(b^*)\rho(a^*)\zeta\\
   &=J\lambda(b^*)J\lambda(a)J\zeta\\
   &=\rho(b)\lambda(a)J\zeta\\
   &=a\,U(C_L\zeta)\,b.
 \end{aligned}
\]

The last equality uses the already proved commutation. Thus \(U\) is the specified \(N\)-\(N\) bimodule self-duality. Under the usual notation \(\zeta^*=J\zeta\), its inverse sends \(\zeta^*\) to \(C_L\zeta\), exactly the correspondence of Takesaki II IX.3.2. That source leaves the proof to the reader; all scalar, normality, fullness and action-order checks needed here have now been supplied. These explanatory additions outside the marked open-definition component are by GPT-6.1 Sol (OpenAI), Ultra, October 2026, CC0-1.0. Earlier original text retains its existing licence.

**Intertwiner totality.** Put

\[
 X_H=\operatorname{Hom}_{N^{\mathrm{op}}}(L,H).
\]

All operators in this space are bounded and everywhere defined. Their ranges span \(H\); in fact each vector of \(H\) belongs to the range of one right-module partial isometry from \(L\).

To prove this, fix \(\xi\in H\). The functional \(f_\xi(b)=\langle\xi b,\xi\rangle\) is positive and normal. By SF-10/11 and standard-form comparison, it has a unique representative \(v_\xi\in P\). A cone vector gives the same functional for the right action: since \(Jv_\xi=v_\xi\),

\[
 \langle\rho(b)v_\xi,v_\xi\rangle
 =\langle v_\xi,\lambda(b^*)v_\xi\rangle
 =\langle\lambda(b)v_\xi,v_\xi\rangle.
\]

For \(b\in N\), both \(\|v_\xi b\|^2\) and \(\|\xi b\|^2\) equal \(f_\xi(bb^*)\). Hence \(v_\xi b\mapsto\xi b\) is a well-defined isometry between the cyclic right-module subspaces. Both subspaces reduce the right actions. Extend this isometry by zero on the orthogonal complement of \(\overline{v_\xi N}\). The resulting operator \(u_\xi\in X_H\) is a partial isometry and \(u_\xi v_\xi=\xi\). It is unique with this value and with initial space \(\overline{v_\xi N}\): the value on its dense cyclic subspace is forced, and its value on the orthogonal complement is zero. This proves totality without selecting a countable collection of vectors.

Form the Hilbert direct sum

\[
 V=L\oplus H\oplus\overline K,\qquad
 R=\operatorname{End}_{N^{\mathrm{op}}}(V),
 \tag{FU.4}
\]

and denote its three coordinate projections by \(e,p,q\). The commutant \(R\) is a von Neumann algebra, and \(eRe=\lambda(N)\). Its corner \(pRe\) consists exactly of the operators \(X_H\), extended by zero on the other coordinates. The cyclic construction applied to \(H\) and \(\overline K\) shows that \(ReV\) has dense span in \(V\). Consequently \(e\) has central support \(1\) in \(R\): any central projection dominating \(e\) has range containing \(ReV\).

We record the full-projection density argument in a form usable on other representations. Let \(E=L^2(R)\) be a standard form, with right action \(r_b=J_Rb^*J_R\), and write \(aEb=\lambda_R(a)r_bE\) for projections \(a,b\). The space \(\overline{\operatorname{span}ReE}\) reduces \(R\) and \(R'\). Its projection is central, dominates \(e\), and is contained in every central majorant of \(e\). Thus it is \(c_R(e)\), and is \(1\) here.

There is a useful explicit bounded net. Index by finite subsets \(F\subset R\) and real \(\varepsilon>0\), ordered by enlargement of \(F\) and decrease of \(\varepsilon\). Set

\[
 s_F=\sum_{a\in F}aea^*,\qquad
 d_{F,\varepsilon}=s_F(s_F+\varepsilon1)^{-1}.
 \tag{FU.5}
\]

The inverse-order inequality shows that these are increasing positive contractions. Their supremum is the projection onto the closed span of all \(aeE\): each fixed \(s_F\) contributes its support as \(\varepsilon\downarrow0\), and the common kernel of the \(s_F\)'s is exactly the orthogonal complement of that span. Therefore \(d_{F,\varepsilon}\to1\) strongly, hence strongly*. Moreover

\[
 d_{F,\varepsilon}
 =\sum_{a\in F}[(s_F+\varepsilon1)^{-1}a]ea^*.
\]

Every term contains the middle corner \(e\). Applying \(J_R\) gives the corresponding right-action approximation. In particular

\[
 \overline{\operatorname{span}pRe(eEe)}=pEe,\qquad
 \overline{\operatorname{span}pRe(eEq)}=pEq.
 \tag{FU.6}
\]

For the second assertion, apply the left net to \(w\in pEq\), then compress by \(p\); its finite terms have their second factor in \(eEq\). This proof remains valid when \(pEq=0\).

By SE-03, \(eEe\) is a faithful standard form of \(eRe\). Let
\(U_e:L\to eEe\) be the canonical unitary from SE-10 for the identification \(\lambda(N)=eRe\). It intertwines both actions and the conjugations. On the dense set of finite sums in \(H\) prescribe

\[
 U_H\left(\sum_iT_i\zeta_i\right)
       =\sum_it_iU_e\zeta_i,
 \qquad T_i\in X_H,\quad t_i\in pRe
 \tag{FU.7}
\]

where \(t_i\) is the corresponding block of \(R\). The squared norms of the two expressions are equal because every cross coefficient \(T_j^*T_i\) corresponds to \(t_j^*t_i\in eRe\). This proves well-definedness and isometry; (FU.6) proves onto \(pEe\). Apply the same construction to \(\overline K\), obtaining \(U_{\overline K}:\overline K\to qEe\), and define

\[
 U_K=J_RU_{\overline K}C_K:K\longrightarrow eEq.
 \tag{FU.8}
\]

Both conjugations are antilinear, so this map is linear. Equation (FU.1) verifies its left \(N\)-intertwining property.

The canonical two-summand conjugation can be read off without a new
choice. Since \(J_R(pEe)=eEp\), define the linear unitary
\(U_{\overline H}:\overline H\to eEp\) by
\(U_{\overline H}(C_H\xi)=J_RU_H\xi\). The standard-form comparison
\(U_e\) commutes with modular conjugation. Therefore, on the indicated
corners,

\[
 J_R(U_e\zeta+U_H\xi)
   =U_e(J\zeta)+U_{\overline H}(C_H\xi),
 \qquad \zeta\in L,\quad \xi\in H.
\]

Conjugation interchanges the left and right actions, so this is also
the conjugate-bimodule compatibility of the canonical embedding
\(L\oplus H\subset E\). It makes the \(J\)-extension in the
two-summand linking construction explicit.

For later use we need all corner intertwiners, not just a subspace of them. The corner commutant theorem SE-02 applied to the right representation on \(Ee\) says

\[
 \bigl(r(eRe)|_{Ee}\bigr)'=\lambda_R(R)|_{Ee}.
\]

A right intertwiner \(A:eEe\to pEe\), extended by zero on the orthogonal complement of \(eEe\) in \(Ee\), commutes with this right action. It is therefore restriction of an element of \(R\), and compression of that element to \(pRe\) represents \(A\). That representative is unique: if \(a\in R\) annihilates \(Ee\), it annihilates \((Ee)R\), which is dense in \(E\) by right-hand full-projection density, so \(a=0\). Interchanging left and right proves that every left intertwiner \(eEe\to eEq\) is uniquely

\[
 \zeta\longmapsto\zeta b,\qquad b\in eRq.
 \tag{FU.9}
\]

These identifications preserve norms and adjoints as rectangular operators.

The realization is canonical relative to the chosen standard form. Equations (FU.7–8) determine its maps on dense subspaces. A canonical comparison between two standard forms of \(R\) intertwines both actions and hence all these maps. There is no freely chosen commutant unitary.

## A positive form and its exact quotient

The coefficient \(S^*T\) of two members of \(X_H\) lies in \(\lambda(N)\). For the algebraic complex tensor product \(X_H\odot K\), define

\[
 B\left(\sum_iT_i\odot\eta_i,\sum_jS_j\odot\zeta_j\right)
 =\sum_{i,j}
 \left\langle\lambda_K\bigl(\lambda^{-1}(S_j^*T_i)\bigr)\eta_i,\zeta_j\right\rangle.
 \tag{FU.10}
\]

This formula is linear in its first variable and conjugate-linear in its second, and is independent of the way an algebraic tensor is written.

For positivity, the matrix \(G\) with row \(j\), column \(i\) equal to \(T_j^*T_i\) is positive: its quadratic form on \(L^n\) is \(\|\sum_iT_i v_i\|^2\). It belongs to \(M_n(\lambda(N))\). Write \(G=Q^*Q\) using the positive square root in that von Neumann algebra. The matrix amplification of \(\lambda_K\lambda^{-1}\) is a *-homomorphism, so it carries this factorization to a positive matrix on \(K^n\). Its quadratic form is exactly \(B(u,u)\). This proves \(B\ge0\).

The elementary polynomial inequality \(B(u+zv,u+zv)\ge0\), for \(z\in\mathbb C\), gives

\[
 |B(u,v)|^2\le B(u,u)B(v,v).
\]

When \(B(v,v)>0\), minimize the polynomial; when \(B(v,v)=0\), varying the size and phase of \(z\) forces \(B(u,v)=0\). Hence
\(\mathcal N=\{u:B(u,u)=0\}\) is exactly the radical of \(B\), and is a linear subspace. Quotient by this whole subspace and complete:

\[
 H\boxtimes_NK=\overline{(X_H\odot K)/\mathcal N}.
 \tag{FU.11}
\]

The resulting inner product is positive definite. The form on the raw tensor product is only positive semidefinite.

For \(a\in N\), the vector

\[
 T\lambda(a)\odot\eta-T\odot a\eta
 \tag{FU.12}
\]

pairs to zero against every generator by (FU.10); it belongs to \(\mathcal N\). This is ordinary balancing of an **intertwiner** against a vector. It does not assert untwisted balancing of weight-labelled module vectors. We will use the immediate norm bound

\[
 \|T\odot\eta\|_{\boxtimes}\le\|T\|\|\eta\|.
 \tag{FU.13}
\]

One convergence rule deserves an explicit statement. If \(T_i:L\to H\) are right intertwiners, uniformly bounded and converging strongly* to \(T\), then for each \(\eta\in K\),

\[
 T_i\odot\eta\longrightarrow T\odot\eta.
 \tag{FU.14}
\]

Indeed \((T_i-T)^*(T_i-T)\to0\) strongly on \(L\), on a bounded set. WH-02 and NP-06 carry this coefficient convergence through \(\lambda^{-1}\) and the normal representation \(\lambda_K\). Formula (FU.10) makes the squared fusion norm tend to zero. For completeness, products of bounded strong* convergent rectangular nets converge strongly*: subtract products, apply the uniform norm bound to the first difference, and use strong convergence on the fixed target vector for the second difference; repeat for adjoints. Finite families can be handled by one product-directed set.

## Exact weight-bounded coordinates and coefficient saturation

Fix an n.s.f. weight \(\psi\), initially using its standard GNS form \(L=H_\psi\), \(\lambda=\pi_\psi\), \(J=J_\psi\). Its actual ideals are

\[
 \mathfrak n_\psi=\{a:\psi(a^*a)<\infty\},\qquad
 \mathfrak n_\psi^*=\{x:x^*\in\mathfrak n_\psi\}.
\]

The linear opposite GNS map is

\[
 \Lambda'_\psi(x)=J_\psi\Lambda_\psi(x^*),\qquad x\in\mathfrak n_\psi^*,
 \qquad \|\Lambda'_\psi(x)\|^2=\psi(xx^*).
 \tag{FU.15}
\]

Both adjoint and \(J_\psi\) are conjugate-linear, which is why their composition here is linear.

Define \(D(H,\psi)\) to consist of the vectors \(\xi\in H\) for which some finite \(C\) satisfies

\[
 \|\xi x\|^2\le C\psi(xx^*)\quad(x\in\mathfrak n_\psi^*).
 \tag{FU.16}
\]

There is then a unique bounded operator

\[
 L_\psi(\xi):H_\psi\to H,\qquad
 L_\psi(\xi)\Lambda'_\psi(x)=\xi x.
 \tag{FU.17}
\]

The dense domain in (FU.15) is the exact test domain; the inequality proves bounded extension, with its least \(C\) equal to \(\|L_\psi(\xi)\|^2\). Since
\(\Lambda'_\psi(x)b=\Lambda'_\psi(xb)\) for \(b\in N\), this operator is a right intertwiner. The last identity follows directly by applying \(J_\psi\) to the GNS identity \(\Lambda_\psi(b^*x^*)=\pi_\psi(b^*)\Lambda_\psi(x^*)\). The map \(\xi\mapsto L_\psi(\xi)\) is injective: apply (FU.17) to WG-008's finite positive contractions \(e_i\in\mathfrak n_\psi^*\) and use \(\xi e_i\to\xi\), by normality of the right action.

Here is the native dictionary that fixes the right-module convention:

\[
 \pi_\psi(a)J_\psi\Lambda_\psi(x^*)
 =J_\psi\pi_\psi(x^*)J_\psi\Lambda_\psi(a),
 \qquad a\in\mathfrak n_\psi,\quad x\in\mathfrak n_\psi^*.
 \tag{FU.18}
\]

To prove it, put \(b=x^*\) and use WG-009's \(b_i=e_ib\in\mathfrak m_\psi\). Then \(\Lambda(b_i)\to\Lambda(b)\), while \(\pi(b_i)\to\pi(b)\) strongly with bound \(\|b\|\). By MF-06, \(J\Lambda(b_i)\) is a right Hilbert-algebra bounded vector with operator \(J\pi(b_i)J\). By WH-11, \(\Lambda(a)\) is left bounded with operator \(\pi(a)\). WH-04 gives
\(\pi(a)J\Lambda(b_i)=J\pi(b_i)J\Lambda(a)\). Passing to the two indicated limits proves (FU.18). Consequently

\[
 \Lambda_\psi(a)\in D(H_\psi,\psi),\qquad
 L_\psi(\Lambda_\psi(a))=\pi_\psi(a).
 \tag{FU.19}
\]

In fact

\[
 D(H_\psi,\psi)=\Lambda_\psi(\mathfrak n_\psi).
 \tag{FU.20}
\]

For the reverse inclusion, restrict the estimate defining \(L_\psi(\xi)\) to \(x^*\in\mathfrak n_\psi\cap\mathfrak n_\psi^*\). The vectors \(J\Lambda_\psi(x^*)\) are the full right Hilbert algebra, by WH-11 and MF-06, and their right operators are \(J\pi_\psi(x^*)J\). Thus the estimate says precisely that \(\xi\) is left bounded for that full Hilbert algebra. WH-11 recovers the unique \(a\in\mathfrak n_\psi\) with \(\xi=\Lambda_\psi(a)\). This use of WH-11 keeps its full finite ideal; no analyticity assumption is introduced.

For an arbitrary \(T\in X_H\), let \(e_i\) be the positive finite-energy contractions of WG-008. They satisfy \(e_i=e_i^*\), \(\psi(e_i)<\infty\), and \(e_i\to1\) strongly*. Define

\[
 \xi_i=T\Lambda_\psi(e_i).
\]

Equations (FU.17–19) give

\[
 \xi_i\in D(H,\psi),\qquad
 L_\psi(\xi_i)=T\pi_\psi(e_i),\qquad
 \|L_\psi(\xi_i)\|\le\|T\|,
 \tag{FU.21}
\]

and these operators converge strongly* to \(T\). Strong convergence follows from \(\pi_\psi(e_i)\to1\); the adjoints converge because
\((T\pi_\psi(e_i))^*=\pi_\psi(e_i)T^*\). Thus all coefficients converge in the bounded strong* topology. One and the same \(e_i\) works for any finite family \(T_1,\ldots,T_n\).

It follows from (FU.14) that

\[
 [L_\psi(\xi_i)\odot\eta]\longrightarrow[T\odot\eta].
 \tag{FU.22}
\]

Therefore the form on \(D(H,\psi)\odot K\) obtained by substituting \(T_i=L_\psi(\xi_i)\) in (FU.10), followed by its exact null quotient and Hilbert completion, maps unitarily **onto** \(H\boxtimes_NK\). We denote its elementary symbol by \(\xi\otimes_\psi\eta\). This proves the onto assertion by coefficient saturation, not merely by vector-domain density. Vector-domain density also holds: \(T\Lambda_\psi(a)\in D(H,\psi)\) for every \(a\in\mathfrak n_\psi\), and these vectors are total by FU-01 and GNS density.

For a left module put

\[
 D'(K,\psi)=\{\eta:\exists C<\infty,\
       \|a\eta\|^2\le C\psi(a^*a)\quad(a\in\mathfrak n_\psi)\},
\]

\[
 R_\psi(\eta)\Lambda_\psi(a)=a\eta.
 \tag{FU.23}
\]

This bounded extension is a left intertwiner. Conjugation gives its exact relation to the right construction:

\[
 C_K\eta\in D(\overline K,\psi)
 \ \Longleftrightarrow\ \eta\in D'(K,\psi),\qquad
 L_\psi(C_K\eta)=C_KR_\psi(\eta)J_\psi.
 \tag{FU.24}
\]

Evaluate both sides at \(\Lambda'_\psi(x)\) to verify the equality: they give \(C_K(x^*\eta)\). In particular \(D'(H_\psi,\psi)=J_\psi\Lambda_\psi(\mathfrak n_\psi)\), and

\[
 R_\psi(J_\psi\Lambda_\psi(a))=J_\psi\pi_\psi(a)J_\psi.
 \tag{FU.25}
\]

Every bounded left intertwiner \(V:H_\psi\to K\) has the uniformly bounded strong* approximation

\[
 \eta_i=VJ_\psi\Lambda_\psi(e_i),\qquad
 R_\psi(\eta_i)=VJ_\psi\pi_\psi(e_i)J_\psi.
 \tag{FU.26}
\]

This proves both vector density and the left coefficient saturation, with no change in \(\psi\).

For a previously fixed standard bimodule \(L\), precompose all right or left operators in this item with the inverse of the canonical unitary \(H_\psi\to L\). The coefficients are then identified by the same represented element of \(N\). This transports the complete construction; it does not identify GNS vectors or finite ideals belonging to different weights.

## The onto corner map and the two-sided pairing

Use FU-01's simultaneous realization and suppress the three specified unitaries in the notation:

\[
 H=pEe,\quad K=eEq,\quad L=eEe,\quad
 X_H=pRe.
\]

The map

\[
 T\odot\eta\longmapsto t\eta\in pEq,\qquad t\in pRe,
 \tag{FU.27}
\]

preserves (FU.10), since
\(\langle t\eta,s\zeta\rangle=\langle s^*t\eta,\zeta\rangle\).
Its range has dense span by (FU.6), so it induces a unitary

\[
 W: H\boxtimes_NK\longrightarrow pEq.
 \tag{FU.28}
\]

Under \(U_H\), \(pRp=\operatorname{End}_{N^{\mathrm{op}}}(H)\).
The conjugate-space map
\(B\mapsto C_K B^* C_K^{-1}\), extended by zero on the other
summands of \(V\), identifies \(\operatorname{End}_N(K)^{\mathrm{op}}\)
with \(qRq=\operatorname{End}_{N^{\mathrm{op}}}(\overline K)\).
Under the specified \(U_K\), the element so associated to \(B\) acts
on \(K=eEq\) by right multiplication. Thus these are precisely the
two outer endomorphism algebras of the linking-corner model. For
\(a\in pRp\) and \(b\in qRq\), define the natural corner actions on
algebraic generators by
\(a[T\odot\eta]b=[(aT)\odot(\eta b)]\). The coefficient Gram form bounds
these actions by \(\|a\|\) and \(\|b\|\), respectively; for the right bound,
\(b\) commutes with the left \(N\)-action on \(K=eEq\). They therefore
descend to bounded actions on the quotient, and

\[
 W\bigl(a[T\odot\eta]b\bigr)
 =W[(aT)\odot(\eta b)]
 =(at)(\eta b)=a(t\eta)b.
\]

Density extends this identity to the completion. Thus \(W\) is a
\(pRp\)-\(qRq\) bimodule unitary, not only a
Hilbert-space unitary. In particular the weight-labelled model is onto the
same corner by (FU.21–22).

**Linking-corner interpretation.** In the standard form \(E=L^2(R)\), the specified realizations identify \(L=eEe\), \(H=pEe\), \(K=eEq\), and \(X_H=pRe\). Fullness of \(e\) makes the span of \(pRe(eEq)\) dense in \(pEq\); \(W[T\odot\eta]=t\eta\) is then the unitary induced by the exact radical quotient. See (FU.4), (FU.6), and (FU.27–28). The source context is Takesaki II, IX.3, Proposition 3.15, Definition 3.16 and Theorem 3.17 (printed pp. 200–202); the displayed full-corner construction is proved here.

There is also a left-intertwiner model. Write
\(Y_K=\operatorname{Hom}_N(L,K)\).
For \(V,W\in Y_K\) the operator \(W^*V\) lies in \(\rho(N)\). Define on \(H\odot Y_K\)

\[
 B'\left(\sum_i\xi_i\odot V_i,\sum_j\chi_j\odot W_j\right)
 =\sum_{i,j}\left\langle
 \rho_H\bigl(\rho^{-1}(W_j^*V_i)\bigr)\xi_i,\chi_j\right\rangle.
 \tag{FU.29}
\]

The order \(W_j^*V_i\) is essential. The map \(\rho_H\circ\rho^{-1}\) is a normal *-representation of \(\rho(N)\): both factors reverse multiplication. Thus finite Gram-matrix positivity proves that (FU.29) is positive semidefinite, exactly as in FU-02.

By (FU.9), \(V_i\zeta=\zeta b_i\) with \(b_i\in eRq\). If \(W_j\zeta=\zeta c_j\), then \(W_j^*V_i\) is right multiplication by \(b_ic_j^*\). It follows that

\[
 \xi\odot V\longmapsto\xi b
 \tag{FU.30}
\]

preserves \(B'\). Its range is dense in \(pEq\), by the right version of (FU.6). Thus its null quotient and completion are onto the same corner. Equation (FU.26), followed by its coefficient-norm argument, proves that restricting \(V\) to \(R_\psi(\eta)\) gives the whole completion. This defines \(\xi\otimes_\psi\eta\) also for \(\xi\in H,\eta\in D'(K,\psi)\).

We must prove that these two meanings agree on their common domain. Let

\[
 \xi\in D(H,\psi),\quad \eta\in D'(K,\psi),\quad
 L_\psi(\xi)=a|_{eEe},\quad
 R_\psi(\eta)=r_b|_{eEe},
 \qquad a\in pRe,\ b\in eRq.
\]

For \(A\in eRp\) and \(B\in qRe\), the vector \(A\xi\in eEe\) is right \(\psi\)-bounded with operator \(Aa\), and \(\eta B\in eEe\) is left \(\psi\)-bounded with operator right multiplication by \(bB\). This follows directly from the defining estimates, since the bounded actions of \(A\) and of right multiplication by \(B\) commute with the appropriate middle action. Equations (FU.20) and (FU.25) put these vectors in the two standard Hilbert-algebra bounded domains. WH-04 therefore gives

\[
 (Aa)(\eta B)=(A\xi)(bB).
\]

Set \(w=a\eta-\xi b\in pEq\). We have \(AwB=0\) for all such \(A,B\). For fixed \(B\), taking \(A=erp\) gives \(er\,wB=0\) for every \(r\in R\), because \(wB=pwB\). The positive net (FU.5), applied to \(wB\), gives \(wB=0\). Repeating with the right net and \(B=qre\) gives \(w=0\). Equivalently, the two full-corner testing families separate \(pEq\). Thus

\[
 a\eta=\xi b.
 \tag{FU.31}
\]

No ambient Tomita domain has been assumed for \(\xi\) or \(\eta\).

Consequently, for \(\xi,\chi\in D(H,\psi)\) and
\(\eta,\zeta\in D'(K,\psi)\),

\[
\begin{aligned}
 &\left\langle
 \lambda_K\bigl(\pi_\psi^{-1}(L_\psi(\chi)^*L_\psi(\xi))\bigr)\eta,\zeta
 \right\rangle\\
 &\qquad =
 \left\langle
 \rho_H\bigl(\rho_\psi^{-1}(R_\psi(\zeta)^*R_\psi(\eta))\bigr)\xi,\chi
 \right\rangle.
\end{aligned}
 \tag{FU.32}
\]

The element of \(N\) in the second line can alternatively be written

\[
 \pi_\psi^{-1}\bigl(J_\psi R_\psi(\eta)^*R_\psi(\zeta)J_\psi\bigr).
 \tag{FU.33}
\]

Indeed \(\rho_\psi^{-1}(D)=\pi_\psi^{-1}(J_\psi D^*J_\psi)\). Formula (FU.33) records both the adjoint and its reversal. Summing (FU.32) gives equality of the two finite forms on their common bounded domain. Their onto maps (FU.28) and (FU.30), not an unsupported intersection-density assertion, identify the completed spaces.

For clarity, the full-corner testing step also has a scalar proof. If \(er\,v=0\) for every \(r\), then \(\langle r^*er\,v,v\rangle=\|er\,v\|^2=0\) for every \(r\). Hence every positive \(s_F\) in (FU.5), after replacing its index \(a\) by \(r^*\), annihilates \(v\). So do its functions \(d_{F,\varepsilon}\); their strong limit is \(1\), giving \(v=0\). The right-hand statement follows by \(J_R\). This uses no faithful action of \(N\) on \(H\) or \(K\).

**The specified balanced-weight model.** The same construction identifies the precise standard \((2,3)\) corner used with diagonal weights, including the bounded multiplication operator on its generators.

**Auxiliary opposite weight.** The third corner \(qRq\) realizes \(\operatorname{End}_N(K)^{\mathrm{op}}\) through the anti-isomorphism \(B\mapsto C_KB^*C_K^{-1}\) used above. If an auxiliary weight is prescribed on the left-module endomorphism algebra, transport it through this anti-isomorphism before forming the balanced weight on the three corners. The map and its inverse preserve positive cones, sums and increasing suprema, which proves faithfulness and normality of the transported weight. They also transport an increasing net of finite positive contractions to such a net, so WG-008 proves semifiniteness. In (FU.34), \(\nu\) denotes this corner weight. This specifies how a prescribed auxiliary weight matches the source’s third diagonal term.

Choose n.s.f. weights \(\phi\) on \(pRp\) and \(\nu\) on \(qRq\), and let

\[
 \Phi(x)=\psi(exe)+\phi(pxp)+\nu(qxq),\qquad x\in R_+,
 \tag{FU.34}
\]

using \(eRe=N\). Two applications of CW-06 make \(\Phi\) faithful, normal and semifinite. Each coordinate projection is fixed by its modular group: the sign unitary for that projection preserves all three compressed terms, and CZ-09 applies. Write \(E_\Phi=H_\Phi\). Its \((i,j)\) space is \(e_iE_\Phi e_j\), with \(e_1=e,e_2=p,e_3=q\).

Here are the precise GNS and bounded-vector identifications needed for this comparison. The map

\[
 V_e\Lambda_\psi(x)=\Lambda_\Phi(x),\qquad x\in\mathfrak n_\psi\subset eRe,
 \tag{FU.35}
\]

is an isometry. It is onto \(eE_\Phi e\): CZ-05 gives
\(\Lambda_\Phi(ye)=r_e\Lambda_\Phi(y)\) for \(y\in\mathfrak n_\Phi\), so \(er_e\) maps the dense GNS domain onto vectors \(\Lambda_\Phi(eye)\), whose elements lie in \(\mathfrak n_\psi\). The range of (FU.35) is therefore exactly that closed corner. On the finite-star domains the closed involutions agree after this compression, because \(er_e\Lambda_\Phi(y)=\Lambda_\Phi(eye)\) and
\((eye)^*=ey^*e\). This projection preserves the graph core and commutes with the involution there. Applying it to a graph-core approximation proves that the restriction of the closed involution is precisely the closure of the corner involution. Their polar decompositions give the corner \(J\) and modular operator. The usual natural cones, obtained as the closures of the positive finite-star vectors acted on by the one-quarter modular power, consequently agree. Thus (FU.35) is the canonical standard-form comparison.

We next prove that the operator \(a=L_\psi(\xi)\in pRe\) is the full left Hilbert-algebra multiplication operator of the vector \(\xi\in pE_\Phi e\). This is a domain assertion and does not follow only from the corner commutant theorem. Take an ambient right Hilbert-algebra vector \(\theta\), with bounded right operator \(R_\theta=r_c\), \(c\in R\). For \(A\in eRp\) and \(B\in Re\), the vector \(e\theta B\) lies in \(eE_\Phi e\) and is left \(\psi\)-bounded: for \(x\in\mathfrak n_\psi\),

\[
 x(e\theta B)=x\theta B
 =R_\theta\Lambda_\Phi(x)B
 =\Lambda_\Phi(x)(ecB).
\]

Hence its left bounded operator is right multiplication by \(ecB\). The vector \(A\xi\) is right bounded with operator \(Aa\). Apply the standard middle-corner mixed identity to these two vectors:

\[
 A a\theta B=(Aa)(e\theta B)
 =(A\xi)(ecB)=A\xi cB.
\]

The full-corner separation just proved yields \(a\theta=\xi c=R_\theta\xi\) for every ambient right Hilbert-algebra vector \(\theta\). Thus \(\xi\) is ambient left bounded and its operator is exactly \(a\). WH-11 now gives

\[
 \xi=\Lambda_\Phi(a),\qquad a\in\mathfrak n_\Phi\cap pRe.
 \tag{FU.36}
\]

Conversely, if \(a\) belongs to this last set, the ambient mixed identity restricted to \(eE_\Phi e\) gives \(L_\psi(\Lambda_\Phi(a))=a|_{eE_\Phi e}\). Because \(p,e\) centralize \(\Phi\), the vector lies in \(pE_\Phi e\). This proves exact equality of the two bounded-vector domains. Conjugating proves the corresponding statement for left-bounded vectors in \(eE_\Phi q\).

Finally, SE-10 supplies the canonical \(R\)-bimodule unitary \(U:E\to E_\Phi\), preserving every \(e_iEe_j\). The defining rectangle maps (FU.7–8) commute with \(U\), and (FU.36) gives, for every bounded generator,

\[
 U\,W(\xi\otimes_\psi\eta)
   =a\,U_K^\Phi\eta
   =\lambda^\Phi_{U_H^\Phi\xi}\,U_K^\Phi\eta
   \ \in pE_\Phi q.
 \tag{FU.37}
\]

Here \(\lambda^\Phi_\gamma\) denotes the bounded left Hilbert-algebra operator of the ambient left-bounded vector \(\gamma\). This is the exact generator formula for the balanced standard linking corner, and the map is onto by (FU.28). Changing the auxiliary diagonal weights changes the displayed standard form by its canonical comparison; (FU.37) remains a commuting diagram.

The construction gives the positive quotient, both bounded-vector descriptions, and the full linking \((2,3)\) corner. Functorial outer actions, the corrected negative half-modular balancing law, unit maps, associativity, coherence and reference-weight-change laws are separate subsequent proof blocks. Nothing here asserts that the joint algebraic tensor product of the two outer endomorphism algebras acts injectively.

## Actions, units and arbitrary sums

The next two steps construct bounded functorial maps, prove normality of the induced factor actions, identify both standard units in weight coordinates, and handle arbitrary Hilbert direct sums. Modular-domain balancing is proved in the FU-08 endpoint companion.

### The construction used here

Fix a von Neumann algebra \(N\) and a standard bimodule \(L=L_N\). Its faithful normal left representation and right antirepresentation are denoted by \(\lambda\) and \(\rho\), with

\[
 \lambda(N)=\rho(N)',\qquad \rho(N)=\lambda(N)'.
\]

All inner products are linear in the first variable. A right action is written \(\xi b=\rho_H(b)\xi\); in particular \(\rho_H(bc)=\rho_H(c)\rho_H(b)\). Every action under consideration is normal and unital, but it may have a kernel. Hilbert spaces and index sets are arbitrary. All intertwiners below are bounded, everywhere-defined linear operators.

For a right \(N\)-module \(H\), write

\[
 X_H=\operatorname{Hom}_{N^{\mathrm{op}}}(L,H).
\]

FU-01 proves that the ranges of the members of \(X_H\) have total linear span in \(H\). For a left \(N\)-module \(K\), FU-02 constructs \(H\boxtimes_N K\) as the Hilbert completion of the null quotient of \(X_H\odot K\). We write \([T\odot\eta]\) for the quotient class. Its finite-sum pairing is

\[
 \left\langle\sum_i[T_i\odot\eta_i],\sum_j[S_j\odot\zeta_j]\right\rangle
 =\sum_{i,j}\left\langle
 \lambda_K\!\left(\lambda^{-1}(S_j^*T_i)\right)\eta_i,\zeta_j
 \right\rangle.                                                   \tag{AU.1}
\]

In particular

\[
 \|[T\odot\eta]\|\leq\|T\|\|\eta\|.                              \tag{AU.2}
\]

The quotient is by the entire nullspace of this positive semidefinite form. None of the arguments below assumes that a raw tensor symbol determines a nonzero vector.

We use the following precise convergence consequence of FU-02. If \(T_\alpha:L\to H\) are uniformly bounded right intertwiners and \(T_\alpha\to T\) strongly*, then

\[
 [T_\alpha\odot\eta]\longrightarrow[T\odot\eta]
 \quad(\eta\in K).                                                \tag{AU.3}
\]

Here rectangular strong* convergence means strong convergence of the operators and of their adjoints on their respective Hilbert spaces. The proof applies (AU.1) to the positive coefficient \((T_\alpha-T)^*(T_\alpha-T)\), which tends strongly to zero on a bounded set. WH-02 transports this through the faithful standard representation, and NP-06 transports it through the normal action on \(K\). The same rule applies to a finite family using one product-directed set.

## Functorial maps and normal commuting actions

Let \(A:H\to H'\) be right \(N\)-linear, and let \(B:K\to K'\) be left \(N\)-linear. There is a unique bounded map

\[
 A\boxtimes_N B: H\boxtimes_N K\longrightarrow H'\boxtimes_N K'
\]

such that

\[
 (A\boxtimes_N B)[T\odot\eta]=[AT\odot B\eta].                     \tag{AU.4}
\]

It satisfies

\[
 \|A\boxtimes_N B\|\leq\|A\|\|B\|,\qquad
 (A\boxtimes_N B)^*=A^*\boxtimes_N B^*,                            \tag{AU.5}
\]

and the identity and composition rules

\[
 1_H\boxtimes_N1_K=1_{H\boxtimes_N K},\qquad
 (A'\boxtimes_N B')(A\boxtimes_N B)
       =(A'A)\boxtimes_N(B'B).                                    \tag{AU.6}
\]

The second formula assumes the displayed operator compositions are defined. Adjoints of module intertwiners are module intertwiners: take the adjoint of the intertwining equation for \(b^*\), for every \(b\in N\).

**The first-variable bound.** For a finite list \(T_i\in X_H\), the two operator matrices with row \(j\), column \(i\) equal to

\[
 T_j^*A^*AT_i\quad\hbox{and}\quad T_j^*T_i
\]

belong to \(M_n(\lambda(N))\), and

\[
 0\leq[T_j^*A^*AT_i]_{j,i}
       \leq\|A\|^2[T_j^*T_i]_{j,i}.                              \tag{AU.7}
\]

Indeed, on a column \((u_i)\in L^n\), the two quadratic forms are respectively \(\|A\sum_iT_i u_i\|^2\) and \(\|\sum_iT_i u_i\|^2\). Apply the matrix amplification of \(\lambda_K\lambda^{-1}\), which preserves positivity by positive square-root factorization. Evaluating its quadratic form on \((\eta_i)\) gives

\[
 \left\|\sum_i[AT_i\odot\eta_i]\right\|^2
 \leq\|A\|^2\left\|\sum_i[T_i\odot\eta_i]\right\|^2.              \tag{AU.8}
\]

This is an inequality for arbitrary finite sums, so it proves preservation of all null relations, not just an estimate for one elementary tensor.

**The second-variable bound.** Let \(G=[\lambda^{-1}(T_j^*T_i)]_{j,i}\in M_n(N)_+\), and put \(g=G^{1/2}\). The norm square in (AU.1) is
\(\|\lambda_K^{(n)}(g)(\eta_i)\|^2\).
The diagonal operator \(B^{(n)}:K^n\to(K')^n\) intertwines the entrywise representations of every element of \(M_n(N)\), including \(g\). Therefore

\[
 \begin{split}
 \left\|\sum_i[T_i\odot B\eta_i]\right\|^2
 &=\|\lambda_{K'}^{(n)}(g)B^{(n)}(\eta_i)\|^2\\
 &=\|B^{(n)}\lambda_K^{(n)}(g)(\eta_i)\|^2\\
 &\leq\|B\|^2\left\|\sum_i[T_i\odot\eta_i]\right\|^2.
 \end{split}                                                       \tag{AU.9}
\]

Apply (AU.8), then (AU.9) with the target intertwiners \(AT_i\). This defines (AU.4) on the null quotient with the bound (AU.5), and hence on its completion. Density gives uniqueness. It also shows that the map depends linearly on \(A\) and on \(B\) separately.

For the adjoint formula, take \(T\in X_H\), \(S\in X_{H'}\), \(\eta\in K\), and \(\zeta\in K'\). With \(c=\lambda^{-1}(S^*AT)\), the defining pairing gives

\[
 \begin{split}
 \langle[AT\odot B\eta],[S\odot\zeta]\rangle
 &=\langle\lambda_{K'}(c)B\eta,\zeta\rangle\\
 &=\langle\lambda_K(c)\eta,B^*\zeta\rangle\\
 &=\langle[T\odot\eta],[A^*S\odot B^*\zeta]\rangle.
 \end{split}                                                       \tag{AU.10}
\]

Both sides extend continuously to the completed spaces. Identity and composition are checked on the same total set of elementary classes, proving (AU.6). In particular, a pair of isometries induces an isometry, a pair of unitaries induces a unitary, and a pair of orthogonal projections induces an orthogonal projection, by (AU.5–6).

**Normal factor actions.** The algebras

\[
 \mathcal E_H=\rho_H(N)'\subseteq B(H),\qquad
 \mathcal E_K=\lambda_K(N)'\subseteq B(K)
\]

act on the fusion by

\[
 \alpha(a)=a\boxtimes_N1_K,\qquad
 \beta(b)=1_H\boxtimes_N b.                                       \tag{AU.11}
\]

Equations (AU.5–6) make these unital *-homomorphisms, and their ranges commute because their two compositions both send \([T\odot\eta]\) to \([aT\odot b\eta]\). They are normal.

Here is a net proof of that last assertion. Suppose \(0\leq a_\gamma\uparrow a\) in \(\mathcal E_H\). By BK-04, \(d_\gamma=a-a_\gamma\) tends strongly to zero, is positive, and has norm at most \(\|a\|\). Thus \(d_\gamma T\) tends strongly* to zero for every \(T\in X_H\): for adjoints use \((d_\gamma T)^*=T^*d_\gamma\). Applying (AU.3) gives

\[
 \alpha(d_\gamma)[T\odot\eta]
       =[d_\gamma T\odot\eta]\longrightarrow0.                    \tag{AU.12}
\]

Explicitly, its squared norm is

\[
 \left\langle\lambda_K\!\left(
  \lambda^{-1}(T^*d_\gamma^2T)\right)\eta,\eta\right\rangle
 \longrightarrow0.                                                \tag{AU.13}
\]

The bounded coefficients tend strongly to zero; no assertion that the squares \(d_\gamma^2\) decrease is required. Finite sums follow by the triangle inequality. Since \(\|\alpha(d_\gamma)\|\leq\|a\|\), density then gives strong convergence to zero on every fusion vector. The positive net \(\alpha(a_\gamma)\) consequently has supremum \(\alpha(a)\), by its strong limit and BK-04. This is normality, equivalently ultraweak continuity by NP-06.

If \(0\leq b_\gamma\uparrow b\) in \(\mathcal E_K\), BK-04 gives \((b-b_\gamma)\eta\to0\), and

\[
 \|\beta(b-b_\gamma)[T\odot\eta]\|
 \leq\|T\|\|(b-b_\gamma)\eta\|\longrightarrow0.                   \tag{AU.14}
\]

The same finite-sum, uniform-bound, and positive-supremum argument proves that \(\beta\) is normal. These proofs do not require either module action to be faithful.

More generally, if \(A_\gamma:H\to H'\) is a uniformly bounded net of right intertwiners converging strongly* to \(A\), then \(A_\gamma T\to AT\) strongly* for each \(T\). Equations (AU.2–5), first on elementary classes and then by density, show that
\(A_\gamma\boxtimes_N1_K\to A\boxtimes_N1_K\) strongly*. For the adjoints apply the same argument to \(A_\gamma^*\) and use (AU.5). If \(B_\gamma:K\to K'\) is uniformly bounded and strongly* convergent, (AU.2) and the adjoint formula give the analogous assertion for \(1_H\boxtimes_N B_\gamma\). These statements concern bounded nets between fixed Hilbert spaces; they make no claim of unrestricted strong-operator continuity.

If \({}_P H_N\) and \({}_N K_Q\) have commuting normal unital outside actions, the fusion has the actions

\[
 p[T\odot\eta]q=[\lambda_H(p)T\odot\rho_K(q)\eta].                 \tag{AU.15}
\]

The left action is the composite of \(\lambda_H:P\to\mathcal E_H\) with \(\alpha\); the right action is the composite of the normal antirepresentation \(\rho_K:Q\to\mathcal E_K\) with \(\beta\). Hence these are respectively a normal unital representation and a normal unital antirepresentation, and they commute. If \(A\) and \(B\) also intertwine their outside actions, (AU.4) shows that \(A\boxtimes_N B\) is a bimodule map. This proves bounded bimodule functoriality with the actual outside algebras and product order.

**Faithfulness of the separate factor actions.** If the original left action of \(N\) on \(K\) is faithful, then \(\alpha\) is faithful. Indeed, take nonzero \(a\in\mathcal E_H\). The ranges of the intertwiners in \(X_H\) span a dense subspace of \(H\), by FU01, so some \(T\in X_H\) satisfies \(aT\ne0\). Then \(c=\lambda^{-1}(T^*a^*aT)\) is a nonzero positive element of \(N\). Faithfulness of \(\lambda_K\) gives an \(\eta\in K\) with \(\langle\lambda_K(c)\eta,\eta\rangle>0\). The defining positive form (AU.1) identifies this number with the squared norm of \(\alpha(a)[T\odot\eta]\), so \(\alpha(a)\ne0\).

If the original right action on \(H\) is faithful, then \(\beta\) is faithful. Use FU04’s left-intertwiner model \(H\odot Y_K\), whose intertwiners have total ranges in \(K\) by the left version of FU01’s full-corner density. For nonzero \(b\in\mathcal E_K\), choose \(V\in Y_K\) with \(bV\ne0\). The coefficient \(d=\rho^{-1}(V^*b^*bV)\) is nonzero and positive. Faithfulness of \(\rho_H\) gives \(\xi\in H\) with \(\langle\rho_H(d)\xi,\xi\rangle>0\). The bimodule identification (FU.30) sends the action of \(\beta(b)\) to \(\xi\odot V\mapsto\xi\odot bV\). Formula (FU.29) makes that positive number its squared norm. Hence \(\beta(b)\ne0\). Under the source’s faithful-module assumptions both separate maps are therefore faithful. The right endomorphism algebra is the opposite algebra: its underlying element acts by \(\beta(b)\), which reverses the opposite product as required for a right module. Faithfulness of these two maps does not imply injectivity of their joint tensor representation.

**The joint tensor representation can have a kernel.** Commutation gives a unital algebraic *-homomorphism

\[
 \Theta:\mathcal E_H\odot\mathcal E_K\longrightarrow
 B(H\boxtimes_N K),\qquad \Theta(a\odot b)=\alpha(a)\beta(b).        \tag{AU.16}
\]

Separate normality and unitality are the assertions proved above. Injectivity is false in general, even when all original module actions and both factor maps are faithful.

For a direct verification, take \(N=\mathbb C^2\), \(L=H=K=\mathbb C^2\) with coordinatewise left and right multiplication and the usual inner product. Every right intertwiner \(L\to H\) is \(T_c=\operatorname{diag}(c_1,c_2)\). By (AU.1),

\[
 [T_c\odot\eta]\longmapsto(c_1\eta_1,c_2\eta_2)
\]

is an isometry after the null quotient, with onto range since \(c=(1,1)\) is allowed. Both endomorphism algebras are the diagonal \(\mathbb C^2\), and \(\Theta(a\odot b)\) becomes \(\operatorname{diag}(a_1b_1,a_2b_2)\). Thus the nonzero algebraic tensor \((1,0)\odot(0,1)\) is in its kernel. It is nonzero because the tensor product of the first-coordinate functional and the second-coordinate functional evaluates it to one. Each factor map remains the faithful diagonal representation. This distinguishes the joint assertion from the two correct separate assertions.

**Weight-labelled functoriality, with its domains.** Fix a faithful normal semifinite weight \(\psi\) and temporarily use \(L=H_\psi\). Write

\[
 \mathfrak n_\psi=\{x:\psi(x^*x)<\infty\},\qquad
 \Lambda'_\psi(x)=J_\psi\Lambda_\psi(x^*)\quad(x\in\mathfrak n_\psi^*).
\]

FU-03 defines \(D(H,\psi)\) by the existence of \(C<\infty\) such that \(\|\xi x\|^2\leq C\psi(xx^*)\) for all \(x\in\mathfrak n_\psi^*\). Its bounded map satisfies

\[
 L_\psi(\xi)\Lambda'_\psi(x)=\xi x.
\]

For \(\xi\in D(H,\psi)\), the vector \(A\xi\) belongs to \(D(H',\psi)\), since
\(\|(A\xi)x\|\leq\|A\|\|\xi x\|\). Testing on that exact opposite GNS domain proves

\[
 L_\psi(A\xi)=A L_\psi(\xi),\qquad
 (A\boxtimes_N B)(\xi\otimes_\psi\eta)
       =A\xi\otimes_\psi B\eta.                                  \tag{AU.17}
\]

Here \(\eta\) is any vector of \(K\), and the right-bounded coordinate is the class of \(L_\psi(\xi)\odot\eta\).

For the left-bounded description, \(D'(K,\psi)\) consists of the \(\eta\) for which \(\|x\eta\|^2\leq C\psi(x^*x)\) on \(\mathfrak n_\psi\), and
\(R_\psi(\eta)\Lambda_\psi(x)=x\eta\). The same estimate and the left intertwining equation give

\[
 B\eta\in D'(K',\psi),\qquad R_\psi(B\eta)=B R_\psi(\eta).          \tag{AU.18}
\]

Formula (AU.17) therefore also holds for arbitrary \(\xi\in H\) and \(\eta\in D'(K,\psi)\), using the left model proved in FU-04. To verify its agreement without assuming an intersection of two domains is dense, first use (AU.17) for \(\xi\in D(H,\psi)\). FU-04 identifies its two meanings on that common domain. Then approximate an arbitrary \(\xi\) in Hilbert norm by vectors of \(D(H,\psi)\), which is dense by FU-03. The left-model bound \(\|\xi\otimes_\psi\eta\|\leq\|R_\psi(\eta)\|\|\xi\|\) and its target version with \(B\eta\) pass the identity to the limit. All operators in these statements are bounded; no unbounded modular endpoint is being used here.

## The standard units and arbitrary Hilbert sums

The standard bimodule is a unit for fusion through the specified maps

\[
 l_K:L\boxtimes_N K\longrightarrow K,\qquad
       l_K[\lambda(a)\odot\eta]=\lambda_K(a)\eta,                  \tag{AU.19}
\]

\[
 r_H:H\boxtimes_N L\longrightarrow H,\qquad
       r_H[T\odot u]=Tu.                                         \tag{AU.20}
\]

Both maps are onto unitaries. These formulas, not an arbitrary equivalence of representations, specify the units.

For the left unit, \(X_L=\rho(N)'=\lambda(N)\). The finite-sum norm identity from (AU.1) is

\[
 \left\|\sum_i[\lambda(a_i)\odot\eta_i]\right\|^2
 =\sum_{i,j}\langle\lambda_K(a_j^*a_i)\eta_i,\eta_j\rangle
 =\left\|\sum_i\lambda_K(a_i)\eta_i\right\|^2.                    \tag{AU.21}
\]

Thus the rule descends to the entire null quotient and extends isometrically to the completion. It has onto range already on its core, because \(l_K[1_L\odot\eta]=\eta\). Its inverse is \(\eta\mapsto[1_L\odot\eta]\).

For the right unit, use \(K=L\) in (AU.1):

\[
 \left\|\sum_i[T_i\odot u_i]\right\|^2
 =\sum_{i,j}\langle T_j^*T_i u_i,u_j\rangle
 =\left\|\sum_iT_i u_i\right\|^2.                                \tag{AU.22}
\]

It follows that (AU.20) descends to an isometry on the null quotient and extends to an isometry on the completion. Its range contains every \(Tu\), whose span is dense by FU-01. An isometry from a complete space has closed range: a Cauchy sequence in its range lifts to a Cauchy sequence in its domain. Its range is therefore all of \(H\). This argument uses totality for the actual normal module \(H\), without a faithful-action assumption or a chosen cyclic vector for the whole module.

The units preserve all indicated actions. For \(c\in N\),

\[
 l_K[\lambda(c)\lambda(a)\odot\eta]
       =\lambda_K(c)l_K[\lambda(a)\odot\eta],
\]

and every right outside action on \(K\) passes through (AU.19) because it commutes with \(\lambda_K(N)\). For a left outside operator \(d\) on \(H\), and for \(b\in N\),

\[
 r_H[dT\odot u]=d\,r_H[T\odot u],\qquad
 r_H[T\odot\rho(b)u]=T\rho(b)u=\rho_H(b)Tu.                       \tag{AU.23}
\]

Thus \(l_K\) is a unitary of the resulting \(N\)-outside bimodules, and \(r_H\) is a unitary of the resulting outside-\(N\) bimodules. Boundedness extends these identities from the displayed total sets.

For bounded module intertwiners \(A:H\to H'\) and \(B:K\to K'\), direct evaluation on those total sets gives

\[
 r_{H'}(A\boxtimes_N1_L)=A r_H,\qquad
 l_{K'}(1_L\boxtimes_N B)=B l_K.                                  \tag{AU.24}
\]

These are naturality for all bounded maps, including nonunitary maps. When both factors are \(L\), the two units agree: each sends \([\lambda(a)\odot u]\) to \(\lambda(a)u\). A further useful explicit identity is

\[
 r_H(1_H\boxtimes_N\rho(b))r_H^{-1}=\rho_H(b),                    \tag{AU.25}
\]

which follows from (AU.23). Its left counterpart is
\(l_K(\lambda(a)\boxtimes_N1_K)l_K^{-1}=\lambda_K(a)\).

**The faithful semifinite weight coordinates of the units.** Use \(L=H_\psi\) and the exact ideals specified above. FU-03 proves

\[
 L_\psi(\Lambda_\psi(y))=\pi_\psi(y)\quad(y\in\mathfrak n_\psi),
\]

so the left unit has the formula

\[
 l_K(\Lambda_\psi(y)\otimes_\psi\eta)=y\eta,\qquad
 y\in\mathfrak n_\psi,\quad\eta\in K.                             \tag{AU.26}
\]

Every displayed first vector is right \(\psi\)-bounded; its operator norm is \(\|y\|\). For a finite sum, the norm on the left is exactly \(\|\sum_i y_i\eta_i\|\), by (AU.21). The span of these images is dense even when \(\psi(1)=\infty\): WG-008 gives finite positive contractions \(e_\gamma\in\mathfrak n_\psi\) tending strongly* to one, and normality of the action gives \(e_\gamma\eta\to\eta\). FU-03's coefficient saturation identifies the whole weight-labelled completion with the all-intertwiner completion, so (AU.26) determines the same onto unit, rather than a smaller finite-weight subspace.

For the right unit, its defining bounded extension gives

\[
 r_H(\xi\otimes_\psi\Lambda'_\psi(x))=\xi x,\qquad
 \xi\in D(H,\psi),\quad x\in\mathfrak n_\psi^*.                    \tag{AU.27}
\]

More generally \(r_H(\xi\otimes_\psi u)=L_\psi(\xi)u\) for every \(u\in H_\psi\) and \(\xi\in D(H,\psi)\). The vectors in (AU.27) span a dense subspace of the completed domain: FU-03 supplies all right-bounded generators, and the opposite GNS vectors \(\Lambda'_\psi(x)\) are dense in \(H_\psi\), so (AU.2) approximates their second entries. Surjectivity is also visible in the displayed images: for fixed \(\xi\in D(H,\psi)\), the vectors \(\xi e_\gamma\to\xi\); these \(\xi\)'s are dense in \(H\).

The left-bounded coordinate makes (AU.27) valid for **every** \(\xi\in H\). Indeed, for \(x\in\mathfrak n_\psi^*\), FU-03 gives

\[
 \Lambda'_\psi(x)\in D'(H_\psi,\psi),\qquad
 R_\psi(\Lambda'_\psi(x))
      =J_\psi\pi_\psi(x^*)J_\psi=\rho(x).                         \tag{AU.28}
\]

The left-model symbol \(\xi\otimes_\psi\Lambda'_\psi(x)\) is therefore defined for arbitrary \(\xi\), and depends on it with norm at most \(\|x\|\|\xi\|\). On the dense subspace \(D(H,\psi)\) its meaning agrees with the right-model symbol, by FU-04, and (AU.27) holds. Hilbert-norm approximation in \(H\) extends that equality to every \(\xi\). This proof keeps the test ideal \(\mathfrak n_\psi^*\) and does not replace \(\Lambda'_\psi(x)\) by \(\Lambda_\psi(x)\).

For completeness, the left unit in the other coordinate is

\[
 l_K(u\otimes_\psi\eta)=R_\psi(\eta)u,\qquad
 u\in H_\psi,\quad\eta\in D'(K,\psi).                             \tag{AU.29}
\]

For \(u=\Lambda_\psi(y)\), \(y\in\mathfrak n_\psi\), this follows from (AU.26) and the definition of \(R_\psi(\eta)\). These GNS vectors are dense; both sides are bounded linear functions of \(u\), and the two meanings of the tensor agree on that domain by FU-04. This proves (AU.29) without an additional domain identification. For a previously fixed standard form \(L\), transport these formulas by the canonical bimodule unitary \(H_\psi\to L\); no identification of finite ideals for different weights is involved.

**Arbitrary direct sums.** Let \((H_i)_{i\in I}\) be any family of normal unital right \(N\)-modules, and let \((K_j)_{j\in J}\) be any family of normal unital left \(N\)-modules. Put

\[
 H=\bigoplus_{i\in I}H_i,\qquad K=\bigoplus_{j\in J}K_j.
\]

These are Hilbert direct sums: a vector's squared norm is the supremum of its finite partial sums of squared coordinate norms. Denote the canonical isometries by \(\iota_i:H_i\to H\) and \(\kappa_j:K_j\to K\). The coordinatewise actions are bounded, normal and unital. Boundedness follows from the uniform bound \(\|b\|\) for each coordinate action, and unitality is coordinatewise. To check normality, take \(0\leq b_\gamma\uparrow b\) in \(N\). Each coordinate action tends strongly to its value at \(b\). On a vector supported in finitely many coordinates this gives norm convergence by a finite sum; on an arbitrary vector, first approximate by its finite-coordinate projection and then use the uniform bound \(2\|b\|\). Thus the direct-sum action preserves this strong limit and hence this positive supremum. The argument works for the right action by viewing it as a representation of the opposite algebra.

There is a canonical onto unitary

\[
 \mathcal D:
 \bigoplus_{(i,j)\in I\times J}(H_i\boxtimes_N K_j)
       \longrightarrow
 \left(\bigoplus_iH_i\right)\boxtimes_N
       \left(\bigoplus_jK_j\right)                               \tag{AU.30}
\]

whose restriction to the \((i,j)\) summand is \(\iota_i\boxtimes_N\kappa_j\). If outside algebras act componentwise, this is a bimodule unitary.

To prove the assertion, write \(Z_{ij}=\iota_i\boxtimes_N\kappa_j\). Equations (AU.5–6) give

\[
 Z_{ij}^*Z_{k\ell}
    =(\iota_i^*\iota_k)\boxtimes_N(\kappa_j^*\kappa_\ell).
\]

This is the identity if \((i,j)=(k,\ell)\) and is zero otherwise. Thus the maps \(Z_{ij}\) are isometries with pairwise orthogonal ranges. Their sum on finitely supported families preserves the sum of squared norms, and extends to the isometry (AU.30).

For onto, let \(F\subset I\) and \(G\subset J\) be finite and set

\[
 P_F=\sum_{i\in F}\iota_i\iota_i^*,\qquad
 Q_G=\sum_{j\in G}\kappa_j\kappa_j^*.
\]

The nets of **all** finite subsets, ordered by inclusion, satisfy \(P_F\to1_H\) and \(Q_G\to1_K\) strongly*. These projections commute with the respective module actions. For every \(T\in X_H\) and \(\eta\in K\), the vector

\[
 [P_F T\odot Q_G\eta]
 =\sum_{i\in F,\,j\in G}
      Z_{ij}[\iota_i^*T\odot\kappa_j^*\eta]                       \tag{AU.31}
\]

lies in the range of \(\mathcal D\). Every term is eligible: \(\iota_i^*T\in X_{H_i}\). Moreover

\[
 \begin{split}
 \|[T\odot\eta]-[P_F T\odot Q_G\eta]\|
 &\leq\|[(1-P_F)T\odot\eta]\|\\
 &\quad+\|T\|\|(1-Q_G)\eta\|\longrightarrow0
 \end{split}                                                       \tag{AU.32}
\]

over the product directed set of finite pairs \((F,G)\). For the first term, \(P_F T\to T\) strongly*, with norm at most \(\|T\|\), because \((P_F T)^*=T^*P_F\). Thus (AU.3) applies. Equivalently, the square of that term is the coefficient evaluation

\[
 \left\langle\lambda_K\!\left(
       \lambda^{-1}(T^*(1-P_F)T)\right)\eta,\eta\right\rangle
 \longrightarrow0.                                                \tag{AU.33}
\]

The second term in (AU.32) is ordinary Hilbert-norm convergence. Each is independent of the other finite index. Hence every elementary class belongs to the closure of the range, and those classes have total span. The range of an isometry from a complete Hilbert space is closed, so \(\mathcal D\) is onto. No enumeration of \(I\) or \(J\), or countable cofinal subnet, was introduced.

Its inverse on an elementary class is the square-summable family

\[
 \mathcal D^{-1}[T\odot\eta]
     =\big([\iota_i^*T\odot\kappa_j^*\eta]\big)_{i,j}.             \tag{AU.34}
\]

Indeed the \((i,j)\) coordinate is \(Z_{ij}^*[T\odot\eta]\) by (AU.4–5). Orthogonality gives the finite partial squared norms, and (AU.32) shows that their supremum is \(\|[T\odot\eta]\|^2\). Finite rectangles suffice here because every finite subset of \(I\times J\) is contained in a finite rectangle. This proves both square summability and the displayed inverse, rather than presuming that a formal infinite sum is defined.

Taking \(I\) or \(J\) to be a singleton gives the two separate direct-sum laws. Taking either index set to be empty gives zero on both sides. The argument also covers zero summands and a vanishing fusion of two nonzero modules. On the zero Hilbert space, the identity is the zero operator, so the stated unitality and unitary conclusions have their literal zero-space meanings.

**Naturality of the sum comparison.** Suppose \(A_i:H_i\to H'_i\) and \(B_j:K_j\to K'_j\) are module intertwiners with
\(\sup_i\|A_i\|<\infty\) and \(\sup_j\|B_j\|<\infty\). These are exactly the bounds needed to form the bounded diagonal sums \(A=\bigoplus_iA_i\), \(B=\bigoplus_jB_j\). The family \(A_i\boxtimes_N B_j\) is uniformly bounded by (AU.5). Its direct sum consequently exists, and

\[
 (A\boxtimes_N B)\mathcal D
   =\mathcal D'\left(\bigoplus_{i,j}(A_i\boxtimes_N B_j)\right).    \tag{AU.35}
\]

On the \((i,j)\) summand this is (AU.6) and the identities \(A\iota_i=\iota'_iA_i\), \(B\kappa_j=\kappa'_jB_j\). Finite-support density extends it to the whole sum. In particular it proves the bimodule assertion in (AU.30) by using the componentwise outside actions, whose norms have the common algebra bound.

The units also commute with these sum comparisons. For example, identify \((\bigoplus_iH_i)\boxtimes_N L\) with \(\bigoplus_i(H_i\boxtimes_N L)\) by (AU.30) with a singleton second family. The right unit then becomes \(\bigoplus_i r_{H_i}\): both maps send a generator in the \(i\)-th summand to \(\iota_iTu\), by (AU.20). The corresponding left-unit assertion follows from (AU.19). These identities hold first on finite-support generators and then by continuity.

**Bounded-vector domains in a direct sum.** The sum law identifies completed spaces; it does not say that any family of coordinatewise bounded vectors is a bounded vector in the sum. Here is the exact criterion. Let \(\xi=(\xi_i)\in\bigoplus_iH_i\), and suppose every \(\xi_i\in D(H_i,\psi)\). Put \(T_i=L_\psi(\xi_i)\). Then

\[
 \xi\in D(H,\psi)
 \quad\Longleftrightarrow\quad
 C:=\sup_{\substack{F\subset I\\ F\text{ finite}}}
          \left\|\sum_{i\in F}T_i^*T_i\right\|<\infty.             \tag{AU.36}
\]

When these conditions hold,

\[
 L_\psi(\xi)u=(T_i u)_i,\qquad
 \|L_\psi(\xi)\|^2=C.                                            \tag{AU.37}
\]

For the forward implication, coordinate projection in (AU.17) gives \(T_i=\iota_i^*L_\psi(\xi)\). Hence \(\sum_{i\in F}T_i^*T_i=L_\psi(\xi)^*P_F L_\psi(\xi)\), bounded by \(\|L_\psi(\xi)\|^2\). These operators converge strongly to \(L_\psi(\xi)^*L_\psi(\xi)\), and their quadratic forms show that the supremum of their norms is its norm. For the reverse implication, the finite-sum bound says
\(\sum_i\|T_i u\|^2\leq C\|u\|^2\) for every \(u\in H_\psi\), with the sum defined as the supremum of finite sums. Thus the column in (AU.37) is a bounded operator. On \(u=\Lambda'_\psi(x)\), \(x\in\mathfrak n_\psi^*\), its coordinates are \(\xi_i x\), so it is exactly \(\xi x\). This is the defining estimate and determines \(L_\psi(\xi)\). Taking the supremum over unit vectors and finite subsets proves its norm formula. Notice that membership of \(\xi\) in the Hilbert direct sum is part of the assertion's hypothesis.

The left version replaces \(T_i\) by \(R_\psi(\eta_j)\) and has the same proof on \(\Lambda_\psi(\mathfrak n_\psi)\). In particular, if \(\xi\in D(H,\psi)\) and \(\eta=(\eta_j)\in K\), (AU.34) takes the weight-coordinate form

\[
 \mathcal D^{-1}(\xi\otimes_\psi\eta)
       =(\xi_i\otimes_\psi\eta_j)_{i,j}.                          \tag{AU.38}
\]

Eligibility follows from the coordinate projection identity, and square summability follows from (AU.34), not from a separate assumption about coordinate tensor norms. The analogous left-coordinate formula holds for \(\xi\in H\) and \(\eta\in D'(K,\psi)\).

These proofs supply exactly the action and unit interfaces used by the creation and associativity components: bounded functoriality with adjoints, separately normal commuting actions, the onto maps (AU.19–20), their naturality, and the compatibility of those maps with arbitrary sums. They do not prove the separate modular endpoint balancing law, reference-weight change, or the later associator. They use the fixed faithful reference weights only for coordinate formulas; faithfulness or countability of module actions was never added.

## Creation operators and associativity

The next two steps use the preceding fusion and standard-module results to construct creation operators, the associator, and its coherence maps.

Throughout, Hilbert inner products are linear in the first variable. All algebras are von Neumann algebras, and all module actions are normal and unital. They may have kernels. There is no restriction on cardinality, separability or sigma-finiteness. For a right action, write \(\xi b=\rho_E(b)\xi\), where \(\rho_E\) is a complex-linear anti-representation. Use faithful normal semifinite reference weights when using weight-labelled coordinates.

### Contracts used from the preceding construction

Fix a standard bimodule \(L_A\) for every intermediate algebra \(A\), with faithful left representation \(\lambda_A\), right action \(\rho_A\), and \(\lambda_A(A)=\rho_A(A)'\). Put

\[
 X_E^A=\operatorname{Hom}_{A^{\mathrm{op}}}(L_A,E)
\]

for a right \(A\)-module \(E\). An intertwiner is a bounded, everywhere-defined Hilbert-space operator. The fusion \(E\boxtimes_A F\) of a right \(A\)-module and a left \(A\)-module is the completion of the null quotient of \(X_E^A\odot F\), with

\[
 \left\langle\sum_i T_i\otimes\eta_i,\sum_j U_j\otimes\theta_j\right\rangle
 =\sum_{i,j}
 \left\langle
 \lambda_F\!\left(\lambda_A^{-1}(U_j^*T_i)\right)\eta_i,\theta_j
 \right\rangle.                                                     \tag{F.1}
\]

The symbol \(\otimes\) in this component denotes the class in this quotient, so it does not assert that the algebraic tensor map is injective.

The preceding blocks supply the positive form, completion and ordinary intertwiner balancing

\[
 (T\lambda_A(a))\otimes\eta=T\otimes\lambda_F(a)\eta;                 \tag{F.2}
\]

the bounded functorial action of intertwiners, its adjoint and composition rules; normal unital induced actions of commuting algebras; and the two unitary unit maps

\[
 r_E:E\boxtimes_A L_A\longrightarrow E,\quad r_E(T\otimes u)=Tu,
 \qquad
 l_F:L_A\boxtimes_A F\longrightarrow F,\quad
 l_F(\lambda_A(a)\otimes\eta)=\lambda_F(a)\eta.                      \tag{F.3}
\]

Intertwiners from \(L_A\) have total ranges in every normal unital right module; the analogous assertion holds for left modules. These statements cover nonfaithful module actions.

For a faithful normal semifinite weight \(\omega\) on \(A\), put the chosen standard bimodule in its GNS coordinates \(L_A=H_\omega\). The preceding bounded-vector dictionary supplies

\[
 \Lambda'_\omega(x)=J_\omega\Lambda_\omega(x^*),\qquad
 L_\omega(\xi)\Lambda'_\omega(x)=\xi x
       \quad(x\in\mathfrak n_\omega^*).                            \tag{F.4}
\]

Thus \(D(E,\omega)\) consists of the \(\xi\) for which this map is bounded. It also supplies positive contractions \(f_j\in\mathfrak n_\omega\) with \(f_j\to1\) strongly*, and, for every \(S\in X_E^A\),

\[
 \eta_j=S\Lambda_\omega(f_j)\in D(E,\omega),\qquad
 L_\omega(\eta_j)=S\lambda_A(f_j).                                  \tag{F.5}
\]

The same net works for every finite family \(S\). In particular these operators tend strongly*, with norm at most \(\|S\|\), to \(S\). In the opposite orientation, for

\[
 Y_F^A=\operatorname{Hom}_A(L_A,F)
\]

the left-bounded map is

\[
 R_\omega(\zeta)\Lambda_\omega(x)=x\zeta
       \quad(x\in\mathfrak n_\omega).
                                                                    \tag{F.6}
\]

Every \(V\in Y_F^A\) has bounded strong* approximants of the form \(R_\omega(\zeta_j)\). The specific version \(V\rho_A(f_j)\), with \(\zeta_j=VJ_\omega\Lambda_\omega(f_j)\), follows from the standard left/right dictionary. No assertion identifies finite ideals for distinct weights.

The topology used below is supplied by OA-MOD-NP-06 and OA-MOD-WH-02: a faithful normal representation identifies bounded strong* convergence with the corresponding intrinsic sigma-strong* convergence, and every normal representation preserves that convergence. The bounded support and resolvent facts are those of OA-MOD-BK-01 and the positive-support cutoff lemma in that unit.

## Creation operators and saturation in a subsequent fusion

Let \(H_M\) and \({}_M K_N\) be as above, and set \(F=H\boxtimes_M K\). For \(T\in X_H^M\), define

\[
 C_T:K\longrightarrow F,\qquad C_T\eta=T\otimes\eta.                 \tag{F.7}
\]

The case of an outer weight-bounded vector is \(C_\xi=C_{L_\varphi(\xi)}\).

**Creation formulas.** The operator \(C_T\) is bounded, with \(\|C_T\|\le\|T\|\), is right \(N\)-linear, and satisfies

\[
 C_U^*C_T=\lambda_K\!\left(\lambda_M^{-1}(U^*T)\right),\qquad
 C_U^*(T\otimes\eta)
 =\lambda_K\!\left(\lambda_M^{-1}(U^*T)\right)\eta.                  \tag{F.8}
\]

If \(\Phi:\operatorname{End}_{M^{\mathrm{op}}}(H)\to
\operatorname{End}_{N^{\mathrm{op}}}(F)\) is the induced normal action, then

\[
 C_T C_U^*=\Phi(TU^*),\qquad
 \Phi(a)C_T=C_{aT}.                                                 \tag{F.9}
\]

Indeed, (F.1) gives both the norm bound and (F.8). The induced right action gives
\(C_T(\eta b)=(C_T\eta)b\). To verify the first equality of (F.9), apply its two sides to \(S\otimes\eta\). By (F.8) and (F.2), the first gives

\[
 T\otimes\lambda_K(\lambda_M^{-1}(U^*S))\eta
 =(TU^*S)\otimes\eta,
\]

which is the second. These vectors span a dense space. The remaining equality follows directly from the definition of the induced action. In particular all adjoints and products in (F.8)–(F.9) are bounded operators between the indicated Hilbert spaces.

**A total creation family yields a bounded approximation.** Let
\(\mathcal T\subseteq X_H^M\) be any set for which the ranges of \(C_T\), \(T\in\mathcal T\), have dense linear span in \(F\). This includes all \(X_H^M\), and also all \(L_\varphi(\xi)\), \(\xi\in D(H,\varphi)\): for the latter assertion, (F.5) and (F.1) approximate each \(T\otimes\eta\).

For a finite subset \(D\subseteq\mathcal T\) and \(\varepsilon>0\), put

\[
 P_D=\sum_{T\in D}C_T C_T^*,\qquad
 E_{D,\varepsilon}=P_D(P_D+\varepsilon I_F)^{-1}.                    \tag{F.10}
\]

These are right \(N\)-linear positive contractions. Direct the pairs by enlarging \(D\) and decreasing \(\varepsilon\). Then

\[
 E_{D,\varepsilon}\longrightarrow I_F\quad\hbox{strongly*}.          \tag{F.11}
\]

Here is the order and density justification. If \(0\le P\le Q\), then
\((Q+\varepsilon I)^{-1}\le(P+\varepsilon I)^{-1}\); one obtains this inequality by conjugating by \((P+\varepsilon I)^{-1/2}\) and using the scalar inverse function on a positive operator bounded below by \(I\). Since \(P(P+\varepsilon I)^{-1}=I-\varepsilon(P+\varepsilon I)^{-1}\), (F.10) increases with \(D\), and scalar functional calculus shows that it increases when \(\varepsilon\) decreases. The strong limit \(E\) of this bounded increasing net therefore exists. For each fixed finite \(D\), the support cutoff formula gives

\[
 E\ge s(P_D).
\]

Moreover

\[
 \ker P_D=\bigcap_{T\in D}\ker C_T^*
\]

by the sum of the squared norms \(\|C_T^*v\|^2\). Thus the closed linear span of the ranges \(s(P_D)F\), over all finite \(D\), is \(F\). A positive contraction which majorizes a projection acts as the identity on its range: compress \(I-E\), take its positive square root, and obtain \((I-E)p=0\). Consequently \(E=I_F\). The operators are self-adjoint, so their strong convergence is strong* convergence. This reasoning uses the full directed set; no countable total family is selected.

Let \(R:L_N\to F\) be any bounded right \(N\)-module intertwiner. Set

\[
 R_{D,\varepsilon}=E_{D,\varepsilon}R
 =\sum_{T\in D} C_T S_{D,\varepsilon,T},\qquad
 S_{D,\varepsilon,T}
 =C_T^*(P_D+\varepsilon I_F)^{-1}R.                                  \tag{F.12}
\]

Each \(S_{D,\varepsilon,T}\) belongs to \(X_K^N\): every factor is right \(N\)-linear, including the inverse, by bounded functional calculus in the commutant. The expansion is the equality
\(P_D(P_D+\varepsilon I)^{-1}R
=\sum_T C_TC_T^*(P_D+\varepsilon I)^{-1}R\).
In particular

\[
 \|R_{D,\varepsilon}\|\le\|R\|,\qquad
 R_{D,\varepsilon}\to R\quad\hbox{strongly*}.                         \tag{F.13}
\]

For the adjoints, use \(R_{D,\varepsilon}^*=R^*E_{D,\varepsilon}\). The rectangular strong* topology means strong convergence of the operators on \(L_N\) and of their adjoints on \(F\).

If \({}_N Z\) is any normal unital left module, (F.13) implies

\[
 R_{D,\varepsilon}\otimes z\longrightarrow R\otimes z
       \quad\hbox{in }F\boxtimes_N Z.                               \tag{F.14}
\]

To check the topology rather than merely infer it from Hilbert-space density, put \(Q_{D,\varepsilon}=R_{D,\varepsilon}-R\). Its norms are at most \(2\|R\|\), and \(Q_{D,\varepsilon}^*Q_{D,\varepsilon}\to0\) strongly in the faithful concrete algebra \(\lambda_N(N)\). It is self-adjoint, hence strongly* null. Transport through \(\lambda_N^{-1}\), then through the normal left action on \(Z\). Formula (F.1) now gives

\[
 \|Q_{D,\varepsilon}\otimes z\|^2
 =
 \left\langle
 \lambda_Z\!\left(\lambda_N^{-1}
       (Q_{D,\varepsilon}^*Q_{D,\varepsilon})\right)z,z
 \right\rangle\longrightarrow0.                                   \tag{F.15}
\]

Finite sums follow by the triangle inequality and the common directed set. It follows that

\[
 \operatorname{span}
 \{(C_T S)\otimes z:T\in\mathcal T,\ S\in X_K^N,\ z\in Z\}
 \quad\hbox{is dense in }F\boxtimes_N Z.                            \tag{F.16}
\]

This is a statement about a subsequent fusion norm, not just the norm on \(F\).

**Weight-bounded iterated generators and one common cutoff.** Choose
\(\mathcal T=\{L_\varphi(\xi):\xi\in D(H,\varphi)\}\) in (F.12), writing \(C_\xi\) for its members. Use a fixed faithful normal semifinite weight \(\psi\) on \(N\) and the common cutoff \(f_j\) in (F.5). For each of the finitely many maps \(S_T\) in (F.12), set

\[
 \eta_{T,j}=S_T\Lambda_\psi(f_j),\qquad
 L_\psi(\eta_{T,j})=S_T\lambda_N(f_j).
\]

Then \(C_\xi\eta_{T,j}\) is itself right \(\psi\)-bounded. On the exact opposite GNS domain,

\[
 (C_\xi\eta_{T,j})x=C_\xi(\eta_{T,j}x),
 \qquad
 L_\psi(C_\xi\eta_{T,j})=C_\xi L_\psi(\eta_{T,j}).                    \tag{F.17}
\]

The boundedness estimate follows by multiplying that for \(\eta_{T,j}\) by \(\|C_\xi\|\), so this identity proves eligibility as well as equality of the extensions.

All finite terms use the same \(f_j\). Accordingly their sum is

\[
 \sum_{T\in D}L_\psi(C_\xi\eta_{T,j})
 =E_{D,\varepsilon}R\lambda_N(f_j),\qquad
 \left\|\sum_{T\in D}L_\psi(C_\xi\eta_{T,j})\right\|\le\|R\|.         \tag{F.18}
\]

Over the product directed set, the last operators tend strongly* to \(R\): their two outside factors are contractions converging strongly* to the identity. This is why independently approximating each term with unrelated choices is unnecessary. Applying (F.15) proves that the eligible tensors

\[
 (\xi\otimes_\varphi\eta)\otimes_\psi z,\qquad
 \xi\in D(H,\varphi),\quad \eta\in D(K,\psi),\quad z\in Z,
                                                                    \tag{F.19}
\]

have dense linear span in the left-associated fusion. Here the middle vector is bounded only for its right \(N\)-action; no simultaneous left-boundedness is asserted.

Finally, (F.9) identifies (F.10) with the induced bounded functional calculus of \(\sum L_\varphi(\xi)L_\varphi(\xi)^*\) on \(H\). These operators preserve creation form:

\[
 \Phi(a)C_\xi=C_{a\xi},\qquad
 L_\varphi(a\xi)=aL_\varphi(\xi)
 \quad(a\in\operatorname{End}_{M^{\mathrm{op}}}(H)).
\]

The last identity again follows by testing \(\Lambda'_\varphi(x)\). This supplies the advertised creation-operator realization of the approximation. \(\square\)

## The associator, its bounded-vector formula and coherence

For \(H_M\), \({}_M K_N\), and \({}_N Z\), there is a unique unitary

\[
 a_{H,K,Z}:
 (H\boxtimes_M K)\boxtimes_N Z
 \longrightarrow
 H\boxtimes_M(K\boxtimes_N Z)                                      \tag{F.20}
\]

satisfying

\[
 a_{H,K,Z}\big((C_T S)\otimes z\big)
       =T\otimes(S\otimes z),
 \quad T\in X_H^M,\quad S\in X_K^N,\quad z\in Z.                    \tag{F.21}
\]

It intertwines every commuting outside action, is natural in bounded module intertwiners, and satisfies the pentagon and the unit triangle.

**Construction and exact coefficient pairing.** Every operator \(C_T S:L_N\to H\boxtimes_M K\) in (F.21) is bounded and right \(N\)-linear by FU-07. Thus its left side is an eligible all-intertwiner generator. For finite families \(T_i,S_i,z_i\) and \(U_j,V_j,w_j\), put

\[
 a_{ji}=\lambda_M^{-1}(U_j^*T_i),\qquad
 b_{ji}=\lambda_N^{-1}\!\left(V_j^*\lambda_K(a_{ji})S_i\right).
                                                                    \tag{F.22}
\]

The second inverse is well-typed: \(\lambda_K(a_{ji})\) commutes with the right \(N\)-action, so its displayed compression belongs to \(\rho_N(N)'=\lambda_N(N)\). In the left bracketing the coefficient is exactly

\[
 (C_{U_j}V_j)^*(C_{T_i}S_i)
       =V_j^*C_{U_j}^*C_{T_i}S_i
       =V_j^*\lambda_K(a_{ji})S_i.
\]

In the right bracketing, first apply (F.1) for \(M\). The induced left \(M\)-action on \(K\boxtimes_N Z\) sends
\(S_i\otimes z_i\) to \((\lambda_K(a_{ji})S_i)\otimes z_i\).
Applying (F.1) for \(N\) then shows that both pairings are

\[
 \sum_{i,j}\langle\lambda_Z(b_{ji})z_i,w_j\rangle.                   \tag{F.23}
\]

This calculation includes all cross terms; it proves that any null relation in the left core is sent to a null relation on the right. Hence (F.21) defines an isometry of the quotient core. The left core is dense by (F.16). On the right, the vectors \(S\otimes z\) span a dense subspace of \(K\boxtimes_N Z\), and the bounded operators \(C_T\) map their span to a total subspace of the right bracketing. The image core is therefore dense too. The isometry extends to the unitary (F.20), and left-core density gives uniqueness.

**A left creation map and the source's outer-bounded display.** For any right \(N\)-module \(E\) and any
\(V\in Y_Z^N=\operatorname{Hom}_N(L_N,Z)\), define the bounded map

\[
 D_V^E:E\longrightarrow E\boxtimes_N Z,\qquad
 D_V^E=(1_E\boxtimes_N V)r_E^{-1}.                                 \tag{F.24}
\]

Thus \(\|D_V^E\|\le\|V\|\), and for \(R\in X_E^N\), \(u\in L_N\),

\[
 D_V^E(Ru)=R\otimes Vu.                                             \tag{F.25}
\]

This follows from \(r_E(R\otimes u)=Ru\) and the defined functorial map. Formula (F.25) determines \(D_V^E\) since the \(Ru\) span a dense subspace of \(E\). For \(V,W\in Y_Z^N\), write

\[
 b=\rho_N^{-1}(W^*V).
\]

Then

\[
 (D_W^E)^*D_V^E=\rho_E(b).                                         \tag{F.26}
\]

Indeed, by the adjoint and composition laws its left side is
\(r_E(1_E\boxtimes_N W^*V)r_E^{-1}\). On \(Ru\) this is
\(R\rho_N(b)u=(Ru)b\), since \(R\) is right \(N\)-linear. This proves (F.26) on a total set.

In particular the left model has the exact first-variable-linear form

\[
 \left\langle\sum_i D_{V_i}^E\xi_i,\sum_jD_{W_j}^E\chi_j\right\rangle
 =\sum_{i,j}
   \left\langle \xi_i\,\rho_N^{-1}(W_j^*V_i),\chi_j\right\rangle.     \tag{F.27}
\]

The order \(W_j^*V_i\) is essential. To see that these left generators are total, use totality of left intertwiners: approximate an arbitrary \(z\in Z\) by finite sums \(Vu\), then use (F.25) on \(R\otimes z\). Formula (F.27) therefore identifies the entire completed left model with the fusion already constructed. This short proof uses the proved standard right unit, and does not presume an intersection of two bounded-vector domains.

For \(T\in X_H^M\), \(\eta\in K\), and \(V\in Y_Z^N\), both terms in

\[
 a_{H,K,Z}\big(D_V^{H\boxtimes_M K}(C_T\eta)\big)
       =C_T^{\,K\boxtimes_N Z}\big(D_V^K\eta\big)                   \tag{F.28}
\]

are defined by bounded maps. Superscripts only specify the creation map's target. First check \(\eta=Su\), with \(S\in X_K^N\) and \(u\in L_N\). Equations (F.25) and (F.21) turn the left side into

\[
 a_{H,K,Z}\big((C_T S)\otimes Vu\big)
   =T\otimes(S\otimes Vu)
   =C_T^{\,K\boxtimes_N Z}(D_V^K(Su)).
\]

Intertwiner totality and boundedness extend this equality to every \(\eta\in K\).

The pairing on this mixed core can also be checked directly. For first data \((T_i,\eta_i,V_i)\) and second data \((U_j,\theta_j,W_j)\), put

\[
 a_{ji}=\lambda_M^{-1}(U_j^*T_i),\qquad
 d_{ji}=\rho_N^{-1}(W_j^*V_i).
\]

Both bracketings have the exact pairing

\[
 \sum_{i,j}
 \left\langle
   \lambda_K(a_{ji})\rho_K(d_{ji})\eta_i,\theta_j
 \right\rangle.                                                   \tag{F.29}
\]

For the left bracketing use (F.26), right \(N\)-linearity of \(C_T\), then (F.8). For the right bracketing use (F.8) for the outer creation, move the induced left \(M\)-action through \(D_V^K\), then use (F.26). The latter commutation follows from (F.25), since \(\lambda_K(a)S\) is again right \(N\)-linear. Finally the left \(M\)-action and right \(N\)-action on \(K\) commute, giving precisely (F.29).

To express (F.28) in the source's coordinates, set

\[
 T=L_\varphi(\xi),\quad \xi\in D(H,\varphi),\qquad
 V=R_\psi(\zeta),\quad \zeta\in D'(Z,\psi),
\]

where \(D'\) uses the exact estimate behind (F.6). The all-intertwiner and left-model comparisons identify (F.28) with

\[
 a_{H,K,Z}\big((\xi\otimes_\varphi\eta)\otimes_\psi\zeta\big)
       =\xi\otimes_\varphi(\eta\otimes_\psi\zeta),
 \quad \eta\in K.                                                  \tag{F.30}
\]

The first \(\psi\)-tensor on the left is interpreted in the proved left-bounded model because \(\zeta\) is left \(\psi\)-bounded. It does not assert that \(\xi\otimes_\varphi\eta\) is right \(\psi\)-bounded for every \(\eta\).

These mixed weight-bounded generators are dense in both bracketings. For completeness, bounded strong* convergence \(V_\alpha\to V\) in \(Y_Z^N\) gives \(D_{V_\alpha}^E\to D_V^E\) strongly: apply (F.26) to the difference, transport
\((V_\alpha-V)^*(V_\alpha-V)\) through the faithful opposite-algebra representation \(\rho_N\), and then through the normal right action on \(E\). The norm bound from (F.24) and (F.6)'s approximation give totality using only \(R_\psi(\zeta)\). Similarly (F.5) and (F.1) give totality using only \(L_\varphi(\xi)\). In the left bracketing, first use totality of the \(D_{R_\psi(\zeta)}^F\), then approximate their arguments in \(F\) by \(C_{L_\varphi(\xi)}\eta\); the \(D\)'s are bounded. In the right bracketing, reverse these two stages. Thus no density of an unproved jointly bounded intersection is used.

**Naturality and outside actions.** Let \(A:H\to H'\) be right \(M\)-linear, \(B:K\to K'\) be \(M\)-\(N\)-linear, and \(C:Z\to Z'\) be left \(N\)-linear, all bounded. The functorial action satisfies

\[
 (A\boxtimes_M B)C_T=C_{AT}B.                                      \tag{F.31}
\]

Both sides have value \(AT\otimes B\eta\) on \(\eta\). On (F.21), the two compositions in the naturality square therefore both give

\[
 AT\otimes(BS\otimes Cz).
\]

Boundedness and left-core density prove

\[
 a_{H',K',Z'}\big((A\boxtimes_M B)\boxtimes_N C\big)
 =
 \big(A\boxtimes_M(B\boxtimes_N C)\big)a_{H,K,Z}.                    \tag{F.32}
\]

Taking \(B\) to be an identity and \(A,C\) to be the prescribed outside actions shows that the associator is a bimodule unitary, including for the full module-endomorphism actions in the source statement.

**A common fourfold core.** Let

\[
 H_M,\qquad {}_M K_N,\qquad {}_N Z_P,\qquad {}_P W.
\]

Choose \(T\in X_H^M\), \(S\in X_K^N\), \(R\in X_Z^P\), and \(w\in W\). Put

\[
 Q=C_T S:L_N\to H\boxtimes_M K,\qquad
 V=C_Q R:L_P\to(H\boxtimes_M K)\boxtimes_N Z.                        \tag{F.33}
\]

Both are module intertwiners by FU-07. The vectors

\[
 V\otimes w                                                       \tag{F.34}
\]

span a dense subspace of the fully left-associated product.

Here is an explicit iterated density proof. By (F.16), the operators
\(Q=C_T S\) have creation maps \(C_Q:Z\to
(H\boxtimes_M K)\boxtimes_N Z\) with total ranges. Apply the general total-family version of (F.10)–(F.16) to this family of creation maps and the following fusion over \(P\). It gives density of
\((C_Q R)\otimes w\), exactly (F.34). This application only requires a total creation family, as proved above; it does not require every right \(N\)-intertwiner into \(H\boxtimes_M K\) to be a single \(C_T S\).

The same abstract finite lists of \((T,S,R,w)\) evaluate in all five bracketings by the formulas in the following pentagon calculation. Every evaluation has the same finite-sum pairing. Specifically, for first data \((T_i,S_i,R_i,w_i)\) and second data \((U_j,V_j,Q_j,v_j)\), define

\[
 \begin{split}
 a_{ji}&=\lambda_M^{-1}(U_j^*T_i),\\
 b_{ji}&=\lambda_N^{-1}\!\left(V_j^*\lambda_K(a_{ji})S_i\right),\\
 c_{ji}&=\lambda_P^{-1}\!\left(Q_j^*\lambda_Z(b_{ji})R_i\right).
 \end{split}
\]

Repeated use of (F.23) gives, in every bracketing,

\[
 \sum_{i,j}\langle\lambda_W(c_{ji})w_i,v_j\rangle.                   \tag{F.35}
\]

All three inverses are taken on the specified standard commutants. This is a common quotient core, with one common nullspace, rather than a claim that independently chosen unbounded domains intersect densely.

**The pentagon.** Write the initial core vector as \((C_{C_T S}R)\otimes w\). Along the route through

\[
 ((H\boxtimes K)\boxtimes Z)\boxtimes W
 \longrightarrow
 (H\boxtimes(K\boxtimes Z))\boxtimes W
 \longrightarrow
 H\boxtimes((K\boxtimes Z)\boxtimes W)
 \longrightarrow
 H\boxtimes(K\boxtimes(Z\boxtimes W)),
\]

the first map gives

\[
 (C_T C_S R)\otimes w.
\]

Indeed, for each \(u\in L_P\), (F.21) gives the operator identity

\[
 a_{H,K,Z}\,C_{C_T S}R\,u
       =T\otimes(S\otimes Ru)
       =C_T C_S R\,u.
\]

The next map gives \(T\otimes((C_S R)\otimes w)\), and the last gives

\[
 T\otimes(S\otimes(R\otimes w)).                                   \tag{F.36}
\]

Here each \(C_T\) has the target dictated by its bracketing.

Along the other route, the first associator gives

\[
 (C_T S)\otimes(R\otimes w)
 \quad\hbox{in }(H\boxtimes K)\boxtimes(Z\boxtimes W),
\]

and the second gives the same expression (F.36). These are applications of (F.21) with respectively first module \(H\boxtimes K\), and third module \(Z\boxtimes W\). All maps are unitaries. Equality on (F.34) therefore proves the pentagon on the completed spaces:

\[
 (1_H\boxtimes a_{K,Z,W})\,a_{H,K\boxtimes Z,W}\,
          (a_{H,K,Z}\boxtimes1_W)
 =
 a_{H,K,Z\boxtimes W}\,a_{H\boxtimes K,Z,W}.                        \tag{F.37}
\]

The suppressed algebra subscripts are \(M,N,P\) in their uniquely typed positions. The images of the dense core along these unitary maps are dense in each of the five bracketings, proving the asserted common-core density as well as its coefficient formula.

**Associativity coherence.** Both routes carry the common dense generator \(V\otimes w\), where \(Q=C_TS\) and \(V=C_QR\), to \(T\otimes(S\otimes(R\otimes w))\). Their common finite-sum coefficient is (F.35). This is the map equality (F.37), extending the associativity context of Takesaki II, IX.3, Theorem 3.20 (printed pp. 203–204).

**The triangle.** For \(H_M\) and \({}_M K\), consider the two maps

\[
 (H\boxtimes_M L_M)\boxtimes_M K\longrightarrow H\boxtimes_M K.
\]

Take \(T\in X_H^M\), \(a\in M\), \(\eta\in K\). The core vectors
\((C_T\lambda_M(a))\otimes\eta\) are dense by (F.16), because
\(X_{L_M}^M=\lambda_M(M)\). Applying \(r_H\boxtimes1_K\) gives
\((T\lambda_M(a))\otimes\eta\), since \(r_HC_T=T\). Applying first the associator and then \(1_H\boxtimes l_K\) gives
\(T\otimes\lambda_K(a)\eta\). These are equal by (F.2). Hence

\[
 (1_H\boxtimes_M l_K)a_{H,L_M,K}
       =r_H\boxtimes_M1_K.                                        \tag{F.38}
\]

This proves the triangle with the actual unit formulas, without replacing them by unspecified equivalences.

All arguments remain valid when a module is zero or a resulting fusion vanishes: the quotient Hilbert spaces and totality statements then have their literal zero-space meaning, and the unique map of zero spaces is unitary. No faithfulness of module actions, common cyclic vector, trace, countable family, or intersection of unbounded domains was used. \(\square\)

### Source context and proof boundaries

The source statement corresponding to (F.20) and (F.30) is Takesaki II, IX.3, Theorem 3.20, printed pp. 203–204 / PDF pp. 223–224. The proof above supplies explicit eligibility and dense range, as well as the displayed coefficient comparison. Pentagon, triangle and all-intertwiner saturation are additional consequences proved here.

The proof uses (F.1)–(F.6), established earlier in this unit, and proves creation saturation, common-core density, the associator and coherence. Its use of faithful reference weights does not define a nonfaithful-reference-weight model.

## Balancing at the half-strip endpoint

The following theorem establishes balancing on the full stated modular endpoint domain. It uses the modular and GNS results listed in section 8 below. All Hilbert inner products are linear in the first variable.

### 1. Conventions and the theorem

Let \(N\) be any von Neumann algebra and let \(\psi\) be a faithful normal semifinite weight. Use its standard GNS realization

\[
 (\pi_\psi,H_\psi,\Lambda_\psi,J_\psi,\Delta_\psi),\qquad
 \sigma_t^\psi=\operatorname{Ad}\Delta_\psi^{it},
\]

identifying \(N\) with its faithful normal represented image when convenient. Its standard right action is

\[
 \rho_\psi(b)=J_\psi\pi_\psi(b^*)J_\psi,\qquad
 \zeta b=\rho_\psi(b)\zeta.
 \tag{BD.1}
\]

The finite left ideal and opposite coordinate are

\[
 \mathfrak n_\psi=\{a:\psi(a^*a)<\infty\},\qquad
 \Lambda'_\psi(x)=J_\psi\Lambda_\psi(x^*),\quad
 x\in\mathfrak n_\psi^*.
 \tag{BD.2}
\]

In particular \(\|\Lambda'_\psi(x)\|^2=\psi(xx^*)\).

Here is the exact endpoint-domain convention. For \(h>0\), put

\[
 S_h^-=\{z:-h\leq\operatorname{Im}z\leq0\}.
\]

An element \(b\in N\) belongs to \(D(\sigma_{-ih}^\psi)\) if there is a bounded, sigma-weakly continuous \(F:S_h^-\to N\), scalar-holomorphic in the interior against every normal functional, satisfying \(F(t)=\sigma_t^\psi(b)\) for real \(t\). Set \(\sigma_{-ih}^\psi(b)=F(-ih)\). Boundary uniqueness proved in section 2 makes the value unique. Norm continuity of the real orbit is not assumed. In particular this condition includes every entire analytic element, but the theorem below uses the entire stated endpoint domain.

Let \(H\) be any Hilbert space with a normal unital right \(N\)-action; its action may have a kernel. Define \(D(H,\psi)\) by

\[
 \xi\in D(H,\psi)
 \quad\Longleftrightarrow\quad
 \exists C<\infty\;\ \|\xi x\|^2\leq C\psi(xx^*)
 \quad(x\in\mathfrak n_\psi^*).
\]

Write \(L_\psi(\xi)\) for the unique bounded extension of

\[
 L_\psi(\xi)\Lambda'_\psi(x)=\xi x.
 \tag{BD.3}
\]

This is the right-module bounded-vector map. In notation that calls this map \(R_\psi\), all conclusions below apply to that map; it is distinct from the left-module map denoted \(R_\psi\) in the current fusion core.

**Theorem.** If \(b\in D(\sigma_{-i/2}^\psi)\) and \(d=\sigma_{-i/2}^\psi(b)\), then

\[
 b\mathfrak n_\psi^*\subseteq\mathfrak n_\psi^*,\qquad
 \Lambda'_\psi(bx)=\pi_\psi(d)\Lambda'_\psi(x)
 \quad(x\in\mathfrak n_\psi^*).
 \tag{BD.4}
\]

Consequently every \(\xi\in D(H,\psi)\) satisfies

\[
 \xi b\in D(H,\psi),\qquad
 L_\psi(\xi b)=L_\psi(\xi)\pi_\psi(d),\qquad
 \|L_\psi(\xi b)\|\leq\|L_\psi(\xi)\|\,\|d\|.
 \tag{BD.5}
\]

For every normal unital left \(N\)-module \(K\) and every \(\eta\in K\), the associated fusion obeys

\[
 (\xi b)\otimes_\psi\eta
   =\xi\otimes_\psi\lambda_K(d)\eta.
 \tag{BD.6}
\]

There is no analyticity or bounded-vector requirement on \(\eta\). There is no restriction on cardinalities, separability or sigma-finiteness, and no assumption that \(\psi(1)\) is finite.

We also obtain the standard GNS right-action identity on its full domain:

\[
 y\,d\in\mathfrak n_\psi,\qquad
 \Lambda_\psi(y)b=\Lambda_\psi(yd)
 \quad(y\in\mathfrak n_\psi).
 \tag{BD.7}
\]

### 2. Strip uniqueness, covariance and reflection

The scalar boundary-uniqueness argument of MA-08 applies to every normal-functional test: a continuous scalar function holomorphic inside a strip and zero on one boundary extends by zero across a small disc centered on that boundary. Splitting triangular integrals across the boundary proves Morera's condition, because the integrals along the two nearby parallel segments cancel in the limit by continuity. The extension is holomorphic and vanishes on an open half-disc. The scalar identity theorem makes it zero on that disc and then on the connected strip. Normal functionals separate \(N\), proving uniqueness for \(F\).

For each real \(s\), the two functions \(F(z+s)\) and \(\sigma_s^\psi(F(z))\) have the same top boundary. Normality of \(\sigma_s^\psi\) preserves all the scalar continuity and holomorphy requirements. Uniqueness gives

\[
 F(z+s)=\sigma_s^\psi(F(z)).
 \tag{BD.8}
\]

In particular the lower boundary is \(\sigma_t^\psi(d)\), where \(d=F(-ih)\). The explicit boundedness in our strip definition does not narrow the usual domain defined by sigma-weak continuity and scalar interior holomorphy. In fact the uniqueness and covariance argument just given did not use boundedness. On the compact segment \(\{-is:0\leq s\leq h\}\), each normal-functional test is bounded by continuity. The uniform boundedness principle, applied to this pointwise bounded family of elements of \(N=(N_*)^*\), gives a common operator-norm bound there. The real covariance (BD.8) transports that bound to the whole strip. Thus the boundedness required in section 1 is automatic for any such strip extension. The bounded-strip maximum principle of MA-08, applied after normal-functional testing, yields

\[
 \|F(z)\|\leq\max\{\|b\|,\|d\|\}.
 \tag{BD.9}
\]

The definition's boundedness is important when applying this principle.

For clarity, holomorphy of any locally bounded sigma-weakly holomorphic \(N\)-valued map in the interior can also be understood in operator norm. Scalar Cauchy coefficients on a small circle define elements of \(N=(N_*)^*\); the common bound gives coefficient norm at most \(CR^{-k}\). Their norm-convergent power series has every prescribed normal-functional coefficient and therefore equals the map. We do not thereby claim norm continuity at either boundary.

Now define, on this same lower strip,

\[
 G(z)=F(\overline z-ih)^*.
 \tag{BD.10}
\]

The argument \(\overline z-ih\) remains in \(S_h^-\). Complex conjugation of the variable together with the conjugate-linear adjoint makes \(G\) holomorphic. More explicitly, if \(\omega^\#(a)=\overline{\omega(a^*)}\), then
\(\omega(G(z))=\overline{\omega^\#(F(\overline z-ih))}\), which is scalar-holomorphic. Continuity and boundedness persist. By (BD.8),

\[
 G(t)=\sigma_t^\psi(d^*),\qquad
 G(t-ih)=\sigma_t^\psi(b^*).
\]

Thus

\[
 d^*\in D(\sigma_{-ih}^\psi),\qquad
 \sigma_{-ih}^\psi(d^*)=b^*.
 \tag{BD.11}
\]

This proves the particular inverse-domain statement needed for (BD.7) by an actual strip extension. It is not a formal use of a complex group law outside its domain.

### 3. Gaussian approximation retains both endpoints

For \(r>0\), set \(g_r(t)=\sqrt{r/\pi}\,e^{-rt^2}\), whose integral is one by MA-03, and define

\[
 b_r(z)=\sqrt{r/\pi}\int_{\mathbb R}
       e^{-r(t-z)^2}\sigma_t^\psi(b)\,dt.
 \tag{BD.12}
\]

The integral is defined on each Hilbert vector in the faithful standard representation; the absolute kernel bound makes a bounded operator of norm at most

\[
 \|b_r(z)\|\leq e^{r(\operatorname{Im}z)^2}\|b\|.
\]

Finite sums of represented elements of \(N\), uniformly bounded for a fixed kernel, converge strongly to this integral, so it lies in \(N\). Equivalently the integral exists against the predual and is represented by this same operator. Its adjoint is obtained with the conjugate kernel. On compact sets of \(z\), the kernel and every complex derivative have a common integrable Gaussian bound. Differentiating in the \(L^1\)-kernel norm proves operator-norm entire dependence. A real change of variable proves
\(\sigma_s^\psi(b_r(0))=b_r(s)\). Hence \(b_r=b_r(0)\) is an entire analytic element with continuation (BD.12).

Suppose \(b\in D(\sigma_{-ih}^\psi)\), with extension \(F\) and endpoint \(d\). Fix a normal functional \(\omega\). Apply the scalar contour theorem to

\[
 w\longmapsto e^{-r(w+ih)^2}\omega(F(w))
\]

on a rectangle whose horizontal sides approach \([-R,R]\) and \([-R-ih,R-ih]\). It suffices first to use sides strictly inside the strip, and then approach its boundary; scalar continuity on each compact rectangle justifies that passage. If \(w=\pm R+iy\), \(-h\leq y\leq0\), then

\[
 |e^{-r(w+ih)^2}|
   =e^{-rR^2+r(y+h)^2}\leq e^{-rR^2+rh^2}.
\]

The two vertical integrals therefore have absolute sum at most
\(2h\,\|\omega\|\,\sup_{S_h^-}\|F\|\,e^{-rR^2+rh^2}\), which tends to zero. The horizontal tails are integrable. Taking \(R\to\infty\), and using \(F(t-ih)=\sigma_t^\psi(d)\), gives

\[
 \sigma_{-ih}^\psi(b_r)=b_r(-ih)
   =\int_{\mathbb R}g_r(t)\sigma_t^\psi(d)\,dt.
 \tag{BD.13}
\]

Equality against all normal functionals is equality in \(N\).

Let \(d_r=\sigma_{-ih}^\psi(b_r)\). Positive Gaussian averaging and (BD.13) imply the separate bounds

\[
 \|b_r\|\leq\|b\|,\qquad \|d_r\|\leq\|d\|,
 \tag{BD.14}
\]

and

\[
 b_r\longrightarrow b,\qquad d_r\longrightarrow d
 \quad\hbox{strongly* as }r\to\infty.
 \tag{BD.15}
\]

Indeed \(\sigma_t^\psi(a)=\Delta_\psi^{it}a\Delta_\psi^{-it}\) is strongly* continuous on each vector. For such a vector, split its Gaussian error integral into \(|t|<\delta\), where continuity makes it small, and the complement, where the error is at most \(2\|a\|\) times the vector norm and the Gaussian mass tends to zero. Apply the same argument to \(a^*\). This proves (BD.15) for both \(a=b\) and \(a=d\). The norm bounds make these limits intrinsic sigma-strong* limits as well, by the faithful normal image/topology theorem WH-02 and NP-06.

No sequence is being used as an approximate identity for the algebra. The real parameter \(r\) smooths a single continuous real orbit. In particular this construction does not impose any countability condition on \(N\) or its representations.

### 4. The exact entire GNS multiplier input

For an entire analytic \(a\in N\), the native right multiplier theorem CX-03 states, for every \(y\in\mathfrak n_\psi\),

\[
 ya\in\mathfrak n_\psi,\qquad
 \Lambda_\psi(ya)
   =J_\psi\pi_\psi(\sigma_{-i/2}^\psi(a^*))J_\psi
      \Lambda_\psi(y).
 \tag{BD.16}
\]

It includes the estimate
\(\|\Lambda_\psi(ya)\|\leq
\|\sigma_{-i/2}^\psi(a^*)\|\,\|\Lambda_\psi(y)\|\).
The GNS domain is the whole finite left ideal, not only the finite-star or Tomita algebra. Here is the domain argument behind that input, so that the limiting steps used below are explicit.

On the finite analytic Hilbert algebra \(\mathcal A_0\) of MF-07–09, the polar identity and the right multiplication formula of MF-11 are

\[
 J_\psi\Lambda_\psi(a)
    =\Lambda_\psi(\sigma_{-i/2}^\psi(a^*)),
 \qquad R_{\Lambda_\psi(a)}
    =J_\psi\pi_\psi(\sigma_{-i/2}^\psi(a^*))J_\psi.
 \tag{BD.17}
\]

All vectors in this display belong to every indicated modular-power domain. The second operator acts on \(\Lambda_\psi(y)\in\mathcal A_0\) as \(\Lambda_\psi(ya)\), proving (BD.16) initially there.

For a fixed such \(a\) and arbitrary \(y\in\mathfrak n_\psi\), HAP-07 followed by MF-08 supplies finite analytic \(y_j\) with

\[
 \Lambda_\psi(y_j)\to\Lambda_\psi(y),\qquad
 y_j\to y\ \hbox{strongly},\qquad
 \sup_j\|y_j\|\leq\|y\|.
\]

One may index the combined approximation by finite collections of Hilbert-vector tests and positive tolerances: first use HAP-07 for the GNS error and those tests, then choose the Gaussian parameter in MF-08 to retain all these finite bounds. Products \(y_ja\) converge sigma-strongly to \(ya\). The bounded right-hand operator in (BD.16) carries \(\Lambda_\psi(y_j)\) to a norm-convergent net. The closed GNS graph theorem NW-12 proves both \(ya\in\mathfrak n_\psi\) and (BD.16).

To remove the finite-vector condition on the multiplier, fix any bounded \(a\) and first smooth it with a fixed Gaussian parameter \(r\). By MF-09 and HAP-05, there are multipliers \(a_j\) of finite analytic vectors with \(\|a_j\|\leq\|a\|\) and \(a_j\to a\) strongly*. Their Gaussian averages \((a_j)_r\) remain multipliers of finite analytic vectors, by MF-08. For fixed \(r,z\),

\[
 (a_j)_r(z)\to a_r(z)\quad\hbox{strongly*},
 \qquad \|(a_j)_r(z)\|\leq e^{r(\operatorname{Im}z)^2}\|a\|.
\]

Here is a valid net argument for this limit. On a compact real interval the vectors
\(\Delta_\psi^{-it}v\) form a norm-compact set. A uniformly bounded strongly convergent net of operators converges uniformly on that compact set: choose a finite norm net, apply strong convergence on its finitely many points, and use the uniform operator bound on the approximation errors. The Gaussian integral over the compact interval consequently converges on \(v\), and its tails have a bound independent of \(j\). The adjoint calculation is identical with its conjugate kernel. This proves the stated strong* convergence without a sequence-only dominated-convergence assumption.

For fixed \(y\in\mathfrak n_\psi\), apply (BD.16) to \((a_j)_r\). Both the product and the right-hand GNS vector have the limits required by NW-12. In the adjoint endpoint, entire analyticity gives
\(\sigma_{-i/2}((a_j)_r^*)=((a_j)_r(i/2))^*\), and the preceding convergence applies at \(z=i/2\). Thus (BD.16) holds for the smoothed multiplier \(a_r\).

Finally suppose \(a\) itself is entire. Gaussian averaging gives \(a_r\to a\) in norm, because its real orbit is norm continuous. Gaussian averaging commutes with the endpoint of the entire orbit of \(a^*\): the same contour argument as section 3, applied to its bounded lower half strip, gives

\[
 \sigma_{-i/2}(a_r^*)
 =\int g_r(t)\sigma_t(\sigma_{-i/2}(a^*))\,dt
 \longrightarrow \sigma_{-i/2}(a^*)
\]

in norm. Boundedness on that whole strip follows from the entire group law and
\(\|\sigma_{t+is}(a^*)\|=\|\sigma_{is}(a^*)\|\), with \(s\) in a compact interval. A last application of NW-12 gives (BD.16) for the full entire multiplier and every \(y\in\mathfrak n_\psi\). This is precisely the native CX-03 argument with its product limits and topology requirements exposed.

### 5. Passing to the half-strip endpoint

Now fix \(b\in D(\sigma_{-i/2}^\psi)\) and use section 3 with \(h=1/2\). Put \(d=\sigma_{-i/2}^\psi(b)\). For any \(y\in\mathfrak n_\psi\), (BD.16) applied to the entire multiplier \(a=b_r^*\) gives

\[
 yb_r^*\in\mathfrak n_\psi,\qquad
 \Lambda_\psi(yb_r^*)=J_\psi\pi_\psi(d_r)J_\psi\Lambda_\psi(y).
 \tag{BD.18}
\]

The products \(yb_r^*\) tend sigma-strongly to \(yb^*\): multiplication on the left by the fixed bounded \(y\) preserves strong convergence, and the products are uniformly norm bounded. The right-hand vectors tend in Hilbert norm to
\(J_\psi\pi_\psi(d)J_\psi\Lambda_\psi(y)\), by the strong convergence of \(d_r\).

NW-12, the closedness of the GNS graph for sigma-strong convergence in \(N\) and weak convergence in \(H_\psi\), now gives

\[
 yb^*\in\mathfrak n_\psi,\qquad
 \Lambda_\psi(yb^*)=J_\psi\pi_\psi(d)J_\psi\Lambda_\psi(y).
 \tag{BD.19}
\]

This first proves ideal membership. Therefore we may put \(y=x^*\) for \(x\in\mathfrak n_\psi^*\) and then apply \(J_\psi\) to the vector identity. Since \(J_\psi^2=1\),

\[
 \Lambda'_\psi(bx)
 =J_\psi\Lambda_\psi(x^*b^*)
 =\pi_\psi(d)J_\psi\Lambda_\psi(x^*)
 =\pi_\psi(d)\Lambda'_\psi(x).
\]

This proves all of (BD.4), with no expression involving \(\Lambda'_\psi(bx)\) used before its domain was established.

To recover the other standard GNS formula, section 2 gives
\(c=d^*\in D(\sigma_{-i/2})\) and \(\sigma_{-i/2}(c)=b^*\).
Apply (BD.19) with \(c\) in place of \(b\):

\[
 yd=yc^*\in\mathfrak n_\psi,\qquad
 \Lambda_\psi(yd)
   =J_\psi\pi_\psi(b^*)J_\psi\Lambda_\psi(y)
   =\Lambda_\psi(y)b.
\]

This proves (BD.7) with both its product domain and right-action convention checked.

### 6. Bounded vectors and the completed tensor product

Let \(\xi\in D(H,\psi)\). For \(x\in\mathfrak n_\psi^*\), (BD.4) gives \(bx\in\mathfrak n_\psi^*\). Module associativity and (BD.3–4) therefore give the legitimate chain

\[
 (\xi b)x=\xi(bx)
  =L_\psi(\xi)\Lambda'_\psi(bx)
  =L_\psi(\xi)\pi_\psi(d)\Lambda'_\psi(x).
 \tag{BD.20}
\]

The last expression has norm at most
\(\|L_\psi(\xi)\|\|d\|\psi(xx^*)^{1/2}\). Hence \(\xi b\) satisfies the exact defining estimate for \(D(H,\psi)\). Both bounded operators in (BD.5) agree on the dense opposite GNS domain, so they are equal.

The all-intertwiner fusion core uses

\[
 X_H=\operatorname{Hom}_{N^{\mathrm{op}}}(H_\psi,H)
\]

and the positive form on \(X_H\odot K\) with coefficient \(S^*T\in\pi_\psi(N)\). In its null quotient one has ordinary intertwiner balancing

\[
 [T\pi_\psi(d)\odot\eta]=[T\odot\lambda_K(d)\eta].
 \tag{BD.21}
\]

Indeed the difference has pairing zero against every \(S\odot\zeta\), because
\(S^*T\pi_\psi(d)\) represents the product of the represented element \(S^*T\) with \(d\). It therefore belongs to the radical of the positive form, which is the nullspace used in the quotient. The weight-labelled vector \(\xi\otimes_\psi\eta\) is the image of \([L_\psi(\xi)\odot\eta]\), by the coefficient-saturation theorem FU-03. Substituting (BD.5) in (BD.21) proves (BD.6), first in the null quotient and hence in its Hilbert completion.

This also identifies why ordinary vector balancing is generally wrong: multiplying a weight-labelled vector on the right changes its intertwiner by \(\pi_\psi(\sigma_{-i/2}^\psi(b))\), rather than by \(\pi_\psi(b)\). The correction is determined by the GNS coordinate.

### 7. A finite sign check with no remaining domains

Take \(N=M_2(\mathbb C)\), \(D=\operatorname{diag}(1,4)\), and \(\psi(a)=\operatorname{Tr}(Da)\) on \(N_+\). In the Hilbert–Schmidt standard realization,

\[
 \Lambda_\psi(a)=aD^{1/2},\quad JX=X^*,\quad
 \Lambda'_\psi(x)=D^{1/2}x,\quad Xb=Xb,
 \quad \sigma_z^\psi(b)=D^{iz}bD^{-iz}.
\]

All finite ideals and analytic domains are the entire finite-dimensional algebra. Let \(\xi=D^{1/2}\), \(b=E_{12}\), and \(\eta=e_2\in\mathbb C^2\). Then

\[
 d=\sigma_{-i/2}^\psi(b)=\tfrac12E_{12},\qquad
 \sigma_{+i/2}^\psi(b)=2E_{12},\qquad
 \xi b=E_{12}=\Lambda_\psi(\tfrac12E_{12}).
\]

The defining fusion form directly makes
\(V(\Lambda_\psi(a)\otimes_\psi\eta)=a\eta\) a unitary onto \(\mathbb C^2\): its finite-sum pairing is the ordinary pairing of the corresponding sums \(a\eta\), and \(a=1\) gives onto. Thus the left side of (BD.6) maps to \(\frac12e_1\), its negative-half right side also maps to \(\frac12e_1\), and the positive-half replacement maps to \(2e_1\). This checks the general proof's sign independently of any infinite-domain limit.

Takesaki II, printed p. 187 / PDF p. 207, gives the standard GNS right action with the negative-half parameter; its IX.3, Corollary 3.18(iii), printed p. 203 / PDF p. 223, prints a positive-half vector-balancing parameter. Under the right action (BD.1), the latter fails by this finite calculation. The proof above establishes the corrected relation on its full stated
endpoint domain \(D(\sigma^\psi_{-i/2})\). The printed clause instead assumes
\(b\in D(\sigma^\psi_{+i/2})\). These are different analytic endpoint domains
in general; the correction changes both the multiplier and its domain, and
makes no assertion that either domain contains the other.

### 8. Prerequisites and scope

The proofs use these actual native statements:

- **The modular fundamental theorem through The analytic algebra is a common core and The opposite structure of a Tomita algebra:** faithful standard modular implementation; finite analytic Hilbert algebra; all modular powers and their indicated core; Gaussian operator/vector estimates; the polar and opposite multiplication identities.
- **Contractive approximation from a nonunital algebra and Approximation of every left-bounded vector; Fullness and recovery of the original weight:** bounded strong* approximation from the nondegenerate finite analytic multiplier algebra, and GNS-vector/left-multiplier approximation for the entire finite ideal.
- **Consequences for GNS maps and sums of weights:** sigma-strong/weak closedness of the full GNS graph for nets, with the membership conclusion.
- **Gaussian normalization and its Fourier transform and Two facts about closed strips:** Gaussian normalization, scalar boundary uniqueness and the bounded-strip maximum principle. The actual Gaussian contour shift is proved in section 3.
- **The image of a faithful normal representation and Normal representations and sigma-strong continuity:** the faithful normal represented-image identification and its bounded sigma-strong* topology transport.
- **Two identities on the full finite left ideal:** the entire right multiplier lemma, whose precise proof and domain passages are reconstructed in section 4.
- **A positive form and its exact quotient through Exact weight-bounded coordinates and coefficient saturation:** the positive null quotient, ordinary intertwiner balancing and exact bounded-vector coordinates. Section 6 uses only these already written proof blocks, not the future units, associator or weight-change theorem.

The endpoint argument uses a faithful normal semifinite reference weight but adds no faithful-state, sigma-finite or separable hypothesis.

## Comparing the reference weights

## Canonical reference-weight comparison

This proof uses the intertwiner construction and coefficient saturation in FU-01–04, the canonical standard-form comparisons in SF-09 and SE-10, and bounded functoriality from FU-05.

### The comparison on a dense set

Let \(N\) be any von Neumann algebra, \(H\) a normal unital right \(N\)-module and \(K\) a normal unital left \(N\)-module. Either action may have a kernel. Choose two faithful normal semifinite weights \(\psi_1,\psi_2\). For \(i=1,2\), let

\[
 L_i=H_{\psi_i},\qquad
 \lambda_i=\pi_{\psi_i},\qquad
 \rho_i(b)=J_i\pi_{\psi_i}(b^*)J_i,\qquad
 X_i=\operatorname{Hom}_{N^{\mathrm{op}}}(L_i,H).
\]

Denote the completed intertwiner model by \(F_i(H,K)\). Its elementary class is \([T,\eta]_i\), for \(T\in X_i,\eta\in K\), with

\[
 \langle[T,\eta]_i,[S,\zeta]_i\rangle
 =\langle\lambda_K(\lambda_i^{-1}(S^*T))\eta,\zeta\rangle.
 \tag{FW.1}
\]

It is the completed null quotient of finite sums, not a completion of raw tensors with a definite form. FU-03 identifies the weight-labelled model \(H\otimes_{\psi_i}K\) unitarily onto \(F_i(H,K)\) by
\(\xi\otimes_{\psi_i}\eta\mapsto[L_{\psi_i}(\xi),\eta]_i\).
We use this identification throughout.

Let \(I_{2\leftarrow1}:L_1\to L_2\) be the unique standard-form comparison implementing the identity of \(N\). It intertwines both actions, maps the cones onto one another and intertwines the conjugations. Write \(I_{1\leftarrow2}=I_{2\leftarrow1}^*\). Prescribe

\[
 W_{2\leftarrow1}[T,\eta]_1
       =[T I_{1\leftarrow2},\eta]_2.
 \tag{FW.2}
\]

The composed operator is a bounded right intertwiner with exactly the required domain \(L_2\). If \(x=\lambda_1^{-1}(S^*T)\), then

\[
 (S I_{1\leftarrow2})^*(T I_{1\leftarrow2})
 =I_{2\leftarrow1}\lambda_1(x)I_{1\leftarrow2}
 =\lambda_2(x).
 \tag{FW.3}
\]

Thus the two elementary pairings agree. Summing this equality over both finite families proves preservation of the complete semidefinite form. In particular the proposed map preserves the nullspace, is independent of representatives and gives an isometry on the quotient. It extends uniquely to an isometry between the Hilbert completions.

The same construction with the indices reversed gives its inverse: composition sends \([T,\eta]_1\) to itself, and the reverse composition fixes every generator of \(F_2(H,K)\). Density proves that both compositions are identities on the completions. Hence \(W_{2\leftarrow1}\) is onto.

For endomorphisms \(a\) of the right module \(H\) and \(b\) of the left module \(K\), the two ways of applying the comparison and the induced outer action both send a generator to
\([aT I_{1\leftarrow2},b\eta]_2\).
Boundedness and density prove that \(W_{2\leftarrow1}\) intertwines both entire outer actions. This assertion includes the case of zero fusion. It makes no injectivity assertion about a joint outer tensor action.

More generally, for bounded right and left module maps \(A:H\to H'\), \(B:K\to K'\), respectively, the same calculation gives

\[
 W^{H',K'}_{2\leftarrow1}(A\otimes_{\psi_1}B)
 =(A\otimes_{\psi_2}B)W^{H,K}_{2\leftarrow1}.
 \tag{FW.4}
\]

Thus the comparison is natural in both modules, with the operator domains and codomains indicated. No particular vectors in the two GNS spaces have been equated.

### Actual weight-bounded symbols after comparison

Formula (FW.2) acts first on intertwiners. It need not carry a weight-bounded vector to the same vector with a different subscript.

There is a useful formula using only eligible symbols in the target space. Fix \(\xi\in D(H,\psi_1)\) and \(\eta\in K\), and put

\[
 T=L_{\psi_1}(\xi)I_{1\leftarrow2}:L_2\to H.
\]

Take the positive finite-energy contractions \(e_\alpha\) supplied by WG-008 for \(\psi_2\), converging strongly* to \(1\). Set

\[
 \xi_\alpha=T\Lambda_{\psi_2}(e_\alpha).
\]

FU-03 gives

\[
 \xi_\alpha\in D(H,\psi_2),\qquad
 L_{\psi_2}(\xi_\alpha)=T\lambda_2(e_\alpha),\qquad
 \|L_{\psi_2}(\xi_\alpha)\|\leq\|T\|.
\]

These operators converge strongly* to \(T\). The coefficient convergence rule in FU-02 therefore gives the norm limit

\[
 W_{2\leftarrow1}(\xi\otimes_{\psi_1}\eta)
   =\lim_\alpha \xi_\alpha\otimes_{\psi_2}\eta.
 \tag{FW.5}
\]

It is the fusion norm that converges here; no assertion about convergence of the vectors \(\xi_\alpha\) in \(H\) is required. A common cutoff works for each finite family, so the formula also computes all finite sums. It neither assumes equality nor density of the intersection of the two weight-bounded domains.

### Characterization by maps into a standard module

We now show that the comparison is determined by a concrete family of bounded tests. This supplies both existence and uniqueness for the usual standard-unit diagram.

For a right intertwiner \(a:H\to L_i\) and a left intertwiner \(b:L_i\to K\), define initially

\[
 Q_i(a,b)[T,\eta]_i=aT b^*\eta\in L_i.
 \tag{FW.6}
\]

The expression is well typed: \(aT\in\lambda_i(N)\), whereas \(b^*\eta\in L_i\).
It is a bounded map on the completed fusion space. One way to see the bound directly is to factor it into the bounded module map \(a\otimes_{\psi_i}b^*\) and the standard multiplication unit

\[
 m_i:F_i(L_i,L_i)\to L_i,\qquad
 m_i[\lambda_i(x),\zeta]_i=\lambda_i(x)\zeta.
\]

Every right endomorphism of \(L_i\) is \(\lambda_i(x)\). Formula (FW.1) proves that \(m_i\) preserves all finite-sum pairings, and \(m_i[1,\zeta]_i=\zeta\) proves that it is onto. Consequently

\[
 Q_i(a,b)=m_i(a\otimes_{\psi_i}b^*),
 \qquad \|Q_i(a,b)\|\leq\|a\|\|b\|.
 \tag{FW.7}
\]

This proves the claimed unit in the one standard-module case used here; the full two-sided unit and naturality statements have their separate FU-06 proof.

Set

\[
 a_2=I_{2\leftarrow1}a_1,\qquad
 b_2=b_1I_{1\leftarrow2}.
 \tag{FW.8}
\]

**The second test needs the inverse comparison.** Here \(a_1:H\to L_1\), \(b_1:L_1\to K\), and \(I_{2\leftarrow1}:L_1\to L_2\). Thus \(a_2=I_{2\leftarrow1}a_1\) has domain \(H\), while \(b_2=b_1I_{1\leftarrow2}\) has domain \(L_2\). Takesaki II, printed 205 / PDF 225, prints \(b_2=b_1I_{2\leftarrow1}\). That composition cannot have the indicated domain and codomain. Formula (FW.8) corrects its direction.

The direction matters even if the underlying scalar vector spaces are informally identified. Take \(N=H=K=\mathbb C\), with the usual module norms and reference weights \(\psi_1(z)=z\), \(\psi_2(z)=9z\). The norms in \(L_1,L_2\) are \(|z|\) and \(3|z|\). Their cone-preserving comparisons multiply by \(1/3\) and \(3\), respectively. With \(a_1=b_1=1\), the correct transported tests are \(a_2=1/3\), \(b_2=3\), and the weighted adjoint \(b_2^*:K\to L_2\) is multiplication by \(1/3\). Precomposition in (FW.2) makes the target intertwiner \(3T\). Consequently (FW.6) evaluates the correct tested comparison at \(T\eta/3\), exactly \(I_{2\leftarrow1}Q_1(a_1,b_1)[T,\eta]_1\).

Forcing the printed direction onto those same scalar coordinates would instead give a second test \(b_2^{\mathrm{wrong}}=1/3\). Its adjoint is multiplication by \(1/27\), since the domain inner product has weight \(9\). The tested image would then be \(T\eta/27\), which differs from \(T\eta/3\) for \(T=\eta=1\). This is a finite check of the diagram, including the Hilbert-space adjoint; it does not use or identify the finite ideals of distinct weights.

They have the required right and left intertwining properties. On each generator,

\[
 \begin{aligned}
 Q_2(a_2,b_2)W_{2\leftarrow1}[T,\eta]_1
 &=I_{2\leftarrow1}a_1T I_{1\leftarrow2}
                  I_{2\leftarrow1}b_1^*\eta\\
 &=I_{2\leftarrow1}Q_1(a_1,b_1)[T,\eta]_1 .
 \end{aligned}
\]

Thus, as an identity of bounded maps on the whole completion,

\[
 Q_2(a_2,b_2)W_{2\leftarrow1}
       =I_{2\leftarrow1}Q_1(a_1,b_1).
 \tag{FW.9}
\]

This is the commuting diagram after its vertical composites have been explicitly defined.

The family \(Q_i(a,b)\) separates points. Indeed its adjoint is

\[
 Q_i(a,b)^*\zeta=[a^*,b\zeta]_i.
 \tag{FW.10}
\]

To check this with first-variable-linear inner products, write \(aT=\lambda_i(x)\). Then

\[
 \begin{aligned}
 \langle[T,\eta]_i,[a^*,b\zeta]_i\rangle
 &=\langle\lambda_K(x)\eta,b\zeta\rangle\\
 &=\langle b^*\lambda_K(x)\eta,\zeta\rangle\\
 &=\langle\lambda_i(x)b^*\eta,\zeta\rangle
 =\langle Q_i(a,b)[T,\eta]_i,\zeta\rangle .
 \end{aligned}
\]

As \(a\) varies, \(a^*\) ranges over all of \(X_i\). By the left version of FU-01's intertwiner totality, vectors \(b\zeta\), with \(b:L_i\to K\) a left intertwiner, have dense linear span in \(K\). For fixed \(T\), the bound
\(\|[T,\eta]_i\|\leq\|T\|\|\eta\|\)
therefore shows that the ranges of the adjoints in (FW.10) have dense linear span in \(F_i(H,K)\). A vector annihilated by every \(Q_i(a,b)\) is orthogonal to this span and is zero.

Suppose a bounded map \(V:F_1(H,K)\to F_2(H,K)\) satisfies (FW.9) with \(V\) in place of \(W_{2\leftarrow1}\), for every pair of intertwiners in (FW.8). Each pair \((a_2,b_2)\) arises from exactly one pair \((a_1,b_1)\), by applying the inverse unitary. The difference \((V-W_{2\leftarrow1})v\) is annihilated by all \(Q_2\) and hence is zero for every \(v\). Thus the diagram determines \(W_{2\leftarrow1}\) uniquely even among bounded maps. An a priori unitary assumption is unnecessary for uniqueness.

### Coherence and canonical choices

For three faithful normal semifinite weights, standard-form uniqueness gives

\[
 I_{1\leftarrow2}I_{2\leftarrow3}=I_{1\leftarrow3}.
\]

Applying (FW.2) twice, including its operator order, gives

\[
 W_{3\leftarrow2}W_{2\leftarrow1}=W_{3\leftarrow1},\qquad
 W_{1\leftarrow1}=1,\qquad
 W_{2\leftarrow1}^*=W_{1\leftarrow2}.
 \tag{FW.11}
\]

These identities hold on every generator and therefore on the completion. The same argument applies when comparing any two standard forms through SE-10. A third standard form gives the same comparison because its canonical unitaries compose in the same order.

**Reference-weight comparison.** For faithful normal semifinite \(\psi_1,\psi_2\), the unique standard-form unitary \(I_{2\leftarrow1}:L_1\to L_2\) determines \(W_{2\leftarrow1}[T,\eta]_1=[T I_{1\leftarrow2},\eta]_2\). For test pairs transported by (FW.8), the bounded tests satisfy \(Q_2(a_2,b_2)W_{2\leftarrow1}=I_{2\leftarrow1}Q_1(a_1,b_1)\). This comparison uses intertwiner coordinates and does not identify GNS vectors of different weights. See (FW.2–3), (FW.6–9), and Takesaki II, IX.3, Theorem 3.21 (printed pp. 205–206).

This identifies what “independent of the reference weight” means: there is a specified coherent unitary family, natural in both modules. An arbitrary left-representation unitary would not suffice. Its possible commutant ambiguity would enter (FW.2); preserving the standard cone removes that ambiguity.

The direct-sum isomorphisms commute with \(W\). On finite sums of summand inclusions this follows from (FW.4); those vectors are dense by FU-06, so it holds for arbitrary index sets.

Associativity is compatible with a change of either middle reference. Here is the dense-core calculation, including the change of the creation operator. Let \(H_M,{}_M K_N,{}_N Z\), with reference spaces \(L_\varphi\) and \(L_\psi\), and take

\[
 T:L_\varphi\to H,\quad S:L_\psi\to K,\quad z\in Z.
\]

Both \(T,S\) are bounded right intertwiners for their indicated middle algebras. In FU-07's notation \(C_T\eta=[T,\eta]_\varphi\). Changing \(\varphi_1\) to \(\varphi_2\) gives

\[
 W^{H,K}_{\varphi_2\leftarrow\varphi_1}C_T
       =C_{T I_{\varphi_1\leftarrow\varphi_2}}.
\]

The associator sends
\([C_T S,z]_\psi\) to \([T,[S,z]_\psi]_\varphi\).
Along either route around the square comparing \(\varphi\), the result is

\[
 [T I_{\varphi_1\leftarrow\varphi_2},[S,z]_\psi]_{\varphi_2}.
\]

Changing \(\psi_1\) to \(\psi_2\) replaces \(S\) by
\(S I_{\psi_1\leftarrow\psi_2}\) in both routes, producing
\([T,[S I_{\psi_1\leftarrow\psi_2},z]_{\psi_2}]_\varphi\).
FU-07's creation-saturation theorem proves that these finite-sum cores are dense; all maps in the squares are bounded unitaries or their induced functorial maps. The equalities therefore extend to the two complete bracketings. Applying the two squares consecutively handles simultaneous changes. This proof uses controlled intertwiners, not an assumed dense common domain of weight-bounded vectors.

### Scope of the reference-weight assumption

Both reference weights in this theorem are faithful, normal and semifinite. This condition concerns the reference standard forms, independently of the possible kernels in the module actions.

Takesaki II defines \(\mathcal W(N)\) as the semifinite normal weights and
\(\mathcal W_0(N)\) as their faithful members (printed p. 154). The first pair
of classes printed in IX.3, Theorem 3.21 (printed pp. 205–206) is
\(\mathcal W_0(N)\times\mathcal W(N)\): it is the **second** weight that has
the broader quantifier. The later chain law is printed for
\(\mathcal W_0(N)\times\mathcal W_0(N)\). The result proved here gives the
coherent two-faithful-normal-semifinite-weight statement and the exact
testing diagram. The broad second-weight clause cannot hold for the raw GNS
bounded-vector completion used here, as the zero-weight example below
shows. It requires a different support construction or a correction of the
printed clause; neither is inferred from its quantifier.

The need to specify an extension is visible in a scalar example. On \(N=\mathbb C\), the zero weight is normal and semifinite, but its GNS Hilbert space is zero. For the nonzero standard scalar right module \(H=\mathbb C\), the defining estimate

\[
 |\xi x|^2\leq C\,0
 \qquad(x\in\mathbb C)
\]

forces \(D(H,0)=\{0\}\). Thus the raw bounded-vector tensor space with any \(K\) is zero, and any null quotient and completion of that space is zero. In contrast, with a strictly positive scalar reference weight and \(K=\mathbb C\), fusion is one dimensional, as computed in the next component. These two completions cannot be related by an onto unitary. More generally, a nonfaithful GNS representation has no inverse identification of its image with all of \(N\), so (FW.1) itself needs additional support data or a changed definition. This is a boundary of the formula, not a restriction of the module generality already proved.

## Reversing fusion by conjugation

## Conjugate-fusion reversal

The construction uses the completed intertwiner fusion, null quotient, two unit maps, and associator from FU-01–08. Hilbert spaces may be arbitrary; normal unital module actions may have kernels. No separability, countability, sigma-finiteness, or faithful outer action is assumed. The middle reference weight used for coordinates is faithful, normal and semifinite.

Let \(H_N\) be a normal right \(N\)-module and \({}_N K\) a normal left \(N\)-module. Write \(C_H:H\to\overline H\) and \(C_K:K\to\overline K\) for the canonical antiunitaries. The conjugate modules have the actions

\[
 a\,C_H\xi=C_H(\xi a^*)\quad(a\in N\text{ when }H\text{ is right }N),
 \qquad
 (C_K\eta)b=C_K(b^*\eta)\quad(b\in N\text{ when }K\text{ is left }N).
 \tag{CF.1}
\]

Thus \(\overline K\) is a right \(N\)-module and \(\overline H\) is a left \(N\)-module. If \(H\) also has a left \(P\)-action and \(K\) a right \(Q\)-action, then \(\overline H\) has a right \(P\)-action and \(\overline K\) a left \(Q\)-action, with the same rule (CF.1). The conjugate of a bounded intertwiner \(A\) is

\[
 \overline A=C_{H'}A C_H^{-1};
 \tag{CF.2}
\]

it is linear, bounded, and \(\overline{A^*}=\overline A^{\,*}\).

### Canonical all-intertwiner map

Fix a standard \(N\)-bimodule \(L\), with left representation \(\lambda\), right antirepresentation \(\rho\), and modular conjugation \(J_L\). For a right intertwiner \(T:L\to H\), define

\[
 \check T=C_H T J_L:L\longrightarrow\overline H.
 \tag{CF.3}
\]

This is a left \(N\)-intertwiner. Indeed \(J_L\lambda(a)=\rho(a^*)J_L\), \(T\rho(a^*)=\rho_H(a^*)T\), and (CF.1) turns \(C_H\rho_H(a^*)\) into left multiplication by \(a\) on \(\overline H\). The map \(T\mapsto\check T\) is **conjugate-linear** in \(T\): the two antiunitaries flank the linear operator, so \(\check{cT}=\overline c\,\check T\). It is a bijection from right to left intertwiners, and its adjoint coefficients satisfy (CF.6) below. This conjugate linearity makes (CF.4) linear on the conjugate source space: multiplying \(T\) or \(\eta\) by \(c\) multiplies both sides by \(\overline c\).

FU04 provides two equivalent completed models. In the right model, \(H\boxtimes_N K\) is the completion of \(X_H\odot K\). In the left model, \(\overline K\boxtimes_N\overline H\) is the completion of \(\overline K\odot Y_{\overline H}\), where \(Y_{\overline H}=\operatorname{Hom}_N(L,\overline H)\). Define on elementary classes in the conjugate of the first model

\[
 \mathfrak c_{H,K}:
 \overline{H\boxtimes_N K}\longrightarrow
 \overline K\boxtimes_N\overline H,\qquad
 \mathfrak c_{H,K}\bigl(C_{H\boxtimes K}[T\odot\eta]\bigr)
   = [C_K\eta\odot\check T].
 \tag{CF.4}
\]

Here the target bracket is the left-intertwiner quotient. The formula uses the standard coordinate \(L\) only to identify the two all-intertwiner models; changing the specified standard bimodule transports both sides by the canonical standard-form comparison.

To verify that (CF.4) descends through the full null quotient, let \(T_i,S_j\in X_H\), \(\eta_i,\zeta_j\in K\), and put

\[
 a_{ji}=\lambda^{-1}(S_j^*T_i)\in N.
\]

The source right-model form is

\[
 B_{ji}=\left\langle\lambda_K(a_{ji})\eta_i,\zeta_j\right\rangle.
 \tag{CF.5}
\]

The target left-model coefficient is

\[
 \check S_j^*\check T_i
 =J_LS_j^*T_iJ_L
 =J_L\lambda(a_{ji})J_L
 =\rho(a_{ji}^*).
 \tag{CF.6}
\]

Consequently the right action of \(\rho^{-1}(\check S_j^*\check T_i)=a_{ji}^*\) on \(C_K\eta_i\) is \(C_K\lambda_K(a_{ji})\eta_i\). Since \(\langle C_Ku,C_Kv\rangle_{\overline K}=\langle v,u\rangle_K\), the target form, with first argument indexed by \(i\) and second by \(j\), is

\[
 \left\langle C_K\lambda_K(a_{ji})\eta_i,C_K\zeta_j\right\rangle_{\overline K}
 =\left\langle\zeta_j,\lambda_K(a_{ji})\eta_i\right\rangle_K
 =B_{ji}^{\,\mathrm{conj}},
 \tag{CF.7}
\]

where \(B_{ji}^{\,\mathrm{conj}}\) is exactly the inner product of the conjugate source vectors in the same order:

\[
 \big\langle C_{H\boxtimes K}[T_i\odot\eta_i],
 C_{H\boxtimes K}[S_j\odot\zeta_j]\big\rangle
 =
 \big\langle[S_j\odot\zeta_j],[T_i\odot\eta_i]\big\rangle
 =
 \left\langle\zeta_j,\lambda_K(a_{ji})\eta_i\right\rangle .
\]

Thus every source null relation maps to a target null relation and (CF.4) is isometric on the quotient.

The image contains every target left-model generator: an arbitrary first vector of \(\overline K\) is \(C_K\eta\), and every left intertwiner \(V:L\to\overline H\) has the unique inverse \(T=C_H^{-1}VJ_L\) in \(X_H\). The composition is well typed and is a bounded linear operator because its two outer factors are antiunitary. FU-04's left model says these generators have dense span in \(\overline K\boxtimes_N\overline H\). Therefore (CF.4) extends to a canonical linear unitary

\[
 \mathfrak c_{H,K}:\overline{H\boxtimes_N K}
 \xrightarrow{\;\cong\;}
 \overline K\boxtimes_N\overline H .
 \tag{CF.8}
\]

The all-intertwiner definition proves independence of any reference weight and remains valid when either action has a kernel or the resulting fusion is zero. In the zero case, both sides are the zero Hilbert space and (CF.8) is its unique unitary.

### Exact weight-coordinate formula and its domains

Choose an n.s.f. weight \(\psi\) on \(N\), and use \(L=H_\psi\). FU03 and FU04 give the exact right-bounded map

\[
 L_\psi(\xi)\Lambda'_\psi(x)=\xi x,
 \quad \xi\in D(H,\psi),\quad x\in\mathfrak n_\psi^*,
\]

and the exact left-bounded map

\[
 R_\psi(\eta)\Lambda_\psi(a)=a\eta,
 \quad\eta\in D'(K,\psi),\quad a\in\mathfrak n_\psi.
\]

(FU.24) gives, for a left-bounded vector \(\eta\),

\[
 L_\psi(C_K\eta)=C_K R_\psi(\eta)J_\psi.
 \tag{CF.9}
\]

For \(\xi\in D(H,\psi)\), the all-intertwiner transform (CF.3) is exactly

\[
 \check{L_\psi(\xi)}
 =C_H L_\psi(\xi)J_\psi
 =R_\psi(C_H\xi),
 \tag{CF.10}
\]

the left-bounded coordinate of \(C_H\xi\). Substituting \(T=L_\psi(\xi)\) in (CF.4), then using FU04's left model, yields the controlled coordinate formula

\[
 \boxed{\ 
 \mathfrak c_{H,K}\!\left(C_{H\boxtimes K}
       (\xi\otimes_\psi\eta)\right)
   =C_K\eta\otimes_\psi C_H\xi\ },
 \qquad
 \xi\in D(H,\psi),\quad \eta\in K.
 \tag{CF.11}
\]

If \(\eta\in D'(K,\psi)\), the same vector is represented in the original left model; the formula remains valid for every \(\xi\in H\):

\[
 \mathfrak c_{H,K}\!\left(C_{H\boxtimes K}
       (\xi\otimes_\psi\eta)\right)
   =C_K\eta\otimes_\psi C_H\xi,
 \qquad
 \xi\in H,\quad\eta\in D'(K,\psi).
 \tag{CF.12}
\]

The common eligible core \(D(H,\psi)\times D'(K,\psi)\) is dense in the fusion. FU-03 coefficient saturation first gives the right-bounded completion with arbitrary second vectors. For fixed \(\xi\in D(H,\psi)\), choose \(\eta_\gamma\in D'(K,\psi)\) with \(\eta_\gamma\to\eta\) in Hilbert norm. The elementary bound (FU.13) gives

\[
 \|\xi\otimes_\psi(\eta_\gamma-\eta)\|
 \leq \|L_\psi(\xi)\|\,\|\eta_\gamma-\eta\|\longrightarrow0.
\]

Apply this to each term of a finite sum. On this core the two meanings agree by FU-04. No uniform bound on the left-bounded operators \(R_\psi(\eta_\gamma)\) is needed, and no simultaneous modular-domain or analytic assumption is added.

For completeness, the one-sided extensions in (CF.11–12) are not formal symbols. If \(\eta\in D'(K,\psi)\), then \(C_K\eta\in D(\overline K,\psi)\) by (CF.9), so the target right model defines \(C_K\eta\otimes_\psi C_H\xi\) for every \(\xi\in H\). If \(\xi\in D(H,\psi)\), then (CF.10) puts \(C_H\xi\) in the target left-bounded domain, so its left model defines the same symbol for every \(\eta\in K\). Continuity of the two bounded-vector maps and the all-intertwiner identity (CF.4) prove the extensions.

### Flipped outer actions

Suppose \(H\) is a \(P\)-\(N\) bimodule and \(K\) an \(N\)-\(Q\) bimodule. Then \(H\boxtimes_NK\) is a \(P\)-\(Q\) bimodule, while \(\overline K\boxtimes_N\overline H\) is a \(Q\)-\(P\) bimodule. The unitary (CF.8) flips these actions:

\[
 \mathfrak c_{H,K}\bigl(q\cdot C u\cdot p\bigr)
 =q\cdot\mathfrak c_{H,K}(Cu)\cdot p,
 \quad p\in P,\ q\in Q,\ u\in H\boxtimes_NK,
 \tag{CF.13}
\]

where the conjugate action is \(q\cdot Cu=C(uq^*)\) and \(Cu\cdot p=C(p^*u)\). On a controlled generator this is just

\[
 C_K(\eta q^*)\otimes C_H(p^*\xi)
 =q\cdot(C_K\eta)\otimes(C_H\xi)\cdot p.
\]

For bounded outer intertwiners \(A:H\to H'\) that are right \(N\)-linear and \(B:K\to K'\) that are left \(N\)-linear, naturality is

\[
 \mathfrak c_{H',K'}\,\overline{(A\boxtimes_NB)}
 =
 (\overline B\boxtimes_N\overline A)\,\mathfrak c_{H,K}.
 \tag{CF.14}
\]

It is checked on (CF.4):
both sides send \(C[T\odot\eta]\) to
\([C_{K'}B\eta\odot C_{H'}ATJ_L]\).
The equality extends by density. Taking \(A\) or \(B\) to be an outside action proves (CF.13), and taking adjoints in (CF.14) uses \(\overline{A^*}=\overline A^{\,*}\).

### Double conjugation

Let \(\delta_H:H\to\overline{\overline H}\) be

\[
 \delta_H\xi=C_{\overline H}C_H\xi,
 \tag{CF.15}
\]

and similarly for \(K\) and every fusion space. These are canonical linear module unitaries. Reversing twice gives

\[
 \bigl(\mathfrak c_{\overline K,\overline H}\bigr)\,
 \overline{\mathfrak c_{H,K}}\,
 \delta_{H\boxtimes_NK}
 =
 \delta_H\boxtimes_N\delta_K.
 \tag{CF.16}
\]

The types in (CF.16) are, from left to right,

\[
 H\boxtimes_NK
 \xrightarrow{\delta_{H\boxtimes K}}
 \overline{\overline{H\boxtimes_NK}}
 \xrightarrow{\overline{\mathfrak c_{H,K}}}
 \overline{\overline K\boxtimes_N\overline H}
 \xrightarrow{\mathfrak c_{\overline K,\overline H}}
 \overline{\overline H}\boxtimes_N\overline{\overline K}.
\]

On the dense all-intertwiner/weight core, the left side sends

\[
 \xi\otimes\eta
 \longmapsto
 \delta_H\xi\otimes\delta_K\eta,
\]

because the first reversal sends \(C(\xi\otimes\eta)\) to \(C\eta\otimes C\xi\), and the second sends this to \(C(C\xi)\otimes C(C\eta)\). Continuity proves (CF.16), including zero fusions.

### Compatibility with the associator

Let \(H_M\), \({}_M K_N\), and \({}_N Z\) be normal modules. Write \(a_{H,K,Z}\) for FU08's canonical associator

\[
 a_{H,K,Z}:(H\boxtimes_MK)\boxtimes_NZ
 \longrightarrow H\boxtimes_M(K\boxtimes_NZ).
\]

The conjugate reversal and associator satisfy the typed identity

\[
\begin{aligned}
 a_{\overline Z,\overline K,\overline H}^{-1}
 (1_{\overline Z}\boxtimes_N\mathfrak c_{H,K})
 \mathfrak c_{H\boxtimes_MK,Z}
 &=
 (\mathfrak c_{K,Z}\boxtimes_M1_{\overline H})
 \mathfrak c_{H,K\boxtimes_NZ}\,
 \overline{a_{H,K,Z}} .
\end{aligned}
\tag{CF.17}
\]

The left side starts in
\(\overline{(H\boxtimes_MK)\boxtimes_NZ}\), reverses \(Z\), then reverses \(H,K\), and finally changes from the right-associated to the left-associated order. The right side first conjugates FU08's associator, then reverses \(K,Z\), and has the same target.

To prove (CF.17) on a dense eligible core, take

\[
 \xi\in D(H,\varphi),\qquad
 \eta\in K,\qquad
 \zeta\in D'(Z,\psi),
\]

for faithful n.s.f. weights \(\varphi\) on \(M\) and \(\psi\) on \(N\). FU08's mixed bounded-generator formula applies to
\((\xi\otimes_\varphi\eta)\otimes_\psi\zeta\), without asserting that \(\xi\otimes\eta\) itself is right-\(\psi\)-bounded. After the two reversals, but before the final inverse associator, the left route has the intermediate value

\[
 C_Z\zeta\otimes_\psi(C_K\eta\otimes_\varphi C_H\xi).
\]

The first reversal uses the second-variable left-bounded extension (CF.12), and the second uses the first-variable right-bounded extension (CF.11). The final \(a_{\overline Z,\overline K,\overline H}^{-1}\) sends this value to

\[
 (C_Z\zeta\otimes_\psi C_K\eta)\otimes_\varphi C_H\xi.
\]

The conjugate associator first sends the same generator to

\[
 C_{H\boxtimes_M(K\boxtimes_NZ)}
   \bigl(\xi\otimes_\varphi(\eta\otimes_\psi\zeta)\bigr).
\]

The next map, \(\mathfrak c_{H,K\boxtimes_NZ}\), uses
\(\xi\in D(H,\varphi)\) and (CF.11) to give

\[
 C_{K\boxtimes_NZ}(\eta\otimes_\psi\zeta)
       \otimes_\varphi C_H\xi.
\]

Finally \(\mathfrak c_{K,Z}\boxtimes_M1_{\overline H}\) uses
\(\zeta\in D'(Z,\psi)\) and (CF.12), giving

\[
 (C_Z\zeta\otimes_\psi C_K\eta)\otimes_\varphi C_H\xi.
\]

Thus both complete routes have the same left-associated value. The eligible generators are dense by FU-03's coefficient saturation in each stage and FU-08's creation-operator saturation; every map is bounded, so (CF.17) extends to the completed spaces. This proof uses no intersection of unproved unbounded domains.

The finite-factor callback in TT3 XIX.2(4) is obtained by specializing this theorem to its finite-index bimodule and conjugate, with the outer type order explicit: an \(M_1\)-\(M_2\) module followed by an \(M_2\)-\(M_3\) module gives an \(M_1\)-\(M_3\) product, and reversal gives an \(M_3\)-\(M_1\) product. The separate irreducible-sector/principal-graph classification remains the D8 callback and is not claimed here. No trace assumption is used in the theorem; a finite trace is only the callback's specialization.

## Calculations and problems

## Calculations, examples and solved problems

The calculations use the conventions in FU-01–04 and the comparison maps in FU-09. They illustrate the general results; none replaces the arbitrary-algebra proofs.

### Scalar normalization and the change of symbols

For \(\lambda>0\), let \(\psi_\lambda(z)=\lambda z\) on the positive cone of \(N=\mathbb C\). Its GNS space is \(\mathbb C\) with inner product
\(\langle z,w\rangle_\lambda=\lambda z\overline w\), GNS map \(\Lambda_\lambda(z)=z\), conjugation \(Jz=\overline z\), and ordinary scalar left and right actions. In particular \(\Lambda'_\lambda(z)=z\).

For \(H=K=\mathbb C\) with their usual Hilbert norms, every vector is right bounded and

\[
 L_\lambda(\xi)z=\xi z,\qquad
 L_\lambda(\chi)^*L_\lambda(\xi)
       =\frac{\overline\chi\xi}{\lambda}.
\]

The factor \(1/\lambda\) comes from the inner product on the operator's domain. Thus

\[
 \left\langle\xi\otimes_{\psi_\lambda}\eta,
                    \chi\otimes_{\psi_\lambda}\zeta\right\rangle
 =\frac{\xi\overline\chi\eta\overline\zeta}{\lambda}.
\]

The map

\[
 U_\lambda(\xi\otimes_{\psi_\lambda}\eta)
       =\frac{\xi\eta}{\sqrt\lambda}
 \tag{FE.1}
\]

therefore preserves every finite-sum pairing. It is onto \(\mathbb C\), since its range contains \(1\). It identifies the null quotient and completion exactly.

The canonical standard comparison from \(L_\mu\) to \(L_\lambda\) is
\(I_{\lambda\leftarrow\mu}z=\sqrt{\mu/\lambda}\,z\): it preserves the weighted norms and the nonnegative real cone. Applying FU-09 to its precomposition gives

\[
 W_{\mu\leftarrow\lambda}
       (\xi\otimes_{\psi_\lambda}\eta)
   =\sqrt{\mu/\lambda}\,
       \xi\otimes_{\psi_\mu}\eta.
 \tag{FE.2}
\]

Equivalently \(U_\mu W_{\mu\leftarrow\lambda}=U_\lambda\). For example, when \(\lambda=1\) and \(\mu=9\), the unchanged target symbol has one third of the norm of the original symbol; the canonical map multiplies it by \(3\). This is a complete instance of the distinction in Takesaki II, IX.3, Remark 3.22.

### A diagonal algebra, including uncountable index sets

Let \(I\) be any nonempty set, \(N=\ell^\infty(I)\), and
\(H=K=\ell^2(I)\), with coordinatewise right and left actions. Put

\[
 \psi(a)=\sum_{i\in I}a_i,\qquad a\in N_+,
\]

where the sum is the supremum over finite subsets of \(I\). This is a faithful normal semifinite weight. Faithfulness follows by testing individual coordinates. For normality, if \(a_\alpha\uparrow a\), each finite coordinate sum preserves the increasing supremum; taking the supremum over both indices in either order gives
\(\psi(a)=\sup_\alpha\psi(a_\alpha)\).
Finite-coordinate truncations \(p_Fa\) increase to \(a\) and have finite weight, proving semifiniteness.

The standard form is \(\ell^2(I)\), with \(J\) coordinate conjugation, the cone of nonnegative real vectors, and

\[
 \mathfrak n_\psi=\ell^2(I)\subset\ell^\infty(I),\qquad
 \Lambda_\psi(x)=x .
\]

Here every square-summable family is bounded, and finite support vectors give the required density. Both the GNS involution and its adjoint are coordinate conjugation, so the modular operator is \(1\). The displayed standard form and right action follow directly.

Every \(\xi\in\ell^2(I)\) is right \(\psi\)-bounded:

\[
 \sum_i|\xi_i x_i|^2
       \leq\|\xi\|_\infty^2\sum_i|x_i|^2.
\]

Its operator \(L_\psi(\xi)\) is multiplication by \(\xi\), with norm \(\|\xi\|_\infty\); testing the individual unit vectors proves the latter equality. Consequently

\[
 L_\psi(\chi)^*L_\psi(\xi)
       =M_{\overline\chi\,\xi}.
\]

For finite tensor sums define

\[
 m\left(\sum_{r=1}^n \xi^{(r)}\odot\eta^{(r)}\right)_i
       =\sum_{r=1}^n\xi_i^{(r)}\eta_i^{(r)}.
\]

The output belongs to \(\ell^2(I)\): each product has norm at most
\(\|\xi^{(r)}\|_\infty\|\eta^{(r)}\|_2\), and there are only finitely many terms. Expanding the finite sums gives exactly

\[
 B(u,v)=\langle m(u),m(v)\rangle_{\ell^2(I)}.
 \tag{FE.3}
\]

Thus the full nullspace is \(\ker m\). The range contains each coordinate vector \(e_i=m(e_i\odot e_i)\); their finite spans are dense. The isometry induced by \(m\) on the null quotient extends onto \(\ell^2(I)\). Hence

\[
 H\otimes_\psi K\simeq\ell^2(I),\qquad
 \xi\otimes_\psi\eta\longmapsto(\xi_i\eta_i)_{i\in I}.
 \tag{FE.4}
\]

Every approximation by finite coordinates is a net; no countable enumeration of \(I\) has been chosen.

When \(I\) is uncountable, \(N\) has no faithful normal positive bounded functional. To see this, let \(f\) be one such functional and set \(m_i=f(p_i)\geq0\). Every finite sum of the \(m_i\)'s is at most \(f(1)<\infty\). For each positive integer \(n\), there can be only finitely many \(i\) with \(m_i\geq1/n\). Thus at most countably many \(m_i\)'s are nonzero. Some \(p_i\neq0\) has \(f(p_i)=0\), contradicting faithfulness. Nevertheless the reference weight \(\psi\), the module actions and the fusion computation above are valid. The general construction therefore has content beyond a faithful-state model.

### Why faithful outer factors do not give an injective joint action

Specialize the preceding calculation to \(I=\{1,2\}\). All spaces and bounded-vector domains are \(\mathbb C^2\). The four tensors \(e_i\odot e_j\) are an algebraic basis, and (FE.3) gives

\[
 m(e_1\odot e_1)=e_1,\quad m(e_2\odot e_2)=e_2,\quad
 m(e_1\odot e_2)=m(e_2\odot e_1)=0.
\]

The nullspace is exactly the span of the two off-diagonal tensors. The fusion completion is \(\mathbb C^2\).

Both outer endomorphism algebras are the diagonal algebra \(\mathbb C^2\): commuting with the two coordinate projections forces an operator to preserve each coordinate line, and every diagonal operator does commute. Their two induced representations on fusion are

\[
 j_P(a)=\operatorname{diag}(a_1,a_2),\qquad
 j_Q(b)=\operatorname{diag}(b_1,b_2).
\]

Each is faithful, normal and unital. Their joint algebraic tensor action is

\[
 \Theta(a\odot b)
       =\operatorname{diag}(a_1b_1,a_2b_2).
 \tag{FE.5}
\]

It annihilates the nonzero tensor \(p_1\odot p_2\). That tensor is nonzero because the tensor product of the first and second coordinate functionals evaluates to \(1\) on it. In fact the kernel is exactly the two-dimensional span of the off-diagonal coordinate tensors. Thus normality, unitality, faithfulness of each factor and nondegeneracy of the joint action do not imply injectivity of the joint algebraic tensor representation.

The original \(N\)-actions on \(H=K=\mathbb C^2\) are faithful as well: a diagonal element annihilating either module has both coordinates zero. Thus this example meets the standing faithful-module convention of Takesaki II, IX.3, Definition 3.1(ii) (printed p. 186) and contradicts the unqualified algebraic joint-action injectivity in Corollary 3.18(ii) (printed p. 202 / PDF p. 222). The finite calculation includes the exact null quotient, so its conclusion is not an artifact of an unfinished completion or an infinite-weight domain.

### A matrix calculation fixes the half-modular sign

Let \(N=M_2(\mathbb C)\), \(d=\operatorname{diag}(1,4)\), and
\(\psi(a)=\operatorname{Tr}(da)\). Use the standard Hilbert–Schmidt form

\[
 \Lambda_\psi(a)=a\sqrt d,\qquad JX=X^*,\qquad
 \lambda(a)X=aX,\qquad \rho(b)X=Xb .
\]

The GNS involution on this finite-dimensional space satisfies
\(S(a\sqrt d)=a^*\sqrt d\). Direct substitution into its polar decomposition gives
\(\Delta X=dXd^{-1}\), and hence
\(\sigma_z^\psi(b)=d^{iz}bd^{-iz}\) for every complex \(z\). Every domain is the full relevant finite-dimensional space.

For \(\xi\) in the standard right module \(H=\operatorname{HS}_2\), the right bounded operator is

\[
 L_\psi(\xi)X=\xi d^{-1/2}X.
\]

Indeed \(\Lambda'_\psi(x)=\sqrt d\,x\), and applying the displayed operator yields \(\xi x\). For the usual left module \(K=\mathbb C^2\), fusion is identified with \(K\) by

\[
 V(\xi\otimes_\psi\eta)=\xi d^{-1/2}\eta .
 \tag{FE.6}
\]

The coefficient formula proves preservation of every finite-sum pairing, and \(\xi=\sqrt d\) proves surjectivity.

Take \(\xi=\sqrt d\), \(b=E_{12}\), and \(\eta=e_2\). Then

\[
 V((\xi b)\otimes_\psi\eta)
       =\sqrt d\,b\,d^{-1/2}e_2=\tfrac12e_1 .
\]

On the other hand,

\[
 \sigma^\psi_{-i/2}(b)=d^{1/2}bd^{-1/2}=\tfrac12E_{12},
 \qquad
 \sigma^\psi_{+i/2}(b)=d^{-1/2}bd^{1/2}=2E_{12}.
\]

Since \(V(\xi\otimes_\psi\zeta)=\zeta\), the negative half-modular balancing formula gives \(\tfrac12e_1\), while the positive sign gives \(2e_1\). The two vectors differ. This verifies the sign under the stated right action and disproves the printed positive sign in Corollary 3.18(iii). The full endpoint-domain proof for the corrected negative sign is provided separately; this finite computation does not replace it.

**Finite modular-sign check.** For \(d=\operatorname{diag}(1,4)\), \(\xi=\sqrt d\), \(b=E_{12}\), and \(\eta=e_2\), (FE.6) gives \(V((\xi b)\otimes_\psi\eta)=\tfrac12e_1\). The negative-half expression agrees; the printed positive-half expression gives \(2e_1\). The general endpoint-domain proof is (BD.4–6). The same results are treated in Takesaki II, IX.3, Corollary 3.18(iii) (printed p. 203).

### Composition of automorphism-twisted correspondences

Let \((N,L,J,P)\) be any standard form. For a normal automorphism \(\alpha\), define the bimodule \(H_\alpha\) on \(L\) by

\[
 a\cdot\xi\cdot b=\lambda(a)\rho(\alpha(b))\xi .
\]

Let \(u_\alpha\) be SF-12 and SE-10's canonical unitary implementing \(\alpha\), preserving \(P\), and commuting with \(J\). It also implements the right action:
\(u_\alpha\rho(b)u_\alpha^*=\rho(\alpha(b))\).
Canonical uniqueness gives \(u_\alpha u_\beta=u_{\alpha\circ\beta}\).

Every right intertwiner from \(L\) to \(H_\alpha\) has the unique form

\[
 T_x=\lambda(x)u_\alpha,\qquad x\in N.
\]

Indeed \(Tu_\alpha^*\) commutes with all \(\rho(N)\), and that commutant is \(\lambda(N)\). Conversely each \(T_x\) has the required intertwining property. Its coefficients are

\[
 T_y^*T_x=\lambda(\alpha^{-1}(y^*x)).
\]

In the complete intertwiner model of \(H_\alpha\boxtimes_N H_\beta\), prescribe

\[
 V_{\alpha,\beta}[T_x,\eta]
       =\lambda(x)u_\alpha\eta .
 \tag{FE.7}
\]

The pairing of the two proposed images is

\[
 \langle\lambda(x)u_\alpha\eta,\lambda(y)u_\alpha\zeta\rangle
 =\langle\lambda(\alpha^{-1}(y^*x))\eta,\zeta\rangle,
\]

which is the fusion coefficient. Finite sums give preservation of the whole semidefinite form, so this descends and extends to an isometry. The elements \([u_\alpha,\eta]\) map to every vector of \(L\); hence it is onto.

For the left action, multiplying \(T_x\) by \(\lambda(a)\) gives \(T_{ax}\), and (FE.7) gives the usual left action on its image. For the right action,

\[
 \lambda(x)u_\alpha\rho(\beta(b))\eta
 =\rho(\alpha(\beta(b)))\,\lambda(x)u_\alpha\eta .
\]

Therefore the target right twist is \(\alpha\circ\beta\), in that order:

\[
 H_\alpha\boxtimes_N H_\beta\simeq H_{\alpha\circ\beta}.
 \tag{FE.8}
\]

This proves the correspondence composition law associated with Takesaki II, IX.3, Exercise 10 without a trace, a faithful state, or a separate action-cocycle theorem. The weight-labelled versions follow through FU-03 and FU-09's specified unitary comparisons.

### Problems with complete solutions

**Problem 1.** In the scalar model, a map from the \(\lambda\)-fusion space to the \(\mu\)-fusion space sends the displayed symbol \(\xi\otimes_{\psi_\lambda}\eta\) to \(c\,\xi\otimes_{\psi_\mu}\eta\). Determine all constants making it unitary, and identify the canonical one.

**Solution.** Formula (FE.1) shows that its norm on the one-dimensional completion is \(|c|\sqrt{\lambda/\mu}\). Thus it is unitary exactly when \(|c|=\sqrt{\mu/\lambda}\). All such constants differ by a phase. The standard positive-cone comparison fixes the positive real value \(c=\sqrt{\mu/\lambda}\), as (FE.2) proves. Norm preservation by itself would not determine that phase.

**Problem 2.** Let \(N=\mathbb C^2\), let \(H=\mathbb C\) carry the first-coordinate right action, and let \(K=\mathbb C\) carry the second-coordinate left action. Compute their fusion for the faithful trace \(\psi(a_1,a_2)=a_1+a_2\).

**Solution.** The reference standard module is \(\mathbb C^2\). A right intertwiner into \(H\) is \(T_t(z_1,z_2)=tz_1\). Its coefficient \(T_s^*T_t\) is the diagonal element \((\overline s t,0)\). The left representation on \(K\) annihilates that coefficient. Every finite-sum pairing is therefore zero; the exact nullspace is the whole algebraic tensor space and the fusion Hilbert space is zero. Both module actions are unital and normal despite their kernels. Unitality of the induced actions on the zero Hilbert space is consistent: the identity operator there is zero.

**Problem 3.** In the matrix model, prove directly for arbitrary \(b\in M_2(\mathbb C)\) that the corrected balancing relation holds for every \(\xi,\eta\). State precisely when replacing the negative half-modular expression by \(b\) itself gives the same relation for every \(\xi,\eta\).

**Solution.** Applying (FE.6) to the two sides gives

\[
 \xi b d^{-1/2}\eta,\qquad
 \xi d^{-1/2}(d^{1/2}bd^{-1/2})\eta,
\]

which are equal. Since \(V\) is unitary, the two fusion vectors agree. Untwisted balancing for every \(\xi,\eta\) is equivalent to
\(b d^{-1/2}=d^{-1/2}b\): necessity follows by taking \(\xi=1\) and arbitrary \(\eta\), and sufficiency follows by substitution. Multiplying or applying the finite-dimensional functional calculus shows this is equivalent to \(bd=db\). Thus the untwisted formula holds exactly on the centralizer of this weight.

**Problem 4.** Characterize the automorphisms \(\alpha\) for which \(H_\alpha\) is isomorphic to the identity correspondence \(H_{\mathrm{id}}\) by a unitary intertwining both actions.

**Solution.** A unitary \(F:L\to L\) intertwining the left actions lies in \(\lambda(N)'=\rho(N)\), so \(F=\rho(v)\) for a unitary \(v\in N\). The right intertwining identity is

\[
 \rho(v)\rho(\alpha(b))=\rho(b)\rho(v)\quad(b\in N).
\]

Because \(\rho\) reverses multiplication and is faithful, this says
\(\alpha(b)v=vb\), or \(\alpha(b)=vbv^*\). Hence \(\alpha\) is inner. Conversely, if \(\alpha=\operatorname{Ad}v\), the same calculation shows that \(\rho(v)\) is a unitary bimodule isomorphism from \(H_\alpha\) to the identity correspondence. Combining this with (FE.8) explains why an inner twist has no effect on the isomorphism class of the correspondence, while the composition order remains fixed.

**Problem 5 (finite fibers, including missing support).** Let \(N=\mathbb C^m\) with its counting trace. Let \(H=\bigoplus_{i=1}^m H_i\) and \(K=\bigoplus_{i=1}^m K_i\), where the actions of \(N\) are coordinatewise and some \(H_i\) or \(K_i\) may be zero. Construct an explicit unitary

\[
 H\boxtimes_N K\ \cong\ \bigoplus_{i=1}^m(H_i\otimes_{\mathbb C}K_i).
 \tag{FE.9}
\]

Identify exactly when the fusion is zero and what happens to a tensor supported in distinct coordinates.

**Solution.** The standard module is \(L=\mathbb C^m\). Every right intertwiner \(T:L\to H\) is determined by vectors \(h_i=T e_i\in H_i\), and conversely any such tuple defines \(T_h(z_1,\ldots,z_m)=(z_ih_i)_i\). If \(S=T_g\), then

\[
 S^*T_h=\operatorname{diag}
 \bigl(\langle h_1,g_1\rangle,\ldots,\langle h_m,g_m\rangle\bigr).
\]

The map on finite sums is

\[
 \sum_r[T_{h^{(r)}}\odot\eta^{(r)}]
 \longmapsto
 \left(\sum_rh_i^{(r)}\otimes_{\mathbb C}\eta_i^{(r)}\right)_{i=1}^m .
\]

The coefficient form (FU.10) is exactly the direct-sum Hilbert-tensor pairing of these images, including all cross terms. Its kernel is therefore the whole radical, and it induces an isometry of the quotient. For each \(i\), vectors \(h_i\otimes\eta_i\) arise by taking both inputs supported only at \(i\); their finite spans are dense in the right-hand side. Hence the isometry extends onto (FE.9). A tensor whose factors are supported at distinct coordinates maps to zero. The fusion is zero exactly when no \(i\) has both \(H_i\ne0\) and \(K_i\ne0\).

**Problem 6 (coordinatewise bounded is insufficient).** Give a faithful finite reference weight, a Hilbert direct sum \(H=\bigoplus_{n\ge1}H_n\), and a vector \(\xi=(\xi_n)\in H\) such that every \(\xi_n\) is right weight-bounded but \(\xi\notin D(H,\psi)\). Verify the failure using (AU.36).

**Solution.** Let \(N=\ell^\infty(\mathbb N)\), \(p_n\) its coordinate projections, and

\[
 \psi(a)=\sum_{n\ge1}2^{-n}a_n\qquad(a\in N_+).
\]

This is a faithful normal finite weight. Take every \(H_n=H_\psi\) with its standard right action and put \(\xi_n=\Lambda_\psi(np_n)\). Each \(np_n\) belongs to \(\mathfrak n_\psi=N\), so (FU.19) gives \(L_\psi(\xi_n)=n\pi_\psi(p_n)\). Yet

\[
 \sum_n\|\xi_n\|^2=\sum_n n^2 2^{-n}<\infty,
\]

so \(\xi\) belongs to the Hilbert direct sum. For a finite \(F\subset\mathbb N\),

\[
 \left\|\sum_{n\in F}L_\psi(\xi_n)^*L_\psi(\xi_n)\right\|
 =\left\|\sum_{n\in F}n^2\pi_\psi(p_n)\right\|
 =\max_{n\in F}n^2 .
\]

The supremum over finite \(F\) is infinite, so (AU.36) proves \(\xi\notin D(H,\psi)\). Square summability of vectors does not itself bound their operator column.

**Problem 7 (the associator on finite fibers).** In Problem 5, let \(K\) also carry a right \(N=\mathbb C^m\)-action that acts by the same \(i\)-th coordinate on \(K_i\), and add the left module \(Z=\bigoplus_i Z_i\). Compute FU-08's associator on a pure tensor supported at \(i\). Explain its pentagon when the intermediate modules in a fourfold product have the same diagonal left and right decompositions.

**Solution.** Apply (FE.9) twice. The two bracketings identify with

\[
 \bigoplus_i\bigl((H_i\otimes K_i)\otimes Z_i\bigr)
 \quad\text{and}\quad
 \bigoplus_i\bigl(H_i\otimes(K_i\otimes Z_i)\bigr).
\]

Let \(T_{h_i}:L\to H\) and \(S_{k_i}:L\to K\) be supported at \(i\). Formula (F.21) sends

\[
 (h_i\otimes k_i)\otimes z_i
 \longmapsto h_i\otimes(k_i\otimes z_i).
\]

Finite sums of these generators are dense by Problem 5, so this determines the unitary. For four factors, each path in (F.37) sends a pure \(i\)-fiber tensor to the same fully right-associated tensor. Their spans are dense, proving the pentagon in this model; (F.37) proves it in the full generality.

**Problem 8 (the full matrix centralizer).** Replace \(M_2(\mathbb C)\) in (FE.6) by \(M_n(\mathbb C)\), with \(d=\operatorname{diag}(d_1,\ldots,d_n)\) and \(d_i>0\). Determine which \(b\) satisfy \((\xi b)\otimes_\psi\eta=\xi\otimes_\psi b\eta\) for every \(\xi\in H_\psi\) and \(\eta\in\mathbb C^n\). Give the entries of the corrected half-modular multiplier.

**Solution.** The same Hilbert–Schmidt calculation as (FE.6) gives the onto unitary \(V(\xi\otimes_\psi\eta)=\xi d^{-1/2}\eta\), and every vector is eligible. Taking \(\xi=d^{1/2}\), the untwisted identity for all \(\eta\) forces \(d^{1/2}bd^{-1/2}=b\), equivalently \(db=bd\). Conversely, this commutation makes the identity hold for every \(\xi,\eta\). Entrywise it says \((d_i-d_j)b_{ij}=0\). The corrected multiplier is

\[
 \bigl(\sigma^\psi_{-i/2}(b)\bigr)_{ij}
 =\sqrt{d_i/d_j}\,b_{ij}.
 \tag{FE.10}
\]

The positive-half multiplier has the reciprocal ratio.

**Problem 9 (linearity of conjugate reversal).** In Problem 5's finite-fiber model, determine the action of (CF.8) on \(C(h_i\otimes k_i)\), and check scalar linearity in its conjugate source space.

**Solution.** Formula (CF.4) gives

\[
 \mathfrak c_{H,K}\bigl(C(h_i\otimes k_i)\bigr)
 =C_Kk_i\otimes C_Hh_i
 \quad\text{in }\overline K_i\otimes\overline H_i.
\]

For \(c\in\mathbb C\), scalar multiplication in the conjugate source is \(c\,C(v)=C(\overline c\,v)\). The image of \(C(\overline c\,h_i\otimes k_i)\) is \(C_Kk_i\otimes C_H(\overline c\,h_i)=c(C_Kk_i\otimes C_Hh_i)\). Thus reversal is linear out of the conjugate space, while \(T\mapsto C_HTJ_L\) before that conjugation is conjugate-linear.

### Further course routes

The diagonal calculation suggests the direct-integral description of fusion over an abelian algebra. Proving that theorem requires measurable fields, their tensor products and the local separability assumptions in the source statement. The finite diagonal model does not establish that measurable-field theorem.

The correspondence composition calculation also supplies the fusion machinery used in finite-index iteration. The finite-factor specialization and conjugate modules use this machinery; irreducible-sector classification and the principal graph are separate topics. No classification theorem follows from the construction or associativity alone.

## References and source correspondence

The primary source is Masamichi Takesaki, [*Theory of Operator Algebras II*](https://doi.org/10.1007/978-3-662-10451-4), Encyclopaedia of Mathematical Sciences 125, Springer-Verlag, 2003, §IX.3, printed pp. 186–210. FU-09 also uses that volume's definitions of \(\mathcal W\) and \(\mathcal W_0\) at printed p. 154. The finite-factor callback is in Takesaki, [*Theory of Operator Algebras III*](https://doi.org/10.1007/978-3-662-10453-8), Encyclopaedia of Mathematical Sciences 127, Springer-Verlag, 2003, §XIX.2, Exercise 4, printed pp. 439–440. For both inspected Volume II spans, the one-based PDF page is the printed page plus 20; for the inspected Volume III callback, it is the printed page plus 20.

The following map identifies antecedent statements and the native course results used in the proofs. Each abbreviated native item has the prefix \(\text{OA-MOD-}\), so SF-10 denotes OA-MOD-SF-10, for example. A source antecedent is not a substitute for the proofs above. In particular the full-radical quotient, arbitrary-cardinality cutoff arguments, coherence calculation, and explicit counterexamples are established in this unit.

| Unit | Source antecedent and printed page | Native course inputs used here |
| --- | --- | --- |
| FU-01 | II, IX.3, Definition 3.1 and Proposition 3.2, pp. 186–187; Exercise 7, pp. 209–210 | SF-10/11, SE-02/03/10, WH-13 |
| FU-02 | II, IX.3, Proposition 3.15(i) and Definition 3.16, pp. 200–201 | WH-02, NP-06 |
| FU-03 | II, IX.3, Proposition 3.15 and Definition 3.16, pp. 200–201 | WG-008/009, WH-04/11, MF-06 |
| FU-04 | II, IX.3, Proposition 3.15(ii), Theorem 3.17, pp. 200–202; Exercise 8, p. 210 | SF-03/04, SE-02/03/10, CW-06, CZ-05/09, WH-04/11 |
| FU-05 | II, IX.3, Corollary 3.18(i)–(ii), p. 202 | BK-04, WH-02, NP-06 |
| FU-06 | II, IX.3, Proposition 3.19 and adjacent direct-sum display, p. 203 | FU-01–05, WG-008 |
| FU-07–08 | II, IX.3, Theorem 3.20, pp. 203–204 | FU-01–06, BK-01, NP-06, WH-02 |
| FU-08 endpoint | II, standard GNS action, p. 187, and IX.3, Corollary 3.18(iii), p. 203 | MF-06–09/11, HAP-05/07, WH-02/11, NP-06, NW-12, MA-03/08, CX-03, FU-02–03 |
| FU-09 | II, definitions of \(\mathcal W,\mathcal W_0\), p. 154; IX.3, Theorem 3.21, pp. 205–206, and Remark 3.22, p. 206 | SF-09, SE-10, WG-008, FU-01–08 |
| FU-10 | No source antecedent is claimed for the general reversal proof; III, XIX.2, Exercise 4, pp. 439–440, is a later finite-factor application | FU-01–09 |
| FU-11 | II, IX.3, Remark 3.22, p. 206, for the scalar weight comparison, and Exercise 10, p. 210, for the automorphism-twist problem; the other calculations are independent examples | SF-12, SE-10, FU-01–10 |

This map is bounded to the unit's claims. Takesaki II, IX.3, Proposition
3.23 (the measurable direct-integral model, printed pp. 206–207) and
Exercises 1–6, 9, and 11 (printed pp. 207–210) remain separate source
obligations. In particular, neither the finite-fiber calculation nor the
automorphism-twist composition law claims the full direct-integral theorem,
the semifinite-trace measurable-operator model, or a classification of every
full bimodule.

The Volume II text's Corollary 3.18(ii) asserts injectivity of the joint algebraic outer action under its standing faithful-module convention. The faithful finite example (FE.3–5) shows a kernel. Its Corollary 3.18(iii) prints a positive-half balancing expression under a positive-half analytic-domain hypothesis; the standard right action on printed p. 187, the general proof (BD.4–6), and the finite calculation (FE.6) require the negative half on its corresponding negative-half domain under the conventions used here. Theorem 3.21's first antecedent pair has the broader second-weight quantifier described in FU-09; the proved comparison here covers two faithful normal semifinite weights. These statements specify the exact points of departure from the source, while the other rows identify mathematical context rather than reproducing its prose.
## The operator GNS map and its normal right action

Let \(\psi\) be faithful, normal and semifinite on \(N\), put \(L=L^2(N)\) in its standard GNS coordinates, and let \(H\) be any normal unital right \(N\)-module. Its action may have a kernel. Write \(\pi=\pi_\psi\), \(\Lambda=\Lambda_\psi\), and

\[
\begin{gathered}
 X=\operatorname{Hom}_{N^{\mathrm{op}}}(L,H),\\
 \begin{aligned}
 \mathfrak n_\psi(H)&=\{T\in X:\\
                  &\quad\psi(c_T)<\infty\}.
 \end{aligned}
 \end{gathered}
\tag{OG.1}
\]

Here \(c_T=\pi^{-1}(T^*T)\). The inverse in this formula is meaningful: \(T^*T\) commutes with the standard right action, whose commutant is \(\pi(N)\), by FU-01. The bounded-vector space \(D(H,\psi)\) and its injective map \(L_\psi\) are those of FU-03. No weight on the left endomorphism algebra is needed here.

**The operator GNS dictionary.** There is a linear bijection with dense range in \(H\),

\[
 \begin{gathered}
 \eta_\psi^H:\mathfrak n_\psi(H)\longrightarrow D(H,\psi),\\
 L_\psi(\eta_\psi^H(T))=T,\\
 \|\eta_\psi^H(T)\|^2=\psi(\pi^{-1}(T^*T)).
 \end{gathered}
 \tag{OG.2}
\]

For its concrete formula, take the rectangular polar decomposition

\[
\begin{gathered}
 T=u\pi(a),\qquad a\in N_+,\\
 \eta_\psi^H(T)=u\Lambda(a).
 \end{gathered}
\tag{OG.3}
\]

Here \(a^2=\pi^{-1}(T^*T)\), and \(u\) is the polar partial isometry from \(L\) to \(H\). BK-07 constructs it as the strong* limit of the bounded right intertwiners \(T(\pi(a)+\varepsilon)^{-1}\). Thus \(u\in X\) and \(u^*u=\pi(s(a))\). If \(T\in\mathfrak n_\psi(H)\), then \(a\in\mathfrak n_\psi\). FU-03 gives \(L_\psi(\Lambda(a))=\pi(a)\), and the defining test formula (FU.17) gives \(L_\psi(u\Lambda(a))=u\pi(a)=T\). Also \(\pi(s(a))\Lambda(a)=\Lambda(s(a)a)=\Lambda(a)\). This proves the norm identity in (OG.2).

Conversely, take \(\xi\in D(H,\psi)\) and polar-decompose \(T=L_\psi(\xi)=u\pi(a)\). The adjoint intertwiner \(u^*\) gives \(L_\psi(u^*\xi)=u^*T=\pi(a)\). The full standard-module dictionary (FU.20) says that \(u^*\xi=\Lambda(c)\) for some \(c\in\mathfrak n_\psi\). Then (FU.19) and faithfulness of \(\pi\) imply \(c=a\); in particular \(a\in\mathfrak n_\psi\). For every \(x\in\mathfrak n_\psi^*\), the vector \(\xi x=T\Lambda'_\psi(x)\) belongs to the closed range of \(u\). WG-008 supplies positive finite contractions \(e_i\to1\) strongly*. Normality of the right action gives \(\xi e_i\to\xi\) in norm. Therefore \(\xi\) itself belongs to that range, and \(\xi=uu^*\xi=u\Lambda(a)\). This proves the onto and inverse assertions on the entire domain.

The domain in (OG.1) is linear: the coefficient inequality
\((S+T)^*(S+T)\le2S^*S+2T^*T\), monotonicity of \(\psi\), and the scalar case prove this directly. The inverse of the injective linear map \(L_\psi\) is linear there. FU-03 proves density of \(D(H,\psi)\), using all right intertwiners and GNS density. If \(M=\operatorname{End}_{N^{\mathrm{op}}}(H)\), then for every \(c\in M\),

\[
\begin{gathered}
 cT\in\mathfrak n_\psi(H),\\
 \eta_\psi^H(cT)=c\eta_\psi^H(T),\\
 \|\eta_\psi^H(cT)\|\\
       \le\|c\|\,\|\eta_\psi^H(T)\|.
 \end{gathered}
\tag{OG.4}
\]

Membership follows from \(T^*c^*cT\le\|c\|^2T^*T\); the vector identity follows from (FU.17) and injectivity. Thus this dictionary also preserves the left action.

**The analytic algebra really is an algebra.** Use exactly the closed-strip endpoint domains defined in the FU-08 companion, including sigma-weak continuity and boundedness. Put

\[
\begin{aligned}
 A={}&D(\sigma_{-i/2}^\psi)\\
     &\cap D(\sigma_{+i/2}^\psi).
 \end{aligned}
\tag{OG.5}
\]

We justify the product issue at the boundary. A bounded sigma-weakly continuous, scalar-holomorphic strip extension \(F\) has operator-norm holomorphy in its interior by the Cauchy-coefficient argument in FU-08. Its boundary values are the real orbits of its two endpoints, by (BD.8). Those orbits are strongly* continuous. Indeed, sigma-weak continuity of \(\sigma_t(b)\) and of \(\sigma_t(b^*b)\), followed by expansion of \(\|(\pi(\sigma_t(b))-\pi(\sigma_{t_0}(b)))\zeta\|^2\), proves strong continuity; apply the same argument to \(b^*\).

Here is the passage from boundary-orbit continuity to continuity through the strip. Fix a boundary point \(z_0\), a vector \(\zeta\), and a sufficiently small rectangle in the strip with \(z_0\) at the midpoint of one horizontal side. On that side, \(\|(F(z)-F(z_0))\zeta\|<\varepsilon\) after shrinking the rectangle. On the other three sides it is bounded by a constant \(C\), since \(F\) is bounded. In coordinates \(|v|\le\delta\), \(0\le u\le\delta\), measured from that side into the strip, the harmonic polynomial

\[
\begin{aligned}
 h(v,u)={}&\frac{2u}{\delta}\\
         &+\frac{v^2-u^2}{\delta^2}.
 \end{aligned}
\tag{OG.6}
\]

is nonnegative, is at least one on the other three sides, and tends to zero at \((0,0)\). Apply the scalar rectangle maximum principle to the real part of every phase multiple of \(\langle(F(z)-F(z_0))\zeta,\chi\rangle\), with \(\|\chi\|\le1\). It gives
\(\|(F(z)-F(z_0))\zeta\|\le\varepsilon+Ch(v,u)\). Every scalar test is continuous on the closed rectangle, so the principle applies. Taking the limit and then \(\varepsilon\downarrow0\) proves strong continuity at \(z_0\). The scalar tests of \(F(z)^*\zeta\) are antiholomorphic, whose real parts are harmonic; the identical argument proves strong* continuity. This uses only the scalar maximum principle already included in MA-01/08, not norm continuity of an endpoint orbit.

Consequently the product of two extensions on the same strip is sigma-weakly continuous up to both boundaries: bounded strongly* convergent products converge strongly*. It is norm holomorphic inside, has the correct real orbit, and remains bounded. Thus each endpoint domain is an algebra, and its endpoint map preserves products. Reflection \(z\mapsto\overline z\) together with adjoint interchanges the two domains. Their intersection \(A\) is therefore a unital self-adjoint subalgebra. Its Gaussian entire elements approximate every \(b\in N\) strongly*, with norm at most \(\|b\|\), by (BD.12–15).

For clarity, \(A\) multiplies \(\mathfrak n_\psi\) and \(\mathfrak n_\psi\cap\mathfrak n_\psi^*\) from both sides. Left multiplication on \(\mathfrak n_\psi\) is the finite-left-ideal property. For \(c\in A\), translate its upper-strip extension downward by \(i/2\): this gives a lower-strip extension for \(b=\sigma_{+i/2}^\psi(c)\) with endpoint \(c\). Formula (BD.7) then gives \(yc\in\mathfrak n_\psi\) for every \(y\in\mathfrak n_\psi\). Applying both conclusions to adjoints, since \(A=A^*\), proves the assertions on the finite-star ideal. Taking adjoints also proves two-sided invariance of the adjoint finite ideal. This translation is an actual strip extension, not a complex group law outside its domain.

**The action on the full operator domain.** If \(b\in D(\sigma_{-i/2}^\psi)\) and \(d=\sigma_{-i/2}^\psi(b)\), then

\[
\begin{gathered}
 T\pi(d)\in\mathfrak n_\psi(H),\\
 \eta_\psi^H(T\pi(d))\\
      =\eta_\psi^H(T)b,\\
 \|\eta_\psi^H(T\pi(d))\|\\
      \le\|b\|\,\|\eta_\psi^H(T)\|.
 \end{gathered}
\tag{OG.7}
\]

In (OG.3), formula (BD.7) gives \(ad\in\mathfrak n_\psi\) and \(\Lambda(ad)=\Lambda(a)b\). The coefficient of \(u\pi(ad)\) is bounded above by \(\pi(d^*a^2d)\), so it is finite. The defining inverse in (OG.2) gives \(\eta_\psi^H(u\pi(ad))=u\Lambda(ad)\). As \(u\) is a right intertwiner, this is \((u\Lambda(a))b\); its norm is bounded by the bounded right action. This proves every clause on the full stated domain.

In particular, for \(b\in A\) put \(d=\sigma_{-i/2}^\psi(b)\). On the dense range of \(\eta_\psi^H\), the source's formula

\[
\begin{gathered}
 \pi'_\psi(b)\eta_\psi^H(T)\\
       =\eta_\psi^H(T\pi(d)),\\
 b\in A.
 \end{gathered}
\tag{OG.8}
\]

equals the original operator \(\rho_H(b)\). Thus it is well-defined and bounded by \(\|b\|\), preserves adjoints, has the unit, and is an antirepresentation: \(\pi'_\psi(bc)=\pi'_\psi(c)\pi'_\psi(b)\). It extends to the original normal right action on all of \(N\). That normal extension is unique. For any \(b\in N\), its bounded Gaussian approximants lie in \(A\) and converge sigma-strongly*; NP-06 transports that limit through either normal representation of \(N^{\mathrm{op}}\). Two extensions agreeing on \(A\) therefore agree on every \(b\). The proof uses neither a finite value at the identity nor a countable approximate unit.

**A complete matrix check.** Let \(N=M_2(\mathbb C)\), \(\psi(x)=\operatorname{Tr}(Dx)\), \(D=\operatorname{diag}(1,4)\), and \(H=L=\mathrm{HS}_2\) with right matrix multiplication. Here \(\Lambda(a)=aD^{1/2}\). Take \(T=\pi(1)\) and \(b=E_{12}\). All matrices are entire, and

\[
\begin{gathered}
 d=D^{1/2}bD^{-1/2}\\
      =\tfrac12E_{12},\\
 \eta_\psi^H(T)=D^{1/2},\\
 \eta_\psi^H(T\pi(d))\\
      =dD^{1/2}=E_{12},\\
 \eta_\psi^H(T)b\\
      =D^{1/2}b=E_{12}.
 \end{gathered}
\tag{OG.9}
\]

Using \(T\pi(b)\) instead would give \(2E_{12}\). This calculation checks both the negative-half endpoint and which side multiplies the operator coordinate.

This original exposition supplies the detail left to the reader in Takesaki II IX.3.4, printed p.190 / PDF p.210. FU-03 retains ownership of bounded-vector coordinates; FU-08 retains the full endpoint multiplier theorem. The present item proves their finite-coefficient dictionary and normal-action application, including the analytic-algebra continuity check. It does not close the spatial-derivative operator appearing after IX.3.5.

## A linking weight with a nonfaithful second corner

Keep \(N,\psi,L,H\) as above, and set

\[
\begin{gathered}
 R=\operatorname{End}_{N^{\mathrm{op}}}(L\oplus H),\\
 e+f=1,\qquad ef=0,\\
 eRe=\pi(N),\\
 M=fRf\\
  =\operatorname{End}_{N^{\mathrm{op}}}(H).
 \end{gathered}
\tag{LW.1}
\]

The off-diagonal corner \(fRe\) consists of the bounded maps \(L\to H\); \(eRf\) consists of the bounded maps \(H\to L\). Let \(\varphi\) be a normal semifinite weight on \(M\), with no faithfulness assumption, and let \(q=s(\varphi)\le f\). For positive \(X\in R\) define

\[
\begin{gathered}
 \rho(X)=\psi(eXe)+\varphi(fXf),\\
 \overline\varphi(X)=\varphi(fXf).
 \end{gathered}
\tag{LW.2}
\]

We identify \(eRe\) with \(N\) in evaluating \(\psi\). Both weights are normal and semifinite. The following proof establishes that assertion, all four GNS ranges, and both clauses of the source lemma at nonfaithful generality.

**A faithful completion, with the correct corners.** WS-06 says that \(\varphi(X)=\varphi(qXq)\) on \(M_+\) and that its restriction to \(qRq\) is faithful, normal and semifinite. Set \(g=f-q\). Choose a faithful normal semifinite weight \(\varphi_0\) on \((f-q)R(f-q)\), using WH-13, and put

\[
\begin{aligned}
 \Theta(X)={}&\psi(eXe)\\
            &+\varphi(qXq)\\
            &+\varphi_0(gXg).
 \end{aligned}
\tag{LW.3}
\]

Zero corners have their unique weight. Apply CW-06 twice to complementary projections and faithful corner weights. It proves that \(\Theta\) is faithful, normal and semifinite. Grouping its last two terms first makes \(e,f\) centralizer projections. Grouping its first and last terms on \((1-q)R(1-q)\) instead makes \(q\) a centralizer projection. Hence \(p=e+q\) also centralizes \(\Theta\). The argument does not apply a faithful-corner theorem directly to the possibly nonfaithful \(\varphi\).

For positive \(X\), compression gives

\[
\begin{gathered}
 \rho(X)=\Theta(pXp),\\
 \overline\varphi(X)=\Theta(qXq).
 \end{gathered}
\tag{LW.4}
\]

CW-05 and the full supported-GNS theorem CL-03 therefore prove normality, semifiniteness and the respective supports \(p,q\). Let \(E=L^2(R)\) be its canonical standard form, with conjugation \(J_R\), and let \(\Lambda_\Theta\) denote the standard GNS coordinates of \(\Theta\). CL-03 identifies the full GNS maps and their ranges as

\[
\begin{gathered}
 \eta_\rho(x)=\Lambda_\Theta(xp),\\
 x\in\mathfrak n_\rho,\qquad H_\rho=Ep,\\
 \eta_{\overline\varphi}(x)=\Lambda_\Theta(xq),\\
 x\in\mathfrak n_{\overline\varphi},\\
 H_{\overline\varphi}=Eq.
 \end{gathered}
\tag{LW.5}
\]

Here \(aEb\) means left multiplication by \(a\) and right multiplication by the projection \(b\), that is \(aJ_RbJ_RE\). Each domain statement and density assertion in (LW.5) holds on the whole finite left ideal. In particular, \(Ep\) and \(Eq\) are not replaced by the smaller faithful support-corner spaces \(pEp\) and \(qEq\).

**Four blocks and the original module.** The commuting left projections \(e,f\) and right projections \(e,q\) give an orthogonal decomposition. Arrange its blocks as follows, denoting the entries by \(H_{ij}\) in the displayed row and column order:

\[
\begin{pmatrix}
 eEe&eEq\\
 fEe&fEq
 \end{pmatrix}.
\tag{LW.6}
\]

The entries mean closures of \(\eta_\rho(eRe\cap\mathfrak n_\rho)\), \(\eta_\rho(eRf\cap\mathfrak n_\rho)\), \(\eta_\rho(fRe\cap\mathfrak n_\rho)\), and \(\eta_\rho(fRf\cap\mathfrak n_\rho)\), in that order. To check these closures, apply the corresponding bounded left and right projections to the dense GNS set in (LW.5). Centralizer right multiplication gives \(\Lambda_\Theta(y)e=\Lambda_\Theta(ye)\) and \(\Lambda_\Theta(y)q=\Lambda_\Theta(yq)\) on the full finite ideal, by CL-03/CZ-05. The projected elements belong to the displayed corner finite ideals; conversely each corner vector lies in that projection range.

FU-01, applied with the third summand zero, identifies \(eEe\) with the standard \(L\), and \(fEe\) with the whole original \(H\). Write these unitaries \(U_e:L\to eEe\) and \(U_H:H\to fEe\). The first preserves the corner standard form. Since \(e\) centralizes \(\Theta\), the modular corner theorem CZ-09 and standard-form comparison SE-03/10 give
\(U_e\Lambda_\psi(a)=\Lambda_\Theta(a)\) for every \(a\in\mathfrak n_\psi\). FU-01 defines \(U_H(T\zeta)=T U_e\zeta\) on a total set. In particular it preserves the left action of \(M\), as well as the right action of \(N\): check the left identity on \(T\zeta\) and extend by boundedness. For \(T=u\pi(a)\in\mathfrak n_\psi(H)\), FU-12 now gives

\[
\begin{aligned}
 U_H\eta_\psi^H(T)&=u\Lambda_\Theta(a)\\
                &=\Lambda_\Theta(T)\\
                &=\eta_\rho(T).
 \end{aligned}
\tag{LW.7}
\]

Thus the first column realizes the precise operator GNS map, not an unspecified Hilbert-space isomorphism. Its finite-coefficient domain is \(fRe\cap\mathfrak n_\rho=\mathfrak n_\psi(H)\), because \(T^*T\in eRe\). For \(y\in eRf\), its finite-coefficient condition is exactly \(\varphi(y^*y)<\infty\); no first-corner term occurs. For the second diagonal entry, the full GNS map of \(\varphi\) on \(M=fRf\) is \(y\mapsto\Lambda_\Theta(yq)\). Its range is dense in \(fEq\), by the same projected-density argument. Hence \(H_{22}\) is the full \(H_\varphi\), not merely \(qEq\).

**The second column is the lifted GNS representation.** For every \(x\in\mathfrak n_{\overline\varphi}\),

\[
\begin{gathered}
 xf\in\mathfrak n_\rho,\\
 \rho((xf)^*(xf))\\
      =\overline\varphi(x^*x),\\
 V\eta_{\overline\varphi}(x):=\eta_\rho(xf)\\
      =\Lambda_\Theta(xq).
 \end{gathered}
\tag{LW.8}
\]

The norm equality and polarization make \(V\) a well-defined isometry on the GNS quotient. The last formula gives dense range in \(Eq=H_{12}\oplus H_{22}\), by (LW.5); hence it extends onto that whole column. For every \(a\in R\), \((ax)f=a(xf)\), so \(V\) intertwines the full left \(R\)-action. This proves clause (i) without a symmetry assumption or an appeal to faithfulness of \(\varphi\).

**The upper second block is a conjugate module.** On a standard form, \(J_R(aEb)=bEa\) for projections. Since \(q\le f\),

\[
\begin{aligned}
 J_R(qH_{21})&=J_R(qEe)\\
             &=eEq\\
             &=H_{12}.
 \end{aligned}
\tag{LW.9}
\]

Consequently the linear unitary

\[
\begin{gathered}
 U:\overline{qH}\longrightarrow H_{12},\\
 U(C_{qH}\xi)\\
       =J_R U_H\xi.
 \end{gathered}
\tag{LW.10}
\]

identifies \(H_{12}\) with the conjugate of the supported module \(qH\). It is linear and unitary because it composes two antiunitaries with \(U_H\), and (LW.9) proves its onto assertion. Its precise algebras are \(N\) on the left and \(M_q=qMq\) on the right. For \(b\in N\), \(a\in M_q\), use the conjugate action from FU-01:

\[
\begin{gathered}
 b(C_{qH}\xi)a=C_{qH}(a^*\xi b^*),\\
 U\bigl(b(C_{qH}\xi)a\bigr)\\
       =J_R(a^*U_H\xi b^*)\\
       =b\,J_R U_H\xi\,a.
 \end{gathered}
\tag{LW.11}
\]

The last equality follows from the standard right action \(J_Ra^*J_R\) and commutation of left and right actions. Thus this is the required \(N\)-\(M_q\) bimodule unitary, proving clause (ii). All actions are the inherited normal unital corner actions, with corner units \(e,q\); kernels are permitted on either represented module.

The auxiliary choice \(\varphi_0\) changes neither statement nor GNS map. CL-03 proves independence of the faithful centralizing completion on every vector of the full supported domain in (LW.5). Canonical standard-form comparisons preserve \(J_R\), the left and right corner projections, and \(U_e,U_H\), by SE-10 and FU-01. They therefore preserve (LW.7–11). This is independence of the actual maps, not just equality of Hilbert-space dimensions.

**A nonfaithful example, with all four dimensions.** Let \(N=\mathbb C\), \(\psi(t)=t\) for \(t\ge0\), and \(H=\mathbb C^2\) with its scalar right action. Then \(R=M_3(\mathbb C)\), \(e=E_{11}\), \(f=E_{22}+E_{33}\), and \(M=fRf\). Take \(\varphi(y)=2y_{22}\) on \(M_+\), so \(q=E_{22}\). A completion is \(\Theta(X)=\operatorname{Tr}(DX)\), with \(D=\operatorname{diag}(1,2,3)\). In \(E=\mathrm{HS}_3\),

\[
\begin{gathered}
 \eta_\rho(X)\\
      =X\operatorname{diag}(1,\sqrt2,0),\\
 \eta_{\overline\varphi}(X)=\sqrt2XE_{22}.
 \end{gathered}
\tag{LW.12}
\]

Every matrix belongs to these finite ideals. The first column has basis \(E_{11},E_{21},E_{31}\), and the second has basis \(E_{12},E_{22},E_{32}\). For \(i,j\in\{1,2\}\), their dimensions are

\[
\bigl(\dim H_{ij}\bigr)
       =\begin{pmatrix}1&1\\2&2\end{pmatrix}.
\tag{LW.13}
\]

Thus \(H_\rho\) has dimension six, the lifted \(H_{\overline\varphi}\) dimension three, and the full \(H_\varphi\) dimension two. Its faithful support corner has only the one-dimensional space \(qEq=\mathbb C E_{22}\). The supported \(qH\) corresponds to \(\mathbb C E_{21}\); \(J_R\xi=\xi^*\) takes it to \(\mathbb C E_{12}=H_{12}\). Formula (LW.10) makes this antiunitary into a linear map on the conjugate space. Changing the last positive entry of \(D\) does not change either map in (LW.12), checking completion independence concretely.

**The zero-weight endpoint.** In the same example set \(\varphi=0\), hence \(q=0\). Then \(\eta_\rho(X)=XE_{11}\), its GNS space is the three-dimensional first column, and \(H_{21}=H\) still has dimension two. Both second-column spaces and the lifted GNS representation are zero, and (LW.10) is the unique unitary between zero spaces. A zero second weight therefore does not erase the original right module. If \(H=0\) instead, all its corners and their maps have their literal zero-space meaning. These cases also show why the full first column cannot be compressed to \(qH\).

The proof corresponds to the complete two-clause Lemma IX.3.5 of Takesaki II, printed pp.190–191 / PDF pp.210–211. In its nonfaithful paragraph on p.191, the complementary support is printed as \(f-q\le e\) and the auxiliary lift uses \(\varphi_1(eXe)\); the types in (LW.1) require \(f-q\le f\) and a second-corner compression instead. Its last two proof-clause labels are interchanged. Equations (LW.3), (LW.8) and (LW.9–11) supply the correctly typed completion and the two correctly assigned proofs. These are editorial and domain corrections, with no claim of novelty. The subsequent closed conjugate-linear spatial-derivative operator and Definition IX.3.6 remain separate obligations.

The new FU-12–13 exposition and solved examples are by GPT-6.1 Sol (OpenAI), Ultra, October 2026, CC0-1.0. The earlier lesson text and its marked adapted components retain their existing licences. No protected source page or source proof is reproduced.
