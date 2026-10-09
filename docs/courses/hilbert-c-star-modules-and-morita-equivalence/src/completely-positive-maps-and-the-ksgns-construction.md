# Completely positive maps and the KSGNS construction

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A positive functional constructs a Hilbert space by assigning a squared length to an element of an algebra. A completely positive map with values in adjointable operators does the same for vectors carrying coefficients in another C*-algebra. Its dilation represents the original algebra on a larger Hilbert module and recovers the map by compression. The extra issue is whether the compression operator is adjointable. For a nonunital domain, strictness supplies precisely what the minimal construction needs.

We prove the construction, its uniqueness and its application to conditional expectations. We then identify the modules for matrix traces and reduced crossed products, and prove the stabilized dilation used in extension theory. Inner products are conjugate linear in their first variable. All tensor products in the initial construction are algebraic tensor products over \(\mathbb C\).

The prerequisites are *Hilbert C*-modules*, *Adjointable operators*, *Compact operators, multipliers and the strict topology*, and *Tensor products and C*-correspondences*. We use the positive-map and Hilbert-space representation results from *Completely positive maps* and *Representations and positive functionals: the GNS construction and the Gelfand–Naimark theorem*. Stabilization enters only in Section 8.

## 1. Strict maps and the dilation theorem

Let \(A,B\) be C*-algebras and \(E\) a Hilbert \(B\)-module. A linear map \(\phi:A\to\mathcal L(E)\) is completely positive if each entrywise map on matrices is positive. Such a map is bounded and preserves adjoints; these are [*Completely positive maps*, Proposition 3.2]. No unitality is assumed.

On bounded subsets of \(\mathcal L(E)\), strict convergence \(T_\lambda\to T\) is equivalent to
\[
T_\lambda x\longrightarrow Tx,
\qquad T_\lambda^*x\longrightarrow T^*x
\quad(x\in E).
\tag{1.1}
\]
This is the strict topology of \(M(\mathcal K(E))\), as proved in *Compact operators, multipliers and the strict topology*. A completely positive map is **strict** if \(\phi(e_\lambda)\) converges strictly to an element \(H\in\mathcal L(E)\) for an approximate identity of positive contractions of \(A\). We use whichever positive contractive approximate identity has this strict limit; it need not be increasing. Lemma 2.2 constructs the dilation directly from that identity, and the end of Section 2 proves that every positive contractive approximate identity then has the same limit. We call \(\phi\) **nondegenerate** when this limit is \(1_E\).

**Theorem 1.1 (Kasparov–Stinespring–GNS).** If \(\phi:A\to\mathcal L(E)\) is strict and completely positive, there are a Hilbert \(B\)-module \(F\), a nondegenerate *-homomorphism \(\pi:A\to\mathcal L(F)\), and \(V\in\mathcal L(E,F)\) such that
\[
\phi(a)=V^*\pi(a)V,
\qquad
F=\overline{\operatorname{span}}\{\pi(a)Vx:a\in A, x\in E\}.
\tag{1.2}
\]
Moreover \(V^*V=H\) and \(\|V\|^2=\|\phi\|\). The dilation is unique up to a unitary intertwining both the representation and \(V\). If \(\phi\) is nondegenerate, \(V\) identifies \(E\) with a complemented submodule of \(F\).

The density requirement in (1.2) is called **minimality**. The theorem is [Blackadar 2006, II.7.5.2]; Sections 2 and 3 prove it. A unital map on a unital algebra is nondegenerate. A strict map need not be: for example, one half of a unital *-homomorphism has limit \(\tfrac12 1_E\).

## 2. The positive kernel and the compression operator

On \(A\odot E\) use the right action \((a\otimes x)b=a\otimes xb\), and define
\[
\langle a\otimes x,c\otimes y\rangle_\phi
=\langle x,\phi(a^*c)y\rangle_B.
\tag{2.1}
\]
Bilinearity of the tensor relations makes this well defined. It is sesquilinear, right \(B\)-linear in the second variable, and conjugate symmetric because \(\phi\) preserves adjoints.

**Lemma 2.1.** Formula (2.1) is positive semidefinite. Its null space is a right submodule orthogonal to the whole algebraic tensor product; the null quotient completes to a Hilbert \(B\)-module \(F\).

*Proof.* For \(z=\sum_{i=1}^n a_i\otimes x_i\), the matrix \([a_i^*a_j]\) is positive in \(M_n(A)\): it is the Gram matrix of the row \((a_1,\ldots,a_n)\). Complete positivity gives
\[
M=[\phi(a_i^*a_j)]\geq0
\quad\hbox{in }\mathcal L(E^n).
\tag{2.2}
\]
For the column \(x=(x_1,\ldots,x_n)\in E^n\),
\[
\langle z,z\rangle_\phi
=\langle x,Mx\rangle
=\langle M^{1/2}x,M^{1/2}x\rangle\geq0.
\tag{2.3}
\]
Thus positivity is \(B\)-valued, not merely positivity after a particular scalar state.

The semi-inner-product Cauchy–Schwarz argument of *Hilbert C*-modules* gives
\(\|\langle z,w\rangle_\phi\|\leq\|z\|_\phi\|w\|_\phi\), where \(\|z\|_\phi=\|\langle z,z\rangle_\phi\|^{1/2}\). Consequently every vector of zero seminorm is orthogonal to every vector. The null space is linear, and \(\|zb\|_\phi\leq\|z\|_\phi\|b\|\) makes it a right submodule. The quotient therefore has a definite inner product. Its completion carries the continuous extension of the right action and of the inner product, and is a Hilbert module. ∎

Write \([z]\) for the image of an algebraic tensor in \(F\). Define left multiplication by
\[
\pi(c)[a\otimes x]=[ca\otimes x].
\tag{2.4}
\]
To check boundedness, let \(z=\sum_i a_i\otimes x_i\). In the unitization of \(A\), the element \(\|c\|^2 1-c^*c\) is positive. Hence the matrix
\([a_i^*(\|c\|^2 1-c^*c)a_j]\) is positive in \(M_n(A)\). Apply complete positivity and then its quadratic form on \(E^n\) to get
\[
\langle\pi(c)z,\pi(c)z\rangle_\phi
\leq\|c\|^2\langle z,z\rangle_\phi.
\tag{2.5}
\]
So (2.4) preserves the null space and extends boundedly, with norm at most \(\|c\|\). Directly from (2.1), its adjoint is \(\pi(c^*)\); multiplication is also preserved. Thus \(\pi\) is a *-homomorphism into \(\mathcal L(F)\).

For an approximate identity \((e_\lambda)\), \(e_\lambda a\to a\). The estimate
\[
\|[a\otimes x]\|\leq\|\phi\|^{1/2}\|a\|\|x\|
\tag{2.6}
\]
shows that \(\pi(e_\lambda)\) tends pointwise to the identity on the dense elementary tensors. Its uniform boundedness extends this convergence to all of \(F\). In particular, \(\pi\) is nondegenerate.

**Lemma 2.2.** Let \((e_\lambda)\) be any positive contractive approximate identity for which \(\phi(e_\lambda)\to H\) strictly. Then
\[
Vx=\lim_\lambda[e_\lambda\otimes x]
\tag{2.7}
\]
exists and defines an adjointable map \(E\to F\). Its adjoint on elementary tensors is
\[
V^*[a\otimes y]=\phi(a)y.
\tag{2.8}
\]

*Proof.* We first obtain an order bound from the given strict limit. If \(a\in A\) is a positive contraction, then
\[
0\leq e_\lambda a e_\lambda
\leq e_\lambda^2\leq e_\lambda.
\]
Moreover \(e_\lambda a e_\lambda\to a\) in norm. Thus, for each \(x\in E\), the positive elements
\(\langle x,(\phi(e_\lambda)-\phi(e_\lambda a e_\lambda))x\rangle_B\)
converge in norm to \(\langle x,(H-\phi(a))x\rangle_B\). The positive cone is closed, and the quadratic-form positivity criterion [*Adjointable operators*, Theorem 3.1] gives
\[
H\geq\phi(a)\geq0
\quad(0\leq a\leq1).
\]
Taking \(a=0\) also proves positivity of \(H\).

Let \(A^\dagger=A\oplus\mathbb C\) be the **forced unitization**, adjoining a new unit even if \(A\) already has one. Define the linear map
\[
\Psi:A^\dagger\longrightarrow\mathcal L(E),
\qquad
\Psi(a+t1)=\phi(a)+tH.
\]
This map is positive. Indeed, if \(a+t1\geq0\), its scalar quotient satisfies \(t\geq0\), and \(a=a^*\). Write \(a=a_+-a_-\), with \(a_\pm\in A_+\) by functional calculus. Positivity of \(a+t1\) implies \(\|a_-\|\leq t\). When \(t>0\), the preceding bound applied to \(a_-/t\) gives \(\phi(a_-)\leq tH\); consequently
\[
\Psi(a+t1)
=\phi(a_+)+tH-\phi(a_-)\geq0.
\]
When \(t=0\), \(a\geq0\) and the assertion is just positivity of \(\phi\). Only positivity of \(\Psi\) is needed here.

For arbitrary indices \(\lambda,\nu\), put \(p=1-e_\lambda\) and \(q=1-e_\nu\) in \(A^\dagger\). These are positive contractions. Since \((p+q)^2\geq0\), and \(p^2\leq p,\ q^2\leq q\), we have
\[
\begin{aligned}
(e_\lambda-e_\nu)^2
&=(p-q)^2\\
&\leq2(p^2+q^2)\\
&\leq2(p+q).
\end{aligned}
\]
No commutativity or ordering of the two indices is used. Apply \(\Psi\) to this inequality. Its value on the left is \(\phi((e_\lambda-e_\nu)^2)\), while its value on the right is \(2(2H-\phi(e_\lambda)-\phi(e_\nu))\). Set
\(D_{\lambda,\nu}=2H-\phi(e_\lambda)-\phi(e_\nu)\geq0\).
Write \(z_\lambda=[e_\lambda\otimes x]\) and \(d_{\lambda,\nu}=e_\lambda-e_\nu\). Formula (2.1) and monotonicity of the norm on positive elements now give
\[
\begin{aligned}
\|z_\lambda-z_\nu\|^2
&=\|\langle x,\phi(d_{\lambda,\nu}^2)x\rangle\|\\
&\leq2\|\langle x,D_{\lambda,\nu}x\rangle\|.
\end{aligned}
\tag{2.9}
\]
The right side tends to zero as both indices tend to infinity, because
\(D_{\lambda,\nu}x=(H-\phi(e_\lambda))x+(H-\phi(e_\nu))x\)
tends to zero by strict convergence. Thus the net in (2.7) is Cauchy for the originally given approximate identity. Since
\(\|[e_\lambda\otimes x]\|^2\leq\|\phi\|\|x\|^2\), its limit is bounded and \(B\)-linear, with \(\|V\|\leq\|\phi\|^{1/2}\).

For \(z=\sum_i[a_i\otimes y_i]\), (2.1) and \(e_\lambda a_i\to a_i\) give
\[
\langle Vx,z\rangle
=\left\langle x,\sum_i\phi(a_i)y_i\right\rangle.
\tag{2.10}
\]
Let \(Rz=\sum_i\phi(a_i)y_i\). For any \(w\in E\),
\[
\|w\|=\sup_{\|x\|\leq1}\|\langle x,w\rangle\|:
\tag{2.11}
\]
the upper bound is Cauchy–Schwarz, and the lower bound follows by taking \(x=w/\|w\|\) when \(w\ne0\). Applying (2.11) to (2.10) gives \(\|Rz\|\leq\|V\|\|z\|\). It also shows that \(Rz=0\) when \(z=0\), so the formula is independent of the tensor presentation and the null quotient. It extends continuously to \(F\). Equation (2.10) now proves \(R=V^*\), including adjointability. ∎

For \(a\in A\), (2.6) and \(ae_\lambda\to a\) imply
\[
\pi(a)Vx=[a\otimes x].
\tag{2.12}
\]
Equations (2.8) and (2.12) prove \(V^*\pi(a)V=\phi(a)\), and also minimality since the elementary tensors span a dense submodule. Furthermore,
\(V^*[e_\lambda\otimes x]=\phi(e_\lambda)x\) tends both to \(V^*Vx\) and to \(Hx\). Thus \(V^*V=H\). Compression gives \(\|\phi\|\leq\|V\|^2\), and Lemma 2.2 gives the reverse inequality. If \(H=1_E\), then \(V\) is an adjointable isometry and \(VV^*\) is the orthogonal projection onto \(VE\), proving the complemented-submodule assertion.

For any positive contractive approximate identity \((f_\mu)\), nondegeneracy gives \(\pi(f_\mu)\xi\to\xi\) on \(F\), by the same elementary-tensor proof following (2.6). Hence \(V^*\pi(f_\mu)V\to V^*V\) pointwise on \(E\). The operators are self-adjoint and uniformly bounded, so the convergence is strict by (1.1). This verifies the approximate-identity independence for every map to which the construction applies.

## 3. Why minimality gives uniqueness

**Theorem 3.1.** Suppose \((F,\pi,V)\) and \((F',\rho,W)\) are minimal dilations of the same map. There is a unique unitary \(U:F\to F'\) with
\[
U\pi(a)=\rho(a)U,
\qquad UV=W.
\tag{3.1}
\]

*Proof.* Define a map on finite sums by
\[
\sum_i\pi(a_i)Vx_i
\longmapsto
\sum_i\rho(a_i)Wx_i.
\tag{3.2}
\]
The inner product of two such sums on either side is
\(\sum_{i,j}\langle x_i,\phi(a_i^*b_j)y_j\rangle\). Thus (3.2) is well defined, preserves inner products, and is \(B\)-linear. Minimality makes its domain and image dense. Its extension is a surjective isometry preserving inner products, whose inverse is its adjoint; it is therefore unitary. Left multiplication in the sums proves the intertwining relation.

A minimal representation is nondegenerate: if \((e_\lambda)\) is an approximate identity, then \(\rho(e_\lambda)\rho(a)Wx=\rho(e_\lambda a)Wx\to\rho(a)Wx\) on a dense set, and uniform boundedness gives convergence on all of \(F'\). The same holds for \(\pi\). Intertwining (3.2) and taking limits in
\(U\pi(e_\lambda)Vx=\rho(e_\lambda)Wx\) gives \(UVx=Wx\). Any unitary satisfying (3.1) must agree with (3.2) on a dense set, so it is unique. ∎

The proof identifies the mathematical object being made canonical: the closure of the vectors generated by the representation and the compression map. An arbitrary dilation may include an additional summand orthogonal to that closure. For modules, the closure need not be complemented in that larger dilation; minimal uniqueness does not assert that every larger dilation splits as an orthogonal direct sum.

## 4. The exact role of strictness

**Proposition 4.1.** If a completely positive map has a dilation \(\phi(a)=W^*\rho(a)W\) with \(W\) adjointable and \(\rho\) nondegenerate, then \(\phi\) is strict. In particular, strictness is necessary for a minimal dilation.

*Proof.* For any approximate identity, \(\rho(e_\lambda)\xi\to\xi\): first check this on vectors \(\rho(a)\eta\), using \(e_\lambda a\to a\), and then use their density and the contractive bound. Thus \(\phi(e_\lambda)x\to W^*Wx\) for every \(x\). The operators are self-adjoint, so (1.1) gives strict convergence. Minimality implies nondegeneracy by the argument in Theorem 3.1. ∎

**Example 4.2.** Put \(A=C_0((0,1])\), \(B=C([0,1])\), and \(E=B\). Extend functions in \(A\) by zero at zero and let \(\phi:A\to\mathcal L(B)=B\) be this inclusion. It is a *-homomorphism, hence completely positive. On \(\mathcal L(B)\), strict convergence implies norm convergence by testing the vector \(1\). An approximate identity of \(A\) converges pointwise to one at every positive point and is zero at zero. It cannot converge uniformly to a continuous function. Therefore \(\phi\) is not strict.

Its tensor construction is the ideal \(A\) itself: \([a\otimes b]\mapsto ab\) preserves the inner product and has dense range. A map \(V:B\to A\) satisfying \(aV(1)=a\) for every \(a\in A\) would have \(V(1)(t)=1\) for \(t>0\), impossible in \(A\). This exhibits the missing compression operator in the minimal construction.

There is nevertheless a dilation on the larger module \(B\): take the same inclusion as \(\rho\) and \(W=1_B\). It is degenerate, since \(\overline{\rho(A)B}=A\ne B\), and is not minimal. Thus the conclusion that fails without strictness is the minimal nondegenerate dilation theorem. The blanket assertion that no dilation can exist would be too strong.

## 5. Conditional expectations and the basic construction

Let \(A\subseteq C\) be a C*-subalgebra. Here a **conditional expectation** is a completely positive contraction \(P:C\to A\) which fixes \(A\) and, for \(a,b\in A\) and \(c\in C\), satisfies
\[
P(acb)=aP(c)b.
\tag{5.1}
\]
The one-sided identities hold for the same map, without any unit assumption. Indeed, for \(a\in A\),
\(P(a^*a)=a^*a=P(a)^*P(a)\) and
\(P(aa^*)=aa^*=P(a)P(a)^*\).
The multiplicative-domain assertion for completely positive contractions [*Completely positive maps*, Theorem 4.1(3)] therefore gives
\[
\begin{aligned}
P(ca)&=P(c)a,\\
P(ac)&=aP(c)
\qquad(c\in C).
\end{aligned}
\]
These are the bimodularity identities used in the construction below.

Neither algebra need be unital, and \(P\) need not be faithful. Define
\[
\begin{aligned}
\langle c,d\rangle_A&=P(c^*d),\\
N&=\{c\in C\mid P(c^*c)=0\}.
\end{aligned}
\tag{5.2}
\]
As in Lemma 2.1, quotienting by \(N\) and completing gives a Hilbert \(A\)-module, denoted \(L^2(C,P)\). Write \([c]\) for the class of \(c\).

**Theorem 5.1.** Left multiplication gives a nondegenerate representation \(\lambda:C\to\mathcal L(L^2(C,P))\). The map \(V:A\to L^2(C,P)\), \(Va=[a]\), is an adjointable isometry, and
\[
V^*[c]=P(c),
\qquad V^*\lambda(c)V=L_{P(c)}.
\tag{5.3}
\]
This is the minimal KSGNS dilation of \(P\), viewed as a map into \(\mathcal L(A)=M(A)\).

*Proof.* The right action and the inner product are compatible by (5.1). For left multiplication,
\[
P(d^*c^*cd)\leq\|c\|^2P(d^*d).
\tag{5.4}
\]
This follows by applying positivity to \(d^*(\|c\|^2 1-c^*c)d\). Thus multiplication by \(c\) descends to the quotient, is bounded, and has adjoint multiplication by \(c^*\). Approximate identities of \(C\) act pointwise as the identity on the dense classes \([d]\), since \(e_\lambda d\to d\) in the algebra norm and \(\|[d]\|\leq\|d\|\). This proves nondegeneracy.

Since \(P\) fixes \(A\), the map \(Va=[a]\) is isometric. The identity
\(\langle Va,[c]\rangle=a^*P(c)\), together with the dual-norm argument (2.11), proves that \([c]\mapsto P(c)\) is its bounded adjoint. Formula (5.3) follows.

For a positive contractive approximate identity \((f_i)\) of \(A\),
\[
\|[c]-[cf_i]\|^2
=\|(1-f_i)P(c^*c)(1-f_i)\|\longrightarrow0.
\tag{5.5}
\]
The identity uses bimodularity, with the units interpreted in the unitization, and convergence uses the approximate-identity property in \(A\). Thus the vectors \(\lambda(c)Va=[ca]\) span a dense submodule, proving minimality.

Strictness is also visible directly. For an approximate identity of \(C\),
\(P(e_\lambda)a=P(e_\lambda a)\to a\) and \(aP(e_\lambda)=P(ae_\lambda)\to a\). Hence \(P(e_\lambda)\to1_{M(A)}\) strictly. Finally the explicit unitary from the tensor construction is
\([c\otimes a]\mapsto[ca]\): bimodularity preserves its inner product, and (5.5) gives dense range. ∎

The **Jones projection** in this setting is \(q=VV^*\). It satisfies
\[
q[c]=[P(c)],
\qquad q\lambda(c)q=\lambda(P(c))q.
\tag{5.6}
\]
The first identity follows from (5.3). For the second, \(\lambda(a)V=VL_a\) for \(a\in A\), so \(q\lambda(c)q=VL_{P(c)}V^*=\lambda(P(c))q\).

**Proposition 5.2.** The norm-closed span of \(\lambda(c)q\lambda(d^*)\), \(c,d\in C\), is \(\mathcal K(L^2(C,P))\).

*Proof.* For any module vector \(\xi\), the creation map \(T_\xi:A\to L^2(C,P)\), \(a\mapsto\xi a\), has adjoint \(T_\xi^*\eta=\langle\xi,\eta\rangle\); boundedness follows from Cauchy–Schwarz. Here \(\lambda(c)V=T_{[c]}\). Consequently
\[
\lambda(c)q\lambda(d^*)
=T_{[c]}T_{[d]}^*
=\theta_{[c],[d]}.
\tag{5.7}
\]
The classes \([c]\) are dense in the module, and rank-one operators depend norm continuously on both vectors. These operators therefore span a dense subspace of the compact algebra, proving the assertion. ∎

This algebra is the C*-basic construction in the displayed representation. If \(C\) and \(A\) share a unit, \(q=\theta_{[1],[1]}\) is compact. In the nonunital case it can be only a multiplier of the compact algebra. For example, \(P=\mathrm{id}_{C_0(\mathbb R)}\) gives \(q=1\in M(C_0(\mathbb R))\), which does not belong to \(C_0(\mathbb R)\). No numerical Jones index is being asserted.

If \(P\) is faithful, meaning \(P(c^*c)=0\) forces \(c=0\), then \(\lambda\) is faithful. Indeed, \(\lambda(c)=0\) gives \([ce_\lambda]=0\) for an approximate identity of \(C\). Faithfulness gives \(ce_\lambda=0\), and its norm limit is \(c\).

## 6. States and matrix traces

**Example 6.1 (GNS).** A state \(\omega:A\to\mathbb C\) is completely positive: the scalar quadratic form of \([\omega(a_i^*a_j)]\) is \(\omega((\sum_i a_i z_i)^*(\sum_j a_j z_j))\geq0\). For a positive contractive approximate identity, \(\omega(e_\lambda)\to\|\omega\|=1\) [*Representations and positive functionals*, Theorem 4.7]. Thus \(\omega\) is nondegenerate. Identify \(A\odot\mathbb C\) with \(A\). Formula (2.1) becomes \(\omega(a^*b)\), the null quotient and completion are the usual GNS Hilbert space, and \(\Omega=V1\) is a unit cyclic vector with
\[
\omega(a)=\langle\Omega,\pi(a)\Omega\rangle.
\tag{6.1}
\]
For unital \(A\), \(\Omega=[1]\). For nonunital \(A\), it is the limit of the approximate-identity classes. This limit produces a cyclic vector without introducing a unit into the minimal representation.

**Example 6.2 (Normalized matrix trace).** For any C*-algebra \(A\), let
\[
P:M_n(A)\longrightarrow A,
\qquad P(c)=\frac1n\sum_{i=1}^n c_{ii}.
\tag{6.2}
\]
Each diagonal compression is completely positive, so their average is too. It is contractive: as an operator-valued compression it is the sum with coefficients \(1/\sqrt n\), or one can represent \(A\) faithfully and use the isometry \(\xi\mapsto n^{-1/2}(\varepsilon_i\otimes\xi)_i\) into \(n\) copies of the matrix representation space. With \(A\) embedded by \(a\mapsto I_n a\), this is a conditional expectation. It is faithful, since \(P(c^*c)=n^{-1}\sum_{i,j}c_{ij}^*c_{ij}=0\) forces every entry to vanish.

Its Hilbert module is \(A^{n^2}\), under
\[
[c]\longmapsto(n^{-1/2}c_{ij})_{i,j}.
\tag{6.3}
\]
The formula is isometric because \(\langle[c],[d]\rangle=n^{-1}\sum_{i,j}c_{ij}^*d_{ij}\), and is onto the finite standard module. Left multiplication acts on each matrix column. The isometry is \(Va=[I_n a]\), its adjoint is (6.2), and the Jones projection sends a matrix to its scalar diagonal matrix \(I_nP(c)\). These formulas remain meaningful when \(A\) has no unit, since \(I_n a\in M_n(A)\).

## 7. Reduced crossed products

Let a discrete group \(\Gamma\) act on \(A\) by automorphisms \(\alpha_g\). Define \(\ell^2(\Gamma,A)\) as the completion of finitely supported columns in the inner product \(\sum_g\xi(g)^*\eta(g)\). The regular operators are
\[
\begin{aligned}
(r(a)\xi)(t)&=\alpha_{t^{-1}}(a)\xi(t),\\
(u_g\xi)(t)&=\xi(g^{-1}t).
\end{aligned}
\tag{7.1}
\]
They are adjointable: \(r(a)^*=r(a^*)\), and \(u_g\) is a unitary with inverse \(u_{g^{-1}}\). The estimate for \(r(a)\) follows by summing \(\xi(t)^*\alpha_{t^{-1}}(a^*a)\xi(t)\leq\|a\|^2\xi(t)^*\xi(t)\). They satisfy \(u_g r(a)u_g^*=r(\alpha_g(a))\). By definition, \(C=A\rtimes_r\Gamma\) is the norm closure of finite sums \(\sum_g r(a_g)u_g\). We abbreviate these as \(\sum_g a_g u_g\). If \(A\) is nonunital, the \(u_g\) are multipliers, and the products \(a_g u_g\) are elements of \(C\).

**Theorem 7.1.** The coefficient map
\[
P\left(\sum_g a_g u_g\right)=a_e
\tag{7.2}
\]
extends to a faithful conditional expectation \(C\to A\). The unitary
\[
J:L^2(C,P)\longrightarrow\ell^2(\Gamma,A)
\tag{7.3}
\]
is given on finite sums by \(J[\sum_g a_g u_g](g)=\alpha_{g^{-1}}(a_g)\). It identifies the KSGNS representation with (7.1), \(V\) with the identity-coordinate embedding, and \(q\) with the projection onto that coordinate.

*Proof.* Let \(W:A\to\ell^2(\Gamma,A)\) send \(a\) to the column with value \(a\) at \(e\). Its adjoint is coordinate evaluation. Compression gives \(W^*cW=L_{a_e}\) for a finite sum. Since \(A\) is norm closed in \(M(A)=\mathcal L(A)\), the same compression has its value in \(A\) for every \(c\in C\). Compression is completely positive and contractive, so this defines \(P\). It fixes \(A\) and is \(A\)-bimodular, either by compression and \(r(a)W=WL_a\), or by (7.2).

For faithfulness, suppose \(P(c^*c)=0\). Then \(cW=0\). For every \(g\), the coefficient formula, followed by norm continuity, gives
\[
P(u_g^*c^*cu_g)=\alpha_{g^{-1}}(P(c^*c))=0.
\tag{7.4}
\]
Thus \(cu_gW=0\). The ranges of \(u_gW\) span all finite columns, a dense submodule, so \(c=0\).

For finite sums \(b=\sum_g b_g u_g\), \(c=\sum_g c_g u_g\), the product rule gives
\[
P(b^*c)=\sum_g\alpha_{g^{-1}}(b_g^*c_g).
\tag{7.5}
\]
This is exactly the column inner product of their proposed images. Right multiplication by \(a\in A\) changes \(b_g\) to \(b_g\alpha_g(a)\), whose image is \(\alpha_{g^{-1}}(b_g)a\); thus the map is \(A\)-linear. Every finite column \(\xi\) is obtained by choosing \(b_g=\alpha_g(\xi(g))\). Finite sums are dense in the algebra norm and hence in the \(P\)-norm, so the isometry extends onto the complete column module.

For a generator \(a u_h\), multiplication takes coefficient \(b_g\) to \(a\alpha_h(b_g)\) at index \(hg\). At \(t=hg\), its image is
\(\alpha_{t^{-1}}(a)\alpha_{g^{-1}}(b_g)\), the value of \(r(a)u_hJ[b]\). This proves the representation identity on a dense set and then on the completions. Finally \([a]\) has its only coefficient at \(e\), and (5.6) gives the asserted coordinate projection. ∎

No countability of \(\Gamma\) is needed for these formulas. If \(\Gamma\) is countable and \(A\) is \(\sigma\)-unital, this module is countably generated: for a countable approximate identity \((f_n)\), the countable family of columns \(\delta_g f_n\) generates every finite column, since \(f_n a\to a\). We do not infer that conclusion for arbitrary discrete groups.

## 8. Stabilized dilation without a strictness assumption

The minimal theorem requires strictness. A different conclusion, allowing a degenerate representation, holds for every completely positive contraction on a standard module.

**Lemma 8.1.** For a completely positive contraction \(\phi:A\to\mathcal L(E)\), the map
\[
\phi^\dagger(a+z1)=\phi(a)+z1_E
\tag{8.1}
\]
on the forced unitization \(A^\dagger=A\oplus\mathbb C\) is unital and completely positive. The forced unitization adjoins a new unit even when \(A\) already has one.

*Proof.* The case \(E=0\) is immediate. Otherwise faithfully and unitally represent \(\mathcal L(E)\) on a Hilbert space \(H\), using the Gelfand–Naimark theorem. The Hilbert-space Stinespring theorem [*Completely positive maps*, Theorem 6.1] gives
\(\phi(a)=W^*\sigma(a)W\) in this representation, with \(\|W\|\leq1\). Extend \(\sigma\) to the unital representation \(\sigma^\dagger(a+z1)=\sigma(a)+z1_K\). In the Hilbert-space representation, (8.1) equals
\[
W^*\sigma^\dagger(a+z1)W
+z(1_H-W^*W).
\tag{8.2}
\]
The first summand is completely positive. The second is completely positive because the scalar quotient \(a+z1\mapsto z\) is a *-homomorphism and \(1_H-W^*W\geq0\). For example, a positive scalar matrix \([z_{ij}]\) maps to the positive operator matrix \([z_{ij}(1_H-W^*W)]\). Faithful representations and their matrix amplifications reflect positivity, so (8.1) is completely positive in \(\mathcal L(E)\). Its value at the new unit is \(1_E\). ∎

**Theorem 8.2.** Let \(A\) be separable and \(B\ne0\) be \(\sigma\)-unital. Every completely positive contraction \(\phi:A\to\mathcal L(H_B)\) is the upper-left corner of a faithful *-homomorphism
\[
\rho:A\longrightarrow M_2(\mathcal L(H_B)).
\tag{8.3}
\]
If \(\phi\) is nondegenerate, \(\rho\) may be chosen nondegenerate. For unital \(A\), a unital \(\phi\) therefore admits a unital \(\rho\).

*Proof.* The zero domain is immediate; assume \(A\ne0\). Apply Theorem 1.1 to the unital extension in Lemma 8.1. It gives \(F\), \(\pi^\dagger\) and an adjointable isometry \(V:H_B\to F\). Restrict the representation to \(A\); no nondegeneracy of this restriction is claimed.

The module \(F\) is countably generated. Indeed, take a countable norm-dense subset \((a_i)\) of \(A^\dagger\) and countable module generators \((x_j)\) of \(H_B\), which exist because \(B\) is \(\sigma\)-unital. The tensors \([a_i\otimes x_j]\) generate: approximate the algebra factor in norm and the module factor by finite sums \(x_jb_j\), using (2.6). Therefore the complemented submodule \(F_0=(1-VV^*)F\) is countably generated too, by projecting those generators.

Choose a faithful representation of \(A\) on a separable Hilbert space [*Representations and positive functionals*, Proposition 7.8]. Restricting to its essential subspace preserves faithfulness and makes it nondegenerate. Countable amplification makes this space isomorphic to \(\ell^2\). Exterior tensoring with \(B\) gives a faithful nondegenerate representation \(\sigma:A\to\mathcal L(H_B)\). Faithfulness also follows directly: if \(\sigma(a)\) vanished, its action on \(\xi\otimes b\), for a nonzero \(b\in B\), would force the original Hilbert-space operator on every \(\xi\) to vanish.

Now use \(\pi\oplus\sigma\) on \(F\oplus H_B\). The decomposition
\[
F\oplus H_B
=VH_B\oplus(F_0\oplus H_B)
\cong H_B\oplus H_B
\tag{8.4}
\]
uses the isometry \(V\) in the first summand and *Kasparov's stabilization theorem*, Theorem 3.1, in the second. Transporting the representation through this unitary gives a faithful (8.3). Its upper-left compression is \(V^*\pi(a)V=\phi(a)\).

If \(\phi\) is nondegenerate, instead start with its strict minimal dilation for \(A\) itself. Its representation is nondegenerate, its \(V\) is an isometry, and the same countable-generation argument applies. The direct sum with \(\sigma\), and then unitary transport, preserve nondegeneracy. For unital \(A\), a nondegenerate representation sends its identity to the identity, proving the last assertion. ∎

This proves [Blackadar 2006, Corollary II.7.5.3], with the harmless nonzero coefficient condition made explicit for faithfulness. If \(B=0\), the target algebra is zero and cannot faithfully represent a nonzero \(A\). No strictness assumption was imposed in the first assertion; the unitization permits degeneracy. Example 4.2 explains why nondegeneracy cannot be required there in general.

## 9. Compression and inverse extensions

Let \(B\ne0\) be \(\sigma\)-unital, put \(D=\mathcal K(H_B)\), and let \(Q=M(D)/D\), with quotient map \(p\). The standard-module compact algebra is \(B\otimes\mathcal K\), so this is the stabilized corona. A *-homomorphism \(\tau:A\to Q\), called a Busby map, specifies an extension; it is **semisplit** here if it has a completely positive contractive lift \(\phi:A\to M(D)=\mathcal L(H_B)\). A homomorphic lift specifies a split extension.

Assume \(A\) is separable. Theorem 8.2 dilates the lift to \(\rho:A\to M_2(M(D))\). Set \(\beta=p^{(2)}\rho\), and write \(e=\operatorname{diag}(1,0)\). Its upper-left corner is \(\tau\). For \(a\in A\),
\[
\begin{aligned}
((1-e)\beta(a)e)^*((1-e)\beta(a)e)
&=e\beta(a^*a)e\\
&\quad-e\beta(a)^*e\beta(a)e=0.
\end{aligned}
\tag{9.1}
\]
The last equality is precisely multiplicativity of \(\tau\). Therefore the lower-left corner vanishes; apply the same argument to \(a^*\) to get a zero upper-right corner. It follows that
\[
\beta(a)=\begin{pmatrix}\tau(a)&0\\0&\tau_-(a)\end{pmatrix},
\tag{9.2}
\]
where \(\tau_-\) is also a *-homomorphism. The direct sum of these two Busby maps has the homomorphic lift \(\rho\). Thus their sum is split, and \(\tau_-\) gives an inverse for \(\tau\) in the stabilized extension semigroup modulo split extensions.

Conversely, when a direct sum has a homomorphic lift, compression of that lift gives a completely positive contractive lift of each summand. Passing between this representative-level statement and invertibility of stable equivalence classes is the exact assigned prerequisite *Ext groups, absorption and Brown–Douglas–Fillmore theory*, Section 2, in *Kasparov’s KK-theory*: for separable \(A\), a Busby map into the stabilized corona represents an invertible class in \(\operatorname{Ext}(A,B)\) if and only if it admits such a lift. That assigned section is planned and owns the stable equivalence conventions and this full class-level converse, for the sigma-unital coefficient algebra \(B\) and separable \(A\) used in this section and the corona of \(B\otimes\mathbb K\). Blackadar, Theorem 15.7.1, credits the result. Its Stinespring input is the construction proved in Sections 1–4 here, which does not use Ext or this application; the proof dependence is therefore at the result level and is not circular. Class equality is not literal equality of chosen Busby maps.

For a unital \(A\) and unital \(\tau\), a contractive lift need not itself be unital. It can be repaired. Choose a state \(\omega\) of \(A\) and set
\[
\psi(a)=\phi(a)+\omega(a)(1-\phi(1)).
\tag{9.3}
\]
The added map is completely positive since \(1-\phi(1)\geq0\), and its quotient is zero because \(p(\phi(1))=1_Q\). Thus \(\psi\) is a unital completely positive lift of \(\tau\). Theorem 8.2 gives a unital representation dilating \(\psi\), so the lower-right map in (9.2) is unital as well. This is the required unital variant of the inverse construction. Unitality of the domain alone cannot make a dilation unital while preserving an arbitrary nonunital upper-left map.

This is the compression mechanism behind the use of generalized Stinespring in extension theory. Kasparov's version of Voiculescu's absorption theorem requires additional representation theory; we do not assert or use that theorem here.

## 10. Exercises with complete solutions

**Exercise 10.1 (GNS).** Recover the GNS construction of a state from KSGNS with \(E=\mathbb C\), including its cyclic vector when \(A\) is nonunital.

*Solution.* The linear identification \(A\odot\mathbb C\to A\), \(a\otimes z\mapsto az\), takes (2.1) to \(\omega(a^*b)\). Its null quotient is \(A/N_\omega\), \(N_\omega=\{a:\omega(a^*a)=0\}\); its completion is the GNS space, and \(\pi(c)[a]=[ca]\). Positivity of \(\omega\) makes the kernel matrix positive by the calculation in Example 6.1, so it is a completely positive map. Since \(\omega(e_\lambda)\to1\), it is strict and nondegenerate. Lemma 2.2 supplies \(\Omega=\lim[e_\lambda]\), with squared norm \(V^*V=1\). Equation (2.12) says \(\pi(a)\Omega=[a]\), proving cyclicity, and (2.8) yields \(\langle\Omega,\pi(a)\Omega\rangle=\omega(a)\). If there is a unit, the same formulas give \(\Omega=[1]\). ∎

**Exercise 10.2 (Positivity).** Prove that the KSGNS form is positive for arbitrary finite tensor sums, and explain why the null quotient is legitimate.

*Solution.* Given \(z=\sum_i a_i\otimes x_i\), let \(M=[\phi(a_i^*a_j)]\). The Gram matrix \([a_i^*a_j]\) is positive and complete positivity makes \(M\) positive on \(E^n\). With \(x=(x_i)\), (2.3) gives \(\langle z,z\rangle=\langle M^{1/2}x,M^{1/2}x\rangle\in B_+\). This handles cross terms between distinct tensors. Sesquilinearity and the tensor relations were verified in (2.1); the semi-inner-product Cauchy–Schwarz inequality shows that a null vector has zero inner product with every vector. Thus the null vectors form a subspace, the inner product is independent of representatives, and its definiteness on the quotient follows from its definition. The estimate \(\|zb\|\leq\|z\|\|b\|\) makes the null space a submodule, so both the right action and the completed inner product are well defined. ∎

**Exercise 10.3 (Uniqueness).** Construct the unitary between two minimal dilations and show that it carries one compression map to the other.

*Solution.* On finite sums set \(U(\sum_i\pi(a_i)Vx_i)=\sum_i\rho(a_i)Wx_i\). Inner products on both sides equal \(\sum_{i,j}\langle x_i,\phi(a_i^*b_j)y_j\rangle\); hence this is well defined, isometric and \(B\)-linear. Its dense image and minimality extend it to a surjective inner-product-preserving isometry, with inverse its adjoint. Multiplication of every \(a_i\) by \(c\) shows \(U\pi(c)=\rho(c)U\). Minimality implies that both representations are nondegenerate, by approximation on their spanning vectors. Consequently \(\pi(e_\lambda)Vx\to Vx\) and \(\rho(e_\lambda)Wx\to Wx\). Applying \(U\) to these nets proves \(UVx=Wx\). Any other intertwining unitary with this property agrees on the dense finite sums and hence equals \(U\). ∎

**Exercise 10.4 (Crossed-product coordinates).** Identify the module and representation of the expectation \(A\rtimes_r\Gamma\to A\), taking account of the right \(A\)-action.

*Solution.* On a finite sum \(b=\sum_g b_g u_g\), use \(J[b](g)=\alpha_{g^{-1}}(b_g)\). The product rule \((a u_g)(b u_h)=a\alpha_g(b)u_{gh}\) gives (7.5), so \(J\) preserves inner products. Since \(b a=\sum_g b_g\alpha_g(a)u_g\), the transformed column is \(J[b](g)a\); this verifies module linearity. For any finite column \(\xi\), choosing \(b_g=\alpha_g(\xi(g))\) gives \(J[b]=\xi\). Density of finite sums in the algebra norm, and \(\|[b]\|\leq\|b\|\), now make \(J\) an onto unitary of the completed modules.

To check the representation, left multiplication by \(a u_h\) gives coefficient \(a\alpha_h(b_g)\) at \(t=hg\). Applying \(\alpha_{t^{-1}}\) yields \(\alpha_{t^{-1}}(a)J[b](h^{-1}t)\), exactly \((r(a)u_hJ[b])(t)\). Extend by norm continuity to all of \(A\rtimes_r\Gamma\). The embedding \(Va=[a]\) becomes the column supported at \(e\); its adjoint evaluates that coordinate, and its range projection deletes every other coordinate. Thus the KSGNS triple is the regular module representation with this compression. ∎

## What this lesson does not prove

We use the basic semi-inner-product Cauchy–Schwarz and completion results from [*Hilbert C*-modules*, Theorem 2.1, Proposition 2.2 and Theorem 2.3]. The strict-topology and multiplier identification are [*Compact operators, multipliers and the strict topology*, Proposition 5.1 and Theorem 4.1], and its Theorem 2.1 identifies the standard-module compact algebra. The exterior tensor action is [*Tensor products and C*-correspondences*, Theorem 5.1]. Countable generation of \(H_B\) for \(\sigma\)-unital \(B\) and absorption of a countably generated module are [*Kasparov's stabilization theorem*, Proposition 5.1 and Theorem 3.1].

The external representation inputs are automatic boundedness and adjoint preservation of positive maps [*Completely positive maps*, Proposition 3.2], the multiplicative-domain identities for completely positive contractions [there, Theorem 4.1(3)], the Hilbert-space Stinespring theorem with \(\|W\|^2=\|\phi\|\) [there, Theorem 6.1], the approximate-identity norm formula for positive functionals [*Representations and positive functionals*, Theorem 4.7], and faithful representations, including the separable case [there, Theorem 7.2 and Proposition 7.8]. Lemma 2.2 uses the quadratic-form positivity criterion [*Adjointable operators*, Theorem 3.1] to handle an arbitrary positive contractive approximate identity with the given strict limit. The independence assertion in [Blackadar 2006, II.7.5.1] is proved at the end of Section 2, without being assumed in the construction.

For extension theory, the stabilized equivalence conventions and class-level invertibility criterion have the exact planned provider *Ext groups, absorption and Brown–Douglas–Fillmore theory*, Section 2, for separable domain algebras and sigma-unital coefficients, as stated in Section 9. Blackadar, Theorem 15.7.1, remains the classical credit. We proved the off-diagonal vanishing, the inverse construction for a lifted direct sum, and the repair of a lift in the unital case. We do not develop the full extension semigroup, its classification, finite-index conditional expectations, or Kasparov–Voiculescu absorption.

## References

- B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006; [author revised version](https://www.bruceblackadar.com/Mathematics/Cycr.pdf), II.7.5.1–II.7.5.3.
- B. Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, Section 15.7, especially Theorem 15.7.1. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- G. G. Kasparov, [“Hilbert C*-modules: theorems of Stinespring and Voiculescu”](https://jot.theta.ro/jot/archive/1980-004-001/1980-004-001-007.html), *Journal of Operator Theory* 4 (1980), 133–150. Historical attribution; the theorem is proved here rather than imported from that paper.
- *Foundations of von Neumann Algebras*, “Completely positive maps” and “Representations and positive functionals: the GNS construction and the Gelfand–Naimark theorem,” at the locators stated above.
