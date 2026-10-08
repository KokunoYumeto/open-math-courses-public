# Spectral transforms and completeness of modified waves

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: How can a modified wave operator be proved onto?** Time construction provides an isometry following a real long-range phase. A stationary transform supplies the additional bandwise observation needed to recover its preimage. The short-range comparison in the reconstruction part suggests the Hilbert-space argument, but the long-range proof must first establish flux normalization and stability under truncated coefficients.

A modified wave operator follows a long-range phase and sends a free state to an interacting state. Its construction preserves the norm. Completeness asks a further question: does every state orthogonal to the eigenvectors arise this way? We answer it by comparing waves with a stationary transform on one energy band at a time. A short Hilbert-space argument then turns an isometry into an explicit formula for the missing preimage.

Read [Admissible differential perturbations](admissible-differential-perturbations.md#admissible-coefficient-class) for the precise coefficient class and [Limiting absorption for long-range differential perturbations](limiting-absorption-for-long-range-differential-perturbations.md#lap-theorem) for real-energy resolvents. [Truncated operators and stable scattering amplitudes](truncated-operators-and-stable-scattering-amplitudes.md#truncation-amplitudes) proves the approximation of their local amplitudes. The normalized actions are constructed in [Escaping Lagrangians on regular energy surfaces](escaping-lagrangians-on-regular-energy-surfaces.md) and [Generating functions and the end of a localized force](generating-functions-and-the-end-of-a-localized-force.md#generator-free-end). For the time-dependent construction, use [Smooth long-range phases from Hamilton trajectories](smooth-long-range-phases-from-hamilton-trajectories.md#phase-global-extension) and [Modified waves and the direction of escape](modified-waves-and-the-direction-of-escape.md#modified-wave-existence).

The stationary prerequisites are [Global radiation and flux](global-radiation-and-flux.md#global-trace-extension) for the canonical free Fourier trace, [Distorted Fourier transforms and spectral density](distorted-fourier-transforms-and-spectral-density.md#distorted-poisson), Lemma 1.1 and Section 2, for continuous-test spectral inversion and measurable assembly, and [The full compact-force stationary comparison](truncated-operators-and-stable-scattering-amplitudes.md#compact-force-setting) for the actual truncated operators. That last proof includes changes to the highest coefficients. The earlier compact-graph short-range theorem alone would not cover them. The arbitrary-self-adjoint measure and exact domain are proved in [Self-adjoint spectral calculus with the original domain](../providers/analysis/self-adjoint-spectral-domains.md#self-adjoint-pvm-domain), through the complete bundled unitary and Cayley-transform proofs, with no lower-bound or separability assumption. [Wave operators and modified phases](wave-operators-and-modified-phases.md), Section 1, proves the group and generator criterion and then the scattering identities. The finiteness of polynomial critical values is proved in [Polynomial translations and regular energies](polynomial-translations-and-regular-energies.md#polynomial-critical-values). Fourier inversion and Plancherel are proved in [Fourier facts](../providers/analysis/finite-derivative-l2.md#fourier-normalization); coarea is proved in [Coordinate integration, CI7](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-integration); bounded Hilbert functionals are represented in [Elementary Hilbert tools](../providers/analysis/finite-trace-ideals.md#elementary-hilbert-tools). The outgoing and Cook integrals use [Hilbert-valued integration](../providers/analysis/hilbert-valued-integration.md), with its norm bounds and tail limits. Section 6 recovers the comparison multiplier by a strong-limit argument and also proves the scalar \(L^1\) representation for the alternative weak-star argument. The freely accessible references have distinct roles: Hörmander [H76] treats differential-polynomial phase construction and wave existence, while Yafaev [Y] gives a long-range Schrödinger comparison and the free author texts of Teschl [T] and Oh [O] supply spectral and analytic context. None replaces a programme proof of the complete differential-polynomial statement below.

<a id="spectral-completeness-setting"></a>

## 1. The complete range

Use \(D=-i\partial\), the unitary Fourier transform \(\mathcal F\), and an inner product linear in its first entry. Let \(P_0\) be a real elliptic scalar polynomial of order \(m\ge1\). Let \(V\) be a symmetric elliptic \(2\)-admissible differential perturbation, in the exact sense of the first prerequisite. In particular its highest coefficients are continuous, its local coefficient products have the sharp order-dependent integrability there, and its long coefficients admit the real smooth regularization used in the phase construction. The operators are

\[
 \begin{gathered}
 H_0=P_0(D),\qquad H=H_0+V,\\
 \mathcal D(H)=\mathcal D(H_0)=H^m.
 \end{gathered}
 \tag{1}
\]

These are self-adjoint realizations. Let \(W(\xi,t)\) be the real global phase constructed from the regularized real long part of \(V\). Its early-time extension is fixed once. On every compact set of regular frequencies, for sufficiently late times in either direction, it solves the Hamilton–Jacobi equation and has all the derivative bounds of the phase prerequisite. The wave existence theorem gives isometries

\[
 \mathcal W_\pm
 =\operatorname{s-lim}_{t\to\pm\infty}
        e^{itH}e^{-iW(D,t)}.
 \tag{2}
\]

Let \(\mathcal H_{\mathrm{pp}}\) be the closed span of **all** eigenvectors of \(H\), including any eigenvectors at critical energies.

The completeness, scattering and scalar-modifier conclusions are Hörmander [H4, Theorem 30.5.10]. We give the spectral assembly and multiplier arguments explicitly, retaining the full coefficient class.

**Theorem 1.1 (completeness).** The operator \(H\) has no singular continuous spectrum, and

\[
 \operatorname{ran}\mathcal W_+
   =\operatorname{ran}\mathcal W_-
   =\mathcal H_{\mathrm{pp}}^\perp
   =\mathcal H_{\mathrm{ac}}(H).
 \tag{3}
\]

The scattering operator \(\mathcal S=\mathcal W_+^*\mathcal W_-\) is unitary. It commutes with every bounded Borel function of \(H_0\), preserves \(\mathcal D(H_0)\), and commutes with \(H_0\) on that domain. The transforms

\[
 J_\pm^{\mathrm{wave}}=\mathcal F\mathcal W_\pm^*,
 \qquad
 \mathcal W_\pm=(J_\pm^{\mathrm{wave}})^*\mathcal F
 \tag{4}
\]

vanish on \(\mathcal H_{\mathrm{pp}}\) and are unitary from its orthogonal complement to momentum \(L^2(\mathbb R^n)\). On each regular energy band they agree, up to a measurable unit phase, with the stationary transform obtained from the local outgoing amplitudes.

We first isolate the norm argument. We then construct its stationary and time-dependent inputs, and finally pass from compact energy bands to the full space.

<a id="spectral-completeness-rigidity"></a>

## 2. A contraction becomes onto

This norm argument isolates the final bandwise step in Hörmander [H4, p. 329, following (30.5.42)′].

**Lemma 2.1.** Let \(J:\mathcal H\to L^2(X)\) satisfy \(J^*J=P\), where \(P\) is an orthogonal projection. Let \(M\) be scalar multiplication with \(|M|\le1\). Suppose an isometry \(U:L^2(X)\to\mathcal H\) satisfies \(U=J^*M\). Then \(|M|=1\) almost everywhere, \(U\) maps onto \(P\mathcal H\), and \(J\) is unitary from \(P\mathcal H\) to \(L^2(X)\). Here \(X\) is a sigma-finite measure space.

**Proof.** The identity for \(J^*J\) gives \(\|J\|\le1\), \(\|J^*\|\le1\), and \(J=JP\). For any \(q\in L^2(X)\),

\[
 \|q\|=\|Uq\|\le\|Mq\|\le\|q\|.
 \tag{5}
\]

Consequently the integral of \((1-|M|^2)|q|^2\) is zero. Test characteristic functions of finite-measure sets in a sigma-finite exhaustion. The nonnegative function \(1-|M|^2\) vanishes almost everywhere. For \(v=Pv\), the explicit choice \(q=\overline M Jv\) gives

\[
 Uq=J^*M\overline M Jv=J^*Jv=v.
 \tag{6}
\]

Also \(J^*=PJ^*\), so every image lies in \(P\mathcal H\). This proves the range assertion. Since multiplication by \(M\) is onto and \(U\) is an isometry, \(J^*\) is an isometry on all of \(L^2(X)\). Thus \(JJ^*=1\), completing the proof. ∎

This lemma explains the main task. We need a stationary map with the exact band norm, a strong limit of the waves, and a comparison multiplier bounded by one. A weak limit of phases can have smaller modulus; the isometry is what excludes that loss.

<a id="spectral-completeness-channels"></a>

## 3. Read a stationary transform from the outgoing channels

Let \(Z(P_0)\) be the critical values of \(P_0\), let \(\mathcal A\) be the eigenvalues of \(H\) outside that set, and write

\[
 \begin{gathered}
 \Omega=\mathbb R\setminus\bigl(Z(P_0)\cup\mathcal A\bigr),\\
 M_\lambda=\{\xi:P_0(\xi)=\lambda\}.
 \end{gathered}
 \tag{7}
\]

Fix a nondegenerate compact interval \(I\subset\Omega\). Neither endpoint is an eigenvalue. Ellipticity makes \(P_0^{-1}(I)\) compact. Cover this set by finitely many charts with a positive signed coordinate component of \(\nabla P_0\), and choose a smooth frequency partition \(\sum_\nu\chi_\nu=1\) on a neighborhood of the band. A negative coordinate direction is handled by reflecting the position and momentum coordinate together. This preserves the unitary Fourier convention.

Choose real \(\rho\in C_c^\infty\), equal to one on the unit ball, and set \(\rho_j(x)=\rho(x/j)\). The compact-force operators are

\[
 H_j=P_0(D)+V_j,\qquad V_j=\rho_jV\rho_j.
 \tag{8}
\]

The truncation theorem gives a common limiting-absorption bound on \(I\), excludes its eigenvalues for large \(j\), and proves the strong convergence of the normalized channel amplitudes, uniformly in \(\lambda\in I\). One Hamilton starting time can be used for this finite chart family and all sufficiently large \(j\).

Let \(J_j^{\mathrm{short}}\) be the canonical upper-sign transform for \(H_j\) constructed in Section 14 of the truncation lesson. Its shell value on a good energy is exactly \(T_\lambda(I-V_jR_{j,+}(\lambda))f\). That section proves its spectral norm, full-order coefficient products, actual boundary inverse and matching-sign wave comparison without assuming that \(V_j\) is a compact graph map. The normalized escaping sheet has a smooth real end action \(\psi_{\infty,j}(\xi)\) on the whole shell, smoothly in regular energy. Define the band function

\[
 F_jf(\xi)=e^{i\psi_{\infty,j}(\xi)}
                 J_j^{\mathrm{short}}f(\xi),
 \qquad P_0(\xi)\in I.
 \tag{9}
\]

It is globally defined before taking any limit. The action has one normalization; independent constants are not inserted in separate charts.

For clarity, the dense forcing space used here is the endpoint space \(B\). With \(S_0=\{|x|<1\}\), \(S_k=\{2^{k-1}\le|x|<2^k\}\) and \(r_k=2^k\),

\[
 \|f\|_B=\sum_{k\ge0}r_k^{1/2}\|f\|_{L^2(S_k)}.
 \tag{10}
\]

Its dual endpoint space has norm \(\sup_k r_k^{-1/2}\|u\|_{L^2(S_k)}\). The boundary solutions and their derivatives through order \(m\) lie in that dual space.

In a positive chart write \(x=(s,z)\), \(\xi=(\xi_1,\eta)\), and express the shell as \(\xi_1=E_\lambda(\eta)\). Set \(v_1=\partial_{\xi_1}P_0>0\) on its compact support. For \(f\in B\), put \(u_j=R_{j,+}(\lambda)f\). The local graph regularity and the actual sharp coefficient products make \(V_ju_j\) a compactly supported \(L^2\) function. Hence \(f_{0,j}=f-V_ju_j\in B\). Free radiation uniqueness and short-range factorization give

\[
 \begin{gathered}
 u_j=R_{0,+}(\lambda)f_{0,j},\\
 J_j^{\mathrm{short}}f=T_\lambda f_{0,j}
       \quad\hbox{on }M_\lambda.
 \end{gathered}
 \tag{11}
\]

Here \(T_\lambda\) is the canonical trace defined by completion from Schwartz forcing. It is not restriction of an arbitrary ambient \(L^2\) representative.

<a id="spectral-completeness-free-trace"></a>

Outside the finite force, the local phase has the exact value \(G_j(s,\eta)=sE_\lambda(\eta)-\psi_{\infty,j}(E_\lambda(\eta),\eta)\). For free forcing \(f_0\), the positive outgoing integral yields

\
 \begin{aligned}
 &\lim_{s\to\infty}\mathcal F_z
       \bigl(e^{-isE_\lambda(D_z)}
           [\chi(D)R_{0,+}(\lambda)f_0\bigr)\\
 &\quad=i\sqrt{2\pi}\,
       \frac{\chi(E_\lambda(\eta),\eta)}
            {v_1(E_\lambda(\eta),\eta)}
       T_\lambda f_0(E_\lambda(\eta),\eta).
 \end{aligned}
 \tag{12}
\]

For Schwartz forcing this follows directly from the scalar first-order outgoing integral: it is \(i\) times the full-line integral, and the quotient at the root is \(v_1\). The unitary time Fourier transform contributes \(\sqrt{2\pi}\). This also agrees with the residue \(2\pi i\) times the one-dimensional inverse Fourier factor. For general \(B\) forcing, approximate in \(B\) by Schwartz functions. The compact-frequency forcing map into \(L^1_sL^2_z\), the uniform outgoing evolution bound, and the canonical trace bound make both sides continuous in that norm. This proves (12) for the actual \(f_{0,j}\).

Let \(A_{\nu,j}(\lambda)\) be the outgoing amplitude in chart \(\nu\), corrected by its normalized \(G_j\). Combining (9), (11) and (12),

\[
 \mathcal F_z A_{\nu,j}(\eta)
    =i\sqrt{2\pi}\,
           \frac{\chi_\nu(\xi)F_jf(\xi)}{v_\nu(\xi)}.
 \tag{13}
\]

The signed distinguished velocity \(v_\nu\) is positive. If \(g=|\nabla P_0|\), the graph Jacobian is

\[
 \frac{dS}{g}=\frac{d\eta}{v_\nu}.
 \tag{14}
\]

Indeed the graph surface factor is \(g/v_\nu\). On the compact chart \(v_\nu\) is bounded above and below. Strong convergence of \(A_{\nu,j}\) therefore gives strong convergence of \(\chi_\nu F_jf\) in \(L^2(M_\lambda,dS/g)\), uniformly in energy. For two indices the finite partition gives

\[
 \begin{aligned}
 &\|F_jf-F_lf\|_{L^2(dS/g)}\\
 &\quad\le\sum_\nu\|\chi_\nu(F_jf-F_lf)\|_{L^2(dS/g)}.
 \end{aligned}
 \tag{15}
\]

Thus there is one strong shell limit \(F_If\). Its overlaps agree because the finite-\(j\) functions already agree. It is norm continuous under fixed local \(L^2(\eta)\) trivializations: the finite-\(j\) canonical trace and forcing depend continuously on energy, their phase is smooth, and the convergence is locally uniform. For the trace continuity just used, work in a fixed compact chart. At a chosen energy approximate the \(B\)-valued forcing by a single Schwartz function. Strong continuity of the forcing and the common canonical trace bound control the approximation uniformly at nearby energies. The trace of the fixed Schwartz function on the smoothly varying graph is continuous in \(L^2(d\eta)\) by dominated convergence on the compact coordinate support. Choosing the approximation first proves the asserted continuity for the original forcing. This uses the [trace extension](global-radiation-and-flux.md#global-trace-extension) and [measurable assembly](distorted-fourier-transforms-and-spectral-density.md#distorted-measurable-assembly) with their actual hypotheses.

All formulas apply to reflected negative coordinate directions. In dimension one the transverse space is \(\mathbb C\) and shell surface measure is counting measure.

<a id="spectral-completeness-assembly"></a>

The shell assembly, flux and band norm are Hörmander [H4, (30.5.38)–(30.5.40)]. The constants below use the unitary Fourier convention fixed in this lesson.

## 4. Flux gives the exact band norm

We must assemble the shell values measurably before using coarea. For fixed \(f\in B\), each \(F_jf\) has the canonical measurable representative of the short-range transform, multiplied by its smooth phase. Select a subsequence whose successive shell \(L^2\) differences have summable norms, uniformly in \(\lambda\in I\). On every fixed shell, Minkowski's inequality bounds the \(L^2\) norm of the sum of their absolute differences by this summable series. Monotone convergence shows that the pointwise series converges almost everywhere on that shell. Define \(F_If\) by this pointwise limit, and set it to zero where convergence fails. It is measurable and represents the strong limit on **each** shell. Coarea then identifies its ambient \(L^2\) class. This construction prevents ambient null-set choices from silently changing prescribed shell values.

<a id="spectral-completeness-flux"></a>

Symmetry gives a real value for \((u_j,V_ju_j)\). To justify this for a boundary solution, use the compact \(H^m\) function \(\rho_ju_j\). The expression equals its symmetric \(V\) quadratic form; local coefficient products and \(H^m\) approximation justify the identity. The exact free forcing-flux identity, together with (11), consequently gives

\[
 \frac1\pi\operatorname{Im}(R_{j,+}(\lambda)f,f)
       =\int_{M_\lambda}|F_jf|^2\,\frac{dS}{g}.
 \tag{16}
\]

The phase in (9) leaves the norm unchanged. The common limiting-absorption estimate bounds this expression by \(C_I\|f\|_B^2\). Pass the strong shell limit on the right and the weak-star resolvent pairing on the left. At every \(\lambda\in I\),

\[
 \begin{aligned}
 q_f(\lambda)&=\frac1\pi\operatorname{Im}(R_+(\lambda)f,f),\\
 q_f(\lambda)&=\int_{M_\lambda}|F_If|^2\,\frac{dS}{g}.
 \end{aligned}
 \tag{17}
\]

This nonnegative function is continuous by boundary-resolvent continuity. Let \(E_H\) be the self-adjoint spectral measure. Continuous-test spectral inversion from Lemma 1.1 of *Distorted Fourier transforms and spectral density* applies to the present \(H\). For continuous tests supported in the interior of \(I\), the nearby uniform limiting-absorption bound permits dominated convergence and gives \(d(E_H(\lambda)f,f)=q_f(\lambda)d\lambda\) there. Increasing continuous tests and the absence of endpoint atoms give

\[
 \begin{aligned}
 \|E_H(I)f\|^2
    &=\int_I q_f(\lambda)\,d\lambda\\
    &=\int_{P_0^{-1}(I)}|F_If(\xi)|^2\,d\xi.
 \end{aligned}
 \tag{18}
\]

The second equality is coarea. Define \(J_If=F_If\) on the band and zero elsewhere. Its shell construction is linear; coarea verifies linearity of its ambient class. Formula (18) makes it a contraction on dense \(B\subset L^2\), so it extends uniquely to all of \(L^2\). Set \(P_I=E_H(I)\) and let \(Q_I\) be multiplication by \(1_{P_0^{-1}(I)}\) in momentum space. Polarization and (18) give

\[
 J_I^*J_I=P_I,\qquad J_I=Q_IJ_I=J_IP_I.
 \tag{19}
\]

At this stage surjectivity is not assumed.

<a id="spectral-completeness-borel"></a>

We also need spectral intertwining. The same continuous-test identity, followed by polarization, gives \(J_I^*\chi(P_0)J_I=\chi(H)P_I\) for real continuous \(\chi\) on \(I\). Use it again for \(\chi^2\). Expanding the squared norm of \(\chi(P_0)J_If-J_I\chi(H)P_If\) makes the two squared terms and the cross term the same spectral integral. The result is zero. Here is the Borel extension explicitly. Continuous functions bounded by one approximate the indicator of an open interval relative to \(I\), and dominated convergence in both spectral measures passes the operator identity to that indicator. The class of sets whose indicators intertwine is closed under complements relative to \(I\), intersections by multiplying their identities, and countable disjoint unions by strong additivity. Disjointifying a general countable union therefore makes it a sigma algebra containing the relatively open intervals, hence all Borel sets of \(I\). Bounded simple approximations, followed by dominated convergence, give every bounded Borel function. Consequently

\[
 \chi(P_0)J_I=J_I\chi(H)P_I.
 \tag{20}
\]

This proof never assumes that a spectral projection preserves \(B\), or applies a canonical trace to such a projected forcing without justification.

## 5. Compare the waves with a common time construction

Write the regularized real-left splitting as \(V=L^{\mathrm r}+S^{\mathrm r}\). For the cutoffs, the long part is \(L_j^{\mathrm r}=\rho_j^2L^{\mathrm r}\); cutoff derivatives are placed in \(S_j^{\mathrm r}\). The truncation theorem proves one set of bounds for this whole family. In particular, for some \(0<\delta_0<1/3\), every long coefficient \(\ell_\alpha\) satisfies

\[
 \begin{gathered}
 |\partial^\beta\ell_\alpha(x)|\le C_{\alpha\beta}
                   \langle x\rangle^{-\mu_0(|\beta|)},\\
 \mu_0(k)=\delta_0+k\quad(0\le k\le2),\\
 \mu_0(k)=1+(1+\delta_0)k/2\quad(k\ge2).
 \end{gathered}
 \tag{21}
\]

The same constants, enlarged once, work for all \(j\). Their short coefficients have a common positive gap \(\kappa=\min(\delta_0,\epsilon_0)>0\): on each unit ball centered at \(y\), their \(L^2\) norm is at most \(C\langle y\rangle^{-1-\kappa}\). Here \(\epsilon_0\) is the positive short-range gap of the splitting. This follows from the local \(L^p\) bounds with \(p\ge2\); no derivative of a rough short coefficient is used.

<a id="spectral-completeness-common-phases"></a>

The finite-force comparison is Hörmander [H4, (30.5.41)–(30.5.44)]. The proof below supplies common choices for the phase construction and an explicit uniform Cook tail.

**Lemma 5.1 (common modifiers and wave convergence).** The global phases \(W_j,W\) can be constructed with one common choice of exhaustion, cutoffs and restart times. For any compact regular-frequency set \(K\) and finite \(S\),

\[
 \begin{gathered}
 W_j(\xi,t)=W(\xi,t),\\
 \xi\in K,\quad |t|\le S,\quad j\ge j(K,S).
 \end{gathered}
 \tag{22}
\]

For either sign, the corresponding modified waves converge strongly:

\[
 \mathcal W_{j,\pm}u\longrightarrow\mathcal W_\pm u.
 \tag{23}
\]

**Proof.** Use the [restart construction](smooth-long-range-phases-from-hamilton-trajectories.md#phase-restarted-graph), [exact overlap agreement](smooth-long-range-phases-from-hamilton-trajectories.md#phase-exact-gluing) and [locally finite global extension](smooth-long-range-phases-from-hamilton-trajectories.md#phase-global-extension). Choose the frequency exhaustion, spatial and velocity buffers, and all smooth cutoffs once for the family. At each finite restart step the contraction threshold and inverse-action derivative bounds depend on common coefficient bounds and the finitely many preceding data bounds. These are uniform by induction. Choose the restart time uniformly and also larger than its index. This yields common late-time thresholds and common phase derivative bounds on each compact regular-frequency set.

For fixed \(K,S\), only finitely many factors of the smooth extension are active. Every action in this finite prefix uses finitely many trajectories and preceding initial action values, with times bounded by the relevant fixed restart times. The compact enlarged frequency sets and common trajectory bounds put all those finite paths in one position ball. Once \(j\) exceeds its radius, the long coefficients and all their jets agree with the untruncated coefficients there. Induct through the restarts: the free initial actions agree; their cutoff initial values agree; uniqueness gives identical trajectories, inverses and integrated actions. Exact overlap agreement and the common final extension give (22), including its additive phase constants and early-time values. No one radius for the infinite exhaustion is asserted.

<a id="spectral-completeness-wave-limit"></a>

Let \(\widehat u\in C_c^\infty(K)\). The short coefficients' cone envelope is at most \(Cr^{-1-\kappa}\) in every cone. The [concentration estimate](modified-waves-and-the-direction-of-escape.md#modified-wave-concentration) uses finitely many common phase jets. Its estimates away from the escape cone use a common weighted square-integrability bound on the rough coefficients. The [rough coefficient bound](modified-waves-and-the-direction-of-escape.md#modified-wave-rough-coefficients) and [finite-derivative bound for the long residual](modified-waves-and-the-direction-of-escape.md#modified-wave-finite-derivative-budget) also use common seminorms. The actual packet residual therefore satisfies, on a sufficiently late half-line,

\[
 \begin{aligned}
 &\|(H_j-W_{j,t}(D,t))e^{-iW_j(D,t)}u\|_2\\
 &\qquad\le C_u\bigl(|t|^{-1-\kappa}
                 +|t|^{-1-\delta}+|t|^{-2}\bigr),
 \end{aligned}
 \tag{24}
\]

where \(\delta>0\) is a fixed smaller phase exponent. All constants and the starting threshold are independent of \(j\). The domain and graph-continuity product rule is the one proved in that prerequisite. Cook integration gives a common tail \(C_u(R^{-\kappa}+R^{-\delta}+R^{-1})\).

Split the difference of the limiting waves into these two tails and the comparison at the fixed time \(\sigma R\). Choose \(R\) large first. Formula (22) makes the Fourier modifiers equal on the packet for large \(j\), and the [strong finite-time group convergence](truncated-operators-and-stable-scattering-amplitudes.md#truncation-groups) compares \(e^{i\sigma RH_j}\) with \(e^{i\sigma RH}\). Then choose \(j\) large. This proves (23) on dense packets; isometry extends it to all \(L^2\). The same cone bounds hold for both signed directions. ∎

<a id="spectral-completeness-compact-end"></a>

For fixed \(j\), the long force vanishes outside a bounded ball. Its phase position obeys \(\partial_\xi W_j=t\nabla P_0+O(|t|^{1-\delta})\), and therefore eventually leaves this ball on each compact regular-frequency set. The Hamilton–Jacobi equation then becomes \(W_{j,t}=P_0\) exactly. At positive time there is a smooth real function \(\phi_j\) such that

\[
 W_j(\xi,t)=tP_0(\xi)+\phi_j(\xi).
 \tag{25}
\]

Its local values agree on overlaps because \(W_j\) is global. Thus

\[
 \mathcal W_{j,+}
   =\mathcal W_{j,+}^{\mathrm{short}}
                   e^{-i\phi_j(D)}.
 \tag{26}
\]

## 6. Find the band preimage

The full compact-force comparison in Section 14 of the truncation lesson proves \(\mathcal W_{j,+}^{\mathrm{short}}=(J_j^{\mathrm{short}})^*\mathcal F\) for these actual operators, including their highest-order perturbations. Let \(\widehat u\) be a smooth packet supported in the interior of the free band, and let \(v\in B\). Formulas (9) and (26), with the linear-first inner product, yield

\[
 \begin{aligned}
 (\mathcal W_{j,+}u,v)
     &=(M_j\mathcal Fu,J_I^{(j)}v),\\
 M_j&=e^{i(\psi_{\infty,j}-\phi_j)}.
 \end{aligned}
 \tag{27}
\]

Here \(J_I^{(j)}v=F_jv\) on the band and is zero off it. To check the sign, \(J_j^{\mathrm{short}}v=e^{-i\psi_{\infty,j}}F_jv\); moving that factor from the second entry to the first changes \(e^{-i\phi_j}\) into \(e^{i(\psi_{\infty,j}-\phi_j)}\).

<a id="spectral-completeness-strong-multiplier"></a>

There is a direct strong-limit construction of the multiplier. Work on the free band space \(K=Q_IL^2(d\xi)\), and write \(U_jq=\mathcal W_{j,+}\mathcal F^{-1}q\), \(Uq=\mathcal W_+\mathcal F^{-1}q\). The matching identity \(J_j^{\mathrm{short}}\mathcal W_{j,+}^{\mathrm{short}}=\mathcal F\) is proved in Section 14 of the truncation lesson for the full compact-force class. Its [damped-integral comparison](truncated-operators-and-stable-scattering-amplitudes.md#compact-force-comparison) uses the [bounded inverse obtained from full radiation uniqueness](truncated-operators-and-stable-scattering-amplitudes.md#compact-force-factorization), retaining every highest-order coefficient product. Together with (9), (26), and the free-band spectral intertwining, this gives

\[
 J_I^{(j)}U_jq=M_jq,\qquad q\in K.
\]

Each \(J_I^{(j)}\) is a contraction: its band norm is \(\|E_{H_j}(I)v\|\). The [uniform amplitude convergence](truncated-operators-and-stable-scattering-amplitudes.md#truncation-amplitudes), the shell conversion (13)–(14) and coarea first give \(J_I^{(j)}v\to J_Iv\) for \(v\in B\). Density and the common contraction bound extend this strong convergence to every fixed \(v\in L^2\). In particular, for each \(q\in K\),

\[
 \begin{aligned}
 \|M_jq-J_IUq\|
 &\le\|J_I^{(j)}(U_jq-Uq)\|
       +\|(J_I^{(j)}-J_I)Uq\|\longrightarrow0.
 \end{aligned}
\]

This uses the stationary convergence on the fixed vector \(Uq\); it does not assume that \(Uq\in B\). Thus the unit-modulus scalar multiplication operators \(M_j\) have a strong limit \(T=J_IU\) on \(K\). To identify it, the band \(K_I=P_0^{-1}(I)\) has finite measure. Put \(M=T1_{K_I}\). Choose a subsequence with \(\|M_{j_k}1_{K_I}-M\|_2\le2^{-k}\). Tonelli gives
\[
 \int_{K_I}\sum_k|M_{j_k}-M|^2
       =\sum_k\|M_{j_k}1_{K_I}-M\|_2^2<\infty.
\]
Thus the squared-error sum is finite almost everywhere, its summands tend to zero, and the unit moduli give \(|M|=1\) almost everywhere on the band. This also proves the precise strong-\(L^2\)-to-pointwise-subsequence fact used below. All \(M_j\) commute with multiplication by measurable indicators, and strong limits preserve that commutation. Hence \(T1_A=1_AM\) for every measurable \(A\subset K_I\). Finite simple functions and \(L^2\) approximation give \(Tq=Mq\) for all \(q\in K\). This identifies the whole sequence's strong limit; the almost-everywhere subsequence was used only to identify its modulus.

Pass (27) using this strong multiplier convergence, strong wave convergence, and strong convergence of \(J_I^{(j)}v\). Cauchy–Schwarz controls both pairing errors, first for \(v\in B\) and then by density for every \(v\). This already proves (28), with a unit multiplier. Smooth packets supported in the interior of the free band are dense in \(K\): each endpoint shell is a null set by its regular-energy coordinates. Thus no endpoint component is lost when extending the pairing identity.

<a id="spectral-completeness-weak-multiplier"></a>

The weak multiplier passage is the method in Hörmander [H4, p. 329, (30.5.42)′–(30.5.42)″].

For completeness, the following alternative scalar compactness argument obtains a contractive multiplier before norm rigidity identifies its modulus. It is useful when only the pairing identity (27), rather than the direct finite-force composition identity, is available. The restrictions to \(K_I\) of finite simple functions on rational coordinate boxes, with rational complex coefficients, form a countable dense family in \(L^1(K_I)\): truncate an integrable function in value, approximate it by a simple function, and approximate its finite-measure level sets by finite unions of boxes. The complete finite-measure box approximation and Euclidean product proof is in [Euclidean measure and products](../providers/analysis/finite-derivative-l2.md#euclidean-products). Approximating the finitely many bounded box endpoints by rational endpoints makes their total symmetric-difference volume arbitrarily small; rational complex coefficients then give the stated countable density. The selected scalar simple-density, subsequence and completeness proofs are also freely available in [Hunter, Measure Theory, Sections 7.3–7.4](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf#page=85), Theorem 7.8, Lemma 7.9, Theorem 7.10 and Corollary 7.11.

Since \(|M_j|=1\), each scalar sequence \(\int_{K_I}M_jh\) is bounded by \(\|h\|_1\). Successive subsequences for the countable dense tests and their diagonal subsequence make all those pairings converge. Approximation gives convergence for every \(h\in L^1(K_I)\): the two pairing errors are each at most the \(L^1\) approximation error. The resulting complex-linear functional \(L\) satisfies \(|L(h)|\leq\|h\|_1\).

On this finite-measure band, \(\|h\|_1\leq|K_I|^{1/2}\|h\|_2\). The complete local projection and representation proof in [Elementary Hilbert tools](../providers/analysis/finite-trace-ideals.md#elementary-hilbert-tools) therefore gives a \(g\in L^2(K_I)\) with \(L(h)=\int h\overline g\) for \(h\in L^2(K_I)\). Set \(M=\overline g\). For any \(\varepsilon>0\), on \(A_\varepsilon=\{|M|>1+\varepsilon\}\) take \(h=1_{A_\varepsilon}\overline M/|M|\), setting it to zero off that set. This bounded test is in \(L^2(K_I)\), and

\[
 (1+\varepsilon)|A_\varepsilon|
 \leq\int_{A_\varepsilon}|M|
 =|L(h)|\leq\|h\|_1=|A_\varepsilon|.
\]

Hence \(A_\varepsilon\) is null. A countable sequence of \(\varepsilon\)'s gives \(|M|\leq1\) almost everywhere. Truncation of an arbitrary \(L^1\) function gives bounded \(L^2\) approximants in \(L^1\), so \(L(h)=\int Mh\) for all \(L^1\) tests. If the band has measure zero, use \(M=0\); its test space is zero. We have thus proved the required weak-star subsequential convergence and its exact unit-ball bound, without a separate \(L^1\)-duality or compactness theorem.

For fixed \(v\in B\), uniform shell convergence and coarea give \(J_I^{(j)}v\to J_Iv\) strongly in momentum \(L^2\). The pairing error from this difference is at most \(\|u\|\|J_I^{(j)}v-J_Iv\|\). The remaining fixed product \(\mathcal Fu\,\overline{J_Iv}\) belongs to \(L^1\), so weak-star convergence applies to it. Strong wave convergence passes the left side. Density in \(v\) and in free band packets gives

\[
 \mathcal W_+u=J_I^*M\mathcal Fu,
 \qquad Q_I\mathcal Fu=\mathcal Fu.
 \tag{28}
\]

The alternative passage needs no pointwise or strong convergence of \(M_j\). Apply Lemma 2.1 with free band space \(Q_IL^2\). Wave isometry and (19) imply

\[
 |M|=1\quad\hbox{almost everywhere on the band}.
 \tag{29}
\]

Both constructions give the same multiplier: Lemma 2.1 makes \(J_I^*\) injective on the band space, so (28) identifies their action on every band vector. In particular the direct argument proves strong convergence of the whole sequence \(M_j\), while the alternative scalar extraction suffices for completeness without that stronger conclusion.

<a id="spectral-completeness-band-preimage"></a>

For any \(v=P_Iv\), its concrete free preimage is

\[
 u=\mathcal F^{-1}\overline M J_Iv,
 \qquad \mathcal W_+u=v.
 \tag{30}
\]

Conversely spectral intertwining of the waves puts every free band image in \(P_IL^2\). Thus the band range is exactly \(P_IL^2\), and \(J_IJ_I^*=Q_I\). The wave-compatible stationary expression is

\[
 \mathcal F\mathcal W_+^*v=\overline M J_Iv,
 \qquad v\in P_IL^2.
 \tag{31}
\]

The Hamilton starting time and action normalization may depend on \(I\). They can change \(J_I\) and \(M\), but their product in (31) is fixed by the chosen global wave. This is sufficient for agreement between bands; a single Hamilton starting time over all energies is unnecessary.

<a id="spectral-completeness-spectral-parts"></a>

## 7. Good energies account for the whole continuous space

On every compact interval in \(\Omega\), the locally uniform \(B\)-to-\(B^*\) resolvent bound already gives absolutely continuous spectral measure for the dense \(B\) vectors. Weighted duality bounds the positive imaginary pairing by \(C_I\|f\|_B^2\); the Stone-formula proof of Theorem 5.1 in [Resolvents, domains and spectral density](resolvents-domains-and-spectral-density.md), with the general spectral measure used here, gives interval and Borel-set domination by \(C_I\|f\|_B^2/\pi\). For a null Borel subset of \(\Omega\), a countable compact-interval exhaustion shows that its spectral projection annihilates every such vector. Boundedness and density make the projection zero on all \(L^2\). Boundary convergence and the flux identity remain necessary for the continuous shell-density formula (17) and the band norm calculation; the bound alone does not supply those formulas.

The limiting-absorption prerequisite shows that \(\Sigma=Z(P_0)\cup\mathcal A\) is closed and countable; polynomial critical values form a finite set. The self-adjoint spectral theorem identifies the singleton projections exactly:

\[
 E_H(\{\lambda\})L^2=\ker(H-\lambda).
 \tag{32}
\]

Indeed a vector with measure supported on \(\{\lambda\}\) has finite second spectral moment, belongs to \(\mathcal D(H)\), and satisfies \(Hv=\lambda v\). Conversely the integral of \(|t-\lambda|^2\) against the spectral measure of an eigenvector is zero, so that measure is supported on the singleton. Countable strong additivity now gives

\[
 E_H(\Sigma)L^2=\mathcal H_{\mathrm{pp}},
 \qquad E_H(\Omega)L^2=\mathcal H_{\mathrm{pp}}^\perp.
 \tag{33}
\]

A noneigenvalue singleton contributes zero, even at a critical value. Eigenvectors at critical values are included without a multiplicity or spatial-decay assumption. Since the spectrum on \(\Omega\) is absolutely continuous and the remaining measure is countably atomic, there is no singular continuous part.

The free polynomial has wholly absolutely continuous spectrum. Its critical set is null: it is contained in the zero set of a nonzero polynomial partial derivative. Near every other frequency, a nonzero partial derivative gives local energy coordinates. The inverse image of a scalar null set is null there by Fubini and change of variables. A countable chart cover proves the assertion on all momentum space. The wave spectral intertwining therefore places the range in \(E_H(\Omega)L^2\).

<a id="spectral-completeness-full-range"></a>

Take increasing finite unions of compact good intervals exhausting \(\Omega\). Explicitly, enumerate all closed intervals with rational endpoints contained in \(\Omega\), and take the union of the first \(N\). Every point of the open set lies inside one such interval. Merging overlapping intervals expresses each finite union as finitely many disjoint compact good intervals, so the band argument applies to each component. Formula (30) puts every vector in the corresponding \(H\) spectral subspace in the wave range. These subspaces have dense union in \(E_H(\Omega)L^2\). The range is closed because the wave is an isometry. This proves positive-time completeness. If a good interval has an empty free band, its shell norm in (17) is zero and inversion gives \(P_I=0\); there is no omitted channel.

For negative time use the [exact time-reversal construction](smooth-long-range-phases-from-hamilton-trajectories.md#phase-time-reversal) for \(-H\) and \(-P_0\), with \(\widetilde W(\xi,s)=W(\xi,-s)\). This is the future construction used to define the negative-time part of the chosen global phase. Its positive-time wave is the original negative-time wave. The boundary solutions correspond through

\[
 R_+^{-H}(-\lambda)=-R_-^H(\lambda).
 \tag{34}
\]

The forcing changes to \(-f\); any scalar sign in its stationary normalization is a unit phase. The range conclusion has no such ambiguity. This proves (3) for both signs.

<a id="spectral-completeness-scattering"></a>

Write \(P_{\mathrm{ac}}=E_H(\Omega)\). Completeness gives \(\mathcal W_\pm\mathcal W_\pm^*=P_{\mathrm{ac}}\) and \(\mathcal W_\pm^*\mathcal W_\pm=1\). Hence

\[
 \mathcal S^*\mathcal S
   =\mathcal W_-^*P_{\mathrm{ac}}\mathcal W_-=1,
 \qquad \mathcal S\mathcal S^*=1.
 \tag{35}
\]

Wave group intertwining implies that \(\mathcal S\) commutes with the free group. Its strong difference quotients then show preservation of \(\mathcal D(H_0)\) and commutation with \(H_0\) there. Spectral intertwining also gives commutation with every bounded Borel energy multiplier. Finally (4) follows by taking adjoints and using Plancherel. These transforms vanish on eigenvectors and are onto the full momentum space. Formula (31) identifies their band restrictions with the local-amplitude construction. Theorem 1.1 is proved. ∎

<a id="spectral-completeness-scalar-gauge"></a>

## 8. Changing a scalar modifier changes a unit phase

This scalar-modifier conclusion is also part of Hörmander [H4, Theorem 30.5.10]. Here its scalar nature follows from the exact comparison of the two Fourier multipliers.

**Theorem 8.1.** Suppose another real scalar phase \(W'(\xi,t)\) satisfies the phase, velocity and short-range cone hypotheses of *Modified waves and the direction of escape*, for this \(H\) and one time sign. Let its modified wave be \(\mathcal W'\). Then there is a measurable \(N(\xi)\), with \(|N|=1\) almost everywhere, such that

\[
 \mathcal W'=\mathcal W N(D),
 \tag{36}
\]

where \(\mathcal W\) is the complete wave of that sign. In particular \(\mathcal W'\) is complete.

**Proof.** Set \(A_t=e^{itH}e^{-iW(D,t)}\), and define \(A'_t\) with \(W'\). The wave existence and intertwining theorem puts the range of \(\mathcal W'\) in \(\mathcal H_{\mathrm{ac}}(H)=\operatorname{ran}\mathcal W\). For \(y=\mathcal Wh\), unitarity gives

\[
 \|A_t^*y-h\|=\|y-A_th\|\longrightarrow0.
 \tag{37}
\]

Combine this convergence on the range with \(A'_tu\to\mathcal W'u\). The comparison thus converges strongly on every vector:

\[
 \begin{aligned}
 A_t^*A'_t&\longrightarrow\mathcal W^*\mathcal W',\\
 A_t^*A'_t&=\mathcal F^{-1}e^{i(W-W')}\mathcal F.
 \end{aligned}
 \tag{38}
\]

To identify this limit in momentum space, take increasing bounded boxes \(B_k\) covering \(\mathbb R^n\). Apply the strong limit to \(1_{B_k}\), defining an \(L^2(B_k)\) function \(N_k\). Every approximating multiplier commutes with frequency indicators; the limit does too. Therefore \(N_l=N_k\) on \(B_k\subset B_l\). On each box, the summable-squared-error argument proved in Section 6 gives an almost-everywhere convergent subsequence along times tending to the selected infinity. It preserves the modulus one of the approximating phases. The countable union of the exceptional null sets is null, so the compatible functions define one measurable \(N\) with \(|N|=1\). Indicator tests inside each box give multiplication by \(N\); simple-function approximation and the uniform operator bound extend this to all \(L^2\).

Consequently \(\mathcal W^*\mathcal W'=N(D)\). Since the range of \(\mathcal W'\) lies in the range of \(\mathcal W\), multiplication on the left by \(\mathcal W\) proves (36). The multiplier is unitary and onto, so the two wave ranges coincide. ∎

This conclusion uses the exact scalar frequency multiplication in (38). Commutation with energy alone would permit mixing different frequencies of the same energy.

### Use the conclusion

Construct a preimage on one good energy band, then account for all continuous states using the stated exceptional-energy set. Changing a scalar modifier changes a unit phase; it must not change the completeness claim.

<a id="spectral-completeness-solutions"></a>

## 9. Exercises with complete solutions

**Exercise 1 — Basic: the two free channels.** On the line take \(H_0=D^2\), \(\lambda=k^2>0\), and Schwartz forcing \(f\). Compute both outgoing amplitudes of \(R_{0,+}(\lambda)f\) with the unitary Fourier convention. Express the spectral density in terms of those amplitudes and explain the negative spatial direction.

**Solution 1.** The upper-boundary Green function is

\[
 K_\lambda(x)=\frac{i}{2k}e^{ik|x|},\qquad
 (-\partial_x^2-k^2)K_\lambda=\delta_0.
 \tag{39}
\]

The derivative jump is \(K'(0+)-K'(0-)=-1\), which gives the delta after applying the negative second derivative. To select the boundary sign, take \(z=k^2+i\varepsilon\) and its square root \(\kappa\) with positive imaginary part. The integrable decaying kernel \(i e^{i\kappa|x|}/(2\kappa)\) has the same derivative jump and solves \((-\partial_x^2-z)K_z=\delta_0\). Fourier transformation therefore gives its convolution multiplier \((\xi^2-z)^{-1}\), since this denominator has no real zeros. As \(\varepsilon\downarrow0\), \(\kappa\to k\); bounded convergence against Schwartz tests gives (39) as exactly the upper boundary. Splitting its convolution at \(y=x\) and letting the integrable forcing tails tend to zero gives

\[
 \begin{aligned}
 a_+&=\lim_{x\to+\infty}e^{-ikx}(K_\lambda*f)(x)
       =\frac{i\sqrt{2\pi}}{2k}\widehat f(k),\\
 a_-&=\lim_{x\to-\infty}e^{ikx}(K_\lambda*f)(x)
       =\frac{i\sqrt{2\pi}}{2k}\widehat f(-k).
 \end{aligned}
 \tag{40}
\]

For the negative spatial direction take \(s=-x\) and reflected momentum \(\xi'=-\xi\). The distinguished velocity becomes \(+2k\). Both outgoing amplitudes have the same \(+i\) factor. The shell consists of two points, with counting measure and \(g=2k\), so

\[
 \begin{aligned}
 q_f(\lambda)
   &=\frac{|\widehat f(k)|^2+|\widehat f(-k)|^2}{2k}\\
   &=\frac{k}{\pi}(|a_+|^2+|a_-|^2).
 \end{aligned}
 \tag{41}
\]

This checks both the velocity factor and the unitary Fourier normalization.

**Exercise 2 — Intermediate: assemble the channels.** On a compact regular shell let \(\sum_\nu\chi_\nu=1\) be a finite smooth partition. Suppose \(F_j\) are globally defined shell functions and each \(\chi_\nu F_j\) converges strongly in weighted shell \(L^2\), uniformly over a compact energy interval under fixed chart trivializations. Prove existence and partition independence of the global limit. Explain why unrelated constants in the chart phases obstruct this argument.

**Solution 2.** The triangle inequality gives

\[
 \begin{aligned}
 &\|F_j-F_l\|_{L^2(dS/g)}\\
 &\quad\le\sum_\nu\|\chi_\nu(F_j-F_l)\|_{L^2(dS/g)}.
 \end{aligned}
 \tag{42}
\]

The finite sum tends uniformly to zero. Completeness gives one global limit \(F\). Each bounded multiplier \(\chi_\nu\) then gives the local limit \(\chi_\nu F\), so every local channel relation holds for this function. Another partition approximates the same sequence \(F_j\); uniqueness of its Hilbert-space limit proves independence. Adding a constant \(\theta_\nu\) to a chart phase multiplies its corrected amplitude by \(e^{-i\theta_\nu}\). Two different choices can assign different values to the same nonzero overlap. A single normalized global finite-range action ensures that all charts approximate one sequence.

**Exercise 3 — Intermediate: a weak phase can lose all its norm.** On \(L^2([0,2\pi])\), let \(M_j\) be multiplication by \(e^{ij\xi}\). Prove weak-star convergence to zero in \(L^\infty\). Take \(U_j=1\), \(J_j=M_j\), and check \((U_ju,v)=(M_ju,J_jv)\). Which convergence required in Section 6 fails?

**Solution 3.** Integration by parts against \(h\in C^1([0,2\pi])\) bounds the oscillatory integral by \((|h(0)|+|h(2\pi)|+\|h'\|_1)/j\). Approximate any \(L^1\) test by \(C^1\) tests. The remaining pairing is bounded by the \(L^1\) approximation error since \(|e^{ij\xi}|=1\). Choose that approximation and then \(j\); this proves weak-star convergence to zero.

Every \(M_j\) is unitary, so \((M_ju,M_jv)=(u,v)\), proving the proposed identity. But for \(v=1\), orthogonality of distinct integer exponentials gives

\[
 \|J_jv-J_lv\|_2^2=4\pi,\qquad j\ne l.
 \tag{43}
\]

Thus the stationary maps do not converge strongly even on this vector. Strong convergence of \(J_I^{(j)}v\) was essential to freeze its \(L^1\) product before passing the weak-star phase limit. Without it the limit phase may be zero.

**Exercise 4 — Advanced: quantitative norm rigidity.** Let \(J:\mathcal H\to K\) satisfy \(J^*J=P\), where \(P\) is an orthogonal projection. Take \(K=L^2(X)\) with \(X\) sigma-finite, and suppose \(U=J^*M\), \(|M|\le1\). If \(\|Uq\|\ge(1-\epsilon)\|q\|\) for all \(q\), with \(0\le\epsilon<1\), bound \(1-|M|^2\) almost everywhere. For \(\epsilon=0\), find a preimage of every \(v=Pv\).

**Solution 4.** Since \(\|J^*\|\le1\),

\[
 (1-\epsilon)^2\|q\|^2
      \le\|Mq\|^2=\int_X|M|^2|q|^2.
 \tag{44}
\]

On a finite-measure subset where \(|M|^2<(1-\epsilon)^2\) by a fixed positive amount, the characteristic-function test contradicts (44). Use a sigma-finite exhaustion and a countable union over positive margins. The conclusion is \(0\le1-|M|^2\le2\epsilon-\epsilon^2\) almost everywhere. At \(\epsilon=0\) this gives \(|M|=1\). Set \(q=\overline M Jv\); then \(Uq=J^*M\overline M Jv=Pv=v\). Also \(J=JP\), so the range of \(U\) lies in \(P\mathcal H\) and is exactly that subspace. In the Fourier identification of the free space this is the preimage in (30).

**Exercise 5 — Advanced: energy commutation is weaker.** In momentum \(L^2(\mathbb R)\), let \(P_0(\xi)=\xi^2\) and \(Rq(\xi)=q(-\xi)\). Show that \(R\) is unitary and commutes with every bounded Borel function of \(P_0\), but cannot be multiplication by a scalar phase. Explain what extra identity for two scalar time modifiers rules out this phenomenon.

**Solution 5.** Reflection preserves Lebesgue measure, and \(R^2=1\), so \(R\) is unitary. Since \(P_0(-\xi)=P_0(\xi)\), it commutes with every \(b(P_0)\). A nonzero function supported in \((1,2)\) is sent to one supported in \((-2,-1)\). A scalar multiplier preserves the original support, so it cannot equal \(R\).

For two scalar modifiers their comparison has the exact identity

\[
 A_t^*A'_t=\mathcal F^{-1}e^{i(W-W')}\mathcal F.
 \tag{45}
\]

It commutes with every frequency indicator, including indicators separating equal-energy channels. On the complete wave range the adjoints converge strongly, as in (37), giving a strong limit of (45). Indicator tests on increasing bounded boxes construct compatible local \(L^2\) functions \(N\), and almost-everywhere subsequences preserve \(|N|=1\). Simple-function approximation identifies the full limit with multiplication by \(N\). Thus modifier ambiguity is a scalar frequency phase, whereas the scattering operator can mix equal-energy channels.

## References

- [Y] Dmitri Yafaev, *Lectures on scattering theory*, arXiv:math/0403213v1, 12 March 2004; prepared by Andrew Hassell from the 2001 ANU lectures. [Free version read](https://arxiv.org/pdf/math/0403213v1). Section 3 treats long-range Schrödinger comparison; it does not supply the full differential-polynomial theorem here.
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, 2014. [Freely readable author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf). Theorem 5.1 gives the self-adjoint unitary evolution and generator domain; Lemma 12.3 gives the Cook-integral criterion. The required programme proofs are identified above.
- [O] Sung-Jin Oh, *Lecture Notes for Math 222A*, University of California, Berkeley, Fall 2023. [Free lecture notes](https://math.berkeley.edu/~sjoh/pdfs/notes-math222a.pdf), Section 2.4.1 on Hamilton characteristics.
- [H76] Lars Hörmander, *The existence of wave operators in scattering theory*, Mathematische Zeitschrift **146** (1976), 69–91. [Freely accessible journal scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf). Section 3 constructs modified waves for admissible differential perturbations; Theorems 3.9–3.10 assume \(\det P_0''\not\equiv0\) and establish existence and comparison of ranges. They do not prove asymptotic completeness.

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, §30.5, (30.5.38)–(30.5.45), pp. 327–329; Theorem 30.5.10 and its proof, p. 329. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
