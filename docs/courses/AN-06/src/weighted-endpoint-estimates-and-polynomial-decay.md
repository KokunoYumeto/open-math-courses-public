# Weighted endpoint estimates and polynomial decay

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: How is one decay estimate promoted to every polynomial weight?** The vanishing-tail condition lets an exterior estimate absorb an annular error. A bounded approximation to a polynomial weight first keeps all operator constants uniform. Increasing the weight in finite steps then bootstraps the solution, rather than assuming that an unbounded weight is already allowed in the graph equation.

A solution whose mass per unit radius vanishes has more room for decay estimates than a general endpoint solution. If the forcing has a polynomial weight, the solution acquires the same weight in its endpoint derivative norms. We prove this uniformly on compact sets of regular energies. A homogeneous solution then has every polynomial Sobolev weight. This also makes the noncritical eigenvalues discrete and of finite multiplicity.

Read [Admissible differential perturbations](admissible-differential-perturbations.md) for the full rough coefficient class and its local multipliers, [The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md) for the realization, and [Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md) for the weighted norms. [The resolvent away from the energy surface](the-resolvent-away-from-the-energy-surface.md) supplies the complete off-energy theorem. The shell maps and unweighted commutator are in [A resolvent estimate at noncritical frequencies](a-resolvent-estimate-at-noncritical-frequencies.md). The primary rough map is proved in [Combining the long-range resolvent estimates](combining-the-long-range-resolvent-estimates.md). [Radiation for limits of long-range resolvents](radiation-for-limits-of-long-range-resolvents.md) constructs the exterior angular multiplier and proves the vanishing shell characterization. [Outgoing flux and vanishing shell mass](outgoing-flux-and-vanishing-shell-mass.md) explains how zero outgoing flux supplies that hypothesis.

The programme's [Finite composition and adjoints with spatial weights](../providers/analysis/finite-weighted-calculus.md) proves the exact finite products, complete remainders and common distributional action. [Weighted positivity from Gaussian packets](../providers/analysis/weighted-positivity.md#weighted-positivity), Theorem 1, proves the scalar positivity input; Section 6 of the radiation lesson supplies its explicit spatial conjugation at every fixed weight. Agmon [A] supplies the freely readable weighted-decay and eigenvalue construction to compare with. Sections 3–9 prove the finite commutator, arbitrary-weight and rough-coefficient arguments, including the signed escape direction. Lerner [L] and Teschl [T] provide free comparisons, with their actual proof roles specified in the references.

Put \(D=-i\partial\), \(X=\langle x\rangle\), \(\Xi=\langle\xi\rangle\), and use an inner product linear in its first entry. Our conventions are

\[
 \begin{gathered}
 \|u\|_{s,t}=\|X^t\langle D\rangle^s u\|_2,\\
 G_\theta=X^{-2\theta}|dx|^2+\Xi^{-2}|d\xi|^2.
 \end{gathered}
 \tag{1}
\]

All quantizations are left quantizations. Integer weighted Sobolev norms are equivalent to the square sum of \(\|X^tD^\alpha u\|_2\), \(|\alpha|\le m\).

## 1. The full uniformly weighted theorem

Let \(P_0(D)\) be a real scalar constant-coefficient elliptic operator of integer order \(m\ge1\), and let \(V\) be a symmetric \(1\)-admissible differential perturbation with its full sharp local coefficient hypotheses. Its self-adjoint realization \(H=P_0+V\) has domain \(H^m\). A free energy is regular when \(\nabla P_0\ne0\) on \(M_\lambda=\{P_0=\lambda\}\); an empty shell is allowed.

For \(A_0=\{|x|<1\}\), \(A_j=\{2^{j-1}\le|x|<2^j\}\), and \(R_j=2^j\), set

\[
 \begin{aligned}
 \|f\|_B&=\sum_{j\ge0}R_j^{1/2}\|f\|_{L^2(A_j)},\\
 \|u\|_{B^*}&=\sup_{j\ge0}R_j^{-1/2}\|u\|_{L^2(A_j)}.
 \end{aligned}
 \tag{2}
\]

The space \(\dot B^*\) is the closure of Schwartz functions in \(B^*\). The radiation lesson proves

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

These equivalences include the inner shell and all real radii. The \(B/B^*\) integral pairing is absolutely convergent.

**Theorem 1.1.** Let \(K\) be a compact set of regular free energies. Suppose \(\lambda\in K\) and

\[
 \begin{gathered}
 D^\alpha u\in\dot B^*,\qquad |\alpha|\le m,\\
 (H-\lambda)u=f,\qquad X^\gamma f\in B,\quad\gamma\ge0.
 \end{gathered}
 \tag{4}
\]

The equation uses the actual local coefficient products. Then

\[
 \begin{gathered}
 X^\gamma D^\alpha u\in B^*,\qquad |\alpha|\le m,\\
 \sum_{|\alpha|\le m}\|X^\gamma D^\alpha u\|_{B^*}\\
 \le C_{\gamma,K}\left(
       \|X^\gamma f\|_B+
       \sum_{|\alpha|\le m}\|D^\alpha u\|_{B^*}\right).
 \end{gathered}
 \tag{5}
\]

The constant is independent of \(u,f,\lambda\). No directional radiation condition is added. The vanishing shell hypothesis is essential to the cutoff passage in the proof.

We first work in a small neighborhood of one regular energy. Choose a real \(0\le\chi\le1\), compactly supported where \(v=\nabla P_0\ne0\), and equal one near every energy shell in this neighborhood. Such a fixed cutoff exists by compactness, ellipticity and regularity. Finitely many neighborhoods cover \(K\). If the shell is empty, a smaller neighborhood has no free shell and its off-energy estimate suffices.

Use the symmetric split \(V=V_L+V_S\), with the compact smooth adjustment making \(P=P_0+V_L\) elliptic. Fix a sufficiently small \(0<\delta\le1\) for all its coefficient bounds, and write

\[
 a=\frac{1+\delta}{2},\qquad
 V_S:H^{m,t}\longrightarrow H^{0,t+1+\delta}.
 \tag{6}
\]

The primary map is consistent with the actual rough expression for every real \(t\). Its proof and the smooth split are given in the combined-resolvent lesson.

## 2. A strict step in the weight

Write \(U_\beta=\sum_{|\alpha|\le m}\|X^\beta D^\alpha u\|_{B^*}\). If \(U_{\gamma'}<\infty\), the shell square sum gives

\[
 \begin{gathered}
 u\in H^{m,t},\qquad t<\gamma'-\frac12,\\
 \|u\|_{m,t}\le C_{t,\gamma'}U_{\gamma'}.
 \end{gathered}
 \tag{7}
\]

Indeed on an outer shell each squared weighted derivative norm is at most
\(C R_j^{2(t-\gamma')+1}U_{\gamma'}^2\). Its exponent is strictly negative, so the geometric series converges. The inner shell is finite separately.

Choose

\[
 0\le\gamma'<\gamma<\gamma'+\frac{\delta}{2}.
 \tag{8}
\]

Then

\[
 \begin{gathered}
 u\in H^{m,\gamma-a}
       \cap H^{m,\gamma-1/2-\delta},\\
 \|u\|_{m,\gamma-a}
   +\|u\|_{m,\gamma-1/2-\delta}
 \le C U_{\gamma'}.
 \end{gathered}
 \tag{9}
\]

The first inclusion uses \(\gamma-a<\gamma'-1/2\); the second has still more margin.

Since \(B\subset H^{0,1/2}\), the weighted forcing is in \(H^{0,\gamma+1/2}\). The primary rough map puts \(V_Su\) in that space as well. Apply the complete real-parameter off-energy theorem to
\((P-\lambda)u=f-V_Su\), with any finite strict auxiliary weight from the preceding shell bound. Uniformly in the energy neighborhood,

\[
 \begin{gathered}
 u_{\mathrm{off}}=(1-\chi(D))u\in H^{m,\gamma+1/2},\\
 \sum_{|\alpha|\le m}
       \|X^\gamma D^\alpha u_{\mathrm{off}}\|_{B^*}\\
 \le C\bigl(\|X^\gamma f\|_B+U_{\gamma'}\bigr).
 \end{gathered}
 \tag{10}
\]

The last bound follows already from the weighted \(L^2\) derivatives. Thus the bootstrap step only needs to estimate \(\chi(D)u\).

## 3. Cutting off the full rough expression

**Lemma 3.1.** Let \(\zeta\) be smooth, equal one on the unit ball and supported in \(|x|<2\). Set \(\zeta_t(x)=\zeta(x/t)\), \(t\ge2\). Then

\[
 \begin{gathered}
 \|[H,\zeta_t]u\|_B\\
 \le C\left(t^{-1}
   \sum_{|\alpha|\le m}\int_{|x|<3t}|D^\alpha u|^2\,dx
          \right)^{1/2}
 \longrightarrow0.
 \end{gathered}
 \tag{11}
\]

Also \(D^\alpha(\zeta_tu)\to D^\alpha u\) in \(B^*\) through order \(m\). Whenever \(u\) is already known in \(H^{m,s}\), the same cutoffs converge there.

**Proof.** Write the complete expression, including the free coefficients, as \(\sum a_\alpha(x)D^\alpha\). Its highest coefficients are bounded, and each lower coefficient has a globally bounded translated unit-ball \(L^{p_\alpha}\) norm. Compact local membership and the admissible tail bounds give these global bounds. Local \(H^m\) membership of \(u\) follows from its derivative hypothesis. The actual local product rule is

\[
 [H,\zeta_t]u
 =\sum_\alpha\sum_{0<\beta\le\alpha}
   \binom{\alpha}{\beta}
   a_\alpha(D^\beta\zeta_t)D^{\alpha-\beta}u.
 \tag{12}
\]

Only the cutoff is differentiated. Its positive derivatives are \(O(t^{-1})\) or smaller and have support in \(t\le|x|\le2t\).

Choose a fixed translated cutoff \(\eta_y\), supported in \(B(y,1)\), equal one on \(B(y,1/2)\). An originally lower coefficient of derivative gap \(k=m-|\alpha|\) is multiplied by a derivative with gap \(k+|\beta|\ge k\). Its original Sobolev/Hölder exponents therefore still bound the local output by
\(Ct^{-1}A_\alpha(y)\|\eta_yu\|_{H^m}\). For an originally highest coefficient use its \(L^\infty\) norm. Integrate the squared inequalities over the contributing centers \(t-1/2\le|y|\le2t+1/2\). The derivative product rule and Fubini from the local multiplier proof give

\[
 \begin{gathered}
 \|[H,\zeta_t]u\|_2^2\\
 \le Ct^{-2}\sum_{|\alpha|\le m}
   \int_{t-3/2<|x|<2t+3/2}|D^\alpha u|^2\,dx.
 \end{gathered}
 \tag{13}
\]

The output annulus intersects a uniformly bounded number of dyadic shells. Its \(B\) norm is at most \(Ct^{1/2}\) times its \(L^2\) norm. Since \(2t+3/2\le3t\), this proves the bound; the ball-vanishing characterization makes it tend to zero.

In the derivative rule for \(\zeta_tu-u\), the undifferentiated cutoff term vanishes in \(B^*\) by the vanishing tail. Every other term is bounded by \(Ct^{-1}\) times a lower derivative endpoint norm. This proves endpoint convergence. For a known finite weighted Sobolev norm, the same finite rule, dominated convergence of its derivative square sums and the weighted norm equivalence prove convergence in \(H^{m,s}\). \(\square\)

In particular \(u_t=\zeta_tu\in H^m\) and

\[
 \begin{gathered}
 (H-\lambda)u_t=f_t,\\
 f_t=\zeta_t f+[H,\zeta_t]u\longrightarrow f
       \quad\hbox{in }B.
 \end{gathered}
 \tag{14}
\]

We will pass a fixed-radius estimate through this convergence. We do not need convergence of \(X^\gamma f_t\).

## 4. An exterior estimate with every nonnegative weight

Use the smooth exterior angular convolution \(\Psi\) from the radiation lesson. It is homogeneous of degree zero in its nonzero velocity argument, has all mixed \(G_1\) bounds, is zero for \(|x|<c\), and satisfies
\(y\cdot\partial_x\Psi\ge0\). That construction includes the half-line formula in dimension one.

Choose its nested excluded angular cutoff \(c_2\) with support in the acute cone \(x\cdot y>0\), and choose a radial smooth \(\omega=1\) on \(1\le|x|\le2\), supported in a fixed larger annulus. The positive probe constant \(k>0\) may be chosen for any positive minimum of \(|v|\) on \(\operatorname{supp}\chi\). Define

\[
 \begin{gathered}
 q_{R,\pm}=\Psi(x/R,\mp v(\xi))\chi(\xi),\\
 g_\pm=1-c_2(x,\pm v(\xi)),\\
 \Phi_{R,\pm}=k\omega(x/R)g_\pm(x,\xi)\chi(\xi).
 \end{gathered}
 \tag{15}
\]

Precisely, the sign \(\sigma=\pm1\) refers to \(P_\sigma=\sigma P\), free polynomial \(\sigma P_0\), energy \(\sigma\lambda\), and forcing \(\sigma(f-V_Su)\). Its free velocity is \(v_{P_\sigma}=\sigma v\). The escape argument is \(-v_{P_\sigma}\), so \(v_{P_\sigma}\cdot\partial_x\Psi(x/R,-v_{P_\sigma})=-R^{-1}\Psi'(x/R,-v_{P_\sigma})\le0\). This opposite direction is necessary for the following nonnegative transport symbol. For either sign let \(Q_R=\operatorname{Op}(q_R)\), \(\Phi_R\) its corresponding probe, and \(v_P=v_{P_\sigma}\). The construction gives

\[
 s_R=-q_R v_P\cdot\partial_xq_R-R^{-1}\Phi_R^2\ge0.
 \tag{16}
\]

Exterior support, with all differentiated bounds, implies for every fixed \(\gamma\ge0\)

\[
 \begin{gathered}
 R^\gamma q_R\in S(X^\gamma\Xi^{-N},G_1),\\
 R^{2\gamma}s_R\in S(X^{2\gamma-1},G_1),\\
 R^{\gamma-1/2}\Phi_R\in S(X^{\gamma-1/2}\Xi^{-N},G_1).
 \end{gathered}
 \tag{17}
\]

Each prescribed rapid frequency exponent \(N\) is allowed for the compact-frequency factors.

**Lemma 4.1.** Under the known finite norm in Section 2, for either sign,

\[
 \begin{gathered}
R^{-1}\|\operatorname{Op}(\Phi_R)u\|_2^2\\
 \le |(Q_R f,Q_Ru)|
       \\
+CR^{-2\gamma}\|u\|_{m,\gamma-a}^2,
 \\
 R\ge1.
 \end{gathered}
 \tag{18}
\]

**Proof.** First take a Schwartz input in the smooth equation. The exact weighted finite calculation is

\[
 \begin{gathered}
 R^{2\gamma}Q_R^*[P_\sigma,Q_R]/i\\
 =\operatorname{Op}(R^{2\gamma}s_R)\\
 \quad+R^{2\gamma-1}\operatorname{Op}(\Phi_R)^*
                         \operatorname{Op}(\Phi_R)+E_{R,\gamma}.
 \end{gathered}
 \tag{19}
\]

Here \(E_{R,\gamma}\) is uniformly in
\(S(X^{2\gamma-1-\delta}\Xi^{-N},G_\delta)\) for every prescribed \(N\). We justify the complete error. The free polynomial commutator is the exact finite Leibniz sum. Its terms with two or more position derivatives, and the first adjoint correction multiplied by the first transport term, have weight \(X^{2\gamma-2}\). A long-range product differentiating a coefficient uses its stronger bound \(X^{-1-\delta|\beta|}\); a product differentiating the escape factor uses \(X^{\gamma-|\beta|}\) beside the undifferentiated \(X^{-\delta}\) coefficient. After the other escape factor, both cases have weight at most \(X^{2\gamma-1-\delta}\).

Choose a finite composition order \(L\) with \(\delta L\ge1\). Its complete long-range remainder has weight at most \(X^{2\gamma-\delta-\delta L}\), hence the same required bound. Arbitrary rapid frequency seminorms of the escape factors handle the full differential order. The exact probe adjoint/product correction has weight \(X^{2\gamma-2}\), contained in the required error class since \(\delta\le1\). No convergent formal series is asserted.

The weighted map thus gives

\[
 \begin{gathered}
 E_{R,\gamma}:H^{0,\gamma-a}\longrightarrow H^{0,a-\gamma},\\
 |(E_{R,\gamma}u,u)|
       \le C\|u\|_{0,\gamma-a}^2.
 \end{gathered}
 \tag{20}
\]

For clarity, the positivity argument also applies when \(\gamma\) exceeds the small weight used for the graph limit. Put \(c_R=R^{2\gamma}s_R\), \(a_R=X^{-2\gamma}c_R\ge0\), and \(M_\gamma=X^\gamma\). By (17), \(a_R\) satisfies the full \(S(X^{-1},G_1)\) bounds of the [proved packet Theorem 1](../providers/analysis/weighted-positivity.md#weighted-positivity), uniformly in \(R\). One finite product gives

\[
 \begin{gathered}
 M_\gamma\operatorname{Op}(a_R)M_\gamma
 =\operatorname{Op}(c_R)+T_{R,\gamma},\\
 T_{R,\gamma}\in\operatorname{Op}S(X^{2\gamma-2},G_1).
 \end{gathered}
\]

The right multiplication has leading symbol \(a_RX^\gamma\) and remainder weight \(X^{\gamma-2}\Xi^{-1}\); the outer multiplication is exact. Consequently \(T_{R,\gamma}:H^{0,\gamma-1}\to H^{0,1-\gamma}\), with a uniform norm. On Schwartz inputs apply packet positivity to \(M_\gamma u\), use the real multiplication factor in the pairing, and subtract this bounded remainder form. This proves the same weighted reduction as [Section 6 of the radiation lesson](radiation-for-limits-of-long-range-resolvents.md#6-the-weighted-commutator-and-its-graph-limit):

\[
 \begin{gathered}
 \operatorname{Re}(\operatorname{Op}(R^{2\gamma}s_R)u,u)\\
 \ge-C\|u\|_{0,\gamma-1}^2
 \ge-C\|u\|_{0,\gamma-a}^2.
 \end{gathered}
 \tag{21}
\]

This uses \(a\le1\) and applies to every \(\gamma\ge0\). All constants use finitely many uniformly bounded seminorms. Large \(\gamma\) is handled first on Schwartz inputs, where every displayed factor acts. The compact-input approximation and fixed-radius inequality passage below then treat the actual solution; no unweighted boundedness of a positive-order spatial symbol is assumed. Exact Fourier conjugation gives the equivalent lower norm \(H^{\gamma-1}\), but no external sharp theorem is needed.

Symmetry in the smooth real-energy equation gives the commutator form as
\(-\operatorname{Im}(Q_R(f-V_Su),Q_Ru)\). The rough contribution obeys

\[
 \begin{gathered}
 \|Q_RV_Su\|_{0,\gamma+a}
       \le C\|u\|_{m,\gamma-a},\\
 \|R^{2\gamma}Q_Ru\|_{0,-\gamma-a}
       \le C\|u\|_{0,\gamma-a}.
 \end{gathered}
 \tag{22}
\]

The first line uses the primary rough map \(1+\delta=2a\); the second uses the exterior \(X^{2\gamma}\) symbol weight. Their weighted pairing bounds the rough term by
\(CR^{-2\gamma}\|u\|_{m,\gamma-a}^2\). Combining the identities proves the lemma on Schwartz inputs.

For each compact input \(u_t\) from Section 3, choose smooth approximants inside a fixed slightly larger compact support. Their \(H^m\) convergence also gives convergence in the known weighted norm, so the exact forms pass to \(u_t\). Smooth coefficients are bounded, \(Q_R\) preserves \(H^m\), and the rough map is consistent. Now hold \(R\) fixed and let \(t\to\infty\). The forcing converges in \(B\), the solution in \(B^*\), and the known \(H^{m,\gamma-a}\) norm converges. Shell maps pass the forcing pairing, and annular output support passes the probe in local \(L^2\). This proves the displayed inequality for the original solution. \(\square\)

## 5. Bounded weights with uniform operator constants

For \(\varepsilon>0\), define

\[
 W_\varepsilon(s)=s^\gamma(1+\varepsilon s)^{-\gamma},
 \qquad w_\varepsilon(x)=W_\varepsilon(X).
 \tag{23}
\]

These weights increase in \(s\), and \(W_\varepsilon(s)\le\varepsilon^{-\gamma}\) for fixed \(\varepsilon\). All normalized derivatives of the weight and its inverse are uniform in \(\varepsilon\):

\[
 \begin{gathered}
 |\partial_x^\alpha w_\varepsilon|
       \le C_\alpha X^{-|\alpha|}w_\varepsilon,\\
 |\partial_x^\alpha w_\varepsilon^{-1}|
       \le C_\alpha X^{-|\alpha|}w_\varepsilon^{-1}.
 \end{gathered}
 \tag{24}
\]

Logarithmic differentiation gives
\(W_\varepsilon'/W_\varepsilon=\gamma/[s(1+\varepsilon s)]\). Further derivatives use only factors \(\varepsilon s/(1+\varepsilon s)\le1\); the reciprocal has the opposite logarithmic derivative. The finite chain rule for \(X\) proves the displayed bounds.

Their weight constants are uniform too:

\[
 \frac{W_\varepsilon(s)}{W_\varepsilon(t)}
       \le\max(1,s/t)^\gamma,\qquad s,t>0.
 \tag{25}
\]

For \(s\ge t\) this follows from the exact quotient, and for \(s\le t\) from monotonicity. Reverse the variables for inverse weights. Japanese-bracket ratios have fixed polynomial bounds, giving uniform metric temperateness.

Let \(Q'_R\) have a slightly larger noncritical frequency cutoff equal one near \(\operatorname{supp}\chi\). Right frequency composition gives \(Q_R=Q'_R\chi(D)\) exactly. Exterior support implies \(W_\varepsilon(R)\le Cw_\varepsilon(x)\) there. Exact weighted products, including their complete remainders, give bounded families in \(\operatorname{Op}S(1,G_1)\):

\[
 \begin{gathered}
 W_\varepsilon(R)Q'_R M_{w_\varepsilon^{-1}},\\
 W_\varepsilon(R)Q_R M_{X^{-\gamma}}.
 \end{gathered}
 \tag{26}
\]

Indeed the first factor has symbol weight \(w_\varepsilon\), canceled by its reciprocal; the second has weight \(X^\gamma\), canceled by \(X^{-\gamma}\). The normalized seminorms and temperateness constants just proved control the finite product bounds uniformly in \(\varepsilon,R\). These are operator identities on the common actions, not pointwise symbol division.

Their weighted \(L^2\) bounds at exponents \(\pm1\) give uniform \(B\) and \(B^*\) bounds by the shell theorem. Put

\[
 \begin{gathered}
F_\gamma=\|X^\gamma f\|_B,\\
 N_\varepsilon=\|w_\varepsilon\chi(D)u\|_{B^*}<\infty.
 \end{gathered}
 \tag{27}
\]

Finiteness follows from \(w_\varepsilon\le\varepsilon^{-\gamma}\) and the unweighted shell map. We obtain

\[
 \begin{gathered}
 \|W_\varepsilon(R)Q_R f\|_B\le CF_\gamma,\\
 \|W_\varepsilon(R)Q_R u\|_{B^*}\le CN_\varepsilon.
 \end{gathered}
 \tag{28}
\]

Multiply Lemma 4.1 by \(W_\varepsilon(R)^2\). Since \(W_\varepsilon(R)\le R^\gamma\), for both signs,

\[
 \begin{gathered}
 R^{-1}\|W_\varepsilon(R)\operatorname{Op}(\Phi_{R,\pm})u\|_2^2\\
 \le CF_\gamma N_\varepsilon+C\|u\|_{m,\gamma-a}^2.
 \end{gathered}
 \tag{29}
\]

## 6. An exact frame for the radial annulus

The excluded acute cones for \(c_2(x,v)\) and \(c_2(x,-v)\) are disjoint. Thus at least one \(g_\pm\) equals one, and \(d=g_+^2+g_-^2\ge1\). Choose \(\omega_1=1\) near \(\operatorname{supp}\omega\), supported in a larger annulus, and a compact noncritical \(\chi_1=1\) near \(\operatorname{supp}\chi\). Put

\[
 \begin{gathered}
b_{R,\pm}=k^{-1}\omega_1(x/R)\chi_1(\xi)\frac{g_\pm}{d},
 \\
 B_{R,\pm}=\operatorname{Op}(b_{R,\pm}).
 \end{gathered}
 \tag{30}
\]

The reciprocal of \(d\) has every smooth bound. The spatial cutoff removes zero and the frequency cutoff allows smooth zero extension. The \(B_{R,\pm}\) are uniformly \(L^2\) bounded.

Their scalar leading products sum exactly to \(\omega(x/R)\chi(\xi)\). The complete finite product formula gives

\[
 \begin{gathered}
 \omega(x/R)\chi(D)
 =B_{R,+}\operatorname{Op}(\Phi_{R,+})\\
 \quad+B_{R,-}\operatorname{Op}(\Phi_{R,-})+T_R.
 \end{gathered}
 \tag{31}
\]

The full remainder is uniformly in
\(\operatorname{Op}S(X^{-1}\Xi^{-N},G_1)\) for every prescribed \(N\): each surviving product has a position derivative, and compact frequency support supplies arbitrary rapid frequency bounds.

Moreover \(T_R\) has output support in a fixed enlarged annulus. This follows from the exact left product kernels, whose output support lies in that of \(b_{R,\pm}\), and from the target multiplication operator. The exact left symbol and all its position derivatives vanish outside that annulus. Consequently

\[
 \begin{gathered}
 R^\gamma T_R\in\operatorname{Op}S(X^{\gamma-1}\Xi^{-N},G_1),\\
 \|R^\gamma T_Ru\|_{0,1-a}\le C\|u\|_{0,\gamma-a}.
 \end{gathered}
 \tag{32}
\]

On the output support \(X\asymp R\), so

\[
 \begin{gathered}
 R^{-1}\|W_\varepsilon(R)T_Ru\|_2^2\\
 \le CR^{2a-3}\|u\|_{0,\gamma-a}^2
 \le C\|u\|_{0,\gamma-a}^2.
 \end{gathered}
 \tag{33}
\]

Uniform \(L^2\) bounds for the two frame factors, the inequality for the norm of a finite sum, and Section 5 now imply

\[
 \begin{gathered}
 R^{-1}\|W_\varepsilon(R)\omega(x/R)\chi(D)u\|_2^2\\
 \le CF_\gamma N_\varepsilon+C\|u\|_{m,\gamma-a}^2.
 \end{gathered}
 \tag{34}
\]

This proves a radial operator estimate. The pointwise angular inequality alone would not be an \(L^2\) operator ordering.

## 7. Absorption, the inner shell and removal of the bounded weight

For \(R<|x|<2R\), \(R\ge1\), we have \(1\le X/R\le\sqrt5\). The weight quotient bound shows

\[
 W_\varepsilon(R)\le w_\varepsilon(x)
       \le5^{\gamma/2}W_\varepsilon(R).
 \tag{35}
\]

Because \(\omega=1\) on this annulus, Section 6 controls every outer squared dyadic endpoint term of \(w_\varepsilon\chi(D)u\). On \(A_0\), \(w_\varepsilon\le2^{\gamma/2}\), and its endpoint term is bounded by \(C\|\chi(D)u\|_{B^*}^2\le CU_0^2\). Therefore

\[
 N_\varepsilon^2
 \le CF_\gamma N_\varepsilon
       +C\|u\|_{m,\gamma-a}^2+CU_0^2.
 \tag{36}
\]

Since \(N_\varepsilon\) is finite for fixed \(\varepsilon\), Young's inequality absorbs half its square and gives a bound independent of \(\varepsilon\). On each fixed shell \(w_\varepsilon\) increases to \(X^\gamma\) as \(\varepsilon\downarrow0\). Monotone convergence first bounds that shell norm; taking the supremum then gives

\[
 \|X^\gamma\chi(D)u\|_{B^*}
 \le C\bigl(F_\gamma+\|u\|_{m,\gamma-a}+U_0\bigr).
 \tag{37}
\]

Choose compact noncritical \(\chi_2=1\) near \(\operatorname{supp}\chi\). Exact right frequency multiplication yields

\[
 \begin{gathered}
 X^\gamma D^\alpha\chi(D)u\\
 =\bigl(M_{X^\gamma}D^\alpha\chi_2(D)M_{X^{-\gamma}}\bigr)
             (X^\gamma\chi(D)u).
 \end{gathered}
 \tag{38}
\]

The conjugated operator is in \(\operatorname{Op}S(1,G_1)\), with its complete finite product remainder. Its shell map recovers every near-energy derivative through \(m\).

## 8. Finite bootstrap and homogeneous decay

Add the off-energy derivative bounds from Section 2 and use its strict shell estimate. One step gives

\[
 U_\gamma\le C_{\gamma,\gamma'}(F_\gamma+U_{\gamma'}),
 \qquad 0<\gamma-\gamma'<\delta/2.
 \tag{39}
\]

The case \(\gamma=0\) is already given. For any fixed target \(\gamma>0\), partition \([0,\gamma]\) into finitely many increments smaller than \(\delta/2\). Each lower forcing norm is at most the target \(F_\gamma\), since \(X\ge1\). Finite induction gives \(U_\gamma\le C(F_\gamma+U_0)\). A finite cover of \(K\) gives one uniform constant. This proves Theorem 1.1, including empty-shell neighborhoods. \(\square\)

**Corollary 8.1 (homogeneous polynomial decay).** If \(f=0\) in Theorem 1.1, then \(u\in H^{m,t}\) for every real \(t\). On every fixed compact regular-energy set, its weighted norm is bounded by a constant times \(U_0\).

**Proof.** The theorem gives every \(U_\gamma\). For a specified \(t\), choose \(\gamma>t+1/2\). The strict shell square sum in Section 2 puts every \(X^tD^\alpha u\) in \(L^2\). The integer weighted norm equivalence proves the assertion and its uniform bound. \(\square\)

This applies in particular to the zero-forcing outgoing graph pairs considered in the radiation and flux lessons: zero flux gives their vanishing derivative hypothesis before this theorem is used.

## 9. Consequences for the noncritical point spectrum

**Theorem 9.1.** The eigenvalues of \(H\) in the regular free-energy set have finite multiplicity and form a discrete subset of that set. Every corresponding eigenfunction lies in \(H^{m,t}\) for every real \(t\).

**Proof.** An \(L^2\) eigenfunction is in the domain \(H^m\). All its derivatives through \(m\) are therefore in \(L^2\subset\dot B^*\), so Corollary 8.1 gives every polynomial weight.

More quantitatively, suppose \(u_j\) are normalized orthogonal eigenfunctions with \(\lambda_j\) in one compact regular-energy set \(K\). The graph norm equivalence gives

\[
 \begin{gathered}
\|u_j\|_{H^m}
 \\
\le C(\|Hu_j\|_2+\|u_j\|_2)
 \\
\le C(1+\max_{\lambda\in K}|\lambda|).
 \end{gathered}
 \tag{40}
\]

Thus their unweighted endpoint derivative sums are uniformly bounded. The uniform homogeneous estimates and the strict shell sum give a common bound in \(H^{m,t}\) for each fixed \(t\).

For \(t>0\), the \(L^2\) tails obey

\[
 \|1_{\{|x|>R\}}u_j\|_2
       \le C R^{-t},\qquad R\ge1.
 \tag{41}
\]

On a fixed ball the bounded \(H^m\) family is precompact in \(L^2\), by the [complete finite-rank kernel argument in the radiation lesson, Lemma 3.1](radiation-for-limits-of-long-range-resolvents.md#3-strong-weighted-convergence-of-the-graph). Specifically, insert compact input and output cutoffs and a smooth Fourier cutoff at frequency \(N\). The high-frequency error is \(O(N^{-m})\) on this bounded \(H^m\) family. The low-frequency kernel between bounded supports is square integrable; approximation by finite sums of products, and Cauchy–Schwarz, approximate that operator in norm by finite-rank maps. Their finite-dimensional convergent subsequences and a diagonal extraction make the original local outputs Cauchy. This gives the asserted compactness using exactly the programme proof. Successive extraction on a countable increasing sequence of balls gives a subsequence converging on every fixed ball. To see global convergence, first make the two tails in (41) smaller than any prescribed error, then use local convergence on that fixed ball. Completeness of \(L^2\) supplies the global limit.

An infinite orthonormal sequence cannot have such a subsequence, since the distance between any two distinct terms is \(\sqrt2\). For eigenvectors \(u,v\) with distinct real eigenvalues \(\lambda,\mu\), symmetry gives \((\lambda-\mu)(u,v)=(Hu,v)-(u,Hv)=0\), so they are orthogonal. If an eigenspace were infinite dimensional, choose successively a vector outside the span of the previously chosen orthonormal vectors, subtract its finite orthogonal projection onto that span, and normalize the nonzero result. This constructs an infinite orthonormal family in that eigenspace. Either possibility contradicts the compactness just proved. Thus each compact regular-energy set contains only finitely many eigenvalues, counted with multiplicity, proving both conclusions. \(\square\)

### Use the conclusion

Check the bounded-weight constants and the exact annular frame, then count the finite steps needed for a prescribed weight. Use the homogeneous conclusion to establish discreteness only away from the stated thresholds.

## 10. Graded exercises with complete solutions

**Exercise 1 — Basic — the strict bootstrap increment.**

Let \(0<\delta\le1\), \(a=(1+\delta)/2\), and suppose \(X^{\gamma'}D^\alpha u\in B^*\) for every \(|\alpha|\le m\). Show that \(u\in H^{m,\gamma-a}\) if \(0\le\gamma'<\gamma<\gamma'+\delta/2\), with a bound by the preceding endpoint derivative norms. Explain why equality at the increment \(\delta/2\) does not follow from the endpoint hypothesis, even when the unweighted derivatives are in \(\dot B^*\).

**Solution 1.** Write \(t=\gamma-a\). On an outer dyadic shell of radius \(R_j\), the bracket \(X\) is comparable to \(R_j\); hence

\[
 \|X^t D^\alpha u\|_{L^2(A_j)}^2
 \le C R_j^{2(t-\gamma')+1}
          \|X^{\gamma'}D^\alpha u\|_{B^*}^2.
 \tag{42}
\]

The exponent is

\[
 2(t-\gamma')+1
 =2(\gamma-\gamma')-\delta<0.
 \tag{43}
\]

The sum over outer shells is geometric and finite. On \(A_0\) the weights are bounded, and the endpoint hypothesis gives the finite local contribution. Summing over the finite derivative family proves

\[
 \begin{gathered}
\sum_{|\alpha|\le m}\|X^t D^\alpha u\|_2
 \\
\le C_{\delta,\gamma-\gamma',m}
      \\
\sum_{|\alpha|\le m}\|X^{\gamma'}D^\alpha u\|_{B^*}.
 \end{gathered}
 \tag{44}
\]

The integer weighted derivative characterization from the weighted Sobolev lesson identifies the left side with a norm equivalent to \(\|u\|_{m,t}\).

For sharpness of this embedding alone, take the smooth radial function

\[
 g(x)=X^{-(n-1)/2-\gamma'}
          \bigl(\log(2+X)\bigr)^{-1/2}.
 \tag{45}
\]

Its weighted normalized shell masses are \(O(1/\log R_j)\), so \(X^{\gamma'}g\) is in \(\dot B^*\). Every positive derivative gains an extra inverse radius (up to smaller logarithmic factors), so \(X^{\gamma'}D^\alpha g\in\dot B^*\) through every fixed order. In particular the unweighted derivatives are in the closure. At the borderline increment \(\gamma-\gamma'=\delta/2\), however, \(t=\gamma'-1/2\), and for large radius the radial integral for \(\|X^t g\|_2^2\) is comparable to

\[
 \int_2^\infty \frac{dr}{r\log r}=\infty.
 \tag{46}
\]

Thus the strict increment is necessary for the embedding step used by the proof. This example imposes no equation or forcing condition and is not a counterexample to the weighted endpoint theorem.


**Exercise 2 — Intermediate — cutoffs with rough local multipliers.**

Let \(H=\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha\) have the complete \(1\)-admissible coefficient bounds. For smooth \(\zeta=1\) on the unit ball, supported in \(|x|<2\), set \(\zeta_t(x)=\zeta(x/t)\), \(t\ge2\). Prove the actual commutator estimate

\[
 \begin{gathered}
\|[H,\zeta_t]u\|_B
 \\
\le C\left(t^{-1}
       \sum_{|\alpha|\le m}\int_{|x|<3t}|D^\alpha u|^2\,dx
        \right)^{1/2}
 \end{gathered}
 \tag{47}
\]

for inputs with all derivatives through \(m\) in \(B^*\). Deduce convergence to zero for \(\dot B^*\) derivatives, and identify exactly which coefficient derivatives enter.

**Solution 2.** Local \(H^m\) membership follows from the derivative bounds. The local differential product rule gives

\[
 [H,\zeta_t]u
 =\sum_\alpha\sum_{0<\beta\le\alpha}
   \binom{\alpha}{\beta}
   a_\alpha(D^\beta\zeta_t)D^{\alpha-\beta}u.
 \tag{48}
\]

There are no derivatives of \(a_\alpha\). All these terms have output support in \(t\le|x|\le2t\), and \(\|D^\beta\zeta_t\|_\infty\le C_\beta t^{-|\beta|}\le C_\beta t^{-1}\).

Choose a translated cutoff \(\eta_y\), equal one on \(B(y,1/2)\), supported in \(B(y,1)\). For an originally lower coefficient \(a_\alpha\), put \(k=m-|\alpha|\) and use its assigned finite exponent \(p_\alpha\), with \(1/p_\alpha+1/q_\alpha=1/2\). On the half-ball, \(D^{\alpha-\beta}u=D^{\alpha-\beta}(\eta_yu)\). The derivative has available Sobolev gap \(k+|\beta|\ge k\), so the original \(H^k\to L^{q_\alpha}\) inequality remains valid there. Hölder bounds its output by \(C t^{-1}A_\alpha(y)\|\eta_yu\|_{H^m}\). For an originally highest coefficient use its bounded \(L^\infty\) norm and the local derivative \(L^2\) norm. All coefficient sizes \(A_\alpha(y)\) have a fixed global bound in the admissible class.

Only centers with \(t-1/2\le|y|\le2t+1/2\) contribute. Integrate these squared inequalities in \(y\). The fixed-cutoff derivative product rule and Fubini, exactly as in Proposition 2.1 of the admissible-perturbation lesson, give

\[
 \begin{gathered}
\|[H,\zeta_t]u\|_2^2
 \\
\le C t^{-2}\sum_{|\alpha|\le m}
       \int_{t-3/2<|x|<2t+3/2}|D^\alpha u|^2\,dx.
 \end{gathered}
 \tag{49}
\]

The output annulus intersects a uniformly bounded number of dyadic shells, each with endpoint weight \(O(t^{1/2})\); hence its \(B\) norm is at most \(C t^{1/2}\) times its \(L^2\) norm. Since \(2t+3/2\le3t\), the displayed commutator bound follows. The ball-vanishing characterization of \(\dot B^*\) makes its right side tend to zero when all the derivatives lie in that closure.

The finite rule for \(D^\alpha(\zeta_tu-u)\) also gives convergence in \(B^*\): the undifferentiated cutoff term vanishes by the endpoint tail, while each differentiated cutoff term is bounded by \(C t^{-1}\) times a lower derivative endpoint norm. If \((H-\lambda)u=f\in B\), the compact-input forcing is \(f_t=\zeta_t f+[H,\zeta_t]u\to f\) in \(B\). For each fixed escape radius, its forcing pairing therefore passes to the original input. No weighted convergence of \(X^\gamma f_t\) is required at this stage.


**Exercise 3 — Intermediate — bounded spatial weights without a growing constant.**

For \(\gamma\ge0\), \(\varepsilon>0\), define

\[
 W_\varepsilon(s)=\left(\frac{s}{1+\varepsilon s}\right)^\gamma,
 \qquad w_\varepsilon(x)=W_\varepsilon(X).
 \tag{50}
\]

Prove uniform normalized derivative and temperateness bounds for \(w_\varepsilon\) and its inverse. If an exterior symbol \(q_R'\) vanishes for \(|x|<cR\), has compact frequency support and uniform \(G_1\) bounds, prove

\[
 \begin{gathered}
W_\varepsilon(R)Q'_R M_{w_\varepsilon^{-1}}
 \\
\text{has a uniform order-zero}\\
\text{shell bound}.
 \end{gathered}
 \tag{51}
\]

Explain why \(N_\varepsilon=\|w_\varepsilon\chi(D)u\|_{B^*}\) is finite for fixed \(\varepsilon\).

**Solution 3.** The logarithmic derivative is

\[
 \frac{W_\varepsilon'(s)}{W_\varepsilon(s)}
 =\frac{\gamma}{s(1+\varepsilon s)}.
 \tag{52}
\]

Each further derivative is a finite sum of factors bounded by \(C_k s^{-k}\), since \(\varepsilon s/(1+\varepsilon s)\le1\). Inductively

\[
 |W_\varepsilon^{(k)}(s)|
 \le C_k s^{-k}W_\varepsilon(s).
 \tag{53}
\]

The same argument for the reciprocal, whose logarithmic derivative has the opposite sign, gives its corresponding bound. Composing with \(X=\langle x\rangle\) and applying the finite chain rule gives every \(G_1\) normalized position derivative, uniformly in \(\varepsilon\).

Monotonicity and the exact quotient yield

\[
 \frac{W_\varepsilon(s)}{W_\varepsilon(t)}
 \le\max(1,s/t)^\gamma.
 \tag{54}
\]

For \(s\ge t\), the extra quotient \((1+\varepsilon t)/(1+\varepsilon s)\) is at most1; for \(s\le t\), monotonicity suffices. Reverse \(s,t\) for the inverse weight. Japanese-bracket ratios have fixed polynomial bounds in the position difference, so the metric temperateness constants are independent of \(\varepsilon\).

On the exterior output support, \(W_\varepsilon(R)\le C_{\gamma,c}w_\varepsilon(x)\). Thus \(W_\varepsilon(R)q_R'\) is uniformly in \(S(w_\varepsilon\Xi^{-N},G_1)\) for every \(N\). Exact finite composition with multiplication by the inverse weight, including its complete remainder, lies uniformly in \(S(1,G_1)\). Its weighted \(L^2\) maps at exponents \(\pm1\) give the consistent shell bounds by Section 2 of the near-frequency lesson. This proves the operator assertion; a pointwise quotient of symbols alone would not prove it.

Finally \(w_\varepsilon\le\varepsilon^{-\gamma}\), and \(\chi(D)\) is bounded on \(B^*\). Hence \(N_\varepsilon\le\varepsilon^{-\gamma}C\|u\|_{B^*}<\infty\) for each fixed positive \(\varepsilon\). This bound may grow as \(\varepsilon\) decreases; the absorption argument supplies a new bound uniform in \(\varepsilon\).


**Exercise 4 — Advanced — a directional frame as an exact operator identity.**

On a fixed scaled annulus let \(g_\pm=1-c_2(x,\pm v(\xi))\), where the two excluded angular cones are disjoint and \(v\ne0\) on the compact frequency support. Let

\[
 \Phi_{R,\pm}=k\omega(x/R)g_\pm(x,\xi)\chi(\xi),
 \qquad k>0.
 \tag{55}
\]

Construct uniformly bounded \(B_{R,\pm}\) and prove

\[
 \begin{gathered}
\omega(x/R)\chi(D)
 \\
=B_{R,+}\operatorname{Op}(\Phi_{R,+})
  \\
+B_{R,-}\operatorname{Op}(\Phi_{R,-})+T_R,
 \end{gathered}
 \tag{56}
\]

where \(R^\gamma T_R\) has weight \(X^{\gamma-1}\) and rapid frequency decay, with annular output support. For \(a=(1+\delta)/2\le1\), bound its normalized weighted annular mass using only \(u\in H^{0,\gamma-a}\).

**Solution 4.** At each point at most one excluded cutoff is nonzero, so at least one \(g_\pm\) equals1. Therefore \(d=g_+^2+g_-^2\ge1\). Choose smooth \(\omega_1=1\) near \(\operatorname{supp}\omega\), supported in a larger fixed annulus, and compact noncritical \(\chi_1=1\) near \(\operatorname{supp}\chi\). Define

\[
 \begin{gathered}
b_{R,\pm}=k^{-1}\omega_1(x/R)\chi_1(\xi)\frac{g_\pm}{d},
 \\
 B_{R,\pm}=\operatorname{Op}(b_{R,\pm}).
 \end{gathered}
 \tag{57}
\]

The denominator has a smooth reciprocal with all normalized derivatives because \(d\ge1\). The spatial cutoff removes the origin, and the frequency cutoff permits smooth zero extension outside the noncritical neighborhood. All \(b_{R,\pm}\) are uniformly in \(S(1,G_1)\), so the operators are uniformly bounded on \(L^2\).

Their scalar leading products sum exactly to \(\omega(x/R)\chi(\xi)\). The complete finite product formula gives the displayed operator identity with \(T_R\in\operatorname{Op}S(X^{-1}\Xi^{-N},G_1)\) for every prescribed \(N\). Every subsequent finite product has a position derivative, and the finite remainder has the same allowed first position loss; both compact frequency factors supply arbitrary rapid frequency bounds. Each required seminorm uses a finite product order.

The exact product kernel has output support inside the output support of its left factor \(b_{R,\pm}\). The target multiplication operator has annular output support too. Thus the complete error has output support in one fixed enlarged annulus, and its exact left symbol and all position derivatives vanish outside that annulus. Consequently \(R^\gamma T_R\) has weight \(X^{\gamma-1}\), uniformly in \(R\).

The weighted map gives

\[
 \|R^\gamma T_Ru\|_{0,1-a}
 \le C\|u\|_{0,\gamma-a}.
 \tag{58}
\]

On its output annulus \(X\asymp R\), so

\[
 \begin{gathered}
R^{-1}\|W_\varepsilon(R)T_Ru\|_2^2
 \\
\le C R^{2a-3}\|u\|_{0,\gamma-a}^2
 \\
\le C\|u\|_{0,\gamma-a}^2.
 \end{gathered}
 \tag{59}
\]

Here \(W_\varepsilon(R)\le R^\gamma\) and \(a\le1\). The norm of the sum of the two \(B_{R,\pm}\) probe terms is bounded by a constant times the sum of their norms. This proves radial control from the two directional inequalities with a fully specified operator error. Pointwise positivity of the scalar symbols was used to construct an inverse frame, not asserted as an exact operator ordering.


**Exercise 5 — Advanced — a finite bootstrap and homogeneous decay.**

Assume the complete weighted proof adapters and let \(\delta=1/3\). Suppose all derivatives through \(m\) of a solution lie in \(\dot B^*\), the energy lies in a fixed compact regular-energy set, and \(X^{3/2}f\in B\). Use a concrete finite sequence of weights to prove the estimate at \(\gamma=3/2\) with only the unweighted endpoint derivative sum on its right side. Deduce every polynomial Sobolev weight for a homogeneous solution.

**Solution 5.** Here \(a=(1+\delta)/2=2/3\). Take twelve steps

\[
 \gamma_k=k/8,\qquad 0\le k\le12.
 \tag{60}
\]

Each increment \(1/8\) is strictly less than \(\delta/2=1/6\). Let \(U_k=\sum_{|\alpha|\le m}\|X^{\gamma_k}D^\alpha u\|_{B^*}\) and \(F=\|X^{3/2}f\|_B\). The base \(U_0\) is finite by hypothesis.

At step \(k\), the known preceding weight gives \(u\in H^{m,\gamma_k-a}\), because

\[
 \begin{gathered}
(\gamma_k-a)-(\gamma_{k-1}-1/2)
 \\
=1/8-1/6=-1/24.
 \end{gathered}
 \tag{61}
\]

The squared shell series in Solution1 has ratio \(2^{-1/12}\); hence its constant is fixed over these twelve steps. The lower input weight needed by the primary rough map for the off-energy forcing is \(\gamma_k-1/2-\delta=\gamma_k-5/6\), still strictly below \(\gamma_{k-1}-1/2=\gamma_k-5/8\). Thus \(V_Su\in H^{0,\gamma_k+1/2}\) with a bound by \(U_{k-1}\). Since \(X^{\gamma_k}f\in B\) and its norm is at most \(F\), the full real off-energy theorem bounds each off-energy weighted derivative by \(C_k(F+U_{k-1})\), uniformly in energy.

The two exact exterior estimates, their directional frame and the uniform bounded-weight maps give

\[
 N_{\varepsilon,k}^2
 \le C_k F N_{\varepsilon,k}
       +C_k U_{k-1}^2+C_k U_0^2,
 \tag{62}
\]

where \(N_{\varepsilon,k}=\|X^{\gamma_k}(1+\varepsilon X)^{-\gamma_k}\chi(D)u\|_{B^*}\) is finite. Young's inequality absorbs half its square. Letting \(\varepsilon\downarrow0\) on each shell gives

\[
 \|X^{\gamma_k}\chi(D)u\|_{B^*}
 \le C_k(F+U_{k-1}+U_0).
 \tag{63}
\]

The exact conjugated compact frequency derivative maps recover all near-energy derivatives. Add their off-energy bounds. Since \(U_{k-1}\ge U_0\) in these nonnegative weights, enlarge the constants to obtain

\[
 U_k\le C_k'(F+U_{k-1}).
 \tag{64}
\]

Finite induction yields \(U_{12}\le C(F+U_0)\). Twelve fixed steps and a finite energy cover give one constant depending on the operator, cutoff cover and target weight, independent of \(u,f,\lambda\).

For \(f=0\), use the same argument with as many fixed increments \(1/8\) as needed for any prescribed \(\gamma\) (choose a smaller final increment when necessary). All weighted endpoint derivatives follow. For any real Sobolev position weight \(t\), choose \(\gamma>t+1/2\). Then the strict endpoint shell sum gives \(X^tD^\alpha u\in L^2\) through \(m\), hence \(u\in H^{m,t}\). This is every polynomial position weight, with quantitative uniform bounds on each compact regular-energy set.

In particular an \(L^2\) eigenfunction has its derivatives in \(L^2\subset\dot B^*\) because the operator domain is \(H^m\); the homogeneous conclusion applies. This deduction does not by itself assert the full boundary-value theorem, its spectral measure formula or the eigenvalue graph decomposition.


## 11. Further questions

The remaining limiting-absorption argument uses these decay and compactness conclusions to remove the compact error from the resolvent estimate away from eigenvalues. It then proves both boundary values, their radiation characterization and continuity. The spectral measure identity and the graph decomposition at an eigenvalue require their additional precise statements.

## References

The [accessible scalar comparisons in the limiting-absorption lesson](limiting-absorption-for-long-range-differential-perturbations.md#accessible-scalar-comparisons-and-their-proof-limits) give Ito–Skibsted's quantitative radiation bounds for \(0<\beta<\min(2,1+\sigma+\rho)\), with \(V\in C^4\), \(q=0\), \(d\ge2\), and no positive eigenvalues. Those additional scalar estimates have a finite weight range. Sections 3–9 here prove the separate arbitrary-weight decay conclusion and regular-eigenvalue compactness for the full differential class.

[A] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), lectures of 17–21 July 1978, §3, Corollaries 3.G–3.H, Theorem 3.I and its point-spectrum corollary, gives the freely readable weighted-decay programme. Those arguments depend on Proposition 3.F, whose complete proof is omitted there. The present proof does not invoke it: Section 3 proves the rough cutoff passage; Section 4 proves the finite commutator at every required weight; Sections 5–7 prove uniform bounded-weight products, the exact two-direction frame and absorption; Sections 8–9 prove the finite bootstrap and compact-energy conclusion. The written programme calculus, packet positivity and local compactness proof supply the needed inputs.

[L] Nicolas Lerner, [*Metrics on the Phase Space and Non-Selfadjoint Pseudo-Differential Operators*, free author chapter on phase-space metrics](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Proposition 2.4.3, printed pp. 101–103, provides the positive-packet construction reconstructed in the programme's weighted-positivity proof. The broader general-metric Theorems 2.5.1 and 2.5.4, printed pp. 111–115, are comparisons. Section 4 uses the programme's packet theorem and finite product with spatial weights to prove (21) for every fixed nonnegative weight. Its full weight range does not depend on an externally cited sharp theorem.

[T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*, author's online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf), treats self-adjoint operators, resolvents and spectral measures.

