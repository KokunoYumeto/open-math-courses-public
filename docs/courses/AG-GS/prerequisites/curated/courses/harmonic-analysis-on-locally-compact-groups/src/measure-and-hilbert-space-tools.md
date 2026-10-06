# Measure and Hilbert space tools for Haar integration

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol. GPT-6 Astra (OpenAI), Ultra, supplied and self-checked the measurable-limit conventions and the one-variable boundary and parameter statements. Original exposition is public domain (CC0).*

Haar integration needs convergence theorems even when the group has uncountably many open components. It also needs a precise meaning for a tensor product of Hilbert spaces. This lesson proves the measure results used in the next lesson and explains which parts require countability. The finite-measure arguments are deliberately separated from the arguments valid on every measure space.

The earlier programme lesson [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators), Theorems 2.1–2.3, 4.1 and 8.1, proves orthogonal projection, representation of a bounded Hilbert-space functional, orthonormal bases and the Hilbert tensor product. Those complete proofs are the Hilbert-space prerequisites below. Elementary set theory, including the axiom of choice, is assumed. No topology is needed until the following Haar lesson. The core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) uses Fremlin’s human text. The core [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) use J. Lebl’s open *Basic Analysis*. Our Lemma 6.1 supplies the one-variable integral identities used here. Basic references for measure theory are [Fremlin] and [Lebesgue].

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

Here “almost everywhere” means outside a measurable null set. All functions integrated below are measurable for the specified sigma-algebra. A limit specified only almost everywhere has a measurable representative: on a measurable null set outside which convergence holds, set both the sequence and its limit equal to zero; the modified limit is a pointwise limit of measurable functions. On an incomplete measure space an arbitrary modification on a subset of a null set need not be measurable. Thus an assertion about the integral of a specified limit requires that limit to be measurable, or means its measurable representative.

For a nonnegative simple function \(s=\sum_{j=1}^r a_j1_{E_j}\), with disjoint measurable \(E_j\) and \(a_j\geq0\), define \(\int s=\sum_j a_j\mu(E_j)\), with \(0\cdot\infty=0\). Refining two partitions proves independence of the presentation, monotonicity, and additivity for simple functions. For measurable \(f\geq0\), define
\[
\int f=\sup\{\int s:0\leq s\leq f,\ s\text{ simple}\}.
\]
There are increasing simple \(s_n\to f\): truncate \(f\) at \(n\) and round down to multiples of \(2^{-n}\). The truncation bounds and the refining dyadic grids ensure monotonicity.

Countable additivity implies continuity from below: if \(E_n\uparrow E\), write \(E\) as the disjoint union of \(E_1,E_2\setminus E_1,\ldots\). Then \(\mu(E_n)\uparrow\mu(E)\). If \(\mu(E_1)<\infty\) and \(E_n\downarrow E\), apply this to \(E_1\setminus E_n\) to obtain continuity from above.

**Theorem 2.1 (Monotone convergence).** For nonnegative extended-real measurable functions \(f_n,f\), if \(f_n\uparrow f\) almost everywhere, then \(\int f_n\uparrow\int f\). A limit specified only almost everywhere is interpreted through the measurable representative just described.

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
If complex measurable \(u_n\) converge almost everywhere to a measurable \(u\), and \(|u_n|\leq g\) almost everywhere for one integrable \(g\geq0\), then \(u\) is integrable and \(\int|u_n-u|\to0\). In particular \(\int u_n\to\int u\). If \(u\) was specified only off a measurable null set, the conclusion applies to its measurable representative; no completeness assumption on \(\mu\) is needed.

*Proof.* The functions \(v_N=\inf_{n\geq N}f_n\) increase to the liminf, and \(\int v_N\leq\inf_{n\geq N}\int f_n\). Monotone convergence proves Fatou. For the second assertion, \(|u|\leq g\) almost everywhere, so measurability makes \(u\) integrable. Take the union of the measurable exceptional null sets for convergence, the countably many bounds, and \(\{g=\infty\}\). Set \(u_n,u,g\) to zero on that union. Their integrals do not change, all bounds now hold pointwise, and no infinite subtraction occurs. Fatou applied to the nonnegative functions \(2g-|u_n-u|\), whose limit is \(2g\), gives
\[
2\int g\leq2\int g-\limsup_n\int|u_n-u|.
\]
All integrals here are finite, so the limsup is zero. The integral inequality proved above gives the last assertion. \(\square\)

**Example (Why the representative convention matters).** Let \(X=\{a,b,c\}\), \(\Sigma=\{\varnothing,\{a,b\},\{c\},X\}\), \(\mu(\{a,b\})=0\), and \(\mu(\{c\})=1\). The measurable functions \(u_n=0\) converge almost everywhere to \(1_{\{a\}}\), and are dominated by zero. But \(1_{\{a\}}\) is not \(\Sigma\)-measurable, since \(\{a\}\notin\Sigma\). Its measurable representative is zero. Theorem 2.2 concerns that representative, not an undefined integral of the nonmeasurable function.

**Example.** On an uncountable set with counting measure, an integrable function has countable support: for each positive integer \(n\), only finitely many points can have \(|f|>1/n\). Nevertheless the whole space is not sigma-finite. Theorems 2.1 and 2.2 remain valid. A later interchange of integrals will need a separate theorem; convergence alone does not supply it.

## 3. The complete spaces of integrable functions

For \(1\leq p<\infty\), let \(L^p(\mu)\) be measurable functions modulo almost-everywhere equality with norm \(\|f\|_p=(\int|f|^p)^{1/p}\). Let \(L^\infty(\mu)\) consist of essentially bounded functions, with essential supremum norm. These definitions use the given sigma-algebra, with no assumption that the measure is complete.

**Theorem 3.1 (Hölder and Minkowski).** If \(1/p+1/q=1\), including the endpoints, then \(\int|fg|\leq\|f\|_p\|g\|_q\). For \(1\leq p\leq\infty\), \(\|f+g\|_p\leq\|f\|_p+\|g\|_p\).

*Proof.* For \(1<p<\infty\), minimization of \(a^p/p-ab+b^q/q\) in \(a\geq0\) gives Young's inequality \(ab\leq a^p/p+b^q/q\). Apply it to \(a=|f|/\|f\|_p\), \(b=|g|/\|g\|_q\) and integrate. A zero norm means the corresponding function vanishes almost everywhere. The endpoints follow by bounding the essentially bounded factor outside its exceptional null set.

For Minkowski with \(1<p<\infty\), the elementary convexity inequality \((a+b)^p\leq2^{p-1}(a^p+b^p)\) first proves \(f+g\in L^p\). Put \(h=|f+g|\). Hölder gives
\[
\int h^p\leq\int(|f|+|g|)h^{p-1}
\leq(\|f\|_p+\|g\|_p)\left(\int h^p\right)^{1/q}.
\]
Divide when \(\|h\|_p>0\). The cases \(p=1,\infty\) are the pointwise triangle inequality. \(\square\)

**Theorem 3.2 (Completeness and simple approximation).** Every \(L^p(\mu)\), \(1\leq p\leq\infty\), is complete. For finite \(p\), simple functions with support of finite measure are dense, and every \(f\in L^p\) vanishes outside a sigma-finite measurable set.

*Proof.* Let \(f_n\) be Cauchy in \(L^p\), \(p<\infty\). Choose a subsequence \(f_{n_j}\) with \(\|f_{n_{j+1}}-f_{n_j}\|_p\leq2^{-j}\), and measurable representatives. The partial sums of
\[
v=\sum_{j\geq1}|f_{n_{j+1}}-f_{n_j}|
\]
have \(L^p\) norm at most one by Minkowski. Monotone convergence applied to their \(p\)-th powers gives \(\int v^p\leq1\). Thus \(v<\infty\) outside a measurable null set, and the subsequence converges there to a measurable \(f\), defined as zero on that null set. Its tail difference satisfies
\[
|f-f_{n_j}|\leq\sum_{k\geq j}|f_{n_{k+1}}-f_{n_k}|,
\qquad \|f-f_{n_j}\|_p\leq\sum_{k\geq j}2^{-k}.
\]
The latter follows by Minkowski for finite sums and monotone convergence. Hence \(f\in L^p\) and the subsequence converges in norm; the original Cauchy sequence does too.

For \(p=\infty\), choose a subsequence with the same summable bounds. Remove a measurable null set on which its first term fails its essential bound, as well as the countably many null sets on which successive differences fail their bounds. On the complement the first term is bounded and the series of differences converges uniformly. Define the limit as zero on the removed measurable set. It is bounded and measurable, and the same tail estimate proves norm convergence.

For finite \(p\), the sets \(E_n=\{1/n<|f|\leq n\}\) increase to \(\{f\ne0\}\), and \(\mu(E_n)\leq n^p\|f\|_p^p<\infty\). Dominated convergence shows \(f1_{E_n}\to f\) in \(L^p\). Approximate the bounded complex function \(f1_{E_n}\) uniformly by simple functions supported on \(E_n\), with error at most \(\varepsilon/(1+\mu(E_n))^{1/p}\). This proves density and the support assertion. \(\square\)

In particular \(L^2\) is a Hilbert space for \(\langle f,g\rangle=\int f\overline g\). Hölder proves that the inner product exists, and the theorem proves completeness. This is the point at which the earlier Hilbert-space results may be applied to measure spaces.

## 4. Densities and bounded functionals

Absolute continuity \(\nu\ll\mu\) means that every \(\mu\)-null measurable set is \(\nu\)-null. We use the classical Hilbert-space method of J. von Neumann, also presented in S. Axler’s [*Measure, Integration & Real Analysis*](https://measure.axler.net/MIRA.pdf). The following proof first produces a bounded density relative to \(\mu+\nu\); division then gives the density relative to \(\mu\). It avoids assuming a Radon–Nikodym theorem inside a representation theorem.

**Theorem 4.1 (Radon–Nikodym).** If \(\mu,\nu\) are sigma-finite measures on the same sigma-algebra and \(\nu\ll\mu\), there is a measurable \(h\geq0\), unique \(\mu\)-almost everywhere, such that \(\nu(E)=\int_Eh\,d\mu\) for every measurable \(E\).

*Proof.* First assume both measures finite and put \(\lambda=\mu+\nu\). The functional \(u\mapsto\int u\,d\nu\) on \(L^2(\lambda)\) is bounded: Cauchy–Schwarz gives a bound \(\nu(X)^{1/2}\|u\|_{L^2(\lambda)}\). The Riesz–Fréchet theorem in the earlier Hilbert lesson, Theorem 2.3, supplies \(g\in L^2(\lambda)\) with \(\int u\,d\nu=\int ug\,d\lambda\); conjugate the representing vector because our inner product is linear in its first variable.

Testing measurable indicators shows that \(g\) is real with \(0\leq g\leq1\) almost everywhere. Indeed \(\int_Eg\) is real and between zero and \(\lambda(E)\) for every \(E\); the level sets where the imaginary part has one sign, or where \(g<0\) or \(g>1\), would violate these inequalities. Redefine \(g\) on the exceptional measurable null set. Then \(\nu=g\lambda\) and \(\mu=(1-g)\lambda\) on all sets. On \(A=\{g=1\}\), \(\mu(A)=0\), so \(\nu(A)=0\), hence \(\lambda(A)=0\). Set \(h=g/(1-g)\) outside \(A\), and \(h=0\) on \(A\). The indicator identities extend to nonnegative functions by simple approximation and monotone convergence. Consequently
\[
\int_Eh\,d\mu=\int_Eh(1-g)\,d\lambda=\int_Eg\,d\lambda=\nu(E).
\]

For sigma-finite measures choose a disjoint countable measurable partition into pieces finite for both measures: intersect their two finite-measure covers and disjointify. Apply the finite argument on each piece and join the densities. Countable additivity and monotone convergence give the formula on \(X\). For uniqueness, a candidate density is finite almost everywhere on each piece where the target measure is finite: its infinite level set must be null for the reference measure. On a finite-measure piece where both candidate densities are bounded, integrate over \(\{h\geq k+1/n\}\). Equality of the integrals forces its measure to vanish. Countably many such pieces cover the set where \(h>k\), up to null sets; interchange them for the reverse inequality. \(\square\)

**Theorem 4.2 (The dual of \(L^1\)).** On a sigma-finite measure space, every bounded complex linear functional \(\Phi\) on \(L^1(\mu)\) has the form \(\Phi(u)=\int bu\,d\mu\) for a unique \(b\in L^\infty(\mu)\), with \(\|\Phi\|=\|b\|_\infty\).

*Proof.* If \(\mu(X)<\infty\), restrict \(\Phi\) to \(L^2\), using \(\|u\|_1\leq\mu(X)^{1/2}\|u\|_2\). Hilbert representation gives a measurable \(b\in L^2\) with \(\Phi(u)=\int bu\) there. For \(c>\|\Phi\|\), take \(E=\{|b|>c\}\) and \(u=1_E\overline b/|b|\), with zero value when \(b=0\). This bounded function belongs to \(L^2\), and
\[
c\mu(E)\leq\int_E|b|=|\Phi(u)|\leq\|\Phi\|\mu(E).
\]
Thus \(\mu(E)=0\), and \(\|b\|_\infty\leq\|\Phi\|\). Simple functions are in \(L^2\) and dense in \(L^1\), by Theorem 3.2, so the identity extends to \(L^1\).

In the sigma-finite case partition \(X\) into finite-measure pieces \(E_n\), apply the argument to \(u\mapsto\Phi(u1_{E_n})\), and join the bounded densities. They have the uniform bound \(\|\Phi\|\). The series \(u=\sum_nu1_{E_n}\) converges in \(L^1\), so the joined density represents \(\Phi\). Its uniqueness follows by testing the phase of the difference on finite-measure pieces. Hölder gives \(\|\Phi\|\leq\|b\|_\infty\), proving norm equality. \(\square\)

The sigma-finite hypothesis in this last theorem is explicit. The Haar lesson later decomposes a general group into open sigma-compact cosets and applies the theorem on each coset; it will not assume the hypothesis globally.

### Why sigma-finiteness matters for a density

**Example 4.3.** Let \(X=[0,1]\) with its Borel sigma-algebra, let \(\mu\) be counting measure, and let \(\nu\) be Lebesgue measure. Then \(\nu\ll\mu\), but no nonnegative measurable function \(h\) satisfies \(\nu(E)=\int_Eh\,d\mu\) for every Borel \(E\).

*Proof.* Counting measure has no nonempty null set, so absolute continuity is automatic. If a density existed, then for every \(x\in[0,1]\),
\[
0=\nu(\{x\})=\int_{\{x\}}h\,d\mu=h(x).
\]
Thus \(h\) would vanish everywhere, contradicting \(\nu([0,1])=1\). A finite-counting-measure set is finite, and a countable union of finite sets is countable, whereas \([0,1]\) is uncountable. Consequently \(\mu\) is not sigma-finite. This example pinpoints the failure of the reference-measure hypothesis in Theorem 4.1, even though the target measure is finite. \(\square\)

## 5. Tensor products as Hilbert–Schmidt operators

For Hilbert spaces \(H,K\), a tensor is built in [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators), Theorem 8.1: choose orthonormal bases indexed by \(I,J\), take \(\ell^2(I\times J)\), and send \((\xi,\eta)\) to the array \(\langle\xi,e_i\rangle\langle\eta,f_j\rangle\). The theorem proves basis independence through its isometric universal property. No separability is assumed.

There is a second useful interpretation. Write \(\overline H\) for the conjugate Hilbert space: \(\overline\xi\) denotes a vector with scalar rule \(a\overline\xi=\overline{\overline a\xi}\) and inner product \(\langle\overline\xi,\overline\eta\rangle=\langle\eta,\xi\rangle\). A bounded operator \(T:H\to K\) is Hilbert–Schmidt if
\[
\|T\|_{\mathrm{HS}}^2=\sum_{i\in I}\|Te_i\|^2<\infty,
\]
where an arbitrary nonnegative sum means the supremum of its finite subsums.

**Theorem 5.1.** This definition and norm do not depend on the orthonormal basis. The Hilbert–Schmidt operators form a Hilbert space canonically isometric to \(K\otimes\overline H\), through
\[
k\otimes\overline h\longmapsto[\xi\mapsto\langle\xi,h\rangle k].
\tag{5.1}
\]
Every Hilbert–Schmidt operator is compact, and \(\|T\|\leq\|T\|_{\mathrm{HS}}\).

*Proof.* Fix bases \((e_i),(f_j)\). Parseval gives
\[
\sum_i\|Te_i\|^2=\sum_{i,j}|\langle Te_i,f_j\rangle|^2
=\sum_j\|T^*f_j\|^2.
\tag{5.2}
\]
The interchange is valid for arbitrary sums of nonnegative numbers: both iterated sums equal the supremum over finite rectangles, and each finite subset of \(I\times J\) lies in a finite rectangle. Fixing the \(f_j\) in (5.2) proves independence of \((e_i)\); the left expression then proves independence of \((f_j)\).

A square-summable array \((a_{ji})\) determines an operator. On finite linear combinations set \(Te_i=\sum_ja_{ji}f_j\). For finite-support \((c_i)\), Cauchy–Schwarz gives
\[
\left\|\sum_i c_iTe_i\right\|^2
\leq\left(\sum_i|c_i|^2\right)\left(\sum_{i,j}|a_{ji}|^2\right).
\]
It extends uniquely to a bounded operator on \(H\), with matrix \((a_{ji})\) and Hilbert–Schmidt norm equal to its \(\ell^2\) norm. Conversely every Hilbert–Schmidt operator has this matrix, so its space is complete and has the inner product of these arrays.

For the rank-one operators in (5.1), summing their matrix inner products gives \(\langle k,k'\rangle\langle h',h\rangle\). This is exactly the elementary-tensor inner product on \(K\otimes\overline H\). Finite-support matrices are finite sums of these rank-one operators and are dense among the square-summable arrays. The universal property of the tensor product therefore extends (5.1) to a unitary. Finally finite-support matrices approximate every such array in Hilbert–Schmidt norm, and hence in operator norm by the displayed estimate. They give finite-rank operators. A norm limit of finite-rank operators is compact: approximate its image of the unit ball by a finite net for the image under one finite-rank approximant. \(\square\)

**Example.** A diagonal operator on \(\ell^2(I)\) is Hilbert–Schmidt exactly when its diagonal \((a_i)\) is square summable. For uncountable \(I\), at most countably many \(a_i\) can be nonzero. The identity is Hilbert–Schmidt exactly when \(I\) is finite. This explains why an uncountable basis causes no uncountable convergence problem in (5.2).

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
If \(H\in C^1(\mathbb R)\) and \(H'\) has compact support, then \(H\) is constant on each sufficiently far tail, with values \(H_-\) and \(H_+\), and
\[
\int_{\mathbb R}H'(t)\,dt=H_+-H_-.
\]
In particular the integral is zero when these constants agree, including when \(H\in C_c^1(\mathbb R)\). Compact support of \(H'\) alone does not imply zero.

For the parameter assertion, let \(F(t,\cdot)\) be measurable and integrable for \(t\) in an open real interval about \(t_0\). Suppose the difference quotients
\[
q_h(x)=\frac{F(t_0+h,x)-F(t_0,x)}h
\]
converge almost everywhere as \(h\to0\) to a measurable \(D(x)\), and \(|q_h(x)|\leq g(x)\) almost everywhere for every sufficiently small nonzero \(h\), for one integrable \(g\). Then
\[
\left.\frac d{dt}\int F(t,x)\,d\mu(x)\right|_{t=t_0}
=\int D(x)\,d\mu(x).
\]
A limit specified only almost everywhere uses its measurable representative as in Theorem 2.2.

*Proof.* Recall the elementary differential facts involved. A continuous function on a compact interval attains its extrema. If its endpoints agree, either it is constant or one extremum occurs in the interior, where its derivative is zero: the left and right difference quotients have opposite weak signs. This is Rolle's theorem. Subtract the line joining the endpoint values to obtain the mean value theorem. The chain rule follows by substituting \(\phi(t+h)-\phi(t)=\phi'(t)h+o(h)\) into the corresponding first-order expansion of the outer function; differentiability makes the inner increment \(O(h)\).

Uniform continuity makes the difference between the upper and lower step functions on a sufficiently fine partition arbitrarily small in integral; both bound \(h\). Their Lebesgue integrals are the same interval-length sums that define the Riemann integral. For \(H\), the mean value theorem on each partition interval expresses its increment as \(H'(\xi)\) times the interval length. Summing telescopes to \(H(b)-H(a)\); uniform continuity of \(H'\) makes the sums converge to its integral.

Define \(A(v)=\int_{v_0}^v h(u)\,du\), with oriented integrals. The difference quotient of \(A\) is an interval average of \(h\), tending to \(h(v)\) by continuity. Thus \((A\circ\phi)'=(h\circ\phi)\phi'\). Apply the preceding identity to \(A\circ\phi\) to obtain (6.1). These real-calculus proofs, including endpoint conventions, are supplied in [Real analysis on closed intervals, Theorems 8, 12 and 13](../../../human/elementary-analysis/real-analysis-on-closed-intervals.html).

If \(H'=0\) outside \([a,b]\), the mean value theorem makes \(H\) constant on each exterior ray. Continuity identifies those constants with \(H(a)\) and \(H(b)\). The integral outside \([a,b]\) vanishes, so the formula above gives \(H_+-H_-\). For compactly supported \(H\), choose endpoints outside the support of \(H\), not just the support of \(H'\); both endpoint values are then zero.

For the parameter assertion fix any sequence of nonzero \(h_n\to0\). The quotients are measurable, their limit has the stated measurable representative, and their countably many exceptional sets can be combined. Dominated convergence gives \(\int q_{h_n}\to\int D\). Linearity identifies \(\int q_{h_n}\) with the difference quotient of \(\int F(t,x)\,d\mu(x)\). Since this holds for every such sequence, it gives the derivative: if a real-parameter limit failed, a fixed error would permit choices \(0<|h_n|<1/n\) witnessing failure. This proves the parameter formula. ∎

**Example (A derivative with integral one).** Set \(H(t)=0\) for \(t\leq0\), \(H(t)=3t^2-2t^3\) for \(0\leq t\leq1\), and \(H(t)=1\) for \(t\geq1\). The polynomial values and first derivatives match at both endpoints, so \(H\in C^1(\mathbb R)\). Its derivative is \(6t-6t^2\) on \([0,1]\) and zero outside, hence is continuous and compactly supported. Nevertheless its integral is \(H_+-H_-=1\).

## 7. Exercises with complete solutions

**1 (easy): finite-measure support.** Prove that \(f\in L^p\), \(p<\infty\), has sigma-finite support without assuming \(X\) sigma-finite. Explain why the same assertion fails for \(p=\infty\).

*Solution.* The support in the measure-theoretic sense \(\{f\ne0\}\) is \(\bigcup_n\{|f|>1/n\}\). On each set, \(n^{-p}\mu(\{|f|>1/n\})\leq\int|f|^p\), so its measure is finite. On an uncountable counting space, \(1\in L^\infty\) has all of \(X\) as support, which cannot be covered by countably many finite sets.

**2 (medium): a summable series in \(L^p\).** If \(\sum_n\|u_n\|_p<\infty\), \(p<\infty\), prove that \(\sum_nu_n\) converges almost everywhere and in \(L^p\), and estimate every tail.

*Solution.* Minkowski bounds the norm of \(\sum_{n=1}^N|u_n|\) by \(\sum_n\|u_n\|_p\). Monotone convergence of its \(p\)-th power shows that \(\sum_n|u_n|<\infty\) almost everywhere. Thus the series converges there. Apply the same argument to a tail, obtaining \(\|\sum_{n\geq N}u_n\|_p\leq\sum_{n\geq N}\|u_n\|_p\to0\). Define the sum as zero on the measurable exceptional set.

**3 (medium): failure of domination.** On \((0,1)\) with Lebesgue measure put \(u_n=n1_{(0,1/n)}\). Find its pointwise limit and its integral. Prove that no integrable common dominator exists.

*Solution.* Every \(x>0\) eventually lies outside \((0,1/n)\), so \(u_n(x)\to0\). Yet \(\int u_n=1\). If \(|u_n|\leq g\) for an integrable \(g\), dominated convergence would force these integrals to tend to zero, a contradiction. The shrinking support does not replace domination.

**4 (hard): weighted finite reduction.** For sigma-finite \(\mu\), construct a strictly positive measurable \(w\) with \(\int w\,d\mu<\infty\). Prove that \(w\mu\) has the same null sets, and that multiplication by \(w^{-1/2}\) gives a unitary from \(L^2(\mu)\) to \(L^2(w\mu)\).

*Solution.* Partition \(X\) into finite-measure measurable \(E_n\) and take \(w=\sum_n2^{-n}(1+\mu(E_n))^{-1}1_{E_n}\). Then \(w>0\) and \(\int w\leq1\). For any measurable \(E\), \(\int_Ew=0\) implies \(\mu(E\cap\{w\geq1/n\})=0\) for each \(n\), hence \(\mu(E)=0\). The converse is immediate. The norm identity is \(\int|w^{-1/2}f|^2w\,d\mu=\int|f|^2\,d\mu\), and the inverse is multiplication by \(w^{1/2}\).

**5 (hard): which tensor represents an operator?** Explain why \(K\otimes H\) is not the canonical tensor for complex-linear rank-one maps \(H\to K\), and verify (5.1) on two rank-one maps.

*Solution.* The map \(h\mapsto[\xi\mapsto\langle\xi,h\rangle k]\) is conjugate-linear in \(h\), while elementary tensors are bilinear in their factors. Passing to \(\overline H\) makes it linear. For \(T\xi=\langle\xi,h\rangle k\) and \(S\xi=\langle\xi,h'\rangle k'\), Parseval gives \(\sum_i\langle Te_i,Se_i\rangle=\langle k,k'\rangle\sum_i\langle e_i,h\rangle\overline{\langle e_i,h'\rangle}=\langle k,k'\rangle\langle h',h\rangle\), the required tensor inner product.

## What this enables

The next lesson uses Theorem 1.1 to construct Radon measures, Theorems 2.1–3.2 to pass to limits and complete \(L^p\), and Theorems 4.1–4.2 on the sigma-finite pieces of a general group. Its Radon-product theorem proves the additional hypotheses required for iterated integration; none are implicit in this lesson. Hilbert tensors then identify \(L^2\) of that product, and Theorem 5.1 interprets square-integrable kernels as Hilbert–Schmidt operators.

## References

- [Erdman] J. M. Erdman, *Functional Analysis and Operator Algebras: An Introduction*, version 4 October 2015, [author's text and editable sources](https://web.pdx.edu/~erdman/). The core Functional Analysis course uses this text. Its Hilbert–Schmidt exercises concern separable spaces; Theorem 5.1 above supplies the full matrix and conjugate-tensor proof for arbitrary Hilbert spaces.
- [Paschke] W. L. Paschke, *Lecture Notes in Functional Analysis*, edition 0.9, [author's Hilbert–Schmidt chapter](https://orthogonalpublishing.com/lnfa/html/hilbertschmidt.html). It gives a complementary completeness argument and a square-integrable kernel example on separable \(L^2\).

- [Hilbert tools] *Hilbert spaces and compact operators*, programme lesson by Claude Opus 5.5 (Anthropic), October 2026, CC0, Theorems 2.1–2.3, 4.1 and 8.1. These are preceding internal full-proof providers.
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1 and 2, Torres Fremlin, 2000–2001. [Freely accessible text and supplied editable TeX](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm). Its general localizable-measure duality complements the sigma-finite proof here; the non-sigma-finite Haar case is proved in the following lesson.
- [Lebesgue] H. Lebesgue, *Leçons sur l'intégration et la recherche des fonctions primitives*, Gauthier-Villars, 1904, [freely accessible historical edition](https://fr.wikisource.org/wiki/Leçons_sur_l’intégration_et_la_recherche_des_fonctions_primitives_(première_édition)). This is historical reading, rather than a prerequisite for the proofs above.

- [Lebl] J. Lebl, *Basic Analysis I* and *Basic Analysis II*, [author’s open reader](https://www.jirka.org/ra/). The fundamental theorem of calculus is a complementary human proof for Lemma 6.1.

- [Axler] S. Axler, [*Measure, Integration & Real Analysis*](https://measure.axler.net/MIRA.pdf), author’s freely accessible edition dated 12 June 2026. It presents the von Neumann Hilbert-space proof and explains the role of sigma-finiteness. The proof and counterexample above are independently written.
