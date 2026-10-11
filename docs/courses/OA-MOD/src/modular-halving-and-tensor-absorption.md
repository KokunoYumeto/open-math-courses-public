# Modular halving and tensor absorption

Fix \(0<\lambda<1\). Let \(R_\lambda\) be the infinite product of copies of \(M_2(\mathbb C)\) with state density


\[
\begin{pmatrix}\lambda/(1+\lambda)&0\\0&1/(1+\lambda)\end{pmatrix}.
\]


The weighted product theorem identifies this concrete product as an AFD factor of type \(\mathrm{III}_\lambda\). We characterize when a type III factor absorbs it. The main construction places new matrix blocks in exact relative commutants. A finite polarization formula makes the required tests positive and gives an explicit error budget.

For a von Neumann algebra \(M\), call the following property \(H_\lambda\): for every finite family \(\varphi_j\in M_*^+\) and every \(\varepsilon>0\), there is a partial isometry \(u\in M\) such that


\[
u^*u+uu^*=1,\qquad
\|\varphi_j u-\lambda u\varphi_j\|<\varepsilon
\quad\hbox{for every }j.
\tag{1}
\]


Our actions are \((\varphi u)(x)=\varphi(ux)\) and \((u\varphi)(x)=\varphi(xu)\). The first identity in (1) makes \(u\) a halving partial isometry, with matrix-unit orientation \(u=e_{12}\), \(uu^*=e_{11}\), \(u^*u=e_{22}\).

**Theorem.** If \(M\) is a type III factor with separable predual, then the following are equivalent:

1. There is a normal isomorphism \(M\cong M\bar\otimes R_\lambda\).
2. \(M\) has property \(H_\lambda\).
3. In a standard form \((M,H,J,\mathcal P)\), for every finite family \(\xi_j\in\mathcal P\) and every \(\varepsilon>0\), there is \(x\in M\), \(x\ne0\), such that


\[
\|\xi_jx-\sqrt\lambda\,x\xi_j\|^2
\le\varepsilon\sum_i\|x\xi_i\|^2
\quad\hbox{for every }j.
\tag{2}
\]


Here \(\xi x=Jx^*J\xi\). We prove the theorem below, using the earlier halving equivalence only for the passage between (1) and (2).

## 1. Positive tests for matrix coefficients

Let \(A\subset M\) be a unital full matrix algebra of size \(d\), with matrix units \(e_{ab}\), and let \(N=A'\cap M\). The normal commutant coordinates give


\[
x=\sum_{a,b=1}^d e_{ab}C_{ab}(x),\qquad
C_{ab}(x)\in N,\qquad
\|C_{ab}(x)\|\le\|x\|.
\tag{3}
\]


For \(\rho\in M_*^+\), define normal functionals on \(N\) by \(\rho_{ab}(n)=\rho(e_{ab}n)\). The off-diagonal ones need not be positive. For \(a\ne b\) and \(r=0,1,2,3\), put


\[
p_{ab}^{(r)}=\frac12\left(
e_{aa}+e_{bb}+i^{-r}e_{ab}+i^re_{ba}\right).
\tag{4}
\]


This is the rank-one projection onto \((e_a+i^re_b)/\sqrt2\) in the indicated two-dimensional corner. Multiplication of matrix units also directly verifies its selfadjointness and idempotence. Summing the four phases gives


\[
\begin{aligned}
e_{ab}&=\frac12\sum_{r=0}^3i^r p_{ab}^{(r)},\\
\sum_{r=0}^3p_{ab}^{(r)}&=2(e_{aa}+e_{bb}).
\end{aligned}
\tag{5}
\]


For any projection \(p\in A\), the functional \(\rho_p(n)=\rho(pn)\) is positive and normal on \(N\): commutation gives \(pn=pnp\), and this is positive when \(n\ge0\). Its norm is \(\rho(p)\). If this number is zero the functional is zero; otherwise normalize it to a normal state.

Suppose that a halving partial isometry \(v\in N\) has defect less than \(\eta\) on the normalized, nonzero functionals associated with all \(e_{aa}\) and \(p_{ab}^{(r)}\). By homogeneity,


\[
\begin{aligned}
\|\rho_{aa}v-\lambda v\rho_{aa}\|
&\le\eta\rho(e_{aa}),\\
\|\rho_{ab}v-\lambda v\rho_{ab}\|
&\le\frac\eta2\sum_{r=0}^3\rho(p_{ab}^{(r)})\\
&=\eta\bigl(\rho(e_{aa})+\rho(e_{bb})\bigr)
\quad(a\ne b).
\end{aligned}
\tag{6}
\]


The expansion (3) and \(v\in N\) imply


\[
(\rho v-\lambda v\rho)(x)
=\sum_{a,b}(\rho_{ab}v-\lambda v\rho_{ab})(C_{ab}(x)).
\]


Sum (6) and use the contraction bounds in (3). Each diagonal mass occurs twice for every other index in the off-diagonal sum. Consequently


\[
\boxed{\|\rho v-\lambda v\rho\|
\le(2d-1)\eta\,\rho(1).}
\tag{7}
\]


The construction works simultaneously for a finite family of positive \(\rho\)'s by taking the union of their finite state tests. When \(d=1\), there are no off-diagonal tests and the factor in (7) is one. Thus a halving property stated only for positive functionals suffices; no positivity is incorrectly assigned to an off-diagonal coefficient.

## 2. Transferring halving to exact commutants

Property \(H_\lambda\) is invariant under normal isomorphism. If \(\theta:B\to C\) is such an isomorphism, pull a finite positive family on \(C\) back by \(\theta\). Positivity and normality are preserved. For \(u\in B\),


\[
\begin{aligned}
\bigl(\varphi\theta\,u-\lambda u\varphi\theta\bigr)(x)
={}&\varphi(\theta(u)\theta(x))\\
&-\lambda\varphi(\theta(x)\theta(u)).
\end{aligned}
\]


The norms agree because \(\theta\) maps the unit ball onto the unit ball. It also preserves both support projections of a partial isometry. Apply the same argument to \(\theta^{-1}\) for the converse.

Now let \(M\) have the type III and separable-predual hypotheses of the theorem. For any finite matrix algebra \(A\subset M\), its commutant \(N=A'\cap M\) is normally isomorphic to \(M\). To prove this, put \(e=e_{11}\). The map


\[
\begin{aligned}
N&\longrightarrow eMe,& n&\longmapsto en,\\
eMe&\longrightarrow N,& z&\longmapsto\sum_{a=1}^d e_{a1}ze_{1a}
\end{aligned}
\tag{8}
\]


has inverse arrows by the matrix-unit identities. Products, adjoints and normality are checked by those identities and the finite sums of bounded module actions.

The type III corner argument in OH06 applies: separable predual makes the factor countably decomposable, and every nonzero corner projection is equivalent to one. In particular there is \(s\in M\) with \(s^*s=1\) and \(ss^*=e\). The normal isomorphism \(x\mapsto sxs^*\) from \(M\) to \(eMe\), followed by (8), gives the asserted isomorphism with \(N\). Hence \(H_\lambda\) passes from \(M\) to every such exact relative commutant.

## 3. Building a summable commuting sequence

Assume \(H_\lambda\). Choose normal states \((\psi_j)_{j\ge1}\) norm dense in the normal state space. This is possible because \(M_*\) is separable. Their complex linear span is norm dense in \(M_*\), by the vector-coefficient polarization argument in TS06.

Inductively construct halving partial isometries \(u_n\) and their unital matrix algebras \(D_n\cong M_2\). Suppose the first \(n-1\) blocks have been constructed and commute. Their head


\[
A_{n-1}=D_1\vee\cdots\vee D_{n-1}
\]


is a full matrix algebra of size \(d=2^{n-1}\), by the finite-head argument in TS03. Start with \(A_0=\mathbb C1\). Its commutant \(N_{n-1}=A_{n-1}'\cap M\) has \(H_\lambda\) by Section 2.

Apply Section 1 to \(\psi_1,\ldots,\psi_n\) and the head matrix units. There are finitely many normalized positive tests on \(N_{n-1}\). Use \(H_\lambda\) there with tolerance


\[
\eta_n=\frac{2^{-n}}{2d-1}.
\tag{9}
\]


The resulting halving partial isometry \(u_n\in N_{n-1}\) satisfies


\[
\|\psi_j u_n-\lambda u_n\psi_j\|
\le2^{-n}\qquad(1\le j\le n)
\tag{10}
\]


by (7), since every \(\psi_j\) has mass one. Its matrix units are \(u_nu_n^*,u_n,u_n^*,u_n^*u_n\), as proved in PS01. They all belong to the exact commutant \(N_{n-1}\). Thus the new block commutes with all earlier blocks, including their adjoints.

For a fixed \(j\), the finitely many defects with \(n<j\) are at most \(1+\lambda\), since \(\|u_n\|=1\). Equation (10) gives


\[
\sum_{n=1}^\infty
\|\psi_j u_n-\lambda u_n\psi_j\|
\le(j-1)(1+\lambda)+\sum_{n=j}^\infty2^{-n}<\infty.
\tag{11}
\]


This proves the countable summability condition needed for the infinite tensor decomposition. The normal states tested at successive stages are allowed to change; the estimate is nevertheless valid for each fixed original \(\psi_j\).

## 4. From splitting to absorption

Put \(P=\bigvee_nD_n\) and \(Q=P'\cap M\). The complete weighted splitting theorem, TS01–06, applied to (11), gives


\[
M\cong P\bar\otimes Q,
\qquad
(P,\omega)\cong\bigotimes_{n\ge1}(M_2,\omega_\lambda).
\tag{12}
\]


In particular \(P\cong R_\lambda\), with its actual product representation. The theorem supplies normality, faithfulness of the limiting expectation, generation by \(P,Q\), and the spatial isomorphism, rather than merely an algebraic multiplication map.

The constant product satisfies


\[
R_\lambda\bar\otimes R_\lambda\cong R_\lambda.
\tag{13}
\]


Here is the required isomorphism. On the product GNS spaces send the first copy's \(n\)-th leg to position \(2n-1\), and the second copy's \(n\)-th leg to position \(2n\). This map takes finite-support tensors to finite-support tensors, preserves their product inner products, and has a dense range with the inverse assignment. It extends to a unitary. It carries every local matrix algebra to its assigned leg, so it carries their generated von Neumann algebras onto each other. The faithful normal product representations in TS05 make (13) a normal isomorphism of the algebras themselves.

The ordinary Hilbert tensor flips and regrouping unitaries, (12) and (13), now give


\[
\begin{aligned}
M\bar\otimes R_\lambda
&\cong Q\bar\otimes(R_\lambda\bar\otimes R_\lambda)\\
&\cong Q\bar\otimes R_\lambda
\cong M.
\end{aligned}
\tag{14}
\]


Thus property \(H_\lambda\) implies the absorption assertion. No uniqueness theorem for all AFD factors of a given type is needed in this step: (12) identifies the specific constant product.

## 5. Tail blocks in an absorbed product

We prove the converse in the more general algebra \(B=N\bar\otimes R_\lambda\), where \(N\ne0\) is arbitrary. Choose a faithful normal concrete representation of \(N\) on \(H_N\), and the faithful product GNS representation of \(R_\lambda\). If \(K_m\) is the GNS space of its first \(m\) legs and \(L_m\) its pointed tail space, then


\[
H_B=H_N\otimes K_m\otimes L_m,
\]


with tail reference vector \(\Omega_{>m}\). Define the isometry \(V_m\zeta=\zeta\otimes\Omega_{>m}\). Compression by \(V_m\), followed by amplification with the tail identity, defines


\[
F_m(x)=(V_m^*xV_m)\otimes1_{L_m}.
\tag{15}
\]


This is a normal unital completely positive contraction onto \(N\bar\otimes A_m\), where \(A_m\) is the first \(m\)-leg matrix algebra. In fact compression is normal and completely positive. On a finite local product it evaluates exactly the factors after \(m\) in their product state, leaving an element of \(N\bar\otimes A_m\). Ultraweak density of the local product algebra and normality extend this range inclusion to every \(x\in B\). Amplification is normal, as can be checked on finite tensor vector coefficients and then their norm limits. Formula (15) fixes \(N\bar\otimes A_m\) and is bimodular over it; contractivity follows directly from \(V_m^*V_m=1\).

For every \(\varphi\in B_*\),


\[
\|\varphi-\varphi F_m\|\longrightarrow0.
\tag{16}
\]


To prove this in the full predual norm, use the summable vector-coefficient description in CP04–06. It approximates \(\varphi\) by finite sums of vector coefficients in the concrete representation. The union of the subspaces


\[
H_N\otimes K_m\otimes\mathbb C\Omega_{>m}
\]


is dense, by the definition of the pointed product. Thus those finite coefficients can in turn be approximated in functional norm by coefficients whose two vectors lie in one such subspace. Formula (15) fixes every such coefficient for all larger \(m\). Given an approximating functional \(\varphi_0\) with this property, contractivity gives


\[
\|\varphi-\varphi F_m\|
\le2\|\varphi-\varphi_0\|
\]


for all sufficiently large \(m\), proving (16). This argument uses neither a faithful normal state on \(N\) nor separability of \(H_N\).

Let \(u_k=e_{12}\) in the \(k\)-th product leg, acting as the identity on the other legs and on \(N\). For \(k>m\), the one-leg identity \(\omega_\lambda(u_k a)=\lambda\omega_\lambda(a u_k)\), checked in PS04, gives


\[
F_m(u_kx)=\lambda F_m(xu_k)\qquad(x\in B).
\tag{17}
\]


First check this on local products in (15), then use normality to pass to all \(B\). Consequently \(\varphi F_m\) has zero modular defect at \(u_k\), and


\[
\|\varphi u_k-\lambda u_k\varphi\|
\le(1+\lambda)\|\varphi-\varphi F_m\|
\qquad(k>m).
\tag{18}
\]


Equation (16) makes the defect tend to zero as \(k\to\infty\), for every normal functional. For a finite positive family, one sufficiently large \(k\) satisfies all prescribed tolerances. The operators \(u_k\) already have complementary initial and final projections. Thus \(B\) has \(H_\lambda\). Transport through a normal isomorphism proves that absorption implies \(H_\lambda\), and more generally that any algebra isomorphic to \(N\bar\otimes R_\lambda\) has it.

## 6. The vector criterion and the completed equivalence

Let \(\varphi_j\) be the normal positive functional represented by \(\xi_j\in\mathcal P\), and put \(c=\sqrt\lambda\). The earlier OH08 equivalence identifies \(H_\lambda\) with the following aggregate vector condition: for every \(s>0\), there is \(x\ne0\) such that


\[
\sum_j\|\xi_jx-cx\xi_j\|^2
\le s\sum_j\|x\xi_j\|^2.
\tag{19}
\]


Its hypotheses hold here because separable predual implies countable decomposability, as proved in OH06. That earlier argument includes nonfaithful functionals, extraction in the common null corner, full-support assembly, and the positive-mass bound needed for the reverse implication. Thus no faithfulness of the individual \(\varphi_j\)'s is added.

Condition (19) and the individual inequalities (2) are equivalent as qualitative conditions for all tolerances. Equation (19) with \(s=\varepsilon\) bounds each summand as in (2). Conversely apply (2) with tolerance \(s/n\), where \(n\) is the finite family's size, and add the inequalities. The family of size zero imposes no condition and may be omitted. This proves the equivalence of properties 2 and 3 in the theorem. Sections 1–5 prove the equivalence of properties 1 and 2, completing all three implications.

The separable-predual assumption is used to diagonalize the normal-state tests into the single commuting sequence in Section 3 and to invoke the stated corner and vector results. The absorbed-product implication in Section 5 holds without it. The range \(0<\lambda<1\) is essential to the vector theorem being used: at \(\lambda=1\), choosing \(x=1\) makes (2) automatic, so this formulation supplies no nontrivial absorption criterion.

## Source

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, §4, Theorem 4.1, printed pp.360–362 and 369–370. The proof above uses explicit positive matrix tests, the previously proved weighted splitting theorem, and the earlier programme's full corner and standard-form arguments.
