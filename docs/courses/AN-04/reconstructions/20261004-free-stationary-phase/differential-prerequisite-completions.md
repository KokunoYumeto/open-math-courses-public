# Completing the algebra and differentiation inputs

Private prerequisite companion to the stationary-phase lesson. This is an
attributed adaptation and extension of Jiří Lebl, *Basic Analysis*, version
6.3, [freely accessible author edition](https://www.jirka.org/ra/), under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
The precise source sections are §§3.1.3, 4.1.1, 4.2.1–4.2.3 and 8.1–8.5.
Their complete programme proofs are retained through exact bindings in
`differential-proof-chain.json`. The arguments below supply particular
exercises, omitted cases and intermediate steps actually needed here.

We use the ordered complete real-field axioms and induction declared in
`elementary-proof-completions.md`, the definitions of real vector spaces,
linear maps, norms, derivatives and finite matrices, and the already closed
topology chain. Finite sums and products include the empty sum 0 and empty
product 1. The zero vector space has the empty basis, dimension 0 and its
unique linear map as its identity. Its operator norm is 0. Statements with
\(1/\|A^{-1}\|\) concern a space of positive dimension; inversion on
the zero space is a constant map and needs no such estimate.

## P9. Finite-dimensional algebra

### P9.1. The omitted linear-map checks

A nonempty subset closed under addition and scalar multiplication inherits
all vector-space identities from the ambient space. It contains zero because
\((0+0)x=0x+0x\) implies \(0x=0\) by cancellation, and it contains
\(-x=(-1)x\) because \((-1)x+x=(-1+1)x=0\).
This proves the subspace criterion used for spans, kernels and images.
The kernel of a linear map is closed under these operations because
\(A(ax+by)=aAx+bAy\); its image is closed because
\(aAx+bAy=A(ax+by)\).

For a linear map, \(A0=A(0+0)=A0+A0\), so cancellation gives
\(A0=0\). For scalars \(a,b,c\),
\[
 (A+B)(ax+by)=a(A+B)x+b(A+B)y,
 \qquad
 (cA)(ax+by)=a(cA)x+b(cA)y.
\]
Also \((BA)(ax+by)=B(aAx+bAy)=aBAx+bBAy\).
These identities fill the first four parts left as exercises in Proposition
8.1.16. The source already proves linearity of the inverse of a bijective
linear map.

For the extension in Proposition 8.1.17, let \(b_1,\ldots,b_n\) be a
basis and prescribe vectors \(v_1,\ldots,v_n\). Unique coordinates,
proved in Proposition 8.1.13, make
\(A(\sum_j x_jb_j)=\sum_j x_jv_j\) well defined. The coordinates
of \(ax+by\) are \(ax_j+by_j\); distributing the finite sum proves
\(A(ax+by)=aAx+bAy\). Thus the extension is linear, the check omitted
in the source proof.

If the target has a basis \(c_1,\ldots,c_m\), define \(E_{ij}\) by
\(E_{ij}b_k=0\) for \(k\ne j\) and \(E_{ij}b_j=c_i\).
Write \(Ab_j=\sum_i a_{ij}c_i\). The preceding uniqueness gives
\(A=\sum_{i,j}a_{ij}E_{ij}\). If that sum is zero, apply it to each
\(b_j\); independence of the \(c_i\)'s forces every \(a_{ij}=0\).
Hence the \(E_{ij}\)'s form a basis and \(\dim L(X,Y)=mn\), including
the empty-basis cases. This proves the exercise in Proposition 8.1.19.

The dependency-solving line before Proposition 8.1.13 contains a denominator
typo. If \(\sum_{j=1}^m a_jx_j=0\) and \(a_k\ne0\), the correct
identity is
\[
 x_k=-\sum_{j\ne k}\frac{a_j}{a_k}x_j.\tag{P9.1}
\]
In particular the denominator of its last term is \(a_k\). Subtracting
the other terms and dividing by \(a_k\) proves the displayed identity.
The complete exchange and basis-extension proofs of Proposition 8.1.14
are retained. If an independent list is empty, its size is 0 and the
dimension inequality is immediate; the exchange argument applies to
nonempty lists. \(\square\)

### P9.2. Norm metrics, convex balls and one-dimensional operators

For a norm \(N\), \(d(x,y)=N(x-y)\) is nonnegative, vanishes exactly
when \(x=y\), is symmetric because \(N(-u)=N(u)\), and satisfies
\(N(x-z)\leq N(x-y)+N(y-z)\). This proves the metric exercise after
Definition 8.2.1. Applying the triangle inequality in both orders also gives
\[
 |N(x)-N(y)|\leq N(x-y).\tag{P9.2}
\]
If \(x,y\) lie in the open ball of radius \(r>0\) about \(p\), then
for \(0<t<1\),
\[
 N((1-t)x+ty-p)\leq(1-t)N(x-p)+tN(y-p)<r.
\]
At \(t=0,1\) membership is already assumed. Replacing strict inequalities
by weak ones proves convexity of a closed ball, also at radius 0. This fills
Proposition 8.1.20.

For \(v\in\mathbb R^m\), the map \(A:\mathbb R\to\mathbb R^m\),
\(At=tv\), has norm \(|v|\): for \(|t|=1\), \(|At|=|v|\), and
for every \(t\), \(|At|=|t||v|\). This is the instance of Exercise
8.2.6 used by the vector mean-value proof. \(\square\)

For the operator norm itself, normalizing each nonzero \(x\) gives
\(\|Ax\|\leq\|A\|\|x\|\); at zero this follows from \(A0=0\).
If \(\|A\|=0\), this bound forces \(Ax=0\) for every \(x\), so
\(A=0\). Conversely the zero map has norm 0. These are the positivity
steps stated without expansion before Proposition 8.2.4. Its continuity
conclusion follows from the same bound and linearity:
\(\|Ax-Ay\|\leq\|A\|\|x-y\|\). For \(\|A\|>0\), an input
distance less than \(\varepsilon/\|A\|\) gives output distance less
than \(\varepsilon\); when \(\|A\|=0\), the output difference is
always zero. Finite operator norms are supplied by P9.3. \(\square\)

### P9.3. The general norm case in boundedness of linear maps

Proposition 8.2.4 proves the Euclidean-domain case and leaves the general
finite-dimensional normed domain as an exercise. Let \(X\) have dimension
\(n>0\), norm \(N\), and basis \(b_1,\ldots,b_n\). Put
\(Bc=\sum_j c_jb_j\) and \(C=\sum_jN(b_j)>0\). Since
\(|c_j|\leq|c|\), the norm axioms give
\[
 N(Bc)\leq C|c|,
 \qquad |N(Bc)-N(Bd)|\leq C|c-d|.\tag{P9.3}
\]
Thus \(c\mapsto N(Bc)\) is continuous in Euclidean coordinates. On
the unit sphere it is everywhere positive, since basis independence implies
\(Bc\ne0\) there. The sphere is closed by the reverse triangle
inequality and bounded, hence compact by the established F0-COMP contract.
The extreme-value theorem supplies an attained minimum \(m>0\). Scaling
each nonzero \(c\) to \(c/|c|\), and checking \(c=0\) separately,
gives
\[
 m|c|\leq N(Bc)\leq C|c|.\tag{P9.4}
\]
This proves norm equivalence rather than presupposing it.

For a linear map \(A:X\to Y\), with any normed target \(Y\),
\[
 \|A(Bc)\|\leq\sum_j|c_j|\|Ab_j\|
 \leq\frac{\sum_j\|Ab_j\|}{m}N(Bc).
\]
Every \(x\in X\) has the form \(Bc\), so this is the asserted finite
operator bound. If \(X=\{0\}\), \(A0=0\) and the bound holds with
constant 0. No dimension or completeness condition on \(Y\) is needed.
\(\square\)

### P9.4. Orthonormal complements in the spectral proof

This completes the induction step in Q5 using the source's basis-extension
theorem and Euclidean inner product. Given a unit vector \(e_1=v\),
extend it to a basis \(b_1=v,b_2,\ldots,b_n\) by Proposition 8.1.14.
Recursively set
\[
 u_j=b_j-\sum_{i<j}(b_j\mathbin{\cdot}e_i)e_i,
 \qquad e_j=u_j/|u_j|.\tag{P9.5}
\]
Suppose the preceding \(e_i\)'s are orthonormal and span
\(b_1,\ldots,b_{j-1}\). Taking the inner product of \(u_j\) with
\(e_k\), \(k<j\), gives
\(b_j\cdot e_k-b_j\cdot e_k=0\). Also \(u_j\ne0\), since otherwise
\(b_j\) would belong to the span of the preceding basis vectors. Its norm
is positive by the Euclidean norm properties and the positive-root proof P8.
Thus \(e_j\) is a unit vector perpendicular to its predecessors.
The formula for \(u_j\) proves that the first \(j\) new vectors and the
first \(j\) old vectors have the same span. This proves every induction
assertion. The resulting list is an orthonormal basis.

Taking the inner product with each \(e_j\) identifies the coordinates in
this basis as \(x\cdot e_j\). Consequently \(v^\perp\) has the basis
\(e_2,\ldots,e_n\): a vector
\(x=\sum_j(x\cdot e_j)e_j\) is perpendicular to \(v=e_1\) precisely
when its first coefficient vanishes. If a symmetric matrix \(H\) leaves
\(v^\perp\) invariant, its matrix there has entries
\(e_i\cdot He_j=e_j\cdot He_i\). It is therefore a real symmetric
\((n-1)\)-by-\((n-1)\) matrix, to which Q5's induction hypothesis
applies. The base cases are the empty basis for \(n=0\) and a single unit
vector for \(n=1\). This supplies the previously implicit choice of
coordinates on the complement. \(\square\)

### P9.5. The dimension argument in signature invariance

If a linear map \(A:V\to W\) is injective, the images of any independent
list in \(V\) are independent: a relation among the images gives a vector
in \(\ker A\), which is zero, and independence then sets each coefficient
to zero. Proposition 8.1.14 now gives \(\dim V\leq\dim W\) for
finite-dimensional spaces. Consequently, when \(\dim V>\dim W\),
the kernel is nonzero. A bijection preserves dimension by applying this
inequality to it and its inverse. These facts justify both the projection
kernel and preservation-of-dimension steps in P5. \(\square\)

## P10. Differentiation without unproved exercise inputs

### P10.1. Limit operations and the omitted function-limit corollaries

These estimates fill Corollaries 3.1.10–3.1.13 and also apply when the
variable approaches a point in a metric domain. Limits are taken along
the stated domain with the limiting point removed. If \(f\to a\) and
\(g\to b\), then eventually \(|f|\leq|a|+1\), and
\[
 |(f\pm g)-(a\pm b)|\leq|f-a|+|g-b|,
 \qquad
 |fg-ab|\leq|f|\,|g-b|+|b|\,|f-a|.\tag{P10.1}
\]
Given \(\varepsilon>0\), make each error on the right smaller than
\(\varepsilon/(2(1+|a|+|b|))\), and also make \(|f-a|<1\).
The displayed bounds prove both sum/difference limits and the product limit.
If \(b\ne0\), eventually \(|g-b|<|b|/2\), so \(|g|>|b|/2\), and
\[
 \left|\frac1g-\frac1b\right|
 \leq\frac{2|g-b|}{|b|^2}.
\]
This proves the reciprocal limit on that neighbourhood, and multiplying
proves the quotient limit. Also \(||f|-|a||\leq|f-a|\).

For completeness, if \(f\geq c\) throughout a punctured neighbourhood
and \(a<c\), convergence with error less than \((c-a)/2\) would give
\(f<(a+c)/2<c\), a contradiction. Hence \(a\geq c\); negating the
functions proves the upper-bound case. Applying these facts to a difference
gives preservation of order. If \(f\leq g\leq h\) and both outside
limits equal \(a\), eventually \(a-\varepsilon<f\leq g\leq h<
a+\varepsilon\), proving the squeeze conclusion. Constants have their
stated limits because their errors are zero. These proofs require the
point to be a cluster point when a nonvacuous order assertion is made.

For vector-valued functions, \(|x_j|\leq|x|\) and
\(|x|\leq\sqrt m\max_j|x_j|\) show directly that convergence in
\(\mathbb R^m\) is equivalent to convergence of every coordinate. A
bounded scalar or vector factor times a scalar tending to zero tends to
zero by the inequality \(|uv|\leq M|v|\). Finite products of matrix
entries are therefore continuous wherever their scalar factors are.
The source's complete sequential-limit proof, Lemma 3.1.7, remains the
bridge used by the scalar Fermat argument. The needed sequences there
can be chosen explicitly as \(c\pm r/(n+1)\), with
\(0<r<\min(c-a,b-c,\delta)\); P6.0 proves their convergence.
\(\square\)

### P10.2. The product rule omitted in the scalar source

Let \(f,g\) be real-valued and differentiable at \(p\) in an open
subset of \(\mathbb R^n\). Write
\[
 f(p+h)=f(p)+Ah+r(h),\qquad
 g(p+h)=g(p)+Bh+s(h),
\]
where \(A=Df(p)\), \(B=Dg(p)\), and
\(|r(h)|/|h|,|s(h)|/|h|\to0\). Expanding and subtracting the proposed
linear term leaves
\[
 f(p)s(h)+g(p)r(h)+(Ah+r(h))(Bh+s(h)).\tag{P10.2}
\]
After division by \(|h|\), the first two terms tend to zero. For small
nonzero \(h\), \(|r(h)|\leq|h|\) and \(|s(h)|\leq|h|\), so the
absolute value of the last term divided by \(|h|\) is bounded by
\((\|A\|+1)(\|B\|+1)|h|\), which also tends to zero. Therefore
\[
 D(fg)(p)=f(p)Dg(p)+g(p)Df(p).\tag{P10.3}
\]
This includes the one-variable exercise, Proposition 4.1.8. Finite sums
of component products give the corresponding product rules for scalar
multiplication of vectors, dot products and matrix multiplication. Their
linearity and boundedness are supplied by P9 and the source norm estimates.
The sum, scalar-multiple and chain rules already have complete proofs in
§8.3.1 and are retained.

For a real \(u\ne0\), direct subtraction gives
\[
 \frac{(u+h)^{-1}-u^{-1}}h=-\frac1{u(u+h)}\longrightarrow-u^{-2}.
\]
P10.1 proves the indicated limit and continuity of this derivative.
The chain and product rules now give
\(D(f/g)=(gDf-fDg)/g^2\) wherever \(g\ne0\), completing Proposition
4.1.9. The region where \(g\ne0\) is open when \(g\) is continuous:
near \(p\) use \(|g(x)-g(p)|<|g(p)|/2\).

In the scalar-multiple proof of Proposition 8.3.6, the printed numerator
has an extra closing parenthesis after \(f(p+h)\). The intended
remainder is \(a(f(p+h)-f(p)-Df(p)h)\); its norm divided by \(|h|\)
is \(|a|\) times the original remainder ratio, proving the assertion
also for \(a=0\). \(\square\)

### P10.3. The base case in continuous partial derivatives

The reverse implication of Proposition 8.4.6 leaves its
\(n=1\), vector-valued base case to the reader. Suppose every component
\(f_j\) has derivative at \(p\), and let
\(Ah=h(f_1'(p),\ldots,f_m'(p))\). For \(h\ne0\),
\[
 \frac{|f(p+h)-f(p)-Ah|}{|h|}
 \leq\sqrt m\max_j
 \left|\frac{f_j(p+h)-f_j(p)}h-f_j'(p)\right|\longrightarrow0.
\]
The last limit follows by choosing the minimum of the finitely many
component thresholds. This proves differentiability. If all the component
derivatives are continuous, the operator-norm identity in P9.2 proves
continuity of \(Df\). The empty target \(m=0\) is constant and immediate.

For the higher-dimensional induction already written in the source, fix a
ball \(B(p,r)\subset U\), and take \(|h|<r\). Writing
\(h=h'+te_n\), each intermediate point
\(p+h'+\theta te_n\), \(0\leq\theta\leq1\), has distance at most
\(|h|\) from \(p\), so all the component mean-value applications stay
in \(U\). If \(h'=0\), the induction remainder is zero; if \(t=0\),
the last-coordinate remainder is zero. Otherwise the source estimates apply
and their sum is bounded by \((1+\sqrt m)\varepsilon|h|\). As
\(\varepsilon\) is arbitrary, this is precisely the required vanishing
remainder ratio. This clarifies the domain and zero-increment cases without
replacing the complete induction argument. \(\square\)

### P10.4. The zero case in the vector mean-value estimate

In Lemma 8.4.1, if \(f(b)=f(a)\), the asserted inequality has left
side 0 and holds at every interior point, for example \((a+b)/2\).
Otherwise the source proof applies the scalar mean-value theorem to
\((f(b)-f(a))\cdot f(t)\), uses Cauchy–Schwarz and cancels the
strictly positive \(|f(b)-f(a)|\). P9.2 identifies the derivative's
operator norm with its vector length. In Proposition 8.4.2, the case
\(p=q\) likewise gives \(0\leq0\); for distinct points the written
line-segment argument and chain rule apply. These cover the cases suppressed
by the divisions in those proofs. \(\square\)

### P10.5. Higher regularity used by matrix and implicit inversion

Use the recursive definition: \(C^0\) means continuous, and \(f\in C^{k+1}\)
means that \(f\) is differentiable and its derivative, represented by its
finite matrix of components, is \(C^k\). Proposition 8.2.7 supplies the
equivalence between matrix-coordinate and operator-norm continuity.

We prove simultaneously by induction on \(k\) that finite sums, products
and compositions of \(C^k\) maps are \(C^k\), with products taken
componentwise or by matrix multiplication whenever defined. For \(k=0\),
P10.1 proves sum and product continuity. Continuity of a composition follows
directly: for a given output error choose an input neighbourhood for the
outer map, then use continuity of the inner map to stay in it.
For \(k\geq1\), the already proved first-derivative rules give derivatives
of sums by summing, of products by P10.3, and of a composition by
\[
 D(g\circ f)=(Dg\circ f)Df.
\]
All factors on the right are \(C^{k-1}\) by the induction hypothesis
and the definition of \(C^k\). The same hypothesis makes their finite
products and sums \(C^{k-1}\), proving the step. Here \(C^k\) implies
\(C^{k-1}\) recursively: differentiability gives continuity by Proposition
8.3.5, and apply the preceding implication to the derivative at each lower
order. Thus no higher-order chain rule is being assumed in this induction.

The reciprocal \(r(u)=1/u\) is \(C^1\) on \(u\ne0\) by P10.2.
If it is \(C^k\), its derivative \(-r(u)^2\) is \(C^k\) by the
product result, so it is \(C^{k+1}\). It is therefore smooth.
Coordinate functions and constants have constant derivatives, hence are
smooth by the recursive definition. Finite products show that every
polynomial is smooth. The adjugate formula in P2 consequently proves smooth
matrix inversion on \(\det A\ne0\), with no appeal to the inverse
function theorem. P8's derivative \(1/(2\sqrt u)\), together with the
same induction, proves smoothness of the positive square root independently
of that theorem.

These facts supply precisely the higher-regularity step in P3 after the
existing complete \(C^1\) inverse and implicit proofs, Theorems 8.5.1
and 8.5.6, have been bound. They apply to every finite \(r\geq1\) and
to \(r=\infty\). No integration, change-of-variables, mixed-partial or
Taylor theorem has been assumed or established by this regularity induction.
\(\square\)

### P10.6. The product-neighbourhood restriction in implicit inversion

In the proof of Theorem 8.5.6, let \(G:V\to O\) denote the inverse
just constructed, where \(V\) is open about \((p,0)\), \(O=G(V)\)
is open about \((p,q)\), and \(F(x,y)=(x,f(x,y))\). Before evaluating
\(G_2(x,0)\), we must ensure that \((x,0)\in V\). Choose an open
ball \(B(p,\rho)\) with \(B(p,\rho)\times\{0\}\subset V\).
Choose open balls \(\widetilde W\) about \(p\) and \(W'\) about
\(q\) whose product lies in \(O\), and shrink \(\widetilde W\) to
its intersection with \(B(p,\rho)\). Such product balls exist: a ball
of radius \(r\) about \((p,q)\) in \(O\) contains the product of the
two balls of radius \(r/2\), since
\(\sqrt{|x-p|^2+|y-q|^2}<r/\sqrt2<r\).

Now \(G_2(x,0)\) is defined for every \(x\in\widetilde W\), and
\[
 W=\{x\in\widetilde W:G_2(x,0)\in W'\}
\]
is an open neighbourhood of \(p\). To verify openness directly, for each
\(x\in W\), choose a ball about \(G_2(x,0)\) contained in \(W'\).
Continuity of \(G_2(\,\cdot\,,0)\) gives a neighbourhood of \(x\)
mapping into that ball; intersect it with the open \(\widetilde W\).
Also \(G_2(p,0)=q\), so \(p\in W\). The graph map
\(g(x)=G_2(x,0)\) is \(C^1\), being the composition of \(G\) with
the linear inclusion and projection.

If \(x\in W\), \(y\in W'\), and \(f(x,y)=0\), then
\((x,y)\in O\) and \(F(x,y)=(x,0)\). Applying the inverse gives
\((x,y)=G(x,0)\), hence \(y=g(x)\). This proves the stated uniqueness
on the entire product \(W\times W'\). The derivative formula is the
chain-rule calculation already written in the source. The additional slice
restriction above resolves an implicit domain choice in that proof; it
does not change the theorem's local generality. \(\square\)

The inverse theorem in dimension 0 requires no contraction estimate:
the only nonempty open set is the singleton \(\mathbb R^0\), its only
self-map is its own inverse, and every derivative is the unique zero-space
linear map. It is smooth by the recursive definition. In the implicit
theorem with zero target dimension, the unknown block lies in
\(\mathbb R^0\) and the unique solution map is the constant empty
tuple. These observations cover the cases excluded by positive-dimensional
operator-norm denominators. \(\square\)

## Scope of the completion

The exact dependency graph distinguishes these algebra/differentiation arguments from the later compact-integral and Taylor completions in `integration-proof-chain.json`. Global integration, exponential and multidimensional change-of-variables inputs, the assembled stationary-phase lesson and its complete distribution payload still require review.
