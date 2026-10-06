# Transverse composition and graph operators

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="transverse-composition"></a>

This reading proves the classical scalar composition and adjoint rules with transverse matching, including their density and Maslov factors. It then proves the graph Sobolev map, an elliptic graph inverse modulo smooth kernels, and ordered Egorov. These results are treated in [Lars Hörmander, *Fourier integral operators I*, Section 4.2 and the beginning of 4.3](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392052). The arguments follow below. The subsequent [Clean composition with positive excess](clean-composition-with-excess.md#clean-composition) proves the proper clean theorem and its normalized symbol fiber integral. Scalar transport and general wavefront-qualified pullback are supplied by their separate readings linked below.

Read the finite scalar calculus, real Sobolev estimates and cutoff summation in [Classical scalar symbols, Sobolev mapping and elliptic domains](classical-scalar-calculus.md#finite-scalar-calculus), followed by [Phase geometry, stationary phase and the Maslov symbol](phase-geometry-and-stationary-phase.md#phase-foundations). We use its nondegenerate phases, critical densities, phase equivalence, symbol realization/recovery and wavefront estimates. The Fourier and coordinate prerequisites are the actual proofs linked there. Smooth compact partitions and the parameter inverse theorem are therefore available. Kernels act on scalar half densities; on a coordinate product their coefficients are paired bilinearly with test coefficients, while Hilbert adjoints insert conjugation. All orders are real and all symbols are classical $S_{1,0}$ with step-one expansions.

Write $n_X=\dim X$, and similarly for $Y,Z$. A relation from $Y$ to $X$ is a conic Lagrangian $C\subset (T^*X\setminus0)\times(T^*Y\setminus0)$ for the form $\omega_X-\omega_Y$. Its kernel Lagrangian is $C'=\{(x,y;\xi,-\eta):(x,\xi;y,\eta)\in C\}$. Both covector components are nonzero. Global assertions use the closed-support convention of the phase reading: $C'$ is closed in $T^*(X\times Y)\setminus0$, or the actual critical supports lie in a conic subset of $C'$ closed in that ambient space. Thus those supports have no limit with exactly one covector component zero. Over compact base sets their normalized portions are compact; the two component norms consequently have positive lower bounds there. Local assertions retain the compact phase supports specified below and require no global closedness of $C$. For a phase with $N$ frequency variables our fixed normalization is
\[
 K_A(x,y)=(2\pi)^{-(n_X+n_Y+2N)/4}
       \int e^{i\phi(x,y,\theta)}a(x,y,\theta)\,d\theta\,
                 |dx\,dy|^{1/2},
 \quad a\in S^{m+(n_X+n_Y-2N)/4}_{1,0}.
 \tag{G1}
\]
Low frequencies are cut off. Phase supports are closed inside their patches and compact after compact base localization and frequency normalization. Proper support means that each projection of the kernel support to one base manifold is proper. Local statements use fixed nested compact cutoffs; global statements below require the stated properness on the actual supports.

## 1. Smooth inputs, distributional actions and cutoff limits

Near the critical set of an operator phase, both $|\phi_x|/|\theta|$ and $|\phi_y|/|\theta|$ have positive lower bounds on a compact normalized support. Shrink to such a neighborhood. Its omitted part has smooth kernel by the frequency integration-by-parts proof in the phase reading. On the retained part put
\[
 L_y=\frac{\phi_y\cdot\partial_y}{i|\phi_y|^2},
 \qquad L_y e^{i\phi}=e^{i\phi}.
 \tag{G2}
\]
Every $y$ derivative of its coefficients is $O(|\theta|^{-1})$. In $A u$, with $u$ compact smooth, transfer $L_y$ any prescribed number of times. Each transfer lowers the frequency growth by one and uses only finitely many derivatives of $u$ and the amplitude. Each fixed output derivative costs only a fixed power of $|\theta|$. After enough transfers the integral and all requested output derivatives converge absolutely. The intermediate base supports are compact by properness. Thus $A:C_c^\infty(Y)\to C^\infty(X)$ is continuous in these actual seminorms. Its transpose has the same property, using $\phi_x$; proper support makes the transposed image of a compact test compact. Hence
$\langle Au,v\rangle=\langle u,A^t v\rangle$
defines a continuous action on distributions, agreeing with the smooth action. Local versions follow with compact supports and the appropriate output restriction.

Insert a smooth cutoff $\chi(\varepsilon\theta)$ equal to one near zero. The resulting $A_\varepsilon$ converges to $A$ in each of the preceding smooth-output seminorm estimates on bounded sets of smooth inputs. Indeed the difference is supported at $|\theta|\gtrsim\varepsilon^{-1}$; arbitrarily many transfers in (G2) make its integral $O(\varepsilon^M)$ for any requested $M$, after choosing enough input derivatives. The cutoffs have uniformly bounded order-zero symbol seminorms. The same reasoning applies to transposes. In particular
$A_{1,\varepsilon}A_{2,\varepsilon}u\to A_1A_2u$
smoothly for every compact smooth $u$: split the difference into $A_{1,\varepsilon}(A_{2,\varepsilon}-A_2)u+(A_{1,\varepsilon}-A_1)A_2u$ and use these estimates and their common compact support.

A properly supported smooth kernel remains smooth when composed on either side with $A$. On one side apply $A$ to the smooth family of its input-variable slices; continuity in every smooth seminorm permits differentiation in the other variable. On the other side use the transpose. This proves that the discarded smooth terms are harmless in the later composition, without assuming an unproved Sobolev estimate for an FIO.

## 2. The exact matching hypothesis

For $C_1:Y\to X$ and $C_2:Z\to Y$, let $M=C_1\times C_2$ and let $M_0$ consist of pairs whose intermediate covectors coincide. The hypothesis is that the differential of the difference of those two intermediate covectors, in cotangent coordinates on $Y$, maps $T M$ onto the full $2n_Y$-dimensional normal space to the diagonal. This is **transverse matching**. It makes $M_0$ a smooth manifold of dimension $n_X+n_Z$ by the parameter inverse theorem. Let
\[
 \pi:M_0\longrightarrow T^*X\times T^*Z,
 \qquad ((x,\xi;y,\eta),(y,\eta;z,\zeta))
                     \longmapsto(x,\xi;z,\zeta).
 \tag{G3}
\]
Assume that this projection is injective and proper on the portion under consideration. This is the unique-matching, excess-zero case; no assertion about positive-dimensional matching fibers is being used.

Here is why $C=\pi(M_0)$ is a Lagrangian and has no hidden immersion kernel. The product $M$ is Lagrangian for $\Omega=\omega_X-\omega_{Y_1}+\omega_{Y_2}-\omega_Z$. A vector in $\ker d\pi\subset T M_0$ has the form $(0,w,w,0)$. Its pairing under $\Omega$ with any vector of $T M$ is minus the symplectic pairing of $w$ with the difference of the two intermediate components. This is zero because both vectors lie in the Lagrangian $T M$. Surjectivity of that difference map, and nondegeneracy of the symplectic form, force $w=0$. Thus $\pi$ is an immersion. On $T M_0$ the two intermediate forms cancel, so $\omega_X-\omega_Z$ vanishes on its image. The dimension is exactly half the ambient dimension; hence it is Lagrangian. Local invertibility onto the image, injectivity and properness make the image embedded: a sequence of extraneous branches approaching a point would, by properness over a compact target neighborhood, have a convergent subsequence to another preimage, contradicting the local immersion chart and injectivity. Positive simultaneous dilation preserves all the equations, so the relation is conic.

For two canonical graphs, the derivative condition follows immediately by varying the intermediate covector on the first graph: its projection to $T^*Y$ is a local diffeomorphism. The input covector on the second graph determines its output and then the first output, so matching is unique. Properness must still be checked on the actual supports; it holds for the closed-manifold global graphs and for the properly localized patches used here. This argument places no restriction on the rank of the projection of a graph to its pair of base manifolds, and therefore permits base caustics.

## 3. A nondegenerate homogeneous phase for the product

Choose phases $\phi_1(x,y,\theta)$ and $\phi_2(y,z,\sigma)$ with $N_1,N_2$ variables. With separate copies $y_1,y_2$, their two critical sets are cut out by independent equations $(\phi_{1,\theta},\phi_{2,\sigma})=0$. On that manifold, the matching equations are
$y_1-y_2=0$ and $\phi_{1,y_1}+\phi_{2,y_2}=0$.
Transversality therefore says that the differentials of all these equations together are independent. Eliminating $y_1-y_2$ by the coordinate change $(y_1,y_2)\mapsto(y_1-y_2,y_2)$, of determinant one, shows that
\[
 F=(\phi_{1,\theta},\phi_{2,\sigma},\phi_{1,y}+\phi_{2,y})
 \quad\hbox{has rank }N_1+N_2+n_Y\quad\hbox{on }F=0.
 \tag{G4}
\]
All derivatives here include the exterior variables $x,z$.

Put $r=(|\theta|^2+|\sigma|^2)^{1/2}$ and introduce
\[
 \omega=(ry,\theta,\sigma),\qquad N=N_1+N_2+n_Y,
 \qquad \Phi(x,z,\omega)=\phi_1(x,y,\theta)+\phi_2(y,z,\sigma).
 \tag{G5}
\]
This is a homogeneous change of fiber coordinates on the indicated cone; its inverse is $y=\omega_y/r$. Its Jacobian gives
$dy\,d\theta\,d\sigma=r^{-n_Y}d\omega$.
The new phase is homogeneous of degree one. Its fiber derivative is an invertible transpose-Jacobian multiple of the equations in (G4), reordered as $(\Phi_y,\Phi_\theta,\Phi_\sigma)$. At their common zero, differentiating that relation gives the same invertible multiple of $dF$. Thus (G4) proves that $\Phi$ is nondegenerate. Its exterior derivatives are $(\phi_{1,x},\phi_{2,z})$, which are nonzero in their respective components at a match. Its critical set parametrizes exactly $C'$ by (G3).

## 4. Incomparable frequencies and the actual kernel product

Write $q_i=m_i+(n_{\rm output}+n_{\rm input}-2N_i)/4$ for the two amplitude orders. By Section 1 we may restrict their supports so that
$c_1|\theta|\le|\phi_{1,y}|\le C_1|\theta|$
and
$c_2|\sigma|\le|\phi_{2,y}|\le C_2|\sigma|$.
Cancellation of these two gradients is possible only when
$c_2/C_1\le |\theta|/|\sigma|\le C_2/c_1$.
Choose a degree-zero cutoff $\chi(\theta,\sigma)$ equal to one on a slightly larger ratio interval and supported in a still larger finite positive ratio interval. Choose the margins by factors at least two. On its complement the triangle inequality then gives
\[
 |\phi_{1,y}+\phi_{2,y}|\ge c(|\theta|+|\sigma|).
 \tag{G6}
\]
All amplitudes vanish near their individual zero sections. Apply (G2) with this summed gradient to the $y$ integral of $(1-\chi)a_1a_2$. If $R=|\theta|+|\sigma|$, every $y$ derivative of its coefficients is $O(R^{-1})$, and the original amplitudes have at most fixed polynomial growth in $R$, also after any fixed derivatives. Derivatives in $x,z,\theta,\sigma$ or external parameters of the exponential and coefficients cost only another fixed power of $R$ on these supports. Transferring sufficiently many times therefore proves
\[
 \left|\partial_{x,z}^{\alpha}\partial_{\theta,\sigma}^{\beta}
       \int e^{i(\phi_1+\phi_2)}(1-\chi)a_1a_2\,dy\right|
       \le C_{\alpha\beta L}(1+R)^{-L}
       \quad\hbox{for every }L.
 \tag{G7}
\]
The compact $y$ support and absence of boundary terms follow from localization. This estimate gives a smooth kernel after integrating both frequencies, including every base and parameter derivative. It also dominates the cutoff versions uniformly and proves their convergence.

In the retained region $|\theta|\asymp|\sigma|\asymp r$. Thus a derivative in either frequency lowers the joint order by one. After (G5) the amplitude is
\[
 b(x,z,\omega)=r^{-n_Y}\chi(\theta,\sigma)
                         a_1(x,y,\theta)a_2(y,z,\sigma)
 \in S^{q_1+q_2-n_Y}_{1,0},
 \quad q_1+q_2-n_Y=m_1+m_2+\frac{n_X+n_Z-2N}{4}.
 \tag{G8}
\]
Indeed a derivative of $y=\omega_y/r$ costs $r^{-1}$ on bounded $y$ supports, and $r\asymp|\omega|$ there. The chain and product rules prove every displayed symbol estimate, including all smooth parameter derivatives and homogeneous coefficients. Multiplying the two normalization constants in (G1) gives exactly $(2\pi)^{-(n_X+n_Z+2N)/4}$. There is no extra power of $2\pi$.

The phase-kernel distribution proof now defines the retained integral with phase $\Phi$ and amplitude $b$. Cutoff limits agree with the double-frequency cutoffs, because both are bounded order-zero symbols tending to one, and the integration-by-parts estimates in that proof make their tails vanish after any fixed test. Together with (G7) this gives a distributional limit of the cutoff kernel products. Section 1 proves that this limit acts as $A_1A_2$ on smooth inputs. Equality as kernels follows from equality on product tests: such tests span a dense subspace of the compact test space on a product chart. To verify that density directly, write a compact smooth product-chart test by Fourier inversion, truncate its rapidly decreasing Fourier transform, approximate the finite Fourier integral and its finitely many derivatives by finite Riemann sums, and multiply each separate factor by fixed compact cutoffs equal to one on the original support. A diagonal choice over derivative orders gives convergence in the full test topology. Each approximant is a finite sum of product tests. Distributional continuity proves the claimed kernel equality.

Compact localization and proper matching allow finitely many of these charts over each compact normalized portion of the composed relation. Contributions outside their critical neighborhoods are smooth by the phase reading's frequency argument. Smooth terms stay smooth under composition by Section 1. We have therefore proved
\[
 A_1A_2\in I^{m_1+m_2}_{\rm cl}(X\times Z,(C_1\circ C_2)').
 \tag{G9}
\]
This is an equality for the actual operator product, with a classical amplitude and every finite remainder supplied by (G7), (G8) and the earlier phase-equivalence/stationary-phase proofs.

<a id="density-contraction"></a>

## 5. The density contraction, including the Jacobian

For an exact sequence of finite-dimensional real spaces $0\to E_0\to E\to E_1\to0$, a density on $E$ divided by a density on $E_1$ defines one on $E_0$. Choose a basis of $E_0$ and lift a basis of $E_1$; another choice of lifts is triangular with diagonal one, so the determinant rule proves independence. The same proof gives square-root densities. For a submersion with coordinates $(u,F)$ the quotient is the reciprocal absolute Jacobian times $|du|$. Taking successive quotients agrees with taking their joint quotient: choose coordinates $(u,F_1,F_2)$ and multiply the triangular Jacobians. These statements supply the density operations used next.

On $M_0$, divide the product of the two critical densities by the density of the matching equations $(y_1-y_2,\eta_1-\eta_2)$. This normal density is intrinsic: in cotangent coordinates it is $|dy\,d\eta|$, preserved by a canonical change of coordinates. To see the latter assertion, the top exterior power $\omega_Y^{n_Y}/n_Y!$ has absolute value $|dy\,d\eta|$; a symplectic derivative preserves that top form. The same derivative acts on the difference normal space at the diagonal. The quotient therefore does not depend on the chosen cotangent coordinates. Take the square root and transfer it through the diffeomorphism (G3). Denote this bilinear half-density contraction by $\mu_D$.

Let $d_F=|dx\,dz\,dy\,d\theta\,d\sigma|/|dF|$ on the set (G4). Successive quotienting first by the two phase critical equations and then by matching, or first by $y_1-y_2$ and then by (G4), gives the same density. Consequently
\[
 \mu_D(\sqrt{d_{\phi_1}}\otimes\sqrt{d_{\phi_2}})=\sqrt{d_F}.
 \tag{G10}
\]
The homogenization must still be included. Its ambient density multiplies by $r^{n_Y}$. On the critical set $d\Phi_\omega=(D_\omega(y,\theta,\sigma))^T dF$, up to a permutation, and this matrix has determinant of absolute value $r^{-n_Y}$. Write $\gamma_i=a_{i,q_i}\sqrt{d_{\phi_i}}$ and $b_{\rm lead}=b_{q_1+q_2-n_Y}$. Thus
\[
 \begin{aligned}
 d_\Phi&=r^{2n_Y}d_F,\\
 b_{\rm lead}\sqrt{d_\Phi}&=\mu_D(\gamma_1\otimes\gamma_2).
 \end{aligned}
 \tag{G11}
\]
The cutoff is one at matching points. Both powers of $r$ are essential: one comes from the ambient variables and the other from the critical equations.

For graphs, identify their half densities by the Liouville half density on their input cotangent space. In input coordinates $v\in T^*Y$ for the first graph and $w\in T^*Z$ for the second, matching is $v=\chi_2(w)$. The change $(v,w)\mapsto(v-\chi_2(w),w)$ is triangular with determinant one. Dividing $|dv\,dw|$ by the matching density leaves $|dw|$. Hence graph density contraction multiplies the scalar coefficients after evaluation at the matched point.

<a id="maslov-contraction"></a>

## 6. Maslov contraction in the fixed normalization

The phase reading defines the coefficient of the principal section by
$s_i=e^{i\pi N_i/4}a_{i,q_i}\sqrt{d_{\phi_i}}$,
with transition $s_j=i^{c_{jk}}s_k$. In the combined phase frame (G5), define the line-and-density product by
\[
 s_1\star s_2=e^{i\pi n_Y/4}\mu_D(s_1\otimes s_2).
 \tag{G12}
\]
The factor is part of this unshifted convention: the combined frequency dimension is $N_1+N_2+n_Y$. Equations (G8) and (G11) immediately give
\[
 \sigma(A_1A_2)=s_1\star s_2.
 \tag{G13}
\]
Omitting the factor in (G12) while retaining the earlier definition of $s_i$ would give the wrong phase.

Here is a proof that (G12) defines an intrinsic line map. A homogeneous fiber change of either input phase induces a homogeneous change of the combined phase variables in (G5); the critical frequency Hessians are congruent. Inserting a quadratic block in one input phase inserts the same block into the combined frequency Hessian, with its same signature: cross derivatives with the inserted variables vanish on their zero critical set, and the positive homogeneous scale does not change the signature. Thus the change in the combined Hessian signature is the sum of the changes in the two input signatures. The change in the combined frequency dimension is likewise their sum. The phase reading's full equivalence theorem reduces every phase change to these two operations. It follows that the combined transition exponent is the sum of the input transition exponents. Therefore (G12) commutes with every transition $i^{c_{jk}}$. It also commutes with base changes by (G10)–(G11). Choosing another positive homogeneous scale in (G5) is just a fiber diffeomorphism. This proves independence of all these choices.

The identity section is the actual identity-kernel section from the phase reading. It is the unit for (G12). One can check the constants directly: composing an identity phase with another phase introduces the variables $(y,\theta)$ with stationary Hessian congruent to
$\left(\begin{smallmatrix}0&-I\\-I&0\end{smallmatrix}\right)$,
of signature zero and absolute determinant one. For a block $\left(\begin{smallmatrix}H&-I\\-I&0\end{smallmatrix}\right)$ the change $v\mapsto v-Hu/2$ gives that form; its positive and negative indices are both $n_Y$. Eliminating these $2n_Y$ variables produces no Gaussian signature factor, and the phase-reading transition cancels the $i^{n_Y}$ from the identity coefficient and (G12). The remaining coefficient is exactly the original one. Equivalently Fourier inversion gives $IA=AI=A$, and (G13) and principal-symbol recovery give the same unit identity. Associativity also follows without an extra line convention: realize any three principal sections by operators using the earlier realization proof, use associativity of their actual smooth-input products, and recover the symbol. The result is independent of the realizations because an order-lower change in one factor is order-lower in (G9).

<a id="graph-adjoints"></a>

## 7. Adjoints, including the phase-frame factor

The actual adjoint kernel is $K_{A^*}(y,x)=\overline{K_A(x,y)}$. In (G1) it has phase $-\phi(x,y,\theta)$, reordered base variables, and amplitude $\overline a$. The critical density is unchanged by the base permutation and by changing signs of the critical equations. Its relation is the inverse relation, and its order is still $m$. Thus
\[
 A^*\in I^m_{\rm cl}(Y\times X,(C^{-1})'),\qquad
 s_{A^*}=i^N\overline{s_A}
 \quad\hbox{in the paired }-\phi,\phi\hbox{ frames}.
 \tag{G14}
\]
This follows by substituting $s_A=e^{i\pi N/4}a_q\sqrt{d_\phi}$; the desired new coefficient is $e^{i\pi N/4}\overline{a_q}\sqrt{d_\phi}$. It is not just bare conjugation in those particular rephased frames. The intrinsic map is an anti-linear isometry: all factors have modulus one. To check gluing, let $c_{jk}$ be the old transition exponent and $c^*_{jk}$ that of the negative phases. Replacing each Hessian signature by its negative in the definition gives
$c^*_{jk}=-c_{jk}+N_j-N_k$.
This is precisely the transition of $i^{N_j}\overline{s_j}$. It proves the well-defined adjoint line operation. On the identity graph it sends the identity-normalized scalar symbol $a$ to $\overline a$, as required. Section 1 justifies the Hilbert pairing identity on compact smooth inputs before any bounded extension is invoked.

<a id="graph-sobolev"></a>

## 8. Every real graph Sobolev shift

Suppose $X,Y$ have the same dimension and $C$ is the graph of a homogeneous canonical diffeomorphism. Then
\[
 A:H^s_{\rm comp}(Y)\longrightarrow H^{s-m}_{\rm loc}(X)
       \quad(s,m\in\mathbb R).
 \tag{G15}
\]
To prove it, first give $A$ compact coordinate input and output supports. Set $B=J^{s-m}AJ^{-s}$, where $J^t=\langle D\rangle^t$. Replace the two Fourier multipliers near these supports by properly localized pseudodifferential kernels. Their omitted tails have all derivatives rapidly decreasing off the diagonal, as proved in the scalar Sobolev section. Composing these tails with a compactly localized FIO gives a smooth Schwartz kernel: apply the smooth-input estimates of Section 1 to each tail slice, retaining its arbitrarily rapid decay in the free variable; for the other side use the transpose. Every weighted two-frequency Fourier norm of that kernel is finite by integration by parts, and Fourier Cauchy–Schwarz gives boundedness between any prescribed Sobolev spaces. Thus these tails cause no gap in using the proper calculus on the main term.

Equations (G9) and (G14) make the main $B$ an order-zero graph FIO and $B^*B$ an order-zero FIO on the identity graph. That last class is the scalar pseudodifferential class: the identity phase is $(x-y)\cdot\eta$, and the phase-equivalence theorem converts any local phase for the identity to it with the corresponding classical amplitude; finite scalar amplitude reduction then gives an ordinary left symbol of order zero, modulo a smooth kernel. The earlier finite-derivative theorem therefore makes $B^*B$ bounded on $L^2$. On compact smooth inputs, whose images are smooth by Section 1,
\[
 \|Bu\|_2^2=(B^*Bu,u)
       \le \|B^*B\|_{2\to2}\|u\|_2^2.
 \tag{G16}
\]
Density gives a bounded extension of $B$, proving (G15), including the tails. The extension agrees with its distributional action: the smooth approximations converge as distributions, and the transpose action of Section 1 is continuous. The finite-atlas localization/reassembly proof in the scalar reading gives the closed-manifold version. Finite graph charts cover each compact normalized support; nowhere was a noncaustic base projection required.

These bounds are locally uniform for smooth parameter families with uniform phase nondegeneracy, matching transversality and symbol seminorm bounds. For any requested finite bound, the preceding operations use only finitely many derivatives and positive lower bounds on compact normalized sets. Parameter derivatives of the amplitudes and stationary remainders remain in their displayed symbol orders. Differentiating the full kernel $k$ times can also differentiate its phase and may raise the operator order by $k$; in general its differentiated map is therefore $H^s\to H^{s-m-k}$. No stronger derivative bound is implied merely by uniform order-$m$ bounds of the undifferentiated family.

<a id="graph-egorov"></a>

## 9. Elliptic inverse and ordered Egorov

For completeness the graph inverse follows from the proved rules. Suppose a properly supported graph FIO $A$ is elliptic on the portion considered, meaning that its principal section is nowhere zero there. At a matched inverse graph point, (G12) is a nondegenerate pairing of one-dimensional lines and density factors. There is therefore a unique inverse principal section $b$ with $b\star\sigma(A)$ equal to the identity section. It has order $-m$. Realize it by a classical inverse-graph FIO $B_0$, using the phase reading. Then $B_0A$ is an elliptic scalar order-zero operator with principal symbol one. Its scalar parametrix $Q$, proved in (FC17), gives $B=QB_0$ with $BA-I$ smooth. Construct a right inverse $D$ in the same manner. The identity
$B-D=B(I-AD)+(BA-I)D$
and Section 1 show that $B-D$ is smooth. Hence $AB-I$ is also smooth. This argument applies globally to a globally elliptic graph between closed manifolds, and microlocally with nested cutoffs on an elliptic patch; the remainders there are smooth on the specified smaller patch, not a claim of a global inverse for an operator elliptic only locally. Actual invertibility is not asserted.

Let now $E$ be a unitary elliptic order-zero graph FIO with graph $\chi:T^*X\setminus0\to T^*X\setminus0$, and let $V$ be scalar classical of order $r$. Then
\[
 E^*VE\in\Psi^r_{\rm cl},\qquad
 \sigma_r(E^*VE)(z)=v_r(\chi z).
 \tag{G17}
\]
The composed graph is the identity by (G3). Multiplication by the scalar principal symbol of $V$ evaluates it at the intermediate output covector $\chi z$; this follows from (G11)–(G13) and the identity frame. The remaining line and density factors are exactly those for $E^*E$. They multiply to one because the actual operator $E^*E=I$ and the principal symbol is recovered uniquely. This proves both the value and its orientation. In particular $E(t)=e^{-itL}$ gives $e^{itL}Ve^{-itL}$ with symbol $v_r\circ\chi_t$.

For smooth parameter families, the composed relation in this application is the fixed identity graph. The parameter phase-equivalence and stationary-phase proofs reduce the composition to the same fixed identity phase, with a classical amplitude whose every parameter derivative has the same symbol order $r$. There is then no parameter derivative of the reduced phase. Finite amplitude reduction and the proved parameter cutoff summation give all lower terms and their differentiated finite remainders. This justifies the smooth symbol family used in time averages; it is stronger than differentiating an arbitrary moving-graph kernel and follows here from the fixed final graph. The wave construction uses the separate [scalar-transport proof](scalar-transport-and-phase-action.md#scalar-transport) and [qualified-pullback proof](wavefront-qualified-pullback.md#qualified-pullback). 

<a id="joint-parameters"></a>

## 10. A parameter as an additional base variable

Suppose a smooth family of the preceding kernels has parameter $t\in\mathbb R^p$ and fixed-time order $m$. Its phase $\phi(t,x,y,\theta)$ is also a nondegenerate phase on the joint base $(t,x,y)$: the independent critical-equation differentials in $(x,y,\theta)$ remain independent when the $t$ directions are added, and its nonzero spatial covectors prevent a zero total covector. The amplitude still has order $q=m+(n_X+n_Y-2N)/4$. The normalization constant in (G1) is smaller by $(2\pi)^{-p/4}$ for the larger joint base, so the actual joint amplitude is $(2\pi)^{p/4}a$. Multiplication by the fixed parameter half density $|dt|^{1/2}$ therefore gives
\[
 K(t,x,y)|dt|^{1/2}\in I^{m-p/4}_{\rm cl},\qquad
 \Lambda=\{(t,x,y;\phi_t,\phi_x,\phi_y):\phi_\theta=0\}.
 \tag{G18}
\]
This order follows by equating $q$ to $(m-p/4)+(p+n_X+n_Y-2N)/4$. The critical density on the joint critical set is $|dt|d_{\phi(t)}$: quotient by the critical equations in coordinates retaining $t$, whose Jacobian is triangular. Consequently its principal section is $(2\pi)^{p/4}|dt|^{1/2}\sigma(A_t)$ in the matched phase frames. Recovering the fixed-time section removes both this constant and the parameter half density. All distributional estimates hold jointly by the uniform parameter estimates already proved. For a parameter-dependent product, the combined phase (G5) has parameter derivative $\phi_{1,t}+\phi_{2,t}$ on its critical set; derivatives of an alternative fiber coordinate add terms proportional to its vanishing critical equations. Thus its joint parameter covector is that sum, invariantly. With one time parameter and order-zero graphs the joint order is $-1/4$, and its joint symbol contains the factor $(2\pi)^{1/4}$. These conclusions concern the explicit smooth families constructed here. The general wavefront criterion for pulling back an arbitrary distribution to a time slice remains a separate proof.
