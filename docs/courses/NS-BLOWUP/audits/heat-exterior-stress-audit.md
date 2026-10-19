# Heat replacement, restored moments and the outer stress

This note constructs the heat replacement and its actual moment compensation, then derives the exterior stress and its limiting direction. It uses the reference profile already constructed in [O0–O8](outer-profile-audit.md), the exact operators in [G0–G6](profile-stress-moment-audit.md), and the original heat integral derived in [L6](physical-realization-audit.md). The analytic regular-axis solution is derived in [J0–J7](analytic-axis-profile-audit.md), and its continuation and exact matching to this exterior in [Q0–Q9](inner-outer-joining-audit.md). The shear modification and complete leading-profile Theorem 4.6 are derived in [V0–V7](shear-realization-audit.md). The positive-order base is derived in [Z0–Z8](base-field-realization-audit.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).

Source: OpenAI, *Finite Time Blowup for Navier–Stokes*, original [PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), SHA256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`, original pages 138–144, (A.32)–(A.56), Proposition A.7, Lemmas A.8–A.9 and Proposition A.10.

## H0. The original heat factor and its exact comparison with the power

Retain \(0<h<1/100\), \(A=1/2+h\), \(D=1/2-h\), \(d=1-\eta^2\), \(L=1-2h\eta^2\), and all fixed reference-profile choices. The heat factor is
\[
\mathcal H(Z)=\frac1{\Gamma(1+h)}\int_0^\infty e^{-v}v^h(1+Zv)^{-h}\,dv,\qquad Z\ge0.
\tag{H0.1}
\]
The complete derivative and heat-equation proof is in L6. In particular
\[
\mathcal H^{(m)}(Z)=\frac{(-1)^m(h)_m}{\Gamma(1+h)}\int_0^\infty e^{-v}v^{h+m}(1+Zv)^{-h-m}dv,
\quad |\mathcal H^{(m)}(Z)|\le(h)_m(1+h)_m.
\tag{H0.2}
\]
Here every factor in the rising factorial is retained and \((h)_0=(1+h)_0=1\). The same integrable majorant works at zero, so all right derivatives extend continuously there. The mean value theorem and the bound for \(m=2\) give
\[
\mathcal H(0)=1,\quad \mathcal H'(0)=-h(1+h),\quad
\mathcal H(Z)=1-h(1+h)Z+O_h(Z^2),\quad
|\mathcal H(Z)-1|+|Z\mathcal H'(Z)|\le C hZ
\tag{H0.3}
\]
on a fixed bounded nonnegative interval, uniformly for \(0<h\le h_0<1/2\). For each fixed positive m, the derivative bound in H0.2 is at most \(C_mh\). This uses a finite Taylor formula, not a convergent series. The exact remainder and coefficient-ratio proof in [L6.3a–L6.3b](physical-realization-audit.md) show that the formal heat Taylor series has radius zero for every h>0; all estimates here use only the proved finite-order formulas.

Let \(E_{\rm pow}(X)=c_\infty X^{-A}\), \(H_{\rm pow}=\sqrt{2X}E_{\rm pow}\), \(s=r^2/2\), \(\tau=1-t\). The physical heat swirl is exactly
\[
K(r,t)=c_\infty s^{-A}\mathcal H(2\tau/s),\quad
\partial_tK=(\partial_{rr}+r^{-1}\partial_r-r^{-2})K,\quad
q^AK=E_{\rm pow}(X)\mathcal H(2d/X).
\tag{H0.4}
\]
It is independent of z. To check the sign used below, \(-Z\mathcal H'/\mathcal H\) is the average of \(hZv/(1+Zv)\) against the positive probability measure obtained by dividing the integrand of H0.1 by its integral. Consequently
\[
0\le-\frac{Z\mathcal H'}{\mathcal H}<h,\qquad
\frac{rK_r}{2K}=-A-\frac{Z\mathcal H'}{\mathcal H}<-1/2.
\tag{H0.5}
\]
In particular K is positive and strictly decreasing in r. Composition with \(Z=2(1-\eta^2)/X\) uses only \(Z\ge0\). Every parameter derivative is a finite chain-rule sum involving powers of \(2/X\), \(-2\eta\), \(-2\), and derivatives in H0.2. No division by d occurs, including at \(\eta=\pm1\).

## H1. The actual heat change and its three full moment changes

Use the source terminal coordinate \(y=\log(X/X_{\rm tail})\), \(X_b=e^3X_{\rm tail}\), and
\[
X_K=e^{.2}X_{\rm tail},\qquad 0\le\chi_K\le1,\qquad
\chi_K=0\ (y\le.2),\quad\chi_K=1\ (y\ge.5).
\tag{H1.1}
\]
The actual terminal replacement is
\[
E_H=E_{\rm cl}\{1+\chi_K(y)[\mathcal H(2d/X)-1]\},\qquad \Delta E=E_H-E_{\rm cl},
\tag{H1.2}
\]
where \(E_{\rm cl}\) is the full reference profile, including its moment corrections. The factor in braces is a convex combination of 1 and the strictly positive heat factor; hence \(E_H>0\) everywhere. On this tail \(E_{\rm cl}=E_{\rm pow}f_o(y)\), and U is zero.

Set \(x=X/X_K\), and let \(e_K=E_{\rm cl}(X_K)\). All logarithmic derivatives of \(f_o\) and \(\chi_K\) are bounded after the preceding choices. H0.2–H0.3 and the chain rule therefore give, for every fixed \(j,m\),
\[
|(X\partial_X)^j\partial_\eta^m\Delta E|
\le C_{j,m,h}e_KX_K^{-1}x^{-A-1},\qquad x\ge1.
\tag{H1.3}
\]
For \(m=0\), the factor \(X^{-1}\) follows from \(\mathcal H-1\); every differentiated heat term also contains at least one factor \(X^{-1}\). Derivatives of the switch are supported in a fixed bounded x interval and obey the same bound. Thus H1.3 holds uniformly at both parameter endpoints.

Keep the original pressure moment \(C_p=\int E^2/(2X)\,dX\), stress moment \(S=\int(U^2-E^2/2)\,dX\), and subtracted angular moment \(\mathcal I=\int(H-H_{\rm pow})\,dX\). The exact discrepancies caused by H1.2 alone are
\[
\begin{split}
\Delta C_p(\infty)&=\int_{X_K}^\infty\frac{E_{\rm cl}\Delta E+(\Delta E)^2/2}{X}\,dX,\\
\Delta S(\infty)&=-\int_{X_K}^\infty[E_{\rm cl}\Delta E+(\Delta E)^2/2]\,dX,\\
\Delta\mathcal I&=\int_{X_K}^\infty\sqrt{2X}\,\Delta E\,dX.
\end{split}
\tag{H1.4}
\]
The subtracted power is unchanged. All quadratic terms and the factor \(1/2\) are present. Since \(\mathcal H\le1\), \(\Delta E\le0\) and \(0<E_H\le E_{\rm cl}\). Accordingly the three displayed discrepancies have signs nonpositive, nonnegative and nonpositive, respectively. The functions M and J are unchanged pointwise in X, because both their affected integrands contain U, which is zero on the edited tail.

For every fixed m, differentiating H1.4 under its absolutely convergent integrals is justified by H1.3 and its product-rule bounds. Keeping the radial factors explicitly gives
\[
\begin{split}
|\partial_\eta^m\Delta C_p(\infty)|&\le C_{m,h}\frac{e_K^2}{X_K}\int_1^\infty x^{-2A-2}dx
=C_{m,h}\frac{e_K^2}{X_K(2A+1)},\\
|\partial_\eta^m\Delta S(\infty)|&\le C_{m,h}e_K^2\int_1^\infty x^{-2A-1}dx
=C_{m,h}\frac{e_K^2}{2A},\\
|\partial_\eta^m\Delta\mathcal I|&\le C_{m,h}e_KX_K^{1/2}\int_1^\infty x^{-A-1/2}dx
=C_{m,h}\frac{e_KX_K^{1/2}}h.
\end{split}
\tag{H1.5}
\]
The \(1/h\) in the last row remains explicit. It is finite because h was fixed before the large-radius choice; no uniform limit as h tends to zero is used here.

## H2. Three additive bumps, their exact nonlinear system and preservation

Use only the second reserved interval \(\mathcal I_2\). At its start \(X_*\), set \(x_*=X/X_*\). There the unmodified field is \(U=0\), \(E_0=e_*f(\eta)x_*^{-1/2-\lambda}\), \(f=(1+\eta^2)^{-1}\ge1/2\). Choose three fixed nonnegative smooth bumps \(\beta_i\) with ordered disjoint compact supports inside this patch and put
\[
v(x_*,\eta)=\sum_{i=1}^3c_i(\eta)\beta_i(x_*),\qquad \delta E=e_*v.
\tag{H2.1}
\]
The tail and this patch are disjoint, so their moment changes add exactly. Divide the three original patch rows by \(e_*^2,X_*e_*^2,X_*^{3/2}e_*\), respectively. The resulting complete map is
\[
\begin{pmatrix}\delta C_p/e_*^2\\\delta S/(X_*e_*^2)\\\delta\mathcal I/(X_*^{3/2}e_*)\end{pmatrix}
=\begin{pmatrix}
\int[fx_*^{-3/2-\lambda}v+v^2/(2x_*)]dx_*\\
\int[-fx_*^{-1/2-\lambda}v-v^2/2]dx_*\\
\sqrt2\int x_*^{1/2}v\,dx_*
\end{pmatrix}=B(\eta)c+\mathscr Q_\eta(c,c).
\tag{H2.2}
\]
Every sign, Jacobian and row factor is fixed by H1.4 applied to the patch. Recovering the original rows means multiplying by precisely those three factors; none is discarded. The linear weights are \(fx_*^{-3/2-\lambda},-fx_*^{-1/2-\lambda},\sqrt2x_*^{1/2}\). Their three exponents are distinct. G4 proves invertibility of the power-moment matrix. The row factors f, -f and \(\sqrt2\) give a uniformly invertible B on [-1,1], with bounded derivatives of each fixed order. The first two quadratic integrals remain in \(\mathscr Q\); the last row is exactly linear.

The desired vector is minus the three full discrepancies H1.4 divided by the corresponding original row factors. The ratios \(X_*/X_K\) and \(e_*/e_K\) are positive fixed numbers after the reference schedule is chosen. Thus H1.5 proves
\[
\|d_{\rm mom}\|_{C^m_\eta}\le C_{m,h}X_K^{-1}
\tag{H2.3}
\]
for each fixed m. In the angular row the constant includes the retained \(1/h\) and the fixed factor \((X_K/X_*)^{3/2}(e_K/e_*)\). The pressure and S rows retain their respective fixed amplitude ratios as well.

Apply the actual iteration G5.6 with this d, this B and both quadratic rows in H2.2. Since B and \(\mathscr Q\) are independent of \(X_R\), their \(C^0\) operator norms are fixed. For sufficiently large \(X_K\), the contraction condition holds and gives the unique small solution \(c=O(X_K^{-1})\). Its differential \(B+\mathscr Q(c,\cdot)+\mathscr Q(\cdot,c)\) has a uniformly bounded inverse, by the same Neumann-series estimate. Differentiate H2.2 m times: the terms containing \(c^{(m)}\) are exactly this differential times \(c^{(m)}\). All remaining terms contain either \(d_{\rm mom}^{(m)}=O(X_K^{-1})\), one lower derivative of c times a fixed derivative of B, or a product of two lower c derivatives and fixed derivatives of \(\mathscr Q\). Induction therefore proves
\[
\|\partial_\eta^mc\|_\infty\le C_{m,h}X_K^{-1}\qquad\text{for every fixed }m.
\tag{H2.4}
\]
A single sufficiently large radius for the \(C^0\) solve suffices for these all-fixed-order estimates, with order-dependent constants. Only the finite small bounds needed below require prescribed thresholds. No smallness of infinitely many derivative norms is assumed.

The corrected E is positive on the patch: its reference lower bound on this fixed compact \(x_*\) interval is \(e_*c_*>0\), while \(|\delta E|\le e_*C_h/X_K\). Choose the radius so the latter is smaller than \(e_*c_*/2\). It is positive elsewhere by H1.2. The solve proves exactly
\[
\Delta M(X)=\Delta J(X)=0\text{ for every }X,\qquad
\Delta S(\infty)=\Delta C_p(\infty)=\Delta\mathcal I=0.
\tag{H2.5}
\]
In particular the actual profile still has \(M(\infty)=J(\infty)=S(\infty)=\mathcal I=0\). The pressure is integrated forward from the unchanged analytic datum \(\Pi_0\). Its total increment is unchanged, so it still vanishes at infinity. Before the compensation patch all profiles and the forward pressure are unchanged. Because U is unchanged everywhere, G0.7 also proves that \(V_0\) is unchanged everywhere.

There is an additional exact endpoint fact. At \(\eta=\pm1\), d is zero and \(\mathcal H(0)=1\), so all three tail discrepancies vanish. The zero coefficient vector solves H2.2 there, and uniqueness in the same small ball gives \(c(\pm1)=0\). Thus the entire modified E agrees with the reference E at both parameter endpoints. Moreover \(c=(1-\eta^2)\widetilde c\) with \(\widetilde c\) smooth on the closed interval: near an endpoint, the fundamental theorem of calculus writes c as its distance from that endpoint times the integral of its first derivative; the other linear factor is nonzero. The tail change has the same factor directly from
\[
\mathcal H(2d/X)-1=\frac{2d}{X}\int_0^1\mathcal H'(2sd/X)\,ds.
\tag{H2.6}
\]
This endpoint equality does not set parameter derivatives of the changes to zero; those derivatives enter the stress and are controlled by H2.4.

## H3. Preservation of the actual stress cone before the terminal collar

The compact interval from \(\mathcal I_2\) to terminal coordinate \(y=.5\) is fixed in \(x=X/X_R\). On it the reference E, Q and \(v_s-2\), and both sufficient cone gaps in O5.1, have positive minima. Every fixed radial and parameter derivative of the heat change and the compensating bumps is \(O_h(X_K^{-1})\) in these x coordinates. This follows from H1.3 on the tail, H2.1–H2.4 on the compact patch, and the fixed ratios of radii. In particular the needed radial shear derivatives are included.

For the cumulative moments retain exactly
\[
M=X_R\widehat M,\quad I=X_R^{3/2}\widehat I,\quad J=X_R^{3/2}\widehat J,
\quad S=X_R\widehat S,\quad C_p=\widehat C_p,
\quad H=\sqrt{X_R}\widehat H.
\tag{H3.1}
\]
Partial integrals of the absolute moment changes satisfy the same \(O_h(X_K^{-1})\) bounds after these divisions: on the patch use H2.2 with absolute values and the fixed supports, and on the tail use the majorants H1.5. Thus every required parameter derivative of \(\Delta\widehat{\mathbf m}\) is \(O_h(X_K^{-1})\). G3.4–G3.6, with the unchanged axis pressure, gives \(\Delta Q_s,\Delta N_s=O_h(X_K^{-1})\), using one additional parameter derivative. Directly differentiating \(a=1-2X\partial_X\log E\) and \(b_s=2XU_X/E\), with the positive reference E bound, gives the same bound for their differences. Division by the positive reference \(EQ_s\) gives it for \(w=N_s/(EQ_s)\) too.

These estimates preserve the positive lower bounds and strict O5.1 gaps for sufficiently large \(X_R\). The image of the perturbed \((a,b_s,w)\) lies in one fixed compact subset of those strict inequalities. G6.5 supplies a common finite threshold \(P_K\), while \(p_{s,1}=X_RxQ_s/L\) grows at least linearly with \(X_R\). Choose the radius also to exceed that threshold. Then the actual stress is admissible throughout the stated interval. This argument retains the full scaling: \(\widehat p_s=X_R^{-1}p_s\) is close, whereas an absolute small bound on \(\Delta p_s\) is not asserted. This completes the construction and cone assertion of Proposition A.7.

## H4. Backward stress from the constructed profile and the boundary traces

The profile now constructed has a temporary inner reference rather than a regular axis. We can nevertheless compute its backward stress directly; this avoids assuming the still-unconstructed inner field. For fixed \((z,t)\) with \(t<1\), its exact inner powers are
\[
u_\theta=C_\theta(z,t)r^{1/5},\qquad
u_z=C_z(z,t),\qquad u_r=C_r(z,t)r,\qquad
p=p_{\rm ax}(z,t)+C_p^{\rm loc}(z,t)r^{2/5}.
\tag{H4.1}
\]
They follow from \(U=4\eta\), \(E=P_*f(X/X_R)^{1/10}\), G0.7 and the pressure integral. The coefficients are smooth on compact sets with \(t<1\). In particular all time and axial derivatives preserve these radial powers. They are not a claim of Cartesian smoothness at the axis.

For the physical leading tangential residuals, retaining radial viscosity and omitting axial viscosity exactly as in original (4.12), incompressibility gives the conservative identities
\[
\begin{split}
r^2\mathscr R_\theta^{(0)}&=\partial_t(r^2u_\theta)
+\partial_r(r^2u_ru_\theta)+\partial_z(r^2u_zu_\theta)
-\partial_r(r^2\partial_ru_\theta-ru_\theta),\\
r\mathscr R_z^{(0)}&=\partial_t(ru_z)+\partial_r(ru_ru_z)
+\partial_z[r(u_z^2+p)]-\partial_r(r\partial_ru_z).
\end{split}
\tag{H4.2}
\]
For example, the first transport divergence has an extra coefficient \((2ru_r+r^2\partial_ru_r+r^2\partial_zu_z)u_\theta=ru_ru_\theta\), exactly the cylindrical angular transport term. No angular term has been lost.

At zero, H4.1 gives
\[
r^2u_ru_\theta=O(r^{16/5}),\quad
r^2\partial_ru_\theta-ru_\theta=-\tfrac45C_\theta r^{6/5},\quad
ru_ru_z=O(r^2),\quad r\partial_ru_z=0.
\tag{H4.3}
\]
All four boundary traces vanish. The leading angular viscous term is a constant times \(r^{-9/5}\), whose weighted integral against \(r^2dr\) converges at zero. The other terms of H4.2 are also integrable there. Thus the forthcoming integrations are valid for the actual temporary reference. For a smooth axis field, the standard axis powers \(u_\theta,u_r=O(r)\), \(u_z=O(1)\), \(\partial_ru_z=O(r)\) give the same vanishing traces; the argument also verifies the receiving identity in Lemma A.8 once the inner field is supplied.

In the exterior \(u_\theta=K\), \(u_r=u_z=0\). Write \(K_{\rm pow}=c_\infty s^{-A}\), which is independent of t and z. H0.2–H0.3 give, locally uniformly in nonnegative bounded \(\tau\),
\[
K-K_{\rm pow}=O_h(\tau r^{-3-2h}),\quad
\partial_tK=O_h(r^{-3-2h}),\quad
r^2K_r-rK=O_h(r^{-2h}).
\tag{H4.4}
\]
For \(R_*\ge1\), both the subtracted angular moment and its time derivative have the common weighted majorant
\[
\int_{R_*}^\infty r^2\bigl(|K-K_{\rm pow}|+|\partial_tK|\bigr)dr
\le C_h(1+\tau)\int_{R_*}^\infty r^{-1-2h}dr
=\frac{C_h(1+\tau)}{2h}R_*^{-2h}.
\tag{H4.5}
\]
The \(r^2\) weight multiplies both terms, as in the original page. Near zero the subtracted power has weighted size \(r^{1-2h}\), integrable since \(h<1\), and its time derivative is zero. These bounds justify differentiation of the convergent subtracted moment and its change of variable:
\[
\int_0^\infty r^2(u_\theta-K_{\rm pow})dr
=q^{3/2-A}\int_0^\infty(H-H_{\rm pow})dX=0,
\quad \int_0^\infty r^2u_zu_\theta dr=q^{3/2-2A}J(\infty)=0.
\tag{H4.6}
\]
The second integral is supported in a bounded radial region; its z derivative is justified by H4.1 at zero and local boundedness elsewhere. Exterior radial transport vanishes because \(U=M=0\) gives \(V_0=0\) exactly. H4.3–H4.6 in the first conservative identity prove \(\int_0^\infty r^2\mathscr R_\theta^{(0)}dr=0\).

For the axial identity, \(\int_0^\infty ru_zdr=q^{1-A}M(\infty)=0\). The exact pressure calculation, justified by absolute convergence or Tonelli applied to its negative, is
\[
\begin{split}
\int_0^\infty rp(r)dr
&=-\int_0^\infty\frac{u_\theta(r')^2}{r'}\left(\int_0^{r'}r\,dr\right)dr'
=-\tfrac12\int_0^\infty r'u_\theta(r')^2dr',\\
\int_0^\infty r(u_z^2+p)dr&=q^{1-2A}S(\infty)=0.
\end{split}
\tag{H4.7}
\]
At infinity \(p=O(r^{-2-4h})\) and \(r^2p\to0\); near zero H4.1 suffices. The axial flux derivative is justified locally in z by the same bounds, and its exterior pressure is z independent. Radial transport and viscosity traces vanish at both ends. Thus \(\int_0^\infty r\mathscr R_z^{(0)}dr=0\).

The original forward primitives can therefore be written with the positive backward sign:
\[
T_\theta(r)=\frac1{r^2}\int_r^\infty r'^2\mathscr R_\theta^{(0)}(r')dr',\qquad
T_z(r)=\frac1r\int_r^\infty r'\mathscr R_z^{(0)}(r')dr',\qquad
T=q^{-A-1/2}\mathcal T_0.
\tag{H4.8}
\]
The forward primitives here equal G1.5: their lower boundary constants vanish by H4.3, and their radial integrating factors are the same \(r^2,r\). Both residuals vanish beyond \(X_b\), by the exact swirl heat equation and its z-independent canonical pressure. Hence \(\mathcal T_0=0\) for \(X\ge X_b\).

This calculation proves the outer stress for the actual reference, with its weaker axis powers. It also gives the exact transfer to the future regular inner construction: G3.1 shows that matching the five cumulative moments and common axis pressure at a radius where the profiles rejoin makes all outer \(Q_s,N_s,p_s,a,b_s,\mathcal T_0\) identical. The actual regular matching is constructed in [Q0–Q9](inner-outer-joining-audit.md); this reference calculation uses its stated temporary axis powers.

## H5. Positive angular stress and the strict cone on the terminal interval

On \(1/2\le y<3\), the switch is identically one. Write \(f=f_o(y)\), \(f'=\partial_y f\). Then \(u_\theta=Kf\), \(u_r=u_z=0\), and K is independent of z. The original coordinate derivatives are
\[
y_t=\frac1{qL},\qquad y_z=-\frac{2\eta}{q^DL},\qquad y_r=\frac2r.
\tag{H5.1}
\]
Apply the product rule to the original radial swirl operator, and use its exact heat equation H0.4. Differentiating the canonical pressure at fixed r gives
\[
\begin{split}
\mathscr R_\theta^{(0)}&=\frac{Kf'}{qL}-K(f_{rr}+r^{-1}f_r)-2K_rf_r,\\
\mathscr R_z^{(0)}=p_z(r)&=\frac{2\eta}{q^DL}\int_y^3K(v)^2f(v)f'(v)\,dv.
\end{split}
\tag{H5.2}
\]
For the second identity start with \(p=-\int_r^\infty K(r')^2f(y(r'))^2dr'/r'\). Its z derivative is \(4\eta(q^DL)^{-1}\int K^2ff'\,dr'/r'\), and \(dr'/r'=dv/2\) gives exactly H5.2. The integrand vanishes beyond the terminal endpoint. This also proves the differentiation directly on its bounded support.

Integrating the viscous terms of H5.2 by parts in H4.8 yields
\[
T_\theta=Kf_r+\frac1{r^2}\int_r^\infty(r'K-r'^2K_{r'})f_{r'}\,dr'
+\frac1{qLr^2}\int_r^\infty r'^2Kf'\,dr'.
\tag{H5.3}
\]
Indeed the integral of \(-r'^2Kf_{r'r'}\) has lower boundary \(+r^2Kf_r\); its remaining coefficient is \(2r'K+r'^2K_{r'}\). Combining it with \(-r'Kf_{r'}-2r'^2K_{r'}f_{r'}\) leaves \((r'K-r'^2K_{r'})f_{r'}\). The upper boundary is zero because f is constant there. Thus the boundary sign and all three terms in H5.3 are fixed.

Each term is nonnegative by H0.5 and \(f'\ge0\). The remaining y interval has length at most \(5/2\); hence \(1\le r'/r\le e^{5/4}\). H0.5 bounds the logarithmic derivative of K between \(-1-2h\) and \(-1\), so \(K(r')/K(r)\) is bounded above and below by positive constants independent of small h and large \(X_R\) on this interval. Since \(\int_y^3f'(v)dv=\rho_o\psi_o(y)\), the last term of H5.3, with \(dr'=r'dv/2\), gives
\[
T_\theta\ge c\frac{rK}{qL}\rho_o\psi_o(y)>0\qquad (y<3).
\tag{H5.4}
\]
Use \(|\eta|\le1\), \(L\ge1-2h\), \(0<f\le1\), and monotonic decrease of K and \(\psi_o\) in H5.2 and then H4.8. The finite length and radius ratio just bounded give
\[
|p_z|\le Cq^{-D}K^2\rho_o\psi_o,
\quad |T_z|\le Crq^{-D}K^2\rho_o\psi_o,
\quad \left|\frac{T_z}{T_\theta}\right|\le Cq^{1-D}K
=CE_{\rm pow}(X)\mathcal H(2d/X).
\tag{H5.5}
\]
The last equality retains \(1-D=A\). The constants can be chosen uniformly for \(0<h\le1/100\) and sufficiently large radius. By the exact amplitude reduction O3.1 and the bounded factor \(f_o^{-1}\), the last expression is at most \(C e_{\rm rel}h^6\). Here \(e_{\rm rel}\) was fixed before h. Include the finite requirement \(Ce_{\rm rel}h^6\le1\) among the small-h choices of O8, before choosing \(X_R\). This is compatible with the earlier choices: it is one further upper bound on h, not a lower bound or a change of h after the profile is chosen. We henceforth use that common choice.

The original shear variables now obey
\[
b_s=0,\qquad
a=2+2h+2Z\frac{\mathcal H'(Z)}{\mathcal H(Z)}-2\frac{f'}f,
\qquad Z=\frac{2d}{X}.
\tag{H5.6}
\]
The reference step has \(f'/f<h/4\). H0.3 and positivity of \(\mathcal H\) give \(-Z\mathcal H'/\mathcal H<h/4\) after increasing \(X_R\). Thus \(2+h<a\le2+2h\). In G6, \(t_s=0\), \(v_s=a>2\), \(P_c-v_s=\mathcal T_{0,\theta}/F>0\), and \(J_c=\mathcal T_{0,z}/F\). Its exact cone criterion becomes
\[
(a-2)\left(\frac{T_z}{T_\theta}\right)^2<2,
\qquad
2-(a-2)\left(\frac{T_z}{T_\theta}\right)^2\ge2-2h>1.
\tag{H5.7}
\]
This proves admissibility at every point of the terminal interval before its outer endpoint, with fixed directional slack. It uses the actual stress calculated in H4, not an independent replacement for it.

## H6. Full flat factors and the smooth limiting direction

First prove the integral identity used at the edge. For \(c>0\), a fixed integer \(j\ge0\), and b smooth on \([0,\delta_0]\) times a compact parameter interval,
\[
\int_0^\delta e^{-c/u^2}u^{-j}b(u,\eta)du
=\tfrac12e^{-c/\delta^2}\delta^{3-j}B(\delta,\eta),
\tag{H6.1}
\]
where the substitution \(u=\delta(1+\delta^2v)^{-1/2}\) gives exactly
\[
B(\delta,\eta)=\int_0^\infty e^{-cv}(1+\delta^2v)^{(j-3)/2}
b\!\left(\frac{\delta}{\sqrt{1+\delta^2v}},\eta\right)dv,
\qquad B(0,\eta)=\frac{b(0,\eta)}c.
\tag{H6.2}
\]
The Jacobian is \(-\tfrac12\delta^3(1+\delta^2v)^{-3/2}\), and \(c/u^2=c/\delta^2+cv\). These give both the factor \(1/2\) and every power in H6.1. Each fixed mixed derivative of the last integrand is bounded by \(e^{-cv}\) times a polynomial in v, uniformly on the closed parameter rectangle: the denominator \(1+\delta^2v\) is at least one, its numerator factors are polynomially bounded in v, and all derivatives of b on its compact domain are bounded. The same holds for derivatives of its composed argument. Dominated differentiation proves smoothness through \(\delta=0\) and all fixed derivative bounds; dominated convergence gives the displayed endpoint value. The proof also permits any finite collection of extra compact smooth parameters.

Put \(\delta=3-y=\log(X_b/X)\). The specific step in O0 has, for sufficiently small nonnegative \(\delta\),
\[
\psi_o=e^{-4/\delta^2}g(\delta),\qquad
g(\delta)=\frac1{e^{-(1-\delta/2)^{-2}}+e^{-4/\delta^2}},\qquad g(0)=e.
\tag{H6.3}
\]
Extend \(e^{-4/\delta^2}\) by zero at zero; its derivatives of every order are a polynomial in \(1/\delta\) times the same exponential and tend to zero. The denominator defining g has a positive value at zero, so g is smooth on a closed small collar. With \(f=1-\rho_o\psi_o\) and \(\partial_y=-\partial_\delta\),
\[
f'=\rho_oe^{-4/\delta^2}\delta^{-3}[8g(\delta)+\delta^3g'(\delta)].
\tag{H6.4}
\]

To retain every scale and integration weight, set \(R(v)=\sqrt{2X_{\rm tail}e^v}\) and \(\mathcal E(v,\eta)=E_{\rm pow}(X_{\rm tail}e^v)\mathcal H(2d/(X_{\rm tail}e^v))\). Thus \(r'=\sqrt qR(v)\) and \(K(r',t)=q^{-A}\mathcal E(v,\eta)\). Multiplying H5.3 and H4.8 by the original \(q^{A+1/2}\) gives the exact profile formulas
\[
\begin{split}
\mathcal T_{0,\theta}(y,\eta)
={}&\frac{2\mathcal E(y,\eta)}{R(y)}f'(y)\\
&+\frac1{R(y)^2}\int_y^3R(v)\,[\mathcal E(v,\eta)-2\partial_v\mathcal E(v,\eta)]f'(v)\,dv\\
&+\frac1{2LR(y)^2}\int_y^3R(v)^3\mathcal E(v,\eta)f'(v)\,dv,\\
\mathcal T_{0,z}(y,\eta)
={}&\frac{\eta}{LR(y)}\int_y^3R(v)^2\left[\int_v^3\mathcal E(w,\eta)^2 f(w)f'(w)\,dw\right]dv.
\end{split}
\tag{H6.5}
\]
For the second angular term use \(K_{r'}=q^{-A-1/2}\partial_{R}\mathcal E\), \(R\partial_R\mathcal E=2\partial_v\mathcal E\), and \(f_{r'}dr'=f'dv\). For the last angular term, \(r'^2Kdr'=q^{3/2-A}R(v)^3\mathcal E\,dv/2\), while its denominator is \(qLr^2=q^2LR(y)^2\). Both have physical factor \(q^{-A-1/2}\). For the axial term, \(r'dr'=qR(v)^2dv/2\) cancels the 2 in H5.2, leaving physical factor \(q^{1/2-D-2A}\). The additional profile factor cancels it exactly because \(q^{A+1/2}q^{1/2-D-2A}=q^{1-D-A}=1\). Hence H6.5 retains the original physical factors and contains no hidden dependence on q.

All remaining coefficients of these integrals are smooth on the closed \((\delta,\eta)\) collar: \(X=X_be^{-\delta}\) is positive there, \(L\ge1-2h>0\), and the heat derivatives are smooth for the full closed interval \(-1\le\eta\le1\). The first angular term, using H6.4, is already \(e^{-4/\delta^2}\delta^{-3}\) times a smooth coefficient. Apply H6.1 with \(j=3,c=4\) to each remaining angular integral. Each becomes \(e^{-4/\delta^2}\) times a smooth function, and hence contributes \(\delta^3\) times a smooth function to that coefficient. This proves
\[
\mathcal T_{0,\theta}=e^{-4/\delta^2}\delta^{-3}b_\theta(\delta,\eta),
\quad
b_\theta(0,\eta)=\frac{16\rho_oE_{\rm pow}(X_b)\mathcal H(2d/X_b)g(0)}{\sqrt{2X_b}}>0.
\tag{H6.6}
\]
Positivity is uniform in \(\eta\), since the heat factor has a positive minimum on \([0,2/X_b]\). Continuity and compactness give a common closed collar where \(b_\theta\) has a positive lower bound.

The inner axial integral in H6.5 has one factor f'; H6.1 with \(j=3,c=4\) writes it as \(e^{-4/u^2}\) times a smooth coefficient. The outer integral then uses H6.1 with \(j=0,c=4\). Consequently
\[
\mathcal T_{0,z}=e^{-4/\delta^2}\delta^3b_z(\delta,\eta),\qquad
\frac{\mathcal T_{0,z}}{\mathcal T_{0,\theta}}=\delta^6\frac{b_z}{b_\theta}.
\tag{H6.7}
\]
Both coefficients are smooth on the closed collar. One can retain also the exact first axial coefficient. Set \(\mathcal E_b=E_{\rm pow}(X_b)\mathcal H(2d/X_b)\), \(R_b=\sqrt{2X_b}\). The inner integral coefficient at zero is \(\rho_og(0)\mathcal E_b^2\): its input coefficient is \(8\rho_og(0)\mathcal E_b^2\), and H6.1–H6.2 divide it by \(2c=8\). The outer integration divides by 8 once more. Thus
\[
b_z(0,\eta)=\frac{\eta\rho_og(0)R_b\mathcal E_b^2}{8L},\qquad
\left.\frac{b_z}{b_\theta}\right|_{\delta=0}=\frac{\eta X_b\mathcal E_b}{64L}.
\tag{H6.8}
\]
This is an explicit consequence of the same source integrals, not an assumption about their leading term. H6.5 also shows that the axial stress has the sign of \(\eta\) on the open collar and is zero at \(\eta=0\).

Write \(\mathcal R=\delta^6b_z/b_\theta\). Since \(\mathcal T_{0,\theta}>0\) before the edge, the unit direction is exactly
\[
\frac{\mathcal T_0}{|\mathcal T_0|}=\frac{(1,\mathcal R)}{\sqrt{1+\mathcal R^2}}
\longrightarrow(1,0).
\tag{H6.9}
\]
The expression extends smoothly to the closed collar. It is a direction extension; the stress itself is zero at the endpoint. H5.7 and continuity show that \(2-(a-2)\mathcal R^2\) remains uniformly positive, with endpoint value 2.

Finally, differentiating H6.6–H6.7 any fixed number of times in X and \(\eta\) introduces only finitely many inverse powers of \(\delta\). Indeed \(\delta_X=-1/X\) is smooth on the collar and the coefficient derivatives are bounded there. Therefore for every fixed mixed derivative I there are finite profile-dependent constants with
\[
|\partial^I\mathcal T_0|\le C_Ie^{-4/\delta^2}\delta^{-N_I},\qquad
|\mathcal T_0|\ge c e^{-4/\delta^2}\delta^{-3}.
\tag{H6.10}
\]
The upper bounds tend to zero to every order, proving that the stress extends smoothly by zero to \(X\ge X_b\), as H4 already requires. Neither constant depends on physical q. These calculations complete the outer-edge assertions of Proposition A.10 and the flat integral lemma A.9.

## H7. Original viscosity and the exact remaining scope

For any original viscosity \(\nu>0\), use the exact spatial map and fields of L3, with t unchanged:
\[
x=x_\nu/\sqrt\nu,\quad u_\nu(x_\nu,t)=\sqrt\nu\,u(x,t),\quad
p_\nu(x_\nu,t)=\nu p(x,t),\quad T_\nu(x_\nu,t)=\nu T(x,t).
\tag{H7.1}
\]
The full coordinates, with the original physical r and z now denoted \(r_\nu,z_\nu\), are
\[
q_\nu-\frac{z_\nu^2}{\nu}q_\nu^{2h}=1-t,\quad
X_\nu=\frac{r_\nu^2}{2\nu q_\nu},\quad
\eta_\nu=\frac{z_\nu}{\sqrt\nu q_\nu^D},\quad
T_\nu=\nu q_\nu^{-A-1/2}\mathcal T_0(X_\nu,\eta_\nu).
\tag{H7.2}
\]
Each physical leading residual scales by \(\sqrt\nu\): time, transport, pressure gradient and \(\nu\) times the radial viscous operator all do so. The stress divergence scales by the same factor, since one radial derivative of \(\nu T(x_\nu/\sqrt\nu,t)\) contributes \(1/\sqrt\nu\). Equivalently, substitution \(r'_\nu=\sqrt\nu r'\) into the two backward integrals gives \(T_{\nu,\theta}=\nu T_\theta\) and \(T_{\nu,z}=\nu T_z\), with their respective weights \(r'^2\) and \(r'\) retained. The stress ratio and its direction therefore agree exactly with H6.7–H6.9 at the mapped point. No viscosity factor is removed from the physical fields or their bounds.

H0–H6 construct the actual heat modification of the reference, restore its three changed moments with all parameter derivatives, preserve its earlier strict stress cone, and prove its outer support, cone and endpoint bounds. The calculation also proves the backward formula for the actual temporary reference axis powers H4.1; it does not assert that those powers are regular. Its matching map to a future inner field is exactly G3.1 with all five moments and the axis pressure retained. These supply the outer parts needed by Lemmas 4.8–4.9.

The actual analytic regular-axis solution with the prescribed \(\Pi_0\), its positive source and its endpoint inequality are derived in [J0–J7](analytic-axis-profile-audit.md). Its actual continuation and exact five-moment matching to this outer field are derived in [Q0–Q9](inner-outer-joining-audit.md). The actual admissible-shear realization and all leading-profile properties of Theorem 4.6 are derived in [V0–V7](shear-realization-audit.md). The positive-order base is derived in [Z0–Z8](base-field-realization-audit.md); the actual local construction and final assembly are proved in [I0–I7](local-construction-assembly-audit.md) and [F0–F8](terminal-force-and-blowup-audit.md). The actual local field and final localization are proved in [I0–I7](local-construction-assembly-audit.md) and [F0–F8](terminal-force-and-blowup-audit.md). This note supplies the outer heat and stress component of the [complete theorem derivation](theorem-audit-conclusion.md). The [outer-profile lesson](../src/constructing-the-outer-profile-and-heat-exterior.md), O0–H7 and X0, develops this construction with five worked exercises.
