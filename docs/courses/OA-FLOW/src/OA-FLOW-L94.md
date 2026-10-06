# The weak-star generator and its domain

A scalar derivative can define an unbounded generator even when the orbit is not differentiable in norm. We first establish the uniform bounds and smoothing estimates that control this domain. The generator then appears as the adjoint of the predual generator, giving its full weak-star closed graph and a weak-star dense invariant domain.

*Programme proof written in Codex (OpenAI), September 2026; foundation integration and revision by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

Let \(X=X_*^*\) be a complex dual Banach space with specified predual, and let \(\alpha:\mathbb R\to\operatorname{GL}(X)\) be a uniformly bounded group of weak-star continuous operators with norm-continuous predual orbits, with the specified-dual conventions of BS0–1. Write \(C_\alpha=\sup_t\|\alpha_t\|\). Put \(\beta_t\phi=\phi\circ\alpha_t\); the specified predual hypothesis makes this a strongly continuous group on \(X_*\).

The exact earlier proofs used here are CF1 for scalar and Banach-valued fundamental calculus, [L24 Proposition4.1](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) for Banach-valued integration, L34 Lemma3.2 for the complete-metric Baire argument, [RF1](OA-FLOW-RF.md#oa-flow.rf.1) for smooth compact kernels, and BS0–1 for the dual action and its full integrated maps. The uniform-boundedness argument is included immediately below.

<a id="oa-flow.gen.bounds"></a>

## Uniform bounds from pointwise bounds

**Uniform-boundedness lemma.** Let $X$ be a Banach space, $Y$ a normed space, and $(T_i)$ any family of bounded linear maps $X\to Y$. If $\sup_i\|T_i x\|<\infty$ for every $x\in X$, then $\sup_i\|T_i\|<\infty$.

**Proof.** The closed sets

$$F_n=\{x:\sup_i\|T_i x\|\leq n\},\qquad n\geq1,$$

cover $X$. By the complete-metric Baire proof in L34 Lemma3.2, some $F_n$ contains an open ball about a point $x_0$ of radius $r>0$. For $\|x\|\leq1$, both $x_0$ and $x_0+(r/2)x$ are in that ball. Hence

$$\frac r2\|T_i x\|\leq\|T_i(x_0+(r/2)x)\|+\|T_i x_0\|\leq2n.$$

Taking the supremum over $i$ and the unit ball gives $\sup_i\|T_i\|\leq4n/r$. $\square$

<a id="oa-flow.gen.smoothing"></a>

## Smoothing and interval averages

Let \(f\) belong to \(C_c^1(\mathbb R)\), put \(L_t f(u)=f(u-t)\), and take nonzero real \(t\). The scalar fundamental theorem gives, for each \(u\),

<a id="equation-lr1"></a>

\[
 \frac{L_t f(u)-f(u)}t+f'(u)
 =-\int_0^1\bigl(f'(u-\theta t)-f'(u)\bigr)\,d\theta.
 \tag{LR1}
\]

Choose \(R\) with the support of \(f\) and \(f'\) inside \([-R,R]\). For \(|t|\le1\), the integrand vanishes outside \([-R-1,R+1]\). CF1's compact uniform-continuity proof applied to \(f'\) gives a modulus \(\omega_{f\prime}(\varepsilon)\) tending to zero. Taking absolute values and integrating on this fixed interval gives

<a id="equation-lr2"></a>

\[
 \left\|\frac{L_t f-f}t+f'\right\|_1
 \le (2R+2)\,\omega_{f'}(|t|)\longrightarrow0.
 \tag{LR2}
\]

Thus no interchange theorem for arbitrary nets or unbounded domains is needed. The same proof works for both signs of \(t\). BS1's norm bound transfers (LR2) to integrated vectors, with the minus sign used in (G4) below.

For density, [RF1](OA-FLOW-RF.md#oa-flow.rf.1) supplies \(b\ge0\), smooth, supported in \([-1,1]\), positive inside. Its integral \(c\) is finite and positive. The kernels \(f_\varepsilon(u)=b(u/\varepsilon)/(c\varepsilon)\) have integral one, nonnegative values and support in \([-\varepsilon,\varepsilon]\), by [SC8's scalar substitution theorem](OA-FLOW-SC.md#sc-08), with [SC2's normalization and affine scaling](OA-FLOW-SC.md#sc-02). For any strongly continuous predual orbit,

<a id="equation-lr3"></a>

\[
 \left\|\int f_\epsilon(u)\beta_u\phi\,du-\phi\right\|
 \le\sup_{|u|\le\epsilon}\|\beta_u\phi-\phi\|\longrightarrow0.
 \tag{LR3}
\]

The analogous scalar estimate for a fixed predual functional gives weak-star density on \(X\). These are the required smoothing estimates; no predual separability is used.

For the strongly continuous predual group \(\beta\), the group law and bounded-map compatibility yield the interval-average identity

<a id="equation-lr4"></a>

\[
 \frac{\beta_h\psi_t-\psi_t}{h}
 =\frac1h\int_t^{t+h}\beta_u\phi\,du
  -\frac1h\int_0^h\beta_u\phi\,du
 \longrightarrow\beta_t\phi-\phi
 \quad(h\to0),
 \qquad \psi_t=\int_0^t\beta_u\phi\,du.
 \tag{LR4}
\]

Oriented intervals and continuity justify both signs of \(h\) and \(t\). This will identify the full adjoint-generator domain below.

<a id="oa-flow.gen.domain"></a>

## Scalar derivatives define the domain

Define \(D(\delta)\) to contain exactly those \(x\in X\) for which every scalar function \(t\mapsto\langle\alpha_t x,\phi\rangle\), \(\phi\in X_*\), has a derivative at zero and

<a id="equation-g1"></a>

$$\phi\longmapsto
\left.\frac{d}{dt}\langle\alpha_t x,\phi\rangle\right|_{t=0}
\quad\text{is bounded on }X_*.\tag{G1}$$

For such \(x\), duality gives a unique \(\delta x\in X\) representing this functional:

<a id="equation-g2"></a>

$$\langle\delta x,\phi\rangle
=\lim_{t\to0}\left\langle\frac{\alpha_t x-x}{t},\phi\right\rangle
\qquad(\phi\in X_*).\tag{G2}$$

Thus (G1)–(G2) say exactly that the difference quotient converges weak-star to \(\delta x\). Under the stated hypothesis that scalar derivatives exist against **every** \(\phi\in X_*\), the boundedness in (G1) is automatic. To prove this, put \(Q_t=(\alpha_t x-x)/t\) for \(0<|t|\le1\). For each fixed \(\phi\), the numbers \(\langle Q_t,\phi\rangle\) are bounded near zero because they converge. Away from zero, the uniform action bound gives \(|\langle Q_t,\phi\rangle|\le(C_\alpha+1)\|x\|\|\phi\|/|t|\), so they are bounded on the entire indicated time interval. Uniform boundedness, applied to these functionals on the Banach space \(X_*\), gives

<a id="equation-g2a"></a>

$$\sup_{0<|t|\le1}\|Q_t\|=:C_x<\infty,
\qquad |\ell(\phi)|\le C_x\|\phi\|,
\quad \ell(\phi):=\lim_{t\to0}\langle Q_t,\phi\rangle. \tag{G2a}$$

The limit \(\ell\) is linear and bounded, hence an element of \(X_*^*=X\); it is the required \(\delta x\). Thus the boundedness clause may be retained to match the source definition, but it adds no domain restriction when all predual scalar derivatives exist. The argument uses all functionals in \(X_*\), rather than only a dense testing subset. Linearity of the domain and generator follows from this scalar characterization.

<a id="oa-flow.gen.density"></a>

## Smoothing gives weak-star density

For \(f\in C_c^1(\mathbb R)\) and \(x\in X\), define the weak-star integral \(x_f=\int_{\mathbb R}f(u)\alpha_u x\,du\). It exists through the predual, and \(\|x_f\|\le C_\alpha\|f\|_1\|x\|\). The group law and a change of variable give

<a id="equation-g3"></a>

$$\alpha_t x_f=\int_{\mathbb R}f(u-t)\alpha_u x\,du.\tag{G3}$$

The explicit estimate (LR2) makes the difference quotient in (G3) converge even in the norm of the resulting integrated vector. In particular

<a id="equation-g4"></a>

$$x_f\in D(\delta),\qquad
\delta x_f=-\int_{\mathbb R}f'(u)\alpha_u x\,du.\tag{G4}$$

Choose a nonnegative smooth unit-mass approximate identity \(f_V\) supported in shrinking neighborhoods of zero. For every \(\phi\in X_*\), weak-star orbit continuity gives \(\langle x_{f_V},\phi\rangle\to\langle x,\phi\rangle\). Hence \(x_{f_V}\to x\) weak-star, proving

<a id="equation-g5"></a>

$$\overline{D(\delta)}^{\,\sigma(X,X_*)}=X.\tag{G5}$$

No norm density of \(D(\delta)\) is inferred for an arbitrary dual-space action.

<a id="oa-flow.gen.closed"></a>

## The predual generator makes the graph closed

Let \(\beta_t\phi=\phi\circ\alpha_t\) on \(X_*\). It is a strongly continuous, uniformly bounded group. Denote its norm generator by \(L\), with domain \(D(L)\). Smooth convolution of predual vectors, by the same calculation as (G3)–(G4), shows \(D(L)\) is norm dense in \(X_*\). Define the Banach adjoint \(L^*\) by

<a id="equation-g6"></a>

$$x\in D(L^*)\quad\Longleftrightarrow\quad
\phi\mapsto\langle x,L\phi\rangle
\text{ is bounded on }D(L)\text{ in the }X_*\text{ norm},\tag{G6}$$

and represent that bounded functional by \(L^*x\in X\). We claim \(\delta=L^*\). If \(x\in D(\delta)\) and \(\phi\in D(L)\), differentiating \(\langle x,\beta_t\phi\rangle\) at zero in the two allowed ways gives \(\langle\delta x,\phi\rangle=\langle x,L\phi\rangle\), so \(x\in D(L^*)\) and \(L^*x=\delta x\).

Conversely, for \(x\in D(L^*)\) and arbitrary \(\phi\in X_*\), set \(\psi_t=\int_0^t\beta_u\phi\,du\), with the oriented integral for negative \(t\). The both-sign interval identity (LR4) shows \(\psi_t\in D(L)\) and \(L\psi_t=\beta_t\phi-\phi\). Therefore

<a id="equation-g7"></a>

$$\langle\alpha_t x-x,\phi\rangle
=\langle x,L\psi_t\rangle
=\int_0^t\langle\alpha_u L^*x,\phi\rangle\,du.\tag{G7}$$

Dividing by \(t\) and using weak-star continuity of the orbit of \(L^*x\) gives the scalar derivative \(\langle L^*x,\phi\rangle\) at zero. It is bounded in \(\phi\), so \(x\in D(\delta)\) and \(\delta x=L^*x\). The graph therefore has the description

<a id="equation-g8"></a>

$$\operatorname{Graph}(\delta)
=\bigcap_{\phi\in D(L)}
\{(x,y)\in X\times X:\langle y,\phi\rangle=\langle x,L\phi\rangle\}.\tag{G8}$$

Each set in the intersection is closed for the product weak-star topology. Thus \(\delta\) is weak-star closed. This argument does not exchange a weak-star convergent net with an integral without a uniform bound; closedness follows from fixed predual test equations.

<a id="oa-flow.gen.invariant"></a>

## The domain is invariant under the action

For \(x\in D(\delta)\) and \(s\in\mathbb R\), commutativity of the group and normality of \(\alpha_s\) give, for every \(\phi\in X_*\),

<a id="equation-g9"></a>

$$\left.\frac{d}{dt}\langle\alpha_t\alpha_s x,\phi\rangle\right|_{t=0}
=\langle\alpha_s\delta x,\phi\rangle.\tag{G9}$$

The right side is a bounded predual functional. Hence \(\alpha_sD(\delta)=D(\delta)\) (apply the same inclusion to \(-s\)) and

<a id="equation-g10"></a>

$$\delta\alpha_sx=\alpha_s\delta x\qquad(x\in D(\delta)).\tag{G10}$$

**Problem.** If \(\alpha_t=\operatorname{diag}(e^{it\lambda_1},\ldots,e^{it\lambda_n})\) on \(\mathbb C^n\), identify \(D(\delta)\) and \(\delta\).

**Solution.** Every coordinate orbit is differentiable, so \(D(\delta)=\mathbb C^n\) and \(\delta=\operatorname{diag}(i\lambda_1,\ldots,i\lambda_n)\). Both (G5) and (G8) are immediate in finite dimension, while the general proof is needed when domain and weak-star topology matter. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Definition XI.1.18 and the preceding domain assertions, printed page325 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The proof above supplies the uniform-boundedness argument, smoothing estimates and complete adjoint-domain calculation. All mathematical inputs have the written local or earlier proof locators stated above.
