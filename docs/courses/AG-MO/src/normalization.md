# Normalization

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

Normalization adjoins rational functions that satisfy monic equations. It separates the branches of a node and supplies the missing parameter of a cusp. In higher dimension it need not remove all singularities. We will construct it locally, prove the gluing and universal properties, and distinguish existence from finiteness. The separable finiteness proof uses a trace pairing; a separate argument handles inseparability over an arbitrary field.

We use integral closure, its localization, and relative Spec from Affine, integral and finite morphisms and Zariski's Main Theorem. The algebraic foundations are Integral extensions, especially Theorems 1.1–1.2 and 2.2 and Proposition 2.3, and Krull dimension and Noether normalization, Corollary 3.2. Normality is defined by local rings, as defined and proved local in the prerequisite Properties of schemes, Section 4; its Noetherian algebra is developed in Discrete valuation rings, normal rings and Serre's criterion. Here a normal local ring is an integrally closed domain, and a normal scheme has normal local rings. A normal scheme need not be integral.

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

**Lemma 4.0 (separable primitive elements and traces).** If \(L/K\) is a finite separable extension of degree \(n\), there is \(\theta\in L\) with \(L=K(\theta)\). Its \(n\) distinct \(K\)-embeddings \(\sigma_i\) into a splitting field satisfy
\[
\operatorname{Tr}_{L/K}(c)=\sum_{i=1}^n\sigma_i(c),
\]
and the bilinear pairing \((c,d)\mapsto\operatorname{Tr}_{L/K}(cd)\) is nondegenerate.

**Proof.** A finite extension is generated by finitely many elements, for example by a finite vector-space basis. For a separable tower, each embedding of an intermediate field extends in as many ways as the degree of the next minimal polynomial: its distinct roots give the maps from the polynomial quotient. Counting along the tower gives \([L:K]\) embeddings; products of tower bases prove the same multiplication rule for the degrees.

Suppose first \(K\) is infinite and \(L=K(\alpha,\beta)\). For each pair of distinct embeddings, equality
\(\sigma_i(\alpha)+c\sigma_i(\beta)=\sigma_j(\alpha)+c\sigma_j(\beta)\)
forbids at most one \(c\in K\) when the two \(\beta\)-images differ; when those images agree, the \(\alpha\)-images differ and it forbids none. Choose \(c\) outside this finite list. The element \(\alpha+c\beta\) has at least \(n\) distinct conjugates, so its minimal-polynomial degree is at least \(n\), and at most \(n\) because it belongs to \(L\). It generates \(L\). Induct on the generating list.

If \(K\) is finite, \(L\) is finite. Its multiplicative group is cyclic: let \(m\) be the least common multiple of its element orders. For each prime divisor of \(m\), choose an element with the maximal corresponding prime-power order and take a power to discard the other factors. Multiplying these elements gives order \(m\), since their orders are relatively prime. Every unit is a root of \(T^m-1\); the polynomial root bound makes their number at most \(m\). The element of order \(m\) already has \(m\) distinct powers, so it generates all units and therefore the field. This supplies a primitive element in this case too. The root bound follows by repeatedly dividing by \(T-a\) at each distinct root.

Write \(\theta_i=\sigma_i(\theta)\). Over a field containing these roots, the evaluation map from the scalar extension of \(L\), on its power basis, has matrix
\(V=(\theta_i^{j-1})_{i,j=1}^n\).
This matrix is invertible: a polynomial of degree below \(n\) vanishing at all \(n\) distinct roots is zero by the same root bound. Evaluation intertwines multiplication by \(c\) with the diagonal matrix having entries \(\sigma_i(c)\). Matrix trace is unchanged by conjugation, giving the trace formula. In the power basis the trace-pairing matrix is \(V^{\mathsf T}V\), whose determinant is \((\det V)^2\ne0\). This proves nondegeneracy. The case \(n=1\) is included. \(\square\)

The same complete arguments appear in Algebraic integers and rings of integers, Sections 1 and 3, and Orders and the discriminant theorem, Lemma 1.2. The proof above supplies every field input used here directly.

**Theorem 4.1.** Let \(R\) be a Noetherian normal domain, \(K=\operatorname{Frac}R\), and \(L/K\) a finite separable extension. The integral closure \(C\) of \(R\) in \(L\) is a finite \(R\)-module.

**Proof.** Lemma 4.0 proves that the trace pairing \(\langle x,y\rangle=\operatorname{Tr}_{L/K}(xy)\) is nondegenerate.

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

### Nagata rings and finite normalization

For a domain \(A\), write **N-1** when its integral closure in \(\operatorname{Frac}A\) is finite over \(A\), and **N-2** when this holds in every finite extension of that fraction field. A **Nagata ring** is a Noetherian ring \(R\) for which every prime quotient \(R/\mathfrak p\) is N-2.

**Theorem 5.2 (Nagata finite-type stability).** Every algebra of finite type over a Nagata ring is Nagata. In particular, the normalization of a scheme of finite type over a Nagata ring is finite. This applies to every field and to \(\mathbb Z\), and hence to schemes of finite type over \(\mathbb Z\).

The finiteness requirement involves all finite field extensions, including inseparable ones. The proof below first treats these extensions, then completion, and finally a single rational generator. Adjoining generators successively will finish the theorem.

We use the following proved elementary programme results. Integral extensions, Theorems 1.1–1.2, 2.1–2.2, 3.2–3.4 and 5.1 and Lemma 3.1, prove integrality, localization, normality, prime lifting, closed images and dimension under integral extensions. Noetherian and Artinian rings, Theorems 2.1, 4.2 and 6.1 and Solution 7.3, prove Hilbert's basis theorem, the Artinian decomposition, Krull intersection and Noetherianity of power-series rings. Associated primes and primary decomposition, Sections 1–3 and Solution 8.4, prove associated-prime existence, exact-sequence inclusions, localization and the absence of embedded primes in a reduced ring. Discrete valuation rings, normal rings and Serre's criterion, Lemma 3.1 and Theorems 1.2, 3.2–3.3 and 4.4, prove element detection, the DVR, codimension-one and normality tests. These inputs retain their stated Noetherian hypotheses.

#### N.1. Elementary finiteness reductions

**Lemma N.1.1.** Let \(A\) be a Noetherian domain.

1. Localization preserves N-1 and N-2.
2. If \(A\subset B\) is finite and both rings are domains, N-2 for \(A\) implies N-2 for \(B\). Conversely, N-1 or N-2 for \(B\) implies the respective property for \(A\).
3. Quotients, localizations and finite algebras over a Nagata ring are Nagata.

**Proof.** Integral closure commutes with localization, and localizing a finite generating list preserves finiteness. This proves the first assertion.

For the second, \(\operatorname{Frac}B/\operatorname{Frac}A\) is finite. Indeed localization of the finite \(A\)-module \(B\) at the nonzero elements of \(A\) is a finite-dimensional domain over \(\operatorname{Frac}A\), hence a field: multiplication by any nonzero element is an injective linear map, so is surjective. This field is \(\operatorname{Frac}B\). In a finite field extension of \(\operatorname{Frac}B\), integral closure over \(A\) and over \(B\) is identical, by transitivity and the inclusion \(A\subset B\). Finiteness over \(A\) therefore gives finiteness over \(B\).

For descent of N-1, the closure of \(A\) in its fraction field is an \(A\)-submodule of the closure of \(B\) in its fraction field. The latter is finite over \(A\); Noetherianity makes the submodule finite. For N-2, given a finite extension \(L/\operatorname{Frac}A\), choose a maximal ideal of the nonzero finite-dimensional algebra \(L\otimes_{\operatorname{Frac}A}\operatorname{Frac}B\). Its field quotient \(M\) is a common finite extension: each structural map from a field is injective. The closure of \(A\) in \(L\) embeds as an \(A\)-submodule of the closure of \(B\) in \(M\). Apply the same argument.

A prime quotient of a quotient of \(R\) is a prime quotient of \(R\). A prime quotient of a localization is a localization of such a quotient, so the first assertion applies. For a finite \(R\)-algebra \(T\), each prime quotient \(T/\mathfrak q\) is a finite domain extension of \(R/\mathfrak p\), where \(\mathfrak p=\mathfrak q\cap R\). The second assertion applies. All these rings are Noetherian: quotients and localizations preserve ascending chains, and a finite algebra is of finite type, so Hilbert's basis theorem applies. \(\square\)

**Lemma N.1.2 (separated modules over a complete ring).** Suppose \(A\) is complete for an ideal \(I\), \(\bigcap_n I^nM=0\), and \(M/IM\) is finite over \(A/I\). Then \(M\) is finite over \(A\).

**Proof.** Choose lifts \(e_1,\ldots,e_r\) of generators modulo \(I\). For \(m\in M\), first express its class modulo \(IM\) using these lifts. If the residual element is in \(I^nM\), write it as a finite sum \(\sum_j c_jm_j\), \(c_j\in I^n\), and replace each \(m_j\) by its expression modulo \(IM\). The new residual is in \(I^{n+1}M\), and the coefficients added to the \(e_i\) lie in \(I^n\). Completeness gives limits \(a_i\in A\) of their partial sums. For every \(n\),
\(m-\sum_i a_ie_i\in I^nM\); separatedness makes this difference zero. Thus the \(e_i\) generate. If \(r=0\), the same argument puts every element in every \(I^nM\), so \(M=0\). \(\square\)

#### N.2. Finite extensions and polynomial rings

**Lemma N.2.1 (the separable lattice).** If \(A\) is a Noetherian normal domain and \(L/K\) is finite separable, where \(K=\operatorname{Frac}A\), the integral closure of \(A\) in \(L\) is finite.

**Proof.** The primitive-element theorem, including finite base fields, is proved in Normalization, Lemma 4.0. Choose a primitive element \(\theta\), of degree \(n\), and a finite splitting field of its separable minimal polynomial, with distinct roots \(\theta_1,\ldots,\theta_n\). After scalar extension to that field, evaluation at the roots identifies the minimal-polynomial quotient with the product of \(n\) copies of the splitting field. Division and Bezout for the distinct linear factors prove this identification. Multiplication is diagonal in that product, so its trace is the sum of the conjugates.

On \(1,\theta,\ldots,\theta^{n-1}\), the trace-pairing matrix is \(V^{\mathsf t}V\), with \(V_{ij}=\theta_i^{j-1}\). Its determinant is nonzero. To see this directly, the determinant of \((X_i^{j-1})\), as a polynomial in its last variable, has the preceding variables as roots and the preceding determinant as its leading coefficient. Induction gives \(\det V=\prod_{i<j}(\theta_j-\theta_i)\). Thus the pairing is nondegenerate, in every characteristic.

Choose a \(K\)-basis \(b_i\) of integral elements. Each algebraic basis element can be multiplied by a nonzero \(a\in A\) so that its monic equation has coefficients in \(A\): for a relation with degree-\(j\) coefficient \(c_j\in K\), choose \(a\) clearing all denominators, so \(a^jc_j\in A\). For an integral element \(c\), each conjugate is integral over \(A\); their sum is integral, and equals \(\operatorname{Tr}_{L/K}(c)\in K\). Normality puts this trace in \(A\). Products \(b_ic\) are integral as well.

The nondegenerate pairing therefore gives an isomorphism
\[
L\longrightarrow K^n,
\qquad c\longmapsto\bigl(\operatorname{Tr}_{L/K}(b_ic)\bigr)_i,
\]
which sends the integral closure into \(A^n\). Its inverse image of \(A^n\) is a free \(A\)-module of rank \(n\). The closure is a submodule of this finite module and is finite by Noetherianity. \(\square\)

**Lemma N.2.2 (inseparability first).** In positive characteristic, a Noetherian domain is N-2 if its integral closures in all finite purely inseparable extensions are finite.

**Proof.** Let \(L/K\) be finite, with generators \(\alpha_i\). Write each irreducible minimal polynomial as
\(f_i(T)=g_i(T^{q_i})\), where \(q_i\) is a power of the characteristic and \(g_i\) is separable. This is obtained by repeatedly removing common powers from the exponents when the derivative is zero; the degree decreases until the derivative is nonzero.

Adjoin the unique \(q_i\)-th roots of all coefficients of \(g_i\) to form a finite purely inseparable field \(K_0/K\). Over \(K_0\),
\(f_i(T)=h_i(T)^{q_i}\). The polynomial \(h_i\) is separable: in a splitting field the distinct roots of \(g_i\) have distinct unique \(q_i\)-th roots, which are the roots of \(h_i\). Thus \(\alpha_i\) is separable over \(K_0\), and \(M=K_0L\) is a finite separable extension of \(K_0\).

Let \(A_0\) be the closure of \(A\) in \(K_0\). It is finite by assumption, normal, and has fraction field \(K_0\). The last assertion follows by scaling any algebraic element of \(K_0\) into \(A_0\), as in Lemma N.2.1. Lemma N.2.1 makes its closure in \(M\) finite over \(A_0\), hence over \(A\). Transitivity identifies this with the closure of \(A\) in \(M\). The closure in \(L\) is an \(A\)-submodule, so is finite. In characteristic zero, an irreducible polynomial has nonzero derivative of smaller degree; Bezout for the polynomial and its derivative excludes any shared root, so every finite extension is separable. Lemma N.2.1 then applies to every Noetherian normal domain. \(\square\)

**Lemma N.2.3.** If a Noetherian domain \(A\) is N-2, then \(A[T]\) is N-2.

**Proof.** The normalization \(A_0\) in \(K\) is finite. It is normal and N-2 by Lemma N.1.1, and \(A_0[T]\) is finite over \(A[T]\). The descent assertion in Lemma N.1.1 allows us to replace \(A\) by \(A_0\). Polynomial normality is proved in Affine descent, Zariski Main and recognition of spaces, Corollary B1.2, including its coefficient argument. Thus in characteristic zero Lemma N.2.1 finishes the proof.

In characteristic \(p\), use Lemma N.2.2. For a finite purely inseparable \(L/K(T)\), choose generators whose \(q\)-th powers, for one \(q=p^e\), are rational functions in \(T\). Adjoin to \(K\) the \(q\)-th roots of the finitely many coefficients of their numerators and denominators. This gives a finite purely inseparable \(K'/K\). If \(u^q=T\), each chosen rational function has a \(q\)-th root in \(K'(u)\), obtained by rooting its coefficients and replacing \(T\) by \(u\). Uniqueness of purely inseparable roots shows \(L\subset K'(u)\).

Let \(C\) be the closure of \(A\) in \(K'\). It is finite by N-2. The algebra \(C[u]\) is finite integral over \(A[T]\), is normal, and has fraction field \(K'(u)\). It is therefore the entire integral closure of \(A[T]\) in that field: an element integral over \(A[T]\) is integral over \(C[u]\), and normality puts it there. The closure in \(L\) is a submodule of this finite \(A[T]\)-module, hence finite. \(\square\)

#### N.3. Completeness and normalization

**Lemma N.3.1.** A power-series ring over a Noetherian normal domain is normal.

**Proof.** Write \(D=A[[T]]\), which is Noetherian by the power-series proof cited above, and \(K=\operatorname{Frac}A\). An integral fraction \(w\in\operatorname{Frac}D\) has a Laurent-series expansion in \(K((T))\). The finite module \(D[w]\) admits a common nonzero denominator \(h\in D\), so \(hw^r\in D\) for every \(r\ge0\).

If \(w\ne0\) begins with \(cT^v\) and \(h\) begins with \(bT^m\), then \(hw^r\) begins with \(bc^rT^{m+rv}\). Consequently \(v\ge0\) and \(bc^r\in A\) for every \(r\). The submodule of \(b^{-1}A\) generated by all \(c^r\) is finite, contains \(1\), and is preserved by multiplication by \(c\). The finite-module determinant argument makes \(c\) integral over \(A\), so \(c\in A\). Subtract \(cT^v\) and repeat; integral elements form a ring, so every subtraction preserves integrality. In increasing degree this puts every coefficient of \(w\) in \(A\). Thus \(w\in D\). The case \(w=0\) is immediate. \(\square\)

##### A complete prime parameter

**Lemma N.3.2 (a complete prime parameter).** Suppose \(A\) is a Noetherian normal domain, \(xA\) is prime, \(A\) is \(x\)-adically complete, and \(A/xA\) is N-2. Then \(A\) is N-2.

**Proof.** If \(x=0\), the assertion is its hypothesis. If the fraction field has characteristic zero, use Lemma N.2.1. Otherwise Lemma N.2.2 reduces the question to a finite purely inseparable extension \(L/K\). Enlarge it by \(y\) with \(y^q=x\), choosing \(q=p^e\) so that \(L^q\subset K\) after enlargement. Proving finiteness in the enlargement suffices, by Noetherianity.

Let \(B\) be the closure of \(A\) in \(L\). For \(b\in B\), normality gives \(b^q\in A\). The only prime above \(xA\) is
\[
\mathfrak q=\{b\in B:b^q\in xA\}=yB.
\]
Indeed membership in any prime above \(xA\) is detected by the \(q\)-th power. If \(b^q=x a\), then \((b/y)^q=a\in A\), so \(b/y\) is integral and belongs to \(B\). This proves the displayed equality.

The ring \(A_{xA}\) is a DVR. Its valuation \(v\) extends to \(L\) by \(w(b)=v(b^q)/q\); the power identities prove the product and triangle rules. The value group is a subgroup of \(q^{-1}\mathbb Z\). The closure of \(A_{xA}\) is exactly the ring \(w\ge0\): one inclusion follows from a monic equation, and the other from \(b^q\in A_{xA}\). Localization of integral closure identifies it with \((A\setminus xA)^{-1}B\); uniqueness of the prime above \(xA\) makes this a local ring, so it is \(B_{\mathfrak q}\). This is a DVR without assuming \(B\) Noetherian: choose the smallest positive value, and every nonzero ideal is generated by an element with its smallest value.

Its residue extension has degree at most \([L:K]\). In fact lifts of residue-linearly-independent units are \(K\)-linearly independent: scale a proposed relation by a power of the base uniformizer until all coefficients have nonnegative valuation and at least one has value zero, then reduce to the forbidden residue relation. Hence the closure of \(A/xA\) in \(\kappa(\mathfrak q)\) is finite by hypothesis. It contains \(B/yB\), so this quotient is finite by Noetherianity. The filtration of \(B/y^qB=B/xB\), with factors \(y^iB/y^{i+1}B\cong B/yB\), makes \(B/xB\) finite.

Finally, if \(b\in\bigcap_n x^nB\), then \(b^q\in\bigcap_n x^{nq}A=0\), so \(b=0\). Lemma N.1.2 now makes \(B\) finite over \(A\). \(\square\)

**Lemma N.3.3.** Every Noetherian complete local domain is N-2.

**Proof.** First, every field is N-2: a finite extension is itself a finite vector space and contains its integral closure. A Cohen ring is a normal DVR of characteristic zero, so is N-2 by Lemma N.2.1. Lemmas N.3.1–N.3.2, applied successively to the series variables, show that every finite-variable formal power-series ring over a field is N-2. A power-series ring over a Cohen ring is normal of characteristic zero, so Lemma N.2.1 gives N-2 there too.

Let \((B,\mathfrak m)\) be a complete local domain of dimension \(d\). The coefficient-ring existence proof in Coefficient rings and the Cohen structure theorem, Theorem 5.1, gives an embedded coefficient field \(k\) in equal characteristic or a coefficient Cohen ring \(C\) in mixed characteristic. In the latter case the coefficient map is injective because \(B\) is a domain and no power of the prime integer is zero.

In equal characteristic choose a system of parameters \(z_1,\ldots,z_d\). In mixed characteristic, the nonzero prime integer \(p\) lowers dimension by one, so choose \(d-1\) parameters modulo \(p\). These parameter statements and the dimension drop are proved in Dimension theory of Noetherian local rings, Theorems 2.1 and 3.2. They define a map
\[
D=k[[Z_1,\ldots,Z_d]]\longrightarrow B,
\quad\text{or}\quad
D=C[[Z_1,\ldots,Z_{d-1}]]\longrightarrow B.
\]
Substitution converges because the variables map into \(\mathfrak m\). The ring \(D\) is complete for its displayed maximal ideal. In mixed characteristic the coefficient of a monomial of degree \(r<n\), modulo the \(n\)-th power of that ideal, is determined modulo \(p^{n-r}\); compatible quotients therefore recover exactly a power series with coefficients in the complete ring \(C\). The image ideal \(I\), including \(p\) in mixed characteristic, is \(\mathfrak m\)-primary; its powers and the maximal-ideal powers are cofinal. Thus \(B\) is separated for \(I\). Its quotient by \(I\) is a finite-dimensional \(k\)-space, by the Artinian local structure theorem. Lemma N.1.2 makes \(B\) finite over \(D\).

The ring \(D\) has dimension \(d\). Its maximal ideal has \(d\) displayed generators, giving the upper bound by the height theorem; the chain of ideals generated by successive variables, starting with \((p)\) in mixed characteristic, gives the lower bound, since their quotients are domains. The map \(D\to B\) is injective. Otherwise its prime kernel contains a nonzero \(F\); the one-equation dimension theorem gives \(\dim D/(F)=d-1\), whereas finiteness and integral prime-chain lifting give \(\dim B=\dim(D/\ker)=d\), a contradiction. For \(d=0\), the domain \(B\) is already its residue field. We have obtained a finite inclusion \(D\subset B\). The preceding N-2 result for \(D\) and Lemma N.1.1 finish the proof. \(\square\)

##### Reduced completion and finite normalization

**Lemma N.3.4.** If a Noetherian local domain \(A\) has reduced completion \(\widehat A\), then \(A\) is N-1.

**Proof.** Completion is faithfully flat and Noetherian, with exact completion of finite modules, by Completion, Theorems 3.1–3.3. For a reduced Noetherian ring the total fraction ring is the product of the fraction fields of its minimal-prime quotients, by Discrete valuation rings, normal rings and Serre's criterion, Lemma 4.3. Each quotient \(\widehat A/\mathfrak p\) is a complete local domain: exact completion identifies a quotient by an ideal with the inverse limit of its quotient system. Lemma N.3.3 gives finite normalization for each quotient. Taking their finite product therefore gives a finite \(\widehat A\)-module \(D\) containing the integral closure of \(\widehat A\) in its total fraction ring.

Let \(C\) be the closure of \(A\) in \(K=\operatorname{Frac}A\). Flatness embeds
\[
C\otimes_A\widehat A\ \subset\ K\otimes_A\widehat A\ \subset\ Q(\widehat A).
\]
The second inclusion holds because each nonzero element of the domain \(A\) stays a nonzerodivisor after flat extension. Every element of the left side is integral over \(\widehat A\); it is a submodule of \(D\), hence finite. Choose finitely many elements of \(C\) whose tensors generate this submodule, by collecting the finitely many tensor expressions in a generating list. The quotient of \(C\) by their \(A\)-span becomes zero after tensoring with \(\widehat A\), so faithful flatness makes it zero. Thus \(C\) is finite. \(\square\)

#### N.4. Detecting reduced completion by a principal section

Call a local ring **analytically unramified** if its completion at the maximal ideal is reduced.

**Lemma N.4.1.** Let \((A,\mathfrak m)\) be a Noetherian local domain and \(0\ne x\in\mathfrak m\). Suppose \(A/xA\) has no embedded associated primes, and for each associated prime \(\mathfrak p\) of this quotient, \(A_{\mathfrak p}\) is regular and the completion of \(A/\mathfrak p\) is reduced. Then \(\widehat A\) is reduced.

**Proof.** Put \(E=\widehat A\) and \(M=A/xA\). Its associated primes are precisely its minimal support primes. They have height one by the principal ideal theorem, because \(A\) is a domain and \(x\ne0\). The module-element detection lemma gives an injection
\[
M\longrightarrow\bigoplus_{\mathfrak p\in\operatorname{Ass}M}M_{\mathfrak p}.
\]
There are finitely many summands. Flatness of \(E\) preserves this injection. Each \(M_{\mathfrak p}\) has finite length over \(A_{\mathfrak p}\); its composition factors are \(\kappa(\mathfrak p)\). Tensoring its composition series with \(E\) yields factors
\[
\kappa(\mathfrak p)\otimes_A E
=(A\setminus\mathfrak p)^{-1}(E/\mathfrak pE).
\]
The ring \(E/\mathfrak pE\) is the completion of \(A/\mathfrak p\), and is reduced by hypothesis. Its associated primes are minimal. The exact-sequence inclusions, which apply to arbitrary modules, now show that every associated prime \(\mathfrak q\) of \(E/xE\) is minimal over some \(\mathfrak pE\) and contracts to \(\mathfrak p\). To check the localization step explicitly, an element of a localized module with prime annihilator has an annihilator disjoint from the inverted set. Multiplying its numerator by finitely many inverted denominators, one for each generator of that annihilator, realizes the same prime as an annihilator before localization. Thus here it is a minimal prime of \(E/\mathfrak pE\) disjoint from \(A\setminus\mathfrak p\). It contracts to \(\mathfrak p\), since it both contains \(\mathfrak p\) and avoids its complement. A smaller prime over \(\mathfrak pE\) would also avoid that complement and would contradict this minimality.

At this \(\mathfrak q\), the quotient \(E_{\mathfrak q}/\mathfrak pE_{\mathfrak q}\) is a field. Thus its maximal ideal is \(\mathfrak pE_{\mathfrak q}\). The regular one-dimensional local ring \(A_{\mathfrak p}\) is a DVR. Its uniformizer generates that maximal ideal after extension and remains a nonzerodivisor by flatness. A Noetherian local ring with its maximal ideal generated by a nonzerodivisor is a DVR: Krull intersection gives a finite order for each nonzero element, division by the generator expresses it as a power times a unit, and the smallest such order generates each nonzero ideal. In particular \(E_{\mathfrak q}\) is a domain.

If \(z^2=0\) in \(E\), then \(z\) vanishes in every such local domain. Element detection on \(E/xE\) implies \(z=xz_1\). Since \(x\) stays a nonzerodivisor in \(E\), \(z_1^2=0\). Repetition puts \(z\) in \(\bigcap_n x^nE=0\), by Krull intersection. Every nonzero nilpotent would have a nonzero square-zero power, so there are none. \(\square\)

**Lemma N.4.2.** Every local Nagata domain is analytically unramified.

**Proof.** Induct on its dimension, a finite integer by the local height theorem. In dimension zero it is a field. Let \((A,\mathfrak m)\) have dimension \(d>0\), and let \(B\) be its normalization in its fraction field. The Nagata condition makes \(B\) finite; Lemma N.1.1 makes it Nagata. It is normal and has finitely many maximal ideals \(\mathfrak n_i\), all over \(\mathfrak m\). Each \(B_{\mathfrak n_i}\) has dimension at most \(d\), by incomparability of primes under an integral inclusion.

For such a normal local ring \(D=B_{\mathfrak n_i}\) of positive dimension, choose \(0\ne x\) in its maximal ideal. The quotient \(D/xD\) has no embedded primes, and all its associated primes have height one, by the normal-domain theorem cited above. Its localizations there are DVRs. For each such prime \(\mathfrak p\), the domain \(D/\mathfrak p\) is Nagata by Lemma N.1.1 and has dimension less than \(d\): prepend \((0)\subsetneq\mathfrak p\) to any chain in the quotient. The induction hypothesis makes its completion reduced. Lemma N.4.1 therefore makes \(\widehat D\) reduced. Dimension-zero factors are fields and have the same conclusion.

The completion \(\widehat A\) injects into the \(\mathfrak mB\)-adic completion of \(B\), by exact completion of the finite inclusion \(A\subset B\). Let \(J=\bigcap_i\mathfrak n_i\). The finite-dimensional algebra \(B/\mathfrak mB\) is Artinian, so its radical is nilpotent; hence \(J^r\subset\mathfrak mB\subset J\) for some \(r\). These filtrations are cofinal. Distinct maximal ideals are comaximal, and Chinese remainders give
\[
\widehat B=\prod_i\widehat{B_{\mathfrak n_i}}.
\]
Explicitly, \(J^n=\prod_i\mathfrak n_i^n=\bigcap_i\mathfrak n_i^n\); the quotient by \(\mathfrak n_i^n\) is unchanged by localization at \(\mathfrak n_i\), and taking inverse limits gives the formula. Every factor is reduced by the preceding paragraph. Their product and its subring \(\widehat A\) are reduced. \(\square\)

#### N.5. Patching finite normalization

**Lemma N.5.1.** Let \(A\) be a Noetherian domain, and suppose \(A_f\) is normal for some \(f\ne0\). Its normal locus is open. If every maximal localization \(A_{\mathfrak m}\) is N-1, then \(A\) is N-1.

**Proof.** By Serre's criterion, if \(A_{\mathfrak p}\) is not normal, there is \(\mathfrak q\subset\mathfrak p\) at which either regularity fails in height one or depth is one in height at least two. Such \(\mathfrak q\) contains \(f\), since \(A_f\) is normal. In the second case the regular-element depth formula gives depth zero for \((A/fA)_{\mathfrak q}\), so \(\mathfrak q\in\operatorname{Ass}(A/fA)\). This formula and the depth-zero test are proved in Regular sequences, depth and Cohen–Macaulay modules, Lemma 2.2 and Theorem 2.3. In height one, the nonzero quotient \((A/fA)_{\mathfrak q}\) has finite length, so its maximal ideal is associated and the same conclusion holds. Therefore the nonnormal locus is the union of \(V(\mathfrak q)\) for the finite subset of \(\operatorname{Ass}(A/fA)\) where \(A_{\mathfrak q}\) is not normal. Conversely every specialization of such a prime is nonnormal because normality localizes. This proves openness.

Let \(C\) be the normalization of \(A\). At a maximal ideal \(\mathfrak m\), choose global integral elements \(c_1,\ldots,c_r\in C\) generating \(C_{\mathfrak m}\); localization of integral closure allows denominators to be absorbed in the local coefficients. The finite ring \(B_{\mathfrak m}=A[c_1,\ldots,c_r]\) has normal local rings at all primes over \(\mathfrak m\). Also \((B_{\mathfrak m})_f=A_f\), so its nonnormal locus is closed by the first paragraph. Its image in \(\operatorname{Spec}A\) is closed because the ring extension is finite. The complementary open \(W_{\mathfrak m}\) contains \(\mathfrak m\).

These opens cover: each prime is contained in a maximal ideal, and an open containing that maximal ideal also contains its generalizations. Choose a finite subcover and form \(B\) by adjoining all generators of the corresponding rings \(B_{\mathfrak m}\). It is finite over \(A\). At a prime \(\mathfrak q\) of \(B\), its image lies in some \(W_{\mathfrak m}\); the contracted local ring of \(B_{\mathfrak m}\) is normal. The finite integral extension inside the common fraction field becomes equality over that normal local ring. Thus \(B_{\mathfrak q}\) is normal. Normality is local, so \(B\) is normal and equals \(C\). This proves N-1. \(\square\)

##### One rational generator

**Lemma N.5.2 (one rational generator).** If \(R\) is a normal Nagata domain, \(K=\operatorname{Frac}R\), and \(z\in K\), then \(R[z]\) is N-1.

**Proof.** If \(z\in R\), the ring is already normal. Otherwise write \(z=b/a\), \(a,b\ne0\), and put \(T=R[z]\). The ring \(T_a=R_a\) is normal. By Lemma N.5.1 it suffices to prove N-1 at every maximal ideal \(\mathfrak m\) of \(T\).

Set \(\mathfrak n=\mathfrak m\cap R\). Replace \(R\) by \(R_{\mathfrak n}\) and \(T\) by \(R_{\mathfrak n}[z]\). This does not change \(T_{\mathfrak m}\): every denominator outside \(\mathfrak n\) is outside \(\mathfrak m\). The extension of \(\mathfrak m\) to the new algebra is maximal and has the same residue field, since \(T/\mathfrak m\) was already a field. Now its residue field is generated as an algebra over \(\kappa(\mathfrak n)\) by the residue of \(z\). The field-algebra theorem in Affine descent, Zariski Main and recognition of spaces, Lemma P0.9, makes this extension finite. Lift its monic minimal polynomial to a monic \(F\in R[Z]\). Then \(F(z)\in\mathfrak m\).

Take a finite splitting field \(K'/K\) of \(F\), and let \(D\) be the closure of \(R\) in \(K'\). It is finite, normal and Nagata by Lemma N.1.1, and has fraction field \(K'\). All roots \(r_i\) of \(F\) belong to \(D\). The ring \(T'=D[z]\) is finite over \(T\). At any maximal ideal \(\mathfrak m'\) above \(\mathfrak m\), the identity \(F(z)=\prod_i(z-r_i)\) gives \(z-r_i\in\mathfrak m'\) for some \(i\). Set \(u=z-r_i\). If \(u=0\), the local ring is a localization of the normal ring \(D\). Otherwise \(T'=D[u]\), with \(u\ne0\) in \(\mathfrak m'\).

We prove that \(A=(D[u])_{\mathfrak m'}\) satisfies Lemma N.4.1. The kernel of \(D[U]\to D[u]\) is generated by its linear relations \(cU-d\), \(cu=d\). Indeed for a relation \(c_nu^n+\cdots+c_0=0\), the element \(c_nu\) is integral over \(D\): multiply by \(c_n^{n-1}\) to obtain a monic equation for it. Normality puts \(d=c_nu\) in \(D\). Subtract \((c_nU-d)U^{n-1}\) and induct on the degree. Consequently
\[
D[u]/uD[u]=D/J,
\qquad J=uD\cap D.
\]
Write \(u=b'/a'\), \(a',b'\ne0\). Multiplication by \(a'\) embeds \(D/J\) in \(D/b'D\), because its kernel is exactly \(J\). Associated primes of this submodule therefore have height one, by the normal-domain quotient theorem. Since \(b'\in J\), any prime containing \(J\) has positive height. Thus the associated primes are minimal over \(J\), so \(D/J\), and hence its localization as an \(A/uA\)-module, has no embedded primes.

For an associated prime \(\mathfrak q\) of \(D[u]/uD[u]\), put \(\mathfrak p=\mathfrak q\cap D\). We just proved \(\operatorname{ht}\mathfrak p=1\); it is minimal over \(J\). Localizing the intersection defining \(J\) gives
\(JD_{\mathfrak p}=uD_{\mathfrak p}\cap D_{\mathfrak p}\). Since this ideal is proper, the DVR valuation of \(u\) is positive. Therefore \(u\in D_{\mathfrak p}\) and
\[
(D[u])_{\mathfrak q}=D_{\mathfrak p},
\]
a regular DVR. The quotient by \(\mathfrak q\) is a quotient of \(D/J\), hence a quotient of the Nagata ring \(D\). For the associated primes that survive at \(\mathfrak m'\), localizing this domain gives a local Nagata domain, whose completion is reduced by Lemma N.4.2. All the conditions of Lemma N.4.1 hold for \(A,u\). Thus \(\widehat A\) is reduced, and Lemma N.3.4 makes \(A\) N-1.

The finite ring \(T'\otimes_T T_{\mathfrak m}\) is semilocal; its maximal localizations are the local rings just treated. It has a normal localization obtained by inverting the denominator of \(z\). Lemma N.5.1 makes this semilocal domain N-1. Descent along the finite inclusion, Lemma N.1.1, gives N-1 for \(T_{\mathfrak m}\). Applying Lemma N.5.1 once more to \(T\) finishes the proof. \(\square\)

#### N.6. Finite-type stability and the arithmetic consequence

**Proof of Theorem 5.2.** First adjoin one generator: let \(S=R[t]/I\), with \(R\) Nagata. Hilbert's basis theorem makes \(S\) Noetherian. For \(\mathfrak q\in\operatorname{Spec}S\), put \(\mathfrak p=\mathfrak q\cap R\), \(A=R/\mathfrak p\), and \(B=S/\mathfrak q=A[b]\). The domain \(A\) is Nagata, since each of its prime quotients is a prime quotient of \(R\). We must show \(B\) is N-2.

If \(b\) is transcendental over \(K=\operatorname{Frac}A\), then \(B=A[b]\) is a polynomial ring, and Lemma N.2.3 applies. Otherwise \(L=\operatorname{Frac}B\) is finite over \(K\). For any finite extension \(M/L\), let \(D\) be the closure of \(A\) in \(M\). The N-2 property of \(A\) makes \(D\) finite over \(A\); it is normal and Nagata by Lemma N.1.1 and has fraction field \(M\). The ring \(D[b]\subset M\) is N-1 by Lemma N.5.2. It is finite over \(B\), since \(D\) is finite over \(A\). The closures of \(B\) and \(D[b]\) in \(M\) coincide by transitivity. The latter is finite over \(D[b]\), hence over \(B\). This proves N-2 for \(B\), and proves that every monogenic algebra over \(R\) is Nagata.

A finite-type algebra has finitely many algebra generators. Adjoin them one at a time, applying the monogenic result at every step. The empty generating list gives \(R\) itself. If \(R=0\), every unital \(R\)-algebra is zero and the assertion is vacuous. This proves finite-type stability.

Fields are Nagata because their finite extensions are finite vector spaces. The ring \(\mathbb Z\) is Noetherian: every nonzero ideal has a least positive member, and integer division makes that member a generator. Applied to \((a,b)\), this also supplies the Bezout relation when \(a,b\) are coprime. The ring is normal: if a reduced fraction \(a/b\) is integral, clearing a monic equation gives \(b\mid a^n\); Bezout makes \(a\) invertible modulo \(b\), so \(b\mid1\). A nonzero proper prime ideal has a positive generator \(p\); a factorization of \(p\) into two smaller positive factors would contradict primality, so \(p\) is a prime integer. Bezout gives an inverse modulo \(p\) to every nonzero residue, making its quotient the field \(\mathbb F_p\). Every finite extension of \(\mathbb Q\) is separable, so Lemma N.2.1 proves N-2 for the zero-prime quotient. Hence \(\mathbb Z\) is Nagata.

For a reduced Noetherian Nagata algebra \(B\), its total fraction ring is
\(\prod_i\operatorname{Frac}(B/\mathfrak p_i)\), with the finitely many minimal primes \(\mathfrak p_i\). Integral closure in this product is the product of the closures of the prime quotients. Projection gives one inclusion; for the other, take a monic annihilating polynomial over \(B/\mathfrak p_i\) for each coordinate, lift its coefficients to \(B\), and multiply these lifted polynomials. Each coordinate is then annihilated by its corresponding factor and hence by the product, giving a monic equation for the tuple. Every factor closure is finite by the Nagata condition, so the product is finite over \(B\). This proves finite normalization on reduced affine charts. These closures glue under localization, and finiteness is affine-local on the target. For a nonreduced chart, apply the same argument to \(B_{\mathrm{red}}\), a quotient which is Nagata; the finite reduced quotient and its finite normalization compose to a finite map. Thus normalization is finite for every scheme of finite type over a Nagata ring, including \(\mathbb Z\). \(\square\)

The full stability statement is [Stacks Project, Tag 0334](https://stacks.math.columbia.edu/tag/0334). Freely readable sources for the constituent arguments are [polynomial N-2, Tag 032O](https://stacks.math.columbia.edu/tag/032O), [the complete prime-parameter argument, Tag 032P](https://stacks.math.columbia.edu/tag/032P), [complete local rings, Tag 032W](https://stacks.math.columbia.edu/tag/032W), [reduced completion and finite normalization, Tag 032Y](https://stacks.math.columbia.edu/tag/032Y), [the principal-section test, Tag 0330](https://stacks.math.columbia.edu/tag/0330), [local Nagata domains, Tag 0331](https://stacks.math.columbia.edu/tag/0331), and [normalization patching, Tag 0333](https://stacks.math.columbia.edu/tag/0333). Every auxiliary assertion used above has its proof here or in the named programme proof.


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

The Stacks project, read in the AI Integrated Stacks Project edition, provides the exact relative construction, universal properties and affine descriptions linked above. The primitive-element theorem, trace formula and nondegenerate pairing are proved in Lemma 4.0. General Nagata finite-type stability and finite normalization over Nagata bases, including the arithmetic extension, are proved in Section 5, Theorem 5.2, with the full auxiliary arguments in Lemmas N.1.1–N.5.2. Tag 0334 identifies a freely accessible comparison source. Linked sources retain GNU FDL 1.2; their expression is not reproduced.

Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024, §10.7, was consulted for normalization examples and the finiteness argument. The rational algebra, componentwise universal property, trace lattice and arbitrary-field finiteness proofs here supply the assigned results. All five exercises have complete solutions.
