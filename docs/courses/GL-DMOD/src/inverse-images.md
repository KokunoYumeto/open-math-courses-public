# Inverse images

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

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

\
\xi\bigl(\zeta(f^*y_j)\bigr)
-\zeta\bigl(\xi(f^*y_j)\bigr)
=[\xi,\zeta.
\]

The terms containing two $\partial_y$ commute and cancel, and the remaining action on $b$ is $\xi,\zeta$. Hence $[\nabla^f_\xi,\nabla^f_\zeta]=\nabla^f_{[\xi,\zeta]}$. The relations for functions and vector fields defining $\mathcal D_X$ are all satisfied. This constructs its action and proves uniqueness. The construction in terms of $df$ glues across coordinate changes.

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

The analytic statement is Kashiwara–Schapira, Definition 11.2.11 and Proposition 11.2.12. An algebraic version, with non-characteristic expressed as finiteness of $f_d$ on the pulled-back conic support, is Schnell, [*D-modules*, Theorem 16.5](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), pages 79–83. For conic support the kernel condition and that finiteness condition agree. The general theorem is stated here; the smooth case was proved completely in Section 3.

At the origin of a line, the polynomial connection is non-characteristic and $\delta_0$ is characteristic. Their Koszul computations show the corresponding presence or absence of higher pullback cohomology. For $m>1$, $f_m$ is characteristic at zero for $Q_\lambda$, whose characteristic support includes the whole cotangent fiber there. Nevertheless its flatness eliminates higher Tor in Section 5. Non-characteristic is a sufficient condition, and its failure does not force higher cohomology in every example.

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

Assume the general preservation theorem assigned to the later chapter *Preservation of holonomicity and minimal extensions*. Deduce that $i^!K$ has holonomic cohomology for a smooth closed embedding $i:Z\hookrightarrow X$ and $K\in D_h^b(\mathcal D_X)$.

**Solution.** The assumed theorem says that $Lf^*$ sends bounded complexes with holonomic cohomology to such complexes on the source for every morphism of smooth varieties. A confirmed external formulation is Schnell, Theorem 18.5(b), page 91. Applying it to $i$ gives $Li^*K\in D_h^b(\mathcal D_Z)$. Its additional shift is $[-c]$, which reindexes cohomology and preserves holonomicity. Therefore $i^!K\in D_h^b(\mathcal D_Z)$.

More concretely, (4.1) computes it by the finite Koszul total complex. For a module, the assumed theorem makes each of that complex's cohomology modules holonomic. For a bounded complex $K$, use the finite truncation triangles that assemble $K$ from its holonomic cohomology modules. Applying $Li^*$ preserves these triangles, and the holonomic Serre property makes the cohomology of each successive cone holonomic. This proves the complex version without identifying every individual Koszul term with a coherent $\mathcal D_Z$-module. The general preservation theorem is the explicit hypothesis of this exercise, not a consequence of the elementary Koszul formula alone.

### Exercise 7.6 — hard: the opposite extension at its boundary

Compute the cohomology of $i_0^!J$, where $J=A_1/A_1(x\partial)$, and compare it with the Laurent extension.

**Solution.** In the basis from the duality chapter, $x$ sends $x^av$ to $x^{a+1}v$, and sends $\partial^bv$ to $-(b-1)\partial^{b-1}v$. Hence its kernel is $k\partial v$, while its cokernel is $kv$: the derivative branch is entirely in its image and the positive branch misses just $v$. Thus $Li_0^*J$ has $k$ in degrees $-1$ and $0$. Shifting by $[-1]$ gives

\[
H^0(i_0^!J)=k,\qquad H^1(i_0^!J)=k,
\]

with all other groups zero. Over a point every finite complex of vector spaces is isomorphic to the direct sum of its cohomology, so $i_0^!J\simeq k\oplus k[-1]$, with no preferred splitting asserted. For $L$, multiplication by $x$ is invertible and the entire derived fiber is zero. Their equal restrictions to $\mathbb G_m$ therefore do not determine their shifted fibers at zero.

## References and proof boundary

The chain-rule module structure, pullback of connections, derived transfer composition, smooth coherence and holonomicity, the Koszul formula, all point and projection examples, and the full ramified Euler pullback are proved here. All six exercises have complete solutions, with the fifth using its explicitly assigned later preservation theorem. The general non-characteristic theorem and the general preservation theorem used in that exercise are stated external inputs.

Beilinson–Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), Section 7.2.8, treats ordinary left-module pullback and its relation with the differential-form formalism. Non-characteristic pullback of analytic D-modules is treated in M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §10.2.

For algebraic pullback and the point examples see Schnell, [*D-modules*](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Lecture 14, Definition 14.2, Examples 14.3–14.5 and Lemma 14.6. Theorem 16.5 gives non-characteristic pullback; its smooth case is discussed on pages 79–81. Theorem 18.5(b) is the stated preservation input for Exercise 7.5.

[Stacks, Tag 0FL5](https://stacks.math.columbia.edu/tag/0FL5) concerns base change of the relative differential-form sheaves in a cartesian square. It supports the usual functorial differential-form background; it does not by itself assert the differential-operator transfer identity or arbitrary derived pullback composition proved in Section 2.
