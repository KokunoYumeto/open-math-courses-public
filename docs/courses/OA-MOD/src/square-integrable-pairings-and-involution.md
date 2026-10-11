# Square-integrable pairings and strong involution

Two families of tests recover two different norms. Pairing a bounded operator with the square-integrable unit ball detects its square integrability. Pairing a square-integrable operator with the trace-norm unit ball detects its boundedness. These tests also clarify why a square-integrable factor can repair the discontinuity of adjoint in the strong topology.

Until LQ-04, let \(M\) be a von Neumann algebra with a faithful normal semifinite trace \(\tau\). No separability, sigma-finiteness or finiteness of \(\tau(1)\) is assumed. We allow the zero algebra. Use the bounded trace ideals
\[
 \begin{gathered}
 \mathfrak n_\tau=\{a\in M:\tau(a^*a)<\infty\},\\
 \mathfrak m_\tau=\{a\in M:\tau(|a|)<\infty\}.
 \end{gathered}
\]
The actual measurable-operator space \(L^2=L^2(M,\tau)\), its bounded module actions and its approximation by bounded finite-support operators were constructed in Complete norms on actual measurable operators. In particular, \(M\cap L^2=\mathfrak n_\tau\), and \(\mathfrak m_\tau\subseteq\mathfrak n_\tau\). Its inner product is linear in the first variable:
\[
 \langle x,y\rangle_2=\tau(y^*x).
\]
The trace Hilbert space proves this formula and the Cauchy–Schwarz inequality. Products of two \(L^2\) elements lie in \(L^1\), by Hölder's inequality and cyclicity. Products of measurable operators mean the closed products constructed there.

## Testing a bounded operator for square integrability

For \(x\in M\), put
\[
 \begin{gathered}
 A_x=\sup\{\,|\tau(y^*x)|:\\
 y\in\mathfrak m_\tau,\ \|y\|_2\leq1\,\}.
 \end{gathered}
\]
Every tested trace exists even before we know that \(x\in L^2\): the bounded finite trace ideal is a two-sided star ideal.

**Theorem.** With extended nonnegative values,
\[
 A_x=\tau(x^*x)^{1/2}.
 \tag{LQ.1}
\]
Consequently \(x\in\mathfrak n_\tau\) if and only if \(A_x<\infty\), and then \(A_x=\|x\|_2\).

**Proof.** Let \(e\) be any finite-trace projection and put \(y=xe\). Its right support is at most \(e\), so \(y\) lies in the finite-support ideal \(\mathfrak m_0\subseteq\mathfrak m_\tau\). Set \(t=\|xe\|_2\). The bounded cyclic trace identities in TB-01 give
\[
 \begin{gathered}
 \tau(y^*x)=\tau(ex^*x)\\
 =\tau(ex^*xe)=\tau(xex^*)=t^2.
 \end{gathered}
\]
For example, cyclically moving the last \(e\) in \(ex^*xe\) gives \(\tau(ex^*x)\). All these products lie in the finite trace ideal. If \(t>0\), testing with \(y/t\) yields \(A_x\geq t\). For \(t=0\) the same inequality holds automatically.

By Finite pieces without a countability assumption, the directed net of all finite-trace projections satisfies \(e\uparrow1\). Thus \(xex^*\uparrow xx^*\), and normality and the trace identity give
\[
 \begin{gathered}
 \sup_e\|xe\|_2^2=\tau(xx^*)\\
 =\tau(x^*x).
 \end{gathered}
\]
This proves the lower bound in (LQ.1), including the case of an infinite right side. If \(\tau(x^*x)<\infty\), Cauchy–Schwarz gives
\[
 |\tau(y^*x)|\leq\|y\|_2\|x\|_2,
\]
which proves the opposite bound. The zero operator and zero algebra cause no exception. \(\square\)

## Testing a square-integrable vector for boundedness

For \(x\in L^2\), define
\[
 \begin{gathered}
 B_x=\sup\{\,|\langle x,y\rangle_2|:\\
 y\in\mathfrak m_\tau,\ \|y\|_1\leq1\,\},\\
 D_x=\sup\{\,\|ax\|_2:\\
 a\in\mathfrak n_\tau,\ \|a\|_2\leq1\,\}.
 \end{gathered}
\]
The second definition makes sense for every \(x\in L^2\), because each \(a\in\mathfrak n_\tau\) is bounded and hence acts on \(L^2\).

**Theorem.** The following conditions are equivalent: \(x\) is bounded; \(B_x<\infty\); \(D_x<\infty\). When they hold,
\[
 B_x=D_x=\|x\|.
 \tag{LQ.2}
\]
Equivalently, either finite testing constant characterizes membership in \(\mathfrak n_\tau\) among all \(L^2\) vectors.

**The upper bounds for bounded vectors.** If \(x\) is bounded, The trace norm and the dual pairing gives
\[
 |\tau(y^*x)|\leq\|y^*\|_1\|x\|
 =\|y\|_1\|x\|.
\]
The bounded right module estimate of TI-09 gives
\[
 \|ax\|_2\leq\|a\|_2\|x\|.
\]
Thus both testing constants are at most \(\|x\|\).

**Finite spectral tests.** Write the measurable polar decomposition as \(x=uk\), where \(k=|x|\) and \(u^*u=s(k)\). Its existence and spectral calculus are proved in Positivity, square roots and polar decomposition. For \(c>0\), put
\[
 e=1_{(c,\infty)}(k).
\]
The positive spectral integral gives
\[
 c^2\tau(e)\leq\tau(k^2)<\infty.
\]
If \(e\ne0\), then \(0<\tau(e)<\infty\). Two normalized tests are
\[
 \begin{gathered}
 y_e=\frac{ue}{\tau(e)},\\
 a_e=\frac{eu^*}{\sqrt{\tau(e)}}.
 \end{gathered}
 \tag{LQ.3}
\]
Since \(e\leq u^*u\), we have \(|ue|=e\), and \(ueu^*\) is a projection of trace \(\tau(e)\). The two supports of \(ue\) and \(eu^*\) therefore have finite trace. In particular,
\[
 \begin{gathered}
 y_e\in\mathfrak m_0,\quad \|y_e\|_1=1,\\
 a_e\in\mathfrak n_\tau,\quad \|a_e\|_2=1.
 \end{gathered}
\]
For the second norm identity, \(a_e^*a_e=ueu^*/\tau(e)\).

These tests have the exact values
\[
 \begin{gathered}
 \langle x,y_e\rangle_2\\
 =\frac{\tau(ek)}{\tau(e)}\geq c,\\
 \|a_ex\|_2^2\\
 =\frac{\tau(k^2e)}{\tau(e)}\geq c^2.
 \end{gathered}
 \tag{LQ.4}
\]
Here \(ek\in L^1\): both \(e\) and \(k\) are in \(L^2\), and their product is integrable by TI-10. Thus the first trace is defined. The identities follow from \(e u^*u=e\), spectral commutation, and the closed products \(y_e^*x=ek/\tau(e)\) and \(a_ex=ek/\sqrt{\tau(e)}\). The second product belongs to \(L^2\); its squared modulus is \(k^2e/\tau(e)\). No unverified trace of an unbounded product is being used.

If \(B_x=C<\infty\), choose \(c=C+\varepsilon\) in this construction. A nonzero \(e\) would contradict the first inequality in (LQ.4). Hence \(1_{(C+\varepsilon,\infty)}(k)=0\) for every \(\varepsilon>0\), which implies \(k\leq C\) by spectral calculus. Thus \(x\) is bounded. If instead \(D_x=C<\infty\), the second inequality yields the identical conclusion. This proves both converses independently.

Finally, if \(x\ne0\) is bounded and \(0<c<\|x\|\), the spectral projection \(e\) above is nonzero. Formula (LQ.4) gives \(B_x\geq c\) and \(D_x\geq c\). Letting \(c\uparrow\|x\|\) proves (LQ.2). If \(x=0\), all three numbers are zero. \(\square\)

The adjoints in (LQ.3) have different orientations: \(y_e\) is tested through \(y_e^*x\), whereas \(a_e\) is tested through \(a_ex\). The argument therefore applies to arbitrary complex operators, without positivity of \(x\).

## A square-integrable factor and the strong topology

The sigma-strong topology on \(M\) is generated by
\[
 p_\varphi(b)=\varphi(b^*b)^{1/2},
 \qquad \varphi\in M_*^+.
\]
The sigma-strong seminorms proves this description and its equivalence with vector seminorms. We first relate it to the square-integrable norm.

**Lemma.** If \(b_i\in\mathfrak n_\tau\), \(\sup_i\|b_i\|\leq K<\infty\), and \(\|b_i\|_2\to0\), then \(b_i\to0\) sigma-strongly in \(M\).

**Proof.** Fix \(\varphi\in M_*^+\). The positive trace-density representation supplies \(h\in L^1_+\) such that \(\varphi(z)=\tau(hz)\). By The complete integrable space, its spectral cutoffs
\[
 h_n=h1_{[1/n,n]}(h)
\]
are bounded, positive and integrable, with \(\|h-h_n\|_1\to0\). The trace pairing bound and bounded cyclicity imply
\[
 \begin{gathered}
 0\leq\varphi(b_i^*b_i)\\
 \leq K^2\|h-h_n\|_1\\
 {}+\|h_n\|\,\|b_i\|_2^2.
 \end{gathered}
 \tag{LQ.5}
\]
For the last term, cyclicity gives
\[
 \begin{gathered}
 \tau(h_n b_i^*b_i)=\tau(b_i h_n b_i^*),\\
 0\leq b_i h_n b_i^*\leq\|h_n\|b_i b_i^*.
 \end{gathered}
\]
Every positive operator in this inequality has finite trace, and \(\tau(b_i b_i^*)=\|b_i\|_2^2\). Given a positive error tolerance, first choose \(n\) so that the first term of (LQ.5) is small, and then a tail of the original net so that its second term is small. If \(K=0\), the conclusion is immediate. It follows that \(p_\varphi(b_i)\to0\) for every \(\varphi\). \(\square\)

**Theorem.** For every fixed \(a\in\mathfrak n_\tau\), the map
\[
 \begin{gathered}
 M\longrightarrow M,\\
 x\longmapsto ax^*
 \end{gathered}
 \tag{LQ.6}
\]
is sigma-strongly continuous on every operator-norm-bounded subset of \(M\).

**Proof.** First suppose that \(x_i\to0\) sigma-strongly and \(\sup_i\|x_i\|\leq K\). The element \(a^*a\) is bounded, positive and integrable. The bounded trace-density representation therefore gives a positive normal functional
\[
 \psi(z)=\tau(a^*az).
\]
Bounded cyclicity and the definition of sigma-strong convergence give
\[
 \begin{gathered}
 \|ax_i^*\|_2^2=\tau(x_i a^*a x_i^*)\\
 =\psi(x_i^*x_i)\longrightarrow0.
 \end{gathered}
\]
Moreover, \(ax_i^*\in\mathfrak n_\tau\) and \(\|ax_i^*\|\leq\|a\|K\). The lemma now proves \(ax_i^*\to0\) sigma-strongly in \(M\), the required target topology.

For a net \(x_i\to x\) in a fixed norm-bounded subset, apply this argument to \(x_i-x\), which remains uniformly bounded. Since \(a(x_i-x)^*=ax_i^*-ax^*\), the conclusion is continuity at every point of that subset. \(\square\)

The equality involving \(\psi\) already proves convergence in \(L^2\). The lemma is the additional step that proves convergence in the algebra itself.

## Adjoint is discontinuous in an infinite corner

This section needs no trace. Let \(M\) be any von Neumann algebra and let \(e\in M\) be an infinite projection. By the definition of infiniteness, there is a partial isometry \(v\in eMe\) with
\[
 v^*v=e,\qquad vv^*<e.
\]
Here \(e\) is the identity of the corner.

**Theorem.** Adjoint on the operator-norm unit ball of \(eMe\) is not sigma-strongly continuous at zero.

**Proof.** Put \(p=e-vv^*\), a nonzero projection. We have \(pv=0\) and \(v^*p=0\). For integers \(n\geq0\), with \(v^0=e\), define
\[
 \begin{gathered}
 w_n=v^np,\\
 q_n=w_nw_n^*,\\
 z_n=w_n^*.
 \end{gathered}
 \tag{LQ.7}
\]
Because \((v^*)^n v^n=e\), one has \(w_n^*w_n=p\); thus \(q_n\) is a projection and \(\|z_n\|=1\). For \(n<m\),
\[
 w_n^*w_m=pv^{m-n}p=0,
\]
so \(q_nq_m=0\). The projections \(q_n\) are pairwise orthogonal and their finite sums are at most \(e\).

For every positive normal functional \(\varphi\) on \(eMe\),
\[
 \sum_{n=0}^N\varphi(q_n)\leq\varphi(e).
\]
The nonnegative scalar terms consequently tend to zero. Since
\[
 \begin{gathered}
 z_n^*z_n=q_n,\\
 z_nz_n^*=p,
 \end{gathered}
 \tag{LQ.8}
\]
the sigma-strong seminorm formula of CP-08 gives \(z_n\to0\).

On the other hand, choose a nonzero vector \(\xi\in pH\) in a faithful concrete representation of the corner. Its vector functional \(\psi(b)=\langle b\xi,\xi\rangle\) is positive and normal, as proved in The concrete predual. Then
\[
 p_\psi(z_n^*)^2=\psi(p)=\|\xi\|^2>0
\]
for every \(n\). Hence \(z_n^*\) does not converge sigma-strongly to zero. This sequence in the unit ball proves the asserted discontinuity. \(\square\)

The construction uses the given infinite projection itself. Neither proper infiniteness of \(e\) nor a countability assumption on \(M\) is needed.

## Three tests of the hypotheses

**A bounded operator that is not square integrable.** Let \(M=\ell^\infty(\mathbb N)\) with counting trace, and let \(x=1\). The trace is faithful and normal because coordinate suprema commute with each finite coordinate sum; taking the supremum over finite sets gives the full sum. Finite coordinate truncations prove semifiniteness. If \(e_N\) projects onto the first \(N\) coordinates, then
\[
 \begin{gathered}
 y_N=N^{-1/2}e_N\in\mathfrak m_\tau,\\
 \|y_N\|_2=1,\qquad \tau(y_N^*x)=\sqrt N.
 \end{gathered}
\]
Thus \(A_x=\infty\), in agreement with \(\tau(x^*x)=\infty\).

**A square-integrable operator that is not bounded.** On the same diagonal algebra, put
\[
 \tau(b)=\sum_{n\geq1}8^{-n}b_n\qquad(b\geq0).
\]
This trace is faithful, normal by the same finite-sum argument, and finite with \(\tau(1)=1/7\); finiteness implies semifiniteness. Let \(x\) be the diagonal operator with entries \(2^n\), on its maximal domain
\[
 D(x)=\{\xi:\sum_{n\geq1}4^n|\xi_n|^2<\infty\}.
\]
Finite-coordinate vectors prove domain density. Coordinate convergence of a vector and its image proves closedness, and the diagonal spectral projections give affiliation. The trace of each high spectral tail tends to zero, so The spectral-tail criterion makes \(x\) measurable. Its squared norm is
\[
 \|x\|_2^2=\sum_{n\geq1}2^{-n}=1.
\]
For the coordinate projection \(q_n\), set
\[
 y_n=8^n q_n,\qquad a_n=8^{n/2}q_n.
\]
Direct evaluation gives
\[
 \begin{gathered}
 \|y_n\|_1=1,\quad \langle x,y_n\rangle_2=2^n,\\
 \|a_n\|_2=1,\quad \|a_nx\|_2=2^n.
 \end{gathered}
\]
Both testing constants in LQ-02 are infinite although \(x\) is a unit vector in \(L^2\).

**The shift version of the infinite-corner sequence.** On \(\ell^2(\mathbb N_0)\), let \(v\delta_n=\delta_{n+1}\). Then \(v^*v=1\), \(p=1-vv^*=E_{00}\), and the construction in LQ-04 gives
\[
 q_n=E_{nn},\qquad z_n=E_{0n}.
\]
For each \(\xi\in\ell^2\), \(\|z_n\xi\|=|\xi_n|\to0\); hence \(z_n\to0\) strongly. Since the sequence is uniformly bounded, CP-08 also gives sigma-strong convergence. But \(z_n^*\delta_0=\delta_n\) has norm one for every \(n\). With the usual trace and \(a=p\), one has \(az_n^*=0\) for all \(n\geq1\). This directly illustrates how the square-integrable factor in LQ-03 changes the continuity behavior.

The corresponding testing and topology statements are Lemmas V.2.20–2.21 and V.2.27–2.28 of M. Takesaki, *Theory of Operator Algebras I*, printed pp. 323–324 and 326–327.
