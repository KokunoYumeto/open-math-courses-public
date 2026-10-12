# Strong stability and tensor absorption

*Written by GPT-6.1 Sol (OpenAI), Ultra. New original exposition: CC0-1.0 to the extent of rights held. Earlier programme and human-source notices retain their own terms.*

The useful distinction is between an exact finite matrix coordinate and a limit of such coordinates. A finite matrix can always be removed from the central sequence algebra. An infinite string splits off only after a summability condition makes its tail averages tend to the identity. We construct the finite coordinates first, prove the finite-head removal, then treat the two summability hypotheses separately before building the commuting string needed for absorption.

The complete [SS0–4 inputs](../components/strong-stability-matrix-and-product-inputs.md) supply the finite sign/permutation average, the numerical commutator bound, whole-domain normality for trace-preserving positive maps, the entire variable-size tracial product and the normal GNS spatial splitting. The [quotient and exact-lift lesson](central-sequence-algebras-and-exact-lifts.md) supplies \(C_\omega,J_\omega,M_\omega,\pi_\omega,\tau_\omega\) and the whole exact matrix-lifting theorem. The [fullness and corner lesson](fullness-hypercentrality-and-ultrafilter-corners.md) treats all ordinary and some/every-ultrafilter alternatives, without replacing type \(\mathrm{II}_1\) by factoriality. A bounded centralizing sequence means
\(\|[x_n,\psi]\|\to0\) for every \(\psi\in M_*\), where
\([x,\psi](z)=\psi(zx)-\psi(xz)\); the ultrafilter version uses that limit instead.

<a id="1-stable-and-strongly-stable-factors"></a>

## The absorption question

For a nonzero factor \(M\), stability means a normal isomorphism \(M\cong M\bar\otimes M_p(\mathbb C)\) for every positive finite integer \(p\). Strong stability means
\[
M\cong M\bar\otimes R,
\tag{1}
\]
where \(R\) is the separable AFD \(\mathrm{II}_1\) factor. SS2 proves both \(M_p\bar\otimes R\cong R\) and \(R\bar\otimes R\cong R\) on their whole normal closures. In the second case, the two dyadic strings are interleaved by an inner-product-preserving map on all local trace vectors, extended to a Hilbert unitary. In the first, the complete variable product with sizes \(p,2,2,\ldots\) is AFD type \(\mathrm{II}_1\), and AF5 applies. Consequently strong stability implies stability: associate the three tensor legs, absorb the finite matrix in the \(R\) leg and use (1) twice. The associativity and flip maps are the Hilbert unitaries defined on elementary tensors, whose inner products and dense spans give their full extensions.

<a id="2-averaging-a-finite-matrix-factor"></a>

## Exact finite coordinates before taking any limit

Let \(D\subseteq M\) be a unital full matrix algebra with matrix units \(e_{ij}\), \(1\leq i,j\leq p\), and put \(D^c=D'\cap M\). No factor assumption on \(M\) is needed here. On a faithful normal concrete representation the unitary
\[
\delta_i\otimes\xi\longmapsto e_{i1}\xi,\qquad \xi\in e_{11}H,
\]
identifies \(M\) with \(M_p(e_{11}Me_{11})\). Orthogonality of the matrix-unit ranges proves isometry, and their unit sum proves surjectivity. Commuting with every scalar matrix unit forces a block matrix to be a single repeated diagonal entry. Amplifying that corner entry therefore identifies \(D^c\) with the corner. In the original algebra these coordinates are
\[
x=\sum_{i,j}e_{ij}a_{ij},\qquad
a_{ij}=\sum_k e_{ki}xe_{jk}\in D^c,\qquad
\|a_{ij}\|\leq\|x\|.
\tag{2}
\]
The bound follows from the norm of the compressed entry \(e_{1i}xe_{j1}\) and its diagonal amplification. CP's finite vector-coordinate tests prove normality of both maps on their entire domains. SS0 supplies the complete multiplication and adjoint check, hence the normal spatial identification \(M=D\bar\otimes D^c\).

**Exercise 1.** Evaluate the coefficient in (2) when \(x=e_{\ell m}a\), \(a\in D^c\), and verify reassembly of \(x\).

*Solution.* Commuting \(a\) past the matrix units and multiplying their indices gives
\[
\sum_k e_{ki}(e_{\ell m}a)e_{jk}
=\delta_{i\ell}\delta_{mj}\sum_k e_{kk}a
=\delta_{i\ell}\delta_{mj}a.
\]
There is just one surviving coefficient. The sum of \(e_{ij}\) times these coefficients is \(e_{\ell m}a\). For arbitrary \(x\), direct multiplication in the double sum gives \(\sum_{i,j}e_{ii}xe_{jj}=x\). Thus coefficient recovery and reconstruction agree on every entry, as required.

The conditional expectation that removes this matrix is
\[
E_D(x)=\frac1p\sum_{i,j}e_{ij}xe_{ji}.
\tag{3}
\]
It is normal, unital and completely positive, fixes \(D^c\), has exactly that range and is \(D^c\)-bimodular. To see faithfulness, if \(x\geq0\) and (3) is zero, every positive summand is zero; in particular \(e_{ii}xe_{ii}=0\). Hence \(x^{1/2}e_{ii}=0\) for every \(i\), whose unit sum forces \(x=0\).

For an explicit finite unitary average, take all sign diagonals
\(v_\varepsilon=\sum_i\varepsilon_i e_{ii}\), \(\varepsilon_i\in\{-1,1\}\), and all permutation matrices \(u_\sigma=\sum_i e_{\sigma(i),i}\). Then
\[
E_D=\frac1{2^p p!}\sum_{\varepsilon,\sigma}
\operatorname{Ad}(u_\sigma v_\varepsilon).
\tag{6}
\]
The sign average cancels each off-diagonal entry. The permutation average sends each surviving diagonal entry to each position equally, giving its normalized scalar matrix trace. This is (3), including \(p=1\). SS0 proves the finite formula and every positivity, range and continuity assertion; no Haar integration is needed.

**Lemma 2.1.** For every normal functional \(\psi\),
\[
\|\psi-\psi\circ E_D\|
\le p^{3/2}\max_{i,j}\|[e_{ij},\psi]\|.
\tag{4}
\]
If \(M\) has a faithful normal tracial state, then
\[
\|x-E_D(x)\|_2
\le p^{3/2}\max_{i,j}\|[e_{ij},x]\|_2.
\tag{5}
\]

**Proof.** Write a unitary of \(D\) as \(u=\sum_{i,j}\lambda_{ij}e_{ij}\). Summing the \(p\) diagonal entries of its scalar identity \(u^*u=1\) gives \(\sum_{i,j}|\lambda_{ij}|^2=p\). Consequently
\[
\|[u,\psi]\|
\leq\sqrt p\left(\sum_{i,j}\|[e_{ij},\psi]\|^2\right)^{1/2}
\leq p^{3/2}\max_{i,j}\|[e_{ij},\psi]\|.
\tag{7}
\]
The identity \((\psi-\psi\operatorname{Ad}u)(x)=[u,\psi](xu^*)\) makes these functional norms equal: multiplication by \(u^*\) bijects the unit ball. Average this bound over the exact finite list in (6), using the triangle inequality. This proves (4). In the tracial setting, the same coefficient calculation gives the same bound for \(\|[u,x]\|_2\); the trace law makes right multiplication by \(u^*\) a \(2\)-norm isometry, so \(\|uxu^*-x\|_2=\|[u,x]\|_2\). The finite triangle inequality now proves (5). All finite matrix sizes are covered. \(\square\)

**Exercise 2.** Obtain the factor \(p^{3/2}\) in Lemma 2.1 from the scalar coefficients of a unitary matrix.

*Solution.* The equation \(u^*u=1_p\) says that each of its \(p\) columns has squared length one. Thus the square-sum of all coefficients is \(p\), giving the first factor \(\sqrt p\) in scalar Schwarz. The \(p^2\) commutator norms have square-sum at most \(p^2\) times the maximum norm squared, giving the second factor \(p\). Their product is \(\sqrt p\,p=p^{3/2}\). This calculation applies to the functional norms and to the trace \(2\)-norms separately.

<a id="4-removing-a-fixed-finite-matrix-factor"></a>

## A finite head leaves the central sequence algebra unchanged

**Lemma 4.1.** If \(M\) is a factor with separable predual and \(D\subset M\) is a unital finite matrix factor, the inclusion \(D^c\subset M\) induces a trace-preserving normal isomorphism
\[
(D^c)_\omega\cong M_\omega.
\tag{21}
\]
Every ordinary centralizing sequence in \(M\) is strong*-equivalent to an ordinary centralizing sequence in \(D^c\).

**Proof.** First record that \(B=D^c\) is a factor with separable predual. In (2), a central matrix must be a repeated central entry of \(B\); hence \(Z(M)=1_p\otimes Z(B)\), and factoriality of \(M\) gives \(Z(B)=\mathbb C\). The map \(B_*\to M_*\), \(\eta\mapsto\eta E_D\), is isometric: contraction gives one inequality and testing on the unit ball of \(B\), which \(E_D\) fixes, gives the other. Its closed image in the separable \(M_*\) is separable. A faithful normal state of \(M\) restricts faithfully and normally to \(B\).

For a bounded centralizing sequence, ordinary or along \(\omega\), the completed quotient lesson proves centrality against every fixed operator. Formula (3) gives
\[
E_D(x_n)-x_n=\frac1p\sum_{i,j}[e_{ij},x_n]e_{ji}\longrightarrow0
\quad\hbox{strong*}.
\tag{22}
\]
Each summand has a fixed right multiplier, so bounded strong* convergence is preserved. The full strong*-perturbation estimate in that lesson makes \(E_D(x_n)\) centralizing in \(M\).

For a bounded sequence \(x_n\in B\), centralizing in \(B\) is equivalent to centralizing in \(M\). One direction uses a normal \(\eta\in B_*\) extended to \(\eta E_D\): on \(z\in B\) its commutator is exactly \([x_n,\eta](z)\), so the \(B_*\) norm is bounded by the \(M_*\) norm. For the reverse direction fix \(\psi\in M_*\) and the normal functionals \(\eta_{ij}(a)=\psi(e_{ij}a)\) on \(B\). For \(\|z\|\leq1\), expand (2), whose coefficients all have norm at most one. Since \(x_n\) commutes with every \(e_{ij}\),
\[
|[x_n,\psi](z)|\leq\sum_{i,j}\|[x_n,\eta_{ij}]\|.
\tag{23}
\]
The finitely many tests tend to zero at the limit being used, proving the assertion in both cases.

NT2 characterizes bounded intrinsic strong* convergence by a faithful normal state's two square seminorms. On \(B\) these are precisely the restricted state's seminorms. Thus inclusion preserves and reflects \(J_\omega\). It preserves the scalar ultraweak limits defining the quotient trace: restricting any normal functional of \(M\) gives the same scalar test on \(B\). The induced map is an injective star homomorphism, and (22) makes it surjective. The completed quotient construction gives faithful normal normalized traces on both whole von Neumann algebras, without asserting a scalar center. Their equality under this isomorphism allows SS1 to prove whole-domain ultraweak continuity of the map and its inverse. This proves the normal isomorphism (21), and the same ordinary perturbation proves the last sentence. \(\square\)

<a id="3-summability-produces-a-spatial-tensor-factor"></a>

## Tail maps distinguish a finite head from an infinite tensor factor

For both summability results take \(M\) with separable predual, commuting unital \(D_\nu\cong M_{p_\nu}\), \(p_\nu\geq1\), and infinitely many \(p_\nu\geq2\). The algebra need not be a factor. Write \(E_\nu=E_{D_\nu}\), \(R_0=\bigvee_\nu D_\nu\), \(B=R_0'\cap M\) and
\[
F_{m,N}=E_mE_{m+1}\cdots E_N,\qquad
N_m=\bigcap_{\nu\geq m}(D_\nu'\cap M).
\tag{11}
\]
The sign/permutation unitaries in different \(D_\nu\)'s commute. Therefore their conjugations and averages commute. A finite composition has range the intersection of its ranges: applying any constituent leaves the product fixed, and every element in the intersection is fixed by every constituent. It is normal, unital, completely positive and faithful. Each constituent is bimodular over the intersection, as is the composition.

The finite head \(A_{m-1}=\bigvee_{\nu<m}D_\nu\) is a full matrix algebra of size \(\prod_{\nu<m}p_\nu\), with \(A_0=\mathbb C1\). Multiplication of its commuting tensor matrix units is a unital representation of that finite full matrix algebra. It is injective: any nonzero ideal contains a nonzero entry; multiplication on its left and right by scalar matrix units extracts every matrix unit and then their unit sum. Thus it has zero kernel. Applying (2) to the head gives the exact identity
\[
N_m=A_{m-1}\vee B.
\tag{14}
\]
Indeed, the coefficients of \(x\in N_m\) commute with the head by (2), and with the tail because each multiplier in that coefficient formula belongs to the head. They belong to \(B\). Conversely every head element and every \(B\) element commutes with the whole tail. Their finite-coordinate algebra is already the entire right side of (14). In particular, any normal tail maps \(T_m\) onto \(N_m\) with \(T_m(x)\to x\) ultraweakly will prove \(M=R_0\vee B\).

**Theorem 3.1.** Let \(M\) have separable predual, without requiring it to be a factor. Let \(D_\nu\subset M\) be mutually commuting unital matrix factors of sizes \(p_\nu\), with infinitely many \(p_\nu\ge2\). Suppose that for a norm-dense sequence of normal states \(\psi_j\),
\[
\sum_{\nu\ge1}\|\psi_j-\psi_j\circ E_{D_\nu}\|<\infty
\qquad\text{for every }j.
\tag{8}
\]
Then
\[
R_0=\bigvee_{\nu\ge1}D_\nu\cong R,\qquad
M\cong R_0\bar\otimes R_0^c,
\quad R_0^c=R_0'\cap M.
\tag{9}
\]

**Proof.** Commutativity lets the newest average be placed next to the tested normal state in the predual. Telescoping and the predual contractions give, for \(L>N\geq m\),
\[
\|\psi_jF_{m,L}-\psi_jF_{m,N}\|
\leq\sum_{\nu=N+1}^{L}\|\psi_j-\psi_jE_\nu\|.
\tag{10}
\]
Every positive normal functional is its norm times a normal state, and NT1 decomposes every normal functional into four positive ones. The span of the given dense states is therefore norm dense in \(M_*\). Cauchy convergence on that span follows termwise from (8); replacing a general functional by a span approximation incurs at most twice its norm error, since both compositions are contractions. Consequently \(P_m\psi=\lim_N\psi F_{m,N}\) exists in the complete \(M_*\) for every \(\psi\), linearly and contractively.

Use CP's identification \(M=(M_*)^*\) to define \(T_m=P_m^*\). Its predual is \(P_m\), so it is normal on its entire domain. For any fixed positive matrix over \(M\), all finite images are positive; entrywise ultraweak convergence gives positivity of the limit matrix by normal vector quadratic tests. Hence \(T_m\) is unital completely positive. The equality \(E_\nu T_m=T_m\) for \(\nu\geq m\) follows from the commuting finite products and normality of \(E_\nu\). It gives range in \(N_m\), while every element of \(N_m\) is fixed by the finite products and by \(T_m\). Fixed multiplication is normal, so their bimodule identities also pass to the limit. Thus it is the claimed conditional expectation.

The same telescope starting at the identity gives
\[
\|\psi_j-\psi_jT_m\|\leq
\sum_{\nu\geq m}\|\psi_j-\psi_jE_\nu\|\longrightarrow0.
\tag{12}
\]
Contraction and norm density extend this to every \(\psi\in M_*\); thus \(T_m(x)\to x\) ultraweakly for each \(x\). Let \(E=T_1\). For \(x\geq0\) with \(E(x)=0\), the exact tail identity is
\[
F_{1,m-1}(T_m(x))=E(x)=0.
\tag{13}
\]
The finite head is faithful and \(T_m(x)\geq0\), so \(T_m(x)=0\). The just-proved tail convergence gives \(x=0\). Therefore the infinite expectation onto \(B\) is faithful.

Take the faithful normal state \(\varphi=\sum_{j\geq1}2^{-j}\psi_j\) from SS3 and set \(\rho=\varphi E\). Norm completeness makes \(\varphi\) normal, and density of the states detects every nonzero positive element, proving faithfulness. Faithfulness of \(E\) then makes \(\rho\) faithful normal. On every finite head the first finitely many averages remove all its matrix legs to their normalized product trace; all subsequent averages fix the scalar. Thus \(\tau_0=\rho|_{R_0}\) is the local product trace. The trace identity extends twice from the local star algebra to its whole von Neumann closure, using normality of fixed-multiplier functionals and BD. It is faithful and normal there.

The finite local trace-vector map from SS2 to the trace GNS space of \(R_0\) preserves every inner product. Local vectors are dense in the latter by BD and cyclicity, so it extends to a unitary. It intertwines every local left action and their whole closures. STC/ST1–2 applies to the already faithful normal \(\tau_0\) and identifies the whole \(R_0\) normally with SS2's complete variable matrix product. Infinitely many sizes at least two give its type \(\mathrm{II}_1\), separable-predual AFD conclusion; AF5 yields \(R_0\cong R\).

Equations (14) and (12) imply \(M=R_0\vee B\). Moreover bimodularity and the finite head average give, first for local \(a\) and then for every \(a\in R_0\) by normality,
\[
\rho(ab)=\tau_0(a)\varphi(b),\qquad b\in B.
\tag{16}
\]
All three states are faithful normal. SS3 constructs the whole product Hilbert space and the onto unitary
\[
a\Omega_{\tau_0}\otimes b\Omega_{\varphi|_B}
\longmapsto ab\Omega_\rho.
\tag{17}
\]
Its product inner products and generation prove surjectivity; faithful normal GNS identifications and their normal inverses make multiplication a whole normal spatial isomorphism. This is (9), with no extra factoriality assumption on \(M\). \(\square\)

**Exercise 3.** Why do the dense-state summability tests in Theorem 3.1 imply the Cauchy property for every normal functional?

*Solution.* NT1 gives four positive normal functionals whose linear combination is a given \(\psi\). Normalize each nonzero term to a state, and approximate those states by the specified dense family. This makes finite linear combinations of that family norm dense in \(M_*\). For \(\eta=\sum_{r=1}^{s}c_r\psi_{j_r}\), (10) bounds the Cauchy difference by the finite sum of \(|c_r|\) times the corresponding summable tails. For arbitrary \(\psi\), the difference of two predual contractions acting on \(\psi-\eta\) has norm at most \(2\|\psi-\eta\|\). Given an error target, first choose \(\eta\) to make this error small, and then choose the common tail threshold for its finitely many terms. This proves Cauchy convergence for every \(\psi\), rather than a summability claim that need not hold for every \(\psi\).

**Exercise 4.** Establish faithfulness of the infinite average from its tail maps, and explain the extra work needed beyond faithfulness of its finite approximants.

*Solution.* At \(x\geq0\) with \(E(x)=0\), (13) applies the faithful finite head \(F_{1,m-1}\) to the positive \(T_m(x)\). Thus \(T_m(x)=0\) for every \(m\). Equation (12) then gives \(x=0\) through the ultraweak limit. A limit of faithful maps need not be faithful: on \(\mathbb C^2\), the faithful positive unital maps \((a,b)\mapsto(a,\varepsilon a+(1-\varepsilon)b)\), \(0<\varepsilon<1\), approach the map \((a,b)\mapsto(a,a)\) as \(\varepsilon\uparrow1\). The positive nonzero \((0,1)\) is killed by the limit. The tail convergence in (12) is what rules out such loss here.

**Exercise 5.** Explain why the type conclusion \(R_0\cong R\) requires infinitely many nontrivial matrix factors.

*Solution.* If every \(D_\nu=\mathbb C1\), then \(E_\nu\) is the identity and every defect in (8) is zero, yet \(R_0=\mathbb C1\). If only finitely many sizes exceed one, multiplying their matrix units gives one finite full matrix algebra, unchanged by all later scalar legs. If infinitely many sizes are at least two, the finite head sizes \(d_n\) are unbounded. In SS2 a purported minimal projection of trace \(\alpha>0\) would contain, by full finite-factor comparison, a nonzero copy of a head diagonal cell of trace \(1/d_n<\alpha\), contradicting minimality. The complete product is consequently type \(\mathrm{II}_1\), AFD and separable, hence \(R\). Summability alone does not distinguish these three cases.

**Exercise 6.** Check the GNS map (17) on two product vectors and on finite sums.

*Solution.* The image inner product of \(a\Omega_{\tau_0}\otimes b\Omega_\varphi\) and \(a'\Omega_{\tau_0}\otimes b'\Omega_\varphi\) is
\[
\rho((ab)^*a'b')=\rho(a^*a'b^*b')
=\tau_0(a^*a')\varphi(b^*b').
\]
Commutation justifies the first rearrangement; (16) gives the final product. That is precisely the tensor inner product. Expanding both finite sums gives equality of every cross term and hence of their squared norms; null-vector relations are preserved. SS3 supplies the complete Hilbert tensor construction and the extension. The generation argument proves that this isometry is onto, a separate step from equality of inner products.

## The independent trace-norm route

**Theorem 3.2.** If \(M\) instead has a faithful normal tracial state \(\tau\), the same tensor decomposition follows when
\[
\sum_{\nu\ge1}\|x_j-E_\nu(x_j)\|_{2,\tau}<\infty
\tag{18}
\]
for a \(2\)-norm dense sequence in its unit ball. This conclusion also retains nonfactor algebras.

**Proof.** The setting, sizes and infinitely-many-nontrivial condition are those specified above; \(M\) still need not be a factor. Each finite \(E_\nu\) preserves \(\tau\) by its multiplier formula and the trace law. Its unital completely positive Schwarz inequality and trace preservation make it a \(2\)-norm contraction. For \(L>N\geq m\), move the newest average next to \(x_j\) and telescope:
\[
\|F_{m,L}(x_j)-F_{m,N}(x_j)\|_2
\leq\sum_{\nu=N+1}^L\|x_j-E_\nu(x_j)\|_2.
\tag{19}
\]
On the unit ball, replacing \(x\) by a dense \(x_j\) adds at most \(2\|x-x_j\|_2\). Hence the finite products are trace-Cauchy at every \(x\) in that ball, and scaling covers all \(M\). Their uniform operator bound is \(\|x\|\). SS1 proves completeness inside exactly that bounded operator ball, so \(T_m(x)=\lim_N F_{m,N}(x)\) lies in \(M\).

Linearity and unitality pass to this limit. NT2 makes the bounded convergence strong*; testing vector quadratic forms of finite matrices proves complete positivity of the entrywise limit. Scalar Schwarz gives \(|\tau(y)|\leq\|y\|_2\), so \(\tau T_m=\tau\). SS1's domination and norm-dense predual construction now proves whole-domain ultraweak continuity of \(T_m\), including on unbounded nets. This is stronger than a continuity statement merely on the unit ball.

The finite products commute with each \(E_\nu\), and \(E_\nu\) is a trace contraction, so \(E_\nu T_m=T_m\) for every \(\nu\geq m\). Conversely elements of \(N_m\) are fixed. Fixed multiplication is bounded in trace norm on either side by the multiplier's operator norm, so the bimodule identities pass as well. Thus \(T_m\) is a normal conditional expectation onto \(N_m\). The summable tails in (18), followed by unit-ball density and scaling, give \(T_m(x)\to x\) in trace norm. Bounded trace convergence is intrinsic strong*, hence ultraweak by CP. Identity (14) again yields \(M=R_0\vee B\).

For completeness the order check underlying normality is also explicit. If \(0\leq x_i\uparrow x\), positivity gives \(y=\sup_iT_m(x_i)\leq T_m(x)\). Such a supremum lies in the von Neumann algebra: the increasing bounded positive operators converge strongly to their quadratic-form supremum. Normality of the already given \(\tau\) and trace preservation imply
\[
\tau(T_m(x)-y)=\tau(x)-\lim_i\tau(x_i)=0,
\tag{20}
\]
and faithfulness gives equality. SS1 separately proves that these maps are normal for the entire ultraweak topology, so no unproved equivalence between order and topological normality is used here.

On each finite head \(A_n\), applying its finitely many trace-preserving averages gives
\(\tau(ab)=\operatorname{tr}_{A_n}(a)\tau(b)\) for \(b\in B\). Normality in \(a\) extends this to \(R_0\). Its faithful normal restricted trace identifies the whole \(R_0\) with SS2's product, by the local-vector unitary and faithful normal GNS inverse used above. Thus \(R_0\cong R\). Finally SS3 applies to \(\tau,\tau|_{R_0},\tau|_B\) and the proved generation, yielding the normal spatial isomorphism (9). This completes the trace-norm proof independently of the normal-functional Cauchy hypothesis. \(\square\)

**Exercise 7.** Show why a positive trace-preserving limit map in the finite-trace argument is normal.

*Solution.* Let \(T\) be that bounded positive map and \(0\leq x_i\uparrow x\). Positivity gives the increasing bounded family \(T(x_i)\), with supremum \(y\leq T(x)\). The normal faithful trace satisfies
\[
\tau(y)=\lim_i\tau(T(x_i))
=\lim_i\tau(x_i)=\tau(x)=\tau(T(x)).
\]
The positive \(T(x)-y\) must therefore vanish. This verifies preservation of all increasing positive suprema. For the full ultraweak assertion, SS1 proves more directly that every normal functional composed with \(T\) stays normal: the positive tests \(\rho_b(z)=\tau(b^*zb)\) satisfy \(\rho_bT\leq\|b\|^2\tau\), their compositions are normal by the complete trace-domination proof, and their span is predual norm dense. Approximation and closedness of the predual prove the claim for every test. Thus the original order calculation and whole-domain normality are both justified.

<a id="5-constructing-commuting-matrix-pieces"></a>

## From a quotient matrix to an ordinary commuting string

**Theorem 5.1.** For a factor \(M\) with separable predual, the following are equivalent:

1. \(M\) is strongly stable.
2. \(M_\omega\) is noncommutative for some free ultrafilter.
3. \(M_\omega\) is noncommutative for every free ultrafilter.
4. \(M_\omega\) is type \(\mathrm{II}_1\) for some, equivalently every, free ultrafilter.
5. \(C(M)\ne H(M)\).
6. \(M\) has an ordinary centralizing sequence of mutually commuting unital two-by-two matrix unit systems.

**Proof.** The completed fullness/hypercentrality and noncommutative-corner results equate statements 2–5 for every factor with separable predual. In particular their type \(\mathrm{II}_1\) conclusion retains the entire center. We prove the implications involving 1 and 6 here.

Assume 1 and write \(M\cong N\bar\otimes R\), with \(N=M\). In the dyadic model of \(R\), successive matrix legs supply unital two-by-two systems \(e_{ij}(n)\), commuting exactly across distinct \(n\). FG2 and the centrality criterion prove ordinary centralizing of each entry sequence in \(R\). They remain centralizing as \(1\otimes e_{ij}(n)\) in the product.

Here are the complete predual tests for this last assertion. In faithful normal representations CP writes any normal functional of the product as a summable vector-pair series. Truncate it, then approximate each vector by finite elementary tensor sums; the estimate for changing a vector pairing on the operator unit ball bounds the error by the relevant vector norm products. The resulting functionals are finite sums of elementary \(\eta\otimes\zeta\). Their norms satisfy \(\|\eta\otimes\zeta\|\leq\|\eta\|\|\zeta\|\): take trace-class extensions of each functional to its represented \(B(H)\), with norms within any prescribed positive error of the CP predual quotient norms, form their tensor trace-class extension using their summable vector-pair series, and let the errors decrease to zero. The product pairing has the displayed norm bound. For such a test,
\[
[1\otimes e_{ij}(n),\eta\otimes\zeta]
=\eta\otimes[e_{ij}(n),\zeta],
\]
whose norm tends to zero. The commutator with a norm error \(\chi\) is bounded by \(2\|e_{ij}(n)\|\|\chi\|\leq2\|\chi\|\), so density proves every normal test. The normal isomorphism and its predual transport this string to \(M\), giving 6.

Assume 6. There is a norm-dense sequence \((\psi_k)\) of normal states: separability of \(M_*\) gives a countable base in its norm metric, and choosing a state in each basic ball that meets the state space gives such a sequence. Choose strictly increasing original coordinates for the matrix systems, with their relabelled entries satisfying
\[
\max_{i,j}\|[e_{ij}(n),\psi_k]\|\leq2^{-n}
\qquad(k\leq n).
\tag{24}
\]
The finitely many tests hold eventually by ordinary centralizing, so each choice can exceed the previous index. Exact mutual commutation survives. Lemma 2.1 bounds the later defect at fixed \(k\) by \(2^{3/2}2^{-n}\). Earlier defects are bounded by \(2\|\psi_k\|=2\), and there are finitely many. Theorem 3.1 consequently applies, giving \(M\cong R\bar\otimes B\). Associating and flipping the Hilbert tensor legs and using SS2's whole normal \(R\bar\otimes R\cong R\) gives
\[
M\bar\otimes R
\cong B\bar\otimes R\bar\otimes R
\cong B\bar\otimes R
\cong M.
\tag{25}
\]
This proves 1.

Finally assume 4 and fix a free \(\omega\) with \(M_\omega\) type \(\mathrm{II}_1\). FH1's full-center halving constructs complementary equivalent projections and hence a unital \(M_2\) system in this finite algebra; it requires neither a scalar center nor separable predual for \(M_\omega\). At the first step, the whole exact-lifting theorem gives a centralizing exact coordinate system in \(M\), with support exactly \(1\) at every coordinate. Its finitely many tests are small on an \(\omega\)-large set. Select one coordinate for (24).

Suppose \(D_1,\ldots,D_{n-1}\) have been selected and commute. Their unital tensor matrix units give the finite full head \(A_{n-1}\) by the finite simplicity argument above. Lemma 4.1 applies to its factor relative commutant \(B_{n-1}=A_{n-1}'\cap M\), with separable predual as proved there, and gives the normal trace-preserving quotient isomorphism
\((B_{n-1})_\omega\cong M_\omega\).
Transfer the unital quotient \(M_2\) system through that isomorphism. The exact-lift theorem inside \(B_{n-1}\) gives unital exact coordinate systems in this algebra, centralizing there. Equation (23) makes them centralizing in \(M\) as well. The intersection of the finitely many \(\omega\)-large test sets for \(k\leq n\) and all four entries is large, hence nonempty; select a coordinate for (24). All its entries already lie in the exact \(B_{n-1}\), so they commute with the entire earlier head. No approximate commutation is being promoted to equality.

Induction gives the required mutually commuting string. For each fixed \(\psi_k\) the ordinary bounds tend to zero. The dense-state span and the commutator bound \(2\|\psi-\eta\|\) extend this to every normal functional. Thus the constructed entry sequences are ordinary centralizing, proving 6. Together with the already established equivalences this proves all six statements. \(\square\)

**Exercise 9.** In this induction, why can the next matrix factor lie in the exact relative commutant even though the centrality information is asymptotic?

*Solution.* Fix the previously selected finite head. Lemma 4.1 transfers an exact unital matrix system of \(M_\omega\) into the quotient of its exact factor relative commutant. The complete exact-lifting theorem is applied to that relative commutant itself, so all lifted coordinate entries belong to it before any coordinate is selected, and their diagonal sum is \(1\). Equation (23) gives their asymptotic normal-functional tests in \(M\). Choosing a coordinate from the finite intersection of the large test sets preserves every exact algebraic relation and exact membership. Hence the errors control the centralizing tests, while membership gives exact commutation with the entire earlier head.

**Exercise 8.** Verify the summability condition (8) for a fixed \(\psi_k\) from (24).

*Solution.* For \(n\geq k\), Lemma 2.1 at size two bounds the \(n\)-th term by \(2^{3/2}2^{-n}\), whose tail sum is finite. At each of the finitely many \(n<k\), the norm of the defect is at most \(\|\psi_k\|+\|\psi_kE_n\|\leq2\), since \(\psi_k\) is a state and \(E_n\) a predual contraction. Adding the finite initial sum to the geometric tail proves (8) for that \(k\). This argument does not require a uniform threshold for all normal states.

The same argument works for a fixed size \(p\geq2\) in place of two. Use \(p^{3/2}\) in Lemma 2.1 and SS2's variable product with constant size \(p\). A commuting centralizing string then gives strong stability. At \(p=1\) the matrix units are just \(1\), all defects vanish, and SS2's product is scalar, so this size gives no absorption information.

<a id="6-exercises-with-complete-solutions"></a>

## A boundary example for stability

**Exercise 10.** Give a stable factor that is not strongly stable.

*Solution.* Retain the full example \(M=B(\ell^2(\mathbb N))\). For each positive finite \(p\), every operator on the finite direct sum of \(p\) copies of this Hilbert space is its finite matrix of bounded operators. Thus
\[
B(\ell^2)\bar\otimes M_p
=B(\ell^2\otimes\mathbb C^p).
\]
The basis bijection \((n,j)\mapsto pn+j\), \(n\geq0\), \(0\leq j<p\), extends to a Hilbert unitary from \(\ell^2\otimes\mathbb C^p\) to \(\ell^2\); its conjugation is normal with normal inverse. This proves stability for every \(p\). SS4 checks factoriality, separable predual and an explicit faithful normal state. CQ6 proves that its central sequence algebra is \(\mathbb C\) for every free ultrafilter, using all rank-one tests and the scalar ultraweak limit. Theorem 5.1 consequently excludes strong stability. No different example or finite-only version has replaced the given infinite type I factor.

<a id="references"></a>

## Complete freely accessible proofs and the historical comparison

The full current arguments use [SS0–4](../components/strong-stability-matrix-and-product-inputs.md), the completed finite comparison and trace construction, the normal predual and faithful normal GNS inputs, AF1–5, and the preceding complete central sequence, exact lifting and fullness/corner proofs. The finite and infinite limits are treated separately: faithfulness uses the converging tails, trace-preserving maps have whole-domain normality, and product states supply the spatial identification.

Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://www.numdam.org/articles/10.24033/asens.1295/), Lemmas 2.3.5–2.3.6, printed pp.406–407 (PDF pp.25–26), is the freely accessible comparison for the matrix-functional estimate and commuting-matrix summability method. Its estimate is \(p^2\), and its splitting proof calls on Haar averaging, finite-factor identification and modular conditional-expectation results. Here the finite sign/permutation average gives \(p^{3/2}\), the complete variable product supplies the factor identification, and the entire product-GNS argument supplies the splitting. The independent trace-norm construction and every boundary case above are proved explicitly.
