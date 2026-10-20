# Operator completeness and open mapping

*Sections 3 and 8 of the earlier programme lesson **Banach estimates, quotient spaces and compact parameter arguments**, AN03-P004. Programme credits and the CC0 dedication are retained in the accompanying notices. Selection by GPT-6 Astra (OpenAI), October 2026.*

These proofs supply complete operator spaces, summable vector series and bounded inverses of Banach-space isomorphisms. The [functional foundation](functional-foundations-U008.md), Section 6, supplies the complete-metric Baire theorem. Scalar completeness and geometric series are proved in the [scalar foundation](metric-foundation-bridges.md), Sections 12–13.

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

## 8. Open mapping through summable corrections

Let \(T:X\to Y\) be a bounded surjective linear map between Banach spaces. We show that a fixed ball about zero in \(Y\) lies in the image of the closed unit ball of \(X\). If \(Y=\{0\}\), this holds for every positive radius, so suppose otherwise. Write \(B_X\) for the open unit ball. Surjectivity gives
\[
Y=\bigcup_{n\geq1}\overline{T(nB_X)}.
\]
By the [Baire theorem, Section 6](functional-foundations-U008.md#6-baire-s-theorem-for-complete-metric-spaces), applied to \(Y\), some closed set on the right contains \(B_Y(y_0,r)\), where \(r>0\). If \(\|y\|<r\), approximate both \(y_0+y\) and \(y_0\) by images of vectors in \(nB_X\). Their differences approximate \(y\) by images of vectors in \(2nB_X\). Consequently
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
