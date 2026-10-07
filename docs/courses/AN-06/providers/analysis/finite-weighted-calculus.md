# Finite composition and adjoints with spatial weights

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

This reading proves the finite calculus for the metrics actually used in the weighted Sobolev and resolvent lessons. The general quantization and product formulas are presented in Nicolas Lerner's freely accessible [author Chapter 2, Lemma 2.3.12 and Theorems 2.3.18–2.3.19](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf). Here the needed symbol estimates, finite remainders and operator identities are proved directly. No general admissible-metric composition theorem is assumed.

We use the full programme proofs of [Fourier inversion, Schwartz-space preservation, Plancherel and Euclidean product integration](finite-derivative-l2.md#fourier-normalization), and the [finite-derivative left-operator bound](finite-derivative-l2.md#finite-derivative-l2). All other operator and symbol arguments used here are supplied below. Our conventions are $D=-i\partial$ and $\widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx$; the inverse factor is $(2\pi)^{-n}$.

<a id="weights-and-symbols"></a>
## 1. The full class of weights

Fix $0<\gamma\le1$, write $X=\langle x\rangle$, $\Xi=\langle\xi\rangle$, and put
\[
 G_\gamma=X^{-2\gamma}|dx|^2+\Xi^{-2}|d\xi|^2,
 \qquad h=X^{-\gamma}\Xi^{-1}.
 \tag{C1}
\]
A positive weight $w$ is admissible here if it has the following two properties, with fixed constants. It is locally comparable on the boxes
\[
 |y|\le rX^\gamma,\quad |\eta|\le r\Xi
 \quad\Longrightarrow\quad
 C^{-1}w(x,\xi)\le w(x+y,\xi+\eta)\le Cw(x,\xi)
 \tag{C2}
\]
for some $r>0$, and it satisfies
\[
 \frac{w(x+y,\xi+\eta)}{w(x,\xi)}
 \le C\bigl(1+\Xi^2|y|^2+X^{2\gamma}|\eta|^2\bigr)^q
 \quad(y,\eta\in\mathbb R^n)
 \tag{C3}
\]
for some finite $q\ge0$. These are the local-comparison and symplectic-temperateness conditions for (C1). They do not require $w$ to be a product of powers or even to be smooth.

The common convention with the quadratic form based at the other point gives the same condition after increasing $q$. Indeed, set $Q=\Xi^2|y|^2+X^{2\gamma}|\eta|^2$. The one-Lipschitz property of the bracket and $Q\ge |y|^2+|\eta|^2$ give
\[
 \langle\xi+\eta\rangle/\Xi\le1+\sqrt Q,
 \qquad \langle x+y\rangle^\gamma/X^\gamma\le(1+\sqrt Q)^\gamma.
\]
The shifted dual quadratic form on $(y,\eta)$ is consequently at most $C(1+Q)^2$. Applying the same argument with the two points reversed proves the equivalence. It also shows that $w^{-1}$ is admissible: reverse (C3), then compare the two base points in the quadratic form.

Products of admissible weights are admissible. So are $wX^a\Xi^b$ for all fixed real $a,b$. For the latter assertion, the ratios of either bracket in either direction are at most $1+|(y,\eta)|$; on the small boxes with $r<1/2$ they are bounded above and below. These observations prove both required conditions, including negative powers. Comparison with the origin in (C3) shows that $w$ and $w^{-1}$ grow at most polynomially in $(x,\xi)$.

Define $S(w,G_\gamma)$ by the seminorms
\[
 |\partial_x^\alpha\partial_\xi^\beta a(x,\xi)|
 \le A_{\alpha\beta}w(x,\xi)X^{-\gamma|\alpha|}\Xi^{-|\beta|}.
 \tag{C4}
\]
Every assertion below controls each output seminorm by finitely many input seminorms and the displayed structural constants. In particular it is uniform for families sharing those constants. This includes admissible families of truncated weights, without a uniform global upper bound on the weights themselves.

<a id="symbol-completeness-and-reciprocal"></a>
These symbol spaces are complete for their displayed countable seminorms. Indeed a Cauchy sequence and each of its derivatives converge uniformly on compact sets, since the weight and its reciprocal are bounded there. Integrating derivatives along line segments shows successively that these limits are the derivatives of one smooth function. Passing to the pointwise limit in each normalized uniform bound, including the bounds for differences, proves convergence in every symbol seminorm. For a symbol with $|a|\ge cw$, its reciprocal is in $S(w^{-1},G_\gamma)$. Starting from $|a^{-1}|\le c^{-1}w^{-1}$, differentiation of $aa^{-1}=1$ gives, for a nonzero phase-space multi-index $\nu$,
\[
 \partial^\nu(a^{-1})=-a^{-1}
       \sum_{0<\kappa\le\nu}\binom\nu\kappa
             (\partial^\kappa a)\partial^{\nu-\kappa}(a^{-1}).
 \tag{C4a}
\]
Induction on $|\nu|$ proves the required bound: each summand has net weight $w^{-1}$, and the position and frequency derivative factors add to those for $\nu$. The argument is pointwise and applies on any open region with this lower bound, uniformly in families sharing the lower constant and symbol bounds.

<a id="four-region-lemma"></a>
## 2. An oscillatory estimate in four regions

For $|t|\le T$, with $T$ fixed, consider
\[
 \begin{aligned}
 I_t(a,b)(x,\xi)
   &=(2\pi)^{-n}\operatorname{Os}\iint e^{-iy\cdot\eta}
       a(x,\xi+\eta)b(x+ty,\xi)\,dy\,d\eta,\\
 T_ta(x,\xi)
   &=(2\pi)^{-n}\operatorname{Os}\iint e^{-iy\cdot\eta}
       a(x+ty,\xi+\eta)\,dy\,d\eta.
 \end{aligned}
 \tag{C5}
\]
The notation $\operatorname{Os}$ means that both integration variables are cut off at radius tending to infinity before taking the limit. The following proof establishes the existence and cutoff independence of those limits as well as their estimates.

**Lemma 2.1.** Uniformly on $|t|\le T$,
\[
 I_t:S(w_1,G_\gamma)\times S(w_2,G_\gamma)
       \longrightarrow S(w_1w_2,G_\gamma),
 \qquad T_t:S(w,G_\gamma)\longrightarrow S(w,G_\gamma).
 \tag{C6}
\]
Both maps have the finite-seminorm continuity just described.

**Proof.** We first bound their values. Divide the amplitudes in (C5) by $W=w_1(x,\xi)w_2(x,\xi)$ or $W=w(x,\xi)$, respectively. Choose $\varepsilon_0>0$ small enough that $|y|\le2\varepsilon_0X^\gamma$ implies $|ty|\le rX^\gamma$, and $|\eta|\le2\varepsilon_0\Xi$ implies the local comparisons in (C2). A smooth cutoff $\chi$, equal to one on the unit ball and zero outside the ball of radius two, divides the integral into four terms using
\[
 \chi_y=\chi\bigl(y/(\varepsilon_0X^\gamma)\bigr),
 \qquad \chi_\eta=\chi\bigl(\eta/(\varepsilon_0\Xi)\bigr).
 \tag{C7}
\]
We call a variable near when its corresponding cutoff occurs, and far when its complementary cutoff occurs. Derivatives of these cutoffs cost $X^{-\gamma}$ per $y$ derivative and $\Xi^{-1}$ per $\eta$ derivative. All constants can depend on $\varepsilon_0,T$.

In the near-near term substitute $y=X^\gamma Y$, $\eta=\Xi H$, and put $\lambda=X^\gamma\Xi\ge1$. The normalized amplitude has fixed compact support in $(Y,H)$ and bounded derivatives in $H$ of every required finite order. This follows from (C2), (C4), and comparability of the shifted brackets. Its integral has the prefactor $\lambda^n$ and phase $e^{-i\lambda Y\cdot H}$. Integration by parts with $(1-\Delta_H)^L$ bounds it by
\[
 C\lambda^n\int_{|Y|\le C}(1+\lambda^2|Y|^2)^{-L}\,dY
 \le C_L\qquad(2L>n).
 \tag{C8}
\]
The last bound follows by $V=\lambda Y$ and integration of $(1+|V|^2)^{-L}$.

For the other terms choose a finite $B\ge0$ large enough for all weight comparisons involved. On a pure position shift, (C3) bounds the normalized weight by $C\Xi^B\langle y\rangle^B$; on a pure frequency shift it bounds it by $CX^{\gamma B}\langle\eta\rangle^B$. On a joint shift it is bounded by their product, since $1+A+B'\le(1+A)(1+B')$ for nonnegative $A,B'$. These estimates apply to either amplitude in (C5). Near shifts of the other variable can instead be absorbed by (C2). For example, in the far-near region, compare $w(x+ty,\xi+\eta)$ first with $w(x+ty,\xi)$, using the frequency box; its size depends on $\Xi$, not on the shifted position.

In the far-near term use $(-\Delta_\eta)^L$ on the exponential, producing $|y|^{-2L}$. Each derivative transferred to the amplitude or its near-frequency cutoff gives $\Xi^{-1}$: the shifted frequency bracket is comparable to $\Xi$. Thus, for $2L>n+B$, this term divided by $W$ is bounded by
\[
 C\Xi^{B-2L}
   \int_{|\eta|\le C\Xi}d\eta
   \int_{|y|\ge cX^\gamma}|y|^{-2L}\langle y\rangle^Bdy
 \le C\Xi^{n+B-2L}X^{\gamma(n+B-2L)}\le C.
 \tag{C9}
\]
The elementary radial integral used here is bounded by $C R^{n+B-2L}$ for $R\ge c>0$; on this region $\langle y\rangle\le C_c|y|$.

In the near-far term use $(-\Delta_y)^K$, producing $|\eta|^{-2K}$. Position derivatives and the near-position cutoff cost $X^{-\gamma}$; factors $t$ from differentiation are bounded. Consequently, for $2K>n+B$, the normalized bound is
\[
 CX^{-2\gamma K+\gamma B}
  \int_{|y|\le CX^\gamma}dy
  \int_{|\eta|\ge c\Xi}|\eta|^{-2K}\langle\eta\rangle^B d\eta
 \le CX^{\gamma(n+B-2K)}\Xi^{n+B-2K}\le C.
 \tag{C10}
\]

In the far-far term first perform the $2L$ frequency integrations by parts and then the $2K$ position integrations. Now discard all derivative improvements in (C4), since the shifted brackets are at least one. The normalized differentiated amplitude is bounded by
$CX^{\gamma B}\Xi^B\langle y\rangle^B\langle\eta\rangle^B$.
Derivatives of $|y|^{-2L}$ only improve its decay; the far cutoffs have the same property on their transition regions. The absolute integral is therefore at most
\[
 CX^{\gamma B}\Xi^B
 \int_{|y|\ge cX^\gamma}|y|^{-2L}\langle y\rangle^Bdy
 \int_{|\eta|\ge c\Xi}|\eta|^{-2K}\langle\eta\rangle^B d\eta
 \le CX^{\gamma(n+2B-2L)}\Xi^{n+2B-2K}.
 \tag{C11}
\]
Choose $2L,2K>n+2B$. This is bounded independently of the base point. Only derivatives through these fixed finite orders occurred. Derivatives of the radial cutoffs are bounded on the far regions, whose radii are bounded below by $c>0$, so none changes the claimed polynomial majorant.

Here are the limit and differentiation details. Initially insert extra cutoffs $\chi(\rho y)\chi(\rho\eta)$ and let $\rho\downarrow0$. On each compact set of base points, these cutoffs are identically one on the near-variable supports for all sufficiently small $\rho$. On a far-variable transition their derivatives satisfy $|\partial^\alpha\chi(\rho v)|\le C_\alpha\langle v\rangle^{-|\alpha|}$, uniformly for $0<\rho\le1$. Thus the integrations by parts in (C8)–(C11) give integrable majorants independent of sufficiently small $\rho$. Dominated convergence gives limits; terms containing derivatives of the extra cutoffs tend to zero. The remaining absolutely convergent expressions do not depend on the choice of these extra cutoffs. Increasing $K,L$ supplies the same conclusion for any finite list of derivatives in the base point and makes the convergence locally uniform.

Specifically, each base derivative distributed to an input replaces its weight by $wX^{-\gamma|\alpha|}\Xi^{-|\beta|}$, an admissible weight by Section 1. Apply the value estimate just proved to those differentiated inputs. In $I_t$ the product of the new weights at the base point is exactly $w_1w_2X^{-\gamma|\alpha|}\Xi^{-|\beta|}$. The same statement holds for $T_t$. When differentiating (C7), one obtains the factors $X^{-1}\le X^{-\gamma}$ or $\Xi^{-1}$, with bounded normalized cutoff derivatives; the four estimates apply unchanged. This proves (C4) for every output derivative. It also justifies differentiating the original cutoff limit and proves the required finite-seminorm continuity. $\square$

<a id="quantization-change"></a>
## 3. Changing quantization, with its exact finite error

For real $t$, define
\[
 \operatorname{Op}_t(a)u(x)=(2\pi)^{-n}\iint e^{i(x-y)\cdot\xi}
 a((1-t)x+ty,\xi)u(y)\,dy\,d\xi.
 \tag{C12}
\]
At this stage its kernel is a tempered distribution: take the partial inverse Fourier transform in frequency of the polynomially growing function $a$, then make the displayed invertible linear change of variables. Such transformations on distributions are defined by applying their continuous transformations to Schwartz test functions, with the change-of-variables Jacobian. This definition requires no kernel representation theorem. Pairing the resulting distribution with $\overline{v(x)}u(y)$ defines (C12) on Schwartz tests. Left quantization is $t=0$; Weyl quantization is $t=1/2$; right quantization is $t=1$.

**Theorem 3.1.** The exact left symbol of (C12) is $T_ta$. The maps $T_t$ are automorphisms of $S(w,G_\gamma)$, with $T_tT_s=T_{t+s}$ and inverse $T_{-t}$. For every integer $N\ge1$,
\[
 T_ta=\sum_{|\alpha|<N}\frac{t^{|\alpha|}}{\alpha!}
              \partial_\xi^\alpha D_x^\alpha a+R_{N,t},
 \qquad R_{N,t}\in S(wh^N,G_\gamma),
 \tag{C13}
\]
uniformly for $t$ in a fixed bounded interval. More precisely,
\[
 R_{N,t}=N\sum_{|\alpha|=N}\frac{t^N}{\alpha!}
     \int_0^1(1-v)^{N-1}T_{vt}
          (\partial_\xi^\alpha D_x^\alpha a)\,dv.
 \tag{C14}
\]

**Proof.** With $y=x+z$, the kernel in (C12) uses $a(x+tz,\xi)$. Fourier inversion in $x-y$ gives its left symbol as the second integral in (C5): set the old frequency equal to the new frequency plus $\eta$. For a Schwartz symbol this follows by Fourier inversion and cutoff integration; it also follows from the following explicit full phase-space Fourier calculation. Denote the Fourier variables dual to $(x,\xi)$ by $(k,l)$. Substituting $x'=x+ty$, $\xi'=\xi+\eta$ in (C5) gives
\[
 \widehat{T_ta}(k,l)=e^{it k\cdot l}\widehat a(k,l).
 \tag{C15}
\]
Indeed Fourier inversion of $e^{-iy\cdot\eta}$ in either integration variable evaluates the other at $l$ or $tk$, with total factor $e^{itk\cdot l}$. This is a distributional Fourier-inversion identity: pairing it with a Schwartz function makes it the inverse formula already proved in the Fourier reading. Thus it does not posit an absolutely integrable integral of a constant exponential.

Multiplication by $e^{itk\cdot l}$ preserves Schwartz space continuously, since each of its derivatives is a polynomial times that same bounded exponential. By transposition it is also continuous on tempered distributions. Therefore (C15) defines $T_t$ on that space and proves the group and inverse identities there. To identify it with the function supplied by Lemma 2.1 for a general symbol, replace $a$ by $a_L=a\chi(x/L)\chi(\xi/L)$. These Schwartz symbols converge to $a$ as tempered distributions and have uniformly bounded $S(w,G_\gamma)$ seminorms: on the cutoff transitions $L^{-1}\le C X^{-\gamma}$ or $C\Xi^{-1}$, respectively. The proof of Lemma 2.1 gives local convergence of all derivatives of $T_ta_L$ to its oscillatory formula and uniform polynomial growth. Hence this convergence also holds on Schwartz tests, by dominated convergence. Equation (C15) and the kernel identity consequently pass to the limit. Lemma 2.1 applied to $t$ and $-t$ now proves the asserted automorphism of the symbol class.

Finally apply one-variable Taylor's formula to $v\mapsto a(x+vty,\xi+\eta)$. Repeated integration of its $N$th derivative gives the integral remainder with factor $N/\alpha!$ after the multinomial expansion of $(y\cdot\partial_x)^N$. For each monomial transfer $y^\alpha$ to frequency derivatives in (C5): since $y_j e^{-iy\cdot\eta}=i\partial_{\eta_j}e^{-iy\cdot\eta}$, integration by parts gives $(-i)^{|\alpha|}\partial_\xi^\alpha\partial_x^\alpha$. This is $\partial_\xi^\alpha D_x^\alpha$. Fourier inversion evaluates the polynomial terms at $y=\eta=0$ and gives the finite sum in (C13). The remainder is exactly (C14).

The integrations by parts can first be performed with the extra cutoffs used in Lemma 2.1; their differentiated boundary terms vanish by its estimates after increasing $K,L$ for the finitely many powers of $y$. Thus this Taylor calculation is valid for all the symbols in question. Each differentiated input in (C14) has weight $wh^N$, so Lemma 2.1 and the finite integral in $v$ prove the full remainder assertion. $\square$

<a id="finite-composition"></a>
## 4. The left product and adjoint

**Theorem 4.1.** If $a\in S(w_1,G_\gamma)$ and $b\in S(w_2,G_\gamma)$, their left product is
\[
 c=I_1(a,b)\in S(w_1w_2,G_\gamma).
 \tag{C16}
\]
For every $N\ge1$ it has the exact finite expansion
\[
 c=\sum_{|\alpha|<N}\frac{\partial_\xi^\alpha a\,D_x^\alpha b}{\alpha!}
       +r_N,\qquad r_N\in S(w_1w_2h^N,G_\gamma),
 \tag{C17}
\]
where
\[
 r_N=N\sum_{|\alpha|=N}\frac1{\alpha!}
        \int_0^1(1-t)^{N-1}
          I_t(\partial_\xi^\alpha a,D_x^\alpha b)\,dt.
 \tag{C18}
\]
The formal Hilbert adjoint has left symbol
\[
 a^\dagger=T_1\overline a
   =\sum_{|\alpha|<N}\frac{\partial_\xi^\alpha D_x^\alpha\overline a}{\alpha!}
      +s_N,\qquad s_N\in S(wh^N,G_\gamma).
 \tag{C19}
\]
The constants again involve only finitely many symbol seminorms. All product identities are identities on both $\mathcal S$ and $\mathcal S'$.

**Proof of the formulas.** Lemma 2.1 gives (C16). Taylor-expand $b(x+y,\xi)$ in $y$ with its integral remainder. In each term, transfer $y^\alpha$ from the exponential to $\partial_\xi^\alpha a$; the sign is the one checked in the proof of (C14). Fourier inversion gives the polynomial terms in (C17), and the integral remainder is (C18). Its first input has weight $w_1\Xi^{-N}$ and its second has weight $w_2X^{-\gamma N}$, both admissible. Lemma 2.1, uniformly for $0\le t\le1$, gives exactly the product weight $w_1w_2h^N$. The cutoff and differentiation justification is the same as for (C14).

Conjugating the left kernel and interchanging input and output makes it the right kernel of $\overline a$. Theorem 3.1 therefore gives (C19), including its full error and sign. For example, if $a=x_j\xi_j$, the formula gives $a^\dagger=x_j\xi_j-i$, in agreement with $(x_jD_j)^*=D_jx_j=x_jD_j-i$ on Schwartz functions. The operator assertions are proved next, so the formal calculation is not an assumption about domains. $\square$

<a id="operator-identities"></a>
## 5. Schwartz functions, distributions and exact operator identities

<a id="weighted-schwartz-action"></a>
First every symbol in (C4) defines a continuous map $A:\mathcal S\to\mathcal S$ by
\[
 Au(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi.
 \tag{C20}
\]
To prove it, bound $w$ by a fixed polynomial, as in Section 1. Differentiating in $x$ produces finitely many products of powers of $\xi$, derivatives of $a$, and $\widehat u$. For decay in $x$, integrate by parts with $(1-\Delta_\xi)^M$, using $(1-\Delta_\xi)^M e^{ix\cdot\xi}=X^{2M}e^{ix\cdot\xi}$. The differentiated symbols retain that same polynomial upper bound, and the finitely many differentiated Schwartz transforms decay faster than any polynomial in $\xi$. Choose $M$ so that $X^{-2M}$ dominates the polynomial growth and the desired output Schwartz weight. The resulting absolutely convergent integrals bound each output seminorm by finitely many symbol seminorms and finitely many input Schwartz seminorms. This proves continuity without an $L^2$ assertion.

For completeness, distribution actions here use the bilinear pairing with Schwartz tests. The transpose kernel is the right kernel of $\widetilde a(x,\xi)=a(x,-\xi)$, and its left symbol is $T_1\widetilde a$. Reflection preserves admissibility of the reflected weight, so Theorem 3.1 and (C20) make this transpose a continuous map $\mathcal S\to\mathcal S$. Define $A$ on $\mathcal S'$ by $\langle Au,v\rangle=\langle u,A^{\mathrm{tr}}v\rangle$. The definition is continuous and agrees with (C20) on Schwartz functions. Partial Fourier transformations and multiplication used above have the same distributional meaning, so the kernel and quantization identities already proved agree with these actions.

<a id="weighted-exact-composition"></a>
We now justify that (C16) is actual operator composition. For compactly supported smooth symbols $a,b$, substitute their two kernels. Put the intermediate position $z=x+y$, the first frequency equal to $\xi+\eta$, and keep $\xi$ as the second frequency. The phase becomes $(x-v)\cdot\xi-y\cdot\eta$, where $v$ is the final input. Fubini is legitimate: the intermediate position and both frequencies have bounded supports, and the input is integrable. The resulting kernel is exactly that of $I_1(a,b)$.

For general symbols set $a_L=a\chi(x/L)\chi(\xi/L)$, and likewise $b_L$. Their symbol seminorms are uniformly bounded as observed in Section 3. Moreover
\[
 \operatorname{Op}_L(a_L)=\chi(x/L)A\chi(D/L).
 \tag{C21}
\]
Both cutoff multipliers converge to the identity in every Schwartz seminorm and are uniformly continuous on Schwartz space: apply the product rule, and use rapid decrease on the regions $|x|\ge L$ or $|\xi|\ge L$ for convergence. Consequently $A_LB_Lu\to ABu$ in Schwartz space for every Schwartz $u$. One can see the product convergence directly by writing $A_L(B_Lu-Bu)+(A_L-A)Bu$ and using those uniform seminorm estimates.

Lemma 2.1 gives uniform polynomial bounds for $c_L=I_1(a_L,b_L)$ and local convergence of every derivative to $c=I_1(a,b)$, by the integrable four-region expressions. In the pairing of (C20) with a second Schwartz function, these bounds and the rapid decrease in both $x$ and $\xi$ permit dominated convergence. Hence $\operatorname{Op}_L(c_L)u\to\operatorname{Op}_L(c)u$ in such pairings. The compact-symbol identity therefore proves $AB=\operatorname{Op}_L(c)$ on $\mathcal S$. Taking bilinear transposes gives $\operatorname{Op}_L(c)^{\mathrm{tr}}=B^{\mathrm{tr}}A^{\mathrm{tr}}$ on $\mathcal S$; the definition by duality then proves the identity on every tempered distribution. No density assertion for Schwartz space in a chosen distribution topology is needed.

The same kernel reasoning proves the formal-adjoint pairing identity of (C19) on Schwartz functions. If the relevant symbols give bounded $L^2$ operators, density makes it the identity for their bounded Hilbert adjoints. For unbounded operators the statement remains the exact Schwartz and distribution identity and does not assert equality of unexamined Hilbert-space domains.

The left symbol is unique. If (C20) vanishes for every Schwartz input, fix $\xi_0$ and take $\widehat u_\varepsilon(\xi)=(2\pi)^n\varepsilon^{-n}\rho((\xi-\xi_0)/\varepsilon)$ with $\rho$ compactly supported and smooth and $\int\rho=1$. Such inputs are Schwartz by Fourier inversion. For each fixed $x$, (C20) tends to $e^{ix\cdot\xi_0}a(x,\xi_0)$ by substitution and dominated convergence on the fixed compact support of $\rho$. Thus $a(x,\xi_0)=0$ everywhere. Consequently finite expansions in different orders describe the same exact remainder symbol when the associated exact operator is fixed.

<a id="order-zero-and-use"></a>
## 6. The boundedness and mapping inputs this supplies

If $a\in S(1,G_\gamma)$, all the coordinate derivatives required by the earlier finite-derivative theorem are bounded, since $X^{-\gamma},\Xi^{-1}\le1$. That proved theorem gives
\[
 \|\operatorname{Op}_L(a)\|_{L^2\to L^2}
       \le C\max_{|\alpha|\le k,|\beta|\le k}A_{\alpha\beta}
 \tag{C22}
\]
for a fixed finite $k$ depending on dimension. Theorem 3.1 gives the same conclusion for Weyl or other fixed quantization, since $T_ta\in S(1,G_\gamma)$ with finite-seminorm control. These bounded extensions agree with the distribution actions on $L^2$: approximate by Schwartz functions, use the continuous embedding $L^2\subset\mathcal S'$ from Cauchy–Schwarz, and pass to the limit in both pairings.

<a id="weighted-sobolev-mapping"></a>
In particular the power multipliers $M_t=\langle x\rangle^t$ and $J_s=\langle D\rangle^s$ have weights $X^t$ and $\Xi^s$ for all real $s,t$. Theorem 4.1 makes the symbols of
$J_sM_tJ_{-s}M_{-t}$ and $M_tJ_sM_{-t}J_{-s}$ members of $S(1,G_\gamma)$. Equation (C22) bounds both. The exact distribution identities then give both inequalities between $\|J_sM_tu\|_2$ and $\|M_tJ_su\|_2$, including both finite-norm implications. Likewise, for $a\in S(X^\tau\Xi^\mu,G_\gamma)$, the conjugate
\[
 M_{t-\tau}J_{s-\mu}\operatorname{Op}_L(a)J_{-s}M_{-t}
 \tag{C23}
\]
has weight one and is bounded on $L^2$. Define $H^{s,t}=\{u\in\mathcal S':M_tJ_su\in L^2\}$ with norm $\|M_tJ_su\|_2$. These spaces need no later lemma: the position and Fourier bracket multipliers preserve Schwartz space by the product rule and their polynomial derivative bounds, and have inverses obtained by negating their exponents. Transposition gives the same inverses on distributions. Thus $M_tJ_s$ is an isometric bijection from this space to $L^2$, with inverse $J_{-s}M_{-t}$. Pullback of the complete $L^2$ inner product proves completeness, and pulling back Schwartz approximations in $L^2$ proves density. Equation (C23) now proves the map $H^{s,t}\to H^{s-\mu,t-\tau}$ for all four real exponents. The weighted Sobolev lesson applies these proved facts to rough elliptic expressions; no result from that later application is needed here.

The same reasoning applies uniformly to a family of weights $w_\varepsilon(x)$ and their inverses when their local comparisons, temperateness constants and symbol seminorms are uniform: replace $M_t$ by multiplication by $w_\varepsilon$ in the two conjugates. Their product weight is exactly one. A bound on $\sup_x w_\varepsilon(x)$ is neither used nor required.

Each error in (C13), (C17) and (C19) gains exactly $X^{-\gamma N}\Xi^{-N}$. Thus, when a resolvent calculation chooses $\gamma N\ge1$, its claimed spatial remainder is obtained with that finite number of derivatives and no infinite expansion. The proof concerns (C1); a metric whose frequency derivative scale instead grows with position requires a separate argument. Lerner's free source gives the broader context and the formula correspondence, while Sections 1–6 above supply every symbol-calculus and operator step asserted here.

<a id="moving-coordinate-calculus"></a>
## 7. The separate moving-coordinate metric

We now prove that separate argument. Fix $s\ge1$, $d\ge1$, $0<c<r<1$ with $c+r=1$, and put
\[
 X=X_s(z)=(1+s^2+|z|^2)^{1/2},\qquad
 g_s=X^{-2r}|dz|^2+X^{2c}|d\eta|^2,\qquad h=X^{c-r}.
 \tag{M1}
\]
Throughout this section the weights are $w=s^aX^b$, for arbitrary fixed real $a,b$. This includes every weight in the moving-coordinate application, and is closed under products, inverses and multiplication by $h$. The definition of $S(w,g_s)$ is
\[
 |\partial_\eta^\alpha\partial_z^\beta f_s(z,\eta)|
 \le C_{\alpha\beta}s^aX^{b+c|\alpha|-r|\beta|},
 \tag{M2}
\]
with constants independent of $s,z,\eta$. No frequency support restriction is imposed. Parameter continuity assertions mean continuity in the indicated seminorms. All bounds below use finitely many such seminorms for each requested output seminorm.

**Theorem 7.1.** For this metric and these weights, exact left composition and formal adjoint have the finite expansions
\[
 \begin{aligned}
 f\circ_Lq
 &=\sum_{|\alpha|<K}\frac{\partial_\eta^\alpha f\,D_z^\alpha q}{\alpha!}
          +R_K,& R_K&\in S(w_fw_qh^K,g_s),\\
 f^\dagger
 &=\sum_{|\alpha|<K}\frac{D_z^\alpha\partial_\eta^\alpha\overline f}{\alpha!}
          +r_K,& r_K&\in S(w_fh^K,g_s),
 \end{aligned}
 \tag{M3}
\]
for every positive integer $K$, where $D_z=-i\partial_z$. Operators and adjoints preserve Schwartz space, composition is exact there and by transposition on tempered distributions, and
\[
 f\in S(1,g_s)\quad\Longrightarrow\quad
 \|\operatorname{Op}_L(f_s)\|_{2\to2}\le C
 \tag{M4}
\]
uniformly in $s$. The bounded adjoint agrees with the formal adjoint when these operators are bounded. We prove all three assertions; (M4) is not an input to the symbolic proof.

<a id="moving-oscillatory-estimate"></a>
### The oscillatory estimate at a fixed output point

For $|t|\le1$ define
\[
 \begin{aligned}
 I_t(f,q)(z,\eta)
 &=(2\pi)^{-d}\operatorname{Os}\!\iint e^{-iy\cdot\theta}
                f(z,\eta+\theta)q(z+ty,\eta)\,dy\,d\theta,\\
 T_t a(z,\eta)
 &=(2\pi)^{-d}\operatorname{Os}\!\iint e^{-iy\cdot\theta}
                a(z+ty,\eta+\theta)\,dy\,d\theta.
 \end{aligned}
 \tag{M5}
\]
We will show $I_t:S(w_f)\times S(w_q)\to S(w_fw_q)$ and $T_t:S(w)\to S(w)$, with bounds uniform in this interval of $t$. At the fixed output point set
\[
 y=X^c u,\qquad \theta=X^{-c}v,\qquad Y=X_s(z+tX^cu).
 \tag{M6}
\]
The Jacobian and phase are unchanged. The bracket is $1$-Lipschitz, so $Y/X\le1+|u|$. If $X\ge2Y$, then $X\le Y+X^c|u|$ gives $X^{1-c}\le2|u|$, and $Y\ge1$ gives $X/Y\le(2|u|)^{1/(1-c)}$. If $X<2Y$, the ratio is bounded by $2$. Consequently
\[
 Y/X\le1+|u|,\qquad X/Y\le C\langle u\rangle^{1/(1-c)}.
 \tag{M7}
\]
These estimates are uniform even when the translated point approaches the origin.

Normalize the first amplitude in (M5) by $w_f(z)w_q(z)$ and the second by $w(z)$. Each $u$ derivative of the translated symbol contributes $X^cY^{-r}$; each $v$ derivative of that symbol contributes $X^{-c}Y^c$. For $I_t$, the $v$ derivatives act instead on $f$ at $z$ and contribute $X^{-c}X^c=1$. For every fixed nonnegative integer $J$, (M2) and (M7) therefore imply, for either normalized amplitude $A$,
\[
 |\partial_u^j\partial_v^k A(u,v)|
       \le C_{J,k}\langle u\rangle^{B_J+c|k|}
       \quad (|j|\le J).
 \tag{M8}
\]
Here $B_J$ depends on the fixed weight exponents and $J$, but not on $k,s,z,\eta,t$. To check this independence, separate $Y^{b-r|j|}$ from $Y^{c|k|}$. The former is bounded relative to its output power by (M7), with an exponent depending only on $b,j$; the latter gives $(Y/X)^{c|k|}\le(1+|u|)^{c|k|}$. The extra factor $X^{(c-r)|j|}$ is at most one. Products are treated by the finite Leibniz formula.

Choose an integer $J_0>d/2$. Integration by parts first in $v$, then in $u$, rewrites the normalized integral as the absolutely convergent expression
\[
 (2\pi)^{-d}\iint e^{-iu\cdot v}\langle v\rangle^{-2J_0}
 (1-\Delta_u)^{J_0}
 \left[\langle u\rangle^{-2L}(1-\Delta_v)^L A(u,v)\right]du\,dv.
 \tag{M9}
\]
Indeed its absolute integrand is at most
$C\langle v\rangle^{-2J_0}\langle u\rangle^{-2(1-c)L+B_{2J_0}}$.
After $J_0$ has been fixed, choose $L$ with
$2(1-c)L>B_{2J_0}+d$. Both scalar integrals converge. This order of choices is essential: increasing the frequency differentiation order costs $2cL$ powers of $u$, while integration by parts supplies $2L$.

For a precise meaning of $\operatorname{Os}$, insert smooth cutoffs $\chi(\varepsilon u)\chi(\varepsilon v)$, equal to one near zero and of compact support. Their derivatives are bounded uniformly and tend pointwise to zero when a derivative has fallen on a cutoff. The same integrable majorant, with $L$ enlarged if necessary, bounds every term in (M9). Dominated convergence proves existence, independence of the cutoffs and equality with (M9). Different choices of $J_0,L$ give the same limit. Cutoffs in the unscaled variables have the same limit after (M6), for each fixed output point. Differentiating the original integrands with respect to $z,\eta$ first yields a finite sum of the same integrals with differentiated symbols. Apply (M6) only afterwards. The derivative weights in (M2) multiply to the required output weight; (M7) handles each translated weight. Formula (M9) gives convergence locally uniformly with all these derivatives. This proves smoothness and every asserted symbol seminorm bound for (M5), without differentiating a frozen scale incorrectly.

<a id="moving-finite-formulas"></a>
### Finite Taylor formulas and exact operators

Taylor's formula with integral remainder gives
\[
 q(z+y,\eta)=\sum_{|\alpha|<K}\frac{y^\alpha}{\alpha!}\partial_z^\alpha q(z,\eta)
 +K\sum_{|\alpha|=K}\frac{y^\alpha}{\alpha!}
       \int_0^1(1-t)^{K-1}\partial_z^\alpha q(z+ty,\eta)\,dt.
 \tag{M10}
\]
This multivariable formula follows by applying the one-variable integral Taylor formula to $t\mapsto q(z+ty,\eta)$ and expanding $(y\cdot\partial_z)^j$ by the multinomial identity. The one-variable formula follows by $K$ integrations of the fundamental theorem. Transferring $y^\alpha$ from the phase onto $f$ by $\theta$ integration by parts multiplies the derivative by $(-i)^{|\alpha|}$. Thus $I_1(f,q)$ has the first expansion in (M3), with the exact remainder
\[
 R_K=K\sum_{|\alpha|=K}\frac1{\alpha!}
        \int_0^1(1-t)^{K-1}I_t(\partial_\eta^\alpha f,D_z^\alpha q)\,dt.
 \tag{M11}
\]
For each summand the two differentiated weights have product
$w_fw_qX^{cK-rK}=w_fw_qh^K$. The estimates (M5)–(M9), uniform in $t$, prove every remainder seminorm. Cutoff terms in the integration by parts vanish by the same dominated-convergence argument. In the finite Taylor terms, integration of the phase against a function of $\theta$ evaluates that function at zero. This follows from the Fourier inversion proved in the earlier finite-derivative provider; it also follows by the same regularized delta approximation there. No unevaluated oscillatory constant is used.

The adjoint kernel has right symbol $\overline f$, and conversion of that right kernel to a left kernel gives $T_1\overline f$. Taylor-expand $\overline f(z+y,\eta+\theta)$ in $y$ and transfer $y^\alpha$ in the same way. Its remainder is
\[
 r_K=K\sum_{|\alpha|=K}\frac1{\alpha!}
        \int_0^1(1-t)^{K-1}T_t(D_z^\alpha\partial_\eta^\alpha\overline f)\,dt.
 \tag{M12}
\]
Each input has weight $w_fh^K$, proving the second expansion of (M3). Applying (M10) with $ty$ also proves the finite quantization-change expansion of $T_t$ with coefficient $t^{|\alpha|}$ and the same order of remainder for bounded $t$.

<a id="moving-exact-operators"></a>
Here are the operator-domain details. At fixed $s$, the operator integral against a Schwartz Fourier transform is absolutely convergent in $\eta$. After integration by parts $2N$ times in $\eta$, the cost from a differentiated symbol is at most $X^{b+2cN}$ and the gain is $\langle z\rangle^{-2N}$. Since $c<1$ and $X$ is comparable to $\langle z\rangle$ at fixed $s$, this proves arbitrary output decay. Output derivatives introduce only finitely many powers of $\eta$ and symbol derivatives, absorbed by Schwartz seminorms. It proves continuous preservation of Schwartz space. The symbols $T_1\overline f$ and $T_1(f(z,-\eta))$ satisfy the same bounds, so the adjoint and bilinear transpose have this property as well.

To justify the kernel identities, first take compactly supported smooth symbols. Substitution of their kernels and Fubini give $f\circ_Lq=I_1(f,q)$ by the change of variables used in Section 5; exchanging the kernel variables gives the right-to-left adjoint formula just used. For general symbols insert $\chi(z/R)\chi(\eta/R)$ and let $R\to\infty$. For each fixed $s$ their symbol seminorms are bounded independently of $R\ge1$. For the position cutoff this follows on $|z|\asymp R$ from $X^r/R\le C_s$; for the frequency cutoff use $R^{-1}\le X^c$. The cutoff operators are $\chi(z/R)\operatorname{Op}_L(f)\chi(D/R)$, and converge on Schwartz space, with uniformly bounded Schwartz seminorm estimates. The estimates (M7)–(M9) give locally uniform convergence of every product-symbol derivative and polynomial bounds independent of $R$ at this fixed $s$. In a pairing with two Schwartz functions those bounds allow dominated convergence, proving the exact composition and adjoint identities. Bilinear transposition then defines the operators on $\mathcal S'$ and gives their exact composition there. Uniformity in $s$ for the symbol formulas comes from (M7)–(M12), not from these auxiliary fixed-$s$ cutoffs.

<a id="moving-position-partition"></a>
### Uniform boundedness by a position partition

We use only the previously proved [finite-derivative $L^2$ estimate](finite-derivative-l2.md) and its unitary dilation identity. Let $\phi$ be smooth, nonincreasing, equal to one on $[0,1]$ and zero on $[2,\infty)$. Such a function is obtained by integrating and normalizing a nonnegative smooth bump supported in $(1,2)$. Put $R_j=2^j$ and
\[
 \chi_0(z)=\phi(X),\qquad
 \chi_j(z)=\phi(X/R_j)-\phi(2X/R_j)\quad(j\ge1).
 \tag{M13}
\]
They sum to one, have uniformly finite overlap, and for $j\ge1$ are supported where $R_j/2\le X\le2R_j$; the $j=0$ support has $1\le X\le2$. Repeated differentiation of $X$ gives $|\partial_z^\beta X|\le C_\beta X^{1-|\beta|}$, by induction on its explicit square root, so $|\partial_z^\beta\chi_j|\le C_\beta R_j^{-|\beta|}$. Choose $0\le\widetilde\chi_j\le1$, identically one on a neighbourhood of this support, with the larger support $R_j/4<X<4R_j$ and the same derivative bounds. For $j=0$ use a cutoff equal to one for $X\le2$ and zero for $X\ge4$. These larger supports also have uniformly finite overlap.

For $f\in S(1,g_s)$ set $f_j=\chi_j f$ and $F_j=\operatorname{Op}_L(f_j)$. Leibniz's rule gives, globally,
\[
 |\partial_\eta^\alpha\partial_z^\beta f_j|
          \le C_{\alpha\beta}R_j^{c|\alpha|-r|\beta|}.
 \tag{M14}
\]
Under the unitary dilation with position scale $R_j^c$, the transformed symbol is $f_j(R_j^c z,R_j^{-c}\eta)$. Its coordinate derivatives are bounded by $C_{\alpha\beta}R_j^{(c-r)|\beta|}\le C_{\alpha\beta}$. The finite-derivative theorem therefore gives $\|F_j\|\le C$ using one fixed finite list of seminorms. Because the output of $F_j$ is supported in $\operatorname{supp}\chi_j$, finite overlap gives
\[
 \left\|\sum_j F_j\widetilde\chi_j u\right\|_2^2
 \le C\sum_j\|F_j\widetilde\chi_j u\|_2^2
 \le C'\sum_j\|\widetilde\chi_j u\|_2^2
 \le C''\|u\|_2^2.
 \tag{M15}
\]
The series converges in $L^2$: the same bound on its tails and scalar dominated convergence apply to the locally finite input cutoffs.

<a id="moving-far-input"></a>
It remains to sum $F_j(1-\widetilde\chi_j)$, for which pointwise kernel estimates at bounded frequencies would be insufficient. Write $\psi_j=1-\widetilde\chi_j$. Every finite Taylor coefficient in the exact symbol of $F_j\psi_j$ is zero, since all derivatives of $\psi_j$ vanish on a neighbourhood of $\operatorname{supp} f_j$. In the remainder (M11), use the fixed scale $y=R_j^cu$, $\theta=R_j^{-c}v$. All derivatives of $\psi_j$ have the global bounds $|\partial_z^\beta\psi_j|\le C_\beta R_j^{-|\beta|}$. Thus $\partial_\eta^\alpha f_j$ for $|\alpha|=K$ contributes $R_j^{cK}$ and $D_z^\alpha\psi_j$ contributes $R_j^{-K}$. After factoring out $R_j^{-(1-c)K}=R_j^{-rK}$, every $u,v$ derivative of the normalized amplitude is uniformly bounded. The integration by parts (M9), now with bounded amplitudes and no translated variable weight, proves for the exact remainder symbol $e_j$ that
\[
 |\partial_\eta^\alpha\partial_z^\beta e_j|
       \le C_{K,\alpha\beta}R_j^{-rK}
                                R_j^{c|\alpha|-r|\beta|}.
 \tag{M16}
\]
For output derivatives on $\psi_j$, its stronger gain $R_j^{-1}$ is at most $R_j^{-r}$; for frequency derivatives all the differentiation is on $f_j$. This verifies the displayed exponents for every derivative, not just the size of the amplitude. All integrands retain the output support of $f_j$. Applying the same dilation and the finite-derivative theorem gives
$\|F_j\psi_j\|\le C_K R_j^{-rK}$.

<a id="moving-uniform-bound"></a>
Since $r>0$, even $K=1$ makes $\sum_{j\ge0}R_j^{-rK}$ finite. The far-input series therefore converges in operator norm with a uniform bound. Together with (M15) it proves (M4). On Schwartz functions the sum equals $\operatorname{Op}_L(f)$, by the locally finite output partition, so this bounded operator is the required extension. There is no appeal here to a variable-metric boundedness theorem.

<a id="moving-integrable-tail"></a>
Finally, $q\in S(s^{-\delta}X^{-1},g_s)$ with $\delta=r-c$ satisfies $s^{1+\delta}q\in S(1,g_s)$ because $s/X\le1$. We have proved
\[
 \|\operatorname{Op}_L(q_s)\|\le C s^{-1-\delta}.
 \tag{M17}
\]
More generally any scalar multiple of a symbol with bounded weight has the corresponding multiple of the bound (M4). Continuity in finitely many input seminorms passes through (M9), the finite sums (M11)–(M12), and (M15)–(M16); hence all these statements hold uniformly for families, and give operator-norm continuity when those seminorms vary continuously.

The free source for the finite composition and quantization-change correspondence is Lerner's [author-hosted Chapter 2](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf#page=35), Theorems 2.3.7, 2.3.18 and 2.3.19, printed pp. 91–92 and 100. Its Theorem 2.5.1, printed pp. 111–112, proves a more general variable-metric $L^2$ theorem by metric partitions and almost orthogonality. The source uses the Fourier phase $2\pi z\cdot\xi$; the change $\eta=2\pi\xi$ converts its first left-product correction to $-i\partial_\eta f\cdot\partial_zq$, exactly (M3). Section 7 gives its own full proof for (M1)–(M2), including boundedness by the position partition above, so none of these source theorems is being used as an unproved prerequisite.
