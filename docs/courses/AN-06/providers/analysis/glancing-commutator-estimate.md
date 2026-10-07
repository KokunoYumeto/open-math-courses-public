# A localized glancing commutator estimate

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="glancing-commutator-estimate"></a>

This reading proves the interior lower estimate for a signed normal-frequency multiplier at a glancing point. The equation makes the localized normal derivative small enough to absorb its mixed terms. We identify the errors on the phase and normal cutoff edges and prove a quantitative half-step regularity gain under explicit bounds on those errors. The final section explains how these hypotheses enter boundary propagation.

Read [Quadratic normal division and Dirichlet phase cutoffs](quadratic-normal-cutoffs.md#quadratic-exact-interior-form), [Dirichlet commutators and a local diffraction estimate](dirichlet-commutator-and-diffraction.md#dirichlet-green-commutator), and [the finite tangential calculus](real-normal-root-trace.md#real-root-cutoff-products) first. We use their finite product, adjoint, separated-support, norm and boundary-form proofs. The scalar positivity estimate is proved by [the Gaussian-packet reading](weighted-positivity.md#high-frequency-norm) and applied in [the tangential Dirichlet estimates](dirichlet-commutator-and-diffraction.md#dirichlet-tangential-estimates), (D10)–(D11).

For further reading, see Victor Ivrii's [*Microlocal Analysis, Sharp Spectral Asymptotics and Applications*, author version of July 9, 2023](https://www.math.utoronto.ca/ivrii/Victor_Ivrii_Microlocal_Analysis,_Sharp_Spectral_Asymptotics_and_Applications.pdf), printed pp. 261–264, especially the separate bulk, lower-regularity and cutoff-edge contributions in (3.4.42).

<a id="glancing-leading-form"></a>

## 1. The exact form and its scalar leading term

Use the same inward normal coordinate $x\in[0,L)$, tangential variables $y$ and semiclassical derivative $d_x=-ih\partial_x$ as in the preceding readings. Let

\[
 \begin{gathered}
 P_h=d_x^2+R_h(x),\\
 \sigma(R_h)=a_0(x,y,\eta)+ha_1(x,y,\eta;h),
 \end{gathered}
 \tag{L1}
\]

where $R_h$ is the full formally self-adjoint scalar tangential differential operator obtained by the proved normal gauge. All smooth coefficient derivatives needed below are bounded. No lower-order term is removed.

Fix the multiplier from (C24), denoted here by

\[
 \begin{gathered}
 A_h=A_{0,h}+\tfrac12(B_hd_x+d_xB_h),\\
 B_h=S_h^*S_h.
 \end{gathered}
 \tag{L2}
\]

Write its real principal coefficients as $\alpha(x,y,\eta)$ and $\beta(x,y,\eta)$, respectively. They have compact tangential phase support, including the fixed outer cutoff. All multiplier families and each fixed normal derivative are uniformly bounded on tangential $L^2$. The following operators are self-adjoint as forms on smooth functions:

\[
 \begin{aligned}
 T_{0,h}={}&\frac ih[R_h,A_{0,h}]
       -\tfrac12(B_h'R_h+R_hB_h')\\
       &-\tfrac12(B_hR_h'+R_h'B_h),\\
 T_{1,h}={}&2A_{0,h}'+\frac ih[R_h,B_h],\\
 T_{2,h}={}&B_h'.
 \end{aligned}
 \tag{L3}
\]

They have uniformly bounded tangential $L^2$ extensions by the finite cutoff calculations. For $P_hv=F$, the exact identity (C27) is

\[
 \begin{aligned}
 \mathcal C_h(v)={}&(T_{0,h}v,v)
       +\operatorname{Re}(T_{1,h}d_xv,v)\\
       &+(T_{2,h}d_xv,d_xv)
       +\operatorname{Re}(B_h'F,v).
 \end{aligned}
 \tag{L4}
\]

Primes mean $x$ derivatives. These formulas keep the forcing term introduced when $d_x^2v$ is replaced by $F-R_hv$.

Define the tangential Poisson bracket by
$\{a,b\}_{\mathrm{tan}}=\partial_\eta a\cdot\partial_yb-\partial_ya\cdot\partial_\eta b$. The scalar leading term of $T_{0,h}$ is

\[
 \begin{aligned}
 t_0={}&\{a_0,\alpha\}_{\mathrm{tan}}\\
       &-a_0\partial_x\beta-\beta\partial_xa_0.
 \end{aligned}
 \tag{L5}
\]

Here is the finite calculus justification, including the order of the remainder. Taylor expansion of the adjoint kernel through its first correction writes the self-adjointized $A_{0,h}$ as $\operatorname{Op}_h(\alpha)+h\operatorname{Op}_h(\alpha_1)+h^2E_h$. The analogous expansion of $S_h^*S_h$ has principal term $\operatorname{Op}_h(\beta)$. The retained coefficient symbols have bounded derivatives and compact frequency support; the remainder amplitudes have bounded derivatives in both positions and compact frequency support. Their norm bounds and those after composing with $R_h$ on either side follow by differentiating those kernels. Each semiclassical derivative inserts a bounded frequency factor or $h$ times a coefficient derivative.

For a compact scalar symbol $a$, applying the product formula (N20) to $R_h\operatorname{Op}_h(a)$ and expanding the input coefficients in the kernel of $\operatorname{Op}_h(a)R_h$ gives

\[
 \frac ih[R_h,\operatorname{Op}_h(a)]
       =\operatorname{Op}_h(\{a_0,a\}_{\mathrm{tan}})+O(h).
 \tag{L6}
\]

To verify the second expansion, first move the finitely many input derivatives onto the kernel, as in (N23). Taylor-expand each coefficient at the output position. Replace each factor of the input-minus-output position by $ih\partial_\eta$ on the exponential and integrate by parts. The linear terms give the displayed bracket, and the second-order remainder has an explicit $h^2$ with bounded compact-frequency amplitude before division by $h$. The lower symbol $ha_1$ contributes only $O(h)$ to (L6). The correction $h\operatorname{Op}_h(\alpha_1)$ also contributes $O(h)$, by (N23). The $h^2E_h$ remainder contributes $O(h)$ because both $R_hE_h$ and $E_hR_h$ are bounded. Thus no unknown $O(1)$ commutator remainder is hidden in (L6). Products in the other lines of (L3) use the first-order version of the same calculation. This proves (L5) with norm-$O(h)$ error after any retained compact phase localization, uniformly in the normal interval and under its fixed parameter derivatives.

Let $z_0=(0,y_0,\eta_0)$ be a glancing point, so $a_0(z_0)=0$, and assume

\[
 t_0(z_0)>0.
 \tag{L7}
\]

For the construction in (C21)–(C24), with the outer cutoff equal to one, (L5) at this point is precisely $H_pq(z_0,0)$ for $p=s^2+a_0$. Thus the signed cutoff supplies (L7) whenever its stated strict phase inequality holds. The estimate below uses exactly (L7), without claiming the existence of a suitable incoming phase for every boundary contact.

<a id="glancing-inner-localization"></a>

## 2. Choosing the inner localization in the correct order

Fix $c>0$ and a neighborhood of $z_0$ on which $t_0\geq6c$. Fix a constant $K\geq1$ bounding $T_{1,h},T_{2,h},B_h'$ and the multiplier norms in (C26) on a small fixed normal interval. These constants depend on the already chosen outer multiplier; they are fixed before shrinking the inner cutoff.

Choose a positive number $m$ sufficiently small that

\[
 K\sqrt{3m}+3Km\leq c.
 \tag{L8}
\]

Since $a_0(z_0)=0$, choose a normal length $\ell<L$ and real tangential cutoffs $q,\theta\in C_c^\infty(T^*\mathbb R^d)$, independent of $x$, such that $q=1$ near $(y_0,\eta_0)$, $\theta=1$ near $\operatorname{supp}q$, and throughout $0\leq x\leq\ell$,

\[
 \begin{gathered}
 t_0\geq6c\text{ on }\operatorname{supp}q,\\
 |a_0|\leq m/2\text{ on }\operatorname{supp}\theta.
 \end{gathered}
 \tag{L9}
\]

Take $0\leq q,\theta\leq1$. Both supports are contained in the fixed coordinate neighborhood. Smooth cutoffs exist by the earlier explicit cutoff construction and compact containment. Their derivative constants may be large; they are finite and are used when choosing $h_0$ last.

Put $Q_h=\operatorname{Op}_h(q)$. The finite products and Gaussian positivity applied to $(t_0-4c)q^2\geq0$ give

\[
 (T_{0,h}Q_hw,Q_hw)
       \geq4c\|Q_hw\|^2-Ch\|w\|^2.
 \tag{L10}
\]

Indeed $Q_h^*T_{0,h}Q_h=\operatorname{Op}_h(t_0q^2)+O(h)$ and $Q_h^*Q_h=\operatorname{Op}_h(q^2)+O(h)$. The positive packet quantization of the nonnegative difference has nonnegative form and differs in norm by $O(h)$, exactly as in (D10)–(D11). Integrate this slice inequality in $x$ when necessary.

There is also, for each fixed integer $J\geq1$, the uniform small-norm estimate

\[
 \|R_hQ_hw\|\leq m\|Q_hw\|+C_Jh^J\|w\|.
 \tag{L11}
\]

For its proof set $E_h=\operatorname{Op}_h(\theta(a_0+ha_1))$. The proved norm estimate (N17) gives $\|E_h\|\leq m/2+C_\theta h\leq m$ after fixing $h_0$ sufficiently small. The symbol of $R_h-E_h$ vanishes near $\operatorname{supp}q$; the full separated-symbol estimate (N21) gives $(R_h-E_h)Q_h=O(h^J)$ for every fixed $J$. This proves (L11). In particular the small constant is chosen before the inner cutoff derivatives and before $h_0$; it is not incorrectly inferred from a derivative-dependent norm bound.

<a id="glancing-lower-bound"></a>

## 3. The lower estimate and the normal boundary term

Let $u,d_xu,f\in L^2$, with $P_hu=f$ distributionally, and suppose $u$ vanishes for $x\geq\ell$. Set

\[
 v=Q_hu,\qquad F=Q_hf+[R_h,Q_h]u.
 \tag{L12}
\]

Assume the localized Dirichlet condition $v(0)=0$. The [weak-trace and approximation proof](dirichlet-commutator-and-diffraction.md#dirichlet-weak-normal-multiplier) applies: $v,d_xv,d_x^2v$ and all required tangential derivatives belong to $L^2$ for each fixed $h$, because $Q_hR_h$ is bounded with compact frequency amplitude. It gives the continuous traces and justifies the exact Green identities, including (L4). Let

\[
 X=\|v\|,\quad Y=\|d_xv\|,\quad
 Z=\|F\|,\quad U=\|u\|.
 \tag{L13}
\]

The ordinary Dirichlet energy identity and (L11) yield

\[
 Y^2\leq ZX+mX^2+C_Jh^JUX
       \leq3mX^2+C_mZ^2+C_{m,J}h^{2J}U^2.
 \tag{L14}
\]

The second inequality uses $ab\leq ma^2+b^2/(4m)$ twice. Taking square roots gives

\[
 Y\leq\sqrt{3m}X+C_mZ+C_{m,J}h^JU.
 \tag{L15}
\]

By (L4), (L10) and the fixed operator bound $K$,

\[
 \begin{aligned}
 \mathcal C_h(v)\geq{}&4cX^2-ChU^2\\
                    &-KXY-KY^2-KZX.
 \end{aligned}
 \tag{L16}
\]

Insert (L14)–(L15). The coefficient of $X^2$ coming from the leading pieces of $KXY+KY^2$ is at most $c$ by (L8). The remaining mixed terms are constant multiples of $ZX$ and $h^JUX$. Young's inequality bounds these by $cX^2$ in total plus $CZ^2+C_Jh^{2J}U^2$. Taking $J=1$, and using $h^2\leq h$ for $0<h\leq1$, proves the actual interior lower bound

\[
 \mathcal C_h(v)\geq2cX^2-CZ^2-ChU^2.
 \tag{L17}
\]

The forcing term in (L4) was part of $KZX$; it has not been dropped. The estimate holds for the exact operator form, not merely for its principal symbol.

Now use the exact positive boundary identity (C25). Its right side is bounded by $Ch^{-1}Z(X+Y)$ by (C26). Substitute (L15), with $J=1$, and absorb the resulting $h^{-1}ZX$ term with $cX^2$. The term $h^{-1}Z^2$ is at most $h^{-2}Z^2$; the remaining $ZU$ is at most a constant times $h^{-2}Z^2+h^2U^2$. Combining with (L17), then with (L14), gives

\[
 \begin{aligned}
 &\|Q_hu\|^2+\|Q_hd_xu\|^2\\
 &\quad+\|S_h(0)d_x(Q_hu)(0)\|^2\\
 &\qquad\leq C\left(h^{-2}\|F\|^2+h\|u\|^2\right).
 \end{aligned}
 \tag{L18}
\]

All constants are independent of sufficiently small $h$. The boundary norm is the actual weighted normal trace appearing in the chosen multiplier. We have not replaced it by an unweighted trace using an unproved global inverse for $S_h$.

<a id="glancing-transition-calculus"></a>

## 4. Where the phase and normal cutoff errors occur

We make the forcing in (L18) more useful without assuming that it is small. Choose a real compact tangential cutoff $g$, independent of $x$, equal to one on a neighborhood of $\operatorname{supp}q$, and put

\[
 G_h=\operatorname{Op}_h(g),\qquad K_h=Q_hG_h.
 \tag{L19}
\]

Choose a second real compact tangential cutoff $e=1$ near the closed support of the derivatives of $q$, with support disjoint from a smaller neighborhood on which $q=1$. Let $E_h^{\mathrm{edge}}=\operatorname{Op}_h(e)$. Such a choice is possible because $q$ is constant on that smaller neighborhood and outside its compact support. Cutoff derivatives of every positive order are supported in the same closed transition set.

For each fixed $J$ the finite calculus gives

\[
 \begin{aligned}
 K_h-Q_h&=O_{L^2\to L^2}(h^{J+1}),\\
 [R_h,K_h]&=[R_h,Q_h]E_h^{\mathrm{edge}}
                         +O_{L^2\to L^2}(h^{J+1}),\\
 \|[R_h,Q_h]\|&\leq Ch.
 \end{aligned}
 \tag{L20}
\]

Here is the support argument to every required finite order. In the expansion for $Q_hG_h$, the principal product is $q$, since $g=1$ near its support. Every higher product coefficient contains a derivative of $g$ and a derivative of $q$ at the same phase point, so it vanishes. The remainder has arbitrarily high powers of $h$ and bounded compact-frequency amplitude. Composing that remainder with the differential $R_h$ on either side keeps the same power, by kernel differentiation as in Section 1; no boundedness of unlocalized $R_h$ is presumed.

Next expand $[R_h,Q_h]$ to any finite order. With $a_h=a_0+ha_1$, its coefficients before the bounded remainder are

\[
 \sum_{1\leq|\nu|<N}\frac{(h/i)^{|\nu|}}{\nu!}
 \operatorname{Op}_h\!\left(
 (\partial_\eta^\nu a_h)(\partial_y^\nu q)
 -(\partial_\eta^\nu q)(\partial_y^\nu a_h)\right).
\]

The first product is (N20). To verify the reversed product explicitly, consider a term $c(y)\eta^\beta$ of the polynomial symbol $a_h$. Moving its input derivatives onto the kernel gives the two-position amplitude

\[
 q(y,\eta)\sum_{\gamma\leq\beta}\binom{\beta}{\gamma}
       \eta^{\beta-\gamma}(ih)^{|\gamma|}
       \partial_z^\gamma c(z).
\]

Taylor-expand at $z=y$. Integration by parts replaces a factor $(z-y)^\delta$ by $(-ih)^{|\delta|}\partial_\eta^\delta$ on the amplitude. Fix the total coefficient derivative $\nu=\gamma+\delta$, and let $\kappa\leq\delta$ derivatives fall on $q$. Set $\mu=\nu-\kappa$. If $\mu\not\leq\beta$, the differentiated frequency monomial vanishes. Otherwise, after the common factors are removed, summing the terms with this $\kappa$ gives
$\sum_{\gamma\leq\mu}(-1)^{|\gamma|}/(\gamma!(\mu-\gamma)!)=\prod_j(1-1)^{\mu_j}/\mu!$.
For $\mu\ne0$ this is zero, by the finite binomial formula. The only surviving case is $\kappa=\nu$, whose coefficient is $(h/i)^{|\nu|}\eta^\beta(\partial_\eta^\nu q)(\partial_y^\nu c)/\nu!$. Summing the differential terms gives exactly the second product above, including the terms from $ha_1$. Taylor's integral remainder is $h^N$ times a bounded compact-frequency amplitude; each transferred derivative either differentiates $q$ or lowers a frequency monomial. The same kernel calculation controls fixed normal derivatives and compositions with $R_h$.

The scalar zeroth-order products cancel. Every remaining displayed coefficient contains a positive-order derivative of $q$, so it is supported in the transition set where $e=1$. Composing on the right with $E_h^{\mathrm{edge}}$ changes each of them only by an arbitrarily high-order remainder: all differentiated products meet a derivative of $e$ outside that transition set. The original remainders have bounded norms with the asserted powers. This proves the second line of (L20), and the last line is also (N23). All estimates are uniform in the retained normal interval.

<a id="glancing-cutoff-forcing"></a>

Let $w$ be an $H^2$ Dirichlet input on the collar. Choose a smooth real normal cutoff $\psi$ equal to one near zero and supported in $[0,\ell)$. Apply (L18) to $u=G_h(\psi w)$, so $v=K_h(\psi w)$. Since $Q_h,G_h$ are independent of $x$, its exact forcing is

\[
 \begin{aligned}
 F={}&K_h(\psi P_hw)+[R_h,K_h](\psi w)\\
       &-2ihK_h(\psi'd_xw)-h^2K_h(\psi''w).
 \end{aligned}
 \tag{L21}
\]

The normal terms follow directly from $[d_x^2,\psi]=-2ih\psi'd_x-h^2\psi''$. Their signs and powers are retained. Applying (L20), the squared triangle inequality and (L18) gives, for every fixed $J\geq1$,

\[
 \begin{aligned}
 &\|v\|^2+\|d_xv\|^2\\
 &\quad+\|S_h(0)d_xv(0)\|^2\\
 &\quad\leq C\Bigl(h^{-2}\|K_h(\psi P_hw)\|^2\\
 &\qquad\quad+\|E_h^{\mathrm{edge}}(\psi w)\|^2\\
 &\qquad\quad+\|K_h(\psi'd_xw)\|^2\\
 &\qquad\quad+h^2\|K_h(\psi''w)\|^2\\
 &\qquad\quad+h\|G_h(\psi w)\|^2\Bigr)\\
 &\qquad+C_Jh^{2J}\|\psi w\|^2,\\
 &\quad v=K_h(\psi w).
 \end{aligned}
 \tag{L22}
\]

The first error uses the actual equation. The next three occur on explicitly identified phase or normal cutoff edges. The term with factor $h$ uses the more localized input $G_h(\psi w)$; only the arbitrarily small remainder uses its unlocalized counterpart. This distinction is what makes a regularity induction possible. The main constant can be chosen from the fixed estimate (L18) and the $O(h)$ commutator norm; the arbitrarily high remainder constant may depend on $J$.

<a id="glancing-half-step"></a>

## 5. The precise half-step consequence

For any real $s$, suppose a family $w_h$ satisfies the domain hypotheses above, is polynomially bounded in the sense $\|\psi w_h\|=O(h^{-M})$ for some fixed $M$, and has the actual bounds

\[
 \begin{aligned}
 \|K_h(\psi P_hw_h)\|&=O(h^{s+1}),\\
 \|E_h^{\mathrm{edge}}(\psi w_h)\|&=O(h^s),\\
 \|K_h(\psi'd_xw_h)\|&=O(h^s),\\
 h\|K_h(\psi''w_h)\|&=O(h^s),\\
 \|G_h(\psi w_h)\|&=O(h^{s-1/2}).
 \end{aligned}
 \tag{L23}
\]

Choose an integer $J\geq1$ with $J-M\geq s$. Every term on the right of (L22) is then $O(h^{2s})$. Taking square roots proves

\[
 \begin{aligned}
 &\|K_h(\psi w_h)\|+\|d_xK_h(\psi w_h)\|\\
 &\quad+\|S_h(0)d_xK_h(\psi w_h)(0)\|=O(h^s).
 \end{aligned}
 \tag{L24}
\]

The five bounds in (L23) are the hypotheses needed to apply this gain. In particular, the homogeneous equation controls the first term only; regularity on the tangential and normal cutoff edges must also be established.

[Incoming phase neighborhoods for Dirichlet waves](diffractive-phase-neighborhoods.md#diffractive-phase-neighborhoods) develops the oriented phase, its incoming edge and the estimates used to propagate regularity along generalized rays. That full-phase outer edge differs from the entire transition set of the inner tangential cutoff $q$ in (L20). A bound on the former therefore does not by itself establish the second line of (L23).

For distributional initial data, [Dirichlet wave regularization](dirichlet-wave-regularization.md#dirichlet-wave-regularization) supplies the finite domain regularity used in this reading. The geometry of the rays, including arbitrary contacts and accumulating reflections, is developed in [Existence and compactness of generalized reflected curves](generalized-reflected-curves.md#generalized-reflected-curves).
