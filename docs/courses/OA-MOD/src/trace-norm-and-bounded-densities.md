# The trace norm and bounded densities

A normal functional can have an unbounded density. Its usual norm measures the integral of that density, while its size on the trace-norm unit ball measures the density's operator norm. We establish both statements and identify exactly when the second quantity is finite.

Throughout, \(M\) is a von Neumann algebra and \(\tau\) is a faithful normal semifinite trace. The Hilbert space and the algebra may be nonseparable, and \(\tau(1)\) may be infinite. The zero algebra is allowed. Write \(\mathfrak m_\tau\) for the bounded finite trace ideal. We use the actual measurable-operator space \(L^1(M,\tau)\) constructed in Trace densities and noncommutative integration, with norm \(\|h\|_1=\tau(|h|)\). Its bounded finite-support subideal is denoted by \(\mathfrak m_0\).

## Completion and the dual pairing

**Theorem.** Completion of \(\mathfrak m_\tau\) in its trace norm gives \(L^1(M,\tau)\). The trace pairing defines an onto complex-linear isometry
\[
 \begin{gathered}
 J:L^1\longrightarrow M_*,\\
 J(h)(a)=\tau(ha).
 \end{gathered}
 \tag{TN.1}
\]
Consequently canonical evaluation gives an onto complex-linear isometry
\[
 \begin{gathered}
 M\longrightarrow (L^1)^*,\\
 a\longmapsto F_a,\\
 F_a(h)=\tau(ha).
 \end{gathered}
 \tag{TN.2}
\]
The pairing is bilinear. In particular, no adjoint or complex conjugation is silently inserted into the representing density.

**Proof.** The bounded-density calculation proves that \(J_0(x)(a)=\tau(xa)\) belongs to \(M_*\) for \(x\in\mathfrak m_\tau\), with
\[
 \|J_0(x)\|=\tau(|x|).
\]
That proof includes normality for increasing nets and the passage from positive to arbitrary complex densities. The completion theorem proves that the actual measurable space \(L^1\) is complete and that \(\mathfrak m_\tau\) is dense in it. Thus \(J_0\) extends to an isometry \(J:L^1\to M_*\); its range is closed. Completeness and norm-closedness of the concrete predual are proved in The concrete predual and its intrinsic norm.

The bounded trace inequality extends \(\tau\) continuously from \(\mathfrak m_\tau\) to \(L^1\). The bounded module estimates in the completion theorem show that \(h\mapsto ha\) is continuous in trace norm. Passing to the limit from \(J_0\) therefore gives exactly the formula in (TN.1).

To prove that the range is all of \(M_*\), suppose it were a proper closed subspace \(Y\). Choose \(\varphi\notin Y\) and put \(d=\operatorname{dist}(\varphi,Y)>0\). The functional \(y+t\varphi\mapsto t\) on \(Y+\mathbb C\varphi\) is bounded by \(1/d\). The Hahn–Banach norm extension extends it to a nonzero element of \((M_*)^*\) annihilating \(Y\). By CP-06, this functional is evaluation at some nonzero \(a\in M\). Hence
\[
 \tau(xa)=0
 \qquad(x\in L^1).
\]
For every finite-trace projection \(e\), the element \(x=ea^*\) belongs to \(\mathfrak m_\tau\). Bounded cyclicity gives
\[
 \begin{gathered}
 0=\tau(ea^*a)=\tau(aea^*),\\
 aea^*=(ae)(ae)^*.
 \end{gathered}
\]
Faithfulness implies \(ae=0\). Finite pieces without a countability assumption proves that all finite-trace projections, ordered by inclusion, increase strongly to \(1\). It follows that \(a=0\), a contradiction. Thus \(J\) is onto.

Now let \(F\in(L^1)^*\). The functional \(F\circ J^{-1}\) belongs to \((M_*)^*\), with the same norm. CP-06 gives a unique \(a\in M\) such that
\[
 \begin{gathered}
 (F\circ J^{-1})(\varphi)=\varphi(a),\\
 \|a\|=\|F\|.
 \end{gathered}
\]
Substituting \(\varphi=J(h)\) proves (TN.2), including surjectivity, uniqueness and the exact norm. \(\square\)

The trace extension and its cyclicity give, for \(a,b\in M\) and \(h\in L^1\),
\[
 \begin{gathered}
 \|ahb\|_1\leq\|a\|\,\|h\|_1\,\|b\|,\\
 J(ah)(b)=J(h)(ba),\\
 J(ha)(b)=J(h)(ab).
 \end{gathered}
\]
In particular,
\[
 \tau(ha)=\tau(ah).
 \tag{TN.3}
\]
For the first functional identity, \(\tau(ahb)=\tau(hba)\); the second follows directly from associativity. These formulas explain the left and right actions without an ambiguous dual-module convention. The notation \(L^\infty(M,\tau)=M\) uses its original operator norm. It does not assert that every element of \(M^*\) is normal: \(L^1\) is the predual of \(M\), while (TN.2) identifies the dual of \(L^1\).

## The bounded-density criterion

For a normal complex functional \(\omega\in M_*\), define
\[
 \begin{gathered}
 C_\omega=\sup\{\,|\omega(y)|:\\
 y\in\mathfrak m_\tau,\ \|y\|_1\leq1\,\}.
 \end{gathered}
\]
The value may be infinite. By (TN.1), there is a unique \(h\in L^1\) with \(\omega=J(h)\).

**Theorem.** The density \(h\) is bounded if and only if \(C_\omega<\infty\). In that case
\[
 \begin{gathered}
 h\in\mathfrak m_\tau=M\cap L^1,\\
 C_\omega=\|h\|,\\
 \|\omega\|=\|h\|_1.
 \tag{TN.4}
 \end{gathered}
\]
Thus boundedness of \(\omega\) on the operator-norm unit ball and boundedness on the trace-norm unit ball are distinct conditions.

**Bounded densities give the estimate.** If \(h\in M\cap L^1\), then \(\tau(|h|)<\infty\), which is exactly membership in the bounded ideal; see Finite trace ideals. The bounded trace estimate gives
\[
 |\omega(y)|=|\tau(hy)|
 \leq\|h\|\,\|y\|_1.
\]
Hence \(C_\omega\leq\|h\|\). The last equality in (TN.4) is (TN.1).

**A finite supremum forces boundedness.** Suppose \(C=C_\omega<\infty\), and write the measurable polar decomposition as \(h=uk\), where \(k=|h|\geq0\), \(u\in M\), and \(u^*u=s(k)\). Fix \(\varepsilon>0\) and let
\[
 e=1_{(C+\varepsilon,\infty)}(k).
\]
The positive spectral integral gives
\[
 (C+\varepsilon)\tau(e)\leq\tau(k)<\infty.
\]
If \(e\ne0\), faithfulness yields \(0<\tau(e)<\infty\). Define the bounded test element
\[
 y=\frac{eu^*}{\tau(e)}.
 \tag{TN.5}
\]
Because \(e\leq u^*u\), the operator \(ueu^*\) is a projection equivalent to \(e\). The partial isometry \(eu^*\) has absolute value \(ueu^*\), so
\[
 \tau(|y|)=\frac{\tau(ueu^*)}{\tau(e)}=1.
\]
Both supports have finite trace. Thus \(y\in\mathfrak m_0\subseteq\mathfrak m_\tau\), and it is an admissible test in the definition of \(C\).

All ensuing traces exist: \(h\in L^1\), and multiplication by any bounded element preserves \(L^1\). Cyclicity from TI-06, the identity \(e\leq u^*u\), and spectral commutation give
\[
 \begin{gathered}
 \omega(y)=\frac{\tau(ukeu^*)}{\tau(e)}\\
 =\frac{\tau(ke)}{\tau(e)}
 \geq C+\varepsilon.
 \tag{TN.6}
 \end{gathered}
\]
The last trace is a nonnegative spectral integral. This contradicts \(|\omega(y)|\leq C\). Therefore every such \(e\) is zero, and spectral calculus implies \(0\leq k\leq C\). Hence \(h\) is bounded, with \(\|h\|\leq C\), and its known integrability puts it in \(\mathfrak m_\tau\).

**The constant is exact.** It remains to obtain the reverse inequality in the first direction. If \(h\ne0\), choose \(0<c<\|h\|\) and put \(e=1_{(c,\infty)}(|h|)\). This is nonzero; the estimate \(c\tau(e)\leq\tau(|h|)\) makes it finite. Using (TN.5) with this \(e\), the same calculation gives \(\|y\|_1=1\) and \(\omega(y)\geq c\). Letting \(c\uparrow\|h\|\) gives \(C_\omega\geq\|h\|\). If \(h=0\), both sides are zero. This proves every assertion of (TN.4). \(\square\)

The spectral test uses a finite projection belonging to one particular density. It does not require the whole algebra to have a countable finite-trace exhaustion. Normality of \(\omega\) is used when (TN.1) supplies its density; that hypothesis is part of the theorem.

## Bounded approximants and their two norms

Every normal functional is a norm limit of functionals with bounded integrable densities. Indeed, for \(h=uk\in L^1\) set
\[
 \begin{gathered}
 p_n=1_{[1/n,n]}(k),\\
 h_n=hp_n,\\
 \omega_n=J(h_n).
 \tag{TN.7}
 \end{gathered}
\]
The spectral approximation proved in The complete integrable space gives \(h_n\in\mathfrak m_0\) and \(\|h-h_n\|_1\to0\). Therefore
\[
 \|\omega-\omega_n\|=\|h-h_n\|_1\longrightarrow0.
\]
This approximation does not supply a common bound for \(C_{\omega_n}\). In fact, if such a bound \(K\) exists, then for every \(y\in\mathfrak m_\tau\), norm convergence of the functionals gives
\[
 |\omega(y)|=\lim_n|\omega_n(y)|
 \leq K\|y\|_1.
\]
TN-02 then forces \(h\) to be bounded. Conversely, if \(h\) is bounded, these spectral approximants satisfy \(\|h_n\|\leq\|h\|\), so \(C_{\omega_n}\leq\|h\|\). The zero density is included.

**A normal functional whose density is unbounded.** Let \(M=\ell^\infty(\mathbb N)\) act diagonally on \(\ell^2(\mathbb N)\), with indices starting at one, and put
\[
 \tau(a)=\sum_{n\geq1}4^{-n}a_n
 \qquad(a\geq0).
\]
This is faithful and finite, with \(\tau(1)=1/3\). It is normal: for an increasing bounded net, the finite coordinate sums commute with its supremum, and then taking the supremum over finite coordinate sets gives the full sum. Every positive bounded element has finite trace, so semifiniteness also holds.

The diagonal operator \(h\) with entries \(2^n\) has maximal domain
\[
 D(h)=\{\xi:\sum_{n\geq1}4^n|\xi_n|^2<\infty\}.
\]
Finite-coordinate vectors form a dense domain. Coordinate convergence proves closedness, and the diagonal spectral projections give affiliation. Its high spectral tails have trace tending to zero, so it is measurable by The spectral-tail criterion. Moreover
\[
 \tau(h)=\sum_{n\geq1}2^{-n}=1.
\]
Thus \(\omega=J(h)\) is a normal positive functional of norm one. If \(q_n\) is the coordinate projection, then \(y_n=4^nq_n\) has trace norm one, whereas
\[
 \omega(y_n)=2^n.
\]
Hence \(C_\omega=\infty\). Put \(h^{(N)}=\sum_{n=1}^N2^nq_n\) and \(\omega_N=J(h^{(N)})\). These bounded densities satisfy the exact formulas
\[
 \begin{gathered}
 \|\omega-\omega_N\|=2^{-N},\\
 C_{\omega_N}=2^N.
 \tag{TN.8}
 \end{gathered}
\]
The functional error tends to zero while the density norms grow without bound.

**A complex matrix density.** On \(M_2(\mathbb C)\), take \(\tau=\tfrac12\operatorname{Tr}\) and \(h=E_{12}\). Then \(|h|=E_{22}\), so
\[
 \|h\|=1,\qquad \|J(h)\|=\tfrac12.
\]
The test \(y=2E_{21}\) satisfies \(\|y\|_1=1\) and \(J(h)(y)=1\). The upper estimate in TN-02 therefore gives \(C_{J(h)}=1\). This verifies the distinction between the two norms for a nonpositive density as well.

For further reading, the abstract trace-predual identification and the bounded-density criterion are Theorem V.2.18 and Proposition V.2.19 of M. Takesaki, *Theory of Operator Algebras I*, printed p. 321. Their trace-norm preliminaries occupy printed pp. 319–320.
