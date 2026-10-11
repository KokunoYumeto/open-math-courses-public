# Weighted tensor splitting from summable errors

Commuting finite matrix algebras need not exhaust the ambient von Neumann algebra. A summable error condition on a norm-total family of normal functionals forces them to split off as an infinite tensor factor. The matrix states may vary, and the ambient algebra need not be a factor, have separable predual, or possess a faithful normal state.

We use the matrix-coordinate calculation, the concrete predual and normal bounded module actions, and the bounded positive GNS construction. We give the weighted extension of the earlier tracial splitting proof, Theorem 3.1. The last section uses the earlier programme's full proofs for the types of the constant products; the splitting argument itself uses no type classification.

## 1. Faithful weighted matrix expectations

Let \(M\ne0\) be a von Neumann algebra. Suppose that \(D_k\subset M\), \(k\ge1\), are mutually commuting unital full matrix algebras of sizes \(d_k\ge1\). Fix matrix units \(e_{ij}^{(k)}\) and positive numbers


\[
r_{ki}>0,\qquad \sum_{i=1}^{d_k}r_{ki}=1.
\]


The state \(\omega_k\) on \(D_k\) is specified by \(\omega_k(e_{ij}^{(k)})=\delta_{ij}r_{ki}\). These are arbitrary faithful matrix states after choosing matrix units that diagonalize their densities. Put \(N_k=D_k'\cap M\). For this section suppress the index \(k\), and define


\[
\begin{aligned}
C_{ij}(x)&=\sum_{a=1}^d e_{ai}xe_{ja},\\
E(x)&=\sum_{i=1}^d r_i C_{ii}(x).
\end{aligned}
\tag{1}
\]


The matrix-unit identities give


\[
\begin{aligned}
e_{ab}C_{ij}(x)&=e_{ai}xe_{jb}=C_{ij}(x)e_{ab},\\
x&=\sum_{i,j=1}^d C_{ij}(x)e_{ij},\\
C_{ij}(ne_{st})&=\delta_{is}\delta_{jt}n
\quad(n\in N).
\end{aligned}
\tag{2}
\]


Thus the coefficients lie in \(N\) and the expansion is unique. They are normal contractions. Indeed, on any faithful concrete representation \(M\subset B(H)\), put \(K=e_{11}H\). The map


\[
W:H\longrightarrow K^{\oplus d},\qquad
W\xi=(e_{1j}\xi)_{j=1}^d
\]


is unitary: its squared norm is \(\sum_j\langle e_{jj}\xi,\xi\rangle\), and its inverse sends \((\eta_j)_j\) to \(\sum_j e_{j1}\eta_j\). For \(n\in N\), \(WnW^*\) has \(n|_K\) on every diagonal. This makes \(n\mapsto n|_K\) faithful and isometric. Also \(WxW^*=[C_{ij}(x)|_K]\), so compression to an entry proves \(\|C_{ij}(x)\|\le\|x\|\). Normality follows from the finite sums of bounded module actions. Equation (2), including its product and adjoint identities, therefore proves the normal multiplication isomorphism


\[
D\bar\otimes N\cong M.
\tag{3}
\]


Each \(C_{ii}\) is a sum of maps \(x\mapsto a^*xa\), and is unital. Hence \(E\) is normal, unital and completely positive, and its norm is one by the contraction bounds. It fixes \(N\), is \(N\)-bimodular, and satisfies


\[
E(bn)=\omega(b)n\qquad(b\in D,\ n\in N).
\tag{4}
\]


It is faithful: if \(x\ge0\) and \(E(x)=0\), positivity and \(r_i>0\) give \(C_{ii}(x)=0\) for every \(i\). One positive summand of this last expression is \(e_{ii}xe_{ii}\). Thus \(x^{1/2}e_{ii}=0\) for all \(i\), and \(x=0\).

Return to the indexed algebras and write \(E_k\) for (1). Their finite Kraus sums commute term by term because different \(D_k\)'s commute. A finite composition is consequently a faithful normal conditional expectation onto the intersection of the corresponding commutants: it has range there, fixes that intersection, and is bimodular over it. Faithfulness follows by removing the faithful factors one at a time from a positive element of its kernel.

## 2. Predual limits for every tail

Let \(\mathcal F\subset M_*\) have norm-dense complex linear span. Assume


\[
\sum_{k=1}^\infty
\|\varphi-\varphi\circ E_k\|<\infty
\qquad(\varphi\in\mathcal F).
\tag{5}
\]


Neither positivity nor countability of \(\mathcal F\) is required. For \(N\ge m\), let \(F_{m,N}=E_m\cdots E_N\), and write \(\delta_k(\varphi)=\|\varphi-\varphi E_k\|\). Commutativity gives the telescoping identity


\[
\varphi F_{m,L}-\varphi F_{m,N}
=\sum_{k=N+1}^L(\varphi E_k-\varphi)F_{m,k-1}.
\]


Every map on the right is contractive, whence


\[
\|\varphi F_{m,L}-\varphi F_{m,N}\|
\le\sum_{k=N+1}^L\delta_k(\varphi).
\tag{6}
\]


The sequence \(\varphi F_{m,N}\) is therefore norm Cauchy for \(\varphi\in\mathcal F\), and then for its linear span. For arbitrary \(\eta\in M_*\), choose \(\varphi\) in that span with \(\|\eta-\varphi\|<\varepsilon\). The corresponding difference for \(\eta\) is at most the difference for \(\varphi\) plus \(2\varepsilon\). Completeness of \(M_*\) proves convergence for every \(\eta\).

The limit defines a linear contraction \(S_m:M_*\to M_*\). Its Banach adjoint, using \(M=(M_*)^*\), is a normal contraction \(T_m:M\to M\), and


\[
\eta(T_mx)=\lim_{N\to\infty}\eta(F_{m,N}x).
\tag{7}
\]


This predual construction proves normality; a pointwise ultraweak limit alone would not. Each finite map is unital and completely positive. At every matrix level its entrywise ultraweak limit is positive, since the positive cone is closed under all vector quadratic-form tests. Thus \(T_m\) is unital and completely positive too.

Set


\[
\mathcal N_m=\bigcap_{k\ge m}(D_k'\cap M).
\tag{8}
\]


For \(k\ge m\), normality of \(E_k\) and eventual equality \(E_kF_{m,N}=F_{m,N}\) give \(E_kT_m=T_m\), so its range lies in \(\mathcal N_m\). Every finite map fixes \(\mathcal N_m\), hence so does \(T_m\). Their bimodule identities over \(\mathcal N_m\) pass to the limit by normality of bounded multiplication. Therefore \(T_m\) is a normal conditional expectation onto \(\mathcal N_m\).

For \(\varphi\in\mathcal F\), the same telescoping estimate, beginning with the empty product, yields


\[
\|\varphi-\varphi T_m\|
\le\sum_{k=m}^\infty\delta_k(\varphi)
\longrightarrow0.
\tag{9}
\]


The linear-span approximation just used extends the convergence, though not necessarily the displayed summability bound, to every \(\eta\in M_*\). In particular


\[
T_m(x)\longrightarrow x\quad\hbox{ultraweakly}
\qquad(x\in M).
\tag{10}
\]


## 3. Faithfulness and generation by the two factors

Put


\[
P=\bigvee_{k\ge1}D_k,\qquad Q=P'\cap M,
\qquad A_n=D_1\vee\cdots\vee D_n,
\]


with \(A_0=\mathbb C1\). The multiplication representation identifies \(A_n\) with \(\bigotimes_{k=1}^nD_k\). Indeed the products of the individual matrix units form a unital full matrix-unit system of size \(\prod_{k=1}^n d_k\); none of its diagonal units is zero, because they are all equivalent and their sum is one. This also proves injectivity of the finite tensor representation.

Let \(E=T_1:M\to Q\). For \(H_{m-1}=E_1\cdots E_{m-1}\), with \(H_0=\operatorname{id}\), normality and the finite composition identities give


\[
E=H_{m-1}T_m.
\tag{11}
\]


Suppose \(x\ge0\) and \(E(x)=0\). The positive element \(T_m(x)\) is killed by the faithful finite composition \(H_{m-1}\), so \(T_m(x)=0\) for every \(m\). Equation (10) gives \(x=0\). Thus **the limit expectation \(E\) is faithful**. This conclusion uses the tail limits approaching the identity, as well as faithfulness of the finite compositions.

The matrix coordinates (2) for the finite head \(A_{m-1}\) show that


\[
\mathcal N_m=A_{m-1}\vee Q.
\tag{12}
\]


To check the nontrivial inclusion, take \(x\in\mathcal N_m\). Its head coefficients commute with the head. Every tail block commutes both with \(x\) and with the head matrix units, so it also commutes with every coefficient. The coefficients therefore belong to \(Q\), and (2) expresses \(x\) as a finite sum of products from \(A_{m-1}\) and \(Q\). Conversely both these algebras commute with all tail blocks.

Now \(T_m(x)\in A_{m-1}\vee Q\subset P\vee Q\). Equations (10) and ultraweak closedness give


\[
M=P\vee Q.
\tag{13}
\]


No assumption that the initially given blocks generate \(M\) has been made.

## 4. Spatial splitting without a faithful ambient state

For a local product \(a=a_1\cdots a_n\), with \(a_k\in D_k\), equations (4), (7) give


\[
E(a)=\left(\prod_{k=1}^n\omega_k(a_k)\right)1.
\tag{14}
\]


Finite local products linearly span an ultraweakly dense subalgebra of \(P\). Normality of \(E\) and ultraweak closedness of \(\mathbb C1\) therefore give \(E(a)=\omega(a)1\) for every \(a\in P\), for a normal state \(\omega\) on \(P\). It is faithful because \(E\) is faithful. Bimodularity gives


\[
E(ab)=\omega(a)b\qquad(a\in P,\ b\in Q).
\tag{15}
\]


Let \(\chi\) run through the normal states of \(Q\), and put \(\rho_\chi=\chi E\), a normal state of \(M\). We briefly verify the representation facts needed here. If \(\rho\) is a normal state on any von Neumann algebra, its bounded GNS representation is normal: for \(0\le x_i\uparrow x\),


\[
\langle\pi_\rho(x-x_i)\pi_\rho(a)\Omega_\rho,
             \pi_\rho(a)\Omega_\rho\rangle
=\rho(a^*(x-x_i)a)\longrightarrow0.
\]


Uniform boundedness and the density of the cyclic vectors extend this to all vectors, proving preservation of the increasing supremum. If \(\rho\) is faithful, \(\pi_\rho(x)=0\) implies \(\rho(x^*x)=0\), hence \(x=0\).

With inner products linear in the second variable, define on a dense algebraic tensor product


\[
U_\chi(a\Omega_\omega\otimes b\Omega_\chi)
=ab\Omega_{\rho_\chi}.
\tag{16}
\]


Because \(P\) and \(Q\) commute, (15) gives


\[
\rho_\chi((ab)^*cd)
=\omega(a^*c)\chi(b^*d).
\tag{17}
\]


This proves that (16) is well defined and isometric, including the null quotients when \(\chi\) is not faithful. It is onto. Indeed a vector orthogonal to all \(ab\Omega_{\rho_\chi}\) defines a normal coefficient of \(\pi_{\rho_\chi}\) vanishing on the algebra generated by \(P,Q\). Equation (13) makes this coefficient zero on all of \(M\), and cyclicity makes the vector zero. The unitary \(U_\chi\) intertwines the first and second factor actions with \(\pi_{\rho_\chi}(P)\) and \(\pi_{\rho_\chi}(Q)\).

The direct sum \(\bigoplus_\chi\pi_\chi\) is a faithful normal representation of \(Q\). Normality follows on finite component vectors and then on all vectors by norm approximation. Faithfulness follows because normal states separate positive elements: in a faithful concrete representation, a vector state detects every nonzero positive operator. Similarly \(\bigoplus_\chi\pi_{\rho_\chi}\) is faithful on \(M\). If all its components kill \(x\), then


\[
\chi(E(x^*x))=0\quad\hbox{for every normal state }\chi;
\]


thus \(E(x^*x)=0\), and faithfulness of \(E\) gives \(x=0\).

Taking the direct sum of (16) and grouping its first leg gives a unitary from


\[
H_\omega\otimes\left(\bigoplus_\chi H_\chi\right)
\quad\hbox{onto}\quad
\bigoplus_\chi H_{\rho_\chi}.
\]


Both factor representations on the left and the representation of \(M\) on the right are faithful and normal. Their images are von Neumann algebras by the normal-image theorem, UB08, and their generated algebras are intertwined, by (13). By the definition of the spatial tensor product, this proves the normal multiplication isomorphism


\[
\boxed{P\bar\otimes Q\ \cong\ M,
\qquad a\otimes b\longmapsto ab.}
\tag{18}
\]


When \(M\) has a faithful normal state, one can use its restriction to \(Q\) alone in this proof. The direct sum supplies the same conclusion without that additional hypothesis.

## 5. The actual infinite product and its center

Let \(H_k\) be the GNS space of \((D_k,\omega_k)\), with reference vector \(\Omega_k\). In the completion of the finite-support tensor vectors, the map


\[
\bigotimes_{k=1}^n a_k\Omega_k
\longmapsto (a_1\cdots a_n)\Omega_\omega
\tag{19}
\]


preserves inner products by (14); reference vectors fill the omitted legs. Its range is dense in \(H_\omega\): a vector orthogonal to the finite-head cyclic vectors gives a normal coefficient vanishing on the ultraweakly dense finite-head algebra, hence on \(P\), and then is zero. Thus (19) extends to a unitary intertwining every local algebra. Since \(\pi_\omega\) is faithful and normal, this identifies the whole represented algebras, not only their finite moments:


\[
(P,\omega)\cong\bigotimes_{k=1}^\infty(D_k,\omega_k).
\tag{20}
\]


Here is a direct proof of factoriality using the already constructed tails. For each \(m\), formula (4) shows that \(T_m\) sends every finite head into \(A_{m-1}\). Normality and finite dimensionality give \(T_m(P)\subset A_{m-1}\). Also (11) and idempotence of \(T_m\) imply \(ET_m=E\), so \(\omega T_m=\omega\) on \(P\).

If \(z\in Z(P)\), bimodularity of \(T_m\) over \(A_{m-1}\) makes \(T_m(z)\) central in that full matrix algebra. It is therefore scalar, and state preservation makes it \(\omega(z)1\). Passing to the limit in (10) gives \(z=\omega(z)1\). Hence \(P\) is a factor. Its increasing finite heads generate it, so it is approximately finite dimensional.

The product representation has separable Hilbert space: choose a finite orthonormal basis of each \(H_k\) containing \(\Omega_k\); its finite-support product basis is countable. The concrete-predual quotient in CP06 therefore gives separable predual for \(P\). This conclusion concerns \(P\); neither \(M\) nor \(Q\) need have separable predual. If infinitely many \(d_k\ge2\), the unbounded matrix-head dimensions make \(P\) infinite dimensional. If only finitely many blocks are nontrivial, \(P\) is just their finite matrix product.

## 6. Summable modular defects and constant products

Suppose now \(d_k=2\), put \(u_k=e_{12}^{(k)}\), and choose any \(\lambda_k>0\), with


\[
\omega_k(e_{11}^{(k)})=\frac{\lambda_k}{1+\lambda_k},
\qquad
\omega_k(e_{22}^{(k)})=\frac1{1+\lambda_k}.
\tag{21}
\]


Thus \(u_ku_k^*=e_{11}^{(k)}\) and \(u_k^*u_k=e_{22}^{(k)}\). For normal positive \(\varphi\), PS03 proves


\[
\begin{aligned}
\|\varphi-\varphi E_k\|
&\le C_{\lambda_k}\,
       \|\varphi u_k-\lambda_k u_k\varphi\|,\\
C_\lambda&=\frac2{1+\lambda}
            +\frac2{\max\{1,\lambda\}}\le4.
\end{aligned}
\tag{22}
\]


The conventions are \((\varphi u)(x)=\varphi(ux)\) and \((u\varphi)(x)=\varphi(xu)\). Therefore, if a norm-total family \(\mathcal F\subset M_*^+\) satisfies


\[
\sum_{k=1}^\infty
C_{\lambda_k}\|\varphi u_k-\lambda_k u_k\varphi\|
<\infty\qquad(\varphi\in\mathcal F),
\tag{23}
\]


all conclusions (18), (20) follow. The stronger assumption obtained by omitting \(C_{\lambda_k}\) also suffices, since those constants are uniformly bounded by four. This allows varying positive weights, even weights approaching zero; no uniform positive lower bound on the individual matrix densities was used.

In particular, let \(\lambda_k=\lambda\) be constant and let \((\varphi_j)\) be norm dense among the normal states of \(M\). This family has norm-dense linear span in \(M_*\). For a concrete verification, CP06 writes every normal functional as a norm limit of finite sums of vector coefficients. Polarization writes each vector coefficient as a linear combination of four positive vector functionals; after removing zero terms and normalizing, these are normal states. Approximate each of the finitely many states by the \(\varphi_j\)'s. Consequently


\[
\sum_k\|\varphi_j u_k-\lambda u_k\varphi_j\|<\infty
\quad\hbox{for every }j
\tag{24}
\]


implies that the constant product factor splits off from \(M\).

For \(0<\lambda<1\), that factor is of type \(\mathrm{III}_\lambda\). The exact earlier proof is Constant CAR states and the periodic core, Section 6, Theorem 6.1, together with its completed product identification in Section 1. Set \(p=1/(1+\lambda)\) there. Its density \(\operatorname{diag}(1-p,p)\) is exactly (21), and its parameter \(\min(p,1-p)/\max(p,1-p)\) equals \(\lambda\). The proof computes the intersection of spectra over **all** faithful normal semifinite weights:


\[
S(P)=\{0\}\cup\lambda^{\mathbb Z}.
\tag{25}
\]


This is the stated subtype input; periodicity of one modular group alone would not prove (25). Combining that programme proof with (18), (20), (24) proves the complete constant-weight splitting and type conclusion.

At \(\lambda=1\), the splitting still holds and the product factor is of type \(\mathrm{II}_1\), by the complete product-trace proof in Infinite tensor products, Section 5, Corollary 5.3. For constant \(\lambda>1\), the same density calculation gives type \(\mathrm{III}_{1/\lambda}\). Varying weights retain the product identification (20), but no fixed subtype follows merely from the summability condition.

Strict positivity of the leg weights is essential to the faithfulness argument. For example, on \(M_2\) the map \(x\mapsto x_{22}1\) is a normal unital completely positive expectation onto the scalars, but kills \(e_{11}\). It is the zero-weight endpoint of (1), and the inference from (11) to \(T_m(x)=0\) cannot be made with that map. Likewise, summability tested on an arbitrary non-total family supplies no density argument extending (6) to every normal functional. The hypotheses used to obtain normality, faithfulness and the spatial product have distinct roles.
