# Outgoing flux and vanishing shell mass

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Can a flux observation force every persistent derivative tail to vanish?** The normalized amplitude uses free velocity, while the forcing pairing determines the imaginary flux. A radial commutator connects them. If that flux is zero, positivity removes the persistent shell part, but the argument must still transfer this conclusion to every derivative through the operator's full order.

An outgoing solution can carry a fixed amount of mass per unit radius. The equation determines that amount: after the wave amplitude is normalized by its free velocity, the limiting mass is the imaginary part of the forcing pairing. We prove this identity for a long-range differential perturbation with rough coefficients. Zero flux then forces every derivative through the operator's order into the vanishing shell space.

Use [Admissible differential perturbations](admissible-differential-perturbations.md) for the full coefficient class and [The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md) for its realization. [Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md) gives the weighted norms and smooth maps. [Combining the long-range resolvent estimates](combining-the-long-range-resolvent-estimates.md) proves the rough short-range map and symmetric split. [The resolvent away from the energy surface](the-resolvent-away-from-the-energy-surface.md) supplies off-energy regularity. The shell maps are in [A resolvent estimate at noncritical frequencies](a-resolvent-estimate-at-noncritical-frequencies.md), and the closure and full-order symbol action are in [Radiation for limits of long-range resolvents](radiation-for-limits-of-long-range-resolvents.md). The programme reading [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md) proves the exact finite products, adjoints, complete remainders and common distributional action used here. Agmon [A], Proposition 4.B, supplies the freely readable radial-flux construction to compare with; Sections 3–8 prove the rough pairing, exact symbol normalization and every-derivative conclusion. Teschl [T] gives spectral context.

We use left quantization, \(D=-i\partial\), and an inner product linear in its first entry. Write

\[
 \begin{gathered}
 X=\langle x\rangle,\qquad \Xi=\langle\xi\rangle,\\
 \|w\|_{s,t}=\|X^t\langle D\rangle^s w\|_2,\\
 G_1=X^{-2}|dx|^2+\Xi^{-2}|d\xi|^2.
 \end{gathered}
 \tag{1}
\]

Thus \(S(\Xi^k,G_1)\) has bounds
\(|\partial_x^\alpha\partial_\xi^\beta a|
\le C_{\alpha\beta}X^{-|\alpha|}\Xi^{k-|\beta|}\).

## 1. The precise outgoing assumption

Use \(A_0=\{|x|<1\}\), \(A_j=\{2^{j-1}\le|x|<2^j\}\), and \(R_j=2^j\). The endpoint norms are

\[
 \begin{aligned}
 \|f\|_B&=\sum_{j\ge0}R_j^{1/2}\|f\|_{L^2(A_j)},\\
 \|u\|_{B^*}&=\sup_{j\ge0}R_j^{-1/2}\|u\|_{L^2(A_j)}.
 \end{aligned}
 \tag{2}
\]

Their integral pairing is absolutely convergent. The closure of Schwartz space in \(B^*\) is \(\dot B^*\), characterized by

\[
 \begin{gathered}
 g\in\dot B^*
 \ \Longleftrightarrow\
 R_j^{-1}\|g\|_{L^2(A_j)}^2\longrightarrow0\\
 \Longleftrightarrow\
 R^{-1}\int_{|x|<R}|g|^2\,dx\longrightarrow0.
 \end{gathered}
 \tag{3}
\]

These [closure equivalences](radiation-for-limits-of-long-range-resolvents.md#radiation-shell-closure) include the inner shell and every real radius.

Let \(P_0(D)\) be real, scalar, constant-coefficient and elliptic of integer order \(m\ge1\). Let \(V\) be a symmetric \(1\)-admissible perturbation, with its full sharp local coefficient hypotheses. Its self-adjoint realization \(H=P_0+V\) has domain \(H^m\). Fix a regular free energy \(\lambda\), and put

\[
 \begin{gathered}
 M_\lambda=\{\xi:P_0(\xi)=\lambda\},\qquad
 v(\xi)=\nabla P_0(\xi),\\
 N_+(M_\lambda)
 =\{(t\,v(\xi),\xi):\xi\in M_\lambda,\ t>0\}.
 \end{gathered}
 \tag{4}
\]

Regular means \(v\ne0\) on the energy shell. The shell is compact and may be empty.

<a id="flux-theorem"></a>
The outgoing-flux identity below is Hörmander [H4, Theorem 30.2.7].

**Theorem 1.1 (outgoing flux).** Suppose

\[
 \begin{gathered}
 D^\alpha u\in B^*,\qquad |\alpha|\le m,\\
 (H-\lambda)u=f\in B,
 \end{gathered}
 \tag{5}
\]

where the equation uses the actual local coefficient products. Assume also that

\[
 \begin{gathered}
 h\in S(\Xi^m,G_1),\qquad h|_{N_+(M_\lambda)}=0\\
 \Longrightarrow\quad h(x,D)u\in\dot B^*.
 \end{gathered}
 \tag{6}
\]

For every \(a\in S(\Xi^m,G_1)\) satisfying

\[
 \begin{gathered}
 |a(x,\xi)|^2=\frac{x}{|x|}\cdot v(\xi)\\
 \text{on }N_+(M_\lambda)
 \text{ for sufficiently large }|x|,
 \end{gathered}
 \tag{7}
\]

we have

\[
 \begin{gathered}
 \lim_{R\to\infty}R^{-1}
       \int_{|x|<R}|a(x,D)u|^2\,dx\\
 =2\operatorname{Im}(u,f)\ge0.
 \end{gathered}
 \tag{8}
\]

The hypothesis is directional radiation of the solution itself. The graph-limit theorem gives (6) for the limits it treats. The present theorem does not require a particular approximating graph.

The zero-flux conclusion is Hörmander [H4, Corollary 30.2.8].

**Corollary 1.2 (zero flux).** If the hypotheses hold and \(\operatorname{Im}(u,f)=0\), then

\[
 D^\alpha u\in\dot B^*,\qquad |\alpha|\le m.
 \tag{9}
\]

Every full-order action in the theorem already belongs to \(B^*\). To see this, use
\(S_m(\xi)=\sum_{|\alpha|\le m}\xi^{2\alpha}\asymp\Xi^{2m}\) and the finite identity

\[
 a(x,\xi)
 =\sum_{|\alpha|\le m}
       \frac{a(x,\xi)\xi^\alpha}{S_m(\xi)}\,\xi^\alpha.
 \tag{10}
\]

Each fraction is order zero. Right composition with \(D^\alpha\) is exact, so the shell maps and (5) control the action. This also identifies its distributional meaning.

## 2. Two small errors in shell space

We will use two elementary consequences of the compact-frequency calculus.

<a id="flux-shell-errors"></a>
**Lemma 2.1.** A compact-frequency symbol with bounded spatial output support sends \(B^*\) inputs into \(L^2\). Also, if \(r\) has position weight \(X^{-1}\) and arbitrary rapid frequency decay, its operator sends \(B^*\) inputs into \(L^2\).

**Proof.** In the first case its kernel, on the bounded output support, satisfies

\[
 |K(x,y)|\le C_N(1+|x-y|)^{-N}.
 \tag{11}
\]

An input shell of radius \(R_j\) has \(L^1\) norm at most
\(C R_j^{(n+1)/2}\|u\|_{B^*}\), by Cauchy–Schwarz and shell volume. Choose \(N>(n+1)/2\); the geometric sum converges uniformly on the bounded output. The output is therefore in \(L^2\). These absolutely convergent integrals agree with the common distributional action, for example by truncation in a strict weighted \(L^2\) space.

For the second assertion, exact left multiplication gives

\[
 X\operatorname{Op}(r)=\operatorname{Op}(Xr).
 \tag{12}
\]

The right side is an order-zero shell map. On \(A_j\), \(j\ge1\), its endpoint bound yields

\[
 \|\operatorname{Op}(r)u\|_{L^2(A_j)}^2
 \le C R_j^{-1}\|u\|_{B^*}^2.
 \tag{13}
\]

The inner shell is bounded separately. Sum the geometric sequence \(R_j^{-1}\). This proves the \(L^2\) assertion. \(\square\)

An order-zero \(G_1\) shell map preserves \(\dot B^*\): it is bounded on \(B^*\) and sends Schwartz space into Schwartz space, hence into that closure. We use both statements on the same distributional actions.

<a id="flux-rough-pairing"></a>
## 3. The rough term has a real weighted pairing

Use the [symmetric split](combining-the-long-range-resolvent-estimates.md#combined-split) \(V=V_L+V_S\), with the compact smooth adjustment making \(P=P_0+V_L\) elliptic. Choose \(0<\delta\le1\) within the coefficient decay gaps. The smooth coefficients of \(V_L\) are \(O(X^{-\delta})\), with their full differentiated bounds. The [primary rough map](combining-the-long-range-resolvent-estimates.md#combined-primary-map) is

\[
 V_S:H^{m,t}\longrightarrow H^{0,t+1+\delta}
 \quad(t\in\mathbb R).
 \tag{14}
\]

It is consistent with the actual coefficient products. Fix

\[
 \begin{gathered}
 b=\frac12+\frac{\delta}{4},\qquad
 c=\frac{\delta}{4},\qquad
 \tau=\frac{1+\delta}{2},\\
 \frac12<b<\tau,\qquad b+c<\frac12+\delta.
 \end{gathered}
 \tag{15}
\]

The [strict endpoint embedding](combining-the-long-range-resolvent-estimates.md#combined-embeddings) and [integer derivative characterization](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-integer-derivatives) give \(u\in H^{m,-b}\). By (14),

\[
 V_Su\in H^{0,\,1+\delta-b}
       \subset H^{0,b}\cap B.
 \tag{16}
\]

The inclusion at weight \(b\) follows from \(1+\delta-b>b\). Thus the pairing is finite:

\[
 |(V_Su,u)|
 \le \|V_Su\|_{0,b}\|u\|_{0,-b}.
 \tag{17}
\]

Choose Schwartz \(u_k\to u\) in \(H^{m,-b}\). Their images converge in \(H^{0,1+\delta-b}\), hence in \(H^{0,b}\), and their inputs converge in \(H^{0,-b}\). The pairings converge by (17). Each approximant has real pairing by symmetry of the actual rough action. Consequently \((V_Su,u)\) is real.

Set \(f_0=f-V_Su\). We have

\[
 \begin{gathered}
 (P-\lambda)u=f_0\in B,\\
 \operatorname{Im}(u,f_0)=\operatorname{Im}(u,f).
 \end{gathered}
 \tag{18}
\]

This argument uses weighted Sobolev density. It does not presume that \(u\) is already in the closure \(\dot B^*\) or in the unweighted operator domain.

<a id="flux-radial-identity"></a>
## 4. The exact radial commutator

Take real smooth \(\psi\), compactly supported on the nonnegative half-line and equal one near zero. Define \(\psi_R(x)=\psi(|x|/R)\), \(R\ge1\). It is smooth at zero. Every positive position derivative has support in an annulus \(c_0R<|x|<C_0R\).

Local \(H^m\) membership of \(u\) justifies compactly supported integration by parts. Approximate a compact cutoff of \(u\) by smooth inputs, with the cutoff equal one near the support of \(\psi_R\) and its derivatives. Formal symmetry of the smooth differential expression gives

\[
 \begin{gathered}
 ([P,\psi_R]u,u)/i
 =2\operatorname{Im}(\psi_Ru,f_0),\\
 2\operatorname{Im}(\psi_Ru,f_0)
 \longrightarrow 2\operatorname{Im}(u,f).
 \end{gathered}
 \tag{19}
\]

All compact pairings use actual local \(L^2\) products. The limit follows from the absolutely summable \(B^*/B\) pairing tail.

For \(e_r=x/|x|\), exact polynomial Leibniz expansion yields

\[
 \begin{gathered}
 [P_0(D),\psi_R]/i\\
 =-R^{-1}\psi'(|x|/R)e_r\cdot v(D)+E_R^0.
 \end{gathered}
 \tag{20}
\]

The free error terms contain at least two cutoff derivatives. Their orders are at most \(m-2\), and their annular coefficients are \(O(R^{-2})\). This sum is empty for \(m=1\).

Write \(V_L=\sum_{|\alpha|\le m}A_\alpha(x)D^\alpha\). Its exact commutator contains terms
\(A_\alpha(D^\beta\psi_R)D^{\alpha-\beta}\), \(0<\beta\le\alpha\), with their multinomial constants. Their order is at most \(m-1\), and their coefficients have size \(O(X^{-\delta}R^{-1})\) on the annulus.

<a id="flux-differential-errors"></a>
Let \(E_R=E_R^0+[V_L,\psi_R]/i\). On its coefficient support, \(R^c\le C X^c\). The free coefficients have weight \(X^{c-2}\), contained in \(X^{c-1-\delta}\) since \(\delta\le1\). The long-range terms have the latter weight directly. The weighted integer derivative norm therefore gives the complete finite bound

\[
 \begin{gathered}
 \|R^c E_Ru\|_{0,\tau}
 \le C\|u\|_{m-1,-b},\\
 \tau=1+\delta-c-b>\frac12.
 \end{gathered}
 \tag{21}
\]

Its output embeds in \(B\). Pairing with \(u\in B^*\), we obtain

\[
 |(E_Ru,u)|
 \le C R^{-c}\|u\|_{m-1,-b}\|u\|_{B^*}
 \longrightarrow0.
 \tag{22}
\]

No rough coefficient is differentiated in this calculation. Equations (19)–(22) prove

\[
 \begin{gathered}
 2\operatorname{Im}(u,f)\\
 =\lim_{R\to\infty}
 -R^{-1}(\psi'(|x|/R)e_r\cdot v(D)u,u).
 \end{gathered}
 \tag{23}
\]

<a id="flux-off-energy"></a>
## 5. Replacing the velocity by an exact positive operator

First suppose \(M_\lambda\ne\varnothing\). Choose real compact smooth \(\chi\), with \(0\le\chi\le1\), equal one near the shell and supported where \(v\ne0\). Since \(f_0\in B\subset H^{0,1/2}\), the [real-parameter off-energy theorem](the-resolvent-away-from-the-energy-surface.md#off-energy-resolvent-estimate) gives

\[
 u_{\mathrm{off}}=(1-\chi(D)^2)u\in H^{m,1/2}.
 \tag{24}
\]

Apply that theorem with forcing indices \(s=0\), \(t=1/2\), and auxiliary indices \(s'=0\), \(t'=-b\). The required auxiliary norm \(\|u\|_{0,-b}\) is finite by the endpoint hypothesis. Its contribution to (23) vanishes: \(v(D)u_{\mathrm{off}}\in L^2\), the annular \(L^2\) norm of \(u\) is \(O(R^{1/2})\), and the pairing carries \(R^{-1}\).

<a id="flux-positive-operator"></a>
For the prescribed full-order symbol \(a\), put \(A=\operatorname{Op}(a\chi)\). Its symbol has compact frequency support and is order zero. Choose smooth radial \(\kappa\), zero on a sufficiently large fixed ball and one outside a larger ball. Choose its zero region so that (7) holds on the bundle wherever \(\kappa\ne0\). Define

\[
 \begin{aligned}
 \ell(x,\xi)&=\kappa(x)e_r\cdot v(\xi)\chi(\xi)^2,\\
 q(x,\xi)&=\kappa(x)
       \bigl(e_r\cdot v(\xi)-|a(x,\xi)|^2\bigr)\chi(\xi)^2.
 \end{aligned}
 \tag{25}
\]

The cutoffs remove the singularity at zero. The symbol \(q\) vanishes on the entire positive bundle. Thus \(\operatorname{Op}(q)u\in\dot B^*\) by (6).

Moreover, \(\ell-|a\chi|^2=q-(1-\kappa)|a\chi|^2\). The second term has bounded output support, so Lemma 2.1 sends its action into \(L^2\). The exact adjoint/product formula gives

\[
 \begin{gathered}
 A^*A=\operatorname{Op}(|a\chi|^2)+\operatorname{Op}(r),\\
 r\in S(X^{-1}\Xi^{-N},G_1)\quad\text{for every }N.
 \end{gathered}
 \tag{26}
\]

The scalar principal product is exact at leading order; every subsequent term loses at least one position power, and compact frequency support supplies every rapid frequency bound in the complete remainder. Lemma 2.1 puts its action into \(L^2\). Hence

\[
 (\operatorname{Op}(\ell)-A^*A)u\in\dot B^*.
 \tag{27}
\]

Multiplying this difference by \(\psi'(|x|/R)\), pairing with \(u\), and dividing by \(R\) gives a quantity tending to zero. Indeed the first factor has vanishing normalized annular norm, while the second has a uniformly bounded normalized norm. The closure condition in (3) controls annuli at all radii by adjacent dyadic shells. The fixed spatial modification \(\kappa\) is immaterial on the moving annulus. We may replace the velocity action in (23) by \(A^*A\).

<a id="flux-cutoff-commutator"></a>
## 6. Moving the cutoff through the adjoint

Put \(\theta_R=R^{-1}\psi'(|x|/R)\). The scalar principal symbols in the commutator cancel. For \(\rho=1/2\), the scaled multiplication symbol \(R^\rho\theta_R\) is uniformly in \(S(X^{\rho-1},G_1)\). Its derivative support is the moving annulus. The exact finite product theorem gives

\[
 \begin{gathered}
 R^\rho[\theta_R,A^*]A
 =\operatorname{Op}(s_R),\\
 s_R\text{ uniformly in }\\
 S(X^{\rho-2}\Xi^{-N},G_1)
 \\\text{for every }N.
 \end{gathered}
 \tag{28}
\]

The first surviving product has one position derivative of the cutoff and a frequency derivative of the adjoint symbol. Higher finite terms have stronger position decay. The exact remainder has that same stated bound, by taking the finite product order needed for a prescribed frequency seminorm. The adjoint symbol is rapidly decreasing in frequency. These observations account for the complete operator, on its common action.

Take \(b_0=3/4\). The weighted map sends \(H^{0,-b_0}\) to \(H^{0,\,2-\rho-b_0}=H^{0,3/4}\subset B\). Thus

\[
 \begin{gathered}
 |([\theta_R,A^*]Au,u)|\\
 \le C R^{-1/2}\|u\|_{0,-3/4}\|u\|_{B^*}
 \longrightarrow0.
 \end{gathered}
 \tag{29}
\]

<a id="flux-weighted-adjoint"></a>
We must also justify the adjoint pairing for each fixed \(R\). The operators \(A,A^*\) preserve every zeroth-order weighted space. Multiplication by \(\theta_R\), whose support is bounded for this fixed radius, maps \(H^{0,-b_0}\) into \(H^{0,b_0}\). Approximate \(u\) by Schwartz inputs in \(H^{0,-b_0}\). Their \(A\)-images converge in that space and locally in \(L^2\); their \(\theta_R A\)-images converge in \(H^{0,b_0}\). Passing the ordinary Schwartz adjoint identity to the weighted pairing gives

\[
 \begin{gathered}
 (A^*\theta_R Au,u)=(\theta_R Au,Au),\\
 (\theta_R A^*Au,u)
 =(\theta_R Au,Au)\\
 +([\theta_R,A^*]Au,u).
 \end{gathered}
 \tag{30}
\]

The left pairings are defined on the specified weights or compact support; they do not require \(u\in L^2\). Combining (23), (27) and (29)–(30) proves, for every fixed radial cutoff,

\[
 \begin{gathered}
 2\operatorname{Im}(u,f)\\
 =\lim_{R\to\infty}
 -R^{-1}\int\psi'(|x|/R)|Au(x)|^2\,dx.
 \end{gathered}
 \tag{31}
\]

<a id="flux-smooth-averages"></a>
## 7. Smooth averages determine sharp shell and ball averages

Choose nonincreasing \(\psi\) and write \(w=-\psi'\). Then \(w\ge0\), it is supported away from zero, and \(\int_0^\infty w=1\). Equation (31) first proves \(C=2\operatorname{Im}(u,f)\ge0\).

Fix \(\varepsilon>0\). Smooth inner and outer approximations to the interval \((1,2)\), with sufficiently thin boundary layers and normalized integrals, give nonnegative \(w_-,w_+\) of integral one satisfying

\[
 \begin{gathered}
 w_-\le(1+\varepsilon)1_{(1,2)},\\
 w_+\ge(1+\varepsilon)^{-1}1_{(1,2)}.
 \end{gathered}
 \tag{32}
\]

For example, take an inner smooth function between zero and one with integral at least \(1/(1+\varepsilon)\), and an outer smooth function equal one on \([1,2]\) with integral at most \(1+\varepsilon\); divide each by its integral. Their supports stay in the positive half-line. The integrated functions \(\psi_\pm(t)=\int_t^\infty w_\pm(s)\,ds\) are allowed radial cutoffs.

For

\[
 F(R)=R^{-1}\int_{R<|x|<2R}|Au|^2\,dx,
 \tag{33}
\]

positivity, (31) and (32) imply

\[
 \begin{gathered}
 \frac{C}{1+\varepsilon}\le\liminf_{R\to\infty}F(R),\\
 \limsup_{R\to\infty}F(R)\le(1+\varepsilon)C.
 \end{gathered}
 \tag{34}
\]

Let \(\varepsilon\downarrow0\) after the radius limit. Then \(F(R)\to C\), also when \(C=0\).

<a id="flux-ball-averages"></a>
For \(R\ge2\), set \(K_R=\lfloor\log_2R\rfloor\). Decompose the ball into the annuli with radii \(R/2^k\), \(1\le k\le K_R\), and one inner ball:

\[
 \begin{gathered}
 R^{-1}\int_{|x|<R}|Au|^2\,dx\\
 =\sum_{k=1}^{K_R}2^{-k}F(R/2^k)
 \\+R^{-1}\int_{|x|<R/2^{K_R}}|Au|^2\,dx.
 \end{gathered}
 \tag{35}
\]

The inner radius is in \([1,2)\), so its contribution tends to zero. All displayed annular radii are at least one. The endpoint norm of \(Au\) bounds \(F\) uniformly there. Extend the summands by zero beyond \(K_R\); their geometric majorant is summable. Every fixed summand tends to \(2^{-k}C\). Dominated convergence for the series, and \(\sum_{k\ge1}2^{-k}=1\), give the ball limit \(C\).

<a id="flux-full-order"></a>
Finally,

\[
 1-\chi=(1+\chi)^{-1}(1-\chi^2).
 \tag{36}
\]

The bounded smooth multiplier \((1+\chi)^{-1}\) preserves \(H^{m,1/2}\). By (24), \(a(x,D)u-Au\in L^2\). Its normalized ball norm tends to zero, and its cross term with the uniformly bounded normalized ball norm of \(Au\) tends to zero by Cauchy–Schwarz. This proves (8) for the originally prescribed full-order symbol.

If the free shell is empty, take \(\chi=0\) in the off-energy theorem. Then all derivatives through \(m\), and every prescribed full-order action, are in \(L^2\). Equation (23) has limit zero, so \(C=0\). The normalization is vacuous and (8) still holds. \(\square\)

<a id="flux-zero"></a>
## 8. A normalized symbol and the zero-flux corollary

For a nonempty regular shell let \(\nu=\min_{M_\lambda}|v|>0\). Choose \(\chi\) supported where \(|v|>\nu/2\), equal one near the shell, and smooth radial \(\kappa\), zero near the origin and one at large radius. The symbol

\[
 a_*(x,\xi)=\kappa(x)\chi(\xi)|v(\xi)|^{1/2}
 \tag{37}
\]

is smooth and order zero. On the positive bundle at large radius, its squared modulus is \(|v|=e_r\cdot v\), as required. Any positive minimum velocity is allowed.

If the flux is zero, (8) and (3) give \(A_*u\in\dot B^*\), where \(A_*=\operatorname{Op}(a_*)\). The order-zero symbol \(b=\kappa\chi/|v|^{1/2}\), extended by zero off its noncritical support, has the exact product

\[
 \begin{gathered}
 \operatorname{Op}(b)A_*
 =\kappa(x)^2\chi(D)^2+\operatorname{Op}(r_*),\\
 r_*\in S(X^{-1}\Xi^{-N},G_1)
 \quad\text{for every }N.
 \end{gathered}
 \tag{38}
\]

The first operator preserves \(\dot B^*\), and Lemma 2.1 puts the remainder output in \(L^2\). The bounded spatial complement of \(\kappa^2\chi(D)^2u\) is also \(L^2\). Thus \(\chi(D)^2u\in\dot B^*\).

Choose compact \(\chi'\), equal one near \(\operatorname{supp}\chi\). Every compact-frequency multiplier \(D^\alpha\chi'(D)\) preserves the closure, and

\[
 D^\alpha\chi(D)^2u
 =(D^\alpha\chi'(D))\chi(D)^2u\in\dot B^*.
 \tag{39}
\]

The off-energy derivatives in (24) are \(L^2\). Adding them proves (9) for all \(|\alpha|\le m\). The empty-shell case already has this conclusion. \(\square\)

### Use the conclusion

Keep the free-velocity normalization in the positive operator and the actual rough symmetry pairing. Follow smooth radial averages to sharp shell averages before using the zero-flux conclusion.

<a id="flux-solutions"></a>
## 9. Graded exercises with complete solutions

**Exercise 1 — Basic: compute the flux on the line.** Let \(H=-\partial_x^2\), \(\lambda=1\), and take a nonzero, even, nonnegative \(f\in C_c^\infty((-1/4,1/4))\). Put

\[
 u_\pm(x)=\frac{\pm i}{2}\int e^{\pm i|x-y|}f(y)\,dy.
 \tag{40}
\]

Choose real compact smooth \(\chi\), equal one near \(\pm1\) and zero near zero, and smooth even \(\kappa\), zero on \(|x|\le1\), one on \(|x|\ge2\). For \(a=\sqrt2\,\kappa\chi\), verify (7), compute the normalized ball mass of \(a(x,D)u_+\), and compare it with \(2\operatorname{Im}(u_+,f)\). Explain the lower sign.

**Solution 1.** The free shell is \(\{-1,1\}\), with velocities \(2\xi\). Its positive rays are \((x,1)\), \(x>0\), and \((x,-1)\), \(x<0\). On them at large radius, \(|a|^2=2=e_r\cdot v\).

Set \(F=\int\cos(y)f(y)\,dy>0\). Evenness removes the sine term, and outside the forcing support \(u_\pm=\pm iF e^{\pm i|x|}/2\). The frequency singularities of \(u_+\) at \(\pm1\) are removed by \(1-\chi\); in distributions,

\[
 \widehat{(1-\chi(D))u_+}(\xi)
 =\frac{1-\chi(\xi)}{\xi^2-1}\widehat f(\xi).
 \tag{41}
\]

This is smooth and rapidly decreasing with all derivatives, so the off-frequency output is Schwartz. Thus \(a(x,D)u_+\) differs from \(\sqrt2\,\kappa u_+\) by an \(L^2\) function. Its squared tail amplitude is \(F^2/2\) on each half-line, giving normalized ball limit \(F^2\). The \(L^2\) difference and its cross term contribute zero, by Cauchy–Schwarz.

Direct calculation gives

\[
 \begin{aligned}
 2\operatorname{Im}(u_+,f)
 &=\iint\cos(x-y)f(x)f(y)\,dx\,dy\\
 &=\left|\int e^{-iy}f(y)\,dy\right|^2=F^2.
 \end{aligned}
 \tag{42}
\]

The lower solution has the same normalized positive mass but imaginary pairing \(-F^2\). Its positive-bundle radiation fails: \(h=\kappa(x)(\xi-\operatorname{sign}x)\) is smooth, vanishes on the positive bundle, and sends \(u_-\) to a function with nonzero normalized tail mass. The positive outgoing hypothesis selects the sign in (8).

**Exercise 2 — Intermediate: the rough symmetric pairing.** Assume the primary symmetric map (14), take \(\delta=1/3\), and let \(u\in H^{m,-7/12}\). Prove that \((V_Su,u)\) is defined and real. Identify the output weights and explain which density is used.

**Solution 2.** The primary output weight is

\[
 1+\frac13-\frac7{12}=\frac34>\frac7{12}.
 \tag{43}
\]

Thus \(V_Su\in H^{0,3/4}\subset H^{0,7/12}\), paired absolutely with \(u\in H^{0,-7/12}\). Choose Schwartz approximants in \(H^{m,-7/12}\). Their outputs converge in \(H^{0,3/4}\), hence at weight \(7/12\), and their inputs converge at weight \(-7/12\). The weighted Cauchy–Schwarz bound (17) passes their real symmetric pairings to the limit.

If the derivatives also have endpoint bounds, the output is in \(B\), since \(3/4>1/2\). The endpoint pairing is the same integral. Approximation in \(B^*\) would require membership in its Schwartz closure; weighted Sobolev density supplies the needed argument before that conclusion is known.

**Exercise 3 — Intermediate: a fourth-order commutator.** On the line take \(P_0(D)=D^4+2D^2\). Compute \([P_0,\psi_R]/i\) exactly. For a smooth \(V_L=\sum_{\alpha=0}^4A_\alpha(x)D^\alpha\) with coefficient size \(O(X^{-1/3})\), verify the error decay at \(b=7/12\), \(c=1/12\).

**Solution 3.** The finite identity is

\[
 [D^k,\psi_R]
 =\sum_{j=1}^k\binom kj(-i)^j\psi_R^{(j)}D^{k-j}.
 \tag{44}
\]

Division by \(i\) gives

\[
 \begin{aligned}
 [P_0,\psi_R]/i
 ={}&-\psi_R'(4D^3+4D)\\
 &+6i\psi_R''D^2+4\psi_R'''D\\
 &-i\psi_R''''+2i\psi_R''.
 \end{aligned}
 \tag{45}
\]

The first term is the velocity term, since \(v(\xi)=4\xi^3+4\xi\) and \(\psi_R'=R^{-1}\psi'(|x|/R)\operatorname{sign}x\). All other free terms have at least two cutoff derivatives, of size \(O(R^{-2})\) or better on the annulus.

The long-range commutator is the exact sum of \(A_\alpha[D^\alpha,\psi_R]/i\). Its order is at most three, its coefficients are \(O(X^{-1/3}R^{-1})\), and it differentiates no \(A_\alpha\). Multiplication by \(R^c\) exchanges the radius factor for \(X^c\) there. The resulting coefficient weight is \(X^{c-1-1/3}\); the free higher terms have stronger decay. Therefore

\[
 \begin{gathered}
 1+\frac13-\frac1{12}-\frac7{12}=\frac23>\frac12,\\
 \|E_Ru\|_B
 \le C R^{-1/12}\|u\|_{3,-7/12}.
 \end{gathered}
 \tag{46}
\]

Pair with \(u\in B^*\) to get the stated vanishing error. The same \(b\) also lies between \(1/2\) and \((1+\delta)/2\), so the rough symmetric pairing is finite.

**Exercise 4 — Advanced: from smooth averages to ball averages.** Let \(g\in B^*\), and suppose

\[
 \begin{gathered}
 \lim_{R\to\infty}R^{-1}\int w(|x|/R)|g|^2\,dx=C\\
 \text{for every }w\in C_c^\infty((0,\infty)),\\
 w\ge0,\ \int w=1.
 \end{gathered}
 \tag{47}
\]

Prove \(C\ge0\) and that the sharp annular and ball averages tend to \(C\). Treat the inner ball explicitly.

**Solution 4.** Each smooth average is nonnegative. For any \(\varepsilon>0\), take an inner smooth approximation to \(1_{(1,2)}\), values in \([0,1]\), with integral at least \(1/(1+\varepsilon)\). Its normalization is at most \((1+\varepsilon)1_{(1,2)}\). Take an outer approximation equal one on \([1,2]\), integral at most \(1+\varepsilon\); its normalization is at least \(1_{(1,2)}/(1+\varepsilon)\). Thin smooth boundary layers provide both. The two smooth limits sandwich the lower and upper annular limits as in (34). Let \(\varepsilon\) decrease to zero.

For \(R\ge2\), use \(K_R=\lfloor\log_2R\rfloor\). The outer annuli contribute \(\sum_{k=1}^{K_R}2^{-k}F_g(R/2^k)\), where \(F_g(r)=r^{-1}\int_{r<|x|<2r}|g|^2\). Every such radius is at least one, where the endpoint bound controls \(F_g\) uniformly. Extend the summands by zero beyond \(K_R\). Dominated convergence with the geometric majorant gives \(C\sum_{k\ge1}2^{-k}=C\).

The remaining radius \(R/2^{K_R}\) is in \([1,2)\). Its mass is bounded by the fixed local \(L^2\) mass on \(|x|<2\); divided by \(R\), it tends to zero. This proves the ball limit including the finite inner contribution.

**Exercise 5 — Advanced: zero flux recovers every derivative.** Construct a normalized order-zero symbol on a nonempty compact regular shell, with arbitrary minimum velocity. Assuming zero imaginary pairing and the radiation hypothesis, prove every derivative through \(m\) lies in \(\dot B^*\). Include the exact product error.

**Solution 5.** With \(\nu=\min_{M_\lambda}|v|>0\), choose \(\chi=1\) near the shell, supported where \(|v|>\nu/2\). Choose smooth radial \(\kappa\), zero near the origin and one at large radius. The symbol \(a_*=\kappa\chi|v|^{1/2}\) is smooth and satisfies \(|a_*|^2=|v|=e_r\cdot v\) on the large positive rays. No unit-speed normalization is needed.

The flux identity and the closure characterization give \(A_*u\in\dot B^*\). The symbol \(b=\kappa\chi/|v|^{1/2}\) defines a bounded order-zero shell map preserving the closure. Its exact product with \(A_*\) is (38); the remainder has weight \(X^{-1}\) and rapid frequency decay. Multiplication by \(X\) turns that error into an order-zero shell map, so its squared shell masses are \(O(R_j^{-1})\), summable. Its output is \(L^2\).

Thus \(\kappa^2\chi(D)^2u\in\dot B^*\). Its bounded spatial complement is \(L^2\) by the compact-frequency kernel argument. Consequently \(\chi(D)^2u\in\dot B^*\). Choose compact \(\chi'=1\) near \(\operatorname{supp}\chi\), and use the exact multiplier identity (39). Each near-energy derivative is in the closure. The off-energy derivatives are \(L^2\) by (24), proving the conclusion for every \(|\alpha|\le m\).

For an empty shell, all these derivatives are already \(L^2\); the radial flux limit is zero. This gives the same conclusion.

## 10. Further questions

Zero shell mass is the first decay conclusion. The next argument upgrades a solution with vanishing shell mass to polynomial weighted endpoint estimates, uniformly over compact sets of regular energies. Homogeneous solutions then acquire every polynomial weight, leading to discreteness and finite multiplicity of the noncritical point spectrum.

## References

The [accessible scalar comparisons in the limiting-absorption lesson](limiting-absorption-for-long-range-differential-perturbations.md#accessible-scalar-comparisons-and-their-proof-limits) describe the radial-flux proofs in Ito–Skibsted, Proposition 4.14, and Isozaki, Lemmas 2.4–2.6. They also retain the imported final Rellich step and the formula-extraction limit of the Isozaki text. The exact signs, velocity normalization, rough pairing and every-derivative conclusion used here are proved in Sections 3–8.

[A] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), lectures of 17–21 July 1978, §4, Proposition 4.B and equations (4.4)–(4.9), supplies the freely readable radial-commutator/velocity-normalization construction. Sections 3–4 above prove the additional real rough pairing and all finite differential errors without differentiating a rough coefficient. Sections 5–6 justify the exact positive operator and adjoint passage on weighted inputs; Section 7 proves the smooth-to-sharp averaging passage rather than assuming it. Section 8 recovers every derivative. These explicit bridges retain arbitrary polynomial velocity and the sharp rough coefficient class.

The source's printed equation (4.8) has \(|P_0(\xi)|\) where its definition (4.6) requires \(|\nabla P_0(\xi)|\). Its signs in (4.7)–(4.9) also fail to follow that definition consistently. Equations (19)–(31) above derive the sign directly with our stated inner-product convention: the positive outgoing mass uses \(-\psi'\). The explicit line calculation in Solution 1 independently verifies both the velocity factor and the sign.

[T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*, author's online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf), treats self-adjoint resolvents and their spectral applications.

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, Theorem 30.2.7, formulas (30.2.26)–(30.2.27), and Corollary 30.2.8, with their proofs, pp. 291–293. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
