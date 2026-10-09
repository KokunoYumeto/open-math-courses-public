# Truncated operators and stable scattering amplitudes

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Does local agreement of truncated forces imply agreement of far-field amplitudes?** The phase \(\varepsilon\log(1+t)\) tends to zero for each fixed time as \(\varepsilon\to0\), but can equal \(\pi\) at an exponentially large time. This simple calculation shows why local coefficient convergence cannot replace uniform resolvent, radiation and amplitude estimates. A growing cutoff must preserve the constants used at infinity.

Cutting off a force makes it act only in a bounded region. We want to recover the original scattering problem as that region grows. Agreement on every bounded set does not by itself control a resolvent at real energy or an amplitude measured at infinite distance. The proof needs a common resolvent bound, a radiation condition that survives the changing operator, and a uniform estimate for the final amplitude.

Read [Admissible differential perturbations](admissible-differential-perturbations.md#admissible-coefficient-class) and [Regularizing long-range coefficients](long-range-coefficient-calculus.md#coefficient-dyadic-regularization) for the coefficient classes used here. [Limiting absorption for long-range differential perturbations](limiting-absorption-for-long-range-differential-perturbations.md#lap-theorem) supplies the fixed-operator boundary values and homogeneous radiation uniqueness. The kernel argument comes from [Frequency cutoffs and compact scattering remainders](frequency-cutoffs-and-compact-scattering-remainders.md#cutoff-compact-remainder). The local Hamilton geometry is in [Hamilton trajectories under a long-range force](hamilton-trajectories-under-a-long-range-force.md), [Escaping Lagrangians on regular energy surfaces](escaping-lagrangians-on-regular-energy-surfaces.md), and [Generating functions and the end of a localized force](generating-functions-and-the-end-of-a-localized-force.md). Finally, [Commuting coordinates for long-range evolution](commuting-coordinates-for-long-range-evolution.md) and [Transverse moments and outgoing amplitudes](transverse-moments-and-outgoing-amplitudes.md#amplitude-uniform-stability) give the factored evolution and its amplitude stability theorem.

We use Fourier inversion, Plancherel and smooth finite-dimensional flows. The complete [Hilbert-valued integration receiver](../providers/analysis/hilbert-valued-integration.md) proves the norm fundamental theorem, bounded-map integral rule, propagator variation and integrable tails used below. The arbitrary-self-adjoint spectral theorem, including its original second-moment domain, is proved in [Self-adjoint spectral calculus with the original domain](../providers/analysis/self-adjoint-spectral-domains.md#self-adjoint-pvm-domain), through the complete bundled unitary and Cayley-transform proofs, with no lower-bound or separability assumption. Section 1 of [Wave operators and modified phases](wave-operators-and-modified-phases.md) proves the group and generator criterion. [Distorted Fourier transforms and spectral density](distorted-fourier-transforms-and-spectral-density.md), [Lemma 1.1](distorted-fourier-transforms-and-spectral-density.md#distorted-poisson), proves continuous-test spectral inversion. Hörmander's freely accessible wave-operator paper [H76] treats differential perturbations and phase comparison; Yafaev [Y] treats a Schrödinger model. Their comparison theorems do not supply the uniform truncation and strong channel-amplitude assertion proved here. Teschl [T] and Oh [O] supply spectral and analytic background.

<a id="truncation-setting"></a>

## 1. The approximation statements

Use \(D=-i\partial\), left quantization, and an inner product linear in its first entry. Put \(X=\langle x\rangle\), \(\Xi=\langle\xi\rangle\), and

\[
 \|u\|_{s,t}=\|X^t\langle D\rangle^s u\|_2.
 \tag{1}
\]

For \(r_k=2^k\), let \(S_0=\{|x|<1\}\) and \(S_k=\{2^{k-1}\le|x|<2^k\}\), \(k\ge1\). The endpoint norms are

\[
 \begin{aligned}
 \|f\|_B&=\sum_{k\ge0}r_k^{1/2}\|f\|_{L^2(S_k)},\\
 \|u\|_{B^*}&=\sup_{k\ge0}r_k^{-1/2}\|u\|_{L^2(S_k)},\\
 \|u\|_{\mathcal Y_m}
     &=\sum_{|\alpha|\le m}\|D^\alpha u\|_{B^*}.
 \end{aligned}
 \tag{2}
\]

Every component of \(\mathcal Y_m\) is a derivative of the same distribution. Weak-star convergence in this space means convergence of every displayed derivative against every \(B\) test. Write \(\dot B^*\) for the \(B^*\)-norm closure of Schwartz space.

Let \(P_0\) be a real scalar elliptic polynomial of integer order \(m\ge1\). Let \(V\) be a symmetric, elliptic, \(2\)-admissible differential perturbation, with the continuous highest coefficients and sharp local coefficient products of the first prerequisite. Its realization is

\[
 H=P_0(D)+V,\qquad \mathcal D(H)=H^m.
 \tag{3}
\]

Choose real \(\rho\in C_c^\infty(\mathbb R^n)\), equal to one on the unit ball, and define

\[
 \rho_j(x)=\rho(x/j),\qquad
 H_j=P_0(D)+\rho_jV\rho_j.
 \tag{4}
\]

Let \(Z(P_0)\) be the critical values of \(P_0\), let \(\mathcal A\) be the eigenvalues of \(H\) outside that set, and put \(\Omega=\mathbb R\setminus(Z(P_0)\cup\mathcal A)\).

The cutoff approximation and common boundary estimate below follow the construction in Hörmander [H4, §30.5, p. 326].

**Theorem 1.1.** Let \(I\subset\Omega\) be a compact interval. For all sufficiently large \(j\), \(H_j\) is self-adjoint on the common domain \(H^m\), has no eigenvalue on \(I\), and has both boundary resolvents there. There are a complex neighborhood \(\mathcal O\) of \(I\) and \(C_I\), independent of \(j\), such that

\[
\begin{gathered}
 \|(H_j-z)^{-1}f\|_{\mathcal Y_m}\le C_I\|f\|_B,\\
 z\in\mathcal O,\qquad \operatorname{Im}z\ne0.
\end{gathered}
\tag{5}
\]

The same bound holds for \(R_{j,\sigma}(\lambda)=(H_j-\lambda-\sigma i0)^{-1}\), \(\sigma=\pm1\). If \(\lambda_j\to\lambda\) in \(I\) and \(f_j\to f\) in \(B\), then

\[
\begin{gathered}
 D^\alpha R_{j,\sigma}(\lambda_j)f_j
       \rightharpoonup^*D^\alpha R_\sigma(\lambda)f,\\
 |\alpha|\le m,\\
 R_{j,\sigma}(\lambda_j)f_j\longrightarrow R_\sigma(\lambda)f\\
 \text{in }H^{m,-b},\qquad b>1/2.
\end{gathered}
\tag{6}
\]

For fixed \(f\), these convergences are uniform in \(\lambda\in I\), with weak-star uniformity understood for each \(B\) test. They also hold for norm-continuous \(B\)-valued \(f(\lambda)\), or for \(f_j(\lambda)\) converging to it uniformly in \(B\).

This amplitude convergence is Hörmander [H4, (30.5.37)]. The source leaves its detailed uniformity argument to the reader; Sections 8–12 give that argument with the data, phases and operator norms specified.

**Theorem 1.2.** Work in a fixed regular frequency chart with a positive distinguished free velocity component. Use one compact frequency cutoff \(\chi\), one transverse cutoff, and the normalized Hamilton constructions with one common starting time. Let \(G_j,G\) be their local real generating functions, and set

\[
 \begin{aligned}
 v_{j,\lambda}(s)&=[\chi(D)R_{j,+}(\lambda)f](s,\cdot),\\
 v_\lambda(s)&=[\chi(D)R_+(\lambda)f](s,\cdot).
 \end{aligned}
 \tag{7}
\]

Each line takes the transverse slice at \(x_1=s\) after applying the full frequency-localized resolvent. These slices have continuous \(L^2(\mathbb R^{n-1})\) representatives. On every compact energy interval for which this chart and cutoff are valid, their strong amplitudes satisfy

\[
 \begin{gathered}
 a_j(\lambda)=\lim_{s\to\infty}
                     e^{-iG_j(s,D_z,\lambda)}v_{j,\lambda}(s),\\
 a(\lambda)=\lim_{s\to\infty}
                     e^{-iG(s,D_z,\lambda)}v_\lambda(s),\\
 \sup_\lambda\|a_j(\lambda)-a(\lambda)\|_{L^2_z}\longrightarrow0.
 \end{gathered}
 \tag{8}
\]

The conclusion also holds for the compact forcing families in Theorem 1.1. The other boundary sign and outgoing direction have the corresponding signed construction. In dimension one the transverse Hilbert space is \(\mathbb C\). Empty free shells have no local channels, and are covered by the off-energy estimates.

We prove the resolvent statement first. We then obtain strong localized forcing, compare finite Hamilton trajectories and normalized actions, and apply the amplitude stability theorem.

<a id="truncation-real-split"></a>

## 2. What the cutoff changes

Regularization permits a real-left splitting \(V=L^{\mathrm r}+S^{\mathrm r}\), where
\(L^{\mathrm r}=\sum\ell_\alpha D^\alpha\) is smooth. For some \(0<\delta_0<1/3\), its coefficients have every derivative bound

\[
\begin{gathered}
 |\partial_x^\beta\ell_\alpha(x)|\le C_{\alpha\beta}X^{-\mu_0(|\beta|)},\\
 \mu_0(k)=
 \begin{cases}
 \delta_0+k,&0\le k\le2,\\
 1+(1+\delta_0)k/2,&k\ge2.
 \end{cases}
\end{gathered}
\tag{9}
\]

The short-range coefficients \(c_\alpha\) of \(S^{\mathrm r}\) obey

\[
 \|c_\alpha\|_{L^{p_\alpha}(B(y,1))}
       \le C_\alpha\langle y\rangle^{-1-\epsilon_0},
 \qquad \epsilon_0>0.
 \tag{10}
\]

Here \(p_\alpha=\infty\) at order \(m\). At lower order, put \(k=m-|\alpha|>0\): take \(p_\alpha=n/k\) when \(n>2k\), a fixed finite \(p_\alpha>2\) when \(n=2k\), and \(p_\alpha=2\) when \(n<2k\). The highest coefficients are continuous. A fixed compact adjustment can make \(L^{\mathrm r}\) zero on a sufficiently large ball for the energy-root construction; that adjustment is included in \(S^{\mathrm r}\).

Write \(V=\sum a_\alpha D^\alpha\). The finite product rule gives the exact splitting

\[
\begin{aligned}
 L_j^{\mathrm r}&=\rho_j^2L^{\mathrm r},\\
 S_j^{\mathrm r}&=\rho_j^2S^{\mathrm r}\\
 &\quad+\rho_j\sum_{|\alpha|\le m}a_\alpha
       \sum_{\beta<\alpha}\binom{\alpha}{\beta}
                   (D^{\alpha-\beta}\rho_j)D^\beta.
\end{aligned}
\tag{11}
\]

In the inner sum, \(\beta\le\alpha\) coordinatewise and \(\beta\ne\alpha\). It uses every coefficient of \(V\). The total \(\rho_jV\rho_j\) is symmetric by two test pairings with real \(\rho_j\). Its real-left part \(L_j^{\mathrm r}\) need not be separately symmetric.

The slope of the concave function \(\mu_0\) is at most one. Therefore

\[
 \mu_0(k)\le q+\mu_0(k-q),\qquad 0\le q\le k.
 \tag{12}
\]

A positive cutoff derivative of order \(q\) has size \(C_qj^{-q}\) on \(j\le|x|\le Cj\). There \(j\) and \(X\) are comparable. Every distributed derivative of \(\rho_j^2\ell_\alpha\) thus retains (9), with common constants. The commutator terms containing a long-range coefficient gain at least one cutoff derivative, so their size is at most \(CX^{-1-\delta_0}\).

For a rough coefficient, the exponent required at the lower order \(\beta\) is no greater than the exponent at order \(\alpha\). The inclusion between these local \(L^p\) spaces on a unit ball is bounded. Multiplication by a cutoff derivative therefore preserves the required product estimate and short-range decay. All commutator terms have lower order, so the continuous highest coefficients are retained.

The full principal coefficients agree with those of \(H\) on \(|x|<j\). Outside that ball the perturbing principal coefficients are uniformly small for large \(j\). The bounded cutoff gives a common ellipticity modulus through its transition region. [The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md#domain-transfer) consequently gives the asserted realization of \(H_j\).

The same actual local product estimate yields

\[
\begin{aligned}
 e_j&:=\|H_j-H\|_{H^m\to L^2}\\
    &\le C\bigl(j^{-\delta_0}+j^{-1-\epsilon_0}\bigr)
       \longrightarrow0.
\end{aligned}
\tag{13}
\]

For the main coefficient differences use their support outside \(j\); unit balls enlarge it by at most one. A long-range cutoff commutator has the better rate \(j^{-1-\delta_0}\). The rough commutators have an extra cutoff power as well. This argument includes the actual highest derivative products.

Insert \(H=H_j+(H-H_j)\) in the fixed graph inequality. For \(u\in H^m\),

\[
 \|u\|_{H^m}\le C_H(\|H_ju\|+\|u\|)
                         +C_He_j\|u\|_{H^m}.
 \tag{14}
\]

Absorption for large \(j\) gives one graph constant. The opposite bound follows from the common coefficient product estimates.

<a id="truncation-groups"></a>

The common-domain comparison below is the argument for Hörmander [H4, (30.5.44), pp. 328–329], with its difference quotient made explicit.

For later use, the unitary groups converge strongly on finite time intervals. For \(f\in H^m\), spectral evolution preserves its graph norm, and the common-domain product rule gives

\[
 \frac d{dt}\bigl(e^{itH_j}e^{-itH}f\bigr)
       =i e^{itH_j}(H_j-H)e^{-itH}f.
 \tag{15}
\]

Here is the common-domain product rule explicitly. Put \(w(t)=e^{-itH}f\). Spectral dominated convergence in the measure \((1+\lambda^2)d(E_H(\lambda)f,f)\) makes this path continuous in the graph norm of \(H\), hence in \(H^m\) and in the graph norm of each fixed \(H_j\). Its Hilbert derivative is \(-iHw(t)\). In the difference quotient of \(e^{itH_j}w(t)\), split the increment into the change of the group on the fixed vector \(w(t)\in\mathcal D(H_j)\) and the change of \(w\) multiplied by the unitary at the new time. The self-adjoint generator criterion gives \(iH_jw(t)\) for the first quotient; strong continuity and \(w'=-iHw\) give the second. This proves (15) in Hilbert norm. Its right side is continuous because \(H_j-H:H^m\to L^2\) is bounded and \(w\) is \(H^m\)-continuous. The norm fundamental theorem therefore integrates (15). Integration and unitarity give

\[
 \sup_{|t|\le T}\|e^{-itH_j}f-e^{-itH}f\|
       \le C_T e_j\|f\|_{H^m}.
 \tag{16}
\]

Approximate any \(L^2\) vector by \(H^m\) vectors. The two unitary approximation errors have sum at most \(2\|f-f_k\|\). Choose \(k\), then \(j\). This proves strong finite-time convergence for every \(L^2\) vector.

<a id="truncation-weighted-graphs"></a>

## 3. Bounded graphs have strong weighted limits

Suppose \((H_j-z_j)u_j=f_j\), \(z_j\to\lambda\), \(f_j\to f\) in \(B\), and \(\|u_j\|_{\mathcal Y_m}\) is bounded. The derivative-graph compactness lemma in the limiting-absorption prerequisite supplies a subsequence with weak-star derivatives and

\[
 u_j\longrightarrow u\quad\text{in }H^{0,-b},
                  \qquad b>1/2.
 \tag{17}
\]

Its [complete compactness proof](limiting-absorption-for-long-range-differential-perturbations.md#lap-compactness) uses local Sobolev compactness and the summable shell tail \(\sum r_k^{1-2b}\). On every fixed ball, \(H_j=H\) eventually, including all differential products. The sharp local coefficient product is a bounded map from local \(H^m\) to \(L^2\). Its weak continuity identifies the equation
\((H-\lambda)u=f\).

The derivative endpoint bound also puts every \(u_j,u\) in \(H^{m,-b}\). Insert the comparable weight on each unit ball in the coefficient product proof. The coefficients of \(H_j-H\) have uniformly small local norms by (13). Weighted integer derivative equivalence, proved in [Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-integer-derivatives), gives

\[
\begin{gathered}
 \|(H_j-H)u_j\|_{0,-b}
       \le C_b e'_j\sum_{|\alpha|\le m}\|X^{-b}D^\alpha u_j\|,\\
 e'_j\longrightarrow0.
\end{gathered}
\tag{18}
\]

No rough coefficient is differentiated. Thus

\[
\begin{aligned}
 H(u_j-u)={}&f_j-f+(z_j-\lambda)u_j\\
            &+\lambda(u_j-u)+(H-H_j)u_j\\
       \longrightarrow{}&0\quad\text{in }H^{0,-b}.
\end{aligned}
\tag{19}
\]

Apply the fixed weighted graph inequality to these already known weighted Sobolev inputs. Together with (17), it proves

\[
 u_j\longrightarrow u\quad\text{in }H^{m,-b},\qquad b>1/2.
 \tag{20}
\]

This conclusion is conditional on a bounded endpoint graph. The common resolvent bound will be proved below.

<a id="truncation-symmetric-split"></a>

## 4. A symmetric split for the resolvent estimate

For the commutator argument use a different split of the same \(V\). [Combining the long-range resolvent estimates](combining-the-long-range-resolvent-estimates.md), Sections 2–4, constructs \(V=L+S\), with both parts symmetric on compact smooth tests, \(L\) smooth and \(P_0+L\) elliptic. Its coefficients satisfy, for some \(\delta_L>0\),

\[
\begin{gathered}
 |\ell_\alpha|\le C_\alpha X^{-\delta_L},\\
 |\partial^\beta\ell_\alpha|\le C_{\alpha\beta}X^{-1-\delta_L|\beta|},
 \qquad|\beta|\ge1.
\end{gathered}
\tag{21}
\]

Complex lower coefficients are allowed in this symmetric left expression. The coefficients of \(S\) are short range with a gap \(\epsilon_S>0\).

Set \(L_j=\rho_jL\rho_j\), \(S_j=\rho_jS\rho_j\). Both are symmetric, and \(H_j=P_0+L_j+S_j\). Choose once

\[
\begin{gathered}
 0<\delta<\min(\delta_L,\epsilon_S,\delta_0,\epsilon_0,1/3),\\
 d_*=1+\delta,\qquad a_*=(1+\delta)/2.
\end{gathered}
\tag{22}
\]

The cutoff coefficient expansion is the same finite rule as (11). Its smooth coefficients obey (21) with the smaller gap \(\delta\), uniformly in \(j\). For a physical derivative of total order \(k\ge1\), a term with \(q<k\) cutoff derivatives has exponent at least \(q+1+\delta_L(k-q)\). If all derivatives hit the cutoff, it has exponent \(k+\delta_L\ge1+\delta k\). The commutator terms have an additional cutoff derivative. These bounds hold at every fixed derivative order. The principal part is \(\rho_j^2\) times that of \(L\), and the argument of Section 2 gives a common ellipticity modulus.

The primary short-range map and its symmetric integral dual are uniform:

\[
 \begin{gathered}
 S_j:H^{m,t}\longrightarrow H^{0,t+d_*},\\
 S_j:H^{0,t}\longrightarrow H^{-m,t+d_*}.
 \end{gathered}
 \tag{23}
\]

For the second line apply the primary map at weight \(-t-d_*\) and use symmetry with the exact weighted-space integral dual.

The strict choice of gap also gives, for every fixed \(t\),

\[
 \|S_j-S\|_{H^{m,t}\to H^{0,t+d_*}}
       \le C_tj^{-(\epsilon_S-\delta)}
       \longrightarrow0.
 \tag{24}
\]

Indeed, \(X^{d_*}\) times the local norm of \((\rho_j^2-1)c_\alpha\) is bounded by \(Cj^{-(\epsilon_S-\delta)}\). Each commutator coefficient gains a cutoff power. Conjugating the input weight adds derivatives of \(X^{-t}\) and lowers the differential order; its new local \(L^p\) exponent is no larger than the old one. Apply the unit-ball product estimate, integrate over centers by Fubini, and sum the finitely many differentiated terms. This proves (24) for the actual products.

<a id="truncation-compact-error"></a>

## 5. One estimate with a compact error

We first allow eigenvalues. On a complex neighborhood of any compact regular free-energy interval,

\[
\begin{gathered}
 \|u\|_{\mathcal Y_m}\le C\bigl(\|f\|_B+\|u\|_{0,-1}\bigr),\\
 (H_j-z)u=f,\qquad u\in H^m,\qquad\operatorname{Im}z\ne0,
\end{gathered}
\tag{25}
\]

with one constant for all large \(j\).

The weighted version of (13) at weight \(-d_*\) makes the fixed weighted graph inequality uniform by absorption. Since \(d_*\ge1\) and \(z\) stays bounded,

\[
 \|u\|_{m,-d_*}
       \le C\bigl(\|f\|_B+\|u\|_{0,-1}\bigr).
 \tag{26}
\]

The primary \(S_j\) map at weight \(-d_*\) bounds \(\|S_ju\|_2\) by the same expression.

Choose \(\chi_0,\chi\in C_c^\infty\), equal one near the free shells, with \(\chi=1\) near \(\operatorname{supp}\chi_0\). Their support lies away from critical frequencies. [The resolvent away from the energy surface](the-resolvent-away-from-the-energy-surface.md#off-energy-resolvent-estimate) gives, uniformly,

\[
 \|(1-\chi(D))u\|_{m,0}
       \le C\bigl(\|f\|_B+\|u\|_{0,-1}\bigr).
 \tag{27}
\]

Here is a finite construction of the required common constant. The common principal ellipticity, coefficient decay and bounded energies choose the same reciprocal region in that prerequisite. Its inverse has common differentiated bounds. Write its exact first identity as

\[
\begin{gathered}
 E_jA_j=1-C_0-\mathscr R_j,\\
 A_j=P_0+L_j-z,\qquad C_0=\chi_0(D),
\end{gathered}
\tag{28}
\]

where \(\mathscr R_j\) has symbol weight \(h=X^{-\delta}\Xi^{-1}\). Put \(C=1-\chi(D)\). Keep the ordered finite identity

\[
\begin{aligned}
 \left(\sum_{\ell<N}C\mathscr R_j^\ell E_j\right)A_j
     & =C-C\mathscr R_j^N\\
     &\quad-\sum_{\ell<N}C\mathscr R_j^\ell C_0.
\end{aligned}
\tag{29}
\]

Choose \(N\ge m\) with \(\delta N\ge1\). Then \(h^N\le X^{-1}\Xi^{-m}\), so the first remainder maps \(H^{0,-1}\) to \(H^{m,0}\). In the separated-cutoff terms, right multiplication by \(C_0\) is exact. Every finite coefficient with the left \(C\) vanishes on \(\operatorname{supp}\chi_0\). A sufficiently long finite remainder therefore has the same required weight. The finite inverse sum has weight \(\Xi^{-m}\) and maps \(L^2\) to \(H^m\). All constants use finitely many common bounds. Apply (29) to \(A_ju=f-S_ju\) and use (26) to obtain (27).

For the near-energy part, \(u\in H^m\) already implies \(S_ju\in H^{0,d_*}\subset B\). The symmetric dual map at weight \(-a_*\), followed by the compact-frequency smoothing \(\chi(D)\), gives

\[
 \|\chi(D)S_ju\|_B\le C\|u\|_{0,-a_*}.
 \tag{30}
\]

Its output weight is \(a_*>1/2\). [A resolvent estimate at noncritical frequencies](a-resolvent-estimate-at-noncritical-frequencies.md#noncritical-shell-estimate), applied to the symmetric \(P_0+L_j\), consequently gives

\[
 \|\chi(D)u\|_{B^*}
       \le C\bigl(\|f\|_B+\|u\|_{0,-a_*}\bigr).
 \tag{31}
\]

The free monotone multiplier and minimum free speed are fixed. The full long-range commutator has common stronger positive derivative bounds, and one finite order \(\delta N\ge1\) controls its remainder. Its positive-symbol and endpoint estimates therefore have common constants.

A fixed compact-frequency multiplier bounds every derivative of \(\chi(D)u\) by its zeroth endpoint norm. Combine (27) and (31). For \(b_0=1/2+\delta/4<a_*\), endpoint embedding gives \(\|u\|_{0,-b_0}\le C_{b_0}\|u\|_{\mathcal Y_m}\). Split physical space at a large radius to obtain

\[
 \|u\|_{0,-a_*}
       \le\eta C_{b_0}\|u\|_{\mathcal Y_m}
                       +C_\eta\|u\|_{0,-1}.
 \tag{32}
\]

Choose \(\eta\) after the common constant from (27)–(31) and absorb. This proves (25). Apply the same argument to \(-H_j\) for the lower half-plane. A finite energy cover supplies one neighborhood of the whole interval. If the nearby free shells are empty, take \(\chi=0\) and use only (27).

<a id="truncation-radiation"></a>

## 6. Radiation survives the changing operator

Suppose \(u_j=(H_j-z_j)^{-1}f_j\) has a bounded derivative graph, with \(\operatorname{Im}z_j>0\), \(z_j\to\lambda\) regular, and \(f_j\to f\) in \(B\). Section 3 gives its subsequential equation and strong weighted convergence. Choose

\[
 0<\gamma<\delta/2,\qquad b=a_*-\gamma>1/2.
 \tag{33}
\]

Then \(d_*-b=a_*+\gamma>1/2\). By (23)–(24),

\[
\begin{aligned}
 S_ju_j-Su&=S(u_j-u)+(S_j-S)u_j\\
 &\longrightarrow0\quad\text{in }H^{0,d_*-b}\subset B.
\end{aligned}
\tag{34}
\]

Thus \(f_j^0=f_j-S_ju_j\to f^0=f-Su\) strongly in \(B\).

Use the escape family \(q_R,Q_R,\Phi_R,s_R\) constructed in [Radiation for limits of long-range resolvents](radiation-for-limits-of-long-range-resolvents.md), Sections 5–6. It depends on the free polynomial, limiting energy and one fixed frequency cutoff, and is independent of \(j\). Its positive symbol is free geometry. In the exact finite commutator for \(P_0+L_j\), scalar zero-order products cancel. Positive coefficient derivatives have (21), and a fixed finite order with \(\delta N\ge1\) controls all full differential-order remainders. After the escape scaling, the error has the common class

\[
\begin{gathered}
 S(X^{2\gamma-1-\delta},G_\delta)=S(X^{-2b},G_\delta),\\
 G_\delta=X^{-2\delta}|dx|^2+\Xi^{-2}|d\xi|^2.
\end{gathered}
\tag{35}
\]

Its quadratic bound is \(C\|u_j\|_{0,-b}^2\). The domain identity is valid because \(u_j\in H^m\), \(Q_R\) preserves this space, and \(P_0+L_j\) is symmetric there. The term \(-\operatorname{Im}z_j\|Q_Ru_j\|^2\) is nonpositive. The escape estimate therefore reads

\[
 \begin{aligned}
 R^{-1}\|\operatorname{Op}(\Phi_R)u_j\|^2
 \le{}&-\operatorname{Im}(Q_Rf_j^0,Q_Ru_j)\\
      &+CR^{-2\gamma}\|u_j\|_{0,-b}^2.
 \end{aligned}
 \tag{36}
\]

Fix \(R\) first. Compact output support and frequency smoothing give strong convergence of the left output. The forcing in the pairing converges strongly in \(B\); the solution converges weak-star in \(B^*\). The last norm converges by (20). Hence

\[
 \begin{aligned}
 R^{-1}\|\operatorname{Op}(\Phi_R)u\|^2
 \le{}&-\operatorname{Im}(Q_Rf^0,Q_Ru)\\
      &+CR^{-2\gamma}\|u\|_{0,-b}^2.
 \end{aligned}
 \tag{37}
\]

Now let \(R\to\infty\). The escape kernel is zero on an inner ball of radius \(cR\), and has a common bounded \(B\) map. Its action on a Schwartz input has a rapidly decreasing outer tail. Density gives \(Q_Rf^0\to0\) in \(B\), whereas \(Q_Ru\) is uniformly bounded in \(B^*\). Thus the annular escape mass in (37) tends to zero.

The remaining radiation argument concerns the fixed limiting equation. Its off-energy part belongs to \(H^{m,1/2}\), because \(f^0\in B\subset H^{0,1/2}\). On the frequency collar, a symbol vanishing on an outgoing angular neighborhood factors through \(\Phi_R\) on the output annulus, up to an \(X^{-1}\) error. For a symbol vanishing exactly on the outgoing free bundle, split it into such a piece and a piece with arbitrarily small supremum on a thin energy-angular collar. The derivative-independent shell limsup estimate in Section 8 of the radiation prerequisite treats the second piece. Take the radius limit before shrinking that collar. The exact full-order decomposition through derivatives then gives

\[
\begin{gathered}
 h\in S(\Xi^m,G_1),\\
 G_1=X^{-2}|dx|^2+\Xi^{-2}|d\xi|^2,\\
 h|_{N_+(M_\lambda)}=0
       \quad\Longrightarrow\quad h(x,D)u\in\dot B^*.
\end{gathered}
\tag{38}
\]

Here \(M_\lambda=\{P_0=\lambda\}\) and
\(N_+(M_\lambda)=\{(t\nabla P_0(\xi),\xi):t>0,\ \xi\in M_\lambda\}\).
This is the full radiation condition. In dimension one the escape construction uses its signed half-line form. Empty shells are entirely off-energy.

For lower resolvents apply the argument to \(-H_j,-H,-P_0\), with \(-z_j,-f_j\). Its positive bundle is the original negative bundle. The same actual products, weights and domain assertions hold.

<a id="truncation-boundary"></a>

## 7. Remove the compact error and take boundary limits

Return to \(I\subset\Omega\). If no common bound (5) existed, choose \(j_k\ge k\), nonreal \(z_k\) of distance at most \(1/k\) from \(I\), and normalized graphs

\[
\begin{gathered}
 \|u_k\|_{\mathcal Y_m}=1,\qquad\|f_k\|_B<1/k,\\
 u_k=(H_{j_k}-z_k)^{-1}f_k.
\end{gathered}
\tag{39}
\]

Extract an energy limit \(\lambda\in I\) and one imaginary sign. Graph compactness and (25) give a limit with

\[
 1\le C\|u\|_{0,-1},\qquad (H-\lambda)u=0.
 \tag{40}
\]

Section 6 gives its signed radiation condition. The homogeneous radiation characterization in the limiting-absorption prerequisite makes \(u\) an eigenfunction of \(H\). Since \(\lambda\in I\subset\Omega\), this is impossible. A common neighborhood and bound therefore exist.

Each \(H_j\) separately satisfies that prerequisite. Its regular-energy eigenvectors have every polynomial weight, so belong to \(B\) and have finite nonzero derivative graph norm. An eigenvector \(e\) with eigenvalue \(\lambda\in I\) would obey

\[
 (H_j-\lambda-i\eta)^{-1}e=i\eta^{-1}e.
 \tag{41}
\]

This contradicts (5) for small \(\eta>0\). Hence large \(j\) have no eigenvalues on \(I\), and their own boundary values exist. Weak lower semicontinuity gives the same common endpoint bound.

Let \(\lambda_j\to\lambda\), \(f_j\to f\), and fix a sign. Choose a countable dense set of \(B\) tests. At the \(j\)-th fixed operator and energy, choose \(0<\eta_j<1/j\) so that

\[
 D^\alpha\bigl[(H_j-\lambda_j-\sigma i\eta_j)^{-1}f_j
                  -R_{j,\sigma}(\lambda_j)f_j\bigr]
 \tag{42}
\]

has pairing less than \(1/j\) against the first \(j\) tests, for all \(|\alpha|\le m\). Boundary existence permits this finite choice. The common endpoint bound extends the small difference to every test by density. Section 6 applies to the genuine nonreal graphs and gives the limiting-energy radiation condition. Every subsequential limit is consequently \(R_\sigma(\lambda)f\), by homogeneous uniqueness. Bounded graph compactness excludes a subsequence separated from that limit in any weak-star test.

The real boundary graphs themselves satisfy their actual equations and the common derivative bound. Section 3 upgrades this weak convergence to (6) for every \(b>1/2\). For fixed \(f\), a failed uniform conclusion on \(I\) would give a sequence of energies with a convergent subsequence. Apply (6) along it and the fixed-\(H\) boundary continuity, with the same weighted graph upgrade. Both limits coincide, a contradiction. The same compactness argument works for the forcing families stated in Theorem 1.1. This proves that theorem.

<a id="truncation-kernels"></a>

## 8. Real roots and changing compact kernels

Use the real-left split again. On a small common graph collar,

\[
\begin{aligned}
 &P_0(\xi)+L_j^{\mathrm r}(x,\xi)-\lambda\\
 &\qquad=(\xi_1-a_j(x,\eta,\lambda))Q_j(x,\xi,\lambda),\\
 &P_0(\xi)+L^{\mathrm r}(x,\xi)-\lambda\\
 &\qquad=(\xi_1-a(x,\eta,\lambda))Q(x,\xi,\lambda).
\end{aligned}
\tag{43}
\]

The fixed large zero region for \(L^{\mathrm r}\), all common regularized coefficient bounds, and positive \(\partial_{\xi_1}P_0\) give one collar and one nonzero quotient bound. [Energy-shell factors and outgoing equations](energy-shell-factors-and-outgoing-equations.md), Sections 5–7, gives the unique real roots and all their physical and frequency derivatives. Energy is a smooth external parameter throughout its finite implicit recursion. Put

\[
\begin{gathered}
 T_{j,\lambda}=\operatorname{Op}(b_{j,\lambda}),\qquad b_{j,\lambda}=\chi/Q_j,\\
 T_\lambda=\operatorname{Op}(\chi/Q).
\end{gathered}
\tag{44}
\]

Every fixed frequency derivative of the difference of the root symbols, quotients and reciprocals has supremum \(O(j^{-\delta_0})\), uniformly in \(x,\lambda\). To prove this, interpolate
\(L_\theta^{\mathrm r}=(1-\theta)L^{\mathrm r}+\theta L_j^{\mathrm r}\).
The root has a common positive derivative denominator. Its exact differentiated equation is

\[
 \partial_\theta a_\theta
   =-\frac{(L_j^{\mathrm r}-L^{\mathrm r})(x,a_\theta,\eta)}
           {\partial_{\xi_1}(P_0+L_\theta^{\mathrm r})
                                      (x,a_\theta,\eta)}.
 \tag{45}
\]

Every frequency derivative of the numerator contains a coefficient difference \(O(j^{-\delta_0})\). All root and denominator derivatives are commonly bounded. Differentiate this finite formula and integrate in \(\theta\). The finite quotient recurrence and reciprocal identity give the same rate.

Compact frequency support and integration by parts imply a kernel difference bounded by
\(C_Nj^{-\delta_0}(1+|x-y|)^{-N}\). The endpoint kernel estimate therefore gives

\[
 \sup_\lambda\|T_{j,\lambda}-T_\lambda\|_{B\to B}
       \le Cj^{-\delta_0}\longrightarrow0.
 \tag{46}
\]

The exact coefficients of \(S_j^{\mathrm r}-S^{\mathrm r}\) vanish inside \(j\) and have common short-range decay with
\(\kappa=\min(\delta_0,\epsilon_0)>0\). The enlarged-shell product estimate, summed only over those outer shells, gives

\[
 \begin{gathered}
 \|S_j^{\mathrm r}\|_{\mathcal Y_m\to B}\le C,\\
 \|S_j^{\mathrm r}-S^{\mathrm r}\|_{\mathcal Y_m\to B}
       \le Cj^{-\kappa}.
 \end{gathered}
 \tag{47}
\]

This includes the rough highest coefficient products.

Extend \(a_j,a\) by one real transverse cutoff \(\psi\), equal to one over the projection of \(\operatorname{supp}\chi\), and denote them by \(\widetilde a_j,\widetilde a\). The exact energy-factor remainder is

\[
\begin{aligned}
 \mathcal R_{j,\lambda}
   &=(D_s-\widetilde a_j(x,D_z))\chi(D)\\
   &\quad-T_{j,\lambda}(P_0+L_j^{\mathrm r}-\lambda)\\
   &=-\sum_{|\alpha|\le m}[T_{j,\lambda},\ell_{j,\alpha}]D^\alpha,
\end{aligned}
\tag{48}
\]

where \(\ell_{j,\alpha}=\rho_j^2\ell_\alpha\). The pre-derivative kernels are
\(K_{b_{j,\lambda}}(x,y)(\ell_{j,\alpha}(x)-\ell_{j,\alpha}(y))\).
The coefficient segment formula when \(|x-y|\le X(x)/2\), and arbitrary kernel distance decay in the complementary region, give

\[
\begin{aligned}
 |K_{\alpha,j,\lambda}(x,y)|
       &\le C_NX(x)^{-1-\delta_0}\\
       &\quad\cdot(1+|x-y|)^{-N}.
\end{aligned}
\tag{49}
\]

The double annular coefficient sum for these compact kernels has one summable majorant, independent of \(j,\lambda\). Its omitted sum outside a finite input-output shell window is uniformly small. Inside any fixed pair of balls the kernels are exactly equal to their untruncated kernels for large \(j\): coefficients, roots and quotients agree there. Choose the window first, then \(j\). Composition with the derivative graph components proves

\[
 \sup_\lambda\|\mathcal R_{j,\lambda}-\mathcal R_\lambda
                                  \|_{\mathcal Y_m\to B}\longrightarrow0.
 \tag{50}
\]

The fixed \(\mathcal R_\lambda\) and \(T_\lambda S^{\mathrm r}\) are compact graph maps by the [compact remainder](frequency-cutoffs-and-compact-scattering-remainders.md#cutoff-compact-remainder) and [smoothed-coefficient](frequency-cutoffs-and-compact-scattering-remainders.md#cutoff-smoothed-coefficients) proofs. They send bounded derivative-wise weak-star convergence to norm convergence, and are norm continuous in energy.

<a id="truncation-slices"></a>

## 9. Strong forcing produces strong local slices

Write \(u_{j,\lambda}=R_{j,+}(\lambda)f\), \(u_\lambda=R_+(\lambda)f\). The localized equation has the exact forcing

\[
\begin{aligned}
 g_{j,\lambda}
   &=T_{j,\lambda}f-T_{j,\lambda}S_j^{\mathrm r}u_{j,\lambda}\\
   &\quad+\mathcal R_{j,\lambda}u_{j,\lambda},\\
 (D_s-\widetilde a_j(s))v_{j,\lambda}
   &=g_{j,\lambda}.
\end{aligned}
\tag{51}
\]

All these forcings have a common \(B\) bound. Along any sequence of energies converging in the compact chart interval, Theorem 1.1 gives weak-star derivative graph convergence. Equations (46)–(50) remove the varying operators with small norm errors. The fixed compact maps then give strong convergence. For the term on \(f\), the bounded \(B\) map suffices. The limiting forcing is \(B\)-norm continuous in energy, by the frequency-kernel prerequisite. Compactness of the energy interval therefore gives

\[
 \sup_\lambda\|g_{j,\lambda}-g_\lambda\|_B\longrightarrow0.
 \tag{52}
\]

The same argument permits the compact forcing families in the theorem.

The root comparison and compact transverse kernels also give

\[
 \begin{gathered}
 \sup_{\lambda,s}\|\widetilde a_j(s)-\widetilde a(s)\|
       \le Cj^{-\delta_0},\\
 \|\widetilde a_j(s)-\widetilde a_j(s)^*\|
       \le C\langle s\rangle^{-1-\delta}.
 \end{gathered}
 \tag{53}
\]

The second line follows from the real-kernel adjoint calculation and the common first physical derivative bound. Its integral is finite. Time derivatives of those kernels give local operator-norm continuity.

Each boundary solution has its own directional radiation. A fixed angular cutoff away from its outgoing velocity rays gives vanishing normalized ball mass in the region \(s<T\), for every fixed \(T\). The [outgoing theorem in the energy-root prerequisite](energy-shell-factors-and-outgoing-equations.md#energy-shell-outgoing) identifies its continuous transverse representative as

\[
 v_{j,\lambda}(s)
       =i\int_{-\infty}^s U_{j,\lambda}(s,t)g_{j,\lambda}(t)\,dt.
 \tag{54}
\]

The propagators have one bound in both time directions, from the common adjoint-defect integral. On a compact two-time rectangle, Duhamel's formula and (53) give uniform operator-norm convergence of propagators.

The embedding \(B\subset L^1(\mathbb R_s;L^2_z)\) turns (52) into strong integrable forcing convergence. To compare (54), split its integral at a large negative time. The old tail is uniformly small because the limiting forcing family is a compact subset of \(L^1\); the forcing differences are uniformly small in that norm. On the remaining finite rectangle use propagator convergence. Thus, with \(\mathcal H=L^2(\mathbb R^{n-1})\),

\[
 \sup_{\lambda,\ |s|\le S}
       \|v_{j,\lambda}(s)-v_\lambda(s)\|_{\mathcal H}
       \longrightarrow0,\qquad S<\infty.
 \tag{55}
\]

All slices have one common bound for every \(s\). This argument also proves strong slice continuity in energy. In transverse dimension zero the root operator is real scalar and its adjoint defect is zero.

<a id="truncation-phases"></a>

## 10. Compare the normalized Hamilton phases

The real coefficient family has common full regularized bounds with the smaller gap \(\delta\) from (22). In the scaled Hamilton proof, the low-order bounds choose one contraction tube, one positive interior margin and one starting time \(T\). The Hessian bound \(Ct^{-1-\delta}\) is integrable. Variation of constants and the finite derivative partitions give common constants at every higher fixed order.

The near-shell initial-sheet contraction has one regular collar and one inverse coefficient bound. The mixed projection inverse has a common first-derivative inverse bound, and every higher derivative follows by isolating it in the finite chain rule. The generating-function proof consequently gives, with \(\mu\) defined as in (9) using \(\delta\),

\[
\begin{gathered}
 |\partial_s^q\partial_\eta^\alpha(G_j-sE)|
       \le C_{q,\alpha}s^{1+|\alpha|-\mu(q+|\alpha|)},\\
 s\ge s_0,
\end{gathered}
\tag{56}
\]

for one \(s_0>2CT\). The initial finite action integral is commonly bounded on a fixed slice; integration of the first radial derivative controls the zeroth-order term too. All choices are uniform on the compact energy chart.

Fix \(S<\infty\). The inverse projection puts each relevant trajectory at a Hamilton time \(T\le t\le C_*S\). Its initial frequencies belong to one compact outer collar. The common escape estimates give

\[
 |x(t)|\le C_0t\le C_0C_*S.
 \tag{57}
\]

Choose a radius \(R_S\) containing these entire finite trajectory segments and the initial positions \(T\nabla P_0(\zeta)\), with \(\zeta\) denoting the full initial frequency, uniformly in energy and \(j\). Use a slightly larger slice interval as well.

For \(j>R_S\), the forces and all derivatives agree in that region. The near-shell initial sheet equations therefore have the same unique root. Their initial action values agree. ODE uniqueness makes their finite trajectories agree, and so does their normalized action

\[
\begin{aligned}
 \psi(t,\zeta)
   &=-T L^{\mathrm r}(T\nabla P_0(\zeta),\zeta)\\
   &\quad+\int_T^t x(\tau,\zeta)\cdot\xi'(\tau,\zeta)\,d\tau.
\end{aligned}
\tag{58}
\]

The two projection maps are identical there, and their unique inverses select the same point at \((s,\eta)\). Since \(G=s\xi_1-\psi\),

\[
\begin{gathered}
 G_j(s,\eta,\lambda)=G(s,\eta,\lambda),\\
 s_0\le s\le S,\qquad j>R_S.
\end{gathered}
\tag{59}
\]

This holds on an open neighborhood of the common cutoff support. All frequency jets agree, and the fixed real compact-frequency extensions agree everywhere. The comparison fixes action constants as well as differentials; Exercise 4 explains why that matters.

<a id="truncation-factors"></a>

## 11. The factored equations have common constants

Apply the explicit coordinate-telescoping factors from the commuting-coordinates prerequisite to each \(G_j,a_j\), using the same cutoffs. Its near and far derivative partitions use only their common root and phase bounds. The metric is the same:

\[
\begin{gathered}
 g_s=X_s^{-1-\delta}|dz|^2+X_s^{1-\delta}|d\eta|^2,\\
 X_s=(1+s^2+|z|^2)^{1/2}.
\end{gathered}
\tag{60}
\]

Its Planck weight is \(X_s^{-\delta}\). One finite product order \(K\delta\ge1\) gives the individual ordering and adjoint defects, coordinate commutators and factor bounds with common constants.

Write \(k\) for a transverse coordinate index and \(j\) for truncation. With \(A_{j,k}=z_k+G_{j,\eta_k}\), \(F_{j,k}=B_{j,k}A_{j,k}\), the exact bounded generator and ordering correction are

\[
\begin{aligned}
 M_j&=G_{j,s}(D_z)-\sum_k\operatorname{Op}(F_{j,k})
                                   -\mathcal T_j,\\
 \mathcal T_j&=-i\sum_k\operatorname{Op}(\partial_{\eta_k}B_{j,k}).
\end{aligned}
\tag{61}
\]

Here \(F_{j,k}=B_{j,k}A_{j,k}\) is a product of symbols, with \(A_{j,k}(s,z,\eta)=z_k+\partial_{\eta_k}G_j(s,\eta)\). The corresponding coordinate operator is its left quantization. The [exact ordering identity](commuting-coordinates-for-long-range-evolution.md#commuting-ordering) supplies \(\mathcal T_j\) when passing from the symbol product to the operator product.

They have the common bounds
\(\|\mathcal T_j(s)\|+\|M_j(s)-M_j(s)^*\|\le Cs^{-1-\delta}\).

For fixed \(S\), (59) makes all canonical coordinates identical. On the near branch \(|A|\le2s\), every coordinate path point has \(|z|\le CS\), so the roots and near factors are identical for large \(j\). On the far branch their difference is \(a-a_j\), multiplied by \(A_k/|A|^2\) or \(A_k^2/|A|^2\). These ratios and their needed frequency derivatives are bounded on \(|A|\ge s_0\), on the entire transverse space. The root comparison gives small frequency seminorms \(C_Sj^{-\delta_0}\) for the individual \(F_k\) differences and \(\partial_\eta B_k\) differences. Compact frequency support and Schur's kernel inequality give

\[
\begin{gathered}
 \sup_{\lambda,\ s_0\le s\le S}\|M_j(s)-M(s)\|\longrightarrow0,\\
 \sup_{\lambda,\ s_0\le s\le S}\|\mathcal T_j(s)-\mathcal T(s)\|
       \longrightarrow0.
\end{gathered}
\tag{62}
\]

Smooth dependence of finite sheets, flows, actions and their inverses on energy gives local norm continuity in that parameter by the same kernel bounds. When there are no transverse coordinates, the sums are empty and \(G_s=a\).

<a id="truncation-amplitudes"></a>

## 12. Take the amplitude limit

The actual localized solution has transverse frequency support where the chosen cutoff equals one. The exact factor identity therefore gives

\[
\begin{aligned}
 (D_s-M_j(s))v_{j,\lambda}&=h_{j,\lambda},\\
 h_{j,\lambda}&=g_{j,\lambda}+\mathcal T_j(s)v_{j,\lambda}.
\end{aligned}
\tag{63}
\]

Its initial values at \(s_0\) converge strongly and uniformly in energy by (55). The forcing converges in \(L^1([s_0,\infty);\mathcal H)\). Indeed, on a finite interval use (52), (55) and (62). Beyond \(S\), the correction terms have a common integral bound \(CS^{-\delta}\), by the uniform slice bound. Choose \(S\), then \(j\). Hence

\[
 \sup_\lambda\|h_{j,\lambda}-h_\lambda\|_{L^1}
       \longrightarrow0.
 \tag{64}
\]

The limiting pair \(\lambda\mapsto(v_\lambda(s_0),h_\lambda)\) is norm continuous into \(\mathcal H\times L^1\). Slice continuity treats the initial value; local norm continuity of the ordering correction and its common integrable tail treat the forcing. Its image is compact.

All hypotheses of the [uniform amplitude theorem](transverse-moments-and-outgoing-amplitudes.md#amplitude-uniform-stability) now hold: common factor, coordinate and individual adjoint bounds; local generator convergence; fixed-time phase convergence, which here is eventual equality; and strong convergence of the initial data and integrable forcing.

To recall its order of limits, approximate the compact limiting data family by finitely many weighted data pairs. For each fixed pair the canonical moment estimate gives a common amplitude tail \(C_kS^{-\delta}\), in addition to its integrable forcing tail. Choose the finite approximation, then \(S\), then \(j\). At this fixed \(S\), Duhamel and (59) give convergence of phase-corrected solutions. Uniform energy bounds remove the data approximation. This proves (8) for arbitrary data in \(\mathcal H\times L^1\), with no first-moment assumption on the original forcing.

Here is the explicit compact-family estimate behind this passage. Equip data with \(\|(w,h)\|_{\mathcal D}=\|w\|+\|h\|_{L^1}\). The common propagator bound and the unitary phase correction bound both the finite-slice maps and their amplitude limits by one constant \(C_A\) on \(\mathcal D\). For \(\varepsilon>0\), choose a finite \(\varepsilon\)-net \(d_1,\ldots,d_N\) for the limiting data family, with each \(d_k\) having smooth compactly supported transverse initial data and a finite simple time forcing of bounded support whose values are smooth and compactly supported in the transverse variables. Such pairs are dense in \(\mathcal D\): truncate the time tail, approximate by finite simple \(L^1\) functions, and approximate their finitely many \(\mathcal H\) values by smooth compactly supported vectors. This is the [all-data density argument](transverse-moments-and-outgoing-amplitudes.md#amplitude-all-data), and gives the required weighted integrability without a time differentiability assumption. On the compact energy interval these pairs have uniformly bounded canonical moments at \(s_0\), because every required phase jet there is commonly bounded. The moment estimate therefore gives one \(K_\varepsilon\), valid for these finitely many pairs, all energies and all sufficiently large \(j\). Take \(S\) beyond their forcing supports. With \(d_{j,\lambda}=(v_{j,\lambda}(s_0),h_{j,\lambda})\) and \(d_\lambda=(v_\lambda(s_0),h_\lambda)\), the triangle inequality gives

\[
 \begin{aligned}
 \sup_\lambda\|a_j(\lambda)-a(\lambda)\|
 \le{}&C_A\sup_\lambda\|d_{j,\lambda}-d_\lambda\|_{\mathcal D}
       +2C_A\varepsilon\\
      &+2K_\varepsilon S^{-\delta}+\tau_{j,\varepsilon}(S),
 \end{aligned}
\]

where \(\tau_{j,\varepsilon}(S)\to0\) for fixed \(S,\varepsilon\), uniformly in energy, by the finite-time generator and phase convergence for the finite net. First fix \(\varepsilon\), then choose \(S\), then use (55) and (64) to choose \(j\). Finally send \(\varepsilon\) to zero. The constant \(K_\varepsilon\) need not remain bounded in that last step; the stated order of choices is why arbitrary integrable forcing is allowed.

Taking the unitary transverse Fourier transform gives the same strong iterated limit in transverse frequency. For the lower boundary apply the construction to \(-H_j,-H,-P_0\); its positive free bundle is the original negative one. A chart with negative distinguished position direction uses the paired reflection of that position and frequency. The normalized initial action and all norm arguments transform with these signs. This proves Theorem 1.2.

### Use the conclusion

Keep the order of cutoff, spectral-boundary and amplitude limits explicit. Verify strong local slices and the comparison of normalized Hamilton phases before taking the final amplitude limit.

<a id="truncation-solutions"></a>

## 13. Graded exercises with complete solutions

**Exercise 1 — Basic: two exact cutoff splittings.** On the line take
\(H=D(1+b)D+c\), \(V=DbD+c\), with real smooth long-range \(b\), real bounded short-range \(c\), and \(1+b\) bounded below by a positive constant. For a real smooth cutoff \(\rho\), compute \(\rho V\rho\) in left differential form. Give a symmetric smooth split and a real-left split, and explain their different lower-order terms.

**Solution 1.** The rules \(D(\rho u)=\rho Du-i\rho'u\) and
\(D^2(\rho u)=\rho D^2u-2i\rho'Du-\rho''u\) give, with \(q=\rho^2b\),

\[
 \rho V\rho=qD^2-iq'D+\rho^2c-\rho(b\rho')'.
 \tag{65}
\]

The last scalar sign includes \((-i)(-i)=-1\) in the \(b'\rho'\) term. A symmetric smooth part is
\(L^{\mathrm{sym}}=DqD-\rho(b\rho')'\), with
\(S^{\mathrm{sym}}=\rho^2c\). This is exactly \(\rho DbD\rho\), with its cutoff potential displayed separately, and each part is symmetric on compact smooth tests.

For the real-left choice take \(L^{\mathrm r}=qD^2\) and
\(S^{\mathrm r}=-iq'D+\rho^2c-\rho(b\rho')'\). The symbol \(q\xi^2\) is real; its operator need not be symmetric. Its remaining terms restore total symmetry. For \(\rho(x)=\rho_0(x/j)\), \(q'=\rho^2b'+2\rho\rho'b\). Each term has short-range decay, using respectively a physical coefficient derivative or a cutoff inverse radius. The scalar commutator has two derivatives in total and has at least that decay.

**Exercise 2 — Intermediate: strict weight margins.** Take \(\delta=1/10\), \(\gamma=1/40\), \(\epsilon_S=1/4\), and \(m=4\). Compute \(b\), \(d_*-b\), the escape error exponent, the cutoff short-range norm-error power, and a finite off-energy order \(N\). Explain the strict endpoint margins.

**Solution 2.** Direct calculation gives

\[
\begin{gathered}
 a_*=\frac{11}{20},\qquad b=\frac{21}{40},\\
 d_*-b=\frac{23}{40},\\
 2\gamma-1-\delta=-\frac{21}{20}=-2b.
\end{gathered}
\tag{66}
\]

Both input compactness and output embedding weights exceed \(1/2\). The small short-range map has rate \(j^{-3/20}\). Choose \(N=10\): then \(N\ge m\), \(\delta N=1\), and \(h^N\le X^{-1}\Xi^{-m}\). At input \(b=1/2\), the compact graph tail sums a constant over infinitely many shells. At output weight \(1/2\), the Cauchy–Schwarz embedding into \(B\) has a nonsummable shell factor. The two arguments require strict inequalities.

**Exercise 3 — Intermediate: a strong weighted limit with no strong graph limit.** Let nonzero \(\phi\in C_c^\infty(\{1<|x|<2\})\), \(r_j=2^j\), and
\(w_j(x)=r_j^{(1-n)/2}\phi(x/r_j)\).
Compute its derivative endpoint norms. Prove derivative-wise weak-star convergence to zero and strong \(H^{m,-b}\) convergence for \(b>1/2\), while its \(\mathcal Y_m\) norm stays positive. For \(\epsilon>0\) and smooth \(\omega\) supported in the unit ball, show that \(Tw=X^{-1-\epsilon}(\omega*w)\) sends it to zero in \(B\).

**Solution 3.** Its support lies in \(S_{j+1}\), with outer radius \(2r_j\). Scaling gives

\[
 \begin{aligned}
 \|D^\alpha w_j\|_2&=r_j^{1/2-|\alpha|}\|D^\alpha\phi\|_2,\\
 \|D^\alpha w_j\|_{B^*}
       &=2^{-1/2}r_j^{-|\alpha|}\|D^\alpha\phi\|_2.
 \end{aligned}
 \tag{67}
\]

The graph is bounded, and its zeroth norm is the fixed positive number
\(2^{-1/2}\|\phi\|_2\). Pairing any derivative with a \(B\) test is bounded by its common endpoint norm times the test's norm on the receding shell. That tail tends to zero.

On the support \(X\) is comparable to \(r_j\). Weighted integer derivative equivalence gives
\(\|w_j\|_{m,-b}\le Cr_j^{1/2-b}\to0\) for \(b>1/2\).
The convolution output is supported in \(r_j-1\le|x|\le2r_j+1\), meeting at most three comparable shells for large \(j\). Its \(L^2\) norm is at most \(\|\omega\|_1\|w_j\|_2\). Therefore

\[
\begin{aligned}
 \|Tw_j\|_B&\le Cr_j^{1/2}r_j^{-1-\epsilon}\|\omega*w_j\|_2\\
           &\le Cr_j^{-\epsilon}\longrightarrow0.
\end{aligned}
\tag{68}
\]

These examples impose no resolvent equation. They explain how compact kernel actions can have strong limits when their input graphs have only weak-star limits.

**Exercise 4 — Advanced: the action constant matters.** In the scalar transverse case solve \((D_s-E)v=0\), \(v(s_0)=1\), for a real constant \(E\). Use \(G(s)=sE\) and \(G_j(s)=sE+\theta_j\), where \(\theta_j=0\) for even \(j\) and \(\pi\) for odd \(j\). Show that the generators and positive phase derivatives agree, with common bounds, but the amplitudes do not converge. Identify the missing hypothesis and the Hamilton normalization that supplies it.

**Solution 4.** The solution is \(v(s)=e^{iE(s-s_0)}\). There are no transverse factors or commutators; the evolutions coincide and are unitary. The bounded phase constants have a common zeroth-order growth bound too. However

\[
 e^{-iG_j(s)}v(s)=e^{-iEs_0}e^{-i\theta_j}
 \tag{69}
\]

alternates between two different amplitudes. The fixed-time phase difference fails to tend to zero. Agreement of phase derivatives alone does not fix the additive constant. In Section 10 the action has its specified value on the entire initial near-shell sheet and its specified finite trajectory integral. Equality of the coefficients and finite trajectories fixes both, on every component.

**Exercise 5 — Advanced: no first moment is needed.** Let real bounded continuous \(a_j,a\) on the line agree on \([-j,j]\). Choose real primitives \(G_j'=a_j\), \(G'=a\), with the same value at \(s_0\), for \(j>|s_0|\). Use \(g(s)=(1+|s|)^{-2}\) in each outgoing equation. Prove existence of the amplitudes, show that the first time moment of \(g\) is infinite, and prove the amplitude error bound \(4/(1+j)\).

**Solution 5.** The outgoing representative and its amplitude are

\[
 \begin{aligned}
 v_j(s)&=i e^{iG_j(s)}
                \int_{-\infty}^s e^{-iG_j(t)}g(t)\,dt,\\
 a_{\infty,j}&=i\int_{\mathbb R}e^{-iG_j(t)}g(t)\,dt.
 \end{aligned}
 \tag{70}
\]

The integrands are absolutely integrable because their phases have modulus one and \(\|g\|_1=2\). Differentiation verifies the equation with the factor \(i\) displayed. The primitive equality gives \(G_j=G\) on \([-j,j]\), whereas
\(2\int_0^\infty t(1+t)^{-2}\,dt=\infty\).
Thus the forcing has no finite first time moment. The phase differences vanish on that interval and have modulus at most two elsewhere, so

\[
 |a_{\infty,j}-a_\infty|
       \le2\int_{|t|>j}g(t)\,dt=\frac4{1+j}.
 \tag{71}
\]

Only fixed-time phase comparison and integrable forcing were needed.

<a id="compact-force-setting"></a>

## 14. The full compact-force stationary comparison

The next lesson needs a stationary transform for each fixed \(H_j\). Its highest differential coefficients may change inside the cutoff. Thus the compact-map hypothesis of [Asymptotic completeness for short-range operators](asymptotic-completeness-for-short-range-operators.md) cannot be assumed here: a compactly supported coefficient multiplying an order-\(m\) derivative need not give a compact map on the order-\(m\) graph. We prove the needed comparison using the full elliptic limiting-absorption theorem instead. The highest-order terms are retained throughout.

Fix a real elliptic \(p=P_0\) of order \(m\ge1\), and let
\[
 K=p(D)+C(x,D),\qquad \mathcal D(K)=H^m,
\]
where \(C\) is a symmetric \(1\)-admissible differential perturbation with all its coefficients supported in one bounded set, including any continuous highest coefficients. The total expression is elliptic. Each sufficiently large \(H_j\) satisfies these assumptions by Section 2. Constants in this subsection may depend on this fixed compact force. The [full limiting-absorption theorem](limiting-absorption-for-long-range-differential-perturbations.md#lap-theorem) applies because this is a special case of its admissible decay class; it does not require a compact perturbation map.

Put \(\Sigma_K=Z(p)\cup\mathcal A_K\), where \(\mathcal A_K\) consists of the regular-energy eigenvalues, and let \(\Omega_K=\mathbb R\setminus\Sigma_K\). The finite critical-value proof, together with [discreteness and closedness of the exceptional set](limiting-absorption-for-long-range-differential-perturbations.md#lap-open-energies), shows that \(\Sigma_K\) is closed and countable. The limiting-absorption theorem gives the boundary resolvents \(R_{K,\sigma}(\lambda):B\to\mathcal Y_m\), their actual equations and their full signed radiation uniqueness. We will construct canonical transforms \(J_{K,\sigma}\) and ordinary wave operators \(W_{K,\sigma}\) such that
\[
 \begin{gathered}
 J_{K,\sigma}^*J_{K,\sigma}=E_K(\Omega_K),\qquad
 J_{K,\sigma}W_{K,\sigma}=\mathcal F,\\
 W_{K,\sigma}=J_{K,\sigma}^*\mathcal F,\qquad
 \operatorname{ran}W_{K,\sigma}=E_K(\Omega_K)L^2
                              =\mathcal H_{\mathrm{ac}}(K).
 \end{gathered}
\]
The transform vanishes on all eigenvectors, including eigenvectors at critical energies. These are statements about the full compact-force class just specified.

We will use that every level set of the nonconstant polynomial \(p\) is null. The full dimension-induction and Fubini proof is in [Distorted Fourier transforms and spectral density, Section 2](distorted-fourier-transforms-and-spectral-density.md): outside the common zero set of a nonzero one-variable coefficient, a polynomial section has only finitely many roots. In particular the free Fourier multiplier has no \(L^2\) eigenvectors, so its good energies are precisely the regular ones.

<a id="compact-force-factorization"></a>

### Boundary factorization without compactness

Choose a compact smooth cutoff \(\zeta=1\) on a neighbourhood of every coefficient support. The actual local coefficient-product estimates give
\[
 \|Cu\|_B\le C_C\|\zeta u\|_{H^m}
               \le C'_C\|u\|_{\mathcal Y_m}.
\]
The first inequality uses that the output is supported in a fixed ball, on which \(B\) and \(L^2\) have comparable norms. The second follows by summing the finitely many derivatives on that ball. The same first inequality holds for global \(H^m\) inputs. No coefficient is differentiated. Symmetry extends to \(H^m\) by compact smooth approximation and these product bounds.

For later use, \(\lambda\mapsto CR_{K,\sigma}(\lambda)f\) is norm continuous in \(B\) for each \(f\in B\); the corresponding nonreal approach has the same limit. Indeed the fixed-operator graph argument in Section 3, or [Lemma 2.2 of the limiting-absorption lesson](limiting-absorption-for-long-range-differential-perturbations.md#lap-rough-graph), gives strong \(H^{m,-b}\) convergence for every \(b>1/2\). Its hypotheses are the common endpoint graph bound, convergence of the forcing in \(B\), and the actual equation. With the operator fixed, the coefficient-difference term in (19) is zero. Multiplication by \(\zeta\) and the preceding estimate then give strong \(B\) convergence of the products. The free operator has the same property with \(C\) as the compactly supported output map.

For \(\lambda\in\Omega_K\) set
\[
 A_\sigma(\lambda)=I-CR_{K,\sigma}(\lambda):B\longrightarrow B.
\]
It is bounded locally uniformly in energy and strongly continuous by the preceding paragraph. If \(u=R_{K,\sigma}(\lambda)f\), then \(f_0=f-Cu\in B\),
\((p(D)-\lambda)u=f_0\), and \(u\) has the free signed radiation condition. Free uniqueness, which is the full elliptic limiting-absorption theorem with zero perturbation, gives
\[
 R_{K,\sigma}(\lambda)f
       =R_{0,\sigma}(\lambda)A_\sigma(\lambda)f.
\]
Conversely, for \(f\in B\), the free solution \(u_0=R_{0,\sigma}(\lambda)f\) belongs to \(\mathcal Y_m\), and
\((K-\lambda)u_0=f+Cu_0\in B\). Its radiation condition is exactly the one in the uniqueness theorem for \(K\), since that condition uses the free polynomial. Consequently
\[
 \begin{aligned}
 R_{K,\sigma}(\lambda)(I+CR_{0,\sigma}(\lambda))f
       &=R_{0,\sigma}(\lambda)f,\\
 A_\sigma(\lambda)(I+CR_{0,\sigma}(\lambda))&=I,\\
 (I+CR_{0,\sigma}(\lambda))A_\sigma(\lambda)&=I.
 \end{aligned}
\]
The last identity follows from the first factorization and \(A_\sigma f=f-CR_{K,\sigma}f\). Thus \(A_\sigma\) is the actual bounded inverse of \(I+CR_{0,\sigma}\). This proof uses radiation uniqueness, with no Fredholm or relative-compactness inference.

<a id="compact-force-transform"></a>

### Construct the stationary transform and its spectral norm

Let \(T_\lambda\) be the canonical free Fourier trace from [Global radiation and flux](global-radiation-and-flux.md#global-amplitude-flux). This prerequisite applies to the elliptic polynomial: its strength is at most \(C\langle\xi\rangle^m\le C'(1+|p(\xi)|)\), so its simple-characteristic condition holds; an invariant direction would contradict ellipticity of the highest homogeneous part. On compact regular bands the free shell is compact and \(|\nabla p|\) is bounded below.

For \(f\in B\), prescribe the shell values
\[
 (J_{K,\sigma}f)|_{M_\lambda}
     =T_\lambda A_\sigma(\lambda)f,\qquad \lambda\in\Omega_K,
\]
and prescribe zero on \(p^{-1}(\Sigma_K)\). Here is the precise measurability input. The construction in Section 2 of [Distorted Fourier transforms and spectral density](distorted-fourier-transforms-and-spectral-density.md) applies to any continuous \(B\)-valued path \(a(\lambda)\). It approximates that path by locally finite parameter partitions with fixed compact-Fourier values and errors at most \(2^{-k}\) in \(B\). In energy coordinates the approximants are jointly measurable. The uniform trace bounds on compact energy sets make their successive shell \(L^2\) differences summable, so their pointwise sums define a measurable representative with the prescribed limit on every shell. Apply that proved construction to the actual path \(a=A_\sigma f\) above. It uses strong continuity of this path, not compactness of \(C\).

For \(u=R_{K,\sigma}(\lambda)f\), the compactly supported \(H^m\) vector \(\zeta u\) justifies the real quadratic form
\((u,Cu)=(\zeta u,C\zeta u)\). The equality holds because \(\zeta\) is identically one near the coefficient support; symmetry and \(H^m\) approximation make the value real. The exact free forcing-flux identity therefore gives
\[
 \frac{\sigma}{\pi}\operatorname{Im}(R_{K,\sigma}(\lambda)f,f)
     =\int_{M_\lambda}|T_\lambda A_\sigma(\lambda)f|^2
                                  \frac{dS}{|\nabla p|}.
\]
Continuous-test spectral inversion, Lemma 1.1 of the same earlier lesson, applies to every self-adjoint operator. The full limiting-absorption bound permits dominated convergence on each compact good interval. It identifies the scalar spectral measure of \(f\in B\) there with the displayed continuous density. Coarea is the proved coordinate formula CI7 in [Coordinate inverses and integration](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-integration). Integrate over compact good intervals and increase to \(\Omega_K\). Monotone convergence gives
\[
 \|J_{K,\sigma}f\|_2^2=\|E_K(\Omega_K)f\|_2^2.
\]
Dense \(B\subset L^2\) thus gives a unique bounded extension \(J_{K,\sigma}\), with norm at most one, and polarization gives \(J_{K,\sigma}^*J_{K,\sigma}=E_K(\Omega_K)\).

<a id="compact-force-spectral-parts"></a>

The same density calculation with a real continuous compactly supported energy test \(b\) gives \(J_{K,\sigma}^*b(p)J_{K,\sigma}=b(K)E_K(\Omega_K)\). Using it for \(b^2\) and expanding a squared norm proves
\(b(p)J_{K,\sigma}=J_{K,\sigma}b(K)E_K(\Omega_K)\).
Complex linearity includes complex continuous tests. To extend this to bounded Borel functions on \(\Omega_K\), approximate relatively open interval indicators by continuous compactly supported functions there, bounded by one; an increasing compact exhaustion supplies their support cutoffs. Dominated convergence in both spectral measures passes the identity to the limit. The sets whose indicators intertwine are closed under complements relative to \(\Omega_K\), intersections by multiplying the identities, and countable disjoint unions by strong additivity. Disjointifying a countable union shows that they form a sigma algebra, hence contain all Borel subsets. The transform vanishes on \(E_K(\Sigma_K)L^2\) by its norm identity and has zero values on \(p^{-1}(\Sigma_K)\). Bounded simple approximation therefore proves the assertion for every bounded Borel multiplier on \(\mathbb R\), including the unitary groups.

There is no remaining continuous spectral mass on \(\Sigma_K\). On \(\Omega_K\), the spectral density makes every null-set projection annihilate dense \(B\), hence all of \(L^2\). On the countable complement, the spectral theorem gives \(E_K(\{\lambda\})L^2=\ker(K-\lambda)\): the second-moment domain formula proves one direction, and integrating \(|t-\lambda|^2\) proves the other. Countable strong additivity makes \(E_K(\Sigma_K)L^2\) precisely the closed span of all eigenvectors. Thus \(E_K(\Omega_K)L^2=\mathcal H_{\mathrm{ac}}(K)\), and there is no singular continuous part.

<a id="compact-force-waves"></a>

### Ordinary waves for a full-order compact force

Take a packet \(f=\mathcal F^{-1}a\), with \(a\in C_c^\infty(\{\nabla p\ne0\})\), and put \(F_t=e^{-itp(D)}f\). On the fixed coefficient support, the phase gradient \(x-t\nabla p(\xi)\) has size at least \(c|t|\) for sufficiently large \(|t|\). Repeated integration by parts with the normalized phase-gradient operator from Section 2 of [Modified waves and the direction of escape](modified-waves-and-the-direction-of-escape.md) gives
\[
 \sup_{x\in\operatorname{supp}C}|D^\alpha F_t(x)|
        \le C_{N,\alpha,f}(1+|t|)^{-N},\qquad |\alpha|\le m.
\]
All coefficients of \(C\) are \(L^2\) on their fixed support, by their local exponents \(p_\alpha\ge2\). Multiplying these pointwise estimates by the coefficient norms proves \(\int_{\mathbb R}\|CF_t\|_2\,dt<\infty\). On bounded time intervals, \(F_t\) is continuous in \(H^m\), and \(C:H^m\to B\) is bounded. In fact \(t\mapsto CF_t\) is continuous and uniformly bounded in \(B\), since the free group preserves the \(H^m\) norm.

The common-domain difference quotient used in (15) gives
\(\partial_t(e^{itK}F_t)=i e^{itK}CF_t\).
The norm integral and the integrable bound above construct the two limits
\[
 W_{K,\sigma}f=\lim_{t\to\sigma\infty}e^{itK}e^{-itp(D)}f.
\]
They are isometries and extend from these dense packets to all of \(L^2\). Packet density follows by smooth approximation off the null zero set of a nonzero polynomial derivative, with the compact cutoff argument already proved in Section 1 of *Modified waves and the direction of escape*. Time translation of the defining limits gives group intertwining; the spectral-intertwining proof in [Wave operators and modified phases](wave-operators-and-modified-phases.md), Proposition 2.1, then gives all Borel energy projections. Every level set of the nonconstant polynomial \(p\) is null by the polynomial-zero-set proof identified at the start of this section. Hence \(p^{-1}(\Sigma_K)\) is null and \(\operatorname{ran}W_{K,\sigma}\subset E_K(\Omega_K)L^2\).

<a id="compact-force-damping"></a>

The damped-integral method is Hörmander [H2, Theorem 14.6.5 and its proof]. Chapter XIV assumes the compact perturbation map in Definition 14.4.1. Here the preceding radiation argument proves the required inverse for the full compact-force class, and the comparison below checks the integral and spectral hypotheses for that class.

### The matching-sign comparison

For the same packet and \(\varepsilon>0\), define the damped vector
\[
 y_{\sigma,\varepsilon}
   =f+\sigma\int_{\sigma t>0}i e^{-\varepsilon|t|}
                             e^{itK}CF_t\,dt.
\]
The undamped integrable \(L^2\) majorant makes \(y_{\sigma,\varepsilon}\to W_{K,\sigma}f\). The scalar integrals
\[
 i\int_0^\infty e^{-\varepsilon t}e^{-it a}\,dt=(a-i\varepsilon)^{-1},
 \qquad
 -i\int_{-\infty}^0e^{\varepsilon t}e^{-it a}\,dt=(a+i\varepsilon)^{-1}
\]
give the exact \(B\)-valued identity
\[
 \sigma\int_{\sigma t>0}i e^{-\varepsilon|t|}e^{it\lambda}CF_t\,dt
        =CR_0(\lambda+\sigma i\varepsilon)f.
\]
To justify applying \(C\), first take the integral in \(H^m\); the free orbit has a constant \(H^m\) norm, so damping makes it norm integrable. Fourier transformation evaluates it as the free resolvent. The bounded map \(C:H^m\to B\) commutes with this integral. This argument includes every order-\(m\) term.

<a id="compact-force-comparison"></a>

Apply \(J_{K,\sigma}\) to the damped vector, and use its group intertwining. On a compact good energy interval the continuous path \(CF_t\) is uniformly bounded in \(B\); \(A_\sigma(\lambda)\) and the canonical trace have common bounds. Their trace integrand is therefore bounded in shell \(L^2\) by \(C e^{-\varepsilon|t|}\). The path \((\lambda,t)\mapsto A_\sigma(\lambda)CF_t\) is jointly continuous in \(B\): split an increment into \(A_\sigma(\lambda)(CF_t-CF_{t_0})\) and \((A_\sigma(\lambda)-A_\sigma(\lambda_0))CF_{t_0}\), and use the common operator bound and strong continuity on the fixed vector. The [joint parameter-partition construction](asymptotic-completeness-for-short-range-operators.md#completeness-joint-assembly) therefore gives a jointly measurable representative. Coarea and Cauchy–Schwarz on each compact energy-coordinate patch make its absolute integral in \((t,\xi)\) finite. Scalar Fubini identifies its time integral with the Hilbert integral: for a test \(q\in L^2\) the absolute paired integral is bounded by \(\|q\|_2\int\|F(t)\|_2dt\); truncated tests \(q=h1_{\{|h|\le N\}}\), followed by monotone convergence, show that the scalar time integral \(h\) belongs to \(L^2\) with this same norm bound. This is also the complete scalar-interchange proof in Section 2 of the earlier short-range comparison lesson, with all its actual hypotheses now verified for \(C\).

Consequently, for almost every energy and shell point, the transform of the damped vector has representative
\[
 T_\lambda A_\sigma(\lambda)
       [f+CR_0(\lambda+\sigma i\varepsilon)f].
\]
The free strong weighted graph limit, followed by the compactly supported coefficient-product map, gives
\(CR_0(\lambda+\sigma i\varepsilon)f\to CR_{0,\sigma}(\lambda)f\) in \(B\). The proved inverse identity makes the displayed limit \(T_\lambda f\). Uniform bounds on every compact good energy interval, coarea and dominated convergence prove convergence in local momentum \(L^2\). The global \(L^2\) limit is \(J_{K,\sigma}W_{K,\sigma}f\), so a countable compact exhaustion and the null set \(p^{-1}(\Sigma_K)\) give
\[
 J_{K,\sigma}W_{K,\sigma}f=\widehat f.
\]
The dense packet class and the common operator bounds extend this identity to every \(f\in L^2\).

<a id="compact-force-onto"></a>

Finally, \(J_{K,\sigma}\) is isometric on \(E_K(\Omega_K)L^2\), and the wave range lies there. For \(v=E_K(\Omega_K)v\), put \(f=\mathcal F^{-1}J_{K,\sigma}v\). The matching identity gives \(J_{K,\sigma}W_{K,\sigma}f=J_{K,\sigma}v\); injectivity on that subspace gives \(W_{K,\sigma}f=v\). Thus both maps are onto their stated spaces, and \(W_{K,\sigma}=J_{K,\sigma}^*\mathcal F\). Their band restrictions satisfy the same identities with the corresponding energy projections. In particular all stationary and wave comparison inputs required for the actual cutoffs \(H_j\) have now been proved, without imposing a lower-order condition on their compact perturbations.

## 15. From local amplitudes to the long-range spectral transform

The two approximation theorems and the full compact-force comparison provide the inputs for passing from bounded-support forces to the long-range stationary transform. The next lesson proves chart compatibility, flux normalization, the band preimage and the assembly over all good energies.

## References

- [Y] Dmitri Yafaev, *Lectures on scattering theory*, arXiv:math/0403213v1, 12 March 2004; prepared by Andrew Hassell from the 2001 ANU lectures. [Free version read](https://arxiv.org/pdf/math/0403213v1). Sections 2–3 provide short-range and long-range Schrödinger context; the full differential-coefficient comparison is proved above.
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, 2014. [Freely readable author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf). Theorem 5.1 gives the self-adjoint unitary evolution and generator domain; Lemma 12.3 gives the Cook-integral criterion. The local proofs include the domains and full coefficient class used here.
- [O] Sung-Jin Oh, *Lecture Notes for Math 222A*, University of California, Berkeley, Fall 2023. [Free lecture notes](https://math.berkeley.edu/~sjoh/pdfs/notes-math222a.pdf), Section 2.4.1 on Hamilton characteristics.
- [H76] Lars Hörmander, *The existence of wave operators in scattering theory*, Mathematische Zeitschrift **146** (1976), 69–91. [Freely accessible journal scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf). Theorems 3.9–3.10 assume \(\det P_0''\not\equiv0\); their wave-existence and phase-comparison conclusions are distinct from Theorems 1.1–1.2 here.

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, §30.5, the cutoff comparison and (30.5.37), p. 326; (30.5.44) and its proof, pp. 328–329. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).

[H2] Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, reprint of the 1983 edition, Springer, 2005, Definition 14.4.1, p. 243; Theorems 14.6.4–14.6.5 and their proofs, pp. 257–259. ISBN 978-3-540-26964-9. [Edition information](https://doi.org/10.1007/978-3-540-26964-9).
