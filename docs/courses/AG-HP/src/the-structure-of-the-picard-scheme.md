# The structure of the Picard scheme

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Picard scheme records two kinds of information. Its tangent space measures how a line bundle changes over a first-order thickening. Its components record discrete classes of line bundles. These interact: in positive characteristic a component can have more tangent directions than its dimension, and torsion classes can occur in components other than the identity component.

We construct the Picard scheme of every proper scheme over a field, using finite infinitesimal frames and scheme coordinates for group spaces. We compute tangent spaces and lifting obstructions and prove two smoothness criteria. We also prove that, on every proper scheme, numerical triviality is equivalent to algebraic triviality of a positive tensor power, and that the torsion components form a scheme of finite type. We prove finite generation of the Néron–Severi group and uniform bounds for both its rank and torsion order in every proper Noetherian family. Curve degrees, étale cohomology, relative numerical boundedness and geometric component counts supply the proofs.

## 1. Setting and the distinction between bundles and classes

Let $X$ be a proper scheme over a field $k$, with

$$
H^0(X,\mathcal O_X)=k. \tag{1.1}
$$

Write $P=\operatorname{Pic}_{X/k}$ for the fppf Picard sheaf. Theorem 1.2 below represents it by a separated group scheme locally of finite type and proves field-extension compatibility for every proper $X/k$. The preceding lesson, Relative divisors and the existence of the Picard scheme, gives a separate projective construction with its relative-base hypotheses. The general proper-field existence theorem is due to Murre: [*On contravariant functors from the category of preschemes over a field into the category of abelian groups*](https://www.numdam.org/item/PMIHES_1964__23__5_0/), result (II.15); see also Kleiman, *The Picard scheme*, Corollary 4.18.3 and its following historical discussion. Our finite-frame argument below uses the earlier algebraicity theorem for the Picard stack.

Condition (1.1) holds universally. Indeed, choose a finite affine covering of $X$. Since $X$ is separated, its finite intersections are affine, and the Čech complex computes coherent cohomology. For any $k$-algebra $A$, tensoring that complex with $A$ is exact on cohomology because $A$ is flat over $k$. Thus

$$
\begin{gathered}
H^i(X_A,\mathcal O_{X_A})=H^i(X,\mathcal O_X)\otimes_k A,\\
H^0(X_A,\mathcal O_{X_A})=A.
\end{gathered} \tag{1.2}
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

### Scheme coordinates for group spaces

We first prove the scheme-recognition result needed for field-valued Picard problems. The finite-type hypothesis is local on the group, so infinitely many components are allowed.

**Lemma 1.1.** A quasi-separated group algebraic space $G$, locally of finite type over a field $k$, is a separated scheme.

**Proof.** Write $e:\operatorname{Spec}k\to G$ for the identity. For an affine étale chart $U\to G$, the scheme

$$
E=U\times_G\operatorname{Spec}k
$$

is étale over $k$. It is quasi-compact: the map $E\to U$ is a pullback of the quasi-compact diagonal of $G$, and $U$ is quasi-compact. Thus $E$ is a finite disjoint union of spectra of finite separable extensions of $k$, and is finite over $k$. The monomorphism $E\to U$ is finite. Indeed its coordinate algebra is finite-dimensional over $k$, hence finite over the coordinate ring of $U$ too.

A finite monomorphism is a closed immersion. Here is the ring argument. For a finite ring map $A\to B$ representing a monomorphism, multiplication $B\otimes_A B\to B$ is an isomorphism. At a residue field of $A$, the dimension $d$ of the resulting finite algebra satisfies $d^2=d$, so it is either zero or the residue field itself. Nakayama then says that $1$ generates $B$ over each local ring of $A$. Thus $A\to B$ is surjective. Applied to our charts, this proves that $e$ is a closed immersion. The diagonal of $G$ is its pullback by $(g,h)\mapsto g^{-1}h$, since this difference equals $e$ exactly when $g=h$. Hence $G$ is separated.

Put $\bar G=G_{\bar k}$. Every nonempty finite-type open in $\bar G$ has a nonempty affine open by Quotients and torsors, Lemma 11.1a. Choose a rational point $v$ in one such affine open $V$. Translation makes $v^{-1}V$ an affine open containing the identity. Its translates by all points of $\bar G(\bar k)$ cover $\bar G$. Otherwise their closed complement would pull back to a nonempty closed subset of a finite-type affine étale chart, and would have a $\bar k$-point. That contradicts the construction. Thus $\bar G$ is a scheme, with its original nilpotents.

We need one further fact about this scheme: any finite set of its geometric points lies in an affine open. Its identity component is irreducible, open and of finite type, by Group schemes over a field, Theorems 2.2–2.3. Every other component is a translate. For the finitely many components meeting the specified set, choose one nonempty affine open in each. Their disjoint union $V$ is affine. For every specified point $x$, the condition $g x\in V$, with $g\in\bar G^0$, defines a nonempty open in the irreducible scheme $\bar G^0$. Their finite intersection has a rational point $g$. Then $g^{-1}V$ is an affine open containing the whole finite set. No smoothness or reduction was used.

We now obtain affine opens over $k$. Let $x\in|G|$ have a representative over a finite extension of $k$. The geometric points above it form a finite set. Choose an affine open $V_{\bar k}\subset\bar G$ containing them. There is a finite extension $K/k$ and an affine open

$$
V_K\subset G_K
$$

whose base change is $V_{\bar k}$. To justify descent, write the coordinate algebra of $V_{\bar k}$ by finitely many generators and relations. Its map to $G$ also uses finitely many data: pull back affine étale charts, choose finitely many affine pieces covering the source, and record their maps and overlap arrows. The relation between finite-type affine charts of the separated space $G$ is affine and finitely presented. The maps, their equations and the cocycle equalities therefore descend to a common finite extension $K$. This constructs $V_K\to G_K$. Being an open immersion descends through the faithfully flat field extension $\bar k/K$, so it is the required open. Enlarging $K$ causes no problem. It need not be separable.

Here is an affine descent argument that retains this possible inseparability. Let

$$
p:G_K\longrightarrow G.
$$

It is finite locally free. The closed set $p(G_K\setminus V_K)$ misses $x$. Set $O=G\setminus p(G_K\setminus V_K)$, so $p^{-1}O\subset V_K$ and $x\in O$. The fibre above $x$ is finite and lies in this open subset of the affine scheme $V_K$. Finite prime avoidance supplies a function $f$ on $V_K$ such that

$$
p^{-1}(x)\subset D_{V_K}(f)\subset p^{-1}O.
$$

Namely, take $f$ in the ideal of the closed complement of $p^{-1}O$ in $V_K$, outside the finitely many fibre primes. On $O$ form the determinant norm $g=N_p(f)$ for the finite locally free map $p^{-1}O\to O$. The value $g(x)$ is nonzero: multiplication by $f$ is invertible on that finite fibre algebra. This criterion includes its nilpotents.

The inverse image of $O_g$ is affine. It lies in $D_{V_K}(f)$ because an invertible norm forces $f$ to be a unit, and it is the principal open defined there by $p^*g$. Thus

$$
W=p^{-1}(O_g)
$$

is an affine scheme finite locally free and surjective over $O_g$. Its relation $W\times_{O_g}W$ is affine with finite locally free projections. The affine effective quotient theorem, Quotients and torsors, Theorem 4.3, represents its fppf quotient by an affine scheme. That quotient sheaf is $O_g$ itself. Hence $O_g$ is an affine open of $G$ containing $x$.

These affine opens cover $G$. If their complement were nonempty, a finite-type affine étale chart meeting it would give a closed point of that inverse image; its residue field is finite over $k$. Its image would be one of the points just covered. Therefore the complement is empty. This proves the lemma over every field. $\square$

### A finite subscheme that removes automorphisms

We can now construct the Picard scheme of every proper $k$-scheme. For this construction only, drop condition (1.1), and allow the finite $k$-algebra of global functions to be larger than $k$.

**Theorem 1.2 (proper-field Picard representability).** If $X$ is a proper scheme over a field $k$, its fppf Picard sheaf is represented by a separated group scheme locally of finite type over $k$. Formation of that scheme commutes with every field extension. No reducedness, smoothness, projectivity or geometric-integrality assumption is required.

**Proof.** The empty scheme has the trivial Picard sheaf, represented by $\operatorname{Spec}k$. Assume $X$ is nonempty and put $C=H^0(X,\mathcal O_X)$. Proper coherent cohomology, Corollary 5.1, makes $C$ finite-dimensional over $k$. The affine Čech calculation in (1.2), without the restriction $C=k$, gives

$$
(p_T)_*\mathcal O_{X_T}
\simeq C\otimes_k\mathcal O_T
$$

for every $k$-scheme $T$. Consequently the automorphism group of any line bundle on $X_T$ is the base change of the group of units of $C$.

There is a finite closed subscheme $Z\subset X$ such that restriction is injective:

$$
C\hookrightarrow D=H^0(Z,\mathcal O_Z). \tag{1.5}
$$

To see this, a nonzero global function has a nonzero germ at some closed point of its coherent support. Krull intersection, Theorem 6.1, in that Noetherian local ring detects the germ modulo some power of its maximal ideal. This quotient is the coordinate ring of a finite infinitesimal neighbourhood of the closed point in $X$. The kernels of all these restriction maps have intersection zero in the finite-dimensional vector space $C$. A finite selection already has zero intersection: whenever a remaining kernel is nonzero, select one restriction which decreases its dimension. The finite union of the selected closed neighbourhoods is $Z$. This construction detects nilpotent global functions as well as reduced ones.

For a finite commutative $k$-algebra $A$, let $U(A)$ denote its unit group functor,

$$
U(A)(R)=(A\otimes_kR)^\times.
$$

It is a smooth affine group scheme of finite type: it is the principal open in the affine vector space of $A$ where the determinant of multiplication is invertible. The injection (1.5) gives a closed subgroup

$$
H=U(C)\hookrightarrow J=U(D). \tag{1.6}
$$

Indeed $C$ is a linear closed subspace of $D$, and the injection remains injective after every $k$-algebra extension. Choose a vector-space complement to $C$ in $D$. For $c\in C_R$, multiplication by $c$ on $D_R$ preserves $C_R$, so its matrix is block triangular in these bases. Its determinant is the product of the determinants on $C_R$ and $D_R/C_R$. If the determinant on $D_R$ is a unit, the determinant on $C_R$ is a unit too, and multiplication by $c$ is invertible on $C_R$. Thus $c$ is already a unit there. The inverse image of the open unit locus of $D_R$ is therefore exactly the unit locus of $C_R$, on every test algebra. This proves the closed-subgroup assertion. The groups commute, so $H$ is normal. The quotient theorem for closed algebraic subgroups, Quotients and torsors, Theorem 11.1b, supplies the finite-type group scheme

$$
K=J/H,
$$

with $J\to K$ an fppf $H$-torsor.

Consider line bundles on $X_T$ with a frame along $Z_T$:

$$
(L,\alpha),\qquad
\alpha:L|_{Z_T}\xrightarrow{\sim}\mathcal O_{Z_T}. \tag{1.7}
$$

Their isomorphism classes form an fppf sheaf $R_Z$. An automorphism of $L$ is an element of $H(T)$; preserving the frame makes its image in $J(T)$ equal to $1$, so injectivity in (1.6) makes it the identity. Isomorphisms preserving the frames are therefore unique, and effective descent of line bundles and their frames gives the sheaf assertion.

The Picard stack of all line bundles on $X$ is algebraic and locally of finite presentation by Moduli stacks are algebraic, Theorem 7.2: $X/k$ is proper, flat and of finite presentation. Its forgetful map from framed bundles has, over $L/T$, the scheme of frames of $L|_{Z_T}$ as fibre. This is a smooth surjective $J_T$-torsor. Concretely, an inverse frame is a generator of $L|_{Z_T}$. Push that line bundle forward along the finite locally free map $Z_T\to T$; its sections form a vector bundle on $T$, and the generator condition is the nonvanishing of the determinant of $D_T\to L|_{Z_T}$. Every geometric fibre admits a generator because an invertible module over a finite Artinian algebra is free. Hence that open frame scheme is smooth and surjective.

Pulling back a smooth scheme atlas of the Picard stack gives a representable smooth surjection from a scheme to $R_Z$. Its diagonal is represented by the isomorphisms preserving the finite frame. Frame compatibility is a closed condition in the affine Isom scheme: restrict the homomorphism to the finite scheme $Z_T$ and equate it to the homomorphism specified by the two frames. The flat sheaf-bootstrap theorem consequently makes $R_Z$ an algebraic space locally of finite presentation.

The group $J$ changes the frame. Its subgroup $H$ acts trivially on framed **isomorphism classes**, since the change is induced by a global automorphism of $L$. Thus the action factors through $K=J/H$. This action is free on all parameter schemes: locally lift a proposed stabilizer from $K$ to $J$; an isomorphism between the resulting framed pairs must be a global unit in $H$, so its class in $K$ is the identity.

The quotient sheaf $R_Z/K$ is exactly the fppf Picard sheaf $P$. Every line bundle has a frame after a covering of its parameter scheme. Two such framed objects represent the same Picard-sheaf class exactly when, locally on that parameter scheme, their underlying line bundles are isomorphic; their two frames then differ by an element of $J$. This identifies the quotient sheaves on every test scheme. Sheafifying the quotient by base line bundles gives the same sheaf, because a base line bundle becomes trivial on a cover.

Since $K/k$ is flat and of finite presentation, the free-action quotient theorem represents $P$ by an algebraic space, with $R_Z\to P$ a $K$-torsor. It is locally of finite presentation over $k$, as follows on this flat presentation from the corresponding property of $R_Z$.

It remains to prove the separation hypothesis needed by Lemma 1.1. Given two maps $T\to P$, work fppf locally on $T$ so they have line-bundle representatives $L,M$. Their isomorphism scheme

$$
I=\underline{\operatorname{Isom}}_{X_T/T}(L,M)
$$

is affine of finite presentation by Moduli stacks are algebraic, Corollary 1.3. Its hypotheses hold for both bundles: finite presentation, relative flatness and proper support. If $E\subset T$ is the fibre of the diagonal of $P$, the map $I\to E$ is an $H_T$-torsor. It is surjective as an fppf sheaf, since equality of the two Picard classes means local isomorphism. After every affine base change on $T$, its affine source is quasi-compact. The surjective image $E$ is consequently quasi-compact too. Quasi-compactness descends from our fppf cover of $T$, proving that the diagonal of $P$ is quasi-compact.

Thus $P$ is a quasi-separated group algebraic space locally of finite type over $k$. Lemma 1.1 makes it a separated scheme. Finally the definition of the fppf Picard sheaf commutes with field extension: its restriction to schemes over a new field is the sheaf for the pulled-back proper scheme. Uniqueness of representing objects gives the stated base-change isomorphism. $\square$

For the remainder of the lesson we again impose (1.1). Then $C=k$, so the automorphism group used above is simply $\mathbb G_m$. The construction proves the full proper-field existence statement; the preceding lesson's projective quotient construction remains a separate proof with its relative-base hypotheses.


## 2. The square-zero sequence and the tangent space

Put $D=k[\epsilon]/(\epsilon^2)$. The tangent space at the identity is the kernel

$$
T_0P=\ker\bigl(P(D)\longrightarrow P(k)\bigr). \tag{2.1}
$$

The underlying topological spaces of $X_D$ and $X$ are identical. Their sheaves of units fit into a split exact sequence of abelian sheaves on the Zariski site of $X$:

$$
0\to \mathcal O_X
\xrightarrow{a\mapsto 1+\epsilon a}
\mathcal O_{X_D}^{\times}
\to \mathcal O_X^{\times}
\to 1. \tag{2.2}
$$

The multiplication rule $(1+\epsilon a)(1+\epsilon b)=1+\epsilon(a+b)$ identifies the kernel with the additive sheaf $\mathcal O_X$. Constants provide the splitting. Since first cohomology of units classifies line bundles, taking cohomology gives

$$
\begin{gathered}
\ker\bigl(\operatorname{Pic}(X_D)\to\operatorname{Pic}(X)\bigr)\\
\simeq H^1(X,\mathcal O_X).
\end{gathered} \tag{2.3}
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
\begin{gathered}
0\longrightarrow J\longrightarrow A'\longrightarrow A\longrightarrow 0,\\
\mathfrak m_{A'}J=0.
\end{gathered} \tag{3.1}
$$

The ideal $J$ is a finite-dimensional $k$-vector space and $J^2=0$. We deform a bundle on the fixed schemes $X_{A'}\to X_A$; we are not simultaneously deforming $X$. There is an exact sequence

$$
\begin{gathered}
0\to \mathcal O_X\otimes_k J
\xrightarrow{u\mapsto 1+u}\mathcal O_{X_{A'}}^{\times}\\
\longrightarrow \mathcal O_{X_A}^{\times}\longrightarrow 1.
\end{gathered} \tag{3.2}
$$

Exactness on the right is local: a lift of an invertible element remains invertible across a nilpotent ideal. Cohomology gives a connecting map

$$
\delta_{A'/A}:\operatorname{Pic}(X_A)
\to H^2(X,\mathcal O_X)\otimes_k J. \tag{3.3}
$$

**Theorem 3.1.** A line bundle $L_A$ on $X_A$ lifts to a line bundle on $X_{A'}$ if and only if $\delta_{A'/A}(L_A)=0$. If it lifts, its isomorphism classes of lifts form a torsor under $H^1(X,\mathcal O_X)\otimes_k J$. For lifts equipped with an identification of their reduction with $L_A$, the automorphisms inducing the identity on $L_A$ are the additive group $J$.

**Proof.** The relevant part of the cohomology sequence is

$$
\begin{aligned}
H^0(\mathcal O_{X_{A'}}^{\times})&\longrightarrow H^0(\mathcal O_{X_A}^{\times})\\
&\longrightarrow H^1(\mathcal O_X\otimes J)\\
&\longrightarrow\operatorname{Pic}(X_{A'})\\
&\longrightarrow\operatorname{Pic}(X_A)\\
&\xrightarrow{\delta_{A'/A}}H^2(\mathcal O_X\otimes J).
\end{aligned} \tag{3.4}
$$

By (1.2), the first arrow is $A'^{\times}\to A^{\times}$, which is surjective. Thus $H^1(\mathcal O_X\otimes J)$ injects into $\operatorname{Pic}(X_{A'})$ and is exactly the kernel of the reduction map. Exactness proves the lifting criterion. If one lift exists, tensoring by the elements of this kernel acts freely and transitively on all lifts. Cohomology with vector-space coefficients gives $H^i(\mathcal O_X\otimes J)=H^i(\mathcal O_X)\otimes J$.

For identified lifts, changing the reduction identification does not introduce another orbit: the automorphisms of $L_A$ are $A^\times$, and each lifts to an element of $A'^\times$. An automorphism of a lift inducing the identity below is multiplication by a global unit $1+u$ with $u\in H^0(\mathcal O_X)\otimes J=J$. Its group law is addition because $J^2=0$. ∎

Here is the obstruction as a cocycle, including the choices. Choose a finite affine cover $\{U_i\}$ of $X$ on whose induced cover of $X_A$ the bundle is trivial. Such a cover exists: a trivialization on the special fibre extends across the nilpotent thickening on an affine open, since higher cohomology of its successive quasi-coherent nilpotent ideals vanishes. Refining the cover if necessary preserves affine intersections.

Choose transitions $g_{ij}\in\mathcal O_{X_A}^{\times}(U_i\cap U_j)$, with $g_{ji}=g_{ij}^{-1}$, and arbitrary lifts $\widetilde g_{ij}$ to $X_{A'}$, again with inverse transitions. On a triple intersection write

$$
\begin{gathered}
\widetilde g_{ij}\widetilde g_{jk}\widetilde g_{ki}=1+c_{ijk},\\
c_{ijk}\in(\mathcal O_X\otimes J)(U_i\cap U_j\cap U_k).
\end{gathered} \tag{3.5}
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

The characteristic-zero criterion has a different mechanism. Its algebraic ingredient is the characteristic-zero differential criterion: a scheme locally of finite type over a characteristic-zero field with locally free sheaf of Kähler differentials is smooth. The derivation and regular-parameter proof is Lie algebras and smoothness of group schemes, Lemmas 4.1–4.2. We now prove that a group scheme satisfies that hypothesis.

**Lemma 4.2.** If $G$ is a group scheme over a field $k$, with identity $e$, then

$$
\Omega_{G/k}\simeq \mathcal O_G\otimes_k e^*\Omega_{G/k}. \tag{4.1}
$$

**Proof.** The map

$$
\begin{gathered}
G\times G\longrightarrow G\times G,\\
(g,h)\longmapsto(gh,h).
\end{gathered} \tag{4.2}
$$

is an isomorphism over the second factor, with inverse $(a,h)\mapsto(ah^{-1},h)$. Relative differentials over that factor are the pullback of $\Omega_{G/k}$ from the first factor. Pull the resulting differential isomorphism back along $h\mapsto(e,h)$. On one side its first-coordinate map is $h\mapsto h$, and on the other it is the constant map $h\mapsto e$. This gives exactly (4.1). This argument does not assume that $G$ is reduced or smooth. ∎

**Theorem 4.3 (Cartier).** A group scheme locally of finite type over a field of characteristic zero is smooth. In particular $P$ is smooth when $\operatorname{char}k=0$.

**Proof.** The vector space $e^*\Omega_{G/k}$ is finite-dimensional by local finite type. Lemma 4.2 makes $\Omega_{G/k}$ a finite locally free module. Apply the characteristic-zero differential criterion above. ∎

The proof deliberately specifies the algebraic input. In positive characteristic locally free differentials do not imply smoothness. For example $\mu_p$ in characteristic $p$ has coordinate ring

$$
\begin{gathered}
k[z,z^{-1}]/(z^p-1)=k[u]/(u^p),\\
u=z-1.
\end{gathered} \tag{4.3}
$$

Its sheaf of differentials is freely generated by $du$ because $d(u^p)=0$, yet its underlying scheme is nonreduced and zero-dimensional. Its tangent space at the identity has dimension one. This is exactly the phenomenon that the characteristic-zero criterion excludes.

## 5. The identity component and the dimension bound

Let $P^0$ be the connected component containing the identity, with its canonical group-scheme structure. We use Group schemes over a field, Theorem 2.3: for a group scheme locally of finite type over a field, the identity component is a closed, quasi-compact, geometrically irreducible subgroup scheme. In particular it is of finite type. It is also open here. Indeed a locally Noetherian scheme is locally connected: each Noetherian open has finitely many connected components, which are open. A connected neighbourhood of the identity lies in its connected component, and the same reasoning at every point makes that component open.

Hence $P^0$ is open and closed in $P$. Its formation commutes with field extension: its base change is geometrically connected and open and closed, contains the identity, and therefore is precisely the identity component after base change. This is also the assertion of Kleiman, Proposition 5.3.

The superscript $0$ retains the whole scheme structure. It does not mean the reduction $(P^0)_{\mathrm{red}}$. Over a perfect field the reduction of a finite-type group scheme is a smooth subgroup scheme, by Group schemes over a field, Proposition 4.1 and Lie algebras and smoothness of group schemes, Theorem 5.1: products of reduced schemes remain reduced, so multiplication restricts to the reduction, and generic smoothness followed by translations makes that reduced group smooth. Over an imperfect field, neither this product argument nor this smoothness assertion is automatic. Our dimension and tangent arguments use $P^0$, with its possible nilpotents, over every field.

**Theorem 5.1.** Under (1.1),

$$
\dim P^0\leq h^1(X,\mathcal O_X), \tag{5.1}
$$

and equality holds if and only if $P^0$ is smooth over $k$. Equivalently, equality holds if and only if $P$ is smooth.

**Proof.** Both sides of (5.1) are unchanged by extension to $\bar k$. Work over that field and let $R$ be the local ring at the identity. Its embedding dimension is $t=h^1(X,\mathcal O_X)$ by Proposition 2.1. The dimension of $R$ is the dimension $d$ of $P^0$: that component is irreducible of finite type, and a closed point on an irreducible finite-type scheme over a field has local dimension equal to its global dimension.

For completeness, the local algebra inequality can be seen directly. Lift a basis of $\mathfrak m_R/\mathfrak m_R^2$ to $t$ elements of $R$. They give a surjective map

$$
\begin{gathered}
\bar k[[x_1,\ldots,x_t]]\longrightarrow \widehat R,\\
\widehat R=\bar k[[x_1,\ldots,x_t]]/I,\\
I\subset(x_1,\ldots,x_t)^2.
\end{gathered} \tag{5.2}
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

Theorem 6.2 below proves finite generation for every proper scheme. Theorems 6.3–6.4 prove uniform rank and torsion-order bounds in proper Noetherian families.

There is an arithmetic distinction when $k$ is not algebraically closed. Actual line-bundle classes inject into $P(k)$, including without (1.1) by the argument below. Define

$$
\begin{gathered}
\operatorname{Pic}^0(X)=\operatorname{Pic}(X)\cap P^0(k),\\
\operatorname{NS}_{\mathrm{arith}}(X)=\operatorname{Pic}(X)/\operatorname{Pic}^0(X).
\end{gathered} \tag{6.3}
$$

To verify injectivity in this generality, suppose an actual $L$ becomes trivial over $\bar k$. Set $C=H^0(X,\mathcal O_X)$ and $M=H^0(X,L)$, both finite over $k$. Flat field base change gives $M\otimes_k\bar k\simeq C\otimes_k\bar k$ as modules over $C\otimes_k\bar k$. Faithfully flat descent makes $M$ an invertible $C$-module. The finite Artinian ring $C$ is semilocal, so $M$ is free of rank one. Its evaluation $M\otimes_C\mathcal O_X\to L$ is an isomorphism after field extension and hence before extension. Thus $L$ was trivial. Over $\bar k$ the Picard sheaf classes have actual representatives and equality is equality of bundles: every fppf-local equality over this algebraically closed field can be pulled back along a $\bar k$-point of a nonempty finite-type covering member. This proves the injection into $P(\bar k)$ and therefore into $P(k)$. Formation of $P^0$ commutes with field extension. It follows that (6.3) injects into (6.2). Thus the arithmetic group is finitely generated as a subgroup of a finitely generated abelian group, but it need not equal the geometric group. A real conic has only even degrees of actual real line bundles, while its geometric Néron–Severi group is $\mathbb Z$.

The numerical boundedness theorem in Section 7 and finite-coefficient étale cohomology give a proof of the theorem of the base. The argument applies to every proper scheme, without a smoothness or projectivity assumption.

**Theorem 6.2 (the theorem of the base).** For every proper scheme $X$ over an algebraically closed field, $\operatorname{NS}(X)$ is a finitely generated abelian group.

**Proof.** Fix a prime $\ell\ne\operatorname{char}k$. We first record the cohomological facts and their exact scope. For our proper $X$,

$$
\begin{gathered}
V_\ell(X)=\varprojlim_n H^2_{\mathrm{et}}(X,\mu_{\ell^n}),\\
H^2_\ell(X,1)=V_\ell(X)\otimes_{\mathbb Z_\ell}\mathbb Q_\ell,\\
b_2(X)=\dim_{\mathbb Q_\ell}H^2_\ell(X,1)<\infty.
\end{gathered} \tag{6.4}
$$

The compact-support version of ℓ-adic sheaves and their cohomology, Proposition 5.2 and Theorems 6.1, 7.2 proves this by recovering a finite free $\mathbb Z_\ell$-complex from its finite-level perfect complexes. Its needed torsion finiteness for a proper scheme is Cohomology with compact support, Theorem 12.3 and Corollary 12.4: compact and ordinary cohomology agree for proper $X$. The compatible finite complexes and their inverse-limit cohomology are proved in Section 6 of the ℓ-adic lesson. These statements allow nonreduced schemes and every dimension. For a smooth connected proper curve $C$, The multiplicative group on a curve, Theorem 6.2 gives the canonical identifications

$$
\begin{gathered}
H^2_{\mathrm{et}}(C,\mu_{\ell^n})=\mathbb Z/\ell^n,\\
c_1^{(\ell^n)}(M)\longmapsto\deg(M)\pmod{\ell^n}.
\end{gathered} \tag{6.5}
$$

They commute with coefficient reduction, so their inverse limit is $\mathbb Z_\ell$ with the same degree normalization.

Here is the class map needed in the argument. On any scheme where $\ell$ is invertible, the Kummer sequence is étale exact: a unit has an $\ell^n$-th root on the finite étale cover defined by $T^{\ell^n}-u$, whose derivative is invertible. Its connecting map, using $H^1_{\mathrm{et}}(X,\mathbb G_m)=\operatorname{Pic}(X)$ from the Picard-functor lesson, is

$$
c_1^{(\ell^n)}:\operatorname{Pic}(X)
                  \longrightarrow H^2_{\mathrm{et}}(X,\mu_{\ell^n}).
$$

In the comparison from exponent $\ell^{n+1}$ to $\ell^n$, take $a\mapsto a^\ell$ on the first copy of $\mathbb G_m$ and the identity on the second. On the kernels this is $\mu_{\ell^{n+1}}\to\mu_{\ell^n}$, $a\mapsto a^\ell$. Thus the connecting maps are compatible and define $c_1(L)\in H^2_\ell(X,1)$. They are additive under tensor product and natural for every pullback. Equation (6.5) implies that pulling $c_1(L)$ to the normalization of a curve in $X$ gives its integer degree, viewed in $\mathbb Q_\ell$.

Let $N$ be the subgroup of numerically trivial line bundles and set

$$
A=\operatorname{Pic}(X)/N.
$$

The degree maps embed $A$ in the product of one copy of $\mathbb Z$ for each integral curve of $X$; in particular $A$ is torsion-free. Suppose $a_1,\ldots,a_m$ are $\mathbb Q$-linearly independent in $A\otimes\mathbb Q$, with representatives $L_1,\ldots,L_m$. The curve-degree functionals separate their $m$-dimensional span. Indeed a nonzero rational vector can be multiplied by a positive integer to give a nonzero class of $A$, and that class has nonzero degree on some curve. Finite-dimensional linear algebra therefore selects curves $C_1,\ldots,C_m$ such that the integer matrix

$$
B_{ij}=\deg(L_j|_{\widetilde C_i})
\tag{6.6}
$$

has nonzero determinant. Pullback to the normalized curves, followed by (6.5), sends the classes $c_1(L_j)$ to the columns of $B$. Its determinant is also nonzero in $\mathbb Q_\ell$. Hence those classes are linearly independent and $m\leq b_2(X)$. This bounds the rank of $A$ by $b_2(X)$.

We now use the integer degree maps to prove finite generation. Let $r$ be this finite rank. Their extensions to $A\otimes\mathbb Q$ separate points, so choose $r$ of them forming a basis of its dual. They induce an injection

$$
A\hookrightarrow\mathbb Z^r. \tag{6.7}
$$

For $r=0$ this says $A=0$. A subgroup of $\mathbb Z^r$ is finitely generated: induct on $r$, project to the last coordinate, whose image is cyclic, and apply induction to the kernel in $\mathbb Z^{r-1}$; one lift of a generator of the image completes the generating set. This integer-lattice argument supplies finite generation, beyond the rank bound.

By Theorem 7.6, $N=P^\tau(k)$ and $P^\tau/P^0$ is finite étale. Its finite group of geometric points is $T=N/P^0(k)$. Thus

$$
0\longrightarrow T\longrightarrow\operatorname{NS}(X)
       \longrightarrow A\longrightarrow0. \tag{6.8}
$$

Lifts of finitely many generators of $A$, together with the finite group $T$, generate $\operatorname{NS}(X)$. Since $A$ is torsion-free and $T$ is finite, $T$ is exactly its torsion subgroup as well. $\square$

**Theorem 6.3 (uniform ranks in a proper family).** Let $f:X\to S$ be proper, with $S$ Noetherian. There is one integer bounding the ranks of $\operatorname{NS}(X_{\bar s})$ for all geometric fibres. Flatness of $f$ is not required.

**Proof.** On the open $S_\ell$ where a prime $\ell$ is invertible, Cohomology with compact support, Theorem 12.3 makes

$$
R^2 f_*\mathbb F_\ell=R^2 f_!\mathbb F_\ell
$$

a constructible sheaf of finite $\mathbb F_\ell$-modules. Properness gives the equality of the two operations. Finite presentation holds because $S$ is Noetherian and $f$ is of finite type. By the geometric fibre formula, Corollary 9.2, its geometric stalk is $H^2(X_{\bar s},\mathbb F_\ell)$. A finite constructible stratification of the Noetherian $S_\ell$ bounds all these dimensions by a single $b_\ell$.

The ordinary, or equivalently proper compact-support, universal-coefficient sequence in ℓ-adic sheaves and their cohomology, Theorem 7.3 injects

$$
H^2(X_{\bar s},\mathbb Z_\ell)/\ell
           \hookrightarrow H^2(X_{\bar s},\mathbb F_\ell).
$$

The finite $\mathbb Z_\ell$-module on the left before reduction has rank $b_2(X_{\bar s})$; choosing a compatible sequence of roots of unity over the algebraically closed residue field identifies the twisted and untwisted ranks. Thus

$$
\begin{gathered}
\operatorname{rank}\operatorname{NS}(X_{\bar s})
  \leq b_2(X_{\bar s})\\
  \leq \dim_{\mathbb F_\ell}H^2(X_{\bar s},\mathbb F_\ell)
  \leq b_\ell.
\end{gathered} \tag{6.9}
$$

The first inequality is the proof of Theorem 6.2, since (6.8) has finite kernel. The two opens $S_2$ and $S_3$ cover $S$, because $2$ and $3$ generate the unit ideal. Taking the maximum of their two bounds proves the assertion in every residue characteristic. $\square$

**Theorem 6.4 (uniform Néron–Severi bounds).** Let $f:X\to S$ be proper with $S$ Noetherian. The geometric-fibre Néron–Severi groups are finitely generated, and one integer bounds both their ranks and the orders of their torsion subgroups. Flatness, projectivity, reduced fibres and a universal equality $f_*\mathcal O_X=\mathcal O_S$ are not required.

**Proof.** Finite generation is Theorem 6.2 on each geometric fibre, and uniform ranks are Theorem 6.3. For torsion, take the finite-type $S$-scheme $T$ and the line bundle on $X_T$ supplied by relative numerical boundedness, Theorem 7.9 below. For every geometric $\bar s$, this family induces a morphism

$$
T_{\bar s}\longrightarrow\operatorname{Pic}_{X_{\bar s}/\bar s}.
$$

Theorem 7.6 identifies the numerical classes with $P^\tau_{\bar s}(\bar s)$, and our parameter contains every one of them. Each connected component of $T_{\bar s}$ maps into a single Picard component. Consequently

$$
\begin{aligned}
\#\operatorname{NS}(X_{\bar s})_{\mathrm{tors}}
 &\leq\#\pi_0(T_{\bar s})\\
 &\leq\#\operatorname{Irr}(T_{\bar s}).
\end{aligned} \tag{6.10}
$$

Here $\operatorname{Irr}$ denotes the set of irreducible components. For a finite-type map to a Noetherian scheme, the geometric irreducible-component counts have a finite common bound. The exact proof is the generic-count argument in Moduli stacks are algebraic, the finite-arithmetic-model lemma: on each integral closed base, split the finitely many generic components after a finite separable extension; their closures cover after shrinking, their pairwise intersections remain nowhere dense, and their fibres remain geometrically irreducible. The count is then constant on a nonempty open. Noetherian induction gives a finite partition and hence a bound. This applies to $T\to S$, including its nonproper parameter strata. Combine the resulting bound in (6.10) with the rank bound and $1$. $\square$

The historical uniform theorem is [AI Integrated Stacks Project, moduli.tex, theorem-picard-neron-severi-uniform-bounds](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/moduli.html#moduli-theorem-picard-neron-severi-uniform-bounds), with quotient by $P^0$, item (vi) of Grothendieck's [complement to FGA, Exposé 236](https://www.numdam.org/item/SB_1961-1962__7__303_1/), and Kleiman, *The Picard scheme*, Corollary 6.17 and Remark 6.19, on the 1971 finiteness theorem. The proof above obtains torsion bounds from families of actual line bundles on a finite-type parameter, using the relative construction in Section 7.

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

**Proof.** Theorem 7.6 below gives a finite-type family containing every numerically trivial line bundle on $X_{\bar k}$ and identifies their classes with $P^\tau(\bar k)$. That family meets only finitely many Picard components. Every such component is a translate of the finite-type $P^0_{\bar k}$, so their union is of finite type. The quotient (7.2) is their finite étale component group. Both assertions descend to $k$. This proof does not use Néron–Severi finite generation. ∎

The quotient in (7.2) can be étale even when $P^\tau$ itself is nonreduced. Nilpotents within the identity component disappear in the component quotient. Nor should $P^\tau$ be described as the set of torsion line bundles: a nontorsion bundle in $P^0$ belongs to $P^\tau$ because its component class is zero.

For numerical equivalence, work geometrically. An invertible sheaf $L$ on a proper $X/\bar k$ is numerically trivial if

$$
\begin{gathered}
\deg(\nu^*L)=0\\
\text{for every integral curve }C\subset X.
\end{gathered} \tag{7.3}
$$

where $\nu:\widetilde C\to C\hookrightarrow X$ is its normalization. Degrees can also be defined by Euler characteristics on $C$; the zero-degree condition is unchanged by normalization.

Algebraic triviality implies numerical triviality. Restrict a connected family of invertible sheaves to $C\times T$. This is a flat coherent family on a proper curve over $T$. Its Euler characteristic is locally constant in $T$, by cohomology and base change. The degree, which is its Euler characteristic minus $\chi(\mathcal O_C)$, is therefore constant on connected $T$. A family joining $L$ to $\mathcal O_X$ forces degree zero on every $C$. Chains give the same conclusion.

If $L^{\otimes n}$ is algebraically trivial, then $n\deg(\nu^*L)=0$; the integer degree is consequently zero. Thus belonging to $P^\tau(\bar k)$ implies numerical triviality.

The full proper-scheme numerical theorem states that, for every proper $X$ over an algebraically closed field,

$$
\begin{gathered}
L\text{ is numerically trivial}\\
\Longleftrightarrow\\
\text{there is }n\geq1\text{ such that}\\
L^{\otimes n}\text{ is algebraically trivial}.
\end{gathered} \tag{7.4}
$$

The historical statements are [AI Integrated Stacks Project, moduli.tex, [theorem-picard-tau-numerical-criteria](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/moduli.html#moduli-theorem-picard-tau-numerical-criteria)] and item (viii) of Grothendieck's complement to FGA, Exposé 236. For projective $X$, Kleiman, *The Picard scheme*, Theorem 6.3 gives the equivalent numerical, boundedness, and Euler-characteristic formulations; Remark 6.14 discusses proper $X$. Theorem 7.2 proves the projective case, and Lemmas 7.3–7.5 and Theorem 7.6 prove the full proper-scheme assertion by projective modification, conductor gluing, and nilpotent lifting. Neither proof assumes the theorem of the base.

Equation (7.4) concerns the whole numerical subgroup. It does not make every numerically trivial bundle algebraically trivial. Enriques surfaces provide the simplest counterexample below.

### Numerical classes on an arbitrary projective scheme

We prove the numerical converse for every projective scheme, including reducible schemes, nilpotents and embedded points. The regularity argument must apply to line bundles themselves; they have not yet been placed in a bounded quotient family.

**Theorem 7.2.** Let $X\subset\mathbb P^n_k$ be projective over an algebraically closed field. For a line bundle $L$ on $X$, the following are equivalent:

1. $L$ has degree zero on every integral curve in $X$.
2. A positive tensor power of $L$ is algebraically trivial.
3. The collection $\{L^{\otimes p}:p\in\mathbb Z\}$ is bounded by a finite-type family of line bundles.
4. $\chi(F\otimes L)=\chi(F)$ for every coherent $F$ on $X$.

Here bounded means that all the listed $k$-line bundles occur at $k$-points of a finite-type parameter scheme carrying one line bundle on its product with $X$.

Moreover, there is one integer $M$, depending on the fixed embedded scheme $X$, such that every numerically trivial line bundle is $M$-regular and has Hilbert polynomial $P_X$. All such bundles belong to one finite-type family. Consequently $P^\tau$ is of finite type and $P^\tau/P^0$ is finite étale for projective $X$, without using Néron–Severi finite generation.

**Proof.** Empty schemes cause no difficulty. We allow arbitrary global-function algebras here, dropping (1.1).

First extend (6.1) to this generality. In the finite-frame construction of Theorem 1.2, $K=U(D)/U(C)$ is connected over our algebraically closed field. Indeed the unit group of any finite $k$-algebra is, as a variety, a product of multiplicative groups and an affine space: split the algebra into its local Artinian factors and write a unit as its nonzero residue plus a nilpotent element. Thus $U(D)$ is connected, and so is its quotient $K$.

The $K$-torsor $R_Z\to P$ is smooth with connected geometric fibres. Its inverse image over the finite-type connected group $P^0$ is consequently connected and of finite type. To justify connectedness, two disjoint open-and-closed pieces upstairs would have disjoint open images downstairs: a connected fibre cannot meet both. Those images would disconnect $P^0$. Choose a finite-type étale scheme atlas of this algebraic space. The graph of its connected components, joining two when their images meet, is connected by the same open-image argument. On an overlap, a closed $k$-point identifies the two fibres of the universal framed line bundle. Its restrictions to the connected atlas components therefore give chains of algebraic equivalences joining any two classes in $P^0(k)$. This proves that classes in $P^0(k)$ are algebraically trivial even without (1.1). The converse still follows from a connected family's map to $P$.

For a zero-dimensional projective scheme, its finite Artinian coordinate algebra has trivial Picard group, higher cohomology vanishes, and tensoring by a line bundle preserves every coherent length. Its Picard sheaf is trivial by taking $Z=X$ in the finite-frame construction. Thus all assertions hold. Assume henceforth that positive-dimensional supports occur.

**A bound for sections before boundedness.** For every fixed coherent $F$ on a projective scheme of dimension at most $r$, there is an integer $C_F$ such that

$$
\begin{gathered}
h^0(F\otimes N(t))\leq C_F\binom{t+r}{r},\\
t\geq0.
\end{gathered} \tag{7.5}
$$

for every numerically trivial line bundle $N$. We prove this by induction on $r$.

A finite graded prime filtration of a graded module defining $F$ gives sheaf factors $\mathcal O_Y(a)$ with $Y$ integral. One obtains such a filtration by taking a homogeneous element whose annihilator is an associated prime, inserting its cyclic module, and repeating on the quotient; the ascending chain condition makes the process finite. Factors supported at the irrelevant ideal sheafify to zero. Tensoring by $N$ preserves the filtration. The cohomology exact sequence bounds $h^0$ of an extension by the sum for its two ends, so it suffices to handle each factor. Numerical triviality restricts to $Y$.

Let $Y$ be integral of dimension $d\geq1$. First,

$$
H^0(Y,N(-1))=0. \tag{7.6}
$$

Here is a degree argument requiring only Hilbert polynomials and curve degrees. Cut $Y$ by $d-1$ hyperplanes, at each step avoiding the finitely many associated points. The final scheme $T$ is a projective curve. Its coherent prime filtration shows

$$
\begin{aligned}
&\chi(N_T(t))-\chi(\mathcal O_T(t))\\
&\quad=\sum_i m_i\deg(N|_{C_i})=0.
\end{aligned}
$$

The $C_i$ are its integral curve components with their generic multiplicities. Zero-dimensional filtration factors contribute zero to this difference; twisting a curve factor changes both degrees equally. The hyperplane exact sequences therefore say that the $(d-1)$st finite difference of $P_N-P_{\mathcal O_Y}$ is zero. Its degree is at most $d-2$. Since $P_{\mathcal O_Y}$ has leading term $\deg(Y)t^d/d!$, the coefficient of degree $d-1$ in

$$
P_N(t-1)-P_{\mathcal O_Y}(t)
$$

is $-\deg(Y)/(d-1)!$. A nonzero section of $N(-1)$ would inject $\mathcal O_Y$ into $N(-1)$. Its cokernel is supported in dimension at most $d-1$ and has a nonnegative coefficient in that degree, contradicting the displayed negative coefficient. This proves (7.6), including $d=1$.

Fix one hyperplane section $H$ of $Y$. By induction, the restrictions $N_H$ satisfy (7.5) in dimension $d-1$, with a constant $C_H$ independent of $N$. The sequences

$$
0\longrightarrow N(t-1)\longrightarrow N(t)
\longrightarrow N_H(t)\longrightarrow0
$$

and (7.6) give, by summing from $0$ to $t$,

$$
\begin{aligned}
h^0(Y,N(t))&\leq C_H\sum_{j=0}^t\binom{j+d-1}{d-1}\\
&=C_H\binom{t+d}{d}.
\end{aligned}
$$

For the factor $\mathcal O_Y(a)$, a negative $a$ only decreases this bound: multiply by a nonzero section of $\mathcal O_Y(-a)$ to inject into the untwisted sheaf. For $a\geq0$, use

$$
\binom{t+a+d}{d}
\leq\binom{a+d}{d}\binom{t+d}{d}.
$$

The inequality follows by multiplying degree-$a$ and degree-$t$ monomials; their products span all degree-$a+t$ monomials. Summing the finitely many factor bounds proves (7.5). This also proves the statement in the presence of nilpotent and embedded components.

**Euler characteristics and regularity.** We prove together, by induction on $\dim X$, that every numerically trivial $N$ has polynomial $P_X$ and that one regularity bound works for all of them. The dimension-zero case was handled above.

Fix $N$. Choose $q\geq1$ for which both $\mathcal O_X(q)$ and $N(q)$ are very ample. In each system choose a section avoiding all associated points of $X$. They give effective Cartier divisors $F,G$ with associated bundles $\mathcal O_X(q),N(q)$. Both have dimension smaller than $X$. For every integer $p$, their two divisor sequences, tensored by $N^{\otimes p}(t+q)$, give

$$
\begin{gathered}
0\longrightarrow N^{\otimes p}(t)
\longrightarrow N^{\otimes p}(t+q)\\
\longrightarrow N_F^{\otimes p}(t+q)\longrightarrow0,\\[4pt]
0\longrightarrow N^{\otimes(p-1)}(t)
\longrightarrow N^{\otimes p}(t+q)\\
\longrightarrow N_G^{\otimes p}(t+q)\longrightarrow0.
\end{gathered}
$$

The restrictions remain numerically trivial. Induction identifies the two right-hand Euler characteristics with those of $\mathcal O_F(t+q),\mathcal O_G(t+q)$, respectively. Subtracting shows that

$$
\chi(N^{\otimes p}(t))
=pA(t)+P_X(t), \tag{7.7}
$$

where $A$ is a polynomial independent of $p$.

The induction hypothesis also gives one regularity bound for all powers $N_F^{\otimes p}$. For every sufficiently large $t$, the adjacent positive cohomology groups on $F$ vanish, uniformly in $p$. The first divisor sequence then identifies $H^i(N^{\otimes p}(t))$ with $H^i(N^{\otimes p}(t+q))$ for $i\geq2$. Serre vanishing for each fixed $p$, iterated backwards, makes these groups zero, still at one threshold independent of $p$. Hence

$$
h^0(N^{\otimes p}(t))
\geq\chi(N^{\otimes p}(t))
=pA(t)+P_X(t)
$$

above that threshold. But (7.5), applied to all the numerically trivial powers, bounds the left side independently of $p$. Letting $p$ tend to positive or negative infinity forces $A(t)=0$. This holds for infinitely many $t$, so $A=0$. In particular

$$
P_N=P_X. \tag{7.8}
$$

We now make regularity uniform over all numerically trivial $N$, without choosing a presentation depending on $N$. Fix a hyperplane $H$ avoiding the associated points of $X$. All its restrictions $N_H$ have a common nonnegative regularity bound $m_H$ by induction. Their positive cohomology vanishes for twists at least $m_H$. The hyperplane sequence and Serre vanishing then give

$$
H^i(N(t))=0\qquad(i\geq2,\ t\geq m_H).
$$

Put $b_t=h^1(N(t))$. For $t\geq m_H$ the sequence ends in

$$
\begin{gathered}
H^0(N(t))\xrightarrow{\rho_t}H^0(N_H(t))\\
\longrightarrow H^1(N(t-1))\longrightarrow H^1(N(t))\longrightarrow0.
\end{gathered}
$$

Thus $b_{t-1}\geq b_t$, with equality exactly when $\rho_t$ is onto. Surjectivity at one such twist propagates to all higher twists by Regularity and bounded families, Lemma 2.2. Equality would therefore give a constant tail, necessarily zero by Serre vanishing. Every positive preceding value strictly decreases at the next step.

Take $m_0=\max(0,m_H+n)$. Equations (7.5) and (7.8), and the higher vanishing, give the uniform budget

$$
\begin{gathered}
b_{m_0}=h^0(N(m_0))-P_X(m_0)\leq B,\\
V=C_{\mathcal O_X}\binom{m_0+\dim X}{\dim X}-P_X(m_0),\\
B=\max(0,\lceil V\rceil).
\end{gathered}
$$

At most $B$ strict decreases give $b_{m_0+B}=0$. With

$$
M=m_0+B+1,
$$

we have $H^1(N(M-1))=0$ and, for $2\leq i\leq n$, also $M-i\geq m_H$, so $H^i(N(M-i))=0$. Thus every $N$ is $M$-regular. This completes both induction assertions. The bound depends on the fixed $X$; no assertion of a bound for all proper families has been used.

**A finite-type family.** Let $a=P_X(M)$. Regularity makes $N(M)$ globally generated with $a$ sections and no higher cohomology. Every numerically trivial $N$ is consequently a quotient of the one fixed sheaf

$$
E=\mathcal O_X(-M)^{\oplus a}.
$$

The projective Quot theorem of the preceding lesson makes $Q=\operatorname{Quot}^{P_X}_{E/X/k}$ a projective scheme. Let $U\subset Q$ be the open subset on which the universal quotient is a line bundle on all of $X_U$. This is open because the complement of the rank-one locally free locus is closed in $X_Q$ and its proper image in $Q$ is closed. A point with line-bundle fibre belongs to $U$: lift a fibre generator locally, use Nakayama for surjectivity, and use base-flatness of both the structure sheaf and the quotient to make the kernel have zero fibre; Nakayama then kills that kernel too. Thus $U$ contains a representative of every numerically trivial bundle and is of finite type. This establishes boundedness of the entire numerical collection.

Every power of $L$ is numerically trivial when $L$ is, so condition 1 implies 3. Conversely, if the powers occur in one finite-type family, two distinct powers occur in the same connected component of its parameter scheme. Their difference is algebraically trivial. Changing the sign of the difference if necessary gives the positive power in condition 2. The implication 2 to 1 was proved above by restriction to curves and constancy of degree.

Finally a coherent prime filtration of any $F$ again has factors $\mathcal O_Y(a)$ for integral projective $Y\subset X$. Equation (7.8), applied on every such $Y$, says that tensoring each factor by a numerically trivial $L$ preserves its Euler characteristic. Additivity proves condition 4. Taking $F=\mathcal O_C$ in condition 4 recovers degree zero on every integral curve, proving 4 to 1.

The same finite-type $U$ maps to the Picard scheme and covers all points of $P^\tau(k)$ by the equivalence just proved. Its finitely many connected components meet only finitely many Picard components. Every component of $P^\tau$ is a translate of the finite-type $P^0$ and has a $k$-point. Hence only finitely many occur. Their union $P^\tau$ is of finite type, and its component quotient is finite étale. The corresponding assertion for a projective scheme over any field follows by algebraic-closure base change and faithful-flat descent. $\square$

Kleiman, *The Picard scheme*, Section 6, Theorem 6.3 and its regularity lemmas, provide the historical comparison. The proof here supplies the regularity budget and the finite-type family explicitly; it does not infer boundedness merely from a fixed Hilbert polynomial or assume Néron–Severi finite generation.

### Numerical classes on an arbitrary proper scheme

Projective modifications need not be flat. We therefore first establish three statements about actual families of line bundles. Throughout this subsection, $k$ is algebraically closed, all schemes called proper are proper over $k$, and bounded has the meaning given before Theorem 7.2. A finite union of bounded collections is bounded, by taking the disjoint union of their parameter schemes.

**Lemma 7.3 (recovering a bounded family from its pullback).** Let $g:Y\to Z$ be a morphism of proper schemes such that $g_*\mathcal O_Y=\mathcal O_Z$. If the pullbacks of a collection of line bundles on $Z$ are bounded on $Y$, then the original collection is bounded on $Z$.

**Proof.** Let $M$ on $Y\times T$, with $T$ of finite type, contain the pullbacks. Replacing $T$ by $T_{\mathrm{red}}$ preserves all its $k$-point fibres. We will partition this reduced scheme into finitely many reduced, locally closed strata on which

$$
R^qg_{T,*}M
$$

is flat over the stratum and commutes with arbitrary base change on that stratum, for every $q$.

Here are the details of this assertion. The sheaves are coherent by proper coherence, Theorem 4.1. Only finitely many $q$ occur: take a finite affine cover of $Z$ and, above each member, a finite affine cover of its inverse image in $Y$. Separatedness makes their intersections affine. These fixed covers bound the lengths of the Čech complexes, also after product with $T$.

Over an integral affine open of $T$, generic freeness, Lemma 5.1 and Corollary 5.2, applied to these finitely many coherent sheaves on a finite affine cover of $Z\times T$, makes them all flat over a dense open of $T$. On that open, the affine Čech complexes just described have flat terms over the base ring: a line bundle on an affine product is a finite projective module over its coordinate algebra, which is flat over the parameter ring. Their cohomology modules are flat as well. For a bounded complex of flat modules with flat cohomology, tensoring with any module commutes with cohomology. To check this, start at the last term. Its quotient by the last boundaries is flat; hence those boundaries are flat. The two exact sequences involving cycles, boundaries and cohomology give flatness successively in each lower degree, and remain exact after tensoring. This proves the asserted base-change isomorphisms, without assuming $g$ flat.

Do this on a dense open in each irreducible component of $T$, first removing their intersections, and repeat on the reduced closed complement. Dimension drops at each repetition, so finitely many strata suffice. Recompute the direct images on each new stratum before applying generic freeness there. Replace $T$ by the finite disjoint union of these strata.

Put $F=g_{T,*}M$. It is now coherent, flat over $T$, and its fibre at $t$ is $g_*M_t$. If $M_t\simeq g^*L$, the projection formula for the invertible sheaf $L$ gives

$$
F_t\simeq L\otimes g_*\mathcal O_Y\simeq L.
$$

The adjunction $g_T^*F\to M$ on this fibre is the usual isomorphism $g^*L\to g^*L$.

There is an open neighbourhood of every such $t$ on which $F$ is a line bundle on all of $Z\times T$. Indeed, at any point of its fibre, lift a generator of $F_t$. Nakayama gives a surjection from the local structure ring onto $F$; flatness over $T$ makes the kernel have zero fibre, since the structure ring is also flat over $T$. A second application of Nakayama kills the kernel. Thus $F$ is locally free of rank one at every point of that fibre. Its rank-one locally free locus is open. The complement has closed image in $T$ by properness of $Z$, so removing that image gives the claimed neighbourhood.

On this open, adjunction is a map of line bundles. Its nonisomorphism locus is closed in $Y\times T$, being the zero locus of the corresponding local multiplier. Its image in $T$ is closed by properness of $Y$. Remove this image too. The resulting open parameter schemes still contain every $t$ whose bundle is a pullback, and carry the line bundles $F$ whose fibres are the original $L$. They are of finite type. $\square$

**Lemma 7.4 (finite gluing).** Let $X$ be proper and let $\alpha:Z\to X$ be finite, with an injection $\mathcal O_X\hookrightarrow\alpha_*\mathcal O_Z$. Suppose $\alpha$ is an isomorphism on an open meeting every irreducible component of $X$. Let

$$
\begin{gathered}
I=\operatorname{Ann}_{\mathcal O_X}
       (\alpha_*\mathcal O_Z/\mathcal O_X),\\
D=V(I),\qquad D'=Z\times_XD.
\end{gathered}
$$

If a collection of line bundles on $X$ has bounded restrictions both to $Z$ and to $D$, it is bounded on $X$.

**Proof.** On an affine open write $A\subset B$ for the finite ring extension. The conductor $I=\{a\in A:aB\subset A\}$ is an ideal of both rings. There is an exact fibre-product identity

$$
A=B\times_{B/I}A/I. \tag{7.9}
$$

Indeed, an element of $B$ whose residue lies in $A/I$ differs from an element of $A$ by an element of $I\subset A$. Tensoring the associated exact sequence of $k$-vector spaces with any $k$-algebra preserves this identity on parameter products.

A line bundle on $X$ is equivalent to a line bundle on $Z$, a line bundle on $D$, and an isomorphism between their restrictions to $D'$. We verify the local assertion needed for this gluing. Given invertible modules on $B$ and $A/I$ and their isomorphism over $B/I$, take their module fibre product. At a prime outside $D$, (7.9) reduces to $A=B$. At a prime $\mathfrak p$ in $D$, the finite algebra $B_{\mathfrak p}$ is semilocal, so its invertible module is free: choose a generator modulo its finitely many maximal ideals by the Chinese remainder theorem, and apply Nakayama. The module over the local ring $(A/I)_{\mathfrak p}$ is free too. In these frames the gluing is multiplication by a unit of $B_{\mathfrak p}/I_{\mathfrak p}$. Since $I_{\mathfrak p}$ lies in every maximal ideal of $B_{\mathfrak p}$, that unit lifts to a unit of $B_{\mathfrak p}$. Adjusting the first frame identifies the fibre product with $A_{\mathfrak p}$. The module fibre product is finite over the Noetherian ring $A$ and hence is a line bundle. Its restrictions recover the two given modules. These constructions are inverse, including on morphisms, and agree on overlaps. The same proof applies on every finite-type parameter product by the base-change assertion following (7.9).

Choose finite-type parameter schemes $T_1,T_2$ for the two collections of restrictions. On $D'\times(T_1\times T_2)$ their two universal line bundles are finitely presented, flat over the parameter scheme, and have proper support. Their isomorphisms are therefore represented by an affine scheme $H$ of finite presentation over $T_1\times T_2$, by Moduli stacks are algebraic, Corollary 1.3. Its universal isomorphism glues the universal bundles to one on $X\times H$. Every original line bundle appears at a $k$-point of $H$, because its two chosen representatives come with their gluing isomorphism. Thus this is a bounded collection. $\square$

**Lemma 7.5 (nilpotent thickenings).** Let $X_0\hookrightarrow X$ be a nilpotent closed immersion of proper schemes. The collection of all line bundles on $X$ restricting to a bounded collection on $X_0$ is bounded.

**Proof.** First suppose the ideal $I$ is square-zero. It is a coherent $\mathcal O_{X_0}$-module. Cover a parameter scheme for the given collection by finitely many affine opens, and consider its universal line bundle $M$ over one $T=\operatorname{Spec}A$. The exact sequence of abelian sheaves

$$
0\longrightarrow I_T\xrightarrow{a\mapsto1+a}
\mathcal O_{X_T}^{\times}\longrightarrow
\mathcal O_{X_{0,T}}^{\times}\longrightarrow1
$$

gives a lifting obstruction

$$
\begin{gathered}
\delta(M)\in H^2(X_{0,T},I_T),\\
H^q(X_{0,T},I_T)=H^q(X_0,I)\otimes_k A.
\end{gathered} \tag{7.10}
$$

The equality is computed by a finite separated affine Čech cover and holds for every $A$, since tensoring over $k$ is exact. Each vector space $H^q(X_0,I)$ is finite-dimensional by proper cohomological finiteness, Corollary 5.1. In a basis of $H^2(X_0,I)$, the obstruction has finitely many coefficients in $A$. Their vanishing defines a closed subscheme $T_0\subset T$. Formation of (7.10) commutes with every parameter base change, so all points whose bundle lifts lie in $T_0$. The obstruction of $M|_{T_0}$ itself is zero. The cohomology exact sequence consequently supplies a line bundle $\widetilde M$ on $X\times T_0$ restricting to it.

All lifts are parameterized as follows. The same exact sequence says that

$$
\ker\bigl(\operatorname{Pic}(X)\to
                 \operatorname{Pic}(X_0)\bigr)
$$

is the image of $H^1(X_0,I)$. Put $h=\dim_k H^1(X_0,I)$ and choose Čech cocycles $c^1_{ij},\ldots,c^h_{ij}$ representing a basis on a finite affine cover. On $X\times\mathbb A^h$ the transition functions

$$
1+\sum_{a=1}^h t_a c^a_{ij}
$$

define a line bundle: their cocycle equation is additive because $I^2=0$. Its $k$-point fibres cover that kernel; no injectivity of $H^1(X_0,I)$ into the Picard group is needed. Tensoring this bundle with $\widetilde M$ gives a family on $T_0\times\mathbb A^h$ containing every lift of every specified fibre. Taking the finite union over the affine cover of $T$ proves the square-zero case.

For a general nilpotent ideal $J$, use its finite filtration by powers. Each closed immersion from the subscheme defined by $J^m$ into the one defined by $J^{m+1}$ has square-zero ideal $J^m/J^{m+1}$, for $m\geq1$. Apply the square-zero case successively. $\square$

**Theorem 7.6 (proper numerical criterion).** For every proper scheme $X$ over an algebraically closed field, the collection of all numerically trivial line bundles on $X$ is bounded. For a line bundle $L$ on $X$, numerical triviality, algebraic triviality of some positive tensor power, and boundedness of $\{L^{\otimes p}:p\in\mathbb Z\}$ are equivalent. In particular (7.4) holds, $P^\tau$ is of finite type, and $P^\tau/P^0$ is finite étale. The last two assertions hold over every field. Nilpotents, reducible schemes, and extra global functions are allowed.

**Proof.** We prove boundedness by induction on $r=\dim X$, for all proper schemes of dimension at most $r$. A zero-dimensional proper scheme is the spectrum of a finite product of local Artinian $k$-algebras. Its line bundles are all trivial, so the assertion holds.

First take a reduced $X$ of dimension $r>0$. Apply the integral Chow construction, Lemma 4.0, to each irreducible component with its reduced structure. The finite disjoint union of the resulting integral projective schemes is a projective scheme $Y$, and the resulting proper map $h:Y\to X$ is an isomorphism on an open $U$ meeting every component: remove their intersections and shrink within each component's isomorphism open.

Proper coherence makes $B=h_*\mathcal O_Y$ a finite coherent $\mathcal O_X$-algebra. The natural map $\mathcal O_X\to B$ is injective. Indeed, a section in its kernel vanishes on $U$; since $X$ is reduced and $U$ meets every component, that section is zero. Set

$$
Z=\operatorname{Spec}_X B,\qquad
Y\xrightarrow{g}Z\xrightarrow{\alpha}X.
$$

The map $\alpha$ is finite and is an isomorphism on $U$. The induced map $g$ is proper: its graph is closed in $Y\times_XZ$ because $Z\to X$ is separated, and the projection to $Z$ is a base change of the proper $h$. Moreover $g_*\mathcal O_Y=\mathcal O_Z$. Applying the exact, faithful affine pushforward $\alpha_*$ to the unit map gives precisely the identity $B\to h_*\mathcal O_Y=B$. This proves the equality and supplies the factorization needed here directly.

Numerical triviality pulls back under every morphism of proper schemes. For an integral curve upstairs, its image is either a point, where the pulled-back bundle is trivial, or an integral curve. In the latter case the morphism between the normalized curves is finite of positive degree, and the pulled-back degree is that positive integer times the original degree. Thus, for the entire collection of numerically trivial $L$ on $X$, the bundles $h^*L$ on projective $Y$ are numerically trivial. They are bounded by Theorem 7.2. Lemma 7.3 applied to $g$ shows that the bundles $\alpha^*L$ are bounded on $Z$.

Let $D$ be the conductor subscheme of $\alpha$. It is proper and meets no generic point of $X$, so $\dim D<r$. It may be nonreduced, which is why our induction includes all scheme structures. Every $L|_D$ is numerically trivial and therefore belongs to a bounded family by induction. Lemma 7.4 now proves boundedness of all the original $L$ on reduced $X$.

For arbitrary $X$ of dimension $r$, the reduced case just proved applies to $X_{\mathrm{red}}$. Every integral curve in $X$ factors through that reduction. Hence a bundle on $X$ is numerically trivial exactly when its restriction to $X_{\mathrm{red}}$ is. Lemma 7.5 lifts the bounded family on the reduction to a bounded collection of all its possible line-bundle lifts on $X$. This completes the induction.

If $L$ is numerically trivial, all its powers lie in this finite-type family. Two distinct powers have representatives in the same connected component of its parameter scheme, because that scheme has only finitely many connected components. Their quotient, or its inverse, is a positive power of $L$ algebraically equivalent to the trivial bundle. Conversely such a power has degree zero on every curve by (7.3), so $L$ is numerically trivial. The same two-powers argument proves the equivalence with boundedness of its powers.

The finite-frame comparison of algebraic triviality with $P^0(k)$ at the beginning of Theorem 7.2 uses only properness, and therefore applies here without (1.1). Consequently the numerical collection is precisely $P^\tau(k)$. Its finite-type parameter scheme maps to $P$ and meets only finitely many of its open connected components. Every component of $P^\tau$ has a $k$-point and is a translate of the finite-type $P^0$. There are thus finitely many such components, proving finite type. Their quotient is the finite constant torsion subgroup of the étale component group, so it is finite étale. Base change of $P$ and $P^0$ to an algebraic closure identifies (7.1) there with its geometric definition. Finite type and finite étaleness descend faithfully flatly, proving the assertions over arbitrary fields. $\square$

The argument gives bounds for a fixed proper scheme and proves finiteness of its torsion component without assuming the theorem of the base. Uniform bounds as $X$ varies in a proper family, and finite generation of the whole Néron–Severi group, are separate assertions in Section 6.

### Numerical line bundles in proper families

For a proper $f:X\to S$ with $S$ Noetherian, call collections $\mathcal C_{\bar s}\subset\operatorname{Pic}(X_{\bar s})$ **bounded over $S$** if there are a finite-type $S$-scheme $T$ and a line bundle $M$ on $X\times_ST$ such that every member of every $\mathcal C_{\bar s}$ occurs at an $\Omega$-point of $T\times_S\operatorname{Spec}\Omega$, for every geometric point $\bar s:\operatorname{Spec}\Omega\to S$. The family may contain additional bundles. Finite unions of such families are represented by disjoint unions of parameters.

We will use Noetherian induction on the base. It is enough, over every integral closed subscheme of $S$, to obtain such a family on a nonempty open. The complement then has a family by induction, and its parameter morphism is still of finite type over $S$. Replacing the base by its reduction preserves its geometric fibres. A finite surjective change of base on a nonempty open is allowed too: each of its fibres over an algebraically closed field has a rational point, and composing its parameter scheme with that finite map gives the required family downstairs.

Here are the finite-presentation preparations used below. Over an integral affine base $\operatorname{Spec}A$ with fraction field $K$, any finite collection of coherent sheaves, maps, ideals, projective embeddings and finite filtrations on the geometric generic fibre is defined over a finite extension $K'/K$. Choose the finitely many coefficients on finite affine covers. Their field extension is finite because they lie in an algebraic closure. Clearing denominators in their monic algebraic equations makes their ring $A'\subset K'$ finite over a localization of $A$, with fraction field $K'$. Generic freeness makes $A'$ finite free of positive rank after another localization. Its spectrum is therefore a finite surjective cover. The equations for the maps, their relations and their gluing then spread after localizing $A'$. Coherent kernels, cokernels or ideal powers that vanish generically vanish after a further localization: on finitely many affine charts, one nonzero base element kills each finite list of generators. This proves exactness and the required identities after shrinking. Generic freeness of the finitely many quotients makes each of these exact sequences remain exact on every fibre.

When the generic closed schemes in these data are geometrically integral or geometrically reduced, all their remaining fibres can be made so. The complete generic geometric irreducibility and reducedness proofs are in Moduli stacks are algebraic, the finite-arithmetic-model lemma and the geometrically reduced model lemma. The former also proves splitting of generic components and geometric component counts; the latter proves persistence of scheme-theoretic density. Combining their generic conclusions gives the integral-fibre assertion. All preparations involve finitely many schemes and sheaves, so a common open suffices. A later shrinking of the integral finite cover can be descended to the original base: remove the finite image of its closed complement, which misses the generic point.

**Lemma 7.7 (uniform projective families).** Let $X\subset\mathbb P^n_S$ be projective, with $S$ Noetherian. There is one integer bounding the regularities of all numerically trivial line bundles on all geometric fibres. These bundles are bounded over $S$.

**Proof.** We first establish the relative version of (7.5). If $F$ is coherent and every fibre of its support has dimension at most $r$, one constant $C_F$ satisfies

$$
\begin{gathered}
h^0(X_{\bar s},F_{\bar s}\otimes N(t))
       \leq C_F\binom{t+r}{r},\\
t\geq0,
\end{gathered} \tag{7.11}
$$

for every geometric $\bar s$ and every numerically trivial $N$ there. We induct on $r$, using Noetherian induction on $S$ at each $r$. Thus it suffices to prove a bound on a nonempty open of an integral affine base, after a finite surjective cover as above.

Take a finite graded prime filtration for a module defining $F$ on the geometric generic fibre. Its nonzero sheaf factors are $\mathcal O_{Y_i}(a_i)$, with $Y_i$ integral closed projective subschemes of $X$. Spread the finite filtration by the preparation above, and shrink so every $Y_i$ has geometrically integral fibres, each factor is base-flat, and the filtration is exact on every fibre. Make their Hilbert polynomials constant by the finite cohomological preparation described below; all their fibres then have their generic dimensions. The shifts $a_i$ form a fixed finite list. In dimension zero each fibre of a $Y_i$ is one reduced geometric point, and the section bound for its factor is $1$, independently of the twist or bundle. This proves the initial case.

For a positive-dimensional $Y_i$, choose a generic hyperplane section and spread it after a finite extension. Make its quotient sheaf flat over the base. Its injection into $\mathcal O_{Y_i}$ then stays injective on every fibre. The resulting projective family $H_i$ has fibre dimension at most $\dim(Y_{i,\bar\eta})-1$. The induction hypothesis bounds sections on $H_i$ uniformly. On each integral geometric fibre of $Y_i$, the negative-twist vanishing (7.6), followed by the hyperplane sequences in the proof of (7.5), gives the same binomial section bound with this common constant for $H_i$. A negative $a_i$ decreases it, while a nonnegative $a_i$ contributes at most the fixed factor $\binom{a_i+\dim Y_{i,\bar\eta}}{\dim Y_{i,\bar\eta}}$. Sum over the finite filtration to obtain (7.11) on the chosen open and cover. Noetherian induction on the complement gives finitely many constants; their maximum works on $S$. The dimensions can be bounded before this induction by Dimension of fibres, Corollary 2.3.

Now prove uniform regularity by induction on the maximum fibre dimension, again with Noetherian induction on the base. Zero-dimensional fibres have no positive coherent cohomology, so their line bundles are $0$-regular. On a nonempty open of an integral base, make $X$ flat, choose a hyperplane avoiding the associated points of its geometric generic fibre, and spread it. Generic freeness of its quotient makes the hyperplane sequence injective on every fibre and makes its hyperplane family $H$ flat. Its fibre dimension is smaller. By induction the numerically trivial restrictions to $H$ have a common nonnegative regularity bound $m_H$.

On this open the fibres have one Hilbert polynomial $P$. One can arrange this directly by proper coherence and generic base change for the finitely many sheaves $\mathcal O_X(j)$, $0\leq j\leq n$: their Euler characteristics become constant, and these $n+1$ values determine a polynomial of degree at most $n$. The field theorem gives $P_N=P$ for every numerical $N$. Use (7.11) for $\mathcal O_X$, with constant $C$ and fibre-dimension bound $r$. The regularity proof following (7.8) now has a common budget

$$
\begin{gathered}
m_0=\max(0,m_H+n),\\
V=C\binom{m_0+r}{r}-P(m_0),\\
B=\max(0,V),\\
M=m_0+B+1.
\end{gathered} \tag{7.12}
$$

Indeed the hyperplane sequence first kills every $H^i(N(t))$, $i\geq2$, for $t\geq m_H$. It then makes $h^1(N(t))$ nonincreasing. Equality of two consecutive values makes restriction of sections surjective in that degree. Lemma 2.2 of the regularity lesson propagates this surjectivity to every later twist. The same exact sequences would then keep $h^1$ constant, contradicting Serre vanishing if that value were positive. Thus each positive value decreases strictly, and the value at $m_0$ is at most $B$ by (7.11) and $P_N=P$. This proves $M$-regularity exactly as in Theorem 7.2. The bound depends only on the prepared family. Finite covers preserve the same fibre assertions, and the maximum of the finitely many bounds from Noetherian induction works on the original base, since regularity propagates to larger integers.

On each flat stratum and finite cover used in this construction, put $a=P(M)$. Every numerical bundle is a quotient of $\mathcal O_X(-M)^{\oplus a}$ with polynomial $P$. The relative projective Quot theorem, Theorem 4.1, gives one projective parameter scheme. Its open subset where the universal quotient is a line bundle on the whole fibre carries that line bundle universally. The fibre criterion in Theorem 7.2 applies because both the structure sheaf and the universal quotient are flat over the parameter base. Properness removes the image of the closed non-locally-free locus. These finite-type parameters, composed with their finite covers and strata and then disjointly united, prove boundedness over $S$. $\square$

**Lemma 7.8 (relative descent of bounded families).** The following forms of Lemmas 7.3–7.5 hold over a Noetherian base.

1. Let $g:Y\to Z$ be a morphism of proper, flat $S$-schemes with $(g_{\bar s})_*\mathcal O_{Y_{\bar s}}=\mathcal O_{Z_{\bar s}}$ on every geometric fibre. Boundedness over $S$ of the pulled-back collections implies boundedness of the original collections on $Z$.
2. Let $\alpha:Z\to X$ be finite over $S$, with its conductor square $D'=Z\times_XD$. Suppose its four corner schemes are proper and flat over $S$, and the ring fibre-product square remains exact under every $S$-base change. Bounded restrictions to $Z$ and $D$ give a bounded collection on $X$.
3. For a square-zero thickening $X_0\hookrightarrow X$ of proper $S$-schemes, bounded families on $X_0$ have bounded collections of all fibrewise line-bundle lifts on $X$, after shrinking an integral $S$ to a nonempty open. The same holds for a finite nilpotent filtration.

**Proof.** For 1, let $M$ be a bounding line bundle on $Y_T$, with $T$ of finite type over $S$. Replace $T$ by its reduction and stratify it by Noetherian induction so all coherent $R^qg_{T,*}M$ are flat over their stratum. There are finitely many such $q$, as in Lemma 7.3. The Čech terms are flat over the parameter ring because $Y$ is flat over $S$ and $M$ is invertible. The flat-cohomology argument of that lemma therefore proves arbitrary base change on each stratum. At every point where $M_t=g_t^*L$, projection formula and the stipulated fibrewise unit equality give $(g_{T,*}M)_t=L$, and adjunction is an isomorphism on that fibre. Since $Z$ is flat over $S$, its parameter products are flat over the parameter. The same Nakayama argument gives the rank-one locally free open. Properness of $Z$ and $Y$ then supplies the open where the pushforward is a line bundle and adjunction is an isomorphism everywhere. These opens contain all required representatives. Their union over the finite stratification proves 1.

For 2, the fibre-product ring identity and the local semilocal-frame argument of Lemma 7.4 work on every parameter product by hypothesis. If $T_1,T_2$ bound the two restrictions, the two bundles on $D'_{T_1\times_ST_2}$ are flat over $T_1\times_ST_2$, since $D'$ is flat over $S$. Their Isom is affine and finitely presented over that product. Its universal isomorphism glues a universal line bundle, containing every required geometric-fibre bundle. This proves 2. The hypotheses can be prepared over an integral base: generic freeness of the coherent corner sheaves makes them flat, and flatness of the last term in

$$
0\to\mathcal O_X\to
\alpha_*\mathcal O_Z\oplus\mathcal O_D
\to\alpha_*\mathcal O_{D'}\to0
$$

makes the square exact after every base change. Flatness of its quotient presentations also preserves the specified ideals and closed immersions.

For 3, write $I^2=0$. Over an integral affine base, shrink so $X$, $X_0$ and $I$ are flat over $S$ and all $E^q=R^q p_*I$ are finite free and commute with arbitrary base change. Here $p:X_0\to S$. Proper coherence gives finite modules and only finitely many $q$; generic freeness makes those cohomology modules free. An affine Čech complex has flat terms because $I$ is base-flat, and the flat-cohomology argument again proves the asserted base changes. Choose bases of $E^1,E^2$.

Cover a bounding parameter by finitely many affine $T$ and let $M$ be its universal bundle on $X_{0,T}$. Its obstruction lies in

$$
H^2(X_{0,T},I_T)=\Gamma(T,E^2\otimes\mathcal O_T).
$$

Its finitely many coefficients cut out a closed affine $T_0\subset T$. Naturality of the obstruction and base change put every liftable geometric fibre in $T_0$. The obstruction vanishes on $T_0$ itself, so the unit sequence supplies an actual lift on $X_{T_0}$. Represent a basis of $E^1=H^1(X_0,I)$ by Čech cocycles on a finite affine cover. The functions $1+\sum t_a c^a_{ij}$ give a kernel family over $\mathbb A^h_S$, $h=\operatorname{rank}E^1$. Base change of $E^1$ says that its fibres cover the image of $H^1(X_{0,\bar s},I_{\bar s})$, which is exactly the kernel of the Picard restriction on that fibre. Tensor this family with the chosen lift, as in Lemma 7.5. This parameterizes all lifts. The flatness and cohomology preparations can be made simultaneously for the finitely many stages of a nilpotent filtration. This proves 3. $\square$

**Theorem 7.9 (relative numerical boundedness).** For every proper morphism $X\to S$ with $S$ Noetherian, the collections of all numerically trivial line bundles on its geometric fibres are bounded over $S$.

**Proof.** Fibre dimensions have a finite common bound. Induct on this bound $r$, and at each $r$ use Noetherian induction on the base. Zero-dimensional geometric fibres are finite Artinian schemes and have trivial Picard groups. Their trivial bundles are already a bounding family with parameter $S$. We may therefore suppose $r>0$, reduce the base, and work on a nonempty affine open of one integral component. Empty generic fibres disappear on a nonempty open by properness, so assume the generic fibre is nonempty.

On the geometric generic fibre take its reduced scheme, its finitely many integral components, and integral projective Chow witnesses for all these components. The finite-presentation preparation above realizes these data after a finite surjective integral cover of an open base. Spread the ideal of the generic reduction and its nilpotence equation. After shrinking, this gives a closed $X_0\subset X$ with nilpotent ideal and geometrically reduced fibres. The generic components spread to finitely many proper closed $X_i\subset X_0$ with geometrically integral fibres. They cover $X_0$ after shrinking. To see this schematically, their generic defining ideals have intersection zero; the coherent kernel of $\mathcal O_{X_0}\to\bigoplus_i\mathcal O_{X_i}$ vanishes generically, so vanishes after shrinking. These preparations also make $X_0$ and the finitely many thickenings in the nilpotent filtration flat.

The Chow witnesses spread to projective schemes $Y_i$ and morphisms $Y_i\to X_i$. Spread their inverses on the generic dense isomorphism opens, clearing the finitely many equations for both identities. Thus $h:Y=\coprod_iY_i\to X_0$ is proper and is an isomorphism on an open $U$ whose generic fibre meets every component. Make $Y$ flat over the base. Proper coherence gives the finite algebra $B=h_*\mathcal O_Y$. The unit $\mathcal O_{X_0}\to B$ is injective generically, and its coherent kernel can be killed by shrinking. Set

$$
Y\xrightarrow{g}Z=\operatorname{Spec}_{X_0}B
       \xrightarrow{\alpha}X_0.
$$

Exactly as in Theorem 7.6, $g$ is proper and $g_*\mathcal O_Y=\mathcal O_Z$. Make $Z$ flat over the base. Generic freeness of the finitely many coherent $R^qg_*\mathcal O_Y$, on $Z$, makes them base-flat. Their Čech complexes have flat terms since $Y$ is base-flat. They therefore commute with every base change by the same flat-cohomology argument. In particular $(g_{\bar s})_*\mathcal O_{Y_{\bar s}}=\mathcal O_{Z_{\bar s}}$ for every remaining geometric fibre.

Let $D\subset X_0$ be the conductor subscheme of $\alpha$, and $D'=Z\times_{X_0}D$. Prepare the flatness and exact-square conditions of Lemma 7.8(2) by generic freeness of these finitely many coherent algebras and quotients. Generically $\alpha$ is an isomorphism on $U$, which meets every generic-fibre component. Thus the generic fibre of $D$ has dimension at most $r-1$. By proper upper semicontinuity, Dimension of fibres, Theorem 3.1, shrink once more so every fibre of $D$ has dimension at most $r-1$.

For every numerical line bundle $L$ on a geometric fibre of $X_0$, the pullback $h_{\bar s}^*L$ is numerical on projective $Y_{\bar s}$. Lemma 7.7 bounds all these bundles over the prepared base. Lemma 7.8(1) bounds their descended bundles $\alpha_{\bar s}^*L$ on $Z$. Their restrictions to $D$ are numerical and are bounded by the induction hypothesis in dimension $r-1$. Lemma 7.8(2) consequently bounds all the original numerical bundles on $X_0$.

Finally the finite nilpotent filtration and Lemma 7.8(3) bound all their possible lifts to $X$. Every integral curve in a geometric fibre of $X$ factors through its reduction, which is the corresponding fibre of $X_0$. Hence these are exactly the required numerical lifts. We have obtained the bounding family after a finite surjective change over a nonempty open. Compose the parameter with that finite map to obtain the family over the original open. Noetherian induction supplies the family on its closed complement; the finite disjoint union completes the induction on $S$ and then on $r$. No relative Picard representability hypothesis was used. $\square$

### Euler characteristics on a proper scheme

**Proposition 7.10.** Let $X$ be proper over an algebraically closed field. A line bundle $N$ is numerically trivial if and only if

$$
\chi(F\otimes N)=\chi(F)
$$

for every coherent $F$ on $X$. Thus the Euler-characteristic condition in Theorem 7.2 also holds at the full proper-scheme scope of Theorem 7.6.

**Proof.** We first prove polynomiality without assuming projectivity. Let $G_0(X)$ denote the group generated by coherent sheaves, with $[B]=[A]+[C]$ for each exact sequence $0\to A\to B\to C\to0$. Filter it by the dimension of support. For any line bundle $L$, the operator $[F]\mapsto[F\otimes L]-[F]$ lowers this filtration by one.

To verify this, choose an open $U$ containing the generic points of the support of $F$ on which $F\otimes L$ is isomorphic to $F$. Such an open exists: choose frames for $L$ near those finitely many points and remove intersections of distinct support components, so the isomorphisms have disjoint supports on their overlaps. The graph of this isomorphism extends to a coherent subsheaf $H\subset F\oplus(F\otimes L)$. Concretely, with $j:U\hookrightarrow X$, take the kernel of the map from this direct sum to $j_*$ of its restriction modulo the graph. The direct image is quasi-coherent: on each affine of $X$, cover its intersection with $U$ by finitely many principal opens. Localization commutes with the finite Čech kernel computing sections, which is the affine quasi-coherence criterion. On the Noetherian $X$, the kernel inside the coherent direct sum is coherent. Both projections from $H$ are isomorphisms on $U$; their kernels and cokernels therefore have smaller-dimensional support. Their two exact sequences express $[F\otimes L]-[F]$ as a sum of those smaller-support classes. This proves the assertion, including for reducible supports, nilpotents and embedded components.

If $d=\dim\operatorname{Supp}F$, it follows that

$$
(L-1)^{d+1}[F]=0\quad\text{in }G_0(X).
$$

Proper cohomological finiteness makes Euler characteristic an additive map $G_0(X)\to\mathbb Z$. Hence $f(p)=\chi(F\otimes L^{\otimes p})$, for $p\in\mathbb Z$, satisfies $\Delta^{d+1}f=0$. Successive finite differences give

$$
f(p)=\sum_{j=0}^d\binom pj\Delta^jf(0),
\qquad p\in\mathbb Z.
$$

This identity holds for negative integers too, by the same finite-difference recurrence. In particular $f$ is a polynomial of degree at most $d$.

Now let $N$ be numerical. Theorem 7.6 puts all its positive and negative powers in one finite-type family $M$ on $X\times T$. The coherent family $F_T\otimes M$ is flat over $T$: $F$ is fixed over the field, and tensoring with a line bundle preserves that flatness. The finite cohomological stratification used in Lemma 7.3 applies to this family. Its affine Čech terms are flat over the parameter ring, its finitely many proper direct images are coherent, and generic freeness followed by Noetherian induction gives finitely many strata with base-change-compatible locally free cohomology. Their ranks have finitely many values. Thus all the fibre Euler characteristics, including every $\chi(F\otimes N^{\otimes p})$, lie in a finite set. The polynomial $f(p)$ is consequently constant, which proves the assertion.

Conversely, take $F=\mathcal O_C$ for each integral curve $C\subset X$. The difference of the two Euler characteristics is the degree of $N|_C$, with the same zero-degree criterion after normalization as in (7.3). All such degrees are zero. $\square$

## 8. Curves and other examples

### Smooth projective curves

**Theorem 8.1.** Let $C$ be a smooth projective geometrically connected curve of genus $g$. Its identity component $\operatorname{Pic}^0_{C/k}$ is an abelian variety of dimension $g$. Moreover $\operatorname{Pic}^\tau_{C/k}=\operatorname{Pic}^0_{C/k}$ and $\operatorname{NS}_{\mathrm{geom}}(C)=\mathbb Z$, via degree.

**Proof.** Smoothness and geometric connectedness make $C$ geometrically integral, and $H^0(C,\mathcal O_C)=k$. A curve has $H^2(C,\mathcal O_C)=0$, so Theorem 4.1 makes the Picard scheme smooth. Proposition 2.1 gives tangent dimension $g$, hence dimension $g$ by Theorem 5.1.

The curve construction in the preceding two lessons proves that the degree-$d$ subschemes are open and closed, geometrically integral, and proper. Here is the properness mechanism again. For $d\geq0$ with $d>2g-2$, the Abel map $\operatorname{Sym}^d C\to\operatorname{Pic}^d_{C/k}$ is surjective on every geometric fibre and has projective-space fibres by Riemann–Roch and Serre duality. The symmetric power is proper. For any base change, the image of the inverse image of a closed subset is its image under the Picard structure map, by surjectivity; that image is closed because the symmetric power is proper. Finite type and separatedness of the degree piece therefore make it proper. Geometric translation carries this assertion to every degree, in particular degree zero.

The degree-zero piece is geometrically integral, contains the identity, and is therefore exactly $P^0$. A smooth proper geometrically connected group scheme over a field is geometrically integral, by the connected-group theorem above, and hence is an abelian variety. Its projectivity is proved in Abelian varieties, Proposition 1.2. Thus $P^0$ is a smooth projective group scheme of dimension $g$.

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

**Theorem 8.2 (the dual abelian variety).** For an abelian variety $A/k$,

$$
A^\vee=\operatorname{Pic}^0_{A/k}
\tag{8.2}
$$

is an abelian variety of dimension $\dim A$. Rigidification at the identity gives a normalized Poincaré bundle on $A\times A^\vee$, trivial on both identity slices. The complete proof over an arbitrary field is Abelian varieties, Theorem 6.15 and Proposition 6.17. Those results use the projective Picard construction of the preceding lesson and the tangent calculation of Proposition 2.1. Their cohomology bialgebra calculation bounds $h^1(A,\mathcal O_A)$ by $\dim A$; an ample bundle produces a finite translation map into the Picard identity component and forces equality. The resulting smooth proper identity component is the dual variety. Rigidification at the origin constructs the universal bundle on every parameter scheme, including nonreduced ones. These arguments do not use the Néron–Severi finiteness or numerical converse of Sections 6–7. The relative historical theorem is in FGA, Exposé 236, Theorem 3.3(iii). This is stronger than the vanishing criterion of Theorem 4.1: for abelian varieties of dimension at least two, $H^2(A,\mathcal O_A)$ need not vanish, yet their Picard schemes are smooth.

### Enriques surfaces

An Enriques surface, in the numerical definition used here, is a smooth proper geometrically integral surface $X$ over an algebraically closed field with numerically trivial canonical bundle $K=\omega_X$ and $\chi(\mathcal O_X)=1$. The following calculation uses these two numerical conditions. It determines the Picard schemes in all three types, including the classical type in characteristic two. The names *singular* and *supersingular* below refer to the Frobenius action; the surfaces themselves are smooth.

**Proposition 8.1 (the three Picard schemes).** If $K\ne\mathcal O_X$, then $K$ has order two and

$$
\begin{gathered}
h^1(\mathcal O_X)=h^2(\mathcal O_X)=0,\\
\operatorname{Pic}^\tau_{X/k}\simeq(\mathbb Z/2\mathbb Z)_k.
\end{gathered} \tag{8.3}
$$

These are the classical Enriques surfaces, and this is the only type outside characteristic two. Their $P^0$ is a point, so their canonical bundle is numerical but not algebraically trivial.

If $K=\mathcal O_X$, then the characteristic is two, $h^1(\mathcal O_X)=h^2(\mathcal O_X)=1$, and $P^\tau=P^0$ is connected of length two. If absolute Frobenius is bijective on $H^1(\mathcal O_X)$, this group is $\mu_2$; this is the singular type. If Frobenius is zero, it is $\alpha_2$; this is the supersingular type. In both cases the torsion component group is zero, while the tangent space has dimension one.

**Proof. A numerical bundle with a section.** On any proper integral scheme, a numerically trivial line bundle with a nonzero section is trivial. Indeed take an integral projective Chow witness $h:Y\to X$. Its pulled-back bundle is numerical, and its section is nonzero because $h$ is dominant. Theorem 7.2 gives the same Hilbert polynomial as $\mathcal O_Y$. The injection of $\mathcal O_Y$ defined by that section therefore has cokernel of polynomial zero. A nonzero coherent sheaf on a projective scheme has positive leading Hilbert coefficient, so that cokernel is zero. The pulled-back section is nowhere vanishing. Surjectivity of $h$ then says that the original section has no zero either, proving the assertion.

We also use proper Serre duality, in its trace-compatible form

$$
H^i(X,L)^\vee\simeq H^{2-i}(X,K\otimes L^{-1}).
$$

The exact proper duality provider is The right adjoint of derived pushforward, Theorems 5.1–5.2. Its local computation on a smooth chart identifies the dualizing complex with $K[2]$, by the canonical-bundle calculation, Proposition 8.2. Explicitly, a regular embedding in a smooth affine chart has dualizing module $\det(I/I^2)^\vee\otimes\det\Omega^1_{\mathrm{ambient}}|_X$, identified with $\det\Omega^1_X$ by the conormal sequence. Changes of regular generators and ambient coordinates have cancelling determinants. Comparing two embeddings through their product gives the same identification on overlaps. Thus this computation applies to the proper duality complex without a projectivity assumption on $X$. Its trace pairing is cup product followed by the trace on $H^2(K)$.

**The geometric points and the classical case.** Let $L$ be numerical and nontrivial. The first paragraph gives $h^0(L)=0$. Proposition 7.10 gives $\chi(L)=1$. Serre duality consequently gives

$$
h^0(K\otimes L^{-1})=1+h^1(L)>0.
$$

The bundle $K\otimes L^{-1}$ is numerical, so the first paragraph forces it to be trivial. Hence $L=K$. Thus the geometric numerical classes are $\{\mathcal O_X,K\}$ when $K$ is nontrivial, and just $\{\mathcal O_X\}$ otherwise. If $K$ is nontrivial, its square is numerical too, and cannot equal $K$ by cancellation. It is therefore trivial. Moreover $h^0(K)=0$, so duality and $\chi(\mathcal O_X)=1$ give $h^2(\mathcal O_X)=h^1(\mathcal O_X)=0$. The Picard scheme is smooth by Theorem 4.1. Its finite-type numerical part has just two geometric points, hence is a finite étale group of order two. This proves (8.3), in every characteristic in which this case occurs.

**The local ring in the remaining case.** Suppose $K=\mathcal O_X$. Then $h^2(\mathcal O_X)=1$, and the Euler characteristic gives $h^1(\mathcal O_X)=1$. The finite-type $P^\tau$ has only one geometric point. It is therefore finite and local, and equals $P^0$. Its tangent space has dimension one. Its local algebra has the form

$$
R=k[t]/(t^m),\qquad m\geq2.
$$

To see this algebra assertion directly, a lift $t$ of a tangent-coordinate generator generates the maximal ideal by Nakayama. Expand successively using $R=k+tR$ and nilpotence; this makes $k[t]\to R$ surjective, with kernel $(t^m)$.

Choose a nonzero tangent class $\xi\in H^1(X,\mathcal O_X)$. Under a trivialization of $K$, Serre duality makes the cup pairing on this one-dimensional space perfect. Thus $\xi\smile\xi\ne0$ in $H^2(X,\mathcal O_X)$.

If $m\geq3$, restrict the universal normalized line bundle to $k[t]/(t^3)$. Such a universal bundle exists because $X$ has a $k$-point and $H^0(\mathcal O_X)=k$, by the Picard-functor rigidification theorem, Theorem 2.1. On a finite affine cover it has transitions

$$
g_{ij}=1+a_{ij}t+b_{ij}t^2.
$$

The first coefficients represent the nonzero universal tangent $\xi$. The equation $g_{ij}g_{jk}=g_{ik}$ gives

$$
b_{ik}=b_{ij}+b_{jk}+a_{ij}a_{jk}.
$$

It makes the Čech representative of $\xi\smile\xi$ a coboundary, contradicting the perfect pairing. Thus $m=2$.

**The group law and Frobenius.** Put $G=P^\tau=\operatorname{Spec}k[t]/t^2$. The counit and the two identity laws force its comultiplication to be

$$
\Delta t=t\otimes1+1\otimes t+c\,t\otimes t
$$

for some $c\in k$. Squaring gives $0=\Delta(t^2)=2t\otimes t$. Since $t\otimes t\ne0$, the characteristic must be two. If $c=0$ this Hopf algebra is $\alpha_2$. If $c\ne0$, the coordinate $u=ct$ has the law $u+v+uv$ and $(1+u)^2=1$, identifying $G$ with $\mu_2$.

It remains to relate $c$ to Frobenius, rather than only list the two possibilities. Write the universal bundle on $X\times G$ with transitions $1+a_{ij}t$, representing $\xi$. The universal tensor-product law on the Picard functor identifies its pullback by multiplication with the tensor product of its two pullbacks. Normalize at the chosen point of $X$. This makes the isomorphism unique and the identity along the axes $t=0$ and $u=0$. On each affine chart it is consequently multiplication by $1+b_i tu$. Comparing the transition functions on $k[t,u]/(t^2,u^2)$ yields

$$
a_{ij}^2+c a_{ij}=b_j-b_i.
$$

Absolute Frobenius on coherent cohomology squares the Čech coefficients, so

$$
F(\xi)=c\xi.
$$

On a one-dimensional space over the perfect field $k$, this semilinear map is zero for $c=0$ and bijective for $c\ne0$. This proves the supersingular and singular assertions, respectively. Their connected length-two Picard scheme has one component, so its component torsion is zero, as claimed. $\square$

For the historical type names and the Picard-scheme statements, compare Liedtke, [*Arithmetic Moduli and Lifting of Enriques Surfaces*](https://arxiv.org/abs/1007.0787v2), Section 1, Definition 1.2 and its following discussion, crediting Bombieri and Mumford. The computation here starts from the numerical Enriques conditions and determines the actual length, group law and Frobenius action.

### Igusa's nonreduced example

Igusa's [*On some problems in abstract algebraic geometry*](https://pmc.ncbi.nlm.nih.gov/articles/PMC534315/) exhibits the characteristic-two phenomenon

$$
\dim\operatorname{Pic}^0_{X/k}=1,
\qquad h^1(X,\mathcal O_X)=2. \tag{8.4}
$$

These values are also recorded in Kleiman, *The Picard scheme*, Remark 5.15. We now realize them by an explicit smooth projective quotient. The calculation will distinguish a finite étale covering of surfaces from the infinitesimal kernel of its pullback on Picard schemes.

#### The surface and its elliptic fibration

Work over an algebraically closed field $k$ of characteristic two. Let $E$ and $F$ be two copies of the plane cubic

$$
\begin{gathered}
Y^2Z+XYZ=X^3+Z^3,\\
O=[0:1:0].
\end{gathered} \tag{8.5}
$$

On $Z=1$, the two partial derivatives are $y+x^2$ and $x$. Their simultaneous zero is not on the curve. At $O$, the derivative with respect to $Z$ is nonzero. Thus the cubic is smooth. It is integral: distinct positive-degree plane components would intersect, producing a singular point. The projective-space sequence for a cubic gives $h^1(\mathcal O_E)=1$, and similarly for $F$.

The degree-one Abel construction identifies a smooth genus-one curve with its degree-zero Picard scheme after choosing $O$. Indeed a degree-one bundle has one section and no first cohomology; its unique effective divisor is one point. Cohomology and base change makes this inverse a morphism in families. Thus $P\mapsto\mathcal O(P-O)$ gives the group law. A vertical line cuts out $P+(x,y+x)+O$, while the line at infinity cuts out $3O$. Consequently inversion on the affine part is

$$
-(x,y)=(x,y+x).
$$

In particular $a=(0,1)$ is a nonidentity point of order two on $E$.

On $Y=E\times F$ let the constant group $G=(\mathbb Z/2\mathbb Z)_k$ act by

$$
\sigma(u,v)=(u+a,-v). \tag{8.6}
$$

This action is schematically free. Equality $u+a=u$ on any test scheme would imply that its map to $E$ makes $a=0$, by cancellation in the group scheme. The two distinct constant sections $a$ and $0$ have empty equalizer. The quotient therefore has a finite étale torsor map

$$
q:Y\longrightarrow X=Y/G. \tag{8.7}
$$

Here both scheme existence and étaleness follow from Quotients and torsors, Theorem 5.2 and Corollary 4.4. Every finite orbit in a projective variety lies in an affine open: choose a hyperplane missing its finitely many points. These results apply without requiring the group order to be invertible in $k$.

We also need projectivity of $X$. The following construction supplies it. Choose a very ample bundle $L$ on $Y$ and replace it by $M=L\otimes\sigma^*L$. Permuting the two factors gives $M$ a $G$-linearization. Its section ring $R$ is finitely generated, and $Y=\operatorname{Proj}R$. For each of finitely many homogeneous algebra generators $r_i$, the coefficients of

$$
\prod_{g\in G}(T-g r_i)
$$

are invariant. Let $C_0$ be the graded $k$-algebra generated by these coefficients. The monic equations make $R$ finite over the Noetherian ring $C_0$. Hence its submodule $C=R^G$ is finite over $C_0$, and is itself a finitely generated graded algebra.

Invariant homogeneous sections cover $Y$ by their nonvanishing loci. To see this, choose a section $s$ nonzero at every point of a prescribed finite orbit and use $\prod_g g s$. On such an invariant open, localization in this invariant section commutes with taking invariants, and its degree-zero invariant ring is $C_{(f)}$. The affine quotient charts are consequently exactly those of $\operatorname{Proj}C$. They identify the sheaf quotient $X$ with $\operatorname{Proj}C$, which is projective over $k$; one may take a Veronese subring to obtain a projective embedding. This argument is valid in characteristic two and uses no averaging operator.

Smoothness descends through the étale covering (8.7), and integrality follows from the integral covering variety. Thus $X$ is a smooth projective integral surface. The same quotient construction on $E$ gives a smooth projective curve

$$
r:E\longrightarrow B=E/\langle a\rangle,
$$

with $r$ finite étale of degree two. A nonzero invariant differential on $E$ is translation invariant and nowhere vanishing, so descends to a nowhere-vanishing differential on $B$. Thus $\omega_B\simeq\mathcal O_B$ and Serre duality gives $h^1(\mathcal O_B)=1$. In particular $B$ has genus one.

The map $Y\to B$ factors through $f:X\to B$. Pulling $f$ back along the torsor $r$ gives $E\times F\to E$: a choice of a lift in $E$ chooses a representative of the diagonal orbit. Thus $f$ is a smooth proper family of genus-one curves. The fixed origin $O_F$ gives a section $s:B\to X$, by descending $E\times\{O_F\}$.

#### Coherent cohomology of the quotient

On the étale cover $E\to B$, the bundles $f_*\mathcal O_X$ and $R^1f_*\mathcal O_X$ become, respectively,

$$
\mathcal O_E,
\qquad H^1(F,\mathcal O_F)\otimes_k\mathcal O_E.
$$

This is the affine Čech calculation for a product, and is compatible with flat base change. The first descent datum is trivial. On the second, the nonidentity deck transformation acts by inversion on $H^1(F,\mathcal O_F)$.

That inversion acts by $-1$ can be checked without a characteristic-zero comparison. The product Čech complex gives

$$
H^1(F\times F,\mathcal O)
\simeq H^1(F,\mathcal O_F)\oplus H^1(F,\mathcal O_F).
$$

Pullback by addition has the two identity components, as restriction to its two axes shows. Pull back again by $v\mapsto(v,-v)$. Addition becomes the constant map, so $1+[-1]^*=0$ on $H^1$. In characteristic two this makes the descent action the identity. Therefore

$$
f_*\mathcal O_X=\mathcal O_B,
\qquad R^1f_*\mathcal O_X=\mathcal O_B. \tag{8.8}
$$

The low-degree exact sequence of the Leray spectral sequence, Theorem 4.1 now reads

$$
\begin{gathered}
0\longrightarrow H^1(B,\mathcal O_B)
\longrightarrow H^1(X,\mathcal O_X)\\
\longrightarrow H^0(B,\mathcal O_B)
\longrightarrow H^2(B,\mathcal O_B)=0.
\end{gathered} \tag{8.9}
$$

Both outside nonzero spaces have dimension one. This proves $h^1(X,\mathcal O_X)=2$. Notice that taking invariants of $H^1(Y,\mathcal O_Y)$ would not by itself justify this calculation: invariants under a group of order two are not exact in characteristic two.

#### The dimension of the Picard component

We first describe $\operatorname{Pic}^0_{Y/k}$. Pullback from the factors and restriction to the two origin slices give homomorphisms

$$
\begin{gathered}
j:\operatorname{Pic}^0_{E/k}\times\operatorname{Pic}^0_{F/k}
\longrightarrow\operatorname{Pic}^0_{Y/k},\\
\rho:\operatorname{Pic}^0_{Y/k}
\longrightarrow\operatorname{Pic}^0_{E/k}\times\operatorname{Pic}^0_{F/k},\\
\rho j=1.
\end{gathered} \tag{8.10}
$$

The source of $j$ is proper, and $j$ is a monomorphism because it has the left inverse $\rho$. Thus it is a closed immersion. The product Čech calculation gives $h^1(Y,\mathcal O_Y)=2$. Theorem 5.1 bounds the dimension of its Picard identity component above by two, while the closed immersion $j$ bounds it below by two. The equality criterion makes that component smooth. It is irreducible, and the closed image of $j$ has its full dimension, so its image has the whole support. Smoothness makes the target reduced; a closed subscheme with that support must be the entire target. Hence $j$ is an isomorphism.

Under (8.10), $\sigma^*$ acts by $(1,[-1])$. Translation acts trivially on degree-zero classes on $E$: the divisor $[P-a]-[-a]$ has the same genus-one group sum as $[P]-[O]$. The equality holds as a scheme morphism, since these smooth Picard curves are reduced and their geometric points are dense. Inversion on $F$ gives inversion on its degree-zero Picard scheme by the same divisor calculation. The fixed subgroup of $\sigma^*$ is therefore

$$
\operatorname{Pic}^0_{E/k}
\times\operatorname{Pic}^0_{F/k}[2]. \tag{8.11}
$$

Its dimension is one. Indeed, under the genus-one Abel isomorphism, the second factor's $[2]$-kernel is the fixed scheme of $(x,y)\mapsto(x,y+x)$. On the affine chart its support has $x=0$, hence $y=1$; its only other possible point is $O$. It is a zero-dimensional closed subscheme of a proper curve, and is finite. This conclusion keeps its possible nilpotents.

Pullback $q^*:\operatorname{Pic}_{X/k}\to\operatorname{Pic}_{Y/k}$ has finite kernel, in fact

$$
\ker(q^*)\simeq\mu_2. \tag{8.12}
$$

To prove this as an equality of fppf sheaves, work locally on a parameter scheme $T$ so that a class in the kernel is a line bundle whose pullback to $Y_T$ is trivial. A descent datum on that trivial bundle is an invertible scalar for each element of $G$. All such scalars come from $T$, since $H^0(Y_T,\mathcal O)=H^0(T,\mathcal O_T)$, locally on $T$, by (1.2). The cocycle condition is precisely a character $G_T\to\mathbb G_{m,T}$, determined by a unit $u$ with $u^2=1$. Changing the trivialization multiplies by a base unit and does not change the character. Conversely every such character descends the trivial bundle. These constructions are inverse and commute with base change, proving (8.12), including nonreduced $T$.

The homomorphism $q^*$ sends $P^0=\operatorname{Pic}^0_{X/k}$ into the fixed subgroup (8.11), since $q\sigma=q$. Its fibres are translates of its finite kernel, so they are zero-dimensional. The finite-type dimension theorem consequently gives $\dim P^0\leq1$. On the other hand $f^*:\operatorname{Pic}^0_{B/k}\to P^0$ has the left inverse $s^*$ furnished by the section of $f$. It embeds a one-dimensional proper Picard curve, so $\dim P^0\geq1$. Thus $\dim P^0=1$, proving (8.4).

Finally Proposition 2.1 gives $\dim T_0P=2$. Theorem 5.1 proves that $P^0$ is not smooth. A reduced finite-type group scheme over the perfect field $k$ is smooth, so $P^0$ is nonreduced. The finite étale nature of $q$ is fully compatible with its infinitesimal pullback kernel $\mu_2$; the two assertions concern different morphisms.

There are also two independent global one-forms on $X$. The invariant forms from $E$ and $F$ form a basis on $Y$; translation fixes the first, and inversion acts by $-1=1$ on the second. Étale descent therefore gives a basis of $\Omega^1_{X/k}$. In particular $h^0(X,\Omega^1_{X/k})=2$ and $\omega_X\simeq\mathcal O_X$.


## 9. Exercises

**Exercise 1.** Compute the tangent space at the identity of the Picard scheme of $\mathbb P^n_k$ and of a smooth projective geometrically connected curve of genus $g$. Include $n=0$.

**Exercise 2.** For a small extension (3.1), construct the obstruction to lifting a line bundle using transition functions. Prove its independence of choices and prove that, when it vanishes, the isomorphism classes of identified lifts form the claimed torsor.

**Exercise 3.** Let $X$ be a smooth projective geometrically connected surface with geometric genus $p_g=h^0(X,\omega_X)=0$. Prove that its Picard scheme is smooth in every characteristic. Explain why this need not make it connected.

**Exercise 4.** Starting from $T_0P=H^1(X,\mathcal O_X)$, prove $\dim P^0\leq h^1(X,\mathcal O_X)$. Prove the equality criterion and identify exactly where passage to an algebraic closure is useful.

**Exercise 5.** For a smooth projective geometrically connected curve $C/k$, prove that a line bundle is geometrically numerically trivial exactly when it has degree zero. Deduce $\operatorname{Pic}^\tau_{C/k}=\operatorname{Pic}^0_{C/k}$ as subgroup schemes. Explain what changes if $C$ has no rational point.

**Exercise 6.** For the quotient (8.7), use the unit $1+\epsilon$ over $D=k[\epsilon]/(\epsilon^2)$ as the descent scalar for $\sigma$ on the trivial bundle on $Y_D$. Show that it descends to a nonzero tangent class in the kernel of $q^*:H^1(X,\mathcal O_X)\to H^1(Y,\mathcal O_Y)$. Explain why étaleness of $q$ does not force this map to be injective. Compute $h^0(X,\Omega^1_X)$ and $h^2(X,\mathcal O_X)$.

**Exercise 7.** Take $X=\operatorname{Spec}k[\eta]/(\eta^2)$ and try to frame line bundles only along $X_{\mathrm{red}}$. Compute the automorphisms of the trivial framed object on every parameter scheme. Explain why reduced points do not suffice for the construction in Theorem 1.2. Then use $Z=X$ and compute its Picard sheaf.

**Exercise 8.** Let $X$ be the disjoint union of two copies of $\mathbb P^1_k$, with the degree-one polarization on each component. For $a\in\mathbb Z$, let $L_a$ restrict to $\mathcal O(a)$ and $\mathcal O(-a)$. Compute its Hilbert polynomial and regularity. Is the collection of all $L_a$ bounded? Which members are numerically trivial? Explain why a fixed Hilbert polynomial alone cannot replace (7.5).

**Exercise 9.** Let $X$ be an integral projective curve with one ordinary node $p$, normalization $\nu:\mathbb P^1\to X$, and $\nu^{-1}(p)=\{0,\infty\}$. Its conductor is $D=\operatorname{Spec}k$, with $D'=\operatorname{Spec}(k\times k)$. Use Lemma 7.4 to prove an exact sequence $1\to k^\times\to\operatorname{Pic}(X)\xrightarrow{\nu^*}\mathbb Z\to0$. Identify the numerically trivial classes and give one finite-type family containing all of them. Explain why the pullback can have infinitely many distinct classes in its kernel while Lemma 7.3 still concerns boundedness.

**Exercise 10.** Let $q$ be a prime. Prove that the additive group $\mathbb Z[1/q]$ is torsion-free of rank one but is not finitely generated, and that every homomorphism $\mathbb Z[1/q]\to\mathbb Z$ is zero. Identify the extra property supplied by curve degrees in the passage from (6.6) to (6.7).

**Exercise 11.** Let $k$ be algebraically closed, $S=\mathbb A^1_k$, and choose distinct $a_n\in k$ for $n\geq2$. Form the $S$-scheme $G$ as the disjoint union of one copy of $S$ and, for each $n$, $n-1$ copies of $\operatorname{Spec}k$ mapping to $a_n$. Give it a commutative group-scheme structure whose fibre at $a_n$ is the constant group $\mathbb Z/n$ and whose other geometric fibres are trivial. Prove that $G$ is locally of finite type with finite geometric fibres of unbounded orders, and explain why it cannot have a finite-type $S$-parameter meeting every point of every geometric fibre. Identify the finiteness property that Theorem 7.9 supplies in the proof of Theorem 6.4.

**Exercise 12.** Let $(a_{ij})$ be an additive Čech $1$-cocycle for $\mathcal O_X$. Compute the Čech coboundary of the $1$-cochain $(a_{ij}^2)$ and show it is $-2(a_{ij}a_{jk})$. Use this to give a second proof that a smooth proper geometrically integral surface with $\omega_X=\mathcal O_X$ and $\chi(\mathcal O_X)=1$ cannot exist in characteristic different from two.

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

**Solution 6.** In characteristic two $(1+\epsilon)^2=1$, so the scalar satisfies the descent cocycle condition for the order-two generator. The descended bundle reduces to the trivial bundle and its pullback to $Y_D$ is trivial by construction. If the descended bundle were trivial, its linearization upstairs could be changed to the identity by an invertible global function on $Y_D$. Every such function is a unit of $D$, by (1.2); $\sigma$ fixes those units, so a change of trivialization leaves the scalar $1+\epsilon$ unchanged. It therefore cannot become $1$. This gives a nonzero tangent class with zero pullback, precisely the tangent direction of the subgroup $\mu_2$ in (8.12).

Finite étale pullback is faithfully flat for sheaves but need not be injective on higher coherent cohomology. In particular there is no averaging retraction when its degree is zero in $k$. The two invariant one-forms of the construction descend to a basis of $\Omega^1_X$, so $h^0(X,\Omega^1_X)=2$ and $\omega_X=\mathcal O_X$. Projective Serre duality gives $h^2(X,\mathcal O_X)=h^0(X,\omega_X)=1$, since $X$ is integral and proper. Thus the nonreduced Picard component does not contradict the $H^2=0$ smoothness criterion.

**Solution 7.** The global functions are $C=k[\eta]/(\eta^2)$, whereas restriction to the reduced point has target $k$. Over a $k$-algebra $R$, every automorphism preserving the frame is multiplication by

$$
1+\eta a,\qquad a\in R.
$$

These are all the kernel elements, and their product corresponds to addition of $a$. Thus the residual automorphism group is $\mathbb G_a$ in every characteristic. The framed stack still has nontrivial automorphisms; it has not yet produced the presentation with unique gluing isomorphisms used in Theorem 1.2. The missing infinitesimal jet is exactly the nonzero kernel of $C\to k$.

For $Z=X$, the restriction algebra is $D=C$, so $H=J$, $K=1$, and a framed bundle has a specified global trivialization. Its isomorphism class is the unique trivial framed object on every test scheme. Consequently $R_Z=\operatorname{Spec}k$ and the fppf Picard sheaf is trivial. Equivalently, a line bundle on the finite scheme $X_T$ has a generator locally on $T$, as the determinant argument in the proof shows. Nonzero infinitesimal units give automorphisms of the trivial bundle, while the Picard sheaf classifies its locally defined isomorphism class.

**Solution 8.** The two curve Euler characteristics give

$$
\chi(L_a(t))=(t+a+1)+(t-a+1)=2t+2.
$$

All higher cohomology with index at least two vanishes. Since $H^1(\mathbb P^1,\mathcal O(b))=0$ exactly when $b\geq-1$, the regularity conditions are $M\geq a$ and $M\geq-a$. The least regularity is therefore $|a|$, which is unbounded despite the common polynomial.

If a finite-type family of line bundles contained all these bundles, restriction to the first fixed component would have locally constant degree on the parameter scheme. Finitely many connected components allow only finitely many degrees, contradicting the occurrence of every $a$. Thus the collection is not bounded. Numerical triviality requires degree zero on both components, so only $a=0$ qualifies. At twist zero, $h^0(L_a)=|a|+1$ for $a\ne0$, whereas $h^0(L_0)=2$. There is no uniform section bound of the form (7.5) for this collection; numerical triviality is the hypothesis that supplies it in Theorem 7.2.

**Solution 9.** A bundle on the normalization is $\mathcal O_{\mathbb P^1}(d)$, and a bundle on $D$ is trivial. Choose frames of its two fibres over $D'$. Gluing is a pair $(u_0,u_\infty)\in(k^\times)^2$. Changing a frame on either whole bundle multiplies both entries by the same scalar. Thus the isomorphism class of the gluing for fixed $d$ is measured by $u_\infty/u_0\in k^\times$. Tensor product multiplies this ratio in degree zero. Every $d$ occurs: choose a smooth $k$-point $q$ of $X$ and use $\mathcal O_X(dq)$. These facts give the exact sequence, with a splitting after the choice of $q$.

The only integral curve in $X$ is $X$ itself, and its normalized degree is $d$. The numerical subgroup is therefore the kernel $k^\times$. For $d=0$, glue the trivial bundle on $\mathbb P^1\times\mathbb G_m$ to the trivial one on $D\times\mathbb G_m$ using $(1,t)$ on the two branches. Lemma 7.4 constructs one line bundle on $X\times\mathbb G_m$ with all the required fibres. The parameter scheme is connected, and $t=1$ gives the trivial bundle, so all these classes are algebraically trivial as well. There are infinitely many such classes, yet they are bounded by this one finite-type family. Boundedness does not require finite fibres of pullback. In this example $\nu_*\mathcal O_{\mathbb P^1}\ne\mathcal O_X$, so the conductor gluing lemma, rather than the hypothesis of Lemma 7.3, supplies that family.

**Solution 10.** The group is a subgroup of $\mathbb Q$, so it is torsion-free, and its tensor product with $\mathbb Q$ is $\mathbb Q$, of dimension one. A finite set of generators would lie in $q^{-m}\mathbb Z$ for one $m$, whose generated subgroup cannot contain $q^{-(m+1)}$. Thus it is not finitely generated.

For a homomorphism $h$ to $\mathbb Z$, the equation $h(1)=q^n h(q^{-n})$ for every $n$ says that $h(1)$ is divisible by every power of $q$. Hence $h(1)=0$, and torsion-freeness of $\mathbb Z$ gives $h(q^{-n})=0$ for all $n$. Thus $h=0$. In Theorem 6.2 the integer curve-degree maps separate every nonzero numerical class. Once their rational span has finite dimension, finitely many of those maps still separate points, giving an injection into $\mathbb Z^r$. The group $\mathbb Z[1/q]$ has no such separating integer-valued maps. This explains why the finite-rank argument needs the integer-lattice step to establish finite generation.

**Solution 11.** Use the copy of $S$ as the identity section. Label the extra copies over $a_n$ by the nonzero elements of $\mathbb Z/n$. On the product of two such copies over the same $a_n$, define multiplication by addition of labels, using the identity section at $a_n$ when their sum is zero. Products of copies supported at distinct $a_n$ are empty over $S$. A product with the identity copy is the corresponding copy itself. These rules define morphisms on the open-and-closed summands of $G\times_SG$ and glue to multiplication. Negation of labels gives inversion. On every summand of a triple product, the group axioms reduce to those of $\mathbb Z/n$, or to the identity copy of $S$, so they hold as morphism identities.

Each summand is of finite type over $S$, hence $G$ is locally of finite type. At $a_n$ its geometric fibre consists of the identity and $n-1$ other reduced points. Every other geometric fibre, including the generic one, has only the identity. Thus all its fibres are finite, with unbounded orders. The infinitely many nonempty open-and-closed summands show that $G$ is not quasi-compact, so it is not of finite type over $S$.

If a finite-type $S$-scheme $T$ mapped to $G$ and met all its geometric-fibre points, each connected component of $T_{\bar s}$ could meet only one point of the discrete $G_{\bar s}$. The component bound used in (6.10) would bound all those fibre orders, a contradiction. Theorem 7.9 supplies exactly a finite-type parameter meeting every numerical Picard class. Its existence, together with the component bound, is the additional uniform finiteness assertion; individual finite fibres alone do not give that bound. This group scheme is not asserted to be a Picard scheme of a proper family.

**Solution 12.** The cocycle equation gives $a_{ik}=a_{ij}+a_{jk}$, so

$$
\begin{aligned}
\delta(a^2)_{ijk}
 &=a_{jk}^2-a_{ik}^2+a_{ij}^2\\
 &=-2a_{ij}a_{jk}.
\end{aligned}
$$

If two is invertible, the cup square of any degree-one class is therefore zero. For the proposed surface, Serre duality gives $h^2(\mathcal O_X)=1$ and the Euler characteristic gives $h^1(\mathcal O_X)=1$. The cup pairing on this one-dimensional space, followed by the canonical trace, is perfect. Its nonzero generator must have nonzero square, a contradiction. In characteristic two the displayed factor $2$ is zero; the length-two calculation in Proposition 8.1 retains the needed infinitesimal information.

## 11. What this lesson does not prove

The deformation, numerical and surface calculations above use the following foundations, with their exact scopes specified below.

- **General proper-scheme representability.** Theorem 1.2 proves the field existence theorem for every proper $X$, including nonreduced schemes and schemes with extra global functions. Its finite subscheme detects the whole global-function algebra. The framed Picard presentation and its quotient use the complete Picard-stack and flat-bootstrap proofs in *Moduli stacks are algebraic* and *The bootstrap theorem*. Lemma 1.1 supplies the additional scheme and separation assertion, including imperfect fields and infinitely many components. The preceding lesson retains its independent projective, relative-base construction.
- **Cohomology and descent foundations.** Affine acyclicity and separated affine Čech computation are [Stacks, Tags 01XD and 01KP]; proper-support finiteness is [Stacks, Tag 02O6]. The preceding Picard-functor lesson supplies the injections, equality of étale and fppf sheaves, and rigidification theorem. Étale-local Artin rings with separably closed residue field are strictly henselian, so étale covers have sections; descent of smoothness and the local Artin smoothness criterion are standard infinitesimal foundations, with the latter [Stacks, Tag 02HX].
- **Characteristic-zero algebra.** The criterion that a locally finite-type scheme over a characteristic-zero field with locally free differentials is smooth is proved by derivations and induction in Lie algebras and smoothness of group schemes, Lemmas 4.1–4.2. Lemma 4.2 proves the group-scheme differential trivialization, and Theorem 4.3 deduces Cartier's theorem from that criterion.
- **Identity components and local algebra.** The canonical closed, quasi-compact, geometrically irreducible identity subgroup is proved in Group schemes over a field, Theorems 2.2–2.3; its finite-type and base-change properties also occur in Kleiman, Proposition 5.3. Completion preserves dimension; a power-series ring is a regular local domain; a nonzero ideal in it lowers dimension. The corresponding local-algebra ingredients were used in the Hilbert–Quot dimension bound. Reduced-group smoothness over a perfect field is proved in Lie algebras and smoothness of group schemes, Theorem 5.1.
- **Finiteness and numerical characterization.** Theorem 7.2 proves the projective numerical criterion, Euler invariance, and uniform regularity for the fixed projective scheme. Lemmas 7.3–7.5 and Theorem 7.6 prove boundedness of all numerical line bundles on every proper scheme, the full converse in (7.4), and finite type of the torsion component. Their programme inputs are proper coherence and the integral Chow construction in *Proper morphisms and coherent direct images*, generic freeness in *Flat morphisms*, and the affine finite-presentation Isom theorem in *Moduli stacks are algebraic*. Theorem 6.2 proves finite generation of the whole Néron–Severi group by the degree-normalized Kummer map, finite second étale cohomology, and an integer-lattice embedding. Theorem 6.3 proves the uniform rank bound from constructibility, proper base change and universal coefficients. Their precise étale and ℓ-adic prerequisite locators are supplied in those proofs. Lemmas 7.7–7.8 and Theorem 7.9 give the required relative numerical family at full proper Noetherian scope. Theorem 6.4 bounds torsion orders by the geometric component counts of that finite-type parameter. The geometric spreading, density and component-count arguments are the exact current programme proofs linked there.
- **Curve and abelian-variety foundations.** Riemann–Roch and Serre duality, including (10.1), are imported cohomological prerequisites. The full Abel construction, connected degree pieces, and properness argument belong to the preceding two lessons. Projectivity is Abelian varieties, Proposition 1.2. The dual variety and its normalized Poincaré bundle are proved there in Theorem 6.15 and Proposition 6.17, using only the earlier Picard existence and tangent results from this course.
- **Special surfaces.** Proposition 8.1 derives all three Enriques Picard schemes from the numerical definition $\chi(\mathcal O_X)=1$ and numerically trivial $\omega_X$, including the classical characteristic-two case. It uses proper Euler invariance in Proposition 7.10, proper Serre duality with its smooth canonical-bundle identification, and the explicit Čech obstruction and tensor law; the group length and Frobenius action are computed there. The separate quotient construction in Section 8 proves the Igusa values (8.4) and nonreducedness directly. Its finite quotient is supplied by Quotients and torsors, Corollary 4.4 and Theorem 5.2; its projectivity, coherent cohomology and full Picard pullback kernel are established in the construction.

## 12. Sources and historical placement

Grothendieck's [FGA, Exposé 236](https://www.numdam.org/item/SB_1961-1962__7__221_0/) separates local group-scheme structure, Picard smoothness, canonical abelian subschemes, and finiteness. Proposition 2.10(iii) contains the dimension and characteristic-zero smoothness statements; Theorem 3.3 treats the canonical abelian subscheme and Albanese construction; Section 4 concerns boundedness and finite-type Picard loci. The stronger proper-family finiteness statements appear in the later [complement to Exposé 236](https://www.numdam.org/item/SB_1961-1962__7__303_1/) and in the finiteness theorems of Raynaud and Kleiman (1971), which Kleiman, *The Picard scheme*, Section 6, surveys. We keep the field-level deformation proof distinct from those relative finiteness results.

[Kleiman, *The Picard scheme*](https://arxiv.org/abs/math/0504020), Sections 5–6, gives precise component, tangent, smoothness, numerical-equivalence and boundedness formulations. In particular Theorem 5.11, Corollaries 5.13–5.14 and Remark 5.15 provide useful comparisons for Sections 2–5 and the nonreduced example. The numerical discussion distinguishes $\operatorname{Pic}^0$, $\operatorname{Pic}^\tau$, and their quotient.

[Liedtke, *Arithmetic Moduli and Lifting of Enriques Surfaces*](https://arxiv.org/abs/1007.0787v2), Section 1, records the classical, singular and supersingular terminology and the corresponding Picard schemes. Proposition 8.1 proves the Picard calculation from the numerical Enriques conditions. The characteristic-two cases retain both the component group and the infinitesimal identity component.

Cheng, Ji, Larson and Olander, [*Theorem of the Base*](https://chngr.github.io/assets/theorem-of-the-base.pdf), Sections 3–4 and 7, give a modern comparison for regularity, numerical classes and the full proper-family finiteness theorem. Those field and family scopes remain distinct here.

The next lesson replaces ad hoc presentations by the cotangent complex. Its deformation groups extend the same pattern seen here: degree zero records infinitesimal automorphisms, degree one records first-order changes, and degree two records obstructions.

The scheme-recognition comparison for Lemma 1.1 is [Stacks, Group algebraic spaces over fields](https://stacks.math.columbia.edu/tag/0B8D). Its proof here uses dense affine scheme opens, translations, finite field descent and determinant norms. The finite-frame construction retains all global functions, including nilpotents, and uses the exact earlier scheme and stack results linked in the proof.

Linked programme proofs retain their own component licences. In particular, *Moduli stacks are algebraic* is distributed as a GNU FDL 1.2-or-later chapter with separately identified CC0 passages. This lesson's independently written text is dedicated to CC0.
