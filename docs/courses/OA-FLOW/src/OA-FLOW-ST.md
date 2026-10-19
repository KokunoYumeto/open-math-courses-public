# Faithful normal states: GNS normality and the modular application

*Proof and exposition by GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights in this exposition.*

This lesson develops the faithful-state GNS construction and its modular application in L159. A normal functional here means a continuous linear functional for the concrete ultraweak vector-series topology, as in SF-2. A faithful normal state belongs to the positive cone of that predual and has value one at the identity. The argument uses this continuity assumption; it does not establish an order-normality theorem for arbitrary weights.

The precise earlier inputs are [CF Section 1](OA-FLOW-CF.md#OA-FLOW.CF.1), [CF Section 4](OA-FLOW-CF.md#OA-FLOW.CF.4), [CF Sections 6–7](OA-FLOW-CF.md#OA-FLOW.CF.6), [GNS Sections 2–5](OA-FLOW-GNS.md#gns-positive-form), [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0)/[SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0), [SF-2](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-2), and [CP-01–06](OA-FLOW-CP.md#oa-flow.cp.1). The six predual results are proved in CP, using the Hilbert-space and Hahn–Banach results in CF and SF. Support results and arbitrary-weight theorems are not prerequisites.

The predual facts from CP used here are as follows: the completion of the projective-norm algebraic tensor \(H\otimes\overline H\) has dual \(B(H)\), via vector pairings; every completed tensor is an absolutely summable pure-tensor series, whose factors may be balanced into two square-summable sequences. Quotienting by the annihilator of a concrete von Neumann algebra \(M\) gives a Banach space \(M_*\), isometric to the vector-series functionals in \(M^*\), with \(M=(M_*)^*\). In particular \(M_*\) is norm closed in \(M^*\). These statements are proved, including tensor norm, completion, quotient and annihilator arguments, in CP-01–06.

The analytic results used below are [BD](OA-FLOW-BD.md#oa-flow.bd.1), [CI](OA-FLOW-CI.md#oa-flow.ci.1), and [HA-R](OA-FLOW-HA-R.md#oa-flow.ha-r.1). The final full-algebra application uses [WH-04 Sections 2–4](OA-FLOW-WH04.md#oa-flow.wh04.2) and [MF-06's general Hilbert-algebra proof](OA-FLOW-MF06.md#oa-flow.mf06.8). Their arbitrary-weight applications are not premises of this route.
The coefficient/GNS-normality argument used below also appears earlier as [ST-3 coefficient proof](OA-FLOW-STC.md#oa-flow.st.coefficient), assuming an ultraweak vector-series state and no modular input. ST-3 combines that argument with the modular application. The earlier topology conclusions used below are [ST-1](OA-FLOW-ST12.md#oa-flow.st.1) and [ST-2](OA-FLOW-ST12.md#oa-flow.st.2).

<a id="oa-flow.st.3"></a>

## ST-3. A faithful normal state's GNS representation meets that hypothesis

Let \(M\subseteq B(H)\) be a nonzero concrete von Neumann algebra and let \(\varphi\in M_*^+\) be a faithful state. GNS Sections 2–5 construct the Hilbert space \(K\), contractive representation \(\pi\), and cyclic vector \(\xi\), with
\[
\langle\pi(x)\pi(a)\xi,\pi(b)\xi\rangle=\varphi(b^*xa).
\tag{ST4}
\]
For fixed \(a,b\), the right side is normal: in any vector-series expression for \(\varphi\), replace its first vectors by \(a u_j\) and its second by \(b v_j\). The new vector sequences are square summable. Arbitrary pairs \(\eta,\zeta\in K\) are norm limits of cyclic-domain pairs. Contractivity gives the uniform functional-norm estimate
\[
\bigl|\langle\pi(x)\eta,\zeta\rangle-
\langle\pi(x)\eta_0,\zeta_0\rangle\bigr|
\leq\|x\|\bigl(\|\eta-\eta_0\|\|\zeta\|
+\|\eta_0\|\|\zeta-\zeta_0\|\bigr).
\tag{ST5}
\]
Since \(M_*\) is norm closed, every vector coefficient of \(\pi\) pulls back to \(M_*\). A square-summable pair of vector sequences in \(K\) gives a norm-convergent sum of those pulled-back functionals, because its tail is bounded in functional norm by the product of the two square-sum tails. Again norm closure puts the sum in \(M_*\). This proves ultraweak continuity of \(\pi\) for the full vector-series topology, without converting order normality through NW or NP.

The representation is faithful: \(\pi(x)=0\) implies \(\varphi(x^*x)=\|\pi(x)\xi\|^2=0\), hence \(x=0\). It is unital since \(\pi(1)\) fixes the dense cyclic domain. ST-2 applies. Its image is a concrete von Neumann algebra, and \(\xi\) is separating for it because \(\pi(x)\xi=0\) gives the same faithful-state test.

In particular the vector algebra
\(\mathcal A=\{\pi(x)\xi:x\in M\}\), with product inherited from \(M\) and involution \(\pi(x)\xi\mapsto\pi(x^*)\xi\), is a left Hilbert algebra. Separatingness makes the definitions unambiguous; its left multipliers are bounded, its inner-product adjoint identity is immediate, and \(\mathcal A^2=\mathcal A\) because the unit is present. CI-4 proves closability by the dense commutant orbit. HA-R and the separately reviewed WH-04 then give its full second dual with the identical closed involution, on the identical Hilbert space.

MF-06's general full-Hilbert-algebra proof can therefore be applied with CI/HA-R/BD in place of its affected TC/HA/RD premises. It returns the modular commutant and automorphism conclusions for the original \(\pi(M)\) and this same \(S\). ST-2 transports the bounded algebra and its normal topology back to \(M\). This is the faithful-normal-state route needed in L159, preserving all its separable-predual cases; ST-1–3 themselves require no separability.

<a id="oa-flow.st.4"></a>

## ST-4. From states to arbitrary weights

For a faithful normal state, the cyclic vector supplies the normality and faithfulness tests in ST-3. The preceding concrete predual construction supplies the topology of the representation.

For a faithful normal semifinite weight, [GW-1–5](OA-FLOW-GW.md#oa-flow.gw.1) and [NF-5](OA-FLOW-NF.md#oa-flow.nf.5) instead use finite ideals, GNS vectors and finite-domain cutoffs. [WR-3](OA-FLOW-WR.md#wr-3) proves closability of the finite-star involution, [WR-4](OA-FLOW-WR.md#wr-4) proves fullness, [WR-5](OA-FLOW-WR.md#wr-5) recovers the weight, and [WR-6](OA-FLOW-WR.md#wr-6) constructs its opposite weight. [WF](OA-FLOW-WF.md#oa-flow.wf.4) proves the forward construction with its full GNS and involution domains. The [normality theorem for extended-valued weights](OA-FLOW-EW.md#ew-5) applies without faithfulness or semifiniteness; [MW-4](OA-FLOW-MW.md#mw-4) identifies the faithful modular action. Each construction retains its stated hypotheses.
