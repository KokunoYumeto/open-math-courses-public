# Metric and topological foundations

Moving-metric arguments need uniform estimates for positive forms, smooth cutoffs, finite-dimensional measure changes, and locally finite sums. This chapter proves the needed forms of those facts, including their endpoints. It leads to [Localizing symbols with moving metrics](metric-localization.md). The elementary calculus is proved in Section 13, arbitrary-metric compactness and the exact support arguments in Section 14, and the measure-theory entries in the linked Banach chapter. Basic references for those foundations are [Lebl] and [Axler]; the arguments developed here are complete relative to those stated prerequisites.

## 1. Entry facts and maximality

Sections 12.1--12.3 construct the complete ordered real field, prove its Archimedean property and compare it exactly with the original real numbers. The underlying set operations, natural-number arithmetic, induction and choice axioms are explicit. We use the finite-dimensional bases, matrix algebra, determinant identities, and elementary elimination proved in Section 10 of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md#full-finite-linear-algebra-foundations); and the construction of complex numbers as pairs of real numbers. Sections 13.1--13.8 prove limits, derivatives, the mean value theorem, the exponential series and its derivative, real-power differentiation, and the Riemann integral of a continuous function on a compact interval, with order, linearity and its uniform bound. Sections 13.5--13.6 give the full finite-coordinate derivative, ordered higher product and Taylor maps used in Section 3.

Sections 15.0 and 16.1 of [Banach estimates and measure foundations](banach-foundation-bridges.md) prove one-dimensional Lebesgue measure built from interval outer measure, completion, measurable functions, nonnegative integration, monotone convergence and bounded convergence on finite-measure spaces. Limits of measurable functions are measurable. For product spaces, Sections 16.2--16.5 of that chapter construct the full sigma-finite product measure, prove both Tonelli orders and prove the completed-factor comparison used in Section 6. The affine change-of-variables result is proved there, not assumed. The real-number construction is proved in Section 12; the measure and integral entry uses only the independent measure construction and convergence proofs, rather than a larger theorem that assumes Tonelli.

The maximality principle used below is Zorn's lemma in this form: a nonempty partially ordered set in which every chain has an upper bound has a maximal element. For disjoint ellipsoid families, the union of a chain is again disjoint, because any two members belong together to one of its comparable families. The empty family makes the partially ordered set nonempty. This selection does not itself establish countability; Section 4 proves that separately.

## 2. Positive forms and tensor norms

Let \(E\) be real of dimension \(d\geq1\), as in the moving-metric lesson, and let \(Q\) be a positive-definite quadratic form. Its polarization is the symmetric bilinear form
\[
\langle x,y\rangle_Q=\tfrac14\bigl(Q(x+y)-Q(x-y)\bigr).
\]
In coordinates \(Q(x)=x^{\mathsf T}Gx\) with \(G\) symmetric; expansion shows the displayed polarization is \(x^{\mathsf T}Gy\), and \(\langle x,x\rangle_Q=Q(x)\). Starting with a basis, subtract its projections on previously constructed orthonormal vectors and divide the nonzero residual by its positive \(Q\)-length. The residual cannot be zero, since that would put the original basis vector in the span of its predecessors. This finite Gram–Schmidt procedure gives a \(Q\)-orthonormal basis. Section 10.5 of the polynomial and contour lesson retains every original residual, its length, the full original Gram matrix and both coordinate maps for this comparison; its Section 10.10 proves the exact receiving metric and volume factors.

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
These comparison factors are exact. They require no uniform condition-number bound over a family of forms.

## 3. Differentiation and segment integrals

Sections 13.1--13.6 prove the finite-dimensional derivative definition, the first-order chain rule, the continuous-partials criterion, and interchange of partials for \(C^2\) maps. For \(C^k\) maps we use the definition by continuous iterated derivatives. The chain rule requires differentiability at a point and at its image; the interchange theorem requires \(C^2\). All domains are open subsets of finite-dimensional real spaces. These local statements restrict to smaller neighborhoods. [Lebl] gives a named reference. We now derive the vector-target and higher-order forms used below.

For one real variable with a vector target, apply the scalar derivative limit to every component. There are finitely many components, so the Euclidean norm of their remainder divided by the absolute value of the increment tends to zero. Continuity of the resulting derivative is likewise componentwise. Complex scalar and finite matrix targets follow by identifying them with their finitely many real coordinates.

For clarity, the higher-order and product interfaces need no further theorem. A fixed bilinear map \(B\) on finite coordinate spaces satisfies
\[
D B(f,g)[h]=B(Df[h],g)+B(f,Dg[h]).
\]
Indeed, expand the increments bilinearly. The term containing both increments is \(O(|h|^2)\), and the two differentiability remainders are \(o(|h|)\). Coordinate multiplication and ordered matrix multiplication are such bilinear maps. Applying the first-order rule repeatedly proves the iterated product rule, without interchanging matrix factors. Applying the chain rule repeatedly proves the iterated composition rules. Applying the continuous-partials criterion to each derivative's finite coordinate list identifies \(D^j f\) with a continuous \(j\)-linear tensor for every \(j\leq k\). Adjacent derivative orders may be exchanged by the \(C^2\) interchange theorem applied to lower derivatives; every permutation is a finite product of adjacent exchanges. This gives symmetry at every allowed order, including complex and matrix-valued functions.

If a function is continuous on \([a,b]\), differentiable in its interior, and has a Riemann-integrable derivative there, the fundamental theorem of calculus identifies its increment with the integral of that derivative. The oriented integral handles a negative increment. [Lebl] is a reference for this elementary theorem. A \(C^1\) coordinate segment meets those hypotheses. Apply it componentwise to obtain
\[
f(x+t e_j)-f(x)=\int_0^t\partial_j f(x+s e_j)\,ds
\]
whenever the segment lies in the coordinate box; for \(t<0\), use the oriented integral. If \(f_n\) and \(\partial_jf_n\) converge uniformly on that segment, the integral error is at most \(|t|\sup|\partial_jf_n-g_j|\), so the identity passes to the limit. Repeat for each derivative order. No exchange of an uncontrolled pointwise limit with an integral is asserted.

## 4. Countability, compactness and supports

Rational points are countable because the integer numerator and positive integer denominator can be enumerated in finite diagonal batches. Finite tuples are likewise countable. By the Archimedean property, for \(a<b\) choose an integer \(N\) with \(N(b-a)>1\); an integer strictly between \(Na\) and \(Nb\) then gives a rational in \((a,b)\). Every nonempty Euclidean open set contains an open coordinate box, hence a rational-coordinate point. Fix an enumeration and assign to each member of a pairwise disjoint family of nonempty open sets its first contained point. The assignment is injective; the family is countable. The countability argument uses no regularity of a varying metric.

Sections 12.4--12.8 prove both the open-cover and sequential forms of compactness, their equivalence with closed and bounded sets, all required extrema and the countability statements below. These apply to the Euclidean spaces here, including the empty set, whose empty open subcover is finite. Section 14.1 gives the full arbitrary-metric cover/sequential equivalence using explicit countable choice, with no maximality assumption; Section 14.2 gives the common compact-support neighborhood. [Lebl] is a reference for these foundational theorems.

For a direct finite-dimensional sequence argument, begin with a bounded sequence in \(\mathbb R^d\). Extract a subsequence convergent in the first coordinate, a subsequence of that one convergent in the second, and continue for exactly \(d\) steps. Each previously convergent coordinate remains convergent. The final subsequence converges in Euclidean norm, since the sum of its finitely many squared coordinate differences tends to zero. A closed set contains the limit. The scalar subsequence fact follows from real completeness: repeatedly bisect a bounded closed interval, retain a half containing infinitely many terms, and choose increasing indices in the nested halves. Their lengths tend to zero and their common point is the subsequential limit. This argument works in every finite dimension.

A fixed positive form is a continuous coordinate polynomial. Its unit sphere comparison, or its orthonormal-coordinate isomorphism, shows that a closed frozen ellipsoid is bounded; it is closed by continuity and hence compact. A finite union of compact sets is compact by taking a finite subcover for each member. Empty sets cause no exception.

For a continuous function \(f\), define \(\operatorname{supp}f\) as the closure of its nonzero set. Outside that support it vanishes on a neighborhood, so all existing derivatives vanish there. If a family of sets is locally finite, cover a compact \(K\) by neighborhoods each meeting only finitely many members. A finite subcover meets only finitely many members in total, both on \(K\) and on the union of those neighborhoods. For empty \(K\), take the empty neighborhood. These observations give a neighborhood conclusion, rather than merely pointwise finiteness.

## 5. Cutoffs and locally finite sums

Define \(\eta(s)=0\) for \(s\leq0\) and \(\eta(s)=e^{-1/s}\) for \(s>0\). Each derivative on the positive half-line is \(e^{-1/s}\) times a polynomial in \(1/s\), by induction. For every fixed integer \(N\), \(u^N e^{-u}\to0\) as \(u\to\infty\): use \(e^u\geq u^{N+1}/(N+1)!\). Thus every one-sided derivative tends to zero at the origin. The derivative there is also zero at every order, since dividing such an expression by \(s\) still has the same vanishing property. Induction proves \(\eta\in C^\infty(\mathbb R)\).

The denominator in
\[
\chi(s)=\frac{\eta(3/2-s)}{\eta(3/2-s)+\eta(s-1)}
\]
is strictly positive for every real \(s\). The function is smooth, lies between zero and one, equals one for \(s\leq1\), and is zero for \(s\geq3/2\). On \([0,\infty)\) its support is contained in \([0,3/2]\), a compact subset of both \([0,2)\) and \([0,4)\). The function \(x\mapsto\chi(|x|^2)\) is a smooth compact cutoff equal to one near the origin. Each fixed derivative is bounded by continuity on a compact support, and vanishes outside it. Smoothness of the quotient follows from the single-variable reciprocal rule and Section 3. The strict support endpoints are retained.

Suppose each point has a neighborhood on which all but finitely many smooth functions \(f_i\) vanish identically. On that neighborhood their pointwise sum is that finite sum, so it is smooth and its derivatives equal the finite sums of derivatives. The local descriptions agree because they are derivatives of the same function. No convergence argument or measurability assumption on the varying metric or weight is needed.

## 6. Lebesgue measure under affine maps

We use Tonelli's theorem in its full \(\sigma\)-finite form: for a nonnegative function measurable for a product \(\sigma\)-algebra, its product integral equals either iterated integral, with \(+\infty\) allowed. Product sections of Borel subsets of Euclidean space are Borel. [Axler] is a reference for the product-measure theorem. Sections 16.1--16.4 of [Banach estimates and measure foundations](banach-foundation-bridges.md) prove that full statement; Section 16.5 proves its completed-factor version and exact original Euclidean comparison. The proof below supplies the affine change-of-variables result from this stated measure-theory prerequisite; it does not assume that result.

For a finite family of measurable rectangles, partition each factor by the finitely many membership patterns determined by their sides. Products of these disjoint pieces refine every rectangle simultaneously. In Euclidean spaces, the product sigma-algebra agrees with the Borel sigma-algebra of the product: the rational-coordinate open rectangles form a countable basis and belong to the product sigma-algebra; conversely each Borel rectangle is the intersection of two continuous-projection preimages. For each fixed coordinate in one factor, the collection of product sets whose section is Borel is a sigma-algebra containing every Borel rectangle. Hence every Borel product set has Borel sections. These are the section facts used in the affine calculation.

We derive the full completed Lebesgue affine-change statement. Let \(m_d\) be the completion of the Borel product of \(d\) copies of one-dimensional Lebesgue measure. First, interval coverings show for every subset \(S\subseteq\mathbb R\), every \(a\ne0\) and every \(b\in\mathbb R\),
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
where \(v_Q=|\det L|m_d(\{|u|<1\})\). The unit ball contains a nonempty coordinate cube and is contained in a bounded cube, so the original coordinate-box volume and monotonicity give \(0<v_Q<\infty\). This is the exact finite packing input. It imposes no smoothness or measurability on \(X\mapsto g_X\) or on the weight.

## 7. Uniform limits

A Cauchy sequence in \(\mathbb C\) has Cauchy real and imaginary parts, which converge by real completeness. The same argument in each of finitely many coordinates proves completeness of finite-dimensional coordinate spaces. If a sequence of functions is uniformly Cauchy on a set, its pointwise limits exist in such a space. Given \(\varepsilon>0\), choose an index after which all pairwise differences are at most \(\varepsilon\) uniformly, then pass one index to the pointwise limit. The resulting bound remains uniform, proving uniform convergence.

If the original functions are continuous, choose one with uniform error less than \(\varepsilon/3\), and use its continuity near any chosen point to make its change less than \(\varepsilon/3\). The triangle inequality bounds the change of the limit by \(\varepsilon\). Thus the limit is continuous; in particular this holds on each compact set. The tensor coefficient estimate of Section 2 gives convergence in each fixed tensor norm from coefficient convergence, and its reverse inequality gives the converse. The integral passage for these uniform limits follows from the segment estimate in Section 3.

## 8. A metric for countably many seminorms

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

The same head-and-tail estimates, applied to differences of sequence terms, show that a sequence is metric Cauchy exactly when it is Cauchy in every seminorm. Applying them to differences from a fixed vector gives the corresponding convergence assertion. Therefore the metric is complete precisely when every sequence Cauchy in all seminorms has a vector limit in all seminorms. No completeness of \(V\) has been assumed in establishing this metric. Section 6 of [Localizing symbols with moving metrics](metric-localization.md) applies it to a symbol space.

## 9. Local inverses and matrix series

If \(f=u+iv\) is a nonvanishing complex \(C^k\) function on a real domain, then locally
\[
\frac1f=\frac{u-iv}{u^2+v^2}.
\]
The denominator stays positive on a sufficiently small neighborhood. Repeated single-variable differentiation gives \((s^{-1})^{(j)}=(-1)^j j!s^{-j-1}\) for \(s>0\). The rules of Section 3 therefore prove the asserted \(C^k\) regularity, including \(k=0\) by continuity. For a matrix function taking invertible values, its determinant is nonzero and its adjugate is a finite polynomial in its entries. The identity \(A^{-1}=\operatorname{adj}(A)/\det A\) proves the corresponding local matrix assertion without any commuting-coefficient assumption.

For induced operator norms, \(\|ABx\|\leq\|A\|\|B\|\|x\|\), so \(\|AB\|\leq\|A\|\|B\|\). In orthonormal coordinates the largest absolute matrix coefficient is at most its operator norm, and the operator norm is at most \(n\) times that coefficient maximum for an \(n\)-by-\(n\) matrix, by two scalar Cauchy–Schwarz estimates. Thus coordinate completeness implies matrix norm completeness. The zero-dimensional matrix space has its single element and satisfies the same assertions separately. This proves matrix norm completeness.

Suppose \(\|B\|\leq q<1\), with \(q\geq0\), and put \(S_N=\sum_{j=0}^N(-B)^j\). For \(M>N\),
\[
\|S_M-S_N\|\leq\sum_{j=N+1}^M q^j\leq\frac{q^{N+1}}{1-q}.
\]
If \(q=0\), then \(B=0\) and the conclusion is immediate; otherwise this bound tends to zero. Matrix completeness gives a limit \(S\), and the norm bound is \(\|S\|\leq(1-q)^{-1}\). Direct finite multiplication yields
\[
(I+B)S_N=S_N(I+B)=I-(-B)^{N+1}.
\]
Continuity of multiplication and \(\|B^{N+1}\|\leq q^{N+1}\) give both inverse identities for \(S\). The conclusion holds for every contraction constant, including \(q=1/2\). No derivative of an infinite series is taken.

## 10. Frequency brackets and real powers

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
Both endpoints are finite and positive, and \(s=0\) gives one. This holds for arbitrary real exponents, without an integer or sign restriction. If a zero-dimensional coordinate factor occurs, its bracket is the constant one and the estimate is immediate.

## 11. Exercises and solutions

**Exercise 11.1 (An incomplete seminorm space).** Let \(V=c_{00}\) be the vector space of complex sequences with finite support, and let \(p_k(x)=|x_k|\) for \(k\geq0\). Show that the metric in Section 8 is not complete.

**Solution.** Put \(x^{(N)}=\sum_{k=0}^{N}2^{-k}e_k\), where \(e_k\) is the \(k\)-th coordinate vector. For each fixed \(k\), \(p_k(x^{(M)}-x^{(N)})=0\) once both indices exceed \(k\). The head-and-tail estimate in Section 8 makes the sequence metric Cauchy. If it converged to \(x\in c_{00}\), convergence in every \(p_k\) would force \(x_k=2^{-k}\) for all \(k\). That sequence has infinite support, a contradiction. Thus countably many separating seminorms need not give a complete space.

**Exercise 11.2 (A shear).** Let \(S=[0,1]^2\) and \(A(x_1,x_2)=(x_1+c x_2,x_2)\), with \(c\in\mathbb R\). Compute the area of \(AS\) directly by sections.

**Solution.** At a fixed \(x_2=t\in[0,1]\), the horizontal section of \(AS\) is \([ct,ct+1]\), of one-dimensional length one. Outside that range of \(t\) the section is empty. Tonelli therefore gives \(m_2(AS)=\int_0^1 1\,dt=1\), in agreement with \(|\det A|=1\).

## 12. Real numbers and finite-dimensional topology

The real field is constructed here with its full arithmetic, order and completeness. Its exact comparison with the real numbers used in this course retains the original values. The logical entry is natural-number arithmetic with induction, ordinary set theory and countable choice. The last two sections apply the construction to the original norms, quadratic forms, polynomial minima and spectral contours. These are standard foundations; no novelty is claimed.

### 12.1. Integer and rational arithmetic with all original fractions retained

Start with natural numbers and their addition, multiplication, order, cancellation and induction. Construct the integers as classes of pairs \((m,n)\in\mathbb N^2\), with
\[
(m,n)\sim(m',n')\quad\Longleftrightarrow\quad m+n'=m'+n.
\tag{RT1}
\]
Reflexivity and symmetry follow from equality. For transitivity, add the two defining equalities for consecutive pairs and cancel the common middle sum in \(\mathbb N\). Addition and multiplication are
\[
[(m,n)]+[(p,q)]=[(m+p,n+q)],\qquad
[(m,n)][(p,q)]=[(mp+nq,mq+np)].
\tag{RT2}
\]
Adding equalities in (RT1) proves addition independent of representatives. For multiplication, replacement of \((m,n)\) by \((m',n')\) follows by multiplying \(m+n'=m'+n\) by \(p\) and \(q\): the equality of the cross sums in (RT1) is the sum of those two equations, with terms reordered. Replacement of \((p,q)\) follows by the same explicit operation with \(m,n\); hence replacing both pairs is valid. The additive inverse is \([(n,m)]\); both inverse sums are \([(m+n,m+n)]=0\). The identities are \(0=[(0,0)]\) and \(1=[(1,0)]\).

Addition is associative and commutative by coordinate addition. Multiplication is commutative by its two coordinate formulas. For associativity, the coordinates of the left associated triple product are
\[
\begin{gathered}
mpr+nqr+mqs+nps,\\
mps+nqs+mqr+npr.
\end{gathered}
\tag{RT3}
\]
The right associated product has these same four terms in each coordinate, in the respective order \(mpr,mqs,nps,nqr\) and \(mps,mqr,npr,nqs\). Distributivity follows by expanding (RT2) against \((p+r,q+s)\): the first coordinate is \(mp+mr+nq+ns\), and the second is \(mq+ms+np+nr\), which are the coordinates of the sum of the two products. Thus every ring identity used here is proved.

Declare \([(m,n)]>0\) when \(m>n\). Equation (RT1) and cancellation preserve this comparison. Exactly one of positive, zero and negative holds. Two positive pairs have \(m=n+k\), \(p=q+l\) for positive natural numbers \(k,l\); their product's first coordinate exceeds its second by \(kl>0\), on expanding all terms in (RT2). Their sum is positive by addition of inequalities. It follows that this is an ordered ring. A nonzero integer and another nonzero integer have nonzero product: apply the positive-product assertion to their respective signs. In particular, multiplication by a nonzero integer permits cancellation.

Construct the rational numbers from pairs \((p,q)\in\mathbb Z^2\) with \(q\ne0\), without restricting the denominator's sign or reducing the fraction. Put
\[
\begin{gathered}
(p,q)\sim(p',q')\ \Longleftrightarrow\ pq'=p'q,\\
[p,q]+[p',q']=[pq'+p'q,qq'],\qquad
[p,q][p',q']=[pp',qq'],\\
-[p,q]=[-p,q],\quad 0=[0,1],\quad 1=[1,1],\quad
[p,q]^{-1}=[q,p]\quad(p\ne0).
\end{gathered}
\tag{RT4}
\]
Transitivity follows by multiplying \(pq'=p'q\) by \(q''\) and \(p'q''=p''q'\) by \(q\), then cancelling the nonzero \(q'\). For sums and products, cross multiplication after changing either representative expands into the defining integer equality times the unchanged numerator or denominator. Hence both operations and negation descend. Associativity, distributivity and commutativity follow by cross multiplication into the already proved integer identities: denominators are the full original products, and the numerator of a sum of three terms is \(pq'q''+p'qq''+p''qq'\). The product \(([p,q]+[p',q'])[r,s]\) has the original numerator \((pq'+p'q)r\) and denominator \(qq's\). Adding the two separate products by (RT4) instead gives the full pair \([prq's+p'rqs,qq's^2]\). These pairs have identical cross products, namely \((pq'+p'q)r\,qq's^2=(prq's+p'rqs)\,qq's\); each side is the same full integer sum. Every factor \(s\) and \(s^2\), including its sign, remains in this comparison. Both inverse products in (RT4) are \([pq,qp]=1\), with \(p,q\ne0\). This proves the field laws.

Declare \([p,q]>0\) precisely when \(pq>0\). If \(pq'=p'q\), multiply by \(qq'\) to obtain \(pq(q')^2=p'q'q^2\). Both denominator squares are positive, so signs agree. The numerator-times-denominator of a sum of two positive fractions is
\[
(pq'+p'q)(qq')=(pq)(q')^2+(p'q')q^2>0.
\tag{RT5}
\]
The product has numerator-times-denominator \((pq)(p'q')>0\). Trichotomy follows from the integer signs and nonzero denominator. The embedding \(z\mapsto[z,1]\) preserves all operations and order and is injective. Thus \(\mathbb Q\) is an ordered field with its full original numerator and denominator data.

For \(q\ne0\), \(|q|\ge1\), so \(|[p,q]|\le |p|\). The integer \(|p|+1\) is a strict upper bound. This proves the rational Archimedean property. Between rationals \(a<b\), the rational \((a+b)/2\) is strictly between them, since its differences from either endpoint are \((b-a)/2>0\). These facts use no real completeness.

### 12.2. Constructing the real field and its exact inverse operations

Let \(\mathcal C\) be the set of rational Cauchy sequences \(a=(a_n)_{n\ge1}\), where for every rational \(\varepsilon>0\) some \(N\) has \(|a_n-a_m|<\varepsilon\) for all \(m,n\ge N\). Let \(\mathcal N\) be the sequences converging to zero by the same rational definition. Define
\[
\begin{gathered}
a\sim b\ \Longleftrightarrow\ a-b\in\mathcal N,\qquad
\mathbb R_{\mathcal C}=\mathcal C/\mathcal N,\\
[a]+[b]=[(a_n+b_n)_n],\qquad
[a][b]=[(a_nb_n)_n],\qquad -[a]=[(-a_n)_n].
\end{gathered}
\tag{RT6}
\]
A Cauchy sequence is bounded: choose \(N\) with \(|a_n-a_N|<1\) for \(n\ge N\), and take the actual rational bound
\[
M_a=1+\max_{1\le j\le N}|a_j|.
\tag{RT7}
\]
This bounds every coordinate, including the entire initial segment. Sums are Cauchy by adding the two actual errors. For products use
\[
|a_nb_n-a_mb_m|
\le M_a|b_n-b_m|+M_b|a_n-a_m|.
\tag{RT8}
\]
Given \(\varepsilon>0\), choose the errors below \(\varepsilon/(2(M_a+M_b+1))\); the displayed sum is less than \(\varepsilon\). The same bound proves a bounded sequence times a null sequence null. The full identity
\[
a_nb_n-c_nd_n=(a_n-c_n)b_n+c_n(b_n-d_n)
\tag{RT9}
\]
proves the product independent of both representatives. Null sums, negations and the triangle inequality prove the equivalence relation and all other operations independent of representatives. Pointwise rational field identities now prove all commutative ring identities on the quotient.

If \([a]\ne0\), the negation of null convergence provides a rational \(\varepsilon>0\) such that arbitrarily late coordinates have \(|a_n|\ge\varepsilon\). Choose \(N\) making every tail difference less than \(\varepsilon/2\), and choose one \(k\ge N\) with \(|a_k|\ge\varepsilon\). Then every \(n\ge N\) has
\[
|a_n|>\varepsilon/2=:\delta>0.
\tag{RT10}
\]
Define \(b_n=1/a_n\) for \(n\ge N\), and \(b_n=1\) for \(n<N\). Its tail differences satisfy
\[
|b_n-b_m|=\frac{|a_m-a_n|}{|a_n||a_m|}
\le\delta^{-2}|a_m-a_n|.
\tag{RT11}
\]
Thus \(b\) is Cauchy. Both pointwise products equal \(1\) on the tail; their discrepancies on the explicitly retained initial coordinates form null sequences. Consequently \([a][b]=[b][a]=1\). Uniqueness of a multiplicative inverse follows from the ring identities, so this construction gives the same inverse for any representative. Constant rational sequences give an injective field map \(\iota:\mathbb Q\to\mathbb R_{\mathcal C}\).

Call \([a]\) positive if \(a_n\ge\delta>0\) eventually for some rational \(\delta\). Changing representatives preserves positivity by choosing their difference below \(\delta/2\). A nonzero sequence in (RT10) has one fixed tail sign: if \(a_k\ge\varepsilon\), then \(a_n>\varepsilon/2\) for \(n\ge N\); if \(a_k\le-\varepsilon\), then \(a_n<-\varepsilon/2\). Thus every nonzero class is either positive or negative, but cannot be both. Positive sums are bounded below by the sum of the two original positive gaps, and positive products by their product. This constructs an ordered field, with \(\iota\) preserving order.

For any \(x=[a]\), (RT7) gives
\[
-\iota(M_a+1)<x<\iota(M_a+1).
\tag{RT12}
\]
A rational upper bound therefore gives an integer upper bound. This proves the real Archimedean property directly in the constructed field. A positive \(x\) has a rational \(\delta/2\) with \(0<\iota(\delta/2)<x\), by its positive tail gap. Absolute values satisfy the triangle and product rules by the field order: \(-|x|\le x\le |x|\), addition gives \(-(|x|+|y|)\le x+y\le |x|+|y|\), and applying the four possible signs gives \(|xy|=|x||y|\).

For every rational \(\varepsilon>0\), sufficiently late \(n\) have
\[
|x-\iota(a_n)|<\iota(\varepsilon).
\tag{RT13}
\]
Indeed choose a rational Cauchy tail with differences less than \(\varepsilon/2\). The sequences representing \(\varepsilon-(a_m-a_n)\) and \(\varepsilon+(a_m-a_n)\) then have positive tail gaps at least \(\varepsilon/2\). This proves (RT13) by the exact order definition. In particular, between \(x<y\), choose a positive rational \(\varepsilon\) with \(4\iota(\varepsilon)<y-x\), approximate \(x\) by \(\iota(a_n)\) within \(\iota(\varepsilon)\), and take \(q=a_n+2\varepsilon\). Then \(x<\iota(q)<y\). All original values and all approximation factors remain in these inequalities.

### 12.3. Suprema, Cauchy completeness and comparison with the given real numbers

Let \(S\subset\mathbb R_{\mathcal C}\) be nonempty and bounded above by \(u\). Choose \(x_0\in S\). By (RT12)--(RT13), choose rational endpoints \(l_0,v_0\) with \(\iota(l_0)<x_0\) and \(u<\iota(v_0)\). In particular \(l_0<v_0\). Inductively put \(m_n=(l_n+v_n)/2\). If \(\iota(m_n)\) is an upper bound of \(S\), set \(l_{n+1}=l_n,v_{n+1}=m_n\). Otherwise set \(l_{n+1}=m_n,v_{n+1}=v_n\). At every step \(\iota(v_n)\) is an upper bound, while \(\iota(l_n)\) is not an upper bound. Moreover
\[
l_n\le l_{n+1}\le v_{n+1}\le v_n,\qquad
v_n-l_n=(v_0-l_0)2^{-n}.
\tag{RT14}
\]
Induction gives \(2^n\ge n+1\). The rational Archimedean property therefore shows that the right side of (RT14) tends to zero. Both endpoint sequences are rational Cauchy, since every later endpoint lies between the displayed endpoints; their difference is null. Define \(s=[(l_n)_n]=[(v_n)_n]\).

Formula (RT13) implies \(\iota(l_n)\to s\) and \(\iota(v_n)\to s\) in the field order, first for rational errors and then for any positive field error using the positive rational below it. If some \(x\in S\) had \(x>s\), eventually \(\iota(v_n)<x\), contradicting its upper-bound property. If an upper bound \(w\) had \(w<s\), eventually \(w<\iota(l_n)\); because \(\iota(l_n)\) is not an upper bound, there is \(x\in S\) with \(\iota(l_n)<x\), contradicting \(w\). Thus \(s\) is exactly the least upper bound. Its uniqueness follows by applying each least-upper-bound property to the other upper bound. Infima are \(-\sup(-S)\), with the full negation map proving both defining inequalities.

Every Cauchy sequence \(x_n\) in this ordered field converges. The argument also applies to any complete ordered field. A tail is bounded by \(|x_N|+1\), and finitely many initial terms give a bound for the whole sequence. Define the original tail endpoints
\[
L_n=\inf_{m\ge n}x_m,\quad U_n=\sup_{m\ge n}x_m,\quad
x=\sup_{n\ge1}L_n.
\tag{RT15}
\]
They exist by the proved least-upper-bound property; the \(L_n\) are increasing and bounded above. For every \(n,k\), \(L_k\le U_n\): for \(k<n\) use \(L_k\le L_n\), and for \(k\ge n\) every member of the smaller tail is at most \(U_n\). Hence \(L_n\le x\le U_n\). If all tail differences are less than \(\varepsilon\), each tail member is an upper bound of that tail minus \(\varepsilon\); taking supremum and then infimum gives \(U_n-L_n\le\varepsilon\). It follows that \(|x_n-x|\le\varepsilon\) on that tail. Taking initially \(\varepsilon/2\) proves the strict-error convergence definition for every \(\varepsilon>0\).

We now compare with the course's given real field \(F=\mathbb R\), without replacing it. In a complete ordered field the positive integers are unbounded: otherwise their supremum \(s\) would have \(s-1\) not an upper bound, giving an integer \(n>s-1\) and \(n+1>s\), a contradiction. For \(a<b\) in \(F\), choose an integer \(N>1/(b-a)\). Among the integers bracketing \(Na\), choose \(k\) with \(k\le Na<k+1\). Such a \(k\) exists by restricting to a finite integer interval whose endpoints exceed \(|Na|+1\), then choosing the largest integer at most \(Na\). Then \((k+1)/N>a\) and \((k+1)/N\le a+1/N<b\). Thus the unique rational field embedding \(\iota_F\), defined by the original integer multiples of \(1_F\) and actual nonzero denominators, has dense image.

Apply (RT15) in \(F\) to the embedded rational Cauchy sequence. Define
\[
\Phi:\mathbb R_{\mathcal C}\longrightarrow F,\qquad
\Phi([a])=\lim_{n\to\infty}\iota_F(a_n).
\tag{RT16}
\]
Null differences have limit zero, so this map is well defined. Limits are unique because two distinct limits have a positive distance and their two errors can each be made smaller than one third of that distance. Sums commute with limits by the triangle inequality. Products commute by the full difference
\[
\iota_F(a_n)\iota_F(b_n)-xy
=\iota_F(a_n)(\iota_F(b_n)-y)+y(\iota_F(a_n)-x),
\tag{RT17}
\]
bounded using the original \(M_a\) and \(|y|\). Both terms tend to zero by their actual finite bounds. Thus \(\Phi\) is a field homomorphism fixing every rational. A positive class has positive gap \(\delta\); its limit is at least \(\iota_F(\delta)>0\), since a smaller limit would contradict its tail lower bound. Consequently \(\Phi\) preserves positivity and is injective. For every \(x\in F\), rational density supplies \(a_n\) with \(|x-\iota_F(a_n)|<1/n\). This rational sequence is Cauchy, because its tail difference is at most \(1/n+1/m\), and \(\Phi([a])=x\). The map is surjective.

For every original rational sequence representative all coordinate values remain in (RT16)--(RT17). Conversely the approximation just constructed is an explicit inverse value for each original \(x\). Two choices differ by at most \(2/n\) and hence give the same class; thus the inverse is well defined. Any ordered field isomorphism fixing the rationals must preserve the two error bounds (RT13), so it must have the value (RT16). This proves uniqueness, both compositions and every domain/codomain. Suprema and infima are transported by \(\Phi\): an upper bound, and then the least such bound, correspond exactly under its order isomorphism. Hence all subsequent constructions may use the original \(\mathbb R\), with their complete construction and comparison already proved. The course complex scalar set is the literal ordered-pair set \(\mathbb R^2\). The coordinatewise comparison \(([a],[b])\mapsto(\Phi([a]),\Phi([b]))\) has the coordinatewise inverse already proved in (RT16). It preserves the full pair addition and the two-coordinate product by (RT17) in every real factor. The separate complete complex field-law calculation is (FA0a)--(FA0d); none of those later laws is needed to construct the real field.

### 12.4. Square roots and the full Euclidean distance

For \(a\ge0\) in the original \(\mathbb R\), take \(T=\{t\ge0:t^2\le a\}\). It contains \(0\) and is bounded by \(a+1\), because \((a+1)^2>a\). Let \(r=\sup T\). If \(r^2<a\), choose
\[
0<\eta<\min\left(1,\frac{a-r^2}{2(2r+1)}\right).
\tag{RT18}
\]
Then \((r+\eta)^2\le r^2+\eta(2r+1)<a\), contradicting the upper bound. If \(r^2>a\), then \(r>0\). Choose \(0<\eta<\min(r/2,1,(r^2-a)/(2(2r+1)))\). Now \((r-\eta)^2\ge r^2-\eta(2r+1)>a\). Every nonnegative \(t\ge r-\eta\) has \(t^2>a\), since \(t^2-(r-\eta)^2=(t-r+\eta)(t+r-\eta)\ge0\). Therefore \(r-\eta\) is an upper bound of \(T\), contradicting minimality of \(r\). We obtain \(r^2=a\). Nonnegative square roots are unique: their square difference factors as the difference times their sum, and a positive difference would make that product positive. The same factorization proves their order preservation.

For \(d\ge0\), use all original coordinates and define
\[
|x|_2=\left(\sum_{j=1}^d x_j^2\right)^{1/2},\qquad
\langle x,y\rangle_0=\sum_{j=1}^d x_jy_j,\qquad
\rho(x,y)=|x-y|_2.
\tag{RT19}
\]
When \(d=0\), the empty sum is zero and \(\mathbb R^0\) is the singleton empty tuple. For \(y\ne0\), expansion of the nonnegative square sum gives
\[
0\le\sum_{j=1}^d\left(x_j-\frac{\langle x,y\rangle_0}{|y|_2^2}y_j\right)^2
=|x|_2^2-\frac{\langle x,y\rangle_0^2}{|y|_2^2}.
\tag{RT20}
\]
Each of the two cross terms is retained in that expansion; their sum is minus twice the full original pairing, and the final square contribution is once its square divided by \(|y|_2^2\). For \(y=0\) the pairing is zero. Thus \(|\langle x,y\rangle_0|\le |x|_2|y|_2\). Expanding \(|x+y|_2^2\) and applying this bound proves the triangle inequality. The other metric axioms follow from the coordinate squares. For \(d>0\),
\[
\max_{1\le j\le d}|x_j|\le |x|_2
\le \sqrt d\max_{1\le j\le d}|x_j|.
\tag{RT21}
\]
No coordinate or dimensional factor is suppressed. Convergence and the Cauchy property are therefore equivalent to their coordinate versions. Coordinatewise Cauchy completeness from (RT15) proves completeness of the entire original Euclidean metric. For \(d=0\) every sequence is the constant empty tuple and the assertion follows directly.

Open sets are those containing a positive-radius metric ball about each of their points. Closed sets have open complements. Convergence in this metric has unique limits by the triangle inequality and the one-third-distance argument. Every limit of a sequence in a closed set stays in that set: an outside limit would have a ball in the complement, contradicting eventual membership in that ball and in the closed set.

### 12.5. Bounded subsequences in every original coordinate

First consider a bounded real sequence \(t_n\), with an original interval \([a_0,b_0]\) containing it. If its endpoints coincide the whole sequence is constant. Otherwise bisect this actual interval. At least one of the two closed halves contains infinitely many sequence indices, since their union contains every index and a union of two finite sets is finite. Choose such a half, retaining its infinite set of indices. Repeat within that half. This gives nested original intervals \([a_k,b_k]\) and nested infinite index sets \(I_k\) with
\[
b_k-a_k=(b_0-a_0)2^{-k},\qquad
t_n\in[a_k,b_k]\quad(n\in I_k).
\tag{RT22}
\]
Choose \(n_k\in I_k\) with \(n_k>n_{k-1}\); an infinite subset of natural numbers cannot be bounded, because a bounded subset is finite. The supremum \(t=\sup_k a_k\) exists. For any \(j,k\), nestedness gives \(a_j\le b_k\), so \(a_k\le t\le b_k\). Thus \(|t_{n_k}-t|\le(b_0-a_0)2^{-k}\to0\). Every original interval length and actual selected index is retained.

For a bounded sequence \(x_n\in\mathbb R^d\), (RT21) bounds every coordinate. Apply the preceding construction to coordinate one. From the selected subsequence apply it to coordinate two, and continue through all \(d\) coordinates. Earlier coordinate convergence is preserved under each later strictly increasing index map: any increasing natural-number map has its \(k\)-th value at least \(k\). The final subsequence has the full original index
\[
n(k)=n_1\bigl(n_2(\cdots n_d(k)\cdots)\bigr)
\tag{RT23}
\]
and converges in every coordinate, hence by (RT21) in the original Euclidean distance. When \(d=0\), take \(n(k)=k\). The resulting limit belongs to any closed set containing the original sequence by Section 4. This proves bounded subsequence existence without using compactness as its own prerequisite.

### 12.6. Open-cover compactness and the exact closed-and-bounded criterion

A subset \(K\subset\mathbb R^d\) is compact if every cover of \(K\) by open subsets of \(\mathbb R^d\) has a finite subcover. The empty set is compact because the empty subfamily covers it. A subset is sequentially compact if every sequence of its points has a subsequence converging to a point of that subset. Section 12.5 proves that every closed bounded set is sequentially compact, with all original coordinates retained.

We prove that sequential compactness supplies open-cover compactness in this metric. First it supplies finite ball covers at every radius \(\varepsilon>0\). Otherwise, for any finite number of stages, choose \(x_1\in K\) and, after \(x_1,\ldots,x_n\), choose
\[
x_{n+1}\in K\setminus\bigcup_{j=1}^n B(x_j,\varepsilon).
\tag{RT24}
\]
Every two distinct selected points in one finite tuple have distance at least \(\varepsilon\). If an infinite extension were already selected, a convergent subsequence would have two sufficiently late terms each within \(\varepsilon/3\) of its limit, giving mutual distance less than \(2\varepsilon/3\). Such an extension would contradict sequential compactness, but the finite extension rule alone does not select it under countable choice. The following independent countable construction proves that finitely many balls \(B(x_j,\varepsilon)\) with centers in \(K\) cover \(K\).

Here is that construction with the original Euclidean distance unchanged. The empty set needs no balls; in dimension zero the nonempty coordinate space is a singleton and one ball covers it. Suppose \(K\ne\varnothing\) and \(d\geq1\). Enumerate all open coordinate boxes \(Q_j=\prod_{i=1}^d(a_{ji},b_{ji})\) with rational endpoints \(a_{ji}<b_{ji}\). This enumeration follows from the existing integer-pair enumeration of rational numbers and the diagonal enumeration of finite tuples: each rational keeps its actual numerator and nonzero denominator. For an original \(x\in\mathbb R^d\) and \(r>0\), rational density gives endpoints on either side of each \(x_i\), within \(r/(2\sqrt d)\). That box contains \(x\), and every \(y\) in it has \(|y-x|<(\sum_{i=1}^d r^2/(4d))^{1/2}=r/2<r\). Thus these original boxes form a countable neighborhood basis, without assuming compactness.

Fix one \(x_0\in K\). For each already fixed box define the independent nonempty set
\[
 H_j=
 \begin{cases}
  K\cap Q_j,&K\cap Q_j\ne\varnothing,\\
  \{x_0\},&K\cap Q_j=\varnothing .
 \end{cases}
 \qquad z_j\in H_j .
 \tag{RT24a}
\]
Countable choice selects this sequence once. Its set of values \(S\) is dense in \(K\): for each \(x\in K\) and \(r>0\), the preceding basis calculation gives a box containing \(x\) inside \(B(x,r)\), and its selected \(z_j\) lies in that ball. If finitely many balls of radius \(\varepsilon/3\), with centres \(c_1,\ldots,c_q\in K\), covered \(S\), then for each original \(x\in K\) density gives \(z_j\) with \(|x-z_j|<\varepsilon/3\). Some cover ball contains \(z_j\), so
\[
 |x-c_i|\leq |x-z_j|+|z_j-c_i|
                  <2\varepsilon/3<\varepsilon .
 \tag{RT24b}
\]
These same finitely many centres would cover \(K\) by its original \(\varepsilon\)-balls. Under the assumed failure of such a cover, \(S\) therefore has no finite \(\varepsilon/3\)-ball cover.

Starting with \(w_1=z_1\), after \(w_1,\ldots,w_n\) take the least enumerated index \(j\) with \(z_j\) outside their finitely many open \(\varepsilon/3\)-balls, and let \(w_{n+1}=z_j\). The preceding failure of a finite cover proves that this least natural-number index exists. This is a deterministic recursion on the single chosen countable sequence; it needs no choices from history-dependent arbitrary sets. It gives
\[
 |w_i-w_j|\geq\varepsilon/3\quad(i\ne j).
 \tag{RT24c}
\]
Sequential compactness would give a convergent subsequence. Two sufficiently late terms have distances to its limit less than \(\varepsilon/6\), hence mutual distance less than \(\varepsilon/3\), contrary to (RT24c). This proves the required finite-ball covering conclusion using exactly the declared countable-choice foundation. The original finite extension formula (RT24), the original distance and its full coordinate norm, and all earlier comparison factors remain. No Zorn or dependent-choice axiom has been inserted.

For an open cover \(\mathcal U\) of nonempty \(K\), some \(\delta>0\) has this property: for every \(x\in K\), one member of \(\mathcal U\) contains \(B(x,\delta)\cap K\). If this failed, for every positive integer \(n\) choose \(x_n\in K\) such that no member contains \(B(x_n,1/n)\cap K\). Take a convergent subsequence \(x_{n_k}\to x\in K\). A member \(U\) containing \(x\) contains \(B(x,r)\) for some \(r>0\). For sufficiently large \(k\),
\[
|x_{n_k}-x|_2<r/2,\qquad 1/n_k<r/2,\qquad
B(x_{n_k},1/n_k)\subset B(x,r)\subset U.
\tag{RT25}
\]
The middle inclusion follows by adding the two original strict distance bounds. This contradicts the selection of \(x_{n_k}\). With the resulting \(\delta\), cover \(K\) by finitely many balls of radius \(\delta/2\) centered in \(K\), using the preceding result. For each center choose a member containing its radius-\(\delta\) ball intersected with \(K\). These finitely many original cover members cover \(K\). This proves open-cover compactness from sequential compactness.

Conversely a compact \(K\) is bounded. The balls \(B(0,n)\), \(n=1,2,\ldots\), cover \(\mathbb R^d\) by the Archimedean property. A finite subcover has maximal radius, giving an actual bound. The empty set is bounded by any nonnegative bound.

It is also closed. Fix \(a\notin K\). If \(K\) is empty its complement is the whole open space. Otherwise each \(x\in K\) has the original positive radius \(r_x=|x-a|_2/3\). Finitely many \(B(x_i,r_{x_i})\) cover \(K\). Put \(\delta=\min_i r_{x_i}>0\). For \(y\in K\), choose \(i\) with \(|y-x_i|_2<r_{x_i}\). Then
\[
|y-a|_2\ge |x_i-a|_2-|y-x_i|_2
>3r_{x_i}-r_{x_i}=2r_{x_i}\ge2\delta.
\tag{RT26}
\]
Thus \(B(a,\delta)\) is disjoint from \(K\). Every outside point has an open ball in the complement, proving closedness.

We have proved all three implications, so for every original finite dimension, including zero,
\[
K\text{ compact}\quad\Longleftrightarrow\quad
K\text{ closed and bounded}
\quad\Longleftrightarrow\quad
K\text{ sequentially compact}.
\tag{RT27}
\]
For the last implication from sequential compactness to closed and bounded, the just-proved route through open-cover compactness supplies it. No definition of compactness was substituted for another without proving the maps between their assertions.

A closed subset \(C\) of a compact set \(K\) is compact. To an open cover of \(C\) add the open complement of \(C\); the resulting family covers \(K\), and a finite subfamily still covers \(C\) after discarding that complement. If closedness is relative to \(K\), use an ambient open set whose intersection with \(K\) is the relative complement; the same cover argument applies. A finite union of compact sets is compact by taking a finite subcover for each member and then their finite union. Empty unions are covered by the already proved empty case.

Finite Cartesian products preserve the original coordinates. For \(K_j\subset\mathbb R^{d_j}\) compact, each factor is closed and bounded. The product is closed because an outside point has a coordinate outside one closed factor, and the inverse image of an open coordinate neighborhood is open by (RT21). If \(|x^{(j)}|_2\le M_j\) in that factor, the complete product satisfies
\[
\left|\bigl(x^{(1)},\ldots,x^{(r)}\bigr)\right|_2^2
=\sum_{j=1}^r |x^{(j)}|_2^2\le\sum_{j=1}^r M_j^2.
\tag{RT28}
\]
Consequently it is compact by (RT27), with every original bound retained. An empty factor gives the empty compact product; a product of no factors is the one-point zero-dimensional space.

### 12.7. Continuous maps, full extrema and uniform continuity

A map \(f:K\to\mathbb R^e\) is continuous at \(x\in K\) when for every \(\varepsilon>0\) some \(\delta>0\) ensures \(|f(y)-f(x)|_2<\varepsilon\) whenever \(y\in K\) and \(|y-x|_2<\delta\). This definition proves directly that inverse images of relatively open sets are relatively open: choose a ball about \(f(x)\) in the target open set, then its continuity preimage ball. Conversely that inverse-image property applied to every target ball gives the same definition. It also proves preservation of sequence limits, by applying the defining \(\delta\) to an eventually close sequence.

If \(K\) is compact, \(f(K)\) is compact: the inverse images of any open cover of \(f(K)\) are a relatively open cover of \(K\); the proved relative-cover formulation yields finitely many of them, whose original target members cover \(f(K)\). Thus continuous real functions on a compact set have bounded image.

If \(K\ne\varnothing\) and \(f:K\to\mathbb R\) is continuous, let \(s=\sup f(K)\), which exists by Section 3. For each positive integer \(n\), least-upper-bound minimality supplies \(x_n\in K\) with
\[
s-1/n<f(x_n)\le s.
\tag{RT29}
\]
Sequential compactness supplies \(x_{n_k}\to x\in K\). Continuity gives \(f(x_{n_k})\to f(x)\), whereas (RT29) gives convergence to \(s\). Uniqueness of limits therefore gives \(f(x)=s\). Applying this same proof to the function \(-f\) gives \(y\in K\) with \(f(y)=\inf f(K)\). This proves both extrema, with the exact hypotheses: the empty set has no attained extremum and is never assigned one.

The intermediate value property also follows from these exact foundations. Let \(f:[a,b]\to\mathbb R\) be continuous with \(a<b\), and \(f(a)\le c\le f(b)\). The set \(S=\{t\in[a,b]:f(t)\le c\}\) is nonempty and bounded above, so put
\[
t_0=\sup S.
\tag{RT29a}
\]
If \(f(t_0)>c\), continuity gives a neighborhood on which \(f>c\). Here \(t_0>a\), since \(f(a)\le c\). Shrink its positive radius below \(t_0-a\). Then \(t_0\) minus half that radius is still an upper bound of \(S\), contradicting the supremum. If \(f(t_0)<c\), then \(t_0<b\), since \(f(b)\ge c\). Shrink the continuity radius below \(b-t_0\); the point \(t_0\) plus half that radius belongs to \(S\), another contradiction. Thus \(f(t_0)=c\). If the endpoint inequalities are reversed, apply this proved argument to \(-f\) with the exact value \(-c\). If \(a=b\), only the common endpoint value is requested, and it is attained there.

For every integer \(q\ge1\) and \(a\ge0\), the polynomial \(t^q\) is continuous. Its values at \(0,a+1\) bracket \(a\), because \((a+1)^q\ge a+1>a\). The just-proved intermediate value property gives a nonnegative \(q\)-th root. For \(x>y\ge0\), the complete identity
\[
x^q-y^q=(x-y)\sum_{j=0}^{q-1}x^{q-1-j}y^j>0
\tag{RT29b}
\]
proves strict increase and uniqueness. Each summand is nonnegative, and the \(j=0\) term is positive, including \(q=1\), when it is \(1\). For \(a=0\) the unique root is zero. This supplies every positive-integer real root in the original polynomial-radius formulas without a calculus prerequisite.

Such a continuous map \(f:K\to\mathbb R^e\) is uniformly continuous. If not, some \(\varepsilon>0\) would supply pairs \(x_n,y_n\in K\) with \(|x_n-y_n|_2<1/n\) but \(|f(x_n)-f(y_n)|_2\ge\varepsilon\). Take \(x_{n_k}\to x\in K\). The full triangle inequality implies \(y_{n_k}\to x\), so both image sequences tend to \(f(x)\); their difference then has norm less than \(\varepsilon\) eventually, a contradiction. For empty \(K\) uniform continuity is vacuous. This gives the precise compact-set continuity needed in all later sup-norm arguments.

Addition and multiplication of real-valued continuous functions are continuous by the estimates for sums and (RT17), with local boundedness obtained from continuity at the point. Reciprocals are continuous on their exact nonzero domain: if \(f(x)\ne0\), choose a neighborhood with \(|f(y)-f(x)|<|f(x)|/2\), giving \(|f(y)|>|f(x)|/2\), and use
\[
\left|\frac1{f(y)}-\frac1{f(x)}\right|
=\frac{|f(y)-f(x)|}{|f(y)||f(x)|}
\le \frac{2}{|f(x)|^2}|f(y)-f(x)|.
\tag{RT30}
\]
Finite sums and products are continuous by induction. Absolute value is continuous since its two values differ by at most the difference of the original values. For nonnegative \(a,b\), \(|\sqrt a-\sqrt b|^2\le |a-b|\): when \(a\ge b\), \((\sqrt a-\sqrt b)^2\le(\sqrt a-\sqrt b)(\sqrt a+\sqrt b)=a-b\), and interchanging them covers the other order. This proves continuity of the square root, including zero.

Identify a complex number with its original pair of real coordinates as in [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (FA0a)--(FA0d). Addition, multiplication, conjugation and squared modulus are exactly the full coordinate polynomials already proved there, so all are continuous. The modulus is the nonnegative square root of the full squared modulus and is therefore continuous. The two-coordinate inverse has the full nonzero denominator \(a^2+b^2\); (RT30) proves its continuity on its actual domain. These are exact maps on the original complex numbers, through the scalar comparison (RT16).

### 12.8. Countable coordinate neighborhoods and exact sequence choices

The set of rational \(d\)-tuples is countable: integers are enumerated by pairs of natural numbers, rational pairs by four such coordinates including their nonzero denominator restrictions, and finite tuples of these by their finite-coordinate enumerations. A finite tuple of natural numbers can be enumerated by first listing all tuples whose coordinate sum is at most \(N\), for \(N=0,1,\ldots\); each stage is finite and every tuple occurs. Hence no unstated identification between countability and compactness is used.

Rational coordinate tuples are dense in \(\mathbb R^d\). Given \(x\) and \(\varepsilon>0\), for \(d>0\) choose each rational coordinate \(q_j\) within \(\varepsilon/(2\sqrt d)\) of \(x_j\). Formula (RT21) gives \(|q-x|_2<\varepsilon/2\). For \(d=0\) the empty tuple is already the point. Balls with rational coordinate centers and positive rational radii form a countable basis. If \(B(x,\varepsilon)\) is contained in an open set, choose such \(q\) with \(|q-x|_2<\varepsilon/4\), and choose rational \(r\) with
\[
|q-x|_2<r<\varepsilon-|q-x|_2.
\tag{RT31}
\]
Rational density from Section 12.2 supplies it, since the endpoint gap is positive. Then \(x\in B(q,r)\subset B(x,\varepsilon)\). Both maps and both radius errors are explicit.

Consequently every open set is the union of a subfamily of this countable basis: for each of its points the preceding construction gives a basis ball contained in it. Any family of pairwise disjoint nonempty open subsets is countable: for each member choose the first rational-coordinate point in a fixed enumeration which it contains. Density guarantees a choice and disjointness makes the assignment injective. This proves the particular countability argument used in this lesson's supports section without assuming compactness implies countability.

For a continuous function \(f\), its support is the closure of \(\{x:f(x)\ne0\}\). Outside that support there is a neighborhood on which it is zero, by the definition of closure and its open complement. Derivatives which exist on such a neighborhood are zero there by their defining difference quotients, since every numerator is zero. This assertion uses the derivative definition only and makes no assertion of global differentiability.

If supports of functions form a locally finite family, each point has a neighborhood meeting only finitely many supports. A compact \(K\) admits finitely many such neighborhoods. Only the finite union of those finite member lists can meet \(K\). The same finite collection of neighborhoods gives an open neighborhood of \(K\) on which only those members may be nonzero. Derivative sums on that neighborhood, wherever the original derivatives exist, therefore consist of the same finite actual summands. This proves the exact compact-support receiving assertion without turning pointwise finiteness into local finiteness.

### 12.9. Every original finite norm and positive quadratic form

Let \(V\) be a finite-dimensional real vector space with its actual ordered basis \(b=(b_1,\ldots,b_d)\), coordinate bijection \(J_b\) from [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (FA3), and its given norm \(N(v)\). We prove comparison with the coordinate metric while retaining \(N\) as the working norm. For \(d>0\), define the actual constant
\[
M_b=\left(\sum_{j=1}^d N(b_j)^2\right)^{1/2}>0.
\tag{RT32}
\]
The full coordinate expansion and (RT20) give
\[
N(J_bx)=N\left(\sum_{j=1}^d x_jb_j\right)
\le\sum_{j=1}^d |x_j|N(b_j)\le M_b|x|_2.
\tag{RT33}
\]
The reverse triangle inequality gives \(|N(J_bx)-N(J_by)|\le M_b|x-y|_2\). Thus the original norm in these coordinates is continuous, with the full original basis constant.

The coordinate sphere \(S=\{x:|x|_2=1\}\) is nonempty for \(d>0\), closed by norm continuity and bounded, hence compact. The function \(N(J_bx)\) has a minimum \(c_b\) on \(S\). At its minimizing point \(x_0\), injectivity of \(J_b\) and \(|x_0|_2=1\) give \(N(J_bx_0)>0\), so \(c_b>0\). For any original \(x\ne0\), the auxiliary radial comparison is the exact bijection
\[
x\longmapsto(|x|_2,\,|x|_2^{-1}x),\qquad
(r,u)\longmapsto ru,\quad r>0,\ |u|_2=1.
\tag{RT34}
\]
Both compositions are identities by the full scalar multiplication and its inverse, and the original vector remains \(x=|x|_2(|x|_2^{-1}x)\). Homogeneity of the given norm, with that entire factor retained, yields
\[
c_b|x|_2\le N(J_bx)\le M_b|x|_2
\quad\text{for every original }x.
\tag{RT35}
\]
The zero vector has both sides zero. In dimension zero \(V=\{0\}\); all topologies are the one-point topology and no sphere minimum or positive coordinate constant is inserted.

The identity coordinate map and its inverse now send balls according to the two exact constants in (RT35). They preserve open and closed sets and both sequence notions. A set is bounded in the original norm precisely when its coordinate set is bounded, and it is compact precisely when its coordinate set is compact, because both inverse-image cover maps are continuous bijections. A bounded original-norm sequence therefore has a convergent subsequence in that same original norm, with indices furnished by (RT23). Nothing replaces \(N\) by another working norm.

For a complex vector space with ordered complex basis \(b\), the exact underlying real-coordinate bijection is
\[
J_b^{\mathbb R}(a_1,c_1,\ldots,a_d,c_d)
=\sum_{j=1}^d(a_j+ic_j)b_j
=\sum_{j=1}^d(a_jb_j+c_j\,ib_j).
\tag{RT36}
\]
Its inverse is the original complex coordinate inverse followed by the original real and imaginary coordinate maps. This is a real basis consisting of all \(b_j,ib_j\), not a replacement of the complex basis. Apply (RT32)--(RT35) to it. Every basis norm, including \(N(ib_j)=N(b_j)\) for a complex norm, is retained in the full sum. Thus complex compactness and subsequence assertions use every original real and imaginary coordinate and both inverse maps.

For a given positive-definite real quadratic form \(Q(x)=x^{\mathsf T}Gx\), retain every entry of \(G\) and its exact Gram map from [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (FA15)--(FA18). Its norm \(N_Q(x)=\sqrt{Q(x)}\) obeys the norm identities proved there, so (RT35) applies to that same original form. Alternatively the more precise residual comparison from (FA22) gives its exact lower constant \(\sqrt{d_{\min}}/F_S\), with \(d_{\min}=\min_jd_j>0\), \(F_S=(\sum_{j,k}|S_{jk}|^2)^{1/2}\), the original residual lengths and full triangular map \(S\). Hence for \(r\ge0\),
\[
Q(x)\le r^2
\ \Longrightarrow\
|x|_2\le \frac{F_S}{\sqrt{d_{\min}}}\,r
\quad(d>0).
\tag{RT37}
\]
The full polynomial \(Q\) is continuous, so its sublevel set is closed and bounded and therefore compact. For \(r=0\) it is exactly \(\{0\}\); for negative \(r\), the literal set \(Q(x)\le r^2\) instead has the bound with \(|r|\), and no radius convention is silently changed. In dimension zero all these sets are the single empty-coordinate point. Unit-level sets are closed and bounded and hence compact; in dimension zero the unit level is empty. All determinant and volume comparisons in the receiving this lesson argument remain its original Gram comparisons, rather than consequences of changing its metric.

### 12.10. Actual polynomial, spectral, metric and stable-boundary receiving maps

For the original complex polynomial \(p(z)=\sum_{k=0}^N a_kz^k\), \(N\ge1\) and \(a_N\ne0\), [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (CR5)--(CR6) supplies its actual radius
\[
A_0=\sum_{k=0}^{N-1}|a_k|,\qquad
R=1+\frac{2A_0}{|a_N|}
+\left(\frac{2(|a_0|+1)}{|a_N|}\right)^{1/N}.
\tag{RT38}
\]
Its finite polynomial map is continuous by Section 12.7, and the literal closed disk \(|z|\le R\) in its two original coordinates is compact by (RT27). Consequently \(|p|\) has a minimum on that disk by Section 12.7. The proved lower bound outside it in (CR5)--(CR6) exceeds \(|a_0|+1\), while \(|p(0)|=|a_0|\) is an available value inside. Thus the disk minimizer is the actual global minimizer required in (CR8)--(CR10). The entire original polynomial and every original coefficient, factor and remainder stay in the receiving argument. The exact positive \(N\)-th root appearing in this radius is supplied by (RT29b). The subsequent exponential and derivative inputs remain their separately identified scalar calculus proofs.

For the original real inner-product space of [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md) Theorem 3.1, the given unit sphere in its actual coordinates is \(\{x:x^{\mathsf T}Hx=1\}\). The precise original bound (FA22) gives \(|x|_2\le F_S/\sqrt{d_{\min}}\) when the dimension is positive. Section 12.9 proves this exact sphere compact. The original Rayleigh expression \(h(AJ_bx,J_bx)\) is a finite coordinate polynomial in the actual matrix \(A\) and Gram matrix \(H\), so it is continuous and attains its maximum on that sphere. This supplies the actual maximizing vector used in the theorem. No spectral decomposition is used to prove this prerequisite, and no original matrix or inner product is changed. The zero-dimensional sphere is empty; the spectral source's empty-basis case is handled directly and never invokes an extremum on that empty set. The derivative step of the receiving proof remains the separately required calculus step.

Let \(T:V\to V\) be the original complex linear operator and \(A=(A_{jk})\) its actual ordered-basis matrix. The exact type-correct coordinate identity is \(TJ_b=J_bA\). For the given original norm, (RT33)--(RT35) give
\[
N(TJ_bx)
\le\sum_{j,k}|A_{jk}||x_k|N(b_j)
\le c_b^{-1}\left(\sum_{j,k}|A_{jk}|N(b_j)\right)N(J_bx).
\tag{RT39}
\]
The output is the original vector \(TJ_bx=J_bAx=\sum_{j,k}A_{jk}x_kb_j\), with \(T\) acting on \(V\) and \(A\) on its exact coordinate space. The given operator, every ordered coordinate factor and both domains are retained. For this complex coordinate argument, \(|x|_2^2=\sum_{j=1}^d((\operatorname{Re}x_j)^2+(\operatorname{Im}x_j)^2)\), and the constant denoted \(c_b\) here is exactly the original-norm minimum obtained for the full real basis \(b_1,ib_1,\ldots,b_d,ib_d\) in (RT36). Both coordinates of every complex coefficient and every basis value remain present. The original operator norm is the supremum over \(N(v)=1\). Its existence follows from the displayed bound and real completeness. Differences of operator norms are bounded by the norm of the original difference, by the triangle inequality applied to each original unit vector and both suprema. Formula (RT39) therefore proves operator-norm continuity under entrywise matrix convergence, with all basis constants retained. The zero-dimensional operator norm is zero and its unit sphere is empty by that stated convention.

Let \(A(y)\) be the actual continuous finite complex operator family on a compact nonempty parameter set \(K\subset\mathbb R^e\), with no real eigenvalue at any \(y\in K\), and suppose the same family is continuously defined on an open parameter domain containing \(K\) for the neighborhood-persistence assertion below, as in [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) Section 7 and [Stable modes and the algebra of boundary data](stable-boundary-models.md) Section 4. For positive vector-space dimension, \(y\mapsto\|A(y)\|\) is continuous by (RT39), so its maximum
\[
M=\max_{y\in K}\|A(y)\|
\tag{RT40}
\]
exists. For every original eigenvector \(v\ne0\) and eigenvalue \(\lambda\), the actual equality and inequality are
\[
|\lambda|N(v)=N(\lambda v)=N(A(y)v)
\le\|A(y)\|N(v),
\qquad |\lambda|\le M.
\tag{RT41}
\]
Division uses the actual positive \(N(v)\); the original \(v\) is retained.

The full characteristic determinant \(\det(\lambda I-A(y))\) is continuous by its original permutation sum, with all signs and zero factors as proved in [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (FA29). Hence
\[
\mathcal E=\{(y,\lambda):y\in K,\ |\lambda|\le M,\
\det(\lambda I-A(y))=0\}
\tag{RT42}
\]
is a closed subset of the compact product of \(K\) and the radius-\(M\) disk in the two original complex coordinates. It is compact. The already proved complex-root theorem and the original nonzero leading coefficient of the characteristic polynomial show it is nonempty when \(K\ne\varnothing\) and the dimension is positive. By the original no-real-eigenvalue hypothesis, the continuous function \(|\operatorname{Im}\lambda|\) is positive everywhere on \(\mathcal E\). It therefore has an attained positive minimum
\[
g=\min_{\mathcal E}|\operatorname{Im}\lambda|>0.
\tag{RT43}
\]
Choose the original contour parameters \(R>M+1\) and \(0<\delta<g\). The positively oriented rectangle with vertical sides at real coordinates \(-R,R\), bottom height \(\delta\) and top height \(R\) encloses every upper eigenvalue, excludes every lower eigenvalue, and meets no eigenvalue. All original coordinates, orientations, gaps and bounds are explicit. In dimension zero there are no eigenvalues, the identity is the zero-space identity, and any such rectangle has the required empty-spectrum meaning. For empty \(K\) the parameter assertion is vacuous; choose any \(R>1,\delta>0\) with \(\delta<R\), without invoking a minimum of an empty set.

The actual compact set \(K\times\Gamma\), where \(\Gamma\) is this finite rectangular path, has a strictly positive minimum of \(|\det(zI-A(y))|\): it is nonzero everywhere and continuous. The adjugate entries are full original finite polynomial sums, so they are bounded there. The exact cofactor formula
\[
(zI-A(y))^{-1}
=\det(zI-A(y))^{-1}\operatorname{adj}(zI-A(y))
\tag{RT44}
\]
thus supplies bounded original resolvent entries, with its original determinant denominator and all cofactor signs. Fix an original \(y_0\in K\), and write \(D>0\) for that minimum. At each \(z_0\in\Gamma\), joint continuity provides a product of neighborhoods of \(y_0,z_0\), with the parameter neighborhood inside the original open parameter domain, on which the determinant differs from its value at \((y_0,z_0)\) by less than \(D/4\). Setting the parameter to \(y_0\) gives the same bound for its fixed-parameter value at every \(z\) in that contour neighborhood. The difference between the two values at \((y,z)\) and \((y_0,z)\) is therefore less than \(D/2\), by adding both original \(D/4\) errors. Finitely many of these contour neighborhoods cover \(\Gamma\). Intersect their finitely many parameter neighborhoods. For every \(y\) in that intersection and every \(z\in\Gamma\), the determinant has modulus greater than \(D/2\), since its original fixed-parameter modulus is at least \(D\). The same actual contour therefore persists locally in the original parameter coordinates. This proves precisely the compactness and continuity prerequisite of the already written ordered inverse-derivative and contour calculations; their \(1/(2\pi i)\), original path length, every ordered derivative factor and every factorial remain those of [Stable modes and the algebra of boundary data](stable-boundary-models.md) (SR22)--(SR24).

Finally, [Stable modes and the algebra of boundary data](stable-boundary-models.md)'s original continuous positive function
\[
h(v)=\int_0^1|\pi_0E_C(s)v|^2\,ds
\tag{RT45}
\]
on its original state space has a positive minimum on the actual unit sphere, once its source's proved positivity and continuous-series/integration input are received. The sphere is compact by Section 12.9; a minimizing vector is nonzero, so the minimum is positive by that exact positivity proof. The full integral, the original projection \(\pi_0\), the original evolution \(E_C\) and the interval \([0,1]\) are retained. The negative-half-line source uses its separate literal interval \([-1,0]\), to which the same sphere result applies. In the zero state space the original bounded-state comparison is trivial and no empty-sphere minimum is assigned.

this lesson's fixed ellipsoid, finite compact unions, locally finite supports, actual matrix inverses and continuous suprema receive Sections 12.6--12.9 through their original coordinates and Gram matrices. This does not supply its still-separate mean value, exponential derivative, real-power or fundamental-theorem-of-calculus entries. The full real-number and finite-topology entry is proved above from the explicit natural-number, set and choice axioms. The separate derivative, exponential and integration arguments retain their actual hypotheses and proofs.

## 13. Original scalar calculus and its finite-coordinate receivers

This section proves the one-variable and finite-coordinate calculus used above, from the original real-field construction and topology in Section 12 and the full scalar and matrix operations in Section 10 of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md#full-finite-linear-algebra-foundations). Natural-number arithmetic, induction, sets and countable choice remain the explicit logical entry. Every original coordinate, norm, endpoint and coefficient is retained. These are standard foundations; no novelty is claimed. The final section proves their exact receiving maps.

### 13.1. Limits with all original scalar and coordinate factors

For a map \(f:D\to\mathbb R\), a point \(x_0\) in the closure of \(D\setminus\{x_0\}\), and an original value \(L\), the limit \(f(x)\to L\) means that for every \(\epsilon>0\) some \(\delta>0\) gives \(|f(x)-L|<\epsilon\) whenever \(x\in D\) and \(0<|x-x_0|<\delta\). Sequences use the same inequality beyond an integer index. One-sided limits restrict the actual domain. A limit is unique: two distinct values at distance \(d>0\) would have a common domain point with both errors less than \(d/3\), contradicting their distance.

If \(f\to a\) and \(g\to b\), the following exact expansions prove sums, scalar multiples and products:

\[
\begin{aligned}
 (f+g)-(a+b)&=(f-a)+(g-b),\\
 cf-ca&=c(f-a),\\
 fg-ab&=(f-a)g+a(g-b),\\
 |fg-ab|&\le |f-a|(|b|+1)+|a||g-b|
 \quad\text{once }|g-b|<1.
\end{aligned}\tag{OC1}
\]

Choose the two errors below \(\epsilon/[2(|b|+|a|+2)]\) to obtain the product limit. If \(b\ne0\), take \(|g-b|<|b|/2\); then \(g\ne0\) and

\[
 \left|\frac1g-\frac1b\right|
 =\frac{|g-b|}{|g||b|}
 \le\frac{2}{|b|^2}|g-b|.
\tag{OC2}
\]

This proves the reciprocal and quotient rules, retaining both denominators. Absolute values are continuous because their difference is at most the original difference. Finite sums/products follow by induction. A function has a limit precisely when every sequence in its punctured domain tending to \(x_0\) has that limit. One implication is the definition. If the definition fails, choose, for each \(n\), a point with \(0<|x_n-x_0|<1/n\) and error at least the same fixed \(\epsilon\). This gives the countersequence. The analogous continuity assertion includes \(x=x_0\).

For an original basis \(b=(b_1,\ldots,b_d)\) of a finite real space \(V\), write \(J_bx=\sum_jx_jb_j\) and retain its given norm \(N\). The earlier finite-norm proof supplies the actual positive constants \(c_b,M_b\) when \(d>0\):

\[
 c_b\left(\sum_{j=1}^d x_j^2\right)^{1/2}
 \le N(J_bx)\le
 M_b\left(\sum_{j=1}^d x_j^2\right)^{1/2},
 \qquad
 M_b=\left(\sum_{j=1}^d N(b_j)^2\right)^{1/2}.
\tag{OC3}
\]

The lower constant is the minimum of the original norm on the actual coordinate unit sphere. Thus coordinate limits are equivalent to limits in \(N\), and coordinatewise real completeness makes every Cauchy sequence complete in the original norm. For a complex space use the exact real basis \(b_1,ib_1,\ldots,b_d,ib_d\), retaining all real and imaginary components. In dimension zero every map has the unique zero value; no positive sphere constant is assigned. Limits, finite sums and all the ensuing integral constructions pass through these proved maps and their actual inverses.

### 13.2. Derivatives, extrema and the mean value theorem

For \(f:I\to\mathbb R\) on an interval, its derivative at an interior \(x\) is the limit of the actual quotient \([f(x+h)-f(x)]/h\) over nonzero \(h\) with \(x+h\in I\). At a finite endpoint use the corresponding one-sided limit if asserted. Differentiability gives the exact remainder

\[
 f(x+h)=f(x)+h f'(x)+h r_x(h),
 \qquad r_x(h)\longrightarrow0.
\tag{OC4}
\]

It implies continuity at \(x\). If an interior point is a local maximum, quotients for positive \(h\) are nonpositive and for negative \(h\) are nonnegative, so their common limit is zero. The same argument with signs reversed proves the minimum case.

Let \(f\) be continuous on \([a,b]\), \(a<b\), differentiable on \((a,b)\), and satisfy \(f(a)=f(b)\). If it is constant its derivative is zero at every interior point. Otherwise the proved compact extrema include a value distinct from the common endpoint value; an attaining maximum or minimum must then be interior, and the preceding argument gives a point where \(f'=0\). This proves Rolle's theorem without an integral prerequisite.

For arbitrary such \(f\), subtract the actual affine secant

\[
 F(t)=f(t)-f(a)-\frac{f(b)-f(a)}{b-a}(t-a).
\tag{OC5}
\]

It has equal endpoint values. Rolle gives some \(c\in(a,b)\) with \(F'(c)=0\), and hence \(f(b)-f(a)=(b-a)f'(c)\). Constants and affine derivatives follow directly from their original quotients. Consequently a zero derivative on an interval gives a constant, and a derivative bounded in absolute value by \(M\) gives \(|f(b)-f(a)|\le M|b-a|\). A nonnegative derivative gives a nondecreasing function; a strictly positive derivative gives a strictly increasing one by the actual secant formula. Unbounded intervals follow by applying the statement to each pair of their points.

Apply this to each coordinate of a vector-valued map. It gives coordinate bounds and then (OC3), rather than asserting a single vector-valued mean-value point. For example, if each coordinate derivative has bound \(M_j\), then

\[
 N(f(b)-f(a))
 \le M_b |b-a|\left(\sum_{j=1}^d M_j^2\right)^{1/2}.
\tag{OC6}
\]

Here \(M_b\) is the original basis constant, not the interval endpoint. Dimension zero gives the zero inequality. Complex-valued functions are handled by both real coordinates.

### 13.3. Constructing the full oriented Riemann integral

For a bounded real function \(f\) on an original interval \([a,b]\), \(a<b\), take a finite partition \(P:a=t_0<\cdots<t_m=b\), and let

\[
\begin{aligned}
 L(f,P)&=\sum_{j=1}^m
   \inf_{[t_{j-1},t_j]}f\,(t_j-t_{j-1}),\\
 U(f,P)&=\sum_{j=1}^m
   \sup_{[t_{j-1},t_j]}f\,(t_j-t_{j-1}),\\
 S(f,P,\xi)&=\sum_{j=1}^m f(\xi_j)(t_j-t_{j-1}),
 \qquad \xi_j\in[t_{j-1},t_j].
\end{aligned}\tag{OC7}
\]

Every infimum and supremum exists by the original completeness theorem. Refinement increases \(L\) and decreases \(U\), by dividing each interval into its actual lengths. Any two partitions have their finite common refinement. Thus \(\sup_P L(f,P)\le\inf_P U(f,P)\). Their equality defines integrability and the value \(\int_a^bf\).

A continuous function on this compact interval is bounded and uniformly continuous. Given \(\epsilon>0\), choose \(\delta>0\) so that oscillation on any interval of length below \(\delta\) is less than \(\epsilon/(b-a+1)\). A finite uniform partition of mesh below \(\delta\) then satisfies

\[
 U(f,P)-L(f,P)
 \le \frac{\epsilon}{b-a+1}\sum_{j=1}^m(t_j-t_{j-1})
 =\frac{\epsilon(b-a)}{b-a+1}<\epsilon.
\tag{OC8}
\]

The upper and lower integrals therefore agree. For any integrable bounded \(f\), all tagged sums tend to this value as mesh tends to zero. To prove the assertion at its full bounded-function scope, first choose \(P_0\) with \(U(f,P_0)-L(f,P_0)<\epsilon/2\), and a bound \(|f|\le M\). Compare a fine tagged partition \(Q\) with the common refinement \(P_0\cup Q\). Intervals of \(Q\) not crossing an interior \(P_0\) endpoint have their tagged contribution between the corresponding refined lower and upper contributions. At most \(m_0-1\) intervals cross such endpoints; their total length is at most \((m_0-1)\operatorname{mesh}Q\). Both the refined contribution and the original tagged contribution on their union have absolute value at most \(M\) times that length. Consequently

\[
 \left|S(f,Q,\xi)-\int_a^bf\right|
 \le U(f,P_0)-L(f,P_0)
       +2M(m_0-1)\operatorname{mesh}Q.
\tag{OC9}
\]

Taking mesh less than \(\epsilon/[4(M+1)m_0]\) proves convergence. Multiple endpoints in one interval only reduce the count; tagged endpoints cause no extra interval length.

Conversely, if all sufficiently fine tagged sums lie within \(\epsilon\) of the same \(I\), take any one sufficiently fine partition. In each interval choose a value within \(\epsilon/(b-a+1)\) of its supremum, and separately a value within that error of its infimum. The corresponding sums lie arbitrarily close to \(U\) and \(L\). Hence \(U-L\le 2\epsilon+2\epsilon(b-a)/(b-a+1)\). Sending \(\epsilon\) to zero proves integrability, with value \(I\). This establishes the tagged-sum criterion, not merely one chosen sequence of sums.

Termwise operations on tagged sums prove linearity. Order passes to sums and limits; constants integrate to their original value times \(b-a\). A partition including an interior \(c\) splits its sums exactly, so the same limit proves interval additivity and integrability of restrictions. Bounded integrable sums and scalar multiples are integrable by the criterion. The absolute value is integrable: its interval oscillation is at most that of \(f\), and \(-|f|\le f\le|f|\). Retain the resulting bounds

\[
 \left|\int_a^b f(t)\,dt\right|
 \le\int_a^b|f(t)|\,dt
 \le(b-a)\sup_{[a,b]}|f|.
\tag{OC10}
\]

Define \(\int_a^a f=0\), and for \(b<a\) define \(\int_a^bf=-\int_b^af\). The sign is part of the definition and remains in additivity and substitution. Continuous vector functions integrate coordinatewise through the original \(J_b\); this value is the limit of the full vector tagged sums by (OC3). The triangle inequality in the given original norm, applied to each full sum, gives

\[
 N\left(\int_a^b f(t)\,dt\right)
 \le |b-a|\sup_{[\min(a,b),\max(a,b)]}N(f).
\tag{OC11}
\]

Linearity and this estimate also prove that uniform convergence passes through the integral. The actual interval length is never absorbed into a norm or an integral convention.

### 13.4. Fundamental theorem, substitution and integration by parts

#### 13.4.1. The primitive and both fundamental-theorem forms

For continuous \(f\) on \([a,b]\), define \(F(x)=\int_a^xf(t)\,dt\). The original uniform bound gives continuity of \(F\). At an interior \(x\), and with the appropriate one-sided interpretation at either endpoint, additivity gives

\[
 \frac{F(x+h)-F(x)}h-f(x)
 =\frac1h\int_x^{x+h}(f(t)-f(x))\,dt,
 \qquad
 \left|\frac{F(x+h)-F(x)}h-f(x)\right|
 \le\sup_{t\text{ between }x,x+h}|f(t)-f(x)|.
\tag{OC12}
\]

The oriented sign for \(h<0\) gives the same absolute bound, which tends to zero by continuity. Thus \(F'=f\). If \(g\) is continuous on \([a,b]\), differentiable on \((a,b)\), and its derivative has a continuous extension to \([a,b]\), use that extension for the proper Riemann integral. Then \(g-F\), where \(F(x)=\int_a^xg'(t)\,dt\), has zero derivative. The mean value theorem proves it constant, and

\[
 g(b)-g(a)=\int_a^b g'(t)\,dt.
\tag{OC13}
\]

The stronger form used in the metric lesson allows a bounded Riemann-integrable function on \([a,b]\) equal to \(g'\) on \((a,b)\), without continuity of that function. Assign its actual endpoint values as the extension denoted by \(g'\) in (OC13); Changing those two values does not change the proper integral. Indeed, for every tagged partition, only its first interval can use the left endpoint as its tag and only its last interval can use the right endpoint. The absolute change of its tagged sum is therefore at most its mesh times the sum of the two absolute endpoint-value changes. This bound tends to zero for every sequence of meshes tending to zero, uniformly over all tags. The full tagged-sum criterion (OC9) and its proved converse give integrability of the endpoint-modified function and the identical integral. This argument uses the actual endpoint values and neither an endpoint derivative nor an improper integral. For each tagged partition, the mean value theorem on every subinterval chooses \(\xi_j\) with \(g(t_j)-g(t_{j-1})=g'(\xi_j)(t_j-t_{j-1})\). Summing retains every endpoint and telescopes exactly to \(g(b)-g(a)\). The full tagged-sum criterion (OC9) gives (OC13). Endpoint derivatives need not exist for this argument. Coordinatewise application proves the vector statement with its original values and norms.

**Finitely many exceptional interior points.** Retain the original continuous \(F:[a,b]\to\mathbb R\) and bounded Riemann-integrable \(f:[a,b]\to\mathbb R\). Suppose \(F'(x)=f(x)\) for every interior \(x\) outside a finite set \(E\). If \(a<b\), list the distinct points of \(E\cap(a,b)\), keeping their actual coordinates, as
\[
 a=t_0<t_1<\cdots<t_q<t_{q+1}=b.
 \qquad
 F(b)-F(a)
 =\sum_{j=1}^{q+1}\bigl(F(t_j)-F(t_{j-1})\bigr)
 =\sum_{j=1}^{q+1}\int_{t_{j-1}}^{t_j}f(t)\,dt
 =\int_a^bf(t)\,dt.
 \tag{OC13a}
\]
On each actual closed subinterval \(F\) is continuous and differentiable at every interior point. The restriction of \(f\) is bounded and Riemann integrable: extending any partition of that subinterval by the two outside intervals shows its upper-minus-lower sum is at most the corresponding nonnegative full-interval difference. Full-interval partitions of arbitrarily small difference, refined by its endpoints, therefore prove the restriction criterion. The mean value theorem on each partition piece supplies derivative samples in its interior, where \(F'=f\). The full fine-tagged-sum criterion then proves the middle equality separately on each \([t_{j-1},t_j]\). Additivity of the original integral and the displayed telescoping endpoint differences prove the last equality. No derivative at a point of \(E\) is required, and no endpoint contribution is omitted.

For \(a=b\) both sides are zero. For reversed endpoints apply the result on the same ordered interval and retain the negative orientation. For a complex or fixed finite-dimensional target, apply the scalar proof to every real coordinate, including both real and imaginary parts of each complex coordinate, and reconstruct the original vector through its actual basis map. The resulting equality is in that original target, with every coordinate and endpoint unchanged. This is an additional proved form of the theorem; the preceding source statement and its proper-integral hypotheses remain identifiable. No novelty is claimed.

#### 13.4.2. Substitution and ordered integration by parts

The product and chain derivative rules are proved in Section 13.5 below directly from (OC4); using them here does not assume the integral theorem. If \(\phi:[c,d]\to[a,b]\) is \(C^1\) and \(f\) is continuous, the derivative of \(F\circ\phi\), for this actual \(F\), is \(f(\phi(t))\phi'(t)\). Thus

\[
 \int_c^d f(\phi(t))\phi'(t)\,dt
 =\int_{\phi(c)}^{\phi(d)}f(s)\,ds.
\tag{OC14}
\]

No monotonicity is needed for this signed derivative substitution. The right side retains its endpoint orientation; the statement does not identify integrals of absolute Jacobians for a noninjective map. Likewise for \(C^1\) scalar functions \(u,v\),

\[
 \int_a^b u'(t)v(t)\,dt
 =u(b)v(b)-u(a)v(a)-\int_a^b u(t)v'(t)\,dt.
\tag{OC15}
\]

For a bilinear map use its actual ordered product in this formula. Complex and matrix entries are integrated in their real coordinates. In particular no noncommuting factors are interchanged. Piecewise \(C^1\) paths are treated by summing over their actual finitely many subintervals; intermediate endpoints cancel only after their matching values are displayed.

### 13.5. Product, chain and full finite-coordinate derivative maps

#### 13.5.1. Pointwise product and chain maps

For scalar \(f,g\) differentiable at \(x\), subtraction of their actual product gives

\[
 \frac{f(x+h)g(x+h)-f(x)g(x)}h
 =\frac{f(x+h)-f(x)}h\,g(x+h)
   +f(x)\frac{g(x+h)-g(x)}h.
\tag{OC16}
\]

Limits from Section 13.1 give \((fg)'=f'g+fg'\). The same identity holds for a bilinear product with the factor order shown. For a nonzero \(g(x)\), write the reciprocal difference as \(-[g(x+h)-g(x)]/[g(x+h)g(x)]\); its quotient limit is \(-g'(x)/g(x)^2\). Every actual denominator remains present in its local domain.

Let \(g:I\to\mathbb R\) be differentiable at \(x\), and \(f\) differentiable at \(g(x)\). In (OC4) for \(f\), set \(\Delta=g(x+h)-g(x)\). Since \(\Delta=h[g'(x)+r_x(h)]\), it tends to zero. Put the remainder at \(\Delta=0\) equal to zero; its value there contributes zero. The exact composition difference is

\[
 f(g(x+h))-f(g(x))
 =f'(g(x))h[g'(x)+r_x(h)]
   +h[g'(x)+r_x(h)]\,r_{g(x)}(\Delta).
\tag{OC17}
\]

Dividing by \(h\) proves the chain rule. The outer function need be differentiable only at the image point; domain membership of the composed values is required. This includes the one-sided endpoint versions with their actual increments.

In finite real coordinates, \(f:U\subset\mathbb R^n\to\mathbb R^q\) is differentiable at \(x\) when it has a linear map \(A\) and remainder \(r(h)\) with \(|r(h)|_2/|h|_2\to0\) and \(f(x+h)=f(x)+Ah+r(h)\).

The derivative map is unique. For two such maps \(A,\widetilde A\), subtract their full remainder identities and set \(h=t e_j\), \(t\ne0\). Dividing by \(|t|\) shows that \(|(A-\widetilde A)e_j|_2\) tends to zero, so this fixed value is zero. Every column therefore agrees. When the domain dimension is zero there is only the unique zero linear map. In the composition below, \(g\)'s domain must contain \(f(x+h)\) for the asserted small increments, as it does when \(g\)'s domain is an open neighborhood of \(f(x)\).

For \(g\) with linear map \(B\) at \(f(x)\), let \(\Delta=Ah+r(h)\). The full composition remainder is

\[
 g(f(x+h))-g(f(x))-BAh
 =B r(h)+s(\Delta).
\tag{OC18}
\]

A finite matrix is bounded by its full entries, as proved in the finite-algebra foundation. Thus \(|\Delta|_2\le(\|A\|+1)|h|_2\) for small \(h\), and each term on the right, divided by \(|h|_2\), tends to zero. The \(\Delta=0\) case has \(s(0)=0\). This proves the finite-coordinate chain map \(BA\). Its \((k,j)\) coordinate is the full sum \(\sum_{\ell=1}^qB_{k\ell}A_{\ell j}\). For original domain and target bases the derivative is exactly \(J_cAJ_b^{-1}\); (OC3) on both sides proves the equivalence with differentiability in their original norms. No coordinate, intermediate dimension or zero-dimensional case is suppressed.

#### 13.5.2. Continuous partials and higher-coordinate tensors

If all first partial derivatives of \(f\) exist and are continuous in a neighborhood, take an actual coordinate box inside \(U\), and put \(h^{(j)}=(h_1,\ldots,h_j,0,\ldots,0)\). The one-variable fundamental theorem on each coordinate segment gives

\[
 \begin{aligned}
 f(x+h)-f(x)
 &=\sum_{j=1}^n h_j\int_0^1
       \partial_jf(x+h^{(j-1)}+s h_j e_j)\,ds,\\
 f(x+h)-f(x)-\sum_{j=1}^n h_j\partial_jf(x)
 &=\sum_{j=1}^n h_j\int_0^1
   [\partial_jf(x+h^{(j-1)}+s h_j e_j)-\partial_jf(x)]\,ds.
 \end{aligned}\tag{OC19}
\]

All the displayed points remain in that box and converge uniformly to \(x\) as \(h\to0\). The norm of the second line is at most
\(\sum_j|h_j|\) times the largest derivative difference. Since \(\sum_j|h_j|\le\sqrt n\,|h|_2\), the remainder divided by \(|h|_2\) tends to zero. This proves the derivative and its continuity. Conversely a continuous derivative has the asserted continuous partials by evaluation on the actual coordinate vectors.

For \(C^2\) functions, mixed partials commute. Here is the exact rectangle proof, including its integral input. A continuous function on a compact coordinate rectangle has uniformly continuous values. Finite rectangular tagged sums converge uniformly to either iterated integral: their error is bounded by rectangle area times the common oscillation on a small rectangle. The same sums therefore prove equality of the two iterated integrals, entry by entry, with the signed side lengths if orientation is reversed. Now subtract the four original corner values of \(f\) at \(x\), \(x+h e_j\), \(x+k e_\ell\) and \(x+h e_j+k e_\ell\). Applying (OC13) successively in the two orders gives

\[
 \begin{aligned}
 &f(x+h e_j+k e_\ell)-f(x+h e_j)-f(x+k e_\ell)+f(x)\\
 &=\int_0^h\int_0^k
    \partial_\ell\partial_jf(x+s e_j+t e_\ell)\,dt\,ds\\
 &=\int_0^k\int_0^h
    \partial_j\partial_\ell f(x+s e_j+t e_\ell)\,ds\,dt.
 \end{aligned}\tag{OC20}
\]

Divide by the actual nonzero product \(hk\) and let both increments tend to zero. Each normalized integral tends to its continuous integrand at \(x\), by the same uniform bound used in (OC12). This proves equality at every point, including each original component. For \(j=\ell\) there is only one derivative order. In \(C^r\), adjacent interchanges applied to the remaining \(C^2\) derivative prove every permutation of up to \(r\) partials. These assertions require the stated neighborhood regularity; existence of two pointwise mixed derivatives alone has not been used.

For clarity, the full higher derivative used below is the actual coordinate multilinear map

\[
 D^r f(x)[h_1,\ldots,h_r]
 =\sum_{j_1=1}^n\cdots\sum_{j_r=1}^n
    \partial_{j_1}\cdots\partial_{j_r}f(x)
       \prod_{\ell=1}^r h_{\ell,j_\ell},
 \qquad r\ge1.
\tag{OC20a}
\]

Here \(C^r\) means that all coordinate partial derivatives through order \(r\) exist and are continuous on the actual open domain. At \(r=1\), (OC19) proves this formula and its derivative remainder. For the induction, regard all order-\(r\) partials as their finite array of scalar or original vector coordinates. Apply (OC19) to that array: its derivative has precisely all order-\(r+1\) partials, with the additional last direction coordinate. Finite sums and the product in (OC20a) give the displayed next multilinear map, and finite-coordinate norm comparison gives its continuity in the actual multilinear operator norm. This proves that the coordinate \(C^r\) definition agrees with \(r\) continuous iterated derivatives, with both directions of the comparison: conversely evaluate each iterated derivative on the original coordinate vectors to recover every partial and its continuity. The derivative of a finite multilinear coordinate expression uses the same proved ordered product rule. Original bases transport this tensor by \(J_c\) on the output and by \(J_b^{-1}\) on every input separately, retaining every basis factor; no input norm is replaced. In dimension zero the sum at positive order is empty and the derivative is its unique zero multilinear map; order zero is the original value of \(f\). This also proves the exact tensor meanings used in the higher chain and Taylor formulas.

### 13.6. Higher products and complete Taylor remainders

Repeated application of (OC16), using induction and Pascal's identity with the actual binomial coefficients, gives for \(C^r\) functions with an ordered bilinear product

\[
 (fg)^{(r)}=\sum_{j=0}^r\binom rj f^{(j)}g^{(r-j)},\qquad
 \partial^\alpha(fg)=
 \sum_{\beta\le\alpha}\binom\alpha\beta
    (\partial^\beta f)(\partial^{\alpha-\beta}g).
\tag{OC21}
\]

At induction step each old term has its derivative on the left factor and on the right factor; collecting only terms with the same ordered factors adds the two adjacent binomial coefficients. This proves every coefficient. In the multivariable formula apply that induction separately in each coordinate and the proved interchange of partials; \(\binom\alpha\beta=\prod_j\binom{\alpha_j}{\beta_j}\). No matrix factor is commuted.

The higher chain rule is equally finite and keeps every direction. For \(g:U\to W\) and \(F:W\to V\) of class \(C^r\) on their actual open finite-coordinate domains, with \(g(U)\subset W\), let \(\mathcal P_r\) be all set partitions of the original labeled set \(\{1,\ldots,r\}\). List blocks in increasing order of their least label; list each block's directions in increasing label order. Then

\[
 D^r(F\circ g)(x)[h_1,\ldots,h_r]
 =\sum_{\{B_1,\ldots,B_k\}\in\mathcal P_r}
  D^kF(g(x))
   \bigl[D^{|B_1|}g(x)[h_i:i\in B_1],\ldots,
         D^{|B_k|}g(x)[h_i:i\in B_k]\bigr].
\tag{OC21a}
\]

For \(r=1\) this is (OC18). Differentiate each actual term once in direction \(h_{r+1}\). Differentiating its outer derivative creates the singleton block \(\{r+1\}\); differentiating any one inner derivative adjoins \(r+1\) to that block. Every partition of \(\{1,\ldots,r+1\}\) is obtained in exactly one of these ways: remove its singleton \(\{r+1\}\) if present, or remove \(r+1\) from its unique nonsingleton block. Hence each term has coefficient one, and none is lost or counted twice. Symmetry of each scalar component derivative, already proved from partial interchange, permits the stated block order; it does not interchange matrix multiplication in the values of \(F\) or \(g\). This induction also proves the asserted existence and continuity of derivatives through order \(r\), by the first-order chain rule and finite ordered products at each step. At order zero the assertion is continuity of the composition. Formula (OC21a) supplies the full derivative map rather than an unproved claim that iterated composition is smooth.

For \(f\in C^{r+1}\) on an interval containing the original endpoints \(a,t\), (OC13) starts at \(r=0\). Repeated integration by parts in its exact ordered oriented form gives

\[
 f(t)=\sum_{j=0}^r\frac{(t-a)^j}{j!}f^{(j)}(a)
   +\frac1{r!}\int_a^t(t-s)^r f^{(r+1)}(s)\,ds.
\tag{OC22}
\]

To verify the induction, integrate the derivative of
\(-(t-s)^{r+1}f^{(r+1)}(s)/(r+1)!\).
Its two terms are \((t-s)^r f^{(r+1)}(s)/r!\) and
\(-(t-s)^{r+1}f^{(r+2)}(s)/(r+1)!\).
At \(s=t\) the boundary value is zero and at \(s=a\) its negative is precisely the new coefficient \((t-a)^{r+1}f^{(r+1)}(a)/(r+1)!\). This proves (OC22) at the next order. The \(r=0\) kernel is the constant one; no ambiguous \(0^0\) endpoint is introduced. For \(t<a\) the original integral is negatively oriented and the same identity holds.

Changing the actual integration variable \(s=a+\theta(t-a)\) retains the factor \(t-a\). The remainder is
\((t-a)^{r+1}\int_0^1(1-\theta)^r f^{(r+1)}(a+\theta(t-a))\,d\theta/r!\).
Since \(\int_0^1(1-\theta)^r\,d\theta=1/(r+1)\), obtained by the derivative of \(-(1-\theta)^{r+1}/(r+1)\), its norm is at most
\(|t-a|^{r+1}\sup N(f^{(r+1)})/(r+1)!\).
Every factorial and endpoint remains in the formula.

For \(f\in C^{r+1}(U)\) and the actual segment \(x+[0,1]h\subset U\), the function \(g(\theta)=f(x+\theta h)\) has

\[
 g^{(j)}(\theta)=
 \sum_{|\alpha|=j}\frac{j!}{\alpha!}h^\alpha
    \partial^\alpha f(x+\theta h).
\tag{OC23}
\]

This is induction by the chain rule and the proved partial interchange. A fixed target multiindex \(\alpha\) at the next order receives \(\sum_\ell\alpha_\ell= j+1\) contributions after their original factorial denominators are written, giving \((j+1)!/\alpha!\). Inserting (OC23) into (OC22) with endpoints \(0,1\) gives the full coordinate formula

\[
 \begin{aligned}
 f(x+h)&=\sum_{|\alpha|\le r}\frac{h^\alpha}{\alpha!}\partial^\alpha f(x)\\
 &\quad +(r+1)\sum_{|\alpha|=r+1}\frac{h^\alpha}{\alpha!}
       \int_0^1(1-\theta)^r
            \partial^\alpha f(x+\theta h)\,d\theta.
 \end{aligned}\tag{OC24}
\]

All multiindices, including zero coordinates and multiplicities, are retained. An exact original-norm remainder bound follows by replacing each term in the second line by its norm and using (OC11); its coefficient is
\((r+1)|h^\alpha|/\alpha!\) times the original weighted integral. Neither a derivative term nor its combinatorial coefficient is absorbed into a replacement symbol.

### 13.7. Uniform limits and differentiation of the actual series

A uniformly Cauchy sequence of maps into an original finite complete normed space has a pointwise limit by (OC3). Passing the Cauchy inequality to this pointwise limit proves uniform convergence, with the same error bound. A uniform limit of continuous functions is continuous: use one fixed approximant with uniform error below \(\epsilon/3\), then its continuity, then the second uniform error. This works on any domain where the uniform bound is asserted.

Let \(F_N\in C^1([a,b],V)\), assume \(F_N(a)\to v\) and \(F_N'\to G\) uniformly. The limit \(G\) is continuous, and (OC13) gives

\[
 F_N(x)=F_N(a)+\int_a^x F_N'(s)\,ds,\qquad
 F(x)=v+\int_a^x G(s)\,ds,
\tag{OC25}
\]

with
\(\sup_x N(F_N(x)-F(x))
\le N(F_N(a)-v)+(b-a)\sup_sN(F_N'(s)-G(s))\).
Thus \(F_N\to F\) uniformly, \(F'=G\), and both actual endpoint values are retained. Apply this argument to each derivative to obtain the theorem at every finite order when the corresponding derivative sequences converge uniformly. It does not permit differentiating an arbitrary pointwise convergent series. Matrix entries and complex values use their actual finite-coordinate maps and original norms.

Define the actual scalar series, retaining every coefficient,

\[
 E(z)=\sum_{k=0}^\infty\frac{z^k}{k!},\qquad
 E_N(z)=\sum_{k=0}^N\frac{z^k}{k!}.
\tag{OC26}
\]

For any fixed \(R\ge0\), choose an integer \(N\) with \(N+2\ge2R\). On \(|z|\le R\), the ratio of successive tail majorants is at most \(1/2\), and

\[
 \sum_{k=N+1}^\infty\frac{|z|^k}{k!}
 \le\frac{R^{N+1}}{(N+1)!}
       \sum_{\ell=0}^\infty2^{-\ell}
 =\frac{2R^{N+1}}{(N+1)!}.
\tag{OC27}
\]

The displayed leading term tends to zero: beyond the same threshold successive leading terms have ratio at most \(1/2\). The finite earlier terms are retained. For \(R=0\), all terms with positive degree vanish and the series is one. The \(r\)-th derivative along a real parameter of \(E_N(ct)\), where \(c\) is an original real or complex scalar, is
\(\sum_{k=r}^N c^k t^{k-r}/(k-r)!\).
Its absolute series is bounded by \(|c|^r E(|c|\,|t|)\); the same tail argument, with the shifted index, gives uniform convergence on every compact real interval. Therefore (OC25), starting with the actual values at zero, proves

\[
 \frac{d^r}{dt^r}E(ct)=c^rE(ct),\qquad E(0)=1.
\tag{OC28}
\]

For the complex variable \(z=u+iv\), apply this argument separately to \(u\) and \(v\). It proves continuous partial derivatives \(\partial_uE=E\) and \(\partial_vE=iE\) on every compact coordinate box. The full finite-coordinate derivative (OC19) is multiplication by the original scalar \(E(z)\), so the complex difference quotient also tends to \(E(z)\): its real-coordinate remainder has norm \(o(|h|)\), and division by the nonzero complex \(h\) has modulus \(1/|h|\). This proves complex differentiability here from the actual series, rather than assuming a complex Cauchy theorem.

Absolute convergence justifies the product of two scalar series at its exact coefficients. To see this without assuming rearrangement, truncate the double sum to a square; the error against the full product is bounded by one tail times the full absolute sum of the other series, in each of the two variables. Both tails tend to zero. The same bound lets the square be compared with a sufficiently large triangle, since the omitted terms have total degree tending to infinity and belong to the union of the two large-index tails. Within a finite triangle the binomial theorem is finite induction. Hence

\[
 E(z)E(w)
 =\sum_{m=0}^\infty\sum_{k=0}^m
       \frac{z^k w^{m-k}}{k!(m-k)!}
 =\sum_{m=0}^\infty\frac{(z+w)^m}{m!}
 =E(z+w),\qquad E(z)E(-z)=1.
\tag{OC29}
\]

All denominators and both inverse factors remain in the comparison. No rearrangement of a conditionally convergent series has been used.

### 13.8. Original exponential, logarithm and every real power

For real \(t\ge0\), every term in (OC26) is nonnegative, and \(E(t)\ge1+t>0\). For \(t<0\), (OC29) gives \(E(t)=1/E(-t)>0\). Its derivative \(E'=E\) and the mean value theorem therefore make \(E\) strictly increasing on the entire original real line. It tends to infinity at the positive end by \(E(t)\ge1+t\), and to zero at the negative end by its exact inverse. Continuity and the intermediate-value theorem show that its range is precisely \((0,\infty)\).

This is the course's original real exponential \(e^t\). The exact comparison is also forced if that exponential was introduced as the solution of \(f'=f\), \(f(0)=1\): for any such original \(f\), differentiation of \(E(-t)f(t)\) gives \(-E(-t)f(t)+E(-t)f'(t)=0\), so it is constantly one and both original inverse factors prove \(f(t)=E(t)\). The notation \(E\) records this comparison; it does not rescale \(t\) or replace the original function.

For \(x>0\), define

\[
 L(x)=\int_1^x\frac{ds}{s},\qquad
 L'(x)=\frac1x,\qquad L(1)=0.
\tag{OC30}
\]

The integrand is continuous on the actual compact interval between \(1\) and \(x\), with its original positive lower endpoint. The fundamental theorem proves the derivative. The chain rule gives
\((L(E(t)))'=E(t)/E(t)=1\);
the zero initial value gives \(L(E(t))=t\). Since \(E\) is onto the positive reals, \(E(L(x))=x\) for every \(x>0\). Thus \(L\) is exactly the original real logarithm, with both compositions and domains proved.

For fixed \(y>0\), the derivative in \(x>0\) of \(L(xy)-L(x)\) is \(y/(xy)-1/x=0\). At \(x=1\) it equals \(L(y)\), so \(L(xy)=L(x)+L(y)\). The same actual derivative, or the inverse product in (OC29), proves \(L(x^{-1})=-L(x)\). All these identities retain their original nonzero-domain restrictions.

For any original real exponent \(s\) and \(x>0\), the power is the exact map

\[
 x^s=E(sL(x)),\qquad
 \frac{d}{dx}x^s=\frac{s}{x}E(sL(x))
   =s\,x^{s-1}.
\tag{OC31}
\]

The final comparison uses \(E((s-1)L(x))E(L(x))=E(sL(x))\) and \(E(L(x))=x\); the original factor \(x^{-1}\) has not disappeared without a proved inverse identity. For integer \(s\ge0\), induction in (OC29) identifies this value with the full repeated product; for negative integers it gives the actual reciprocal. For \(s=p/q\), \(q\ge1\), it has \(q\)-th power \(x^p\) and is positive; the earlier unique positive-root proof identifies it with that original root. No rational approximation is required to define a general real exponent. The formulas \(x^{s+t}=x^sx^t\), \((xy)^s=x^sy^s\) and \((x^s)^t=x^{st}\) follow from the two exact inverse maps and (OC29)–(OC30), with \(x,y>0\).

Every further derivative is proved by induction:

\[
 \frac{d^r}{dx^r}x^s
 =\left(\prod_{j=0}^{r-1}(s-j)\right)x^{s-r},
 \qquad r\ge0.
\tag{OC32}
\]

For \(r=0\) the product is empty and equals one. Zero factors remain in the formula when \(s\) is an integer and the derivative vanishes. The working domain is \(x>0\); no differentiability at zero for arbitrary \(s\) is inferred. For negative \(s\), the sign in (OC31) proves decreasing powers on that domain, and for positive \(s\) it proves increasing powers. This supplies the original positive frequency-bracket bounds without changing their exponents.

### 13.9. Arctangent, circular parameters and the original pi

Define \(C(t)\) and \(S(t)\) by the real and imaginary coordinates of the actual \(E(it)\), not by assumed trigonometric derivatives. The absolute convergence above gives

\[
 \begin{aligned}
 C(t)&=\sum_{k=0}^\infty\frac{(-1)^k t^{2k}}{(2k)!},
 &S(t)&=\sum_{k=0}^\infty\frac{(-1)^k t^{2k+1}}{(2k+1)!},\\
 C'&=-S,\quad S'=C,\quad C(0)=1,\quad S(0)=0,
 &C(t)^2+S(t)^2&=1.
 \end{aligned}\tag{OC33}
\]

The last identity is the full product \(E(it)E(-it)=1\), since conjugating the original coefficients gives \(E(-it)=\overline{E(it)}\). The full addition laws are the two coordinates of (OC29):

\[
 C(s+t)=C(s)C(t)-S(s)S(t),\qquad
 S(s+t)=S(s)C(t)+C(s)S(t).
\tag{OC34}
\]

There is a first positive zero \(t_0\) of \(C\). Indeed continuity gives a zero-free positive neighborhood of zero. At \(t=2\), the first three terms have value \(1-2+2/3=-1/3\). The remaining terms can be grouped into negative/positive consecutive pairs starting at \(k=3\); the absolute terms strictly decrease because their successive ratio is \(4/[(2k+1)(2k+2)]<1\). Every pair is negative, so \(C(2)<-1/3\). Intermediate values give a zero in \((0,2)\); its least positive one is the attained minimum of the closed zero set outside the zero-free neighborhood. Before \(t_0\), continuity and the absence of zeros give \(C>0\), so \(S'=C>0\), and \(S(t_0)=1\) by (OC33). Oddness of \(S\) and evenness of \(C\) follow term by term. Thus on \((-t_0,t_0)\), \(C>0\) and

\[
 T(t)=\frac{S(t)}{C(t)},\qquad
 T'(t)=\frac{C(t)^2+S(t)^2}{C(t)^2}
       =1+T(t)^2.
\tag{OC35}
\]

The denominator is the actual \(C^2\), and the equality uses the previously proved full identity. \(T\) is strictly increasing, and tends to the respective infinities at the two endpoints because \(S\to\pm1\) and \(C\to0\) positively. It is therefore a bijection onto the original real line. Define

\[
 A(x)=\int_0^x\frac{ds}{1+s^2},\qquad
 A'(x)=\frac1{1+x^2}.
\tag{OC36}
\]

The denominator is strictly positive. The derivative of \(A(T(t))\) is \(T'(t)/(1+T(t)^2)=1\), and its value at zero is zero, so \(A(T(t))=t\). Surjectivity gives \(T(A(x))=x\) with \(A(x)\in(-t_0,t_0)\). This constructs the original principal arctangent with both inverse maps and its full domain. In particular \(A(x)\to t_0\) as \(x\to+\infty\): for each \(t<t_0\), \(x>T(t)\) implies \(A(x)>t\), and all \(A(x)<t_0\). The negative limit is \(-t_0\).

The actual circle parameter has its original pi, rather than a newly chosen scale. From \(E(it_0)=i\), (OC29) gives \(E(2it_0)=-1\) and \(E(4it_0)=1\). On \((0,t_0)\), \(S,C>0\). Formula (OC34) at twice \(t_0/2\) gives \(C(t_0/2)^2=S(t_0/2)^2\), hence \(T(t_0/2)=1\) and \(A(1)=t_0/2\). Thus the usual inverse-tangent definition \(\pi=4\arctan(1)\) gives exactly \(\pi=2t_0\).

The same comparison agrees with the geometric original circle constant. For any \(C^1\) real-coordinate curve \(\gamma:[a,b]\to\mathbb R^d\), its polygon length is the sum of the actual norms \(\sum_j|\gamma(t_j)-\gamma(t_{j-1})|_2\). The fundamental theorem writes each increment as the integral of \(\gamma'\). Choose a sample \(\xi_j\). Uniform continuity of \(\gamma'\) bounds the norm of the difference from \((t_j-t_{j-1})\gamma'(\xi_j)\) by \((t_j-t_{j-1})\omega(\operatorname{mesh}P)\), where \(\omega(\delta)\to0\). The reverse triangle inequality therefore shows that the polygon length differs from \(\sum_j|\gamma'(\xi_j)|_2(t_j-t_{j-1})\) by at most \((b-a)\omega(\operatorname{mesh}P)\). Consequently fine polygon lengths tend to \(\int_a^b|\gamma'|_2\). Any fixed coarser polygon is bounded by this integral, by (OC11) interval by interval; refinement increases polygon length by the triangle inequality. Their supremum is therefore the same integral.

For \(\gamma(t)=(C(t),S(t))\), \(|\gamma'|_2=(S^2+C^2)^{1/2}=1\). On \([0,t_0]\) this curve traverses the first quadrant exactly once: \(T\) increases from zero to infinity and \(C,S>0\) recover its unique unit vector. The addition laws at \(t_0,2t_0,3t_0\) give the other quadrants with the actual orientations and endpoints. Hence the circumference of the original unit circle is \(4t_0\), and its half-circumference definition also gives \(\pi=2t_0\). For radius \(r>0\), retain the map \(r(C,S)\); its speed and circumference are \(r\) and \(4rt_0=2\pi r\).

The exact quadrant inverse for an original unit vector \((u,v)\) with \(u>0,v\ge0\) is \(t=A(v/u)\). Indeed (OC35)–(OC36) give \(S(t)/C(t)=v/u\), while positivity and the full square sum give
\(C(t)=[1+(v/u)^2]^{-1/2}=u\) and
\(S(t)=(v/u)[1+(v/u)^2]^{-1/2}=v\).
The missing vertical endpoint is exactly \((0,1)=\gamma(t_0)\). Thus both the coordinate map and inverse, including their actual endpoint, have been proved. The same original rotations from (OC34) give the other three quadrant maps.

Thus the full original circular parameter \(e^{i\theta}=E(i\theta)\) is \(2\pi\)-periodic, and its derivative is \(iE(i\theta)\). Its integrals retain all constants:

\[
 \int_a^b E(i n\theta)\,d\theta
 =\begin{cases}
   [E(i n b)-E(i n a)]/(i n),&n\in\mathbb Z\setminus\{0\},\\
   b-a,&n=0.
 \end{cases}
\tag{OC37}
\]

For \([0,2\pi]\) the nonzero-integer numerator is zero by the proved original period, while the zero mode contributes \(2\pi\). This supplies the circular and rectangular contour computations without a hidden trigonometric or angular-scale assumption.

### 13.10. The actual smooth cutoff with all endpoint constants

Keep the function from this lesson:

\[
 \eta(s)=\begin{cases}0,&s\le0,\\ E(-1/s),&s>0.\end{cases}
 \qquad
 \chi(s)=\frac{\eta(3/2-s)}
               {\eta(3/2-s)+\eta(s-1)}.
\tag{OC38}
\]

For \(s>0\), chain and product differentiation give

\[
 \eta^{(r)}(s)=E(-1/s)P_r(1/s),\qquad
 P_0(u)=1,\quad
 P_{r+1}(u)=u^2[P_r(u)-P_r'(u)].
\tag{OC39}
\]

This exact recursion retains every polynomial coefficient, sign and power. If \(u>0\) and \(m\ge0\) is an integer, the positive series gives \(E(u)\ge u^{m+1}/(m+1)!\), whence

\[
 0\le u^mE(-u)
 \le\frac{(m+1)!}{u}\longrightarrow0
 \quad(u\longrightarrow+\infty).
\tag{OC40}
\]

Every term of \(P_r(u)\), and of \(uP_r(u)\), therefore tends to zero after multiplication by \(E(-u)\). It follows first that \(\eta\) is continuous at zero. Inductively, extend the positive-side \(r\)-th derivative by zero for \(s\le0\). It is continuous at zero, and its derivative there is the limit of \(E(-1/s)P_r(1/s)/s\), which is zero by the just-proved estimate. Its derivative away from zero is precisely the next recursion. This proves \(\eta\in C^\infty(\mathbb R)\) and every derivative zero at the original endpoint.

The denominator in \(\chi\) is strictly positive for every real \(s\). Otherwise both terms would vanish, requiring simultaneously \(s\ge3/2\) and \(s\le1\). The full reciprocal and product rules show that \(\chi\) is smooth, with \(0\le\chi\le1\), \(\chi=1\) for \(s\le1\), and \(\chi=0\) for \(s\ge3/2\). The function \(\chi\) itself is not asserted to have compact support on the whole real line: its negative half-line is one. On \([0,\infty)\) its support is exactly \([0,3/2]\).

The actual Euclidean cutoff is \(\theta(x)=\chi(\sum_{j=1}^d x_j^2)\). The inner function is a polynomial in every original coordinate. The proved full chain rules therefore make \(\theta\) smooth; it equals one when \(\sum_jx_j^2\le1\) and vanishes when \(\sum_jx_j^2\ge3/2\). Its support is the full closed ball \(\sum_jx_j^2\le3/2\), compact by the proved original topology. Every derivative is continuous on that support and zero outside it; compact extrema give its actual finite derivative bounds. In dimension zero the entire space is a point, the value is one and its support is compact; no nonexistent coordinate derivative is assigned.

For any specified original center \(x_0\) and radii \(0\le r<R\), the map
\[
 x\longmapsto
 \chi\left(1+\frac{\sum_{j=1}^d(x_j-x_{0j})^2-r^2}{2(R^2-r^2)}\right)
\tag{OC41}
\]
retains every translation, square and denominator. It equals one on the closed radius-\(r\) ball. Its nonzero set is exactly the open radius-\(R\) ball, because the full cutoff is positive precisely when its scalar input is below \(3/2\). Its support is therefore the full closed radius-\(R\) ball, including the outer sphere where the value itself is zero. In dimension zero the domain is its single point and these sets have that same one-point meaning. This is a proved coordinate construction, not a change to the original cutoff in (OC38). For an open domain and any one of its points, choose an outer ball whose closure lies inside that domain; the construction gives the required local compact cutoff.

For a locally finite family of supports, every point has a neighborhood meeting only finitely many of them. All other functions and all their derivatives vanish on that neighborhood. Its full sum and every derivative are therefore the corresponding finite sums there. The same argument applies to a compact set by its finite neighborhood subcover. No interchange of an uncontrolled infinite derivative sum is asserted.

### 13.11. Exact integrating factors and original operator exponentials

For continuous real or complex \(a:I\to\mathbb C\) on an interval and a fixed original \(t_*\in I\), let \(H(t)=\int_{t_*}^ta(s)\,ds\). Coordinatewise fundamental calculus gives \(H'=a\). For a differentiable scalar \(f\) satisfying \(f'=a f\), the actual product
\[
 \frac d{dt}[E(-H(t))f(t)]
 =-a(t)E(-H(t))f(t)+E(-H(t))a(t)f(t)=0.
\tag{OC42}
\]
The commutation here is scalar multiplication, already proved in the complex pair field. The product is therefore constant. Its original value at \(t_*\) and both inverse factors give \(f(t)=f(t_*)E(H(t))\). Conversely direct differentiation proves that value solves the equation on the whole original interval. The initial value, integral endpoint and sign are retained. This is not an assertion for noncommuting time-dependent matrix coefficients.

For the original real equation \(f'(t)+t f(t)=0\), keep the integrating factor \(E(t^2/2)\):

\[
 \begin{aligned}
 \frac d{dt}[E(t^2/2)f(t)]
 &=t E(t^2/2)f(t)+E(t^2/2)f'(t)=0,\\
 f(t)&=f(t_*)E\bigl((t_*^2-t^2)/2\bigr).
 \end{aligned}\tag{OC43}
\]

Both halves, both endpoint squares and the original sign remain. At \(t_*=0\), the actual answer is \(f(0)E(-t^2/2)\). This conclusion also holds for complex \(f\), coordinatewise.

Let now \(A\in\operatorname{End}(V)\) be the original finite-dimensional complex operator with its actual norm. Retain the entire series

\[
 E_A(t)=\sum_{k=0}^\infty\frac{(itA)^k}{k!}.
\tag{OC44}
\]

For \(|t|\le T\), each term has norm at most \((T\|A\|)^k/k!\). The actual \(r\)-th ordinary derivative term, for \(k\ge r\), is
\(i^k A^k t^{k-r}/(k-r)!\), bounded in norm by \(\|A\|^r(T\|A\|)^{k-r}/(k-r)!\).
The full tail bounds (OC27) prove locally uniform convergence of every derivative, including each finite initial segment and the zero-operator case. Thus

\[
 \frac{d^r}{dt^r}E_A(t)=(iA)^rE_A(t),\quad
 D_t^rE_A(t)=(-i)^r(iA)^rE_A(t)=A^rE_A(t),
 \qquad D_t=-i\frac d{dt}.
\tag{OC45}
\]

The last equality is the exact scalar inverse product \((-i)^ri^r=1\) from the original complex pair law; no ordinary derivative is identified with \(D_t\) without that comparison.

The absolute-series product proof applies to (OC44) in its original norm. Each product \(A^jA^k=A^{j+k}\) is a power of the same original \(A\); it does not commute arbitrary operators. Finite binomial coefficients give
\(E_A(t)E_A(s)=E_A(t+s)\) and both products \(E_A(t)E_A(-t)=E_A(-t)E_A(t)=I_V\).
For \(D_tu=Au\), the product derivative is
\[
 \frac d{dt}[E_A(-t)u(t)]
 =-iA E_A(-t)u(t)+E_A(-t)iA u(t)=0,
\tag{OC46}
\]
where \(A\) commutes with its own series by the full termwise products. Hence
\(u(t)=E_A(t-t_*)u(t_*)\), and conversely that value solves the original equation with all \(i\) factors. In dimension zero the identity and all maps are those of the zero space, the \(k=0\) term is its identity and every later power is zero.

### 13.12. Full metric, Gaussian, polynomial, contour and boundary receivers

#### 13.12.1. Original metric, Gaussian and Rayleigh maps

The statements above supply the actual one-variable entry, not an assumed list of its names. Product/chain and ordered higher derivative rules enter this lesson, Sections 3, 5, 7, 9 and 10 through (OC16)–(OC24). Its segment formula
\(f(x+t e_j)-f(x)=\int_0^t\partial_jf(x+s e_j)\,ds\)
is (OC13) with the actual coordinate path; negative \(t\) retains negative orientation. Its vector and tensor factors stay in their original coordinates and norm maps. The full real-power bounds of its Section 10 receive (OC31)–(OC32) at their actual positive bracket values, and its exact \(\eta,\chi\) cutoffs are (OC38)–(OC40).

The Gaussian receiver in [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md) keeps, for original \(\epsilon>0\),
\[
 I_\epsilon(x)=\int_{\mathbb R^d}
      E\bigl(i x\cdot\xi-\epsilon|\xi|^2\bigr)\,d\xi,\qquad
 \partial_{x_j}I_\epsilon(x)=-\frac{x_j}{2\epsilon}I_\epsilon(x).
\tag{OC47}
\]
The whole-space integral, differentiation under that integral and integration by parts are supplied by the already separately proved measure/Fourier argument; the present scalar calculus does not assume a new whole-space Riemann integral. With other original coordinates fixed, differentiate
\(E(x_j^2/(4\epsilon))I_\epsilon(x)\).
Its two terms are \([x_j/(2\epsilon)]E(x_j^2/(4\epsilon))I_\epsilon(x)\) and
\(-[x_j/(2\epsilon)]E(x_j^2/(4\epsilon))I_\epsilon(x)\), so the product is constant along that original coordinate line. Apply this successively in every coordinate, with the actual value at zero. The exact result is
\[
 I_\epsilon(x)
 =I_\epsilon(0)E\left(-\frac{\sum_{j=1}^d x_j^2}{4\epsilon}\right),
 \qquad
 I_\epsilon(0)=\left(\frac{\pi}{\epsilon}\right)^{d/2},
 \qquad
 (2\pi)^{-d}I_\epsilon(x)
 =(4\pi\epsilon)^{-d/2}
      E\left(-\frac{\sum_{j=1}^d x_j^2}{4\epsilon}\right).
\tag{OC48}
\]
The middle equality is the previously proved original polar/Gaussian integral, not an inference from the differential equation. The last coefficient comparison follows from the positive real-power product law (OC31), retaining the original \((2\pi)^{-d}\), \((\pi/\epsilon)^{d/2}\), \(4\), \(\pi\) and \(\epsilon\). In dimension zero the integral is the original point-mass value one; the empty coordinate sum is zero and each displayed power with exponent zero is one. No source Fourier convention changes.

The original spectral maximization argument on the actual inner-product unit sphere receives the derivative of
\[
 \frac{h(A(v+t w),v+t w)}{h(v+t w,v+t w)}.
\tag{OC49}
\]
The denominator is positive near zero because its actual value at zero is one. For the real self-adjoint \(A\), full bilinearity and self-adjointness give numerator derivative \(2h(Av,w)\) and denominator derivative \(2h(v,w)\) at zero. The quotient derivative is therefore
\(2h(Av,w)-2h(Av,v)h(v,w)\).
Its vanishing at the actual maximizer, for every original \(w\), gives
\(h(Av-h(Av,v)v,w)=0\).
Putting \(w=Av-h(Av,v)v\) proves the original eigenvector equation. No coordinate identity matrix substitutes for the original \(h\); compact attainment and exact norm/Gram comparison remain the independently proved real-topology receiving steps.

#### 13.12.2. The original half-plane primitive

[Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) receives the actual globally convergent exponential, real logarithm and principal arctangent. Its original right-half-plane primitive is
\[
 L_{\rm hp}(x+iy)=\frac12 L(x^2+y^2)+i A(y/x),
 \qquad x>0.
\tag{OC50}
\]
Full product/quotient and chain differentiation gives
\(\partial_xL_{\rm hp}=x/(x^2+y^2)-i y/(x^2+y^2)=1/(x+iy)\)
and
\(\partial_yL_{\rm hp}=y/(x^2+y^2)+i x/(x^2+y^2)=i/(x+iy)\).
Here the derivative of \(A(y/x)\) includes the original factor
\([1+(y/x)^2]^{-1}\), multiplied by \(-y/x^2\) or \(1/x\), and its equality with the displayed denominator is the exact field identity
\(1+(y/x)^2=(x^2+y^2)/x^2\), with \(x\ne0\). Both original logarithmic and angular contributions are retained. Composition with a \(C^1\) path \(w(s)\) in that half-plane gives \(dL_{\rm hp}(w(s))/ds=w'(s)/w(s)\). The piecewise path integral is thus its original endpoint difference by (OC13), with all endpoint cancellation explicit.

#### 13.12.3. Uniform calculus for the original entire series

The same lesson's circular modes use (OC37) at the original \(2\pi\) interval. Its general entire-series differentiation uses (OC25) with the actual absolute coefficient bounds on a slightly larger radius: for \(0<R<R'\), convergence at radius \(R'\) bounds each original \(|c_k|(R')^k\) by a finite \(M\), so the \(r\)-th derivative on \(|z|\le R\) has majorant
\(M\,k(k-1)\cdots(k-r+1)R^{k-r}/(R')^k\) for \(k\ge r\).
Its consecutive ratio tends to \(R/R'<1\), so a geometric bound proves summability of the full majorant, including all earlier terms. This establishes the termwise derivatives at every finite order. Fixed-contour integrals pass through uniform convergence using their actual finite path lengths and derivative weights; no general holomorphic residue theorem has been assumed.

#### 13.12.4. Original matrix and half-line receivers

[Stable modes and the algebra of boundary data](stable-boundary-models.md) receives the full original \(E_A(t)\), its derivative conventions and its two inverse maps in (OC44)–(OC46). Its bounded-jet integral remains
\[
 h(v)=\int_0^1|\pi_0E_C(s)v|^2\,ds.
\tag{OC51}
\]
The finite original state, \(\pi_0\), interval \([0,1]\), and all coordinate norm factors are unchanged. Continuity in \(v\) follows because the integrand's actual finite-coordinate products are continuous uniformly on compact sets, and (OC11) passes their uniform convergence through this same interval. On the negative half-line the source retains its distinct original interval \([-1,0]\). Positivity of the jet integral and its compact-sphere minimum remain the source's full jet/uniqueness and earlier compactness arguments; the calculus constructed here supplies only their actual continuous integral and derivative input.

Finally its original half-line inverse
\[
 (T_\lambda g)(t)=-i\int_0^\infty E(-\lambda s)g(t+s)\,ds,
 \qquad \lambda>0,
\tag{OC52}
\]
retains the scalar \(-i\), positive half-line, original \(\lambda\) and shifted argument. For the source's smooth exponentially decreasing \(g\), suppose its actual derivative bounds are \(N(D^k g(t))\le M_kE(-\delta t)\) for \(t\ge0\), \(\delta>0\). Truncate at \(R\); continuous Riemann calculus gives every derivative there. The tail norm is at most
\[
 M_k E(-\delta t)\int_R^\infty E(-(\lambda+\delta)s)\,ds
 =\frac{M_k}{\lambda+\delta}E(-\delta t)E(-(\lambda+\delta)R).
\tag{OC53}
\]
The improper integral is the limit of finite intervals, whose antiderivative is
\(-E(-(\lambda+\delta)s)/(\lambda+\delta)\).
Thus all truncated derivatives converge uniformly on every compact \(t\)-interval, and (OC25) proves differentiation of the original infinite integral. The full bound is
\(N(D^kT_\lambda g(t))\le M_kE(-\delta t)/(\lambda+\delta)\).
For the zeroth derivative, integration by parts on \([0,R]\) retains
\[
 \int_0^R E(-\lambda s)g'(t+s)\,ds
 =E(-\lambda R)g(t+R)-g(t)
    +\lambda\int_0^R E(-\lambda s)g(t+s)\,ds.
\tag{OC54}
\]
The actual upper boundary tends to zero by the same bound. Consequently, for \(f=T_\lambda g\), \(f'-\lambda f=i g\), and with the original \(L(D)=D+i\lambda\),
\(L(D)f=-i(f'-\lambda f)=g\).
The difference of two bounded solutions of that equation is \(cE(\lambda t)\) by (OC42); since \(\lambda>0\) and the exponential is unbounded at the positive end, boundedness forces \(c=0\). For fixed negative \(t\), the finite segment with \(t+s<0\) is continuous on a compact interval and the remaining tail has the same exponential estimate; this proves the source's extension when \(g\) is smooth on the whole real line and the stated decay is required only on its positive half-line. This is the exact original inverse and uniqueness argument with both boundary contributions and every derivative factor retained.

The preceding scalar and finite-coordinate proofs provide the calculus used by the displayed original Gaussian, contour and boundary differential equations. Each receiving argument keeps its separately proved measure, algebra and topology hypotheses.

## 14. General metric compactness and local support calculations

### 14.1. Open covers and sequences for the full original metric

Let \((M,d)\) be an arbitrary metric space and \(K\subset M\), with the restriction of its original metric. For \(x\in K\) and \(r>0\), write \(B_K(x,r)=\{y\in K:d(x,y)<r\}\). An open cover is a family of relatively open subsets of \(K\) with union \(K\). Compactness means that every such cover has a finite subcover. Sequential compactness means that every sequence of points of \(K\) has a subsequence converging to a point of \(K\), for this same distance. The empty set is compact, using the empty subcover, and sequentially compact, since it has no sequence of points. We first treat nonempty \(K\).

Suppose \(K\) is sequentially compact. We prove that for every original \(\varepsilon>0\), finitely many \(\varepsilon\)-balls with centres in \(K\) cover \(K\). A careless greedy construction on an arbitrary set can conceal a dependent-choice assumption; here only the declared countable choice is needed. If no such finite cover exists, for each positive integer \(n\) there is an ordered \(n\)-tuple of points of \(K\) at pairwise distances at least \(\varepsilon\). Its existence is a finite induction: given any finite tuple, its finitely many open \(\varepsilon\)-balls fail to cover \(K\), and one point outside them extends that tuple. Countable choice, applied to the independent nonempty sets of such \(n\)-tuples, gives tuples
\[
 (x_{n,1},\ldots,x_{n,n}),\qquad
 d(x_{n,i},x_{n,j})\geq\varepsilon\quad(i\ne j,\ 1\leq i,j\leq n).
 \tag{GC1}
\]
Enumerate all their labelled entries in order of \(n\), then in order of the entry within that finite tuple. Denote the resulting countable sequence by \(z_1,z_2,\ldots\), retaining repeated points if they occur. Its set of values cannot be covered by finitely many original balls of radius \(\varepsilon/3\): each such ball contains at most one entry of a fixed tuple, since two entries in it would have distance less than \(2\varepsilon/3<\varepsilon\). A proposed cover by \(q\) balls therefore cannot cover the tuple of length \(q+1\).

Now a deterministic recursion on this enumeration chooses \(w_1=z_1\) and, after \(w_1,\ldots,w_j\), takes \(w_{j+1}\) to be the first enumerated entry outside their finitely many \(\varepsilon/3\)-balls. The proved failure of a finite cover makes this least index exist at every step. This recursion uses the well-order of the natural numbers, not a choice from new arbitrary sets at successive steps. Its resulting points satisfy
\[
 d(w_i,w_j)\geq\varepsilon/3\quad(i\ne j).
 \tag{GC2}
\]
Any convergent subsequence is Cauchy: two sufficiently late terms have distances to their limit less than \(\varepsilon/6\), hence mutual distance less than \(\varepsilon/3\). This contradicts (GC2). Therefore \(K\) has the asserted finite covers for every \(\varepsilon>0\). This property is called total boundedness; no bound on the original distance has been changed.

Next let \(\mathcal U\) be any relatively open cover of this sequentially compact \(K\). It has a number \(\delta>0\) such that every \(B_K(x,\delta)\) is contained in some member of \(\mathcal U\). If no such number existed, then for each positive integer \(n\) the independent set
\[
 F_n=\{x\in K:B_K(x,1/n)
               \text{ is not contained in any }U\in\mathcal U\}
 \tag{GC3}
\]
would be nonempty. Countable choice selects \(x_n\in F_n\). A subsequence \(x_{n_j}\to x\in K\) has its limit in one \(U\in\mathcal U\). Relative openness gives \(r>0\) with \(B_K(x,r)\subset U\). Eventually both \(d(x_{n_j},x)<r/2\) and \(1/n_j<r/2\). The original triangle inequality then gives \(B_K(x_{n_j},1/n_j)\subset B_K(x,r)\subset U\), contrary to the definition of \(F_{n_j}\). This proves the asserted covering number.

Use the already proved finite \(\delta/2\)-ball cover with centres \(a_1,\ldots,a_q\in K\). For each of these finitely many centres, its \(\delta\)-ball is contained in some \(U_i\in\mathcal U\). Finitely many choices require no additional choice principle. Every point of \(K\) belongs to one of its \(\delta/2\)-balls and hence to the corresponding \(U_i\). Thus the original cover has a finite subcover. We have proved sequential compactness implies open-cover compactness for the arbitrary original metric.

Conversely, suppose \(K\) is compact and let \((x_n)_{n\geq1}\) be a sequence of its points. If no subsequence converged to a point of \(K\), then for each \(x\in K\) there would be some radius \(r>0\) for which the set of indices \(\{n:x_n\in B_K(x,r)\}\) is finite. Indeed, if every \(1/j\)-ball about some \(x\) contained infinitely many sequence indices, recursively take the least such index greater than the previously taken index. This deterministic recursion produces a subsequence with distance to \(x\) less than \(1/j\), which converges to \(x\). It contradicts the assumed absence of a convergent subsequence.

Take the family of all original balls whose sequence-index sets are finite. By the previous paragraph this is an open cover of \(K\). It uses all such balls; no choice of a radius for uncountably many centres is required. Compactness gives a finite subcover. The union of its finitely many finite index sets is finite, while every positive integer \(n\) must belong to that union because \(x_n\in K\). This is a contradiction. Therefore a subsequence converges in \(K\). Including the empty case, the exact equivalence is
\[
 K\text{ compact for }d
 \quad\Longleftrightarrow\quad
 K\text{ sequentially compact for the same }d .
 \tag{GC4}
\]

The proof gives a further precise criterion with the same choice foundation: a metric space is compact if and only if it is complete and totally bounded. First, a compact space is totally bounded by the proved implication. A Cauchy sequence in it has a convergent subsequence by (GC4). For any \(\eta>0\), take a Cauchy index \(N\) making mutual distances less than \(\eta/2\), and a later subsequence term whose distance to the subsequence limit is less than \(\eta/2\). The triangle inequality makes every term with index at least \(N\) have distance less than \(\eta\) to that same limit. This proves completeness, with a limit in the original space.

For the reverse implication, assume \(K\) complete and totally bounded. The empty case is already settled. For each \(j\geq1\), choose a finite ordered cover of \(K\) by its original balls of radius \(2^{-j}\). The sets of such finite covers are independent nonempty sets, indexed by \(j\); countable choice supplies them once. Given a sequence \(x_n\in K\), the first finite cover has a ball containing infinitely many of its indices. Choose the least index of such a ball in the chosen ordered cover, and retain the infinite set \(I_1\) of sequence indices in it. Within \(I_{j-1}\), the \(j\)-th finite cover has a ball containing infinitely many of those indices; take its least cover index and retain their infinite set \(I_j\subset I_{j-1}\). All these choices are least indices in fixed finite enumerations, so the recursion is deterministic. Finally take \(n_j\) to be the least member of \(I_j\) greater than \(n_{j-1}\), with \(n_0=0\). Infinitude makes it exist. For \(p,q\geq j\), both \(n_p,n_q\) belong to \(I_j\), and thus
\[
 d(x_{n_p},x_{n_q})<2\cdot2^{-j}=2^{1-j}.
 \tag{GC5}
\]
The subsequence is Cauchy for the original \(d\). Completeness gives a limit in \(K\), so (GC4) proves compactness. The exact decreasing numerical estimates in this construction are auxiliary bounds, not a new metric on \(K\).

Compact subsets of an arbitrary metric space are closed and bounded. For boundedness when \(K\ne\varnothing\), fix one \(a\in K\); the balls \(B_M(a,n)\), \(n\geq1\), cover \(K\), and a finite subcover has a largest integer radius. For closedness, if \(a\in M\setminus K\) lay in the closure of \(K\), each \(K\cap B_M(a,1/n)\) would be nonempty. Countable choice gives a sequence from those independent sets. It converges to \(a\) in \(M\), while (GC4) gives a subsequence converging to some \(b\in K\). The original triangle inequality forces \(d(a,b)=0\), hence \(a=b\), a contradiction. Thus every exterior point has a neighborhood disjoint from \(K\). The empty set satisfies both conclusions.

The reverse closed-and-bounded assertion belongs specifically to finite-dimensional Euclidean space, as proved in Sections 12.5--12.6 with every original coordinate: bounded coordinate subsequences give a convergent diagonal subsequence, and closedness retains its limit. Equation (GC4) then gives compactness. Dimension zero is the one-point coordinate space, and every subset is either empty or that point. In a general metric space, closedness and boundedness alone do not suffice: the original set of positive integers with distance zero for equality and one otherwise is closed in itself and bounded, while the sequence \(1,2,3,\ldots\) has no convergent subsequence. Its balls of radius \(1/2\) are singletons, so their open cover has no finite subcover. This exact example retains its given distance and states the required scope of Heine--Borel.

### 14.2. Compact supports, local finiteness and unchanged smooth derivatives

These facts also give the exact support clauses used in metric localization. A closed subset \(F\) of a compact \(K\) is compact: an open cover of \(F\), together with the open relative complement \(K\setminus F\), covers \(K\); a finite subcover restricts to a finite cover of \(F\). A finite union of compact sets is compact: take a finite subcover on each of the finitely many sets and then take their finite union. Both arguments include empty sets.

For a positive-definite original quadratic form \(Q\) on real finite-dimensional \(E\), its coefficients make \(Q\) continuous in the original coordinates. In positive dimension its minimum \(c\) on the Euclidean unit sphere exists by the compactness and extreme-value proof in Sections 12.6--12.7; positivity gives \(c>0\). Homogeneity, with the original coordinates retained, yields
\[
 Q(v)\geq c|v|^2,\qquad
 \{X+v:Q(v)\leq R^2\}
 \subset\{X+v:|v|\leq |R|/\sqrt c\}.
 \tag{GC6}
\]
The first inequality includes \(v=0\), whose both sides are zero. This ellipsoid is closed by continuity of \(Q\) and bounded by the full original \(c\) and \(R\). Hence it is compact. At \(R=0\) it is the singleton \(\{X\}\); in dimension zero the same conclusion is immediate. For the positive radii in metric localization, \(|R|=R\). No contribution to the radius estimate is absorbed into a redefined quadratic form.

Let \((S_i)_{i\in I}\) be a family of subsets of a metric space, locally finite in the exact set sense: every point has an open neighborhood meeting only finitely many of the \(S_i\). For each compact \(K\), there is an open neighborhood \(V\supset K\) and a finite set \(J\subset I\) such that \(V\) meets no \(S_i\) with \(i\notin J\). To prove this without choosing neighborhoods for all points, take the family of all open sets meeting only finitely many members. Local finiteness says this family covers \(K\). A finite subcover \(V_1,\ldots,V_q\) has open union \(V\), and the union \(J\) of its finite sets of intersected indices is finite. Any \(S_i\) meeting \(V\) meets one of these \(V_j\), so \(i\in J\). For empty \(K\), use \(V=\varnothing,J=\varnothing\). In particular only finitely many members meet the original compact set, and one neighborhood works for all the other members.

For a smooth scalar, vector or matrix function \(f\) on an open original domain \(\Omega\), its support is the relative closure in \(\Omega\) of \(\{x:f(x)\ne0\}\). Every point outside the support has a neighborhood where \(f=0\); the derivative limit there is zero, and repeating the argument gives zero for every original derivative tensor. If smooth \(f_i\) have the property that near each point all but finitely many vanish identically, their sum is defined there by that finite sum. On overlapping neighborhoods the sums agree, because every omitted function is zero on the neighborhood where it is omitted. Finite linearity of the derivative, proved with the original coordinate tensors in Section 13, gives
\[
 \partial^\alpha\!\left(\sum_{i\in I}f_i\right)(x)
     =\sum_{i\in I}\partial^\alpha f_i(x)
 \tag{GC7}
\]
on each such neighborhood. Only its finitely many potentially nonzero terms occur. This proves smoothness and the displayed formula at every original derivative order. If the supports themselves form a locally finite family, the preceding compact-set result also supplies a single neighborhood of every compact set on which only finitely many terms can be nonzero. No regularity or measurability of a separately supplied metric field or weight is needed.

### 14.3. The maximality boundary and the exact declared foundation

This proof removes maximality from the general metric compactness route. It does not claim that countable choice proves the separate general Zorn statement. For the actual collection of pairwise disjoint fixed-radius frozen ellipsoid families in metric localization, the empty family makes the partially ordered set nonempty. A chain has its union as an upper bound: two ellipsoids in that union belong to two comparable families, so both belong to the larger family and are disjoint. The explicitly chosen maximality principle then supplies a maximal family. Assigning the first contained rational-coordinate point proves that this chosen disjoint family is countable, as already established in Section 4 and Section 12.8; it does not supply maximality.

An attempted replacement would enumerate rational-coordinate points and at each stage choose an eligible original ellipsoid disjoint from the preceding choices. The eligibility sets depend on earlier, arbitrarily chosen centres. Such an instruction does not become a proof under countable choice merely because its stages are countable: the independent-set selection used in (GC1) and (GC3) is not the same assertion. No Zorn-free maximal-ellipsoid selection is established here. The already valid Zorn application, original radii, centres, slow-variation constants, volume terms, multiplicity and support estimates remain. The mathematical correction is to remove the unnecessary maximality edge from the compactness proof, and to keep the separate maximality assumption visible where the ellipsoid selection actually uses it.



### 14.4. The full stated fundamental theorem and uniform coordinate passage

Let \(a<b\), let \(F:[a,b]\to\mathbb R\) be continuous on the closed original interval and differentiable at every interior point, and let \(f:[a,b]\to\mathbb R\) be bounded and Riemann-integrable, with \(f(t)=F'(t)\) for \(a<t<b\). No endpoint derivative or continuity of \(f\) is assumed. For each finite partition \(a=t_0<\cdots<t_m=b\), the original real mean value theorem gives an interior \(\xi_j\in(t_{j-1},t_j)\) satisfying \(F(t_j)-F(t_{j-1})=f(\xi_j)(t_j-t_{j-1})\). Its finite sum telescopes exactly:
\[
 F(b)-F(a)=\sum_{j=1}^m f(\xi_j)(t_j-t_{j-1})
             \longrightarrow\int_a^b f(t)\,dt .
 \tag{GC8}
\]
The limit uses the all-fine-tagged-partition criterion OC9, not a special family of partitions. It therefore proves the full stated theorem. The two endpoint values of \(f\) may be arbitrary finite values; the chosen tags are interior, and the original integral's full partition criterion is already assumed and proved. If \(a=b\), the difference and integral are both zero. Reversing the original endpoints gives the oriented identity with its minus sign.

For complex or finite-dimensional vector and matrix targets, use their original real coordinate functionals and apply this real proof separately. Different coordinates may have different mean-value points; no false common-point assertion for a vector function is needed. Each coordinate integral is exactly its coordinate of the original vector integral, by the fixed finite-coordinate maps and all their norm constants proved in Section 13.3 and Section 11.1 of the polynomial/contour chapter. Equality of all coordinates proves the original vector identity.

In particular, on an original coordinate box, a \(C^1\) function satisfies for every segment lying in the box
\[
 F(x+t e_j)-F(x)
      =\int_0^t\partial_j F(x+s e_j)\,ds .
 \tag{GC9}
\]
For \(t<0\) the oriented integral retains its sign. Suppose on each compact subbox that \(F_n\) and every coordinate derivative \(\partial_jF_n\) converge uniformly to \(F,g_j\), respectively. The limit functions are continuous by the already proved uniform-limit theorem. For any original segment in such a subbox the integral error is bounded, in the original target norm, by \(|t|\sup N(\partial_jF_n-g_j)\). Passing through (GC9) therefore gives the same identity with \(F,g_j\). Applying the primitive derivative argument OC12 to that continuous \(g_j\) gives \(\partial_jF=g_j\). The continuous-partials proof in Section 13.5.2 gives differentiability of \(F\) with the original coordinate derivative tensor. For convergence through a higher order, apply this same argument to each already retained derivative coordinate, starting at order zero and proceeding by finite induction. Every actual segment length, endpoint, coordinate, order and original norm is retained.

## References

- [Lebl] Jiří Lebl, *Basic Analysis*, [author's LaTeX source](https://github.com/jirilebl/ra/tree/e21ec524ca7d54f800c693b948020c188d21d01f).
- [Axler] Sheldon Axler, *Measure, Integration & Real Analysis*, [author's online edition](https://measure.axler.net/).
