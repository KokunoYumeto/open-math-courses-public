# Convergence on large domains

**Self-checked by the writing AI.**

Convergence on vectors, convergence in measure, and uniform convergence after a projection cutoff are different demands. We construct the closed operator determined by vector convergence, then use moving supports to locate the boundaries between these demands. Domains and quantifiers remain part of each statement.

Throughout, \(M\subseteq B(H)\) has a faithful normal semifinite trace \(\tau\), and \(A_n\in S(M,\tau)\). No separability or sigma-finiteness is imposed except in the explicitly commutative sections. The closed measurable algebra and its completed vector module are constructed in MT05–11. A subspace is **trace-dense** in the sense of MM05: it contains the ranges of increasing projections whose complementary traces tend to zero.

The same results are treated in Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, Exercise 6(a)–(i), pp. 183–184. All nine clauses are treated below, including the two on the continuation page. Several printed conclusions require correction under the definition of convergence given there. NE09 states the correspondence explicitly; none of those corrections is hidden in an extra standing hypothesis.

## The maximal limit domain and bounded restrictions

Assume there is a trace-dense linear subspace \(D\) contained in every \(D(A_n)\), such that \(A_n\xi\) converges in Hilbert norm for every \(\xi\in D\). Let \(D_L\) be the set of all vectors in \(\bigcap_nD(A_n)\) for which \((A_n\xi)_n\) converges in Hilbert norm, and define its operator by

\[
 \begin{gathered} D_L\subseteq\bigcap_nD(A_n),\\
 L\xi=\lim_n A_n\xi. \end{gathered}
 \tag{NE.1}
\]

Linearity of the domains, limits and operators proves that \(D_L\) is a linear subspace and \(L\) is linear. It contains \(D\), hence is Hilbert-space dense by MM05.

For every unitary \(u\in M'\), affiliation of all \(A_n\) gives \(uD_L=D_L\) and \(Lu\xi=uL\xi\). Indeed, apply the bounded map \(u\) to the convergent sequence and then use \(u^*\) for the reverse domain inclusion. Thus the raw limit has the commutant invariance required for affiliation. We do **not** infer that it is closed. In this course, an affiliated operator is normally required to be closed; this qualification matters for the raw \(L\).

If a projection \(p\in M\) satisfies \(pH\subseteq D_L\), then

\[
 \begin{gathered} A_np,\ Lp\in M,\\
 C_p:=\sup_n\|A_np\|,\\
 C_p<\infty,\\
 \|Lp\|\leq C_p,\\
 A_np\longrightarrow Lp. \end{gathered}
 \tag{NE.2}
\]

The convergence in (NE.2) is strong. For each \(n\), the closed graph specialization CG03 makes \(A_np\) bounded and in \(M\). For every \(\xi\in H\), the sequence \(A_np\xi\) converges and is bounded. The full uniform boundedness theorem AB03 gives \(C_p<\infty\). Passing to the pointwise limit gives a bounded operator \(Lp\) with the stated norm. Strong closedness of \(M\), proved in BK02, puts it in \(M\). This argument does not apply the closed graph theorem to \(L\).

## Closing the limit without losing its full domain

**Closure theorem.** There is a unique closed measurable operator \(T\) such that

\[
 \overline L=T.
 \tag{NE.3}
\]

If \(p_k\) increases, \(p_kH\subseteq D\), and \(\tau(1-p_k)\to0\), then \(D_0=\bigcup_kp_kH\) is a graph core for \(T\). In particular, the resulting closed operator is independent of the witnessing trace-dense subspace.

**Proof.** Put \(B_k=Lp_k\in M\). The compatibility \(B_mp_k=B_k\) for \(m\geq k\) permits the increasing-domain theorem MT10. It gives an element \(a\) of the completed algebra, with

\[
 \begin{gathered} B_k\longrightarrow a,\\
 T=T_a=\overline{L|_{D_0}}. \end{gathered}
 \tag{NE.4}
\]

The convergence in (NE.4) is in measure. This initially closes only the restriction. We must show that every vector of the larger domain \(D_L\) belongs to \(D(T)\), with the same image.

Fix \(\xi\in D_L\). For each \(n,k\), the closed measurable product
\(C_{n,k}=\overline{A_n(1-p_k)}\) exists by MT09. Its kernel contains \(p_kH\), so its right support is at most \(1-p_k\). Its polar decomposition RD02 identifies this support with its range projection \(r_{n,k}\in M\). The trace identity MT02 gives

\[
 \tau(r_{n,k})\leq\tau(1-p_k).
 \tag{NE.5}
\]

The vector \((1-p_k)\xi\) is in \(D(A_n)\): both \(\xi\) and \(p_k\xi\) are. Its image belongs to \(r_{n,k}H\), and

\[
 \begin{gathered} A_n(1-p_k)\xi\\
 \longrightarrow L\xi-B_k\xi. \end{gathered}
 \tag{NE.6}
\]

in Hilbert norm as \(n\to\infty\).

Recall the vector neighborhoods from MT03: a vector \(v\) belongs to \(O(\varepsilon,d)\) if some projection \(q\) has \(\tau(1-q)<d\) and \(\|qv\|<\varepsilon\). For given \(\varepsilon,d>0\), choose \(k\) so that \(\tau(1-p_k)<d\), then choose \(n\) so late in (NE.6) that its norm error is less than \(\varepsilon\). Taking \(q=1-r_{n,k}\) proves
\(L\xi-B_k\xi\in O(\varepsilon,d)\). This works for every sufficiently large \(k\), with \(n\) allowed to depend on \(k\). Hence \(B_k\xi\to L\xi\) in vector measure.

On the other hand, (NE.4) and continuity of the completed action in MT05 give \(B_k\xi\to a\xi\). Separation in MT04–05 yields \(a\xi=L\xi\in H\). The exact realization definition in MT08 now gives \(\xi\in D(T)\) and \(T\xi=L\xi\). Thus \(L\subseteq T\). Since the smaller restriction in (NE.4) already has closure \(T\), the full \(L\) is closable and has that same closure. This proves (NE.3), the core assertion and uniqueness. \(\square\)

**The closure is essential.** On \(H=L^2(0,1)\), with the integral trace, let

\[
 A_n=M_{n1_{(0,1/n)}}.
 \tag{NE.7}
\]

These are bounded measurable operators. Every vector vanishing on some neighborhood of zero eventually has image zero. Such vectors contain \(p_mH\) for \(p_m=M_{1_{[1/m,1)}}\), with \(\tau(1-p_m)=1/m\), so convergence is trace-nearly everywhere in the stated sense.

Any norm limit of \(A_n\xi\) must be zero: for each \(m\), all sufficiently late images vanish outside \((0,1/m)\); their limit has the same property, and the intersection of these intervals is empty. But the constant vector \(1\) is not in \(D_L\), since \(\|A_n1\|_2=\sqrt n\). Therefore \(L\) is zero on a proper dense domain. Its graph is not closed, while its closure is the everywhere-defined zero operator. Under Definition IX.2.8, p. 173, which explicitly requires closedness, the raw limit is not a measurable operator. Its closure is.

## Finite corners give moving cutoffs and subsequences

Let \(T=\overline L\), and let \(e\in M\) be a projection with \(\tau(e)<\infty\). Then for every \(\varepsilon,d>0\), there is an \(N\) such that for each \(n\geq N\) there exists a projection \(s_n\leq e\) satisfying

\[
 \begin{gathered}
 \tau(e-s_n)<d,\\
 s_nH\subseteq D_L,\\
 \|(A_n-T)s_n\|<\varepsilon.
 \end{gathered}
 \tag{NE.8}
\]

The projection can depend on \(n\). All products in (NE.8) are the actual bounded restrictions on their indicated ranges.

**Proof.** Choose \(q\) with \(qH\subseteq D\) and \(\tau(1-q)<d/2\), and put \(p=e\wedge q\). The polar decomposition of \((1-q)e\) identifies its right support \(e-p\) with a subprojection of \(1-q\). Thus
\(\tau(e-p)\leq\tau(1-q)<d/2\). The operators
\(Y_n=(A_n-T)p\in M\) are uniformly bounded and converge strongly to zero by NE01–02. Their positive squares \(Y_n^*Y_n\) also converge strongly to zero: their value on \(\xi\) has norm at most \((\sup_n\|Y_n\|)\|Y_n\xi\|\).

Here is the exact trace-continuity input. The map \(x\mapsto\tau(pxp)\) is a bounded positive functional on \(M\), using the finite linear extension and Cauchy–Schwarz proved in WG004–005. Its norm is \(\tau(p)\), and congruence preserves increasing bounded suprema by BK04. It is order normal, hence ultraweakly continuous by the scalar theorem NP02. Bounded strong convergence implies ultraweak convergence by BK03. Since \(Y_n^*Y_n=pY_n^*Y_np\), we obtain

\[
 \tau(Y_n^*Y_n)\longrightarrow0.
 \tag{NE.9}
\]

No continuity of an infinite trace on arbitrary bounded sequences is being asserted.

Inside \(pMp\), let \(h_n\) be the spectral projection of \(Y_n^*Y_n\) for values greater than \((\varepsilon/2)^2\), and put \(s_n=p-h_n\). The spectral calculus SK04–05 gives

\[
 \begin{gathered} \|Y_ns_n\|\leq\varepsilon/2,\\
 \tau(h_n)\\
 \leq4\varepsilon^{-2}\tau(Y_n^*Y_n). \end{gathered}
 \tag{NE.10}
\]

For all sufficiently large \(n\), the last quantity is less than \(d/2\). Since \(s_n\leq p\leq q\), its range lies in \(D\), and (NE.8) follows. \(\square\)

**A single subsequence for each finite corner.** There are strictly increasing indices \(n_k\) and increasing projections \(r_m\leq e\) with the following estimates. Write \(Z_k=A_{n_k}-T\) on the common domain:

\[
 \begin{gathered} \tau(e-r_m)\\
 \leq2^{1-m},\\
 r_mH\subseteq D_L,\\
 \|Z_kr_m\|<2^{-k}\\
 (k\geq m). \end{gathered}
 \tag{NE.11}
\]

Indeed, (NE.8) permits successive choices of \(n_k\) and \(s_k\leq e\), with trace defect less than \(2^{-k}\) and norm error less than \(2^{-k}\). Define \(r_m=\bigwedge_{k\geq m}s_k\). The noncommuting projection estimate MT02, applied in the finite corner, gives the trace bound; range inclusion and the norm estimate follow from \(r_m\leq s_k\). Thus for every \(d>0\), one of these projections has defect less than \(d\) and the chosen subsequence converges uniformly on its range. The subsequence may depend on \(e\); no countable exhaustion of an arbitrary algebra has been assumed.

When \(\tau(1)<\infty\), (NE.8) with \(e=1\) also proves global convergence in measure of the full sequence to \(T\). For an infinite trace this need not hold. On the diagonal algebra on \(\ell^2(\mathbb N)\) with counting trace, the coordinate projections \(A_n\) converge strongly to zero on all of \(H\), hence trace-nearly everywhere. Their traces are all one. A cutoff with complementary trace less than one must be the identity, so \(A_n\) cannot converge to zero in measure. The diagonal model and its trace are verified in MG04–05.

## A bounded moving-support sequence

Work on \((0,1)\) with Lebesgue measure. At level \(k\geq1\), partition the interval into the \(2^k\) half-open dyadic intervals \(I_{k,j}\); endpoint choices do not affect the multiplication operators. List these intervals level by level, and set \(f_n=1_{I_{k,j}}\) when index \(n\) corresponds to \((k,j)\). Every \(x\in(0,1)\) belongs to exactly one interval at each level and misses at least one other. Consequently

\[
 \begin{gathered} \liminf_n f_n(x)=0,\\
 \limsup_n f_n(x)=1. \end{gathered}
 \tag{NE.12}
\]

The sequence fails to converge at every such point.

Nevertheless, the multiplication operators converge strongly to zero on **all** of \(L^2(0,1)\). For \(\xi\in L^2\) and \(R>0\), let \(a_R(\xi)\) be the integral of \(|\xi|^2\) over the set where \(|\xi|^2>R\). Then

\[
 \begin{gathered} \|f_n\xi\|_2^2\\
 \leq R\,2^{-k}+a_R(\xi). \end{gathered}
 \tag{NE.13}
\]

First make the integrable tail small, using scalar dominated convergence, and then let \(k\to\infty\). This proves strong convergence, so the witnessing trace-dense domain can be \(H\) itself.

It also disproves a stronger uniform-cutoff conclusion. If a measurable set \(E\subseteq(0,1)\) has positive measure, then at every level at least one \(I_{k,j}\cap E\) has positive measure, since finitely many of these intersections partition \(E\). For its index,

\[
 \|M_{f_n}M_{1_E}\|=1.
 \tag{NE.14}
\]

Such indices occur arbitrarily late. All projections in the multiplication algebra are \(M_{1_E}\) by MM01. Thus no fixed projection of positive trace makes the tail norms less than \(1/2\), or makes them tend to zero. In particular, with \(e=1\) and discarded trace less than \(1/2\), the whole-sequence conclusions printed in IX.2(6)(d) and (e) fail. They cannot follow from strong convergence of the bounded restrictions. Equations (NE.8) and (NE.11) give the moving-cutoff and subsequence replacements.

This same example proves the valid assertion in part (h): trace-nearly everywhere convergence does not imply pointwise almost-everywhere convergence, even for bounded self-adjoint multipliers on a finite measure space.

## Almost-everywhere convergence and the global envelope

Let \((X,\mu)\) be sigma-finite, let \(A_n=M_{f_n}\in S(L^\infty(\mu),\tau)\), and suppose the measurable finite-almost-everywhere functions \(f_n\) converge almost everywhere to a finite-valued function \(f\). Work outside their common measurable null set, and put

\[
 \begin{gathered} F(x)\\
 =\sup_n|f_n(x)|. \end{gathered}
 \tag{NE.15}
\]

Set its value to zero on the exceptional set. This is measurable and finite almost everywhere, because each convergent scalar sequence is bounded.

**Exact criterion.** Under this almost-everywhere convergence hypothesis, \((A_n)\) converges trace-nearly everywhere if and only if

\[
 \begin{gathered} \mu\{F>R\}\longrightarrow0\\
 (R\to\infty). \end{gathered}
 \tag{NE.16}
\]

When this holds, the closed limit is \(M_f\).

**Sufficiency.** Let \(E_m=\{F\leq m\}\). Their indicators give increasing projections with trace defects tending to zero. For every \(\xi\in L^2(E_m)\), all products \(f_n\xi\) and \(f\xi\) lie in \(L^2\), and

\[
 \begin{gathered} |(f_n-f)\xi|^2\\
 \leq4m^2|\xi|^2. \end{gathered}
 \tag{NE.17}
\]

Dominated convergence gives convergence in \(L^2\) on these ranges. Their union is a trace-dense witnessing subspace. The tail criterion MM04, together with \(|f|\leq F\), makes \(M_f\) measurable. It agrees with the limit on these ranges, so MT07 graph uniqueness identifies the closure in NE02 with \(M_f\).

**Necessity.** For any \(d>0\), choose a projection \(p=M_{1_E}\) whose range lies in the convergence domain and with \(\mu(X\setminus E)<d\). By NE01, \(\sup_n\|M_{f_n}p\|=C<\infty\). The multiplier norm and domain characterization MM01–02 imply \(|f_n|\leq C\) almost everywhere on \(E\) for every \(n\): a violation on a finite positive-measure subset would contradict that operator bound by testing its indicator. Remove the countable union of the exceptional null sets. Then \(F\leq C\) on \(E\), and \(\mu\{F>C\}<d\). Since \(d\) was arbitrary, this proves (NE.16). The necessity of the envelope condition uses only convergence on a trace-dense domain, not the assumed pointwise convergence.

When \(\mu(X)<\infty\), the decreasing sets \(\{F>R\}\) have null intersection and their measures tend to zero. One may prove this by applying monotone convergence to their complements and subtracting from the finite number \(\mu(X)\). Thus almost-everywhere convergence implies trace-nearly everywhere convergence on every finite measure space.

**Why sigma-finiteness alone is insufficient.** On \((0,\infty)\), set

\[
 \begin{gathered} f_n(x)\\
 =x1_{(0,n)}(x). \end{gathered}
 \tag{NE.18}
\]

Each multiplier is bounded and trace-measurable, and the functions converge pointwise to \(x\). Their envelope is \(F(x)=x\), whose every high-level tail has infinite measure. Hence there is no trace-dense convergence domain. More precisely, the maximal convergence domain is exactly \(D(M_x)\): if the images converge, their squared norms \(\int_0^n x^2|\xi|^2\) remain bounded, and monotone convergence puts \(x\xi\) in \(L^2\); the converse follows by dominated convergence. By MM04, \(M_x\) is not trace-measurable, so MT11 confirms that this domain is not trace-dense.

Even a bounded limit does not repair the missing condition. The bounded multipliers for \(f_n=n1_{[n,n+1)}\) converge pointwise to zero, but their envelope has infinitely many unit intervals above every fixed threshold. Its high-level tails again have infinite measure. These examples refute the forward implication of printed part (f) on a general sigma-finite infinite measure space. Criterion (NE.16) retains exactly what is needed.

## Recovering the scalar limit along a subsequence

For the same sigma-finite multiplication model, now assume only trace-nearly everywhere convergence. By NE02 and MM03–04, its closed limit is \(T=M_f\) for a unique trace-measurable function \(f\), modulo null sets. There is a subsequence \(f_{n_k}\) converging almost everywhere to \(f\), and any almost-everywhere convergent subsequence of the original sequence has this same limit.

**Proof.** Choose increasing measurable sets \(E_j\) whose projection ranges lie in \(D\) and with \(\mu(X\setminus E_j)\to0\). The union is conull. Choose an increasing exhaustion \(X_j\) by finite-measure sets, using sigma-finiteness, and put \(K_j=E_j\cap X_j\). These sets increase, have finite measure and exhaust \(X\) modulo a null set. Testing convergence on \(1_{K_j}\) gives

\[
 \begin{gathered} \|(f_n-f)1_{K_j}\|_2^2\\
 \longrightarrow0. \end{gathered}
 \tag{NE.19}
\]

Choose strictly increasing \(n_k\) such that the integral over \(K_k\) is less than \(2^{-3k}\). For
\(V_k=K_k\cap\{|f_{n_k}-f|>2^{-k}\}\), the scalar integral bound yields

\[
 \mu(V_k)\leq2^{-k}.
 \tag{NE.20}
\]

For each \(m\), countable subadditivity bounds \(\mu(\bigcup_{k\geq m}V_k)\) by \(2^{1-m}\). Its intersection over \(m\) therefore has measure zero. Outside that null set and the complement of \(\bigcup K_j\), every point eventually lies in \(K_k\) and outside \(V_k\). This proves the asserted pointwise convergence without appealing to a subsequence theorem in place of a proof.

If another subsequence converges almost everywhere to \(g\), apply scalar Fatou on each \(K_j\) to (NE.19). It gives \(\int_{K_j}|g-f|^2=0\). The countable exhaustion proves \(g=f\) almost everywhere. If an extended infinite limit had been allowed, the same Fatou estimate would exclude infinite values on a positive-measure subset. This proves both existence and uniqueness assertions in the converse portion of part (f).

## A diffuse algebra separates measure from domain convergence

Suppose \(M\ne0\) is diffuse. There is a sequence of bounded positive operators which tends to zero in global measure but does not converge trace-nearly everywhere to any operator.

Choose a nonzero projection \(e\) with
\(0<t:=\tau(e)<\infty\), using TI01. The projection-splitting proof DU01 permits successive equal halvings. At level \(k\), obtain orthogonal projections \(e_{k,j}\), \(1\leq j\leq2^k\), with

\[
 \begin{gathered}
 \sum_{j=1}^{2^k}e_{k,j}=e,\\
 \tau(e_{k,j})=t2^{-k}.
 \end{gathered}
 \tag{NE.21}
\]

List the levels consecutively and define

\[
 A_n=4^k e_{k,j}.
 \tag{NE.22}
\]

The projection \(1-e_{k,j}\) kills \(A_n\), and its discarded trace tends to zero. Thus \(A_n\to0\) in every measure neighborhood, regardless of the growing scalar amplitude.

Suppose a trace-dense convergence domain existed. Choose \(q\) with range in that domain and \(\tau(1-q)<t/2\). NE01 would give \(\sup_n\|A_nq\|=C<\infty\). Hence
\(\|e_{k,j}q\|\leq C4^{-k}\), and positivity gives

\[
 \begin{gathered} e_{k,j}q e_{k,j}\\
 \leq C^2 16^{-k}e_{k,j}. \end{gathered}
 \tag{NE.23}
\]

Trace cyclicity for finite corners, proved in MT13, yields

\[
 \begin{gathered} \tau(eqe)\\
 =\sum_{j=1}^{2^k}\tau(e_{k,j}q e_{k,j})\\
 \leq C^2 16^{-k}t. \end{gathered}
 \tag{NE.24}
\]

For completeness, the equality follows by writing
\(\tau(eqe)=\tau(qeq)\), expanding \(e=\sum_j e_{k,j}\), and using
\(\tau(qe_{k,j}q)=\tau(e_{k,j}q e_{k,j})\) term by term. All these positive quantities are finite. On the other hand, writing \(q^\perp=1-q\),

\[
 \begin{gathered} \tau(eqe)\\
 =t-\tau(eq^\perp e)\\
 \geq t-\tau(q^\perp)\\
 >t/2. \end{gathered}
 \tag{NE.25}
\]

The inequality follows from
\(\tau(e(1-q)e)=\tau((1-q)e(1-q))\), which is at most \(\tau(1-q)\).
Letting \(k\to\infty\) contradicts (NE.24). This proves the separation in part (g) for every nonzero diffuse semifinite algebra, including arbitrary nonseparable representations. No trace-preserving embedding of a unit-mass probability algebra into a corner of insufficient trace has been assumed. The zero algebra has only the zero sequence and is the trivial exception to any assertion that a counterexample exists.

## Self-adjoint limits and resolvents

Assume now that every \(A_n\) is self-adjoint. The closed limit \(T\) from NE02 is self-adjoint, and for every nonreal \(z\),

\[
 \begin{gathered} (A_n-z)^{-1}\\
 \longrightarrow(T-z)^{-1}. \end{gathered}
 \tag{NE.26}
\]

The convergence in (NE.26) is strong; each inverse is the bounded resolvent on all of \(H\).

**Proof.** For \(\xi,\eta\in D_L\), taking limits of the self-adjoint pairings gives
\(\langle L\xi,\eta\rangle=\langle\xi,L\eta\rangle\).
Passing to graph limits makes \(T=\overline L\) symmetric. Therefore \(T\subseteq T^*\); in particular \(T^*\) is densely defined. The adjoint is closed and affiliated, as follows directly by transferring the commutant identity through the adjoint-domain test. The maximality theorem MT08 says that a closed measurable operator has no proper closed affiliated extension. Applying it to \(T\subseteq T^*\) gives \(T=T^*\).

NE02 gives the graph core \(D_0\subseteq D(T)\cap\bigcap_nD(A_n)\), and \(A_n\xi\to T\xi\) for every \(\xi\in D_0\). The core convergence theorem SK09 now applies. Its resolvent estimate can also be seen directly. Write \(R_n=(A_n-z)^{-1}\) and \(R=(T-z)^{-1}\). The self-adjoint spectral calculus gives

\[
 \begin{gathered} \|R_n\|,\ \|R\|\\
 \leq|\operatorname{Im}z|^{-1}. \end{gathered}
 \tag{NE.27}
\]

On the dense set \((T-z)D_0\), write \(\eta=(T-z)\xi\), with \(\xi\in D_0\). Then

\[
 \begin{gathered} (R_n-R)\eta\\
 =R_n(T-A_n)\xi\\
 \longrightarrow0. \end{gathered}
 \tag{NE.28}
\]

Density follows from the graph-core approximation and surjectivity of \(T-z\), both proved in SK06–09. The common resolvent bound extends convergence from that dense set to every vector. This proves (NE.26) for every nonreal \(z\), without a separate resolvent convergence assumption. \(\square\)

## Exact statement boundaries

The nine source clauses have the following dispositions under their stated definition of convergence.

| Clause | Result established here |
| --- | --- |
| (a) | The raw limit has commutant invariance on its entire domain (NE01); its closure is a closed affiliated operator (NE02). Closedness of the raw limit does not follow. |
| (b) | Every projection range in the convergence domain has bounded restrictions, with a uniform bound over the sequence (NE01). |
| (c) | The closure of the raw limit is trace-measurable. The raw limit itself need not be closed; (NE.7) is an explicit counterexample (NE02). |
| (d) | A cutoff may be chosen separately for each sufficiently late index (NE03). The printed single-cutoff claim for the whole tail is false (NE04). |
| (e) | Each finite corner admits a subsequence and arbitrarily large fixed cutoffs with uniform convergence (NE03). The printed whole-sequence version is false (NE04). |
| (f) | Almost-everywhere convergence implies domain convergence exactly when the global envelope has vanishing measure tails; this holds automatically in finite measure but not for arbitrary sigma-finite measure (NE05). The converse subsequence existence and uniqueness are valid (NE06). |
| (g) | In every nonzero diffuse traced algebra, measure convergence does not imply convergence on a trace-dense domain (NE07). |
| (h) | Domain convergence does not imply almost-everywhere convergence, even for bounded self-adjoint multipliers on a finite measure space (NE04). |
| (i) | For self-adjoint approximants the closed limit is self-adjoint, and all nonreal resolvents converge strongly (NE08). |

The countable projection arguments use the exact estimates of MT02 and MM05. Scalar integration, Fatou and dominated convergence used above are proved in the scalar integration programme, Sections 0–2; scalar Hilbert completeness and finite-support indicator approximations are proved in SS1. These internal proofs, together with the section-specific links, supply the mathematical inputs. Source citations identify the comparison being corrected; they do not replace any proof.
