# An isometry with one spectral value

An isometry can fail to be onto, so its norm-preserving property alone does not make it a group action. If its ordinary operator spectrum is exactly \(\{1\}\), invertibility supplies the missing negative powers. Passing to the bidual then lets the action-spectrum and singleton-frequency results apply to an arbitrary Banach space. This proves Takesaki II, Corollary XI.1.14 without assuming the original space is a dual.

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

<a id="oa-flow.frequency.singletonisometry"></a>

<a id="OA-FLOW.ISOM.INVERTIBLE"></a><a id="oa-flow.isom.invertible"></a>

## The spectral hypothesis supplies negative powers

Let \(X\ne\{0\}\) be a complex Banach space and let \(S:X\to X\) be a bounded linear operator satisfying \(\|Sx\|=\|x\|\) for every \(x\). Assume

<a id="equation-r1"></a>

$$\operatorname{Sp}_{\mathcal B(X)}(S)=\{1\}.\tag{R1}$$

Since \(0\) is outside the spectrum, \(S\) is invertible. It is therefore a surjective isometry, and its inverse is an isometry as well. Consequently

<a id="equation-r2"></a>

$$\|S^n\|=1\quad(n\in\mathbb Z),\qquad
\gamma_n:=S^n\text{ defines a uniformly bounded action of }\mathbb Z.\tag{R2}$$

The negative powers in (R2) would not be available for a proper isometric embedding. The spectrum assumption is what rules that case out.

<a id="OA-FLOW.ISOM.BIDUAL"></a><a id="oa-flow.isom.bidual"></a>

## The bidual makes the action eligible

The action \(\gamma\) on \(X\) need not be a dual Banach action. Instead set \(Y=X^{**}=(X^*)^*\) with its specified predual \(X^*\), and define \(\widetilde\gamma_n=(S^{**})^n\). Each operator is weak-star continuous, and its preadjoint is \((S^*)^n\). Because \(\mathbb Z\) is discrete, every predual orbit is norm continuous. Equation (R2) bounds all positive and negative powers. Thus \(\widetilde\gamma\) meets the exact specified-dual hypotheses of [AF0](OA-FLOW-AF.md#af-0), [BS0](OA-FLOW-BS.md#bs-0), and [the individual-operator proof](OA-FLOW-L89.md#oa-flow.frequency.operator). The norming-functional and separation statements used below are proved in [CF1](OA-FLOW-CF.md#oa-flow.cf.1).

The bidual does not add spectral values to a bounded operator:

<a id="equation-r3"></a>

$$\operatorname{Sp}_{\mathcal B(X^{**})}(S^{**})
=\operatorname{Sp}_{\mathcal B(X)}(S)=\{1\}.\tag{R3}$$

For completeness, an operator \(T-\lambda I\) is invertible exactly when its Banach adjoint is invertible. One direction follows by taking adjoints of an inverse. Conversely, if \((T-\lambda I)^*\) is invertible, then \(T-\lambda I\) is bounded below: for every \(x\), duality and the inverse-adjoint bound give \(\|x\|\le\|((T-\lambda I)^*)^{-1}\|\,\|(T-\lambda I)x\|\). Its range is therefore closed. The adjoint's injectivity makes the range dense by Hahn–Banach, so the range is all of \(X\). Apply this equivalence twice to get (R3).

<a id="OA-FLOW.ISOM.RIGIDITY"></a><a id="oa-flow.isom.rigidity"></a>

## The singleton action spectrum fixes every vector

The dual of \(\mathbb Z\) is \(\mathbb T\), with \((n,z)=z^n\). Formula (O9) of the earlier individual-operator proof, applied at \(n=1\), and (R3) yield

<a id="equation-r4"></a>

$$\operatorname{Sp}(\widetilde\gamma)=\{1\}.\tag{R4}$$

Indeed the action spectrum is closed in \(\mathbb T\), so the closure in (O9) adds no point when evaluation at \(1\in\mathbb Z\) is the identity map on \(\mathbb T\). Every \(y\in X^{**}\) has vector spectrum contained in the action spectrum. The complete Banach singleton theorem [BS5](OA-FLOW-BS.md#bs-5), reflected by AF0 to the positive convention, therefore gives \(\widetilde\gamma_n y=1^n y=y\). In particular \(S^{**}=I_{X^{**}}\). The canonical embedding \(J:X\hookrightarrow X^{**}\) intertwines \(S\) and \(S^{**}\), so

<a id="equation-r5"></a>

$$J(Sx)=S^{**}Jx=Jx\quad\Longrightarrow\quad Sx=x
\quad(x\in X).\tag{R5}$$

Hence \(S=I_X\). \(\square\)

**Problem.** Why does the unilateral right shift on \(\ell^2(\mathbb N)\) not contradict this result?

**Solution.** It preserves norms but is not onto, so \(0\) belongs to its operator spectrum. It fails (R1), and no inverse powers exist on the given space. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Corollary XI.1.14, printed page 324 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The retained proof supplies invertibility, both-sign powers, adjoint spectral equality and the full arbitrary-Banach-to-bidual passage. Its singleton input is the actual BS5 proof, rather than a broader spectral-transfer or action-recovery theorem.
