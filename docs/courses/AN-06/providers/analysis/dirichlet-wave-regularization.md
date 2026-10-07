# Dirichlet wave regularization at every negative order

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="dirichlet-wave-regularization"></a>

This reading constructs the spectral Dirichlet wave for compactly supported interior data of every finite negative Sobolev order. An inverse power gives a wave of arbitrarily high prescribed finite regularity, preserves the wave equation and Dirichlet condition, and preserves its interior wavefront set. The regularized initial data are smooth near the boundary, with every iterated Dirichlet compatibility condition. Thus their nonlocality introduces no artificial singular boundary data. This proves a reduction to finite-energy propagation; it does not prove that propagation theorem.

Read [Smooth Dirichlet regularity, power domains, and projector growth](smooth-dirichlet-powers.md#smooth-dirichlet-powers), especially its local boundary estimates and Theorems 4.1 and 5.1; [Compact positive inverses and diagonal domains](compact-spectrum-domains.md#all-diagonal-multipliers-and-ordered-domains); the [finite scalar calculus and elliptic parametrix](classical-scalar-calculus.md#elliptic-parametrix-domains); and the [Fourier definition and cutoff estimates for wavefront sets](phase-geometry-and-stationary-phase.md#phase-wavefront). The compact spectral comparison is Gerald Teschl's free [*Mathematical Methods in Quantum Mechanics*, second author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), Section 6.2, Theorem 6.6. The second-order boundary comparison is John K. Hunter's free [*Notes on Partial Differential Equations*, revised 18 June 2014](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), Theorem 4.30, printed pp. 115–116. The higher boundary induction is in [Smooth Dirichlet regularity, Section 3](smooth-dirichlet-powers.md#smooth-dirichlet-induction). The reduction and wavefront argument below use that induction together with the exact power domains.

<a id="dirichlet-negative-spectral-spaces"></a>

## 1. The exact spectral spaces and interior distributions

Let $X$ and $P$ be the full compact smooth scalar Dirichlet setting of the boundary lesson: no corners, positive quadratic principal symbol $p$, arbitrary smooth formally self-adjoint lower terms, and a strictly positive Dirichlet realization. Its proved orthonormal eigenbasis is $e_j$, with $Pe_j=\lambda_je_j$, $\lambda_j>0$. Put

\[
 A=1+P,\qquad a_j=1+\lambda_j.
 \tag{W1}
\]

The earlier exact domain formula shows $D(A^m)=D(P^m)$ for every nonnegative integer $m$, with equivalent graph norms: the weights $a_j^{2m}$ and $1+\lambda_j^{2m}$ are comparable. In particular

\[
 \|v\|_{H^{2m}(X)}\leq C_m\|A^mv\|_2,
       \qquad v\in D(A^m).
 \tag{W2}
\]

For any real $s$, define the complete coefficient space

\[
 \mathcal H_D^s
   =\left\{c=(c_j):\|c\|_{s,D}^2
                       :=\sum_j a_j^s|c_j|^2<\infty\right\}.
 \tag{W3}
\]

Completeness and density of finite sequences follow by multiplication by $a_j^{s/2}$ and the proved completeness of $\ell^2$. For $s\geq0$ the eigenbasis identifies it with $D(A^{s/2})$. For negative $s$ it is the coefficient completion. We will define its interior distributional action explicitly; no identification with all distributions on the closed manifold, or with unspecified boundary traces, is being assumed.

We use the anti-dual convention: $\langle f,\phi\rangle$ is linear in $f$ and conjugate-linear in the test function. Every interior compact smooth $\phi$ belongs to every $D(A^m)$: its iterated differential expressions are still compactly supported in the interior and satisfy the proved recursive domain conditions. Hence a coefficient vector $c\in\mathcal H_D^{-2m}$ acts by

\[
 \begin{aligned}
 \langle c,\phi\rangle
       &=\sum_j c_j\overline{(\phi,e_j)},\\
 |\langle c,\phi\rangle|
       &\leq\|c\|_{-2m,D}\|A^m\phi\|_2.
 \end{aligned}
 \tag{W4}
\]

This is an absolutely convergent Cauchy–Schwarz pairing and a distributional bound on each fixed compact test support. Every real $s$ embeds continuously in some $\mathcal H_D^{-2m}$, so (W4) defines the needed interior action in all cases. The action of the coefficient multiplier $A$ agrees with the differential expression on interior tests: move $A$ to the test in (W4), where its eigenfunction coefficients are multiplied by $a_j$. The same argument works for every integer power.

Let $K\Subset X^\circ$ and let $f\in H^{-2M}$ have support in $K$, where $M\geq0$ is an integer. Define $f_j=\langle f,\chi e_j\rangle$ with $\chi\in C_c^\infty(X^\circ)$ equal to one near $K$. This is independent of $\chi$, because a distribution supported in $K$ annihilates a test vanishing near $K$. For a finite eigenfunction sum $v$, Sobolev duality, smooth multiplication and (W2) give

\[
 |\langle f,\chi v\rangle|
       \leq C_{K,M}\|f\|_{H^{-2M}}\|A^Mv\|_2.
 \tag{W5}
\]

Take $v_j=a_j^{-2M}f_j$ on any finite index set and zero elsewhere. The left side of (W5) is the nonnegative sum $S=\sum a_j^{-2M}|f_j|^2$ and the last norm is $S^{1/2}$. Thus

\[
 \sum_j a_j^{-2M}|f_j|^2
          \leq C_{K,M}^2\|f\|_{H^{-2M}}^2.
 \tag{W6}
\]

The coefficient distribution (W4) is the original $f$. Indeed the finite eigenfunction sums of an interior compact smooth $\phi$ converge to $\phi$ in every $D(A^m)$ by the exact weighted-sum domain. By (W2) they converge in $H^{2M}$, so multiplication by $\chi$ and pairing with $f$ pass to the limit and give precisely (W4). This also proves injectivity on these compactly supported interior data.

The fixed-support negative spaces in the lesson are covered for every $M$. More generally each compactly supported distribution belongs to one such space: its finite-order test estimate gives a polynomial Fourier bound after a coordinate cutoff, and a sufficiently negative squared Sobolev weight makes that polynomial integrable. A finite interior chart partition proves the assertion on $X$.

<a id="dirichlet-exact-wave-regularization"></a>

## 2. The wave and exact regularization

Take $f,g$ as in Section 1, increasing $M$ if their orders differ. Define

\[
 u_j(t)=\cos(t\sqrt{\lambda_j})f_j
      +\frac{\sin(t\sqrt{\lambda_j})}{\sqrt{\lambda_j}}g_j.
 \tag{W7}
\]

For each finite time interval $I$ and nonnegative integer $k$, the $k$th derivatives of the two multipliers have absolute value at most $C_{I,k}a_j^{k/2}$. For the sine multiplier at $k=0$, use $|\sin(t\sqrt\lambda)|/\sqrt\lambda\leq|t|$. At $k\geq1$ its bound is at most $\lambda_j^{(k-1)/2}$; the cosine derivative is bounded by $\lambda_j^{k/2}$. The weighted squares are therefore summable by (W6). Finite sums, the scalar fundamental theorem and dominated convergence prove

\[
 \begin{gathered}
 u\in C^k(I;\mathcal H_D^{-2M-k}),\\
 \partial_t^2u+Pu=0,\\
 u(0)=f,\qquad\partial_tu(0)=g.
 \end{gathered}
 \tag{W8}
\]

For clarity about differentiation, the difference quotient of the $(k-1)$st scalar multiplier is bounded by the supremum of its $k$th derivative on a slightly larger compact interval. The same summable bound controls that quotient in the target coefficient norm, so its limit is the displayed termwise derivative. Equation (W8) is first an identity in the indicated coefficient spaces and then an interior distribution identity by (W4). The initial derivative is interpreted in $\mathcal H_D^{-2M-1}$, where the same limit proves it. This constructs the spectral Dirichlet solution used in the lesson; it is not an assertion of uniqueness among unspecified distributional boundary realizations.

For a positive integer $N$ define $v=A^{-N}u$ coefficientwise. Direct multiplication proves

\[
 \|A^{-N}c\|_{s+2N,D}=\|c\|_{s,D},\qquad
 u=A^Nv,
 \tag{W9}
\]

and, without a commutator error,

\[
 \begin{aligned}
 \partial_t^2v+Pv&=0,\\
 v(0)&=A^{-N}f,\qquad
 \partial_tv(0)=A^{-N}g.
 \end{aligned}
 \tag{W10}
\]

All operators here are diagonal on the same original Dirichlet realization. For any prescribed integer $q\geq1$, choosing $N\geq M+q+1$ gives

\[
 v\in C^2(I;D(A^q))\subset C^2(I;H^{2q}(X)).
 \tag{W11}
\]

Indeed (W8)–(W9) put the $k$th derivative, $0\leq k\leq2$, in $\mathcal H_D^{2N-2M-k}$, whose exponent is at least $2q$. Its continuous inclusion into $D(A^q)$ is immediate from the weights. The graph-domain description supplies zero Dirichlet value at every time. Taking $q=1$ gives more than finite energy; taking larger $q$ supplies any fixed finite number of spatial derivatives needed in an estimate. A fixed $N$ is not asserted to make arbitrary rough data infinitely smooth.

The unregularized solution also has a precise distributional homogeneous boundary condition. If $\vartheta\in C_c^\infty(\mathbb R_t)$, let $h_\lambda(t)$ be either $\cos(t\sqrt\lambda)$ or $\sin(t\sqrt\lambda)/\sqrt\lambda$. Since $h_\lambda''=-\lambda h_\lambda$, integration by parts $2L$ times gives $\int\vartheta h_\lambda=(-1)^L\lambda^{-L}\int\vartheta^{(2L)}h_\lambda$. No endpoint terms remain because the test is compactly supported. For $\lambda\geq1$, the absolute value is at most $\lambda^{-L}\|\vartheta^{(2L)}\|_{L^1}$ for either multiplier. For $0<\lambda<1$, use $|\cos(t\sqrt\lambda)|\leq1$ and $|\sin(t\sqrt\lambda)|/\sqrt\lambda\leq|t|$ on the fixed test support. Together these give arbitrary inverse powers of $1+\lambda$, bounded by finitely many test seminorms. Thus

\[
 u_\vartheta:=\int\vartheta(t)u(t)\,dt
                         \in\bigcap_{m\geq0}D(A^m).
 \tag{W12}
\]

For each target $m$, (W6) and sufficiently many integrations by parts give its graph-norm bound by a fixed finite number of seminorms of $\vartheta$. The power-domain proof makes $u_\vartheta$ smooth up to the boundary and gives $u_\vartheta|_{\partial X}=0$. This continuously defines the zero boundary distribution after time testing. It does not manufacture a pointwise-in-time trace for the original negative-order solution.

<a id="dirichlet-interior-data-decomposition"></a>

## 3. A compact interior decomposition of the rough datum

The nonlocality of $A^{-N}$ must be checked. We first prove that for each fixed $K,M$ as above there are compactly supported interior functions $b\in L^2$ and $c\in C_c^\infty$ such that

\[
 \begin{gathered}
 f=A^Mb+c,\\
 \|b\|_2+\|c\|_{H^r}\leq C_{K,M,r}\|f\|_{H^{-2M}}\\
 (r\geq0).
 \end{gathered}
 \tag{W13}
\]

Their supports lie in a fixed compact subset of $X^\circ$. For $M=0$, take $b=f,c=0$. For $M>0$, first suppose that $K$ lies compactly inside one interior coordinate patch. Use the already proved scalar parametrix construction for the elliptic differential operator $A^M$ on a larger interior neighborhood of $K$. Its properly supported right parametrix $E$ has order $-2M$ and satisfies $A^ME=I-S$ on that neighborhood, with smooth-kernel $S$. This is the reciprocal principal symbol, finite corrections and cutoff summation of (FC17), with position cutoffs equal to one on the retained neighborhood; no boundary parametrix is being used.

Choose $\eta\in C_c^\infty(X^\circ)$ equal to one near $K$ with support inside that neighborhood, and set $b=\eta Ef$. The order mapping theorem gives $b\in L^2$ with the stated bound. The exact product rule gives

\[
 A^Mb=f-\eta Sf+[A^M,\eta]Ef.
 \tag{W14}
\]

The last term is smooth: the differentiated cutoff is separated from $K$, so the kernel of $E$ between these sets is smooth by the proved integration-by-parts estimate for the scalar kernel off its diagonal. Pairing that smooth kernel with the fixed-support $H^{-2M}$ datum gives every output derivative continuously. The same statement holds for $Sf$. Hence $c=\eta Sf-[A^M,\eta]Ef$ is compactly supported and obeys every bound in (W13).

For a general $K$, choose a finite smooth partition $\rho_\ell$ whose sum is one near $K$, with each $K_\ell=K\cap\operatorname{supp}\rho_\ell$ compactly inside one interior chart. Apply the construction just given to $f_\ell=\rho_\ell f$, with a separate cutoff $\eta_\ell$ equal to one near $K_\ell$. Extend its compactly supported $b_\ell,c_\ell$ by zero and put $b=\sum_\ell b_\ell$, $c=\sum_\ell c_\ell$. The identities $f_\ell=A^Mb_\ell+c_\ell$ sum to (W13). There is no commutation of $A^M$ past $\rho_\ell$: that partition was applied to the datum before inversion. Smooth multiplication bounds the finitely many input norms, so the same estimates hold. This proves (W13) without a chart-edge error.

In the coefficient pairing, choose the cutoff to equal one near the union of the supports of $f$, $b$ and $c$; this does not change $f_j$. Integration by parts in (W13) moves $A^M$ onto this cutoff eigenfunction. Derivatives of the cutoff vanish near the support of $b$, leaving $a_j^Mb_j$. Thus the equality also holds in coefficient form, $f_j=a_j^Mb_j+c_j$. Multiplying by $a_j^{-N}$ gives, for $N>M$,

\[
 A^{-N}f=A^{-(N-M)}b+A^{-N}c.
 \tag{W15}
\]

Both terms on the right are positive inverse powers of the original Dirichlet realization applied to interior-supported $L^2$ data.

<a id="dirichlet-compatible-collar-data"></a>

## 4. No artificial boundary singularities

Let $b\in L^2$ be supported in a fixed compact interior set, and put $w_k=A^{-k}b$, $k\geq1$. Each $w_k$ belongs to $D(A)$ and solves

\[
 \begin{gathered}
 Aw_1=b,\qquad Aw_k=w_{k-1}\ (k>1),\\
 w_k|_{\partial X}=0.
 \end{gathered}
 \tag{W16}
\]

The first right side is zero on a collar disjoint from the support. The local higher boundary estimate proved in Sections 2–3 of the smooth Dirichlet reading therefore makes $w_1$ smooth on a smaller collar. Here is its use without a hidden global smoothness assumption. Start with $w_1\in H^2$. On nested half patches, commute a cutoff through $A$; its commutator has order one. If $w_1$ is already in $H^{r+1}$ on the larger patch, the commutator is in $H^r$, and the local estimate raises regularity to $H^{r+2}$ on the smaller patch. For any fixed derivative order a finite nested chain fits between the original collar and a fixed smaller one. This proves all orders there. For $k>1$, induction gives a smooth right side near the boundary, and the same argument applies. The estimates also give continuous bounds for each fixed collar seminorm in terms of $\|b\|_2$.

Equation (W15) proves that $A^{-N}f$ is smooth near $\partial X$, with zero boundary value. More is true: every iterated compatibility condition holds there. For an integer $j\geq0$, the coefficient identity is

\[
 A^jA^{-N}f=A^{j+M-N}b+A^{j-N}c.
 \tag{W17}
\]

When an exponent on the right is negative, (W16) makes that term smooth with zero boundary trace. When it is nonnegative, it is a differential operator applied to an interior-supported distribution, so it vanishes on the collar. Thus the right side always has a smooth collar representative with trace zero. Differential equality on interior tests from (W4) identifies it with the corresponding derivative of the smooth collar function $A^{-N}f$. Since $P=A-1$, the finite binomial expansion yields

\[
 \begin{gathered}
 (P^jA^{-N}f)|_{\partial X}=0\\
 \hbox{for every integer }j\geq0.
 \end{gathered}
 \tag{W18}
\]

Apply the same proof to $g$. The regularized initial data may be nonzero away from their original supports, but they are smooth near the boundary and satisfy all these boundary compatibility conditions. No new singular initial covector has appeared at the wall.

<a id="dirichlet-interior-wavefront-equality"></a>

## 5. The interior microlocal equality

Use the Fourier convention $\widehat z(\xi)=\int e^{-ix\cdot\xi}z(x)\,dx$, with inverse factor $(2\pi)^{-n}$, and the same convention for the symbol in its position variable. We first prove the elliptic wavefront fact needed here. For a properly supported scalar pseudodifferential operator $B$ with compact local position support, its left symbol obeys

\[
 \begin{gathered}
 \widehat{Bz}(\eta)=(2\pi)^{-n}\\
 {}\times\int\widehat b(\eta-\xi,\xi)\widehat z(\xi)\,d\xi,\\
 |\widehat b(\theta,\xi)|\leq C_L\langle\theta\rangle^{-L}
                                      \langle\xi\rangle^{m}.
 \end{gathered}
 \tag{W19}
\]

The second inequality is repeated integration by parts in the compact position variable. For a distribution localized to a compact set, its Fourier transform has polynomial growth. In a smaller regular output cone, split the integral into a slightly larger regular input cone and its complement. In the first part the input decreases rapidly. Where $|\xi|\geq|\eta|/2$, this supplies any desired output decay, leaving an integrable power of $\xi$ after choosing the input decay order. Where $|\xi|<|\eta|/2$, the factor $\langle\eta-\xi\rangle^{-L}$ supplies that decay instead, and $L$ can be increased arbitrarily. In the complementary input cone, angular separation gives $|\eta-\xi|\geq c(|\eta|+|\xi|)$, and the arbitrary power $L$ dominates the polynomial input bound. This proves rapid output decrease. Spatially separated inputs have a smooth kernel contribution by the earlier off-diagonal calculation. Thus $\operatorname{WF}(Bz)\subset\operatorname{WF}(z)$. The same separated-cone argument shows that a symbol vanishing on a conic neighborhood of a selected nonzero phase point at all sufficiently large frequencies cannot produce a wavefront there; bounded frequencies give a smooth kernel.

If a scalar differential operator $L$ is elliptic at that phase point, its principal symbol has a reciprocal with the usual symbol estimates on a slightly larger closed cone. Choose nested smooth phase cutoffs and repeat the finite inverse recursion and cutoff summation of (FC17) on this cone. At every step the reciprocal cancels the current leading error where the inner cutoff is one; cutoff errors are supported outside that smaller phase neighborhood. The resulting properly supported $B$ satisfies $BL=I+R$ microlocally there: on the inner neighborhood the symbol of $R$ decreases with every derivative faster than every power, and its remaining symbol vanishes near the point. Both parts give a regular output there by (W19) and the smooth-kernel estimate. Consequently

\[
 \begin{gathered}
 \operatorname{WF}(Lz)=\operatorname{WF}(z)\\
 \hbox{at every elliptic point of }L.
 \end{gathered}
 \tag{W20}
\]

Indeed the forward inclusion is pseudolocality, while $z=BLz-Rz$ gives the reverse one. This is the actual local parametrix argument, rather than an external elliptic-regularity citation.

Apply (W20) in the spatial interior to $A^N$, whose principal symbol is $p(x,\xi)^N>0$ for $\xi\ne0$. Equations (W9) and (W10) give

\[
 \begin{aligned}
 \operatorname{WF}(A^{-N}f)&=\operatorname{WF}(f),\\
 \operatorname{WF}(A^{-N}g)&=\operatorname{WF}(g)
                     \qquad\text{in }T^*X^\circ\setminus0.
 \end{aligned}
 \tag{W21}
\]

In interior spacetime, (W8) and (W10), followed by the same parametrix argument for the wave differential operator, place both wavefront sets in $\tau^2=p(x,\xi)$. On that nonzero characteristic set, $\xi\ne0$. On a small conic neighborhood of each such point, $p(x,\xi)^N$ is bounded below by a positive constant times $(|\tau|+|\xi|)^{2N}$. Hence the spatial differential operator $A_x^N$ is elliptic as a spacetime operator on precisely that neighborhood. Since $u=A_x^Nv$, (W20) proves

\[
 \operatorname{WF}(u)=\operatorname{WF}(v)
             \qquad\text{in }T^*(\mathbb R\times X^\circ)\setminus0.
 \tag{W22}
\]

At pure-time covectors with $\xi=0$, the wave operator is elliptic, so both wavefront sets are absent; those covectors have not been incorrectly treated as elliptic for $A_x^N$.

<a id="dirichlet-regularization-transfer"></a>

## 6. Exact use in the boundary lesson

For every fixed-support $H^{-2M}$ datum used in the cosine-kernel argument, take $g=0$ and $N\geq M+2$. Equations (W8)–(W11) give a finite-energy Dirichlet wave $v$. Its interior initial wavefront equals that of $f$ by (W21); Section 4 gives smooth, fully compatible collar data; and (W22) identifies its interior spacetime wavefront with that of the original spectral wave $u$.

Consequently, a finite-energy propagation theorem with these initial-data hypotheses transfers to the original negative-order spectral solution: apply that theorem to $v$, replace its initial and spacetime wavefront sets by the equal sets in (W21)–(W22), and retain the same generalized reflected curves and all permitted endpoint lifts. This deduction loses no wavefront directions and places no additional restriction on glancing contact.

For the finite-energy theorem, see [Cauchy-data propagation for Dirichlet waves](diffractive-phase-neighborhoods.md#dirichlet-cauchy-endpoints), Sections 71–75, and its [singular-curve construction](diffractive-phase-neighborhoods.md#singular-generalized-curves), Sections 63–70. That analytic argument includes the incoming-edge bounds, the spatial-cutoff forcing, the regularizer commutators, the local energy recovery and the induction through arbitrary glancing contacts. The geometric relation, its existence and continuation are proved in [Generalized reflected curves](generalized-reflected-curves.md#generalized-reflected-curves). The present reading supplies the negative-order reduction used by those propagation arguments; curved spectral asymptotics also require the separate local wave comparison.
