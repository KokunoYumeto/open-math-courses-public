# Inverse images

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Source and dependency reconciliation and full algebraic and analytic non-characteristic proofs, including central specialization, uniform analytic filtrations and characteristic equality, by GPT-6 Astra (OpenAI), Ultra, October 2026. Original examples and complete solutions retained.*

The fiber of the point module at its own supporting point is zero as an ordinary tensor product. Its derived fiber is one-dimensional. This is the first reason inverse image of differential equations must be derived. A second issue is coherence: restricting the regular differential-operator module to a point leaves infinitely many derivative directions. Smooth maps and non-characteristic maps provide useful situations where these problems are controlled.

Let $k$ have characteristic zero. All varieties are smooth, separated and of finite type, with pure dimensions. Geometric characteristic varieties use an algebraically closed $k$; analytic statements use $\mathbb C$. Modules are left differential-operator modules, quasi-coherent over the structure sheaf. For $f:X\to Y$, this chapter uses

\[
f^!:=Lf^*[d_X-d_Y].
\tag{0.1}
\]

The star before deriving means the ordinary right-exact pullback. The exclamation mark means this particular shifted derived pullback. We have not defined another inverse image by duality. Our prerequisites are [connections and left/right conventions](d-modules-flat-connections-and-local-systems.md) and [holonomic modules and duality](holonomic-d-modules-and-duality.md), together with derived tensor products and Koszul complexes.

## 1. The chain rule and the transfer bimodule

The differential of $f$ is the map

\[
df:T_X\longrightarrow
\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}T_Y.
\tag{1.1}
\]

If $df(\xi)=\sum_\nu a_\nu\otimes\eta_\nu$, define on the ordinary pullback

\[
\xi(b\otimes m)=
\xi(b)\otimes m+
\sum_\nu b a_\nu\otimes\eta_\nu m,
\qquad
f^*M=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}M.
\tag{1.2}
\]

This is independent of the tensor expression for $df(\xi)$, since the action of vector fields on $M$ is $\mathcal O_Y$-linear in the vector field.

To check balancing, move $h\in\mathcal O_Y$ across the tensor. Acting on $bf^*h\otimes m$ produces the extra term $b\xi(f^*h)\otimes m$. Acting instead on $b\otimes hm$ produces $\sum_\nu ba_\nu f^*(\eta_\nu h)\otimes m$, equal to the same term by (1.1). The remaining terms coincide. Thus (1.2) descends to the tensor product.

### Proposition 1.1. The canonical differential-operator action

Formula (1.2) makes $f^*M$ a left $\mathcal D_X$-module. If $M$ is a finite integrable connection, this is its usual pullback connection.

**Proof.** The product commutator is immediate:

\[
[\xi,b]\,(c\otimes m)=\xi(b)c\otimes m.
\]

For the Lie bracket relation, work in commuting étale coordinates $y_1,\ldots,y_{d_Y}$ on $Y$. Formula (1.2) becomes

\[
\nabla^f_\xi=\xi\otimes1+
\sum_j\xi(f^*y_j)\,\partial_{y_j}.
\tag{1.3}
\]

On a tensor $b\otimes m$, the commutator of two such operators has derivative coefficients

\[
\xi\bigl(\zeta(f^*y_j)\bigr)
-\zeta\bigl(\xi(f^*y_j)\bigr)
=[\xi,\zeta](f^*y_j).
\]

The terms containing two $\partial_y$ commute and cancel, and the remaining action on $b$ is $[\xi,\zeta](b)$. Hence $[\nabla^f_\xi,\nabla^f_\zeta]=\nabla^f_{[\xi,\zeta]}$. The relations for functions and vector fields defining $\mathcal D_X$ are all satisfied. This constructs its action and proves uniqueness. The construction in terms of $df$ glues across coordinate changes.

For a connection $\nabla:M\to\Omega_Y^1\otimes M$, let $\rho:f^*\Omega_Y^1\to\Omega_X^1$ be the map on differential forms. The usual pullback connection is

\[
\nabla^f(b\otimes m)
=db\otimes m+b(\rho\otimes1)(1\otimes\nabla m).
\]

Its contraction with $\xi$ is exactly (1.2). The coefficient-derivative term makes the whole formula balanced; $\nabla$ is not being treated as an $\mathcal O_Y$-linear map to which ordinary tensor pullback could be applied alone. The bracket calculation proves flatness. $\square$

Take $M=\mathcal D_Y$, with its left regular action. The resulting module is

\[
\mathcal D_{X\to Y}
=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_Y.
\tag{1.4}
\]

Right multiplication on the second factor commutes with every operation in (1.2), so (1.4) is a $(\mathcal D_X,f^{-1}\mathcal D_Y)$-bimodule. It is the **transfer module**.

Multiplication gives a natural isomorphism

\[
\mathcal D_{X\to Y}
\otimes_{f^{-1}\mathcal D_Y}f^{-1}M
\simeq f^*M.
\tag{1.5}
\]

Explicitly $(b\otimes P)\otimes m\mapsto b\otimes Pm$; its inverse sends $b\otimes m$ to $(b\otimes1)\otimes m$. The chain rule verifies $\mathcal D_X$-linearity.

Kashiwara–Schapira use $f:Y\to X$ and therefore write $\mathcal D_{Y\to X}$. Equation (1.4) uses the source first for our $f:X\to Y$. Beilinson–Drinfeld denote the ordinary left-module pullback by $f^\dagger$ in Section 7.2.8. In this chapter it is $f^*$.

## 2. Deriving pullback and composing it

Define

\[
Lf^*M=
\mathcal D_{X\to Y}
\otimes^{L}_{f^{-1}\mathcal D_Y}f^{-1}M.
\tag{2.1}
\]

Its underlying derived structure-sheaf module is

\[
\mathcal O_X
\otimes^{L}_{f^{-1}\mathcal O_Y}f^{-1}M.
\tag{2.2}
\]

Indeed, a resolution of $M$ by locally free differential-operator modules is also flat over $\mathcal O_Y$, by PBW. Applying (1.5) term by term computes both expressions. For an $\mathcal O_Y$-flat connection there is no higher pullback cohomology, but this conclusion does not hold for an arbitrary coherent $\mathcal D_Y$-module.

Locally the regular ring $\mathcal O_Y$ has finite global dimension bounded by $d_Y$. Thus (2.2) takes bounded complexes to bounded complexes. This statement only asserts boundedness; coherence of the resulting differential-operator cohomology needs additional arguments.

### Theorem 2.1. Composition

For $X\xrightarrow fY\xrightarrow gZ$, there are canonical natural isomorphisms

\[
L(gf)^*\simeq Lf^*Lg^*,
\qquad
(gf)^!\simeq f^!g^!.
\tag{2.3}
\]

**Proof.** The underived transfer identity is

\[
\mathcal D_{X\to Y}
\otimes_{f^{-1}\mathcal D_Y}f^{-1}\mathcal D_{Y\to Z}
\simeq\mathcal D_{X\to Z}.
\tag{2.4}
\]

Canceling the middle regular $\mathcal D_Y$ factor identifies its left side with $\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_{Y\to Z}$, and then with $\mathcal O_X\otimes_{(gf)^{-1}\mathcal O_Z}(gf)^{-1}\mathcal D_Z$. The left action is that of $d(gf)$ because the two chain-rule terms combine by the differential's composition law. Right multiplication is preserved as well.

There are no hidden higher Tor terms in this particular transfer product. As a left $\mathcal O_Y$-module, $\mathcal D_{Y\to Z}$ is locally a direct sum of copies of $\mathcal O_Y$: use PBW for $\mathcal D_Z$ and then pull its coefficient modules to $Y$. Hence it is $\mathcal O_Y$-flat. Applying the comparison (2.1)–(2.2) to this module proves the derived version of (2.4).

Derived tensor associativity now gives

\[
\begin{aligned}
Lf^*Lg^*M
&\simeq
\left(\mathcal D_{X\to Y}
\otimes^L_{f^{-1}\mathcal D_Y}
f^{-1}\mathcal D_{Y\to Z}\right)
\otimes^L_{(gf)^{-1}\mathcal D_Z}(gf)^{-1}M\\
&\simeq L(gf)^*M.
\end{aligned}
\tag{2.5}
\]

Exactness of inverse image of sheaves and flat resolutions justify these associations. All maps are the multiplication and chain-rule maps above, so the isomorphism is natural and compatible with a third composition. Finally

\[
(d_X-d_Y)+(d_Y-d_Z)=d_X-d_Z.
\]

Adding the shifts from (0.1) proves the second assertion. $\square$

## 3. Smooth maps: exactness and characteristic support

Write the cotangent maps as

\[
X\times_YT^*Y
\xrightarrow{\,f_d\,}T^*X,
\qquad
X\times_YT^*Y
\xrightarrow{\,f_\pi\,}T^*Y.
\tag{3.1}
\]

Here $f_d(x,\eta)=(x,df_x^*\eta)$, and $f_\pi(x,\eta)=(f(x),\eta)$.

### Theorem 3.1. Smooth pullback

If $f$ is smooth of relative dimension $r=d_X-d_Y$, then $f^*$ is exact and preserves coherent differential-operator modules. For coherent $M$,

\[
\operatorname{Ch}(f^*M)
=f_d\bigl(f_\pi^{-1}\operatorname{Ch}(M)\bigr).
\tag{3.2}
\]

In particular it preserves holonomic modules.

**Proof.** Smoothness implies flatness of $\mathcal O_X$ over $\mathcal O_Y$; see [Stacks, Tag 01VF](https://stacks.math.columbia.edu/tag/01VF). Equations (1.5) and (2.2) then prove exactness and vanishing of higher pullback cohomology.

Work locally in étale coordinates adapted to the smooth map: lift coordinates $y_1,\ldots,y_{d_Y}$ and append relative coordinates $t_1,\ldots,t_r$. The coordinate vector fields in the $y$ directions lift those on $Y$, while the $t$ directions act only on coefficients from $\mathcal O_X$. Thus the transfer module is generated over $\mathcal D_X$ by $1\otimes1$, with relative derivatives killing that generator. Pulling back a finite presentation of $M$ gives finite differential-operator generators and relations locally; equivalently, the following good-filtration calculation proves coherence directly.

Choose a good order filtration $F$ of $M$ and give $N=f^*M$ the filtration $F_pN=f^*F_pM$. Flatness makes these inclusions and gives

\[
\operatorname{gr}N\simeq
\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\operatorname{gr}M.
\tag{3.3}
\]

The pulled-back base derivatives act on its symbols as their counterparts on $\operatorname{gr}M$. Relative derivatives preserve $F_pN$ and therefore have zero degree-one action on $\operatorname{gr}N$. This makes (3.3) finite over

\[
\mathcal O_X[\xi_y,\xi_t],
\quad\text{with }\xi_t\operatorname{gr}N=0.
\]

Its filtration pieces are coherent over $\mathcal O_X$ and bounded below, so the filtration is good and $N$ is coherent.

Geometrically (3.3) is the pullback of the graded sheaf along $f_\pi$, followed by its pushforward along the closed immersion $f_d$. The latter is a closed immersion because the cotangent map of a smooth morphism is injective. Support under flat base change is exactly the inverse image: at a point lying over the original support the corresponding local flat map is faithfully flat, so the finite module cannot become zero. This proves (3.2), including smooth maps that are not surjective.

The map $f_\pi$ is smooth of relative dimension $r$. If $M$ is holonomic, its nonempty characteristic components have dimension $d_Y$, so every component of their pullback has dimension $d_Y+r=d_X$. The closed immersion $f_d$ preserves this dimension. Therefore $N$ is holonomic, or zero if the support is missed. $\square$

### Projection examples

For $p:\mathbb A_x^1\times\mathbb A_t^1\to\mathbb A_x^1$,

\[
p^*M=k[t]\otimes_kM,
\quad
\partial_x(h\otimes m)=h\otimes\partial_xm,
\quad
\partial_t(h\otimes m)=h'\otimes m.
\tag{3.4}
\]

Coordinates act on their respective factors. Thus $p^*\mathcal O_{\mathbb A^1}=\mathcal O_{\mathbb A^2}$. Pulling back $\delta_0$ gives a holonomic module supported on the divisor $x=0$, with characteristic set $x=0,\ \xi_t=0$ and free covectors $\xi_x$.

For a cyclic $M=A_1/A_1P$, the presentation is

\[
p^*M\simeq
A_2/(A_2P+A_2\partial_t).
\tag{3.5}
\]

The cyclic generator satisfies both equations. PBW with $t,\partial_t$ separated from $x,\partial_x$ identifies its quotient with $k[t]\otimes M$, proving the presentation. The shifted pullback is $p^!M=p^*M[1]$, concentrated in cohomological degree $-1$.

## 4. Closed embeddings and Koszul fibers

Let $i:Z\hookrightarrow X$ be a smooth closed subvariety of codimension $c$. It is a regular immersion; see [Stacks, Tag 067U](https://stacks.math.columbia.edu/tag/067U). Locally its ideal is generated by a regular sequence $x_1,\ldots,x_c$, chosen as normal coordinates.

### Proposition 4.1. Derived pullback by a closed embedding

The underlying derived pullback is represented locally by

\[
Li^*M\simeq K(x_1,\ldots,x_c;M),
\qquad
i^!M\simeq K(x_1,\ldots,x_c;M)[-c].
\tag{4.1}
\]

The Koszul complex has terms $\bigwedge^a k^c\otimes M$ in degree $-a$, with differential

\[
d(e_{j_1}\wedge\cdots\wedge e_{j_a}\otimes m)
=\sum_{b=1}^{a}(-1)^{b-1}
e_{j_1}\wedge\cdots\widehat{e_{j_b}}\cdots
\wedge e_{j_a}\otimes x_{j_b}m.
\tag{4.2}
\]

These are commuting multiplication operators; no normal derivative appears in this differential.

**Proof.** A regular sequence has an augmented Koszul resolution of the quotient structure sheaf. To see the exactness, begin with the two-term resolution for a single nonzerodivisor. Tensor successively with the next two-term complex. At each stage multiplication by the next normal equation is injective on the previous quotient, so its cone has cohomology only in degree zero, equal to the new quotient. This proves the finite free resolution of $\mathcal O_Z$; compare [Stacks, Tag 062F](https://stacks.math.columbia.edu/tag/062F).

Tensor this resolution with $M$ in (2.2). Since the resolution terms are locally free, the result computes the derived tensor product even when the normal equations are zerodivisors on $M$. Its differential is (4.2), proving the first formula. Since $d_Z-d_X=-c$, (0.1) gives the second.

The canonical $\mathcal D_Z$-structure is that of the transfer construction (2.1). In adapted coordinates, tangent derivatives commute with multiplication by the normal equations and give its action on Koszul cohomology. Each normal equation acts null-homotopically on the Koszul complex, so the cohomology is a module over the quotient structure sheaf. The individual terms $M$ of this underlying Koszul model need not be annihilated by the ideal of $Z$; they are not separately being asserted to be $\mathcal O_Z$-modules. $\square$

### Three fibers at the origin

For $i_0:\{0\}\hookrightarrow\mathbb A^1$, the complex is

\[
[M\xrightarrow{x}M]\quad\text{in degrees }-1,0.
\tag{4.3}
\]

Consequently $H^{-1}(Li_0^*M)=\ker x$, $H^0(Li_0^*M)=M/xM$, and $i_0^!=Li_0^*[-1]$.

For $M=k[x]$, multiplication by $x$ is injective and its cokernel is $k$. Thus $Li_0^*\mathcal O=k$ in degree zero, while $i_0^!\mathcal O=k[-1]$ has its only cohomology in degree one.

For $\delta_0=k[\partial]v$ with $xv=0$, the identity

\[
x\partial^jv=-j\partial^{j-1}v
\tag{4.4}
\]

shows that $x$ is surjective and has kernel $kv$. Hence the ordinary fiber $i_0^*\delta_0$ is zero, $Li_0^*\delta_0\simeq k[1]$, and $i_0^!\delta_0\simeq k$ in degree zero.

For $L=k[x,x^{-1}]=j_*\mathcal O_{\mathbb G_m}$, $x$ is invertible, so both terms of (4.3) cancel: $Li_0^*L=i_0^!L=0$.

For comparison, $Li_0^*\mathcal D_{\mathbb A^1}$ has only degree-zero cohomology $A_1/xA_1$, with basis $1,\partial,\partial^2,\ldots$. This is infinite-dimensional over $\mathcal D_{\{0\}}=k$. It disproves preservation of coherence by arbitrary pullback.

## 5. A power map, including its ramification point

Let $f_m:\mathbb A_z^1\to\mathbb A_x^1$ be $x=z^m$, with $m\geq1$. On $\mathbb G_m$ a rank-one connection with $\partial_xe=\lambda x^{-1}e$ pulls back to

\[
\partial_ze=mz^{m-1}\lambda z^{-m}e
=m\lambda z^{-1}e.
\tag{5.1}
\]

Thus $\mathcal O x^\lambda$ pulls back to $\mathcal O z^{m\lambda}$. The whole affine-line pullback of $Q_\lambda=A_1/A_1(x\partial_x-\lambda)$ needs more care.

The ring $k[z]$ is free of rank $m$ over $k[x]$, with basis $1,z,\ldots,z^{m-1}$. Indeed grouping polynomial monomials by their exponent modulo $m$ gives unique coefficients in $k[z^m]$. Therefore this map is flat and $Lf_m^*=f_m^*$, even though it is not smooth at zero for $m>1$.

Put $E_\alpha=k[z,z^{-1}]e_\alpha$ with $\partial_ze_\alpha=\alpha z^{-1}e_\alpha$. Write $L_z=k[z,z^{-1}]$ and $J_z=A_1(z)/A_1(z)(z\partial_z)$.

### Proposition 5.1. Full Euler pullback

There are isomorphisms

\[
f_m^*Q_\lambda\simeq
\begin{cases}
E_{m\lambda},&\lambda\notin\mathbb Z,\\
L_z,&\lambda\in\mathbb Z_{<0},\\
J_z,&\lambda\in\mathbb Z_{\geq0}.
\end{cases}
\tag{5.2}
\]

If $\lambda\notin\mathbb Z$ but $m\lambda\in\mathbb Z$, the first answer is isomorphic to $L_z$. It need not be $Q_{m\lambda}$ with its usual cyclic generator.

**Proof.** Normal forms in $Q_\lambda$ consist of $x^av$, $a\geq0$, and $\partial_x^bv$, $b\geq1$. Its mixed terms reduce by

\[
x\partial_x^bv=(\lambda-b+1)\partial_x^{b-1}v.
\tag{5.3}
\]

For $\lambda\notin\mathbb Z$, map $v$ to the Laurent-connection generator $e_\lambda$. The two branches map to $x^ae_\lambda$ and $(\lambda)_b x^{-b}e_\lambda$, where all falling-factorial coefficients are nonzero. Their distinct exponents prove bijectivity onto the full Laurent connection. The same argument works for every negative integer $\lambda$, and the resulting connection is isomorphic to $L_x$ by $e_\lambda\mapsto x^\lambda$.

For $\lambda=\ell\geq0$, use the basis of $J_x$ from the duality chapter and map $v$ to $x^\ell v_0$. Successive derivatives first give nonzero multiples of $x^{\ell-b}v_0$ for $b\leq\ell$, then $\ell!\partial_xv_0$ and its higher derivatives. The positive branch supplies the higher powers of $x$. Again the images are exactly its independent basis vectors, so $Q_\ell\simeq J_x$.

Pulling back a Laurent connection tensors its coefficient ring to $k[z,z^{-1}]$; (5.1) gives its derivative action. This proves the first case and the negative-integer case of (5.2).

It remains to pull back $J_x$. Flatness pulls its nonsplit extension to

\[
0\longrightarrow f_m^*\delta_{0,x}
\longrightarrow f_m^*J_x\longrightarrow k[z]\longrightarrow0.
\tag{5.4}
\]

The description $\delta_{0,x}=L_x/k[x]$ gives

\[
f_m^*\delta_{0,x}
=L_z/k[z]=\delta_{0,z},
\tag{5.5}
\]

with the usual derivative action by the chain rule. Under this identification, the vector $\partial_xv_0$ in the point submodule maps to $[z^{-m}]$. If $U=1\otimes v_0$, then

\[
\partial_zU=mz^{m-1}\otimes\partial_xv_0
=m[z^{-1}].
\tag{5.6}
\]

In particular $z\partial_zU=0$, so $v_0\mapsto U$ defines $J_z\to f_m^*J_x$. It maps its point submodule isomorphically to the point submodule of (5.4), since $m\ne0$, and induces the identity on the polynomial quotient. The short exact sequences then show it is an isomorphism. This proves the last case.

Finally if $\alpha=m\lambda\in\mathbb Z$, the map $e_\alpha\mapsto z^\alpha$ identifies $E_\alpha$ with $L_z$. For example $\lambda=1/2,m=2$ gives $L_z$, whereas $Q_1\simeq J_z$. The naive pulled-back cyclic vector satisfies Euler eigenvalue $1$, but its derivatives cannot produce all inverse powers; the full tensor product still contains them. $\square$

## 6. Non-characteristic maps: the stated general theorem

For coherent $M$, the morphism $f$ is **non-characteristic** if

\[
f_\pi^{-1}\operatorname{Ch}(M)\cap\ker f_d
\subseteq X\times_Y(\text{zero section of }T^*Y).
\tag{6.1}
\]

For a closed embedding this says that characteristic covectors contain no nonzero conormal covector to the embedded variety. For a smooth map $\ker f_d=0$, so every coherent module is non-characteristic. For a finite connection its characteristic support is the zero section, so every morphism is non-characteristic.

**Non-characteristic pullback theorem — statement.** Under (6.1), $Lf^*M$ is concentrated in degree zero, its module $f^*M$ is coherent, and

\[
\operatorname{Ch}(f^*M)
=f_d\bigl(f_\pi^{-1}\operatorname{Ch}(M)\bigr).
\tag{6.2}
\]

For the analytic statement, see Pierre Schapira, [*An introduction to D-modules*, draft v7, March 2020](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/Dmod.pdf): Definition 2.3.1 and Theorem 2.3.7, pages 28–31, give the condition, coherence, concentration in degree zero and characteristic containment. Remark 2.3.8 on page 30 states the stronger equality (6.2), referring its proof to Kashiwara. Definition 3.1.10 and Lemma 3.1.11, page 54, give the cotangent-kernel and finite-projection comparison. Schapira's $f_D^{-1}$ is the unshifted $Lf^*$ here, not $f^!$.

The algebraic statement, including equality (6.2), is Schnell, [*D-modules*, Theorem 16.5](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), pages 79–83. Its proof supplies coherence and vanishing but leaves an additional filtration argument for the general equality. The smooth equality was proved in Section 3. Lemmas 6.1–6.2 and Proposition 6.3 below supply the general algebraic finite-projection comparison, coherence, vanishing and containment. Lemma 6.4 and Theorem 6.5 below complete the full algebraic equality by a Rees-torsion argument and the earlier involutivity theorem. Lemmas 6.6 and Theorem 6.7 below supply the additional analytic coherence and support arguments, proving the full analytic theorem as well.

At the origin of a line, the polynomial connection is non-characteristic and $\delta_0$ is characteristic. Their Koszul computations show the corresponding presence or absence of higher pullback cohomology. For $m>1$, $f_m$ is characteristic at zero for $Q_\lambda$, whose characteristic support includes the whole cotangent fiber there. Nevertheless its flatness eliminates higher Tor in Section 5. Non-characteristic is a sufficient condition, and its failure does not force higher cohomology in every example.

### Lemma 6.1. A cone and a finite projection

Let $A$ be a Noetherian ring and $C$ a quotient of $A[z_1,\ldots,z_r]$ by a homogeneous ideal; all $z_j$ have degree one. Let $\eta_1,\ldots,\eta_q\in C_1$. The map $\operatorname{Spec}C\to\operatorname{Spec}A[\eta_1,\ldots,\eta_q]$ is finite if the inverse image of the zero section has no nonzero geometric point. Conversely, finiteness implies that condition for this conic linear map.

**Proof.** The condition says that every $z_j$ belongs to the radical of $(\eta_1,\ldots,\eta_q)C$. Choose positive integers $n_j$ with $z_j^{n_j}$ in that ideal. Every monomial of degree at least $N=1+\sum_j(n_j-1)$ therefore belongs to it. By taking homogeneous components, every element of $C_d$ for $d\geq N$ is a sum of $\eta_i$ times elements of $C_{d-1}$. Induction on $d$ shows that the finitely many monomials of degree less than $N$ generate $C$ over $A[\eta_1,\ldots,\eta_q]$. This is finiteness. The argument keeps nilpotents: the powers $n_j$ need not be one. Conversely, a nonzero geometric point in the kernel brings its entire scaling line into that fiber. Such a line cannot lie in a finite fiber. $\square$

Apply the lemma locally to the coordinate algebra of $f_\pi^{-1}\operatorname{Ch}(M)$ and to the linear functions induced by $f_d$. It proves, in the algebraic setting, the asserted equivalence between (6.1) and finiteness on the pulled-back characteristic support. The image is consequently closed. No properness of $f$ is required.

### Lemma 6.2. Normal multiplication is injective

Let $i:X=\{t=0\}\hookrightarrow Y$ be a smooth hypersurface in a smooth characteristic-zero variety. Suppose it is non-characteristic for the coherent module $M$. Then $t:M\to M$ is injective near $X$.

**Proof.** Choose adapted étale coordinates $(x_1,\ldots,x_n,t)$ at a point $y\in X$, and write their symbols as $(\xi_1,\ldots,\xi_n,\tau)$. Take $u$ with $tu=0$. The cyclic submodule $\mathcal D_Yu$ is coherent and has characteristic support contained in that of $M$, by the characteristic-support exact-sequence theorem. In its cyclic quotient filtration, this support is the zero set of the graded annihilator of $u$.

At $y$, no nonzero point of the $\tau$-axis lies in that zero set. Some homogeneous element $q$ of the graded annihilator thus has a nonzero pure $\tau^d$ coefficient at $y$: restrict the homogeneous ideal to the axis, where an ideal whose zero set is only the origin contains a power of $\tau$, and lift a homogeneous expression for that power. Lift $q$ to an operator $P$ annihilating $u$. After shrinking the coordinate neighborhood its pure $\partial_t^d$ coefficient $a$ is a unit. All other monomials have normal derivative exponent less than $d$, since the total order is $d$.

Define $\operatorname{ad}_t(Q)=tQ-Qt$. The Weyl relations give the operator identity

\[
\operatorname{ad}_t^{\,d}(P)=(-1)^d d!a.
\tag{6.3}
\]

Indeed, $t$ commutes with coefficient functions and tangent derivatives, and $[t,\partial_t^j]=-j\partial_t^{j-1}$. Repeating the commutator kills every term with fewer than $d$ normal derivatives. Moreover every iterated commutator annihilates $u$: if $Qu=0$, then $(tQ-Qt)u=0$ because $tu=0$. Equation (6.3), the invertibility of $a$, and characteristic zero imply $u=0$. For $d=0$ the same conclusion follows directly from $Pu=au=0$. $\square$

The commutators here are repeated commutators **with the normal coordinate $t$**, not repeated commutators with $P$. This distinction determines both the order reduction and the scalar in (6.3).

### Proposition 6.3. Algebraic coherence, vanishing and containment

For every algebraic morphism $f:X\to Y$ in the scope of this lesson satisfying (6.1), $Lf^*M$ is concentrated in degree zero, $f^*M$ is coherent, and

\[
\operatorname{Ch}(f^*M)
\subseteq f_d\bigl(f_\pi^{-1}\operatorname{Ch}(M)\bigr).
\tag{6.4}
\]

**Proof for a hypersurface.** Keep the coordinates of Lemma 6.2, put $B=\mathcal O_Y$ on the chosen chart, and let $\mathcal T$ be the subalgebra of $\mathcal D_Y$ generated by $B$ and the tangent derivatives $\partial_{x_1},\ldots,\partial_{x_n}$. The derivations commute and kill $t$. PBW gives

\[
\begin{aligned}
\operatorname{gr}\mathcal T&=B[\xi_1,\ldots,\xi_n],\\
\mathcal T/t\mathcal T&\simeq i_*\mathcal D_X
\quad\text{on the hypersurface chart}.
\end{aligned}
\tag{6.5}
\]

The second identification means the sheaf with coefficients $B/(t)$ and the induced tangent derivations; it is not a splitting of $B\to B/(t)$.

Give $M$ a good order filtration $F$. At $y$, the restriction of the homogeneous annihilator of $\operatorname{gr}_FM$ to the normal axis again contains a power of $\tau$. A homogeneous lift gives a polynomial in that annihilator whose pure $\tau^d$ coefficient is nonzero at $y$. Invert that coefficient on a neighborhood. If $d=0$, the resulting unit annihilates $\operatorname{gr}_FM$, so the exhaustive, bounded-below filtration gives $M=0$ there and all claims follow. Otherwise this yields a monic relation in $\tau$, with coefficients in $B[\xi]$. Division by this monic relation shows that $\operatorname{gr}_FM$ is finite over $B[\xi]$: take a finite set of its original symbol generators and their products by $1,\tau,\ldots,\tau^{d-1}$. Thus the same $F$ is a good $\mathcal T$-filtration, not merely a good $\mathcal D_Y$-filtration.

Here are the finiteness details needed for the quotient. The Rees algebra of $\mathcal T$, with central homogenizing variable $h$, is generated by $B,h,h\partial_{x_j}$. Filtering by the number of $h\partial_{x_j}$ factors, while keeping $h$ in degree zero, gives the polynomial associated graded algebra $B[h,\zeta_1,\ldots,\zeta_n]$. The leading-term lifting proof of Noetherianity from the differential-operator lesson, Theorem 5.1 applies: finite homogeneous generators of a graded ideal lift to generators of the filtered ideal by successively decreasing order. The corresponding module argument gives finite submodules of finite Rees modules. Consequently the intersection filtration on the $\mathcal T$-submodule $tM$, and the image filtration on $N=M/tM$, are good. This is also the explicit Rees argument of the characteristic-variety lesson, Section 4, now applied to $\mathcal T$.

The image filtration of $N$ therefore proves its coherence over $\mathcal T/t\mathcal T=\mathcal D_X$. There is a surjection of graded $(B/(t))[\xi]$-modules

\[
(\operatorname{gr}_FM)/t(\operatorname{gr}_FM)
\twoheadrightarrow \operatorname{gr}_FN.
\tag{6.6}
\]

To check it in degree $p$, map the class of $m\in F_pM$ to its class in $F_pN/F_{p-1}N$. Both $F_{p-1}M$ and $tF_pM$ map to zero, and every class in the target has such a lift. Tangent symbols commute with this construction. A normal derivative need not descend to $N$, so (6.6) is **not** asserted to be a map of modules over the full symbol algebra containing $\tau$.

As a module over $(B/(t))[\xi,\tau]$, the left side has support $\operatorname{Ch}(M)\cap\{t=0\}$. This equality follows from localization and Nakayama's lemma applied to the finite graded module. Viewed instead over $(B/(t))[\xi]$, its support is the image under forgetting $\tau$. To verify this last fact, use the finite algebra obtained by quotienting by its annihilator: after localizing at a prime of the smaller ring, a nonzero finite module has a prime of its support above that prime, by Nakayama applied to the corresponding finite algebra. The reverse implication follows by localization. Thus support of the quotient in (6.6) is contained in that projected support. This proves (6.4) for $i$. Finally the two-term Koszul calculation in Proposition 4.1 and injectivity from Lemma 6.2 show that $Li^*M=N$ in degree zero.

**Higher codimension.** At a point of a smooth closed embedding choose normal coordinates $t_1,\ldots,t_c$. Factor the embedding locally through the successive smooth hypersurfaces $t_1=0$, then $t_2=0$, and so on. The first hypersurface is non-characteristic near the point: its normal line lies in the full conormal space, which has zero intersection with the characteristic cone away from zero. The monic-relation argument above also proves this condition on a neighborhood, not only at the one point.

After that restriction, (6.4) places the new characteristic support in the projection of the old one. A covector in this projected support which is normal to the remaining embedding lifts to an old covector in the full original conormal space. Condition (6.1) forces that lift, and hence its projection, to be zero. This proves the non-characteristic hypothesis for the next stage. Induction proves it at every stage. Theorem 2.1 composes the derived pullbacks; each stage is coherent and concentrated in degree zero. Composing the cotangent projections gives precisely (6.4) for the original embedding. The statements are local and hence glue.

**An arbitrary morphism.** Factor $f$ by its graph:

\[
X\xrightarrow{\ i=(1,f)\ }X\times Y
\xrightarrow{\ p\ }Y.
\tag{6.7}
\]

The smooth theorem proves all three conclusions, including equality of characteristic supports, for $p^*M$. Along the graph, its covectors have the form $(0,\eta)$ with $\eta\in\operatorname{Ch}(M)$. Restriction to the graph sends this covector to $df^*\eta$. Therefore the graph is non-characteristic for $p^*M$ exactly when (6.1) holds. Apply the closed-embedding result and the canonical composition isomorphism $Lf^*\simeq Li^*Lp^*$. The resulting support projection is $f_d f_\pi^{-1}$, giving (6.4) with the original source and target. $\square$

Surjectivity in (6.6) alone does not establish equality of supports. The following central-specialization argument supplies the missing reverse inclusion, using the already-proved involutivity theorem. The analytic theorem retains its full statement and exact external source; its separate common-neighborhood coherence proof is supplied in Lemma 6.6 and Theorem 6.7.

### Lemma 6.4. Central specialization without strictness

Let $A$ be a filtered ring whose Rees ring $R$ is left Noetherian and whose symbol ring $S=R/hR$ is commutative Noetherian. Let $M$ have a good filtration, put $L=\operatorname{Rees}M$ and $E=L/hL$, and let $t\in F_0A$ be central. Suppose $t$ acts injectively on $M$. Give $N=M/tM$ the image filtration. If no irreducible component of $\operatorname{Supp}_S E$ is contained in $V(t)$, then

\[
\operatorname{Supp}_S\operatorname{gr}N
=\operatorname{Supp}_S E\cap V(t).
\tag{6.8}
\]

The $S$-action on $\operatorname{gr}N$ factors through $S/(t)$. The assertion concerns support, not an isomorphism $\operatorname{gr}N\simeq E/tE$. In particular, it does not assume that multiplication by $t$ is strict for the chosen filtration.

**Proof.** Set $C=L/tL$, a finite graded $R$-module, and let $K$ be its $h$-power torsion. Since $R$ is left Noetherian, $K$ is finitely generated. Centrality of $h$ therefore gives a single integer $r$ with $h^rK=0$. Localizing at $h$ identifies

\[
C[h^{-1}]=N[h,h^{-1}],\qquad
C/K=\operatorname{Rees}N.
\tag{6.9}
\]

Indeed $L[h^{-1}]=M[h,h^{-1}]$ by exhaustiveness, and the image of $L$ in $N[h,h^{-1}]$ is precisely the Rees module of the image filtration. The kernel of a central localization consists of the elements killed by a power of the element being inverted. The quotient $C/K$ is $h$-torsion-free. Reduction of $0\to K\to C\to C/K\to0$ modulo $h$ is consequently exact on the left as well:

\[
0\longrightarrow K/hK\longrightarrow E/tE
\longrightarrow\operatorname{gr}N\longrightarrow0.
\tag{6.10}
\]

For example, injectivity on the left follows directly: if $k=hc$ belongs to $K$, then $h\bar c=0$ in $C/K$; thus $c\in K$. This also proves that the displayed middle term is $C/hC$.

There is an $S$-linear identification, with a grading shift of one,

\[
E[t]:=\ker(t:E\to E)\ \simeq\ C[h]=K[h].
\tag{6.11}
\]

Here is the actual map. Lift $e\in E[t]$ to $\ell\in L$. Write $t\ell=h\ell'$ and send $e$ to the class of $\ell'$ modulo $tL$. Changing $\ell$ by $hw$ changes $\ell'$ by $tw$, so the map is well-defined. Its image is killed by $h$. Conversely, if $h\ell'\in tL$, write $h\ell'=t\ell$; then the class of $\ell$ in $E$ is killed by $t$ and maps back to the given class. If $\ell'=tw$, injectivity of $t$ on $L\subset M[h,h^{-1}]$ gives $\ell=hw$, proving injectivity. Centrality of $t$ and $h$ proves $S$-linearity. The grading shift will not affect any ungraded local length below. Elements killed by $h$ belong to $K$, giving the last equality.

We need to compare $K[h]$ and $K/hK$ without treating the noncommutative $R$-module $K$ as an $S$-module. Put

\[
\begin{aligned}
Q_j&=h^jK/h^{j+1}K,\\
A_j&=(K[h]\cap h^jK)/(K[h]\cap h^{j+1}K).
\end{aligned}
\tag{6.12}
\]

These modules really are finite $S$-modules. Multiplication by $h$ gives a surjection $Q_j\to Q_{j+1}$, with a grading shift. Its kernel is $A_j$: if $x\in h^jK$ and $hx=h^{j+2}z$, subtract $h^{j+1}z$ from $x$ to obtain an element of $K[h]\cap h^jK$ representing the same class. Thus $0\to A_j\to Q_j\to Q_{j+1}\to0$ is exact. Since $Q_r=0$, additivity of finite length and the filtration of $K[h]$ by its intersections with $h^jK$ give

\[
\ell_{S_{\mathfrak q}}((K/hK)_{\mathfrak q})
=\ell_{S_{\mathfrak q}}(K[h]_{\mathfrak q})
\tag{6.13}
\]

at any prime $\mathfrak q$ where $Q_0$ has finite length. Finiteness for every $Q_j$ follows from its being a quotient of $Q_0$, and for the $A_j$ from the displayed exact sequences. Thus (6.13) does not presuppose that localization of $K$ itself is defined over $S$.

Containment in (6.8) follows from (6.10). For the reverse inclusion take a prime $\mathfrak q$ minimal in $\operatorname{Supp}E\cap V(t)$ and put $U=S_{\mathfrak q}$, $H=E_{\mathfrak q}$. The modules $H/tH$ and $H[t]$ have support only at the closed point of $\operatorname{Spec}U$, so they have finite length. To justify the last implication, their annihilator radicals are the maximal ideal; finite generation of that ideal supplies a power annihilating the module, and its finite maximal-ideal filtration has finite-dimensional residue-field factors. Equation (6.10) makes $(K/hK)_{\mathfrak q}$ finite length too. Equations (6.10)–(6.13) therefore yield the exact formula

\[
\ell_U((\operatorname{gr}N)_{\mathfrak q})
=\ell_U(H/tH)-\ell_U(H[t]).
\tag{6.14}
\]

The right side is positive. Here are the commutative-algebra details, including embedded components. A finite module over a Noetherian ring has a finite filtration with prime cyclic factors: choose a nonzero element with maximal annihilator, which is prime (if $ab$ kills it and $b$ does not, maximality of the annihilator of its nonzero $b$-multiple forces $a$ into the original annihilator). Repeat in the quotient. An infinite repetition would give a strictly ascending chain of submodules, so Noetherianity makes the process finite. Apply this to $H$.

For a factor $U/\mathfrak p$, both its $t$-kernel and $t$-cokernel have finite length, since their support lies in $\operatorname{Supp}H\cap V(t)$, which consists only of the closed point. If $t\in\mathfrak p$, then $\mathfrak p$ is the maximal ideal, and those two modules are the same residue field: their length difference is zero. If $t\notin\mathfrak p$, primality makes the kernel zero, whereas $U/(\mathfrak p,t)$ is nonzero and has positive finite length. It is nonzero because both $\mathfrak p$ and $t$ lie in the maximal ideal. A short exact sequence of modules gives the six-term kernel/cokernel exact sequence for multiplication by $t$; hence the difference of the two lengths is additive along the prime filtration.

At least one factor has $t\notin\mathfrak p$. Otherwise the support of $H$, the union of the supports of its factors, would lie in $V(t)$. But $\mathfrak q$ contains a minimal support prime of $E$, and no such prime contains $t$ by hypothesis; this prime remains in the support after localization. Thus the sum of the nonnegative factor contributions is positive. Equation (6.14) proves that every minimal point of $\operatorname{Supp}E\cap V(t)$ lies in $\operatorname{Supp}\operatorname{gr}N$. The latter is closed, so it contains their closures, proving (6.8). The empty-support case is immediate. $\square$

The hypothesis excluding vertical components is essential. In the commutative filtered ring $k[t,z]$, with $t$ of order zero and $z$ of order one, take $M=k[t,z]/(tz-1)$. Multiplication by $t$ is invertible on $M$, so $N=0$, while $E=k[t,\xi]/(t\xi)$ and $E/tE=k[\xi]$. Its component $t=0$ violates the hypothesis. This is a counterexample to inferring equality from (6.6) or from injectivity on $M$ alone, not a counterexample to the non-characteristic theorem.

### Theorem 6.5. Full algebraic characteristic equality

For every algebraic morphism $f:X\to Y$ and coherent $\mathcal D_Y$-module $M$ in the stated characteristic-zero scope, condition (6.1) implies the full equality (6.2), as well as coherence and higher-Tor vanishing.

**Proof.** Start with a hypersurface $t=0$ and use the neighborhood, good filtration and tangent-operator algebra $\mathcal T$ from Proposition 6.3. Write

\[
S=B[\xi_1,\ldots,\xi_n],\qquad
\operatorname{gr}\mathcal D_Y=S[\tau],\qquad E=\operatorname{gr}_FM.
\tag{6.15}
\]

On this neighborhood a monic polynomial $q(\tau)\in S[\tau]$ of degree $d>0$ annihilates $E$, and $E$ is finite over $S$. The case of a degree-zero unit was already handled by $M=0$. In particular the projection of the full characteristic support to $\operatorname{Spec}S$ is finite and its image is $\operatorname{Supp}_S E$, by the finite-support comparison proved in Proposition 6.3.

No irreducible component of the full characteristic support lies in $t=0$. Indeed, let $\mathfrak p$ be a minimal support prime in $S[\tau]$. Theorem 7.0 of the characteristic-variety lesson, specifically its return to each minimal prime, proves $\{\mathfrak p,\mathfrak p\}\subset\mathfrak p$, not merely a bracket statement about an unreduced annihilator. If $t\in\mathfrak p$, the cotangent bracket gives

\[
a\in\mathfrak p\ \Longrightarrow\
\{t,a\}=-\partial_\tau a\in\mathfrak p.
\tag{6.16}
\]

Since $q\in\operatorname{Ann}E\subset\mathfrak p$, iterating (6.16) $d$ times puts $d!$ in $\mathfrak p$. This contradicts characteristic zero and primality. Here the leading coefficient of $q$ is exactly one; normalizing it was justified by the neighborhood construction in Proposition 6.3.

Nor can an irreducible component of $\operatorname{Supp}_S E$ be contained in $t=0$. The finite projection sends each of the finitely many full support components to a closed irreducible set; their union is this support. Each irreducible component of the image is one of those maximal images. If it lay in $t=0$, its corresponding full component would also lie in $t=0$, since the projection preserves coefficient functions. This has just been excluded.

All hypotheses of Lemma 6.4 now hold with $A=\mathcal T$. Its Noetherian Rees ring and the goodness of $F$ over $\mathcal T$ were proved in Proposition 6.3; $t$ is central in $\mathcal T$, and Lemma 6.2 proves its injectivity on $M$. Hence

\[
\begin{aligned}
\operatorname{Ch}_X(M/tM)
&=\operatorname{Supp}_S E\cap V(t)\\
&=\operatorname{pr}_{\xi}\bigl(\operatorname{Ch}_Y(M)\cap\{t=0\}\bigr).
\end{aligned}
\tag{6.17}
\]

Both sides are viewed in $\operatorname{Spec}(S/(t))=T^*X$. The second equality holds because the finite projection preserves $t$: a point in its image has $t=0$ exactly when every point above it does. This is the reverse inclusion missing from (6.6). No action of the normal symbol $\tau$ on $M/tM$, and no strictness of the original filtration, was assumed.

For a smooth closed embedding of arbitrary codimension, use the successive hypersurfaces in Proposition 6.3. That proof already establishes the non-characteristic condition at every stage using containment alone. Apply (6.17) at each stage. Composing the coordinate restrictions and cotangent projections gives equality for the original embedding, with precisely its original pulled-back characteristic support. Finally factor any $f$ into its graph and the smooth projection as in (6.7). The smooth equality in Theorem 3.1 and the closed-embedding equality just proved compose to (6.2); the graph non-characteristic comparison and the derived-composition map were verified in Proposition 6.3. These are local support equalities, so they agree on overlaps and give the global assertion. Coherence and higher-Tor vanishing are already supplied by Proposition 6.3. $\square$

This closes the algebraic theorem without replacing its equality by containment, and without restricting $M$ to a holonomic module or $f$ to an embedding. The analytic tangent-ring construction additionally needs common-neighborhood coherence, proved next rather than inferred from algebraic stalk Noetherianity.

### Lemma 6.6. Analytic parameters and uniform tangent operators

Let \(U\) be a coordinate neighborhood in a complex manifold, with coordinates \(z_1,\ldots,z_m\). Choose any subset \(I\) of the coordinate directions, including the empty subset, and let \(\mathcal A_I\) consist of finite sums of holomorphic-coefficient monomials in the derivatives \(\partial_{z_i}\), \(i\in I\). Give it the derivative-order filtration. Then:

1. \(\mathcal A_I\) is left and right coherent. Finite operator matrices have locally finitely generated kernels and images, and their images in filtered finite free modules have good induced filtrations, on one base neighborhood for all orders.
2. Suppose a filtered \(\mathcal A_I\)-module \(V\) is bounded below and exhaustive, with coherent holomorphic filtration pieces and a finite-presentation graded module over \(\mathcal O_U[\xi_i:i\in I]\). If \(t\) is a coordinate annihilated by the chosen derivatives, the image filtration on \(V/tV\) is good. On \(t=0\), if \(I\) consists of all remaining coordinate directions, this is a coherent analytic differential-operator module.
3. A holomorphic coordinate projection is flat on structure-sheaf stalks. It has the exact smooth pullback and characteristic-support formula of Theorem 3.1.

**Proof of the analytic algebra input.** The necessary uniform results for the full operator sheaf are proved in the analytic local-resolution theorem, Lemmas 3.0c.1–3.0c.4. Here is why the argument permits the parameters and the number of symbol variables needed here.

At a coordinate point take any \(r\geq0\), not necessarily \(r=m\), and put

\[
\begin{aligned}
H&=\mathbb C\{z_1,\ldots,z_m\},&
R&=H[u_1,\ldots,u_r]_{(\mathfrak m_H,u)},\\
B&=\mathbb C\{z_1,\ldots,z_m,u_1,\ldots,u_r\},&
C&=H[[u_1,\ldots,u_r]].
\end{aligned}
\tag{6.18}
\]

The convergent rings are Noetherian by the preparation-and-division induction proved in that lesson. Polynomial extension and localization make \(R\) Noetherian. With \(J=(u_1,\ldots,u_r)\), both \(R/J^a\) and \(B/J^a\) equal \(H[u]/J^a\). For \(B\), Taylor expansion in \(u\) proves this: finitely many coefficient germs have a common neighborhood, and the remainder is a sum of degree-\(a\) monomials times convergent germs. For \(R\), a denominator has a unit constant \(u\)-coefficient in \(H\), and its truncated inverse is a finite geometric series. Thus both \(J\)-adic completions are \(C\).

The Noetherian completion theorem used and linked in Lemma 3.0c.1 makes \(C\) faithfully flat over both local rings. For an injection of \(R\)-modules, tensor first with \(B\) and then with \(C\). Flatness over \(R\) kills the resulting kernel, flatness over \(B\) identifies it with the tensor of the first kernel, and faithfulness over \(B\) kills that first kernel. This proves flatness of \(B\) over \(R\). Faithfulness follows by applying faithful flatness of \(C/R\) to a module killed by \(B\). These arguments apply to arbitrary modules, not just finite ones. When \(r=0\), they reduce to the identity. Also \(R\) is flat over \(H\), being a localization of a polynomial algebra. Hence \(B\) is flat over \(H\).

**One neighborhood for symbols and operators.** Set \(r=|I|\) in (6.18). A homogeneous matrix over \(\mathcal O_U[\xi_I]\) has a finite homogeneous kernel at the base stalk. Represent its generators nearby and pass to the corresponding analytic matrix at the zero section of \(U\times\mathbb C^r\). The flat comparison just proved and Oka coherence identify its analytic kernel there. The quotient by the chosen generators is coherent with zero stalk, so it vanishes on a product neighborhood.

This analytic vanishing detects the polynomial kernel at every nearby base point. Indeed, a finite graded polynomial module \(Q\) that vanished at the maximal ideal \((\mathfrak m,\xi_I)\) would be killed by a polynomial outside that ideal. Every homogeneous component of that annihilator kills \(Q\); its constant component is a unit. Thus \(Q=0\). Faithful flatness at the zero section followed by this detection proves that the same finite list generates the polynomial kernel in all degrees. This is the proof of Lemma 3.0c.3 with the independent counts \(m,r\); it involves no shrinking indexed by degree.

The finite PBW expression for \(\mathcal A_I\) has symbol ring \(\mathcal O_U[\xi_I]\). Its commutators with coefficients lower order, and its chosen coordinate derivatives commute. These are exactly the operator properties used in the uniform image-and-relation proof, Lemma 3.0c.4. More explicitly, for a finite matrix \(\phi:F\to F'\), choose stalk image generators \(g_j\) whose symbols generate its induced symbol module; let \(\psi:G\to F'\) send a shifted free basis to them. Descending order gives strictness at the base stalk. Choose finite matrices \(u:F\to G\) and \(v:G\to F\) with \(\psi u=\phi\) and \(\phi v=\psi\). For each homogeneous symbol relation \(\lambda_a\) of degree \(k_a\), lift it and subtract an element of \(G_{k_a-1}\) with the same \(\psi\)-image. The resulting \(r_a\) satisfies

\[
\psi(r_a)=0,\qquad \sigma(r_a)=\lambda_a.
\tag{6.19}
\]

There are finitely many identities and order bounds to represent. The uniform symbol result makes the \(\lambda_a\) generate nearby. Subtracting the corresponding combinations of \(r_a\) lowers order, so proves both nearby strictness and generation of \(\ker\psi\). For \(w\in\ker\phi\), the identity

\[
w=v\,u(w)+(1-vu)w
\tag{6.20}
\]

expresses it using \(v(r_a)\) and the finitely many \((1-vu)(e_j)\). These elements really lie in \(\ker\phi\), by the two matrix identities. This proves the kernel assertion and good induced image filtration. It proves coherence, and formal transposition gives the right-module version. Derivatives in \(I\) differentiating the holomorphic coefficients cause only the already-accounted-for lower-order terms; no derivative in a missing direction is required.

**Good quotient filtration.** Lift a finite homogeneous generating list for \(\operatorname{gr}V\) to obtain a shifted free surjection \(F_0\to V\). Order reduction proves that it is strict on a neighborhood. The graded kernel of this map is finite: the polynomial symbol sheaf is coherent by the uniform matrix-kernel result, and \(\operatorname{gr}V\) has finite presentation. Lift its finitely many homogeneous relations. At the base point subtract lower-order preimages of their images to obtain actual relations, exactly as in (6.19). Represent those finitely many equations nearby. The same descending-order argument shows that they generate \(K=\ker(F_0\to V)\) there, with its induced filtration.

Since \(t\) commutes with \(\mathcal A_I\), the preimage of \(tV\) in \(F_0\) is \(K+tF_0\). It is the image of one finite operator matrix. Part 1 gives this submodule a good induced filtration, and its quotient is precisely the image filtration on \(V/tV\). The quotient symbols are finite over \(\mathcal O_U[\xi_I]/(t)\), with coherent holomorphic degree pieces. When \(I\) is all the tangent directions, \(\mathcal A_I/t\mathcal A_I\) is the differential-operator sheaf of \(t=0\). This proves part 2. In particular it supplies a sheaf-level good filtration; stalk Noetherianity alone was not substituted for that assertion.

**Coordinate projections.** For \(p:U\times W\to U\), the stalk inclusion is \(H\to B\) in (6.18), after translating the chosen point to the origin. It is flat by the first argument. Thus the filtration pieces of \(p^*M\) are the actual pullbacks of those of \(M\), and

\[
\operatorname{gr}(p^*M)
=\mathcal O_{U\times W}\otimes_{p^{-1}\mathcal O_U}
 p^{-1}\operatorname{gr}M,\qquad
\xi_W\operatorname{gr}(p^*M)=0.
\tag{6.21}
\]

Coherent holomorphic pieces, a finite symbol presentation, and part 1 give coherence of the pulled-back operator module. The same flatness kills higher pullback Tor.

For precision about the support, a finite graded symbol module near \(y\) has a finite polynomial presentation. At a complex covector \((y,\eta)\), its analytified cokernel is nonzero exactly when its presentation matrix, evaluated at \(y,\eta\), is not surjective. This follows from Nakayama in the analytic local ring. The same rank test in \(H[\xi]_{(\mathfrak m_y,\xi-\eta)}\) gives the identical condition. In (6.21) this test is unchanged in the base cotangent directions and the new symbols act as zero. Its analytic support is therefore exactly \((y,w;\eta,0)\) with \((y,\eta)\in\operatorname{Ch}(M)\). This proves part 3. A holomorphic submersion is locally such a projection, so the result holds for all smooth analytic maps. \(\square\)

### Theorem 6.7. Full analytic non-characteristic pullback

Let \(f:X\to Y\) be any holomorphic map between complex manifolds, and \(M\) any coherent left analytic \(\mathcal D_Y\)-module. If (6.1) holds, then

\[
\begin{aligned}
\mathcal H^j(Lf^*M)&=0 &&(j\ne0),\\
\mathcal H^0(Lf^*M)&=f^*M
 &&\text{is coherent over }\mathcal D_X,\\
\operatorname{Ch}(f^*M)
 &=f_d\bigl(f_\pi^{-1}\operatorname{Ch}(M)\bigr).
\end{aligned}
\tag{6.22}
\]

There is no holonomicity, regularity, properness, or algebraicity hypothesis. Characteristic supports here are subsets of the analytic cotangent bundles. The shifted convention remains \(f^!=Lf^*[d_X-d_Y]\); its nonzero degree is consequently \(d_Y-d_X\), not generally zero.

**Proof for an analytic hypersurface.** Write \(X=\{t=0\}\), with holomorphic coordinates \((x_1,\ldots,x_n,t)\) on \(Y\). The earlier analytic coherence theorem gives a good filtration \(F\) of \(M\) on one neighborhood. Let \(E=\operatorname{gr}_F M\), a finite-presentation homogeneous module over \(\mathcal O_Y[\xi,\tau]\).

At a point \(y\in X\), non-characteristicity excludes every nonzero point of the normal \(\tau\)-axis from the symbol support. The rank test in Lemma 6.6 identifies that analytic statement with the corresponding support test for the polynomial module over the local coefficient ring \(H=\mathcal O_{Y,y}\). The homogeneous ideal \(\operatorname{Ann}E_y\), restricted to the axis over the residue field \(\mathbb C\), therefore has zero set contained in the origin. An ideal in \(\mathbb C[\tau]\) with that property contains a power of \(\tau\). A homogeneous lift supplies

\[
q(\xi,\tau)\in\operatorname{Ann}E_y
\quad\text{with a unit pure }\tau^d\text{ coefficient}.
\tag{6.23}
\]

Represent its finitely many coefficients and its equations on a finite list of symbol generators nearby. They hold on one smaller neighborhood. Normalize the unit coefficient there. Thus \(q\) is a monic polynomial in \(\tau\) annihilating the sheaf \(E\), not just its closed fiber. If \(d=0\), it is a unit and \(M=0\) nearby by bounded-below exhaustiveness; all claims follow.

Let \(\mathcal T\) be the tangent-operator algebra generated by holomorphic functions and the \(\partial_{x_j}\). For \(d>0\), monic division makes \(E\) finite over \(\mathcal S=\mathcal O_Y[\xi]\), with finite presentation on the same neighborhood. To see the latter explicitly, factor the symbol action through \(\mathcal S[\tau]/(q)\), a finite free \(\mathcal S\)-module. A finite presentation over \(\mathcal S[\tau]\) remains finite over this quotient. Multiplying each of its finitely many relation generators by \(1,\tau,\ldots,\tau^{d-1}\), and reducing by \(q\), presents its relation module over \(\mathcal S\). Use the original degree shifts and the homogeneous monic relation throughout. Thus \(F\) is a good \(\mathcal T\)-filtration with the finite-presentation hypothesis of Lemma 6.6.

Multiplication by \(t\) on \(M\) is injective. The full proof of Lemma 6.2 applies with holomorphic coefficients: the analytic cyclic submodule generated by \(u\) with \(tu=0\) is coherent; its characteristic support lies in that of \(M\); and the same axis test supplies an annihilating operator \(P\) with invertible pure normal leading coefficient \(a\). The commutator identity is still

\[
\operatorname{ad}_t^{\,d}(P)=(-1)^d d!a.
\tag{6.24}
\]

Every commutator kills \(u\), so \(u=0\). The submodule and support assertions used here hold analytically: finite presentations and the uniform image result give good induced filtrations, their graded exact sequences give support inclusion, and the stalk good-filtration comparison of the characteristic-variety lesson identifies this support with that of the cyclic quotient filtration. The coefficient ring being convergent rather than polynomial changes none of those finite filtered-ring identities.

Part 2 of Lemma 6.6 now makes \(N=M/tM\), with its image filtration, a coherent \(\mathcal D_X\)-module on a neighborhood. The two-term normal Koszul resolution has injective multiplication by \(t\) on \(M\), so \(Li^*M=N\) in degree zero. Its graded quotient has the actual map (6.6) over \((\mathcal O_Y/(t))[\xi]\); it does not acquire a normal-symbol action.

#### Equality, not only containment

At each base stalk write

\[
A=\mathcal T_y,\qquad S=H[\xi],\qquad
\operatorname{gr}\mathcal D_{Y,y}=S[\tau].
\tag{6.25}
\]

The Rees ring of \(A\) is left Noetherian. Indeed it is generated by \(H,h,h\partial_{x_j}\); auxiliary degree in the last generators gives associated graded \(H[h,\zeta]\), a Noetherian polynomial ring. Leading-symbol lifting with decreasing auxiliary degree proves the assertion. The filtration of \(M_y\) is good over \(A\) by (6.23), and the same holds for the quotient filtration by Lemma 6.6. Centrality of \(t\) in \(A\) and its injectivity on \(M_y\) have just been proved.

There are no vertical irreducible characteristic components. The full Noetherian rational-symbol involutivity theorem applies to the analytic operator stalk: it is filtered Noetherian by PBW and descending order, \(H[\xi,\tau]\) is commutative Noetherian over \(\mathbb Q\), the commutator lowers order by one, and \(M_y\) has a good filtration. That theorem proves involutivity separately for each minimal support prime \(\mathfrak p\). If \(t\in\mathfrak p\), then repeated brackets with \(t\) of the monic \(q\in\mathfrak p\) give

\[
(-1)^d\partial_\tau^d q=(-1)^d d!\in\mathfrak p,
\tag{6.26}
\]

a contradiction. Since the support is finite over \(S\), its image is \(\operatorname{Supp}_S E_y\). Every irreducible component of this image is the image of a full component; the projection preserves \(t\). Hence the image has no component contained in \(t=0\) either.

All hypotheses of the abstract central-specialization Lemma 6.4 are now verified at this analytic stalk. That lemma is a filtered-ring assertion, not a claim about algebraic varieties, and gives

\[
\operatorname{Supp}_{S}\operatorname{gr}N_y
=\operatorname{Supp}_{S}E_y\cap V(t).
\tag{6.27}
\]

This use retains its exact cancellation of Rees torsion and does not assume strict multiplication by \(t\).

It remains to interpret (6.27) as the analytic equality, rather than leave an algebraic spectrum in place of the cotangent bundle. At every \(y\in X\) and every tangent covector \(\xi_0\), the finite-presentation rank test from Lemma 6.6 identifies the left side at \((\mathfrak m_y,\xi-\xi_0)\) with \((y,\xi_0)\in\operatorname{Ch}_X N\). On the right, the finite algebra \(S[\tau]/(q)\) shows that this prime belongs to the projected support exactly when there is a point of the full support above it. The residue field of such a point is a finite extension of \(\mathbb C\), hence \(\mathbb C\); it specifies an actual normal covector \(\tau_0\). Nakayama, or the same presentation-matrix rank test, identifies it with \((y,\xi_0,\tau_0)\in\operatorname{Ch}_Y M\). The converse is immediate by localization. Thus (6.27) is precisely

\[
\operatorname{Ch}_X(M/tM)
=\operatorname{pr}_{\xi}
   \bigl(\operatorname{Ch}_Y(M)\cap\{t=0\}\bigr)
\tag{6.28}
\]

as analytic cotangent sets. Every complex covector is tested, not only the zero section. The monic equation also bounds all possible \(\tau\) over compact sets of \((y,\xi)\), so this projection of the closed analytic support is locally proper and has closed image. No properness assumption on the original hypersurface map or on a later \(f\) is used to supply the finite cotangent projection.

#### Every closed embedding and every holomorphic map

For a smooth analytic embedding, choose holomorphic normal coordinates \(t_1,\ldots,t_c\). At the chosen point its first normal line is contained in the full conormal space, so it is non-characteristic. The monic construction extends that condition to a neighborhood for the first restriction. After restricting, (6.28) says that every new characteristic covector lifts to an old one. If the new covector is normal to the remaining embedding, its lift belongs to the full original conormal space. Condition (6.1) makes it zero. This proves the hypothesis for the next restriction; shrink once at each of the finitely many stages. The Koszul and chain-rule composition of Section 2 uses only PBW structure-sheaf flatness and transfer multiplication, which hold for the holomorphic coordinates as well. It identifies the resulting degree-zero coherent module with \(Li^*M\). Successive cotangent projections compose to the original \(i_d i_\pi^{-1}\), proving (6.22) for the embedding.

Finally use the holomorphic graph factorization \(f=p\circ i\) in (6.7). Lemma 6.6 proves the exact smooth pullback and its characteristic equality for the projection \(p:X\times Y\to Y\). Its characteristic covectors along the graph are \((0,\eta)\), and pullback to the graph sends them to \(df^*\eta\). The graph is therefore non-characteristic exactly under (6.1). Apply the analytic embedding result and the canonical transfer composition

\[
Li^*Lp^*M\simeq Lf^*M.
\tag{6.29}
\]

All identifications are the actual tensor, multiplication and chain-rule maps, so the local results agree on overlaps. They give coherence, concentration, and the full equality for the original holomorphic map. \(\square\)

The algebraic proof in Theorem 6.5 and the analytic proof in Theorem 6.7 now establish the entire non-characteristic statement (6.2). Their common Rees lemma controls a possible failure of strictness; the analytic argument additionally supplies common-neighborhood coherence, holomorphic projection flatness, and the conversion of stalk support to analytic cotangent support.

## 7. Exercises with complete solutions

### Exercise 7.1 — easy: the shifted point fibers

Compute every $H^j(i_0^!\delta_0)$ and $H^j(i_0^!\mathcal O_{\mathbb A^1})$.

**Solution.** Formula (4.4) makes $\ker x$ on $\delta_0$ one-dimensional and $x$ surjective. In the two-term Koszul complex the only cohomology is therefore $H^{-1}=k$. Shifting by $[-1]$ moves it to degree zero: $H^0(i_0^!\delta_0)=k$ and all other groups vanish.

On $k[x]$, $x$ is injective with one-dimensional cokernel, so the Koszul cohomology is $k$ in degree zero. The same shift moves it to degree one: $H^1(i_0^!\mathcal O)=k$ and every other group is zero.

### Exercise 7.2 — easy: a pulled-back connection

Show directly that pulling back a flat connection produces the usual flat pullback connection.

**Solution.** Formula (1.2) differentiates a coefficient on $X$ and then applies the original connection through $df$. In a local frame with connection matrix $\Gamma=\sum_j\Gamma_jdy_j$, its matrix on $X$ is $\sum_j f^*(\Gamma_j)d(f^*y_j)$. Its curvature is the pullback of $d\Gamma+\Gamma\wedge\Gamma$, since pullback commutes with exterior differentiation and wedge product. The original curvature is zero, so the new one is zero. This is the connection in Proposition 1.1. A finite connection is locally free over $\mathcal O_Y$, so its derived pullback has no higher Tor.

### Exercise 7.3 — medium: a closed embedding followed by a smooth map

Prove (2.3) when $f:X\hookrightarrow Y$ is a closed embedding and $g:Y\to Z$ is smooth, and identify the resulting shift.

**Solution.** Locally let $x_1,\ldots,x_c$ be the equations of the embedding. Since $g$ is flat, $Lg^*M=g^*M$ for a module, or termwise pullback for a flat complex model. Its pullback by $f$ is the Koszul complex

\[
K(x_1,\ldots,x_c;\mathcal O_Y\otimes_{\mathcal O_Z}M).
\]

This computes $\mathcal O_X\otimes^L_{\mathcal O_Z}M$: the Koszul terms are locally free over $\mathcal O_Y$ and hence flat over $\mathcal O_Z$, while their augmentation resolves $\mathcal O_X$. The transfer chain-rule action is that of the composite by (2.4), so this is an isomorphism of differential-operator complexes, not just of vector spaces. If $g$ has relative dimension $r$, the total shift is $[-c][r]=[r-c]=[d_X-d_Z]$, proving $(gf)^!=f^!g^!$.

### Exercise 7.4 — medium: exponent multiplication

Pull back $\mathcal O_{\mathbb G_m}x^\lambda$ along $z\mapsto z^m$. Explain what may change for the affine-line extension.

**Solution.** The chain rule gives $\partial_ze=m\lambda z^{-1}e$, as in (5.1), so the answer on $\mathbb G_m$ is $\mathcal O z^{m\lambda}$. No higher Tor appears because the original connection is locally free.

For the affine-line Euler extension use (5.2), retaining the sign and integrality of the original $\lambda$. In particular a nonintegral $\lambda$ with integral $m\lambda$ pulls back to the full Laurent extension. The example $\lambda=1/2,m=2$ gives $L_z$, rather than $Q_1=J_z$. The cyclic presentation and the full tensor product have different generators at the ramification point.

### Exercise 7.5 — hard: holonomic pullback of a closed embedding

Use the general preservation theorem proved in *Preservation of holonomicity and minimal extensions*, Theorem 2.1. It is an explicitly assigned later result for this exercise. Deduce that $i^!K$ has holonomic cohomology for a smooth closed embedding $i:Z\hookrightarrow X$ and $K\in D_h^b(\mathcal D_X)$.

**Solution.** The cited internal Theorem 2.1 proves that $f^!$ preserves bounded holonomic complexes for every morphism of smooth varieties. By (0.1), undoing its dimension shift gives the same assertion for $Lf^*$. Applying this to $i$ gives $Li^*K\in D_h^b(\mathcal D_Z)$. Its additional shift is $[-c]$, which reindexes cohomology and preserves holonomicity. Therefore $i^!K\in D_h^b(\mathcal D_Z)$.

More concretely, (4.1) computes it by the finite Koszul total complex. For a module, the assumed theorem makes each of that complex's cohomology modules holonomic. For a bounded complex $K$, use the finite truncation triangles that assemble $K$ from its holonomic cohomology modules. Applying $Li^*$ preserves these triangles, and the holonomic Serre property makes the cohomology of each successive cone holonomic. This proves the complex version without identifying every individual Koszul term with a coherent $\mathcal D_Z$-module. The proof of the later preservation theorem uses its Proposition 1.1 on localization, the preceding adjunction lesson's Lemma 1.1 on the localization triangle, Kashiwara's Theorem 3.1 on supported modules, and this lesson's smooth Theorem 3.1 and composition Theorem 2.1. It does not use Exercise 7.5 or the non-characteristic equality in Theorem 6.5, so this forward reference introduces no proof cycle. The elementary Koszul formula alone would not establish holonomicity.

### Exercise 7.6 — hard: the opposite extension at its boundary

Compute the cohomology of $i_0^!J$, where $J=A_1/A_1(x\partial)$, and compare it with the Laurent extension.

**Solution.** In the basis from the duality chapter, $x$ sends $x^av$ to $x^{a+1}v$, and sends $\partial^bv$ to $-(b-1)\partial^{b-1}v$. Hence its kernel is $k\partial v$, while its cokernel is $kv$: the derivative branch is entirely in its image and the positive branch misses just $v$. Thus $Li_0^*J$ has $k$ in degrees $-1$ and $0$. Shifting by $[-1]$ gives

\[
H^0(i_0^!J)=k,\qquad H^1(i_0^!J)=k,
\]

with all other groups zero. Over a point every finite complex of vector spaces is isomorphic to the direct sum of its cohomology, so $i_0^!J\simeq k\oplus k[-1]$, with no preferred splitting asserted. For $L$, multiplication by $x$ is invertible and the entire derived fiber is zero. Their equal restrictions to $\mathbb G_m$ therefore do not determine their shifted fibers at zero.

## References and proof boundary

The chain-rule module structure, pullback of connections, derived transfer composition, smooth coherence and holonomicity, the Koszul formula, all point and projection examples, and the full ramified Euler pullback are proved here. All six exercises have complete solutions, with the fifth using its explicitly assigned later preservation theorem. The algebraic coherence, higher-Tor vanishing and characteristic containment for every non-characteristic map are proved in Proposition 6.3. Theorem 6.5 proves the full algebraic characteristic equality (6.2), using Lemma 6.4 to account exactly for non-strict filtration torsion. Lemma 6.6 proves the required uniform analytic tangent-operator and projection-flatness statements, and Theorem 6.7 proves coherence, concentration and characteristic equality for every non-characteristic holomorphic map and coherent analytic differential-operator module. Exercise 7.5 now uses the internal preservation Theorem 2.1 in the later lesson, with its proof inputs identified above. Exact prerequisite identities and proof boundaries distinguish these states.

Beilinson–Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), Section 7.2.8, treats ordinary left-module pullback and its relation with the differential-form formalism. The analytic non-characteristic reference is Schapira's *An introduction to D-modules*, draft v7, March 2020, Theorem 2.3.7 and Remark 2.3.8, with the conventions specified in Section 6. Kashiwara–Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §10.2, concerns a different result: a conditional normal-cone bound for induced systems and a regular-holonomic corollary. It is not the source of the general non-characteristic theorem or of the numbering 11.2.11–11.2.12.

For algebraic pullback and the point examples see Schnell, [*D-modules*](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Lecture 14, Definition 14.2, Examples 14.3–14.5 and Lemma 14.6. Theorem 16.5 gives non-characteristic pullback; its smooth case is discussed on pages 79–81. Theorem 18.5(b) is a supplementary statement of the preservation result now proved in the internal lesson used by Exercise 7.5.

[Stacks, Tag 0FL5](https://stacks.math.columbia.edu/tag/0FL5) concerns base change of the relative differential-form sheaves in a cartesian square. It supports the usual functorial differential-form background; it does not by itself assert the differential-operator transfer identity or arbitrary derived pullback composition proved in Section 2.
