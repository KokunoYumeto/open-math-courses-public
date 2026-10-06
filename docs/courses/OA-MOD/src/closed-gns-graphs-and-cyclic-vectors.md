# Closed GNS graphs, cyclic vectors and bounded modular time

**Self-checked by the writing AI.**

A finite-domain Hilbert vector and its adjoint carry different information. We first prove which GNS graphs really are closed, and give a counterexample to a restricted-domain claim. We then construct the approximations behind cyclic-vector density, prove weak compactness of normal-functional order intervals, and explain why a bounded modular operator forces a finite trace.

The arguments use arbitrary Hilbert spaces and arbitrary von Neumann algebras. Sequences suffice for the explicitly constructed approximations; no countable dense subset of the representation space is assumed. Free comparisons for central comparison and the construction of a faithful normal state are Jesse Peterson’s [*Notes on von Neumann algebras*, Lemma 3.1.8, Proposition 3.1.9, Theorem 3.1.10 and Proposition 4.5.2, pages 43–44 and 67](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf). Both arguments are proved below. The general-weight input is the correspondence proved in WH02, WH04 and WH11, together with FL01. Those proofs reconstruct the bounded multiplication spaces from free Combes and Nelson sources and supply their analytic prerequisites. VT01 derives graph closure directly from the mixed multiplication identity. The remaining proofs use the exact programme results linked below; a free reference does not replace any invoked proof. The fixed-point step uses the full group theorem proved in the earlier programme note linked in VT10; its compactness and separation inputs have written local proofs.

## Two closed multiplication graphs and the necessary second vector

Let \(\varphi\) be a faithful normal semifinite weight on \(M\), and let \((H_\varphi,\pi_\varphi,\Lambda_\varphi)\) be its GNS triple. Use WH02 to identify \(M\) with its faithful normal GNS image. Write

\[
\begin{gathered}
\mathfrak n_\varphi=\{x:\varphi(x^*x)<\infty\},\\
\mathfrak a_\varphi=\mathfrak n_\varphi\cap\mathfrak n_\varphi^*,\qquad
\mathcal B_l=\Lambda_\varphi(\mathfrak n_\varphi).
\end{gathered}
\tag{VT.1}
\]

WH11 proves the last equality and the bijection
\(x\leftrightarrow\Lambda_\varphi(x)\), whose multiplier is \(x\).
For the right Hilbert algebra \(\mathcal A_r\), FL01 and WH04 give

\[
 x\eta=R_\eta\Lambda_\varphi(x)
 \quad(x\in\mathfrak n_\varphi,\ \eta\in\mathcal A_r).
\tag{VT.2}
\]

Every \(R_\eta\) here is bounded. The normality of the GNS representation used below is proved in WG007; the intrinsic vector seminorms are identified in CP08.

**Closed-graph theorem.** The map
\(\Lambda_\varphi:\mathfrak n_\varphi\to H_\varphi\) has a closed graph when \(M\) has its sigma-strong topology and \(H_\varphi\) its norm topology. Its inverse
\(\lambda:\mathcal B_l\to M\) has a closed graph when \(H_\varphi\) has its norm topology and \(M\) has the strong operator topology of this GNS representation. No uniform operator bound on the convergent net is required.

**Proof.** Suppose \(x_i\in\mathfrak n_\varphi\), \(x_i\to x\) sigma-strongly and \(\Lambda_\varphi(x_i)\to\xi\) in norm. The GNS representation is sigma-strong continuous: a vector seminorm after applying \(\pi_\varphi\) is the seminorm of the positive normal functional
\(a\mapsto\langle\pi_\varphi(a)\eta,\eta\rangle\). Thus \(x_i\eta\to x\eta\) for every \(\eta\in H_\varphi\). Passing to the limit in (VT.2) gives
\(R_\eta\xi=x\eta\) for every \(\eta\in\mathcal A_r\). This is exactly the left-boundedness criterion, with constant \(\|x\|\). Consequently \(\xi\in\mathcal B_l\), \(\lambda_\xi=x\), and WH11 gives \(x\in\mathfrak n_\varphi\) and \(\Lambda_\varphi(x)=\xi\).

For the inverse graph, suppose \(\xi_i\in\mathcal B_l\), \(\xi_i\to\xi\) and \(\lambda_{\xi_i}\to x\) strongly, with \(x\in M\). The same limit in
\(\lambda_{\xi_i}\eta=R_\eta\xi_i\) gives left boundedness and \(\lambda_\xi=x\). This proves the assertion for arbitrary nets. The graph is closed in the asserted ambient product spaces, even though neither domain need be closed in its own ambient space. \(\square\)

Restricting the first map to \(\mathfrak a_\varphi\) loses the information that \(x^*\) has finite energy. The corrected closed graph on that domain keeps both vectors:

\[
 \begin{gathered}
 \Gamma(x)=\bigl(\Lambda_\varphi(x),\\
 \Lambda_\varphi(x^*)\bigr),\qquad x\in\mathfrak a_\varphi.
 \end{gathered}
\tag{VT.3}
\]

This is a real-linear map into \(H_\varphi\oplus H_\varphi\), with closed graph for sigma-strong* convergence in \(M\) and norm convergence of both components. Apply the theorem separately to \(x_i\) and \(x_i^*\). The two limits prove both finite-domain memberships and both vector identities. Equivalently, the target can use the closed involution's graph norm on \(D(S)\). Hilbert-norm convergence of the first component alone is insufficient.

## A rank-one counterexample to the restricted GNS claim

On \(K=\ell^2(\mathbb N_0)\) with basis \(e_j\), put

\[
 h e_j=4^j e_j,\qquad
 \varphi(a)=\sum_{j\ge0}4^j\langle ae_j,e_j\rangle
 \quad(a\in B(K)_+).
\tag{VT.4}
\]

In (VT.4), \(h\) denotes the diagonal operator on the finite span of the basis; no closed extension is needed for this example. The weight is defined by the displayed nonnegative series, which is allowed to be infinite. It defines a faithful normal weight: increasing positive suprema commute with the increasing finite partial sums, and zero value forces every \(a^{1/2}e_j\) to vanish. It is semifinite because the finite-coordinate projections have finite weight, increase strongly to \(1\), and their matrix corners are ultraweakly dense.

The GNS space is the Hilbert–Schmidt completion of finite matrices, with
\(\Lambda_\varphi(x)\) represented by the matrix having columns
\(2^jxe_j\). Indeed its squared norm is
\(\sum_j4^j\|xe_j\|^2=\varphi(x^*x)\), and the finite matrix units span a dense Hilbert–Schmidt subspace.

Here is the completion argument explicitly. Identify a matrix with its entries indexed by \(\mathbb N_0\times\mathbb N_0\), with the square-sum norm. The completeness and finite-support density argument in OW09, with all coordinate weights equal to one, makes this a Hilbert space. Each element of the GNS domain gives a square-summable entry array by the displayed column formula. Conversely every finite entry array \((a_{ij})\) is the image of the finite matrix with entries \(2^{-j}a_{ij}\). This matrix is bounded and belongs to the finite domain. The image therefore contains a dense subspace of that Hilbert space, proving the asserted GNS completion.

Write \(\Lambda=\Lambda_\varphi\) in the following calculation. Let \(\Theta_{\xi,\eta}z=\langle z,\eta\rangle\xi\), let
\(\xi=\sum_{j\ge1}2^{-j}e_j\), and let \(\xi_N\) be its first \(N\) terms. Set \(x_N=\Theta_{\xi_N,e_0}\) and \(x=\Theta_{\xi,e_0}\). Then

\[
\begin{gathered}
 \|x_N-x\|=\|\xi_N-\xi\|\\
 \longrightarrow0,\\
 \|\Lambda(x_N)-\Lambda(x)\|
 =\|\xi_N-\xi\|\\
 \longrightarrow0,\\
 \varphi(x^*x)=\|\xi\|^2<\infty,\\
 \varphi(xx^*)=\sum_{j\ge1}1=\infty.
\end{gathered}
\tag{VT.5}
\]

The norm convergence here has the exact tail bound

\[
 \|\xi-\xi_N\|^2
 =\sum_{j>N}4^{-j}=\frac{4^{-N}}3.
\]

Indeed the sum from \(N+1\) through \(m\), multiplied by \(1-1/4\), telescopes to \(4^{-(N+1)}-4^{-(m+1)}\); let \(m\) tend to infinity. Each \(x_N\) belongs to \(\mathfrak a_\varphi\), but \(x\) does not. Operator-norm convergence implies sigma-strong* convergence. Therefore the graph of the restriction
\(\Lambda_\varphi|_{\mathfrak a_\varphi}\), with only Hilbert norm in its target, is not closed. The failure already occurs for a sequence, a type I algebra and a faithful weight. The full-domain graph and the multiplier inverse graph of VT01 remain valid. Also
\(\|\Lambda_\varphi(x_N^*)\|^2=N\); the missing second component is visibly responsible.

## Comparing two projections by their central supports

For projections \(r,s\in M\), write \(r\precsim s\) if there is a partial isometry \(w\in M\) with \(w^*w=r\) and \(ww^*\le s\).

Use the projection theorem BK01, the bicommutant theorem BK02, bounded polar decomposition BK07, and the strong convergence facts BK03–04. First construct the central carrier \(c(r)\). The closed subspace

\[
 K_r=\overline{\operatorname{span}}\,MrH
\tag{VT.6}
\]

reduces \(M\), so its projection commutes with \(M\). It also reduces \(M'\), since \(b'ar\xi=ar b'\xi\). Its projection therefore belongs to \(M\cap M'=Z(M)\). It dominates \(r\); any central projection dominating \(r\) contains this subspace. It is consequently the least such central projection.

If \(rMs=0\), taking adjoints gives \(sMr=0\), and
\(\langle ar\xi,bs\eta\rangle=0\) for every \(a,b,\xi,\eta\). Thus

\[
 rMs=0\quad\Longrightarrow\quad c(r)c(s)=0.
\tag{VT.7}
\]

**Central comparison lemma.** There is a central projection \(z\) such that

\[
 zr\precsim zs,\qquad (1-z)s\precsim(1-z)r.
\tag{VT.8}
\]

**Proof.** Choose a maximal family \((w_i)\) of nonzero partial isometries having mutually orthogonal initial projections under \(r\) and mutually orthogonal final projections under \(s\). The maximal principle applies because a union of a chain of such families still has these properties. Their finite sums and adjoints converge strongly: the squared norm of each vector's tail is the sum of the squared norms of its orthogonal components. The sums are contractions, and their strong limits \(w,w^*\) belong to \(M\). Put

\[
 r_0=r-w^*w,\qquad s_0=s-ww^*,\qquad
 z=1-c(r_0).
\tag{VT.9}
\]

If \(s_0Mr_0\ne0\), the polar decomposition of a nonzero element of this corner supplies another partial isometry, contradicting maximality. Hence (VT.7) makes the central carriers of \(r_0,s_0\) orthogonal. On \(z\), \(r_0=0\), so \(zw\) has initial projection \(zr\) and final projection at most \(zs\). On \(1-z=c(r_0)\), \(s_0=0\), so \((1-z)w^*\) has initial projection \((1-z)s\) and final projection at most \((1-z)r\). This proves (VT.8). The empty family handles a zero corner. \(\square\)

The argument proves central comparison directly from the bicommutant, projections, polar decomposition and the maximal principle. It invokes no classification of von Neumann algebras.

## The sigma-strong closure of the unitaries

**Theorem.** The sigma-strong closure of \(U(M)\) is exactly the set of isometries \(v\in M\), meaning \(v^*v=1\).

A strong limit of unitaries preserves every vector norm, so is an isometry. Since the unitary net is norm bounded, strong and sigma-strong convergence agree by CP08. It remains to approximate an arbitrary isometry.

Put \(d=1-vv^*\), \(d_j=v^jdv^{*j}\), and

\[
 p_s=\sum_{j\ge0}d_j,\qquad p_u=1-p_s.
\tag{VT.10}
\]

The \(d_j\)'s are pairwise orthogonal: for \(k>j\), the product contains
\(dv^{k-j}=0\). The relation \(vd_jv^*=d_{j+1}\) gives
\(vp_sv^*=p_s-d\). Consequently \(p_u\) reduces \(v\), and \(vp_u\) is unitary in \(p_uMp_u\). These statements can also be checked on the orthogonal sum of the \(d_jH\)'s and its complement: \(v\) sends the \(j\)-th subspace isometrically onto the next, \(v^*\) sends the next back, and \(v^*dH=0\).

For \(n\ge1\), set \(t_n=p_s-\sum_{j=0}^nd_j\) and define

\[
 \begin{aligned}
 u_n&=v\sum_{j=0}^{n-1}d_j\\
 &\quad+v^{*n}d_n\\
 &\quad+t_n+vp_u.
 \end{aligned}
\tag{VT.11}
\]

The first two terms cyclically permute \(d_0H,\ldots,d_nH\), using \(v\) on each forward edge and \(v^{*n}\) on the returning edge. The remaining terms act as the identity on \(t_nH\) and as \(v\) on \(p_uH\). The initial spaces are orthogonal and sum to \(H\), as do the final spaces. Thus \(u_n^*u_n=u_nu_n^*=1\).

On any fixed finite sum of the \(d_jH\)'s, \(u_n=v\) for all sufficiently large \(n\). On the unitary part they always agree. More explicitly,

\[
 \|(u_n-v)\xi\|
 \le2\left\|\left(p_s-\sum_{j=0}^{n-1}d_j\right)\xi\right\|
 \longrightarrow0.
\tag{VT.12}
\]

The projection tails decrease strongly to zero. This proves strong, hence sigma-strong, convergence. No separability of the defect subspace was used. \(\square\)

## Invertibles are sigma-strongly dense

**Theorem.** \(GL(M)\) is sigma-strongly dense in \(M\). In fact each \(x\in M\) has a norm-bounded sequence of invertible approximants converging strongly.

First approximate a coisometry \(v^*\), where \(v\) is the isometry used in VT04. With any \(0<\varepsilon_n\le1\) tending to zero, set

\[
 b_n=
 v^*\sum_{j=1}^nd_j+
 \varepsilon_n v^nd_0+t_n+v^*p_u.
\tag{VT.13}
\]

On the finite shift block, this moves each \(d_jH\) back one place and moves \(d_0H\) to \(d_nH\) with the nonzero weight \(\varepsilon_n\). The inverse in \(M\) is

\[
 \begin{aligned}
 b_n^{-1}&=v\sum_{j=0}^{n-1}d_j\\
 &\quad+\varepsilon_n^{-1}v^{*n}d_n\\
 &\quad+t_n+vp_u.
 \end{aligned}
\tag{VT.14}
\]

Multiplying on each of the four orthogonal parts verifies both inverse identities. Their finite-block norms give \(\|b_n\|\le1\), and

\[
 \|(b_n-v^*)\xi\|
 \le\varepsilon_n\|d_0\xi\|+2\|t_n\xi\|
 \longrightarrow0.
\tag{VT.15}
\]

Here \(v^*\) already agrees with \(b_n\) on \(d_jH\) for \(1\le j\le n\), and on \(p_uH\). The inverse norms can diverge; no uniform bound on them is asserted.

Now write \(x=a|x|\), with \(a\) its polar partial isometry, initial projection \(p\) and final projection \(q\). Apply the construction in VT03 to \(r=1-p\), \(s=1-q\). Its partial isometry \(w\), lying in \(sMr\), has the property that for its central projection \(z\),

\[
 V=a+w,\qquad
 (zV)^*(zV)=z,\qquad
 ((1-z)V)((1-z)V)^*=1-z,\qquad
 V|x|=x.
\tag{VT.16}
\]

Indeed \(a,w\) have orthogonal initial and final spaces. On \(z\), the initial residual \(r_0\) is zero; on \(1-z\), the final residual \(s_0\) is zero. Also \(w|x|=0\), since \(|x|=p|x|\).

The central corners have their inherited von Neumann algebra topologies by CP11. In \(zM\), VT04 gives unitary approximants to the isometry \(zV\). In \((1-z)M\), (VT.13) gives invertible contraction approximants to the coisometry \((1-z)V\). Their central direct sums \(V_n\) are invertible contractions in \(M\), converge strongly to \(V\), and have bounded inverses individually. Therefore

\[
 \begin{gathered}
 x_n=V_n(|x|+n^{-1}1),\\
 x_n\in GL(M),\\
 x_n\longrightarrow x\ \text{strongly},\\
 \|x_n\|\le\|x\|+1.
 \end{gathered}
\tag{VT.17}
\]

The positive factor has an inverse by continuous functional calculus. Convergence follows by testing the fixed vector \(|x|\xi\) in \(V_n\to V\), with the additional term at most \(n^{-1}\|\xi\|\). CP08 upgrades the bounded strong convergence to sigma-strong convergence. This proves the theorem, including either zero central summand. \(\square\)

The theorem concerns sigma-strong topology. It does not assert norm density: the unilateral shift is a useful test of this distinction.

## Cyclic vectors form a dense \(G_\delta\) when one exists

A vector \(\xi\) is cyclic for \(M\subseteq B(H)\) if
\(\overline{M\xi}=H\). If there is no cyclic vector, the cyclic set is empty and is itself a \(G_\delta\). Otherwise fix one, \(\xi_0\). For \(n\ge1\), let

\[
 O_n=\bigcup_{a\in M}
 \{\xi\in H:\|a\xi-\xi_0\|<1/n\}.
 \qquad
 \operatorname{Cyc}(M,H)=\bigcap_{n\ge1}O_n.
\tag{VT.18}
\]

Each set in the union is open, hence \(O_n\) is open. If \(\xi\) is cyclic, it lies in every \(O_n\). Conversely membership in the intersection puts \(\xi_0\) in \(K=\overline{M\xi}\). This subspace reduces \(M\): it is invariant under every element and its adjoint. Since \(\xi_0\) is cyclic, \(K=H\). This proves (VT.18).

Every \(a\xi_0\) with \(a\in GL(M)\) is cyclic. For its cyclic subspace, \(a^{-1}(a\xi_0)=\xi_0\), so the preceding argument applies. VT05 gives

\[
 \overline{GL(M)\xi_0}
 \supseteq M\xi_0,\qquad
 \overline{GL(M)\xi_0}=H.
\tag{VT.19}
\]

Thus the cyclic set is dense, and each \(O_n\) is dense. No countable dense list of target vectors was needed: the single cyclic vector furnishes the countable intersection.

For later use, the projection theorem in BK01 and the bicommutant theorem BK02 give the following equivalence: \(\xi\) is cyclic for \(M\) exactly when it is separating for \(M'\). Indeed the projection onto \(\overline{M\xi}\) belongs to \(M'\). If \(\xi\) is separating, its complementary projection kills \(\xi\) and must be zero. Conversely an element of \(M'\) killing a cyclic vector kills \(M\xi\), and therefore all of \(H\). This argument applies to arbitrary representations.

## Cyclic separating vectors for two properly infinite algebras

Assume \(M,M'\) are sigma-finite and properly infinite, in a nonzero representation. Sigma-finite means that every orthogonal family of nonzero projections is countable. Proper infiniteness here means that the identity contains two orthogonal subprojections each equivalent to the identity.

We first justify the two existence steps. A sigma-finite von Neumann algebra \(N\) has a faithful normal state. Choose a maximal orthogonal family of supports of nonzero positive normal functionals. If its supports failed to sum to \(1\), a nonzero remaining projection would support a nonzero vector functional: compress a vector with nonzero image under that projection. The least-support assertion CP12 puts its support in the remaining corner, contradicting maximality. CP12 proves this assertion for bounded normal functionals using their null projections; no general infinite-valued weight-support theorem is needed here. Sigma-finiteness makes the family countable. Normalize its members to states \(\rho_j\), and choose positive numbers \(\alpha_j\) summing to \(1\). Then

\[
 \rho=\sum_j\alpha_j\rho_j
\tag{VT.20}
\]

converges in predual norm, is normal and is a state. To justify the limit, CP07 gives \(\|\rho_j\|=\rho_j(1)=1\). For finite partial sums with \(m>n\),

\[
 \left\|\sum_{j=n+1}^{m}\alpha_j\rho_j\right\|
 \leq\sum_{j=n+1}^{m}\alpha_j.
\]

The scalar tails tend to zero, so completeness of the concrete predual in CP06 gives a norm limit in that predual. Evaluation on positive elements preserves positivity in the limit; evaluation at the identity gives one. Thus the limit is indeed a normal state. If \(\rho(a)=0\), \(a\ge0\), all \(\rho_j(a)=0\). By CP12, \(\rho_j(a)=\rho_j(p_jap_j)\). Faithfulness on that support corner gives \(p_jap_j=0\), hence \(a^{1/2}p_j=0\), since the squared norm of \(a^{1/2}p_j\xi\) is \(\langle p_jap_j\xi,\xi\rangle\). Here \(p_j\) denotes each support. Their supremum is \(1\), so \(a=0\). A finite family uses any strictly positive finite list of coefficients.

Proper infiniteness supplies isometries \(v_1,v_2\in M\) with orthogonal ranges. Put \(w_j=v_2^{j-1}v_1\); then

\[
 w_j^*w_k=\delta_{jk}1.
\tag{VT.21}
\]

For \(j<k\), the cross term contains \(v_1^*v_2^{k-j}=0\); diagonal terms are \(1\). Their final projections need not sum to \(1\).

Apply (VT.20) to \(M'\), obtaining a faithful normal state \(\rho\). CP08 supplies a positive normal functional
\(\theta(y)=\sum_j\langle y\eta_j,\eta_j\rangle\ge\rho(y)\) on \(M'_+\), with \(\sum_j\|\eta_j\|^2<\infty\). Thus \(\theta\) is faithful. The norm-convergent vector
\(\zeta=\sum_jw_j\eta_j\) satisfies

\[
 \begin{gathered}
 \langle y\zeta,\zeta\rangle\\
 =\sum_j\langle y\eta_j,\eta_j\rangle\\
 =\theta(y)\qquad(y\in M').
 \end{gathered}
\tag{VT.22}
\]

For clarity, (VT.21) gives the tail identity

\[
 \left\|\sum_{j=n+1}^{m}w_j\eta_j\right\|^2
 =\sum_{j=n+1}^{m}\|\eta_j\|^2.
\]

Hilbert-space completeness therefore supplies \(\zeta\). For each finite sum, commutation and (VT.21) eliminate all cross terms in (VT.22). Its vector coefficient tends to the coefficient of \(\zeta\) by boundedness of \(y\), and the scalar series converges absolutely since its terms are bounded in magnitude by \(\|y\|\|\eta_j\|^2\). This proves (VT.22) for every \(y\in M'\), not just positive elements. Its vector functional is faithful, so \(\zeta\) is separating for \(M'\), hence cyclic for \(M\).

Interchanging \(M,M'\) produces a cyclic vector for \(M'\), equivalently a separating vector for \(M\). VT06 makes each of these two sets a dense \(G_\delta\) in \(H\). Their intersection is dense by Baire's theorem AB03: in any nonempty open subset of a complete metric space, a countable intersection of dense open sets is dense. Its points are precisely the cyclic separating vectors for \(M\). This proves the full assertion without requiring \(H\) to be separable. \(\square\)

## Normal-functional order intervals are weakly compact

Let \(\varphi,\psi\in M_*^{\rm sa}\) with \(\varphi\le\psi\), and put \(\nu=\psi-\varphi\ge0\). The weak topology on the Banach space \(M_*\) is \(\sigma(M_*,M)\), using the exact onto duality CP06. It is not an unspecified weak-star topology.

Let \((H_\nu,\pi_\nu,\Omega_\nu)\) be the normal bounded-functional GNS representation. For

\[
 C_\nu=\{T\in\pi_\nu(M)':0\le T\le1\},
\tag{VT.23}
\]

set

\[
 \rho_T(a)=
 \langle\pi_\nu(a)T^{1/2}\Omega_\nu,T^{1/2}\Omega_\nu\rangle
 =\langle\pi_\nu(a)T\Omega_\nu,\Omega_\nu\rangle.
\tag{VT.24}
\]

This is a normal positive functional and \(0\le\rho_T\le\nu\). Conversely every \(0\le\rho\le\nu\) has the unique operator \(T\in C_\nu\) given by DW03, since both functionals have finite domain all of \(M\). Evaluate its pairing at \(a\) and \(1\) to obtain (VT.24). No faithfulness of \(\nu\) is assumed.

The set \(C_\nu\) is ultraweakly closed inside the operator unit ball: commutation is a family of closed coefficient equalities, and both positive inequalities are families of closed quadratic-form inequalities. The written Banach–Alaoglu proof AB05, applied to the concrete predual and its onto dual identification CP06, makes the ball compact. The map \(T\mapsto\rho_T\) is continuous from this topology to \(\sigma(M_*,M)\), because for fixed \(a\) its second expression is a single ultraweakly continuous vector coefficient of \(T\). Hence \([0,\nu]\) is weakly compact as its image. Translation gives

\[
 [\varphi,\psi]
 =\varphi+[0,\psi-\varphi],
 \qquad
 [\varphi,\psi]\ \text{weakly compact in }M_*.
\tag{VT.25}
\]

The zero functional gives the singleton interval, so the degenerate case is included. This compactness step in \(M_*\) is supplied by the preceding AB05 proof. \(\square\)

## A bounded modular operator bounds every unitary orbit state

Let \(\varphi\) be a faithful normal state, \(\Omega=\Lambda_\varphi(1)\), and

\[
 S=\overline{(x\Omega\mapsto x^*\Omega)}
   =J\Delta^{1/2},\qquad C=\|\Delta\|<\infty.
\tag{VT.26}
\]

Here are the precise prerequisites for this state case. WG006–007 construct the normal GNS representation, and WH02 identifies its faithful image as a von Neumann algebra. Because the state is bounded, its finite domain is all of \(M\), so \(M\Omega=\Lambda_\varphi(M)\) is dense. If \(x\Omega=0\), then \(\varphi(x^*x)=0\); faithfulness gives \(x=0\). Thus \(\Omega\) is cyclic and separating. TC04–05 prove closability of this involution, TC07 constructs its positive operator and exact square-root domain, and TC08 proves that \(J\) is antiunitary. Consequently
\(\|S\xi\|^2=\|\Delta^{1/2}\xi\|^2\le C\|\xi\|^2\) on its domain. Boundedness of \(\Delta\) makes that domain all of \(H_\varphi\). In particular

\[
 \varphi(xx^*)\le C\varphi(x^*x)
 \quad(x\in M),\qquad C\ge1.
\tag{VT.27}
\]

The last inequality follows by taking \(x=1\), whose state value is \(1\).

For \(u\in U(M)\), define \(\varphi_u(a)=\varphi(u^*au)\). Apply (VT.27) to \(x=u^*a^{1/2}\) to get the upper bound. Apply the same upper bound for \(u^*\) to the positive element \(u^*au\) to get the lower bound. Thus

\[
 C^{-1}\varphi\le\varphi_u\le C\varphi.
\tag{VT.28}
\]

This argument keeps the squared norm and the orientation of \(u\) visible; replacing \(C\) by a square of \(C\) is unnecessary.

Let \(K\) be the weak closure of the convex hull of the orbit states. Positive inequalities are weakly closed, being tests on every \(a\in M_+\). VT08 therefore gives

\[
 K\subseteq[C^{-1}\varphi,C\varphi],\qquad
 K\text{ is nonempty, convex and weakly compact}.
\tag{VT.29}
\]

Every point of \(K\) is a normal state, because positivity and evaluation at \(1\) persist under weak closure. The interval lower bound makes all these states faithful.

## The fixed-point step yields a faithful normal finite trace

We use the following earlier programme theorem, registered as **OA-MOD-VT-DEP-RYLL** and proved in *A written fixed-point proof for affine isometries*, Theorem 5.1:

> On a nonempty weakly compact convex subset of a Banach space, a group of weakly continuous affine norm isometries preserving the set has a common fixed point.

The linked note proves the compact-face and small-cap lemmas, produces a fixed point of each finite average, proves that each averaged isometry fixes that point, and applies compactness to all group elements. Its only analytic inputs are the written Hahn–Banach/separation, dual completeness and uniform-boundedness proofs. The countable subgroup used inside the finite-average argument imposes no countability assumption on the acting group or on the Banach space.

For \(u\in U(M)\), define

\[
 (\alpha_u\rho)(a)=\rho(u^*au).
\tag{VT.30}
\]

These maps satisfy \(\alpha_u\alpha_v=\alpha_{uv}\), since
\(v^*u^*a uv=(uv)^*a(uv)\). Each is linear, preserves normal functionals and is weakly continuous: evaluation at \(a\) after the map is evaluation at \(u^*au\) before it. Also

\[
 \|\alpha_u\rho-\alpha_u\eta\|
 =\|\rho-\eta\|.
\tag{VT.31}
\]

Indeed conjugation bijects the operator unit ball onto itself, so the suprema defining the two functional norms agree. The maps permute the orbit of \(\varphi\), and therefore preserve its convex hull and weak closure \(K\).

All hypotheses of the written fixed-point theorem hold. It gives \(\tau\in K\) with \(\tau(u^*au)=\tau(a)\) for every unitary \(u\). The bounds in (VT.29) imply that \(\tau\) is faithful, normal and a state.

To prove it is tracial, fix \(h=h^*\in M\). Norm differentiation of the exponential series at \(t=0\), followed by boundedness of \(\tau\), gives

\[
 \begin{gathered}
 f_h(t)=\tau(e^{-ith}ae^{ith}),\\
 0=f_h'(0)=i\tau(ah-ha),\\
 \tau(ab)=\tau(ba)\quad(a,b\in M).
 \end{gathered}
\tag{VT.32}
\]

The second assertion follows by writing \(b\) as the sum of a self-adjoint part and \(i\) times a self-adjoint part. The remainder after the linear term is \(O(t^2)\). For completeness, the continuous functional calculus in BK01 makes \(e^{ith}\) unitary for real \(t\). Its absolutely convergent series satisfies

\[
 \|e^{ith}-1-ith\|
 \le \tfrac12 |t|^2\|h\|^2 e^{|t|\|h\|}.
\]

Indeed \(k!\ge 2(k-2)!\) for \(k\ge2\); sum the norm bounds for the terms of order at least two. Apply the same bound to \(-t\). Multiplying the two expansions around \(a\) gives

\[
 e^{-ith}ae^{ith}=a+it(ah-ha)+O(t^2)
\]

in operator norm, which proves the derivative used in (VT.32).

Thus a bounded modular operator of a faithful normal state implies the existence of a faithful normal finite trace, indeed a tracial state. The trace is comparable to the starting state. The fixed-point theorem used in this deduction is proved in full in the note linked above.

## Solved checks for topology, cyclicity and trace bounds

**The returning edge of a shift.** Let \(v\) be the unilateral shift on \(\ell^2(\mathbb N_0)\). Its defect \(d_j\) is the projection onto \(e_j\), and \(p_u=0\). Formula (VT.11) is the cyclic permutation of \(e_0,\ldots,e_n\) followed by the identity on the tail. It sends any fixed \(e_j\) to \(e_{j+1}\) for sufficiently large \(n\), but
\(u_ne_n=e_0\). The discrepancy on the moving last coordinate prevents operator-norm convergence.

Formula (VT.13) gives

\[
 \begin{gathered}
 b_ne_0=\varepsilon_ne_n,\\
 b_ne_j=e_{j-1}\ (1\le j\le n),\\
 b_ne_j=e_j\ (j>n),\\
 \|b_n^{-1}\|=\varepsilon_n^{-1}.
 \end{gathered}
\tag{VT.33}
\]

For every fixed vector, the returning-edge term tends to zero and the tail norm tends to zero. Hence \(b_n\to v^*\) strongly with \(\|b_n\|=1\). This verifies why invertibles can approximate a coisometry while unitaries cannot: a strong limit of unitaries preserves vector norms, whereas \(v^*e_0=0\).

**An uncountable diagonal representation.** Let \(I\) be uncountable and let \(M=\ell^\infty(I)\) act on \(\ell^2(I)\). Every vector has countable support: for each positive integer \(n\), the coordinates of magnitude at least \(1/n\) form a finite set; their union contains the nonzero coordinates. Multiplication cannot create a coordinate outside that support. Thus no vector is cyclic, consistently with the empty \(G_\delta\) branch in VT06. For \(I=\mathbb N\), a vector is cyclic exactly when all coordinates are nonzero: coordinate projections generate the basis vectors after rescaling, while a zero coordinate cannot be generated. This is the countable intersection of the open dense conditions \(\xi_j\ne0\). The countability appears in this example's index set, not in the general proof.

**A nontracial state with bounded modular operator.** On \(M_2(\mathbb C)\), let \(D=\operatorname{diag}(1/5,4/5)\), and let \(\varphi(a)=\operatorname{Tr}(Da)\). We derive its modular operator directly. On the four-dimensional matrix space use \(\langle X,Y\rangle=\operatorname{Tr}(Y^*X)\) and \(\Lambda(x)=xD^{1/2}\). The finite-sum identity
\(\operatorname{Tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=\operatorname{Tr}(BA)\)
gives

\[
 \langle\Lambda(x),\Lambda(y)\rangle
 =\operatorname{Tr}(Dy^*x)=\varphi(y^*x).
\]

All diagonal entries of \(D\) are positive, so this map is onto the matrix space and \(\Omega=D^{1/2}\) is cyclic and separating for left multiplication. Thus the Tomita operator is everywhere defined:

\[
 \begin{aligned}
 S(X)&=D^{-1/2}X^*D^{1/2},\\
 J(X)&=X^*,\\
 A(E_{ij})&=\sqrt{D_{ii}/D_{jj}}\,E_{ij}.
 \end{aligned}
\]

The finite-matrix inner product, its completeness and the positive density representation are proved by finite sums in OW10. The matrix units are an orthonormal basis. Therefore \(A\) is positive and invertible, \(J\) is antiunitary, and direct substitution gives \(S=JA\). The uniqueness proved in TC08 identifies \(\Delta=A^2\). In this Hilbert–Schmidt GNS model, \(\Delta(X)=DXD^{-1}\). Its eigenvalues on the matrix units are the ratios \(D_{ii}/D_{jj}\), so \(C=4\). Conjugating \(D\) by the swapping unitary gives \(\operatorname{diag}(4/5,1/5)\). Averaging the original and swapped states yields

\[
 \tau(a)=\tfrac12\operatorname{Tr}(a),\qquad
 \tfrac14\varphi\le\tau\le4\varphi.
\tag{VT.34}
\]

The inequalities can be checked on diagonal densities: the density of \(\tau-\varphi/4\) is \(\operatorname{diag}(9/20,3/10)\), and that of \(4\varphi-\tau\) is \(\operatorname{diag}(3/10,27/10)\). Both are positive, so the order equivalence proved in OW10 gives the functional inequalities. This exhibits a trace in \(K\); it does not say that the original state was a trace. The displayed matrix-unit calculation supplies the modular formula within this lesson.

VT01–02 distinguishes the full finite-domain GNS graph from its restricted-domain version. VT03–10 proves central comparison, the approximation and cyclic \(G_\delta\) statements at arbitrary Hilbert-space cardinality, weak compactness of normal-functional intervals, and the trace deduction using the earlier written affine fixed-point theorem. The bounded-functional support, compactness, state polar and finite-matrix steps now identify or supply their exact written proofs. The general-weight proofs in WH02, WH04, WH11 and FL01 supply the exact multiplication domains and identities used here. In particular the graph argument retains arbitrary nets, and none of the approximation or fixed-point arguments assumes a separable Hilbert space.
