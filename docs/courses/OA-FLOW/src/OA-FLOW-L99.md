# The spectrum of the full generator of a real action

For a uniformly bounded real action, the generator spectrum is the action spectrum multiplied by \(i\). We prove the result both for norm-continuous Banach-space orbits and for specified-dual weak-star actions. Reciprocal filters give the entire resolvent off the action spectrum; localized vectors then show that every action frequency remains in the spectrum.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.genspec.intertwining"></a>

## Filters and the full generator domain

Use either [BS0's ordinary Banach setting or its specified-dual setting](OA-FLOW-BS.md#bs-0), with \(C_\alpha=\sup_t\|\alpha_t\|<\infty\). In the first setting let \(\tau\) be norm topology; in the second let \(X=Y^*\), let \(\tau=\sigma(X,Y)\), and assume the operators are normal and the predual orbits are norm continuous. Let \(\delta\) denote the full generator in the appropriate topology. Its \(\tau\)-closed graph is proved in [L94](OA-FLOW-L94.md#oa-flow.gen.closed), with the ordinary norm case in [the same lesson](OA-FLOW-L94.md#oa-flow.gen.norm). Its domain need not be norm dense in the dual setting.

Use [AF0's positive convention](OA-FLOW-AF.md#af-0): \(f(q)=\int a(t)e^{itq}dt\) and \(\alpha_f=\int a(t)\alpha_tdt\). Let \(D_\rho\) be the complete modulation generator from [L97](OA-FLOW-L97.md#oa-flow.recip.domain). For \(f\in D(D_\rho)\), the covariance identity gives
\[
 \left\|\frac{\alpha_s\alpha_fx-\alpha_fx}{s}-\alpha_{D_\rho f}x\right\|
 \leq C_\alpha\left\|\frac{\rho_sf-f}{s}-D_\rho f\right\|_A\|x\|
 \longrightarrow0.
 \tag{T1}
\]
Thus, in both settings,
\[
 \alpha_fX\subset D(\delta),\qquad \delta\alpha_f=\alpha_{iqf}.
 \tag{T2}
\]
The derivative of these filtered vectors exists even in norm. No unbounded map is applied before its domain has been checked.

<a id="oa-flow.genspec.reciprocal"></a>

## Every missing frequency has a bounded full-domain inverse

Put \(S=\operatorname{Sp}(\alpha)=h(I_\alpha)\), where \(I_\alpha=\{f:\alpha_f=0\}\). Let \(p\notin S\). Choose \(\theta\in C_c^\infty(\mathbb R)\), equal to one near \(p\), with support disjoint from \(S\). The minimal local ideal inclusion of [LF6](OA-FLOW-LF.md#lf-6), transported by AF0's reflection of signs, implies
\[
 \alpha_\theta=0.
 \tag{T3}
\]
It is the compact support off the hull that justifies this conclusion; no synthesis assertion for arbitrary closed sets is needed.

Set \(b_p=(1-\theta)/(i(\,\cdot-p))\in A(\mathbb R)\), by L97. Take the bounded approximate identity \(e_n(q)=\chi(q/n)\) from [RF3](OA-FLOW-RF.md#rf-3), where \(\chi\) is a smooth compact cutoff with \(\chi(0)=1\). The concentrating-kernel proof there, or [BS2](OA-FLOW-BS.md#bs-2), gives
\[
 \alpha_{e_n}x\longrightarrow x\quad\text{in }\tau.
 \tag{T4}
\]
In the dual case the convergence follows after each predual pairing by the same bounded-kernel estimate; in the norm case it follows from orbit norm continuity.

Although \(b_p\) itself need not belong to \(D(D_\rho)\), its product \(b_pe_n\) does, because
\[
 iqb_p(q)e_n(q)=(1-\theta(q))e_n(q)+ipb_p(q)e_n(q)\in A(\mathbb R).
\]
Apply (T2), the filter multiplication law of BS1, and (T3):
\[
 (\delta-ip)\alpha_{b_pe_n}x=\alpha_{e_n}x.
 \tag{T5}
\]
The vectors on the left before applying the generator equal \(\alpha_{b_p}\alpha_{e_n}x\) and converge to \(\alpha_{b_p}x\) in \(\tau\). Here \(\alpha_{b_p}\) is bounded, and in the dual setting it is normal by BS1. The \(\tau\)-closed graph of \(\delta-ip\) now yields
\[
 \alpha_{b_p}X\subset D(\delta),\qquad
 (\delta-ip)\alpha_{b_p}=I_X.
 \tag{T6}
\]
Since the filter commutes with the group, applying it to a defining difference quotient proves
\(\delta\alpha_{b_p}x=\alpha_{b_p}\delta x\) for every \(x\in D(\delta)\). Normality justifies this passage in the weak-star case. Combining it with (T6) gives
\[
 \alpha_{b_p}(\delta-ip)x=x\quad(x\in D(\delta)).
 \tag{T7}
\]
Therefore \((\delta-ip)^{-1}=\alpha_{b_p}\), including the full-domain range statement, and its norm is at most \(C_\alpha\|b_p\|_A\).

<a id="oa-flow.genspec.bump"></a>

## Localized unit vectors detect every frequency

Now let \(p\in S\). Choose \(H\in C_c^\infty(\mathbb R)\), equal to one on \([-1/2,1/2]\), supported in \([-1,1]\), and put
\[
 h_\varepsilon(q)=H((q-p)/\varepsilon),\quad
 K(r)=irH(r),\quad
 k_\varepsilon(q)=i(q-p)h_\varepsilon(q)
                =\varepsilon K((q-p)/\varepsilon).
 \tag{T8}
\]
For each \(\varepsilon>0\), choose a smooth compact \(c\), supported in \((p-\varepsilon/3,p+\varepsilon/3)\), with \(c(p)=1\). RF1 constructs it. Since \(p\in h(I_\alpha)\), the operator \(\alpha_c\) is nonzero. Choose \(y\) with \(\alpha_cy\ne0\) and normalize this vector to \(x_\varepsilon\).

[BS3](OA-FLOW-BS.md#bs-3) puts its vector spectrum in \(\operatorname{supp}c\). The same lemma says that a filter equal to one near this compact spectrum fixes the vector. Hence
\[
 \|x_\varepsilon\|=1,\qquad
 \alpha_{h_\varepsilon}x_\varepsilon=x_\varepsilon.
\]
Both \(h_\varepsilon\) and \(qh_\varepsilon\) are smooth compact functions, so L97 and (T2) give \(x_\varepsilon\in D(\delta)\) and
\[
 (\delta-ip)x_\varepsilon=\alpha_{k_\varepsilon}x_\varepsilon,\qquad
 \|(\delta-ip)x_\varepsilon\|
 \leq C_\alpha\varepsilon\|K\|_A.
 \tag{T9}
\]
The norm calculation uses the exact dilation and translation identities (R5). Thus these are approximate eigenvectors in the full generator domain. A bounded inverse for \(\delta-ip\) would imply
\(1\leq\|(\delta-ip)^{-1}\|C_\alpha\varepsilon\|K\|_A\) for all \(\varepsilon>0\), which is impossible. Therefore \(iS\subset\sigma(\delta)\).

<a id="oa-flow.genspec.equality"></a>

## The equality and its scope

The complete Laplace proofs in [L95](OA-FLOW-L95.md#oa-flow.res.forward), and its [ordinary Banach version](OA-FLOW-L95.md#oa-flow.res.norm), supply every resolvent with nonzero real part. Equations (T6)–(T7) supply the remaining parameters \(ip\) outside \(iS\), and (T9) includes every point of \(iS\). Therefore
\[
 \boxed{\sigma(\delta)=i\,\operatorname{Sp}(\alpha).}
 \tag{T10}
\]
The spectrum here uses a bounded inverse on all of \(X\) whose range is \(D(\delta)\). In the dual setting this formulation does not require norm density of that domain. For \(X=0\), both spectra are empty; the same identities hold with the unique maps of that space.

**Example.** For \(\alpha_t=\operatorname{diag}(e^{itp_1},\ldots,e^{itp_n})\), a filter acts diagonally by \(f(p_j)\). Cutoffs show that the action spectrum is the set of distinct \(p_j\), and coordinate differentiation gives \(\delta=\operatorname{diag}(ip_j)\). This realizes (T10) directly.

**Domain diagnostic.** The \(c_0\) and \(\ell^\infty\) phase actions in [L94](OA-FLOW-L94.md#oa-flow.gen.norm-model) have the same action spectrum \(\{1,2,\ldots\}\). Indeed a filter acts on the \(n\)-th coordinate by \(f(n)\), so its annihilator consists exactly of the functions vanishing on this closed set. Its hull is this set, by smooth cutoffs off it. Their generator spectra therefore agree, although their full derivative domains differ. Equality of spectra does not identify generator domains.

The source statement is Takesaki, *Theory of Operator Algebras II*, XI.1, equation (21′) and Theorem 1.23, printed p.328 ([edition](https://doi.org/10.1007/978-3-662-10451-4)). The full inverse and localized-vector arguments above use the proved Fourier and generator inputs.
