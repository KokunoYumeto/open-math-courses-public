# Completing the change-of-variables prerequisites

Prerequisite companion to the stationary-phase lesson. The human source
is Jiří Lebl, *Basic Analysis* 6.3 (15 May 2026), freely accessible in the
[author edition](https://www.jirka.org/ra/):
[§10.3](https://www.jirka.org/ra/html/sec_outermeasure.html),
[§10.4](https://www.jirka.org/ra/html/sec_riemannlebesgue.html),
[§10.5](https://www.jirka.org/ra/html/sec_jordansets.html), and
[§10.7](https://www.jirka.org/ra/html/sec_mvchangeofvars.html).
Their complete proofs remain in the exact earlier programme files identified
in `change-of-variables-proof-chain.json`. This companion completes used
exercises and makes domain restrictions explicit; it does not replace those
correct proofs with external citations. Original text: public domain (CC0).

The compact and absolute-improper integrals are those constructed in P17–P18.
All sets below lie in a fixed finite-dimensional Euclidean space. Unless stated
otherwise \(n\geq1\). In dimension zero the space is a singleton, integration
is evaluation, the empty determinant is 1, and an injective coordinate change
is the identity; all required substitution statements then follow directly.

## P19. Outer measure and images of null sets

### P19.1. Covering definitions and countable sums

Use Definition 10.3.1: \(m^*(E)\) is the infimum of the sums of volumes
of countable open rectangle covers of \(E\). A nonnegative series is the
supremum of its finite partial sums. For a countable array of nonnegative
numbers, its sum is the supremum over finite sets of indices. This agrees
with an enumeration: every finite set occurs in some initial segment and
every initial segment is finite. It also agrees with repeated summation.
Indeed each finite sum is bounded by the repeated sum, while a finite sum
of row sums is the supremum of finite sums from those finitely many rows.
Taking the supremum over the rows proves the reverse inequality. The pairs
of positive integers can be enumerated by increasing sum of their coordinates,
then by the first coordinate within each finite diagonal. Thus this argument
supplies the nonnegative-series exercise used in Proposition 10.3.4 without
assuming an interchange theorem for integrals.

If \(A\subset B\), every cover of \(B\) covers \(A\), so
\(m^*(A)\leq m^*(B)\). Allowing finite covers leaves the infimum unchanged:
append open cubes of total volume less than any prescribed \(\varepsilon>0\)
to a finite cover. Such cubes exist by choosing a side length with \(n\)th
power below \(\varepsilon2^{-j}\); the positive power and root rules were
proved in P8/P14.2. The empty set consequently has outer measure zero.
The definition can use an empty finite cover for it.

For finitely or countably many sets \(E_j\),
\[
 m^*\Bigl(\bigcup_jE_j\Bigr)\leq\sum_jm^*(E_j).       \tag{P19.1}
\]
If the right side is infinite the inequality is automatic. Otherwise choose
an open rectangle cover of \(E_j\) with sum at most
\(m^*(E_j)+\varepsilon2^{-j}\), combine the covers, use the just-proved
nonnegative summation rule and let \(\varepsilon\downarrow0\).
This completes the monotonicity, finite-cover and subadditivity exercises and
the sum step in the existing proof of Proposition 10.3.4. In particular a
countable union of null sets is null. If \(N\) is null, monotonicity and
(P19.1) give \(m^*(A\cup N)=m^*(A)\). \(\square\)

### P19.2. Rectangle measure and finite disjoint rectangles

A closed bounded rectangle \(R=\prod_i[a_i,b_i]\) satisfies
\(m^*(R)=\prod_i(b_i-a_i)=V(R)\). For the upper bound, expand every
side by \(\delta>0\); the product of the expanded side lengths tends to
\(V(R)\). For the lower bound, any countable open rectangle cover of \(R\)
has a finite subcover by P1. Introduce all its endpoints and the endpoints of
\(R\) into one finite grid in a containing rectangle. For every positive-volume
grid cell inside \(R\), an interior point belongs to some cover rectangle.
No endpoint of that rectangle lies inside the grid cell, so the whole cell
interior belongs to it. Assign the cell to one such rectangle. The sum of
the volumes assigned to one rectangle is at most its volume, by the grid
volume identity P17.1. Summing gives \(V(R)\leq\sum_jV(O_j)\).
Zero-side rectangles have volume zero and require only the upper bound.

For an open bounded rectangle \(O\), inward closed rectangles give
\(m^*(O)\geq V(O)\) by monotonicity and limits of the side products;
outward rectangles give the reverse inequality. For finitely many pairwise
disjoint open rectangles \(O_1,\ldots,O_k\), shrink them to closed
rectangles \(K_j\subset O_j\). Any open cover of their compact union has
a finite subcover. Apply the same grid assignment argument to the cells of
all the \(K_j\), which have disjoint interiors, to obtain a lower bound
\(\sum_jV(K_j)\) on the covering sum. Let the shrinkages tend to zero.
Subadditivity gives the opposite bound, hence
\[
 m^*\Bigl(\bigcup_{j=1}^kO_j\Bigr)=\sum_{j=1}^kV(O_j).
\]
This supplies Exercises 10.3.4 and 10.3.16 used by the existing proof of
Proposition 10.5.3. Empty finite families have both sides zero. \(\square\)

### P19.3. Small balls, compact null covers and coordinate faces

Retain Proposition 10.3.2 and its full cube-to-ball proof. Its cube side is
chosen smaller than both the smallest rectangle side and
\(\delta/(2\sqrt n)\); thus the resulting balls have the prescribed small
radii. The finite subdivisions used there are supplied by P17.1 and the
Archimedean property P6.0. The countable regrouping of their volume sums
is justified by P19.1. This uses no formula for the volume of a ball.

For the omitted ball half of Proposition 10.3.7, start with those open balls
of radii \(r_j<\delta\) and \(\sum_jr_j^n<\varepsilon\). Compactness
selects a finite subcover; discarding the other nonnegative terms preserves
the bound. This is exactly the proof already supplied there for rectangles.

A coordinate hyperplane is null. Intersect it with each box
\([-k,k]^n\); the intersection is contained in a slab with one side \(2t\)
and the other sides \(2(k+1)\). Its volume tends to zero as \(t\downarrow0\).
Take the countable union over positive integers \(k\), using P19.1.
Every rectangle boundary is contained in finitely many such hyperplanes and
is therefore null. This is the full argument of Example 10.3.5 with its
countable-union input now proved. \(\square\)

### P19.4. The full \(C^1\) null-image theorem

If \(U\subset\mathbb R^n\) is open, \(g:U\to\mathbb R^n\) is \(C^1\),
and \(E\subset U\) is null, then \(g(E)\) is null. This completes the
noncompact case left to Exercise 10.3.6; no nullity of \(\overline E\) is
assumed.

First let \(E\subset K\subset U\), with \(K\) compact, but do not assume
\(E\) closed. If \(K\) is empty there is nothing to prove. At each point
of \(K\) choose a ball whose concentric closed ball of twice the radius lies
in \(U\). Finitely many smaller balls cover \(K\). Their doubled closed
balls form a compact subset of \(U\), so continuity of \(g'\) bounds its
operator norm there by a finite number \(M\geq1\). There exists
\(\delta>0\) such that the entire \(\delta\)-neighbourhood of \(K\) lies
in their union: if smaller balls have radii \(r_1,\ldots,r_q\), choose
\(\delta<\min_jr_j\) and use the triangle inequality.

By Proposition 10.3.2 cover \(E\) by countably many open balls of radii
\(r_j<\delta/3\) and \(\sum_jr_j^n<\varepsilon\). Discard balls not
meeting \(E\). Every retained ball is inside that \(\delta\)-neighbourhood.
The vector mean-value estimate (the proved Proposition 8.4.2, including
P10.4) gives
\[
 |g(x)-g(c_j)|\leq M|x-c_j|<Mr_j
\]
for \(x\) in the ball centred at \(c_j\). Thus its image lies in the open
ball centred at \(g(c_j)\) of radius \(Mr_j\). The sum of these radii to
power \(n\) is below \(M^n\varepsilon\). Each is contained in an open
cube of side \(2Mr_j\), so \(m^*(g(E))\leq 2^nM^n\varepsilon\).
Let \(\varepsilon\downarrow0\). Choosing \(M\geq1\) also avoids the
zero-radius open-ball ambiguity in the wording of Lemma 10.3.9 when
\(g'=0\); the non-strict closed-ball estimate is valid even for \(M=0\).

For general \(E\), put
\[
 K_k=\{x\in\mathbb R^n:|x|\leq k,
          \ |x-y|\geq1/k\text{ for every }y\notin U\}.
\]
Each inequality defines a closed set by continuity of distance to a fixed
point. Their intersection with the closed ball is closed and bounded,
hence compact by P1; it lies in \(U\), since \(x\notin U\) could be
chosen as \(y\). If \(U=\mathbb R^n\), the condition on \(y\) is empty.
Every point of \(U\) belongs to some \(K_k\), because it has a ball inside
\(U\) and finite norm. The first part applies to the null set \(E\cap K_k\).
Now \(g(E)=\bigcup_kg(E\cap K_k)\) is null by P19.1. \(\square\)

## P20. Riemann integrability and Jordan domains

### P20.1. Completing the oscillation criterion's grid details

Retain the complete proofs of Propositions 10.4.1–10.4.2 and Theorem
10.4.3 in the exact earlier programme page. They prove that a bounded real
function on a closed rectangle is Riemann integrable exactly when its
discontinuities form a null set. The oscillation is relative to that rectangle.
The supremum/infimum operations are P12.1; the compactness and Darboux
criterion they use are P1 and Proposition 10.1.12, already proved.

Here are the finite-grid details in the sufficiency proof. Its finitely many
open bad-set rectangles \(O_\ell\), together with the interiors of the
good-set rectangles \(T_\ell\), cover the original rectangle. Insert all
their coordinate endpoints into the partition. An interior point of a
positive-volume grid cell belongs to one of those open rectangles. No
endpoint lies strictly inside a grid interval, so the closed cell is
contained in the closure of that covering rectangle. If the latter is a
good rectangle \(T_\ell\), its closed-cell oscillation is below the
chosen tolerance. Otherwise assign the cell to a bad \(O_\ell\).
P17.1 bounds the total volume of cells assigned to each \(O_\ell\) by
\(V(O_\ell)\). Thus the proof's upper-minus-lower sum is indeed bounded
by \(\varepsilon V(R)+2B\varepsilon\). An empty bad set or empty good
set simply omits the corresponding finite family.

In the necessity proof the union of grid faces is null by P19.3. The
interiors of those cells meeting \(\{o(f,x)\geq1/k\}\) have total volume
at most \(k(U(P,f)-L(P,f))\). Together with an arbitrarily small open
cover of the faces, these rectangles cover that oscillation level set.
Every positive oscillation exceeds \(1/k\) for some positive integer
\(k\), by P6.0, so P19.1 completes the countable union step. When the
original rectangle has a zero side, every bounded function has integral
zero by P17.1 and all its discontinuities lie in a null coordinate
hyperplane. This handles that case without using cell interiors.
\(\square\)

### P20.2. The omitted algebra, null-change and composition exercises

For bounded integrable real functions, linearity and product integrability
are P17.2. Absolute value is covered there as well, and
\[
 \max(f,g)=\tfrac12(f+g+|f-g|),\qquad
 \min(f,g)=\tfrac12(f+g-|f-g|).
\]
This proves the algebra and maximum/minimum parts of Corollary 10.4.4.
Finite-dimensional vector or complex statements follow componentwise;
their norm is continuous, and its oscillation on a cell is at most the
sum of the component oscillations, by the reverse triangle inequality.

Suppose \(h\) is Riemann integrable and zero outside a null set \(N\).
Every positive-volume grid cell has a point outside \(N\), since its outer
measure is its positive volume by P19.2. The lower sum of \(|h|\) is
therefore zero on every partition; zero-volume cells contribute zero.
As \(|h|\) is integrable, its integral is zero, hence \(\int h=0\) by
the norm bound. Consequently two integrable functions equal outside a null
set have the same integral. If two integrable real functions satisfy
\(f\leq g\) outside a null set, the integrable function
\((f-g)_+=\max(f-g,0)\) has integral zero; monotonicity applied to
\(f-g\leq(f-g)_+\) gives \(\int f\leq\int g\).

When a bounded function differs from an integrable function only on a
*closed* null set, it is itself integrable. Indeed outside that closed set
it agrees locally with the original function. Its discontinuity set is
contained in the original discontinuity set together with the closed
null set. Theorem 10.4.3 applies, and the preceding paragraph gives
equality of the integrals. This proves Exercises 10.4.1, 10.4.3–10.4.4
in the scope used here. Arbitrary changes on a nonclosed null set are not
asserted to preserve Riemann integrability.

For the composition part of Corollary 10.4.4, let
\(g:U\to U'\) be a \(C^1\) bijection with \(C^1\) inverse,
\(R\subset U\), \(R'\subset U'\) closed rectangles, \(g(R)\subset R'\),
and \(f\) Riemann integrable on \(R'\). It is bounded. If \(f\) is
continuous relative to \(R'\) at \(g(x)\), continuity of \(g|_R\)
implies continuity of \(f\circ g\) at \(x\), relative to \(R\).
Thus the discontinuity set of the composition is contained in
\(g^{-1}(D_f\cap U')\). The set \(D_f\) is null by Theorem 10.4.3.
Apply P19.4 to the map \(g^{-1}\), then apply Theorem 10.4.3 on \(R\).
This proves the used part of Exercise 10.4.8. \(\square\)

### P20.3. Jordan sets, boundaries and volume

Use the source definition: a bounded set \(S\) is Jordan measurable when
its indicator is Riemann integrable on a containing rectangle, and
\(V(S)=\int\chi_S\). Independence of the containing rectangle is exactly
P17.3. Retain the full proof of Proposition 10.5.1: inside a rectangle
whose interior contains \(\overline S\), the discontinuity set of
\(\chi_S\) is exactly \(\partial S\), so Theorem 10.4.3 applies.
This includes \(S=\varnothing\).

To complete Proposition 10.5.2, a point outside \(\partial S\) has a
neighbourhood wholly inside \(S\) or wholly outside \(\overline S\).
It follows that
\[
 \partial\overline S\subset\partial S,\qquad
 \partial(S^\circ)\subset\partial S.
\]
A point outside \(\partial S\cup\partial T\) has a neighbourhood on
which both membership indicators are constant. Their union, intersection
and difference indicators are therefore constant there. Their boundaries
are contained in \(\partial S\cup\partial T\), which is null by P19.1.
All these sets are bounded, so Proposition 10.5.1 proves their Jordan
measurability. The sets \(S^\circ,S,\overline S\) differ only on
\(\partial S\), and P20.2 gives equality of their volumes. A bounded
closed null set, and every subset of it, is Jordan measurable of volume
zero: the boundary of any such subset lies in the closed null set.

Retain the full proof of Proposition 10.5.3, \(V(S)=m^*(S)\).
Its lower-bound step now has the exact finite-disjoint-rectangle exercise
proved in P19.2. Its upper-bound step enlarges finitely many closed grid
rectangles by arbitrarily small amounts; continuity of their side products
gives the asserted volume error. If no cell meets \(S\), then \(S\)
is empty, and both quantities are zero without dividing by the number
of cells. Thus all cases in that proof are covered. \(\square\)

### P20.4. Integrals on Jordan sets and finite decompositions

For bounded \(f:S\to\mathbb C^q\) on a bounded Jordan set, use
Definition 10.5.4: extend \(f\) by zero to a containing rectangle and
integrate there if every component is Riemann integrable. P17.3 proves
independence of the rectangle. The full proof of Proposition 10.5.5 is
retained: for bounded continuous \(f\), discontinuities of the extension
can occur only on \(\partial S\), which is null.

Linearity, products of scalar functions, real maxima/minima, norms,
equalities almost everywhere and inequalities almost everywhere now
follow by extending all functions to one containing rectangle and using
P17.2/P20.2. These are all the assertions of Proposition 10.5.6.
Restriction to a Jordan subset \(T\subset S\) preserves integrability:
multiply the zero extension by \(\chi_T\). If \(A,B\) are disjoint
Jordan sets and \(f\) is integrable on each, the zero extensions satisfy
\(\widetilde f_{A\cup B}=\widetilde f_A+\widetilde f_B\).
This proves Proposition 10.5.7. If finitely many Jordan sets have null
pairwise intersections and \(f\) is integrable on each, the same identity
holds outside a finite union of null sets, so it still holds for integrals.
Integrability on the union follows, for example, by first replacing
each set by its difference from its predecessors, which is Jordan by
P20.3. Thus null overlaps do not get silently counted twice.

Here is Exercise 10.5.7 in its used generality. Let \(S\subset U\)
and \(T\subset U'\) be compact Jordan sets, \(g:U\to U'\) a \(C^1\)
diffeomorphism, \(g(S)\subset T\), and \(f\) integrable on \(T\).
The zero extension \(\widetilde f\) on a rectangle containing \(T\)
has a null discontinuity set. At every \(x\in S^\circ\) with
\(\widetilde f\) continuous at \(g(x)\), the zero extension of
\((f\circ g)|_S\) is continuous. Outside \(S\) it is locally zero.
Its remaining possible discontinuities lie in
\[
 \partial S\ \cup\ g^{-1}(D_{\widetilde f}\cap U'),
\]
which is null by P19.4 and P20.3. The extension is bounded, so
Theorem 10.4.3 proves its integrability. Multiplication by a continuous
function bounded on \(S\), in particular \(|\det g'|\), is justified
by the already proved product rule for integrable functions.
\(\square\)

### P20.5. Images of compact Jordan sets

Retain Proposition 10.5.9 and its full proof. For compact Jordan
\(S\subset U\) and an injective \(C^1\) map \(g:U\to\mathbb R^n\)
with \(\det g'\ne0\) on \(S\), compactness of \(g(S)\) is the exact
earlier continuous-image proof (Lemma 7.5.5). Its key inclusion is
\(\partial g(S)\subset g(\partial S)\). At \(x\in S^\circ\),
the inverse-function theorem applied within \(S^\circ\) makes \(g(x)\)
an interior point of \(g(S)\); hence a preimage of a boundary point
cannot be interior. This is also the conclusion of the source's sequence
argument. The notation \(f|_V\) in that source paragraph means \(g|_V\).
The local inverse theorem and its smooth-domain details are already proved
in P3/P10.6. P19.4 makes \(g(\partial S)\) null, and P20.3 proves
Jordan measurability of \(g(S)\).

In particular an invertible affine map takes compact Jordan sets to compact
Jordan sets. Translations preserve their volume: translating every grid in
the Darboux definition translates all its cells with unchanged side lengths
and unchanged indicator infima/suprema. Taking suprema and infima gives
\(V(S+b)=V(S)\), without assuming a substitution theorem. \(\square\)

## P21. Determinants and substitution

### P21.1. Completing the determinant–volume exercise

We prove Proposition 10.7.1, including singular linear maps:
\[
 V(A(R))=|\det A|V(R)                                      \tag{P21.1}
\]
for a bounded rectangle \(R\subset\mathbb R^n\).
Begin with a closed rectangle and invertible \(A\). It is compact,
convex and Jordan measurable. Every invertible linear image has these
three properties, the last by P20.5. A section of a compact convex set
along one coordinate is empty, a singleton, or a compact interval:
compactness makes its extrema exist, and convexity fills everything
between them. Its indicator has one-dimensional integral equal to the
interval length, including zero for the empty and singleton cases.
Compact Fubini (P17.5) therefore computes the volume by integrating
these section lengths over the other coordinates.

An elementary shear \(x_i\mapsto x_i+c x_j\), \(i\ne j\), translates
each \(i\)-coordinate section by the fixed amount \(c x_j\) and leaves
the other coordinates unchanged. Its section length and hence its volume
are unchanged. A nonzero elementary dilation \(x_i\mapsto c x_i\)
multiplies each such length by \(|c|\), for either sign of \(c\).
Choose common boxes in the other coordinates and containing intervals
in the integrated coordinate; the section statements then apply even
when a section is empty. A coordinate interchange preserves volume by
the exact relabelling of product grids proved in P17.5. From the
determinant permutation formula (P7), these three operations have
determinants \(1,c,-1\), respectively; these computations are also
covered by the already bound Proposition 8.2.8.

Every invertible matrix is a product of these elementary matrices.
For completeness, eliminate its first column by selecting a nonzero
entry, interchanging it into the first position, scaling the pivot to 1
and subtracting multiples of its row from the other rows. A nonzero
entry exists because an invertible matrix has no zero column.
The resulting matrix has block form
\(\begin{pmatrix}1&v\\0&B\end{pmatrix}\), with \(B\) invertible:
if \(Bw=0\), then \((-vw,w)\) lies in the kernel of the whole matrix,
so \(w=0\); finite-dimensional injectivity implies invertibility by
Proposition 8.1.18, with its linear-algebra omissions completed in
P9.1. Induction reduces \(B\) to the identity, and subtraction of the
remaining first-row entries reduces the whole matrix to the identity.
The inverses of the row operations are operations of the same three
types. Apply them to \(R\) in the resulting order. Every intermediate
set remains compact, convex and Jordan measurable, so the preceding
section calculation applies at every stage. Determinant multiplication
from Proposition 8.2.9, with permutation parity supplied by P7, then
proves (P21.1).

If \(A\) is singular, its range is a proper subspace by P9.1. Complete
an orthonormal basis of that range using P9.4 to obtain a nonzero vector
\(w\) orthogonal to it. Choose \(i\) with \(w_i\ne0\). The hyperplane
\(w\cdot x=0\) is the image of \(y_i=0\) under the invertible linear map
\[
 x_j=y_j\ (j\ne i),\qquad
 x_i=y_i-\sum_{j\ne i}(w_j/w_i)y_j.
\]
It is null by P19.3–P19.4. The compact set \(A(R)\) lies in it, so it
is Jordan measurable of volume zero by P20.3. Also \(\det A=0\):
the determinant/invertibility equivalence is the already proved
Proposition 8.2.9.
This proves (P21.1) in the singular case.

For an open or partly open rectangle, its closure is a closed rectangle.
The difference between its image and the image of the closure is
contained in \(A(\partial R)\). This is a compact null set by P19.3–P19.4.
Deleting an arbitrary subset of a closed null set from a compact Jordan
set preserves Jordan measurability: its boundary is contained in the
union of the original boundary and that closed null set, by the same
local membership argument as P20.3. P20.2 preserves the volume.
The side product is unchanged. This also covers zero-side rectangles.
\(\square\)

### P21.2. Neighbourhoods, finite covers and controlled refinements

Let \(S\subset U\) be compact, \(g:U\to\mathbb R^n\) injective and
\(C^1\), and suppose \(\det g'\ne0\) on \(S\). Before covering \(S\)
by surrounding rectangles, restrict the domain to
\[
 W=\{x\in U:\det g'(x)\ne0\}.
\]
It is open by continuity of the determinant, contains \(S\), and
\(g|_W\) is a diffeomorphism onto the open set \(g(W)\).
Indeed the inverse-function theorem supplies a local \(C^1\) inverse
near each point; injectivity makes these inverses agree on overlaps.
Their domains cover \(g(W)\), proving that the global inverse is \(C^1\).
This supplies the domain restriction needed in the opening reduction
of the source proof of Theorem 10.7.2.

For any compact \(K\subset W\), there is \(\delta>0\) whose closed
\(\delta\)-neighbourhood lies in \(W\): use the finite smaller/doubled
ball cover argument of P19.4 and decrease \(\delta\).
Choose an axis-aligned grid of cube side \(s>0\) with
\(\sqrt n\,s<\delta\). Only finitely many of its cubes meet bounded \(K\).
Every such closed cube lies in \(W\), since every point of it is
within \(\sqrt n\,s\) of a point of \(K\). These cubes have disjoint
interiors and cover \(K\), proving Exercise 10.7.2.
Their union is compact and Jordan by P20.3. It contains \(K\) in its
interior: all cubes incident to each point of \(K\) have been selected,
and their finite union contains a neighbourhood of that point.
This also completes Exercise 10.5.6.

The operator norm satisfies
\(|\|B\|-\|C\||\leq\|B-C\|\), by applying the triangle inequality in
both directions. Its continuity with respect to matrix entries was
proved in P9.2–P9.3. Hence
\(\{y:\|g'(x)-g'(y)\|<c\}\) is open, completing Exercise 10.7.3.
Uniform continuity of \(g'\) on a compact rectangle makes its oscillation
less than any prescribed tolerance on all sufficiently small cells.

For Exercise 10.7.4, consider the finitely many positive side lengths
of a given finite rectangular partition. Choose \(\tau>0\) smaller
than all of them. Divide an interval of length \(a\) into
\(N=\lceil a/\tau\rceil\) equal pieces. The Archimedean property gives
this integer, and
\[
 a/\tau\leq N<a/\tau+1\leq2a/\tau
 \quad\Longrightarrow\quad \tau/2<a/N\leq\tau .
\]
The product subdivisions refine the original partition; every side of
every new cell lies in \([\tau/2,\tau]\), and its diameter is at most
\(\sqrt n\,\tau\). Degenerate rectangles have integral zero; in the
substitution proof their images are null by P19.4 and are removed first.
Thus no positive-side division is used for them. \(\square\)

### P21.3. The full compact Jordan change-of-variables theorem

With \(S,U,g\) as in P21.2, suppose additionally that \(S\) is Jordan
measurable and \(f:g(S)\to\mathbb R\) is Riemann integrable. Then
\(f\circ g\) is Riemann integrable on \(S\) and
\[
 \int_S f(g(x))|\det g'(x)|\,dx=\int_{g(S)}f(u)\,du.       \tag{P21.2}
\]
This is the full scope of the existing Theorem 10.7.2. Retain its
proof with the following supplied inputs and domain clarification.

First use \(W\) from P21.2. P20.5 proves that \(g(S)\) is Jordan,
and P20.4 proves integrability of the composition and of its product
with the continuous Jacobian. Extend \(f\) by zero away from \(g(S)\).
Cover \(S\) by the finite rectangles in P21.2. The extension is
integrable on every image rectangle, by restriction of its integrable
zero extension to a Jordan set. On each domain rectangle its pullback
vanishes outside \(S\), since \(g\) is injective. Domain overlaps
lie in grid faces, and their image overlaps lie in their null images
by P19.4. P20.4 therefore justifies summing the integrals. This reduces
the theorem to a nondegenerate closed rectangle \(R\subset W\).

Here are the precise estimates in the retained proof. On \(R\),
\(\|(g'(x))^{-1}\|\leq M\) for a finite \(M\geq1\), by P2 and
compactness. Take \(f\geq0\), put
\(\varphi(x)=f(g(x))|\det g'(x)|\), and choose a Darboux partition
with \(U(P,\varphi)\leq\int_R\varphi+\varepsilon\).
P21.2 refines it to cells \(R_j\) with side lengths in
\([\tau/2,\tau]\), with \(\tau\) sufficiently small that
\(\|g'(\xi)-g'(\eta)\|<\varepsilon/M\) within each cell.
Choose \(x_j\in R_j\) minimizing \(|\det g'|\), and put \(A_j=g'(x_j)\).
For \(x\in R_j\), the normalized map
\[
 q_j(x)=x_j+A_j^{-1}(g(x)-g(x_j))
\]
satisfies \(q_j(x_j)=x_j\) and \(\|q_j'(x)-I\|<\varepsilon\).
The compact vector fundamental theorem along the segment in \(R_j\)
gives
\[
 |q_j(x)-x|\leq\varepsilon|x-x_j|
             \leq\varepsilon\sqrt n\,\tau.
\]
Thus \(q_j(R_j)\) lies in the rectangle obtained by adding
\(\varepsilon\sqrt n\,\tau\) at both ends of every side. Its volume is
at most \(V(R_j)(1+4\sqrt n\,\varepsilon)^n\).
Using monotonicity of volume, translation invariance P20.5, and
the proved determinant formula P21.1 gives
\[
 V(g(R_j))\leq |\det g'(x_j)|V(R_j)
                      (1+4\sqrt n\,\varepsilon)^n.        \tag{P21.3}
\]
The nonnegative Darboux estimate, followed by P20.4 on the null overlaps,
now yields
\[
 \int_R\varphi+\varepsilon
 \ \geq\ \sum_j\sup_{R_j}(f\circ g)\,|\det g'(x_j)|V(R_j)
 \ \geq\ (1+4\sqrt n\,\varepsilon)^{-n}\int_{g(R)}f.
\]
Let \(\varepsilon\downarrow0\). This proves the inequality
\(\int_S(f\circ g)|\det g'|\geq\int_{g(S)}f\) on the original
compact Jordan set as well.

Apply that already proved inequality to \(g^{-1}:g(W)\to W\),
the compact Jordan set \(g(S)\), and the nonnegative integrable function
\(\varphi\) on \(S\). The chain rule and determinant multiplication give
\[
 |\det(g^{-1})'(u)|\,|\det g'(g^{-1}(u))|=1.
\]
Consequently the resulting inequality is the reverse one in (P21.2).
For general real \(f\), apply the result to
\(f_+=\max(f,0)\) and \(f_-=\max(-f,0)\), which are integrable
by P20.2, and subtract. Real and imaginary parts prove the complex
version; finitely many components give the vector version.
This completes every invoked exercise and domain step while preserving
the original theorem's full Riemann-integrable amplitude scope.
\(\square\)

### P21.4. Whole-space affine and compact-chart substitutions

We first extend the exhaustion fact in P18.1 from rectangles to bounded
Jordan sets. If \(F:\mathbb R^n\to\mathbb C\) is continuous and absolutely
integrable, \(K_r=[-r,r]^n\subset S\subset K_t\), and \(S\) is Jordan,
P20.4 gives
\[
 \left|\int_SF-\int_{K_r}F\right|
 \leq\int_{K_t\setminus K_r}|F|
 \leq\int_{\mathbb R^n}|F|-\int_{K_r}|F|.
\]
The last quantity tends to zero with \(r\). Any family of bounded Jordan
sets eventually containing each \(K_r\) therefore has integrals tending
to the same whole-space integral. No monotonicity of that family is needed.

Let \(A\) be invertible and \(b\in\mathbb R^n\). Apply P21.3 to
\(x\mapsto Ax+b\) on \(K_R\), first with \(|F|\).
The image is compact Jordan, and
\[
 \int_{K_R}|F(Ax+b)|\,|\det A|\,dx
     =\int_{A K_R+b}|F|\leq\int_{\mathbb R^n}|F|.
\]
Thus \(F(Ax+b)\) is absolutely integrable by the definition P18.1.
The image sets eventually contain every \(K_r\): if \(u\in K_r\), then
\(|A^{-1}(u-b)|\leq\|A^{-1}\|(\sqrt n\,r+|b|)\).
The preceding exhaustion estimate and P21.3 for \(F\) show
\[
 \int_{\mathbb R^n}F(Ax+b)|\det A|\,dx
       =\int_{\mathbb R^n}F(u)\,du.                        \tag{P21.4}
\]
This proves translations, orthogonal changes (\(|\det A|=1\)) and
positive dilations (\(\det(cI)=c^n\)), with their exact Jacobians.

For a compactly supported Riemann-integrable function \(f\) on an open
chart image \(V\), let \(g:U\to V\) be a \(C^1\) diffeomorphism.
Its compact support \(K\subset V\) has compact preimage \(g^{-1}(K)\)
by continuity of the inverse and the earlier compact-image theorem.
Choose a compact Jordan neighbourhood \(S\subset U\) of that preimage
using P21.2. Apply P21.3 on \(S\). Both integrands vanish outside the
corresponding compact supports, so extending them by zero gives
\[
 \int_U f(g(x))|\det g'(x)|\,dx=\int_V f(u)\,du.
\]
On the left the extension is explicitly zero outside \(U\); no second
preimage elsewhere is counted. When both \(f\) and \(g\) are smooth,
this zero extension is smooth by P17.4 and the ordinary product/chain rules. This is the
compact chart substitution needed by the parameter-Morse argument.
\(\square\)

### P21.5. Polar coordinates and the Gaussian integral

For \(0<a<b\) and \(0<\delta<\pi/2\), use
\[
 g(r,\theta)=(r\cos\theta,r\sin\theta),\qquad
 S=[a,b]\times[\delta,2\pi-\delta].
\]
It is injective on a neighbourhood of \(S\) contained in
\((0,\infty)\times(0,2\pi)\). Equality of images first gives equality
of the radii by \(\cos^2\theta+\sin^2\theta=1\). P16.2–P16.3 give
uniqueness of the angle in this interval: the quadrant signs distinguish
the four quadrants, and the monotone inverse tangent distinguishes angles
inside a quadrant; the four axis cases were included there.
Its derivative and determinant are
\[
 g'(r,\theta)=
 \begin{pmatrix}\cos\theta&-r\sin\theta\\
                 \sin\theta&r\cos\theta\end{pmatrix},
 \qquad \det g'=r>0.
\]
P21.3 consequently proves the compact-sector formula
\[
 \int_{g(S)}F(x,y)\,dx\,dy
 =\int_\delta^{2\pi-\delta}\int_a^b
       F(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta            \tag{P21.5}
\]
for every continuous \(F\) on the sector image. The iterated integrals
are justified by compact Fubini.

Here is the exhaustion needed at the missing ray and origin. Suppose
\(F\) is continuous and absolutely integrable on \(\mathbb R^2\).
Fix \(T>0\), and bound \(|F|\) on \(K_T=[-T,T]^2\) by \(M_T\).
If \(b>\sqrt2T\) and \(0<\delta<\pi/4\), the part of \(K_T\)
outside \(g(S)\) lies in the union of
\[
 [-a,a]^2,\qquad [0,T]\times[-T\tan\delta,T\tan\delta].
\]
Indeed a point with radius at least \(a\) and at most \(b\) fails
to have angle in \([\delta,2\pi-\delta]\) only in the sector around
the positive horizontal axis; there \(x\geq0\) and
\(|y|\leq x\tan\delta\). These statements include the ray itself.
The difference of the integrals over \(K_T\) and its intersection
with the sector is bounded by
\[
 M_T(4a^2+2T^2\tan\delta).
\]
All these sets are Jordan by P20.3/P20.5, so the bound follows from
finite additivity and the norm inequality, not from an unproved
convergence theorem for indicator functions. The part of the sector
outside \(K_T\) has absolute integral at most the absolute tail outside
\(K_T\), by P20.4 and P18.1. Hence
\[
 \left|\int_{\mathbb R^2}F-\int_{g(S)}F\right|
 \leq 2\int_{K_T^c}|F|+
             M_T(4a^2+2T^2\tan\delta).
\]
First make the tail small by increasing \(T\), then let
\(a\downarrow0\), \(b\uparrow\infty\), \(\delta\downarrow0\).
P16.3 proves \(\tan\delta\to0\).
This proves the whole-plane polar substitution as a limit of the
compact formulas (P21.5), with no assumption about arbitrary section
integrals of an absolutely integrable function.

In the actual Gaussian application \(F(x,y)=e^{-(x^2+y^2)/2}\),
absolute integrability was proved in P18.3. Compact Fubini and the
fundamental theorem evaluate the right side of (P21.5) exactly as
\[
 (2\pi-2\delta)\bigl(e^{-a^2/2}-e^{-b^2/2}\bigr).
\]
Its limit is \(2\pi\), using continuity and P14.3. P18.4 also gives
\[
 \left(\int_{\mathbb R}e^{-x^2/2}\,dx\right)^2
       =\int_{\mathbb R^2}e^{-(x^2+y^2)/2}\,dx\,dy .
\]
The one-dimensional integral is positive, since its restriction to
\([-1,1]\) is at least \(2e^{-1/2}>0\). The unique positive root
from P8 therefore gives its value \(\sqrt{2\pi}\).
This closes the polar-coordinate step in Q2. \(\square\)

### P21.6. The remaining quadratic proofs and the preserved full lesson

Q2 now uses the proved Gaussian value P21.5, P18.3 for all polynomial
Gaussian majorants, Q1 for its parameter derivatives, and P16.3 for its
right-half-plane root. Its integrations by parts are the compact
fundamental theorem followed by the proved absolute tails and exponential
boundary decay. Thus its path and real-frequency differential identities
have all stated prerequisites supplied.

Q4 uses the product-majorant Fubini theorem P18.4, Q2 in each coordinate,
and the affine substitutions P21.4. Its finite first Gaussian moment
follows from P18.3. Q3 supplies the Schwartz Fourier bounds and Q1
justifies the limiting multiplier. Hence the Fourier inversion proof
is closed before it is used in stationary phase.

Q6 uses exactly the now-proved orthogonal substitution, Q5, Q4, the
product-majorant theorem and the root limits in P16.3. The integrable
majorant and compact-uniform convergence written there permit both
regularization limits by Q1. Q7 then uses the proved integral Taylor
formula, Q3's weighted estimate and Q4's differentiated inversion.
Its coefficient sign and finite-order bound are unchanged. Q8 uses the
smooth cofactor inverse P2, the continuous seminorm estimates of Q3 and
the repeated parameter version of Q1; its normalized parameter remainder
therefore retains its full stated scope. E1 follows from Q2/Q7, with
the same absolute-tail integration by parts for its Gaussian moments.
All of Q1–Q9 and E1 now have their exact prerequisite proofs.

This closes the *quadratic reconstruction module*. The sharper finite derivative bounds, coefficient gluing, all frequency derivatives, clean critical manifolds and quotient densities of the full stationary-phase lesson are not proved here. That larger lesson and the full AN-04 course remain the intended deliverables.
