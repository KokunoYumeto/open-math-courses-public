# Four tests for an action frequency

A point of the action spectrum can be detected without constructing a spectral measure: narrow-band vectors become approximate character eigenvectors uniformly on compact group sets. The same points are characterized by lower bounds for every finite-measure integrated operator, or only for Fourier filters. The implications require a compact-tail estimate for measures and the exact Fourier sign in the measure definition. This lesson proves Takesaki II, Lemma XI.1.12 for the arbitrary LCA dual-Banach action of AF0 setting (D).

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

<a id="oa-flow.frequency.tests"></a>

<a id="OA-FLOW.ACTSPEC.APPROX"></a><a id="oa-flow.actspec.approx"></a>

## Spectral points yield approximate character vectors

Let \(G\) be an arbitrary locally compact Hausdorff abelian group, \(H=\widehat G\), and \(\alpha\) a uniformly bounded normal action on \(X=X_*^*\) with norm-continuous predual orbits, as in [AF0](OA-FLOW-AF.md#af-0). Write \((t,p)=p(t)\). The first two tests are equivalent:

**(i)** \(p\in\operatorname{Sp}(\alpha)\).

**(ii)** There is a net of unit vectors \(x_i\in X\) such that, for every compact \(K\subset G\),

<a id="equation-f1"></a>

$$\sup_{t\in K}\|\alpha_t x_i-(t,p)x_i\|\longrightarrow0.\tag{F1}$$

Assume (i). Given compact \(K\) and \(\varepsilon>0\), [the earlier narrow-band proof](OA-FLOW-L87.md#oa-flow.band.orbits) supplies an open neighborhood \(U\ni p\) such that every \(x\in X_\alpha(U)\) has orbit error at most \(\varepsilon\|x\|\) on \(K\). This space contains a nonzero vector by a direct current-provider argument. LF1 gives a compactly supported filter \(c\) in \(U\) with \(c(p)=1\). Since \(p\in h(I(\alpha))\), the operator \(\alpha_c\) cannot vanish. Choose \(y\) with \(\alpha_cy\ne0\). The filter-support theorem BS3 puts its spectrum inside \(\operatorname{supp}c\subset U\); normalize that vector. Thus \(X_0^\alpha(U)\ne0\), where this notation denotes the closed filtered span of BS4. In particular a nonzero generator \(\alpha_fy\), with \(\operatorname{supp}f\subset U\), has spectrum inside that compact support. This is the actual nonzero-band proof; the closed filtered span itself can acquire boundary frequencies, as BS4 explains.

Direct the pairs \((K,\varepsilon)\) by inclusion of compact sets and decreasing positive error. A finite union of compact sets is compact, so this is a directed set even when \(G\) is not sigma compact. Selecting one normalized narrow-band vector for each pair gives the net in (ii). In particular, no sequence is claimed in the absence of a countable compact exhaustion.

<a id="oa-flow.frequency.measures"></a>

<a id="OA-FLOW.ACTSPEC.MEASURE"></a><a id="oa-flow.actspec.measure"></a>

## Finite-measure integrated operators

For a finite complex regular Borel measure \(\mu\) on \(G\), use the negative action parameter and the matching negative character sign:

<a id="equation-f2"></a>

$$\widehat\mu(p)=\int_G\overline{(t,p)}\,d\mu(t),\qquad
\alpha_\mu x=\int_G\alpha_{-t}x\,d\mu(t). \tag{F2}$$

The finite-measure convention and its complete vector integral are proved in [AF1](OA-FLOW-AF.md#af-1): \(\|\mu\|=|\mu|(G)<\infty\), with Radon total variation and its completion. The second integral is a weak-star integral, defined through the specified predual. For \(\phi\in X_*\), the orbit \(t\mapsto\phi\circ\alpha_{-t}\) is norm continuous and bounded by \(C_\alpha\|\phi\|\). AF1 proves strong measurability on a full-measure countable union of compact sets, with separable essential range even when the predual and group are nonseparable. It therefore gives the full norm integral. Equivalently, integrate it in \(X_*\) first over compact sets. Regularity of \(|\mu|\) provides compact sets whose complements have arbitrarily small mass; the integrals converge in predual norm, independent of the exhaustion. Their bounded operator \(B_\mu:X_*\to X_*\) has \(\|B_\mu\|\le C_\alpha\|\mu\|\), and \(\alpha_\mu=B_\mu^*\). Therefore

<a id="equation-f3"></a>

$$\alpha_\mu\text{ is normal},\qquad
\|\alpha_\mu\|\le C_\alpha\|\mu\|. \tag{F3}$$

There is no global sigma-finiteness assumption on Haar measure and no assertion that arbitrary \(X\)-orbits are Bochner integrable in norm.

<a id="OA-FLOW.ACTSPEC.TAIL"></a><a id="oa-flow.actspec.tail"></a>

## Compact-tail control of a measure

Assume (ii), and fix \(\mu\). For a compact \(K\subset G\), a unit vector \(x_i\), and \(t\in K\), compare \(\alpha_{-t}x_i\) with \(\overline{(t,p)}x_i=(-t,p)x_i\). The triangle inequality and the uniform action bound give

<a id="equation-f4"></a>

$$\begin{aligned}
\|\alpha_\mu x_i-\widehat\mu(p)x_i\|
&\le |\mu|(K)
\sup_{s\in-K}\|\alpha_sx_i-(s,p)x_i\|\\
&\quad +(C_\alpha+1)|\mu|(G\setminus K).
\end{aligned}\tag{F4}$$

For every unit predual functional, integrate its continuous scalar pairing and bound it by the same compact supremum. Taking the norming supremum proves (F4) even when the X-valued orbit has no norm integral. The compact part follows by integration of the norm bound; on the complement, \(\|\alpha_{-t}x_i\|+\|x_i\|\le C_\alpha+1\). For fixed \(K\), the first term tends to zero by (ii), since \(-K\) is compact. Given \(\delta>0\), regularity supplies \(K\) with \(|\mu|(G\setminus K)<\delta/(C_\alpha+1)\); then take the net index large. Consequently \(\alpha_\mu x_i-\widehat\mu(p)x_i\to0\) in norm, and \(\|x_i\|=1\) implies

<a id="equation-f5"></a>

$$|\widehat\mu(p)|\le\|\alpha_\mu\|
\quad\text{for every finite complex regular measure }\mu. \tag{F5}$$

This is test (iii). The two limits are ordered: first choose a compact set controlling the measure tail, then use compact-uniform approximation on that set. No uniform approximation over all of a noncompact \(G\) is required.

<a id="OA-FLOW.ACTSPEC.NORM"></a><a id="oa-flow.actspec.norm"></a>

## Fourier filters and the reverse implication

Test (iv) is the corresponding statement only for Fourier functions:

<a id="equation-f6"></a>

$$|f(p)|\le\|\alpha_f\|
\quad\text{for every }f\in A(H). \tag{F6}$$

Condition (iii) implies (iv) with an explicit sign check. Write \(f=\mathcal Fa\) using the positive Fourier convention, and set \(d\mu(s)=a(-s)\,ds\). [L24’s inversion proof](OA-FLOW-L24.md#oa-flow.grp.translations) gives Haar inversion invariance on an LCA group; [HR3](OA-FLOW-HR.md#hr-03) and AF1 give the finite regular density measure at a Borel representative of the kernel. Changing variables \(t=-s\) in (F2) gives

<a id="equation-f7"></a>

$$\alpha_\mu=\alpha_f,
\qquad\widehat\mu(p)
=\int_G\overline{(s,p)}a(-s)\,ds
=\int_G(t,p)a(t)\,dt=f(p). \tag{F7}$$

Finally assume (iv). If \(p\notin\operatorname{Sp}(\alpha)=h(I(\alpha))\), some \(f\in I(\alpha)\) has \(f(p)\ne0\). But \(\alpha_f=0\), contradicting (F6). Thus (iv) implies (i). Together with the preceding sections, (i)–(iv) are equivalent. \(\square\)

All four tests hold also in AF0 setting (B). Use AF1’s norm integral on every vector for (F2), giving the same bound (F3) without a normality assertion; (F4) is the norm integral inequality there. The band proof, hull implication and all scalar sign calculations are unchanged. Thus the dual-space theorem is retained and the ordinary Banach generality has its actual complete construction.

**Problem.** Let \(\alpha_t=\operatorname{diag}(e^{it\lambda_1},e^{it\lambda_2})\) on \(\mathbb C^2\). Identify its action spectrum and the norm \(\|\alpha_\mu\|\).

**Solution.** The two coordinate lines have frequencies \(\lambda_1,\lambda_2\), so \(\operatorname{Sp}(\alpha)=\{\lambda_1,\lambda_2\}\), with a repeated frequency listed once. Formula (F2) makes \(\alpha_\mu\) diagonal with entries \(\widehat\mu(\lambda_1)\) and \(\widehat\mu(\lambda_2)\), hence \(\|\alpha_\mu\|=\max_j|\widehat\mu(\lambda_j)|\). Thus (F5) holds at either spectral frequency. For \(p\) outside the finite set, a local Fourier cutoff can be one at \(p\) and zero at both \(\lambda_j\), violating (F6) and therefore (F5). \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Lemma XI.1.12, printed pages 322–323 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). Equations (F2)–(F7) use the same negative character sign as the negative action parameter. The narrow-band proof and all finite-measure domains are supplied at exact earlier locators; the compact-tail order of limits retains arbitrary LCA groups.
