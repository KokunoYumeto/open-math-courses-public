# Valuation rings and the valuative criterion of separatedness

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

Separatedness says that two positions in a family cannot agree generically and then separate when a parameter specializes. To make that statement a criterion, we need parameter spaces that can witness every specialization. Valuation rings provide them. Discrete valuation rings are the familiar one-dimensional examples, but they suffice for the converse criterion only with suitable finiteness hypotheses.

We use the diagonal and equalizer results from The diagonal and separated morphisms, and the criterion that a quasi-compact morphism has closed image precisely when its image is stable under specialization, from Finiteness of morphisms. The ring theory needed for general valuation rings is developed here. A single additional open algebraic proof, identified in Section 5, supplies a discrete valuation ring dominating a nonfield Noetherian local domain.

## 1. Divisibility and values

A **valuation ring of a field** \(K\) is a subring \(R\subset K\) such that for every \(x\in K^\times\), either \(x\in R\) or \(x^{-1}\in R\). Its fraction field is automatically \(K\). A field is allowed as a valuation ring. For local subrings \(A\subset B\subset K\), we say that \(B\) **dominates** \(A\) if \(\mathfrak m_B\cap A=\mathfrak m_A\). This requires an inclusion and a local map; an inclusion alone is insufficient.

**Proposition 1.1.** A valuation ring is local and integrally closed in its fraction field. Its ideals are totally ordered by inclusion, and every finitely generated ideal is principal.

**Proof.** For nonzero \(a,b\in R\), one of \(a/b,b/a\) belongs to \(R\). Therefore one of \((a),(b)\) contains the other. The nonunits form an ideal: they are stable under multiplication by arbitrary ring elements, and if \(a,b\) are nonunits, choose the larger of their principal ideals. Both \(a\) and \(b\), hence \(a+b\), belong to that proper ideal. The nonunits are exactly one maximal ideal \(\mathfrak m\), so \(R\) is local.

If ideals \(I,J\) are not ordered by \(I\subset J\), choose \(0\ne a\in I\setminus J\). For each nonzero \(b\in J\), the possibility \(a/b\in R\) would put \(a\) in \(J\). Thus \(b/a\in R\) and \(b\in I\). Hence \(J\subset I\). Among finitely many principal ideals one contains all the others, proving the finite-generation assertion.

Suppose \(x\in K\) is integral over \(R\) but is not in \(R\). Then \(y=x^{-1}\) lies in \(\mathfrak m\): it is in \(R\) by the valuation-ring condition and cannot be a unit. Multiply a monic equation for \(x\) by its highest inverse power. The result is \(1+a_1y+\cdots+a_ny^n=0\), with \(a_j\in R\). It says \(1\in\mathfrak m\), a contradiction. Thus \(R\) is integrally closed. \(\square\)

The **value group** of \(R\) is the abelian group

\[
\Gamma=K^\times/R^\times,
\qquad v:K^\times\to\Gamma,
\]

written additively. Order it by \(v(x)\geq v(y)\) if \(x/y\in R\). Multiplication by units does not change this condition. It is a total order compatible with addition, because ratios are comparable by the defining property of \(R\). Also

\[
v(xy)=v(x)+v(y),\qquad
v(x+y)\geq\min\{v(x),v(y)\}
\tag{1.1}
\]

when the sum is nonzero. To check the inequality, if \(x/y\in R\), factor \(x+y=y(1+x/y)\). Set \(v(0)=\infty\) to include zero in the notation. We recover

\[
R=\{0\}\cup\{x:v(x)\geq0\},\quad
\mathfrak m=\{0\}\cup\{x:v(x)>0\}.
\tag{1.2}
\]

Conversely, any valuation into a totally ordered abelian group gives a valuation ring by (1.2): the two inequalities in (1.1) make it a subring, and one of \(v(x),-v(x)\) is nonnegative. Taking the image group makes the valuation surjective.

For a nonzero ideal \(I\), its nonzero values form an upper subset of \(\Gamma_{\geq0}\). If \(x\in I\) and \(v(y)\geq v(x)\), then \(y/x\in R\) and \(y\in I\). Every upper subset conversely defines an ideal by this rule and (1.1). A principal ideal has the upper subset \(v(x)+\Gamma_{\geq0}\). An ideal can fail to have a least nonzero value, and then it cannot be principal.

These facts correspond to [Stacks, Tags 00IB–00IF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-valuation-group). Ford’s [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), Chapter 5, Section 4, gives the divisibility and ordered-group viewpoints.

## 2. A valuation ring over every local subring

**Theorem 2.1 (domination).** Let \(A\subset K\) be a local subring of a field. There exists a valuation ring \(R\) of \(K\) dominating \(A\). The field \(K\) may be larger than the fraction field of \(A\).

**Proof.** Consider local subrings of \(K\) dominating \(A\), ordered by domination. A chain has an upper bound: its union is a ring, and the union of the maximal ideals is its ideal of nonunits. To see this, an element outside its maximal ideal at some stage is a unit there; an element in the maximal ideal remains a nonunit at every larger stage by domination. The union therefore is local and dominates every member of the chain. Zorn’s lemma gives a maximal member \(R\).

We first show that \(R\) is integrally closed in \(K\), without yet knowing it is a valuation ring. If \(z\in K\) is integral over \(R\), the ring \(C=R[z]\) is a finite \(R\)-module. The ideal \(\mathfrak m_RC\) is proper. Here is the finite-module argument: if it were the whole ring, take a finite list of module generators of \(C\) including \(1\), express them as combinations of themselves with coefficients in \(\mathfrak m_R\), and apply the adjugate to that linear system. The determinant is congruent to \(1\) modulo \(\mathfrak m_R\), hence a unit, but annihilates all the generators. This would annihilate \(1\), which is impossible inside a field. Choose a maximal ideal \(\mathfrak n\) of \(C\) containing \(\mathfrak m_RC\). Its contraction is \(\mathfrak m_R\); the local subring \(C_{\mathfrak n}\subset K\) dominates \(R\). Maximality makes it equal to \(R\), so \(z\in R\).

Now take \(x\in K^\times\setminus R\). If \(\mathfrak m_RR[x]\) were proper, localization at a maximal ideal containing it would give a local subring dominating \(R\) and containing \(x\), contradicting maximality. Thus

\[
1=a_0+a_1x+\cdots+a_nx^n,
\qquad a_j\in\mathfrak m_R,
\]

for some \(n\geq1\). Put \(y=x^{-1}\), multiply by \(y^n\), and divide by the unit \(1-a_0\). This gives a monic polynomial for \(y\) over \(R\). Integral closedness in \(K\) puts \(y\) in \(R\). The defining valuation-ring property follows for every \(x\), and also shows that \(\operatorname{Frac}R=K\). \(\square\)

This is [Stacks, Tag 00IA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dominate), with the valuation-ring characterization at [Tag 00IB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-valuation-ring-x-or-x-inverse). The construction controls the centre on \(A\) through domination. It gives no bound on the rank or the number of prime ideals of \(R\).

There is also an equivalent maximality definition. A valuation ring \(R\) is maximal among local subrings of \(K\) dominating it. Indeed, if a larger local ring \(B\) dominating \(R\) contained \(x\notin R\), then \(x^{-1}\in\mathfrak m_R\subset\mathfrak m_B\), contradicting invertibility of \(x^{-1}\) in \(B\). Conversely, the proof of Theorem 2.1 shows that a maximal such local subring has the ratio property. This reconciles the two usual definitions.

## 3. When the valuation is discrete

A **discrete valuation ring**, or **DVR**, is the valuation ring of a surjective valuation \(v:K^\times\to\mathbf Z\). An element \(\pi\) of value \(1\) is a **uniformizer**. Such a ring is not a field.

**Theorem 3.1.** A valuation ring is Noetherian if and only if it is a field or a DVR.

**Proof.** In a DVR the nonzero values in any nonzero ideal have a least integer \(n\geq0\). An element with this value generates the ideal by divisibility. Thus every ideal is principal and the ring is Noetherian. A field is Noetherian too.

Conversely, suppose \(R\) is a Noetherian valuation ring which is not a field. Its nonzero maximal ideal is finitely generated, hence principal by Proposition 1.1; write \(\mathfrak m=(\pi)\). Every nonzero \(x\in R\) is divisible by only finitely many successive powers of \(\pi\). Otherwise all the elements \(x/\pi^n\) would belong to \(R\), and their principal ideals would form an infinite strictly ascending chain. Strictness follows by cancellation in the domain: equality of two consecutive ideals would make \(\pi\) a unit. This contradicts Noetherianity.

Take the largest \(n\) with \(x\in\pi^nR\). Then \(x=\pi^nu\), where \(u\notin\mathfrak m\) is a unit. A ratio of two nonzero elements therefore has a unique expression \(\pi^nu\) with \(n\in\mathbf Z\) and \(u\) a unit. Uniqueness follows again because \(\pi\) is not a unit. The exponent gives a surjective valuation to \(\mathbf Z\), with valuation ring \(R\). \(\square\)

The source is [Stacks, Tag 00II](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-valuation-ring-Noetherian-discrete). The examples \(k[[t]]\) and \(\mathbf Z_{(p)}\) are DVRs, with valuations given by order in \(t\) and exponent of the prime \(p\). Every nonzero series is a power of \(t\) times an invertible series; every nonzero rational number is a power of \(p\) times a unit in \(\mathbf Z_{(p)}\).

Here is a valuation whose order has two levels. Let

\[
K=k((u))((t)),\qquad
v(F)=\bigl(\operatorname{ord}_tF,
\operatorname{ord}_u(\text{leading }t\text{-coefficient of }F)\bigr),
\tag{3.1}
\]

with \(\mathbf Z^2\) ordered lexicographically. The coefficient in (3.1) is taken after removing the lowest power of \(t\). Multiplication adds both coordinates. In a sum, either the smaller \(t\)-order survives, or equal orders allow cancellation and the order rises; at equal \(t\)-order without cancellation, the usual \(u\)-valuation inequality applies. Thus (3.1) is a valuation. It is surjective, since \(v(t^au^b)=(a,b)\).

Its ring is

\[
R=k[[u]]+t\,k((u))[[t]].
\tag{3.2}
\]

The first coordinate must be nonnegative, and when it is zero the constant coefficient must have nonnegative \(u\)-order. Its maximal ideal is \(uR\), because \((0,1)\) is the least positive value. Nevertheless \(R\) is not Noetherian:

\[
(t)\subsetneq(t/u)\subsetneq(t/u^2)\subsetneq\cdots.
\tag{3.3}
\]

Every generator here has positive first coordinate and hence belongs to \(R\). The inclusions are strict because \(u\) is not a unit. This illustrates the distinction between the least positive value and the stronger assertion that every positive value is an integer multiple of it. Noetherianity forced the latter in Theorem 3.1.

![A finite lattice window in the lexicographically ordered value group: all points with positive first coordinate are positive, however negative their second coordinate. The values of t, t/u, t/u squared, and t/u cubed descend along the first-coordinate-one column, while their principal ideals strictly increase.](../assets/rank-two-values.png)

*Figure 1. The rank-two example (3.1)–(3.3), drawn as an exact finite sample of the value group. The vertical arrows follow decreasing values, hence increasing principal ideals. This is an order schematic; the group has no Euclidean distance in the argument. Theorem 3.1 explains why this chain prevents Noetherianity.*

## 4. Specializations become valuation diagrams

Write \(x'\leadsto x\) when \(x\) lies in the closure of \(\{x'\}\). The prime corresponding to \(x'\) is then contained in the prime corresponding to \(x\) in any common affine chart.

**Theorem 4.1 (witnessing a specialization).** Given a specialization \(x'\leadsto x\) on a scheme \(X\) and a field extension \(L/\kappa(x')\), there is a valuation ring \(R\subset L\), with fraction field \(L\), and a morphism \(h:\operatorname{Spec}R\to X\) sending the generic point to \(x'\) with the specified residue-field extension, and the closed point to \(x\).

**Proof.** Choose an affine neighbourhood \(\operatorname{Spec}B\) of \(x\). Every open containing a specialization also contains its generizations, so \(x'\) belongs to this chart. Let its primes be \(\mathfrak p'\subset\mathfrak p\). The image of the ring map

\[
B_{\mathfrak p}\longrightarrow\kappa(\mathfrak p')\longrightarrow L
\]

is the local domain \(A=(B/\mathfrak p')_{\mathfrak p/\mathfrak p'}\). Apply Theorem 2.1 to find a valuation ring of \(L\) dominating \(A\). The composite \(B\to A\to R\) defines the desired map. Its generic-point contraction is \(\mathfrak p'\), because \(A\) embeds into \(L\). Its closed-point contraction is \(\mathfrak p\), because domination preserves the maximal ideal of \(A\). The map on the generic residue field is precisely the specified inclusion into \(L\). \(\square\)

The source is [Stacks, Tag 01J8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-points-specialize). A general valuation spectrum can have intermediate points. The theorem fixes its endpoints and does not assert that it has only two points. Also \(\operatorname{Spec}\operatorname{Frac}R\to\operatorname{Spec}R\) is a localization morphism and need not be an open immersion for a general valuation ring. It is an open immersion for a DVR, where it is \(D(\pi)\).

A morphism \(f:X\to S\) satisfies **valuative uniqueness** if, for every valuation ring \(R\) with fraction field \(K\), every pair of compatible maps

\[
\operatorname{Spec}K\longrightarrow X,
\qquad\operatorname{Spec}R\longrightarrow S
\tag{4.1}
\]

has at most one extension \(\operatorname{Spec}R\to X\) over \(S\). “At most one” allows there to be no extension. Existence is a different requirement, used later for properness.

**Theorem 4.2 (valuative criterion of separatedness).** A separated morphism satisfies valuative uniqueness. Conversely, a quasi-separated morphism satisfying valuative uniqueness is separated.

**Proof.** If \(f\) is separated, the equalizer of two candidate extensions \(a,b:\operatorname{Spec}R\to X\) is a closed subscheme. Its ideal \(I\subset R\) becomes zero in \(K\), since the extensions agree generically. The inclusion \(R\subset K\) is injective, so \(I=0\). The extensions coincide as morphisms of schemes, including their maps on functions.

For the converse, put \(Y=X\times_S X\). The diagonal is a quasi-compact immersion by quasi-separatedness and the first lesson. We show its image is stable under specialization. Take a specialization \(y'\leadsto y\) in \(Y\), with \(y'\) in the diagonal. By Theorem 4.1, choose a valuation diagram \(h:\operatorname{Spec}R\to Y\) witnessing it. The generic point map factors through the diagonal: an immersion identifies the residue field of a point with that of its image. The two projections of \(h\) to \(X\) therefore agree over \(\operatorname{Spec}K\). They have the same map to \(S\). Valuative uniqueness makes them equal over \(\operatorname{Spec}R\). The universal property of the fibre product then makes \(h\) factor through the diagonal, so \(y\) belongs to its image.

The quasi-compact image criterion from the second lesson now makes the diagonal image closed. An immersion with closed image is a closed immersion, as proved in the first lesson. Hence \(f\) is separated. \(\square\)

The precise sources are [Stacks, Tag 01KZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-separated-implies-valuative) and [Tag 01L0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-valuative-criterion-separatedness). In this proof, quasi-separatedness enters when specialization stability is converted to closedness. It is not needed in the separated-to-uniqueness direction.

To see a failure of uniqueness directly, glue two affine lines \(U_1,U_2\) along their punctured lines by the identity on the coordinate \(z\). Map each \(\operatorname{Spec}k[[t]]\) into its own chart by \(z\mapsto t\). The generic-point restrictions agree in the common open, while the closed points map to the two distinct origins. These are two different extensions of one map from \(\operatorname{Spec}k((t))\). This is the valuation version of the chart-ring failure in the first lesson.

## 5. The Noetherian test by discrete valuations

We need a precise algebraic bridge to replace an arbitrary valuation witness by a DVR.

**Lemma 5.1 (discrete domination).** If \(A\) is a Noetherian local domain which is not a field, there is a DVR \(R\) dominating \(A\) with \(\operatorname{Frac}R=\operatorname{Frac}A\).

**Open proof.** The full proof is [Stacks, Tag 00PH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-exists-dvr), applied with no extension of the fraction field. Its exact statement also allows a finitely generated extension of that field. The proof first replaces \(A\), inside its fraction field, by a one-dimensional Noetherian local overring dominating it; the construction is [Tag 00P8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dominate-by-dimension-1). It uses a dominating valuation to choose the least-valued generator of the maximal ideal and adjoins the ratios of the other generators to it. The maximal ideal becomes principal, and localization at a minimal prime over that nonzero principal ideal gives dimension one. The integral closure of this one-dimensional ring is Noetherian by the Krull–Akizuki theorem, [Tag 00PG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-krull-akizuki). Localization over the maximal ideal is a one-dimensional normal Noetherian local ring, hence a DVR. The linked proof and all its algebraic dependencies are available under the [GNU Free Documentation License, version 1.2](https://github.com/stacks/stacks-project/blob/master/COPYING). These links supply the algebraic proof of the bridge; no text is copied into this lesson.

**Theorem 5.2 (DVR criterion).** Suppose \(S\) is locally Noetherian and \(f:X\to S\) is of finite type. Then \(f\) is separated if and only if it satisfies the uniqueness condition (4.1) for all DVRs \(R\).

**Proof.** The forward direction is Theorem 4.2. For the converse, separatedness is local on the base, so restrict to an affine Noetherian open of \(S\). The finite type source \(X\), and \(Y=X\times_S X\), are Noetherian. Suppose the diagonal image \(D\subset Y\) were not closed. Because \(X\) is Noetherian, it has finitely many irreducible components. Some \(y\in\overline D\setminus D\) lies in the closure of the diagonal image of one such component.

Give that closure its reduced structure and call it \(Z\). It is an integral Noetherian closed subscheme of \(Y\). Its generic point lies in \(D\): the diagonal is an immersion, so the relevant component is an open dense subscheme of its reduced closure. The local ring \(A=\mathcal O_{Z,y}\) is a Noetherian local domain, not a field, with fraction field \(K=\kappa(\eta_Z)\). Lemma 5.1 gives a DVR \(R\subset K\) dominating \(A\). We obtain

\[
\operatorname{Spec}R\longrightarrow Z\longrightarrow X\times_S X,
\]

whose generic point lands in the diagonal and whose closed point lands at \(y\notin D\). Composing with the two projections gives two maps to \(X\) over \(S\) which agree on \(\operatorname{Spec}K\). DVR uniqueness makes them equal. The displayed map would then factor through the diagonal, impossible at its closed point. Thus \(D\) is closed. Since the diagonal is an immersion, it is a closed immersion, proving separatedness. \(\square\)

The source [Stacks, Tag 0207](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-Noetherian-dvr-valuative-separation) proves the stronger version with \(f\) locally of finite type. That strengthening follows from the finite type case just proved. After restricting the base to an affine Noetherian open, any two extensions from a local valuation spectrum land in the union of affine neighbourhoods of their two closed-point images. An open containing the closed point contains the whole image of a local spectrum. The union is of finite type over the base, inherits DVR uniqueness, and is separated by Theorem 5.2. The two extensions consequently agree there. The source is locally Noetherian, hence quasi-separated; Theorem 4.2 now proves separatedness of the whole morphism.

Vakil’s *The Rising Sea*, §13.7, explains the geometry of this test and states both valuation criteria. Its discussion of the converse is an outline. Lemma 5.1 and the full diagonal argument above supply the algebraic bridge and the proof at the required Noetherian generality.

## 6. Exercises with solutions

**Exercise 6.1 (easy: locality and normality).** Starting with the ratio definition of a valuation ring, show that its nonunits form an ideal. Give an integral-closedness proof that solves a monic equation for the allegedly missing element, instead of using its reduction modulo the maximal ideal.

**Solution.** Principal ideals of two nonzero elements are comparable. If \(a,b\) are nonunits, both lie in the larger of the proper ideals \((a),(b)\), so their sum is a nonunit. Multiples of nonunits remain nonunits. This ideal contains every proper ideal, because a proper ideal contains no unit; thus it is the unique maximal ideal. For the alternate normality argument, if \(x\notin R\) is integral, then \(x^{-1}\in R\). A monic equation of degree \(n\), multiplied by \(x^{1-n}\), expresses \(x\) as an \(R\)-linear combination of \(1,x^{-1},\ldots,x^{1-n}\). Every term belongs to \(R\), contradicting \(x\notin R\).

**Exercise 6.2 (easy: the two origins).** Make the two extensions for the doubled line explicit. Show that, for the fixed generic map \(z\mapsto t\), they are the only extensions over \(k\).

**Solution.** On chart \(U_i=\operatorname{Spec}k[z]\), the homomorphism \(k[z]\to k[[t]]\), \(z\mapsto t\), defines an extension \(a_i\). Both generic restrictions are the map from \(k[z,z^{-1}]\) sending \(z\) to \(t\), so the glued generic map is the same. Their closed points lie at different origins, making the maps different. Any extension must send the closed point to an origin, because the generic coordinate \(t\) extends in either chart with value zero at the closed point. More explicitly, choose a chart containing its closed-point image; the whole map factors through that chart since the source is local. Its coordinate image in \(k[[t]]\) is forced to be \(t\) by injectivity into \(k((t))\). Thus the closed-point coordinate is zero and the map is one of the two \(a_i\).

**Exercise 6.3 (medium: two levels of value).** Verify the valuation (3.1) and the ring (3.2). Find its prime ideals and show that it is not Noetherian despite its principal maximal ideal.

**Solution.** Orders and leading coefficients multiply, giving additivity; the three possibilities for adding leading terms give the valuation inequality described before (3.2). Monomials \(t^au^b\) attain every value in \(\mathbf Z^2\), and lexicographic nonnegativity gives exactly (3.2). Let

\[
\mathfrak p=t\,k((u))[[t]],\qquad\mathfrak m=uR.
\]

Taking the constant \(t\)-coefficient gives \(R/\mathfrak p\cong k[[u]]\), so \(\mathfrak p\) is prime; also \(R/\mathfrak m\cong k\). These give \((0)\subsetneq\mathfrak p\subsetneq\mathfrak m\). To see there are no others, let \(\mathfrak q\) be a nonzero prime. If it contains an element with first value coordinate zero, that element is a unit times \(u^n\) for \(n>0\), so \(u\in\mathfrak q\) and \(\mathfrak q=\mathfrak m\). Otherwise it is contained in \(\mathfrak p\). Choose \(0\ne x\in\mathfrak q\) of value \((a,b)\), \(a\geq1\). Since \(t^{a+1}/x\in R\), primality gives \(t\in\mathfrak q\). For any \(y\in\mathfrak p\), a sufficiently large power \(y^N\) has first value coordinate greater than \(1\), so \(y^N\in tR\subset\mathfrak q\) and \(y\in\mathfrak q\). Thus \(\mathfrak q=\mathfrak p\). Finally (3.3) is an infinite strict ascending ideal chain, proving non-Noetherianity.

**Exercise 6.4 (medium: the exact Noetherian conclusion).** Let \(R\) be a Noetherian valuation ring which is not a field. Show directly that every nonzero ideal is a power of its maximal ideal, and that its only prime ideals are \((0)\) and the maximal ideal.

**Solution.** The maximal ideal is \((\pi)\). The ascending-chain argument in Theorem 3.1 writes every nonzero element uniquely as \(\pi^nu\), with \(n\geq0\) and \(u\) a unit. In any nonzero ideal choose the smallest occurring exponent. An element attaining it generates the ideal, giving \(I=(\pi^n)=\mathfrak m^n\). If a nonzero proper prime contains \(\pi^n u\), then \(n>0\) and primality puts \(\pi\) in that prime. It is therefore \(\mathfrak m\). The zero ideal is prime because \(R\) is a domain. This also explains the two-point spectrum of a DVR.

**Exercise 6.5 (hard: finding a failed DVR test).** Let \(X\to S\) be of finite type with \(S\) locally Noetherian, and suppose it is not separated. Construct a DVR diagram with two extensions. Explain why it is insufficient merely to observe that the two projected closed points have the same or different underlying points.

**Solution.** Restrict to an affine Noetherian base open where separatedness fails. The diagonal immersion then has nonclosed image. Choose a point \(y\) outside that image in the closure of the image of an irreducible component of \(X\). Give the latter closure its reduced structure \(Z\), and dominate the nonfield domain \(\mathcal O_{Z,y}\) by the DVR from Lemma 5.1. The two projections of \(\operatorname{Spec}R\to Z\subset X\times_S X\) give the required maps. They agree generically because the generic point of \(Z\) lies on the diagonal. They are distinct because equality as scheme morphisms would factor the entire map through the diagonal, contradicting the image of the closed point. A point of a fibre product contains residue-field information in addition to its two projected points. Two maps can even have identical underlying point maps and different maps on functions. The fibre-product universal property, rather than a comparison of underlying points alone, proves nonuniqueness here.

## Sources and proof dependencies

The primary open reference is *The Stacks project*, read in the AI Integrated Stacks Project edition: valuation rings at Tags 00IA–00II, specialization witnesses at 01J8, the general uniqueness criterion at 01KZ and 01L0, and the Noetherian DVR criterion at 0207. The exact linked proof of discrete domination, Tag 00PH, includes its one-dimensional reduction and Krull–Akizuki dependencies. Its source text retains the GNU Free Documentation License; this lesson’s independently written text is CC0.

Further references are T. J. Ford, [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), version of 23 September 2026, Chapter 5, Section 4, and Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), draft of 27 July 2024, §§13.5 and 13.7. They treat the divisibility, discrete-value, and geometric viewpoints. The local and normal properties, domination by a general valuation ring, the value-group assertions, specializations, and both separatedness criteria are proved here, with the explicitly supplied open algebraic bridge for the DVR criterion.
