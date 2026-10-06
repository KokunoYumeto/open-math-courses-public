# Fourier completion and the character topology

Original reviewed H1 proof, now placed after the independently proved topology and Haar/Radon foundations and L24/L25. It identifies the universal Fourier completion and compact-open character topology without a scalar Plancherel or biduality premise. Original CC0 expression retained.

The actual earlier inputs are [H0: compact topology and Hilbert tensor](OA-FLOW-TOPOLOGY.md#l138-h0), [HR-03](OA-FLOW-HR.md#hr-03), [HR-06](OA-FLOW-HR.md#hr-06), [HR-07](OA-FLOW-HR.md#hr-07), [HR-09](OA-FLOW-HR.md#hr-09), [CF-6](OA-FLOW-CF.md#oa-flow.cf.6), [CF-7](OA-FLOW-CF.md#oa-flow.cf.7), [CF-9](OA-FLOW-CF.md#oa-flow.cf.9), and [L24 convolution](OA-FLOW-L24.md#oa-flow.grp.algebra), [L24 recovery](OA-FLOW-L24.md#oa-flow.grp.recovery), [L24 translation continuity](OA-FLOW-L24.md#oa-flow.grp.translations), [L24 universal completion](OA-FLOW-L24.md#oa-flow.grp.completions).

<a id="l138-h1"></a>

## H1. The full Fourier completion directly from CF and L24

Let \(D=C^*(G)\), constructed in [L24](OA-FLOW-L24.md#oa-flow.grp.completions). Abelian convolution makes \(D\) commutative. For \(A=\mathbb C\), the left regular representation on the nonzero Haar \(L^2(G)\) space shows that \(D\ne0\). Its forced unitization \(D^+\) has compact character space \(X\), and [CF Section 6](OA-FLOW-CF.md#oa-flow.cf.6) identifies it isometrically with \(C(X)\). The scalar quotient \(D^+\to\mathbb C\) is a character \(q\in X\). Its kernel \(D\) corresponds exactly to functions vanishing at \(q\). Restriction gives
\[
 D\cong C_0(X\setminus\{q\}).
\tag{H1.1}
\]
For clarity, a continuous function on \(X\) vanishing at \(q\) has compact level sets away from \(q\). Conversely a function vanishing at infinity on \(X\setminus\{q\}\), extended by zero at \(q\), is continuous there because each positive level set is compact and hence closed in \(X\). This proves the asserted \(C_0\) identification.

A character of \(D\) is a nonzero one-dimensional star representation. Its restriction to \(L^1(G)\) is nondegenerate, since density prevents it from vanishing identically. [L24's vector-domain recovery theorem](OA-FLOW-L24.md#oa-flow.grp.recovery) gives a unique continuous unitary character \(s\mapsto\overline{\chi(s)}\), with integrated value
\[
 \psi_\chi(f)=\widehat f(\chi)
 =\int_G f(s)\overline{\chi(s)}\,dm(s).
\tag{H1.2}
\]
Conversely every continuous group character gives this nonzero algebra character: integrate its unitary action, and use the shrinking mass-one bumps from [L24](OA-FLOW-L24.md#oa-flow.grp.translations) to see nonvanishing. These are inverse correspondences.

The topology on \(X\setminus\{q\}\) is exactly compact-open convergence of group characters. Compact-open convergence implies convergence in ([H1](OA-FLOW-HARMONIC.md#l138-h1).2) for \(f\in C_c(G)\), bounded by \(\|f\|_1\) times the uniform character error on its support. Approximate any \(L^1\) function by \(C_c\); character norms are one. Density in \(D\) extends convergence to every element of \(D\).

Conversely suppose \(\psi_i\to\psi\ne0\) on \(D\). Choose \(f_0\in L^1(G)\) with \(\psi(f_0)\ne0\). For a compact \(C\subset G\), the set \(\{L_sf_0:s\in C\}\) is norm compact by [L24's translation continuity](OA-FLOW-L24.md#oa-flow.grp.translations). A finite norm net and the uniform functional bound show
\[
 \sup_{s\in C}|\psi_i(L_sf_0)-\psi(L_sf_0)|\longrightarrow0.
\]
The identity \(\psi_\chi(L_sf_0)=\overline{\chi(s)}\psi_\chi(f_0)\), and denominators bounded away from zero eventually, give uniform convergence of \(\chi_i\) on \(C\). This is a net argument.

Consequently \(\widehat G\), with pointwise character multiplication, is LCH and the Fourier map extends to an isometric star isomorphism
\[
 C^*(G)\cong C_0(\widehat G),\qquad
 \|f\|_u=\|\widehat f\|_\infty.
\tag{H1.3}
\]
The group operations are continuous for compact-open convergence by the scalar inequalities for products and conjugates of unit-modulus functions. Since \(C_c(G)\) is \(L^1\)-dense and the universal norm is at most the \(L^1\) norm, its Fourier image is uniformly dense in \(C_0(\widehat G)\). Fourier injectivity follows here from the definiteness of the universal norm already proved in [L24](OA-FLOW-L24.md#oa-flow.grp.completions); it is not imported from biduality.

<a id="l138-h2"></a>

<a id="oa-flow.xgaps.cstar.h2"></a>

<a id="l138-h0"></a><a id="oa-flow.xgaps.cstar.h0"></a><a id="OA-FLOW.XGAPS.CSTAR.H0"></a>

[H0: actual earlier topology](OA-FLOW-TOPOLOGY.md#l138-h0).

<a id="OA-FLOW.XGAPS.CSTAR.H2"></a>

[H2: actual later deduction](OA-FLOW-HARMONIC-LATE.md#l138-h2).

<a id="l138-h3"></a><a id="oa-flow.xgaps.cstar.h3"></a><a id="OA-FLOW.XGAPS.CSTAR.H3"></a>

[H3: actual later deduction](OA-FLOW-HARMONIC-LATE.md#l138-h3).

<a id="l138-h4"></a><a id="oa-flow.xgaps.cstar.h4"></a><a id="OA-FLOW.XGAPS.CSTAR.H4"></a>

[H4: actual later deduction](OA-FLOW-HARMONIC-LATE.md#l138-h4).

<a id="l138-h5"></a><a id="oa-flow.xgaps.cstar.h5"></a><a id="OA-FLOW.XGAPS.CSTAR.H5"></a>

[H5: actual later deduction](OA-FLOW-HARMONIC-LATE.md#l138-h5).

<a id="oa-flow.xgaps.cstar.harmonic"></a><a id="OA-FLOW.XGAPS.CSTAR.HARMONIC"></a>

[Complete harmonic prerequisite scope](OA-FLOW-HARMONIC-LATE.md#oa-flow.xgaps.cstar.harmonic).
