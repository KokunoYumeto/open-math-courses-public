# Closed graphs and complete smooth quotients

This is a modified selection from *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Original principal author: AN-03 course-writing task; original publisher: AN-03 local course project. Copyright © 2026 AN-03 course project contributors. The renewed edition is by the AN-03 course-writing task and OpenAI Codex. Current selection, exact prerequisite connections and explicitly identified additions: GPT-6 Astra (OpenAI), Ultra, 5 October 2026 UTC; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under the GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The [complete licence](notices/COPYING), [title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and rights notice accompany it. Its combined text retains that licence.

## F0. Exact earlier proofs and retained scope

The complete open-mapping and closed-graph proofs BF10–BF13 and the seminorm-extension and quotient proofs FQ1–FQ10 below are retained from AN03-P004, *Banach estimates, quotient spaces and compact parameter arguments*. The unrelated subsequent editorial improvements are not needed here.

The retained Section 14.1 and its product/subspace facts mean the complete [seminorm metric proof in the earlier test-space companion](../20261004-free-tangent-zoom/prerequisites/complete-test-spaces.md). Its Section 14.2 proves smooth-space completeness and its Sections 6 and 19 prove the complete-metric Baire theorem with the declared choice input. Section 5 means the complete [real and complex Hahn–Banach proof](../20261005-cauchy-foundations/integration-and-duality.md), preserving extension from an arbitrary normed subspace. Thus all inputs to the following proofs are already present in the programme. The [exact proof map](proof-map.json) records their current versions.

In the compact-solvability receiver, BF10 is used for the closed-graph theorem. Its smooth range argument supplies its own closure neighborhoods before using the correction series BF11–BF12. It therefore does not presume surjectivity in order to prove surjectivity. FQ4–FQ10 retain the actual increasing quotient seminorms, not a replacement Banach norm.

### 14.4. Open mapping with every seminorm retained

Let \(T:E\to F\) be a continuous surjective linear map between Fréchet spaces, with original seminorms \(p_i\) on \(E\) and \(q_i\) on \(F\). First let \(V\) be any balanced convex open neighborhood of zero in \(E\). It contains a finite-seminorm neighborhood and therefore absorbs every vector: all conditions of that smaller neighborhood can be met by dividing by a sufficiently large positive integer. Thus \(F=\bigcup_{m\geq1}T(mV)\), and the closed sets \(\overline{T(mV)}\) cover \(F\). Baire shows that one has interior. Scalar multiplication by a nonzero integer is a homeomorphism by (BF1), so \(\overline{T(V)}\) has interior. Choose \(y_0\) and an open neighborhood \(W\) of zero with \(y_0+W\subset\overline{T(V)}\). In particular \(y_0\in\overline{T(V)}\). Approximating each of \(y_0+w\) and \(y_0\) by points of \(T(V)\) shows
\[
 W\subset\overline{T(V)-T(V)}
       \subset\overline{T(2V)},
 \qquad \tfrac12W\subset\overline{T(V)}.
 \tag{BF10}
\]
Here \(V-V\subset2V\) follows from balance and convexity, and the approximations can be taken in arbitrarily small metric neighborhoods. Thus the closure of the image of every such \(V\) contains a neighborhood of zero.

We now remove the closure while controlling all seminorms. Given an open neighborhood \(U\) of zero in \(E\), choose a finite list of original constraints \(p_i(x)<a_i\), \(i\in J\), whose intersection lies in \(U\). For \(j\geq1\) take the balanced convex open neighborhood
\[
 V_j=\{v:p_i(v)<a_i2^{-j-1}\ (i\in J),
                 \ p_i(v)<2^{-j}\ (1\leq i\leq j)\}.
 \tag{BF11}
\]
By (BF10), choose a balanced open neighborhood \(W_j\) of zero contained in \(\overline{T(V_j)}\), and shrink it also to satisfy \(q_i(w)<2^{-j}\) for \(1\leq i\leq j\). Let \(y\in W_1\) and \(r_0=y\). Since \(r_{j-1}\in W_j\subset\overline{T(V_j)}\), select \(v_j\in V_j\) with \(r_j=r_{j-1}-Tv_j\in W_{j+1}\). This is possible because \(r_{j-1}-W_{j+1}\) is an open neighborhood of \(r_{j-1}\). For every fixed \(i\), the tails of \(\sum_jv_j\) are Cauchy in \(p_i\): after \(j\geq i\), their seminorms are bounded by the tails of \(\sum_j2^{-j}\). Completeness gives an actual sum \(v\in E\). For \(i\in J\), continuity of \(p_i\) and the retained bounds give
\[
 p_i(v)\leq\sum_{j\geq1}p_i(v_j)
          \leq a_i\sum_{j\geq1}2^{-j-1}
          =a_i/2<a_i,
 \qquad
 y-T\sum_{j=1}^Nv_j=r_N\longrightarrow0
                      \text{ in every }q_i.
 \tag{BF12}
\]
Thus \(v\in U\) and continuity gives \(Tv=y\). Hence \(W_1\subset T(U)\). Translating this conclusion proves that \(T\) is open on every open subset of \(E\). A continuous bijective linear map between Fréchet spaces consequently has a continuous inverse. The proof requires no countability of a basis of vectors and no normability; the countable seminorms and completeness are used exactly in the correction series. It makes no assertion about a linear right inverse for a noninjective map.

### 14.5. The closed graph and its exact estimate

Let \(L:E\to F\) be an everywhere-defined linear map between Fréchet spaces, and suppose its graph \(G=\{(x,Lx):x\in E\}\) is closed in \(E\times F\). By Section 14.1 the product is Fréchet and its closed subspace \(G\) is Fréchet. Projection \(\pi_E:G\to E\) is continuous, linear and bijective. Section 14.4 makes its inverse continuous. Projection \(\pi_F:G\to F\) is continuous, so \(L=\pi_F\pi_E^{-1}\) is continuous. This proves the closed graph theorem for both Fréchet spaces and in particular for a Banach domain.

If \(E\) is Banach, each target seminorm has an explicit form of bound: continuity gives \(r_i>0\) such that \(q_i(Lx)<1\) whenever \(\|x\|<r_i\). For nonzero \(x\) apply that bound to \(r_i x/(2\|x\|)\); for zero use linearity. Thus
\[
 q_i(Lx)\leq(2/r_i)\|x\|\quad(x\in E).
 \tag{BF13}
\]
There is a possibly different \(r_i\) for every target seminorm. A bounded operator into one chosen smooth norm alone does not replace these bounds for all derivative orders.

### 14.7. Extending a functional with its original seminorm bound

The totally characteristic calculus uses two functional-analytic bridges: extension of a functional dominated by an actual seminorm, and completeness of a quotient by a closed subspace of a Fréchet space. Section5 already proves norm-preserving real and complex Hahn–Banach, while Section14.1 constructs the complete metric from the given seminorms. The following arguments supply their full required versions without an external proof.

First let \(p\) be the given seminorm on a complex vector space \(X\), \(M\subset X\) a linear subspace, and \(f:M\to\mathbb C\) complex-linear with \(|f(x)|\leq p(x)\) on \(M\). Keep the actual null space and quotient map
\[
K=\{x\in X:p(x)=0\},\qquad \pi:X\longrightarrow X/K.
\tag{FQ1}
\]
The triangle inequality and absolute homogeneity make \(K\) a complex subspace. If \(k\in K\), both inequalities \(p(x+k)\leq p(x)+p(k)\) and \(p(x)\leq p(x+k)+p(-k)\) prove \(p(x+k)=p(x)\). Therefore
\[
\|\pi x\|_p=p(x)
\tag{FQ2}
\]
is a well-defined norm on the actual quotient, with no completeness assumption. Since \(f\) vanishes on \(M\cap K\), the rule \(f_0(\pi m)=f(m)\) is well-defined on \(\pi M\), complex-linear and bounded by this norm. Section5 extends it to a complex-linear \(F_0:X/K\to\mathbb C\) with norm at most one. Then
\[
\Lambda=F_0\pi,\qquad
\Lambda|_M=f,\qquad |\Lambda(x)|\leq \|\pi x\|_p=p(x)
\quad(x\in X).
\tag{FQ3}
\]
This is the full original seminorm bound, retaining its exact constant one and its original null directions. If \(p=0\), both \(f\) and its zero extension vanish; the same zero-dimensional quotient construction applies. If \(M=0\) or \(M=X\), the construction still gives the stated extension.



### 14.8. Complete quotients with every original seminorm

Now let \(E\) be a real or complex Fréchet space with the original countable separating seminorms \(p_j\), \(j\geq1\), and actual complete translation-invariant metric
\[
d_E(x,y)=\sum_{j=1}^\infty 2^{-j}\min\{1,p_j(x-y)\}.
\tag{FQ4}
\]
Let \(N\subset E\) be a closed linear subspace and \(q:E\to E/N\) the original quotient map. Put
\[
P_j(x)=\max_{1\leq i\leq j}p_i(x),\qquad
\bar P_j(qx)=\inf_{n\in N}P_j(x+n),\qquad
d_N(qx,qy)=\inf_{n\in N}d_E(x-y+n,0).
\tag{FQ5}
\]
Each infimum is over a nonempty set and is finite, since \(n=0\) is allowed. A change of representative translates \(N\) bijectively, so both quantities are well-defined. The full family \(p_i\) remains visible in \(P_j\); it has not been replaced by one norm.

Each \(\bar P_j\) is a seminorm. Absolute homogeneity for a nonzero scalar follows from the bijection \(n\mapsto an\) of \(N\); at scalar zero the value is zero. For the triangle inequality choose \(n_1,n_2\) within an arbitrary \(\varepsilon>0\) of the two infima, use \(n_1+n_2\in N\) and the triangle inequality for \(P_j\), then let \(\varepsilon\) decrease to zero. The same proof with the translation-invariant metric \(d_E\) gives symmetry and the triangle inequality for \(d_N\). If \(d_N(qx,qy)=0\), there are \(n_r\in N\) with \(x-y+n_r\to0\) in \(E\). Thus \(n_r\to y-x\), and closedness gives \(y-x\in N\). Hence \(qx=qy\), proving that \(d_N\) is a metric.

The exact balls satisfy, for each \(\varepsilon>0\),
\[
B_{d_N}(qx,\varepsilon)=q(B_{d_E}(x,\varepsilon)),\qquad
\{z:\bar P_j(z)<\varepsilon\}
=q(\{x:P_j(x)<\varepsilon\}).
\tag{FQ6}
\]
The forward directions choose an element within the strict infimum bound; the reverse directions use that same representative in the infimum. Images of open sets are open in the quotient topology: \(q^{-1}q(U)=U+N=\bigcup_{n\in N}(U+n)\) is open. Thus FQ6 proves that \(d_N\) gives exactly the quotient topology. The increasing \(P_j\) also give the original topology of \(E\): every finite intersection of original seminorm balls contains a \(P_j\)-ball with the minimum of its finitely many tolerances, while a \(P_j\)-ball is their finite intersection with a common tolerance. FQ6 consequently proves that the increasing \(\bar P_j\) give the same quotient topology. They separate points, since if all vanish, the coset has a representative arbitrarily close to zero in every basic original neighborhood and hence lies in the metric closure of the zero coset; the quotient metric is Hausdorff.

We prove completeness of the actual \(d_N\), rather than assume that a quotient of a complete metric is automatically complete. Let \((z_r)\) be \(d_N\)-Cauchy. Choose increasing indices \(r_j\) so that
\[
d_N(z_r,z_s)<2^{-j-2}\qquad(r,s\geq r_j).
\tag{FQ7}
\]
Choose a representative \(x_1\) of \(z_{r_1}\). Given \(x_j\), choose any representative \(y\) of \(z_{r_{j+1}}\). FQ5 and FQ7 give \(n\in N\) such that
\[
x_{j+1}=y+n,\qquad qx_{j+1}=z_{r_{j+1}},\qquad
d_E(x_{j+1},x_j)<2^{-j-1}.
\tag{FQ8}
\]
The latter bound is larger than the infimum by a positive margin, so such a choice is possible. For every \(k>j\) the triangle inequality retains all increments:
\[
d_E(x_k,x_j)\leq
\sum_{\nu=j}^{k-1}d_E(x_{\nu+1},x_\nu)
<\sum_{\nu=j}^{k-1}2^{-\nu-1}<2^{-j}.
\tag{FQ9}
\]
Thus the representatives form an \(E\)-Cauchy sequence. Its original completeness gives \(x_j\to x\in E\). Since \(d_N(qx_j,qx)\leq d_E(x_j,x)\), the subsequence \(z_{r_j}\) converges to \(qx\). The Cauchy condition and the triangle inequality then give convergence of the full original sequence: given \(\varepsilon>0\), choose a tail on which its mutual distances are less than \(\varepsilon/2\), and a subsequence member there with distance to \(qx\) less than \(\varepsilon/2\).

The quotient seminorm metric required by the definition of a Fréchet space is
\[
d_Q(z,w)=\sum_{j=1}^\infty2^{-j}
                    \min\{1,\bar P_j(z-w)\}.
\tag{FQ10}
\]
Section14.1 proves that it gives the topology of the separating countable seminorm family. It is complete as well. Indeed FQ6 shows that \(d_Q\) and \(d_N\) have exactly the same neighborhoods at zero. Both are translation-invariant, so for each radius in either metric there is a zero-centered ball of the other metric inside it. Applying that containment to every difference \(z_r-z_s\) transfers the Cauchy condition in both directions; applying it to \(z_r-z\) transfers convergence. The completeness just proved for \(d_N\) therefore proves completeness for \(d_Q\).

The quotient is locally convex, Hausdorff, metrizable and complete with exactly its original quotient topology, so \(E/N\) is Fréchet. The map \(q\) is linear, continuous and open, and its kernel is precisely \(N\). All quotient seminorms, representatives and completion increments have been supplied explicitly. This includes \(N=0\), \(N=E\) and the zero space. The closedness of \(N\) is used exactly at the metric's nondegeneracy step; no assertion about a nonclosed quotient is inferred.
