# Injective algebras and separable tracial envelopes

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text: public domain (CC0).*

Every injective von Neumann algebra is locally approximately finite dimensional. Countability is needed for the familiar increasing sequence and the center-times-\(R\) structure, but the local approximation theorem itself has no factor or separability assumption. The bridge is a separable injective algebra containing any prescribed countable set in a faithfully tracial algebra.

The complete trace-preserving matrix models, [separable finite theorem](central-disintegration-and-measurable-matrix-assembly.md#theorem-3-2), [properly infinite theorem and dyadic construction](properly-infinite-injective-algebras-and-dyadic-approximation.md#theorem-4-2), and [central finite AFD structure](central-traces-and-afd-finite-algebras.md#theorem-3-1) supply the approximation arguments. The [semidiscrete retraction proof](semidiscrete-finite-models.md#theorem-4-2) is used at its full normal finite-matrix scope.

The remaining foundations are the complete [central trace, comparison, corner-center and countable absorption proofs](../components/central-finite-trace-inputs.md), [faithful normal-state topology](../components/central-sequence-foundations.md#nt2-faithful-state-topology), [trace Hilbert space and trace-preserving expectations](../components/invariant-state-trace-hilbert-inputs.md), and actual measurable operators and positive integrable densities. In particular TI.19–20 proves the onto positive isometry \(L^1(M,\tau)\to M_*\) for every faithful normal semifinite trace, including nonseparable finite algebras. Its measure-completion, closed-domain, spectral-tail, normality and predual prerequisites are included in that proof route. Formula (4) uses that actual density theorem.

The [projection proofs PC1–7](../components/central-finite-trace-inputs.md#pc-1) include arbitrary orthogonal sums, central comparison, mutual subequivalence, the normal corner-center isomorphism, the finite central-part criterion and PC8 countable absorption. Here type II means that there is no nonzero abelian projection and that the central supports of finite projections fill the identity. The full-support finite corner and its countable matrix decomposition will be constructed below. The zero algebra has the zero finite-dimensional algebra as its unital approximant; the faithful-state arguments concern nonzero algebras.

## 1. A countable set has a separable injective envelope

**Theorem 1.1.** Let \(M\) be injective with faithful normal tracial state \(\tau\). Every countable subset of \(M\) is contained in a von Neumann subalgebra \(N\subset M\) with separable predual that is injective. The restricted trace on \(N\) is faithful and normal.

**Proof.** Start with a norm separable unital C* algebra \(A_0\) containing the specified set. Suppose \(A_0\subset\cdots\subset A_k\) have been constructed, with countable norm dense sets of contractions \(c_{j,l}\) in \(A_j\). At stage \(k\ge1\), apply the trace-preserving finite-model theorem to the finite list
\[
c_{j,l}\quad(0\le j<k,\ 1\le l\le k).
\]
It gives normal ucp \(S_k:M\to M_{q_k}\) and ucp \(T_k:M_{q_k}\to M\), satisfying
\[
\tau_{q_k}S_k=\tau,\quad \tau T_k=\tau_{q_k},\quad
\|\theta_k(c_{j,l})-c_{j,l}\|_2<1/k,\qquad
\theta_k=T_kS_k.
\tag{1}
\]
Adjoin all the finitely many entries \(T_k(E_{ab})\) to \(A_{k-1}\) to form \(A_k\), and choose its dense set. This inductive order uses only already chosen tests.

Put \(A=\overline{\bigcup_kA_k}^{\|\cdot\|}\), \(N=A''\) inside \(M\). Each \(T_k\) takes values in \(N\). Schwarz and the two exact trace identities give
\[
\|\theta_k(x)\|_2\le\|x\|_2\qquad(x\in M).
\tag{2}
\]
The diagonal choice of tests, norm contractivity and norm density imply \(\theta_k(a)\to a\) in \(2\)-norm for every \(a\in A\). If \(x\in N\), Kaplansky density supplies \(a\in A\) with \(\|x-a\|_2\) arbitrarily small. Thus
\[
\|\theta_k(x)-x\|_2
\le2\|x-a\|_2+\|\theta_k(a)-a\|_2\longrightarrow0.
\tag{3}
\]
The maps \(S_k|_N,T_k\) are normal: \(S_k\) is normal by (1), and a positive map from a finite-dimensional algebra is normal. Their compositions converge pointwise \(2\)-norm, hence pointwise ultraweakly on the bounded image of each fixed \(x\). These are finite matrix models for \(N\), making it semidiscrete and therefore injective.

Finally \(A\) is norm separable. In the faithful normal trace GNS representation of \(N\), \(A\xi_\tau\) is dense by Kaplansky density. Hence \(L^2(N,\tau)\) is separable. For a separable Hilbert space \(K\), its completed Hilbert projective tensor \(\overline K\widehat\otimes_\pi K\) is separable: finite rational combinations of tensor pairs from countable dense sets are dense. The complete predual coefficient theorem identifies \(N_*\) as the quotient of this space by the kernel of its normal coefficient map. Indeed finite sums give vector coefficients and the completed projective tensors give their absolutely summable series; every normal functional has such a series. Thus \(N_*\) is separable. The restricted trace is faithful, and normality follows by the normal inclusion \(N\subset M\). \(\square\)

**Corollary 1.2.** Every injective algebra with faithful normal tracial state is locally AFD, with no separability assumption.

**Proof.** Place a given finite family in the algebra \(N\) of Theorem 1.1. The preceding lesson's separable finite theorem supplies a unital finite algebra \(D\subset N\subset M\) and contractive tracial approximants to that family. On bounded sets trace \(2\)-norm convergence is sigma-strong* convergence. To see its intrinsic scope explicitly, if \(\psi(x)=\tau(hx)\), \(h\in L^1_+\), and \(\|d\|\le C\), then
\[
\psi(d^*d),\ \psi(dd^*)\le
L\|d\|_2^2+C^2\tau(h1_{(L,\infty)}(h)).
\tag{4}
\]
Choose \(L\) to control the integrable tail and then the \(2\)-norm error. This handles any finite collection of normal seminorms. \(\square\)

Exact trace preservation in (1) matters. Normal finite-rank maps approximating only a strongly dense C* algebra need not approximate its von Neumann closure; Exercise 7 gives a concrete counterexample.

<a id="normal-model-counterexample-inputs"></a>

### The scalar construction for the normal-model counterexample

Here are all the measure and positivity inputs for Exercise 7. Enumerate the rationals in \((0,1)\) as \(q_j\), and choose an open interval about \(q_j\) of length at most \(2^{-j-2}\). Their union \(O\) is dense and has Lebesgue measure at most \(1/4\). Hence \(K=[0,1]\setminus O\) is closed, nowhere dense, and has measure at least \(3/4\). Every dyadic cell has nonempty interior meeting the open set \(O\), so its intersection with \(O\) has positive measure. Endpoints can be assigned to one of their adjacent cells without changing any integral.

The averages on these intersections are positive normal unital scalar functionals. Positivity makes a scalar functional completely positive: for a positive operator matrix and a scalar vector, its scalar quadratic form is the functional applied to a positive element. Taking their diagonal direct sum therefore gives normal ucp \(S_n\). At each point of a dyadic cell, \(T_n\) is one diagonal matrix coefficient, a ucp scalar functional; positivity at every matrix size proves that \(T_n\) is ucp. Its finite-dimensional domain makes it normal. Oscillation of a continuous function on intervals of length \(2^{-n}\) tends uniformly to zero, so these maps approximate every continuous function uniformly.

For completeness continuous functions are strongly dense in the represented \(L^\infty[0,1]\). [Finite regularity and compact cutoffs](../components/compact-rmk-from-function-covers.md#rm03) give, for every measurable set modulo a null set, continuous functions between zero and one converging to its indicator in \(L^2\). Approximate bounded functions first by simple functions, then their indicators this way. Apply the continuous radial retraction to the original bound disk; its error from a point in that disk is at most twice the original error. Thus the continuous approximants have a common norm bound and converge in \(L^2\), as do their conjugates. If \(g\in L^2\), truncate \(g\) to a bounded function; the bounded part of \(g\) tests the \(L^2\) error, and the remaining tail is controlled by the common sup norm bound. This proves strong convergence of the multiplication operators and their adjoints. Conversely every multiplication operator in this von Neumann algebra is bounded and measurable, so the closure is precisely \(L^\infty\).

Finally the averages of \(1_K\) on every chosen intersection are zero, while its Lebesgue integral is positive. This supplies the failure on the closure and the failure of trace preservation, without changing the full example of Exercise 7.

## 2. Finite algebras need not carry a faithful normal state

**Theorem 2.1.** Every finite injective von Neumann algebra is locally AFD.

**Proof.** Fix a finite family of contraction tests \(x_l\), positive normal functionals \(\psi_1,\ldots,\psi_r\), and a required sigma-strong* error. We may suppose at least one functional is nonzero. Let \(T:M\to Z\) be the faithful normal center-valued trace, put
\[
\eta=\sum_j\psi_j|_Z,\qquad z=s(\eta)\in Z.
\tag{5}
\]
The support in (5) can be constructed without a global faithful state. In the commutative algebra \(Z\), finite joins of projections of zero \(\eta\)-value again have zero value. Normality makes their full supremum \(p\) have zero value. Put \(z=1-p\). If a positive central element on \(z\) had zero value, each of its positive spectral cuts would be a zero-value projection dominated by both \(p\) and \(z\), hence zero. This proves faithfulness on \(Zz\), and also \(\eta(1-z)=0\). The restriction of \(\eta\) to \(Zz\) is faithful. The finite central algebra \(Mz\) has the faithful normal tracial state
\[
\tau_z(x)=\eta(T(x))/\eta(z)\qquad(x\in Mz).
\tag{6}
\]
Injectivity passes to this central corner, so Corollary 1.2 approximates all \(zx_l\) by contractions in a unital finite algebra \(D_z\subset Mz\).

Each \(\psi_j(1-z)=0\), and Cauchy–Schwarz shows it ignores every operator supported on \(1-z\). Its restriction to \(Mz\) has an \(L^1(\tau_z)\) density. Formula (4), with \(C=2\) for the difference of two contractions, makes sufficiently small \(\tau_z\)-norm errors small for both \(\psi_j(d^*d)\) and \(\psi_j(dd^*)\). For example choose each tail contribution below half the squared desired error and then choose \(L\|d\|_{2,z}^2\) below its other half. Adjoin \(\mathbb C(1-z)\) to \(D_z\), and choose zero approximants there. This is a finite-dimensional unital algebra meeting all original seminorm tests. If all \(\psi_j=0\), any scalar algebra works. \(\square\)

The central support cut in (5) depends on the finite neighborhood being tested. The argument neither asserts nor requires a global faithful normal state.

## 3. The full local equivalence

**Theorem 3.1.** For every von Neumann algebra \(M\), the following are equivalent:

1. \(M\) is injective.
2. \(M\) is locally AFD: every finite subset has approximants in a unital finite-dimensional subalgebra in every sigma-strong* neighborhood.

If \(M_*\) is separable, these are also equivalent to generation by an increasing sequence of finite-dimensional unital subalgebras.

**Proof.** Split \(1=z_f+z_\infty\) into its finite and properly infinite central parts. An injective \(M\) has injective summands. Theorem 2.1 handles \(Mz_f\), and the previously proved properly infinite local theorem handles \(Mz_\infty\). Approximate the two central restrictions of any finite family and add their finite algebras. Central orthogonality makes the squared normal seminorms add, so halving their squared error budgets gives local AFD in \(M\).

Conversely represent a locally AFD \(M\) in standard form on \(H\). Direct the finite tests and sigma-strong* neighborhoods by refinement, and choose a finite-dimensional unital \(D_i\subset M\) meeting each test. The compact unitary group of \(D_i\) gives a ucp map
\[
F_i(b)=\int_{\mathcal U(D_i)}ubu^*\,du\in D_i',\qquad b\in B(H).
\tag{7}
\]
The average in (7) has an explicit finite formula. If \(D_i=\bigoplus_aM_{n_a}\) has matrix units \(e^{(a)}_{jk}\) with their block identities summing to one, put
\[
 F_i(b)=\sum_a\frac1{n_a}\sum_{j,k=1}^{n_a}
                 e^{(a)}_{jk}b e^{(a)}_{kj}.
\]
Each summand is a completely positive Kraus term. Summing its value at one gives one. Matrix-unit multiplication shows that the output commutes with every block and every matrix unit, hence belongs to \(D_i'\). If \(b\in D_i'\), moving \(b\) past the units shows that this sum is \(b\). Conjugating the input by any block unitary and summing its scalar matrix entries uses \(\sum_k u_{rk}\overline{u_{sk}}=\delta_{rs}\), proving invariance. Thus this finite formula is the normalized invariant unitary average denoted by the integral in (7); no general existence theorem for Haar measure is a prerequisite here. It is normal and ucp. Each \(F_i\) fixes \(M'\), and \(\|F_i(b)\|\le\|b\|\). Product ultraweak compactness gives a pointwise convergent subnet with ucp limit \(F\). For fixed \(x\in M\), vectors \(\xi,\zeta\in H\), and approximants \(d_i\in D_i\) to \(x\), its commutation with \(F_i(b)\) gives
\[
\begin{aligned}
&\left|\langle\zeta,[F_i(b),x]\xi\rangle\right|\\
&\le\|b\|\|\zeta\|\|(x-d_i)\xi\|\\
&\quad+\|b\|\|\xi\|\|(x-d_i)^*\zeta\|\\
&\longrightarrow0.
\end{aligned}
\tag{8}
\]
The directed tests include these two seminorms; one can choose the \(d_i\) for this fixed finite requirement on each tail. Passing to the limit gives \(F(b)\in M'\). Thus \(F\) is a ucp retraction onto \(M'\). If \(J\) is the standard conjugation, \(b\mapsto JF(JbJ)J\) is a linear ucp retraction onto \(M\). Complete positivity follows at each matrix size by conjugating on the conjugate Hilbert space twice. The norm-one projection criterion proves injectivity.

For separable predual, the existing local-to-sequential construction treats properly infinite summands by dyadic factors, finite type II summands by finite matrix/central partitions, and finite type I summands by finite central partitions and matrix blocks. It therefore produces the claimed increasing generating sequence. Such a sequence gives local AFD by bounded strong* density of its union, and the directed averaging proof also gives injectivity. \(\square\)

The implication from local AFD in (8) does not assume that the chosen \(D_i\)'s are nested. Both error terms act on fixed vectors, which is essential when the averaged operators vary with \(i\).

## 4. The central structure and subalgebras of \(R\)

**Corollary 4.1.** If \(M\) is injective of type \(\mathrm{II}_1\) or \(\mathrm{II}_\infty\) with separable predual, then respectively
\[
M\cong Z(M)\bar\otimes R,\qquad
M\cong Z(M)\bar\otimes R\bar\otimes B(\ell^2).
\tag{9}
\]

<a id="full-nonfactor-matrix-decomposition"></a>

Here is the full projection construction needed for the infinite case. A separable predual gives a faithful normal state by NT2, so every orthogonal family of nonzero projections is countable. Every nonzero projection \(r\) contains a nonzero finite subprojection: its central support meets that of some finite projection \(p\); PC2 supplies a nonzero polar bridge between subprojections of \(r\) and \(p\), and finiteness passes to equivalent subprojections. Choose a maximal orthogonal family of finite nonzero projections \(p_j\); the preceding argument forces their sum to be one. Their central supports therefore have supremum one. Define disjoint central projections
\[
 z_j=c(p_j)\left(1-\bigvee_{i<j}c(p_i)\right),\qquad
 e=\sum_jz_jp_j.
\]
They fill the center, and \(c(e)=1\). The projection \(e\) is finite: an isometry in \(eMe\) compresses on each \(z_j\) to an isometry in the finite corner of \(p_j\), so each compressed defect is zero; their strong sum is the entire defect. The corner has no abelian nonzero projection, hence is of type \(\mathrm{II}_1\).

A properly infinite identity has an orthogonal countable partition \(r_j\sim1\), with any residual absorbed into the first member by PC3 and PC5. Transport \(e\) into these corners to obtain \(e_j\sim e\), as in the proof below. If \(v_j^*v_j=e_1\), \(v_jv_j^*=e_j\), the strong sums of \(v_{2j}v_j^*\) and \(v_{2j-1}v_j^*\) implement equivalences of \(q=\sum_je_j\) with its even and odd sums. PC1 justifies the sums and all initial and final projections. The same holds on every nonzero central cut; full central support of \(e\) ensures those cuts are nonzero. Thus \(q\) is properly infinite and \(c(q)=1\). The countable absorption proof PC8 applies to the source projection \(1\), giving \(1\precsim q\); PC3 then gives \(1\sim q\). This is the countable absorption theorem in exactly the nonfactor scope used here.

Choose \(w^*w=1\), \(ww^*=q\) and put \(f_j=w^*e_jw\). These are equivalent finite projections with sum one. Set \(f=f_1\), and choose \(u_j^*u_j=f\), \(u_ju_j^*=f_j\), with \(u_1=f\). The map
\[
 U:H\longrightarrow fH\otimes\ell^2,\qquad
 U\xi=\sum_j u_j^*\xi\otimes\delta_j
\]
is unitary: orthogonality gives equality of squared norms, and the inverse on finitely supported vectors is \(\sum_j u_j\xi_j\). Completeness extends that inverse to all vectors. For \(x\in M\), all its matrix entries \(u_i^*xu_j\) belong to \(fMf\). Its finite block compressions lie in \(fMf\otimes M_n\), are uniformly bounded and converge strongly to \(UxU^*\). Conversely the elementary matrices \(a\otimes E_{ij}\) correspond to \(u_i a u_j^*\in M\), so taking the von Neumann closure gives both inclusions and
\[
 UMU^*=fMf\bar\otimes B(\ell^2).
\]
Commuting with every scalar matrix unit forces a central element to be a constant diagonal; commuting with \(fMf\) makes its entry central. Equivalently PC4 identifies \(Z(fMf)=fZ(M)\), normally and onto, since \(c(f)=1\). Compression extends every normal corner functional normally to \(M\), so the corner has separable predual. A ucp retraction onto \(M\), compressed by \(f\) after extending an operator on \(fH\) by zero, is a ucp retraction onto \(fMf\), with unit \(f\). Thus injectivity also passes to this corner.

**Proof.** The finite case combines Theorem 3.1 with the already proved central finite AFD structure theorem. For the infinite case choose a finite projection \(e\) with central support one. Such a projection exists by the semifinite projection lemma. The properly infinite identity splits into countably many equivalent copies of itself; transport \(e\) into each copy to obtain orthogonal equivalent projections \(e_n\), and put \(q=\sum_ne_n\). Their even and odd sums show \(q\) is properly infinite, and \(c(q)=1\). Since \(M_*\) is separable, \(M\) is sigma-finite. The countable absorption theorem PC8, proved above at its exact source-countability scope, gives \(1\precsim q\); as \(q\le1\), projection Schroeder–Bernstein gives \(q\sim1\).

Transporting the \(e_n\)'s by this equivalence yields a partition of \(1\) into countably many equivalent finite projections. Its matrix units give \(M\cong e'Me'\bar\otimes B(\ell^2)\), with \(e'\sim e\). The corner is injective, has separable predual, and is type \(\mathrm{II}_1\). Its center identifies with \(Z(M)\) by full central support and matrix splitting. Apply the finite case. This proof is valid for nonfactors: every projection equivalence used has full central support, and sigma-finiteness is stated exactly where absorption needs it. \(\square\)

**Corollary 4.2.** Every von Neumann subalgebra \(P\) of \(R\) is injective and AFD. It has the finite central decomposition
\[
P\cong(A_0\bar\otimes R)\ \oplus\
\bigoplus_{n\ge1}(A_n\bar\otimes M_n(\mathbb C)),
\tag{10}
\]
where the \(A_n\) are commutative von Neumann algebras, any of which may be zero. The countable sum is the von Neumann direct sum.

**Proof.** If \(P=0\), all the summands in (10) are zero. Otherwise first suppose \(P\) has unit \(1_R\). The normal trace-preserving expectation \(E_P:R\to P\) exists in a finite traced algebra. Composing it with a ucp retraction onto the injective \(R\) gives a ucp retraction onto \(P\), so \(P\) is injective. It is finite and has separable predual: it acts faithfully and normally on the separable trace Hilbert space of \(R\). Theorem 3.1 gives an increasing finite-dimensional generating sequence.

Split \(P\) into its finite type I and type \(\mathrm{II}_1\) central parts. The finite type I structure theorem decomposes the first into \(A_n\bar\otimes M_n\), \(n\ge1\); infinite homogeneous sizes are excluded by finiteness. Corollary 4.1 identifies the second with its center \(A_0\) tensored with \(R\). This gives (10). If \(P\)'s unit is a projection \(p<1_R\), apply the same argument in the injective finite corner \(pRp\), with normalized trace. \(\square\)

## 5. Exercises with complete solutions

**Exercise 1.** Why must the entries of \(T_k\), rather than the entries of \(S_k\), be adjoined?

*Solution.* \(S_k\) already maps the prospective algebra into a fixed finite matrix algebra. The range condition needed for a model on \(N\) is \(T_k(M_{q_k})\subset N\). Its entries span that range linearly, so adjoining all \(T_k(E_{ab})\) enforces precisely this condition.

**Exercise 2.** Prove (2).

*Solution.* Schwarz gives \(S_k(x)^*S_k(x)\le S_k(x^*x)\). Taking \(\tau_{q_k}\) gives \(\|S_k(x)\|_2^2\le\tau(x^*x)\). Apply the same argument to \(T_k\) and use \(\tau T_k=\tau_{q_k}\). The two contractions compose.

**Exercise 3.** Show that the diagonal tests imply convergence on \(A\).

*Solution.* Every fixed \(c_{j,l}\) is tested at every \(k>\max(j,l)\), so its error tends to zero. Approximate a contraction of \(A_j\) in norm by one such element. Norm contractivity bounds its two replacement errors by that norm distance. Then approximate an element of \(A\) by an element of some \(A_j\) and repeat. Scaling handles arbitrary norms.

**Exercise 4.** Derive (4), including its adjoint version.

*Solution.* Split \(h=h1_{[0,L]}(h)+h1_{(L,\infty)}(h)\). The bounded part contributes at most \(L\tau(d^*d)\), while the positive tail contributes at most \(C^2\tau(h1_{(L,\infty)}(h))\). Apply the same bound to \(dd^*\), using \(\tau(dd^*)=\tau(d^*d)\). No commutation of \(h\) and \(d\) is required.

**Exercise 5.** Why is (6) faithful?

*Solution.* If \(x\ge0\) in \(Mz\) has \(\eta(T(x))=0\), faithfulness of \(\eta\) on \(Zz\) gives \(T(x)=0\). Faithfulness of the center-valued trace then gives \(x=0\). Its central bimodularity and trace identity make the composition a trace; normality of both maps gives normality.

**Exercise 6.** Prove that \(\psi_j\) ignores the complementary central summand.

*Solution.* Since \(\sum_j\psi_j(1-z)=\eta(1-z)=0\) and each term is nonnegative, every term vanishes. Cauchy–Schwarz yields \(|\psi_j((1-z)x)|^2\le\psi_j(1-z)\psi_j(x^*x)=0\). Centrality removes the other orientation as well.

**Exercise 7.** Give normal finite matrix models converging on a strongly dense C* algebra but failing on its von Neumann closure.

*Solution.* In \(L^\infty[0,1]\), choose a positive-measure closed nowhere dense set \(K\). For every dyadic cell \(I_{n,j}\), its complement \(E_{n,j}=I_{n,j}\setminus K\) has positive measure. Let \(S_n(f)\) be the diagonal matrix of the averages of \(f\) on these \(E_{n,j}\), and let \(T_n\) send a matrix to the step function whose cell values are its diagonal entries. Both maps are normal ucp. Their composition approximates each continuous function uniformly, since the error is at most its oscillation on a dyadic cell. Continuous functions are strongly dense in \(L^\infty[0,1]\). Yet \(T_nS_n(1_K)=0\) for every \(n\), so convergence fails in trace norm and ultraweakly on \(1_K\). The models do not preserve Lebesgue trace.

**Exercise 8.** Why does (8) need sigma-strong* approximation?

*Solution.* Its first term involves \((x-d_i)\xi\) and its second involves \((x-d_i)^*\zeta\). Sigma-strong* neighborhoods control both. Mere strong convergence would not supply the second vector estimate for general \(x,d_i\).

**Exercise 9.** Does (8) require uniform strong convergence on all vectors \(F_i(b)\xi\)?

*Solution.* No. Move the second error to the adjoint acting on the fixed vector \(\zeta\), and bound \(\|F_i(b)\xi\|\) by \(\|b\|\|\xi\|\). The two errors therefore act only on the fixed vectors \(\xi,\zeta\), exactly as displayed.

**Exercise 10.** Explain why \(q=\sum_ne_n\) in Corollary 4.1 is properly infinite.

*Solution.* A bijection from \(\mathbb N\) to its even indices transports the mutually equivalent diagonals to show \(q\sim\sum_ne_{2n}\); the odd indices give a second orthogonal copy. Central cuts preserve these equivalences and have nonzero diagonal whenever the cut is nonzero, since \(c(e)=1\). Thus every nonzero central cut is infinite.

**Exercise 11.** Why does finiteness rule out an infinite matrix size in (10)?

*Solution.* In \(A\bar\otimes B(\ell^2(I))\) for infinite \(I\), a bijection \(I\to I\setminus\{i_0\}\) gives a proper isometry. Its initial projection is the identity and its final projection omits \(1\otimes e_{i_0i_0}\). Thus the identity is infinite. A central summand of finite \(P\) cannot have this form.

**Exercise 12.** Why is Corollary 4.2 consistent with \(P\) having a diffuse center?

*Solution.* The expectation onto \(P\) and injectivity do not force \(P\) to be a factor. Its finite type II central summand has the full center \(A_0\), and every homogeneous finite type I summand has its own center \(A_n\). For example an abelian diffuse subalgebra lies entirely in the \(n=1\) summand; no \(R\) summand is required.

## References and proof scope

George A. Elliott, [*On approximately finite-dimensional von Neuman algebras, II*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6B3F0C139253D86C4335ECD2549F1B7A/S0008439500059609a.pdf/on_approximately_finitedimensional_von_neuman_algebras_ii.pdf), Canadian Mathematical Bulletin 21 (1978), 415–418: Theorem 2, pp.415–416, proves the local AFD converse by averaging and an ultraweak limit; Theorem 4 and Corollary 5, pp.416–417, give the general injective-to-local-AFD reduction. The finite branch of Theorem 4 also uses injectivity of every von Neumann subalgebra of a finite injective algebra. Combined with the tracial separability argument, it supports the existence asserted in Theorem 1.1. The explicit trace-preserving model construction above is retained in full.

Sorin Popa, [*A short proof of “injectivity implies hyperfiniteness” for finite von Neumann algebras*](https://www.theta.ro/jot/archive/1986-016-002/1986-016-002-005.pdf), Journal of Operator Theory 16 (1986), 261–272: the theorem and full proof in §3, pp.271–272, treat finite algebras without separable predual, using the local matrix-corner approximation proved in Proposition 2.2, p.270. Sections 1–2 use additional primary inputs; their citation does not certify the complete reference chain.

Uffe Haagerup, [*A new proof of the equivalence of injectivity and hyperfiniteness for factors on a separable Hilbert space*](https://doi.org/10.1016/0022-1236(85)90002-3), Journal of Functional Analysis 62 (1985), 160–201: §6.3, pp.199–200, discusses the nonfactor extension, and §6.4, p.200, records Elliott’s arbitrary-algebra equivalence. Those final sections are discussion and attribution, not complete proofs of the general central structure and equivalence.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft: the trace Hilbert-space chapter discusses separability; the normal-functional and positive integrable-density chapters discuss the trace pairing; the conditional-expectation chapter gives the normal trace-preserving expectation. The injectivity chapter discusses ucp extension/retraction criteria and injectivity of \(R\). The complete programme trace-density, coefficient, expectation and retraction arguments are the proof inputs here; page numbers differ between author drafts.

The center-times-\(R\) conclusions retain separable predual. The separable-envelope and finite normal-test arguments above prove the local theorem for arbitrary injective algebras. The local converse is also proved without countability. All twelve exercises have full solutions.
