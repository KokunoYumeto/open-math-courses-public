# Trace defects and graph cores

A projection whose complement has small trace retains enough information to determine a closed affiliated operator. The information must include domains as well as values. We begin with the scalar functionals that detect a normal semifinite trace, then turn trace estimates into projection and graph uniqueness. This also supplies graph cores and a self-adjointness test.

Throughout, \(M\subseteq B(H)\) is a unital von Neumann algebra on an arbitrary complex Hilbert space. No separability or sigma-finiteness is assumed. Inner products are linear in the first variable. The zero algebra and zero Hilbert space are included. Traces take values in \([0,\infty]\), with the scalar convention \(0\cdot\infty=0\).

## A trace as a sum of normal positive functionals

**Theorem.** Every normal semifinite trace \(\tau\), including a nonfaithful or zero trace, can be written on \(M_+\) as a sum of bounded normal positive linear functionals. Consequently it is lower semicontinuous on \(M_+\) for the ultraweak topology.

**Projections of finite trace fill the unit.** Choose a maximal orthogonal family \((e_j)_{j\in J}\) of nonzero projections with \(\tau(e_j)<\infty\). Such families are ordered by inclusion; the union of a chain is again a family, so Zorn's lemma applies. Their join is one. Indeed, if its complement \(r\) were nonzero, the order characterization of semifiniteness would give \(0\ne b\leq r\) with finite trace. For some \(\delta>0\), the spectral projection \(f=1_{[\delta,\infty)}(b)\) is nonzero, lies under \(r\), and satisfies \(\delta\tau(f)\leq\tau(b)\). Adding \(f\) contradicts maximality. These spectral projections are supplied by bounded Borel spectral calculus. They belong to \(M\): bounded continuous approximations to the interval indicator give elements of \(M\) by continuous calculus, and their strong limit belongs to the strongly closed algebra \(M\). This argument uses no faithfulness of \(\tau\).

For each \(j\), the restriction of \(\tau\) to \(e_jMe_j\) has finite value at its identity. Its positive linear extension is bounded by the finite-trace construction, and is normal because increasing positive nets in the corner are increasing nets in \(M\). Composing it with compression gives a normal positive linear functional \(\phi_j\) on \(M\), with
\[
 \begin{gathered}
 \phi_j(x)=\\
 \tau(e_jxe_j),\\
 x\in M_+,\\
 \|\phi_j\|=\tau(e_j).
 \end{gathered}
 \tag{TD.1}
\]
Compression is normal by the fixed multiplication tests; equivalently it preserves bounded increasing positive limits directly on vectors. The scalar normality criterion identifies preservation of bounded increasing positive suprema with ultraweak continuity for these bounded positive functionals. The extension to all of \(M\) is the bounded linear compression followed by the corner functional.

Let \(F\) range over the finite subsets of \(J\), and put \(e_F=\sum_{j\in F}e_j\). Then \(e_F\uparrow1\) strongly. For \(x\geq0\), the trace identity applied to \(e_jx^{1/2}\), followed by finite additivity, gives
\[
 \begin{gathered}
 \sum_{j\in F}\phi_j(x)\\
 =\sum_{j\in F}\tau(x^{1/2}e_jx^{1/2})\\
 =\tau(x^{1/2}e_Fx^{1/2}).
 \end{gathered}
\]
The positive operators on the last line increase to \(x\). Normality therefore proves
\[
 \begin{gathered}
 \tau(x)=\\
 \sum_{j\in J}\phi_j(x).
 \end{gathered}
 \tag{TD.2}
\]
The sum means the supremum of finite subsums, not a countable enumeration. Every finite subsum is ultraweakly continuous on \(M_+\). Its supremum is lower semicontinuous: for a finite real \(a\), the set where that supremum exceeds \(a\) is the union of the open sets where individual finite subsums exceed \(a\). This also covers \(\tau(x)=\infty\). Zero summands may be omitted; for the zero trace the empty sum is allowed. \(\square\)

The functionals \(\phi_j\) need not themselves be traces on \(M\). Their construction uses corners of finite trace, whose projections need not be central. With a nonfaithful trace, such a corner need not be a finite von Neumann algebra.

## Projections detected outside small complements

For this and the next two sections, let \(\tau\) be faithful, normal and semifinite. The projection comparison estimate says that if \(e\wedge p=0\), then \(e\precsim1-p\), hence \(\tau(e)\leq\tau(1-p)\). To recall its concrete reason, the bounded operator \((1-p)e\) has zero kernel on \(eH\); its polar partial isometry has initial projection \(e\) and final projection at most \(1-p\). Equivalent projections have equal trace.

For arbitrary projections \(e,p\), the projection \(r=e-(e\wedge p)\) has zero intersection with \(p\). The same argument gives the more convenient form
\[
 \begin{gathered}
 e-(e\wedge p)\\
 \precsim1-p,\\
 \tau(e-(e\wedge p))\\
 \leq\tau(1-p).
 \end{gathered}
 \tag{TD.3}
\]
No subtraction of two infinite trace values appears here: the difference inside the trace is a projection.

**Zero-intersection test.** If for every \(\varepsilon>0\) there is \(p\in\operatorname{Proj}(M)\) with \(\tau(1-p)<\varepsilon\) and \(e\wedge p=0\), then \(e=0\). The preceding estimate makes \(\tau(e)\) smaller than every positive number, and faithfulness finishes the proof.

**Equal-intersection test.** If for every \(\varepsilon>0\) there is such a \(p\) with \(e\wedge p=f\wedge p\), then \(e=f\). Put \(r=e-(e\wedge f)\). A vector in \(rH\cap pH\) belongs to \((e\wedge p)H=(f\wedge p)H\), hence to \((e\wedge f)H\), and also to its orthogonal complement. Thus \(r\wedge p=0\), and the zero-intersection test gives \(r=0\). Interchanging \(e,f\) gives both inclusions.

We will also use the faithful normal semifinite matrix trace from matrix amplification theorem: on \(M_k(M)_+\), set \(\tau_k(X)=\sum_{i=1}^k\tau(X_{ii})\). The same projection estimates hold in that algebra. For a bounded row operator \(A:H^2\to H\) with entries in \(M\), let \(k=s(A^*A)\) and \(l=s(AA^*)\). Then
\[
 \tau_2(k)=\tau(l).
 \tag{TD.4}
\]
Indeed, embed the row as an off-diagonal block in \(M_3(M)\), on \(H\oplus H^2\). Its bounded polar decomposition has initial block \(0\oplus k\) and final block \(l\oplus0\). Applying the trace identity to that partial isometry proves (TD.4), including infinite values. This justifies the rectangular dimension comparison used below.

## Graph uniqueness under mutual domain inclusions

A closed operator in this section is not required to have dense domain. Affiliation means invariance of both its domain and action under every unitary of \(M'\). The graph-projection criterion applies with this convention: the orthogonal projection \(g_T\) onto its closed graph belongs to \(M_2(M)\).

For a projection \(p\in M\), define
\[
 \begin{gathered}
 A_T(p)=\{\xi\in D(T)\cap pH:\\
 T\xi\in pH\}.
 \end{gathered}
\]
Thus inverse images under an unbounded operator always include its domain condition.

**Theorem.** Let \(S,T\) be closed affiliated operators. Suppose projections \(p_n\) satisfy \(\tau(1-p_n)\to0\), and, for each \(n\),
\[
 \begin{gathered}
 A_T(p_n)\subseteq D(S),\\
 A_S(p_n)\subseteq D(T),\\
 S\xi=T\xi\\
 \bigl(\xi\in A_T(p_n)\\
 {}\cap A_S(p_n)\bigr).
 \end{gathered}
 \tag{TD.5}
\]
Then \(S=T\), including equality of domains. The sequence need not be increasing.

The assumptions do not state that \(A_T(p_n)=A_S(p_n)\). We instead prove a quantitative one-sided estimate. Fix \(p=p_n\), put \(P=\operatorname{diag}(p,p)\), and let
\[
 \begin{gathered}
 Q=g_T\wedge P,\\
 K=Q(H\oplus H).
 \end{gathered}
\]
The vectors of \(K\) are exactly \((\xi,T\xi)\) with \(\xi\in A_T(p)\). By the first inclusion in (TD.5), the rule
\[
 \begin{gathered}
 L:K\longrightarrow H,\\
 L(\xi,T\xi)=S\xi
 \end{gathered}
\]
is everywhere defined. It has closed graph: if \((\xi_j,T\xi_j)\to(\xi,T\xi)\) in \(K\) and \(S\xi_j\to\eta\), closedness of \(S\) gives \(S\xi=\eta\). The space \(K\) is closed in \(H^2\), hence is a Hilbert space. The complete Banach closed graph theorem therefore makes \(L\) bounded. This application is to all of \(K\), not to an assumed full domain for \(S\).

The bounded extension \(LQ:H^2\to H\) has both entries in \(M\). In fact \(Q\) commutes with \(\operatorname{diag}(u,u)\) for \(u\in\mathcal U(M')\), and affiliation of \(S\) gives \(L\operatorname{diag}(u,u)=uL\) on \(K\). Consequently each entry of \(LQ\) commutes with every such \(u\). The unitary commutation test and bicommutant theorem put those entries in \(M\).

Set \(A=(1-p)LQ\), \(k=s(A^*A)\), and \(Q_0=Q-k\). Since \(A=AQ\), \(k\leq Q\), so \(Q_0\) is a projection. Its vectors are exactly the vectors of \(K\) annihilated by \(A\). The final support of \(A\) is at most \(1-p\). Formula (TD.4) gives
\[
 \tau_2(k)\leq\tau(1-p).
 \tag{TD.6}
\]
For \((\xi,T\xi)\in Q_0H^2\), both \(\xi,T\xi\) lie in \(pH\), and \((1-p)S\xi=0\). Thus \(\xi\in A_T(p)\cap A_S(p)\), where (TD.5) gives \(S\xi=T\xi\). It follows that \(Q_0\leq g_T\wedge g_S\).

By (TD.3) in \(M_2(M)\), the first removal has trace at most \(\tau_2(1-P)=2\tau(1-p)\). The two removed projections \(g_T-Q\) and \(k\) are orthogonal. Therefore
\[
 \begin{gathered}
 \tau_2(g_T-(g_T\wedge g_S))\\
 \leq\tau_2(g_T-Q_0)\\
 =\tau_2(g_T-Q)+\tau_2(k)\\
 \leq3\tau(1-p).
 \end{gathered}
\]
Letting \(n\) tend to infinity gives \(g_T\leq g_S\) by faithfulness. Repeat the argument with \(S,T\) interchanged, using the second domain inclusion. It gives \(g_S\leq g_T\). Equality of graph projections gives equality of the closed operators. \(\square\)

In particular, it suffices that \(p_nH\subseteq D(S)\cap D(T)\) and \(S\xi=T\xi\) on \(p_nH\). These stronger conditions imply all three assertions of (TD.5). This recovers the special case of the earlier graph-uniqueness theorem, while the proof above addresses the weaker mutual-domain assumptions themselves.

## Trace-dense domains are graph cores

Let projections \(e_n\) satisfy \(\tau(1-e_n)\to0\), with no monotonicity assumption, and put
\[
 \mathcal D=\operatorname{span}_{\mathbb C}
 \Bigl(\bigcup_{n\geq1}e_nH\Bigr).
\]
This is dense in \(H\). Indeed the projection \(q=\bigvee_n e_n\) has range \(\overline{\mathcal D}\), and \(\tau(1-q)\leq\tau(1-e_n)\) for every \(n\). Faithfulness gives \(q=1\).

**Graph-core theorem.** If a closed affiliated operator \(T\) has \(\mathcal D\subseteq D(T)\), then \(T\) is the closure of \(T|_{\mathcal D}\). Equivalently, for every \(\xi\in D(T)\) there are \(\xi_j\in\mathcal D\) such that
\[
 \begin{gathered}
 \xi_j\longrightarrow\xi,\\
 T\xi_j\longrightarrow T\xi.
 \end{gathered}
 \tag{TD.7}
\]

**Proof.** The graph of the restriction is contained in the closed graph of \(T\), so its closure is the graph of a closed operator \(T_0\subseteq T\). Explicitly the closure cannot contain \((0,\eta)\) for \(\eta\ne0\), since the graph of \(T\) contains no such vector. Its domain contains the dense subspace \(\mathcal D\). Each \(e_n\in M\) commutes with the unitaries of \(M'\), so \(\mathcal D\) is invariant under them. Affiliation of \(T\) makes the graph of the restriction invariant under their diagonal actions and inverses. The same is true of its closure. Hence \(T_0\) is affiliated, by GP-01. The operators \(T,T_0\) agree on all of \(e_nH\). The last assertion of TD-03 proves \(T=T_0\). Finally, the graph norm is a metric norm; closure of the graph means that one can choose an approximating vector within \(1/j\) for each \(j\). These choices give (TD.7). \(\square\)

**Self-adjointness with trace-dense cutoffs.** If in addition \(T\) is symmetric, then it is self-adjoint. Here symmetry means \(\langle T\xi,\eta\rangle=\langle\xi,T\eta\rangle\) on its domain; density is already guaranteed by \(\mathcal D\). Thus \(T\subseteq T^*\), so \(T^*\) is densely defined as well. It is closed: if \(\eta_j\to\eta\) and \(T^*\eta_j\to v\), taking limits in the defining pairings gives \(\eta\in D(T^*)\) and \(T^*\eta=v\).

The adjoint is affiliated too. For \(u\in\mathcal U(M')\), \(\eta\in D(T^*)\) and \(\xi\in D(T)\), affiliation gives
\[
 \begin{aligned}
 \langle T\xi,u\eta\rangle
 &=\langle Tu^*\xi,\eta\rangle\\
 &=\langle u^*\xi,T^*\eta\rangle\\
 &=\langle\xi,uT^*\eta\rangle.
 \end{aligned}
\]
Hence \(u\eta\in D(T^*)\) and \(T^*u\eta=uT^*\eta\); use \(u^*\) for equality of domains. Both \(T\) and \(T^*\) contain \(e_nH\) in their domains and agree there. TD-03 gives \(T=T^*\), including their domains. Notice that being a graph core for a symmetric operator alone would not prove self-adjointness; the comparison with its adjoint uses affiliation and the small trace complements.

## Self-adjointness in an arbitrary finite algebra

**Theorem.** If \(M\) is finite, every closed densely defined symmetric operator affiliated with \(M\) is self-adjoint. No scalar trace, faithful normal state or countability hypothesis is required.

**Proof.** Put \(A_\pm=T\pm iI\), on exactly \(D(T)\). Symmetry makes \(\langle T\xi,\xi\rangle\) real, so
\[
 \begin{gathered}
 \|A_\pm\xi\|^2\\
 =\|T\xi\|^2+\|\xi\|^2.
 \end{gathered}
 \tag{TD.8}
\]
Thus each \(A_\pm\) is injective. It is closed: if \(\xi_j\to\xi\) and \(A_\pm\xi_j\to y\), then \(T\xi_j\to y\mp i\xi\), so closedness of \(T\) gives the required domain membership and value. Its range is closed as well. A convergent sequence \(A_\pm\xi_j\) makes \(\xi_j\) Cauchy by (TD.8); the preceding closedness argument then identifies the limit in the range. Affiliation is preserved by the scalar shift.

Apply the closed-operator polar decomposition to \(A_\pm\). Its partial isometry \(v_\pm\) lies in \(M\). The initial projection is one because the kernel is zero; the final projection is the projection onto the closed range. Thus \(v_\pm^*v_\pm=1\). Finiteness of \(M\) says precisely that every such isometry is unitary. Therefore
\[
 \operatorname{ran}(T+iI)
 =\operatorname{ran}(T-iI)=H.
\]

For completeness these two surjectivity assertions imply equality with the adjoint, not just maximal symmetry. Take \(\eta\in D(T^*)\). Surjectivity of \(T+iI\) gives \(\xi\in D(T)\) with
\[
 (T+iI)\xi=(T^*+iI)\eta.
\]
Then \(\zeta=\eta-\xi\) lies in \(D(T^*)\) and \((T^*+iI)\zeta=0\). The adjoint definition gives
\[
 \ker(T^*+iI)
 =\operatorname{ran}(T-iI)^\perp.
\]
Indeed \((T-iI)^*=T^*+iI\), as follows by moving the bounded scalar term across the inner product. The right side is zero by the other surjectivity assertion. Hence \(\eta=\xi\in D(T)\). Symmetry supplies the opposite domain inclusion and agreement of actions. Thus \(T=T^*\). \(\square\)

## Tests of the hypotheses

**The functional sum can be uncountable.** On \(\ell^\infty(I)\), for an uncountable set \(I\), let \(\tau(a)=\sum_{i\in I}a_i\) for \(a\geq0\). Each coordinate evaluation is a bounded normal positive functional. Finite-coordinate projections show semifiniteness, and commuting two suprema shows normality of their sum. Faithfulness follows by testing any nonzero coordinate. This trace cannot be a countable sum of normal positive functionals. To see it, a bounded positive functional has nonzero value on only countably many coordinate projections: for each positive integer \(n\), only finitely many of those values can exceed \(1/n\), since their finite sums are bounded by its value at one. A countable family of such functionals therefore misses a coordinate outside a countable union, whereas \(\tau\) has value one there.

**The cutoff sequence need not increase.** On \(\ell^2(\mathbb N)\), let \(M\) be the diagonal algebra and \(\tau(a)=\sum_{j\geq1}2^{-j}a_j\). Let \(f_m\) project onto the first \(m\) coordinates, and set \(e_{2k}=f_{2k}\), \(e_{2k-1}=f_k\). The defect traces tend to zero, but for \(k>1\), \(e_{2k+1}=f_{k+1}<f_{2k}=e_{2k}\). Their algebraic span is the finite-coordinate vectors. The diagonal operator \(T\xi=(j\xi_j)_j\), on the domain \(\sum_jj^2|\xi_j|^2<\infty\), is closed, symmetric and affiliated: coordinate limits prove closedness, real diagonal entries prove symmetry, and diagonal unitary multiplication preserves the domain and action. Commutation with each coordinate projection forces a bounded operator to be diagonal, so these are all the commutant unitaries. TD-04 applies. Concretely, the usual finite-coordinate truncations converge both in norm and after applying \(T\).

**Faithfulness matters for defects.** On \(M=\mathbb C\oplus\mathbb C\), take \(\tau(a,b)=a\) on positive pairs, \(e=(0,1)\), and \(p=(1,0)\). This trace is normal and semifinite but not faithful. We have \(e\wedge p=0\) and \(\tau(1-p)=0\), although \(e\ne0\). Thus TD-02 cannot infer vanishing without faithfulness. TD-01 deliberately allowed this nonfaithful situation because its conclusion does not require such an inference.

**Density is part of the final operator statement.** The zero operator with domain \(\{0\}\) on a nonzero Hilbert space is closed and invariant under every unitary; its graph projection is zero. Its symmetry identity is vacuous, but its domain is not dense, and the usual single-valued adjoint is not defined. Thus the dense-domain hypothesis in TD-05 is essential. TD-03 allowed nondense closed operators, while TD-04 obtained density from its trace-dense domain assumption.

The mathematical antecedent is Masamichi Takesaki, *Theory of Operator Algebras I*, V.2, Exercises 1–4, printed pages 332–333. The exposition above proves every subpart. In particular the graph argument handles the two mutual domain inclusions by a bounded map on a closed graph subspace, and the finite-algebra argument uses the two shifted polar factors directly. Neither proof substitutes a faithful-state or countable-decomposition assumption for the stated generality.
