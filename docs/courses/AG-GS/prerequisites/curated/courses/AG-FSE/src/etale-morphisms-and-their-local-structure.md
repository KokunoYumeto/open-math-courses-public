# Étale morphisms and their local structure

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An étale morphism combines the absence of relative infinitesimal motion with flatness. Its fibres are separable points, but those points need not form separate Zariski sheets. Over a field of characteristic different from two, the map taking an invertible coordinate to its square already exhibits this distinction. The main algebraic result of this lesson is more precise: near any point, an étale morphism is described by a monic polynomial whose derivative is invertible.

We use **Flat morphisms**, **Flatness criteria, dimension and the flat locus**, and **Unramified morphisms**. The algebraic prerequisites are **Formally smooth, unramified and étale ring maps**, **Smooth algebras over a field and the Jacobian criterion**, and **Zariski's Main Theorem**. For local-ring properties we also use the depth and normality criteria from **Regular sequences, depth and Cohen–Macaulay modules** and **Discrete valuation rings, normal rings and Serre's criterion**. Exact imported statements appear at the end.

## 1. A definition and its geometric tests

An $A$-algebra is **étale** if it is finitely presented and formally étale: every $A$-algebra map to a quotient by a square-zero ideal has a unique lift. A scheme morphism is étale at $x$ if it has étale affine charts around $x$ and its image, and is étale if this holds everywhere. Formal lifting here is an algebraic definition. Lesson **Infinitesimal lifting and the invariance of étale morphisms under thickenings** will establish the corresponding global scheme statements.

The algebraic prerequisites say that formal étaleness is formal smoothness together with vanishing differentials. They also say that a smooth algebra is locally standard smooth. Consequently an étale algebra is locally of the form

$$
D=\left(A[X_1,\ldots,X_n]/(F_1,\ldots,F_n)\right)_{h\Delta},
\qquad
\Delta=\det\left(\frac{\partial F_i}{\partial X_j}\right).
\tag{1.1}
$$

Indeed, the standard smooth presentation has differentials free of rank equal to the number of variables minus the number of equations; their vanishing makes these numbers equal. Conversely (1.1) is smooth and has zero differentials, hence is étale. Localization can also be incorporated into a square presentation: adjoining $Z$ and the equation $h\Delta Z-1$ adds a Jacobian row and column with invertible new diagonal entry.

**Lemma 1.1.** An étale morphism is flat, locally of finite presentation and unramified.

**Proof.** An étale algebra over an arbitrary commutative ring is flat, unramified and finitely presented by Smooth algebras over a field and the Jacobian criterion, Corollary 6.2, whose flatness assertion uses its Theorem 6.1. Apply this exact algebraic result to the étale affine charts defining the morphism. Flatness and local finite presentation are local on source and target, and the differential criterion of **Unramified morphisms** passes algebraic unramifiedness to these scheme charts. ∎

Here is a useful converse proof which does not assume that the base is Noetherian.

**Lemma 1.2.** Let $B$ be a finite type $A$-algebra and $\mathfrak q\in\operatorname{Spec}B$. If $\Omega_{B/A,\mathfrak q}=0$, then a neighbourhood of $\mathfrak q$ is a quotient of an étale $A$-algebra of the square form (1.1). If $B$ is finitely presented and $B_{\mathfrak q}$ is flat over $A_{\mathfrak p}$, where $\mathfrak p=\mathfrak q\cap A$, then $A\to B$ is étale at $\mathfrak q$.

**Proof.** Choose a presentation $B=A[X_1,\ldots,X_n]/I$. The conormal sequence gives

$$
I/I^2\longrightarrow B^n\longrightarrow\Omega_{B/A}\longrightarrow0.
$$

After tensoring with $\kappa(\mathfrak q)$, the first map is surjective. Choose $n$ relations $F_i\in I$ whose Jacobian determinant $\Delta$ is nonzero at $\mathfrak q$. Then

$$
D=\left(A[X_1,\ldots,X_n]/(F_1,\ldots,F_n)\right)_\Delta
\twoheadrightarrow B_\Delta
\tag{1.2}
$$

has étale source. This proves the first assertion without finite presentation of $B$.

For the second, the kernel of (1.2) is finitely generated because $I$ is finitely generated. Localize at the inverse image $\mathfrak r$ of $\mathfrak q$, obtaining

$$
0\longrightarrow K\longrightarrow D_{\mathfrak r}
\longrightarrow B_{\mathfrak q}\longrightarrow0.
$$

Both fibre local rings over $\kappa(\mathfrak p)$ are fields: this follows for $D$ from Lemma 1.1 and the unramified fibre classification, and for $B$ from that same classification at the point. Their quotient map is therefore an isomorphism. Flatness of $B_{\mathfrak q}$ makes reduction of the displayed sequence modulo $\mathfrak p A_{\mathfrak p}$ injective on $K/\mathfrak pK$. Thus $K/\mathfrak pK=0$. Nakayama applies to the finite $D_{\mathfrak r}$-module $K$, since $\mathfrak pD_{\mathfrak r}$ is contained in its maximal ideal, and gives $K=0$.

The finitely many generators of the kernel of (1.2) consequently vanish after one further principal localization avoiding $\mathfrak r$. There (1.2) is an isomorphism, so $B$ is étale near $\mathfrak q$. ∎

**Theorem 1.3 (equivalent descriptions).** For a morphism $f:X\to S$, the following are equivalent:

1. $f$ is étale.
2. $f$ is flat and G-unramified, meaning locally of finite presentation with $\Omega_{X/S}=0$.
3. $f$ is smooth and unramified.
4. $f$ is flat and locally of finite presentation, and every fibre is a disjoint union of spectra of finite separable extensions of the base residue field.
5. $f$ is flat and locally of finite presentation, and every geometric fibre is a disjoint union of reduced points.

**Proof.** Lemmas 1.1–1.2 give (1)$\Leftrightarrow$(2). For (3), smoothness gives a local standard smooth presentation; unramifiedness makes its free differential module zero, so the presentation is square and étale. The reverse implication follows directly from the algebraic definition. Differential base change and the unramified field classification in the preceding lesson give (2)$\Leftrightarrow$(4). That classification is unchanged by extension to an algebraic closure: finite separable fields split into products of the algebraic closure, whereas a nonseparable extension produces nonreduced geometric fibres. Equivalently, vanishing of the finite differential module can be tested after a faithfully flat field extension. This gives (4)$\Leftrightarrow$(5). ∎

**Pointwise form.** Suppose $f$ is locally of finite presentation, $s=f(x)$, $A=\mathcal O_{S,s}$ and $B=\mathcal O_{X,x}$. Then each of the following tests is equivalent to étaleness at $x$:

- $B$ is flat over $A$ and the fibre is étale at $x$;
- $B$ is flat over $A$ and the fibre is unramified at $x$;
- $B$ is flat over $A$ and $\Omega_{X/S,x}=0$;
- $B$ is flat over $A$ and $\Omega_{X/S,x}\otimes_B\kappa(x)=0$;
- $B$ is flat over $A$, $\mathfrak m_A B=\mathfrak m_B$, and $\kappa(x)/\kappa(s)$ is finite separable;
- there is a square Jacobian chart as in (1.1) around $x$.

The differential module is finite, so Nakayama equates its vanishing with vanishing after tensoring with $\kappa(x)$. The six unramified pointwise tests proved in the preceding lesson identify the fibre and residue-field conditions. Lemma 1.2 then supplies the étale neighbourhood. We will add the one-variable standard form in Section 3. These are the tests of [Stacks, Tags [02GK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-smooth-unramified), [02GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-flat-etale-fibres), [02GU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-at-point), [02GV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-flat-unramified-etale)].

## 2. Permanence and standard étale algebras

Étaleness is local on source and target and is preserved by composition and arbitrary base change. One can check composition by flatness and the differential exact sequence

$$
f^*\Omega_{Y/S}\longrightarrow\Omega_{X/S}\longrightarrow\Omega_{X/Y}\longrightarrow0;
$$

local finite presentation is preserved by composition. Base change follows from flat base change, differential base change and finite presentation. Open immersions are étale because their local maps are localizations. In particular products of étale morphisms are étale [Stacks, Tags [02GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-etale), [02GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-etale)].

**Proposition 2.1 (cancellation).** If $X$ and $Y$ are étale over $S$, every $S$-morphism $a:X\to Y$ is étale.

**Proof.** Factor it as

$$
X\xrightarrow{\Gamma_a}X\times_S Y\xrightarrow{\operatorname{pr}_Y}Y.
$$

The graph is a section of the unramified projection $X\times_S Y\to X$, hence is an open immersion by the section theorem of **Unramified morphisms**. The other projection is a base change of the étale map $X\to S$. Composition proves the assertion. No separatedness hypothesis is needed. ∎

A **standard étale algebra** means

$$
E=(A[T]/(f))_g,\qquad f\in A[T]\text{ monic},\qquad f'\in E^\times.
\tag{2.1}
$$

It is étale: the single equation has invertible derivative, so it is a standard smooth presentation of relative dimension zero. Equivalently, a lifted approximate root across a square-zero ideal is corrected uniquely by subtracting its error divided by $f'$. Monicity implies that $A[T]/(f)$ is free over $A$, with basis $1,T,\ldots,T^{d-1}$ when $d=\deg f$. The localization in (2.1) need not be finite over $A$.

Base changes and principal localizations of a standard étale algebra remain standard étale; in a localization, multiply $g$ by a polynomial representing the element to be inverted. We do not require a composition to have a single global presentation (2.1). The local structure theorem is what supplies such a presentation near each point [Stacks, Tags [00UB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-standard-etale), [00UC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-standard-etale)].

## 3. Why one monic polynomial is enough

**Theorem 3.1 (local standard form).** If $A\to B$ is étale at $\mathfrak q$, some $B_b$, with $b\notin\mathfrak q$, is standard étale over $A$ [Stacks, Tag [00UE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-etale-locally-standard)].

**Proof.** We give the reduction and the monic-polynomial construction explicitly.

First replace $B$ by an étale square Jacobian neighbourhood of $\mathfrak q$. Its finitely many coefficients descend to a finitely generated $\mathbf Z$-subalgebra $A_0\subset A$, giving an étale algebra $B_0$ and $B=A\otimes_{A_0}B_0$. The contraction of $\mathfrak q$ is a point of $B_0$. A standard presentation around that point base changes to the desired presentation. Thus it suffices to treat Noetherian $A$.

Now $B$ is quasi-finite near $\mathfrak q$, by the unramified fibre classification. Algebraic Zariski's Main Theorem gives an integral subalgebra whose localization agrees with $B$ near $\mathfrak q$. It can be replaced by a finite $A$-subalgebra $C$: include the integral localization element and finitely many integral numerators for algebra generators of the common localization. Then $C_c\simeq B_c$ for some $c$ avoiding $\mathfrak q$. It is enough to construct the standard neighbourhood for $C$ and further invert $c$. We may therefore suppose $B$ is finite over $A$, retaining étaleness at the selected point only.

Put $\mathfrak p=\mathfrak q\cap A$ and $k=\kappa(\mathfrak p)$. The finite fibre algebra decomposes into Artinian local factors

$$
B\otimes_A k=L\times R_2\times\cdots\times R_r,
\qquad L=\kappa(\mathfrak q).
\tag{3.1}
$$

The first factor is a finite separable field because the map is unramified at $\mathfrak q$. Choose a nonzero primitive element $\alpha$ of $L/k$. The element $(\alpha,0,\ldots,0)$ of (3.1), after multiplication by a nonzero scalar in $k$ to clear a denominator from $A\setminus\mathfrak p$, lifts to $t\in B$. The scaled element still generates $L$.

Let $C=A[t]\subset B$ and $\mathfrak r=C\cap\mathfrak q$. Both $C$ and $B$ are finite over $A$. The only prime of $B$ over $\mathfrak r$ is $\mathfrak q$: the other factors in (3.1) send $t$ to zero, while its image at $\mathfrak q$ is nonzero. Localizing the finite extension at $\mathfrak r$ therefore gives the local finite algebra $B_{\mathfrak q}$. The map

$$
C_{\mathfrak r}\longrightarrow B_{\mathfrak q}
$$

is injective. Moreover $\mathfrak pB_{\mathfrak q}=\mathfrak qB_{\mathfrak q}$ and $\kappa(\mathfrak r)=L$, since the image of $t$ is primitive. Its cokernel is finite over $C_{\mathfrak r}$ and has zero reduction modulo the maximal ideal; Nakayama makes the map surjective. Hence it is an isomorphism. The finite $C$-module $B/C$ vanishes at $\mathfrak r$, so one $h\in C\setminus\mathfrak r$ kills it after localization, giving $C_h=B_h$.

We may now work with the finite monogenic algebra $C=A[T]/I$, étale at $\mathfrak r$. The ideal $\overline I\subset k[T]$ is principal. Choose $u\in I$ whose reduction is a nonzero scalar times its generator, clearing denominators if necessary. At the root $\alpha$, that generator has a simple separable factor: the corresponding local fibre is the field $L$. Thus $\overline u'(\alpha)\ne0$.

Integrality of $t$ supplies a monic $m\in I$. Choose an integer $e\ge2$ with $e\deg m>\deg u$, and set

$$
f=m^e+u.
\tag{3.2}
$$

This polynomial is monic and belongs to $I$. At $\alpha$, $\overline m(\alpha)=0$, so $\overline f'(\alpha)=\overline u'(\alpha)\ne0$. Consequently

$$
D=(A[T]/(f))_{f'}\twoheadrightarrow C_{f'}
$$

is a surjection from a standard étale algebra, and the selected point survives. Further localize both sides by a lifted element so that the target is étale, using the pointwise criterion of Section 1. The source remains standard étale. By Proposition 2.1 the resulting quotient map is étale, in particular flat and finitely presented.

The flat closed-subscheme theorem of **Flat morphisms** says that a finitely presented flat quotient is cut out by a finitely generated pure ideal, hence by an idempotent. Such a quotient is a principal localization: $D/(e_0)=D_{1-e_0}$ for an idempotent $e_0$. A principal localization of a standard étale algebra is standard étale. Restoring the localizations made earlier, and then base changing from $A_0$, proves the theorem. ∎

**Corollary 3.2 (geometric form).** Let $f:X\to Y$ be étale at $x$ and let $V=\operatorname{Spec}A$ be any affine neighbourhood of $f(x)$. There is an affine neighbourhood $U$ of $x$ mapping into $V$, a monic $f_0\in A[T]$, and an open immersion over $V$

$$
U\hookrightarrow\operatorname{Spec}(A[T]/(f_0))_{f_0'}.
\tag{3.3}
$$

**Proof.** Take an étale affine neighbourhood inside the inverse image of $V$ and apply Theorem 3.1. In its standard presentation the derivative is invertible, so the presentation is a further principal localization of the algebra on the right of (3.3). ∎

This also completes the pointwise tests: a one-variable chart $(A[T]/(f_0))_g$ with $f_0$ monic and $f_0'(x)\ne0$ is equivalent to étaleness at $x$, after shrinking by the derivative [Stacks, Tags [025B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-structure-etale), [025C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-geometric-structure)].

**Corollary 3.3 (unramified form).** An unramified morphism is locally a closed subscheme of a standard étale scheme. In local-ring language, an essentially finite type local map $A\to B$ with $\Omega_{B/A}=0$ presents $B$ as a quotient of a standard étale $A$-algebra localized at a prime [Stacks, Tag [039O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-structure-unramified)].

**Proof.** Lemma 1.2 constructs a surjection from a square Jacobian étale algebra to a neighbourhood of the point. Apply Theorem 3.1 to that algebra at the inverse image of the point and localize the quotient correspondingly. Localization at the point gives the local-ring statement. The quotient ideal need not be finitely generated; unramifiedness only imposes local finite type. ∎

For precision, an **essentially étale local map** means a localization at a prime of an étale algebra over the base local ring. For Noetherian local rings $A,B$, an essentially finite type local map is essentially étale if and only if it is flat, $\mathfrak m_AB=\mathfrak m_B$, and the residue extension is finite separable. To see the converse, write $B=C_{\mathfrak q}$ for a finite type $A$-algebra. Noetherianity makes $C$ finitely presented, and the pointwise criterion applies. Theorem 3.1 then gives the local form (2.1). This distinguishes a local map obtained by localization from an algebra required itself to be finitely presented.

## 4. The topology and the open-immersion criterion

An étale map is open because it is flat and locally of finite presentation, by the openness theorem of **Flat morphisms**. It is locally quasi-finite because it is unramified. Neither conclusion requires quasi-compactness or separatedness [Stacks, Tags [03WS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-locally-quasi-finite), [03WT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-open)].

**Theorem 4.1.** For $f:X\to Y$, the following are equivalent:

1. $f$ is an open immersion.
2. $f$ is étale and universally injective.
3. $f$ is a flat monomorphism locally of finite presentation.

**Proof.** An open immersion is étale, and every base change is an open immersion, giving (1)$\Rightarrow$(2). By **Unramified morphisms**, an unramified universally injective map is a monomorphism; Lemma 1.1 gives (2)$\Rightarrow$(3).

Assume (3). Openness and injectivity make $X\to V=f(X)$ a homeomorphism, where $V$ is open in $Y$. We show that its local rings agree. Choose affine charts $\operatorname{Spec}B\subset X$ and $\operatorname{Spec}A\subset V$. Their map is a monomorphism, so $B\otimes_A B\to B$ is an isomorphism. At corresponding primes $\mathfrak q,\mathfrak p$, the map $A_{\mathfrak p}\to B_{\mathfrak q}$ is therefore a ring epimorphism; it is also faithfully flat, being flat and local.

For any faithfully flat ring map $R\to T$, the equalizer sequence

$$
0\longrightarrow R\longrightarrow T
\xrightarrow{\,t\mapsto t\otimes1-1\otimes t\,}T\otimes_R T
\tag{4.1}
$$

is exact. Here is the needed elementary verification: tensor with $T$. If $z\in T\otimes_R T$ satisfies $z\otimes1$ equal to the element obtained by inserting $1$ in the middle, multiplication of the first two factors shows $z=\mu(z)\otimes1$. Thus the tensored sequence is exact; faithful flatness reflects exactness. For a ring epimorphism the last arrow in (4.1) is zero, so $R\to T$ is an isomorphism. Apply this to the local rings above. A homeomorphism inducing isomorphisms of all stalks is an isomorphism of schemes. Hence $X\simeq V$, proving (1). ∎

This proves [Stacks, Tag [025G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-theorem-etale-radicial-open)] directly, including its arbitrary-base scope.

**Proposition 4.2 (one-point finite fibre).** Suppose $f:X\to S$ is finite étale, $X_s$ has exactly one point $x$, and $\kappa(x)/\kappa(s)$ is purely inseparable. Then $f^{-1}(U)\to U$ is an isomorphism for some open neighbourhood $U$ of $s$ [Stacks, Tag [04DH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-etale-one-point)].

**Proof.** The residue extension is also finite separable, so it is trivial; the entire fibre algebra is $\kappa(s)$. On an affine neighbourhood write $X=\operatorname{Spec}B$ over $\operatorname{Spec}A$. A finite étale algebra is a finite locally free $A$-module: a finite finitely presented algebra is finitely presented as a module, and finite presented flat modules are locally free. Near $s$ its rank is the fibre dimension, namely one. The element $1\in B$ is a basis at $s$, so it is a basis after shrinking. Then $A\to B$ is an isomorphism of modules and hence of algebras on that neighbourhood. ∎

## 5. What happens to Noetherian local rings

Throughout this section $A\to B$ is an essentially étale local map of Noetherian local rings. Put $\mathfrak m=\mathfrak m_A$, $\mathfrak n=\mathfrak m_B$, $k=A/\mathfrak m$, and $l=B/\mathfrak n$. We have a faithfully flat map, $\mathfrak mB=\mathfrak n$, and a finite separable extension $l/k$.

**Theorem 5.1.** The following equalities and equivalences hold:

$$
\dim A=\dim B,\qquad \operatorname{depth}A=\operatorname{depth}B;
$$

$$
\begin{aligned}
A\text{ Cohen–Macaulay}&\Longleftrightarrow B\text{ Cohen–Macaulay},\\
A\text{ regular}&\Longleftrightarrow B\text{ regular},\\
A\text{ reduced}&\Longleftrightarrow B\text{ reduced},\\
A\text{ a normal domain}&\Longleftrightarrow B\text{ a normal domain}.
\end{aligned}
\tag{5.1}
$$

**Proof of dimension and depth.** The flat local dimension formula of **Flatness criteria, dimension and the flat locus** gives

$$
\dim B=\dim A+\dim(B/\mathfrak mB)=\dim A.
$$

For depth, take a free resolution $F_\bullet\to k$ over $A$ with each term of finite rank; such a resolution exists because $A$ is Noetherian. Flatness makes $F_\bullet\otimes_A B$ a free resolution of $l=B/\mathfrak mB$. Termwise finite freeness identifies the cochain complexes

$$
\operatorname{Hom}_B(F_\bullet\otimes_A B,B)
=\operatorname{Hom}_A(F_\bullet,A)\otimes_A B.
$$

Flat tensor product commutes with their cohomology. Hence

$$
\operatorname{Ext}_B^i(l,B)
\simeq\operatorname{Ext}_A^i(k,A)\otimes_A B.
$$

Faithful flatness preserves whether these modules vanish. The Ext characterization of depth therefore gives equality of depths. Equality of dimension and depth immediately gives the Cohen–Macaulay equivalence [Stacks, Tags [039S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-etale-dimension), [039T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-proposition-etale-depth), [025Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-proposition-etale-CM)].

**Proof of regularity.** Flatness identifies $\mathfrak m\otimes_A B$ with $\mathfrak mB=\mathfrak n$ and identifies the corresponding quotient by $\mathfrak m^2$. Consequently

$$
\mathfrak n/\mathfrak n^2
\simeq (\mathfrak m/\mathfrak m^2)\otimes_k l.
\tag{5.2}
$$

Thus the two local rings have the same embedding dimension. Their Krull dimensions are equal, so the criterion “embedding dimension equals dimension” gives regularity in both directions [Stacks, Tag [025N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-proposition-etale-regular)].

**Proof of reducedness.** Faithful flatness embeds $A$ into $B$, so reducedness descends. If $A$ is reduced, let $\mathfrak p_1,\ldots,\mathfrak p_r$ be its minimal primes and $K_i=\operatorname{Frac}(A/\mathfrak p_i)$. There is an injection $A\hookrightarrow\prod_i K_i$, since the intersection of the minimal primes is zero. Flatness gives

$$
B\hookrightarrow\prod_i(B\otimes_A K_i).
$$

Each algebra on the right is a localization of an étale finite type $K_i$-algebra, hence a localization of a finite product of finite separable fields. It is reduced. A subring of a reduced ring is reduced, proving ascent [Stacks, Tag [025O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-proposition-etale-reduced)].

**Proof of normality.** Use Serre's criterion for Noetherian rings: normality is equivalent to $(R_1)$ and $(S_2)$. At every prime $\mathfrak q\subset B$, with contraction $\mathfrak p\subset A$, the map $A_{\mathfrak p}\to B_{\mathfrak q}$ is again essentially étale and local. The dimension, depth and regularity arguments just proved apply there. They transfer the requirements

$$
\dim A_{\mathfrak p}\le1\ \Rightarrow\ A_{\mathfrak p}\text{ regular},
\qquad
\operatorname{depth}A_{\mathfrak p}\ge\min(2,\dim A_{\mathfrak p})
$$

to the corresponding requirements for $B_{\mathfrak q}$. Thus normality ascends. Conversely faithful flatness makes $\operatorname{Spec}B\to\operatorname{Spec}A$ surjective. For each $\mathfrak p$ choose a prime above it and use the same equalities and equivalence to descend $(R_1)$ and $(S_2)$. Finally a normal Noetherian local ring is a domain, so this proves precisely the last line of (5.1) [Stacks, Tag [025P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-proposition-etale-normal)]. ∎

## 6. Examples that distinguish the hypotheses

**Roots of unity.** For a positive integer $n$ and $A=\mathbf Z[1/n]$, the algebra

$$
A[T]/(T^n-1)
$$

is finite free of rank $n$. The element $T$ is invertible and the derivative $nT^{n-1}$ is a unit, so the algebra is finite étale. Over a residue field $k$ of $A$, $T^n-1$ factors into distinct irreducible separable polynomials. The fibre is the product of the corresponding finite separable fields. Over an algebraic closure it consists of $n$ distinct roots of unity.

**The power map on the torus.** Over a field $k$, the map $\mathbf G_m\to\mathbf G_m$ taking $z$ to $z^n$ has coordinate algebra

$$
k[t,t^{-1}]\longrightarrow k[z,z^{-1}],\qquad t\longmapsto z^n.
$$

The target is free with basis $1,z,\ldots,z^{n-1}$. Its presentation by $Z^n-t$ has derivative $nZ^{n-1}$, so the map is finite étale exactly when $n\ne0$ in $k$. If $n=0$ in $k$, its differential module is the nonzero free module $k[z,z^{-1}]\,dz$. More generally over a nonempty base it is étale exactly when $n$ is invertible in the base ring, as the same differential computation shows. For $n>1$ over a field, no nonempty source open maps isomorphically to a target open: such an isomorphism would identify the function fields, but $[k(z):k(z^n)]=n$. One verifies this degree by the linear independence of $1,z,\ldots,z^{n-1}$ over $k(z^n)$, grouping polynomial exponents modulo $n$.

**Artin–Schreier.** In characteristic $p$,

$$
\mathbf F_p[x]\longrightarrow
\mathbf F_p[x,y]/(y^p-y-x)\simeq\mathbf F_p[y]
$$

is monic of degree $p$ in $y$ and has derivative $-1$. It is a connected finite étale cover of degree $p$. Over an algebraic closure, each fibre has the $p$ distinct roots $a+c$, $c\in\mathbf F_p$, for any one root $a$.

**A bijective étale map.** The map $\operatorname{Spec}\mathbf C\to\operatorname{Spec}\mathbf R$ is finite étale and bijective on points. After base change to $\mathbf C$, however,

$$
\mathbf C\otimes_{\mathbf R}\mathbf C\simeq\mathbf C\times\mathbf C.
$$

Its fibre has two points. It is not universally injective and therefore is not an open immersion.

**A bijective unramified map.** Let $k$ have characteristic different from $2$ and let

$$
C=\operatorname{Spec} k[x,y]/(y^2-x^2(x+1)).
$$

Its normalization is parametrized by $x=u^2-1$, $y=u(u^2-1)$. Restrict the normalization to $N=\mathbf A^1_k\setminus\{-1\}$. Away from the node $(0,0)$ the inverse is $u=y/x$; over the node only $u=1$ remains. Thus $N\to C$ is bijective on points, including points with nontrivial residue fields. Its relative differentials are generated by $du$ with relations

$$
2u\,du=0,\qquad(3u^2-1)\,du=0.
$$

These coefficients generate the unit ideal, since $2$ is invertible and $3u^2-1$ is $-1$ modulo $(u)$. The map is unramified. At the node, the local ring of $C$ has embedding dimension $2$, while the local ring at $u=1$ has embedding dimension $1$. Moreover its maximal ideal is generated by the images of $x,y$, since $u+1$ is a unit there and $x=(u-1)(u+1)$. If the map were flat at this point, the flat-ideal argument in (5.2), with identical residue fields, would make those embedding dimensions equal. It is therefore not flat, not étale, and not an open immersion.

**Why finite presentation matters.** Let $A=\prod_{j\ge1}k$ and let $I\subset A$ be the ideal of sequences of finite support. Every $a\in I$ satisfies $a=ae$ for a finite-support idempotent $e\in I$. The pure-ideal criterion of **Flat morphisms** makes $A/I$ flat over $A$. It is a quotient algebra, so it is of finite type and has zero relative differentials; the map is unramified. But $I$ is not finitely generated: finitely many generators have support in one finite set and cannot generate an idempotent supported outside it. Hence $A\to A/I$ is not finitely presented and is not étale. This gives flat plus unramified without G-unramified over a non-Noetherian base.

## 7. Exercises

**Exercise 1 (easy).** Classify schemes étale over a separably closed field. Must such a scheme be finite?

**Exercise 2 (medium).** Prove that $y^p-y=x$ defines a connected finite étale cover of $\mathbf A^1_{\mathbf F_p}$ of degree $p$. Describe its geometric fibres and its translations over the base.

**Exercise 3 (medium).** Prove the cancellation law using the graph of an $S$-morphism $X\to Y$, and specify which projection makes the graph a section.

**Exercise 4 (medium).** For the nodal cubic of Section 6, prove that removing one preimage of the node gives a bijective unramified map. Identify the failed hypothesis of Theorem 4.1 by a local calculation.

**Exercise 5 (hard).** Let $A\to B$ be an essentially étale local map of Noetherian local rings. Prove regularity in both directions by comparing dimension and cotangent spaces.

## 8. Solutions

**Solution 1.** The unramified fibre classification makes the scheme a disjoint union of spectra of finite separable extensions of the base field. A separably closed field has no nontrivial such extension, so the scheme is a disjoint union of copies of its spectrum. Conversely any such disjoint union is étale, as each component is an open chart with identity structure map. The indexing set may be infinite. It is finite exactly when the scheme is quasi-compact: its components form an open cover, and a finite subcover exists precisely for finitely many components.

**Solution 2.** As a polynomial in $y$, $y^p-y-x$ is monic of degree $p$. Polynomial division gives a free basis $1,y,\ldots,y^{p-1}$ over $\mathbf F_p[x]$, so the morphism is finite of degree $p$. Its derivative is $-1$, giving a standard étale algebra. Eliminating $x$ gives the integral domain $\mathbf F_p[y]$, hence a connected source. At a geometric point $x=b$, choose a root $a$ of $Y^p-Y-b$. Every $a+c$ with $c\in\mathbf F_p$ is a root; these $p$ distinct roots exhaust a polynomial of degree $p$. The transformations $y\mapsto y+c$ fix $x=y^p-y$, act transitively and freely on each geometric fibre, and compose by addition in $\mathbf F_p$.

**Solution 3.** The graph $\Gamma_a:X\to X\times_S Y$ is a section of $\operatorname{pr}_X$, which is the base change of the unramified map $Y\to S$. Pulling back its open diagonal shows that the section is an open immersion. The projection $\operatorname{pr}_Y$ is the base change of the étale map $X\to S$, and is étale. Thus $a=\operatorname{pr}_Y\circ\Gamma_a$ is étale. The two projections have different roles; no closed-diagonal or separatedness argument is needed.

**Solution 4.** The parametrization satisfies the equation because $y^2=u^2(u^2-1)^2=x^2(x+1)$. On $D(x)$ its inverse is $u=y/x$. The complement of $D(x)$ on the underlying curve is just the node, whose normalization preimages are $u=\pm1$. Deleting $-1$ leaves exactly one rational preimage, proving bijectivity. The differential quotient is $k[u]du/(2u,3u^2-1)du=0$; localizing at $u+1$ retains this equality. The map is locally of finite type and unramified. At the node the equation has no linear term, so the classes of $x,y$ form a two-dimensional cotangent space. At the remaining preimage the cotangent space is generated by $u-1$. The images of $x,y$ generate that maximal ideal and the residue fields are both $k$. Flatness would identify the two cotangent spaces by flat tensor product, a contradiction. Thus the missing condition is étaleness, specifically flatness. Bijectivity and unramifiedness alone do not give the second condition of Theorem 4.1.

**Solution 5.** Write $\mathfrak n=\mathfrak mB$ and $l/k$ for the finite separable residue extension. The flat local dimension formula gives $\dim B=\dim A$, since the local fibre is the field $l$. Flatness of $B$ over $A$ gives $\mathfrak m\otimes_A B\simeq\mathfrak n$ and, after taking the quotient by $\mathfrak m^2$, gives

$$
\mathfrak n/\mathfrak n^2\simeq(\mathfrak m/\mathfrak m^2)\otimes_k l.
$$

The vector-space dimensions over $l$ and $k$ are equal. A Noetherian local ring is regular exactly when the dimension of this cotangent space is its Krull dimension. The two quantities agree on one side exactly when they agree on the other, proving both ascent and descent.

## What this lesson does not prove

The following exact algebraic prerequisites are imported, rather than replacing any of the local structure or geometric equivalence proofs above.

- Formal smoothness plus $\Omega=0$ is formal étaleness; smooth finitely presented algebras are locally standard smooth; a standard smooth presentation has differentials locally free of rank “variables minus equations.” These are results of **Formally smooth, unramified and étale ring maps** [Stacks, Tags [00UR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-formally-etale-etale), [00TA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-smooth-syntomic), [00T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-standard-smooth), [00UB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-standard-etale)].
- Over an arbitrary commutative base, every smooth algebra is flat and every étale algebra is flat, unramified and finitely presented: Smooth algebras over a field and the Jacobian criterion, Theorem 6.1 and Corollary 6.2. Lemma 1.1 applies these algebraic statements to scheme charts. Standard étale algebras are étale by Formally smooth, unramified and étale ring maps, Proposition 6.1; its proof supplies the unique square-zero root lift used by the standard presentations here.
- Algebraic Zariski's Main Theorem: if $A\to B$ is finite type and quasi-finite at $\mathfrak q$, its integral closure $C$ of $A$ in $B$ contains $c\notin\mathfrak q$ with $C_c=B_c$ [Stacks, Tag [00Q9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-main-theorem)], from **Zariski's Main Theorem**. Section 3 explains why a finite subalgebra suffices.
- For a Noetherian local ring $(R,\mathfrak m,k)$, $\operatorname{depth}R=\inf\{i:\operatorname{Ext}_R^i(k,R)\ne0\}$, from **Regular sequences, depth and Cohen–Macaulay modules** [Stacks, Tag [00LW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-depth-ext)]. Serre's normality criterion is $(R_1)+(S_2)$, from **Discrete valuation rings, normal rings and Serre's criterion** [Stacks, Tag [031S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-criterion-normal)].
- A finite finitely presented algebra is finitely presented as a module, and a finitely presented flat module is finite locally free Stacks, Tags [0564, [00NX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-projective)]. These are elementary finite-module criteria used in Proposition 4.2.

Our principal references are the Stacks Project, the cited tags, and Vakil's *The Rising Sea*, §§13.6 and 24.8. The next lesson develops smooth morphisms in positive relative dimension, including the étale factorization through affine space. Étale-local splitting over henselian rings belongs to **Étale neighbourhoods, henselization and quasi-finite morphisms**.
The arbitrary-base algebraic Zariski Main provider is Zariski’s Main Theorem, Theorem 1.1. Its main induction is written in Sections 1–2. The complete supporting proofs are also available in the programme’s AI Integrated Stacks Project algebra chapter: Coefficients in the radical of a conductor (Tag 00PY, with its conductor setup and leading-coefficient lemma) and Strong transcendence excludes quasi-finite points (Tag 00Q2, for reduced rings finite over the algebra generated by the strongly transcendental element). The same proofs are included in the portable programme reader. They are prerequisites of the algebraic theorem and are not consequences of the étale local structure proved here. The Stacks Project supplies these proofs, retained under GNU FDL 1.2 in the [pinned AI Integrated Stacks edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex); that source credit and licence remain in force. Availability and the checked correspondence of these named proofs do not assert that all their recursive prerequisites have been checked.
