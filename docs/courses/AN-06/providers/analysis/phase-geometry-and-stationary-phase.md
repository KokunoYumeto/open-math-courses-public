# Phase geometry, stationary phase and the Maslov symbol

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="phase-foundations"></a>

This reading supplies programme proofs of local phase construction, homogeneous phase changes, stationary phase, the Maslov principal symbol and its wavefront implication. These topics are treated in [Lars Hörmander, *Fourier integral operators I*, Sections 3.1–3.2](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392052). The arguments below give the required classical scalar case directly, including the constants and parameter remainders. After this reading, [Transverse composition and graph operators](transverse-composition-and-graph-operators.md#transverse-composition) proves the composition and adjoint rules. Scalar transport and general wavefront-qualified pullback remain further programme obligations.

The integration and Fourier inputs are the proved [Euclidean product theorem](finite-derivative-l2.md#euclidean-products) and [Fourier inversion and Gaussian formula](finite-derivative-l2.md#fourier-normalization). Coordinate inverses, finite smooth partitions and change of variables are proved in [Coordinate inverses and integration](coordinate-inverses-and-integration.md#coordinate-integration). The implicit-function assertion used here follows from that inverse theorem by applying it to $(t,y)\mapsto(t,F(t,y))$ when $D_yF$ is invertible. The [scalar calculus](classical-scalar-calculus.md#classical-summation) supplies cutoff summation, also after every parameter derivative. Distributional pairings are bilinear; complex conjugation is inserted only for Hilbert adjoints. We use $D=-i\partial$ and $\widehat f(\zeta)=\int e^{-iv\zeta}f(v)\,dv$.

All parameter estimates are local on compact parameter sets. An amplitude of order $q$ means a smooth $S^q_{1,0}$ symbol: a frequency derivative lowers its bound by one, and a base or parameter derivative preserves the order. A classical amplitude has a step-one homogeneous expansion. We cut off bounded frequencies; those changes give smooth kernels. Conic supports are closed inside the phase patch and compact after restricting the base to a compact set and the frequency to its unit sphere.

<a id="parameter-morse"></a>
## 1. Quadratic reduction with parameters

Suppose $f(t,y)$ is real and smooth, $f_y(t_0,y_0)=0$, and $f_{yy}(t_0,y_0)$ is invertible, with $y\in\mathbb R^k$. The implicit theorem gives a smooth critical point $y_c(t)$. There are smooth coordinates $v$ centered there, and fixed signs $\varepsilon_j\in\{1,-1\}$, such that
\[
 f(t,y)=f(t,y_c(t))+\frac12\sum_{j=1}^k\varepsilon_jv_j^2.
 \tag{P1}
\]
Here is a constructive proof, including the parameter dependence.

A real symmetric invertible matrix has an orthonormal eigenbasis. Indeed its quadratic form reaches a maximum on the unit sphere; differentiation along tangent directions makes a maximizing vector an eigenvector. The orthogonal complement is invariant by symmetry, so induction proves the assertion. At the single initial parameter apply such a fixed orthogonal change to the Hessian and rescale its nonzero eigenvalues to $\pm1$. After replacing $y$ by $y-y_c(t)$, Taylor's formula gives
\[
 f(t,y)-f(t,0)=\tfrac12y^TB(t,y)y,
 \qquad B(t,y)=2\int_0^1(1-s)f_{yy}(t,sy)\,ds.
 \tag{P2}
\]
Near $(t_0,0)$ this symmetric matrix has a smooth elimination without pivot changes. Explicitly its first pivot is $b_{11}$, its remaining block is replaced by
$b_{ij}-b_{i1}b_{1j}/b_{11}$, and the procedure is repeated. At the initial diagonal matrix every pivot is $\pm1$, so all pivots remain nonzero nearby, with their signs fixed. These finite algebraic operations give
$B=L\operatorname{diag}(d_1,\ldots,d_k)L^T$, with $L$ lower triangular with diagonal one. All entries are smooth. Set
$v=\operatorname{diag}(|d_j|^{1/2})L^Ty$.
Its derivative in $y$ at the critical point is invertible; the parameter inverse theorem makes it a coordinate change. This proves (P1). At the critical point its inverse Jacobian satisfies
\[
 \left|\det\frac{\partial y}{\partial v}(t,0)\right|
       =|\det f_{yy}(t,y_c(t))|^{-1/2}.
 \tag{P3}
\]
This follows by taking determinants in the quadratic Hessian transformation. The signs sum to the signature of that Hessian and cannot change in this neighborhood. Compact parameter sets on which the critical point stays nondegenerate are covered by finitely many such constructions; their derivatives and inverse Jacobians have the required uniform bounds.

<a id="quadratic-stationary-phase"></a>
## 2. The Gaussian constant and every finite error

Let $H$ be a real symmetric invertible $k\times k$ matrix, $R\ge1$, and $b\in C_c^\infty(\mathbb R^k)$. Put
$Q_H=\sum_{j,l}(H^{-1})_{jl}\partial_{v_j}\partial_{v_l}$.
For every positive integer $L$,
\[
 \begin{split}
 \int e^{iRv^THv/2}b(v)\,dv
  ={}&(2\pi/R)^{k/2}|\det H|^{-1/2}
       e^{i\pi\operatorname{sgn}H/4}\left[
        \sum_{j<L}\frac{(i/2R)^j}{j!}(Q_H^jb)(0)
                      +\mathcal R_L(R)\right],\\
 &|\mathcal R_L(R)|\le C_LR^{-L}
                      \int\langle\zeta\rangle^{2L}|\widehat b(\zeta)|\,d\zeta.
 \end{split}
 \tag{P4}
\]
We prove the oscillatory constant, not just its absolute value.

In one dimension first regularize by $e^{-\epsilon v^2/2}$, $\epsilon>0$. For $A=\epsilon-iRh$ integration by parts gives
\[
 G_A(\zeta)=\int e^{-Av^2/2+i\zeta v}\,dv
    =(2\pi)^{1/2}A^{-1/2}e^{-\zeta^2/(2A)}.
 \tag{P5}
\]
For completeness, differentiation in $\zeta$ and integration by parts give
$G_A'=-\zeta G_A/A$. Its constant at zero is obtained by varying
$A(s)=\epsilon-isRh$, $0\le s\le1$. The absolutely convergent differentiated integral obeys
$\frac{d}{ds}G_{A(s)}(0)=-A'(s)G_{A(s)}(0)/(2A(s))$,
because integration by parts gives $\int v^2e^{-Av^2/2}\,dv=G_A(0)/A$.
At $s=0$ the real Gaussian formula gives $(2\pi/\epsilon)^{1/2}$. Multiplication by the continuous square root of $A(s)$ shows that the solution is $(2\pi)^{1/2}A(s)^{-1/2}$, with the branch whose argument lies between $-\pi/4$ and $\pi/4$. This proves (P5) without an analytic-continuation assumption.

Diagonalize $H$ by the finite-dimensional argument above and multiply (P5). As $\epsilon\downarrow0$ the Fourier Gaussian becomes
\[
 (2\pi/R)^{k/2}|\det H|^{-1/2}
 e^{i\pi\operatorname{sgn}H/4}
       e^{-i\zeta^TH^{-1}\zeta/(2R)}.
 \tag{P6}
\]
To justify its use, insert Fourier inversion for $b$ before taking the limit. For $\epsilon>0$ the interchange is absolute. The modulus of each regularized determinant factor is bounded by its limiting absolute factor, and the real part of $1/(\epsilon-iRh)$ is positive, so the remaining exponential has modulus at most one. Thus $C|\widehat b(\zeta)|$ is an integrable majorant, uniform as $\epsilon\downarrow0$. Dominated convergence in both the original compact $v$ integral and its Fourier expression proves the exact identity obtained by integrating (P6) against $(2\pi)^{-k}\widehat b(\zeta)$.

Expand the last exponential through degree $L-1$ in $R^{-1}$. Its remainder has modulus at most $C_LR^{-L}|\zeta|^{2L}$, since its exponent is purely imaginary. Fourier inversion changes each quadratic polynomial in $\zeta$ into $-Q_H$, which gives the factor $(i/2R)^j$ in (P4). Every weighted Fourier integral there is bounded by finitely many derivatives of $b$ on its fixed compact support: apply $(1-\Delta_v)^M$ before Fourier transformation and choose $2M>k+2L$.

The proof also gives symbol remainders. Suppose $b=b(t,v,R)$ has fixed compact $v$ support and
\[
 |\partial_t^\alpha\partial_v^\beta\partial_R^a b(t,v,R)|
             \le C_{\alpha\beta a}R^{q-a}.
 \tag{P7}
\]
After taking $a$ derivatives in $R$, the exponential Taylor error is bounded by
$C_{La}R^{-L-a}\langle\zeta\rangle^{2\max(L,a)}$.
To check this, put $r=R^{-1}$ and use
$\partial_R^a=\sum_{j\le a}c_{aj}r^{a+j}\partial_r^j$ for $a>0$.
For $j\le L$, the $j$th derivative of the Taylor error is bounded by
$C r^{L-j}|\zeta|^{2L}$; for $j>L$ it is bounded by $C|\zeta|^{2j}$ and $r^{a+j}\le r^{a+L}$.
The case $a=0$ is the earlier estimate. Apply the product rule and the weighted Fourier estimates to obtain
\[
 |\partial_t^\alpha\partial_R^a\mathcal R_L(t,R)|
                         \le C_{L\alpha a}R^{q-L-a}.
 \tag{P8}
\]
Each constant uses finitely many of the input seminorms. We apply this with a fixed diagonal sign matrix after (P1), so parameter derivatives of $H$ do not enter the Gaussian. The case $k=0$ is the identity with determinant and Gaussian factor one.

<a id="stationary-phase"></a>
## 3. Stationary phase and its nonstationary complement

Suppose $f(t,y)$ has exactly one critical point $y_c(t)$ on a neighborhood of the compact support of $a(t,y,R)$, and that point is nondegenerate. Assume (P7) for $a$. Then
\[
 \begin{split}
 \int e^{iRf(t,y)}a(t,y,R)\,dy
 ={}&e^{iRf(t,y_c(t))}(2\pi/R)^{k/2}
       e^{i\pi\operatorname{sgn}f_{yy}/4}\left[
       \sum_{j<L} R^{-j}B_j(t,R)+E_L(t,R)\right],\\
 B_0(t,R)={}&|\det f_{yy}(t,y_c(t))|^{-1/2}a(t,y_c(t),R),\\
 |\partial_t^\alpha\partial_R^a E_L(t,R)|
       \le{}& C_{L\alpha a}R^{q-L-a}.
 \end{split}
 \tag{P9}
\]
The $B_j$ are explicitly $(i/2)^jQ_D^jb(t,0,R)/j!$, where $b$ is the amplitude, including its coordinate Jacobian, in (P1), and $D=\operatorname{diag}(\varepsilon_j)$. They have order $q$ and depend on finitely many amplitude and phase derivatives. The error bound is for the bracket **after removing the displayed critical-value exponential**.

Choose a cutoff equal to one near the critical point and supported in its quadratic coordinate patch. There (P1), change of variables and (P4)–(P8) prove (P9); (P3) gives its leading coefficient. On the complementary support, $|f_y|\ge c>0$. The operator
\[
 L_f=\frac{f_y\cdot\partial_y}{iR|f_y|^2}
 \quad\hbox{satisfies}\quad L_fe^{iRf}=e^{iRf}.
 \tag{P10}
\]
Each integration by parts with its transpose supplies $R^{-1}$ and finitely many derivatives of smooth coefficients and the amplitude. After any prescribed parameter derivatives the phase contributes only a fixed number of additional powers of $R$; further integrations absorb them. Frequency derivatives and the removal of the critical exponential have the same property. The complementary integral is therefore $S^{-\infty}$ in $R$, with all parameter derivatives, and can be included in $E_L$. This also proves the assertion when no critical point is present. A finite partition gives the sum over several isolated nondegenerate critical points. Such points are finite on the compact support after localization, since each is isolated and an accumulation point would also be critical and nondegenerate. Classical input amplitudes give a classical expansion: the coefficient at one output degree is the finite sum of terms whose amplitude degree loss and Gaussian Taylor degree add to that loss.

<a id="oscillatory-phase-kernels"></a>
## 4. Homogeneous oscillatory kernels as distributions

A real phase $\phi(x,\theta)$ on a conic patch in
$\mathbb R^d_x\times(\mathbb R^N_\theta\setminus0)$ is homogeneous of degree one in $\theta$ and has $d\phi\ne0$. With $a$ of order $q$ and the support convention above, use the local normalization
\[
 I_\phi(a)=(2\pi)^{-(d+2N)/4}
                   \int e^{i\phi(x,\theta)}a(x,\theta)\,d\theta
                         \,|dx|^{1/2}.
 \tag{P11}
\]
The meaning is a cutoff limit on compact smooth dual half-density tests. This limit exists and is independent of the frequency cutoff, as follows.

On the closed normalized support let
\[
 F=\langle\theta\rangle^{-2}|\phi_x|^2+|\phi_\theta|^2,
 \qquad
 L=\frac{\langle\theta\rangle^{-2}\phi_x\cdot\partial_x
                       +\phi_\theta\cdot\partial_\theta}{iF}.
 \tag{P12}
\]
Homogeneity, $d\phi\ne0$ and compactness make $F$ bounded below for $|\theta|\ge1$. The $x$ coefficients have order $-1$ and the $\theta$ coefficients order zero. Thus the transpose $L^{\mathrm{tr}}$, acting on the amplitude times the compact test, lowers its symbol order by one: an $x$ derivative is accompanied by order $-1$, while a $\theta$ derivative itself lowers the order. Also $Le^{i\phi}=e^{i\phi}$. After $M>q+N$ integrations by parts the integral is absolutely convergent. All derivatives of an extra cutoff $\chi(\epsilon\theta)$ have the corresponding uniform symbol bounds on their transition annulus, and terms differentiating it tend to zero by that same integrable majorant. This proves the distributional limit and its continuity in finitely many test derivatives. Derivatives of any fixed finite order in external parameters are handled by increasing $M$.

Where $\phi_\theta\ne0$, use only the $\theta$ part
$\phi_\theta\cdot\partial_\theta/(i|\phi_\theta|^2)$.
Its transpose lowers order by one without differentiating a test. After any number of base derivatives, more integrations make the amplitude integrable. Consequently a part supported away from $\phi_\theta=0$ is a smooth kernel. An amplitude of every negative order gives a smooth kernel directly by absolute integration after all base derivatives. These facts justify all later support cutoffs and retained smooth errors.

<a id="phase-geometry"></a>
## 5. Nondegenerate phases and construction at a caustic

A phase is nondegenerate if the $N$ differentials of $\phi_\theta$ are independent on
$C_\phi=\{\phi_\theta=0\}$. The inverse theorem applied to an invertible minor makes $C_\phi$ a smooth manifold of dimension $d$. Its map
\[
 \kappa_\phi:C_\phi\longrightarrow T^*X\setminus0,
             \qquad (x,\theta)\longmapsto(x,\phi_x)
 \tag{P13}
\]
is an immersion and is a diffeomorphism onto its image after restricting to a sufficiently small conic patch. To prove injectivity of its differential, a tangent vector $(u,v)$ in its kernel has $u=0$,
$\phi_{x\theta}v=0$ and $\phi_{\theta\theta}v=0$. The transpose of the full-rank matrix $d(\phi_\theta)$ is injective, so $v=0$. Choose $d$ independent image coordinates and use their inverse theorem to obtain the asserted local inverse. The image avoids the zero section because $d\phi\ne0$.

The tautological form $\alpha=\sum\xi_jdx_j$ pulls back to zero on $C_\phi$. Indeed Euler's identity gives $\phi=\theta\cdot\phi_\theta=0$ there, and
$\kappa_\phi^*\alpha=d(\phi|_{C_\phi})=0$.
Its differential also vanishes. The image has dimension $d$, so it is Lagrangian; homogeneity makes it conic. Its base-projection corank is
\[
 \operatorname{corank}(d\pi|_\Lambda)
                 =N-\operatorname{rank}\phi_{\theta\theta}.
 \tag{P14}
\]
In fact the kernel of the base differential consists exactly of the tangent vectors $(0,v)$ with $\phi_{\theta\theta}v=0$. This proves the rank identity even where the rank changes nearby. Euler's identity also gives $\phi_{\theta\theta}\theta=0$, so this corank is at least one.

Conversely let $\Lambda\subset T^*X\setminus0$ be an embedded conic Lagrangian, and let $\lambda_0=(x_0,\xi_0)\in\Lambda$. First $\alpha|_\Lambda=0$: the radial tangent vector $(0,\xi)$ lies in $T\Lambda$, and its symplectic pairing with any tangent vector is $\alpha$ on that vector. Let the base-projection rank at $\lambda_0$ be $d-r$. Choose linear base coordinates $(x',x'')$, of dimensions $d-r$ and $r$, so that the image of that differential is the $x'$ subspace. Then
\[
 \Lambda\longrightarrow(x',\xi'')
 \tag{P15}
\]
has invertible differential. For a vector in its kernel, $dx'=0$ forces $dx=0$ by the choice of the projected tangent space. Isotropy says that its vertical covector annihilates that projected tangent space, so $d\xi'=0$; the assumed $d\xi''=0$ then makes the vector zero. The dimensions agree, proving invertibility.

Write the local inverse as $x''=F(x',\eta)$, $\xi'=G(x',\eta)$, $\xi''=\eta$. The radial tangent and (P15) imply $\eta_0\ne0$. After conic restriction, uniqueness of the inverse gives $F$ degree zero and $G$ degree one in $\eta$. The identity $\alpha|_\Lambda=0$ reads $G\,dx'+\eta\,dF=0$. Thus the explicit function
$S(x',\eta)=\eta\cdot F(x',\eta)$ satisfies
$dS=F\,d\eta-G\,dx'$.
The homogeneous phase
\[
 \phi(x',x'',\eta)=x''\cdot\eta-S(x',\eta)
 \tag{P16}
\]
has critical equation $x''=F$, and its critical covectors are $(G,\eta)$. The derivative of that equation in $x''$ is the identity, so the phase is nondegenerate and parametrizes the given $\Lambda$. Moreover $F_\eta=0$ at the initial point, since every projected tangent has zero $x''$ component there; hence $\phi_{\eta\eta}=0$ at that point. This constructs a minimal phase with $r$ frequency variables at every point, including a caustic, without assuming locally constant base rank.

<a id="phase-equivalence"></a>
## 6. Elimination and equivalence of homogeneous phases

**Removing an invertible frequency block.** Split $\theta=(\theta',\theta'')$ so that the $k\times k$ block $\phi_{\theta''\theta''}$ is invertible at the chosen critical point. The retained vector $\theta'_0$ is nonzero: otherwise $\phi_{\theta\theta}\theta_0=0$ and invertibility of that block would force $\theta''_0=0$. Solve $\phi_{\theta''}=0$ as
$\theta''=g(x,\theta')$ by the parameter inverse theorem. Uniqueness and homogeneity make $g$ homogeneous of degree one. The reduced phase
\[
 \phi_0(x,\theta')=\phi(x,\theta',g(x,\theta'))
 \tag{P17}
\]
is nondegenerate and parametrizes the same Lagrangian. To check the rank assertion, first replace $\theta''$ by $\theta''-g$. On its zero set the critical equations in this block have differentials only in $d\theta''$, with invertible coefficient. The other critical equations restrict exactly to $d(\phi_{0,\theta'})$. Independence of all the original equations therefore gives independence of the reduced ones. The base gradients also agree on their critical sets. Block elimination of the symmetric frequency Hessian shows that the reduced Hessian is its Schur complement. If $k$ is the entire original Hessian rank at the point, this Schur complement is zero there.

Put $r=|\theta'|$, $\omega=\theta'/r$ in a small angular patch, and write
$\theta''=g(x,\theta')+rv$. Apply (P1) to the smooth function of $(x,\omega,v)$ obtained by dividing the phase by $r$. On a smaller conic patch a homogeneous fiber coordinate $w$ then gives the exact identity
\[
 \phi=\phi_0(x,\theta')+\frac{w^TDw}{2r},
 \qquad D=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_k).
 \tag{P18}
\]
The transformation is homogeneous of degree one in all frequency variables, with degree-zero Jacobian. This is the required homogeneous quadratic reduction; its proof uses the parameter construction, not an unproved homogeneous Morse assertion.

In (P11), after this change of variables, integrate first in $w$. The support has $|w|\le Cr$. On setting $w=rv$, (P4)–(P9) show that the exact reduced amplitude is classical of order $q+k/2$, with every finite error of order $q+k/2-L$. Its leading term is
\[
 b_{q+k/2}(x,\theta')=
    e^{i\pi\operatorname{sgn}D/4}r^{k/2}
                        a_q(x,\theta',0).
 \tag{P19}
\]
Here $a$ already includes the homogeneous coordinate Jacobian. The factor $(2\pi)^{-k/2}$ arising from the two normalizations in (P11) cancels the Gaussian factor $(2\pi)^{k/2}$. All base and angular derivatives are covered by (P8), and a $\theta'$ derivative is $r^{-1}$ times a combination of $r\partial_r$ and angular derivatives. Thus the assertion is a full $S_{1,0}$ symbol assertion, including smooth external parameters. The low-frequency differences and the noncritical tails are smooth by Section 4.

Conversely any amplitude $b$ for the reduced phase is obtained modulo $S^{-\infty}$ by choosing in (P18)
$a=e^{-i\pi\operatorname{sgn}D/4}r^{-k/2}b(x,\theta')\chi(w/r)$,
where $\chi=1$ near zero and has small compact support. In stationary phase all its positive-order $v$ derivatives at zero vanish. Thus (P19) gives $b$ and all further stationary coefficients vanish; (P8) leaves an arbitrarily low-order error. This proves equality of the local kernel classes under insertion as well as removal of quadratic variables.

**Equivalence of minimal phases.** Suppose two nondegenerate phases $\phi(x,\theta)$ and $\psi(x,\sigma)$ parametrize the same Lagrangian near one covector, and both frequency Hessians vanish at their respective points. Equation (P14) makes their frequency dimensions equal, say $N$. Their matrices $\phi_{\theta x}$ and $\psi_{\sigma x}$ both have rank $N$ and have the same kernel, the projected tangent space of $\Lambda$. Choose the same $N$ base coordinates $x''$ so that both critical sets can be solved for $x''$; each critical set is then parametrized by $(x',\theta)$ or $(x',\sigma)$.

The identification through $\Lambda$ is a diffeomorphism of these two critical sets preserving $x'$. It has the form
$(x',\theta)\mapsto(x',S(x',\theta))$ with invertible $S_\theta$. It also preserves the actual $x''$ values and is homogeneous in frequency. Extend it to the neighborhood by keeping this formula independent of $x''$. This gives a homogeneous fiber diffeomorphism. After pulling back $\psi$ by it, the two phases have the same critical set $C$ and the same first derivatives there. Their values are both zero there by Euler's identity.

Use $(x',\theta,v)$ with $v=\phi_\theta$ as coordinates near $C$. Taylor's formula in $v$ writes the difference as
\[
 \psi-\phi=\tfrac12 v^TB(x,\theta)v,
 \tag{P20}
\]
where $B$ is symmetric, smooth and homogeneous of degree one. Seek a symmetric matrix $W$ and the fiber change $\theta\mapsto\theta+Wv$. Taylor's formula gives
\[
 \phi(x,\theta+Wv)-\phi(x,\theta)
       =v^TWv+\tfrac12v^TW C(x,\theta,Wv)Wv,
 \tag{P21}
\]
where $C=2\int_0^1(1-s)\phi_{\theta\theta}(x,\theta+sWv)\,ds$ is symmetric. It suffices to solve on the finite-dimensional space of symmetric matrices
$W+\tfrac12WCW=B/2$.
At the initial point $v=0$ and $C=0$, so $W_0=B/2$ solves it, and its derivative with respect to $W$ is the identity: the dependence of $C$ on $W$ contains the vanishing factor $v$. The inverse theorem supplies a smooth solution. Its homogeneous extension has degree one, since the equation scales with $B$ and $W$ of degree one, $v$ of degree zero and $C$ of degree minus one; uniqueness gives consistency on overlapping normalized patches. The derivative of the resulting fiber map at the initial point is $I+W\phi_{\theta\theta}=I$. It is a local diffeomorphism and (P20)–(P21) prove exact phase equivalence.

Every nondegenerate phase reduces by its full invertible Hessian block to one of these minimal phases. Thus any two phases for the same Lagrangian are related locally by homogeneous fiber changes and insertion or removal of nondegenerate quadratic variables. All constructions persist smoothly for parameters near the initial point. No equality of the base-projection rank at nearby points was used.

<a id="maslov-line"></a>
## 7. Critical densities and the exact Maslov convention

In coordinates $(u,v)$ with $v=\phi_\theta$, define a positive density on $C_\phi$ by
\[
 d_\phi=
  \left|\det\frac{\partial(u,\phi_\theta)}{\partial(x,\theta)}\right|^{-1}
                           |du|\quad\hbox{on }C_\phi.
 \tag{P22}
\]
The change-of-variables formula proves independence of the extended coordinates $u$: on $v=0$ their Jacobian has the required triangular blocks, and the tangent-coordinate determinant cancels the transformation of $|du|$. This is the concrete meaning of dividing the ambient density by the critical-equation density.

Under a fiber change $\theta=\Theta(x,\vartheta)$ let $J=\Theta_\vartheta$. On the critical set the new equations satisfy
$d(\widetilde\phi_\vartheta)=J^T d(\phi_\theta)$.
The ambient Jacobian contributes $|\det J|$, and the critical-equation Jacobian contributes its reciprocal when expressing the old equations in the new ones. Hence
$\Theta^*d_\phi=|\det J|^2d_{\widetilde\phi}$.
The transformed amplitude is $\widetilde a=(a\circ\Theta)|\det J|$, so
$\widetilde a_q\sqrt{d_{\widetilde\phi}}$ is exactly the pullback of $a_q\sqrt{d_\phi}$. With an additional base change $x=\kappa(X)$, its square-root Jacobian appears on both sides because the kernel is a half density. This proves the full coordinate rule. Under positive frequency dilation, the ambient density scales by $r^N$ while the equations $\phi_\theta$ have degree zero. Thus $\sqrt{d_\phi}$ has degree $N/2$.

For (P18), at $w=0$ the last $k$ critical equations have differential $D\,dw/r$, and the other ones reduce to those of $\phi_0$. Therefore
\[
 d_\phi=r^k d_{\phi_0},\qquad
 b_{q+k/2}\sqrt{d_{\phi_0}}
       =e^{i\pi\operatorname{sgn}D/4}a_q\sqrt{d_\phi}.
 \tag{P23}
\]
The density is identified along the common Lagrangian. Invertible congruence preserves the signature of a symmetric form: its positive index is the largest dimension of a subspace on which it is positive definite, a description invariant under an invertible linear map; the eigenbasis proves this equals its number of positive eigenvalues, and likewise for the negative index. Consequently Hessians add signatures under the quadratic reduction and keep their signatures under fiber equivalence on the critical set.

For two phase patches $j,k$ let $H_j=\phi_{j,\theta\theta}$ on their critical sets, matched at the same Lagrangian covector, and set
\[
 c_{jk}=\frac{(\operatorname{sgn}H_k-N_k)
                        -(\operatorname{sgn}H_j-N_j)}2.
 \tag{P24}
\]
This is an integer: (P14) fixes $N-\operatorname{rank}H$ on the overlap, and signature and rank have the same parity. It is locally constant even across a caustic. To see this, reduce both phases at any chosen point as in Section 6. Their reduced phases are equivalent on a neighborhood, so their possibly varying reduced Hessians have equal signatures pointwise; the eliminated blocks have fixed signatures. Their difference is therefore constant there. Positive frequency dilation leaves it unchanged, and direct subtraction gives
$c_{jk}+c_{kl}=c_{jl}$.

Glue local copies of $\mathbb C$ with the rule $s_j=i^{c_{jk}}s_k$. The cocycle equality makes the identifications transitive, and the locally constant transitions define a flat complex line on $\Lambda$: the **Maslov line** in this convention. No cohomology theorem or global trivialization is needed for this construction. Sections differentiate in these constant frames, and multiplication by the transition constants makes those derivatives agree.

Parallel transport here has a direct construction. Cover the compact image of a finite path by finitely many phase patches and subdivide its parameter interval so that each subpath stays in one patch. Keep its coefficient constant there and apply the transition constant at each change of patch. Refining the subdivision changes nothing; two choices have a common refinement, on which the cocycle identity gives the same result. Transport is therefore well defined, composes under concatenation and reverses to its inverse. It preserves absolute values since all transition factors have modulus one. For nearby smooth paths the same subdivision and patches apply, and the transition constants stay constant; this proves smooth dependence and locally constant holonomy for closed paths. The holonomy of any closed path is a product of powers of $i$, hence a fourth root of unity. This is the precise flat transport used along a Hamilton trajectory; it does not choose a preferred global trivialization of the line.

For the unshifted phase integral (P11), its principal coefficient in this line is
\[
 s_\phi=e^{i\pi N/4}a_q\sqrt{d_\phi},
 \qquad q=m+\frac{d-2N}{4}.
 \tag{P25}
\]
It has homogeneous degree $m+d/4$. Indeed (P23) and the equivalence theorem give, with $\gamma_j=a_{q,j}\sqrt{d_{\phi_j}}$,
$\gamma_k=e^{i\pi(\operatorname{sgn}H_j-\operatorname{sgn}H_k)/4}\gamma_j$.
Multiplying by $e^{i\pi N_k/4}$ proves precisely $s_j=i^{c_{jk}}s_k$. Equivalently one may put $e^{-i\pi N/4}$ into the phase-integral normalization and use the rephased amplitude for its symbol. Mixing these two conventions would lose a phase factor.

For the identity graph on an $n$-dimensional manifold use the phase $(x-y)\cdot\eta$. In (P11), $d=2n$ and $N=n$, so its unshifted integral is exactly $(2\pi)^{-n}\int e^{i(x-y)\eta}a(x,\eta)\,d\eta$. With $a=1$ it is the identity kernel by Fourier inversion. Its distinguished Maslov half-density symbol is the section represented by
$e^{i\pi n/4}|dy\,d\eta|^{1/2}$ in (P25). Using this actual identity section as the identity-graph frame gives the usual scalar pseudodifferential principal symbol $a$. This specifies the identity normalization without presuming that a Maslov line on another Lagrangian has a preferred global frame.

<a id="principal-symbol-proof"></a>
## 8. Realization, loss of one order and recovery of the symbol

Define $I^m_{\mathrm{cl}}(X,\Lambda)$ locally by sums of (P11), with classical amplitude order $q=m+(d-2N)/4$, and smooth kernels. Use locally finite supports over the base. Sections 5–7 show that these local classes agree under phase changes and give the transition law for a proposed leading symbol. We now prove that this symbol is realized and is determined by the actual distribution modulo one lower order.

**Extension and vanishing.** Normalize frequency by its positive radius. The critical equations have independent differentials on the normalized space as well: the radial direction is in their kernel, so removing it does not lower their rank. An invertible minor gives local coordinates $(u,v)$ there with $v=\phi_\theta$. The map $(u,v)\mapsto(u,0)$, extended with unchanged radius, is a smooth homogeneous retraction to the critical set. It extends a homogeneous scalar coefficient on $C_\phi$ off that set without changing its degree; a supported cutoff then gives an amplitude in the phase patch.

If the leading amplitude vanishes on $C_\phi$, Taylor's formula in $v$ gives, near that set,
$a_q=\sum_j\phi_{\theta_j}b_j$, where each $b_j$ has degree $q$ and has symbol estimates of that order. Explicitly the coefficient is the integral of the corresponding transverse derivative along $(u,sv)$, $0\le s\le1$; the retraction coordinates are smooth and degree zero on the normalized space. Use a cutoff equal to one near the relevant critical set. Its complement gives a smooth kernel by Section 4. In the remaining integral,
$\phi_{\theta_j}e^{i\phi}=(1/i)\partial_{\theta_j}e^{i\phi}$,
so integration by parts replaces that term by $-(1/i)\partial_{\theta_j}b_j$, of order $q-1$. Section 4 justifies the cutoff limit and boundary terms. The part of $a$ below its leading homogeneous term already has that order. Thus zero leading restriction lowers the actual kernel order by one.

A desired homogeneous Maslov half-density section of degree $m+d/4$ is realized as follows. In a phase frame divide it by $e^{i\pi N/4}\sqrt{d_\phi}$, obtaining a coefficient of degree $q$. Extend it by the preceding retraction, cut off small frequency, and form (P11). A partition on the normalized Lagrangian gives the sum of these constructions. Over a compact base portion, closedness of $\Lambda$ makes its unit-covector portion compact, so the partition is finite. For noncompact base portions use a locally finite compact exhaustion: smooth cutoffs $\alpha_j$ equal to one on the $j$th compact set give
$\beta_j=\alpha_j\prod_{l<j}(1-\alpha_l)$.
These are locally finite, sum to one by telescoping, and each has compact support; apply finite partitions on their supports. Such cutoffs are supplied by the coordinate reading. Homogeneous extension from the unit covectors preserves all symbol estimates. On an overlap (P19) and (P25) identify the leading restrictions; their difference has zero restriction and is one order lower by the preceding paragraph. Refining two partitions by their pairwise products proves that the constructed class modulo $I^{m-1}$ is independent of the partition and the extensions.

**A transverse test that reads the coefficient.** At any $\lambda_0=(x_0,\xi_0)\in\Lambda$ there is a real smooth $\psi$ with $\psi_x(x_0)=\xi_0$ such that the graph of $d\psi$ is transverse to $\Lambda$ there. Here is the needed linear algebra. Choose the base splitting used in (P15). Its tangent space has the form
$\{(u,0;Au,v)\}$ with $A$ symmetric: vertical covectors annihilate the projected tangent space, and isotropy makes the remaining block symmetric. Choose the $x'x'$ Hessian block of $\psi$ to be $A+I$, and its other Hessian blocks zero, with the prescribed linear term. A common tangent vector of the two graphs would have $x''$ component zero and would satisfy $(A+I)u=Au$, hence $u=0$ and then be zero. This proves transversality, including the case with no $x'$ coordinates.

Set $\theta=R\omega$ in the pairing with $u(x)e^{-iR\psi(x)}$, where $u$ is a compact smooth dual coefficient supported sufficiently near $x_0$. The critical equations of
$\Phi(x,\omega)=\phi(x,\omega)-\psi(x)$ are
$\phi_\omega=0$ and $\phi_x=\psi_x$. They have precisely the matched critical point $(x_0,\omega_0)$ on the localized phase patch. Its Hessian is invertible. In fact, a Hessian-kernel vector satisfies the tangent equations for $C_\phi$, and its image by $d\kappa_\phi$ lies in the tangent graph of $d\psi$. Transversality makes that image zero, and the immersion in (P13) then makes the original vector zero. Let $K=\Phi''(x_0,\omega_0)$.

Stationary phase in the $d+N$ variables gives
\[
 \begin{split}
 e^{iR\psi(x_0)}\langle I_\phi(a),u e^{-iR\psi}\rangle
 ={}&(2\pi)^{d/4}e^{i\pi\operatorname{sgn}K/4}|\det K|^{-1/2}
       a_q(x_0,\omega_0)u(x_0)R^{m-d/4}\\
 &\quad+O(R^{m-d/4-1}).
 \end{split}
 \tag{P26}
\]
The power follows from $R^N$ in the frequency substitution, $R^{-(d+N)/2}$ from stationary phase and $R^q$ from the leading amplitude. The $(2\pi)^{d/4}$ factor follows from (P11). Euler's identity makes $\phi(x_0,\omega_0)=0$, accounting for the exponential on the left.

Here are the support and tail details needed to apply (P9) to that unbounded frequency integral. First discard portions away from $C_\phi$; they are smooth by Section 4 and their pairings decrease rapidly by (P10), since $\psi_x\ne0$ near $x_0$. On a small conic neighborhood of the remaining critical point, $c|\theta|\le|\phi_x|\le C|\theta|$. If $|\theta|/R$ is sufficiently small or large, then
$|\phi_x-R\psi_x|\ge c'(R+|\theta|)$.
Integrating in $x$ with that gradient gives, after $M$ transfers, an integrable majorant
$C_M\langle\theta\rangle^q(R+|\theta|)^{-M}$.
Split its radial integral at $|\theta|=R$; increasing $M$ gives every desired inverse power of $R$. In the retained comparable-frequency region $\omega$ ranges in a compact annulus. Outside a small neighborhood of its unique critical point the full $(x,\omega)$ gradient is bounded below, so (P10) again gives every inverse power. Only the compact stationary neighborhood remains, where (P9) applies. The same estimates are uniform for small smooth parameter changes of the test and phase and after their derivatives. This proves (P26) with its full classical expansion, rather than a formal rescaling.

If two local representations give the same distribution, convert the finitely many phase pieces meeting $\lambda_0$ to one phase by Section 6. Pieces whose critical images miss that covector have no stationary point in this test after shrinking its support and have rapid pairings by the estimates just given. The leading coefficient in (P26) therefore reads the sum of the critical amplitudes in the common frame. It is zero for the zero distribution. An $I^{m-1}$ representation gives at most $O(R^{m-1-d/4})$, so it too has zero coefficient at degree $m-d/4$. Since $\lambda_0$ and $u(x_0)\ne0$ were arbitrary, this proves well-definedness and recovery of the principal symbol. Conversely, zero principal symbol lowers every localized piece by the vanishing argument. Together with realization this proves the exact correspondence
\[
 I^m_{\mathrm{cl}}(X,\Lambda)/I^{m-1}_{\mathrm{cl}}(X,\Lambda)
 \quad\longleftrightarrow\quad
 \{\text{smooth homogeneous Maslov half-density sections of degree }m+d/4\}.
 \tag{P27}
\]
Support restrictions are retained in both directions. Cutoff summation from the scalar reading, on each phase patch and after every parameter derivative, realizes successive orders $m-j$. It does not change the homogeneous conic support. A remainder of every negative order is smooth by Section 4. None of these arguments asserts that an arbitrary matrix-valued or positive-excess composition has already been proved.

<a id="phase-wavefront"></a>
## 9. Wavefront inclusion and a nonzero symbol

In a coordinate chart, $(x_0,\xi_0)$ is absent from the wavefront set of a distribution if a cutoff equal to one near $x_0$ has a Fourier transform decreasing faster than every power on a cone about $\xi_0$. A compactly supported distribution has a polynomially bounded Fourier transform: its finite-order test estimate applied to $e^{-ix\xi}$ times a fixed support cutoff gives $C\langle\xi\rangle^M$. Multiplying by another smooth cutoff preserves rapid decrease on a smaller cone. To prove this last assertion, use Fourier convolution with the rapidly decreasing transform of the new cutoff. For $\xi$ in the smaller cone, split at $|\xi-\eta|\le\epsilon|\xi|$. In that part $\eta$ is in the original cone and comparable to $\xi$, so its rapid bound applies. In the complement the rapid decrease of the cutoff transform dominates both the polynomial bound in $\eta$ and any desired power of $|\xi|$. Absolute integration, with an arbitrarily high chosen decay exponent, proves the claim.

For (P11) the wavefront is contained in the image of $C_\phi$ under (P13). Localize near a candidate covector outside that image. In the Fourier integral the phase is $\phi(x,\theta)-x\cdot\xi$. Discard the smooth part away from $C_\phi$ as before. Where $|\theta|$ and $|\xi|$ are incomparable, integration in $x$ has the same lower gradient bound and integrable majorant as in the proof of (P26), with $R=|\xi|$. In the comparable-frequency region put $\theta=R\omega$, $\xi=R\nu$. Both $\omega$ and the chosen unit directions $\nu$ range in compact sets. There is no critical point of $\phi(x,\omega)-x\nu$, and its full gradient is bounded below uniformly after shrinking the base and directional neighborhoods. Repeated integration by parts gives every inverse power of $R$, including the original $R^N$ and symbol factors. This is the required Fourier decrease. A finite phase cover and cutoff stability prove
\[
 \operatorname{WF}(I_\phi(a))\subset\Lambda.
 \tag{P28}
\]

Finally, absence from the wavefront would make the nonlinear transverse test in (P26) rapidly decreasing. We verify this implication rather than assuming it. Choose $\psi$ and $u$ as in that proof, with $\psi_x$ in a compact subcone of the regular Fourier cone and with $0<c\le|\psi_x|\le C$. Fourier inversion for the test gives the pairing as
\[
 (2\pi)^{-d}\int \widehat v(\xi)G_R(\xi)\,d\xi,
 \qquad G_R(\xi)=\int u(x)e^{i(x\xi-R\psi(x))}\,dx,
 \tag{P29}
\]
where $v$ is a compact localization of the distribution equal to it near the support of $u$. The test is Schwartz, so this is the usual distributional Fourier pairing. In the regular cone with $cR/2\le|\xi|\le2CR$, use $|G_R|\le\|u\|_1$ and arbitrarily rapid decay of $\widehat v$; the region has volume $O(R^d)$. Everywhere else
$|\xi-R\psi_x|\ge c_1(|\xi|+R)$,
after choosing the compact subcone strictly inside the original cone. Integration by parts in $x$ gives
$|G_R(\xi)|\le C_L(|\xi|+R)^{-L}$.
The global polynomial bound for $\widehat v$ then makes its integral rapidly decreasing in $R$ by choosing $L$ large. This proves the implication. The estimates are uniform for the smooth directional families of tests involved.

If $s_\phi(\lambda_0)\ne0$, its scalar leading amplitude is nonzero there. Taking $u(x_0)\ne0$ in (P26) gives a nonzero leading power of $R$, contradicting the rapid decrease in (P29). Thus
\[
 \{\lambda\in\Lambda:s(\lambda)\ne0\}
            \subset\operatorname{WF}(I),
 \qquad I\in I^m_{\mathrm{cl}}(X,\Lambda).
 \tag{P30}
\]
In particular an everywhere nonzero principal symbol gives wavefront set exactly $\Lambda$. The same nonlinear-test estimate proves the coordinate rule for wavefront: after a smooth base change, a Fourier test has phase $\kappa(x)\cdot\eta$ with gradient $D\kappa(x)^T\eta$, and the Jacobian is a smooth amplitude. Apply the estimate uniformly in a small cone of $\eta$ directions and then apply the inverse coordinate change for the reverse inclusion. This proves coordinate independence for the assertions above. It does not establish the separate pullback theorem for a general map with a possibly noninvertible differential.
