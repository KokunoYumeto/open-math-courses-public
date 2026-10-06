# Finite trace domains, central parts and amplification

For a general weight, finite values and zero values are controlled by different projections, neither of which need be central. The trace identity changes this geometry: the finite domain becomes a two-sided ideal, both projections become central, and ordered finite approximations become available. These facts let us add traces on disjoint central pieces and amplify a trace by an arbitrary type I factor.

The source correspondence is Masamichi Takesaki, *Theory of Operator Algebras I*, V.2: Definition 2.1; Proposition 2.10, Definition 2.11 and Lemmas 2.12–2.13; Proposition 2.14; Lemma 2.16, its following remark and Definition 2.17. These are PDF pages 317 and 323–327 in the approved edition. The present organization starts with the finite-domain algebra, constructs the two central parts, and then uses ordered cutoffs for amplification. Every invoked weight result has an exact earlier proof below. Trace results are also proved in existing programme lessons; this direct route supplements their uses in the course.

## Trace axioms and the two finite ideals

Let \(M\subseteq B(H)\) be a unital von Neumann algebra. No countability hypothesis is imposed. A **trace** is a weight \(\tau:M_+\to[0,\infty]\) satisfying

\[
 \tau(x^*x)=\tau(xx^*)\quad(x\in M).
\]

Thus it is additive on positive elements and nonnegatively homogeneous, with \(0\cdot\infty=0\) and \(\tau(0)=0\). These are the weight conventions of WG002. A trace is **faithful** if its only positive zero is zero, **finite** if \(\tau(1)<\infty\), and **normal** if it preserves the supremum of every bounded increasing positive net. We use the course definition of **semifinite**, namely ultraweak density of its finite definition algebra. TB02 proves its equivalence, specifically for traces, to the condition that every nonzero positive element dominates a nonzero positive element of finite trace.

We keep three domains distinct:

\[
 \begin{gathered}
 F_\tau=\{a\in M_+:\tau(a)<\infty\},\\
 \mathfrak n_\tau=\{x\in M:\tau(x^*x)<\infty\},\\
 \mathfrak m_\tau=\operatorname{span}_{\mathbb C}
       (\mathfrak n_\tau^*\mathfrak n_\tau).
 \end{gathered}
\]

WG003 proves that \(F_\tau\) is hereditary, \(\mathfrak n_\tau\) is a left ideal, and

\[
 \begin{gathered}
 \mathfrak m_\tau=\operatorname{span}_{\mathbb C}F_\tau,\\
 (\mathfrak m_\tau)_+=F_\tau.
 \end{gathered}
 \tag{TB.1}
\]

For a trace there is more. Its defining equality makes \(\mathfrak n_\tau\) invariant under adjoints; a self-adjoint left ideal is two-sided, since \(xb=(b^*x^*)^*\). Thus \(\mathfrak n_\tau\) and its product span \(\mathfrak m_\tau\) are self-adjoint two-sided ideals. They need not be closed.

By WG004, there is a unique positive complex-linear extension \(\widetilde\tau:\mathfrak m_\tau\to\mathbb C\). It satisfies \(\widetilde\tau(a^*)=\overline{\widetilde\tau(a)}\). The proof defines it first on differences of finite positive elements, verifies independence by an equality involving only finite numbers, and then complexifies. In particular, no subtraction of infinite trace values occurs.

Polarizing the equality \(\widetilde\tau(w^*w)=\widetilde\tau(ww^*)\) on the complex vector space \(\mathfrak n_\tau\) gives
\(\widetilde\tau(y^*x)=\widetilde\tau(xy^*)\). To see exactly what polarization uses, substitute \(w=x+y\) and \(w=x+iy\), expand by linearity, and use the Hermitian identity to identify respectively the real and imaginary parts of the cross terms. Replacing \(y\) by \(y^*\) gives

\[
 \begin{gathered}
 \widetilde\tau(xy)=\widetilde\tau(yx)\\
 (x,y\in\mathfrak n_\tau).
 \end{gathered}
 \tag{TB.2}
\]

For \(b\in M\), \(x,y\in\mathfrak n_\tau\), both \(bx\) and \(yb\) lie in \(\mathfrak n_\tau\). Applying (TB.2) twice gives
\(\widetilde\tau((bx)y)=\widetilde\tau(y(bx))=\widetilde\tau(x(yb))\).
Products \(xy\) span \(\mathfrak m_\tau\), so

\[
 \begin{gathered}
 \widetilde\tau(ba)=\widetilde\tau(ab)\\
 (a\in\mathfrak m_\tau,\ b\in M).
 \end{gathered}
 \tag{TB.3}
\]

These finite-valued identities require the stated domains.

The bounded polar decomposition of BK07 also shows that, for either of these two-sided ideals, \(x\) belongs to the ideal if and only if \(|x|\) does: use \(x=v|x|\) and \(|x|=v^*x\). If \(a\in\mathfrak m_\tau\), then \(|a|\in F_\tau\) by (TB.1). Both \(|a|^{1/2}\) and \(v|a|^{1/2}\) lie in \(\mathfrak n_\tau\). Consequently every member of \(\mathfrak m_\tau\) is a **single** product of two members of \(\mathfrak n_\tau\), not merely a finite sum of such products. We call \(\mathfrak m_\tau\) the definition ideal.

If \(\tau\) is finite, then every positive element has finite trace because \(a\leq\|a\|1\); hence \(\mathfrak m_\tau=M\). The extension is bounded, with norm \(\tau(1)\): the Cauchy–Schwarz inequality WG005 gives
\(|\widetilde\tau(x)|^2\leq\tau(x^*x)\tau(1)\leq\|x\|^2\tau(1)^2\), and evaluation at the identity gives equality of norms when \(M\ne0\). The zero algebra has the same conclusion with norm zero. No normality assumption was used here.

Finally, every trace is invariant under unitary conjugation. For \(a\geq0\) and a unitary \(u\), apply the trace identity to \(ua^{1/2}\); its two squared products are \(a\) and \(uau^*\). This argument includes infinite values.

## Where finite approximation is possible

For any trace, even before assuming normality, WS02 constructs a projection \(e\in M\) such that

\[
 \begin{gathered}
 \overline{\mathfrak n_\tau}^{\mathrm{uw}}=Me,\\
 \overline{\mathfrak m_\tau}^{\mathrm{uw}}=eMe.
 \end{gathered}
 \tag{TB.4}
\]

Here “uw” denotes the ultraweak topology. The same closure equalities hold strongly and sigma-strongly. That proof gives the increasing finite positive contractions

\[
 \begin{gathered}
 u_a=a(1+a)^{-1},\\
 a\in F_\tau,\qquad u_a\uparrow e,
 \end{gathered}
 \tag{TB.5}
\]

where \(F_\tau\) is directed by positive order. It also identifies \(eH\) as the closed span of the ranges of all finite positive elements. The fact that these contractions increase follows from inverse order; their strong limit is the projection onto that span, as proved there.

Unitary conjugation permutes \(F_\tau\), so it preserves this closed span. Hence \(ueu^*=e\) for every unitary \(u\in M\). By BK08, unitaries span \(M\). Thus \(e\in Z(M)\), and \(eMe=Me\). This is the additional centrality supplied by the trace identity.

Let \(x\in(Me)_+\). The ordered approximants

\[
 \begin{gathered}
 y_a=x^{1/2}u_ax^{1/2},\\
 0\leq y_a\uparrow x
 \end{gathered}
 \tag{TB.6}
\]

have finite trace. Indeed, applying the trace identity to \(u_a^{1/2}x^{1/2}\) gives

\[
 \begin{gathered}
 \tau(y_a)=\tau(u_a^{1/2}xu_a^{1/2})\\
 \leq\|x\|\tau(u_a)<\infty.
 \end{gathered}
\]

Thus every nonzero positive \(x\) in this central corner dominates a nonzero finite positive element: otherwise all \(y_a\) would be zero, contradicting their strong limit \(x\). Conversely, a finite positive element belongs to \(eMe\) by WS02. Therefore \(M(1-e)\) contains no nonzero finite positive element.

This proves the equivalence between the course's density definition of semifiniteness and the order condition used for traces in Definition V.2.1: both say precisely \(e=1\). More strongly, the restriction to \(Me\) is semifinite, and

\[
 \begin{gathered}
 x\in(M(1-e))_+,\\ x\ne0\\
 \Longrightarrow\tau(x)=\infty.
 \end{gathered}
 \tag{TB.7}
\]

The restriction is a trace because \(e\) is central. If \(\tau\) is normal, both central restrictions are normal, and (TB.6) further gives \(\tau(x)=\sup_a\tau(y_a)\). Without normality we have only the stated order and strong-convergence assertions, not that equality of values.

The projection \(e\) is unique with these properties. If a central \(z\) also has a semifinite restriction and no nonzero finite positive element on its complement, every \(a\in F_\tau\) has \((1-z)a=0\), since that positive component has trace at most \(\tau(a)\). The range characterization gives \(e\leq z\). If \(z-e\ne0\), semifiniteness on \(Mz\) supplies a nonzero finite positive element below \(z-e\), contradicting (TB.7). Thus \(z=e\).

This proof yields the normal-trace decomposition of Lemma V.2.13, and also shows which assertions hold without normality. It does not impose the order condition on general weights: WG013 gives a normal semifinite weight for which that condition fails.

## Null support is a different central projection

Now suppose \(\tau\) is normal. By WS04, there is a largest projection \(q\) of trace zero, and a positive \(x\) has trace zero exactly when \(x=qxq\). That earlier proof takes finite joins of null projections and then their increasing supremum, using normality at the supremum. Its support-cutoff argument also proves the assertion for every positive element.

Conjugation by a unitary preserves null projections. By maximality, \(uqu^*=q\) for all unitaries, so \(q\) is central. Put

\[
 s(\tau)=1-q.
 \tag{TB.8}
\]

The trace vanishes on \((Mq)_+\), since every positive element there is bounded above by a scalar multiple of \(q\). Its restriction to \(Ms(\tau)\) is faithful: a positive zero there would also be supported in the orthogonal projection \(q\), hence would be zero. This restriction is normal, and central decomposition gives

\[
 \tau(x)=\tau(s(\tau)x)\quad(x\geq0).
\]

This remains valid at infinite values, since the omitted summand is zero.

The support is unique. If a central \(s'\) has faithful restriction and zero trace on its complement, then \(1-s'\leq q\). Also \(s'q\) is a null projection in the faithful corner, so \(s'q=0\), giving \(q\leq1-s'\). Thus \(s'=1-q\). Semifiniteness was not needed for this support theorem; when the whole trace is semifinite, its support restriction is semifinite too, by the order characterization in TB02. This covers the full statement of Proposition V.2.10 and its support definition.

Since \(\tau(q)=0<\infty\), the finite-domain projection satisfies \(q\leq e\). We therefore have three orthogonal central pieces:

\[
 q,\quad e-q,\quad1-e.
 \tag{TB.9}
\]

The trace is zero on the first, faithful and semifinite on the second, and infinite on every nonzero positive element of the third. Their sum is the identity. In particular, the faithful support \(1-q\) and the semifinite projection \(e\) need not coincide. For the zero trace they are respectively \(0\) and \(1\); for the trace that is infinite on every nonzero positive element they are respectively \(1\) and \(0\). Both conventions agree on the zero algebra, where \(1=0\).

## Arbitrary sums on disjoint supports

Let \((\tau_i)_{i\in I}\) be normal semifinite traces on the same algebra \(M\), with pairwise orthogonal supports \(s_i=s(\tau_i)\). Define

\[
 \begin{gathered}
 \tau(x)=\sum_{i\in I}\tau_i(x),\\
 x\in M_+.
 \end{gathered}
 \tag{TB.10}
\]

A sum of nonnegative extended numbers means the supremum over finite subsets of \(I\), including the empty subset. Additivity follows because any two finite index sets have a finite union: both inequalities between the sum of two suprema and the supremum of their finite sums follow this way. Homogeneity, the zero convention and the trace identity follow term by term. Hence (TB.10) is a trace.

It is normal. For \(x_\alpha\uparrow x\), normality of each summand and directedness of the net give, for each finite \(F\subseteq I\),

\[
 \sum_{i\in F}\sup_\alpha\tau_i(x_\alpha)
 =\sup_\alpha\sum_{i\in F}\tau_i(x_\alpha).
\]

For a finite target below the left side, choose sufficiently large values of the finitely many terms and then one common upper index; this proves the nontrivial inequality even if some supremum is infinite. Taking the supremum over \(F\) allows the two suprema to be interchanged. The result is \(\tau(x)=\sup_\alpha\tau(x_\alpha)\).

Let \(x\geq0\) be nonzero. If \(xs_i=0\) for every \(i\), TB03 gives \(\tau_i(x)=0\) for every \(i\), so \(x\) itself has finite trace. Otherwise choose \(i\) with \(xs_i\ne0\). Centrality gives \(0\leq xs_i\leq x\). Semifiniteness of \(\tau_i\) supplies \(0\ne y\leq xs_i\) with \(\tau_i(y)<\infty\). Its support is under \(s_i\): positivity of \(y\leq xs_i\) forces \(y^{1/2}(1-s_i)=0\). Orthogonality then gives \(\tau_j(y)=0\) for \(j\ne i\), by TB03. Hence \(\tau(y)=\tau_i(y)<\infty\). TB02 proves semifiniteness of the sum.

Its support is \(s=\bigvee_i s_i\). Indeed, \(\tau(x)=0\) is equivalent to \(\tau_i(x)=0\) for every \(i\), or \(xs_i=0\) for every \(i\); strong convergence of the finite projection sums makes this equivalent to \(xs=0\). TB03 characterizes the support by exactly these positive zeros. All assertions include empty families and zero summands.

The support hypothesis has content. On \(M=\mathbb C\), take \(\tau_n(t)=t\) for every positive integer \(n\). Each summand is faithful, finite and normal, but the sum is infinite at every \(t>0\). It is not semifinite. No claim about arbitrary overlapping sums follows from the disjoint-support theorem.

## Matrix amplification without a countable basis

Let \(\tau\) be a faithful normal semifinite trace on \(M\), and let \(K\) be any Hilbert space with orthonormal basis \((f_i)_{i\in I}\). The Hilbert tensor product used here is the completion of finite tensors with their product inner product. To check positivity of that inner product, express the finitely many first-coordinate vectors in an orthonormal basis of their finite-dimensional span: a tensor becomes \(\sum_r h_r\otimes k_r\) with orthonormal \(h_r\), and its squared norm is \(\sum_r\|k_r\|^2\). This also proves \(\|I_H\otimes b\|\leq\|b\|\); exchanging factors proves the corresponding bound for \(a\otimes I_K\). These bounded maps extend to the completion, with product and adjoint rules checked on finite tensors. Positive elementary tensors are positive because their square roots give a factorization as a bounded operator times its adjoint. In particular, identifying \(\xi\otimes f_i\) with the \(i\)-th copy of \(\xi\) gives the isometry onto the Hilbert direct sum of copies of \(H\).

On this Hilbert space put \(N=M\mathbin{\overline\otimes}B(K)\), the weak closure of the elementary tensor algebra, equivalently its bicommutant by BK02. For \(X\in N\), its entry is
\(X_{ji}=\iota_j^*X\iota_i\in M\), where \(\iota_i:H\to H\otimes K\) sends \(\xi\) to \(\xi\otimes f_i\). Membership in \(M\) holds first on elementary tensors and then on their weak closure, since coordinate compression is weakly continuous. For positive \(X\), define

\[
 \begin{gathered}\mathcal T(X)\\=\sum_{i\in I}\tau(X_{ii}).\end{gathered}
 \tag{TB.11}
\]

Additivity and homogeneity follow as in TB04. To prove the trace identity, let \(P_F\) project onto the span of a finite subset \(F\subseteq I\). The projections \(I_H\otimes P_F\) increase strongly to the identity, by finite-span density of an orthonormal basis. Consequently, for each \(i\),

\[
 \begin{gathered}
 (X^*X)_{ii}=\sum_{j\in I}X_{ji}^*X_{ji},\\
 (XX^*)_{jj}=\sum_{i\in I}X_{ji}X_{ji}^*.
 \end{gathered}
\]

These are bounded increasing strong sums of positive operators in \(M\); the first is obtained by compressing \(X^*(I_H\otimes P_F)X\), and the second in the same way with \(X^*\) in place of \(X\). Normality and the scalar trace identity therefore give

\[
 \begin{gathered}
 \mathcal T(X^*X)\\
 =\sum_i\sum_j\tau(X_{ji}^*X_{ji})\\
 =\sum_j\sum_i\tau(X_{ji}X_{ji}^*)\\
 =\mathcal T(XX^*).
 \end{gathered}
\]

Interchanging these sums is legitimate for arbitrary index sets: both sides are the supremum of finite sums over subsets of \(I\times I\). Thus \(\mathcal T\) is a trace.

If \(X_\alpha\uparrow X\), each diagonal entry increases to the corresponding entry of \(X\), by bounded monotone convergence and coordinate testing. Interchanging the increasing supremum with the finite-subset supremum, exactly as in TB04, proves normality. If \(X\geq0\) and \(\mathcal T(X)=0\), faithfulness of \(\tau\) gives \(X_{ii}=0\) for every \(i\). Hence \(X^{1/2}\iota_i=0\), by its squared norm on each vector. The ranges of all \(\iota_i\) have dense linear span, so \(X=0\). This proves faithfulness.

For semifiniteness, take the finite positive contractions \(u_a\uparrow1\) from TB02 and set

\[
 \begin{gathered}
 d_{a,F}=u_a\otimes P_F,\\
 d_{a,F}\uparrow1,
 \end{gathered}
 \tag{TB.12}
\]

with the product ordering on the two index sets. Positivity of tensor products gives monotonicity; strong convergence follows first on elementary tensors and then by their density and the uniform contraction bound. Moreover
\(\mathcal T(d_{a,F})=|F|\tau(u_a)<\infty\).
For \(X\geq0\), the elements \(X^{1/2}d_{a,F}X^{1/2}\) increase strongly to \(X\), lie below it, and have finite trace: the trace identity bounds their values by \(\|X\|\mathcal T(d_{a,F})\). A nonzero \(X\) has a nonzero member of this approximating net, proving semifiniteness by TB02. This argument avoids a separability assumption and avoids assuming that the diagonal corners of \(X\) are already trace-finite.

The trace is independent of the chosen basis. To compare two bases \((f_i)_{i\in I}\) and \((g_j)_{j\in J}\), put \(Y=X^{1/2}\) and form its rectangular coefficients from the \(f\)-coordinates to the \(g\)-coordinates. Their entries lie in \(M\) by the same coordinate-compression argument. The two positive-sum identities just proved express \(X_{ii}\) in the first basis as a column sum \(\sum_jY_{ji}^*Y_{ji}\), and \(X_{jj}\) in the second basis as a row sum \(\sum_iY_{ji}Y_{ji}^*\). The same trace and double-sum calculation equates the two values of (TB.11). No correspondence of individual basis vectors is asserted or needed.

For a unit vector \(f\in K\), this trace satisfies

\[
 \mathcal T(a\otimes p_f)=\tau(a)\quad(a\geq0),
\]

where \(p_f\) is its rank-one projection: choose a basis containing \(f\) in the basis-independent formula. When \(K=0\), the amplified algebra is zero and the empty sum is its zero trace, which is faithful and semifinite in the vacuous sense.

## Returning to an arbitrary type I factor

The preceding theorem is formulated on a specified tensor product with \(B(K)\). Here is the exact reduction from any type I factor in its given concrete representation. We use the intrinsic condition that a nonzero factor \(A\subseteq B(L)\) of type I contains a minimal nonzero projection \(p\).

First \(pAp=\mathbb Cp\). If a self-adjoint element of that corner were nonscalar, its continuous calculus from BK01 would have two nonzero positive continuous functions with disjoint supports. The support projection of either function, constructed by BK06, would be nonzero and strictly below \(p\): the other function has a nonzero range orthogonal to it. This contradicts minimality. Taking real and imaginary parts proves the assertion for all corner elements.

The closed subspace \([ApL]\) reduces both \(A\) and \(A'\). For the latter, use \(b'ap\xi=apb'\xi\); for the former, use the algebra and adjoints. Its projection therefore belongs to \(A'\cap A''=Z(A)\), by BK02. It is nonzero, so it is the identity, because \(A\) is a factor. In particular, if \(q\in A\) is a nonzero projection, then \(qAp\ne0\). The bounded polar decomposition of a nonzero \(qap\) supplies a partial isometry with initial projection a nonzero subprojection of \(p\), hence equal to \(p\), and final projection under \(q\).

Use Zorn's lemma to choose a maximal orthogonal family \((p_i)_{i\in I}\) of projections equivalent to \(p\), beginning with \(p\) itself. If its strong sum were not the identity, the preceding argument in the nonzero complement would supply another member. Thus \(\sum_i p_i=1\). Choose partial isometries \(w_i\in A\) with

\[
 \begin{gathered}w_i^*w_i=p,\\w_iw_i^*=p_i.\end{gathered}
 \tag{TB.13}
\]

Let \(E=pL\ne0\), \(K=\ell^2(I)\), and define

\[
 \begin{gathered}
 U:K\otimes E\longrightarrow L,\\
 U(\delta_i\otimes\xi)=w_i\xi.
 \end{gathered}
 \tag{TB.14}
\]

Orthogonality of the final projections makes this map isometric on finite sums; completeness extends it to an isometry on the tensor product. Its range contains every \(p_iL\), so their totality makes it onto. Thus \(U\) is a unitary with the specified coordinates.

For \(a\in A\), every coefficient \(w_i^*aw_j\) is a scalar multiple of \(p\). These scalars form a bounded matrix on \(K\): test finite scalar vectors against a fixed unit vector of \(E\), which bounds its norm by \(\|a\|\). Coordinate testing and density give \(U^*aU=B_a\otimes I_E\) for that bounded matrix \(B_a\). Conversely, every finite scalar matrix gives an element \(\sum_{i,j}b_{ij}w_iw_j^*\) of \(A\). For a bounded \(B\in B(K)\), its finite compressions \(P_FBP_F\) converge strongly to \(B\), with norms bounded by \(\|B\|\). Their images under \(U\) converge strongly to \(U(B\otimes I_E)U^*\), which belongs to the strongly closed algebra \(A\). We have proved the concrete equality

\[
 \begin{gathered}U^*AU\\=B(K)\otimes I_E.\end{gathered}
 \tag{TB.15}
\]

On \(H\otimes L\), conjugate \(M\mathbin{\overline\otimes}A\) by \(I_H\otimes U\), and associate the three Hilbert factors in their displayed order; the associating map is isometric on elementary tensors by the product inner product and extends onto by density. Equation (TB.15), first on elementary tensors and then by weak closure, identifies the image with
\((M\mathbin{\overline\otimes}B(K))\otimes I_E\). To justify closedness of this last image, if \(B_\alpha\otimes I_E\) converges weakly, compression by a fixed unit vector of \(E\) gives a weak limit \(B\) in \(M\mathbin{\overline\otimes}B(K)\); testing elementary tensors then identifies the original limit with \(B\otimes I_E\). This proves one inclusion. For the other, the finite matrix compressions of any \(B\in M\mathbin{\overline\otimes}B(K)\) have entries in \(M\), by TB05. They are finite sums \(\sum_{i,j\in F}B_{ij}\otimes e_{ij}\), converge strongly to \(B\), and have norms at most \(\|B\|\). Tensoring these bounded approximants with \(I_E\) preserves strong convergence, first on elementary tensors and then by density. Each approximant belongs to the conjugated tensor algebra; its strong limit therefore belongs there too. This proves the claimed equality without assuming weak continuity of infinite amplification on arbitrary unbounded nets.

The map \(B\mapsto B\otimes I_E\) is consequently a faithful normal star isomorphism onto this image. Positivity is reflected by testing vectors \(\eta\otimes\xi\) for a fixed unit \(\xi\in E\), and bounded increasing suprema are preserved and reflected by the same vector tests and finite-tensor density. Its inverse on this image has those properties as well.

Pulling back the trace of TB05 through these specified isomorphisms gives a faithful normal semifinite trace on \(M\mathbin{\overline\otimes}A\). Faithfulness follows from injectivity and positivity reflection, normality from preservation of bounded increasing suprema, and semifiniteness from carrying a nonzero finite positive subelement back through the order isomorphism. Thus the matrix construction proves the full type I factor statement, including representations with arbitrary multiplicity.

## Examples and the limits of the hypotheses

**Three different central parts in one trace.** On \(\mathbb C^3\), define, for \(a,b,c\geq0\),

\[
 \tau(a,b,c)=b+\infty\,c,
\]

with the fixed convention \(\infty\,0=0\). Additivity and homogeneity are coordinatewise; commutativity makes the trace identity automatic. It is normal: increasing coordinate nets have the usual scalar suprema; if the final third coordinate is positive, some net member already has positive third coordinate and hence infinite trace. The null projection is \(q=(1,0,0)\), the semifinite projection is \(e=(1,1,0)\), and the faithful support is \(s(\tau)=(0,1,1)\). The middle coordinate is the faithful semifinite piece. This computes, rather than identifies by analogy, all three parts in TB03.

**Normality is needed for recovery of values.** On \(\ell^\infty(\mathbb N)\), let \(\theta(a)=0\) for positive \(a\in c_0(\mathbb N)\), and \(\theta(a)=\infty\) for other positive \(a\). A sum of two nonnegative sequences tends to zero exactly when each does, proving additivity with extended values; scaling proves homogeneity. It is a trace because the algebra is commutative. It is semifinite: any nonzero positive sequence dominates a nonzero single-coordinate sequence of trace zero. But the finite-coordinate projections \(p_n\uparrow1\) have \(\theta(p_n)=0\), while \(\theta(1)=\infty\). Thus the value-recovery conclusion of TB02 and the largest-null-projection conclusion of TB03 fail without normality. Indeed each coordinate projection is null, so a largest null projection would dominate their supremum \(1\), which is not null. The underlying diagonal algebra is a von Neumann algebra by CY05.

**Semifinite is not finite, and finite is not faithful.** Counting trace on \(\ell^\infty(I)\) for an infinite set \(I\) is faithful, normal and semifinite, but has infinite value on the identity. Positivity of coordinate sums proves faithfulness, finite-coordinate suprema prove normality, and finite-coordinate subelements prove semifiniteness. On \(\mathbb C^2\), the trace \((a,b)\mapsto a\) is finite and normal but not faithful. The trace on \(\mathbb C\) taking infinity at every positive scalar is faithful and normal but not semifinite. These examples keep the four adjectives distinct; every finite trace is nevertheless semifinite, since all its positive values are finite.

**A finite-rank compression need not have finite amplified trace.** If \(\tau(1)=\infty\) and \(f\) is a unit vector, then \(I_H\otimes p_f\) has amplified trace \(\tau(1)=\infty\). The proof of TB05 therefore uses both a finite-coordinate projection and a finite-trace cutoff in \(M\). Its ordered approximation is \(X^{1/2}dX^{1/2}\), which lies below \(X\); the compression \(d^{1/2}Xd^{1/2}\) supplies the trace bound and need not lie below \(X\). Keeping those two roles separate is necessary even for finite matrices.
