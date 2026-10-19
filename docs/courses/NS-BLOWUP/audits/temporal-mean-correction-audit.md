# The temporal mean correction

The following construction proves original Lemma 8.6, (8.19)–(8.23), pages 95–96, and its mean-equation receiver in Step 3 of Proposition 9.6. The [radial construction](radial-primitive-audit/src/radial-primitives-and-compact-mean-corrections.md), R1–R8, supplies the preceding compact-primitive operators.

## T1. The exact inverse and its domain

The original torus is \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\), with Haar mass one. Retain
\[
J_g=\begin{pmatrix}3&1\\1&5\end{pmatrix},\quad
T_g=4+\sqrt2,\quad\Lambda_g=4-\sqrt2,\quad
v_t=(\sqrt2-1,1),\quad v_r=(1,1-\sqrt2),\quad
N=v_t\cdot\partial_y.
\tag{T1.1}
\]
For \(k\in\mathbb Z^2\setminus\{0\}\), let \(n=\max(|k_1|,|k_2|)\geq1\). Then
\[
(v_t\cdot k)((k_2-k_1)-\sqrt2k_1)
=(k_2-k_1)^2-2k_1^2\in\mathbb Z\setminus\{0\}.
\]
If this integer were zero, irrationality of \(\sqrt2\) would force \(k_1=0\), then \(k_2=0\). The conjugate's magnitude is at most \((2+\sqrt2)n\), proving
\[
|v_t\cdot k|^{-1}\leq(2+\sqrt2)n.
\tag{T1.2}
\]
For a smooth real or complex function \(F\) with \(\int_{\mathbb T^2}F=0\), define
\[
\widehat F(k)=\int_{[0,1]^2}F(y)e^{-2\pi i k\cdot y}\,dy,\qquad
\varphi(y)=\sum_{k\ne0}\frac{\widehat F(k)}{2\pi i\,v_t\cdot k}e^{2\pi i k\cdot y}.
\tag{T1.3}
\]
Let the \(C^m\) norm be the maximum of the suprema of all coordinate derivatives of total order at most \(m\). For a coordinate with \(|k_j|=n\), periodic integration by parts \(m+4\) times gives
\[
|\widehat F(k)|\leq\frac{\|F\|_{C^{m+4}}}{(2\pi n)^{m+4}}.
\]
For each derivative of order at most \(m\), its summand in (T1.3) is consequently bounded by
\((2+\sqrt2)(2\pi)^{-5}n^{-3}\|F\|_{C^{m+4}}\). Exactly \(8n\) integer vectors have maximum norm \(n\), and \(\sum_{n\geq1}n^{-2}\leq1+\int_1^\infty x^{-2}dx=2\). Hence all these differentiated series converge absolutely and uniformly and
\[
\|\varphi\|_{C^m}\leq\frac{16(2+\sqrt2)}{(2\pi)^5}\|F\|_{C^{m+4}}.
\tag{T1.4}
\]
Applying this at every \(m\) proves smoothness and termwise differentiation. The Fourier coefficients of \(N\varphi\) equal those of \(F\), including the zero coefficient. For completeness, equality of all Fourier coefficients determines a continuous function: its convolution with the product of the two Fejér kernels
\[
K_L(s)=\frac1{L+1}\left|\sum_{j=0}^{L}e^{2\pi ijs}\right|^2
\]
is the corresponding finite Fourier sum. The kernel is nonnegative and has integral one by orthogonality of the exponentials. Outside any fixed neighborhood of the integers it is at most \(((L+1)\sin^2(\pi\delta))^{-1}\), where \(\delta\) is the distance of that neighborhood's boundary to the integers. Uniform continuity therefore proves uniform convergence of the product-kernel convolution to the function: split the integral into the small neighborhood, where the function oscillation is small, and its complement, whose kernel mass tends to zero. A function with all coefficients zero is thus zero. This proves \(N\varphi=F\). If \(N\psi=0\), its nonzero Fourier coefficients vanish by (T1.2); requiring zero mean removes its constant coefficient. This proves uniqueness. For real \(F\), the coefficients at \(k\) and \(-k\) in (T1.3) are complex conjugates, so \(\varphi\) is real.

Thus (T1.3) is an actual map
\[
N^{-1}:C^\infty_0(\mathbb T^2)\longrightarrow C^\infty_0(\mathbb T^2),
\tag{T1.5}
\]
where the subscript denotes zero Haar mean, with the finite derivative bound (T1.4). It is not defined on a nonzero constant: integrating \(N\varphi=F\) proves the necessary condition \(\int F=0\). All slow and radial coefficient derivatives commute with this fixed Fourier multiplier. It acts at each fixed \((R,Z,T)\), so it preserves their support and smooth zero extensions. It need not preserve a subset of the auxiliary torus, and no such support condition is imposed on mean coefficients.

## T2. Original physical scaling and covering compatibility

Put \(P_iF(Y)=F(J_g^iY)\). The identity \(J_gv_t=T_gv_t\) gives, by differentiating the composition,
\[
N_{\rm abs}P_i=T_g^iP_iN_i,
\qquad N_{\rm abs}^{-1}P_i=T_g^{-i}P_iN_i^{-1}.
\tag{T2.1}
\]
For the inverse identity, the proposed right side is a zero-mean solution of the left side's defining equation, so uniqueness from T1 proves it. The covering preserves Haar mean: the pullback of the \(k\)-th exponential has frequency \((J_g^i)^Tk\), which is nonzero whenever \(k\ne0\), since \(\det J_g=14\). The identity follows first for trigonometric polynomials, then for smooth functions by their uniform Fourier convergence. No inverse of the many-to-one covering is used.

Retain the source's physical velocity and residual factors for its viscosity-one construction. The exact map to every original viscosity \(\nu>0\), including the force, physical coordinates and all moment multipliers, is proved in the mean-moment audit (M2.4)–(M2.7):
\[
u_*=Q^Au_{\rm phys},\qquad E_*=Q^{2A+1/2}E_{\rm phys},\quad
A=1/2+h,\quad Q=2^{-\ell},\quad \varepsilon=Q^h.
\]
The physical update is \(-N_{\rm abs}^{-1}E_{\rm phys}^\circ\), where \(E^\circ=E-\langle E\rangle_Y\). On a common torus \(y=J_g^{i_0}Y\), (T2.1) gives exactly
\[
Q^A[-N_{\rm abs}^{-1}E_{\rm phys}^\circ]
=-Q^{A-(2A+1/2)}T_g^{-i_0}N_{i_0}^{-1}E_*^\circ
=-c_{i_0}^{-1}N_{i_0}^{-1}E_*^\circ,
\quad c_{i_0}=T_g^{i_0}Q^{1+h}.
\tag{T2.2}
\]
The band integer is \(i=\lfloor\log_{T_g}(Q^{-1-h}/S_*)\rfloor\), with \(S_*=\ell^2\). Thus
\[
T_g^{-1}S_*^{-1}<T_g^iQ^{1+h}\leq S_*^{-1}.
\]
If the common index satisfies \(|i_0-i|\leq C_0\), the explicit bound is
\[
c_{i_0}^{-1}<T_g^{C_0+1}S_*.
\tag{T2.3}
\]
Indices and \(Q\) remain fixed during differentiation on a chart. The multiplier therefore costs a polynomial in \(S_*\) and four additional torus derivatives, not a power of \(\varepsilon\). Original common-torus compatibility (6.20), its bounded index difference, and (T2.1) prove agreement on overlaps of the same physical update.

Use the full \(\mathsf M_\alpha\) definition and original weights in mean-moment audit (M4.6). Haar averaging and subtraction preserve it. Applying (T1.4) after each fixed slow derivative, at each radial point, retains the factors \(\varepsilon^\alpha\zeta\delta^{-D_I}\). The weights have no auxiliary dependence, so they are unchanged by the torus supremum. Equations (T2.2)–(T2.3) therefore prove
\[
\Delta v=-c^{-1}N^{-1}E_\theta^\circ\in\mathsf M_\alpha,
\qquad\gamma_d=-c^{-1}N^{-1}E_z^\circ\in\mathsf M_\alpha.
\tag{T2.4}
\]
Both have zero auxiliary mean at every radial and slow point. The support, derivative and overlap conclusions also hold up to one-sided endpoints on any closed region \(q\geq c_0>0\). They require no target smallness and no stage-dependent reduction of the domain.

## T3. Compact realization, exact moments and the retained error

Use the original positive vector potential
\[
\Psi_*=\mathsf T_1\gamma_d,\qquad
\Delta\beta=-\varepsilon\partial_Z\Psi_*,\qquad
\Delta\gamma=(D_r+R^{-1})\Psi_*=\gamma_d-\mathcal A_1\gamma_d.
\tag{T3.1}
\]
The compact-primitive identity and estimates are proved in radial audit R3–R6 from original (8.4)–(8.8). Since \(\langle\gamma_d\rangle_Y=0\) at every radius, its required weighted mean integral is zero. The result is
\[
\Psi_*,\Delta\gamma\in\mathsf M_\alpha,\quad
\Delta\beta\in\mathsf M_{\alpha+1},\qquad
a=-\mathcal A_1\gamma_d.
\tag{T3.2}
\]
The complete \(a\) is part of the actual axial velocity. Here it need not vanish pointwise, unlike the auxiliary-independent moment correction.

Translation invariance of Haar measure gives \(\langle\mathcal I g\rangle=\int_0^R\langle g\rangle\,dR'\) and the corresponding identity for \(\mathcal J\); the torus translations in (8.5) do not affect the averages. Applied to \(g=R\gamma_d\), both averages are zero. The torus-independent cutoff and factor \(R^{-1}\) then give \(\langle\Psi_*\rangle=0\). Consequently \(\langle\Delta\beta\rangle=\langle\Delta\gamma\rangle=0\), and \(\langle\Delta v\rangle=0\) was already known. Both moments in (8.2) remain exactly unchanged. The full physical divergence vanishes because
\[
(D_r+R^{-1})(-\varepsilon\partial_Z\Psi_*)
+\varepsilon\partial_Z(D_r+R^{-1})\Psi_*=0:
\]
the coefficients of \(D_r\) depend only on \(R\) on a fixed chart. The azimuthal component is independent of \(\theta\). All components have the smooth shell zero extensions supplied by the compact inverse.

The operator \(N\) commutes with both translated radial integrals and their cutoff, since it is a constant derivative in the translation variable and the cutoff has no torus dependence. With \(c=c_{i_0}\), the exact fast-time equations are therefore
\[
cN\Delta v=-E_\theta^\circ,\qquad
cN\Delta\gamma=-E_z^\circ+\mathcal F_{\rm ax},\qquad
\mathcal F_{\rm ax}=cNa.
\tag{T3.3}
\]
For every fixed coefficient multi-index \(I\) and integer \(p\geq1\), the compact remainder estimate gives
\[
|\partial^I\mathcal F_{\rm ax}|
\leq C_{I,p}\varepsilon^{\alpha+p\kappa_s}S_*^{B_{I,p}}
\zeta\delta^{-D_{I,p}}.
\tag{T3.4}
\]
One additional torus derivative is enough to account for \(N\); multiplying by \(c\leq T_g^{C_0}S_*^{-1}\) changes no \(\varepsilon\) power. The physical chain rule has a finite loss for each fixed derivative, independent of \(p\). Choosing \(p\) large enough that \(hp\kappa_s\) exceeds that loss and the requested power, and only then taking \(q\) small, makes every physical derivative of \(\mathcal F_{\rm ax}\) of order \(O(q^L)\) for every prescribed \(L\). Polynomial logarithmic factors are absorbed by the strict exponent excess, as proved in radial audit R6. This proves flatness with the actual physical factors retained. It does not identify \(a\) or \(\mathcal F_{\rm ax}\) with zero.

## T4. The pressure and exact nonlinear receiver

Keep the base and actual wave velocity fixed. The complete radial source and defects are mean-moment audit (M5.2)–(M5.3). Its algebraic difference (M5.4) remains valid for this update, because that identity required no independence of the increments from \(Y\). Write again
\[
\Delta g_r=(2V/R)\Delta v+\mathcal R_g,
\qquad \Delta\mathcal P=\int\langle\Delta g_r\rangle_Y\,dR,
\qquad \Delta p_m=\mathsf T_0(\Delta g_r-\rho\Delta\mathcal P).
\tag{T4.1}
\]
This is the full pressure recomputation. Its cutoff error is retained by the exact identity
\[
D_r\Delta p_m-\Delta g_r=-\rho\Delta\mathcal P
-\mathcal A_0(\Delta g_r-\rho\Delta\mathcal P).
\tag{T4.2}
\]
Assume the incoming classes of the source's finite-state definition: \(v,\gamma\in\mathsf M_{0.9}\), \(\beta\in\mathsf M_{1.9}\), \(\alpha\geq0.9\). The source's fixed base has coefficient bounds \(b=O(\varepsilon S_*^B)\), \(V,G=O(S_*^B)\) on the enlarged shell. This step uses those bounds, whose global construction is an earlier audit component; it does not introduce a replacement base. Products add exponents with the full edge weights, since \(\zeta^2\leq\zeta\) and powers of \(\delta^{-1}\) add. The original radial operator loses at most \(\kappa_s\), \(D_z\) adds one, and the fast term \(cN\) has no \(\varepsilon\) loss, with a finite extra coefficient derivative.

For \(\mathcal R_g\) in (M5.4), the fast-time part of \(-\mathfrak t_*\Delta\beta\) has exponent \(\alpha+1\), its slow part has exponent \(\alpha+2\); the base-linear radial part has \(\alpha+2-\kappa_s\); the remaining radial products have \(\alpha+2.9-\kappa_s\) or \(2\alpha+2-\kappa_s\). The base-linear axial terms have \(\alpha+2\), the remaining axial terms \(\alpha+2.9\) or \(2\alpha+2\). The angular products have \(\alpha+0.9\) and \(2\alpha\). The viscous term has exponent at least \(\alpha+2-2\kappa_s\). All are at least \(\alpha+0.9\). Thus
\[
\mathcal R_g\in\mathsf M_{\alpha+0.9},\quad
\Delta g_r\in\mathsf M_\alpha,\quad
\Delta p_m\in\mathsf M_\alpha.
\tag{T4.3}
\]
The last conclusion uses the proved compact primitive after subtracting its actual moment, with \(\rho\Delta\mathcal P\) retained.

Unlike the moment solve, this temporal solve does not cancel the old three defects. Its base-linear changes have zero auxiliary average because \(V,G\) are slow and all increments have zero auxiliary mean. Expanding (M5.3) therefore gives the exact *changes*
\[
\begin{aligned}
\Delta\mathcal P&=\int\langle\mathcal R_g\rangle_Y\,dR,\\
\Delta\mathcal J_\theta&=\int R^2\langle\gamma\Delta v+v\Delta\gamma+\Delta\gamma\Delta v\rangle_Y\,dR,\\
\Delta\mathcal J_z&=\int R\langle2\gamma\Delta\gamma+(\Delta\gamma)^2\rangle_Y\,dR
-\frac12\int R^2\langle\mathcal R_g\rangle_Y\,dR.
\end{aligned}
\tag{T4.4}
\]
Their class is \(\mathsf S_{\alpha+0.9}\) by (T4.3), products and the full moment factors (M2.1)–(M2.3). Thus incoming defects of order \(\mathsf S_\alpha\) remain of that order. They are not assumed to vanish.

The full tangential differences are exactly (M7.3). Substituting (T3.3) into their time terms gives
\[
\begin{aligned}
E_{\theta,\rm new}-\langle E_\theta\rangle_Y
={}&-\varepsilon\partial_T\Delta v-\varepsilon(\Delta_0-R^{-2})\Delta v\\
&+(D_r+2/R)(b\Delta v+V\Delta\beta+\beta\Delta v+v\Delta\beta+\Delta\beta\Delta v)\\
&+D_z(G\Delta v+V\Delta\gamma+\gamma\Delta v+v\Delta\gamma+\Delta\gamma\Delta v),\\
E_{z,\rm new}-\langle E_z\rangle_Y
={}&-\varepsilon\partial_T\Delta\gamma-\varepsilon\Delta_0\Delta\gamma+\mathcal F_{\rm ax}\\
&+(D_r+1/R)(b\Delta\gamma+G\Delta\beta+\beta\Delta\gamma+\gamma\Delta\beta+\Delta\beta\Delta\gamma)\\
&+D_z(2G\Delta\gamma+2\gamma\Delta\gamma+(\Delta\gamma)^2+\Delta p_m).
\end{aligned}
\tag{T4.5}
\]
Every occurrence of \(\Delta\gamma\) means \(\gamma_d+a\). In particular all products with \(a\) remain. The slow time terms have exponent \(\alpha+1\); the radial base-linear fluxes \(\alpha+1-\kappa_s\); radial products with old means \(\alpha+1.9-\kappa_s\); radial new-new products \(2\alpha+1-\kappa_s\). Axial base-linear and pressure terms have \(\alpha+1\), the remaining axial products \(\alpha+1.9\) or \(2\alpha+1\). Viscosity has exponent at least \(\alpha+1-2\kappa_s\). Therefore
\[
E_{\theta,\rm new}-\langle E_\theta\rangle_Y\in\mathsf M_{\alpha+1-2\kappa_s},
\quad
E_{z,\rm new}-\langle E_z\rangle_Y-\mathcal F_{\rm ax}
\in\mathsf M_{\alpha+1-2\kappa_s}.
\tag{T4.6}
\]
This is precisely the mean improvement used in Step 3. With \(\alpha=H=C_*-2\kappa_s\) and the incoming averaged residual order \(C_*+0.17\), the new non-flat mean residual has order
\(\min(C_*+0.17,H+1-2\kappa_s)\); the actual axial field still contains the explicitly flat term. The moment update proved in M1–M8 can then be applied to the recomputed defects. The [wave-interaction audit](wave-interaction-audit.md), W5 and W7, proves the nonzero-harmonic receiver for this complete increment, including the actual axial cutoff remainder: it is an added wave source of order H with the same wave support and envelope. The [pulse inverse and actual linear residual](pulse-inverse-audit.md), P1–P8, are derived. The [stress covariance audit](stress-covariance-audit.md), C1–C9, supplies the positive primary amplitudes, signed linear inverse and actual curl covariance errors. The [source-containment audit](source-containment-audit.md), S1–S5, proves the finite-stage closure and exact conservative means. The [initialization and complete cycle audit](correction-cycle-audit.md), K0–K8, proves the actual four updates, their simultaneous gains, accumulated-field bounds and common finite-stage domain. The [physical derivative and realization audit](physical-realization-audit.md), L0–L7, derives the stage-independent derivative loss, exact potential summation, retained cutoff curls, full nonlinear residual comparison, one-sided endpoint limits and preservation of the exterior and inner fields. The actual leading profile and complete base field are supplied by [V0–V7](shear-realization-audit.md) and [Z0–Z8](base-field-realization-audit.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).

Source: [original PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), original pages 63–64 for phase definitions and divisor estimates, 90–93 for the radial inverse, 95–96 for this inverse, and 110 for its receiver. The [mean-moment audit](mean-moment-correction-audit.md), M1–M8, supplies the full original-coordinate row factors and nonlinear difference calculation. The operators proved here are used in the actual finite cycle [K0–K8](correction-cycle-audit.md) and local construction [I0–I7](local-construction-assembly-audit.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).


## Exact remainder, slow commutators and auxiliary averages

The [complete auxiliary-time derivation](auxiliary-time-correction-audit.md), TM7.7–TM7.16, proves the direct identity for the full axial remainder, both slow derivative commutators, the exact quadratic changes of every auxiliary-averaged equation, and their class bounds. TM5 supplies all original-viscosity factors. These consequences retain the actual compact velocity and pressure and propagate the averaged Step 3 bound without asserting an improved complete iteration rate.
