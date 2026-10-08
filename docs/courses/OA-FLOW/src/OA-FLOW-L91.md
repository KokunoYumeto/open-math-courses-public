# Characters of the filter algebra

Fourier filters act on the Banach space through operators \(\alpha_f\). Their operator-norm closure is a commutative Banach algebra whose characters record exactly the action frequencies. This lesson proves Takesaki II, Corollary XI.1.15, including the topology of that character space and the possibly nonunital case. Its harmonic character input is the complete convolution-algebra classification in [AF2](OA-FLOW-AF.md#af-2), with actual current Haar and norm-integral proofs.

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

<a id="oa-flow.frequency.filtercharacters"></a>

<a id="OA-FLOW.CHAR.ALGEBRA"></a><a id="oa-flow.char.algebra"></a>

## The norm-closed filter algebra

Retain the arbitrary locally compact abelian group \(G\), dual \(H\), and uniformly bounded normal dual Banach action \(\alpha\) of [AF0](OA-FLOW-AF.md#af-0). Let

<a id="equation-c1"></a>

$$\mathcal B_\alpha
:=\overline{\{\alpha_f:f\in A(H)\}}^{\|\cdot\|_{\mathcal B(X)}}.\tag{C1}$$

The map \(f\mapsto\alpha_f\) is a bounded algebra homomorphism by (AF2), proved at [BS1](OA-FLOW-BS.md#bs-1). Its image is already a linear subalgebra, so (C1) is a commutative Banach algebra. It may have no identity, even though it sits inside the unital algebra \(\mathcal B(X)\). Write \(\Delta(\mathcal B_\alpha)\) for its nonzero continuous multiplicative linear functionals. No character of an adjoined unit is included.

<a id="OA-FLOW.CHAR.FROM-FREQUENCY"></a><a id="oa-flow.char.from-frequency"></a>

## A frequency gives a bounded character

For \(p\in\operatorname{Sp}(\alpha)\), define on the dense filter image

<a id="equation-c2"></a>

$$\chi_p(\alpha_f):=f(p).\tag{C2}$$

If \(\alpha_f=\alpha_g\), then \(f-g\in I(\alpha)\), whose hull contains \(p\); thus (C2) is well defined. The norm test (F6) of [the four-tests proof](OA-FLOW-L88.md#oa-flow.frequency.tests) gives

<a id="equation-c3"></a>

$$|\chi_p(\alpha_f)|=|f(p)|\le\|\alpha_f\|.\tag{C3}$$

Therefore \(\chi_p\) extends uniquely and continuously to \(\mathcal B_\alpha\). It remains multiplicative because \(\alpha_f\alpha_g=\alpha_{fg}\) and operator multiplication is norm continuous. Choose a local Fourier cutoff \(c\in A_c(H)\) with \(c(p)=1\). Then \(\chi_p(\alpha_c)=1\), so the extension is nonzero. Thus \(p\mapsto\chi_p\) maps the action spectrum into \(\Delta(\mathcal B_\alpha)\).

<a id="OA-FLOW.CHAR.TO-FREQUENCY"></a><a id="oa-flow.char.to-frequency"></a>

## Every character comes from one frequency

Let \(\chi\in\Delta(\mathcal B_\alpha)\). The pullback \(\psi(f)=\chi(\alpha_f)\) is a continuous multiplicative functional on \(A(H)\), and it is nonzero: if it vanished on every filter operator, continuity and the density in (C1) would make \(\chi=0\). Under the isometric Fourier identification with \(L^1(G)\), the complete convolution-character proof in [AF2](OA-FLOW-AF.md#af-2) says that \(\psi\) is evaluation at exactly one \(p\in H\). Hence

<a id="equation-c4"></a>

$$\chi(\alpha_f)=\psi(f)=f(p)\quad(f\in A(H)).\tag{C4}$$

For \(f\in I(\alpha)\), (C4) gives \(f(p)=0\), so \(p\in h(I(\alpha))=\operatorname{Sp}(\alpha)\). The density of filter operators then forces \(\chi=\chi_p\). Distinct points give distinct characters because local Fourier cutoffs separate points. We obtain a bijection

<a id="equation-c5"></a>

$$\operatorname{Sp}(\alpha)\longleftrightarrow\Delta(\mathcal B_\alpha),
\qquad p\longmapsto\chi_p.\tag{C5}$$

AF2 proves automatic continuity even for initially algebraic characters, constructs the unit-modulus character of \(G\) by translations, and identifies it on every \(L^1\) kernel by the full vector convolution integral, with \(C_c(G)\)-density proved in L24. The exact earlier norm-controlled cutoffs are [LF1/4](OA-FLOW-LF.md#lf-1). Thus the harmonic classification is a complete local input, while the present proof supplies its operator-algebra image and topology.

<a id="OA-FLOW.CHAR.TOPOLOGY"></a><a id="oa-flow.char.topology"></a>

## The two topologies agree

The Gelfand topology on \(\Delta(\mathcal B_\alpha)\) is the weakest topology making \(\chi\mapsto\chi(B)\) continuous for every \(B\in\mathcal B_\alpha\). For \(B=\alpha_f\), its pullback under (C5) is \(p\mapsto f(p)\), continuous on \(H\). For arbitrary \(B\), choose \(\alpha_{f_j}\to B\) in operator norm. Every character has norm at most one: in the unitization, \(|\chi(B)|>\|B\|\) would make \(1-B/\chi(B)\) invertible by a Neumann series although its extended character value is zero. Thus \(f_j(p)=\chi_p(\alpha_{f_j})\) converges uniformly in \(p\in\operatorname{Sp}(\alpha)\) to \(\chi_p(B)\). Hence \(p\mapsto\chi_p\) is continuous.

Conversely, suppose a net \(\chi_{p_i}\to\chi_p\) in the Gelfand topology. Then \(f(p_i)\to f(p)\) for every \(f\in A(H)\). Given any open neighborhood \(U\) of \(p\) in \(H\), choose \(c\in A_c(H)\) supported in \(U\) with \(c(p)=1\). Eventually \(c(p_i)\) is near one, hence nonzero, so \(p_i\in U\). Therefore \(p_i\to p\) in \(H\), and (C5) is a homeomorphism:

<a id="equation-c6"></a>

$$\Delta(\mathcal B_\alpha)\cong\operatorname{Sp}(\alpha)
\quad\text{with the subspace topology inherited from }H.\tag{C6}$$

This argument also covers an empty action spectrum: the pullback proof shows there is then no nonzero character of \(\mathcal B_\alpha\). It does not silently adjoin a unit or an extra point.

This proof also applies in AF0 setting (B). It uses only the bounded integrated homomorphism, the four-tests norm inequality and scalar local cutoffs, all already proved in (B). In particular it does not treat an arbitrary operator space as an unspecified dual.

**Problem.** For the diagonal action \((\alpha_t x)_n=e^{int}x_n\) on \(\ell^\infty(\mathbb N)\), identify \(\mathcal B_\alpha\) and explain why its unitization has one more character than \(\mathcal B_\alpha\).

**Solution.** AF0 proves the actual dual and predual-continuity hypotheses. Each \(\alpha_f\) is the diagonal multiplier \((f(n))_n\), and \(f\in A(\mathbb R)\subset C_0(\mathbb R)\) makes this sequence tend to zero. Local Fourier cutoffs produce each finite coordinate projection, so their norm-closed span is all diagonal \(c_0(\mathbb N)\). Its characters are coordinate evaluations: a nonzero continuous character is nonzero on some coordinate projection by finite-support density; idempotency makes its value there one, and orthogonality makes its values on all other projections zero. Density then gives exactly that coordinate evaluation. The unitization adds the character that vanishes on \(c_0\) and evaluates the adjoined scalar part; this extra character is not an action frequency. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Corollary XI.1.15, printed page 324 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The convolution-character proof, nonunital norm bound, exact frequency correspondence and both topologies are established above. The unitized scalar character is distinguished from the character space of the original filter algebra.
