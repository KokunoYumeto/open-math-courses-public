# Narrow spectral bands give nearly character orbits

A vector whose frequencies lie in a sufficiently narrow band around \(p\) behaves, for a fixed compact set of group elements, almost like a \(p\)-eigenvector in norm. The width can be chosen uniformly for every vector in that spectral band. A norm-controlled Fourier cutoff and singleton synthesis make this precise even when individual orbits are only weak-star continuous. This is Takesaki II, Lemma XI.1.11 at arbitrary LCA and specified dual-Banach generality.

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

The positive Fourier convention and both eligible Banach settings are [AF0](OA-FLOW-AF.md#af-0). The exact earlier scalar inputs are LF0–1 for the complete dual-Haar correlation identity and norm-controlled local plateaus, LF4 for plateaus around compact sets, and SS1 for singleton synthesis. BS1–3 supply the full integrated action, filter bounds and cutoff laws in both Banach settings.

<a id="oa-flow.band.plateau"></a>

<a id="OA-FLOW.BAND.FLATTOP"></a><a id="oa-flow.band.flattop"></a>

## A flat-top cutoff with norm below two

Use the arbitrary locally compact Hausdorff abelian group \(G\), its dual \(H=\widehat G\), and the Fourier algebra \(A(H)=\mathcal F L^1(G)\) of [AF0](OA-FLOW-AF.md#af-0). For any \(p\in H\) and open neighborhood \(O\ni p\), there is \(h\in A_c(H)\) such that

<a id="equation-n1"></a>

$$h=1\text{ near }p,\qquad
\operatorname{supp}h\subset O,\qquad
\|h\|_A<2. \tag{N1}$$

Here is an explicit construction. Translate to \(p=0\). Choose a relatively compact open identity neighborhood \(N\) so small that \(N-N\subset O\). Let \(V\subset N\) be compact with positive Haar measure, and by outer regularity choose an open \(W\) with \(V\subset W\), compact closure inside \(N\), and \(m(W)<4m(V)\). Such \(V,W\) can be chosen by first putting a positive-measure compact set inside a smaller open neighborhood and then shrinking its outer neighborhood. Define

<a id="equation-n2"></a>

$$h(q)=\frac{1}{m(V)}\int_H 1_W(r)1_V(r-q)\,dr
=\frac{m(W\cap(V+q))}{m(V)}. \tag{N2}$$

The \(L^2\) correlation is continuous and supported in the compact set \(\overline W-V\subset N-N\). Since \(V\) is compact and \(W\) open, \(V+q\subset W\) for every \(q\) in some identity neighborhood, so \(h=1\) there. With the chosen dual Haar normalization, put \(u=\mathcal F^{-1}(1_W)\) and \(v=\mathcal F^{-1}(1_V)\). The correlation in (N2) has inverse Fourier kernel \(u\overline v/m(V)\). Plancherel and Cauchy–Schwarz give the required \(L^1\) bound. Thus it lies in \(L^1(G)\), and

<a id="equation-n3"></a>

$$\|h\|_A
\le\frac{\|1_W\|_2\|1_V\|_2}{m(V)}
=\sqrt{\frac{m(W)}{m(V)}}<2. \tag{N3}$$

Frequency translation moves this cutoff to \(p\) without changing its \(A\)-norm. The construction uses compact Haar sets and nets of neighborhoods, not second countability or a smooth structure on \(H\).

<a id="oa-flow.band.localproduct"></a>

<a id="OA-FLOW.BAND.SMALLPRODUCT"></a><a id="oa-flow.band.smallproduct"></a>

## A vanishing filter has a small local product

The complete singleton-synthesis proof SS1, transported by the reflection in AF0, and (N1) give the following local multiplication lemma. If \(g\in A(H)\) and \(g(p)=0\), then for every \(\eta>0\) there is an \(h\in A_c(H)\), equal to \(1\) near \(p\), with

<a id="equation-n4"></a>

$$\|h\|_A<2,\qquad \|hg\|_A<\eta. \tag{N4}$$

To prove it, use \(j(\{p\})=I(\{p\})\) to choose \(g_0\in A_c(H)\) whose support misses \(p\) and with \(\|g-g_0\|_A<\eta/2\). Choose a neighborhood \(O\ni p\) disjoint from \(\operatorname{supp}g_0\), and construct \(h\) from (N1) supported in \(O\). Then \(hg_0=0\), so \(\|hg\|_A\le\|h\|_A\|g-g_0\|_A<\eta\). This proof identifies exactly where singleton synthesis is used; mere pointwise continuity of \(g\) would not control the Fourier-algebra norm of \(hg\).

<a id="oa-flow.band.orbits"></a>

<a id="OA-FLOW.BAND.ORBIT"></a><a id="oa-flow.band.orbit"></a>

## The filtered orbit identity

Let \(X=X_*^*\) and \(\alpha\) satisfy the uniformly bounded normal action hypotheses of AF0 setting (D), with \(C_\alpha=\sup_t\|\alpha_t\|\). If \(X=\{0\}\), the conclusion is immediate; otherwise \(C_\alpha\ge1\), so the divisions below are defined. Fix \(p\in H\), a compact set \(K\subset G\), and \(\varepsilon>0\). Choose a compact neighborhood \(V\) of \(p\) and \(f\in A_c(H)\) equal to \(1\) on a neighborhood of \(V\). For \(t\in G\), set

<a id="equation-n5"></a>

$$f_t(q)=(t,q)f(q),\qquad
g_t(q)=f_t(q)-(t,p)f(q). \tag{N5}$$

The actual integrated covariance BS1, in AF0’s positive convention, gives \(\alpha_t\alpha_f=\alpha_{f_t}\), and \(g_t(p)=0\). If \(U\) is a relatively compact open neighborhood of \(p\) with \(\overline U\subset\operatorname{int}V\), and \(x\in X_\alpha(U)\), then \(\operatorname{Sp}_\alpha(x)\subset\overline U\) is compact. The proved compact-spectral cutoff BS3 gives \(\alpha_f x=x\). Hence

<a id="equation-n6"></a>

$$\alpha_t x-(t,p)x=\alpha_{g_t}x. \tag{N6}$$

The map \(t\mapsto g_t\) is norm continuous in \(A(H)\): \(t\mapsto f_t\) is norm continuous by translation continuity of the inverse \(L^1\) kernel in [L24 Lemma 3.1](OA-FLOW-L24.md#oa-flow.grp.translations), and \(t\mapsto(t,p)\) is continuous. This norm continuity is stronger than orbit weak-star continuity and is the input for the compact-uniform step.

<a id="OA-FLOW.BAND.UNIFORM"></a><a id="oa-flow.band.uniform"></a>

## One band for a whole compact time set

For each \(t\in K\), apply (N4) to \(g_t\) with \(\eta=\varepsilon/(2C_\alpha)\). Obtain \(h_t\in A_c(H)\), equal to \(1\) on a neighborhood \(U_t\) of \(p\), with \(\|h_tg_t\|_A<\eta\). By norm continuity of \(s\mapsto g_s\), choose a neighborhood \(W_t\) of \(t\) such that

<a id="equation-n7"></a>

$$\|h_tg_s\|_A<\varepsilon/C_\alpha
\qquad(s\in W_t). \tag{N7}$$

Finitely many \(W_{t_1},\ldots,W_{t_m}\) cover \(K\). Choose a relatively compact open neighborhood \(U\) of \(p\) whose closure lies inside \(\operatorname{int}V\) and inside every neighborhood on which the finitely many \(h_{t_j}\) equal \(1\). For \(x\in X_\alpha(U)\), the compact-spectral cutoff lemma gives \(\alpha_{h_{t_j}}x=x\). If \(s\in K\cap W_{t_j}\), use (N6), the module law and filter bound (AF2):

<a id="equation-n8"></a>

$$\begin{aligned}
\|\alpha_sx-(s,p)x\|
&=\|\alpha_{g_s}\alpha_{h_{t_j}}x\|\\
&=\|\alpha_{h_{t_j}g_s}x\|\\
&\le C_\alpha\|h_{t_j}g_s\|_A\|x\|
\le\varepsilon\|x\|.
\end{aligned}\tag{N8}$$

Thus one neighborhood \(U\) works for every \(s\in K\) and every vector \(x\in X_\alpha(U)\). The last inequality is strict for \(x\ne0\); the non-strict statement in (N8) also includes \(x=0\). The estimate is meaningful even when \(X_\alpha(U)=\{0\}\); lesson 88 will relate nonzero narrow-band vectors to membership of \(p\) in the action spectrum.

The same estimate also holds in AF0 setting (B), on an arbitrary Banach space with norm-continuous orbits. Every step above uses the bounded integrated homomorphism, its norm bound, translation continuity and the vector-spectrum cutoff law. BS1–3 prove those statements in (B); the calculation has no additional weak-star limit. In fact it works for every vector with spectrum in \(\overline U\), so it applies both to \(X_\alpha(U)\) as defined in AF0 and to BS4’s filtered-span space \(X_\alpha^0(U)\subset X_\alpha(\overline U)\).

**Problem.** On \(X=\mathbb C^2\), let \(\alpha_t=\operatorname{diag}(e^{it\lambda_1},e^{it\lambda_2})\) with \(\lambda_1\ne\lambda_2\) and choose \(p=\lambda_1\). How can \(U\) be chosen so that (N8) holds with zero error?

**Solution.** Take \(U\) containing \(\lambda_1\) but not \(\lambda_2\). Then \(X_\alpha(U)\) is the first coordinate line, and \(\alpha_t x=e^{it\lambda_1}x=(t,p)x\) there for every \(t\in\mathbb R\). The general lemma replaces this exact finite-frequency separation by a uniform estimate for possibly continuous spectra. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Lemma XI.1.11, printed pages 321–322 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The norm-controlled correlation and complete singleton proof have their exact earlier locators above. The argument keeps the compact-uniform estimate at arbitrary LCA generality and preserves its finite-frequency example; it does not use the separate full spectral-transfer theorem.
