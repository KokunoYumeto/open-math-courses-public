# Weighted Sobolev spaces and rough elliptic estimates

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Does the order of a spatial weight and a derivative matter?** Multiplication by \(\langle x\rangle^t\) and the Fourier multiplier \(\langle D\rangle^s\) generally do not commute. Even for integer derivatives the product rule produces lower-order terms. The norm-equivalence theorem controls these terms for all real exponents and then applies the resulting scale to the actual rough elliptic graph.

A Sobolev norm measures derivatives; a spatial weight measures behavior at infinity. Scattering problems need both at once. The position weight and the Fourier multiplier usually do not commute, so a definition must specify their order and prove that exchanging them gives an equivalent norm. After doing this for every real pair of exponents, we show that an elliptic graph estimate survives multiplication by a polynomial weight even when the operator has rough coefficients.

Read [The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md) for the unweighted graph estimate and its precise coefficient class, and [Admissible differential perturbations](admissible-differential-perturbations.md) for the local multiplication estimates. For the smooth symbol calculus we use the complete programme proof [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md). It supplies the symbol estimates, distribution identities and uniform finite remainders for the exact metric below. Fourier inversion, Plancherel, Schwartz density and the needed measure interchanges are proved in [A finite-derivative bound for left quantization](../providers/analysis/finite-derivative-l2.md#fourier-normalization). The particular calculus interfaces are identified in Section 2. See also Lerner [L].

Write \(D_j=-i\partial_j\), \(\langle x\rangle=(1+|x|^2)^{1/2}\), and

\[
 M_tu=\langle x\rangle^t u,\qquad
 J_su=\langle D\rangle^s u,\qquad s,t\in\mathbb R.
 \tag{1}
\]

The Fourier transform has kernel \(e^{-ix\cdot\xi}\). Thus \(J_s\) is multiplication by \(\langle\xi\rangle^s\) on the Fourier side, and \(H^s\) has norm \(\|J_su\|_2\).

## 1. Measuring derivatives and decay

**Definition 1.1.** For arbitrary real \(s,t\), let

\[
 H^{s,t}(\mathbb R^n)
 =\{u\in\mathcal S'(\mathbb R^n):M_tJ_su\in L^2\},
 \qquad \|u\|_{s,t}=\|M_tJ_su\|_2.
 \tag{2}
\]

Here \(s\) measures differentiability and \(t\) measures spatial decay. Positive \(t\) demands more decay; negative \(t\) permits more growth. The case \(t=0\) is \(H^s\), and the case \(s=0\) is weighted \(L^2\).

Both \(M_t\) and \(J_s\) are continuous automorphisms of \(\mathcal S\) and \(\mathcal S'\). For multiplication this follows from

\[
 |\partial^\gamma\langle x\rangle^t|
 \le C_{t,\gamma}\langle x\rangle^{t-|\gamma|}.
 \tag{3}
\]

To prove (3) for every real exponent, repeated differentiation produces a finite sum of terms \(c x^\nu(1+|x|^2)^{t/2-\ell}\) with \(2\ell-|\nu|=|\gamma|\). A derivative on the monomial reduces \(|\nu|\) by one; a derivative on the power increases \(\ell\) by one and \(|\nu|\) by one. Thus this identity holds inductively, and \(|x^\nu|\le\langle x\rangle^{|\nu|}\) proves (3).

The product rule controls every Schwartz seminorm; the same argument with \(-t\) gives the inverse. On the Fourier side it proves the assertion for \(J_s\). The distribution actions follow by transposition, or by Fourier transformation and multiplication. In particular,

\[
 (M_tJ_s)^{-1}=J_{-s}M_{-t}.
 \tag{4}
\]

This order is essential.

**Proposition 1.2.** The space \(H^{s,t}\), with the norm in (2), is a Hilbert space continuously embedded in \(\mathcal S'\). Schwartz functions are dense in it.

**Proof.** The map \(T=M_tJ_s\) sends the displayed space bijectively onto \(L^2\), with inverse (4), and is an isometry for its defining norm. Pull back the \(L^2\) inner product. Completeness follows: if \(Tu_j\) converges to \(v\) in \(L^2\), then \(u_j\) converges in the norm to \(T^{-1}v\). The embedding \(L^2\subset\mathcal S'\) is continuous by Cauchy–Schwarz against a Schwartz test, and \(T^{-1}\) is continuous on \(\mathcal S'\), giving the asserted embedding.

For density, approximate \(Tu\) in \(L^2\) by Schwartz functions \(v_j\). The functions \(T^{-1}v_j\) are Schwartz and converge to \(u\) in (2). No sign restriction on \(s\) or \(t\) entered this argument. \(\square\)

For a smooth power tail \(u(x)=\langle x\rangle^{-a}\),

\[
 u\in H^{0,t}
 \quad\Longleftrightarrow\quad a>t+\frac n2.
 \tag{5}
\]

Indeed its squared weighted radial integrand is comparable at infinity to \(r^{n-1+2(t-a)}\). Equality gives a logarithmically divergent integral. In particular a nondecaying function can lie in a sufficiently negatively weighted space. Problem 2 compares this threshold with integer Sobolev orders.

## 2. The metric and the exact calculus interfaces

For \(0<\delta\le1\), use the phase-space metric

\[
 G_{\delta,(x,\xi)}(y,\eta)
 =\langle x\rangle^{-2\delta}|y|^2
   +\langle\xi\rangle^{-2}|\eta|^2.
 \tag{6}
\]

For a positive weight \(w\), the scalar class \(S(w,G_\delta)\) consists of smooth symbols with

\[
 |\partial_x^\beta\partial_\xi^\alpha a(x,\xi)|
 \le C_{\alpha\beta}w(x,\xi)
       \langle x\rangle^{-\delta|\beta|}
       \langle\xi\rangle^{-|\alpha|}.
 \tag{7}
\]

This coordinate description agrees with the directional metric seminorms: test coordinate directions for one implication, and expand multilinear derivatives for the other. The constants at each derivative order involve only finitely many coordinate derivatives.

We check the metric conditions rather than infer them from (7). On phase space take
\(\sigma((x,\xi),(y,\eta))=\xi\cdot y-x\cdot\eta\). Quadratic duality gives

\[
 \begin{aligned}
 G_{\delta,(x,\xi)}^\sigma(y,\eta)
 &=\langle\xi\rangle^2|y|^2
  +\langle x\rangle^{2\delta}|\eta|^2,\\
 h_\delta(x,\xi)&=\langle x\rangle^{-\delta}\langle\xi\rangle^{-1}\le1.
 \end{aligned}
 \tag{8}
\]

Here \(h_\delta^2=\sup G_\delta/G_\delta^\sigma\). The metric has no mixed position–frequency terms, so it also satisfies the reflection condition used for changes of quantization.

**Lemma 2.1.** The metric \(G_\delta\) is slowly varying and symplectically temperate. Every weight

\[
 w_{\tau,\mu}(x,\xi)=\langle x\rangle^\tau\langle\xi\rangle^\mu,
 \qquad \tau,\mu\in\mathbb R,
 \tag{9}
\]

is locally comparable and symplectically temperate for this metric.

**Proof.** Suppose \(G_{\delta,X}(Y-X)\le r^2\), where \(X=(x,\xi)\), \(Y=(y,\eta)\) and \(r<1/2\). Then

\[
 |y-x|\le r\langle x\rangle^\delta\le r\langle x\rangle,\qquad
 |\eta-\xi|\le r\langle\xi\rangle.
 \tag{10}
\]

The Japanese bracket is one-Lipschitz. Each bracket at \(Y\), divided by the corresponding bracket at \(X\), therefore lies between \(1-r\) and \(1+r\). Raising these ratios to the fixed powers in (6) and (9) proves the local comparisons.

For the global condition put

\[
 Q_Y(X-Y)=G_{\delta,Y}^\sigma(X-Y).
 \tag{11}
\]

Since both coefficients in (8) are at least one, \(Q_Y(X-Y)\ge |X-Y|^2\). In each direction,

\[
 \frac{\langle x\rangle}{\langle y\rangle},
 \frac{\langle y\rangle}{\langle x\rangle},
 \frac{\langle\xi\rangle}{\langle\eta\rangle},
 \frac{\langle\eta\rangle}{\langle\xi\rangle}
 \le 1+|X-Y|\le C(1+Q_Y(X-Y))^{1/2}.
 \tag{12}
\]

Compare the two coefficients of \(G_{\delta,X}^\sigma\) with those of \(G_{\delta,Y}^\sigma\). Formula (12) bounds both ratios by a fixed power of \(1+Q_Y(X-Y)\). This is the required dual-form temperateness inequality. The same formula gives
\(w_{\tau,\mu}(Y)/w_{\tau,\mu}(X)\le C(1+Q_Y(X-Y))^N\)
for a finite \(N\), including negative \(\tau,\mu\). \(\square\)

The programme reading [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md#weights-and-symbols) proves the following interfaces for exactly this metric and all its locally comparable, symplectically temperate weights. It uses our Fourier normalization throughout.

1. Section 5 proves the continuous actions on \(\mathcal S\) and \(\mathcal S'\). Theorem 3.1 proves the exact quantization-change automorphism and inverse, so left and Weyl symbols give equivalent classes.
2. Theorem 4.1 and Section 5 prove the finite-seminorm left product in \(S(w_1w_2,G_\delta)\), its finite remainder in \(S(w_1w_2h_\delta^N,G_\delta)\), and its equality to operator composition on both spaces. Lemma 2.1 supplies the complete oscillatory estimates in all four near/far regions.
3. Section 6 applies the proved finite-derivative operator bound to \(S(1,G_\delta)\) and its quantization transforms. This gives the required \(L^2\) bounds with finite-seminorm control.

These are programme proofs, not inferences from the accessibility of a reference. Lerner [L], Lemma 2.3.12 and Theorems 2.3.18–2.3.19, gives the broader free-source formulas.

The constants depend on the fixed metric and weight comparison constants and the required finite seminorms. Thus bounded symbol families with common structural constants give uniform operator bounds. This uniformity will be needed for the truncated weights in Section 5. These interfaces concern smooth symbols; we will apply them to the weight operators, while treating rough coefficients by the separate multiplication estimate.

## 3. Exchanging the factors and mapping between spaces

**Theorem 3.1.** For every \(s,t\in\mathbb R\),

\[
 c_{s,t}\|M_tJ_su\|_2
 \le \|J_sM_tu\|_2
 \le C_{s,t}\|M_tJ_su\|_2.
 \tag{13}
\]

Each finite-norm condition implies the other, for \(u\in\mathcal S'\). Moreover, if a left symbol belongs to \(S(w_{\tau,\mu},G_\delta)\), then

\[
 a(x,D):H^{s,t}\longrightarrow H^{s-\mu,t-\tau}
 \quad\text{continuously}.
 \tag{14}
\]

All four exponents are arbitrary real numbers. The operator norm is bounded by finitely many symbol seminorms, with constants fixed by the exponents, metric and weight structure.

**Proof.** By (3), the symbols of \(M_t\) and \(J_s\) belong to
\(S(\langle x\rangle^t,G_\delta)\) and \(S(\langle\xi\rangle^s,G_\delta)\).
The composite operators

\[
 A=J_sM_tJ_{-s}M_{-t},\qquad
 B=M_tJ_sM_{-t}J_{-s}
 \tag{15}
\]

have symbols of weight one. The three interfaces therefore make them bounded on \(L^2\). Their algebraic identities on \(\mathcal S'\) are

\[
 \begin{aligned}
 J_sM_tu&=A(M_tJ_su),\\
 M_tJ_su&=B(J_sM_tu).
 \end{aligned}
 \tag{16}
\]

They prove both inequalities and both finite-norm implications. The bounded extensions agree with the distributional operators on \(L^2\): approximate in \(L^2\) by Schwartz inputs and use their continuous embeddings and distributional action.

For (14) conjugate by the defining isometries of the source and target:

\[
 C_a=M_{t-\tau}J_{s-\mu}\,a(x,D)\,J_{-s}M_{-t}.
 \tag{17}
\]

Its product weight is

\[
 \langle x\rangle^{t-\tau}\langle\xi\rangle^{s-\mu}
 \langle x\rangle^\tau\langle\xi\rangle^\mu
 \langle\xi\rangle^{-s}\langle x\rangle^{-t}=1.
 \tag{18}
\]

Consequently \(C_a\) is bounded on \(L^2\) with the asserted finite-seminorm control. Apply it to \(M_tJ_su\), and use (4), to obtain
\(\|a(x,D)u\|_{s-\mu,t-\tau}\le C\|u\|_{s,t}\).
Density, or the distributional identity in (17), gives the assertion on the whole space. \(\square\)

For example the left symbol \(\langle x\rangle^{-\rho}\langle\xi\rangle^\mu\) quantizes exactly as \(M_{-\rho}J_\mu\), and maps

\[
 H^{s,t}\longrightarrow H^{s-\mu,t+\rho}.
 \tag{19}
\]

Its decaying coefficient improves the permitted spatial weight by \(\rho\). This conclusion uses operator composition rather than a claim that the position and Fourier factors commute.

For nonnegative integer \(k\), the definition also has a familiar derivative form.

**Corollary 3.2.** For \(u\in\mathcal S'\),

\[
 \|u\|_{k,t}\asymp
 \sum_{|\alpha|\le k}\|\langle x\rangle^tD^\alpha u\|_2.
 \tag{20}
\]

In particular either side is finite exactly when the other is.

**Proof.** Set \(v=M_tu\). The ordinary integer Sobolev norm is equivalent to \(\sum_{|\alpha|\le k}\|D^\alpha v\|_2\), by Plancherel and comparison of \(\langle\xi\rangle^{2k}\) with the finite sum of \(|\xi^\alpha|^2\). Theorem 3.1 compares this norm with \(\|u\|_{k,t}\). In the distributional product rule every term of \(D^\alpha(M_tu)\) is a bounded smooth multiple of \(M_tD^\beta u\), \(|\beta|\le|\alpha|\), by (3). Conversely, expand \(M_tD^\alpha(M_{-t}v)\); all the ratios \(M_tD^\gamma\langle x\rangle^{-t}\) are bounded, so each resulting term is controlled by a derivative of \(v\). These finite expansions prove the two bounds, including the finite-norm implications. \(\square\)

**Corollary 3.3 (Fourier exchange of decay and regularity).** For every real \(s,t\), the unitary Fourier transform gives an isomorphism

\[
 \mathcal F:H^{s,t}\longrightarrow H^{t,s}.
\]

**Proof.** On Schwartz inputs, Fourier inversion and the even bracket multipliers give
\(\mathcal F^{-1}M_s\mathcal F=J_s\) and
\(\mathcal F^{-1}J_t\mathcal F=M_t\). Consequently

\[
 \|\mathcal Fu\|_{t,s}=\|J_sM_tu\|_2
                  \asymp\|M_tJ_su\|_2.
\]

Theorem 3.1 supplies the equivalence for every real pair, and the same argument for the inverse Fourier transform gives the reverse map. Density extends both maps and identifies them with the distributional Fourier transform. This proves the Fourier-exchange statement of [HJS], Proposition 3.10, with the factor order in our definition kept explicit. \(\square\)

## 4. The rough elliptic estimate

We retain the full scalar coefficient class from the preceding domain theorem. Let \(n,m\ge1\) be integers, \(P_0(D)\) a real constant-coefficient elliptic operator of order \(m\), and

\[
 P=P_0+\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha.
 \tag{21}
\]

The highest-order \(a_\alpha\) are continuous and tend to zero at infinity. For \(k=m-|\alpha|>0\), the lower coefficient belongs to \(L^{p_\alpha}_{\mathrm{loc}}\), where

\[
 p_\alpha=
 \begin{cases}
 n/k,&n>2k,\\
 \text{a fixed finite number greater than }2,&n=2k,\\
 2,&n<2k,
 \end{cases}
 \qquad
 \|a_\alpha\|_{L^{p_\alpha}(B(y,1))}\longrightarrow0
 \quad (|y|\to\infty).
 \tag{22}
\]

Assume that the perturbation is symmetric on compact smooth tests and that the total continuous principal symbol is elliptic. Local membership is explicit; the tail limit by itself would not supply it. The preceding theorem makes \(P\) self-adjoint with domain \(H^m\) and proves

\[
 \|v\|_{H^m}\le C_0(\|Pv\|_2+\|v\|_2),\qquad v\in H^m.
 \tag{23}
\]

**Theorem 4.1.** For every \(t\in\mathbb R\), if \(u\in H^m\) and the right side below is finite, then \(u\in H^{m,t}\) and

\[
 \|u\|_{m,t}\le C_t\bigl(\|Pu\|_{0,t}+\|u\|_{0,t}\bigr).
 \tag{24}
\]

The constant depends on the fixed operator and weight exponent. No derivatives of the rough coefficients and no prescribed rate of their decay are required.

This is an estimate on the known unweighted domain. It transfers a spatial weight from \(u\) and \(Pu\) to the highest derivatives. In particular it does not assert that every distributional solution already belongs to \(H^m\). We prove it using bounded weights whose estimates stay uniform as their truncation is removed.

## 5. Uniform bounds for the regularized weight

For \(0<\varepsilon\le1\), define

\[
 F_\varepsilon(x)=
 \frac{\langle x\rangle}{(1+\varepsilon|x|^2)^{1/2}},
 \qquad w_\varepsilon(x)=F_\varepsilon(x)^t.
 \tag{25}
\]

For each fixed \(\varepsilon\), \(1\le F_\varepsilon\le\varepsilon^{-1/2}\). Thus \(w_\varepsilon\) and its reciprocal are bounded smooth functions with bounded derivatives, though their zeroth-order bounds can depend on \(\varepsilon\). Also \(w_\varepsilon(x)\to\langle x\rangle^t\) pointwise as \(\varepsilon\downarrow0\).

**Lemma 5.1.** For every multi-index \(\gamma\),

\[
 \begin{aligned}
 |D^\gamma w_\varepsilon|&\le C_{t,\gamma}
     w_\varepsilon\langle x\rangle^{-|\gamma|},\\
 |D^\gamma w_\varepsilon^{-1}|&\le C_{t,\gamma}
     w_\varepsilon^{-1}\langle x\rangle^{-|\gamma|}.
 \end{aligned}
 \tag{26}
\]

uniformly for \(0<\varepsilon\le1\). The weights \(w_\varepsilon^{\pm1}\) have common local comparison and temperateness constants for \(G_1\).

**Proof.** Put \(b_\varepsilon=(1+\varepsilon|x|^2)^{1/2}\). For \(|\gamma|\ge1\), differentiation of \(\log\langle x\rangle\), followed by scaling \(x\mapsto\sqrt\varepsilon x\), gives

\[
 |\partial^\gamma\log b_\varepsilon(x)|
 \le C_\gamma\left(\frac{\varepsilon}{1+\varepsilon|x|^2}\right)^{|\gamma|/2}
 \le C_\gamma\langle x\rangle^{-|\gamma|}.
 \tag{27}
\]

For completeness the unscaled logarithmic estimate follows inductively by differentiating \(\tfrac12\log(1+|x|^2)\): its positive-order derivatives are finite sums of polynomials of degree at most twice the denominator power minus the derivative order, divided by powers of \(1+|x|^2\). Each term has the claimed decay. The last inequality in (27) uses
\(\varepsilon(1+|x|^2)\le1+\varepsilon|x|^2\).
The same bound holds for positive derivatives of
\(\log w_\varepsilon=t(\log\langle x\rangle-\log b_\varepsilon)\).
Repeatedly differentiate its exponential. Each resulting product of logarithmic derivatives has total derivative order \(|\gamma|\); division by \(w_\varepsilon\) leaves a bound \(C\langle x\rangle^{-|\gamma|}\). Apply the same argument to \(-\log w_\varepsilon\) for the reciprocal.

The function \(b_\varepsilon\) is \(\sqrt\varepsilon\)-Lipschitz, and
\(\sqrt\varepsilon\langle x\rangle\le b_\varepsilon(x)\).
If \(|y-x|\le r\langle x\rangle\), \(r<1/2\), the ratios of both
\(\langle y\rangle/\langle x\rangle\) and \(b_\varepsilon(y)/b_\varepsilon(x)\) lie between \(1-r\) and \(1+r\). This proves uniform local comparison. Globally each of these ratios, and its reciprocal, is at most \(1+|x-y|\). Hence

\[
 \frac{w_\varepsilon(y)}{w_\varepsilon(x)},
 \frac{w_\varepsilon(x)}{w_\varepsilon(y)}
 \le (1+|x-y|)^{2|t|}.
 \tag{28}
\]

The dual distance for \(G_1\) dominates \(|x-y|^2\), proving the uniform global condition. \(\square\)

The symbols \(w_\varepsilon\) and \(w_\varepsilon^{-1}\), independent of frequency, consequently form uniformly bounded families relative to their respective variable weights for \(G_1\). In the factor-exchange proof (15), replace \(M_t,M_{-t}\) by multiplication by these two functions. Their product weights still cancel to one, and all structural and normalized derivative constants remain uniform. Thus for each fixed \(s\),

\[
 \|w_\varepsilon J_su\|_2
 \asymp \|J_s(w_\varepsilon u)\|_2,
 \tag{29}
\]

with constants independent of \(\varepsilon\). The large possible supremum of \(w_\varepsilon\), or of its reciprocal, is not used in this bound.

## 6. Commutators without differentiating coefficients

**Lemma 6.1.** On \(H^m\),

\[
 \|[P,w_\varepsilon]w_\varepsilon^{-1}v\|_2
 \le C_t\|v\|_{H^{m-1}},
 \tag{30}
\]

where the expression on the left extends continuously to \(H^{m-1}\) and \(C_t\) is independent of \(\varepsilon\).

**Proof.** Include the constant coefficients of \(P_0\) among coefficients \(c_\alpha\) of \(P\). Since a scalar coefficient commutes with the weight, the product rule gives

\[
 \begin{aligned}
 &[c_\alpha D^\alpha,w_\varepsilon]w_\varepsilon^{-1}v\\
 &\quad=\sum_{0<\gamma\le\alpha}
 \binom{\alpha}{\gamma}c_\alpha(D^\gamma w_\varepsilon)
       D^{\alpha-\gamma}(w_\varepsilon^{-1}v).
 \end{aligned}
 \tag{31}
\]

Expand the last derivative. Every term has the form

\[
 \begin{gathered}
 C_{\alpha\gamma\eta}\,c_\alpha b_{\gamma\eta,\varepsilon}D^\beta v,\\
 b_{\gamma\eta,\varepsilon}
   =(D^\gamma w_\varepsilon)(D^\eta w_\varepsilon^{-1}),\\
 \beta=\alpha-\gamma-\eta.
 \end{gathered}
 \tag{32}
\]

By (26) its smooth ratio is uniformly bounded, in fact by
\(C\langle x\rangle^{-|\gamma|-|\eta|}\). Neither expansion differentiates \(c_\alpha\).

For a lower rough coefficient, with original gap \(k=m-|\alpha|>0\), the gap for \(D^\beta v\) under the \(H^{m-1}\) norm is

\[
 k'=(m-1)-|\beta|=k-1+|\gamma|+|\eta|\ge k.
 \tag{33}
\]

The original \(L^{p_\alpha}\) assumption suffices at this larger gap. To check every endpoint, the multiplier exponent for gap \(k'\) is \(n/k'>2\) when \(n>2k'\), any fixed finite exponent greater than 2 when \(n=2k'\), and 2 when \(n<2k'\). In the first case \(n/k'\le p_\alpha\); in the second choose an exponent no larger than \(p_\alpha\), which is greater than 2 because \(k\le k'=n/2\); in the third use \(2\le p_\alpha\). Finite-volume inclusion on unit balls supplies each smaller local exponent. Multiplication by the bounded ratio in (32) preserves these bounds.

Local membership and the tail hypothesis in (22) give a finite uniform unit-ball norm: far centers are bounded by the tail limit, and balls with centers in a fixed compact set lie in one larger compact set. The global coefficient multiplier estimate from *Admissible differential perturbations*, Proposition 2.1, now bounds every such term \(H^{m-1}\to L^2\). Highest-order coefficients are bounded and \(|\beta|\le m-1\), so their terms are bounded directly by \(\|v\|_{H^{m-1}}\). The same direct argument handles all constant coefficients of \(P_0\).

If \(m=1\), only terms with \(|\alpha|=1\) contribute: the zeroth-order coefficients commute with the weight, and the remaining terms are bounded multipliers on \(L^2=H^0\). Thus this case does not require a positive-order multiplier theorem with order zero.

There are finitely many terms, all with uniform constants, proving (30). Initially the identities hold on compact smooth inputs. For fixed \(\varepsilon\), multiplication by \(w_\varepsilon^{\pm1}\) is continuous on \(H^m\), \(P:H^m\to L^2\) is continuous, and compact smooth functions are dense in \(H^m\). Passage to the limit proves the identity there. The term estimates also give its stated extension. \(\square\)

**Proof of Theorem 4.1.** Set \(v=w_\varepsilon u\). It belongs to \(H^m\) for every fixed \(\varepsilon\), and

\[
 Pv=w_\varepsilon Pu+[P,w_\varepsilon]w_\varepsilon^{-1}v.
 \tag{34}
\]

Apply (23) and Lemma 6.1 to obtain

\[
 \|v\|_{H^m}\le C_0\|w_\varepsilon Pu\|_2
               +C_1\|v\|_{H^{m-1}}+C_0\|v\|_2,
 \tag{35}
\]

with \(C_1\) independent of \(\varepsilon\). For any \(\eta>0\), splitting Fourier space at a sufficiently large fixed radius gives

\[
 \|v\|_{H^{m-1}}\le\eta\|v\|_{H^m}+C_\eta\|v\|_2.
 \tag{36}
\]

On the high-frequency part the ratio \(\langle\xi\rangle^{m-1}/\langle\xi\rangle^m\) is as small as needed; on the remaining ball \(\langle\xi\rangle^{m-1}\) is bounded. This also proves (36) for \(m=1\). Choose \(\eta\) so that \(C_1\eta\le1/2\) and absorb. Then (29), with \(s=m\), yields

\[
 \|w_\varepsilon J_mu\|_2
 \le C_t\bigl(\|w_\varepsilon Pu\|_2+\|w_\varepsilon u\|_2\bigr).
 \tag{37}
\]

All constants here precede the limit in \(\varepsilon\).

If \(t\ge0\), \(w_\varepsilon\le\langle x\rangle^t\), so the finite weighted right side gives integrable dominating squares. If \(t<0\), \(F_\varepsilon\ge1\) gives \(w_\varepsilon\le1\), and \(u,Pu\in L^2\) provide dominating squares. In both cases dominated convergence makes the right side of (37) tend to the right side of (24). Since \(J_mu\in L^2\), pointwise convergence of the weights and Fatou's inequality give

\[
 \|\langle x\rangle^tJ_mu\|_2
 \le\liminf_{\varepsilon\downarrow0}\|w_\varepsilon J_mu\|_2.
 \tag{38}
\]

This proves membership and (24). \(\square\)

Combined with (20), the theorem controls every weighted derivative through order \(m\). Only the smooth auxiliary weights were differentiated. The coefficient class stays exactly the one needed for the unweighted domain theorem.

### Use the conclusion

Compare the two orders of the weight and multiplier before applying a mapping theorem. Check that the rough graph estimate uses a known input regularity rather than assuming the conclusion being proved.

## 7. Graded exercises with complete solutions

**Exercise 1 — Basic: equivalent norms can differ.** Take \(s=t=2\). Compute the commutator of \(J_2=1-\Delta\) and \(M_2=1+|x|^2\). Show on a Schwartz function that factor-order equivalence does not mean equality of operators.

**Solution 1.** Apply the ordinary Laplacian product rule:

\[
 [J_2,M_2]u=-4x\cdot\nabla u-2nu.
 \tag{39}
\]

For \(u=e^{-|x|^2}\), \(\nabla u=-2xu\), so the right side is
\((8|x|^2-2n)e^{-|x|^2}\), which is not zero. Theorem 3.1 compares the two norms by bounded conjugated operators. It does not replace the product rule by commutation. The equality in (39) also makes explicit that the commutator has fewer derivatives than \(J_2\).

**Exercise 2 — Intermediate: a power tail at every integer order.** For real \(a,t\) and integer \(k\ge0\), determine exactly when \(u=\langle x\rangle^{-a}\) belongs to \(H^{k,t}\). Include the equality case.

**Solution 2.** For \(|\alpha|\le k\), (3) gives
\(|D^\alpha u|\le C_\alpha\langle x\rangle^{-a-|\alpha|}\).
If \(a>t+n/2\), all these weighted derivatives are square integrable by radial integration, hence (20) gives \(u\in H^{k,t}\). Conversely, (20) requires its zeroth derivative to belong to weighted \(L^2\), whose exact condition is (5). At \(a=t+n/2\) the radial square integral behaves as \(\int_1^\infty r^{-1}\,dr\), so it diverges. Thus the threshold is the same for every nonnegative integer \(k\). This reflects the extra decay of derivatives of this particular smooth tail; it is not a statement about arbitrary oscillating functions.

**Exercise 3 — Intermediate: constants before a limit.** In one dimension compute \(\partial_x\log w_\varepsilon\). Prove that its bound is uniform in \(\varepsilon\), explain why the reciprocal has the same normalized derivative estimates, and decide which domination applies for positive and negative \(t\).

**Solution 3.** Direct differentiation of (25) gives

\[
 \partial_x\log w_\varepsilon
 =t\left(\frac{x}{1+x^2}-\frac{\varepsilon x}{1+\varepsilon x^2}\right)
 =\frac{t(1-\varepsilon)x}{(1+x^2)(1+\varepsilon x^2)}.
 \tag{40}
\]

Its absolute value is at most \(|t|\langle x\rangle^{-1}\).
Higher logarithmic derivatives have the uniform bound (27), for both terms in the difference. Differentiating an exponential expresses
\(w_\varepsilon^{-1}\partial_x^j w_\varepsilon\) as a finite sum of products of these derivatives, with total order \(j\). Replacing \(t\) by \(-t\) proves the reciprocal assertion.

Since \(1\le F_\varepsilon\le\langle x\rangle\), positive \(t\) gives
\(w_\varepsilon\le\langle x\rangle^t\), while negative \(t\) gives
\(w_\varepsilon\le1\). The former uses the assumed weighted norms of \(u,Pu\) for domination; the latter uses their already known unweighted \(L^2\) norms. The possibly large supremum of \(w_\varepsilon^{-1}\) for negative \(t\) is irrelevant to the normalized estimates and factor exchange.

**Exercise 4 — Advanced: a rough coefficient loses no derivatives.** In dimension four let \(a\in L^4_{\mathrm{loc}}\) have finite uniform unit-ball \(L^4\) norm. It is a possible coefficient of \(D_1^2\) in an order-three operator. Expand
\([aD_1^2,w_\varepsilon]w_\varepsilon^{-1}v\), and prove that it is bounded from \(H^2\) to \(L^2\) uniformly in \(\varepsilon\), without any derivative of \(a\).

**Solution 4.** The expansion is

\[
 2a(D_1w_\varepsilon)w_\varepsilon^{-1}D_1v
 +a\left((D_1^2w_\varepsilon)w_\varepsilon^{-1}
       +2(D_1w_\varepsilon)(D_1w_\varepsilon^{-1})\right)v.
 \tag{41}
\]

The ratios are uniformly bounded by (26). The first term uses one derivative of \(v\), with remaining gap one under the \(H^2\) norm. In dimension four the required coefficient exponent is \(4/1=4\), exactly the given one. For the zeroth-derivative term the remaining gap is two, the critical case \(n=2k'\); a finite exponent greater than 2 is allowed, so choose 4 again. The uniform local multiplication estimate therefore controls each term by a constant times \(\|v\|_{H^2}\). Equivalently its local Hölder step pairs \(a\in L^4\) with the respective local \(L^4\) functions \(D_1v\) and \(v\), and its partition argument sums the estimates. No coefficient derivative appears: \(a\) multiplies the product-rule expansion on the left. The larger gap in the second term only improves the available embedding.

**Exercise 5 — Advanced: a spectral parameter and the indispensable lower norm.** Under Theorem 4.1 suppose \(u\in H^m\) and \((P-z)u=f\), with \(f,u\in H^{0,t}\). Derive a weighted estimate for \(u\), uniform for \(z\) in a fixed bounded set. Show that a term controlling \(u\) cannot generally be deleted, already for the unweighted Laplacian.

**Solution 5.** The equation gives \(Pu=f+zu\), so (24) implies

\[
 \|u\|_{m,t}
 \le C_t\bigl(\|f\|_{0,t}+(1+|z|)\|u\|_{0,t}\bigr).
 \tag{42}
\]

If \(|z|\le R\), the constant \(C_t(1+R)\) is uniform. This argument applies to real or complex \(z\); it does not assert an inverse or bound \(\|u\|_{0,t}\) by \(f\).

For necessity of the lower norm, take \(P=-\Delta\), \(t=0\), a nonzero \(\phi\in C_c^\infty\), and \(u_R(x)=R^{-n/2}\phi(x/R)\). Change of variables gives

\[
 \|u_R\|_2=\|\phi\|_2,\qquad
 \|Pu_R\|_2=R^{-2}\|\Delta\phi\|_2,\qquad
 \|u_R\|_{H^2}\ge\|\phi\|_2.
 \tag{43}
\]

Let \(R\to\infty\). A bound \(\|u\|_{H^2}\le C\|Pu\|_2\) would contradict these identities. The graph estimate retains its \(L^2\) term because it controls frequencies near zero as well as the elliptic high-frequency part.

## 8. Reading and further directions


[L] Nicolas Lerner, [*Metrics on the Phase Space and Non-Selfadjoint Pseudo-Differential Operators*, chapter on phase-space metrics](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), explains the metric calculus and the role of uncertainty and temperateness. Its quantization conventions should be compared with the \(D=-i\partial\) convention here. The linked course prerequisites give the precise interfaces used in this proof.

[A] Shmuel Agmon, [*Spectral properties of Schrödinger operators and scattering theory*](https://www.numdam.org/item/ASNSP_1975_4_2_2_151_0/), 1975, Appendix A, Lemma A.3, equations (A.16)–(A.19), gives the constant-coefficient weighted-commutator proof. Sections 5–6 supply the rough-coefficient extension without differentiating those coefficients.

[K] Shige Toshi Kuroda, [*Scattering theory for differential operators, II*](https://www.jstage.jst.go.jp/article/jmath1948/25/2/25_2_222/_pdf/-char/en), 1973, §2.4, uses a positive constant-coefficient form reference and a weighted derivative factor. Its bounded, strongly elliptic form coefficients are a different class from (21)–(22); the rough graph proof here supplies that distinction.

[AT] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), Theorem 2.A, states the smooth weighted mapping rule without giving its proof. Theorem 3.1 above proves the factor exchange and mapping rule on every real scale using the complete programme calculus proof; Sections 5–6 then treat the additional rough coefficients.

[HJS] Andrew Hassell, Qiuye Jia and Ethan Sussman, [*Lecture notes on non-elliptic Fredholm theory*, arXiv:2604.18956v1](https://arxiv.org/abs/2604.18956v1), Propositions 3.10–3.11, gives Fourier exchange and all-real mapping in the smooth scattering calculus. Corollary 3.3 integrates the former, while our metric proof and rough commutator argument handle the additional coefficient class.

The next question is how much differentiability can be recovered from a distributional solution away from its energy surface. The weighted mapping theorem supplies the norm estimates for a smooth inverse symbol. To allow an arbitrary initial spatial weight in the error term, a parametrix must have a remainder rapidly decreasing in both position and frequency. The present lesson proves the weighted scale and rough graph estimate; construction of that inverse and the estimates near the energy surface require further work.
