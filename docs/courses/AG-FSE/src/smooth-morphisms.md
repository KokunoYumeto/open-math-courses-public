# Smooth morphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent AI review of this edition is not complete. Public domain (CC0).*

Smooth morphisms allow relative motion in a controlled number of directions. Their fibres are geometrically regular, their differentials form a vector bundle, and locally they factor through affine space by an étale map. Flatness is essential: a smooth fibre by itself says nothing about whether a family fits together smoothly.

We use the preceding lessons **Flatness criteria, dimension and the flat locus** and **Étale morphisms and their local structure**, together with the algebraic results in **Formally smooth, unramified and étale ring maps** and **Smooth algebras over a field and the Jacobian criterion**. Dimension means Krull dimension; $\dim_x X$ means the infimum of the dimensions of open neighbourhoods of $x$. For a finite type scheme over a field, it is the maximum dimension of the irreducible components through $x$, and generally differs from $\dim\mathcal O_{X,x}$.

## 1. Smooth charts and their relative dimension

An algebra is **smooth** if it is finitely presented and formally smooth, in the algebraic square-zero lifting sense. Equivalently, it is finitely presented and its naive cotangent complex is quasi-isomorphic to a finite projective module in degree zero. A scheme morphism is smooth at $x$ if suitable affine charts give a smooth algebra, and smooth if it is smooth everywhere [Stacks, Tag [01V5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-smooth)].

**Proposition 1.1 (standard charts).** If $f:X\to S$ is smooth at $x$ and $V=\operatorname{Spec}A$ is any affine neighbourhood of $f(x)$, there is an affine neighbourhood $U$ of $x$ mapping into $V$ with a presentation

$$
U=\operatorname{Spec}\left(A[X_1,\ldots,X_n]/(F_1,\ldots,F_c)\right)_{h\Delta},
\qquad
\Delta=\det\left(\frac{\partial F_i}{\partial X_j}\right)_{1\le i,j\le c}.
\tag{1.1}
$$

Conversely every such chart is smooth. On it $\Omega_{U/S}$ is free on $dX_{c+1},\ldots,dX_n$, and every nonempty fibre has pure dimension $n-c$.

**Proof.** Inside the inverse image of $V$, take a smooth affine chart. The algebraic local standard-smooth theorem gives the presentation (1.1); conversely the algebraic Jacobian lifting theorem makes this presentation smooth. The differential relations $dF_i=0$ can be solved uniquely for $dX_1,\ldots,dX_c$ using the invertible minor. Thus the remaining differentials are a basis. After any field base change the same minor is invertible. The field Jacobian criterion, or the regular-sequence dimension calculation in the polynomial ambient space, gives pure dimension $n-c$. All of these constructions commute with restriction to smaller charts. ∎

Thus $\Omega_{X/S}$ is finite locally free and

$$
\operatorname{rank}_x\Omega_{X/S}=\dim_x X_{f(x)}.
\tag{1.2}
$$

A smooth map has **relative dimension $d$** when this rank is the constant $d$. On a general smooth source the rank is locally constant and may differ between components [Stacks, Tags [01V7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-locally-standard-smooth), [02G1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-omega-finite-locally-free), [02G2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-smooth-relative-dimension)].

**Proposition 1.2 (permanence and flatness).** Smoothness is local on source and target and is preserved by composition and arbitrary base change. Smooth morphisms are flat, locally of finite presentation, syntomic and universally open.

**Proof.** Algebraic formal smoothness and finite presentation have the stated permanence properties, and the chart description gives the locality assertions. Alternatively, for composition, combine two standard presentations: the Jacobian minor for the combined equations is block triangular with the two invertible minors on its diagonal. Open immersions are smooth because localization is formally étale.

For flatness, apply Smooth algebras over a field and the Jacobian criterion, Theorem 6.1: every smooth algebra over an arbitrary commutative base is flat. Each chart (1.1) is therefore flat over its affine base. Locality of flatness passes this assertion to the scheme morphism, without a Noetherian assumption on $S$.

Here syntomic means flat and locally of finite presentation with local complete-intersection fibres. In a fibre chart the ambient polynomial local ring is regular, the quotient is regular of codimension $c$, and the ideal has $c$ generators. The Cohen–Macaulay regular-sequence criterion makes those generators a regular sequence. Thus the fibres are local complete intersections. Finally every base change remains flat and locally of finite presentation, so the openness theorem of **Flat morphisms** proves universal openness. ∎

See [Stacks, Tags [01VA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-smooth), [01VB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-smooth), [01VC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-open-immersion-smooth), [01VD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-syntomic), [01VE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-locally-finite-presentation), [01VF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-flat), [056G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-open)]. Local finite presentation does not imply quasi-compactness; smooth maps need not be finitely presented globally.

## 2. Over a field: regularity must be geometric

For $X$ locally of finite type over $k$, **geometric regularity at $x$** means that for every extension field $K/k$, every local ring at a point of $X_K$ above $x$ is regular.

**Theorem 2.1.** Such an $X$ is smooth at $x$ if and only if it is geometrically regular at $x$. A smooth $k$-scheme is geometrically regular, geometrically normal and geometrically reduced [Stacks, Tags [038X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-geometrically-regular-smooth), [056T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-smooth-geometrically-normal)].

**Proof.** If $X$ is smooth at $x$, choose a smooth neighbourhood. Every field base change is smooth; smooth finite type algebras over a field have regular local rings by the algebraic field criterion. This proves geometric regularity. Regular Noetherian local rings are normal domains and reduced, giving the last assertions after every field extension.

Conversely choose an algebraically closed field $K$ containing $\kappa(x)$. Evaluation at $x$ gives a $K$-rational closed point $z\in X_K$ above $x$. Geometric regularity makes $\mathcal O_{X_K,z}$ regular. At a rational closed point the cotangent sequence identifies

$$
\Omega_{X_K/K,z}\otimes K\simeq\mathfrak m_z/\mathfrak m_z^2.
$$

Its dimension is therefore $\dim\mathcal O_{X_K,z}=\dim_z X_K$. Dimension at a point of a finite type field-scheme is unchanged by a field extension at points above it, so this is $\dim_x X$. Differential base change identifies the left-hand vector space with $(\Omega_{X/k,x}\otimes\kappa(x))\otimes_{\kappa(x)}K$. The algebraic field criterion, “cotangent dimension at most $\dim_x X$,” now proves smoothness at $x$. ∎

Here is the explicit Jacobian test. On a chart

$$
X=\operatorname{Spec}k[X_1,\ldots,X_n]/(F_1,\ldots,F_m),
$$

the conormal sequence presents $\Omega_{X/k}\otimes\kappa(x)$ as the cokernel of the Jacobian matrix $J=(\partial F_i/\partial X_j)(x)$. Hence

$$
\dim_{\kappa(x)}\Omega_{X/k}\otimes\kappa(x)
=n-\operatorname{rank}J(x).
$$

The field criterion gives

$$
X\text{ smooth at }x
\quad\Longleftrightarrow\quad
\operatorname{rank}J(x)=n-\dim_x X.
\tag{2.1}
$$

The equality uses the dimension at this point, not the largest component dimension elsewhere on $X$. Over a perfect field, every finitely generated residue extension is separably generated, so regular local rings of finite type schemes are smooth points by the algebraic separable-residue criterion. Over an imperfect field this conclusion fails.

For example, over $k=\mathbf F_p(t)$ the algebra $L=k[u]/(u^p-t)$ is a field. The polynomial is irreducible since $t\notin k^p$, so $L$ is a regular zero-dimensional local ring. Its differential module is $L\,du$, of dimension one; (2.1) says it is not smooth. After extending to a field containing $t^{1/p}$, the algebra becomes $K[v]/(v^p)$, which is nonreduced.

## 3. From smooth fibres to a smooth family

**Theorem 3.1 (fibrewise criterion).** Suppose $f:X\to S$ is locally of finite presentation, $x\in X$ and $s=f(x)$. Then $f$ is smooth at $x$ if and only if $\mathcal O_{X,x}$ is flat over $\mathcal O_{S,s}$ and $X_s$ is smooth at $x$. In particular, flatness, local finite presentation and smoothness of every fibre characterize smooth morphisms [Stacks, Tags [01V8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-flat-smooth-fibres), [01V9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-at-point)].

**Proof.** Necessity follows from Proposition 1.2 and base change. For sufficiency use affine charts $B=A[X_1,\ldots,X_n]/I$, with $I$ finitely generated. Let $\mathfrak q$ represent $x$, $\mathfrak p=\mathfrak q\cap A$, and $k=\kappa(\mathfrak p)$. Write $d=\dim_x X_s$ and $c=n-d$. The field criterion gives Jacobian rank $c$ in the fibre. Choose $F_1,\ldots,F_c\in I$ and $c$ variables giving a minor $\Delta$ nonzero at $\mathfrak q$. Then

$$
C=\left(A[X_1,\ldots,X_n]/(F_1,\ldots,F_c)\right)_\Delta
\twoheadrightarrow B_\Delta
\tag{3.1}
$$

has standard smooth source. Let $\mathfrak r$ be the inverse image of $\mathfrak q$. Its kernel is finitely generated.

In the fibre, the local map $C_{\mathfrak r}/\mathfrak pC_{\mathfrak r}\twoheadrightarrow B_{\mathfrak q}/\mathfrak pB_{\mathfrak q}$ is a surjection of regular local domains. Both have the same local dimension

$$
d-\operatorname{trdeg}_k\kappa(x).
$$

For the source this follows from its standard smooth relative dimension $n-c=d$; for the target from smoothness of the fibre at $x$. The residue fields are identical. A nonzero ideal in a Noetherian local domain lowers dimension: prepend the zero prime to any chain of primes containing that ideal. Thus this surjection of domains of equal dimension is an isomorphism.

Let $K$ be the kernel of $C_{\mathfrak r}\to B_{\mathfrak q}$. Tensoring its exact sequence with $k$ is injective on $K/\mathfrak pK$, because $B_{\mathfrak q}$ is flat over $A_{\mathfrak p}$. The fibre isomorphism just proved gives $K/\mathfrak pK=0$. Since $K$ is finite over the local ring $C_{\mathfrak r}$, Nakayama gives $K=0$. Finitely many kernel generators therefore vanish after one principal localization avoiding $\mathfrak r$. There (3.1) is an isomorphism, exhibiting a smooth neighbourhood of $x$. ∎

Finite presentation was used exactly to make the quotient kernel finite. No Noetherian hypothesis on $A$ entered the proof.

The pointwise differential versions follow as well. Under local finite presentation, smoothness at $x$ is equivalent to flatness at $x$ together with either

$$
\dim_{\kappa(x)}(\Omega_{X/S,x}\otimes\kappa(x))\le\dim_x X_s,
$$

or the assertion that $\Omega_{X/S,x}$ has at most $\dim_x X_s$ generators. Differential base change gives the fibre cotangent space, the field criterion gives fibre smoothness, and Nakayama equates these two formulations.

## 4. Étale coordinates and the dimension formula

**Theorem 4.1 (étale coordinates).** If $f:X\to S$ is smooth at $x$, and $V\subset S$ is an affine neighbourhood of $s=f(x)$, there are an affine neighbourhood $U$ of $x$ and an integer $d\ge0$ with a factorization

$$
U\xrightarrow{\pi}\mathbf A^d_V\longrightarrow V,
\qquad \pi\text{ étale}.
\tag{4.1}
$$

More generally, if $g_1,\ldots,g_d$ are local functions whose differentials form a basis of $\Omega_{X/S}\otimes\kappa(x)$, their coordinate map to $\mathbf A^d_V$ is étale at $x$ [Stacks, Tags [054L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-etale-over-affine-space), [039Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-smooth-etale-over-n-space)].

**Proof.** In a standard chart (1.1), take the last $n-c=d$ variables as coordinates on affine space. The remaining $c$ variables and $c$ equations have an invertible square Jacobian, so the map to affine space is étale by the preceding lesson.

For the asserted choice of arbitrary coordinates, shrink so that $dg_i$ form a basis of the differential bundle. The differential sequence gives $\Omega_{X/\mathbf A^d_V,x}=0$, so the coordinate map is unramified at $x$. It is locally of finite presentation: in an affine presentation, add the finitely many equations identifying the new base coordinates with $g_i$.

On the fibre over $s$, the source and target are regular schemes of geometric dimension $d$. Unramifiedness makes $\kappa(x)$ finite separable over the residue field at $t=\pi(x)$. Their local rings therefore both have dimension $d-\operatorname{trdeg}_{\kappa(s)}\kappa(x)$. Miracle flatness, with regular target local ring and Cohen–Macaulay source local ring, makes this fibre coordinate map flat at $x$.

Now apply the general fibrewise flatness criterion from **Flatness criteria, dimension and the flat locus** to the local diagram

$$
\mathcal O_{S,s}\longrightarrow
\mathcal O_{\mathbf A^d_V,t}\longrightarrow\mathcal O_{X,x}.
$$

The last ring is flat over the first because $f$ is smooth; its fibre is flat over the middle ring's fibre by the previous paragraph. The presentation hypotheses hold for the coordinate map. The criterion makes $\pi$ flat at $x$. Flatness and G-unramifiedness then make it étale at $x$. Shrinking gives the desired factorization. ∎

**Proposition 4.2 (dimensions).** For smooth $f:X\to S$ between locally Noetherian schemes,

$$
\dim_x X=\dim_s S+\dim_x X_s.
\tag{4.2}
$$

**Proof.** First an étale map preserves $\dim$ of local rings by the preceding lesson. Since it is open, it also preserves geometric dimension at a point. Indeed, for every source open $W$,

$$
\dim W=\sup_{w\in W}\dim\mathcal O_{W,w}
=\sup_{v\in f(W)}\dim\mathcal O_{S,v}=\dim f(W).
$$

Take infima over neighbourhoods of the point. Their open images are neighbourhoods of its image; conversely intersect a fixed source neighbourhood with the inverse image of any target neighbourhood. This gives equality of the two infima.

For the projection $p:\mathbf A^d_S\to S$, let $W$ be an affine open neighbourhood of a point $t$ above $s$. The flat local dimension formula gives, for $w\in W$,

$$
\dim\mathcal O_{W,w}
=\dim\mathcal O_{S,p(w)}+\dim\mathcal O_{W_{p(w)},w}.
$$

The last term is at most $d$. For each $v\in p(W)$, the nonempty open $W_v\subset\mathbf A^d_{\kappa(v)}$ contains a closed point, at which that term is $d$. Taking suprema gives $\dim W=\dim p(W)+d$. The image is open, and neighbourhoods obtained from the inverse image of target opens show, on taking infima, that $\dim_t\mathbf A^d_S=\dim_s S+d$.

Apply the étale factorization (4.1); here $d=\dim_x X_s$. This proves (4.2), also with infinite dimensions interpreted in the usual extended sense. ∎

The separate local-ring formula is

$$
\dim\mathcal O_{X,x}=\dim\mathcal O_{S,s}+\dim\mathcal O_{X_s,x}.
$$

It uses the height at $x$ in the fibre. For example, at the generic point of $\mathbf A^1_k$, the local ring has dimension zero while $\dim_x\mathbf A^1_k=1$. Formula (4.2) concerns the latter [Stacks, Tag [0AFF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smoothness-dimension)].

## 5. Slicing and étale-local sections

**Lemma 5.1 (a smooth slice).** Let $f$ be smooth of relative dimension $d$ at $x$, and let $h\in\mathfrak m_x$ have $dh$ nonzero in $\Omega_{X/S}\otimes\kappa(x)$. After shrinking around $x$, $V(h)$ is an effective Cartier divisor and is smooth over $S$ of relative dimension $d-1$.

**Proof.** Complete $dh$ to a basis of the differential bundle by differentials of local functions. Theorem 4.1 makes their coordinate map étale, with $h$ as first coordinate. In affine space the first coordinate is a nonzerodivisor over every base ring, and its zero subscheme is $\mathbf A^{d-1}_S$. Flatness of the étale coordinate map preserves this nonzerodivisor. Its zero subscheme is a base change of the étale chart to $\mathbf A^{d-1}_S$, hence is smooth of relative dimension $d-1$. ∎

If the map $\Omega_{X_s/\kappa(s),x}\otimes\kappa(x)\to\Omega_{\kappa(x)/\kappa(s)}$ has a nonzero kernel, the cotangent sequence for the fibre supplies such an $h$: lift an element of the fibre maximal ideal whose differential represents a nonzero kernel element. Thus the lemma includes both slicing forms [Stacks, Tags [057C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-slice-smooth-given-element), [057D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-slice-smooth-once)].

**Theorem 5.2 (étale-local sections).** If $f:X\to S$ is smooth and $s$ is in its image, there is an étale morphism $T\to S$, a point $t$ above $s$, and an $S$-morphism $T\to X$. Equivalently $X\times_S T\to T$ has a section [Stacks, Tag [055U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-nbhd-dominates-smooth)].

**Proof.** We first produce a point of the fibre with finite separable residue extension. Take a nonempty smooth affine open of $X_s$ and an étale chart to affine space. Extend to a separable closure $k^{\mathrm{sep}}$ of $k=\kappa(s)$. The chart has nonempty open image. The infinite field $k^{\mathrm{sep}}$ has a rational point in every nonempty affine-space open: a nonzero polynomial cannot vanish on all tuples over an infinite field. The étale fibre there consists of finite separable extensions of $k^{\mathrm{sep}}$, hence of copies of that field. A rational point in the chart uses only finitely many elements of $k^{\mathrm{sep}}$ and descends to a finite separable extension of $k$. Its image $x_0\in X_s$ is closed with $L=\kappa(x_0)$ finite separable over $k$.

Realize $L=k[\alpha]$ by a monic separable polynomial. On an affine neighbourhood $V=\operatorname{Spec}A$ of $s$, lift its coefficients from $k$ to $A$ after clearing denominators and shrinking $V$. The corresponding monic polynomial defines a standard étale neighbourhood $S'\to V$, localized at its derivative, with a point $s'$ whose residue field is $L$. The fibre product $X\times_S S'$ has a rational point $x'$ above $s'$ determined by the identity on $L$.

Near $x'$ choose an étale chart $U\to\mathbf A^d_{S'}$. Lift the coordinate values of $x'$ from $\kappa(s')$ to functions on an affine neighbourhood of $s'$, shrinking again to clear denominators. They define a section $a:S'\to\mathbf A^d_{S'}$. Set

$$
T=U\times_{\mathbf A^d_{S'},a}S'.
$$

The map $T\to S'$ is étale by base change, and $T$ contains the point specified by $x'$ and $s'$. Thus $T\to S$ is an étale neighbourhood of $s$, and the projection $T\to U\to X$ is the required morphism. Its graph is the section of $X\times_S T\to T$. ∎

This asserts a section over every point in the image. It does not require that a section pass through an arbitrary specified fibre point with transcendental residue extension.

## 6. Generic smoothness and its hypotheses

There are two distinct useful statements.

**Theorem 6.1 (generic smoothness on the source).** Let $f:X\to Y$ be a dominant finite type morphism of integral Noetherian schemes, with $\operatorname{char}K(Y)=0$. There is a dense open $W\subset X$ on which $f$ is smooth, of relative dimension $\operatorname{trdeg}_{K(Y)}K(X)$.

**Proof.** At the generic points, the local map is the field extension $K(Y)\to K(X)$ and is flat. The generic fibre is of finite type over $K(Y)$ and is regular at its generic point, whose local ring is $K(X)$. In characteristic zero the finitely generated residue extension is separably generated. The algebraic separable-residue criterion gives smoothness of the generic fibre at that point. Theorem 3.1 makes $f$ smooth at the generic point of $X$; its smooth locus is open. The rank of its differential bundle at that point is the dimension of $\Omega_{K(X)/K(Y)}$, namely the stated transcendence degree. Shrink to the open locus of that constant rank. ∎

For varieties over a characteristic-zero field, this relative dimension is $\dim X-\dim Y$.

**Theorem 6.2 (generic smoothness on the target).** Let $k$ have characteristic zero and let $f:X\to Y$ be a dominant morphism of integral $k$-varieties with $X$ smooth over $k$. There is a dense open $V\subset Y$ such that the entire map $f^{-1}(V)\to V$ is smooth.

**Proof.** The generic fibre is regular: its local rings are local rings of $X$ at points over the generic point of $Y$, since passing to $K(Y)$ merely inverts functions already outside those primes. They are regular because $X$ is smooth over $k$. The characteristic-zero field $K(Y)$ is perfect, so every point of this regular finite type fibre is smooth. Flatness over $K(Y)$ is automatic. Theorem 3.1 therefore says that every point of the generic fibre is in the smooth locus of $f$.

Let $Z$ be the closed complement of that locus. Chevalley's theorem makes $f(Z)$ constructible. It does not contain the generic point of $Y$. A constructible subset of an irreducible Noetherian space whose closure is the whole space contains a nonempty open and hence contains the generic point. Consequently $\overline{f(Z)}\ne Y$. Take $V=Y\setminus\overline{f(Z)}$. Every point over $V$ is smooth. ∎

For a nondominant morphism into an integral variety, removing the closure of its image gives a dense target open with empty inverse image; the meaningful nonempty-family statement is the dominant version above. These are Vakil's *The Rising Sea*, Theorems 21.6.4 and 21.6.6, with their different source hypotheses kept explicit.

The smooth-source hypothesis in Theorem 6.2 cannot be dropped. Over characteristic zero, let $C=\operatorname{Spec}k[u,v]/(v^2-u^3)$ and project $C\times_k\mathbf A^1_k$ to the second factor. This is a dominant morphism of integral varieties, but every fibre has the cusp: its differential Jacobian vanishes at $u=v=0$, so it is not smooth. No nonempty target open makes the whole family smooth. The source statement still holds off the singular section.

In characteristic $p$, the Frobenius map $\mathbf A^1_{\mathbf F_p}\to\mathbf A^1_{\mathbf F_p}$, $t=z^p$, is finite free of rank $p$ and universally bijective. Every geometric fibre has algebra $K[z]/((z-a)^p)$ and is nonreduced. It is smooth at no point. Its differential module over the target is nevertheless free of rank one, while its geometric fibres have dimension zero. Thus flatness, finite presentation and a locally free differential module without the correct fibre dimension do not characterize smoothness.

## 7. Examples and exercises

Affine space is smooth over any base by its polynomial charts. Projective space is smooth by its affine-space cover. The groups $\mathbf G_m$ and $\mathrm{GL}_n$ are open subschemes of affine space, obtained by inverting a coordinate and the determinant respectively. A hypersurface has a smooth chart wherever one partial derivative is invertible; redundant or zero equations are handled by the full rank criterion (2.1).

For $\operatorname{char}k\ne2,3$, the plane cubic $y^2=x^3+ax+b$ is smooth exactly when

$$
4a^3+27b^2\ne0.
$$

Indeed its nonsmooth points satisfy $y=0$, $3x^2+a=0$ and $x^3+ax+b=0$. These give $a=-3r^2$, $b=2r^3$ at a nonsmooth point $r$, and force the displayed discriminant to vanish. Conversely if it vanishes, $r=0$ works when $a=0$; when $a\ne0$, $r=-3b/(2a)$ gives precisely those two identities and produces the nonsmooth point.

The family $y^2=x^3+t$ has total space isomorphic to $\mathbf A^2_k$ by eliminating $t$, so its total space is smooth over $k$. Its projection to $\mathbf A^1_t$ is a different question, resolved below.

**Exercise 1 (easy).** Determine the nonsmooth locus of $y^2=x^3+ax+b$ when $\operatorname{char}k\ne2,3$, and recover the discriminant condition.

**Exercise 2 (medium).** Prove that $\operatorname{Spec}\mathbf F_p(t^{1/p})$ is regular but not smooth over $\mathbf F_p(t)$, using both differentials and geometric reducedness.

**Exercise 3 (medium).** Prove that a smooth morphism of relative dimension zero is étale, and conversely.

**Exercise 4 (medium).** Determine the smooth locus of $y^2=x^3+t$ over $\mathbf A^1_t$ in characteristic different from $2,3$, and in characteristic $3$. Compare relative smoothness with smoothness of the total space.

**Exercise 5 (hard).** Choose local functions whose differentials form a basis for a smooth morphism at $x$. Prove their map to affine space is étale at $x$, explicitly using miracle flatness on the fibre and the general fibrewise flatness criterion.

## 8. Solutions

**Solution 1.** Put $F=y^2-x^3-ax-b$. The curve has pure dimension one. Its Jacobian has entries $-3x^2-a$ and $2y$. Thus its nonsmooth locus is cut out on the curve by $y=0$ and $3x^2+a=0$. At a point $x=r$ the equation gives $r^3+ar+b=0$, equivalent to $a=-3r^2$ and $b=2r^3$. Hence $4a^3+27b^2=0$. Conversely when this expression is zero and $a\ne0$, set $r=-3b/(2a)$. Direct substitution gives $r^2=-a/3$ and $2r^3=b$, so $(r,0)$ is nonsmooth. If $a=0$, the vanishing discriminant gives $b=0$ and the nonsmooth point is $(0,0)$. These calculations work over $k$ itself; they also determine the geometric nonsmooth locus.

**Solution 2.** The polynomial $U^p-t$ is irreducible over $k=\mathbf F_p(t)$: a $p$th root of $t$ cannot be a rational function, since its $t$-adic valuation would be $1/p$ whereas rational functions have integral valuation. A purely inseparable polynomial of degree $p$ without a root is irreducible. Its quotient is the field $L=\mathbf F_p(t^{1/p})$, hence a regular local ring of dimension zero. The relation has derivative zero, so $\Omega_{L/k}=L\,dU$, contradicting the cotangent dimension required for smoothness. After base change to $L$ the polynomial becomes $(U-t^{1/p})^p$, and $L\otimes_k L\simeq L[V]/(V^p)$ is nonreduced. Smoothness would imply geometric reducedness, giving the second obstruction.

**Solution 3.** For a smooth relative-dimension-zero map, $\Omega_{X/S}$ is locally free of rank zero and therefore zero. It is smooth and unramified, so the equivalence theorem in **Étale morphisms and their local structure** makes it étale. Conversely an étale map is smooth with zero differentials, so its relative dimension is zero. No quasi-compactness assertion is involved.

**Solution 4.** As a polynomial in $y$, $y^2-x^3-t$ is monic, so the coordinate algebra is free of rank two over $k[t,x]$ and is flat over $k[t]$. Every fibre has pure dimension one. In characteristic different from $2,3$, the relative Jacobian is $(-3x^2,2y)$; both entries vanish exactly at $x=y=0$, which forces $t=0$. The family is smooth everywhere else. In characteristic $3$, the relative Jacobian is $(0,2y)$, so its nonsmooth locus is the whole curve $y=0$, $t=-x^3$ in the total space. Every geometric fibre has a point on this curve. Thus in characteristic $3$ no nonempty base open makes the entire restricted family smooth. In both cases the total space is $\operatorname{Spec}k[x,y]$ and is smooth over $k$; solving for $t$ does not turn its projection into a smooth morphism.

**Solution 5.** Let $d=\dim_xX_s$ and let $\pi$ be the coordinate map defined by $g_1,\ldots,g_d$. Shrink to make their differentials a basis. The right-exact differential sequence makes $\Omega_{X/\mathbf A^d_S}=0$, so $\pi$ is unramified there, and its finite presentation follows by adjoining equations for the $g_i$ to a finite presentation of $X/S$.

On the fibre, let $t=\pi(x)$, $R=\mathcal O_{\mathbf A^d_{\kappa(s)},t}$, and $M=\mathcal O_{X_s,x}$. Both are regular local rings, and $M$ is therefore Cohen–Macaulay. Unramifiedness makes the fibre $\operatorname{Spec}M$ over $R$ a point and makes $\kappa(x)/\kappa(t)$ finite separable. The source and target have geometric dimension $d$, so

$$
\dim M=d-\operatorname{trdeg}_{\kappa(s)}\kappa(x)
=d-\operatorname{trdeg}_{\kappa(s)}\kappa(t)=\dim R.
$$

The miracle-flatness equality $\dim M=\dim R+\dim(M/\mathfrak m_RM)$ holds because the last dimension is zero. Hence $M$ is flat over $R$. Finally apply the general fibrewise criterion to $\mathcal O_{S,s}\to\mathcal O_{\mathbf A^d_S,t}\to\mathcal O_{X,x}$: the last ring is flat over the base by smoothness, and its base fibre is flat over the middle base fibre by the miracle-flatness argument. All essential finite-presentation hypotheses hold. Thus $\pi$ is flat at $x$. Its G-unramifiedness and flatness make it étale at $x$, and the open étale locus gives the required neighbourhood.

## What this lesson does not prove

- The algebraic local standard-smooth theorem and the conormal/Jacobian lifting criterion are imported from **Formally smooth, unramified and étale ring maps** [Stacks, Tags [00T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-standard-smooth), [00TA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-smooth-syntomic)]. Proposition 1.1 passes those exact algebraic statements to schemes.
- The field criterion $\dim_{\kappa(x)}\Omega_{X/k}\otimes\kappa(x)\le\dim_xX$ and the regularity criterion with separably generated residue extension come from **Smooth algebras over a field and the Jacobian criterion** [Stacks, Tags [00TT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-smooth-over-field), [00TV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-separable-smooth)]. We also import its Theorem 6.1, which proves smooth-flatness over an arbitrary commutative base; Proposition 1.2 makes the scheme-local application.
- The dimension of a finite type field-scheme at a point is preserved by field extensions, and at a rational closed point equals the local-ring dimension Stacks, Tags [00P4, [00OU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-closed-point-finite-type-field)]. Also $\dim_x X=\dim\mathcal O_{X,x}+\operatorname{trdeg}_k\kappa(x)$ [Stacks, Tag [00P1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-at-a-point-finite-type-field)]. These are the affine dimension results used in Sections 2–4; they follow from Noether normalization and the dimension formulas of **Krull dimension and Noether normalization**. The cotangent-space identification at a separable closed point follows from the separable coefficient-field lift modulo the square of the maximal ideal [Stacks, Tag [00TU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-computation-differential)].
- Regular Noetherian local rings are Cohen–Macaulay, normal and reduced; a $c$-generated ideal of height $c$ in a Cohen–Macaulay local ring is generated by a regular sequence. These are prerequisites from **Regular local rings** and **Regular sequences, depth and Cohen–Macaulay modules**.
- Chevalley's constructibility theorem is imported from **Quasi-finite morphisms and Chevalley's theorem**. Theorem 6.2 uses it only to remove the image of the nonsmooth locus.

The fibrewise criterion, étale coordinates, smooth slices, étale-local sections, dimension comparison and both generic-smoothness statements have been proved here. Our main references are the Stacks Project and Vakil's *The Rising Sea*, §§13.6, 21.6 and 24.8. The next lesson makes the scheme infinitesimal lifting properties precise and proves invariance of étale morphisms under nilpotent thickenings.
The written internal providers are Krull dimension and Noether normalization for the affine dimension results, Regular sequences, depth and Cohen–Macaulay modules and Regular local rings for the local algebra, and Quasi-finite morphisms and Chevalley’s theorem, Section 5, Theorem 5.1, for constructibility. The arbitrary-base smooth-flatness proof is the exact Theorem 6.1 of the commutative-algebra lesson already cited above.
