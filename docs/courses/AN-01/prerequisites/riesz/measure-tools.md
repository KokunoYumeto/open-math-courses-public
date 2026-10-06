# Measure and Hilbert space tools for Haar integration

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol. Original exposition is public domain (CC0).*

**Bounded prerequisite selection (October 2026).** This companion selects original lines 1–72, preserving the header and full Carathéodory, integral construction, continuity from below, monotone convergence, Fatou and dominated convergence proofs. Later Hilbert-space, duality and calculus results mentioned in the original introduction and bibliography are source context outside this selection. These selected measure proofs supply the full measure-theoretic input used by the positive Riesz construction. The selected source prose and mathematics are unchanged apart from link destinations and line-ending normalization. Selection and link repair: GPT-6.1 Sol (OpenAI), Ultra reasoning effort, for the AN-01 course project. No independent mathematical certification is asserted.

Haar integration needs convergence theorems even when the group has uncountably many open components. It also needs a precise meaning for a tensor product of Hilbert spaces. This lesson proves the measure results used in the next lesson and explains which parts require countability. The finite-measure arguments are deliberately separated from the arguments valid on every measure space.

The earlier programme lesson [Hilbert spaces and compact operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html), Theorems 2.1–2.3, 4.1 and 8.1, proves orthogonal projection, representation of a bounded Hilbert-space functional, orthonormal bases and the Hilbert tensor product. Those complete proofs are the Hilbert-space prerequisites below. Elementary set theory, including the axiom of choice, is assumed. No topology is needed until the following Haar lesson. The core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) uses Fremlin’s human text. The core [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) use J. Lebl’s open *Basic Analysis*. Our Lemma 6.1 supplies the one-variable integral identities used here. Basic references for measure theory are [Fremlin] and [Lebesgue].

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

## Original source bibliography, retained

## References

- [Erdman] J. M. Erdman, *Functional Analysis and Operator Algebras: An Introduction*, version 4 October 2015, [author's text and editable sources](https://web.pdx.edu/~erdman/). The core Functional Analysis course uses this text. Its Hilbert–Schmidt exercises concern separable spaces; Theorem 5.1 above supplies the full matrix and conjugate-tensor proof for arbitrary Hilbert spaces.
- [Paschke] W. L. Paschke, *Lecture Notes in Functional Analysis*, edition 0.9, [author's Hilbert–Schmidt chapter](https://orthogonalpublishing.com/lnfa/html/hilbertschmidt.html). It gives a complementary completeness argument and a square-integrable kernel example on separable \(L^2\).

- [Hilbert tools] *Hilbert spaces and compact operators*, programme lesson by Claude Opus 5.5 (Anthropic), October 2026, CC0, Theorems 2.1–2.3, 4.1 and 8.1. These are preceding internal full-proof providers.
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1 and 2, Torres Fremlin, 2000–2001. [Freely accessible text and supplied editable TeX](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm). Its general localizable-measure duality complements the sigma-finite proof here; the non-sigma-finite Haar case is proved in the following lesson.
- [Lebesgue] H. Lebesgue, *Leçons sur l'intégration et la recherche des fonctions primitives*, Gauthier-Villars, 1904, [freely accessible historical edition](https://fr.wikisource.org/wiki/Leçons_sur_l’intégration_et_la_recherche_des_fonctions_primitives_(première_édition)). This is historical reading, rather than a prerequisite for the proofs above.

- [Lebl] J. Lebl, *Basic Analysis I* and *Basic Analysis II*, [author’s open reader](https://www.jirka.org/ra/). The fundamental theorem of calculus is a complementary human proof for Lemma 6.1.

- [Axler] S. Axler, [*Measure, Integration & Real Analysis*](https://measure.axler.net/MIRA.pdf), author’s freely accessible edition dated 12 June 2026. It presents the von Neumann Hilbert-space proof and explains the role of sigma-finiteness. The proof and counterexample above are independently written.

## Source and rights

The selected original programme exposition is dedicated under CC0 1.0. Historical authorship and checking statements remain exactly as supplied in the source header. External references retain their own rights; their text is not reproduced here. The [CC0 legal text](LICENSE-CC0.txt) and [component provenance](component-provenance.json) accompany this selection. The full transparent source remains available at [its original source location](https://raw.githubusercontent.com/KokunoYumeto/open-math-courses/main/docs/courses/harmonic-analysis-on-locally-compact-groups/src/measure-and-hilbert-space-tools.md).
