# The resolvent away from the energy surface

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Why must an off-energy inverse control both position and frequency?** Away from the energy surface, a reciprocal gives derivative gain. A residual that is only smooth in frequency can still have a long spatial tail, so it need not preserve arbitrary polynomial weights. The corrected inverse therefore needs cutoffs and decay in both variables. This is the first half of a resolvent estimate, with the characteristic frequencies deliberately left for a different argument.

An equation can be difficult at the frequencies where its principal constant-coefficient part equals the energy, while remaining elliptic everywhere else. A long-range perturbation becomes small at distant positions, so the off-energy reciprocal exists outside a compact set in phase space. We correct that reciprocal to obtain a full gain of derivatives in weighted spaces. The error must decrease rapidly in position as well as frequency: frequency smoothing alone cannot transfer an arbitrary spatial weight.

Read [Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-symbol-mapping) for the metric, all-real weighted scales and their mapping theorem, and [Admissible differential perturbations](admissible-differential-perturbations.md#admissible-regularization) for the smooth long-range splitting. We use [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md), whose Section 1 proves symbol completeness and reciprocal estimates, Theorem 4.1 proves finite left composition, and Section 5 proves the common operator action and uniqueness of the left symbol. The Fourier facts and Euclidean interchanges are proved in [A finite-derivative bound for left quantization](../providers/analysis/finite-derivative-l2.md#fourier-normalization). Their required interfaces are recalled below. See also Lerner [L]. The joint summation and its weighted residual are constructed here.

Write \(D=-i\partial\), \(\langle x\rangle=(1+|x|^2)^{1/2}\), and

\[
 \begin{gathered}
 J_s=\langle D\rangle^s,\qquad M_t=\langle x\rangle^t,\\
 \|u\|_{s,t}=\|M_tJ_su\|_2.
 \end{gathered}
 \tag{1}
\]

All weighted and Sobolev exponents below are real. The spaces \(H^{s,t}\) are defined on tempered distributions, as in the preceding lesson.

We use the unitary Fourier transform \(\widehat u(\xi)=(2\pi)^{-n/2}\int e^{-ix\cdot\xi}u(x)\,dx\). The operator kernel still has prefactor \((2\pi)^{-n}\), from the transform followed by its inverse. The product formula in the exercises consequently has prefactor \((2\pi)^{-n/2}\).

## 1. The complete off-energy theorem

Let \(P_0(D)\) be a scalar constant-coefficient operator of order \(m\ge1\), with real coefficients and elliptic principal polynomial \(p_m\). Consider its smooth long-range perturbation

\[
 \begin{gathered}
 P=P_0(D)+V_L(x,D),\\
 V_L(x,D)=\sum_{|\alpha|\le m}b_\alpha(x)D^\alpha.
 \end{gathered}
 \tag{2}
\]

Assume \(V_L\) is symmetric on Schwartz functions, the total principal symbol is elliptic, and, for some fixed \(0<\delta\le1\), its coefficients satisfy

\[
 \begin{aligned}
 |b_\alpha(x)|&\le C_\alpha\langle x\rangle^{-\delta},\\
 |\partial_x^\beta b_\alpha(x)|
 &\le C_{\alpha\beta}\langle x\rangle^{-1-\delta|\beta|}
       &&(|\beta|\ge1).
 \end{aligned}
 \tag{3}
\]

The coefficients may be complex. In particular symmetry need not make the full left symbol real; ordering corrections can have imaginary lower-order coefficients.

<a id="off-energy-coefficient-class"></a>
For the smooth part of a 1-admissible perturbation, the [regularization theorem](admissible-differential-perturbations.md#admissible-regularization) permits any \(0<b<\varepsilon<1\). At \(K=1\), its derivative budget is exactly \(M(0)=b\) and \(M(q)=1+bq\) for every integer \(q\ge1\). Thus (3) holds with \(\delta=b\). The [exterior elliptic splitting](admissible-differential-perturbations.md#admissible-exterior-ellipticity) cuts off the smooth coefficients near a sufficiently large compact set and symmetrizes the expression while preserving this entire budget. Its leading coefficients are uniformly small compared with \(p_m\), ensuring total ellipticity. Hence the hypotheses include that smooth long-range equation, with an explicit common choice of \(\delta\) for all derivative orders. The theorem below retains the displayed larger range \(0<\delta\le1\).

Fix \(\lambda\in\mathbb R\), and let

\[
 M_\lambda=\{\xi\in\mathbb R^n:P_0(\xi)=\lambda\}.
 \tag{4}
\]

This set is compact and can be empty. Let \(\chi\in C_c^\infty(\mathbb R^n)\) equal one on a neighborhood of \(M_\lambda\).

<a id="off-energy-theorem"></a>
**Theorem 1.1.** There is \(r>0\) such that, if \(u\in\mathcal S'\) solves

\[
 (P-z)u=f,\qquad f\in H^{s,t},\qquad |z-\lambda|<r,
 \tag{5}
\]

then

\[
 (I-\chi(D))u\in H^{s+m,t}.
 \tag{6}
\]

For every fixed pair \(s',t'\in\mathbb R\), there is a constant \(C\), uniform in \(z\) in this disc, such that

\[
 \|(I-\chi(D))u\|_{s+m,t}
 \le C\bigl(\|f\|_{s,t}+\|u\|_{s',t'}\bigr)
 \tag{7}
\]

whenever the right side is finite. The radius can be chosen before the exponents in the estimate.

The energy need not be a regular value of \(P_0\), and \(z\) may be real. Membership (6) holds for every tempered solution, even before any auxiliary norm of \(u\) is known to be finite. The theorem controls the frequencies outside the energy neighborhood; estimates inside it require a different argument.

## 2. The smooth calculus used in the proof

We use the same metric and Planck weight as in the preceding lesson:

\[
 \begin{aligned}
 G_{\delta,(x,\xi)}(y,\eta)
 &=\langle x\rangle^{-2\delta}|y|^2
    +\langle\xi\rangle^{-2}|\eta|^2,\\
 h(x,\xi)&=\langle x\rangle^{-\delta}\langle\xi\rangle^{-1}\le1.
 \end{aligned}
 \tag{8}
\]

The metric is slowly varying, symplectically temperate, satisfies uncertainty, and has orthogonal position and frequency directions. All real product powers of the two Japanese brackets are temperate weights. These facts were proved in the weighted-space lesson.

For a positive weight \(w\), write \(S(w)\) for \(S(w,G_\delta)\) in this lesson. Its coordinate estimates are

\[
 |\partial_x^\beta\partial_\xi^\alpha a|
 \le C_{\alpha\beta}w\langle x\rangle^{-\delta|\beta|}
                         \langle\xi\rangle^{-|\alpha|}.
 \tag{9}
\]

Use the left quantization \(a(x,D)\). Each such operator acts on both \(\mathcal S\) and \(\mathcal S'\). If \(a\in S(w_1)\), \(b\in S(w_2)\), their composition has left symbol \(a\circ_L b\in S(w_1w_2)\), agrees with operator composition on these spaces, and for every integer \(N\ge1\) obeys

\[
 \begin{aligned}
 a\circ_L b-&
 \sum_{|\gamma|<N}\frac{\partial_\xi^\gamma a\,D_x^\gamma b}{\gamma!}\\
 &\in S(h^Nw_1w_2).
 \end{aligned}
 \tag{10}
\]

Every target seminorm is bounded by finitely many source seminorms, with fixed metric and weight constants. This is Theorem 4.1, with the operator identities in Section 5, of the [complete programme calculus proof](../providers/analysis/finite-weighted-calculus.md#finite-composition). It does not assert convergence of the untruncated formal series.

The symbol spaces are complete. A nonvanishing symbol of size at least \(cw\) has a reciprocal of weight \(w^{-1}\); the derivative estimates follow by differentiating \(aa^{-1}=1\) and induction. The pointwise version of this recursion also applies on a region where that lower bound holds. [Section 1 of the calculus proof](../providers/analysis/finite-weighted-calculus.md#symbol-completeness-and-reciprocal) gives both arguments, including the pointwise reciprocal recursion (C4a).

Finally the weighted mapping theorem gives

\[
 \begin{gathered}
 a\in S(\langle\xi\rangle^{-m})\\
 \Longrightarrow
 a(x,D):H^{s,t}\longrightarrow H^{s+m,t}.
 \end{gathered}
 \tag{11}
\]

All these estimates are uniform on symbol families with uniform seminorms. In this proof “uniform” means uniform in the fixed small closed disc of spectral parameters, separately at each symbol derivative order.

## 3. A reciprocal outside a compact phase region

<a id="off-energy-reciprocal"></a>
**Lemma 3.1.** Choose \(\chi_0\in C_c^\infty\), equal one near \(M_\lambda\), with its support contained in an open set on which \(\chi=1\). There are a smooth cutoff \(\theta(x,\xi)\), equal one outside a compact phase set, and \(r>0\), such that

\[
 \begin{gathered}
 e_z(x,\xi)=
 \frac{\theta(x,\xi)(1-\chi_0(\xi))}
      {P_0(\xi)+V_L(x,\xi)-z},\\
 e_z\in S(\langle\xi\rangle^{-m}).
 \end{gathered}
 \tag{12}
\]

is well defined by smooth extension across the zero-numerator region and has uniform seminorms for \(|z-\lambda|\le r\).

**Proof.** Ellipticity of \(p_m\) and compactness of the unit sphere give \(|P_0(\xi)|\ge c|\xi|^m\) for sufficiently large \(|\xi|\). Hence (4) is compact. Choose nested neighborhoods of this compact set inside a neighborhood where \(\chi\) is identically one, and choose \(\chi_0=1\) on the smaller one, denoted \(U_0\). If \(M_\lambda\) is empty, take \(U_0=\varnothing\) and \(\chi_0=0\).

The total principal polynomial

\[
 A_m(x,\xi)=p_m(\xi)+\sum_{|\alpha|=m}b_\alpha(x)\xi^\alpha
 \tag{13}
\]

has a uniform modulus lower bound \(c_0|\xi|^m\). At distant positions this follows from decay of the leading coefficients and the lower bound for \(p_m\). On the remaining compact position set it follows from ellipticity and compactness of that set times the unit sphere. All lower coefficients are bounded. Therefore, first fixing \(|z-\lambda|\le1\), we can choose \(T\) so large that

\[
 \begin{gathered}
 |P_0(\xi)+V_L(x,\xi)-z|
 \ge c_1\langle\xi\rangle^m,\\
 |\xi|\ge T,\quad x\in\mathbb R^n.
 \end{gathered}
 \tag{14}
\]

This uses subtraction of the bounded lower-order terms from the principal modulus. It does not require the full denominator to be real or the principal symbol to be positive.

If the compact set \(\{|\xi|\le T\}\setminus U_0\) is empty, choose \(r=1\) and any positive \(R\); (14) already covers every active frequency outside \(U_0\). If it is nonempty, \(P_0(\xi)-\lambda\) has a positive modulus lower bound there, say \(d\). Decay in (3) makes \(|V_L(x,\xi)|\le d/4\) on it when \(|x|\ge R\), for a sufficiently large \(R\). Choose \(0<r\le\min(1,d/4)\). In this case

\[
 \begin{gathered}
 |P_0(\xi)+V_L(x,\xi)-z|\ge d/2
 ,\\
 |x|\ge R,\quad|\xi|\le T,\quad\xi\notin U_0.
 \end{gathered}
 \tag{15}
\]

After decreasing the constant, (14)–(15) give a bound \(c\langle\xi\rangle^m\) on the relevant region.

Take compact smooth functions \(\varphi,\psi\) equal one on the position ball of radius \(R\) and the frequency ball of radius \(T\), respectively, and put

\[
 \theta(x,\xi)=1-\varphi(x)\psi(\xi).
 \tag{16}
\]

Whenever \(\theta\ne0\), either \(|x|>R\) or \(|\xi|>T\). On the support of \(1-\chi_0\), the frequency lies outside \(U_0\). Thus the denominator is uniformly nonzero on the active region of (12). Inside \(U_0\) the numerator vanishes identically; where both cutoffs are one it also vanishes identically. Extending by zero across those excluded regions makes a smooth global symbol. At their boundaries the same nonvanishing estimate, or the identically vanishing numerator in a neighborhood, gives the extension.

Let \(p_z=P_0+V_L-z\). Formula (3), with \(\delta\le1\), implies \(p_z\in S(\langle\xi\rangle^m)\) uniformly. Apply the reciprocal derivative recursion at each point of the active region, where \(|p_z|\ge c\langle\xi\rangle^m\). The resulting derivatives of \(p_z^{-1}\) have exactly the weight \(\langle\xi\rangle^{-m}\). The numerator is in \(S(1)\), and derivatives of \(\theta\) have compact phase support. Product differentiation proves (12) and its uniform bounds. \(\square\)

<a id="off-energy-first-error"></a>
Set \(E_z=e_z(x,D)\) and \(A_z=P-z\). The \(N=1\) case of (10) gives the exact operator identity

\[
 E_zA_z=I-\chi_0(D)-R_z,\qquad r_z\in S(h),
 \tag{17}
\]

uniformly in \(z\), where \(r_z\) is the left symbol of \(R_z\). Indeed the pointwise leading product is \(\theta(1-\chi_0)\). Its discrepancy from \(1-\chi_0\) has compact phase support, hence belongs to \(S(h)\), and the composition error has weight \(h\). No support property for the exact symbol \(r_z\) is inferred.

## 4. Summation with cutoffs in both variables

The residual becomes small in either distant position or large frequency:

\[
 h(x,\xi)\longrightarrow0
 \quad\text{as }|(x,\xi)|\longrightarrow\infty.
 \tag{18}
\]

This allows an asymptotic sum with a joint Schwartz error.

<a id="off-energy-joint-summation"></a>
**Lemma 4.1.** Suppose, for each \(j\ge0\), \(b_{j,z}\) is a uniformly bounded family in \(S(w h^j)\), with \(w=\langle\xi\rangle^{-m}\). There is a uniformly bounded family \(b_z\in S(w)\) satisfying, for every \(N\ge1\),

\[
 b_z-\sum_{j<N}b_{j,z}\in S(w h^N)
 \quad\text{uniformly in }z.
 \tag{19}
\]

**Proof.** Choose \(\rho\in C_c^\infty(\mathbb R^n)\) with \(0\le\rho\le1\), equal one near zero, and for \(L\ge1\) set

\[
 q_L(x,\xi)=1-\rho(x/L)\rho(\xi/L).
 \tag{20}
\]

These cutoffs are uniformly bounded in \(S(1)\). A positive position derivative of a cutoff is supported where \(|x|\) is comparable to \(L\); there
\(L^{-|\beta|}\le C\langle x\rangle^{-\delta|\beta|}\)
because \(\delta\le1\). Frequency derivatives have
\(L^{-|\alpha|}\le C\langle\xi\rangle^{-|\alpha|}\)
on their supports. Mixed derivatives have both bounds.

Every nonzero term in a differentiated product \(q_Lb_{j,z}\) is outside a phase ball of radius proportional to \(L\): this is true for \(q_L\) itself and for each of its nonzero derivatives. On that set \(h\) tends uniformly to zero. The product rule therefore gives, for fixed \(j,k,N\) with \(j>N\),

\[
 p_k(q_Lb_{j,z};w h^N)
 \le C_{j,k,N}\sup_{|(x,\xi)|\ge cL}h^{j-N}
 \longrightarrow0.
 \tag{21}
\]

Here \(p_k\) is a defining symbol seminorm; the constants use finitely many uniformly bounded source seminorms.

Choose \(L_j\) increasing so fast that the left side of (21) is at most \(2^{-j}\) for all derivative orders \(k\le j\) and all integers \(0\le N\le\lfloor j/2\rfloor\). These are finitely many conditions at each \(j\), and \(j-N>0\). Define

\[
 b_z=b_{0,z}+\sum_{j\ge1}q_{L_j}b_{j,z}.
 \tag{22}
\]

For each fixed derivative order the sufficiently late terms have summable seminorms in \(S(w)\). Completeness gives a symbol in that space, with uniform bounds. For fixed \(N,k\), the sufficiently late terms have summable seminorms in \(S(w h^N)\) as well. The finitely many terms with \(j\ge N\) before this tail also belong to that class, since \(h\le1\).

For \(1\le j<N\), the difference \((q_{L_j}-1)b_{j,z}\) has compact phase support and belongs to \(S(w h^N)\), with uniform bounds. The \(j=0\) term was left unchanged. Subtracting the finite sum in (19) proves the assertion. The same sequence of cutoffs works for the whole parameter family. \(\square\)

<a id="off-energy-schwartz-symbols"></a>
There is a useful exact identification:

\[
 \bigcap_{N\ge1}S(h^N)=\mathcal S(\mathbb R^{2n}).
 \tag{23}
\]

To prove it, \(h^N=\langle x\rangle^{-\delta N}\langle\xi\rangle^{-N}\). Given any required powers of both brackets and any derivative order, choose \(N\) large enough to dominate those powers. Formula (9) then gives every Schwartz bound. Conversely every Schwartz symbol satisfies all these weighted normalized derivative bounds. Uniform bounds in each \(S(h^N)\) give uniform Schwartz seminorms. Positivity of \(\delta\) is essential; Problem 1 explains the endpoint failure at \(\delta=0\).

## 5. Correcting the inverse without commuting cutoffs

Put

\[
 C=I-\chi(D),\qquad C_0=\chi_0(D).
 \tag{24}
\]

For each \(j\ge0\), take \(b_{j,z}\) to be the exact left symbol of \(CR_z^jE_z\). The composition theorem and (17) give

\[
 b_{j,z}\in S(\langle\xi\rangle^{-m}h^j)
 \tag{25}
\]

uniformly in \(z\), for each fixed \(j\). Let \(B_z\) be the operator of the joint asymptotic sum supplied by Lemma 4.1.

We first identify the cutoff error that finite telescoping leaves behind.

<a id="off-energy-separated-cutoffs"></a>
**Lemma 5.1.** For every fixed \(j\ge0\), the operator \(CR_z^jC_0\) has a uniformly Schwartz left symbol.

**Proof.** For \(j=0\) it is zero, since \((1-\chi)\chi_0=0\). For \(j\ge1\), let \(r_{j,z}\in S(h^j)\) be the left symbol of \(R_z^j\). Right multiplication by \(\chi_0(D)\) has the exact left symbol

\[
 r_{j,z}(x,\xi)\chi_0(\xi).
 \tag{26}
\]

This identity follows directly from the left Fourier formula on Schwartz inputs and then from the common distributional action. It does not hold in this pointwise form for a frequency multiplier placed on the left.

In the finite expansion (10) for the remaining left factor \(1-\chi(D)\), every term is

\[
 \frac{\partial_\xi^\gamma(1-\chi(\xi))}{\gamma!}
       (D_x^\gamma r_{j,z}(x,\xi))\chi_0(\xi)=0.
 \tag{27}
\]

For \(\gamma=0\), \(\chi=1\) on the support of \(\chi_0\); for positive \(\gamma\), all derivatives of \(\chi\) vanish on a neighborhood of that support. Thus the exact composition belongs to \(S(h^{N+j})\) for every \(N\), by the finite remainder estimate. Formula (23) makes it Schwartz, uniformly in \(z\). \(\square\)

An exact product can be nonzero even though all its finite expansion coefficients vanish. It is then measured by the remainder in every order. Problem 4 gives an explicit nonzero example of this phenomenon.

<a id="off-energy-exact-telescoping"></a>
For \(N\ge1\), (17) and finite telescoping give

\[
 \begin{aligned}
 &\left(\sum_{j<N}CR_z^jE_z\right)A_z\\
 &\quad=C-CR_z^N-\sum_{j<N}CR_z^jC_0.
 \end{aligned}
 \tag{28}
\]

Every factor keeps its indicated order. The last sum consists of Schwartz operators by Lemma 5.1; no cutoff has been commuted through \(R_z\).

By (19), \(B_z-\sum_{j<N}CR_z^jE_z\) has symbol in
\(S(\langle\xi\rangle^{-m}h^N)\). Multiplication by \(A_z\), whose symbol has weight \(\langle\xi\rangle^m\), puts its product in \(S(h^N)\). The term \(CR_z^N\) has this same weight. Consequently (28) implies

\[
 B_zA_z-C\in\operatorname{Op}S(h^N)
 \quad\text{for every }N.
 \tag{29}
\]

[Uniqueness of the left symbol](../providers/analysis/finite-weighted-calculus.md#weighted-exact-composition) makes these assertions about the same exact residual symbol. Formula (23) proves

\[
 \begin{gathered}
 B_zA_z=C+K_z,\\
 b_z\in S(\langle\xi\rangle^{-m}),\\
 k_z\in\mathcal S(\mathbb R^{2n}),
 \end{gathered}
 \tag{30}
\]

with uniform bounds in the indicated spaces. This argument uses only finite sums of the individually Schwartz cutoff errors. It does not assume that their unmodified infinite series converges.

<a id="off-energy-joint-kernel"></a>
## 6. What the joint Schwartz kernel controls

For a left Schwartz symbol \(k_z\), the explicit kernel is

\[
 \begin{aligned}
 &\mathcal K_z(x,y)\\
 &\quad=(2\pi)^{-n}\int
       e^{i(x-y)\cdot\xi}k_z(x,\xi)\,d\xi.
 \end{aligned}
 \tag{31}
\]

Partial inverse Fourier transformation followed by the invertible linear change \((x,y)\mapsto(x,x-y)\) preserves Schwartz space. Hence \(\mathcal K_z\) is uniformly Schwartz on \(\mathbb R^{2n}\). The Fourier reading proves Schwartz preservation, and the chain rule proves it for the displayed invertible linear substitution; thus (31) itself supplies this kernel construction.

The parameter-dependent version can be checked directly. Write \(v=x-y\). Multiplying the partial Fourier integral by any \(x^\alpha v^\beta\) and differentiating in \(x,v\) gives, after integration by parts in \(\xi\), a fixed normalization factor times the integral of
\(e^{iv\cdot\xi}x^\alpha\partial_\xi^\beta(\xi^\nu\partial_x^\gamma k_z(x,\xi))\).
Every such amplitude is bounded by \(C\langle\xi\rangle^{-n-1}\), uniformly in \(x,z\), from a finite list of Schwartz seminorms. Its integral is finite, proving all joint seminorm estimates. Under an invertible linear substitution, each coordinate polynomial and derivative becomes a finite linear combination of coordinate polynomials and derivatives, so the same bounds hold in \((x,y)\).

<a id="off-energy-tempered-inputs"></a>
**Lemma 6.1.** An operator with a uniformly Schwartz kernel maps every tempered distribution to a Schwartz function. For arbitrary fixed \(s',t',q,t\in\mathbb R\), it also satisfies

\[
 \|K_zu\|_{q,t}\le C\|u\|_{s',t'}
 \tag{32}
\]

uniformly in \(z\).

**Proof.** A tempered distribution \(u\) has a finite-order estimate on Schwartz tests, for some \(a,M\):

\[
 |\langle u,\phi\rangle|
 \le C_u\sum_{|\beta|\le a}
       \sup_y\langle y\rangle^M|\partial_y^\beta\phi(y)|.
 \tag{33}
\]

Indeed continuity of \(u\) at zero in the Schwartz topology supplies a neighborhood defined by finitely many seminorms on which \(|\langle u,\phi\rangle|\le1\). A common derivative order and polynomial weight dominate those seminorms by the sum in (33). Rescaling an arbitrary test into that neighborhood gives (33); if the sum vanishes, rescale by arbitrarily large constants to obtain zero. Thus the estimate follows from the definition of a tempered distribution, with no preliminary weighted norm assumption.

Apply this to \(\partial_x^\alpha\mathcal K_z(x,\cdot)\). Every resulting bound decreases faster than any power of \(\langle x\rangle\). To justify differentiation in the Schwartz test topology, apply the scalar Taylor formula in one \(x\)-coordinate: the difference between its difference quotient and its first derivative is bounded in each \(y\)-Schwartz seminorm by \(C|h|\), using the corresponding second \(x\)-derivative on a compact neighborhood of the fixed \(x\). The joint kernel bounds supply this constant uniformly in \(z\). Repeat for each \(x\)-derivative and then apply the continuous functional \(u\). Thus the resulting function \(K_zu\) has every Schwartz seminorm finite. This proves the first assertion for all tempered inputs.

<a id="off-energy-weighted-kernel"></a>
For the norm estimate conjugate by the weighted-space isometries:

\[
 T_z=M_tJ_qK_zJ_{-s'}M_{-t'}.
 \tag{34}
\]

Its kernel is again uniformly Schwartz. On the output variable the operators \(M_t,J_q\) preserve Schwartz space. On the input variable use their bilinear transposes in reverse order. The transpose of \(J_{-s'}\) is itself, because its Fourier multiplier is even; the transpose of multiplication is the same multiplication. Polynomially growing bracket multipliers, on either the position or Fourier side, preserve every Schwartz seminorm with a bound by finitely many such seminorms. Thus both variable operations retain uniform kernel bounds.

Let \(\widetilde{\mathcal K}_z\) denote this kernel. Cauchy–Schwarz in \(y\) and integration in \(x\) give

\[
 \|T_zv\|_2\le
 \|\widetilde{\mathcal K}_z\|_{L^2(\mathbb R^{2n})}\|v\|_2.
 \tag{35}
\]

The kernel norms are uniformly bounded. Apply this to \(v=M_{t'}J_{s'}u\), using the exact inverse \(J_{-s'}M_{-t'}\), to obtain (32). Schwartz approximation extends the norm estimate to the whole weighted space and agrees with the distributional kernel action. \(\square\)

<a id="off-energy-resolvent-estimate"></a>
**Proof of Theorem 1.1.** Apply (30) to the distributional equation (5):

\[
 (I-\chi(D))u=B_zf-K_zu.
 \tag{36}
\]

By (11), \(B_zf\in H^{s+m,t}\), with norm bounded uniformly by \(C\|f\|_{s,t}\). Lemma 6.1 puts \(K_zu\) in Schwartz space for every tempered \(u\), so it belongs to this target space without any preliminary auxiliary norm assumption. This proves (6). Apply (32), with \(q=s+m\), whenever the chosen initial norm is finite to obtain (7). All symbol, kernel and mapping constants were fixed before taking \(z\) toward the real axis. \(\square\)

The term involving \(u\) measures a compact phase-space error through a kernel that decreases rapidly in both variables. The frequency cutoff removes the energy surface; it does not impose any regularity of that surface. This explains why the theorem remains valid at critical energies and for empty energy shells.

### Use the conclusion

Inspect the joint Schwartz kernel and the finite composition remainder. State the weight transferred by that kernel; frequency smoothing by itself is not the asserted off-energy theorem.

<a id="off-energy-solutions"></a>
## 7. Graded exercises with complete solutions

**Exercise 1 — Basic: why both variables and positive \(\delta\) matter.** Show that outside a phase ball of radius \(L\), the weight in (8) is at most \(CL^{-\delta}\). Explain why the joint-summation argument fails with this weight at \(\delta=0\).

**Solution 1.** If \(|(x,\xi)|\ge L\), either \(|x|\ge L/\sqrt2\) or \(|\xi|\ge L/\sqrt2\). In the first case \(h\le C L^{-\delta}\), and in the second \(h\le C L^{-1}\le C L^{-\delta}\), since \(L\ge1\) and \(\delta\le1\). Thus (21) can be bounded by \(C_{j,k,N}L^{-\delta(j-N)}\), which tends to zero when \(j>N\). Finitely many such conditions can be made smaller than \(2^{-j}\) at each step.

For \(\delta=0\), \(h=\langle\xi\rangle^{-1}\) stays equal to one when \(\xi=0\) and \(|x|\to\infty\). It gives no smallness on that part of the cutoff support. The symbol \(e^{-|\xi|^2}\), independent of \(x\), belongs to every \(S(h^N,G_0)\) but is not Schwartz in phase space. Hence (23) and the required joint smallness both fail at that endpoint.

**Exercise 2 — Intermediate: infinitely smoothing is not enough for spatial weights.** Let \(A\) have left symbol \(e^{-|\xi|^2}\). Show that its kernel is smooth but not joint Schwartz, and that \(A\) does not map \(H^{0,-n}\) to \(H^{0,0}\).

**Solution 2.** Gaussian Fourier inversion gives

\[
 \mathcal K_A(x,y)=(4\pi)^{-n/2}e^{-|x-y|^2/4}.
 \tag{37}
\]

This decreases rapidly in \(x-y\), but it is the same nonzero constant on every point of the diagonal \(x=y\). It is not jointly decreasing in \(x,y\).

The tempered function \(u=1\) belongs to \(H^{0,-n}\), since
\(\int\langle x\rangle^{-2n}\,dx<\infty\) for \(n\ge1\). Its unitary Fourier transform is \((2\pi)^{n/2}\delta_0\); multiplication by \(e^{-|\xi|^2}\) leaves it unchanged. Thus \(Au=1\notin L^2=H^{0,0}\). Arbitrary frequency regularity does not replace the spatial decrease used in Lemma 6.1.

**Exercise 3 — Intermediate: critical and empty energy shells.** Take \(P_0(D)=-\Delta\), \(V_L=0\). Construct the off-energy inverse at \(\lambda=0\), including real \(z=0\). Then treat the empty shell \(\lambda=-1\) with \(\chi=0\).

**Solution 3.** At \(\lambda=0\), the shell is \(\{0\}\), where \(\nabla_\xi|\xi|^2=0\). Choose \(\chi=1\) on \(|\xi|<a\). On the support of \(1-\chi\), \(|\xi|\ge a\). If \(|z|<a^2/2\), then
\(\bigl||\xi|^2-z\bigr|\ge|\xi|^2/2\).
Define

\[
 b_z(\xi)=\frac{1-\chi(\xi)}{|\xi|^2-z},
 \tag{38}
\]

extended by zero where the numerator is identically zero. It is uniformly a symbol of weight \(\langle\xi\rangle^{-2}\), and
\(b_z(D)(-\Delta-z)=I-\chi(D)\) exactly. Therefore the weighted mapping theorem gives the conclusion for every tempered solution, with no auxiliary error term. In particular \(z=0\) is allowed despite the critical energy.

For \(\lambda=-1\) the shell is empty. If \(|z+1|<1/2\), then
\(\operatorname{Re}(|\xi|^2-z)\ge|\xi|^2+1/2\).
The global reciprocal \(b_z=(|\xi|^2-z)^{-1}\) is uniformly of weight \(\langle\xi\rangle^{-2}\). Its exact inverse identity gives \(u=b_z(D)f\), so the whole solution belongs to \(H^{s+2,t}\). No frequency neighborhood has to be removed.

**Exercise 4 — Advanced: a zero expansion with a nonzero product.** Let \(v(x)=e^{-|x|^2}\), let \(0\le\chi_0\in C_c^\infty\) equal one near zero, and let \(\chi\in C_c^\infty\) equal one near \(\operatorname{supp}\chi_0\). Prove that every finite left-product coefficient of
\((I-\chi(D))\,v(x)\chi_0(D)\)
vanishes, while the exact operator can be nonzero.

**Solution 4.** The rightmost two factors have left symbol \(v(x)\chi_0(\xi)\). Every coefficient with the remaining left factor is
\(\partial_\xi^\gamma(1-\chi)\,(D_x^\gamma v)\chi_0/\gamma!\),
which vanishes by the support conditions exactly as in (27). The finite remainder theorem therefore gives a Schwartz symbol for the exact product.

To see it is nonzero, its Fourier action is

\[
 \begin{aligned}
 &\widehat{Au}(\xi)\\
 &\quad=(1-\chi(\xi))(2\pi)^{-n/2}\\
 &\qquad\cdot
 \int \widehat v(\xi-\eta)\chi_0(\eta)\widehat u(\eta)\,d\eta.
 \end{aligned}
 \tag{39}
\]

The Gaussian transform is
\(\widehat v(\zeta)=2^{-n/2}e^{-|\zeta|^2/4}>0\).
Choose a nonzero nonnegative compact smooth \(\widehat u\) supported where \(\chi_0=1\). At any \(\xi\) outside \(\operatorname{supp}\chi\), the integral in (39) is strictly positive and the prefactor is one. Thus \(A\ne0\). A remainder can be smaller than every symbolic order without being the zero operator. The product is not obtained by commuting the frequency cutoff past \(v\).

**Exercise 5 — Advanced: the exact norm for a joint kernel.** Let \(g(x)=e^{-|x|^2}\) and \(Ku(x)=g(x)\langle u,g\rangle\). For arbitrary real \(s',t',q,t\), find a bound \(H^{s',t'}\to H^{q,t}\), keeping the order of the position and Fourier factors correct. Show that the resulting bound is the exact operator norm.

**Solution 5.** Put \(v=M_{t'}J_{s'}u\), so \(u=J_{-s'}M_{-t'}v\). Bilinear transposition, in reverse order, gives

\[
 \langle u,g\rangle
 =\langle v,M_{-t'}J_{-s'}g\rangle.
 \tag{40}
\]

Both this test function and \(M_tJ_qg\) are Schwartz. Cauchy–Schwarz yields

\[
 \|Ku\|_{q,t}\le
 \|M_tJ_qg\|_2\,\|M_{-t'}J_{-s'}g\|_2\,\|u\|_{s',t'}.
 \tag{41}
\]

The two constants are finite for every displayed exponent. Let \(h_0=M_{-t'}J_{-s'}g\), which is nonzero since the factors are invertible. Taking \(v=\overline{h_0}/\|h_0\|_2\) makes the bilinear Cauchy–Schwarz bound an equality and gives \(\|u\|_{s',t'}=1\). Thus the product of the two constants in (41) is the exact operator norm. Exchanging \(M_{-t'}\) and \(J_{-s'}\) in (40) would generally change that constant; reverse transposition determines the order.

## 8. Reading and further directions


[L] Nicolas Lerner, [*Metrics on the Phase Space and Non-Selfadjoint Pseudo-Differential Operators*, Chapter 2](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Theorems 2.3.7, 2.3.18–2.3.19 and 2.5.1, gives the general finite product, quantization change and order-zero bound. The complete programme proof linked above proves the particular calculus used here, and the preceding weighted-space lesson supplies the all-real mapping theorem.

[AT] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), §3, equations (3.2)–(3.5), gives the initial off-shell reciprocal and a finite-order error. Sections 4–6 above prove the additional joint residual needed for arbitrary initial weights.

[HJS] Andrew Hassell, Qiuye Jia and Ethan Sussman, [*Lecture notes on non-elliptic Fredholm theory*, arXiv:2604.18956v1](https://arxiv.org/abs/2604.18956v1), Proposition 2.3 and §2.4, constructs smooth scattering parametrices with Schwartz kernels. Proposition 4.10 states the localized version and refers back to that construction. Proposition 2.3 leaves the finite-to-asymptotic telescoping identity as an exercise. Here \(G_\delta\) admits the weaker position derivative scale, and Lemmas 4.1–6.1 supply the joint summation, exact finite telescoping and uniform kernel bounds used in this lesson.

The remaining part \(\chi(D)u\) lies near the energy surface and is not controlled by division by \(P_0-\lambda\). At noncritical frequencies its Hamiltonian direction can instead guide a positive-commutator estimate. Combining such an estimate with the off-energy result is the next step toward boundary values of the long-range resolvent, radiation conditions and the point spectrum. The off-energy theorem itself does not establish those conclusions.
