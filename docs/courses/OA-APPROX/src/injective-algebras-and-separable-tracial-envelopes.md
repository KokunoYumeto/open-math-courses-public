# Injective algebras and separable tracial envelopes

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text: public domain (CC0).*

Every injective von Neumann algebra is locally approximately finite dimensional. Countability is needed for the familiar increasing sequence and the center-times-\(R\) structure, but the local approximation theorem itself has no factor or separability assumption. The bridge is a separable injective algebra containing any prescribed countable set in a faithfully tracial algebra.

We use exact trace-preserving finite models, [the separable finite theorem](central-disintegration-and-measurable-matrix-assembly.md#theorem-3-2), [injectivity and semidiscreteness](averaging-crossed-products-injectivity.md), [the properly infinite local theorem](properly-infinite-injective-algebras-and-dyadic-approximation.md#theorem-4-2), and [the finite AFD structure](central-traces-and-afd-finite-algebras.md#theorem-3-1). The trace inputs include the faithful normal center-valued trace on every finite algebra and the positive \(L^1\) densities of normal functionals relative to a faithful finite trace. Standard form, trace-preserving expectations, projection comparison and the finite/type II/properly infinite central decomposition retain their declared foundation and OA-MOD interfaces.

The selected [foundation results on projections and types](https://raw.githubusercontent.com/KokunoYumeto/open-math-courses/3188415a95f932d4ad6794418c3aed2abc3fbb77/docs/courses/foundations-of-von-neumann-algebras/src/projections-and-types-of-von-neumann-algebras.md) — Lemma 7.4, Proposition 8.4, Lemmas 9.3 and 9.5, Lemma 10.2, Theorem 10.3 and Proposition 15.2 — supply the finite type I structure and countable projection absorption used below. The central decomposition into finite type I, finite type II and properly infinite summands is the one needed for the local approximation theorem.

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

Finally \(A\) is norm separable. In the faithful normal trace GNS representation of \(N\), \(A\xi_\tau\) is dense by Kaplansky density. Hence \(L^2(N,\tau)\) is separable. The predual of a von Neumann algebra represented faithfully and normally on a separable Hilbert space is a quotient of its separable trace-class space, so \(N_*\) is separable. \(\square\)

**Corollary 1.2.** Every injective algebra with faithful normal tracial state is locally AFD, with no separability assumption.

**Proof.** Place a given finite family in the algebra \(N\) of Theorem 1.1. The preceding lesson's separable finite theorem supplies a unital finite algebra \(D\subset N\subset M\) and contractive tracial approximants to that family. On bounded sets trace \(2\)-norm convergence is sigma-strong* convergence. To see its intrinsic scope explicitly, if \(\psi(x)=\tau(hx)\), \(h\in L^1_+\), and \(\|d\|\le C\), then
\[
\psi(d^*d),\ \psi(dd^*)\le
L\|d\|_2^2+C^2\tau(h1_{(L,\infty)}(h)).
\tag{4}
\]
Choose \(L\) to control the integrable tail and then the \(2\)-norm error. This handles any finite collection of normal seminorms. \(\square\)

Exact trace preservation in (1) matters. Normal finite-rank maps approximating only a strongly dense C* algebra need not approximate its von Neumann closure; Exercise 7 gives a concrete counterexample.

## 2. Finite algebras need not carry a faithful normal state

**Theorem 2.1.** Every finite injective von Neumann algebra is locally AFD.

**Proof.** Fix a finite family of contraction tests \(x_l\), positive normal functionals \(\psi_1,\ldots,\psi_r\), and a required sigma-strong* error. We may suppose at least one functional is nonzero. Let \(T:M\to Z\) be the faithful normal center-valued trace, put
\[
\eta=\sum_j\psi_j|_Z,\qquad z=s(\eta)\in Z.
\tag{5}
\]
The restriction of \(\eta\) to \(Zz\) is faithful. The finite central algebra \(Mz\) has the faithful normal tracial state
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
Each \(F_i\) fixes \(M'\), and \(\|F_i(b)\|\le\|b\|\). Product ultraweak compactness gives a pointwise convergent subnet with ucp limit \(F\). For fixed \(x\in M\), vectors \(\xi,\zeta\in H\), and approximants \(d_i\in D_i\) to \(x\), its commutation with \(F_i(b)\) gives
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

**Proof.** The finite case combines Theorem 3.1 with the already proved central finite AFD structure theorem. For the infinite case choose a finite projection \(e\) with central support one. Such a projection exists by the semifinite projection lemma. The properly infinite identity splits into countably many equivalent copies of itself; transport \(e\) into each copy to obtain orthogonal equivalent projections \(e_n\), and put \(q=\sum_ne_n\). Their even and odd sums show \(q\) is properly infinite, and \(c(q)=1\). Since \(M_*\) is separable, \(M\) is sigma-finite. The countable absorption theorem, Proposition 15.2(2), gives \(1\precsim q\); as \(q\le1\), projection Schroeder–Bernstein gives \(q\sim1\).

Transporting the \(e_n\)'s by this equivalence yields a partition of \(1\) into countably many equivalent finite projections. Its matrix units give \(M\cong e'Me'\bar\otimes B(\ell^2)\), with \(e'\sim e\). The corner is injective, has separable predual, and is type \(\mathrm{II}_1\). Its center identifies with \(Z(M)\) by full central support and matrix splitting. Apply the finite case. This proof is valid for nonfactors: every projection equivalence used has full central support, and sigma-finiteness is stated exactly where absorption needs it. \(\square\)

**Corollary 4.2.** Every von Neumann subalgebra \(P\) of \(R\) is injective and AFD. It has the finite central decomposition
\[
P\cong(A_0\bar\otimes R)\ \oplus\
\bigoplus_{n\ge1}(A_n\bar\otimes M_n(\mathbb C)),
\tag{10}
\]
where the \(A_n\) are commutative von Neumann algebras, any of which may be zero. The countable sum is the von Neumann direct sum.

**Proof.** First suppose \(P\) has unit \(1_R\). The normal trace-preserving expectation \(E_P:R\to P\) exists in a finite traced algebra. Composing it with a ucp retraction onto the injective \(R\) gives a ucp retraction onto \(P\), so \(P\) is injective. It is finite and has separable predual: it acts faithfully and normally on the separable trace Hilbert space of \(R\). Theorem 3.1 gives an increasing finite-dimensional generating sequence.

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

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft: Proposition 2.6.7, p.48, proves the tracial Hilbert-space separability criterion; Theorems 7.3.8 and 7.4.5, pp.110–111 and 114–115, prove the normal-functional and positive integrable-density inputs; Theorem 9.1.2, p.140, proves existence of the normal trace-preserving expectation. Proposition 10.2.2, p.161, explains the ucp extension and retraction criteria, and Theorem 10.2.4, p.162, proves injectivity of \(R\).

The center-times-\(R\) conclusions retain separable predual. The separable-envelope and finite normal-test arguments above prove the local theorem for arbitrary injective algebras. The local converse is also proved without countability. All twelve exercises have full solutions.
