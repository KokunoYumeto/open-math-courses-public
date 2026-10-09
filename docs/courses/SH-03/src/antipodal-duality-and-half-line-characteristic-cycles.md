# Antipodal duality and half-line characteristic cycles

Verdier duality exchanges a closed boundary with an open one. Its characteristic cycle records that exchange by reversing the cotangent covector. The reversal acts on the orientation coefficient as well as the carrier. We construct this operation, prove compatibility with the actual identity and evaluated trace, and calculate the four half-lines with their boundary conservation law.

[Characteristic cycles from supported microlocal identities](characteristic-cycles-from-supported-microlocal-identities.md#the-coefficient-and-the-supported-identity) constructs the kernel unit and supported evaluation. The [factor-exchange comparison](natural-duality-for-specialization-and-microlocal-hom.md#factor-exchange-reverses-the-dual-inputs) supplies the natural internal-Hom reversal and the actual diagonal deformation map. We use [evaluation biduality](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#the-evaluation-map-is-biduality) for constructible perfect coefficients and the [external evaluation map](natural-duality-for-specialization-and-microlocal-hom.md#the-cotangent-dual-has-one-base-dualizing-factor), retaining their adjunctions and graded symmetry. [Integer coefficients and additive characteristic cycles](integer-coefficients-and-additive-characteristic-cycles.md) supplies the integral comparison and additivity. The [ordered relative dualizing coefficient](lagrangian-cycles-and-proper-cotangent-images.md#the-orientation-coefficient-fixes-the-dimension), [graph zero-section normalization](transverse-pullback-of-normalized-conormal-cycles.md#a-supported-point-unit-survives-every-tangential-rank), and [constant-coefficient calculation](transporting-characteristic-cycles-through-a-graph.md#globally-constant-finite-coefficients-fix-conormal-normalization) fix the cycle generators used below. These are the precise programme inputs; the proofs here check the antipodal action and its compatibility with those particular maps.

Let \(X\) be a finite-dimensional real analytic manifold, Hausdorff and countable at infinity. The geometric cycle operation below works over a commutative ring \(A\) of finite global dimension. For characteristic cycles, assume that \(k\) is a field of characteristic zero and \(F\in D^b_{\mathbb R\text{-}c}(k_X)\), including finite perfect stalks. Work on a component of dimension \(n\).

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

## An involution of supported cycles

Put \(T=T^*X\), \(\pi:T\to X\), \(E=\pi^{-1}\omega_X\), and

\[
a:T\longrightarrow T,\qquad a(x;\xi)=(x;-\xi).
\qquad\text{(1)}
\]

This is a proper analytic diffeomorphism, with \(a^2=1\) and \(\pi a=\pi\). It commutes with positive fibre scaling. Its pullback sends the canonical one-form to its negative, and hence \(a^*\omega=-\omega\) for \(\omega=d\theta\). Thus a closed conic subanalytic isotropic carrier \(\Lambda\) is carried to another such carrier \(a\Lambda\): the canonical-form condition and the dimension bound are preserved. Properness here follows directly from the continuous inverse, without any compactness of \(X\).

The equality \(\pi a=\pi\) gives the particular coefficient identification \(a^{-1}E=E\). Diffeomorphism base change for closed support therefore gives

\[
a^{-1}R\Gamma_\Lambda(E)
\simeq R\Gamma_{a\Lambda}(a^{-1}E)
\simeq R\Gamma_{a\Lambda}(E).
\qquad\text{(2)}
\]

These maps commute with enlargement of closed support. Taking degree zero and the directed colimit over allowed carriers constructs

\[
a_*:a^{-1}\mathcal L_X\longrightarrow\mathcal L_X,
\qquad \lambda^a=a_*(a^{-1}\lambda).
\qquad\text{(3)}
\]

The second expression denotes the resulting section when \(\lambda\) is a global cycle; locally it is transported from the corresponding inverse open set. Applying (2) twice is the identity by diffeomorphism coherence, so \((\lambda^a)^a=\lambda\). The map respects integral coefficients and frontier boundaries, because both arise from the same support and dualizing maps. It is an operation on cotangent cycles; it is not a direct image for a map between the base manifolds.

## The conormal sign is the base submanifold dimension

For an embedded analytic submanifold \(Z\subset X\), with \(m=\dim Z\), the normalized conormal cycle satisfies

\[
[T_Z^*X]^a=(-1)^m[T_Z^*X].
\qquad\text{(4)}
\]

The brackets retain their graph normalization: on an \(m\)-dimensional manifold the zero-section class is \((-1)^m\) times the positive fibre point trace, and a closed embedding transports this class by its actual closed trace. In a chart where \(Z\) is closed, accordingly, \(CC(k_Z)=(-1)^m[T_Z^*X]\). The eigenvalue in (4) concerns the action on this fixed generator; multiplying a generator by a constant sign does not change that eigenvalue.

This statement is local if \(Z\) is not closed in the chosen ambient chart. To prove it, use adapted coordinates \((u,v;\alpha,\beta)\), where \(u\in\mathbb R^m\), \(v\in\mathbb R^{n-m}\), and \(Z=\{v=0\}\). Its conormal has equations \(v=\alpha=0\), with free \((u,\beta)\). Normal directions to that conormal in \(T\) are \((v,\alpha)\). The antipode fixes \(v\) and negates the \(m\) coordinates \(\alpha\), so it has normal determinant sign \((-1)^m\). The supported coefficient of a normalized smooth conormal is its normal Thom class tensored with \(E\). The base coefficient is fixed by \(\pi a=\pi\), and the normal Thom class changes by exactly this determinant sign. This proves (4).

The same calculation explains the relative orientation factors in the cycle description. On the conormal, the tangent determinant is \((-1)^{n-m}\), from negating \(\beta\). On \(T\), it is \((-1)^n\), from negating all cotangent directions. Their quotient, governing \(\omega_{T_Z^*X/T}\), is \((-1)^{n-m-n}=(-1)^m\). Equivalently, in the \(n\)-cycle description with \(B=\operatorname{or}_{T/X}\), the tangent sign \((-1)^{n-m}\) multiplies the fibre-coefficient sign \((-1)^n\). Counting only the tangent conormal or only the ambient determinant would give the wrong answer. The calculation uses local orientation lines and glues on nonorientable manifolds. In particular, the zero section has sign \((-1)^n\), while a full cotangent fibre has sign \(+1\).

## The swapped kernel carries the identity to the dual identity

Let \(\delta:X\to X^2\) be the diagonal and \(\sigma(x_1,x_2)=(x_2,x_1)\). Write

\[
K_F=F\boxtimes D_XF,\qquad
u_F:k_{\Delta_X}\to K_F,\qquad
v_F:K_F\to\delta_*\omega_X.
\qquad\text{(5)}
\]

Here \(u_F\) is the mate of \(\mathrm{id}_F\) under exceptional diagonal restriction and the actual external-Hom comparison. The map \(v_F\) is ordinary diagonal restriction followed by the graded evaluation
\(t_F:F\otimes D_XF\to\omega_X\). These are the particular maps used to define \(CC(F)\).

Put \(b_F:F\to D_XD_XF\) for evaluation biduality, an isomorphism for the stated constructible input. The factor exchange and this map give

\[
c_F:\sigma^{-1}K_F
=D_XF\boxtimes F
\xrightarrow{\ 1\boxtimes b_F\ }
D_XF\boxtimes D_XD_XF=K_{D_XF}.
\qquad\text{(6)}
\]

The factor-exchange identification includes the graded symmetry. We claim the actual two squares commute:

\[
c_F\,\sigma^{-1}u_F=u_{D_XF},\qquad
v_{D_XF}\,c_F=\sigma^{-1}v_F,
\qquad\text{(7)}
\]

using \(\sigma^{-1}k_\Delta=k_\Delta\) and \(\sigma^{-1}\delta_*\omega_X=\delta_*\omega_X\).

For the first equality, apply exceptional diagonal adjunction to (6), with the canonical diffeomorphism comparison \(\delta^!\sigma^{-1}\simeq\delta^!\). Under the external-Hom comparison its induced map is the contravariant duality transpose of endomorphisms. This is exactly the natural internal-Hom reversal proved in the factor-exchange lesson, before applying microlocalization. Its mate sends \(u:F\to F\) to \(D_Xu:D_XF\to D_XF\); the coherent bidual map identifies its twice-transposed inputs. Thus it sends \(\mathrm{id}_F\) to \(\mathrm{id}_{D_XF}\), proving the first equality. The exceptional projection and its orientation are part of these adjunctions; replacing them by ordinary diagonal restriction would not prove the assertion.

For the second equality, ordinary restriction commutes with \(\sigma\), and \(\sigma\delta=\delta\). It remains to check the evaluated coefficient map. Write \(\operatorname{ev}_F:D_XF\otimes F\to\omega_X\), and let \(s\) denote the graded symmetry. The bidual map is the mate of right evaluation, so its defining identity is

\[
\operatorname{ev}_{D_XF}(b_F\otimes1)
=\operatorname{ev}_F\,s_{F,D_XF}=t_F.
\qquad\text{(8)}
\]

Naturality and involutivity of \(s\) now give

\[
\begin{aligned}
t_{D_XF}(1\otimes b_F)s_{F,D_XF}
&=\operatorname{ev}_{D_XF}
 s_{D_XF,D_XD_XF}(1\otimes b_F)s_{F,D_XF}\\
&=\operatorname{ev}_{D_XF}(b_F\otimes1)
 s_{D_XF,F}s_{F,D_XF}=t_F.
\end{aligned}
\qquad\text{(9)}
\]

This is the ordinary-diagonal restriction of the second square in (7); pushing along \(\delta\) proves that square. The graded symmetry and the actual bidual evaluation occur together. Neither can be replaced by an ungraded vector-space swap.

There is a useful finite-complex sign check. At a point, the identity tensor of a finite complex \(P\) is \(\sum e_r\otimes e_r^*\), with \(|e_r|=r\), \(|e_r^*|=-r\). The swap contributes \((-1)^r\), and the canonical cochain bidual map sends \(e_r\) to \((-1)^r e_r^{**}\). Their product carries the tensor to \(\sum e_r^*\otimes e_r^{**}\), the identity tensor of \(P^\vee\). Each right evaluation contributes \((-1)^r\), so both traces agree. This checks (7)–(9) without removing odd cohomological degrees; it is not a replacement for the sheaf adjunction argument.

## Microlocalization retains the coefficient map and support

Factor exchange fixes the positive normal-deformation parameter and negates the diagonal normal vector. Simultaneous normal-vector and normal-covector negation preserves the Fourier pairing and its closed negative inequality. The actual diffeomorphism comparisons for the deformation's open and central inclusions and the Fourier proper projection therefore give

\[
\mu_\Delta(\sigma^{-1}K)
\simeq a^{-1}\mu_\Delta(K).
\qquad\text{(10)}
\]

This is the full comparison proved in the linked natural-duality lesson. On \(k_\Delta\), its normal specialization is supported on the zero vector, and the Fourier incidence projects identically to every normal covector. On \(\delta_*\omega_X\) the same calculation retains the coefficient \(\omega_X\). Consequently (10) identifies their maps with \(a^{-1}k_T=k_T\) and the specific \(a^{-1}E=E\) of (2). No normal integration or residual shift occurs on these center-supported objects.

Apply \(\mu_\Delta\) to both squares (7). They identify the canonical units and the evaluated targets, not just the middle objects. Here is the support assertion with its map retained. The comparison (10), followed by \(\mu_\Delta c_F\), identifies \(a^{-1}\mu\operatorname{hom}(F,F)\) with \(\mu\operatorname{hom}(D_XF,D_XF)\) and carries the identity germs to one another. In the [point-localized identity criterion](characteristic-cycles-from-supported-microlocal-identities.md#the-coefficient-and-the-supported-identity), such a germ is zero exactly when its cotangent point is absent from microsupport. Hence \(SS(D_XF)=a\,SS(F)\), including the zero covectors. This uses the whole microlocal-Hom comparison and its unit, without inferring support from the evaluated cycle, which can vanish by cancellation.

For the supported trace, put \(j:SS(F)\hookrightarrow T\). The middle microlocal-Hom object is supported on this closed set. Closed adjunction identifies every map from it to \(E\) uniquely with a map to \(j_*j^!E=R\Gamma_{SS(F)}E\): write the supported source as \(j_*j^{-1}\) of itself and apply \(j_*\dashv j^!\). The same applies on \(aSS(F)\). Diffeomorphism base change (2) and these adjunction bijections therefore lift the commuting evaluated square uniquely to the specified supports. Evaluating the units proves

\[
CC(D_XF)=CC(F)^a.
\qquad\text{(11)}
\]

It first proves the equality over \(k\). Both sides are images of integral cycles, and (3) is defined over \(\mathbb Z\); the proved injective coefficient comparison gives the identical equality for their canonical integral lifts. No choice of a global orientation, a generic stalk substitute for the supported map, or an additional factor \((-1)^n\) is inserted in (11).

## Four rays and one boundary equation

Take \(X=\mathbb R\), with increasing coordinate \(t\), dual coordinate \(\tau\), and \(\omega=d\tau\wedge dt\). Denote the normalized full zero-section and point-conormal cycles by \(\gamma=[T_X^*X]\) and \(\beta=[T_{\{0\}}^*X]\). Their four open ray chains are

\[
\alpha_\pm=\gamma|_{\{\pm t>0\}},\qquad
\beta_\pm=\beta|_{\{\pm\tau>0\}}.
\qquad\text{(12)}
\]

These are chain extensions to the crossing, retaining endpoint boundary germs. An individual ray is not a cycle there. Fix the positive fibre coefficient \(o_B\) determined by \(\partial_\tau\). The actual graph-normalized generators are

\[
\gamma=+\partial_t\otimes o_B,\qquad
\beta=+\partial_\tau\otimes o_B.
\]

We check both the trace and its conversion to a chain. Let \(p\) be the positive fibre point trace along \(\tau=0\), characterized by the identity under \(z^!\omega_\pi=k_X\). The [graph coefficient calculation](transverse-pullback-of-normalized-conormal-cycles.md#a-supported-point-unit-survives-every-tangential-rank) gives \(\gamma=-p\) in dimension one. The class \(\beta\) is the pullback of the positive closed point trace along \(t=0\); it involves no inverse graph coefficient.

For the chain comparison use \(\omega_T=B[1]\otimes E\), with ambient order \(d\tau\wedge dt\). The ordered cancellation to \(E\simeq\omega_T\otimes B[-1]\) moves the inverse fibre line past the odd base dualizing line and contributes a minus sign. A positive normal Thom class pairs with its tangent orientation in normal-then-tangent order, as fixed by the [compact-generator and trace calculation](intersections-of-supported-subanalytic-cycles.md#the-trace-map-is-the-inverse-chain-comparison). For \(p\), that order is \((\tau,t)\), agreeing with the ambient order; the cancellation therefore gives \(p=-\partial_t\otimes o_B\). For \(\beta\), the order is \((t,\tau)\), whose additional minus sign gives \(+\partial_\tau\otimes o_B\). Finally \(\gamma=-p\) gives the displayed positive horizontal generator. This calculation keeps the graph sign separate from the Thom and coefficient signs. A simultaneous change of the final coefficient trivialization changes neither the normalized cycles nor their conservation equation.

Let \(s\) be the positive vertex coefficient in that trivialization. The oriented interval boundary gives

\[
\partial\alpha_+=-s,\quad \partial\alpha_-=s,
\quad\partial\beta_+=-s,\quad\partial\beta_-=s.
\qquad\text{(13)}
\]

For example, a positively oriented ray \((0,\infty)\) has boundary minus its initial point; both \(\alpha_+\) and \(\beta_+\) have that orientation in their respective coordinates. A chain with coefficients \((a_+,a_-,b_+,b_-)\) on the four rays is a cycle exactly when

\[
a_+-a_-=-b_++b_-.
\qquad\text{(14)}
\]

There are no extra top-chain coefficients at the vertex: its dimension is zero whereas these chains have dimension one. A cycle restricts to a locally constant orientation coefficient on each smooth open ray, by the lowest-dualizing cycle description there. Each ray is connected, so it has one constant integer coefficient. These four integers determine the entire top chain, and the only remaining boundary is (13) at the vertex. Conversely the four constant ray chains with that boundary zero give a cycle. Solving (14) therefore gives the free integral cycle group

\[
H^0_{\{t\tau=0\}}(T^*\mathbb R;\mathcal L_{X,\mathbb Z})
=\mathbb Z(\alpha_++\alpha_-)
 \oplus\mathbb Z(\beta_++\beta_-)
 \oplus\mathbb Z(\alpha_+-\beta_+).
\qquad\text{(15)}
\]

Indeed every cycle is uniquely
\(a_-\gamma+b_-\beta+(a_+-a_-)(\alpha_+-\beta_+)\).
The crossing is itself a closed conic subanalytic isotropic carrier, so the proved cycle-sheaf identification applies. Formula (15) is a statement about cycles with this support on this crossing, not a claim about arbitrary singular cotangent carriers.

## Closed and open half-lines select different conormal rays

Let \(Z_\pm=\{\pm t\geq0\}\) and \(U_\pm=\{\pm t>0\}\). All coefficients are extended by zero from the indicated subset. Then

| Sheaf &emsp; | Integral characteristic cycle |
| --- | --- |
| \(k_X\) | \(-\alpha_+-\alpha_-\) |
| \(k_{\{0\}}\) | \(\beta_++\beta_-\) |
| \(k_{Z_+}\) | \(-\alpha_++\beta_+\) |
| \(k_{Z_-}\) | \(-\alpha_-+\beta_-\) |
| \(k_{U_+}\) | \(-\alpha_+-\beta_-\) |
| \(k_{U_-}\) | \(-\alpha_--\beta_+\) |

**Proof.** The [constant conormal calculation](transporting-characteristic-cycles-through-a-graph.md#globally-constant-finite-coefficients-fix-conormal-normalization) gives \(CC(k_X)=-\gamma\), while the [closed point calculation](characteristic-cycles-from-supported-microlocal-identities.md#a-finite-point-coefficient-fixes-the-normalization) gives \(CC(k_{\{0\}})=\beta\). These are the first two rows. The signed half-space microsupport tests in [Directional tests at a constructible boundary](../../sheaf-proof-readings/src/SH03/directional-tests-at-a-constructible-boundary.md#open-and-closed-boundary-conditions) give, away from zero covectors, the positive boundary ray for \(k_{Z_+}\) and the negative boundary ray for \(k_{U_+}\). Explicitly, the local support test is the fibre of the attachment to the opposite open half interval: the closed positive half-line has tests \((k,0)\), and the open positive half-line has tests \((0,k[-1])\). The same monotone-test proof gives the reversed rays for the minus half-lines. On the positive base zero section both plus half-lines are locally the constant coefficient; on the negative base they vanish. Their horizontal chain coefficients are therefore \((-1,0)\).

At \((0;\tau>0)\), the support triangle

\[
k_{U_+}\longrightarrow k_{Z_+}\longrightarrow k_{\{0\}}
\xrightarrow{+1}
\qquad\text{(16)}
\]

has its first object invisible in the point-localized category. It identifies \(k_{Z_+}\) there with \(k_{\{0\}}\), giving the coefficient \(+1\) on \(\beta_+\). At \((0;\tau<0)\), its middle object is invisible, so it identifies \(k_{U_+}\) with \(k_{\{0\}}[-1]\). The point coefficient and odd-shift rule give \(-1\) on \(\beta_-\). On the other boundary rays their microsupport is absent and their cycle coefficient is zero. The reversed-coordinate proof gives the minus rows, with their normalized relative orientations intact.

The dense top-ray coefficients determine each chain uniquely, by the top-chain injection. All rows satisfy (14), verifying the frontier cancellation directly. This proves the formulas as integral cycles through the crossing, including the zero covector; it does not extend each open ray independently as a cycle. \(\square\)

As another check, \(D_Xk_{Z_+}=k_{U_+}[1]\) and \(D_Xk_{U_+}=k_{Z_+}[1]\), with the increasing-line orientation. Formula (4) sends \(\alpha_+\) to \(-\alpha_+\), and (3) sends \(\beta_+\) to \(\beta_-\). Thus
\((-\alpha_++\beta_+)^a=\alpha_++\beta_-=-CC(k_{U_+})\), exactly (11). The minus and open rows obey the same check. These duality identities retain the entire complexes and their degree-one shift. For the constant line, \(D_Xk_X=k_X[1]\), while \(CC(k_X)=-\gamma\). Hence \(CC(D_Xk_X)=\gamma=(-\gamma)^a\). The odd shift and the antipodal eigenvalue agree after the constant-sheaf normalization has been included; no additional ambient-dimension factor belongs in (11).

## Exercises with complete solutions

### A tangent sign alone gives the wrong conormal answer

*Difficulty: Introductory.*

In \(X=\mathbb R^3\), let \(Z\) be a line. Compute the antipodal signs on the conormal tangent, the ambient cotangent orientation, the fibre coefficient, and the normalized conormal cycle. Compare the zero section and a point conormal.

**Solution.** Here \(m=1\) and \(n-m=2\). The two conormal fibre directions give tangent sign \(+1\), while negating all three ambient cotangent directions gives sign \(-1\). Their relative quotient is \(-1\). In the cycle model, the fibre orientation coefficient also has sign \(-1\), so tangent times coefficient is again \(-1\). Thus the line conormal changes sign, as \((-1)^m\) requires. The zero section has \(m=3\), giving \(-1\); a point has \(m=0\), giving \(+1\). Ignoring either the ambient relative orientation or the fibre coefficient would miss the line's sign.

### An odd degree needs the bidual sign

*Difficulty: Intermediate.*

At a point take \(P=k[1]\), with basis vector \(e\) of degree \(-1\). Calculate its identity tensor, its image under (6), and both evaluated traces. What would happen if biduality were replaced by the unsigned identification of bases?

**Solution.** Its dual vector \(e^*\) has degree \(1\). The identity tensor is \(e\otimes e^*\). Graded exchange gives \(-e^*\otimes e\), and the canonical bidual map gives \(b_P(e)=-e^{**}\). Their product is \(e^*\otimes e^{**}\), the dual identity tensor. Each right evaluation has the swap sign \(-1\), so both traces are \(-1\), agreeing with \(\chi(k[1])=\chi(k[-1])=-1\). An unsigned bidual identification would send the original tensor to the negative of the dual unit and give the wrong unit square. This is why objectwise dual-kernel isomorphism alone does not prove (11).

### Solve the crossing conservation equation

*Difficulty: Intermediate.*

Take ray coefficients \((2,1,3,4)\). Express their cycle in the basis (15). Then change the last coefficient to \(3\). Can a chain supported only at the vertex repair its boundary as a one-cycle?

**Solution.** The first tuple has \(2-1=-3+4=1\), so it is a cycle. Its unique decomposition is \(\gamma+4\beta+(\alpha_+-\beta_+)\). The altered tuple has boundary \((-2+1-3+3)s=-s\). A top chain supported only at the vertex is zero because the vertex has dimension zero, so it cannot change this one-chain or repair its boundary. One must change an incident ray coefficient or add an actual one-dimensional carrier. The rank-three cycle group is the kernel of the complete rank-one boundary map, rather than four independent endpoint-free rays.

### Finite coefficients retain the opposite open ray

*Difficulty: Intermediate.*

Let \(V\) have cohomology dimensions \(2,1,3\) in degrees \(0,1,2\) and vanish elsewhere. Compute the cycles of \(V_{Z_+}\), \(V_{U_+}\), and \(D_X(V_{Z_+})\). Explain both the coefficient and the conormal sign.

**Solution.** Its Euler characteristic is \(2-1+3=4\). Finite coefficient additivity, or the local coefficient-action model, multiplies every normalized ray coefficient by this integer. Thus the first two cycles are \(4(-\alpha_++\beta_+)\) and \(4(-\alpha_+-\beta_-)\). The dual is \(V^\vee_{U_+}[1]\); coefficient duality reverses cohomological degrees and preserves the Euler characteristic \(4\), while \([1]\) negates it. Its cycle is therefore \(4\alpha_++4\beta_-\). This also equals the antipodal image of the first cycle: the horizontal generator changes sign and the vertical positive ray becomes the negative ray with unchanged point-conormal normalization. The horizontal minus sign before dualizing comes from the one-dimensional constant-sheaf normalization. The open boundary's minus sign comes from the localized \([-1]\) in (16), not from a loss of finite coefficient rank.

### Two endpoints and the compact index

*Difficulty: Advanced.*

For \(a<b\), calculate the cycles of all four intervals with endpoints \(a,b\), open or closed independently. Use the section \(dt\) and the normalized point-conormal intersection to recover their compact-support Euler characteristics.

**Solution.** Let \(\gamma_{(a,b)}\) be the trimmed normalized zero-section chain, with its endpoint germs, and let \(\beta_{c,\pm}\) denote the corresponding point-conormal rays at \(c\). The local half-line formulas give

\[
\begin{aligned}
CC(k_{[a,b]})&=-\gamma_{(a,b)}+\beta_{a,+}+\beta_{b,-},\\
CC(k_{(a,b)})&=-\gamma_{(a,b)}-\beta_{a,-}-\beta_{b,+},\\
CC(k_{[a,b)})&=-\gamma_{(a,b)}+\beta_{a,+}-\beta_{b,+},\\
CC(k_{(a,b]})&=-\gamma_{(a,b)}-\beta_{a,-}+\beta_{b,-}.
\end{aligned}
\]

At the right endpoint the inward coordinate is \(b-t\), so its closed inward ray is negative in \(\tau\). The horizontal coefficient is \(-1\) on every interval interior. Its endpoint boundary is \(+s_a-s_b\); the vertical terms contribute \(-s_a+s_b\) in each displayed row. Their carriers are closed after joining at the endpoints, hence these are cycles.

The section \(dt\) has \(\tau=1\); it misses the zero section and all negative vertical rays. Its normalized intersection with a full point conormal is \(+1\), by the [actual closed-point trace calculation](continuous-sections-and-supported-cycle-intersections.md#every-section-meets-a-full-point-conormal-with-number-one). It therefore counts the positive vertical coefficients: respectively \(1,-1,1-1,0\). The straight section homotopy \(s\,dt\), \(0\leq s\leq1\), meets the carrier only over \([a,b]\) and at bounded fibre height. Its full incidence support is compact.

To identify this count with the compact index through specified maps, apply the [supported section-intersection comparison](continuous-sections-and-supported-cycle-intersections.md#the-complete-supported-section-intersection-comparison) to \(dt\) and to the zero section. Both resulting supported base classes become the same \(\beta_\pi(CC(F))\) after enlargement to the common closed base support \([a,b]\). That support is compact, so composing with its supported-to-compact map and the trace proves equality of the two scalar intersections. For the collapse \(a_X:\mathbb R\to\mathrm{pt}\), the cotangent incidence is the zero section over \([a,b]\), and its coefficient map is \(Ra_{X!}\omega_X\to k\). Thus the zero-section intersection is exactly the [proper cotangent direct image](lagrangian-cycles-and-proper-cotangent-images.md#a-direct-image-has-a-cotangent-incidence-domain) of \(CC(F)\). The [proper characteristic-cycle formula](transporting-characteristic-cycles-through-a-graph.md#the-transported-microlocal-identity-is-the-identity-of-the-image) identifies that number with \(CC(Ra_{X!}F)=\chi_c(\mathbb R;F)\). Properness holds on the compact closed support of each ambient extension, including the zero-stalk endpoints of an open interval.

Hence \(\chi_c=1,-1,0,0\). Directly, the closed interval has cohomology \(k\) in degree zero, the open interval has compact cohomology \(k[-1]\), and each half-open interval is acyclic by the endpoint localization triangle. Both calculations agree, with compact cycle intersection support even for the open intervals.

### Orientation monodromy survives numerical duality

*Difficulty: Advanced.*

Take \(X=\mathbb {RP}^2\times S^1\), a nonorientable analytic manifold of dimension three. Determine \(D_Xk_X\), its characteristic cycle, and the antipodal image of \([T_X^*X]\). Does the cycle calculation trivialize the orientation local system?

**Solution.** The orientation line \(\operatorname{or}_X\) has nontrivial sign monodromy along the nonorientable loop inherited from \(\mathbb {RP}^2\); the circle factor does not remove it. Verdier duality gives \(D_Xk_X=\operatorname{or}_X[3]\). Its local coefficient rank is one and its odd shift has Euler coefficient \(-1\). On each orientation chart the local-system normalization is \((-1)^3\) times that coefficient, so \(CC(D_Xk_X)=+[T_X^*X]\). In contrast, \(CC(k_X)=-[T_X^*X]\).

Formula (4), with \(Z=X\) and \(m=3\), gives \([T_X^*X]^a=-[T_X^*X]\). Applying it to the actual constant-sheaf cycle gives \(CC(k_X)^a=+[T_X^*X]\), agreeing with (11). This distinguishes the antipodal image of the normalized generator from the antipodal image of \(CC(k_X)\). It uses the globally defined relative orientation coefficient on cotangent cycles and local orientation calculations that agree on overlaps. It neither trivializes \(\operatorname{or}_X\) nor identifies the dual sheaf with the untwisted constant sheaf. A characteristic cycle retains the local Euler coefficient and its geometric orientation normalization, rather than all monodromy of the coefficient sheaf.

## References

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–2.3, pp. 196–197, supplies the coefficient-valued chain and twisted conormal framework; §§3–4 develop characteristic cycles and their index formulas. Our brackets are normalized by the programme's negative-first graph operation, while \(CC\) uses the positive-first microlocal-Hom parameter. The factor \((-1)^{\dim Z}\) in \(CC(k_Z)\) is the proved comparison between these conventions; it cannot be removed by reading a carrier as an oriented cycle.

M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Definition 5.5.1, printed pp. 90–91, defines diagonal microlocal Hom with the first-covector convention and records its support and recovery framework. Definition 5.6.1 and Proposition 5.6.2, printed p. 98, treat perfect formal neighborhood systems and the coefficient dual \(R\mathcal Hom(F,A_X)\), including biduality, antipodal microsupport and external-Hom exchange. On a manifold the passage to the Verdier dual \(R\mathcal Hom(F,\omega_X)\) also carries the orientation line and dimension shift, as in the linked costalk and natural-duality lessons. The kernel squares (7), their supported microlocalization and the cycle equality (11) are proved above with those particular maps.

The open and closed half-space signs are the classical Kashiwara–Schapira examples. The linked directional-test lesson proves the needed one-dimensional cases from attachment maps and monotone tests. Here the support triangle (16) determines the point coefficients and their odd shift, while the actual graph and closed-point traces determine the horizontal and vertical orientations. The four-ray boundary calculation then proves the formulas through the zero covector. The complete interval and nonorientable examples retain their compact support and orientation local system, respectively. Human sources keep their authorship and their own terms; the lesson text and solutions have the stated CC0 license.
