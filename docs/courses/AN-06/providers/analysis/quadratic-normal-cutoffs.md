# Quadratic normal division and Dirichlet phase cutoffs

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="quadratic-normal-cutoffs"></a>

A boundary multiplier may need to distinguish the two normal directions. A tangential cutoff cannot do that. This reading proves the smooth division that replaces a general normal-frequency cutoff, on a scalar quadratic characteristic set, by a polynomial of degree one in normal frequency. It includes the double-root point, smooth parameters and the region without real normal roots. We then construct a multiplier with an exactly nonnegative Dirichlet boundary form and retain its complete forcing identity.

Read [Dirichlet commutators and a local diffraction estimate](dirichlet-commutator-and-diffraction.md#dirichlet-green-commutator), [the finite tangential products and weak traces](real-normal-root-trace.md#real-root-cutoff-products), and [the finite scalar calculus](classical-scalar-calculus.md#finite-scalar-calculus) first. The smooth sums below are justified directly, using the elementary fundamental theorem and uniform derivative convergence already used in that calculus. No preparation or division theorem is assumed.

For further reading, see Victor Ivrii's [*Microlocal Analysis, Sharp Spectral Asymptotics and Applications*, author version of July 9, 2023](https://www.math.utoronto.ca/ivrii/Victor_Ivrii_Microlocal_Analysis,_Sharp_Spectral_Asymptotics_and_Applications.pdf), Section 3.4: printed pp. 260–266, especially the normal polynomial reduction in (3.4.35)–(3.4.42) and the two-root formulas near (3.4.53)–(3.4.56).

<a id="quadratic-even-root"></a>

## 1. Even functions at a double root

Let $z$ range over a fixed relatively compact parameter neighborhood. All estimates may be taken on a slightly smaller such neighborhood. If $E(z,\rho)$ is smooth and even in $\rho$, then

\[
 e(z,R)=E(z,\sqrt R),\qquad R\geq0,
 \tag{C1}
\]

is smooth up to $R=0$, including all parameter derivatives. Here and below smoothness on a closed half interval means that every one-sided derivative is continuous there.

To prove this without differentiating a singular square root at zero, use evenness and the fundamental theorem:

\[
 \frac{\partial_\rho E(z,\rho)}{2\rho}
     =\frac12\int_0^1\partial_\rho^2E(z,t\rho)\,dt.
 \tag{C2}
\]

The right side is smooth and even, also at $\rho=0$. Apply this same operation repeatedly to the resulting even functions. Away from zero it is exactly differentiation in $R$ in (C1). At zero the continuous limit is the corresponding one-sided derivative: integrate the proposed continuous derivative from zero and use the fundamental theorem on $R>0$, then let its lower endpoint tend to zero. Induction proves every order. Parameter derivatives commute with the integrals on their compact domains. Each $k$th $R$ derivative is bounded by a constant times finitely many $\rho$ derivatives through order $2k$ on the same interval.

Taylor's formula, or applying this operation to each even Taylor monomial, gives

\[
 \partial_R^ke(z,0)
       =\frac{k!}{(2k)!}\partial_\rho^{2k}E(z,0).
 \tag{C3}
\]

The same argument applies when other variables, such as an additional normal frequency, are included among the parameters. These uniform derivative bounds will control the divided difference below.

<a id="quadratic-jet-extension"></a>

## 2. A smooth extension with prescribed one-sided derivatives

We will need to extend a smooth function $e(z,R)$ from $R\geq0$ across zero. We give the actual construction. Write

\[
 e_j(z)=\frac1{j!}\partial_R^je(z,0).
 \tag{C4}
\]

Fix a smooth compactly supported scalar function $\theta$, equal to one near zero, using the earlier [smooth cutoff construction](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs). For $R\leq0$, set

\[
 e_-(z,R)=\sum_{j\geq0}
                 e_j(z)R^j\theta(R/\varepsilon_j).
 \tag{C5}
\]

Choose positive $\varepsilon_j\downarrow0$ as follows. For $j\geq1$, make the supremum of every derivative $\partial_R^k\partial_z^\alpha$ of the $j$th summand at most $2^{-j}$ whenever $k+|\alpha|\leq j-1$. This is possible simultaneously for that finite set of derivatives: differentiating the cutoff costs at most $\varepsilon_j^{-k}$, whereas $|R|^j\leq C_j\varepsilon_j^j$ on its support, so the resulting bound is $C_{j,k,\alpha}\varepsilon_j^{j-k}$. The exponent is positive. The coefficients and their derivatives are bounded on the compact parameter set. Also require $\varepsilon_j<\varepsilon_{j-1}/2$.

For any fixed derivative order, the tail of (C5) and all derivatives of that order converge uniformly by the geometric majorant. The finitely many initial terms are smooth. Repeated use of the fundamental theorem identifies the limits as derivatives, proving smoothness through $R=0$ from the left. At zero the $k$th derivative of the $j$th term is zero unless $j=k$, since $\theta=1$ near zero; the exceptional value is $k!e_k(z)$. Thus every derivative, including parameter derivatives, matches the one-sided jet of $e$. Gluing $e_-$ to $e$ gives a smooth extension. Matching continuous derivatives across zero again proves joint smoothness by the fundamental theorem along coordinate segments. This is a local construction on the retained parameter neighborhood and is all that is needed here.

<a id="quadratic-two-root-quotient"></a>

## 3. The two real roots and their quotient

Let $q(z,s)$ be any smooth scalar function for $s$ near zero, with the same compact parameter convention. Introduce an independent real variable $R$. For $R\geq0$ put $\rho=\sqrt R$ and define

\[
 \begin{aligned}
 a_+(z,R)&=\tfrac12\bigl(q(z,\rho)+q(z,-\rho)\bigr),\\
 b_+(z,R)&=\frac{q(z,\rho)-q(z,-\rho)}{2\rho}.
 \end{aligned}
 \tag{C6}
\]

The value of the second expression at zero is $\partial_sq(z,0)$. Indeed

\[
 b_+(z,R)=\frac12\int_{-1}^1
                         \partial_sq(z,t\sqrt R)\,dt.
 \tag{C7}
\]

Both functions in (C6) are even smooth functions of $\rho$ before the substitution. Sections 1–2 give smooth extensions $a(z,R),b(z,R)$ to both signs of $R$.

For $R\geq0$ the exact remainder has a useful nonsingular expression:

\[
 \begin{aligned}
 \mu_+(z,s,R)
  =\int_0^1\int_0^{1-t}
   q_{ss}\bigl(z,ts+v\rho-(1-t-v)\rho\bigr)\,dv\,dt.
 \end{aligned}
 \tag{C8}
\]

It satisfies

\[
 q(z,s)=a_+(z,R)+s b_+(z,R)
                              +(s^2-R)\mu_+(z,s,R).
 \tag{C9}
\]

Here is an explicit verification. When $\rho\ne0$ and $s\ne\pm\rho$, integrate first in $v$, then in $t$. The result is

\[
 \frac1{2\rho}\left(
 \begin{aligned}
 \frac{q(z,s)-q(z,\rho)}{s-\rho}
 \\[-2pt]
 {}-\frac{q(z,s)-q(z,-\rho)}{s+\rho}
 \end{aligned}\right),
 \tag{C10}
\]

which is the quotient in (C9) by direct multiplication. Continuity of the integrand proves the identity also at repeated nodes. Interchanging $v$ and $1-t-v$ shows that (C8) is even in $\rho$. Section 1 therefore proves its joint smoothness in $(z,s,R)$ up to $R=0$. In particular $\mu_+(z,0,0)=q_{ss}(z,0)/2$. No division by the distance between merging roots is left in this formula.

<a id="quadratic-smooth-division"></a>

## 4. The region with no real roots and exact smooth division

For $R<0$, use the extensions from Section 2 and define

\[
 \mu_-(z,s,R)
      =\frac{q(z,s)-a(z,R)-s b(z,R)}{s^2-R}.
 \tag{C11}
\]

The denominator is positive. The only remaining issue is joint smoothness as $(s,R)\to(0,0)$, since smoothness across $R=0$ with $s\ne0$ follows directly from the nonzero denominator and the matching jets. We now verify that issue at every derivative order.

Write $q_j(z)=\partial_s^jq(z,0)/j!$. For an integer $J\geq1$, divide the Taylor polynomial $\sum_{j=0}^{2J+1}q_j(z)s^j$ by $s^2-R$. The elementary identities

\[
 \begin{aligned}
 s^{2j}&=R^j+(s^2-R)
               \sum_{\ell=0}^{j-1}R^\ell s^{2(j-1-\ell)},\\
 s^{2j+1}&=sR^j+(s^2-R)s
               \sum_{\ell=0}^{j-1}R^\ell s^{2(j-1-\ell)}
 \end{aligned}
 \tag{C12}
\]

follow by telescoping; the sums are empty for $j=0$. Denote the resulting polynomial quotient by $M_J(z,s,R)$ and the two remainder coefficients by

\[
 \begin{aligned}
 A_J(z,R)&=\sum_{j=0}^Jq_{2j}(z)R^j,\\
 B_J(z,R)&=\sum_{j=0}^Jq_{2j+1}(z)R^j.
 \end{aligned}
 \tag{C13}
\]

Equations (C3), (C6) and (C7) show that $a-A_J$ and $b-B_J$ have zero $R$ derivatives through order $J$ at zero. The extensions retain these exact derivatives. Taylor's formula with integral remainder on each side of zero therefore writes

\[
 \begin{aligned}
 a-A_J&=R^{J+1}\alpha_J(z,R),\\
 b-B_J&=R^{J+1}\beta_J(z,R),
 \end{aligned}
 \tag{C14}
\]

with smooth bounded coefficients and any fixed finite number of their derivatives on a smaller neighborhood. Also $q-\sum_{j=0}^{2J+1}q_js^j=s^{2J+2}F_J(z,s)$ with a smooth remainder. Substitution in (C11) gives

\[
 \begin{aligned}
 \mu_- -M_J
 &=\frac{s^{2J+2}F_J}{s^2-R}
       -\frac{R^{J+1}\alpha_J}{s^2-R}\\
 &\quad-\frac{sR^{J+1}\beta_J}{s^2-R}.
 \end{aligned}
 \tag{C15}
\]

For $R<0$, let $\delta=(s^2+|R|)^{1/2}$. Differentiating the reciprocal denominator gives the bound $C_{k,l}\delta^{-2-k-2l}$ for $\partial_s^k\partial_R^l(s^2-R)^{-1}$. Indeed each derivative is a finite sum of terms $C s^a(s^2-R)^{-b}$ with $2b-a=2+k+2l$. Differentiation in $s$ replaces a term by multiples with exponents $(a-1,b)$ and $(a+1,b+1)$; differentiation in $R$ replaces them by $(a,b+1)$. Terms with a zero coefficient are omitted, so $a\geq0$. This proves the relation by induction. Since $|s|\leq\delta$ and $s^2-R=\delta^2$, it gives the asserted bound. The numerator and its derivatives have weighted order at least $2J+2$, by (C15) and the product rule. Consequently, for any fixed indices with $k+2l\leq2J$,

\[
 |\partial_z^\alpha\partial_s^k\partial_R^l
                      (\mu_- -M_J)|
           \leq C_{J,k,l,\alpha}\delta^{2J-k-2l}.
 \tag{C16}
\]

There is a matching bound from $R\geq0$, with $\delta_+=(s^2+R)^{1/2}$. Apply (C8) to the Taylor remainder $s^{2J+2}F_J$. Its second derivative, and each further derivative of total order $k+2l$, are bounded by $C\delta_+^{2J-k-2l}$ on the convex hull of $s,\rho,-\rho$. The repeated integral operation (C2) expresses $l$ derivatives in $R$ using at most $2l$ derivatives in $\rho$ at contracted values of $\rho$. Differentiating (C8) in $s$ and in the parameters preserves this bound. Polynomial division (C12) gives precisely $M_J$ for the polynomial part. Hence (C16) holds for $\mu_+-M_J$ as well.

For any desired ordinary derivative order $K$, take $J>K+1$. All derivatives through order $K$ of these two remainders tend to zero at $(s,R)=(0,0)$, uniformly in the retained parameters. The polynomial jets agree on both sides. They are consistent as $J$ increases, since each extra quotient monomial has weighted degree at least $2J$ and ordinary degree at least $J$. Thus the derivatives through order $K$ extend continuously with the same values at the corner. Applying the fundamental theorem on coordinate segments proves that they are the actual derivatives of the glued function. Since $K$ was arbitrary, $\mu$ is smooth there.

We have proved the local smooth division theorem

\[
 \begin{aligned}
 q(z,s)={}&a(z,R)+s b(z,R)\\
          &+(s^2-R)\mu(z,s,R)
 \end{aligned}
 \tag{C17}
\]

for both signs of $R$, with all parameter derivatives. The construction does not require $q$ to be analytic. For a smooth function $R=R(z)$, substitution in (C17) gives smooth coefficient functions of $z$. For $R\geq0$ those coefficients are exactly (C6); the smooth extension into $R<0$ is a choice, and no uniqueness there is asserted.

<a id="quadratic-cutoff-sign"></a>

## 5. A decreasing cutoff and its boundary sign

The scalar function

\[
 \chi(v)=
 \begin{cases}\exp(1/v),&v<0,\\0,&v\geq0\end{cases}
 \tag{C18}
\]

is smooth, nonnegative and decreasing, with $\chi'<0$ on $v<0$. All derivatives at zero vanish. To check these assertions, each derivative on $v<0$ is $\exp(1/v)$ times a polynomial in $1/v$. For every integer $m$, $t^{-m}e^{-1/t}\to0$ as $t\downarrow0$: the exponential series gives $e^{1/t}\geq t^{-m-1}/(m+1)!$. This proves the smooth extension and its derivative signs directly. It also proves that $\sqrt\chi$ and $\sqrt{-\chi'}$, extended by zero, are smooth, since on the negative half line they are $e^{1/(2v)}$ and $e^{1/(2v)}/|v|$.

On every bounded $v$ interval, every derivative order $m$ and every $0<\gamma<1$ satisfy

\[
 |\chi^{(m)}|\leq C_{m,\gamma}\chi^{1-\gamma},
 \qquad
 |(-\chi')^{(m)}|\leq C_{m,\gamma}(-\chi')^{1-\gamma}.
 \tag{C19}
\]

Near zero the ratios are an exponentially decreasing factor times a fixed power of $1/|v|$; away from zero continuity on a compact interval proves the bound. At zeros both sides are zero. These are the precise derivative bounds used when such weights are differentiated repeatedly.

For the gauged wave operator in the preceding reading, write

\[
 p(z,s)=s^2+a_0(z),\qquad R(z)=-a_0(z),
 \tag{C20}
\]

where $z=(x,y,\eta)$, $x\geq0$ is the inward normal coordinate, and $y$ includes time. Fix a glancing point $z_0$ at $x=0$, with $a_0(z_0)=0$. Choose a smooth real $\phi_0(z)$ with $\phi_0(z_0)=0$, constants $c>0$, $\epsilon>0$, and put

\[
 \begin{aligned}
 \phi(z,s)&=\phi_0(z)-cs,\\
 q(z,s)&=\chi(\phi(z,s)-\epsilon).
 \end{aligned}
 \tag{C21}
\]

Apply (C17) and then substitute $R=-a_0(z)$. Denote the resulting real coefficients by $a(z),b(z)$ and the remainder by $\mu(z,s)$. Formula (C7) proves $b\geq0$ wherever $R\geq0$, since $\partial_sq=-c\chi'\geq0$. At the glancing point,

\[
 b(z_0)=-c\chi'(-\epsilon)>0.
 \tag{C22}
\]

Continuity therefore gives a fixed neighborhood on which $b$ is bounded below by a positive constant, including its elliptic part $R<0$. This conclusion uses strict positivity at the retained point. We do not assert that an arbitrary smooth extension is nonnegative everywhere in the elliptic region.

If $H_p\phi(z_0,0)<0$, then $H_pq=\chi'(\phi-\epsilon)H_p\phi$ is positive in a smaller neighborhood of that point. Such a choice exists at strict diffraction: if $\partial_xa_0(z_0)<0$, take $\phi_0=0$. Since $H_ps=-\partial_xa_0$, this gives $H_p\phi=c\partial_xa_0<0$. More general $\phi_0$ are allowed when they retain that strict inequality. The construction alone does not yet show that their level sets form the needed incoming neighborhood of a generalized ray.

Choose a real smooth compact tangential phase cutoff $\zeta(z)$ equal to one near $z_0$ and supported where $b>0$. Its normal support may meet $x=0$, and it vanishes before the outer edge of the coordinate collar. Set $\widetilde a=\zeta^2a$ and $\widetilde b=\zeta^2b$. Equation (C17) gives the exact principal-symbol identity

\[
 \begin{aligned}
 H_p(\widetilde a+s\widetilde b)
  ={}&\zeta^2\chi'(\phi-\epsilon)H_p\phi\\
    &+\chi(\phi-\epsilon)H_p(\zeta^2)
       -pH_p(\zeta^2\mu).
 \end{aligned}
 \tag{C23}
\]

Here $H_pp=0$. Thus the desired sign holds on the characteristic set where $\zeta=1$. The second term is supported where the phase cutoff varies; it has not vanished from the propagation problem. The last term is a multiple of the principal equation symbol. Symbol division has not been promoted to an exact operator identity.

<a id="quadratic-positive-quantization"></a>

## 6. Quantization with a positive Dirichlet boundary form

Use $d_x=hD_x=-ih\partial_x$ and $P_h=d_x^2+R_h(x)$ from the preceding reading, with $R_h$ tangential and formally self-adjoint. All coefficients and their required derivatives are uniformly bounded on the retained coordinate extension. Put

\[
 \begin{aligned}
 S_h&=\operatorname{Op}_h(\zeta\sqrt b),\qquad B_h=S_h^*S_h,\\
 A_{0,h}&=\tfrac12\bigl(\operatorname{Op}_h(\widetilde a)
                         +\operatorname{Op}_h(\widetilde a)^*\bigr),\\
 A_h&=A_{0,h}+\tfrac12(B_hd_x+d_xB_h).
 \end{aligned}
 \tag{C24}
\]

The symbol $\zeta\sqrt b$ is smooth with compact tangential phase support: define it on the positive neighborhood and extend it by zero outside, since $\zeta$ is supported strictly inside that neighborhood. Finite products and adjoints prove that $A_{0,h},B_h$ have respective principal symbols $\widetilde a,\widetilde b$ and uniform norm bounds, including each fixed normal derivative. In particular $A_h$ realizes the polynomial from Section 5 using at most one normal derivative, with all lower terms retained. Positivity of $B_h$ is exact because it is $S_h^*S_h$; no assertion that left quantization preserves arbitrary nonnegative symbols is involved.

For a smooth Dirichlet function $u$ vanishing near the outer normal endpoint, set $f=P_hu$. The exact identity (D7) becomes

\[
 \begin{aligned}
 &\left(\frac ih[P_h,A_h]u,u\right)
          +\|S_h(0)d_xu(0)\|^2\\
 &\qquad=\frac2h\operatorname{Im}(f,A_hu).
 \end{aligned}
 \tag{C25}
\]

Both the positive boundary term and the actual forcing survive. Expanding $d_xB_h=B_hd_x-ihB_h'$ also gives

\[
 \|A_hu\|\leq C(\|u\|+\|d_xu\|),\qquad 0<h\leq1.
 \tag{C26}
\]

All norms are over the collar and tangential variables, except the boundary norm in (C25). The uniform bound follows from the finite cutoff norm bounds and their normal derivatives.

<a id="quadratic-exact-interior-form"></a>

There is an exact version of the interior form in (C25) that eliminates the second normal derivative using the equation. With primes denoting normal derivatives and with the inner product linear in its first entry, (D8) gives

\[
 \begin{aligned}
 \mathcal C_h(u)={}&2\operatorname{Re}(A_{0,h}'u,d_xu)
       +\left(\tfrac ih[R_h,A_{0,h}]u,u\right)\\
 &+(B_h'd_xu,d_xu)
       +\operatorname{Re}(B_h'f,u)\\
 &-\operatorname{Re}(B_h'R_hu,u)
       +\operatorname{Re}\left(\tfrac ih[R_h,B_h]d_xu,u\right)\\
 &-\operatorname{Re}(B_hR_h'u,u),\\
 \mathcal C_h(u)&=\left(\tfrac ih[P_h,A_h]u,u\right).
 \end{aligned}
 \tag{C27}
\]

For the normal terms, integrate $d_xB_h'd_x$ once to get $(B_h'd_xu,d_xu)$. The two remaining second-normal terms in (D8) give $\operatorname{Re}(B_h'd_x^2u,u)$; substitute $d_x^2u=f-R_hu$. Their boundary terms vanish because $u(0)=0$. The two terms containing $[R_h,B_h]$ combine into the real part displayed in (C27), using self-adjointness of $i[R_h,B_h]/h$ and the first-order integration by parts. These calculations prove (C27), including the forcing term $\operatorname{Re}(B_h'f,u)$.

Every operator multiplying $u,d_xu,f$ in (C27) is bounded on tangential $L^2$, uniformly for small $h$. For example the finite differential-cutoff calculation (N23) proves $[R_h,S_h]=O(h)$, $R_hS_h=O(1)$ and $S_hR_h=O(1)$. Taking adjoints and using the product commutator rule proves the same assertions for $B_h=S_h^*S_h$ and for $A_{0,h}$; differentiate the factors to treat $B_h'$ and $R_h'$. Hence

\[
 |\mathcal C_h(u)|
  \leq C\bigl(\|u\|^2+\|d_xu\|^2+\|f\|\|u\|\bigr).
 \tag{C28}
\]

The bound is for the exactly expanded form, not for an unlocalized unbounded operator $R_h$ on arbitrary $L^2$ data.

Equations (C25)–(C28) also hold for $H^2$ Dirichlet inputs with compact normal support and $f=P_hu\in L^2$. The odd extension across $x=0$ has no point mass in its first two normal derivatives, since its zero value and evenly extended first derivative match. Even normal mollification and tangential mollification give smooth Dirichlet approximants converging in $H^2$. The [norm-primitive trace bound](dirichlet-commutator-and-diffraction.md#dirichlet-weak-normal-multiplier) gives convergence of their normal traces, and smooth bounded coefficients give convergence of their $P_h$ images. Thus every bounded term in (C25)–(C28) passes to the limit. The [negative-order wave reading](dirichlet-wave-regularization.md#dirichlet-exact-wave-regularization), (W11), supplies such regularity for every rough datum needed in the boundary lesson after the proved inverse-power reduction. The source datum is not restricted to $H^2$.

## 7. From division to propagation

The smooth division theorem gives a normal polynomial that agrees with the full phase cutoff on the characteristic set. Its positive boundary realization is exact, while the interior identity retains both the forcing and the derivatives of the outer cutoff. Those terms must be estimated using the actual wave and the geometry of the incoming region.

The [localized glancing estimate](glancing-commutator-estimate.md#glancing-commutator-estimate) gives the interior lower bound for this multiplier. [Incoming phase neighborhoods for Dirichlet waves](diffractive-phase-neighborhoods.md#two-root-diffraction-supports) constructs the incoming region and develops the regularity iteration; its [singular-curve argument](diffractive-phase-neighborhoods.md#singular-generalized-curves) treats the full relation defined in [Generalized reflected curves](generalized-reflected-curves.md#generalized-reflected-curves). The local choice of a phase with the required sign in Section 5 is one ingredient of that argument.
