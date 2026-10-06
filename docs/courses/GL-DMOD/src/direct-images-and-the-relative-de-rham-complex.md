# Direct images and the relative de Rham complex

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Sending a differential equation to a point is a cohomological operation. On the affine line, the polynomial functions give one copy of the ground field in degree $-1$; a module concentrated at the origin gives one copy in degree $0$. The difference comes from a two-term complex, rather than from the ordinary space of sections. We will construct that complex, prove that direct images compose, and compute a finite map whose direct image has a singular summand.

Throughout, $k$ has characteristic zero. Varieties are smooth, separated and of finite type over $k$, with pure dimensions. For the composition theorem we take them quasi-projective. Modules are left differential-operator modules, quasi-coherent over their structure sheaves. Complexes have cohomological indexing:
\[
H^a(K[b])=H^{a+b}(K).
\]
Write $f_{\mathrm{sh},*}$ for sheaf pushforward and $f_*$ for differential-operator direct image. The inverse-image convention remains $f^!=Lf^*[d_X-d_Y]$. An ordinary tensor product of left modules means the tensor over the structure sheaf, with the diagonal vector-field action; its derived version is denoted $\otimes^L$.

We use the transfer module, chain-rule action and derived transfer composition from [Inverse images](inverse-images.md), the side-changing equivalence from [D-modules, flat connections and local systems](d-modules-flat-connections-and-local-systems.md), and the Spencer argument from [Holonomic D-modules and duality](holonomic-d-modules-and-duality.md). The algebraic-geometric background is quasi-coherent sheaf cohomology, finite affine Čech covers on separated varieties, and proper coherent direct image.

## 1. A definition that remembers both sides

Let $f:X\to Y$. Recall the $(\mathcal D_X,f^{-1}\mathcal D_Y)$-bimodule
\[
T_f=\mathcal D_{X\to Y}
=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_Y. \tag{1.1}
\]
There is a particularly transparent definition on right modules. If $N$ is a right $\mathcal D_X$-complex, set
\[
f_*^rN
=Rf_{\mathrm{sh},*}
\left(N\otimes^L_{\mathcal D_X}T_f\right). \tag{1.2}
\]
The right action of $f^{-1}\mathcal D_Y$ survives the tensor product and induces the right $\mathcal D_Y$-action after pushforward.

For left modules we apply the exact side-changing equivalences
\[
S_X(M)=\omega_X\otimes_{\mathcal O_X}M,
\qquad
S_Y^{-1}(N)=N\otimes_{\mathcal O_Y}\omega_Y^{-1}.
\]
In particular,
\[
f_*M=S_Y^{-1}f_*^rS_X(M). \tag{1.3}
\]
Equivalently, side-changing both actions of $T_f$ gives the $(f^{-1}\mathcal D_Y,\mathcal D_X)$-bimodule
\[
\mathcal D_{Y\leftarrow X}
=\omega_X\otimes_{\mathcal O_X}T_f
 \otimes_{f^{-1}\mathcal O_Y}f^{-1}\omega_Y^{-1},
\]
and
\[
f_*M
=Rf_{\mathrm{sh},*}
\left(\mathcal D_{Y\leftarrow X}
\otimes^L_{\mathcal D_X}M\right). \tag{1.4}
\]
The two differential-operator actions in this expression include transposition. For example, with a local volume form $\eta$, a vector field $\xi$ acts on $S_X(M)$ on the right by
\[
(\eta\otimes m)\xi
=-\mathcal L_\xi\eta\otimes m-\eta\otimes\xi m.
\]
Thus the factors of $\omega$ determine actual actions, as well as line-bundle twists.

The identity map has $T_{\mathrm{id}}=\mathcal D_X$, so its direct image is the identity. There is no additional dimension shift in (1.2) or (1.4). The shifts in later computations arise from resolutions of the transfer module.

These formulas define triangulated functors on bounded quasi-coherent complexes. Locally the rings of differential operators have finite homological dimension: the filtered resolution argument using the regular symbol ring, established in the duality lesson, bounds their flat dimension by $2d_X$. A finite affine cover bounds sheaf cohomology. Hence the derived tensors and pushforwards here have finite amplitude. Quasi-coherence can be checked using resolutions by induced right modules $F\otimes_{\mathcal O_X}\mathcal D_X$: their transferred terms are
\[
F\otimes_{\mathcal O_X}T_f
=F\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_Y.
\]
Their sheaf cohomology on affine pieces is computed by quasi-coherent terms. Finite Čech totalizations and the bounded cohomological amplitude then give quasi-coherent cohomology on $Y$. This does not assert coherence for an arbitrary nonproper map.

## 2. Integration along a product

Let $p:W=X\times Y\to Y$, and put $r=d_X$. Define the unshifted relative de Rham complex of a left module $M$ by
\[
\operatorname{DR}_{W/Y}^{\,0}(M)
=\left[
M\longrightarrow\Omega^1_{W/Y}\otimes M
\longrightarrow\cdots\longrightarrow\Omega^r_{W/Y}\otimes M
\right], \tag{2.1}
\]
in degrees $0,\ldots,r$. For a relative form $\alpha$ of degree $a$, its differential is
\[
d_M(\alpha\otimes m)
=d_{\mathrm{rel}}\alpha\otimes m
+(-1)^a\alpha\wedge\nabla_{\mathrm{rel}}m. \tag{2.2}
\]
This is independent of how a tensor is written: the coefficient derivatives on both sides of the tensor relation agree by Leibniz. Flatness of the vector-field action gives $d_M^2=0$.

The product gives canonical horizontal vector fields coming from $Y$. They act on the coefficients of forms and on $M$, and commute with $d_M$. Consequently (2.1) is a complex of $p^{-1}\mathcal D_Y$-modules.

**Theorem 2.1.** There is a natural isomorphism
\[
p_*M\simeq
Rp_{\mathrm{sh},*}\operatorname{DR}_{W/Y}^{\,0}(M)[r]. \tag{2.3}
\]
It holds for bounded quasi-coherent complexes, using total complexes.

**Proof.** Write $T_{\mathrm{rel}}=T_{W/Y}$. The relative Spencer complex has terms
\[
\mathcal D_W\otimes_{\mathcal O_W}\bigwedge^jT_{\mathrm{rel}}
\quad\text{in degree }-j.
\]
It augments to $T_p$ by sending $P$ to $P(1\otimes1)$. Its differential is
\[
\begin{aligned}
\delta(P\otimes\xi_1\wedge\cdots\wedge\xi_j)
={}&\sum_{a=1}^j(-1)^{a-1}P\xi_a\otimes
 \xi_1\wedge\cdots\widehat{\xi_a}\cdots\wedge\xi_j\\
&+\sum_{a<b}(-1)^{a+b}P\otimes
 [\xi_a,\xi_b]\wedge
 \xi_1\wedge\cdots\widehat{\xi_a}\cdots
 \widehat{\xi_b}\cdots\wedge\xi_j .
\end{aligned} \tag{2.4}
\]
The bracket term makes this formula compatible with changes of vector fields and ensures $\delta^2=0$.

In product étale coordinates $(x_1,\ldots,x_r;y_1,\ldots,y_s)$, the transfer module is the quotient of $\mathcal D_W$ by the left ideal generated by the vertical derivatives $\partial_{x_i}$. PBW identifies its elements with operators in the $y$-derivatives with coefficients on $W$. Filter the degree $-j$ term by operators of order at most $q-j$. The associated graded complex is the Koszul complex of
\[
\xi_{x_1},\ldots,\xi_{x_r}
\]
in the polynomial symbol algebra. These are a regular sequence, and its quotient is the symbol module of $T_p$. Therefore the augmented graded complex is exact. A cycle of finite filtration degree can be corrected by a boundary with the same leading symbol; repeating lowers the filtration degree until the cycle vanishes. This proves exactness of the original augmented complex. Its terms are locally free left $\mathcal D_W$-modules, so it computes the derived tensor in (1.2).

Tensor with $N=S_W(M)$ on the right. Since
\[
\omega_W=\omega_{W/Y}\otimes p^*\omega_Y,
\]
side-changing on $Y$ leaves the terms
\[
\omega_{W/Y}\otimes M\otimes\bigwedge^jT_{\mathrm{rel}}.
\]
Contraction identifies these with $\Omega^{r-j}_{W/Y}\otimes M$. To fix signs explicitly, multiply the contraction
$\iota_{\xi_j}\cdots\iota_{\xi_1}\eta$ by
$(-1)^{j(r-1)+\binom j2}$. With the usual shifted-complex differential, (2.4) becomes the differential of (2.1)$[r]$. The right action on a volume form supplies the coefficient-divergence terms in $d_{\mathrm{rel}}\alpha$. All identifications commute with horizontal $Y$-operators. Applying $Rp_{\mathrm{sh},*}$ proves (2.3). ∎

For the map $p:X\to\operatorname{Spec}k$, this specializes to
\[
p_*M=R\Gamma\!\left(X,\operatorname{DR}_{X/k}^{\,0}(M)\right)[d_X].
\tag{2.5}
\]
The de Rham differential is $k$-linear and usually not $\mathcal O_X$-linear. Its individual terms are quasi-coherent, so an affine cover still computes its hypercohomology term by term. On an affine variety, global sections of those terms suffice. This is the same acyclicity mechanism as [Stacks, Tag 0FLW](https://stacks.math.columbia.edu/tag/0FLW).

### Three degree checks

On $\mathbb A^1$, the complex for $\mathcal O$ is
\[
k[x]\xrightarrow{\,d/dx\,}k[x],
\qquad\text{in degrees }-1,0.
\]
Its kernel is $k$, and integration of each monomial proves surjectivity in characteristic zero. Hence
\[
p_*\mathcal O_{\mathbb A^1}=k[1]. \tag{2.6}
\]

For $\delta_0=A_1/A_1x=k[\partial]v$, the same complex has differential multiplication by $\partial$. It is injective and has cokernel $kv$. Thus
\[
p_*\delta_0=k. \tag{2.7}
\]

For $\mathbb P^1$, use the two affine charts with coordinates $x$ and $w=x^{-1}$. The Čech calculation gives
\[
H^0(\mathcal O)=k,\quad H^1(\mathcal O)=0,\quad
H^0(\Omega^1)=0,\quad H^1(\Omega^1)=k[dx/x].
\]
Indeed the last group is
\[
\frac{k[x,x^{-1}]\,dx}
 {k[x]\,dx+x^{-2}k[x^{-1}]\,dx},
\]
and precisely the monomial $x^{-1}dx$ survives. The other three assertions follow from intersections and sums of the corresponding polynomial spaces. The de Rham hypercohomology therefore has $k$ in degrees $0,2$ and vanishes elsewhere. Every complex of vector spaces splits as its cohomology, by choosing complements to boundaries and cycles. After shifting by $1$,
\[
p_*\mathcal O_{\mathbb P^1}\simeq k[1]\oplus k[-1]. \tag{2.8}
\]
The displayed splitting as a complex need not be chosen canonically.

## 3. Embeddings: normal derivatives and localization

**Proposition 3.1.** Direct image along a smooth closed embedding $i:Z\hookrightarrow W$ is exact on modules. In adapted coordinates, with normal equations $t_1,\ldots,t_c$,
\[
i_*M\simeq
i_{\mathrm{sh},*}\bigl(M\otimes_k k[\partial_{t_1},\ldots,\partial_{t_c}]\bigr).
\tag{3.1}
\]
This local expression depends on the chosen coordinates and volume forms.

**Proof.** PBW gives the forward transfer module as a free left $\mathcal D_Z$-module with basis the normal derivative monomials. Equivalently, after side-changing, the backward transfer module is free as a right $\mathcal D_Z$-module with that basis. Derived tensor consequently has no higher Tor. Sheaf pushforward for a closed embedding is exact, proving the assertion.

In the resulting left-module normal form, tangent operators act on $M$ and normal derivatives multiply their polynomial variables. Normal coordinates act by
\[
t_a(m\otimes\partial_t^\alpha)
=-\alpha_a\,m\otimes\partial_t^{\alpha-e_a}. \tag{3.2}
\]
These operators satisfy $[\partial_{t_a},t_b]=\delta_{ab}$. Functions of the normal coordinates act by their finite Taylor expansion on each vector, since the normal coordinates lower polynomial degree. This verifies the coordinate description and its support on $Z$. The global gluing is the transfer construction, including its density twists. ∎

For the origin in the line, (3.1) gives $i_*k=\delta_0$. Together with (2.7), it already shows that pushing the origin to the line and then to a point gives the identity.

**Proposition 3.2.** For an open embedding $j:U\hookrightarrow W$,
\[
j_*M=Rj_{\mathrm{sh},*}M. \tag{3.3}
\]
The right side carries the natural $\mathcal D_W$-action.

**Proof.** Restriction of $\mathcal D_W$ to $U$ is $\mathcal D_U$, so both forward and backward transfer reduce to $\mathcal D_U$. Derived tensor with this identity bimodule does nothing. On an affine open subset of $W$, a finite affine cover of its intersection with $U$ computes the pushforward by a Čech complex. Ambient differential operators restrict to every term and commute with the Čech differential. This constructs the indicated action. ∎

If $j$ is affine, its higher direct images of quasi-coherent modules vanish. For instance, the punctured-line embedding gives
\[
j_*\mathcal O_{\mathbb G_m}=k[x,x^{-1}]
\]
with ordinary differentiation, in degree zero. A general open embedding need not be affine or exact; Exercise 8.6 computes the first higher direct image for the punctured plane.

## 4. Why successive integrations compose

**Theorem 4.1.** For maps $X\xrightarrow fY\xrightarrow gZ$ of smooth quasi-projective varieties, there is a natural isomorphism
\[
(gf)_*\simeq g_*f_*. \tag{4.1}
\]
The isomorphisms agree for three successive maps.

We first justify the tensor-pushforward interchange used in the proof. Let
\[
A=N\otimes^L_{\mathcal D_X}T_f,\qquad B=T_g,
\]
where $N$ is a bounded quasi-coherent right-module complex. Then
\[
Rf_{\mathrm{sh},*}A\otimes^L_{\mathcal D_Y}B
\ \simeq\
Rf_{\mathrm{sh},*}
\left(A\otimes^L_{f^{-1}\mathcal D_Y}f^{-1}B\right). \tag{4.2}
\]
Here is a resolution proof that keeps track of the needed hypotheses. The question is local on $Y$, so take $Y$ affine. Quasi-coherent $\mathcal D_Y$-modules on an affine smooth variety are the sheafifications of modules over $\Gamma(Y,\mathcal D_Y)$: the structure-sheaf equivalence respects the vector-field action and its relations. The finite homological-dimension bound permits a bounded resolution of $B$ by possibly infinitely generated free modules, with a projective last term. A projective term is a direct summand of a free term.

Choose an induced flat resolution of $N$ on affine pieces of $f^{-1}Y$ and a finite affine Čech cover. After tensoring with $T_f$, its terms are quasi-coherent $\mathcal O_X$-modules of the form $F\otimes_{\mathcal O_X}T_f$. The differential need not be $\mathcal O_X$-linear, but every term is acyclic on the affine intersections. This double complex computes $Rf_{\mathrm{sh},*}A$. On each affine intersection, sections of a quasi-coherent module commute with arbitrary direct sums; the cover is finite. Thus this particular derived pushforward commutes with the direct sums used by the free resolution. For a free term $B=\mathcal D_Y^{(I)}$, both sides of (4.2) are the same direct sum of copies of $Rf_{\mathrm{sh},*}A$. The map is therefore an isomorphism for free terms, their direct summands, and bounded complexes of those terms. This proves (4.2). The construction is compatible with restrictions on $Y$, so the local isomorphisms glue.

The induced resolutions used here can be obtained by surjecting induced modules onto $N$ and resolving their coefficient sheaves by flat quasi-coherent sheaves. Equivalently, one can use free differential-operator resolutions on the affine pieces and their Čech totalization. Quasi-projectivity supplies the usual quasi-coherent resolutions; finite homological and Čech dimensions ensure that the totalizations compute bounded derived objects. The argument makes no claim that arbitrary sheaf pushforwards commute with infinite direct sums.

**Proof of the theorem.** The derived forward-transfer identity from the inverse-image lesson is
\[
T_f\otimes^L_{f^{-1}\mathcal D_Y}f^{-1}T_g
\simeq T_{gf}. \tag{4.3}
\]
Recall its acyclicity point: $T_g$ is locally free over $\mathcal O_Y$ by PBW on $Z$. A $\mathcal D_Y$-flat resolution is also $\mathcal O_Y$-flat. Hence the left side has underlying derived structure-sheaf tensor
$\mathcal O_X\otimes^L_{f^{-1}\mathcal O_Y}f^{-1}T_g$, whose higher Tor vanishes, even if $f$ is nonflat. The underived identification follows from the chain rule and tensor associativity.

For a right module complex $N$, substitute (4.2) and (4.3) into the definition:
\[
\begin{aligned}
g_*^rf_*^rN
&\simeq Rg_{\mathrm{sh},*}Rf_{\mathrm{sh},*}
 \left(N\otimes^L_{\mathcal D_X}T_f
 \otimes^L_{f^{-1}\mathcal D_Y}f^{-1}T_g\right)\\
&\simeq R(gf)_{\mathrm{sh},*}
 \left(N\otimes^L_{\mathcal D_X}T_{gf}\right)
=(gf)_*^rN.
\end{aligned}
\]
Derived sheaf pushforwards compose: inverse image of sheaves is exact, so its right-adjoint pushforward preserves injectives; alternatively an acyclic resolution gives the same comparison. Side-changing at $X,Y,Z$ cancels the middle equivalences and proves (4.1). For three maps, the chain-rule transfer identifications and the derived tensor and pushforward associativity maps give the same map from either parenthesization. ∎

For computation, every $f:X\to Y$ has the graph factorization
\[
X\xrightarrow{\ \Gamma_f\ }X\times Y\xrightarrow{\ p\ }Y. \tag{4.4}
\]
The graph is closed because $Y$ is separated. Its direct image is exact by Proposition 3.1; the projection is computed by Theorem 2.1. A projective morphism also admits a closed embedding into $\mathbb P^N\times Y$. For a general quasi-projective morphism, the corresponding immersion into a projective product may only be locally closed, so an open-embedding step must then be retained.

For affine $f$, the induced flat resolution in the preceding proof has no positive-degree terms, and its transferred terms are quasi-coherent on $X$. Affine sheaf pushforward is exact on those terms. Thus a module in degree zero has
\[
H^a(f_*M)=0\quad(a>0). \tag{4.5}
\]
Negative cohomology can remain, as (2.6) shows. With the convention that “right $t$-exact” means preservation of complexes in degrees $\leq0$, (4.5) gives that property; it does not give exactness on modules.

## 5. A branched cover, including its singular extension

Let $f:\mathbb A_z^1\to\mathbb A_t^1$ be $t=z^2$. We compute its entire direct image, including the point over $0$:
\[
f_*\mathcal O_{\mathbb A_z^1}
\simeq
\mathcal O_{\mathbb A_t^1}\oplus
\frac{A_t}{A_t(t\partial_t+\tfrac12)}. \tag{5.1}
\]
The second summand is also the Laurent rank-one connection
\[
E_{-1/2}=k[t,t^{-1}]b,\qquad
\partial_tb=-\frac{1}{2t}b.
\]
The equivalence of these two descriptions for a nonintegral Euler exponent was proved in the inverse-image lesson.

Here is an explicit calculation. Use graph coordinates $(z,t)$, let $u$ denote the normal derivative $\partial_t$, and let $v$ be the graph generator. Proposition 3.1 gives its underlying space as $k[z,u]v$. The operators are
\[
\partial_t=u,\qquad
t=z^2-\partial_u,\qquad
\partial_z=\partial_z^{\mathrm{coeff}}-2zu. \tag{5.2}
\]
These formulas follow by putting the normal equation $t-z^2=0$: the tangent vector field $\partial_z+2z\partial_t$ annihilates $v$, and the normal coordinate acts as $-\partial_u$. They satisfy the two Weyl relations and all cross commutators.

The graph factorization and the relative de Rham complex give
\[
k[z,u]\xrightarrow{\,L=\partial_z^{\mathrm{coeff}}-2zu\,}k[z,u],
\quad\text{in degrees }-1,0. \tag{5.3}
\]
The target corresponds to forms with factor $dz$. If a nonzero polynomial has highest $u$-degree $b$, the highest-degree term of its image is $-2zu^{b+1}$ times its nonzero leading coefficient. Hence $\ker L=0$.

In the cokernel, write $e_a=[z^a dz]$. The relations are
\[
2u[z^{a+1}u^b dz]=a[z^{a-1}u^b dz],
\qquad a,b\geq0, \tag{5.4}
\]
where the right side is zero for $a=0$. Since $e_{a+2}=te_a$, the cokernel is generated over $A_t$ by $e_0,e_1$. The first two instances of (5.4) give
\[
\partial_te_1=0,\qquad
(2t\partial_t+1)e_0=0. \tag{5.5}
\]
Therefore $\mathcal O_t\oplus A_t/A_t(t\partial_t+\tfrac12)$ surjects onto this cokernel.

To prove that there are no additional relations, define a map in the other direction by
\[
[z^{2r+1}u^b dz]\longmapsto
\partial_t^b(t^r a),\qquad
[z^{2r}u^b dz]\longmapsto
\partial_t^b(t^r b_0), \tag{5.6}
\]
where $\partial_ta=0$ and $\partial_tb_0=-b_0/(2t)$. The relations (5.4) map to zero: for even $a=2r$ this is the derivative of $t^r a$, and for odd $a=2r+1$ it is
$2\partial_t(t^{r+1}b_0)=(2r+1)t^r b_0$. Formula $t=z^2-\partial_u$ ensures that (5.6) also respects $t$; it plainly respects $\partial_t$. The images of $e_1,e_0$ are $a,b_0$, so the map is inverse to the preceding surjection. This proves (5.1), concentrated in degree zero.

The deck involution $z\mapsto-z$ acts on $dz$ by $-1$. Thus $e_1$ is invariant and $e_0$ is anti-invariant. Over $\mathbb C$ the anti-invariant summand has monodromy $-1$ around $t=0$, since a horizontal coefficient for $E_{-1/2}$ is $t^{1/2}$. On the punctured line one may instead use the function $z$, whose exponent is $+1/2$; multiplying the Laurent generator by $t$ changes the exponent by $1$. Formula (5.1) fixes the extension across zero, which the punctured computation alone would leave unspecified.

## 6. Relative cohomology acquires the Gauss–Manin connection

Let $f:X\to Y$ be smooth of relative dimension $r$. The relative Spencer resolution used above works locally in smooth adapted coordinates. Its symbol differential is again the Koszul differential in the vertical cotangent variables. The same filtration proof consequently identifies the underlying derived $\mathcal O_Y$-object as
\[
f_*\mathcal O_X\simeq Rf_{\mathrm{sh},*}\Omega^\bullet_{X/Y}[r],
\qquad
H^a(f_*\mathcal O_X)=\mathcal H^{a+r}_{dR}(X/Y). \tag{6.1}
\]
Unlike a product, a smooth map has no preferred global horizontal lifts. Accordingly, the relative de Rham terms need not carry individually chosen $\mathcal D_Y$-actions. The transfer construction gives an action on the derived image; we now identify its action on cohomology.

**Theorem 6.1.** The action on $\mathcal H^q_{dR}(X/Y)$ is the Gauss–Manin integrable connection. If $f$ is also proper, these sheaves are finite locally free on $Y$.

**Proof.** Filter the absolute de Rham complex $\Omega^\bullet_{X/k}$ by the number of factors pulled back from $\Omega^1_{Y/k}$. Smoothness gives the locally split cotangent sequence, hence
\[
\operatorname{gr}^p_F\Omega^\bullet_{X/k}
\simeq f^*\Omega^p_{Y/k}\otimes\Omega^\bullet_{X/Y}[-p]. \tag{6.2}
\]
The absolute differential preserves the filtration. A finite affine Čech cover can be used throughout; each quotient has quasi-coherent terms. Since $\Omega_Y^p$ is locally free, its tensor commutes with this computation and with cohomology. The first page of the filtered complex is therefore
\[
E_1^{p,q}=\Omega_Y^p\otimes\mathcal H^q_{dR}(X/Y).
\]
Its differential $d_1^{0,q}$ defines $\nabla$. Equivalently, it is the connecting map for the first two filtration layers, with the $[-1]$ in (6.2) accounting for the connecting-map degree.

Take a relative cocycle and lift it to the absolute Čech de Rham complex modulo $F^2$. Its total differential has one base differential and represents $\nabla$ of the class. Changing the lift changes this representative by a boundary. For a local function $h$ on $Y$,
\[
d(f^*h\,\widetilde\alpha)
=f^*(dh)\wedge\widetilde\alpha+f^*h\,d\widetilde\alpha.
\]
Projection to the first layer gives
$\nabla(hs)=dh\otimes s+h\nabla s$. On a base $p$-form, the same calculation identifies $d_1$ with the usual exterior extension of this connection. Since $d_1^2=0$ in the spectral sequence, $\nabla^2=0$.

For comparison with transfer, lift a vector field $\xi$ on $Y$ locally to a field $\widetilde\xi$ on $X$. Contracting the first-layer differential with $\xi$ gives the action of $\mathcal L_{\widetilde\xi}$ on relative cocycles. Two lifts differ by a vertical field $v$, whose action is homotopic to zero:
\[
\mathcal L_v=d_{\mathrm{rel}}\iota_v+\iota_vd_{\mathrm{rel}}.
\]
The relative Spencer resolution implements exactly these lifted operators and these homotopies. In adapted coordinates this is immediate from its differential: a vertical derivative is a null-homotopic action, while a horizontal derivative acts by differentiating the relative complex. The absolute filtration glues this local description. Thus the connection just constructed is the canonical differential-operator action in (6.1).

If $f$ is proper, proper coherent direct image applied to each finite locally free $\Omega^p_{X/Y}$, and the bounded hypercohomology spectral sequence, makes $\mathcal H^q_{dR}(X/Y)$ coherent over $\mathcal O_Y$. A coherent module with an integrable connection on a smooth characteristic-zero variety is locally free, by the connection theorem in the second lesson. This proves finite local freeness without using degeneration of a Hodge spectral sequence. ∎

The filtration construction is the one underlying [Stacks, Tag 0FMM](https://stacks.math.columbia.edu/tag/0FMM) and the [Gauss–Manin remark, Tag 0FMN](https://stacks.math.columbia.edu/tag/0FMN); proper coherence is [Tag 0FLY](https://stacks.math.columbia.edu/tag/0FLY). Smoothness alone supplies the connection. Properness supplies the finiteness asserted here.

### The Legendre family: a stated geometric example

Over $\mathbb C$, let $E\to B=\mathbb A^1\setminus\{0,1\}$ be the smooth projective family with affine equation
$y^2=x(x-1)(x-\lambda)$. Its middle direct-image module is the rank-two Gauss–Manin bundle. Set $\omega=[dx/y]$ and $\eta=\nabla_{\partial_\lambda}\omega$. The geometric identification of these as a basis is stated here. The connection is described by
\[
\nabla_{\partial_\lambda}\omega=\eta,\qquad
\lambda(1-\lambda)\nabla_{\partial_\lambda}\eta
=(2\lambda-1)\eta+\tfrac14\omega. \tag{6.3}
\]
Consequently a locally transported period $F(\lambda)$ of $dx/y$ satisfies
\[
\lambda(1-\lambda)F''+(1-2\lambda)F'-\tfrac14F=0. \tag{6.4}
\]
These assertions are the Legendre computation in Daniel Litt, [*Variation of Hodge Structures*, §1.4.2, pp. 9–10](https://virtualmath1.stanford.edu/~conrad/shimsem/2013Notes/Littvhs.pdf). They describe $H^0(f_*\mathcal O_E)=\mathcal H^1_{dR}(E/B)$ under the relative-dimension shift in (6.1).

## 7. Exercises and complete solutions

### Exercise 8.1 — affine space (easy)

Compute the direct image of $\mathcal O_{\mathbb A^n}$ to a point, including the degree.

**Solution.** The polynomial de Rham complex is the tensor product over $k$ of $n$ copies of $k[x]\to k[x]dx$. In each factor, every positive-degree monomial one-form is the derivative of its polynomial antiderivative, including the constant one-form; the only kernel consists of constants. More explicitly, decompose a factor into $k$ in degree zero and the two-term isomorphism from $xk[x]$ to $k[x]dx$. The latter is contractible by polynomial integration. Tensoring these decompositions leaves only the constants as cohomology in degree zero; every other summand is contractible. Formula (2.5) shifts by $n$. The answer is $k[n]$, with $H^{-n}=k$ and all other cohomology zero. This includes $n=0$.

### Exercise 8.2 — a point and its ambient line (easy)

Let $i:\operatorname{Spec}k\to\mathbb A^1$ be the origin and $p:\mathbb A^1\to\operatorname{Spec}k$. Prove $p_*i_*=\mathrm{id}$ directly.

**Solution.** For a vector space $V$, Proposition 3.1 gives $i_*V=k[\partial]\otimes V$. Its direct image to the point is the two-term complex with differential $\partial$, in degrees $-1,0$. The derivative polynomial variable acts injectively, and the quotient is $V$, by evaluation at $\partial=0$. This evaluation defines a natural quasi-isomorphism to $V$ in degree zero. For complexes $V$, use the same degreewise maps and totalize; the positive powers of $\partial$ give a contractible complementary complex. Thus the resulting functor is naturally the identity, agreeing with Theorem 4.1 and $pi=\mathrm{id}$.

### Exercise 8.3 — projection formula and the shift (medium)

For $p:X\times Y\to Y$, prove the projection formula. State it for derived tensor products and explain its unshifted tensor version when $N$ is a finite-rank connection on $Y$. Replace $p^*$ by $p^!$ and track the change.

**Solution.** Because $p$ is smooth, $Lp^*=p^*$ on modules. Resolve a bounded quasi-coherent $N$ by $\mathcal O_Y$-flat differential-operator modules; induced flat modules provide such resolutions. The vertical fields act trivially on the pulled-back factor except for their derivative on structure-sheaf coefficients. Consequently the balanced relative differential gives a natural identification
\[
\operatorname{DR}^{\,0}_{W/Y}(p^*N\otimes^L M)
\simeq p^*N\otimes^L\operatorname{DR}^{\,0}_{W/Y}(M). \tag{7.1}
\]
On an affine open of $Y$, a finite affine Čech cover of $X\times Y$ computes pushforward of the terms on the right. For an $\mathcal O_Y$-free resolution term, taking sections and tensoring agree, including arbitrary free direct sums. Direct summands give flat projective terms; bounded flat dimension over the smooth base and finite Čech dimension justify totalization. Thus the usual tensor-pushforward map is a quasi-isomorphism. It respects $Y$-derivatives by the diagonal Leibniz rule. Apply (2.3) to obtain
\[
p_*(p^*N\otimes^L M)\simeq N\otimes^L p_*M. \tag{7.2}
\]
If $N$ is a finite-rank connection, it is locally free over $\mathcal O_Y$. The derived tensors involving $N$ are ordinary tensors; no further shift occurs. For $r=d_X$, $p^!N=p^*N[r]$, so instead
\[
p_*(p^!N\otimes^L M)\simeq(N\otimes^L p_*M)[r]. \tag{7.3}
\]
This is the dimension shift required by the chosen inverse-image convention.

### Exercise 8.4 — the two square-root summands (medium)

Decompose the direct image of $\mathcal O$ under $z\mapsto z^2$. Identify the deck action and the connection on the punctured target.

**Solution.** The graph module has operators (5.2), and its projection is (5.3). The highest $u$-degree argument gives zero kernel. In the cokernel, $e_1=[z\,dz]$ is killed by $\partial_t$, whereas $e_0=[dz]$ is killed by $t\partial_t+\tfrac12$. They generate since $e_{a+2}=te_a$. Map these vectors to $a$ in $k[t]a$ and $b$ in $k[t,t^{-1}]b$, with $\partial_ta=0$ and $\partial_tb=-b/(2t)$. The formula (5.6) kills every relation and supplies an inverse. Hence the direct image is exactly $\mathcal O_t\oplus E_{-1/2}$, with no other cohomology. The involution changes both $z$ and $dz$ by a sign, so the first generator is invariant and the second anti-invariant. On $t\ne0$, $tb$ has exponent $+1/2$ and corresponds to the square-root function. Both gauges have monodromy $-1$ over $\mathbb C$. This identifies the entire extension, not only its generic rank.

### Exercise 8.5 — an irregular exponential (hard)

Let $M=k[x]e$ with $\partial e=3x^2e$. Compute $H^0(p_*M)$ for $p:\mathbb A^1\to\operatorname{Spec}k$, and compare it with the trivial connection.

**Solution.** The differential in the shifted de Rham complex is
\[
L(g)=g'+3x^2g.
\]
For nonzero $g$ of degree $m$, $L(g)$ has degree $m+2$ with leading coefficient three times that of $g$. Thus $L$ is injective. In its cokernel,
\[
[x^{r+2}]=-\frac r3[x^{r-1}]\quad(r\geq0),
\]
with $[x^2]=0$ when $r=0$. Induction reduces every polynomial class to a linear combination of $[1],[x]$. No nonzero linear polynomial lies in the image of $L$, by the leading-degree argument. Therefore
\[
H^0(p_*M)=k\,\overline1\oplus k\,\overline x,\qquad H^{-1}(p_*M)=0,
\]
where the overlines denote polynomial classes. Its dimension is $2$. For the trivial connection, $H^0p_*\mathcal O=0$ and $H^{-1}p_*\mathcal O=k$. Over $\mathbb C$ the exponential has an irregular singularity at infinity: putting $w=x^{-1}$ makes its connection term $3x^2dx=-3w^{-4}dw$. The additional middle cohomology is compatible with this irregular behavior. No bound for all regular modules on arbitrary open curves is inferred from this comparison.

### Exercise 8.6 — a higher open direct image (medium)

Let $j:\mathbb A^2\setminus\{0\}\hookrightarrow\mathbb A^2$. Compute $R^1j_{\mathrm{sh},*}\mathcal O$ on the affine target and identify its differential-operator module.

**Solution.** Cover the punctured plane by $D(x)$ and $D(y)$. The first Čech cohomology is
\[
\frac{k[x,x^{-1},y,y^{-1}]}
 {k[x,x^{-1},y]+k[x,y,y^{-1}]}. \tag{7.4}
\]
Its basis consists of the classes $x^{-a}y^{-b}$ with $a,b\geq1$. The zeroth cohomology is the intersection of the two localization rings, namely $k[x,y]$. No higher Čech degrees occur. The class $v=[x^{-1}y^{-1}]$ is killed by $x$ and $y$, and
\[
\partial_x^r\partial_y^sv
=(-1)^{r+s}r!s!\,[x^{-r-1}y^{-s-1}].
\]
These vectors form a basis, so (7.4) is $A_2/(A_2x+A_2y)=\delta_0$. Proposition 3.2 consequently gives $H^0(j_*\mathcal O)=\mathcal O_{\mathbb A^2}$ and $H^1(j_*\mathcal O)=\delta_0$. This open direct image is not exact.

## What this lesson does not prove

The identification of the Legendre middle cohomology as a rank-two bundle with the cyclic basis $\omega,\nabla_{\partial_\lambda}\omega$, and its explicit Picard–Fuchs relation, is stated from Litt, §1.4.2, pp. 9–10. The passage from transported algebraic classes to analytic period integrals uses the de Rham comparison described there and will be treated as part of the analytic background to the de Rham and Riemann–Hilbert lessons.

We have not used or proved the general theorem that direct images preserve holonomicity. Nor does the construction alone prove coherent direct image for every proper differential-operator module. Those general finiteness statements belong to later lessons. Proper coherence for ordinary coherent sheaves, used in Theorem 6.1, is an algebraic-geometric prerequisite.

## References

The definitions and ordinary de Rham cohomology conventions are in [Stacks, Tag 0FL6](https://stacks.math.columbia.edu/tag/0FL6), with affine computation in Tag 0FLW, proper relative coherence in Tag 0FLY, and the smooth filtration in Tags 0FMM–0FMN.

Beilinson and Drinfeld, [*Quantization of Hitchin’s integrable system and Hecke eigensheaves*, §§7.2.8–7.2.11](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), use right modules and an equivalent de Rham-complex formalism; §7.2.10 gives the transfer direct image. Transfer modules and direct images of D-modules are also treated in V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf).

Christian Schnell, [*D-modules*, Lecture 17, Examples 17.4–17.7 and Proposition 17.8, pp. 85–88](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), treats embeddings, Spencer computation and composition. Victor Ginzburg, [*Lectures on D-modules*, §§3.2.10–3.2.17](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), explains the density twist and normal derivative description for closed embeddings. Edward Frenkel, [*Lectures on the Langlands program and conformal field theory*, §3.6](https://arxiv.org/abs/hep-th/0512172), provides the relation with geometric functors and their eventual representation-theoretic use.
