# Incoming phase neighborhoods for Dirichlet waves

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="diffractive-phase-neighborhoods"></a>

This reading constructs the incoming phase neighborhood required at a strict diffractive contact. The symbol has positive Hamilton derivative near the contact, its real-root divided difference has the Dirichlet boundary sign, and its principal cutoff error is supported in a prescribed regular interior neighborhood of the incoming leg. We also prove rapid semiclassical bounds for the full-phase operator supported on that error. Sections 5–7 prove smoothness of the divided weight’s square root at all its zeros, construct a nonnegative elliptic extension and quantize an exactly positive boundary form over the whole weight. Sections 8–11 prove a bulk square estimate on this whole phase neighborhood, with the actual full-phase edge, the equation contribution and an explicit unlocalized energy remainder. Sections 12–13 confine the elliptic completion to the nonvanishing shifted weight and prove weighted bounds for its operator errors. Sections 14–18 control every bulk remainder and forcing pairing by larger shifted weights, and use two positive squares to recover the full local energy. Sections 19–21 control the forcing created by spatial localization of the fixed spectral wave reduction and prove a conditional semiclassical half-step gain. Sections 22–26 construct a tangential Sobolev-regularized Dirichlet family, prove its exact first-order commutator and uniform norm bounds, and verify its cutoff-forcing and incoming-edge estimates. Sections 27–31 control all three regularizer commutator energy pairings with uniform lower-norm remainders. Sections 32–35 recover the full local energy uniformly in the regularizer and prove a half-order Sobolev gain from the explicit larger-weight hypothesis. Section 36 gives the fixed-neighborhood induction criterion. Sections 37–40 prove the tangentially elliptic boundary input by positive normal energy and a full-order Sobolev induction on one fixed open set. Sections 41–47 prove local reflection at separated normal roots and interior propagation for the actual wave, including exact mode coupling, transported cutoffs and fixed-neighborhood regularity. Sections 48–50 prove a two-root reachable region, continuity through tangency, the regularity of its incoming and transversely reflected legs, and containment of the entire larger diffraction weights. Sections 51–54 prove finite-order outgoing transport, simultaneous induction on the fixed two-root region, and normal smoothness from the actual equation. This establishes strict-diffraction regularity for the fixed H² Dirichlet wave. Sections 55–62 prove a local cone-regularity estimate at arbitrary glancing contacts, using nested phase tubes, the actual Sobolev regularizer and a two-component energy recovery. Sections 63–70 construct a curve in the closed compressed singular set and prove that it satisfies the exact inward-reaction relation (G1)–(G23), including all glancing orders and accumulating reflections. This proves the singular-curve theorem for the actual H² wave on homogeneous time intervals. Sections 71–75 prove the Cauchy-data endpoint argument, including smoothness near the initial wall from compatible collar data, and transfer propagation to every compact interior distributional datum in the spectral Dirichlet realization. Sections 76–79 prove uniform regularity for bounded families of homogeneous Dirichlet waves and a quantitative estimate for nearby operators with no returning ray. This controls all target derivatives of smooth waves by their H² norm, uniformly up to the wall. Sections 80–89 extend the estimate to rough source columns approaching the wall and prove joint parameter, time, source and target regularity of the actual no-return kernels. The complete scaled comparison and both curved spectral bounds are proved in [the spectral reading](curved-boundary-spectral-reduction.md#scaled-reflected-parametrix), Sections 31–38. 

The freely accessible comparison is [Victor Ivrii, *Microlocal Analysis, Sharp Spectral Asymptotics and Applications*, author version of 9 July 2023](https://www.math.utoronto.ca/ivrii/Victor_Ivrii_Microlocal_Analysis,_Sharp_Spectral_Asymptotics_and_Applications.pdf), printed pp. 259–266, especially the phase neighborhood in (3.4.45) and the separate errors in (3.4.42). The phase choice and the regular-edge bound are proved below; the source's brief assertion about those errors is not used as a programme proof.

A second comparison is Lars Hörmander, [*The Analysis of Linear Partial Differential Operators III*, 2007 reprint](https://doi.org/10.1007/978-3-540-49938-1), Lemmas 24.4.3–24.4.4, printed pp. 445–446, for completion of the quadratic form on the elliptic side, and Lemmas 24.4.8–24.4.9, printed p. 452, for square roots of flat divided weights. The two-multiplier argument on printed p. 454 is a further comparison for Sections 18 and 32–35; the parameter-uniform inverse and frequency-summation proof used here are given explicitly below. The distinction between cutoff forcing and Sobolev-regularization commutators in Lemma 24.4.7, printed pp. 449–451, also guides the scope distinction in Sections 19–21; Sections 22–26 give a separate uniform proof of the regularizer and commutator estimates used here. Sections 27–31 absorb the actual commutator energy term using a scalable flat transport weight and lower-norm remainder estimates. The two-root reachable region on printed pp. 448–449 is a further comparison for Sections 48–50; the continuity at tangency, actual connecting paths and complete weight supports are proved here. Sections 51–54 complete the finite-order induction here by explicit mode energy, frequency summation and normal-derivative recurrence; printed p. 454 provides a comparison for the separate outgoing-arc step. For Sections 55–62, Proposition 24.5.1 and Lemma 24.5.2, printed pp. 455–458, provide the comparison for the general glancing tube. We prove the local estimate here using an explicit physical-time clock, a scalable flat weight, a normal divided-slope inverse and a fixed-tube Sobolev induction. Sections 63–70 supply the singular-curve construction and its exact inward-reaction laws. The comparisons are Definition 24.3.7, printed pp. 434–435, Lemma 24.3.15, printed pp. 441–442, and the existence conclusion of Theorem 24.5.3, printed pp. 458–459. The compressed interpolation, limit equations, gliding-energy identity and normal-reaction proof are given here. No source propagation or anisotropic regularity theorem is imported as a programme proof. The explicit division, dyadic majorant and square-root proofs below are retained. Sections 12–13 give the support choice and localized operator bounds used here; the source lemmas are comparisons, not replacements for these programme proofs.

The prerequisites are [the smooth-flow proof (G13)](generalized-reflected-curves.md#generalized-reflected-curves), [coordinate inverses](coordinate-inverses-and-integration.md), [smooth quadratic division (C1)–(C17)](quadratic-normal-cutoffs.md#quadratic-normal-cutoffs), and the flat cutoff and its derivative bounds (C18)–(C19) in the same reading. The Fourier definition of wavefront and its localization estimates are proved in [the phase reading](phase-geometry-and-stationary-phase.md#phase-foundations). We retain a compact semiclassical frequency patch away from the zero section; no conic homogeneity of the auxiliary cutoff is needed.

## 1. A normal-frequency coordinate along the flow

Use the gauged wave principal symbol
\[
 p(x,y,s,\eta)=s^2+a_0(x,y,\eta),\qquad x\ge0,
 \tag{T1}
\]
where $x$ is inward normal distance and $y$ includes physical time. At the point $z_*=(0,y_*,0,\eta_*)$ assume
\[
 a_0(0,y_*,\eta_*)=0,\qquad
 -\partial_xa_0(z_*)>0.
 \tag{T2}
\]
The latter is strict diffraction in this convention: $H_p^2x=-2\partial_xa_0>0$. Extend the smooth coefficients across $x=0$ locally. Shrink a full phase neighborhood so that
$\kappa\le c=-\partial_xa_0\le K$,
with positive constants. Then $H_ps=c>0$. The smooth vector field
\[
 V=c^{-1}H_p,\qquad Vs=1,\qquad Vp=0
 \tag{T3}
\]
has a local smooth flow by (G13). Start its trajectories on the section $s=0$, coordinatized by $I=(x,y,\eta)-(0,y_*,\eta_*)$. Its flow map, denoted $\mathcal F(I,s)$, is a coordinate map: at $s=0$ the section directions together with $V$ are independent, since $Vs=1$. The parameter inverse theorem supplies the inverse after shrinking. Its invariant coordinate functions obey
$H_pI=0$, and $\mathcal F(0,0)=z_*$.

The reference trajectory $\Gamma(s)=\mathcal F(0,s)$ stays characteristic. Its normal position satisfies
\[
 \begin{aligned}
 &x(\Gamma(s))=\int_0^s\frac{2u}{c(\Gamma(u))}\,du,\\
 &\frac{s^2}{K}\le x(\Gamma(s))\le\frac{s^2}{\kappa}.
 \end{aligned}
 \tag{T4}
\]
For negative $s$, reverse the integral limits and the sign of $u$ to obtain the same bounds. Thus each punctured leg lies in the interior, with an explicit lower separation from the wall on every closed subsegment. This calculation does not assume a boundary propagation theorem.

Choose an orientation $\nu\in\{1,-1\}$ and a small $\sigma>0$. Let $\mathcal U$ be any prescribed open full-phase neighborhood of the compact leg
$\{\Gamma(s):\sigma\le\nu s\le2\sigma\}$,
contained in $x>0$. In the later propagation application it is a neighborhood where the solution is already microlocally smooth. Both choices of $\nu$ are allowed; which leg is physically incoming is determined by the time covector. Choose $\sigma$ so that a slightly larger flow box exists. Compactness and continuity allow a number $r_0>0$ such that
\[
 \begin{gathered}
 \mathcal F(I,s)\in\mathcal U,\quad
 x(\mathcal F(I,s))>\frac{\sigma^2}{2K}\\
 \text{if }|I|\le r_0,\quad \sigma\le\nu s\le2\sigma.
 \end{gathered}
 \tag{T5}
\]
Indeed the compact reference segment has positive distance from the closed complement of a smaller neighborhood in $\mathcal U$, and the flow map is uniformly continuous on a compact box. Shrink $r_0$ also so that the closed box $|I|\le r_0$, $|s|\le2\sigma$ lies strictly inside the coordinate chart and its frequency patch.

## 2. A phase whose outer error is on the chosen leg

Choose real smooth cutoffs $\rho(I)$ and $\vartheta(s)$ with values in $[0,1]$, where $\rho=1$ for $|I|\le r_0/2$ and $\rho=0$ for $|I|\ge r_0$, while $\vartheta$ is even, equals one for $|s|\le\sigma$ and vanishes for $|s|\ge2\sigma$. Their supports may be chosen strictly inside the larger flow box. Put $\zeta=\rho(I)\vartheta(s)$. Choose a fixed $\delta>0$ so small that
\[
 \delta\sqrt{3\sigma}<r_0/2,\qquad
 \frac{r_0^2}{4\delta^2}>4\sigma.
 \tag{T6}
\]
These choices precede the small positive shift $\epsilon$. Let $0<2\epsilon<\sigma$, with additional restrictions in Section 3, and define
\[
 \begin{aligned}
 \phi_\nu&=|I|^2/\delta^2-\nu s,\\
 q_\nu&=\nu\zeta^2\chi(\phi_\nu-\epsilon),\\
 \chi(v)&=
 \begin{cases}e^{1/v},&v<0,\\0,&v\ge0.\end{cases}
 \end{aligned}
 \tag{T7}
\]
Extend $q_\nu$ by zero outside the flow box. It is smooth with compact phase support; flatness of $\chi$ treats its level-set boundary, and the other cutoffs have closed interior support. The sign $\nu$ on $q_\nu$ is essential when the chosen regular leg has negative $s$.

Because $I$ is invariant and $H_ps=c$,
\[
 \begin{aligned}
 H_p\phi_\nu&=-\nu c,\\
 H_pq_\nu
   &=-c\zeta^2\chi'(\phi_\nu-\epsilon)+e_\epsilon,\\
 e_\epsilon&=\nu\chi(\phi_\nu-\epsilon)H_p(\zeta^2).
 \end{aligned}
 \tag{T8}
\]
The first term is nonnegative and is strictly positive at $z_*$. We now prove that the closed support of $e_\epsilon$ is contained in $\mathcal U$, not in an unspecified set of cutoff edges.

First $H_p\rho(I)=0$ identically, so a derivative of the invariant cutoff contributes nothing to $H_p(\zeta^2)$. At the opposite end, $\nu s\le-\sigma$ gives $\phi_\nu\ge\sigma>\epsilon$, so $\chi$ and all its derivatives vanish. At the chosen end, $\sigma\le\nu s\le2\sigma$ and $\chi(\phi_\nu-\epsilon)\ne0$ imply
\[
 |I|^2<\delta^2(2\sigma+\epsilon)<3\delta^2\sigma.
 \tag{T9}
\]
Thus $|I|<r_0/2$ by (T6), and (T5) places the point in the prescribed interior neighborhood. The same strict containment holds for the closed support, since all inequalities have fixed margins and the cutoff support is compact.

There is also no hidden side edge for differentiated weights. On the transition of $\rho$, where $|I|\ge r_0/2$ and $|s|\le2\sigma$, (T6) gives $\phi_\nu>2\sigma$. Hence every derivative of $\chi(\phi_\nu-\epsilon)$ vanishes in a neighborhood of that transition. The same assertions hold with $\epsilon$ replaced by $2\epsilon$. This shifted neighborhood is needed for lower-regularity terms; it is not obtained by assuming the solution regular on the entire enclosing box.

At $I=0$ and $0\le\nu s\le\sigma$, the phase is $-\nu s$, the cutoffs are one, and the weight is positive. Thus the retained neighborhood contains $z_*$ and the segment connecting it to the known leg. The invariant radius in (T9) can be made as small as required by choosing $\delta$ after $\mathcal U$ and before $\epsilon$.

## 3. The divided difference has the Dirichlet sign

The phase $\phi_\nu$ need not be affine in $s$ in the original coordinates. Apply the already proved smooth quadratic division directly to the full smooth cutoff $q_\nu$. With $z=(x,y,\eta)$ and $R=-a_0(z)$ it gives
\[
 q_\nu(z,s)=\alpha(z)+s\beta(z)+p(z,s)\mu(z,s).
 \tag{T10}
\]
For $R\ge0$ the coefficients are fixed, rather than arbitrary extensions:
\[
 \begin{aligned}
 \alpha(z)&=\frac{q_\nu(z,\sqrt R)+q_\nu(z,-\sqrt R)}2,\\
 \beta(z)&=\frac{q_\nu(z,\sqrt R)-q_\nu(z,-\sqrt R)}{2\sqrt R}.
 \end{aligned}
 \tag{T11}
\]
At $R=0$ the latter value is $\partial_s q_\nu(z,0)$. All coefficients and the remainder are smooth through merging roots by (C1)–(C17).

We show $\beta\ge0$ at every pair of real roots under consideration, including boundary points. If $\nu=1$ and the value at the negative root vanishes, the numerator in (T11) is nonnegative, since $q_1\ge0$. If $\nu=-1$ and the value at the positive root vanishes, the same numerator is nonnegative, since $q_{-1}\le0$. These observations also treat roots outside the compact cutoff support. The only remaining case is a nonzero value at the root of sign opposite to $\nu$.

Write $r=\sqrt R$. At that root $s=-\nu r$, nonzero weight forces
\[
 r<\epsilon,\qquad
 |I(z,-\nu r)|<\delta\sqrt{\epsilon}.
 \tag{T12}
\]
Choose a fixed small product neighborhood of $z_*$ on which $I(z,s)$ is defined along these short vertical segments, and let $M\ge1$ bound $|\partial_sI|$ there. The inverse flow map and (T12) put the entire segment $|s|\le r$ in that product neighborhood once $\epsilon$ is sufficiently small. More explicitly, its initial point approaches $z_*$ uniformly as the two bounds in (T12) tend to zero; holding $z$ fixed and changing $s$ by at most $2\epsilon$ keeps it in a preselected smaller box. On the segment,
$|I(z,s)|\le\delta\sqrt{\epsilon}+2M\epsilon$.
Require
\[
 \begin{aligned}
 &\epsilon<\sigma,\quad
 \delta\sqrt{\epsilon}+2M\epsilon<r_0/2,\\
 &2M\delta^{-2}
       (\delta\sqrt{\epsilon}+2M\epsilon)<1/2 .
 \end{aligned}
 \tag{T13}
\]
All are possible after $\delta$ is fixed. The cutoffs $\rho,\vartheta$ are then identically one on this whole root interval. Furthermore
$|\partial_s\phi_\nu+\nu|<1/2$ there. Since $\chi'\le0$,
$\partial_s q_\nu=\nu\chi'(\phi_\nu-\epsilon)\partial_s\phi_\nu\ge0$.
The fundamental theorem of calculus between $-r$ and $r$ proves the remaining sign in (T11). For a vanishing root take the continuous limit of the same formulas, or differentiate directly when $a_0=0$. At the center in particular
\[
 \beta(z_*)=-\chi'(-\epsilon)>0
 \tag{T14}
\]
for both orientations. Continuity gives strict positivity on a smaller neighborhood including its elliptic side, so the exact positive boundary quantization (C24) applies there.

The real-root sign alone does not supply a smooth square root at its zeros or a nonnegative elliptic extension. Sections 5–7 below prove those additional properties for this particular flat cutoff and construct the positive boundary form on its whole support.

Applying $H_p$ to (T10), using $H_pp=0$, gives the exact identity
\[
 \begin{aligned}
 H_p(\alpha+s\beta)
  &=-c\zeta^2\chi'(\phi_\nu-\epsilon)\\
  &\quad+e_\epsilon-pH_p\mu .
 \end{aligned}
 \tag{T15}
\]
Thus the normal-linear principal multiplier has the required positive term on the characteristic set and an explicitly located regular-edge term. This is a symbol identity with a retained multiple of the equation; it is not yet an exact operator factorization.

## 4. The actual full-phase edge operator is rapidly small

Let $u$ be a fixed distribution and suppose $\mathcal U$ lies outside its wavefront set, in the interior of the spacetime collar. Multiply $u$ by a fixed interior cutoff that equals one near the compact base projection needed below. For any smooth semiclassical symbol $b_h$ with uniformly bounded derivatives, compact support in a fixed closed subset of $\mathcal U$ and frequency support in a fixed annulus,
\[
 \|\operatorname{Op}_h(b_h)u\|_{H^k}
            =O(h^N)\qquad (k,N\ge0).
 \tag{T16}
\]
This holds also for each fixed semiclassical differential derivative of the output. We give the localization argument to specify precisely what the assertion uses.

Cover the compact phase support by finitely many product patches whose smaller frequency cones have closures inside cones of rapid Fourier decay for a spatially localized $u$. Choose a finite smooth partition of the symbol, and a compact base cutoff $\lambda$ equal to one on a neighborhood of each output support. On the retained cone, the definition of wavefront gives
$|\widehat{\lambda u}(\xi)|\le C_L\langle\xi\rangle^{-L}$ for every $L$. Write $F_h(\theta)=\widehat{\lambda u}(\theta/h)$. The formula
\[
 \begin{aligned}
 &\operatorname{Op}_h(b_h)(\lambda u)(w)\\
 &\quad=(2\pi h)^{-D}
   \int e^{iw\cdot\theta/h}b_h(w,\theta)F_h(\theta)\,d\theta
 \end{aligned}
 \tag{T17}
\]
uses full interior variables $w=(x,y)$, $D=\dim w$, and full frequencies $\theta=(s,\eta)$. In the annulus $|\theta|\asymp1$, the Fourier factor is $O(h^L)$. Every prescribed output derivative costs at most a fixed power of $h^{-1}$; the frequency region and output base support are compact. Taking $L$ arbitrarily large proves the corresponding uniform derivative and $H^k$ bounds.

The remaining input $(1-\lambda)u$ has base support separated from the output support. In its oscillatory kernel apply
$h(w-v)\cdot\partial_\theta/(i|w-v|^2)$
repeatedly to the exponential and transfer it to the amplitude. Each application gives a power of $h$, with bounded coefficients because of separation. Pair the resulting smooth kernel with the compact distribution, whose continuity bounds it by finitely many input derivatives; those derivatives and the requested output derivatives cost only a fixed power of $h^{-1}$. Arbitrarily many integrations prove the same estimates. Summing the finite partition proves (T16). The restriction away from the physical boundary is essential to this particular full-variable argument.

By (T8)–(T9), $b_h=e_\epsilon$ satisfies these hypotheses for every fixed permitted $\epsilon$. The same is true for the shifted edge $e_{2\epsilon}$. Thus their full-phase quantizations satisfy actual rapid bounds, rather than hypothetical bounds on an arbitrary enclosing annulus.

Sections 5–7 below establish the exactly nonnegative boundary form over the whole weight. Sections 8–11 then prove the bulk square estimate with its equation term and actual full-phase edge. Sections 12–13 localize the elliptic completion and its operator errors to the shifted weight. Sections 14–18 supply the corresponding control of the other terms and recover the full local energy. Sections 19–21 control the forcing created by spatial localization of the fixed spectral wave reduction and prove a conditional semiclassical half-step gain. Sections 22–26 construct a tangential Sobolev-regularized Dirichlet family, prove its exact first-order commutator and uniform norm bounds, and verify its cutoff-forcing and incoming-edge estimates. Sections 27–31 control all three regularizer commutator energy pairings with uniform lower-norm remainders. Sections 32–35 recover the full local energy uniformly in the regularizer and prove a half-order Sobolev gain from the explicit larger-weight hypothesis. Section 36 gives the fixed-neighborhood induction criterion. Sections 37–40 prove the tangentially elliptic boundary input by positive normal energy and a full-order Sobolev induction on one fixed open set. Sections 41–47 prove local reflection at separated normal roots and interior propagation for the actual wave, including exact mode coupling, transported cutoffs and fixed-neighborhood regularity. Sections 48–50 prove a two-root reachable region, continuity through tangency, the regularity of its incoming and transversely reflected legs, and containment of the entire larger diffraction weights. Sections 51–54 prove finite-order outgoing transport, simultaneous induction on the fixed two-root region, and normal smoothness from the actual equation. This establishes strict-diffraction regularity for the fixed H² Dirichlet wave. Sections 55–62 prove a local cone-regularity estimate at arbitrary glancing contacts, using nested phase tubes, the actual Sobolev regularizer and a two-component energy recovery. Sections 63–70 construct a curve in the closed compressed singular set and prove that it satisfies the exact inward-reaction relation (G1)–(G23), including all glancing orders and accumulating reflections. This proves the singular-curve theorem for the actual H² wave on homogeneous time intervals. Sections 71–75 prove the Cauchy-data endpoint argument, including smoothness near the initial wall from compatible collar data, and transfer propagation to every compact interior distributional datum in the spectral Dirichlet realization. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. In particular the operator $E_h^{\mathrm{edge}}$ in (L20) comes from a different inner cutoff; its entire support need not lie in $\mathcal U$. Equation (T16) does not silently give its bounds. The [localized estimate](glancing-commutator-estimate.md#glancing-commutator-estimate) remains a valid conditional estimate, while Sections 63–75 supply the full propagation assertion for the spectral Dirichlet solutions required here.

<a id="divided-weight-square-root"></a>

## 5. A smooth square root at the zero weights

We now strengthen the coefficient construction on the entire cutoff, including points where $\beta=0$. Keep $z=(x,y,\eta)$ as a parameter and first regard $R$ as independent. A further smallness choice for $\epsilon$ is permitted in the construction above. Fix a small $a>0$, with $a<\sigma/2$, such that points with $|s|\le a$ and $|I|\le\delta\sqrt{2a}$ lie in the fixed product neighborhood where $|\partial_sI|\le M$, and
$\delta\sqrt{2a}<r_0/2$ and $2M\delta^{-1}\sqrt{2a}<1/2$.
This is possible by the inverse flow chart and then by decreasing $a$. Take $0<\epsilon<a/4$, also satisfying (T13). These choices work for both $\epsilon$ and its shift $2\epsilon$.

Where $|s|\le a$ and $\chi(\phi_\nu-\epsilon)\ne0$, we have $|I|<\delta\sqrt{2a}$. Thus both cutoffs are one there and $|\partial_s\phi_\nu+\nu|<1/2$. Consequently the function
$g(z,s)=\partial_s q_\nu(z,s)$
is nonnegative on this whole small $s$ interval, for every retained $z$. On its positive set it is comparable, with fixed positive constants, to $-\chi'(\phi_\nu-\epsilon)$. Where the latter vanishes, all derivatives of $g$ vanish as well. The chain rule and (C19), applied to $-\chi'$, prove
\[
 \begin{gathered}
 |D^\alpha g(z,s)|
       \le C_{\alpha,\gamma}g(z,s)^{1-\gamma},\\
 |s|\le a,\quad 0<\gamma<1 .
 \end{gathered}
 \tag{T18}
\]
Here $D^\alpha$ includes arbitrary mixed derivatives in $z,s$. Indeed on the nonzero set $g=\nu(\partial_s\phi_\nu)\chi'(\phi_\nu-\epsilon)$ with the first factor bounded away from zero in absolute value; all its derivatives and those of $\phi_\nu$ are bounded on the compact patch. Every differentiated term is therefore bounded by a constant times $(-\chi')^{1-\gamma}$. On the zero set the same inequality follows from flatness. No derivative assumption on the outer cutoffs at their zeros is needed here: they are identically one wherever this small-$s$ weight can be nonzero.

We prove an averaging fact to control the divided difference without factors singular at $R=0$. For $0\le R\le a^2$, set
\[
 b_+(z,R)=\frac12\int_{-1}^1g(z,t\sqrt R)\,dt.
 \tag{T19}
\]
It is smooth up to $R=0$ by the even-function proof (C1)–(C3). If $r=\sqrt R>0$, write
$A=\max_{|s|\le r}g(z,s)$.
The derivative estimate (T18) implies $|\partial_s g|\le C_\gamma A^{1-\gamma}$ on that interval. Starting at a maximum point, choose the direction with available interval length at least $r$. On a subinterval of length
$\min(r,A^\gamma/(2C_\gamma))$
the value is at least $A/2$. Integration over $[-r,r]$ shows
\[
 \begin{aligned}
 A^{1+\gamma}&\le C_\gamma b_+(z,R),\\
 A&\le C_\gamma b_+(z,R)^{1/(1+\gamma)} .
 \end{aligned}
 \tag{T20}
\]
To see the first inequality uniformly, divide $g$ by a fixed upper bound to make $A\le1$. Its average is at least
$A\min(1,A^\gamma/(2C_\gamma r))/4$;
since $r\le a$, this is at least a fixed multiple of $A^{1+\gamma}$. Restoring the upper bound only changes constants. At $r=0$ the same inequalities hold because $A=b_+(z,0)$ is bounded. The case $A=0$ is immediate.

Each $\partial_z^\alpha\partial_R^\ell b_+$ is bounded by a constant times the supremum of derivatives of $g$ through order $|\alpha|+2\ell$ on $[-r,r]$. This is the explicit repeated integral operation (C2): differentiate the even function in $r$ twice, integrate at contracted values of $r$, and repeat. The factors from differentiating $g(z,tr)$ are powers of the integration variables of absolute value at most one. There are finitely many such integrals for each order, all over fixed compact intervals with bounded total weights. Hence (T18) and (T20) give a bound by
$C b_+^{(1-\gamma)/(1+\gamma)}$.
Given any $0<\lambda<1$, choose $\gamma$ so small that $(1-\gamma)/(1+\gamma)>1-\lambda$ and use boundedness of $b_+$ to obtain
\[
 |\partial_z^\alpha\partial_R^\ell b_+|
        \le C_{\alpha,\ell,\lambda}b_+^{1-\lambda}.
 \tag{T21}
\]
At a zero of $b_+$ these derivatives vanish. This estimate concerns the divided coefficient itself, not just its two endpoint values.

On $\{b_+>0\}$ differentiate $S_+=\sqrt{b_+}$. A derivative of positive total order $m$ is a finite sum of products
$C b_+^{1/2-j}\prod_{i=1}^j D^{\alpha_i}b_+$,
where $1\le j\le m$ and each $\alpha_i$ has positive order. Formula (T21) bounds each such term by $C b_+^{1/2-j\lambda}$. Taking $\lambda<1/(4m)$ shows that every derivative through order $m$ tends to zero at the zero set:
\[
 |D^\alpha S_+|\le C_\alpha b_+^{1/4}
 \quad(1\le|\alpha|\le m)
 \tag{T22}
\]
after increasing constants on the bounded range of $b_+$. Define these derivatives to be zero on that set. They are the actual continuous derivatives. For a coordinate segment ending at a zero, split its positive portion into component intervals; the fundamental theorem bounds each change by interval length times the supremum of the proposed derivative, and at zero endpoints the function is zero. This proves differentiability there with derivative zero. Repeat for the derivative functions just obtained. Segments in $R$ at zero are taken from the right. Thus $S_+$ is smooth in all variables up to $R=0$, including arbitrary parameter derivatives and all zero weights.

This covers $r\le a$. For $r\ge a/2$, the wrong-sign root has $|s|\ge a/2>\epsilon$, so its cutoff is zero as in Section 3. The exact remaining formula is
$b_+(z,R)=\zeta(z,\nu r)^2\chi(\phi_\nu(z,\nu r)-\epsilon)/(2r)$.
Its nonnegative square root is
$\zeta(z,\nu r)\sqrt{\chi(\phi_\nu(z,\nu r)-\epsilon)}/\sqrt{2r}$,
which is smooth because $r$ is bounded away from zero and $\sqrt\chi$ is smooth and flat. The two square roots agree pointwise on the overlap, hence give a smooth square root on the full retained real-root region. The same proof applies to the shifted cutoff $2\epsilon$, since $2\epsilon<a/2$.

## 6. A nonnegative extension with exact division

Extend the smooth one-sided function $S_+(z,R)$ across $R=0$ using the explicit summation (C4)–(C5); call the extension $S(z,R)$. It need not be nonnegative for negative $R$. Its square is nonnegative and matches $b_+$ and all its derivatives on the real-root side. This avoids the unjustified assumption that an arbitrary extension of $b_+$ itself preserves its sign.

The extension can retain compact parameter support and can be confined to a prescribed small negative-$R$ collar. The one-sided jets of $S_+$ have compact parameter support, since $q_\nu$ does. Their summation coefficients have that same support. Choose every cutoff radius in (C5), including the zeroth, inside the desired collar, and multiply the negative-side extension by a cutoff equal to one near zero if needed. These operations leave every boundary jet unchanged. An additional parameter cutoff equal to one on the union of the jet supports also leaves every boundary jet unchanged. Gluing to the unchanged $S_+$ on $R\ge0$ remains smooth by the proved extension argument.

There is a useful more precise support choice. At $R=0$ the jets of $S_+$ vanish unless $\phi_\nu(z,0)\le\epsilon$. Indeed where $\phi_\nu(z,0)>\epsilon$ the original cutoff is identically zero in an $s$ neighborhood, and at equality all its jets, and then those of $S_+$ by (T21)–(T22), vanish. Choose the negative-side parameter cutoff equal to one on this compact set and supported in $\phi_\nu(z,0)<3\epsilon/2$, within the original compact patch. On its closure the shifted divided coefficient at $R=0$ is strictly positive, with a uniform positive lower bound: its value is
$\nu\,\partial_s\phi_\nu(z,0)\chi'(\phi_\nu(z,0)-2\epsilon)$,
whose two factors have the required strict signs by the smallness choices in Section 5. First construct a square-root extension for the shifted weight. By continuity it stays bounded away from zero on this compact parameter support for sufficiently small negative $R$. Then choose the extension collar for $S$ inside that region. Thus the elliptic-side adjustment for the smaller weight can be supported where the shifted boundary weight is nonvanishing. This is a support statement for the boundary coefficient, not an interior propagation estimate.

Let $b(z,R)$ be the previous, possibly signed smooth extension used in quadratic division, and put $\Delta=S^2-b$. It is identically zero for $R\ge0$ and is smooth across zero. Therefore Taylor's formula at zero gives, for every fixed derivative and every $L$,
$|\partial_z^\alpha\partial_R^\ell\Delta|\le C_{\alpha,\ell,L}|R|^L$ on the negative side. The correction needed for the division remainder is
\[
 E=
 \begin{cases}
 s\Delta(z,R)/(s^2-R),&R<0,\\
 0,&R\ge0.
 \end{cases}
 \tag{T23}
\]
It is smooth. Away from $s=R=0$ the denominator is nonzero across the gluing set. Near that corner put $\omega=(s^2+|R|)^{1/2}$. The reciprocal-denominator derivative bound proved in (C16), together with the flat bounds on $\Delta$, gives
$|\partial_z^\alpha\partial_s^k\partial_R^\ell E|
\le C\omega^{2L-1-k-2\ell}$
after taking enough orders of flatness for the finitely many differentiated numerator terms. Since $L$ is arbitrary, every derivative tends to zero at the corner. Gluing these derivatives by the fundamental theorem proves smoothness, with zero jets there. This explicitly checks the division correction at the merging roots.

Keep the old average coefficient $a(z,R)$ and replace $b$ by $S^2$ and the old remainder $\mu$ by $\mu-E$. The division identity is still exact, because $s\Delta=(s^2-R)E$:
\[
 \begin{aligned}
 q_\nu(z,s)
   &=a(z,R)+sS(z,R)^2\\
   &\quad+(s^2-R)(\mu-E)(z,s,R).
 \end{aligned}
 \tag{T24}
\]
Now substitute $R=-a_0(z)$. This gives (T10)–(T15) with $\beta(z)=S(z,-a_0(z))^2\ge0$ on both sides of the glancing set. All real-root values, the actual cutoff $q_\nu$ and the support of its full-phase edge $e_\epsilon$ are unchanged. The multiple of the equation in (T15) uses the adjusted smooth remainder and must still be retained in its later quantization.

<a id="whole-weight-boundary-form"></a>

## 7. Quantizing the whole boundary weight

Write $s_0(z)=S(z,-a_0(z))$ on the retained compact tangential phase patch. With an outer tangential cutoff equal to one on the coefficient support if necessary, $s_0$ is smooth and compactly supported, including at every zero of the weight. No restriction to the smaller neighborhood where $\beta$ is strictly positive is required. Set
\[
 \begin{aligned}
 S_h&=\operatorname{Op}_h(s_0),\qquad B_h=S_h^*S_h,\\
 A_{0,h}&=\tfrac12\bigl(\operatorname{Op}_h(\alpha)
                         +\operatorname{Op}_h(\alpha)^*\bigr),\\
 A_h&=A_{0,h}+\tfrac12(B_hd_x+d_xB_h).
 \end{aligned}
 \tag{T25}
\]
The finite tangential calculus in (N19)–(N23) gives the principal symbols $\alpha,\beta$ and uniform bounds for these tangential factors and each fixed normal derivative. The lower terms are the actual product and adjoint terms; they have not been set to zero. The exact boundary commutator calculation (D5)–(D8), applied to this $A_h$, gives for a smooth Dirichlet input $u$ vanishing near the outer normal endpoint and $f=P_hu$,
\[
 \begin{aligned}
 &\left(\frac ih[P_h,A_h]u,u\right)
          +\|S_h(0)d_xu(0)\|^2\\
 &\qquad=\frac2h\operatorname{Im}(f,A_hu).
 \end{aligned}
 \tag{T26}
\]
The boundary term is exactly nonnegative on the whole weight. There is no boundary error from applying a positivity theorem to left quantization. Expansion of $d_xB_h=B_hd_x-ihB_h'$ gives the same uniform bound $\|A_hu\|\le C(\|u\|+\|d_xu\|)$ as (C26). The exact bulk expansion is (C27), including $\operatorname{Re}(B_h'f,u)$. Thus every term is defined for the $H^2$ Dirichlet inputs supplied by the earlier negative-order wave reduction. The odd-mollification and trace argument following (C28) proves (T26) for that domain as well; it uses precisely the bounded factors and derivatives just verified.

This closes the smooth-square-root and full-boundary-sign steps for the incoming cutoff, for either orientation. The following sections convert the positive principal expression in (T15) into an actual bulk square estimate, keep the equation contribution and recover the full-phase edge of (T16). The last section states exactly what remains before propagation can be claimed.

<a id="whole-phase-bulk-estimate"></a>

## 8. A positive quadratic form across the elliptic side

Keep the fixed phase neighborhood and its shift $\epsilon$. Put $z=(x,y,\eta)$ and $R=-a_0(z)$. Define the smooth full-phase function
\[
 j(z,s)=\sqrt{c(z)}\,\zeta(z,s)
            \sqrt{-\chi'(\phi_\nu(z,s)-\epsilon)}.
 \tag{T27}
\]
The square root is smooth and flat by (C18)–(C19). The factor $c$ is positive on a neighborhood of the support; extension by zero outside that neighborhood is smooth. Thus $j$ has compact phase support. Apply (C1)–(C17) separately to $j$ and $e_\epsilon$, keeping real coefficients:
\[
 \begin{aligned}
 j&=j_0(z)+j_1(z)s+p\mu_j(z,s),\\
 e_\epsilon&=e_0(z)+e_1(z)s+p\mu_e(z,s).
 \end{aligned}
 \tag{T28}
\]
The coefficient extensions have compact tangential phase support. Their negative-$R$ collars may be chosen inside a fixed product chart where $\partial_xa_0<0$, as in Section 6. We will make a particular, simpler choice for $e_0,e_1$ in Section 10.

Write the Hamilton derivative of the normal polynomial as
\[
 \begin{aligned}
 F&=H_p(\alpha+\beta s)=F_0+F_1s+F_2s^2,\\
 F_0&=\{a_0,\alpha\}_{\rm tan}-\beta\partial_xa_0,\\
 F_1&=2\partial_x\alpha+\{a_0,\beta\}_{\rm tan},\qquad
 F_2=2\partial_x\beta,\\
 \lambda&=F_2-j_1^2,\\
 D_0&=F_0-j_0^2-e_0-\lambda a_0,\\
 D_1&=F_1-2j_0j_1-e_1.
 \end{aligned}
 \tag{T29}
\]
At the two real characteristic roots, (T15) and (T28) give
$F=(j_0+j_1s)^2+e_0+e_1s$.
Subtracting the multiple $\lambda p$ cancels the quadratic coefficient. For $R>0$, evaluating the remaining polynomial $D_0+D_1s$ at $s=\pm\sqrt R$ proves $D_0=D_1=0$. By smoothness the same holds at $R=0$. Because $t=a_0=-R$ is a coordinate, every derivative of $D_0,D_1$ is flat at $t=0$: it vanishes on $t<0$, and Taylor's formula bounds it on $t>0$ by $C_Mt^M$ for every $M$. All such bounds are uniform on the retained compact parameter set. We must account for these possibly nonzero elliptic residuals; a real-root identity alone would not do so.

There is a smooth, nonnegative, compactly supported function $k(z)$, zero for $t\le0$ and flat at zero, such that on $t>0$
\[
 k\ge \frac{2|D_0|}{t}+\frac{|D_1|}{\sqrt t}.
 \tag{T30}
\]
Here is a construction with every smoothness issue retained. Use coordinates $(t,w)$ and make the negative-$R$ coefficient extensions small enough that the residuals are supported in $0<t<T/2$, inside a product chart containing $0\le t\le2T$. Choose a nonnegative parameter cutoff $\omega(w)$ equal to one on their projected support and compactly supported in that chart. Let $\psi\ge0$ be smooth, supported in $(1/4,2)$ and at least one on $[1/2,1]$. For $t_m=T2^{-m}$, $m\ge0$, let $A_m$ be the supremum of the right side of (T30) over $t\in[t_m/4,2t_m]$ and all parameters, extending the residuals by zero outside their compact parameter support. Set $a_m=A_m+2^{-m^2}$ and put
\[
 \begin{aligned}
 k(t,w)&=\omega(w)\sum_{m\ge0}a_m\psi(t/t_m)
                         &&(t>0),\\
 k(t,w)&=0 &&(t\le0).
 \end{aligned}
 \tag{T31}
\]
At each positive $t$ only a bounded number of summands is nonzero. On the residual support, some $t/t_m$ lies in $[1/2,1]$, so this sum dominates (T30); off that support the right side is zero. Flatness gives $A_m=O(2^{-mM})$ for every $M$. A derivative of order $l$ in $t$ costs at most $C_l2^{ml}$. Consequently all derivatives of the sum tend to zero faster than every power of $t$, uniformly in $w$. Repeated use of the fundamental theorem across zero verifies its smooth extension with zero jets. The support stays in $t<2T$ and the compact support of $\omega$. These choices concern a fixed phase neighborhood; no constant is asserted uniform as $\epsilon$ tends to zero.

Set $\ell=\lambda-k$ and
\[
 \begin{gathered}
 N(z)=\begin{pmatrix}
       D_0+ka_0&D_1/2\\ D_1/2&k
       \end{pmatrix},\qquad N\ge0,\\
 \begin{aligned}
 F={}&(j_0+j_1s)^2+(e_0+e_1s)\\
     &+\ell p+(1,s)N(1,s)^{\mathsf T}.
 \end{aligned}
 \end{gathered}
 \tag{T32}
\]
Both assertions are global on the retained coefficient patch. For $t\le0$, $N=0$. For $t>0$, (T30) gives $D_0+kt\ge kt/2$ and $|D_1|\le k\sqrt t$. If $k>0$, completing the square in the second component of a complex vector leaves the coefficient
$D_0+kt-D_1^2/(4k)\ge kt/4\ge0$ in the first component. If $k=0$, both residuals vanish and the matrix is zero. This proves positivity without taking a potentially nonsmooth matrix square root. Expanding the right side of (T32) gives (T29) exactly. All coefficients in (T32) and each fixed normal derivative are smooth, compactly supported and bounded.

## 9. Quantizing the positive form and the equation multiple

For a real tangential coefficient $b$ denote its self-adjoint quantization by
$b_h^s=(\operatorname{Op}_h(b)+\operatorname{Op}_h(b)^*)/2$.
For a real normal polynomial $v=v_0+v_1s+v_2s^2$ define
\[
 \begin{aligned}
 \mathcal Q_h(v;u)={}&((v_0)_h^su,u)
       +\operatorname{Re}((v_1)_h^sd_xu,u)\\
       &+((v_2)_h^sd_xu,d_xu),\\
 H_h(u)^2={}&\|u\|^2+\|d_xu\|^2,\\
 J_hu={}&\operatorname{Op}_h(j_0)u
                       +\operatorname{Op}_h(j_1)d_xu.
 \end{aligned}
 \tag{T33}
\]
Inner products here include integration in the normal variable. For smooth Dirichlet inputs with compact normal support, the finite tangential products give
\[
 \begin{aligned}
 &\mathcal Q_h((j_0+j_1s)^2;u)\\
 &\qquad=\|J_hu\|^2+O(h)H_h(u)^2,\\
 &\mathcal Q_h((1,s)N(1,s)^{\mathsf T};u)\\
 &\qquad\ge-ChH_h(u)^2.
 \end{aligned}
 \tag{T34}
\]
For the first line, expand the square norm. Each product of two tangential factors differs in norm by $O(h)$ from the self-adjoint quantization of its real principal product. The mixed term is bounded by $Ch\|u\|\|d_xu\|$.

For the second line, apply the proved Gaussian-packet construction to the two-component function $(u,d_xu)$ at each fixed $x$. The analysis map acts on both components. Multiplication by the positive matrix $N(y,h\xi)$ has nonnegative quadratic form pointwise, so its packet quantization is nonnegative. The kernel calculation, Gaussian second-moment estimate and left-to-Weyl correction in [the Gaussian reading, Lemmas 2–3 and Theorem 4](weighted-positivity.md#high-frequency-norm), are linear in each entry. They show that each entry differs from its self-adjoint tangential quantization by norm at most $Ch$. There are only four entries. Their errors have total form bounded by $Ch(\|u\|^2+\|d_xu\|^2)$. The constants are uniform in the compact normal interval, and integration proves the second line. This proves the matrix version actually needed here directly from the scalar kernel estimates.

For every real compact coefficient $v(z)$, let $V_h=v_h^s$. If $P_hu=f$, integration once in $x$ gives
\[
 \begin{aligned}
 (V_hd_xu,d_xu)
   &={}\operatorname{Re}(V_hd_x^2u,u)\\
   &\quad+\operatorname{Re}(-ihV_h'd_xu,u),\\
 \mathcal Q_h(vp;u)
   &={}\operatorname{Re}(V_hf,u)\\
   &\quad+O(h)H_h(u)^2.
 \end{aligned}
 \tag{T35}
\]
The first line has no boundary term because $u(0)=0$ and the input vanishes near the outer endpoint. In the second line substitute $d_x^2u=f-R_hu$. The finite differential-cutoff calculation shows that the real form of $V_hR_h$ differs from $(va_0)_h^s$ by norm $O(h)$, including the full lower symbol $ha_1$. The last term in the first line is bounded by $Ch\|d_xu\|\|u\|$. This establishes the second line with the actual equation and lower terms present.

Let $\mathcal C_h(u)=(i[P_h,A_h]u/h,u)$ and $\mathcal E_h(u)=\mathcal Q_h(e_0+e_1s;u)$. The exact formula (C27), and the principal coefficients checked in (L3)–(L6), give
\[
 \begin{aligned}
 \mathcal C_h(u)
   ={}&\mathcal Q_h(F-\beta_xp;u)\\
      &+\operatorname{Re}(B_h'f,u)\\
      &+O(h)H_h(u)^2,\\
 V_h={}&(\ell-\beta_x)_h^s,\\
 \Lambda_h={}&V_h+B_h',\\
 \mathcal C_h(u)
   \ge{}&\|J_hu\|^2+\mathcal E_h(u)\\
      &+\operatorname{Re}(\Lambda_hf,u)\\
      &-ChH_h(u)^2.
 \end{aligned}
 \tag{T36}
\]
Indeed the three coefficients of $F-\beta_xp$ are $F_0-a_0\beta_x,F_1,\beta_x$, exactly the reduced bulk coefficients in (L3)–(L5). Insert (T32), apply (T34), and apply (T35) with $v=\ell-\beta_x$. This proves the last line. In particular the $B_h'f$ term has not been discarded. The family $\Lambda_h$ is uniformly bounded on tangential $L^2$, by the finite norm bounds already proved.

## 10. Recovering the actual interior edge operator

It remains to relate $\mathcal E_h$ to the full-phase edge whose regularity was proved in (T16). A linear normal polynomial obtained by division need not itself be supported on the incoming branch. The equation is needed for this step too.

In the present construction, $e_\epsilon$ vanishes for $|s|<\sigma$ and is supported where $x>\sigma^2/(2K)$, by (T8)–(T9). Its real-root average and divided difference therefore vanish for $0\le R<\sigma^2$. Choose $e_0=e_1=0$ for $R<0$. This is a smooth extension agreeing with every jet at zero. For $R>0$, use the exact real-root formulas. Their supports are compact and separated from the wall, since every nonzero endpoint value has that property. Define $\mu_e$ by (T28), with the smooth values at the real roots supplied by the division proof. Its output-position and tangential-frequency support is also compact and separated from the wall. Outside the projection of the support of $e_\epsilon$, all three numerator terms vanish, hence so does $\mu_e$.

For large $|s|$ the full-phase edge is zero, and
$\mu_e=-(e_0+e_1s)/(s^2+a_0)$.
Differentiating this rational expression, and using smoothness on the remaining compact region, gives for all fixed multi-indices
\[
 |\partial_z^\gamma\partial_s^l\mu_e(z,s)|
       \le C_{\gamma l}\langle s\rangle^{-1-l}.
 \tag{T37}
\]
In particular it is a bounded-derivative symbol in all full position and frequency variables. No isotropic order-minus-one assertion in $(s,\eta)$ is required. [The finite-derivative bound](finite-derivative-l2.md#finite-derivative-l2) and the bounded-amplitude lemma apply: replacing the ordinary frequency by $h$ times that frequency multiplies its derivatives by powers of $h\le1$ and keeps all needed seminorms uniformly bounded.

Write $\operatorname{Op}^{\rm full}_h$ for left quantization in $(x,y)$ and $(s,\eta)$. Choose a smooth normal cutoff $\theta=1$ near the normal projection of these supports, zero near both endpoints of the collar. Extend $\theta u$ by zero to the full normal line, and extend the smooth differential coefficients to have bounded derivatives on that line. For $w=\theta u$, the finite calculation gives
\[
 \begin{aligned}
 \operatorname{Op}^{\rm full}_h(\mu_e)P_hw
      &=\operatorname{Op}^{\rm full}_h(\mu_ep)w+hZ_hw,\\
 \sup_{0<h\le h_0}\|Z_h\|_{L^2\to L^2}&<\infty.
 \end{aligned}
 \tag{T38}
\]
Here are the required bounds for this calculation despite the unbounded normal frequency. The normal term is exact: right composition with $d_x^2$ multiplies the left symbol by $s^2$. For the tangential differential terms, move the finitely many input derivatives onto the kernel. The leading amplitude is $\mu_e(X,\Xi)a_0(Y,\eta)$, with full positions $X,Y$ and frequency $\Xi=(s,\eta)$. Taylor's formula for each coefficient between $X$ and $Y$ replaces its difference from the value at $X$ by a position difference times an integral of a first derivative. Move that position difference onto the exponential as $h$ times a frequency derivative, and integrate by parts. The resulting amplitudes and all required derivatives are bounded: the tangential frequency is compact, (T37) bounds the normal frequency and its derivatives, and the extended differential coefficients have bounded derivatives. Terms already containing $h$, including $ha_1$, obey the same bounds. The bounded-amplitude lemma therefore proves (T38). One can first cut off $s$ at radius $L$. The bounded symbol $\mu_e$ and its needed derivatives converge in supremum norm as $L\to\infty$; the differentiated remainder amplitudes have the same property. The normal product converges on $H^2$ inputs by writing it as the bounded operator on $d_x^2w$. Thus the calculation has a well-defined limit on that domain.

We also need separated normal supports, not an assumption that quantization is local in $x$. If an input multiplier is supported at positive normal distance from the output support of $\mu_e$, integrate its kernel $N$ times by parts in $s$. After at least one such derivative, (T37) is integrable in $s$. Additional tangential integrations by parts give an integrable factor $(1+|y-y'|/h)^{-d-2}$. The kernel is bounded by a constant times
$h^{N-d-1}|x-x'|^{-N}(1+|y-y'|/h)^{-d-2}$,
where $d$ is the number of tangential variables. For $N>1$, the positive normal separation and compact output support give finite row and column integrals, bounded by $C_Nh^{N-1}$. The earlier Schur estimate proves norm $O(h^M)$ for any prescribed $M$, by taking $N$ sufficiently large. The same proof applies to the compact full-phase symbol $e_\epsilon$.

Let $u^0,f^0$ denote zero extension from the collar, only as $L^2$ functions, and put
$M_hf=\operatorname{Op}^{\rm full}_h(\mu_e)(\theta f)^0$.
This family is uniformly bounded. Use
$P_h(\theta u)=\theta f-2ih\theta'd_xu-h^2\theta''u$.
The last two terms are at separated normal supports, so the preceding estimates make their images under $\operatorname{Op}^{\rm full}_h(\mu_e)$ arbitrarily small powers of $h$ times $H_h(u)$. Equation (T28), (T38), and the same separated-support bound for $e_\epsilon$ give
\[
 \begin{aligned}
 &\mathcal E_h(u)\\
 &\quad=\operatorname{Re}\bigl(
        \operatorname{Op}^{\rm full}_h(e_\epsilon)u^0,u^0\bigr)\\
 &\qquad-\operatorname{Re}(M_hf,u^0)+O(h)H_h(u)^2.
 \end{aligned}
 \tag{T39}
\]
To check the left side, full left quantization of $e_0+e_1s$ is exactly
$\operatorname{Op}_h(e_0)+\operatorname{Op}_h(e_1)d_x$.
Its action on $\theta u$ equals its action on $u$, since $\theta=1$ near the coefficient support. Its real quadratic form differs from $\mathcal E_h(u)$ by $O(h)\|d_xu\|\|u\|$: only the replacement of the left $e_1$ factor by its self-adjoint quantization is involved, and the tangential adjoint formula bounds that difference by $O(h)$. The constant term already has the same real form. This proves (T39). No differential equation for the zero extension at the boundary has been used; the equation was applied only to the interior function $\theta u$.

## 11. The whole-neighborhood estimate and its remaining use

Combine (T26), (T36), and (T39). For $P_hu=f$, Cauchy–Schwarz, the uniform bounds on $\Lambda_h,M_h$ and $A_h$, and $h\le1$ give
\[
 \begin{aligned}
 &\|J_hu\|^2+\|S_h(0)d_xu(0)\|^2\\
 &\quad\le C h^{-1}\|f\|H_h(u)\\
 &\qquad\quad+ChH_h(u)^2\\
 &\qquad\quad+
       \|\operatorname{Op}^{\rm full}_h(e_\epsilon)u^0\|\,\|u\|.
 \end{aligned}
 \tag{T40}
\]
This holds for the full phase cutoff, in either orientation, with constants independent of sufficiently small $h$. It first holds for smooth Dirichlet inputs with compact normal support. The $H^2$ Dirichlet approximation and normal-trace proof after (C28) extends it to that domain: every bulk factor is bounded on $u,d_xu,f$, and the normal traces converge. All norm estimates in Sections 8–10 are uniform in that approximation.

The positive square is nontrivial at the glancing point: $j_0(z_*)=j(z_*,0)=\sqrt{c(z_*)}\sqrt{-\chi'(-\epsilon)}>0$. The boundary square is the exact one from Section 7. If the input has the fixed-distribution microlocal regularity on the prescribed interior neighborhood assumed in Section 4, its full-phase edge factor in (T40) has the rapid bound (T16). Section 10 proves why that bound applies to the divided edge after the equation contribution is retained. It is not substituted for the different, larger inner-cutoff edge in (L20)–(L23).

The error $hH_h(u)^2$ in (T40) is explicitly unlocalized. The following sections refine the elliptic majorant in (T31) so that its support and the errors from the elliptic completion are controlled by the shifted divided weight. They retain every real-root coefficient and the bulk estimate already proved. Sections 14–18 provide the selective estimate for the other lower terms and the main forcing, then recover the full local energy from two multipliers. Sections 19–21 control the forcing created by spatial localization of the fixed spectral wave reduction and prove a conditional semiclassical half-step gain. Sections 22–26 construct a tangential Sobolev-regularized Dirichlet family, prove its exact first-order commutator and uniform norm bounds, and verify its cutoff-forcing and incoming-edge estimates. Sections 27–31 control all three regularizer commutator energy pairings with uniform lower-norm remainders. Sections 32–35 recover the full local energy uniformly in the regularizer and prove a half-order Sobolev gain from the explicit larger-weight hypothesis. Section 36 gives the fixed-neighborhood induction criterion. Sections 37–40 prove the tangentially elliptic boundary input by positive normal energy and a full-order Sobolev induction on one fixed open set. Sections 41–47 prove local reflection at separated normal roots and interior propagation for the actual wave, including exact mode coupling, transported cutoffs and fixed-neighborhood regularity. Sections 48–50 prove a two-root reachable region, continuity through tangency, the regularity of its incoming and transversely reflected legs, and containment of the entire larger diffraction weights. Sections 51–54 prove finite-order outgoing transport, simultaneous induction on the fixed two-root region, and normal smoothness from the actual equation. This establishes strict-diffraction regularity for the fixed H² Dirichlet wave. Sections 55–62 prove a local cone-regularity estimate at arbitrary glancing contacts, using nested phase tubes, the actual Sobolev regularizer and a two-component energy recovery. Sections 63–70 construct a curve in the closed compressed singular set and prove that it satisfies the exact inward-reaction relation (G1)–(G23), including all glancing orders and accumulating reflections. This proves the singular-curve theorem for the actual H² wave on homogeneous time intervals. Sections 71–75 prove the Cauchy-data endpoint argument, including smoothness near the initial wall from compatible collar data, and transfer propagation to every compact interior distributional datum in the spectral Dirichlet realization. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. 

<a id="shifted-elliptic-support"></a>

## 12. Keeping the elliptic correction inside the shifted weight

The majorant in (T31) can be chosen with more than compact support. We now choose all extensions into the elliptic side together, so that this majorant is supported where the shifted divided weight is strictly positive. Fix the already chosen $\epsilon$; constants below may depend on it. A subscript $2\epsilon$ denotes the construction with that shift, with the same orientation $\nu$.

Use the full neighborhood across the wall from Section 1. Since $\partial_xa_0\ne0$, the coordinate inverse proof gives coordinates $(t,w)$ with $t=a_0$ and $z=z(t,w)$. The real-root side is $t\le0$. Define
\[
 \begin{aligned}
 K_0&=\{w:\phi_\nu(z(0,w),0)\le\epsilon\},\\
 b_*&=\min_{w\in K_2}\beta_{2\epsilon}(z(0,w))>0,
 \end{aligned}
 \tag{T41}
\]
where the compact sets $K_1,K_2$ are chosen with $K_0\subset\operatorname{int}K_1\subset K_1\subset\operatorname{int}K_2$ and $K_2$ contained in $\phi_\nu(z(0,w),0)<3\epsilon/2$. These sets lie strictly inside the fixed coordinate patch. Indeed, $\phi_\nu(z,0)=|I(z,0)|^2/\delta^2$, and $I$ is a coordinate on the section $s=0$; its small sublevel set is compact inside that patch. Choose the cutoffs by the earlier smooth cutoff construction. The positive minimum in (T41) exists: at $t=0$ the shifted coefficient is $\nu\partial_s\phi_\nu\chi'(\phi_\nu-2\epsilon)$, the cutoffs are one, and both factors have the strict signs and uniform bounds proved in Sections 3 and 5.

First fix any smooth square-root extension for the shifted weight as in Section 6. Continuity on the compact $K_2$ gives a $T>0$ such that $\beta_{2\epsilon}(z(t,w))\ge b_*/2$ on $0\le t\le2T$, $w\in K_2$. Decrease $T$ to keep this product inside the chart. These choices precede the smaller weight's extensions.

On $t\le0$, retain exactly the real-root coefficients $\alpha,\beta,j_0,j_1$ already constructed, and retain the nonnegative square root $s_\epsilon=\sqrt\beta$. Every one-sided $t$ jet of $\alpha,s_\epsilon,j_0,j_1$ at zero is supported in $K_0$. To check this support, if $\phi_\nu(z(0,w),0)>\epsilon$, the full symbols $q_\nu$ and $j$ vanish for all sufficiently small $t,s,w-w_0$. Their real-root coefficients therefore vanish for small $t\le0$. Their jets are zero there. The smooth square root has the same property by (T22). Derivatives at the boundary of this support are zero by continuity. This reasoning includes the variation of $z(t,w)$, rather than treating its normal variable as fixed during differentiation.

Apply the explicit jet summation (C4)–(C5), with $-t$ in place of $R$, separately to $\alpha,s_\epsilon,j_0,j_1$. Choose every summation radius inside $0<t<T/2$, and multiply by a parameter cutoff equal to one near $K_0$ and supported in $\operatorname{int}K_1$. The jets are unchanged; hence gluing to the retained real-root side is smooth. Put $\beta=s_\epsilon^2$ on the extended side. Keep $e_0=e_1=0$ there as in Section 10. All these extended coefficients and their derivatives then vanish outside $0\le t<T/2$, $w\in K_1$. Every division identity remains exact after adjusting its remainder: the change of the affine coefficients is flat at $t=0$, and division of $\Delta_0+s\Delta_1$ by $s^2+t$ is smooth by the arbitrary-order denominator estimate in (C16) and (T23). The original symbols $q_\nu,j,e_\epsilon$, and every real-root coefficient, are unchanged.

Recompute $F,\lambda,D_0,D_1$ from (T29). The residuals are still flat at $t=0$, vanish for $t\le0$, and now have parameter support in $K_1$ and positive-$t$ support in $t<T/2$. In (T31) choose $\omega=1$ near $K_1$, supported in $\operatorname{int}K_2$, and keep the same $t_m=T2^{-m}$ and $\psi$. The proof of (T30)–(T32) applies without alteration. It now also proves
\[
 \begin{gathered}
 \operatorname{supp}k\ \cup\ \bigcup_{i,j}\operatorname{supp}N_{ij}
       \ \subset\ K_{\rm ell},\\
 K_{\rm ell}=\{z(t,w):0\le t\le2T,\ w\in K_2\},\\
 \beta_{2\epsilon}\ge b_*/2\quad\hbox{on }K_{\rm ell}.
 \end{gathered}
 \tag{T42}
\]
All normal and tangential derivatives have the same support containment. Although $k=0$ at $t=0$, its closed support can meet that set; (T42) deliberately includes it. Its dyadic summands need not be positive everywhere else in the chart. The parameter cutoff confines even the added $2^{-m^2}$ part to the region just proved admissible. Thus that small strictly positive tail introduces no unexamined support.

## 13. Localizing the operator error of that correction

Write $\mathsf S_h=\operatorname{Op}_h(s_{2\epsilon})$, where $s_{2\epsilon}^2=\beta_{2\epsilon}$, and set
\[
 \mathcal H_{2\epsilon,h}(u)^2
       =\|\mathsf S_hu\|^2+\|\mathsf S_hd_xu\|^2.
 \tag{T43}
\]
This is an interior tangentially weighted norm; it is distinct from the boundary trace in (T26) and from the bulk square $J_h$. We first prove the localized factorization needed to use it.

Choose real compact tangential phase cutoffs $q_0,q_1$ with $q_0=1$ near $K_{\rm ell}$, $q_1=1$ near $\operatorname{supp}q_0$, and both supported where $|s_{2\epsilon}|$ is bounded below. They may depend smoothly on $x$. Such cutoffs exist by (T42), compactness and continuity in the full extended chart. For a smooth symbol $a$ supported in this region, with its support a compact subset of $\{s_{2\epsilon}\ne0\}$, division by $s_{2\epsilon}$ is smooth there. Extend $a/s_{2\epsilon}$ by zero after an intermediate cutoff. The finite product formula (N20) gives $\operatorname{Op}_h(a/s_{2\epsilon})\mathsf S_h=\operatorname{Op}_h(a)+h\operatorname{Op}_h(r_1)+O(h^2)$, with $r_1$ supported in that same nonvanishing region. Cancel this coefficient by adding $-h\operatorname{Op}_h(r_1/s_{2\epsilon})$. Repeat for any fixed number of orders. Each new coefficient is a finite sum of derivatives of the earlier coefficients and $s_{2\epsilon}$, so it retains compact support inside that region. The remainder bounds in (N20) and the finite-derivative norm bound justify every cancellation, uniformly in $x$ and after any fixed number of normal derivatives. This proves, for any integer $M$, a uniformly bounded family $C_{a,h,M}$ such that
\[
 \begin{aligned}
 \operatorname{Op}_h(a)&=C_h\mathsf S_h+h^ME_h,\\
 \sup_h\bigl(\|C_h\|+\|E_h\|\bigr)&<\infty.
 \end{aligned}
 \tag{T44}
\]
Here the dependence of $C_h,E_h$ on $a,M$ is suppressed. The same proof applies to finite symbol expansions and self-adjoint quantizations, using their proved adjoint expansions; a remainder of sufficiently high order remains in $E_h$. This is a finite construction for each $M$, not an inverse of $\mathsf S_h$ on its zero set.

Let $U=(u,d_xu)$ and let $\mathfrak N_h$ be the two-by-two matrix whose entries are the self-adjoint quantizations of $N_{ij}$. Its quadratic form is exactly $\mathcal Q_h((1,s)N(1,s)^{\mathsf T};u)$. With $Q_0=\operatorname{Op}_h(q_0)$ acting on each component, the separated-symbol estimate and the adjoint expansion give $\mathfrak N_h=Q_0^*\mathfrak N_hQ_0+O(h^L)$ for every fixed $L$. In fact every nonconstant Taylor coefficient containing a derivative of $q_0$ vanishes on the support of every derivative of $N$; the remaining remainders have the uniform bounds of (N20). The matrix packet proof of (T34), now applied to $Q_0U$, gives the lower bound $-Ch\|Q_0U\|^2$. Apply (T44) to $q_0$ component by component, integrate in $x$, and take $L$ sufficiently large. The result is
\[
 \begin{aligned}
 &\mathcal Q_h((1,s)N(1,s)^{\mathsf T};u)\\
 &\qquad\ge-Ch\mathcal H_{2\epsilon,h}(u)^2
                -C_Mh^MH_h(u)^2 .
 \end{aligned}
 \tag{T45}
\]
This argument localizes the packet error as well as the principal positive form. Positivity of a principal matrix alone would not give the displayed weighted error.

The equation multiple introduced by $k$ has the same control. Put $K_h=k_h^s$. The exact integration in (T35), with the full $R_h$ retained, writes
\[
 \begin{aligned}
 L_h={}&(ka_0)_h^s\\
      &-\tfrac12(K_hR_h+R_hK_h),\\
 &\mathcal Q_h(kp;u)-\operatorname{Re}(K_hf,u)\\
 &\quad=\operatorname{Re}(-ihK_h'd_xu,u)+(L_hu,u).
 \end{aligned}
\]
The operator $L_h$ is $O(h)$ in norm, and every coefficient of its finite expansion is supported in $K_{\rm ell}$: the leading terms cancel, and every remaining term contains $k$ or one of its derivatives. This includes the lower differential symbol $ha_1$ of $R_h$. Moving its finitely many input derivatives onto the compact-frequency kernel and Taylor-expanding as in (N23) and (L6) gives a bounded remainder of any required fixed order. The same support assertion holds for $K_h'$. Insert $Q_0^*,Q_0$ on both sides of these forms, with an arbitrarily high-order remainder, and use (T44). The mixed form is bounded by the product of the two weighted norms in (T43). Also, self-adjointness and (T44) give $|(K_hf,u)|=|(f,K_hu)|\le C\|f\|\|\mathsf S_hu\|+C_Mh^M\|f\|\|u\|$. Therefore (T45) implies
\[
 \begin{aligned}
 &\mathcal Q_h((1,s)N(1,s)^{\mathsf T}-kp;u)\\
 &\quad\ge -C\|f\|\|\mathsf S_hu\|
                  -Ch\mathcal H_{2\epsilon,h}(u)^2\\
 &\qquad\quad-C_Mh^M\bigl(H_h(u)^2+\|f\|H_h(u)\bigr).
 \end{aligned}
 \tag{T46}
\]
Here $P_hu=f$ and the same Dirichlet and compact normal-support conditions as in (T40) apply. No commutation of $Q_0$ through $d_x$ is used: it acts on the two components after the exact normal integration. This avoids adding an unstated normal-cutoff commutator. The established $H^2$ Dirichlet approximation extends these bounds to that domain, as for (T40).

Equations (T42), (T45) and (T46) close the support and weighted-error obligations for the *elliptic completion* $N-kp$ in (T32). The following sections also control the real-root square, the other equation coefficient $\lambda-\beta_x$, the full-phase edge composition remainder and the main commutator forcing. Formula (T46) is their elliptic-completion input; Sections 19–21 treat the spatial localization forcing. Sections 22–26 construct a tangential Sobolev-regularized Dirichlet family, prove its exact first-order commutator and uniform norm bounds, and verify its cutoff-forcing and incoming-edge estimates. Sections 27–31 control all three regularizer commutator energy pairings with uniform lower-norm remainders. Sections 32–35 recover the full local energy uniformly in the regularizer and prove a half-order Sobolev gain from the explicit larger-weight hypothesis. Section 36 gives the fixed-neighborhood induction criterion. Sections 37–40 prove the tangentially elliptic boundary input by positive normal energy and a full-order Sobolev induction on one fixed open set. Sections 41–47 prove local reflection at separated normal roots and interior propagation for the actual wave, including exact mode coupling, transported cutoffs and fixed-neighborhood regularity. Sections 48–50 prove a two-root reachable region, continuity through tangency, the regularity of its incoming and transversely reflected legs, and containment of the entire larger diffraction weights. Sections 51–54 prove finite-order outgoing transport, simultaneous induction on the fixed two-root region, and normal smoothness from the actual equation. This establishes strict-diffraction regularity for the fixed H² Dirichlet wave. Sections 55–62 prove a local cone-regularity estimate at arbitrary glancing contacts, using nested phase tubes, the actual Sobolev regularizer and a two-component energy recovery. Sections 63–70 construct a curve in the closed compressed singular set and prove that it satisfies the exact inward-reaction relation (G1)–(G23), including all glancing orders and accumulating reflections. This proves the singular-curve theorem for the actual H² wave on homogeneous time intervals. Sections 71–75 prove the Cauchy-data endpoint argument, including smoothness near the initial wall from compatible collar data, and transfer propagation to every compact interior distributional datum in the spectral Dirichlet realization. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. The general curved spectral application is proved in the linked spectral reading, Sections 31–38.

<a id="shifted-whole-bulk"></a>

## 14. A larger weight controlling every divided coefficient

We now refine (T40), including its full-phase edge composition error. The smaller multiplier will retain all its real-root coefficients. The larger weight uses the same phase and shift $2\epsilon$, but a nested outer cutoff. This is a choice of auxiliary cutoffs, with no new hypothesis on the solution.

Make the permitted choice of $\vartheta$ in Section 2 more specific, and choose a second even cutoff $\vartheta_+$, with values in $[0,1]$, so that
\[
 \begin{aligned}
 &\vartheta=1\quad(|s|\le\sigma),\\
 &\vartheta=0\quad(|s|\ge3\sigma/2),\\
 &\vartheta_+=1\quad(|s|\le7\sigma/4),\\
 &\vartheta_+=0\quad(|s|\ge2\sigma),\\
 &q_+=\nu\rho(I)^2\vartheta_+(s)^2
                          \chi(\phi_\nu-2\epsilon).
 \end{aligned}
 \tag{T47}
\]
Both transition regions on the selected leg remain in the prescribed regular neighborhood $\mathcal U$. The invariant-cutoff argument (T6)–(T9) removes the side transition, and the opposite normal end contributes zero. Thus the earlier sign and smooth square-root proofs apply to the divided coefficient $\beta_+$ of $q_+$. Write its smooth square root as $s_+$. At merging roots the two outer cutoffs are identically one in a common neighborhood. Consequently $\beta_+$ has the same jets there as the earlier weight with shift $2\epsilon$. Choose the same elliptic-side extension for these square roots. The support construction of Section 12 and its positive lower bound on $K_{\rm ell}$ therefore still apply to $\beta_+$.

Let $B$ be the compact full-phase support of the smaller $q_\nu$, and let $\pi(z,s)=z$. The supports of $j$ and $e_\epsilon$ are contained in $B$. Set $K_{\rm r}=\pi(B\cap\{p=0\})$. We claim
\[
 \begin{gathered}
 \beta_+>0\quad\hbox{on }K_{\rm r},\\
 K_{\rm r}\cup K_{\rm ell}\Subset V,\qquad
 \inf_{\overline V}\beta_+>0,
 \end{gathered}
 \tag{T48}
\]
for some relatively compact open tangential phase neighborhood $V$ in the extended coordinate patch.

Here is the strictness needed for this assertion. At a point of $B\cap\{p=0\}$, one root $s$ has $\phi_\nu(z,s)\le\epsilon$ and $|s|\le3\sigma/2$. The invariant cutoff is one there by (T6), and $\vartheta_+=1$ on a neighborhood of that root. The shifted cutoff is strictly nonzero there because its argument is at most $-\epsilon$. If only the root of sign $\nu$ has nonzero shifted weight, the divided difference is strictly positive by its explicit one-root formula in Section 5. If the opposite root has nonzero shifted weight, its magnitude is less than $2\epsilon$; the root interval is then in the small normal band where the derivative of the shifted signed cutoff is nonnegative. That derivative is strictly positive near the nonzero endpoint, so its integral over the root interval is positive. At a double root its value is the strictly positive derivative itself. This proves the first line, including points on the closed cutoff support, where the smaller weight may be zero. Compactness of $K_{\rm r}$, (T42), and continuity give the second line after choosing and shrinking $V$.

Every smaller divided coefficient $\alpha,s_\epsilon,j_0,j_1,e_0,e_1$, and every derivative of it, is supported in $K_{\rm r}\cup K_{\rm ell}$. On the real-root side this follows from the endpoint formulas: outside $K_{\rm r}$ both roots have neighborhoods disjoint from $B$, so the coefficients vanish in a neighborhood. The root maps are continuous also as they merge; smooth division then treats their derivatives. On the elliptic side the assertion is the extension construction of Section 12. The same support statement follows for $F_i,\lambda,D_i,k,N$ and $\beta_x$ by their explicit formulas. A real smooth cutoff $v=1$ near this common compact support can therefore be chosen with support compactly contained in $V$. Formula (T44), with $s_+$, applies to $v$ and to every finite symbol coefficient just listed. Denote
$\mathsf S_{+,h}=\operatorname{Op}_h(s_+)$ and
$\mathcal H_{+,h}(u)^2=\|\mathsf S_{+,h}u\|^2+\|\mathsf S_{+,h}d_xu\|^2$.

## 15. Localizing the full-phase edge without adding a Hamilton error

Projection of $B$ itself need not lie in $V$. Its characteristic part does, and this is enough. The compact set $B\setminus\pi^{-1}(V)$ is disjoint from $\{p=0\}$. If it is nonempty, $|p|$ has a positive minimum there. Choose a real nonnegative smooth scalar $\gamma$, equal to one near zero and supported in a smaller interval than that minimum. If the set is empty, choose any sufficiently small compact interval around zero. Put
\[
 \begin{aligned}
 \widetilde q&=\gamma(p)^2q_\nu,\qquad
 \widetilde j=\gamma(p)j,\\
 \widetilde e&=\gamma(p)^2e_\epsilon,\\
 H_p\widetilde q&=\widetilde j^{\,2}+\widetilde e.
 \end{aligned}
 \tag{T49}
\]
Indeed $H_pp=0$, so differentiating $\gamma(p)$ contributes exactly zero. Choose its support with a strict margin; the three new full-phase symbols then have compact projected support inside $V$. On $p=0$ their values are unchanged, and $\gamma(p)=1$ on a full neighborhood of that set. Thus every real-root coefficient and every jet at merging roots is unchanged. Keep their elliptic extensions unchanged too. Exact division is recovered by changing only the smooth remainders, since $(\gamma(p)^2-1)/p$ and $(\gamma(p)-1)/p$ are smooth, with value zero near $p=0$. In particular $A_h,J_h,\beta,N$ and $k$ are unchanged. The edge remains supported in $\mathcal U$ and separated from the wall.

Let $\widetilde\mu_e$ be the quotient in
$\widetilde e=e_0+e_1s+p\widetilde\mu_e$.
Its tangential phase support is now a compact subset of $V$. Outside the union of the projected support of $\widetilde e$ and the coefficient supports, its numerator is zero. Its normal output support is still separated from the wall. The large-$|s|$ expression is still $-(e_0+e_1s)/(s^2+a_0)$, so (T37) holds for this quotient with every derivative.

We need finite compositions with a tangential cutoff even for this noncompact normal-frequency tail. The following verification supplies that step. Write $X=(x,y)$, $\Xi=(s,\eta)$ and $D=1+\dim y$. For two smooth bounded-derivative full symbols $a,b$, with $b$ compactly supported in $X$ and compactly supported in $\eta$, the exact left-product calculation uses the translated Fourier transform from (N19):
\[
 \begin{gathered}
 (2\pi)^{-D}\int
 a(X,\Xi+h\Theta)\widehat b_X(\Theta,\Xi)\,d\Theta,\\
 \widehat b_X(\Theta,\Xi)
       =\int e^{-iZ\cdot\Theta}b(X+Z,\Xi)\,dZ.
 \end{gathered}
\]
This transform is $e^{iX\cdot\Theta}\widehat b(\Theta,\Xi)$, where the latter transform is in the position variable. It decreases faster than every power of $\Theta$, uniformly in $X,s,\eta$ and after any prescribed $X,\Xi$ derivatives; each derivative of the phase costs only a fixed power of $\Theta$. Compact normal-frequency support is unnecessary: compact position support and bounded derivatives give this decrease. Taylor expansion in $h\Theta$ therefore has a bounded-symbol remainder of order $h^L$ for every fixed $L$, by exactly the integral majorant in (N20). The finite-derivative bound controls its operator norm. The full adjoint expansion has the same property: Taylor-expand the transposed amplitude in its position variable; transfer each position difference to a frequency derivative; bound the integral remainder by the bounded-amplitude lemma. These identities hold first on Schwartz inputs through frequency cutoffs and then by bounded extension. No isotropic negative-order estimate for $\widetilde\mu_e$ is asserted.

Choose a real compact cutoff $v_1=1$ near the projected support of $\widetilde\mu_e$ and all the smaller coefficients, supported in $V$, and let $Q_h=\operatorname{Op}_h(v_1)$ act pointwise in $x$. For a full symbol $b$ with the just-proved bounds and projected support in the region where $v_1=1$, the product and adjoint expansions give
\[
 \begin{aligned}
 \operatorname{Op}^{\rm full}_h(b)
   &=Q_h^*\operatorname{Op}^{\rm full}_h(b)Q_h
                                   +O(h^L),\\
 \operatorname{Op}^{\rm full}_h(b)
   &=Q_h^*\operatorname{Op}^{\rm full}_h(b)+O(h^L)
 \end{aligned}
 \tag{T50}
\]
in full $L^2$ operator norm. Every nonconstant finite coefficient containing a derivative of $v_1$ vanishes near the support of the derivatives of $b$. The argument applies to $b=\widetilde\mu_e$, to $\widetilde e$, and to the finite coefficients of the equation-composition error below. For a bounded remainder without that support property we retain its already arbitrarily high power of $h$.

To check the equation-composition assertion, repeat (T38) to $L$ orders. Right composition with $d_x^2$ is exact. For each tangential differential term move input derivatives onto the kernel and Taylor-expand its coefficient to $L$ orders. The zeroth term is the principal product; the higher terms contain derivatives of $\widetilde\mu_e$. The lower symbol contributes $h\widetilde\mu_e a_1$ and its differentiated terms. They all have projected support inside $V$, compact tangential frequency support and bounded derivatives, including the normal-frequency tails. The remainder is $h^L$ times a bounded amplitude by (T37) and the finite differential order. Thus the entire order-$h$ composition error has a finite expansion whose coefficients satisfy (T50), plus a bounded $O(h^L)$ remainder.

## 16. The complete weighted bulk error

Fix any integer $M\ge1$; take the finite expansions a few orders beyond $M$ when a commutator is divided by $h$. A tangential operator with an order-$h$ finite expansion supported in $V$ has a form bounded by
$Ch\mathcal H_{+,h}(u)^2+C_Mh^MH_h(u)^2$
on the pair $(u,d_xu)$. Indeed insert a cutoff equal to one near its coefficient supports on both sides, with the finite remainders just proved, and factor that cutoff through $\mathsf S_{+,h}$ using (T44). Mixed forms are bounded by the product of the two component norms. Normal derivatives of all symbols obey the same bounds.

Apply this argument to the difference between the first form in (T34) and $\|J_hu\|^2$: its order-zero products agree, while each higher coefficient contains a smaller $j$ coefficient or its derivatives. Apply the matrix packet argument of (T45) to $N$. Apply the exact integration in (T35) to $\ell-\beta_x$, retaining the normal derivative term and the full lower symbol. Finally apply it to the finite remainders in (L6) and (T36); (C27) supplies their exact normal reduction, including $B_h'f$. Each coefficient is supported in the common compact subset of $V$ identified in Section 14. A forcing factor $T_h$ occurring here also satisfies
$\|T_h^*u\|\le C\|\mathsf S_{+,h}u\|+C_Mh^M\|u\|$
by the finite adjoint expansion and (T44). These observations establish
\[
 \begin{aligned}
 \mathcal C_h(u)\ge{}&\|J_hu\|^2+\mathcal E_h(u)\\
 &-C\|f\|\mathcal H_{+,h}(u)
       -Ch\mathcal H_{+,h}(u)^2\\
 &-C_Mh^M\bigl(H_h(u)^2+\|f\|H_h(u)\bigr).
 \end{aligned}
 \tag{T51}
\]
All the lower terms of the actual multiplier and differential operator are included. Only the final arbitrary-order remainder uses the unlocalized energy.

For the divided edge use the same interior normal cutoff $\theta$ as in Section 10. With $E_h=\operatorname{Op}^{\rm full}_h(\widetilde e)$, the proof of (T39), now using (T50) for each composition-error coefficient, gives
\[
 \begin{aligned}
 &\left|\mathcal E_h(u)
            -\operatorname{Re}(E_hu^0,u^0)\right|\\
 &\quad\le C\|f\|\mathcal H_{+,h}(u)
                    +Ch\mathcal H_{+,h}(u)^2\\
 &\qquad+C_Mh^M\bigl(H_h(u)^2+\|f\|H_h(u)\bigr).
 \end{aligned}
 \tag{T52}
\]
For precision, the forcing term here is $\operatorname{Op}^{\rm full}_h(\widetilde\mu_e)(\theta f)^0$. Its adjoint applied to $u^0$ is bounded by $C\|\mathsf S_{+,h}u\|+C_Mh^M\|u\|$, using (T50) and (T44). The full composition remainder has the localized form bound just proved. The replacement of the left $e_1$ factor by its self-adjoint quantization has an order-$h$ tangential expansion supported in $V$, so its mixed error has the same bound. The terms containing $\theta'$ and $\theta''$ retain arbitrarily high powers of $h$ by the separated-normal-support proof after (T38). The operators $Q_h$ and $\mathsf S_{+,h}$ commute with $\theta$ and with zero extension in the normal variable because they act pointwise in that variable. Hence the full-line localized norms are exactly the collar norms used in (T52), or bounded by them when $\theta$ is present. The equation is still applied only to $\theta u$, never to the zero extension across the physical boundary.

## 17. The shifted estimate with the actual incoming edge

The remaining forcing in the exact identity (T26) has the required localization too. Expand $A_h=A_{0,h}+B_hd_x-ihB_h'/2$. All three tangential factors have finite expansions supported in $V$; their normal derivatives have the same property. Formula (T44) consequently gives the first estimate below. The second uses the one-sided form of (T50) for $E_h$, followed by (T44) for $Q_h$. Its high-order cross term is bounded using the uniform $L^2$ norm of $E_h$.
\[
 \begin{aligned}
 &\|A_hu\|\\
 &\quad\le C\mathcal H_{+,h}(u)
                         +C_Mh^{M+1}H_h(u),\\
 &|(E_hu^0,u^0)|\\
 &\quad\le C\|E_hu^0\|\mathcal H_{+,h}(u)
                         +C_Mh^MH_h(u)^2.
 \end{aligned}
 \tag{T53}
\]
Combining (T26), (T51), (T52) and (T53), and using $h\le1$, proves
\[
 \begin{aligned}
 &\|J_hu\|^2+\|S_h(0)d_xu(0)\|^2\\
 &\quad\le C\bigl(h^{-1}\|f\|+\|E_hu^0\|\bigr)
                                  \mathcal H_{+,h}(u)\\
 &\qquad\quad+Ch\mathcal H_{+,h}(u)^2\\
 &\qquad\quad+C_Mh^M\bigl(H_h(u)^2+\|f\|H_h(u)\bigr),\\
 &\qquad P_hu=f,\qquad u(0)=0.
 \end{aligned}
 \tag{T54}
\]
The hypotheses are the same compact normal support and $H^2$ Dirichlet domain as in (T40); the estimate first holds for smooth inputs and extends by the same Dirichlet approximation. The choices of cutoffs, weights and extensions are fixed before $h\to0$. Constants may depend on those choices and on $M$, but not on $h$ or $u$. Both orientations are included.

The edge in (T54) is the actual full-phase symbol $\gamma(p)^2e_\epsilon$, supported in the prescribed regular interior neighborhood. It has the rapid bound (T16) for a fixed distribution microlocally smooth there. Every order-$h$ energy error and every solution factor paired with the forcing is now controlled by the larger shifted weight; the unlocalized terms have arbitrarily high powers of $h$. This is the selective estimate missing from (T40). The next section extracts the full local energy from two such positive squares. Neither step presumes that the larger weighted norm is already controlled at an improved Sobolev order, or that the forcing of a regularized solution is zero.

## 18. Two squares recover the full local energy

Keep the same orientation and the same $\sigma,\delta$, and use the smaller shifts $\epsilon_1=\epsilon$ and $\epsilon_2=\epsilon/2$, with the permitted additional choice $\epsilon<1$. Apply Sections 14–17 to each. Write $j_{0,i},j_{1,i}$ for its two divided square coefficients and $J_{i,h}$ for its positive-square operator. At the central point, $I=0$, the cutoff derivatives vanish, $\partial_s\phi_\nu=-\nu$, and $c$ is independent of $s$. Since $-\chi'(v)=e^{1/v}/v^2$ for $v<0$, differentiation gives the following values, with $m_i=j_{1,i}(z_*)/j_{0,i}(z_*)$:
\[
 \begin{aligned}
 j_{0,i}(z_*)&=\sqrt{c(z_*)}\,
          \epsilon_i^{-1}e^{-1/(2\epsilon_i)}>0,\\
 m_i
       &=\nu\left(\frac1{2\epsilon_i^2}-\frac1{\epsilon_i}\right),\\
 m_2-m_1
       &=\nu\frac{3-2\epsilon}{2\epsilon^2}\ne0.
 \end{aligned}
 \tag{T55}
\]
Here the double-root division formula identifies $j_{1,i}(z_*)$ with $\partial_sj_i(z_*,0)$. The characteristic cutoff of Section 15 is identically one near that point and changes none of these derivatives. Thus the matrix $\mathcal J$ with rows $(j_{0,1},j_{1,1})$ and $(j_{0,2},j_{1,2})$ is invertible at $z_*$ and on a smaller neighborhood. Both larger shifted weights are also nonzero there.

Choose a real compact tangential phase cutoff $q=1$ near $z_*$, supported in this common neighborhood, and put $Q_h=\operatorname{Op}_h(q)$. Its normal dependence is allowed. The entries of $q\mathcal J^{-1}$ are smooth and compactly supported, since the determinant has a positive absolute lower bound on that support. Finite matrix products give a left parametrix: start with that matrix symbol, cancel the order-$h$ coefficient by multiplying its negative by $\mathcal J^{-1}$, and repeat to any fixed order. The coefficient supports remain in the same invertible neighborhood, and (N20) bounds the finite remainder. For $U=(u,d_xu)$ this proves the next identity, where $\mathsf B_h,\mathsf R_h$ may depend on the fixed $M$:
\[
 \begin{aligned}
 &Q_hU=\mathsf B_h
             \begin{pmatrix}J_{1,h}u\\J_{2,h}u\end{pmatrix}\\
 &\qquad+h^M\mathsf R_hU,\\
 &\sup_h(\|\mathsf B_h\|+\|\mathsf R_h\|)<\infty.
 \end{aligned}
 \tag{T56}
\]
The matrix norm estimate (N18) bounds the entries together, uniformly in the normal interval. No regularity assumption on a transition region of $q$ has entered this argument.

Let $\mathcal H_{i,h}$ and $E_{i,h}$ denote the larger weighted norm and the actual edge for the $i$th construction, and set $\mathcal F_{i,h}=h^{-1}\|f\|+\|E_{i,h}u^0\|$. The exact identity $d_xQ_hu=Q_hd_xu-ihQ_h'u$ retains the only extra normal term in the local energy. The symbol $\partial_xq$ is supported where both larger weights are nonzero; (T44) bounds $\|Q_h'u\|$ by either corresponding weighted norm plus an arbitrary-order global remainder. Square (T56), integrate in $x$, and use this identity and the two copies of (T54). Since $h^2\le h$, we obtain
\[
 \begin{aligned}
 &H_h(Q_hu)^2\\
 &\quad\le C\sum_{i=1}^2\mathcal F_{i,h}
                      \mathcal H_{i,h}(u)\\
 &\qquad+Ch\sum_{i=1}^2\mathcal H_{i,h}(u)^2\\
 &\qquad+C_Mh^M\bigl(H_h(u)^2+\|f\|H_h(u)\bigr).
 \end{aligned}
 \tag{T57}
\]
This controls both the solution and its normal derivative near the strict diffractive point. The equation estimate was applied to $u$ before localizing its output by $Q_h$, so no unestimated $[P_h,Q_h]u$ is discarded. The normal commutator just displayed is included, and $Q_hu$ retains the zero Dirichlet value. As before, the $H^2$ approximation proves the same estimate on the stated domain.

Sections 19–21 below apply (T57) to the fixed spectral wave reduction and estimate its actual spatial-cutoff forcing. Sections 22–26 construct that regularized family and prove uniform operator, cutoff-forcing and edge bounds. Sections 27–35 control its commutator energy pairings, recover local energy uniformly and prove the conditional Sobolev half-step. Sections 48–54 prove the support and regularity induction on one fixed open region at strict diffraction. The rapid estimate (T16) for a fixed distribution is not automatically a bound for an arbitrary regularized family. The larger inner-cutoff transition in (L20) is still not declared regular. Hyperbolic, gliding and degenerate-contact propagation and the curved spectral remainder retain their full intended scope.

<a id="separated-cutoff-forcing"></a>

## 19. Separated position supports for the actual operator families

For a local homogeneous wave, cutting down to this coordinate patch introduces forcing even though the original equation has zero right side. We now control that forcing in the actual pairings. The coarse norm $\|f\|$ in (T54) need not be rapidly small. Its position support, however, can be separated from every multiplier coefficient.

We first prove the operator statement used for this separation. Let $b_h(X,\Xi)$ have uniformly bounded derivatives and fixed compact output-position support $K$. Normal-frequency support need not be compact. Let $m(X)$ be smooth with bounded derivatives, and suppose its support has positive distance from $K$. Then, for every integer $N\ge1$,
\[
 \|\operatorname{Op}^{\rm full}_h(b_h)m\|_{L^2\to L^2}
                   \le C_Nh^N.
 \tag{T58}
\]
Here the constants depend on finitely many symbol and cutoff derivatives and the fixed separation. In its kernel, apply
$h(X-Y)\cdot\partial_\Xi/(i|X-Y|^2)$
to the exponential and transfer the derivatives to $b_h(X,\Xi)m(Y)$. After $N$ integrations the kernel is $h^N$ times a semiclassical amplitude whose derivatives of every fixed order are bounded uniformly. To define the coefficients across $X=Y$, multiply them by a smooth cutoff that is zero near that diagonal and one on the separated support. The numerator amplitude already vanishes near the omitted diagonal, so this changes no operator. The factors involving $(X-Y)/|X-Y|^2$ and their derivatives are bounded on the retained region.

[The bounded-amplitude proof, Lemma 2](weighted-positivity.md#bounded-amplitudes), now applies in the full dimension. Indeed replacing the ordinary frequency by $\Xi=h\xi$ preserves its derivative bounds for $h\le1$. It bounds the residual amplitude operator independently of $h$. The integrations are justified first with frequency cutoffs; the same proof's cutoff pairing limit gives their identity on Schwartz inputs and then on $L^2$. This proves (T58) without an integrability assumption on the undifferentiated normal-frequency tail.

The tangential version holds uniformly in $x$. A tangential operator does not change the normal position. At pairs with the same $x$, separation of the full base positions is separation of $y,y'$. Repeat the preceding argument in $\eta$ and use the tangential bounded-amplitude bound at each $x$, then integrate. Where there are no such pairs the kernel is zero. Compactness and the fixed full base separation make the constants uniform, also after any fixed number of normal-parameter derivatives.

It follows in particular that a tangential family with a finite expansion to every required order, whose coefficient symbols all have base support in $K$, has the same small norm after multiplication by $m$. Choose its finite expansion beyond $N$; (T58) treats each coefficient and the bounded remainder retains its chosen high power of $h$. Its adjoint has the same property when the adjoint expansion has that coefficient support. This applies to $A_{0,h},B_h,B_h'$ and $\Lambda_h$ in (T25) and (T36). All their finite coefficients are made from the smaller divided coefficients and their derivatives, as verified in Sections 14–17.

## 20. The energy estimate with spatially separated forcing

Choose a compact set $K$ in the closed base coordinate patch containing the base projections of those tangential coefficients and of $\widetilde\mu_e$, for both constructions in Section 18. Suppose $P_hu=f$, $u(0)=0$, with the same $H^2$ domain and compact normal support as before, and suppose $f=mf$ for a cutoff $m$ whose support is separated from $K$. The full symbol $\widetilde\mu_e$ satisfies (T58) by (T37). Multiplication by the interior normal cutoff $\theta$ does not enlarge the support of $f$. Therefore
\[
 \begin{aligned}
 &\|A_{0,h}f\|+\|B_hf\|+\|B_h'f\|\\
 &\quad+\|\Lambda_hf\|
       +\|\operatorname{Op}^{\rm full}_h(\widetilde\mu_e)
                                      (\theta f)^0\|\\
 &\qquad\le C_Nh^N\|f\|.
 \end{aligned}
 \tag{T59}
\]
The tangential factors here are self-adjoint. Using
$A_h=A_{0,h}+B_hd_x-ihB_h'/2$,
move only these tangential factors across the inner product. Formula (T59) bounds $|(f,A_hu)|$ by $C_Nh^N\|f\|H_h(u)$. No normal derivative is moved onto $f$, and no boundary condition on $f$ is required. Taking one additional order absorbs the $h^{-1}$ in the exact identity (T26).

The forcing in the bulk identity (T36) is exactly $(\Lambda_hf,u)$; its lower-order product terms are included in $\Lambda_h$, not discarded. Formula (T59) treats this term and the interior forcing term in (T39). The weighted energy errors already proved in Sections 16–17 remain unchanged. Thus the same argument as for (T54), before replacing these actual pairings by a coarse norm, gives
\[
 \begin{aligned}
 &\|J_hu\|^2+\|S_h(0)d_xu(0)\|^2\\
 &\quad\le C\|E_hu^0\|\mathcal H_{+,h}(u)
                  +Ch\mathcal H_{+,h}(u)^2\\
 &\qquad+C_Nh^N
                  \bigl(H_h(u)^2+\|f\|H_h(u)\bigr).
 \end{aligned}
 \tag{T60}
\]
This holds for every fixed $N$, with the separated supports fixed in advance. The $H^2$ Dirichlet approximation passes through every term, including $f=P_hu$, as in (C28). Pass the earlier exact bounded pairings to the limit first, then apply (T59) to the limiting $f$. No support claim about an arbitrary approximating forcing is needed.

Apply (T60) for both shifts and use the finite matrix parametrix and its retained normal commutator from Section 18. Put
$\mathcal R_N=C_Nh^N(H_h(u)^2+\|f\|H_h(u))$.
The result is
\[
 \begin{aligned}
 &H_h(Q_hu)^2\\
 &\quad\le C\sum_{i=1}^2
              \|E_{i,h}u^0\|\mathcal H_{i,h}(u)\\
 &\qquad+Ch\sum_{i=1}^2\mathcal H_{i,h}(u)^2
              +\mathcal R_N.
 \end{aligned}
 \tag{T61}
\]
The hypothesis is separation of the actual forcing from $K$. It is not a claim that every phase-cutoff or Sobolev-regularization commutator has such support.

## 21. Application to the existing spectral wave reduction

Let $v$ be a fixed $H^2$ Dirichlet solution of the homogeneous wave equation on a neighborhood of this base patch. For the original fixed differential wave operator and its gauge (D1)–(D4), write $P_h=h^2L$, with $L$ independent of $h$. The gauge and change to half-density coefficients are smooth multiplications and preserve this local regularity and the zero boundary value.

Enlarge $K$ to include the base supports of the larger weights and of $Q_h$. Choose a real smooth position cutoff $\chi$, compactly supported inside the coordinate patch before the outer normal endpoint and equal to one on a neighborhood of $K$. This is a cutoff in the closed half patch; it may equal one at $x=0$. Its transition has positive distance from $K$. Put $u=\chi v$. Then
\[
 \begin{aligned}
 u(0)&=0,\qquad f=P_hu=h^2[L,\chi]v,\\
 \operatorname{supp}f&\subset\operatorname{supp}d\chi,\\
 \|f\|&\le C_\chi h^2\|v\|_{H^1(O)},\\
 H_h(u)&\le C_\chi\|v\|_{H^1(O)}.
 \end{aligned}
 \tag{T62}
\]
Here $O$ is a fixed slightly larger half patch containing the cutoff support, with the norms finite there. The product rule proves the commutator statement: in each differential monomial of order at most two, at least one derivative falls on $\chi$, leaving at most one derivative of $v$. The normal part is exactly
$-2ih\chi_xd_xv-h^2\chi_{xx}v$;
the tangential part has the analogous product terms. Derivatives of $\chi$ of higher order are supported in the closed support of its first derivative. This proves both the support assertion and the stated norm bound, with all lower-order coefficients retained. The final energy bound follows by differentiating $\chi v$ once. Smooth cutoffs provide $m=1$ near $\operatorname{supp}d\chi$ and zero on a neighborhood of $K$, as required for (T59).

Assume that $v$ is microlocally smooth on the prescribed incoming interior neighborhood $\mathcal U$ containing both full-phase edge supports. Multiplication by $\chi$ preserves that property. Formula (T16) gives $\|E_{i,h}u^0\|=O(h^N)$ for every $N$; the edges have compact interior output support, so zero extension across the wall introduces only the separated-position contribution already estimated. The larger tangential weights are uniformly bounded, hence $\mathcal H_{i,h}(u)\le C H_h(u)$. Substituting (T62) into (T61) gives, for every $N$,
\[
 \begin{aligned}
 &H_h(Q_h(\chi v))^2\\
 &\quad\le Ch\sum_{i=1}^2\mathcal H_{i,h}(\chi v)^2
                   +C_{N,v}h^N.
 \end{aligned}
 \tag{T63}
\]
The constants $C_{N,v}$ may use the fixed wave's microlocal smoothness seminorms on the incoming region. They are not asserted uniform for a family known only to be bounded in $H^2$. Changing $\chi$ to another cutoff equal to one near these base supports changes the localized output by arbitrarily high powers of $h$ in $H_h$: apply (T58) to the cutoff difference and to its differentiated product with $v$, using $d_xQ_h=Q_hd_x-ihQ_h'$. Both $q$ and $\partial_xq$ have the same separated base support. Thus the conclusion depends only on the local wave.

For a spectral wave with compactly supported interior negative-order initial data, (W9)–(W11) produce precisely such a fixed $H^2$ wave after applying a sufficiently high inverse power of the original Dirichlet operator. Its wave equation and boundary condition are unchanged. The time and space regularity in (W11) implies local spacetime $H^2$ on finite coordinate patches, including mixed derivatives. Equations (W21)–(W22) preserve its interior wavefront set, so the incoming regularity assumption transfers too. Thus (T62) controls the actual patch-localization forcing of that reduction; no additional smoothing family is needed merely to justify the energy identity.

As one finite consequence, if both larger weighted norms in (T63) are $O(h^r)$ for a real $r$, choose $N>2r+1$ to obtain
\[
 H_h(Q_h(\chi v))=O(h^{r+1/2}).
 \tag{T64}
\]
This is a conditional semiclassical norm gain. Sections 22–35 control the regularizer and its commutator energy pairings; Sections 48–54 supply the complete larger-weight induction and smoothness on one fixed strict-diffraction neighborhood. In particular, estimates on successively shrinking neighborhoods alone are not asserted to prove absence from the smooth wavefront set. Sections 41–47 below supply local separated-root reflection and interior propagation. Sections 48–50 supply the geometric connections and larger-weight support region. Sections 51–54 prove finite-order transport and the strict-diffraction induction. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38.

<a id="uniform-sobolev-commutator"></a>

## 22. A tangential regularizer with uniform symbol bounds

Fix the geometric shift $\epsilon$ and all the preceding cutoffs. A separate parameter $0<\varepsilon\le1$ will tend to zero. For a real Sobolev order $r$, choose an integer $m_0\ge1$ with $2m_0\ge\max(r,0)$, and put
\[
 \begin{aligned}
 a_\varepsilon(\xi)
   &=\langle\xi\rangle^r(1+\varepsilon^2|\xi|^2)^{-m_0},\\
 \mathcal A_\varepsilon&=a_\varepsilon(D_y),\qquad
 J_y=\langle D_y\rangle .
 \end{aligned}
 \tag{T65}
\]
Here $\xi$ is ordinary tangential frequency; $\eta=h\xi$ remains semiclassical frequency. All constants below may depend on $r,m_0$ and the fixed patch, but not on $\varepsilon$. No derivative in this parameter is asserted.

The multiplier is positive. Its derivatives and those of its reciprocal satisfy
\[
 \begin{aligned}
 |\partial_\xi^\beta a_\varepsilon|
      &\le C_\beta a_\varepsilon
                         \langle\xi\rangle^{-|\beta|},\\
 |\partial_\xi^\beta a_\varepsilon^{-1}|
      &\le C_\beta a_\varepsilon^{-1}
                         \langle\xi\rangle^{-|\beta|},\\
 \frac{a_\varepsilon(\xi+t\theta)}{a_\varepsilon(\xi)}
      &\le C\langle\theta\rangle^{|r|+2m_0},
                  \qquad 0\le t\le1.
 \end{aligned}
 \tag{T66}
\]
To verify these bounds, differentiating a power of $1+|\xi|^2$ gives its original power times a sum of rational factors of the stated decreasing orders. The other factor has the same property with length
$(\varepsilon^{-2}+|\xi|^2)^{1/2}\ge\langle\xi\rangle$;
its constant factor $\varepsilon^{-2m_0}$ cancels in each derivative ratio. The product rule gives both derivative bounds, for positive or negative $r$. For the last line apply (FC1) to the first factor. For the second use
$1+\varepsilon^2|\xi|^2\le2(1+\varepsilon^2|\xi+t\theta|^2)(1+\varepsilon^2|t\theta|^2)$.
The same estimates, the product rule and (FC1) show that a frequency derivative of order $b$ of a ratio in (T66) gains $\langle\xi\rangle^{-b}$ at the cost of a fixed additional power of $\langle\theta\rangle$.

Plancherel gives $\|\mathcal A_\varepsilon z\|_{H^{t-r}}\le\|z\|_{H^t}$ for every real $t$. As $\varepsilon\to0$ the outputs converge to $J_y^rz$ in $H^{t-r}$ by dominated convergence. For fixed positive $\varepsilon$, $a_\varepsilon$ has order $r-2m_0\le0$, so it is bounded on every $H^t$, though that bound need not be uniform in $\varepsilon$. Both it and its reciprocal preserve Schwartz functions and act on tempered distributions by the Fourier definition. These statements distinguish fixed-parameter domain regularity from uniform bounds at the desired Sobolev order.

## 23. The exact commutator and its leading sign

Write the fixed gauged differential operator as $L=D_x^2+R(x,y,D_y)$, where
$R=\sum_{|\alpha|\le2}r_\alpha(x,y)D_y^\alpha$.
We may choose its extension to have compact coefficient support in $y$, uniformly on the normal interval. Indeed replace $R$ outside a larger patch by $(\zeta R+R\zeta)/2$, with a real compact position cutoff $\zeta=1$ near the region containing the input cutoff. This preserves formal self-adjointness and agrees with the original operator there. All derivative terms of $\zeta$ are retained. The constant normal operator is unchanged. In particular the quadratic tangential symbol $r_2$ is real, including after extension.

The normal part commutes exactly with $\mathcal A_\varepsilon$. Define
$\mathcal G_\varepsilon=[L,\mathcal A_\varepsilon]\mathcal A_\varepsilon^{-1}$.
Fourier inversion on each compact coefficient gives its exact left symbol:
\[
 \begin{aligned}
 g_\varepsilon(x,y,\xi)
    &=\sum_{|\alpha|\le2}\xi^\alpha I_{\alpha,\varepsilon},\\
 I_{\alpha,\varepsilon}
    &=(2\pi)^{-d}\int e^{iy\cdot\theta}
             \widehat r_\alpha(x,\theta)\\
    &\qquad\times\left(1-
           \frac{a_\varepsilon(\xi+\theta)}{a_\varepsilon(\xi)}\right)
                   \,d\theta.
 \end{aligned}
 \tag{T67}
\]
For verification, $R\mathcal A_\varepsilon\mathcal A_\varepsilon^{-1}=R$. In the other product an input frequency $\xi$ is first multiplied by $a_\varepsilon(\xi)^{-1}$, shifted by the coefficient's Fourier variable $\theta$, and finally multiplied by $a_\varepsilon(\xi+\theta)$. This gives (T67) with its displayed minus sign. The Fourier transforms of the coefficients and every normal derivative decrease faster than every power of $\theta$. Formula (T66) consequently makes these integrals, and each differentiated version needed below, absolutely convergent. It justifies the operator identity first on Schwartz functions and then distributionally.

Write $\mathfrak r=\sum_{|\alpha|\le2}r_\alpha\xi^\alpha$. Taylor expansion of the numerator in $\theta$ gives, to any fixed order $N$, the finite expression
\[
 -\sum_{1\le|\beta|<N}\frac1{\beta!}
   \frac{\partial_\xi^\beta a_\varepsilon}{a_\varepsilon}
               D_y^\beta\mathfrak r,
\]
with a remainder uniformly in $S^{2-N}_{1,0}$. This claim includes every normal-parameter derivative. In fact the integral remainder contains
$\theta^\beta(\partial^\beta a_\varepsilon)(\xi+t\theta)/a_\varepsilon(\xi)$,
$|\beta|=N$. After any further $\xi$ derivatives, (T66) bounds it by a constant times $\langle\xi\rangle^{-N-b}$ times a fixed power of $\langle\theta\rangle$. Multiplication by $\xi^\alpha$ raises the order by at most two. Arbitrary Fourier decay of the coefficient supplies the integrable majorant, even after $y$ or $x$ derivatives. Thus the finite remainder, not just a formal expansion, has the asserted uniform order.

In particular,
\[
 \begin{aligned}
 g_\varepsilon
    &=i\ell_\varepsilon(\xi)\cdot\partial_y r_2
                                   +b_\varepsilon,\\
 \ell_\varepsilon(\xi)
    &=\frac{r\xi}{1+|\xi|^2}\\
    &\quad-\frac{2m_0\varepsilon^2\xi}{1+\varepsilon^2|\xi|^2},\\
 &\{b_\varepsilon\}\text{ is bounded in }S^0_{1,0}.
 \end{aligned}
 \tag{T68}
\]
The first-order term is purely imaginary because $r_2$ and $\ell_\varepsilon$ are real. The contribution of the first-order and zero-order coefficients of $R$ is included in $b_\varepsilon$. It is not removed by assuming the operator has no lower terms.

Here are norm bounds with the same uniformity, proved directly rather than inferred from a parameter-dependent inverse norm:
\[
 \begin{aligned}
 &\|\mathcal G_\varepsilon z\|_{H^t_y}\\
 &\quad\le C_t\|z\|_{H^{t+1}_y},\\
 &\|(\mathcal G_\varepsilon+
                \mathcal G_\varepsilon^*)z\|_{H^t_y}\\
 &\quad\le C_t\|z\|_{H^t_y}.
 \end{aligned}
 \tag{T69}
\]
The adjoint here is tangential at a fixed $x$. By the first-order Taylor formula and (T66), the Fourier kernel of $\mathcal G_\varepsilon$ is bounded by
$C_M\langle\xi-\xi'\rangle^{-M}\langle\xi'\rangle$
for arbitrary $M$. Conjugating its Fourier kernel by the two Sobolev weights and using (FC1) leaves an integrable function of $\xi-\xi'$. Its row and column integrals are bounded; the proved Schur estimate and Plancherel give the first line.

For the second line use the actual self-adjointness of $R$ on Schwartz pairings. If $K_R(\xi,\xi')$ denotes its Fourier kernel and $a=a_\varepsilon$, the sum of the two kernels is exactly
$[2-a(\xi)/a(\xi')-a(\xi')/a(\xi)]K_R(\xi,\xi')$.
The bracket factors as
$[a(\xi)/a(\xi')-1][a(\xi')/a(\xi)-1]$.
Each difference gains one inverse frequency factor by (T66) and the first-order Taylor formula. The change from $\langle\xi\rangle$ to $\langle\xi'\rangle$ costs only a power of $\langle\xi-\xi'\rangle$. These two gains cancel the degree at most two of $K_R$. Arbitrary Fourier decay of its coefficient then proves the order-zero Schur bound, with the same Sobolev conjugation. Normal derivatives act only on the coefficients and obey the same estimates. Integrating the pointwise estimates in $x$ is therefore valid.

## 24. The regularized Dirichlet family and its actual equation

Take the fixed $u=\chi v$ from Section 21 and put $u_\varepsilon=\mathcal A_\varepsilon u$. At every fixed $\varepsilon>0$ this family belongs to the $H^2$ Dirichlet domain and has the same compact normal support. To check the domain, the multiplier is bounded on tangential $H^j$ for fixed $\varepsilon$, and it commutes with each normal derivative. It therefore preserves the $L^2$ norms of all derivatives through total order two up to a finite parameter-dependent constant. The continuous normal $L^2_y$ trace commutes with this bounded tangential multiplier, by the norm-primitive trace construction. Since $u(0)=0$, its image trace is also zero.

The operator identities on smooth inputs extend to this domain by the same density and Fourier bounds, and give
\[
 \begin{aligned}
 P_hu_\varepsilon
     &=\mathcal A_\varepsilon f
                     +h^2\mathcal G_\varepsilon u_\varepsilon,\\
 f&=h^2[L,\chi]v,\qquad u_\varepsilon(0)=0,\\
 u_\varepsilon&\longrightarrow J_y^ru
                         \quad\hbox{distributionally}.
 \end{aligned}
 \tag{T70}
\]
Both forcing terms are present. In particular a homogeneous equation for $v$ does not make the second term zero. There are uniform lower-order controls: for $j=0,1,2$, the $L^2_xH^{-r}_y$ norm of $\partial_x^ju_\varepsilon$ is bounded by the $L^2$ norm of $\partial_x^ju$. These follow immediately from $a_\varepsilon\le\langle\xi\rangle^r$. They do not assert a uniform unweighted $H^2$ bound as $\varepsilon\to0$.

## 25. Uniform cutoff-forcing and incoming-edge estimates

Shrink the fixed tangential frequency patch if needed so that $0<c_0\le|\eta|\le C_0$ on every retained symbol support. This is possible at the nonzero glancing covector and is consistent with every preceding compact support choice. On such an annulus,
\[
 |\partial_\eta^\beta a_\varepsilon(\eta/h)|
                 \le C_\beta h^{-r}.
 \tag{T71}
\]
Indeed the uniform $S^r$ estimate from (T66), the chain rule and $\langle\eta/h\rangle\asymp h^{-1}$ give this bound, for positive or negative $r$.

Keep the separated position cutoff $m$ from Section 20. For any fixed $N$ the following bounds are uniform in both $h$ and $\varepsilon$:
\[
 \begin{aligned}
 &\|T_h\mathcal A_\varepsilon m\|_{L^2\to L^2}
       \le C_Nh^N,\\
 &T_h\in\{A_{0,h},B_h,B_h',\Lambda_h\},\\
 &\|\operatorname{Op}^{\rm full}_h(\widetilde\mu_e)
                \mathcal A_\varepsilon m\|_{L^2\to L^2}\\
 &\quad\le C_Nh^N.
 \end{aligned}
 \tag{T72}
\]
The full-line statement uses the same position cutoff extended smoothly there. Multiplication by the interior $\theta$ may be included because it commutes with $\mathcal A_\varepsilon$ and does not enlarge the input support.

Here are the product estimates needed to establish (T72), including adjoints. Right composition of a left tangential symbol $a(x,y,\eta)$ with the Fourier multiplier is exact multiplication by $a_\varepsilon(\eta/h)$. Formula (T71) and (T58), with as many integrations as needed to offset $h^{-r}$, give the separated norm bound. For its adjoint counterpart first examine $\mathcal A_\varepsilon\operatorname{Op}_h(a)$ using (N19). The exact integral contains $a_\varepsilon(\eta/h+\theta)\widehat a_y(\theta,\eta)$. Taylor expansion in $h\theta$ through order $L-1$ has coefficients supported where derivatives of $a$ are supported. Its remainder is $h^{L-r}$ times a bounded symbol with compact $\eta$ support. To verify the bound also for large $\theta$, apply (FC1) to $\eta/h+t\theta$: after any fixed $\eta$ derivatives it bounds the differentiated multiplier by $h^{-r}$ times a fixed power of $\langle\theta\rangle$, which the Fourier decay of $a$ absorbs. This is the finite majorant argument of (N20), now uniform in $\varepsilon$.

Take adjoints of that finite identity and use the finite adjoint expansion on each compact coefficient. The coefficients remain supported in the same base region; the remainder retains arbitrarily high powers after choosing $L$. Applying (T58) on the right therefore bounds $\operatorname{Op}_h(a)^*\mathcal A_\varepsilon m$ as well. This treats the self-adjoint quantizations $A_{0,h}$ and $(\lambda-k-\beta_x)^s_h$. For $B_h=S_h^*S_h$, the right factor $S_h\mathcal A_\varepsilon m$ already has the bound, and $S_h^*$ is uniformly bounded. Differentiate this product once to treat $B_h'$, retaining both terms. These observations also treat $\Lambda_h$. Finally the full quotient product is exactly the symbol $\widetilde\mu_e(x,y,s,\eta)a_\varepsilon(\eta/h)$. After multiplication by $h^r$ it has all the uniform bounded derivatives needed in (T58), including the noncompact normal-frequency tail. This proves the last line of (T72).

Although $\mathcal A_\varepsilon f$ no longer has separated position support, (T72) applies because the original $f=mf$ does. In each of the three actual forcing pairings used for (T60), its contribution is bounded by $C_Nh^N\|f\|H_h(u_\varepsilon)$, taking one extra order for the main factor $h^{-1}$. Normal differentiation is again left on the solution, never moved onto the forcing.

The incoming edge has a uniform bound for this particular family too:
\[
 \begin{gathered}
 \|E_{i,h}u_\varepsilon^0\|_{H^j}
           \le C_{N,j,u}h^N,\\
 i=1,2,\qquad N,j\ge0.
 \end{gathered}
 \tag{T73}
\]
The tangential multiplier commutes with normal zero extension. The exact full left symbol of $E_{i,h}\mathcal A_\varepsilon$ is the edge symbol multiplied by $a_\varepsilon(\eta/h)$. After normalization by $h^r$ it has uniformly bounded derivatives by (T71), with the unchanged compact full-phase support in the regular interior neighborhood. Apply the actual proof of (T16) to this bounded symbol family and the fixed distribution $u^0$. Arbitrarily many powers there absorb $h^{-r}$ and any prescribed output derivatives. Thus (T73) follows from a proved uniform symbol statement; it is not inferred for arbitrary regularized families.

## 26. The limiting argument and the remaining energy term

For later use, let $B$ be a fixed tangential localization, or another fixed operator continuous on the distributions under consideration. If an estimate establishes
\[
 \begin{gathered}
 \sup_{0<\varepsilon\le1}\|Bu_\varepsilon\|_2\le C,\\
 \text{then }BJ_y^ru\in L^2,\qquad
                    \|BJ_y^ru\|_2\le C.
 \end{gathered}
 \tag{T74}
\]
To prove this, test the distributional convergence in (T70) against compact smooth functions. Cauchy–Schwarz bounds each pairing by $C$ times the test's $L^2$ norm. The limiting functional extends by the proved smooth density to all of $L^2$ with the same bound. The [programme Hilbert representation proof](finite-trace-ideals.md#elementary-hilbert-tools) supplies an $L^2$ representing vector. Equality on all compact smooth tests identifies that vector with $BJ_y^ru$. This argument claims no boundary trace of an otherwise unspecified limiting distribution. It also applies with a retained normal derivative once the corresponding distributional convergence and uniform norm bound have been proved.

The remaining forcing in (T70) is $h^2\mathcal G_\varepsilon u_\varepsilon$. Its contributions include $2h\operatorname{Im}(\mathcal G_\varepsilon u_\varepsilon,A_hu_\varepsilon)$ and the two bulk/edge equation pairings with $h^2\mathcal G_\varepsilon u_\varepsilon$ in place of $f$. Equations (T68)–(T69) identify and bound this first-order operator uniformly, but its purely imaginary leading symbol does not make that imaginary energy pairing vanish. Sections 27–31 below control these actual pairings with a scalable positive weight and remainders uniform in the available lower Sobolev norms. Sections 32–35 recover local energy from the corrected squares and prove the conditional Sobolev half-step. Sections 48–54 supply the joint support and regularity induction and fixed-neighborhood smoothness at strict diffraction. The full theorem including the other contact types remains open. None of (T65)–(T74) changes the full theorem or spectral-remainder obligations.

<a id="regularized-commutator-energy"></a>

## 27. The real coefficient in the regularized energy term

Keep a fixed real Sobolev order $r$, the integer $m_0$ and the regularized family of Section 24. The regularizer parameter is still $\varepsilon$, whereas $\epsilon$ is the fixed geometric shift. On the retained tangential annulus, define
\[
 \begin{aligned}
 b_{h,\varepsilon}(z)
   &=v_{h,\varepsilon}(\eta)\cdot\partial_y r_2(x,y,\eta),\\
 v_{h,\varepsilon}(\eta)
   &=\frac{r\eta}{h^2+|\eta|^2}\\
   &\quad-\frac{2m_0\varepsilon^2\eta}
                       {h^2+\varepsilon^2|\eta|^2}.
 \end{aligned}
 \tag{T75}
\]
The variables in $z$ are $(x,y,\eta)$, and $r_2$ is the quadratic symbol of the ordinary tangential differential operator $R$. Thus $r_2(x,y,\eta/h)=h^{-2}r_2(x,y,\eta)$. Equations (T68) and (T75) give
\[
 \begin{gathered}
 h g_\varepsilon(x,y,\eta/h)
       =i b_{h,\varepsilon}(z)+h c_{h,\varepsilon}(z),\\
 \{c_{h,\varepsilon}\}\text{ bounded on the annulus}.
 \end{gathered}
 \tag{T76}
\]
Here and below boundedness includes every fixed derivative in $x,y,\eta$. Both families in (T76) are uniform for $0<h,\varepsilon\le1$. For the second fraction in (T75), write its denominator as $(h/\varepsilon)^2+|\eta|^2$. Differentiation then gives uniform bounds on the annulus, even when $h/\varepsilon$ tends to zero or infinity. The first fraction has the same property. For $c_{h,\varepsilon}$ use the uniform $S^0_{1,0}$ bound from (T68); an $\eta$ derivative costs $h^{-1}$, cancelled by the corresponding ordinary-frequency decay. In particular $b_{h,\varepsilon}$ is real. Fix a smooth extension from a slightly larger annulus. Its derivatives remain bounded, and write $B$ for a common bound for its absolute value on the phase box. Constants may depend on $r,m_0$ and the box. They do not depend on $h$ or $\varepsilon$.

We will use (T76) only between the actual phase localizations. It is not a global order-zero norm assertion for $h\mathcal G_\varepsilon$.

## 28. Uniform remainders on lower tangential norms

We give the weighted remainder detail needed before sending $\varepsilon$ to zero. For a nonnegative integer $m_1$, put
\[
 \begin{aligned}
 \mathfrak L_{m_1,h}(w)^2
    &=\sum_{j=0}^2\|J_y^{-m_1}d_x^jw\|^2,\\
 \sup_{h,\varepsilon}\mathfrak L_{m_1,h}(u_\varepsilon)
    &\le C\|u\|_{H^2},\\
 &m_1\ge\max(r,0).
 \end{aligned}
 \tag{T77}
\]
The second line follows directly from (T65), since $h\le1$. This is the available uniform global norm. We do not replace it by an unweighted $H^2$ bound.

Here is how to strengthen the arbitrary-order remainders in Sections 13–20 to this norm. A smooth compact tangential symbol $a(x,y,\eta)$ in the fixed annulus has Fourier kernel
$(2\pi)^{-d}\widehat a(x,\xi-\xi',h\xi')$. It satisfies, with all fixed normal derivatives,
\[
 \begin{aligned}
 &|K_{a,h}(\xi,\xi')|\\
 &\quad\le C_M\langle\xi-\xi'\rangle^{-M}
                    {\bf1}_{K}(h\xi'),\\
 &|K_{\mathcal G,\varepsilon}(\xi,\xi')|\\
 &\quad\le C_M\langle\xi-\xi'\rangle^{-M}
                                      \langle\xi'\rangle .
 \end{aligned}
 \tag{T78}
\]
The first assertion is Fourier integration by parts in the compact position variable; the second was proved in (T69). The compact set $K$ is contained in a slightly larger annulus. If an input or output frequency lies outside a still larger annulus while the other lies in $h^{-1}K$, their difference is at least a fixed multiple of $h^{-1}$, or of the larger frequency when that is larger. Taking $M$ arbitrarily large then bounds the omitted-frequency kernels, after multiplication by any fixed powers of $\langle\xi\rangle$ and $\langle\xi'\rangle$, by $O(h^N)$ in both Schur integrals. For compositions, integrate the product of the two kernels in the middle frequency. The convolution of two sufficiently large inverse powers has the same required decay. The extra factor in the second line costs one frequency power; it does not prevent an arbitrary $N$.

It follows that one may put fixed, slightly larger annular Fourier cutoffs on both sides of every finite localized product, at an error $O(h^N)$ from $H_y^{-m_1}$ to $H_y^{m_1}$. The same statement holds for a product containing one $h\mathcal G_\varepsilon$. On the enlarged annulus its symbol is (T76), with uniform derivatives. The finite product and adjoint calculations (N19)–(N21) therefore apply uniformly. A remainder of order $h^L$ there, sandwiched by the annular cutoffs, has $H_y^{-m_1}\to H_y^{m_1}$ norm at most $C_Lh^{L-2m_1}$: each of the two Fourier weights has norm at most $Ch^{-m_1}$ on that annulus. Choose $L$ beyond $N+2m_1$ and beyond the finite additional losses from a commutator divided by $h$.

For spatial cutoffs and adjoints the same conclusion follows directly from the transposed kernels. For a separated position factor, integrate the oscillatory kernel as in (T58), taking extra integrations for the inserted Fourier weights. For the full symbols with a normal-frequency tail used in (T50), insert these cutoffs only in the tangential frequency. Their normal derivatives and normal-frequency derivatives have the uniform bounds proved in (T37) and Section 15. The full bounded-amplitude estimate then gives the same weighted operator norm. The tangential weights commute with the normal cutoffs and zero extension. No inverse power of the normal frequency is introduced, and no trace of a negative-order distribution is taken.

There is a minor support issue when a finite remainder is not compactly supported in the position variable. Keep its bounded-amplitude remainder as such, insert the enlarged annular cutoffs as just proved, and retain its chosen $h^L$. Only the finite coefficients are used in the support factorization (T44). Their supports stay in the support of the original compact coefficients and their derivatives. The tail of $\mathcal G_\varepsilon$ in the position variable has the same treatment: off a larger position cutoff its uniform $S^1$ kernel is smooth by repeated frequency integration, and the separated-position calculation applies. These observations prove the weighted assertion for actual remainders, not only for the formal coefficients.

Consequently every arbitrarily small quadratic remainder needed here is bounded by $C_Nh^N\mathfrak L_{m_1,h}(w)^2$. A bilinear remainder with one tangential forcing factor is treated by the same weighted duality. Normal derivatives in the exact energy calculation are at most two before reduction and at most one in its quadratic forms; both are included in (T77). For the particular family $w=u_\varepsilon$, all these bounds are uniform in $\varepsilon$.

The same reasoning improves the use of (T72): its separated forcing operator may be estimated into $H_y^{m_1}$, with any prescribed power of $h$, and then paired with $u_\varepsilon$ or $d_xu_\varepsilon$ in $H_y^{-m_1}$. Its contribution is thus $O(h^N)$ with constants depending on the fixed $u$ and the fixed cutoff forcing, but not on the regularizer parameter. Equation (T73), already valid in every output Sobolev norm, gives the same conclusion for the actual incoming-edge pairing.

## 29. Increasing transport positivity on the same support

Introduce a number $\tau\ge1$, fixed before $h,\varepsilon$ vary, and define a second family of weights
\[
 \begin{aligned}
 \chi_\tau(v)&=e^{\tau/v}\quad(v<0),\\
 \chi_\tau(v)&=0\quad(v\ge0),\\
 q_\tau&=\nu\zeta^2\chi_\tau(\phi_\nu-\epsilon),\\
 e_\tau&=\nu\chi_\tau(\phi_\nu-\epsilon)H_p(\zeta^2).
 \end{aligned}
 \tag{T79}
\]
The geometric cutoffs, shift and phase box are unchanged. In particular their closed supports and the prescribed regular interior edge do not depend on $\tau$. The old weights are the case $\tau=1$, and their proofs remain available.

All flatness and divided-square-root arguments of Sections 3–6 apply at each fixed $\tau$. To verify the precise input, every derivative of $e^{\tau/v}$ is that exponential times a polynomial in $1/v$ with coefficients depending on $\tau$. Such a polynomial is bounded by a constant times $e^{\gamma\tau/|v|}$ for any $\gamma>0$ on the fixed negative interval. This proves the analogues of (C19) and (T18). Its derivative is $-\tau e^{\tau/v}/v^2$, with the same sign as before. Thus the averaging proof (T19)–(T22) gives a smooth divided square root, and the extension in Section 6 gives a nonnegative coefficient $\beta_\tau$ on both sides of glancing. Denote the resulting multiplier by $A_{\tau,h}$ and its boundary factor by $S_{\tau,h}$. They obey the exact identity (T26).

Let $v=\phi_\nu-\epsilon$ and $D=2\sigma+\epsilon$. On the nonzero weight support, $-D\le v<0$. With $c\ge\kappa$ and the bound $B$ after (T76), choose
$\tau\ge\max(1,4BD^2/\kappa)$. Then the following is an exact full-symbol identity on that support:
\[
 \begin{aligned}
 &H_pq_\tau-2b_{h,\varepsilon}q_\tau
       =\widehat j_{h,\varepsilon}^{\,2}+e_\tau,\\
 &\widehat j_{h,\varepsilon}
       =\frac{\zeta e^{\tau/(2v)}}{-v}
                         \sqrt{c\tau-2\nu b_{h,\varepsilon}v^2},\\
 &c\tau-2\nu b_{h,\varepsilon}v^2
       \ge c\tau/2 .
 \end{aligned}
 \tag{T80}
\]
Set $\widehat j=0$ at $v\ge0$. The positive radical is defined in a neighborhood of the compact support and can be extended before multiplying by $\zeta$. Its lower bound and the flat exponential show smoothness at every zero. The symbols and all their spatial derivatives are bounded uniformly in $h,\varepsilon$. Constants may depend on the chosen $\tau$. This is how the actual real coefficient in the energy pairing is absorbed; it is not discarded by its sign or by formal skew-adjointness.

For clarity, this choice keeps the phase support fixed as the Sobolev order changes: a new order may require a larger $\tau$, rather than a smaller $\sigma$ or geometric shift. It does not by itself prove that the later two-square inverse or the whole regularity induction works on one fixed neighborhood.

## 30. Dividing and quantizing the corrected positive square

Divide $q_\tau,\widehat j,e_\tau$ as in (T10) and (T28). Write their coefficients as $\alpha_\tau,\beta_\tau$, $\widehat j_0,\widehat j_1$ and $e_{0,\tau},e_{1,\tau}$. Only the square coefficients depend on $h,\varepsilon$. Put
\[
 \begin{aligned}
 \widehat F
     &=H_p(\alpha_\tau+\beta_\tau s)\\
     &\quad-2b_{h,\varepsilon}(\alpha_\tau+\beta_\tau s),\\
 \widehat\lambda&=F_{2,\tau}-\widehat j_1^2,\\
 \widehat D_0
     &=F_{0,\tau}-2b_{h,\varepsilon}\alpha_\tau\\
     &\quad-\widehat j_0^2-e_{0,\tau}-\widehat\lambda a_0,\\
 \widehat D_1
     &=F_{1,\tau}-2b_{h,\varepsilon}\beta_\tau\\
     &\quad-2\widehat j_0\widehat j_1-e_{1,\tau}.
 \end{aligned}
 \tag{T81}
\]
Here $F_{k,\tau}$ are the three Hamilton-derivative coefficients of (T29) for $\alpha_\tau,\beta_\tau$. The correction is normal-linear, so it changes neither $F_{2,\tau}$ nor the normal reduction in (T35).

At both real characteristic roots, (T80) gives exactly $\widehat F=(\widehat j_0+\widehat j_1s)^2+e_{0,\tau}+e_{1,\tau}s$. Hence $\widehat D_0,\widehat D_1$ vanish on the real-root side and are flat at $a_0=0$, with uniform flat bounds. The smooth division and jet extension may be made uniform for this family: their proofs use suprema of finitely many derivatives at each fixed order. In (C5), choose each extension radius using the supremum over $h,\varepsilon$ of the finitely many seminorms used at that step. These suprema are finite by (T76) and (T80). No derivative in either parameter is required. Taylor's integral remainder gives the uniform flat estimates after the extension.

Choose the common elliptic collar and parameter cutoffs as in Sections 12–14, using the larger shifted $q_{\tau,+}$. Its divided square root is denoted $s_{\tau,+}$. The support set of the real-root coefficients is unchanged because $q_\tau$ and $\widehat j$ have the same phase support as the old cutoff. The compact positivity argument (T48) applies to $\beta_{\tau,+}$ at this fixed $\tau$. Choose the coefficient extensions inside that positive region. In the construction (T31), take each $A_m$ to be the supremum also over $h,\varepsilon$. Uniform flatness gives the same arbitrary geometric decay, so the resulting smooth $k$ is a common majorant. The proof of (T32), entry by entry, gives a uniformly bounded positive matrix $\widehat N$ and
\[
 \begin{aligned}
 \widehat F
   &=(\widehat j_0+\widehat j_1s)^2\\
   &\quad+(e_{0,\tau}+e_{1,\tau}s)\\
   &\quad+(\widehat\lambda-k)p
                     +(1,s)\widehat N(1,s)^{\mathsf T},\\
 \widehat N&\ge0,\\
 \widehat J_hw&=\operatorname{Op}_h(\widehat j_0)w\\
   &\quad+\operatorname{Op}_h(\widehat j_1)d_xw.
 \end{aligned}
 \tag{T82}
\]
The full-phase characteristic cutoff $\gamma(p)^2$ may again be inserted without changing these root coefficients. Since $b_{h,\varepsilon}$ is a multiplier in the symbol identity and $H_pp=0$, both terms on the left of (T80) are multiplied by the same $\gamma(p)^2$. The actual edge remains in the regular interior neighborhood. All the finite coefficients and their derivatives are supported where $s_{\tau,+}$ is bounded away from zero.

Apply the exact calculation (T36) after subtracting the real quadratic form with symbol $2b_{h,\varepsilon}(\alpha_\tau+\beta_\tau s)$. Its principal polynomial is now (T82). The square norm, positive-matrix packet argument and equation-multiple calculation (T34)–(T35) apply uniformly, because the relevant finitely many symbol bounds are uniform. The boundary factor remains the original $S_{\tau,h}$; nothing has been subtracted from its nonnegative squared norm. Every order-$h$ form error is controlled by
$Ch\mathcal H_{\tau,+,h}(w)^2$, with
$\mathcal H_{\tau,+,h}(w)^2=\|\operatorname{Op}_h(s_{\tau,+})w\|^2+\|\operatorname{Op}_h(s_{\tau,+})d_xw\|^2$,
plus an arbitrary-order lower-norm remainder from Section 28.

## 31. The energy estimate for the actual regularized wave

Take $w=u_\varepsilon=\mathcal A_\varepsilon u$ and its exact equation (T70). The main regularizer forcing in (T26) is
$2\operatorname{Im}(h\mathcal G_\varepsilon w,A_{\tau,h}w)$.
Expand $A_{\tau,h}=A_{0,\tau,h}+B_{\tau,h}d_x-ihB_{\tau,h}'/2$ and use the localized formula (T76). The principal terms are precisely the real form with symbol $2b_{h,\varepsilon}(\alpha_\tau+\beta_\tau s)$: $\operatorname{Im}(iz_1,z_2)=\operatorname{Re}(z_1,z_2)$ in our first-variable-linear inner product. Moving only the tangential factors and using their finite products leaves order-$h$ forms in $(w,d_xw)$. The derivative term $-ihB_{\tau,h}'/2$ also has that order. Section 28 and the common support factorization bound the complete difference by
$Ch\mathcal H_{\tau,+,h}(w)^2+C_Nh^N\mathfrak L_{m_1,h}(w)^2$.

There are two other uses of the equation. The bulk pairing has the actual bounded factor
$\widehat\Lambda_h=(\widehat\lambda-k-\partial_x\beta_\tau)^s_h+B_{\tau,h}'$.
Its regularizer part is $h(\widehat\Lambda_h\,h\mathcal G_\varepsilon w,w)$. The localized order-zero expansion (T76) and Section 28 bound it by the same order-$h$ weighted energy error and arbitrary-order lower-norm remainder. The full-phase quotient pairing is
$h(\operatorname{Op}^{\rm full}_h(\widetilde\mu_{e,\tau})\theta\,h\mathcal G_\varepsilon w,w^0)$,
with the interior normal cutoff and zero extension understood as in (T39). The normal cutoff commutes with $\mathcal G_\varepsilon$. Its finite full products have the bounded normal-frequency tail and compact tangential support required in Section 28. They obey the same bound. The equation is applied to the interior cutoff of $w$, never across the wall. Thus all three commutator forcing pairings have been accounted for.

The remaining forcing is $\mathcal A_\varepsilon f$, where $f=h^2[L,\chi]v$. Its separated-support contribution is arbitrarily small by the weighted version of (T72) proved in Section 28. The actual edge contribution is arbitrarily small by (T73) and weighted duality. These estimates apply also to the fixed $\tau$ weight: the closed supports are unchanged, and its finitely many new symbol seminorms only change the constants. Combining the exact identity (T26), (T82), these forcing estimates and the weighted remainders proves
\[
 \begin{aligned}
 &\|\widehat J_hu_\varepsilon\|^2
          +\|S_{\tau,h}(0)d_xu_\varepsilon(0)\|^2\\
 &\qquad\le Ch\mathcal H_{\tau,+,h}(u_\varepsilon)^2
                              +C_{N,u}h^N,\\
 &0<h,\varepsilon\le1,\qquad N\ge1.
 \end{aligned}
 \tag{T83}
\]
The constant $C_{N,u}$ uses the fixed wave's $H^2$ norm, the cutoff forcing and its microlocal smoothness seminorms on the actual incoming interior edge. It may depend on the fixed order $r$, $m_0$, the geometric cutoffs and the selected $\tau$. It is independent of $h,\varepsilon$. The weighted norm on the right is still an explicit input. For each positive regularizer parameter the input is in the $H^2$ Dirichlet domain, so the already proved approximation argument applies; no limiting boundary trace is being assumed.

This proves the regularized commutator energy estimate. Sections 32–35 below recover the required local energy from the corrected squares and prove a conditional Sobolev half-step using (T74). Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38.

<a id="corrected-squares-and-sobolev-gain"></a>

## 32. The corrected squares have a uniform inverse

Use the two shifts $\epsilon_1=\epsilon$ and $\epsilon_2=\epsilon/2$, with $0<\epsilon<1$, and the same orientation, phase box and Sobolev regularizer. Use a common fixed $\tau$ in (T79), large enough for (T80) for both shifts. Write $c_*=c(z_*)$ and $b_*=b_{h,\varepsilon}(z_*)$. At the central point the cutoff factors are one, $\partial_s\phi_\nu=-\nu$, and $c,b_{h,\varepsilon}$ are independent of the normal frequency $s$. Direct differentiation of (T80) therefore gives
\[
 \begin{aligned}
 a_i&=c_*\tau-2\nu b_*\epsilon_i^2,\\
 \widehat j_{0,i}(z_*)&=
     \epsilon_i^{-1}e^{-\tau/(2\epsilon_i)}\sqrt{a_i},\\
 m_i&=\frac{\widehat j_{1,i}(z_*)}{\widehat j_{0,i}(z_*)}\\
    &=\nu\left(\frac{\tau}{2\epsilon_i^2}
                          -\frac1{\epsilon_i}\right)
                      -\frac{2b_*\epsilon_i}{a_i}.
 \end{aligned}
 \tag{T84}
\]
The double-root division formula identifies $\widehat j_{1,i}$ with the normal-frequency derivative. The last term in $m_i$ is the derivative of the new radical; it must be retained.

The bounds $|b_*|\le B$ and $a_i\ge\kappa\tau/2$ show
\[
 \begin{aligned}
 &\left|m_2-m_1-
           \nu\frac{3\tau-2\epsilon}{2\epsilon^2}\right|\\
 &\qquad\le\frac{6B\epsilon}{\kappa\tau},\\
 |m_2-m_1|&\ge\frac{\tau}{2\epsilon^2},\\
 \tau&\ge\max\left(2,\sqrt{12B\epsilon^3/\kappa}\right).
 \end{aligned}
 \tag{T85}
\]
The last line is an additional permitted choice of $\tau$, together with (T80). Indeed $\tau\ge2$ and $\epsilon<1$ give $(3\tau-2\epsilon)/(2\epsilon^2)\ge\tau/\epsilon^2$, and the additional square-root bound makes the error at most half this quantity. Both $\widehat j_{0,i}(z_*)$ have positive lower bounds independent of $h,\varepsilon$, at the fixed $\tau$. Consequently the determinant of the matrix $\widehat{\mathcal J}$ with rows $(\widehat j_{0,i},\widehat j_{1,i})$ has a positive absolute lower bound at $z_*$, uniformly in these parameters.

The spatial derivatives of this matrix are uniformly bounded by Section 30. The mean-value estimate for its determinant gives one neighborhood on which the determinant stays away from zero for every $h,\varepsilon$. Choose a real compact tangential phase cutoff $q=1$ near $z_*$, supported there and where both larger shifted weights are positive. For this fixed Sobolev order the cutoff is independent of $h,\varepsilon$. Its neighborhood is not yet claimed uniform in $r$.

The entries of $q\widehat{\mathcal J}^{-1}$ have uniform derivatives: differentiate the adjugate-over-determinant formula using the lower determinant bound. Construct a finite left inverse as in (T56). At each order the previous product error is cancelled by multiplying its symbol by $\widehat{\mathcal J}^{-1}$; nested cutoffs retain the support inside the uniformly invertible region. The finite product formula is uniform for parameter-dependent symbols with these derivative bounds. It does not require an expansion or a derivative in $h$ or $\varepsilon$. Section 28 bounds its remainder on the actual lower norms after choosing sufficiently many terms.

## 33. Uniform local energy for the regularized family

Let $Q_h=\operatorname{Op}_h(q)$ and let $\mathcal H_{i,h}$ denote the larger shifted norm for the $i$th corrected square. Apply the finite inverse just constructed to the vector $(u_\varepsilon,d_xu_\varepsilon)$. Square its norm, use the two instances of (T83), and use the lower-norm remainder estimate (T77). For every $N\ge1$ this proves
\[
 \begin{aligned}
 &\|Q_hu_\varepsilon\|^2
               +\|Q_hd_xu_\varepsilon\|^2\\
 &\qquad\le Ch\sum_{i=1}^2
                       \mathcal H_{i,h}(u_\varepsilon)^2
                               +C_{N,u}h^N,\\
 &0<h,\varepsilon\le1.
 \end{aligned}
 \tag{T86}
\]
All constants are uniform in the displayed parameters. The weighted norms on the right still have their stated meaning. The full output energy $H_h(Q_hu_\varepsilon)$ has the same bound: use $d_xQ_h=Q_hd_x-ihQ_h'$, factor $Q_h'$ through either larger weight by (T44), and absorb its squared factor $h^2$ into $h$. This retains the normal commutator and the zero Dirichlet value. The equation estimate was applied before the output cutoff, so no unestimated $[P_h,Q_h]u_\varepsilon$ has been dropped.

For a finite number of frequency bands bounded away from $h=0$, increase the constant if necessary. Their tangential frequency localizations and the uniform bound $a_\varepsilon(\xi)\le\langle\xi\rangle^r$ give uniform finite-band norms directly from the fixed $u\in H^2$. Thus the same estimate can be used on any geometric sequence of small frequency scales, with its finite initial segment treated separately.

## 34. A frequency-band reconstruction with a fixed cutoff

We prove the summation statement needed to turn (T86) into Sobolev regularity. Choose a compact product of a base neighborhood, angular neighborhood and radial interval $[a,b]\Subset(0,\infty)$ inside the region where $q=1$. Choose $\varrho>1$ sufficiently close to one that some smaller interval and its $\varrho$-multiple are both inside $(a,b)$. Let $\theta\ge0$ be smooth, supported in $(a,b)$ and strictly positive on an interval $[a',\varrho a']$. For $t>0$ set
\[
 \begin{gathered}
 Z(t)=\sum_{k\in\mathbb Z}\theta(\varrho^{-k}t),\\
 \psi(t)=\theta(t)/Z(t),\qquad h_k=\varrho^{-k},\\
 \sum_{k\in\mathbb Z}\psi(h_kt)=1,\\
 \sup_{t>0}\#\{k:h_kt\in[a,b]\}<\infty.
 \end{gathered}
 \tag{T87}
\]
Each sum defining $Z$ is locally finite, positive and smooth; $Z(\varrho t)=Z(t)$. These facts prove the partition identity. The number of terms is bounded by a fixed integer greater than $1+\log(b/a)/\log\varrho$, proving the overlap statement. For all sufficiently large $t$, the terms with $k<0$ vanish, so the sum over $k\ge0$ is one. Its defect is a smooth compact-frequency cutoff, equal to one near zero.

Choose a smooth compact position cutoff $b_0(x,y)$ and a smooth angular cutoff in the smaller product where $q=1$. Let $\Omega(\xi)$ be the latter angular cutoff times a radial cutoff vanishing near zero and equal to one at large radius. Define $\mathcal B=b_0(x,y)\Omega(D_y)$ and
$\mathcal B_k=b_0(x,y)\Omega(D_y)\psi(h_k|D_y|)$.
The symbol of each $\mathcal B_k$ has normalized support inside $\{q=1\}$; a strict support margin is retained. The partition identity gives $\mathcal B=\sum_{k\ge0}\mathcal B_k$ modulo a tangentially smoothing compact-frequency operator. This equality first holds on test functions and then on tempered distributions, since the locally finite symbol sum and its differentiated sums have the defining bounded symbol estimates.

For a distribution $z$ with
$\mathfrak K_m(z)^2=\|J_y^{-m}z\|^2+\|J_y^{-m}D_xz\|^2<\infty$,
where $m$ is a sufficiently large nonnegative integer, the following two bounds hold whenever their right sides are finite:
\[
 \begin{aligned}
 &\|\mathcal Bz\|^2\\
 &\quad\le C\sum_{k\ge0}\|Q_{h_k}z\|^2
                                  +C_m\mathfrak K_m(z)^2,\\
 &\|\mathcal B J_y^{-1}D_xz\|^2\\
 &\quad\le C\sum_{k\ge0}h_k^2\|Q_{h_k}D_xz\|^2\\
 &\qquad+C_m\mathfrak K_m(z)^2.
 \end{aligned}
 \tag{T88}
\]
Here all norms include integration over the normal interval. We give both the localization and the summation details.

The finite product expansion gives $\mathcal B_kQ_{h_k}=\mathcal B_k+R_{k,N}$, where $R_{k,N}$ has $H_y^{-m}\to L_y^2$ norm $O(h_k^N)$, uniformly in $x$. Every nonconstant finite coefficient vanishes because derivatives of $q$ vanish near the normalized support of $\mathcal B_k$. The weighted remainder assertion is exactly Section 28. The compact-frequency defect has a bounded $H_y^{-m}\to L_y^2$ norm. Since $\mathcal B_k$ are uniformly bounded, their localized outputs are therefore square summable if the first right side of (T88) is finite.

Square summability alone would not justify summing arbitrary output functions. Here their frequencies can also be confined to fixed enlarged annuli. The Fourier kernel of $\mathcal B_k$ is a rapidly decreasing function of $\xi-\xi'$ times its input annular factor, as in the first line of (T78). Let $\widetilde\psi(h_kD_y)$ equal one on a slightly larger input annulus and have still larger compact annular support. The output tail $(1-\widetilde\psi(h_kD_y))\mathcal B_kz$ is $O(h_k^N)\|J_y^{-m}z\|$ by the weighted Schur proof after (T78). These tails have summable norms. The remaining outputs have finite-overlap Fourier supports. Pointwise Cauchy–Schwarz at each frequency and Plancherel give
$\|\sum_k v_k\|^2\le C\sum_k\|v_k\|^2$
for every finite collection of such band-supported outputs. Their partial sums are Cauchy in $L^2$ and converge to the distributional sum. This proves the first bound.

For the second bound use $\mathcal B_kJ_y^{-1}$. Its left symbol is the symbol of $\mathcal B_k$ times $\langle\xi\rangle^{-1}$, because the latter is a Fourier multiplier on the right. On the input annulus its operator norm is at most $Ch_k$, and after division by $h_k$ its normalized symbol derivatives are uniformly bounded. Apply the same finite localization with $Q_{h_k}$, now to $D_xz$, and choose sufficiently many orders for its weighted remainder. The same output-tail and finite-overlap proof applies. The compact-frequency contribution is bounded by $\|J_y^{-m}D_xz\|$. This proves the second bound. No normal-frequency decomposition or normal extension across the boundary is used in (T87)–(T88).

## 35. An actual half-step Sobolev gain

The hypothesis on the larger weighted region can now be stated precisely. Let $\Pi$ be a fixed order-zero tangential cutoff whose symbol equals one, for sufficiently large frequencies, on a neighborhood of the conic hull of both larger-weight symbol supports. Its high-frequency support may be chosen in any prescribed open conic tangential phase set containing those conic hulls. Suppose
\[
 \begin{aligned}
 F_0&=\Pi J_y^{r-1/2}u\in L^2,\\
 F_1&=\Pi J_y^{r-3/2}D_xu\in L^2.
 \end{aligned}
 \tag{T89}
\]
All other hypotheses remain those of the fixed spatially localized Dirichlet wave: its actual cutoff forcing is separated as in Section 21, and the full incoming edge is microlocally smooth. This is a hypothesis on the solution at the preceding Sobolev order, not a consequence of the existence of the cutoff.

Write $S_{i,h}=\operatorname{Op}_h(s_{i,+})$ for a larger-weight operator. Its symbols are fixed once $r,\tau$ and the geometric choices have been made. Consider
$h^{1/2}S_{i,h}\mathcal A_\varepsilon J_y^{-(r-1/2)}$.
Its exact left symbol is $h^{1/2}s_{i,+}(x,y,h\xi)a_\varepsilon(\xi)\langle\xi\rangle^{-r+1/2}$. On its input annulus all normalized derivatives are bounded independently of $h,\varepsilon$, by (T66) and (T71). The same is true of
$h^{3/2}S_{i,h}\mathcal A_\varepsilon J_y^{-(r-3/2)}$.
The powers $h^{1/2}$ and $h^{3/2}$ cancel the respective frequency growth. Their input Fourier supports remain in a fixed annulus scaled by $h^{-1}$.

Insert $\Pi$ immediately before the weighted input. Its complement gives an arbitrarily small remainder, because the finite coefficient supports lie where its high-frequency symbol is one. Section 28 bounds that remainder on the fixed global lower norms, uniformly in $\varepsilon$. For the retained term choose a scalar annular multiplier equal to one on the exact input frequency support. The uniform operator norm bound and the finite-overlap statement in (T87) show that the squares of these retained outputs sum to at most $C\|F_0\|^2$ or $C\|F_1\|^2$. The normal derivative commutes with $\mathcal A_\varepsilon$, and $d_x=hD_x$, so these are exactly the two terms required below. Consequently
\[
 \begin{aligned}
 &\sup_{0<\varepsilon\le1}\sum_{k\ge0}h_k
             \sum_{i=1}^2\mathcal H_{i,h_k}(u_\varepsilon)^2\\
 &\qquad\le C(\|F_0\|^2+\|F_1\|^2)+C_u.
 \end{aligned}
 \tag{T90}
\]
The finite low-frequency segment and the summable remainders are included in $C_u$. It uses a finite global lower norm of the fixed $u$, not a presumed uniform high norm of $u_\varepsilon$.

Sum (T86) over $h=h_k$, using any $N>0$, and apply (T90). The constant $C_u$ below also includes the actual incoming-edge seminorms and cutoff-forcing bounds from (T83). First keep a finite number of terms. Their uniform bound passes as $\varepsilon\to0$ by the Hilbert representation argument in (T74), applied to the finite vector of outputs and their normal derivatives. The convergence is distributional because $Q_{h_k}$ is fixed and tangential, and normal differentiation is continuous on distributions. Then let the number of terms increase. Monotone convergence for the sum of nonnegative squared norms gives, with $z=J_y^ru$,
\[
 \begin{aligned}
 &\sum_{k\ge0}\|Q_{h_k}z\|^2
       +\sum_{k\ge0}h_k^2\|Q_{h_k}D_xz\|^2\\
 &\qquad\le C(\|F_0\|^2+\|F_1\|^2)+C_u.
 \end{aligned}
 \tag{T91}
\]
Choose $m\ge\max(r,0)$ in (T88); the fixed $H^2$ input makes $\mathfrak K_m(J_y^ru)$ finite. The reconstruction bound therefore proves
\[
 \begin{aligned}
 &\|\mathcal B J_y^ru\|^2
       +\|\mathcal B J_y^{r-1}D_xu\|^2\\
 &\qquad\le C(\|F_0\|^2+\|F_1\|^2)+C_u.
 \end{aligned}
 \tag{T92}
\]
The cutoff $\mathcal B$ is elliptic near the central tangential covector and is fixed throughout the regularizer limit. Equations (T89) and (T92) give a half-order gain for the tangentially localized wave and the corresponding normal derivative. This is a Sobolev statement obtained from a convergent frequency sum, not merely a separate estimate at each frequency. The normal derivative has its required one-order offset throughout. The Fourier-weighted localization in these formulas is the actual definition being used; no unproved commutation of $J_y^r$ through a position cutoff has entered the argument.

## 36. A fixed-neighborhood induction criterion

There is a useful general way to keep the final neighborhood fixed. Suppose an open conic tangential phase set $\mathcal O$ has the following property. Compactness and compact containment here refer to the base variables and unit tangential frequency directions. The required property is this: at every point of each compact subset, for each required order, an estimate of the form (T89)–(T92) is available with output elliptic near that point and with the closed support of its input cutoff $\Pi$ compactly contained in $\mathcal O$. Any additional inputs used by that estimate must already be smooth on explicitly specified sets. Then starting from the available order-two pair, these estimates give every finite half-integer order throughout the same open set $\mathcal O$.

Here are the localization details of this conditional assertion. At one induction step assume the preceding Fourier-weighted pair is locally $L^2$ everywhere in $\mathcal O$. The compact support of a particular $\Pi$ has a finite cover by cutoffs for which those norms are known. On smaller sets divide a partition symbol by each nonvanishing cutoff symbol and construct its finite parametrix using the scalar product proof. Take enough orders that its remainder acts on the fixed global lower norm. Summing this finite partition proves that the two actual inputs in (T89) are $L^2$. The new estimate proves the higher pair near each output point. This holds at every point of $\mathcal O$, completing the induction step. For any fixed compactly supported cutoff inside $\mathcal O$, another such finite cover gives its norms at each order. The cutoff is kept fixed while the covers and constants may depend on the order. Thus this argument would establish all orders on one neighborhood, rather than only on a sequence of neighborhoods shrinking to a point.

Sections 48–50 below prove the geometric support property for the strict-diffraction weights. Sections 51–54 prove the corresponding finite-order propagation and strict-diffraction regularity induction. The larger weights in (T89) contain real-root, elliptic and interior regions. Their required regularity must be supplied by the corresponding propagation and elliptic arguments, with the exact supports checked. In particular neither (T86) nor (T92) declares the larger inner-cutoff transition in (L20) regular. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. The general curved spectral application is proved in the linked spectral reading, Sections 31–38.

<a id="tangentially-elliptic-boundary-regularity"></a>

## 37. Positive normal energy in a tangentially elliptic patch

We now supply the elliptic input required by Section 36. This argument does not require the strict-diffraction condition (T2). It applies wherever the tangential principal symbol of the gauged wave is positive. Keep the actual spatially localized wave $u\in H^2$, its zero Dirichlet trace, the operator $P_h=d_x^2+R_h$ and the regularized family $w=u_\varepsilon$ from (T65)–(T70). The spatial cutoff defining $u$ is one on the base neighborhoods used below. Its equation forcing is therefore separated from those neighborhoods. No incoming-ray regularity is assumed in this section.

Let $\mathcal O_+$ be an open conic tangential phase set, including possible points at $x=0$, whose closure in the chosen base chart stays where that spatial cutoff is one, and on which $a_0>0$. Compactness of phase supports will again mean compactness in the base variables and unit tangential directions. Around any point of $\mathcal O_+$ choose a compact annular patch and real smooth cutoffs $q,s$, with strict margins, such that
\[
 \begin{gathered}
 q=1\text{ near the chosen point},\\
 s=1\text{ near }\operatorname{supp}q,\\
 \operatorname{supp}s\Subset\mathcal O_+,\\
 a_0\ge3c>0\text{ near }\operatorname{supp}s,\\
 Q_h=\operatorname{Op}_h(q),\qquad
 S_h=\operatorname{Op}_h(s),\\
 E_{s,h}(w)^2=\|S_hw\|^2+\|S_hd_xw\|^2.
 \end{gathered}
 \tag{T93}
\]
All symbols have compact normal support at the outer endpoint; at $x=0$ they are smooth up to the boundary. Their supports and all auxiliary enlargements lie in one fixed nonzero tangential annulus. They are independent of $h,\varepsilon$. They need not have any relation to the diffractive weights of the earlier sections.

We first prove coercivity for $v=Q_hw$. Choose a real symbol $t\ge c$ which equals $a_0$ on a neighborhood of $\operatorname{supp}q$ and equals the constant $c$ outside a compact phase set. To construct it take $t=c+\chi(a_0-c)$, where $0\le\chi\le1$, $\chi=1$ near that support, and $\chi$ is supported where $a_0\ge3c$. The scalar case of the packet proof in (T34), applied to $t-c$, gives
$\operatorname{Re}(\operatorname{Op}_h(t)v,v)\ge(c-Ch)\|v\|^2$.
The constant part is exactly $cI$.

Here is the comparison with the actual differential operator, including its lower terms. Write its exact left symbol as $a_0+h a_1+h^2 a_2$, with $a_1$ at most linear and $a_2$ constant in the normalized frequency. The finite coefficients of $\operatorname{Op}_h(a_0-t)Q_h$ all vanish, because $a_0-t$ vanishes on a neighborhood of the support of $q$ and of its derivatives. The finite product formula and the weighted remainder estimate of Section 28 therefore make this product arbitrarily small on $H_y^{-m_1}$. The differential part of that formula terminates after degree two; no boundedness assertion for an unlocalized quadratic symbol is needed.

For the lower terms, confine the output of $Q_h$ to a slightly larger annulus by (T78). On that annulus $a_1,a_2$ and their normalized derivatives are bounded. Outside it the output tail is arbitrarily small, even after one or two tangential derivatives, by the same weighted Fourier-kernel estimate. Thus their contribution is at most $Ch\|v\|^2+C_Nh^N\mathfrak L_{m_1,h}(w)^2$, after Young's inequality. Normal integration by parts has no boundary term: $v(0)=Q_h(0)w(0)=0$, and $v$ vanishes near the outer endpoint. For sufficiently small $h$ this proves
\[
 \begin{aligned}
 &H_h(v)^2\le C\operatorname{Re}(P_hv,v)
       +C_Nh^N\mathfrak L_{m_1,h}(w)^2,\\
 &H_h(v)^2=\|v\|^2+\|d_xv\|^2.
 \end{aligned}
 \tag{T94}
\]
All constants are uniform in $\varepsilon$. For each positive $\varepsilon$ the input is in the $H^2$ Dirichlet domain; the approximation proof already used for (T35) justifies this calculation there. Uniform unweighted $H^2$ bounds on $w$ have not been assumed.

## 38. The equation and all cutoff commutators

Apply the exact equation (T70) before estimating its terms. It gives
\[
 \begin{aligned}
 P_hv={}&Q_h\mathcal A_\varepsilon f
       +h^2Q_h\mathcal G_\varepsilon w\\
       &+[P_h,Q_h]w,\\
 [d_x^2,Q_h]w={}&-2ihQ_h'd_xw-h^2Q_h''w,\\
 \|P_hv\|\le{}&C_rh E_{s,h}(w)+C_{N,r,u}h^N.
 \end{aligned}
 \tag{T95}
\]
We verify the last line. The separated-position proof (T58), with the normalized regularizer bounds (T71) and the weighted version in Section 28, applies to $Q_h\mathcal A_\varepsilon f$. Its symbol has the same required strict spatial separation from the actual support of $f$. It gives any prescribed power of $h$, uniformly in $\varepsilon$.

For $hQ_h\mathcal G_\varepsilon$, use (T76) only between enlarged annular cutoffs. Its finite product coefficients are uniformly bounded and supported in $\operatorname{supp}q$. Since $s=1$ on a neighborhood of that support, the finite factorization through $S_h$ has a uniformly bounded factor and an arbitrarily small weighted remainder. The off-annulus tails and the one extra ordinary-frequency power of $\mathcal G_\varepsilon$ are handled exactly by (T78). Multiplying by the remaining $h$ gives the asserted bound for $h^2Q_h\mathcal G_\varepsilon w$.

The principal products in $[R_h,Q_h]$ cancel. Its finite expansion is $h$ times uniformly bounded annular symbols supported where $q$ or its derivatives are supported, plus an arbitrarily small weighted remainder. The exact lower-order differential terms have the same property. Factor these coefficients through $S_h$. Factor $Q_h'$ and $Q_h''$ through $S_h$ as well, retaining the two displayed normal-commutator terms. This bounds the commutator by $C h E_{s,h}(w)$ plus the weighted remainder. In all these calculations choose the finite expansion order after $m_1$ and $N$. The uniform bound (T77), with $m_1\ge\max(r,0)$, then gives the constant in (T95).

Insert (T95) into (T94), bound $|(P_hv,v)|$ by $\|P_hv\|H_h(v)$, and apply Young's inequality with a fixed small coefficient on $H_h(v)^2$. This proves the following uniform estimate, for any prescribed $N$:
\[
 \begin{aligned}
 &\|Q_hw\|^2+\|Q_hd_xw\|^2\\
 &\qquad\le C_rh^2 E_{s,h}(w)^2+C_{N,r,u}h^N.
 \end{aligned}
 \tag{T96}
\]
To replace $d_xQ_hw$ by $Q_hd_xw$ use $d_xQ_h=Q_hd_x-ihQ_h'$. The last factor again passes through $S_h$, and its squared contribution is $O(h^2)E_{s,h}(w)^2$ plus a weighted remainder. This explains the normal component in (T96). The constant may depend on the requested Sobolev order; it is independent of both small parameters. The finitely many bands outside the small-$h$ range are controlled from the fixed $H^2$ input as in Section 33.

## 39. A full-order gain on the elliptic region

Let $\Pi$ be an order-zero tangential cutoff with compact high-frequency cosphere support in $\mathcal O_+$, equal to one near the conic hull of $\operatorname{supp}s$. Suppose the preceding-order pair is available:
\[
 \begin{aligned}
 &F_0=\Pi J_y^{r-1}u\in L^2,\\
 &F_1=\Pi J_y^{r-2}D_xu\in L^2,\\
 &\sup_{\varepsilon}\sum_{k\ge0}
       h_k^2 E_{s,h_k}(u_\varepsilon)^2\\
 &\quad\le C_r(\|F_0\|^2+\|F_1\|^2)+C_{r,u}.
 \end{aligned}
 \tag{T97}
\]
Here $h_k=\varrho^{-k}$ is chosen by (T87) for a product patch where $q=1$. To prove the last line use the exact right Fourier products
$h S_h\mathcal A_\varepsilon J_y^{-(r-1)}$
and
$h^2 S_h\mathcal A_\varepsilon J_y^{-(r-2)}$.
Their normalized symbols and derivatives are uniformly bounded on the input annulus: the respective powers of $h$ cancel their frequency growth by (T66) and (T71). The second expression accounts for $d_x=hD_x$. Insert $\Pi$; its complement has all finite coefficients zero by the strict support margin and gives a summable weighted remainder by Section 28. For the retained term put an annular Fourier cutoff immediately to the right. The operator norms are uniformly bounded, and those input annuli overlap finitely many times. Plancherel proves the sum in (T97). This is the same proved summation mechanism as (T90), with the explicit powers changed from $h^{1/2},h^{3/2}$ to $h,h^2$.

Sum (T96), use (T97), and pass first each finite vector of outputs through $\varepsilon\to0$ by (T74). Then increase the number of bands. The nonnegative squared norms give the infinite-sum bound by monotone convergence. Apply (T88) to $z=J_y^ru$, taking $m\ge\max(r,0)$ for its fixed global lower norm. With $\mathcal B$ the fixed product cutoff constructed there, this yields
\[
 \begin{aligned}
 &\|\mathcal B J_y^ru\|^2
       +\|\mathcal B J_y^{r-1}D_xu\|^2\\
 &\qquad\le C_r(\|F_0\|^2+\|F_1\|^2)+C_{r,u}.
 \end{aligned}
 \tag{T98}
\]
The output cutoff is elliptic near the selected point and is fixed during the limit. The constant uses the spatial forcing and the fixed lower norm. There is no incoming-edge term in this elliptic estimate. In particular the full-order gain is obtained from the actual regularized equation with its commutator, not by treating that commutator as zero.

## 40. Closing this induction on one open elliptic set

All the supports in (T93) and (T97) can be chosen compactly inside the same open set $\mathcal O_+$. At each point choose nested base and angular neighborhoods, a sufficiently small radial interval, and an outer normal cutoff still inside that set. Positivity has a uniform lower bound on each resulting compact annular support. The outer normal transition remains inside $\mathcal O_+$ too; its commutator was included in (T95). Thus the support condition of Section 36 is now verified for this elliptic argument, with a full-order gain and no other regularity inputs.

The starting pair $J_y^2u,J_yD_xu$ is globally $L^2$ because $u\in H^2$. Suppose the order-$n$ pair is locally $L^2$ throughout $\mathcal O_+$. Cover the compact cosphere support of each $\Pi$ by finitely many previous-order regularity neighborhoods. The finite partition and elliptic inverse argument in Section 36 proves its two inputs in (T97), now with $r=n+1$. Equation (T98) gives the next pair near every point of $\mathcal O_+$. This proves the induction simultaneously on that open set. Consequently, for every fixed tangential cutoff $B$ of compact cosphere support in $\mathcal O_+$,
\[
 \begin{gathered}
 B J_y^n u\in L^2,\qquad
 B J_y^{n-1}D_xu\in L^2,\\
 n=2,3,4,\ldots .
 \end{gathered}
 \tag{T99}
\]
For each $n$ the finite cover may change, but $B$ and $\mathcal O_+$ do not. Intermediate real orders follow by choosing a larger integer order, inserting a cutoff equal to one near the support of $B$, and using the finite product formula with the Fourier multiplier of nonpositive order. Its remainder acts on the fixed global lower norm, as before. This proves exactly the tangential pair needed for (T89) on every compact subset of the elliptic region, up to and including the Dirichlet boundary.

This resolves the elliptic input only. A cutoff crossing $a_0=0$ is not covered by a positive lower bound, and (T99) supplies no assertion there. Sections 41–47 supply local separated-root reflection and interior propagation. Sections 48–50 supply the geometric connections and strict-diffraction weight supports. Sections 51–54 supply the finite-order transport and strict-diffraction induction. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. 

<a id="separated-normal-roots-and-reflection"></a>

## 41. The two normal flows away from glancing

We next prove local reflection at a hyperbolic boundary covector. Keep the fixed $H^2$ Dirichlet wave $u=\chi v$ of (T62). Thus $P_hu=f$, and the actual spatial-cutoff forcing is separated from every base support below. We use this fixed wave directly; no Sobolev regularizer is needed for the first-order energy argument in this section. Choose a boundary tangential covector with $a_0<0$. In a compact nonzero tangential annulus about it, and on a sufficiently short normal interval, set
\[
 \begin{gathered}
 k(x,y,\eta)=\sqrt{-a_0(x,y,\eta)},\\
 k\ge\kappa>0,\qquad p=s^2-k^2,\\
 s=\sigma k,\qquad \sigma\in\{+1,-1\},\\
 X_\sigma=\partial_x-H_{\sigma k}^{\rm tan}.
 \end{gathered}
 \tag{T100}
\]
The tangential Hamilton field has the same bracket convention as (T3). On $p=0$, divide $H_p$ by $H_px=2\sigma k$. The tangential position velocity is $-\sigma k_\eta$, and the tangential frequency velocity is $\sigma k_y$. These are exactly the velocities of $X_\sigma$. Its smooth flow exists by (G13), also for negative normal time. Thus each of the two full characteristic branches is the lift $s=\sigma k$ of one such tangential flow. At the wall the reflected pair has the same $(y,\eta)$ and opposite $s$. This is the separated-root part of the geometric relation already constructed in (G1)–(G23).

Take a small compact tangential patch $K$ at $x=0$. Shrink it and the interval $[0,\ell]$ so that both transported patches and slightly larger tubes stay inside the region in (T100), within the chosen annulus, and away from the spatial-cutoff forcing. This follows from continuity of the two flows on a compact interval. All subsequent support margins are fixed before $h$ tends to zero. Their constants need not remain bounded as $k$ tends to zero.

## 42. Finite roots of the actual operator

We give an operator construction which retains the lower-order terms and the exact Dirichlet coupling. Extend $k$ smoothly to a positive symbol on all tangential phase space, bounded below by a positive constant and equal to a constant $k_0$ outside a compact annular phase set. For example, interpolate by a smooth cutoff between $k$ and $k_0$ inside a larger region where the original $k$ is positive. On the entire normal interval, all derivatives of this extension are bounded. Extend the exact lower symbol of $R_h$ with another cutoff, equal to one on a neighborhood of both tubes. This gives
\[
 \widetilde R_h=\operatorname{Op}_h(-k^2+h\rho_1).
 \tag{T101}
\]
Here $\rho_1$ is compactly supported in the larger phase patch, has uniformly bounded derivatives, and includes every actual first-order and zero-order coefficient from (D4). It may depend on $h$. The exact left symbols of $\widetilde R_h$ and $R_h$ agree on a neighborhood of both tubes; the operators are not asserted equal globally.

For every integer $L\ge1$ we construct bounded tangential operators $B_+,B_-$ such that
\[
 \begin{gathered}
 B_\sigma=\operatorname{Op}_h(b_\sigma),\qquad
 b_\sigma=\sigma k+h c_\sigma,\\
 \mathcal E_\sigma
   =B_\sigma^2-ih\partial_xB_\sigma+\widetilde R_h,\\
 \|\partial_x^j\mathcal E_\sigma\|_{2\to2}
       \le C_{L,j}h^L,\\
 \|B_\sigma-B_\sigma^*\|_{2\to2}\le C_Lh.
 \end{gathered}
 \tag{T102}
\]
All fixed derivatives of $c_\sigma$ are bounded uniformly in $h$. Its finite coefficients have compact phase support; $B_\sigma$ equals the constant $\sigma k_0$ plus a quantized compact symbol. These operators are allowed to depend on the chosen finite accuracy $L$.

Here is the recursion and its remainder justification. Start with $b_{\sigma,0}=\sigma k$. The leading term in the Riccati expression is $k^2-k^2=0$, so its finite product expansion starts at order $h$. Suppose the remaining expression starts with $h^j e_j$, with $e_j$ having uniformly bounded derivatives. Add $h^j c_j$ to the root symbol, where
\[
 c_j=-\frac{e_j}{2\sigma k}.
 \tag{T103}
\]
The new term in the square at order $h^j$ is $2\sigma k c_j$; normal differentiation and every nonconstant product coefficient carry one further $h$. This cancels $e_j$. The positive lower bound on $k$ bounds every derivative of the quotient. Repeat for $j=1,\ldots,L-1$, taking one additional term if needed for the stated error. Only normal, position and frequency derivatives occur; no derivative or asymptotic expansion in $h$ of $\rho_1$ is required. At each stage divide the current finite symbol residual by its known power of $h$; its bounded coefficient may itself depend on $h$. Retain sufficiently many terms of every product for the final requested accuracy. The bounded operator remainder is kept separately and is never used as a compactly supported coefficient in the recursion.

The finite product proof (N19)–(N20) applies to each compact term and to its products with the constant parts. Its bounded-amplitude remainder gives the asserted $O(h^L)$ operator bound, including each normal derivative. Outside the compact phase set all constant terms cancel and the correction coefficients vanish. Thus this is a finite operator estimate, not an unestimated formal factorization. Finally, the principal symbol $\sigma k$ is real; the adjoint formula differs from its left quantization by $O(h)$, and the remaining symbol already has a factor $h$. This proves the last line of (T102).

Put $D_h=B_+-B_-$. The positive-packet estimate applied to its principal symbol $2k$, followed by its $O(h)$ lower term, gives
$\operatorname{Re}(D_hz,z)\ge\kappa_1\|z\|^2$
for a fixed $\kappa_1>0$ and small enough $h$. The same real-form inequality holds for $D_h^*$. Hence $D_h$ is injective with closed range, and the orthogonal complement of its range is $\ker D_h^*=0$. It is onto. Its exact inverse
\[
 E_h=D_h^{-1},\qquad \|E_h\|\le\kappa_1^{-1}
 \tag{T104}
\]
is uniformly bounded. The difference-quotient identity for inverses gives $\partial_xE_h=-E_h(\partial_xD_h)E_h$; iteration bounds every fixed normal derivative.

The inverse also has finite local symbol expansions to arbitrary accuracy. Start with $1/(2k)$ and cancel each finite product error by division by $2k$, as in (T44), now for $D_hE_{h,M}$. This yields $D_hE_{h,M}=I+O(h^M)$ in operator norm with all normal derivatives. Multiplication by the exact $E_h$ proves $E_h-E_{h,M}=O(h^M)$. The finite coefficients are a constant plus compact symbols. This supplies the local calculus for the exact inverse without identifying it with a merely formal inverse.

## 43. Mode equations and the exact boundary relation

Define two actual functions, for each fixed small $h$, by
\[
 \begin{gathered}
 V_+=E_h(d_xu-B_-u),\\
 V_-=u-V_+,\qquad u=V_++V_-,\\
 d_xu=B_+V_++B_-V_-,\\
 \sup_h(\|V_+\|+\|V_-\|)\le C_L\|u\|_{H^2}.
 \end{gathered}
 \tag{T105}
\]
These equalities are exact, by (T104). The modes have an $H^1$ normal representative with values in tangential $L^2$: $u\in H^2$, the operators and their normal derivatives are bounded, and $d_xu$ has one normal derivative in $L^2$. The norm-primitive proof (N24) therefore supplies their traces. Since $u(0)=0$,
\[
 V_-(0)=-V_+(0).
 \tag{T106}
\]
There is no lower-order error in this relation. In particular a boundary correction to a principal eigenvector is not being omitted.

To derive the equations let $F=f+(\widetilde R_h-R_h)u$, so that $(d_x^2+\widetilde R_h)u=F$. Differentiate the second equality in (T105), and use $d_xB=Bd_x-ihB'$. Solving the resulting two equations with $D_h^{-1}$ gives
\[
 \begin{aligned}
 (d_x-B_+)V_+&=E_h(F-\mathcal E_+V_+-\mathcal E_-V_-),\\
 (d_x-B_-)V_-&=-E_h(F-\mathcal E_+V_+-\mathcal E_-V_-).
 \end{aligned}
 \tag{T107}
\]
This derivation keeps the order of every operator product. The roots need not commute with each other.

For every compact tangential cutoff $A_h$ supported in the interior of either retained tube, and every prescribed power $M$, choose the root accuracy $L$ sufficiently large. Equations (T102), (T104) and (T105) bound the localized Riccati errors by $C h^M\|u\|_{H^2}$. The other two contributions in (T107) are also $O(h^M)$ in $L^2$ over the normal interval. We give the support argument because $F$ itself need not be small near unrelated frequencies.

Replace $E_h$ by a finite inverse $E_{h,J}$. For $A_hE_{h,J}(\widetilde R_h-R_h)$ every finite product coefficient vanishes: the last symbol and all its derivatives vanish near the supports of the first coefficients. The actual differential part is a polynomial of degree at most two; its cutoff products and tails have precisely the bounded-amplitude estimates (N19)–(N23). All remaining finite factors are compact symbols. Thus the remainder is arbitrarily small on $u\in H^2$. The replacement error $E_h-E_{h,J}$ acts on $(\widetilde R_h-R_h)u$, whose norm is bounded by $C\|u\|_{H^2}$, so it has the same conclusion. For $A_hE_{h,J}f$ use the separated-position calculation (T58), since the actual support of $f$ is separated from the tube's base support. Its inverse replacement error is controlled by (T62). The bounds hold for bounded families of such cutoffs, including the finitely corrected symbols constructed next. Consequently
\[
 \|A_h(d_x-B_\sigma)V_\sigma\|_{L^2_{x,y}}
       \le C_{M,u}h^M.
 \tag{T108}
\]
No equation has been applied to an extension across the Dirichlet boundary. The functions and equations so far live on the actual closed half collar. The unlocalized right sides of (T107) also have a uniform $L^2$ bound depending on $\|u\|_{H^2}$, since $R_hu$, $\widetilde R_hu$ and $f$ do. This global bound controls the off-support operator remainders in the interior localization below.

## 44. Transported cutoffs and scalar energy

Choose a compact symbol $q_0(y,\eta)$ on the boundary patch, equal to one on a smaller patch. Let $q_{\sigma,0}(x)$ solve $X_\sigma q_{\sigma,0}=0$ with this initial value, by composition with the inverse flow. For any prescribed $J$, its finite correction gives operators $Q_\sigma(x)$ satisfying
\[
 \begin{gathered}
 Q_\sigma(0)=\operatorname{Op}_h(q_0),\\
 Q_\sigma=\operatorname{Op}_h\left(
       q_{\sigma,0}+\sum_{j=1}^{J}h^j q_{\sigma,j}\right),\\
 -ihQ_\sigma'+[Q_\sigma,B_\sigma]=O(h^{J+1}).
 \end{gathered}
 \tag{T109}
\]
The last equality is in operator norm. All fixed derivatives are bounded. Every correction has zero initial value and support inside the transported support of $q_0$. On the transported open set where $q_0$ is identically one, every correction is zero.

Indeed, the first commutator coefficient is
$-ih(\partial_x-H_{\sigma k}^{\rm tan})q_{\sigma,0}$,
with this sign because $[Q,B]$ has leading symbol $(h/i)\{q,\sigma k\}$. At a later step the uncancelled coefficient is a known smooth function. Solve the inhomogeneous equation for $q_{\sigma,j}$ along $X_\sigma$, with zero initial value, by integrating that function along the flow, including the required scalar factor $i$. Differentiation under the integral proves all bounds. The source vanishes on any transported neighborhood where all previous symbols are constant, because the commutator with the identity and its normal derivative are zero. It also vanishes outside their transported supports. Uniqueness of the scalar integral equation proves both support claims. The finite product remainder proves the last line of (T109). The construction uses the actual lower coefficients of $B_\sigma$; keeping only the principal transport would leave an unaccounted $h^2$ error.

Set $Z_\sigma=Q_\sigma V_\sigma$. Equations (T108)–(T109) give $(d_x-B_\sigma)Z_\sigma=g_\sigma$, with $\|g_\sigma\|_{L^2_{x,y}}\le C_{M,u}h^M$, by choosing both finite accuracies sufficiently large. For any $z$ satisfying $(d_x-B_\sigma)z=g$ and having a norm-primitive representative, (T102) implies
\[
 \begin{aligned}
 &\|z(x)\|\le e^{C_L\ell}\|z(x_0)\|\\
 &\qquad+e^{C_L\ell}h^{-1}
       \int_{\min(x,x_0)}^{\max(x,x_0)}\|g(t)\|\,dt.
 \end{aligned}
 \tag{T110}
\]
To verify it, write $\partial_xz=(i/h)(B_\sigma z+g)$. Differentiating the squared norm bounds its absolute derivative by $C_L\|z\|^2+(2/h)\|g\|\|z\|$, because the imaginary part of $(B_\sigma z,z)$ is bounded by half the norm of $B_\sigma-B_\sigma^*$. Apply this inequality to $(\|z\|^2+\delta^2)^{1/2}$, multiply by the integrating factor, integrate in either direction, and let $\delta\downarrow0$. The norm-primitive approximation justifies the same formula for the displayed weak inputs. Cauchy–Schwarz bounds the forcing integral by $\ell^{1/2}\|g\|_{L^2}$.

This estimate has no factor $e^{C/h}$. The real principal symbol of $B_\sigma$ is the reason its skew-adjoint part has the necessary factor $h$. It will carry regularity from an interior slice to the boundary and back along the other mode.

## 45. Identifying the mode on a smooth interior leg

We must connect an interior wavefront hypothesis on $u$ to the mode in (T110). Let $I\Subset(0,\ell)$ be a closed interval with nonempty interior. Suppose $u$ is microlocally smooth on an open full-phase neighborhood of the lift $s=\sigma k$ of the closed transported support of $q_0$ over a slightly larger interval. Choose all tube margins inside that open neighborhood at this branch. Then, for every $M$, the root and transport accuracies can be chosen so that
\[
 \|Q_\sigma V_\sigma\|_{L^2(I\times\mathbb R^d)}
          \le C_{M,u}h^M.
 \tag{T111}
\]
The hypothesis concerns only this branch; no regularity of the opposite root is assumed.

Here is the frequency separation argument. Insert a normal cutoff equal to one near $I$, compactly supported in the slightly larger interior interval, and work there in the full variables $(x,y)$. Choose a smooth full-phase factor $\gamma$ equal to one near $s=\sigma k$ over the relevant compact tangential support, supported in the prescribed smooth region, and zero for sufficiently large $|s|$. For any of the finitely many tangential coefficients of $Q_\sigma$, its portion multiplied by $\gamma$ is compact in all frequencies. Substitute (T105) and a finite expansion of $E_h$. Finite products with $d_x$ and $B_-$ express that portion of the mode as a finite sum of full-phase operators on $u$, supported in the same smooth region, plus $O(h^M)\|u\|_{H^2}$. The $d_x$ factor is harmless on this compact normal-frequency set; its exact product is retained. Formula (T16), including its proof for bounded symbol families, makes each retained term rapidly small. The exact-inverse replacement is small by (T104) and the bounded norm of $d_xu-B_-u$.

On the complementary part divide the leading full symbol by $s-\sigma k$. This denominator is bounded away from zero at bounded $s$ on that support, and grows like $|s|$ at infinity. The first quotient has normal-frequency decay $\langle s\rangle^{-1}$, is compact in tangential frequency and base variables, and has bounded derivatives. Cancel successive errors in its product with $d_x-B_\sigma$ by division by the same denominator. A normal-root cutoff with slightly larger support retains the separation. This constructs a finite left parametrix for the complementary portion, to arbitrary operator-norm accuracy.

For clarity, the norm and tail assertions in this last calculation have the same direct justification as (T37)–(T38). Composition with $d_x$ is an exact finite differentiation. Composition with $B_\sigma$ uses Taylor's formula in its input base variables. Tangential coefficients obey (N20); each normal Taylor term is transferred to a normal-frequency derivative of the quotient, which improves its inverse-power tail. The integral remainders have bounded derivatives and that tail, so the full bounded-amplitude lemma bounds them uniformly. At each finite step the remaining leading error is divided by $s-\sigma k$, retaining these properties. Thus the final remainder is $O(h^M)$ on $L^2$, with all cutoffs fixed. This argument requires no isotropic order-minus-one assertion in the combined frequencies.

Apply this parametrix to the actual localized residual in (T108), with a larger tangential cutoff equal to one near its symbol support. Products with its complement have every finite coefficient zero and arbitrary-order remainders. The inserted outer normal cutoff contributes $-ih\theta' V_\sigma$. Its support is separated in $x$ from the retained interval; the parametrix kernel there is arbitrarily small by repeated normal-frequency integration, using the just-proved derivative decay. This term is bounded by the global $L^2$ bound (T105). The same argument handles every outer normal transition in the finite inverse. We use the equation only after this interior localization, never for the zero extension at the wall.

Combining the root portion and its complement proves (T111). This also proves a useful related fact: on either interior tube, the mode has no wavefront away from its own normal root, to every finite accuracy required, by the same complementary parametrix. This is a consequence of (T108), not an assumption that an algebraic principal projection automatically separates all wavefronts.

## 46. Local reflection and a fixed boundary neighborhood

Apply (T111) to one sign, say $\sigma=+1$. Averaging over $I$ supplies, for each $h$, a slice $x_h\in I$ at which $\|Z_+(x_h)\|$ is bounded by $|I|^{-1/2}\|Z_+\|_{L^2(I)}$. Use (T110) from that slice to zero. The factor $h^{-1}$ costs one power in the residual; the chosen accuracies are arbitrary, so the boundary norm is still $O(h^M)$ for every requested $M$. By (T106) and the equal initial cutoffs in (T109), $Z_-(0)=-Z_+(0)$ exactly. Apply (T110) forward to both modes. This gives
\[
 \begin{gathered}
 \sup_{0\le x\le\ell}\|Q_\sigma(x)V_\sigma(x)\|
           \le C_{M,u}h^M,\\
 \sigma=+1,-1.
 \end{gathered}
 \tag{T112}
\]
The bound holds for every requested $M$, with sufficiently accurate finite roots and cutoffs. The same proof with the signs interchanged starts from the other interior leg. The averaging point need not be fixed: the constant in (T110) is uniform for all points of this fixed interval.

The conclusion for the wave itself uses cutoffs independent of the chosen accuracy. On smaller transported tubes, $q_{\sigma,0}=1$ and every correction in (T109) vanishes. A fixed inner cutoff therefore factors through $Q_\sigma$ modulo any requested power of $h$, by the finite product proof and (T105). Near the boundary the two smaller transported tubes have a common open tangential neighborhood, fixed by continuity of the two flows from the same initial patch. Choose a fixed compact cutoff $A_h$ inside it. Equations (T105), (T112) and the finite products with $B_\sigma$ give rapid bounds for $A_hu$ and $A_hd_xu$. For the latter product insert a slightly larger inner cutoff before $B_\sigma$; its complement has zero finite coefficients by the support margin. All inverse and root replacement errors remain arbitrary-order errors on the fixed $H^2$ input.

The frequency reconstruction (T87)–(T88) now supplies the boundary regularity pair at every real order on any fixed smaller conic tangential neighborhood. More explicitly, a band of $B J_y^r$ has norm $O(h^{-r})$ and a band of $B J_y^{r-1}D_x$ has the same factor relative to $d_xu$. Their finite factorization through $A_h$, their output tails and their finite-overlap synthesis are proved exactly as in Section 34. Choose the rapid exponent larger than $|r|+2$ and the finite remainder order large enough; the geometric sums converge. Thus $B J_y^ru$ and $B J_y^{r-1}D_xu$ belong to $L^2$ for one fixed $B$ at every real $r$.

In the interior part of the outgoing tube, (T112) removes the outgoing mode's wavefront. The opposite mode is elliptic at that full normal root, by the complementary parametrix of Section 45. Since $u=V_++V_-$, the actual wave is microlocally smooth there. The passage from rapid full-phase annular bounds to wavefront regularity is the Fourier-band proof of Section 34 applied to all interior variables, after compact interior localization; no extension across the boundary is involved. This proves local reflection from a smooth incoming full-phase leg, the corresponding outgoing leg, and the tangential boundary pair between them.

This local theorem is valid wherever the two roots stay separated. It does not assert constants uniform at glancing. To use it in the strict-diffraction argument, the incoming leg of each relevant hyperbolic tube must be connected to the prescribed regular region by interior propagation. Section 47 supplies that interior theorem for the actual wave. Sections 48–50 below prove the geometric containment and larger-weight support region through $a_0=0$. Sections 51–54 prove the finite-order transport and simultaneous strict-diffraction induction. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38. The general geometric relation and full theorem scope have not been narrowed to this local case.

## 47. Interior propagation for the actual wave

The same mode argument supplies the interior input, after checking its coordinate and operator hypotheses. In an interior spacetime chart write the principal symbol of the scalar wave, up to its overall sign, as $\tau^2-r(z,\zeta)$, where $t$ is physical time, $z$ is the spatial coordinate, and $r$ is the positive definite quadratic metric symbol. All arbitrary smooth self-adjoint lower terms are retained. On a compact nonzero characteristic patch,
\[
 \begin{gathered}
 p_{\rm time}=\tau^2-r(z,\zeta),\\
 \tau=\sigma k_{\rm time},\qquad
 k_{\rm time}=\sqrt{r(z,\zeta)}>0,\\
 Y_\sigma=\partial_t-H_{\sigma k_{\rm time}}^{\rm space}.
 \end{gathered}
 \tag{T113}
\]
Indeed, a nonzero characteristic covector cannot have $\zeta=0$ or $\tau=0$, because the metric is positive definite. On a sufficiently small annular spatial patch, $k_{\rm time}$ therefore has a fixed positive lower bound. Dividing the Hamilton field by its time component $2\tau$ gives exactly $Y_\sigma$, as in (T100). Multiplying the original wave operator by minus one only reverses its Hamilton parameter; it does not change the characteristic curves or the differential equation's solutions.

Use physical time as the distinguished variable in (D1)–(D4). The absence of mixed principal time-space derivatives and the constant time-leading coefficient give the same decomposition into a symmetrized real first derivative and a self-adjoint tangential operator. Completing that square and multiplying by the explicitly integrated unit-modulus gauge removes the single time derivative. Thus, on this chart, the actual equation becomes $((hD_t)^2+R_{h,\rm time}(t))\widetilde v=0$, with tangential principal symbol $-r$ and all remaining lower terms included in its exact left symbol. No boundary condition is imposed on a time slice. The gauge and its inverse are smooth, so they preserve $H^2$ locally and preserve the absence of wavefront points, by the Fourier cutoff proof in the phase reading.

Choose a compact spacetime cutoff equal to one on slightly larger tubes around a short interior characteristic segment. The localized wave $\widetilde u$ lies in $H^2$, and its equation forcing is separated from those tubes with the same bound as (T62). Extend the coefficients and construct finite roots, exact modes and inverses by Sections 42–43, now with $x=t$ and $y=z$. Everything through (T105), (T107)–(T111) uses the actual equation and its local supports; none of it needs the Dirichlet relation (T106). The modes have the required traces on interior time slices by their norm-primitive representatives.

If the wave is microlocally smooth near one point of the retained characteristic segment, shrink the initial phase patch and choose a small interior time interval about that point so that its own root lift lies inside this open regular region. Section 45 then gives a rapidly small norm for that mode on the time interval, without an assumption about the opposite mode. Average to one time slice and apply (T110) to the same mode in both time directions. On every smaller transported tube its norm is rapidly small to arbitrary accuracy. At that mode's full normal root, the other mode is elliptic, so the complementary parametrix from Section 45 makes its contribution rapidly small too. Their exact sum is $\widetilde u$. The fixed-cutoff Fourier reconstruction in Section 46 proves absence of wavefront throughout that short segment, including a neighborhood of each point. Undoing the smooth gauge gives the same assertion for the original wave.

Consequently, for a fixed $H^2$ homogeneous wave $v$ and a compact characteristic segment $\Gamma$ lying wholly in the interior,
\[
 \begin{gathered}
 \Gamma\cap\operatorname{WF}(v)=\varnothing
 \quad\text{or}\quad
 \Gamma\subset\operatorname{WF}(v).
 \end{gathered}
 \tag{T114}
\]
To pass from the local assertion to a compact segment, cover its image by finitely many smaller phase boxes of the type just proved. The time component never vanishes, so physical time is a valid parameter on each box. Compactness gives a finite partition of the parameter interval into subintervals each lying in one such box: take a finite subcover of the inverse-image open intervals and a mesh shorter than its positive covering radius. Starting from any regular point, apply the two-direction local assertion successively along those subintervals. Regularity reaches both endpoints of the whole segment. If any other point were singular, this would contradict the same local conclusion there. This proves the dichotomy. It is an interior statement for the actual wave operator, not an invocation of the fixed closed-manifold evolution theorem under different hypotheses.

Sections 37–47 now provide elliptic boundary regularity, local separated-root reflection and interior propagation for the fixed $H^2$ wave supplied by (W9)–(W11). Sections 48–50 below establish the actual connecting segments and a fixed open region containing the entire larger-weight supports in (T89). Sections 51–54 transport the newly gained finite order along the outgoing tangency arcs, close one simultaneous fixed-neighborhood induction and recover normal smoothness. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38.

<a id="two-root-diffraction-supports"></a>

## 48. A region that controls both normal lifts

The divided weights in (T11) are tangential symbols. Their support must therefore be checked at both real normal roots, even when the original full-phase cutoff lies mainly on one leg. We now construct an open region in which the required geometric connections are explicit. This construction supplies the support part of the induction; it does not yet supply its preceding-order Sobolev bounds.

Keep the fixed homogeneous wave and a strict-diffraction chart on which $c=-\partial_xa_0>0$. The principal symbol is stationary in physical time. Its time covector $\tau$ is conserved by the Hamilton flow and by reflection. It is nonzero at every nonzero characteristic covector, by positive definiteness of the spatial metric. We may consequently normalize by $\lambda=|\tau|$ and work on either section $\tau/|\tau|=1$ or $-1$. In this paragraph $s,\eta,a_0,c$ denote their normalized versions. Dividing the Hamilton field by $c$ still gives
\[
 \frac{dx}{ds}=\frac{2s}{c},\qquad
 0<\kappa\le c\le K.
 \tag{T115}
\]
Indeed $s_{\rm old}=\lambda s$ and $c_{\rm old}=\lambda^2c$, with constant $\lambda$ along each trajectory, so the change of variable in (T3) gives exactly this formula. Positive scaling restores the conic region at the end. No homogeneity of the compact semiclassical weight itself is asserted.

First suppose the prescribed smooth leg has negative $s$. By (T114) move its known regular point along the negative reference leg to a sufficiently small value $-s_0<0$. Choose an open characteristic section $\Gamma_0$ about that point in $\{s=-s_0,\ p=0\}$, entirely in the interior regular region. Choose a larger open full-phase chart $\mathcal B$, on which (T115) holds, containing the reference segment from $-s_0$ to a small positive value and its boundary contact. All its base points needed below lie in the region where the fixed spatial cutoff equals one, so the actual wave equation is homogeneous there. The section and trajectory have strict margins in this chart.

Choose an open tangential chart $O$ containing the projected reference segment, including its incoming section point. Restrict the starting points to $O_* = O\cap\{|a_0|<s_0^2/4\}$, so their real roots have magnitude less than $s_0/2$. The paths themselves are allowed over all of $O$. Smooth flow and the margins just chosen ensure that the extended trajectories below exist: flow from either starting lift to $s=0$ and backwards to $-s_0$, and flow backwards from the reflected states that occur below. Here is an order of choices that ensures this simultaneous existence. Take a compact product box inside a larger coefficient-extension box where $c>0$; the flow has one positive existence time on that compact box by (G13). Take $s_0$ smaller than a fixed fraction of that time, then take $O$ sufficiently small within the product box while retaining the projected reference segment. Starting roots and reflected roots have magnitude less than $s_0/2$, so every required flow interval has length at most $3s_0/2$ and remains in the larger box. The smooth extension across $x=0$ is used only to construct the trajectories; the wave equation will only be used on physical segments with $x\ge0$.

For a characteristic lift $q=(x,y,s,\eta)$ with $x\ge0$, define a backwards path to the section as follows. If $s\le0$, decrease $s$ to $-s_0$. Formula (T115) shows that $x$ increases backwards, so there is no boundary encounter except a possible starting contact. If $s>0$, let $m$ be the normal coordinate of its extended trajectory at $s=0$.

If $m\ge0$, the trajectory remains in $x\ge0$ while passing through $s=0$ and continuing to $-s_0$. It touches the boundary precisely when $m=0$. If $m<0$, there is a unique $b\in(0,s]$ at which the backwards trajectory reaches $x=0$: on $[0,s]$ the function $x$ is strictly increasing, and its endpoint values bracket zero. At that point reflect the normal covector from $b$ to $-b$, keeping the base point and tangential covector unchanged, and continue backwards from $-b$ to $-s_0$. The reflected state is characteristic because $p=s^2+a_0$. Its negative leg moves strictly into $x>0$. Thus there is at most one reflection. For an initial outward lift at $x=0$ this reflection is immediate.

The hitting parameter tends to zero continuously at a tangency. More precisely, on the outgoing extended trajectory,
\[
 \begin{gathered}
 -m=\int_0^b\frac{2u}{c(u)}\,du,\qquad
 \frac{b^2}{K}\le -m\le\frac{b^2}{\kappa},\\
 b\le\sqrt{K|m|}\longrightarrow0
 \quad\text{as }m\uparrow0.
 \end{gathered}
 \tag{T116}
\]
Here $c(u)$ is evaluated on that particular extended trajectory. At a transverse hit $b>0$, the derivative $2b/c$ is nonzero, so the inverse theorem makes the hit and reflected state smooth functions of the initial point. At $m=0$, (T116) and continuity of the flow show that both the hit and the reflected state converge to the same zero-normal-covector state. Their subsequent backwards flow to $-s_0$ converges to the unbroken negative leg. The small omitted pieces have $s$-length tending to zero and images tending to the contact. Thus the endpoint map is continuous through tangency, and the union of the two compact physical arcs is continuous in Hausdorff distance. The same conclusion holds at an initial contact and as the two starting roots merge: at $s=0$, $x\ge0$ and the positive and negative constructions converge to the same backwards path. Reflection has two covector endpoints at a transverse hit; we regard both as part of the compact path. We do not interpolate between them by a fictitious vertical characteristic segment.

Let $W_0$ be the subset of $O_*$ defined as follows. Points with $a_0>0$ are included. For $a_0\le0$, require that the backwards paths from **both** lifts $s=\pm\sqrt{-a_0}$ stay in $\mathcal B$, have their entire tangential projections in $O$, and have endpoints in $\Gamma_0$. Each path is compact, so both open containments have positive margins. The two roots, their endpoint maps and their compact paths are continuous by the preceding argument. Since $\Gamma_0$ is relatively open in the section, these conditions persist in a neighborhood of each allowed point. At $a_0=0$ the two paths coincide; the same continuity proves the condition for both roots at nearby points with $a_0<0$, while points with $a_0>0$ are already included. Consequently $W_0$ is relatively open in the physical tangential phase space. It contains the projected reference contact. Scaling the normalized construction by positive $\lambda$ makes $W_0$ conic, because the normalized flow, the reflection and all defining conditions are unchanged by this scaling.

There is a useful closure property. If a path from a lift over $W_0$ has a tangency $g$, its backwards subpath from $g$ to $\Gamma_0$ stays in $\mathcal B$ and projects into $O$. Also $\pi g\in O_*$ because $a_0(g)=0$. At $g$ the two normal lifts coincide. Hence $\pi g$ itself belongs to $W_0$. The outgoing segment from $g$ to the original point stays in $\mathcal B$ and projects into $O$; we do **not** need, or assert, that its projection stays in $W_0$, since the condition on its other normal lift may fail along that segment. Keeping $O$ distinct from the smaller allowed-starting region $O_*$ is essential to this argument.

The opposite orientation follows without a new geometric assumption. Use $\widetilde s=-s$ and the reversed Hamilton field $-H_p$. Then $(-H_p)\widetilde s=c$ and $dx/d\widetilde s=2\widetilde s/c$, so the entire argument applies with the prescribed positive leg as its negative leg in these coordinates. Both directions in (T114) and the two starting signs in Section 46 have already been proved.

## 49. Which legs are already regular

Let $\mathcal G$ consist of the characteristic contacts in this chart with $x=s=a_0=0$. Every such contact is strictly diffractive, since $c>0$. We use the negative-leg orientation of Section 48. At an interior lift over $W_0$ with $s<0$, its entire backwards path to $\Gamma_0$ lies in the interior. Formula (T114) therefore makes that lift regular, on an open full-phase neighborhood.

For a positive lift, there are three possibilities. If its backwards path has no boundary contact, (T114) again applies. If it has a transverse reflection, the negative leg reaches $\Gamma_0$ through the interior. A compact part of that negative leg is consequently regular. Since the root at the reflection has $b>0$, Section 46 applies on a sufficiently small neighborhood of that reflection and supplies a regular positive leg. Formula (T114) carries regularity from that leg to the original point. Only a backwards path with a tangency remains. By Section 48 that tangency lies over $W_0$. An interior point with $s=0$ has $m=x>0$; its backwards path is wholly interior and is regular too. Write $\mathcal S_{W_0}$ for the interior characteristic wavefront points of $v$ whose tangential projections belong to $W_0$, and $\mathcal F_+(E)$ for the positive outgoing arcs from contacts in $E$. We have proved the precise containment
\[
 \mathcal S_{W_0}\subset
 \mathcal F_+\bigl(\mathcal G\cap\pi^{-1}(W_0)\bigr).
 \tag{T117}
\]
The arcs on the right are the actual physical trajectories in $\mathcal B$ from the construction, with $s>0$ after the contact. This is an upper bound on possible singularities, not a claim that those arcs are singular. Noncharacteristic interior points are regular as well: on a compact full-phase patch where $p\ne0$, division by $p$ and the finite product construction give a left parametrix to arbitrary order. Apply it to an interior localization of the actual homogeneous equation; separated cutoff errors have the rapid bounds of Section 4. The fixed $H^2$ norm controls the finite remainders. This proves the usual elliptic exclusion here without importing a propagation statement.

At a boundary point of $W_0$ with $a_0<0$, the same regular negative leg and Section 46 give the tangential boundary pair at all orders. At a boundary point with $a_0>0$, Section 40 gives that pair. These are open local conclusions at each such point; their constants need not be uniform as $a_0$ tends to zero. On a compact interior negative-root tube separated from $a_0=0$, the now-established full-phase regularity also satisfies the hypothesis of (T111), so its negative mode is rapidly small to every required accuracy. No regularity of the positive mode was used to prove this fact.

We have not inferred all-order tangential regularity from regularity of only one normal lift. In particular, an outgoing tangency arc on the right of (T117) may contribute to a tangential cutoff whose negative lift is already regular. This is exactly the distinction needed when using (T89).

## 50. Placing the entire larger weight inside this region

Fix a contact $g\in\mathcal G$ with $\pi g\in W_0$, and fix a finite desired Sobolev order. Choose a small full-phase box about $g$ whose physical tangential projection has compact closure in $W_0$ on the frequency annulus. This is possible by the openness just proved. The backwards negative leg of $g$ reaches $\Gamma_0$. Every compact negative subsegment near $g$ is regular by (T114). Choose the new parameter $\sigma$ so small that the full reference segment $|s|\le2\sigma$, together with the slightly larger box required by Section 12, remains in the preselected box. Take $\mathcal U_g$ to be a regular interior neighborhood of its compact negative leg $-2\sigma\le s\le-\sigma$.

Now perform (T5)–(T13) with this $g$, this $\sigma$ and this actual $\mathcal U_g$: choose the invariant radius, then $\delta$, then a sufficiently small positive shift. Use the larger normal cutoff and shifted weight of (T41)–(T48) inside the same preselected box. This ordering of choices confines the **whole** projected real-root support of each larger weight to $W_0$, not merely the support of its differentiated principal error. The compact neighborhoods for the smooth elliptic extensions in Sections 12–13 can also be chosen inside $W_0$, since their real-root supports already have a strict margin there. Their flat extension and majorant constructions are local; multiplication by a cutoff equal to one near the required compact set confines the extension to that chosen neighborhood, as proved there. Thus for both shifted multipliers and every larger tangential weight $s_{+,i}$ occurring in (T89),
\[
 \begin{gathered}
 \operatorname{supp}s_{+,i}\Subset W_0,\\
 \operatorname{supp}e_i\Subset\mathcal U_g.
 \end{gathered}
 \tag{T118}
\]
All these inclusions concern the physical half-space and have strict margins. The first also includes normal transitions of the larger weights and the elliptic extensions. Scaling restores the corresponding conic support inclusions. Each desired finite order permits its own auxiliary sizes and constants, while the containing open region $W_0$ is fixed once and for all in Section 48.

The compactness in (T118) supplies a tangential cutoff $\Pi$ equal to one near the entire input support and supported in $W_0$. If the preceding-order pair in (T89) has been established locally everywhere in $W_0$, a finite cover of this compact support and the finite cutoff factorization from Section 36 give exactly the two input norms required there. The incoming-edge term is already rapidly small, by (T16) on $\mathcal U_g$. Equations (T83)–(T92) then give the next half-order pair on a neighborhood of $g$.

This proves the geometric support condition for the actual divided weights. Section 51 transports the finite order gained near a tangency along its outgoing arc, using the actual modes and a weighted frequency sum. Section 52 supplies the full normal-frequency tails on regular interior patches. Sections 53–54 then close the simultaneous induction on the fixed $W_0$ and recover all normal derivatives from the homogeneous equation. The all-order statement (T114) alone would not replace those finite-order steps. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38.

<a id="finite-order-diffraction-induction"></a>

## 51. Transporting a finite Sobolev order along an outgoing arc

We first supply the finite-order input left open after (T118). Fix a compact positive-root characteristic arc in the interior homogeneous chart. Its normal coordinate increases strictly, and suppose $k=\sqrt{-a_0}$ has a positive lower bound on a slightly larger tube. Use $x$ as parameter on a closed interval $[a,b]\Subset(0,\infty)$. Choose a smaller closed interval $I\subset(a,b)$ with nonempty interior near the starting end. The constants below may depend on the tube and its distance from glancing.

Construct the finite roots $B_\pm$, their exact difference inverse $E_h$, and the actual modes $V_\pm$ by (T101)–(T108). Choose the extensions to agree with the actual equation on the larger tube and on the small additional target neighborhoods used below. Construct $Q_+$ by (T109), now with its initial slice at $x=a$. That construction only integrates a transport equation from its initial slice; it imposes no physical boundary condition. Take its leading symbol equal to one on a smaller transported tube. Every correction vanishes on that smaller tube. All supports and margins are fixed before the finite accuracy is increased.

Let $r$ be any fixed real number. Suppose an order-zero tangential cutoff $\Pi$ equals one near the conic hull of the transported cutoff supports over $I$, with a strict margin, and suppose the actual seed pair is finite:
\[
 \begin{gathered}
 F_0=\Pi J_y^r u\in L^2(I\times\mathbb R^d),\\
 F_1=\Pi J_y^{r-1}D_xu\in L^2(I\times\mathbb R^d),\\
 N_r=\|F_0\|^2+\|F_1\|^2+\|u\|_{H^2}^2.
 \end{gathered}
 \tag{T119}
\]
The last norm is on the fixed localization region used for the actual wave. No improved norm outside the seed region is assumed.

Put $Z_+=Q_+V_+$. The finite expansion of $E_h$ in (T104), followed by the exact mode formula (T105), writes $Z_+$ over $I$ as $C_{0,h}u+hC_{1,h}D_xu$ plus a remainder of arbitrary power of $h$ on the fixed $H^2$ input. Each $C_{j,h}$ is a finite sum of tangential symbols with uniform derivatives and compact support in a fixed annulus. Its finite coefficients have the same seed support margins. The bounded, possibly noncompact remainder of an exact product is kept in the arbitrary-order error rather than assigned a fictitious symbol support.

The normalized operators $h^{-r}C_{0,h}J_y^{-r}$ and $h^{1-r}C_{1,h}J_y^{1-r}$ are uniformly bounded. To see this directly, a Fourier multiplier on the right multiplies the left symbol exactly. On $\eta=h\xi$ in the fixed annulus, the two normalized Fourier factors are $(h^2+|\eta|^2)^{-r/2}$ and $(h^2+|\eta|^2)^{(1-r)/2}$. Their derivatives are uniformly bounded there. Insert $\Pi$ before each weighted input. Every finite coefficient from its complement vanishes by the support margin. The weighted remainder proof of Section 28 bounds what remains on $J_y^{-m}J_y^ru$ and $J_y^{-m}J_y^{r-1}D_xu$, for a fixed sufficiently large $m$; both are controlled by the fixed $H^2$ norm. Taking enough finite terms makes these errors any desired power of $h$ after normalization.

Choose the geometric frequency sequence of (T87), with a ratio small enough for the inner output annulus. For the seed terms, insert a Fourier annulus equal to one on the exact input support of each finite coefficient. The enlarged seed annuli may be wider than the output annulus, but still have finite overlap independent of the frequency index. Uniform boundedness, pointwise finite overlap and Plancherel therefore give
\[
 \sum_{k\ge k_0}h_k^{-2r}
       \|Z_{+,h_k}\|_{L^2(I\times\mathbb R^d)}^2
       \le C_rN_r.
 \tag{T120}
\]
The arbitrary-order errors are summable after choosing their order greater than $r$. The finitely many omitted low frequencies have bounded weighted norms on the fixed input. This is a bound for a frequency sum of the actual modes, not just a separate finite norm at each $h$.

Choose the root and transport accuracies so that $(d_x-B_+)Z_+=g_h$ on $[a,b]$ with $\|g_h\|_{L^2}\le C h^M\|u\|_{H^2}$ and $M>r+2$. This follows from (T108)–(T109); the equation is homogeneous on the tube, and its localization errors are separated. For each $h$, average the seed norm over $I$ to select a slice $x_h\in I$. Formula (T110) is uniform in this choice. Square it, use Cauchy–Schwarz on the forcing integral, and sum after multiplication by $h^{-2r}$. The forcing contributes at most a constant times $\sum_k h_k^{2(M-r-1)}\|u\|_{H^2}^2$, which converges. We obtain
\[
 \sum_{k\ge k_0}h_k^{-2r}
    \sup_{a\le x\le b}\|Z_{+,h_k}(x)\|_{L_y^2}^2
       \le C_rN_r.
 \tag{T121}
\]
The one-power loss in (T110) has thus been included. Increasing the finite accuracy does not change the geometric inner tube, because all transported corrections vanish there.

Suppose now that the negative full normal lift at a target point of this arc is regular. Choose a small target neighborhood where its negative lift remains regular, and a short negative-root tube inside that neighborhood. The same root extensions may be used there. Formula (T111), with sufficiently high finite accuracy, makes the localized negative mode rapidly small. It does not require the positive lift to be regular. Take a fixed tangential annular cutoff $A_h$ inside both the positive inner tube and this target neighborhood. Since $Q_+$ equals the identity there to every required finite order, the finite product formula gives $A_hV_+=A_hQ_+V_++O(h^L)$ on the uniformly bounded modes. For $A_hB_+V_+$ insert a slightly larger inner cutoff before $B_+$ and use the same finite product argument. The negative terms are rapidly small on the target patch. The exact identities $u=V_++V_-$ and $d_xu=B_+V_++B_-V_-$ consequently show that the sum of $h_k^{-2r}(\|A_{h_k}u\|^2+\|A_{h_k}d_xu\|^2)$ is finite there.

To reconstruct the actual Fourier-weighted pair, use the band cutoffs $\mathcal B_k$ from Section 34 inside this fixed target neighborhood. Finite factorization of $\mathcal B_kJ_y^r$ through $A_{h_k}$ has operator norm at most $C_rh_k^{-r}$ and an arbitrary-order remainder on the fixed lower norm. For $\mathcal B_kJ_y^{r-1}D_xu$ the corresponding factor is $h_k^{1-r}D_x=h_k^{-r}d_x$. The Fourier-kernel tail proof of (T88) confines the normalized outputs to enlarged annuli, up to summable tails; finite overlap then sums them in $L^2$. It yields one fixed cutoff $\mathcal B$, elliptic at the target, for which
\[
 \begin{gathered}
 \mathcal B J_y^r u\in L^2,\qquad
 \mathcal B J_y^{r-1}D_xu\in L^2,\\
 \begin{aligned}
 &\|\mathcal B J_y^r u\|^2+
 \|\mathcal B J_y^{r-1}D_xu\|^2\\
 &\qquad\le C_rN_r+C_{u,\mathrm{reg}}.
 \end{aligned}
 \end{gathered}
 \tag{T122}
\]
Here $C_{u,\mathrm{reg}}$ uses only finitely many seminorms from the already regular negative lift. This transports the given order $r$ without a derivative gain or an assumption of smooth positive-root data. The identical proof applies to the other orientation after the reversal described in Section 48.

## 52. The interior pair when every characteristic lift is regular

We also need to pass from full-phase regularity of all characteristic lifts to the tangential pair on an interior patch, including points where the normal roots merge in the interior. Let $K$ be a compact tangential annular patch in $x>0$, and suppose every real characteristic lift over a neighborhood of $K$ is regular. Such a patch exists about any point where all its characteristic lifts are regular: the two root maps are continuous, including at a merging root, and their finite compact set of lifts has an open regular neighborhood. Noncharacteristic points are regular by the finite parametrix proved after (T117).

Let $A_h$ have support in a smaller patch. Localize the actual wave by an interior base cutoff $\theta$ equal to one near this support, retaining strict margins. The localized equation has forcing separated from that support. Choose a scalar normal-frequency cutoff $\gamma(s)$ equal to one on a bounded interval containing every real root over the larger patch, and zero outside a larger interval. The full symbol $A_h(x,y,\eta)\gamma(s)$ is compact in all frequencies and supported outside the wavefront set of the localized input. Formula (T16) therefore makes this part of $A_hu$, and its version applied to $d_xu$, rapidly small to arbitrary order.

For the complement, $(1-\gamma(s))/p$ is smooth on the retained tangential patch and decays like $\langle s\rangle^{-2}$. For the output $d_xu$ its numerator has the extra factor $s$ and the tail is $\langle s\rangle^{-1}$. Construct a finite left parametrix in each case by successively dividing the remaining principal error by $p$. Composition with $d_x^2$ is a finite differentiation; tangential compositions and normal Taylor remainders are precisely the bounded-amplitude calculation of (T37)–(T38) and (T50). Normal-frequency derivatives improve the displayed tails. Thus all finite remainders have arbitrary powers of $h$ in operator norm on the fixed $H^2$ input. The separated forcing and the terms where $\theta$ is differentiated are rapidly small after application of the parametrix: integrate in the separated frequency variable as in Sections 4 and 19. Derivatives of the normal tails are integrable after sufficiently many integrations. The equation is only applied to the interior localization, so no boundary extension enters this argument.

We conclude, for every $N$,
\[
 \|A_hu\|+\|A_hd_xu\|\le C_{N,u}h^N.
 \tag{T123}
\]
Apply the fixed-cutoff reconstruction just used in (T122), choosing $N$ larger than the desired order. It proves the tangential pair at every real order on one fixed smaller neighborhood. In particular, a smooth full-phase statement about the bounded characteristic roots has now been supplemented by a proof controlling the unbounded normal-frequency tails.

## 53. Simultaneous induction on the fixed two-root region

Return to the open conic region $W_0$ of Section 48. We prove that its tangential pair is locally finite at every half-integer order $r\ge2$. The initial order is $2$: $u\in H^2$ gives $J_y^2u$ and $J_yD_xu$ in $L^2$ by Plancherel, and order-zero tangential localization is bounded.

Assume the pair is locally finite throughout $W_0$ at order $r-1/2$. At each boundary contact with $a_0=0$, (T118) places the entire closed input support inside $W_0$. The finite-cover argument of Section 36 supplies the actual preceding-order norms in (T89). The incoming edge is regular on the explicitly constructed $\mathcal U_g$. Formula (T92) therefore gives order $r$ in a neighborhood of every such contact. At boundary points with $a_0>0$ or $a_0<0$, Sections 40 and 49 already give all orders.

Consider an interior point over $W_0$. If all its characteristic lifts are regular, Section 52 gives all orders. Otherwise (T117) places the only possible singular lift on a positive outgoing arc from a contact $g$ whose projection belongs to $W_0$. The newly obtained order-$r$ neighborhood of $g$ contains an initial positive part of this arc. Choose a compact interior seed slab there, with positive normal coordinate, and a slightly larger seed cutoff $\Pi$ inside that neighborhood. Its pair in (T119) follows from the gained pair by finite elliptic cutoff factorization, exactly as in Section 36.

The compact arc from this seed slab to the target stays in the larger homogeneous chart by construction. Its $s$ is positive and increasing, so $x$ is a valid parameter and $k=s$ has a positive lower bound on the retained compact arc. Its constants may depend on the chosen seed slab and hence on $r$; no estimate uniform down to the tangency is required. At the target the negative lift is regular by Section 49. Formula (T122) therefore transports order $r$ to a neighborhood of the target. The arc need not project into $W_0$ between the seed and the target: (T121) uses its homogeneous equation and the seed norm, not preceding-order bounds all along the arc.

This accounts for every point of $W_0$ and completes the induction step. For any fixed tangential cutoff $\mathcal B$ with compact conic support in $W_0$, a finite cover at each order gives
\[
 \begin{gathered}
 \mathcal B J_y^r u\in L^2,\qquad
 \mathcal B J_y^{r-1}D_xu\in L^2\\
 \text{for every real }r.
 \end{gathered}
 \tag{T124}
\]
It is enough to prove this for the unbounded sequence of half-integer orders: for a smaller real order, factor the localized operator through a slightly larger elliptic cutoff at the higher order; the remaining Fourier factor has nonpositive order, and the finite remainder acts on the fixed lower norm. Equivalently, its annular norm is multiplied by the bounded factor $h_k^{R-r}$ when $R\ge r$, and the same finite-overlap proof applies. The low-frequency part is bounded directly. The cutoff $\mathcal B$ in (T124) remains fixed for all orders, although the finite covers, seed slabs and constants may change. This avoids replacing smoothness on an open neighborhood by unrelated estimates on neighborhoods shrinking to a point.

## 54. Recovering normal smoothness from the equation

The tangential conclusion also controls all normal derivatives; we give the argument to avoid assuming an external anisotropic regularity theorem. Work in the chart where the original gauged wave $v$ obeys $(D_x^2+R)v=0$, with the actual unscaled tangential differential operator $R$ and all its lower terms. A dot over a tangential differential operator denotes $-i\partial_x$ applied only to its coefficients. Define tangential differential operators $A_j,C_j$ by
\[
 \begin{gathered}
 A_0=I,\quad C_0=0,\quad A_1=0,\quad C_1=I,\\
 A_{j+1}=\dot A_j-C_jR,\\
 C_{j+1}=A_j+\dot C_j,\\
 D_x^jv=A_jv+C_jD_xv.
 \end{gathered}
 \tag{T125}
\]
The last identity holds for $j=0,1$. Differentiate it distributionally, use $D_x(Av)=\dot A v+A D_xv$, and substitute $D_x^2v=-Rv$. This gives exactly the displayed recurrence and proves the identity for every $j$. The orders are at most $j$ and $j-1$, respectively, by induction; all coefficients are smooth. No high normal derivative of the input is assumed in deriving this distributional identity.

Choose a tangential cutoff $\mathcal B$ with compact conic support in $W_0$, and choose its kernel properly supported inside the homogeneous base chart. This means multiplying its kernel away from the diagonal by a smooth cutoff equal to one near the diagonal; the change is tangentially smoothing by the separated-kernel proof of Section 4. The input and output supports, including those of every normal derivative of this kernel, stay in a chart where $u=v$. Thus (T125) can be applied before each such tangential operator, without differentiating the spatial-localization forcing.

Leibniz's formula and (T125) express every mixed derivative of $w=\mathcal Bv$ as a finite sum of tangential operators of finite order acting on $v$ or $D_xv$. Their finite symbol coefficients have phase supports in the support of $\mathcal B$; differentiation does not enlarge those supports. Product and proper-support remainders are retained separately. Each such operator factors through a slightly larger cutoff in (T124) at sufficiently high order. To justify this factorization, use the finite product expansion and divide by the cutoff symbol where it is one; choose the Fourier weight order at least the operator order for $v$, or one greater for $D_xv$. The remaining factor then has order at most zero. Taking enough finite terms leaves an order-zero or smoothing remainder on the fixed $L^2$ inputs $v,D_xv$. The same argument treats compact-frequency terms directly. Consequently every mixed derivative of $w$ is $L^2$ on the half-chart. The recurrence has reduced all remainder inputs to these two fixed functions, so no unproved higher normal norm is hidden in the remainder bound.

Here are explicit boundary and embedding details. For any positive integer $m$, the mixed derivatives just obtained give $w\in H^m$ on the half-space after compact localization. Choose constants $a_1,\ldots,a_m$ with $\sum_{j=1}^m a_j(-j)^k=1$ for $0\le k<m$. The coefficient matrix is invertible: a vector annihilated by all these moments also pairs to zero with every polynomial of degree at most $m-1$, including each polynomial that is one at one of the distinct points $-1,\ldots,-m$ and zero at the others. Every component of that vector must therefore vanish. Define an extension by $E_mw=w$ for $x\ge0$ and $E_mw(x,y)=\sum_{j=1}^m a_jw(-jx,y)$ for $x<0$.

The moment equations match the normal derivatives of orders $0$ through $m-1$ at zero. Their traces exist as $L_y^2$ norm-primitive traces, by (N24), applied to the corresponding mixed derivatives with one further normal derivative in $L^2$. Integration by parts in that norm-primitive identity shows that no boundary delta terms occur when differentiating the extension through order $m$. Changes of variable in the reflected integrals then bound $\|E_mw\|_{H^m}$ by $C_m\|w\|_{H^m(x\ge0)}$.

For $m>k+(d+1)/2$, Cauchy–Schwarz in all Fourier variables gives integrability of $|\xi|^k|\widehat{E_mw}(\xi)|$: the remaining squared weight is bounded by $\langle\xi\rangle^{-2(m-k)}$, whose integral is finite by radial integration. Fourier inversion and dominated convergence give continuous derivatives through order $k$. Since $m$ is arbitrary and each extension agrees with the same $w$ on the physical half-space, we conclude
\[
 \mathcal Bv\in C^\infty(\{x\ge0\}).
 \tag{T126}
\]
Here smoothness up to the boundary means that every mixed derivative is continuous on the closed half-chart. Its normal traces, in particular, are smooth in the tangential variables. The cutoff is fixed and elliptic at the original contact, so this proves strict-diffraction boundary regularity for the actual fixed $H^2$ Dirichlet wave from either prescribed regular punctured leg. It also makes every characteristic lift over a smaller interior portion of this tangential region regular by the Fourier localization argument.

This closes the strict-diffraction argument for the $H^2$ wave under its stated homogeneous local equation and regular incoming-leg hypothesis. Sections 55–62 supply the local cone-regularity input at all glancing contacts; Sections 63–70 construct the corresponding singular generalized curves and prove their exact relation membership. Sections 63–70 supply the homogeneous-interval singular-curve theorem at all contacts. Sections 71–75 prove the initial-data endpoint argument and complete the negative-order transfer for compact interior data. The general curved spectral application is proved in the linked spectral reading, Sections 31–38.

<a id="general-glancing-tube-regularity"></a>

## 55. A clock and transverse coordinates at general glancing

We now drop the strict-diffraction assumption (T2). Throughout Sections 55–62, the actual gauged operator is the stationary wave operator of Section 21, with homogeneous equation near the phase sets used below. Write its principal symbol as $p=s^2+a_0$, where $a_0=r_{\rm sp}(x,y',\zeta)-\tau^2$, $y=(t,y')$, and $\eta=(\tau,\zeta)$. The spatial quadratic form $r_{\rm sp}$ is positive definite. Consider a compact set $K$ of boundary glancing points, normalized by $|\tau|=1$. The time covector is nonzero at every nonzero glancing covector: $r_{\rm sp}=\tau^2$ would otherwise force $\zeta=0$. Work first in one chart with fixed sign of $\tau$; a finite cover treats $K$.

There is an explicit clock, independent of any contact-order condition. Put
\[
 \begin{gathered}
 \lambda=|\tau|,\qquad N=-\tfrac12\operatorname{sgn}(\tau)t,\\
 H_p\lambda=0,\qquad H_pN=\lambda,\\
 Y_0=\lambda^{-1}H_{a_0(0)}^{\rm tan},\qquad Y_0N=1.
 \end{gathered}
 \tag{T127}
\]
Stationarity proves the first identity, and $\partial_\tau p=-2\tau$ proves the second. The normalized boundary field $Y_0$ acts on $(y,\zeta/\lambda)$; it preserves the sign of $\tau$ and the level $\lambda=1$. Flow a local transverse section by $Y_0$. The proved flow and inverse results used in Section 1 give coordinates $(N,I)$, with $Y_0I=0$. Extend $I$ homogeneously of degree zero in $\eta$. For a central point $g\in K$, set $\omega=|I-I(g)|^2$.

On a fixed slightly larger compact coordinate patch, constants can be chosen uniformly for $g\in K$. The boundary function $a_0(0)/\lambda^2$ is invariant under $Y_0$ and vanishes along the orbit through $g$. The mean-value theorem in the $I$ coordinates, followed by differentiation of the square defining $\omega$, therefore gives
\[
 \begin{gathered}
 |a_0(0)|/\lambda^2\le C\sqrt\omega,\\
 |\partial_y\omega|+\lambda|\partial_\eta\omega|
     \le C\sqrt\omega,\\
 |\lambda^{-1}H_p\omega|\le Cx\sqrt\omega,\\
 p=0\quad\Longrightarrow\quad
 |s|/\lambda\le C\sqrt{x+\sqrt\omega}.
 \end{gathered}
 \tag{T128}
\]
For the third line, the normalized tangential Hamilton field at $x$ differs from $Y_0$ by $O(x)$, and $Y_0\omega=0$. For the last line use $a_0(x)-a_0(0)=O(x\lambda^2)$ and $s^2=-a_0(x)$. These are uniform local estimates with all coefficients smooth; they use neither a nonzero $\partial_xa_0$ nor a finite order of contact.

## 56. Nested tubes with positive transport

Choose either orientation $\nu\in\{1,-1\}$, a geometric number $0<\epsilon<1/4$, and a length $\delta>0$ that will be small depending on $\epsilon$ and the coordinate patch. These are distinct from the regularizer parameter $\varepsilon$. For $0\le\theta\le1$ define
\[
 \begin{aligned}
 \phi&=\nu(N-N(g))+x/\epsilon+\omega/(\delta\epsilon^2),\\
 A_\theta&=1+\theta-\phi/\delta,\\
 C_\theta&=\frac{\nu(N-N(g))+\delta}{\epsilon\delta}+\theta,\\
 W_\theta&=\{x\ge0:A_\theta>0,\ C_\theta>0\}.
 \end{aligned}
 \tag{T129}
\]
Here $W_\theta$ is an open relative conic set in tangential phase space inside the coordinate patch. If $A_\theta,C_\theta\ge0$, then $\nu(N-N(g))\ge-\delta-\theta\epsilon\delta\ge-2\delta$ and $\phi\le2\delta$. The nonnegative last two terms in $\phi$ consequently give
\[
 \begin{gathered}
 |N-N(g)|\le2\delta,\quad x\le4\epsilon\delta,\\
 \sqrt\omega\le2\epsilon\delta,\quad A_\theta\le4,\\
 \nu H_p\phi/\lambda
   =1+\frac{2\nu s}{\lambda\epsilon}
          +O\!\left(\frac{x\sqrt\omega}{\delta\epsilon^2}\right),\\
 \nu H_p\phi\ge\lambda/2\quad\text{on }p=0.
 \end{gathered}
 \tag{T130}
\]
Indeed the two errors on the characteristic set have absolute values at most $C\sqrt{\delta/\epsilon}$ and $C\delta$. Choose $\delta_0(\epsilon)$ so their sum is at most $1/2$. The choice also puts the closed physical tube strictly inside the homogeneous base chart and the $(N,I)$ coordinate patch. Fixed auxiliary cutoffs are then one on a neighborhood of this whole tube, including all its physical support boundaries. Their derivatives contribute no physical transport error. A compact extension in the negative $x$ direction is harmless because all quantization here is tangential.

We need positivity between the two normal roots as well as at them. By (T128), every real root over the closed tube satisfies $|s|/\lambda\le C_0\sqrt{\epsilon\delta}$ for a fixed $C_0$. Shrink $\delta_0$ once more so that the same lower bound in (T130) holds throughout $|s|/\lambda\le2C_0\sqrt{\epsilon\delta}$. This follows from its displayed affine formula in $s$. Retain a smooth normal-frequency cutoff equal to one on the smaller interval containing every root and supported in this larger interval. This cutoff will only be used in a square, not in the multiplier whose Hamilton derivative is being computed.

For compact radial support choose $\rho=1/8$ and $Z_\theta(\lambda)=F_1(1+\theta-(\lambda-1)^2/\rho^2)$, where $F_L(a)=e^{-L/a}$ for $a>0$ and $F_L(a)=0$ for $a\le0$. The function $Z_\theta$ is nonnegative and smooth, and $H_pZ_\theta=0$. Increasing $\theta$ increases all three support thresholds. Hence, whenever $\theta<\theta'<1$,
\[
 \begin{gathered}
 \mathcal K_\theta=\overline{\{A_\theta>0,C_\theta>0,Z_\theta>0\}},\\
 \mathcal K_\theta\Subset W_{\theta'}\cap\{Z_{\theta'}>0\},\\
 g\in W_0.
 \end{gathered}
 \tag{T131}
\]
The closure and compact containment are relative to the physical half-space, with the radial variable included. They follow from the strict differences $\theta'-\theta$ in the three defining inequalities and the bounds (T130). The conic hull of any such compact support is correspondingly contained in $W_{\theta'}$. None of these geometric choices depends on a Sobolev order.

## 57. The multiplier and its regular edge

Define $\kappa(c)=F_1(c)/(F_1(c)+F_1(1-c))$. Its denominator never vanishes. This smooth increasing function is zero for $c\le0$ and one for $c\ge1$. The functions $\sqrt{\kappa}$ and $\sqrt{\kappa'}$ are smooth. For the first, near zero factor out $e^{-1/(2c)}$ from its positive smooth denominator. On $0<c<1$,
$\kappa'=\kappa(1-\kappa)(c^{-2}+(1-c)^{-2})$.
Taking its square root gives the product of $\sqrt{\kappa(1-\kappa)}$ and $\sqrt{c^2+(1-c)^2}/(c(1-c))$. Flat exponential decay at both endpoints dominates every derivative of the reciprocal factors, by (C18)–(C19). Extending by zero proves the second assertion. Likewise $\sqrt{F_L'}=\sqrt L\,a^{-1}e^{-L/(2a)}$ on $a>0$, extended by zero, is smooth and flat.

For a fixed $L\ge1$ put
\[
 q=-\nu Z_\theta^2F_L(A_\theta)\kappa(C_\theta).
 \tag{T132}
\]
This is a real tangential multiplier; its normal-linear coefficient is exactly zero. Every physical finite coefficient of its quantization and derivatives has support in the closed tube of (T131). The only negative term in its Hamilton derivative is where $\kappa'$ is nonzero. The closed support of that term satisfies
\[
 \begin{gathered}
 |\nu(N-N(g))+\delta|\le\epsilon\delta,\\
 0\le x\le4\epsilon\delta,\qquad |I-I(g)|\le2\epsilon\delta,\\
 |z-\exp(-\nu\delta Y_0)g|\le C_1\epsilon\delta,\\
 z=(y,\zeta/\lambda).
 \end{gathered}
 \tag{T133}
\]
The first line follows from $0\le C_\theta\le1$ and $0\le\theta\le1$. In flow coordinates the reference point in the last line has coordinates $(N(g)-\nu\delta,I(g))$. The inverse coordinate map has bounded derivative on the compact patch, proving that line without a flow approximation. We will assume regularity on a slightly larger open cylinder containing this closed edge. Compact containment is essential for the estimates below.

## 58. Squares retaining the actual regularizer

Fix a target Sobolev order $r$ and use $w=u_\varepsilon=\mathcal A_\varepsilon u$ from (T65)–(T70), with its actual equation $P_hw=\mathcal A_\varepsilon f+h^2\mathcal G_\varepsilon w$. Write $b=b_{h,\varepsilon}$ for the real coefficient in (T75), with uniform bound $|b|\le M_r$ on the larger tangential annulus. It is independent of $s$. Let $\lambda_{\min}>0$ be a lower bound on the radial supports. Choose
$L\ge\max(1,256M_r\delta/\lambda_{\min})$.
Only this flatness parameter, not the tube geometry, depends on $r$.

On the physical tube define the following real nonnegative symbols, with the normal cutoff specified after (T130) understood on $J$:
\[
 \begin{aligned}
 B&=Z_\theta\sqrt{\kappa(C_\theta)F_L'(A_\theta)}
                              \sqrt{\lambda/(4\delta)},\\
 E&=Z_\theta\sqrt{F_L(A_\theta)\kappa'(C_\theta)}
                              \sqrt{\lambda/(\epsilon\delta)},\\
 D&=\nu H_p\phi-\lambda/4
                         +2\nu b\delta A_\theta^2/L,\\
 J&=Z_\theta\sqrt{\kappa(C_\theta)F_L'(A_\theta)/\delta}\sqrt D,\\
 H_pq-2bq&=J^2+B^2-E^2\qquad(p=0).
 \end{aligned}
 \tag{T134}
\]
The bracket $D$ is at least $\lambda/8$ on the larger normal interval: (T130) leaves $\lambda/4$, and the subtracted regularizer contribution is at most $32M_r\delta/L\le\lambda_{\min}/8$. It also has a uniform upper bound. Thus $J$ is smooth before multiplication by its cutoff and extends smoothly by zero through all the flat support boundaries. All fixed symbol derivatives are uniform for $0<h,\varepsilon\le1$. No differentiation in these two parameters is needed.

To verify the last line, use $H_pA_\theta=-H_p\phi/\delta$, $H_pC_\theta=\nu\lambda/(\epsilon\delta)$ and $F_L/F_L'=A_\theta^2/L$. The radial factor has zero Hamilton derivative. These identities give the stated positive and negative terms with their displayed signs for either orientation. The normal cutoff equals one at both roots, so it does not affect this identity. No Hamilton derivative of that cutoff has been introduced into $H_pq$.

There is also a useful normal slope. Throughout the interval joining the two roots, the normal cutoff is identically one and $\partial_sD=2\nu/\epsilon$. Consequently
\[
 \partial_sJ
  =\frac{\nu Z_\theta
        \sqrt{\kappa(C_\theta)F_L'(A_\theta)/\delta}}
            {\epsilon\sqrt D}.
 \tag{T135}
\]
In particular its sign is $\nu$ and it cannot vanish in the interior of the tangential weight. This will recover the normal derivative instead of leaving it as an uncontrolled input at the output point.

## 59. The localized energy identity on the full tube

Divide $J$ by $s^2+a_0$ using (C1)–(C17), writing $J=j_0+j_1s+p\mu$. A tangential momentum coordinate can be chosen to be $a_0$ near the glancing patch: the spatial quadratic form is positive definite and $r_{\rm sp}=\tau^2>0$ there, so its gradient in $\zeta$ is nonzero. This choice retains $x$ as an independent parameter. Thus the division and the flat elliptic completion require no assumption on $\partial_xa_0$. Choose their extensions in a small collar contained in the larger support in (T131). The jet construction is uniform in $h,\varepsilon$: at each extension step use the supremum of its finitely many required symbol seminorms, as in Section 30.

Here is the polynomial calculation including the elliptic side. Put $F_0=\{a_0,q\}_{\rm tan}-2bq$, $F_1=2\partial_xq$, and $\ell=-j_1^2$. Define
$D_0=F_0-j_0^2-B^2+E^2-\ell a_0$ and $D_1=F_1-2j_0j_1$.
At both real roots, (T134) gives $D_0+sD_1=0$. Hence both residuals vanish on $a_0<0$, and are flat at $a_0=0$, with uniform bounds. The explicit dyadic construction (T30)–(T31), taking suprema also over $h,\varepsilon$, gives a common nonnegative flat majorant $k$. To retain its support, cover the intersection of the closed coefficient support with $a_0=0$ by finitely many product collars in the $a_0$ coordinate, each contained in $W_{\theta'}$. Partition the residuals among these collars, construct each local majorant, and sum them. The triangle inequality preserves the required domination for the original residuals. Any remaining compact elliptic part, bounded away from $a_0=0$, has a smooth dominating cutoff in $W_{\theta'}$. Thus the entire majorant stays in the larger tube. Exactly as in (T32),
\[
 \begin{gathered}
 \mathcal N=\begin{pmatrix}
 D_0+ka_0&D_1/2\\ D_1/2&k
 \end{pmatrix}\ge0,\\
 F_0+sF_1=(j_0+j_1s)^2+B^2-E^2\\
 \hspace{13mm}+(\ell-k)p+(1,s)\mathcal N(1,s)^{\mathsf T}.
 \end{gathered}
 \tag{T136}
\]
The inequality follows from $k\ge2|D_0|/a_0+|D_1|/\sqrt{a_0}$ on $a_0>0$ by completing the square; on $a_0\le0$ the matrix is zero. This is an identity throughout the coefficient patch, not only on the characteristic set.

Let $Q_h$ be the self-adjoint tangential quantization of $q$, $B_h=\operatorname{Op}_h(B)$, $E_h=\operatorname{Op}_h(E)$, and $\mathcal J_hw=\operatorname{Op}_h(j_0)w+\operatorname{Op}_h(j_1)d_xw$. The exact Dirichlet identity (T26) now has zero boundary contribution: the multiplier has no normal-linear coefficient, and $Q_hw(0)=0$ because $w(0)=0$. Its right side contains $2\operatorname{Im}(h\mathcal G_\varepsilon w,Q_hw)$. The expansion (T76) makes its principal real form $2bq$. Moving this term to the left leaves $F_0+sF_1$; the remainder is an order-$h$ quadratic form with localized coefficients, together with the arbitrary-order lower-norm remainder of Section 28.

Apply (T34) to the two squares and the matrix in (T136). Apply (T35) to its equation multiple. The latter contributes the actual pairing $\operatorname{Re}((\ell-k)^s_hP_hw,w)$, including $h^2\mathcal G_\varepsilon w$. On the enlarged annulus, $h\mathcal G_\varepsilon$ is uniformly of order zero by (T76), so this contribution is bounded by order $h$ times the larger localized energy. The same estimate retains the normal derivative of $(\ell-k)^s_h$ from the integration by parts and every lower coefficient of $R_h$. There is no full-phase edge quotient in this calculation: $E$ itself is tangential. Each use of the equation has therefore been accounted for.

For clarity about localization, fix $\theta<\theta'<1$. All finite coefficient supports just described, including the chosen elliptic collars and their normal derivatives, lie in a compact subset of $W_{\theta'}$. Choose a smooth tangential symbol $S$, equal to one on a neighborhood of those supports and supported in $W_{\theta'}$, with a slightly larger such support retained for finite product remainders. The factorization (T44) localizes each order-$h$ form to these cutoffs. The packet positivity estimate is localized by the same finite products, applied to the vector $(w,d_xw)$. Moving a normal derivative through a cutoff contributes $-ih\partial_xS$, whose support is covered by the larger cutoff. Enlarge $S$ once to cover this finite collection. Actual bounded-amplitude remainders, whose supports need not remain compact, are estimated by (T77)–(T78) with sufficiently many powers of $h$. They are not assigned the supports of formal coefficients.

The forcing $\mathcal A_\varepsilon f$ is rapidly small in all these pairings by (T72) and its weighted version in Section 28: the whole closed tube lies where the spatial localization equals one. The resulting estimate is
\[
 \begin{aligned}
 &\|\mathcal J_hw\|^2+\|B_hw\|^2\\
 &\qquad\le\|E_hw\|^2+Ch\mathcal H_{S,h}(w)^2\\
 &\qquad\quad+C_{N,u}h^N,\\
 &\mathcal H_{S,h}(w)^2=\|S_hw\|^2+\|S_hd_xw\|^2.
 \end{aligned}
 \tag{T137}
\]
Here $S_h=\operatorname{Op}_h(S)$, and $N$ is arbitrary. Constants may depend on $r,L,\theta,\theta',\epsilon,\delta$ and the fixed solution, but not on $h,\varepsilon$. The uniform global remainder norm is (T77), not a presumed high $H^2$ norm of $u_\varepsilon$. For each positive regularizer the Dirichlet approximation already proved for (T26) justifies these identities on the actual $H^2$ input.

## 60. Recovering the two components and estimating the edge

Fix a tangential point in $W_\theta$ with $a_0\le0$ and normalize its time frequency to $\lambda=1$. Put $\kappa_0=\sqrt{-a_0}$. The root-division formula and (T135) give
\[
 \begin{aligned}
 j_1&=\frac{1}{2\kappa_0}
             \int_{-\kappa_0}^{\kappa_0}\partial_sJ\,ds
                    &&(\kappa_0>0),\\
 j_1&=\partial_sJ|_{s=0}&& (\kappa_0=0),\\
 \nu j_1&\ge c_r>0,\qquad B\ge c_r>0,\\
 \mathcal M&=\begin{pmatrix}B&0\\j_0&j_1\end{pmatrix}.
 \end{aligned}
 \tag{T138}
\]
The lower bounds hold on each retained compact inner real-root patch and are uniform in $h,\varepsilon$. They follow because the flat factors are strictly positive there, while $D$ has a uniform upper bound. At a merging root use the second line and continuity. The bounded symbol derivatives then give a common neighborhood on which the matrix determinant stays away from zero, including a small elliptic collar if needed. Construct a finite left inverse using the adjugate formula and the same recursive error cancellation as in Section 32. Uniformity requires no derivatives in the regularizer parameters. Normal ordering, if a self-adjoint normal-linear representative is used, adds only the actual term $-ih\partial_x\operatorname{Op}_h(j_1)/2$, already controlled by the larger energy. Equivalently the definition of $\mathcal J_h$ above puts every normal derivative on the input and avoids that ordering change.

Call a tangential phase point regular if one fixed tangential cutoff, elliptic there and properly supported in the homogeneous base chart, has the Fourier-weighted pair $\mathcal B J_y^R u$, $\mathcal B J_y^{R-1}D_xu$ in $L^2$ for every real $R$. This is an open condition: the same cutoff is elliptic on a neighborhood, and finite cutoff factorization proves the assertion for smaller cutoffs. On compact subsets of an open regular set the finite-cover argument of Section 36 gives these norms for any cutoff supported there.

Suppose the closed edge in (T133) is contained in such a regular open set. For every desired $N$, choose a sufficiently large $R$ and a cutoff $\Pi$ equal to one near its support. The exact right Fourier product $E_h\mathcal A_\varepsilon J_y^{-R}$ has normalized annular norm at most $Ch^{R-r}$. Insert $\Pi$ before $J_y^Ru$ by the finite product formula. The complementary term is arbitrarily small on the fixed lower norm by (T78), and the retained term is bounded by the actual regular norm $\|\Pi J_y^Ru\|$. Taking $R$ sufficiently large proves $\|E_hu_\varepsilon\|=O(h^N)$ uniformly in $\varepsilon$. This proof does not assume that the edge lies in the interior or that only one of its normal lifts is regular.

Apply the finite inverse of $\mathcal M$ to (T137). Choose a fixed output symbol $q_*$ equal to one on a smaller neighborhood of the chosen point, independent of $h,\varepsilon$, and put $Q_{*,h}=\operatorname{Op}_h(q_*)$. Weighted remainders are again bounded by (T77)–(T78). We obtain
\[
 \begin{aligned}
 &\|Q_{*,h}u_\varepsilon\|^2+
       \|Q_{*,h}d_xu_\varepsilon\|^2\\
 &\qquad\le Ch\mathcal H_{S,h}(u_\varepsilon)^2+C_{N,u}h^N.
 \end{aligned}
 \tag{T139}
\]
The constants and auxiliary inverse may depend on the target order; the tube $W_\theta$ and its larger neighbor $W_{\theta'}$ do not.

## 61. Sobolev induction on the fixed nested regions

Assume that the preceding pair of order $r-1/2$ is locally finite throughout $W_{\theta'}$. The support of $S$ is compact there, so the finite-cover argument gives the two actual inputs in (T89) with a cutoff equal to one near this support. The proof of (T90) applies with this single $S$: the multipliers $h^{1/2}S_h\mathcal A_\varepsilon J_y^{-(r-1/2)}$ and $h^{3/2}S_h\mathcal A_\varepsilon J_y^{-(r-3/2)}$ have uniformly bounded normalized symbols and finite-overlap input annuli. Thus the sum of $h\mathcal H_{S,h}(u_\varepsilon)^2$ is uniformly bounded on the frequency sequence (T87).

Sum (T139), first over finitely many bands, pass to $\varepsilon=0$ by (T74), and then increase the number of bands. The output cutoff is fixed in this limit. The output-frequency tail and finite-overlap proof of (T88) gives the order-$r$ pair near the chosen point. In particular we have a half-order gain for both components with their one-order offset; an estimate for the wave alone has not been used as a substitute for the normal component.

Prove the following statements simultaneously for every $0\le\theta<1$: the pair is locally finite on $W_\theta$ at order $r_n=2+n/2$. The initial case is the fixed global $H^2$ input. At an induction step fix $\theta$ and choose $\theta'=(1+\theta)/2$. At every point of $W_\theta$ with $a_0\le0$, (T139) and the preceding paragraph apply, because the previous-order assertion is already known everywhere in $W_{\theta'}$. At points with $a_0>0$, boundary regularity is supplied by (T99); in the interior (T123) applies since there are no real characteristic lifts. Those points are already regular to all orders. This covers every point of $W_\theta$ and proves the step simultaneously for all $\theta$.

The choice of $L$ at each step may increase with $r_n$, but the geometry and the nested open sets never change. Consequently, for any fixed tangential cutoff $\mathcal B$ with compact conic support in $W_0$,
\[
 \begin{gathered}
 \mathcal B J_y^r u\in L^2,\qquad
 \mathcal B J_y^{r-1}D_xu\in L^2,\\
 \text{for every real }r.
 \end{gathered}
 \tag{T140}
\]
Use finite covers at each half-integer order and then the lower-order factorization after (T124). The cutoff stays fixed while the covers and constants vary. Finally the normal recurrence (T125) and the finite-reflection extension proof of Section 54 use only the actual homogeneous equation and these all-order pair norms. Neither proof uses strict diffraction. Applying them here yields
\[
 \mathcal Bv\in C^\infty(\{x\ge0\}),
 \qquad \mathcal B\text{ elliptic near }g.
 \tag{T141}
\]
Thus the local conclusion includes normal smoothness up to the boundary and a fixed regular neighborhood of the original point.

## 62. Local cone regularity at arbitrary contact order

We can state the input just proved without the internal cutoff constants. Let $K$ be a compact normalized glancing set in a homogeneous stationary Dirichlet wave chart, and let $\epsilon_*>0$. There is a $\delta_*>0$, uniform on $K$, such that the following implication holds for either orientation $\nu$ and every $0<\delta<\delta_*$. If every point of the open relative cylinder
\[
 \begin{gathered}
 0\le x<\epsilon_*\delta,\\
 |z-\exp(-\nu\delta Y_0)g|<\epsilon_*\delta,
 \qquad g\in K,
 \end{gathered}
 \tag{T142}
\]
is tangentially regular in the sense of Section 60, then $g$ is regular, with the normal smoothness in (T141). To obtain this statement, choose the internal $\epsilon$ smaller than $\epsilon_*/(2\max(4,C_1))$ and smaller than $1/4$. Then (T133) puts the whole closed edge strictly inside (T142). Compactness gives the edge's finitely many regular cutoffs. Choose $\delta_*$ below the geometric bounds in Section 56 and use a finite chart cover of $K$. The remaining argument is Sections 58–61. In particular $\delta_*$ is independent of the Sobolev order, because increasing $L$ absorbs the regularizer coefficient without reducing the tube.

Equivalently, if $g$ is not regular, each such cylinder contains a point that is not regular. At an interior point, (T123) shows that at least one actual characteristic lift is then singular. At boundary elliptic points, (T99) rules out such a failure. Taylor's integral formula for the smooth flow gives $\exp(-\nu\delta Y_0)g=g-\nu\delta Y_0(g)+O(\delta^2)$, uniformly on $K$. Hence the failed-regularity point has arbitrarily small error relative to the first-order gliding displacement when $\epsilon_*$ and then $\delta$ are small. This controls $x$ and the normalized tangential variables. It does not assert an $O(\delta)$ bound for the normal covector; the square-root bound in (T128) is what was actually proved.

This local result applies at gliding, strict-diffraction and arbitrarily degenerate glancing contacts. It supplies the local approximate gliding step needed to construct a curve of singular points. Sections 63–70 construct that curve and prove its membership in the full normal-reaction relation (G1)–(G23). Sections 71–75 prove the initial-data endpoint argument and negative-order transfer for the spectral Dirichlet wave at every required compact interior input order. For the curved spectral remainder, use the spectral reading, Sections 31–38.

<a id="singular-generalized-curves"></a>

## 63. The closed compressed singular set

Continue with the actual stationary Dirichlet wave $v$ of local class $H^2$, homogeneous in the spacetime region under consideration. Normalize the time covector to $\tau=\pm1$ and fix its sign. Write $y'$ for the spatial tangential coordinates, $\zeta$ for their covectors and
\[
 \begin{gathered}
 p=s^2+r(x,y',\zeta)-1,\qquad r=r_{\rm sp},\\
 z=(t,y',\zeta),\qquad v_n=xs,\\
 \Gamma=(x,z,v_n).
 \end{gathered}
 \tag{T143}
\]
The new symbol $v_n$ denotes a compressed normal coordinate, not the wave $v$. These are the energy-space coordinates (G3), with physical time retained. In the interior they recover the full covector $s=v_n/x$. At the wall they identify exactly the two opposite normal lifts; at glancing the lifts coincide.

Define $F$ as follows. At $x>0$ retain the actual characteristic wavefront points of $v$, with their full covectors encoded by (T143). At $x=0$ retain the tangential points that fail the regularity condition of Section 60. Elliptic boundary points are absent by (T99), and interior noncharacteristic points are absent by the finite parametrix used after (T117). Thus $F$ is a subset of this compressed characteristic space.

This set is relatively closed in the homogeneous region. Interior closedness follows from the definition of wavefront as the complement of the open set of Fourier-regular cutoffs. At the wall, regularity in Section 60 is open and (T125)–(T126) turn its pair norms into smoothness of one properly supported tangential localization up to the wall. On a smaller conic tangential patch, construct a finite inverse of this elliptic cutoff, to any prescribed order, using the proved product expansion. Every characteristic full covector there has nonzero tangential frequency, comparable to its full frequency. The inverse therefore shows that all nearby interior characteristic lifts are regular. The remainders are controlled on the fixed lower norm; increasing their order gives every Fourier decay rate. Consequently interior singular points cannot approach a regular boundary point. Boundary singular points cannot do so either, by openness. This proves the asserted closedness, including sequences that change from interior to boundary. In a compact phase box, $F$ is compact.

Introduce the closed exceptional contact set
\[
 \mathcal S=\{x=0,\ r=1,\ r_x\ge0\}.
 \tag{T144}
\]
It consists of strict gliding and degenerate glancing points in our inward-normal convention. Outside $\mathcal S$, $F$ is locally invariant along the ordinary, reflected or strict-diffractive characteristic arc. Interior invariance is the contrapositive of (T114). At a hyperbolic wall point, (T112) says that regularity on either incident leg gives boundary regularity and regularity of the reflected leg. Hence a point of $F$ has both singular incident legs. Conversely a singular interior leg cannot reach a regular boundary point, by the closedness just proved. At strict diffraction, (T126) gives the same implication from either punctured leg, so both legs through a singular contact are singular. Their ordinary trajectory is unique and is interior on its punctured sides by (T4). These arguments prove local invariance with the actual full interior covectors retained.

## 64. Approximate gliding steps in compressed coordinates

At a point $g\in F\cap\mathcal S$, the contrapositive of (T142) supplies short steps in $F$. More precisely, for any compact subset of $F\cap\mathcal S$ and any $e>0$, all sufficiently small nonzero $h$ have an endpoint $q_e(h,g)\in F$ with
\[
 \begin{aligned}
 0\le x(q_e)&\le e|h|,\\
 |z(q_e)-\exp(hY_0)g|&\le e|h|.
 \end{aligned}
 \tag{T145}
\]
Uniformity on the compact set is part of Section 62. Use $\nu=-1$ for $h>0$ and $\nu=1$ for $h<0$. If its nonregular endpoint is interior, (T123) supplies at least one singular characteristic lift; choose that actual lift to define $q_e$. At a boundary endpoint use the compressed point. No arbitrary regular normal lift is selected.

At $g$, $r=1$ and $Y_0$ is the boundary restriction of the wave's tangential Hamilton field. It preserves $r(0)$ along its boundary orbit. Smoothness and (T145) imply $|1-r(q_e)|\le C e|h|$. At an interior endpoint, energy therefore gives $|s(q_e)|\le C\sqrt{e|h|}$. At the wall $v_n=0$ anyway. It follows that
\[
 \begin{gathered}
 |v_n(q_e)|\le C(e|h|)^{3/2},\\
 \left|\frac{q_e(h,g)-g}{h}-V_g(g)\right|
       \le C(e+|h|),\\
 V_g=(0,Y_0,0).
 \end{gathered}
 \tag{T146}
\]
The norm in the second line is the Euclidean norm of the compressed coordinates (T143). Taylor's integral formula bounds the flow error by $C|h|$ after division by $h$. The normal-coordinate error divided by $|h|$ is $O(e^{3/2}|h|^{1/2})$, absorbed in the displayed bound when $e,|h|\le1$. This is exactly where compression is useful: no first-order estimate for the uncompressed normal covector has been asserted.

## 65. Piecewise curves that stay close to the singular set

Fix an initial point in a smaller compact phase box whose closure lies in a larger homogeneous coordinate chart. In a boundary chart use (T143); in an interior chart ordinary propagation already gives the local result. All the following constants refer to the larger compact box. Genuine ordinary arcs, their transverse reflections and their passages through strict diffraction satisfy (G4). Their compressed coordinate speeds are uniformly bounded by (G6)–(G7), on every finite segment before reaching $\mathcal S$. This bound also gives a limit if such an arc has a finite maximal endpoint. The limit is in $F$ by closedness. If it is outside $\mathcal S$ and still in the chart, the local invariance and continuation from Section 63 extend the arc. Hence an unextendible endpoint within the box belongs to $F\cap\mathcal S$.

Choose $e_j\downarrow0$ and a fixed step length $\delta_j\downarrow0$ for each $j$, smaller than the uniform threshold in (T145) for $e=e_j$. From the initial point follow the exact singular arc for as long as possible, stopping at $F\cap\mathcal S$, or at the chosen final parameter time. At a stopped point in $F\cap\mathcal S$, join it by a straight line in compressed coordinates to $q_{e_j}(\delta_j,g)$, over a parameter interval of length $\delta_j$. Resume the exact singular arc from that endpoint. Use a shorter final step only if it reaches the prescribed final time. Repeat backward with $h<0$ for the negative parameter interval.

There are at most $1+T/\delta_j$ inserted steps in either interval of length $T$. An exact piece may include infinitely many reflections approaching its endpoint; its compressed limit exists by the uniform speed bound just given. It is a single continuous piece ending in $F$, so no finite-time accumulation is omitted. If an exact piece lies wholly in $F\cap\mathcal S$, start an inserted step immediately instead. These rules define the approximant on the whole prescribed interval unless it leaves the larger box.

Equation (T146) gives a uniform bound on the speeds of the inserted steps as well. Take $T>0$ smaller than the distance from the smaller box to the boundary of the larger chart divided by twice a common speed bound. If necessary take $\delta_j$ still smaller than this margin. The total displacement estimate then prevents every approximant from leaving the chart before time $T$, in either direction. Denote it by $\Gamma_j:[-T,T]\to\mathbb R^m$. Its exact pieces lie in $F$, while every point of an inserted step is within $C\delta_j$ of its initial endpoint in $F$. Thus
\[
 \begin{gathered}
 |\Gamma_j(b)-\Gamma_j(a)|\le C|b-a|,\\
 \operatorname{dist}(\Gamma_j(a),F)\le C\delta_j.
 \end{gathered}
 \tag{T147}
\]
Intermediate points of the straight segments need not be characteristic. This is permitted only for the approximants; the limit will lie in $F$. The countable-mesh diagonal argument proved in Section 4 of the generalized-curve reading gives a uniformly convergent subsequence. Write its limit as $\Gamma$. It is Lipschitz, starts at the prescribed point, and belongs to $F$ at every parameter value, by (T147) and closedness. This constructs a curve of singular points, but its differential laws still require verification.

## 66. Exact equations in the limit

Use $a$ for the curve parameter, and retain the normalization $\tau=\pm1$. On every exact piece,
\[
 \begin{gathered}
 \frac{dt}{da}=-2\tau,\\
 \frac{dy'}{da}=r_\zeta,\qquad\frac{d\zeta}{da}=-r_{y'},\\
 \frac{dv_n}{da}=2(1-r)-xr_x.
 \end{gathered}
 \tag{T148}
\]
The last equality is (G6). The first three right sides are smooth functions of $x,z$; they do not involve $s$. At the initial point of an inserted step, its tangential derivative differs from the first three right sides by $O(e_j+\delta_j)$, by (T146). Throughout the step, the right sides change by at most $C\delta_j$. Its $v_n$ derivative has size $O(e_j^{3/2}\delta_j^{1/2})$, while the last right side is zero at its initial point and $O(\delta_j)$ along the step. The same bounds hold for a shortened final step, and for negative steps. Consequently all four integral equations in (T148) have errors bounded by $C(e_j+\delta_j)$ times the interval length. Uniform convergence permits passage to the limit in their smooth right sides. We conclude that $t,y',\zeta,v_n$ are $C^1$ and satisfy (T148) exactly along $\Gamma$.

The limiting curve is already admissible in the sense of (G4) locally wherever its value is outside $\mathcal S$. To verify this carefully, choose a small closed parameter interval whose limiting image has positive distance from $\mathcal S$ and remains in one chart. Inserted steps start on $\mathcal S$ and have diameter $O(\delta_j)$, so for large $j$ no such step meets this interval. Its restrictions are genuine arcs satisfying (G4). The compactness theorem proved in Section 4 of the generalized-curve reading applies to these restrictions and identifies their limit with an admissible curve. In the interior the full covector is recovered by $s=v_n/x$; at a hyperbolic wall point its two one-sided lifts have the exact reflection law (G9), and the reflection is isolated. At strict diffraction (G11)–(G12) make the limiting arc the ordinary smooth Hamilton trajectory on both punctured sides. None of these conclusions uses compactness of the artificial straight segments as if they were admissible curves.

Define $s=v_n/x$ where $x>0$, set $s=0$ at glancing points, and use the outgoing one-sided value at an isolated transverse reflection. Energy and continuity of the compressed curve give
\[
 \begin{gathered}
 g(a):=1-r(x(a),y'(a),\zeta(a))\ge0,\\
 s(a)^2=g(a),\\
 x(b)-x(a)=2\int_a^b s(u)\,du.
 \end{gathered}
 \tag{T149}
\]
Here is an integral proof of the second identity that does not assume differentiability on the wall set. The open set $\{x>0\}$ is a countable union of disjoint intervals: assign a different rational number to each interval. On each such interval the already proved ordinary equation is $x'=2s$. For an interval with both endpoints on the wall, its integral is zero, by boundedness of $s$, continuity of $x$ and limits of the ordinary identity. Between arbitrary $a,b$, at most two components have only one endpoint on the wall; their integrals give exactly $x(b)-x(a)$. Sum the integrals, which converge absolutely since $s$ is bounded. On the remaining wall set $s=0$ except at the isolated transverse reflections. These are countable and do not affect the integral. This proves (T149) and supplies the required absolute continuity of $x$ directly.

## 67. Normal regularity at gliding and degenerate points

The smooth chain rule applied to (T149) and the exact tangential equations gives
\[
 g'=-2r_xs\quad\text{almost everywhere}.
 \tag{T150}
\]
For this use of the chain rule, one may telescope the smooth function $r$ along a fine partition of the Lipschitz coordinate path. Taylor's remainder is bounded by a constant times the sum of squared increments, which tends to zero. The first-order sums converge to the integrals against $x'=2s$ and the continuous tangential derivatives. The two tangential terms cancel, since $r_{y'}r_\zeta-r_\zeta r_{y'}=0$. This proves (T150) as an integral identity as well.

Regularize the square root by $\sqrt{g+\mu^2}$ for $\mu>0$. Its absolutely continuous derivative has absolute value at most $|r_x|$, because $|s|=\sqrt g$. Integration followed by $\mu\downarrow0$ yields
\[
 \left|\sqrt{g(b)}-\sqrt{g(a)}\right|
       \le\int_a^b|r_x(u)|\,du.
 \tag{T151}
\]
Here $a<b$. Thus the normal magnitude is Lipschitz, even if there are infinitely many reflections. At a degenerate contact $a_0$, both $g(a_0)$ and $r_x(a_0)$ vanish. The composed function $r_x$ is Lipschitz on the retained compact chart, so (T151) and then (T149) give
\[
 \begin{gathered}
 |s(a)|\le C|a-a_0|^2,\\
 0\le x(a)\le C|a-a_0|^3.
 \end{gathered}
 \tag{T152}
\]
In particular the chosen normal representative is differentiable at $a_0$ with derivative zero, regardless of nearby reflection accumulation. This treats arbitrarily degenerate contact; it does not assume a first nonzero finite jet.

At a strict gliding point, $r_x>0$. Retain a neighborhood where $r_x\ge\kappa>0$, and put $E=g+xr_x$. Its chain rule and (T150) give
\[
 \begin{gathered}
 E\ge g+\kappa x\ge0,\qquad E'=x(r_x)',\\
 |E'|\le C E.
 \end{gathered}
 \tag{T153}
\]
The derivative of $r_x$ along the Lipschitz path is bounded, by the same smooth chain rule. At the gliding point, $E=0$. The integral inequality forces $E=0$ in a neighborhood in both directions: on a sufficiently short interval its supremum is at most $C$ times the interval length times that same supremum, and subdivision extends the conclusion. Therefore $x=g=s=0$ there. The tangential equations reduce to the gliding Hamilton field on the wall, and $s'=0$. This proves local gliding residence rather than assuming it from a limiting picture.

## 68. The inward reaction and the exact geometric relation

We now check the remaining part of (G4), namely that the normal reaction is nonnegative and has no support in the interior. Set
\[
 M(a)=s(a)+\int_{a_*}^a r_x(u)\,du.
 \tag{T154}
\]
Here $r_x(u)$ is evaluated at $(x(u),y'(u),\zeta(u))$. The function $s$ is continuous at every glancing point by energy, and is smooth in the interior. Its only discontinuities are the isolated transverse reflections already established in Section 66; their jumps are $2\sqrt g>0$. Choose the right-continuous, outgoing representative there. Consequently $M$ is upper semicontinuous on a compact parameter interval. At an accumulation of reflection points the limiting point must be glancing, since each hyperbolic point has an isolated-reflection neighborhood; energy makes $s$ tend to zero there and proves continuity. This also verifies upper semicontinuity at such accumulations.

At every nonreflection point $M$ is differentiable and $M'\ge0$. In the interior and at strict diffraction its derivative is zero by the ordinary Hamilton equation. At degenerate glancing it is zero by (T152). At strict gliding it is $r_x>0$ by (T153). At a transverse reflection the right derivative exists and is zero, and the jump is positive.

These facts imply monotonicity without assuming bounded variation in advance. For any $c<d$ and $\alpha>0$, the upper semicontinuous function $M(a)+\alpha a$ attains its maximum on $[c,d]$. A maximum at a point before $d$ is impossible: its right derivative exists and is at least $\alpha>0$, including at a reflection with the outgoing representative. Hence the maximum is at $d$, which gives $M(c)\le M(d)+\alpha(d-c)$. Let $\alpha\downarrow0$. Thus $M$ is nondecreasing.

It is constant on every open interval with $x>0$ by the ordinary equation. Its total increase on a compact collar interval obeys the same elementary bound as (G5); specifically $|s|\le1$ and $|r_x|\le C$ give
\[
 \begin{gathered}
 0\le M(b)-M(a)\le2+C(b-a),\\
 \operatorname{Var}_{[a,b]}s\le2+2C(b-a).
 \end{gathered}
 \tag{T155}
\]
Equation (T154), the nondecreasing $M$, its interior constancy, (T149), energy, and the tangential equations in (T148) are precisely (G4). The Stieltjes construction already proved after (G5) therefore identifies its increase as an inward reaction supported on the wall. Every limiting singular curve constructed here belongs to the exact programme relation, including the prescribed full endpoint lifts. No weaker boundary cone has replaced that relation.

## 69. Continuation inside the homogeneous singular set

The local construction gives an open two-sided interval through every point of $F$. Its interval length has a positive lower bound for starting points in a compact subset of one smaller phase chart: the speed and chart-margin bounds in Section 65 are uniform, and (T145) is uniform on the compact exceptional set in the larger chart. A finite chart cover gives the corresponding local existence on a compact part of the normalized characteristic space.

A singular curve can be continued while remaining in a compact homogeneous region. Its compressed endpoint exists by (G7), and belongs to $F$ by closedness. Apply the local construction at that endpoint and attach the required half of its singular curve. In the interior the full covector is determined by compression. At glancing both normal limits are zero. At a transverse point an arriving lift is negative and a departing lift positive, so the join adds the allowed nonnegative jump to $M$. The exact tangential derivatives agree. Thus the continuation remains in $F$ and satisfies (G4), preserving the segment already constructed. The uniform local intervals just described permit successive extension across any compact parameter interval inside the homogeneous region.

Finally the exact clock in (T148) gives
\[
 t(a)=t(0)-2\tau a,\qquad \tau=\pm1.
 \tag{T156}
\]
It cannot stall at a radial point. On a compact spatial manifold and a compact physical-time slab contained in the homogeneous region, the normalized phase space is compact, so the singular curve continues across the slab. General nonzero time frequencies follow by the homogeneous scaling already checked after (G22). With physical time as parameter, the tangential equations become exactly (G22), and the endpoint convention is the one used in (G23).

## 70. The proved propagation statement and the initial-data step

We have proved the following local and homogeneous-interval statement for the actual $H^2$ Dirichlet wave: through every point of its closed compressed singular set there is a two-sided generalized characteristic, contained in that singular set, satisfying the full energy-preserving inward-reaction relation (G1)–(G23). The curve continues across every compact time slab on which the equation is homogeneous and the stated regularity is available. In the interior its singular points are actual full wavefront points, not projections with an arbitrary normal lift. The construction allows all glancing orders and all accumulating-reflection limits. It asserts existence of an appropriate singular curve through each point; it does not assert propagation along every possible generalized curve when uniqueness fails.

This supplies the previously missing analytic identification of the local singular-curve construction with the programme's geometric relation. Sections 71–75 below give the Cauchy-data assertion used in the boundary lesson. A boundary local-dependence estimate compares the actual wave to a smooth compatible spectral solution near the initial wall. Exact time modes then identify an interior singular endpoint with singular initial data. Finally (W1)–(W22) transfer this assertion to every required negative order for compact interior data. The complete scaled comparison and both curved spectral bounds are proved in [the spectral reading](curved-boundary-spectral-reduction.md#scaled-reflected-parametrix), Sections 31–38. 

<a id="dirichlet-cauchy-endpoints"></a>

## 71. Local dependence in a boundary collar

We now supply the initial-data step for the actual spectral waves in (W11). Fix a smooth positive density $\mu$ on the compact manifold and use it to represent half densities by scalar functions. The differential expression has the form
\[
 \begin{gathered}
 P w=-\operatorname{div}_{\mu}(a\,dw)+b\cdot dw+cw,\\
 e_w=\tfrac12\bigl(|w_t|^2+a(dw,d\overline w)+|w|^2\bigr).
 \end{gathered}
 \tag{T157}
\]
Here $a$ is the real positive principal quadratic form on covectors. Subtracting the displayed divergence operator from $P$ leaves a smooth first-order operator, which defines $b,c$. They may be complex. All these coefficients are time independent. This construction retains every lower term of the given operator.

Let $w\in C^2(I;H^2(X)\cap H_0^1(X))$ satisfy $w_{tt}+Pw=0$. This is the regularity supplied by (W11) with $q=1$, and it will also hold for the difference used below. For a nonnegative real smooth weight $\varphi(t,x)$, put $E_\varphi(t)=\int_X\varphi e_w\,d\mu$. Test the equation against $\varphi w_t$, take real parts, and differentiate the quadratic terms. This is a legitimate weak Dirichlet test: $w_t\in H_0^1$ and smooth multiplication preserves that space. The defining integration-by-parts identity on $H_0^1$ follows from its smooth compactly supported density. Consequently no conormal trace or unproved boundary flux is needed. The exact identity is
\[
 \begin{aligned}
 E_\varphi'(t)&=\int_X \varphi_t e_w\,d\mu\\
 &\quad-\int_X\operatorname{Re}\bigl(a(dw,d\varphi)\overline{w_t}\bigr)\,d\mu\\
 &\quad+\int_X\varphi R_w\,d\mu,\\
 R_w&=\operatorname{Re}
       \bigl(((1-c)w-b\cdot dw)\overline{w_t}\bigr).
 \end{aligned}
 \tag{T158}
\]
The last integrand is bounded above in absolute value by $C\varphi e_w$. This uses only uniform ellipticity and boundedness of the lower coefficients. The time derivatives and products in (T158) are justified in $L^2$ by the stated strong time regularity, so $E_\varphi$ is continuously differentiable.

Choose a smooth nonnegative function $d$ equal to the inward normal coordinate on a fixed collar, with $d=0$ exactly on the boundary and positive elsewhere. It can be continued as a positive constant beyond a slightly larger collar by a smooth cutoff. Choose $\rho>0$ so that $\{d<\rho\}$ lies in the first collar, and choose a constant $V>0$ with $a(dd,dd)\le V^2$ on $X$. Such a constant exists by compactness. Let $\chi$ be smooth, bounded and nondecreasing, zero on $(-\infty,0]$ and strictly positive on $(0,\infty)$; for example $\chi(s)=e^{-1/s}$ for $s>0$ and zero otherwise. For $t\ge0$ set
\[
 \begin{gathered}
 \varphi(t,x)=\chi(\rho-d(x)-Vt),\\
 E_\varphi'(t)\le C E_\varphi(t).
 \end{gathered}
 \tag{T159}
\]
Indeed $\varphi_t=-V\chi'$ and $d\varphi=-\chi'\,dd$. Cauchy–Schwarz for the positive form $a$ gives
$|\operatorname{Re}(a(dw,dd)\overline{w_t})|\le V e_w$.
The first two terms of (T158) therefore have nonpositive sum, proving (T159). The cutoffs need not have small derivatives.

Suppose $w(0)=w_t(0)=0$ on $\{d<\rho\}$. Its weak spatial derivatives also vanish there, so $E_\varphi(0)=0$. Multiplication of (T159) by $e^{-Ct}$ and the ordinary fundamental theorem imply $E_\varphi(t)=0$. Nonnegativity of the energy and strict positivity of $\chi$ on its positive arguments show that $w$ vanishes in the shrinking collar. Apply the same argument to $w(-t)$ for negative time. We have proved
\[
 w(t,x)=0\quad\text{if }d(x)+V|t|<\rho.
 \tag{T160}
\]
Equality first holds almost everywhere in each spatial slice and then as a spacetime distribution, by continuity in time. This proves the local dependence assertion with the actual boundary condition and arbitrary allowed lower terms. It extends the interior local-energy argument in the boundary lesson without using propagation of wavefront sets.

## 72. Compatible collar data give a smooth initial wall neighborhood

Let $v$ be the spectral Dirichlet wave in (W11), and write $F=v(0)$, $G=v_t(0)$. Suppose these functions are smooth on a collar and satisfy $(P^jF)|_{\partial X}=(P^jG)|_{\partial X}=0$ for every nonnegative integer $j$. Equations (W15)–(W18) prove precisely these hypotheses for the inverse-power regularization of compact interior distributions.

Choose a smooth spatial cutoff $\eta$ equal to one on a smaller full boundary collar, supported in the collar where both data are smooth. Define $F_c=\eta F$ and $G_c=\eta G$, extended by zero outside it. They are globally smooth. Since $\eta=1$ on a neighborhood of the whole boundary, every differential iterate there agrees with the corresponding iterate of $F$ or $G$. The exact power-domain theorem, (22) of [Smooth Dirichlet regularity, power domains, and projector growth](smooth-dirichlet-powers.md), therefore gives
\[
 F_c,G_c\in\bigcap_{m\ge0}D(A^m),\qquad A=1+P.
 \tag{T161}
\]
This is an actual compatible extension, not an arbitrary smooth extension of boundary traces.

Let $v_c$ be the spectral wave (W7) with data $F_c,G_c$. For any prescribed time-derivative order and power-domain norm, differentiating its scalar sine and cosine multipliers costs only a fixed power of $a_j$. Equation (T161) supplies every such weighted square sum. The same difference-quotient and dominated-convergence argument as in (W8) proves $v_c\in C^k(I;D(A^m))$ for every $k,m$. The elliptic power estimate and the Fourier Sobolev embedding proved after (22) of that reading give joint smoothness up to the wall: for each finite collection of spatial and time derivatives, choose $m$ sufficiently large, apply the continuous embedding, and use the strong time derivatives in that norm. Thus all mixed derivatives exist and are continuous.

The difference $w=v-v_c$ has the regularity required in Section 71, satisfies the same homogeneous Dirichlet wave equation, and has zero Cauchy data in a full smaller collar. Choose $\rho$ inside that collar. Equation (T160) yields
\[
 \begin{gathered}
 v=v_c\in C^\infty\quad\text{where}\\
 d(x)+V|t|<\rho.
 \end{gathered}
 \tag{T162}
\]
In particular a neighborhood of the entire initial boundary is absent from the compressed singular set of $v$. This conclusion concerns the actual wave for a fixed finite regularization power. It does not require that power to smooth the original data everywhere, nor does it infer spacetime smoothness merely from smooth initial traces.

## 73. A singular interior endpoint must have singular Cauchy data

Fix an interior spatial covector $(z_0,\zeta_0)\ne0$ outside $\operatorname{WF}(F)\cup\operatorname{WF}(G)$. There is a common open conic phase neighborhood on which both data are regular. We prove that neither characteristic lift $(0,z_0,\tau,\zeta_0)$, $\tau=\pm\sqrt{p(z_0,\zeta_0)}$, is a wavefront point of $v$.

Use physical time as the distinguished variable, as in Section 47. In this spectral setting the equation already has no first time derivative, so no gauge is necessary: after multiplication by $-h^2$ it is $((hD_t)^2-h^2P)v=0$. Choose a spacetime cutoff equal to one on a neighborhood of the two short time-root tubes issuing from a compact annular patch around $(z_0,\zeta_0)$. Its time factor is identically one near zero. Write the localized wave as $u$, and its initial data as $F_0,G_0$. They are spatial localizations of $F,G$, remain regular on the chosen patch, and are in $H^2$.

Sections 42–44 apply with $x=t$, $y=z$: the roots $B_\pm$ retain the complete symbol of $-h^2P$ on the tubes, $E_h=(B_+-B_-)^{-1}$ is the exact inverse, and $Q_\pm$ are transported cutoffs with a common initial value $Q_0=\operatorname{Op}_h(q_0)$. All their higher transport corrections have zero initial value. There is no Dirichlet identity between the two modes on this time slice. Instead their exact initial values are
\[
 \begin{aligned}
 V_+(0)&=E_h(0)\bigl(-ihG_0-B_-(0)F_0\bigr),\\
 V_-(0)&=F_0-V_+(0).
 \tag{T163}
\end{aligned}
\]
The strong time traces supplied by (W11) agree with the norm-primitive representatives used for the modes, since the latter are defined by the same bounded operators on $u$ and $hD_tu$.

For every $M$, the finite expansion of $E_h(0)$ in (T104), the finite product formula and the spatial Fourier cutoff estimate (W19) give $\|Q_0V_\pm(0)\|_2=O(h^M)$. To see all the supports and errors, replace $E_h$ to an arbitrarily high finite accuracy. Each finite coefficient of $Q_0E_hB_-$ or $Q_0E_h$ is supported inside the regular initial phase patch; its action on $F_0$ or $G_0$ is rapidly small by (W19). The exact product and inverse remainders are arbitrary powers of $h$ on these fixed finite norms. The term $Q_0F_0$ obeys the same bound. Choose all margins before increasing the accuracy, so the regularity neighborhood is fixed.

The actual localized equation has forcing separated from the retained tubes. Therefore (T108)–(T110), now in physical time, apply to $Z_\pm=Q_\pm V_\pm$ from the initial slice itself. The forcing has any prescribed finite power of $h$, and the factor $h^{-1}$ in the energy inequality is included by choosing one additional power. In either time direction they give, for sufficiently accurate roots and transports,
\[
 \begin{gathered}
 \sup_{|t|\le\delta}\|Q_\pm(t)V_\pm(t)\|_2
       \le C_M h^M,\\
 (0,z_0,\tau,\zeta_0)\notin\operatorname{WF}(v),\\
 \tau=\pm\sqrt{p(z_0,\zeta_0)}.
 \end{gathered}
 \tag{T164}
\]
Here $\delta$ and the inner tubes are independent of $M$. For the second assertion, on the smaller transported tube $Q_\sigma$ is the identity to every requested finite order. A fixed inner cutoff factors through it by the finite product estimate. At its full time root the opposite mode is elliptic by the complementary parametrix in Section 45, applied after localization in an interior time interval. The two modes sum exactly to $u$. The full-frequency reconstruction used in Section 46 then excludes wavefront on a fixed full-phase neighborhood of the root. Noncharacteristic lifts are already excluded by the scalar wave parametrix. All this occurs in spatial interior charts; it uses no extension through the reflecting wall.

Taking the contrapositive, every actual interior characteristic wavefront point of $v$ over $t=0$ projects to $\operatorname{WF}(F)\cup\operatorname{WF}(G)$. Merely restricting a distribution to the initial slice would give the opposite useful inclusion and would not prove this assertion; the mode energy above supplies the required implication.

## 74. Reaching the singular initial data in the exact boundary relation

Let $(t_*,x_*,\tau_*,\xi_*)\in\operatorname{WF}(v)$, with $x_*$ in the interior, for a spectral wave having the compatible smooth collar data of Section 72. The wave equation is elliptic off its characteristic set, so $\tau_*\ne0$ and $\tau_*^2=p(x_*,\xi_*)$. Normalize its scale and fix the sign of $\tau_*$ as in Section 63. The singular-curve construction in Sections 63–69 continues a curve through this point to physical time zero: the equation is homogeneous throughout, the spatial manifold is compact, the normalized energy set is compact, and (T156) gives a nonvanishing time clock. The endpoint still belongs to the closed compressed singular set. This uses the construction inside that set when continuing, rather than attaching an arbitrary geometric curve.

Equation (T162) excludes every boundary endpoint at time zero. The endpoint is consequently an interior full covector $(0,y,\tau_*,\eta)$ in $\operatorname{WF}(v)$. Section 73 implies $(y,\eta)\in\operatorname{WF}(F)\cup\operatorname{WF}(G)$. Restore the original homogeneous scale. Denote by $\mathcal R_{t,\tau}$ the relation of the generalized curves (G1)–(G23) running from physical time zero to time $t$, at the fixed nonzero time covector $\tau$, with their full interior endpoint covectors retained. We have proved
\[
 \begin{gathered}
 (x_*,\xi_*;y,\eta)\in\mathcal R_{t_*,\tau_*},\\
 (y,\eta)\in\operatorname{WF}(F)\cup\operatorname{WF}(G),\\
 p(y,\eta)=\tau_*^2.
 \end{gathered}
 \tag{T165}
\]
The physical-time equations are exactly (G22), hence exactly equation (4) of the boundary lesson. The proof retains gliding, arbitrarily degenerate contacts and accumulation of transverse reflections. It asserts the existence of a suitable singular curve; it does not assert propagation along every possible curve when the relation is nonunique.

## 75. Transfer to all compact interior distributional data

Let $f,g$ be arbitrary distributions with compact support in the spatial interior. As proved before (W7), both belong to fixed-support $H^{-2M}$ for some finite integer $M$. Construct the exact spectral solution $u$ by (W7) and choose a fixed integer $N\ge M+2$. Then $v=A^{-N}u$ satisfies (W11) with $q=1$, and its data satisfy all the collar hypotheses by (W15)–(W18). The elliptic proofs (W21)–(W22) give
\[
 \begin{aligned}
 \operatorname{WF}(v)&=\operatorname{WF}(u),\\
 \operatorname{WF}(v(0))&=\operatorname{WF}(f),\\
 \operatorname{WF}(v_t(0))&=\operatorname{WF}(g).
 \tag{T166}
\end{aligned}
\]
The first equality is in interior spacetime, and the other two are in the spatial interior. Apply (T165) to any interior wavefront point of $u$, using the first equality, then use the last two equalities at its initial endpoint. This proves the third boundary input in the lesson for every stated negative input order, and indeed for every compactly supported interior distribution. The constructed curve has the original full covectors and energy, so no wavefront direction or contact type is lost. All its interior points are wavefront points of $u$ by (T166); the boundary portion is controlled by the compressed singular set of the regularized wave. No pointwise trace of the original negative-order wave is assumed. Its homogeneous Dirichlet condition is the distributional condition already proved in (W12).

This completes the Cauchy-data propagation input for the exact spectral solutions used in the cosine-kernel argument. It does not prove a statement about every unspecified distributional boundary realization, the converse realization of every generalized curve, or the curved spectral-projector remainder. The curved spectral remainder is proved separately in the spectral reading, Sections 31–38.

<a id="uniform-dirichlet-wave-families"></a>
## 76. Uniform regularity for bounded families of actual waves

The spectral application needs bounds that survive a change of scale and of coefficients. Smoothness for each operator separately does not imply such bounds. We prove a uniform statement from the estimates above before using any scaled kernel.

Let \(\omega\) range over a compact finite-dimensional parameter set \(Z\), with coefficients smooth on a neighborhood of \(Z\). On one fixed compact manifold with boundary, let \(P_\omega\) be smooth scalar formally symmetric second-order operators with uniformly positive spatial principal symbols. Use the same boundary collar coordinates for the family, and suppose there the symbols are \(s^2+r_\omega(d,y,\eta)\). The allowed lower terms are retained and have uniform coefficient bounds. Write \(L_\omega=\partial_t^2+P_\omega\). On a fixed open time interval \(I\), consider an arbitrary collection of smooth waves, indexed by \(\iota\):
\[
 \begin{gathered}
 L_\omega u_{\omega,\iota}=0,\qquad
           u_{\omega,\iota}|_{\partial X}=0,\\
 \sup_{\omega,\iota}
       \|u_{\omega,\iota}\|_{H^2(I\times X)}<\infty .
 \end{gathered}
 \tag{T167}
\]
One may use bounded \(H^2\) norms on each larger compact time slab instead. No continuity of the waves in \(\omega\) or \(\iota\) is required. The parameter is an index here, not an extra covector variable. Parameter neighborhoods are relative to the compact set when necessary. The normal gauge (D1)–(D4) is also uniform: its multiplier is the exponential of an integral of the smooth normal first-order coefficient. On a compact collar its derivatives, inverse and finite Sobolev multiplication norms are bounded uniformly. We use that gauge in the local estimates and undo it afterward.

Call \((\omega_0,g_0)\) *uniformly regular* if there are one parameter neighborhood \(V\) and one fixed microlocal cutoff, elliptic near \(g_0\), for which every spatial and time Sobolev seminorm is bounded over \(\omega\in V\) and all \(\iota\). At the wall the initial definition is the tangential pair from Section 60:
\[
 \begin{gathered}
 \|\mathcal B J_y^r u_{\omega,\iota}\|_2\le C_r,\\
 \|\mathcal B J_y^{r-1}D_du_{\omega,\iota}\|_2\le C_r,\\
 r\in\mathbb R,\qquad\omega\in V,\qquad\text{all }\iota .
 \end{gathered}
 \tag{T168}
\]
The letter \(y\) in this pair includes physical time, as in the earlier boundary estimates. All base cutoffs are supported inside the homogeneous time interval. In the interior use a full spacetime cutoff and full Sobolev weights. The normal recurrence (T125), with the actual equation, makes the boundary definition equivalent to uniform microlocal smoothness up to the wall. The same recurrence works for the family because its coefficients and all their finite derivatives are uniformly bounded.

We check why the local propagation implications above hold for this definition. At a reference parameter choose the compact phase neighborhoods, separated cutoffs, strict positivity margins and root gaps used in the corresponding proof. Shrink \(V\) once to preserve those margins and support separations. Flows and their derivatives depend smoothly on the coefficients by the integral-equation proof (G13). A glancing center can also be chosen smoothly: retain its base and tangential direction and adjust its nonzero time frequency using \(\tau^2=r_\omega\). Thus the moving construction has a fixed smaller output neighborhood after shrinking. It is not necessary to keep a reference glancing covector characteristic for every nearby operator.

Here are the norm dependencies in this passage.

- The symbol products, inverses, positivity estimates and separated-support integrations in (N19)–(N23), (T44) and (T72) use only finitely many coefficient and cutoff derivatives at each prescribed order. On the retained neighborhoods their constants are uniform in \(\omega\).
- The lower weighted norm (T77) is bounded by the common \(H^2\) norm in (T167). The original spatial localization forcing is \(h^2[L_\omega,\chi]u_{\omega,\iota}\); its \(L^2\) norm has the same uniform bound. Its separated factors retain arbitrary powers of \(h\) by (T72) and (T78).
- An incoming edge contained in the uniformly regular set has bounds of every required order by (T168), or by its full interior version. On its compact support a finite subcover gives a common parameter neighborhood and finitely many such norms. The Fourier integrations in (T16) and the argument after (T138) therefore bound that edge by \(C_Nh^N\) uniformly in \(\omega,\iota\). The constants previously denoted \(C_{N,u}\) have thereby been replaced by bounded, specified family seminorms.
- The actual Sobolev regularizer is the same Fourier multiplier for every member. Its bounds (T65)–(T78) are uniform in both its regularization parameter and \(\omega,\iota\). The scalable flat weight absorbs its first-order commutator exactly as in (T130)–(T137); for a chosen Sobolev order its size is fixed before the family is considered.

In particular the two-component glancing recovery (T139) has the family form
\[
 \begin{gathered}
 \|Q_{*,h}u_{\omega,\iota,\varepsilon}\|_2^2
       +\|Q_{*,h}hD_du_{\omega,\iota,\varepsilon}\|_2^2\\
 \qquad\leq Ch\mathcal H_{S,h}
                   (u_{\omega,\iota,\varepsilon})^2+C_Nh^N .
 \end{gathered}
 \tag{T169}
\]
Here the larger region has the preceding-order uniform pair norm and the edge has the uniform regularity just specified. The constants are independent of \(\omega,\iota,h,\varepsilon\). This statement retains both components and the larger-weight hypothesis.

Summing on the sequence (T87), using its finite-overlap bounds and then passing to the regularizer limit as in (T74), gives the uniform half-order gain. The order of choices matters. First fix a compact parameter neighborhood on which the flow chart, the strict inequality in (T130), the outer support margins and the incoming-edge regularity all hold. Construct the functions (T129)–(T131) with the moving flow coordinates on this whole neighborhood. For each \(\theta<\theta'<1\), their support inclusion has the positive threshold difference \(\theta'-\theta\), uniformly in the parameter. The resulting open tubes can move with \(\omega\); the reference point has one fixed smaller output neighborhood inside every nearby \(W_0(\omega)\).

Start at the common \(H^2\) bound and run Section 61's simultaneous induction on all these nested tubes. At each step the relevant closed supports in the product of the parameter set and the phase chart are compact. Their finite covers supply the preceding-order bounds uniformly. Higher orders change the finite symbol seminorms and the flat-weight constant, which are allowed to grow with the order; they do not require further shrinking of the parameter set. This proves all orders on the fixed output neighborhood and the same parameter neighborhood, as required in (T168). An intersection of successively shrinking parameter neighborhoods would not suffice.

The elliptic boundary argument (T96)–(T99) is uniform for the same reason: its positive gap and finite coefficient bounds persist. The separated-root and interior mode energies (T104)–(T124) use a fixed positive root gap and bounded evolution coefficients; their forcing and commutator bounds have the uniform norm dependencies above. The strict-diffraction construction has a fixed strict sign at its reference point and the same nested-support induction. Consequently all the local regularity implications used in Sections 63–70 apply to the uniformly regular set. No parameter derivative of a wave has been estimated in this argument.

## 77. Curves of failure of uniform regularity

Let \(F\) be the complement of the uniformly regular set in the product of \(Z\) with the normalized compressed phase charts, and put \(F_{\omega_0}=\{g:(\omega_0,g)\in F\}\). Regularity is open by its definition, so these sets are closed. This includes passage from interior points to the wall: the finite inverse of a fixed tangential cutoff, the normal recurrence and the lower-norm remainders in Section 63 are uniform by Section 76. They exclude all nearby interior characteristic lifts when the boundary point is uniformly regular. The uniform elliptic estimates exclude noncharacteristic points. A nonzero characteristic point has nonzero time covector; normalize it to \(\tau=\pm1\) as before.

Fix \(\omega_0\). If all points of an incoming cylinder (T142) lie outside \(F_{\omega_0}\), then the compact edge of its chosen smaller weight has a finite cover by uniformly regular neighborhoods. Intersect their parameter neighborhoods. The uniform local estimate just proved makes the output regular too. Its contrapositive is exactly the approximate singular step needed in (T145), now for the closed set \(F_{\omega_0}\) and the coefficients of \(P_{\omega_0}\).

At interior, transverse and strict-diffraction points use the corresponding uniform local implications from Section 76. Follow the construction (T143)–(T156) in this fixed slice: concatenate genuine arcs and the approximate glancing steps, use their uniform speed bound, and pass to a compressed limit. Its points stay in \(F_{\omega_0}\), by closedness. The integral tangential equations, energy identity and nonnegative normal reaction are proved by the same limit identities (T148)–(T155), now involving the fixed coefficients \(P_{\omega_0}\). Thus
\[
 \begin{gathered}
 g_0\in F_{\omega_0}
 \ \Longrightarrow\
 \Gamma(t)\in F_{\omega_0},\qquad \Gamma(t_0)=g_0,\\
 \Gamma\text{ satisfies (G1)–(G23) for }P_{\omega_0}.
 \end{gathered}
 \tag{T170}
\]
The curve continues throughout compact homogeneous time slabs by Section 69. The parameter \(\omega_0\) stays fixed along it. This proves a uniform-family statement, not just a separate smoothness assertion for each \(u_{\omega,\iota}\). In particular every point where the whole family vanishes on a common open spacetime neighborhood lies outside \(F\).

## 78. A uniform region with no returning ray

We next verify the geometric condition for a concrete scaled collar. Suppose a boundary coordinate patch contains the Euclidean half-ball of radius \(10\), its center on the wall. At a reference parameter the spatial symbol in this patch is
\(s^2+|\eta|^2\). For nearby parameters it is \(s^2+r_\omega(d,y,\eta)\), with \(r_\omega\) close to \(|\eta|^2\) in \(C^1\) on the normalized frequencies. All lower coefficients may vary smoothly. Set \(a=1/8\). We shall take smooth waves whose two Cauchy data at time zero are supported in \(\{|x|\leq a\}\).

Choose a smooth function \(b\) on \(X\) equal to \(|x|\) for \(a/2\leq|x|\leq8\), at most \(a\) on the small inner ball, and constant outside a slightly larger coordinate half-ball. It can be made nondecreasing in radius with radial derivative at most one: smooth its transitions strictly inside the two indicated margins. For parameters close enough to the reference, \(\sqrt{p_\omega(x,db)}\leq V\) with \(V=5/4\). Outside the chart \(db=0\).

Apply the full-coefficient energy identity (T158) to
\(\varphi(t,x)=\chi(b(x)-a-Vt)\) for \(t\geq0\). Its time derivative is \(-V\chi'\), while the flux is bounded by \(\chi'\sqrt{p_\omega(db)}\,e_u\). Their sum is nonpositive. The initial weighted energy is zero because both data are supported where \(b\leq a\). The same exponential-factor integration as in (T159) and the argument applied to \(u(-t)\) show
\[
 u_{\omega,\iota}(t,x)=0
       \quad\text{if } b(x)>a+V|t|.
 \tag{T171}
\]
All constants and this open zero region are common to the family. The physical boundary term vanishes because the time derivative of the Dirichlet trace is zero. No artificial coordinate boundary is used in this global weighted identity.

For the flat symbol, every generalized ray of unit physical speed unfolds to a straight line. Use increasing spatial Hamilton parameter in (G4): it makes the tangential covector constant and the inward normal covector nondecreasing. Its absolute value is constant by energy. If that value is positive, there is at most one change from its negative to its positive sign; if it is zero, the normal coordinate is constant. These are precisely straight motion and its single wall reflection, including motion tangent to the wall. Physical time is an affine parameter by (G21); either orientation gives the same unfolded segment length. Reflection in the wall preserves the Euclidean norm. Thus a ray through \((t_*,x_*)\), with \(1\leq t_*\leq2\) and \(|x_*|\leq a\), obeys
\[
 |x(-1)|\geq t_*+1-|x_*|
                  \geq 2-a=\tfrac{15}{8}.
 \tag{T172}
\]

This separation persists for all sufficiently close coefficients, with the weaker lower bound \(|x(-1)|>3/2\). Here is a compactness proof that includes accumulating reflections. If not, choose parameters tending to the reference and violating rays. Their physical speeds are uniformly at most two, so the entire interval from \(t_*\) back to \(-1\) stays inside the radius-eight patch: reaching its edge would require displacement at least \(8-a>6\). Pass to a fixed sign of \(\tau\), convergent target positions and times, and parametrize each interval on \([0,1]\) in increasing spatial Hamilton orientation. The bounds (G5)–(G7), with uniform coefficient bounds, give uniformly Lipschitz positions and tangential covectors and bounded variation of the normal covectors.

In this flat limit one can check convergence directly. The tangential equations tend uniformly to constant-covector equations. The normal covector is a bounded nondecreasing function plus a term tending uniformly to zero, since the normal derivative of \(r_\omega\) tends to zero. Extract its values on a countable dense set; monotonicity then gives convergence at every continuity point of the limiting monotone function, hence almost everywhere. Boundedness permits passage through its integrals in the normal position equation. Energy gives the constant absolute normal value almost everywhere, and the reaction is supported on the limiting wall: on any closed interval at positive distance from it, every approximating reaction is constant. The limit is therefore exactly one of the flat rays described above. Its endpoints contradict (T172). This proves the uniform separation without assuming a finite number of reflections.

At time \(-1\), the bound \(3/2>a+V=11/8\) puts every such ray in the common open zero region (T171). This is the required no-return property for the actual nearby metrics.

## 79. The resulting quantitative homogeneous-wave estimate

Choose a compact sufficiently small parameter neighborhood \(Z_0\) on which that geometric separation holds. Apply (T170) to the normalized family of all smooth homogeneous Dirichlet waves with the stated Cauchy support and \(H^2((-3,3)\times X)\) norm at most one. If a point of the compact target set \(1\leq t\leq2,\ |x|\leq a\) failed uniform regularity, its singular curve would reach time \(-1\) in the common zero region. That contradicts (T170) and (T171).

A finite cover of the target's normalized phase directions gives uniform tangential Sobolev bounds of every order; the elliptic directions are covered by the uniform elliptic estimate. The normal recurrence (T125) and the finite half-space extension in Section 54 convert them to ordinary Sobolev bounds on a neighborhood of the target, including the wall. Fourier Cauchy–Schwarz with a Sobolev order greater than the spacetime dimension divided by two plus the desired derivative order gives pointwise bounds there. Compactness in \(\omega\) gives a finite parameter cover as well. Rescaling a nonzero wave by its \(H^2\) norm proves the actual estimate
\[
 \begin{gathered}
 \sup_{\substack{1\leq t\leq2\\ |x|\leq1/8,\ x\in X}}
           |D_{t,x}^{\beta}u_\omega(t,x)|\\
       \leq C_\beta
             \|u_\omega\|_{H^2((-3,3)\times X)},\\
 \omega\in Z_0 .
 \end{gathered}
 \tag{T173}
\]
For a zero norm the wave is zero and the assertion is immediate. This conclusion controls all target derivatives up to the reflecting wall, uniformly over the operators and waves. It uses their actual lower terms and homogeneous Dirichlet condition.

The connection with boundary scaling is explicit. Under
\((d,y)=(\epsilon a,y_0+\epsilon z)\) and \(t=\epsilon s\), the conjugated operator \(\epsilon^2P\) has spatial principal symbol
\[
 \begin{gathered}
 \xi_a^2+\zeta^TG_\epsilon(a,z)\zeta,\\
 G_\epsilon(a,z)=G(\epsilon a,y_0+\epsilon z),\\
 \text{first-order coefficients }O(\epsilon),\\
 \text{zeroth-order coefficients }O(\epsilon^2).
 \end{gathered}
 \tag{T174}
\]
Here the coefficients of each lower differential term include the coordinate half-density convention already used for \(P\). The assertions follow term by term from \(\partial_d=\epsilon^{-1}\partial_a\) and \(\partial_y=\epsilon^{-1}\partial_z\). A fixed linear tangential change makes \(G(0,y_0)\) the identity at a chosen reference point. On a sufficiently small boundary base patch and for small \(\epsilon\), the whole scaled family meets the coefficient hypotheses of Section 78. Finite boundary patches cover a compact wall.

A fixed compact spatial realization can be supplied without an artificial boundary in this patch. Take a long product cylinder whose tangential torus has periods greater than \(100\), and whose normal length is greater than \(100\). Embed the coordinate half-ball of radius \(12\) at one end. In a fixed density, write the formally symmetric operator as its divergence-form principal part plus a formally symmetric first-order part and a potential. Interpolate the positive principal matrices with the identity using a cutoff equal to one on the radius-ten half-ball and zero outside radius eleven. Interpolate the remaining terms using the same cutoff, replacing a first-order term \(B\) by \((\chi B+B^*\chi)/2\) when necessary. This agrees exactly with the scaled operator where \(\chi=1\), preserves formal symmetry and positive principal ellipticity, and has smooth bounded coefficient dependence through \(\epsilon=0\). In the boundary collar the normal principal coefficient stays one and mixed normal terms stay zero.

The energy proof (T158) identifies waves on the common patch whenever their Cauchy data agree and their propagation region stays inside it. Thus this extension provides a setting for (T173); it does not impose a new boundary condition on the physical radius-ten patch. For this step, see also Lemma 17.5.14 and the uniform-operator argument of Section 24.7 in volume III cited above. The argument here tracks the finite norm dependencies and constructs the closed set of failures of uniform regularity explicitly.

Equation (T173) is the quantitative homogeneous-wave input for this scaled family. Sections 80–89 below now prove the rough point-source and coefficient-parameter steps using temporal regularization, resolvents on the common first domain and a joint Fourier estimate. The complete scaled comparison and both curved spectral bounds are proved in [the spectral reading](curved-boundary-spectral-reduction.md#scaled-reflected-parametrix), Sections 31–38. The actual near-normal construction and complementary frozen model (B1)–(B111) remain available and unchanged.

<a id="uniform-rough-dirichlet-columns"></a>
## 80. Uniform power norms on the compact realization

We now extend the no-return estimate to rough source columns, including sources tending to the wall. We retain the coefficient family and geometry of Sections 76–79. Use one fixed smooth density \(\mu\), and suppose the Dirichlet realizations satisfy \(P_\omega\geq\lambda_*I\) for a constant \(\lambda_*>0\). Every spatial derivative below is taken in the fixed coordinate chart, and kernel values are relative to \(\mu\).

This positivity condition is available for the scaled compact extension in Section 79. In its product cylinder of normal length \(L\), the principal form is uniformly positive. The formally symmetric first-order form has coefficients \(O(\epsilon)\); its quadratic value is bounded by \(C\epsilon\|dw\|_2\|w\|_2\). Indeed, writing it as the symmetric part of a first-order expression makes its value the real part of the corresponding first-order pairing. The derivatives of the interpolating cutoff are included in this identity and introduce no additional real potential. The remaining potential is \(O(\epsilon^2)\). Thus
\[
 \begin{gathered}
 \begin{aligned}
 q_\omega(w,w)&\geq c\|dw\|_2^2
       -C\epsilon\|dw\|_2\|w\|_2\\
       &\qquad-C\epsilon^2\|w\|_2^2,
 \end{aligned}\\
 q_\omega(w,w)\geq \tfrac c2\|dw\|_2^2
                            -C'\epsilon^2\|w\|_2^2,\\
 \|w\|_2^2\leq L^2\|\partial_aw\|_2^2 .
 \end{gathered}
 \tag{T175}
\]
The last inequality follows by writing \(w(a,z)=\int_0^a\partial_aw(s,z)\,ds\), applying Cauchy–Schwarz and integrating; density extends it to \(H_0^1\). Shrinking the common range of \(\epsilon\) gives a fixed positive lower bound. The principal matrix may still vary with the boundary base point. This calculation neither adds a potential to the physical operator nor changes it in the retained patch.

Let \(e_{\omega j}\) be the proved orthonormal eigenbasis, with eigenvalues \(\lambda_{\omega j}\), and put \(A_\omega=1+P_\omega\). Set \(a_{\omega j}=1+\lambda_{\omega j}\) and \(\kappa_{\omega j}=\sqrt{\lambda_{\omega j}}\). We use the coefficient spaces of (W3) separately for each parameter:
\[
 \begin{gathered}
 \|c\|_{s,\omega}^2=\sum_j a_{\omega j}^{s}|c_j|^2,\\
 \|w\|_{H^{2q}(X)}
       \leq C_q\|A_\omega^qw\|_2,\qquad
                         w\in D(A_\omega^q).
 \end{gathered}
 \tag{T176}
\]
The constants in the second line are uniform. To check this, use the finite atlas and extension of the smooth Dirichlet reading. Its difference-quotient second-order estimate depends on a positive ellipticity lower bound and finitely many coefficient derivatives. Its higher-order induction uses the same fixed chart cutoffs, the reciprocal normal coefficient, bounded coefficient derivatives and the fixed Sobolev interpolation inequality. All these quantities have common bounds on our compact family. Inducting on the power domain as in its equation (22) therefore gives a uniform bound by \(\|P_\omega^qw\|_2+\|w\|_2\). The spectral inequality \(1+\lambda^q\leq2(1+\lambda)^q\) proves (T176). No continuity of eigenvectors in \(\omega\) is used.

## 81. A uniformly bounded regularized wave

Initially take smooth Cauchy data \(f_\omega,g_\omega\) belonging to every power domain, both supported in the radius-\(a\) half-ball, \(a=1/8\). Smooth functions compactly supported in its interior are examples. Let \(u_\omega\) be their exact spectral wave (W7). An additional arbitrary family index is permitted and is suppressed. Fix an integer \(M\geq0\), and write
\[
 \begin{gathered}
 B_\omega=\|f_\omega\|_{-2M,\omega}
                          +\|g_\omega\|_{-2M,\omega},\\
 \sup_{t\in\mathbb R}\|u_\omega(t)\|_{-2M,\omega}
                                  \leq C B_\omega,\\
 v_\omega=A_\omega^{-N}u_\omega,\qquad N=M+2,\\
 \|v_\omega\|_{H^2((-3,3)\times X)}
                                  \leq C_M B_\omega .
 \end{gathered}
 \tag{T177}
\]
For the second line, the cosine multiplier has absolute value at most one and the sine multiplier divided by \(\sqrt{\lambda}\) has absolute value at most \(\lambda_*^{-1/2}\). For \(0\leq k\leq2\), the \(k\)th time derivatives cost at most \(C a_{\omega j}^{k/2}\). Since \(1-N+M+k/2\leq0\), multiplication by \(A_\omega^{1-N}\) bounds \(\partial_t^ku_\omega\) in \(L^2\) by \(CB_\omega\). Equation (T176) with \(q=1\), followed by time integration, supplies all derivatives in the last line, including the mixed ones. The difference-quotient argument in (W8) justifies the strong derivatives. Each wave here is individually smooth up to the wall; only the displayed finite norm is initially uniform.

The regularized wave still solves the homogeneous Dirichlet equation. Its Cauchy data need not be supported in the small ball. Consequently (T173) cannot be applied directly to \(v_\omega\). We next prove the regularity of \(v_\omega\) in the exterior region that the singular curves reach.

## 82. Temporal regularization in a common zero region

Use the time Fourier convention \(\widehat k(\tau)=\int e^{-ir\tau}k(r)\,dr\). Define
\[
 \begin{gathered}
 k_1(r)=\tfrac12e^{-|r|},\qquad
 k_N=\underbrace{k_1*\cdots*k_1}_{N\ {\rm factors}},\\
 \widehat k_N(\tau)=(1+\tau^2)^{-N},\\
 v_\omega(t)=\int_{\mathbb R}k_N(r)u_\omega(t-r)\,dr .
 \end{gathered}
 \tag{T178}
\]
The Fourier identity for \(k_1\) follows by integrating its two exponential half-lines; the convolution identity follows by absolutely convergent iterated integrals. The last integral converges in \(\mathcal H_\omega^{-2M}\), using (T177) and \(k_N\in L^1\). Pairing with each coefficient functional and using evenness of \(k_N\) multiplies both the sine and cosine terms by \((1+\lambda_{\omega j})^{-N}\). This proves the exact identity with \(A_\omega^{-N}u_\omega\). It is not a local spatial inverse or a cutoff approximation.

The function \(k_N\) is smooth off zero and every one of its derivatives has an exponentially decreasing polynomial bound there. Here are details for the only possible singularity. Inductively \(k_N(r)=e^{-|r|}p_N(|r|)\) for a polynomial \(p_N\). For \(r>0\), split its convolution with \(k_1\) into \(s<0\), \(0<s<r\), and \(s>r\). After taking out \(e^{-r}/2\), the three terms are a constant integral of \(e^{2s}p_N(-s)\), the polynomial integral \(\int_0^r p_N(s)\,ds\), and \(e^{2r}\int_r^\infty e^{-2s}p_N(s)\,ds\). Repeated elementary integration by parts makes the last term a polynomial in \(r\). Evenness supplies \(r<0\). This proves the asserted form and all its off-zero derivative bounds by induction.

Fix a spacetime point in the common open zero region \(b(x)>a+V|t|\) of (T171). Choose a smaller closed half-chart neighborhood \(O\) of that point and a number \(\delta>0\) such that \(u_\omega(t-r,x)=0\) for all \((t,x)\in O\), all \(|r|<2\delta\), and every family member. This is possible by the strict inequality and continuity of \(b\). Choose an even smooth cutoff \(\chi\), equal to one for \(|r|\leq\delta\), supported in \(|r|<2\delta\), and set
\[
 \begin{gathered}
 k_{\rm out}(r)=(1-\chi(r))k_N(r),\\
 |\widehat k_{\rm out}(\tau)|
                    \leq C_\ell(1+|\tau|)^{-\ell}
                    \quad(\ell\geq0).
 \end{gathered}
 \tag{T179}
\]
Every derivative of \(k_{\rm out}\) is in \(L^1\). Repeated integration by parts proves the displayed Fourier estimate for \(|\tau|\geq1\); its \(L^1\) norm treats smaller \(\tau\). Boundary terms at infinity vanish by exponential decay. Thus the estimate follows from the actual convolution function, with no appeal to a spectral smoothing theorem.

Let \(w_{\rm out}=k_{\rm out}*u_\omega\). Its coefficient multipliers are \(\widehat k_{\rm out}(\sqrt{\lambda_{\omega j}})\) times the original wave multipliers. From (T179), for every \(q,k\),
\[
 \begin{gathered}
 \sup_{|t|\leq3}\|A_\omega^q\partial_t^kw_{\rm out}(t)\|_2
                                      \leq C_{q,k,M} B_\omega,\\
 v_\omega=w_{\rm out}\qquad\text{on }O .
 \end{gathered}
 \tag{T180}
\]
Choose \(\ell\geq2(q+M)+k+2\) in (T179) and use the weighted coefficient squares to prove the first line. The same summable bounds and scalar difference quotients prove continuity and differentiation in every power norm. Uniform elliptic regularity (T176) and the explicit Sobolev extension and Fourier embedding in Section 54 turn these bounds into all spacetime derivative bounds up to the wall.

For the second line of (T180), the omitted integrand \(\chi(r)k_N(r)u_\omega(t-r,x)\) is zero on \(O\) by its choice. For our individually smooth waves this is a pointwise identity as well as a distribution identity. Each convolution can also be computed in an arbitrarily high power norm for that fixed wave, so its boundary values cause no exchange-of-limit problem. We have proved uniform smoothness of \(v_\omega\) near every point of the common exterior zero region, when \(B_\omega\leq1\). This conclusion allows sources arbitrarily close to the wall; it uses no interior collar whose width depends on their support.

## 83. The estimate in a negative spectral norm

Apply (T170) to the family of all the regularized waves in (T177) with \(B_\omega\leq1\). Their common \(H^2\) bound is proved, and (T180) supplies their uniform regularity wherever the backward curves reach the exterior region at time \(-1\). The no-return geometry (T172) applies to the same operators, independently of the waves. Thus a failure of uniform regularity in the target would continue to a uniformly regular exterior point, a contradiction.

The finite phase cover, normal recurrence and Sobolev embedding in Section 79 now bound every derivative of \(v_\omega\) on the target, uniformly over this whole unit family. Recover \(u_\omega=A_\omega^Nv_\omega\) using the actual differential expression. Its coefficients and the finitely many derivatives needed for a prescribed output order are uniformly bounded. Scaling the data by \(B_\omega\), with zero data treated separately, gives
\[
 \begin{gathered}
 \sup_{\substack{1\leq t\leq2\\ |x|\leq1/8,\ x\in X}}
             |D_{t,x}^{\beta}u_\omega(t,x)|\\
 \qquad\leq C_{M,\beta}
       \bigl(\|f_\omega\|_{-2M,\omega}
                       +\|g_\omega\|_{-2M,\omega}\bigr).
 \end{gathered}
 \tag{T181}
\]
This estimate is first proved for the smooth compatible data supported in the radius-\(1/8\) half-ball. It extends by completion to any limit of such data in the displayed coefficient norm: apply it to differences. Completeness in every target derivative norm gives the smooth limit on the target. Equation (W8) identifies that limit with the spectral wave as a distribution, so this extension does not select a different solution. We will construct precisely the required source-column limits next.

## 84. Evaluation and its derivatives at a moving source point

Let \(|y|\leq1/16\) in the closed source half-ball and let \(\alpha\) be a spatial multi-index. Define the coefficient functional \(F_{\alpha,y}\) by
\[
 \begin{gathered}
 (F_{\alpha,y})_j
             =\partial_y^\alpha\overline{e_{\omega j}(y)},\\
 2M>n/2+|\alpha|\\
       \Longrightarrow\quad
       \|F_{\alpha,y}\|_{-2M,\omega}\leq C_{M,\alpha}.
 \end{gathered}
 \tag{T182}
\]
To prove the bound, let \(\phi\) be a finite eigenfunction sum. The explicit Sobolev extension and Fourier Cauchy–Schwarz give
\(|\partial^\alpha\phi(y)|\leq C\|\phi\|_{H^{2M}}\), uniformly on the closed chart. Equation (T176) bounds this by \(C\|A_\omega^M\phi\|_2\). Taking the finite coefficient vector \(\phi_j=a_{\omega j}^{-2M}(F_{\alpha,y})_j\) makes the squared coefficient sum on the left of the resulting inequality equal to its pairing with \(F_{\alpha,y}\). Hence its square root is at most \(C\). Increasing the finite index set proves (T182), exactly as in (W6). This is a statement about the spectral anti-dual. For \(\alpha=0\) at the wall it is the zero functional, since every eigenfunction has zero trace.

We verify that these functionals are limits of the supported smooth data used in (T181). Write \(d\mu(z)=\rho(z)\,dz\) in the chart. Choose a nonnegative smooth mollifier \(\varrho\), supported in the unit ball with integral one, and put \(\varrho_\eta(z)=\eta^{-n}\varrho(z/\eta)\). Translate its center inward to \(y_\eta=y+3\eta e_n\). For sufficiently small \(\eta>0\), its support is in the spatial interior and in \(|z|<1/8\). Define
\[
 \begin{gathered}
 f_{\eta,\alpha,y}(z)
   =\frac{(-1)^{|\alpha|}}{\rho(z)}
              \partial_z^\alpha\varrho_\eta(z-y_\eta),\\
 \langle f_{\eta,\alpha,y},\phi\rangle
   =\int\varrho_\eta(z-y_\eta)
                          \partial_z^\alpha\overline{\phi(z)}\,dz .
 \end{gathered}
 \tag{T183}
\]
The second line follows by ordinary integration by parts on its interior compact support and fixes both the sign and the density factor. These data are in every Dirichlet power domain because all iterates remain compactly supported in the interior.

Choose now \(2M>n/2+|\alpha|+1\), and abbreviate \(E_\eta=f_{\eta,\alpha,y}-F_{\alpha,y}\). The Sobolev estimate with one additional derivative and the mean-value theorem give, for every finite eigenfunction sum,
\[
 \begin{gathered}
 |\langle E_\eta,\phi\rangle|
                 \leq C\eta\|A_\omega^M\phi\|_2,\\
 \|E_\eta\|_{-2M,\omega}
                                                   \leq C\eta .
 \end{gathered}
 \tag{T184}
\]
Indeed all sampled points lie within \(4\eta\) of \(y\), and their joining segments stay in the closed half-chart. The second line follows by the same finite-coefficient duality argument as in (T182). The constants are uniform in the source point and in \(\omega\). This proves convergence even when \(y\) lies on the wall.

The same argument supplies source differentiation without differentiating eigenvectors in the operator parameter. For fixed \(\omega\), Taylor's integral remainder applied to \(\partial^\alpha\overline{\phi(y)}\), and then coefficient duality, proves
\(\|F_{\alpha,y+h}-F_{\alpha,y}-\sum_\ell h_\ell F_{\alpha+e_\ell,y}\|_{-2M,\omega}\leq C|h|^2\)
when \(2M>n/2+|\alpha|+2\). Here the segment remains in the half-chart. Bounds of one lower order give continuity of \(F_{\alpha+e_\ell,y}\) in a sufficiently negative space. Repeating this reasoning proves all source derivatives, interpreted one-sided at the wall. Each prescribed order may use a larger \(M\); (T181) is available for every such \(M\).

The radius \(1/16\) merely leaves a margin for the mollifiers. The same proof applies to any fixed closed source ball of radius less than \(1/8\). In particular source differentiation at the outer edge of the displayed ball can use a slightly larger ball; it does not differentiate through an unsupported source cutoff.

## 85. The actual local wave kernels, uniformly up to both walls

Define the cosine and sine kernels initially as spectral distributions:
\[
 \begin{aligned}
 C_\omega(t,x,y)
   &=\sum_j\cos(t\kappa_{\omega j})\\
   &\qquad{}\times e_{\omega j}(x)\overline{e_{\omega j}(y)},\\
 S_\omega(t,x,y)
   &=\sum_j\frac{\sin(t\kappa_{\omega j})}{\kappa_{\omega j}}\\
   &\qquad{}\times e_{\omega j}(x)\overline{e_{\omega j}(y)}.
 \end{aligned}
 \tag{T185}
\]
These expressions do not assert pointwise convergence of the unsmoothed series. Their column meaning is (W7) with data \(F_{0,y},0\), or \(0,F_{0,y}\), justified by (T182). On interior test functions this agrees with the original spectral calculus by (W4). More explicitly, integrating the columns against a smooth source test in the small ball gives that test's eigenfunction coefficients and hence its exact cosine or sine wave. Coefficient Cauchy–Schwarz justifies the integration in the negative norm. This identifies the distribution kernel relative to \(\mu\).

Apply (T181) to the mollified data (T183). Estimate (T184), applied to differences, makes the resulting waves converge in every target derivative norm on compact target rectangles. Their distributional limit is the corresponding spectral column. Taking the data \(f_{\eta,\alpha,y},0\), or \(0,f_{\eta,\alpha,y}\), supplies its \(\alpha\)th source derivative. The Taylor bound after (T184), combined with (T181), proves that these are actual derivatives of the kernel as maps into each target derivative space. Continuity in the source point in those same norms proves joint continuity of every mixed derivative. Abbreviate \(\mathcal D=\partial_t^k\partial_x^\beta\partial_y^\alpha\). For either kernel \(K_\omega=C_\omega\) or \(S_\omega\), we have
\[
 \begin{gathered}
 \sup_{\substack{1\leq t\leq2\\ |x|\leq1/8,\ |y|\leq1/16\\
                              x,y\in X}}
                |\mathcal D K_\omega(t,x,y)|
     \leq C_{k,\alpha,\beta}.
 \end{gathered}
 \tag{T186}
\]
All target and source normal derivatives here have continuous limits at their respective walls. At zeroth source order both kernels vanish on the source wall, as already noted after (T182); they vanish on the target wall by the Dirichlet condition and convergence. The bound is uniform in the operator parameter but estimates no derivative in that parameter.

For later localization the same conclusions hold on a neighborhood of the closed set in (T186). To check the geometric margin explicitly, enlarge the time interval to \(7/8\leq t\leq17/8\), the target radius to \(3/16\), and the source radius to \(3/32<1/8\). The flat backward endpoint distance is at least \(27/16>3/2\); all these rays still stay inside radius eight before time \(-1\). The compactness argument in Section 78 therefore preserves separation from the same exterior support radius \(11/8\), after one further fixed parameter shrink. Sections 81–85 apply unchanged. Thus compact smooth cutoffs can be one on the entire original target and supported inside this larger region.

See also the rough-input clause of Lemma 17.5.14 and Section 24.7 in volume III. The temporal convolution, its exterior smoothness, the uniform evaluation functionals and the interior mollifier limits supply the programme proof of that step for these kernel columns. The following sections prove coefficient-parameter regularity as well, using weak resolvent estimates and a Fourier argument.

## 86. Parameter derivatives on the common first domain

Write \(\omega\in\mathbb R^p\) in a fixed parameter chart. The exact first Dirichlet domain is
\(D=H^2(X)\cap H_0^1(X)\) for every \(P_\omega\), by the smooth Dirichlet proof. Its higher power domains may vary; they will not be differentiated. The map \(\omega\mapsto P_\omega\) is smooth as a map from \(D\) to \(L^2(X,\mu)\). This follows term by term from the product rule and smooth coefficient dependence on the compact manifold.

For real \(\tau\), put
\[
 \begin{gathered}
 s=1+i\tau,\qquad z=-s^2,\\
 R_\omega(\tau)=(P_\omega+s^2)^{-1},\\
 \|R_\omega(\tau)\|_{L^2\to L^2}\leq C\langle\tau\rangle^{-1},\\
 \|R_\omega(\tau)\|_{L^2\to D}\leq C\langle\tau\rangle .
 \end{gathered}
 \tag{T187}
\]
Here \(D\) has the fixed \(H^2\) norm. If \(|\tau|\geq1\), then \(|\operatorname{Im}z|=2|\tau|\), which bounds the distance to the real spectrum. If \(|\tau|\leq1\), then \(\operatorname{Re}z\leq0\) and \(\lambda_{\omega j}\geq\lambda_*\). The spectral coefficient formula proves the first norm estimate in both regions. Since \(P_\omega R_\omega=I-s^2R_\omega\), the uniform second-order estimate proves the second.

The identity
\[
 \begin{gathered}
 \partial_{\omega_\ell}R_\omega
       =-R_\omega(\partial_{\omega_\ell}P_\omega)R_\omega,\\
 \|\partial_\omega^\alpha R_\omega(\tau)\|_{L^2\to L^2}
                         \leq C_\alpha\langle\tau\rangle^{|\alpha|-1},\\
 \|\partial_\omega^\alpha(sR_\omega(\tau))\|_{L^2\to L^2}
                         \leq C_\alpha\langle\tau\rangle^{|\alpha|}
 \end{gathered}
 \tag{T188}
\]
is justified on this common first domain. At each fixed \(\tau\), factor
\(P_\omega+s^2=I+(P_\omega-P_{\omega_0})R_{\omega_0}\).
The first bracket is inverted by its norm-convergent geometric series for \(\omega\) sufficiently close to \(\omega_0\). The usual difference quotient of the inverse identity then gives the first line in operator norm, with values in \(D\) before multiplication by \(P_\omega'\). Repeated product differentiation gives finite sums of ordered products
\(R_\omega P_\omega^{(\beta_1)}R_\omega\cdots P_\omega^{(\beta_\ell)}R_\omega\), where every \(|\beta_j|\geq1\), \(\sum|\beta_j|=|\alpha|\), and \(\ell\leq|\alpha|\). Each factor \(P_\omega^{(\beta_j)}R_\omega:L^2\to L^2\) is bounded by \(C\langle\tau\rangle\), by (T187). The leftmost resolvent costs \(C\langle\tau\rangle^{-1}\). This proves the last two lines, including \(\alpha=0\). The local inverse neighborhoods may depend on \(\tau\); the displayed derivative bounds are uniform on the fixed compact coefficient family and are what is needed below.

## 87. Weak parameter bounds for the exact kernels

Let \(H(t)\) be one for \(t>0\) and zero for \(t<0\). Write \(\mathsf C_\omega(t)=\cos(t\sqrt{P_\omega})\) and \(\mathsf S_\omega(t)=\sin(t\sqrt{P_\omega})/\sqrt{P_\omega}\) for the operators whose kernels are \(C_\omega,S_\omega\). The elementary Laplace integrals of each spectral multiplier give
\[
 \begin{aligned}
 \mathcal F_t\!\left(e^{-t}H(t)\mathsf C_\omega(t)\right)
                                      &=sR_\omega(\tau),\\
 \mathcal F_t\!\left(e^{-t}H(t)\mathsf S_\omega(t)\right)
                                      &=R_\omega(\tau).
 \end{aligned}
 \tag{T189}
\]
The time integrals converge strongly on \(L^2\), since the undamped operators have uniformly bounded norms and \(e^{-t}\) is integrable on the positive half-line. Finite spectral sums give the identities first; their uniformly bounded multiplier limits give them on every \(L^2\) vector. Conversely the programme Fourier inversion on smooth rapidly decreasing tests identifies these transforms as operator-valued distributions. By (T188), differentiating in \(\omega\) under such a test integral is justified to any finite order: choose its Fourier decay larger than the polynomial derivative bound. Difference quotients and their integral remainders then prove smooth parameter dependence in this weak distribution sense.

Choose compact smooth cutoffs in the larger region described after (T186), and write
\(Z_\omega(t,x,y)=\chi(t)a(x)b(y)K_\omega(t,x,y)\), where \(K=C\) or \(S\). The cutoffs are one on smaller retained sets; \(\chi\) is supported in positive time. Flatten the two spatial boundary charts and extend \(Z_\omega\) by zero in their outward normal directions and beyond their artificial chart edges. Call the resulting Euclidean distribution \(Z_\omega^0\).

For every parameter multi-index \(\alpha\), its full Fourier transform satisfies
\[
 \left|
   \partial_\omega^\alpha
        \widehat{Z_\omega^0}(\sigma,\xi,\eta)
 \right|
          \leq C_\alpha\langle\sigma\rangle^{|\alpha|}.
 \tag{T190}
\]
Here \(\sigma\) is dual to time, and \(\xi,\eta\) to the two spatial points. To verify the spatial part of this assertion, pair the operator on the right of (T189) with the two chart exponentials multiplied by \(a,b\). Their \(L^2\) norms are bounded independently of \(\xi,\eta\). The smooth density factors converting \(\mu\) to coordinate Lebesgue measure are included in these cutoffs, so the pairing is exactly the spatial Fourier transform of the localized kernel. Cauchy–Schwarz and (T188) give a bound \(C_\alpha\langle\tau\rangle^{|\alpha|}\). Multiplying the damped causal kernel by \(\chi(t)e^t\) convolves this expression with a rapidly decreasing time Fourier transform. The inequality
\(\langle\tau\rangle^r\leq C_r\langle\sigma\rangle^r\langle\sigma-\tau\rangle^r\)
and an absolutely convergent integral prove (T190).

This argument also defines the zero extension without a boundary distribution ambiguity: time testing gives a bounded \(L^2\) operator. On the no-return region its kernel agrees on interior tests with the smooth function already proved in Section 85. The localized integral operator with that smooth kernel is bounded on \(L^2\). Density of interior smooth functions in \(L^2(X)\) therefore identifies the two on all spatial tests, including those nonzero at the wall.

Put \(d=1+2n\), the total number of spacetime kernel variables. By direct radial integration of (T190),
\[
 \begin{gathered}
 m_\alpha>|\alpha|+d/2\\
 \Longrightarrow\quad
 \|\partial_\omega^\alpha Z_\omega^0\|_{H^{-m_\alpha}(\mathbb R^d)}
                                                   \leq C_\alpha .
 \end{gathered}
 \tag{T191}
\]
Indeed the integrand in its squared Fourier norm is bounded by a constant times
\(\langle(\sigma,\xi,\eta)\rangle^{-2m_\alpha+2|\alpha|}\), which is integrable. The weak parameter derivatives in this formula are the derivatives of the actual kernel. No differentiable choice of eigenbasis and no assertion about a common higher power domain has been used.

## 88. From weak parameter derivatives to joint smoothness

We give the Fourier step, including the physical boundary extension. Fix an integer \(q\geq1\). For either normal coordinate use the finite reflection extension with moment equations (6) of the smooth Dirichlet reading, matching derivatives through order \(q-1\). In terms of a zero-extended function \(w^0\), its formula is
\(w^0(x_n)+\sum_{j=1}^q c_jw^0(-j x_n)\), with tangential variables unchanged. On the positive half-space the reflected terms vanish, and on the negative half-space they give the usual extension. Every reflection and dilation is bounded on each fixed full-space Sobolev space, including negative integer orders: its Fourier transform is the inverse-determinant factor times the transform at the inverse transpose linear map, and the corresponding polynomial weights are comparable. Thus this formula also defines a bounded linear operator on \(H^{-m}\) distributions. Apply it in both normal coordinates and denote the resulting operator by \(E_q\).

On the smooth localized kernel of Section 85 this is precisely the ordinary extension on the product of the two half-charts. The moment equations remove the boundary terms in weak derivatives through order \(q\), one coordinate at a time. Its \(H^q\) norm is bounded by finitely many of the uniform derivative norms already proved. On the other hand, (T191) remains valid after \(E_q\), since \(E_q\) is a finite sum of those fixed linear pullbacks. In particular it commutes with weak parameter differentiation. This simultaneously supplies positive spatial norms and weak parameter norms for the same extension.

Choose a smooth compact parameter cutoff \(\rho\), equal to one near a selected retained parameter point, and put \(F(\omega,z)=\rho(\omega)E_qZ_\omega^0(z)\). For any prescribed positive integer \(l\), choose an integer \(m>2l+d/2\) and then take \(q=m+2l\). Equations (T186) and (T191), applied also to the derivatives of \(\rho\), give
\[
 \begin{gathered}
 I_w=\int\langle\zeta\rangle^{4l}
          \langle\nu\rangle^{-2m}
                  |\widehat F|^2<\infty,\\
 I_s=\int\langle\nu\rangle^{2q}
                  |\widehat F|^2<\infty .
 \end{gathered}
 \tag{T192}
\]
Here \(\zeta\) is dual to the \(p\) parameter variables, \(\nu\) to the \(d\) physical variables, and the Fourier transform is in all variables. The first line is Plancherel for all weak parameter derivatives through order \(2l\), with values in \(H^{-m}\); the integer weight is bounded by their finite sum of monomial weights. Hilbert-valued Plancherel here follows by applying scalar Plancherel to finite orthonormal projections and increasing those projections in the squared norm. The second line is Plancherel for the \(H^q\) spatial norm integrated over the compact parameter support. Both integrals have bounds independent of the particular retained parameter point when its cutoff belongs to a fixed finite cover.

Cauchy–Schwarz gives the exact intermediate estimate
\[
 \begin{gathered}
 \int\langle\zeta\rangle^{2l}\langle\nu\rangle^{2l}
                              |\widehat F|^2\\
 \qquad\leq I_w^{1/2}I_s^{1/2}.
 \end{gathered}
 \tag{T193}
\]
All integrals here are over both frequency variables. Since
\(\langle(\zeta,\nu)\rangle^{2l}\leq
\langle\zeta\rangle^{2l}\langle\nu\rangle^{2l}\),
this proves \(F\in H^l(\mathbb R^{p+d})\). To obtain continuous derivatives through any specified order \(r\), choose \(l>r+(p+d)/2\). Weighted Fourier Cauchy–Schwarz then makes every Fourier multiplier of order at most \(r\) integrable, and dominated Fourier inversion gives those continuous derivatives with their uniform bounds. This is the same elementary embedding proof used in Section 54, now in the joint variables.

The extension order \(q\) may change with the requested derivative order. Each extension agrees with the same kernel on the physical quadrant, where \(\rho=1\), so its derivatives and their boundary limits there agree. Consequently the physical kernel is jointly smooth in the parameters, time, source and target up to both walls. A finite parameter and coordinate cover gives the corresponding uniform bounds on the retained compact sets. If a scaling parameter is initially restricted to a closed half-interval, take its smooth coefficient extension to an open interval; positivity persists after shrinking by (T175). Restriction gives the asserted one-sided derivatives at its endpoint.

## 89. Full parameter regularity of the no-return kernel

Combining the preceding arguments, for every \(\gamma,k,\alpha,\beta\), with \(\mathcal D\) as in (T186) and \(K=C\) or \(S\),
\[
 \begin{gathered}
 \sup_{\substack{\omega\in Z_0,\ 1\leq t\leq2\\
                   |x|\leq1/8,\ |y|\leq1/16\\ x,y\in X}}
          |\partial_\omega^\gamma\mathcal D K_\omega(t,x,y)|
       \leq C_{\gamma,k,\alpha,\beta}.
 \end{gathered}
 \tag{T194}
\]
These are the actual Dirichlet wave kernels for the nearby compact realizations. The bounds include the zero scaling endpoint of (T174), after its fixed compact extension, and all normal source and target derivatives. Coefficient derivatives are obtained from resolvents on the common first domain and the joint Fourier estimate, not by assuming that derivatives of smooth families are automatically uniformly smooth.

This supplies the rough-column and parameter-regularity input for a scaled wave-kernel construction. The complete scaled comparison and both curved spectral bounds are proved in [the spectral reading](curved-boundary-spectral-reduction.md#scaled-reflected-parametrix), Sections 31–38. The source and target radii are auxiliary neighborhoods inside that construction and do not narrow the original curved spectral theorem. All alternative proofs (B1)–(B111) remain preserved.
