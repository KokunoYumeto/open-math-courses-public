# The reference outer profile: moments, pressure and stress cone

This note derives Proposition A.4 and Lemma A.5 for the reference profile with a power-law exterior. The later replacement by a heat flow, regular inner profile and shear modification are separate parts of Theorem 4.6. They are not established here. The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).

Source: OpenAI, *Finite Time Blowup for Navier–Stokes*, original [PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), SHA256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`, pages 129–137, (A.5)–(A.31). The exact coordinate, stress, moment and finite-system operators are proved in [G0–G6](profile-stress-moment-audit.md); their original formulas and factors are retained below.

## O0. The complete reference schedule and the order of choices

Retain \(A=1/2+h,D=1/2-h,d=1-\eta^2,L=1-2h\eta^2\), \(f=(1+\eta^2)^{-1}\), \(J_0=\log(1+\eta^2)\), \(H=\sqrt{2X}E\), \(l=X\partial_X\log H\). All profiles have \(-1\le\eta\le1\). For each interval the coordinate \(y\) starts at its left endpoint and satisfies \(dX=X\,dy\). Hence prescribing l means solving \((\log E)'=l-1/2\), with the preceding endpoint value of E. Every prime on a radial profile below is a y derivative unless otherwise indicated.

Use the source's smooth step
\[
\sigma(y)=\frac{e^{-1/y^2}}{e^{-1/y^2}+e^{-1/(1-y)^2}}\ (0<y<1),\quad
\sigma(y)=0\ (y\le0),\quad \sigma(y)=1\ (y\ge1).
\tag{O0.1}
\]
It is increasing and smooth, flat at its endpoints. Indeed the logarithmic derivative of the ratio of the second exponential to the first is \(-2(1-y)^{-3}-2y^{-3}<0\); endpoint smoothness follows from \(y^{-n}e^{-1/y^2}\to0\) for every n. Positive correcting bumps are fixed translates or rescalings of \(\sigma'\), with the supports stated below. Their fixed derivative norms are finite.

The parameter order is
\[
M_d,\qquad T_d=e^{M_d}+10,\qquad P_*>e^{T_d},\qquad
0<\lambda\ll1,\qquad 0<h\ll\min\{\lambda,e^{-T_d}\},\qquad X_R.
\tag{O0.2}
\]
We always take \(h<1/100\). Fixed shape constants, including the interpolation length \(T_f\) and terminal constant \(c_o\), are chosen independently of the later small parameters. Below, \(C_{\rm pre}\) denotes finite constants depending only on those shapes, \(M_d,T_d,P_*\) and a specified finite derivative order, uniformly for sufficiently small \(\lambda\) and then sufficiently small h. No such constant depends on \(X_R\) or the amplitude factor \(\mathsf C\). Constants denoted C before the choice of \(M_d\) depend only on the fixed shapes. Estimates below justify this order rather than assuming its compatibility.

The entire schedule is as follows.

1. For \(X=X_Re^y\), \(y\le0\), set \(U=4\eta\), \(E=P_*fe^{y/10}\), so \(l=3/5\). This is the temporary inner reference, not a regular physical axis.
2. For one unit of logarithmic length keep \(U=4\eta\), and set \(l=(3/5)(1-\sigma(y))\).
3. On \(0\le y\le T_d\), set \(l=0\), \(E=P_1fe^{-y/2}\), and
\[
U=k(y)\eta,\quad k(y)=4[1-\sigma(\log(1+y)/M_d)],\qquad
|k'(y)|\le\frac{e_d}{1+y},\quad e_d=4\|\sigma'\|_\infty/M_d.
\tag{O0.3}
\]
Here \(e^{-1/2}P_*\le P_1\le e^{1/10}P_*\). The function k is zero on the last eleven units, since it is zero for \(y\ge e^{M_d}-1=T_d-11\).
4. With \(U=0\), move l from zero to \(-\lambda\) by \(l=-\lambda\sigma(y)\) on a unit interval. Keep \(l=-\lambda\) for \(T_w=60\log(1/\lambda)\). Reserve, in this latter local coordinate, the four intervals
\[
(T_w-25,T_w-20),\quad(T_w-20,T_w-15),\quad
(T_w-14,T_w-9),\quad(T_w-8,T_w-3).
\tag{O0.4}
\]
For sufficiently small \(\lambda\), all are nonempty, ordered and inside this interval. None of the reference-profile corrections below touches them. On them \(U=0\), \(E\) is the same positive multiple of \(fX^{-1/2-\lambda}\).
5. Let \(X_p\) be the end radius and \(E(X_p,\eta)=e_bf\). For \(0\le y\le13/\lambda\), retain \(l=-\lambda\), so \(E=e_bfe^{-(1/2+\lambda)y}\), and put
\[
\begin{gathered}
\zeta_b=\lambda y,\quad
\varphi_b(\zeta)=\int_0^\zeta\sigma(v/.02)\,dv,\quad
R_0(\zeta)=\varphi_b(\zeta)[1-\sigma(\zeta-10)],\\
R_b=\operatorname{Amp}(\eta)R_0(\lambda y)+c_1(\eta)\beta_1(y)+c_2(\eta)\beta_2(y),\qquad U=ER_b.
\end{gathered}
\tag{O0.5}
\]
Extend \(\varphi_b\) by zero on negative arguments. The \(\beta_j\) are identical width-.3 bumps centered at \(13/\lambda-3\) and \(13/\lambda-1\). Their coefficients restore M and J; Amp restores S. These choices are made in O1–O3.
6. After the pulse put \(U=0\) permanently. Writing \(E(X_{\rm end},\eta)=e_{\rm end}f\), prescribe
\[
\log E=\log e_{\rm end}-(1/2+\lambda)y-\vartheta_f(y)J_0-(1-\vartheta_f(y))\log2,
\quad \vartheta_f(y)=1-\sigma(y/T_f).
\tag{O0.6}
\]
Choose the fixed \(T_f\ge10\|\sigma'\|_\infty\log2\), so \(-\lambda-.1\le l\le-\lambda\). This also satisfies the source's weaker lower bound \(-\lambda-1\). Continue the resulting \(\eta\)-independent exponential for \(30\log(1/\lambda)\). Two relative E bumps of width .3, centered three and one units before that interval ends, impose
\[
I=\frac{XH}{1-\lambda}\quad\hbox{at the endpoint},\qquad
\int_{\text{two bumps}}(E^2-E_{\rm unedited}^2)\,dy=0.
\tag{O0.7}
\]
These bumps have zero endpoint values and leave all later E values unchanged.
7. At radius \(X_{\rm rel}\), with common value \(e_{\rm rel}\), move l from \(-\lambda\) to \(-1\) on a unit interval, hold \(-1\) for \(4\log(1/h)\), and move from \(-1\) to \(-h\) on a unit interval. Every transition uses \(\sigma\). Then hold \(-h\) for the finite length selected in O2.
8. On the final interval \(0\le y\le3\), use
\[
\psi_o=1-\sigma((y-1)/2),\quad f_o=1-\rho_o\psi_o,\quad
\rho_o=c_oh,\quad l=-h+f_o'/f_o.
\tag{O0.8}
\]
Choose \(c_o>0\) so small that \(0\le f_o'/f_o\le h/4\). For example \(c_o\le[16(1+\|\psi_o'\|_\infty)]^{-1}\) suffices for \(h<1/100\). Extend \(f_o\) constantly on the left and by one on the right. Thereafter \(E=E_{\rm pow}=c_\infty X^{-A}\), with \(c_\infty>0\) independent of \(\eta\).

Smooth flat endpoint matching of the step functions and bumps makes this schedule smooth for \(X>0\); solving the logarithmic equation gives E positive before its small relative corrections. Positivity after those corrections is proved below. All stage lengths are finite after the parameter choices. Their endpoint radii divided by \(X_R\) are fixed.

## O1. The actual axial correction and the initial moment bounds

Use the five original integrals \((M,I,J,S,C_p)\) from G2.1. Before the long intermediate interval all dimensionless profiles and their fixed \(\eta\) derivatives have finite bounds depending only on the preceding choices. Radial integration over this finite logarithmic interval, and over the inner reference where the powers are integrable, gives finite bounds on \(M/X_R\), \(J/X_R^{3/2}\), \(S/X_R\), and the corresponding parameter derivatives. On the intermediate interval \(U=0\), so M and J remain constant. The exact multiplicative changes in its denominators are
\[
E/E(0)=e^{-(1/2+\lambda)y},\quad
XE/[XE](0)=e^{(1/2-\lambda)y},\quad
XHE/[XHE](0)=e^{(1/2-2\lambda)y},\quad
XE^2/[XE^2](0)=e^{-2\lambda y}.
\tag{O1.1}
\]
The entering unit transition has uniformly bounded factors. At \(T_w=60\log(1/\lambda)\), take \(\lambda<1/120\). Then \(e^{-(1/2-2\lambda)T_w}=\lambda^{30-120\lambda}\le\lambda^{29}\); the analogous M bound is no larger. The factor \(e^{2\lambda T_w}=e^{120\lambda\log(1/\lambda)}\) stays bounded as \(\lambda\downarrow0\). Integrating \(dS/dy=-XE^2/2\) over this interval and retaining the incoming S yields
\[
e_b\le C_{\rm pre}\lambda^{30},\quad
\left\|\frac{M(X_p)}{X_pe_bf}\right\|_{C^k_\eta}
+\left\|\frac{J(X_p)}{X_pH(X_p)e_bf}\right\|_{C^k_\eta}
\le C_{{\rm pre},k}\lambda^{29},\quad
\left\|\frac{S(X_p)}{X_pe_b^2f^2}\right\|_{C^k_\eta}
\le C_{{\rm pre},k}(1+\log(1/\lambda)).
\tag{O1.2}
\]
Every fixed k is allowed here. The factors f and its reciprocal have bounded derivatives on [-1,1]. The preceding estimates follow from exact integrals of the stated powers; they introduce no dependence on h through a divergent exterior integral.

On the pulse, the two original axial moment rows for a relative bump \(c\beta\) are exactly
\[
\delta M=X_pe_bf\,c\int e^{s_1y}\beta(y)\,dy,\qquad
\delta J=X_pH(X_p)e_bf\,c\int e^{s_2y}\beta(y)\,dy,
\quad s_1=1/2-\lambda,\quad s_2=1/2-2\lambda.
\tag{O1.3}
\]
This includes the Jacobian \(dX=X_pe^y\,dy\). Let \(y_1=13/\lambda-3\), \(y_2=y_1+2\). After dividing each row by its displayed physical factor and then by \(e^{s_iy_1}\), its two entries are \(b(s_i),e^{2s_i}b(s_i)\), with \(b(s)=\int e^{st}\beta(t)\,dt>0\). The determinant is \(b(s_1)b(s_2)(e^{2s_2}-e^{2s_1})\). G4.4 proves an inverse bound \(C/\lambda\), retaining the exact row factors to recover the original moments.

The main pulse ends by \(11/\lambda\), and \(R_0\le11\) on its support. For small \(\lambda\), \(s_i\ge2/5\). Its first-center-weighted moment has magnitude at most
\[
11|\operatorname{Amp}|e^{-s_iy_1}\int_0^{11/\lambda}e^{s_iy}\,dy
\le(55/2)|\operatorname{Amp}|e^{-2s_i/\lambda+3s_i}.
\tag{O1.4}
\]
The incoming moments in O1.2 gain the factor \(e^{-s_iy_1}\). Multiplication by the inverse loss \(1/\lambda\) is absorbed by a smaller positive exponential rate: for every \(a>0,n\), \(\lambda^{-n}e^{-a/\lambda}\le C_{a,n}e^{-a/(2\lambda)}\), since \(v^ne^{-av/2}\) is bounded for \(v\ge1\). Therefore the exact linear solve gives affine functions of Amp with
\[
c_i=c_{i,0}(\eta)+\operatorname{Amp}\,c_{i,1}(\eta),\qquad
\|c_{i,0}\|_{C^k_\eta}+\|c_{i,1}\|_{C^k_\eta}\le C_{{\rm pre},k}e^{-c/\lambda},\qquad
M=J=0\quad\hbox{after the pulse}.
\tag{O1.5}
\]
The same statement holds for fixed radial bump derivatives; a \(\zeta_b\) derivative adds a power of \(\lambda^{-1}\), which remains exponentially small. No quadratic term was dropped: M and J are exactly linear in U for the fixed E used here.

## O2. Angular moment restoration and the complete terminal schedule

The identity \(I'=XH\) gives, for \(r_I=I/(XH)\),
\[
r_I'+(1+l)r_I=1.
\tag{O2.1}
\]
Before interpolation, \(1+l\) has a fixed positive lower bound. The inner reference has \(r_I=5/8\); variation of constants bounds it and every fixed parameter derivative through the subsequent intervals. During interpolation, our choice in O0.6 keeps \(1+l\ge1-\lambda-.1>1/2\). Thus at its end \(r_I\) and its fixed parameter derivatives are bounded by \(C_{{\rm pre},k}\). On the following constant-slope interval the exact discrepancy is
\[
r_I(y)-(1-\lambda)^{-1}
=e^{-(1-\lambda)y}\,[r_I(0)-(1-\lambda)^{-1}].
\tag{O2.2}
\]
At the first angular bump center \(30\log(1/\lambda)-3\), its \(C^k_\eta\) norm is at most \(C_{{\rm pre},k}\lambda^{28}\) for sufficiently small \(\lambda\).

Write the relative change as \(E\mapsto E(1+v)\), \(v=d_1\beta_1+d_2\beta_2\). The two exact rows are
\[
\delta I=\int XHv\,dy,\qquad
\delta C_p=\int E^2(v+v^2/2)\,dy.
\tag{O2.3}
\]
Divide by \(XH\) and \(E^2\) at the first center, respectively. Their linear weights have exponents \(1-\lambda\) and \(-1-2\lambda\), separated by \(2+\lambda\). G4.4 gives a uniformly bounded inverse. The quadratic pressure term in O2.3 has uniformly bounded bilinear norms on these two fixed supports. The desired first-row discrepancy is O2.2 transported to the endpoint; equivalently, undoing that transport gives an \(O_{C^k}(C_{{\rm pre},k}\lambda^{28})\) discrepancy at the first center. The pressure discrepancy is zero. The actual finite solve G5.6–G5.8 therefore applies for sufficiently small \(\lambda\), giving
\[
\|(d_1,d_2)\|_{C^k_\eta}\le C_{{\rm pre},k}\lambda^{28},\qquad
I=XH/(1-\lambda)\text{ at the endpoint},\qquad \delta C_p=0.
\tag{O2.4}
\]
Only a specified finite k must have a small bound; smoothness of all orders follows from the same fixed branch. Taking k at least one gives \(|v|+|v'|\le C_{\rm pre}\lambda^{28}\). Thus \(1+v>0\) and the slope change \(v'/(1+v)\) is smaller than \(\lambda/2\). On the bumps, \(l\le-\lambda/2\). All earlier and later E values are unchanged. These choices involve E only and are independent of Amp.

At the exterior-transition start, \(U=M=J=0\), E and I are independent of \(\eta\), and G2.5 gives exactly
\[
Q_s=-1+(1-h)I/(XH)=\frac{\lambda-h}{1-\lambda},\qquad
Q_s'+(1+l)Q_s=-l-h.
\tag{O2.5}
\]
The first transition keeps a positive lower bound \(c\lambda\) when \(h\ll\lambda\). On the hold with \(l=-1\), \(Q_s'=1-h\); its length \(4\log(1/h)\) gives a value comparable to \(\log(1/h)\). The next unit transition changes that value by bounded positive factors and bounded terms, since its coefficients are bounded and its source is nonnegative. Call its final value \(Q_{\rm in}\).

For the terminal profile O0.8 define the source's exact value
\[
Q_p=\int_0^3\exp\!\left(\int_0^v(1+l(s))\,ds\right)\frac{f_o'(v)}{f_o(v)}\,dv.
\tag{O2.6}
\]
On this interval \(1+l\) is bounded above and below by positive constants. Also \(\int_0^3f_o'/f_o=-\log(1-c_oh)\), between \(c_oh\) and \(2c_oh\) for the stated small h. Thus \(c h\le Q_p\le C h\), with fixed positive constants. Consequently \(Q_{\rm in}>Q_p>0\) for sufficiently small h. The additional hold at \(l=-h\) has the explicitly positive finite length
\[
T_{\rm hold}=(1-h)^{-1}\log(Q_{\rm in}/Q_p).
\tag{O2.7}
\]
It decreases Q exactly to \(Q_p\). On the terminal interval, variation of constants with final value zero gives
\[
Q_s(y)=\int_y^3\exp\!\left(\int_y^v(1+l(s))\,ds\right)\frac{f_o'(v)}{f_o(v)}\,dv.
\tag{O2.8}
\]
Indeed differentiation gives \(Q_s'+(1+l)Q_s=-f_o'/f_o=-l-h\), and its initial value is O2.6. It is positive for every \(y<3\), vanishes at 3, and is zero thereafter. Its lower bound on \(0\le y\le1/2\) is \(ch\), because the integral over the fixed portion where \(f_o'>0\) remains present.

Beyond the terminal interval, \(H=H_{\rm pow}=\sqrt2c_\infty X^{-h}\) and \(I=XH/(1-h)\). But \(\int_0^XH_{\rm pow}\,dx=XH_{\rm pow}/(1-h)\), since \(h<1\). Therefore
\[
\int_0^\infty(H-H_{\rm pow})\,dX=0.
\tag{O2.9}
\]
This integral converges at zero and has identically zero integrand sufficiently far out. All exterior lengths and \(c_\infty\) are independent of Amp and \(\eta\).

## O3. Closing S with the actual amplitude

The integral after the pulse must be bounded uniformly as h becomes small. On the steep hold \(l=-1\), the exact changes are
\[
\frac{(XE^2)_{\rm end}}{(XE^2)_{\rm start}}=h^8,\qquad
\frac{E_{\rm end}}{E_{\rm start}}=h^6.
\tag{O3.1}
\]
The first follows from \((\log XE^2)'=2l=-2\); the second from \((\log E)'=-3/2\), each over \(4\log(1/h)\). The first unit transition and steep hold contribute at most \(CX_{\rm rel}e_{\rm rel}^2\) to \(\int XE^2dy\). After the steep hold, \(l\le-3h/4\) at every point. Thus the rest is bounded by
\(CX_{\rm rel}e_{\rm rel}^2h^8\int_0^\infty e^{-3hy/2}dy\le CX_{\rm rel}e_{\rm rel}^2h^7\). In particular the complete exterior release, regardless of its hold length, satisfies
\[
\int_{\rm release}XE^2\,dy\le CX_{\rm rel}e_{\rm rel}^2.
\tag{O3.2}
\]
Interpolation and the subsequent uniform interval have length \(T_f+30\log(1/\lambda)\), nonincreasing \(XE^2\) before the small bumps, and bounded relative bump factors. Their contribution, together with O3.2, is at most \(C(1+\log(1/\lambda))X_{\rm end}e_{\rm end}^2\). Fixed parameter derivatives obey the same estimate: f, its powers with exponents in [0,1], and the small angular coefficients have bounded derivatives; the release itself is independent of \(\eta\).

On the pulse the exact identity is \(XE^2=X_pe_b^2f^2e^{-2\lambda y}\). The pulse contribution to S, including its two end bumps, is therefore
\[
\frac{\lambda S(\infty)}{X_pe_b^2f^2}
=\operatorname{Amp}^2K_b-\frac{1-e^{-26}}4+\mathcal E(\operatorname{Amp},\eta),\qquad
K_b=\int_0^{13}e^{-2\zeta}R_0(\zeta)^2\,d\zeta.
\tag{O3.3}
\]
To justify every part of the error bound, the incoming S gives \(O_{C^k_\eta}(C_{{\rm pre},k}\lambda(1+\log(1/\lambda)))\) by O1.2. The post-pulse E integral has the same bound by O3.2 and
\(X_{\rm end}e_{\rm end}^2=X_pe_b^2e^{-26}\), with \(f^{-2}\) retained in the displayed denominator. The extra U terms are exactly \(2\operatorname{Amp}R_0(c_1\beta_1+c_2\beta_2)+(c_1\beta_1+c_2\beta_2)^2\). In fact the first term is zero because the end bumps lie after the main pulse; even its absolute bound from O1.5 is exponentially small. On the bounded amplitude bracket \([.9,1.2]\), the second term and all its fixed parameter derivatives are exponentially small too. The original coefficients are affine in Amp; differentiating them with respect to Amp uses their equally small linear coefficients. Thus
\[
\|\mathcal E\|_{C^1(\operatorname{Amp},\eta)}\le C_{\rm pre}\lambda(1+\log(1/\lambda)).
\tag{O3.4}
\]
All constants are uniform for the subsequently small h. This supplies the amplitude derivative estimate as well as the parameter estimate needed to infer a unique root.

Here are exact bounds on \(K_b\). Since \(0\le R_0\le\zeta\), \(K_b\le1/4\). On \(1/50\le\zeta\le9\), \(R_0\ge\zeta-1/50\). Direct integration gives
\[
K_b\ge\frac{e^{-1/25}}4-\frac{225301}{5000}e^{-18}>\frac15.
\tag{O3.5}
\]
For the strict last inequality, \(e^{-1/25}\ge24/25\) gives a first term at least \(6/25\), and \(e^{18}>18^4/24=4374\) gives a second term smaller than \(1/25\). These are exact analytic inequalities, not quadrature.

For \(F_0(a)=a^2K_b-(1-e^{-26})/4\), it follows that
\[
F_0(.9)<-.047,\qquad F_0(1.2)>.038,\qquad F_0'(a)>.36\quad(.9\le a\le1.2).
\tag{O3.6}
\]
The first follows from \(-19/400+e^{-26}/4<-47/1000\), using \(e^{26}>500\). The second is \((36/25)(1/5)-1/4=19/500\), and the derivative is larger than \(2(9/10)(1/5)=9/25\). Choose \(\lambda\) so that O3.4 is smaller than \(.01\), for example. Then the complete expression is negative and positive at the respective endpoints and has derivative greater than \(.35\). The intermediate value theorem and this derivative bound give exactly one root Amp in the bracket at each \(\eta\). The implicit function theorem gives a smooth root, including endpoint derivatives, with
\[
|\partial_\eta\operatorname{Amp}|\le C_{\rm pre}\lambda(1+\log(1/\lambda)).
\tag{O3.7}
\]
Implicit differentiation gives finite higher derivatives, and any finite set of small derivative bounds can be secured before choosing the parameters. Consequently the actual constructed profile has \(S(\infty)=0\), as well as O2.9 and \(M=J=0\) after the pulse. The integrals converge because U is compactly supported and \(E^2\) has the exterior power \(X^{-1-2h}\).

## O4. The analytic pressure supplied to the inner construction

Before the two pressure-preserving angular bumps, the complete schedule has the form \(E_{\rm id,sched}(y,\eta)=c(y)f(\eta)^{\vartheta(y)}\), with \(0\le\vartheta\le1\). Here use the global coordinate \(y=\log(X/X_R)\). The coefficient c and all interval lengths are independent of \(\eta\); O2 shows that the later lengths are independent of Amp as well. In the interpolation, c includes \(2^{-(1-\vartheta)}\), exactly as in O0.6. The exponent is one through the pulse, decreases to zero during interpolation, and is zero afterwards.

Choose a bounded simply connected complex neighborhood of [-1,1] whose closure avoids \(\pm i\). The function \(f(\eta)=(1+\eta^2)^{-1}\) is holomorphic and nonvanishing there, so choose an analytic logarithm. The functions \(\exp(2\vartheta\log f)\) are uniformly bounded on the closure for \(0\le\vartheta\le1\). At the two infinite ends c squared is a fixed multiple of \(e^{y/5}\) and \(e^{-(1+2h)y}\); the intervening interval is finite. Dominated integration and Morera's theorem therefore prove holomorphy on one common neighborhood of
\[
\Pi_0(\eta)=-\frac12\int_{-\infty}^\infty c(y)^2f(\eta)^{2\vartheta(y)}\,dy.
\tag{O4.1}
\]
For completeness, Morera applies because the uniform integrable majorant permits interchanging each triangular contour integral with the y integral, and each interior contour integral is zero. Continuity follows from the same majorant.

The function is even, and for real \(\eta\)
\[
\Pi_0'=J_0'\int c(y)^2\vartheta(y)f^{2\vartheta(y)}\,dy,\qquad
J_0'=\frac{2\eta}{1+\eta^2},\qquad
\Pi_0\le-\frac52P_*^2f^2.
\tag{O4.2}
\]
The integral in the derivative is strictly positive, since the inner reference has \(\vartheta=1,c>0\). This proves the required strict sign of \(\Pi_0'\) for \(\eta\ne0\). Its inner contribution is exactly \(-\frac12P_*^2f^2\int_{-\infty}^0e^{y/5}dy=-(5/2)P_*^2f^2\); all others are nonpositive. Independence of \(X_R\) follows from \(dX/X=dy\). Restoring the angular bumps leaves the total pressure integral exactly unchanged by O2.4. Thus for the actual reference profile
\[
\Pi(X,\eta)=\Pi_0+\int_0^X\frac{E(x,\eta)^2}{2x}\,dx
=-\frac12\int_{\log(X/X_R)}^\infty E(v,\eta)^2\,dv.
\tag{O4.3}
\]
Later smooth edits need not be analytic to preserve this already fixed analytic datum: exact zero total pressure increment is the sufficient identity, proved by splitting the last integral. This proves Lemma A.5 for the actual constructed reference family.

## O5. The cone through the reference and axial transitions

Keep the source test, with \(w=N_s/(EQ_s)\),
\[
a-b_sw>0,\qquad 2b_sw+b_s^2/a+(a-2)w^2<2,
\quad a=2-2l,\quad b_s=2U'/E.
\tag{O5.1}
\]
G6 proves how these inequalities imply the relaxed cone once \(p_{s,1}=XQ_s/L\) is large enough, and the admissible cone when also \(v_s=a+b_s^2/a>2\). We first prove the two strict inequalities and \(Q_s>0\), before choosing \(X_R\).

On the reference inner interval \(\mathcal A_XU=4\eta\), \(W=1-4L\), \(l=3/5\), \((\log E)_\eta=-J_0'\). The regular radial primitive for its constant angular source gives exactly
\[
Q_s=\frac{(3/5)(4L-1)-h(1-8\eta^2)+(D+4d)\eta J_0'}{8/5}.
\tag{O5.2}
\]
For \(h<1/100\), \(L\ge.98\), and \(\eta J_0'=2\eta^2/(1+\eta^2)\ge0\), the numerator is at least \((3/5)(4\cdot.98-1)-.01>8/5\). Hence \(Q_s>1\). Here \(a=4/5\), \(b_s=0\), so O5.1 holds for every finite w. On any fixed \(x=X/X_R\ge x_*>0\), E is positive and all quantities are bounded.

During the first unit transition U and W retain these values, \(0\le l\le3/5\), and the angular source \(-Wl-h(1-8\eta^2)+(D+4d)\eta J_0'\) is at least \(-h\). Variation of constants in \(Q_s'+(1+l)Q_s=S_q\) gives at its end
\(Q_s\ge e^{-8/5}-h>1/10\). One may use \(e^2<9\) to verify the last inequality. The same formula gives a positive bound throughout this unit. Since \(b_s=0\) and \(4/5\le a\le2\), O5.1 continues to hold.

On the axial transition, \(l=0\) and the original source is
\[
S_q=-h(1-2k\eta^2)+(D+dk)\eta J_0',\qquad
Q_s(y)\ge\tfrac1{10}e^{-y}+D\eta^2(1-e^{-y})-h(1-e^{-y}).
\tag{O5.3}
\]
The inequality uses \(k\ge0\) and \(\eta J_0'\ge\eta^2\). Take \(h\le e^{-T_d}/20\). The negative h term is then at most \(e^{-y}/20\). Splitting at \(y=\log2\), using \(D\ge.49\), proves for example
\[
Q_s(y)\ge\tfrac1{100}(\eta^2+e^{-y}),\qquad 0\le y\le T_d.
\tag{O5.4}
\]
For \(y\le\log2\), \(\eta^2+e^{-y}\le3e^{-y}\), while the retained exponential term is \(e^{-y}/20\). For \(y\ge\log2\), the two positive terms dominate \(e^{-y}/20+.245\eta^2\). Thus the constant here is independent of \(M_d\).

We need a uniform axial-source bound to justify choosing \(M_d\) first. Write \(\mathcal A_XU=\bar k\eta\); then \(0\le k,\bar k\le4\) and \(W=1-L\bar k\) is bounded by fixed constants. Choose \(M_d\) large enough that \(e_d\le1\). The geometric portion
\(-Wk'\eta-A(1-2k\eta^2)k\eta-(D+dk)\eta k\)
is bounded by \(C|\eta|\), with C independent of \(M_d,T_d,P_*\). For the pressure portion use O4.3. Every unedited later E is bounded by \(E(y)e^{-(v-y)/2}\) for \(v\ge y\), and its logarithmic parameter derivative has magnitude at most \(|J_0'|\). The full future angular correction may be omitted in this backward pressure integral because its total pressure increment is zero. Thus
\[
|\Pi|\le E^2/2,\quad |\Pi_\eta|\le |J_0'|E^2,
\qquad |-d\Pi_\eta+4A\eta\Pi+2\eta\mathcal D_X\Pi|\le C|\eta|E^2.
\tag{O5.5}
\]
The last term is exactly \(\eta E^2\). At the start of the first unit transition the radial formula \(N_s=X^{-1}\int_0^XS_n\,dx\) gives \(|N_s|\le C|\eta|(1+P_*^2)\): its geometric terms are bounded odd functions of \(\eta\), and its pressure terms are bounded by \(CP_*^2|\eta|\). Integrability of the inner powers and the fixed first transition preserve this bound to the axial start. The pressure bound is independent of the later transition length, by the exponential estimate just used. Solving \(N_s'+N_s=S_n\) on the axial interval, with \(E^2=P_1^2f^2e^{-y}\), gives
\[
|N_s|\le C|\eta|\{1+P_1^2(1+y)e^{-y}\},\qquad
\frac{|N_s|}{E^2}\le C|\eta|\left(\frac{e^{T_d}}{P_*^2}+1+y\right)
\le C|\eta|(1+y).
\tag{O5.6}
\]
We used \(f\ge1/2\), \(P_1\asymp P_*\) with fixed comparison constants, and \(P_*>e^{T_d}\). This proves the stated C can be chosen independently of \(M_d\).

Since \(b_s=2k'\eta/E\), O5.4–O5.6 yield
\[
|b_sw|\le C e_d\frac{\eta^2}{\eta^2+e^{-y}}\le C e_d,
\qquad b_s^2\le C e_d^2e^{T_d}/P_*^2.
\tag{O5.7}
\]
Here \(a=2\). Choose \(M_d\) first so \(Ce_d<1/8\), and \(P_*\) later sufficiently large that the second bound is less than \(1/4\). Then \(a-b_sw>15/8\) and \(2b_sw+b_s^2/a<3/8<2\). This proves both strict cone tests throughout the axial interval without a circular parameter choice.

## O6. The intermediate interval and the pulse cone

The equation \(\bar k'=k-\bar k\) and the last eleven units with k zero give \(\bar k(T_d)\le4e^{-11}\), so \(L\bar k<1/2\). On the next unit transition U is zero and \(W=1-L\bar k\ge1/2\). Set
\[
c_\eta=D\eta J_0'=\frac{2D\eta^2}{1+\eta^2}.
\tag{O6.1}
\]
On that transition \(S_q=(-l)W-h+c_\eta\). The positive incoming value in O5.4 and variation of constants retain a positive lower bound depending only on the preceding choices, uniformly for small \(\lambda\) and h. On this finite interval w is bounded by \(C_{\rm pre}\); hence \(\sqrt\lambda|w|\) is small after choosing \(\lambda\). With \(b_s=0\) and \(2\le a\le2+2\lambda\), O5.1 follows. The admissible cone applies wherever \(l<0\), and the relaxed cone at its initial endpoint.

On the constant-slope interval let \(\alpha=1-\lambda\) and \(\bar k=\bar k_0e^{-y}\). The angular equation is exactly
\[
Q_s'+\alpha Q_s=\lambda-h+c_\eta-\lambda L\bar k_0e^{-y}.
\tag{O6.2}
\]
The incoming value has a lower bound \(c_{\rm pre}(1+\eta^2)\). Since \(L\bar k_0<1/2\) and \(h<\lambda/4\), the right side is at least \(\lambda/4+c_\eta\). Its positive convolution proves the first of the following bounds; direct integration proves the second:
\[
\begin{split}
Q_s&\ge c_{\rm pre}(\eta^2+\lambda+e^{-\alpha y}),\\
Q_s-\frac{\lambda-h+c_\eta}{\alpha}
&=e^{-\alpha y}\left[Q_s(0)-\frac{\lambda-h+c_\eta}{\alpha}-L\bar k_0(1-e^{-\lambda y})\right]
=O_{C^1_\eta}(C_{\rm pre}(1+y)e^{-\alpha y}),\\
|N_s/E|&\le C_{\rm pre}|\eta|(1+y)e^{-(1/2-\lambda)y}.
\end{split}
\tag{O6.3}
\]
For the last line, U zero removes every geometric axial-source term. O5.5 bounds the pressure source by \(C|\eta|E^2\). Its convolution with \(e^{-y}\), and \(E^2=E(0)^2e^{-(1+2\lambda)y}\), gives \(C_{\rm pre}|\eta|(1+y)e^{-y}\) for N. Divide by the exact E. One parameter derivative gives the same bound with the \(|\eta|\) factor removed. Since \(|\eta|/(\eta^2+e^{-\alpha y})\le\frac12e^{\alpha y/2}\),
\[
\sqrt\lambda|w|\le C_{\rm pre}\sqrt\lambda(1+y)e^{\lambda y/2}=o(1),
\qquad 0\le y\le60\log(1/\lambda).
\tag{O6.4}
\]
The last limit is uniform on that interval: its right side is at most \(C_{\rm pre}\sqrt\lambda(1+60\log(1/\lambda))e^{30\lambda\log(1/\lambda)}\), which tends to zero. Thus \(a=2+2\lambda,b_s=0\) satisfy both cone tests there.

For the pulse retain \(m=\mathcal A_XU/E\), \(\beta=1/2-\lambda\), and the actual R in O0.5, including both end bumps. Differentiating the radial average gives the exact equation
\[
m'+\beta m=R_b.
\tag{O6.5}
\]
Extend R by zero to negative y. The main pulse is flat at its start; the later bumps have exponentially small fixed \(\zeta_b\) derivatives. Its convolution solution and Taylor's formula give
\[
\begin{split}
m(y)&=m(0)e^{-\beta y}+\int_0^\infty e^{-\beta v}R_b(y-v)\,dv\\
&=\frac{R_b}{\beta}-\frac{\lambda\partial_{\zeta_b}R_b}{\beta^2}
+O(C_{\rm pre}\lambda^2)+m(0)e^{-\beta y}.
\end{split}
\tag{O6.6}
\]
The remainder is bounded by \(\frac12\lambda^2\|\partial_{\zeta_b}^2R_b\|_\infty\int_0^\infty e^{-\beta v}v^2dv\). The same argument works after one \(\eta\) derivative. The initial m and its derivative are \(O(C_{\rm pre}\lambda^{29})\) by O1.2. The fixed point amplitude estimate O3.7 and O1.5 give \(\|m_\eta\|_\infty\le C_{\rm pre}\lambda(1+\log(1/\lambda))\).

On the pulse, \(W=1-2D\eta Em-d(Em)_\eta\). Since \((\log E)_\eta=-J_0'\), the angular source is \(\lambda-h+c_\eta+O(C_{\rm pre}E)\). The initial angular discrepancy is bounded by O6.3 at \(T_w\); \(E\le C_{\rm pre}\lambda^{30}\) throughout the pulse. Convolution with \(e^{-(1-\lambda)y}\) therefore proves
\[
Q_s=\frac{\lambda-h+c_\eta}{1-\lambda}+O(C_{\rm pre}\lambda^{28}).
\tag{O6.7}
\]
The weakened power 28 retains the source's estimate. To bound all terms of N, integrate the original S: \(dS/dy=XE^2(R_b^2-1/2)\). The ratio \(XE^2/(X_pe_b^2f^2)\) is between \(e^{-26}\) and one on the pulse. Its length is \(13/\lambda\), R and its first parameter derivative are bounded, and O1.2 controls the incoming moment. Thus
\[
\left\|S/(XE^2)\right\|_{C^1_\eta}\le C_{\rm pre}e^{26}/\lambda.
\tag{O6.8}
\]
The canonical pressure and its parameter derivative are \(O(E^2)\) by O4.3, omitting the complete later pressure-preserving correction. Substitute \(M/X=Em\), \(U=ER_b\) into the complete formula G2.5. In particular \((M-\eta M_\eta)/(XE)=m-\eta m_\eta+\eta J_0'm\). The S and pressure terms are \(O(C_{\rm pre}E/\lambda)\), and \((1-W)R_b=O(C_{\rm pre}E)\). This proves the full source formula
\[
N_s/E=-R_b+(D+c_\eta)m-D\eta m_\eta+O(C_{\rm pre}\lambda^{27}).
\tag{O6.9}
\]
All pressure and moment contributions have thus been bounded rather than omitted.

Divide O6.9 by O6.7. The factor \(|\eta|/(\lambda+c_\eta)\le C/\sqrt\lambda\) and the m derivative bound make its parameter term \(o(1)\). The Taylor remainder divided by Q is \(O(\lambda)\); the incoming exponential term and angular error give smaller powers. Since \(D+c_\eta-\beta=\lambda-h+c_\eta\), the coefficient of R is \((1-\lambda)/\beta=2+O(\lambda)\). Therefore, uniformly on the whole pulse,
\[
w=2R_b-C_d\partial_{\zeta_b}R_b+o(1),\qquad
C_d=\frac{\lambda(D+c_\eta)(1-\lambda)}{\beta^2(\lambda-h+c_\eta)},\qquad
0\le C_d\le2+o(1).
\tag{O6.10}
\]
The quotient \((D+c)/(\lambda-h+c)\) decreases for \(c\ge0\), because its derivative has numerator \(\lambda-h-D=\lambda-1/2<0\). Its maximum occurs at zero; taking \(\lambda\downarrow0\) and then \(h/\lambda\downarrow0\) gives the stated upper limit. This is compatible with O0.2.

The exact other shear is
\[
a=2+2\lambda,\qquad b_s=-(1+2\lambda)R_b+2\lambda\partial_{\zeta_b}R_b=-R_b+O(\lambda).
\tag{O6.11}
\]
Apart from exponentially small end bumps, R is nonnegative and \(\partial_{\zeta_b}R_b\le1.2\): the derivative of \(\varphi_b\) is at most one, and differentiating its terminal cutoff gives a nonpositive term. Both R and every fixed shape derivative have finite uniform bounds. Choose \(\lambda,h\) small enough that \(1.2C_d\le2.41\). The exact quadratic maxima then give
\[
\begin{split}
b_sw&\le\sup_{R\ge0}(-2R^2+2.41R)+o(1)
=\frac{58081}{80000}+o(1)<.74,\\
2b_sw+b_s^2/a+(a-2)w^2
&\le\sup_{R\ge0}(-3.5R^2+4.82R)+o(1)
=\frac{58081}{35000}+o(1)<1.68.
\end{split}
\tag{O6.12}
\]
The rational gaps to the stated upper bounds are \(1119/80000\) and \(719/35000\). Choose the finitely many uniform o(1) terms smaller than half these gaps. This is possible by the explicit preceding bounds, involving \(\lambda\), \(\sqrt\lambda\log(1/\lambda)\), exponentially small terms and \(h/\lambda\). Negative shape derivatives only decrease the cross terms, so no lower bound on that derivative is needed. Consequently \(a-b_sw>1\), the second expression is less than 2, and \(v_s\ge a>2\). This proves the admissible cone test throughout the actual pulse, including its correcting bumps.

## O7. Interpolation, the steep hold and the terminal half-interval

After the pulse \(U=M=J=0\) exactly, hence \(W=1\). Before the angular bumps the interpolation source is \(-l-h+\vartheta_fc_\eta\), at least \(\lambda-h\). Its integrating coefficient \(1+l\) has fixed bounds, and the pulse endpoint Q is bounded below by \(c\lambda\). Thus \(Q_s\ge c\lambda\) through interpolation and the uniform interval. On the two bumps the perturbations of l and \((\log E)_\eta\) are \(O(C_{\rm pre}\lambda^{28})\), by O2.4, and their total logarithmic length is fixed. Variation of constants changes Q by that same order. It therefore remains at least \(c\lambda\) there, with a smaller fixed c.

The already established \(S(\infty)=0\), together with U zero, gives the exact backward identity
\[
S(X)/X=\frac1{2X}\int_X^\infty E(X',\eta)^2\,dX'.
\tag{O7.1}
\]
Before the exterior release, \(l\le-\lambda/2\), including the angular bumps, so the remaining pre-release integral is bounded by \(CXE^2/\lambda\). The release contribution is bounded by O3.2 and is no larger than another \(CXE^2\), since \(XE^2\) decreases before release up to bounded bump factors. The same proof after a parameter derivative uses the bounded logarithmic parameter derivatives and small angular-coefficient derivatives. Also O4.3 gives \(|\Pi|+|\Pi_\eta|\le CE^2\). Thus
\[
\frac{|S|+|S_\eta|}{X}\le CE^2/\lambda,\quad
|N_s|\le CE^2/\lambda,\quad |w|\le CE/\lambda^2=o(1).
\tag{O7.2}
\]
The last statement uses \(E\le C_{\rm pre}\lambda^{30}e^{-13/(2\lambda)-13}\) at pulse end, with a nonincreasing unedited profile and small relative bumps thereafter. Here \(b_s=0\), and \(2<a\le2+2\lambda+.2+O(C_{\rm pre}\lambda^{28})\). The two cone margins are positive; \(v_s=a>2\).

From the release start onward E is independent of \(\eta\), as are its remaining moment integrals. Equations O4.3, O7.1 and G2.5 therefore give the exact formula
\[
N_s=2\eta\int_y^\infty(he^{v-y}-A)E(v)^2\,dv.
\tag{O7.3}
\]
Every subsequent slope satisfies \(l\le-3h/4\). Hence
\[
E(v)^2\le E(y)^2e^{-(1+3h/2)(v-y)},\quad
h\int_y^\infty e^{v-y}E(v)^2dv\le\tfrac23E(y)^2,\quad
\int_y^\infty E(v)^2dv\le\frac{E(y)^2}{1+3h/2}.
\tag{O7.4}
\]
Thus \(|N_s|\le CE^2\) with a constant independent of h. Before and during the steep hold Q is at least \(c\lambda\); during that hold it increases by O2.5. Hence \(|w|\le Ce_{\rm rel}/\lambda=o(1)\) there. After the steep hold, its next transition retains a large positive Q, the \(-h\) hold decreases it only to \(Q_p\asymp h\), and O2.8 gives \(Q_s\ge ch\) on the first half-unit of the terminal interval. The exact \(h^6\) amplitude drop in O3.1 yields
\[
E\le Ce_{\rm rel}h^6,\qquad |w|\le Ce_{\rm rel}h^5=o(1)
\tag{O7.5}
\]
on that latter range. This remains small even if h is much smaller than \(e_{\rm rel}\); no reversed parameter order is used. Throughout the release range in question \(b_s=0\), \(2<a\le4\), so O5.1 holds and \(v_s=a>2\). The endpoint collar after terminal coordinate \(1/2\) is intentionally not included in this conclusion: it is the source's separate heat and endpoint-stress construction.

## O8. One finite parameter choice and the resulting reference profile

Choose the fixed shapes, \(T_f\), and \(c_o\) as in O0. Select \(M_d\) to meet O5.7, define \(T_d\), then choose \(P_*\) as there. All constants denoted \(C_{\rm pre}\) are now fixed. Select \(\lambda>0\) sufficiently small to meet the finite list of moment-solve conditions O2.4, the root bracket O3.4–O3.7, the bounds O6.4, and the parts of O6.12 and O7.2 depending on \(\lambda\). All their controlling quantities tend to zero. Finally select h sufficiently small relative to this \(\lambda\) and \(e^{-T_d}\) to meet O5.4, O6.2, O6.10–O6.12 and the positive holding-length condition O2.7. Include also the finite outer heat-stress requirement of [H5.5](heat-exterior-stress-audit.md), with its constant uniform for small h and the already fixed amplitude \(e_{\rm rel}\). The h-uniform bounds in O3.2 and O7.4 ensure that making h smaller does not undo any preceding smallness condition. This proves existence of a single finite parameter choice for the entire schedule.

For any fixed \(x_*\in(0,1]\), the remaining radial range from \(X=x_*X_R\) through terminal coordinate \(1/2\) is a compact interval in \(x=X/X_R\), after these choices. The proof gives positive Q and strict O5.1 throughout it. All a, \(b_s\), w are continuous and bounded there. Their image is therefore a compact subset of the strict set in G6.4–G6.5, with positive minimum gaps. The exact comparison G3.7 proves that these quantities are independent of \(X_R\), while
\[
p_{s,1}=X_R\frac{xQ_s(x,\eta)}{L},\qquad
\min_{x,\eta}\frac{xQ_s(x,\eta)}L>0.
\tag{O8.1}
\]
Choose \(X_R\) large enough that the left side exceeds the finite threshold \(P_K\) of G6.5 everywhere. The relaxed cone follows on the entire specified compact interval. The admissible cone follows wherever \(v_s>2\), in particular throughout the intermediate power-law interval, pulse, interpolation and exterior release, and at every point with \(l<0\) in the transition into the intermediate interval. This is precisely the range in Proposition A.4. All stage boundaries divided by \(X_R\) are independent of \(X_R\) and \(\eta\).

The reference profile has positive E, smooth U and E for \(X>0\), \(M=J=U=0\) after the pulse, \(S(\infty)=0\), \(\int_0^\infty(H-H_{\rm pow})\,dX=0\), and the four unchanged reserved patches. Beyond the terminal interval it equals the stated \(\eta\)-independent power law. Its canonical pressure has the analyticity, sign, size and scale-independence properties of Lemma A.5. These conclusions establish those two source components. They do not replace the power exterior by a heat flow, construct the regular axis, prove the endpoint stress direction, or complete Theorem 4.6.

The receiving heat construction is derived in [H0–H7](heat-exterior-stress-audit.md): the exact heat replacement, three restored moments, backward stress with the actual reference axis traces, strict terminal cone, flat factors and smooth endpoint direction. The analytic regular-axis solution and its endpoint inequality are derived in [J0–J7](analytic-axis-profile-audit.md). Its continuation and exact matching to this exterior are derived in [Q0–Q9](inner-outer-joining-audit.md). The subsequent shear modification and every leading-profile property of Theorem 4.6 are derived in [V0–V7](shear-realization-audit.md). The positive-order base is derived in [Z0–Z8](base-field-realization-audit.md). The complete theorem and its proof dependencies are stated in the [theorem construction](theorem-audit-conclusion.md).
