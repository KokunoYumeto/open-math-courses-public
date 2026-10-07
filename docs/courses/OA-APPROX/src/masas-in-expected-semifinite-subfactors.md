# MASAs in expected semifinite subfactors

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text: public domain (CC0).*

An abelian algebra can be maximal inside a subfactor and still commute with extra operators in the ambient algebra. The [pinching test](abelian-pinching-and-relative-commutants.md#theorem-2-1) lets us rule out those extra operators during an increasing matrix construction. Its diagonal will be a MASA in the ambient factor, while the matrix permutations guarantee enough normalizers inside the subfactor.

For a unital abelian von Neumann algebra \(A\subset P\), write
\[
\mathcal N_P(A)=\{u\in\mathcal U(P):uAu^*=A\},
\qquad \mathcal P_P(A)=\mathcal N_P(A)''.
\tag{1}
\]
A **MASA** means \(A'\cap P=A\). In a factor \(P\), it is **regular** if \(\mathcal P_P(A)=P\), and **semiregular** if \(\mathcal P_P(A)\) is a factor. Semiregularity does not require that this factor equal the ambient one.

We prove the semifinite expected-subfactor construction. A conditional expectation in this theorem is normal. Its faithfulness will follow, rather than be assumed. Separability means separable predual. The finite construction and the semifinite matrix reduction are given in full. For the AFD \(\mathrm{II}_\infty\) regularity clause we also use finite-corner permanence, supplied by the later [finite injective-factor proof](unitary-couplings-and-finite-injective-factors.md#theorem-5-1).

## 1. Faithfulness from irreducibility

**Lemma 1.1.** Let \(N\subset M\) be unital von Neumann algebras, let \(N\) have a faithful normal state, and suppose \(N'\cap M\subset N\). Every normal conditional expectation \(E:M\to N\) is faithful.

**Proof.** Choose a faithful normal state \(\psi\) of \(N\), and put \(\theta=\psi E\). This is a normal state of \(M\), possibly nonfaithful for now. Its support \(p\) gives
\[
K=\{x:\theta(x^*x)=0\}=M(1-p)
=\{x:E(x^*x)=0\}.
\tag{2}
\]
The last equality uses positivity and faithfulness of \(\psi\). Here the support formula can be obtained directly. If \(a\ge0\) and \(\theta(a)=0\), the increasing functions \(\min\{1,na\}\le na\) converge strongly to its support, whose state value is therefore zero by normality. Finite joins of state-null projections are null: their join is the support of their positive sum. The join \(q\) of all null projections is also null, by normality on the directed finite joins. Now \(\theta(x^*x)=0\) implies that the support of \(x^*x\) is below \(q\), hence \(x=xq\). Conversely \(x=xq\) implies \(0\le x^*x\le\|x\|^2q\) and thus \(\theta(x^*x)=0\). Consequently the null left ideal is \(Mq\), and \(p=1-q\) is the support in (2). If \(a\in N\), bimodularity gives \(E((xa)^*xa)=a^*E(x^*x)a=0\) for \(x\in K\). Hence \(K\) is invariant under right multiplication by \(N\). Taking \(x=1-p\), and then \(a^*\), shows
\[
(1-p)ap=0=pa(1-p).
\]
Thus \(1-p\in N'\cap M\subset N\). But \(E(1-p)=0\) by (2), while \(E\) fixes \(N\). Therefore \(p=1\), making \(\theta\), and consequently \(E\), faithful. \(\square\)

This argument is valid for nonfactor algebras under its stated relative-commutant condition. Normality enters the support formula for the composed state.

## 2. The finite expected-subfactor theorem

**Theorem 2.1.** Let \(M\) have separable predual, and let \(N\subset M\) be an irreducible \(\mathrm{II}_1\) subfactor, meaning \(N'\cap M=\mathbb C1\). Suppose a normal expectation \(E:M\to N\) exists. There are
\[
A\subset R\subset N,\qquad R\cong
\bar\bigotimes_{j\ge1}(M_2,\operatorname{tr}_2),
\tag{3}
\]
such that \(A\) is a MASA in \(M\) and regular in \(R\). It is therefore semiregular in \(N\). If \(N\) is AFD, the construction can have \(R=N\), making \(A\) regular in \(N\).

**Proof.** With the normalized trace \(\tau\) of \(N\), let \(\varphi=\tau E\). Lemma 1.1 makes it faithful and normal. Bimodularity and traciality give
\[
\varphi(ax)=\tau(aE(x))=\tau(E(x)a)=\varphi(xa)
\quad(a\in N,x\in M),
\tag{4}
\]
so \(N\subset M_\varphi\).

Choose a \(\varphi\)-norm dense sequence \((x_j)\) in the unit ball of \(M\). One way to obtain it is to start with a countable weak* dense subset of that ball, available from separability of the predual, and take rational convex combinations. Their GNS vectors are weakly dense and hence norm dense by convex separation.

We construct increasing dyadic matrix factors \(F_n\subset N\), with diagonals \(A_n\), satisfying
\[
A_n\subset A_{n+1},\qquad
\|(T_{A_n}-S_{A_n})(x_j)\|_\varphi<2^{-n}
\quad(j\le n).
\tag{5}
\]
Their embeddings will be tensor embeddings compatible with the diagonals. Start with \(F_0=\mathbb C1\). Suppose \(F_n\cong M_d\), with units \(e_{ij}\), has been chosen. Set \(e=e_{11}\).

The [corner commutant lemma](abelian-pinching-and-relative-commutants.md#lemma-3-1) gives
\[
(eNe)'\cap eMe=\mathbb Ce.
\tag{6}
\]
The corner state is \(\varphi_e=d\,\varphi|_{eMe}\), because \(\varphi(e)=1/d\). Apply the [equal-atom gap theorem](abelian-pinching-and-relative-commutants.md#theorem-6-1) there to the finite set
\[
z_{ij}=e_{1i}x_j e_{i1}\quad
(1\le i\le d,\ 1\le j\le n+1).
\tag{7}
\]
It gives a dyadic diagonal \(B\subset eNe\), of as large a size as needed, whose gap on each \(z_{ij}\) is below \(2^{-(n+1)}\) in \(\varphi_e\)-norm. Complete its equal atoms to dyadic matrix units \(f_{st}\) in \(eNe\). Define the larger full matrix algebra by
\[
E_{(i,s),(j,t)}=e_{i1}f_{st}e_{1j}.
\tag{8}
\]
Multiplication verifies the matrix-unit relations. Summing over \(s\) recovers each old \(e_{ij}\); its diagonal refines the old diagonal.

For any \(x\in M\), only the old diagonal corners survive this new pinching. Transport each of them to \(eMe\) by \(e_{1i},e_{i1}\). Since these matrix units lie in the centralizer, the gap identity is
\[
\|(T_{A_{n+1}}-S_{A_{n+1}})(x)\|_\varphi^2
=\frac1d\sum_{i=1}^d
\|(T_B-S_B)(e_{1i}xe_{i1})\|_{\varphi_e}^2.
\tag{9}
\]
The scalar expectation coefficients are unchanged by this transport: both the numerator and its atom weight acquire the same factor. Thus (7) and (9) prove (5) at the next stage. Choose the new matrix size strictly larger than the old one at every stage.

Put \(A=(\bigcup_n A_n)''\), \(R=(\bigcup_n F_n)''\). The gap projections are contractions, so (5) and density extend their convergence to every \(x\in M\). Theorem 2.1 of the pinching lesson makes \(A\) a MASA in \(M\).

The matrix embeddings in (8) identify \(F_{n+1}\) with \(F_n\otimes G_n\), where \(G_n\) is the propagated first-corner matrix algebra commuting with \(F_n\). Their diagonals have the same tensor form. Each finite diagonal permutation, and every diagonal phase unitary, therefore normalizes every later diagonal and its closure \(A\). These unitaries generate \(F_n\), so
\[
R\subset\mathcal P_N(A).
\tag{10}
\]
The finite-factor increasing-matrix theorem makes \(R\) a factor; its unbounded dyadic sizes and trace-GNS tensor identification give the stated copy of \(R\) in (3). Because \(A\subset R\), any element of \(R'\cap N\) belongs to \(A'\cap N=A\), and then to \(R\cap R'=Z(R)=\mathbb C\). Hence \(Z(\mathcal P_N(A))\subset R'\cap N=\mathbb C\), proving semiregularity. The same normalizers generate \(R\) itself, proving regularity there.

For the AFD clause, take also a \(\tau\)-norm dense sequence \((y_j)\) in the unit ball of \(N\). The finite corner \(eNe\) is AFD by the [finite AFD corner theorem](hyperfinite-finite-factors.md#theorem-5-1). Having chosen the first-corner dyadic matrix algebra with diagonal \(B\), apply the [exact containment lemma](hyperfinite-finite-factors.md#lemma-4-1) inside \(eNe\). Enlarge it to a dyadic matrix algebra \(G\) approximating every entry
\[
e_{1i}y_j e_{k1}\quad(1\le i,k\le d,\ j\le n+1)
\tag{11}
\]
to corner \(2\)-norm error below \(2^{-(n+1)}/\sqrt d\). Choose a diagonal of \(G\) extending \(B\): a unital matrix inclusion splits as the old matrix algebra tensored with its matrix relative commutant. Its gap can only decrease under this diagonal refinement.

Use \(G\) instead of the original corner algebra in (8). The resulting \(F_{n+1}\) still satisfies (5), while entry orthogonality gives
\[
\|y_j-E_{F_{n+1}}(y_j)\|_2^2
=\frac1d\sum_{i,k}
\|e_{1i}y_j e_{k1}-E_G(e_{1i}y_j e_{k1})\|_{2,e}^2
<4^{-(n+1)}.
\tag{12}
\]
The expectations here are trace preserving. Thus \(R\) contains the entire dense sequence and equals \(N\). Its matrix normalizers make \(A\) regular in \(N\). \(\square\)

## 3. Splitting the semifinite case

We use the semifinite factor matrix decomposition: a \(\mathrm{II}_\infty\) factor with separable predual has a finite projection \(e\) and countable matrix units \((e_{ij})\) with \(e_{11}=e\), \(\sum_i e_{ii}=1\), and
\[
N\cong B(\ell^2)\bar\otimes eNe.
\tag{13}
\]
Here \(eNe\) is \(\mathrm{II}_1\). The projection and trace inputs are explicit: choose a finite projection of trace one, take infinitely many orthogonal equivalent copies, and compare their infinite sum with \(1\) by the sigma-finite infinite projection theorem. A partial isometry carrying that sum to \(1\) transports the copies and gives the displayed system.

The same matrix units split the ambient algebra:
\[
M\cong B(\ell^2)\bar\otimes eMe,
\tag{14}
\]
compatibly with (13). For completeness, on a faithful representation the unitary
\[
W:eH\otimes\ell^2\longrightarrow H,\qquad
W(\zeta\otimes\delta_i)=e_{i1}\zeta
\tag{15}
\]
identifies \(M\) with the bounded matrices whose entries \(e_{1i}xe_{j1}\) belong to \(eMe\). Finite coordinate compressions converge strongly and generate the spatial tensor product. Restricting the same argument to \(N\) proves compatibility. This is a matrix decomposition, not a decomposition by classification of factors.

**Theorem 3.1.** Let \(M\) be a factor with separable predual and \(N\subset M\) a semifinite subfactor with \(N'\cap M=\mathbb C\). If a normal conditional expectation \(M\to N\) exists, then \(N\) contains a MASA \(A\) which is maximal abelian in \(M\) and semiregular in \(N\). If \(N\) is AFD, \(A\) can be chosen regular in \(N\).

**Proof.** If \(N\) is type I, choose its finite or countable full matrix units with a minimal first projection \(e\). The corner lemma gives \((eNe)'\cap eMe=\mathbb Ce\); since \(eNe=\mathbb Ce\), this forces \(eMe=\mathbb Ce\). The matrix decomposition then gives \(M=N\). Its atomic diagonal is a MASA, and permutations of its atoms together with diagonal unitaries generate \(N\). Thus it is regular.

If \(N\) is \(\mathrm{II}_1\), Theorem 2.1 applies. Otherwise use (13)–(14). Bimodularity restricts the normal expectation to \(eMe\to eNe\), and (6) gives irreducibility in that corner. Theorem 2.1 provides a MASA \(A_1\subset eNe\) maximal abelian in \(eMe\), and an AFD factor \(R_1\) containing it with \(R_1'\cap eNe=\mathbb C\).

Let \(D\subset B(\ell^2)\) be the atomic diagonal and set
\[
A=D\bar\otimes A_1.
\tag{16}
\]
An operator commuting with \(A\) first commutes with all its coordinate projections, hence is block diagonal. Each diagonal entry commutes with \(A_1\) in \(eMe\), so lies in \(A_1\). The bounded collection of those entries belongs to \(D\bar\otimes A_1\). Thus \(A\) is a MASA in \(M\).

Finite coordinate permutations normalize \(A\), as do the unitaries \(1\otimes v\) for \(v\in\mathcal N_{eNe}(A_1)\). Therefore its normalizer algebra contains
\[
B(\ell^2)\bar\otimes R_1.
\tag{17}
\]
The relative commutant of this factor in \(N\) is
\(1\otimes(R_1'\cap eNe)=\mathbb C\), by the tensor commutation theorem. Its normalizer algebra is consequently a factor, so \(A\) is semiregular.

If \(N\) is AFD, finite-corner permanence makes \(eNe\) AFD. Then the final clause of Theorem 2.1 allows \(R_1=eNe\), and (17) is all of \(N\). This proves regularity. \(\square\)

The finite-corner permanence input for an AFD \(\mathrm{II}_\infty\) factor follows from [AFD-to-injectivity](central-traces-and-afd-finite-algebras.md#theorem-4-1), corner permanence of injectivity, and the [finite injective-factor theorem](unitary-couplings-and-finite-injective-factors.md#theorem-5-1). Its complete proof later in the course supplies the final regularity step. The matrix reduction above uses only the independent projection comparison input; the finite regularity proof in Theorem 2.1 uses the earlier finite corner and containment results.

## 4. MASAs in a state centralizer

**Corollary 4.1.** Let \(M\) be a factor with separable predual and \(\varphi\) a faithful normal state such that
\[
(M_\varphi)'\cap M=\mathbb C.
\tag{18}
\]
Then \(M_\varphi\) contains a MASA which is maximal abelian in \(M\) and semiregular in \(M_\varphi\).

**Proof.** The centralizer has a faithful normal tracial state \(\varphi|_{M_\varphi}\), hence is finite. Its center lies in the relative commutant in (18), so it is a factor. It is fixed by the modular group, so the modular expectation theorem gives a normal \(\varphi\)-preserving expectation onto it. Apply Theorem 3.1, or directly Theorem 2.1 in its type II case. \(\square\)

This corollary keeps the irreducible-centralizer hypothesis. It does not assert that every state centralizer is a factor or contains a MASA of the ambient algebra.

## 5. Exercises with complete solutions

**Exercise 1.** Why does the kernel argument in Lemma 1.1 need normality?

*Solution.* The composed state \(\theta=\psi E\) must be normal to have a support projection with null left ideal \(M(1-p)\). That concrete ideal identifies the right-invariance condition with commutation of \(p\) and \(N\). No such normal support argument is provided for a singular retraction.

**Exercise 2.** Verify the centralizer calculation (4) without assuming \(M\) finite.

*Solution.* For \(a\in N\), expectation bimodularity gives \(E(ax)=aE(x)\) and \(E(xa)=E(x)a\). Applying the normalized trace of \(N\) gives equal scalar values. This is exactly the definition of \(a\in M_\varphi\), irrespective of the type of \(M\).

**Exercise 3.** Multiply the matrix units in (8).

*Solution.* Since \(e_{1j}e_{k1}=\delta_{jk}e\) and \(f_{st}f_{uv}=\delta_{tu}f_{sv}\), the product of \(E_{(i,s),(j,t)}\) and \(E_{(k,u),(l,v)}\) is \(\delta_{jk}\delta_{tu}E_{(i,s),(l,v)}\). Adjoints interchange the index pairs. Their diagonal sum is \(\sum_i e_{i1}(\sum_s f_{ss})e_{1i}=1\).

**Exercise 4.** Explain the normalization \(1/d\) in (9).

*Solution.* The old minimal projection has state value \(1/d\). The normalized corner state is therefore \(\varphi_e=d\varphi\). Transport by \(e_{i1}\) preserves the unnormalized \(\varphi\)-norm because the matrix units are in the centralizer. Each corner squared norm is \(1/d\) times its normalized counterpart; the mutually orthogonal diagonal corners then add.

**Exercise 5.** Why do the old matrix permutations normalize the final diagonal, rather than merely the current finite one?

*Solution.* Each later embedding is obtained by propagating the same first-corner algebra across all old rows. It identifies the new diagonal with the old diagonal tensored with a commuting new diagonal. An old permutation changes only its old coordinate and preserves every later tensor diagonal. Passing to their generated von Neumann algebra proves the final normalization.

**Exercise 6.** Distinguish regularity in \(R\) from semiregularity in \(N\) in Theorem 2.1.

*Solution.* The constructed finite matrix normalizers generate \(R\), so \(A\) is regular there. Inside \(N\), the full normalizer algebra may be larger. It contains \(R\), whose relative commutant in \(N\) is scalar, and therefore has scalar center. That proves it is a factor, which is the semiregularity assertion; equality with \(N\) is not inferred.

**Exercise 7.** Derive \(R'\cap N=\mathbb C\) from \(A\subset R\) and the MASA property.

*Solution.* An element commuting with \(R\) commutes with \(A\), hence belongs to \(A\) by maximal abelianness in \(N\). Since \(A\subset R\), it also belongs to \(R\cap R'=Z(R)\). This center is scalar.

**Exercise 8.** Why does enlarging the first-corner matrix algebra in the AFD clause preserve the ambient gap estimate?

*Solution.* Choose a diagonal of the enlarged algebra containing the earlier diagonal \(B\). Its scalar expectation projection increases and its commutant expectation projection decreases. The resulting gap projection is below the old one, by (5) of the pinching lesson. Every prescribed gap norm therefore remains within its bound.

**Exercise 9.** Check the sum and normalization in (12).

*Solution.* There are \(d^2\) entries and the ambient squared norm equals \(1/d\) times their normalized corner squared norms. If each error is below \(\alpha/\sqrt d\), their total is below \(d^{-1}d^2(\alpha^2/d)=\alpha^2\). Set \(\alpha=2^{-(n+1)}\).

**Exercise 10.** Prove directly that \(D\bar\otimes A_1\) in (16) is maximal abelian.

*Solution.* Commutation with every coordinate projection \(p_i\otimes1\) makes an operator block diagonal. Its \(i\)-th diagonal entry lies in \(eMe\) and commutes with \(A_1\), hence belongs to \(A_1\). A uniformly bounded sequence of entries in \(A_1\) is precisely an element of the product diagonal algebra \(D\bar\otimes A_1\).

**Exercise 11.** Show that the infinite atomic diagonal of \(B(\ell^2)\) is regular.

*Solution.* Its projections \(p_i\) belong to the normalizer algebra, since every diagonal unitary normalizes it and these generate the diagonal. For a finite permutation unitary \(u\) sending basis \(j\) to basis \(i\), \(p_iup_j=e_{ij}\). Thus every finite matrix unit belongs to the normalizer algebra. Finite matrix compressions converge strongly to each bounded operator, so it is all of \(B(\ell^2)\).

**Exercise 12.** Explain why (18) makes the centralizer a finite factor.

*Solution.* The restricted state is faithful, normal and tracial, so the centralizer is finite. Every central element of the centralizer commutes with that algebra inside \(M\), hence belongs to the scalar relative commutant in (18). Its center is therefore scalar. Neither conclusion needs the ambient state to be tracial.

## Reading and prerequisites

Sorin Popa, [On a problem of R. V. Kadison on maximal abelian \*-subalgebras in factors](https://imar.ro/~increst/1981/41_1981.pdf), INCREST preprint 41/1981, May 1981, second version; the journal article appeared in *Inventiones Mathematicae* 65 (1981), 269–281, DOI [10.1007/BF01389015](https://doi.org/10.1007/BF01389015). Theorem 1 and its construction in Section 2, printed pp.10–13, produce compatible matrix factors and a diagonal MASA for a separable finite tracial ambient algebra. Corollary 3.1, printed p.14, passes from the finite case to a semifinite ambient factor by common matrix coordinates. Here the finite construction instead uses the state \(\tau E\), so the ambient algebra can be nontracial, and the semifinite reduction is performed on the expected subfactor itself. The faithfulness argument, its normal-state support calculation, both type I cases and every matrix transport are supplied explicitly.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft. Section 11.2, printed pp.185–188, provides the dyadic approximation and trace-GNS uniqueness method. The AFD clause here uses the earlier independently proved finite corner and exact containment lemmas. The final AFD \(\mathrm{II}_\infty\) clause also uses AFD-to-injectivity, permanence of injectivity under corners and the later finite injective-factor theorem, as detailed above. General modular expectations, state centralizers, projection comparison and spatial tensor commutation remain declared foundations whose exact accessible transitive verification is pending.
