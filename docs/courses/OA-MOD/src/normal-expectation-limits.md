# Averaging and limits of normal expectations

A conditional expectation can arise from a vector in a tensor factor, from averaging conjugations, or as a limit of expectations. The last construction requires control of normal functionals: pointwise convergence alone need not preserve normality. We develop all three constructions and then use a summable predual estimate to obtain a tensor decomposition.

Inner products are linear in the first variable. All von Neumann subalgebras in this lesson have the same identity as the ambient algebra. A normal functional means an element of the predual, with its Banach norm. We use the written predual representation in CP06, dual-ball compactness in AB05, normal multiplication maps in BK03, and the trace-preserving expectation and Hilbert projection of TA03–04. CP07 supplies positivity detection, Cauchy–Schwarz and decomposition of normal functionals. The equivalence of order normality, ultraweak continuity and a bounded preadjoint is NP03–04.

## Compression along a tensor tail

For clarity, the finite Hilbert tensor product is the completion of the algebraic tensor product with its product inner product. Positivity is checked on a finite sum by choosing an orthonormal basis of the finite-dimensional span of its first-factor vectors: successively subtract the projections onto previously chosen unit vectors and normalize each nonzero remainder. The sum becomes \(\sum_i e_i\otimes\eta_i\), whose squared norm is \(\sum_i\|\eta_i\|^2\); zero norm forces every coefficient to vanish. This proves positive definiteness as well as independence from the chosen expression, since the product inner product respects the defining bilinear relations. Completion and extension of bounded maps are the explicit construction in CP01.

Let \(H_j\) be Hilbert spaces with chosen unit vectors \(\Omega_j\). Put \(H_{\leq n}=H_1\otimes\cdots\otimes H_n\). Embed \(H_{\leq n}\) isometrically in \(H_{\leq n+1}\) by \(\xi\mapsto\xi\otimes\Omega_{n+1}\). Identify a vector with its image at every later stage. The inner product of two such vectors is computed at any common stage; the embeddings show that it is independent of that choice. Its completion is a Hilbert space \(H\), and the union of the finite-stage spaces is dense by construction.

The same construction on the factors after \(n\) gives a tail space \(K_n\) and a unit vector \(\Omega_{>n}\). Concatenation of finite tensors preserves inner products and has dense range, so it extends to a unitary \(H_{\leq n}\otimes K_n\to H\). We use this identification. Let \(V_n\xi=\xi\otimes\Omega_{>n}\) and define
\[
 E_n(x)=(V_n^*xV_n)\otimes I_{K_n},\qquad x\in B(H).
\tag{EL.1}
\]
This is a normal conditional expectation onto \(B(H_{\leq n})\otimes I\).

Indeed, compression is linear, unital and positive, and at every matrix level it remains a compression. Amplification by the identity has the same properties. For bounded \(a\), its amplification has norm \(\|a\|\): expand in an orthonormal basis of the second factor for the upper bound, and test unit simple tensors for the lower bound. Thus \(E_n\) is contractive. Formula (EL.1) fixes the stated range and is bimodular over it. Compression preserves bounded increasing positive suprema by testing on vectors. Amplification does so first on finite sums of simple tensors and then on all vectors by density and the common operator bound. Hence both maps, and their composition, are normal.

For every \(\omega\in B(H)_*\),
\[
 \|\omega\circ E_n-\omega\|\longrightarrow0.
\tag{EL.2}
\]
To prove this, write \(\omega_{\xi,\eta}(x)=\langle x\xi,\eta\rangle\). If \(\xi,\eta\) are in a common finite-stage space, then \(\omega_{\xi,\eta}\circ E_n=\omega_{\xi,\eta}\) for all later \(n\). For general vectors choose finite-stage \(\xi_0,\eta_0\) close to them. The elementary estimate
\[
 \|\omega_{\xi,\eta}-\omega_{\xi_0,\eta_0}\|
 \leq\|\xi-\xi_0\|\,\|\eta\|+\|\xi_0\|\,\|\eta-\eta_0\|
\]
and contractivity of the preadjoints give (EL.2) for vector functionals. Finite sums of vector functionals are norm dense in the predual by CP06. Approximate a general \(\omega\) by such a sum and use \(\|E_n\|\leq1\) once more. No finite-dimensionality of the individual \(H_j\) is used.

## A unitary subgroup and the trace projection

Let \(M\) have a faithful normal finite trace \(\tau\), let \(G\) be any subgroup of its unitary group, and put \(N=G'\cap M\). The restriction of \(\tau\) to \(N\) is finite and faithful, so TA03–04 provide the normal trace-preserving expectation \(E_N\). For \(x\in M\), let \(K_G(x)\) be the ultraweakly closed convex hull of \(\{uxu^*:u\in G\}\). Then
\[
 K_G(x)\cap N=\{E_N(x)\}.
\tag{EL.3}
\]
Neither a topology on \(G\) nor an invariant mean on \(G\) is assumed.

Here are the compactness and minimization details. The set \(K_G(x)\) is contained in the radius-\(\|x\|\) ball of the dual space \(M\), so it is ultraweakly compact. The function \(q(y)=\tau(y^*y)\) is ultraweakly lower semicontinuous. If \(y_i\to y\) ultraweakly, normality of \(z\mapsto\tau(y^*z)\) and Cauchy–Schwarz give
\[
 |\tau(y^*y_i)|^2\leq q(y)q(y_i).
\]
For \(q(y)>0\), divide and take the lower limit; for \(q(y)=0\), positivity suffices. The closed sublevel sets at \(\inf_{K_G(x)}q+1/k\) have the finite intersection property. Compactness gives a minimizer \(y_0\). The parallelogram identity and faithfulness make it unique.

Conjugation by every \(u\in G\) preserves both the set and \(q\), so it fixes \(y_0\); thus \(y_0\in N\). For \(a\in N\), trace preservation and bimodularity imply
\[
 \tau\!\left(aE_N(uxu^*)\right)=\tau(auxu^*)=\tau(ax)
 =\tau\!\left(aE_N(x)\right).
\]
The trace pairing separates \(N\): apply it to the adjoint of the difference. Consequently \(E_N(uxu^*)=E_N(x)\). Linearity and normality extend this constancy to \(K_G(x)\). Since \(E_N(y_0)=y_0\), we obtain \(y_0=E_N(x)\). Any other member of \(K_G(x)\cap N\) is similarly equal to \(E_N(x)\), proving (EL.3). This argument also applies when \(M\) is not a factor.

## A finite matrix algebra and explicit error bounds

Let \(A\subseteq M\) be a unital copy of \(M_p(\mathbb C)\), with matrix units \(e_{ij}\), and set \(C=A'\cap M\). Define
\[
 Q_A(x)=\frac1p\sum_{i,j=1}^p e_{ij}xe_{ji}.
\tag{EL.4}
\]
This is a faithful normal conditional expectation onto \(C\). Each summand is a normal completely positive map, and
\(\frac1p\sum_{i,j}e_{ij}e_{ji}=1\).
For a matrix unit \(e_{ab}\), both \(e_{ab}Q_A(x)\) and \(Q_A(x)e_{ab}\) equal
\(\frac1p\sum_j e_{aj}xe_{jb}\).
Thus the range is in \(C\). If \(x\in C\), (EL.4) gives \(Q_A(x)=x\). Bimodularity follows directly by moving elements of \(C\) past the matrix units. Contractivity follows, for example, from the Schwarz inequality for the unital completely positive map. That inequality follows by applying its two-by-two amplification to the positive matrix
\(\left(\begin{smallmatrix}x^*x&x^*\\x&1\end{smallmatrix}\right)\).
If \(x\geq0\) and \(Q_A(x)=0\), every positive summand vanishes. In particular \(x^{1/2}e_{ii}=0\) for all \(i\), whence \(x=0\). This proves faithfulness.

The product identification used here is elementary, including its normality. With \(e=e_{11}\), the mutually inverse maps
\[
 (a_{ij})\longmapsto\sum_{i,j}e_{i1}a_{ij}e_{1j},
 \qquad
 x\longmapsto(e_{1i}xe_{j1})_{ij}
\tag{EL.5}
\]
identify \(M_p(eMe)\) with \(M\). Matrix multiplication and the adjoint verify that these are *-homomorphisms; their entries are normal multiplication maps. In these coordinates the commutant \(C\) consists of equal diagonal entries, and \(Q_A\) replaces the matrix by its normalized diagonal sum on every diagonal. In particular, under \(M\cong A\bar\otimes C\),
\[
 Q_A=\tau_p\otimes\operatorname{id}_C,
\tag{EL.6}
\]
where \(\tau_p\) is the normalized matrix trace.

For a normal functional \(\omega\), define
\(c_a\omega(y)=\omega(ay)-\omega(ya)\).
The following bounds hold:
\[
 \begin{aligned}
 \|\omega-\omega Q_A\|&\leq p\max_{i,j}\|c_{e_{ij}}\omega\|,\\
 \|x-Q_A(x)\|_{2,\tau}&\leq
 p\max_{i,j}\|e_{ij}x-xe_{ij}\|_{2,\tau}.
 \end{aligned}
\tag{EL.7}
\]
The second line assumes a finite trace \(\tau\) on \(M\). The first follows from the exact identity
\[
 (\omega-\omega Q_A)(x)=\frac1p\sum_{i,j}
 (c_{e_{ji}}\omega)(e_{ij}x).
\]
For the second, use
\[
 x-Q_A(x)=\frac1p\sum_{i,j}e_{ij}(e_{ji}x-xe_{ji}),
\]
the triangle inequality and
\(\|e_{ij}z\|_{2,\tau}\leq\|z\|_{2,\tau}\).
Each estimate is \(p^2\) terms divided by \(p\). In particular they imply the bounds with coefficient \(p^{3/2}\). If \(\tau\) is tracial, (EL.4) also preserves \(\tau\), so uniqueness in TA04 identifies it with the trace-preserving expectation onto \(C\).

## Summable errors give a normal limit

Suppose \(A_1,A_2,\ldots\) are mutually commuting unital finite matrix subalgebras of \(M\), and write \(Q_n=Q_{A_n}\). Suppose there is a subset \(\mathcal D\subseteq M_*\) whose complex linear span is norm dense and such that
\[
 \sum_{n=1}^{\infty}\|\omega-\omega Q_n\|<\infty
 \quad(\omega\in\mathcal D).
\tag{EL.8}
\]
A norm-dense sequence of normal states is one way to supply such a set; its complex span is dense in the predual by the decomposition of a normal functional into a linear combination of positive normal functionals. The theorem itself uses the stated density condition, not a separability assumption on \(M\).

The maps \(Q_n\) commute: insert (EL.4) twice and commute the matrix units from different algebras. Let \(F_m=Q_1\cdots Q_m\). These are normal contractive expectations onto
\((A_1\vee\cdots\vee A_m)'\cap M\).
For \(\omega\in\mathcal D\), commutation gives the crucial estimate
\[
 \|\omega F_{m+1}-\omega F_m\|
 =\|(\omega Q_{m+1}-\omega)F_m\|
 \leq\|\omega Q_{m+1}-\omega\|.
\tag{EL.9}
\]
Hence \(\omega F_m\) is norm Cauchy. This extends first by linearity to the span of \(\mathcal D\) and then, using the common contraction bound, to every \(\omega\in M_*\). Completeness of the predual produces a bounded linear map \(P:M_*\to M_*\) with \(P\omega=\lim_m\omega F_m\).

Set \(F=P^*:M\to M\), using \(M=(M_*)^*\). Thus \(F\) is normal and \(F_m(x)\to F(x)\) ultraweakly. Positivity, unitality and contractivity pass to this limit. For fixed \(k\), normality of \(Q_k\) and \(Q_kF_m=F_m\) for \(m\geq k\) give \(Q_kF=F\). Therefore the range is contained in
\[
 N=\bigcap_{k\geq1}(A_k'\cap M).
\]
Every \(F_m\) fixes \(N\) and is \(N\)-bimodular, so the limit does too. This proves that \(F\) is a normal conditional expectation onto \(N\). Its complete positivity can either be checked on matrix levels by the same positive-cone limit or obtained from the written conditional-expectation theorem.

For every \(\omega\) for which the series converges, summing (EL.9) gives
\[
 \|\omega F-\omega F_m\|
 \leq\sum_{n>m}\|\omega Q_n-\omega\|.
\tag{EL.10}
\]
The proof has constructed a preadjoint. It has not inferred normality from a bare pointwise limit of normal maps.

## Tail limits, faithfulness and generation

For each \(m\), apply the preceding construction to \(Q_m,Q_{m+1},\ldots\); call its normal expectation \(T_m\). It has range
\(N_m=\bigcap_{n\geq m}(A_n'\cap M)\).
Telescoping from the identity gives, for \(\omega\in\mathcal D\),
\[
 \|\omega T_m-\omega\|\leq
 \sum_{n\geq m}\|\omega Q_n-\omega\|\longrightarrow0.
\tag{EL.11}
\]
Density and contractivity extend convergence to every normal functional, so \(T_m(x)\to x\) ultraweakly for every \(x\in M\).

Put \(B_{m-1}=A_1\vee\cdots\vee A_{m-1}\), with \(B_0=\mathbb C1\). Multiplication identifies \(B_{m-1}\) with the finite tensor product of these matrix algebras. To justify injectivity, the multiplication map is a unital *-homomorphism from a full matrix algebra; its kernel is an ideal and a full matrix algebra has no nonzero proper ideal, as multiplication by matrix units shows. Now (EL.5) identifies \(M\) with a matrix algebra over \(B_{m-1}'\cap M\). Each \(A_n\), \(n\geq m\), lies in this commutant. Commutation with all these \(A_n\) is therefore equivalent, entry by entry, to membership of every matrix entry in the common commutant. Consequently
\[
 N_m=B_{m-1}\vee N.
\tag{EL.12}
\]
On this finite matrix algebra over \(N\), the expectation \(F\) is the normalized matrix trace tensored with the identity. Indeed all the later \(Q_n\) fix it, and the product of the first \(m-1\) expectations is precisely that partial trace by (EL.6). In particular this restriction of \(F\) is faithful.

Also \(F T_m=F\): first \(FQ_n=F\), by the finite-product formula and the predual limit, and then pass to the defining limit for \(T_m\), using normality of \(F\). If \(x\geq0\) and \(F(x)=0\), it follows that
\(F(T_m(x))=0\).
But \(T_m(x)\geq0\) is in \(N_m\), where the restriction is faithful; hence \(T_m(x)=0\). Its ultraweak limit is \(x\), so \(x=0\). Thus \(F\) is faithful. This step is necessary: faithfulness does not follow merely by taking a limit of faithful expectations.

Let \(R=\bigvee_n A_n\). By (EL.12), every \(T_m(x)\) belongs to \(R\vee N\). Ultraweak closure and (EL.11) give
\[
 M=R\vee N,\qquad N=R'\cap M.
\tag{EL.13}
\]

## The spatial tensor product

The restriction of \(F\) to \(R\) has scalar range. It has this property on each finite \(B_m\), and then on their ultraweak closure by normality. Write
\[
 F(r)=\tau_R(r)1,\qquad r\in R.
\]
Here \(\tau_R\) is a normal faithful state. It is tracial: the identity
\(\tau_R(ab)=\tau_R(ba)\)
holds on the union of the finite matrix algebras. Extend one variable and then the other using separate ultraweak continuity of multiplication and normality. If \(z\in Z(R)\), then \(z\in N\), so \(z=F(z)\) is scalar. Thus \(R\) is a finite factor.

There is a normal *-isomorphism
\[
 R\bar\otimes N\longrightarrow M,\qquad r\otimes n\longmapsto rn.
\tag{EL.14}
\]
We give the representation argument, including faithfulness. For a normal positive functional \(\varphi\) on \(N\), let \(\psi=\varphi F\). On the dense algebraic tensor domain, define
\[
 U_\varphi\bigl(\Lambda_{\tau_R}(r)\otimes\Lambda_\varphi(n)\bigr)
   =\Lambda_\psi(rn).
\]
For two such products, commutation and \(N\)-bimodularity of \(F\) give
\[
 \psi((sm)^*rn)=\tau_R(s^*r)\,\varphi(m^*n).
\]
Thus the map is well defined and isometric. Its range is dense: the closed span of the vectors \(\Lambda_\psi(rn)\) contains the cyclic vector, is invariant under both represented algebras and their adjoints, and hence is reducing for the algebra they generate. By (EL.13), this is the whole represented \(M\), whose cyclic vector generates the GNS space. Therefore \(U_\varphi\) is unitary and carries multiplication by \(r\) and \(n\) to their separate tensor representations.

Take the direct sum over all normal states \(\varphi\) of \(N\). Their GNS representations are normal by WG007 and jointly faithful, by positivity separation in CP07. The corresponding direct sum of representations of \(M\) is faithful as well: if \(x\geq0\) vanishes in every summand, then \(\varphi(F(x))=0\) for every such \(\varphi\); positive normal functionals separate positive elements, so \(F(x)=0\), and faithfulness of \(F\) gives \(x=0\). Direct sums preserve normality: for a vector with square-summable components, first control a finite head by normality and then the tail by the common positive operator bound. The image theorem WH02 makes these faithful normal images von Neumann algebras. The unitaries above therefore identify faithful normal representations of the two algebras in (EL.14), and the elementary products generate both. This proves the claimed isomorphism.

The type of \(R\) needs one explicit qualification. A type \(\mathrm{II}_1\) factor is a finite factor with no nonzero minimal projection. If infinitely many \(A_n\) have matrix size at least two, write \(B_m\cong M_{d_m}(\mathbb C)\); then \(d_m\to\infty\). A minimal matrix projection \(q_m\) in \(B_m\) has \(\tau_R(q_m)=1/d_m\), since the restriction of \(\tau_R\) is the normalized matrix trace. These nonzero projections have traces tending to zero. If \(R\) had a minimal projection \(p\), MG01–02 would give \(\tau_R(q)\geq\tau_R(p)>0\) for every nonzero projection \(q\) of \(R\), a contradiction. Thus \(R\) has no minimal projection and is of type \(\mathrm{II}_1\). If only finitely many \(A_n\) are nontrivial, \(R\) is their finite matrix tensor product instead. This proves the type assertion without a separate factor-classification theorem.

## The tracial square-integrable hypothesis

Assume now that \(M\) has a faithful normal finite trace \(\tau\). Let \(Q_n\) be the matrix expectations of EL03 for mutually commuting finite matrix algebras. Suppose a family \((x_j)_{j\in J}\subset M\) has complex linear span dense in \(L^2(M,\tau)\), and
\[
 \sum_{n=1}^{\infty}\|x_j-Q_n(x_j)\|_{2,\tau}<\infty
 \quad(j\in J).
\tag{EL.15}
\]
Then all conclusions of EL04–06 hold. A sigma-strongly dense sequence in \(M\), as in the comparison statement, is sufficient: the seminorm defined by the normal functional \(\tau\) is exactly the \(L^2\) norm, and \(M\) is dense in its GNS completion. No uniform operator bound on that dense sequence is required.

To reduce (EL.15) to the predual hypothesis, define
\[
 \omega_y(a)=\tau(y^*a),\qquad y\in M,
 \qquad
 \|\omega_y\|\leq\tau(1)^{1/2}\|y\|_{2,\tau}.
\tag{EL.16}
\]
The estimate is Cauchy–Schwarz applied to \(y\) and \(a\), followed by \(\tau(a^*a)\leq\tau(1)\|a\|^2\). The map is conjugate-linear in \(y\), which does not affect density of its complex span. Each functional is normal by fixed multiplication and normality of \(\tau\).

These bounded-density functionals have norm-dense span in \(M_*\). Here is a proof avoiding an unstated integration duality theorem. The trace GNS representation is faithful and normal, and WH02 identifies its image with \(M\) and the same predual. By CP06, finite sums of vector functionals are norm dense in that predual. Replace their vectors by \(\Lambda_\tau(a),\Lambda_\tau(b)\), using density of the GNS domain and the vector-functional estimate from EL01. The resulting functional is
\[
 z\longmapsto\tau(b^*za)=\tau(ab^*z)=\omega_{ba^*}(z),
\]
which has bounded density in \(M\). This proves the claim. Estimate (EL.16) and the assumed \(L^2\) density now show that the span of \(\{\omega_{x_j}:j\in J\}\) is norm dense in \(M_*\).

TA04 identifies each trace-preserving \(Q_n\) with the orthogonal projection in \(L^2\). Consequently
\[
 \omega_y Q_n=\omega_{Q_n(y)},\qquad
 \|\omega_{x_j}-\omega_{x_j}Q_n\|
 \leq\tau(1)^{1/2}\|x_j-Q_n(x_j)\|_{2,\tau}.
\tag{EL.17}
\]
Thus (EL.15) gives (EL.8) on a family with norm-dense span, and EL04–06 apply, including the tail approximation, faithfulness and tensor decomposition. In this tracial setting, there is also a direct check of faithfulness of the limit: normality of \(\tau\) gives \(\tau(F(x))=\lim_m\tau(F_m(x))=\tau(x)\); for \(x\geq0\), \(F(x)=0\) therefore implies \(x=0\).

## Sources and scope

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIV, Lemmas 1.8, 2.6, 4.9, 4.10 and 4.10′, provides comparison statements for these constructions. The proofs here use the explicit finite matrix formula and preadjoint convergence. The finite-matrix error bound \(p\) implies the comparison bound \(p^{3/2}\); the tensor conclusion includes the necessary nontrivial-factor qualification. The factor-classification theorems surrounding those lemmas are separate results.
