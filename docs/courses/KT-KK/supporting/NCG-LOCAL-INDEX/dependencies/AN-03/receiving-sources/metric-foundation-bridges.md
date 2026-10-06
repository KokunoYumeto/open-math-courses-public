# Support contracts for moving-metric localization

This independently authored AI draft supplies the short support arguments needed to bind the fourteen elementary contracts of AN03-U001. It is not admitted. The advanced localization lesson and its hypotheses remain unchanged. Standard facts below are not presented as novel results. External books are linked readings under their own licenses; their prose and figures are not incorporated into the independently written course text.

## AN03-MFD-001 — Entry boundary and the maximality assumption

The finite entry boundary reuses the earlier prerequisite companion's real completeness, finite linear algebra and elementary single-variable calculus. More precisely, assume the complete ordered field of real numbers, its Archimedean property, finite and countable set operations, finite induction, finite-dimensional bases and matrix algebra, determinant identities and elimination by elementary matrices. Complex numbers are pairs of real numbers. For single-variable calculus assume limits, derivatives, the mean value theorem, the exponential series and its derivative, the usual real-power derivative laws, and the Riemann integral of a continuous function on a compact interval with its order, linearity and uniform bound. The multivariable differentiation and compactness interfaces are identified below instead of being concealed in this entry list.

For measure theory the entry boundary is the one-dimensional Lebesgue construction from interval outer measure, the definition and basic properties of a measure and its completion, measurable functions, nonnegative integration, monotone convergence and bounded convergence on finite measure spaces. Limits of measurable functions are measurable. The selected product-measure and Tonelli reading is given in AN03-MFD-006. These are a finite measure-theory entry boundary within the earlier `BASE-LEBESGUE` contract; the linear-change formula being proved below is not assumed as part of it. The construction of the real numbers, measure and integral is not rewritten here.

For EC-004 we explicitly select **Zorn's maximality principle as a foundational assumption**: a nonempty partially ordered set in which each chain has an upper bound has a maximal element. This is the form of choice used by the maximal disjoint-family argument. No proof of this assumption or of its equivalence with other forms of choice is claimed. U001 already checks the relevant chain condition: the union of a chain of pairwise disjoint ellipsoid families is again such a family, because any two members occur together in one of the comparable families. The empty family supplies a member of the partially ordered set. Countability is proved after the selection; it does not replace the maximality assumption.

## AN03-MFD-002 — Positive forms and tensor norms

Let \(E\) be real of dimension \(d\geq1\), as in U001, and let \(Q\) be a positive-definite quadratic form. Its polarization is the symmetric bilinear form
\[
\langle x,y\rangle_Q=\tfrac14\bigl(Q(x+y)-Q(x-y)\bigr).
\]
In coordinates \(Q(x)=x^{\mathsf T}Gx\) with \(G\) symmetric; expansion shows the displayed polarization is \(x^{\mathsf T}Gy\), and \(\langle x,x\rangle_Q=Q(x)\). Starting with a basis, subtract its projections on previously constructed orthonormal vectors and divide the nonzero residual by its positive \(Q\)-length. The residual cannot be zero, since that would put the original basis vector in the span of its predecessors. This finite Gram–Schmidt procedure gives a \(Q\)-orthonormal basis.

For \(y\ne0\), nonnegativity of
\(Q(x-t y)\) at \(t=\langle x,y\rangle_Q/Q(y)\) gives
\( |\langle x,y\rangle_Q|^2\leq Q(x)Q(y)\); the case \(y=0\) is immediate. Expanding \(Q(x+y)\) and applying this inequality proves the triangle inequality for \(\|x\|_Q=\sqrt{Q(x)}\). Thus it is a norm.

Let \(T:E^k\to\mathbb C\) be multilinear, and let \(M\) be the largest absolute value of its coefficients in a \(Q\)-orthonormal basis. Its operator tensor norm obeys
\[
M\leq\|T\|_Q\leq d^{k/2}M.
\]
The first inequality evaluates \(T\) on basis vectors. For the second, expand each unit vector \(u_j=\sum_a u_{ja}e_a\). The absolute value of the resulting sum is bounded by
\(M\prod_j\sum_a|u_{ja}|\leq M d^{k/2}\), by the scalar Cauchy–Schwarz inequality. For \(k=0\), both sides are simply the absolute value of the scalar and \(d^0=1\).

If \(cQ\leq P\leq CQ\), where \(0<c\leq C<\infty\), comparison of the two unit balls in every tensor argument gives
\[
C^{-k/2}\|T\|_Q\leq\|T\|_P\leq c^{-k/2}\|T\|_Q.
\]
These are the exact factors of EC-001; no uniform condition number over a family of forms has been added.

## AN03-MFD-003 — Exact differential-calculus and segment-integral readings

The differentiation reading is Jiří Lebl's *Basic Analysis*, version 6.3 source, at the [pinned revision](https://github.com/jirilebl/ra/tree/e21ec524ca7d54f800c693b948020c188d21d01f). In [the several-variables chapter](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-several-vars-ders.tex), read the derivative definition at lines 2490–2504 and uniqueness proof at 2538–2580; linearity and its proof at 2656–2686; the chain-rule statement and full proof at 2696–2819; the continuous-partials criterion and proof at 3578–3733; and the \(C^k\) definition and interchange-of-partials proof at 4662–4817. Domains are open subsets of finite-dimensional real spaces. The first-order chain rule requires differentiability at the evaluation point and its image; the interchange theorem assumes \(C^2\). These are local assertions, so restricting to a smaller neighborhood gives exactly the neighborhood formulation used in U001.

The continuous-partials proof leaves the case of one real variable with a vector target as an exercise. Here is that step: apply the scalar derivative limit to every component. There are finitely many components, so the Euclidean norm of their remainder divided by the absolute value of the increment tends to zero. Continuity of the resulting derivative is likewise componentwise. Complex scalar and finite matrix targets follow by identifying them with their finitely many real coordinates.

For clarity, the higher-order and product interfaces need no further theorem. A fixed bilinear map \(B\) on finite coordinate spaces satisfies
\[
D B(f,g)[h]=B(Df[h],g)+B(f,Dg[h]).
\]
Indeed, expand the increments bilinearly. The term containing both increments is \(O(|h|^2)\), and the two differentiability remainders are \(o(|h|)\). Coordinate multiplication and ordered matrix multiplication are such bilinear maps. Applying the first-order rule repeatedly proves the iterated product rule, without interchanging matrix factors. Applying the chain rule repeatedly proves the iterated composition rules. Applying the continuous-partials criterion to each derivative's finite coordinate list identifies \(D^j f\) with a continuous \(j\)-linear tensor for every \(j\leq k\). Adjacent derivative orders may be exchanged by the \(C^2\) interchange theorem applied to lower derivatives; every permutation is a finite product of adjacent exchanges. This gives symmetry at every allowed order, including complex and matrix-valued functions, and establishes EC-002.

For EC-010 use [Lebl's first fundamental theorem of calculus and its complete proof](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-riemann.tex#L1593-L1675), lines 1593–1675. It assumes continuity on \([a,b]\), differentiability inside, and a Riemann-integrable function agreeing there with the derivative. A \(C^1\) coordinate segment meets those hypotheses. Apply it componentwise to obtain
\[
f(x+t e_j)-f(x)=\int_0^t\partial_j f(x+s e_j)\,ds
\]
whenever the segment lies in the coordinate box; for \(t<0\), use the oriented integral. If \(f_n\) and \(\partial_jf_n\) converge uniformly on that segment, the integral error is at most \(|t|\sup|\partial_jf_n-g_j|\), so the identity passes to the limit. Repeat for each derivative order. No exchange of an uncontrolled pointwise limit with an integral is asserted.

The [pinned license notice](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/LICENSE.md) offers CC BY-SA 4.0 and CC BY-NC-SA 4.0. Choose the BY-SA option for these separately attributed readings. Their expression retains that license; it is not included in the course's CC0 dedication. The pinned source, rather than the date of a live PDF build, identifies the reading.

## AN03-MFD-004 — Countability, compactness and supports

Rational points are countable because the integer numerator and positive integer denominator can be enumerated in finite diagonal batches. Finite tuples are likewise countable. By the Archimedean property, for \(a<b\) choose an integer \(N\) with \(N(b-a)>1\); an integer strictly between \(Na\) and \(Nb\) then gives a rational in \((a,b)\). Every nonempty Euclidean open set contains an open coordinate box, hence a rational-coordinate point. Fix an enumeration and assign to each member of a pairwise disjoint family of nonempty open sets its first contained point. The assignment is injective; the family is countable. This proves EC-005 and uses no regularity of a varying metric.

For compactness, use [Lebl's metric-space chapter](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-metric.tex): the open-cover definition at 2062–2076, the covering lemma and proof at 2217–2259, equivalence with sequential compactness and its proof at 2301–2406, and the closed-subset/Heine–Borel proof run at 2418–2489. In the empty-set case a finite empty subcover suffices. For nonempty sets these proofs use exactly the stated metric hypotheses.

The displayed Heine–Borel proof treats two coordinates and leaves arbitrary finite dimension as an exercise. To supply it, begin with a bounded sequence in \(\mathbb R^d\). Extract a subsequence convergent in the first coordinate, a subsequence of that one convergent in the second, and continue for exactly \(d\) steps. Each previously convergent coordinate remains convergent. The final subsequence converges in Euclidean norm, since the sum of its finitely many squared coordinate differences tends to zero. A closed set contains the limit. The scalar subsequence fact follows from real completeness: repeatedly bisect a bounded closed interval, retain a half containing infinitely many terms, and choose increasing indices in the nested halves. Their lengths tend to zero and their common point is the subsequential limit. Thus no dimension restriction from the source exercise remains.

A fixed positive form is a continuous coordinate polynomial. Its unit sphere comparison, or its orthonormal-coordinate isomorphism, shows that a closed frozen ellipsoid is bounded; it is closed by continuity and hence compact. A finite union of compact sets is compact by taking a finite subcover for each member. Empty sets cause no exception.

For a continuous function \(f\), define \(\operatorname{supp}f\) as the closure of its nonzero set. Outside that support it vanishes on a neighborhood, so all existing derivatives vanish there. If a family of sets is locally finite, cover a compact \(K\) by neighborhoods each meeting only finitely many members. A finite subcover meets only finitely many members in total, both on \(K\) and on the union of those neighborhoods. For empty \(K\), take the empty neighborhood. These observations finish EC-007, including its neighborhood conclusion rather than merely pointwise finiteness.

## AN03-MFD-005 — Cutoffs and locally finite sums

Define \(\eta(s)=0\) for \(s\leq0\) and \(\eta(s)=e^{-1/s}\) for \(s>0\). Each derivative on the positive half-line is \(e^{-1/s}\) times a polynomial in \(1/s\), by induction. For every fixed integer \(N\), \(u^N e^{-u}\to0\) as \(u\to\infty\): use \(e^u\geq u^{N+1}/(N+1)!\). Thus every one-sided derivative tends to zero at the origin. The derivative there is also zero at every order, since dividing such an expression by \(s\) still has the same vanishing property. Induction proves \(\eta\in C^\infty(\mathbb R)\).

The denominator in
\[
\chi(s)=\frac{\eta(3/2-s)}{\eta(3/2-s)+\eta(s-1)}
\]
is strictly positive for every real \(s\). The function is smooth, lies between zero and one, equals one for \(s\leq1\), and is zero for \(s\geq3/2\). On \([0,\infty)\) its support is contained in \([0,3/2]\), a compact subset of both \([0,2)\) and \([0,4)\). The function \(x\mapsto\chi(|x|^2)\) is a smooth compact cutoff equal to one near the origin. Each fixed derivative is bounded by continuity on a compact support, and vanishes outside it. Smoothness of the quotient follows directly from the single-variable reciprocal rule and AN03-MFD-003. This proves EC-003 with the required strict support endpoints.

Suppose each point has a neighborhood on which all but finitely many smooth functions \(f_i\) vanish identically. On that neighborhood their pointwise sum is that finite sum, so it is smooth and its derivatives equal the finite sums of derivatives. The local descriptions agree because they are derivatives of the same function. This proves EC-008. No convergence argument, integration of a variable metric, or measurability assumption on the metric or weight occurs.

## AN03-MFD-006 — Full Lebesgue linear changes and frozen volumes

The product-measure reading is Sheldon Axler's *Measure, Integration & Real Analysis*, author PDF dated 12 June 2026: [product measures and Tonelli](https://measure.axler.net/MIRA.pdf#page=136). Read 5.13, 5.17, 5.20 and 5.25–5.28 with the product-algebra and section definitions in 5.2 and 5.6, pages 117–118. The needed conclusion is that for \(\sigma\)-finite measure spaces and a nonnegative function measurable for the product \(\sigma\)-algebra, the product integral equals either iterated integral, allowing the value \(+\infty\). The full proof preserves these hypotheses. To make the finite disjoint refinement in 5.13 explicit, partition each factor space into the membership patterns of its finitely many constituent measurable sets; products of these finitely many disjoint pieces partition all the original rectangles. Definitions 5.37 and 5.40 and the proof of 5.39, pages 137–139, identify the Borel product in Euclidean space. These are sufficient for the Borel indicator functions used below.

The book's first page gives [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) terms. It remains an external reading with its source notice, not part of the independently written course expression. The private source receipt pins the exact PDF bytes. The standard measure-convergence facts named in AN03-MFD-001 remain the finite base for this reading, rather than a claim of foundational reconstruction.

Here is an independent adapter to the full completed Lebesgue statement of EC-006. Let \(m_d\) be the completion of the Borel product of \(d\) copies of one-dimensional Lebesgue measure. First, interval coverings show for every subset \(S\subseteq\mathbb R\), every \(a\ne0\) and every \(b\in\mathbb R\),
\[
m_1^*(aS+b)=|a|m_1^*(S).
\]
Transform a countable interval cover to prove one inequality; transform back to prove the other. The equality, applied also to intersections and complements, preserves the outer-measure measurability criterion. It therefore gives one-dimensional translation and scaling for measurable sets. The corresponding substitution for integrals of nonnegative functions follows first for indicators, then finite nonnegative simple functions, then increasing simple approximations by monotone convergence.

For a Borel subset \(S\subseteq\mathbb R^d\), Tonelli applied to \(1_S\) shows that a coordinate translation preserves its product measure, a nonzero scaling of one coordinate multiplies it by the absolute value of that scaling, and a permutation of coordinates preserves it. A shear \(x_i\mapsto x_i+c x_j\), with \(i\ne j\), also preserves the measure: hold the other coordinates fixed and integrate first in \(x_i\); its section is simply translated by the fixed number \(c x_j\). Every section used here is Borel, and the coordinate measures are \(\sigma\)-finite. These arguments remain valid for sets of infinite measure.

An invertible real matrix is a finite product of the elementary scaling, shear and coordinate-interchange matrices, by Gaussian elimination. Their absolute determinants are respectively \(|a|\), \(1\) and \(1\). Applying the preceding identities successively and using determinant multiplicativity gives
\[
m_d(AS)=|\det A|m_d(S)
\]
for every Borel \(S\) and every invertible \(A\). The same coordinate argument gives translation invariance. Invertible affine maps and their inverses are continuous, so they preserve Borel sets.

To include every Lebesgue-measurable \(S\), use the completion description: there is a Borel \(B\) and a Borel null set \(N\) with \(S\mathbin{\triangle}B\subseteq N\). The Borel formula makes \(AN\) null and Borel, and \(AS\mathbin{\triangle}AB\subseteq AN\). Completeness therefore makes \(AS\) measurable with the same measure as \(AB\), proving the formula for \(S\). Translation is handled identically. Finite additivity and monotonicity are immediate measure properties; no varying family is integrated.

Finally choose a linear isomorphism \(L:\mathbb R^d\to E\) carrying Euclidean coordinates to a \(Q\)-orthonormal basis. In fixed volume coordinates on \(E\),
\[
\{x:Q(x)<r^2\}=L\{u:|u|<r\},\qquad
m_d(\{x:Q(x)<r^2\})=r^d v_Q\quad(r>0),
\]
where \(v_Q=|\det L|m_d(\{|u|<1\})\). The unit ball contains a nonempty coordinate cube and is contained in a bounded cube, so normalized product volume and monotonicity give \(0<v_Q<\infty\). This is the exact finite packing input. It imposes no smoothness or measurability on \(X\mapsto g_X\) or on the weight.

## AN03-MFD-007 — Uniform limits and finite-dimensional completeness

A Cauchy sequence in \(\mathbb C\) has Cauchy real and imaginary parts, which converge by real completeness. The same argument in each of finitely many coordinates proves completeness of finite-dimensional coordinate spaces. If a sequence of functions is uniformly Cauchy on a set, its pointwise limits exist in such a space. Given \(\varepsilon>0\), choose an index after which all pairwise differences are at most \(\varepsilon\) uniformly, then pass one index to the pointwise limit. The resulting bound remains uniform, proving uniform convergence.

If the original functions are continuous, choose one with uniform error less than \(\varepsilon/3\), and use its continuity near any chosen point to make its change less than \(\varepsilon/3\). The triangle inequality bounds the change of the limit by \(\varepsilon\). Thus the limit is continuous; in particular this holds on each compact set. The tensor coefficient estimate of AN03-MFD-002 gives convergence in each fixed tensor norm from coefficient convergence, and its reverse inequality gives the converse. This proves EC-009. The integral passage required with these limits was proved in AN03-MFD-003.

## AN03-MFD-008 — The countable-seminorm metric

Let \(V\) be a real or complex vector space with a countable separating family of seminorms \((p_k)_{k\geq0}\). Define
\[
d(x,y)=\sum_{k=0}^\infty 2^{-k-1}\min\{1,p_k(x-y)\}.
\]
The series converges because it is bounded termwise by a summable geometric series. Symmetry and nonnegativity are immediate, and separation makes \(d(x,y)=0\) imply \(x=y\). Subadditivity of each summand follows from the seminorm triangle inequality and \(\min(1,s+t)\leq\min(1,s)+\min(1,t)\). Summing proves the triangle inequality. Thus \(d\) is a translation-invariant metric.

The topology specified by the seminorms has zero-neighborhoods given by finite intersections \(p_{k_j}(x)<\varepsilon_j\). For a fixed \(k\), if
\(d(x,0)<2^{-k-1}\min(1,\varepsilon)\), then \(p_k(x)<\varepsilon\); this also works when \(\varepsilon\geq1\). Taking a minimum over finitely many indices produces a metric ball within any such neighborhood. Conversely, given a metric radius \(\varepsilon>0\), choose \(N\) with \(\sum_{k>N}2^{-k-1}<\varepsilon/2\), and require \(p_k(x)<\varepsilon/2\) for \(0\leq k\leq N\). The initial sum is less than \(\varepsilon/2\), so this finite seminorm neighborhood lies in the metric ball. The topologies coincide.

Finite intersections of seminorm balls are convex and balanced. Addition is continuous by subadditivity. Scalar multiplication is continuous because, at \((a_0,x_0)\),
\[
p_k(ax-a_0x_0)\leq |a|p_k(x-x_0)+|a-a_0|p_k(x_0),
\]
and \(|a|\) is bounded on a sufficiently small neighborhood of \(a_0\). Apply these estimates to each of finitely many seminorm conditions. Hence the topology is a Hausdorff locally convex vector-space topology.

The same head-and-tail estimates, applied to differences of sequence terms, show that a sequence is metric Cauchy exactly when it is Cauchy in every seminorm. Applying them to differences from a fixed vector gives the corresponding convergence assertion. Therefore the metric is complete precisely when every sequence Cauchy in all seminorms has a vector limit in all seminorms. This is the assertion of EC-011 used in U001's completeness proof; no completeness of \(V\) has been assumed in establishing the metric.

## AN03-MFD-009 — Local inverses and the matrix geometric series

If \(f=u+iv\) is a nonvanishing complex \(C^k\) function on a real domain, then locally
\[
\frac1f=\frac{u-iv}{u^2+v^2}.
\]
The denominator stays positive on a sufficiently small neighborhood. Repeated single-variable differentiation gives \((s^{-1})^{(j)}=(-1)^j j!s^{-j-1}\) for \(s>0\). AN03-MFD-003 therefore proves the asserted \(C^k\) regularity, including \(k=0\) by continuity. For a matrix function taking invertible values, its determinant is nonzero and its adjugate is a finite polynomial in its entries. The identity \(A^{-1}=\operatorname{adj}(A)/\det A\) proves the corresponding local matrix assertion without any commuting-coefficient assumption.

For induced operator norms, \(\|ABx\|\leq\|A\|\|B\|\|x\|\), so \(\|AB\|\leq\|A\|\|B\|\). In orthonormal coordinates the largest absolute matrix coefficient is at most its operator norm, and the operator norm is at most \(n\) times that coefficient maximum for an \(n\)-by-\(n\) matrix, by two scalar Cauchy–Schwarz estimates. Thus coordinate completeness implies matrix norm completeness. The zero-dimensional matrix space has its single element and satisfies the same assertions separately. This proves EC-012.

Suppose \(\|B\|\leq q<1\), with \(q\geq0\), and put \(S_N=\sum_{j=0}^N(-B)^j\). For \(M>N\),
\[
\|S_M-S_N\|\leq\sum_{j=N+1}^M q^j\leq\frac{q^{N+1}}{1-q}.
\]
If \(q=0\), then \(B=0\) and the conclusion is immediate; otherwise this bound tends to zero. Matrix completeness gives a limit \(S\), and the norm bound is \(\|S\|\leq(1-q)^{-1}\). Direct finite multiplication yields
\[
(I+B)S_N=S_N(I+B)=I-(-B)^{N+1}.
\]
Continuity of multiplication and \(\|B^{N+1}\|\leq q^{N+1}\) give both inverse identities for \(S\). This proves EC-013 for every contraction constant, including the \(q=1/2\) used in U001. No derivative of an infinite series is taken.

## AN03-MFD-010 — The bracket estimate and fixed powers

For \(\xi\in\mathbb R^n\), direct differentiation gives
\[
\nabla\langle\xi\rangle=\frac{\xi}{\sqrt{1+|\xi|^2}},\qquad
|\nabla\langle\xi\rangle|\leq1.
\]
Apply the segment fundamental theorem to
\(t\mapsto\langle\eta+t(\xi-\eta)\rangle\), use the chain rule and Cauchy–Schwarz, and integrate on \([0,1]\). The result is
\[
|\langle\xi\rangle-\langle\eta\rangle|\leq|\xi-\eta|.
\]
For a fixed \(s\in\mathbb R\) and \(0<a\leq r\leq b<\infty\), monotonicity of the real power, reversed when \(s<0\), gives
\[
\min(a^s,b^s)\leq r^s\leq\max(a^s,b^s).
\]
Both endpoints are finite and positive, and \(s=0\) gives one. This is EC-014 for arbitrary real exponents, without an integer or sign restriction. If a zero-dimensional coordinate factor occurs, its bracket is the constant one and the estimate is immediate.
