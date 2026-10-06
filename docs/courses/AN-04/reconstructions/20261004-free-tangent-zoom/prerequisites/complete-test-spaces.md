# Complete fixed-support test spaces

This separate GFDL 1.2 component retains the full used arguments from AN03-P004,
*Banach estimates, quotient spaces and compact parameter arguments*, as selected
in the earlier AN-01 programme. Original numbering and mathematical text are
unchanged. The omitted Hahn–Banach and general smooth-space paragraphs are not
used by the tangent lesson.

Its scalar, finite-dimensional and compact calculus inputs are the already
proved stationary prerequisite chain.
The [notation and foundational axioms](../../20261004-free-stationary-phase/provider-context.md)
are retained; Section 19 below additionally declares Zorn's principle and proves
the choice consequence used in the Baire recursion. No norm-extension theorem
is needed here.

Original principal author and publisher: AN-03 course-writing task / AN-03 local
course project. Copyright © 2026 AN-03 course project contributors. Earlier
modification: AN-03 course-writing task and OpenAI Codex. AN-01 selection and
this narrower AN-04 selection: GPT-6 Astra (OpenAI), Ultra, 4 October 2026.
Permission is granted under the GNU Free Documentation License, Version 1.2
only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.
The full [licence](notices/COPYING) and [version history](notices/HISTORY.md)
accompany this component. It is not relicensed under the receiving lesson's
separate terms.

## 6. Baire's theorem for complete metric spaces

**Complete-metric Baire theorem.** Every countable intersection of dense open subsets of a complete metric space is dense. Here is its full nested-ball proof. Let \(Z\) be complete, let \(U_j\subset Z\), \(j\geq1\), be dense and open, and let \(V\subset Z\) be nonempty and open. Since \(U_1\) is dense, \(V\cap U_1\) contains a point \(z_1\). Openness supplies \(r_1>0\), chosen also with \(r_1\leq2^{-1}\), such that
\[
 \overline B(z_1,r_1)\subset V\cap U_1.
 \tag{B12}
\]
Indeed choose a ball contained in the open set and take a smaller radius, so its closed ball is contained in that original ball. Suppose \(z_j,r_j>0\) have been chosen. The nonempty open ball \(B(z_j,r_j)\) meets dense \(U_{j+1}\). Choose \(z_{j+1}\) in that intersection and a positive radius \(r_{j+1}\leq2^{-j-1}\) whose closed ball lies in the intersection. Thus
\[
 \overline B(z_{j+1},r_{j+1})
       \subset B(z_j,r_j)\cap U_{j+1},\qquad
 0<r_j\leq2^{-j}.
 \tag{B13}
\]
The construction works also at isolated points: a sufficiently small ball then consists of that point. For \(k,l\geq j\), both centers lie in \(\overline B(z_j,r_j)\), so \(d(z_k,z_l)\leq2r_j\to0\). Completeness gives a limit \(z\). For each \(j\), the entire tail lies in that closed ball; continuity of distance gives \(z\in\overline B(z_j,r_j)\). The first inclusion puts \(z\) in \(V\), and each successive inclusion puts it in \(U_j\). Hence \(V\cap\bigcap_jU_j\ne\varnothing\). This proves density. If \(Z\) is empty, the assertion is true by the definition of density, and no ball is chosen. Neither separability nor local compactness is required. The complete proof above supplies the Baire input; Garrett's freely accessible Theorem 4.0.1 provides a comparison.

The form needed below follows exactly. If a nonempty complete metric space is the union of closed sets \(F_n\), then some \(F_n\) has nonempty interior. If every interior were empty, each open complement would be dense, while their intersection would be empty, contradicting the theorem just proved. Completeness will be checked for each space to which this form is applied.

### 14.1. The original seminorms and a complete metric

Let \(E\) be a real or complex vector space with a countable family of seminorms \(p_j\), \(j\geq1\), separating points: \(p_j(x)=0\) for every \(j\) implies \(x=0\). A seminorm has the triangle inequality and \(p_j(ax)=|a|p_j(x)\). Give \(E\) the topology whose neighborhoods of zero are finite intersections of sets \(p_j(x)<a_j\), with all \(a_j>0\). Translates are neighborhoods at other points. The separating property makes this topology Hausdorff: if \(p_j(x-y)>0\), disjoint sufficiently small translates of a \(p_j\)-ball separate \(x,y\). Each seminorm is continuous, since \(|p_j(x)-p_j(y)|\leq p_j(x-y)\). Addition is continuous by the triangle inequalities. Scalar multiplication is continuous by
\[
 p_j(ax-a_0x_0)
 \leq |a|p_j(x-x_0)+|a-a_0|p_j(x_0).
 \tag{BF1}
\]
The original family is retained in every estimate. The following auxiliary metric measures the same topology:
\[
 d_E(x,y)=\sum_{j=1}^{\infty}2^{-j}
                  \min\{1,p_j(x-y)\}.
 \tag{BF2}
\]
The series converges, is symmetric, vanishes exactly at equality, and satisfies the triangle inequality because \(\min(1,a+b)\leq\min(1,a)+\min(1,b)\) for \(a,b\geq0\). Given finitely many seminorm tolerances, choose \(0<\delta<\min_j 2^{-j}\min(1,a_j)\) over their indices. Then \(d_E(x,y)<\delta\) implies every requested \(p_j(x-y)<a_j\). Conversely, given a metric tolerance \(\varepsilon>0\), take \(J\) with \(\sum_{j>J}2^{-j}<\varepsilon/2\), and require \(p_j(x-y)<\varepsilon/2\) for \(1\leq j\leq J\). Their weighted contributions sum to less than \(\varepsilon/2\); with the tail this gives \(d_E(x,y)<\varepsilon\). Thus the two topologies agree. The same two arguments show that a sequence is metric Cauchy exactly when it is Cauchy for each original seminorm, and converges in this metric exactly when it converges for every seminorm.

A Fréchet space here means such a space complete for (BF2). The definition is unchanged if another countable separating family gives the same topology: the identity in both directions is linear and continuous, so each target seminorm is bounded by a constant times a finite maximum of source seminorms. To prove that bound, continuity gives a finite intersection on which the target seminorm is less than one; rescale a vector into half that intersection, and use arbitrary rescaling when its finite maximum is zero. The bound transfers Cauchy sequences and convergence in both directions. This proves the completeness comparison instead of replacing the original family. A Banach space is a Fréchet space by taking \(p_j(x)=\|x\|\) for every \(j\).

Finite products of Fréchet spaces are Fréchet: use all the coordinate seminorms and interleave their countable lists. A sequence Cauchy in each product seminorm is Cauchy in each factor, and its factor limits give a product limit. A closed subspace is Fréchet with the restricted seminorms, since an ambient limit remains in the closed subspace. These conclusions include zero spaces. Section 6 therefore applies to these spaces with their actual complete metrics.

### 14.2. Completeness of the smooth spaces

Let \(\Omega\subset\mathbb R^n\) be open and let \(K\subset\Omega\) be compact. Define
\[
 \mathcal D_K(\Omega)
   =\{f\in C^\infty(\Omega):\operatorname{supp}f\subset K\},
 \qquad
 p_N(f)=\max_{|\alpha|\leq N}\sup_{x\in\Omega}
                                      |\partial^\alpha f(x)|,
 \quad N=0,1,2,\ldots .
 \tag{BF3}
\]
These are finite seminorms, in fact norms on this vector space, and \(p_0\) separates points. A function supported in \(K\) extends by zero to a smooth function on \(\mathbb R^n\): near every point outside \(K\) the extension is zero, and near a point of \(K\) it agrees with its smooth expression inside \(\Omega\). Its derivatives also vanish outside \(K\). No regularity of the boundary of \(K\) is required.

If \(f_l\) is Cauchy for every \(p_N\), each \(\partial^\alpha f_l\) converges uniformly on \(\mathbb R^n\) to a continuous function \(g_\alpha\). Scalar completeness gives the pointwise limit; the uniform Cauchy estimate gives uniform convergence, and the usual three-term estimate proves continuity of the limit. Each \(g_\alpha\) vanishes off \(K\). On a coordinate segment the scalar fundamental theorem gives, for every \(l\),
\[
 \partial^\alpha f_l(x+h e_i)-\partial^\alpha f_l(x)
   =\int_0^h\partial^{\alpha+e_i}f_l(x+t e_i)\,dt.
 \tag{BF4}
\]
Uniform convergence passes through this integral, with error at most \(|h|\sup|\partial^{\alpha+e_i}f_l-g_{\alpha+e_i}|\). Hence (BF4) holds with the corresponding \(g\)'s. Dividing by \(h\) and using continuity shows \(\partial_i g_\alpha=g_{\alpha+e_i}\). Continuous coordinate partial derivatives give a full derivative: telescope the change along the finitely many coordinate segments and bound the differences of these continuous partial derivatives. Repeating this argument shows that \(g_0\) is smooth and \(\partial^\alpha g_0=g_\alpha\) for every \(\alpha\). It is supported in \(K\), and the original uniform estimates give \(p_N(f_l-g_0)\to0\). Thus \(\mathcal D_K(\Omega)\) is Fréchet for its exact smooth topology, including \(K=\varnothing\) and compact sets with empty interior.

## 19. The selected Zorn entry and the original Baire recursion

The course chooses Zorn's maximality principle as an explicit logical axiom. Here is the exact selection map needed in the original complete-metric Baire argument. For any set-indexed family of nonempty sets \((A_i)_{i\in I}\), consider partial functions \(c\) with domain a subset of \(I\) and \(c(i)\in A_i\), ordered by extension. The empty function belongs to the poset. Every chain has an upper bound: its union is a function, since any two partial functions in the chain agree wherever both are defined, and every union value remains in its specified \(A_i\). Zorn gives a maximal partial function. If its domain omits \(i\), choose one element of that nonempty \(A_i\); adjoining that one pair extends the function, a contradiction. Consequently
\[
 c:I\longrightarrow\bigcup_{i\in I}A_i,\qquad c(i)\in A_i
                     \text{ for every }i\in I.
 \tag{BZ1}
\]
This proves the required choice consequence from the chosen axiom, without adding an unannounced sequence-selection hypothesis.

For the original metric space \(Z\), form the set-indexed family of all nonempty subsets of \(Z\times(0,\infty)\), and fix its selector from (BZ1). For a nonempty open \(W\subset Z\) and an integer \(j\geq1\), the set
\[
 A(W,j)=\{(z,r):z\in W,\ 0<r\leq2^{-j},\
                   \overline B(z,r)\subset W\}
 \tag{BZ2}
\]
is nonempty. Indeed take one point of \(W\), a positive ball lying in \(W\), and a smaller positive radius, also at most \(2^{-j}\); its closed ball lies in the original open ball. This includes isolated points. Given dense open \(U_j\) and nonempty open \(V\), choose the first pair by applying that fixed selector to \(A(V\cap U_1,1)\). Having selected \((z_j,r_j)\), apply the same selector to
\(A(B(z_j,r_j)\cap U_{j+1},j+1)\).
The intersection is nonempty by density. Ordinary natural-number recursion now gives exactly the original nested balls and dyadic bounds \(B12\)--\(B13\); its next value is an actual function of the preceding pair and the original sets.

All later centers lie in \(\overline B(z_j,r_j)\), so their mutual distances are at most \(2r_j\leq2^{1-j}\). Completeness supplies a limit \(z\). Each closed ball contains the tail and is closed, hence contains \(z\); its original inclusion puts \(z\) in \(V\cap\bigcap_jU_j\). This proves density of that intersection with the original metric unchanged. If \(Z=\bigcup_jF_j\) is a countable closed cover and no \(F_j\) has interior, every \(Z\setminus F_j\) is dense open. For nonempty \(Z\), the result gives a point outside their union, a contradiction. The source Baire and closed-cover conclusions therefore have the complete stated proof at their selected logical base.

## Free comparisons

Paul Garrett, *Review of metric spaces*, 2 February 2014, Theorem 4.0.1,
[author PDF](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2012-13/01_metric_spaces.pdf),
supplies the complete-metric nested-ball comparison. Semyon Dyatlov,
*Lecture notes for 18.155*, Section 4.3,
[author PDF](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf),
supplies the distributional metric and uniform-bound comparison. All arguments
used from this component are written above; these citations replace none of them.
