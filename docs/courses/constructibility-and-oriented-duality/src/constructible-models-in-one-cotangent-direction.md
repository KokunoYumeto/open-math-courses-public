# Constructible models in one cotangent direction

Local isotropic control of microsupport produces a constructible model in the localized category, even when the original sheaf is arbitrary elsewhere. The construction must control every direction of its new model near the chosen base point, including directions created at a cutoff boundary. We use a polyhedral cone and a flat cap to achieve this, then extend a compactly supported model to the whole manifold. A second application shows that a constructible contact kernel preserves the pointwise perfect constructible categories in both directions.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

Use Constructibility through smooth cutoffs and microlocal properness for the pointwise category definition, the forward criterion and perfect microlocally proper images. The geometric operations used here are proved in [Conic subanalytic images and isotropic dimension](../../sheaf-proof-readings/SH03-conic-subanalytic-images-and-isotropic-dimension.html), [Isotropic cotangent transport](../../sheaf-proof-readings/SH03-isotropic-cotangent-transport-and-discrete-critical-values.html), and [Limiting cotangent sums and characteristic inverse images](../../sheaf-proof-readings/SH03-limiting-cotangent-sums-and-characteristic-inverse-images.html). The contact equivalence and its actual unit/counit maps are those of [When a kernel quantizes a contact transformation](../../sheaf-proof-readings/SH03-when-a-kernel-quantizes-a-contact-transformation.html).

The exact sheaf inputs are the cone projector's polar bound and counit, its ordinary kernel realization, the full bounded tensor/Hom limiting estimates, noncharacteristic tensor and proper-on-support image estimates, and saturated localized fractions. We assume these sheaf-operation and localization results. The local-model proof below uses radial saturation, a flat cap and a final compact supported localization. The contact application additionally needs the identity on microlocal endomorphisms and both actual adjunction maps; a graph-shaped correspondence alone is insufficient.

## The local criterion and its coefficient scope

Let $k$ be commutative of finite global dimension. Manifolds and maps in constructibility arguments are real analytic, Hausdorff, countable at infinity, with uniform finite dimension bounds. Inputs and all representatives are globally bounded derived objects. Tensor products are derived. Write $a(x;\xi)=(x;-\xi)$ for the antipode. Weak R-constructibility imposes the geometric condition; R-constructibility additionally requires perfect stalk complexes. No field, Noetherianity, finite-rank or orientation hypothesis is added.

For any subset $\Omega\subset T^*X$, the preceding lesson defined $D^b_{\mathrm{w\text{-}R\text{-}c}}(k_X;\Omega)$ by existence, at every $p\in\Omega$, of a globally weakly R-constructible representative isomorphic to $F$ in $D^b(k_X;p)$. It proved the forward implication of the following criterion.

**Local isotropic criterion.** An object $F\in D^b(k_X;\Omega)$ belongs to this weak constructible subcategory if and only if there is an open neighborhood $U$ of $\Omega$ with

\[
 \operatorname{SS}(F)\cap U\subset\Lambda,
 \qquad \Lambda\text{ relatively closed, subanalytic and isotropic in }U.
 \tag{1}
\]

The word isotropic on a region retains vanishing of the canonical one-form $\alpha=\sum\xi_i\,dx_i$ on the subanalytic set. This is the local restriction of the conic isotropy used by the source criterion. We now prove the converse by constructing an actual global weakly constructible model at each $p$. A geometric hypothesis alone does not imply perfect coefficients.

## A compact angular slice produces a global isotropic container

Work in analytic coordinates near $x_0$, identify $x_0=0$, and let $p_0=(0;\xi_0)$ be nonzero. Choose a small compact base ball $\overline B_1$ and a closed angular cone $C'$ around $\xi_0$ so that, with $r_0=|\xi_0|$,

\[
 \overline B_1\times\{\xi\in C':|\xi|=r_0\}\subset U.
 \tag{2}
\]

The compact slice

\[
 \Sigma=\Lambda\cap
 \bigl(\overline B_1\times C'\cap\{ |\xi|=r_0\}\bigr)
 \tag{3}
\]

is subanalytic and compact. Subanalytic subset calculus preserves $\alpha|_\Sigma=0$. Let $A$ be its nonnegative radial image together with the **whole** zero section of the coordinate vector space:

\[
 A=\{(x;s\xi):(x;\xi)\in\Sigma,\ s\geq0\}
       \ \cup\ T^*_{\mathbb R^n}\mathbb R^n.
 \tag{4}
\]

This is a closed conic subanalytic isotropic set. For closedness, a finite-covector limit of the first term has bounded $s$, since $|\xi|=r_0>0$, and compactness of $\Sigma$ provides a convergent preimage. For subanalyticity, restrict $s$ to a bounded interval over any bounded target covector neighborhood and use the proper subanalytic-image theorem. The radial map $m(s,x,\xi)=(x;s\xi)$ satisfies

\[
 m^*\alpha=s\alpha.
 \tag{5}
\]

There is no $ds$ term, since radial change leaves the base point fixed. Analytic detection of vanishing on images therefore proves isotropy of the first term. The zero section is isotropic; finite union preserves it. Adding that zero section is a deliberate containing-set enlargement, not an assertion that positive radial saturation supplies zero covectors over all base points.

Conicity of the original microsupport and (1)–(3) show that $A$ contains every original covector over $\overline B_1$ whose direction lies in $C'$. We need no initial subanalyticity of that original microsupport.

There is also a zero-covector version. If $p_0=(0;0)$, choose $r_0>0$ small and $\overline B_1$ so that the full radius-$r_0$ sphere over that base ball lies in $U$. Use all angular directions in (3). Then (4) contains the **entire** microsupport over $B_1$. The geometric criterion makes $F|_{B_1}$ weakly constructible. A compact supported localization inside $B_1$, described below, gives its global representative. In dimension zero every local bounded coefficient object is already weakly constructible; the same compact extension applies.

## A cone capped by one affine inequality

For the nonzero case choose linear coordinates $(z,t)$ with $\xi_0=-dt$. Choose full-dimensional proper closed polyhedral covector cones $C,C'$ such that

\[
 -dt\in\operatorname{Int}C,\qquad
 C\setminus0\subset\operatorname{Int}C',
 \tag{6}
\]

with the larger cone still satisfying (2). One can take the cones over two nested compact polytopes in the affine section $\xi(\partial_t)=-1$. Shrinking those polytopes around $-dt$ keeps their entire angular closures inside the available neighborhood. Put

\[
 \gamma=(C^a)^\circ,
 \qquad C=(\gamma^\circ)^a,
 \qquad Z=\{t\leq\varepsilon\},\quad\varepsilon>0.
 \tag{7}
\]

The polar is nonnegative: $v\in\gamma$ means $\xi(v)\leq0$ for every $\xi\in C$. The bipolar equality gives the middle identity. The cone $\gamma$ is closed, polyhedral and proper. Since $-dt$ lies in the interior of $C$, $t$ is strictly positive on $\gamma\setminus0$. Compactness of its unit section gives a constant $c>0$ with

\[
 |v|\leq c\,t(v)\qquad(v\in\gamma).
 \tag{8}
\]

Extend the original sheaf from its coordinate chart to $\mathbb R^n$ by ordinary open extension by zero, and continue to call that bounded object $F$. On the smaller ball in (2) it is the original sheaf and has the same controlled microsupport. With source point $x$ and output point $v$, set

\[
 G=R\Gamma_ZF,
 \qquad s(x,v)=x-v,
 \qquad
 T=Rr_{2*}\bigl(s^{-1}k_\gamma\otimes^L r_1^{-1}G\bigr).
 \tag{9}
\]

Here $r_1,r_2$ are the two projections of $\mathbb R^n\times\mathbb R^n$. The ordinary cone-kernel prerequisite identifies $T$ with the cone projector $\phi_\gamma^{-1}R\phi_{\gamma*}G$. It identifies restriction of the kernel to its vertex with the projector counit. Hence the natural arrow

\[
 T\longrightarrow R\Gamma_ZF\longrightarrow F
 \tag{10}
\]

is invertible at $p_0$: the first map is microlocally invertible in $\operatorname{Int}C$, and the second is an ordinary isomorphism near $0\in\operatorname{Int}Z$. The same prerequisite gives

\[
 \operatorname{SS}(T)\subset\mathbb R^n\times C.
 \tag{11}
\]

All objects are bounded by the stated internal-Hom and manifold-operation bounds. The coefficient in (9) has closed support inside

\[
 S=\{(x,v):x-v\in\gamma,\ t(x)\leq\varepsilon\}.
 \tag{12}
\]

Projection $S\to\mathbb R^n_v$ is proper. In fact for $v$ in a compact set, writing $x=v+w$ gives $w\in\gamma$ and $t(w)\leq\varepsilon-t(v)$; (8) bounds $w$ and therefore $x$. Closedness supplies compact inverse images. Furthermore choose $\varepsilon$ small, then an output neighborhood $O$ of zero small, so that

\[
 (x,v)\in S,\ v\in O\quad\Longrightarrow\quad x\in B_0,
 \qquad \overline B_0\subset B_1.
 \tag{13}
\]

Indeed $|x|\leq|v|+c(\varepsilon+|t(v)|)$. The strict margin between $B_0$ and $B_1$ will also contain the base points of every sufficiently late limiting witness.

## The flat boundary keeps all input directions controlled

Put $N=\operatorname{SS}(k_Z)^a$. In the interior of $Z$ it has only zero covectors; at its boundary its nonzero rays are $\lambda\,dt$ with $\lambda\geq0$. There are no covectors over the complement of $Z$. Thus the full internal-Hom estimate gives

\[
 \operatorname{SS}(G)\subset\operatorname{SS}(F)\widehat+N.
 \tag{14}
\]

We claim that, for $x\in B_0$ and nonzero $\xi\in C$,

\[
 (x;\xi)\in\operatorname{SS}(G)
 \quad\Longrightarrow\quad
 (x;\xi)\in A_Z:=A\widehat+N.
 \tag{15}
\]

In a witness for (14), write the source covector as $\sigma_j$ and the second covector as $\lambda_jdt$, permitting $\lambda_j=0$. Then

\[
 \beta_j:=\sigma_j+\lambda_jdt\longrightarrow\xi,
 \qquad
 \sigma_j=\beta_j-\lambda_jdt.
 \tag{16}
\]

Because $C\setminus0\subset\operatorname{Int}C'$, sufficiently late $\beta_j$ lie in $C'$. Both $\beta_j$ and $-dt$ lie in this convex cone, so $\sigma_j\in C'$ for every sufficiently late term, however large $\lambda_j$ becomes. The source base points tend to $x\in B_0$, and therefore lie in $B_1$ eventually. Container (4) contains these actual source covectors. The original base-separation–norm product still tends to zero; we have changed no term of that witness, only its containing set. It is consequently a witness for $A\widehat+N$, proving (15). This argument includes unbounded cancellation at the cap boundary. Inside $Z$ it reduces to the zero second covector.

The geometric limiting-sum theorem makes $A_Z$ closed, conic, subanalytic and isotropic. Introduce the global geometric sets

\[
 B_\gamma=\operatorname{SS}(s^{-1}k_\gamma),
 \qquad J=r_{1d}r_{1\pi}^{-1}A_Z,
 \qquad
 \Xi=(B_\gamma\widehat+J)\cap T^*(\mathbb R^{2n})|_S.
 \tag{17}
\]

The subanalytic polyhedron $\gamma$ has weakly constructible constant coefficients. Analytic submersion pullback makes $B_\gamma$ a closed conic subanalytic isotropic set. Ordinary inverse cotangent transport gives the same properties for $J$: its covectors have the form $(\beta,0)$ over $(x,v)$ with $(x;\beta)\in A_Z$. Limiting-sum isotropy and restriction to the closed subanalytic base set $S$ give these properties for $\Xi$ as well.

The proper direct cotangent image

\[
 L=r_{2\pi}r_{2d}^{-1}\Xi
 \tag{18}
\]

is closed, conic, subanalytic and isotropic. Here the required cotangent properness is checked on its actual incidence: a compact output set of $(v;\xi)$ determines the lifted covector $(x,v;0,\xi)$, while (12) and its properness bound $x$. The incidence is closed, so it is compact. No properness of an unconstrained projection has been assumed.

We now show that $L$ contains the nonzero microsupport of $T$ over $O$. The two factors in (9) are noncharacteristic for tensor product: a kernel covector has form $(\alpha,-\alpha)$, a source covector has form $(\beta,0)$, and their cancellation in both components forces $\alpha=\beta=0$. The noncharacteristic tensor estimate and proper-on-support image estimate therefore give, for a nonzero $(v;\xi)\in\operatorname{SS}(T)$, a common source point $x$ with

\[
 (x,v)\in S,\qquad
 (x;\xi)\in\operatorname{SS}(G),\qquad
 (x,v;-\xi,\xi)\in B_\gamma.
 \tag{19}
\]

By (11), $\xi\in C$, and by (13), $x\in B_0$ whenever $v\in O$. Formula (15) then puts $(x;\xi)$ in $A_Z$. The covector $(x,v;\xi,0)$ lies in $J$. Adding it to the final covector in (19) gives $(x,v;0,\xi)$ in the ordinary sum, hence in $\Xi$. Formula (18) gives $(v;\xi)\in L$. Zero covectors can be included by adjoining the whole output zero section. Thus

\[
 \operatorname{SS}(T|_O)\subset
 (L\cup T^*_{\mathbb R^n}\mathbb R^n)|_O.
 \tag{20}
\]

The right side is a relatively closed conic subanalytic isotropic set. The global geometric criterion on the open analytic manifold $O$ proves that $T|_O$ is weakly R-constructible.

Choose a small closed analytic ball $D_0$ with $0\in\operatorname{Int}D_0$ and $D_0\subset O$, and let $j:O\hookrightarrow X$ be the coordinate inclusion. Define

\[
 F'=j_!R\Gamma_{D_0}(T|_O).
 \tag{21}
\]

The inner object is weakly constructible by subanalytic cutoff and bounded internal-Hom closure. Its closed support is compact inside $O$, so $j$ is proper on that support. Proper weak-image closure makes $F'$ globally weakly R-constructible. The supported counit, restriction of (10), and the ordinary open-extension counit give an actual arrow $F'\to F$. Near zero, the extra supported localization is the identity, so that arrow is a $p_0$-denominator. It is the required global representative. For a zero covector use the weakly constructible restriction obtained after (5) in place of $T|_O$; its compact supported localization maps isomorphically to $F$ on an ordinary neighborhood. This finishes the converse of (1) at every point of an arbitrary $\Omega$.

The outer compact localization in (21) is essential to the global assertion. Local weak constructibility on an open set does not by itself guarantee that extension across its boundary is weakly constructible. Here the closed support lies strictly inside that open set, and the proper-image hypothesis is verified there.

## A constructible contact kernel preserves perfect local models

Let $q_1,q_2:X\times Y\to X,Y$. Retain all hypotheses of the contact-kernel equivalence theorem: a relatively closed conic graph $\Gamma$, its two homeomorphic projections, selected open regions $\Omega_X,\Omega_Y$, union containment of $\operatorname{SS}(K)$ in that graph, and the identity-induced self-microlocal-Hom isomorphism. Write the graph in physical kernel covectors as

\[
 \Gamma=\{(x,y;\xi,-\eta):(x;\xi)=\chi(y;\eta)\}.
 \tag{22}
\]

Assume additionally that $K$ is R-constructible. This implies the cohomological constructibility required by the original theorem, by the costalk/duality result. Its inverse equivalences are

\[
 \Phi_KG=Rq_{1!}(K\otimes^Lq_2^{-1}G),
 \qquad
 \Psi_KF=Rq_{2*}R\mathcal Hom(K,q_1^!F).
 \tag{23}
\]

The extraordinary inverse image in the right operator retains its orientation and dimension normalization. We do not replace it by an unshifted ordinary pullback.

First take a globally R-constructible $G$. The tensor coefficient

\[
 H=K\otimes^Lq_2^{-1}G
 \tag{24}
\]

is R-constructible. It satisfies the microlocally proper projection hypothesis over $\Omega_X$. To see this for a compact output set $T\subset\Omega_X$, choose a compact neighborhood $T'\subset\Omega_X$ of $T$. In a full tensor limiting witness for a covector of $H$ over $T$, the second factor has zero $X$ component. The kernel's $X$ covectors consequently converge to the chosen output covector and eventually lie in $T'$. The proper graph projection in (22) confines both their $Y$ base points and their complete $Y$ covectors to a compact set. In particular all limiting $Y$ base points lie in one compact set, regardless of the total $Y$ covector of $H$ or any cancellation with the second factor. This gives all-fibre-covector compact control; the compact-neighborhood argument from the previous lesson supplies the closure version of projection properness. Its perfect-image theorem makes $\Phi_KG$ pointwise R-constructible on $\Omega_X$.

Next take a globally R-constructible $F$. The coefficient

\[
 H'=R\mathcal Hom(K,q_1^!F)
 \tag{25}
\]

is R-constructible by perfect exceptional inverse image and internal-Hom closure. The full Hom estimate is

\[
 \operatorname{SS}(H')
 \subset \operatorname{SS}(K)^a\widehat+
          \operatorname{SS}(q_1^!F).
 \tag{26}
\]

The second set has zero $Y$ component, because $q_1$ is a submersion and its relative dualizing factor is invertible locally constant. Over a compact set of $Y$ output covectors, the first factor's $Y$ components therefore converge to that compact set. If the physical kernel covector is $(\xi,-\eta)$, its antipode has $Y$ component $\eta$, which is exactly the input coordinate of (22). Properness of the other graph projection confines the $X$ base points and kernel $X$ covectors. Thus (25) is microlocally proper for $q_2$ over $\Omega_Y$, for all total $X$ covectors. The ordinary-image clause of the same theorem proves pointwise perfect constructibility of $\Psi_KF$ there.

Now let $G$ have only the pointwise constructible property on $\Omega_Y$. Fix $p_X\in\Omega_X$ and set $p_Y=\chi^{-1}(p_X)$. Choose a globally R-constructible $G_{p_Y}$ isomorphic to $G$ at $p_Y$. A finite localized fraction representing this isomorphism has two denominator cones missing $p_Y$. Closedness of their microsupports gives an open neighborhood $V\subset\Omega_Y$ where both cones are invisible. The source roof therefore gives an isomorphism in $D^b(k_Y;V)$.

On $\chi(V)$ the kernel graph has no input outside $V$, and its projection is still proper. The already established kernel descent thus applies to these smaller regions. It sends both arrows of that roof to denominators and gives

\[
 \Phi_KG\simeq\Phi_KG_{p_Y}
 \quad\text{in }D^b(k_X;\chi(V)).
 \tag{27}
\]

The globally constructible-input argument after (24) supplies a global perfect constructible representative of the right side at $p_X$, through the compact fibre cutoff of the preceding lesson. Composing the two localized isomorphisms supplies such a representative for the left side. Applying the same roof argument to the inverse graph and (25) proves preservation by $\Psi_K$ for pointwise constructible inputs on $\Omega_X$.

We have proved

\[
 \Phi_K:
 D^b_{\mathrm{R\text{-}c}}(k_Y;\Omega_Y)
 \xrightarrow{\sim}
 D^b_{\mathrm{R\text{-}c}}(k_X;\Omega_X),
 \qquad\text{inverse }\Psi_K.
 \tag{28}
\]

These are full subcategories of the original localized categories. The original unit and counit are isomorphisms; after both preservation arguments their components lie in the two full subcategories and remain isomorphisms there. This proves full faithfulness and essential surjectivity, establishing the asserted restricted equivalence. Perfection came from actual constructible coefficients (24)–(25) and the compact fibre theorem, rather than from isotropy alone. All right-adjoint shifts and orientations remain in the original maps (23).

## Exercises with complete solutions

### Radial saturation retains the canonical-form equation

*Difficulty: Introductory.*

Let $\Sigma$ be a compact subanalytic subset of a radius-$r_0$ sphere bundle, with $r_0>0$ and $\alpha|_\Sigma=0$. Prove closedness and isotropy of its nonnegative radial image. Distinguish its zero section from the enlargement used in (4).

**Solution.** For $m(s,x,\xi)=(x;s\xi)$, the pullback is $m^*\alpha=s\alpha$: only the projected base differential enters, so varying $s$ adds no term. Vanishing pulls back to $[0,\infty)\times\Sigma$, and analytic image detection gives vanishing on its subanalytic image. Locally that image is subanalytic because bounded output norm bounds $s$ by the positive fixed norm $r_0$, making the relevant map proper. The same bound and compactness of $\Sigma$ give convergent preimages of every finite-covector limit; the image is closed. At $s=0$ it contains zero covectors only over the base projection of $\Sigma$. The full zero section in (4) includes the other base points deliberately; each added point has zero canonical form, and the union remains closed and isotropic.

### The cone projector replaces a point by a closed halfline

*Difficulty: Intermediate.*

Assume $k\ne0$. Take $X=\mathbb R$, $p_0=(0;-dt)$, $F=k_{\{0\}}$, $\gamma=[0,\infty)$ and $Z=(-\infty,\varepsilon]$, with $\varepsilon>0$. Compute $G,T$ in (9), the arrow (10) and its cone. Check the sign of its invisible direction.

**Solution.** The source point lies in the interior of $Z$, so $G=F$. In the kernel correspondence the source coordinate is $x=0$ and $x-v\in\gamma$ means $v\leq0$. Projection is a homeomorphism from this support to $(-\infty,0]$, so

\[
 T=k_{(-\infty,0]}.
\]

There is no fibre integration shift. Restriction to the kernel vertex is the closed-point restriction $k_{(-\infty,0]}\to k_{\{0\}}$. The open/closed triangle identifies its cone with $k_{(-\infty,0)}[1]$. The closed left halfline has negative conormal at zero; the open left halfline has positive conormal there. Consequently the cone misses $(0;-dt)$, as required. The projector has selected the negative direction of the point's full conormal. Both source and model are globally constructible in this example.

### An unbounded cap correction stays in the larger cone

*Difficulty: Intermediate.*

In covector coordinates $(a,b)$ for $(z,t)$, use

\[
 C=\{b\leq-2|a|\},\qquad C'=\{b\leq-|a|\},
 \quad \xi=(1,-2).
\]

If $\beta_j\to\xi$ and $\lambda_j\geq0$, prove that $\sigma_j=\beta_j-\lambda_jdt$ lies in $C'$ eventually. Give a genuinely divergent sequence whose base-separation–norm product tends to zero.

**Solution.** The nonzero $\xi$ belongs to the interior of $C'$, so $\beta_j=(a_j,b_j)$ eventually satisfies $b_j\leq-|a_j|$. Subtracting $\lambda_jdt$ replaces $b_j$ by $b_j-\lambda_j$, preserving that inequality for every nonnegative $\lambda_j$. Choose $\beta_j=(1+1/j,-2)$, $\lambda_j=j^2$, so

\[
 \sigma_j=(1+1/j,-2-j^2),\qquad
 \sigma_j+\lambda_jdt=\beta_j\to\xi.
\]

Place their base points at $x_j=(j^{-3},\varepsilon)$ and $z_j=(0,\varepsilon)$, respectively. The second is on the flat cap boundary. The norm of $\sigma_j$ diverges like $j^2$, while

\[
 |x_j-z_j|\,|\sigma_j|=O(j^{-1})\longrightarrow0.
\]

These are valid limiting-sum witness conditions and exhibit cancellation of unbounded covectors. This calculation is a cone/witness test; it does not assert that an arbitrary set of such first covectors is itself isotropic. In the theorem their isotropic container is constructed separately in (3)–(5).

### Zero-covector control proves weak constructibility without finiteness

*Difficulty: Intermediate.*

Over a field, let $M=\bigoplus_{j\geq0}k$ and $F=M_{\mathbb R^n}$. Verify the criterion near a zero covector and give a global weakly constructible representative. Does its geometric control force perfect coefficients?

**Solution.** The microsupport is the zero section, a closed subanalytic isotropic set, so (1) holds near any zero covector and every other covector. The original constant sheaf is already a global weakly constructible representative. Alternatively (21) applied to a compact ball gives a compactly supported weak representative mapping isomorphically to it near the chosen interior point. The stalk $M$ is infinite dimensional, so it is not perfect over the field. In particular at the zero covector no perfect model can be ordinarily locally isomorphic to this stalk. The reverse criterion asserts weak constructibility and supplies no coefficient finiteness. When $n=0$, the same example is simply a bounded coefficient module at a point, which is weakly constructible regardless of its rank.

Any denominator at a zero covector has cone vanishing on an ordinary neighborhood, because zero-section microsupport records closed support. A finite isomorphism roof at that covector therefore gives ordinary local isomorphisms. This justifies the obstruction to a perfect localized model in this example, rather than assuming that all nonzero-covector isomorphisms have that stronger ordinary meaning.

### The outer compact support avoids an accumulating boundary

*Difficulty: Advanced.*

Assume $k\ne0$. On $U=(0,1)$ take the locally finite sheaf $G=\bigoplus_{j\geq2}k_{\{1/j\}}$. Show that it is R-constructible on $U$, whereas its extension by zero to $\mathbb R$ is not weakly R-constructible. Explain the support properness gained by a cutoff inside $U$.

**Solution.** Every compact subset of $U$ contains only finitely many of the points $1/j$. They and the complementary intervals form a locally finite semianalytic stratification, with stalk $k$ at each included point and zero elsewhere. Thus $G$ is R-constructible. Its open extension still has nonzero stalks at all those points and zero stalk at zero. Its closed support is $\{0\}\cup\{1/j:j\geq2\}$, which is not locally subanalytic at zero: arbitrarily small neighborhoods contain infinitely many isolated components. The zero-section base of the microsupport of a weakly constructible sheaf is subanalytic, so this extension cannot be weakly constructible.

For the embedding $U\hookrightarrow\mathbb R$, that original coefficient support is nonproper: the inverse image of a compact interval around zero contains an accumulating sequence with no limit in $U$. A closed ball $D_0$ compactly contained in $U$ meets only finitely many points. Either its ordinary cutoff or supported cutoff has compact closed support inside $U$, and its image under the embedding is proper on that support and constructible. Formula (21) uses exactly this strict interior placement, rather than relying on unrestricted open extension of a local model.

### The identity kernel checks the adjoint orientation shift

*Difficulty: Advanced.*

On oriented lines $X=Y=\mathbb R$, let $K=k_\Delta$ for the diagonal. Compute both operators (23). Verify the physical covector sign and explain the cancellation of the exceptional shift in the right operator.

**Solution.** The diagonal conormal is $(x,x;\xi,-\xi)$, so (22) gives the identity contact map. The two graph projections are homeomorphisms. Tensoring the input pullback with $k_\Delta$ gives its closed pushforward along the diagonal; proper-support projection from that support is a homeomorphism, hence $\Phi_KG=G$.

The projection $q_1$ has an oriented one-dimensional fibre, so $q_1^!F=q_1^{-1}F[1]$. Internal Hom with $k_\Delta$ is $R\Gamma_\Delta(q_1^!F)$. The diagonal's codimension-one exceptional restriction of $q_1^{-1}F$ is $F[-1]$, with its normal orientation line; it is the noncharacteristic submanifold formula, since pullback covectors have zero second component. Its normal orientation cancels the projection's relative orientation under $q_1\Delta=\mathrm{id}$. The shift $[-1]$ cancels $[1]$, giving $R\Gamma_\Delta(q_1^!F)=\Delta_*F$. Ordinary projection then gives $\Psi_KF=F$. This uses the normalized exceptional composition; omitting the fibre shift would produce an incorrect inverse.

### A shifted identity kernel has the oppositely shifted inverse

*Difficulty: Intermediate.*

For any integer $s$, replace the identity kernel by $k_\Delta[s]$. Compute both operators, their unit/counit degrees and the effect on pointwise perfect constructibility.

**Solution.** The tensor kernel shifts the forward operator by $[s]$, so $\Phi G=G[s]$. Internal Hom is contravariant in its first argument, hence shifts the right operator by $[-s]$, giving $\Psi F=F[-s]$. Each composite has total shift zero. The actual adjunction units and counits are therefore the original identity maps under the normalized shifted identifications; there is no new degree in either composite. Both microsupport and perfect-stalk properties are invariant under shifts. A global perfect representative $G_p$ for $G$ becomes $G_p[s]$ for its forward image, and similarly with $[-s]$ for the inverse. The graph and identity-induced directional endomorphism remain unchanged.

### A constructible kernel alone need not preserve perfect local models

*Difficulty: Advanced.*

Let $k$ be a nonzero field, $X=Y=\mathbb R$, $K=k_{\{0\}\times\mathbb R}$ and $G=i_*k_{\mathbb Z}$ for the closed discrete integer inclusion $i:\mathbb Z\hookrightarrow\mathbb R$. Verify that both inputs are R-constructible. Compute $\Phi_KG$ and show that it has no perfect constructible representative at $(0;dx)$. Identify the failed contact hypothesis.

**Solution.** The kernel has constant perfect coefficient $k$ on a closed analytic submanifold. The integer support is locally finite, with perfect point stalks and zero elsewhere, so $G$ is R-constructible. Tensoring restricts the first factor to zero and leaves the discrete input in the second. Compact sections of the discrete set are finite-support tuples and have no higher cohomology. Therefore

\[
 \Phi_KG=k_{\{0\}}\otimes_k V,
 \qquad V=\bigoplus_{m\in\mathbb Z}k.
 \tag{29}
\]

This is weakly constructible, but its nonzero point coefficient is infinite dimensional. The submanifold microlocal-Hom formula gives

\[
 \bigl(\mu\operatorname{hom}(k_{\{0\}},\Phi_KG)\bigr)_{(0;dx)}=V.
\]

If a globally R-constructible representative were isomorphic there, microlocal Hom would invert that isomorphism. Its stalk would be perfect by the perfect microlocal-Hom theorem, since both inputs would be R-constructible. Over the field this contradicts infinite dimensionality of $V$ in degree zero. Hence there is no perfect constructible representative at this covector.

The kernel covectors over a nonzero $X$ normal have arbitrary $Y$ base point and zero $Y$ component. They cannot form the contact graph with proper homeomorphic projection required in (22). The inverse image of that one output covector contains the whole noncompact $Y$ line. Thus constructibility of $K$ and $G$ supplies the coefficient condition for (24), but the missing graph/properness condition prevents application of the perfect localized-image theorem. This is a failure of that hypothesis, not a counterexample to (28).

## References and proof boundaries

Masaki Kashiwara and Pierre Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985), §6.2, Proposition 6.2.2, p. 106, gives the local coefficient-object model when microsupport lies in a smooth conormal; [freely readable PDF](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). Masaki Kashiwara, *Index theorem for constructible sheaves*, Astérisque 130 (1985), §3, Proposition 3.3, p. 198, gives the finite-dimensional field-coefficient version; [free article](https://www.numdam.org/item/AST_1985__130__193_0/). These conormal statements are useful antecedents; the general isotropic cutoff construction and perfect contact argument are supplied by the proof above and its named prerequisites.

For the contact theorem, Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorem 6.3.4 and its proof, imposes the graph, union-of-cotangent-regions, cohomological-constructibility and identity conditions. Its Proposition 8.4.1 treats constructible contact transport. Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §5, Theorem 5.11, is a readable statement of the contact equivalence, not a replacement for the full proof. The present proof keeps the two explicit functors, their unit and counit, and separately proves preservation of perfect coefficients by compact fibre control. The smooth-conormal models cited above alone do not prove the arbitrary isotropic local-model criterion: the complete cone-and-cap construction in this lesson is the additional argument.

The current foundation contracts are [SH02-MST-CUTOFF-FORWARD](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-CUTOFF-FORWARD), [SH02-GAM-KERNEL](../../sheaf-proof-readings/SH02-cone-topology.html#SH02-GAM-KERNEL), [SH02-MO-DIAGONAL](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-DIAGONAL) and [SH02-MO-PROPER-PUSH](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-PROPER-PUSH), SH02-CHE-006, SH02-AE-MICROPROPER and its full sum witness criterion, and [SH02-MC-LOCAL](../../sheaf-proof-readings/SH02-microlocal-categories.html#SH02-MC-LOCAL). The elementary projector statements include both its polar bound and its actual counit; the ordinary kernel realization includes its section/relative-contraction proof and has no arbitrary nonproper closed-fibre base-change assertion. We apply those results to the capped coefficient whose projection is proved proper in (12).

These arguments and eight solved exercises establish the local criterion and contact-preservation statements using the named prerequisites. Isotropic control yields weak constructible models; the perfect contact conclusion also uses perfect coefficient complexes and the stated graph and projection conditions. The sheaf-operation, localization and geometric prerequisites are assumed at their stated scopes.
