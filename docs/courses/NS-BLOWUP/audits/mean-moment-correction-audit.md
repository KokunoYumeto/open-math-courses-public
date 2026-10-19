# Compact mean-moment correction

The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md). This note proves the finite map in Lemma 8.7, the recomputed defects in Lemma 8.8, and their pressure and tangential-mean receivers.

The authority for the comparison is OpenAI, *Finite Time Blowup for Navier–Stokes*, original PDF, SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. The source passages are pages 34, 52, 56, 60, 63–64, 68–70, 89–100 and 110–111. The formulas below use the original positive potential and radial scale.

## M1. Original objects, maps and support

Retain
\[
0<h<1/100,\quad A=1/2+h,\quad D=1/2-h,\quad
1-t=q(1-\eta^2),\quad z=q^D\eta,\quad X=r^2/(2q),
\]
with \(q>0\), \(-1\leq\eta\leq1\). On a fixed dyadic chart put
\[
Q=2^{-\ell},\quad\varepsilon=Q^h,\quad S_*=\ell^2,\quad
R=r/\sqrt Q,\quad Z=z/Q^D,\quad T=(1-t)/Q,\quad \xi=q/Q.
\tag{M1.1}
\]
Here \(\xi\) ranges over a fixed positive compact interval. It is the original ratio, not a replacement for the physical variable. Its exact defining equation and its derivative are
\[
\xi-Z^2\xi^{2h}=T,\qquad
\partial_\xi(\xi-Z^2\xi^{2h})=1-2h\eta^2\geq1-2h>0,
\quad \eta=Z\xi^{-D}.
\tag{M1.2}
\]
Repeated implicit differentiation expresses every fixed derivative of \(\xi\) as a finite sum of products of derivatives of \(\xi-Z^2\xi^{2h}-T\), divided by powers of the displayed positive derivative. Since \(\xi\) and \(Z=\xi^D\eta\) range over compact sets, every such derivative is bounded. The same holds for \(\eta\), every fixed power of \(\xi\), and \(x=r/\sqrt q=R/\sqrt\xi\) on an annulus. This proves the coefficient bounds needed below, including one-sided bounds at \(\eta=\pm1\).

The reserved physical patch is \(x\in I_m=\{\sqrt{2X}:X\in\mathcal I_{\rm mean}\}\). On it the source prescribes, in (4.30) and (5.44),
\[
G_q=q^Au_{z,B}=0,\qquad
V_q=q^Au_{\theta,B}=a(\eta)x^{-1-2\lambda},\qquad
a(\eta)=2^{1/2+\lambda}c_{\rm patch}(1+\eta^2)^{-1},
\tag{M1.3}
\]
where \(\lambda>0\) and \(c_{\rm patch}>0\) are fixed. In particular
\[
2^{-1/2+\lambda}c_{\rm patch}\leq a(\eta)
\leq2^{1/2+\lambda}c_{\rm patch}.
\tag{M1.4}
\]
The factor \(2^{1/2+\lambda}\) is required because \(X=x^2/2\). There is no limit \(\lambda\downarrow0\) in this construction.

The support mechanism behind the exact patch identity is visible in (5.18): each positive-order \(E_n,U_n\) is supported to the left of the mean patch, and its zero axial integral makes \(F_n(X)=\int_0^X U_n(s)\,ds\) zero there as well. Its streamfunction is \(\mathcal S_n=q^{1-A+\lambda_n}F_n\), and its vector potential is \((\mathcal S_n/r)e_\theta\), as in (5.27). On the open mean patch both this potential and the azimuthal increment vanish identically. Multiplying by \(\chi(c_nq)\), then differentiating, still gives zero there: every product-rule term contains the vanished potential or one of its derivatives. Thus potential cutoffs cannot change (M1.3). This verifies preservation of the patch by the specified summation. The global leading-profile and positive-order constructions are supplied by V/D/Y/Z; [I3](local-construction-assembly-audit.md) verifies this map on their actual reserved interval.

The radial leading velocity is \(u_{r,B}=q^{-1/2}V_0(X,\eta)/\sqrt{2X}\). Consequently on the patch
\[
b=Q^Au_{r,B}=\varepsilon\xi^{-1/2}\frac{V_0(X,\eta)}x,
\qquad V=\xi^{-A}a(\eta)x^{-1-2\lambda},\qquad G=0.
\tag{M1.5}
\]
Every fixed derivative of the smooth fixed profile on a compact subinterval is bounded. Formula (M1.2) therefore gives \(|\partial^I b|\leq C_I\varepsilon\), \(|\partial^I V|+|\partial^I G|\leq C_I\) there. The larger allowed factors \(S_*^{B_I}\) in Lemma 8.8 are harmless. These bounds apply on the entire compact subinterval, not only on the bump supports.

## M2. Every radial measure and row factor

For any physical coefficient \(f_{\rm phys}\) with chart representative \(f_*=Q^{a_f}f_{\rm phys}\), substitution \(r=\sqrt Q R\), \(dr=\sqrt Q\,dR\), gives exactly
\[
\int R^e\langle f_*\rangle_Y\,dR
=Q^{a_f-(e+1)/2}\int r^e\langle f_{\rm phys}\rangle_Y\,dr.
\tag{M2.1}
\]
The Haar measure has total mass one. Both sides integrate the same auxiliary-independent quantity when no auxiliary variable occurs. In particular the five original rows have the following multipliers:

| Physical row | Multiplier for its \(Q\)-chart row |
|---|---|
| \(\int r^2\Delta v_{\rm phys}\,dr\) | \(Q^{A-3/2}\) |
| \(\int r\gamma_{d,\rm phys}\,dr\) | \(Q^{A-1}\) |
| \(\int (2V_{\rm phys}/r)\Delta v_{\rm phys}\,dr\) | \(Q^{2A}\) |
| \(\int r^2(G_{\rm phys}\Delta v_{\rm phys}+V_{\rm phys}\gamma_{d,\rm phys})\,dr\) | \(Q^{2A-3/2}\) |
| \(\int (2rG_{\rm phys}\gamma_{d,\rm phys}-rV_{\rm phys}\Delta v_{\rm phys})\,dr\) | \(Q^{2A-1}\) |

For the third row the factor \(1/r\) cancels the radial measure's \(\sqrt Q\), leaving the two velocity factors \(Q^{-2A}\). For the fourth row \(r^2dr\) contributes \(Q^{3/2}\); for the fifth \(rdr\) contributes \(Q\). This proves each nonzero factor separately, including its sign. The corresponding target multipliers are exactly (8.17):
\[
\mathcal P_*=Q^{2A}\mathcal P_{\rm phys},\quad
\mathcal J_{\theta,*}=Q^{2A-3/2}\mathcal J_{\theta,\rm phys},\quad
\mathcal J_{z,*}=Q^{2A-1}\mathcal J_{z,\rm phys}.
\tag{M2.2}
\]
The same identities with \(q\) in place of \(Q\) define the three inputs to the finite matrices:
\[
\mathcal P_q=\xi^{2A}\mathcal P_*,\quad
\mathcal J_{\theta,q}=\xi^{2A-3/2}\mathcal J_{\theta,*},\quad
\mathcal J_{z,q}=\xi^{2A-1}\mathcal J_{z,*}.
\tag{M2.3}
\]
No row uses another row's multiplier.

The equations being audited in Section 8 are the source's physical construction with viscosity one. The original target allows every fixed viscosity \(\nu>0\). Their exact connection retains the physical coordinates: from fields \((u_1,p_1,f_1)\) at viscosity one define
\[
y=x/\sqrt\nu,\qquad u_\nu(x,t)=\sqrt\nu\,u_1(y,t),\quad
p_\nu(x,t)=\nu p_1(y,t),\quad f_\nu(x,t)=\sqrt\nu f_1(y,t).
\tag{M2.4}
\]
Direct differentiation gives
\[
\partial_tu_\nu+(u_\nu\cdot\nabla_x)u_\nu-\nu\Delta_xu_\nu+\nabla_xp_\nu
=\sqrt\nu[\partial_tu_1+(u_1\cdot\nabla_y)u_1-\Delta_yu_1+\nabla_yp_1](y,t),
\qquad\operatorname{div}_xu_\nu=\operatorname{div}_yu_1.
\tag{M2.5}
\]
In particular this is an exact invertible map of equations with their forces, not a claim that a field solving them has already been constructed. Its inverse evaluates at \(x=\sqrt\nu y\) and divides the velocity and force by \(\sqrt\nu\), and the pressure by \(\nu\). Time, initial zero velocity, and the terminal time one are unchanged. A spatial support \(K\) becomes \(\sqrt\nu K\); a compact space–time force support is sent by the same spatial dilation. Smoothness follows from the invertible linear change. The norms satisfy \(\|u_\nu(t)\|_{L^2_x}^2=\nu^{5/2}\|u_1(t)\|_{L^2_y}^2\) and \(\|u_\nu(t)\|_\infty=\sqrt\nu\|u_1(t)\|_\infty\). The inverse sends a global smooth finite-uniform-energy competitor with the same data and force to one at viscosity one.

For the actual viscosity-\(\nu\) physical coordinates, write \(r_\nu,z_\nu\) and retain
\[
q_\nu-(z_\nu^2/\nu)q_\nu^{2h}=1-t,\quad
X_\nu=r_\nu^2/(2\nu q_\nu),\quad
R=r_\nu/\sqrt{\nu Q},\quad Z=z_\nu/(\sqrt\nu Q^D).
\tag{M2.6}
\]
These are precisely the pullbacks of the source coordinates; they are not \(q(r_\nu,z_\nu,t)\) with a suppressed factor. The corresponding chart factors are \(u_*=Q^A\nu^{-1/2}u_\nu\), \(g_*=Q^{2A+1/2}\nu^{-1/2}g_\nu\), \(p_*=Q^{2A}\nu^{-1}p_\nu\). A vector potential has \(\Psi_\nu(x,t)=\nu\Psi_1(y,t)\), giving \(\Psi_*=Q^{A-1/2}\nu^{-1}\Psi_\nu\). Each of the five multipliers in the table above acquires, in its displayed row order, the factors
\[
\nu^{-2},\quad\nu^{-3/2},\quad\nu^{-1},\quad\nu^{-5/2},\quad\nu^{-2}.
\tag{M2.7}
\]
To check them, use \(dr_\nu=\sqrt\nu\,dr_1\), each velocity factor \(\sqrt\nu\), and each radial factor \(r_\nu=\sqrt\nu r_1\). The third row has two velocities and one inverse radius followed by the radial measure, hence scales by \(\nu\). The fourth has two velocities and \(r_\nu^2dr_\nu\), hence \(\nu^{5/2}\); the fifth has two velocities and \(r_\nu dr_\nu\), hence \(\nu^2\). Its radial-source contribution scales by the same \(\nu^2\), since \(g_\nu=\sqrt\nu g_1\). The first two rows follow from one velocity factor. Also \(c_{\rho,*}=(\nu Q)^{-1}c_{\rho,\nu}\) for \(\rho_\nu(r_\nu)=\nu^{-1/2}\rho_1(r_\nu/\sqrt\nu)\). This accounts for the arbitrary-viscosity target without discarding any factor from the source's audited equations.

## M3. Construction and exact inverse of the five-profile map

Choose \(0<L<U\) with \([L,U]\subset I_m\). Set \(d=\log(U/L)/8\), \(x_0=Le^{2d}\), \(\sigma=d/4\), and
\[
\eta_0(x)=
\begin{cases}
\exp[-1/(\sigma^2-\log^2(x/x_0))],&|\log(x/x_0)|<\sigma,\\
0,&\text{otherwise},
\end{cases}
\quad
a_j=e^{jd},\quad\eta_j(x)=a_j^{-1}\eta_0(x/a_j),\quad j=0,1,2.
\tag{M3.1}
\]
The letter \(\eta_j\) here denotes the source's bump profiles, not the slow coordinate \(\eta\). The exponent's derivatives produce only finite powers of the positive denominator; \(e^{-1/s}s^{-N}\to0\) as \(s\downarrow0\) for every \(N\). One proof is \(e^{1/s}\geq s^{-m}/m!\) with \(m>N\). Thus these are smooth zero extensions. Their logarithmic supports are centered at \(\log L+(2+j)d\) and have half-width \(d/4\); they are disjoint and their closed hull
\[
K=[x_0e^{-\sigma},x_0e^{2d+\sigma}]
\tag{M3.2}
\]
lies in \((L,U)\). For every real \(p\), define the positive, finite exact constant
\[
\mu_p=\int_0^\infty x^p\eta_0(x)\,dx>0.
\]
Changing variables \(x=a_js\) gives
\[
\int_0^\infty x^p\eta_j(x)\,dx=\mu_p e^{jdp}.
\tag{M3.3}
\]
All moments remain these exact integrals; no numerical values are needed.

Using the original \(a=a(\eta)\), define the matrices exactly as on original page 98:
\[
A_\theta=
\begin{pmatrix}
\mu_2&\mu_2e^{2d}&\mu_2e^{4d}\\
2a\mu_{-2-2\lambda}&2a\mu_{-2-2\lambda}e^{d(-2-2\lambda)}&2a\mu_{-2-2\lambda}e^{2d(-2-2\lambda)}\\
-a\mu_{-2\lambda}&-a\mu_{-2\lambda}e^{-2d\lambda}&-a\mu_{-2\lambda}e^{-4d\lambda}
\end{pmatrix},\qquad
A_z=\begin{pmatrix}\mu_1&\mu_1e^d\\
a\mu_{1-2\lambda}&a\mu_{1-2\lambda}e^{d(1-2\lambda)}\end{pmatrix}.
\tag{M3.4}
\]
For explicit determinants put \(z_0=e^{2d}\), \(z_1=e^{d(-2-2\lambda)}\), \(z_2=e^{-2d\lambda}\), \(y_0=e^d\), \(y_1=e^{d(1-2\lambda)}\). Then
\[
\det A_\theta=-2a^2\mu_2\mu_{-2-2\lambda}\mu_{-2\lambda}
(z_1-z_0)(z_2-z_0)(z_2-z_1),
\]
\[
\det A_z=a\mu_1\mu_{1-2\lambda}(y_1-y_0).
\tag{M3.5}
\]
To verify the first determinant, factor the three displayed row factors from (M3.4), subtract its first remaining row from the other two, and factor \(z_i-z_0\). The residual two-by-two determinant is \((z_2+z_0)-(z_1+z_0)=z_2-z_1\). The second determinant follows by expanding its two products. For \(\lambda>0\), \(z_1<z_2<1<z_0\) and \(y_1<y_0\). Every factor is therefore nonzero. Formula (M1.4) gives lower bounds on the determinant magnitudes uniform in the slow point and band. Constants can depend on the fixed \(\lambda,d,\eta_0,c_{\rm patch}\).

Here is the full inverse without an unevaluated matrix inversion. Define polynomials \(U(t)=u_0+u_1t+u_2t^2\) and \(S(t)=s_0+s_1t\) by
\[
U(t)=-\frac{\mathcal P_q}{2a\mu_{-2-2\lambda}}
\frac{(t-z_0)(t-z_2)}{(z_1-z_0)(z_1-z_2)}
+\frac{\mathcal J_{z,q}}{a\mu_{-2\lambda}}
\frac{(t-z_0)(t-z_1)}{(z_2-z_0)(z_2-z_1)},
\tag{M3.6}
\]
\[
S(t)=-\frac{\mathcal J_{\theta,q}}{a\mu_{1-2\lambda}}
\frac{t-y_0}{y_1-y_0}.
\tag{M3.7}
\]
Evaluating these polynomials at their three or two nodes verifies every row of
\[
A_\theta u=(0,-\mathcal P_q,-\mathcal J_{z,q})^T,
\qquad A_zs=(0,-\mathcal J_{\theta,q})^T.
\tag{M3.8}
\]
Their coefficient vectors are the unique vectors solving these systems, because the determinants are nonzero. This uniqueness is within the specified five-profile space, not among all compactly supported velocity fields.

Set, in physical variables,
\[
\Delta v_{\rm phys}=q^{-A}\sum_{j=0}^2u_j\eta_j(r/\sqrt q),
\qquad \gamma_{d,\rm phys}=q^{-A}\sum_{j=0}^1s_j\eta_j(r/\sqrt q).
\tag{M3.9}
\]
The five integrals of these fields are exactly the five rows of (M3.8): the angular block tests powers \(2,-2-2\lambda,-2\lambda\) with factors \(1,2a,-a\), and the axial block tests \(1,1-2\lambda\) with factors \(1,a\). Section M2 then gives, in every fixed chart,
\[
\begin{gathered}
\int R^2\Delta v\,dR=0,\qquad\int R\gamma_d\,dR=0,\\
\int(2V/R)\Delta v\,dR=-\mathcal P,\\
\int R^2(G\Delta v+V\gamma_d)\,dR=-\mathcal J_\theta,\\
\int(2RG\gamma_d-RV\Delta v)\,dR=-\mathcal J_z.
\end{gathered}
\tag{M3.10}
\]
Here and below unsuffixed fields and targets are the \(Q\)-chart representatives. The terms containing \(G\) are retained: their vanishing in this solve follows from the exact patch value (M1.3).

## M4. The actual compact potential and coefficient estimates

Define
\[
H_j(x)=\int_0^x s\eta_j(s)\,ds,\qquad H(x,z,t)=\sum_{j=0}^1s_j(z,t)H_j(x),
\qquad \Psi_{\rm phys}=q^{1/2-A}\frac{H(r/\sqrt q,z,t)}{r/\sqrt q}.
\tag{M4.1}
\]
Below \(K\), both \(H_j\) vanish. Above \(K\), their sum is
\(\mu_1(s_0+e^ds_1)=0\), by the first row of \(A_z\). Hence \(H\), and therefore \(\Psi\), vanish outside the whole closed hull \(K\). They can be nonzero between the two axial bump supports. This entire hull is contained in the reserved patch. Slow derivatives preserve that support: the constant expression beyond the hull is identically zero as a function of the slow variables, so all its derivatives vanish there as well.

The original positive potential gives the physical velocity
\[
\Delta\beta_{\rm phys}=-\partial_z\Psi_{\rm phys},\qquad
\Delta\gamma_{\rm phys}=(\partial_r+r^{-1})\Psi_{\rm phys}=\gamma_{d,\rm phys}.
\tag{M4.2}
\]
The last identity follows from \(H_x=x\sum s_j\eta_j(x)\) and \(\partial_rx=q^{-1/2}\), with \(q,z,t\) held in their indicated roles. It is exact; no radial cutoff remainder survives. Indeed the full weighted integral \(\int r\gamma_{d,\rm phys}\,dr\) is zero, and the source is independent of the auxiliary variable, so the subtracted full radial integral in (8.4) vanishes identically.

For clarity the slow differentiation in the radial component retains both the changing scale and the changing coefficients. At fixed \(r,t\),
\[
\partial_z\Psi_{\rm phys}=q^{1/2-A}
\left[
\sum_{j=0}^1(\partial_zs_j)\frac{H_j(x)}x
+\frac{q_z}{q}\left\{(1/2-A)\frac{H(x)}x
-\frac x2\partial_x\left(\frac{H(x)}x\right)\right\}
\right],\qquad q_z=\frac{2\eta q^{1-D}}{1-2h\eta^2}.
\tag{M4.3}
\]
In the first sum only the coefficient is differentiated. This formula includes every term from \(x_z=-xq_z/(2q)\); dropping it would change the actual velocity.

The chart potential is
\[
\Psi_*=Q^{A-1/2}\Psi_{\rm phys}
=\xi^{1/2-A}\frac{H(R/\sqrt\xi,z,t)}{R/\sqrt\xi},\quad
\Delta\beta=-\varepsilon\partial_Z\Psi_*,\quad
\Delta\gamma=(\partial_R+R^{-1})\Psi_*.
\tag{M4.4}
\]
Consequently
\[
(\partial_R+R^{-1})\Delta\beta+\varepsilon\partial_Z\Delta\gamma=0
\tag{M4.5}
\]
by commuting \(\partial_Z\) with \(\partial_R+R^{-1}\). The angular field \(\Delta v e_\theta\) is divergence-free because it is independent of \(\theta\). All fields vanish near the axis for each \(q>0\), so their cylindrical expressions have smooth Cartesian zero extensions there. Both original radial moments remain exactly zero after addition to a state satisfying (8.2).

Use the original classes (6.23)–(6.25):
\[
\zeta(X)=\exp\left[-\frac{a_a}{\log^2(X/X_a)}-\frac{a_b}{\log^2(X_b/X)}\right],\quad
\delta(X)=\min\{1,\log(X/X_a),\log(X_b/X)\},
\]
\[
|\partial^If|\leq C_I\varepsilon^\alpha S_*^{B_I}\zeta\delta^{-D_I}
\quad(f\in\mathsf M_\alpha),\qquad
|\partial_{Z,T}^IF|\leq C_I\varepsilon^\alpha S_*^{B_I}
\quad(F\in\mathsf S_\alpha).
\tag{M4.6}
\]
The \(\mathsf M\) functions have smooth shell zero extensions and common-torus compatibility. The derivative indices in \(\mathsf M\) run over all five coefficient variables. For this correction all auxiliary derivatives vanish.

By (M2.3), the three \(q\)-targets inherit every \(\mathsf S_\alpha\) estimate from the chart targets. The explicit coefficients in (M3.6)–(M3.7) are fixed multiples of these targets and of \(1/a=(1+\eta^2)/(2^{1/2+\lambda}c_{\rm patch})\). Every fixed slow derivative has the same \(\varepsilon^\alpha\) factor, by (M1.2) and the product rule. The chart velocities are \(\xi^{-A}\sum u_j\eta_j(R/\sqrt\xi)\) and \(\xi^{-A}\sum s_j\eta_j(R/\sqrt\xi)\). Their derivatives and those of (M4.4) have that same factor. On the fixed compact \(X\)-set \(K^2/2\), both \(\zeta\) and \(\delta\) have positive lower bounds; outside it the corrections vanish smoothly. Thus the full weighted bounds are
\[
\Delta v,\Delta\gamma,\Psi_*\in\mathsf M_\alpha,
\qquad \Delta\beta\in\mathsf M_{\alpha+1}.
\tag{M4.7}
\]
The slow support of the target functions is preserved because the operation uses their values and derivatives at the same \((z,t)\). It does not change \(q\), hence creates no new dyadic band. The physical definitions (M3.9), (M4.1) are independent of a chart: uniqueness of (M3.8), together with the exact row factors, proves agreement on chart overlaps. The fields have no auxiliary dependence, so every integer covering pulls them back to themselves. All arguments preserve one-sided source derivatives on closed sets \(q\geq c>0\), including \(\eta=\pm1\). No smallness of the three target values is needed to define this linear map, and no stage-dependent domain reduction is used.

## M5. Complete nonlinear recomputation

Keep the actual base \((b,V,G)\) and full wave field \(w\) fixed. Write \(W_{ab}=\langle w_aw_b\rangle_\theta\). The old means \((\beta,v,\gamma)\) may depend on the auxiliary torus. With
\[
D_r=\partial_R+Md_rR^{d_r-1}\mathcal L,\quad
D_z=\varepsilon\partial_Z,\quad
\mathfrak t_*=-\varepsilon\partial_T+c\mathcal N,\quad
\Delta_0=D_r^2+R^{-1}D_r+D_z^2,
\tag{M5.1}
\]
the original radial source, including its complete covariance, is
\[
g_r=-\mathfrak t_*\beta-(D_r+R^{-1})(2b\beta+\beta^2+W_{rr})
-D_z(b\gamma+G\beta+\beta\gamma+W_{zr})
+(2Vv+v^2+W_{\theta\theta})/R
+\varepsilon(\Delta_0-R^{-2})\beta.
\tag{M5.2}
\]
Here \(M=\Lambda_g^{i_0}Q^{d_r/2}\), \(\mathcal L=v_r\cdot\partial_y\), \(c=T_g^{i_0}Q^{1+h}\), \(\mathcal N=v_t\cdot\partial_y\), with all original phase data fixed on a chart. The radial correction audit proves \(M\leq C\varepsilon^{-\kappa_s}S_*^{-\rho_g}\), \(\kappa_s=10^{-5}\), at the fixed common index. Every fixed derivative of its \(R\)-coefficient obeys the same bound on the patch. Only this precise radial loss is used below.

The exact old defects are
\[
\mathcal P=\int\langle g_r\rangle_Y\,dR,\quad
\mathcal J_\theta=\int R^2\langle Gv+V\gamma+\gamma v+W_{z\theta}\rangle_Y\,dR,
\]
\[
\mathcal J_z=\int R\langle2G\gamma+\gamma^2+W_{zz}\rangle_Y\,dR
-\frac12\int R^2\langle g_r\rangle_Y\,dR.
\tag{M5.3}
\]
Apply (M3.9)–(M4.4) to these actual defects, and form the new fields by addition of all three actual velocity increments. Define \(\mathcal R_g=g_{r,\rm new}-g_r-(2V/R)\Delta v\). Expanding each product in (M5.2) yields exactly
\[
\begin{aligned}
\mathcal R_g={}&-\mathfrak t_*\Delta\beta
-(D_r+R^{-1})(2b\Delta\beta+2\beta\Delta\beta+(\Delta\beta)^2)\\
&-D_z(b\Delta\gamma+G\Delta\beta+\beta\Delta\gamma
+\gamma\Delta\beta+\Delta\beta\Delta\gamma)\\
&+(2v\Delta v+(\Delta v)^2)/R
+\varepsilon(\Delta_0-R^{-2})\Delta\beta.
\end{aligned}
\tag{M5.4}
\]
For instance, the two quadratic radial terms subtract to \(2\beta\Delta\beta+(\Delta\beta)^2\), and the mixed term subtracts to \(\beta\Delta\gamma+\gamma\Delta\beta+\Delta\beta\Delta\gamma\). The time and viscous operators are linear. Every \(W\) term cancels because the wave velocity has been held fixed, including its curl remainders; none has been approximated.

Integrating (M5.4) and using the third row of (M3.10) gives \(\mathcal P_{\rm new}=\mathcal P-\mathcal P+\int\langle\mathcal R_g\rangle\). Expanding \(\mathcal J_\theta\), its change linear in the base is precisely the fourth row. Expanding \(\mathcal J_z\), its base-linear part is the fifth row, since
\(-\tfrac12R^2(2V/R)\Delta v=-RV\Delta v\). The remaining terms are therefore
\[
\begin{aligned}
\mathcal P_{\rm new}&=\int\langle\mathcal R_g\rangle_Y\,dR,\\
\mathcal J_{\theta,\rm new}&=\int R^2\langle\gamma\Delta v+v\Delta\gamma+\Delta\gamma\Delta v\rangle_Y\,dR,\\
\mathcal J_{z,\rm new}&=\int R\langle2\gamma\Delta\gamma+(\Delta\gamma)^2\rangle_Y\,dR
-\frac12\int R^2\langle\mathcal R_g\rangle_Y\,dR.
\end{aligned}
\tag{M5.5}
\]
These are (8.26)–(8.27), with every quadratic term retained and \(\Delta\gamma=\gamma_d\) established for the actual compact potential.

## M6. Derivative estimates, including the local underclaim

Use the original iteration bounds \(v,\gamma\in\mathsf M_{0.9}\), \(\beta\in\mathsf M_{1.9}\), and targets in \(\mathsf S_\alpha\) with \(\alpha\geq0.9\). All products in (M5.4) are supported in the fixed compact patch hull. There the edge factors in (M4.6) are bounded above and below. The product rule consequently adds the two class exponents, coefficient differentiation preserves them, multiplication by \(R^{-j}\) preserves them, and \(D_z\) adds one. Applying \(D_r\) to a function that depends on \(y\) loses at most \(\kappa_s\), by the full formula (M5.1). Applying it to a function independent of \(y\) is exactly \(\partial_R\), with no loss. These statements hold after every fixed coefficient derivative by the finite product rule and the derivative bounds on the coefficients of (M5.1).

Every new increment and each base coefficient is independent of \(y\). In particular \(\mathfrak t_*\Delta\beta=-\varepsilon\partial_T\Delta\beta\), and \(\Delta_0\Delta\beta=(\partial_R^2+R^{-1}\partial_R+\varepsilon^2\partial_Z^2)\Delta\beta\). The following table includes every term of (M5.4):

| Term, with its displayed derivative | Class exponent at least |
|---|---|
| \(-\mathfrak t_*\Delta\beta\) | \(\alpha+2\) |
| \((D_r+R^{-1})(2b\Delta\beta)\) | \(\alpha+2\) |
| \((D_r+R^{-1})(2\beta\Delta\beta)\) | \(\alpha+2.9-\kappa_s\) |
| \((D_r+R^{-1})(\Delta\beta)^2\) | \(2\alpha+2\) |
| \(D_z(b\Delta\gamma)\) | \(\alpha+2\) |
| \(D_z(G\Delta\beta)\) | \(\alpha+2\) |
| \(D_z(\beta\Delta\gamma)\) | \(\alpha+2.9\) |
| \(D_z(\gamma\Delta\beta)\) | \(\alpha+2.9\) |
| \(D_z(\Delta\beta\Delta\gamma)\) | \(2\alpha+2\) |
| \(2v\Delta v/R\) | \(\alpha+0.9\) |
| \((\Delta v)^2/R\) | \(2\alpha\) |
| \(\varepsilon(\partial_R^2+R^{-1}\partial_R-R^{-2})\Delta\beta\) | \(\alpha+2\) |
| \(\varepsilon^3\partial_Z^2\Delta\beta\) | \(\alpha+4\) |

All exponents are at least \(\alpha+0.9\): the possibly smaller comparisons reduce to \(2\alpha\geq\alpha+0.9\) and \(2.9-\kappa_s>0.9\). For \(0<\varepsilon\leq1\), a larger exponent gives the required bound with the smaller exponent without changing the constant. Thus this exact map satisfies the stronger local conclusion
\[
\mathcal R_g\in\mathsf M_{\alpha+0.9},\qquad
(\mathcal P_{\rm new},\mathcal J_{\theta,\rm new},\mathcal J_{z,\rm new})
\in\mathsf S_{\alpha+0.9}.
\tag{M6.1}
\]
For the second assertion, each product in (M5.5) has exponent at least \(\alpha+0.9\). Radial integration has bounded length and bounded \(R,R^2\) factors on the patch. Each fixed slow derivative can be passed under the integral after the smooth zero extension, on a common compact radial interval. Haar averaging has operator norm one. These facts prove the \(\mathsf S\) bounds with no hidden radial-measure factor; the physical factors are precisely M2.

The original assertion \(\mathsf M_{\alpha+0.9-2\kappa_s}\), \(\mathsf S_{\alpha+0.9-2\kappa_s}\) therefore follows. The stronger conclusion uses the same hypotheses and the already stated auxiliary independence, not an added smallness condition. It is a local sharpening of this step, not a claim of a stronger blowup theorem or a novelty claim. The old field bounds are preserved after addition because \(\alpha\geq0.9\) and \(\alpha+1\geq1.9\); constants may depend on the fixed finite stage.

## M7. Pressure and the full tangential-mean receiver

Let the unchanged bump \(\rho\) satisfy \(\int\rho\,dR=1\), and use the original compact operator \(\mathsf T_0\). Set \(p_m=\mathsf T_0(g_r-\rho\mathcal P)\) at both states. Linearity and (M5.5) give the full pressure change
\[
\Delta p_m=
\mathsf T_0\bigl((2V/R)\Delta v+\rho\mathcal P\bigr)
+\mathsf T_0\bigl(\mathcal R_g-\rho\mathcal P_{\rm new}\bigr).
\tag{M7.1}
\]
Both sources have zero radial auxiliary-mean integral. The first is auxiliary independent, so its cutoff remainder is identically zero. The second may depend on the torus; its cutoff remainder must remain in the actual radial residual. The exact radial identity is
\[
D_r\Delta p_m-(g_{r,\rm new}-g_r)
=-\rho(\mathcal P_{\rm new}-\mathcal P)
-\mathcal A_0\bigl(\mathcal R_g-\rho\mathcal P_{\rm new}\bigr).
\tag{M7.2}
\]
The all-order compact-primitive estimates in original Lemma 8.2, independently derived in the radial audit R3–R6, apply to both sources. The first belongs to \(\mathsf M_\alpha\), and the second to \(\mathsf M_{\alpha+0.9}\); hence \(\Delta p_m\in\mathsf M_\alpha\). The retained \(\mathcal A_0\) term has all physical derivatives flat at \(q=0\) by the weighted-mean condition and that lemma. It has not been set to zero or removed from future products. The compact-primitive estimates supply the bound used here.

Subtracting the first two equations of original (8.3), while keeping the entire wave covariance and stress fixed, gives
\[
\begin{aligned}
\Delta E_\theta={}&\mathfrak t_*\Delta v
+(D_r+2/R)(b\Delta v+V\Delta\beta+\beta\Delta v+v\Delta\beta+\Delta\beta\Delta v)\\
&+D_z(G\Delta v+V\Delta\gamma+\gamma\Delta v+v\Delta\gamma+\Delta\gamma\Delta v)
-\varepsilon(\Delta_0-R^{-2})\Delta v,\\
\Delta E_z={}&\mathfrak t_*\Delta\gamma
+(D_r+1/R)(b\Delta\gamma+G\Delta\beta+\beta\Delta\gamma+\gamma\Delta\beta+\Delta\beta\Delta\gamma)\\
&+D_z(2G\Delta\gamma+2\gamma\Delta\gamma+(\Delta\gamma)^2+\Delta p_m)
-\varepsilon\Delta_0\Delta\gamma.
\end{aligned}
\tag{M7.3}
\]
For both lines the time and viscous terms have exponent at least \(\alpha+1\), because the increments are auxiliary independent. The base-linear radial terms have exponent \(\alpha+1\) and no fast radial loss. The radial products involving old means have exponent at least \(\alpha+1.9-\kappa_s\). The new-new radial products have exponent \(2\alpha+1\). The base-linear axial terms and the pressure term have exponent at least \(\alpha+1\); the remaining axial products have exponents \(\alpha+1.9\) or \(2\alpha+1\). Since \(\alpha\geq0.9\), every one is at least \(\alpha+1\). Therefore
\[
\Delta E_\theta,\Delta E_z\in\mathsf M_{\alpha+1}.
\tag{M7.4}
\]
The pressure term can extend farther within the active shell than the compact patch hull. Its bound uses the full weighted primitive estimate, and \(D_z=\varepsilon\partial_Z\) preserves that estimate with the extra factor \(\varepsilon\). All other terms are patch supported. This distinction ensures (M7.4) does not incorrectly assume that the pressure has the same support as the velocity bumps.

Finally the axial integrated residual is \(\varepsilon\partial_Z(\mathcal J_z+c_\rho\mathcal P)\), not \(\varepsilon\partial_Z\mathcal J_z\) alone. The fixed physical bump is \(\rho_{\rm phys}=q^{-1/2}\widehat\rho(r/\sqrt q)\), so
\[
c_{\rho,*}=\frac12\int R^2\rho_*\,dR
=\frac{q}{2Q}\int x^2\widehat\rho(x)\,dx.
\tag{M7.5}
\]
Its fixed slow derivatives are bounded by (M1.2). Thus the new axial integrated residual is in \(\mathsf S_{\alpha+1.9}\) with its complete product derivative retained. The angular integrated residual \(\varepsilon\partial_Z\mathcal J_{\theta,\rm new}\) has the same bound. These conclusions include every physical multiplier in M2 and the \(q/Q\) factor in (M7.5).

## M8. What this closes and what comes next

The original five-profile solve, compact potential, exact nonlinear defect recomputation, and its pressure and tangential-mean changes are proved above. The local sharpening (M6.1) follows without modifying the source's map. At the fourth step of Proposition 9.6, the source sets \(\alpha=H=C_*-2\kappa_s\). Thus this map gives defects of order \(H+0.9=C_*+0.9-2\kappa_s\), which implies the source's order \(C_*+0.9-4\kappa_s\); (M7.4) gives tangential changes of order \(H+1\), implying its weaker estimate. M6 alone does not determine the complete cycle gain. The [cycle audit](correction-cycle-audit.md), K6–K7, propagates this exact remainder through all four steps and proves a common gain of 17999/100000, keeping the original state definitions.

The global base and its receiving compatibility are proved in [Z0–Z8](base-field-realization-audit.md) and [I1–I3](local-construction-assembly-audit.md). The actual preceding operations in [K3–K6](correction-cycle-audit.md) supply the incoming state. The effects of this full mean change on nonzero angular harmonics are derived in the [wave-interaction audit](wave-interaction-audit.md), W5 and W7: the exact receiver is (W7.3), with an added wave source of order H and the original support and envelope retained. The [pulse inverse and actual linear residual](pulse-inverse-audit.md), P1–P8, are derived with the original source coefficients. The [stress covariance audit](stress-covariance-audit.md), C1–C9, supplies the positive primary amplitudes, signed linear inverse and actual curl covariance errors. The [source-containment audit](source-containment-audit.md), S1–S5, proves the finite-stage closure and exact conservative means. The [initialization and complete cycle audit](correction-cycle-audit.md), K0–K8, proves the actual four updates, their simultaneous gains, accumulated-field bounds and common finite-stage domain. The [physical derivative and realization audit](physical-realization-audit.md), L0–L7, derives the stage-independent derivative loss, exact potential summation, retained cutoff curls, full nonlinear residual comparison, one-sided endpoint limits and preservation of the exterior and inner fields. The actual leading profile and complete base field are supplied by [V0–V7](shear-realization-audit.md) and [Z0–Z8](base-field-realization-audit.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md). The [temporal mean inverse and its actual compact axial correction](temporal-mean-correction-audit.md) are proved in the companion construction, T1–T4, using original pages 95–96 and the third step of the cycle. The supplied V/D/Y/Z constructions retain the original reserved patches and moment data; I1–I3 proves their exact use by this correction map.

Original source: [paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), (4.30), (5.18), (5.27), (5.44), (6.23)–(6.26), (8.3), (8.14)–(8.17), (8.24)–(8.27). The derivations receiving and supplying this construction are the retained [radial-primitive audit](radial-primitive-audit/src/radial-primitives-and-compact-mean-corrections.md), R1–R8, and the earlier [coordinate and summation proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/NS-BLOWUP/src/summing-the-correction-fields.md), S1. The full theorem follows from the linked constructions and final comparison argument.


## Full finite-map formulas

The [complete five-profile derivation](five-profile-correction-audit.md), MM8–MM9, supplies the full wave receiver, all five explicit coefficients, every original-viscosity factor in the actual compact curl, the exact rank and image at every exceptional exponent of the local matrix, and the complete quadratic defect map with its first and second variations. The averaged tangential formulas retain all base-linear and pressure terms. These statements concern the given local map and do not claim a different global theorem.
