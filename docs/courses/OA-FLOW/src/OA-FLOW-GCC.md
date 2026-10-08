
<a id="oa-flow.gcc.0"></a><a id="gcc-opening-context"></a>

# Connes spectrum through fixed corners

The ordinary spectrum of an action sees every frequency occurring anywhere in the algebra. The Connes spectrum keeps only frequencies that survive every nonzero corner cut out by a fixed projection. This lesson defines that intersection, proves that central supports suffice, and shows that equivalent fixed projections give reduced actions with the same Connes spectrum.

The proof is organized around spectral subspaces rather than an unproved corner slogan. Its key construction localizes a partial isometry in frequency, takes the join of the right supports of its orbit, and sandwiches a spectral element between two orbit translates.

*Restored local proof, 5 October 2026. Original historical arguments and alternatives are retained. Spot-checked in a separate AI session. Original expression and new illustration are CC0-1.0 to the extent of rights held; prerequisite component terms remain their own.*

<a id="oa-flow.gcc.inputs"></a>

<a id="gcc-inputs"></a>
## Earlier tools and the frequency convention

The group and Hilbert space are arbitrary; no countability, separability or factor assumption is imposed. The actual normal integrated action is [AT5](OA-FLOW-AT.md#oa-flow.at.5). Its restriction to any fixed corner uses exactly the same scalar integrals. The complete spectral tools are [GL0–3](OA-FLOW-GL.md#gl-0), [GL6–7](OA-FLOW-GL.md#gl-6), the compact local Fourier plateaus of [LF1](OA-FLOW-LF.md#lf-1), and the fixed/eigenoperator identification of [SS3](OA-FLOW-SS.md#ss-3). Bounded supports and arbitrary joins are constructed in [PC1](OA-FLOW-PC.md#oa-flow.projection.pc1); [SF0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0) proves the commutant-unitary test. The local compact-neighbourhood arguments use [H0](OA-FLOW-TOPOLOGY.md#l138-h0).

Use the negative transform \(\widehat k(\gamma)=\int_G k(t)\overline{\gamma(t)}\,dm(t)\) and \(A(H)=\{\widehat k:k\in L^1(G)\}\), with \(\|\widehat k\|_A=\|k\|_1\). In the retained formulas \(\alpha_g=T_k\) when \(g=\widehat k\). Fourier injectivity is the earlier scalar theorem bound through LF/GL. Thus \(\alpha_t(x)=\overline{\gamma(t)}x\) has label \(\gamma\). This fixes all signs while leaving the historical equations (C1)–(C28) unchanged. The existing real-line positive-transform proof and alternative support sandwich in [CS0–3](OA-FLOW-CS.md#oa-flow.cs.0) remain earlier results; reflection of real labels compares the two conventions. The general-group proof below does not replace that specialization.

For \(J\subset A(H)\), write \(h(J)=\{\gamma\in H:g(\gamma)=0\text{ for every }g\in J\}\). Here \(\operatorname{Sp}_\alpha(x)=h(\{g:\alpha_g(x)=0\})\), \(\operatorname{Sp}(\alpha)=h(\{g:\alpha_g=0\})\), and \(M_\alpha(E)=\{x:\operatorname{Sp}_\alpha(x)\subset E\}\). These are exactly the GL hull spectra, with capitalized notation; no second spectrum or support convention is introduced.

Every use of a product spectrum below is [GL6](OA-FLOW-GL.md#gl-6), whose general bound has a closure. A fixed multiplier contributes only the compact set \(\{0\}\); a compact set plus a closed set is closed. In (C28) all three sets are compact, so their sum is compact and closed. These are the precise reasons the displayed formulas need no extra closure.

<a id="oa-flow.gcc.setting"></a>

<a id="gcc-setting"></a>
## Fixed projections produce reduced actions

Let \(G\) be a locally compact abelian group, let \(H=\widehat G\), and let

<a id="equation-c1"></a>

$$\alpha:G\longrightarrow\operatorname{Aut}(M) \tag{C1}$$

be a point-ultraweakly continuous action on a nonzero von Neumann algebra. Write

<a id="equation-c2"></a>

$$N=M^\alpha=\{x\in M:\alpha_t(x)=x\text{ for every }t\in G\}. \tag{C2}$$

If \(e\in\operatorname{Proj}(N)\), then \(eMe\) is globally invariant and

<a id="equation-c3"></a>

$$\alpha_t^e(x)=\alpha_t(x),\qquad x\in eMe, \tag{C3}$$

defines the **reduced action**. Its fixed algebra is

$$(eMe)^{\alpha^e}=eNe.$$

The Fourier filters of the reduced action are the restrictions of the original filters:

$$(\alpha^e)_f(x)=\alpha_f(x),\qquad x\in eMe,\quad f\in A(H).$$

Indeed \(e\) is fixed, so weak-star integration gives
\(\alpha_f(exe)=e\alpha_f(x)e\). Consequently the ambient and reduced vector spectra agree for elements of the corner, and for every closed \(E\subset H\),

<a id="equation-c4"></a>

$$(eMe)_{\alpha^e}(E)=M_\alpha(E)\cap eMe. \tag{C4}$$

Here the corner is a concrete von Neumann algebra on \(e\mathcal H\), as proved in PC1. Normal vector-series tests on that space extend to normal tests on \(M\) by viewing their vectors in \(\mathcal H\); [CP6](OA-FLOW-CP.md#oa-flow.cp.6) supplies precisely these concrete predual tests. Fixed multiplication is normal: testing \(azb\) replaces the square-summable vectors \((\xi_n,\eta_n)\) by \((b\xi_n,a^*\eta_n)\), which remain square summable. Compression uses the same calculation with \(a=b=e\). Thus the restricted action has the same normality and point-ultraweak continuity, and AT5 applies to it. Its scalar integral agrees with the ambient integral on every such test. The annihilator ideals are consequently identical for an element of the corner, which proves the exact spectral equality (C4), not just one inclusion.

We will repeatedly use the following local detection criterion. If \(\beta\) is an action on a nonzero von Neumann algebra \(P\), then

<a id="equation-c5"></a>

$$p\in\operatorname{Sp}(\beta)
\quad\Longleftrightarrow\quad
\text{for every open }O\ni p\text{ there is }0\ne x\in P
\text{ with }\operatorname{Sp}_\beta(x)\subset O. \tag{C5}$$

For the forward implication, choose \(g\in A_c(H)\) with \(g(p)\ne0\) and \(\operatorname{supp}g\subset O\). Since \(p\) lies in the hull of the action annihilator, \(\beta_g\ne0\); a nonzero \(\beta_g(y)\) has spectrum in \(\operatorname{supp}g\). Conversely, if \(p\notin\operatorname{Sp}(\beta)\), choose \(O\) disjoint from that closed spectrum. Every vector spectrum lies in \(\operatorname{Sp}(\beta)\), so a vector whose spectrum also lies in \(O\) has empty spectrum and is zero.

<a id="oa-flow.gcc.definition"></a>

<a id="gcc-definition"></a>
## The intersection that defines the Connes spectrum

The **Connes spectrum**, also called the essential spectrum, is

<a id="equation-c6"></a>

$$\boxed{
\Gamma(\alpha)
=
\bigcap_{\substack{e\in\operatorname{Proj}(N)\\e\ne0}}
\operatorname{Sp}(\alpha^e).} \tag{C6}$$

Thus \(p\in\Gamma(\alpha)\) precisely when every nonzero fixed corner detects \(p\). The definition immediately gives

<a id="equation-c7"></a>

$$\Gamma(\alpha)\subset\operatorname{Sp}(\alpha), \tag{C7}$$

because \(1\in\operatorname{Proj}(N)\) and \(\alpha^1=\alpha\). Each action spectrum is closed, so \(\Gamma(\alpha)\) is closed. The deeper facts that it is a subgroup and that it identifies a kernel on the center of a crossed product require later arguments.

The distinction from the ordinary spectrum is already visible in \(M_2(\mathbb C)\). Let

<a id="equation-c8"></a>

$$\alpha_t=\operatorname{Ad}
\begin{pmatrix}1&0\\0&e^{it}\end{pmatrix},
\qquad t\in\mathbb R. \tag{C8}$$

Then \(\operatorname{Sp}(\alpha)=\{-1,0,1\}\), while each diagonal rank-one fixed corner is scalar with trivial action. Hence

<a id="equation-c9"></a>

$$\Gamma(\alpha)=\{0\}. \tag{C9}$$

For completeness in (C8)–(C9), the matrix units \(e_{11},e_{22},e_{12},e_{21}\) have negative spectral labels \(0,0,1,-1\), respectively, by their explicit eigenphases and SS3. They span \(M_2\), so GL2's finite-sum rule and GL7's union formula give the stated ordinary action spectrum. Every nonzero fixed corner has its fixed unit, which makes zero belong to its action spectrum. The scalar \(e_{11}\)-corner has trivial action and spectrum exactly \(\{0\}\). Thus the Connes intersection both contains and is contained in \(\{0\}\), proving (C9).

For a zero corner the action spectrum is empty: every Fourier filter is zero and LF1 separates each character from the hull of the entire Fourier algebra. The literal intersection defining its Connes spectrum is an empty intersection, hence \(H\). This convention is used only for the zero–zero case of (C18). Statements (C5), (C7), (C9) and the factor conclusion concern nonzero algebras as stipulated. If equivalent projections have one zero member then both are zero, and (C18) is immediately an equality of the two empty intersections.

For a nonzero fixed corner its unit has spectrum \(\{0\}\) by SS3 (or the direct scalar filter computation). Hence every corner action spectrum contains zero. Adjoint reflection and GL7's union formula also make each corner spectrum symmetric. Consequently the intersection (C6) is closed, symmetric, contains zero and satisfies (C7). No subgroup or crossed-product-center theorem is being inferred here.

<a id="oa-flow.gcc.tools"></a>

<a id="gcc-tools"></a>
## Supports and joins used by the transport

Write \(s_r(a)\) for the projection onto \(\overline{a^*\mathcal H}=(\ker a)^\perp\). PC1 constructs this projection in \(M\), including \(a=0\). It is the least projection \(q\) with \(aq=a\): that identity makes \(a\) vanish on \((1-q)\mathcal H\), so \(\overline{a^*\mathcal H}\subset q\mathcal H\). Conversely \(a\,s_r(a)=a\) by the kernel decomposition. For bounded \(a,b\), consequently

<a id="equation-gcc1"></a>

\[
 ab=0\ \Longleftrightarrow\ s_r(a)b=0,\qquad
 ba^*=0\ \Longleftrightarrow\ b\,s_r(a)=0.
\tag{GCC1}
\]

For the first equivalence, \(ab=0\) puts \(b\mathcal H\) in \(\ker a\); the converse uses \(a=a\,s_r(a)\). For the second, \(ba^*=0\) means that \(b\) vanishes on \(a^*\mathcal H\), hence on its closure; the converse uses \(s_r(a)a^*=a^*\).

For any family of projections \((q_i)\), PC1's join \(q=\bigvee_iq_i\) projects onto the closed span of their ranges. Thus

<a id="equation-gcc2"></a>

\[
 q_i b=0\ (\text{all }i)\Rightarrow qb=0,\qquad
 bq_i=0\ (\text{all }i)\Rightarrow bq=0.
\tag{GCC2}
\]
In the first implication the range of \(b\) is perpendicular to every range of \(q_i\); in the second \(b\) vanishes on their span and its closure. Neither argument requires a countable family.

An automorphism preserves projections, their order and least upper bounds by applying its inverse. The least-projection characterization above therefore gives \(s_r(\alpha_t(a))=\alpha_t(s_r(a))\). In particular translating an orbit permutes the joined projections in (C24). This supplies its invariance and the two genuine nonvanishing steps in (C27), without asserting that \(s_r(x)\) itself is fixed.

We will also use the central-support orbit formula. For \(e\in N=M^\alpha\), form \(c=\bigvee_{u\in\mathcal U(N)}ueu^*\) using the projection lattice of \(M\). Every summand is fixed, so preservation of joins gives \(c\in N\). Conjugation by any unitary of \(N\) permutes the family, hence \(c\) commutes with every such unitary. For bounded self-adjoint \(b\in N\), its norm exponential \(e^{itb}\) is in \(\mathcal U(N)\); the exponential and norm differentiation are the SF0 proof. Differentiating commutation at zero gives \(cb=bc\). Self-adjoint decomposition gives commutation with every element of \(N\). Thus \(c\in Z(N)\) and \(c\ge e\). Any central projection of \(N\) dominating \(e\) dominates every \(ueu^*\), hence dominates their join. This proves (C10) as the least central support, with no imported comparison theorem.

<a id="oa-flow.gcc.equivalence"></a>

<a id="gcc-equivalence"></a>
## Equivalent fixed corners have the same Connes spectrum

Let \(e,f\in\operatorname{Proj}(N)\) be Murray--von Neumann equivalent in \(M\). Choose \(u\in M\) with

<a id="equation-c17"></a>

$$u^*u=e,\qquad uu^*=f. \tag{C17}$$

We prove

<a id="equation-c18"></a>

$$\boxed{\Gamma(\alpha^e)=\Gamma(\alpha^f).} \tag{C18}$$

It is enough to prove the forward inclusion. Fix \(p\in\Gamma(\alpha^e)\), a nonzero projection

<a id="equation-c19"></a>

$$f_1\in\operatorname{Proj}\bigl((fMf)^{\alpha^f}\bigr)
=\operatorname{Proj}(fNf), \tag{C19}$$

and an open neighborhood \(O\) of \(p\). Choose open neighborhoods \(V\ni p\) and \(W\ni0\), with compact closures after shrinking, such that

<a id="equation-c20"></a>

$$\overline V+W\subset O. \tag{C20}$$

The element \(f_1u\) is nonzero because
\((f_1u)(f_1u)^*=f_1\). Its vector spectrum is therefore nonempty. Choose

$$q\in\operatorname{Sp}_\alpha(f_1u)$$

and an open neighborhood \(U_1\ni q\) satisfying

<a id="equation-c21"></a>

$$\overline{U_1}-\overline{U_1}\subset W. \tag{C21}$$

Take \(g\in A_c(H)\) with \(\operatorname{supp}g\subset U_1\) and \(g(q)\ne0\). Since \(q\) lies in the hull of the annihilator of \(f_1u\),

<a id="equation-c22"></a>

$$x=\alpha_g(f_1u)=f_1\alpha_g(u)\ne0. \tag{C22}$$

Moreover

<a id="equation-c23"></a>

$$f_1x=x=xe,\qquad
\operatorname{Sp}_\alpha(x)\subset\overline{U_1}. \tag{C23}$$

The shrinking used here is valid for arbitrary \(H\). At \((p,0)\), continuity of addition gives \(V_0\ni p\) and \(W_0\ni0\) with \(V_0+W_0\subset O\). H0 shrinks \(V\) with compact closure inside \(V_0\), and shrinks \(W\) inside \(W_0\). At \((q,q)\), continuity of subtraction and compact shrinking give \(U_1\ni q\) with compact closure and \(\overline{U_1}-\overline{U_1}\subset W\). These are finite neighbourhood choices, not a sequence of approximations to the group. LF1 supplies \(g\) with compact support inside \(U_1\), equal to one near \(q\). GL3's lower filter inclusion makes (C22) nonzero.

Let \(s_r(a)\) denote the right support of \(a\), and form the orbit-support join

<a id="equation-c24"></a>

$$e_1=\bigvee_{t\in G}s_r(\alpha_t(x)). \tag{C24}$$

Every term is at most \(e\), the join is nonzero, and translating the index set leaves it unchanged. Thus

<a id="equation-c25"></a>

$$0\ne e_1\le e,\qquad e_1\in N. \tag{C25}$$

Because \(p\in\Gamma(\alpha^e)\), it belongs to
\(\operatorname{Sp}(\alpha^{e_1})\). Criterion (C5) supplies

<a id="equation-c26"></a>

$$0\ne y\in e_1Me_1,\qquad
\operatorname{Sp}_\alpha(y)\subset\overline V. \tag{C26}$$

The definition of \(e_1\) gives \(t_1,t_2\in G\) such that

<a id="equation-c27"></a>

$$z=\alpha_{t_1}(x)y\alpha_{t_2}(x)^*\ne0. \tag{C27}$$

Here is the nonvanishing argument. If \(\alpha_t(x)y=0\) for every \(t\), then
\(s_r(\alpha_t(x))y=0\) for every \(t\), so \(e_1y=0\), a contradiction. After choosing \(t_1\) with \(\alpha_{t_1}(x)y\ne0\), if every product in (C27) vanished, the same support-join argument on the right would give
\(\alpha_{t_1}(x)y e_1=0\), again a contradiction.

The support relations in (C23)--(C25) put \(z\) in \(f_1Mf_1\). Orbit invariance, adjoint reflection, and the product-spectrum theorem give

<a id="equation-c28"></a>

$$\begin{aligned}
\operatorname{Sp}_\alpha(z)
&\subset
\overline{U_1}+\overline V-\overline{U_1}\\
&\subset \overline V+W
\subset O.
\end{aligned} \tag{C28}$$

Thus every neighborhood \(O\ni p\) contains the spectrum of a nonzero element of the \(f_1\)-corner. By (C5),
\(p\in\operatorname{Sp}(\alpha^{f_1})\). Since \(f_1\) was arbitrary,
\(p\in\Gamma(\alpha^f)\). Replacing \(u\) by \(u^*\) proves the reverse inclusion and hence (C18).

**Problem.** Why is the orbit-support join in (C24) needed instead of the right support of \(x\) alone?

**Solution.** The right support of \(x\) need not be fixed, so it need not be an admissible projection in the intersection defining \(\Gamma(\alpha^e)\). Taking the join of all its translates makes the projection invariant. It is also the smallest invariant projection dominating \(s_r(x)\), and the two support-join contradictions used in (C27) depend on the entire family of translates. \(\square\)

<a id="oa-flow.gcc.central"></a>

<a id="gcc-central"></a>
## Central support preserves every closed spectral test

For \(e\in\operatorname{Proj}(N)\), let \(c_N(e)\) be its central support in \(N\). The unitary-orbit formula is

<a id="equation-c10"></a>

$$c_N(e)=\bigvee_{u\in\mathcal U(N)}ueu^*. \tag{C10}$$

Put \(c=c_N(e)\). For every closed \(E\subset H\),

<a id="equation-c11"></a>

$$M_\alpha(E)\cap eMe\ne\{0\}
\quad\Longleftrightarrow\quad
M_\alpha(E)\cap cMc\ne\{0\}. \tag{C11}$$

Only the reverse implication needs proof. Take \(0\ne x\in M_\alpha(E)\cap cMc\). If

<a id="equation-c12"></a>

$$ueu^*xvev^*=0
\qquad(u,v\in\mathcal U(N)), \tag{C12}$$

then, for fixed \(v\), the join formula (C10) gives \(cxvev^*=0\). Taking the join over \(v\) then gives \(cxc=0\), contrary to \(x=cxc\ne0\). Thus some \(u,v\in\mathcal U(N)\) make the expression in (C12) nonzero. Multiplying by \(u^*\) on the left and \(v\) on the right shows that

<a id="equation-c13"></a>

$$0\ne y=eu^*xve\in eMe. \tag{C13}$$

The factors \(u^*,v\) are fixed by the action and therefore have frequency zero. The spectral product theorem gives \(y\in M_\alpha(E)\), proving (C11).

Applying (C11) to arbitrarily small closed neighborhoods and using (C5) yields

<a id="equation-c14"></a>

$$\operatorname{Sp}(\alpha^e)
=\operatorname{Sp}\!\left(\alpha^{c_N(e)}\right). \tag{C14}$$

This equality concerns the action spectra of the two corners. It does not assert that \(eMe\) and \(c_N(e)Mc_N(e)\) are equal.

For precision in (C14), if a point is detected in the \(c\)-corner, each open neighbourhood admits by (C5) a nonzero element with compact spectrum \(K\) inside that neighbourhood. Apply (C11) to the closed set \(K\), then (C5) in the \(e\)-corner. This proves one inclusion. The reverse inclusion follows either the same detection test or the fact that the \(e\)-corner is contained in the \(c\)-corner and has identical restricted filters. If \(e=0\), then \(c=0\) and both action spectra are empty.

<a id="oa-flow.gcc.intersection"></a>

<a id="gcc-intersection"></a>
## Central fixed corners suffice

Every \(c_N(e)\) is a nonzero projection in \(Z(N)\) when \(e\ne0\). Formula (C14) therefore reduces the defining intersection to central fixed corners:

<a id="equation-c15"></a>

$$\boxed{
\Gamma(\alpha)
=
\bigcap_{\substack{z\in\operatorname{Proj}(Z(N))\\z\ne0}}
\operatorname{Sp}(\alpha^z).} \tag{C15}$$

One inclusion follows because central projections are among all fixed projections. For the other, take \(p\) in the right side and an arbitrary nonzero \(e\in\operatorname{Proj}(N)\). Then \(p\in\operatorname{Sp}(\alpha^{c_N(e)})\), and (C14) puts \(p\) in \(\operatorname{Sp}(\alpha^e)\).

In particular, if the fixed algebra \(N=M^\alpha\) is a factor, its only nonzero central projection is \(1\), and hence

<a id="equation-c16"></a>

$$\boxed{\Gamma(\alpha)=\operatorname{Sp}(\alpha).} \tag{C16}$$

The factor condition is on the fixed algebra. Example (C8) shows why it cannot simply be omitted.

<a id="oa-flow.gcc.model"></a>

<a id="gcc-model"></a>
## An orbit support that actually grows

The rank-one example (C8)–(C9) remains the distinction between ordinary and Connes spectra. Here is a separate exact model of why the orbit join in (C24) is necessary. Keep that action on \(M_2\), let \(e=f=1\), \(f_1=e_{11}\), and set

<a id="equation-gcc3"></a>

\[
 u=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
 x=f_1u=2^{-1/2}(e_{11}+e_{12}),\qquad y=e_{22}.
\tag{GCC3}
\]
The matrix \(u\) is a unitary, implementing (C17). The negative-label spectrum of \(x\) is exactly \(\{0,1\}\): its two summands have those eigenlabels by SS3, and filtering at each label gives a nonzero summand. Choose a plateau equal to one near \(\{0,1\}\), supported in \(U_1=(-1/10,11/10)\); LF4 supplies one compact plateau for this compact set. Then the filtered \(f_1u\) is precisely \(x\), by GL3. Direct multiplication gives

<a id="equation-gcc4"></a>

\[
 \alpha_t(x)=2^{-1/2}(e_{11}+e^{-it}e_{12}),\qquad
 s_r(\alpha_t(x))=\frac12
 \begin{pmatrix}1&e^{-it}\\e^{it}&1\end{pmatrix},\qquad
 s_r(x)\ne\alpha_\pi(s_r(x)).
\tag{GCC4}
\]
Each displayed matrix is the projection onto the normalized vector \(2^{-1/2}(1,e^{it})\), as direct multiplication shows; in particular it is a rank-one projection and is the right support of \(\alpha_t(x)\). At \(t=0,\pi\) their sum is \(1\); hence the entire orbit join is \(e_1=1\), although \(s_r(x)\) is not fixed. In (C27), with \(t_1=t_2=0\),

<a id="equation-gcc5"></a>

\[
 z=xyx^*=\tfrac12e_{11}\ne0,\qquad
 \operatorname{Sp}_\alpha(y)=\operatorname{Sp}_\alpha(z)=\{0\}.
\tag{GCC5}
\]
The exact neighbourhoods \(V=(-1/10,1/10)\), \(W=(-13/10,13/10)\), \(O=(-3/2,3/2)\) satisfy (C20)–(C21): \(\overline V+W=(-7/5,7/5)\subset O\), and \(\overline{U_1}-\overline{U_1}=[-6/5,6/5]\subset W\). The spectral set bound in (C28) is conservative: \(\{0,1\}+\{0\}-\{0,1\}=\{-1,0,1\}\), while the actual sandwich has only frequency zero. This numerical model illustrates the proved mechanism, not a countable reduction of the general group.

**Additional problem.** Could one replace \(e_1\) by \(s_r(x)\) in this model merely because it is a projection?

**Solution.** No: its displayed matrix is changed by \(\alpha_\pi\), so it is not a fixed projection and cannot index (C6). The join of the two displayed translates is already \(1\), which is fixed. This is exactly the domain distinction used in the retained problem and solution after (C28).

<a id="oa-flow.gcc.sources"></a>

<a id="gcc-sources"></a>
## Sources and the bounded conclusion

The historical equations (C1)–(C28), their proofs, rank-one example, and original problem and solution are retained. The transport is presented before the central-support reduction: one mechanism transports a nonzero local spectral witness along orbit supports, while the other finds a witness by multiplying with fixed unitaries. Both use the actual earlier local Fourier and projection proofs.

The general fixed-corner assertions correspond to Takesaki, *Theory of Operator Algebras II*, [XI.2 Definition 2.1 and Lemma 2.2, printed 332–333](https://doi.org/10.1007/978-3-662-10451-4). The independent integration and hull-spectrum framework is also developed in Arveson, [*On groups of automorphisms of operator algebras*](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-arveson/1970s/1974_On_groups_of_automorphisms_of_operator_algebras.pdf), J. Funct. Anal. 15 (1974), §§1–2. LF, GL and SS supply complete local proofs for the harmonic-analysis results that those source pages cite externally. The existing free-source real-action CS argument remains available with its own stronger factor hypotheses and positive-transform convention. None of these citations replaces a programme proof.

The bounded results here are fixed-corner restriction, local detection, central-support spectral detection, the central-corner formula, the fixed-algebra factor case and equivalent-fixed-corner invariance for arbitrary LCA \(G\). No subgroup theorem, cocycle invariance, dual-action-center identification or whole C3 completion is claimed. Spot-checked in a separate AI session.

<a id="oa-flow.gcc.figure"></a>

## Orbit supports and a spectral witness in the target corner

![Exact matrix model of the orbit-support join](../assets/general-connes-corners/assets/fixed-corners.png)

This original figure illustrates the support join in [C24–C28](OA-FLOW-GCC.md#gcc-equivalence) through the complete exact model [GCC3–5](OA-FLOW-GCC.md#gcc-model). The general theorem concerns an arbitrary LCH abelian group and arbitrary von Neumann algebra. The picture is a separate \(M_2\), real-action example, not an approximation or a countable reduction of that theorem.

In this example \(\alpha_t=\operatorname{Ad}\operatorname{diag}(1,e^{it})\), \(e=f=1\), \(f_1=e_{11}\), and

<a id="equation-gccf1"></a>

\[
 u=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
 \qquad x=f_1u,\qquad y=e_{22}.
\tag{GCCF1}
\]
The negative Fourier convention gives \(e_{11}\) label zero and \(e_{12}\) label one, so \(\operatorname{Sp}_\alpha(x)=\{0,1\}\). LF4 gives a compact Fourier plateau equal to one near both labels, supported in \(U_1=(-1/10,11/10)\); filtering \(f_1u\) with it leaves \(x\) unchanged. The figure does not depict that plateau's shape.

The right support \(r_t=s_r(\alpha_t(x))\) is the displayed rank-one matrix

<a id="equation-gccf2"></a>

\[
 r_t=\frac12\begin{pmatrix}1&e^{-it}\\e^{it}&1\end{pmatrix}.
\tag{GCCF2}
\]
Panel 3 plots the auxiliary coordinates \((\cos t,\sin t)\) labeling these matrices. The map from these two coordinates to the matrix is explicit: its off-diagonal entry is \((\cos t-i\sin t)/2\). This circle is not a plot of real subspaces of the complex Hilbert space. Its outline uses 721 numerical samples; the matrices, marked points and identities are exact.

The opposite points \(t=0,\pi\) label orthogonal supports with \(r_0+r_\pi=1\). Thus \(s_r(x)\) is not fixed but the join of its full orbit is \(e_1=1\), an admissible fixed projection for the Connes-spectrum intersection. In the abstract proof the join is over all group elements and can have arbitrary cardinality. The illustrated two-point join is a feature of this exact finite model.

For \(t_1=t_2=0\), the final sandwich is

<a id="equation-gccf3"></a>

\[
 z=xyx^*=\frac12e_{11}\ne0,\qquad
 \operatorname{Sp}_\alpha(z)=\{0\}
 \subset\{0,1\}+\{0\}-\{0,1\}=\{-1,0,1\}.
\tag{GCCF3}
\]
Thus the product bound can be conservative without losing nonvanishing or the target corner. With \(V=(-1/10,1/10)\), \(W=(-13/10,13/10)\), and \(O=(-3/2,3/2)\), the exact containments are \(\overline{U_1}-\overline{U_1}=[-6/5,6/5]\subset W\) and \(\overline V+W=(-7/5,7/5)\subset O\). These are the neighbourhood relations required by C20–C21. The abstract argument can choose arbitrarily small differences around any selected spectral point; this particular model uses the explicitly stated larger window.

The proof mechanism's human antecedent is Takesaki, *Theory of Operator Algebras II*, [XI.2 Lemma 2.2(iv), printed 332–333](https://doi.org/10.1007/978-3-662-10451-4). The earlier local Fourier and hull-spectrum tools retain their freely accessible Arveson/LF/GL/SS developments. The reviewed source pages contain no corresponding matrix circle or finite model; this figure and its caption are original.

[Editable SVG](../assets/general-connes-corners/assets/fixed-corners.svg), [exact semantic data](../assets/general-connes-corners/assets/fixed-corners-data.json), and [reproduction source](../assets/general-connes-corners/render_corners.py) are included. Native PNG: 3000 by 2000 pixels. Original figure and caption: GPT-6.1 Sol (OpenAI), Ultra, 5 October 2026, CC0-1.0 to the extent of rights held.
