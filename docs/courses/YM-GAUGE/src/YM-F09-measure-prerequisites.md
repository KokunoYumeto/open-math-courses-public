# Measure, integration and complete function spaces

*Original proof sections by GPT-6.1 Sol (OpenAI) and GPT-6 Astra
(OpenAI), under CC0. The writing AIs self-checked these sections;
independent human review is not claimed.*

These are the selected measure and Euclidean-product sections of
the exact AN-06 provider edition, source lines
29–104 and 186–204. The component proves outer measure,
integration convergence, Hölder, complete function spaces,
Euclidean measure and the needed product theorem.
Its scalar power prerequisite is included in the
[companion component](../analysis-scalar-prerequisites.html).
The teaching prerequisites are the course's stated real arithmetic
and one-variable calculus.

The spectral-measure and operator-quantization sections of the
original component are outside this selection. The editorial
provenance sentence about an earlier AN03 version is omitted;
no mathematical step in the selected sections is omitted.
The single prerequisite link is directed to the bundled component.

<a id="measure-foundations"></a>

## Measure construction, convergence and complete function spaces

An outer measure on a set $S$ is a monotone function $m^*:2^S\to[0,\infty]$, zero at the empty set, with $m^*(\bigcup_j A_j)\le\sum_jm^*(A_j)$. A set $E$ is called measurable for this construction when

\[
 m^*(A)=m^*(A\cap E)+m^*(A\setminus E)\qquad(A\subset S).
\]

It suffices to prove the greater-than-or-equal inequality: subadditivity gives the reverse, and the desired inequality is automatic when $m^*(A)=\infty$.

<a id="outer-measure-construction"></a>

**Outer-measure lemma.** These measurable sets form a sigma-algebra, and restriction of $m^*$ to it is a complete measure.

**Proof.** The empty set and complements have the required property. Split $A$ by two measurable sets $E,F$ in succession. The resulting three pieces show

\[
 m^*(A)\ge m^*(A\cap(E\cup F))+m^*(A\setminus(E\cup F)),
\]

using subadditivity on the pieces inside $E\cup F$. Thus finite unions, intersections and differences are measurable. For disjoint measurable $E_j$, finite splitting gives

\[
 m^*(A)\ge\sum_{j=1}^k m^*(A\cap E_j)+m^*(A\setminus\textstyle\bigcup_j E_j).
\]

Let $k\to\infty$ and apply subadditivity to $A\cap\bigcup_jE_j$. This proves measurability of the disjoint union. An arbitrary union is disjointified by removing all earlier sets, proving the sigma-algebra assertion. Taking $A=\bigcup_jE_j$ in the finite inequality, and then using subadditivity, proves countable additivity. If $m^*(N)=0$, every subset $Z\subset N$ satisfies the splitting equality: its first piece has measure zero, and monotonicity and subadditivity make the second piece have measure $m^*(A)$. This proves completeness. $\square$

<a id="simple-integral-construction"></a>

Here a sigma-algebra contains the whole set and is closed under complements and countable unions; a measure is countably additive on disjoint sets and zero at the empty set. On a measure space $(S,\Sigma,\mu)$, a real function is measurable when all its strict upper level sets belong to $\Sigma$; a complex function is measurable when its real and imaginary parts are. A nonnegative simple function is a finite sum $s=\sum_jc_j1_{E_j}$ on disjoint measurable sets, with finite $c_j\ge0$. Define $\int s=\sum_jc_j\mu(E_j)$, with $0\cdot\infty=0$. A common finite partition proves that this definition is independent of the representation, additive and order preserving. For measurable $f\ge0$ define $\int f$ as the supremum of $\int s$ over simple $0\le s\le f$. The functions $2^{-k}\lfloor2^k\min(f,k)\rfloor$ are increasing finite-valued measurable functions with limit $f$. Countable suprema and limits are measurable because their strict level sets are countable unions and intersections of level sets. Countable additivity also gives continuity from below for sets: disjointify an increasing union and sum its measures.

<a id="scalar-measurability"></a>

**Scalar and measurability details.** We use ordered-real completeness and elementary field operations. Completeness implies the Archimedean property: if the positive integers had supremum $a$, some integer would exceed $a-1$, and its successor would exceed $a$. Hence positive rational meshes can be arbitrarily small, and every nonempty real open interval contains a rational number. It follows that open subsets of $\mathbb R^d$ are countable unions of rational open rectangles: around each point choose a sufficiently small rectangle contained in the given open neighbourhood. The countability follows because finite tuples of integers form a countable set, by enumerating tuples whose entries have bounded absolute value.

For completeness, the nonnegative square root uses no calculus. For $r\ge0$, the set $\{t\ge0:t^2\le r\}$ is nonempty and bounded by $r+1$. Its supremum $s$ satisfies $s^2=r$: if $s^2<r$, a sufficiently small positive increment still has square less than $r$, contradicting the upper bound; if $s^2>r$, a sufficiently small decrement remains an upper bound, contradicting the supremum. These choices follow by expanding $(s\pm h)^2$; the zero case is immediate. Uniqueness follows from strict increase of the square on nonnegative reals. The identity $|s^2-t^2|=|s-t|(s+t)\ge|s-t|^2$ proves continuity of this root. Finite sums and products are continuous by the identities for their differences, with the factors bounded in a small neighbourhood. Thus complex conjugation and modulus, and real maxima, minima and positive and negative parts, are continuous as well. Here $\max(a,b)=(a+b+|a-b|)/2$. The complex triangle inequality follows by expanding $|z+w|^2$ and using $\operatorname{Re}(z\overline w)\le|z||w|$; the latter follows from $\operatorname{Re}u\le|u|$ and $|z\overline w|=|z||w|$.

If $f_1,\ldots,f_d$ are finite real measurable functions and $H:\mathbb R^d\to\mathbb R$ is continuous, then $H(f_1,\ldots,f_d)$ is measurable. Indeed, the preimage under $H$ of a strict upper interval is open and is therefore a countable union of rational rectangles. The preimage of each rectangle under $(f_1,\ldots,f_d)$ is a finite intersection of measurable interval preimages. This proves all the finite algebra and modulus operations on measurable functions used in integration below.

The assertions about sequences follow directly from level sets, including extended values. For example $\{\sup_j f_j>a\}=\bigcup_j\{f_j>a\}$, whereas $\{\inf_j f_j>a\}$ is the union, over rational $q>a$, of $\bigcap_j\{f_j\ge q\}$. Complements convert strict upper to weak lower sets and conversely. Infima, suprema, liminf and limsup are consequently measurable, as are pointwise limits when they exist. Also $\{f<h\}=\bigcup_{q\in\mathbb Q}\{f<q\}\cap\{h>q\}$, which proves measurability of the comparisons used below. For nonnegative extended $f$, the dyadic approximations in the preceding paragraph are measurable because their level sets are interval preimages. Refining the dyadic grid and increasing the cutoff proves that they increase; once $k>f(x)$ their error is less than $2^{-k}$, and when $f(x)=\infty$ their value is $k$. Thus they converge pointwise in both cases.

<a id="monotone-integral-and-convergence"></a>

**Convergence lemma.** If $0\le f_j\uparrow f$ almost everywhere, then $\int f_j\uparrow\int f$. If $f_j\ge0$, then $\int\liminf_jf_j\le\liminf_j\int f_j$. If $u_j\to u$ almost everywhere, the functions are complex measurable, and $|u_j|\le g$ for one integrable $g\ge0$, then $\int|u_j-u|\to0$.

**Proof.** Integrals over a measurable null set vanish by the simple-function definition, so remove the exceptional set first. In the increasing case, fix simple $s\le f$ and $0<c<1$. The sets $E_j=\{f_j\ge cs\}$ increase and cover $\{s>0\}$. Continuity from below on the finitely many levels of $s$ yields $\int s1_{E_j}\uparrow\int s$. Since $f_j\ge cs1_{E_j}$, the limit of their integrals is at least $c\int s$. Let $c\uparrow1$ and take the supremum over $s$. Monotonicity supplies the opposite inequality, including infinite integrals.

Apply this conclusion to increasing simple approximations of two functions and to their sum. It proves additivity of nonnegative integration, and then $\int\sum_jv_j=\sum_j\int v_j$ for $v_j\ge0$. Define integrals of absolutely integrable real functions by their positive and negative parts, and complex integrals by real and imaginary parts. Nonnegative additivity proves linearity. Multiplying an integral by a complex scalar of modulus one that makes it nonnegative real shows $|\int u|\le\int|u|$.

For Fatou, the functions $\inf_{j\ge k}f_j$ increase to the liminf and have integral at most $\inf_{j\ge k}\int f_j$; use the increasing case. In the dominated case, $|u|\le g$ almost everywhere and all differences are integrable. Apply Fatou to $2g-|u_j-u|\ge0$. Their pointwise limit is $2g$, so

\[
 2\int g\le 2\int g-\limsup_j\int|u_j-u|.
\]

The integral of $g$ is finite; subtract it to conclude. The integral inequality above also proves $\int u_j\to\int u$. $\square$

<a id="complete-function-spaces"></a>

For finite $p\ge1$ set $\|f\|_p=(\int|f|^p)^{1/p}$, and let $\|f\|_\infty$ be the infimum of bounds for $|f|$ outside measurable null sets. The space $L^p(\mu)$ consists of functions with finite such quantity, modulo almost-everywhere equality. A finite essential bound equal to the infimum is attained: choose the bounds $\|f\|_\infty+1/j$ outside their measurable null sets and discard the countable union of those sets. On the complement let $j\to\infty$. In particular essential norm zero means vanishing almost everywhere.

**Function-space lemma.** For $1\le p\le\infty$, $L^p(\mu)$ is a complete normed space. For finite $p$, simple functions supported on sets of finite measure are dense. Hölder's inequality holds for conjugate exponents, and $L^2$ is a Hilbert space with inner product $(f,h)=\int f\overline h$.

For the Hilbert-space case $p=q=2$, the scalar inequality needed below is $ab\le(a^2+b^2)/2$, obtained by expanding $(a-b)^2\ge0$. Thus the $L^2$ norm, completeness and density arguments below use only the scalar and integration facts already proved, without a differentiation input. The endpoint cases $p=1,\infty$ likewise use only those facts. The proof also retains the full range of exponents. For the general real exponents, first read the [logarithm, real-power and Young proofs (EF6)–(EF8)](../analysis-scalar-prerequisites.html#logarithm-and-real-powers). Their scalar integral input uses only the preceding measure facts, not the function-space lemma.

**Proof.** For $1<p<\infty$ put $q=p/(p-1)$. The function $a^p/p-ab+b^q/q$, for fixed $b>0$, decreases until $a=b^{1/(p-1)}$ and increases thereafter, since its derivative is $a^{p-1}-b$. Its value at that minimum is zero. Continuity handles $a=0$ or $b=0$. Thus $ab\le a^p/p+b^q/q$. Apply this inequality to $|f|/\|f\|_p$ and $|h|/\|h\|_q$ and integrate to obtain $\int|fh|\le\|f\|_p\|h\|_q$. A zero norm implies vanishing almost everywhere, since each set where the modulus exceeds $1/j$ then has measure zero. Infinite positive norms make the inequality automatic. The endpoint cases follow by bounding the essentially bounded factor outside a null set. In particular $p=q=2$ gives Cauchy–Schwarz.

The inequality $(a+b)^p\le2^p(a^p+b^p)$ first ensures that the sum of two $L^p$ functions is in $L^p$. For $1<p<\infty$, apply Hölder to $|f|\,|f+h|^{p-1}$ and $|h|\,|f+h|^{p-1}$. It follows that

\[
 \|f+h\|_p^p\le(\|f\|_p+\|h\|_p)\|f+h\|_p^{p-1}.
\]

Division proves the triangle inequality when the sum has positive norm; the zero case is immediate. For $p=1,\infty$ use the pointwise triangle inequality. Homogeneity and definiteness on equivalence classes now give a norm.

Let $f_j$ be Cauchy in that norm, with $p<\infty$. Choose indices $j_k$ so that $\|f_{j_{k+1}}-f_{j_k}\|_p\le2^{-k}$. The partial sums of $v=\sum_k|f_{j_{k+1}}-f_{j_k}|$ have norms at most $\sum_k2^{-k}$. Monotone convergence of their $p$th powers implies $v\in L^p$, so the subsequence converges pointwise outside a measurable null set to a finite measurable $f$. Define $f=0$ on that set. The same argument applied to each tail gives

\[
 \|f-f_{j_k}\|_p\le\sum_{l\ge k}2^{-l}.
\]

In particular $f\in L^p$. The Cauchy property and the triangle inequality extend convergence from the subsequence to the entire sequence. For $p=\infty$, remove the null sets on which the chosen differences violate the same bounds, as well as the null set on which the first term violates an essential bound. The series of differences converges uniformly on the complement, to a bounded measurable limit; its uniform tail bound gives convergence in $L^\infty$.

Finally, if $f\in L^p$ with $p<\infty$, the sets $E_j=\{1/j<|f|\le j\}$ increase to its nonzero set, up to a null set, and $\mu(E_j)\le j^p\|f\|_p^p$. Dominated convergence gives $f1_{E_j}\to f$ in $L^p$. Partition a bounded region of the complex plane into squares of arbitrarily small side length to approximate $f1_{E_j}$ uniformly by finite-valued measurable functions, zero outside $E_j$. Their $L^p$ error is bounded by the uniform error times $\mu(E_j)^{1/p}$. This proves density. For $p=2$, Cauchy–Schwarz, linearity and conjugation of the integral verify the inner-product axioms, and completeness was just proved. $\square$

<a id="euclidean-products"></a>

## Euclidean measure and the product theorem used below

In $\mathbb R^d$ cover a set by countably many bounded open axis-parallel rectangles and take the infimum of the sums of their volumes. The empty set and monotonicity properties are immediate. Combining covers with summable errors proves countable subadditivity; if the sum of outer measures is infinite there is no inequality to check. The splitting inequality for a coordinate half-space can be seen directly. For $H=\{x:x_i<a\}$, split a covering open rectangle crossing the hyperplane into its left open part and an open rectangle containing its right part, extending that second rectangle to $x_i>a-\delta$. The sum of their volumes exceeds the original volume by at most $\delta$ times the product of the other side lengths. Rectangles not crossing the hyperplane need no split. Choose the enlargements so that their total excess is below any prescribed $\varepsilon>0$. These rectangles cover the two parts of the set in question. For a set of finite outer measure, take a cover whose volume sum is within $\varepsilon$ of its outer measure, and let $\varepsilon$ tend to zero; an infinite outer measure makes the desired inequality automatic. Thus every coordinate half-space satisfies the outer-measure splitting criterion. Complements, finite intersections and countable unions of these half-spaces give every open set: each open set is the union of the rational rectangles contained in it. Thus the preceding outer-measure lemma makes all Borel sets measurable and supplies a complete measure.

A closed bounded rectangle has its usual volume. Enlargement gives the upper bound. For the lower bound, a cover by open rectangles has a finite subcover. Here is the needed compactness argument: if a closed box had no finite subcover, subdivision into $2^d$ equal boxes would leave one box without such a subcover. Iterate; the nested coordinate intervals have lengths tending to zero and, by real completeness, one common point. An open set of the cover containing that point contains an entire sufficiently small box, a contradiction. For the finite cover now obtained, draw the grid of all its coordinate endpoints and the target endpoints. The interior of each grid cell in the target lies wholly in any covering rectangle that contains its midpoint. Assign each cell to one such rectangle. Finite distributivity of products of interval lengths shows that the sum of the cell volumes is the target volume and that the sum assigned to each covering rectangle is at most its volume. This proves the lower bound without a product-integration assumption. Bounded faces have measure zero by arbitrarily thin rectangle covers. Translation invariance follows by translating covers and translating back. Increasing bounded boxes give sigma-finiteness.

We will also need the exact relation with Borel sets. If a measurable $E$ has finite measure, choose open rectangle unions $O_j\supset E$ with $\mu(O_j)\le\mu(E)+2^{-j}$. Their intersection $G$ is Borel and contains $E$, with $\mu(G\setminus E)=0$. Every set of outer measure zero is contained in a Borel null set: intersect open rectangle unions of total volumes tending to zero. Thus $E$ differs from a Borel set by a subset of a Borel null set. For general $E$, apply this argument to its intersections with bounded boxes and take the union of the resulting Borel sets and null envelopes. This proves the same assertion without a finite-measure hypothesis. Conversely, the completeness already proved makes every such modification measurable.

Here is the product argument without importing an interchange rule. Restrict first to two bounded boxes $B\subset\mathbb R^r$, $C\subset\mathbb R^s$. For a Borel rectangle $E=E_1\times E_2$ whose two factors are axis rectangles, its sections are measurable and

\[
 \mu_{r+s}(E)=\int_B\mu_s(E_x)\,d\mu_r(x).
\]

Let $\mathcal D$ be the class of Borel subsets of $B\times C$ for which this equality holds and $x\mapsto\mu_s(E_x)$ is measurable. Sections of Borel sets are Borel: for each fixed $x$, taking a section preserves complements and countable unions and sends generating rectangles to Borel sets. The class $\mathcal D$ contains the whole box and the generating axis rectangles. It is closed under complements in the whole box, by subtracting from the finite constant $\mu_s(C)$ and the finite total measure; it is closed under countable disjoint unions, by the monotone convergence theorem just proved applied to the nonnegative section measures. Thus it is a Dynkin class. The elementary pi-lambda argument shows that it contains the sigma-algebra generated by the rectangles. To recall that argument, take the smallest Dynkin class containing a family closed under finite intersections. For a fixed generator the class of sets whose intersection with it belongs to that smallest class is a Dynkin class; this proves intersections first with generators, and by repeating the argument with a fixed member, between any two members. A Dynkin class closed under finite intersections is a sigma-algebra, since differences and then disjointification give countable unions. This proves the claim.

Increasing the boxes proves the section formula for every Borel set in the full product. For a completed measurable set, enclose its null difference from a Borel set in a Borel null set. The section formula for that enclosing null set makes its sections null for almost every $x$; completeness then gives the same formula and measurability after one null exceptional set is discarded. This also applies to every completed-measurable function: outside a product null set it has a Borel representative, obtained by choosing Borel representatives of the level sets in a countable simple approximation. The section formula for indicators extends by simple approximation and monotone convergence to every nonnegative function. Applying it to the absolute value and then positive/negative real and imaginary parts gives Fubini for absolutely integrable complex functions. These are exactly all the product interchanges in this proof.

The finite-measure approximation used for Schwartz density follows from this construction too: choose an open rectangle cover of $E$ whose total volume is at most $\mu(E)+\varepsilon$. Its union differs from $E$ by measure at most $\varepsilon$. Finite truncations approximate the union in measure by continuity from below. A finite union of boxes therefore approximates $E$ in measure.

