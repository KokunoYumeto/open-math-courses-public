# Compact frequencies and norm-continuous actions

An action can move each predual vector continuously while its operators fail to approach the identity in norm. Compactness of the action spectrum is the precise extra condition that upgrades the action to operator-norm continuity. This lesson proves Takesaki II, Corollary XI.1.16 in both directions for the uniformly bounded dual Banach action of [AF0](OA-FLOW-AF.md#af-0).

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

<a id="oa-flow.frequency.compact"></a>

<a id="OA-FLOW.NORMCONT.FORWARD"></a><a id="oa-flow.normcont.forward"></a>

## Norm continuity puts the identity in the filter algebra

Assume first that \(s\mapsto\alpha_s\) is continuous in operator norm. Let \(a_V\in C_c(G)\) be the nonnegative unit-mass approximate identity proved in [L24](OA-FLOW-L24.md#oa-flow.grp.algebra) and [BS2](OA-FLOW-BS.md#bs-2), supported in shrinking identity neighborhoods \(V\), and put \(e_V=\mathcal Fa_V\). The complete integrated-action proof BS1 gives

<a id="equation-n1"></a>

$$\|\alpha_{e_V}-I\|
\le\sup_{t\in V}\|\alpha_t-I\|\longrightarrow0.\tag{N1}$$

Therefore the operator identity belongs to the norm-closed filter algebra \(\mathcal B_\alpha\) of [the filter-character proof](OA-FLOW-L91.md#oa-flow.frequency.filtercharacters). When \(X\ne\{0\}\), this makes \(\mathcal B_\alpha\) a unital commutative Banach algebra. Its character space is compact in the Gelfand topology by the complete character-space proof [CF4](OA-FLOW-CF.md#oa-flow.cf.4): the product of bounded coordinate discs is compact by the proved ultrafilter argument, and the character equations define a closed subset. Its identity \(I\) has norm one, so the hypotheses of that proof match exactly. By the homeomorphism (C6),

<a id="equation-n2"></a>

$$s\longmapsto\alpha_s\text{ norm continuous}
\quad\Longrightarrow\quad\operatorname{Sp}(\alpha)\text{ compact}.\tag{N2}$$

If \(X=\{0\}\), the action is norm continuous and its action spectrum is empty, hence compact. This case does not require treating the zero operator algebra as a nonzero unital algebra.

<a id="OA-FLOW.NORMCONT.CUTOFF"></a><a id="oa-flow.normcont.cutoff"></a>

## A compact spectrum gives one identity filter

Conversely, suppose \(E=\operatorname{Sp}(\alpha)\) is compact. The complete compact-set plateau [LF4](OA-FLOW-LF.md#lf-4) supplies \(f\in A_c(H)\) equal to one on an open neighborhood of \(E\). Write \(f=\mathcal Fa\), and represent it by the finite measure \(d\mu(t)=a(-t)\,dt\) as in (F7) of [the four-tests proof](OA-FLOW-L88.md#oa-flow.frequency.measures). Then \(\widehat\mu=f\). The local measure identity (O8) of [the individual-operator proof](OA-FLOW-L89.md#oa-flow.frequency.operator) yields

<a id="equation-n3"></a>

$$\alpha_f=\alpha_\mu=I.\tag{N3}$$

The neighborhood in this cutoff is important: the argument uses the minimal local ideal and does not require every Fourier function vanishing pointwise on \(E\) to annihilate the action. If \(E=\varnothing\), the full empty-hull and essentiality proofs [LF6](OA-FLOW-LF.md#lf-6) and [BS2–3](OA-FLOW-BS.md#bs-2) imply \(X=\{0\}\), and the conclusion is again immediate.

<a id="OA-FLOW.NORMCONT.REVERSE"></a><a id="oa-flow.normcont.reverse"></a>

## Translating the cutoff controls the operator norm

For \(s\in G\), let \(m_sf(p)=(s,p)f(p)\). The complete integrated covariance (AF2) and (N3) give

<a id="equation-n4"></a>

$$\alpha_s=\alpha_s\alpha_f=\alpha_{m_sf}.\tag{N4}$$

If \(f=\mathcal Fa\), the positive Fourier convention gives \(m_sf=\mathcal F(\tau_s a)\), where \((\tau_s a)(u)=a(u-s)\). Translation is norm continuous on \(L^1(G)\), without a countability assumption. The translation proof [L24 Lemma 3.1](OA-FLOW-L24.md#oa-flow.grp.translations) and the actual filter bound (AF2) therefore give, for \(s,t\in G\),

<a id="equation-n5"></a>

$$\|\alpha_s-\alpha_t\|
\le C_\alpha\|m_sf-m_tf\|_A
=C_\alpha\|\tau_sa-\tau_ta\|_1\longrightarrow0
\quad(s\to t).\tag{N5}$$

Together with (N2), this proves the equivalence

<a id="equation-n6"></a>

$$\boxed{s\mapsto\alpha_s\text{ is operator-norm continuous}
\quad\Longleftrightarrow\quad\operatorname{Sp}(\alpha)\text{ is compact}.}\tag{N6}$$

The statement is about continuity in \(\mathcal B(X)\)'s operator norm, not only norm continuity of each individual orbit. The latter condition is already part of many Banach representations and does not supply the uniform estimate in (N1).

The same equivalence holds in AF0 setting (B), for a uniformly bounded strongly continuous Banach action. The mass-one integrated estimate, filter algebra, character homeomorphism and local measure identity have already been proved there. The last norm estimate uses only translation continuity in \(L^1(G)\), in the \(L^1\) norm.

**Problem.** On \(X=\ell^\infty(\mathbb N)\), compare the diagonal actions \((\alpha_t x)_n=e^{int}x_n\) and \((\beta_t x)_n=e^{it/n}x_n\), both with predual \(\ell^1(\mathbb N)\). Which is operator-norm continuous at zero?

**Solution.** For \(t_k=\pi/k\), the \(k\)-th coordinate of \(\alpha_{t_k}-I\) has modulus \(2\), so \(\|\alpha_{t_k}-I\|=2\); this action is not norm continuous. Its spectral frequencies contain all positive integers and are not compact. For \(\beta\), \(\|\beta_t-I\|=\sup_n|e^{it/n}-1|\le|t|\), so it is norm continuous. Its action spectrum is the compact closure \(\{1/n:n\ge1\}\cup\{0\}\). To check equality rather than only inclusion, a coordinate vector of frequency \(r_n\) has filter value \(f(r_n)\), so BS3 and the scalar singleton ideals put \(r_n\) in the action spectrum. Closedness includes their closure. If \(p\) is outside that closure, an LF1 plateau supported in its open complement is one at \(p\), while its diagonal filter is zero; hence \(p\) is outside the hull. This proves that the exact spectrum of either diagonal example is \(\overline{\{r_n\}}\). AF0 supplies the actual \(\ell^1\) predual, and AF4 identifies the real dual topology. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Corollary XI.1.16, printed page 324 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). Both implications use the exact mass-one, character-space and local measure/filter proofs above. The theorem and examples retain operator-norm continuity, distinct from continuity of individual or predual orbits.
