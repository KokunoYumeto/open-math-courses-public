# A faithful vector-series state has an ultraweak GNS representation

Original reviewed ST-3 coefficient argument, placed before the order-normal functional proof. The premise is a state already belonging to the concrete vector-series predual. Neither an order-normality equivalence nor a modular theorem is an input. Original CC0 component expression and GPT-6 Astra (OpenAI), Ultra credit retained.

The actual earlier proofs are [GNS Sections 2–5](OA-FLOW-GNS.md#gns-positive-form), [CP01–06](OA-FLOW-CP.md#oa-flow.cp.1), [ST-2](OA-FLOW-ST12.md#oa-flow.st.2), [CF Sections 6–7](OA-FLOW-CF.md#OA-FLOW.CF.6) and [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0)/[SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0). The complete later ST-3 modular application remains in its original reader.

<a id="oa-flow.st.coefficient"></a>

## ST-C. A faithful normal state's GNS representation meets that hypothesis

Let \(M\subseteq B(H)\) be a nonzero concrete von Neumann algebra and let \(\varphi\in M_*^+\) be a faithful state. [GNS Sections 2–5](OA-FLOW-GNS.md#gns-positive-form) construct the Hilbert space \(K\), contractive representation \(\pi\), and cyclic vector \(\xi\), with
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

The representation is faithful: \(\pi(x)=0\) implies \(\varphi(x^*x)=\|\pi(x)\xi\|^2=0\), hence \(x=0\). It is unital since \(\pi(1)\) fixes the dense cyclic domain. [ST-2](OA-FLOW-ST12.md#oa-flow.st.2) applies. Its image is a concrete von Neumann algebra, and \(\xi\) is separating for it because \(\pi(x)\xi=0\) gives the same faithful-state test.
