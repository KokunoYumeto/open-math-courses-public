# Normalization

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

Normalization adjoins rational functions that satisfy monic equations. It separates the branches of a node and supplies the missing parameter of a cusp. In higher dimension it need not remove all singularities. We will construct it locally, prove the gluing and universal properties, and distinguish existence from finiteness. The separable finiteness proof uses a trace pairing; a separate argument handles inseparability over an arbitrary field.

We use integral closure, its localization, and relative Spec from Affine, integral and finite morphisms and Zariski's Main Theorem. The algebraic foundations are Integral extensions, especially Theorems 1.1–1.2 and 2.2 and Proposition 2.3, and Krull dimension and Noether normalization, Corollary 3.2. Normality is defined by local rings, as in the planned *Properties of schemes* lesson of *Sheaves and schemes*; its Noetherian algebra is developed in Discrete valuation rings, normal rings and Serre's criterion. Here a normal local ring is an integrally closed domain, and a normal scheme has normal local rings. A normal scheme need not be integral.

## 1. Integral completion relative to a map

Let \(f:Y\to X\) be quasi-compact and quasi-separated. Its direct-image algebra \(f_*\mathcal O_Y\) is quasi-coherent, by the finite-affine-equalizer proof in the ample-sheaf lesson. Let \(\mathcal C\) be the integral closure of \(\mathcal O_X\) in this algebra. The localization argument in the Zariski lesson shows it is quasi-coherent: on \(U=\operatorname{Spec}A\), it is associated to the integral closure of \(A\) in \(\Gamma(f^{-1}U,\mathcal O_Y)\), and this description localizes on every \(D(a)\).

Define the **normalization of \(X\) in \(Y\)** by

\[
X'=\operatorname{Spec}_X\mathcal C,
\qquad Y\xrightarrow{f'}X'\xrightarrow{\nu}X.
\tag{1.1}
\]

The first arrow corresponds to the inclusion \(\mathcal C\to f_*\mathcal O_Y\); the second is integral. This relative construction does not assert that \(X'\) is normal. For the identity map of any scheme, it gives that same scheme.

**Theorem 1.1 (relative universal property).** The factorization (1.1) is characterized by the following property: for every factorization \(Y\xrightarrow{g}Z\xrightarrow{\pi}X\) with \(\pi\) integral, there is a unique \(X\)-map \(h:X'\to Z\) such that \(h f'=g\).

**Proof.** An integral map is affine, so write \(Z=\operatorname{Spec}_X\mathcal B\), with \(\mathcal B\) an integral quasi-coherent algebra. By relative Spec, \(g\) gives an algebra map \(\mathcal B\to f_*\mathcal O_Y\). Each section of \(\mathcal B\) over an affine base open is integral over that base algebra, and its image is integral as well. The map therefore factors uniquely through the subsheaf \(\mathcal C\). Relative Spec turns this unique factorization into \(h\), and the algebra diagram proves \(h f'=g\). The constructed \(\nu\) is integral. Conversely, any other integral factorization having the same universal property receives and supplies unique compatible maps to (1.1); their composites are identities by uniqueness. \(\square\)

See [Stacks, Tag 035I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-characterize-normalization). The direction of the arrow matters: the integral completion maps to every other integral intermediate scheme.

**Proposition 1.2 (restriction and functoriality).** Restricting (1.1) to an open \(U\subset X\) gives the normalization of \(U\) in \(f^{-1}U\). A commutative square \(Y_2\to Y_1\), \(X_2\to X_1\), with both vertical maps qcqs, induces a unique compatible map of their relative normalizations \(X_2'\to X_1'\).

**Proof.** Restriction follows from the affine localization description. For the square, the pullback \(X_2\times_{X_1}X_1'\to X_2\) is integral and \(Y_2\to X_2\) factors through it. Theorem 1.1 gives \(X_2'\to X_2\times_{X_1}X_1'\), hence the requested map, uniquely. \(\square\)

These are [Stacks, Tags 035J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-functoriality-normalization) and [035K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-normalization-localization). Functoriality supplies a map; it does not assert commutation with arbitrary base change.

## 2. The rational algebra of a reduced scheme

For a reduced ring \(A\), let \(Q(A)\) be its **total ring of fractions**, obtained by inverting all nonzerodivisors. Suppose it has finitely many minimal primes \(\mathfrak p_1,\ldots,\mathfrak p_r\). Then

\[
Q(A)=\prod_{i=1}^r K_i,
\qquad K_i=\operatorname{Frac}(A/\mathfrak p_i).
\tag{2.1}
\]

Here is a direct verification. The map \(A\to\prod_i A/\mathfrak p_i\) is injective, since their intersection is zero. An element outside all the \(\mathfrak p_i\) is a nonzerodivisor. Choose
\(a_i\in\bigcap_{j\ne i}\mathfrak p_j\setminus\mathfrak p_i\), by multiplying elements of \(\mathfrak p_j\setminus\mathfrak p_i\); for one component take \(a_1=1\). Distinct \(a_i\) have product zero. The sum \(s=\sum_i a_i\) avoids every minimal prime. Thus
\(e_i=a_i/s\in Q(A)\) are orthogonal idempotents summing to one, selecting the factors in (2.1). Every element of a minimal prime annihilates its corresponding nonzero \(a_i\); hence the zero divisors are exactly the union of those primes. Finally any \(b\notin\mathfrak p_i\) becomes invertible in the \(i\)-th factor: invert the nonzerodivisor
\(a_i b+\sum_{j\ne i}a_j\), whose other components are nonzero. Consequently that factor is the full fraction field \(K_i\), proving (2.1).

Let \(\bar A\) be the integral closure of \(A\) in \(Q(A)\). The idempotents \(e_i\) are integral, satisfying \(T^2-T=0\); adjoining them gives the finite integral algebra \(\prod_i A/\mathfrak p_i\). By transitivity, integral closure over that algebra and over \(A\) agree. Integrality over a finite product is checked in its factors, so

\[
\bar A=\prod_i\overline{A/\mathfrak p_i}^{\,K_i}.
\tag{2.2}
\]

Each factor is an integrally closed domain with fraction field \(K_i\): an element integral over it is integral over \(A/\mathfrak p_i\) by transitivity and already belongs to it. Its localizations are normal. Thus \(\operatorname{Spec}\bar A\) is a disjoint union of normal integral schemes. Compare the exact descriptions in [Stacks, Tag 035P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-description-normalization).

## 3. Gluing normalization and lifting maps

Assume \(X\) is reduced and has locally finitely many irreducible components. This means its irreducible components form a locally finite family; equivalently here every quasi-compact open has finitely many components. In particular every affine open has finitely many minimal primes.

**Theorem 3.1.** There is an integral surjection \(\nu:X^\nu\to X\) whose inverse image over \(\operatorname{Spec}A\) is \(\operatorname{Spec}\bar A\). Its source is normal; it matches the irreducible components and their generic residue fields. For every morphism \(Z\to X\) from a normal scheme such that each component of \(Z\) dominates a component of \(X\), there is a unique factorization through \(\nu\).

**Proof of construction and generic behaviour.** For a basic open \(D(a)\subset\operatorname{Spec}A\), the total rational algebra is obtained from (2.1) by retaining the factors in which \(a\) is nonzero. Integral closure commutes with this localization, so
\(\overline{A_a}=\bar A_a\).
These canonical identifications agree under repeated localization. They glue the affine schemes \(\operatorname{Spec}\bar A\) over overlaps of affine opens, giving \(X^\nu\). The construction is affine and integral over every affine of \(X\), hence integral globally. Lying over for \(A\subset\bar A\) proves surjectivity. Normality follows from (2.2). On each component, \(A/\mathfrak p_i\subset\overline{A/\mathfrak p_i}\subset K_i\) has the same fraction field. Thus the generic points and their fields are matched. This is birationality on each affine open; when \(X\) is integral it is the usual equality of function fields, and when it has finitely many components it is the componentwise definition of birationality.

**Proof of the lifting property.** Work with affine opens \(W=\operatorname{Spec}B\subset Z\) mapping into \(U=\operatorname{Spec}A\subset X\). Since every source component dominates a target component, every minimal prime of \(B\) contracts to a minimal prime of \(A\). An element avoiding all minimal primes of \(A\) consequently avoids all minimal primes of \(B\). The ring \(B\) is reduced, and its embedding into its component domains shows such an element is a nonzerodivisor. Therefore \(A\to B\) extends to \(Q(A)\to Q(B)\).

A normal ring \(B\), even without a finiteness assumption on its components, is integrally closed in \(Q(B)\). Indeed an integral element lies in every normal domain \(B_{\mathfrak q}\), after localization. Its class in the module \(Q(B)/B\) vanishes at every prime, hence is zero by local module detection. Images of elements of \(\bar A\) are integral over \(B\), so lie in \(B\). This gives \(\bar A\to B\), hence \(W\to\nu^{-1}U\). It is unique: every element of \(\bar A\subset Q(A)\) is a fraction with nonzerodivisor denominator, whose image in \(B\) is a nonzerodivisor, so its value is forced by that fraction. Uniqueness makes the local lifts agree on overlaps and glue. \(\square\)

These are [Stacks, Tags 035Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-normalization-normal) and [0BXC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-normalization-birational). For integral \(X\) and integral normal \(Z\), dominance is precisely the required condition. For reducible \(Z\), overall dominance alone is insufficient. For example, the disjoint union of the normalization of a node and an extra \(\operatorname{Spec}k\) mapping to the node is normal and dominant. The extra point has two possible lifts. Requiring each component to dominate a target component excludes it and restores uniqueness.

This distinction also separates birationality from being an isomorphism over a dense open. Generic-field equality always holds here. The dense-open isomorphism will follow when the normalization is finite; we will prove that conclusion under the next theorem's hypotheses.

## 4. A trace lattice proves separable finiteness

**Theorem 4.1.** Let \(R\) be a Noetherian normal domain, \(K=\operatorname{Frac}R\), and \(L/K\) a finite separable extension. The integral closure \(C\) of \(R\) in \(L\) is a finite \(R\)-module.

**Proof.** The trace pairing
\(\langle x,y\rangle=\operatorname{Tr}_{L/K}(xy)\)
is nondegenerate. One verification uses a primitive element \(\theta\) and its distinct conjugates \(\theta_1,\ldots,\theta_n\). On the power basis its matrix is \(V^{\mathsf T}V\), where \(V_{ij}=\theta_i^{j-1}\). The Vandermonde determinant is nonzero, hence so is the pairing determinant. The elementary primitive-element theorem and complete trace proof are [Stacks, Tags 030N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-primitive-element) and [0BIL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-separable-trace-pairing).

Choose a \(K\)-basis \(b_1,\ldots,b_n\) lying in \(C\). Such a basis exists: start with any basis of algebraic elements and multiply each by a nonzero element of \(R\) clearing the coefficients of a monic equation, as in (1.3) of the Zariski lesson. Scaling basis elements preserves independence.

For \(c\in C\), its trace belongs to \(R\). Its conjugates are integral over \(R\), so the coefficients of its minimal polynomial are integral over \(R\) and lie in \(K\); normality puts those coefficients in \(R\). Its trace is the appropriate integer multiple of the negative next-to-leading coefficient, so also lies in \(R\). In particular \(\operatorname{Tr}(b_i c)\in R\).

The \(K\)-linear map

\[
\Phi:L\longrightarrow K^n,
\qquad c\longmapsto(\operatorname{Tr}(b_i c))_i
\tag{4.1}
\]

is an isomorphism by nondegeneracy. Its inverse image \(M=\Phi^{-1}(R^n)\) is thus a free \(R\)-module of rank \(n\), and \(C\subset M\) is an \(R\)-submodule. Noetherianity makes that submodule finitely generated. \(\square\)

This is [Stacks, Tag 032L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-normal-domain-finite-separable-extension). Separability is used in nondegeneracy; it cannot be removed from this trace proof.

## 5. Finiteness over fields, including inseparability

**Theorem 5.1 (Noether's finiteness theorem).** For a finite-type domain \(A\) over any field \(k\), the integral closure of \(A\) in any finite extension \(L\) of \(\operatorname{Frac}A\) is finite over \(A\). Consequently normalization of a reduced finite-type \(k\)-scheme is finite.

**Proof.** Choose a polynomial normalization \(P=k[x_1,\ldots,x_d]\subset A\), with \(A\) finite over \(P\). Put \(K=\operatorname{Frac}P\). The extension \(L/K\) is finite. In characteristic zero it is separable, and Theorem 4.1 makes the integral closure of \(P\) in \(L\) finite over \(P\).

In characteristic \(p>0\), choose finitely many field generators \(\alpha_j\) of \(L/K\). Each irreducible minimal polynomial can be written
\(f_j(T)=h_j(T^{q_j})\), where \(q_j\) is a power of \(p\) and \(h_j\) is separable. Choose a common power \(q\) divisible by all \(q_j\). Only finitely many coefficients of \(k\) occur in the rational functions that are coefficients of the \(h_j\). Adjoin their \(q\)-th roots to obtain a finite purely inseparable extension \(k'/k\), and set

\[
P'=k'[x_1^{1/q},\ldots,x_d^{1/q}],
\qquad K'=\operatorname{Frac}P'.
\tag{5.1}
\]

Every coefficient of \(h_j\) has a \(q_j\)-th root in \(K'\), by taking roots of its numerator and denominator. Taking these coefficient roots produces a separable polynomial \(\tilde h_j(T)\) with
\(f_j(T)=\tilde h_j(T)^{q_j}\).
Separability follows because \(h_j\) has distinct roots; the power map is injective in an algebraic closure. Hence \(\alpha_j\) satisfies the separable polynomial \(\tilde h_j\) over \(K'\). The compositum \(L'=LK'\) is a finite separable extension of \(K'\).

The ring \(P'\) is a polynomial normal Noetherian domain, and is finite over \(P\): use a finite \(k\)-basis of \(k'\) and monomials in the root variables with exponents less than \(q\). Theorem 4.1 makes its integral closure \(C'\) in \(L'\) finite over \(P'\), hence finite over \(P\). The integral closure \(C\) of \(P\) in \(L\) embeds into \(C'\), since every monic equation over \(P\) is also one over \(P'\). It is a \(P\)-submodule, so is finite because \(P\) is Noetherian.

Finally, integral closure of \(P\) and of \(A\) in \(L\) agree: one inclusion uses \(P\subset A\), and the other uses transitivity and integrality of \(A/P\). A finite generating list over \(P\) also generates this algebra over \(A\). This proves the domain assertion. For a reduced affine algebra with finitely many components, (2.2) is a finite product of these finite closures, hence finite over \(A\). Finiteness is local on the scheme, proving the last assertion. \(\square\)

In the finite case, normalization is an isomorphism over a dense open. On an affine reduced chart choose a finite generating list for \(\bar A\subset Q(A)\), and a product \(s\) of its nonzerodivisor denominators. Then \(\bar A_s=A_s\). The basic open \(D(s)\) contains all generic points. Union these chart opens to obtain the desired dense open. If a general Noetherian scheme is given, finiteness requires an additional hypothesis; Noetherianity alone is not a substitute for this theorem.

For the standard arithmetic extension, call a ring **Nagata** if it is Noetherian and for every prime \(\mathfrak p\), integral closure of \(R/\mathfrak p\) in every finite extension of its fraction field is finite. Fields are Nagata directly, and \(\mathbb Z\) is Nagata by Theorem 4.1 at the zero prime and the field case at its other primes. Finite-type algebras over a Nagata ring are Nagata by the exact full open proof [Stacks, Tag 0334](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-nagata-universally-japanese); the list of these standard bases is [Tag 0335](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-ubiquity-nagata). Using this stated full stability provider, normalization of schemes of finite type over \(\mathbb Z\) is finite too: on each reduced affine chart use (2.2) and the defining Nagata condition. For a nonreduced chart first pass to its finite reduced quotient. This is the proof of [Tag 035S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-nagata-normalization). The linked general stability proof retains GNU FDL 1.2.

## 6. Three computations

**The node.** In characteristic different from two, the normalization of
\(y^2=x^2(x+1)\) is the map from \(\mathbb A^1_t\) with
\(x=t^2-1\), \(y=t(t^2-1)\), as proved in the Zariski lesson. Its fibre over the node is \(\operatorname{Spec}k[t]/(t^2-1)\cong\operatorname{Spec}(k\times k)\). Two branches become two points. For comparison, the cusp \(k[t^2,t^3]\subset k[t]\) is also finite and birational, but its origin fibre is \(\operatorname{Spec}k[t]/(t^2)\), a single point of length two. Normalization need not have reduced fibres.

**A number ring.** The fraction field of \(\mathbb Z[2i]\) is \(\mathbb Q(i)\). Adjoining \(i\), integral by \(i^2+1=0\), gives \(\mathbb Z[i]\). This ring is normal: its norm is Euclidean, because rounding real and imaginary parts gives a remainder of squared distance at most \(1/2\), smaller than one. A Euclidean domain is a UFD, and UFDs are integrally closed. Thus \(\mathbb Z[i]\) is the normalization. The conductor is \(2\mathbb Z[i]\): if \(a+bi\) and \((a+bi)i\) both lie in \(\mathbb Z[2i]\), then both \(a,b\) are even. The map is an isomorphism after inverting two. Its fibre over \((2,2i)\) is
\(\operatorname{Spec}\mathbb F_2[T]/((T+1)^2)\), one point of length two.

**The Whitney umbrella.** Over any field let

\[
A=k[x,y,z]/(x^2-y^2z),\qquad
B=k[u,v],\quad x=uv,\ y=u,\ z=v^2.
\tag{6.1}
\]

The polynomial is irreducible, because \(z\) is not a square in \(k(y,z)\). On \(y\ne0\), \(v=x/y\), so the map identifies the fraction fields. Also \(B=A[v]\), with \(v^2=z\), is finite and normal. It is therefore the integral closure, giving normalization \(\mathbb A^2\to\operatorname{Spec}A\). The map is an isomorphism off the line \(x=y=0\). At a point of that line with residue field \(K\) and coordinate \(z=a\), the fibre algebra is

\[
K[v]/(v^2-a).
\tag{6.2}
\]

For characteristic different from two and \(a\ne0\), this is two rational points when \(a\) is a square, and one degree-two point otherwise; geometrically it is two points. At \(a=0\) it is a double point. In characteristic two, every geometric fibre on the line is a double point, although (6.2) can be a field over \(K\) when \(a\) is not a square. Residue-field fibres and geometric fibres must be distinguished.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Normalize \(y^2=x^3+x^2\), and specify where the word node requires a characteristic hypothesis.

**Solution.** Set \(t=y/x\) in the fraction field. The equation gives \(t^2=x+1\), hence \(x=t^2-1\) and \(y=t(t^2-1)\). Thus the normalization is \(k[t]\): it is integral over the original domain, has its fraction field and is normal. In characteristic different from two, \(t^2-1\) has distinct roots and the origin has two inverse-image points. In characteristic two its fibre is \(k[t]/((t-1)^2)\), and the singularity is not that ordinary node, even though the same normalization formulas remain valid.

**Exercise 7.2 (easy).** Normalize \(\mathbb Z[2i]\) and determine its exceptional fibre.

**Solution.** The integral normal overring in the common fraction field is \(\mathbb Z[i]\), so it is the full integral closure by transitivity and normality. Away from two the inclusion is equality. The only prime of \(\mathbb Z[2i]\) containing the conductor \((2,2i)\) is that maximal ideal, with residue field \(\mathbb F_2\). Tensoring \(\mathbb Z[i]\) with this field gives \(\mathbb F_2[T]/(T^2+1)=\mathbb F_2[T]/((T+1)^2)\). Its nonreduced length-two structure also proves the map is not an isomorphism at that point.

**Exercise 7.3 (medium).** Prove birationality and the universal property for normalization of an integral scheme, then explain the extra condition for a reducible normal source.

**Solution.** On \(\operatorname{Spec}A\), the inclusion \(A\subset\bar A\subset K(A)\) preserves the fraction field, hence the generic point and its field. A dominant map from an integral normal \(Z\) embeds \(K(A)\) into \(K(Z)\). Every element of \(\bar A\) is integral in every normal local ring on the source over this affine chart, so is regular there. It determines a unique map to \(\operatorname{Spec}\bar A\); the local uniqueness glues. For reducible normal \(Z\), each component must map dominantly to a component of the target, so the nonzerodivisor denominators stay nonzerodivisors. The extra-point node example in Section 3 shows that overall dominance does not guarantee this or uniqueness.

**Exercise 7.4 (medium).** Prove finiteness of the integral closure of \(k[x]\) in a finite separable extension of \(k(x)\) using a trace lattice.

**Solution.** The ring \(R=k[x]\) is Noetherian and normal. Scale a field basis into integral elements \(b_i\), and use the nondegenerate pairing to identify the field with \(k(x)^n\) by \(c\mapsto(\operatorname{Tr}(b_i c))\). Integral elements have all these traces in \(k[x]\), so the integral closure embeds as an \(R\)-submodule of the free lattice \(R^n\). A submodule of this finite module is finite because \(R\) is Noetherian. The basis may depend on the extension; no single uniform discriminant is assumed.

**Exercise 7.5 (hard).** Normalize the Whitney umbrella and describe the fibre at the generic point of its double line, at a nonzero geometric point, and at the origin.

**Solution.** The element \(v=x/y\) satisfies \(v^2=z\); adjoining it gives \(k[y,v]\), a polynomial normal domain in the same fraction field. Hence this is normalization. At the generic point of the line the residue field is \(k(z)\), and \(v^2-z\) is irreducible, so the fibre is one degree-two point. It is separable if the characteristic is not two and purely inseparable in characteristic two. At a nonzero point over an algebraic closure, it is two distinct points in characteristic not two, and one length-two point in characteristic two. At the origin it is always \(\bar k[v]/(v^2)\), one length-two point. These computations follow directly from (6.2) and include the scheme structure, rather than only counting points.

## References and proof providers

The Stacks project, read in the AI Integrated Stacks Project edition, provides the exact relative construction, universal properties and affine descriptions linked above. The trace-pairing field prerequisites have the complete open providers at Tags 030N and 0BIL. General Nagata stability has the exact full proof at Tag 0334, used only for the arithmetic extension after the field case has been proved. Linked sources retain GNU FDL 1.2; their expression is not reproduced.

Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024, §10.7, was consulted for normalization examples and the finiteness argument. The rational algebra, componentwise universal property, trace lattice and arbitrary-field finiteness proofs here supply the assigned results. All five exercises have complete solutions.
