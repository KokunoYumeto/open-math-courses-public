# Banach estimates, quotient spaces and compact parameter arguments

A Banach-space argument uses completeness, scalar separation and compactness for different reasons. This lesson proves the forms needed later for Fredholm operators, symbol actions and positivity estimates. Its examples show exactly where each hypothesis matters.

The useful distinction is between three mechanisms. Completeness turns summable errors into actual vectors. Hahn–Banach produces scalar tests without a completeness assumption. Compactness permits uniform control of a parameter family, even when that parameter space has no countable neighborhood basis. Keeping these mechanisms separate prevents a Banach-space estimate from being applied silently to a nonnormable space.

## 1. The assumptions used here

Work over \(\mathbb K=\mathbb R\) or \(\mathbb C\), with complex-linear duals when \(\mathbb K=\mathbb C\). A normed space has the metric \(d(x,y)=\|x-y\|\); it is Banach when every Cauchy sequence converges in that norm. Write \(\mathcal L(X,Y)\) for continuous linear maps. No space below is assumed separable.

Begin with Metric and topological foundations: the complete real field, its Archimedean property, finite linear algebra, scalar Cauchy–Schwarz, compactness in finite dimensions, and Zorn's maximality principle. The measure and differentiation results of that lesson are not used here. Complex scalar completeness follows coordinatewise from real completeness. Zorn's principle is the stated assumption in the Hahn–Banach proof in Section 5.

We use the definitions of open sets, neighborhoods, closure, the subspace topology and the product topology. Closure means that every open neighborhood meets the set. A map is continuous when inverse images of open sets are open; equivalently, each neighborhood of its value contains the image of a sufficiently small neighborhood of the input. The latter equivalence follows by taking inverse images in one direction and the union of these input neighborhoods in the other. Complements give the corresponding inverse-image statement for closed sets. Sections 9–10 prove the needed compactness and net assertions.

The proofs proceed from finite-dimensional norm control through completeness of operator spaces and quotients, Hahn–Banach separation, uniform boundedness, open mapping, nets, compactness and square-summable sequences. The complete-metric Baire theorem is proved in Section 6. Bochner integration, Hilbert-space representation and a closed-graph theorem for Fréchet spaces need separate arguments.

## 2. Finite-dimensional norms and exact sequences

Let \(E\) have basis \(e_1,\ldots,e_d\) and any norm \(N\). Set \(|a|=(\sum_{j=1}^d|a_j|^2)^{1/2}\) for its coordinate vector. The triangle inequality and the finite scalar Cauchy–Schwarz inequality give
\[
N\left(\sum_j a_je_j\right)\leq C|a|,
\qquad C=\left(\sum_jN(e_j)^2\right)^{1/2}.
\tag{B1}
\]
Also \(|N(u)-N(v)|\leq N(u-v)\leq C|u-v|\), so \(N\) is continuous in coordinates. For \(d>0\) there is \(c>0\) such that \(N(a)\geq c\) on \(|a|=1\). Otherwise choose unit vectors with norms tending to zero. The compactness interface Section 4 of Metric and topological foundations gives a coordinate-convergent subsequence whose limit is still a unit vector; continuity makes its norm zero, a contradiction. Scaling yields
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
The construction works also at isolated points: a sufficiently small ball then consists of that point. For \(k,l\geq j\), both centers lie in \(\overline B(z_j,r_j)\), so \(d(z_k,z_l)\leq2r_j\to0\). Completeness gives a limit \(z\). For each \(j\), the entire tail lies in that closed ball; continuity of distance gives \(z\in\overline B(z_j,r_j)\). The first inclusion puts \(z\) in \(V\), and each successive inclusion puts it in \(U_j\). Hence \(V\cap\bigcap_jU_j\ne\varnothing\). This proves density. If \(Z\) is empty, the assertion is true by the definition of density, and no ball is chosen. Neither separability nor local compactness is required. Garrett's cited Theorem 4.0.1 and the nested-ball argument in Section 1 of From Weyl symbols to operators and changes of coordinates are comparisons; the complete proof above supplies this input here.

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
contradicting its selection. Now take a finite cover of \(K\) by \(\delta/2\)-balls. For each center, choose a member of \(\mathcal U\) containing its \(\delta\)-ball; this finite list covers \(K\). Therefore \(K\) is compact. This proves the equivalence for the actual metric, without assuming completeness or any countability of the given cover. Lebl's linked metric-space chapter gives the classical comparison. The finite-dimensional Heine–Borel consequence, including its exercise step, is proved in Section 4 of Metric and topological foundations and supplies the input used in Section 2 here.

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

These tools support later finite-dimensional defect splittings, operator-valued estimates and compact parameter arguments. They do not provide a bounded linear right inverse for every surjection: the open-mapping proof selects preimages without a linear selection rule. Such a conclusion requires a complemented kernel. Passing from Banach spaces to Fréchet spaces likewise requires an open-mapping or closed-graph argument with its actual topologies. The complete-metric Baire theorem remains useful there, while the norm estimates in Sections 7–8 cannot simply be renamed. Vector-valued integration and reflexive-space duality require separate proofs or exact imports.

## References

- Paul Garrett, [Review of metric spaces](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2012-13/01_metric_spaces.pdf), Theorem 4.0.1, 2 February 2014; [Banach Spaces](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2016-17/02_banach.pdf), 13 November 2017, cited propositions and theorems.
- Jiří Lebl, [Basic Analysis, metric-space chapter](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-metric.tex#L2217-L2406), pinned author-source revision.
- Mathlib, [Hahn–Banach module](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/Mathlib/Analysis/Normed/Module/HahnBanach.lean), pinned source revision.
