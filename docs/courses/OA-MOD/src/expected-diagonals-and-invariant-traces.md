# Expected diagonals and invariant traces

*Original exposition by the OA-MOD course project; CC0-1.0.*

A trace on an algebra need not remain semifinite when restricted to a subalgebra. For a maximal abelian subalgebra admitting a normal conditional expectation, it does. More precisely, the expectation preserves every faithful normal semifinite trace, and the expectation is unique. We prove this without a countability hypothesis. For a countable measured relation, the result identifies every faithful normal semifinite trace with an equivalent invariant measure. It also determines the sign of the density that removes the modular action.

## 1. Objects and exact proof inputs

Let \(M\) be a von Neumann algebra on an arbitrary Hilbert space. A unital von Neumann subalgebra \(A\subseteq M\) is **maximal abelian** when

\[
 A'\cap M=A.
 \tag{EDT.1}
\]

A **normal conditional expectation** \(E:M\to A\) means a positive complex-linear map with \(E(1)=1\), \(E|_A=\operatorname{id}_A\), the bimodule property

\[
 E(aTb)=aE(T)b\qquad(a,b\in A,\ T\in M),
 \tag{EDT.2}
\]

and preservation of bounded increasing positive suprema. Faithfulness of \(E\) is not assumed.

A **faithful normal semifinite trace** \(\tau:M_+\to[0,\infty]\) is additive and nonnegatively homogeneous, faithful, normal on arbitrary bounded increasing positive nets, semifinite in the finite-definition-algebra sense, and satisfies

\[
 \tau(T^*T)=\tau(TT^*)\qquad(T\in M).
 \tag{EDT.3}
\]

All extended-value equalities below avoid subtraction of infinities.

The needed earlier proofs are these:

- CP06 identifies \(M\) isometrically with its predual's dual. AB04–AB05 prove compact products, dual-ball compactness and the convergent-subnet criterion, at arbitrary cardinality.
- NP02 and NP04 identify order normality with ultraweak continuity for bounded positive functionals and positive maps. This applies both to \(E\) and to finite trace corners.
- TB01–TB02 prove the finite trace linear extension and the trace-specific equivalence between semifiniteness and order density. SK08 supplies spectral projections in the algebra and finite step approximation of bounded self-adjoint elements.
- RWT01–RWT03 and RWT06 prove the counting-measure conventions, the faithful normal semifinite relation weight, equivalent-measure transport and its normalized relative cocycle.
- VR01–VR02 prove that a faithful normal semifinite weight is a trace exactly when its modular group is trivial, and that existence of such a trace is equivalent to implementation of a modular flow by a strongly continuous unitary **group** in the algebra.

For the relation application we also use the full earlier programme proofs of the positive-measure Radon–Nikodym theorem, Theorem 0.1, partial orbit operators and the maximal abelian diagonal, Lemma 3.1 and Section 4, and the normal diagonal expectation, Theorem 1.1. Their probability-space representation transfers to an arbitrary nonzero sigma-finite base through the source-coordinate unitary in RWT03. None of these imports is replaced by a source citation.

## 2. Pinching determines the expectation

Let \(\mathcal P(A)\) be the directed set of finite partitions of \(1\) into orthogonal projections belonging to \(A\). Order it by refinement. Two partitions have a common refinement formed by their nonzero pairwise products. For \(\Pi\in\mathcal P(A)\), put

\[
 Q_\Pi(T)=\sum_{p\in\Pi}pTp.
 \tag{EDT.4}
\]


**Theorem.** If \(A\) is maximal abelian and \(E:M\to A\) is a normal conditional expectation, then

\[
 Q_\Pi(T)\longrightarrow E(T)\quad\hbox{ultraweakly}
 \qquad(T\in M).
 \tag{EDT.5}
\]

Consequently there is at most one normal conditional expectation onto \(A\).

**Proof.** Orthogonality gives, for every vector \(\xi\),

\[
 \|Q_\Pi(T)\xi\|^2
   =\sum_{p\in\Pi}\|pTp\xi\|^2
   \leq\|T\|^2\sum_{p\in\Pi}\|p\xi\|^2
   =\|T\|^2\|\xi\|^2.
 \tag{EDT.6}
\]

Thus the net lies in the ultraweakly compact ball of radius \(\|T\|\), by CP06 and AB05.

Fix a projection \(q\in A\). Once \(\Pi\) refines \(\{q,1-q\}\), its pinching commutes with \(q\). Every ultraweak cluster point therefore commutes with every projection of \(A\): multiplication by a fixed bounded operator is ultraweakly continuous, as is immediate from the vector-series tests for that topology. Finite spectral step approximation then makes it commute with every self-adjoint element of \(A\), and hence with \(A\). Maximal abelianness puts the cluster point in \(A\).

On the other hand, bimodularity and abelianness give

\[
 E(Q_\Pi(T))=\sum_{p\in\Pi}pE(T)p=E(T).
 \tag{EDT.7}
\]

Ultraweak continuity of \(E\), from NP04, shows that a cluster point \(a\in A\) satisfies \(a=E(a)=E(T)\).

This unique cluster point is the limit of the whole net. Indeed, if a neighborhood of \(E(T)\) failed to contain a tail, a subnet could be chosen in its closed complement; compactness would give a cluster point there, a contradiction. Applying (EDT.5) to a second normal expectation gives the same limit for every \(T\), proving uniqueness. \(\square\)

No countable family of projections is chosen here. The proof uses the entire directed family of finite partitions. It proves uniqueness only among **normal** expectations.

## 3. Finite trace projections and lower semicontinuity

**Lemma.** For a faithful normal semifinite trace on an arbitrary \(M\), there is a net of finite-trace projections \(e_F\uparrow1\). For every \(x\in M_+\),

\[
 \tau(x)=\sup_F\tau(e_Fxe_F).
 \tag{EDT.8}
\]

In particular, \(\tau\) is lower semicontinuous on \(M_+\) in the ultraweak topology.

**Proof.** Every nonzero projection \(r\) contains a nonzero finite-trace projection. To see this, semifiniteness and ultraweak density of the finite positive span give a finite positive \(b\) with \(rbr\ne0\). Otherwise compression by \(r\) would annihilate that dense span and then all of \(M\), including \(r\). The trace identity gives

\[
 \tau(rbr)=\tau(b^{1/2}rb^{1/2})\leq\tau(b)<\infty.
 \tag{EDT.9}
\]

For some \(\varepsilon>0\), the spectral projection
\(f=1_{[\varepsilon,\infty)}(rbr)\) is nonzero. It lies below \(r\), and
\(\varepsilon f\leq rbr\), so it has finite trace.

Choose a maximal orthogonal family \((p_i)_{i\in I}\) of nonzero finite-trace projections. Zorn's principle supplies it, and the preceding argument makes its sum \(1\). For finite \(F\subseteq I\), set \(e_F=\sum_{i\in F}p_i\). These projections increase strongly to \(1\) and have finite trace. The index set \(I\) need not be countable.

For \(x\geq0\), the elements \(x^{1/2}e_Fx^{1/2}\) increase to \(x\). Normality and (EDT.3) prove

\[
 \tau(x)=\sup_F\tau(x^{1/2}e_Fx^{1/2})
        =\sup_F\tau(e_Fxe_F).
 \tag{EDT.10}
\]

The functional \(x\mapsto\tau(e_Fxe_F)\) is bounded and positive, with norm \(\tau(e_F)\), by TB01. It is order normal because compression preserves bounded increasing positive suprema and \(\tau\) is normal. NP02 makes it ultraweakly continuous. Formula (EDT.10) expresses \(\tau\) as the supremum of these continuous functions on \(M_+\). Its finite sublevel sets are therefore intersections of closed sets, proving lower semicontinuity. \(\square\)

More generally, for any increasing net of projections \(q_j\uparrow1\), whether or not trace finite,

\[
 \tau(q_jxq_j)=\tau(x^{1/2}q_jx^{1/2})\uparrow\tau(x).
 \tag{EDT.11}
\]

This is a statement about the trace values. The operators \(q_jxq_j\) themselves need not increase.

## 4. Every semifinite trace is preserved

**Theorem.** Let \(A\subseteq M\) be maximal abelian and let \(E:M\to A\) be a normal conditional expectation. For every faithful normal semifinite trace \(\tau\) on \(M\), its restriction to \(A\) is faithful, normal and semifinite, and

\[
 \tau(E(x))=\tau(x)\qquad(x\in M_+).
 \tag{EDT.12}
\]

Thus, when \(M\) admits such a trace, the expectation is faithful even if this was not assumed.

**Proof.** For a finite partition \(\Pi\), trace additivity and (EDT.3) give

\[
 \begin{aligned}
 \tau(Q_\Pi(x))
 &=\sum_{p\in\Pi}\tau(pxp)
  =\sum_{p\in\Pi}\tau(x^{1/2}px^{1/2})\\
 &=\tau(x).
 \end{aligned}
 \tag{EDT.13}
\]

Taking the ultraweak limit from EDT02 and using EDT03 yields

\[
 \tau(E(x))\leq\tau(x).
 \tag{EDT.14}
\]


Take the finite-trace exhaustion \(e_F\uparrow1\) of EDT03. Normality gives \(E(e_F)\uparrow1\). For \(n\geq1\), put

\[
 q_{F,n}=1_{[1/n,1]}(E(e_F))\in A.
 \tag{EDT.15}
\]

Then

\[
 \tau(q_{F,n})\leq n\tau(E(e_F))\leq n\tau(e_F)<\infty.
 \tag{EDT.16}
\]

The join of all these projections is \(1\). In fact a projection orthogonal to them is orthogonal to the support of every \(E(e_F)\), and the increasing supremum of those positive operators is \(1\).

Let \(\mathcal Q_\tau(A)\) be **all** projections of \(A\) with finite trace. It is directed by joins: the projections commute and \(p\vee q\leq p+q\), so \(\tau(p\vee q)<\infty\). By the preceding paragraph,

\[
 q\uparrow1\quad(q\in\mathcal Q_\tau(A)).
 \tag{EDT.17}
\]

For \(a\in A_+\), the positive elements \(qa\) increase to \(a\) and have trace at most \(\|a\|\tau(q)\). This proves semifiniteness of \(\tau|_A\), including its finite-definition-algebra version. Faithfulness and normality restrict immediately.

It remains to upgrade (EDT.14) to equality. Fix \(q\in\mathcal Q_\tau(A)\). Because \(q\) commutes with every member of \(\Pi\),

\[
 qQ_\Pi(x)q=Q_\Pi(qxq),\qquad
 \tau(qQ_\Pi(x)q)=\tau(qxq).
 \tag{EDT.18}
\]

On \(qMq\), the trace is a bounded normal functional. The ultraweak limit of (EDT.18) therefore gives

\[
 \tau(qE(x)q)=\tau(qxq).
 \tag{EDT.19}
\]

Pass through the net (EDT.17) and use (EDT.11) on both sides. This proves (EDT.12), including when the common value is infinite. Finally \(E(x)=0\), \(x\geq0\), implies \(\tau(x)=0\) and hence \(x=0\). \(\square\)

The theorem does not assert that an arbitrary restriction of a semifinite weight is semifinite. It uses the trace identity, maximal abelianness and normality of the expectation at separate steps.

## 5. All traces of a measured relation

Let a countable group \(\Gamma\) act nonsingularly by Borel bijections on a nonzero standard Borel sigma-finite measure space \((X,\mu)\). No freeness or ergodicity is assumed. Let \(R\) be its orbit relation, with arrows \((y,x)\) from source \(x\) to range \(y\), and write

\[
 M=\mathcal M(R,\mu),\qquad
 A=\{M_f:f\in L^\infty(X,\mu)\}.
 \tag{EDT.20}
\]

Here \(M_f\) multiplies the range coordinate. Let \(E:M\to A\) be the normal diagonal expectation. The earlier programme proofs named in EDT01 make \(A\) maximal abelian and give the partial orbit operators

\[
 V_\theta^*V_\theta=M_{1_B},\qquad
 V_\theta V_\theta^*=M_{1_{\theta B}}
 \tag{EDT.21}
\]

for a Borel partial orbit bijection \(\theta:B\to\theta B\).

**Theorem.** The assignment

\[
 \eta\longmapsto\tau_\eta,\qquad
 \tau_\eta(T)=\int_X E(T)\,d\eta\quad(T\geq0),
 \tag{EDT.22}
\]

is a bijection from equivalent sigma-finite invariant measures on \(X\) to all faithful normal semifinite traces on \(M\). Invariance may be tested on the presenting group or on all partial orbit bijections.

**Proof from a trace.** Given such a trace \(\tau\), define

\[
 \eta(B)=\tau(M_{1_B}).
 \tag{EDT.23}
\]

Normality and finite additivity make this countably additive on disjoint Borel sets, with arbitrary infinite values allowed. A \(\mu\)-null set has zero multiplication projection. Conversely, \(\eta(B)=0\) forces that projection to vanish by faithfulness; its restriction to the diagonal subspace detects whether \(\mu(B)>0\). Thus \(\eta\) and \(\mu\) have the same null sets. Equation (EDT.21) and the trace identity show \(\eta(\theta B)=\eta(B)\).

We must still prove sigma-finiteness; it is not a consequence of equivalence of null sets alone. By EDT04, the finite-trace projections of \(A\) increase to \(1\). Choose an equivalent probability \(\rho\). Explicitly, disjointify a countable finite-\(\mu\) cover into \(X_k\), give each nonnull \(X_k\) the positive constant density \(2^{-k}/(1+\mu(X_k))\), and normalize its finite, nonzero integral. Integration against \(\rho\) is a faithful normal state on \(A\). Here is normality for arbitrary bounded increasing positive nets \((a_j)\). Put \(s=\sup_j\int a_j\,d\rho\), choose an increasing sequence of net members whose integrals tend to \(s\), and let \(b\) be its pointwise supremum. Monotone convergence gives \(\int b\,d\rho=s\). For each fixed \(j\), directed upper bounds imply that the maximum of \(a_j\) and each chosen member has integral at most \(s\). Passing through the sequence gives \(\int\max(a_j,b)\,d\rho\leq s\). Thus \((a_j-b)_+\) has integral zero, so \(a_j\leq b\) as a measurable class. Every upper bound for the net also bounds \(b\). Consequently \(b\) is the order supremum and has integral \(s\). This proves normality without replacing the order definition by a sequence assumption.

It follows that there are increasing \(q_n\in\mathcal Q_\tau(A)\) with

\[
 \rho(q_n)>1-2^{-n}.
 \tag{EDT.24}
\]

Take finite joins when choosing successive members. Their supremum has \(\rho\)-value \(1\), hence is \(1\). Represent them by increasing Borel sets \(B_n\), changing representatives on null sets if necessary. Each \(\eta(B_n)<\infty\), and their union is conull for both measures. The null complement may be added to the first set. Thus \(\eta\) is sigma-finite.

For positive simple functions, (EDT.23) gives \(\tau(M_f)=\int f\,d\eta\); increasing simple approximation and normality give the same equality for all bounded \(f\geq0\). EDT04 now proves

\[
 \tau(T)=\tau(E(T))=\int_XE(T)\,d\eta
 \qquad(T\in M_+).
 \tag{EDT.25}
\]

This identifies the whole trace, not only its diagonal restriction.

**Proof from a measure.** Given an equivalent sigma-finite invariant \(\eta\), the Radon–Nikodym proof in EDT01 supplies \(d\eta=q\,d\mu\), where \(0<q<\infty\) almost everywhere. RWT02–RWT03 show that (EDT.22) is a faithful normal semifinite weight on the same algebra, even when \(q\) is unbounded or \(\eta(X)=\infty\). Invariance makes its range and source counting measures equal: partition the relation into disjoint pieces of group graphs and use measure invariance on each piece. Its modulus is therefore \(1\). The modular formula in RWT02 makes its modular group trivial, so VR01 proves it is a trace.

Group invariance implies partial-map invariance by partitioning the domain into the Borel sets on which \(\theta\) equals a chosen group element; their images are disjoint. The reverse implication includes the group maps themselves. Finally, restriction of (EDT.22) to indicators recovers \(\eta\), proving injectivity and the stated inverse construction. \(\square\)

## 6. The modular coboundary criterion

Let \(\nu_s,\nu_r\) be the source and range counting measures of RWT01, and set

\[
 \delta(y,x)=\frac{d\nu_r}{d\nu_s}(y,x),\qquad
 \varphi_\mu(T)=\int_XE(T)\,d\mu.
 \tag{EDT.26}
\]

Use the common invariant conull set on which the modulus is a positive finite cocycle.

**Theorem.** The following conditions are equivalent:

1. \(M\) admits a faithful normal semifinite trace.
2. There is an equivalent sigma-finite invariant measure \(\eta\) on \(X\).
3. There is a Borel \(h\), positive and finite almost everywhere, such that

   \[
    \delta(y,x)=\frac{h(y)}{h(x)}
    \tag{EDT.27}
   \]

   on the relation after removing an invariant null set.
4. There is a strongly continuous unitary group \((u_t)_{t\in\mathbb R}\) in \(M\) with

   \[
    \sigma_t^{\varphi_\mu}=\operatorname{Ad}(u_t).
    \tag{EDT.28}
   \]


When (3) holds, the measure in (2) and one implementing group in (4) are

\[
 d\eta=h^{-1}\,d\mu,\qquad u_t=M_{h^{it}}.
 \tag{EDT.29}
\]


**Proof.** EDT05 proves \(1\Longleftrightarrow2\). If \(d\eta=q\,d\mu\), the change-of-measure formula RWT03 is

\[
 \delta_\eta(y,x)=\frac{q(y)}{q(x)}\delta(y,x).
 \tag{EDT.30}
\]

An invariant measure has \(\delta_\eta=1\). Taking \(h=q^{-1}\) gives (3). Conversely, (EDT.27) makes (EDT.30) equal to \(1\) for \(q=h^{-1}\). For each \(g\in\Gamma\), the partial-map derivative in RWT01 then gives
\(\eta(gB)=\eta(B)\) for every Borel \(B\), including infinite values. The measure is equivalent and sigma-finite: if \(X_n\uparrow X\) have finite \(\mu\)-measure, the sets \(X_n\cap\{h^{-1}\leq k\}\) form a countable finite-\(\eta\) cover modulo a null set. Equality on the countably many group graphs becomes simultaneous after null saturation, giving exactly the conull formulation in (3). This proves \(2\Longleftrightarrow3\).

Under (3), the multiplication operators \(M_{h^{it}}\) form a unitary group. They are strongly continuous because pointwise continuity and the bound
\(\lvert h^{it}-h^{is}\rvert\leq2\) permit dominated convergence on every vector in \(L^2(R,\nu_s)\). Conjugation multiplies a kernel at \((y,x)\) by \(h(y)^{it}h(x)^{-it}=\delta(y,x)^{it}\). RWT02 identifies this with the modular action on the generating kernel algebra. Normality extends the equality to all of \(M\), proving (4).

Finally VR02, at the arbitrary-algebra and faithful normal semifinite weight scope stated in EDT01, proves \(4\Longrightarrow1\). Thus every implication has a written programme proof. \(\square\)

The normalized cocycle records the reciprocal sign:

\[
 [D\tau_\eta:D\varphi_\mu]_t=M_{h^{-it}},
 \qquad
 \sigma_t^{\varphi_\mu}=\operatorname{Ad}(M_{h^{it}}).
 \tag{EDT.31}
\]

Indeed, apply RWT06 with numerator density \(h^{-1}\) and denominator density \(1\). An arbitrary choice of unitary implementing each individual automorphism is insufficient for condition (4): the hypothesis is a strongly continuous group, and VR02 uses its affiliated positive generator.

This proves the semifiniteness criterion of Takesaki III, Chapter XIII, Proposition 2.9, with the construction of the invariant measure and its sigma-finiteness explicit. The stronger classification in EDT05 determines all traces.

## 7. Central density and scalar ambiguity

Assume there is one equivalent sigma-finite invariant measure \(\eta_0\).

**Proposition.** All equivalent sigma-finite invariant measures are precisely

\[
 d\eta=z\,d\eta_0,\qquad
 0<z<\infty\ \hbox{almost everywhere},\qquad
 z(gx)=z(x)\ \hbox{almost everywhere for every }g\in\Gamma.
 \tag{EDT.32}
\]

Their traces satisfy, for \(T\geq0\),

\[
 \tau_\eta(T)
 =\lim_{n\to\infty}
   \tau_{\eta_0}\!\left(M_{\min(z,n)}^{1/2}
               T M_{\min(z,n)}^{1/2}\right).
 \tag{EDT.33}
\]

The function \(z\) represents a positive injective operator affiliated with \(Z(M)\). If the relation is ergodic, \(z\) is a positive scalar. In that case all faithful normal semifinite traces are positive scalar multiples of one another.

**Proof.** The Radon–Nikodym theorem gives the positive finite density of any equivalent sigma-finite \(\eta\). Invariance of both measures, applied to indicators and change of variables by a fixed \(g\), says that \(z\) and \(z\circ g\) give the same measure relative to \(\eta_0\). Uniqueness of the density proves (EDT.32). Conversely, an invariant \(z\) gives an invariant measure by that same change of variables. It is sigma-finite by intersecting a finite-\(\eta_0\) cover with \(\{z\leq n\}\).

The center formula in the relation-diagonal proof from EDT01 puts each bounded multiplication operator \(M_{\min(z,n)}\) in \(Z(M)\). Bimodularity of \(E\) gives

\[
 E(M_{\min(z,n)}^{1/2}T M_{\min(z,n)}^{1/2})
   =\min(z,n)E(T).
 \tag{EDT.34}
\]

Monotone convergence of these scalar integrals proves (EDT.33), including infinite values.

For clarity, the unbounded multiplication operator \(M_z\) is taken on its maximal square-integrability domain in the range coordinate. The cutoffs \(\{z\leq n\}\) exhaust the space and give dense domain. It is symmetric and positive. If \(M_z^*\xi=\eta\), testing vectors in each cutoff gives \(1_{\{z\leq n\}}\eta=z1_{\{z\leq n\}}\xi\); hence \(\eta=z\xi\) belongs to the Hilbert space and \(\xi\) is in the maximal multiplication domain. Thus the adjoint is \(M_z\) itself. Its kernel is zero because \(z>0\) almost everywhere. All its spectral projections \(M_{1_{\{z\in B\}}}\) are central by invariance and the same center formula. The affiliation criterion SK08 proves the assertion.

If the action is ergodic, all rational level sets of the bounded invariant function \(z/(1+z)\) are null or conull. Their nested order determines a single scalar value almost everywhere: the cut between conull lower levels and null upper levels traps the function between arbitrary rational bounds at that value. Positivity and finiteness of \(z\) make its resulting scalar strictly positive and finite. The trace assertion follows from (EDT.22). \(\square\)

If \(h_1,h_2\) both satisfy (EDT.27), then \(h_2/h_1\) is invariant: cancel the two endpoint ratios on every arrow. Conversely, multiplying one solution by any positive finite invariant function gives another. The corresponding invariant measures have ratio

\[
 \frac{d(h_2^{-1}\mu)}{d(h_1^{-1}\mu)}
   =\frac{h_1}{h_2}.
 \tag{EDT.35}
\]

Thus even in a factor the modular action alone does not choose a trace normalization. Replacing \(h\) by \(ch\), \(c>0\), leaves its adjoint action unchanged, scales the trace by \(c^{-1}\), and multiplies the normalized cocycle in (EDT.31) by \(c^{-it}\).

## 8. Tests of the hypotheses and conventions

**A two-point relation fixes the density sign.** Take the complete relation on \(\{1,2\}\) with masses \(\mu(\{1\})=2\), \(\mu(\{2\})=5\). Then

\[
 M=M_2(\mathbb C),\quad E(T)=\operatorname{diag}(T_{11},T_{22}),
 \quad \varphi_\mu(T)=2T_{11}+5T_{22}.
 \tag{EDT.36}
\]

Source counting gives \(\delta(i,j)=\mu(\{i\})/\mu(\{j\})\). The choice \(h=(2,5)\) makes \(h^{-1}\mu\) counting measure, and \(\tau_\eta=\operatorname{Tr}\). Consequently

\[
 \sigma_t^{\varphi_\mu}(E_{ij})
   =(h_i/h_j)^{it}E_{ij},\qquad
 [D\operatorname{Tr}:D\varphi_\mu]_t
   =\operatorname{diag}(2^{-it},5^{-it}).
 \tag{EDT.37}
\]

Using \(h\mu\) instead would give masses \(4,25\), which are not invariant under interchange of the two points.

**Maximal abelianness is essential.** In \(M_2(\mathbb C)\), take \(A=\mathbb C1\), which is abelian but not maximal abelian, and define

\[
 E(T)=\left(\tfrac34 T_{11}+\tfrac14 T_{22}\right)1.
 \tag{EDT.38}
\]

This is a normal faithful positive unital \(A\)-bimodule projection. Positivity and faithfulness follow from the positive diagonal coefficients: a positive matrix with both diagonal entries zero is zero, since its positive square root kills both basis vectors. For the normalized trace \(\tau=\tfrac12\operatorname{Tr}\),

\[
 \tau(E(E_{11}))=\tfrac34\ne\tfrac12=\tau(E_{11}).
 \tag{EDT.39}
\]

Thus the range being abelian does not suffice for EDT04.

**Compression is not monotone.** Let

\[
 x=\begin{pmatrix}1&1\\1&1\end{pmatrix}\geq0,\qquad
 q=\begin{pmatrix}1&0\\0&0\end{pmatrix}\leq1.
 \tag{EDT.40}
\]

The determinant of \(x-qxq=\begin{pmatrix}0&1\\1&1\end{pmatrix}\) is \(-1\); alternatively its quadratic form at \((1,-1)\) is \(-1\). Hence \(qxq\not\leq x\). The trace limit in EDT03 correctly uses \(x^{1/2}qx^{1/2}\), not operator monotonicity of compression.

**The general theorem requires nets.** For an arbitrary set \(I\), put \(M=B(\ell^2(I))\), with diagonal \(A=\ell^\infty(I)\). Define

\[
 E(T)_i=\langle Te_i,e_i\rangle,\qquad
 \tau(T)=\sup_{F\subseteq I,\ F\ {\rm finite}}
                \sum_{i\in F}\langle Te_i,e_i\rangle
 \quad(T\geq0).
 \tag{EDT.41}
\]

The diagonal is maximal abelian: commuting with every rank-one coordinate projection forces all off-diagonal entries to vanish. The map \(E\) is a normal conditional expectation by coordinatewise positivity, bimodularity and monotone convergence of vector coefficients. The weight \(\tau\) is faithful and normal because its finite sums of vector functionals are so and the two increasing suprema commute. For a bounded \(S\), Parseval gives

\[
 \tau(S^*S)=\sum_{i,j\in I}|\langle Se_i,e_j\rangle|^2
          =\tau(SS^*).
 \tag{EDT.42}
\]

These sums mean suprema over finite sets; exchanging their order is valid for nonnegative terms. Finite-coordinate projections \(p_F\uparrow1\), and
\(x^{1/2}p_Fx^{1/2}\) are finite-trace positive elements increasing to \(x\), so \(\tau\) is semifinite. Formula (EDT.41) gives \(\tau\circ E=\tau\) directly.

If \(I\) is uncountable, finite-trace diagonal projections have finite support. No sequence of them can exhaust \(1\), although their full directed net does. Thus EDT04 does not assert a sigma-finite restriction. The countability conclusion for relation measures in EDT05 uses their equivalent probability, an additional hypothesis absent here.

The construction source for the measured-relation criterion is Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Proposition 2.9, printed page 22. The arguments used in this lesson are proved above or at the precise earlier programme locators in EDT01. The general expected-diagonal theorem and trace classification are stated at the full scopes proved here. This lesson does not establish the later ratio-set identification with the all-weight \(S\)-invariant or a classification of type III factors.

