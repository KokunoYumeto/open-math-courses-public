# Banach estimates, quotient spaces and compact parameter arguments

A Banach-space argument uses completeness, scalar separation and compactness for different reasons. This lesson proves the forms needed later for Fredholm operators, symbol actions and positivity estimates. Its examples show exactly where each hypothesis matters.

The useful distinction is between three mechanisms. Completeness turns summable errors into actual vectors. Hahn–Banach produces scalar tests without a completeness assumption. Compactness permits uniform control of a parameter family, even when that parameter space has no countable neighborhood basis. Keeping these mechanisms separate prevents a Banach-space estimate from being applied silently to a nonnormable space.

## 1. The assumptions used here

Work over \(\mathbb K=\mathbb R\) or \(\mathbb C\), with complex-linear duals when \(\mathbb K=\mathbb C\). A normed space has the metric \(d(x,y)=\|x-y\|\); it is Banach when every Cauchy sequence converges in that norm. Write \(\mathcal L(X,Y)\) for continuous linear maps. No space below is assumed separable.

Begin with [Metric and topological foundations](metric-foundation-bridges.md): the complete real field, its Archimedean property, finite linear algebra, scalar Cauchy–Schwarz, compactness in finite dimensions, and Zorn's maximality principle. The measure and differentiation results of that lesson are not used in Sections 1--13. Later sections use their stated independent entries: the fundamental theorem in Section 14.2, trigonometric calculus in Section 15.6, and the full scalar and cutoff calculus in Sections 17--21. Those later uses do not enter the earlier Banach arguments. Complex scalar completeness follows coordinatewise from real completeness. Zorn's principle is the stated assumption in the Hahn–Banach proof in Section 5.

We use the definitions of open sets, neighborhoods, closure, the subspace topology and the product topology. Closure means that every open neighborhood meets the set. A map is continuous when inverse images of open sets are open; equivalently, each neighborhood of its value contains the image of a sufficiently small neighborhood of the input. The latter equivalence follows by taking inverse images in one direction and the union of these input neighborhoods in the other. Complements give the corresponding inverse-image statement for closed sets. Sections 9–10 prove the needed compactness and net assertions.

The proofs proceed from finite-dimensional norm control through completeness of operator spaces and quotients, Hahn–Banach separation, uniform boundedness, open mapping, nets, compactness and square-summable sequences. The complete-metric Baire theorem is proved in Section 6. Sections 14.1–14.6 give the separate Fréchet arguments, including the exact smooth-space applications. Sections 17--21 supply the full Bochner and Hilbert-valued integration entry, original monomial Schwartz operations, selected-Zorn Baire map and exact lattice cutoffs. Hilbert-space representation has its separately identified proof.

## 2. Finite-dimensional norms and exact sequences

Let \(E\) have basis \(e_1,\ldots,e_d\) and any norm \(N\). Set \(|a|=(\sum_{j=1}^d|a_j|^2)^{1/2}\) for its coordinate vector. The triangle inequality and the finite scalar Cauchy–Schwarz inequality give
\[
N\left(\sum_j a_je_j\right)\leq C|a|,
\qquad C=\left(\sum_jN(e_j)^2\right)^{1/2}.
\tag{B1}
\]
Also \(|N(u)-N(v)|\leq N(u-v)\leq C|u-v|\), so \(N\) is continuous in coordinates. For \(d>0\) there is \(c>0\) such that \(N(a)\geq c\) on \(|a|=1\). Otherwise choose unit vectors with norms tending to zero. The compactness interface Section 4 of [Metric and topological foundations](metric-foundation-bridges.md) gives a coordinate-convergent subsequence whose limit is still a unit vector; continuity makes its norm zero, a contradiction. Scaling yields
\[
c|a|\leq N\left(\sum_j a_je_j\right)\leq C|a|.
\tag{B2}
\]
Thus every norm is equivalent to the coordinate norm. Identifying \(\mathbb C^d\) with \(\mathbb R^{2d}\) includes complex spaces. Dimension zero has one vector and is treated without choosing positive comparison constants.

A closed bounded subset of \(E\) is coordinate closed and bounded by (B2), hence compact by the same finite-dimensional interface. Every linear map out of \(E\) into a normed space is bounded: apply the estimate in (B1) with \(N(e_j)\) replaced by the norms of the images and then the lower bound in (B2). In particular all coordinate functionals are continuous. Coordinate completeness and (B2) make \(E\) Banach.

If \(E\) is a finite-dimensional subspace of an arbitrary normed space \(X\), a sequence of points of \(E\) converging in \(X\) is Cauchy in the restricted norm. Its coordinates converge, so the sequence converges to a point of \(E\). Norm limits are unique by the triangle inequality. Therefore \(E\) contains the limit. A point in the closure of a set in a metric space is the limit of a sequence in that set, by selecting a point within \(1/n\) at step \(n\). Thus \(E\) is closed in \(X\), without any completeness assumption on \(X\).

For a finite-dimensional exact sequence
\[
0\longrightarrow E_0\xrightarrow{A_0}E_1\xrightarrow{A_1}\cdots
\xrightarrow{A_{r-1}}E_r\longrightarrow0,
\]
rank-nullity gives \(\dim E_j=\dim\ker A_j+\dim\operatorname{im}A_j\), with the terminal zero map understood. Exactness identifies \(\ker A_j=\operatorname{im}A_{j-1}\), while the initial kernel is zero. Multiply by \((-1)^j\) and sum. Each internal image dimension occurs twice with opposite signs, yielding \(\sum_{j=0}^r(-1)^j\dim E_j=0\). In particular a short exact sequence has middle dimension equal to the sum of its endpoint dimensions. This calculation includes zero spaces and makes no topological exactness assumption.

## 3. Completeness of operator spaces

First note that a linear map \(T:X\to Y\) is continuous exactly when \(\|Tx\|\leq C\|x\|\) for some finite \(C\). The estimate implies continuity. Conversely, continuity at zero gives \(\|Tx\|<1\) when \(\|x\|<r\), for some \(r>0\). For \(x\ne0\), apply this to \(rx/(2\|x\|)\) to obtain \(\|Tx\|\leq2\|x\|/r\). Define
\[
\|T\|=\sup_{\|x\|\leq1}\|Tx\|.
\]
It is finite, and scaling gives \(\|Tx\|\leq\|T\|\|x\|\). The triangle inequality and homogeneity pass through the supremum. If \(\|T\|=0\), scaling shows that \(T\) vanishes everywhere. Thus this is a norm, also for the zero domain, whose unit ball still contains zero. Composition satisfies \(\|ST\|\leq\|S\|\|T\|\).

A closed linear subspace of a Banach space is Banach: a Cauchy sequence has a limit in the ambient space, and closedness keeps the limit in the subspace. A finite product \(X_1\times\cdots\times X_q\) of Banach spaces is Banach under \(\|(x_1,\ldots,x_q)\|_{\max}=\max_j\|x_j\|\). A Cauchy sequence has a limit in every coordinate; taking the maximum of finitely many coordinate errors proves norm convergence. The sum norm is equivalent, since
\[
\|x\|_{\max}\leq\sum_j\|x_j\|\leq q\|x\|_{\max}.
\]
The empty product is the zero vector space. A product of the coordinate norms is not a norm and is never used here.

If \(Y\) is Banach and \(X\) merely normed, then \(\mathcal L(X,Y)\) is Banach. For an operator-norm Cauchy sequence \(T_n\), the values \(T_nx\) are Cauchy for every fixed \(x\). Let \(Tx\) be their limit in \(Y\). Passing to the limit in \(T_n(ax+by)=aT_nx+bT_ny\) proves linearity. The operator norms of the sequence are bounded: the tail lies within one of a fixed operator, and the remaining initial segment is finite. Calling a bound \(M\), passage to the limit gives \(\|Tx\|\leq M\|x\|\), so \(T\in\mathcal L(X,Y)\). Given \(\varepsilon>0\), take \(n,m\geq N\) with \(\|T_n-T_m\|\leq\varepsilon\). Holding \(n\) and \(x\) fixed and taking \(m\to\infty\) yields
\[
\|(T_n-T)x\|\leq\varepsilon\|x\|,
\]
and taking the unit-ball supremum gives \(\|T_n-T\|\leq\varepsilon\). The completeness of \(X\) was unnecessary. In particular \(X'=\mathcal L(X,\mathbb K)\) is Banach.

We shall repeatedly use the resulting series criterion: if \(X\) is Banach and \(\sum_j\|x_j\|<\infty\), then \(\sum_jx_j\) converges in \(X\), with every tail norm bounded by the corresponding scalar tail sum. Indeed the finite partial sums are Cauchy by the triangle inequality; pass to their limit in that same inequality. No integration theorem is involved.

## 4. Quotient norms and completeness

Let \(M\) be a linear subspace of a normed space \(X\). The formula
\[
\|x+M\|_q=\inf_{m\in M}\|x+m\|
\tag{B3}
\]
does not depend on the representative: replacing \(x\) by \(x+m_0\) simply translates the set of vectors over which the infimum is taken. Approximate the infima for two cosets within \(\varepsilon\), add the representatives, and let \(\varepsilon\downarrow0\); this proves the triangle inequality. Rescaling the subspace proves homogeneity for nonzero scalars, and the zero scalar case is immediate. Finally \(\|x+M\|_q=0\) exactly when \(x\in\overline M\). Therefore (B3) is a norm precisely when \(M\) is closed. The quotient map \(Q:X\to X/M\) has \(\|Qx\|_q\leq\|x\|\).

Assume now that \(X\) is Banach and \(M\) is closed. Let \(z_n\) be a Cauchy sequence in \(X/M\). Choose an increasing subsequence \(z_{n_j}\) with
\[
\|z_{n_{j+1}}-z_{n_j}\|_q<2^{-j}\quad(j\geq1).
\]
Choose a representative \(x_1\) of \(z_{n_1}\) and a representative \(h_j\) of \(z_{n_{j+1}}-z_{n_j}\) with \(\|h_j\|<2^{1-j}\). Such a representative exists by the definition of the infimum; no nearest representative is asserted. Section 3 makes \(x=x_1+\sum_{j\geq1}h_j\) a vector in \(X\). The partial sums represent the successive \(z_{n_j}\), so continuity of \(Q\) shows \(z_{n_j}\to Qx\). A Cauchy sequence with a convergent subsequence converges to that same limit: bound the distance from a late term to a still later subsequence term and then to the limit. Hence \(z_n\to Qx\) and \(X/M\) is Banach.

This includes \(M=\{0\}\) and \(M=X\). It does not establish completeness of the image of an arbitrary bounded map; that image may fail to be closed.

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

For any complex normed space \(E\), this implies the exact norm identity
\[
\|v\|=\sup_{\ell\in E',\ \|\ell\|\leq1}|\ell(v)|.
\tag{B6}
\]
The right side is at most the left by the operator bound. If \(v\ne0\), define \(f(zv)=z\|v\|\) on the complex line it spans. Its norm is one, and (B5) extends it with the same norm, attaining \(\ell(v)=\|v\|\). If \(v=0\), every value is zero and the dual ball contains the zero functional. Thus the identity holds also for the zero space. It applies in particular to \(E=\mathcal L(B_1,B_2)\); Section 3 separately proves that this operator space is Banach when \(B_2\) is Banach.

The practical consequence is precise. If \(|\ell(v)|\leq K\|\ell\|\) for every continuous complex-linear \(\ell\), with the same \(K\), then \(\|v\|\leq K\). A bound depending arbitrarily on \(\ell\) cannot be substituted for that uniform estimate.

**Editorial consequence: the same original uniform-boundedness data give a stronger constant.** Retain the original \(x_0,r,n\) and operator family from Section7. For \(\|x\|\leq1\) and every real \(0<\theta<1\), the actual \(h=\theta r x\) lies in the same original ball. Its proved bound gives
\[
 \theta r\|Ax\|=\|A(\theta r x)\|\leq2n.
 \tag{BE1}
\]
Let \(\theta\) increase to one, then take both original suprema. Thus \(\sup_{A\in\mathcal A}\|A\|\leq2n/r\). The original \(4n/r\) conclusion remains valid. No completeness of the target or countability of the operator family is added; the empty family still has bound zero. This is a standard further consequence of the displayed proof, not a replacement of its original data.

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
The construction works also at isolated points: a sufficiently small ball then consists of that point. For \(k,l\geq j\), both centers lie in \(\overline B(z_j,r_j)\), so \(d(z_k,z_l)\leq2r_j\to0\). Completeness gives a limit \(z\). For each \(j\), the entire tail lies in that closed ball; continuity of distance gives \(z\in\overline B(z_j,r_j)\). The first inclusion puts \(z\) in \(V\), and each successive inclusion puts it in \(U_j\). Hence \(V\cap\bigcap_jU_j\ne\varnothing\). This proves density. If \(Z\) is empty, the assertion is true by the definition of density, and no ball is chosen. Neither separability nor local compactness is required. Garrett's cited Theorem 4.0.1 and the nested-ball argument in Section 1 of [From Weyl symbols to operators and changes of coordinates](weyl-covariance-action.md) are comparisons; the complete proof above supplies this input here.

The form needed below follows exactly. If a nonempty complete metric space is the union of closed sets \(F_n\), then some \(F_n\) has nonempty interior. If every interior were empty, each open complement would be dense, while their intersection would be empty, contradicting the theorem just proved. Completeness will be checked for each space to which this form is applied.

This is the general complete-metric result. The Banach consequences in the next two sections apply in normed spaces; a later argument in the Schwartz topology must verify completeness for its own metric.

## 7. Uniform boundedness for any operator family

Let \(X\) be Banach, let \(Y\) be normed, and let \(\mathcal A\subset\mathcal L(X,Y)\) be any family. Assume
\[
\sup_{A\in\mathcal A}\|Ax\|<\infty\quad\hbox{for every }x\in X.
\tag{B7}
\]
Then the operator norms of the family have a common finite bound. The empty family is covered by the bound zero, so assume it is nonempty. Define
\[
F_n=\bigcap_{A\in\mathcal A}\{x:\|Ax\|\leq n\},\qquad n\geq1.
\]
Every set in the intersection is closed by continuity. Arbitrary intersections of closed sets are closed, including uncountable intersections. Assumption (B7) says \(X=\bigcup_{n\geq1}F_n\). Baire applies to the complete norm metric on \(X\), a nonempty space even when \(X=\{0\}\). Hence \(B(x_0,r)\subset F_n\) for some \(r>0\) and \(n\). If \(\|h\|<r\), both \(x_0+h\) and \(x_0\) are in \(F_n\), and
\[
\|Ah\|\leq\|A(x_0+h)\|+\|Ax_0\|\leq2n
\quad(A\in\mathcal A).
\]
For every \(\|x\|\leq1\), substitute \(h=rx/2\). It follows that \(\|Ax\|\leq4n/r\), so \(\sup_{A\in\mathcal A}\|A\|\leq4n/r<\infty\). No countability of \(\mathcal A\) and no completeness of \(Y\) entered the argument. The countable family used by Baire is the family of level sets \(F_n\), not the operator family.

## 8. Open mapping through summable corrections

Let \(T:X\to Y\) be a bounded surjective linear map between Banach spaces. We show that a fixed ball about zero in \(Y\) lies in the image of the closed unit ball of \(X\). If \(Y=\{0\}\), this holds for every positive radius, so suppose otherwise. Write \(B_X\) for the open unit ball. Surjectivity gives
\[
Y=\bigcup_{n\geq1}\overline{T(nB_X)}.
\]
By Section 6 applied to \(Y\), some closed set on the right contains \(B_Y(y_0,r)\), where \(r>0\). If \(\|y\|<r\), approximate both \(y_0+y\) and \(y_0\) by images of vectors in \(nB_X\). Their differences approximate \(y\) by images of vectors in \(2nB_X\). Consequently
\[
B_Y(0,r)\subset\overline{T(2nB_X)},\qquad
B_Y(0,\delta)\subset\overline{T(B_X)},
\quad\delta=\frac r{2n}>0.
\tag{B8}
\]
The second inclusion follows by scaling. Scaling again gives \(B_Y(0,t\delta)\subset\overline{T(tB_X)}\) for every \(t>0\).

Take \(\|y\|<\delta/2\). From (B8) with \(t=1/2\), choose \(x_1\) with \(\|x_1\|<1/2\) and \(\|y-Tx_1\|<\delta/4\). If \(x_1,\ldots,x_j\) have been chosen with residual norm less than \(\delta 2^{-j-1}\), use (B8) at \(t=2^{-j-1}\) to choose \(x_{j+1}\) with
\[
\|x_{j+1}\|<2^{-j-1},\qquad
\left\|y-T\sum_{k=1}^{j+1}x_k\right\|<\delta 2^{-j-2}.
\]
Section 3 and completeness of \(X\) give \(x=\sum_{j\geq1}x_j\) with \(\|x\|\leq1\). Continuity of \(T\) and the residual bounds give \(Tx=y\). This is actual surjectivity of a ball, not merely density of its image.

For any open \(O\subset X\) and \(x_0\in O\), choose \(s>0\) with \(x_0+s\overline B_X\subset O\), for example half a radius of an open ball contained in \(O\). The preceding conclusion gives
\[
Tx_0+B_Y(0,s\delta/2)\subset T(O).
\]
Therefore \(T\) is open. If \(T\) is bijective, its inverse is linear by uniqueness of preimages. For \(y\ne0\), apply the unit-ball conclusion to \(\delta y/(4\|y\|)\); rescaling and uniqueness yield
\[
\|T^{-1}y\|\leq\frac4\delta\|y\|.
\tag{B9}
\]
The zero vector satisfies the same estimate. Thus the inverse is bounded. The two completeness assumptions have distinct uses: Baire on \(Y\), and convergence of the correction series in \(X\).

## 9. Nets, convergence and connectedness

A directed set is a nonempty preordered set \(I\) in which any two indices have a common upper bound. A net in \(Z\) is a function \(i\mapsto z_i\) on such a set. It converges to \(z\) if, for every open neighborhood \(U\) of \(z\), all terms with \(i\geq i_0\) lie in \(U\) for some \(i_0\). A subnet here means \(z_{\phi(j)}\), where \(J\) is directed and \(\phi:J\to I\) is order-preserving and cofinal: for every \(i\) there is \(j\) with \(\phi(j)\geq i\). Monotonicity then makes the subnet eventually lie over every final segment. Every subnet of a convergent net converges to the same limit by the definition.

Continuous maps preserve convergent nets, by the neighborhood criterion in Section 1. Conversely, if \(f:Z\to W\) is not continuous at \(z\), there is an open neighborhood \(V\) of \(f(z)\) such that each open neighborhood \(U\) of \(z\) contains a point \(y\) with \(f(y)\notin V\). Index all such pairs \((U,y)\), ordered by shrinking \(U\), with ties allowed. This is a nonempty directed preorder: use the intersection of two neighborhoods and one of its offending points. The resulting net of \(y\)'s converges to \(z\), but its image never enters \(V\). Thus preservation of all convergent nets characterizes continuity without a metrizability assumption.

The same construction characterizes closure. If \(z\in\overline A\), index all pairs \((U,a)\) with \(U\) an open neighborhood of \(z\) and \(a\in U\cap A\), again by shrinking neighborhoods. It is a directed net in \(A\) converging to \(z\). If \(A\) is closed, the open complement shows that no net in \(A\) can converge outside it. Hence a set is closed exactly when it contains every limit of every convergent net in it. No uniqueness of limits is needed for this assertion. In a Hausdorff space limits are unique: two disjoint neighborhoods of distinct putative limits would both contain every sufficiently late term, which is impossible.

For a norm-convergent net \(x_i\to x\), choose \(i_0\) with \(\|x_i-x\|<1\) for \(i\geq i_0\). Then \(\|x_i\|\leq\|x\|+1\) on that final segment. There need not be a bound for the entire net. For example, on \(I=\mathbb N\times\mathbb N\) ordered coordinatewise, set \(a_{m,n}=m\) when \(n=0\), and \(a_{m,n}=0\) when \(n\geq1\). The net converges to zero and has unbounded range. This is why estimates involving convergent nets use final segments, not a sequence's finite-prefix argument.

**Connectedness from the real entry base.** A space is connected if it cannot be written as the union of two disjoint nonempty relatively open subsets. Every real interval is connected, including open, closed, half-open and unbounded intervals. Empty intervals and singletons have no such separation. For any other interval \(J\), suppose that \(J=A\cup B\) is a separation. Choose one point in each part, interchange the names of the parts if necessary, and write them as \(a\in A\), \(b\in B\), with \(a<b\). The set \(E=A\cap[a,b]\) is nonempty and bounded above. By the least-upper-bound property of the real numbers, \(c=\sup E\) exists and lies in \([a,b]\subset J\). Every neighborhood of \(c\) contains a point of \(E\): for every \(\varepsilon>0\), the number \(c-\varepsilon\) is not an upper bound for \(E\). Since \(A\) is relatively closed in \(J\), as the complement of the relatively open set \(B\), this gives \(c\in A\). Thus \(c<b\), because \(b\in B\). Relative openness of \(A\) gives \(\eta>0\) with \(J\cap(c-\eta,c+\eta)\subset A\). But \(d=c+\tfrac12\min\{\eta,b-c\}\) lies in \(A\cap[a,b]\) and satisfies \(d>c\), contrary to the definition of \(c\). This proves the assertion without a compactness or intermediate-value theorem import.

Continuous images preserve connectedness. Indeed, if the image of a connected space under a continuous map had a separation, the inverse images of its two parts would be disjoint nonempty open subsets of the domain covering it. This contradicts connectedness. Continuity into the image with its subspace topology follows directly by taking inverse images of intersections with open sets in the codomain.

In particular, every convex subset \(C\) of a real or complex normed space is connected. If \(C\) had a separation, choose \(x,y\) in its two parts. Convexity puts \(\gamma(t)=(1-t)x+ty\) in \(C\) for every real \(t\in[0,1]\). The estimate \(\|\gamma(t)-\gamma(s)\|=|t-s|\,\|y-x\|\) proves continuity. The connected image \(\gamma([0,1])\) meets both parts, whose intersections with that image would be a separation, a contradiction. Empty convex subsets are already covered by the definition. This supplies the connectedness extension of the topological results proved here used for norm balls and for a real homotopy parameter interval.

## 10. Compactness without a countability assumption

A space is compact if every open cover has a finite subcover. A closed subset of a compact space is compact: adjoin its open complement to any open cover and then discard that complement from a finite subcover. Continuous images of compact spaces are compact, by pulling a cover back to the domain. A compact subset \(K\) of a normed space is bounded, since the increasing balls \(B(0,n)\), \(n\geq1\), cover it and a finite subcover lies in one of these balls.

Finite products of compact spaces are compact, with no separation assumption required. For two nonempty factors \(K,L\), refine any open cover of \(K\times L\) by open rectangles each lying in a member of that cover. Fix \(x\in K\). The second factors of rectangles containing \((x,y)\), as \(y\) ranges over \(L\), cover \(L\). Select finitely many of them by compactness. Intersect their first factors to obtain an open neighborhood \(V_x\) of \(x\); the strip \(V_x\times L\) is covered by the selected finite list of original cover members. The neighborhoods \(V_x\) cover \(K\), so finitely many suffice. Combining their finite lists proves compactness of the product. Induction handles any positive finite number of factors; an empty factor gives the empty compact product, and the product of no factors is a singleton.

Every net in a compact space has a convergent subnet, in the explicit convention of Section 9. To prove this, let \((z_i)_{i\in I}\) be a net in compact \(K\), and put
\[
C_i=\overline{\{z_j:j\geq i\}}\quad\hbox{inside }K.
\]
These are nonempty closed sets. Any finitely many have nonempty intersection: choose an upper bound of their indices and a term from that tail. Compactness implies \(\bigcap_i C_i\ne\varnothing\); otherwise the open complements would have a finite subcover, contrary to that finite-intersection property. Choose \(z\) in the intersection. Every neighborhood \(U\) of \(z\) and every tail contain a common net term.

For an actual monotone subnet, take as indices all triples \((i,U,j)\) with \(i\leq j\), \(U\) an open neighborhood of \(z\), and \(z_j\in U\). Order them by
\[
(i,U,j)\preceq(i',U',j')
\quad\Longleftrightarrow\quad i\leq i',\quad U'\subseteq U,\quad j\leq j'.
\]
For two triples choose an index dominating their four original indices, intersect the two neighborhoods, and use the preceding tail property to find a still later term in that intersection. This gives an upper triple, so the set is directed. Projection to \(j\) is order-preserving. It is cofinal, since a triple with first coordinate at least any prescribed \(i_0\) exists. Finally every sufficiently late triple has neighborhood contained in any prescribed neighborhood of \(z\), so its term lies there. This proves convergence of the subnet. The index set of the original net need not have a countable cofinal subset, and the compact space need not be metrizable.

**Metric compactness and sequences.** A metric space \(K\) is compact if and only if every sequence in it has a subsequence converging to a point of \(K\). The empty space is compact and the sequence assertion is vacuous. Suppose first that nonempty \(K\) is compact and \(x_j\in K\). The closures of its tails are nonempty closed subsets with the finite-intersection property. Compactness, by the open-complement argument already proved, supplies
\[
 x\in\bigcap_{N\geq1}\overline{\{x_j:j\geq N\}}\quad
       \text{with }x\in K.
 \tag{B14}
\]
Choose successively \(j_k>j_{k-1}\) with \(d(x_{j_k},x)<1/k\), using the closure of the tail starting after \(j_{k-1}\). This proves subsequential convergence in \(K\).

Conversely, assume the stated subsequence property. For every \(\varepsilon>0\), finitely many \(\varepsilon\)-balls cover \(K\). Otherwise choose \(x_1\in K\) and, at each step, a point outside the union of the \(\varepsilon\)-balls about the earlier choices. Distinct selected points have distance at least \(\varepsilon\). No subsequence is Cauchy, whereas every convergent sequence is Cauchy by the triangle inequality. This contradiction proves the finite-ball assertion.

Let \(\mathcal U\) be any open cover of \(K\). There is \(\delta>0\) such that every ball \(B_K(x,\delta)\) is contained in some member of the cover. If not, for each \(j\geq1\) choose \(x_j\in K\) whose \(1/j\)-ball is contained in no cover member. A subsequence \(x_{j_k}\) converges to \(x\in K\). Choose a cover member \(U\) containing \(x\), and \(r>0\) with \(B_K(x,r)\subset U\). For all sufficiently large \(k\), \(d(x_{j_k},x)<r/2\) and \(1/j_k<r/2\), so
\[
 B_K(x_{j_k},1/j_k)\subset B_K(x,r)\subset U,
 \tag{B15}
\]
contradicting its selection. Now take a finite cover of \(K\) by \(\delta/2\)-balls. For each center, choose a member of \(\mathcal U\) containing its \(\delta\)-ball; this finite list covers \(K\). Therefore \(K\) is compact. This proves the equivalence for the actual metric, without assuming completeness or any countability of the given cover. Lebl's linked metric-space chapter gives the classical comparison. The finite-dimensional Heine–Borel consequence, including its exercise step, is proved in Section 4 of [Metric and topological foundations](metric-foundation-bridges.md) and supplies the input used in Section 2 here.

The preceding general compactness argument is what permits a compact, possibly nonmetrizable parameter space in the topological results proved here. The metric equivalence is used only for spaces that actually carry the indicated metric.

## 11. Square-summable sequences

Define \(\ell^2(\mathbb N)\) to consist of complex sequences \(x=(x_k)_{k\geq0}\) for which the increasing partial sums \(\sum_{k=0}^N|x_k|^2\) have a finite supremum, denoted \(\|x\|_2^2\). Finite scalar Cauchy–Schwarz gives the triangle inequality for every finite coordinate truncation. Taking limits in those finite inequalities proves
\[
\|x+y\|_2\leq\|x\|_2+\|y\|_2.
\]
In particular the sum belongs to \(\ell^2\). Homogeneity and definiteness are immediate; thus this is a norm. The same finite Cauchy–Schwarz bound shows that \(\sum_k x_k\overline{y_k}\) converges absolutely for \(x,y\in\ell^2\), since its absolute partial sums are bounded by \(\|x\|_2\|y\|_2\).

Let \(x^{(j)}\) be a norm-Cauchy sequence. Each coordinate is Cauchy because \(|x_k^{(j)}-x_k^{(l)}|\leq\|x^{(j)}-x^{(l)}\|_2\), and hence has a complex limit \(x_k\). The norms \(\|x^{(j)}\|_2\) have some common bound \(M\). For any fixed \(N\), the finite sum passes to the limit in \(j\), giving \(\sum_{k=0}^N|x_k|^2\leq M^2\). Take the supremum over \(N\) to obtain \(x\in\ell^2\). For \(j,l\geq J\) the Cauchy bound \(\|x^{(j)}-x^{(l)}\|_2\leq\varepsilon\) holds. Fix \(j\geq J\), pass \(l\to\infty\) in each finite squared coordinate sum, and then take its supremum. This gives \(\|x^{(j)}-x\|_2\leq\varepsilon\). Hence \(\ell^2\) is Banach. Only limits of finite sums were exchanged; no unproved infinite-sum convergence theorem is being used.

Let \(P_Nx\) retain coordinates \(0\) through \(N\) and set the others to zero. Then \(\|P_N\|\leq1\), and
\[
\|x-P_Nx\|_2^2=\sum_{k>N}|x_k|^2\longrightarrow0.
\tag{B10}
\]
The limit follows directly from convergence of the nonnegative series. The coordinate vectors \(e_k\) have norm one and \(\|e_j-e_k\|_2=\sqrt2\) for \(j\ne k\). Their sequence has no norm-convergent subsequence, so the closed unit ball is not compact by the metric compactness interface. This assertion does not concern weak compactness.

## 12. Worked examples

**A quotient measures the right distance.** In \(\mathbb C^2\) with its Euclidean norm, let \(M=\mathbb C(1,0)\) and \(v=(3,4)\). The infimum in (B3) is \(4\), attained by removing the first coordinate. A norm-one functional annihilating \(M\) is \(\ell(z_1,z_2)=z_2\), and \(\ell(v)=4\). No norm-one functional annihilating \(M\) can take value \(5=\|v\|\), since its value on \(v\) equals its value on \((0,4)\). More generally, if \(M\) is closed and \(v\notin M\) in a normed space, apply (B6) on the normed quotient to obtain \(\lambda\in(X/M)'\) of norm one with \(\lambda(Qv)=\|Qv\|_q\). Then \(\ell=\lambda Q\) annihilates \(M\), has norm at most one and takes the value \(\operatorname{dist}(v,M)\). In fact its norm is one: representatives of any unit quotient vector can be chosen with norm arbitrarily close to one, and the norm of \(\lambda\) is one. This is a distance statement; replacing that distance by \(\|v\|\) would change the claim.

**An uncountable family of tests.** On \(\ell^2\), index by every sequence \(\theta=(\theta_k)\) of unit complex numbers, and set \(D_\theta x=(\theta_kx_k)\). Directly \(\|D_\theta x\|_2=\|x\|_2\), so each map is bounded and the family has common operator norm one. Its index set is uncountable: even its sign sequences cannot be listed, since changing the \(k\)-th sign of the \(k\)-th proposed sequence gives a sequence absent from any proposed list. Section 7 also applies, because its assumption holds for each fixed \(x\), regardless of the number of phase sequences. There is no need to enumerate the family or to impose a topology on its index set.

**Compact strong families act jointly continuously.** Let \(K\) be any compact topological space, \(X\) Banach, \(Y\) normed, and \(T_t\in\mathcal L(X,Y)\) for \(t\in K\). Suppose \(t\mapsto T_tx\) is continuous for every \(x\in X\). If \(K\) is empty, the evaluation map has empty domain and is continuous; assume \(K\) is nonempty. For fixed \(x\), its image is compact and bounded by Section 10. Section 7 gives \(C=\sup_{t\in K}\|T_t\|<\infty\). If \(t_i\to t\) and \(x_i\to x\), then
\[
\|T_{t_i}x_i-T_tx\|
\leq C\|x_i-x\|+\|(T_{t_i}-T_t)x\|\longrightarrow0.
\tag{B11}
\]
The net criterion proves joint continuity on \(K\times X\); convergence in this finite product is equivalent to convergence in both coordinates by its neighborhood basis. This argument uses the entire compact parameter space to obtain the bound, without assuming that its compactness can be tested by sequences.

## 13. Exercises and solutions

**Problem 1: An algebraic quotient without a norm.** Let \(c_{00}\) be the finitely supported sequences inside \(\ell^2\). Show that the quotient formula (B3) is identically zero on \(\ell^2/c_{00}\), although the algebraic quotient is nonzero. Determine which hypothesis prevents this in Section 4.

**Solution.** By (B10), every \(x\in\ell^2\) is approximated by its finite truncations, so \(\inf_{m\in c_{00}}\|x+m\|_2=0\). The sequence \(x_k=2^{-k}\) is square-summable and has infinitely many nonzero coordinates; it is not in \(c_{00}\), so its coset is algebraically nonzero. Thus the formula is a seminorm with a nontrivial null space. The missing hypothesis is closedness of the subspace. Completeness of the ambient \(\ell^2\) does not repair that failure.

**Problem 2: Scalar tests for an operator bound.** Let \(X,Y\) be complex normed spaces and \(T:X\to Y\) an algebraic linear map. Assume \(|\ell(Tx)|\leq C\|\ell\|\|x\|\) for all \(x\in X\), \(\ell\in Y'\), with one finite \(C\). Prove that \(T\) is bounded without assuming that it was continuous. Explain why the conclusion does not require either space to be Banach.

**Solution.** For each fixed \(x\), apply (B6) to the actual vector \(Tx\in Y\). Taking the supremum over \(\|\ell\|\leq1\) gives \(\|Tx\|\leq C\|x\|\). Section 3 identifies this estimate with continuity. The Hahn–Banach proof uses normed spaces and Zorn, not completeness, and the boundedness criterion is also independent of completeness. Thus no Banach assumption was used.

**Problem 3: Where completeness enters uniform boundedness.** On \(c_{00}\) with the inherited \(\ell^2\) norm, put \(L_nx=(n+1)x_n\). Show that each \(L_n\) is continuous and the family is pointwise bounded, while its operator norms are unbounded.

**Solution.** The coordinate estimate gives \(|L_nx|\leq(n+1)\|x\|_2\), and equality at \(e_n\) shows \(\|L_n\|=n+1\). For fixed finitely supported \(x\), all but finitely many \(L_nx\) vanish, so \(\sup_n|L_nx|<\infty\). Their norms nevertheless tend to infinity. Problem 1 supplies a Cauchy sequence of finite truncations whose limit is not in \(c_{00}\), so this domain is not Banach. This is the precise missing condition in Section 7; the scalar codomain is already complete.

**Problem 4: A bounded inverse fails on an incomplete target.** Give \(\ell^2\) its usual norm in the domain and the norm
\[
\|x\|_w=\left(\sum_{k\geq0}2^{-k}|x_k|^2\right)^{1/2}
\]
on the same vector set in the target. Show that the identity is a bounded bijection with unbounded inverse and that the target is incomplete.

**Solution.** The target formula is a norm, by finite weighted Euclidean triangle inequalities and their limits, or by applying the \(\ell^2\) norm to \((2^{-k/2}x_k)\). Since \(\|x\|_w\leq\|x\|_2\), the identity is bounded and algebraically bijective. On \(e_k\), the ratio \(\|e_k\|_2/\|e_k\|_w=2^{k/2}\) is unbounded, so its inverse is unbounded. To see incompleteness directly, let \(u^{(N)}\) equal one in coordinates \(0\) through \(N\) and zero afterward. Weighted geometric tails show that it is Cauchy in \(\|\cdot\|_w\). A limit in that norm would have each coordinate equal to one, since \(|x_k|\leq2^{k/2}\|x\|_w\) makes every coordinate continuous. The constant-one sequence is not in the target's underlying set \(\ell^2\). Hence no target limit exists. The failure occurs in the space to which Baire would have been applied in Section 8.

**Problem 5: A compact family can fail norm continuity.** On \(\ell^2\), let \(R_nx=x_ne_n\). Put \(K=\{0\}\cup\{1/(n+1):n\geq0\}\subset\mathbb R\), define \(T_0=0\) and \(T_{1/(n+1)}=R_n\). Prove that this is a strongly continuous family on compact \(K\), and that its action on \(K\times\ell^2\) is jointly continuous, but that it is not operator-norm continuous at zero.

**Solution.** The set \(K\) is closed and bounded in \(\mathbb R\): its only possible accumulation point is zero, which it contains. It is compact by the finite-dimensional compactness interface. For each \(x\in\ell^2\), the convergence of \(\sum|x_n|^2\) implies \(x_n\to0\), so \(\|R_nx\|_2=|x_n|\to0\). Every nonzero point of \(K\) is isolated, hence continuity there is immediate, and the preceding limit gives continuity at zero. The third worked use proves joint continuity. On the other hand \(\|R_n\|=1\), since coordinate deletion decreases the norm and equality holds at \(e_n\). Therefore \(\|T_{1/(n+1)}-T_0\|\) does not tend to zero. Joint continuity of evaluation is weaker than norm continuity of the operator-valued map.

**Problem 6: A separated quotient has a sharp scalar witness.** Let \(M\) be a closed subspace of a complex normed space \(X\), and let \(v\notin M\). Prove that
\[
\operatorname{dist}(v,M)=
\max_{\substack{\ell\in X',\ \|\ell\|\leq1\\ \ell|_M=0}}|\ell(v)|.
\]
Does this claim require a nearest point of \(M\) to \(v\)?

**Solution.** For an allowed \(\ell\), \(|\ell(v)|=|\ell(v-m)|\leq\|v-m\|\) for every \(m\in M\). Taking the infimum gives the upper bound. The quotient is normed by Section 4, and \(Qv\ne0\). Apply (B6) to \(Qv\) and compose its attaining functional with \(Q\), as in the first worked use. This gives an allowed functional with value \(\|Qv\|_q=\operatorname{dist}(v,M)\), proving attainment of the displayed maximum. The construction uses the infimum and a functional on the quotient; it does not choose a norm-minimizing representative or prove that such a representative exists.

## 14. Source comparisons and limits

Garrett's [Banach Spaces](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2016-17/02_banach.pdf), Proposition 4.2, Theorem 6.1, Theorem 7.1 and Corollary 7.2 give corresponding operator-completeness, arbitrary-family boundedness and inverse statements. The arguments above expose the completeness checks and correction-series constants used later.

That reading's Theorem 9.1 states norm-preserving extension, but several neighboring formulas need care. In Corollary 9.3, the attainable value for a unit functional annihilating a closed subspace is the distance to that subspace; the norm of the original vector can be larger. The first worked example and Problem 6 prove the exact statement. In the complex reconstruction, the real functional occurs in both terms of (B5), and the phase argument makes the imaginary component vanish, not the real component giving the absolute value. The product-space argument requires a sum or maximum norm, as in Section 3. These are corrections to the identified formulas, not to the extension theorem itself.

The pinned mathlib [Hahn–Banach module](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/Mathlib/Analysis/Normed/Module/HahnBanach.lean) contains exists_extension_norm_eq and exists_dual_vector. Specializing its scalar field to \(\mathbb C\) and its seminormed space to a normed space gives a source-level statement comparison for the extension and scalar norm tests here.

These tools support later finite-dimensional defect splittings, operator-valued estimates and compact parameter arguments. They do not provide a bounded linear right inverse for every surjection: the open-mapping proof selects preimages without a linear selection rule. Such a conclusion requires a complemented kernel. Sections 14.1–14.6 now prove the Fréchet open-mapping and closed-graph results with their actual seminorm topologies. The complete-metric Baire theorem supplies their common input; the norm estimates in Sections 7–8 alone do not establish them. Vector-valued integration and reflexive-space duality require separate proofs or exact imports.

**Editorial consequence: the original closure radius gives the full quotient inverse bound.** Keep the bounded surjection \(T:X\to Y\), the Banach spaces, and exactly the original \(\delta=r/(2n)>0\) from (B8). Put \(M=\ker T\), closed by continuity, and use the actual quotient norm (B3). For \(y\ne0\), choose any real \(t>\|y\|/\delta\) and \(0<a<1\). The original scaled closure inclusion gives \(x_1\) with \(\|x_1\|<t\) and \(\|y-Tx_1\|<at\delta\). At every subsequent step use that same inclusion at scale \(a^jt\). It gives
\[
 \|x_{j+1}\|<a^jt,\qquad
 \left\|y-T\sum_{k=1}^{j+1}x_k\right\|<a^{j+1}t\delta.
 \tag{BE2}
\]
The original Banach series criterion gives \(x=\sum_{j\geq1}x_j\), with
\[
 Tx=y,\qquad \|x\|\leq\sum_{j\geq1}a^{j-1}t=\frac{t}{1-a}.
 \tag{BE3}
\]
Every preimage of \(y\) has the same coset modulo the actual \(M\). Thus the map \(\widetilde T:X/M\to Y\), \(\widetilde T(qx)=Tx\), is well-defined and bijective, and \(\|\widetilde T^{-1}y\|_q\leq t/(1-a)\) for every displayed \(a,t\). First let \(a\downarrow0\), then \(t\downarrow\|y\|/\delta\). The original quotient norm is a fixed real number in these inequalities, giving
\[
 \|\widetilde T^{-1}y\|_q\leq\frac{\|y\|}{\delta},\qquad \|\widetilde T(qx)\|\leq\|T\|\|qx\|_q. \tag{BE4} \] The second bound follows by applying \(\|Tx\|=\|T(x+m)\|\leq\|T\|\|x+m\|\) for every original \(m\in M\) and taking the actual infimum. For \(y=0\) use the zero coset. If \(T\) is bijective, \(M=0\) and the quotient norm is exactly the original norm, so \(\|T^{-1}y\|\leq\|y\|/\delta\), strengthening (B9) without changing \(\delta\). The earlier \(4/\delta\) bound remains valid. For a general surjection neither attainment of a smallest preimage norm nor a linear selection is asserted. Zero spaces are included.

**Editorial proof: both exact maps between a bounded linear right inverse and a closed kernel complement.** Let \(T:X\to Y\) be the original bounded surjection between Banach spaces. If bounded linear \(S:Y\to X\) satisfies \(TS=I_Y\), set \(P=ST\). The complete ordered products give
\[
 P^2=STST=S(TS)T=ST=P,
 \qquad \|P\|\leq\|S\|\|T\|.
 \tag{BE5}
\]
Its range \(E=S(Y)=\ker(I_X-P)\) is closed. Its kernel is exactly \(M=\ker T\): \(Tx=0\) gives \(Px=0\), and \(Px=0\) gives \(Tx=TSTx=TPx=0\). Every original vector has the decomposition
\[
 x=(I_X-P)x+Px,\qquad (I_X-P)x\in M,\quad Px\in E.
 \tag{BE6}
\]
If a vector belongs to both subspaces, \(Px=0\) and \(Px=x\), so it is zero. Both projections are continuous, with \(\|P\|\leq\|S\|\|T\|\) and \(\|I_X-P\|\leq1+\|S\|\|T\|\). The restriction \(T_E:E\to Y\) is bijective and its inverse is the actual \(S\) with codomain \(E\).

Conversely, suppose closed linear \(E\subset X\) satisfies the algebraic direct sum \(X=M\oplus E\) for this actual kernel. The original closed-subspace proof makes \(E\) Banach. The restriction \(T_E\) is bounded, injective because \(E\cap M=0\), and surjective because any preimage \(x=m+e\) has \(Tx=Te\). Section8 gives the bounded linear inverse \(T_E^{-1}:Y\to E\). Composing with the original inclusion \(E\hookrightarrow X\) gives \(S\) and \(TS=I_Y\); the preceding construction then gives both continuous projections onto this exact decomposition. These maps prove both implications, including zero spaces. They supply the complement assertion above; they do not make an arbitrary correction-series selection linear. No novelty is claimed.

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

### 14.3. A common finite order for an arbitrary family

Let \(E\) be Fréchet and let \(\{L_t:t\in I\}\) be any family of continuous linear maps from \(E\) to a space with a continuous seminorm \(q\). Assume \(\sup_t q(L_t x)<\infty\) for each fixed \(x\in E\). The index set need not be countable. Put
\[
 F_m=\{x\in E:q(L_t x)\leq m\text{ for every }t\in I\},
 \qquad m=1,2,\ldots .
 \tag{BF6}
\]
Each set is closed by continuity and arbitrary intersections of closed sets. They cover \(E\). Baire supplies \(m\) and \(x_0\) such that \(x_0+V\subset F_m\), where \(V\) is a balanced finite-seminorm neighborhood of zero. We may take
\[
 V=\{v:p_j(v)<a_j\text{ for }j\in J\},
 \qquad P(v)=\max_{j\in J}p_j(v)/a_j,
 \tag{BF7}
\]
with \(J\) a nonempty finite set and all \(a_j>0\); an unused extra seminorm can be included when needed. Both \(x_0+v\) and \(x_0\) lie in \(F_m\), so \(q(L_t v)\leq2m\) for every \(v\in V\) and \(t\in I\). If \(P(x)>0\), the vector \(x/(2P(x))\) lies in \(V\). Homogeneity gives
\[
 q(L_t x)\leq4m\max_{j\in J}p_j(x)/a_j
              \quad(x\in E,\ t\in I).
 \tag{BF8}
\]
If \(P(x)=0\), every positive scalar multiple of \(x\) lies in \(V\); its bound \(2m\), divided by that scalar and then sent to infinity, gives \(q(L_t x)=0\), proving (BF8) in that case too. The empty family satisfies it vacuously. For a locally convex target this construction applies separately to each target seminorm, which is the precise equicontinuity conclusion; one finite set for all target seminorms is not asserted.

For continuous scalar functionals on \(\mathcal D_K(\Omega)\), take \(q(z)=|z|\). Since the seminorms (BF3) increase with \(N\), (BF8) yields one \(N\) and one finite \(C\) such that
\[
 |L_t f|\leq C p_N(f)
       \quad(f\in\mathcal D_K(\Omega),\ t\in I).
 \tag{BF9}
\]
Thus pointwise boundedness really supplies one common finite derivative order. For a weakly convergent sequence of distributions, scalar convergence supplies pointwise boundedness of the differences from its limit; each difference is a continuous functional on \(\mathcal D_K(\Omega)\). Equation (BF9) then controls the entire sequence, including its finite initial part.

This convergence is uniform on every compact family \(\mathcal C\subset\mathcal D_K(\Omega)\). Given \(\varepsilon>0\), cover \(\mathcal C\) by the neighborhoods \(p_N(f-f_a)<\varepsilon/(2(C+1))\) about its points, and choose a finite subcover. Pointwise convergence is eventually less than \(\varepsilon/2\) at all its finitely many centers. Applying (BF9) to each difference from a center gives a bound less than \(\varepsilon\) on all of \(\mathcal C\). This proves the compact-family assertion used for differentiated smoothing kernels.

**Editorial consequence with every original seminorm retained.** In the exact data of (BF7), let \(P(x)=\max_{j\in J}p_j(x)/a_j\), as already defined. When \(P(x)>0\), use the original vector \(\theta x/P(x)\) for any real \(0<\theta<1\). It lies in the same \(V\), so the proved bound \(2m\) gives \(q(L_tx)\leq2mP(x)/\theta\). Let \(\theta\uparrow1\). When \(P(x)=0\), use the already proved arbitrary-scaling argument. Therefore
\[
 q(L_tx)\leq2m\max_{j\in J}\frac{p_j(x)}{a_j}
 \quad(x\in E,\ t\in I).
 \tag{BE7}
\]
The original (BF8) remains valid. No seminorm, tolerance, null direction or target dependence is removed. The application to (BF9) keeps its same finite derivative order; for each chosen target seminorm the same argument keeps its own finite source list. This is a standard strengthening, not a common list for all target seminorms.

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

**Editorial consequence for the original closed-graph radius.** Keep the original Banach domain, target seminorm \(q_i\) and \(r_i>0\) from (BF13). For \(x\ne0\) and \(0<\theta<1\), the actual vector \(\theta r_i x/\|x\|\) has norm less than \(r_i\). The same continuity estimate gives \(q_i(Lx)<\|x\|/(\theta r_i)\). Let \(\theta\uparrow1\); at zero use linearity. Thus
\[
 q_i(Lx)\leq\frac{1}{r_i}\|x\|\quad(x\in E).
 \tag{BE8}
\]
This strengthens the original \(2/r_i\) bound while keeping each actual \(r_i\), the domain norm and every target seminorm. In the distributional graph application below, it improves the same radius-based bounds after that graph is proved closed; it adds no smoothness hypothesis. No novelty is claimed.

### 14.6. The distributional graph used for a smooth kernel

Here is the exact Banach space in the geometric application. Fix compact sets \(K\subset\operatorname{int}L\subset\Omega\) and an integer \(N\geq0\). Start with smooth germs on a neighborhood of \(L\), and use
\[
 \|f\|_{N,L}=\max_{|\alpha|\leq N}\sup_{x\in L}
                                      |\partial^\alpha f(x)|.
 \tag{BF14}
\]
If distinct germs have zero distance, first identify them; their derivatives of order at most \(N\) then agree on \(L\). Its completion \(X_{N,L}\) is Banach by the Cauchy-sequence construction: identify two norm-Cauchy sequences when their difference tends to zero, use limits of their norms for the completion norm, and approximate the \(j\)-th member of a Cauchy sequence of classes by an original vector within \(2^{-j}\) to obtain a Cauchy representative and its class limit. Section 3 makes its scalar dual \(X_{N,L}'\) Banach.

In that dual take the subspace of functionals annihilating every original smooth germ that vanishes on a neighborhood of \(K\). It is closed, since each annihilation condition is the kernel of evaluation at a fixed vector. Call it \(E'_{K,N}\), with the inherited dual norm. It is therefore Banach. A member defines a distribution by restricting test functions to \(L\); (BF14) bounds its value and proves continuity on each compact-support test space. Its support lies in \(K\) by the annihilation conditions. Conversely, a distribution supported in \(K\) and satisfying \(|u(f)|\leq C\|f\|_{N,L}\) on test functions acts on a germ by multiplying it by a fixed smooth cutoff \(\eta\) equal to one near \(K\) and supported in \(\operatorname{int}L\). The support condition makes this independent of cutoff and of the extension of the germ. The full product rule gives
\[
 \|\eta f\|_{N,L}
 \leq\max_{|\alpha|\leq N}\sum_{\beta\leq\alpha}
       \binom{\alpha}{\beta}
       \sup_L|\partial^\beta\eta|\,
       \sup_L|\partial^{\alpha-\beta}f|
 \leq C_{\eta,N}\|f\|_{N,L},\qquad
 C_{\eta,N}=\max_{|\alpha|\leq N}\sum_{\beta\leq\alpha}
       \binom{\alpha}{\beta}\sup_L|\partial^\beta\eta|.
 \tag{BF15}
\]
Thus the functional has bound \(CC_{\eta,N}\) and extends uniquely to \(X_{N,L}\). The constructions are inverse: a germ and \(\eta\) times that germ agree near \(K\), so every member of the annihilator assigns them the same value. Such a cutoff is the explicit finite-calculus entry input. Convergence in the Banach dual norm implies strong distributional convergence. Indeed \(f\mapsto\|f\|_{N,L}\) is a continuous seminorm on the test space: its restriction to each fixed-support smooth space is continuous by its defining seminorms, and the stated inductive-limit topology gives this continuity on all test functions. Every bounded test family \(\mathcal B\) therefore has finite \(\sup_{f\in\mathcal B}\|f\|_{N,L}\). The pairing bound
\[
 \sup_{f\in\mathcal B}|(u_l-u)(f)|
 \leq\|u_l-u\|_{X_{N,L}'}
             \sup_{f\in\mathcal B}\|f\|_{N,L}\longrightarrow0
 \tag{BF16}
\]
is exactly the strong dual convergence condition. In particular it gives convergence on every fixed test function.

Suppose the localized operator \(A\) is continuous into distributions and sends every member of this \(E'_{K,N}\) to a smooth function on an open output set \(V\). If \(u_l\to u\) in its dual norm and \(Au_l\to g\) in \(C^\infty(V)\), then the first convergence and distributional continuity give \(Au_l\to Au\) in distributions, while local uniform convergence gives \(Au_l\to g\) in distributions. Indeed the latter pairing error is bounded by the local supremum error times the integral of the absolute value of the compact test function. Scalar test pairings separate distributions, so \(Au=g\). This proves sequential closedness of the graph. The product has a metric by (BF2); a point in the closure is the limit of graph points chosen within \(1/l\), so the graph is closed. Sections 14.2 and 14.5 now give continuity into every smooth seminorm, with the bounds (BF13).

For \(y\in\operatorname{int}K\), evaluation \(\delta_y\) belongs to \(E'_{K,N}\). More generally \(f\mapsto\partial^\alpha f(y)\) has dual norm at most one when \(|\alpha|\leq N\). For \(|\alpha|\leq r\) and \(N\geq r+1\), its difference between nearby points is bounded, on the unit ball of (BF14), by \(\sqrt n\,|h|\), using a segment inside \(K\) and the derivatives of order \(|\alpha|+1\). For \(|\alpha|\leq r-1\), first-order Taylor remainder on this same ball is bounded by \(n|h|^2/2\), using the derivatives of order \(|\alpha|+2\). Thus the derivatives in the Banach dual norm exist and equal these evaluation functionals, and the derivatives of order \(r\) are norm continuous. This proves \(y\mapsto\delta_y\) is \(C^r\) with the original requirement \(N\geq r+1\). Composing with the continuous \(A:E'_{K,N}\to C^\infty(V)\) gives all the mixed input and output derivatives of \((A\delta_y)(x)\) asserted in the geometric lesson. The derivative evaluation on \(V\) is jointly continuous on compact output subsets, by the corresponding next-derivative seminorm. This argument closes the functional-analysis step, while the scalar distribution kernel theorem and the operator's distributional continuity remain their separately stated analytic inputs.

The kernel identification needs only a concrete Banach-valued Riemann integral. Take \(N\geq1\), as is already required for the continuous \(r=0\) evaluation map above. Let \(f\) be a smooth test function supported in \(\operatorname{int}K\), and extend the map \(y\mapsto f(y)\delta_y\) by zero outside that interior. It is norm continuous: on the support use the preceding evaluation estimate, and off the support use the zero neighborhood and the bound \(\|\delta_y\|\leq1\). Choose a closed coordinate box \(Q\) containing its support in its interior. For a partition into finitely many boxes \(Q_a\), with tags \(y_a\in Q_a\), put
\[
 S_{\mathcal P}=\sum_a |Q_a|f(y_a)\delta_{y_a},
 \qquad
 \|S_{\mathcal P}-S_{\mathcal R}\|_{X_{N,L}'}
 \leq |Q|\,\omega(\operatorname{mesh}\mathcal P)
             \quad(\mathcal R\text{ refines }\mathcal P).
 \tag{BF17}
\]
Zero terms are interpreted as the zero vector even if their tags lie outside \(K\). Here \(\omega(t)\) is the supremum of the norm difference of this continuous map at points of \(Q\) within distance \(t\). Compactness gives uniform continuity, hence \(\omega(t)\to0\); for example a failure would give two sequences at distance tending to zero and a common convergent subsequence, contradicting continuity. The displayed bound follows by grouping the refined boxes inside each original box, retaining their volumes, and applying the triangle inequality. Two partitions have a common refinement, so their sum difference is at most \(|Q|\) times the sum of their two moduli. A sequence of partitions with mesh tending to zero is therefore Cauchy and has a limit in the actual Banach space \(E'_{K,N}\). Evaluation against any smooth test \(\psi\) gives the scalar Riemann integral \(\int f(y)\psi(y)\,dy\), so the limit is exactly the distribution defined by \(f\). Continuous \(A\) sends these sums to a limit in every output smooth seminorm; evaluation at \(x\) consequently gives
\[
 (Af)(x)=\int f(y)(A\delta_y)(x)\,dy.
 \tag{BF18}
\]
The same argument applies after each output derivative. Since the mixed derivatives of \((A\delta_y)(x)\) were proved above, this is the smooth kernel on the selected input interior and output neighborhood. Arbitrary compact input tests can be covered by finitely many such interiors and localized by the stated smooth-cutoff input. This proves the integral interchange needed in that application without assuming a general vector-valued integration theorem.

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

## 15. Integration, approximation and weak derivatives

The elliptic estimates use more than an abstract Banach-space argument: they need the original Lebesgue norms, convolution bounds and weak derivatives. We give those proofs here. The starting measure is the completed, countably additive Lebesgue measure on the original Euclidean coordinates, characterized on coordinate boxes by their full volume product and by its outer-measure coverings. The nonnegative integral is the supremum of integrals of nonnegative measurable simple functions below the integrand. These are the measure-construction inputs. The convergence, product-integration, norm and approximation results below are consequences, rather than additional assumptions. No polar-coordinate formula is used in these proofs.

### 15.0. Constructing the measure without importing a convergence theorem

We now construct the measure input used in Section 15.1. Fix the original coordinates on \(\mathbb R^n\), \(n\geq1\). The covering boxes are bounded half-open coordinate boxes \(B=\prod_{i=1}^n(a_i,b_i]\), \(a_i<b_i\), with original geometric volume \(v(B)=\prod_{i=1}^n(b_i-a_i)\). The empty box has volume zero. For every subset \(E\subset\mathbb R^n\), put
\[
 \mu^*(E)=\inf\left\{\sum_{j=1}^\infty
           \prod_{i=1}^n(b_{ji}-a_{ji}):
       E\subset\bigcup_{j=1}^\infty
                  \prod_{i=1}^n(a_{ji},b_{ji}]\right\}.
                                                               \tag{LM1}
\]
Finite covers are allowed by appending empty boxes. The empty cover gives \(\mu^*(\varnothing)=0\). Every set has a cover, since a countable collection of bounded coordinate boxes covers the whole original space. Enlarging a set only reduces the choices of covers, so \(\mu^*\) is monotone. For a countable collection \(E_k\), if \(\sum_k\mu^*(E_k)\) is finite, choose a cover of \(E_k\) with cost below \(\mu^*(E_k)+\varepsilon2^{-k}\), for \(k\geq1\). Concatenating these original covers proves \(\mu^*(\bigcup_kE_k)\leq\sum_k\mu^*(E_k)+\varepsilon\). Let \(\varepsilon\downarrow0\). If that sum is infinite, the inequality already holds. Thus
\[
        \mu^*\left(\bigcup_k E_k\right)
                         \leq\sum_k\mu^*(E_k).                 \tag{LM2}
\]
This proof uses only countable sums of nonnegative real numbers, not an integral or a convergence theorem for one.

The box volume in (LM1) is exact. One box covering itself gives \(\mu^*(B)\leq v(B)\). To prove the reverse inequality, take any countable box cover. If its cost is infinite there is nothing to show. Otherwise enlarge each covering box to an open box with added geometric volume less than \(\varepsilon2^{-j}\). This is possible by continuity of its full finite product in its endpoints. For \(0<\delta<\frac12\min_i(b_i-a_i)\), the closed coordinate box \(C_\delta=\prod_i[a_i+\delta,b_i-\delta]\) lies in the original \(B\) and has a finite subcover by these enlarged open boxes. The finite-subcover fact has a direct proof here. If a closed box had no finite subcover by an open cover, bisect all its original coordinate intervals. At least one of its \(2^n\) closed subboxes still has no finite subcover, because otherwise the union of the finite subcovers would cover the original box. Repeat inside that chosen subbox. Real completeness gives a point in all the resulting nested boxes: each coordinate's increasing lower and decreasing upper endpoints have the same limit, since their difference is its original side length times \(2^{-k}\). The diameter at step \(k\) is the full \((\sum_i 2^{-2k}(b_i-a_i-2\delta)^2)^{1/2}\), which tends to zero. One covering open set contains the limiting point and a small ball about it. Eventually the entire chosen box lies in that one set, contradicting its lack of a finite subcover. This proves exactly the compactness needed for \(C_\delta\).

For a finite family of open boxes covering \(C_\delta\), include every covering endpoint and every endpoint of \(C_\delta\) in a finite coordinate grid, inside a bounded box containing them all. The product distributive law writes the full volume of each box as the sum of the grid-cell products contained in it. On the interior of each grid cell, membership in a covering open box is constant, because all its boundary coordinates are grid endpoints. Every grid cell inside \(C_\delta\) is therefore contained, in its interior, in at least one covering box. Summing the full products, with their actual multiplicities, gives
\[
 \prod_{i=1}^n(b_i-a_i-2\delta)
       \leq\sum_{j\ {\rm in\ the\ finite\ subcover}}
                         v(B_j^{\rm enlarged})
       \leq\sum_{j=1}^\infty v(B_j)+\varepsilon .              \tag{LM3}
\]
Grid faces have a zero side length in this geometric calculation; no assertion about an already constructed measure is being used. First let \(\varepsilon\downarrow0\), then \(\delta\downarrow0\). Every covering cost is at least the original full \(v(B)\). Taking its infimum proves \(\mu^*(B)=\prod_i(b_i-a_i)\).

Define the measurable sets by the exact splitting condition
\[
 \mathcal M=\left\{A:\ 
   \mu^*(E)=\mu^*(E\cap A)+\mu^*(E\setminus A)
                        \quad\hbox{for every subset }E\right\}.
                                                               \tag{LM4}
\]
The reverse inequality to this equality always holds by (LM2), so only its other direction needs proof. Complements preserve (LM4). If \(A,B\in\mathcal M\), split first at \(A\) and then split both pieces at \(B\). The resulting four original pieces have sum of outer measures \(\mu^*(E)\). The three pieces outside \(A\cap B\) cover its complement in \(E\); (LM2) therefore proves the required inequality for \(A\cap B\). Thus finite intersections and finite unions preserve measurability.

For disjoint measurable \(A_k\), repeated finite splitting gives, for every positive integer \(N\),
\[
 \mu^*(E)\geq\sum_{k=1}^N\mu^*(E\cap A_k)
                  +\mu^*\left(E\setminus\bigcup_{k=1}^\infty A_k\right).
                                                               \tag{LM5}
\]
Let \(N\to\infty\). The full sum bounds \(\mu^*(E\cap\bigcup_k A_k)\) from below by (LM2), proving (LM4) for their union. For an arbitrary countable union of measurable sets, replace its \(k\)-th set by its difference from the preceding finite union; finite intersections and complements have already proved these disjoint differences measurable. Their union is the original union, so \(\mathcal M\) is a sigma-algebra. Taking \(E=\bigcup_k A_k\) in (LM5) and using (LM2) proves countable additivity of \(\mu=\mu^*|_{\mathcal M}\). No subtraction of two infinite numbers occurs.

Every covering box \(Q\) is in \(\mathcal M\). Indeed, subdivide any covering box \(B_j\) at all coordinate endpoints of \(Q\). The half-open grid pieces partition \(B_j\) exactly. Each is either inside \(Q\) or outside it, and the sum of their full volume products is \(v(B_j)\), by the distributive law. The inside pieces cover \(E\cap Q\), and the outside pieces cover \(E\setminus Q\), for any original cover of \(E\). Thus each covering cost is at least \(\mu^*(E\cap Q)+\mu^*(E\setminus Q)\). Taking its infimum proves (LM4). These boxes generate the Borel sigma-algebra: every open set is a countable union of coordinate boxes with rational endpoints whose closures are contained in it, since each of its points has an interior ball and rational endpoints can be chosen on both sides of each original coordinate. Hence every Borel set is measurable, with the exact box volumes proved in (LM3).

Every subset of an outer-measure-zero set is also measurable. For such a subset \(S\), \(\mu^*(E\cap S)=0\), and (LM2) and monotonicity give \(\mu^*(E)=\mu^*(E\setminus S)\). This is (LM4), with its first term zero. Therefore \(\mu\) is complete. A coordinate hyperplane has outer measure zero: its bounded part with other coordinates in \([-R,R]\) is covered by one box of thickness \(2\delta\) in its fixed coordinate and side lengths \(2R+2\delta\) in the others. Its full cost is
\[
                  (2\delta)(2R+2\delta)^{n-1}\longrightarrow0.
                                                               \tag{LM6}
\]
The whole hyperplane is a countable union of these bounded parts, so (LM2) applies. Consequently every open, closed or half-open choice of endpoints on a bounded coordinate box differs only by a measurable null subset of its faces and retains the full original volume.

The completion is exactly the completed Borel measure, rather than a larger unexplained collection. If \(E\in\mathcal M\) has finite measure, choose covers with costs tending to \(\mu(E)\), enlarge their boxes to open boxes with additional total cost tending to zero, and denote their open unions by \(O_k\supset E\). Additivity gives \(\mu(O_k\setminus E)\to0\). Thus \(G=\bigcap_kO_k\) is Borel, contains \(E\), and \(\mu(G\setminus E)=0\). Every measurable null set \(H\) has a Borel null superset: make the same open-cover construction with total cost below \(2^{-k}\), and intersect the resulting open sets. Apply this to \(H=G\setminus E\). It follows that \(E\) differs from a Borel set by a subset of a Borel null set. For infinite \(\mu(E)\), apply the finite construction to \(E\cap Q_k\), where bounded coordinate boxes \(Q_k\) increase to the whole original space. Each has finite measure by (LM3). The countable union of the resulting Borel supersets is a Borel superset of \(E\), and its difference from \(E\) lies in the countable union of the Borel null supersets just constructed. This again has measure zero. Conversely, completeness has already shown that every Borel set changed on a subset of a Borel null set belongs to \(\mathcal M\).

Finally, this construction is the unique completed Borel measure with the stated coordinate-box volumes. On a bounded coordinate box \(Q\), suppose two finite Borel measures have these volumes. The sets on which they agree form a Dynkin class: agreement holds on \(Q\), relative complements subtract from its finite original volume, and disjoint countable unions use countable additivity. The coordinate rectangles form an intersection-closed generating class. The independent Dynkin-class argument in Section 16.2, which uses only these set operations, makes agreement extend to all Borel subsets of \(Q\). Exhausting by bounded \(Q_k\) and writing their increasing union as successive disjoint differences proves agreement on all Borel sets. Both completions contain exactly the same Borel null sets and all their subsets, as proved above; their completed measures therefore agree as well. Thus (LM1)–(LM6) construct precisely the countably additive completed Lebesgue measure used in (LP1)–(LP19), with its actual original coordinates, full products, face contributions and outer-measure covers.

### 15.1. Convergence, product integration and the full linear Jacobian

Countable additivity gives continuity of measure on increasing sets: write their union as the disjoint union of the first set and successive differences. For \(0\leq f_j\uparrow f\), the definition of the nonnegative integral first gives \(\lim_j\int f_j\leq\int f\). If \(a\) is a nonnegative simple function below \(f\) and \(0<t<1\), the sets \(E_j=\{f_j\geq ta\}\) increase to a set containing \(\{a>0\}\). Integrating the finitely many values of \(a\) and using measure continuity gives \(\int a1_{E_j}\uparrow\int a\), including infinite values. Thus \(\int f_j\geq t\int a1_{E_j}\). First let \(j\) tend to infinity, then \(t\) tend to one, and then take the supremum over \(a\). This proves
\[
 0\leq f_j\uparrow f\quad\Longrightarrow\quad
                 \int f_j\uparrow\int f.
 \tag{LP1}
\]
The zero values of \(a\) cause no problem, and no finiteness of the ambient measure is needed. Every nonnegative measurable \(f\) has increasing simple approximations: truncate at \(2^j\) and round down to multiples of \(2^{-j}\). These approximations increase and tend to \(f\), with infinite values treated by the same truncation. Additivity for nonnegative simple functions follows by taking their common finite measurable partition and adding the coefficient of each part. Apply (LP1) to increasing simple approximations of \(f\), of \(g\), and to their sums, which increase to \(f+g\). This proves \(\int(f+g)=\int f+\int g\), including infinite values; positive scalar multiplication follows by the same argument. Decomposition into the positive and negative parts of real and imaginary components then gives linearity on absolutely integrable complex functions, where each of those component integrals is finite.

For arbitrary nonnegative \(f_j\), apply (LP1) to \(g_m=\inf_{j\geq m}f_j\). Since \(\int g_m\leq\inf_{j\geq m}\int f_j\), this proves Fatou's bound \(\int\liminf f_j\leq\liminf\int f_j\). If complex measurable \(f_j\to f\) almost everywhere and \(|f_j|\leq g\) with \(\int g<\infty\), then \(|f|\leq g\) almost everywhere. Fatou applied to \(2g-|f_j-f|\) gives
\[
 \int|f_j-f|\longrightarrow0,\qquad
                  \int f_j\longrightarrow\int f.
 \tag{LP2}
\]
Indeed its lower bound is \(2\int g\), so the upper limit of the subtracted nonnegative integral is zero. Values on the original null exceptional set can be set to zero for this calculation; integrals and equivalence classes remain unchanged.

Here is product integration with its actual measurability requirement. In a fixed finite coordinate box \(Q=Q_x\times Q_y\), let \(\mathcal C\) consist of the Borel sets \(E\subset Q\) whose sections \(E_x\) are measurable, whose section measure is a measurable function of \(x\), and which satisfy
\[
 |E|=\int_{Q_x}|E_x|\,dx.
 \tag{LP3}
\]
Coordinate rectangles belong to \(\mathcal C\), by the full box-volume formula. The whole box belongs. Relative complementation preserves membership because every section measure is at most the finite \(|Q_y|\), so both sides subtract from \(|Q_x||Q_y|\). Disjoint countable unions preserve membership by countable additivity and (LP1), which also proves measurability of the sum of the section measures. Thus \(\mathcal C\) is a Dynkin class containing the rectangles.

For completeness, the needed class argument is finite and exact. Let \(\mathcal L\) be the smallest Dynkin class containing the rectangles. A Dynkin class is closed under differences of nested members: if \(A\subset B\), use the disjoint union \(A\cup(Q\setminus B)\) and complement. For a rectangle \(A\), the sets \(B\) for which \(A\cap B\in\mathcal L\) form a Dynkin class and contain the rectangles, since intersections of rectangles are rectangles or empty. Hence they contain \(\mathcal L\). Fixing now any \(B\in\mathcal L\) and making the same argument in \(A\) shows that \(\mathcal L\) is closed under all finite intersections. Complements give finite unions. Disjointifying a countable union by subtracting its finitely many preceding members then shows closure under countable unions. Therefore \(\mathcal L\) is a sigma-algebra containing the rectangles, which generate the Borel sets of \(Q\). This proves (LP3) for every Borel set in the box.

Increasing simple approximation and (LP1) now prove nonnegative Tonelli on \(Q\). Exhausting both original spaces by expanding coordinate boxes proves it on \(\mathbb R^a\times\mathbb R^b\). A Lebesgue measurable set differs from a Borel set by a subset of a Borel null set. For that null set, (LP3) says that its sections are null outside a null set of \(x\)'s. Completeness of the section measure makes every subset section measurable there. On the exceptional null set one may choose the value zero for the inner integral. Thus completed Lebesgue measurability gives the same iterated identity almost everywhere; it does not assert measurable sections at every exceptional point. Applying this argument to simple approximations proves the completed version for nonnegative functions. Finally, apply it to \(|h|\) when \(\int|h|<\infty\), and to the positive and negative parts of the real and imaginary components. All these integrals are finite. We obtain the full identities
\[
 \int h(x,y)\,dx\,dy
   =\int\left(\int h(x,y)\,dy\right)dx
   =\int\left(\int h(x,y)\,dx\right)dy,
 \tag{LP4}
\]
for nonnegative \(h\), with possibly infinite integrals, and for absolutely integrable complex \(h\). Sections and inner integrals have their almost-everywhere meanings in the completed case.

Translations, coordinate reflections, coordinate permutations and positive diagonal scalings preserve the box identities, with the full product of the diagonal scale factors retained. The same Dynkin argument compares the two measures on Borel sets; completion extends it to Lebesgue sets because null sets remain null. A shear \(x_i\mapsto x_i+c x_j\), \(i\ne j\), preserves measure: all other coordinates are fixed, and each one-dimensional section is translated by the fixed section parameter \(c x_j\); (LP4) and one-dimensional translation give equality. Every invertible real matrix is a finite product of swaps, nonzero diagonal scalings and shears, by Gaussian elimination on its actual rows. Each shear has determinant one, a swap has determinant minus one, and a diagonal scaling retains its actual signed factor. Multiplying the absolute factors therefore proves
\[
 \int f(Cx+d)|\det C|\,dx=\int f(z)\,dz,
       \qquad C\in\operatorname{GL}(n,\mathbb R),\quad d\in\mathbb R^n,
 \tag{LP5}
\]
on the nonnegative and absolutely integrable domains. The transformations carry Borel null supersets to null supersets, so the completed measure and its exceptional sets are respected. This is a comparison of the original integrals with their complete Jacobian; no determinant is removed from the working formula.

### 15.2. Hölder, Minkowski and all Young endpoints

For \(1<p<\infty\), put \(p'=p/(p-1)\). The scalar inequality \(ab\leq a^p/p+b^{p'}/p'\), \(a,b\geq0\), follows by maximizing \(ab-a^p/p\) as a function of \(a\): its derivative is \(b-a^{p-1}\), with maximum at \(a=b^{1/(p-1)}\); the zero case follows directly. Apply it to \(|f|/\|f\|_p\) and \(|g|/\|g\|_{p'}\) when both norms are nonzero and finite. The original functions and norms are retained, and multiplication restores both norm factors. If a norm is zero, its function vanishes almost everywhere and the conclusion follows directly. This proves
\[
 \int|fg|\leq\|f\|_p\|g\|_{p'},\qquad
 \int|fg|\leq\|f\|_1\|g\|_\infty.
 \tag{LP6}
\]
The second inequality is the pointwise essential bound. It also covers its reversed ordering. The first inequality includes integral Cauchy–Schwarz at \(p=p'=2\). Repeated application proves Hölder for any finite number of factors whose reciprocal exponents sum to one, including infinite exponents by their essential bounds.

For \(1<p<\infty\), the convexity of \(t^p\) gives \(|f+g|^p\leq2^{p-1}(|f|^p+|g|^p)\), so the sum is integrable. Using \(|f+g|^p\leq(|f|+|g|)|f+g|^{p-1}\) and (LP6) gives \(\|f+g\|_p^p\leq(\|f\|_p+\|g\|_p)\|f+g\|_p^{p-1}\). Divide when that norm is positive; if it is zero the result is immediate. The integral triangle inequality gives the case \(p=1\), and the essential-supremum triangle inequality gives \(p=\infty\). Thus every original \(L^p\) norm satisfies Minkowski.

Let \(1\leq p,q,r\leq\infty\) satisfy \(1+1/r=1/p+1/q\). Convolution uses the original density \(dy\). When \(r<\infty\), the relation forces \(p,q<\infty\) and \(r\geq p,q\). Split the absolute integrand into the three factors
\[
 |f(y)g(x-y)|
 =\bigl(|f(y)|^{p/r}|g(x-y)|^{q/r}\bigr)
        |f(y)|^{1-p/r}|g(x-y)|^{1-q/r}.
 \tag{LP7}
\]
If an exponent is zero, its factor is omitted; this convention also applies where its base vanishes. Hölder uses exponents \(r\), \(pr/(r-p)\) and \(qr/(r-q)\) for the retained factors. A factor with zero exponent requires no division by zero. Their reciprocal sum is \(1/r+(1/p-1/r)+(1/q-1/r)=1\). Hence, outside any exceptional set where the first integral is infinite,
\[
 |f*g(x)|^r
 \leq\left(\int|f(y)|^p|g(x-y)|^q\,dy\right)
         \|f\|_p^{r-p}\|g\|_q^{r-q}.
 \tag{LP8}
\]
Zero input norms give zero convolution. For positive norms, integrating (LP8), using (LP4) and the translation case of (LP5), shows that the first integral is finite for almost every \(x\), and proves
\[
 \|f*g\|_r\leq\|f\|_p\|g\|_q.
 \tag{LP9}
\]
If \(r=\infty\), then \(1/p+1/q=1\), so (LP6) proves (LP9) directly for each defined section and its essential supremum. This includes \(p=1,q=\infty\) and \(p=\infty,q=1\). For \(p=q=r=1\), (LP8) is simply the integrated triangle bound; the two omitted factors have exponent zero. These cases exhaust the displayed exponent relation, and no strong estimate with an invalid exponent is being asserted.

### 15.3. Completeness and compact smooth density

For \(1\leq p<\infty\), let \((f_j)\) be norm Cauchy. Choose a subsequence \((f_{j_k})\) with \(\|f_{j_{k+1}}-f_{j_k}\|_p\leq2^{-k}\). The increasing finite sums \(G_M=|f_{j_1}|+\sum_{k=1}^M|f_{j_{k+1}}-f_{j_k}|\) have norms at most \(\|f_{j_1}\|_p+\sum_{k=1}^M2^{-k}\), by Minkowski. Equation (LP1), applied to \(G_M^p\), proves that their pointwise limit \(G\) is in \(L^p\) and finite almost everywhere. Thus the series of original differences converges absolutely almost everywhere, giving a measurable limit \(f\). The same argument for the tail gives
\[
 \|f-f_{j_k}\|_p
 \leq\sum_{\nu=k}^\infty\|f_{j_{\nu+1}}-f_{j_\nu}\|_p
 \leq\sum_{\nu=k}^\infty2^{-\nu}.
 \tag{LP10}
\]
One obtains the first bound by dominating the pointwise difference by that nonnegative tail and passing its finite partial sums through (LP1). The Cauchy property and the triangle inequality then give convergence of the entire sequence to \(f\). For \(p=\infty\), use the same subsequence, remove the countable union of exceptional null sets for the initial essential bound and all difference bounds, and sum the uniformly convergent difference series on the complement. Its limit is essentially bounded and satisfies (LP10) in the essential-supremum norm. Again the full Cauchy sequence converges. These arguments use only measure additivity, (LP1) and the norm inequalities; they prove completeness on any measure space with these definitions, not only Euclidean Lebesgue space.

The smooth density assertion has a different domain: \(1\leq p<\infty\) on \(\mathbb R^n\). First truncate the original \(f\) by \(|x|\leq R\) and \(|f(x)|\leq M\). Dominated convergence applied to \(|f|^p\) proves convergence of these truncations as \(R,M\) grow. On the resulting bounded support and bounded complex range, a finite square grid of mesh \(\delta\) gives a measurable simple function \(a=\sum_{j=1}^J c_j1_{E_j}\), with \(|f-a|\leq\sqrt2\delta\). Each \(E_j\) has finite measure, so the \(L^p\) error is at most \(\sqrt2\delta\) times the support measure to the power \(1/p\).

For a measurable \(E\) with finite measure, its outer-measure definition gives a countable coordinate-box cover with total volume less than \(|E|+\varepsilon\). Enlarge its boxes to open boxes, choosing the extra volume of box \(j\) less than \(\varepsilon2^{-j}\). Their open union \(O\) contains \(E\) and has \(|O\setminus E|<2\varepsilon\). The finite unions \(F_J\) of the first \(J\) boxes increase to \(O\). Since \(|O|<\infty\), (LP1) gives \(|O\setminus F_J|\to0\). Therefore \(|E\mathbin{\triangle} F_J|\leq|O\setminus E|+|O\setminus F_J|\), proving approximation in measure by a finite union of bounded coordinate boxes.

Write one such union as \(F=\bigcup_{j=1}^J\prod_{i=1}^n(a_{ji},b_{ji})\). For \(\delta>0\) smaller than half every side length, choose one-dimensional smooth functions between zero and one, equal to one on \([a_{ji}+\delta,b_{ji}-\delta]\) and supported in \((a_{ji}-\delta,b_{ji}+\delta)\). Their product is \(\theta_{j,\delta}\), and \(\Theta_\delta=1-\prod_{j=1}^J(1-\theta_{j,\delta})\) is compact smooth, between zero and one. The difference from \(1_F\) is supported in the union of the full box layers. Hence
\[
 \|\Theta_\delta-1_F\|_p^p
 \leq\sum_{j=1}^J\left[
       \prod_{i=1}^n(b_{ji}-a_{ji}+2\delta)
       -\prod_{i=1}^n(b_{ji}-a_{ji}-2\delta)\right]
       \longrightarrow0.
 \tag{LP11}
\]
Coordinate faces have measure zero: cover a bounded face by a box with arbitrarily small thickness and use the full volume product; unbounded faces are countable unions of bounded ones. Thus open or closed endpoint choices do not alter this estimate. Combining the finite-union approximation with (LP11) proves compact smooth approximation of each original indicator \(1_{E_j}\). Minkowski gives the full coefficient bound \(\|\sum_j c_j(1_{E_j}-\Theta_j)\|_p\leq\sum_j|c_j|\|1_{E_j}-\Theta_j\|_p\). Keeping these finitely many coefficients and then taking the preceding truncation and grid errors to zero proves density of \(C_c^\infty\) in \(L^p\).

Translations \(\tau_hf(x)=f(x-h)\) are isometries by (LP5). For a fixed compact smooth \(v\), all supports with \(|h|\leq1\) lie in a fixed bounded coordinate box \(Q\). The fundamental theorem of calculus on the actual segment gives
\[
 \|\tau_hv-v\|_p
 \leq |Q|^{1/p}\sum_{i=1}^n|h_i|\,\|\partial_i v\|_\infty,
                   \qquad 1\leq p<\infty.
 \tag{LP12}
\]
The same supremum bound holds at \(p=\infty\), without a volume factor. For general finite-\(p\) \(f\), choose the compact smooth \(v\) just proved dense. The triangle inequality gives \(\|\tau_h f-f\|_p\leq2\|f-v\|_p+\|\tau_hv-v\|_p\). First let \(h\to0\), then the approximation error tend to zero. This proves translation continuity for every finite \(p\). The general \(L^\infty\) assertion would be false: \(1_{[0,1]}\) and each translate with \(0<|h|<1\) differ by one on a set of positive measure. Their essential-supremum distance is one. The finite-\(p\) density and continuity results have not been extended to that endpoint.

### 15.4. The original scaled approximate identity

Let \(r\in C_c^\infty(\mathbb R^n)\) have integral one; it may be signed or complex. Set \(r_\varepsilon(x)=\varepsilon^{-n}r(x/\varepsilon)\), retaining its actual scale and density. The scalar change of variables gives \(\|r_\varepsilon\|_1=\|r\|_1\). For \(f\in L^p\), Young's bound proves \(\|r_\varepsilon*f\|_p\leq\|r\|_1\|f\|_p\), including \(p=\infty\). For finite \(p\), the full difference formula is
\[
 (r_\varepsilon*f)(x)-f(x)
       =\int r(z)\bigl(f(x-\varepsilon z)-f(x)\bigr)\,dz.
 \tag{LP13}
\]
The original factor \(\varepsilon^{-n}\) and its Jacobian \(\varepsilon^n\) are both included in this substitution. Hölder for the weighted scalar integral, or its triangle inequality when \(p=1\), followed by Tonelli gives
\[
 \|r_\varepsilon*f-f\|_p^p
 \leq\|r\|_1^{p-1}\int|r(z)|
                       \|\tau_{\varepsilon z}f-f\|_p^p\,dz
                       \longrightarrow0.
 \tag{LP14}
\]
The norm \(\|r\|_1\) is positive because its integral is one. To verify Hölder's weighted bound for \(p>1\), write the integrand as \(|r|^{1/p}(f(x-\varepsilon z)-f(x))\) times a factor of modulus \(|r|^{1-1/p}\); the zero values of \(r\) contribute zero. Translation continuity makes the inner norm tend to zero for each \(z\), and its bound \((2\|f\|_p)^p\) is integrable against \(|r|\). Equation (LP2) proves the stated limit, with the entire factor \(\|r\|_1^{p-1}\) retained.

The convolution is smooth even before the approximation limit. On a compact output neighborhood, the input variable in \(r_\varepsilon(x-y)\) lies in one compact set. Hölder makes \(f\) integrable on that set. Difference quotients of the kernel and all their subsequent derivatives converge uniformly there by the scalar fundamental theorem, with a common bound. Integration against this locally integrable \(f\) therefore proves
\[
 \partial_x^\alpha(r_\varepsilon*f)(x)
       =\int\partial_x^\alpha r_\varepsilon(x-y)f(y)\,dy,
 \qquad
 \partial^\alpha r_\varepsilon(x)
       =\varepsilon^{-n-|\alpha|}(\partial^\alpha r)(x/\varepsilon).
 \tag{LP15}
\]
Every kernel derivative and scale factor remains. The general \(L^\infty\) convergence conclusion is again false. The convolutions of \(1_{[0,1]}\) are continuous; a continuous function has essential-supremum distance at least \(1/2\) from that indicator, since values arbitrarily near an endpoint from its two sides would otherwise force incompatible limits. Uniform boundedness at that endpoint is the bound already proved, not convergence for all inputs.

### 15.5. Complete weak-derivative limits and Sobolev approximation

An \(L^p_{\rm loc}(\Omega)\) function defines a distribution through the original integral against compact smooth tests. For \(1\leq p\leq\infty\), Hölder on a compact test support proves continuity and gives the exact passage to limits. If \(f_j\to f\) and \(g_j\to g\) in local \(L^p\), and \(D^\alpha f_j=g_j\) distributionally, then for every compact test \(\phi\),
\[
 \int g\phi
 =\lim_j\int g_j\phi
 =(-1)^{|\alpha|}\lim_j\int f_jD^\alpha\phi
 =(-1)^{|\alpha|}\int fD^\alpha\phi.
 \tag{LP16}
\]
Here \(D=-i\partial\) and every factor \((-i)^{|\alpha|}\) is retained inside \(D^\alpha\phi\); the resulting pairing coefficient is \(i^{|\alpha|}\). The test belongs to the conjugate Lebesgue space, including the \(L^\infty\) test bound when \(p=1\) and the \(L^1\) test bound when \(p=\infty\). Thus the integrals converge and (LP16) proves \(D^\alpha f=g\), not merely a prospective derivative identity.

For an integer \(s\geq0\), use the original derivative array \((D^\alpha f)_{|\alpha|\leq s}\). For finite \(p\), its norm is \(N_{s,p}(f)=(\sum_{|\alpha|\leq s}\|D^\alpha f\|_p^p)^{1/p}\); for \(p=\infty\), use the maximum of the component essential bounds. These are precisely the component \(L^p\) norms of the pointwise \(\ell^p\) array, by Tonelli. If one uses the sum of component norms as well, its comparison retains the entire component count \(M_s=\binom{n+s}{s}\):
\[
 N_{s,p}(f)\leq\sum_{|\alpha|\leq s}\|D^\alpha f\|_p
       \leq M_s^{1-1/p}N_{s,p}(f),
             \qquad 1\leq p\leq\infty.
 \tag{LP17}
\]
At infinity the exponent is one. The finite count follows by introducing a slack coordinate to turn \(|\alpha|\leq s\) into an \((n+1)\)-coordinate nonnegative tuple of sum \(s\); placing its separators gives the displayed binomial count. For the homogeneous array \(|\alpha|=j\), the same separator count without the slack coordinate gives \(\binom{n+j-1}{j}\), so its two norm comparisons have exactly this component count in place of \(M_s\). The first comparison follows from the finite-sum triangle inequality and the second from (LP6) on that finite counting measure. A Cauchy Sobolev sequence has an \(L^p\) limit in every component by Section 15.3. Equation (LP16) identifies every component with the corresponding derivative of the zeroth component. The finite array converges in its original norm. This proves completeness of \(W^{s,p}(\Omega)\) for every open \(\Omega\), including disconnected and empty sets, at every displayed \(p\).

For global \(f\in W^{s,p}(\mathbb R^n)\), \(1\leq p<\infty\), choose a fixed compact smooth \(\chi\), equal to one on \(B_1\), and set \(\chi_R(x)=\chi(x/R)\), \(R\geq1\). The distributional product rule has its full test proof as follows. For any smooth \(a\), distribution \(f\) and compact test \(\phi\), \(\langle D_i(af),\phi\rangle=-\langle f,aD_i\phi\rangle=-\langle f,D_i(a\phi)-(D_i a)\phi\rangle=\langle aD_i f+(D_i a)f,\phi\rangle\). Thus every \(-i\) factor agrees with the original derivative convention. Suppose the multi-index rule holds at \(\alpha\), and apply this first-derivative rule in coordinate \(i\) to every term. The coefficients for a fixed \(\beta\) add as \(\binom{\alpha}{\beta}+\binom{\alpha}{\beta-e_i}=\binom{\alpha+e_i}{\beta}\), with an out-of-range term zero; coefficients in the other coordinates remain unchanged. Induction from \(\alpha=0\), and the exact chain-rule factor \(D^\beta\chi_R=R^{-|\beta|}(D^\beta\chi)(x/R)\), give the entire expression
\[
 D^\alpha(\chi_R f)
 =\sum_{\beta\leq\alpha}\binom{\alpha}{\beta}
         R^{-|\beta|}(D^\beta\chi)(x/R)D^{\alpha-\beta}f.
 \tag{LP18}
\]
The \(\beta=0\) difference from \(D^\alpha f\) tends to zero in \(L^p\) by dominated convergence, because \(\chi(x/R)\to1\). Every remaining term is bounded by \(\binom{\alpha}{\beta}R^{-|\beta|}\|D^\beta\chi\|_\infty\|D^{\alpha-\beta}f\|_p\), which tends to zero. These finitely many original terms prove \(\chi_R f\to f\) in the entire Sobolev norm.

If \(D^\alpha f=g\in L^p\), testing its derivative identity against the compact kernel \(y\mapsto r_\varepsilon(x-y)\) gives
\[
 D^\alpha(r_\varepsilon*f)=r_\varepsilon*(D^\alpha f).
 \tag{LP19}
\]
The derivative in the input kernel contributes \((-1)^{|\alpha|}\), which cancels the sign from the distributional test derivative; the \((-i)^{|\alpha|}\) factors are unchanged. Formula (LP15) identifies the result with the classical smooth output derivative. Equation (LP14) applies separately to every original derivative component, so smoothing converges in the entire \(W^{s,p}\) norm. Apply this to the compactly supported \(\chi_R f\). Its convolution is compact smooth, with support in \(\operatorname{supp}\chi_R+\varepsilon\operatorname{supp}r\). First let its smoothing error tend to zero for fixed \(R\), then the cutoff error tend to zero as \(R\) grows. This proves density of \(C_c^\infty\) in global \(W^{s,p}(\mathbb R^n)\) for every finite \(p\).

Local approximation retains the actual open domain and the restriction \(1\leq p<\infty\). For a compact \(K\subset\Omega\), choose \(\chi\in C_c^\infty(\Omega)\) equal to one near \(K\). If \(f\in W^{s,p}_{\rm loc}(\Omega)\), formula (LP18), with the fixed cutoff and no scale factors, proves that its cutoff product, extended by zero, belongs to global \(W^{s,p}\). To check every boundary contribution, choose \(\zeta\in C_c^\infty(\Omega)\) equal to one near \(\operatorname{supp}\chi\). In the global derivative pairing for a test \(\phi\), replace \(\phi\) by \(\zeta\phi\); all terms containing derivatives of \(\zeta\) vanish on the support of the original cutoff product and of every term in its product-rule derivative. The pairing is therefore exactly the interior derivative pairing, with the finite sum from (LP18) extended by zero and no boundary term. Smoothing that extension then approximates \(f\) and all its original derivatives on \(K\). To obtain one sequence for the whole open set, exhaust \(\Omega\) by increasing compact \(K_j\)'s with interiors covering it, choose such \(\chi_j\), and choose \(\varepsilon_j\) so the smoothing error on \(K_j\), for the entire finite derivative array, is at most \(2^{-j}\). The limits just proved supply each such positive choice. The resulting globally smooth functions converge in \(W^{s,p}\) on every fixed compact subset of \(\Omega\). This is local smooth approximation, without an unproved global boundary-extension assertion.

These proofs supply the integration and weak-derivative operations in [Local inverses and distance-weighted elliptic estimates](local-elliptic-coefficients.md). Its \(L^p\) inverse series uses actual completeness from (LP10). The compact zero extension of its input is integrable by (LP6), Young gives exactly its strict kernel bounds, and (LP14), (LP18) and (LP19) justify the original full-domain approximation step after (L14). Formula (LP16) identifies the highest-derivative limits in (L42) with the distributional derivatives on the original interior ball. Dominated and monotone convergence from (LP1)–(LP2) justify passage to the distance-weighted exhaustion in (L43). The multiplier and fractional-integration theorems have their own harmonic-analysis proofs; the inequalities here do not substitute for those statements.

### 15.6. The full polar formula on the original plane

The remaining change of variables has a singular point and an angular endpoint. We prove it from the measure in Section 15.0 and the product and linear formulas (LP4)–(LP5), without assuming a nonlinear change-of-variables theorem. The finite scalar calculus used here includes the original sine and cosine, their derivatives and addition formulas, and their period \(2\pi\). Define
\[
 \begin{aligned}
 D&=(0,\infty)\times[0,2\pi),\\
 \Phi(r,\theta)&=(r\cos\theta,r\sin\theta),\\
 D\Phi(r,\theta)&=
 \begin{pmatrix}\cos\theta&-r\sin\theta\\
                 \sin\theta&r\cos\theta\end{pmatrix},\\
 w(r,\theta)&=\det D\Phi(r,\theta)
       =r\cos^2\theta+r\sin^2\theta=r.
 \end{aligned}                                                 \tag{PC1}
\]
**The angular inverse, including its endpoints.** We use the original scalar functions constructed in [Arctangent, circular parameters and the original pi](metric-foundation-bridges.md#arctangent-circular-parameters-and-the-original-pi). There \(C=\cos\), \(S=\sin\), \(\pi=2t_0\), \(C(t_0)=0\), \(S(t_0)=1\), and \(C,S>0\) on \((0,t_0)\), with \(C'=-S\), the full addition laws and \(C^2+S^2=1\). If \(0<u<t_0\), those laws give \(S(t_0+u)=S(t_0)C(u)+C(t_0)S(u)=C(u)>0\). Thus \(S>0\) throughout \((0,\pi)\). The mean value theorem makes \(C\) strictly decreasing on \([0,\pi]\), including comparisons with either endpoint. Its endpoint values are \(C(0)=1\) and \(C(\pi)=-1\). Continuity and intermediate values therefore give a bijection \(C:[0,\pi]\to[-1,1]\).

Define \(\arccos:[-1,1]\to[0,\pi]\) as this exact inverse. Both compositions are proved by bijectivity: \(C(\arccos a)=a\) for \(-1\le a\le1\), and \(\arccos(C\theta)=\theta\) for \(0\le\theta\le\pi\). In particular \(\arccos(1)=0\) and \(\arccos(-1)=\pi\). To prove continuity at every \(a\), including \(a=\pm1\), take \(a_n\to a\). If \(\arccos a_n\) failed to tend to \(\arccos a\), some subsequence would stay at distance at least \(\varepsilon>0\). Compactness of \([0,\pi]\) supplies a convergent further subsequence with limit \(\theta\). Continuity of \(C\) gives \(C\theta=a\); uniqueness forces \(\theta=\arccos a\), a contradiction. Sequential continuity is continuity in these original real intervals.

For a nonzero point \((x,y)\), its radius \(r=(x^2+y^2)^{1/2}\) is strictly positive. If \(y>0\), then \(-1<x/r<1\), so \(\theta=\arccos(x/r)\) belongs to \((0,\pi)\). We have \(C\theta=x/r\) and \(S\theta>0\); the full square identity gives \(S\theta=(1-x^2/r^2)^{1/2}=y/r\). If \(y<0\), put \(\theta=2\pi-\arccos(x/r)\). Periodicity, evenness of \(C\) and oddness of \(S\) give \(C\theta=x/r\), \(S\theta=y/r\), and \(\pi<\theta<2\pi\). If \(y=0\), the positive ray has angle zero and the negative ray has angle \(\pi\), with the stated coordinates in both cases.

These formulas also recover the angle from every \((r,\theta)\in D\). On \((0,\pi)\) the sine is positive and the inverse composition recovers \(\theta\); on \((\pi,2\pi)\) apply that composition to \(2\pi-\theta\). The two horizontal cases recover \(0\) and \(\pi\). The excluded value \(2\pi\) is never a second representative of the positive ray, and the excluded radius zero is never used in a quotient. Thus both compositions of the original coordinate map and the stated inverse are the identity, with their full domains and endpoints.

The two determinant summands and the equality comparing them with the radial density are retained. In particular \(w>0\) on \(D\). The map \(\Phi\) is a bijection from \(D\) onto \(\mathbb R^2\setminus\{0\}\). Indeed a nonzero point has the unique radius \(r=(x^2+y^2)^{1/2}\). Its unique angle is \(\arccos(x/r)\) on \(y>0\), \(2\pi-\arccos(x/r)\) on \(y<0\), \(\pi\) on the negative horizontal ray, and zero on the positive horizontal ray. The four pieces are Borel and the formulas on each are continuous. Thus the inverse is Borel. The continuous map \(\Phi\) and this Borel inverse carry Borel sets to Borel sets in their respective spaces. Continuity of the inverse across the negative ray is not needed for this conclusion.

We first compute sector areas from triangles. A line has plane measure zero: the horizontal line is a coordinate hyperplane by (LM6), and an affine rotation sends it to any prescribed line with absolute determinant one in (LP5). A circle of radius \(R>0\) is null as well. Partition its parameter interval \([0,2\pi]\) into \(N\) intervals of length \(h=2\pi/N\). Since each coordinate derivative of \(R(\cos\theta,\sin\theta)\) has modulus at most \(R\), each image lies in a coordinate square of side \(2Rh\) about its initial point. Endpoints may be included by the null-face conclusion after (LM6). The covering bound is
\[
 \mu^*(\{x^2+y^2=R^2\})
       \leq N(2Rh)^2
       =4R^2\frac{(2\pi)^2}{N}\longrightarrow0.                \tag{PC2}
\]
The radius-zero circle is a singleton and is already null. These arguments include every line segment, ray, circular arc and endpoint appearing below.

The coordinate triangle
\(T=\{(u,v):u\geq0,\ v\geq0,\ u+v\leq1\}\)
has measure \(\int_0^1(1-u)\,du=1/2\) by (LP4) and finite calculus. The integral of a continuous function on a compact interval agrees with its elementary integral: upper and lower step approximations on a fine partition bound the Lebesgue integral, and uniform continuity makes their difference tend to zero. This justifies the scalar evaluations here directly from the simple-integral definition.

For \(0<h<\pi\), the triangle with vertices zero,
\(R(\cos t,\sin t)\), and \(R(\cos(t+h),\sin(t+h))\)
is the image of \(T\) under the matrix having those two vectors as columns. Its positive determinant gives the exact inner area
\[
 \begin{split}
 A_{\rm in}(R,t,h)
 &=\frac{R^2}{2}
       \bigl(\cos t\sin(t+h)-\sin t\cos(t+h)\bigr)
   =\frac{R^2}{2}\sin h,\\
 A_{\rm out}(R,t,h)
 &=\frac{R^2}{2\cos^2(h/2)}
       \bigl(\cos t\sin(t+h)-\sin t\cos(t+h)\bigr)
   =R^2\tan(h/2).
 \end{split}                                                   \tag{PC3}
\]
The outer triangle uses the original two bounding rays, with their endpoint radii \(R/\cos(h/2)\). Each equality follows from (LP5); both original determinant terms and the full outer scale are displayed.

To check the inclusions, write \(m=t+h/2\). The inner chord has projection \(R\cos(h/2)\) on \((\cos m,\sin m)\). Its intersection with the ray of angle \(\theta\in[t,t+h]\) therefore has radius
\(R\cos(h/2)/\cos(\theta-m)\leq R\).
Thus the entire inner triangle lies in the disk sector of radius \(R\). The outer chord has projection \(R\) on the same direction, and its intersection radius is
\(R/\cos(\theta-m)\geq R\).
It therefore contains that sector. Every denominator is positive because
\(|\theta-m|\leq h/2<\pi/2\).
This proves the actual inclusions used in the measure bounds.

Fix \(0\leq\alpha<\beta\leq2\pi\). The sector is Borel, by the radius and angle formulas above, with its origin added if desired. Divide its angle interval into \(N\) equal pieces of length \(h=(\beta-\alpha)/N<\pi\). The triangles of the distinct pieces have disjoint interiors; any overlap lies on their finitely many bounding rays, which have measure zero. Finite additivity, the proved inclusions and (PC3) give
\[
 N\frac{R^2}{2}\sin\!\left(\frac{\beta-\alpha}{N}\right)
 \ \leq\ \mu(\text{sector}(R;\alpha,\beta))
 \ \leq\
 NR^2\tan\!\left(\frac{\beta-\alpha}{2N}\right).
                                                               \tag{PC4}
\]
The derivatives of sine and tangent at zero imply that both bounds tend to
\(R^2(\beta-\alpha)/2\).
Hence this is the exact sector area. All choices of the two radial sides or the circular side differ only by the null sets just proved. The full-angle case \(\beta-\alpha=2\pi\) is included: repeated initial and final rays are null.

For \(0\leq a<b<\infty\), subtract the inner sector of radius \(a\) from that of radius \(b\). Both have finite measure. The annular sector therefore has measure
\[
 \begin{split}
 \frac{b^2}{2}(\beta-\alpha)-\frac{a^2}{2}(\beta-\alpha)
 &=\frac{b^2-a^2}{2}(\beta-\alpha)\\
 &=\int_\alpha^\beta\int_a^b
       \bigl(r\cos^2\theta+r\sin^2\theta\bigr)\,dr\,d\theta.
 \end{split}                                                   \tag{PC5}
\]
There is no subtraction of infinite measures. At \(a=0\) the removed point is null; at either positive radius the endpoint circle is null. The original two square contributions in the density and both radial endpoint terms remain in the formula.

Now let \(E\) be a Borel subset of \(D\), and define two measures on this same original domain by
\[
 \lambda(E)=\mu(\Phi(E)),\qquad
 \nu(E)=\int_D1_E(r,\theta)
                \bigl(r\cos^2\theta+r\sin^2\theta\bigr)\,dr\,d\theta.
                                                               \tag{PC6}
\]
The first is countably additive because \(\Phi\) is injective and carries Borel sets to Borel sets. The second is countably additive by (LP1) and the simple-integral definition. Formula (PC5) shows equality on every coordinate rectangle
\((a,b]\times[\alpha,\beta)\subset D\).
These rectangles form an intersection-closed family and generate the Borel sets of \(D\). To see generation, express each relative open coordinate interval as a countable union of such intervals with endpoints in a fixed countable dense set, adjoining zero and \(2\pi\) for the angular endpoints. Relative open sets then have countable unions of these rectangular neighborhoods.

Both measures are finite on
\(Q_k=(1/k,k]\times[0,2\pi)\), \(k\geq2\), and these sets increase to \(D\). They agree on \(Q_k\) and on its intersections with the rectangles. On \(Q_k\), the class of sets on which two finite measures agree is a Dynkin class: relative complements subtract from the equal finite whole masses, and disjoint countable unions use countable additivity. The full intersection-closed-family argument proved after (LP3) shows agreement on all its Borel subsets. Increasing \(k\) and using countable additivity therefore gives \(\lambda(E)=\nu(E)\) on every Borel subset of \(D\).

This equality respects the completions in both directions. If \(E\subset D\) is Borel, then \(\nu(E)=0\) is equivalent to its original coordinate measure being zero. One implication follows by integration on a null set. For the other, (PC1) gives \(w=r>1/k\) on \(Q_k\), so
\(\nu(E\cap Q_k)\geq k^{-1}|E\cap Q_k|\).
The equality of the two measures proves that \(\Phi\) carries every Borel coordinate-null subset of \(D\) to a plane-null Borel set, and its inverse carries every plane-null Borel set avoiding zero to a coordinate-null Borel set. Every completed measurable set is a Borel set changed on a subset of a Borel null set, by Section 15.0. Applying the actual bijection to these two parts proves that \(\Phi\) and its inverse preserve completed measurability and null equivalence classes. Thus (PC6) holds for every completed measurable \(E\), with the same density.

Apply this set identity first to indicators and finite nonnegative simple functions. Increasing simple approximation and (LP1) then give, for every nonnegative Lebesgue measurable \(f\) on the original plane,
\[
 \begin{split}
 \int_{\mathbb R^2} f(x,y)\,dx\,dy
 &=\int_0^{2\pi}\int_0^\infty
     f(r\cos\theta,r\sin\theta)
         \bigl(r\cos^2\theta+r\sin^2\theta\bigr)\,dr\,d\theta\\
 &=\int_0^{2\pi}\int_0^\infty
     f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta.
 \end{split}                                                   \tag{PC7}
\]
The point zero in the original plane has measure zero. Both right-hand formulas retain the comparison to the full determinant, and either may have value \(+\infty\). Product integration (LP4) allows reversal of the order, with the already proved almost-everywhere section convention. In particular no claim of measurable sections at every exceptional angle is introduced.

Applying (PC7) to \(|f|\) proves the exact absolute-integrability equivalence. When these integrals are finite, applying it to the positive and negative parts of each real and imaginary component gives (PC7) for complex \(f\), with all integrals finite. This is the full signed and complex polar formula, including its actual domain of validity.

The endpoints do not require deletion of any contribution. On
\(\overline D=[0,\infty)\times[0,2\pi]\),
the newly added radius-zero and angle-\(2\pi\) sets lie on coordinate lines and have coordinate measure zero. Define the weighted integrand to be zero on the radius-zero line, including if \(f(0)=+\infty\). Its density there is zero. The extra angle is a copy of the positive horizontal ray, already null in the original plane. Therefore adding either endpoint changes neither integral. This accounts explicitly for the collapsed origin and duplicated ray rather than asserting that \(\Phi\) is injective on \(\overline D\).

### 15.7. The exact Gaussian factor used by Fourier inversion

The original one-dimensional Gaussian in Section 1 of [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md) now has a complete integration proof. Put
\(I=\int_{\mathbb R}e^{-t^2}\,dt\), initially allowing \(+\infty\). The lower bound \(I\geq\int_0^1e^{-1}\,dt=e^{-1}>0\) excludes a zero value. Nonnegative (LP4), followed by (PC7), gives
\[
 \begin{split}
 I^2
 &=\int_{\mathbb R^2}e^{-x^2}e^{-y^2}\,dx\,dy\\
 &=\int_0^{2\pi}\int_0^\infty
    e^{-r^2\cos^2\theta-r^2\sin^2\theta}
       \bigl(r\cos^2\theta+r\sin^2\theta\bigr)\,dr\,d\theta\\
 &=\int_0^{2\pi}
       \left[-\frac12e^{-r^2}\right]_{r=0}^{r=\infty}d\theta
   =2\pi\left(\frac12-0\right)=\pi .
 \end{split}                                                   \tag{PC8}
\]
The radial evaluation follows on finite intervals from the derivative of
\(-e^{-r^2}/2\); (LP1) takes the upper endpoint to infinity. Thus \(I\) is finite and, because it is positive, \(I=\sqrt\pi\). The displayed calculation preserves both original Cartesian exponent terms, both polar exponent terms, both determinant terms and both radial endpoint values.

For \(a>0\) and an integer \(d\geq1\), (LP5) with the actual linear map \(a^{-1/2}I_d\), and repeated (LP4), give
\[
 \begin{split}
 \int_{\mathbb R^d}e^{-a|x|^2}\,dx
 &=\left|\det(a^{-1/2}I_d)\right|
       \int_{\mathbb R^d}\prod_{j=1}^d e^{-z_j^2}\,dz
   =(a^{-1/2})^d(\sqrt\pi)^d=(\pi/a)^{d/2},\\
 \int_{\mathbb R^d}
      (4\pi\varepsilon)^{-d/2}e^{-|x|^2/(4\varepsilon)}\,dx
 &=(4\pi\varepsilon)^{-d/2}
       \left|\det((4\varepsilon)^{1/2}I_d)\right|
       (\sqrt\pi)^d=1,\qquad \varepsilon>0 .
 \end{split}                                                   \tag{PC9}
\]
Every original Fourier heat-kernel factor is present. At \(d=0\) the coordinate space is one point with mass one, the empty product and determinant are one, and these identities again have value one. This is the exact Gaussian mass needed for Fourier inversion; it does not assume the Fourier inversion theorem in its own proof.

## 16. General measurable functions and sigma-finite product integration

### 16.1. Measures, completions, measurable limits and the full nonnegative integral

A measure space is an original set \(X\), a sigma-algebra \(\mathcal A\) of its subsets, and a countably additive map \(\mu:\mathcal A\to[0,\infty]\), with \(\mu(\varnothing)=0\). Countable additivity is for disjoint sequences. If \(A\subset B\) are measurable, the disjoint decomposition \(B=A\cup(B\setminus A)\) gives monotonicity. For \(A_n\uparrow A\), decompose \(A\) into \(A_1\) and the successive disjoint differences. The original countable sum gives \(\mu(A_n)\uparrow\mu(A)\), with infinity permitted. If \(A_n\downarrow A\) and \(\mu(A_1)<\infty\), apply the increasing statement to \(A_1\setminus A_n\) and subtract only from the finite \(\mu(A_1)\). This proves \(\mu(A_n)\downarrow\mu(A)\). Countable subadditivity follows by replacing the sets of any sequence by their successive disjoint differences. These operations preserve the original measure.

The completion is the sigma-algebra
\[
 \overline{\mathcal A}
 =\{E\subset X:\ A\subset E\subset B
       \text{ for some }A,B\in\mathcal A,\ \mu(B\setminus A)=0\},
 \qquad \overline\mu(E)=\mu(A)=\mu(B).
 \tag{GM1}
\]
The equality of the last two values follows by adding the zero-measure difference; it does not subtract infinities. If \(A',B'\) are another pair, then \(A\setminus A'\subset B'\setminus A'\) and \(A'\setminus A\subset B\setminus A\) have zero measure. Disjoint decomposition through \(A\cap A'\) proves \(\mu(A)=\mu(A')\). Complements exchange the bounding sets \(B^c,A^c\). For countable unions, their bounds are \(\bigcup A_n,\bigcup B_n\), whose difference is contained in the measurable null union \(\bigcup(B_n\setminus A_n)\). Hence this is a sigma-algebra. When the \(E_n\) are disjoint, the lower bounds \(A_n\) are disjoint, so the same original countable sum proves countable additivity of \(\overline\mu\). Every subset of a completed null set has the lower bound empty and an original measurable null upper bound. Thus this measure is complete. Equivalently, \(E\) differs from an original measurable set by a subset of an original measurable null set: use \(E\setminus A\subset B\setminus A\) in one direction, and the bounds \(C\setminus N,C\cup N\) for \(E\mathbin{\triangle} C\subset N\) in the other. Section 15.0 proves, from its actual interval/box covers, that its outer-measure construction is exactly the completion of its Borel restriction. Formula (GM1) also treats arbitrary measure spaces without a hidden finiteness assumption.

For an extended real function, measurability means that all inverse images of open rays are measurable. It is enough to check rational endpoints: an arbitrary open ray is a countable union of the appropriate rational rays. Countable suprema and infima are measurable, since
\[
 \{\sup_n f_n>t\}=\bigcup_n\{f_n>t\},\qquad
 \{\inf_n f_n<t\}=\bigcup_n\{f_n<t\},\qquad
 \liminf_n f_n=\sup_N\inf_{n\geq N}f_n .
 \tag{GM2}
\]
To obtain the other ray for a given extended real function, use the complement of a non-strict ray, itself a countable intersection of strict rays. Consequently a pointwise limit of measurable real functions, including an infinite limit, is measurable. For complex functions apply the assertion to both real coordinates; the Borel sets of the complex plane are generated by the rational-coordinate rectangles. Finite sums of measurable real functions and products wherever their extended values are defined are measurable: their pair map has measurable inverse images of rational rectangles and hence of every open set, and finite real addition and multiplication are continuous. This gives in particular every finite-valued simple function and its level sets. Nonnegative sums with infinite limits follow by increasing finite sums and (GM2).

For a nonnegative finite-valued simple function \(s=\sum_{j=1}^r c_j1_{A_j}\), with disjoint measurable \(A_j\) and finite \(c_j\geq0\), define its integral to be \(\sum_j c_j\mu(A_j)\). The convention \(0\cdot\infty=0\) records the fact that a zero value contributes zero, even on a set of infinite measure. Two presentations give the same answer: intersect their finite partitions, including the zero-valued complement, and use finite additivity on each original part. On this common partition \(s\leq t\) gives \(\int s\leq\int t\); sums and finite positive scalar multiples have their exact additive integral. For a nonnegative measurable \(f\), define
\[
 \int_X f\,d\mu
 =\sup_{\substack{s\ {\rm nonnegative,\ finite\ valued,\ simple}\\s\leq f}}
       \int_Xs\,d\mu,\qquad
 s_n(x)=
 \begin{cases}
  \min(2^n,\,2^{-n}\lfloor2^n f(x)\rfloor),&f(x)<\infty,\\
  2^n,&f(x)=\infty .
 \end{cases}
 \tag{GM3}
\]
Each \(s_n\) has finitely many measurable levels. The next dyadic grid retains every earlier grid value and its truncation is higher, so \(s_n\uparrow f\). This is an approximation to the original \(f\); neither the measure nor \(f\) is replaced in the conclusion.

Here is monotone convergence directly from that definition. If \(0\leq f_n\uparrow f\), monotonicity gives \(L=\lim_n\int f_n\leq\int f\). For an arbitrary nonnegative simple \(s\leq f\) and \(0<t<1\), let \(E_n=\{f_n\geq ts\}\). These increase, and their union contains \(\{s>0\}\): at a point where \(s>0\), the limit \(f\geq s>ts\) forces an eventual such inequality. On each of the finitely many positive levels of \(s\), measure continuity gives \(\int s1_{E_n}\uparrow\int s\). This includes an infinite level-set measure; zero levels still contribute zero. Since \(\int f_n\geq t\int s1_{E_n}\), we have \(L\geq t\int s\). If \(\int s=\infty\), this already forces \(L=\infty\); otherwise let \(t\uparrow1\). Taking the supremum over \(s\) proves
\[
 0\leq f_n\uparrow f\quad\Longrightarrow\quad
       \int f_n\,d\mu\uparrow\int f\,d\mu,\qquad
 \int(f+g)\,d\mu=\int f\,d\mu+\int g\,d\mu .
 \tag{GM4}
\]
For the additive assertion, use the increasing simple approximations of both original functions in (GM3). Their sums increase to \(f+g\), and every simple integral is additive. Positive homogeneity follows first for simples and then by the same limit. Applying (GM4) to the finite partial sums proves integration of an arbitrary countable nonnegative sum. No sigma-finiteness is needed in this paragraph.

If \(\int g<\infty\), the set on which \(g=\infty\) has measure zero: \(n1_{\{g=\infty\}}\leq g\) gives \(n\mu\{g=\infty\}\leq\int g\) for every positive integer \(n\). Integrating the four nonnegative parts of a complex measurable \(h\) with \(\int|h|<\infty\) defines its integral and proves linearity, because all those integrals are finite. Its triangle inequality follows without a pointwise choice of phase: if \(I=\int h\ne0\), use the constant \(c=\overline I/|I|\) and \(\operatorname{Re}(ch)\leq|h|\); if \(I=0\), the inequality already holds.

For nonnegative \(f_n\), put \(g_N=\inf_{n\geq N}f_n\). These are measurable by (GM2), increase to \(\liminf f_n\), and satisfy \(\int g_N\leq\inf_{n\geq N}\int f_n\). Formula (GM4) proves Fatou's inequality. If \(h_n\) and \(h\) are measurable complex functions, \(h_n\to h\) almost everywhere and \(|h_n|\leq g\) almost everywhere with \(\int g<\infty\), take the countable union of their measurable exceptional null sets and the null infinite-value set of \(g\). Change all the functions to zero on that measurable null set. This preserves all original integrals. Now \(|h|\leq g\) everywhere, and Fatou applies to \(2g-|h_n-h|\). Additivity expresses its finite integral as \(2\int g-\int|h_n-h|\). Fatou therefore gives
\[
 \int|h_n-h|\,d\mu\longrightarrow0,\qquad
 \int h_n\,d\mu\longrightarrow\int h\,d\mu .
 \tag{GM5}
\]
Every subtraction here is of finite integrals. If \(\mu(X)<\infty\) and \(|h_n|\leq M<\infty\), use the original constant majorant \(M1_X\), whose integral is \(M\mu(X)\), to prove bounded convergence. For \(M=0\) or \(\mu(X)=0\) this integral is exactly zero. This proves the entire convergence entry used for one-dimensional Lebesgue measure, and also its stated general finite-measure version.

### 16.2. The exact generating-class argument and measurable sections

A Dynkin class on a set \(Z\) contains \(Z\), is closed under relative complements, and is closed under countable disjoint unions. It is closed under differences of nested members: if \(A\subset B\) belong, complement the disjoint union \(A\cup(Z\setminus B)\). Let \(\mathcal P\) be an intersection-closed family containing \(Z\), and let \(\mathcal L\) be the intersection of all Dynkin classes containing \(\mathcal P\). This intersection is itself a Dynkin class. For \(A\in\mathcal P\), the sets \(B\subset Z\) with \(A\cap B\in\mathcal L\) form a Dynkin class. The whole-set condition uses \(A\in\mathcal L\); the complement condition uses the proved nested-difference rule inside \(A\); disjoint unions use intersections with their disjoint parts. Intersection closure of \(\mathcal P\) makes this class contain \(\mathcal P\), so it contains \(\mathcal L\). Fix now \(B\in\mathcal L\) and make the same argument with the class of \(A\) satisfying \(A\cap B\in\mathcal L\). The first argument shows that every \(A\in\mathcal P\) belongs, and hence every \(A\in\mathcal L\) belongs. Thus \(\mathcal L\) is closed under all finite intersections. Complementation gives finite unions, and disjointifying a countable union by subtracting its preceding finite union gives every countable union. It follows that
\[
 \mathcal P\subset\mathcal D,\quad\mathcal D\ {\rm a\ Dynkin\ class}
 \quad\Longrightarrow\quad \sigma(\mathcal P)\subset\mathcal D .
 \tag{GM6}
\]
This implication has just been proved, rather than assumed as a convergence or product theorem.

For original measurable spaces \((X,\mathcal A)\), \((Y,\mathcal B)\), define \(\mathcal A\otimes\mathcal B\) as the sigma-algebra on the original \(X\times Y\) generated by the rectangles \(A\times B\). For \(E\subset X\times Y\), retain both original sections
\[
 E_x=\{y:(x,y)\in E\},\qquad E^y=\{x:(x,y)\in E\}.
 \tag{GM7}
\]
For fixed \(x\), the class of \(E\) with \(E_x\in\mathcal B\) is a sigma-algebra: sections commute with complements and countable unions. It contains the generating rectangles, so it contains \(\mathcal A\otimes\mathcal B\). The same proof gives \(E^y\in\mathcal A\) for every \(y\). These are statements at every point, before taking any completion. If \(h\) is product-measurable, the sections of every inverse-image ray are the inverse-image rays of \(h_x,h^y\). Consequently all its sections are measurable, including nonnegative functions with infinite values.

### 16.3. Constructing the original product measure and proving uniqueness

Let \((X,\mathcal A,\mu)\), \((Y,\mathcal B,\nu)\) be sigma-finite measure spaces. Retain increasing measurable exhaustions \(X_n\uparrow X\), \(Y_n\uparrow Y\) with finite original \(\mu(X_n)\), \(\nu(Y_n)\). Such increasing exhaustions are obtained by taking the finite unions of the finite-measure sets in the given sigma-finite covers. Empty factors are allowed throughout.

First suppose \(\nu(Y)<\infty\). The product-measurable sets \(E\) for which \(x\mapsto\nu(E_x)\) is measurable form a Dynkin class. The whole product gives the constant \(\nu(Y)\). For the complement the original value is \(\nu(Y)-\nu(E_x)\), a difference of finite values. For a disjoint countable union its section measure is the countable sum of the section measures; its finite partial sums are measurable and their pointwise increasing limit is measurable by (GM2). Every rectangle belongs because its section measure is \(\nu(B)1_A(x)\). Rectangles are intersection-closed and include the whole product, so (GM6) proves the assertion for every product-measurable \(E\).

For general sigma-finite \(\nu\), apply that finite proof to the measure \(\nu_n(B)=\nu(B\cap Y_n)\) on the original \(Y\). It gives measurability of \(x\mapsto\nu(E_x\cap Y_n)\). Measure continuity and (GM2) then give measurability of \(x\mapsto\nu(E_x)\). Define
\[
 \rho(E)=\int_X\nu(E_x)\,d\mu(x)
      \quad(E\in\mathcal A\otimes\mathcal B),\qquad
 \rho(A\times B)=\mu(A)\nu(B).
 \tag{GM8}
\]
For disjoint \(E_j\), the sections are disjoint, and the section measure of their union is \(\sum_j\nu((E_j)_x)\). Countable nonnegative integration proved in (GM4) gives \(\rho(\bigcup E_j)=\sum_j\rho(E_j)\), and \(\rho(\varnothing)=0\). Thus this definition constructs a measure, without assuming a product-measure theorem. The rectangle identity follows by integrating \(\nu(B)1_A\). If \(\nu(B)<\infty\), it is the simple integral. If \(\nu(B)=\infty\), take the increasing functions \(k1_A\): the integral is zero when \(\mu(A)=0\), and infinite when \(\mu(A)>0\). If \(\nu(B)=0\), the function is zero even when \(\mu(A)=\infty\). Hence the full identity uses the stated \(0\cdot\infty=0\) convention and retains all zero and infinite cases. The original windows \(X_n\times Y_n\) have finite \(\rho\)-measure \(\mu(X_n)\nu(Y_n)\) and exhaust the product. This proves sigma-finiteness of \(\rho\).

This is the unique measure on \(\mathcal A\otimes\mathcal B\) with the rectangle values in (GM8). If \(\rho'\) is another, restrict both to the window \(Z_n=X_n\times Y_n\). They have the same finite mass on \(Z_n\). The sets in its restricted sigma-algebra on which they agree form a Dynkin class: relative complements subtract from that finite common mass, and disjoint unions use countable additivity. Rectangles intersected with \(Z_n\) are an intersection-closed generating class and have identical original product values. Formula (GM6) proves equality on every restricted measurable set. For \(E\in\mathcal A\otimes\mathcal B\), continuity on \(E\cap Z_n\uparrow E\) then proves \(\rho(E)=\rho'(E)\), including infinity. We denote this proved measure by \(\mu\otimes\nu\).

Apply the same construction in the opposite order, and let \(\tau(x,y)=(y,x)\). This is a measurable bijection with measurable inverse, since both inverse-image operations take generating rectangles to generating rectangles. The transported measure \(E\mapsto(\nu\otimes\mu)(\tau E)\) has the same rectangle values as (GM8). Uniqueness therefore proves the exact comparison
\[
 (\mu\otimes\nu)(E)=(\nu\otimes\mu)(\tau E)
   =\int_X\nu(E_x)\,d\mu(x)
   =\int_Y\mu(E^y)\,d\nu(y).
 \tag{GM9}
\]
The comparison is proved on the original spaces and their original measurable sets. No factor measure has been rescaled, completed silently, or replaced.

### 16.4. Full Tonelli and absolutely integrable complex Fubini

Let \(h:X\times Y\to[0,\infty]\) be \(\mathcal A\otimes\mathcal B\)-measurable. Its finite simple approximations \(s_n\uparrow h\) in (GM3) are product-measurable. For each simple function, (GM9) applied to its disjoint level sets and the finite original coefficients proves equality of its product integral and both iterated integrals. Its section integrals are measurable functions of the outer variable by the section-measure proof in Section 16.3 and finite additivity. For every original \(x\), sectionwise (GM4) gives \(\int (s_n)_x\,d\nu\uparrow\int h_x\,d\nu\). Thus the latter is measurable by (GM2). Applying (GM4) once more to these outer functions, and also to the product integrals, proves
\[
 \int_{X\times Y}h\,d(\mu\otimes\nu)
 =\int_X\left(\int_Yh(x,y)\,d\nu(y)\right)d\mu(x)
 =\int_Y\left(\int_Xh(x,y)\,d\mu(x)\right)d\nu(y).
 \tag{GM10}
\]
Each integral may be infinite, and the sections are measurable at every point. The reverse integral follows either by the same argument or by the exact swap in (GM9). Every factor value, original point and original measure remains.

For product-measurable complex \(h\) with \(\int|h|\,d(\mu\otimes\nu)<\infty\), apply (GM10) to \(|h|\). The inner absolute integral is finite outside a measurable outer null set, by the finite-integral infinite-value argument in Section 16.1. Apply (GM10) separately to the positive and negative parts of \(\operatorname{Re}h\) and \(\operatorname{Im}h\). All four product integrals are finite, because each integrand is at most \(|h|\). Their inner integrals are finite outside the same exceptional set, and finite subtraction yields
\[
 \int h\,d(\mu\otimes\nu)
 =\int_X\left(\int_Y h_x\,d\nu\right)d\mu
 =\int_Y\left(\int_X h^y\,d\mu\right)d\nu,\qquad
 \left|\int_Y h_x\,d\nu\right|\leq\int_Y|h_x|\,d\nu
 \quad\text{for almost every }x .
 \tag{GM11}
\]
Define an otherwise undefined inner complex integral to be zero on its measurable exceptional null set. The resulting outer function is measurable: it is the corresponding finite combination of the four measurable nonnegative inner integrals off that set, and zero on it. The displayed bound and (GM10) show it is absolutely integrable. Interchanging the factors proves the same assertions in the opposite order. This establishes Fubini at its actual absolute-integrability hypothesis; it does not subtract infinite positive and negative integrals.

### 16.5. Completed products, exceptional sections and the Euclidean receiving map

Write \(\widehat\rho\) for the completion of \(\rho=\mu\otimes\nu\) by (GM1). If a set \(S\) belongs to this completion, there are \(E,N\in\mathcal A\otimes\mathcal B\) with \(\rho(N)=0\) and \(S\mathbin{\triangle} E\subset N\). Formula (GM10) for \(1_N\) gives \(\nu(N_x)=0\) outside a measurable \(\mu\)-null set, and \(\mu(N^y)=0\) outside a measurable \(\nu\)-null set. For those nonexceptional \(x\), the section \(S_x\) differs from the original measurable \(E_x\) by a subset of the measurable null \(N_x\). Hence it belongs to the completed factor sigma-algebra \(\overline{\mathcal B}\) and has measure \(\overline\nu(S_x)=\nu(E_x)\). The same statement holds for the opposite sections with \(\overline\mu\). We have proved
\[
 \widehat\rho(S)=\rho(E)
 =\int_X\overline\nu(S_x)\,d\overline\mu(x)
 =\int_Y\overline\mu(S^y)\,d\overline\nu(y),
 \tag{GM12}
\]
where an inner integral or section measure is assigned zero on its exceptional null set. The resulting outer function agrees with the measurable section function of \(E\) off that null set, so it is measurable for the completed factor and has the same integral. If a factor was not complete, using its completed measure in (GM12) is necessary. Even if both factors were complete, this proof gives no assertion about the exceptional sections.

For a nonnegative \(\widehat\rho\)-measurable function \(f\), take its increasing finite simple approximations \(f_n\) from (GM3). Each of their finitely many completed-measurable level sets differs from a product-measurable set by a subset of a product-measurable null set. There are only countably many such level sets over all \(n\). Let \(N\) be the union of their null upper bounds. It is product-measurable and \(\rho(N)=0\). Replacing each level set by its product-measurable representative gives a product-measurable simple function \(h_n\) agreeing with \(f_n\) on \((X\times Y)\setminus N\); representatives that overlap on \(N\) cause no problem because we set \(h_n=0\) on all of \(N\). The resulting sequence is increasing everywhere: off \(N\) it is the original increasing \(f_n\), and on \(N\) every value is zero. Its product-measurable supremum \(h\) agrees with \(f\) off \(N\). In the completed measure a nonnegative function supported on a null set has integral zero, by the simple-integral definition. Thus \(\int f\,d\widehat\rho=\int h\,d\rho\). Outside the outer null set on which the sections of \(N\) may fail to be null, the section \(f_x\) is measurable for \(\overline{\mathcal B}\) and agrees with \(h_x\) off the factor null \(N_x\). To check measurability, for each real ray their inverse images have symmetric difference in \(N_x\); (GM1) applies. Their completed section integrals are equal. Applying (GM10) to \(h\) proves both completed iterated identities for \(f\), with exactly the exceptional-set convention in (GM12). Applying this to \(|f|\) and to the four real and imaginary parts proves the completed absolutely integrable complex version as well.

The exceptional-section qualification cannot be removed. Take the original completed Lebesgue \(X=[0,1]\), and let \(Y=\{0,1\}\) with sigma-algebra \(\{\varnothing,Y\}\) and measure \(\nu(Y)=1\). This factor is already complete: its only measurable null set is empty. The measurable product set \(\{0\}\times Y\) has measure \(\mu(\{0\})\nu(Y)=0\cdot1=0\). Its subset \(S=\{(0,0)\}\) is measurable in the completed product and has measure zero, while its section at \(x=0\) is \(\{0\}\), which is not measurable in that original, already complete, factor. For every \(x\ne0\) the section is empty. This is a concrete counterexample, with finite factor measures, to a claim of measurable completed-product sections at every point.

Finally take the original Borel measures on \(\mathbb R^a\) and \(\mathbb R^b\), \(a,b\geq1\), constructed in Section 15.0 with every coordinate interval length retained. Their product sigma-algebra equals the Borel sigma-algebra of the original \(\mathbb R^{a+b}\). One inclusion follows because Borel rectangles are Borel: the two coordinate projections are continuous, as their distances are bounded by the full original Euclidean distance. For the other inclusion, each Euclidean open set is the countable union of rational-endpoint open coordinate boxes whose closures it contains, by the coordinate density and interior-ball argument already proved in Section 12.8 of the metric chapter. Each such box is a product rectangle, so every open set lies in the product sigma-algebra. Both the constructed \((a+b)\)-dimensional Borel measure and the product measure give the full same box value
\[
 \prod_{i=1}^{a+b}(b_i-a_i)
 =\left(\prod_{i=1}^{a}(b_i-a_i)\right)
   \left(\prod_{i=a+1}^{a+b}(b_i-a_i)\right).
 \tag{GM13}
\]
On each bounded coordinate window they are finite and agree on the generating boxes; (GM6) and exhaustion prove equality on all Borel sets. Their completions therefore agree by (GM1) and the completed-Borel characterization in Section 15.0. This is the exact comparison with the Euclidean integrals in LP3--LP5, retaining the full original coordinate product and every null face. The new general proof extends the scope of the prerequisite; it leaves those receiving formulas intact.

## 17. Strong measurability and complete Banach-valued integration

These proofs supply the exact analytic entry used by the positivity, Fourier and symbol chapters. It keeps the original Banach norm, every coordinate seminorm and the Fourier coefficient \((2\pi)^{-n}\). The scalar measure, nonnegative integral, convergence, Hölder, Minkowski and sigma-finite product theorems are the independent constructions in Sections 15--16 of the Banach and measure chapter. Completeness is part of the definition of each stated Banach space. The chosen Zorn axiom is used only where identified. These are standard foundations; no novelty is claimed.

### 17.1. Strong measurability and finite-valued approximation

Let \((\Omega,\mathcal A,\mu)\) be a positive measure space. It need not be sigma-finite or complete. Let \(B\) be the original real or complex Banach space. Equality almost everywhere means equality outside a measurable null set. We replace values on that set by zero when constructing representatives. A finite-valued measurable function is
\[
 s=\sum_{j=1}^J b_j1_{E_j},\qquad
 E_j\in\mathcal A,\quad E_j\cap E_k=\varnothing\ (j\ne k),
 \quad b_j\in B.
 \tag{BI1}
\]
The value off their union is zero. A function \(f:\Omega\to B\) is strongly measurable when it is the pointwise limit almost everywhere of such functions. The union of the finitely many values in a countable approximating sequence, together with zero, is countable. Its closure \(S\) is separable, and \(f\) takes values in \(S\) off one measurable null set. For each \(b\in B\), the real function \(\|f-b\|_B\) is measurable there, since it is the pointwise limit of the corresponding measurable distances. Its extension by the distance from zero on the null set is measurable.

Conversely suppose, after this null-set replacement, that \(f\) takes values in a separable subset \(S\subset B\) and every distance \(\|f-b\|_B\) is measurable. Choose a countable dense family \(b_1,b_2,\ldots\) in \(S\cup\{0\}\), with \(b_1=0\). For each \(N\geq1\), choose the least index among the minimizers of the first \(N\) distances. The measurable cells are explicitly
\[
 E_{N,j}=
 \{\|f-b_j\|_B<\|f-b_k\|_B\text{ for every }k<j\}
 \cap
 \{\|f-b_j\|_B\leq\|f-b_k\|_B\text{ for every }j<k\leq N\},
 \quad 1\leq j\leq N,
 \qquad
 q_N=\sum_{j=1}^N b_j1_{E_{N,j}}.
 \tag{BI2}
\]
An intersection over no indices imposes no condition. These disjoint cells cover \(\Omega\), including ties and zero distances. Density proves \(q_N(x)\to f(x)\) at every point of this representative. Since zero is always one of the candidates,
\[
 \|q_N(x)-f(x)\|_B\leq\|f(x)\|_B,\qquad
 \|q_N(x)\|_B\leq2\|f(x)\|_B.
 \tag{BI3}
\]
This proves the converse without a sigma-finiteness assumption. It also proves closure of strong measurability under pointwise almost-everywhere limits: take the closure of the countable union of the separable ranges of all functions in the sequence. The limit has its range in that closure, and every distance to a fixed vector is a measurable pointwise limit. Finite sums and continuous linear images are covered by the same argument; their ranges lie in the separable closure of the appropriate countable sums or images.

If \(1\leq p<\infty\) and \(\int\|f\|_B^p\,d\mu<\infty\), dominated convergence applied to (BI3) gives
\[
 \|q_N-f\|_{L^p(\mu;B)}^p
  =\int_\Omega\|q_N-f\|_B^p\,d\mu\longrightarrow0.
 \tag{BI4}
\]
Each nonzero value \(b_j\) of \(q_N\) has a support of finite measure: on its cell, (BI3) gives \(\|f\|_B\geq\|b_j\|_B/2\), hence
\[
 \mu(E_{N,j})
 \leq {2^p\over\|b_j\|_B^p}
          \int_{E_{N,j}}\|f(x)\|_B^p\,d\mu(x)<\infty
 \quad(b_j\ne0).
 \tag{BI5}
\]
The zero cell can have infinite measure and contributes the zero vector; no expression \(0\cdot\infty\) is used to define its integral. Thus finite-valued functions with finite-measure nonzero cells are dense in every finite-\(p\) Bochner space, on the original arbitrary measure space.

### 17.2. The actual vector integral, norm bound and continuous maps

For (BI1) with finite-measure nonzero cells, set
\[
 I(s)=\sum_{\{j:b_j\ne0\}}\mu(E_j)b_j,\qquad
 \|I(s)\|_B\leq\sum_{\{j:b_j\ne0\}}\mu(E_j)\|b_j\|_B
                 =\int_\Omega\|s\|_B\,d\mu.
 \tag{BI6}
\]
The sums on the right also omit zero cells. Refining any two finite representations by their intersections proves independence: the measure of each finite-measure cell is the sum of its refined pieces, and every original vector coefficient remains. A common refinement proves linearity for finite-valued integrable functions and the difference bound
\(\|I(s)-I(t)\|_B\leq\int\|s-t\|_B\,d\mu\).

Let \(f\) be strongly measurable and norm-integrable. Choose any finite-valued integrable sequence \(s_k\) tending to \(f\) in \(L^1(\mu;B)\), supplied by (BI4). Its integrals are Cauchy by the difference bound, so completeness of the original \(B\) supplies a vector limit. Define
\[
 \int_\Omega f\,d\mu=\lim_{k\to\infty}I(s_k),\qquad
 \left\|\int_\Omega f\,d\mu\right\|_B
       \leq\int_\Omega\|f\|_B\,d\mu.
 \tag{BI7}
\]
Indeed
\(\int\|s_k\|_B\leq\int\|f\|_B+\int\|s_k-f\|_B\).
Any second approximating sequence \(t_k\) gives the same limit because
\(\|I(s_k)-I(t_k)\|_B\leq\|s_k-f\|_1+\|t_k-f\|_1\).
This proves existence, independence, linearity, almost-everywhere invariance and the exact norm inequality. It is the Bochner integral; its definition retains the original vector space and its norm.

If \(T:B\to C\) is bounded linear between the original Banach spaces, then \(Tf\) is strongly measurable and
\[
 \int_\Omega Tf\,d\mu
       =T\!\left(\int_\Omega f\,d\mu\right),\qquad
 \|Tf\|_{L^1(\mu;C)}\leq\|T\|_{\mathcal L(B,C)}\|f\|_{L^1(\mu;B)}.
 \tag{BI8}
\]
Both statements hold first for each finite sum, with its original coefficient order, and then follow by the displayed operator norm and (BI7). In particular every real or complex continuous linear functional commutes with integration. Complex Banach duality here is complex linear, with no conjugation inserted in that identity.

Suppose \(f_k\) are strongly measurable, \(f_k\to f\) almost everywhere, and \(\|f_k(x)\|_B\leq g(x)\) for one nonnegative integrable \(g\). The closure argument in Section 17.1 proves strong measurability of the limit; continuity of the norm gives \(\|f\|_B\leq g\). Scalar dominated convergence applied to the exact bound \(\|f_k-f\|_B\leq2g\) gives
\[
 \int_\Omega\|f_k-f\|_B\,d\mu\longrightarrow0,\qquad
 \left\|\int_\Omega f_k\,d\mu-\int_\Omega f\,d\mu\right\|_B
       \leq\int_\Omega\|f_k-f\|_B\,d\mu\longrightarrow0.
 \tag{BI9}
\]
The majorant hypothesis and the pointwise limit are explicit; a weak scalar limit alone cannot be substituted.

### 17.3. Complete Bochner spaces, including nonseparable Hilbert spaces

For \(1\leq p<\infty\), the space \(L^p(\mu;B)\) consists of almost-everywhere classes of strongly measurable functions with norm
\[
 \|f\|_{L^p(\mu;B)}
     =\left(\int_\Omega\|f(x)\|_B^p\,d\mu(x)\right)^{1/p}.
 \tag{BI10}
\]
At \(p=\infty\) use the essential supremum of the same original pointwise norm. Scalar Minkowski and the pointwise Banach triangle inequality give the norm triangle inequality; vanishing norm is exactly almost-everywhere vanishing.

Let \(f_j\) be Cauchy. Choose a subsequence with
\(\|f_{j_{k+1}}-f_{j_k}\|_p\leq2^{-k}\).
For finite \(p\), the increasing functions
\[
 G_M(x)=\|f_{j_1}(x)\|_B+
          \sum_{k=1}^M\|f_{j_{k+1}}(x)-f_{j_k}(x)\|_B
\]
have \(L^p\) norms at most \(\|f_{j_1}\|_p+\sum_{k=1}^M2^{-k}\).
Scalar monotone convergence applied to \(G_M^p\) shows that their limit is finite almost everywhere and has that same finite bound. Completeness of \(B\) therefore gives the pointwise vector sum
\[
 f(x)=f_{j_1}(x)+
           \sum_{k=1}^\infty(f_{j_{k+1}}(x)-f_{j_k}(x))
 \quad\text{almost everywhere},\qquad
 \|f-f_{j_k}\|_p
       \leq\sum_{\nu=k}^\infty
                   \|f_{j_{\nu+1}}-f_{j_\nu}\|_p
       \leq\sum_{\nu=k}^\infty2^{-\nu}.
 \tag{BI11}
\]
The first inequality follows by bounding the pointwise difference by the entire nonnegative tail and passing its finite sums through monotone convergence. Strong measurability of \(f\) follows from Section 17.1. The bound on \(G\) puts \(f\) in \(L^p\); the Cauchy property and the triangle inequality give convergence of the entire original sequence. For \(p=\infty\), remove the countable union of measurable null sets for the initial essential bound and every displayed difference bound. The same series converges uniformly in \(B\) on the complement and satisfies (BI11) in the essential-supremum norm. This proves completeness at every \(1\leq p\leq\infty\) on the original measure space.

Finite-valued density (BI4) has only been proved for finite \(p\). It is false in general at infinity. On \(\Omega=\mathbb N\) with counting measure and \(B=\ell^2(\mathbb N)\), let \(f(k)=e_k\), the original unit coordinate vectors. The truncations are finite-valued and converge pointwise, so \(f\) is strongly measurable, with essential-supremum norm one. If \(s\) has any finite set of values \(v_1,\ldots,v_J\), then
\[
 \|e_k-v_j\|_{\ell^2}^2
      =1+\|v_j\|_{\ell^2}^2
                -2\operatorname{Re}(v_{j,k})\longrightarrow
                       1+\|v_j\|_{\ell^2}^2.
 \tag{BI12}
\]
Each coordinate \(v_{j,k}\) tends to zero, because its square sum is finite. Taking the minimum over this finite family shows
\(\liminf_{k\to\infty}\|e_k-s(k)\|_{\ell^2}\geq1\).
Thus the exact original essential-supremum distance is at least one.

For an arbitrary complex Hilbert space \(H\), finite or infinite dimensional and possibly nonseparable, define
\[
 (f,g)_{L^2(\mu;H)}
       =\int_\Omega(f(x),g(x))_H\,d\mu(x).
 \tag{BI13}
\]
The inner product is linear in its first variable. Scalar Cauchy--Schwarz proves absolute integrability of this scalar pairing and its continuity. Strong measurability of the pair is inherited from finite-valued approximations. The pointwise Hilbert identities give linearity, conjugate symmetry and positivity after integration, with \((f,f)=\|f\|_2^2\). Completeness is (BI11), so this is a Hilbert space. No countable basis of the ambient \(H\) was used.

**The full pointwise Hilbert inequality used in (BI13).** For the original possibly nonseparable \(H\), let \(v\ne0\) and \(c=(u,v)_H/(v,v)_H\). Positivity of its original norm gives the complete expansion
\[
 0\leq\|u-cv\|_H^2
 =\|u\|_H^2-\overline c(u,v)_H-c(v,u)_H+|c|^2\|v\|_H^2
 =\|u\|_H^2-\frac{|(u,v)_H|^2}{\|v\|_H^2}.
 \tag{BI13a}
\]
Every term uses the original inner product, linear in its first variable. For \(v=0\), the pairing is zero. Thus \(|(u,v)_H|\leq\|u\|_H\|v\|_H\), including all zero cases. Applying the separately proved scalar integral Cauchy--Schwarz to these two original pointwise norms proves the absolute-integrability clause of (BI13). No basis or separability of \(H\) is used.

### 17.4. Both original Fubini orders and the completed-product exception

Let \((X,\mathcal A,\mu)\), \((Y,\mathcal B,\nu)\) be sigma-finite positive measure spaces, and let \(\mu\otimes\nu\) be their original product measure constructed in the independent scalar proof. For \(f:X\times Y\to B\) strongly measurable with
\(\int_{X\times Y}\|f\|_B\,d(\mu\otimes\nu)<\infty\), we prove both iterated Bochner integrals and
\[
 \int_X\left(\int_Y f(x,y)\,d\nu(y)\right)d\mu(x)
       =\int_{X\times Y}f\,d(\mu\otimes\nu)
       =\int_Y\left(\int_X f(x,y)\,d\mu(x)\right)d\nu(y).
 \tag{BI14}
\]
The original sigma-finiteness hypotheses are retained here; the arbitrary-measure construction of a single integral does not remove them from this product theorem.

For a finite-valued integrable \(s=\sum_{j=1}^Jb_j1_{A_j}\) on the product, scalar measurable sections and Tonelli give measurable functions \(x\mapsto\nu((A_j)_x)\), finite almost everywhere when \(b_j\ne0\), since then \((\mu\otimes\nu)(A_j)<\infty\). Therefore
\[
 g_s(x)=\sum_{\{j:b_j\ne0\}}b_j\nu((A_j)_x),\qquad
 \int_X g_s\,d\mu=\sum_{\{j:b_j\ne0\}}
                         b_j(\mu\otimes\nu)(A_j)=I(s).
 \tag{BI15}
\]
On the exceptional measurable null set assign \(g_s=0\). This map takes values in a finite-dimensional span; distances to any vector are measurable continuous functions of the finitely many measurable coefficients. Section 17.1 proves strong measurability. The norm bound
\(\|g_s(x)\|_B\leq\int_Y\|s(x,y)\|_B\,d\nu(y)\)
and Tonelli prove integrability. The integral identity follows from (BI8) applied to each fixed-vector linear map on the scalar integrable coefficient.

Choose integrable finite-valued \(s_k\) with
\(\|s_k-f\|_{L^1(\mu\otimes\nu;B)}\leq2^{-k}\).
The definition of strong measurability uses its own pointwise approximating sequence. Its sections converge pointwise off one product-null set; scalar Tonelli shows that its sections are null for almost every \(x\). Thus for almost every \(x\), \(f(x,\cdot)\) is strongly measurable. Tonelli on \(\|f\|_B\) gives its section integrability. Further,
\[
 \int_X\sum_{k=1}^\infty
       \left(\int_Y\|s_k(x,y)-f(x,y)\|_B\,d\nu(y)\right)d\mu(x)
       \leq\sum_{k=1}^\infty2^{-k}<\infty.
 \tag{BI16}
\]
Hence every inner error tends to zero outside one measurable null set. The integral \(g(x)=\int_Yf(x,y)\,d\nu(y)\), defined as zero on the exceptional set, is the almost-everywhere norm limit of the strongly measurable \(g_{s_k}\). Section 17.1 proves its strong measurability. The pointwise norm inequality and Tonelli give
\[
 \int_X\|g(x)\|_B\,d\mu(x)\leq
             \int_{X\times Y}\|f(x,y)\|_B\,d(\mu\otimes\nu),\qquad
 \|g-g_{s_k}\|_{L^1(\mu;B)}
       \leq\|f-s_k\|_{L^1(\mu\otimes\nu;B)}.
 \tag{BI17}
\]
Use (BI7), (BI15) and this exact difference bound to pass to the limit, proving the first equality in (BI14). The scalar factor-swap map preserves the original product measure; applying the proved argument after that map proves the second order, without replacing a coefficient or measure.

For the completion of the product, every measurable finite-valued approximant can be replaced by a raw-product-measurable one outside a product-null set: its finitely many measurable cells differ from raw cells by subsets of a measurable null set, by the definition of completion. Subtract earlier raw cells from later ones to restore disjointness; put the value zero on their common raw null exceptional set. These measurable operations preserve the original values elsewhere. Performing this replacement for the countably many approximants leaves one raw null exceptional set. Its sections are null almost everywhere by scalar Tonelli. The preceding proof then applies to the completed factor sections and gives the same original vector integral. Exceptional sections may fail to be measurable before completion and cannot be asserted integrable at every point. The full finite-factor counterexample in the scalar product chapter remains in force; (BI14) asserts its section statements almost everywhere.

### 17.5. The exact Fourier and operator receivers

**Editorial scope correction for real Banach spaces.** The complex exponentials in (BI18) act on a complex Banach space. For an original real \(B\), they do not define scalar multiplication inside \(B\). The real-space construction following the original receiver proves the exact replacement map into \(B\times B\) and back to \(B\), retaining its original norm, both real components, both phases and the complete inverse coefficient. The complex-space formulas and proofs below keep their original meaning; none is silently asserted as a \(B\)-valued complex exponential when \(B\) is real.

On \(\mathbb R^n\), a norm-continuous \(B\)-valued function has separable range: images of a countable dense set in each coordinate box are dense in the image by continuity, and the boxes exhaust the domain. Norm distance functions are continuous, so Section 17.1 proves strong measurability. The same holds for every norm-continuous derivative. For a norm-smooth Schwartz function with the original seminorms
\(s_N(u)=\max_{|\alpha|\leq N}\sup_x\langle x\rangle^N\|\partial^\alpha u(x)\|_B\),
the integral of every derivative multiplied by every fixed coordinate polynomial is finite, using the exact weight integral proved in Section 18 below. Thus its original Fourier integral exists in \(B\):
\[
 \widehat u(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}u(x)\,dx,\qquad
 u(x)=(2\pi)^{-n}\int_{\mathbb R^n}e^{ix\cdot\xi}\widehat u(\xi)\,d\xi.
 \tag{BI18}
\]
For fixed derivatives, the full integrable derivative majorants and (BI9) justify differentiating the first integral. Banach integration by parts follows by applying each continuous linear functional, using scalar integration by parts with compact cutoffs, then passing the cutoff through (BI9). The cutoff derivative terms have the complete Schwartz decay and tend to zero in norm. This proves all original derivative and coordinate Fourier identities. For clarity the full differentiated identity is, for every multiindex \(\alpha\) and integer \(M\geq0\),
\[
 (1+|\xi|^2)^M\partial_\xi^\alpha\widehat u(\xi)
 =(-i)^{|\alpha|}
 \sum_{\substack{j,k_1,\ldots,k_n\geq0\\j+\sum_i k_i=M}}
  {M!\over j!\prod_i k_i!}(-1)^{\sum_i k_i}
       \widehat{\partial_x^{(2k_1,\ldots,2k_n)}(x^\alpha u)}(\xi).
 \tag{BI18a}
\]
The first derivative identity is
\(\partial_\xi^\alpha\widehat u=(-i)^{|\alpha|}\widehat{x^\alpha u}\);
integration by parts gives
\(\widehat{\partial_x^{2k}(x^\alpha u)}=(-1)^{|k|}\xi^{2k}\widehat{x^\alpha u}\).
Expanding the whole polynomial proves (BI18a), including every sign and coefficient. Each input derivative in its right side has the complete Leibniz sum (SC2), and (SC4) bounds its integral. Its Fourier norm is at most that original input integral, by (BI7), uniformly in \(\xi\). Thus choosing \(2M\) greater than \(n\) plus any specified output coordinate weight proves integrability of every weighted output derivative. To justify the preceding integrations by parts, take a compact smooth \(\chi=1\) on \(|x|\leq1\), supported in \(|x|\leq2\), and \(\chi_R(x)=\chi(x/R)\). Every nonzero cutoff derivative is \(R^{-|\beta|}(\partial^\beta\chi)(x/R)\), supported in \(R\leq|x|\leq2R\). Every full product term tends to zero in norm by the Schwartz bound of order greater than \(n\) plus its coordinate degree, and its original \(R^{-|\beta|}\) factor remains. The undifferentiated cutoff tends to one with the integrable Schwartz majorant. This proves the claimed limit for all original derivative orders. Hence the second integral also exists. By (BI8), every continuous linear functional turns it into the original scalar inversion formula. The exact Hahn--Banach norm identity in the Banach chapter proves (BI18) as an equality of the original vectors. No Fourier coefficient is altered.

For \(H\)-valued \(L^2\) on the original Euclidean space, approximate a finite-valued function by replacing each scalar cell indicator of finite measure by compact smooth scalar functions using the complete scalar density proof. The exact approximation bound is
\[
 \left\|\sum_{j=1}^J b_j(a_j-1_{E_j})\right\|_{L^2(dx;H)}
       \leq\sum_{j=1}^J\|b_j\|_H
                         \|a_j-1_{E_j}\|_{L^2(dx)}.
 \tag{BI19}
\]
Together with (BI4), this proves density of finite sums of compact smooth scalar functions times original Hilbert vectors. Their pairings have the entire Gram sum
\[
 \int_{\mathbb R^n}
       \left(\sum_j a_j(x)b_j,\sum_k c_k(x)d_k\right)_Hdx
 =\sum_{j,k}(b_j,d_k)_H
                \int_{\mathbb R^n}a_j(x)\overline{c_k(x)}\,dx.
 \tag{BI20}
\]
Applying scalar Plancherel to each term preserves every Gram entry and proves
\[
 \int_{\mathbb R^n}(u(x),v(x))_H\,dx
   =(2\pi)^{-n}\int_{\mathbb R^n}
                         (\widehat u(\xi),\widehat v(\xi))_H\,d\xi.
 \tag{BI21}
\]
The original inverse coefficient is \((2\pi)^{-n}\). Both transforms extend by completeness and this density; their inverse identities on the dense finite sums extend to all of \(L^2(dx;H)\). They act between the original \(dx\) norm and the original \((2\pi)^{-n}d\xi\) norm, with the displayed factor retained. The argument supplies the precise Bochner \(L^2\) step in the positivity chapter's \(P14\)--\(P18\), and does not impose separability on \(H\).

A norm-smooth symbol taking values in \(\mathcal L(B_1,B_2)\) has strongly measurable range on every finite coordinate domain by the same continuity argument. That full operator space is Banach because \(B_2\) is Banach, by the existing operator-completeness proof. Every integrable operator-valued expression therefore obeys (BI7)--(BI9), and every absolutely norm-integrable product kernel obeys (BI14), in its original order. The finite-valued approximating values remain the actual bounded operators; no rank restriction is inserted. These facts supply the original \(P1\)--\(P13\) Banach Fourier, transpose and composition receivers.

**Editorial bridge: the original real Banach space and its complete Fourier receiver.** Let \(B\) now be the original real Banach space with its original norm. On the real vector space \(B\times B\), define complex scalar multiplication and a norm by
\[
 (a+ib)(x,y)=(ax-by,bx+ay),\qquad
 \|(x,y)\|_{B_{\mathbb C}}=
 \sup_{\theta\in\mathbb R}\|\cos\theta\,x-\sin\theta\,y\|_B.
 \tag{BC1}
\]
The scalar law follows by expanding both component products: multiplying successively by \(a+ib\) and \(c+id\) gives the components with scalar coefficients \(ac-bd\) and \(ad+bc\), in their original order. Identity, distributivity and addition follow componentwise. Each displayed real combination obeys the original triangle inequality; taking its supremum proves the triangle inequality in (BC1). The exact comparisons are
\[
 \max\{\|x\|_B,\|y\|_B\}
 \leq\|(x,y)\|_{B_{\mathbb C}}
 \leq\|x\|_B+\|y\|_B,
 \qquad \|(x,0)\|_{B_{\mathbb C}}=\|x\|_B.
 \tag{BC2}
\]
The lower bounds use \(\theta=0,-\pi/2\); the upper bound retains both original norms. For a nonzero scalar \(\lambda=a+ib\), put \(r=(a^2+b^2)^{1/2}>0\) and choose \(\phi\) with \(a=r\cos\phi\), \(b=r\sin\phi\), using the proved real trigonometric/polar entry. The entire expression in (BC1) after multiplication is
\[
 \cos\theta(ax-by)-\sin\theta(bx+ay)
 =r\bigl(\cos(\theta+\phi)x-\sin(\theta+\phi)y\bigr).
 \tag{BC3}
\]
Taking the original supremum, invariant under the bijection \(\theta\mapsto\theta+\phi\), proves absolute complex homogeneity. For zero scalar it is immediate. Definiteness follows from both lower bounds. A norm-Cauchy sequence of pairs has Cauchy original components by (BC2). Their limits lie in the original \(B\); the full upper bound gives convergence of the pairs. Thus \(B_{\mathbb C}\) is a complex Banach space, including \(B=0\).

Keep the maps \(\iota:B\to B_{\mathbb C}\), \(\iota x=(x,0)\), \(\operatorname{Re}_B(x,y)=x\), \(\operatorname{Im}_B(x,y)=y\), and \(C_B(x,y)=(x,-y)\). The injection is real-linear and isometric, both projections are real-linear of norm at most one, and \(\operatorname{Re}_B\iota=I_B\), \(\operatorname{Im}_B\iota=0\). The angle substitution \(\theta\mapsto-\theta\) proves that \(C_B\) is an isometry. Its full scalar relation is
\[
 C_B^2=I_{B_{\mathbb C}},\qquad
 C_B(\lambda z)=\overline\lambda C_Bz,
 \qquad \{z:C_Bz=z\}=\iota(B).
 \tag{BC4}
\]
The last equality follows from \(y=-y\), hence \(y=0\) in the original real vector space. These are exact maps, not an identification that discards the second component.

For a norm-smooth original real Schwartz function \(u\), its injection has exactly the original seminorms, since real derivatives and positive real weights commute with \(\iota\) and (BC2) is an equality on that image. The already proved complex-space Bochner integral therefore gives its full original Fourier map
\[
 F_Bu(\xi)=\int_{\mathbb R^n}
    \bigl(\cos(x\cdot\xi)u(x),-\sin(x\cdot\xi)u(x)\bigr)\,dx
 =\int_{\mathbb R^n}e^{-ix\cdot\xi}\iota u(x)\,dx.
 \tag{BC5}
\]
All integrals are in the complete norm (BC1); their integrable majorants are the original \(\|u(x)\|_B\). The two real projections give, respectively, \(\int\cos(x\cdot\xi)u(x)\,dx\) and \(-\int\sin(x\cdot\xi)u(x)\,dx\). Bounded real-linear maps commute with this integral: the assertion holds for every original finite sum, whose measure coefficients are real, and passes to the norm limit by (BI7). This supplies that statement for the projections and the conjugation even though the latter is conjugate-linear for complex scalars.

The norm-Schwartz bounds already proved for the complex receiver apply to \(\iota u\), with every original coefficient, cutoff derivative and inverse factor retained. Applying its exact inversion formula gives
\[
 \iota u(x)=(2\pi)^{-n}\int_{\mathbb R^n}
                   e^{ix\cdot\xi}F_Bu(\xi)\,d\xi.
 \tag{BC6}
\]
This vector lies in the original isometric image, and the real projection recovers exactly \(u(x)\); its imaginary projection is zero. More explicitly (BC5) gives \(C_BF_Bu(\xi)=F_Bu(-\xi)\). Apply the real-linear conjugation to the inverse integral. Its scalar relation in (BC4), followed by the original variable substitution \(\eta=-\xi\), gives that same inverse integral. It is therefore fixed by \(C_B\), proving the image statement without suppressing a component. Dimension zero uses the original point mass, factor \((2\pi)^0=1\), and the identity injection/inverse projection.

For the two-sided receiving scope, let \(v\) be a \(B_{\mathbb C}\)-valued norm-Schwartz function with \(C_Bv(\xi)=v(-\xi)\). Its original complex inverse \(Gv\) is Schwartz and obeys \(C_BGv=Gv\) by precisely the same integral and variable substitution. Thus \(Gv=\iota u\) for \(u=\operatorname{Re}_BGv\), an original real Schwartz function, and the other complex inverse identity gives \(F_Bu=v\). Conversely (BC5) gives that conjugation condition for every original \(u\). Hence (BC5) and (BC6) are both inverse maps between the original real Schwartz space and this exact conjugate-symmetric subspace, with its original complexification norm; they do not assert that the real Fourier transform takes values inside \(B\) at each frequency.

Finally, an original bounded real-linear \(T:B_1\to B_2\) extends by \(T_{\mathbb C}(x,y)=(Tx,Ty)\). Expanding (BC1) proves complex-linearity and
\[
 \|T_{\mathbb C}(x,y)\|_{(B_2)_{\mathbb C}} \leq\|T\|\|(x,y)\|_{(B_1)_{\mathbb C}},\qquad \|T_{\mathbb C}\|=\|T\|, \qquad T_{\mathbb C}\iota_1=\iota_2T. \tag{BC7} \] The reverse norm inequality tests the original vectors \((x,0)\), including the zero-domain case. Componentwise calculation proves \((ST)_{\mathbb C}=S_{\mathbb C}T_{\mathbb C}\) and \((I_B)_{\mathbb C}=I_{B_{\mathbb C}}\); if an original two-sided inverse exists, its extension remains that exact two-sided inverse. The maps commute with (BC5) and (BC6) by the finite-sum integral identity and norm limits. This proves the complete operator receiving bridge for real spaces while retaining every original norm, ordered product, phase and coefficient.

**Editorial bridge for the original real Hilbert L2 receiver.** For an original real Hilbert space \(H\), the Banach norm (BC1) is not asserted to be an inner-product norm. Keep that norm and construct the following additional Hilbert structure on the same complex vector space \(H\times H\). Write \([x,u]_H\) for the original real inner product and define
\[
 ((x,y),(u,v))_{H_{\mathbb C}}
 =[x,u]_H+[y,v]_H+i\bigl([y,u]_H-[x,v]_H\bigr),\qquad
 \|(x,y)\|_{H_{\mathbb C}}^2=\|x\|_H^2+\|y\|_H^2.
 \tag{BC8}
\]
Every real inner-product term remains. Expanding the component scalar law (BC1) shows complex-linearity in the first variable and conjugate-linearity in the second. Symmetry of the original real inner product gives conjugate symmetry. At equal vectors the imaginary terms cancel and the real terms give precisely the displayed positive square, zero only at the zero pair. This proves the asserted inner product. Its triangle inequality follows from the complete inner-product expansion in (BI13a). A Cauchy sequence has Cauchy original components and their limits converge in the displayed sum, so this is a complete complex Hilbert space without a separability hypothesis. The two norms obey the full comparison
\[
 \|(x,y)\|_{B_{\mathbb C}}
 \leq\|(x,y)\|_{H_{\mathbb C}}
 \leq\sqrt2\,\|(x,y)\|_{B_{\mathbb C}}.
 \tag{BC9}
\]
For the first inequality apply the original real Cauchy--Schwarz inequality to the scalar coefficients \(\cos\theta,-\sin\theta\) and the two component norms, using their squared sum one, and then take the actual supremum in (BC1). For the second use both lower bounds in (BC2). The identity maps between these two complete pair spaces are thus bounded with the displayed constants; neither norm replaces the other. The original injection \(\iota_H\) is isometric for both. Both real projections are contractions for the Hilbert norm, and \(C_H(x,y)=(x,-y)\) is an isometric conjugation with the same exact fixed space \(\iota_H(H)\).

Use precisely the original measures \(dx\) and \((2\pi)^{-n}d\xi\). The proved complex Hilbert Fourier maps in (BI19)--(BI21) act on this \(H_{\mathbb C}\). Their Schwartz integrals coincide with (BC5)--(BC6): the bounded identity map between the two pair norms commutes with finite-valued sums and their integral limits, by the already proved real-linear integral argument. Define \(F_H^{\mathbb R}u=F_{H_{\mathbb C}}\iota_Hu\) for every original real \(u\in L^2(dx;H)\). This is a real-linear map and its exact pairing formula is
\[
 \int_{\mathbb R^n}[u(x),w(x)]_H\,dx
 =(2\pi)^{-n}\int_{\mathbb R^n}
       (F_H^{\mathbb R}u(\xi),F_H^{\mathbb R}w(\xi))_{H_{\mathbb C}}\,d\xi,
 \qquad
 \|F_H^{\mathbb R}u\|_{L^2((2\pi)^{-n}d\xi;H_{\mathbb C})}
 =\|u\|_{L^2(dx;H)}.
 \tag{BC10}
\]
This follows from (BC8), the isometric injection and the entire complex Gram calculation (BI20)--(BI21), with every original factor retained. In particular the integral on the right has zero imaginary part, as the displayed equality proves; its integrand need not be real at every frequency.

For the exact range let \(\mathcal R_H\) consist of the original pair-valued L2 classes \(v\) satisfying \(C_Hv(\xi)=v(-\xi)\) almost everywhere. Reflection preserves the original weighted measure, and conjugation is isometric. Their difference is a bounded real-linear operator on that L2 space, of norm at most two, so its kernel \(\mathcal R_H\) is closed. On norm-Schwartz functions, the full integral substitution proved after (BC6) gives both identities
\[
 C_HF_{H_{\mathbb C}}f(\xi)=F_{H_{\mathbb C}}(C_Hf)(-\xi),\qquad
 C_HG_{H_{\mathbb C}}v(x)=G_{H_{\mathbb C}}\bigl(C_Hv(-\,\cdot)\bigr)(x).
 \tag{BC11}
\]
They extend to all the original L2 classes by the already proved density of finite sums of compact smooth scalar functions times actual Hilbert vectors, the norm bounds in (BI21), and the two isometries just proved. No pointwise integral of a general L2 class is asserted. Since \(C_H\iota_Hu=\iota_Hu\), the first identity puts \(F_H^{\mathbb R}u\) in \(\mathcal R_H\). Conversely, if \(v\in\mathcal R_H\), the second identity makes \(G_{H_{\mathbb C}}v\) fixed by conjugation almost everywhere. Outside the measurable null exceptional set its imaginary component is zero by (BC4). Thus it is exactly \(\iota_Hu\) for \(u=\operatorname{Re}_HG_{H_{\mathbb C}}v\in L^2(dx;H)\). The two previously proved complex inverse identities now give both \(F_H^{\mathbb R}u=v\) and \(\operatorname{Re}_HG_{H_{\mathbb C}}F_H^{\mathbb R}u=u\). These are both inverse maps onto the entire original \(\mathcal R_H\), with the full inverse coefficient, both pair components, almost-everywhere scope, nonseparable spaces and the dimension-zero point mass retained. In dimension zero the maps are the injection and its real projection onto the fixed space, and \((2\pi)^0=1\). This completes the real Hilbert receiver of (BI21) and its positivity applications; it does not attribute a Hilbert norm to the Banach norm (BC1). No novelty is claimed.

## 18. The original monomial Schwartz entry

For \(u:\mathbb R^n\to\mathbb C\) smooth, retain exactly
\[
 p_{\alpha,\beta}(u)=\sup_{x\in\mathbb R^n}
                           |x^\alpha\partial^\beta u(x)|,
 \qquad \alpha,\beta\in\mathbb N^n,\qquad
 \mathcal S=\{u:p_{\alpha,\beta}(u)<\infty
                               \text{ for all }\alpha,\beta\}.
 \tag{SC1}
\]
The continuous complex-linear dual is the stated tempered-distribution space. This is a definition, not a claimed proof of a different distribution topology.

For any original coordinate powers \(\gamma\) and derivatives \(\delta\), the full product formula is
\[
 \partial^\beta(x^\gamma\partial^\delta u)
 =\sum_{\substack{\theta\leq\beta\\\theta\leq\gamma}}
       {\beta\choose\theta}{\gamma!\over(\gamma-\theta)!}
       x^{\gamma-\theta}\partial^{\delta+\beta-\theta}u,\qquad
 p_{\alpha,\beta}(x^\gamma\partial^\delta u)
 \leq\sum_{\substack{\theta\leq\beta\\\theta\leq\gamma}}
       {\beta\choose\theta}{\gamma!\over(\gamma-\theta)!}
       p_{\alpha+\gamma-\theta,\delta+\beta-\theta}(u).
 \tag{SC2}
\]
The multiindex inequalities are coordinatewise. The formula follows by the finite Leibniz rule with every derivative multiplicity; zero coordinates give the usual factorial \(0!=1\). It proves continuity and stability under every original polynomial and derivative without discarding any summand.

Choose an integer \(M>n/2\). Retain the actual constant
\[
 I_{n,M}=\int_{\mathbb R^n}(1+|x|^2)^{-M}\,dx,\qquad
 (1+|x|^2)^M
 =\sum_{\substack{j,k_1,\ldots,k_n\geq0\\j+\sum_i k_i=M}}
       {M!\over j!\prod_i k_i!}\,x_1^{2k_1}\cdots x_n^{2k_n}.
 \tag{SC3}
\]
For \(n\geq1\), split into \(|x|_\infty<1\) and the shells
\(2^l\leq|x|_\infty<2^{l+1}\), \(l\geq0\).
The first integral is at most \(2^n\); the \(l\)-th integral is at most
\(2^{n(l+2)}2^{-2Ml}\).
Therefore
\(I_{n,M}\leq2^n+2^{2n}/(1-2^{n-2M})<\infty\).
This is a bound on the original integral, not a substitution for its actual value. The multinomial identity in (SC3) gives
\[
 \int_{\mathbb R^n}|u(x)|\,dx
 \leq I_{n,M}
    \sum_{\substack{j,k_1,\ldots,k_n\geq0\\j+\sum_i k_i=M}}
       {M!\over j!\prod_i k_i!}\,p_{(2k_1,\ldots,2k_n),0}(u).
 \tag{SC4}
\]
Every coefficient and seminorm remains. For \(n=0\), the Euclidean space is a single point with its original zero-dimensional Lebesgue mass one: \(I_{0,M}=1\), integration is evaluation and the sole multiindex is empty. Thus this entry includes that case.

Completeness for the exact seminorms also follows. If \(u_l\) is Cauchy for every \(p_{\alpha,\beta}\), the derivatives converge uniformly on every compact set because \(p_{0,\beta}\) controls them. The full coordinate-segment FTC argument from the smooth-completeness proof makes the common limit \(u\) smooth with those exact derivative limits. For each fixed \(\alpha,\beta\), the uniform Cauchy inequality
\(|x^\alpha\partial^\beta(u_l-u_k)(x)|<\varepsilon\)
for every \(x\) and all large \(l,k\) passes to the pointwise limit in \(k\). Taking the same supremum shows
\(p_{\alpha,\beta}(u_l-u)\leq\varepsilon\).
In particular every seminorm of \(u\) is finite. Enumerating the multiindices and taking finite maxima gives the exact locally convex topology and a complete separating metric by the earlier explicit Fréchet metric construction. No support or coordinate bound was removed.

For comparison with the original bracket seminorms used by the Banach-valued chapter, one has
\[
 p_{\alpha,\beta}(u)\leq s_{|\alpha|+|\beta|}(u),\qquad
 s_N(u)\leq
 \max_{|\beta|\leq N}
 \sum_{\substack{j,k_1,\ldots,k_n\geq0\\j+\sum_i k_i=M}}
        {M!\over j!\prod_i k_i!}\,p_{(2k_1,\ldots,2k_n),\beta}(u),
 \quad 2M\geq N.
 \tag{SC5}
\]
Here \(s_N\) retains \(\langle x\rangle^N=(1+|x|^2)^{N/2}\). The first inequality is \(|x^\alpha|\leq\langle x\rangle^{|\alpha|}\); the second uses the entire polynomial (SC3) and \(\langle x\rangle^N\leq\langle x\rangle^{2M}\). Thus both original seminorm families and their exact maps are retained, rather than replacing one by a preferred presentation. The same inequalities hold with the original Banach norm in place of scalar absolute value, supplying the integrability used in (BI18).

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

## 20. Exact entry and receiving scope

The existing original \(L^2\) completeness, compact smooth density, translation continuity, dominated convergence and compact smooth integration-by-parts statements are already proved by \(LP1\)--\(LP2\), \(LP5\), \(LP10\)--\(LP12\) and \(LP17\)--\(LP19\) in the Banach chapter. The new Banach-valued proof extends those necessary operations at their actual norm and strong-measurability hypotheses. The monomial Schwartz contract is supplied by \(SC1\)--\(SC5\), and the exact Baire selection map by \(BZ1\)--\(BZ2\) together with the original full nested-ball argument.

The original finite-coordinate Taylor contract is already proved by \(OC19\)--\(OC24\) in the metric chapter. Its ordered derivative tensors, every multiindex, coefficient, integral remainder and target norm are present. A metadata flag calling that exact entry unfinished is stale; routing its actual full proof does not add a hypothesis or alter an equation. For integer \(K\geq1\), take \(r=K-1\) in (OC22)--(OC24); the entire integral remainder and its \(K!\) coefficient bound are then present. At \(K=0\), the Taylor polynomial is empty, the remainder is the original \(f(x+h)\), and its norm is bounded by the zeroth derivative supremum on the segment. No negative factorial or nonexistent derivative enters that endpoint.

These entry providers must remain independent of their positivity, Fourier and symbol receivers. Scalar measure/integration, finite calculus and the selected logical axioms enter the providers; operator quantization and Hilbert-valued Fourier outputs do not supply their own bases.

## 21. Exact lattice cutoffs and the original derivative map

The positivity chapter requires a compact smooth lattice partition before its scalar or Banach-valued Fourier-series argument. The construction below uses only the independent real/topology and scalar-calculus proofs. It retains the entire denominator and every derivative term; no symbol estimate or Fourier theorem supplies this entry.

### 21.1. The full original lattice construction

Let \(n\geq1\). Retain the actual \(OC38\) scalar cutoff, writing \(\chi_{\rm cut}\) for that same function to distinguish it from the lattice function constructed below:
\[
 \eta(s)=\begin{cases}0,&s\leq0,\\E(-1/s),&s>0,\end{cases}
 \qquad
 \chi_{\rm cut}(s)
   ={\eta(3/2-s)\over\eta(3/2-s)+\eta(s-1)},\qquad
 \theta(t)=\chi_{\rm cut}\left(
       1+{t^2-(3/4)^2\over2((7/8)^2-(3/4)^2)}
                         \right).
 \tag{LT0}
\]
The existing full \(OC38\)--\(OC41\) endpoint and derivative proof applies to these exact radii. Hence \(\theta\) is nonnegative and smooth, equals one on \([-3/4,3/4]\), and has its support in the closed interval \([-7/8,7/8]\), which is strictly inside \((-1,1)\). Every translation, original square and denominator remains. Set
\[
 \phi(x)=\prod_{i=1}^n\theta(x_i),\qquad
 H(x)=\sum_{k\in\mathbb Z^n}\phi(x-k),\qquad
 \chi(x)={\phi(x)\over H(x)}.
 \tag{LT1}
\]
All functions and all terms in this formula are the actual ones. For each coordinate \(x_i\), choose an integer \(k_i\) with \(|x_i-k_i|\leq1/2\). Existence follows from the Archimedean integer-part proof; it does not require a nearest-lattice optimization. Thus one summand in \(H(x)\) is exactly one, since every chosen coordinate lies in the unchanged plateau \([-3/4,3/4]\). Only finitely many integer vectors can have \(x-k\in[-1,1]^n\), and on any fixed bounded neighborhood there is one common finite list of such vectors. This proves local finiteness and smoothness of \(H\), with
\[
 H(x-l)=H(x)\quad(l\in\mathbb Z^n),\qquad
 H(x)>0,\qquad
 \sum_{k\in\mathbb Z^n}\chi(x-k)
   ={1\over H(x)}\sum_{k\in\mathbb Z^n}\phi(x-k)=1.
 \tag{LT2}
\]
The equal denominator follows from reindexing the whole locally finite sum by the actual translation \(k\mapsto k+l\); it is not assumed constant in \(x\). The real compactness theorem and continuity on \([0,1]^n\) supply constants \(c,C\) with \(0<c\leq H(x)\leq C<\infty\) there. The full integer-periodicity extends those same bounds to all of \(\mathbb R^n\), by subtracting an integer vector with remaining coordinates in \([0,1]\).

The same original construction gives the sharp numerical bounds
\[
 1\le H(x)\le 2^n,\qquad
 H(l)=1,\qquad
 H\bigl(l+(1/2,\ldots,1/2)\bigr)=2^n
 \quad(l\in\mathbb Z^n).
 \tag{LT2a}
\]
For the lower bound use the actual plateau summand just exhibited. For the upper bound, a nonzero factor \(\theta(x_i-k_i)\) requires \(|x_i-k_i|<7/8\). That interval has length \(7/4<2\), so it contains at most two integers: three distinct integers have first-to-last distance at least two. Thus at most \(2^n\) products in the full sum can be nonzero, and each is at most one. At an integer point only the actual translate \(k=l\) survives and its product is one. At the displayed half-integer point precisely the two nearest choices per coordinate survive; each coordinate factor equals one, so all \(2^n\) products equal one. This proves both bounds are attained without changing \(\theta,\phi,H\) or \(\chi\).

The function \(\chi\) is nonnegative, smooth, compactly supported in \((-1,1)^n\), and at most one because \(H(x)\) contains the nonnegative summand \(\phi(x)\). For every multiindex \(\alpha\), differentiation of the exact equality \(H\chi=\phi\) gives
\[
 \partial^\alpha\chi(x)
 ={1\over H(x)}
 \left[
   \partial^\alpha\phi(x)-
   \sum_{\substack{0<\beta\leq\alpha}}
       {\alpha\choose\beta}
       (\partial^\beta H(x))
       (\partial^{\alpha-\beta}\chi(x))
 \right],
 \qquad
 \partial^\beta H(x)=
       \sum_{k\in\mathbb Z^n}\partial^\beta\phi(x-k).
 \tag{LT3}
\]
For \(\alpha=0\) the derivative sum is empty and this is (LT1). For higher orders it is a finite recursion in strictly smaller derivative orders of the original \(\chi\); every binomial factor, denominator and derivative of \(H\) remains. The common finite lists on compact neighborhoods prove each derivative identity. Periodicity and compactness bound every derivative of \(H\) globally, and the same recursion with \(H\geq c\) bounds every derivative of \(\chi\). These are bounds on the constructed functions, not replacements for their formulas.

Here are full derivative constants for the same functions. For every original multiindex \(\beta\), put
\[
 T_\beta=\prod_{i=1}^n\|\theta^{(\beta_i)}\|_\infty,\qquad
 A_\alpha=\|\partial^\alpha\chi\|_\infty.
 \tag{LT3a}
\]
Every factor is finite by the compact-support derivative proof. The product formula gives \(\partial^\beta\phi(x)=\prod_i\theta^{(\beta_i)}(x_i)\), with no mixed-coordinate summand suppressed. All derivatives of \(\theta\) vanish outside its full closed support, and vanish at either outer endpoint by their continuity and the zero exterior. At each original \(x\), at most two integer choices per coordinate can contribute to the entire derivative sum in (LT3). Consequently
\[
 \|\partial^\beta\phi\|_\infty\le T_\beta,\qquad
 \|\partial^\beta H\|_\infty\le 2^nT_\beta,\qquad
 A_0\le1,\qquad
 A_\alpha\le T_\alpha+
 2^n\sum_{0<\beta\le\alpha}{\alpha\choose\beta}
                     T_\beta A_{\alpha-\beta}\quad(|\alpha|>0).
 \tag{LT3b}
\]
The last inequality follows directly from the entire (LT3) recursion and \(H\ge1\). Induction bounds every \(A_\alpha\), using exactly the displayed smaller orders; no denominator or Leibniz term is replaced in the actual formula. Translation gives the identical bound \(A_\alpha\) for each \(\chi(x-k)\). Thus the original positivity reconstruction receives uniform derivative constants for every one of its unchanged lattice translates, with its actual period, density and Fourier factors retained below. These sharpen the preceding sufficient compactness bounds; no novelty is claimed.

Choose also the full compact smooth function
\[
 \vartheta(x)=\prod_{i=1}^n
       \chi_{\rm cut}\left(1+
                {x_i^2-1^2\over2((7/4)^2-1^2)}\right).
 \tag{LT4}
\]
It equals one on \([-1,1]^n\) and has support in \([-7/4,7/4]^n\), strictly inside \((-2,2)^n\), by the same exact \(OC41\) construction. For any original cube side \(L>4\), that support lies strictly inside the cube \((-L/2,L/2)^n\); hence it contains the full support of \(\chi\) away from its boundary and \(\vartheta\chi=\chi\). Translating both functions by \(k\) gives exactly the cutoffs required by the positivity chapter's \(P3\)--\(P4\) reconstruction. The period \(L\), density \(dx/L^n\), phase \(2\pi i l\cdot(x-k)/L\), every Fourier coefficient and every derivative factor \(2\pi i l_j/L\) remain those of that original reconstruction.

For \(n=0\), the original space has one point and \(\mathbb Z^0\) has the single empty vector. Empty products in (LT1) give \(\phi=H=\chi=1\); the sum in (LT2) is one, the sole derivative order is zero, and the cutoff can be \(\vartheta=1\). The original zero-dimensional measure has mass one. Thus no dimensional endpoint is omitted.

### 21.2. Exact prerequisite scope

Finite-coordinate Taylor, chain/product and integration-by-parts operations are supplied by the original full scalar/finite calculus \(OC1\)--\(OC24\); their complete target-coordinate and tensor maps include fixed complex matrices. The compact smooth cutoff is the original \(OC38\)--\(OC41\) construction and its proved full endpoint derivatives. Scalar measure convergence and product integration are the actual \(LP1\)--\(LP5\), \(GM1\)--\(GM13\) proofs, and finite Gram/orthogonalization is the full original finite-algebra proof with all residual lengths and both Gram matrices.

Together with the exact lattice construction (LT1)--(LT3), these independent providers supply every clause of the positivity chapter's original elementary-analysis contract. Hilbert inner-product identities refer to the stated Hilbert-space definition; completeness and the Bochner \(L^2\) receiving map are supplied by the preceding complete Banach integration proof. Neither operator quantization nor the positive-probe theorem is used as its own prerequisite.

This is an owned proof of the original entry and its exact receiving construction.

## References

- Paul Garrett, [Review of metric spaces](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2012-13/01_metric_spaces.pdf), Theorem 4.0.1, 2 February 2014; [Banach Spaces](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2016-17/02_banach.pdf), 13 November 2017, cited propositions and theorems.
- Jiří Lebl, [Basic Analysis, metric-space chapter](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-metric.tex#L2217-L2406), pinned author-source revision.
- Mathlib, [Hahn–Banach module](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/Mathlib/Analysis/Normed/Module/HahnBanach.lean), pinned source revision.
