# Operators recovered from small trace defects

**Self-checked by the writing AI.**

A large operator can become bounded after removing a projection with very small trace. This observation leads to a topology whose completion remembers both an operator and the vectors on which it acts. We construct that completion, recover its closed operators with their actual domains, and then characterize the result by spectral tails. Projection geometry provides the uniqueness argument that makes the algebraic operations rigorous.

The mathematical antecedents for this cluster are Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, items 2.1–2.11. The exposition is organized around quantitative cutoffs, the completed module and graph uniqueness; the spectral and trace statements appear after their domain requirements have been proved. The course audits record the exact source comparisons and the separate open closed-graph prerequisite.

## The traced representation and the inputs

Throughout, \(M\subseteq B(H)\) is a von Neumann algebra acting nondegenerately on a complex Hilbert space, and \(\tau:M_+\to[0,\infty]\) is a faithful normal semifinite trace. Neither \(H\) nor \(M\) is assumed separable, and no faithful normal state is assumed to exist. Inner products are linear in the first entry. The zero representation is allowed. Write \(e^\perp=1-e\) for a projection's complement.

The trace condition means \(\tau(x^*x)=\tau(xx^*)\) for every \(x\in M\); additivity, homogeneity, normality and faithfulness have the meanings fixed in OA-MOD-WG-002. The finite-domain algebra and its linear trace are supplied by WG-003–005. We use the bounded operator kernel, the spectral calculus of OA-MOD-SK-04–09, and the closed-operator polar decomposition of OA-MOD-RD-02. These inputs retain all operator domains. The additional closed graph theorem input is the exact Banach-space theorem that an everywhere defined linear map with closed graph between two Banach spaces is bounded; its open-source statement and specialization are bound in the trace-measure closed graph audit. It does not assert that an arbitrary densely defined closed operator is bounded.

A closed densely defined linear operator \(T:D(T)\subseteq H\to H\) is **affiliated** with \(M\) if every unitary \(u\in M'\) preserves \(D(T)\) and \(Tu\xi=uT\xi\) there. An equality of unbounded operators always includes equality of domains. Later, a product or sum with an overline denotes the closure of the ordinary operator on its ordinary domain; its existence will be proved before the notation is used as an algebraic operation.

## Projection geometry measures what is removed

Two projections \(e,f\in M\) are equivalent when a partial isometry \(v\in M\) satisfies \(v^*v=e\) and \(vv^*=f\). Write \(e\precsim f\) when \(e\) is equivalent to a subprojection of \(f\). The trace condition gives equal traces to equivalent projections, including when the common value is infinite. Consequently

\[
 e\precsim f\quad\Longrightarrow\quad\tau(e)\leq\tau(f).
 \tag{MT.1}
\]

**Projection estimates.** For any projections \(e,f\),

\[
 \tau(e\vee f)\leq\tau(e)+\tau(f),\qquad
 e\wedge f=0\ \Longrightarrow\ e\precsim f^\perp.
 \tag{MT.2}
\]

For a countable family \((e_j)\), the first inequality gives

\[
 \tau\!\left(1-\bigwedge_j e_j\right)
 \leq\sum_j\tau(1-e_j).
 \tag{MT.3}
\]

**Proof.** The bounded operator \((1-e)f\) belongs to \(M\). Its range closure is \((e\vee f-e)H\): projecting the closed span of \(eH+fH\) onto \((1-e)H\) leaves precisely the closure of \((1-e)fH\). Its right support is at most \(f\). Polar decomposition and (MT.1) therefore give \(\tau(e\vee f-e)\leq\tau(f)\). Add \(\tau(e)\), using the orthogonality of the two projections. If \(e\wedge f=0\), the operator \((1-f)e\) has zero kernel on \(eH\). Its polar decomposition has initial projection \(e\) and final projection at most \(1-f\), proving the second assertion. Finite induction and normality for the increasing finite joins prove (MT.3). \(\square\)

Here is a useful consequence with no subtraction of infinite traces. If projections \(e,f\) have the following property,

\[
 \text{for every }d>0\text{ there is }p\in\operatorname{Proj}(M)
 \text{ with }\tau(p^\perp)<d\text{ and }e\wedge p=f\wedge p,
 \tag{MT.4}
\]

then \(e=f\). Indeed, put \(r=e-(e\wedge f)\). A vector in \(rH\cap pH\) belongs to \((e\wedge p)H=(f\wedge p)H\), and also is orthogonal to \((e\wedge f)H\), so it is zero. Thus \(r\precsim1-p\), \(\tau(r)<d\), and faithfulness gives \(r=0\). Interchange \(e,f\).

For later cutoffs, if \(p_n\) increases and \(\tau(1-p_n)\to0\), then \(p_n\uparrow1\) strongly. Its strong supremum \(p\) lies in \(M\); \(\tau(1-p)\leq\tau(1-p_n)\) for every \(n\), so faithfulness gives \(p=1\).

## Two neighborhood systems and their estimates

For \(r,d>0\) define

\[
 \begin{aligned}
 U(r,d)&=\{x\in M:\ \|xp\|<r,\ \tau(1-p)<d
                    \text{ for some projection }p\in M\},\\
 V(r,d)&=\{\xi\in H:\ \|p\xi\|<r,\ \tau(1-p)<d
                    \text{ for some projection }p\in M\}.
 \end{aligned}
 \tag{MT.5}
\]

Their translates define the **measure topologies** on \(M\) and \(H\). The parameters are strictly positive, and the displayed inequalities are strict. These choices remove ambiguity at a spectral atom. Both families are balanced, are monotone in each parameter, and contain norm balls. The estimates below prove the addition and scalar-multiplication axioms; thus they define topological vector spaces.

For positive parameters,

\[
 \begin{aligned}
 U(r,d)^*&=U(r,d),\\
 U(r_1,d_1)+U(r_2,d_2)&\subseteq U(r_1+r_2,d_1+d_2),\\
 U(r_1,d_1)U(r_2,d_2)&\subseteq U(r_1r_2,d_1+d_2),\\
 V(r_1,d_1)+V(r_2,d_2)&\subseteq V(r_1+r_2,d_1+d_2),\\
 U(r_1,d_1)V(r_2,d_2)&\subseteq V(r_1r_2,d_1+d_2).
 \end{aligned}
 \tag{MT.6}
\]

**Proof of the adjoint estimate.** Suppose \(\|xp\|<r\). Choose \(c\) strictly between \(\|xp\|\) and \(r\), and let \(s=1_{(c,\infty)}(|x|)\). If \(0\ne\eta\in sH\cap pH\), the scalar spectral integral gives \(\|x\eta\|>c\|\eta\|\), contradicting the choice of \(c\). Hence \(s\wedge p=0\), and \(\tau(s)\leq\tau(1-p)\). If \(x=v|x|\) is its polar decomposition, set \(q=1-vsv^*\). Then \(\tau(1-q)=\tau(s)\) and \(\|qx\|\leq c<r\). Therefore \(\|x^*q\|<r\), proving one inclusion. Apply it to \(x^*\) for equality. This argument also gives a left cutoff with the same trace allowance whenever a right cutoff is given.

**Proof of the algebra estimates.** For sums, intersect the two witnessing projections and use (MT.3). For products, suppose \(\|ap\|<r_1\), \(\|bq\|<r_2\) with the corresponding trace bounds. Let \(k\) be the projection onto the kernel of \((1-p)b\). The right support of this operator is \(1-k\), and its left support is at most \(1-p\). Polar decomposition gives \(\tau(1-k)\leq\tau(1-p)\). On \(s=q\wedge k\), one has \(bs=pbs\), whence

\[
 \|abs\|=\|apbqs\|<r_1r_2,
 \qquad \tau(1-s)<d_1+d_2.
\]

**Proof of the vector estimates.** The sum estimate again uses an intersection. To prove the action estimate, take a left cutoff \(e\) for \(a\) with \(\|ea\|<r_1\), and choose \(q\) with \(\|q\xi\|<r_2\). Let \(l\) be the left support of \(a(1-q)\). Its right support is at most \(1-q\), so \(\tau(l)\leq\tau(1-q)\). With \(s=e\wedge(1-l)\),

\[
 sa\xi=saq\xi,\qquad
 \|sa\xi\|\leq\|ea\|\,\|q\xi\|<r_1r_2,
 \qquad \tau(1-s)<d_1+d_2.
\]

This proves the last line of (MT.6). \(\square\)

For scalar multiplication at a fixed \(x\) or \(\xi\), norm continuity gives continuity of \(z\mapsto zx\) and \(z\mapsto z\xi\). Continuity jointly in a scalar and a variable follows from balanced neighborhoods and the addition estimate. The countable families \(U(2^{-n},2^{-n})\) and \(V(2^{-n},2^{-n})\) are neighborhood bases.

## Separation and bounded sets

**The measure topologies are Hausdorff.** To see this first for \(H\), suppose \(\xi\in V(2^{-n},2^{-n})\) for every \(n\), witnessed by \(q_n\). Put \(p_n=\bigwedge_{j\geq n}q_j\). Formula (MT.3) gives \(\tau(1-p_n)\leq2^{1-n}\); hence \(p_n\uparrow1\) strongly. For every \(j\geq n\),

\[
 \|p_n\xi\|=\|p_nq_j\xi\|<2^{-j}.
\]

Thus \(p_n\xi=0\), and \(\xi=0\). If \(a\) lies in every operator neighborhood, then for each fixed \(\xi\), the last estimate in (MT.6), applied with \(\xi\) in a suitable norm ball, places \(a\xi\) in every vector neighborhood. Hence \(a\xi=0\) for every \(\xi\), and \(a=0\).

A subset \(S\) of either space is **bounded in measure** if every neighborhood of zero absorbs it: for each neighborhood \(W\) there is \(t_0>0\) such that \(tS\subseteq W\) whenever \(|t|\leq t_0\). In terms of (MT.5), this says that for every \(d>0\) there is a finite \(R\) such that \(S\subseteq U(R,d)\), or \(S\subseteq V(R,d)\), respectively. Indeed, scaling changes only the first parameter. Singletons and norm-bounded sets are bounded in measure.

Multiplication and the action are jointly continuous and uniformly continuous on every product of two bounded-in-measure sets. Here is the quantitative point. If \(a,b\) range over such fixed sets, choose \(R_1,R_2\) giving cutoffs with trace allowance \(d/8\). For perturbations \(h,k\in U(s,d/8)\),

\[
 (a+h)(b+k)-ab=ak+hb+hk.
\]

By (MT.6), the right side belongs to

\[
 U(R_1s+R_2s+s^2,\,3d/4).
 \tag{MT.7}
\]

Choose \(s\) with the first parameter smaller than the desired \(r\). The same calculation, with \(b,k\) replaced by \(\xi,\eta\) and the appropriate vector neighborhoods, proves uniform continuity of the action. Fixed pairs are covered by singleton sets. Involution and both additions are uniformly continuous on the whole spaces.

Every Cauchy sequence is bounded in measure. For a prescribed \(d\), its tail differs from one term by elements of \(U(1,d/2)\), or \(V(1,d/2)\). Absorb that one term with trace allowance \(d/2\), and then absorb the finitely many terms before the tail by increasing the first parameter. This observation is essential: continuity alone would not justify multiplying two arbitrary Cauchy sequences.

## Completing the algebra and its representation together

Let \(\widehat M\) and \(\widehat H\) be the Hausdorff completions of the two additive uniform spaces just constructed. One explicit construction uses Cauchy sequences, with \((x_n)\) and \((y_n)\) equivalent when \(x_n-y_n\to0\) in measure. Constant sequences embed the original spaces injectively by MT-04. Neighborhoods of a class are obtained by requiring an approximating sequence eventually to lie in a prescribed neighborhood, and allowing a smaller neighborhood before taking its closure. The sum estimate in (MT.6) shows that this definition is independent of representatives and has the same uniform structure on the embedded original space.

For completeness of this construction, choose a subsequence from a Cauchy sequence of classes whose successive differences lie in neighborhoods with both parameters at most \(2^{-n}\). Choose representatives in the original space with errors in the same neighborhoods. Their successive differences then have summable parameters. Finite addition in (MT.6) proves that the representatives are Cauchy and that their class is the limit of the selected subsequence, hence of the original Cauchy sequence. A Cauchy net reduces to this case by choosing, for each member of the countable neighborhood base, an index after which all its differences lie in that neighborhood. The resulting Cauchy sequence has the same limit as the net. Thus the construction is a full uniform completion, not merely a sequential closure.

The operations are defined on representatives:

\[
 [a_n]^*=[a_n^*],\quad
 [a_n]+[b_n]=[a_n+b_n],\quad
 [a_n][b_n]=[a_nb_n],\quad
 [a_n][\xi_n]=[a_n\xi_n].
 \tag{MT.8}
\]

MT-04 proves that these are Cauchy sequences and are unchanged by changing representatives. For example, the difference of two representative products is
\((a_n-a'_n)b_n+a'_n(b_n-b'_n)\); each factor sequence is bounded in measure and (MT.7) makes the difference tend to zero. The vector action has the identical argument with its proved vector estimate. Addition, associativity, distributivity, the star laws and the module identity now follow term by term before passage to equivalence classes. The identity of \(M\) remains the identity of \(\widehat M\) and of its action on \(\widehat H\).

All five operations retain their continuity properties: the star and additions are uniformly continuous everywhere, and multiplication and action are uniformly continuous on products of sets bounded in measure in the completed spaces. To check the latter assertion without assuming bounded representatives, fix a target neighborhood and a bounded set in the completion. Choose its uniform cutoff bound with a smaller trace allowance. By density, each of its elements can be approximated within one still smaller neighborhood by an element of the original space. These approximants have one common enlarged cutoff bound, by the addition estimate. Apply (MT.7) to them and let the approximation error tend to zero, reserving a smaller first and second parameter before taking closures. This proves precisely the desired uniform estimate for the completed bounded sets.

Norm convergence in \(M\) or \(H\) implies convergence in measure, so norm limits that already exist agree with their limits in the completion. Elements of \(M'\) act continuously on \(\widehat H\): for \(b\in M'\), \(p b\xi=b p\xi\), and hence \(bV(r,d)\subseteq V(\|b\|r,d)\) when \(b\ne0\); the zero case is immediate. Their action commutes with \(\widehat M\), first on the original spaces and then by density and continuity.

## Bounded pieces of an element of the completion

**Cutoff theorem.** Given \(a\in\widehat M\), there are increasing projections \(p_n\in M\) such that

\[
 \tau(1-p_n)\longrightarrow0,\qquad ap_n\in M.
 \tag{MT.9}
\]

In particular, a bounded piece can be found with any prescribed positive trace defect.

**Proof.** Choose \(a_n\in M\) converging to \(a\), and pass to a subsequence for which \(a_{n+1}-a_n\in U(2^{-n},2^{-n})\). Take witnessing projections \(q_n\), and set \(p_n=\bigwedge_{j\geq n}q_j\). The trace defect is at most \(2^{1-n}\), and \(p_n\) increases. For fixed \(n\),

\[
 a_kp_n=a_np_n+\sum_{j=n}^{k-1}(a_{j+1}-a_j)p_n
 \qquad(k>n).
 \tag{MT.10}
\]

The summands have norms less than \(2^{-j}\), so the series converges in operator norm to some \(c_n\in M\). Continuity of multiplication in the completion gives \(a_kp_n\to ap_n\) in measure, while norm convergence gives the measure limit \(c_n\). Separation proves \(ap_n=c_n\). \(\square\)

For a projection \(p\), membership \(ap\in M\) means equality in \(\widehat M\) to an actual bounded operator. It is not a formal statement that the product of an unbounded symbol and a projection is always bounded. Also, \(p_n\to1\) in measure whenever \(\tau(1-p_n)\to0\): the complement is annihilated on \(p_n\). Therefore

\[
 ap_n\longrightarrow a\quad\text{in measure}.
 \tag{MT.11}
\]

## Closed graphs detected outside small defects

We first record the promised closed graph specialization. If a closed operator \(T\) has \(eH\subseteq D(T)\), define \(A:H\to H\) by \(A\xi=T(e\xi)\). Its graph is the inverse image of the closed graph of \(T\) under the continuous map \((\xi,\eta)\mapsto(e\xi,\eta)\). It is therefore closed, and the exact Banach closed graph theorem in MT-01 makes \(A\) bounded. If \(T\) is affiliated and \(e\in M\), \(A\) commutes with every unitary of \(M'\); the four-unitary span and bicommutant theorem give

\[
 eH\subseteq D(T)\quad\Longrightarrow\quad Te\in M.
 \tag{MT.12}
\]

For a closed densely defined affiliated operator \(T\), its graph projection \(g_T\) belongs to \(M_2(M)\). Indeed, \(\operatorname{graph}(T)\) is invariant under both \(\operatorname{diag}(u,u)\) and its inverse for every unitary \(u\in M'\). It is a reducing subspace for these unitaries, so its orthogonal projection commutes with them. Each of the four matrix entries then belongs to \((M')'=M\).

For clarity, the projection itself is determined by the closed polar decomposition. Write \(h=|T|\), \(T=vh\),

\[
 c=(1+h^2)^{-1/2},\qquad b=Tc=v h(1+h^2)^{-1/2}.
\]

Both \(c,b\) are bounded, \(cH=D(T)\), and \(c^2+b^*b=1\). The map \(W\xi=(c\xi,b\xi)\) is therefore an isometry onto \(\operatorname{graph}(T)\). Onto follows because for \(\eta\in D(h)\), \((1+h^2)^{1/2}\eta\in H\), and applying \(W\) to that vector gives \((\eta,T\eta)\). Consequently

\[
 g_T=WW^*=\begin{pmatrix}c^2&cb^*\\bc&bb^*\end{pmatrix}.
 \tag{MT.13}
\]

Every entry in this formula is a product of bounded operators. No unbounded matrix product is left implicit.

On positive matrices define \(\tau_2(X)=\tau(X_{11})+\tau(X_{22})\). Additivity and normality follow on the two diagonal entries. Faithfulness follows because zero diagonal quadratic forms force a positive matrix's square root to vanish on both coordinate spaces. Finally
\(\tau_2(Y^*Y)=\sum_{i,j}\tau(Y_{ij}^*Y_{ij})
=\sum_{i,j}\tau(Y_{ij}Y_{ij}^*)=\tau_2(YY^*)\).
This trace is also semifinite. To see this using the finite-domain definition in WG-002–003, write \(E_{ij}(x)\) for the matrix with entry \(x\) in position \((i,j)\) and zero elsewhere. If \(x\in\mathfrak n_\tau\), then \(E_{ij}(x)^*E_{ij}(x)=E_{jj}(x^*x)\) has finite \(\tau_2\)-trace, so \(E_{ij}(x)\in\mathfrak n_{\tau_2}\). For any fixed row index \(k\),

\[
 E_{ki}(x)^*E_{kj}(y)=E_{ij}(x^*y)
 \qquad(x,y\in\mathfrak n_\tau).
\]

Consequently \(\mathfrak m_{\tau_2}\) contains every matrix with entries in \(\mathfrak m_\tau\). These matrices are ultraweakly dense in \(M_2(M)\): the finite matrix-entry maps are ultraweakly continuous, and \(\mathfrak m_\tau\) is ultraweakly dense in \(M\) by semifiniteness. Thus \(\tau_2\) is semifinite in precisely the sense of WG-002. The projection estimates and the projection uniqueness assertion of MT-02 therefore apply in this matrix algebra. Their proofs themselves only need faithfulness, normality and the trace identity.

**Graph uniqueness theorem.** Let \(S,T\) be closed densely defined affiliated operators. Suppose that for every \(d>0\) a projection \(p\) exists with \(\tau(1-p)<d\) such that

\[
 \begin{aligned}
 pH\cap D(S)\cap S^{-1}(pH)
 &=pH\cap D(T)\cap T^{-1}(pH)=D_p,\\
 S\xi&=T\xi\qquad(\xi\in D_p).
 \end{aligned}
 \tag{MT.14}
\]

Then \(S=T\). In particular it suffices that, for every \(d>0\), such a \(p\) has \(pH\subseteq D(S)\cap D(T)\) and \(Sp=Tp\).

**Proof.** Formula (MT.14) says exactly that

\[
 g_S\wedge\operatorname{diag}(p,p)
 =g_T\wedge\operatorname{diag}(p,p).
\]

The complement of the diagonal projection has \(\tau_2\)-trace less than \(2d\). Apply (MT.4) in the matrix algebra to obtain \(g_S=g_T\), hence equality of the graphs. The stated special case implies (MT.14), since the two restrictions on all of \(pH\) already agree. \(\square\)

## The operator associated to a completion element

For \(a\in\widehat M\) define

\[
 \begin{aligned}
 D(T_a)&=\{\xi\in H:a\xi\text{ belongs to the embedded copy of }H
                                     \text{ in }\widehat H\},\\
 T_a\xi&=a\xi\quad(\xi\in D(T_a)),
 \end{aligned}
 \tag{MT.15}
\]

where the second equality is interpreted using that injective embedding.

**Realization theorem.** The operator \(T_a\) is closed, densely defined and affiliated with \(M\). It has no proper closed affiliated extension. Moreover, \(a\mapsto T_a\) is injective and extends the original representation of \(M\).

**Proof.** If \(ap\in M\), then for \(\xi\in H\) the module identity gives \(a(p\xi)=(ap)\xi\in H\). Thus \(pH\subseteq D(T_a)\) and \(T_ap=ap\). The projections of MT-06 increase strongly to one, proving density.

If \(\xi_n\in D(T_a)\), \(\xi_n\to\xi\) in Hilbert norm and \(T_a\xi_n\to\eta\) in Hilbert norm, both convergences hold in \(\widehat H\). Continuity of multiplication by the fixed element \(a\) gives \(a\xi_n\to a\xi\) there. Separation therefore gives \(a\xi=\eta\); this is exactly \(\xi\in D(T_a)\) and \(T_a\xi=\eta\). Hence \(T_a\) is closed.

For a unitary \(u\in M'\), MT-05 gives \(a(u\xi)=u(a\xi)\). Both \(u\) and \(u^*\) preserve the original \(H\) inside \(\widehat H\), so they preserve \(D(T_a)\) and commute with its action. This proves affiliation. If a closed affiliated \(S\) extends \(T_a\), then on the projections in (MT.9), \(Sp=T_ap\); MT-07 gives \(S=T_a\).

Finally, if \(T_a=T_b\), choose cutoffs for \(a,b\) with arbitrarily small trace defect and intersect them. On their intersection \(p\), the bounded operators \(ap=T_ap\) and \(bp=T_bp\) agree. Select such \(p_n\) with defects tending to zero. Then \((a-b)p_n=0\), and continuity together with \(p_n\to1\) in measure gives \(a=b\). For \(a\in M\), the original action sends all \(H\) into itself and (MT.15) is exactly the bounded operator \(a\). \(\square\)

## Adjoint, addition and multiplication keep the domains

For all \(a,b\in\widehat M\),

\[
 T_{a^*}=T_a^*,\qquad
 T_{a+b}=\overline{T_a+T_b},\qquad
 T_{ab}=\overline{T_aT_b}.
 \tag{MT.16}
\]

The ordinary domains on the right are, respectively,
\(D(T_a)\cap D(T_b)\) and
\(\{\xi\in D(T_b):T_b\xi\in D(T_a)\}\).
Both are dense, and their operators are closable.

**Adjoints.** Put \(T=T_a\). For its spectral projections \(q_n=1_{[0,n]}(|T|)\), the closed polar calculus gives \(q_n\uparrow1\), \(Tq_n\in M\), and \(Tq_n\xi\to T\xi\) for every \(\xi\in D(T)\). These are graph cutoffs; no assertion about their trace defects is needed. Since \(a q_n\) acts on every vector as the bounded operator \(Tq_n\), injectivity in MT-08 gives \(a q_n=Tq_n\) in \(\widehat M\).

Choose a projection \(p\) with \(a^*p\in M\) and small trace defect. For \(\eta\in pH\) and \(\xi\in D(T)\), use the bounded adjoint identity and (MT.8):

\[
 \begin{aligned}
 \langle Tq_n\xi,\eta\rangle
 &=\langle\xi,(Tq_n)^*p\eta\rangle\\
 &=\langle\xi,q_n(a^*p)\eta\rangle
 \longrightarrow\langle\xi,(a^*p)\eta\rangle.
 \end{aligned}
 \tag{MT.17}
\]

Thus \(pH\subseteq D(T^*)\) and \(T^*p=a^*p=T_{a^*}p\). In particular \(T^*\) is densely defined, even directly from these cutoffs. It is closed and affiliated: the adjoint test transfers the commutation with each unitary of \(M'\). Graph uniqueness proves \(T^*=T_{a^*}\).

**Sums.** The module identity gives \(T_a+T_b\subseteq T_{a+b}\). The sum is therefore closable. Intersect cutoffs for \(a,b\); their ranges lie in its domain, so this domain is dense. The closure is affiliated because its graph is the closure of a graph invariant under the diagonal commutant unitaries. On the intersected cutoffs it agrees with \(T_{a+b}\). MT-07 gives equality.

**Products.** Again the module identity gives \(T_aT_b\subseteq T_{ab}\). Choose \(p,q\) with small trace defects and \(ap,bq\in M\), and put \(c=bq\in M\). Let \(k\) be the kernel projection of \((1-p)c\), and put \(s=q\wedge k\). As in MT-03,

\[
 \tau(1-s)\leq\tau(1-q)+\tau(1-p).
\]

For \(\xi\in sH\), \(\xi\in D(T_b)\), \(T_b\xi=c\xi\in pH\subseteq D(T_a)\), and \(T_aT_b\xi=T_{ab}\xi\). Arbitrarily small defects prove density of the product domain. The inclusion proves closability; graph invariance proves affiliation of the closure. Apply graph uniqueness once more. \(\square\)

This establishes the algebra laws for closed sums and products without treating three unbounded factors as if they were everywhere defined. Associativity belongs first to \(\widehat M\), where it was proved using bounded Cauchy representatives; (MT.16) transports it to the closed operators.

## Increasing domains determine a unique closed operator

**Increasing-domain theorem.** Suppose \(p_n\in M\) increases, \(\tau(1-p_n)\to0\), and a linear operator \(A\) is defined on

\[
 D_0=\bigcup_n p_nH.
\]

Assume that each everywhere defined map \(Ap_n:H\to H\) is a bounded member of \(M\). Then \(A\) is closable, and there is a unique \(a\in\widehat M\) such that

\[
 \overline A=T_a.
 \tag{MT.18}
\]

**Proof.** Set \(a_n=Ap_n\). Whenever \(m,n\geq k\),
\((a_m-a_n)p_k=0\). Since \(\tau(1-p_k)\to0\), this makes \((a_n)\) Cauchy in measure, regardless of how quickly the norms \(\|a_n\|\) grow. Let \(a\) be its limit in \(\widehat M\).

If \(\xi\in p_kH\), then \(a_n\xi=A\xi\) for all \(n\geq k\). Continuity of the action gives \(a\xi=A\xi\) in \(\widehat H\). The right side belongs to \(H\), so \(A\subseteq T_a\). Therefore \(A\) is closable and its closure is densely defined, because \(p_n\uparrow1\).

The domain \(D_0\) is invariant under each unitary \(u\in M'\), since every \(p_n\) commutes with \(u\). For \(\xi\in p_nH\),
\(Au\xi=Ap_nu\xi=uAp_n\xi=uA\xi\).
This proves affiliation of the graph closure. It agrees with \(T_a\) on every \(p_nH\), and graph uniqueness gives (MT.18). Injectivity in MT-08 gives uniqueness of \(a\). \(\square\)

The compatibility here is carried by the single operator \(A\). If bounded operators \(c_n\) are supplied instead, the sufficient compatibility condition is \(c_np_n=c_n\) and \(c_mp_n=c_n\) for \(m\geq n\); then \(A\xi=c_n\xi\) for \(\xi\in p_nH\) is well defined and the theorem applies.

## Spectral tails characterize the resulting operators

A closed densely defined affiliated operator is called **\(\tau\)-measurable** when it is \(T_a\) for some \(a\in\widehat M\). Write \(S(M,\tau)\) for this set of concrete operators. The following characterization also makes sense without referring to the completion.

**Spectral-tail theorem.** For a closed densely defined affiliated \(T\), with \(h=|T|\), the following are equivalent:

1. \(T\in S(M,\tau)\).
2. For every \(d>0\), some projection \(p\in M\) has \(\tau(1-p)<d\) and \(pH\subseteq D(T)\).
3. \(\tau(1_{(R,\infty)}(h))\to0\) as \(R\to\infty\).
4. \(\tau(1_{(R_0,\infty)}(h))<\infty\) for at least one finite \(R_0\geq0\).

**Proof.** The implication 1 to 2 follows from MT-06 and MT-08. For 2 to 3, the closed graph specialization makes \(Tp\) bounded. If \(R>\|Tp\|\), the spectral projection \(s=1_{(R,\infty)}(h)\) has zero intersection with \(p\): a nonzero vector in the intersection lies in \(D(T)\) and has squared spectral integral strictly greater than \(R^2\) times its squared norm, contradicting the bound on \(Tp\). Hence \(\tau(s)\leq\tau(1-p)<d\) by MT-02. Since \(d\) is arbitrary, the tails tend to zero. The implication 3 to 4 is immediate.

For 4 to 3, set \(s_R=1_{(R,\infty)}(h)\) for \(R\geq R_0\). The differences \(s_{R_0}-s_R\) increase strongly to \(s_{R_0}\). Normality and finiteness of \(\tau(s_{R_0})\) imply

\[
 \tau(s_R)=\tau(s_{R_0})-\tau(s_{R_0}-s_R)\longrightarrow0.
\]

Only finite numbers are subtracted in this argument.

Finally, if 3 holds, take \(p_n=1_{[0,n]}(h)\). These projections increase, their trace defects tend to zero, and \(Tp_n\in M\) by the polar calculus. The restriction of \(T\) to \(\bigcup_n p_nH\) has closure \(T\), because the spectral cutoffs converge in its graph norm. MT-10 now gives \(T=T_a\) for a unique \(a\in\widehat M\). \(\square\)

In condition 2, the projection is allowed to depend on \(d\); there is no assertion of a common domain for all measurable operators. Nevertheless the proof of MT-09 supplies a trace-dense domain for each particular finite sum or product. Affiliation alone is weaker than measurability: it gives bounded spectral cutoffs, but does not force their complement traces to be finite or to tend to zero.

## Positivity, square roots and polar decomposition

The bijection \(a\mapsto T_a\) identifies \(\widehat M\) with the complete topological star-algebra \(S(M,\tau)\), whose operations are (MT.16). Its positive cone can equivalently be described as

\[
 \widehat M_+=\{b^*b:b\in\widehat M\}
 =\{a\in\widehat M:T_a\text{ is positive self-adjoint}\}.
 \tag{MT.19}
\]

Every positive element has a unique positive square root. This is a pointed convex cone, and every \(a\in\widehat M\) has a polar decomposition

\[
 a=v|a|,\qquad v\in M,\qquad |a|=(a^*a)^{1/2},
 \tag{MT.20}
\]

with the usual initial and final support projections and uniqueness of \(v\) on the support of \(|a|\).

**Proof.** The operator corresponding to \(b^*b\) is \(T_b^*T_b\). This ordinary product is already the positive self-adjoint operator furnished by the closed polar calculus, so its closure in (MT.16) changes nothing. Conversely, if \(A=T_a\) is positive self-adjoint, its positive square root is affiliated; its spectral tail above \(R\) is the spectral tail of \(A\) above \(R^2\). MT-11 makes \(A^{1/2}\) measurable, and (MT.16) gives \(a=b^*b\) for its corresponding positive element \(b\). Uniqueness of the positive operator square root in the spectral calculus, followed by injectivity, gives uniqueness in the algebra.

If \(a,b\) correspond to positive operators, \(a+b\) is self-adjoint by (MT.16). Its operator is the closure of their sum. On the dense sum domain its quadratic form is nonnegative, and this remains true on the graph closure by continuity of the inner product. Thus it is positive self-adjoint. Nonnegative scaling is immediate. If both \(A\) and \(-A\) are positive, then \(\langle A\xi,\xi\rangle=0\) on \(D(A)\). Polarization gives \(\langle A\xi,\eta\rangle=0\) for \(\xi,\eta\in D(A)\); density gives \(A\xi=0\). Its closed graph and dense domain then imply \(A=0\) on all of \(H\). This proves pointedness.

For general \(T_a=v h\), the closed polar calculus puts \(v\) in \(M\), while \(h\) is measurable by MT-11 because it has the same spectral tails used there. Also \(T_a^*T_a=h^2\), so the square-root assertion identifies its algebra element as \(|a|\). The polar equality and its supports are transported to (MT.20) by (MT.16) and injectivity. \(\square\)

## The first integral and the bounded trace ideals

For a positive measurable \(h\), define its extended trace by

\[
 \tau(h)=\lim_{\varepsilon\downarrow0}
       \tau\bigl(h(1+\varepsilon h)^{-1}\bigr).
 \tag{MT.21}
\]

The expression inside the trace is a bounded positive member of \(M\). Its scalar spectral function increases to the identity function, so the limit exists in \([0,\infty]\). Equivalently, if \(E_h\) is the spectral measure, normality makes \(B\mapsto\tau(E_h(B))\) a countably additive extended measure, and

\[
 \tau(h)=\int_{[0,\infty)}t\,d(\tau\circ E_h)(t)
        =\sup_n\tau\bigl(\min(h,n)\bigr).
 \tag{MT.22}
\]

These equalities follow first for nonnegative simple spectral functions and then by monotone convergence. Infinite mass at zero causes no problem because the integrand there is zero. On bounded positive \(h\), (MT.21) agrees with the original trace by normality.

Every measurable \(x=v|x|\) has bounded regularizations

\[
 x_\varepsilon=x(1+\varepsilon|x|)^{-1}\in M,
 \qquad x_\varepsilon\longrightarrow x\quad\text{in measure}.
 \tag{MT.23}
\]

Indeed, boundedness follows from \(t/(1+\varepsilon t)\leq1/\varepsilon\). On a fixed spectral cutoff \(e_R=1_{[0,R]}(|x|)\),

\[
 \|(x-x_\varepsilon)e_R\|
 \leq\frac{\varepsilon R^2}{1+\varepsilon R}\longrightarrow0.
\]

First choose \(R\) making \(\tau(1-e_R)\) small, then choose \(\varepsilon\) making this norm small. This proves precisely convergence in the topology already constructed.

We also need the trace identities on the original bounded algebra. Put

\[
 \mathfrak n_\tau=\{z\in M:\tau(z^*z)<\infty\},\qquad
 \mathfrak m_\tau=\operatorname{span}(\mathfrak n_\tau^*\mathfrak n_\tau).
\]

Both are two-sided ideals, and \(\mathfrak n_\tau\) is invariant under adjoints. The linear trace on \(\mathfrak m_\tau\) satisfies

\[
 \tau(xy)=\tau(yx)\quad(x,y\in\mathfrak n_\tau),\qquad
 \tau(ab)=\tau(ba)\quad(a\in\mathfrak m_\tau,\ b\in M).
 \tag{MT.24}
\]

**Proof of the ideal and cyclicity assertions.** Adjoint invariance is the trace condition. For \(b\in M\),

\[
 \begin{aligned}
 \tau((bz)^*(bz))&\leq\|b\|^2\tau(z^*z),\\
 \tau((zb)^*(zb))&=\tau(zbb^*z^*)
                      \leq\|b\|^2\tau(zz^*)
                      =\|b\|^2\tau(z^*z).
 \end{aligned}
\]

Thus \(\mathfrak n_\tau\) is two-sided; its product span is too. Polarizing the identity \(\tau(w^*w)=\tau(ww^*)\) on the complex vector space \(\mathfrak n_\tau\) gives \(\tau(z^*w)=\tau(wz^*)\). Replacing \(z\) by \(x^*\) proves the first identity in (MT.24).

For the second, every \(a\in\mathfrak m_\tau\) can be factored as \(a=xy\) with \(x,y\in\mathfrak n_\tau\). To justify this beyond positive \(a\), write its bounded polar decomposition \(a=v|a|\). The two-sided ideal property puts \(|a|=v^*a\) in \(\mathfrak m_\tau\). By the finite-positive-domain identity in WG-003, \(\tau(|a|)<\infty\). Hence take \(x=v|a|^{1/2}\) and \(y=|a|^{1/2}\). Now \(yb,bx\in\mathfrak n_\tau\), and repeated use of the already proved two-factor identity gives

\[
 \tau(ab)=\tau(x(yb))=\tau((yb)x)
          =\tau(y(bx))=\tau((bx)y)=\tau(ba).
\]

All expressions belong to the finite trace ideal, so no infinite scalar subtraction is involved. \(\square\)

A useful refined Cauchy–Schwarz estimate is

\[
 |\tau(xy)|^2
 \leq \tau(|x^*|\,|y|)\,\tau(|x|\,|y^*|),
 \qquad x\in\mathfrak m_\tau,\quad y\in M.
 \tag{MT.25}
\]

The two traces on the right are nonnegative finite real numbers even though their written bounded products need not be positive operators: cyclicity identifies each with a positive sandwich.

**Proof.** Write \(x=u h\), \(y=v k\), where \(h=|x|\), \(k=|y|\). Set

\[
 z=h^{1/2}v k^{1/2},\qquad w=k^{1/2}u h^{1/2}.
\]

Both lie in \(\mathfrak n_\tau\), because \(h^{1/2}\) does and this is a two-sided ideal. Cyclicity gives \(\tau(xy)=\tau(zw)\). Apply the weight Cauchy–Schwarz inequality to \(z^*,w\):

\[
 |\tau(zw)|^2\leq\tau(zz^*)\tau(w^*w).
\]

Again by cyclicity,

\[
 \tau(zz^*)=\tau(h vkv^*)=\tau(|x|\,|y^*|),\qquad
 \tau(w^*w)=\tau(u h u^* k)=\tau(|x^*|\,|y|).
\]

The identities \(vkv^*=|y^*|\) and \(uhu^*=|x^*|\) are the bounded polar calculus, including their zero-support parts. This proves (MT.25). \(\square\)

The construction (MT.21) is the positive spectral integral. Its full algebraic extension to all integrable measurable operators, the measure-closed integral estimates and the ensuing \(L^p\) spaces require further results; (MT.24)–(MT.25) have been asserted and proved here on their stated bounded ideals.

## Three models that separate the assumptions

**A diffuse finite trace permits unbounded operators.** On \(H=L^2(0,1)\), let \(M=L^\infty(0,1)\) act by multiplication and \(\tau(f)=\int_0^1f(t)\,dt\) for \(f\geq0\). Multiplication by \(g(t)=t^{-2}\), on the domain where \(g\xi\in L^2\), is closed and affiliated. For \(R\geq1\),

\[
 \tau(1_{(R,\infty)}(|g|))=R^{-1/2}.
\]

It is measurable, although it is unbounded. Multiplication by any measurable function finite almost everywhere is similarly measurable: its high-value sets decrease to a null set, and the ambient measure is finite. The criterion explicitly excludes a function infinite on a set of positive measure, since it would not give a densely defined multiplication operator.

**The counting trace can force boundedness.** Let \(M=B(\ell^2(I))\) with its canonical trace, for an arbitrary index set \(I\). Every nonzero projection has trace at least one. A spectral tail with trace less than one must therefore be zero. MT-11 shows that every measurable operator is bounded, so \(S(M,\tau)=M\). In both neighborhood systems, taking \(d<1\) forces the witnessing projection to be one. Thus both measure topologies are exactly the original norm topologies and \(\widehat H=H\). The affiliated diagonal operator \(De_n=ne_n\) on \(\ell^2(\mathbb N)\) is not measurable: every tail projection has infinite trace. Strong convergence of its bounded spectral cutoffs does not imply convergence in this measure topology.

**A trace with uncountable support still has measurable unbounded elements.** Let \(I\) be uncountable and \(M=\ell^\infty(I)\) act diagonally on \(\ell^2(I)\). Choose distinct \(i_n\in I\), assign weights \(w_{i_n}=2^{-n}\), and put \(w_i=1\) elsewhere. The trace \(\tau(f)=\sum_iw_if_i\), interpreted as the supremum of finite sums, is faithful, normal and semifinite. It admits no faithful normal state: any normal functional on this diagonal algebra has at most countable support. Define \(g(i_n)=2^n\) and \(g(i)=0\) elsewhere. The corresponding diagonal operator is unbounded but densely defined and closed; for \(R\geq1\),

\[
 \tau(1_{(R,\infty)}(|g|))
   =\sum_{2^n>R}2^{-n}\longrightarrow0.
\]

The construction therefore lies within the full, possibly non-sigma-finite setting of the unit. The small complements used for this one operator do not make the entire algebra sigma-finite.

## Problems with complete solutions

**Problem 1: the completed vector space can enlarge the Hilbert space.** Use the diffuse representation in MT-14. Show that \(\xi_n(t)=\min(n,t^{-1/2})\) is Cauchy for the vector measure topology, and that its limit in \(\widehat H\) does not belong to \(H\).

**Solution.** For \(m,n\geq N\), the functions agree on \([N^{-2},1)\), so multiplying their difference by the projection of this set gives zero; the discarded trace is \(N^{-2}\). Hence they are Cauchy. If their completion limit were some \(\eta\in L^2(0,1)\), vector measure convergence would force \(\xi_n\to\eta\) in ordinary scalar measure. Indeed, if a projection \(p=1_E\) satisfies \(\|p(\xi_n-\eta)\|_2<r\) and \(|E^c|<d\), then Chebyshev's inequality gives

\[
 |\{|\xi_n-\eta|>s\}|\leq d+r^2/s^2.
\]

Let \(r,d\to0\). On the other hand \(\xi_n\to t^{-1/2}\) in measure, since they agree with that function outside a set of measure \(n^{-2}\). Uniqueness of scalar limits in measure follows from the triangle inequality for the exceptional sets, so \(\eta=t^{-1/2}\) almost everywhere. Its squared integral is infinite, a contradiction.

**Problem 2: two finite cutoffs need not commute.** In \(M_2(\mathbb C)\) with the unnormalized trace, let \(e\) project onto \((1,0)\), and let \(f\) project onto \((1,1)\). Compute \(e\wedge f\), \(e\vee f\), and the initial and final projections of \((1-e)f\). Explain how this checks the noncommuting step of MT-02.

**Solution.** The two lines meet only at zero and span \(\mathbb C^2\), so \(e\wedge f=0\) and \(e\vee f=1\). The map \((1-e)f\) has kernel \(f^\perp H\) and range \(e^\perp H\). Its polar partial isometry therefore has initial projection \(f\) and final projection \(1-e\). This gives \(e\vee f-e\sim f\) in this case and \(\tau(e\vee f)=2=\tau(e)+\tau(f)\), without requiring \(ef=fe\).

**Problem 3: one finite tail is enough, but finite projections alone are not.** For a closed affiliated \(T\), suppose \(\tau(1_{(7,\infty)}(|T|))<\infty\). Prove measurability. Contrast this with merely having increasing finite-trace projections \(e_n\uparrow1\) such that \(Te_n\) is bounded.

**Solution.** The finite-tail argument in MT-11 applies with \(R_0=7\): inside that finite-trace projection, normality makes the traces of the decreasing high tails tend to zero. Hence \(T\) is measurable. For the contrast use \(De_n=ne_n\) on \(\ell^2(\mathbb N)\) with the canonical trace, and let \(p_N\) project onto the first \(N\) basis vectors. Each \(p_N\) has finite trace and \(Dp_N\) is bounded, but \(\tau(1-p_N)=\infty\). Every high spectral tail of \(D\) also has infinite trace, so \(D\) is not measurable. The increasing-domain theorem needs small trace of the complements, not finite trace of the retained projections.

**Problem 4: recover an operator from compatible pieces.** In the uncountable diagonal model of MT-14, put \(p_N=1-1_{\{i_n:n>N\}}\), and let \(c_N\) be multiplication by the bounded function equal to \(2^n\) at \(i_n\) for \(n\leq N\) and zero elsewhere. Verify the compatibility in MT-10 and identify the closed operator obtained there, including its domain.

**Solution.** The projections increase and \(\tau(1-p_N)=\sum_{n>N}2^{-n}=2^{-N}\to0\). Also \(c_Np_N=c_N\), and \(c_Mp_N=c_N\) for \(M\geq N\). Thus the theorem applies even though \(\|c_N\|=2^N\). Its operator is multiplication by the function \(g\) in MT-14 on

\[
 D(T)=\left\{\xi\in\ell^2(I):\sum_{n\geq1}4^n|\xi_{i_n}|^2<\infty\right\},
 \quad (T\xi)_{i_n}=2^n\xi_{i_n},\quad (T\xi)_i=0\ (i\notin\{i_n\}).
\]

This multiplication operator is closed by coordinate convergence. The projections \(p_N\) converge in its graph norm on the displayed domain, since the omitted squared image norms are tails of a convergent nonnegative series. Therefore it is precisely the closure of the compatible operator on \(\bigcup_Np_NH\), not merely an extension of it.

## What has been constructed and what follows

Projection estimates and graph uniqueness were proved in MT-02 and MT-07. MT-03–06 construct the measure completions of the algebra and its representation space, with uniform continuity on bounded-in-measure sets. MT-08–10 identify the completion with closed affiliated operators, prove all domain-sensitive algebra operations, and treat increasing trace-cofinite domains. MT-11 gives both forms of the spectral-tail criterion. MT-12 supplies positivity, square roots and polar decomposition. MT-13 begins integration and proves the bounded trace-ideal identities and their refined Cauchy–Schwarz estimate.

The next integration unit must prove the trace inequalities on measurable limits, construct the full integrable ideal and the noncommutative \(L^p\) norms, and establish completeness, duality and interpolation at their exact parameter ranges. Measurable-operator constructions for nontracial weights use additional machinery. None of those later results, nor the complete assigned B8 source inventory, is declared closed by this unit.
