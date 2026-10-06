# Affine morphisms, relative Spec, and finite morphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

An affine scheme is described by one ring. An affine morphism is described by a ring over each affine open of its base, with those rings agreeing under localization. Relative Spec turns that compatible family back into geometry. It also lets us distinguish two forms of algebraic control: integral elements satisfy monic equations, while a finite algebra has a finite list of module generators.

The sheaf-theoretic prerequisite is the equivalence between modules and quasi-coherent sheaves on an affine scheme, together with restriction, tensor products, and pullback of quasi-coherent sheaves. These belong to *Affine schemes* and *Quasi-coherent sheaves on schemes*, the fourth and ninth lessons of *Sheaves and schemes*. Exact open affine proof providers are [Stacks, Tag 01I7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-compare-constructions) and [Tag 01IA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-quasi-coherent-affine). The ring-theoretic prerequisite is the already written Integral extensions: lying over, going up and going down, especially Theorem 1.2 and Theorems 3.2–3.4. We use the chart descriptions of finite type from Finiteness of morphisms.

## 1. Relative Spec from compatible affine charts

Let \(S\) be a scheme and \(\mathcal A\) a quasi-coherent sheaf of commutative \(\mathcal O_S\)-algebras. Quasi-coherence concerns its underlying module. On an affine open \(U=\operatorname{Spec}R\), it is the sheaf associated to the \(R\)-algebra \(B=\Gamma(U,\mathcal A)\). On \(D(r)\subset U\), its sections are \(B_r\).

**Theorem 1.1 (construction and universal property).** There is a scheme \(\pi:\operatorname{Spec}_S\mathcal A\to S\) with a natural bijection, for every \(g:T\to S\),

\[
\operatorname{Hom}_S(T,\operatorname{Spec}_S\mathcal A)
\cong\operatorname{Hom}_{\mathcal O_T\text{-alg}}(g^*\mathcal A,\mathcal O_T).
\tag{1.1}
\]

For every affine \(U\subset S\),

\[
\pi^{-1}(U)=\operatorname{Spec}\Gamma(U,\mathcal A),
\qquad \pi_*\mathcal O_{\operatorname{Spec}_S\mathcal A}\cong\mathcal A.
\tag{1.2}
\]

The construction commutes with arbitrary base change:

\[
S'\times_S\operatorname{Spec}_S\mathcal A
\cong\operatorname{Spec}_{S'}(h^*\mathcal A)
\quad\text{for }h:S'\to S.
\tag{1.3}
\]

**Proof.** Over \(U=\operatorname{Spec}R\), take \(\operatorname{Spec}B\). Its inverse image over \(D(r)\) is \(\operatorname{Spec}B_r\), exactly the spectrum prescribed by restriction of \(\mathcal A\). For two affine opens of \(S\), their intersection is covered by distinguished opens from either chart. The restriction descriptions identify the two inverse images canonically on this intersection; their restrictions agree on further overlaps. These identifications satisfy the cocycle condition because they all come from the same sheaf algebra. Gluing produces the desired scheme. This construction does not require affine or quasi-compact chart intersections.

On an affine base \(U\), a morphism \(T\to\operatorname{Spec}B\) over \(U\) is an \(R\)-algebra map \(B\to\Gamma(T,\mathcal O_T)\). Such a map determines the sheaf-algebra map in (1.1) by restriction and localization: a base function inverted on an open acts invertibly there, so denominators have their forced images. Conversely, taking global sections after pullback recovers the map from \(B\). The two constructions are inverse on sections over affine opens of \(T\), hence on their sheaves and on \(T\). No quasi-coherence of \(g_*\mathcal O_T\) is required.

For a general base, restrict \(T\) to the inverse images of the chosen affine cover. Both scheme maps and sheaf-algebra maps glue uniquely, so the affine bijections give (1.1). This also proves independence of the chosen cover. In particular, restricting to any other affine open \(U\), the same functor is represented by \(\operatorname{Spec}\Gamma(U,\mathcal A)\). Uniqueness of a representing object proves the first identity of (1.2) for every affine open, not just those used in the original gluing. The second follows on these opens because their section algebras are the same.

Finally, a map to the left side of (1.3) is a map \(g':T\to S'\) together with a map from \((hg')^*\mathcal A\) to \(\mathcal O_T\). Since \((hg')^*\mathcal A=(g')^*h^*\mathcal A\), this is the functor represented by the right side. The natural isomorphism of functors proves (1.3). \(\square\)

The construction and its properties are [Stacks, Tags 01LU and 01LX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-lemma-spec-properties). The algebra homomorphism goes toward functions on the test scheme, whereas its associated geometric morphism goes toward relative Spec.

## 2. Affineness and the algebra over the base

A morphism \(f:X\to S\) is **affine** if the inverse image of every affine open of \(S\) is affine. The source itself need not be affine: the identity of any scheme is an affine morphism.

**Theorem 2.1.** The following are equivalent:

1. \(f\) is affine.
2. There is an affine open cover \((U_i)\) of \(S\) such that every \(f^{-1}(U_i)\) is affine.
3. There is a quasi-coherent algebra \(\mathcal A\) on \(S\) and an isomorphism \(X\cong\operatorname{Spec}_S\mathcal A\) over \(S\).

In that case \(\mathcal A=f_*\mathcal O_X\) canonically. Affineness is local on the target for arbitrary open covers. Affine morphisms are quasi-compact and separated, survive arbitrary base change and composition, and include closed immersions.

**Proof.** The first condition implies the second. Under the second, on each \(U_i=\operatorname{Spec}R_i\), the restriction of \(f_*\mathcal O_X\) is the quasi-coherent algebra associated to the coordinate ring of the affine inverse image. Indeed, on each distinguished \(D(r)\subset U_i\), its sections are the localization of that ring. Quasi-coherence is local, so \(\mathcal A=f_*\mathcal O_X\) is globally quasi-coherent. The identity of this algebra defines a canonical map \(X\to\operatorname{Spec}_S\mathcal A\) by (1.1). It is the usual affine-scheme isomorphism on every inverse image of \(U_i\), hence an isomorphism globally. This proves the third condition. By (1.2), the third implies the first, completing the equivalence without assuming that affineness was already target-local.

If affineness holds over an arbitrary open cover, refine it by affine base opens and apply the equivalence. Quasi-compactness and separatedness follow on affine base charts, where the source is affine and its diagonal is the surjective multiplication map on tensor-product rings. These properties are target-local by the first two lessons. For a base change, affine charts give tensor products of rings, or one may use (1.3). For composition, successively taking inverse images of an affine base open gives an affine scheme at each step. A closed immersion over an affine chart is \(\operatorname{Spec}(R/I)\to\operatorname{Spec}R\), so is affine. \(\square\)

**Corollary 2.2.** The assignments

\[
(X\xrightarrow f S)\longmapsto f_*\mathcal O_X,
\qquad \mathcal A\longmapsto\operatorname{Spec}_S\mathcal A
\]

give an anti-equivalence between affine \(S\)-schemes and quasi-coherent \(\mathcal O_S\)-algebras. It is compatible with arbitrary base change.

**Proof.** Theorem 2.1 and (1.2) give the two identifications on objects. For \(X=\operatorname{Spec}_S\mathcal A\) and \(Y=\operatorname{Spec}_S\mathcal B\), (1.1) and pullback–pushforward adjunction identify maps \(X\to Y\) over \(S\) with algebra maps \(\mathcal B\to f_*\mathcal O_X=\mathcal A\). The correspondence respects identities and composition on affine charts, hence globally. Formula (1.3) proves the base-change assertion. \(\square\)

These are [Stacks, Tags 01S8 and 01SA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-affine-equivalence-algebras). One should not cancel affineness indiscriminately. A useful valid cancellation statement is: if \(X\) is affine over \(S\) and \(Y\) is separated over \(S\), then any \(S\)-map \(X\to Y\) is affine. Its graph into \(X\times_S Y\) is a closed immersion, and the projection \(X\times_S Y\to Y\) is a base change of the affine map \(X\to S\). Their composite is affine. The same proof works when the diagonal of \(Y/S\) is affine; this is [Stacks, Tag 01SG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-affine-permanence).

## 3. Modules under an affine morphism

Let \(f:X\to S\) be affine, and put \(\mathcal A=f_*\mathcal O_X\). An \(\mathcal A\)-module in this section is called quasi-coherent when its underlying \(\mathcal O_S\)-module is quasi-coherent. This agrees with the usual locally presented sheaf-module definition: on an affine base it is a module over the section algebra, with an arbitrary free presentation; conversely, presentations by sums of \(\mathcal A\) give quasi-coherent underlying modules.

**Theorem 3.1.** Pushforward gives an equivalence

\[
\operatorname{QCoh}(X)
\xrightarrow{\;f_*\;}
\operatorname{QCoh}_{\mathcal A}(S).
\tag{3.1}
\]

A quasi-inverse sends \(\mathcal M\) to

\[
f^*\mathcal M\otimes_{f^*\mathcal A}\mathcal O_X,
\tag{3.2}
\]

where the algebra map \(f^*\mathcal A\to\mathcal O_X\) is the evaluation map. In particular, \(f_*\) is exact on quasi-coherent modules.

**Proof.** On \(U=\operatorname{Spec}R\subset S\), write \(f^{-1}(U)=\operatorname{Spec}B\). A quasi-coherent sheaf on this inverse image is \(\widetilde N\) for a \(B\)-module \(N\). Its pushforward on \(U\) is the sheaf of the same module, viewed as an \(R\)-module with its retained \(B\)-action: over \(D(r)\) the sections are \(N_r\). Thus pushforward is quasi-coherent and has the stated algebra action.

An \(\mathcal A\)-module \(\mathcal M\) restricts on \(U\) to a \(B\)-module \(M\). Formula (3.2) has chart module

\[
(B\otimes_R M)\otimes_{B\otimes_R B}B.
\]

The map \((b\otimes m)\otimes c\mapsto bcm\) is an isomorphism to \(M\); its inverse sends \(m\) to \((1\otimes m)\otimes1\). The tensor relations verify both compositions, including the relation that the second \(B\)-factor acts on \(M\). This gives the inverse on chart objects and on homomorphisms. Both constructions commute with localization in \(R\), so these chart equivalences glue and their identity maps glue. Finally, restriction of scalars from \(B\) to \(R\) preserves exact sequences, proving exactness on every affine base chart and hence on \(S\). \(\square\)

This is [Stacks, Tag 01SB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-affine-equivalence-modules). The right-hand side retains the \(\mathcal A\)-action. Forgetting that action would lose the information needed to reconstruct a sheaf on \(X\).

## 4. Integral and finite morphisms

An affine morphism is **integral** if, over every affine \(U=\operatorname{Spec}R\subset S\), its coordinate algebra is integral over \(R\). It is **finite** if that algebra is finite as an \(R\)-module. Neither definition assumes Noetherianity. Finiteness refers to module generators, not merely algebra generators.

We recall the precise algebraic inputs from *Integral extensions: lying over, going up and going down*. Theorem 1.1 characterizes an integral element by finiteness of its generated subalgebra. Theorem 1.2 proves closure and transitivity of integrality and the equivalence “finite algebra = integral algebra of finite type”. Its proof uses bounded powers in monic equations and the determinant argument on a finite module. Proposition 1.3 proves quotient and localization stability and tensor-product stability for finite modules.

**Lemma 4.1 (patching module finiteness).** If \(D(r_1),\ldots,D(r_n)\) cover \(\operatorname{Spec}R\), an \(R\)-module \(M\) is finite whenever every \(M_{r_i}\) is finite. An \(R\)-algebra \(B\) is integral whenever every \(B_{r_i}\) is integral over \(R_{r_i}\).

**Proof.** Lift finitely many generators of each \(M_{r_i}\) to elements of \(M\), clearing their denominators, and let \(N\) be their finite \(R\)-span. Each localization of \(M/N\) is zero. Any element of this quotient is killed by some power of each \(r_i\). Those powers generate the unit ideal, since their distinguished opens still cover the spectrum. The element is zero. Thus \(M=N\).

For the algebra assertion fix \(b\in B\). The algebra \(R[b]\) becomes a finite module after each localization by the integral-element test. The module assertion makes \(R[b]\) finite, so the same test makes \(b\) integral. \(\square\)

**Theorem 4.2.** Integrality and finiteness are local on the target for arbitrary open covers, and survive arbitrary base change and composition. A morphism is finite if and only if it is integral and locally of finite type.

**Proof.** If either property holds over a target cover, Theorem 2.1 first makes the morphism affine. On any affine base open refine its intersection with that cover by finitely many distinguished opens. On each, the required integral or finite ring-map property holds; Lemma 4.1 proves it on the whole affine open. This gives target locality and also shows that restrictions to arbitrary base opens retain the property.

For finite base change, tensor the finite list of module generators. For integral base change, every generator \(b\otimes1\) remains integral by its same monic equation. Every element of the tensor product is a finite sum of multiples of such elements; integral elements form a subalgebra by the recalled Theorem 1.2. Thus the base-changed algebra is integral. Affineness survives base change, so these ring calculations prove the scheme assertions.

For composition of finite algebras, products of module generators give a finite list over the first ring. Composition of integral algebras is integral by transitivity. Together with affine composition, this proves the morphism assertions. Finally, an integral and locally finite type morphism has finite type algebras on its affine charts, hence finite algebras by the recalled equivalence. Conversely, a finite algebra is integral and its module generators are algebra generators, giving local finite type. \(\square\)

The corresponding sources are [Stacks, Tags 02K8, 01WI, and 01WJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-integral). An infinite algebraic field extension gives an integral morphism which is not finite. In the other direction, a finite morphism need not be of finite presentation: \(\operatorname{Spec}(R/I)\to\operatorname{Spec}R\) is finite for every ideal \(I\), including infinitely generated ideals whose quotient is not finitely presented.

## 5. Closed images and fibres

**Theorem 5.1.** An integral morphism is universally closed. Every point in a fibre of an integral morphism is closed in that fibre. A finite morphism has finitely many points in each fibre, with finite residue-field extensions of the base residue field.

**Proof.** For an integral ring map \(R\to B\) and any ideal \(J\subset B\), the injection \(R/(J\cap R)\to B/J\) is integral. Lying over, proved in the internal algebra lesson’s Theorem 3.2, gives

\[
\operatorname{image}(\operatorname{Spec}(B/J)\to\operatorname{Spec}R)
=V(J\cap R).
\tag{5.1}
\]

Thus every closed subset has closed image. Closedness is local on the target as a topological assertion, so affine charts prove that an integral morphism is closed. Its arbitrary base changes are integral by Theorem 4.2, hence closed too.

A fibre over \(s\in S\) is the spectrum of an algebra integral over \(\kappa(s)\). Each prime quotient is a domain integral over a field and therefore a field. To check the latter assertion directly, a nonzero integral element has a monic equation with nonzero constant term after canceling any trailing power of that element; solving the equation for its inverse puts that inverse in the domain. Thus every prime is maximal and every point is closed.

For a finite morphism the fibre algebra \(C\) is finite-dimensional over \(\kappa(s)\). Its prime quotients are finite-dimensional fields. It has finitely many maximal ideals: for any \(n\) distinct maximal ideals, the Chinese remainder theorem surjects \(C\) onto the product of their residue fields, whose vector-space dimension is at least \(n\). Thus \(n\leq\dim_{\kappa(s)}C\). This bounds the number of points and proves finiteness of their residue-field extensions. The fibre may have nilpotents. \(\square\)

These are [Stacks, Tags 01WM and 02NT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-integral-universally-closed) and the finite-fibre consequence at [Tag 02NU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-quasi-finite). Integral does not imply finitely many fibre points. For example, \(B=\prod_{n\geq1}\mathbf F_2\) is integral over \(\mathbf F_2\), because every element satisfies \(T^2-T=0\). The coordinate projections have infinitely many distinct prime kernels. All points of its spectrum are closed, as the theorem predicts.

Finite morphisms are separated by affineness, of finite type by Theorem 4.2 and quasi-compactness, and universally closed by Theorem 5.1. These are precisely the three conditions in the definition of a proper morphism. Properness will be developed further in its own lesson; the finite case already follows from the results here.

## 6. Three affine calculations

The squaring map \(\mathbf A^1_k\to\mathbf A^1_k\) corresponds to \(k[y]\to k[x]\), \(y\mapsto x^2\). As a module the latter ring is free with basis \(1,x\): separate even and odd powers. Hence the map is finite. Over a \(k\)-rational value \(a\), the scheme fibre is \(\operatorname{Spec}k[x]/(x^2-a)\). Its points and nilpotents are calculated in Exercise 7.1.

For the cusp, use \(A=k[t^2,t^3]\subset B=k[t]\). The fraction fields agree, since \(t=t^3/t^2\), and \(t\) is integral over \(A\). Thus \(B=A+At\) is finite over \(A\). The polynomial ring \(k[t]\) is integrally closed, so it is the integral closure of \(A\) in their fraction field: an element integral over \(A\) is also integral over \(B\) and must belong to \(B\). Conversely every element of \(B\) is integral over \(A\). This computes the normalization of the cusp \(y^2=x^3\). The fibre over its origin is \(\operatorname{Spec}k[t]/(t^2)\), one nonreduced point.

For an irreducible node assume \(\operatorname{char}k\ne2\), and put

\[
x=u^2-1,\qquad y=u(u^2-1),\qquad
A=k[x,y]\subset k[u]=B.
\]

The relation is \(y^2=x^2(x+1)\). The map from its plane coordinate ring to \(B\) is injective: as a polynomial in \(y\), this equation is irreducible over \(k(x)\), since \(x+1\) is not a square there; the parametrization gives the corresponding embedding of its fraction field. Also \(u=y/x\) in that field and \(u^2=x+1\). Thus \(B=A+Au\) is finite with the same fraction field, and its normality again proves that it is the normalization. The fibre at \((x,y)=(0,0)\) is \(k[u]/(u^2-1)\cong k\times k\): the two branches have separated into two reduced points, \(u=1\) and \(u=-1\).

Finally, \(\mathbf A^1_k\setminus\{0\}\to\mathbf A^1_k\) is affine, since its ring is \(k[t,t^{-1}]\). It is not integral: a monic equation for \(t^{-1}\), multiplied by a suitable power of \(t\), would put \(1\) in \((t)\subset k[t]\). Hence it is not finite. By contrast, the punctured plane inclusion is not even affine; Exercise 7.3 computes its functions and explains the obstruction.

## 7. Exercises with solutions

**Exercise 7.1 (easy: squaring fibres).** Describe the fibre of the squaring map over a \(k\)-rational \(a\), including its scheme structure, in characteristic two and in other characteristics. Also describe the geometric fibres.

**Solution.** The fibre algebra is \(k[x]/(x^2-a)\). If the characteristic is not two and \(a\ne0\), the polynomial is separable. If \(a\) is a square in \(k\), its distinct roots give two reduced \(k\)-points; otherwise it is irreducible and gives one point with a separable quadratic residue field. At \(a=0\) it is \(k[x]/(x^2)\), a double point. In characteristic two, if \(a=b^2\) the algebra is \(k[\epsilon]/(\epsilon^2)\), with \(x=b+\epsilon\). If \(a\) is not a square it is a purely inseparable quadratic field extension, so is reduced over \(k\) but becomes nonreduced after extending to an algebraic closure. Over an algebraic closure all characteristic-two fibres are double points; in other characteristics the nonzero geometric fibres are two reduced points and the zero fibre is a double point. All have algebra dimension two.

**Exercise 7.2 (medium: locality without circularity).** Suppose an open cover \((V_i)\) of \(S\) has the property that each restricted morphism \(f^{-1}(V_i)\to V_i\) is affine. Prove that \(f\) is affine, indicating how arbitrary affine opens of \(S\) are handled.

**Solution.** Refine the \(V_i\) by affine opens \(U_j\). Their inverse images are affine by the given affineness over \(V_i\). The local section and localization calculation makes \(\mathcal A=f_*\mathcal O_X\) quasi-coherent on each \(U_j\), hence globally. The identity of \(\mathcal A\) gives a map to \(\operatorname{Spec}_S\mathcal A\) which is an isomorphism over each \(U_j\); therefore it is an isomorphism. The relative Spec universal property, already proved before target locality, gives its restriction over every affine \(U\subset S\) as \(\operatorname{Spec}\Gamma(U,\mathcal A)\). Thus every affine inverse image is affine. Merely knowing this for the original chosen cover would not have established the definition without that last argument.

**Exercise 7.3 (medium: the punctured plane).** Show that \(U=\mathbf A^2_k\setminus\{(0,0)\}\) is not affine, and hence that its inclusion in \(\mathbf A^2_k\) is not an affine morphism.

**Solution.** Put \(R=k[x,y]\). The cover \(U=D(x)\cup D(y)\) identifies its functions with

\[
\Gamma(U,\mathcal O_U)=R_x\cap R_y=R
\]

inside \(k(x,y)\). For the intersection equality, if \(p/x^n=q/y^m\), then \(y^mp=x^nq\). Since \(x\) and \(y\) are relatively prime prime elements, \(x^n\mid p\), and the fraction is a polynomial. If \(U\) were affine, its canonical map to \(\operatorname{Spec}\Gamma(U,\mathcal O_U)=\mathbf A^2_k\) would be an isomorphism. That canonical map is the original inclusion, since its coordinate functions are \(x,y\). It misses the origin and cannot be an isomorphism. Since the entire target is affine, an affine inclusion would require \(U\) itself to be affine.

**Exercise 7.4 (medium: universal closedness).** Let \(f:X\to S\) be integral and let \(S'\to S\) be any morphism. Show explicitly that every closed subset of \(X\times_S S'\) has closed image in \(S'\), without assuming an integral map is injective.

**Solution.** Restrict to an affine \(\operatorname{Spec}R'\subset S'\), on which the base-changed source is \(\operatorname{Spec}B'\) and \(R'\to B'\) is integral by Theorem 4.2. A closed subset is \(V(J)\). The map \(R'/(J\cap R')\to B'/J\) is injective and integral; lying over applies to this injection and gives image \(V(J\cap R')\). Closedness on an open cover implies closedness in \(S'\). This proves universal closedness for arbitrary base change. For the empty closed subset, \(J=B'\), and the formula correctly gives the empty subset. Replacing the image by the whole base spectrum without removing the kernel would have been incorrect.

**Exercise 7.5 (hard: a finite monomorphism).** Show that a finite morphism which is a monomorphism is a closed immersion. No Noetherian or finite-presentation hypothesis may be added.

**Solution.** Work on an affine target \(\operatorname{Spec}R\), whose inverse image is \(\operatorname{Spec}B\) with \(B\) finite over \(R\). A monomorphism has an isomorphism as its diagonal, by its defining universal property. Thus multiplication \(B\otimes_R B\to B\) is an isomorphism. Let \(C\) be the cokernel of \(R\to B\) as an \(R\)-module. Tensoring \(R\to B\to C\to0\) with \(B\), the first map becomes \(B\to B\otimes_R B\), inverse to multiplication. Hence \(C\otimes_R B=0\). Since \(B\to C\) is surjective, right exactness gives \(C\otimes_R C=0\).

If the finite module \(C\) were nonzero, choose a maximal ideal \(\mathfrak m\) containing its annihilator. Then \(C_{\mathfrak m}\ne0\): otherwise one element outside \(\mathfrak m\) would kill all its finitely many generators and belong to its annihilator. Nakayama’s finite-module argument gives \(V=C\otimes_R\kappa(\mathfrak m)\ne0\). Explicitly, if \(C_{\mathfrak m}=\mathfrak mC_{\mathfrak m}\), a matrix with entries in the maximal ideal expressing its generators in terms of themselves has \(\det(I-M)\) a unit; the adjugate makes that unit annihilate the generators, forcing the module to be zero. But

\[
(C\otimes_R C)\otimes_R\kappa(\mathfrak m)
\cong V\otimes_{\kappa(\mathfrak m)}V\ne0,
\]

contradicting \(C\otimes_R C=0\). Thus \(C=0\) and \(R\to B\) is surjective. The chart map is a closed immersion, and these quotient descriptions glue on the target. This proves the assertion, [Stacks, Tag 03BB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-monomorphism-closed). Finiteness matters in choosing the annihilating element and applying the finite-module argument. A bijection on geometric points alone would not give the diagonal isomorphism used here.

## Sources and proof dependencies

The primary reference is *The Stacks project*, read in the AI Integrated Stacks Project edition: relative Spec at Tags 01LU and 01LX; affine morphisms and the two category equivalences at 01S8, 01SA and 01SB; integral and finite morphisms at 02K8, 01WI–01WM, 02NT and 02NU; finite monomorphisms at 03BB. All assigned morphism results and all exercise solutions are proved in this lesson.

The written internal algebra provider is *Integral extensions: lying over, going up and going down*, in *Commutative algebra for geometry*: Theorems 1.1–1.2 give integral-element tests, closure and transitivity; Proposition 1.3 gives quotient and localization stability; Proposition 2.3 gives polynomial normality; Theorem 3.2 gives lying over. The sheaf providers and exact available open affine proofs are named in the introduction. Those open source texts retain their GNU Free Documentation License; none is copied here. Further exposition consulted is Ravi Vakil’s *The Rising Sea*, §§8.3 and 17.1. This lesson’s expression is independent CC0 material.
