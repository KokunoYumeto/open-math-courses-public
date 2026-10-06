# Boundary traces near a real normal root

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="real-normal-root-trace"></a>

This reading proves the small-constant trace estimate for a normal first-order system near a real root, including arbitrary finite nilpotent blocks, Hilbert-valued inputs and small bounded operator perturbations. Sections 6–10 prove its tangentially localized form for matrix differential systems and the actual variable-coefficient scalar wave operator, with cutoff errors and weak traces included. It is one input to a boundary microlocal energy argument. It does not prove that energy argument, generalized propagation, or the curved spectral-projector remainder required in [Generalized rays and the Dirichlet Weyl law](../../src/generalized-rays-and-the-dirichlet-weyl-law.md).

The freely accessible comparison is Victor Ivrii's [*Microlocal Analysis, Sharp Spectral Asymptotics and Applications*, author version of July 9, 2023](https://www.math.utoronto.ca/ivrii/Victor_Ivrii_Microlocal_Analysis,_Sharp_Spectral_Asymptotics_and_Applications.pdf), Proposition 3.1.14, printed pp. 218–219, and its proof, pp. 223–225. We give the finite normal estimate by a polynomial averaging argument. The tangential operator bound uses the independently proved [Gaussian-packet norm estimate, Theorem 4](weighted-positivity.md#high-frequency-norm), whose free comparison is [Nicolas Lerner's author Chapter 2, Proposition 2.4.3](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), printed pp. 101–103. Read that theorem, its bounded-amplitude Lemma 2, and the [finite scalar product proof](classical-scalar-calculus.md#finite-scalar-calculus) before Sections 6–10. We write the specific semiclassical products and errors below; neither free citation replaces their proof.

The vector integration, fundamental theorem and bounded-operator product rule are the written programme proofs in [Hilbert-valued integration](hilbert-valued-integration.md), Sections 1–4. Scalar integrals and Cauchy–Schwarz have the earlier proofs linked there. We take complex Hilbert spaces, with inner products linear in the first entry, and write $D_t=-i\partial_t$.

## 1. A polynomial average that recovers the initial value

Fix an integer $r\geq1$. Let $G$ be the real $r\times r$ matrix indexed by $0\leq j,k<r$ with

\[
 G_{jk}=\int_0^1 s^{j+k}\,ds=\frac1{j+k+1}.
 \tag{N1}
\]

It is positive definite. Indeed for a nonzero complex vector $a$,

\[
 a^*Ga=\int_0^1\left|\sum_{j=0}^{r-1}a_js^j\right|^2ds>0.
\]

The strict inequality follows because a continuous function with zero squared integral vanishes everywhere; a polynomial vanishing on an interval has all coefficients zero by differentiating at zero. Thus $Ga=0$ forces $a=0$. Successive elimination in a finite-dimensional system then makes $G$ invertible. For clarity, the first positive pivot permits eliminating the first column and row; its Schur complement is positive definite because its quadratic form is the original one minimized over the first variable. Repeating gives nonzero pivots and the unique solution of every right-hand side. No infinite-dimensional inverse theorem is involved.

Let $b=G^{-1}(1,0,\ldots,0)^T$ and set

\[
 w_r(s)=\sum_{j=0}^{r-1}b_js^j,
 \qquad c_r^2=\int_0^1|w_r(s)|^2ds>0.
 \tag{N2}
\]

The defining linear system says exactly

\[
 \int_0^1w_r(s)s^j\,ds=\delta_{j0}
 \quad(0\leq j<r).
 \tag{N3}
\]

Consequently, for every polynomial $p$ of degree less than $r$ with coefficients in any complex Banach space,

\[
 p(0)=\int_0^Rw_{r,R}(t)p(t)\,dt,
 \qquad w_{r,R}(t)=R^{-1}w_r(t/R),
 \qquad \|w_{r,R}\|_{L^2(0,R)}=c_rR^{-1/2}.
 \tag{N4}
\]

To verify the identity expand the finite sum for $p$, change variables $t=Rs$, and use (N3) term by term. The norm identity follows from the same change of variables. No positivity of $w_r$ is asserted or needed. For example, $w_1=1$, while $w_2(s)=4-6s$ and $c_2^2=4$.

## 2. The exact nilpotent evolution and the finite-interval estimate

Let $H$ be a complex Hilbert space, without a separability assumption, and let $N:H\to H$ be bounded with $N^r=0$. Put

\[
 U(t)=\sum_{j=0}^{r-1}\frac{(itN)^j}{j!},
 \qquad M_R=\sum_{j=0}^{r-1}\frac{R^j\|N\|^j}{j!}.
 \tag{N5}
\]

Multiplying the two finite polynomials and grouping equal powers of $N$ gives $U(t)U(s)=U(t+s)$: for each surviving power use the binomial formula, while every power at least $r$ is zero. Differentiation gives $U'=iNU$, and $U(-t)$ is the inverse. Also $\|U(t)\|\leq M_R$ for $0\leq t\leq R$.

Let $v:[0,R]\to H$ be a norm primitive of an $L^2$ function plus a fixed vector; thus $v$ is continuous, $v'$ exists almost everywhere in norm, and $v'$ belongs to $L^2(0,R;H)$. This is the concrete $H^1$ representative used below. Set $f=(D_t-N)v$. The bounded-operator product rule and the vector fundamental theorem give

\[
 v(t)=U(t)v(0)+i\int_0^tU(t-s)f(s)\,ds.
 \tag{N6}
\]

In detail, $v'=iNv+if$ and therefore $(U(-t)v(t))'=iU(-t)f(t)$ almost everywhere. Integrate and multiply by $U(t)$. Every integral exists by the norm bound in the integration reading; on a finite interval $L^2\subset L^1$ by Cauchy–Schwarz.

Write the integral term in (N6) as $F(t)$. Pointwise Cauchy–Schwarz, followed by scalar integration, proves

\[
 \begin{aligned}
 \|F(t)\|^2&\leq M_R^2 t\int_0^t\|f(s)\|^2ds,\\
 \|F\|_{L^2(0,R;H)}^2
 &\leq \frac{M_R^2R^2}{2}\|f\|_{L^2(0,R;H)}^2.
 \end{aligned}
 \tag{N7}
\]

For the second inequality interchange the nonnegative scalar integrals: the coefficient of $\|f(s)\|^2$ is $M_R^2\int_s^Rt\,dt\leq M_R^2R^2/2$. The polynomial $U(t)v(0)$ has degree at most $r-1$. Apply (N4) to it and substitute (N6). The vector integral norm estimate and Cauchy–Schwarz yield

\[
 \|v(0)\|\leq c_rR^{-1/2}\|v\|_{L^2(0,R;H)}
       +c_rM_R(R/2)^{1/2}\|f\|_{L^2(0,R;H)}.
\]

Write $\|v\|_R=\|v\|_{L^2(0,R;H)}$. Squaring with $(a+b)^2\leq2a^2+2b^2$ proves the precise finite-interval estimate

\[
 \begin{aligned}
 \|v(0)\|^2\leq{}& \frac{2c_r^2}{R}\|v\|_R^2\\
       &+c_r^2M_R^2R\|(D_t-N)v\|_R^2.
 \end{aligned}
 \tag{N8}
\]

There is no condition at $t=R$. The nilpotent evolution need not be unitary, and $N$ need not be normal or self-adjoint. Its polynomial growth is retained in $M_R$.

## 3. A small bounded perturbation and a real spectral shift

Let $E(t)$ be a strongly measurable family of bounded operators on $H$, with $\|E(t)\|\leq\delta$ almost everywhere. Strong measurability here means that $t\mapsto E(t)a$ is strongly measurable for each fixed $a\in H$. Then $E(t)v(t)$ is strongly measurable: approximate the continuous $v$ uniformly by finite step functions on the compact interval and use the uniform bound on $E$. Define

\[
 f=(D_t-N-E(t))v,
 \qquad K_R=c_r^2M_R^2R.
\]

Substitute $(D_t-N)v=f+Ev$ in (N8) and use the norm bound on $E$. This gives

\[
 \begin{aligned}
 \|v(0)\|^2\leq{}&
 \left(\frac{2c_r^2}{R}+2K_R\delta^2\right)\|v\|_R^2\\
       &+2K_R\|f\|_R^2.
 \end{aligned}
 \tag{N9}
\]

Given any $\varepsilon>0$, first choose $R\geq\max(1,4c_r^2/\varepsilon)$, and then choose $\delta>0$ so that $\delta^2\leq\varepsilon/(4K_R)$. For these choices,

\[
 \begin{gathered}
 \|v(0)\|^2\leq\varepsilon\|v\|_R^2
          +C_\varepsilon\|f\|_R^2,\\
 f=(D_t-N-E(t))v,\qquad C_\varepsilon=2K_R.
 \end{gathered}
 \tag{N10}
\]

The order of the choices matters: $M_R$ can grow with $R$, so the allowed perturbation may become much smaller as $\varepsilon$ decreases. No uniform estimate in unbounded nilpotent norms or unbounded block size is asserted.

For a real number $\eta$, replace the operator by $D_t-\eta I-N-E(t)$. Put $v(t)=e^{i\eta t}u(t)$. Direct differentiation gives

\[
 (D_t-\eta I-N-E(t))v
       =e^{i\eta t}(D_t-N-E(t))u.
 \tag{N11}
\]

All displayed norms and the initial value are unchanged, because $\eta$ is real. Thus (N8)–(N10) hold with this shift, with the same constants. A complex shift is not covered by this argument.

Here is the exact finite-matrix scope of the nilpotence hypothesis. If an $r\times r$ complex matrix $A$ has characteristic polynomial $(z-\eta)^r$, then $N=A-\eta I$ satisfies $N^r=0$. To prove the needed polynomial identity, use the cofactor formula
$(zI-A)\operatorname{adj}(zI-A)=\det(zI-A)I$.
The cofactor expansion proves this identity entry by entry. Compare coefficients, writing the adjugate as $\sum_{j=0}^{r-1}B_jz^j$. The top equation is $B_{r-1}=I$, and successive equations are $B_{j-1}-AB_j=p_jI$, where $p_j$ are the characteristic coefficients. These equations express every $B_j$ as a polynomial in $A$. The constant equation then telescopes to $p(A)=0$. With $p(z)=(z-\eta)^r$ this is the asserted nilpotence. Hence the estimate covers every finite normal block with one real characteristic root, including all Jordan multiplicities. No choice or regularity of Jordan bases is required.

## 4. Semiclassical scaling and an explicit residual

Let $h>0$ and let

\[
 P_h=hD_x-\eta I-N-E_h(x)
\]

act on $H$-valued functions on $0\leq x\leq hR$. Assume $\|E_h(x)\|\leq\delta$ with the choices in Section 3. For $V(t)=v(ht)$, direct differentiation gives $D_tV(t)=(hD_xv)(ht)$. Change variables in (N10), including both squared integrals, and multiply by $h$. The result is

\[
 h\|v(0)\|^2\leq\varepsilon\|v\|_{hR}^2
                    +C_\varepsilon\|P_hv\|_{hR}^2.
 \tag{N12}
\]

The constants are independent of $h$. A function on a larger half-interval can be restricted to this slab, and its larger nonnegative norms give the same bound. One first fixes $\varepsilon$, then $R,\delta$, and only then restricts $h$ so the slab lies inside the available normal neighborhood.

One frequently has a localized equation $P_hv=F+g$, where $g$ is an error already controlled in the same $L^2$ norm. The actual consequence is

\[
 h\|v(0)\|^2\leq\varepsilon\|v\|^2
                    +2C_\varepsilon\|F\|^2+2C_\varepsilon\|g\|^2.
 \tag{N13}
\]

All norms on the right may be taken on the slab or on the larger interval. In particular an $O(h^M)$ bound for $g$ contributes $O(h^{2M})$ here. It must not be discarded before it has been proved. Since $H$ may itself be a tangential $L^2$ space, the estimate applies to a bounded tangential operator family whenever the stated norm bound is established.

## 5. The double real root of the scalar wave operator

The algebra behind the glancing normal block is explicit. Freeze a tangential wave covector $(\tau,\xi')$ and write the scalar principal wave expression in normal coordinates as

\[
 Q_h=(hD_x)^2+a(x),
 \qquad a(x)=r(x,x',\xi')-\tau^2.
\]

For $w=(u,hD_xu)^T$ define

\[
 A(x)=\begin{pmatrix}0&1\\-a(x)&0\end{pmatrix}.
\]

Multiplication of this matrix, with no differentiation of $a$, gives

\[
 (hD_xI-A(x))w=\binom{0}{Q_hu}.
 \tag{N14}
\]

At a glancing root $a(0)=0$, the frozen matrix is

\[
 N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad N^2=0.
\]

Moreover $\|A(x)-N\|=|a(x)|$ in the Euclidean product norm. Thus, whenever $|a(x)|\leq\delta$ on the slab, (N12) proves

\[
 \begin{aligned}
 &h\bigl(|u(0)|^2+|hD_xu(0)|^2\bigr)\\
 &\qquad\leq\varepsilon\bigl(\|u\|^2+\|hD_xu\|^2\bigr)\\
 &\qquad\phantom{\leq{}}+C_\varepsilon\|Q_hu\|^2.
 \end{aligned}
 \tag{N15}
\]

For this formula $u$ and $hD_xu$ have the primitive regularity of Section 2 and $Q_hu\in L^2$. All norms on the right are on $0<x<hR$. A homogeneous Dirichlet condition makes $u(0)=0$, so (N15) controls the normal derivative trace as well. The estimate remains valid when the first-order system has an additional bounded matrix term whose norm is absorbed into the same $\delta$; such a term is not silently dropped.

Formula (N14) treats a frozen tangential covector. The remaining sections now supply the tangential operator and cutoff steps for the variable differential operator. The subsequent Dirichlet and glancing readings supply localized positive-commutator estimates, and [Existence and compactness of generalized reflected curves](generalized-reflected-curves.md#generalized-reflected-curves) supplies the geometric curve construction. The boundary lesson still requires the full analytic propagation argument.

<a id="tangential-normal-trace"></a>

## 6. Semiclassical tangential norms with the correct leading constant

Use $x\geq0$ for the normal variable and $y\in\mathbb R^d$ for all tangential variables, including time when treating the wave equation. For $0<h\leq1$ write

\[
 \operatorname{Op}_h(b)v(y)
  =(2\pi h)^{-d}\iint e^{i(y-z)\cdot\eta/h}
                          b(y,\eta)v(z)\,dz\,d\eta.
 \tag{N16}
\]

Suppose $b$ is a scalar symbol with bounded derivatives, uniformly in any auxiliary parameters, and $\sup|b|\leq M$. Substitute $\eta=h\xi$ in (N16). Its ordinary left symbol is $b(y,h\xi)$, whose frequency derivatives gain $h^{|\beta|}$. Theorem 4 of the preceding Gaussian-packet reading, with $R=h^{-1}$, therefore proves

\[
 \|\operatorname{Op}_h(b)\|\leq M+C_bh.
 \tag{N17}
\]

Only finitely many derivative bounds enter $C_b$. These bounds may depend on an already fixed cutoff; the cutoff is fixed before making $h$ small. The same substitution in bounded-amplitude Lemma 2 shows that an amplitude $c(y,z,\eta)$ with uniformly bounded derivatives gives a uniformly bounded operator. An amplitude whose derivative bounds are all $O(h)$ gives operator norm $O(h)$.

For an $s\times s$ matrix symbol apply these scalar estimates to its entries. If every entry operator has norm at most $K$, then
$\|(Tv)_j\|\leq K\sum_k\|v_k\|$ and Cauchy–Schwarz gives $\|Tv\|\leq sK\|v\|$. In particular,

\[
 \|\operatorname{Op}_h(b)\|
 \leq s\max_{j,k}\sup|b_{jk}|+C_bh.
 \tag{N18}
\]

The harmless factor $s$ is retained. It is not silently replaced by a sharp matrix norm. For a scalar cutoff $0\leq q\leq1$, acting on every component, (N17) gives $\|Q_h\|\leq2$ for all sufficiently small $h$, where $Q_h=\operatorname{Op}_h(q)I$.

## 7. Products with a compact phase cutoff

Let $q(y,\eta)$ be compactly supported and smooth. Let $b(x,y,\eta;h)$ have at most polynomial growth in $\eta$, together with every derivative, uniformly for $x$ in a fixed compact normal interval and $0<h\leq1$. The symbols below have precisely this property: a polynomial in $\eta$ with smooth bounded coefficients minus a compactly supported symbol.

The left symbol of $\operatorname{Op}_h(b)\operatorname{Op}_h(q)$ is

\[
 \begin{gathered}
 c(x,y,\eta;h)=(2\pi)^{-d}\int
       b(x,y,\eta+h\theta;h)\widehat q_y(\theta,\eta)\,d\theta,\\
 \widehat q_y(\theta,\eta)
       =\int e^{-iz\cdot\theta}q(y+z,\eta)\,dz.
 \end{gathered}
 \tag{N19}
\]

This is the exact product calculation of (FC7) in the finite scalar reading after the frequency substitution. It also follows directly by inserting the two kernels and integrating the compact intermediate variable first. The remaining integral is absolutely convergent: $\widehat q_y=e^{iy\theta}\widehat q(\theta,\eta)$ and the Fourier transform of the compact smooth $q$ decreases faster than every power of $\theta$, with every derivative and uniformly on its compact $\eta$ support. Each $y$ derivative of the displayed phase costs a fixed power of $\theta$, which that decrease absorbs. This also justifies the kernel identity by cutoff limits on Schwartz tests.

Taylor's formula with integral remainder in $h\theta$ gives, for every integer $J\geq1$,

\[
 c=\sum_{|\alpha|<J}\frac{(h/i)^{|\alpha|}}{\alpha!}
          (\partial_\eta^\alpha b)(\partial_y^\alpha q)
            +h^Jr_J.
 \tag{N20}
\]

Every normal, tangential and frequency derivative of $r_J$ is uniformly bounded; no derivative in $h$ is needed. It vanishes outside the fixed $\eta$ support of $q$. To verify the estimate rather than just formally expand, its terms are constant multiples of

\[
 \int_0^1(1-t)^{J-1}\int
       \theta^\alpha(\partial_\eta^\alpha b)
                  (x,y,\eta+th\theta;h)
                  \widehat q_y(\theta,\eta)\,d\theta\,dt,
 \quad |\alpha|=J.
\]

On that compact $\eta$ set, polynomial growth of $b$ bounds the first two factors and any fixed derivatives by a fixed power of $\langle\theta\rangle$, uniformly in $t,h$. Arbitrarily many integrations by parts in the compact variable of $q$ provide an integrable majorant. This proves the bound, including every needed normal derivative. Formula (N17), or the finite-derivative bound after $\eta=h\xi$, gives $\|\operatorname{Op}_h(r_J)\|\leq C_J$.

In particular, if $b$ vanishes on a neighborhood of $\operatorname{supp}q$, then all finite terms in (N20) vanish, and

\[
 \|\operatorname{Op}_h(b)Q_h\|\leq C_Jh^J
 \quad\hbox{for every fixed }J.
 \tag{N21}
\]

This includes the frequency tails. No unsupported replacement of a product by the product of its principal symbols has been made. Matrix symbols satisfy the same assertion entry by entry, with the product order retained.

## 8. The differential commutator and its extension to weak inputs

Let

\[
 A_h(x)=\sum_{|\alpha|\leq m}a_\alpha(x,y;h)(hD_y)^\alpha,
 \tag{N22}
\]

where the coefficients are $s\times s$ matrices with all derivatives bounded uniformly on the normal interval, in $y$, and for $0<h\leq1$. The scalar $Q_h$ from Section 7 satisfies

\[
 \begin{aligned}
 \|Q_hA_h\|+\|A_hQ_h\|&\leq C,\\
 \|[Q_h,A_h]\|&\leq Ch.
 \end{aligned}
 \tag{N23}
\]

Here these compositions, initially defined on Schwartz functions, have bounded $L^2$ extensions. We prove that fact directly, so no unbounded-operator domain is suppressed.

For the term $a_\alpha(hD_y)^\alpha$, differentiating the left kernel of $Q_h$ gives for $A_hQ_h$ the amplitude

\[
 \sum_{\beta\leq\alpha}\binom\alpha\beta
       a_\alpha(x,y;h)\eta^{\alpha-\beta}
                         (hD_y)^\beta q(y,\eta).
\]

For $Q_hA_h$, integration by parts in the input variable $z$ gives

\[
 \sum_{\beta\leq\alpha}\binom\alpha\beta
       q(y,\eta)\eta^{\alpha-\beta}
                         (-hD_z)^\beta a_\alpha(x,z;h).
\]

Both amplitudes have compact $\eta$ support and bounded derivatives, so Section 6 proves both norm bounds. The signs in the second formula use the bilinear transpose $D_z^t=-D_z$; acting on $e^{i(y-z)\eta/h}$, $-hD_z$ gives $+\eta$.

Every term with $|\beta|>0$ has an explicit factor $h$. Since $q$ is scalar, the remaining commutator amplitude is
$q(y,\eta)\eta^\alpha(a_\alpha(x,z;h)-a_\alpha(x,y;h))$.
Write the difference as

\[
 \sum_j(z_j-y_j)\int_0^1
      \partial_{y_j}a_\alpha(x,y+t(z-y);h)\,dt.
\]

Use $(z_j-y_j)e^{i(y-z)\eta/h}=ih\partial_{\eta_j}e^{i(y-z)\eta/h}$ and integrate by parts in $\eta_j$. The resulting amplitude has an explicit factor $h$, compact $\eta$ support and bounded derivatives in both positions. Lemma 2 therefore proves the commutator estimate. These identities first hold on Schwartz inputs, and the uniform bounded-amplitude estimates and Schwartz density give their stated extensions. They also identify the distributional compositions, by pairing with Schwartz tests. Parameter differentiation in $x$ gives the same boundedness statements because the coefficient bounds are uniform.

We will need a weak trace. Suppose $W,F\in L^2((0,L);H)$, $H=L^2(\mathbb R^d;\mathbb C^s)$, satisfy
$(hD_x-A_h(x))W=F$ as distributions. Then $V=Q_hW$ has distributional derivative

\[
 hD_xV=Q_hF+Q_hA_hW\in L^2((0,L);H).
 \tag{N24}
\]

It follows that $V$ has precisely the primitive representative required in Section 2, including a trace at zero. Here is the complete passage from the weak identity. Take the norm primitive $B(x)$ of its $L^2$ derivative, using the earlier vector integral theorem. The difference $V-B$ has zero distributional derivative. Fix a compactly supported smooth scalar $\rho$ of integral one. Every compactly supported smooth scalar $\phi$ with zero integral is the derivative of a compactly supported smooth function, so $\int(V-B)\phi=0$. Subtracting $\rho\int\phi$ in the general case shows that the distribution $V-B$ is the constant vector $\int(V-B)\rho$. This identifies it almost everywhere as that constant: convolution with scalar mollifiers gives the equality pointwise on smaller intervals, and the norm Lebesgue-point theorem in the vector integration reading recovers the original function almost everywhere. Its primitive therefore extends continuously to both endpoints. This argument uses no pre-existing trace of $W$.

## 9. The tangentially localized real-root trace theorem

Assume the matrix polynomial symbol of (N22) has the form
$A(x,y,\eta;h)=A_0(x,y,\eta)+hA_1(x,y,\eta;h)$,
with the uniform coefficient bounds of Section 8. Fix a boundary tangential covector $(y_0,\eta_0)$ such that

\[
 \begin{gathered}
 A_0(0,y_0,\eta_0)=\kappa I+N,\\
 \kappa\in\mathbb R,\qquad N^r=0.
 \end{gathered}
 \tag{N25}
\]

For every $\varepsilon>0$ there exist a real scalar $q\in C_c^\infty(T^*\mathbb R^d)$, $0\leq q\leq1$, equal to one on a neighborhood of $(y_0,\eta_0)$, and constants $h_0,C_\varepsilon>0$, such that every distributional solution as in Section 8 satisfies, for $0<h\leq h_0$,

\[
 \begin{aligned}
 &h\|(Q_hW)(0)\|_H^2\\
 &\quad\leq\varepsilon\|W\|_{L^2((0,L);H)}^2\\
 &\quad\phantom{\leq{}}+C_\varepsilon\|Q_hF\|_{L^2((0,L);H)}^2.
 \end{aligned}
 \tag{N26}
\]

The trace on the left is the proved trace of $Q_hW$, not an assumed $H$-valued trace of $W$. If $W$ already has a continuous trace, boundedness of $Q_h$ identifies the two meanings.

**Proof.** Choose the small coefficient $\varepsilon_0=\varepsilon/8$ in (N12), and let $R,\delta,C_0$ be its resulting constants for the fixed $N$. By continuity, choose a normal length $\ell>0$ and a compact phase neighborhood of $(y_0,\eta_0)$ on which every entry of $A_0-(\kappa I+N)$ has modulus at most $\delta/(2s)$, for $0\leq x\leq\ell$. Choose $q$ as above with support inside this neighborhood. Choose a scalar $\chi$, with $0\leq\chi\leq1$, supported in that neighborhood and equal to one on a neighborhood of $\operatorname{supp}q$. The previously proved smooth cutoff construction supplies both. Define

\[
 E_h(x)=\operatorname{Op}_h\!\left(
       \chi\,[A_0-\kappa I-N+hA_1]\right).
 \tag{N27}
\]

Equations (N17)–(N18) give $\|E_h(x)\|\leq\delta/2+Ch\leq\delta$ on $[0,\ell]$ after making $h$ small. Normal derivatives and the finite operator bounds also show norm continuity of $E_h(x)$, so it satisfies the measurability hypothesis of Section 3. At the same time $\|Q_h\|\leq2$ for small $h$.

The symbol of $A_h-\kappa I-N-E_h$ is $(1-\chi)(A_0-\kappa I-N+hA_1)$. It vanishes near $\operatorname{supp}q$. Thus (N21) gives
$D_h=(A_h-\kappa I-N-E_h)Q_h=O(h^J)$ on $H$ for every fixed $J$, uniformly in $0\leq x\leq\ell$.
The exact localized equation is

\[
 \begin{aligned}
 &(hD_x-\kappa I-N-E_h)V\\
 &\quad=Q_hF+[Q_h,A_h]W+D_hW,\\
 &V=Q_hW.
 \end{aligned}
 \tag{N28}
\]

The commutator sign follows by expanding both sides; $Q_h$ is independent of $x$. By (N23) and (N21), the last two terms have $L^2$ norm at most $C_1h\|W\|$ on the slab $0<x<hR$, provided $hR\leq\min(\ell,L)$. Section 8 proves the needed primitive regularity for $V$ even on weak inputs. Apply (N12) to (N28) and use $\|V\|\leq2\|W\|$ and the squared triangle inequality. On this slab the result is

\[
 \begin{aligned}
 &h\|V(0)\|^2\\
 &\quad\leq(4\varepsilon_0+2C_0C_1^2h^2)\|W\|^2\\
 &\quad\phantom{\leq{}}+2C_0\|Q_hF\|^2.
 \end{aligned}
 \tag{N29}
\]

Choose $h_0$ still smaller so $2C_0C_1^2h_0^2\leq\varepsilon/2$. Now $4\varepsilon_0=\varepsilon/2$, and enlarging the nonnegative integrals from the slab to $(0,L)$ proves (N26), with $C_\varepsilon=2C_0$. All choices occur in the required order: $\varepsilon_0$, then $R,\delta$, then the fixed neighborhoods and cutoffs, then $h_0$. Derivatives of a shrinking cutoff need not be uniformly small. Their finite constants are accounted for when choosing $h_0$. This completes the proof.

The result covers any finite matrix size and nilpotent index satisfying (N25), with every lower-order differential term retained. It does not assert the same real-root reduction for a matrix with several distinct normal roots; that requires separating those blocks.

## 10. Application to the actual variable tangential wave operator

In a boundary normal coordinate patch for the scalar wave operator, let $y=(t,y')$ and let $\eta=(\tau,\xi')$. After multiplying by the fixed sign that makes the normal second-order coefficient one, its semiclassical form on coordinate half-density coefficients is

\[
 \begin{aligned}
 \mathcal Q_h={}&(hD_x)^2+
     \operatorname{Op}_h(a_0(x,y,\eta))\\
   &+h\operatorname{Op}_h(a_1(x,y,\eta;h))
                         +h b(x,y;h)hD_x,\\
 a_0={}&r(x,y',\xi')-\tau^2.
 \end{aligned}
 \tag{N30}
\]

Here $a_1$ is a tangential polynomial of degree at most one, with its degree-zero coefficients permitted to depend uniformly on $h$, and $b$ is smooth. This includes all first-order and zero-order terms. Indeed multiplying an ordinary differential operator of order two by $h^2$ turns a first-order term into $h$ times a first-order semiclassical derivative and a zero-order term into $h^2$ times multiplication; put the latter in the $h$-dependent degree-zero coefficient of $a_1$. Boundary normal coordinates remove mixed principal normal/tangential terms. Writing the remaining differential terms with coefficients on the left includes derivatives of coefficients in these same lower-order terms. No self-adjoint simplification is needed for the following trace estimate.

For $W=(u,hD_xu)^T$ set

\[
 A_h=
 \begin{pmatrix}
  0&I\\
  -\operatorname{Op}_h(a_0+ha_1)&-hb
 \end{pmatrix}.
\]

The exact distributional identity is

\[
 (hD_xI-A_h)W=\binom{0}{\mathcal Q_hu}.
 \tag{N31}
\]

At every glancing boundary tangential covector, $a_0(0,y_0,\eta_0)=0$, so its principal normal matrix is the nilpotent double-root matrix of Section 5. Thus (N26), with $s=r=2$ and $\kappa=0$, proves

\[
 \begin{aligned}
 &h\|\bigl(Q_hu,Q_hhD_xu\bigr)(0)\|^2\\
 &\qquad\leq\varepsilon\bigl(\|u\|^2+\|hD_xu\|^2\bigr)\\
 &\qquad\phantom{\leq{}}+C_\varepsilon\|Q_h\mathcal Q_hu\|^2.
 \end{aligned}
 \tag{N32}
\]

The norms on the right are over $(0,L)\times\mathbb R^d$. It suffices that $u,hD_xu,\mathcal Q_hu$ belong to $L^2$ distributionally; the localized pair on the left has its continuous trace by Section 8. For a function with the homogeneous Dirichlet trace, its localized first component is zero; its localized normal derivative remains controlled. For general weak functions this statement uses precisely the localized trace just constructed.

For a coordinate-local use, extend the smooth coefficients with bounded derivatives outside a smaller chart and apply the theorem to the actual localized equation there. Multiplying the original wave by a position cutoff adds its explicit commutator to the forcing; that forcing is retained in $F$ or $\mathcal Q_hu$, rather than assumed zero. The estimates above apply to every such fixed extension and cutoff and are independent of $h$. They impose no condition on the order of tangency of a glancing characteristic. Subsequent readings now prove the [Dirichlet commutator and strict-diffraction estimate](dirichlet-commutator-and-diffraction.md#dirichlet-commutator), [negative-order spectral regularization](dirichlet-wave-regularization.md#dirichlet-wave-regularization), and [quadratic normal cutoff construction](quadratic-normal-cutoffs.md#quadratic-normal-cutoffs). These are specific inputs. [Existence and compactness of generalized reflected curves](generalized-reflected-curves.md#generalized-reflected-curves) now supplies the geometric curve construction at full contact scope. Full wavefront propagation along that precise relation, its incoming cutoff estimates and its complete regularity iteration remain to be proved.
