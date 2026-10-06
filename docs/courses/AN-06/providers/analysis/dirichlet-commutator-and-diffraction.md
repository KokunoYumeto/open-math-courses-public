# Dirichlet commutators and a local diffraction estimate

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="dirichlet-commutator"></a>

This reading proves an exact boundary commutator identity and a quantitative estimate near a strict diffractive scalar wave covector. It includes the normal gauge, all lower-order terms, compact tangential cutoffs and weak localized traces. The resulting estimate is one analytic step in the full boundary propagation problem. The subsequent [negative-order wave reading](dirichlet-wave-regularization.md#dirichlet-wave-regularization) proves the spectral regularization needed for the boundary lesson, and [Quadratic normal division and Dirichlet phase cutoffs](quadratic-normal-cutoffs.md#quadratic-normal-cutoffs) constructs cutoffs involving normal frequency and their exact boundary form. Full propagation at every contact type remains to be proved.

The free comparison is Victor Ivrii's [*Microlocal Analysis, Sharp Spectral Asymptotics and Applications*, author version of July 9, 2023](https://www.math.utoronto.ca/ivrii/Victor_Ivrii_Microlocal_Analysis,_Sharp_Spectral_Asymptotics_and_Applications.pdf), Section 3.4, especially the boundary term in (3.4.4), the discussion of normal-frequency multipliers on printed pp. 259–260, and the estimates on pp. 262–266. Theorem 3.4.10 describes the refined generalized relation for a single quadratic normal block; using that theorem here still requires its complete programme proof. We derive our signs and estimates directly below. The identities are not inferred from a source locator.

Read [Boundary traces near a real normal root](real-normal-root-trace.md), Sections 6–10, first. Its formulas (N19)–(N23) prove the finite tangential products, cutoff tails and bounded differential compositions used here; Section 8 constructs weak traces from norm primitives. The [Gaussian-packet reading](weighted-positivity.md#high-frequency-norm), Lemmas 2–3 and Theorem 4, supplies the proved positivity and norm estimates. Its free comparison is [Nicolas Lerner's author Chapter 2](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Proposition 2.4.3. Vector integration and the fundamental theorem have their earlier proofs in [Hilbert-valued integration](hilbert-valued-integration.md).

## 1. Conventions and the normal gauge

Work on $0\leq x<L$ with tangential variables $y\in\mathbb R^d$, including time for the wave operator. Put $H=L^2(\mathbb R^d)$, $d_x=hD_x=-ih\partial_x$, and use inner products linear in the first entry. Norms without a boundary subscript are over $(0,L)\times\mathbb R^d$. Functions considered below vanish near $x=L$.

In boundary normal coordinates and half-density coefficients, a formally self-adjoint scalar wave operator, multiplied by $h^2$ and the sign that makes its normal leading coefficient one, can be written

\[
 \mathcal P_h=d_x^2+
        \frac h2(bd_x+d_xb)+T_h(x),\qquad b\text{ real}.
 \tag{D1}
\]

Here $T_h(x)$ is a formally self-adjoint tangential differential operator of order at most two. Its principal symbol is $a_0=r(x,y',\xi')-\tau^2$, with $y=(t,y')$ and $\eta=(\tau,\xi')$. All coefficients and the derivatives needed below are bounded on the coordinate extension. This description retains arbitrary smooth self-adjoint first-order and zero-order terms.

To check the decomposition, put every derivative on the right. The coefficient of the single normal derivative is real: comparison with the formal adjoint gives its complex conjugate as the same coefficient, since the normal leading coefficient is the constant one and there are no mixed principal normal/tangential derivatives. Symmetrizing that term gives the middle term in (D1); its extra zero-order term stays in $T_h$. The difference is tangential and formally self-adjoint, so $T_h(x)$ has that property for each fixed $x$.

Define the multiplication operator

\[
 U(x,y)=\exp\!\left(-\frac i2\int_0^x b(s,y)\,ds\right).
 \tag{D2}
\]

Then $|U|=1$, $U(0,y)=1$, and $d_xU=-hbU/2$. Completing the square in (D1) gives the exact identities

\[
 \begin{aligned}
 \mathcal P_h&=(d_x+hb/2)^2+T_h-h^2b^2/4,\\
 U^{-1}\mathcal P_hU&=d_x^2+R_h(x),\\
 R_h&=U^{-1}(T_h-h^2b^2/4)U.
 \end{aligned}
 \tag{D3}
\]

The operator $R_h$ is tangential and formally self-adjoint. Differentiating $U$ tangentially shows directly that its principal symbol is still $a_0$: each derivative falling on $U$ removes one derivative from the input, and hence adds a factor $h$ in semiclassical notation. Thus its left symbol has the form

\[
 a(x,y,\eta;h)=a_0(x,y,\eta)+h a_1(x,y,\eta;h),
 \tag{D4}
\]

where $a_1$ is a polynomial of degree at most one in $\eta$, with uniformly bounded coefficient derivatives. Its degree-zero part includes the original potential, the square-completion term and all derivatives of $U$. No such term has been discarded. Multiplication by $U$ preserves the Dirichlet condition. For a Dirichlet function $v$, $(d_xUv)(0)=(d_xv)(0)$ as well. We prove the remaining assertions for $P_h=d_x^2+R_h$; (D3) transfers them to the original operator with this explicit gauge.

## 2. Green's identity and the boundary commutator

First take functions smooth to the boundary, with sufficient tangential decay and compact support before $L$. Two integrations by parts give

\[
 \begin{aligned}
 &(P_hv,w)-(v,P_hw)\\
 &\quad=ih\bigl((d_xv(0),w(0))_H
                      +(v(0),d_xw(0))_H\bigr).
 \end{aligned}
 \tag{D5}
\]

Indeed the second-derivative boundary term is
$h^2(v'(0)\overline{w(0)}-v(0)\overline{w'(0)})$, integrated in $y$; using $d_x=-ih\partial_x$ gives (D5). The tangential terms cancel by the formal self-adjointness of $R_h$. This fixes both the inward-normal sign and the inner-product convention.

Let $A_0(x)$ and $B(x)$ be tangential, formally self-adjoint operators and set

\[
 A=A_0+\tfrac12(Bd_x+d_xB).
 \tag{D6}
\]

Initially all operations are on the smooth functions just specified. Compact tangential phase symbols, or finite products and adjoints of their quantizations, are admissible. A prime on such an operator denotes its $x$ derivative. For $u(0)=0$, the exact identity is

\[
 \begin{aligned}
 &\left(\frac ih[P_h,A]u,u\right)
            +(B(0)d_xu(0),d_xu(0))_H\\
 &\qquad=\frac2h\operatorname{Im}(P_hu,Au).
 \end{aligned}
 \tag{D7}
\]

Here is the full boundary calculation. Since $u(0)=0$ and all its tangential derivatives at the boundary vanish, (D6) gives $(Au)(0)=B(0)d_xu(0)$. Applying (D5) to $Au,u$ yields
$(P_hAu,u)=(Au,P_hu)+ih((Au)(0),d_xu(0))_H$.
The first-order Green formula for $A$ has boundary term
$ih(Bv(0),w(0))_H$. It vanishes for $v=P_hu,w=u$. Consequently $(AP_hu,u)=(P_hu,Au)$. Subtracting these two identities and using
$\overline z-z=-2i\operatorname{Im}z$ proves (D7).

In particular, tangential multipliers have $B=0$ and give no boundary term. A multiplier with a normal derivative has the displayed term; it cannot be discarded using $u(0)=0$. If $B=S^*S$, that term is exactly $\|S(0)d_xu(0)\|_H^2\geq0$, without any assertion that quantization preserves arbitrary nonnegative symbols.

For completeness, the entire commutator can be expanded without a symbolic remainder. The relations $[d_x,C]=-ihC'$ and $[R_h,d_x]=ihR_h'$ give

\[
 \begin{aligned}
 \frac ih[P_h,A]={}&d_xA_0'+A_0'd_x+\frac ih[R_h,A_0]\\
 &+d_xB'd_x+\tfrac12(B'd_x^2+d_x^2B')\\
 &+\frac{i}{2h}\bigl([R_h,B]d_x+d_x[R_h,B]\bigr)\\
 &-\tfrac12(BR_h'+R_h'B).
 \end{aligned}
 \tag{D8}
\]

Each term follows by the product commutator rule. For example
$[d_x^2,B]=-ih(d_xB'+B'd_x)$, and commuting $R_h$ with the two terms in $Bd_x+d_xB$ produces the last line with its minus sign. This proves (D8), including all lower terms. When $A=d_x$, it reduces to $-R_h'$.

## 3. Two scalar tangential estimates

We write the precise finite estimates needed below, including their proofs. Let $q(y,\eta)$ be real, smooth and compactly supported, independent of $x$, and put $Q_h=\operatorname{Op}_h(q)$. Assume on its support, for $0\leq x\leq\ell<L$, that

\[
 -\partial_x a_0(x,y,\eta)\geq2c,\qquad c>0.
 \tag{D9}
\]

All constants below are uniform in that normal interval and for sufficiently small $h$. We claim

\[
 \begin{aligned}
 &-\operatorname{Re}(R_h'Q_hw,Q_hw)_H\\
 &\qquad\geq c\|Q_hw\|_H^2-Ch\|w\|_H^2.
 \end{aligned}
 \tag{D10}
\]

To prove it, the finite product (N20), applied to the differential symbol (D4), gives
$R_h'Q_h=\operatorname{Op}_h((\partial_xa_0)q)+hE_h$ with $\|E_h\|\leq C$. The finite adjoint calculation in the preceding scalar calculus gives
$Q_h^*=\operatorname{Op}_h(q)+hF_h$, $\|F_h\|\leq C$.
Explicitly, its kernel amplitude is $q(z,\eta)$; expand at $z=y$, replace $z-y$ by $ih\partial_\eta$ on the kernel, and integrate by parts. The first-order remainder has an explicit $h$, compact frequency support and bounded derivatives in both positions. The bounded-amplitude estimate proves its norm bound. Thus this adjoint assertion uses no unproved infinite expansion.

Applying (N20) once more to the compact right symbols gives

\[
 \begin{aligned}
 Q_h^*R_h'Q_h
   &=\operatorname{Op}_h((\partial_xa_0)q^2)+O_{H\to H}(h),\\
 Q_h^*Q_h&=\operatorname{Op}_h(q^2)+O_{H\to H}(h).
 \end{aligned}
 \tag{D11}
\]

The scalar symbol $g=(-\partial_xa_0-c)q^2$ is nonnegative everywhere by (D9) and zero off the compact support of $q$. Its operator has real quadratic form bounded below by $-Ch\|w\|^2$. To see this with the leading sign intact, use the packet proof of Theorem 4 in the Gaussian reading with $R=h^{-1}$ and packet width $h^{1/2}$ in ordinary position/frequency coordinates. Its positive operator $W^*\mathcal M_{g(y,h\xi)}W$ differs from $\operatorname{Op}_h(g)$ by norm at most $Ch$, by the proved second-order Gaussian and left-to-Weyl remainders. The positive operator has nonnegative quadratic form because $g\geq0$. Combining this fact with (D11) proves (D10).

There is also a constant $M$ such that, for every fixed integer $J\geq1$,

\[
 \|R_hQ_hw\|_H\leq M\|Q_hw\|_H+C_Jh^J\|w\|_H.
 \tag{D12}
\]

Choose a compact smooth $\chi$ equal to one near $\operatorname{supp}q$ and set $E_h=\operatorname{Op}_h(\chi a)$. The cutoff symbol has uniformly bounded derivatives and supremum, so (N17) gives $\|E_h\|\leq M$ after increasing $M$. The symbol of $R_h-E_h$ vanishes near $\operatorname{supp}q$. The complete tail calculation (N21) therefore gives $\|(R_h-E_h)Q_h\|\leq C_Jh^J$, which is (D12). Smallness of $a_0$ is not needed for this assertion.

The compositions $R_hQ_h,Q_hR_h$ and their normal derivatives are bounded on $H$ by (N23), and $[R_h,Q_h]=O_{H\to H}(h)$. These are bounded distributional extensions, not a claim that $R_h$ itself is bounded on $H$.

## 4. Weak inputs and the exact normal multiplier identity

Suppose $u,d_xu,f\in L^2((0,L);H)$, $P_hu=f$ distributionally, and $u$ vanishes for $x\geq\ell$ with some $\ell<L$. Let

\[
 v=Q_hu,\qquad F=Q_hf+[R_h,Q_h]u.
 \tag{D13}
\]

Then the exact equation is $P_hv=F$. Also $d_xv=Q_hd_xu$ and
$d_x^2v=Q_hf-Q_hR_hu\in L^2((0,L);H)$ by the bounded compositions just proved. The primitive argument in Section 8 of the normal-root reading, applied first to $v$ and then to $d_xv$, gives continuous traces of both. Assume the localized Dirichlet condition $v(0)=0$. This follows from the usual homogeneous Dirichlet condition whenever that trace is already defined; it also states exactly the trace hypothesis needed for these weak inputs.

The following two identities hold:

\[
 \|d_xv\|^2+\operatorname{Re}(R_hv,v)
                       =\operatorname{Re}(F,v),
 \tag{D14}
\]

\[
 \begin{aligned}
 &\|d_xv(0)\|_H^2\\
 &\quad-\int_0^L(R_h'(x)v(x),v(x))_H\,dx\\
 &\qquad=\frac2h\operatorname{Im}(F,d_xv).
 \end{aligned}
 \tag{D15}
\]

For smooth inputs, (D14) is one normal integration by parts, with zero boundary value. Equation (D15) is (D7) with $A=d_x$. It can also be checked directly: the imaginary part of $(d_x^2v,d_xv)$ is $h\|d_xv(0)\|^2/2$, and

\[
 \operatorname{Im}(R_hv,d_xv)
      =-\frac h2\int_0^L(R_h'v,v)_H\,dx.
 \tag{D16}
\]

Indeed differentiate the real scalar function $(R_hv,v)_H$ and integrate; both endpoint terms vanish because $v(0)=0$ and $v$ vanishes near $L$. This proves the sign in (D15).

Here are the approximation details for the stated weak domain. For every fixed $h>0$, the compact phase cutoff maps $H$ boundedly into every integer tangential Sobolev space: differentiating its kernel only inserts a power of $\eta/h$ or a derivative of $q$, so the bounded-amplitude proof applies. The same statement holds for $Q_hR_h$, using its two-position differential amplitude in (N23). Consequently $v,d_xv,d_x^2v$ have every required tangential derivative in $L^2$, for this fixed $h$.

Extend $v$ oddly across $x=0$. Its zero trace makes this extension continuous; its first normal derivative extends evenly, hence continuously as well. Applying the primitive integration-by-parts formula separately on the two half intervals shows that the first and second distributional derivatives have no point-mass boundary terms. They are precisely the reflected $L^2$ derivatives. Convolve with an even smooth normal mollifier and a smooth tangential mollifier, and multiply by a fixed even normal cutoff equal to one on the support under consideration. The approximants are smooth, odd in $x$, zero at the boundary and zero near $L$, and converge with two normal derivatives and every tangential derivative needed here. Convolution convergence follows from the already proved translation continuity and averaging result.

If compact tangential support is desired, a smooth cutoff tending to one gives the same convergence: its nonzero derivatives are bounded by inverse powers of its radius and the remaining terms tend to zero by the $L^2$ tail bound. All boundary traces converge as well. For an $H$-valued primitive $z$, the elementary estimate
$\|z(0)\|\leq L^{-1/2}\|z\|_{L^2}+L^{1/2}\|z'\|_{L^2}$ follows by integrating $z(x)-z(0)$ and Cauchy–Schwarz. Apply it to $v$ and to $v'$. Thus every term of (D14)–(D15) passes to the limit. Constants in this approximation may depend on fixed $h$; the identities are exact, and the uniform estimates below come from Sections 3 and 5.

<a id="strict-diffraction-estimate"></a>

## 5. The quantitative localized estimate

Under the hypotheses of Sections 3–4 there is a constant $C$ independent of sufficiently small $h$ such that

\[
 \begin{aligned}
 &\|Q_hu\|^2+\|Q_hd_xu\|^2\\
 &\quad+\|(Q_hd_xu)(0)\|_H^2\\
 &\qquad\leq C\left(h^{-2}\|F\|^2+h\|u\|^2\right),\\
 &F=Q_hf+[R_h,Q_h]u.
 \end{aligned}
 \tag{D17}
\]

This includes the exact localization forcing. In particular a small right-hand side is not inferred just from $f=0$.

**Proof.** Write $X=\|v\|$, $Y=\|d_xv\|$, $Z=\|F\|$, $U_0=\|u\|$, and $T=\|d_xv(0)\|$. Integrate (D10) in $x$. From (D15) and Cauchy–Schwarz,

\[
 cX^2+T^2\leq 2h^{-1}ZY+ChU_0^2.
 \tag{D18}
\]

Equations (D14) and (D12), with $J=1$, give

\[
 \begin{aligned}
 Y^2&\leq ZX+MX^2+C_1hU_0X\\
    &\leq KX^2+Z^2+C_2h^2U_0^2
 \end{aligned}
 \tag{D19}
\]

for fixed constants $K,C_2$. The last inequality uses $ab\leq(a^2+b^2)/2$ twice. Taking square roots and using $\sqrt{a+b+c}\leq\sqrt a+\sqrt b+\sqrt c$ yields
$Y\leq\sqrt KX+Z+\sqrt{C_2}hU_0$.
Insert this bound into (D18). The three resulting products satisfy

\[
 \begin{aligned}
 2\sqrt K h^{-1}ZX&\leq\tfrac c2X^2+C h^{-2}Z^2,\\
 2h^{-1}Z^2&\leq2h^{-2}Z^2,\\
 2\sqrt{C_2}ZU_0&\leq C h^{-2}Z^2+h^2U_0^2.
 \end{aligned}
 \tag{D20}
\]

Absorb $cX^2/2$ into the left side and use $h^2\leq h$. This bounds $X^2+T^2$ by $C(h^{-2}Z^2+hU_0^2)$. Substitute that bound into (D19) to bound $Y^2$ by the same expression. Equation (D17) follows. Every constant was fixed before taking $h$ small. $\square$

For example, for any real $s$, the actual bounds $\|u\|=O(h^{s-1/2})$ and $\|F\|=O(h^{s+1})$ imply that all three norms on the left of (D17) are $O(h^s)$. This is a direct consequence of the estimate, not a claim that a homogeneous wave automatically satisfies its cutoff-forcing hypothesis. Normal position localization also contributes $[d_x^2,\psi]u$ to $f$; that term must be retained.

## 6. Which contact this estimate treats

The normalized scalar principal symbol is
$p=\xi_x^2+r(x,y',\xi')-\tau^2$, with the Hamilton convention
$H_p=\partial_\xi p\,\partial_x-\partial_xp\,\partial_\xi$ in each canonical pair. Direct differentiation gives

\[
 \begin{gathered}
 H_px=2\xi_x,\\
 H_p^2x=-2\partial_xr.
 \end{gathered}
 \tag{D21}
\]

At a glancing point, $x=\xi_x=0$ and $r=\tau^2$. A strict diffractive contact, where the tangent Hamilton curve bends into $x>0$ in both time directions, has $H_p^2x>0$, or $\partial_xr<0$. Since this inequality is strict, continuity provides a normal interval and a compact tangential cutoff equal to one near the point on which (D9) holds. For physical time, $H_pt=-2\tau$ and $\tau$ is constant for the time-independent wave. At glancing,
$d^2x/dt^2=-\partial_xr/(2\tau^2)>0$.
These signs follow from (D21), regardless of notation or printing conventions in the comparison source.

Thus (D17) is available for the actual variable scalar Dirichlet wave near every strict diffractive covector. It gives the positive normal boundary term and the quantitative local estimate needed in that part of a propagation argument. The [quadratic normal cutoff reading, Sections 1–6](quadratic-normal-cutoffs.md#quadratic-normal-cutoffs), proves smooth division through the double root, constructs a signed normal-frequency cutoff and quantizes its Dirichlet boundary form as an exact square. The [localized glancing estimate](glancing-commutator-estimate.md#glancing-commutator-estimate) now proves the interior lower estimate for that multiplier, identifies its actual phase and normal cutoff errors, and gives a half-step gain under the stated bounds on those errors. The [negative-order wave reduction](dirichlet-wave-regularization.md#dirichlet-wave-regularization) is also proved. [Existence and compactness of generalized reflected curves](generalized-reflected-curves.md#generalized-reflected-curves) now proves the geometric existence, compactness and continuation, including gliding and degenerate contacts. A full analytic argument must still obtain the cutoff bounds from the incoming phase neighborhood and complete the regularity iteration to prove propagation along that precise relation. These readings do not replace those obligations by the strict-contact case.
