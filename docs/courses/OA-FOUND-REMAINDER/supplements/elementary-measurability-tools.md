# Elementary measurability tools

*Self-checked by the writing AI. Original text: CC0 1.0.*

The first two results supply the exact background used in the measurable-field and diagonal-algebra chapters. They assume neither a topology nor a measure on the domain. The final two results supply finite-measure and Lebesgue approximation inputs for the finite-algebra and MASA examples.

<a id="oa-found-mt-01"></a>
## 1. Separable Hilbert space measurability

Let \((X,\Sigma)\) be a measurable space, let \(H\) be a separable complex Hilbert space, and let \(f:X\to H\). Inner products are linear in the first variable. The following conditions are equivalent:

1. \(x\mapsto\langle f(x),v\rangle\) is measurable for every \(v\in H\).
2. \(f\) is measurable for the norm-Borel sigma algebra of \(H\).
3. \(f\) is the pointwise norm limit of a sequence of measurable functions with finite range.

**Proof.** Choose a finite or countable orthonormal basis \((e_j)\) of \(H\), as provided by the Hilbert space basis theorem. If (1) holds, then, for every \(v\in H\), Parseval's identity gives
\[
\|f(x)-v\|^2=\sum_j|\langle f(x),e_j\rangle-\langle v,e_j\rangle|^2.
\]
The finite partial sums are measurable and their increasing limit is measurable. Hence the inverse image of every norm ball is measurable. A separable metric space has a countable base of balls, with centres in a countable dense set and positive rational radii. Each open set is the union of a subfamily of that countable base. Its inverse image is therefore measurable, proving (2).

For (2) implies (3), choose a norm-dense sequence \((v_j)_{j\ge1}\) in \(H\). For each \(n\), define \(j_n(x)\) to be the least index in \(\{1,\ldots,n\}\) that minimizes \(\|f(x)-v_j\|\), and set \(f_n(x)=v_{j_n(x)}\). The distances are measurable, and each event \(j_n(x)=j\) is a finite intersection of strict or weak comparisons between these measurable real functions. Thus \(f_n\) is measurable and has finite range. Moreover,
\[
\|f(x)-f_n(x)\|=\min_{1\le j\le n}\|f(x)-v_j\|\longrightarrow0
\]
by density. Finally, (3) implies (1), since scalar products of the finite-range functions are measurable and converge pointwise to \(\langle f(x),v\rangle\). The zero Hilbert space causes no exception. \(\square\)

**Consequence.** For a measure space, the corresponding almost-everywhere assertion follows by applying the theorem on the common conull set where the representatives are defined. If the measure space is complete, extension by zero across a null set preserves measurability. No such extension is needed when the map is defined everywhere as in the theorem.

The basis theorem and Parseval identity are proved in [Hilbert spaces and compact operators](../../foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html). The proof above contains the measurability argument rather than assuming a Pettis theorem.

<a id="oa-found-mt-02"></a>
## 2. The monotone class theorem for sets

An algebra of subsets of \(X\) contains \(X\) and is closed under complements and finite unions. A monotone class is closed under countable increasing unions and countable decreasing intersections. If \(\mathcal A\) is an algebra, the smallest monotone class \(\mathcal C\) containing \(\mathcal A\) is \(\sigma(\mathcal A)\).

**Proof.** The sigma algebra \(\sigma(\mathcal A)\) is a monotone class, so \(\mathcal C\subseteq\sigma(\mathcal A)\). The class
\[
\mathcal D=\{B\subseteq X:B^c\in\mathcal C\}
\]
is a monotone class: complementation interchanges increasing unions and decreasing intersections. It contains \(\mathcal A\), so minimality gives \(\mathcal C\subseteq\mathcal D\). Thus \(\mathcal C\) is closed under complements.

Fix \(A\in\mathcal A\). The class \(\{B\subseteq X:A\cap B\in\mathcal C\}\) is a monotone class and contains \(\mathcal A\), since the algebra is closed under finite intersections. It consequently contains \(\mathcal C\). Now fix \(B\in\mathcal C\). The class \(\{A\subseteq X:A\cap B\in\mathcal C\}\) is again a monotone class; the preceding conclusion says that it contains \(\mathcal A\), so it contains \(\mathcal C\). Therefore \(\mathcal C\) is closed under finite intersections, hence under finite unions by complements. For any sequence \((B_n)\) in \(\mathcal C\), the finite unions \(\bigcup_{n\le k}B_n\) increase to \(\bigcup_nB_n\), which is in \(\mathcal C\). Hence \(\mathcal C\) is a sigma algebra containing \(\mathcal A\), and \(\sigma(\mathcal A)\subseteq\mathcal C\). \(\square\)

In particular, if a class of measurable sets is monotone and contains an algebra generating the domain sigma algebra, it contains every measurable set. This is the exact set-class argument used to extend commutation from generating indicator multipliers to all indicator multipliers.

<a id="oa-found-mt-03"></a>
## 3. Uniform convergence outside a small set

Let \((X,\Sigma,\mu)\) have finite measure. If measurable complex functions \(f_n\) converge to a measurable function \(f\) almost everywhere, then for every \(\varepsilon>0\) there is a measurable \(E\subseteq X\) with \(\mu(X\setminus E)<\varepsilon\) such that \(f_n\to f\) uniformly on \(E\).

**Proof.** Let \(N\) be a measurable null set outside which convergence holds, and define
\[
B_{k,n}=\bigcup_{m\ge n}\{x:|f_m(x)-f(x)|>1/k\}\quad(k,n\ge1).
\]
For each \(k\), these sets decrease with \(n\), and their intersection is contained in \(N\). Continuity of a finite measure from above gives \(\mu(B_{k,n})\to0\). Choose \(n_k\) with \(\mu(B_{k,n_k})<\varepsilon2^{-k}\), and put
\[
E=X\setminus\left(N\cup\bigcup_{k\ge1}B_{k,n_k}\right).
\]
Countable subadditivity gives \(\mu(X\setminus E)<\varepsilon\). On \(E\), for every \(k\) and every \(m\ge n_k\), \(|f_m-f|\le1/k\). This is uniform convergence. Continuity from above itself follows from countable additivity by applying continuity from below to complements in the finite-measure set \(X\). \(\square\)

If \(X\) is compact Hausdorff and \(\mu\) is a finite Radon measure, inner regularity gives a compact \(F\subseteq E\) with \(\mu(E\setminus F)<\varepsilon/2\), after using \(\varepsilon/2\) in the theorem. Thus \(\mu(F)>\mu(X)-\varepsilon\) and convergence is uniform on \(F\). This is the precise Egoroff-and-compact-cutoff input in the finite type-II representation proof. Radon regularity, including regularity on finite-measure Borel sets, is proved in Theorem 2.2 and Proposition 2.3 of [Haar measure on locally compact groups](../../harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups.html).

<a id="oa-found-mt-04"></a>
## 4. Interval and arc step functions

Finite linear combinations of bounded interval indicators are dense in \(L^1(\mathbb R)\) for Lebesgue measure. Finite linear combinations of arc indicators are dense in \(L^1(\mathbb T)\) for normalized Lebesgue measure.

**Proof.** Proposition 3.1(4) of [Haar measure on locally compact groups](../../harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups.html) proves that compactly supported continuous functions are dense in \(L^1\) of a Radon measure. Lebesgue measure is Radon: the interval-cover construction gives open outer approximations with arbitrarily small excess measure, and, for a finite-measure set, first cutting off a small tail outside \([-R,R]\) and then taking the complement of an open outer approximation to its complement inside \([-R,R]\) gives a compact inner approximation. Open sets are countable disjoint unions of intervals, so their inner regularity also follows by retaining finitely many slightly shortened bounded intervals. The normalized circle measure is the image of Lebesgue measure on \([0,1]\); compact inner approximations pass to their compact images, and outer regularity follows by applying inner regularity to complements in this finite-measure compact space. For a compactly supported continuous \(g\) on \(\mathbb R\), choose a bounded interval \([-R,R]\) containing its support. On this interval \(g\) is uniformly continuous. Indeed, if uniform continuity failed, there would be pairs \(x_n,y_n\) whose distance tends to zero but whose value difference is bounded away from zero; a convergent subsequence of \(x_n\), and hence of \(y_n\) to the same limit, contradicts continuity. Partition \([-R,R]\) into intervals of sufficiently small length and give the step function on each interval the value of \(g\) at one endpoint. The uniform approximation error on \([-R,R]\) tends to zero, and both functions vanish outside it. Their \(L^1\) distance is at most \(2R\) times that error. Endpoint values affect no integral. This proves the first density assertion. For the circle, apply the same argument to the continuous periodic representative on \([0,1]\); the partition intervals become arcs, and the \(L^1\) error is at most the uniform error. Density of continuous functions proves the second assertion. \(\square\)

For a translated interval indicator, the \(L^1\) difference is the measure of its symmetric difference and is at most twice the translation distance; the same bound holds for arc indicators and sufficiently small circle distance. The density just proved and the fact that translation is an \(L^1\) isometry then prove continuity of translation on every \(L^1\) function. Reflection, translation and nonzero scalar dilation preserve or scale Lebesgue measure by the interval-cover construction. In the rational-translation proof, the two-variable map \((t,x)\mapsto(x-t,x)\) preserves product Lebesgue measure: Tonelli integrates first in \(t\), and reflection followed by translation changes that inner integral to integration in \(y=x-t\). The same argument applies to normalized circle measure. The exact Tonelli and Fubini theorems, including their sigma-finite support condition, are proved in Sections 4 and 5 of the linked Haar-measure chapter; the real line and circle meet that condition.
