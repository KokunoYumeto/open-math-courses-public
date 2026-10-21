# Physical derivative bounds and realization of the correction fields

The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md). This note derives the passage from the actual finite correction cycle to its physical summation. The actual leading profile and complete base field are supplied by [V0–V7](shear-realization-audit.md) and [Z0–Z8](base-field-realization-audit.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).

Source: OpenAI, *Finite Time Blowup for Navier–Stokes*, original [PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), SHA256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. The source passages are on original pages 15–16, 57–59, 63–66, 74, 112–116 and 138. Principal locators are Theorem 3.1, Lemma 5.4, (6.2)–(6.12), (7.2)–(7.4), Lemma 9.8, Proposition 9.9 and Lemma A.6.

The complete local suppliers are [the cycle K0–K8](correction-cycle-audit.md), [source closure S1–S5](source-containment-audit.md), [pulse P1–P8](pulse-inverse-audit.md), [wave interactions W1–W8](wave-interaction-audit.md), [stress C1–C9](stress-covariance-audit.md), [temporal means T1–T4](temporal-mean-correction-audit.md), [five-profile means M1–M8](mean-moment-correction-audit.md), and [radial primitives R1–R8](radial-primitive-audit/src/radial-primitives-and-compact-mean-corrections.md). The physical summation proof is also retained in the previously delivered [N6.1, S1–S5](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/NS-BLOWUP/src/summing-the-correction-fields.md). The receiving data and summation argument are given below.

## L0. The actual potential and pressure increments

Retain \(0<h<1/100\), \(A=1/2+h\), \(D=1/2-h\), \(Q=2^{-\ell}\), \(\varepsilon=Q^h\), \(S_*=\ell^2\), \(\kappa_s=1/100000\), and the original stage orders
\[
\sigma_j=\tfrac15+\tfrac j{10},\qquad B_j=\tfrac12+\sigma_j,
\qquad C_j^*=1+\sigma_j.
\tag{L0.1}
\]
K2 constructs the finite initialization. For \(j\ge1\), collect the actual physical wave-potential increments of the cycle from \(j-1\) to \(j\) in \(A_j^w\), its azimuthal-potential coefficients in \(\Psi_j\), and its direct azimuthal-velocity coefficients in \(b_j\). Original (9.15) is exactly
\[
\begin{gathered}
A_j=A_j^w+\Psi_je_\theta,\quad B_j^{\rm vec}=b_je_\theta,
\quad p_j=p^{[j]}-p^{[j-1]},\quad Z_j=(A_j,B_j^{\rm vec},p_j),\\
\Delta u_j=\operatorname{curl}A_j+B_j^{\rm vec}=u^{[j]}-u^{[j-1]},\qquad
(u^{[J]},p^{[J]})=U_0+\sum_{j=1}^J(\Delta u_j,p_j).
\end{gathered}
\tag{L0.2}
\]
The superscript on \(B_j^{\rm vec}\) only distinguishes the vector from the already defined exponent \(B_j\); it does not alter either object. Every wave potential retains the factor \(i n_\Phi\times(\psi t)/(km|n_\Phi|^2)\) before its physical rescaling. Every mean potential retains the compact primitive and its remainder. No curl term is discarded.

Linearity of the same \(\mathsf T_0\) and the fixed \(\rho\), with pressure reconstructed after every intermediate update, gives original (9.16):
\[
Q^{2A}p_j=p_w^{[j]}-p_w^{[j-1]}
+\mathsf T_0\bigl(g_r^{[j]}-g_r^{[j-1]}-\rho(\mathcal P^{[j]}-\mathcal P^{[j-1]})\bigr).
\tag{L0.3}
\]
Here the quantities on the right are the complete chart quantities. The intermediate pressure differences telescope because their old and new full radial sources telescope inside a fixed linear operator. The background pressure cancels between the two finite states. The physical pressure has not been replaced by the last pressure increment in a cycle.

For a physical tuple \(V\), \(|V|_m\) denotes the sum of the absolute values of all its Cartesian component derivatives of total space–time order at most \(m\), evaluated at the point. Constants may depend on \(j,m\); the power loss to be proved must not depend on \(j\).

## L1. Physical differentiation with every graph and phase factor

First use the source viscosity one. The exact extension-to-physical map is
\[
R=r/Q^{1/2},\quad Z=z/Q^D,\quad T=(1-t)/Q,\quad
Y_i=J_g^i(v_rr^{d_r}+v_tt),
\tag{L1.1}
\]
with the original matrix, eigenvectors and index of W1.3. They remain fixed within a chart. For a coefficient \(a(R,Z,T,Y_i)\), the physical derivative operators before evaluation are exactly
\[
\begin{split}
\partial_r^{\rm phys}&=Q^{-1/2}(\partial_R+M_i d_rR^{d_r-1}\mathcal L_i),\\
\partial_z^{\rm phys}&=Q^{-D}\partial_Z,\\
\partial_t^{\rm phys}&=-Q^{-1}\partial_T+T_g^iN_i,
\end{split}
\quad
M_i=\Lambda_g^iQ^{d_r/2},\quad T_g^i=Q^{-1-h}c_i.
\tag{L1.2}
\]
The floor inequalities give
\[
T_g^{-1}S_*^{-1}<c_i\le S_*^{-1},\qquad
\Lambda_g^{-1}\varepsilon^{-\kappa_s}S_*^{-\rho_g}<M_i
\le\varepsilon^{-\kappa_s}S_*^{-\rho_g}.
\tag{L1.3}
\]
Thus one radial derivative of a coefficient costs at most \(Q^{-1/2-h\kappa_s}\), one axial derivative \(Q^{-D}\), and one time derivative \(Q^{-1-h}\), with polynomial factors in \(S_*\). The shell has \(\sqrt{X_a}\le R\le2\sqrt{X_b}\). All derivatives of \(R^{d_r-1}\) and of \(R^{-1}\) are bounded there. Applying (L1.2) repeatedly and the finite product rule proves the same per-derivative bounds at every fixed order: when a derivative hits an operator coefficient, it contributes its ordinary radial cost \(Q^{-1/2}\), which is no greater than the allowed radial cost. No new factor tied to the construction stage occurs.

For Cartesian derivatives retain
\[
\partial_{x_1}=\cos\theta\,\partial_r-\sin\theta\,r^{-1}\partial_\theta,
\qquad
\partial_{x_2}=\sin\theta\,\partial_r+\cos\theta\,r^{-1}\partial_\theta.
\tag{L1.4}
\]
Derivatives of the cylindrical frame and of these coefficients cost \(r^{-1}=Q^{-1/2}R^{-1}\), with the exact frame identities \(\partial_\theta e_r=e_\theta\), \(\partial_\theta e_\theta=-e_r\). These terms are included by induction in (L1.4); they are not treated as constant frame vectors.

The scalar phase has a better spatial bound than a general torus-dependent coefficient. On each lifted rectangle, original (6.11)–(6.12) gives
\[
v=(\eta_g+r_0)/c_i,\quad L_s=2r_0/c_i,\qquad
\partial_x^{\rm phys}v=0,\quad \partial_t^{\rm phys}v=Q^{-1-h}.
\tag{L1.5}
\]
The time derivative is constant in that chart. The phase is the full original expression
\[
\Phi=p\theta+p_zZ/\varepsilon+x_0R-v(pF+p_zG),\qquad
k=\lceil\varepsilon^{-1/2}\rceil\le2Q^{-h/2}.
\tag{L1.6}
\]
Here \(F=V/R\), \(p,p_z,x_0\) are fixed label constants, and the original coefficient \(B_s^2=\lambda_0/[\varepsilon k^2(1+u_*^2)^{3/2}]\) is used. P1 proves uniform bounds on these constants. They, the rounded integer \(kp\), and the representative are not differentiated.

For spatial multi-index \(a\), time order \(b\), and \(|a|+b\ge1\), differentiating every summand of (L1.6) gives
\[
|\partial_x^a\partial_t^b\Phi|
\le C_{a,b}Q^{-|a|/2-b(1+h)}S_*^{P_{a,b}}.
\tag{L1.7}
\]
Indeed \(p\theta\) contributes only spatial derivatives bounded by powers of \(r^{-1}\); \(p_zZ/\varepsilon\) has its sole nonzero derivative \(p_zQ^{-D}\varepsilon^{-1}=p_zQ^{-1/2}\); and \(x_0R\) has only the stated spatial costs. In \(v(pF+p_zG)\), every spatial derivative hits a slow factor, while a time derivative may hit either that factor or the one constant first derivative of \(v\). The slow factors cost \(Q^{-1/2}\), \(Q^{-D}\), \(Q^{-1}\), and \(|v|\le L_s\le C S_*\). Their all-order slow bounds come from P1's actual base inputs. This proves (L1.7), including every term of its product rule.

Set the original two costs
\[
s_x=\tfrac12+\tfrac h2,\qquad s_t=1+\tfrac{3h}{2}.
\tag{L1.8}
\]
A derivative of \(e^{ikn\Phi}\), for any fixed nonzero harmonic integer \(n\), is a finite sum of products
\((ikn)^d e^{ikn\Phi}\prod_{v=1}^d\partial_x^{a_v}\partial_t^{b_v}\Phi\), where \(d\le |a|+b\) and the derivative indices sum to \((a,b)\). Equations (L1.6)–(L1.7) bound each product by
\[
C_{a,b,n}Q^{-|a|/2-b(1+h)-dh/2}S_*^P
\le C_{a,b,n}Q^{-|a|s_x-bs_t}S_*^P.
\tag{L1.9}
\]
This keeps the carrier frequency contribution; it is not a bound on the phase alone. Since \(s_x\ge1/2+h\kappa_s,D,1/2\) and \(s_t\ge1+h\), the same costs dominate all coefficient and frame derivatives in (L1.2)–(L1.4).

All weights \(\sqrt\zeta\delta^{-M}\) and \(\zeta\delta^{-M}\) are bounded on the closed shell for each fixed \(M\), with smooth zero extensions already proved in S2 and C4. To verify boundedness at an edge, set its logarithmic distance to \(s>0\); the factor is bounded by a constant times \(s^{-M}\exp(-c/s^2)\), which tends to zero because the exponential series dominates any fixed power. The envelopes satisfy \(0<P(v)\le1\). Leibniz' rule and (L1.9) consequently give, for an actual coefficient of original class exponent \(\alpha\),
\[
|\partial_x^a\partial_t^b(a_\gamma e^{ikn\Phi_\gamma})|
\le C_{j,a,b}Q^{h\alpha-|a|s_x-bs_t}S_*^{P_{j,a,b}}.
\tag{L1.10}
\]
The identical bound without the exponential holds for a mean coefficient. Source closure S1 gives a finite harmonic set at each stage, independent of the band; its size and the powers of \(n\) enter constants, not powers of \(Q\). Bounded differences of overlapping covering indices multiply constants by fixed powers of \(J_g\). Slow mesh cutoffs cost powers of \(S_*\). Their bounded local multiplicity and smooth support extensions therefore preserve (L1.10) across label and band boundaries. Since \(q/Q\in[1/2,2]\), changing \(Q\) to the original \(q\) changes constants; even the factor \(2^{h\alpha}\) is allowed to depend on the stage. Also \(S_*^P\le C_P(1+|\log q|)^{2P}\) on these bands.

## L2. Stage-independent losses for the exact tuples

For the cycle from \(j-1\) to \(j\), K3–K6 give
\[
B_{j-1}=\tfrac35+\tfrac j{10},\quad
C_{j-1}^*=\tfrac{11}{10}+\tfrac j{10},\quad
H_{j-1}=\tfrac{11}{10}+\tfrac j{10}-2\kappa_s.
\tag{L2.1}
\]
The particular and signed wave velocities have exponents \(B_{j-1}\) and \(B_{j-1}-\kappa_s\). Their potentials contain the additional factor \(1/(kn)\) and have exponents at least \(B_{j-1}+1/2\) and \(B_{j-1}+1/2-\kappa_s\), respectively. The derivative and division estimates of P6 and C5 retain those full potential bounds. Mean potentials and direct azimuthal fields have exponent \(H_{j-1}\). Mean-pressure increments have exponents \(C_{j-1}^*-\kappa_s\) or \(H_{j-1}\), and the two harmonic pressure increments have the same exponents as their corresponding wave potentials. Consequently every entry of the exact tuple, and every actual velocity increment, has coefficient exponent at least \(j/10\). All omitted positive offsets in this last inequality remain recorded in the preceding list; it is an estimate on the original fields, not their replacement by leading terms.

The physical rescaling factors for velocity, pressure, wave potential and mean potential are, respectively,
\[
Q^{-A},\qquad Q^{-2A},\qquad Q^{1/2-A},\qquad Q^{1/2-A}.
\tag{L2.2}
\]
Every one is bounded above by \(Q^{-2A}\) for \(0<Q<1\). The factor \((kn)^{-1}\) is already inside the potential coefficient. One more spatial derivative covers its complete curl. Combining (L1.10) and (L2.1)–(L2.2) therefore proves original (9.17) with the explicit common loss
\[
|Z_j|_m+|\Delta u_j|_m
\le C_{j,m}q^{g_j-\ell_m}(1+|\log q|)^{P_{j,m}},\qquad
g_j=\frac{hj}{10},\quad
\ell_m=2A+(m+1)\left(1+\frac{3h}{2}\right).
\tag{L2.3}
\]
The loss is independent of \(j\), nonnegative and increasing in \(m\). This derivation uses the exact original stage orders, not the stronger cycle gain from K7.

For the complete residual, K0 and K7 give wave exponent at least \(B_j\), exact tangential means at least \(C_j^*\), and the radial term \(-\rho\mathcal P\) at least \(C_j^*\). All are at least \(\sigma_j\). The radial compact remainder, Gaussian tails and the base residual are the additive flat terms recorded in S3; they have not been included as new pulse sources. The physical residual factor is \(Q^{-2A-1/2}\), so (L1.10) gives on the correction shell
\[
|\mathscr R_1(u^{[j]},p^{[j]})|_m
\le C_{j,m}q^{h\sigma_j-K_m^R}(1+|\log q|)^{P_{j,m}}
+E_{j,m},\quad K_m^R=2A+\tfrac12+ms_t,
\tag{L2.4}
\]
where, for every fixed \(j,m,N\), \(E_{j,m}\le C_{j,m,N}q^N\). The source-base part of this assertion is the actual flat residual proved in [Z5](base-field-realization-audit.md#z5-the-complete-augmented-residual-is-flat), original (5.41). All correction-generated flat terms have the uniform band estimates proved in P7, R5–R6 and S3. The bound is for the actual field after evaluating the torus map. Differentiating that map was included in L1.

Finite addition and the retained total bounds in K7 also give
\[
|(u^{[j]},p^{[j]})|_m\le C_{j,m}q^{-K_m^U}(1+|\log q|)^{P_{j,m}},
\tag{L2.5}
\]
where one may take \(K_m^U=\max\{K_m^{\rm base},\ell_{m+1}\}\). Here \(K_m^{\rm base}\) is the fixed-base exponent supplied by (5.42) and its Cartesian axis/exterior representations; it is independent of the correction stage. A finite number of new constants cannot change \(K_m^U\). Taking the maximum of \(K_m^R\) and \(K_m^U\) yields the common \(K_m\) allowed in original (9.18). Outside the annular corrections the finite fields equal the actual base. Thus uniformity on every bounded profile rectangle uses precisely the base assertions just identified, and exterior uniformity uses its exact heat field proved in L6 below. The shell and exterior estimates apply on their stated domains.

## L3. The original viscosity, coordinates and cutoff derivatives

For every fixed \(\nu>0\), the exact bridge is \(y=x_\nu/\sqrt\nu\), with time unchanged. Put
\[
A_{j,\nu}(x_\nu,t)=\nu A_j(y,t),\quad
B_{j,\nu}^{\rm vec}(x_\nu,t)=\sqrt\nu B_j^{\rm vec}(y,t),\quad
p_{j,\nu}(x_\nu,t)=\nu p_j(y,t),\quad
\Delta u_{j,\nu}=\sqrt\nu\Delta u_j(y,t).
\tag{L3.1}
\]
The curl of the first field is \(\sqrt\nu\operatorname{curl}_y A_j\). For every spatial multi-index \(a\) and time order \(b\), the exact derivative factors are
\[
\begin{array}{c|c}
\text{field}&\text{factor multiplying its derivative in }(y,t)\\\hline
A_{j,\nu},p_{j,\nu}&\nu^{1-|a|/2}\\
B_{j,\nu}^{\rm vec},\Delta u_{j,\nu}&\nu^{1/2-|a|/2}\\
\mathscr R_\nu(u_\nu,p_\nu)&\nu^{1/2-|a|/2}.
\end{array}
\tag{L3.2}
\]
The last line follows by expanding the time, diffusion, convection and pressure terms: each has the common factor \(\sqrt\nu\) before further differentiation. These fixed positive factors enter the constants in (L2.3)–(L2.5), while their \(q\)-exponents and stage independence are unchanged.

Keep the actual scale variable and profile coordinates
\[
q_\nu-(z_\nu^2/\nu)q_\nu^{2h}=1-t,\quad
\eta_\nu=z_\nu/(\sqrt\nu q_\nu^D),\quad
X_\nu=r_\nu^2/(2\nu q_\nu),\quad L=1-2h\eta_\nu^2\ge1-2h>0.
\tag{L3.3}
\]
The original \(q\) is not replaced by a new time variable. Implicit differentiation gives
\[
\begin{split}
\partial_{z_\nu}q_\nu&=\nu^{-1/2}\frac{2\eta_\nu q_\nu^{1-D}}L,
&\partial_tq_\nu&=-1/L,\\
\partial_{z_\nu}\eta_\nu&=\nu^{-1/2}\frac{q_\nu^{-D}(1-\eta_\nu^2)}L,
&\partial_t\eta_\nu&=D\eta_\nu/(q_\nu L).
\end{split}
\tag{L3.4}
\]
Applying these formulas repeatedly to \(q_\nu^\lambda F(\eta_\nu)\) gives
\[
\partial_{z_\nu}^a\partial_t^bq_\nu
=\nu^{-a/2}q_\nu^{1-aD-b}F_{a,b}(\eta_\nu),\quad
F_{a,b}\in C^\infty([-1,1]),
\tag{L3.5}
\]
because the recurrences use only derivatives, products and division by powers of the positive \(L\). The first-step operators on \(F\) are \([2\lambda\eta F+(1-\eta^2)F']/L\) and \([-\lambda F+D\eta F']/L\), respectively. They prove the induction and its finite bounds on the closed interval. Also \(q_\nu\ge1-t\); thus it has a positive lower bound on every compact subset of \(t<1\).

Let \(\chi\) be smooth, one on \([0,1/2]\), zero on \([1,\infty)\). Such a function is given by \(\chi(s)=\psi(1-s)/(\psi(1-s)+\psi(s-1/2))\), with \(\psi(s)=e^{-1/s}\) for \(s>0\) and zero otherwise. Every derivative of \(\psi\) at zero vanishes, by the exponential-versus-power estimate used in L1. For any scale \(a_*>0\), a positive-order derivative of \(\chi(a_*q_\nu)\) is a finite sum
\[
c\,a_*^k\chi^{(k)}(a_*q_\nu)
\prod_{v=1}^k\partial_{z_\nu}^{a_v}\partial_t^{b_v}q_\nu,
\quad \sum a_v=a,\quad\sum b_v=b,\quad a_v+b_v\ge1.
\tag{L3.6}
\]
It is supported where \(1/2\le a_*q_\nu\le1\). Equation (L3.5) bounds the product by a constant times \(\nu^{-a/2}q_\nu^{k-aD-b}\); hence the factor \(a_*^k\) is bounded using \((a_*q_\nu)^k\le1\). The resulting bound is \(C_{a,b}\nu^{-a/2}q_\nu^{-aD-b}\), independent of \(a_*\). Derivatives in the first two Cartesian coordinates vanish. Every cutoff derivative of total order at most \(m\) therefore costs at most \(q_\nu^{-m}\), with its actual viscosity factors retained.

## L4. One actual sum of potentials, with every cutoff curl

K8 supplies one domain \(0<q<q_{\rm big}\) for all finite operations. Take \(U_{0,\nu}\) to be the actual slow base plus finite initialization. If an outer cutoff is needed for the initialization, apply it to its wave and mean potentials before taking curls, and to its direct azimuthal field and pressure. Keep the slow base itself unchanged. Choose that one cutoff to equal one for \(q_\nu<c_0\), with \(c_0>0\), and to vanish before \(q_{\rm big}\). Its extra terms have compact annular support with \(q_\nu\ge c_0\); their derivatives are bounded and hence at most \(C_Nq_\nu^N\) for every fixed \(N\). There are only finitely many dyadic labels in this region. This changes no finite-state comparison near \(q_\nu=0\) and preserves the base exterior. It does not set these extra terms to zero.

For \(a_*>0\), define the complete cut increment
\[
W_{j,\nu}(a_*)=
\left(\operatorname{curl}(\chi(a_*q_\nu)A_{j,\nu})
+\chi(a_*q_\nu)B_{j,\nu}^{\rm vec},\quad
\chi(a_*q_\nu)p_{j,\nu}\right).
\tag{L4.1}
\]
Its velocity contains both terms in
\[
\operatorname{curl}(\chi(a_*q_\nu)A_{j,\nu})
=\chi(a_*q_\nu)\operatorname{curl}A_{j,\nu}
+a_*\chi'(a_*q_\nu)\nabla q_\nu\times A_{j,\nu}.
\tag{L4.2}
\]
The full product rule, (L2.3) and (L3.6) imply
\[
|W_{j,\nu}(a_*)|_m\le\widehat C_{j,m,\nu}
q_\nu^{g_j-\ell'_m}(1+|\log q_\nu|)^{\widehat P_{j,m}},
\qquad \ell'_m=\ell_{m+1}+m+1,
\tag{L4.3}
\]
with constants independent of \(a_*\). Indeed the potential needs at most \(m+1\) derivatives; each term is bounded using \(q_\nu^{-m-1}q_\nu^{g_j-\ell_{m+1}}\), and the direct field and pressure need no more derivatives. The fixed \(\nu\) factors from L3 remain in \(\widehat C_{j,m,\nu}\).

For \(g>0\) and finite \(P\), \(q^g(1+|\log q|)^P\to0\) as \(q\downarrow0\). Setting \(y=-\log q\), this follows from \(e^{gy/2}\ge(gy/2)^n/n!\) with an integer \(n>P\). We can therefore choose one increasing sequence \(a_{j+1}\ge2a_j\), \(a_1^{-1}<q_{\rm big}\), by requiring the finite list
\[
\widehat C_{j,m,\nu}(1+|\log q_\nu|)^{\widehat P_{j,m}}
q_\nu^{g_j/2}\le2^{-j}
\quad(0<q_\nu\le a_j^{-1},\quad0\le m\le j).
\tag{L4.4}
\]
The already proved positive \(g_j=hj/10\) makes every member possible. Larger cutoffs meet all members at once. Alternatively, the viscosity-one sequence may be pulled back by (L3.1); its derivative bounds then gain the fixed factors in (L3.2). Either construction uses the same original \(q_\nu\) and gives the original viscosity \(\nu\), not a new field equation.

On compact sets with \(q_\nu\ge c>0\), all sufficiently large \(j\) satisfy \(a_jq_\nu\ge1\), so their summands vanish. Define the locally finite fields
\[
\begin{split}
\mathcal A_\nu&=\mathcal A_{0,\nu}+\sum_{j\ge1}\chi(a_jq_\nu)A_{j,\nu},\\
\mathcal B_\nu e_\theta&=\mathcal B_{0,\nu}e_\theta+\sum_{j\ge1}\chi(a_jq_\nu)B_{j,\nu}^{\rm vec},\\
p_{{\rm loc},\nu}&=p_{0,\nu}+\sum_{j\ge1}\chi(a_jq_\nu)p_{j,\nu},\qquad
u_{{\rm loc},\nu}=\operatorname{curl}\mathcal A_\nu+\mathcal B_\nu e_\theta.
\end{split}
\tag{L4.5}
\]
These are original (9.21) with every viscosity factor included. Mixed Cartesian derivatives commute, so the curl has zero divergence. Each direct azimuthal field is independent of \(\theta\), including its auxiliary dependence after evaluation, because \(Y(r,t)\) has no angular argument. Its divergence is \(r_\nu^{-1}\partial_\theta b=0\). Multiplication by \(\chi(a_jq_\nu)\) adds \(\nabla\chi\cdot(b e_\theta)=0\), since \(q_\nu\) is independent of radius and angle. Thus incompressibility holds exactly, including (L4.2).

For \(J\ge\max(1,m)\) and \(q_\nu<(2a_J)^{-1}\), the first \(J\) cutoffs are identically one near the point and their derivatives vanish. Equations (L4.3)–(L4.4) give the exact comparison with the uncut finite state,
\[
|(u_{{\rm loc},\nu},p_{{\rm loc},\nu})-(u_\nu^{[J]},p_\nu^{[J]})|_m
\le\sum_{j>J}2^{-j}q_\nu^{g_j/2-\ell'_m}
\le2^{-J}q_\nu^{g_{J+1}/2-\ell'_m}.
\tag{L4.6}
\]
If the finite initialization received its optional cutoff, also require \(q_\nu<c_0\). This is one fixed additional restriction, independent of the later stage. The monotonicity of \(g_j\) and the geometric series prove the second inequality. The first equality of fields behind this estimate holds only in the region where those first cutoffs are one; no assertion has been made about matching a finite state on all transition annuli.

Every correction potential and direct azimuthal field vanishes in a neighborhood of the axis for each fixed \(q_\nu>0\). Local finiteness makes that neighborhood common for the finite set of nonzero summands near a point. The source base Stokes streamfunction has the form \(S=r^2s(r^2,z,t)\); its azimuthal potential is \((S/r)e_\theta=(-x_2,x_1,0)s\). Its base angular field likewise has \(r e(r^2,z,t)e_\theta=(-x_2,x_1,0)e\). These are the precise Cartesian maps used for the base in original (5.27). Their actual source coefficients and Cartesian regularity are proved in [Z0–Z4](base-field-realization-audit.md); these are the same original Stokes potentials, with their full cutoff curls. All correction boundary extensions were proved in S1–S2, and all added series vanish for \(q_\nu\ge a_1^{-1}\). Thus the summation preserves the original Cartesian axis and outer-support properties.

## L5. The nonlinear residual of the summed fields

Keep the entire original operator
\[
\mathscr R_\nu(u,p)=\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p.
\tag{L5.1}
\]
For one finite state put \(v=u_\nu^{[J]}\), \(p_*=p_\nu^{[J]}\), \(e=u_{{\rm loc},\nu}-v\), and \(\pi=p_{{\rm loc},\nu}-p_*\). Direct subtraction gives
\[
\mathscr R_\nu(v+e,p_*+\pi)-\mathscr R_\nu(v,p_*)
=\partial_te-\nu\Delta e+\nabla\pi
+(v\cdot\nabla)e+(e\cdot\nabla)v+(e\cdot\nabla)e.
\tag{L5.2}
\]
For each component and multi-index \(I\), the convective product rule is
\(\partial^I(v_k\partial_ke_i)=\sum_{L\le I}\binom IL(\partial^Lv_k)(\partial^{I-L}\partial_ke_i)\); the other two products have the identical formula with their displayed factors. Summing the finite component and multi-index lists proves
\[
|\mathscr R_\nu(v+e,p_*+\pi)-\mathscr R_\nu(v,p_*)|_m
\le C_m\bigl((1+\nu)|e|_{m+2}+|\pi|_{m+1}
+|v|_{m+1}|e|_{m+1}+|e|_{m+1}^2\bigr).
\tag{L5.3}
\]
This includes the complete new-new nonlinear term. All cutoff contributions are already part of \(e\) through (L4.2).

Fix \(m,N\ge0\), set \(r=m+2\), and choose one finite \(J\ge r\) so large that
\[
\alpha:=g_{J+1}/2-\ell'_r\ge N+K_r^U+1,
\qquad h\sigma_J-K_m^R\ge N+1.
\tag{L5.4}
\]
This is possible because both \(g_j\) and \(h\sigma_j\) tend to infinity, while all displayed losses are independent of the stage. Explicitly, the two latter inequalities require
\[
J\ge\frac{20}{h}(N+K_r^U+1+\ell'_r)-1,
\qquad
J\ge\frac{10}{h}(N+1+K_m^R)-2.
\tag{L5.5}
\]
Choose an integer meeting these and \(J\ge r\); this is an existence calculation, with no numerical trajectory or limiting precision required. Keep this \(J\) fixed. Shrink the \(q_\nu\)-neighborhood below \((2a_J)^{-1}\) and, if needed, \(c_0\), until the finitely many constants and logarithmic factors in (L2.4)–(L2.5) are bounded by \(q_\nu^{-1}\). The limit proved before (L4.4) justifies this choice. Then (L4.6) gives
\[
|(e,\pi)|_{m+2}\le2^{-J}q_\nu^\alpha,
\qquad |v|_{m+1}\le q_\nu^{-K_r^U-1}.
\tag{L5.6}
\]
The terms in (L5.3) have powers at least \(\alpha\), \(\alpha-K_r^U-1\), and \(2\alpha\), respectively. Every one is at least \(N\) by (L5.4). The finite-state residual has its retained remainder and satisfies
\[
|\mathscr R_\nu(v,p_*)|_m
\le q_\nu^{h\sigma_J-K_m^R-1}+C_{J,m,N,\nu}q_\nu^N
\le(1+C_{J,m,N,\nu})q_\nu^N.
\tag{L5.7}
\]
Combining (L5.3), (L5.6) and (L5.7) proves every derivative of the summed residual vanishes to every prescribed order. The order of choices is \((m,N)\), then one finite \(J\), then its neighborhood and constants. No infinite sum of finite-stage flat remainders has been taken. This supplies the actual correction sequence to the summation argument, rather than relying on an unsupported assertion that a sum of flat functions remains flat.

## L6. Endpoint regularity and the exact exterior heat field

Fix a compact spatial set and \(0<c<c'<q_{\rm big}\), and work up to \(\tau=1-t=0\) where \(c\le q_\nu\le c'\). Only finitely many correction stages survive (L4.5). Only finitely many dyadic bands satisfy \(q_\nu/Q\in[1/2,2]\), and their bounded slow rectangles have finitely many mesh labels. The original labels, representatives, rounded frequencies and torus rectangles were chosen on the closed \(\tau\ge0\) range in (6.8), before differentiation. None is recomputed at the endpoint.

For each of these finite labels, the pulse ODE has fixed positive denominators, its finite derivative bounds from P4–P5, and its original smooth cutoffs. The signed operator divides by the same positive primary amplitude; C4–C5 handles its edge derivatives. The radial and temporal maps have their closed-boundary estimates from R, M and T. The base coefficients extend with all fixed derivatives to \(\eta=\pm1\) by the precise source assertion (5.43) and the following paragraph of Proposition 5.5. The actual supplier is proved in [Z7](base-field-realization-audit.md); [I5](local-construction-assembly-audit.md) verifies the complete endpoint assembly for these potentials and pressure. Coordinate conversion uses \(L\ge1-2h\) in (L3.4), while annular support gives a positive lower bound for \(r_\nu\) on \(q_\nu\ge c\). At the axis use the Cartesian factors just displayed in L4. Thus each fixed derivative of the finite sum is uniformly bounded on a neighborhood of the chosen compact set up to the endpoint.

The limits and their compatibility follow explicitly. For each derivative \(\partial^I f\), bound one additional time derivative on that neighborhood. The fundamental theorem of calculus gives
\[
|\partial^I f(x,t_2)-\partial^I f(x,t_1)|\le C_I|t_2-t_1|.
\tag{L6.1}
\]
It is uniformly Cauchy as \(t_1,t_2\uparrow1\). Denote its continuous limit by \(f_I(x)\). On every small coordinate segment in the same neighborhood, the identity
\(\partial^I f(x+s e_k,t)-\partial^I f(x,t)=\int_0^s\partial^{I+e_k}f(x+v e_k,t)\,dv\)
passes to the uniform limit and proves \(\partial_{x_k}f_I=f_{I+e_k}\). The time integral identity similarly proves the one-sided time derivative equals the corresponding limit. This proves every compatibility assertion for \(\mathcal A_\nu,\mathcal B_\nu e_\theta,p_{{\rm loc},\nu}\) themselves, not merely for the velocity.

The exact exterior heat factor is also directly checkable. Original (A.32) defines
\[
a_K=1+h,\qquad
\mathcal H(Z)=\frac1{\Gamma(1+h)}\int_0^\infty e^{-v}v^h(1+Zv)^{-h}\,dv,
\qquad Z\ge0.
\tag{L6.2}
\]
Here \(\Gamma(1+h)=\int_0^\infty e^{-v}v^h\,dv\); neither its argument nor the exponent of \(1+Zv\) is altered. For the full rising factorial \((b)_m=b(b+1)\cdots(b+m-1)\), with \((b)_0=1\), differentiating under this integral yields exactly
\[
\mathcal H^{(m)}(Z)=\frac{(-1)^m(h)_m}{\Gamma(1+h)}
\int_0^\infty e^{-v}v^{h+m}(1+Zv)^{-h-m}\,dv,
\quad
\sup_{Z\ge0}|\mathcal H^{(m)}(Z)|\le(h)_m(1+h)_m.
\tag{L6.3}
\]
The dominating function is the displayed integrand with its last factor replaced by one; it is integrable at zero since \(h+m>-1\) and at infinity by exponential decay. Gamma integration by parts gives \(\Gamma(1+h+m)/\Gamma(1+h)=(1+h)_m\). Dominated convergence proves smooth right derivatives at zero of all orders, where equality is \(\mathcal H^{(m)}(0)=(-1)^m(h)_m(1+h)_m\). No convergent Taylor series is asserted.

The finite Taylor remainder can be retained exactly. For every integer \(n\ge0\) and \(Z\ge0\), the fundamental theorem of calculus and (L6.3) give
\[
\begin{split}
\mathcal H(Z)&=\sum_{m=0}^n\frac{(-1)^m(h)_m(1+h)_m}{m!}Z^m+R_n(Z),\\
R_n(Z)&=\frac1{n!}\int_0^Z(Z-s)^n\mathcal H^{(n+1)}(s)\,ds,\\
|R_n(Z)|&\le\frac{(h)_{n+1}(1+h)_{n+1}}{(n+1)!}Z^{n+1}.
\end{split}
\tag{L6.3a}
\]
For \(Z>0\), its sign is \((-1)^{n+1}\), directly from the positive integral in (L6.3). Every fixed truncation is therefore justified with its full error. In contrast, for \(h>0\) the absolute Taylor coefficient \(a_m=(h)_m(1+h)_m/m!\) satisfies
\[
\frac{a_{m+1}|Z|^{m+1}}{a_m|Z|^m}
=|Z|\frac{(h+m)(1+h+m)}{m+1}\longrightarrow\infty
\quad(Z\ne0).
\tag{L6.3b}
\]
The formal series has radius zero, since its terms do not tend to zero at any nonzero argument. Thus this heat factor has no analytic extension through zero, while all its right derivatives exist as proved above. This precise regularity statement does not alter the source's finite Taylor argument. It also does not concern the different analytic axis-pressure integral, whose holomorphic extension is proved in [O4](outer-profile-audit.md).

Multiplying the derivative of \(e^{-v}v^{1+h}(1+Zv)^{-1-h}\) by \(h\), and expressing the result with the common factor \(e^{-v}v^h(1+Zv)^{-h-2}\), gives the polynomial \(h(1+h-v-Zv^2)\). Substituting (L6.2)–(L6.3) into the following left side gives that same integrand. Both endpoint terms vanish, so
\[
Z^2\mathcal H''+(1+2a_KZ)\mathcal H'+a_K(a_K-1)\mathcal H=0.
\tag{L6.4}
\]
This verifies the integral identity in original (A.37) with its boundary terms.

Retain \(s=r^2/2\) and the original positive coefficient \(c_\infty\). The physical exterior field is
\[
K(r,\tau)=c_\infty s^{-A}\mathcal H(2\tau/s)
=r^{-1-2h}\mathcal H_{\rm ext}(\tau/r^2),\qquad
\mathcal H_{\rm ext}(\omega)=2^Ac_\infty\mathcal H(4\omega).
\tag{L6.5}
\]
All constants in this comparison remain explicit. Direct differentiation with \(Z=2\tau/s\) gives
\[
\begin{split}
\partial_tK&=-2c_\infty s^{-A-1}\mathcal H',\\
(\partial_r^2+r^{-1}\partial_r-r^{-2})K
&=2c_\infty s^{-A-1}
\{Z^2\mathcal H''+(2A+1)Z\mathcal H'+(A^2-1/4)\mathcal H\}.
\end{split}
\tag{L6.6}
\]
Since \(2A+1=2a_K\) and \(A^2-1/4=a_K(a_K-1)\), (L6.4) makes these two quantities equal. Thus the exact swirl heat equation, including \(-r^{-2}K\), holds. Equation (L6.3) also gives the original uniform bound
\[
\sup_{\omega\ge0}|\mathcal H_{\rm ext}^{(m)}(\omega)|
\le2^Ac_\infty4^m(h)_m(1+h)_m.
\tag{L6.7}
\]
It applies on the full nonnegative half-line.

The exterior pressure is exactly
\[
p_{\rm ext}(r,\tau)=-\int_r^\infty\frac{K(\rho,\tau)^2}{\rho}\,d\rho.
\tag{L6.8}
\]
The integral converges because \(0<\mathcal H\le1\) and its integrand is bounded by \((2^Ac_\infty)^2\rho^{-3-4h}\). Its radial derivative is \(+K(r,\tau)^2/r\), cancelling the centrifugal component \(-K^2/r\) of \((Ke_\theta\cdot\nabla)(Ke_\theta)\). The other pressure components vanish. Together with (L6.6), this proves the full momentum residual is identically zero in the exterior.

For completeness, every derivative of the pressure is controlled without discarding its endpoint. Put \(d=1+2h\), \(\omega=\tau/r^2\). Differentiation gives the exact finite formula
\[
\partial_r^a\partial_\tau^bK
=r^{-d-a-2b}\sum_{k=0}^a c_{a,b,k}\omega^k\mathcal H_{\rm ext}^{(b+k)}(\omega),
\tag{L6.9}
\]
where \(c_{0,b,0}=1\), coefficients outside \(0\le k\le a\) are zero, and
\(c_{a+1,b,k}=(-d-a-2b-2k)c_{a,b,k}-2c_{a,b,k-1}\).
In the exterior \(X\ge X_{\rm ext}\), \(\omega=(1-\eta^2)/(2X)\le1/(2X_{\rm ext})\). Equations (L6.7)–(L6.9) bound every term. Time differentiation of (L6.8) retains the full sum \(\sum_{i=0}^b\binom bi(\partial_\tau^iK)(\partial_\tau^{b-i}K)/\rho\), bounded by \(C_b\rho^{-3-4h-2b}\); it is integrable. Each subsequent radial derivative differentiates its lower-endpoint value. This proves all fixed exterior derivative bounds and right limits for \(r\) bounded away from zero, including the pressure.

For the original viscosity, the exact exterior formulas are
\[
\begin{split}
K_\nu(r_\nu,\tau)&=\sqrt\nu\,K(r_\nu/\sqrt\nu,\tau)
=\nu^{1+h}r_\nu^{-1-2h}\mathcal H_{\rm ext}(\nu\tau/r_\nu^2),\\
p_{{\rm ext},\nu}(r_\nu,\tau)&=\nu p_{\rm ext}(r_\nu/\sqrt\nu,\tau)
=-\int_{r_\nu}^\infty K_\nu(\rho,\tau)^2\,\frac{d\rho}{\rho}.
\end{split}
\tag{L6.10}
\]
The derivatives have the factors in (L3.2), and the heat equation is \(-\partial_\tau K_\nu=\nu(\partial_{r_\nu}^2+r_\nu^{-1}\partial_{r_\nu}-r_\nu^{-2})K_\nu\). The same exact centrifugal cancellation gives \(\mathscr R_\nu=0\).

## L7. The preserved inner and exterior fields

All wave and mean potentials, direct angular corrections and pressure increments in this cycle have support in \(X_a\le X_\nu\le X_b\). Multiplication by \(\chi(a_jq_\nu)\) preserves this support. The extra curl term (L4.2) also has this support; differentiation cannot create a value outside the closed support of the smooth potential. Thus the summed correction is identically zero in both the inner region \(X_\nu<X_a\) and the common exterior \(X_\nu>X_b\).

The source base's exact exterior is supplied by its leading profile together with the zero total axial moments of every positive-order coefficient, which make its Stokes potentials vanish there. Its pressure is fixed by its value zero at radial infinity. These are proved for the actual fields by V7, Y3 and [Z4/Z7](base-field-realization-audit.md), including the zero exterior pressure and the full cutoff curl. The calculation here proves that no correction or summation cutoff changes that exterior, and L6 proves the full claimed heat-field and pressure properties from its original integral. It does not infer the base's exterior matching from the existence of the heat field alone.

At the original inner point \(X_{\rm in}\in(0,X_a)\), \(z_\nu=0\), one has \(q_\nu=\tau\), \(\eta_\nu=0\), and \(r_\nu=\sqrt{2\nu X_{\rm in}\tau}\). Every annular correction vanishes there, including its cutoff curl. The original leading coefficient and full base remainder therefore pass unchanged to
\[
u_{\theta,{\rm loc},\nu}(\sqrt{2\nu X_{\rm in}\tau},0,0,1-\tau)
=\sqrt\nu\,\tau^{-A}\bigl(E_0(X_{\rm in},0)+O(\tau^{2h})\bigr).
\tag{L7.1}
\]
The entries denote cylindrical position and time, as in original (3.6). V7 proves the actual positive value \(e_0=E_0(X_{\rm in},0)>0\), and [Z6.2](base-field-realization-audit.md) proves the displayed base remainder with every required derivative. The annular support proved above then gives L7.1 for the supplied fields, with the original viscosity factor. Final localization and the global theorem conclusion remain separate checks.

The physical derivative loss and summation mechanism are derived from the finite cycle proved in K0–K8. The actual leading profile, reserved patches, strict stress cone, edge weights, global coefficient sequence and realized base are supplied by G/O/H/J/Q/V/D/Y and [Z0–Z8](base-field-realization-audit.md). Their exact domains, supports, full curl terms, residual comparison, endpoint limits and exterior integral are retained. The complete assembly of Theorem 3.1 from these actual inputs and K/L is proved in [I0–I7](local-construction-assembly-audit.md). Final localization, smooth force extension, solution class, energy and comparison are derived for the actual fields in [F0–F8](terminal-force-and-blowup-audit.md); their complete proof connections are recorded in the [audit conclusion](theorem-audit-conclusion.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).