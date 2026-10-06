# Corner weights tested on all positive energies

**Original proof and import proposal.**

A corner weight is evaluated on a compressed positive energy. When the energy is unbounded, compression is an operation on forms, and it can create directions of infinite energy. This bridge specifies that operation before proving the support and completion identities. It applies to arbitrary von Neumann algebras, including the zero algebra, with no countability assumption.

## Inputs and conventions

Let \(M\subseteq B(\mathcal H)\) be a faithful concrete unital von Neumann algebra. A weight takes values in \([0,\infty]\), with \(0\cdot\infty=0\). Scalar sums over an arbitrary set mean suprema of finite subsums. A projection corner \(pMp\) has identity \(p\). On the zero algebra the unique zero weight is normal, semifinite and faithful.

The existing providers used here are:

- **Normality produces a largest null projection through The faithful semifinite support corner:** null projections, support reduction, and the faithful normal semifinite restriction of a normal semifinite weight to its support corner;
- **Finite positive cutoffs characterize semifiniteness:** semifiniteness is equivalent to finite positive contraction cutoffs increasing to the identity;
- **The full characterization through Consequences for GNS maps and sums of weights:** a normal weight is the pointwise supremum of its dominated positive normal functionals, and arbitrary sums of normal weights are normal;
- **Corners have exactly their inherited predual:** the inherited corner predual and its positive isometric lift by compression;
- **Positive observations can be implemented by vector sums:** every positive normal functional in the given faithful concrete representation is a countable sum of vector functionals with summable squared vector norms;
- **Representation with the exact square-root domain through Nondense forms, lower semicontinuity, and symmetry and Bounded Borel functions and the spectral measure through Transport, reduction, and membership in an algebra:** representation of closed positive forms, including a domain dense only in a closed subspace, and the exact spectral calculus and commutant symmetry test;
- **Every von Neumann algebra has such a weight:** every von Neumann algebra, and hence every corner, has a faithful normal semifinite weight;
- **Recognize exactly the fixed observations and Justify spectral restriction before using it:** centralizer unitary invariance on the entire positive cone, the sign-unitary criterion for a projection to belong to the centralizer, and faithful normal semifinite restriction to a centralizer corner.

The new arguments below supply the extended-positive pairing and the general corner assembly clauses. They do not use a crossed product, an action, or a scalar cocycle reconstruction.

## Infinite energies have bounded spectral tests

Define \(\widehat M_+\) to consist of additive, nonnegatively homogeneous maps

\[
H:M_*^+\longrightarrow[0,\infty],\qquad H(0)=0,
\]

which are lower semicontinuous for the norm topology of the positive predual cone. Order is pointwise. A bounded positive \(a\in M\) is identified with \(\omega\mapsto\omega(a)\).

**Theorem.** For every \(H\in\widehat M_+\) there are a projection \(e\in M\) and a positive self-adjoint operator \(A\) on \(e\mathcal H\), affiliated with \(eMe\). For each integer \(n\geq1\), define the bounded positive operator \(H_n\in M_+\) by

\[
\begin{aligned}
H_n&=\min(A,n)e\\
   &\quad+n(1-e).
\end{aligned}
\tag{CW.1}
\]

These bounded positive operators increase and, for every \(\omega\in M_*^+\), satisfy

\[
H(\omega)=\sup_n\omega(H_n).
\tag{CW.2}
\]

Here the first term in (CW.1) is extended by zero off \(e\mathcal H\). The pair \((e,A)\) is unique. In particular, the cone includes an infinite part on \((1-e)\mathcal H\); it is not restricted to densely defined operators on \(\mathcal H\).

**Proof.** Write \(\omega_\xi(x)=\langle x\xi,\xi\rangle\) and set \(q[\xi]=H(\omega_\xi)\). Additivity makes \(H\) order preserving. The inequality
\(\omega_{\xi+\eta}\leq2\omega_\xi+2\omega_\eta\)
shows that \(D=\{\xi:q[\xi]<\infty\}\) is linear. On this domain, the vector-functional parallelogram identity gives the finite-valued parallelogram identity for \(q\), and scalar homogeneity gives \(q[z\xi]=|z|^2q[\xi]\). Polarization therefore gives a nonnegative sesquilinear form on \(D\). No subtraction of infinite values is used.

The map \(\xi\mapsto\omega_\xi\) is norm continuous, since

\[
\|\omega_\xi-\omega_\eta\|\leq(\|\xi\|+\|\eta\|)\|\xi-\eta\|.
\]

Thus the extended diagonal \(q\) is norm lower semicontinuous. It is closed as a form: if \((\xi_j)\) is Cauchy for \((\|\xi\|^2+q[\xi])^{1/2}\), let \(\xi\) be its Hilbert-space limit. For each fixed \(j\), lower semicontinuity yields

\[
q[\xi_j-\xi]\leq\liminf_k q[\xi_j-\xi_k].
\]

The right side is finite for large \(j\) and tends to zero. Hence \(\xi_j-\xi\in D\) for such a \(j\), which implies \(\xi\in D\), and convergence holds in the form norm.

Put \(K=\overline D\). QF-04 gives the unique positive self-adjoint \(A\) on \(K\) with \(D(A^{1/2})=D\) and \(q[\xi]=\|A^{1/2}\xi\|^2\). For every unitary \(u'\in M'\), one has \(\omega_{u'\xi}=\omega_\xi\), so \(u'D=D\) and \(q[u'\xi]=q[\xi]\). It follows that \(K\) reduces every such unitary and its projection \(e\) belongs to \(M\). Apply the symmetry statement of QF-04 on \(K\). The operator \((1+A)^{-1}\), extended by zero off \(K\), commutes with \(M'\), and belongs to \(M\). Its support is \(e\). The spectral calculus in SK identifies the spectral projections of \(A\) as projections in \(eMe\). This proves the stated affiliation.

For every \(\xi\in\mathcal H\), scalar monotone convergence in this spectral calculus gives

\[
q[\xi]=\sup_n\langle H_n\xi,\xi\rangle,
\tag{CW.3}
\]

including infinity both outside \(K\) and at vectors in \(K\setminus D\).

For general \(\omega\in M_*^+\), SC-02 gives \(\omega=\sum_{j\geq1}\omega_{\xi_j}\), with \(\sum_j\|\xi_j\|^2=\omega(1)\). The partial sums converge in predual norm: the positive remainder has norm equal to its value at the identity. Additivity and monotonicity give
\(\sum_{j\leq r}q[\xi_j]\leq H(\omega)\).
Lower semicontinuity at those partial sums gives the reverse inequality after passing to their supremum. Consequently

\[
H(\omega)=\sum_jq[\xi_j]
=\sup_n\sum_j\langle H_n\xi_j,\xi_j\rangle
=\sup_n\omega(H_n).
\]

The interchange is between increasing nonnegative scalar sums and requires no finite-value assumption. Finally, \(H\) determines \(q\), then \(D\), \(K\), and its unique representing operator, proving uniqueness. \(\square\)

Conversely, any such affiliated pair defines an element of \(\widehat M_+\) by (CW.2): increasing limits commute with finite nonnegative sums, and a supremum of continuous functions is lower semicontinuous. This proves the equivalence with the spectral description of the full extended positive cone.

## Evaluating a normal weight on every extended positive

For an arbitrary normal weight \(\varphi\), write \(\omega\leq\varphi\) when
\(\omega(x)\leq\varphi(x)\) for every \(x\in M_+\), and set

\[
\begin{aligned}
\mathcal F_\varphi
  &=\{\omega\in M_*^+:\omega\leq\varphi\},\\
\widehat\varphi(H)
  &=\sup_{\omega\in\mathcal F_\varphi}H(\omega).
\end{aligned}
\tag{CW.4}
\]

**Theorem.** This is the unique extension of \(\varphi\) to \(\widehat M_+\) that preserves nonnegative scaling, positive addition, and increasing suprema. For the cutoffs of CW-02,

\[
\widehat\varphi(H)=\sup_n\varphi(H_n).
\tag{CW.5}
\]

For every family \((\varphi_i)_{i\in I}\) of normal weights,

\[
\widehat{\sum_{i\in I}\varphi_i}(H)
=\sum_{i\in I}\widehat\varphi_i(H).
\tag{CW.6}
\]

All these identities include infinite values and empty sums. No semifiniteness assumption is needed in this item.

**Proof.** On bounded positives (CW.4) agrees with \(\varphi\) by NW-11. Equations (CW.2) and (CW.4), followed by interchange of two suprema, give (CW.5).

If \(H_\alpha\uparrow H\) pointwise, then \(H\) is still additive and nonnegatively homogeneous: finite sums of increasing nonnegative nets commute with the supremum on the same directed set. It is lower semicontinuous as a supremum. Formula (CW.4) immediately gives

\[
\widehat\varphi(H)=\sup_\omega\sup_\alpha H_\alpha(\omega)
=\sup_\alpha\widehat\varphi(H_\alpha).
\]

For \(H,K\in\widehat M_+\), their pointwise sum belongs to the cone and \(H_n+K_n\uparrow H+K\) pointwise. The preceding equality, agreement on bounded positives, and finite additivity of \(\varphi\) show

\[
\widehat\varphi(H+K)
=\sup_n[\varphi(H_n)+\varphi(K_n)]
=\widehat\varphi(H)+\widehat\varphi(K).
\]

Positive scaling follows in the same way; scaling by zero gives the zero element even where the original value was infinite. These arguments never require \(\mathcal F_\varphi\) to be upward directed. Uniqueness follows by applying preservation of increasing suprema to (CW.2).

By NW-12, \(\psi=\sum_i\varphi_i\) is a normal weight on \(M\). Now (CW.5) yields

\[
\widehat\psi(H)
=\sup_n\sup_{F\subseteq I\text{ finite}}\sum_{i\in F}\varphi_i(H_n)
=\sup_{F\subseteq I\text{ finite}}\sum_{i\in F}\sup_n\varphi_i(H_n),
\]

which is (CW.6). For each finite \(F\), approximate each of its finitely many target values from below and choose one large enough \(n\); this proves the displayed interchange even when some target values are infinite. \(\square\)

The sum of normal weights in this statement need not be semifinite. A proof of (CW.6) therefore cannot restrict the intermediate sum to faithful normal semifinite weights.

## Compression and the supported pairing

For a projection \(p\in M\), let \(\iota_p:(pMp)_*^+\to M_*^+\) send \(\omega\) to the normal positive functional

\[
\iota_p(\omega)(x)=\omega(pxp).
\]

For \(\omega\in(pMp)_*^+\), define the **extended-positive compression** by

\[
(pHp)(\omega)=H(\iota_p(\omega)).
\tag{CW.7}
\]

The notation in (CW.7) is a definition on the entire extended positive cone.

**Theorem.** Formula (CW.7) defines an element of \(\widehat{pMp}_+\). Suppose a normal weight \(\varphi\) satisfies
\(\varphi(x)=\theta(pxp)\) on \(M_+\), where \(\theta\) is a normal weight on \(pMp\). Then, for every \(H\in\widehat M_+\),

\[
\widehat\varphi(H)=\widehat\theta(pHp).
\tag{CW.8}
\]

In particular, a normal semifinite weight and its faithful support restriction from WS-06 satisfy (CW.8).

**Proof.** The predual map \(\iota_p\) is positive, linear and norm continuous. For a positive \(\omega\), its norm is preserved because \(\iota_p(\omega)(1)=\omega(p)\). Additivity, scaling and lower semicontinuity of \(H\) therefore transfer through this map, proving the first assertion.

If \(\rho\in\mathcal F_\varphi\), then \(\rho(1-p)=0\). The positive-functional Cauchy–Schwarz inequality gives \(\rho(x(1-p))=\rho((1-p)x)=0\) for every \(x\in M\), and thus \(\rho(x)=\rho(pxp)\). Its corner restriction belongs to \(\mathcal F_\theta\). Conversely, every \(\omega\in\mathcal F_\theta\) lifts through \(\iota_p\) to an element of \(\mathcal F_\varphi\). These operations are inverse, so

\[
\widehat\varphi(H)
=\sup_{\omega\in\mathcal F_\theta}H(\iota_p(\omega))
=\widehat\theta(pHp).
\]

This proves the result at all energies, without a GNS finiteness restriction. \(\square\)

On vector functionals of \(p\mathcal H\), the compressed energy equals the restriction of the original extended closed form to that Hilbert subspace. Its finite-energy domain can fail to be dense there. Its bounded approximants \(pH_np\) increase to \(pHp\) in the extended-positive sense, but need not be the spectral truncations of \(pHp\). We do not identify this construction with an unchecked densely defined operator product.

## Lifting a corner weight preserves semifiniteness

**Theorem.** Let \(\theta\) be a normal semifinite weight on \(pMp\). Its lift is the function on \(M_+\) given by

\[
\theta^{\uparrow}(x)=\theta(pxp).
\tag{CW.9}
\]

This lift is a normal semifinite weight on \(M\). If \(\theta\) is faithful on \(pMp\), the support of \(\theta^{\uparrow}\) is exactly \(p\), and its restriction to \(pMp\) is \(\theta\). Hence lift and faithful support restriction are inverse operations between faithful normal semifinite weights on \(pMp\) and normal semifinite weights on \(M\) with support \(p\).

**Proof.** Compression preserves addition, nonnegative scaling and bounded increasing positive suprema, so the weight axioms and normality follow. Choose finite positive contractions \(e_i\uparrow p\) in the corner by WG-008. The positive contractions \(e_i+(1-p)\) increase to \(1\) in \(M\), and

\[
\theta^{\uparrow}(e_i+1-p)=\theta(e_i)<\infty.
\]

WG-008 on \(M\) proves semifiniteness. No centrality of \(p\) is required.

When \(\theta\) is faithful, \(\theta^{\uparrow}(x)=0\) for \(x\geq0\) holds exactly when \(pxp=0\), or equivalently \(x^{1/2}p=0\). This is exactly \(x=(1-p)x(1-p)\). Thus the maximal null projection is \(1-p\); by WS-06 the support is \(p\). The restriction identity is immediate, and WS-06 gives the converse reconstruction. If \(p=0\), the lift is the zero weight and its support is zero; the finite cutoff can be the single operator \(1\). \(\square\)

## Completing two complementary corners

**Theorem.** Let \(q=1-p\), and let \(\theta\) and \(\eta\) be faithful normal semifinite weights on \(pMp\) and \(qMq\), respectively. Define \(\Psi\) on \(M_+\) by

\[
\Psi(x)=\theta(pxp)+\eta(qxq).
\tag{CW.10}
\]

Then \(\Psi\) is faithful, normal and semifinite, its restrictions to the two corners are \(\theta\) and \(\eta\), and \(p,q\in M_\Psi\). Moreover, for every \(H\in\widehat M_+\),

\[
\begin{aligned}
\widehat\Psi(H)
  &=\widehat\theta(pHp)\\
  &\quad+\widehat\eta(qHq).
\end{aligned}
\tag{CW.11}
\]

Such a complementary \(\eta\) always exists by WH-13, including when \(q=0\).

**Proof.** The two lifts are normal weights by CW-05, and NW-12 makes their sum normal. If \(\Psi(x)=0\), faithfulness of the corner weights gives \(pxp=qxq=0\). Thus \(x^{1/2}p=x^{1/2}q=0\), and \(x=0\).

Choose finite positive contraction nets \(e_i\uparrow p\) and \(f_j\uparrow q\) in the respective corners. Ordered by the product directed set, \(e_i+f_j\) are positive contractions increasing to \(1\), and
\(\Psi(e_i+f_j)=\theta(e_i)+\eta(f_j)<\infty\).
WG-008 gives semifiniteness. The restriction assertions use the vanishing of the opposite corner compression and hold also at infinite values.

For \(u=p-q=2p-1\), one has \(puxup=pxp\) and \(quxuq=qxq\). Hence \(\Psi(uxu)=\Psi(x)\) for every positive \(x\). The projection lemma in CZ-09 applies to the now established faithful normal semifinite weight \(\Psi\), giving \(p\in M_\Psi\). Its unital fixed-point algebra also contains \(q\). Finally, apply (CW.6) to the two lifted weights and (CW.8) to each lift to obtain (CW.11). \(\square\)

No trace is assumed, and neither corner weight is assumed bounded at its identity. The earlier special diagonal construction has one bounded corner functional; the present theorem supplies the case of two arbitrary faithful normal semifinite corner weights.

## Compressing a centralizer projection recovers its support

**Theorem.** Suppose \(\Psi\) is a faithful normal semifinite weight on \(M\), \(p\in M_\Psi\) is a projection, and \(q=1-p\). Then the restrictions
\(\theta=\Psi|_{pMp}\) and \(\eta=\Psi|_{qMq}\)
are faithful normal semifinite. The compressed weights on \(M\),

\[
\Psi_p(x)=\Psi(pxp),\qquad \Psi_q(x)=\Psi(qxq),
\]

are normal semifinite with respective supports exactly \(p\) and \(q\). Moreover, for every \(H\in\widehat M_+\),

\[
\begin{aligned}
\Psi&=\Psi_p+\Psi_q,\\
\widehat\Psi(H)
  &=\widehat\theta(pHp)\\
  &\quad+\widehat\eta(qHq).
\end{aligned}
\tag{CW.12}
\]

**Proof.** CZ-09 supplies both faithful normal semifinite corner restrictions, since \(q\) also belongs to the centralizer. CW-05 supplies their lifts and exact supports. The unitary \(u=2p-1\) belongs to \(M_\Psi\); the all-positive identity (CZ.18) in CZ-05 gives \(\Psi(uxu)=\Psi(x)\). Since

\[
pxp+qxq=\tfrac12(x+uxu),
\]

additivity and scaling of \(\Psi\) give the bounded-positive identity in (CW.12), including infinite values. Its extension to \(H\) follows from CW-03 and CW-04. The zero-corner cases are already included in those providers. \(\square\)

Faithfulness of the ambient \(\Psi\) is an explicit condition here. For a nonfaithful ambient weight, compression can have support smaller than \(p\). Also, an arbitrary projection need not admit a semifinite restriction of a specified semifinite weight; the centralizer condition is used by CZ-09.

## Two domain checks with complete solutions

**Problem 1: compression can create an infinite corner.** On \(\ell^2(\mathbb N)\), let \(A\) be diagonal with eigenvalues \(n^2\). Let \(v\) be the normalization of the vector with coordinates \(1/n\), and let \(p\) project onto \(\mathbb Cv\). Compute the extended-positive compression \(pAp\) and its value under the corner state \(\theta(\lambda p)=\lambda\).

**Solution.** The vector \(v\) is square summable, but
\(\sum_n n^2|v_n|^2=\infty\).
Thus no nonzero vector of \(p\mathcal H\) has finite compressed energy. The compressed extended positive is the infinite value on every nonzero positive functional of the one-dimensional corner, and \(\widehat\theta(pAp)=\infty\). The normal bounded lift of \(\theta\) is the vector state \(\omega_v\), whose canonical value on \(A\) is also infinity by (CW.5). An operator product on an assumed dense corner domain would miss this example.

**Problem 2: faithfulness determines the support assertion.** In \(M_2(\mathbb C)\), put \(\Psi(x)=x_{11}\) and take \(p=1\). Determine the support of \(x\mapsto\Psi(pxp)\). Then take complementary coordinate projections \(e_{11},e_{22}\) and arbitrary positive scalars \(a,b\); construct the faithful diagonal completion of their corner weights and identify the role of the values at the identities.

**Solution.** The compressed weight is \(\Psi\) itself, with support \(e_{11}\), smaller than \(p\). Thus faithfulness cannot be deleted from the exact-support statement in CW-07. For the second assertion, \(\theta(\lambda e_{11})=a\lambda\), \(\eta(\mu e_{22})=b\mu\), and (CW.10) is \(\Psi_{a,b}(x)=ax_{11}+bx_{22}\). Positivity of both coefficients makes it faithful. Both coordinate projections centralize it by CW-06. Finite values at their identities occur in this finite-dimensional model; the proof of CW-06 used finite contraction nets and remains valid when those identity values are infinite.

## The full cone calculus and its spectral flags

For \(a\in M\) and \(\omega\in M_*^+\), write

\[
(a\omega a^*)(x)=\omega(a^*xa),\qquad x\in M.
\]

Besides pointwise addition and nonnegative scaling, let \((H_i)\) be an increasing net in \(\widehat M_+\), write \(S=\sup_iH_i\), and define

\[
\begin{aligned}
(a^*Ha)(\omega)
  &=H(a\omega a^*),\\
S(\omega)
  &=\sup_i H_i(\omega).
\end{aligned}
\tag{CW.13}
\]

**Theorem.** All the operations in (CW.13) stay in \(\widehat M_+\). If
\(q_H[\xi]=H(\omega_\xi)\), then

\[
q_{a^*Ha}[\xi]=q_H[a\xi].
\]

If \(H\) and \(K\) correspond to extended closed forms \(q_H\) and \(q_K\), then \(H+K\) corresponds to their form sum on
\(D(q_H)\cap D(q_K)\). This intersection need not be dense and may equal \(\{0\}\).

Every \(H\in\widehat M_+\) also has a unique spectral notation. For every \(\omega\in M_*^+\), with the integral taken over \([0,\infty)\),

\[
\begin{aligned}
H(\omega)
  &=\int\lambda\,d\omega(e_H(\lambda))\\
  &\quad+\infty\,\omega(p_H).
\end{aligned}
\tag{CW.14}
\]

where \(e_H(\lambda)\) is increasing and right-continuous,
\(p_H=1-\sup_{\lambda\geq0}e_H(\lambda)\), and
\(0\cdot\infty=0\). Call \(H\) **faithful** if \(H(\omega)>0\) for every nonzero \(\omega\in M_*^+\), and **semifinite** if

\[
\{\omega\in M_*^+:H(\omega)<\infty\}
\]

is norm dense in \(M_*^+\). For this \(H\), the exact criteria are

\[
\begin{array}{c@{\quad\Longleftrightarrow\quad}c}
\text{faithful} & e_H(0)=0,\\
\text{semifinite} & p_H=0.
\end{array}
\tag{CW.15}
\]

**Proof.** The map \(\omega\mapsto a\omega a^*\) is positive linear and norm continuous, with norm at most \(\lVert a\rVert^2\). Composition with this map therefore preserves additivity, nonnegative homogeneity and lower semicontinuity. The vector-form identity follows directly from
\(a\omega_\xi a^*=\omega_{a\xi}\). Pointwise increasing suprema are additive because two increasing nonnegative nets indexed by the same directed set satisfy
\(\sup_i(s_i+t_i)=\sup_i s_i+\sup_i t_i\); they are lower semicontinuous because they are suprema of lower-semicontinuous functions. The form-sum assertion follows on vector functionals. Its form is closed: a sequence Cauchy for the sum norm is Cauchy in each of the two form norms, and the two Hilbert-space limits coincide.

For the spectral statement, use the unique pair \((e,A)\) of CW-02, put
\(p_H=1-e\), and let \(e_H(\lambda)\) be the spectral family of \(A\), extended by zero on \(p_H\mathcal H\). The vector identity (CW.3), followed by the countable vector expansion in SC-02 and monotone convergence of nonnegative scalar sums, gives (CW.14) for every positive normal functional. Uniqueness is the uniqueness already proved in CW-02.

The kernel of \(A\) is \(e_H(0)\mathcal H\). Hence (CW.14) vanishes on a nonzero vector functional exactly when \(e_H(0)\ne0\). If \(e_H(0)=0\), every nonzero positive normal functional has a vector expansion with a nonzero summand, and that summand has strictly positive or infinite energy. This proves the first equivalence in (CW.15).

Suppose \(p_H=0\), and let \(f_n=\mathbf1_{[0,n]}(A)\uparrow1\). For \(\omega\in M_*^+\), set
\(\omega_n(x)=\omega(f_nxf_n)\). Normality gives \(\omega_n\to\omega\) in predual norm, while

\[
H(\omega_n)=\omega(f_nAf_n)\leq n\omega(1)<\infty.
\]

Thus the finite-value functionals are dense. If \(p_H\ne0\), every finite-value \(\omega\) satisfies \(\omega(p_H)=0\). Such functionals cannot approximate any nonzero positive functional supported by \(p_H\), proving the converse. \(\square\)

For bounded positive operators (CW.13) is the usual congruence. For unbounded energies it is a form pullback, so the notation \(a^*Ha\) does not assert that an everywhere-defined operator product exists.

## Bounded resolvents recover order and monotone limits

Write the spectral pair from CW-09 as

\[
H=h+\infty p,
\]

where \(h\) is positive self-adjoint on \((1-p)\mathcal H\). Define bounded positive elements of \(M\) by

\[
H_0=(1+h)^{-1}(1-p),
\tag{CW.16}
\]

and, for \(\varepsilon>0\),

\[
\begin{aligned}
H_\varepsilon
  &=h(1+\varepsilon h)^{-1}(1-p)\\
  &\quad+\varepsilon^{-1}p.
\end{aligned}
\tag{CW.17}
\]

They satisfy

\[
H_\varepsilon
=\varepsilon^{-1}\bigl(1-(\varepsilon H)_0\bigr).
\tag{CW.18}
\]

**Theorem.** For \(H,K\in\widehat M_+\) and every fixed \(\varepsilon>0\),

\[
\begin{aligned}
H\leq K
  &\iff H_0\geq K_0,\\
  &\iff H_\varepsilon\leq K_\varepsilon.
\end{aligned}
\tag{CW.19}
\]

If \((H_i)\) is an increasing net and \(H=\sup_iH_i\), then the following equivalences hold. Both convergences on the right are strong, and the last condition is required for every \(\varepsilon>0\):

\[
\begin{aligned}
H_i\uparrow H
  &\iff (H_i)_0\downarrow H_0,\\
  &\iff (H_i)_\varepsilon\uparrow H_\varepsilon.
\end{aligned}
\tag{CW.20}
\]

For every \(\omega\in M_*^+\), the bounded approximants also recover the value:

\[
H(\omega)=\sup_{\varepsilon\downarrow0}\omega(H_\varepsilon).
\tag{CW.21}
\]

**Proof.** Let \(q_H\) be the extended closed form of CW-02. Its domain is
\(D(h^{1/2})\subseteq(1-p)\mathcal H\), and it is infinite off that domain. For \(\eta\in D(q_H)\), set

\[
\begin{aligned}
F_\xi(\eta)
  &=2\operatorname{Re}\langle\xi,\eta\rangle\\
  &\quad-\lVert\eta\rVert^2-q_H[\eta].
\end{aligned}
\]

Completing a square in the form Hilbert space gives the variational identity

\[
\langle H_0\xi,\xi\rangle
  =\sup_{\eta\in D(q_H)}F_\xi(\eta).
\tag{CW.22}
\]

Therefore \(q_H\leq q_K\) implies \(H_0\geq K_0\).

Conversely, suppose \(H_0\geq K_0\). The bounded positive factorization lemma gives a contraction \(C\) such that

\[
K_0^{1/2}=H_0^{1/2}C.
\tag{CW.23}
\]

For completeness, define a map first on \(\operatorname{ran}H_0^{1/2}\) by
\(H_0^{1/2}\xi\mapsto K_0^{1/2}\xi\). It is well defined and contractive because

\[
\lVert K_0^{1/2}\xi\rVert^2
\leq\lVert H_0^{1/2}\xi\rVert^2.
\]

Extend it by continuity to the closed range and by zero on its orthogonal complement. Taking the adjoint gives the contraction \(C\) in (CW.23).

The range of \(H_0^{1/2}\) is exactly \(D(q_H)\), and if
\(\eta=H_0^{1/2}\zeta\) with \(\zeta\) in the support of \(H_0\), then

\[
\lVert\eta\rVert^2+q_H[\eta]=\lVert\zeta\rVert^2.
\tag{CW.24}
\]

Take \(\eta=K_0^{1/2}\zeta\in D(q_K)\), with \(\zeta\) in the support of \(K_0\). Equations (CW.23)–(CW.24) give

\[
\eta\in D(q_H),
\qquad
\lVert\eta\rVert^2+q_H[\eta]
\leq\lVert C\zeta\rVert^2
\leq\lVert\zeta\rVert^2
=\lVert\eta\rVert^2+q_K[\eta].
\]

Thus \(q_H\leq q_K\). The vector-sum formula in CW-02 shows that form order is equivalent to pointwise order on all of \(M_*^+\). This proves the first equivalence in (CW.19). Apply it to \(\varepsilon H\) and \(\varepsilon K\), then use (CW.18), to obtain the second.

The map \(H\mapsto H_0\) is onto the positive contractions of \(M\). Indeed, for such a contraction \(R\), put \(p=1-s(R)\) and define
\(h=R^{-1}-1\) by spectral calculus on \(s(R)\mathcal H\); then
\((h+\infty p)_0=R\). Hence this map is an order-reversing bijection by (CW.19).

If \(H_i\uparrow H\), the bounded net \((H_i)_0\) decreases strongly to some positive contraction \(R\). The preceding bijection writes \(R=L_0\). Order reversal says that \(L\) is the least upper bound of the \(H_i\), so \(L=H\). This proves the first equivalence in (CW.20), including arbitrary directed nets. Formula (CW.18), applied after scaling the entire net by \(\varepsilon\), proves the second. Finally, the scalar functions
\(t\mapsto t/(1+\varepsilon t)\) increase to \(t\), while the value \(\varepsilon^{-1}\) on \(p\) increases to infinity. Equation (CW.21) follows from (CW.14) and monotone convergence. \(\square\)

The bounded coordinate \(H_0\) stores both parts of the energy: its kernel records the infinite projection, and its behavior near zero records the unbounded finite part. Thus strong convergence in (CW.20) does not erase domain information.

## Fixed-point extended densities classify every invariant normal weight

Let \(\varphi\) be a faithful normal semifinite weight on \(M\), and put
\(N=M_\varphi\). For \(x\in M_+\), define a normal weight on \(N\) by

\[
\Theta_x(a)=\varphi(a^{1/2}xa^{1/2}).
\tag{CW.25}
\]

Here and below \(a\in N_+\).
Normality, additivity in \(a\), and monotone continuity follow from the bounded-density calculus in CZ-07. For \(H\in\widehat N_+\), define

\[
\varphi_H(x)=\widehat{\Theta_x}(H).
\tag{CW.26}
\]

This holds for \(x\in M_+\), and the hat is the normal-weight extension of CW-03. If \(H_\varepsilon\in N_+\) are the bounded cutoffs from CW-10, write
\(b_\varepsilon=H_\varepsilon^{1/2}xH_\varepsilon^{1/2}\). Then

\[
\begin{aligned}
\varphi_H(x)
 &=\sup_{\varepsilon>0}\varphi_{H_\varepsilon}(x)\\
 &=\lim_{\varepsilon\downarrow0}\varphi(b_\varepsilon).
\end{aligned}
\tag{CW.27}
\]

**Theorem.** The map

\[
H\longmapsto\varphi_H
\tag{CW.28}
\]

is an order isomorphism from \(\widehat N_+\) onto the cone of all normal weights on \(M\) invariant under \(\sigma^\varphi\). The target includes zero weights, nonfaithful weights, and weights which are not semifinite. For every increasing directed net,

\[
\begin{aligned}
H_i\uparrow H
&\quad\Longleftrightarrow\quad\\
\varphi_{H_i}(x)&\uparrow\varphi_H(x).
\end{aligned}
\tag{CW.29}
\]

**Construction and invariance.** Each \(H_\varepsilon\) belongs to the centralizer. CZ-07 therefore makes \(\varphi_{H_\varepsilon}\) a normal semifinite weight, and CW-10 plus its order calculation makes these weights increase as \(\varepsilon\) decreases. Their pointwise supremum is a normal weight by NW-12. With \(b_\varepsilon\) as above,

\[
\begin{aligned}
\varphi_{H_\varepsilon}(\sigma_t^\varphi(x))
 &=\varphi(\sigma_t^\varphi(b_\varepsilon))\\
 &=\varphi(b_\varepsilon)\\
 &=\varphi_{H_\varepsilon}(x).
\end{aligned}
\tag{CW.30}
\]

Thus \(\varphi_H\) is invariant. Formula (CW.26) and preservation of increasing suprema in CW-03 show at once that \(H\mapsto\varphi_H\) preserves order and arbitrary increasing suprema.

**The scalar tests reflect order.** Use the faithful normal GNS representation
\(\pi_\varphi\) of \(M\) and its modular conjugation \(J_\varphi\). The dense linear space

\[
\mathcal D_0=J_\varphi\Lambda_\varphi(\mathfrak n_\varphi)
\subset H_\varphi
\]

is invariant under \(\pi_\varphi(N)\). Indeed CZ-05 gives
\(\Lambda_\varphi(ba)=J_\varphi\pi_\varphi(a^*)J_\varphi\Lambda_\varphi(b)\)
for every \(a\in N\) and \(b\in\mathfrak n_\varphi\), with
\(ba\in\mathfrak n_\varphi\). For a bounded positive \(a\in N\), it follows that

\[
\begin{aligned}
\Theta_{b^*b}(a)
 &=\|\Lambda_\varphi(ba^{1/2})\|^2\\
 &=\|\pi_\varphi(a^{1/2})J_\varphi\Lambda_\varphi(b)\|^2.
\end{aligned}
\]

Let \(q_H,q_K\) be the closed spectral forms of the extended positives
\(H,K\) in this representation, with infinite values outside their finite form domains. Increasing bounded spectral cutoffs and CW-03 extend the displayed identity to

\[
\varphi_H(b^*b)=q_H[J_\varphi\Lambda_\varphi(b)].
\tag{CW.31}
\]

The identity holds for every \(b\in\mathfrak n_\varphi\). Thus \(\varphi_H\leq\varphi_K\) implies \(q_H\leq q_K\) on \(\mathcal D_0\).

This dense-space comparison identifies the full form order because
\(\mathcal D_0\) is a form core for \(q_K\), not merely a dense set in the Hilbert norm.
To verify the core assertion, let \(E_n=1_{[0,n]}(K)\in N\), excluding the infinite part. For any
\(\xi\in D(q_K)\), spectral calculus gives \(E_n\xi\to\xi\) in the \(K\)-form norm. For fixed \(n\), choose \(\eta_j\in\mathcal D_0\) converging to \(E_n\xi\) in Hilbert norm. Then
\(E_n\eta_j\in\mathcal D_0\), and the bound
\(q_K[E_n\eta_j-E_n\xi]\leq n\|E_n\eta_j-E_n\xi\|^2\)
gives form-norm convergence. Choosing one sufficiently accurate vector for each \(n\) produces
\(\zeta_n\in\mathcal D_0\cap D(q_K)\) converging to \(\xi\) in that form norm.
The inequality on \(\mathcal D_0\), applied also to
\(\zeta_n-\zeta_m\), makes this sequence Cauchy for the \(H\)-form norm. Closedness yields
\(\xi\in D(q_H)\) and \(q_H[\xi]\leq q_K[\xi]\).
The vector-sum spectral description in CW-02 now gives \(H\leq K\) on all of \(N_*^+\).
The map in (CW.28) therefore reflects order as well as preserving it.

The centralizer restriction \(\varphi|_N\) need not be semifinite, so it cannot serve as a trace-density reference here. For example, take
\(M=B(L^2([1,2],dt))\), let \(h\) multiply by \(t\), and set
\(\varphi(x)=\operatorname{Tr}(h^{1/2}xh^{1/2})\).
Since \(1\leq h\leq2\), this is faithful, normal and semifinite. Its GNS realization is the Hilbert–Schmidt space with
\(\Lambda_\varphi(x)=xh^{1/2}\); the Tomita polar decomposition gives
\(\Delta=L_hR_{h^{-1}}\), hence
\(\sigma_s^\varphi(x)=h^{is}xh^{-is}\).
The centralizer is the diffuse multiplication algebra \(L^\infty([1,2])\): the imaginary powers generate the spectral algebra of \(h\), which is maximal abelian. Every nonzero positive multiplier has infinite trace, because a positive spectral cutoff on a set of positive measure has infinite-dimensional range. Its \(\varphi\)-weight is therefore infinite as well. Consequently \(\varphi|_N\) has no nonzero finite positive elements. The preceding GNS-core proof applies to this example and to arbitrary \(M\).

**Every invariant normal weight occurs.** Let \(\psi\) be an arbitrary normal \(\sigma^\varphi\)-invariant weight. Let \(e\) be the finite-domain projection from WS-02, let \(f\leq e\) be the maximal null projection from WS-04, and put \(p=e-f\). Invariance carries \(\mathfrak n_\psi\) onto itself, so it preserves the closure \(Me\); uniqueness of the right support gives \(\sigma_t^\varphi(e)=e\). It also carries null projections to null projections, so maximality gives \(\sigma_t^\varphi(f)=f\). Thus

\[
e,f,p\in N.
\]

By WS-06, the restriction \(\psi_p\) to \(pMp\) is faithful, normal, and semifinite. CZ-09 says the same for
\(\varphi^p=\varphi|_{pMp}\), with modular group
\(\sigma_t^{\varphi^p}=\sigma_t^\varphi|_{pMp}\). The faithful invariant-density theorem PT-05 therefore supplies a unique positive injective self-adjoint operator \(h\), affiliated with

\[
(pMp)_{\varphi^p}=pNp,
\]

such that \(\psi_p=(\varphi^p)_h\).

Set \(q=1-e\). On \(e\mathcal H=p\mathcal H\oplus f\mathcal H\), let \(A=h\oplus0\), and form the extended positive

\[
H_\psi=A+\infty q\in\widehat N_+.
\tag{CW.32}
\]

Put \(h_\varepsilon=h(1+\varepsilon h)^{-1}\). Its bounded cutoff is

\[
(H_\psi)_\varepsilon
 =h_\varepsilon+\varepsilon^{-1}q,
\]

with value zero on \(f\mathcal H\). Additivity of bounded centralizer densities in CZ-07 shows that, for \(x\in M_+\),

\[
\begin{aligned}
\varphi_{(H_\psi)_\varepsilon}(x)
 &=\varphi_{h_\varepsilon}(pxp)\\
 &\quad+\varepsilon^{-1}\varphi(qxq).
\end{aligned}
\tag{CW.33}
\]

If \(x=exe\), the second term vanishes and the first terms increase to
\((\varphi^p)_h(pxp)=\psi_p(pxp)\). If \(x\ne exe\), positivity implies \(qxq\ne0\). Faithfulness of \(\varphi\) then gives \(\varphi(qxq)>0\), possibly infinity, and the second term in (CW.33) tends to infinity. Therefore

\[
\varphi_{H_\psi}(x)=\psi_p(pxp).
\tag{CW.34}
\]

This equality applies to the preceding case \(x=exe\).
For every remaining positive \(x\), namely \(x\ne exe\), its value is
\(\varphi_{H_\psi}(x)=+\infty\).
This is exactly the reconstruction formula for \(\psi\) in WS-06. Hence \(\varphi_{H_\psi}=\psi\), proving surjectivity. Order reflection gives uniqueness.

Finally, suppose the weights \(\varphi_{H_i}\) increase pointwise to \(\varphi_H\). Order reflection makes \((H_i)\) increasing and bounded above by \(H\). If \(L=\sup_iH_i\), the already proved forward implication gives
\(\varphi_{H_i}\uparrow\varphi_L\). Injectivity gives \(L=H\), which proves the reverse implication in (CW.29). \(\square\)

The mathematical antecedents for the extended-positive definition, spectral description, cone calculus, bounded order coordinates, normal-weight extension, and fixed-point density classification are Takesaki, *Theory of Operator Algebras II*, IX.4.4–4.11, and Hiai, *Concise lectures on selected topics of von Neumann algebras*, [arXiv:2004.02383v1](https://arxiv.org/abs/2004.02383v1), Definition 8.1, Theorem 8.3, including its faithfulness and finite-value predual-density criteria, and Proposition 8.4. The complete arguments here use the existing course form, predual, support-corner, and invariant-density theorems. In particular, the extension proof uses dominated functionals and two directed suprema, the order proof uses the variational resolvent and bounded factorization rather than commuting spectral operators, and CW-11 recovers the nonsemifinite part from the finite-domain projection instead of presuming a densely defined density. CW-09 proves both the faithfulness and semifiniteness criteria, including norm density of the finite-value positive normal functionals; these correspond to (8.2) and (8.3) of Hiai's Theorem 8.3. The existing WS, WH, CZ, and PT units retain their own antecedent records. No source text or exercises are imported.
