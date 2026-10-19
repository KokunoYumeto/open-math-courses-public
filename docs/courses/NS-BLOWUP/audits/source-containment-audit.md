# Finite-stage source containment and exact residuals

The original Proposition 9.3 is a closure statement for finite applications of specified operators. This note proves that closure using their complete local derivations. It does not prove the global profile/base construction, the improving correction cycle, or the complete blowup theorem.

Source: OpenAI, *Finite Time Blowup for Navier–Stokes*, original [PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), SHA256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. The source passages are on original pages 70, 89 and 103–105. The actual leading profile and base are supplied by [V0–V7](shear-realization-audit.md) and [Z0–Z8](base-field-realization-audit.md).

The supplying operator proofs are [radial primitives R1–R8](radial-primitive-audit/src/radial-primitives-and-compact-mean-corrections.md), [five-profile means M1–M8](mean-moment-correction-audit.md), [temporal means T1–T4](temporal-mean-correction-audit.md), [wave interactions W1–W8](wave-interaction-audit.md), [pulse inverse P1–P8](pulse-inverse-audit.md), and [stress realization C1–C9](stress-covariance-audit.md). All are included in this construction collection. The letter \(j\) below is a finite number of updates; constants may depend on \(j\) and a fixed derivative order. There is no claim of a uniform infinite-stage estimate in this note.

## S1. The actual support invariant and harmonic sets

Keep the original band, phase and class definitions in W1–W3 and C1. In particular the band \(Q=2^{-\ell}\), \(\varepsilon=Q^h\), \(S_*=\ell^2\) and the integer \(kp_\gamma\ne0\) are fixed before coefficient differentiation. Original (6.28), on page 70, prescribes
\[
\begin{split}
\mathcal E_\gamma&=\{(x_*,H):H\in\overline{\mathcal R_\gamma^H}\},\\
\Omega_\gamma&=\{(x_*,H)\in\mathcal E_\gamma:
x_*\in K_\gamma^*,\ \xi_g(H)\in\operatorname{supp}\chi_g,\ X_a\le X\le X_b\},\\
\Omega_\gamma^{\rm cut}&=\Omega_\gamma\cap\{v(H)\in\operatorname{supp}\psi\}.
\end{split}
\tag{S1.1}
\]
Here \(x_*=(R,Z,T)\), \(K_\gamma^*\) is the prescribed slow support, and \(\mathcal E_\gamma^+\) replaces the closed rectangle by its fixed open enlargement. The coefficient is independent of \(\theta\), smooth on that open domain, and extends by zero across the slow, transverse and radial shell boundaries. On \(0\le v\le L_s\), its bound is
\[
|\partial^Ia_{\gamma,m}|\le C_{j,I}\varepsilon^\alpha S_*^{b_{j,I}}
\sqrt\zeta\delta^{-d_{j,I}}P(v),\qquad
0<P(v)\le1.
\tag{S1.2}
\]
Actual cut velocities have support in \(\Omega_\gamma^{\rm cut}\) and a smooth zero extension in \(v\). The uncut local initial-value solution has no temporal zero-extension requirement. The source entering that solve is an actual supported coefficient; it need not be divisible by \(\eta_\beta\chi_g\psi\).

The primary amplitudes have these properties by C4 and C7. Differentiating an identically zero smooth function outside a closed support leaves it zero there. Applying a smooth local differential operator therefore preserves the support in (S1.1). Explicit \(D_r\) occurrences cost at most \(\kappa_s=10^{-5}\) each, as proved in W3; further coefficient derivatives of the resulting estimate only change its fixed constants and polynomial degrees. The full linearized residual, including phase derivatives and all cylindrical terms, is expanded in P8, so its class estimate does not omit derivatives falling on an exponential.

For products, the full unsymmetrized formulas in W5–W6 give the following exhaustive possibilities. A mean coefficient times a nonzero harmonic retains that harmonic and its support. Two waves with the same label have integer multiplier \(m+m'\); if this is nonzero they retain the wave weight since \(P^2\le P\) and \(\zeta\le\sqrt\zeta\). If it is zero, the phases cancel and the result has the mean weight \(\zeta\). Angular averaging removes every other integer multiplier because \(kp_\gamma\ne0\). Products of different labels, including derivatives and curls, vanish on their closed supports by W2. Thus no mixed phase has to be inverted. Products involving exactly one wave and any mean generated earlier inherit the wave's support even if that mean now occupies the entire auxiliary torus.

Starting with multipliers \(\{-1,1\}\), the set after one update is contained in
\[
\mathscr H_{j+1}\subset
\bigl(\mathscr H_j\cup\{-1,1\}\cup
\{m+m':m,m'\in\mathscr H_j\cup\{-1,1\}\}\bigr)\setminus\{0\}.
\tag{S1.3}
\]
A pulse solve, curl, pressure coefficient or coefficient derivative preserves its multiplier; the signed stress map introduces only \(\pm1\); means introduce zero only. Formula (S1.3) is a finite set at every finite stage and does not depend on a band. For example, if all old multipliers have modulus at most \(M_j\ge1\), all newly formed ones have modulus at most \(2M_j\). This supplies a finite stage-dependent harmonic bound rather than presupposing one.

Finally P4 gives the particular pulse by an integral along the original auxiliary path, holding all slow and transverse coordinates fixed. If that fixed pair is outside its prescribed support, the source vanishes along the entire path, so the integral and all its derivatives vanish. Inside it the P3 forward propagator cancels the source envelope exactly and yields (S1.2) with a polynomial factor from the length \(L_s=O(S_*)\). P4's differentiated integral equation proves every fixed derivative estimate. Multiplying by the original \(\psi\) restores \(\Omega_\gamma^{\rm cut}\); taking the full curl preserves it. This proves the inverse's incoming support property at every finite update, without a cutoff-division assumption.

## S2. Mean operations, edge integration and stress input

The mean class allows full auxiliary dependence. Its exact bound is
\[
|\partial^If|\le C_{j,I}\varepsilon^\mu S_*^{b_{j,I}}
\zeta(X)\delta(X)^{-d_{j,I}},\qquad
\zeta(X)=\exp\left(-\frac{a_a}{\log^2(X/X_a)}-
\frac{a_b}{\log^2(X_b/X)}\right),\quad a_a,a_b>0.
\tag{S2.1}
\]
Radial integration follows the original shifted auxiliary path and retains its full cutoff remainder; the exact operator and all its coefficient derivatives are proved in R3–R6. Its domain and output are \(\mathsf M_\mu\), with the original physical measures in R1 and M2. The pressure uses the same operator, the axial velocity uses the full compact curl in R7, and the temporal mean inverse is the exact Fourier operator with its finite derivative bound in T1–T3. The five-profile operation has the explicit inverse in M3 and the complete nonlinear recomputation in M5–M7. These mean operations preserve angular independence. They can enlarge auxiliary support; they cannot create a new nonzero angular harmonic. W5 treats their next interaction with each wave using the full resulting mean, including all cutoff remainders.

For the auxiliary-independent stress passed to C5, fix \(e\in\{1,2\}\). Given its radial source \(f(R,Z,T)\), put
\[
M_e=\int_0^\infty R^ef\,dR,\quad
f_0=f-\rho_e M_e,\quad
\int_0^\infty R^e\rho_e\,dR=1,\quad
\Sigma_e(R)=R^{-e}\int_0^R s^ef_0(s)\,ds
=-R^{-e}\int_R^\infty s^ef_0(s)\,ds.
\tag{S2.2}
\]
The prescribed smooth bump \(\rho_e\) has compact interior support in the shell and is independent of the auxiliary variable. Its chart representative includes the original radial moment normalization in (S2.2); any slow dependence of this representative is retained under differentiation and has the uniform bounds in R4 and M2. The equality of the two integrals follows from the exact zero total moment of \(f_0\). In the original correction it is the auxiliary average of the tangential residual that supplies \(f\); this is precisely why the input here is auxiliary independent. Its moment is retained as a separate mean defect, not discarded. Both formulas vanish outside the closed shell. They show \((\partial_R+e/R)\Sigma_e=f_0\), including its sign and radial weight.

Here is an explicit estimate for the edge integral used in original pages 104–105. For \(a>0\), \(M\ge0\), put \(p=(M-3)/2\) and \(v_0=a/\delta^2\). Substitution gives
\[
\int_0^\delta s^{-M}e^{-a/s^2}\,ds
=\tfrac12a^{(1-M)/2}\int_{v_0}^\infty v^pe^{-v}\,dv.
\tag{S2.3}
\]
For \(p\le0\), the final integral is at most \(v_0^pe^{-v_0}\). For \(p>0\) and \(v_0\ge2p\), write \(v=v_0+w\) and use \(\log(1+w/v_0)\le w/v_0\) to obtain \((v_0+w)^p\le v_0^pe^{w/2}\). Integration then gives at most \(2v_0^pe^{-v_0}\). Hence, in both cases for sufficiently small \(\delta>0\),
\[
\int_0^\delta s^{-M}e^{-a/s^2}\,ds
\le a^{-1}\delta^{3-M}e^{-a/\delta^2}.
\tag{S2.4}
\]
All fixed derivatives of \(e^{-a/s^2}\) are a finite linear combination of powers \(s^{-j}e^{-a/s^2}\) with \(0\le j\le3k\) at derivative order \(k\): differentiate each term, producing exponents \(j+1\) and \(j+3\), and induct. On \(0<s\le1\) this bounds them by \(C_{k,a}s^{-3k}e^{-a/s^2}\). The other edge factor and its derivatives are bounded in a sufficiently small collar and its value is bounded below positively there.

Use the forward integral in (S2.2) at the inner edge and the backward integral at the outer edge. The bump vanishes in both collars; all radial Jacobians and powers of \(R\) are bounded there. Equation (S2.4), after each allowed coefficient derivative, retains \(\zeta\delta^{-M'}\). Moving-boundary terms vanish because the integrand has every zero edge jet; equivalently differentiate its zero extension on a fixed half-line as in R4. In the remaining compact interior, \(\zeta\) is bounded below positively. Thus a source in \(\mathsf M_\mu\) yields \(\Sigma_e\in\mathsf M_\mu\), with smooth edge extension. The same reasoning applies to the two stress components with \(e=2,1\), respectively. C5 then proves the signed amplitude division and wave class \(\mathsf W_{\mu-1/2}\) at every derivative order. Those are coefficient bounds: one must retain the carrier exponential separately when differentiating an actual velocity field.

The common band set is unchanged by a radial path because \(q\) depends on \((z,t)\), which the path holds fixed. Temporal inversion and pulse propagation fix all slow coordinates. For each of the boundedly many active bands, a radial segment of bounded chart length meets at most \(C S_*^3\) radial mesh boxes: their chart widths are comparable to \(S_*^{-3}\). At fixed \((Z,T)\) there are boundedly many transverse/time mesh choices. Thus radial aggregation introduces at most a fixed polynomial factor in \(S_*\); any finite composition still has a finite polynomial factor. The common-torus degree differences depend on the bounded band range, not on the number of radial boxes. At a point, wave labels have bounded slow overlap and the disjoint auxiliary supports of W2. These facts justify the uniform-in-band estimates after aggregation.

## S3. Exact residual decomposition and every flat term

For the original viscosity define
\[
\mathscr R_\nu(u,p)=\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p.
\]
For any actual increment \((w,\pi)\), componentwise expansion gives exactly
\[
\mathscr R_\nu(u+w,p+\pi)=\mathscr R_\nu(u,p)
+\partial_tw-\nu\Delta w+\nabla\pi
+(u\cdot\nabla)w+(w\cdot\nabla)u+(w\cdot\nabla)w.
\tag{S3.1}
\]
All velocities in this equation are the full fields, including the curl remainders, compact-primitive remainders and earlier corrections. If \(\mathscr R_\nu(u,p)=\mathcal G+\mathcal F\), the old \(\mathcal F\) enters additively. It is a residual field, not an omitted part of \(u\).

The finite-stage split starts with the original base error \(\mathcal E_{B,\nu}\) in \(\mathcal F\), together with the generated pulse endpoint and primitive cutoff errors. P6 proves the exact pulse error \((1-\psi)f_m+\psi't_m\). On its support the Gaussian estimate gives, after any fixed physical derivative, \(C Q^{-M}S_*^B e^{-cS_*}\). Since \(S_*=\ell^2\), \(Q=2^{-\ell}\) and \(q\) is comparable to \(Q\),
\[
q^{-N}Q^{-M}S_*^B e^{-cS_*}
\le C_N\exp[-c\ell^2+(M+N)\ell\log2+2B\log\ell]\longrightarrow0.
\tag{S3.2}
\]
R5–R6 prove the exact primitive cutoff error is \(O(q^N)\) in every prescribed physical derivative, using finitely many extra coefficient derivatives for each prescribed \(N\). Thus a polynomial count of labels and finitely many error types at a fixed stage preserve these estimates: for the primitive bound first choose the power \(N+1\), and use the boundedness of \(S_*^Bq\); for the Gaussian use (S3.2) with the larger polynomial. Every fixed \(\nu>0\) has the unchanged factors in C9 and M2, so constants may depend on \(\nu\), but no viscosity is omitted.

The actual \(\mathcal E_B\) has the original all-order flat bound in Proposition 5.5 by [Z5](base-field-realization-audit.md); [I1](local-construction-assembly-audit.md) identifies that same base and residual in the chart construction. The proof here establishes that the subsequent operators preserve this supplied property and do not require any stronger uniform-in-stage version of it.

At each update expand (S3.1) first. Keep its newly identified endpoint errors and uncompensated primitive cutoff errors in \(\mathcal F\); all remaining terms form \(\mathcal G\) and have the supported coefficient estimates in S1–S2. Nonzero-harmonic Gaussian endpoint errors are not fed into a new forward pulse solve. A mean operation can cancel an explicit old flat mean term because the exact conservative residual includes it. If its actual residual change has the form \(-H+G_{\rm new}+F_{\rm new}\), where \(H\) is that canceled contribution of old \(\mathcal F\), the new split is exactly
\[
\mathcal G'=\mathcal G+G_{\rm new},\qquad
\mathcal F'=\mathcal F-H+F_{\rm new}.
\tag{S3.3}
\]
The compact-primitive estimates put this specific \(H\) in every required mean class and give its physical flat bounds. Thus subtraction preserves the finite-stage flat estimate. No inference that every physically flat function has every coefficient-class bound is needed. Formula (S3.3) prevents double counting a canceled contribution. The exact velocities remain unchanged by how their residual terms are assigned.

After each finite stage, therefore,
\[
\mathscr R_\nu(u^{[j]},p^{[j]})=\mathcal G^{[j]}+\mathcal F^{[j]},\qquad
|\mathcal F^{[j]}|_m\le C_{j,m,N,\nu}q^N
\tag{S3.4}
\]
for every fixed derivative order \(m\) and power \(N\). Its supported part has the finite locally supported harmonic expansion in S1, and its angular mean is in the mean class furnished by the actually applied estimates. This statement does not sum \(\mathcal F^{[j]}\) over infinitely many \(j\).

## S4. Exact mean equations after every update

Use the exact chart from M2, with the original viscosity retained by that map. Its representative has viscosity coefficient \(\varepsilon\). Write the full velocity as
\[
u_*=(b+\beta,V+v,G+\gamma)+w,\qquad \langle w\rangle_\theta=0,
\qquad W_{ab}=\langle w_aw_b\rangle_\theta.
\]
The base and mean correction are divergence free and every wave is an actual curl. Put
\(\Delta_0=D_r^2+R^{-1}D_r+D_z^2\) and
\(\mathfrak t_*=-\varepsilon\partial_T+c_i\mathcal N_i\).
To keep its role distinct from the signed increment of C5, denote the original base stress by
\(\Sigma^B=(\Sigma^B_\theta,\Sigma^B_z)=Q^{2A}\mathcal T_{\rm phys}\) at viscosity one; at the original viscosity its representative is \(\nu^{-1}Q^{2A}\mathcal T_{\rm phys,\nu}\). This is the full base stress of (5.41), not only its order-zero part.

The conservative transport identity follows directly from divergence zero. For example
\((D_r+R^{-1})(u_ru_\theta)+R^{-1}\partial_\theta(u_\theta^2)+D_z(u_zu_\theta)\)
equals the scalar transport of \(u_\theta\), because the extra factor multiplying \(u_\theta\) is the divergence. The cylindrical component equation additionally has \(u_ru_\theta/R\), giving \(D_r+2/R\). The same argument for \(u_r\) adds the centrifugal term \(-u_\theta^2/R\); for \(u_z\) there is no additional connection term. Hence the exact three transport components are
\[
\begin{split}
(u\cdot\nabla_*u)_r&=(D_r+R^{-1})u_r^2+R^{-1}\partial_\theta(u_\theta u_r)+D_z(u_zu_r)-u_\theta^2/R,\\
(u\cdot\nabla_*u)_\theta&=(D_r+2/R)(u_ru_\theta)+R^{-1}\partial_\theta(u_\theta^2)+D_z(u_zu_\theta),\\
(u\cdot\nabla_*u)_z&=(D_r+R^{-1})(u_ru_z)+R^{-1}\partial_\theta(u_\theta u_z)+D_z(u_z^2).
\end{split}
\tag{S4.1}
\]
Angular derivatives integrate to zero. Terms with exactly one factor of \(w\) have zero average; terms with two retain the entire \(W\). The cylindrical vector Laplacian has components
\(\Delta_{\rm sc}u_r-u_r/R^2-2\partial_\theta u_\theta/R^2\),
\(\Delta_{\rm sc}u_\theta-u_\theta/R^2+2\partial_\theta u_r/R^2\),
\(\Delta_{\rm sc}u_z\), where \(\Delta_{\rm sc}=\Delta_0+R^{-2}\partial_\theta^2\).
After averaging it is \(\Delta_0-R^{-2}\) on the first two components and \(\Delta_0\) on the third. These formulas follow by twice differentiating \(\partial_\theta e_r=e_\theta\), \(\partial_\theta e_\theta=-e_r\), retaining the two cross derivatives. Subtracting the pure base, whose nonflat tangential residual is minus the radial divergence of \(\Sigma^B\), now gives
\[
\begin{split}
g_r={}&-\mathfrak t_*\beta-(D_r+R^{-1})(2b\beta+\beta^2+W_{rr})
-D_z(b\gamma+G\beta+\beta\gamma+W_{zr})\\
&+(2Vv+v^2+W_{\theta\theta})/R+\varepsilon(\Delta_0-R^{-2})\beta,\\
E_\theta={}&\mathfrak t_*v+(D_r+2/R)(bv+V\beta+\beta v+W_{r\theta})
+D_z(Gv+V\gamma+\gamma v+W_{z\theta})\\
&-\varepsilon(\Delta_0-R^{-2})v-(D_r+2/R)\Sigma^B_\theta,\\
E_z={}&\mathfrak t_*\gamma+(D_r+1/R)(b\gamma+\beta G+\beta\gamma+W_{rz})
+D_z(2G\gamma+\gamma^2+W_{zz}+p_m)\\
&-\varepsilon\Delta_0\gamma-(D_r+1/R)\Sigma^B_z.
\end{split}
\tag{S4.2}
\]
These are original (8.3) with every term retained, on original page 89. Reconstruct the pressure after each update using the full new \(g_r\):
\[
\mathcal P=\int_0^\infty\langle g_r\rangle_Y\,dR,\qquad
\int_0^\infty\rho\,dR=1,\qquad
p_m=\mathsf T_0(g_r-\rho\mathcal P).
\tag{S4.3}
\]
The exact compact-primitive identity from R7 gives
\(D_rp_m-g_r=-\rho\mathcal P-\mathcal A_0(g_r-\rho\mathcal P)\).
Thus neither the radial defect nor the cutoff remainder is silently set to zero. The nonzero-harmonic pulse pressures and their endpoint residuals have zero angular average. Recalling the exact split (S3.4), we obtain at every finite stage
\[
\left\langle\mathcal G_*^{[j]}+\mathcal F_*^{[j]}-\mathcal E_{B,*}\right\rangle_\theta
=(D_rp_m^{[j]}-g_r^{[j]},E_\theta^{[j]},E_z^{[j]}),
\tag{S4.4}
\]
where all three physical residual representatives have the factor
\(\nu^{-1/2}Q^{2A+1/2}\). This is original (9.6) at \(\nu=1\), with its exact extension to every original viscosity. The pressure and flux derivatives in (S4.2) use the complete current state, so (S4.4) holds irrespective of whether a cancelable flat mean term is presently recorded in \(\mathcal F\).

## S5. What the finite induction establishes

At stage zero C1–C7 supply the primary amplitudes, supports, real curls and their covariance errors; S4 supplies the exact mean identities after pressure reconstruction. Suppose a finite list of operators has been applied. S1 handles each differential, pulse and wave-product operation, gives its finite harmonic set, and proves the next pulse source has its prescribed support. S2 handles each mean operation and its next auxiliary-independent signed stress input. S3 updates the full residual by equality and preserves the all-order physical flat bound. S4 recomputes pressure and the conservative means from the full new fields. This covers every operator listed in original Proposition 9.3 and proves its finite-stage closure by induction, with the source base's stated input properties left visible.

The step does not need a uniform bound over all stages, a numerical calculation or a new smallness threshold depending on the derivative order. The fixed pulse and cone thresholds are those in P1 and C3; estimates at a fixed stage may have larger finite constants. The [cycle audit](correction-cycle-audit.md), K0–K8, proves the initialization and original Propositions 9.5–9.6, including simultaneous exponent inequalities, accumulated-field hypotheses and the common finite-stage domain. The [physical derivative and realization audit](physical-realization-audit.md), L0–L7, derives the stage-independent derivative loss, exact potential summation, retained cutoff curls, full nonlinear residual comparison, one-sided endpoint limits and preservation of the exterior and inner fields. The actual leading profile and complete base field are supplied by [V0–V7](shear-realization-audit.md) and [Z0–Z8](base-field-realization-audit.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).
