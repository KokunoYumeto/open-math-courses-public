# Local fields: classification and Haar measure

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

Multiplication by a nonzero element of a field changes additive volume by a fixed factor. For a nondiscrete locally compact field, that factor measures size well enough to recover the topology. We will derive an absolute value from it, classify the fields that result, and compute additive and multiplicative Haar measures explicitly.

Throughout, a topological field is commutative and Hausdorff, with continuous addition, multiplication and inversion on its nonzero elements. A **local field** means a nondiscrete locally compact topological field; this convention includes \(\mathbf R\) and \(\mathbf C\). No absolute value is part of the initial hypothesis.

We use measure theory from [**Measure and Hilbert space tools for Haar integration**, Theorems 2.1–2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools.html#2-integration-and-convergence-without-countability-assumptions), the Haar theorem from [**Haar measure on locally compact groups**](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups.html), and the preceding lessons **Completions, the p-adic numbers and complete discretely valued fields** and **Extensions of complete valued fields**. A Haar measure is a nonzero translation-invariant Radon measure: compact sets have finite measure, nonempty open sets have positive measure, and outer regularity holds on Borel sets. Its existence and uniqueness up to a positive scalar are imported, with precise locators at the end.

## 1. Volume supplies a continuous size

Let \(\mu\) be additive Haar measure on \(K\). For \(a\ne0\), multiplication by \(a\) is an automorphism of the additive group. Therefore \(E\mapsto\mu(aE)\) is another additive Haar measure. Uniqueness defines a positive number \(m(a)\) by
\[
\mu(aE)=m(a)\mu(E).
\]
Put \(m(0)=0\). We call \(m=\operatorname{mod}_K\) the **Haar modulus of the field**.

The compactness step used below does not require a metric. If \(C\subset K\) is compact and \(aC\subset U\) with \(U\) open, continuity of multiplication gives, for each \(c\in C\), open neighborhoods \(W_c\) of \(a\) and \(V_c\) of \(c\) with \(W_cV_c\subset U\). Finitely many \(V_c\) cover \(C\). The intersection of the corresponding \(W_c\) is an open neighborhood \(W\) of \(a\), and \(WC\subset U\). This applies both at \(a=0\) and at a nonzero \(a\), including when \(U\) is chosen using outer regularity of Haar measure.

**Proposition 1.1 (continuity and compact size bounds).** The definition is independent of the Haar normalization and of the Borel set of finite positive measure used to compute it. The modulus is multiplicative, continuous on \(K\), and positive away from zero. For every \(r\ge0\), the set
\[
B_r=\{x\in K\mid m(x)\le r\}
\]
is compact. The sets \(\{m<\varepsilon\}\), for \(\varepsilon>0\), form a neighborhood basis at zero in the original topology.

*Proof.* Scaling \(\mu\) cancels from the ratio \(\mu(aE)/\mu(E)\). The defining equality holds for every Borel set, so any one of finite positive measure gives the same ratio. Composition of multiplication maps gives
\[
m(ab)=m(a)m(b),\quad m(1)=1,\quad
m(a^{-1})=m(a)^{-1},\quad m(-1)=1.
\]
The last identity follows from positivity and \(m(-1)^2=1\). The equality for products involving zero follows from the definition.

First observe that every point has Haar measure zero. Otherwise translation invariance gives the same positive mass to every point. A compact neighborhood of zero would then contain only finitely many points, since its measure is finite. A finite neighborhood in a Hausdorff topological group makes zero isolated, and all translations become isolated, contrary to nondiscreteness.

Fix a compact neighborhood \(V\) of zero, so \(0<\mu(V)<\infty\). For \(a\in K\) and \(\eta>0\), outer regularity supplies an open \(U\) containing \(aV\) with
\[
\mu(U)<\mu(aV)+\eta.
\]
For \(a=0\), this uses the just-proved zero measure of the singleton. Compactness of \(V\) and continuity of multiplication give a neighborhood \(W\) of \(a\) with \(WV\subset U\). Consequently
\[
m(x)\le m(a)+\eta/\mu(V)\quad(x\in W).
\]
This proves continuity at zero and upper semicontinuity elsewhere. On \(K^\times\), apply the same upper bound at \(a^{-1}\), together with continuous inversion and \(m(x)=1/m(x^{-1})\), to obtain lower semicontinuity. Thus \(m\) is continuous.

We next choose a scalar that contracts \(V\). Compactness gives a neighborhood \(W_0\) of zero with \(W_0V\subset\operatorname{int}V\). Continuity of \(m\) at zero and nondiscreteness allow a nonzero
\[
c\in W_0\cap V,\qquad 0<m(c)<1.
\]
Every positive power of \(c\) lies in \(V\). Any cluster point of this sequence has modulus zero, so is zero. It follows that \(c^n\to0\). To justify this before having a metric, if infinitely many terms lay outside a neighborhood of zero, compactness would give a convergent subnet of those terms with limit outside that neighborhood's interior, contradicting the only possible cluster point. We may equivalently take the neighborhood open, whose complement is closed.

The compact sets \(c^{-n}V\) increase and cover \(K\), since \(c^nx\to0\) for each \(x\). Set
\[
A=\overline{V\setminus cV}.
\]
This compact set excludes zero because \(cV\) is a neighborhood of zero. It is nonempty: \(cV\subset V\) and \(\mu(cV)=m(c)\mu(V)<\mu(V)\). Thus \(\delta=\min_A m>0\).

For \(x\notin V\), let \(n\ge1\) be the first integer with \(c^nx\in V\). The preceding term is outside \(V\), so \(c^nx\notin cV\), and
\[
\delta\le m(c)^n m(x).
\]
If \(m(x)\le r\), this bounds \(n\) above by an integer depending only on \(r\). Hence \(B_r\) lies in a single compact set \(c^{-N}V\). It is closed by continuity, so it is compact. The case \(r=0\) is \(B_0=\{0\}\).

Finally, let \(U\) be any neighborhood of zero and choose a compact neighborhood \(V_1\subset U\). Choose \(r>0\) larger than every modulus on \(V_1\). The compact set \(B_r\setminus\operatorname{int}V_1\), if nonempty, has a positive minimum modulus. Choosing \(\varepsilon\) smaller than this minimum and than \(r\) ensures \(\{m<\varepsilon\}\subset V_1\subset U\). If the compact difference is empty, any \(\varepsilon\le r\) works. The strict modulus sets are already open by continuity. This proves the basis assertion. \(\square\)

This proposition also makes \(K\) a countable union of compact sets, namely the \(B_n\). Countability was a consequence, rather than a condition imposed on the field.

## 2. An ordinary absolute value from the modulus

The modulus need not itself be an absolute value: complex multiplication scales area by squared modulus. A power corrects this.

**Proposition 2.1 (a power satisfying the triangle inequality).** There is \(t>0\) such that \(\rho(x)=m(x)^t\) is a nontrivial ordinary absolute value and induces the given topology of \(K\).

*Proof.* By Proposition 1.1, \(B_1\) is compact. Define
\[
C=\max_{u\in B_1}m(1+u)\ge1.
\]
If \(m(x)\ge m(y)\) and \(x\ne0\), divide by \(x\) to get
\[
m(x+y)\le C\max\{m(x),m(y)\}.
\tag{2.1}
\]
The other cases follow by symmetry or by a zero summand. If \(C=1\), \(m\) already satisfies the ultrametric inequality, and we take \(t=1\).

Suppose \(C>1\), and put \(s=\log_2 C>0\). Repeatedly pairing summands in (2.1), padding by zeros to a power of two, gives
\[
m(z_1+\cdots+z_N)
\le C^{\lceil\log_2N\rceil}\max_i m(z_i)
\le C N^s\max_i m(z_i).
\tag{2.2}
\]
In particular, for a positive integer \(k\), interpreted in \(K\),
\[
m(k\cdot1)\le C k^s.
\]
This estimate remains valid if the integer becomes zero in positive characteristic.

If either \(x\) or \(y\) is zero, the desired triangle inequality is immediate, so assume both are nonzero. Write \(A=m(x)^{1/s}\) and \(D=m(y)^{1/s}\). Apply (2.2) to the \(n+1\) terms in the binomial expansion of \((x+y)^n\). Each term has modulus at most
\[
C\left(\binom nj A^j D^{n-j}\right)^s
\le C(A+D)^{ns}.
\]
When a summand vanishes this inequality is automatic. We obtain
\[
m(x+y)^n\le C^2(n+1)^s(A+D)^{ns}.
\]
Taking \(n\)-th roots and letting \(n\to\infty\) shows
\[
m(x+y)^{1/s}\le m(x)^{1/s}+m(y)^{1/s}.
\]
Thus \(t=1/s\) works. Multiplicativity, positivity, the values at zero and one, and nontriviality follow from Proposition 1.1 and the element \(c\) used there. The balls for any positive power of \(m\) give the same neighborhood basis, proving the topological assertion. \(\square\)

**Corollary 2.2 (completeness).** The field \(K\) is complete for \(\rho\).

*Proof.* A Cauchy sequence is bounded in \(\rho\), hence in \(m\), and lies in a compact \(B_r\). After Proposition 2.1 this is a compact metric space, so the sequence has a convergent subsequence. The Cauchy condition forces the entire sequence to converge to the same point. \(\square\)

## 3. Compactness forces a discrete valuation

Suppose \(\rho\) is nonarchimedean. Define
\[
\mathcal O=\{\rho\le1\},\qquad
\mathfrak m=\{\rho<1\}.
\]

**Proposition 3.1 (the finite residue field and uniformizer).** The ring \(\mathcal O\) is compact and open; its unit group is \(\{\rho=1\}\), and its unique maximal ideal \(\mathfrak m\) is compact and open. There is a \(\pi\in\mathfrak m\setminus\{0\}\) and an integer-normalized discrete valuation \(v\) such that
\[
\mathfrak m=\pi\mathcal O,\qquad
\rho(K^\times)=\rho(\pi)^{\mathbf Z},\qquad
\mathcal O/\mathfrak m=\mathbf F_q,\qquad
m(x)=q^{-v(x)}.
\]
The ideals \(\pi^n\mathcal O\) form a neighborhood basis at zero. The ring \(\mathcal O\) is the unique maximal compact subring of \(K\).

*Proof.* The ultrametric inequality makes \(\mathcal O\) a subring and \(\mathfrak m\) an ideal. For a nonzero element of \(\mathcal O\), its inverse is integral exactly when its value is \(1\). Thus \(\mathfrak m\) contains precisely the nonunits and is the unique maximal ideal. Compactness of \(\mathcal O\) follows from Proposition 1.1, since \(\rho=m^t\). It is open: a translate of the open ball \(\{\rho<1\}\) around any integral element stays integral.

The unit set is open as well. If \(\rho(u)=1\) and \(\rho(h)<1\), strict ultrametric dominance gives \(\rho(u+h)=1\). Hence \(\mathfrak m\), the complement of the units in \(\mathcal O\), is closed in \(\mathcal O\) and therefore compact. It is open by continuity.

Nondiscreteness supplies a nonzero element of \(\mathfrak m\). Compactness shows that its positive maximum value is attained:
\[
\lambda=\max_{x\in\mathfrak m}\rho(x)<1,\qquad
\rho(\pi)=\lambda.
\]
For \(x\in\mathfrak m\), \(\rho(x/\pi)\le1\), so \(\mathfrak m=\pi\mathcal O\). There is no value in \((\lambda,1)\). For any \(x\ne0\), choose an integer \(n\) with
\[
\lambda^{n+1}<\rho(x)\le\lambda^n.
\]
Then \(\lambda<\rho(\pi^{-n}x)\le1\), forcing this value to be \(1\). Therefore \(\rho(x)=\lambda^n\). Define \(v(x)=n\), and \(v(0)=+\infty\). Multiplicativity and the ultrametric inequality give the valuation axioms; its value group is \(\mathbf Z\). The formulas for its balls prove the neighborhood assertion.

The field \(\mathcal O/\mathfrak m\) is compact as a quotient of \(\mathcal O\) and discrete because \(\mathfrak m\) is open. It is therefore a finite field, say of order \(q\). Its \(q\) additive cosets in \(\mathcal O\) have the same measure, and hence
\[
\mu(\mathcal O)=q\,\mu(\pi\mathcal O)
=q\,m(\pi)\mu(\mathcal O).
\]
Since \(\mu(\mathcal O)\) is finite and positive, \(m(\pi)=q^{-1}\). For a unit \(u\), \(\rho(u)=1\) implies \(m(u)=1\). Writing \(x=\pi^{v(x)}u\) proves \(m(x)=q^{-v(x)}\).

The ring is a DVR: in a nonzero ideal, choose an element with the least nonnegative valuation; division shows it generates the ideal. If \(R\) is any compact subring of \(K\), continuity bounds \(m\) on \(R\). An element \(x\in R\) with \(m(x)>1\) would have powers in \(R\) of unbounded modulus. Thus \(R\subset\mathcal O\), proving the final assertion. \(\square\)

In particular, in this case the Haar modulus itself is an ultrametric absolute value, even if Proposition 2.1 initially chose another power.

## 4. The finite-dimensionality needed for classification

**Lemma 4.1 (Riesz).** Let \(k\) be a complete field with a nontrivial absolute value, and let \(V\) be a normed \(k\)-vector space. If \(V\) is locally compact in its norm topology, then \(V\) is finite-dimensional.

*Proof.* Choose \(a\in k\) with \(0<|a|<1\). A compact neighborhood of zero contains a closed norm ball of some positive radius. By scaling by a sufficiently small power of \(a\), and then back, it follows that the closed unit ball is compact.

Every finite-dimensional subspace \(W\) is complete by finite-dimensional norm equivalence over the complete field \(k\), and is consequently closed in \(V\). If \(W\ne V\), choose \(x\notin W\). Its distance \(d\) from \(W\) is positive. Select \(w\in W\) with
\[
\|x-w\|<2d,
\]
and put \(z=x-w\). Scaling \(z\) by a suitable integer power of \(a\) gives a vector \(y\) with
\[
|a|<\|y\|\le1,\qquad
\operatorname{dist}(y,W)>\tfrac12|a|.
\]
Indeed the distance scales by exactly the same scalar factor as the norm, and \(d>\|z\|/2\).

If \(V\) were infinite-dimensional, repeat this with \(W\) the span of the previously selected vectors. It produces infinitely many points in the unit ball whose pairwise distances exceed \(|a|/2\). A compact metric space has a finite cover by balls of radius \(|a|/6\), each containing at most one of these points. This contradiction proves finite-dimensionality. \(\square\)

Completeness of the scalar field is essential in the closed-subspace step. Nondiscreteness supplies a scalar of value strictly between zero and one; a trivially valued field does not satisfy that condition.

## 5. Classification in every characteristic

**Theorem 5.1 (classification of local fields).** Every nondiscrete locally compact topological field is isomorphic as a topological field to exactly one of the following types:
\[
\mathbf R,\qquad \mathbf C,\qquad
\text{a finite extension of }\mathbf Q_p,\qquad
\mathbf F_q((T)).
\]
Here \(p\) is a prime and \(q\) is a prime power. Conversely, every field in this list, with its usual topology, is nondiscrete and locally compact.

*Proof.* Construct \(\rho\) by Proposition 2.1; the given field is complete for it by Corollary 2.2. If \(\rho\) is archimedean, the complete archimedean classification in Theorem 2.4 of **Completions, the p-adic numbers and complete discretely valued fields** gives \(\mathbf R\) or \(\mathbf C\), with an equivalent power of its usual absolute value. Equivalence makes the field isomorphism topological.

If \(\rho\) is nonarchimedean, Proposition 3.1 supplies a complete discrete valuation with finite residue field \(\mathbf F_q\), of characteristic \(p\).

First assume \(\operatorname{char}K=0\). The integer \(p\) reduces to zero in the residue field, so \(v(p)>0\). A rational prime different from \(p\) reduces to a nonzero element of the residue prime field and is a unit. Multiplicativity therefore shows that the absolute value restricted to \(\mathbf Q\) is a positive power of the \(p\)-adic value. Completeness extends the inclusion of \(\mathbf Q\) to a topological embedding \(\mathbf Q_p\hookrightarrow K\).

View \(K\) as a normed vector space over \(\mathbf Q_p\), using its chosen absolute value and its restriction on the base. That base value is equivalent to the usual one, remains complete and is nontrivial. The vector-space topology is exactly the original field topology, so the space is locally compact. Lemma 4.1 shows that its dimension is finite. Finite-dimensional norm equivalence identifies its topology with the usual topology on a finite extension of \(\mathbf Q_p\).

Now assume \(K\) has positive characteristic. Its prime subfield injects into the residue field, so its characteristic is \(p\). We construct an actual coefficient field in \(\mathcal O\). For each residue class, the polynomial
\[
X^q-X
\]
has a simple root in that class, because its derivative in characteristic \(p\) is \(-1\). Hensel's lemma gives a unique root in \(\mathcal O\) lifting each residue element. There are exactly \(q\) such roots. They form a field: the \(q\)-power map is a ring homomorphism in characteristic \(p\), so sums, products and negatives of roots are roots, as are inverses of nonzero roots. Reduction identifies this subfield \(A\) with \(\mathbf F_q\).

Choose a uniformizer \(\pi\). The digit expansion theorem for complete discrete valuations now gives, uniquely,
\[
x=\sum_{n\ge n_0}a_n\pi^n,\qquad a_n\in A.
\]
Thus substitution \(T\mapsto\pi\), with the residue-field lift for coefficients, defines a bijection
\[
A((T))\longrightarrow K.
\]
It respects addition and multiplication. These identities hold for finite truncations, and the omitted tails tend to zero; alternatively, each fixed coefficient of a Laurent-series product involves only finitely many pairs of terms. A series with first nonzero coefficient at exponent \(n\) has valuation \(n\), so the map and its inverse respect the valuation topologies. This proves the asserted topological field isomorphism.

For the converse, \(\mathbf R\) and \(\mathbf C\) have their usual locally compact nondiscrete topologies. Finite extensions of \(\mathbf Q_p\) are finite-dimensional normed spaces over \(\mathbf Q_p\); norm equivalence identifies them with \(\mathbf Q_p^d\) topologically, which is locally compact. Powers of a uniformizer approach zero and show nondiscreteness. For \(\mathbf F_q((T))\), the ring \(\mathbf F_q[[T]]\) is topologically the compact product of its finite coefficient sets. It is an open neighborhood of zero; its translates give local compactness, and \(T^n\to0\) proves nondiscreteness.

The types are distinct. Positive characteristic separates the Laurent-series fields from the others. Among characteristic-zero fields, \(\mathbf R,\mathbf C\) are connected, while the nonarchimedean fields have open-and-closed valuation balls separating any two points. Finally \(\mathbf R\) admits an ordering and has no square root of \(-1\), while \(\mathbf C\) does. \(\square\)

The integer \(p\) and a uniformizer should not be confused. In characteristic zero, \(p=u\pi^e\) for a unit \(u\) and some \(e\ge1\). In characteristic \(p\), the integer \(p\) is zero in the field; the nonzero uniformizer is still available.

## 6. Additive and multiplicative Haar measures

For \(\mathbf R\), choose Lebesgue measure; multiplication by \(a\) scales it by \(|a|\), so \(m(a)=|a|\). For \(\mathbf C\), choose planar Lebesgue measure \(dx\,dy\). The real determinant of multiplication by \(z=x+iy\) is \(x^2+y^2\), giving
\[
\operatorname{mod}_{\mathbf C}(z)=|z|^2.
\]
Doubling the complex Haar measure, as in some automorphic conventions, does not change this modulus.

For a nonarchimedean local field, let \(\pi\) be a uniformizer, let \(q\) be the residue cardinality, and normalize additive measure by \(\mu(\mathcal O)=1\). Write
\[
|x|_K=q^{-v(x)}=m(x).
\]
This is the normalized local size used in the preceding product-formula lesson.

**Proposition 6.1 (balls, units and integration).** For \(a\in K\) and \(n\in\mathbf Z\),
\[
\mu(a+\pi^n\mathcal O)=q^{-n}.
\]
The measure on \(K^\times\) defined by
\[
d^\times x=\frac{dx}{|x|_K}
\]
is multiplicative Haar measure, with
\[
\mu^\times(\mathcal O^\times)=1-q^{-1}.
\]
For \(s\in\mathbf C\) with \(\operatorname{Re}s>-1\),
\[
\int_{\mathcal O}|x|_K^s\,dx
=\frac{1-q^{-1}}{1-q^{-1-s}}.
\]

*Proof.* Translation invariance and the modulus formula give
\[
\mu(a+\pi^n\mathcal O)=m(\pi)^n\mu(\mathcal O)=q^{-n},
\]
also for negative \(n\).

The density \(1/m(x)\) is continuous and positive on \(K^\times\), and bounded on its compact subsets. Thus it defines a nonzero Radon measure there. Under multiplication by \(b\ne0\), additive measure gains a factor \(m(b)\), while the denominator gains the same factor. Explicitly, for a Borel set \(E\subset K^\times\),
\[
\int_{bE}\frac{dx}{m(x)}
=\int_E\frac{m(b)\,dx}{m(bx)}
=\int_E\frac{dx}{m(x)}.
\]
This is multiplicative invariance. On \(\mathcal O^\times\), the denominator is \(1\), and its additive volume is \(1-\mu(\pi\mathcal O)=1-q^{-1}\).

The scalar series calculation can be checked directly. If \(|r|<1\), finite cancellation gives \((1-r)\sum_{n=0}^N r^n=1-r^{N+1}\). For \(0<t<1\), induction gives \(t^{-N}\ge 1+N(t^{-1}-1)\), so \(t^N\to0\); the case \(t=0\) is immediate. Apply this to \(t=|r|\). The partial sums therefore converge to \((1-r)^{-1}\), and applying the same identity to \(|r|\) proves absolute convergence. If \(|r|\ge1\), the terms do not tend to zero, so the series cannot converge. In the shell calculation take \(r=q^{-(1+s)}\), whose absolute value is \(q^{-(1+\operatorname{Re}s)}\). Theorems 2.1–2.2 of the measure lesson identify the integral of the shell sum with the limit of its partial integrals: monotone convergence first makes the absolute shell sum integrable, and that sum dominates the complex partial sums.

For the integral, zero has measure zero. The disjoint shells \(\pi^n\mathcal O^\times\), for \(n\ge0\), have measure \((1-q^{-1})q^{-n}\), and \(|x|_K^s=q^{-ns}\) on the \(n\)-th shell. Their absolute integrals are summable precisely when \(\operatorname{Re}s>-1\). Hence
\[
\int_{\mathcal O}|x|_K^s\,dx
=(1-q^{-1})\sum_{n\ge0}q^{-n(1+s)}
=\frac{1-q^{-1}}{1-q^{-1-s}}.
\]
The value assigned to the integrand at zero is immaterial. \(\square\)

The unit-volume multiplicative normalization is instead
\[
d^\times_{\!1}x=
\frac{dx}{(1-q^{-1})|x|_K}.
\]
It gives \(\mathcal O^\times\) volume \(1\). Both are Haar measures, and their constant ratio must be carried through an integral.

**Example 6.2.** For \(\mathbf Q_p\), \(q=p,\pi=p\); thus
\[
m(a)=|a|_p,\qquad
\mu(\mathbf Z_p^\times)=1-p^{-1},\qquad
\mu(1+p^n\mathbf Z_p)=p^{-n}\quad(n\ge1).
\]
For \(\mathbf F_q((T))\), multiplication by \(T\) removes one free coefficient in its integral ring, giving \(m(T)=q^{-1}\). For \(\mathbf C\), multiplication by \(2\) has modulus \(4\). These are length, coefficient-count and area factors of the same definition.

## 7. Exercises

1. For \(n\ge1\) and additive measure with \(\mu(\mathbf Z_p)=1\), compute the measures of \(1+p^n\mathbf Z_p\) and \(\mathbf Z_p^\times\). Compute their multiplicative measures with \(dx/|x|_p\), and again with the unit group normalized to volume \(1\).

2. Derive \(m(a)=|a|_p\) in \(\mathbf Q_p\) directly from the additive volume of \(a\mathbf Z_p\), including negative valuations.

3. Prove Lemma 4.1, explaining both why finite-dimensional subspaces are closed and why a discrete range of norm values causes no problem.

4. Starting with a nondiscrete Hausdorff locally compact field of characteristic \(p\), construct its coefficient field and uniformizer and prove the topological isomorphism with \(\mathbf F_q((T))\).

## 8. Complete solutions

**Solution 1.** Additive translation invariance gives
\[
\mu(1+p^n\mathbf Z_p)=\mu(p^n\mathbf Z_p)=p^{-n},
\qquad
\mu(\mathbf Z_p^\times)=1-p^{-1}.
\]
Both sets consist of units when \(n\ge1\), so \(1/|x|_p=1\) on them. Thus these are also their measures for \(dx/|x|_p\). For \(d^\times_{\!1}x\), divide both answers by \(1-p^{-1}\):
\[
\mu^\times_1(\mathbf Z_p^\times)=1,\qquad
\mu^\times_1(1+p^n\mathbf Z_p)=
\frac{p^{-n}}{1-p^{-1}}=
\frac1{(p-1)p^{n-1}}.
\]
This last denominator is also the index of \(1+p^n\mathbf Z_p\) in the unit group, by reduction to \((\mathbf Z/p^n\mathbf Z)^\times\).

**Solution 2.** Write \(a=p^ku\), with \(u\in\mathbf Z_p^\times\) and \(k\in\mathbf Z\). Since \(u\mathbf Z_p=\mathbf Z_p\), it suffices to measure \(p^k\mathbf Z_p\). For \(k\ge0\), \(\mathbf Z_p\) is the disjoint union of \(p^k\) translates of \(p^k\mathbf Z_p\), so each has volume \(p^{-k}\). For \(k<0\), the group \(p^k\mathbf Z_p\) is a union of \(p^{-k}\) translates of \(\mathbf Z_p\), so its volume is \(p^{-k}\) again. Therefore
\[
m(a)=\frac{\mu(a\mathbf Z_p)}{\mu(\mathbf Z_p)}
=p^{-k}=|a|_p.
\]
Haar uniqueness then gives the same scaling factor for every Borel set of finite positive additive measure.

**Solution 3.** Let \(U\) be a compact neighborhood in \(V\), and choose \(r>0\) so that the closed ball of radius \(r\) lies in \(U\). Choose \(a\in k\) with \(0<|a|<1\) and an integer \(j\) with \(|a|^j\le r\). The closed ball of radius \(|a|^j\) is compact as a closed subset of \(U\). Its image under multiplication by \(a^{-j}\) is the closed unit ball, so that ball is compact.

A finite-dimensional subspace \(W\), with the induced norm, is complete by Proposition 2.1 of **Extensions of complete valued fields**, since \(k\) is complete. Any limit in \(V\) of a sequence in \(W\) is a limit of a Cauchy sequence and hence lies in \(W\). In a metric space this proves closedness.

For a proper such \(W\), choose \(x\notin W\). Closedness implies \(d=\operatorname{dist}(x,W)>0\). Choose \(w\in W\) with \(\|x-w\|<2d\). For \(z=x-w\), select an integer \(h\) so that
\[
|a|<|a|^h\|z\|\le1.
\]
Such an \(h\) always exists, regardless of which values the norm attains. Put \(y=a^hz\). Since \(W\) is a vector subspace,
\[
\operatorname{dist}(y,W)=|a|^h d
\mathrel{>}\tfrac12|a|^h\|z\|>\tfrac12|a|.
\]
In an infinite-dimensional space, successive choices outside the span of preceding vectors produce infinitely many points of the unit ball separated by more than \(|a|/2\). Compactness supplies a finite cover by balls of radius \(|a|/6\); the ordinary triangle inequality shows that none can contain two selected points. This contradiction proves the lemma.

**Solution 4.** Proposition 2.1 supplies an absolute value inducing the original topology. Since the prime subfield is finite, the absolute values of integers are bounded; the nonarchimedean criterion from **Absolute values, valuations and Ostrowski's theorem** makes this value ultrametric. Proposition 3.1 supplies a finite residue field \(\kappa=\mathbf F_q\), a uniformizer \(\pi\), and a discrete valuation. Corollary 2.2 supplies completeness.

Lift every element of \(\kappa\) by Hensel's lemma applied to \(X^q-X\), whose derivative is \(-1\). The \(q\) lifted roots form a field \(A\): in characteristic \(p\), taking the \(q\)-th power commutes with addition and multiplication, and also with inversion of a nonzero element. Reduction is a bijective field homomorphism \(A\to\kappa\).

For \(x\in\mathcal O\), choose its constant coefficient \(a_0\in A\) from its residue, divide \(x-a_0\) by \(\pi\), and repeat. The digit theorem proves convergence and uniqueness of
\[
x=a_0+a_1\pi+a_2\pi^2+\cdots.
\]
Multiplying an arbitrary nonzero field element by a power of \(\pi\) reduces to this integral case, giving a Laurent expansion with only finitely many negative exponents. Map \(\sum a_nT^n\) to \(\sum a_n\pi^n\). The unique expansion makes this map bijective; truncation and continuous field operations prove the algebra identities. The first nonzero coefficient determines the same integer valuation on both sides, so the map carries \(T^nA[[T]]\) onto \(\pi^n\mathcal O\) for every integer \(n\). These are neighborhood bases, proving that both map and inverse are continuous. Identifying \(A\) with \(\mathbf F_q\) finishes the construction.

## 9. What this lesson does not prove

- Existence and uniqueness of Haar measure, and positivity on nonempty open sets, are Theorem 8.3, Theorem 9.2 and Proposition 9.1 of **Haar measure on locally compact groups**. Radon outer regularity and finiteness on compact sets are its Definition 2.1. Basic compact-neighborhood and tube arguments are the topology tools in its Section 1.
- Completion and its universal property, the complete archimedean classification, and digit expansions are Theorems 2.1 and 2.4 and Proposition 2.3 of **Completions, the p-adic numbers and complete discretely valued fields**.
- Finite-dimensional norm equivalence and completeness are Proposition 2.1 of **Extensions of complete valued fields**. This lesson proves the locally compact infinite-dimensional obstruction separately.
- The equivalence between bounded integer values and the ultrametric inequality is Proposition 1.1 of **Absolute values, valuations and Ostrowski's theorem**. Simple-root Hensel lifting is Corollary 1.2 of **Hensel's lemma, squares and roots of unity in p-adic fields**.
- Compactness of arbitrary products of compact spaces is [Tychonoff’s theorem, Theorem 2.3 of Weak topologies](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-02). Its finite discrete factors give the compact coefficient product used in Theorem 5.1.
- The complete-and-totally-bounded criterion and sequential compactness for metric spaces are [Lemma 5.0 of Hilbert spaces and compact operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html#OA-FND-HS-10). They supply the compact metric subsequence argument in Corollary 2.2 and the finite-ball-cover argument in Lemma 4.1.
- Monotone and dominated convergence are [Theorems 2.1–2.2 of Measure and Hilbert space tools for Haar integration](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools.html#2-integration-and-convergence-without-countability-assumptions), with no sigma-finiteness or completeness assumption on the measure. Limits are measurable functions or their specified measurable representatives. The finite geometric-series identity and the absolute-convergence calculation used for the shells are proved in Proposition 6.1 above.

The additive measure fixed here gives the integral ring volume \(1\). The choice of a self-dual measure relative to an additive character is a further normalization, treated in the adèle lessons. No self-dual convention is inferred from the present Haar normalization.

## References

J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 7, Proposition 7.46, Corollary 7.47 and Remark 7.49.

J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*, author draft, 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §3.5, pp. 75–76, especially Lemma 3.5.1 and the two multiplicative measure normalizations. This citation identifies the complete freely available author draft.

J.-B. Bost and A. Connes, [*Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf), Selecta Mathematica 1 (1995), 411–457, §3, Proposition 9.

The overlapping modulus results are also treated in *The Bost–Connes Hecke algebra*, Section 10, “Recovering a local field from its Haar modulus”: Lemma 10.1 gives continuity, properness and the original topology; Lemma 10.2 gives the archimedean alternative; Theorem 10.3 gives the compact valuation ring and residue normalization. Theorem 5.1 here adds the full field classification, including the coefficient-field construction, and Proposition 6.1 gives the integration formulas.
