# Clean composition with positive excess

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="clean-composition"></a>

This reading proves clean composition of classical scalar Fourier integral operators, including positive excess, the actual kernel product, every finite symbol remainder and the principal-symbol fiber integral. For the geometric framework, see [Victor Guillemin and Shlomo Sternberg, *Semi-Classical Analysis*, author text dated 25 April 2012, Sections 5.1.1, 5.6–5.7 and 8.13](https://people.math.harvard.edu/~shlomo/docs/Semi_Classical_Analysis_Start.pdf). The proof below includes the homogeneous removal of inactive variables and derives the order, density and Maslov factors in the classical normalization used here.

First read [Phase geometry, stationary phase and the Maslov symbol](phase-geometry-and-stationary-phase.md#phase-foundations), Sections 1–9, and [Transverse composition and graph operators](transverse-composition-and-graph-operators.md#transverse-composition), Sections 1–6. Their proved inputs are homogeneous phase equivalence, stationary phase with differentiated remainders, critical densities and Maslov transitions, symbol recovery, smooth-input FIO actions, distributional cutoff limits and the incomparable-frequency estimate. We use the same closed conic support convention: normalized critical supports over compact base patches stay away from either zero covector component, and phase cutoffs have closed support inside their coordinate patches. The [inverse-coordinate proof](coordinate-inverses-and-integration.md#coordinate-inverse), [change of variables](coordinate-inverses-and-integration.md#coordinate-integration) and [finite partitions](coordinate-inverses-and-integration.md#finite-partitions) supply the coordinate and integration facts used below. The short flow argument needed for reduction is proved here.

<a id="clean-matching-geometry"></a>

## 1. Hypotheses and the geometry of matching

Let $A_1:Y\to X$ and $A_2:Z\to Y$ be properly supported scalar classical FIOs on half densities, of orders $m_1,m_2$, with conic canonical relations $C_1,C_2$. Both covector components of each relation are nonzero. Write $d=n_X+n_Z$ and $M=C_1\times C_2$. On the matching set $M_0$, the two intermediate points of $T^*Y$ coincide. Let $E=T(T^*Y)$ at that common point, and let
\[
 \begin{aligned}
 &D:TM\longrightarrow E,\quad D(v)=v_{Y_1}-v_{Y_2},\\
 &\pi:M_0\longrightarrow T^*X\times T^*Z
 \end{aligned}
 \tag{E1}
\]
be the difference differential and the outer projection. The following are the clean-composition hypotheses on the part of the relations meeting the symbol supports. The set $M_0$ is a smooth submanifold, $TM_0=\ker D$, and $\operatorname{rank}D=2n_Y-e$ is constant. The image $C=\pi(M_0)$ is an embedded manifold, and $\pi$ is proper on the closed matching supports over compact normalized portions of $C$. Equivalently for the local theorem, one may work with a specified embedded image branch and this same properness over it. Assume $e$ fixed on that portion. No graph condition or regularity of projection onto the base variables is imposed. Compact matching fibers are allowed to have several components; connected fibers are a special case.

Here is the linear algebra that also proves the dimension assertions implicit in these hypotheses. The tangent space $TM$ is Lagrangian for
$\omega_X-\omega_{Y_1}+\omega_{Y_2}-\omega_Z$.
A vector in $V=\ker d\pi$ has the form $(0,w,w,0)$. Its pairing with a vector $v\in TM$ is $-\omega_Y(w,Dv)$. Conversely, if $w$ annihilates $\operatorname{im}D$ under $\omega_Y$, the vector $(0,w,w,0)$ annihilates $TM$ and hence belongs to $TM$, since a Lagrangian equals its symplectic orthogonal. It belongs to $\ker D$ as well. Thus
\[
 \begin{aligned}
 &V\simeq(\operatorname{im}D)^{\omega_Y},\quad \dim V=e,\\
 &\dim M_0=d+e,\quad \operatorname{rank}d\pi=d.
 \end{aligned}
 \tag{E2}
\]
On $TM_0$ the intermediate symplectic forms cancel, so $\operatorname{im}d\pi$ is isotropic of dimension $d$, and is Lagrangian. Constant rank gives a local form directly: choose $d$ independent output coordinates, complete them to coordinates on $M_0$ by the inverse theorem, and note that the derivatives of every other output coordinate in the remaining directions vanish. On a small connected coordinate box these outputs are independent of those directions.

We check that the dimension of the embedded image $C$ is exactly $d$. Its dimension is at least $d$, since it contains these local images. The countable coordinate cover of $M_0$ expresses $C$ as a countable union of such images. In a coordinate chart of $C$, each is covered by countably many smooth $d$-dimensional graphs, using the same inverse-coordinate argument on its injective differential. If that chart had dimension greater than $d$, every graph would have measure zero: subtract its smooth graphing function in product coordinates and apply [Fubini's theorem](finite-derivative-l2.md#general-tonelli-fubini) to its singleton normal sections. Change of variables preserves this conclusion. A countable union of these sets cannot cover the positive-volume chart. Thus $\dim C=d$. Each local image is now open in $C$ by the inverse theorem, and $\pi$ is a submersion onto $C$. The tangent calculation proves that $C$ is Lagrangian; simultaneous dilation makes it conic.

We shall prove
\[
 A_1A_2\in I_{\mathrm{cl}}^{\,m_1+m_2+e/2}(X\times Z,C').
 \tag{E3}
\]
Here $C'$ changes the sign of the input covector, as in the transverse reading. The order assertion is membership; cancellation in a fiber integral can lower the actual order.

<a id="clean-homogeneous-reduction"></a>

## 2. Homogeneous removal of the inactive variables

Consider a real degree-one phase $\Phi(x,\omega)$ with $x\in\mathbb R^d$, $\omega\in\mathbb R^N\setminus0$. Its critical set $\mathcal C=\{\Phi_\omega=0\}$ is called clean of excess $e$ when it is a smooth manifold and
\[
 \begin{aligned}
 &T\mathcal C=\ker d(\Phi_\omega),\\
 &\operatorname{rank}d(\Phi_\omega)=K=N-e.
 \end{aligned}
 \tag{E4}
\]
Assume $\Phi_x\ne0$ there. The map $\kappa(x,\omega)=(x,\Phi_x)$ has a kernel on $T\mathcal C$ consisting of frequency vectors $h$ satisfying
$\Phi_{\omega\omega}h=0$ and $\Phi_{x\omega}h=0$.
This is the nullspace of $d(\Phi_\omega)^T$, of dimension $e$. Euler's identity gives
$d(\Phi_\omega)^T\omega=(\Phi_x,0)$
on $\mathcal C$, with the base and frequency components in that order. The radial vector is therefore not in this kernel. In particular $K\ge1$.

Fix a critical point and make a constant linear frequency change so that the last $e$ coordinate vectors span this kernel and the first $K$ coordinates contain the radial vector at that point. Its last $e$ coordinates are then zero. The differentials of the first $K$ components $F_i=\Phi_{\omega_i}$ are independent. Their zero set agrees locally with $\mathcal C$: it is a manifold of the same dimension containing $\mathcal C$, and the inverse-coordinate charts make that inclusion locally open. Every other $F_j$ consequently vanishes on that zero set.

Take a positive linear frequency coordinate $\rho$ on a small cone. The functions $F_i$ have degree zero, so their independent-coordinate construction can be made on the normalized slice $\rho=1$ and then extended by dilation. In coordinates $(u,F_1,\ldots,F_K)$ on this slice, the fundamental theorem of calculus gives
\[
 \begin{aligned}
 F_j(u,F)&=\sum_{i=1}^K g_{ji}(u,F)F_i,\\
 g_{ji}(u,F)&=\int_0^1\partial_{F_i}F_j(u,tF)\,dt.
 \end{aligned}
 \tag{E5}
\]
Extend $g_{ji}$ with degree zero. At the chosen point the last rows $dF_j$ vanish, so $g_{ji}=0$ there. The vertical vector field
$\nu_j=\partial_{\omega_j}-\sum_i g_{ji}\partial_{\omega_i}$
annihilates $\Phi$ exactly, throughout a neighborhood. The vector field $W=\rho\nu_j$ has degree-one coefficients and commutes with dilation.

For clarity, its local smooth flow follows directly from an integral equation. On a compact box in the base and frequency variables bound $W$ and its first derivatives by $B,L$. For $|v|\le T$, choose $BT$ smaller than the box margin and $LT<1/2$. The map
$z(v)\mapsto z_0+\int_0^v W(x,z(t))\,dt$
preserves the closed box of continuous curves and is a contraction. Its iterates have geometrically summable differences, yielding existence and uniqueness. Subtraction gives Lipschitz dependence on $(x,z_0)$. Parameter difference quotients converge to the unique solution of the differentiated linear integral equation: subtract that equation, use the uniform Taylor remainder for $W$ and absorb $LT$ times the supremum error. Repeating after differentiation proves smooth dependence of every finite order. Negative time gives the inverse flow. Uniqueness and $W(x,c\omega)=cW(x,\omega)$ give dilation equivariance wherever both flows are defined.

The hypersurface $\omega_j=0$ contains the chosen radial point and is transverse to $W$, since $W\omega_j=\rho>0$. Flowing from that hypersurface gives a frequency coordinate change
$\omega=\Theta(x,\eta,v)$,
where $\eta$ has $N-1$ degree-one coordinates and $v$ has degree zero. The inverse theorem applies because the frequency differential has full rank. The phase is constant along the flow and therefore independent of $v$. The new phase in $\eta$ is clean with the same rank $K$ and excess $e-1$: its critical equations together with an identically zero $v$ equation are an invertible transpose-Jacobian multiple of the old ones on their common zero set. Repeat on this smaller phase, carrying the already inactive parameters along. After $e$ steps we obtain
\[
 \begin{aligned}
 &\omega=\Theta(x,\eta,v),\\
 &\Theta(x,c\eta,v)=c\Theta(x,\eta,v),\\
 &\Phi(x,\Theta(x,\eta,v))=\psi(x,\eta),\\
 &\eta\in\mathbb R^K\setminus0,\qquad v\in\mathbb R^e .
 \end{aligned}
 \tag{E6}
\]
The phase $\psi$ is nondegenerate and generates the same local Lagrangian. This reduction is exact, including off the critical set in its coordinate neighborhood. Its frequency Jacobian
\[
 \begin{aligned}
 &J=|\det D_{(\eta,v)}\Theta|>0,\\
 &J(x,c\eta,v)=c^eJ(x,\eta,v)
 \end{aligned}
 \tag{E7}
\]
has degree $e$, since its $\eta$ columns have degree zero and its $v$ columns degree one. On closed smaller normalized patches $|\Theta|\asymp|\eta|$. These facts, including all their differentiated bounds, are the reason the homogeneous reduction preserves the full classical symbol class.

<a id="clean-compact-integration"></a>

## 3. Exact integration and the order shift

Localize by a degree-zero smooth partition to a reduction patch (E6), with its support closed inside the patch and compact in $v$. Terms supported away from $\mathcal C$ are smooth: on a closed normalized patch there, $|\Phi_\omega|$ has a positive lower bound; repeated integration by parts in frequency lowers the amplitude order indefinitely. For the retained term let $b\in S^q_{\mathrm{cl}}$. Write $(b\circ\Theta)(x,\eta,v)=b(x,\Theta(x,\eta,v))$, retaining the base variables. The exact coordinate change and ordinary compact $v$ integration give
\[
 \begin{aligned}
 &(2\pi)^{-(d+2N)/4}\int e^{i\Phi}b\,d\omega\\
 &\qquad=(2\pi)^{-(d+2K)/4}
                 \int e^{i\psi}B\,d\eta,\\
 &B(x,\eta)=(2\pi)^{-e/2}\int (b\circ\Theta)J\,dv .
 \end{aligned}
 \tag{E8}
\]
The common base half density is understood. Extend the integrand by zero from its closed interior support. The chain rule and (E7) show, for all multiindices, that
$|\partial_x^\alpha\partial_\eta^\beta B|
\le C_{\alpha\beta}\langle\eta\rangle^{q+e-|\beta|}$.
For example each frequency derivative of $\Theta$ has the degree required to cancel the corresponding derivative of $b$, and a frequency derivative of $J$ lowers its degree by one. Integration is over a fixed compact set after this extension; the same bounds hold for every smooth parameter derivative.

Apply this argument to each homogeneous coefficient of $b$ and to its remainder after $L$ coefficients. The coefficients of $B$ have degrees $q+e-j$, and the remainder belongs to $S^{q+e-L}$. Thus the expansion is classical with every finite differentiated remainder, not only a leading scaling identity. Low-frequency modifications are smooth. The distributional identity in (E8) follows first with compact frequency cutoffs and then against compact smooth tests. On the right the nondegenerate phase estimates already proved make those limits independent of the cutoff. On the left the transformed cutoffs have uniformly bounded order-zero seminorms and tend to one, uniformly in the compact $v$ set, so the same estimates apply before the $v$ integration. No absolute convergence of the original oscillatory integral is assumed.

If $q=m+(d-2N)/4$, then
\[
 q+e-\frac{d-2K}{4}=m+\frac e2.
 \tag{E9}
\]
The factor $(2\pi)^{-e/2}$ in (E8) is the ratio of the two displayed normalization constants. There is no stationary Gaussian in the inactive variables: the phase is exactly independent of them.

<a id="clean-kernel-product"></a>

## 4. Applying the reduction to the operator product

Take input phases $\phi_1(x,y,\theta)$ and $\phi_2(y,z,\sigma)$ with $N_1,N_2$ frequencies in the normalization (G1) of the transverse reading. With separate $y_1,y_2$, the input critical equations are independent and parametrize $C_1\times C_2$ locally. Add the equations
$y_1-y_2=0$ and $\phi_{1,y_1}+\phi_{2,y_2}=0$.
Clean matching says exactly that their joint zero set is a manifold whose tangent is the kernel of their differential, of codimension $N_1+N_2+2n_Y-e$. Eliminating $y_1-y_2$ by a determinant-one coordinate change yields the clean equations
\[
 \begin{aligned}
 &F=(\phi_{1,\theta},\phi_{2,\sigma},
                         \phi_{1,y}+\phi_{2,y})=0,\\
 &\operatorname{rank}dF=N_1+N_2+n_Y-e .
 \end{aligned}
 \tag{E10}
\]
The rank counts all variables, including $x,z$. Set
\[
 \begin{aligned}
 &r=(|\theta|^2+|\sigma|^2)^{1/2},\\
 &\omega=(ry,\theta,\sigma),\quad N=N_1+N_2+n_Y,\\
 &\Phi(x,z,\omega)=\phi_1(x,y,\theta)\\
 &\hspace{7em}+\phi_2(y,z,\sigma).
 \end{aligned}
 \tag{E11}
\]
At $F=0$, the differential of $\Phi_\omega$ is an invertible transpose-Jacobian multiple of $dF$. Thus $\Phi$ satisfies (E4) with this same excess $e$ and has nonzero outer covectors. Its critical set maps to $C'$ under the projection in (E1).

First localize each input amplitude to a sufficiently small conic neighborhood of its own phase critical set. Its complementary kernel is smooth by the nonstationary frequency estimate; composing that smooth term on either side remains smooth by the smooth-family argument in Section 1 of the transverse reading. On the retained closed normalized supports the nonzero intermediate covectors give uniform positive lower bounds for the ratios $|\phi_{1,y}|/|\theta|$ and $|\phi_{2,y}|/|\sigma|$. These bounds persist in the chosen neighborhoods.

The smooth-input and transpose actions in Section 1 of the transverse reading require only nonzero input and output covectors and proper support; they did not use transversality. Consequently the frequency-cutoff products converge on compact smooth inputs to the actual $A_1A_2$. On the neighborhoods just chosen, the incomparable-frequency proof in its Section 4 uses only
$|\phi_{1,y}|\asymp|\theta|$ and $|\phi_{2,y}|\asymp|\sigma|$.
Outside a fixed comparable-ratio region,
$|\phi_{1,y}+\phi_{2,y}|\ge c(|\theta|+|\sigma|)$;
the stated integration by parts in $y$ proves rapid decay with every requested base, frequency and parameter derivative. That contribution is smooth, with uniformly convergent cutoff kernels.

In the retained region put $\chi=1$ on all matches. The exact Jacobian in (E11) gives
\[
 \begin{aligned}
 b&=r^{-n_Y}\chi a_1a_2\in S^q_{\mathrm{cl}},\\
 q&=m_1+m_2+\frac{d-2N}{4}.
 \end{aligned}
 \tag{E12}
\]
Indeed $dy\,d\theta\,d\sigma=r^{-n_Y}d\omega$, the input normalization constants multiply to $(2\pi)^{-(d+2N)/4}$, and $|\theta|\asymp|\sigma|\asymp r\asymp|\omega|$ on these compact base patches. The chain rule proves the entire symbol expansion and all remainders exactly as in (G8), independently of the rank deficit.

Properness on the matching supports gives a finite collection of reduction patches over each compact normalized portion of $C'$. A subordinate smooth partition yields (E8) on each. The complement of their critical neighborhoods has no critical points and is smooth by the frequency estimate in Section 3. If necessary first work in a slightly larger compact normalized output neighborhood: properness makes its closed matching support compact, so no unmatched sequence can escape all these patches while approaching a critical point. The phase reading converts the finitely many resulting phases to any fixed local phase for the embedded image, with all classical remainders. Equations (E9) and (E12) prove (E3).

The resulting distribution is the actual product kernel. Both its cutoff limit and $A_1A_2$ agree on compact smooth inputs by the first paragraph of this section. Equality on product tests implies equality on arbitrary compact tests: Fourier inversion and finite Riemann sums approximate a product-chart test in every derivative by finite sums of product tests, as proved in Section 4 of the transverse reading. Proper localization handles all charts. Smooth discarded kernels stay smooth under either composition by that reading's smooth-family argument. This completes the operator assertion, not merely a formal composition of phases.

<a id="clean-symbol"></a>

## 5. The density carried by a matching fiber

Write $\mathcal D(W)$ for the density line of a real vector space $W$; $\mathcal D(W^*)=\mathcal D(W)^{-1}$. Exact-sequence determinant rules are proved by choosing a kernel basis and lifts of a quotient basis: changing lifts is triangular with diagonal one. They apply also to square roots. Put $E_0=\operatorname{im}D$. The symplectic pairing from Section 1 induces an isomorphism
\[
 \begin{aligned}
 &E/E_0\longrightarrow V^*,\\
 &[z]\longmapsto\bigl[w\mapsto\omega_Y(w,z)\bigr].
 \end{aligned}
 \tag{E13}
\]
It is well defined by (E2); its kernel is zero since the symplectic double orthogonal of $E_0$ is $E_0$, and dimensions are equal. Applying the exact-sequence rules to $TM$, $TM_0$ and $E$ gives
\[
 \begin{aligned}
 \mathcal D(TM)&=\mathcal D(TM_0)\mathcal D(E_0),\\
 \mathcal D(TM_0)&=\pi^*\mathcal D(TC)\mathcal D(V),\\
 \mathcal D(E)&=\mathcal D(E_0)\mathcal D(V^*).
 \end{aligned}
 \tag{E14}
\]
Divide an input product half density by the Liouville half density on $E$, namely $|dy\,d\eta|^{1/2}$. Equations (E13)–(E14) give a canonical bilinear contraction
\[
 \begin{aligned}
 \mu_e:\ &\mathcal D(TC_1)^{1/2}\otimes
             \mathcal D(TC_2)^{1/2}\\
       &\longrightarrow
       \pi^*\mathcal D(TC)^{1/2}\otimes\mathcal D(V).
 \end{aligned}
 \tag{E15}
\]
In particular the result has a full density along the fiber, which can be integrated. Taking only a half density there would be incorrect. Absolute determinants make this construction independent of orientations. Liouville density is invariant because it is the absolute top power of the symplectic form.

<a id="clean-density-coefficient"></a>

We verify the exact coordinate coefficient of (E15). For any clean phase the derivative of its critical equations has the exact sequence
$0\to T\mathcal C\to T(x,\omega)\to(\mathbb R^N)^*\to V^*\to0$.
The last map pairs an equation covector with a frequency vector in $\ker d\kappa$; its kernel is precisely the image of $d(\Phi_\omega)$ by the transpose-nullspace calculation of Section 2. Taking the square root of the ambient density divided by the equation-space density therefore gives a half density on the image times a full fiber density. This is a determinant-line quotient, not division by a vanishing determinant of $N$ supposedly independent equations.

In the reduced coordinates (E6), let $F'=(\psi_\eta,0)$. On the critical set $dF'=D\Theta^T\,d(\Phi_\omega)$. Both the ambient Jacobian and the equation transformation must be included:
$|dx\,d\omega|=J|dx\,d\eta\,dv|$
and the old equation-space density is $J^{-1}$ times the new one. In these adapted bases the $K$ independent equations are $\psi_\eta$, the cokernel pairs with the $v$ directions with matrix identity, and the preceding quotient is
$J^2d_\psi\,|dv|^2$, where
$d_\psi=|dx\,d\eta|/|d(\psi_\eta)|$.
Its square root is $J\sqrt{d_\psi}|dv|$.

Here is also the comparison with the matching quotient, so no normalization is hidden in this calculation. Start with the separate phase variables and take the quotient by their independent critical equations. This produces the product of their critical densities. Adjoin the matching equations and use (E13) for their cokernel. Alternatively eliminate $y_1-y_2$ first, then use the clean critical equations $F$ in (E10). The elimination has determinant one. The identifications of the two cokernels agree in absolute determinant: if $(0,w,w,0)\in V$ has intermediate components $w=(w_y,w_\eta)$ and phase frequency components $h_1,h_2$, differentiating the phase parametrizations gives the relation
\[
 \begin{aligned}
 &h_1\cdot d\phi_{1,\theta}+h_2\cdot d\phi_{2,\sigma}\\
 &\quad+w_\eta\cdot d(y_1-y_2)\\
 &\quad+w_y\cdot d(\phi_{1,y_1}+\phi_{2,y_2})=0.
 \end{aligned}
 \tag{E16}
\]
For example its $dy_1$ coefficient is $-w_\eta+w_\eta=0$ and its $dy_2$ coefficient is $w_\eta-w_\eta=0$; its outer and frequency coefficients vanish because the variation has zero outer covectors and is tangent to both phase critical sets. The matching momentum difference is $-(\phi_{1,y_1}+\phi_{2,y_2})$, so the induced functional is $w_\eta\cdot\delta y-w_y\cdot\delta\eta$, the symplectic pairing up to sign. Thus it is exactly (E13) in absolute density, with no numerical factor.

Finally (E11) multiplies the ambient Jacobian by $r^{n_Y}$ and the inverse equation-space Jacobian by the same factor. This gives $r^{2n_Y}$ before taking the square root, just as in the transverse calculation. Multiplication by $b=r^{-n_Y}a_1a_2$ cancels it. If $\gamma_i=a_{i,\mathrm{lead}}\sqrt{d_{\phi_i}}$, the full result in reduced coordinates is consequently
\[
 \begin{aligned}
 &\mu_e(\gamma_1\otimes\gamma_2)\\
 &\qquad=(b_{\mathrm{lead}}\circ\Theta)J\sqrt{d_\psi}\,|dv|.
 \end{aligned}
 \tag{E17}
\]
Partition factors are inserted on the right when a matching fiber needs several charts; their sum is one there.

<a id="clean-maslov-integration"></a>

## 6. Maslov factors, integration and independence of choices

The programme uses the phase coefficient
$s_\phi=e^{i\pi N_\phi/4}a_{\mathrm{lead}}\sqrt{d_\phi}$.
For the combined phase of dimension $N=N_1+N_2+n_Y$ and its reduction of dimension $K=N-e$, (E8) and (E17) give
\[
 \begin{aligned}
 \sigma(A_1A_2)
 &= (2\pi)^{-e/2}\int_{\pi^{-1}(\lambda)}
                         (s_1\star_e s_2),\\
 s_1\star_e s_2
 &= e^{i\pi(n_Y-e)/4}\mu_e(s_1\otimes s_2).
 \end{aligned}
 \tag{E18}
\]
The second formula is in the paired input-phase frames and the reduced output-phase frame. It includes the induced map into the pullback of the output Maslov line, as checked next; it is not a multiplication of unrelated scalar frames. The integrand takes values in that fixed line at $\lambda$, times its half-density line, and a full density on the fiber.

On the critical set a change of frequency variables makes the frequency Hessian congruent, because terms containing first critical derivatives vanish. In (E6) the new Hessian is the direct sum of $\psi_{\eta\eta}$ and an $e$-dimensional zero block. It therefore has the same signature as $\psi_{\eta\eta}$. Two such reductions of a fixed clean phase have the same reduced frequency dimension and Hessian signature at corresponding points. The phase reading's equivalence theorem and transition formula
$c_{jk}=[(\operatorname{sgn}H_k-N_k)-(\operatorname{sgn}H_j-N_j)]/2$
then give transition one between these reduced phase frames. Their density transformation is exactly the Jacobian computation of Section 5.

A homogeneous input fiber change induces a change of the combined frequency variables, hence congruence of its Hessian. Inserting a nondegenerate quadratic block in either input adds that same block to the combined phase and to its reduced active variables. Its signature and dimension contributions are the same in the input and output, while $e$ remains fixed. Consequently the output transition is the product of the two input transitions. The phase equivalence theorem reduces arbitrary input phase changes to these operations. This proves that (E18) commutes with all Maslov transitions. A different homogenizing scale is a frequency diffeomorphism. Base changes preserve (E15); ordinary changes of the fiber coordinate preserve the full density integral. Thus the construction is intrinsic.

For explicit integration over a possibly nontrivial fiber, trivialize the output line over a small target chart and pull that trivialization back. Cover its compact matching support by finitely many submersion charts with a smooth partition. In each chart the integrand is a scalar smooth function times $|dv|$, with compact support in a fixed $v$ box, so its integral is smooth in the target variables by differentiated compact integration. Coordinate changes give identical values by the already-proved density change of variables; summing the partition removes its choice. This also handles disconnected fibers. After converting the local reduced phases to a common output phase, the same stationary-phase estimates and finite sum prove every lower classical coefficient and remainder. Uniqueness of the recovered principal symbol confirms that the integrated section is the symbol of the actual product established in Section 4.

If $e=0$, fiber integration sums over the discrete matching points. A proper such fiber is finite: an infinite subset of a compact discrete submanifold would accumulate and contradict its local discreteness. For connected fibers there is one point, $(2\pi)^{-e/2}=1$, and (E18) is exactly (G12)–(G13). No extra graph or no-caustic condition appears at positive excess.

<a id="clean-excess-example"></a>

## 7. A positive-excess check and parameter limits

Let $X=Z=\mathbb R$ and $Y=\mathbb R\times W$, with $W$ a compact smooth $e$-manifold carrying a smooth positive density $\nu$. Use compact exterior localizations if desired. On half densities define, in the trivialization by $|dt|^{1/2}\nu^{1/2}$,
\[
 \begin{aligned}
 A_2 f(t,w)&=b(w)f(t),\\
 A_1 g(t)&=\int_W a(w)g(t,w)\,\nu(w),\\
 A_1A_2 f(t)&=\left(\int_W ab\,\nu\right)f(t).
 \end{aligned}
 \tag{E19}
\]
The kernel phases are $(x-t)\theta$ and $(t-z)\sigma$, with one frequency each. On matching, $x=t=z$, $\theta=\sigma\ne0$, and the $W$ momentum is zero. The matching fiber is $W$, so its excess is $e$. Each kernel has amplitude order zero in these phases, hence FIO order $-e/4$, because its base dimension is $2+e$. Formula (E3) gives order zero for the product, as the exact last line of (E19) requires.

Each input normalization in (G1) is $(2\pi)^{-1-e/4}$, so the amplitudes for these actual delta kernels contain $(2\pi)^{e/4}a$ and $(2\pi)^{e/4}b$. Formula (E18) contributes $(2\pi)^{-e/2}$ and cancels their product. After removing the inactive $W$ variables, the two intermediate active variables have a stationary Hessian congruent to $\left(\begin{smallmatrix}0&-1\\-1&0\end{smallmatrix}\right)$; its signature is zero and absolute determinant one. The phase-transition formula therefore reduces the symbol to the identity phase coefficient times $\int_W ab\,\nu$. This checks both the positive order shift and the constants on an actual operator, without treating the example as proof of the general theorem.

All local constructions above are uniform for smooth parameter families with constant excess, uniform clean rank, a common embedded image branch and proper matching support uniformly on compact parameter sets. Apply the inverse and flow arguments with parameters retained; their positive lower bounds persist after shrinking a compact patch, and the finite symbol estimates differentiate as stated. Differentiating a moving phase may increase its operator order, as in the transverse reading. If the clean rank or excess changes, or matching support escapes to infinity, these hypotheses fail and this theorem makes no assertion across that transition. The theorem does cover every fixed excess $e$ and base caustics under the stated clean proper hypotheses.
