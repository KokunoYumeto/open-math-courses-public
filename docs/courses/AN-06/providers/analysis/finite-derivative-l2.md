# A finite-derivative bound for left quantization

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


<a id="finite-derivative-l2"></a>
## The exact bound

Let $n\geq1$ and let $N$ be an integer with $N>n/2$. For $a\in C^\infty(\mathbb R^n_x\times\mathbb R^n_\xi)$ put
\[
 M_N(a)=\max_{|\alpha|\leq2N,\ |\beta|\leq2N}
 \sup_{x,\xi}|\partial_x^\alpha\partial_\xi^\beta a(x,\xi)|.
\]
If $M_N(a)<\infty$, the left operator
\[
 A u(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi,
 \qquad \widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx,
 \tag{1}
\]
initially on Schwartz functions, has a unique bounded extension to $L^2(\mathbb R^n)$ and
\[
 \|A\|_{L^2\to L^2}\leq C_{n,N}M_N(a).
 \tag{2}
\]
In particular derivatives of total order at most $4N$ suffice. There is no condition on a Hessian, positivity, ellipticity, support, or a lower bound of a symbol. The same constant works for a family with the displayed seminorm bounded uniformly. For $n=0$, (1) is scalar multiplication and the assertion is immediate.

The measure inputs are monotone and dominated convergence, Fatou, Cauchy–Schwarz, $L^2$ completeness, and the product interchange theorem for Euclidean Lebesgue measure. The following subsections prove these inputs directly. For comparison, Sheldon Axler's free author text [*Measure, Integration & Real Analysis*, 12 June 2026](https://measure.axler.net/MIRA.pdf), §§3A–3B and §§7A–7B, supplies the integration and $L^p$ route; D. H. Fremlin's [free author sources for *Measure Theory*, Volume 1, 2011 edition](https://www1.essex.ac.uk/maths/people/fremlin/mt1.2011/index.htm), 113C and 115B, 115D–115F, supply the outer-measure and rectangle construction. In particular the dominated-convergence proof below uses Fatou directly, and the rectangle-volume proof uses a finite grid. These references do not replace any step below.

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

For the Hilbert-space case $p=q=2$, the scalar inequality needed below is $ab\le(a^2+b^2)/2$, obtained by expanding $(a-b)^2\ge0$. Thus the $L^2$ norm, completeness and density arguments below use only the scalar and integration facts already proved, without a differentiation input. The endpoint cases $p=1,\infty$ likewise use only those facts. The proof also retains the full range of exponents. For the general real exponents, first read the [logarithm, real-power and Young proofs (EF6)–(EF8)](elementary-functions-and-cutoffs.md#logarithm-and-real-powers). Their scalar integral input uses only the preceding measure facts, not the function-space lemma.

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


<a id="general-product-measures"></a>
## Products with a spectral measure

A scalar spectral measure is a finite Borel measure; it need not be Lebesgue measure or have a density. The following construction therefore allows arbitrary sigma-finite measures. Its only integration inputs are the simple integral and monotone convergence proved above. Neither a spectral theorem nor Fourier analysis is used here.

Let $(X,\Sigma,\mu)$ and $(Y,\mathcal T,\nu)$ be measure spaces. The product sigma-algebra $\Sigma\otimes\mathcal T$ is the smallest sigma-algebra containing the rectangles $A\times B$ with $A\in\Sigma$ and $B\in\mathcal T$. For $E\subset X\times Y$, put $E_x=\{y:(x,y)\in E\}$ and $E^y=\{x:(x,y)\in E\}$. We first prove the set-generation argument needed to construct the product.

<a id="pi-lambda-uniqueness"></a>

**Set-generation and uniqueness lemma.** A family $\mathcal P$ containing its whole underlying set and closed under finite intersections generates a sigma-algebra. Every family containing $\mathcal P$, closed under complements and countable disjoint unions, contains that sigma-algebra. Consequently two finite measures agreeing on $\mathcal P$ agree on the generated sigma-algebra.

**Proof.** Call a family containing the whole set and closed under complements and countable disjoint unions a lambda-system. It is closed under differences of nested members: if $A\subset B$ belong to it, then $B\setminus A$ is the complement of the disjoint union $A\cup B^c$. Let $\mathcal D$ be the intersection of all lambda-systems containing $\mathcal P$; intersections preserve the defining properties.

For $A\in\mathcal D$, the members $B\in\mathcal D$ for which $A\cap B\in\mathcal D$ form a lambda-system. The whole set belongs because $A\in\mathcal D$; complements follow from the nested-difference property applied inside $A$; disjoint unions follow by intersecting their disjoint pieces with $A$. If $A\in\mathcal P$, this system contains $\mathcal P$, hence contains $\mathcal D$ by minimality. Thus $A\cap B\in\mathcal D$ whenever $A\in\mathcal P$ and $B\in\mathcal D$. Fixing instead any $A\in\mathcal D$, symmetry now shows that its system also contains $\mathcal P$, hence all of $\mathcal D$. Therefore $\mathcal D$ is closed under intersections, complements and finite unions. Disjointifying a countable union using finite unions and differences proves that $\mathcal D$ is a sigma-algebra. This proves the first assertion.

For finite measures with equal total mass, the sets on which their values agree form a lambda-system: complements use subtraction from that finite total, and disjoint unions use countable additivity. Agreement on $\mathcal P$ includes the total mass and therefore implies agreement everywhere on its generated sigma-algebra. $\square$

<a id="section-measurability"></a>

**Section lemma.** If $E\in\Sigma\otimes\mathcal T$, all its sections are measurable. If $\nu$ is sigma-finite, then $x\mapsto\nu(E_x)$ is $\Sigma$-measurable. If $\mu$ is sigma-finite, then $y\mapsto\mu(E^y)$ is $\mathcal T$-measurable.

**Proof.** For a rectangle, each section is either the corresponding factor or the empty set. Taking a section commutes with complements and countable unions. The sets with measurable sections therefore form a sigma-algebra containing the rectangles.

First suppose $\nu(Y)<\infty$. The product-measurable sets $E$ for which $x\mapsto\nu(E_x)$ is measurable form a lambda-system. For complements the section measure is $\nu(Y)-\nu(E_x)$; for disjoint unions it is the sum of the nonnegative measurable section measures. On a rectangle it is $\nu(B)1_A(x)$. Rectangles form an intersection-closed family containing $X\times Y$, so the set-generation lemma proves the assertion.

For sigma-finite $\nu$, choose a measurable disjoint partition $Y=\bigcup_j C_j$ with $\nu(C_j)<\infty$: disjointify any countable cover of finite measure. The measures $\nu_j(B)=\nu(B\cap C_j)$ are finite on $Y$. The finite case and countable additivity give
\[
 \nu(E_x)=\sum_j\nu_j(E_x).
 \tag{MP1}
\]
This is a measurable function, possibly infinite. Interchanging the roles of $X$ and $Y$ proves the other assertion. $\square$

<a id="product-measure-construction"></a>

**Product-measure lemma.** For sigma-finite $\mu,\nu$, there is exactly one measure $m$ on $\Sigma\otimes\mathcal T$ satisfying $m(A\times B)=\mu(A)\nu(B)$, with $0\cdot\infty=0$. It is sigma-finite, and
\[
 \begin{aligned}
 m(E)&=\int_X\nu(E_x)\,d\mu(x)\\
     &=\int_Y\mu(E^y)\,d\nu(y).
 \end{aligned}
 \tag{MP2}
\]

**Proof.** Define $m$ by the first integral, which is defined by the section lemma. It is zero at the empty set. Sections of disjoint sets are disjoint; countable additivity of $\nu$ and monotone convergence for the sum then prove countable additivity of $m$. On a rectangle the integrand is $\nu(B)1_A$, giving the claimed value, including zero and infinite cases by the definition of nonnegative integration. Reversing the order defines another measure $\widetilde m$ with the same rectangle values.

Choose disjoint finite-measure partitions $X=\bigcup_i D_i$ and $Y=\bigcup_j C_j$. On each measurable block $D_i\times C_j$, both measures are finite and agree on all rectangles in the block. Those rectangles generate the trace product sigma-algebra: intersections with the block of the ambient rectangles are precisely such rectangles, and taking traces commutes with sigma-algebra generation. The uniqueness lemma proves equality on every measurable subset of the block. Summing over the countable disjoint blocks gives $m=\widetilde m$ on the whole product and proves (MP2). Any other measure with the prescribed rectangle values has the same finite restrictions and is equal to $m$ by this argument. The same blocks prove sigma-finiteness. We write $m=\mu\otimes\nu$. $\square$

<a id="general-tonelli-fubini"></a>

**Tonelli and Fubini.** Suppose $\mu,\nu$ are sigma-finite. For every nonnegative $\Sigma\otimes\mathcal T$-measurable $f$, its sections are measurable, the two section integrals are measurable, and
\[
 \begin{gathered}
 \int_{X\times Y}f\,d(\mu\otimes\nu)\\
 =\int_X\!\int_Y f(x,y)\,d\nu(y)\,d\mu(x)\\
 =\int_Y\!\int_X f(x,y)\,d\mu(x)\,d\nu(y).
 \end{gathered}
 \tag{MP3}
\]
The equalities include the value $+\infty$. For a real or complex product-measurable $f$ satisfying
\[
 \int_{X\times Y}|f|\,d(\mu\otimes\nu)<\infty,
 \tag{MP4}
\]
the sections are absolutely integrable almost everywhere, their integrals, defined to be zero on the exceptional sets, are measurable and integrable, and (MP3) holds for $f$.

**Proof.** Measurability of sections follows by taking sections of the level sets, using the section lemma. For $f=1_E$, all assertions in the nonnegative case are (MP2) and the section lemma. Finite nonnegative linear combinations give the same assertions for simple functions. Choose the increasing finite-valued approximations $f_k=2^{-k}\lfloor2^k\min(f,k)\rfloor$. For each fixed $x$, monotone convergence gives $\int f_k(x,y)\,d\nu(y)\uparrow\int f(x,y)\,d\nu(y)$. Hence that section integral is measurable; the other order is identical. Apply monotone convergence once more to each outer integral and to the product integral to prove (MP3).

Apply this conclusion to $|f|$ under (MP4). The nonnegative section-integral function has finite integral and so is finite almost everywhere: if it were infinite on a set of positive measure, its integral would exceed every finite bound by comparison with constants times that indicator. Thus its infinite set is measurable and null. On its complement, real and imaginary parts of the section of $f$ are absolutely integrable. Apply the nonnegative formula to the positive and negative parts of each component and subtract their finite integrals. On the null exceptional set set the resulting function to zero. This gives measurability and (MP3); the pointwise integral inequality bounds its absolute integral by the finite expression in (MP4). The same argument applies in the opposite order. $\square$

<a id="completed-product-measures"></a>

**Completion.** If the two factor measures are complete, the same assertions hold for the completion of $\mu\otimes\nu$, with measurable sections and section formulas asserted almost everywhere.

**Proof.** The completion consists of sets $E$ for which $E\mathbin{\triangle}B\subset N$ with $B,N$ product-measurable and $m(N)=0$, and assigns them measure $m(B)$. Two choices of $B$ differ by a measurable null set, so give the same value. Complements and countable unions preserve this description by taking the corresponding operations on the $B$'s and the countable union of the null envelopes. For a disjoint union of completed sets, their representatives overlap only inside that null union; disjointifying those representatives proves countable additivity. Every subset of a completed null set is again of this form. This proves that the construction is a complete measure.

Every nonnegative function measurable for this completion has a product-measurable representative equal to it outside a product-measurable null set. To see this, take its finite-valued dyadic approximations. Replace each of their finitely many level sets by a product-measurable set differing inside a product-measurable null envelope. The resulting measurable simple functions agree with the approximations off one countable union $N$ of null envelopes. Their limsup is measurable and agrees with the original function off $N$; set it to zero on $N$. For a real or complex function use its nonnegative components.

By (MP3) applied to $1_N$, $\nu(N_x)=0$ for almost every $x$ and $\mu(N^y)=0$ for almost every $y$. Outside these exceptional sets, completeness of the factors makes all modifications inside the sections of $N$ measurable and preserves their integrals. Apply the preceding theorem to the product-measurable representative. Extending the section integrals by zero on the exceptional sets proves the completed version. Completeness of the factors is used only here; the product-measurable version needs no such assumption. $\square$

For further reading, Axler's freely accessible *Measure, Integration & Real Analysis*, version 12 June 2026, §5A, 5.20 and 5.25–5.27, and §5B, 5.28 and 5.32 (pages 129–133), give the section, product and interchange theorems. The construction uses the proved intersection/lambda-system argument and uniqueness on finite blocks, then gives a separate completion argument. These source locators are credit and comparison; the complete proof needed for a spectral measure is above.

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

The finite-measure approximation used for Schwartz density follows from this construction too: choose an open rectangle cover of $E$ whose total volume is at most $\mu(E)+\varepsilon$. Its union differs from $E$ by measure at most $\varepsilon$. Finite truncations approximate the union in measure by continuity from below. A finite union of boxes therefore approximates $E$ in measure. No density or product-measure theorem from the unverified inherited AN03 construction is used.

<a id="fourier-normalization"></a>
## Fourier facts with the normalization retained

Read [Coordinate inverses, integration and surface measure](coordinate-inverses-and-integration.md#coordinate-integration) after the preceding measure subsection and before this subsection. Its complete change-of-variables proof, which uses only that measure subsection, justifies the polar substitution below. No Fourier fact is used to prove that substitution.

We use the exponential, powers, trigonometry and flat cutoffs proved in [Elementary functions and cutoffs](elementary-functions-and-cutoffs.md). First, for $m>n$, the weight $(1+|x|)^{-m}$ is integrable. On $|x|<1$ it is bounded and the ball lies in a finite box. On $2^j\le|x|<2^{j+1}$ its integral is at most $C_n2^{j(n-m)}$, by enclosure in a box of side $2^{j+2}$. The geometric series converges. The same argument proves integrability of $(1+|x|^2)^{-N}$ when $2N>n$. The exponential domination of powers in (EF9) implies that a Gaussian times any polynomial is integrable: split into a bounded ball and its complement and dominate there by any prescribed integrable negative power.

Schwartz space consists of smooth $f$ for which every $x^\alpha\partial^\beta f$ is bounded. Equivalently all the seminorms
\[
 \begin{gathered}
 p_{m,k}(f)=\max_{|\beta|\le k}\sup_x
          (1+|x|)^m|\partial^\beta f(x)|,\\
 m,k\in\mathbb N_0.
 \end{gathered}
 \tag{F1}
\]
are finite. Indeed $|x^\alpha|\le(1+|x|)^{|\alpha|}$ gives one implication; expanding $(1+\sum_j|x_j|)^m$ as a finite sum of monomials gives the other. The integrable-weight bound just proved shows that every polynomial times every derivative of $f$ is integrable.

Differentiation of its Fourier integral is justified by domination by $|x_jf(x)|$: the exponential difference quotient is at most $|x_j|$, by its scalar integral formula and modulus one. Iterating proves all frequency derivatives. For integration by parts, first multiply by a smooth cutoff $\chi(x/R)$ equal to one near zero. The compactly supported scalar product rule and fundamental theorem give the identity without boundary terms. Derivatives falling on the cutoff have a factor $R^{-1}$ and an integrable Schwartz bound; dominated convergence removes the cutoff and those errors. Thus
$\widehat{\partial_jf}=i\xi_j\widehat f$ and
$\partial_{\xi_j}\widehat f=-i\widehat{x_jf}$.
Apply these identities repeatedly and use the finite product rule to obtain
\[
 p_{m,k}(\widehat f)\le C_{m,k,n}\,p_{k+n+1,m}(f).
 \tag{F2}
\]
To check the bound, each $\xi^\alpha\partial_\xi^\beta\widehat f$ with $|\alpha|\le m$, $|\beta|\le k$ is, up to constant factors, the transform of $\partial_x^\alpha(x^\beta f)$. Its absolute value is at most the $L^1$ norm of that expression. Each of its finitely many terms is bounded by $C p_{k+n+1,m}(f)(1+|x|)^{-n-1}$. The same monomial expansion used for (F1) gives (F2). Consequently the transform preserves Schwartz space and is continuous in all its seminorms.

The preceding bounds make the one-variable Gaussian integral finite and positive. Its value is $\int e^{-x^2/2}\,dx=\sqrt{2\pi}$: square the integral, use polar coordinates in the nonnegative two-dimensional integral, and obtain $2\pi\int_0^\infty re^{-r^2/2}\,dr=2\pi$. For its Fourier transform $G$, differentiation and integration by parts give $G'(\xi)=-\xi G(\xi)$ and $G(0)=\sqrt{2\pi}$, hence $G(\xi)=\sqrt{2\pi}e^{-\xi^2/2}$. Explicitly, the product and chain rules make the derivative of $e^{\xi^2/2}G(\xi)$ zero; scalar mean value makes it constant. The radial integral above is one by the primitive $-e^{-r^2/2}$ and its vanishing limit. All limiting radial integrals use monotone convergence. Product interchange proves the $n$-variable formula.

For $f$ Schwartz and $\varepsilon>0$, absolute interchange and that formula give
\[
 (2\pi)^{-n}\int e^{ix\xi}e^{-\varepsilon|\xi|^2/2}\widehat f(\xi)\,d\xi
 =\int f(y)(2\pi\varepsilon)^{-n/2}e^{-|x-y|^2/(2\varepsilon)}\,dy.
\]
The right side tends to $f(x)$: substitute $y=x-\sqrt\varepsilon t$ and use dominated convergence, since $f$ is bounded and continuous and the fixed Gaussian has integral one. Dominated convergence on the left, since $\widehat f\in L^1$, proves the exact inverse formula $f(x)=(2\pi)^{-n}\int e^{ix\xi}\widehat f(\xi)\,d\xi$.

Apply the inverse formula to $h$ Schwartz and interchange its absolutely integrable product with $f$. This gives Parseval:
\[
 \int f\overline h=(2\pi)^{-n}\int\widehat f\,\overline{\widehat h}.
 \tag{3}
\]
Thus $(2\pi)^{-n/2}\widehat{\phantom f}$ is an isometry on Schwartz space; its inverse is $(2\pi)^{-n/2}\int e^{ix\xi}(\cdot)\,d\xi$. Schwartz space is dense in $L^2$: finite-measure simple functions approximate by the function-space lemma above; for Euclidean Lebesgue measure, finite unions of bounded rectangles approximate finite-measure measurable sets in measure, by the rectangle outer-measure definition and finite truncation of a countable cover. A finite grid of all endpoints splits each finite union into boxes with disjoint interiors, up to null faces. Its indicator can therefore be approximated in $L^2$ by finite sums of products of the [explicit smooth step cutoffs (EF16)–(EF18)](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs) between zero and one whose transition intervals shrink to each rectangle's faces. These products are smooth and compactly supported, and dominated convergence proves the approximation. Hence (3) extends by completion to the full forward and inverse unitary maps on $L^2$. More explicitly, approximate an $L^2$ function by Schwartz functions. The isometry makes the transformed sequence Cauchy; $L^2$ completeness supplies a limit independent of the approximation. The inverse has the same property because its formula is the forward transform composed with reflection and the appropriate constant, and reflection preserves measure. The forward and inverse compositions equal the identity on the dense Schwartz subspace, hence on all of $L^2$. This proves both isometry and surjectivity.

<a id="tempered-fourier-duality"></a>

### Fourier duality and weak derivatives

For clarity, a tempered distribution is a continuous linear functional on Schwartz space with its seminorms (F1); its pairing with a test is bilinear, written $\langle T,\phi\rangle$. Define
\[
 \begin{aligned}
 \langle\widehat T,\phi\rangle&=\langle T,\widehat\phi\rangle,\\
 \langle\partial_jT,\phi\rangle&=-\langle T,\partial_j\phi\rangle.
 \end{aligned}
 \tag{F3}
\]
These are continuous functionals by (F2) and the definitions of the seminorms. The inverse transform on tests is continuous by the same estimate and reflection; transposing the two inverse identities on Schwartz space proves that the distributional Fourier transform is invertible. For $D_j=-i\partial_j$, differentiating the test Fourier integral gives $\partial_j\widehat\phi=-i\widehat{\xi_j\phi}$, so (F3) gives
\[
 \widehat{D^\alpha T}=\xi^\alpha\widehat T.
 \tag{F4}
\]
This is an identity of tempered distributions, with the same unnormalized transform as (1).

The convention agrees with weak derivatives tested only against compact smooth functions. To see this, choose a smooth $\chi$ equal to one on the unit ball and supported in the ball of radius two. For every Schwartz $\phi$, the functions $\chi(x/R)\phi(x)$ converge to $\phi$ in all seminorms (F1). In the product-rule expansion of their difference, the term with no derivative on the cutoff is supported in $|x|\ge R$, and every other term has the same support restriction and a bounded factor $R^{-|\gamma|}\partial^\gamma\chi(x/R)$. For $R\ge1$ each term is therefore bounded in $p_{m,k}$ by $C_{k,\chi}R^{-1}p_{m+1,k}(\phi)$. Two continuous functionals agreeing on compact smooth tests consequently agree on all Schwartz tests. Thus equality of tempered weak derivatives can be checked in either test class.

Each $u\in L^2$ defines a tempered distribution $\phi\mapsto\int u\phi$, since Cauchy–Schwarz and the integrable-weight bound control $\|\phi\|_2$ by a seminorm (F1). This embedding is injective: if all pairings vanish, density of Schwartz functions in $L^2$, applied to the conjugate test, makes $\|u\|_2=0$. For Schwartz $u,\phi$, absolute interchange gives $\int\widehat u\phi=\int u\widehat\phi$. Approximation of $u$ in $L^2$ and Cauchy–Schwarz pass this identity to every $L^2$ function. Thus its distributional transform agrees with its $L^2$ transform. In particular, if $\widehat T$ is represented by an $L^2$ function, inverse unitarity and injectivity of the distributional transform imply that $T$ is represented by its $L^2$ inverse.

For every real $s$, multiplication by $\langle x\rangle^s=(1+|x|^2)^{s/2}$ is continuous on Schwartz space. Repeated product and chain rules express each derivative as a finite sum of a polynomial times a power of $1+|x|^2$; the [real-power proof](elementary-functions-and-cutoffs.md#logarithm-and-real-powers) supplies these differentiations. On bounded sets these expressions are bounded, and outside the unit ball each has at most polynomial growth. The product rule therefore bounds each seminorm of $\langle x\rangle^s\phi$ by finitely many higher seminorms of $\phi$. Transposition defines the corresponding multiplication of tempered distributions, and the products with exponents $s,-s$ are inverse. This gives the weighted-distribution convention used in the Sobolev reading.

<a id="packet-resolution"></a>

## Packets and resolution of the identity

The [earlier local Hilbert proof](finite-trace-ideals.md#elementary-hilbert-tools) constructs representing vectors and bounded adjoints. Thus the adjoint of the analysis map below exists once its norm bound is proved. No compact-operator spectral theorem is used for the packet identity.

Fix the real Gaussian $g(x)=\pi^{-n/4}e^{-|x|^2/2}$, so $\|g\|_2=1$, and put
\[
 \phi_{y,\eta}(x)=e^{i\eta\cdot x}g(x-y),\qquad
 Vu(y,\eta)=\langle u,\phi_{y,\eta}\rangle.
\]
The inner product is linear in the first variable. For Schwartz $u$, (3) in the $\eta$ variable and nonnegative interchange give
\[
 \int |Vu(y,\eta)|^2\,dy\,d\eta
 =(2\pi)^n\int\int |u(x)|^2|g(x-y)|^2\,dx\,dy
 =(2\pi)^n\|u\|_2^2.
 \tag{4}
\]
Therefore $W=(2\pi)^{-n/2}V$ extends to an isometry $L^2(\mathbb R^n)\to L^2(\mathbb R^{2n})$. Polarization of (4) gives $W^*W=I$; for a compactly supported smooth phase-space function $F$,
\[
 W^*F=(2\pi)^{-n/2}\int F(y,\eta)\phi_{y,\eta}\,dy\,d\eta.
 \tag{5}
\]
Here are the integral and representative details. The map $(y,\eta)\mapsto\phi_{y,\eta}$ is norm-continuous into $L^2$. On a compact parameter set its pointwise differences tend to zero, and their squared absolute values are dominated by $C e^{-|x|^2/2}$: for bounded $|y|$, $|x-y|^2\ge |x|^2/2-|y|^2$. Scalar dominated convergence therefore gives norm continuity. Thus $F(y,\eta)\phi_{y,\eta}$ is continuous with compact support into the complete space $L^2$, hence strongly measurable and Bochner integrable by [the exact integral construction, Sections 1–2](hilbert-valued-integration.md#bochner-integral). Pairing with a Schwartz test commutes with the integral and absolute scalar interchange gives exactly the adjoint identity (5).

For any $u\in L^2$ the formula $(2\pi)^{-n/2}(u,\phi_{y,\eta})$ is the representative of $Wu$. Indeed Schwartz approximants converge in each such pairing, uniformly in $(y,\eta)$ by Cauchy–Schwarz and $\|\phi_{y,\eta}\|_2=1$. Their images also converge in phase-space $L^2$ by (4). A summable subsequence has the same almost-everywhere limit by the already proved $L^2$ completeness argument, identifying the two representatives. Finally, polarization can be checked directly by expanding (4) for $u+v$ and $u+iv$: both real and imaginary parts of $(Wu,Wv)$ equal those of $(u,v)$. Hence $(W^*Wu,v)=(u,v)$ for all $v$, proving $W^*W=I$. The adjoint norm is one. No spectral theorem enters.

<a id="packet-off-diagonal"></a>

## Off-diagonal matrix estimate

First let $a$ be smooth with compact support in $(x,\xi)$. Formula (1) is bounded on $L^2$ even before (2): if the two projections of its support have finite measures $|X_0|,|\Xi_0|$, Cauchy–Schwarz in $\xi$ and (3) give $\|Au\|_2^2\le(2\pi)^{-n}|X_0||\Xi_0|\|a\|_\infty^2\|u\|_2^2$. Density gives this bounded operator before any uniform seminorm estimate. We may therefore form $WAW^*$ without assuming the desired conclusion.

Write $w=(y,\eta)$ and $z=(y',\eta')$. The Fourier transform of a packet is
\[
 \widehat{\phi_w}(\xi)=e^{-iy\cdot(\xi-\eta)}\widehat g(\xi-\eta).
\]
Set $X=x-y'$, $\Xi=\xi-\eta$, $d=y'-y$, $e=\eta-\eta'$. Substitution in (1) gives, with a constant phase of modulus one,
\[
 \langle A\phi_w,\phi_z\rangle
 =(2\pi)^{-n}e^{ie\cdot y'}
 \int e^{i(e\cdot X+d\cdot\Xi)}
 b_{z,w}(X,\Xi)\,dX\,d\Xi,
 \tag{6}
\]
where
\[
 b_{z,w}=a(X+y',\Xi+\eta)\widehat g(\Xi)g(X)e^{iX\cdot\Xi}.
\]
Integrate (6) by parts with $(1-\Delta_X)^N(1-\Delta_\Xi)^N$. The corresponding factors on the displayed exponential are $(1+|e|^2)^N(1+|d|^2)^N$. Every derivative of $b$ is a finite sum of a derivative of $a$ of orders at most $2N$ in each variable, times a polynomial in $(X,\Xi)$ times the two fixed Gaussian functions and $e^{iX\Xi}$. All such Gaussian-polynomial factors have a fixed finite $L^1$ norm. The product rule therefore gives
\[
 |\langle A\phi_w,\phi_z\rangle|
 \leq C_{n,N}M_N(a)
 (1+|y-y'|^2)^{-N}(1+|\eta-\eta'|^2)^{-N}.
 \tag{7}
\]
The boundary terms vanish because of Gaussian decay. This proves the estimate with the stated finite derivative count; no uncontrolled symbol derivatives enter the constant.

<a id="schur-extension"></a>

## Schur estimate and extension

By (5), the matrix kernel of $WAW^*$ is $(2\pi)^{-n}\langle A\phi_w,\phi_z\rangle$. To justify this representation before invoking its bound, take $F\in C_c^\infty(\mathbb R^{2n})$. The already bounded compact-symbol operator $A$ commutes with the Bochner integral (5); pairing its value with $\phi_z$ gives the stated kernel formula. The packet continuity proves continuity, hence measurability, of this kernel in $(z,w)$. The dyadic-box argument at the start of the Fourier subsection proves that the integrals of $(1+|v|^2)^{-N}$ are finite precisely in the range needed here, $N>n/2$. Estimate (7) bounds both every row integral and every column integral of the absolute kernel by $C_{n,N}M_N(a)$.

For completeness, if a kernel $K$ has row bound $r$ and column bound $c$, weighted Cauchy–Schwarz gives
\[
 |TF(z)|^2\leq\left(\int|K(z,w)|dw\right)
 \left(\int|K(z,w)||F(w)|^2dw\right).
\]
Integrating and applying nonnegative interchange yields $\|TF\|_2^2\leq rc\|F\|_2^2$. Initially take compactly supported tests, then extend by density. Thus $\|WAW^*\|\leq C_{n,N}M_N(a)$. Because $W^*W=I$, $A=W^*(WAW^*)W$, which proves (2) for compactly supported $a$.

For general $a$ as in the statement, choose a fixed smooth compactly supported cutoff $\chi$, equal to one near zero, and put $a_R=a\chi(x/R)\chi(\xi/R)$ for $R\geq1$. The product rule gives $M_N(a_R)\leq C_{n,N,\chi}M_N(a)$ uniformly. For a Schwartz $u$, dominated convergence in the absolutely convergent $\xi$ integral gives $A_Ru(x)\to Au(x)$ pointwise; the dominating function is a constant times $|\widehat u(\xi)|$. Fatou then gives $\|Au\|_2\leq C M_N(a)\|u\|_2$. Density proves the unique extension. The constant can absorb the one fixed cutoff and depends only on $n,N$. This proves the full assertion.

## Exact use after a dilation

For $\rho>0$, if $D_\rho u(x)=\rho^{n/2}u(\rho x)$, then $D_\rho$ is unitary, and direct substitution in (1) gives
\[
 D_\rho^{-1}\operatorname{Op}_L(a)D_\rho
 =\operatorname{Op}_L(a(x/\rho,\rho\xi)).
\]
Consequently apply (2) to the *actual conjugated symbol*. Its derivative factors are $\rho^{-|\alpha|+|\beta|}$ times the corresponding derivatives of $a$ evaluated at $(x/\rho,\rho\xi)$. A uniform bound on these finitely many quantities is exactly the hypothesis needed in AN06-U044. The theorem does not assert that an arbitrary dilation keeps the seminorm bounded automatically.
