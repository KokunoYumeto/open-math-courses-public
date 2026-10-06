# The structure of the Picard scheme

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Picard scheme records two kinds of information. Its tangent space measures how a line bundle changes over a first-order thickening. Its components record discrete classes of line bundles. These interact: in positive characteristic a component can have more tangent directions than its dimension, and torsion classes can occur in components other than the identity component.

We will compute the tangent space and the obstruction to lifting a line bundle, prove two smoothness criteria, and distinguish the identity component, torsion components, and numerical equivalence. The finiteness theorem for the Néron–Severi group is a precisely stated input. The tangent and obstruction calculations are proved here.

## 1. Setting and the distinction between bundles and classes

Let $X$ be a proper scheme over a field $k$, with

$$
H^0(X,\mathcal O_X)=k. \tag{1.1}
$$

Write $P=\operatorname{Pic}_{X/k}$ for the scheme representing the fppf Picard sheaf. For projective geometrically integral $X$, its construction was proved in Relative divisors and the existence of the Picard scheme. For arbitrary proper $X/k$, we use Murre's representability theorem: the fppf Picard sheaf is represented by a group scheme locally of finite type over $k$, and its formation commutes with field extension. The precise source is Murre, [*On contravariant functors from the category of preschemes over a field into the category of abelian groups*](https://www.numdam.org/item/PMIHES_1964__23__5_0/), Publications Mathématiques de l'IHÉS 23 (1964), result (II.15); see also Kleiman, *The Picard scheme*, Corollary 4.18.3 and the discussion immediately following it. This existence input does not require $X$ to be smooth, reduced, or projective.

Condition (1.1) holds universally. Indeed, choose a finite affine covering of $X$. Since $X$ is separated, its finite intersections are affine, and the Čech complex computes coherent cohomology. For any $k$-algebra $A$, tensoring that complex with $A$ is exact on cohomology because $A$ is flat over $k$. Thus

$$
H^i(X_A,\mathcal O_{X_A})=H^i(X,\mathcal O_X)\otimes_k A,
\qquad H^0(X_A,\mathcal O_{X_A})=A. \tag{1.2}
$$

The same argument works with coefficients in any $k$-vector space. Consequently the presheaf

$$
T\longmapsto \operatorname{Pic}(X_T)/p_T^*\operatorname{Pic}(T)
\tag{1.3}
$$

injects into its étale and fppf sheafifications, by the descent argument in The Picard functor and the Picard scheme of a curve, Section 1. A sheaf class need not have a global bundle representative: the real conic in that lesson already illustrates the obstruction.

There is a useful place where representatives do exist. Suppose $k$ is algebraically closed and $A$ is a local Artin $k$-algebra with residue field $k$. The ring $A$ is strictly henselian. Any étale covering of $\operatorname{Spec}A$ has a section after selecting a member above its closed point. The equality of the étale and fppf Picard sheaves from the preceding lesson therefore implies that every element of $P(A)$ is represented by a line bundle on $X_A$. Moreover $\operatorname{Pic}(A)=0$. Thus

$$
P(A)=\operatorname{Pic}(X_A). \tag{1.4}
$$

We will use (1.4) for the infinitesimal smoothness argument, after extending the field to an algebraic closure. We will not assume it for all parameter schemes.

## 2. The square-zero sequence and the tangent space

Put $D=k[\epsilon]/(\epsilon^2)$. The tangent space at the identity is the kernel

$$
T_0P=\ker\bigl(P(D)\longrightarrow P(k)\bigr). \tag{2.1}
$$

The underlying topological spaces of $X_D$ and $X$ are identical. Their sheaves of units fit into a split exact sequence of abelian sheaves on the Zariski site of $X$:

$$
0\longrightarrow \mathcal O_X
\xrightarrow{a\mapsto 1+\epsilon a}
\mathcal O_{X_D}^{\times}
\longrightarrow \mathcal O_X^{\times}
\longrightarrow 1. \tag{2.2}
$$

The multiplication rule $(1+\epsilon a)(1+\epsilon b)=1+\epsilon(a+b)$ identifies the kernel with the additive sheaf $\mathcal O_X$. Constants provide the splitting. Since first cohomology of units classifies line bundles, taking cohomology gives

$$
\ker\bigl(\operatorname{Pic}(X_D)\to\operatorname{Pic}(X)\bigr)
\simeq H^1(X,\mathcal O_X). \tag{2.3}
$$

The resulting map to (2.1) is injective by (1.3), since $\operatorname{Pic}(D)=0$. It is surjective if $k$ is algebraically closed, by (1.4).

To remove that restriction, extend to an algebraic closure $\bar k$. The tangent space of a scheme at a rational point commutes with field extension: it is the dual of the cotangent space, or equivalently the kernel on dual-number points after tensoring. Equation (1.2) shows that coherent cohomology does too. The map (2.3) is natural under field extension. After tensoring with $\bar k$ it is an isomorphism, and faithful flatness of $\bar k/k$ makes it an isomorphism before tensoring.

**Proposition 2.1.** For $X$ satisfying (1.1), there is a canonical $k$-linear isomorphism

$$
T_0\operatorname{Pic}_{X/k}\simeq H^1(X,\mathcal O_X). \tag{2.4}
$$

The preceding argument proves bijectivity. We check the linear structure explicitly. If $a_{ij}$ is a Čech cocycle on an affine cover, glue trivial bundles using transition functions $1+\epsilon a_{ij}$. Tensoring two such bundles adds their cocycles. Substitution $\epsilon\mapsto c\epsilon$ multiplies the cocycle by $c\in k$. These are exactly addition and scalar multiplication in the tangent space. A change of local frames by $1+\epsilon b_i$ changes $a_{ij}$ by a coboundary. Hence (2.4) is a canonical linear isomorphism. ∎

At any rational point $[L]\in P(k)$, translation by that point identifies $T_{[L]}P$ with $T_0P$. Over a field extension $K/k$, the corresponding statement is

$$
T_{[L]}P_K\simeq H^1(X_K,\mathcal O_{X_K}). \tag{2.5}
$$

The tangent dimension depends on $X$, not on the chosen bundle.

## 3. Lifting a line bundle and its obstruction

A small extension of local Artin $k$-algebras with residue field $k$ is a surjection

$$
0\longrightarrow J\longrightarrow A'\longrightarrow A\longrightarrow 0,
\qquad \mathfrak m_{A'}J=0. \tag{3.1}
$$

The ideal $J$ is a finite-dimensional $k$-vector space and $J^2=0$. We deform a bundle on the fixed schemes $X_{A'}\to X_A$; we are not simultaneously deforming $X$. There is an exact sequence

$$
0\longrightarrow \mathcal O_X\otimes_k J
\xrightarrow{u\mapsto 1+u}
\mathcal O_{X_{A'}}^{\times}
\longrightarrow \mathcal O_{X_A}^{\times}
\longrightarrow 1. \tag{3.2}
$$

Exactness on the right is local: a lift of an invertible element remains invertible across a nilpotent ideal. Cohomology gives a connecting map

$$
\delta_{A'/A}:\operatorname{Pic}(X_A)
\longrightarrow H^2(X,\mathcal O_X)\otimes_k J. \tag{3.3}
$$

**Theorem 3.1.** A line bundle $L_A$ on $X_A$ lifts to a line bundle on $X_{A'}$ if and only if $\delta_{A'/A}(L_A)=0$. If it lifts, its isomorphism classes of lifts form a torsor under $H^1(X,\mathcal O_X)\otimes_k J$. For lifts equipped with an identification of their reduction with $L_A$, the automorphisms inducing the identity on $L_A$ are the additive group $J$.

**Proof.** The relevant part of the cohomology sequence is

$$
H^0(\mathcal O_{X_{A'}}^{\times})\longrightarrow
H^0(\mathcal O_{X_A}^{\times})\longrightarrow
H^1(\mathcal O_X\otimes J)\longrightarrow
\operatorname{Pic}(X_{A'})\longrightarrow
\operatorname{Pic}(X_A)\xrightarrow{\delta_{A'/A}}
H^2(\mathcal O_X\otimes J). \tag{3.4}
$$

By (1.2), the first arrow is $A'^{\times}\to A^{\times}$, which is surjective. Thus $H^1(\mathcal O_X\otimes J)$ injects into $\operatorname{Pic}(X_{A'})$ and is exactly the kernel of the reduction map. Exactness proves the lifting criterion. If one lift exists, tensoring by the elements of this kernel acts freely and transitively on all lifts. Cohomology with vector-space coefficients gives $H^i(\mathcal O_X\otimes J)=H^i(\mathcal O_X)\otimes J$.

For identified lifts, changing the reduction identification does not introduce another orbit: the automorphisms of $L_A$ are $A^\times$, and each lifts to an element of $A'^\times$. An automorphism of a lift inducing the identity below is multiplication by a global unit $1+u$ with $u\in H^0(\mathcal O_X)\otimes J=J$. Its group law is addition because $J^2=0$. ∎

Here is the obstruction as a cocycle, including the choices. Choose a finite affine cover $\{U_i\}$ of $X$ on whose induced cover of $X_A$ the bundle is trivial. Such a cover exists: a trivialization on the special fibre extends across the nilpotent thickening on an affine open, since higher cohomology of its successive quasi-coherent nilpotent ideals vanishes. Refining the cover if necessary preserves affine intersections.

Choose transitions $g_{ij}\in\mathcal O_{X_A}^{\times}(U_i\cap U_j)$, with $g_{ji}=g_{ij}^{-1}$, and arbitrary lifts $\widetilde g_{ij}$ to $X_{A'}$, again with inverse transitions. On a triple intersection write

$$
\widetilde g_{ij}\widetilde g_{jk}\widetilde g_{ki}
=1+c_{ijk},\qquad c_{ijk}\in(\mathcal O_X\otimes J)(U_i\cap U_j\cap U_k).
\tag{3.5}
$$

On quadruple intersections associativity and commutativity give

$$
c_{jkl}-c_{ikl}+c_{ijl}-c_{ijk}=0. \tag{3.6}
$$

Replacing $\widetilde g_{ij}$ by $(1+b_{ij})\widetilde g_{ij}$ changes $c$ to $c+db$. Thus $[c]$ is independent of the lifts. Changes of local frames and refinements do not change the resulting cohomology class. This is precisely (3.3). Its vanishing permits a choice of $b$ for which the corrected transitions satisfy the cocycle equation, and hence glue a lift. Conversely a lifted bundle supplies transitions with $c=0$.

The construction is functorial under maps of small extensions and linear maps on $J$. In particular the obstruction is a specified class, not merely a dimension estimate. A nonzero space $H^2(X,\mathcal O_X)$ allows obstructions; it does not assert that every deformation has one.

For a bundle on $X$ itself, the constant pullback to $X_A$ always extends to $X_{A'}$. The potentially obstructed object is a previously chosen deformation of that bundle over $A$.

## 4. Two smoothness criteria

**Theorem 4.1.** The Picard scheme $P$ is smooth over $k$ if $H^2(X,\mathcal O_X)=0$.

**Proof.** Smoothness can be checked after the faithfully flat field extension $\bar k/k$, and (1.2) preserves the cohomology vanishing. Work therefore over $\bar k$. For each small extension (3.1), every element of $P(A)$ has a line-bundle representative by (1.4). Its obstruction lies in the zero group, so it lifts to $P(A')$ by Theorem 3.1.

This proves formal smoothness on local Artin tests at the identity. The finite-type infinitesimal criterion then proves smoothness at the identity; we use the criterion of [Stacks, Tag 02HX], as in the formal-moduli lesson. Every surjection between local Artin rings with the fixed residue field factors into small extensions, so the small-extension test is sufficient.

Translation carries the identity to each $\bar k$-point of $P$. Consequently $P$ is smooth at all closed points. The smooth locus is open, and any nonempty closed subset of a scheme locally of finite type over an algebraically closed field has a closed point. The nonsmooth locus is therefore empty. Descent gives smoothness over $k$. ∎

The characteristic-zero criterion has a different mechanism. Its essential input is the characteristic-zero differential criterion: a scheme locally of finite type over a characteristic-zero field with locally free sheaf of Kähler differentials is smooth [Stacks, Tag 04QN]. We now prove that a group scheme satisfies that hypothesis.

**Lemma 4.2.** If $G$ is a group scheme over a field $k$, with identity $e$, then

$$
\Omega_{G/k}\simeq \mathcal O_G\otimes_k e^*\Omega_{G/k}. \tag{4.1}
$$

**Proof.** The map

$$
G\times G\longrightarrow G\times G,
\qquad (g,h)\longmapsto(gh,h)
\tag{4.2}
$$

is an isomorphism over the second factor, with inverse $(a,h)\mapsto(ah^{-1},h)$. Relative differentials over that factor are the pullback of $\Omega_{G/k}$ from the first factor. Pull the resulting differential isomorphism back along $h\mapsto(e,h)$. On one side its first-coordinate map is $h\mapsto h$, and on the other it is the constant map $h\mapsto e$. This gives exactly (4.1). This argument does not assume that $G$ is reduced or smooth. ∎

**Theorem 4.3 (Cartier).** A group scheme locally of finite type over a field of characteristic zero is smooth. In particular $P$ is smooth when $\operatorname{char}k=0$.

**Proof.** The vector space $e^*\Omega_{G/k}$ is finite-dimensional by local finite type. Lemma 4.2 makes $\Omega_{G/k}$ a finite locally free module. Apply the characteristic-zero differential criterion above. ∎

The proof deliberately specifies the algebraic input. In positive characteristic locally free differentials do not imply smoothness. For example $\mu_p$ in characteristic $p$ has coordinate ring

$$
k[z,z^{-1}]/(z^p-1)=k[u]/(u^p),\qquad u=z-1.
\tag{4.3}
$$

Its sheaf of differentials is freely generated by $du$ because $d(u^p)=0$, yet its underlying scheme is nonreduced and zero-dimensional. Its tangent space at the identity has dimension one. This is exactly the phenomenon that the characteristic-zero criterion excludes.

## 5. The identity component and the dimension bound

Let $P^0$ be the connected component containing the identity, with its canonical group-scheme structure. We use the general group-scheme theorem [Stacks, Tag 0B7R]: for a group scheme locally of finite type over a field, the identity component is a closed, quasi-compact, geometrically irreducible subgroup scheme. In particular it is of finite type. It is also open here. Indeed a locally Noetherian scheme is locally connected: each Noetherian open has finitely many connected components, which are open. A connected neighbourhood of the identity lies in its connected component, and the same reasoning at every point makes that component open.

Hence $P^0$ is open and closed in $P$. Its formation commutes with field extension: its base change is geometrically connected and open and closed, contains the identity, and therefore is precisely the identity component after base change. This is also the assertion of Kleiman, Proposition 5.3.

The superscript $0$ retains the whole scheme structure. It does not mean the reduction $(P^0)_{\mathrm{red}}$. Over a perfect field the reduction of a finite-type group scheme is a smooth subgroup scheme: products of reduced schemes remain reduced, so multiplication restricts to the reduction, and generic smoothness followed by translations makes that reduced group smooth. Over an imperfect field, neither this product argument nor this smoothness assertion is automatic. Our dimension and tangent arguments use $P^0$, with its possible nilpotents, over every field.

**Theorem 5.1.** Under (1.1),

$$
\dim P^0\leq h^1(X,\mathcal O_X), \tag{5.1}
$$

and equality holds if and only if $P^0$ is smooth over $k$. Equivalently, equality holds if and only if $P$ is smooth.

**Proof.** Both sides of (5.1) are unchanged by extension to $\bar k$. Work over that field and let $R$ be the local ring at the identity. Its embedding dimension is $t=h^1(X,\mathcal O_X)$ by Proposition 2.1. The dimension of $R$ is the dimension $d$ of $P^0$: that component is irreducible of finite type, and a closed point on an irreducible finite-type scheme over a field has local dimension equal to its global dimension.

For completeness, the local algebra inequality can be seen directly. Lift a basis of $\mathfrak m_R/\mathfrak m_R^2$ to $t$ elements of $R$. They give a surjective map

$$
\bar k[[x_1,\ldots,x_t]]\longrightarrow \widehat R,
\qquad \widehat R=\bar k[[x_1,\ldots,x_t]]/I,
\quad I\subset(x_1,\ldots,x_t)^2. \tag{5.2}
$$

Surjectivity follows by successively approximating any element modulo powers of the maximal ideal; completeness then takes the limit. The condition on $I$ follows from the chosen tangent basis. Thus $d=\dim\widehat R\leq t$. If $d=t$, then $I=0$: the power-series ring is a regular local domain of dimension $t$, and its quotient by any nonzero ideal has dimension at most $t-1$. Therefore $R$ is regular. Over an algebraically closed field, regularity of a finite-type scheme at a closed point is equivalent to smoothness there. Translation gives smoothness on all of $P$ as in Theorem 4.1, and faithful-flat descent gives smoothness over the original $k$.

Conversely, if $P^0$ is smooth, the tangent dimension at the identity equals its dimension, proving equality. Finally $P^0$ is an open neighbourhood of the identity. Smoothness of $P^0$ makes $P$ smooth by translations after extending to $\bar k$, and smoothness of $P$ plainly implies smoothness of that open subscheme. ∎

Over an algebraic closure, every component is a translate of $P^0$. To see this, take a closed point on the component and translate it to the identity. Translation is a homeomorphism and an isomorphism of schemes, so it identifies the whole component with $P^0$. The dimensions and infinitesimal structures of components are therefore the same. The total Picard scheme can still have infinitely many components.

## 6. Algebraic equivalence and Néron–Severi groups

First work over an algebraically closed field. Two line bundles are algebraically equivalent if they can be connected by a finite chain of families of line bundles parameterized by connected schemes of finite type. More precisely, in each link an invertible sheaf on $X\times T$ has the two required bundles as fibres at two $k$-points of a connected finite-type $T$. Tensor product makes the bundles algebraically equivalent to $\mathcal O_X$ a subgroup, denoted $\operatorname{Pic}^0(X)$.

**Proposition 6.1.** Over an algebraically closed field,

$$
\operatorname{Pic}^0(X)=P^0(k). \tag{6.1}
$$

**Proof.** A family on a connected $T$ gives a morphism $T\to P$ whose image lies in one connected component. The difference of the classes at its two specified points belongs to $P^0(k)$, because components are cosets of $P^0$. This proves one inclusion, including chains of families.

For the converse, $X$ has a $k$-point because it is a nonempty finite-type scheme over an algebraically closed field. Rigidification at that point identifies the Picard sheaf with the functor of normalized invertible sheaves, as proved in the Picard-functor lesson. The universal point of $P^0$ therefore supplies an invertible sheaf on $X\times P^0$, normalized at the chosen point of $X$. Since $P^0$ is connected and of finite type, its fibres at the identity and at any $[L]\in P^0(k)$ give the required algebraic equivalence. ∎

Define the geometric Néron–Severi group for general $k$ by

$$
\operatorname{NS}_{\mathrm{geom}}(X)
=\operatorname{Pic}(X_{\bar k})/P^0_{\bar k}(\bar k).
\tag{6.2}
$$

For algebraically closed $k$, this is usually written simply $\operatorname{NS}(X)$. Its elements are connected-component classes. The component group can be expressed as an étale group scheme, possibly with infinitely many components; over $\bar k$ it is the constant group scheme associated with (6.2). This follows either from the general quotient by the open and closed subgroup $P^0$, or by gluing one point for each coset over $\bar k$ and descending the resulting étale scheme.

Here is the exact finiteness theorem used in this lesson.

**Finiteness input (the theorem of the base).** For every proper scheme $X$ over an algebraically closed field, $\operatorname{Pic}(X)/P^0(k)$ is a finitely generated abelian group. More generally, for a proper morphism $X\to S$ with $S$ Noetherian, the ranks and the orders of the torsion subgroups of the geometric-fibre Néron–Severi groups are bounded by a single integer. We use [AI Integrated Stacks Project, moduli.tex, theorem-picard-neron-severi-uniform-bounds], whose displayed quotient is by $P^0$, together with its first statement, item (vi) of Grothendieck's [complement to FGA, Exposé 236](https://www.numdam.org/item/SB_1961-1962__7__303_1/). The proof of the bounds in this generality is due to Kleiman (1971); see Kleiman, *The Picard scheme*, Corollary 6.17 and Remark 6.19. This theorem is stated here, not reproved.

There is an arithmetic distinction when $k$ is not algebraically closed. Define

$$
\operatorname{Pic}^0(X)=
\{L\in\operatorname{Pic}(X):[L]\in P^0(k)\},
\qquad
\operatorname{NS}_{\mathrm{arith}}(X)=
\operatorname{Pic}(X)/\operatorname{Pic}^0(X). \tag{6.3}
$$

The actual-bundle group $\operatorname{Pic}(X)$ injects into $P(k)$ by (1.3). Its pullback to $P(\bar k)$ is injective too, because equality of two $k$-points of a scheme can be checked faithfully flatly. Formation of $P^0$ commutes with field extension. It follows that (6.3) injects into (6.2). Thus the arithmetic group is finitely generated as a subgroup of a finitely generated abelian group, but it need not equal the geometric group. A real conic has only even degrees of actual real line bundles, while its geometric Néron–Severi group is $\mathbb Z$.

## 7. Torsion components and numerical equivalence

Define $P^\tau$ as the union of components whose image in the component group is torsion. Equivalently,

$$
P^\tau=\bigcup_{n\geq1}[n]^{-1}(P^0), \tag{7.1}
$$

where $[n]$ is tensor power. Each inverse image is open; after extending to $\bar k$, (7.1) is a union of whole components. Its complement is also a union of components, hence open. These properties descend, so $P^\tau$ is an open and closed subgroup scheme.

**Proposition 7.1.** The scheme $P^\tau$ is of finite type over $k$, and

$$
P^\tau/P^0
\tag{7.2}
$$

is a finite étale group scheme. Over $\bar k$ its group of points is exactly $\operatorname{NS}_{\mathrm{geom}}(X)_{\mathrm{tors}}$.

**Proof.** The torsion subgroup of a finitely generated abelian group is finite. By the finiteness input, only finitely many components of $P_{\bar k}$ occur in $P^\tau_{\bar k}$. Each is a translate of the finite-type scheme $P^0_{\bar k}$. Their finite disjoint union is of finite type, and this property descends to $k$. The quotient (7.2) is the finite part of the étale component group described in Section 6. After extending to $\bar k$ it is the finite constant torsion group, so it is finite étale before extension as well. ∎

The quotient in (7.2) can be étale even when $P^\tau$ itself is nonreduced. Nilpotents within the identity component disappear in the component quotient. Nor should $P^\tau$ be described as the set of torsion line bundles: a nontorsion bundle in $P^0$ belongs to $P^\tau$ because its component class is zero.

For numerical equivalence, work geometrically. An invertible sheaf $L$ on a proper $X/\bar k$ is numerically trivial if

$$
\deg(\nu^*L)=0 \quad\text{for every integral curve }C\subset X,
\tag{7.3}
$$

where $\nu:\widetilde C\to C\hookrightarrow X$ is its normalization. Degrees can also be defined by Euler characteristics on $C$; the zero-degree condition is unchanged by normalization.

Algebraic triviality implies numerical triviality. Restrict a connected family of invertible sheaves to $C\times T$. This is a flat coherent family on a proper curve over $T$. Its Euler characteristic is locally constant in $T$, by cohomology and base change. The degree, which is its Euler characteristic minus $\chi(\mathcal O_C)$, is therefore constant on connected $T$. A family joining $L$ to $\mathcal O_X$ forces degree zero on every $C$. Chains give the same conclusion.

If $L^{\otimes n}$ is algebraically trivial, then $n\deg(\nu^*L)=0$; the integer degree is consequently zero. Thus belonging to $P^\tau(\bar k)$ implies numerical triviality.

We use the converse as a second precise finiteness input: for every proper $X$ over an algebraically closed field,

$$
L\text{ is numerically trivial}
\quad\Longleftrightarrow\quad
L^{\otimes n}\text{ is algebraically trivial for some }n\geq1.
\tag{7.4}
$$

It is stated in [AI Integrated Stacks Project, moduli.tex, theorem-picard-tau-numerical-criteria] and, for every proper scheme over a field, in item (viii) of Grothendieck's complement to FGA, Exposé 236. For projective $X$, Kleiman, *The Picard scheme*, Theorem 6.3 gives the equivalent numerical, boundedness, and Euler-characteristic formulations; Remark 6.14 explains the extension to proper $X$. We have proved the forward implication from torsion of the component class to numerical triviality, and import the converse in the direction from numerical triviality to torsion of the component class.

Equation (7.4) concerns the whole numerical subgroup. It does not make every numerically trivial bundle algebraically trivial. Enriques surfaces provide the simplest counterexample below.

## 8. Curves and other examples

### Smooth projective curves

**Theorem 8.1.** Let $C$ be a smooth projective geometrically connected curve of genus $g$. Its identity component $\operatorname{Pic}^0_{C/k}$ is an abelian variety of dimension $g$. Moreover $\operatorname{Pic}^\tau_{C/k}=\operatorname{Pic}^0_{C/k}$ and $\operatorname{NS}_{\mathrm{geom}}(C)=\mathbb Z$, via degree.

**Proof.** Smoothness and geometric connectedness make $C$ geometrically integral, and $H^0(C,\mathcal O_C)=k$. A curve has $H^2(C,\mathcal O_C)=0$, so Theorem 4.1 makes the Picard scheme smooth. Proposition 2.1 gives tangent dimension $g$, hence dimension $g$ by Theorem 5.1.

The curve construction in the preceding two lessons proves that the degree-$d$ subschemes are open and closed, geometrically integral, and proper. Here is the properness mechanism again. For $d\geq0$ with $d>2g-2$, the Abel map $\operatorname{Sym}^d C\to\operatorname{Pic}^d_{C/k}$ is surjective on every geometric fibre and has projective-space fibres by Riemann–Roch and Serre duality. The symmetric power is proper. For any base change, the image of the inverse image of a closed subset is its image under the Picard structure map, by surjectivity; that image is closed because the symmetric power is proper. Finite type and separatedness of the degree piece therefore make it proper. Geometric translation carries this assertion to every degree, in particular degree zero.

The degree-zero piece is geometrically integral, contains the identity, and is therefore exactly $P^0$. A smooth proper geometrically connected group scheme over a field is an abelian variety and is projective; we use this projectivity theorem [Stacks, Tag 0BFA]. Thus $P^0$ is a smooth projective group scheme of dimension $g$.

Over $\bar k$, degree is surjective because there are points of degree one. Each degree piece is one component. The component group is consequently $\mathbb Z$, whose torsion subgroup is zero. This proves the remaining assertions, including equality of the subgroup schemes by (7.1) and base-change descent. ∎

A curve without a rational point can have fewer degrees of actual $k$-line bundles, as in the real-conic example. This does not change its geometric component group or the dimension of its Jacobian.

### A product of two curves

Let $C,D$ be smooth projective geometrically connected curves. After extending to $\bar k$, choose points $c\in C$ and $d\in D$. On $X=C\times D$ consider

$$
A=\operatorname{pr}_C^*\mathcal O_C(c),
\qquad B=\operatorname{pr}_D^*\mathcal O_D(d). \tag{8.1}
$$

On $C\times\{d\}$, their degrees are $1$ and $0$, while on $\{c\}\times D$ they are $0$ and $1$. If $A^{\otimes a}\otimes B^{\otimes b}$ is algebraically trivial, its degree on both curves is zero by Section 7. Therefore $a=b=0$. The classes of $A$ and $B$ generate a copy of $\mathbb Z^2$ in $\operatorname{NS}_{\mathrm{geom}}(X)$, so its rank is at least two. Additional classes can arise; the argument does not claim that these two generate the whole group.

### Abelian varieties

For an abelian variety $A/k$, the duality theorem states that

$$
A^\vee=\operatorname{Pic}^0_{A/k}
\tag{8.2}
$$

is an abelian variety of dimension $\dim A$. Rigidification at the identity gives a normalized Poincaré bundle on $A\times A^\vee$, trivial on both identity slices. We use this duality theorem as a stated input, with locator [AI Integrated Stacks Project, moduli.tex, theorem-dual-abelian-scheme], specialized to a field; the historical dual-abelian-scheme discussion occurs in FGA, Exposé 236, Theorem 3.3(iii). This is stronger than the vanishing criterion of Theorem 4.1: for abelian varieties of dimension at least two, $H^2(A,\mathcal O_A)$ need not vanish, yet their Picard schemes are smooth.

### Enriques surfaces

For an Enriques surface over an algebraically closed field of characteristic different from two, the classification input is

$$
h^1(\mathcal O_X)=h^2(\mathcal O_X)=0,
\qquad \operatorname{Pic}^\tau_{X/k}\simeq(\mathbb Z/2\mathbb Z)_k,
\tag{8.3}
$$

with nonzero class the canonical bundle. See Liedtke, *Arithmetic Moduli and Lifting of Enriques Surfaces*, Section 1, especially Definition 1.2 and the following Picard-scheme description. We state this classification without proof. Our own results then imply $P^0=\operatorname{Spec}k$, and hence $P^\tau/P^0=(\mathbb Z/2\mathbb Z)_k$. The canonical bundle is numerically trivial but not algebraically trivial.

In characteristic two, the same source identifies $P^\tau$ for singular and supersingular Enriques surfaces with $\mu_2$ and $\alpha_2$, respectively. Both are connected and nonreduced, so in these cases $P^\tau=P^0$ although their tangent space is nonzero. The torsion of the component group is therefore zero; it does not measure these nilpotents.

### Igusa's nonreduced example

There is also a smooth projective surface in characteristic two for which

$$
\dim\operatorname{Pic}^0_{X/k}=1,
\qquad h^1(X,\mathcal O_X)=2. \tag{8.4}
$$

This is Igusa's example in [*On some problems in abstract algebraic geometry*](https://pmc.ncbi.nlm.nih.gov/articles/PMC534315/), Proceedings of the National Academy of Sciences 41 (1955), pp. 964–967; the precise numerical statement we use is verified in Kleiman, *The Picard scheme*, Remark 5.15. The construction is an input, not a construction supplied here. Theorem 5.1 proves immediately from (8.4) that the identity component is not smooth. Over the perfect ground field of the example, a reduced finite-type group scheme would be smooth, so this component is nonreduced. A point-set description of line bundles cannot recover its additional tangent direction.

## 9. Exercises

**Exercise 1.** Compute the tangent space at the identity of the Picard scheme of $\mathbb P^n_k$ and of a smooth projective geometrically connected curve of genus $g$. Include $n=0$.

**Exercise 2.** For a small extension (3.1), construct the obstruction to lifting a line bundle using transition functions. Prove its independence of choices and prove that, when it vanishes, the isomorphism classes of identified lifts form the claimed torsor.

**Exercise 3.** Let $X$ be a smooth projective geometrically connected surface with geometric genus $p_g=h^0(X,\omega_X)=0$. Prove that its Picard scheme is smooth in every characteristic. Explain why this need not make it connected.

**Exercise 4.** Starting from $T_0P=H^1(X,\mathcal O_X)$, prove $\dim P^0\leq h^1(X,\mathcal O_X)$. Prove the equality criterion and identify exactly where passage to an algebraic closure is useful.

**Exercise 5.** For a smooth projective geometrically connected curve $C/k$, prove that a line bundle is geometrically numerically trivial exactly when it has degree zero. Deduce $\operatorname{Pic}^\tau_{C/k}=\operatorname{Pic}^0_{C/k}$ as subgroup schemes. Explain what changes if $C$ has no rational point.

## 10. Complete solutions

**Solution 1.** Projective-space cohomology gives $H^1(\mathbb P^n_k,\mathcal O)=0$ for $n\geq1$. For $n=0$, the scheme is $\operatorname{Spec}k$, whose higher cohomology vanishes. Proposition 2.1 therefore gives zero tangent space in every case. In fact the Picard scheme is constant $\mathbb Z$ for $n\geq1$ and trivial for $n=0$, as proved in the preceding lessons. For a curve, $H^1(C,\mathcal O_C)$ has dimension $g$ by definition of genus, so its tangent space is canonically that $g$-dimensional vector space. Theorem 8.1 shows that this tangent dimension equals the dimension of the Jacobian.

**Solution 2.** Choose an affine cover and transitions $g_{ij}$ as in Section 3. Lift them to units $\widetilde g_{ij}$ and use (3.5) to define $c_{ijk}$. The four ways of multiplying transitions on a quadruple intersection give (3.6), since all products of two elements in $J$ vanish. Thus $c$ is a 2-cocycle in $\mathcal O_X\otimes J$.

For new lifts $(1+b_{ij})\widetilde g_{ij}$, the triple product changes by $1+b_{ij}+b_{jk}-b_{ik}$. The new obstruction cocycle is $c+db$. Changes of frames change the transition cocycles by conjugating with local units; units commute, and the contributions cancel around each triple. A refinement pulls back the same cohomology class. Therefore $[c]\in H^2(\mathcal O_X)\otimes J$ is canonical. Its vanishing supplies $b$ with $db=-c$, producing transitions satisfying the gluing equation and hence a lift. A lift implies vanishing by choosing its transitions.

Fix one lift with transitions $\widetilde g_{ij}$. Any other identified lift has transitions $(1+a_{ij})\widetilde g_{ij}$ after lifting the reduction frames. Both sets satisfy the cocycle equation exactly when $da=0$. An isomorphism inducing the identity below changes $a$ by the coboundary of local elements $u_i\in\mathcal O_X\otimes J$. Hence the identified lifts are classified, relative to the chosen lift, by $H^1(\mathcal O_X)\otimes J$. Choosing another initial lift translates this identification, so the intrinsic object is a torsor. Finally global automorphisms of the reduced bundle lift because $A'^\times\to A^\times$ is surjective, so forgetting the reduction identification does not alter the torsor of isomorphism classes.

**Solution 3.** Serre duality for the smooth projective surface gives

$$
H^2(X,\mathcal O_X)\simeq H^0(X,\omega_X)^*.
\tag{10.1}
$$

Thus $p_g=0$ implies $H^2(X,\mathcal O_X)=0$, and Theorem 4.1 applies. Geometric connectedness gives $H^0(X,\mathcal O_X)=k$. No characteristic restriction occurs in this argument. Smoothness governs each component's infinitesimal structure, not the number of components. For example $X=\mathbb P^2_k$ has $p_g=0$ and smooth Picard scheme $\mathbb Z_k$, with infinitely many components. An Enriques surface in characteristic different from two gives a smooth Picard scheme whose finite torsion-component subgroup is nontrivial.

**Solution 4.** Extend to $\bar k$. Both the dimension of $P^0$ and $h^1$ remain unchanged. The local ring $R$ at the identity has embedding dimension $h^1$ by Proposition 2.1, and local dimension $\dim P^0$ because $P^0_{\bar k}$ is irreducible of finite type. The surjection (5.2) gives the desired inequality. Equality forces its kernel to be zero, since a nonzero ideal in the power-series domain lowers dimension. Thus $R$ is regular and the Picard scheme is smooth at the identity over $\bar k$. Translation makes it smooth everywhere, and descent gives smoothness over $k$. Conversely smoothness equates local dimension with tangent dimension. Passage to $\bar k$ justifies the implication from regularity to smoothness without an imperfect-field separability issue; one must not use regularity at a point alone as an unrestricted smoothness test over an imperfect field.

**Solution 5.** Over $\bar k$, the only closed integral curve in the integral one-dimensional scheme $C_{\bar k}$ is $C_{\bar k}$ itself. Thus condition (7.3) is precisely $\deg L=0$. The degree is unchanged by field extension for a line bundle defined over $k$. The degree-zero Picard subscheme is the identity component by Theorem 8.1. If a component has degree $d$, its $n$th tensor power has degree $nd$. It can meet degree zero for some positive $n$ only if $d=0$. Hence $P^\tau_{\bar k}=P^0_{\bar k}$, including their scheme structures: each is the same union of open and closed components. Faithfully flat descent proves equality over $k$.

Without a rational point, every geometric degree piece still exists, but some $k$-points of the Picard sheaf need not be represented by actual line bundles, and some integer degrees may have no actual $k$-line bundle. Degree zero remains exactly the identity component geometrically, and the equality of subgroup schemes remains valid. On a real nonsplit conic, actual real bundles have even degree, but the geometric degree group is $\mathbb Z$ and the Jacobian is trivial.

## 11. What this lesson does not prove

The following are exact inputs, rather than omitted steps in the central deformation proofs.

- **General proper-scheme representability.** Murre's result (II.15), as stated in Kleiman, Corollary 4.18.3 and the following discussion, supplies the locally finite-type Picard group scheme for arbitrary proper $X/k$. The preceding lesson proves the projective geometrically integral case and arbitrary base change in that setting.
- **Cohomology and descent foundations.** Affine acyclicity and separated affine Čech computation are [Stacks, Tags 01XD and 01KP]; proper-support finiteness is [Stacks, Tag 02O6]. The preceding Picard-functor lesson supplies the injections, equality of étale and fppf sheaves, and rigidification theorem. Étale-local Artin rings with separably closed residue field are strictly henselian, so étale covers have sections; descent of smoothness and the local Artin smoothness criterion are standard infinitesimal foundations, with the latter [Stacks, Tag 02HX].
- **Characteristic-zero algebra.** The criterion that a locally finite-type scheme over a characteristic-zero field with locally free differentials is smooth is [Stacks, Tag 04QN]. Lemma 4.2 proves the group-scheme differential trivialization, and Theorem 4.3 deduces Cartier's theorem from that criterion.
- **Identity components and local algebra.** The canonical closed, quasi-compact, geometrically irreducible identity subgroup is [Stacks, Tag 0B7R]; its finite-type and base-change properties also occur in Kleiman, Proposition 5.3. Completion preserves dimension; a power-series ring is a regular local domain; a nonzero ideal in it lowers dimension. The corresponding local-algebra ingredients were used in the Hilbert–Quot dimension bound. Generic smoothness for reduced finite-type schemes over a perfect field is the input used only for the reduction comment and the nonreduced-example deduction.
- **Finiteness and numerical characterization.** The theorem of the base is the exact statement in Section 6, with [AI Integrated Stacks Project, moduli.tex, theorem-picard-neron-severi-uniform-bounds], item (vi) of Grothendieck's complement to FGA, Exposé 236, and Kleiman, Corollary 6.17 and Remark 6.19, as references. The converse numerical implication (7.4) is [AI Integrated Stacks Project, moduli.tex, theorem-picard-tau-numerical-criteria], item (viii) of the same complement, and Kleiman, Theorem 6.3 with Remark 6.14. No reduction sketch is claimed as a proof of these inputs.
- **Curve and abelian-variety foundations.** Riemann–Roch and Serre duality, including (10.1), are imported cohomological prerequisites. The full Abel construction, connected degree pieces, and properness argument belong to the preceding two lessons. Projectivity of an abelian variety is [Stacks, Tag 0BFA]. Dual abelian varieties and the normalized Poincaré bundle are the stated theorem [AI Integrated Stacks Project, moduli.tex, theorem-dual-abelian-scheme], specialized to a field.
- **Special surfaces.** The Enriques classification statements are Liedtke, *Arithmetic Moduli and Lifting of Enriques Surfaces*, Section 1. Igusa's existence and the values in (8.4) are the example recorded in Kleiman, Remark 5.15, with the original 1955 article identified there. Their surface constructions are not supplied here.

## 12. Sources and historical placement

Grothendieck's [FGA, Exposé 236](https://www.numdam.org/item/SB_1961-1962__7__221_0/) separates local group-scheme structure, Picard smoothness, canonical abelian subschemes, and finiteness. Proposition 2.10(iii) contains the dimension and characteristic-zero smoothness statements; Theorem 3.3 treats the canonical abelian subscheme and Albanese construction; Section 4 concerns boundedness and finite-type Picard loci. The stronger proper-family finiteness statements appear in the later [complement to Exposé 236](https://www.numdam.org/item/SB_1961-1962__7__303_1/) and in the finiteness theorems of Raynaud and Kleiman (1971), which Kleiman, *The Picard scheme*, Section 6, surveys. We keep the field-level deformation proof distinct from those relative finiteness results.

[Kleiman, *The Picard scheme*](https://arxiv.org/abs/math/0504020), Sections 5–6, gives precise component, tangent, smoothness, numerical-equivalence and boundedness formulations. In particular Theorem 5.11, Corollaries 5.13–5.14 and Remark 5.15 provide useful comparisons for Sections 2–5 and the nonreduced example. The numerical discussion distinguishes $\operatorname{Pic}^0$, $\operatorname{Pic}^\tau$, and their quotient.

[Liedtke, *Arithmetic Moduli and Lifting of Enriques Surfaces*](https://arxiv.org/abs/1007.0787), Section 1, gives the surface classifications used above. The characteristic-two examples show why the component group and the infinitesimal identity component must be retained as different pieces of information.

The next lesson replaces ad hoc presentations by the cotangent complex. Its deformation groups extend the same pattern seen here: degree zero records infinitesimal automorphisms, degree one records first-order changes, and degree two records obstructions.
