# Scalar measure and integration: programme proofs

*Sections 1, 2 and 6 were written and self-checked by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Their original exposition is CC0. The selection, preliminary clarifications and companion proofs were prepared and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Independent review remains separate.*

This is the complete mathematical text of Sections 1, 2 and 6 of the programme lesson *Measure and Hilbert space tools for Haar integration*. The numbering is retained for exact references. The unused Hilbert-space material and the surrounding course introduction are omitted. Read these proofs before [Products, scalar Fubini and the polar integral](scalar-product-integration.md), which constructs product measures and supplies the additional arguments needed by the modular kernel.

The starting conventions are elementary set theory and the complete ordered real field, with its usual complexification. No measure-theoretic convergence theorem is assumed. The following elementary details make explicit the compactness and measurability steps used in the selected text.

## 0. Preliminary details

**Compact intervals.** Every open cover of \([a,b]\) has a finite subcover. Let \(c\) be the supremum of the points \(x\) for which \([a,x]\) has a finite subcover. A cover member containing \(a\) first makes this set nonempty. A cover member containing \(c\), together with a covered point sufficiently close to \(c\) from the left, extends a finite cover to a neighbourhood of \(c\). If \(c<b\), this contradicts the supremum property; when \(c=b\), the same argument covers the endpoint. The case \(a=b\) is immediate.

A continuous scalar function on a compact interval is bounded: finitely many neighbourhoods on which its value differs from the central value by less than one cover the interval. It is uniformly continuous: for a given \(\varepsilon>0\), choose at each \(x\) a radius \(r_x>0\) so that values within \(r_x\) of \(x\) differ from its value by less than \(\varepsilon/2\). Finitely many half-radius neighbourhoods cover the interval. If \(\delta\) is the minimum of those half-radii, any two points of distance less than \(\delta\) lie within the full radius of the same centre; their values differ by less than \(\varepsilon\).

For the extremum assertion in Section 6, every sequence in \([a,b]\) has a convergent subsequence. Repeatedly bisect the interval, retain a closed half containing infinitely many terms, and select terms with strictly increasing indices. The nested endpoints have a common limit by completeness, and the selected terms tend to it. A sequence of function values approaching the supremum therefore has a subsequence whose arguments converge; continuity gives a point attaining that supremum. The infimum follows by negation. This proves the real extremum facts used in Rolle's theorem. Complex integral identities in Section 6 are obtained by applying the real argument to real and imaginary parts.

**Measurability and null sets.** A pair of measurable real functions is measurable as a map to \(\mathbb R^2\): inverse images of rational open boxes are measurable, and every open set is a countable union of such boxes. Composing with continuous scalar maps proves measurability of sums, products, absolute values and positive and negative parts. The same reasoning applies to any finite tuple. A measurable nonnegative function supported on a measurable null set has integral zero directly from the definition by simple minorants. Consequently measurable functions equal off a measurable null set have the same nonnegative or integrable scalar integral. This justifies discarding the exceptional sets in Section 2. On a noncomplete space, a nonmeasurable modification on a null set is always interpreted by its measurable representative; it is not asserted to be literally measurable.

## 1. From an outer measure to a measure

A sigma-algebra on a set \(X\) is a family containing \(X\) and closed under complements and countable unions. A measure on it is a function into \([0,\infty]\) taking the empty set to zero and countably additive on disjoint sets. An outer measure \(m^*\) is defined on every subset of \(X\), is zero at the empty set, is monotone, and satisfies
\[
m^*\left(\bigcup_n A_n\right)\leq\sum_n m^*(A_n).
\]

**Theorem 1.1 (Carathéodory).** The sets \(E\subseteq X\) satisfying
\[
m^*(A)=m^*(A\cap E)+m^*(A\setminus E)\qquad(A\subseteq X)
\tag{1.1}
\]
form a sigma-algebra. The restriction of \(m^*\) to it is a complete measure. To verify (1.1) it suffices to prove its greater-than-or-equal inequality for \(A\) with finite outer measure.

*Proof.* The other inequality is subadditivity; when \(m^*(A)=\infty\), the greater-than-or-equal inequality is automatic. Complements preserve the condition. If \(E,F\) satisfy it, split \(A\) first by \(E\), and then split \(A\setminus E\) by \(F\). The sum of the first two resulting terms is at least \(m^*(A\cap(E\cup F))\), by subadditivity. This proves the condition for \(E\cup F\); differences and finite intersections follow.

Let \(E_n\) be disjoint sets satisfying the condition, and put \(E=\bigcup_nE_n\). Repeated finite splitting gives
\[
m^*(A)=\sum_{n=1}^N m^*(A\cap E_n)+m^*\left(A\setminus\bigcup_{n=1}^N E_n\right)
\geq\sum_{n=1}^N m^*(A\cap E_n)+m^*(A\setminus E).
\]
Let \(N\) increase. Subadditivity gives \(\sum_n m^*(A\cap E_n)\geq m^*(A\cap E)\), so \(E\) satisfies the condition. An arbitrary countable union is reduced to this case by replacing \(E_n\) with \(E_n\setminus\bigcup_{j<n}E_j\). Thus the family is a sigma-algebra. Taking \(A=E\) in the finite-splitting inequality proves countable additivity on the disjoint \(E_n\), together with subadditivity. If \(N\) has outer measure zero, every subset of \(N\) satisfies (1.1): monotonicity makes the first term zero, while monotonicity and subadditivity force the second term to equal \(m^*(A)\). This also proves completeness. \(\square\)

**Example.** Assign to a subset of the real line the infimum of the sums of lengths of countable open interval covers. This is an outer measure: combine covers with errors \(\varepsilon2^{-n}\) to prove subadditivity. Splitting every covering interval at a fixed point splits its total length between the two half-lines; enlarge the split intervals by errors whose sum is arbitrarily small. This gives the reverse Carathéodory inequality for each half-line. Half-lines generate the Borel sigma-algebra, so Theorem 1.1 makes every Borel set measurable.

The measure of \([a,b]\) is \(b-a\). An enlarged interval gives the upper bound. For any countable open cover of \([a,b]\), compactness selects a finite subcover. The sum of its interval lengths is at least \(b-a\): arrange its endpoints in order, and each successive subinterval of \([a,b]\) is covered by at least one member. Summing lengths proves the lower bound. Singletons have measure zero, so the same length formula holds for open and half-open bounded intervals. Translating or dilating interval covers shows directly that \(m^*(E+t)=m^*(E)\) and \(m^*(aE)=|a|m^*(E)\) for \(a\ne0\), using the inverse operation for the reverse inequalities. The resulting Borel Lebesgue measure, or its completion, is therefore translation invariant. The next lesson instead constructs an outer measure using continuous functions on an arbitrary LCH space.

## 2. Integration and convergence without countability assumptions

Fix a measure space \((X,\Sigma,\mu)\). A measurable real function is one for which \(\{f>t\}\in\Sigma\) for every real \(t\). Countable suprema and infima are measurable: use \(\{\sup_n f_n>t\}=\bigcup_n\{f_n>t\}\), and negate for infima. Limits are measurable because \(\liminf f_n=\sup_N\inf_{n\geq N}f_n\). Complex functions are measurable when their real and imaginary parts are.

For a nonnegative simple function \(s=\sum_{j=1}^r a_j1_{E_j}\), with disjoint measurable \(E_j\) and \(a_j\geq0\), define \(\int s=\sum_j a_j\mu(E_j)\), with \(0\cdot\infty=0\). Refining two partitions proves independence of the presentation, monotonicity, and additivity for simple functions. For measurable \(f\geq0\), define
\[
\int f=\sup\{\int s:0\leq s\leq f,\ s\text{ simple}\}.
\]
There are increasing simple \(s_n\to f\): truncate \(f\) at \(n\) and round down to multiples of \(2^{-n}\). The truncation bounds and the refining dyadic grids ensure monotonicity.

Countable additivity implies continuity from below: if \(E_n\uparrow E\), write \(E\) as the disjoint union of \(E_1,E_2\setminus E_1,\ldots\). Then \(\mu(E_n)\uparrow\mu(E)\). If \(\mu(E_1)<\infty\) and \(E_n\downarrow E\), apply this to \(E_1\setminus E_n\) to obtain continuity from above.

**Theorem 2.1 (Monotone convergence).** If \(0\leq f_n\uparrow f\) almost everywhere, then \(\int f_n\uparrow\int f\).

*Proof.* Discard one measurable null set to obtain pointwise inequalities; changing values there changes none of the integrals. Monotonicity gives \(\lim\int f_n\leq\int f\). For simple \(s\leq f\) and \(0<t<1\), the sets \(A_n=\{f_n\geq ts\}\) increase and cover \(\{s>0\}\). Consequently continuity from below on the finitely many level sets of \(s\) gives \(\int s1_{A_n}\uparrow\int s\). Since \(f_n\geq ts1_{A_n}\), the limit of their integrals is at least \(t\int s\). Let \(t\uparrow1\) and then take the supremum over \(s\). The same argument works when \(\int s=\infty\). \(\square\)

Applying this to increasing simple approximations of \(f,g\geq0\) proves \(\int(f+g)=\int f+\int g\). Applying it to partial sums proves
\[
\int\sum_n f_n=\sum_n\int f_n\qquad(f_n\geq0).
\tag{2.1}
\]
These identities justify defining the integral of an integrable real function as \(\int f^+-\int f^-\), and then treating complex functions by real and imaginary parts. Here integrable means \(\int|f|<\infty\). Linearity follows from nonnegative additivity by moving all negative parts to the opposite side of the desired equality. Choosing a phase so that \(e^{i\theta}\int f\) is nonnegative real gives \(|\int f|\leq\int|f|\).

**Theorem 2.2 (Fatou and dominated convergence).** For measurable \(f_n\geq0\),
\[
\int\liminf_n f_n\leq\liminf_n\int f_n.
\]
If complex measurable \(u_n\to u\) almost everywhere and \(|u_n|\leq g\) almost everywhere for one integrable \(g\geq0\), then \(u\) is integrable and \(\int|u_n-u|\to0\). In particular \(\int u_n\to\int u\).

*Proof.* The functions \(v_N=\inf_{n\geq N}f_n\) increase to the liminf, and \(\int v_N\leq\inf_{n\geq N}\int f_n\). Monotone convergence proves Fatou. For the second assertion, \(|u|\leq g\) almost everywhere. Fatou applied to the nonnegative functions \(2g-|u_n-u|\), whose limit is \(2g\), gives
\[
2\int g\leq2\int g-\limsup_n\int|u_n-u|.
\]
All integrals here are finite, so the limsup is zero. The integral inequality proved above gives the last assertion. \(\square\)

**Example.** On an uncountable set with counting measure, an integrable function has countable support: for each positive integer \(n\), only finitely many points can have \(|f|>1/n\). Nevertheless the whole space is not sigma-finite. Theorems 2.1 and 2.2 remain valid. A later interchange of integrals will need a separate theorem; convergence alone does not supply it.


## 6. One-variable integral identities

The explicit Haar and arithmetic examples use elementary calculus. Here are the integral identities needed, with their proofs, so no general multidimensional change-of-variables theorem is implicit.

**Lemma 6.1.** If \(h\) is continuous on a compact interval, its Lebesgue integral equals its Riemann integral. For \(H\in C^1([a,b])\),
\(\int_a^b H'(t)\,dt=H(b)-H(a)\).
If \(\phi\in C^1([a,b])\) and \(h\) is continuous on an interval containing its image, then
\[
 \int_{\phi(a)}^{\phi(b)}h(u)\,du
 =\int_a^b h(\phi(t))\phi'(t)\,dt.
 \tag{6.1}
\]
In particular, the integral of a compactly supported continuous derivative on the real line is zero. Differentiating a parameter integral is valid when its difference quotients converge pointwise and have a common integrable bound.

*Proof.* Recall the elementary differential facts involved. A continuous function on a compact interval attains its extrema. If its endpoints agree, either it is constant or one extremum occurs in the interior, where its derivative is zero: the left and right difference quotients have opposite weak signs. This is Rolle's theorem. Subtract the line joining the endpoint values to obtain the mean value theorem. The chain rule follows by substituting \(\phi(t+h)-\phi(t)=\phi'(t)h+o(h)\) into the corresponding first-order expansion of the outer function; differentiability makes the inner increment \(O(h)\).

Uniform continuity makes the difference between the upper and lower step functions on a sufficiently fine partition arbitrarily small in integral; both bound \(h\). Their Lebesgue integrals are the same interval-length sums that define the Riemann integral. For \(H\), the mean value theorem on each partition interval expresses its increment as \(H'(\xi)\) times the interval length. Summing telescopes to \(H(b)-H(a)\); uniform continuity of \(H'\) makes the sums converge to its integral.

Define \(A(v)=\int_{v_0}^v h(u)\,du\), with oriented integrals. The difference quotient of \(A\) is an interval average of \(h\), tending to \(h(v)\) by continuity. Thus \((A\circ\phi)'=(h\circ\phi)\phi'\). Apply the preceding identity to \(A\circ\phi\) to obtain (6.1). The zero-integral assertion follows by choosing endpoints outside the support. Finally apply dominated convergence, Theorem 2.2, to the difference quotients to justify the parameter derivative. ∎

