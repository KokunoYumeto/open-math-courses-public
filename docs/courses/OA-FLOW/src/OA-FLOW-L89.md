# The spectrum of one action operator

The action spectrum lives in the dual group, while the ordinary spectrum of one operator \(\alpha_s\) lives in the complex plane. Evaluating characters at \(s\) gives the connection, but its image may need closure. This lesson proves Takesaki II, Lemma XI.1.13 for the uniformly bounded dual Banach action of [AF0](OA-FLOW-AF.md#af-0). The proof keeps the finite-measure sign from [the four-tests proof](OA-FLOW-L88.md#oa-flow.frequency.tests) and uses local annihilation instead of assuming spectral synthesis for an arbitrary closed set.

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

<a id="oa-flow.frequency.operator"></a>

<a id="OA-FLOW.OPSP.CIRCLE"></a><a id="oa-flow.opsp.circle"></a>

## Two-sided powers and approximate eigenvalues

Fix \(s\in G\) and suppose \(X\ne\{0\}\). Write \(U=\alpha_s\) and \(C_\alpha=\sup_{t\in G}\|\alpha_t\|<\infty\). The group law gives

<a id="equation-o1"></a>

$$U^n=\alpha_{ns},\qquad \|U^n\|\le C_\alpha\quad(n\in\mathbb Z).\tag{O1}$$

For \(|\lambda|>1\), the series \(\lambda^{-1}\sum_{n\ge0}\lambda^{-n}U^n\) is a norm-convergent inverse of \(\lambda I-U\). For \(|\lambda|<1\), the series \(\sum_{n\ge0}\lambda^n U^{-(n+1)}\) is a norm-convergent inverse of \(U-\lambda I\). Thus

<a id="equation-o2"></a>

$$\operatorname{Sp}_{\mathcal B(X)}(U)\subset\mathbb T.\tag{O2}$$

This uses both positive and negative power bounds; \(U\) need not be an isometry in the given norm. If \(p\in\operatorname{Sp}(\alpha)\), the approximate-character net of [the four-tests proof](OA-FLOW-L88.md#oa-flow.frequency.tests) satisfies \(\|(U-(s,p)I)x_i\|\to0\) with \(\|x_i\|=1\). An invertible operator is bounded below, so \((s,p)\in\operatorname{Sp}_{\mathcal B(X)}(U)\). Since the latter set is closed,

<a id="equation-o3"></a>

$$K_s:=\overline{\{(s,p):p\in\operatorname{Sp}(\alpha)\}}^{\mathbb C}
\subset\operatorname{Sp}_{\mathcal B(X)}(U).\tag{O3}$$

<a id="OA-FLOW.OPSP.RECIPROCAL"></a><a id="oa-flow.opsp.reciprocal"></a>

## A smooth reciprocal on the circle

For the reverse inclusion take \(\lambda\in\mathbb T\setminus K_s\). The closed set \(K_s\subset\mathbb T\) is compact. Choose a smooth function \(F\) on the circle that agrees with \(z\mapsto(z-\lambda)^{-1}\) on an open neighborhood \(V\) of \(K_s\). A smooth cutoff supported away from \(\lambda\), equal to one near \(K_s\), gives such an \(F\). Its Fourier coefficients are absolutely summable; for example, two integrations by parts bound their magnitudes by a constant times \((1+|n|)^{-2}\). The explicit smooth reciprocal, normalized circle measure, coefficient estimate and full Fourier reconstruction are proved in [AF3](OA-FLOW-AF.md#af-3), using the complete earlier scalar CC0 basis. Hence

<a id="equation-o4"></a>

$$F(z)=\sum_{n\in\mathbb Z}a_nz^n,\qquad
\sum_{n\in\mathbb Z}|a_n|<\infty,\qquad
T:=\sum_{n\in\mathbb Z}a_nU^n\in\mathcal B(X).\tag{O4}$$

The operator series converges in norm by (O1). It commutes with \(U\). The intended identity is \((U-\lambda I)T=I\); proving it from values of \(F\) at spectral characters needs a local argument, because pointwise vanishing on \(\operatorname{Sp}(\alpha)\) alone does not imply an arbitrary Fourier filter annihilates the action.

<a id="OA-FLOW.OPSP.MEASURE-SIGN"></a><a id="oa-flow.opsp.measure-sign"></a>

## The atomic measure has a negative group sign

With the convention \(\alpha_\mu x=\int_G\alpha_{-t}x\,d\mu(t)\) from (F2), [AF1](OA-FLOW-AF.md#af-1) proves that the absolutely summable atomic series is a finite regular measure, and its Dirac translation law shows that the finite measure representing \(T\) is

<a id="equation-o5"></a>

$$\mu=\sum_{n\in\mathbb Z}a_n\delta_{-ns},\qquad
\alpha_\mu=T,\qquad
\widehat\mu(p)=F((s,p)).\tag{O5}$$

The series converges in total-variation norm, even if different integers give the same group element. Put \(\nu=(\delta_{-s}-\lambda\delta_0)*\mu\). Convolution and the group law give

<a id="equation-o6"></a>

$$\alpha_\nu=(U-\lambda I)T,
\qquad\widehat\nu(p)=((s,p)-\lambda)F((s,p)).\tag{O6}$$

In particular \(\widehat\nu=1\) on the open neighborhood \(\{p:(s,p)\in V\}\) of \(\operatorname{Sp}(\alpha)\). The negative signs in the point masses are forced by the negative parameter in \(\alpha_\mu\); positive point masses would represent powers of \(U^{-1}\) instead.

<a id="OA-FLOW.OPSP.LOCAL-IDENTITY"></a><a id="oa-flow.opsp.local-identity"></a>

## A local measure identity without synthesis

Here is the precise fact needed in (O6). If \(\rho\) is a finite complex regular measure and \(\widehat\rho=1\) on an open neighborhood \(W\) of \(E=\operatorname{Sp}(\alpha)\), then \(\alpha_\rho=I\).

To prove it, take \(f=\mathcal Fa\in A_c(H)\). [AF1](OA-FLOW-AF.md#af-1) proves the measure-module relation by a norm-continuous \(L^1(G)\)-valued translation integral and the bounded integrated-action map; no unrestricted product-measure or product-Borel identity is needed:

<a id="equation-o7"></a>

$$\alpha_\rho\alpha_f=\alpha_{\widehat\rho f}.\tag{O7}$$

The product \(h=(\widehat\rho-1)f\) belongs to \(A(H)\): equation (AF8) explicitly constructs its \(L^1\) kernel by the complete vector integral \(\int L_{-t}a\,d\rho(t)\), and subtracts \(a\). It has compact support inside \(\operatorname{supp}f\), and it vanishes on \(W\). Consequently \(\operatorname{supp}h\cap E=\varnothing\). The proved minimal local ideal inclusion LF6 puts \(h\in I(\alpha)\), so (O7) gives \(\alpha_\rho\alpha_f=\alpha_f\). LF5’s norm density extends this identity from \(A_c(H)\) to every \(f\in A(H)\). The span of the filtered vectors is weak-star dense by BS2, and both \(\alpha_\rho\) and \(I\) are normal. They therefore agree on all of \(X\):

<a id="equation-o8"></a>

$$\widehat\rho=1\text{ near }\operatorname{Sp}(\alpha)
\quad\Longrightarrow\quad\alpha_\rho=I.\tag{O8}$$

The neighborhood condition is essential to this argument. It ensures a compactly supported test function in the *minimal local ideal*; no equality between that ideal and the full vanishing ideal has been used.

<a id="OA-FLOW.OPSP.FORMULA"></a><a id="oa-flow.opsp.formula"></a>

## The operator-spectrum formula

Apply (O8) to \(\rho=\nu\). Equations (O5)–(O6) give \((U-\lambda I)T=I\). Since \(T\) is a norm-convergent series of powers of \(U\), it commutes with \(U\), so also \(T(U-\lambda I)=I\). Thus every \(\lambda\in\mathbb T\setminus K_s\) is resolvent. Values off the circle were already excluded in (O2), and (O3) supplies the other inclusion. We have proved

<a id="equation-o9"></a>

$$\boxed{\operatorname{Sp}_{\mathcal B(X)}(\alpha_s)
=\overline{\{(s,p):p\in\operatorname{Sp}(\alpha)\}}^{\mathbb C}.}\tag{O9}$$

The theorem holds also for the ordinary Banach setting (B). AF1 constructs its full finite-measure norm integral and the same measure-module relation. In the last step of (O8), the filtered span is norm dense by BS2 and the operators are bounded, so equality passes to all vectors in norm. All other steps and constants are unchanged.

**Problem.** On \(X=\ell^\infty(\mathbb N)\), with predual \(\ell^1(\mathbb N)\), let \((\alpha_t x)_n=e^{int}x_n\) for \(t\in\mathbb R\). If \(s/(2\pi)\) is irrational, identify the spectrum of \(\alpha_s\).

**Solution.** Every coordinate vector has action frequency \(n\), so \(\{n:n\in\mathbb N\}\subset\operatorname{Sp}(\alpha)\). The values \(e^{ins}\) are dense in \(\mathbb T\) by the elementary irrational-rotation proof in [AF3](OA-FLOW-AF.md#af-3). The diagonal action has the actual \(\ell^1\) predual and norm-continuous predual orbits by AF0. Formula (O9) and (O2) therefore give \(\operatorname{Sp}_{\mathcal B(X)}(\alpha_s)=\mathbb T\). The example shows why the closure in (O9) cannot be dropped. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Lemma XI.1.13, printed page 323 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). Both-sign power bounds give (O2) for a uniformly bounded action. Under (F2), the negative atomic signs in (O5)–(O6) represent powers of \(U\); positive signs would represent inverse powers. The actual scalar Fourier and measure-module proofs are supplied above. No arbitrary closed-set synthesis is used.
