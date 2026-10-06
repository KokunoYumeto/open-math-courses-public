# Functional extension and complete test spaces

*Selected from the earlier programme lesson **Banach estimates, quotient spaces and compact parameter arguments**, AN03-P004. The programme credits and CC0 1.0 dedication are retained in the accompanying notices. Selection by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026.*

These complete proof selections supply exactly the complex norm-preserving extension theorem, the Baire theorem and completeness of fixed-support smooth test spaces. Section numbers are retained. Here a norm is a positive definite, absolutely homogeneous function satisfying the triangle inequality; no completeness of a normed space is assumed unless stated. The scalar arithmetic, finite-dimensional norm rules, Euclidean compactness and fundamental theorem used in these proofs are proved in the accompanying [scalar calculus](metric-foundation-bridges.md) and [finite algebra](stable-prerequisite-bridges.md) selections.

Zorn's maximality principle is the selected set-theoretic axiom for arbitrary normed-space extension. The last selection makes its choice consequence and the countable Baire construction explicit. The proof uses no distributional convergence result that depends on this selection.

## 5. Hahn–Banach and scalar norm tests

Let \(M\subset X\) be a linear subspace of a real normed space and \(f:M\to\mathbb R\) bounded and linear, with \(C=\|f\|\). We first prove an extension by one vector. For \(v\notin M\), consider the real intervals with endpoints
\[
f(m)-C\|m-v\|,\qquad f(m)+C\|m-v\|\quad(m\in M).
\]
Every lower endpoint is at most every upper endpoint: for \(m,n\in M\),
\[
f(m)-f(n)\leq C\|m-n\|\leq C\|m-v\|+C\|n-v\|.
\]
The endpoints from \(m=0\) show that the lower endpoints are bounded above and the upper endpoints bounded below. Real completeness supplies a real \(c\) between their supremum and infimum. Consequently
\[
|c-f(m)|\leq C\|v-m\|\quad(m\in M).
\tag{B4}
\]
Define \(F(m+tv)=f(m)+tc\). The representation is unique because \(v\notin M\), so \(F\) is real-linear and extends \(f\). For \(t\ne0\), apply (B4) to \(-m/t\) and multiply by \(|t|\); it gives \(|F(m+tv)|\leq C\|m+tv\|\). For \(t=0\) use the original bound. Restriction supplies the reverse inequality for the norms, so \(\|F\|=C\). This also handles \(C=0\).

For extension to all of \(X\), order the pairs consisting of a subspace containing \(M\) and an extension of \(f\) bounded by \(C\), by extension. The original pair makes this a nonempty partially ordered set. For a nonempty chain, the union of its subspaces is a subspace: any finite list of vectors belongs to one member of the chain. The functionals agree on overlaps, giving a well-defined linear functional on that union with the same bound. This is an upper bound; the original pair bounds an empty chain. Zorn's explicitly assumed maximality principle gives a maximal pair. The one-vector construction shows that its domain cannot omit any vector of \(X\). Thus the real extension exists on all of \(X\), with norm \(C\).

Now let \(X\) and \(M\) be complex and \(f:M\to\mathbb C\) bounded and complex-linear. Its real part \(h=\operatorname{Re}f\) is a real-linear functional on the underlying real subspace. Its real operator norm equals \(\|f\|\): one inequality is \(|h(m)|\leq|f(m)|\); for the other, when \(f(m)\ne0\), multiply \(m\) by \(\theta=\overline{f(m)}/|f(m)|\), so \(h(\theta m)=|f(m)|\) and \(\|\theta m\|=\|m\|\). Extend \(h\) by the real result to \(a:X\to\mathbb R\), with norm \(\|f\|\), and put
\[
F(x)=a(x)-i\,a(ix).
\tag{B5}
\]
Real-linearity gives additivity and \(F(ix)=iF(x)\); together these prove complex-linearity. On \(M\), \(\operatorname{Re}f(im)=-\operatorname{Im}f(m)\), so \(F(m)=f(m)\). For any \(x\) with \(F(x)\ne0\), choose a unit scalar \(\theta\) making \(\theta F(x)=|F(x)|\). Complex-linearity gives
\[
|F(x)|=\operatorname{Re}F(\theta x)=a(\theta x)
\leq\|a\|\|x\|.
\]
The zero value is harmless. Thus \(\|F\|\leq\|a\|=\|f\|\), while restriction proves equality. Neither the closedness of \(M\) nor the completeness of \(X\) was required.

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

The space \(C^\infty(\Omega)\) is also Fréchet. For nonempty \(\Omega\), choose
\[
 K_j=\{x\in\Omega:|x|\leq j,
          \operatorname{dist}(x,\mathbb R^n\setminus\Omega)\geq1/j\},
 \qquad
 q_j(f)=\max_{|\alpha|\leq j}\sup_{x\in K_j}
                                           |\partial^\alpha f(x)|,
 \quad j\geq1.
 \tag{BF5}
\]
When \(\Omega=\mathbb R^n\), omit the distance condition; a supremum over an empty \(K_j\) is defined as zero. Each \(K_j\) is compact, \(K_j\subset\operatorname{int}K_{j+1}\), and the interiors cover \(\Omega\). Every compact subset of \(\Omega\) lies in some such interior: its coordinate norm has a finite maximum and its distance to the closed complement has a positive minimum. Consequently the \(q_j\)'s separate points and give exactly uniform convergence of every derivative on each compact subset. A Cauchy sequence has continuous derivative limits on each \(K_j\); the limits agree on overlaps. Apply (BF4) on sufficiently small coordinate segments in an interior \(K_j\) to prove that the common limit is smooth. The original \(q_j\)-estimates give convergence for every \(j\), proving completeness. For empty \(\Omega\), the space consists of the single zero function and is complete. Finite-component smooth sections in a fixed chart use finite products; the same proof covers their topology.

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

## Source and licence

The selections above retain their original mathematical text and numbering. Original licence and attribution: [RIGHTS](notices/RIGHTS.md), [title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md), and [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). This selection is licensed under CC0 1.0, with no Invariant Sections, Front-Cover Texts or Back-Cover Texts. Its [selection history](notices/U008_SELECTION_HISTORY.md) records the changes and retained source credit.

Free human sources for the compared arguments are Paul Garrett's [*Banach Spaces*](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2016-17/02_banach.pdf), Section 9, and [*Review of metric spaces*](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2012-13/01_metric_spaces.pdf), Theorem 4.0.1. Their external citations do not replace any of the included proofs.
