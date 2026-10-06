# Faithful normal states: GNS normality and the modular application

*Fresh local proof by GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights in this exposition.*

This bridge proves the faithful-state route needed by L159 without the inherited arbitrary-weight normality theorem. A normal functional here means a continuous linear functional for the concrete ultraweak vector-series topology, as in SF-2. A faithful normal state belongs to the positive cone of that predual and has value one at the identity. We do not replace an order-normal arbitrary-weight theorem by this convention.

The precise earlier inputs are [CF Section 1](OA-FLOW-CF.md#OA-FLOW.CF.1), [CF Section 4](OA-FLOW-CF.md#OA-FLOW.CF.4), [CF Sections 6–7](OA-FLOW-CF.md#OA-FLOW.CF.6), [GNS Sections 2–5](OA-FLOW-GNS.md#gns-positive-form), [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0)/[SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0), [SF-2](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-2), and [CP-01–06](OA-FLOW-CP.md#oa-flow.cp.1). Those six predual proof bodies are earlier in this reader. Their Hilbert and Hahn–Banach inputs are the displayed fresh CF/SF proofs. No support or arbitrary-weight descendant is an input.

For clarity, the entire CP contract used here is this: the completion of the projective-norm algebraic tensor \(H\otimes\overline H\) has dual \(B(H)\), via vector pairings; every completed tensor is an absolutely summable pure-tensor series, whose factors may be balanced into two square-summable sequences. Quotienting by the annihilator of a concrete von Neumann algebra \(M\) gives a Banach space \(M_*\), isometric to the vector-series functionals in \(M^*\), with \(M=(M_*)^*\). In particular \(M_*\) is norm closed in \(M^*\). These statements are proved, including tensor norm, completion, quotient and annihilator arguments, in the exact CP range just identified; a source-history judgment is separate from this mathematical proof binding.

The new local analytic providers used below are [BD](OA-FLOW-BD.md#oa-flow.bd.1), [CI](OA-FLOW-CI.md#oa-flow.ci.1), and [HA-R](OA-FLOW-HA-R.md#oa-flow.ha-r.1). The final full-algebra application uses [WH-04 Sections 2–4](OA-FLOW-WH04.md#oa-flow.wh04.2) and [MF-06's general Hilbert-algebra proof](OA-FLOW-MF06.md#oa-flow.mf06.2), at the replaced foundation bindings specified here. Their arbitrary-weight applications are not premises of this route.
The coefficient/GNS-normality argument used below also appears earlier as [ST-3 coefficient proof](OA-FLOW-STC.md#oa-flow.st.coefficient), with the already ultraweak vector-series state premise and no modular input. The full original ST-3 scope and its modular application remain here. The earlier topology conclusions used below are [ST-1](OA-FLOW-ST12.md#oa-flow.st.1) and [ST-2](OA-FLOW-ST12.md#oa-flow.st.2).

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

## ST-4. Exact remaining distinctions

This route uses the actual free-developed CP-01–06 construction at newly specified Hilbert/Hahn–Banach inputs, not its support or arbitrary-weight descendants. It still requires those exact CP proof bodies to be admitted before the reader invokes them. Their earlier source records support their independently written tensor construction; a review receipt or current bibliography alone is not historical proof of every ancestor.

The arbitrary given-weight finite ideals, GNS construction, cutoffs, density and normal faithful representation now have the earlier GW/NF proof bodies. Its finite-star involution closability and full/reverse/opposite-weight correspondence now have the earlier [WR-3](OA-FLOW-WR.md#wr-3)–[WR-6](OA-FLOW-WR.md#wr-6) faithful n.s.f. proofs. WF proves the full forward algebra-to-weight construction and its GNS/involution-domain transport. The earlier [extended-valued normality theorem](OA-FLOW-EW.md#ew-5) covers every weight, and [MW](OA-FLOW-MW.md#mw-4) supplies the faithful modular opposite formula. Broader nonfaithful statements retain their precise scopes.