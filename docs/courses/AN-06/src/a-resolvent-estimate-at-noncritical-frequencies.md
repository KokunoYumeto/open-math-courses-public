# A resolvent estimate at noncritical frequencies

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: What replaces division where the symbol vanishes?** At a noncritical energy the symbol may be zero but its gradient has a direction. A multiplier increasing along that direction creates a positive commutator. Its imaginary-parameter term has the useful sign on the chosen half-plane, while shell norms measure escape at large distance. This is the second half of the estimate that the off-energy reciprocal cannot provide.

Near an energy surface, division by the free symbol can fail. Its gradient still supplies a direction when the frequency is noncritical. We build a multiplier that changes monotonically in that direction. A commutator then measures the solution on large spatial annuli, while the imaginary spectral parameter has a favorable sign. This gives an endpoint estimate with constants independent of the spectral parameter throughout either open half-plane.

Read [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md) for the spatial norms, [Mild weights and frequency localization](mild-weights-and-frequency-localization.md) for the shell operator estimate, and [Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md) for the weighted calculus. The coefficient class comes from [Admissible differential perturbations](admissible-differential-perturbations.md). We use the complete programme proof [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md#finite-composition) for finite composition, adjoints and quantization changes, and the complete programme proof [Weighted positivity from Gaussian packets](../providers/analysis/weighted-positivity.md#weighted-positivity) for the sharp weighted bound. Lemma 4.1 below applies it with the precise order-minus-one Fourier form. The needed finite-calculus specializations are stated below. Lerner [L] supplies the freely accessible metric estimates studied here.

Use \(D=-i\partial\), the Fourier transform \(\widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx\), and an inner product linear in its first entry. Put \(X=\langle x\rangle\) and \(\Xi=\langle\xi\rangle\).

## 1. The complete endpoint estimate

The spatial shells and their radii are

\[
 \begin{gathered}
 A_0=\{|x|<1\},\qquad R_j=2^j,\\
 A_j=\{2^{j-1}\le |x|<2^j\}\quad(j\ge1).
 \end{gathered}
 \tag{1}
\]

Define

\[
 \begin{aligned}
 \|f\|_B&=\sum_{j\ge0}R_j^{1/2}\|f\|_{L^2(A_j)},\\
 \|u\|_{B^*}&=\sup_{j\ge0}R_j^{-1/2}\|u\|_{L^2(A_j)}.
 \end{aligned}
 \tag{2}
\]

The endpoint lesson proves \(B\subset L^2\subset B^*\) and

\[
 |(f,u)|\le\|f\|_B\|u\|_{B^*}.
 \tag{3}
\]

<a id="noncritical-coefficients"></a>

Let \(P_0(D)\) be a real scalar constant-coefficient elliptic differential operator of order \(m\ge1\). Set

\[
 \begin{gathered}
 P=P_0(D)+V_L(x,D),\\
 V_L(x,D)=\sum_{|\alpha|\le m}b_\alpha(x)D^\alpha.
 \end{gathered}
 \tag{4}
\]

Assume \(V_L\) is symmetric on Schwartz functions, the total principal symbol is elliptic, and, for a fixed \(0<\delta\le1\),

\[
 \begin{aligned}
 |b_\alpha(x)|&\le C_\alpha X^{-\delta},\\
 |\partial_x^\beta b_\alpha(x)|
 &\le C_{\alpha\beta}X^{-1-\delta|\beta|}
       &&(|\beta|\ge1).
 \end{aligned}
 \tag{5}
\]

All coefficients are smooth; complex lower coefficients are allowed. For the symmetric smooth part of a 1-admissible perturbation, the [regularization theorem](admissible-differential-perturbations.md#admissible-regularization) gives the budget \(M_0=b\), \(M_q=1+bq\) for \(q\ge1\), where \(0<b<1\). Choosing \(\delta=b\) gives (5) at every derivative order. The [symmetric exterior splitting](admissible-differential-perturbations.md#admissible-exterior-ellipticity) preserves these bounds.

<a id="noncritical-theorem"></a>

The estimate and angular positive-commutator construction are Hörmander [H4, Proposition 30.2.4].

**Theorem 1.1.** Let \(\chi\in C_c^\infty(\{\xi:\nabla P_0(\xi)\ne0\})\), possibly complex-valued. If \(u\in H^m\) solves

\[
 (P-z)u=f,\qquad f\in B,\qquad \operatorname{Im}z\ne0,
 \tag{6}
\]

then

\[
 \begin{aligned}
 \|\chi(D)u\|_{B^*}
 &\le C_\chi\bigl(\|\chi(D)f\|_B\\
 &\hspace{24mm}+\|X^{-(1+\delta)/2}u\|_2\bigr).
 \end{aligned}
 \tag{7}
\]

The constant depends on the fixed operator and cutoff, and is uniform for all nonreal \(z\). In particular no bound on \(\operatorname{Re}z\) or small energy disc is assumed. The full differential order is permitted in \(V_L\). The forcing norm retains the same frequency cutoff as the solution.

<a id="noncritical-calculus"></a>

## 2. The calculus and endpoint interfaces

For \(0<\gamma\le1\), use

\[
 \begin{gathered}
 G_\gamma=X^{-2\gamma}|dx|^2+\Xi^{-2}|d\xi|^2,\\
 h_\gamma=X^{-\gamma}\Xi^{-1}.
 \end{gathered}
 \tag{8}
\]

The [metric calculation in Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-metric) proves their metric hypotheses and the temperateness of every real product power of \(X,\Xi\). Write \(S(w,G_\gamma)\) for the coordinate bounds

\[
 |\partial_x^\beta\partial_\xi^\alpha a|
 \le C_{\alpha\beta}wX^{-\gamma|\beta|}\Xi^{-|\alpha|}.
 \tag{9}
\]

All operators below are in left quantization. Theorem 4.1 and Section 5 of that programme calculus proof establish the exact common action on \(\mathcal S,\mathcal S'\), finite-seminorm composition, and, for every integer \(N\ge1\),

\[
 \begin{aligned}
 a\circ_L b-&
 \sum_{|\alpha|<N}
 \frac{\partial_\xi^\alpha a\,D_x^\alpha b}{\alpha!}\\
 &\in S(h_\gamma^Nw_1w_2,G_\gamma).
 \end{aligned}
 \tag{10}
\]

The adjoint symbol has leading term \(\overline a\) and a remainder of weight \(h_\gamma w\). This is formula (C19) of that proof, obtained from its exact finite change between right and left quantization. Each fixed target seminorm uses finitely many input seminorms. We will use only finite expansions, with their remainders.

The [weighted symbol mapping theorem](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-symbol-mapping) gives

\[
 \begin{gathered}
 a\in S(X^{-2a_0},G_\gamma)\\
 \Longrightarrow
 a(x,D):L^2_{-a_0}\longrightarrow L^2_{a_0},
 \qquad a_0\in\mathbb R,
 \end{gathered}
 \tag{11}
\]

where \(\|u\|_{L^2_t}=\|X^tu\|_2\). It also gives uniform bounds on \(L^2_t\) and \(H^s\) for bounded families of weight-one symbols.

<a id="noncritical-shell-transfer"></a>

We need one consequence for the endpoint norms. Suppose \(T\) has consistent bounds on \(L^2_{-1}\) and \(L^2_1\), with a common bound \(A\). The [consistent weighted-to-shell bounds](mild-weights-and-frequency-localization.md#mild-weighted-transfer) give

\[
 \|1_{A_k}T1_{A_j}\|_{2\to2}
 \le CA\,2^{-|k-j|}.
 \tag{12}
\]

For this specialization the calculation is short. On \(A_j\), including \(j=0\), one has \(R_j/2\le X\le\sqrt2R_j\). The two weighted bounds respectively give
\[
 \begin{aligned}
 \|1_{A_k}T1_{A_j}v\|_2
 &\le 2\sqrt2 A\,(R_j/R_k)\|1_{A_j}v\|_2,\\
 \|1_{A_k}T1_{A_j}v\|_2
 &\le 2\sqrt2 A\,(R_k/R_j)\|1_{A_j}v\|_2.
 \end{aligned}
\]
Take the smaller bound to obtain (12). The consistency hypothesis means these estimates concern the same output, so this minimum is legitimate.

Multiplication by \(R_k^{1/2}\), followed by summation, gives the \(B\) bound. Division by \(R_k^{1/2}\), followed by a supremum, gives the \(B^*\) bound: the ratio \(R_j^{1/2}/R_k^{1/2}\) costs at most \(2^{|j-k|/2}\), leaving the summable series \(\sum_{\ell\in\mathbb Z}2^{-|\ell|/2}\). Thus

\[
 \|T\|_{B\to B}+\|T\|_{B^*\to B^*}\le C A.
 \tag{13}
\]

For the second extension, finite shell sums converge to a \(B^*\) input in \(L^2_{-1}\), since their squared tails are bounded by \(C\|u\|_{B^*}^2\sum_{j>J}2^{-j}\). Passage to each output shell preserves the bound and the consistent weighted operator. These maps therefore agree with the distributional action. Uniform weighted constants give uniform constants in (13).

<a id="noncritical-angular"></a>

## 3. A monotone angular multiplier in every dimension

We construct a nonnegative smooth function \(\Psi(x,y)\), for \(y\ne0\), with

\[
 \Psi'(x,y):=y\cdot\partial_x\Psi(x,y)\ge0.
 \tag{14}
\]

Choose a nonnegative smooth even function \(\rho\), supported in \((-1/2,1/2)\), with \(\rho(0)=1\), decreasing for positive arguments and with strictly negative derivative on some open subinterval of \((0,1/2)\). For \(z\ne0\), set

\[
 a(z,y)=\rho\left(1-\frac{z\cdot y}{|z||y|}\right).
 \tag{15}
\]

Its support has angle less than \(\pi/3\) between \(z\) and \(y\). Along \(z+ty\), their directional cosine increases; for \(e=y/|y|\),

\[
 \begin{aligned}
 \frac{d}{dt}\frac{(z+te)\cdot e}{|z+te|}
 &=\frac{|z+te|^2-((z+te)\cdot e)^2}{|z+te|^3}\\
 &\ge0.
 \end{aligned}
 \tag{16}
\]

Consequently \(a\) is nondecreasing in that direction away from the origin. Homogeneity and differentiation on the two unit spheres give

\[
 |\partial_z^\alpha\partial_y^\beta a(z,y)|
 \le C_{\alpha\beta}|z|^{-|\alpha|}|y|^{-|\beta|}.
 \tag{17}
\]

Choose a radial smooth \(\psi\ge0\), compactly supported in \(1/2<|x|<5/2\), positive on \(3/4\le|x|\le9/4\) and equal one on \(1\le|x|\le2\). Define

\[
 \begin{aligned}
 \Psi(x,y)&=\int\psi(x-z)a(z,y)\,dz\\
          &=\int\psi(z)a(x-z,y)\,dz.
 \end{aligned}
 \tag{18}
\]

**Lemma 3.1.** This function is smooth for \(y\ne0\), homogeneous of degree zero in \(y\), and satisfies (14) and

\[
 |\partial_x^\alpha\partial_y^\beta\Psi(x,y)|
 \le C_{\alpha\beta}X^{-|\alpha|}|y|^{-|\beta|}.
 \tag{19}
\]

Both \(\Psi\) and \(\Psi'\) are strictly positive wherever \(\psi(x)>0\). There is a compact smooth \(\phi_0\), constant and nonzero on \(1\le|x|\le2\), with

\[
 \phi_0(x)^2
 \le\frac{\Psi(x,y)\Psi'(x,y)}{|y|}.
 \tag{20}
\]

**Proof.** For bounded \(x\), use the first integral in (18) and put position derivatives on \(\psi\). Frequency-direction derivatives of the angular factor are bounded by \(C|y|^{-|\beta|}\), uniformly as \(z\to0\), because it has degree zero in \(z\). A value assigned at the single point \(z=0\) has no effect on the integral. Differentiation under a bounded compact integral proves smoothness and the required bounds there. For \(|x|\ge5\), use the second integral; \(|x-z|\) is comparable to \(|x|\) on the support of \(\psi\). Formula (17) proves every mixed bound in (19).

If \(n\ge2\), the directional derivative \(y\cdot\partial_z a\) is nonnegative, bounded by \(C|y|/|z|\), and locally integrable. It is the distributional derivative too: the boundary term on a sphere of radius \(\varepsilon\) is \(O(|y|\varepsilon^{n-1})\). Therefore

\[
 \Psi'(x,y)=\int\psi(x-z)\,
                 (y\cdot\partial_z a(z,y))\,dz\ge0.
 \tag{21}
\]

When \(\psi(x)>0\), the first factor is positive for sufficiently small \(z\). A small open cone in the angular transition region has \(y\cdot\partial_z a>0\) and positive measure. Integrating over it gives strict positivity of \(\Psi'\). An inner cone where \(a>0\) gives strict positivity of \(\Psi\).

For \(n=1\), the angular factor is one on \(zy>0\) and zero on \(zy<0\). Its directional distributional derivative is \(|y|\delta_0\). Thus

\[
 \Psi'(x,y)=|y|\psi(x).
 \tag{22}
\]

The half-line integral in (18) is positive wherever \(\psi(x)>0\); hence both strict assertions hold in this dimension as well.

On the compact collar \(3/4\le|x|\le9/4\) and the unit sphere in \(y\), the continuous product \(\Psi\Psi'\) has a positive minimum \(\mu\). Homogeneity makes \(\Psi\Psi'/|y|\) have the same lower bound for every \(y\ne0\). Take a smooth radial cutoff \(\omega\), supported in the interior of that collar, with \(0\le\omega\le1\) and \(\omega=1\) on \(1\le|x|\le2\). Then \(\phi_0=c\omega\), with \(0<c^2\le\mu\), satisfies (20) everywhere, since its left side vanishes outside the collar. \(\square\)

<a id="noncritical-algebraic"></a>

### An explicit alternative multiplier

There is also a direct algebraic construction with all the properties needed in Sections 4–6. For \(e=y/|y|\), put
\[
 \widetilde\Psi(x,y)=2+\frac{x\cdot e}{\langle x\rangle}.
\]
It lies between 1 and 3, is smooth for \(y\ne0\), and is homogeneous of degree zero in \(y\). Direct differentiation gives
\[
 y\cdot\partial_x\widetilde\Psi
 =|y|\frac{\langle x\rangle^2-(x\cdot e)^2}{\langle x\rangle^3}
 \ge |y|\langle x\rangle^{-3}>0.
\]
The [all-real bracket derivative proof](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-automorphisms), applied to \(\langle x\rangle^{-1}\), and the product rule for \(x_j\langle x\rangle^{-1}\), give the position bounds in (19). Derivatives of \(e=y/|y|\) have the bound \(C_\beta|y|^{-|\beta|}\), by differentiation and homogeneity on the unit sphere. This proves all mixed bounds in (19) as well.

Use the annular cutoff \(\omega\) from Lemma 3.1 and set
\[
 \widetilde\phi_0=
 \bigl(1+(9/4)^2\bigr)^{-3/4}\omega.
\]
On its support \(\langle x\rangle\le\bigl(1+(9/4)^2\bigr)^{1/2}\), so the preceding inequalities prove
\(\widetilde\phi_0^2\le\widetilde\Psi(y\cdot\partial_x\widetilde\Psi)/|y|\).
Outside that support the left side vanishes. Thus (20) also holds, with an explicit nonzero constant on the required annulus, in every dimension. The proof in Sections 4–6 uses only nonnegativity, (19), and (20); replacing \(\Psi,\phi_0\) there by \(\widetilde\Psi,\widetilde\phi_0\) proves the same full estimate. The original convolution construction and its one-dimensional formula remain useful for Exercise 1, but no angular-convolution input is required for this alternative proof of the theorem.

<a id="noncritical-scaled-multiplier"></a>

## 4. Positivity after exchanging position and frequency

We may assume \(\chi\ne0\). On its compact support the velocity

\[
 v(\xi)=-\nabla P_0(\xi)
 \tag{23}
\]

has a positive minimum speed \(c_v\). Set \(\phi=\sqrt{c_v}\phi_0\) and, for \(R\ge1\), define

\[
 \begin{gathered}
 q_R(x,\xi)=\Psi(x/R,v(\xi))\chi(\xi),\\
 Q_R=q_R(x,D).
 \end{gathered}
 \tag{24}
\]

The expression is smooth on a neighborhood of the support of \(\chi\), where \(v\ne0\), and extends by zero outside that neighborhood. All velocity derivatives and inverse speeds are bounded on the fixed frequency support. Position derivatives satisfy

\[
 R^{-k}\langle x/R\rangle^{-k}
 =(R^2+|x|^2)^{-k/2}\le X^{-k}.
 \tag{25}
\]

It follows that \(q_R\) is uniformly in \(S(\Xi^{-L},G_1)\) for every fixed \(L\), and also in \(S(\Xi^{-L},G_\delta)\).

Since only \(\Psi\) has a position derivative, the leading commutator term is real even for complex \(\chi\):

\[
 \begin{aligned}
 -\overline{q_R}\nabla P_0\cdot\partial_xq_R
 &=R^{-1}|\chi|^2\\
 &\quad\cdot\Psi(x/R,v)\Psi'(x/R,v).
 \end{aligned}
 \tag{26}
\]

By (20) and \(|v|\ge c_v\), the symbol

\[
 \begin{aligned}
 s_R={}&-\overline{q_R}\nabla P_0\cdot\partial_xq_R\\
       &-R^{-1}\phi(x/R)^2|\chi(\xi)|^2
 \end{aligned}
 \tag{27}
\]

is real and nonnegative. It is uniformly in \(S(X^{-1},G_1)\), with rapid frequency decay. For its first term this follows from one positive position derivative in (26); the second has annular position support \(|x|\) comparable to \(R\), and each derivative has the matching scaling power.

<a id="noncritical-positivity"></a>

**Lemma 4.1.** Uniformly in \(R\ge1\),

\[
 \begin{gathered}
 \operatorname{Re}(s_R(x,D)u,u)
 \ge-C\|X^{-1}u\|_2^2,\\
 u\in L^2.
 \end{gathered}
 \tag{28}
\]

**Proof.** Let \(\mathcal F\) be the unitary Fourier transform. Direct substitution in the left Fourier formula, followed by the change of variable \(\eta=-x\), gives

\[
 \begin{gathered}
 \mathcal F\,s_R(x,D)\,\mathcal F^{-1}
       =\operatorname{Op}_{\mathrm{right}}(b_R),\\
 b_R(y,\eta)=s_R(-\eta,y).
 \end{gathered}
 \tag{29}
\]

The new coefficient is evaluated at the input position, which is right quantization. Conjugating its kernel and exchanging the variables shows that its adjoint is left quantization of the same real symbol \(b_R\). An operator and its adjoint have the same real quadratic form.

By (9), the original nonnegative symbol has the uniform bounds
\(|\partial_x^\alpha\partial_\xi^\beta s_R|\le C_{\alpha\beta}X^{-1-|\alpha|}\Xi^{-|\beta|}\).
The complete programme proof [Weighted positivity from Gaussian packets, Theorem 1](../providers/analysis/weighted-positivity.md#weighted-positivity) therefore gives (28) directly, with a constant independent of \(R\). Its proof includes the bounded-amplitude estimate, the positive Gaussian packet operator at each spatial scale, the quantization error and the sum of all localization errors. It covers the full displayed class without needing the additional rapid frequency decay available for this particular \(s_R\).

In the Fourier variables, its exact equivalent statement is

\[
 \operatorname{Re}(\operatorname{Op}_{\mathrm{left}}(b_R)w,w)
 \ge-C\|w\|_{H^{-1}}^2.
 \tag{30}
\]

Indeed \(b_R(y,\eta)=s_R(-\eta,y)\) obeys
\(|\partial_y^\beta\partial_\eta^\alpha b_R|\le C_{\alpha\beta}\langle\eta\rangle^{-1-|\alpha|}\langle y\rangle^{-|\beta|}\),
and [the programme proof's Fourier form](../providers/analysis/weighted-positivity.md#rotated-negative-order) proves (30) for that full class. Plancherel identifies
\(\|\mathcal Fu\|_{H^{-1}}=\|X^{-1}u\|_2\).
The symbol's frequency order is \(-1\), while the error is the squared \(H^{-1}\) norm. The finite-derivative bound and Schwartz density extend the quadratic form inequality to every \(L^2\) input. Thus (29)–(30) also recover (28), with its exact weight and uniform constant. \(\square\)

<a id="noncritical-conjugation"></a>
### An alternative proof by conjugation

The sharp lower-bound method of Hörmander [H3, Theorem 18.1.14] and Lerner [L, Theorem 2.5.4] also yields (30) through an order-one symbol. Write
\(Y=\langle y\rangle\), \(H=\langle\eta\rangle\),
\(G'_1=Y^{-2}|dy|^2+H^{-2}|d\eta|^2\), and \(J=\langle D_y\rangle\).
The displayed derivative bounds for \(b_R\) say exactly that
\(b_R\in S(H^{-1},G'_1)\), uniformly in \(R\). Thus
\(c_R=H^2b_R\geq0\) belongs uniformly to \(S(H,G'_1)\).
The [order-one positivity proof in The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md#domain-half-order-conjugation) applies, with variables renamed, and gives
\[
 \operatorname{Re}(\operatorname{Op}_{\mathrm{left}}(c_R)v,v)
       \geq-C\|v\|_2^2,\qquad v\in\mathcal S.
\]
That proof derives this bound from ordinary order-zero positivity by half-order conjugation; its constant depends on finitely many uniform symbol seminorms.

The [finite weighted composition formula](../providers/analysis/finite-weighted-calculus.md#finite-composition) gives the exact identity
\[
 J\operatorname{Op}_{\mathrm{left}}(b_R)J
   =\operatorname{Op}_{\mathrm{left}}(c_R)+T_R,
 \qquad T_R\in\operatorname{Op}S(Y^{-1},G'_1).
\]
Right multiplication by \(J\) multiplies the left symbol exactly by \(H\). In the remaining left composition, the zeroth term is \(H^2b_R\), of weight \(H\). The remainder gains one factor \(Y^{-1}H^{-1}\), so its weight is \(Y^{-1}\). The [finite-derivative operator bound](../providers/analysis/finite-derivative-l2.md#finite-derivative-l2) therefore bounds \(T_R\) on \(L^2\), uniformly in \(R\).

For \(w\in\mathcal S\), set \(v=J^{-1}w\). Fourier powers preserve \(\mathcal S\), and \(J\) is symmetric there. Consequently
\[
 \begin{aligned}
 \operatorname{Re}(\operatorname{Op}_{\mathrm{left}}(b_R)w,w)
 &=\operatorname{Re}((\operatorname{Op}_{\mathrm{left}}(c_R)+T_R)v,v)\\
 &\geq-(C+\|T_R\|)\|v\|_2^2
 =-C'\|w\|_{H^{-1}}^2.
 \end{aligned}
\]
This recovers (30). Boundedness of \(\operatorname{Op}_{\mathrm{left}}(b_R)\) and Schwartz density extend it to \(L^2\). Applying the exact Fourier and adjoint identities (29), with \(w=\mathcal Fu\), gives (28). The argument uses only the full displayed derivative bounds; compact frequency support is unnecessary.

## 5. The full long-range commutator error

<a id="noncritical-commutator"></a>

**Lemma 5.1.** Put \(a_0=(1+\delta)/2\). There are uniformly bounded operators
\(E_R:L^2_{-a_0}\to L^2_{a_0}\) such that

\[
 \begin{aligned}
 Q_R^*[P,Q_R]/i={}&s_R(x,D)\\
 &+R^{-1}\chi(D)^*\phi(x/R)^2\chi(D)\\
 &+E_R.
 \end{aligned}
 \tag{31}
\]

In particular

\[
 |(E_Ru,u)|\le C\|X^{-a_0}u\|_2^2.
 \tag{32}
\]

**Proof.** All assertions first concern Schwartz inputs and their exact left symbols. The finite adjoint remainder in the \(G_1\) calculus gives

\[
 q_R^\dagger=\overline{q_R}+t_R,\qquad
 t_R\in S(X^{-1}\Xi^{-L},G_1)
 \tag{33}
\]

for every fixed \(L\), uniformly in \(R\).

<a id="noncritical-free-error"></a>

For \(P_0(D)\), direct Leibniz expansion gives the exact finite commutator symbol

\[
 \sum_{1\le|\alpha|\le m}
 \frac{\partial_\xi^\alpha P_0\,D_x^\alpha q_R}{\alpha!}.
 \tag{34}
\]

After division by \(i\), its degree-one term is
\(-\nabla P_0\cdot\partial_xq_R\).
Every term of higher degree has at least two position derivatives and weight \(X^{-2}\), with arbitrary rapid frequency decay. The product with \(\overline{q_R}\) has leading term in (26); its one-order composition remainder has weight \(X^{-2}\) as well. The correction \(t_R\) in (33), multiplied by the degree-one term, has that same weight. Thus the entire free commutator differs from (26) by a uniformly bounded family in \(\operatorname{Op}S(X^{-2},G_1)\).

<a id="noncritical-long-range-error"></a>

For \(V_L\), write \(v_L(x,\xi)=\sum b_\alpha(x)\xi^\alpha\). It belongs to \(S(X^{-\delta}\Xi^m,G_\delta)\), and every positive position derivative has the stronger bound in (5). In the finite expansion of \([V_L,Q_R]\), degree zero cancels because the symbols are scalar. Each positive-degree coefficient is a difference of

\[
 \begin{gathered}
 (\partial_\xi^\alpha v_L)(D_x^\alpha q_R),\\
 (\partial_\xi^\alpha q_R)(D_x^\alpha v_L),
 \qquad |\alpha|\ge1.
 \end{gathered}
 \tag{35}
\]

The first product has position weight \(X^{-\delta-|\alpha|}\), and the second \(X^{-1-\delta|\alpha|}\). Both have weight at most \(X^{-1-\delta}\) and rapid frequency decay. Further position derivatives preserve the normalized bounds: if they hit a coefficient in the first product, (5) improves its estimate; in the second product there is already a positive coefficient derivative, giving \(X^{-1-\delta(|\alpha|+|\beta|)}\).

The exact remainder after \(N\) terms has weight

\[
 \begin{aligned}
 X^{-\delta}\Xi^{m-L}h_\delta^N
 &=X^{-\delta(N+1)}\Xi^{m-L-N}.
 \end{aligned}
 \tag{36}
\]

Choose a fixed integer \(N\) with \(\delta N\ge1\), and use the arbitrary rapid frequency weights of \(q_R\). This puts the remainder, and hence the whole commutator, in \(S(X^{-1-\delta}\Xi^{-L_0},G_\delta)\) for every prescribed \(L_0\). Multiplication by \(Q_R^*\) preserves this class. Since \(\delta\le1\), the free error of weight \(X^{-2}\) belongs to it too.

Finally, compare the left symbol \(R^{-1}\phi(x/R)^2|\chi|^2\) with the positive operator
\(R^{-1}\chi(D)^*\phi(x/R)^2\chi(D)\).
Right frequency multiplication is exact. The finite one-order remainder for the remaining left factor contains one position derivative of \(R^{-1}\phi(x/R)^2\); its annular support and scaling give weight \(X^{-2}\), uniformly in \(R\). Thus their discrepancy belongs to the same allowed error class.

This proves (31) with a symbol error in \(S(X^{-1-\delta},G_\delta)\). Formula (11) gives its uniform map \(L^2_{-a_0}\to L^2_{a_0}\). Weighted Cauchy–Schwarz proves (32). The finite-calculus operator identities agree with the weighted extensions by Schwartz density. \(\square\)

The stronger positive derivative bound in (5) is used explicitly in (35). A generic first-order metric remainder would only give \(X^{-2\delta}\), which does not reach the needed decay when \(\delta<1\).

<a id="noncritical-domain"></a>

## 6. The equation, its domain and the full shell norm

All coefficients of \(P\) are bounded, so \(P:H^m\to L^2\) is continuous. Symmetry on \(\mathcal S\) extends by \(H^m\)-density to
\((Pv,w)=(v,Pw)\) for \(v,w\in H^m\).
The weight-one mapping theorem gives uniform \(Q_R:H^m\to H^m\) and \(Q_R:L^2\to L^2\). Consequently the exact identity

\[
 \begin{aligned}
 \operatorname{Im}(Q_Rf,Q_Ru)
 ={}&\operatorname{Im}([Q_R,P]u,Q_Ru)\\
    &-\operatorname{Im}z\,\|Q_Ru\|_2^2
 \end{aligned}
 \tag{37}
\]

holds for every \(u\) in (6). To justify it, first expand on Schwartz inputs, using symmetry of \(P\), and then approximate \(u\) in \(H^m\). All displayed terms converge in \(L^2\). The approximating forcing terms need only converge in \(L^2\) for this identity.

<a id="noncritical-sign"></a>

Suppose first \(\operatorname{Im}z>0\). Set \(W_R=([P,Q_R]u,Q_Ru)\). With the inner product linear in its first entry, \(\operatorname{Re}(W_R/i)=\operatorname{Im}W_R\). Equation (37) therefore gives \(\operatorname{Re}(Q_R^*[P,Q_R]u/i,u)=-\operatorname{Im}(Q_Rf,Q_Ru)-(\operatorname{Im}z)\|Q_Ru\|_2^2\), and hence

\[
 \begin{aligned}
 \operatorname{Re}(Q_R^*[P,Q_R]u/i,u)
 &\le |(Q_Rf,Q_Ru)|\\
 &\le\|Q_Rf\|_B\|Q_Ru\|_{B^*}.
 \end{aligned}
 \tag{38}
\]

Choose \(\chi'\in C_c^\infty\), supported away from critical frequencies and equal one near \(\operatorname{supp}\chi\). Define \(Q'_R\) with \(\chi'\) in place of \(\chi\) in (24). The exact right-frequency identity is

\[
 Q_R=Q'_R\chi(D).
 \tag{39}
\]

Uniform weighted bounds for \(Q'_R\), followed by (13), bound its \(B\) and \(B^*\) norms independently of \(R\). Combining (28), (31), (32) and (38) therefore gives

\[
 \begin{aligned}
 &R^{-1}\|\phi(x/R)\chi(D)u\|_2^2\\
 &\quad\le C\|\chi(D)f\|_B\|\chi(D)u\|_{B^*}\\
 &\qquad+C\|X^{-a_0}u\|_2^2.
 \end{aligned}
 \tag{40}
\]

Here \(\|X^{-1}u\|_2\le\|X^{-a_0}u\|_2\), since \(a_0\le1\).

<a id="noncritical-shell-estimate"></a>

For each outer shell \(A_j\), choose \(R=2^{j-1}\). The function \(\phi(x/R)\) has a fixed nonzero value there, so the supremum of the left side of (40) controls every outer term in the squared \(B^*\) norm. The unit ball requires one more bound:

\[
 \begin{aligned}
 \|\chi(D)u\|_{L^2(A_0)}
 &\le C\|X^{-a_0}\chi(D)u\|_2\\
 &\le C_\chi\|X^{-a_0}u\|_2.
 \end{aligned}
 \tag{41}
\]

The last step is the weighted mapping theorem for the frequency multiplier. Thus, writing
\(Y=\|\chi(D)u\|_{B^*}\), \(F_0=\|\chi(D)f\|_B\) and \(U_0=\|X^{-a_0}u\|_2\), we obtain

\[
 Y^2\le C F_0Y+C U_0^2.
 \tag{42}
\]

All norms are finite before absorption: \(u\in H^m\subset L^2\subset B^*\), \(f\in B\), and the cutoff is bounded on these spaces. Young's inequality proves (7).

If \(\operatorname{Im}z<0\), replace \(P,z,f\) by \(-P,-z,-f\) and use the angular direction for \(-P_0\). The coefficient class and all remainder bounds are retained. The positive-half-plane argument gives the same estimate, with constants chosen as the maximum of the two fixed choices. For \(\chi=0\) the theorem is immediate. This proves Theorem 1.1 in its full stated range. \(\square\)

### Use the conclusion

Check the monotone multiplier in dimension one as well as higher dimensions. Carry the full commutator order through to the endpoint norm, including all long-range errors and both spectral signs.

<a id="noncritical-solutions"></a>

## 7. Graded exercises with complete solutions

**Exercise 1 — Basic: the commutator sign and a one-dimensional multiplier.** Derive (37) with an inner product linear in the first entry. For \(P_0(D)=D\) in dimension one and \(\operatorname{Im}z>0\), express \(\Psi(x,-1)\) as an integral of \(\psi\) and check the sign of the leading commutator.

**Solution 1.** Expand
\(Q(P-z)u=PQu+[Q,P]u-zQu\).
The first inner product \((PQu,Qu)\) is real by symmetry. Taking imaginary parts gives (37); multiplication by \(1/i=-i\) has real part equal to the imaginary part, so (38) has the displayed sign.

For \(y=-1\), the angular factor is \(1_{z<0}\). Changing variable \(w=x-z\) gives

\[
 \begin{gathered}
 \Psi(x,-1)=\int_x^\infty\psi(w)\,dw,\\
 \partial_x\Psi(x,-1)=-\psi(x).
 \end{gathered}
 \tag{43}
\]

The free velocity is \(\nabla P_0=1\). Hence the leading symbol for the multiplier \(q_R=\Psi(x/R,-1)\chi(\xi)\) is

\[
 -\overline{q_R}\partial_xq_R
 =R^{-1}|\chi|^2\Psi(x/R,-1)\psi(x/R)\ge0.
 \tag{44}
\]

For the other half-plane the replacement \(P_0\mapsto-P_0\) uses \(y=1\), whose half-line integral increases in \(x\), giving the appropriate reversed direction.

**Exercise 2 — Intermediate: uniform scaling and the annular term.** Prove uniform \(X^{-k}\) position derivative bounds for \(\Psi(x/R,y)\), \(R\ge1\), on any compact set of nonzero \(y\). Prove that \(R^{-1}\phi(x/R)^2\) has weight \(X^{-1}\), including all normalized position derivatives.

**Solution 2.** The chain rule and (19) bound every derivative of order \(k\) by
\(C R^{-k}\langle x/R\rangle^{-k}\).
Equation (25) makes this at most \(CX^{-k}\). Mixed \(y\) derivatives have the same estimate with fixed inverse powers of the positive minimum of \(|y|\).

On the support of any derivative of the annular function, \(cR\le|x|\le CR\) for fixed positive constants. Its derivative of order \(k\) is bounded by \(C_kR^{-1-k}\). Since \(R\ge1\), \(X\) is comparable to \(R\) there, proving the bound \(C_kX^{-1-k}\). Off the support it vanishes. No constant grows with \(R\).

**Exercise 3 — Intermediate: how many finite terms are enough?** Take \(\delta=1/4\). Explain why the generic one-order estimate for \([V_L,Q_R]\) misses the required position weight. Find a sufficient finite remainder order and show by a symbol example that the weaker class cannot simply be included in the stronger one.

**Solution 3.** The generic weight is \(X^{-\delta}h_\delta\), whose position factor is \(X^{-1/2}\). The required factor is \(X^{-1-\delta}=X^{-5/4}\). Choose \(N=4\); then the remainder in (36) has position factor
\(X^{-\delta(N+1)}=X^{-5/4}\).
The finitely many positive-degree coefficients have this weight by (35), while their frequency factors are harmless on the fixed compact support. Arbitrary additional frequency decay is supplied by choosing the input symbol weight accordingly.

For a nonzero \(\eta\in C_c^\infty\), the symbol \(X^{-1/2}\eta(\xi)\) belongs to \(S(X^{-1/2},G_{1/4})\): its position derivatives decrease even faster than the normalized metric cost requires. It is not in \(S(X^{-5/4},G_{1/4})\), since at a frequency where \(\eta\ne0\) the ratio of their zeroth weights grows like \(X^{3/4}\). Thus the missing position power requires the actual coefficient estimates and a sufficiently long finite expansion.

**Exercise 4 — Advanced: the exact Fourier specialization.** Let \(a\ge0\) be real and in \(S(X^{-1},G_1)\). Derive its Fourier-conjugated right symbol and use the proved sharp weighted lower bound to prove
\(\operatorname{Re}(a(x,D)u,u)\ge-C\|X^{-1}u\|_2^2\).
Keep the input symbol order and the Sobolev exponent distinct.

**Solution 4.** Inserting the two unitary Fourier transforms gives a kernel with phase \(x\cdot(\xi-\eta)\). Substitution of the new frequency \(-x\) yields the right symbol \(b(y,\theta)=a(-\theta,y)\), exactly as in (29). Its adjoint is left quantization of \(b\), because \(b\) is real. The real quadratic forms agree.

Its derivatives satisfy

\[
 |\partial_y^\beta\partial_\theta^\alpha b|
 \le C_{\alpha\beta}
       \langle\theta\rangle^{-1-|\alpha|}\langle y\rangle^{-|\beta|}.
 \tag{45}
\]

Consequently \(b\) is a nonnegative classical symbol of order \(-1\) in the full class of (P16) in [Weighted positivity from Gaussian packets](../providers/analysis/weighted-positivity.md#rotated-negative-order). That result is proved there from the positive packet operator, its quantization errors and weighted localization; it gives
\(\operatorname{Re}(\operatorname{Op}_{\mathrm{left}}(b)w,w)\ge-C\|w\|_{H^{-1}}^2\).
No compact frequency support has been imposed on \(a\), so all the hypotheses of this exercise are retained. The squared error has Sobolev exponent \(-1\); equivalently its input symbol order is \(2s+1=-1\) with \(s=-1\). Using
\(\|\mathcal Fu\|_{H^{-1}}=\|X^{-1}u\|_2\),
proves the claim. Using \(s=-1/2\) would correspond to an order-zero input and would lose the required spatial error weight.

There is also a conjugation proof. Apply the [alternative argument in Section 4](#noncritical-conjugation) to the symbol \(b\) in (45): \(\langle\theta\rangle^2b\) is nonnegative of order one in the metric \(\langle y\rangle^{-2}|dy|^2+\langle\theta\rangle^{-2}|d\theta|^2\), and the exact conjugation remainder has weight \(\langle y\rangle^{-1}\). Pairing with \(\langle D_y\rangle^{-1}\mathcal Fu\) gives the same squared \(H^{-1}\) error and hence the stated spatial weight, with no support restriction on \(a\).

**Exercise 5 — Advanced: the unit ball and absorption.** Show that the annular supremum in (40) alone need not control a full \(B^*\) norm. Explain how (41) repairs this for the frequency-localized solution. Finally deduce a linear estimate from \(Y^2\le A F_0Y+B U_0^2\), with all quantities nonnegative.

**Solution 5.** Choose a nonzero smooth function supported in \(|x|<1/2\). Since \(\phi\) is supported in \(3/4<|x|<9/4\), its product with \(\phi(x/R)\) vanishes for every \(R\ge1\), although its \(B^*\) norm is positive. Thus the missing unit ball has to be supplied.

On that ball, \(X^{a_0}\le2^{a_0/2}\). This bounds its unweighted norm by the \(L^2_{-a_0}\) norm of \(\chi(D)u\). The all-real weighted multiplier estimate then bounds it by \(C_\chi\|u\|_{L^2_{-a_0}}\), which is (41). The annular estimate and this local bound together control every shell.

Finally \(A F_0Y\le Y^2/2+A^2F_0^2/2\). Therefore

\[
 \begin{gathered}
 Y^2\le A^2F_0^2+2B U_0^2,\\
 Y\le A F_0+\sqrt{2B}\,U_0.
 \end{gathered}
 \tag{46}
\]

This is the required linear estimate. In the theorem \(Y\) is already finite because the solution lies in \(L^2\); the absorption therefore uses an inequality between finite numbers.

## 8. Reading and further directions


[L] Nicolas Lerner, [*Metrics on the Phase Space and Non-Selfadjoint Pseudo-Differential Operators*, Chapter 2](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Theorems 2.3.18–2.3.19 and 2.5.1, gives general quantization change, finite left composition and order-zero boundedness. The complete programme calculus proof above supplies these steps for the actual metric used here. Definition 2.4.1 and Proposition 2.4.3(1)–(3) give the positive Gaussian construction used in the separate programme proof of weighted positivity. That programme proof supplies the localization, amplitude bound and error estimates used by Lemma 4.1. The linked prerequisites give the same operator conventions.

Theorem 2.5.4 of [L], pp. 114–115, gives the order-one sharp lower bound used in the conjugation formulation. Section 4 links its complete programme proof and derives the negative-order specialization with its exact squared Sobolev error.

[AT] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), §3, Proposition 3.B and Lemma 3.C, uses a localized first-order evolution route. Its auxiliary Proposition 3.F has no complete proof in that transcription. The angular multiplier, sharp conjugation and finite commutator argument above prove the present estimate directly, without invoking 3.F.

The [off-energy estimate](the-resolvent-away-from-the-energy-surface.md) supplies the complementary gain of derivatives. Combining the two estimates requires accounting for the rough short-range remainder in the admissible splitting. The subsequent steps lead to boundary values of the resolvent and information about the point spectrum.

[H3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, reprint of the 1994 edition, Springer, 2007, Theorem 18.1.14 and its proof, pp. 76–78. ISBN 978-3-540-49938-1. [Edition information](https://doi.org/10.1007/978-3-540-49938-1).

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, §30.2, Proposition 30.2.4 and its proof, pp. 286–288. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
