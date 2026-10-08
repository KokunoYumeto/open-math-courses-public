# Notation for the selected prerequisite proofs

These definitions make the selected proofs from Jiří Lebl's *Basic Analysis
I–II*, version 6.3, readable together. They use the same conventions as the
[free author edition](https://www.jirka.org/ra/). The accompanying programme
proof map identifies the complete proofs and the local completions of used
exercises. A definition here does not assert a theorem about the object defined.

## Ordered numbers, sequences and series

We use the ordered real field with the least-upper-bound axiom and natural-number
induction. An upper bound for a set \(A\subset\mathbb R\) is a number at least
every member of \(A\); \(\sup A\) is its least upper bound when it exists.
Lower bounds and \(\inf A\) are defined with the order reversed. The real-field
axiom guarantees \(\sup A\) for every nonempty bounded-above set. We set
\(\inf A=-\sup(-A)\) when the right side is defined.
The empty finite sum is zero and the empty finite product is one.

A sequence \(x_n\) converges to \(x\) if, for each \(\varepsilon>0\), there is
\(N\) such that \(|x_n-x|<\varepsilon\) for all \(n\geq N\).
It is bounded when \(|x_n|\leq M\) for some \(M\); increasing means
\(x_n\leq x_{n+1}\), and decreasing means the reverse inequality.
A subsequence is \(x_{n_j}\) with strictly increasing natural indices \(n_j\).
A tail discards finitely many initial terms. A real Cauchy sequence satisfies
\(|x_n-x_m|<\varepsilon\) for all sufficiently large \(n,m\).
For bounded real sequences the tail suprema and infima are
\(a_n=\sup_{k\geq n}x_k\), \(b_n=\inf_{k\geq n}x_k\); their limits, when
they exist, are \(\limsup x_n\) and \(\liminf x_n\).

A series is the limit of its finite partial sums when that limit exists.
Absolute convergence means convergence of the series of absolute values.
For nonnegative terms we also allow the value \(+\infty\), defined as the
supremum of finite partial sums. Complex numbers are pairs of reals with
\(i^2=-1\); \(\overline{x+iy}=x-iy\) and \(|x+iy|=\sqrt{x^2+y^2}\).
The complex arithmetic and series operations used in the selected proofs
are justified in the exponential companion.

## Metric spaces and their topology

A metric \(d\) on \(X\) is nonnegative, symmetric, zero exactly for equal
points, and satisfies the triangle inequality. The subspace metric is the
restriction to a subset. We write
\(B(x,r)=\{y:d(x,y)<r\}\) and \(C(x,r)=\{y:d(x,y)\leq r\}\).
A subset is bounded if it lies in some ball of finite radius.
In \(\mathbb R^n\) the Euclidean scalar product is
\(x\cdot y=\sum_jx_jy_j\), the norm is \(|x|=\sqrt{x\cdot x}\),
and the distance is \(|x-y|\).

A set is open if each of its points has a ball inside it, and closed if its
complement is open. The interior consists of the points with such a ball.
The closure is the intersection of the closed sets containing the set.
The boundary is the closure minus the interior. A neighborhood of a point
contains an open set containing that point. Relative openness uses the
subspace metric. A nonempty space is connected if its only subsets that are
both open and closed are itself and the empty set.

Metric convergence means \(d(x_n,p)\to0\). The metric Cauchy condition uses
\(d(x_n,x_m)<\varepsilon\) eventually for all \(n,m\). A metric space is
complete if every Cauchy sequence converges in it. A set is compact if every
cover by open sets has a finite subcover.

Continuity of \(f:X\to Y\) at \(p\) means that for each \(\varepsilon>0\)
there is \(\delta>0\) such that \(d_X(x,p)<\delta\) implies
\(d_Y(f(x),f(p))<\varepsilon\). Uniform continuity uses one \(\delta\) for
all pairs of points. A cluster point of \(S\) has another point of \(S\)
in every ball about it. A function limit uses the same inequality on
\(S\setminus\{p\}\). Restrictions are denoted \(f|_S\); one-sided limits
restrict the domain to the corresponding half-line. A \(k\)-Lipschitz map
satisfies \(d_Y(f(x),f(y))\leq k\,d_X(x,y)\).
A contraction has such a constant with \(0\leq k<1\).
A fixed point satisfies \(f(x)=x\).

## Linear algebra and differentiation

A real vector space has associative commutative addition, zero and additive
inverses, and scalar multiplication satisfying the distributive, associative
and unit axioms. Linear combinations are finite sums of scalar multiples.
The span of a set consists of its finite linear combinations.
A finite list is linearly independent if a linear combination equal to zero
has all coefficients zero. A basis is an independent spanning list.
The dimension is the size of a basis; the selected basis theorems justify
that this does not depend on the basis.

A linear map preserves addition and scalar multiplication.
\(L(X,Y)\) denotes the vector space of such maps;
\(\ker A=\{x:Ax=0\}\), and \(\operatorname{ran}A=\{Ax:x\in X\}\).
An invertible map is bijective. \(GL(X)\) is the set of invertible linear
maps \(X\to X\). Once bases are fixed, the \(j\)-th matrix column is the
coordinate vector of the image of the \(j\)-th basis vector.
The identity matrix is \(I\), and the transpose is \(A^T\).

A norm is nonnegative, zero only at zero, absolutely homogeneous, and
subadditive. For a linear map its operator norm is
\(\|A\|=\sup_{\|x\|=1}\|Ax\|\), interpreted with the zero-space convention
in the local differential companion. In the source, \(\|\cdot\|\) may
denote either a vector norm or its induced operator norm.
The determinant is the alternating permutation sum
\(\det A=\sum_\sigma\operatorname{sgn}(\sigma)\prod_i a_{i,\sigma(i)}\).
The parity and all determinant identities used are proved in the selected
proofs and P7. A set is convex if it contains every segment joining its points.

For an open set \(U\subset\mathbb R^n\), a map \(f:U\to\mathbb R^m\) is
differentiable at \(x\) if there is a linear map \(A\) such that
\(|f(x+h)-f(x)-Ah|/|h|\to0\) as \(h\to0\), \(h\neq0\).
We write \(f'(x)=Df(x)=A\). A partial derivative takes this limit in one
coordinate direction; the Jacobian matrix has those partials as its columns.
The Jacobian determinant of a square map is \(\det f'(x)\).
A map is \(C^1\) when its derivative is continuous; \(C^k\) and smooth mean
successive continuous differentiability through order \(k\) and every finite
order, respectively. One-variable derivatives at an interval endpoint are
one-sided when specified. A local maximum or minimum compares the value
with values in a neighborhood in the domain.

## Riemann integrals, null sets and substitution

For \(a<b\), a partition is \(a=x_0<\cdots<x_q=b\).
For bounded real \(f\), put \(m_j=\inf_{[x_{j-1},x_j]}f\),
\(M_j=\sup_{[x_{j-1},x_j]}f\). The lower and upper Darboux sums are
\(\sum_jm_j(x_j-x_{j-1})\) and \(\sum_jM_j(x_j-x_{j-1})\).
The lower integral is the supremum of lower sums; the upper integral is the
infimum of upper sums. Equality defines Riemann integrability and the integral.
The notation \(\mathscr R(S)\) means the Riemann-integrable functions on \(S\).
A refinement adds partition points. A zero-length interval has integral zero;
reversal changes the sign. Complex and finite-vector integrals are defined
componentwise, with their norm inequalities proved in the local companions.

A rectangle in \(\mathbb R^n\) is a Cartesian product of intervals. Its volume
is the product of their lengths. A rectangle partition is a product of
one-dimensional partitions; a subrectangle uses consecutive partition points.
Darboux sums multiply each subrectangle's infimum or supremum by its volume.
Their upper and lower integrals and the integrability definition are as above.
The indicator \(\chi_S\) is one on \(S\) and zero elsewhere.

The outer measure \(m^*(S)\) is the infimum of the sums of volumes of
countable open-rectangle covers of \(S\). The value \(+\infty\) is allowed.
A null set has outer measure zero: equivalently, for every \(\varepsilon>0\)
there is such a cover with total volume below \(\varepsilon\), directly by the
infimum definition. A bounded set is Jordan measurable when its indicator
on a containing rectangle is Riemann integrable. Its Jordan volume is that
integral. For a bounded function on a Jordan set, extend it by zero to a
containing rectangle; integrability and the integral use this extension.
The selected proofs establish independence of the containing rectangle and
the other used properties.

For bounded real \(f\) on a domain, its oscillation at \(x\) is
\[
o(f,x)=\inf_{\delta>0}\left(
\sup_{y\in B(x,\delta)\cap\operatorname{dom}f}f(y)
-\inf_{y\in B(x,\delta)\cap\operatorname{dom}f}f(y)\right).
\]
Equivalently the infimum is the decreasing-radius limit by the monotone-limit
proofs. Improper one-dimensional integrals take limits at excluded endpoints
or infinity of the compact integrals. The multivariable absolute integrals,
tails and product-majorant interchanges used by the stationary-phase lesson
are defined and proved in P17–P18, rather than by an unspecified general
integration theorem.

## Exponentials and trigonometric notation

The source writes \(L(x)=\int_1^x dt/t\) for \(x>0\). Its proved inverse
is \(E\); these functions are \(\log\) and the real exponential.
For complex \(z\), the exponential is the convergent series
\(\exp z=\sum_{j=0}^{\infty}z^j/j!\).
Define \(\cos z=(e^{iz}+e^{-iz})/2\) and
\(\sin z=(e^{iz}-e^{-iz})/(2i)\).
The selected source proofs together with P13–P16 establish the series
operations, derivatives, real period \(2\pi\) and all root choices used here.
No analytic-continuation theorem is assumed.

*Definitions arranged by GPT-6 Astra (OpenAI), Ultra, 4 October 2026, following the selected freely accessible Lebl programme edition and its local completions. Original text: public domain (CC0). The Lebl sections it links keep Jiří Lebl's authorship and licence.*

