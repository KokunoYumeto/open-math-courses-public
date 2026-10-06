# Rectangle integrals, tails and the interchanges used in stationary phase

Prerequisite companion, adapted and extended from Jiří Lebl,
*Basic Analysis* 6.3, [freely accessible author edition](https://www.jirka.org/ra/),
under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
The selected human proofs are in §§10.1–10.2 and §5.5. Their complete arguments
are retained through exact programme bindings. P17 supplies actual omissions;
P18 extends the proved compact integrals to the unbounded integrals used here.
The change-of-variables theorem is a separate dependency.

We use the earlier ordered real-field, topology, differential, complex-number
and compact one-variable integral chains. Rectangles, grid partitions, volume,
upper/lower Darboux sums and integrability have Lebl's definitions in §10.1.
Vector-valued integrability means integrability of every component; its integral
is the vector of those integrals. Complex integrals use the identification
\(\mathbb C=\mathbb R^2\). All sums defining a grid are finite.

## P17. Completing the multivariable compact integral proofs

### P17.1. Grid volumes, degenerate rectangles and both refinements

For a nondegenerate rectangle \(R=\prod_{j=1}^n[a_j,b_j]\), each point
has its \(j\)th coordinate in at least one interval of the finite partition
of \([a_j,b_j]\). Choosing one such interval in each coordinate puts the
point in a grid cell. Thus the cells cover \(R\). Their volumes sum to
\[
 \sum_{k_1,\ldots,k_n}\prod_{j=1}^n
       (x_{j,k_j}-x_{j,k_j-1})
 =\prod_{j=1}^n\sum_{k_j}(x_{j,k_j}-x_{j,k_j-1})
 =\prod_{j=1}^n(b_j-a_j)=V(R).
\]
Finite distributivity gives the first equality and telescoping gives the
second. The same calculation within any old cell proves the refined-cell
volume identity used in Proposition 10.1.5. No volume of a curved set is used.

If a side is a singleton \([a_j,a_j]\), take that singleton as its one
interval, of length zero; its product cells all have volume zero. Both Darboux
sums and both integrals are zero for every bounded function. This supplies
Exercise 10.1.3 and removes the division-by-zero case from Theorem 10.1.15.
For dimension zero, the rectangle is the single empty tuple, its volume is
the empty product 1, and its integral is evaluation. All subsequent statements
use that convention; estimates involving \(\sqrt n\) concern \(n\geq1\).

Keep the written lower-refinement proof in Proposition 10.1.5. For its omitted
upper half, let \(M_k=\sup_{R_k}f\) and
\(\widetilde M_l=\sup_{\widetilde R_l}f\). If the new cell lies in
the old one, \(\widetilde M_l\leq M_k\), by the definition of supremum.
Multiply by its nonnegative volume, sum inside the old cell, and use the
volume identity above. Summing over the old cells gives
\(U(\widetilde P,f)\leq U(P,f)\).
The complete written proofs of Propositions 10.1.2, 10.1.6, 10.1.12 and
10.1.13 now apply. Their uses of suprema/infima and common refinements are
justified by P12.1; in particular a nonempty family of nonnegative Darboux
gaps has infimum zero exactly when it has arbitrarily small members.
\(\square\)

### P17.2. Linearity, monotonicity, products and the vector norm bound

Here are the proofs left in Propositions 10.1.10–10.1.11. For \(c\geq0\),
\(L(P,cf)=cL(P,f)\) and \(U(P,cf)=cU(P,f)\); the case \(c=0\)
is immediate. For \(c<0\), multiplication reverses order, giving
\(L(P,cf)=cU(P,f)\) and \(U(P,cf)=cL(P,f)\).
P12.1 transfers these equalities to the upper/lower integrals and proves
scalar linearity for integrable \(f\).

On each cell the infimum of \(f+g\) is at least the sum of the infima,
and its supremum is at most the sum of the suprema. Thus
\[
 L(P,f)+L(P,g)\leq L(P,f+g)\leq U(P,f+g)
                   \leq U(P,f)+U(P,g).
\]
Choose small-gap partitions for \(f,g\), then their common refinement.
The resulting gap for \(f+g\) is arbitrarily small. Moreover the sum of
their integrals and the integral of \(f+g\) both lie between the two outer
sums above, whose difference tends to zero. This proves additivity, and
induction proves finite linearity. If \(f\leq g\), every lower sum for
\(f\) is at most the same lower sum for \(g\); taking suprema proves
monotonicity. Constants integrate to their value times \(V(R)\), by
Proposition 10.1.6, just as in Example 10.1.9.

Write \(\operatorname{osc}_Q f=\sup_Q f-\inf_Q f\). For real bounded
functions, the elementary pointwise estimates give
\[
 \operatorname{osc}_Q|f|\leq\operatorname{osc}_Qf,\qquad
 \operatorname{osc}_Q(fg)
 \leq\|f\|_\infty\operatorname{osc}_Qg
       +\|g\|_\infty\operatorname{osc}_Qf.
\]
For example, write \(f(x)g(x)-f(y)g(y)\) as
\(f(x)(g(x)-g(y))+g(y)(f(x)-f(y))\), take absolute values and then
suprema over \(x,y\). The equality between the supremum of differences
and the oscillation follows from P12.1. Multiplying these inequalities by
cell volumes and using common small-gap partitions proves integrability
of \(|f|\) and \(fg\) whenever \(f,g\) are integrable.

If \(F=(f_1,\ldots,f_d)\), the reverse-triangle inequality yields
\[
 \operatorname{osc}_Q |F|\leq\sum_{j=1}^d\operatorname{osc}_Q f_j.
\]
Hence \(|F|\) is integrable. Put \(I=\int_R F\). If \(I\ne0\),
take the constant unit vector \(q=I/|I|\); finite linearity and
\(q\cdot F\leq|F|\) give
\[
 \left|\int_R F\right|=q\cdot I=\int_R q\cdot F\leq\int_R|F|.
 \tag{P17.1}
\]
If \(I=0\), the inequality follows from nonnegativity of the last integral.
Consequently \(|\int_R(F-G)|\leq V(R)\sup_R|F-G|\) for two integrable
functions. Complex linearity follows by expanding multiplication by a
constant complex number into its two real coordinates. \(\square\)

### P17.3. Additivity, zero faces and extension by zero

Suppose a fixed finite grid divides a rectangle into cells \(R_1,\ldots,R_N\),
and \(f\) is integrable on each cell. It is bounded on their union, since
there are only finitely many cells. In each cell choose a partition with gap
less than \(\varepsilon/N\). Extend all their coordinate cuts to the whole
rectangle and take their union with the original grid. The induced partition
on every old cell refines its chosen partition, so the sum of these gaps is
less than \(\varepsilon\). The global lower and upper sums are exactly
the sums of the cell lower and upper sums. The gap criterion proves global
integrability; both the global integral and \(\sum_j\int_{R_j}f\) lie
between these same sums. Letting \(\varepsilon\to0\) proves equality.
Restriction to cells is Proposition 10.1.13, already proved. Degenerate cells
contribute zero. This supplies the grid-additivity form of Exercise 10.1.8.

For the boundary issue, let a bounded \(h\), \(|h|\leq M\), vanish
off finitely many coordinate hyperplanes inside a nondegenerate rectangle
\(S=\prod[a_j,b_j]\). For a plane \(x_j=c\), insert \(c\) and
\(c\pm\delta\), when they lie inside the interval, among the cuts.
The cells touching that plane have total volume at most
\(2\delta\prod_{k\ne j}(b_k-a_k)\). All other cells have \(h=0\).
For finitely many planes, the sum of the volumes of the cells that touch
at least one is bounded by the sum of these bounds: a cell counted multiple
times only enlarges that sum. Thus the Darboux gap is at most twice \(M\)
times a quantity tending to zero with \(\delta\). The absolute values
of both sums are at most \(M\) times that same quantity. Hence
\(\int_S h=0\). If \(S\) is degenerate, P17.1 proves this directly.
The boundary of a rectangle in positive dimension lies in its finitely many
coordinate face hyperplanes, including the degenerate case. This proves
Exercise 10.1.6 and proves that changing bounded values on those faces
does not change an integral.

Let \(R'\subset R\) be closed rectangles, with \(f\) integrable on
\(R'\) and zero on \(R\setminus R'\). Change its values on
\(\partial R'\) to zero, obtaining \(g\). On \(R'\) this changes
the integral by zero. Cut \(R\) at every face of \(R'\). The function
\(g\) is zero on every outside cell, and integrable on each inside cell
by restriction. Grid additivity proves that \(g\) is integrable on \(R\)
and \(\int_R g=\int_{R'}g\). Its difference from \(f\) is supported
on the face hyperplanes and has integral zero on both rectangles. Therefore
\(\int_R f=\int_{R'}f\), proving the full Exercise 10.1.7.
If \(R'\) is degenerate, \(f\) itself is supported on one such plane,
which proves the same conclusion. Dimension zero is immediate by evaluation.

It follows in particular that an integrable compactly supported function has
the same integral in every containing rectangle. To compare two rectangles,
first place both in one larger rectangle and extend the given function by
zero there using the result just proved; restrict to the second rectangle
and apply it again. If the support is empty, the function is zero. This
completes Exercise 10.1.9 and the dependency left in Proposition 10.1.19.
\(\square\)

### P17.4. Continuous functions, compact support and parameter continuity

Retain the complete diameter and uniform-continuity proofs in Proposition
10.1.14 and Theorem 10.1.15. In the nondegenerate positive-dimensional case,
a finite grid with each side shorter than \(\delta/\sqrt n\) exists:
for the \(j\)th side choose an integer
\(N_j>\sqrt n(b_j-a_j)/\delta\), by P6.0, and divide it into \(N_j\)
equal intervals. Its cells have the required diameter. The zero-volume and
zero-dimensional cases are handled by P17.1, so no division by \(V(R)=0\)
or by \(\sqrt0\) is made. Boundedness, extrema and uniform continuity
come from the existing F0-COMP proofs.

For Exercise 10.1.1, suppose \(f\) is continuous on open \(U\) with
compact support \(K\subset U\). The inclusion of \(U\) into
\(\mathbb R^n\) is continuous, so \(K\) is compact in \(\mathbb R^n\)
and therefore closed there. Extend \(f\) by zero outside \(U\).
At points in \(U\) continuity is unchanged. At any point outside \(U\),
the open complement of \(K\) supplies a neighborhood on which the extension
is identically zero. Thus the extension is continuous. The same reasoning
gives a \(C^r\) or smooth extension whenever \(f\) has that regularity.
Every derivative is zero wherever the original function is zero on a
neighborhood, so taking derivatives cannot enlarge its support.

If \(F(p,x)\) is jointly continuous near \(\{p_0\}\times R\), choose
a compact parameter box around \(p_0\) on which it is defined for all
\(x\in R\). Such a box follows from a finite subcover of the compact
set \(\{p_0\}\times R\) by product neighborhoods. Uniform continuity
on the resulting compact product and (P17.1) imply
\[
 \left|\int_R F(p,x)\,dx-\int_R F(p_0,x)\,dx\right|
 \leq V(R)\sup_{x\in R}|F(p,x)-F(p_0,x)|\longrightarrow0.
\]
This proves the finite-parameter continuity used in repeated integration.
\(\square\)

### P17.5. The upper half of Fubini and every coordinate order

Retain the complete written argument of Lebl Theorem 10.2.2. For its omitted
upper-sum inequality, let
\(M_{ij}=\sup_{R_i\times S_j}f\) and
\(M_j(x)=\sup_{y\in S_j}f(x,y)\). For \(x\in R_i\),
\(M_j(x)\leq M_{ij}\), and hence
\[
 h(x)=\overline{\int_S}f(x,y)\,dy
 \leq U(P',f_x)=\sum_j M_j(x)V(S_j)
 \leq\sum_j M_{ij}V(S_j).
\]
Take the supremum over \(x\in R_i\), multiply by \(V(R_i)\), and
sum over \(i\). The result is
\(U(P,h)\leq U((P,P'),f)\), completing Exercise 10.2.2.
The source's lower bound, its Darboux-gap estimates and the fact
\(g\leq h\) then prove integrability and equality of both outer
integrals. These functions are bounded because the lower and upper integrals
of each section lie between \(-B V(S)\) and \(B V(S)\) if \(|f|\leq B\).

For the reverse order (Exercise 10.2.3), define
\(\widetilde f(y,x)=f(x,y)\). A product grid becomes the swapped grid;
each cell has the same infimum and supremum, and
\(V(R_i)V(S_j)=V(S_j)V(R_i)\). Thus all Darboux sums and the integral
are unchanged, directly from the definitions. Applying the proved version A
to \(\widetilde f\) proves version B. This argument is not an appeal to
an unproved change-of-variables formula.

For continuous \(f\), every section is integrable by Theorem 10.1.15 and
each partial integral is continuous by P17.4. Repeating Fubini therefore
permits every finite coordinate order; a permutation merely relabels grid
coordinates and their volume factors as above. The vector and complex
versions follow componentwise. In particular, for continuous \(u,v\)
on the respective rectangles,
\[
 \int_{R\times S}u(x)v(y)\,dx\,dy
 =\left(\int_R u(x)\,dx\right)\left(\int_S v(y)\,dy\right),
\]
by first integrating the constant factor \(u(x)\) in the \(y\) integral
and then the other constant factor. This supplies Exercise 10.2.5, including
complex-valued factors. The general compact-rectangle theorem retains its
upper/lower-integral formulation when individual sections are not integrable.
\(\square\)

## P18. The unbounded integrals actually used by Q1–Q9

### P18.1. Absolute integrability, Cauchy limits and tails

Lebl §5.5 defines improper integrals as limits of compact integrals. Retain
the complete tail and nonnegative-supremum arguments in Propositions 5.5.3
and 5.5.4. Its comparison proof (Proposition 5.5.5) uses the Cauchy bound
\(|\int_b^c f|\leq\int_b^c g\) for \(|f|\leq g\). The following
argument gives its vector/multivariable version and the explicit passage
from integer radii to arbitrary radii.

Call \(F:\mathbb R^n\to\mathbb R^d\) locally Riemann integrable if
its restriction to every compact rectangle is integrable. For \(R>0\),
write \(K_R=[-R,R]^n\). Define absolute integrability by
\[
 A=\sup_{R>0}\int_{K_R}|F|<\infty.                 \tag{P18.1}
\]
For a nonnegative locally integrable \(g\), \(A_R=\int_{K_R}g\)
increases with \(R\): cut the larger cube along the faces of the smaller,
and use P17.3 and nonnegativity. If its supremum \(A\) is finite, for
every \(\varepsilon>0\) choose \(R_0\) with \(A-A_{R_0}<\varepsilon\).
For all \(R\geq R_0\), \(0\leq A-A_R<\varepsilon\). Thus
\(A_R\to A\). This is exactly the supremum argument in Proposition 5.5.4,
now applied to cubes.

For \(F\) satisfying (P18.1), finite grid additivity and the norm bound
give, for \(T\geq R\),
\[
 \left|\int_{K_T}F-\int_{K_R}F\right|
 \leq\int_{K_T}|F|-\int_{K_R}|F|
 \leq A-\int_{K_R}|F|.                             \tag{P18.2}
\]
Indeed the difference consists of the finitely many outside cells in that
grid; apply the triangle inequality and (P17.1) to them. Therefore the
integrals over \(K_N\), \(N\in\mathbb N\), form a Cauchy sequence in
the complete finite-dimensional space, and have a limit \(I\). For arbitrary
\(R\geq N\), compare with \(K_N\) in (P18.2); letting \(N\to\infty\)
shows that \(\int_{K_R}F\to I\) through all real radii. Define
\(\int_{\mathbb R^n}F=I\). This is an absolutely convergent improper
integral, not a claim that a conditionally convergent principal value suffices.

The nonnegative tail outside \(K_R\) is
\(A-\int_{K_R}|F|\), which tends to zero. Its interpretation as a limit
of the outside-cell integrals follows directly from the preceding grid
identity. Letting \(T\to\infty\) in (P18.2) gives the error bound by
this tail. If a rectangle \(B\) contains \(K_R\), enclose \(B\) in a
larger cube and use the same finite cuts to get
\[
 \left|\int_B F-\int_{K_R}F\right|
 \leq A-\int_{K_R}|F|.
\]
Every family of rectangles that eventually contains each fixed cube thus
has the same limit, independently of rates or nesting. This also establishes
the usual two independent endpoints on the real line for an absolutely
integrable function. On the right half-line replace \(K_R\) by \([a,R]\)
for \(R>a\): compact additivity gives the identical increment bound
\(|I_T-I_R|\leq A_T-A_R\), so the integer-sequence and arbitrary-radius
argument applies unchanged, starting at an integer greater than \(a\).
On the left use \([-R,a]\) and start with \(R>-a\). The two halves add
by compact additivity. No reversal of a conditional limit is
used. In dimension zero all integrals are evaluation and all tails are zero.
\(\square\)

### P18.2. Global linearity, comparison and the compact-uniform limit rule

The compact norm, linearity and monotonicity inequalities pass to limits.
For example, \(|aF+bG|\leq|a||F|+|b||G|\) implies that \(aF+bG\)
satisfies (P18.1), and taking cube limits proves linearity and
\[
 \left|\int F\right|\leq\int|F|.
\]
If \(|F|\leq g\), with \(g\geq0\) locally Riemann integrable and
\(\sup_R\int_{K_R}g<\infty\), compact comparison gives absolute
integrability of \(F\) and its integral and tail bounds by those of \(g\).
This is the norm-valued comparison theorem needed here.

Let continuous \(F_t\) tend to continuous \(F_0\) uniformly on every
compact set, and let \(|F_t|\leq g\) for such a nonnegative \(g\),
including \(t=0\). Choose \(R\) so that the tail of \(g\) is less
than \(\varepsilon\). Splitting the two global integrals into \(K_R\)
and their tails yields
\[
 \left|\int F_t-\int F_0\right|
 \leq V(K_R)\sup_{K_R}|F_t-F_0|+2\varepsilon.
\]
First let \(t\to0\), then \(\varepsilon\to0\). This proves precisely
the first part of Q1, for any finite-dimensional target. Its differentiation
part follows from the compact-interval identity
\[
 \frac{F(t+s,x)-F(t,x)}s
 =\int_0^1\partial_tF(t+us,x)\,du.
\]
Joint continuity of the derivative makes the difference quotients converge
uniformly on compact \(x\)-sets, by uniform continuity on the product with
a small closed parameter interval. Their modulus is bounded by the same
integrable majorant as the derivative. The proved limit rule therefore
passes this difference quotient through the global integral. The compact
fundamental theorem also gives
\(|F(t+s,x)-F(t,x)|\leq|s|g(x)\), so integrability at \(t\) ensures
integrability nearby. The same limit rule proves continuity of the derivative;
induction covers every fixed finite order with the stated local majorants.
\(\square\)

### P18.3. Integrable decay bounds and the Gaussian majorants

The written \(p>1\) part of Proposition 5.5.2 follows from the already
proved real-power derivative and the fundamental theorem:
\[
 \int_1^R t^{-p}\,dt=\frac{1-R^{1-p}}{p-1}
 \longrightarrow\frac1{p-1}.
\]
For noninteger \(p\), \(R^{1-p}\to0\) follows explicitly from
\(R^{1-p}=\exp(-(p-1)L(R))\), the logarithm endpoint limit and the
real exponential endpoint limit in P14. No unused part of the source's
\(p\)-test is imported. In particular, by integrating separately on the
two half-lines,
\[
 w(t)=(1+|t|)^{-2},\qquad \int_{\mathbb R}w(t)\,dt=2.
\]
The compact computation on each half uses its primitive
\(-(1+t)^{-1}\) after reflecting the negative half by the proved
one-variable substitution formula. Compact Fubini gives
\(\int_{K_R}\prod_{j=1}^n w(x_j)=(\int_{-R}^R w)^n\);
taking limits proves that this product is integrable with integral \(2^n\).

For the sharper radial decay threshold, let \(s>n\) and
\(|F(x)|\leq C(1+|x|)^{-s}\), with \(F\) locally integrable.
Cut \(K_{2^{j+1}}\) along the faces of \(K_{2^j}\). On each outside
cell, \(|x|\geq2^j\); their total volume is at most
\((2^{j+2})^n\). Hence
\[
 \int_{K_{2^{j+1}}}|F|-\int_{K_{2^j}}|F|
 \leq C2^{2n}2^{j(n-s)}.
\]
The ratio \(2^{n-s}\) lies in \((0,1)\), by P14's real exponential
and logarithm laws. The finite geometric sum formula and its vanishing
geometric tail bound the sum of these increments uniformly and make their
tail tend to zero. The integral inside \(K_1\) is finite. Every cube lies
in a dyadic cube, so (P18.1) follows. This proof uses rectangular shells,
not an unproved volume or integration formula for annuli.

Every polynomial multiple of a Schwartz derivative satisfies this bound for
arbitrarily large \(s\), by its defining seminorms and
\(|x^\alpha|\leq(1+|x|)^{|\alpha|}\). It is therefore integrable.
The weight in Q3 satisfies, for \(|\xi|\geq1\),
\[
 \frac{|\xi|^{2N}}{(1+|\xi|^2)^M}
 \leq |\xi|^{-(2M-2N)}
 \leq 2^{2M-2N}(1+|\xi|)^{-(2M-2N)},
\]
so the stated condition \(M>N+n/2\) suffices. It is bounded near zero.
Finally, P14.3 shows that every fixed polynomial times \(e^{-c|x|^2}\)
has arbitrary polynomial decay for \(c>0\): as a function of \(r=|x|\),
its product with any required power of \(1+r\) tends to zero at infinity
and is bounded on the remaining compact interval. These are the absolute
majorants used by Q2 and all Gaussian regularizations. \(\square\)

### P18.4. Global Fubini under the domination present in this lesson

Let \(F:\mathbb R^n\times\mathbb R^m\to\mathbb C\) be continuous,
and suppose
\[
 |F(x,y)|\leq g(x)h(y),                             \tag{P18.3}
\]
where \(g,h\) are nonnegative continuous absolutely integrable functions.
Then all section integrals exist, their integrals can be taken in either
order, and both equal \(\int_{\mathbb R^{n+m}}F\).

Write \(G_R=\int_{K_R^n}g\), \(H_R=\int_{K_R^m}h\), and their
finite limits as \(G,H\). Compact Fubini and comparison give
\(\int_{K_R^{n+m}}|F|\leq G_RH_R\leq GH\), establishing global
absolute integrability. For fixed \(x\), comparison with \(g(x)h\)
gives \(A(x)=\int_{\mathbb R^m}F(x,y)\,dy\), and
\[
 |A(x)|\leq Hg(x),\qquad
 \left|A(x)-\int_{K_T^m}F(x,y)\,dy\right|
 \leq g(x)(H-H_T).                                \tag{P18.4}
\]
The compact partial integrals are continuous by P17.4. Since \(g\) is
bounded on compact sets, (P18.4) is uniform there; its limit \(A\) is
continuous by the three-term continuity argument of P15.1. Comparison then
shows that \(A\) is globally absolutely integrable. For each \(R\),
\[
 \left|\int_{K_R^n}A(x)\,dx
       -\int_{K_R^{n+m}}F(x,y)\,dx\,dy\right|
 \leq G_R(H-H_R)\longrightarrow0.
\]
The compact Fubini theorem and the compact norm bound prove this inequality.
Letting \(R\to\infty\) proves the asserted equality. Interchange
\(x,y\), whose product grids have identical volumes, to prove the other
order. A zero-dimensional factor is evaluation and the same assertion is
immediate. The proof applies componentwise to any finite-dimensional target.

For continuous absolutely integrable \(u(x),v(y)\), take
\(g=|u|\), \(h=|v|\) and apply complex linearity to the section
integral. This gives \(\int u(x)v(y)=(\int u)(\int v)\).
For a rapidly decreasing continuous function of \(d\) real coordinates,
\[
 |F(x)|\leq C(1+|x|)^{-2d}
 \leq C\prod_{j=1}^d(1+|x_j|)^{-2},
\]
since \(\prod_j(1+|x_j|)^2\leq(1+|x|)^{2d}\).
The factors on the right are continuous and have the proved finite
integrals. Repeated application of (P18.4) gives every coordinate order for
such functions and for their polynomially weighted derivatives. In Q4 and
Q6 the doubled integral has the explicit product majorant of a Gaussian
in one group of variables and a Schwartz function's modulus in the other.
Thus (P18.3) holds at each actual interchange.

This is the global Fubini statement used here. It does not assert existence
of every section integral for an arbitrary absolutely integrable function
without (P18.3); no such assertion is needed in these proofs. The compact
upper/lower-integral theorem in P17.5 retains its separate full generality.
\(\square\)

### P18.5. Exact closure of Q1, Q3 and Q9

P18.2 proves all integral and differentiation passages in Q1. For Q3,
polynomial multiples of Schwartz derivatives are integrable by P18.3.
The exponential derivative and its unit modulus are proved in P15. A fixed
number of Fourier-variable derivatives therefore has a common integrable
majorant on every compact parameter set. P18.2 permits those derivatives
under the integral. For integration by parts, first fix all coordinates but
one and integrate on \([-R,R]\). The compact fundamental theorem and
product rule give the boundary term; it tends to zero by rapid decrease.
The two one-dimensional integrals converge absolutely. This gives the
section identity at every fixed remaining coordinate. The product majorants
in P18.4 then permit integration over those remaining coordinates in either
order. Repetition proves the multi-index identity in Q3. Its weighted
\(L^1\) estimate uses exactly the radial bound proved in P18.3, so it
retains the threshold \(M>N+n/2\), not a stronger substitute condition.

For Q9, the product of the locally defined phase exponential with its compactly
supported amplitude extends smoothly by zero, by P17.4. The same is true for
every iterated amplitude \(T^j a\), whose support is contained in the original
compact support: differentiation and multiplication do not enlarge support.
Choose a box with this support in its interior. Compact Fubini and the
one-dimensional product rule/fundamental theorem prove each coordinate
integration by parts, with zero boundary term. Repetition and the norm bound
give exactly (NS), using the already proved \(|e^{i\phi/h}|=1\).
The parameter estimates use finite product/chain rules and bounds on that
common compact set, as stated in Q9. Thus Q1, Q3 and Q9 have complete
selected programme proof chains. Q2, Q4 and Q6–Q8 still require the indicated
change-of-variables proofs; this companion does not close the whole lesson.
\(\square\)

## Next dependency: the actual change-of-variables proof

The free source §10.7 has been read, but its theorem is not imported yet.
Proposition 10.7.1 leaves the determinant/volume assertion to an exercise.
Theorem 10.7.2 also uses the Jordan-set and null-set image results, finite
rectangle covering, controlled subdivision, and a restriction to a
neighborhood where the Jacobian is nonzero before replacing the compact set
by surrounding rectangles. These inputs must be supplied explicitly.
The polar-coordinate and whole-line applications need their own domain and
exhaustion justification. This records the actual missing proofs rather than
turning free access to the page into mathematical clearance.
