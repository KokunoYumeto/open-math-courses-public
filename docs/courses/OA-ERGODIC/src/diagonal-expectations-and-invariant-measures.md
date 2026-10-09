# Diagonal expectations and invariant measures

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text is public domain (CC0).*

## Introduction

A relation operator is a matrix on every orbit. Reading its diagonal at the point that labels the orbit fibre gives a function on the measured space. Integrating that function gives a state or a weight. Invariance of the measure is exactly what allows us to exchange the two indices in the trace calculation.

We use the countable nonsingular action, relation \(R\), algebra \(\mathcal M(R,\mu)\), and diagonal \(\mathcal A\) of [Orbits, stabilizers, and relation algebras](orbits-stabilizers-and-relation-algebras.md). The positive-measure density theorem used below is proved in Measurable actions and compact models, Theorem 0.1. General type decomposition and the structure \(B(K)\) of type I factors are written prerequisites from the programme lesson [Projections and types of von Neumann algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html), Theorems 7.2 and 10.3 and Corollary 10.4. We also reuse the written programme lesson [Traces on von Neumann algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-FOUND-REMAINDER/reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html), Corollary 5.12 and Theorem 6.7: a finite factor has a faithful normal tracial state, and a semifinite algebra with a faithful normal state has a faithful normal semifinite trace. These results are owned by the programme's operator-algebra foundations course; their compared proofs cover our countable-relation factors. The measurable-relation implications are proved below, including the sigma-finiteness of the invariant measure and the obstruction to a diffuse diagonal in a type I factor. Basic references are [Anantharaman–Popa] and [Takesaki].

## 1. Compressing to the diagonal

First replace \(\mu\) by an equivalent probability measure. Let \(P\) project \(L^2(R,\nu_s)\) onto functions supported on the diagonal. This subspace is naturally \(L^2(X,\mu)\).

**Theorem 1.1.** There is a faithful normal conditional expectation

\[
E:\mathcal M(R,\mu)\longrightarrow\mathcal A
\]

characterized by

\[
PTP=M_{E(T)}\quad\text{on }L^2(X,\mu).
\tag{1.1}
\]

We identify \(E(T)\) with its bounded function. For a finite sum of orbit-map kernels \(a\),

\[
E(L_a)(x)=a(x,x).
\tag{1.2}
\]

*Proof.* Every \(T\in\mathcal M\) commutes with second-coordinate multiplication \(N_h\), and so does \(P\). Thus \(PTP\), on the diagonal subspace, commutes with every multiplication operator on \(L^2(X)\). Such an operator is itself multiplication: apply it to the constant function \(1\), use commutation on bounded functions, and use its norm bound on indicators to show that its value at \(1\) is essentially bounded. Density of bounded functions then determines the operator.

Compression is unital on this subspace and completely positive. Identifying the multiplication algebra with \(L^\infty(X)\) therefore makes \(E\) a unital completely positive map. Since \(P\) commutes with the left diagonal, the map is \(\mathcal A\)-bimodular and fixes \(\mathcal A\). If \(T_i\uparrow T\) is a bounded increasing net of positive operators, compression gives \(PT_iP\uparrow PTP\). Hence \(E\) is normal.

For \(T\in\mathcal M\),

\[
\int_X E(T^*T)\,d\mu=\|T\Omega\|^2.
\tag{1.3}
\]

If \(E(T^*T)=0\), the separating-vector theorem implies \(T=0\). This is faithfulness. Finally, convolution of a finite orbit-map kernel with the diagonal vector has diagonal value \(a(x,x)\), proving (1.2). \(\square\)

The expectation does not depend on the equivalent probability measure chosen. The unitary changing the measure multiplies by a positive function of the source coordinate. It preserves the diagonal subspace and conjugates its multiplication operators to themselves. Thus (1.1) gives the same function after any equivalent sigma-finite change of measure.

**Proposition 1.2.** The expectation \(E\) is the unique normal conditional expectation onto \(\mathcal A\). For a full-group map \(\theta\),

\[
E(V_\theta T V_\theta^*)=E(T)\circ\theta^{-1}.
\tag{1.4}
\]

*Proof.* Let \(F\) be another such expectation. Bimodularity and
\(V_\theta M_f=M_{f\circ\theta^{-1}}V_\theta\)
force \(F(V_\theta)\) to be supported on the fixed points of \(\theta\), by a countable separating family. On that set \(V_\theta\) is the identity, so
\(F(V_\theta)=1_{\{\theta x=x\}}\).
This is also the value of \(E\). Both maps agree on \(M_fV_g\), hence on their algebraic span and, by normality, on \(\mathcal M\).

Conjugating \(E\) by \(V_\theta\) gives another normal expectation onto \(\mathcal A\). Uniqueness and the action of \(V_\theta\) on functions give (1.4). \(\square\)

## 2. When diagonal integration is a trace

Call \(\mu\) *invariant for \(R\)* if every partial orbit map preserves measure between its domain and range. In the countable-action setting this is equivalent to invariance under every group element. One direction is immediate; the other follows by partitioning a partial orbit map into restrictions of group elements.

It is also equivalent to \(\nu_s=\nu_r\). To verify this, decompose a Borel subset of \(R\) into disjoint partial-map graphs as in the prerequisite lesson. On each graph, equality of the two counting integrals says exactly that the partial map preserves measure.

**Theorem 2.1.** If \(\mu\) is an invariant probability measure, then

\[
\tau(T)=\int_XE(T)(x)\,d\mu(x)
\tag{2.1}
\]

is a faithful normal tracial state on \(\mathcal M\).

*Proof.* Positivity, faithfulness, normality, and \(\tau(1)=1\) follow from Theorem 1.1. It remains to prove the trace identity.

A finite linear combination of the generators \(M_fV_g\) has a bounded kernel \(a(z,x)\) supported on finitely many group graphs. The action is

\[
(L_a\xi)(z,x)=\sum_{y\in[x]_R}a(z,y)\xi(y,x).
\]

The finite graph bound gives uniformly bounded row and column sums, so these sums define bounded operators. Products and adjoints correspond to matrix products and conjugate transposes. For two such kernels,

\[
\tau(L_aL_b)
=\int_X\sum_{z\in[x]_R}a(x,z)b(z,x)\,d\mu(x).
\]

Invariance allows inversion \((x,z)\leftrightarrow(z,x)\) in this integral. The result is \(\tau(L_bL_a)\). Absolute integrability follows from the finite graph bounds and the probability normalization. The algebraic span is ultraweakly dense in \(\mathcal M\). Holding one variable fixed and then the other, separate ultraweak continuity extends the identity to all bounded operators in \(\mathcal M\). \(\square\)

There is a useful sigma-finite version.

**Theorem 2.2.** If \(\mu\) is a sigma-finite invariant measure, then

\[
\tau_\mu(T)=\int_XE(T)(x)\,d\mu(x),\qquad T\ge0,
\tag{2.2}
\]

is a faithful normal semifinite trace.

*Proof.* Choose \(X_n\uparrow X\) with \(\mu(X_n)<\infty\), and set \(e_n=M_{1_{X_n}}\). The corner \(e_n\mathcal M e_n\) has an ultraweakly dense algebra of finite orbit-map kernels supported on \(R\cap(X_n\times X_n)\). Indeed, compressing a monomial \(M_fV_g\) restricts its graph to points whose two endpoints lie in \(X_n\). Products are again finite sums of such restricted partial-map kernels, and compression of an ultraweak approximation gives the stated density.

The finite-measure kernel calculation in Theorem 2.1, followed by separate ultraweak continuity, says that (2.2) is a finite trace on this corner, of total mass \(\mu(X_n)\). This argument does not identify the source-coordinate multiplicity of the represented corner with a new base space. For \(T\in\mathcal M\) and indices \(m,n\), the operator \(e_mTe_n\) lies in a finite corner containing both projections. Its trace identity gives

\[
\tau_\mu(e_nT^*e_mTe_n)
=\tau_\mu(e_mTe_nT^*e_m).
\]

For every positive \(A\), bimodularity gives \(E(e_nAe_n)=\mathbf1_{X_n}E(A)\). Thus
\[
\tau_\mu(e_nAe_n)=\int_{X_n}E(A)\,d\mu\uparrow\tau_\mu(A).
\tag{2.3}
\]
This scalar convergence does not assert that \(e_nAe_n\) increases as an operator. First let \(n\) increase in the finite-corner identity above. Its left side converges by (2.3) to \(\tau_\mu(T^*e_mT)\); its right side converges by normality, since \(e_mTe_nT^*e_m\uparrow e_mTT^*e_m\). Now let \(m\) increase: \(T^*e_mT\uparrow T^*T\), while (2.3) applies to the compressed right side. We obtain

\[
\tau_\mu(T^*T)=\tau_\mu(TT^*).
\]

This is the trace identity for the weight. For \(A\ge0\), the increasing operators
\(A^{1/2}e_nA^{1/2}\le A\)
converge strongly to \(A\), and

\[
\tau_\mu(A^{1/2}e_nA^{1/2})
=\tau_\mu(e_nAe_n)\le\|A\|\mu(X_n)<\infty.
\]

They prove semifiniteness. Faithfulness and normality follow from the expectation and integration. \(\square\)

## 3. Traces force invariant measures

**Proposition 3.1.** If \(\mathcal M(R,\mu)\) has a faithful normal tracial state \(\sigma\), then the measure

\[
\eta(B)=\sigma(M_{1_B})
\tag{3.1}
\]

is an invariant probability measure equivalent to \(\mu\).

*Proof.* Normality gives countable additivity; normalization gives total mass one. Faithfulness gives exactly the same null sets as \(\mu\). For a partial orbit map \(\theta:D\to E\) and \(B\subset D\),

\[
V_\theta M_{1_B}V_\theta^*=M_{1_{\theta B}},
\qquad
V_\theta^*V_\theta M_{1_B}=M_{1_B}.
\]

The trace identity consequently gives \(\eta(\theta B)=\eta(B)\). \(\square\)

**Lemma 3.2.** If an ergodic relation preserves a sigma-finite measure \(\mu\), then every equivalent sigma-finite invariant measure is a positive scalar multiple of \(\mu\).

*Proof.* Write \(\eta=h\mu\) with \(0<h<\infty\) almost everywhere. Invariance of both measures gives \(h(gx)=h(x)\) almost everywhere for every group element, by changing variables in the integral of each indicator. Countability makes the identities simultaneous on an invariant conull set. The level sets of \(h\), or of the bounded injective function \(h/(1+h)\), are invariant. Ergodicity makes \(h\) constant almost everywhere. \(\square\)

This lemma supplies a simple obstruction. An ergodic invariant infinite measure cannot be equivalent to a finite invariant measure.

**Lemma 3.3 (trace decreases under diagonal pinching).** For any faithful normal semifinite trace \(\tau\) on \(\mathcal M\) and \(T\geq0\),
\[
\tau(E(T))\leq\tau(T).
\tag{3.2}
\]

*Proof.* First choose finite-trace projections \(e_n\uparrow1\). To justify their existence, take a maximal orthogonal family of nonzero finite-trace projections. If its residual projection \(q\) were nonzero, ultraweak density of the span of finite-trace positive elements would give such an element \(A\) with \(qAq\ne0\). The trace identity gives \(\tau(qAq)=\tau(A^{1/2}qA^{1/2})\leq\tau(A)<\infty\). A nonzero spectral projection of \(qAq\) then lies below \(q\) and has finite trace, contradicting maximality. Thus the family sums to one. It is countable because the faithful normal state given by the diagonal vector is positive on every nonzero member. Finite partial sums give \(e_n\). This argument uses the trace identity; the corresponding order property must not be assumed for an arbitrary semifinite weight.

For \(A\geq0\), the trace identity and normality give
\[
\tau(A)=\sup_n\tau(e_nAe_n).
\]
Each functional \(A\mapsto\tau(e_nAe_n)\) is bounded and normal. Their supremum makes \(\tau\) lower semicontinuous in the ultraweak topology on positive operators.

Let \(\mathcal P_m\) be the finite partition generated by the first \(m\) members of a countable Borel generating family, and let \(p_{m,j}\) be its diagonal projections. Define
\[
Q_m(T)=\sum_jp_{m,j}Tp_{m,j}.
\]
Every ultraweak cluster point commutes with all generating diagonal projections and hence belongs to the maximal abelian algebra \(\mathcal A\). Bimodularity gives \(E(Q_m(T))=E(T)\). Normality of \(E\) therefore forces every cluster point to be \(E(T)\), so \(Q_m(T)\to E(T)\) ultraweakly.

For positive \(T\), the trace identity gives
\[
\tau(Q_m(T))
=\sum_j\tau(T^{1/2}p_{m,j}T^{1/2})
=\tau(T).
\]
Lower semicontinuity proves (3.2). \(\square\)

**Theorem 3.4.** The countable relation algebra is semifinite exactly when \(R\) admits an equivalent sigma-finite invariant measure.

*Proof.* An invariant measure gives the faithful normal semifinite trace in Theorem 2.2, after the measure-class unitary change.

Conversely, let \(\tau\) be a faithful normal semifinite trace, and set \(\eta(B)=\tau(M_{\mathbf1_B})\). Normality gives countable additivity, and faithfulness gives exactly the same null sets as \(\mu\). The partial-isometry calculation in Proposition 3.1 works with infinite trace values as well, giving invariance.

It remains to prove sigma-finiteness; restriction of a semifinite weight to a subalgebra does not establish this automatically. Take the \(e_n\)'s from Lemma 3.3. Write \(E(e_n)=M_{a_n}\), where \(0\leq a_n\uparrow1\) almost everywhere by normality. For
\[
B_{n,k}=\{x:a_n(x)\geq1/k\},
\]
the order inequality \(M_{\mathbf1_{B_{n,k}}}\leq kE(e_n)\) and (3.2) give
\[
\eta(B_{n,k})\leq k\tau(E(e_n))\leq k\tau(e_n)<\infty.
\]
The countable family \(B_{n,k}\) covers a conull set. The remaining null set has \(\eta\)-measure zero, so \(\eta\) is sigma-finite. \(\square\)

**Proposition 3.5 (an invariant ergodic subgroup fixes the density).** Suppose a subgroup \(H\) preserves a sigma-finite measure \(\mu\) and its action is ergodic on measurable classes. Any sigma-finite measure equivalent to \(\mu\) and invariant under the whole acting group is a positive scalar multiple of \(\mu\). In particular, if some element of the whole group fails to preserve \(\mu\), no such invariant measure exists.

*Proof.* Write the other measure as \(h\mu\) with \(0<h<\infty\) almost everywhere. Invariance of both measures under any fixed \(s\in H\), tested on indicators and followed by Radon–Nikodym uniqueness, gives \(h(sx)=h(x)\) almost everywhere. Thus the bounded injective transform \(h/(1+h)\) is an invariant function class for \(H\). Its rational level sets are invariant classes, so ergodicity makes this function, and hence \(h\), constant almost everywhere. If the other measure were invariant under the whole group, this scalar identity would force \(\mu\) invariant as well. \(\square\)

For a countable subgroup, exact invariant representatives come from countable null saturation. For a locally compact subgroup in the scope of [Free actions and the crossed-product diagonal](free-actions-and-the-crossed-product-diagonal.md), Proposition 4.7 supplies them. The proof above only needs ergodicity of measurable classes; it does not assume a common pointwise density identity for an arbitrary uncountable subgroup. This is the measure argument behind Takesaki III, Chapter XIII, Lemma 1.8.

## 4. Atoms, single orbits, and type I

Assume from now on that \(R\) is ergodic, so that \(\mathcal M\) is a factor.

**Lemma 4.0 (small cells on a diffuse diagonal).** Let \(\mathcal A=L^\infty(X,\mu)\) for a standard sigma-finite space, and let \(q\in\mathcal A\) be a nonzero diffuse projection. If \(\lambda\) is a finite normal positive functional on \(q\mathcal A\), then for every \(\varepsilon>0\) there is a finite partition \(q=\sum_iq_i\) in \(\mathcal A\) with \(\lambda(q_i)\leq\varepsilon\).

*Proof.* Realize \(q\) as a Borel subset \(Y\) of \(X\). The functional defines a finite measure on \(Y\), absolutely continuous with respect to \(\mu|_Y\): null sets represent the zero projection. Every singleton has zero \(\mu\)-measure on \(Y\), since a positive-measure singleton would be a minimal projection below \(q\). It therefore also has zero \(\lambda\)-measure. Choose a countable Borel family separating points, and let \(\mathcal P_n\) be its increasing finite partitions of \(Y\). The largest \(\lambda\)-mass of a cell tends to zero. Otherwise some \(\varepsilon>0\) would occur at arbitrarily large levels. In the finitely branching tree of cells, retain those cells with arbitrarily deep descendants of mass at least \(\varepsilon\). A retained cell has a retained child, so recursively choose nested cells \(C_n\) with \(\lambda(C_n)\geq\varepsilon\). Their intersection contains at most one point, by separation. Continuity from above for the finite measure gives \(\lambda(\bigcap_n C_n)\geq\varepsilon\), contradicting the zero mass of singletons. A partition at a sufficiently large level gives the required projections. \(\square\)

**Theorem 4.1.** The factor is type I exactly when \(\mu\) is concentrated on one orbit. On an orbit \(O\) its algebra is \(B(\ell^2(O))\).

*Proof.* If one orbit is conull, each of its points has positive mass: some point must have positive mass because the orbit is countable, and nonsingularity transports that property to all the other points. The explicit matrix-unit calculation from the prerequisite lesson gives \(B(\ell^2(O))\), with the source-coordinate space as multiplicity.

Conversely, identify the type I factor abstractly with \(B(K)\). The diagonal still has the faithful normal expectation of Theorem 1.1. We show that this diagonal must be atomic.

Suppose it has a nonzero diffuse projection \(q\). Choose a unit vector \(\xi\in qK\), and let \(p=|\xi\rangle\langle\xi|\). Apply Lemma 4.0 to the normal finite functional \(e\mapsto\|e\xi\|^2\) on \(q\mathcal A\). For any \(\varepsilon>0\), it gives finitely many orthogonal \(q_i\) summing to \(q\), with \(\|q_i\xi\|^2\le\varepsilon\). Since \(p=qpq\), bimodularity gives

\[
E(p)=\sum_iq_iE(p)q_i=E\!\left(\sum_iq_ipq_i\right).
\]

The vectors \(q_i\xi\) are orthogonal. Thus the positive finite-rank operator in parentheses has norm at most \(\varepsilon\). Contractivity of \(E\) implies \(\|E(p)\|\le\varepsilon\). Letting \(\varepsilon\) decrease to zero contradicts faithfulness, since \(p\ne0\).

The diagonal is therefore atomic: otherwise the complement of the sum of its minimal projections would be a nonzero diffuse projection. There are countably many positive-measure atoms, since an equivalent probability assigns positive mass to each disjoint atom. Each atom has a point representative. Indeed sigma-finiteness gives it a finite positive-measure representative; for each member of a countable separating Borel family choose the side containing the atom modulo a null set. Their intersection still contains the atom modulo a countable union of null sets and contains at most one point. Thus a singleton represents that atom. Its saturation is an invariant set of positive measure, and ergodicity makes that orbit conull. \(\square\)

## 5. Finite and infinite invariant measures

**Theorem 5.1.** An ergodic countable nonsingular relation has a type \(II_1\) algebra exactly when it is not concentrated on one orbit and admits an equivalent finite invariant measure.

*Proof.* Normalize such a measure to a probability. Theorem 2.1 and change of measure give a faithful normal tracial state. This makes the factor finite: if \(v^*v=1\), then the trace of \(1-vv^*\) is zero, so faithfulness gives \(vv^*=1\). Theorem 4.1 excludes type I, and the general factor alternatives give type \(II_1\). Conversely, the tracial state of a type \(II_1\) factor gives the finite invariant measure by Proposition 3.1, and Theorem 4.1 excludes a conull single orbit. \(\square\)

**Theorem 5.2.** An ergodic relation has a type \(II_\infty\) algebra exactly when it is not concentrated on one orbit and admits an equivalent infinite sigma-finite invariant measure.

*Proof.* Such a measure makes it semifinite by Theorem 2.2, and Theorem 4.1 excludes type I. If it were type \(II_1\), Proposition 3.1 would produce a finite invariant measure equivalent to the given infinite one, contradicting Lemma 3.2. It is consequently type \(II_\infty\).

Conversely, Theorem 3.4 gives an equivalent sigma-finite invariant measure. It cannot be finite, by Theorem 5.1, and Theorem 4.1 excludes a conull single orbit. \(\square\)

**Example 5.3.** Let \(\mathbb Z\) act on a set of five points by a cycle. The presenting group is infinite; every stabilizer is \(5\mathbb Z\); the orbit relation is the complete relation on five points. Uniform probability is invariant and the action is ergodic. Its relation algebra is \(M_5(\mathbb C)\), of type \(I_5\). Thus an infinite presenting group does not replace the “not concentrated on one orbit” hypothesis in Theorem 5.1.

Even a faithful point action can have this measured behavior. Adjoin a disjoint copy of \(\mathbb Z\), give that copy measure zero, and let \(n\) translate it by \(n\). The action on the enlarged countable standard Borel space is faithful at the level of points, because no nonzero translation fixes that copy pointwise. Its maps are nonsingular, its probability remains invariant and ergodic, and its relation algebra is still \(M_5(\mathbb C)\): a null source component contributes no Hilbert-space vectors. Faithfulness of the induced action on \(L^\infty\) is a stronger requirement and fails in this example.

Takesaki III, Chapter XIII, Theorem 2.10(iii) uses “\(G\) is infinite” after dropping freeness in this section. Example 5.3 satisfies that hypothesis and its finite invariant-measure hypothesis, yet yields type \(I_5\). The corrected relation criterion is Theorem 5.1: replace the group-size condition by absence of a conull single orbit. Pointwise faithfulness alone does not repair the printed assertion, as the null-orbit variant shows. Under the separate free-action hypothesis of Theorem 1.7(ii), infinite group labels do give infinite orbits; [the free-action lesson](free-actions-and-the-crossed-product-diagonal.md) proves the resulting crossed-product criterion explicitly.

**Theorem 5.4.** An ergodic countable nonsingular relation has a type \(III\) algebra exactly when it admits no equivalent sigma-finite invariant measure.

*Proof.* A factor is type \(III\) exactly when it has no faithful normal semifinite trace. Apply Theorem 3.4. \(\square\)

The sigma-finite condition on the invariant measure is essential. Without it every nonsingular relation has an equivalent invariant measure taking only the values zero and infinity: assign zero to each \(\mu\)-null set and infinity to every other measurable set. Exercise 6.9 proves this and explains why it supplies no semifinite trace. The type criterion uses the sigma-finite measured-space convention throughout.

The resulting classification depends on the measured orbit relation:

| Measured relation, assumed ergodic | Equivalent invariant measure | Factor type |
| --- | --- | --- |
| One conull orbit with \(n<\infty\) points | Equal positive mass at each point | \(I_n\) |
| One conull countably infinite orbit | Counting measure, up to scalar | \(I_\infty\) |
| No conull single orbit | Finite invariant measure | \(II_1\) |
| No conull single orbit | Infinite sigma-finite invariant measure | \(II_\infty\) |
| Any ergodic relation | No equivalent sigma-finite invariant measure | \(III\) |

These alternatives do not overlap. A conull countable orbit always has an equivalent counting measure, which is finite exactly when the orbit is finite. In the nontransitive invariant cases, Lemma 3.2 prevents both finite and infinite equivalent invariant measures from occurring.

## 6. Exercises with solutions

Level 1 asks for a computation or a direct application. Level 2 asks for a proof using the lesson’s framework. Level 3 combines results or examines a hypothesis whose failure changes the conclusion.

**Exercise 6.1 (diagonal entries).** *Level 1.* For a three-point complete relation with arbitrary positive masses, compute \(E\) on a matrix \(T=(t_{ij})\).

*Solution.* It is the diagonal matrix with entries \(t_{ii}\). The source weights change the represented Hilbert-space norm but not this expectation. Integration gives \(\sum_i p_it_{ii}\); it is tracial exactly when the masses \(p_i\) are equal. Comparing the products of the matrix units \(e_{ij}\) and \(e_{ji}\) proves the necessity.

**Exercise 6.2 (an invariant infinite measure).** *Level 1.* Let \(O=\mathbb Z\) with counting measure and let the action be translation. Identify the algebra and the trace. Explain why infinite invariant measure does not imply type \(II_\infty\) here.

*Solution.* There is one orbit. The algebra is \(B(\ell^2(\mathbb Z))\), and (2.2) is its ordinary operator trace, obtained by summing the diagonal. It is type \(I_\infty\). Theorem 5.2 includes the essential hypothesis excluding a conull single orbit.

**Exercise 6.3 (a nonfree finite factor).** *Level 2.* Let \(\mathbb Z\times C_3\) act on the two-sided fair Bernoulli space by the shift of its first factor. Prove that the relation algebra is type \(II_1\).

*Solution.* Product probability is invariant. The shift is mixing: for cylinder events depending on finitely many coordinates, sufficiently distant translates use disjoint coordinates and hence are independent. Approximate arbitrary events in measure by cylinder events to get mixing for all events. An invariant event \(A\) then satisfies \(\mu(A)=\mu(A)^2\), proving ergodicity. The measure is nonatomic: each sequence has probability at most \(2^{-n}\) from specifying any \(n\) coordinates. A countable orbit therefore has measure zero. Theorem 5.1 gives type \(II_1\), even though the \(C_3\) stabilizer is present everywhere.

**Exercise 6.4 (uniqueness of a density).** *Level 2.* Suppose an ergodic relation preserves probability \(\mu\), and \(h>0\) is integrable. Show that \(h\mu\) is invariant exactly when \(h\) is constant almost everywhere.

*Solution.* The forward implication is Lemma 3.2. The reverse implication follows by multiplying every measure-preservation identity by that constant.

**Exercise 6.5 (semifinite approximation).** *Level 3.* In Theorem 2.2, verify both the order bound and trace estimate for \(A^{1/2}e_nA^{1/2}\).

*Solution.* Since \(0\le e_n\le1\), multiplication on both sides by \(A^{1/2}\) gives \(0\le A^{1/2}e_nA^{1/2}\le A\). Apply the trace identity to \(e_nA^{1/2}\) to get equality of its weight with that of \(e_nAe_n\). The latter operator is at most \(\|A\|e_n\), so the weight is at most \(\|A\|\mu(X_n)\). Strong convergence follows from \(e_n\uparrow1\).

**Exercise 6.6 (a finite presenting group).** *Level 2.* Let a finite group \(G\) act nonsingularly and ergodically on a nonzero standard sigma-finite measured space. Freeness is not assumed. Prove that one finite orbit is conull and identify the relation factor. Explain how its matrix size depends on a stabilizer.

*Solution.* Replace the measure by an equivalent probability. All orbit classes are finite, so the finite-class sorting lemma supplies a Borel orbit selector \(s\). Every Borel subset of its representative space pulls back to an invariant Borel set. The probability \(s_*\mu\) therefore assigns only zero or one to its Borel sets. Choose a countable separating family of those sets; for each choose either the set or its complement with measure one. Their intersection has measure one and at most one point, so \(s_*\mu\) is concentrated at one representative. Its orbit \(O\) is conull. Each point of \(O\) has positive mass by nonsingularity, and equal masses give an equivalent invariant probability. The relation algebra is \(M_n(\mathbb C)\), where \(n=|O|=[G:G_x]\) for any \(x\in O\), by the orbit–stabilizer bijection \(G/G_x\to O\). Thus the matrix size is the index of the stabilizer; it equals \(|G|\) precisely when that stabilizer is trivial.

**Exercise 6.7 (compression need not increase).** *Level 2.* On \(\mathbb C^2\), let \(e_1=\operatorname{diag}(1,0)\), \(e_2=1\), and \(A=\begin{pmatrix}1&1\\1&1\end{pmatrix}\). Show that \(e_1\leq e_2\) but \(e_1Ae_1\not\leq e_2Ae_2\). Explain which two different limit arguments justify Theorem 2.2.

*Solution.* The difference is \(A-e_1Ae_1=\begin{pmatrix}0&1\\1&1\end{pmatrix}\), whose determinant is \(-1\); its eigenvalues have opposite signs, so it is not positive. In the relation calculation the scalar identity (2.3) handles compression by diagonal \(e_n\), because the integrals over \(X_n\) increase. For \(n\) at fixed \(m\), the right-side operators \(e_mTe_nT^*e_m\) do increase: they are of the form \(Be_nB^*\). Normality handles this operator limit. Then normality handles \(T^*e_mT\uparrow T^*T\), while (2.3) handles \(e_mTT^*e_m\). Neither step assumes an order inequality for \(e_nAe_n\).

**Exercise 6.8 (no faithful expectation onto a diffuse diagonal).** *Level 2.* Suppose a diffuse standard abelian algebra \(\mathcal A\) is a unital subalgebra of \(B(K)\). Prove that a normal \(\mathcal A\)-bimodular positive unital map \(F:B(K)\to\mathcal A\) cannot be faithful.

*Solution.* Fix a unit vector \(\xi\in K\) and its rank-one projection \(p\). The vector functional is normal on \(\mathcal A\), by restriction from \(B(K)\). Lemma 4.0 gives a finite partition \(1=\sum q_i\) in \(\mathcal A\) with \(\|q_i\xi\|^2\leq\varepsilon\). Since \(F(p)\in\mathcal A\), bimodularity yields \(F(p)=F(\sum_iq_ipq_i)\). The summands act on orthogonal vectors \(q_i\xi\), so \(0\leq\sum_iq_ipq_i\leq\varepsilon1\). Positivity and unitality give \(0\leq F(p)\leq\varepsilon1\). As \(\varepsilon\) is arbitrary, \(F(p)=0\), although \(p\ne0\). This violates faithfulness. The argument also proves the conclusion without assuming normality of \(F\); the normal functional needed for the partition is the vector functional itself.

**Exercise 6.9 (an invariant measure outside the sigma-finite category).** *Level 3.* On any nonzero sigma-finite nonsingular measured action, define \(\eta(B)=0\) if \(\mu(B)=0\), and \(\eta(B)=\infty\) otherwise. Prove countable additivity, equivalence and invariance. Show that \(\eta\) is neither sigma-finite nor semifinite. Apply this observation to the affine type \(III\) example in Measurable actions and compact models, Example 4.3, and explain why it does not contradict Theorem 5.4.

*Solution.* For a disjoint countable union, either all sets are \(\mu\)-null, in which case both the union's value and the sum of values are zero, or one set has positive \(\mu\)-measure, in which case both are infinity. Thus \(\eta\) is a measure with precisely the \(\mu\)-null sets. Nonsingularity preserves this zero-versus-infinity distinction under every partial orbit map, giving invariance. Every set of finite \(\eta\)-measure is \(\mu\)-null. Countably many such sets cannot cover the nonzero measured space, so \(\eta\) is not sigma-finite. A positive-measure set has infinite \(\eta\)-measure but has no subset of positive finite \(\eta\)-measure; the measure is not semifinite either. Example 4.3 proves that rational translations together with a nontrivial dilation have no equivalent sigma-finite invariant measure, and the resulting ergodic relation has type \(III\). The present infinite-valued measure still exists there. It is excluded by Theorem 5.4's explicit sigma-finite hypothesis, and diagonal integration against it is infinite on every nonzero positive operator by faithfulness of the expectation, so it supplies no semifinite trace.

## References

- [Anantharaman–Popa] Claire Anantharaman and Sorin Popa, *An introduction to \(II_1\) factors*, author-hosted draft `IIunV15.pdf`. Sections 1.4–1.5 and 9.1 provide probability-preserving examples and finite tracial conditional expectations. [Read the authors’ draft](https://www.math.ucla.edu/~popa/Books/IIunV15.pdf). This is an accessible scholarly reference; no licence to reproduce or translate its text is assumed. The complete proofs used here are the owned and programme arguments identified above.
- [Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).
