# SH02-LFI — Local models and change of ambient manifold

Independently expressed programme text is dedicated under CC0 1.0 Universal. This lesson develops local representatives and compatibility of microlocalization with inverse images. Its cutoff and deformation arguments are compared with Kashiwara and Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985), §§4.2, 5.4–5.5 and 6.2. The account below identifies their shared mechanisms, the boundary and support distinctions made here, and the separately named operation and comparison-map prerequisites.

## SH02-LFI-SOURCES — Local representatives, deformation and graph-relative Hom

The local representative constructions are compared with Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), §6.2, Propositions 6.2.1–6.2.3, pp. 106–107. Those propositions give the supported representative, the coefficient model and the inverse-image representative under the corresponding cotangent constraints. Their methods use signed open localization, the closed-embedding microsupport equality, a cone projector, a halfspace cutoff and local constancy along submersion fibers. The present arguments share those classical mechanisms; they are not unrelated constructions inferred from a replacement citation. The course keeps bounded arbitrary-module inputs over a commutative ring of finite global dimension, without constructibility or finite-rank assumptions, and distinguishes a representative at one covector from an isomorphism on an ordinary neighborhood.

The projector test is compared more precisely with Proposition 4.2.3, pp. 66–67. Its proof uses the difference map and the cone kernel to transport a forbidden covector. SH02-LFI-PROJECTOR writes out why the compact forward-support condition makes that ordinary image locally proper. The horizontal construction then bounds all relevant forward rays in a compact truncated cone, checks the halfspace boundary sign and applies the projector on an ordinary neighborhood. For the supported model, Proposition 6.2.1 reduces by codimension induction. Here a single containing hypersurface and the closed-embedding equality force the residual support into the full submanifold; the coefficient model separately removes tangential covectors by scaling. The operation and cutoff proofs remain the named programme prerequisites.

The three-condition inverse-image theorem follows the geometric framework of Astérisque 128, Theorem 5.4.1, pp. 85–89, with the submersive-center simplification in Remark 5.4.3, p. 90. The three tests control ambient cotangent escape, the normal-cone noncharacteristic condition and containment in the center conormal. The source proof passes to normal deformation, compares the ordinary base-change map, and obtains a contradiction by normalizing the tangential covectors left after the ambient ones have been bounded. SH02-LFI-ESCAPE retains that mechanism with the weighted discrepancies and both zero-normal base points explicit. The boundary step uses only convergence of spatial covectors; it does not require a full covector at zero parameter to be a limit of interior covectors. Problem 2 explains why that stronger lifting claim fails. SH02-LFI-NORMAL-TEST records the precise projected statement needed later.

The inverse-image proof also separates the supported defect from the trace defect. The cone D of ordinary base change is supported at zero parameter; the trace cone can persist on the positive chamber. Triangle LFI28 relates these two objects and the positive-side trace cone before Fourier transform is used to detect the supported defect. Problem 3 checks this distinction. The resulting identifications preserve the proper and ordinary direct images, relative orientation factors and the specified comparison arrows. The exact Fourier and trace square remains SH02-MIC-INVERSE and SH02-MIC-TRACE-EXCHANGE; comparison with Theorem 5.4.1 alone does not identify every course normalization.

The graph-relative objects and their functorial comparisons are compared with Definition 5.5.1 and Propositions 5.5.4–5.5.5, pp. 91–93, and Corollary 5.5.7, p. 94. The source applies the inverse-image theorem to Hom kernels along the graph and uses properness on the coefficient support for the direct comparison. The course spells out the escaping-sequence test for each Hom kernel, keeps the antipode in the contravariant graph object, and checks properness only on the relevant cotangent support before identifying the natural arrows through their trace-compatible square. The source formulates these Hom constructions with a bounded first input and bounded-below output. For the bounded output categories used here, [SH02-MD-BOUNDED-HOM in Manifold duality](../../SH02-manifold-duality.html#SH02-MD-BOUNDED-HOM) supplies the separate arbitrary-module bound, after the submersion orientation formula makes each exceptional projection pullback bounded.

The teaching order is projector and local representatives, the three geometric tests, the spatial boundary lemma, the supported-defect triangle, and the graph-relative consequences. It reorganizes and expands the source mechanisms and retains five solved tests of signs, support, escape and center maps. Independently expressed programme text retains CC0; the cited human source is credited without inferring permission to reuse its protected expression.

## SH02-LFI-SETUP — What a local model asserts

Fix a commutative ring $k$ of finite global dimension. All manifolds are finite dimensional, countable at infinity, and all complexes below belong to $D^b(k_X)$ on their indicated manifold. Submanifolds are locally closed unless explicitly called closed. A submersion is a map with surjective differential. No finiteness of stalks or constructibility is assumed.

An isomorphism in $D^b(k_X;p)$ can discard a complex whose microsupport avoids $p$. It usually says nothing about equality on a whole ordinary neighborhood of the base point. This distinction permits a complex with complicated singularities in other covector directions to have a particularly simple representative at $p$.

For a closed embedding $i:Y\hookrightarrow X$, write $T_Y^*X$ for its conormal bundle and $\pi_X:T^*X\to X$ for the projection. For a submersion $f:Y\to X$, the transpose differential identifies $Y\times_XT^*X$ with the horizontal covector subbundle of $T^*Y$. These are different constraints: the former involves where a covector is based; the latter involves which tangent directions it annihilates.

The proofs use the following exact contracts. A reference to a draft is a dependency, not a certification of it.

| Identifier | Required content |
| --- | --- |
| SH02-OPS-SIX | Bounded six operations, localization triangles, proper-support base change, tensor and internal-Hom adjunctions, coherent relative traces |
| SH02-MD-BOUNDED-HOM | [Manifold duality, M43–M44](../../SH02-manifold-duality.html#SH02-MD-BOUNDED-HOM): internal derived Hom of arbitrary bounded complexes is bounded on a finite-dimensional manifold; apply on the product manifold to both graph-relative kernels |
| SH02-MST-FORMAL | Triangle estimate for microsupport and the identification of its intersection with the zero section with the support |
| SH02-MST-CUTOFF-FORWARD | $P_\gamma=\phi_\gamma^{-1}R\phi_{\gamma *}$ has microsupport in the negative polar cone; its counit is a microlocal isomorphism in the interior of that cone |
| SH02-GAM-KERNEL | The ordinary direct-image kernel for $P_\gamma$ on a finite-dimensional vector space |
| SH02-AE-SEQUENCES, SH02-AE-NONCHAR | Weighted sequence descriptions of $f^\sharp A$ and its escaping part $f^\sharp_\infty A$ |
| SH02-AE-OPEN | Microsupport estimate for ordinary direct image or extension by zero across an arbitrary open set |
| SH02-CHE-005, SH02-CHE-PROPER | Localized trace comparison and properness of the cotangent correspondence above a noncharacteristic open set |
| SH02-MIC-INVERSE, SH02-MIC-TRACE-EXCHANGE | The two inverse-image comparison maps and the exact trace compatibility in their square |

### SH02-LFI-OPS — Microsupport operations contract

Closed-embedding equality and proper direct image in SH02-MO-PROPER-PUSH; external products in SH02-MO-EXTERNAL-TENSOR; exact pullback and local descent in SH02-MO-SUBMERSION.

### SH02-LFI-SPECIALIZATION — Specialization estimates contract

Normal deformation and specialization in SH02-SP-CONIC and SH02-MIC-DEFINITION; support in SH02-MO-MICROLOCAL-SUPPORT; the full normal-cone estimate in SH02-CHE-001; equality of microsupports under Fourier–Sato for every bounded conic complex in SH02-MO-FS-SS.

### SH02-LFI-HOM — Microlocal Hom comparison contract

Graph-relative microlocal Hom comparisons and their adjunction mates, with their full exact map contracts still required; the two-variable microsupport bound is SH02-MO-EXTERNAL-HOM.

Here is the precise content of the two elementary geometric operation contracts above. For a closed embedding,

$$
\operatorname{SS}(Ri_*A)
=i_\pi i_d^{-1}\operatorname{SS}(A),
\tag{LFI1}
$$

where $i_d$ restricts ambient covectors to $TY$. For a submersion $f$, a complex whose microsupport is contained in the horizontal subbundle on an ordinary neighborhood is, after shrinking to a product chart with contractible fibres, an inverse image from the base. This is the arbitrary-module local constancy theorem along the fibres; it does not require a globally trivial local system.

## SH02-LFI-PROJECTOR — A compactness test for transporting a covector

Let $E$ be a real vector space of finite dimension and let $\gamma\subset E$ be a closed convex pointed cone containing $0$. Its negative polar is

$$
\Lambda=\{\xi\in E^*: \langle v,\xi\rangle\leq0\text{ for every }v\in\gamma\}.
$$

Let $A\in D^b(k_E)$ and $x\in E$. Suppose there is a compact neighborhood $K$ of $x$ such that

$$
(K+\gamma)\cap\operatorname{supp}(A)\quad\text{is compact}.
\tag{LFI2}
$$

If $(x+\gamma)\times\{\xi\}$ is disjoint from $\operatorname{SS}(A)$, then

$$
(x,\xi)\notin\operatorname{SS}(P_\gamma A).
\tag{LFI3}
$$

**Proof.** Use coordinates $(v,z)$ on $E\times E$ and the difference map $d(v,z)=z-v$. The kernel theorem gives

$$
P_\gamma A\simeq Rd_*(k_\gamma\boxtimes A).
$$

Condition (LFI2) makes $d$ proper on the support of this kernel over a neighborhood of $x$. Indeed, if $z-v\in K$ and $v\in\gamma$, then $z\in(K+\gamma)\cap\operatorname{supp}(A)$, a compact set; then $v=z-(z-v)$ also ranges in a compact set. The relevant support is closed, so its intersection with this compact product is compact. The proper direct-image estimate is therefore applicable locally, although $d$ is not globally proper.

The transpose of $dd$ sends $\xi$ to $(-\xi,\xi)$. The external-product estimate consequently bounds the output microsupport by covectors for which some $v\in\gamma$ satisfies

$$
(v,-\xi)\in\operatorname{SS}(k_\gamma),
\qquad (x+v,\xi)\in\operatorname{SS}(A).
$$

The second condition is excluded by hypothesis. Notice that this argument needs ordinary direct image and the local properness check; it does not replace $Rd_*$ by $Rd_!$ without a support argument. $\square$

## SH02-LFI-HORIZONTAL — Replacing a complex by a pullback

Let $f:Y\to X$ be a submersion, let $p\in Y\times_XT^*X\subset T^*Y$, and let $G\in D^b(k_Y)$. If

$$
\operatorname{SS}(G)\subset Y\times_XT^*X
\quad\text{on a cotangent neighborhood of }p,
\tag{LFI4}
$$

then there is $F\in D^b(k_X)$ and an isomorphism

$$
G\simeq f^{-1}F\quad\text{in }D^b(k_Y;p).
\tag{LFI5}
$$

**Proof.** Work in a product chart around the base point, with $f$ the projection. Any object constructed on a smaller base chart may be extended by zero to $X$; its pullback has the same germ at the point under consideration. Thus it suffices to construct the model in the chart.

If $p$ is a zero covector, a cotangent neighborhood contains all sufficiently small covectors over a smaller base neighborhood. Conicity then turns (LFI4) into horizontal containment for every covector over that neighborhood. The local fibrewise constancy contract applies directly.

Now let the covector of $p$ be $\xi_0\ne0$, and put the base point at the origin of a vector space $E$. The horizontal covectors form a fixed linear subspace $H\subset E^*$. Choose closed convex cones $\Lambda_0,\Lambda_1$ such that

$$
\xi_0\in\operatorname{Int}\Lambda_0,
\qquad \Lambda_0\setminus\{0\}\subset\operatorname{Int}\Lambda_1,
$$

and $\Lambda_1$ is contained in the directional neighborhood in (LFI4). They can be chosen with $\xi_0$ strictly negative on the nonzero vectors of the negative polar $\gamma$ of $\Lambda_0$. Shrink a convex ordinary neighborhood $O$ so that

$$
\operatorname{SS}(G)\cap(O\times\Lambda_1)\subset O\times H.
\tag{LFI6}
$$

Choose $\epsilon>0$ small, put $B=\{z:\langle z,\xi_0\rangle> -\epsilon\}$, and replace $G$ outside a slightly smaller chart by extension by zero. All forward rays relevant below will stay inside $O$ while they meet $\overline B$. To arrange this explicitly, take a small ball $D$ around $0$ and use the directionally open set $D+\gamma$. Since $\xi_0$ is strictly negative on $\gamma\setminus\{0\}$, the set

$$
(\overline D+\gamma)\cap\{\langle z,\xi_0\rangle\geq-\epsilon\}
$$

is compact and can be made a subset of $O$ by decreasing $D$ and $\epsilon$. A still smaller neighborhood of $0$ has its $\gamma$-translates inside $D+\gamma$.

Set $A=G_B$, where the subscript means restriction followed by extension by zero. On the compact region just constructed,

$$
\operatorname{SS}(A)\cap(E\times\Lambda_0)\subset E\times H.
\tag{LFI7}
$$

Here is the boundary check. The open-extension estimate adds negative multiples of $\xi_0$ at $\partial B$. If an output covector $\xi\in\Lambda_0\setminus H$ were obtained, its input covectors would tend to $\xi+\lambda\xi_0$, possibly with $\lambda\to+\infty$. The strict containment $\Lambda_0\setminus0\subset\operatorname{Int}\Lambda_1$ implies that these input covectors eventually lie in $\Lambda_1$, also in the unbounded case after normalization. By (LFI6) they are horizontal. The added normal is horizontal as well, so their output limit is horizontal, a contradiction. Weighted base-point errors in the asymptotic-sum definition do not change this conclusion, because the defining function of $B$ is linear and its differential is the same at every point. The zero output covector is horizontal automatically.

Apply the projector to $A$. Its microsupport lies in $E\times\Lambda_0$. For an output covector in $\Lambda_0\setminus H$ over a sufficiently small neighborhood of $0$, (LFI7) excludes that covector at every point of its forward translate. Condition (LFI2) holds by the compact truncation above. The preceding projector lemma therefore excludes every such output covector. We have obtained

$$
\operatorname{SS}(P_\gamma A)\subset E\times H
\quad\text{over an ordinary neighborhood of }0.
$$

The counit $P_\gamma A\to A$ is an isomorphism at $p$, since $\xi_0\in\operatorname{Int}\Lambda_0$, and $A=G$ near the base point. The local fibrewise constancy theorem gives $P_\gamma A\simeq f^{-1}F$ on a smaller product chart. This proves (LFI5), with arbitrary fibre dimension and without induction on that dimension. $\square$

## SH02-LFI-SUPPORTED — Replacing a complex by one on a submanifold

Let $i:Y\hookrightarrow X$ be a closed embedding and $p\in T_Y^*X$. Suppose $F\in D^b(k_X)$ satisfies

$$
\operatorname{SS}(F)\subset\pi_X^{-1}(Y)
\quad\text{near }p.
\tag{LFI8}
$$

Then $F\simeq Ri_*G$ in $D^b(k_X;p)$ for some $G\in D^b(k_Y)$. If the stronger condition

$$
\operatorname{SS}(F)\subset T_Y^*X\quad\text{near }p
\tag{LFI9}
$$

holds, there is a bounded complex $M$ of $k$-modules with

$$
F\simeq M_Y\quad\text{in }D^b(k_X;p).
\tag{LFI10}
$$

Here $M_Y$ denotes the constant complex on $Y$, extended by zero to $X$. Its use is local in the category; the theorem does not assert that the original object is constant along all of $Y$.

**Proof of the supported representative.** At a zero covector, conicity converts (LFI8) into the assertion that the support is contained in $Y$ on a smaller ordinary neighborhood. The localization triangle gives the desired representative there, and extension by zero globalizes it.

For a nonzero $p$, choose coordinates in which a hypersurface $Z=\{h=0\}$ contains $Y$, $h$ is one coordinate, and $dh$ at the base point equals the covector of $p$. Let $j_-$ and $j_+$ denote the inclusions of $\{h<0\}$ and $\{h>0\}$. The open direct-image estimate gives

$$
p\notin\operatorname{SS}(Rj_{-*}j_-^{-1}F).
\tag{LFI11}
$$

To see the sign explicitly, a possible output near the positive covector $dh$ would be an input covector minus $\lambda dh$, $\lambda\geq0$. Thus the input would point near the positive $dh$ direction, whether $\lambda$ is bounded or tends to infinity. Its base point is in $\{h<0\}$ and hence outside $Y$, contradicting (LFI8). The same argument applies to the extension by zero $j_{+!}$, whose additional boundary covectors are again negative multiples of $dh$.

The first localization triangle replaces $F$ microlocally by $K=R\Gamma_{\{h\geq0\}}F$. It still satisfies (LFI8) near $p$, because the cone of $K\to F$ avoids $p$. The second localization triangle is

$$
j_{+!}j_+^{-1}K\longrightarrow K
\longrightarrow Ri_{Z*}i_Z^{-1}K\xrightarrow{+1}.
$$

The sign argument just given excludes $p$ from the first term. Thus $F$ has a representative $Ri_{Z*}A$ with $A=i_Z^{-1}K$. The same triangle estimate shows that this representative satisfies (LFI8) on a possibly smaller cotangent neighborhood of $p$.

This single hypersurface already suffices for arbitrary codimension. By (LFI1), every point in the support of $A$ carries every normal covector to $Z$ in the microsupport of $Ri_{Z*}A$. Near the chosen point, take the normal covector $dh$. Condition (LFI8) then forces $\operatorname{supp}(A)$ to lie in $Y$ after shrinking the base neighborhood. The support localization triangle on $Z$ identifies $A$ with the direct image of a complex on $Y$. Composing the two closed embeddings gives the required $G$. $\square$

**Proof of the coefficient model.** Start with $Ri_*G$. Formula (LFI1) says that every tangential covector of $\operatorname{SS}(G)$ lifts after adding an arbitrary normal covector. Choose the normal component near the fixed component of $p$ and scale the tangential component to be arbitrarily small. Condition (LFI9), combined with conicity, excludes every nonzero tangential covector of $G$ over a smaller neighborhood. Thus $G$ has microsupport in the zero section there. The local constancy theorem, applied on a small contractible coordinate ball of $Y$, gives a bounded coefficient complex $M$ with $G\simeq M_Y$ on that ball. Extend the model to obtain (LFI10). $\square$

## SH02-LFI-CORRESPONDENCE — Two levels of cotangent geometry

Let $f:Y\to X$ carry a closed submanifold $N\subset Y$ into a closed submanifold $M\subset X$. Put $g=f|_N$. We use the correspondences

$$
T^*Y\xleftarrow{d_f}Y\times_XT^*X\xrightarrow{\pi_f}T^*X,
\qquad d_f(y,\xi)=(y,df_y^t\xi),
$$

and

$$
T_N^*Y\xleftarrow{r}C\xrightarrow{s}T_M^*X,
\qquad C=N\times_M T_M^*X.
\tag{LFI12}
$$

The maps in the second line are restrictions of the first ones. In particular, $r(n,\xi)=(n,df_n^t\xi)$ and $s(n,\xi)=(g(n),\xi)$. There is no antipodal sign in these maps. Write $u:C\to N$ for the projection and set

$$
\omega_f=\omega_Y\otimes f^{-1}\omega_X^{-1},
\qquad \omega_g=\omega_N\otimes g^{-1}\omega_M^{-1}.
$$

The shift in $\omega_f$ is $\dim Y-\dim X$, component by component. An inverse on an orientation complex always means its tensor inverse, including reversal of its shift.

For a closed conic set $A\subset T^*X$, the phrase **$f$ is noncharacteristic for $A$ on $V\subset T^*Y$** means

$$
f^\sharp_\infty A\cap V=\varnothing.
\tag{LFI13}
$$

In coordinates, an element $(y_0,\eta_0)$ of the excluded set would be supplied by sequences $y_n\to y_0$ and $(x_n,\xi_n)\in A$ such that

$$
x_n\to f(y_0),\quad df_{y_n}^t\xi_n\to\eta_0,
\quad |x_n-f(y_n)|\,|\xi_n|\to0,
\quad |\xi_n|\to\infty.
\tag{LFI14}
$$

This localized condition includes a bound at infinity in the cotangent fibres. Merely checking the kernel of $df^t$ at one base point is insufficient.

The normal cone $C_{T_M^*X}(A)$ lives in the normal bundle to $T_M^*X$ inside $T^*X$. The symplectic form identifies that normal bundle with $T^*(T_M^*X)$. In adapted coordinates $x=(a,b)$, $M=\{a=0\}$, an element of $T_M^*X$ is $(b,\alpha)$, representing the ambient covector $(0,b;\alpha,0)$. The normal directions are changes in $a$ and in the tangential covector $\beta$; under the cotangent identification they give $(b,\alpha;\beta,-a)$. Fixing this convention prevents confusing the normal derivative with its negative transpose.

## SH02-LFI-ESCAPE — Why the deformed map is noncharacteristic

Put $A=\operatorname{SS}(F)$, where $F\in D^b(k_X)$, and let $V\subset T_N^*Y$ be open. Assume the following three conditions:

1. $f^\sharp_\infty A\cap V=\varnothing$.
2. The map $s:r^{-1}(V)\to T_M^*X$ is noncharacteristic, in the ordinary cotangent-kernel sense, for $B=C_{T_M^*X}(A)$.
3. Every $(y,\xi)\in\pi_f^{-1}(A)$ with $d_f(y,\xi)\in V$ has $\xi\in T_M^*X$.

The third condition concerns the full ambient correspondence, not only its already conormal restriction $C$. Equivalently,

$$
d_f^{-1}(V)\cap\pi_f^{-1}(A)
\subset Y\times_XT_M^*X.
\tag{LFI15}
$$

Let $\widetilde X_M,\widetilde Y_N$ be the normal deformations, $\widetilde f:\widetilde Y_N\to\widetilde X_M$ the induced map, and $j_X$ the positive-parameter inclusion. On the positive side let $p_X$ be the map to $X$, and set $E=Rj_{X*}p_X^{-1}F$.

For $(y_0,\eta_0)\in V$ and any real number $\tau_0$, the deformed map is locally noncharacteristic for $E$ at

$$
q=(0,y_0,0;\eta_0,0,\tau_0)\in T^*\widetilde Y_N.
\tag{LFI16}
$$

The zero before $y_0$ is the zero normal vector. This is exactly the normal vector that corresponds, after Fourier transform, to the zero cotangent vector above $(y_0,\eta_0)$.

**Proof.** Use adapted coordinates $(a,b)$ on $X$ and $(u,v)$ on $Y$, so that $M=\{a=0\}$ and $N=\{u=0\}$. Write

$$
f(u,v)=(g(u,v),h(u,v)),\qquad g(0,v)=0.
$$

On the deformation spaces put

$$
\widetilde f(u,v,t)=(G(u,v,t),H(u,v,t),t),
\quad tG(u,v,t)=g(tu,v),\quad H(u,v,t)=h(tu,v).
\tag{LFI17}
$$

The function $G$ is smooth at $t=0$ because $g(0,v)=0$. All its derivatives used below are bounded on a sufficiently small compact coordinate neighborhood.

Suppose an escaping sequence for $\widetilde f$ existed at $q$. Write its source base points as $(u_n,v_n,t'_n)$ and its covectors in $\operatorname{SS}(E)$ as

$$
(a_n,b_n,t_n;\alpha_n,\beta_n,\sigma_n).
$$

The sequence criterion yields convergence of both base points to their corresponding zero-normal points, together with

$$
\begin{aligned}
G_u^t\alpha_n+H_u^t\beta_n&\longrightarrow\eta_0,\\
G_v^t\alpha_n+H_v^t\beta_n&\longrightarrow0,\\
\sigma_n+G_t^t\alpha_n+H_t^t\beta_n&\longrightarrow\tau_0,
\end{aligned}
\tag{LFI18}
$$

where the derivatives are evaluated at $(u_n,v_n,t'_n)$. Moreover,

$$
\begin{aligned}
|\alpha_n|+|\beta_n|+|\sigma_n|&\longrightarrow\infty,\\
|(a_n,b_n,t_n)-\widetilde f(u_n,v_n,t'_n)|
(|\alpha_n|+|\beta_n|+|\sigma_n|)&\longrightarrow0.
\end{aligned}
\tag{LFI19}
$$

Boundedness of the derivatives in the last line of (LFI18) implies

$$
|\alpha_n|+|\beta_n|\longrightarrow\infty.
\tag{LFI20}
$$

Indeed, a bounded spatial part would make $\sigma_n$ bounded as well. From now on we retain only the first two lines of (LFI18), (LFI20), and the weaker weighted error using $|\alpha_n|+|\beta_n|$.

We may now arrange $t_n>0$. This reduction requires care. At $t=0$, the open direct-image estimate adds a nonnegative multiple of $dt$ to interior covectors. It implies that the *spatial projection* of each boundary microsupport point is a limit of spatial projections of interior microsupport points. It does not assert convergence of the full covector. Choose such interior approximants separately for each $n$, with errors smaller than $1/n$ times the reciprocal of all finite spatial norms occurring at that stage. A diagonal choice preserves the first two limits in (LFI18), the spatial growth (LFI20), and

$$
|(a_n,b_n,t_n)-\widetilde f(u_n,v_n,t'_n)|
(|\alpha_n|+|\beta_n|)\longrightarrow0.
\tag{LFI21}
$$

This argument also treats a sequence alternating between positive and zero parameters. Points with negative parameter are absent from the support of $E$.

On the positive side the submersion formula for microsupport gives

$$
(t_na_n,b_n;\alpha_n,t_n\beta_n)\in A;
\tag{LFI22}
$$

we used conicity to multiply the ordinary pulled-back covector by $t_n>0$. Differentiating (LFI17) gives the useful identity

$$
df_{(t'u,v)}^t(\alpha,t'\beta)
=\bigl(G_u^t\alpha+H_u^t\beta,
\ t'(G_v^t\alpha+H_v^t\beta)\bigr).
\tag{LFI23}
$$

By (LFI21), replacing $t'_n\beta_n$ by $t_n\beta_n$ changes the first component by a quantity tending to zero. The weighted discrepancy between $(t_na_n,b_n)$ and $f(t'_nu_n,v_n)$ also tends to zero after multiplication by $|\alpha_n|+|t_n\beta_n|$. Thus (LFI22) and (LFI23) would be an escaping sequence for $f$ at $(0,v_0;\eta_0,0)$ unless

$$
\{\alpha_n\}\text{ and }\{t_n\beta_n\}\text{ are bounded}.
\tag{LFI24}
$$

Condition 1 proves this boundedness. Passing to a subsequence, let $(\alpha_n,t_n\beta_n)\to(\alpha_*,\beta_*)$. Closedness of $A$ and (LFI23) put the limit in the correspondence appearing in (LFI15). Condition 3 therefore gives $\beta_*=0$. In particular, (LFI20) forces $|\beta_n|\to\infty$.

Pass to another subsequence with $\beta_n/|\beta_n|\to\beta_\infty$, where $|\beta_\infty|=1$. The covectors in (LFI22) approach $(0,b_0;\alpha_*,0)\in T_M^*X$. Dividing their normal displacement from $T_M^*X$ by $t_n|\beta_n|\to0$ gives

$$
\left(\frac{a_n}{|\beta_n|},
\frac{\beta_n}{|\beta_n|}\right)\longrightarrow(0,\beta_\infty).
$$

Consequently $B$ contains the covector at $(b_0,\alpha_*)$ whose base component is $\beta_\infty$ and whose fibre component is zero. Since $r(v_0,\alpha_*)=(v_0,\eta_0)$, condition 2 says that

$$
h_v(0,v_0)^t\beta_\infty\ne0.
\tag{LFI25}
$$

But divide the second line of (LFI18) by $|\beta_n|$. The bounded $\alpha_n$ term tends to zero, and $H_v(u_n,v_n,t'_n)\to h_v(0,v_0)$. The result is $h_v(0,v_0)^t\beta_\infty=0$, contradicting (LFI25). $\square$

## SH02-LFI-NORMAL-TEST — A boundary test that only needs spatial covectors

Let $C\in D^b(k_Y)$ and suppose $(y_0,\eta_0)\in T_N^*Y$ is absent from $\operatorname{SS}(C)$. Then every covector

$$
(0,y_0,0;\eta_0,0,\tau),\qquad\tau\in\mathbb R,
$$

is absent from $\operatorname{SS}(Rj_{Y*}p_Y^{-1}C)$.

**Proof.** If $\eta_0=0$, the support criterion makes $C$ zero near $y_0$, so the assertion is immediate. Otherwise suppose one of the displayed covectors belonged to that microsupport. Projecting the open-boundary estimate onto spatial covectors gives positive-parameter points

$$
(u_n,v_n,t_n;\eta'_n,\eta''_n,\tau_n),
\quad t_n>0,
$$

with $(u_n,v_n,t_n)\to(0,y_0,0)$ and $(\eta'_n,\eta''_n)\to(\eta_0,0)$. The submersion formula and conicity then give

$$
(t_nu_n,v_n;\eta'_n,t_n\eta''_n)\in\operatorname{SS}(C).
$$

These covectors converge to $(y_0,\eta_0)$. Closedness supplies the contradiction. No bound or convergence for $\tau_n$ is needed. $\square$

## SH02-LFI-INVERSE — Microlocalization commutes with inverse image under three tests

Under the three hypotheses in SH02-LFI-ESCAPE, the natural maps

$$
Rr_!\bigl(u^{-1}\omega_g\otimes s^{-1}\mu_MF\bigr)|_V
\longrightarrow
\mu_N(\omega_f\otimes f^{-1}F)|_V
\tag{LFI26}
$$

and

$$
\mu_N(f^!F)|_V\longrightarrow
(Rr_*s^!\mu_MF)|_V
\tag{LFI27}
$$

are isomorphisms. The first map uses proper direct image and the second ordinary direct image. Their relation through the relative-trace square uses the exact dependency SH02-MIC-TRACE-EXCHANGE; that natural-transformation identity is not inferred from an isomorphism of their objects.

**Proof of the first comparison.** Retain the deformation notation above. The ordinary base-change arrow is

$$
\beta:\widetilde f^{-1}E
\longrightarrow Rj_{Y*}\widetilde f_+^{-1}p_X^{-1}F.
$$

Its cone $D$ is supported on $t=0$: over $t>0$ it is the identity base-change map, and over $t<0$ both sides vanish. It is this cone, rather than the cone of an arbitrary trace comparison, that has the required support property.

Let $H$ be the cone of the trace map

$$
\omega_{\widetilde f}\otimes\widetilde f^{-1}E
\longrightarrow\widetilde f^!E.
$$

Exceptional base change across the open inclusions identifies the right hand object with $Rj_{Y*}\widetilde f_+^!p_X^{-1}F$. Naturality of relative trace gives a map from this trace cone to the direct image of its restriction $H_+$, and the cone-of-a-square triangle is

$$
\omega_{\widetilde f}\otimes D
\longrightarrow H\longrightarrow Rj_{Y*}H_+\xrightarrow{+1}.
\tag{LFI28}
$$

On the positive side the deformation is a product with the parameter, so

$$
H_+\simeq p_Y^{-1}C_F,
\qquad
C_F=\operatorname{Cone}(\omega_f\otimes f^{-1}F\to f^!F).
$$

Condition 1 and the localized trace theorem give $\operatorname{SS}(C_F)\cap V=\varnothing$. The normal-test lemma therefore excludes every $q$ in (LFI16) from $\operatorname{SS}(Rj_{Y*}H_+)$. The escape lemma and the same localized trace theorem exclude $q$ from $\operatorname{SS}(H)$. Applying the triangle estimate to (LFI28) excludes $q$ from $\operatorname{SS}(D)$.

Write $s_Y:T_NY\hookrightarrow\widetilde Y_N$ for the zero-parameter embedding. Since $D$ is supported there, $D\simeq Rs_{Y*}s_Y^{-1}D$. Restricting $\beta$ to the zero fibre gives the specialization inverse comparison; its two terms are conic, so its cone $s_Y^{-1}D$ is conic as well. Formula (LFI1) now implies that $(0,y_0;\eta_0,0)$ is absent from the microsupport of $s_Y^{-1}D$. Under the Fourier cotangent identification, this is the zero cotangent vector above $(y_0,\eta_0)\in T_N^*Y$. The microsupport equality SH02-MO-FS-SS and the zero-section support criterion show that the Fourier transform of $s_Y^{-1}D$ vanishes near that point. This proves that the transformed specialization inverse comparison is an isomorphism on $V$.

Finally, the orientation identity on the normal deformation is

$$
\omega_{T_Nf}=\tau_N^{-1}(\omega_f|_N).
$$

The Fourier operation identities convert the just-proved comparison, tensored by this line, into (LFI26). Their orientation cancellation gives exactly $u^{-1}\omega_g$ on its left hand side. This is the same specified map as SH02-MIC-INVERSE, not an arbitrarily selected isomorphism between the two functors.

**Proof of the second comparison.** The relative-trace square for the two maps has right vertical arrow induced by $\omega_f\otimes f^{-1}F\to f^!F$. Its microlocalization is an isomorphism on $V$, since the support of $\mu_N C_F$ is contained in $\operatorname{SS}(C_F)\cap T_N^*Y$.

For the other vertical arrow, the specialization estimate gives

$$
\operatorname{SS}(\mu_MF)\subset C_{T_M^*X}(A)=B.
$$

Condition 2 therefore makes $u^{-1}\omega_g\otimes s^{-1}\mu_MF\to s^!\mu_MF$ an isomorphism on $r^{-1}(V)$. Condition 1 makes $d_f$ proper on $\pi_f^{-1}(A)$ above $V$. As $\operatorname{supp}\mu_MF\subset A\cap T_M^*X$, its restriction $r$ is proper on the relevant pulled-back support. Hence forgetting proper support, $Rr_!\to Rr_*$, is also an isomorphism on $V$ for these objects. The left vertical arrow is thus invertible.

The trace-compatible square, whose precise map identification remains the declared dependency, now has an invertible top arrow and invertible vertical arrows. Its bottom arrow is (LFI27), so that map is invertible as well. $\square$

## SH02-LFI-SUBMERSIVE-CENTERS — A simpler test on the centers

Retain $f:(Y,N)\to(X,M)$ and $V\subset T_N^*Y$ open. Suppose $f$ is locally noncharacteristic for $F$ on $V$, and $g:N\to M$ is a submersion. Then both (LFI26) and (LFI27) are isomorphisms on $V$.

**Proof.** The map $s$ is the base change of $g$ by the bundle projection $T_M^*X\to M$, so it too is a submersion. Its transpose differential is injective; consequently it is noncharacteristic for every cotangent subset, including $B$.

If $df_n^t\xi$ annihilates $T_nN$, then $\xi$ annihilates $df_n(T_nN)=T_{g(n)}M$, because $dg_n$ is surjective. Thus any ambient covector whose image lies in $T_N^*Y$ already lies in $T_M^*X$. This proves (LFI15), independently of $F$. All three conditions of the theorem hold. The ambient map $f$ itself need not be a submersion. $\square$

## SH02-LFI-NESTED — Changing the center inside one manifold

Let $N\subset M\subset X$ be closed submanifolds. Put

$$
C=T_M^*X|_N=T_N^*X\cap T_M^*X,
\qquad r:C\hookrightarrow T_N^*X,
\qquad s:C\hookrightarrow T_M^*X.
$$

Let $V\subset T_N^*X$ be open and assume that $s:C\cap V\to T_M^*X$ is noncharacteristic for $C_{T_M^*X}(\operatorname{SS}(F))$. Then the natural map

$$
\mu_NF|_{C\cap V}\longrightarrow(s^!\mu_MF)|_{C\cap V}
\tag{LFI29}
$$

is an isomorphism. The functor on the right is exceptional inverse image. Its orientation and codimension shift are part of the assertion.

**Proof.** Write $A=\operatorname{SS}(F)$ and $L=T_M^*X$. We first show that, in a neighborhood of $C\cap V$ inside $T_N^*X$, every point of $A$ lies in $L$.

Use coordinates $(a,b,c)$ on $X$ with $M=\{a=0\}$ and $N=\{a=b=0\}$. A point of $T_N^*X$ has coordinates $(0,0,c;\alpha,\beta,0)$, and it lies in $L$ exactly when $\beta=0$. If the claim failed at a point of $C\cap V$, there would be points of $A\cap T_N^*X$ tending to it with $\beta_n\ne0$. Divide their displacement normal to $L$ by $|\beta_n|$. A subsequence gives a nonzero limit covector in $C_L(A)$ with only a $b$-covector component. It annihilates the tangent space of $C\subset L$, so it is characteristic for $s$. This contradicts the hypothesis.

Choose an open neighborhood $W$ of $C\cap V$ in $T_N^*X$ on which the claimed containment holds, with $W\cap C\subset V$. Apply SH02-LFI-INVERSE to the identity map $f:X\to X$, with centers $N$ and $M$, and the open set $W$. The identity has no escaping cotangent sequences, the second hypothesis is the assumption, and the third is precisely the containment just proved. The lower comparison is

$$
\mu_NF|_W\longrightarrow(Rr_*s^!\mu_MF)|_W.
$$

Restricting to the image of the closed embedding $r$ gives (LFI29). $\square$

## SH02-LFI-GRAPH — Separating an ambient map from a change of center

Every map of pairs $f:(Y,N)\to(X,M)$ admits the factorization

$$
(Y,N)\xrightarrow{\Gamma_f}(Y\times X,\Gamma_g)
\xrightarrow{\mathrm{id}}(Y\times X,N\times M)
\xrightarrow{\operatorname{pr}_X}(X,M),
\tag{LFI30}
$$

where $\Gamma_f(y)=(y,f(y))$ and $\Gamma_g$ is its restriction to $N$. The first map identifies the source center with the target center, the middle map changes only the center, and the last map is a product projection. The first and last center maps are submersions. Thus the submersive-center and nested-center results isolate the two geometric issues in a general comparison: possible escaping ambient covectors and possible characteristic covectors for the inclusion of one center into another.

This factorization also checks the types in the direct proof. The intermediate center is first the graph $\Gamma_g$, and only then the product $N\times M$; substituting the product at both stages changes the statement. The normal-deformation maps compose to the deformation of $f$. The adjunction units defining ordinary inverse comparison and the counits defining exceptional inverse comparison compose to the corresponding unit and counit for $f$. Applying the same Fourier equivalences to these equalities proves that the composed comparison maps agree with (LFI26) and (LFI27). Relative orientation complexes multiply according to $\omega_{ab}\simeq\omega_b\otimes b^{-1}\omega_a$. These observations justify using the factorization as an alternative proof organization without introducing an untracked scalar or sign into the comparisons.

## SH02-LFI-GRAPH-HOM — Microlocal morphisms along a map

We spell out the objects in the final two consequences. On $X\times Y$ let $q_X,q_Y$ be the projections, and let $\Gamma=\{(f(y),y):y\in Y\}$. Its conormal bundle is identified with $Y\times_XT^*X$ by

$$
(y,\xi)\longmapsto(f(y),y;\xi,-df_y^t\xi).
\tag{LFI31}
$$

For $F\in D^b(k_X)$ and $G\in D^b(k_Y)$ define the graph-relative objects

$$
\begin{aligned}
\mathcal H_f(G,F)&=\mu_\Gamma R\mathcal Hom(q_Y^{-1}G,q_X^!F),\\
\mathcal H_f(F,G)&=\bigl(\mu_\Gamma R\mathcal Hom(q_X^{-1}F,q_Y^!G)\bigr)^a.
\end{aligned}
\tag{LFI32}
$$

The superscript $a$ is pullback by antipodal multiplication on conormal covectors. Both lines of (LFI32) are written on the same correspondence (LFI31); the antipode in the second is therefore essential.

Let $V$ be any subset of $T^*Y$. If

$$
f^\sharp_\infty\operatorname{SS}(F)
\cap V\cap\operatorname{SS}(G)=\varnothing,
\tag{LFI33}
$$

then the canonical maps

$$
\mu hom(G,f^!F)|_V
\longrightarrow(Rd_{f*}\mathcal H_f(G,F))|_V
\tag{LFI34}
$$

and

$$
\mu hom(f^{-1}F,G)|_V
\longrightarrow(Rd_{f*}\mathcal H_f(F,G))|_V
\tag{LFI35}
$$

are isomorphisms. Openness of $V$ is not required here: the proof gives the assertion on suitable neighborhoods of its individual points, then restricts to $V$.

**Proof.** Both Hom kernels in LFI32 are bounded by SH02-MD-BOUNDED-HOM on the product manifold. The exceptional projection pullbacks are bounded by the submersion orientation formula, and ordinary inverse image is exact. This uses no perfectness, finite stalks or constructibility. Consider $h=f\times\mathrm{id}_Y:Y\times Y\to X\times Y$, with the diagonal in the source and $\Gamma$ in the target. Its map between the centers is a diffeomorphism. Thus SH02-LFI-SUBMERSIVE-CENTERS applies as soon as we verify localized noncharacteristicness for the two Hom kernels.

For the first kernel $K=R\mathcal Hom(q_Y^{-1}G,q_X^!F)$, the two-variable microsupport estimate gives

$$
\operatorname{SS}(K)\subset
\{(x,z;\xi,-\zeta):
(x,\xi)\in\operatorname{SS}(F),\ (z,\zeta)\in\operatorname{SS}(G)\}.
\tag{LFI36}
$$

Suppose $h$ had an escaping sequence at the diagonal covector $(y,y;\eta,-\eta)$ with $(y,\eta)\in V$. The transpose differential has components $(df^t\xi,-\zeta)$, so $\zeta_n\to\eta$. Closedness implies $(y,\eta)\in\operatorname{SS}(G)$. The $\zeta_n$ are bounded, so the escaping norm must come from $|\xi_n|\to\infty$. The weighted base-point error for $h$ implies the weighted error for $f$, and $df^t\xi_n\to\eta$. Thus the same sequence gives $(y,\eta)\in f^\sharp_\infty\operatorname{SS}(F)$, contradicting (LFI33).

The lower exceptional comparison from the submersive-center theorem is therefore an isomorphism. The internal-Hom adjunction and composition of exceptional inverse images identify

$$
h^!K\simeq
R\mathcal Hom(p_2^{-1}G,p_1^!f^!F)
$$

on $Y\times Y$. Its diagonal microlocalization is $\mu hom(G,f^!F)$. The induced conormal map is exactly $d_f$, with the positive transpose in (LFI31). This proves (LFI34) for the specified canonical map.

For the second kernel the estimate has signs $(-\xi,\zeta)$, and the relevant diagonal covector before applying the antipode is $(-\eta,\eta)$. The same sequence argument, with both signs reversed, again reduces an escaping sequence to the forbidden point in (LFI33). The formal identification is now

$$
h^!R\mathcal Hom(q_X^{-1}F,q_Y^!G)
\simeq R\mathcal Hom(p_1^{-1}f^{-1}F,p_2^!G).
$$

After diagonal microlocalization and the antipode, this is $\mu hom(f^{-1}F,G)$. This proves (LFI35). At points outside $\operatorname{SS}(G)$ the escaping-sequence check is already impossible; at points in it, (LFI33) applies. These are local assertions, so the same argument covers arbitrary $V$. $\square$

## SH02-LFI-CLOSED-HOM — A closed embedding converts the graph comparison

Under the hypotheses of SH02-LFI-GRAPH-HOM, suppose in addition that $f:Y\hookrightarrow X$ is closed. Then the natural maps

$$
(Rd_{f!}\pi_f^{-1}\mu hom(Rf_*G,F))|_V
\longrightarrow\mu hom(G,f^!F)|_V
\tag{LFI37}
$$

and

$$
(Rd_{f!}\pi_f^{-1}\mu hom(F,Rf_*G))|_V
\longrightarrow\mu hom(f^{-1}F,G)|_V
\tag{LFI38}
$$

are isomorphisms. Here $Rf_!=Rf_*$ because the embedding is closed. The functor $Rd_{f!}$ remains a proper-support direct image; the cotangent restriction map $d_f$ generally has noncompact affine fibres.

**Proof.** Closedness makes $\pi_f:Y\times_XT^*X\hookrightarrow T^*X$ a closed embedding. The proper graph-Hom comparisons identify

$$
R\pi_{f*}\mathcal H_f(G,F)\simeq\mu hom(Rf_*G,F),
\quad
R\pi_{f*}\mathcal H_f(F,G)\simeq\mu hom(F,Rf_*G).
$$

Applying $\pi_f^{-1}$ and its counit gives the graph-relative objects themselves. This uses the full faithfulness of a closed embedding, not a nonexistent identity for an arbitrary map.

For either graph-relative object, its support lies in the set where $\xi\in\operatorname{SS}(F)$ and $d_f(y,\xi)\in\operatorname{SS}(G)$. At a point of $V\cap\operatorname{SS}(G)$, (LFI33) and cotangent properness give a neighborhood on which $d_f$ is proper on that support. At a point outside $\operatorname{SS}(G)$ the output support is absent on a neighborhood. Hence forgetting proper support is an isomorphism on $V$:

$$
Rd_{f!}\mathcal H_f\longrightarrow Rd_{f*}\mathcal H_f.
$$

Now use (LFI34) and (LFI35). To verify the direction and identity of the arrows in (LFI37) and (LFI38), use the graph-Hom adjunction square: the upper arrow is the proper-support comparison; its target is initially expressed using $\omega_f\otimes f^{-1}F$. Compose with relative trace, and in the contravariant variable cancel the same invertible orientation line in both arguments. The trace-compatible square identifies this composite with the inverse of (LFI34), respectively (LFI35), after forgetting proper support. Thus the displayed natural arrows, not only their source and target objects, are isomorphisms. This last identification uses the declared graph-Hom and trace-compatibility dependencies. $\square$

## SH02-LFI-EXAMPLES — Three calculations that separate the hypotheses

**A local coefficient model with no finite-rank condition.** Let $X=\mathbb R^2$, $Y=\{x=0\}$, and let $M$ be any bounded complex of $k$-modules. Then $M_Y$ has microsupport in $T_Y^*X$, so the coefficient model holds at every conormal covector. Add a sheaf $A$ whose microsupport near the origin has only nonzero covectors proportional to $dy$, for example a constant coefficient complex on the line $y=0$, extended by zero. At the covector $dx$, the resulting direct sum $M_Y\oplus A$ is microlocally isomorphic to $M_Y$. It is generally not isomorphic to it on an ordinary neighborhood, because the second summand has nonzero stalks on that line. This example works for infinitely generated modules and complexes with several nonzero cohomology groups.

**A product projection with a vertical singularity discarded.** Let $f:\mathbb R_s\times\mathbb R_x\to\mathbb R_x$ be projection and set

$$
G=f^{-1}k_{\{x\geq0\}}\oplus k_{\{s=0\}}.
$$

At $p=(0,0;0,dx)$, the second summand has only vertical conormal covectors and is absent microlocally. Thus $G$ has the pullback model $f^{-1}k_{\{x\geq0\}}$ at $p$. At the vertical covector $ds$, horizontal containment fails. A statement about the full ordinary neighborhood would confuse these two tests.

**The shift in a nested-center restriction.** Let $X=M=\mathbb R^d$, let $N=\{0\}$, and let $F=k_X$. The center conormal $T_M^*X$ is the zero section. Its normal-cone microsupport condition is satisfied. Formula (LFI29), restricted to the common zero covector, gives

$$
(\mu_{\{0\}}k_X)_0\simeq i^!k_X
\simeq\operatorname{or}_{\{0\}/X}[-d].
$$

On an oriented coordinate chart this is $k[-d]$. The exceptional inverse image in (LFI29) accounts for the shift. Ordinary restriction would instead give $k$.

## SH02-LFI-PROBLEMS — Problems with solutions

**Problem 1: preserve the positive side of a covector.** In the supported-representative proof, replace $p=dh$ by $p=-dh$. Which two open sets must be used, and which support complex replaces $F$ first?

*Solution.* Replace the coordinate $h$ by $-h$. The first discarded direct image is from $\{h>0\}$, and the first representative is $R\Gamma_{\{h\leq0\}}F$. The second discarded extension by zero is from $\{h<0\}$. In each boundary estimate the added conormal points opposite to the chosen covector. Therefore an output in the chosen direction forces an input in that same direction outside $Y$. The zero-hypersurface representative remains on $\{h=0\}$.

**Problem 2: why a boundary covector cannot be lifted literally.** Take $j:(0,\infty)\hookrightarrow\mathbb R$ and $A=k_{(0,\infty)}$ as a sheaf on its own domain. Compute $Rj_*A$ near $0$. Explain why a covector $\tau\,dt$ with $\tau>0$ at $0$ need not be a limit of covectors of $A$ on the open interval, and identify the fact that remains valid in the escape proof.

*Solution.* Sections on sufficiently small positive intervals are constant and have no higher cohomology, so $Rj_*A=k_{[0,\infty)}$. At $0$ its microsupport contains the positive half-conormal $\{\tau\,dt:\tau\geq0\}$. On the open interval $A$ is locally constant, so its microsupport is the zero section. A fixed nonzero $\tau\,dt$ is not a limit of those zero covectors. Projection that forgets the $dt$ component sends both sets to zero. In higher-dimensional products the boundary estimate preserves the convergence of the other covector components, which is precisely the projected statement used in SH02-LFI-ESCAPE and SH02-LFI-NORMAL-TEST.

**Problem 3: the trace defect need not be supported at zero parameter.** Let $f:\mathbb R_y\hookrightarrow\mathbb R^2_{x,y}$ embed the line $x=0$, let $F=k_{\{x=0\}}$, and take $N=M=\{0\}$ in their respective manifolds. Show that $f$ is locally noncharacteristic for $F$ on the positive nonzero conormal ray $V=\{(0,\eta\,dy):\eta>0\}$, although the cone of $\omega_f\otimes f^{-1}F\to f^!F$ is nonzero. Explain why the deformation proof uses the base-change cone $D$ to obtain a complex supported at $t=0$.

*Solution.* Every covector in $\operatorname{SS}(F)$ is a multiple of $dx$ based on the embedded line. The transpose differential sends all of them to zero. Thus an escaping sequence can only have zero output, and the positive ray $V$ is disjoint from its escaping set. The center map is a map between points, so the other two hypotheses of the submersive-center result hold automatically. Nevertheless $f^{-1}F=k_Y$, $f^!F=k_Y$, and $\omega_f=k_Y[-1]$ after choosing the coordinate orientation. The comparison $k_Y[-1]\to k_Y$ is not an isomorphism. In a positive-parameter product its nonzero cone persists at every positive parameter. The base-change arrow defining $D$, by contrast, is an identity after restriction to the positive side, and both its terms vanish on the negative side. Its cone is therefore supported at zero parameter. Triangle (LFI28) uses the two trace cones to control the microsupport of this supported defect.

**Problem 4: a cotangent-fibre properness test.** Suppose $(y_n,\xi_n)$ is a sequence in $\pi_f^{-1}\operatorname{SS}(F)$ whose image $d_f(y_n,\xi_n)$ lies in a compact subset $K$ of an open set on which $f$ is locally noncharacteristic. Prove that the sequence has a convergent subsequence.

*Solution.* Pass to a subsequence with $d_f(y_n,\xi_n)\to(y_0,\eta_0)\in K$. The base points already satisfy $x_n=f(y_n)$, so the weighted base discrepancy in (LFI14) is zero. If the norms of $\xi_n$ were unbounded, a subsequence would give an escaping cotangent sequence at $(y_0,\eta_0)$, contradicting noncharacteristicness. Thus the covectors are bounded in a local trivialization, and a convergent subsequence exists. Closedness of the correspondence over $K$ puts its limit in the same set. This proves properness locally above $K$; it supplies no properness assertion away from the chosen open set.

**Problem 5: the center map and the ambient map have different roles.** Let $f:Y\hookrightarrow X$ be a closed embedding, take $N=Y$, and take $M=f(Y)$. Which of the three hypotheses for the inverse-image theorem are automatic?

*Solution.* The center map $g:Y\to f(Y)$ is a diffeomorphism, hence a submersion. Consequently $s$ is a submersion and condition 2 is automatic. If an ambient covector pulls back to a covector annihilating $TY$, it annihilates $T(f(Y))$, so condition 3 is automatic as well. Condition 1 remains a condition on $F$: the example in Problem 3 shows that the ambient closed embedding can be characteristic. The center-map simplification does not eliminate this issue.

## SH02-LFI-ROUTES — Further uses and the remaining proof boundary

The two local model theorems are tools for working in a category localized at a covector: they turn a geometric constraint into a representative on a smaller base or on a submanifold. The inverse-image theorem has a different purpose. Its three tests control ambient escape, limiting tangential covectors, and compatibility of the two centers. The graph-relative Hom consequences allow one to transport local morphisms after these tests have been verified.

A useful next calculation is to choose a characteristic embedding and follow the nonzero base-change defect through normal deformation and Fourier transform. Another is to study a nested pair of submanifolds for which the normal-cone condition fails, and compare the two sides of (LFI29). Neither investigation licenses removing the hypotheses of the theorem.

All displayed results have proofs here relative to the typed contracts in SH02-LFI-SETUP, including the explicit bounded-Hom provider. The Fourier/trace and graph-Hom natural-transformation identities retain their named suppliers and prerequisite boundaries. The analytic sequence argument, spatial boundary reduction and supported-defect distinction are written out.
