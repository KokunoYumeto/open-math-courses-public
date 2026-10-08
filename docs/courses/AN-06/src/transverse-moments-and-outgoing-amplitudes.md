# Transverse moments and outgoing amplitudes


*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Why begin with a transverse moment if the final amplitude is unweighted?** A transverse moment controls the error caused by removing the phase and makes the amplitude Cauchy for a dense class of data. The uniform energy bound then extends that limit to arbitrary square-integrable initial data and integrable forcing. Density without a common bound would not justify passing the limiting amplitude to all states.


A long-range phase follows the motion of an outgoing packet. After removing that phase, its transverse position stays controlled and the packet converges in a fixed Hilbert space. We prove this first for data with a transverse moment. A uniform energy estimate then extends the amplitude limit to arbitrary square-integrable initial data and integrable forcing.


Read [Commuting coordinates for long-range evolution](commuting-coordinates-for-long-range-evolution.md), especially the [full factor estimates](commuting-coordinates-for-long-range-evolution.md#commuting-factor-estimates), [individual defects](commuting-coordinates-for-long-range-evolution.md#commuting-defects), [coordinate commutators](commuting-coordinates-for-long-range-evolution.md#commuting-moments) and [local norm continuity](commuting-coordinates-for-long-range-evolution.md#commuting-continuity). Its [integrable-defect evolution theorem](commuting-coordinates-for-long-range-evolution.md#commuting-evolution) supplies the uniform energy bound in both time directions. [Energy-shell factors and outgoing equations](energy-shell-factors-and-outgoing-equations.md#energy-shell-application) constructs the outgoing equation; [Frequency cutoffs and compact scattering remainders](frequency-cutoffs-and-compact-scattering-remainders.md#cutoff-forcing) proves continuity of its forcing. We use the [Bochner integral](../providers/analysis/hilbert-valued-integration.md#bochner-integral), [product rule](../providers/analysis/hilbert-valued-integration.md#operator-products), [variation formula](../providers/analysis/hilbert-valued-integration.md#variation-of-constants) and [integrable-tail argument](../providers/analysis/hilbert-valued-integration.md#integrable-tails) from *Hilbert-valued integration*. Teschl [O], Sections 2.3–2.4, discusses Picard iteration and integrating factors. Yafaev [Y] and Teschl [T] discuss scattering theory; Hörmander's Theorem 3.9 [H] treats modified wave operators with stronger coefficient and Hessian hypotheses.


<a id="amplitude-setup"></a>
We use \(D=-i\partial\), \(\mathcal H=L^2(\mathbb R^d_z)\), and \(s\ge s_0\ge1\). Norms without subscripts are \(\mathcal H\) norms. Fix \(0<\delta<1/3\). Write


\[

 \begin{aligned}

 A_0&=D_s-G_s(s,D_z),\\

 A_j&=z_j+G_{\eta_j}(s,D_z),\\

 \mathcal L&=A_0+\sum_j\mathcal B_jA_j=D_s-M(s).

 \end{aligned}

 \tag{1}

\]


The real compact-frequency phase and factors are those of the preceding lesson. Its [phase-domain identity](commuting-coordinates-for-long-range-evolution.md#commuting-coordinates) holds on the full coordinate domain in both directions. In particular \(M\) is uniformly bounded and locally norm continuous, and


\[

 \begin{gathered}

 \|M-M^*\|+\sum_j\|\mathcal B_j\|

 +\sum_{j,k}\|\mathcal R_{jk}\|\\

 \le Cs^{-1-\delta},\\

 \mathcal R_{jk}=[A_j,\mathcal B_k],\\

 \|[z_j,M]\|\le C,\\

 \|G_\eta(s,D_z)\|\le Cs,\\

 \|G_{s\eta}(s,D_z)\|\le C.

 \end{gathered}

 \tag{2}

\]


The coordinate commutators are locally norm continuous. The \(A_j\) commute with one another and with \(A_0\). All sums and vector norms below have the finite transverse dimension \(d\).


## 1. Propagating a transverse moment


Put


\[

 \begin{gathered}

 \mathcal H_1=\{v\in\mathcal H:z_jv\in\mathcal H,\ 1\le j\le d\},\\

 \|v\|_{\mathcal H_1}=\|v\|+\sum_j\|z_jv\|,\\

 W(v)=\||z|v\|.

 \end{gathered}

 \tag{3}

\]


<a id="amplitude-moment-space"></a>
Coordinate multiplication is closed: convergence of \(v_n\) and \(z_jv_n\) in \(\mathcal H\), tested against compactly supported smooth functions, identifies the latter limit as \(z_jv\). This also proves completeness of (3). More precisely, the graph map \(Jv=(v,z_1v,\ldots,z_dv)\) has closed image in \(\mathcal H^{d+1}\). The induced inner product \((u,v)_1=(u,v)+\sum_j(z_ju,z_jv)\) makes \(\mathcal H_1\) a Hilbert space. Its norm is \((\|v\|^2+W(v)^2)^{1/2}\), which is bounded above by the norm in (3) and bounds that norm divided by \(\sqrt{d+1}\). Thus the Hilbert-valued integral and product rules apply in this space as well; the equivalent norm (3) has the same integrable functions and locally absolutely continuous curves.


<a id="amplitude-density"></a>
Smooth compactly supported functions are dense in \(\mathcal H_1\). The needed [unweighted density](../providers/analysis/euclidean-approximation-and-convolution.md#finite-p-density), [convolution inequality](../providers/analysis/euclidean-approximation-and-convolution.md#holder-and-young) and [smooth approximate identities](../providers/analysis/euclidean-approximation-and-convolution.md#mollification) are proved in *Euclidean approximation and convolution*. First apply a physical cutoff tending to one; both ordinary and coordinate-weighted tails tend to zero by dominated convergence. For a smooth approximate identity \(\rho_\varepsilon\),


\[

 z_j(\rho_\varepsilon*v)

   =\rho_\varepsilon*(z_jv)+(z_j\rho_\varepsilon)*v.

 \tag{4}

\]


The first term converges to \(z_jv\), while the second tends to zero because

\(\|z_j\rho_\varepsilon\|_{L^1}=O(\varepsilon)\). Apply this after the cutoff. It proves the density claim without losing the moment.


<a id="amplitude-domain"></a>
Let \(K_j=[z_j,M]\). On Schwartz tests,


\[

 z_jMv=M(z_jv)+K_jv.

 \tag{5}

\]


Approximate in \(\mathcal H_1\). Boundedness of \(M\) and \(K_j\) makes both terms on the right converge in \(\mathcal H\); closedness of coordinate multiplication then proves (5) on the entire domain. In particular
\[
 \|Mu\|_{\mathcal H_1}
 \le \|M\|\|u\|_{\mathcal H_1}
            +\sum_j\|K_j\|\|u\|.
\]
The same inequality for \(M(s)-M(t)\), with commutators \(K_j(s)-K_j(t)\), proves local norm continuity on \(\mathcal H_1\). Thus the norm Picard construction works on this complete space, even though the uniform energy estimate will be taken in \(\mathcal H\).


<a id="amplitude-moment-estimate"></a>
This moment estimate is Hörmander [H4, Lemma 30.5.8].

**Theorem 1.1 (the full moment estimate).** If \(v_0\in\mathcal H_1\) and \(h\in L^1_{\mathrm{loc}}(ds;\mathcal H_1)\), the unique solution of

\(\mathcal Lv=h,\ v(s_0)=v_0\), takes values in \(\mathcal H_1\), is locally absolutely continuous there, and satisfies


\[

 \begin{aligned}

 W(v(s))\le {}&CW(v_0)+C(s-s_0)\|v_0\|\\

 &+C\int_{s_0}^s\|\Omega_{s,t}h(t)\|\,dt.

 \end{aligned}

 \tag{6}

\]


Here \(\Omega_{s,t}(z)=(|z|^2+(s-t)^2)^{1/2}\). The constant is independent of \(s\).


**Proof.** On each finite interval, apply the factorial Picard construction of the preceding lesson in the \(\mathcal H_1\) norm. Forcing in \(L^1_{\mathrm{loc}}(\mathcal H_1)\) gives a locally absolutely continuous solution there by its Bochner variation integral. After inclusion in \(\mathcal H\), it solves the same equation and has the same initial value, so uniqueness identifies it with the original solution. Multiplication by \(z_j\) is bounded from \(\mathcal H_1\) to \(\mathcal H\); it therefore commutes with the Bochner derivative. Formula (5) gives, for \(Y_j=z_jv\),


\[

 (D_s-M)Y_j=z_jh+K_jv.

 \tag{7}

\]


The propagator of \(D_s-M\) has norm at most one fixed \(C\) in both time directions, because the adjoint defect in (2) is integrable. On \(\mathcal H^d\), its diagonal action has the same bound. The vector operator \(u\mapsto(K_1u,\ldots,K_du)\) is bounded uniformly, with norm at most \((\sum_j\|K_j\|^2)^{1/2}\). Its variation formula applied to (7) therefore yields


\[

 \begin{aligned}

 W(v(s))\le {}&CW(v_0)\\

 &+C\int_{s_0}^s\bigl(W(h(t))+\|v(t)\|\bigr)\,dt.

 \end{aligned}

 \tag{8}

\]


The ordinary energy estimate and Fubini's theorem yield


\[

 \begin{aligned}

 \int_{s_0}^s\|v(t)\|\,dt\le {}&C(s-s_0)\|v_0\|\\

 &+C\int_{s_0}^s(s-t)\|h(t)\|\,dt.

 \end{aligned}

 \tag{9}

\]


For each fixed \(t\), the sum \(W(h(t))+(s-t)\|h(t)\|\) is at most \(\sqrt2\) times the square root of the sum of their squares. That square root is exactly the integrand norm in (6). Equations (8)–(9) prove the claim. \(\square\)


<a id="amplitude-coordinate-energy"></a>
## 2. Energy in the commuting coordinates


The preceding moment can grow linearly. The phase coordinates have a stronger estimate. Define


\[

 \begin{aligned}

 V(s)&=\left(\sum_j\|A_j(s)v(s)\|^2\right)^{1/2},\\

 H_A(s)&=\left(\sum_j\|A_j(s)h(s)\|^2\right)^{1/2}.

 \end{aligned}

 \tag{10}

\]


The coordinate estimate below is part of Hörmander [H4, Lemma 30.5.9 and its proof].

**Lemma 2.1.** For the weighted data of Theorem 1.1,


\[

 V(s)\le C\left(V(s_0)+\int_{s_0}^s H_A(t)\,dt\right).

 \tag{11}

\]


The corresponding homogeneous estimate holds backward with the same kind of uniform constant.


**Proof.** Set \(b_j(s)=G_{\eta_j}(s,D_z)\) and \(Y_j(s)=z_jv(s)+b_j(s)v(s)\). The first moment theorem makes \(z_jv\) locally absolutely continuous in \(\mathcal H\). The Fourier multiplier \(b_j\) is norm differentiable locally, with derivative \(G_{s\eta_j}(s,D_z)\), so the Bochner product rule makes \(Y_j=A_jv\) locally absolutely continuous as well.

For Schwartz tests the commuting identities give
\([\mathcal L,A_j]=-\sum_k[A_j,\mathcal B_k]A_k=-\sum_k\mathcal R_{jk}A_k\).
At each fixed time this is the spatial operator identity
\([A_j,M]-i b_j'=-\sum_k\mathcal R_{jk}A_k\).
Both sides are continuous from \(\mathcal H_1\) to \(\mathcal H\): \(M\) preserves \(\mathcal H_1\) by (5), each \(A_k\) maps \(\mathcal H_1\) continuously into \(\mathcal H\), and \(M,\mathcal R_{jk},b_j'\) are bounded on \(\mathcal H\). Graph-norm density therefore extends this identity to every vector in \(\mathcal H_1\). For the actual time-dependent solution, the Bochner product rule now gives
\((D_s-M)Y_j=A_jh+([A_j,M]-i b_j')v\) almost everywhere. Substitution gives the ordinary Hilbert-space equation


\[

 (D_s-M)(A_jv)+\sum_k\mathcal R_{jk}A_kv=A_jh.

 \tag{12}

\]


Its matrix generator on \(\mathcal H^d\) is


\[

 \begin{aligned}

 \mathbb M(s)={}&\operatorname{diag}(M(s),\ldots,M(s))\\

 &-(\mathcal R_{jk}(s))_{j,k}.

 \end{aligned}

 \tag{13}

\]


It is bounded and locally norm continuous. The norm of its adjoint defect is at most

\(\|M-M^*\|+2\|(\mathcal R_{jk})\|\le Cs^{-1-\delta}\).

For the homogeneous coordinate equation, the derivative of \(\|Y\|_{\mathcal H^d}^2\) is bounded in absolute value by this adjoint defect times \(\|Y\|^2\). The integrating-factor calculation of the preceding lesson therefore bounds its matrix propagator in both orientations by
\(\exp(C\int_{s_0}^{\infty}t^{-1-\delta}\,dt/2)\).
Its variation integral for the forcing vector \((A_jh)_j\) proves (11). No second spatial moment is used. \(\square\)


The finite-interval Picard construction also preserves \(\mathcal H_1\) for terminal data evolved backward. The matrix energy estimate just proved is uniform in that orientation too.

This proof controls the whole coordinate vector. It does not replace each individual commutator or adjoint estimate by an estimate for their sum.


<a id="amplitude-weighted"></a>
## 3. The amplitude for weighted data


Remove the phase by setting


\[

 w(s)=e^{-iG(s,D_z)}v(s).

 \tag{14}

\]


This multiplier is unitary. Its derivative and its coordinate identity are


\[

 \begin{aligned}

 w'(s)&=i e^{-iG(s,D_z)}A_0v(s),\\

 z_jw(s)&=e^{-iG(s,D_z)}A_j(s)v(s).

 \end{aligned}

 \tag{15}

\]


The weighted amplitude conclusion is Hörmander [H4, Lemma 30.5.9].

**Theorem 3.1.** Suppose \(v_0\in\mathcal H_1\) and


\[

 \int_{s_0}^{\infty}

       \big\|(1+(s^2+|z|^2)^{1/2})h(s,z)\big\|\,ds<\infty.

 \tag{16}

\]


Then \(w(s)\) converges strongly in \(\mathcal H\) to a limit \(v_\infty\in\mathcal H_1\). The convergence norm is the unweighted \(L^2\) norm; the first moment of the limit follows from the separate bound (19). If


\[

 M_A=V(s_0)+\int_{s_0}^{\infty}H_A(t)\,dt,

 \tag{17}

\]


then


\[

 \begin{aligned}

 \|A_0v(s)\|&\le\|h(s)\|+Cs^{-1-\delta}M_A,\\

 \|w(s)-v_\infty\|

     &\le\int_s^\infty\|h(t)\|\,dt

                            +\frac C\delta s^{-\delta}M_A.

 \end{aligned}

 \tag{18}

\]


Moreover,


\[

 \begin{aligned}

 \|(1+|z|)v_\infty\|\le {}&C\|(1+|z|)v_0\|\\

 &+C\int_{s_0}^{\infty}\|\Lambda_s h(s)\|\,ds.

 \end{aligned}

 \tag{19}

\]


Here \(\Lambda_s(z)=1+(s^2+|z|^2)^{1/2}\). Constants may depend on the fixed \(s_0\).


**Proof.** Condition (16) also gives the required local \(\mathcal H_1\)-valued integrability. Indeed the bounded multipliers \(z_j\mathbf1_{\{|z|\le R\}}\) applied to the strongly measurable forcing converge in \(\mathcal H\) to \(z_jh(s)\) for almost every \(s\). These coordinate maps are therefore strongly measurable. The closed graph map \(J\) identifies \(h\) as a strongly measurable \(\mathcal H_1\)-valued function, and its graph norm is locally integrable by (16). The bound \(\|G_\eta(s,D_z)\|\le Cs\) shows that

\(H_A(s)\le W(h(s))+Cs\|h(s)\|\). Thus (16) makes (17) finite. Lemma 2.1 gives \(V(s)\le CM_A\). The equation (1) now gives the first line of (18), using the integrable bounds on each \(\mathcal B_j\).


By (15), \(w'\) is integrable on the entire half-line. More explicitly, for \(t>s\),
\(w(t)-w(s)=i\int_s^t e^{-iG(q,D_z)}A_0v(q)\,dq\).
The bound on the norm of this integral tends to zero as \(s\to\infty\), uniformly in \(t>s\). Completeness gives a strong limit, and sending \(t\to\infty\) in that integral gives its error estimate. Integrating the first line of (18) proves the second, since
\(\int_s^\infty t^{-1-\delta}\,dt=s^{-\delta}/\delta\).


<a id="amplitude-limit-moment"></a>
The second identity in (15) gives \(W(w(s))=V(s)\le CM_A\). This moment passes to the strong limit using bounded truncations: multiplication by \(\min(|z|,R)\) has norm at most \(R\), so
\(\|\min(|z|,R)v_\infty\|=\lim_{s\to\infty}\|\min(|z|,R)w(s)\|\le CM_A\).
Monotone convergence as \(R\to\infty\) gives \(W(v_\infty)\le CM_A\) and \(v_\infty\in\mathcal H_1\). Finally the ordinary energy estimate bounds
\(\|v_\infty\|\) by \(C(\|v_0\|+\int\|h\|)\), while

\(V(s_0)\le W(v_0)+Cs_0\|v_0\|\). Combining these estimates proves (19). \(\square\)


<a id="amplitude-fatou-moment"></a>

There is also a direct Fatou proof of the first-moment conclusion. Strong convergence permits an increasing sequence \(s_k\geq\max(s_0,k)\) such that \(\|w(s_k)-v_\infty\|\leq2^{-k}\). Apply [monotone convergence](../providers/analysis/finite-derivative-l2.md#monotone-integral-and-convergence) to the finite partial sums of the nonnegative squared differences. It gives
\[
 \int_{\mathbb R^d}\sum_{k=1}^{\infty}|w(s_k,z)-v_\infty(z)|^2\,dz
 =\sum_{k=1}^{\infty}\|w(s_k)-v_\infty\|^2
 \leq\sum_{k=1}^{\infty}4^{-k}<\infty.
\]
Consequently the sum is finite almost everywhere, so its terms tend to zero there. For these representatives, \(w(s_k,z)\to v_\infty(z)\) almost everywhere. [Fatou's inequality](../providers/analysis/finite-derivative-l2.md#monotone-integral-and-convergence), applied to \(|z|^2|w(s_k,z)|^2\), now yields
\[
 W(v_\infty)^2
 \leq\liminf_{k\to\infty}W(w(s_k))^2
 \leq C^2M_A^2.
\]
Combining this with the same unweighted energy bound and initial-coordinate estimate gives (19). This argument, like the truncation proof, establishes the moment of the limit without asserting convergence in the moment norm.

<a id="amplitude-all-data"></a>
## 4. Every integrable forcing has an amplitude


The weighted hypothesis is useful for a rate and a moment, but it is not needed for existence of the limit.


Hörmander [H4, the paragraph after Lemma 30.5.9] extends the amplitude to arbitrary square-integrable data and integrable forcing by the approximation argument written out below.

**Theorem 4.1.** For every \(v_0\in\mathcal H\) and \(h\in L^1(ds;\mathcal H)\), the solution of \(\mathcal Lv=h\) has a strong phase-corrected amplitude:


\[

 \begin{gathered}

 v_\infty=\lim_{s\to\infty}e^{-iG(s,D_z)}v(s),\\

 \|v_\infty\|\le C\left(\|v_0\|+

                         \int_{s_0}^{\infty}\|h(t)\|\,dt\right).

 \end{gathered}

 \tag{20}

\]


The amplitude depends boundedly and linearly on the pair \((v_0,h)\).


**Proof.** Approximate \(v_0\) in \(\mathcal H\) by smooth compactly supported data \(v_0^k\). Approximate \(h\) in \(L^1(ds;\mathcal H)\) by forcings \(h^k\) satisfying (16). Such forcings are dense: truncate the integrable time tail, approximate on the remaining interval by finitely many simple Hilbert-valued functions, and approximate their finitely many values in \(\mathcal H\) by smooth compactly supported functions. The resulting time supports are bounded, and all spatial moments are finite.


Let \(v^k,w^k,a_k\) be the corresponding solutions, phase corrections and amplitudes. The uniform energy estimate gives


\[

 \begin{gathered}

 \sup_{s\ge s_0}\|w^k(s)-w(s)\|\\

 \le C\left(\|v_0^k-v_0\|+

                      \|h^k-h\|_{L^1(ds;\mathcal H)}\right).

 \end{gathered}

 \tag{21}

\]


Apply the same estimate to two approximations and let \(s\to\infty\). Their amplitudes \(a_k\) form a Cauchy sequence; write its limit as \(a\). For fixed \(k\),

\(\|w(s)-a\|\) is bounded by the uniform error in (21), the error \(\|w^k(s)-a_k\|\), and \(\|a_k-a\|\). First make \(k\) large, then make \(s\) large. This proves (20), with \(v_\infty=a\). Taking limits in the ordinary energy estimate proves its norm bound. Linearity and the difference estimate follow from uniqueness of the evolution. \(\square\)


This argument gives existence for all \(L^1\) forcing. It asserts a moment and the explicit rate (18) only when the weighted assumptions hold.


<a id="amplitude-outgoing-application"></a>
For an outgoing frequency-localized solution, the preceding lessons give

\(\mathcal Lv=g+\mathcal Tv\), where \(g\in L^1(ds;\mathcal H)\),

\(\|\mathcal T(s)\|\le Cs^{-1-\delta}\), and \(v\) has bounded slice norm.

Thus Theorem 4.1 applies to its actual right side. The limit is independent of changes to the phase extension outside its Fourier support, because the multiplier acting on that solution is unchanged.


When \(d=0\), the coordinate vectors are empty and the moments vanish. The equation is \(A_0v=h\); (15) directly integrates it and gives (20). All formulas above retain this interpretation.


<a id="amplitude-stability"></a>
## 5. Stability under approximation


To pass from truncated coefficients to a full force, convergence on each bounded time interval must be combined with a uniform estimate at infinity. The following statement specifies both ingredients.


The proof below makes explicit the uniform-tail comparison underlying Hörmander [H4, (30.5.37)]. We state and prove the parameter hypotheses for this family of systems.

**Theorem 5.1.** Let systems indexed by \(n\) and a limiting system have the structure (1)–(2), with the same \(s_0,\delta\) and common constants, including the bound for the individual adjoint defects used to obtain the uniform evolution estimate. Suppose


\[

 \begin{gathered}

 \sup_{s_0\le s\le S}\|M_n(s)-M(s)\|\longrightarrow0,\\

 \|G_n(S,D_z)-G(S,D_z)\|\longrightarrow0,\\

 v_{0,n}\longrightarrow v_0,\\

 h_n\longrightarrow h\quad\text{in }L^1(ds;\mathcal H).

 \end{gathered}

 \tag{22}

\]


The first two convergence conditions hold for every finite or fixed \(S\), respectively. Then the phase-corrected amplitudes satisfy \(v_{\infty,n}\to v_\infty\) strongly.


**Proof.** Choose one weighted approximation \((u^k,f^k)\) to the limiting pair \((v_0,h)\), as in Theorem 4.1. In each system solve with this same pair, and call its amplitude \(a_n^k\); call the limiting-system amplitude \(a^k\). The uniform difference estimate gives


\[

 \begin{gathered}

 \|v_{\infty,n}-a_n^k\|\\

 \le C\bigl(\|v_{0,n}-u^k\|+\|h_n-f^k\|_{L^1}\bigr),\\

 \|v_\infty-a^k\|\\

 \le C\bigl(\|v_0-u^k\|+\|h-f^k\|_{L^1}\bigr).

 \end{gathered}

 \tag{23}

\]


For fixed \(k\), the canonical-coordinate quantities \(M_{A,n}^k\) in (17) have a common finite bound \(C_k\). This follows from

\(\|G_{n,\eta}(s,D_z)\|\le Cs\) and the fixed weighted data; it does not require convergence of their moments. Equation (18) therefore gives


\[

 \|w_n^k(S)-a_n^k\|

       \le\int_S^\infty\|f^k(t)\|\,dt+C_k S^{-\delta},

 \tag{24}

\]


uniformly in \(n\), with the same estimate for the limiting system.


At fixed \(S\), Duhamel's formula for the difference of the two evolutions gives


\[

 \begin{gathered}

 \sup_{s_0\le s\le S}\|v_n^k(s)-v^k(s)\|\\

 \le C\int_{s_0}^S\|(M_n(t)-M(t))v^k(t)\|\,dt\\

 \longrightarrow0.

 \end{gathered}

 \tag{25}

\]


All phases in (22) are real Fourier multipliers, so the elementary inequality

\(|e^{-ia}-e^{-ib}|\le|a-b|\) gives convergence of their exponentials in operator norm at \(S\). Thus \(w_n^k(S)\to w^k(S)\). Choose \(k\) to make the limiting data errors small, then \(S\) to make (24) small, then \(n\) to make (25), the phase error and the data errors small. The triangle inequality proves the asserted amplitude convergence. \(\square\)


<a id="amplitude-uniform-stability"></a>
There is a useful uniform version. Suppose an additional parameter \(p\) ranges over a compact set, the convergence in (22) is uniform in \(p\), all structural bounds are common, and the limiting data pair is norm continuous into
\(\mathcal D=\mathcal H\times L^1(ds;\mathcal H)\), with norm \(\|(u,f)\|_{\mathcal D}=\|u\|+\|f\|_{L^1}\).
Its image \(K\) is compact. Given \(\varepsilon>0\), density and compactness give finitely many weighted data pairs \(d_1,\ldots,d_m\), with bounded time support, whose \(\varepsilon\)-balls cover \(K\). The amplitude operators for every system have one common norm bound on \(\mathcal D\). Thus (23) makes the two errors between actual data and the chosen center at most \(C\varepsilon\), plus the uniformly vanishing data error from (22).

There are only finitely many centers. Their weighted bounds in (17) have a common finite maximum independent of \(n,p\), so (24) gives one terminal time \(S\) at which every center has amplitude error at most \(\varepsilon\). For this fixed \(S\), (25) is uniform in \(p\): common energy bounds control the finitely many center solutions, and the generator difference tends to zero uniformly. The phase difference at \(S\) is uniform by (22). Choose the cover first, then this one \(S\), then \(n\). Taking the supremum over \(p\) and letting \(\varepsilon\to0\) proves uniform amplitude convergence. The original compact family needs only its \(\mathcal D\) norm; its members need not have a first moment.


### Use the conclusion


Write the three terms in the approximation comparison: data error, fixed-data evolution error and limiting amplitude error. Check where the common energy constant is used, then retain stability for every integrable forcing.


<a id="amplitude-solutions"></a>
## 6. Exercises with complete solutions


**Exercise 1 — Foundation: an exactly integrable forcing.** Take \(M=G=0\) and \(h(s)=e^{-(s-s_0)}f\), with \(v_0,f\in\mathcal H\). Find \(v(s)\), its amplitude, and the exact norm of its amplitude error.


**Solution 1.** Since \(D_sv=h\), we have \(v'=ih\). Direct integration gives


\[

 \begin{aligned}

 v(s)&=v_0+i(1-e^{-(s-s_0)})f,\\

 v_\infty&=v_0+if,\\

 \|v(s)-v_\infty\|&=e^{-(s-s_0)}\|f\|.

 \end{aligned}

 \tag{26}

\]


Here the phase correction is the identity. If \(v_0,f\in\mathcal H_1\), multiplication by each coordinate gives the same formulas in the weighted space. With arbitrary \(f\in\mathcal H\), Theorem 4.1 still applies.


**Exercise 2 — Intermediate: a limit with no first moment.** For \(d\ge1\), \(s_0=1\), set

\(f(z)=(1+|z|^2)^{-(d+1)/4}\), \(v_0=0\), \(M=G=0\), and \(h(s)=(1+s)^{-2}f\). Check the \(L^1(ds;\mathcal H)\) hypothesis, compute the amplitude, and show that it has no transverse first moment.


**Solution 2.** At large radius the radial integral for \(\|f\|^2\) has integrand comparable to

\(r^{d-1}r^{-(d+1)}=r^{-2}\), which is integrable. The origin is harmless. The radial integral for \(\||z|f\|^2\) instead has integrand comparable to \(1\), so it diverges. Thus \(f\in\mathcal H\setminus\mathcal H_1\).


The forcing norm has finite integral \(\|f\|\int_1^\infty(1+s)^{-2}\,ds=\|f\|/2\). Its solution and amplitude are


\[

 v(s)=i\left(\frac12-\frac1{1+s}\right)f,\qquad

 v_\infty=\frac i2 f.

 \tag{27}

\]


The limit has no first moment. The stronger time-weighted integral also fails: \(s(1+s)^{-2}\) has a logarithmically divergent integral. This example requires the density theorem rather than the weighted conclusion (19).


**Exercise 3 — Intermediate: reading the two tail rates.** Under Theorem 3.1 assume in addition \(\|h(s)\|\le C_hs^{-1-\beta}\), with \(\beta>0\). Give the amplitude error bound. Evaluate its slower exponent for \(\delta=1/5,\ \beta=3/2\), and explain what happens when \(\beta=\delta\).


**Solution 3.** Integrating each term of (18) separately gives


\[

 \|w(s)-v_\infty\|

       \le\frac{C_h}{\beta}s^{-\beta}

                  +\frac{CM_A}{\delta}s^{-\delta}.

 \tag{28}

\]


The slower exponent in the stated example is \(1/5\). This is an upper bound; a particular solution can converge faster. If \(\beta=\delta\), the two coefficients add in front of \(s^{-\delta}\). There is no logarithm, since both integrations have exponent strictly below \(-1\); no convolution of the two tails was used.


**Exercise 4 — Advanced: a pulse escaping to late time.** On \(\mathcal H=\mathbb C\), choose real smooth \(\rho\) supported in \((1,2)\) with \(\int\rho=1\). Take \(s_0=1,\ v_0=1,\ h=G=0\), and \(M_n(s)=n^{-1}\rho(s/n)\). Show that the generators converge locally to zero and all evolutions have norm one, but their amplitudes do not converge to that of the limiting zero generator. Identify the missing uniform hypothesis of Theorem 5.1. These are general scalar evolutions, not the full factored systems of (1).


**Solution 4.** For each fixed \(S\), \(M_n=0\) on \([1,S]\) once \(n>S\), so local operator convergence is exact. The real generators give


\[

 v_n(s)=\exp\left(i\int_1^s n^{-1}\rho(t/n)\,dt\right).

 \tag{29}

\]


Their norms are one and their adjoint defects are zero. For \(s\ge2n\), the integral equals one, hence \(v_{\infty,n}=e^{i}\). The limiting zero generator has constant solution and amplitude \(1\).


The uniform bound on the phase-corrected tail in (24) is missing. At a point \(s=nu\) with \(\rho(u)\ne0\), a bound

\(|M_n(s)|\le Cs^{-1-\delta}\) would require

\(C\ge |\rho(u)|u^{1+\delta}n^\delta\), which is impossible with one \(C\). Thus local convergence and a uniform energy bound alone cannot justify a limit at infinity.


**Exercise 5 — Advanced: the local homogeneous amplitude map is invertible.** With \(h=0\), define \(Fv_0=v_\infty\) by Theorem 4.1. Prove that \(F:\mathcal H\to\mathcal H\) is a bounded isomorphism. Use backward evolution from the terminal value \(e^{iG(t,D_z)}a\), initially for \(a\in\mathcal H_1\).


**Solution 5.** The propagator and its inverse have common bound \(C\), so

\(\|U(s,s_0)v_0\|\ge C^{-1}\|v_0\|\). Phase multiplication is unitary; strong convergence therefore gives

\(\|Fv_0\|\ge C^{-1}\|v_0\|\). Together with (20), this proves boundedness, injectivity and closed range.


Fix \(a\in\mathcal H_1\). For terminal time \(t\), put

\(v^t(t)=e^{iG(t,D_z)}a\) and evolve backward. Formula (15) gives

\(A_j(t)v^t(t)=e^{iG(t,D_z)}z_ja\).

Lemma 2.1 in the backward orientation bounds its whole coordinate vector by \(CW(a)\) at all earlier times. The homogeneous equation and (15) consequently give


\[

 \begin{gathered}

 \|e^{-iG(s,D_z)}v^t(s)-a\|\le Cs^{-\delta}W(a),\\

 s_0\le s\le t.

 \end{gathered}

 \tag{30}

\]


Let \(u_t=v^t(s_0)\). For \(t_2>t_1\), apply (30) to \(v^{t_2}\) at \(t_1\). Comparing its value there with the terminal value of \(v^{t_1}\), and evolving their difference backward, gives

\(\|u_{t_2}-u_{t_1}\|\le Ct_1^{-\delta}W(a)\). Thus \(u_t\) is Cauchy. Write its limit as \(u\); the terminal norm and the backward energy estimate give \(\|u\|\le C\|a\|\).


At each fixed \(s\), the forward solutions with initial data \(u_t\) converge to that with data \(u\). Passing to the limit in (30) shows that its phase-corrected solution tends to \(a\). Hence \(Fu=a\). The range contains the dense space \(\mathcal H_1\) and is closed, so it is all of \(\mathcal H\). The inverse bound follows from the lower bound above.


For \(d=0\), the same argument has no coordinates; directly \(Fv_0=e^{-iG(s_0)}v_0\). This local transverse isomorphism concerns the first-order channel equation. Establishing asymptotic completeness for the original global differential operator also requires its spectral and channel assembly.


## References


- [Y] Dmitri Yafaev, *Lectures on scattering theory*, lecture notes prepared by Andrew Hassell, arXiv:math/0403213v1, 12 March 2004. [Free lecture paper](https://arxiv.org/pdf/math/0403213v1).
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, freely readable author edition of the second edition, 2014, Chapter 12. [Free author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
- [O] Gerald Teschl, *Ordinary Differential Equations and Dynamical Systems*, author's preliminary version, 2012. Theorem 2.5 and Corollary 2.6, pp. 40–41, give Picard iteration; Lemma 2.7, pp. 42–43, gives the integrating-factor estimate. [Author's online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
- [H] Lars Hörmander, “The existence of wave operators in scattering theory,” *Mathematische Zeitschrift* **146** (1976), 69–91. [Digitized paper](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf).

[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, Lemma 30.5.8 and proof, p. 324; Lemma 30.5.9 and proof, pp. 324–325; the extension following that lemma and (30.5.37), p. 326. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
