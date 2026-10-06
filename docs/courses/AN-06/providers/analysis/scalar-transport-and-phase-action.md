# Scalar transport and finite action on a phase

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="scalar-transport"></a>

This reading proves the classical scalar transport formula, including the half-density divergence and every finite remainder needed by the local wave construction. For comparison, see [Duistermaat and Hörmander, *Fourier integral operators II*, Sections 5.2–5.3](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392165), and [Hörmander, *The spectral function of an elliptic operator*, Theorem 2.12, Corollary 2.13 and Section 3](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02391913). The proofs below use the already proved programme calculus and supply the needed arguments directly.

Prerequisites are the [finite scalar calculus and invariant subprincipal symbol](classical-scalar-calculus.md#finite-scalar-calculus), its parameter cutoff summation, and the [phase, stationary-phase and principal-symbol proofs](phase-geometry-and-stationary-phase.md#phase-foundations). We use $D=-i\partial$, left quantization with inverse Fourier factor $(2\pi)^{-d}$, and the unshifted phase normalization and Maslov section of (P11), (P25). All symbols are classical $S_{1,0}$ of real order. Parameter bounds are local on compact parameter sets; amplitudes have compact localized base support. The [joint-parameter normalization (G18)](transverse-composition-and-graph-operators.md#joint-parameters) is used when passing from a family of wave kernels to a half-density kernel on the joint time/base manifold. The initial value in Section 6 uses [Wavefront-qualified pullback and restriction of phases, Sections 6–7](wavefront-qualified-pullback.md#phase-restriction), including the normal half-density frame and the exact quarter-order shift.

<a id="finite-phase-action"></a>

## 1. Finite action with a nonlinear phase

Let $P$ have full left symbol $p(x,\zeta)\in S^r_{1,0}$ in dimension $d$. Let $a(x,\theta)\in S^q_{1,0}$ and let $\phi(x,\theta)$ be real, smooth and homogeneous of degree one in the parameter frequency $\theta$. Suppose $|\phi_x|\ge c|\theta|$ on the localized support, with all normalized derivatives bounded. We prove that
$c(x,\theta)=e^{-i\phi(x,\theta)}P(e^{i\phi(\cdot,\theta)}a(\cdot,\theta))(x)$
is a symbol of order $r+q$ and give its complete finite expansion. Proper cutoffs and compact localization are understood in this actual operator expression.

Put $w=z-x$ and
$F(x,w,\theta)=\int_0^1\phi_x(x+tw,\theta)\,dt$.
The fundamental theorem gives $\phi(x+w,\theta)-\phi(x,\theta)=w\cdot F(x,w,\theta)$. The change $\zeta=\rho+F(x,w,\theta)$ has Jacobian one and turns the exact left-kernel phase into $-w\cdot\rho$. Consequently, for every positive integer $L$,
\[
 \begin{split}
 c(x,\theta)&=\sum_{|\alpha|<L}\frac{1}{i^{|\alpha|}\alpha!}
  \left.\partial_w^\alpha\partial_\rho^\alpha
   \{p(x,\rho+F(x,w,\theta))a(x+w,\theta)\}\right|_{w=\rho=0}
       +R_L(x,\theta),\\
 R_L&\in S^{r+q-L}_{1,0}.
 \end{split}
 \tag{T1}
\]
Here the $\alpha$th term has order $r+q-|\alpha|$. A $\rho$ derivative lowers the order of $p$; if a $w$ derivative falls on $F$, its order-one factor accompanies one further frequency derivative of $p$. All remaining $w$ derivatives preserve order. This proves the stated degree for each coefficient, including its classical homogeneous expansion.

Here are the convergence and remainder details. Set $R=|\theta|$ and $\theta=R\omega$ on a compact angular patch. In the original integral split the $\zeta$ variable into small, comparable and large multiples of $R$. On the two noncomparable parts, $|\phi_z-\zeta|\ge c'(R+|\zeta|)$ after making the base patch small. Transferring the corresponding $z$ gradient gives arbitrarily high inverse powers of $R+|\zeta|$. Fixed derivatives in the other variables cost only fixed powers. The amplitude grows at most as $R^q\langle\zeta\rangle^r$, with analogous polynomial bounds after derivatives. Splitting the radial integral at $|\zeta|=R$ and choosing more transfers makes the resulting remainder $O(R^{-M})$ for every prescribed $M$, also after those derivatives. Properly localized off-diagonal smooth kernels have the same estimate by integration in $z$, using the nonzero $\phi_z$; this accounts for the smooth tails of the pseudodifferential kernel.

On the comparable part set $\rho=R\nu$. Away from $(w,\nu)=(0,0)$ the phase $-w\cdot\nu$ is nonstationary, so the same compact normalized integration-by-parts argument gives every inverse power. Near zero the transformed amplitude is a compactly supported symbol family of order $r+q$ in $R$. The quadratic stationary-phase proof (P4)–(P8), with Hessian
$\left(\begin{smallmatrix}0&-I\\-I&0\end{smallmatrix}\right)$,
applies. Its determinant has absolute value one and its signature is zero. Its Gaussian factor $(2\pi/R)^d$ cancels the integral prefactor $(2\pi)^{-d}R^d$. Its differential operator is $-2\partial_w\cdot\partial_\nu$, producing exactly (T1) after $\partial_\nu=R\partial_\rho$. The error after $L$ terms is $S^{r+q-L}$ by (P8). Cutoffs are one near the critical point, so their derivatives do not alter these coefficients. Every external parameter derivative is included in that estimate. A $\theta$ derivative is a combination of a radial derivative and $R^{-1}$ angular derivatives; hence the estimates are full $S_{1,0}$ bounds, not just bounds along one ray. This also proves equality of the cutoff integral with the actual operator expression by the distributional continuity of the scalar calculus. The finite constants depend on finitely many symbol and normalized phase seminorms and the displayed positive gradient bound.

Since $F(x,0,\theta)=\phi_x$ and $\partial_{w_j}F_k(x,0,\theta)=\phi_{x_jx_k}/2$, the first two orders are
\[
 c=p(x,\phi_x)a
    +\frac1i\sum_j p_{\zeta_j}(x,\phi_x)\partial_{x_j}a
    +\frac1{2i}\sum_{j,k}p_{\zeta_j\zeta_k}(x,\phi_x)
                               \phi_{x_jx_k}a
       \pmod{S^{r+q-2}}.
 \tag{T2}
\]
This formula uses the full symbol $p$. In its last two terms one may replace $p$ by its leading homogeneous term when computing only degree $r+q-1$.

<a id="frequency-coordinate-phase"></a>

## 2. Frequency coordinates at every Lagrangian point

We need a normal phase that also works at a base caustic. Let $\Lambda\subset T^*M\setminus0$ be conic Lagrangian, with $\dim M=d$, and fix $(x_0,\xi_0)\in\Lambda$. After a smooth change of base coordinates, the map from $\Lambda$ to its frequency coordinates is locally invertible. The following linear and coordinate argument proves this assertion.

Let $W$ be the base projection of its tangent space. Isotropy shows that the purely vertical tangent vectors are exactly $\{0\}\times W^\perp$: they annihilate $W$, and both spaces have dimension $d-\dim W$. For a tangent vector with base component $u\in W$, the $W$ component of its frequency component is therefore a well-defined linear map $Au$. Isotropy says that $A:W\to W$ is symmetric. Choose a real $\lambda>\|A\|$. Adding $\lambda u$ to the frequency component makes the projection onto frequency injective, since $A+\lambda I$ is invertible on $W$ and the unrestricted $W^\perp$ component accounts for the vertical directions. Equal dimensions then make it an isomorphism.

This addition is achieved by an actual base-coordinate change. Choose a vector $v$ with $\xi_0\cdot v=1$ and, in centered coordinates, set
$x=\kappa(X)=x_0+X+\frac{\lambda}{2}|X|^2v$.
Its derivative at zero is the identity, so the inverse theorem gives a coordinate map. The transformed covector is $\Xi=D\kappa(X)^T\xi$; at the chosen point its variation is $\delta\Xi=\delta\xi+\lambda\delta X$. Thus the preceding isomorphism is precisely the differential of the frequency projection in these coordinates. The inverse theorem proves the local claim. The symmetric-map assertion and the bound for $A+\lambda I$ follow from the elementary symmetric eigenbasis proof in the phase reading, so no canonical transformation theorem is being assumed.

Write the resulting Lagrangian as $x=X(\xi)$. Homogeneity makes $X$ degree zero. The tautological form $\xi\cdot dx$ vanishes on a conic Lagrangian: its value on a tangent vector is the symplectic pairing of that vector with the radial tangent vector, and both are tangent to $\Lambda$. Therefore $H(\xi)=\xi\cdot X(\xi)$ satisfies $dH=X\cdot d\xi$ and is homogeneous of degree one. We have the phase
\[
 \phi(x,\xi)=x\cdot\xi-H(\xi),\qquad
 C_\phi=\{x=H_\xi\},\qquad d_\phi=|d\xi|.
 \tag{T3}
\]
Its critical equations have identity derivative in $x$, so it is nondegenerate. The critical density follows directly by their Jacobian, as in (P22). The earlier phase-equivalence theorem permits this representation of every localized $I^m(\Lambda)$ distribution. The construction varies smoothly with additional parameters near the chosen point: choose $\lambda$ large enough on a compact parameter neighborhood and make the same inverse constructions there. It does not assume constant base-projection rank nearby.

## 3. Removing base dependence from the amplitude

For (T3), Taylor's formula around $x=H_\xi$ writes any amplitude $a(x,\xi)$ of order $q$ as $a(H_\xi,\xi)+\sum_j(x_j-H_{\xi_j})a_j(x,\xi)$, with $a_j$ of the same order. The derivatives of $H_\xi$ have the required decreasing homogeneous orders, so restriction to that graph preserves the symbol estimates. Since $\phi_{\xi_j}=x_j-H_{\xi_j}$, integration by parts gives
\[
 \int e^{i\phi}\sum_j(x_j-H_{\xi_j})a_j\,d\xi
       =-\frac1i\int e^{i\phi}\sum_j\partial_{\xi_j}a_j\,d\xi.
 \tag{T4}
\]
The derivatives on the right are at fixed $x$ and lower the order by one. The distributional cutoff proof from the phase reading justifies this identity and the vanishing of its cutoff-boundary errors.

Repeat Taylor restriction on the right. After any finite number of steps the amplitude is a finite sum of terms depending only on $\xi$, with a remainder of correspondingly lower order. Parameter cutoff summation gives a classical $a_0(\xi)$ with all those terms; the difference of the original kernel and this representation is smooth. Base cutoffs are chosen equal to one near the critical image of the smaller angular support. Their differentiated parts have no critical point in the local region and give smooth kernels by (P12). Thus the amplitude is independent of $x$ near the critical set where the computation is used, while proper localization is retained. Its leading term is the original critical restriction. This proves the asserted reduction to all orders, rather than just at principal order.

<a id="invariant-transport-formula"></a>

## 4. The vanishing-symbol calculation

Let $P\in\Psi^r_{\rm cl}(M;\Omega^{1/2})$ have homogeneous principal symbol $h$, with $h|_\Lambda=0$, and let $u\in I^m_{\rm cl}(M,\Lambda)$. The symbol may be complex; then the vector field below is interpreted in the complexified tangent space. For the real wave problem it is a real vector field. Use (T3) and the amplitude $a_0(\xi)$ just constructed, of order $q=m-d/4$. The principal section of $u$ is represented by $e^{i\pi d/4}a_{0,q}\sqrt{|d\xi|}$ in this frame.

Acting on $e^{i(x\cdot\xi-H(\xi))}a_0(\xi)$ gives full amplitude $p(x,\xi)a_0(\xi)$, up to the localized rapid remainder: (T1) has no positive-order coefficient because the phase is linear in $x$ and $a_0$ is independent of it. Equivalently this is the exact left-symbol action on a plane wave. Near the critical graph Taylor's formula gives
\[
 h(x,\xi)=\sum_j(x_j-H_{\xi_j})h_j(x,\xi),\qquad
 h_j(x,\xi)=\int_0^1 h_{x_j}(H_\xi+t(x-H_\xi),\xi)\,dt.
 \tag{T5}
\]
Each $h_j$ is homogeneous of degree $r$. Apply (T4) to this leading product. The resulting amplitude has order $q+r-1$, and its leading critical restriction is
\[
 b=p_{r-1}a-\frac1i\sum_j
           \left(h_j\partial_{\xi_j}a+
                        (\partial_{\xi_j}h_j)_{x\ \mathrm{fixed}}a\right)
                \quad\hbox{at }x=H_\xi,
 \qquad a=a_{0,q}.
 \tag{T6}
\]
Every discarded term has order at most $q+r-2$: it comes from a lower amplitude term, a symbol term below $p_{r-1}$, or one further Taylor/integration-by-parts step. The same argument applied to an order-lower $u$ proves the corresponding extra drop, so (T6) depends only on its principal section.

In frequency coordinates the restricted Hamilton field is
$V=-\sum_jh_j(H_\xi,\xi)\partial_{\xi_j}$.
Indeed (T5) gives $h_{x_j}=h_j$ on the graph, and differentiating $h(H_\xi,\xi)=0$ gives $h_\xi=-H_{\xi\xi}h_x$. These are exactly the base and fiber components $(h_\xi,-h_x)$ of the tangent vector represented by $V$. Its divergence is
\[
 \operatorname{div}V=-\sum_j\left[
    (\partial_{\xi_j}h_j)_{x\ \mathrm{fixed}}
       +\sum_k(\partial_{x_k}h_j)H_{\xi_k\xi_j}\right]_{x=H_\xi}.
 \tag{T7}
\]
The derivative in this formula is the total derivative along the critical graph, and is different from the fixed-$x$ derivative in (T6).

Differentiating (T5) first in $x_j$, then in $\xi_j$ at fixed $x$, and restricting to the graph gives
\[
 \sum_j h_{x_j\xi_j}
   =\sum_j(\partial_{\xi_j}h_j)_{x\ \mathrm{fixed}}
       -\sum_{j,k}(\partial_{x_k}h_j)H_{\xi_k\xi_j}.
 \tag{T8}
\]
The equality of the two forms of the double sum uses the symmetry of the Hessian of $H$. Substituting (T7)–(T8) into (T6) yields the invariant statement
\[
 \begin{gathered}
 Pu\in I^{m+r-1}_{\rm cl}(M,\Lambda),\\
 \sigma(Pu)=\frac1i\mathcal L_{H_h}\sigma(u)
                           +p_{\rm sub}\sigma(u),\\
 p_{\rm sub}=p_{r-1}-\frac1{2i}\sum_jh_{x_j\xi_j}.
 \end{gathered}
 \tag{T9}
\]
The constant phase $e^{i\pi d/4}$ occurs in both principal sections and cancels from the calculation. Thus (T9) uses exactly the earlier unshifted convention.

## 5. Why the density and coordinate statements are intrinsic

For a vector field $V=\sum_jV_j\partial_{z_j}$ and a half density $a|dz|^{1/2}$,
\[
 \mathcal L_V(a|dz|^{1/2})
       =\left(Va+\tfrac12\sum_j\partial_{z_j}V_j\,a\right)|dz|^{1/2}.
 \tag{T10}
\]
To prove the formula and its coordinate invariance, use the local maps $z\mapsto z+tV(z)$ for small real $t$. They are diffeomorphisms on a smaller neighborhood by the inverse theorem, and their determinant is $1+t\operatorname{tr}DV+O(t^2)$ by the determinant expansion. Differentiating the half-density pullback gives (T10). Under another chart the same maps have first variation equal to the transformed vector field; terms of order $t^2$ do not affect the derivative. The ordinary change-of-variables identity for half densities therefore proves the coordinate rule. Complex vector fields are handled by complex linearity. On the Maslov line all transition factors are locally constant, so this derivative commutes with them and defines the asserted derivative of a Maslov half density.

The Hamilton field is tangent to $\Lambda$ because $dh$ vanishes on its tangent space and the symplectic orthogonal of a Lagrangian tangent space is itself. The latter follows from isotropy and equal half dimension, using the nondegeneracy of the symplectic pairing. Finally $p_{\rm sub}$ is invariant for scalar half densities by (FC9)–(FC15), whose complete base-coordinate calculation precedes this reading. Both sides of (T9) are therefore independent of the convenient coordinates in (T3). This proves the formula at every point, including a caustic. Finite partitions and the preceding remainder estimates give its proper local and global versions. The same arguments and stationary bounds apply after every smooth parameter derivative.

<a id="wave-transport-recursion"></a>

## 6. The wave equation and every lower-order correction

In a small-time wave phase write $\phi=\psi(t,x,\eta)-y\cdot\eta$, where $\psi_t+h(x,\psi_x)=0$ and $h$ is real homogeneous of degree one. Use the fixed-time normalization $(2\pi)^{-n}\int e^{i\phi}a\,d\eta$. The joint normalized amplitude has the additional factor $(2\pi)^{1/4}$ by (G18). Formula (T2), together with $D_t=-i\partial_t$, gives the degree-zero transport operator on the leading amplitude:
\[
 \mathcal T a=-i\left(\partial_t+
                 \sum_jh_{\xi_j}(x,\psi_x)\partial_{x_j}\right)a
     +\left[p_0(x,\psi_x)+\frac1{2i}
          \sum_{j,k}h_{\xi_j\xi_k}(x,\psi_x)\psi_{x_jx_k}\right]a.
 \tag{T11}
\]
The degree-one term vanishes by the eikonal equation. Formula (T1) proves to every finite order that all remaining terms have successively lower integer degrees, with differentiated symbol remainders. Thus (T11) is the actual first step of a classical expansion, not just a formal transport expression.

The invariant version (T9) on the wave relation uses $H_{\tau+h}=\partial_t$ in its flow coordinates $(t,z)$. In the preserved half-density frame it is $(-i\partial_t+c)a=b$, where $c$ is the subprincipal coefficient restricted to the flow. Its full inhomogeneous solution is
\[
 a(t,z)=e^{-iC(t,z)}
    \left[a(0,z)+i\int_0^t e^{iC(s,z)}b(s,z)\,ds\right],
 \qquad C(t,z)=\int_0^t c(s,z)\,ds.
 \tag{T12}
\]
Differentiate this formula to verify both the equation and the initial value, with the oriented integral also covering negative $t$. The Maslov frame is transported by the flat-line construction already proved. On compact time intervals, differentiation under these finite integrals and the product rule bound every derivative. For $c$ homogeneous of degree zero and $a(0),b$ of a given homogeneous degree, the formula retains that degree; frequency derivatives lower it in the usual way. The exponential has symbol order zero, since every derivative of its exponent has the corresponding degree and the time interval is compact. If $c$ is real, that factor has absolute value one and a nonzero homogeneous initial value stays nonzero when $b=0$.

At each lower order, take the actual leading residual supplied by (T1) or (T9), set $b$ to its negative, and choose the initial value to cancel the actual initial-symbol error. Formula (T12) supplies the correction with all parameter estimates. Realize its principal section by (P27). The error is one order lower by (T9) and the vanishing-principal-symbol proof; iterate. Parameter cutoff summation then realizes all corrections with their prescribed finite tails. Applying $P$ to an omitted tail of order $m-L$ has ordinary order at most $m-L+r$, and, on this characteristic Lagrangian, (T9) improves that to $m-L+r-1$. Since $L$ is arbitrary, the final residual is smoothing. Fixed-time initial errors use [the restriction formula (R11)–(R13)](wavefront-qualified-pullback.md#wave-restrictions), with the same constant $(2\pi)^{-1/4}$ at every order. These steps give every correction on the stated flow-coordinate region, with its qualified time restrictions and chosen normal half-density frame.
