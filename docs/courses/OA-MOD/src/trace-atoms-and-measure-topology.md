# When a small trace defect must vanish

**Self-checked by the writing AI.**

Measure convergence permits an operator to be large on a projection of small trace. If every nonzero projection has a fixed minimum cost, this permission disappears. We first isolate that mechanism, prove that it applies to every type I factor, and then compare it with a countable atomic algebra whose atom costs can tend to zero. This comparison also determines exactly when every scalar sequence defines a measurable operator.

Throughout, \(M\subseteq B(H)\) is a von Neumann algebra acting nondegenerately, and \(\tau\) is a faithful normal semifinite trace. Hilbert spaces and factors need not be separable. Semifiniteness means ultraweak density of \(\mathfrak m_\tau\), as in WG002–003; we will not substitute an unproved order-density condition. For \(r,d>0\), use the neighborhoods from MT03: an element \(x\in M\) belongs to \(U(r,d)\) precisely when some projection \(e\in M\) satisfies

\[
 \begin{gathered}
 \|xe\|<r,\\
 \tau(1-e)<d.
 \end{gathered}
 \tag{MG.1}
\]

The algebra \(S(M,\tau)\) consists of the closed densely defined affiliated operators characterized in MT11. Equalities of such operators include their domains.

The same results are treated in with Masamichi Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, Exercises 1 and 3, p. 182, in the approved receipt-backed edition. The proofs below are organized around the common projection-cost argument and explicitly establish the diagonal operator domains.

## A minimal projection has a finite positive trace

A nonzero projection \(p\in M\) is **minimal** when its only subprojections in \(M\) are \(0,p\). First,

\[
 pMp=\mathbb C p.
 \tag{MG.2}
\]

Indeed, the spectral projections of a self-adjoint element of the corner belong to the corner by SK04 and SK08. If that element were not scalar on \(pH\), a spectral cut between two distinct points of its spectrum would be a proper nonzero subprojection of \(p\). Thus every self-adjoint corner element is scalar; its real and imaginary parts give (MG.2) for every element. Conversely, a corner satisfying (MG.2) has no proper nonzero projection.

**Lemma.** Every minimal projection satisfies

\[
 0<\tau(p)<\infty.
 \tag{MG.3}
\]

**Proof.** Put \(\mathfrak n_\tau=\{x:\tau(x^*x)<\infty\}\). For \(x\in\mathfrak n_\tau\), the trace identity and positivity give

\[
 \begin{gathered}
 \tau((xp)^*(xp))\\
 =\tau(xpx^*)\\
 \leq\tau(xx^*)\\
 =\tau(x^*x)<\infty.
 \end{gathered}
 \tag{MG.4}
\]

Here \(xx^*-xpx^*=x(1-p)x^*\geq0\); no tracial cyclic permutation involving an unbounded operator is used.

There is an \(x\in\mathfrak n_\tau\) with \(xp\ne0\). Otherwise every product \(y^*x\), with \(x,y\in\mathfrak n_\tau\), would annihilate \(pH\), and hence so would every member of \(\mathfrak m_\tau\). Choose a unit vector \(\eta\in pH\). The ultraweakly continuous vector functional \(a\mapsto\langle a\eta,\eta\rangle\) would vanish on that ultraweakly dense space but take value one at \(1\), a contradiction. The continuity used here is proved in BK03.

For this \(x\), (MG.2) gives \(px^*xp=\lambda p\) with \(\lambda>0\). Equation (MG.4) and positive homogeneity imply \(\tau(p)<\infty\), while faithfulness and \(p\ne0\) imply \(\tau(p)>0\). \(\square\)

This lemma does not assume that \(M\) is a factor. Different central summands may have different minimal-projection traces.

## In a factor one atom controls every projection

Suppose \(M\) is a nonzero factor and has a minimal projection \(p\). Set \(c=\tau(p)\). We prove that every nonzero projection \(q\in M\) satisfies

\[
 \tau(q)\geq c>0.
 \tag{MG.5}
\]

Let \(K\subseteq H\) be the closed linear span of the vectors \(xp\xi\), for \(x\in M\), \(\xi\in H\), and let \(z:H\to K\) be its orthogonal projection. The subspace \(K\) is invariant under every \(a\in M\) and its adjoint, so \(z\in M'\). It is also invariant under every \(b\in M'\) and its adjoint: \(bxp\xi=xpb\xi\). Hence \(z\in(M')'=M\), by the bicommutant theorem BK02. Thus \(z\) is central. It is nonzero because \(pH\subseteq K\). Factoriality gives \(z=1\), so \(K=H\).

For \(q\ne0\), some \(x\in M\) consequently satisfies \(qxp\ne0\). Otherwise \(q\) would vanish on the dense span defining \(K\), hence on \(H\). Write \(a=qxp\). By (MG.2), \(a^*a=\lambda p\) for \(\lambda>0\). The bounded operator \(v=\lambda^{-1/2}a\in M\) satisfies

\[
 \begin{gathered}
 v^*v=p,\\
 vv^*\leq q.
 \end{gathered}
 \tag{MG.6}
\]

Indeed \(a=ap=qa\), so \((vv^*)^2=v(v^*v)v^*=vv^*\), and its range is contained in \(qH\). The trace identity now gives

\[
 c=\tau(v^*v)=\tau(vv^*)\leq\tau(q),
\]

which proves (MG.5).

We use the intrinsic characterization of a **type I factor** as a nonzero factor containing a minimal projection. In the usual model \(B(L)\), any rank-one projection is minimal. The argument just given works in any faithful concrete representation of the factor and uses no countable matrix-unit decomposition or assumption on the dimension of \(L\) or \(H\).

## Exact equality with the norm topology

For a general traced \(M\), the following conditions are equivalent:

1. Its measure topology agrees with its operator norm topology.
2. There is a real \(c>0\) such that every nonzero projection of \(M\) has trace at least \(c\).

**Proof.** Norm convergence always implies measure convergence: in (MG.1) choose \(e=1\). Suppose condition 2 holds. If \(0<d\leq c\) and \(\tau(1-e)<d\), the projection \(1-e\) must be zero. Write \(B_r\) for the norm ball \(\{x\in M:\|x\|<r\}\). For every \(r>0\) and \(0<d\leq c\), we have the exact neighborhood identity

\[
 U(r,d)=B_r.
 \tag{MG.7}
\]

This proves equality of the topologies and thus equality of their convergent and Cauchy nets, not only their convergent sequences.

If condition 2 fails, choose a nonzero projection \(q_n\) with \(\tau(q_n)<1/n\). For any fixed \(r,d>0\), sufficiently large \(n\) has \(q_n\in U(r,d)\), witnessed by \(e=1-q_n\): the product \(q_ne\) is zero. Thus \(q_n\to0\) in measure. But \(\|q_n\|=1\), since it fixes every unit vector in its nonzero range and is a contraction. It does not converge to zero in norm, contradicting condition 1. \(\square\)

Under these equivalent conditions,

\[
 S(M,\tau)=M
 \tag{MG.8}
\]

as concrete operators and as topological algebras. To check the domains directly, let \(T\in S(M,\tau)\). By MT11 there is a projection \(e\) with \(\tau(1-e)<c\) and \(eH\subseteq D(T)\). Necessarily \(e=1\), hence \(D(T)=H\). The proved closed-graph and affiliation specialization MT07 gives \(T=T1\in M\). Conversely every bounded member of \(M\) is measurable, using the same domain criterion with \(e=1\). In the completion formulation, every Cauchy net is norm Cauchy by (MG.7), and has a limit in \(M\), by the completeness of \(B(H)\) and norm closedness of \(M\) proved in BK01–02. Thus the completion adds no elements and its topology is the same norm topology. The zero algebra satisfies these assertions as well, with condition 2 vacuous.

Applying MG02 proves both conclusions for every type I factor with a faithful normal semifinite trace. The strict inequality in (MG.1) allows \(d=c\); for neighborhoods using \(\leq d\), one instead takes \(d<c\).

## All affiliated operators in a diagonal algebra

Now take \(H=\ell^2(\mathbb N)\), with unit vectors \(\delta_n\), and let \(M=\ell^\infty(\mathbb N)\) act by coordinatewise multiplication. For each sequence \(a=(a_n)\) of finite complex numbers, define a linear operator \(T_a:D(T_a)\subseteq H\to H\). Its domain consists exactly of those \(\xi\in\ell^2\) satisfying the first condition below; the second formula specifies its action:

\[
 \begin{gathered}
 \sum_n|a_n\xi_n|^2<\infty,\\
 (T_a\xi)_n=a_n\xi_n.
 \end{gathered}
 \tag{MG.9}
\]

These are precisely all closed densely defined operators affiliated with \(M\).

**Proof of the forward assertion.** The domain contains every finitely supported sequence, so is dense. If \(\xi^{(j)}\to\xi\) and \(T_a\xi^{(j)}\to\eta\) in \(\ell^2\), then coordinate convergence gives \(\eta_n=a_n\xi_n\). Since \(\eta\in\ell^2\), the vector \(\xi\) belongs to (MG.9) and \(T_a\xi=\eta\). Thus \(T_a\) is closed.

The commutant of \(M\) is \(M\) itself. A bounded operator commuting with all coordinate projections sends \(\delta_n\) to \(b_n\delta_n\), with \(|b_n|\) bounded by its norm; finite truncation then shows it is diagonal. Conversely diagonal bounded operators commute. A unitary in this commutant is multiplication by numbers of modulus one, which preserves the sum in (MG.9), preserves the domain in both directions, and commutes with \(T_a\). This proves affiliation.

**Proof of the reverse assertion.** Let \(T\) be closed, densely defined and affiliated. Write \(e_n\) for the projection onto \(\mathbb C\delta_n\). Affiliation for the unitary \(1-2e_n\) implies, for every \(\xi\in D(T)\),

\[
 \begin{gathered}
 e_n\xi\in D(T),\\
 Te_n\xi=e_nT\xi.
 \end{gathered}
 \tag{MG.10}
\]

Density of \(D(T)\) implies \(e_nD(T)\) is dense in \(\mathbb C\delta_n\), so some vector of the domain has nonzero \(n\)-th coordinate. By (MG.10) and scaling, \(\delta_n\in D(T)\) and \(T\delta_n=a_n\delta_n\) for a finite scalar \(a_n\).

For \(\xi\in D(T)\), (MG.10) gives \((T\xi)_n=a_n\xi_n\). Thus \(T\subseteq T_a\), including the domain inclusion. On the other hand, for \(\xi\in D(T_a)\), its first \(N\) coordinates form a vector \(\xi^{[N]}\in D(T)\), and both of the following limits hold in \(\ell^2\):

\[
 \begin{aligned}
 \xi^{[N]}&\longrightarrow\xi,\\
 T\xi^{[N]}&\longrightarrow T_a\xi.
 \end{aligned}
 \tag{MG.11}
\]

The second convergence follows from the convergent sum in (MG.9). Closedness of \(T\) proves \(T_a\subseteq T\). Hence the operators and their maximal domains are equal. \(\square\)

For use with MT11, \(|T_a|=T_{|a|}\). One can verify this without assuming normality: the adjoint test on each \(\delta_n\) forces \((T_a^*\eta)_n=\overline{a_n}\eta_n\), and the square summability of these coordinates is also sufficient by Cauchy–Schwarz. Hence \(T_a^*=T_{\bar a}\). The product \(T_a^*T_a\) has domain \(\sum_n |a_n|^4|\xi_n|^2<\infty\), since \(t^2\leq1+t^4\). It is multiplication by \(|a_n|^2\); its positive square root is multiplication by \(|a_n|\), either by the same diagonal adjoint test or by SK05–07. Its spectral projection above \(R\) is therefore multiplication by the indicator of \(\{n:|a_n|>R\}\).

## Atom weights decide which sequences are measurable

Set \(c_n=\tau(e_n)\). Every \(e_n\) is minimal, so MG01 gives \(0<c_n<\infty\). For every bounded nonnegative sequence \(x=(x_n)\), normality applied to the increasing finite truncations proves

\[
 \begin{aligned}
 \tau(x)&=\sum_{n=1}^{\infty}c_nx_n,\\
 \tau(1)&=\sum_{n=1}^{\infty}c_n.
 \end{aligned}
 \tag{MG.12}
\]

The sums may be infinite. In particular every projection, which is the indicator of a subset of \(\mathbb N\), has trace equal to the sum of its atom weights. Equations (MG.9)–(MG.12) and MT11 give the exact criterion

\[
 \begin{gathered}
 T_a\in S(M,\tau)\\
 \Longleftrightarrow\\
 \sum_{|a_n|>R}c_n\longrightarrow0\\
 (R\to\infty).
 \end{gathered}
 \tag{MG.13}
\]

**Theorem.** Every complex sequence defines a \(\tau\)-measurable operator if and only if \(\tau(1)<\infty\).

**Proof.** Suppose \(\sum_n c_n<\infty\), and let \(a\) be any sequence. Given \(\varepsilon>0\), choose a finite initial set \(F\) such that \(\sum_{n\notin F}c_n<\varepsilon\). For \(R\geq\max_{n\in F}|a_n|\), the set in (MG.13) misses \(F\), so its weight is below \(\varepsilon\). This proves measurability with no growth restriction on \(a\).

Conversely suppose \(\sum_n c_n=\infty\). Take the particular sequence \(a_n=n\). For each finite \(R\), the sum over \(n\leq R\) is finite, because it has only finitely many finite terms. Consequently

\[
 \sum_{\{n:\,n>R\}}c_n=\infty.
 \tag{MG.14}
\]

Otherwise adding the finite initial sum would make the total sum finite. Criterion (MG.13) shows that this sequence is not measurable. Its multiplication operator remains closed, densely defined and affiliated by MG04; those properties alone do not imply measurability. \(\square\)

The same atom weights also show exactly why factoriality mattered earlier. By MG03, the measure and norm topologies on \(\ell^\infty\) coincide precisely when \(\inf_n c_n>0\): this lower bound controls every nonempty projection, while its failure supplies coordinate projections with arbitrarily small trace. For example, with \(c_n=2^{-n}\) every sequence is measurable, but \(e_n\to0\) in measure and \(\|e_n\|=1\). With \(c_n=1\), measure topology equals norm topology and only bounded sequences are measurable. These are both faithful normal semifinite traces: faithfulness follows from positive atom weights, normality by exchanging the two increasing suprema over finite sums and the directed net, and semifiniteness because bounded finite-support truncations lie in the finite-domain algebra and converge strongly, hence ultraweakly, to every bounded diagonal operator. The bounded strong-to-ultraweak implication is BK03.

Thus the number of atoms, their total trace, and a uniform positive lower bound on their traces govern different questions. The two examples separate those questions without changing the definition of measurable operator.
