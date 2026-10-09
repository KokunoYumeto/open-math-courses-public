# Real analysis on closed intervals

Why does a continuous curve attain an extreme value? Why does a derivative control a finite change? Why can an integral recover that change? The proofs below connect these questions through completeness and compactness.

This teaching unit follows Jiří Lebl's *Basic Analysis*, volume I, version 6.3. It is written by GPT-6 Astra (OpenAI), Ultra, in Codex, with complete intervening arguments and worked solutions. Self-checked by the writing AI. Original text: public domain (CC0). The [source and edition notice](real-analysis-source-notice.html) identifies the source passages.

## Starting point

We use the complete ordered field \(\mathbb R\) supplied by [Constructing the real numbers](constructing-the-real-numbers.html): Theorems 4 and 5 establish its field and order laws, Theorem 7 proves completeness, and Theorem 10 proves uniqueness. Completeness means that every nonempty subset bounded above has a least upper bound. For a nonempty set bounded below, define \(\inf S=-\sup(-S)\). Natural numbers, induction, rational arithmetic, sets and equivalence classes are the stated starting knowledge of that preceding unit. The construction is proved there, not assumed as an external result here.

A sequence \(x_n\) tends to \(x\) if for every \(\varepsilon>0\), eventually \(|x_n-x|<\varepsilon\). A function \(f:S\to\mathbb R\) is continuous at \(c\in S\) if for every \(\varepsilon>0\) some \(\delta>0\) makes \(|f(x)-f(c)|<\varepsilon\) whenever \(x\in S\) and \(|x-c|<\delta\). At an interval endpoint this definition uses only points in the interval. Unless explicitly stated otherwise, intervals used in differentiation have \(a<b\).

The results support [the complex exponential and the circle](complex-exponential-and-the-circle.html), and hence the programme's Cauchy and functional-calculus arguments. They do not require complex integration.

## Order, limits and completeness

**Proposition 1 (Archimedean property and rational density).** The natural numbers are unbounded above in \(\mathbb R\). For \(u<v\) there is a rational \(q\) with \(u<q<v\).

**Proof.** If \(\mathbb N\) had supremum \(s\), some \(n\in\mathbb N\) would exceed \(s-1\), and then \(n+1>s\), a contradiction. Thus, for \(x>0\) and any \(y\), some \(n\) satisfies \(nx>y\). In particular \(1/n\to0\); also \(2^{-n}\to0\), since induction gives \(2^n\geq n+1\).

Choose a positive integer \(n\) such that \(n(v-u)>1\). If \(u\geq0\), take the least positive integer \(m>nu\). It exists by unboundedness and well-ordering; its minimality gives \(m-1\leq nu\). Hence \(nu<m\leq nu+1<nv\), so \(q=m/n\) works. If \(u<0<v\), take \(q=0\). If \(u<v\leq0\), apply the nonnegative case to \(-v<-u\) and negate the resulting rational. \(\square\)

**Lemma 2 (Limit rules).** Limits are unique. Sums, products and quotients have their expected limits, provided the limiting denominator is nonzero. Inequalities pass to limits, and a sequence squeezed between two sequences with the same limit has that limit. A bounded increasing sequence converges to the supremum of its terms; a bounded decreasing sequence converges to their infimum.

**Proof.** If \(x_n\to x,y\), then \(|x-y|\leq|x-x_n|+|x_n-y|\), which can be made smaller than any positive number, forcing \(x=y\). A convergent sequence is bounded: its tail lies within distance one of its limit, and its remaining finite terms have a maximum absolute value. The estimates
\[
|(x_n+y_n)-(x+y)|\leq|x_n-x|+|y_n-y|,\qquad
|x_ny_n-xy|\leq |x_n|\,|y_n-y|+|y|\,|x_n-x|
\]
prove the sum and product rules. If \(y\ne0\), eventually \(|y_n|\geq|y|/2\), and
\[
\left|\frac1{y_n}-\frac1y\right|
\leq\frac{2|y_n-y|}{|y|^2}.
\]
This proves the reciprocal and quotient rules. If \(x_n\leq y_n\) but \(x>y\), approximation within \((x-y)/3\) contradicts that inequality. The squeeze assertion follows directly by bounding the middle sequence between \(x-\varepsilon\) and \(x+\varepsilon\).

If \(s\) is the supremum of an increasing bounded sequence, for each \(\varepsilon>0\) some \(x_N>s-\varepsilon\); then \(s-\varepsilon<x_n\leq s\) for all \(n\geq N\). Negation gives the decreasing case. These arguments also prove the corresponding function-limit rules, by replacing “eventually” with “sufficiently close to the limiting point.” \(\square\)

**Theorem 3 (Nested intervals, subsequences and Cauchy completeness).** Nonempty nested closed bounded intervals \(I_n=[a_n,b_n]\) have a common point. If \(b_n-a_n\to0\), they have exactly one common point. Every bounded real sequence has a convergent subsequence. A real sequence converges if and only if it is Cauchy.

**Proof.** Let \(c=\sup_n a_n\). Every \(b_m\) bounds all the \(a_n\): for \(n\geq m\) use nesting, and for \(n<m\) use \(a_n\leq a_m\). Thus \(a_m\leq c\leq b_m\) for every \(m\). If \(c,d\) are both common points, \(|c-d|\leq b_n-a_n\); lengths tending to zero force equality.

Place a bounded sequence inside a closed interval. Bisect it and keep a closed half containing infinitely many terms; at least one half does. Repeat, retaining nesting. At step \(k\), choose an index \(n_k>n_{k-1}\) with \(x_{n_k}\) in the retained half; infinitely many eligible indices make this possible. The intervals have lengths \(2^{-k}\) times the original length, and hence a unique common point \(c\). The same length bounds \(|x_{n_k}-c|\), proving convergence.

Convergence implies the Cauchy condition by the triangle inequality through the limit. Conversely, a Cauchy sequence has a bounded tail, since \(|x_n-x_N|<1\) for sufficiently large \(n,N\); the finitely many remaining terms preserve boundedness. Extract \(x_{n_k}\to c\). Given \(\varepsilon>0\), the Cauchy condition bounds \(|x_n-x_m|<\varepsilon/2\) for \(n,m\geq N\). Choose \(n_k\geq N\) with \(|x_{n_k}-c|<\varepsilon/2\). Then \(|x_n-c|<\varepsilon\) for every \(n\geq N\). \(\square\)

The same Cauchy conclusion holds coordinatewise in \(\mathbb R^d\) with the maximum norm. Extracting a subsequence successively in each of the finitely many coordinates proves the bounded-subsequence assertion there as well. In particular, complex Cauchy sequences converge, since a complex number is a pair of real coordinates.

## Compact intervals and continuous functions

**Theorem 4 (Finite-subcover property).** Every cover of a closed bounded interval by sets open relative to that interval has a finite subcover.

**Proof.** A one-point interval is immediate. Otherwise suppose no finite subcover exists. If both halves of the interval had finite subcovers, their union would cover the original interval; therefore one half has no finite subcover. Continue bisecting and retaining such a half. Theorem 3 gives a point \(c\) in all the retained intervals. Some member \(U\) of the original cover contains \(c\), and relative openness supplies a \(\delta>0\) such that all points of the original interval within \(\delta\) of \(c\) lie in \(U\). A retained interval of length less than \(\delta\) lies entirely in \(U\), contradicting its construction. \(\square\)

**Theorem 5 (Extreme values and uniform continuity).** A continuous real-valued function on a nonempty closed bounded interval is bounded, attains its minimum and maximum, and is uniformly continuous.

**Proof.** If \(f\) were unbounded, choose \(x_n\) with \(|f(x_n)|>n\). By Theorem 3 a subsequence tends to \(c\) in the interval. Continuity gives \(f(x_{n_k})\to f(c)\), contradicting \(|f(x_{n_k})|>n_k\).

Let \(M=\sup f([a,b])\). Choose \(x_n\) with \(M-1/n<f(x_n)\leq M\). A convergent subsequence \(x_{n_k}\to c\) again has \(c\in[a,b]\). Continuity and the squeeze rule give \(f(c)=M\). Applying this argument to \(-f\) gives a minimum.

If uniform continuity fails, some \(\varepsilon>0\) admits points \(x_n,y_n\in[a,b]\) with \(|x_n-y_n|<1/n\) and \(|f(x_n)-f(y_n)|\geq\varepsilon\). Extract \(x_{n_k}\to c\). The triangle inequality gives \(y_{n_k}\to c\) as well. Continuity then makes both image sequences tend to \(f(c)\), a contradiction. \(\square\)

**Theorem 6 (Intermediate values).** If \(f:[a,b]\to\mathbb R\) is continuous, it takes every value between \(f(a)\) and \(f(b)\). A value strictly between them is attained in \((a,b)\).

**Proof.** Subtract the desired value and, if necessary, negate; it suffices to handle \(f(a)<0<f(b)\). Bisect. A zero midpoint ends the proof. Otherwise retain the half whose endpoint values have opposite signs. The nested lengths tend to zero, so both endpoint sequences tend to the same \(c\). Continuity and the inequalities at the endpoints imply \(f(c)\leq0\) and \(f(c)\geq0\). Thus \(f(c)=0\), and \(c\) is not an original endpoint. For an endpoint value no bisection is needed. \(\square\)

Consequently \(f([a,b])=[m,M]\), with \(m,M\) its attained extrema: restrict to the interval between points attaining them and apply Theorem 6.

**Corollary 7 (Positive roots).** For each \(y>0\) and positive integer \(k\), there is exactly one \(x>0\) with \(x^k=y\).

**Proof.** The polynomial \(t^k\) is continuous by Lemma 2, and \(0^k<y< (y+1)^k\). Theorem 6 gives existence. If \(0<s<t\), then
\[
t^k-s^k=(t-s)\sum_{j=0}^{k-1}t^{k-1-j}s^j>0,
\]
so two distinct positive roots are impossible. \(\square\)

Taking \(k=2\) justifies Euclidean lengths. In a finite-dimensional real coordinate space,
\(\max_j|x_j|\leq(\sum_jx_j^2)^{1/2}\leq\sqrt d\,\max_j|x_j|\).
Thus the coordinatewise convergence and completeness above agree with the Euclidean ones, including the usual complex modulus.

## Differentiation and finite change

The derivative is the limit \(f'(c)=\lim_{h\to0}(f(c+h)-f(c))/h\). Equivalently,
\[
f(c+h)=f(c)+f'(c)h+h\,r(h),\qquad r(h)\to0.
\]
This expansion proves continuity of differentiable functions. Adding and multiplying two such expansions gives
\((f+g)'=f'+g'\) and \((fg)'=f'g+fg'\). For a nonzero value \(g(c)\), the identity
\[
\frac{1/g(c+h)-1/g(c)}h
=-\frac{(g(c+h)-g(c))/h}{g(c+h)g(c)}
\]
gives the reciprocal and quotient rules. If \(g\) is differentiable at \(c\) and \(f\) at \(g(c)\), write
\(f(g(c)+u)=f(g(c))+f'(g(c))u+u\,s(u)\), setting \(s(0)=0\).
Substitute \(u=g(c+h)-g(c)\). The quotient \(u/h\) is bounded near zero, and \(s(u)\to0\), proving the chain rule even when \(u=0\) at some nearby points. These algebraic arguments also apply to complex scalar derivatives.

**Theorem 8 (Fermat, Rolle and mean value).** A differentiable real function has derivative zero at an interior local extremum. If \(f\) is continuous on \([a,b]\) and differentiable on \((a,b)\), then some \(c\in(a,b)\) satisfies
\[
f(b)-f(a)=f'(c)(b-a).
\]
More generally, if \(g\) has the same continuity and differentiability properties, some \(c\in(a,b)\) satisfies
\[
(f(b)-f(a))g'(c)=(g(b)-g(a))f'(c).
\]
No nonvanishing assumption on \(g'\) is required for this undivided identity.

**Proof.** At an interior local maximum the difference quotients from the right are nonpositive, and those from the left are nonnegative. Their common limit is zero. Negating handles a minimum.

If \(f(a)=f(b)=K\), either \(f\) is constant or an attained maximum greater than \(K\), or an attained minimum less than \(K\), lies in the interior. Theorem 5 and the local-extremum result give \(f'(c)=0\). This is Rolle's theorem.

Apply Rolle to \(f(x)-f(a)-(x-a)(f(b)-f(a))/(b-a)\) to obtain the ordinary mean value theorem. For the general identity apply it to
\[
(f(x)-f(a))(g(b)-g(a))-(g(x)-g(a))(f(b)-f(a)),
\]
whose endpoint values are both zero. Differentiating gives the claimed identity. \(\square\)

**Corollary 9 (Derivative bounds).** On an interval, a differentiable real function with derivative zero is constant; with nonnegative derivative it is nondecreasing; with positive derivative it is strictly increasing. If \(|f'|\leq M\), then \(|f(y)-f(x)|\leq M|y-x|\).

**Proof.** Apply Theorem 8 on the closed interval between any two distinct points in the domain. Differentiability implies the continuity needed at these points, and the sign or absolute-value bound on \(f'(c)\) gives each conclusion. \(\square\)

For example, \(x^2\) is Lipschitz on each bounded interval, but not on all of \(\mathbb R\). Also, a derivative can vanish at a point without there being an extremum: \(x^3\) at zero is an example. Rolle's real-valued conclusion must not be silently transferred to vector-valued curves.

## Defining the integral by upper and lower sums

Let \(f:[a,b]\to\mathbb R\) be bounded. A partition is
\(P=(a=x_0<x_1<\cdots<x_n=b)\). Put
\[
L(P,f)=\sum_i\inf_{[x_{i-1},x_i]}f\,(x_i-x_{i-1}),\qquad
U(P,f)=\sum_i\sup_{[x_{i-1},x_i]}f\,(x_i-x_{i-1}).
\]
Define the lower integral as \(\sup_P L(P,f)\) and the upper integral as \(\inf_P U(P,f)\). If these are equal, their common value is the Riemann integral \(\int_a^b f\). Integrals over a one-point interval are zero.

**Proposition 10 (Darboux criterion and elementary operations).** The lower integral never exceeds the upper integral. A bounded \(f\) is integrable if and only if for every \(\varepsilon>0\) some partition has \(U(P,f)-L(P,f)<\varepsilon\). Integrable functions form a real vector space, integration is linear and preserves order, and
\[
\left|\int_a^b f\right|\leq M(b-a)\quad\text{if }|f|\leq M.
\]
An integrable function is integrable on every subinterval, and the integral is additive over adjacent intervals. Conversely, integrability on finitely many adjacent subintervals implies integrability on their union.

**Proof.** A refinement raises the lower sum and lowers the upper sum: on every smaller interval its infimum is at least the old infimum and its supremum is at most the old supremum, while lengths add. For arbitrary \(P,Q\), their common refinement gives \(L(P,f)\leq U(Q,f)\). Taking supremum and infimum proves the first assertion. All sums lie between \(m(b-a)\) and \(M(b-a)\) if \(m\leq f\leq M\), so these suprema and infima are finite.

If the two integrals agree, select one lower sum and one upper sum within \(\varepsilon/2\) of their common value and refine both partitions. This gives the criterion. Conversely, their nonnegative difference is at most \(U(P,f)-L(P,f)\), proving equality when the criterion holds.

For integrable \(f,g\), choose a common partition with each oscillation sum \(U-L\) arbitrarily small. On each interval, the oscillation of \(f+g\) is at most the sum of their oscillations; thus the criterion proves integrability of \(f+g\). Moreover
\[
L(P,f)+L(P,g)\leq L(P,f+g)
\leq U(P,f+g)\leq U(P,f)+U(P,g).
\]
The outer quantities can be made arbitrarily close to \(\int f+\int g\), proving additivity. Positive scalar multiplication multiplies both sums; negative multiplication interchanges upper and lower sums with the corresponding sign. This proves homogeneity. Constants integrate to their value times length. If \(f\leq g\), then \(L(P,f)\leq L(P,g)\) for every partition, and taking suprema proves order preservation. Apply this to the constants \(-M,M\) to obtain the displayed bound.

For \(c\in(a,b)\), refine by inserting \(c\). Lower and upper sums then split into the sums on \([a,c]\) and \([c,b]\); their two nonnegative oscillation sums add. If the whole oscillation can be made arbitrarily small, so can each part. Conversely, unite partitions with small oscillations on the two parts. The criterion proves both directions of integrability; approximation by their lower and upper sums proves
\(\int_a^b f=\int_a^c f+\int_c^b f\). Induction proves the finite-partition version. Applying this twice proves restriction to any subinterval. \(\square\)

For \(x<y\) define \(\int_y^x f=-\int_x^y f\). The adjacent-interval identity then gives \(\int_x^z f=\int_x^y f+\int_y^z f\) in every ordering of the three points.

**Theorem 11 (Continuous and piecewise-continuous functions).** Every continuous real function on \([a,b]\) is Riemann integrable. More generally, every bounded real function on \([a,b]\) with only finitely many possible discontinuities is integrable.

**Proof.** By Theorem 5 a continuous \(f\) is bounded and uniformly continuous. Given \(\varepsilon>0\), choose \(\delta>0\) making its oscillation on any interval of length less than \(\delta\) at most \(\varepsilon/(2(b-a))\). Choose an equal partition of such mesh, possible by Proposition 1. Its total oscillation sum is at most \(\varepsilon/2\), so Proposition 10 applies.

For the more general assertion let \(|f|\leq M\); the case \(M=0\) is immediate. Surround the finitely many exceptional points by a finite union of relative open intervals of total length less than \(\varepsilon/(4M)\), with endpoints that are not exceptional unless they are endpoints of \([a,b]\). On their closed complementary intervals \(f\) is continuous, hence integrable by the first part. Choose partitions there whose total oscillation contribution is less than \(\varepsilon/2\). Insert all the endpoints of the exceptional intervals and join the partitions. The exceptional intervals contribute at most \(2M\) times their total length, less than \(\varepsilon/2\). Thus \(U-L<\varepsilon\). \(\square\)

The same estimate shows that altering a bounded function at finitely many points does not change its integral: the difference vanishes away from those points, is integrable by Theorem 11, and has integral arbitrarily small in absolute value by surrounding them with intervals of arbitrarily small total length.

## The two directions of the fundamental theorem

**Theorem 12 (Integrating a derivative).** Let \(F:[a,b]\to\mathbb R\) be continuous and differentiable on \((a,b)\). Suppose \(f\) is Riemann integrable and \(f(x)=F'(x)\) for \(a<x<b\). Then
\[
\int_a^b f(x)\,dx=F(b)-F(a).
\]
The conclusion still holds when equality and differentiability are required only outside a finite subset of \((a,b)\), provided \(F\) remains continuous everywhere.

**Proof.** For a partition \(P\), Theorem 8 supplies \(c_i\in(x_{i-1},x_i)\) such that
\[
F(x_i)-F(x_{i-1})=f(c_i)(x_i-x_{i-1}).
\]
Summing and bounding each term by its infimum and supremum gives
\[
L(P,f)\leq F(b)-F(a)\leq U(P,f).
\]
Take the supremum of the lower sums and infimum of the upper sums. Their equality proves the formula. If there are finitely many exceptional points, insert them as partition endpoints. Apply the proved formula on each closed piece, using Proposition 10 for restriction and additivity; the increments of the continuous \(F\) telescope. Values of \(f\) at the partition endpoints are immaterial. \(\square\)

**Theorem 13 (Differentiating an integral).** Let \(f:[a,b]\to\mathbb R\) be Riemann integrable and \(d\in[a,b]\). Define \(F(x)=\int_d^x f(t)\,dt\). If \(|f|\leq M\), then \(F\) is Lipschitz with constant \(M\). At each interior continuity point \(c\) of \(f\), \(F'(c)=f(c)\). At an endpoint the same formula holds for the derivative from within the interval when \(f\) is continuous there.

**Proof.** Additivity and the integral bound give
\[
|F(x)-F(y)|=\left|\int_y^x f\right|\leq M|x-y|.
\]
Fix a continuity point \(c\). Given \(\varepsilon>0\), choose \(\delta>0\) so that \(|f(t)-f(c)|<\varepsilon\) for all interval points with \(|t-c|<\delta\). If \(0<|x-c|<\delta\), linearity, orientation and the same integral bound imply
\[
\left|\frac{F(x)-F(c)}{x-c}-f(c)\right|
=\frac1{|x-c|}\left|\int_c^x(f(t)-f(c))\,dt\right|
\leq\varepsilon.
\]
Using \(\varepsilon/2\) for an arbitrary requested tolerance gives the derivative definition. This works from either side at an interior point, and from the available side at an endpoint. \(\square\)

Complex-valued continuous integrands are integrated by their real and imaginary parts. Linearity and both fundamental-theorem conclusions then hold componentwise. There is no claim that the real mean value equality holds with a single intermediate point for a complex-valued function.

## Examples, exercises and worked solutions

**Exercise 1.** Prove that changing the endpoints of an interval changes the extreme-value question. Give a continuous bounded function on an open bounded interval that does not attain either extremum.

**Solution.** The function \(f(x)=x\) on \((0,1)\) has infimum zero and supremum one, but neither belongs to its image. On \([0,1]\) it attains both. Thus boundedness of the function alone cannot replace closedness of the domain.

**Exercise 2.** Give a guaranteed enclosure of width at most \(2^{-n}\) for the positive solution of \(x^3=2\), starting from \([1,2]\). Explain why the solution is unique.

**Solution.** The endpoint values of \(x^3-2\) are negative and positive. At each step evaluate the midpoint, stopping if it is zero and otherwise retaining the sign-changing half as in Theorem 6. After \(n\) steps the interval has width \(2^{-n}\) and still contains a zero. The positive-root uniqueness proof in Corollary 7 shows it is the same zero at every stage. A midpoint approximation therefore has error at most \(2^{-n-1}\).

**Exercise 3.** Let \(f(x)=|x|\) on \([-1,1]\). Why is it not a counterexample to Rolle's theorem? Compute \(\int_{-1}^1 g\), where \(g=-1\) on \([-1,0)\), \(g=1\) on \((0,1]\), and \(g(0)\) is any real number.

**Solution.** The difference quotient of \(f\) at zero is \(-1\) from the left and \(1\) from the right, so the differentiability condition fails there. The function \(g\) is bounded with only one possible discontinuity. Theorem 12 with the single exceptional point zero gives \(\int_{-1}^1g=f(1)-f(-1)=0\). The arbitrary value at zero does not affect the integral.

**Exercise 4.** Suppose \(f\) is Riemann integrable and \(F(x)=\int_a^x f\). Does differentiability of \(F\) at \(c\) imply continuity of \(f\) there?

**Solution.** No. On \([-1,1]\), let \(f(0)=1\) and \(f(x)=0\) elsewhere. The finite-point observation after Theorem 11 shows that all its integrals vanish. Thus \(F\) is identically zero and differentiable everywhere, although \(f\) is discontinuous at zero. This also shows why \(F'(c)=f(c)\) in Theorem 13 is asserted at continuity points.

**Exercise 5.** If \(F,G\) are differentiable on an interval, have equal derivatives, and agree at one point, prove they agree everywhere. If a continuously differentiable \(F\) has \(m\leq F'\leq M\) on \([a,b]\), bound its increment.

**Solution.** The derivative of \(F-G\) vanishes, so Corollary 9 makes the difference constant; its value at the specified point is zero. For the increment, either Theorem 8 or Theorem 12 and order preservation gives
\[
m(b-a)\leq F(b)-F(a)\leq M(b-a).
\]
The first argument actually needs only continuity on the closed interval and differentiability in its interior, with the derivative bounds there; continuity of the derivative is unnecessary.

## Sources and onward study

Jiří Lebl, [*Basic Analysis: Introduction to Real Analysis*](https://www.jirka.org/ra/), volume I, version 6.3, provides the real-number, sequence, continuity, differentiation and integration material used in this unit. Its source is supplied in editable LaTeX. The [edition notice](real-analysis-source-notice.html) records the exact source passages.

Author's editable chapters: [real numbers](https://raw.githubusercontent.com/jirilebl/ra/v6.3/ch-real-nums.tex), [sequences](https://raw.githubusercontent.com/jirilebl/ra/v6.3/ch-seq-ser.tex), [continuous functions](https://raw.githubusercontent.com/jirilebl/ra/v6.3/ch-contfunc.tex), [differentiation](https://raw.githubusercontent.com/jirilebl/ra/v6.3/ch-der.tex), and [Riemann integration](https://raw.githubusercontent.com/jirilebl/ra/v6.3/ch-riemann.tex).

Continue with [the complex exponential and the circle](complex-exponential-and-the-circle.html). Theorems 12 and 13 distinguish the two directions of calculus; keeping those directions separate is equally important in later complex and operator-valued integration.
