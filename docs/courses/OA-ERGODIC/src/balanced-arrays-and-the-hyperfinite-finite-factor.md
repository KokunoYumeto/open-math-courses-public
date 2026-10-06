# Balanced arrays and the hyperfinite finite factor

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text is public domain (CC0).*

## Introduction

Finite classes give matrix algebras over a measurable base. To obtain an increasing sequence of ordinary finite-dimensional matrix algebras, their matrix units must be compatible and their diagonal partitions must eventually detect every measurable set.

For an ergodic probability-preserving relation, equal-measure sets can be matched inside orbits. This supplies the balancing step. We use it to construct dyadic arrays, identify the relation with the fair binary tail relation, and prove uniqueness of its diagonal algebra pair.

Read [Finite orbit classes and matrix blocks](finite-orbit-classes-and-matrix-blocks.md), [Diagonal expectations and invariant measures](diagonal-expectations-and-invariant-measures.md), and [Towers and odometer orbits](towers-and-odometer-orbits.md). We use the function-algebra realization Lemma 0.1 of [Normalizers, phases, and orbit cocycles](normalizers-phases-and-orbit-cocycles.md).

For Sections 1–2, let \(R\) be an ergodic principal relation of a countable nonsingular action on a standard nonatomic probability space \((X,\mu)\), with \(\mu\) invariant under every partial orbit map. Their matching and balancing proofs require no finite exhaustion. From Section 3 onward assume in addition that \(R\) is hyperfinite. This separates the preliminary balancing step used in the nonsingular array lesson from the later classification proved here. All identifications are modulo null sets; countability makes the required identities hold on one invariant conull Borel space.

## Reading finite approximation through to the factor

**First identify the finite-stage convention.** A finite subrelation may have different finite class sizes. A bounded finite subrelation adds one uniform bound on those sizes. Takesaki's source definition of an AF groupoid instead asks for stages having one constant finite class size on each stage's own unit space; that unit space may be a proper subset of \(X\). Adding the missing diagonal arrows makes the unit space all of \(X\), but may introduce singleton classes. The [groupoid definitions](groupoids-and-measured-orbit-relations.md#8-finite-classes-and-approximation-stages) keep these distinctions explicit. Every exhaustion here is a statement modulo counting-measure null sets; the countable presentation lets us pass to an invariant conull Borel space.

**Then preserve compatibility during refinement.** Sections 1–2 use ergodicity, nonatomicity and invariant probability to match equal-measure sets and balance a bounded finite relation. Hyperfiniteness enters in Section 3, when we choose finite relations that approximate the desired orbit maps. Refining an existing array must preserve every old transport exactly on the corresponding new cells. We also ask the new cell partitions to approximate a countable generating family of measurable sets. Graph approximation supplies the arrows; partition approximation supplies the entire diagonal. Exercise 7.3 explains why both are needed.

**Distinguish the two operator approximations.** A finite subrelation \(F_n\) gives a type I algebra containing every diagonal function. On its \(q\)-point part this is a measurable matrix field \(L^\infty(B_q)\bar\otimes M_q(\mathbb C)\); a diffuse base leaves that algebra infinite dimensional. The [rotation-factor lesson](type-i-stages-in-irrational-rotation-factors.md#3-finite-classes-inside-the-full-relation-representation) proves this statement in the ambient relation representation, including its multiplicity. By contrast, the compatible array in Section 5 gives an ordinary matrix algebra \(M_{2^{m_n}}(\mathbb C)\). Exact refinement makes its inclusion the usual tensor-multiplicity inclusion. The increasing diagonal partitions, rather than a diffuse centre at each stage, recover all diagonal functions in the limit.

**Check where the final restriction projection belongs.** To recover a presenting orbit operator \(V_g\), retain the arrows already in the \(n\)-th array relation: write \(D_{g,n}=\{x:(gx,x)\text{ lies in that relation}\}\). The restriction \(V_g1_{D_{g,n}}\) is a finite sum of array matrix units multiplied by diagonal projections. Those extra projections belong to the generated limiting algebra; they need not belong to the particular finite matrix stage. Since \(D_{g,n}\) increases to a conull set, the restricted operators converge strongly to \(V_g\). Theorem 5.1 and Exercise 7.4 carry out exactly this argument.

**Finally apply the correct measure hypothesis.** Invariant probability makes the binary address law fair and gives the type \(II_1\) conclusion when no single orbit is conull. An equivalent infinite sigma-finite invariant measure leads instead to the amplification in Section 6. The [classification lesson](diagonal-expectations-and-invariant-measures.md#5-finite-and-infinite-invariant-measures) explains the single-orbit type I cases and the trace converses. For an ergodic hyperfinite nonsingular relation on a standard nonatomic space, use the [nonsingular array theorem](matching-sets-and-nonsingular-dyadic-arrays.md#5-exact-refinement-binary-coding-and-one-generator): its binary law is quasi-invariant and need not be fair. The finite atomic exceptions to the unqualified source dyadic assertions are treated there explicitly.

## 1. Matching equal-measure sets inside orbits

**Lemma 1.1.** If \(\mu(A)=\mu(B)>0\), there is a measure-preserving Borel partial orbit bijection \(A\to B\), modulo null sets.

*Proof.* Enumerate the presenting group so that every element is visited infinitely often. Starting with the unused parts of \(A,B\), at each visit to \(g\) match the entire set of unused \(x\in A\) for which \(gx\) is in the unused part of \(B\), by the map \(x\mapsto gx\). Remove the matched domain and range.

The domains and ranges of these pieces are separately disjoint. Their union is a measure-preserving partial bijection. The unused sets \(A_\infty,B_\infty\) have equal measure. For every \(g\), \(gA_\infty\cap B_\infty\) is null, because the corresponding available set was removed when \(g\) was visited. If the unused measure were positive, the invariant saturation of \(A_\infty\) would be conull by ergodicity, and some \(gA_\infty\) would meet \(B_\infty\) in positive measure. This contradiction exhausts both sets. \(\square\)

A reduction \(R|_A\) to a positive set is still ergodic for normalized \(\mu|_A\): the saturation of any positive invariant subset of \(A\) is conull and meets \(A\) only in that subset. If \(R\) is hyperfinite, its reduction is also hyperfinite, by restricting the finite exhaustion.

## 2. Balanced finite arrays

An **array of order \(q\)** consists of a partition \(X=\bigsqcup_{a=0}^{q-1}Z_a\) and measure-preserving partial orbit maps \(U_{ab}:Z_b\to Z_a\) satisfying
\[
U_{aa}=\mathrm{id},\qquad U_{ab}U_{bc}=U_{ac}.
\tag{2.1}
\]
All cells have measure \(1/q\). Its generated relation has exactly one point in each cell in every class, hence classes of size \(q\). Its operators \(V_{U_{ab}}\) are matrix units.

**Lemma 2.1 (balancing).** Let \(F\subset R\) have class sizes bounded by \(N\), and let \(\mathcal P\) be a finite Borel partition. Given \(\varepsilon>0\), there is an array of order \(2^k\) with relation \(H\) such that
\[
\nu_s(F\setminus H)<\varepsilon,
\tag{2.2}
\]
and each member of \(\mathcal P\) differs by measure less than \(\varepsilon\) from a union of array cells.

*Proof.* Use the finite selectors to sort the classes of \(F\). On the size-\(j\) part choose a base \(B_j\) and transports \(\theta_i:B_j\to X\), \(0\leq i<j\). Invariance makes all sheet measures equal to \(\mu|_{B_j}\). Split the bases further according to the \(\mathcal P\)-membership of all \(j\) transported points. There are finitely many base pieces, say \(L\), and every sheet of each piece lies in one partition member.

Put \(\delta=2^{-k}\). Nonatomicity lets us split each base piece into finitely many sets of measure exactly \(\delta\) and one remainder of measure below \(\delta\). For an explicit split, push its measure through a Borel injection into \([0,1]\). The resulting distribution has no atoms, so its continuous cumulative function attains every intermediate mass; successive thresholds give the required pieces. Transport these sets to all its sheets. Each complete base chunk produces \(j\) disjoint cells of measure \(\delta\), on which all old \(F\)-arrows are retained. The combined remainders, on all sheets, have measure at most \(LN\delta\).

The selected cells occupy \(M\delta\) measure for an integer \(M\leq2^k\). Split the complement into \(2^k-M\) further cells of measure \(\delta\). Choose one cell as reference. For each selected base chunk \(D\), match the reference cell to \(D\) using Lemma 1.1, and transport that match to all its old sheets by the \(\theta_i\)'s. For the block containing the reference cell, use its existing sheet transport so that the reference transport is the identity. Match each remaining complement cell directly to the reference.

Let these transports be \(w_a\). Define \(U_{ab}=w_aw_b^{-1}\). This is an array of order \(2^k\). Within every selected old block, the common base transport cancels, so all its \(F\)-arrows belong to the new array relation. Missing \(F\)-arrows have sources in the remainder, giving
\[
\nu_s(F\setminus H)\leq N(LN\delta).
\]
Each original partition member is a union of selected cells up to the same remainder of measure at most \(LN\delta\). Choose \(k\) large enough for both errors to be below \(\varepsilon\). \(\square\)

The old finite relation is approximated here, while the new array covers the whole space. Ergodic matching may join cells coming from different old classes.

## 3. Refining an existing array

**Lemma 3.1.** Given an array of order \(q=2^m\), finitely many partial orbit maps \(T_j\), a finite Borel partition, and \(\varepsilon>0\), there is a refining array of order \(q2^k\) whose relation \(H'\) contains the old array relation, approximates every \(T_j\) in source measure to error below \(\varepsilon\), and whose cells approximate the prescribed partition to error below \(\varepsilon\).

*Proof.* Write the old transports \(v_a:Z_0\to Z_a\). For each \(T_j\), each source cell \(Z_a\), and each target cell \(Z_b\), form the partial map on \(Z_0\)
\[
T_j^{b,a}=v_b^{-1}T_jv_a,
\tag{3.1}
\]
on the points for which the displayed composition is defined. These are maps of the reduced relation \(R|_{Z_0}\), which is ergodic, nonatomic, and hyperfinite for normalized measure \(\mu_0=q\mu|_{Z_0}\).

Its finite exhaustion approximates the finitely many graphs in (3.1), by monotone convergence. A finite-class stage can, if necessary, be cut off at a large class-size bound, retaining singleton classes elsewhere; this adds arbitrarily small error on these finitely many graphs. Thus we obtain a bounded finite relation \(F\) approximating all the maps.

On \(Z_0\), take the finite partition recording membership of every \(v_ax\) in each prescribed partition member. Apply Lemma 2.1 to \(F\) and this partition, choosing its two errors as small as required. Its new array has order \(2^k\), cells \(Y_i\), and transports \(w_i:Y_0\to Y_i\).

Lift it to \(X\), with cells \(v_aY_i\) and transports
\[
U'_{(a,i),(b,j)}
=v_aw_iw_j^{-1}v_b^{-1}.
\tag{3.2}
\]
These form an array of order \(q2^k\). Summing (3.2) over equal \(i=j\) recovers each old map \(v_av_b^{-1}\) on its partitioned domain, proving exact refinement.

For the approximation estimates, each source-error set for a \(T_j\) is a finite union of images, under measure-preserving \(v_a\), of the corresponding reduced errors. Since \(\mu=\mu_0/q\) on the base, choosing the finitely many reduced errors small makes their sum below \(\varepsilon\). In passing from \(F\) to its balancing array, a reduced graph can lose only its already missing arrows and arrows in \(F\setminus H\); the number of prescribed graphs is finite, so the error (2.2) can be chosen small enough for all of them.

The lifted partition cells detect all prescribed membership patterns outside the lifted remainder. The sum of its measures over the \(q\) old cells is exactly its \(\mu_0\)-measure. This gives the partition estimate. \(\square\)

## 4. Coding the entire relation

**Theorem 4.1.** The measured relation \(R\) is isomorphic to the fair binary tail relation. In particular, any two ergodic hyperfinite probability-preserving principal relations on standard nonatomic spaces are isomorphic.

*Proof.* Choose a countable Borel family \(B_1,B_2,\ldots\) generating the measurable space and a sequence \(T_1,T_2,\ldots\) of presenting transformations. Starting with the identity array, use Lemma 3.1 inductively to construct exactly refining arrays \(\mathcal A_n\) of orders \(2^{m_n}\), with \(m_n\) strictly increasing, such that:

- the graphs of \(T_1,\ldots,T_n\) miss the array relation \(H_n\) in source measure by less than \(2^{-n}\);
- each \(B_j\), \(j\leq n\), is within measure \(2^{-n}\) of a union of \(\mathcal A_n\)'s cells.

The relations \(H_n\) increase. For each \(T_j\), their union misses its graph in measure zero. Remove the countable union of these exceptional source sets and its group saturation; the union of the array relations is then exactly \(R\).

Label the old cells by binary words of length \(m_n\), and label the refining quotient cells by words of length \(m_{n+1}-m_n\). Concatenation makes the labels compatible. Each \(x\) therefore has an infinite binary address \(\Phi(x)\). A cylinder of length \(m_n\) has inverse image one array cell, of measure \(2^{-m_n}\). The same holds for shorter cylinders by summing cells. Thus \(\Phi_*\mu\) is fair product measure.

The address sigma-field is the completed sigma-field of \(X\). Indeed, for a fixed \(B_j\), the approximating cell unions have summable errors. Their indicators converge to \(\mathbf1_{B_j}\) almost everywhere by the elementary Borel–Cantelli bound. Hence every generator belongs to the completed address sigma-field.

Pullback by \(\Phi\) is consequently a normal onto isomorphism of the two function algebras. Lemma 0.1 in the normalizer lesson realizes it by a Borel isomorphism on conull subsets. Comparing the countably many coordinate functions shows that this realization agrees with \(\Phi\) almost everywhere.

Each array transport changes its prefix label and keeps every later label fixed: this is exactly the equal-quotient-index refinement in (3.2). Thus it becomes a finite-prefix replacement. Conversely, any finite-prefix replacement is realized at a sufficiently long array stage. The countably many map identities can be placed on one conull invariant set. Therefore \(\Phi\) is an isomorphism of the measured relations. \(\square\)

This proves the finite-measure uniqueness result by an explicit coding. It does not identify all nonsingular type \(III\) relations: there the measure on the binary addresses need not be fair.

## 5. Increasing ordinary matrix algebras

Let \(\mathcal D_n\) be the span of the matrix units \(V_{U^{(n)}_{ab}}\).

**Theorem 5.1.** These are unital algebras \(\mathcal D_n\cong M_{2^{m_n}}(\mathbb C)\), they increase by tensor-multiplicity inclusions, and
\[
\mathcal M(R,\mu)=\left(\bigcup_n\mathcal D_n\right)''.
\tag{5.1}
\]
All such relation algebras are the same hyperfinite type \(II_1\) factor up to an isomorphism carrying diagonal onto diagonal.

*Proof.* Equation (2.1) gives matrix-unit multiplication and adjoints, and the diagonal cells sum to one. Exact refinement gives
\[
e_{ab}^{(n)}
=\sum_i e_{(a,i),(b,i)}^{(n+1)},
\]
which is \(A\mapsto A\otimes1\).

The diagonal cell projections generate all \(L^\infty(X)\) by the coding proof. Their multiplication operators therefore belong to \((\bigcup_n\mathcal D_n)''\).

For a presenting \(g\), let \(D_{g,n}=\{x:(gx,x)\in H_n\}\). These sets increase to a conull set. On \(D_{g,n}\), partition by the source and target array cells. Each restricted map is the corresponding array transport restricted to a measurable subdomain. Its operator is a matrix unit multiplied by a diagonal projection, hence lies in the same generated von Neumann algebra. Thus \(V_gM_{\mathbf1_{D_{g,n}}}\) belongs to that algebra and converges strongly to \(V_g\). The diagonal and these \(V_g\)'s generate the full relation algebra, proving (5.1).

Ergodicity makes it a factor. Its faithful normal trace is diagonal integration. The nonatomic measure is not concentrated on a countable orbit, so the type criterion in the expectation lesson makes it type \(II_1\). Theorem 4.1 and the orbit-equivalence transport theorem identify its diagonal pair with that of the fair binary model. \(\square\)

## 6. The infinite-measure amplification

**Proposition 6.1.** If an ergodic hyperfinite principal relation preserves a nonatomic infinite sigma-finite measure, it is isomorphic, in measure class, to the product of a fair binary tail relation with the complete relation on \(\mathbb N\). Its algebra is the hyperfinite \(II_1\) factor tensored with \(B(\ell^2(\mathbb N))\), of type \(II_\infty\).

*Proof.* Choose a set \(A_0\) of finite positive measure \(c\). Partition its complement into sets \(A_1,A_2,\ldots\), each of measure \(c\); nonatomicity and infinite sigma-finite measure permit this. The matching proof of Lemma 1.1 works in sigma-finite measure for two equal finite-measure sets: if positive unmatched sets remained, ergodicity of their saturations would give an available match. Choose measure-preserving orbit bijections \(v_n:A_0\to A_n\), with \(v_0=\mathrm{id}\).

The map \((x,n)\mapsto v_nx\) identifies the measured space with \(A_0\times\mathbb N\), and the relation with
\[
(R|_{A_0})\times(\mathbb N\times\mathbb N).
\]
Indeed, \(v_nx\sim v_my\) exactly when \(x\sim y\), since the transports themselves stay inside \(R\). The reduced relation is ergodic and hyperfinite for normalized measure \(c^{-1}\mu|_{A_0}\), so Theorem 4.1 applies.

On the regular relation space, the two coordinates supply respectively the reduced relation operators and the matrix units on \(\mathbb N\). Their products give all partial maps of the product relation by its countable graph decomposition. The resulting algebra is \(\mathcal M(R|_{A_0})\overline\otimes B(\ell^2(\mathbb N))\). Its trace is the finite trace tensored with the ordinary operator trace, scaled by \(c\) for the original measure. It is semifinite and infinite, while the diffuse reduced factor excludes type I; hence it is type \(II_\infty\). \(\square\)

## 7. Exercises with solutions

Level 1 asks for a computation or a direct application. Level 2 asks for a proof using the lesson’s framework. Level 3 combines results or examines a hypothesis whose failure changes the conclusion.

**Exercise 7.1 (balancing a three-sheet piece).** *Level 1.* Suppose a finite relation piece has classes of size three and one base piece. Bound the balancing error when the base remainder has measure below \(2^{-k}\).

*Solution.* Its three-sheet remainder has measure below \(3\cdot2^{-k}\). Every missing relation fibre there has at most three points, so its \(\nu_s\)-measure is below \(9\cdot2^{-k}\). Extra base subdivisions by a prescribed partition multiply the bound by the number of such pieces.

**Exercise 7.2 (an exact refinement).** *Level 1.* An array of order four is refined by a quotient array of order eight. Give the new matrix order, the embedding, and the trace of a new diagonal matrix unit.

*Solution.* The order is \(32\); the embedding is \(A\mapsto A\otimes1_8\). Every new diagonal cell has probability \(1/32\), so its trace is \(1/32\). Summing its eight refinements recovers an old diagonal trace \(8/32=1/4\).

**Exercise 7.3 (why partition approximation is necessary).** *Level 2.* What would be missing if the arrays approximated every orbit map but their cell partitions were not required to generate the sigma-field?

*Solution.* The address map could lose measurable information inside the cells. Approximation of maps alone controls the relation graphs, but does not force pullback from binary addresses to be onto \(L^\infty(X)\). The partition estimates make every measurable generator an almost-everywhere limit of address events and supply that surjectivity.

**Exercise 7.4 (strong generation).** *Level 3.* Why does the factor \(M_{\mathbf1_{D_{g,n}}}\) in Theorem 5.1 cause no gap in the proof of (5.1), even though that projection need not belong to \(\mathcal D_n\)?

*Solution.* All diagonal projections already belong to the von Neumann algebra generated by the entire chain, by address generation. Thus each finite sum of an array matrix unit times one of those projections belongs to that algebra. Strong limits remain inside it. The proof does not assert membership in a particular finite-dimensional stage.

**Exercise 7.5 (a finite corner of the amplification).** *Level 1.* In Proposition 6.1, compute the trace of \(1\otimes e_{nn}\) and of \(\sum_{n=0}^{N-1}1\otimes e_{nn}\), for the original measure normalization.

*Solution.* They are \(c\) and \(Nc\). Each single corner has the finite factor with normalized trace after division by \(c\), while the increasing sums have traces tending to infinity. This exhibits the infinite semifinite amplification.

## References

[Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The finite-measure orbit-equivalence uniqueness theorem is due to H. A. Dye.
