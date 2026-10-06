# Casimir operators, Laplacians and tensor products

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

A character records weights, a Casimir records an energy, and a tensor product combines characters. The Weyl formula makes all three computations explicit. The metric and exponential convention must stay visible: changing either can multiply every eigenvalue by the same constant.

Throughout, \(G\) is a compact connected Lie group with an \(\operatorname{Ad}(G)\)-invariant positive inner product \(B\) on its real Lie algebra \(\mathfrak g\). We use the [highest-weight classification and Weyl formulas](RT-CPT-11.md), [Peter–Weyl decomposition](RT-CPT-02.md), and smooth differentiation from lesson five. Analytic weights retain the convention
\[
d\pi(H)v=2\pi i\lambda(H)v,\qquad H\in\mathfrak t.
\]
The norm of a weight means the norm for the dual of \(B|_{\mathfrak t}\). Put \(\ell=2\pi\lambda\) and \(r=2\pi\rho\) when angular weights are more convenient.

## The metric Casimir

For any real \(B\)-orthonormal basis \(X_1,\ldots,X_d\), define
\[
C_B=-\sum_{j=1}^d X_j^2\in U(\mathfrak g_{\mathbb C}). \tag{1.1}
\]
An orthogonal basis change leaves this element unchanged, by expanding the squares and using \(\sum_j O_{jk}O_{jl}=\delta_{kl}\); commutativity of the generators is not required.

**Proposition 1.2.** The element \(C_B\) is central. On the irreducible representation of highest analytic weight \(\lambda\), it acts by
\[
c_B(\lambda)=4\pi^2(\lambda,\lambda+2\rho)_B
=(\ell,\ell+2r)_B. \tag{1.3}
\]
It is nonnegative, and scaling \(B\) by \(a>0\) scales \(c_B\) by \(a^{-1}\).

*Proof.* Write \([Y,X_j]=\sum_k a_{kj}X_k\). Invariance of \(B\) says that the matrix \(a\) is skew-symmetric. Therefore
\[
[Y,C_B]=-\sum_{j,k}a_{kj}(X_kX_j+X_jX_k)=0.
\]
The generators \(Y\) generate the enveloping algebra, proving centrality.

Extend \(B\) complex bilinearly. Choose an orthonormal basis \(H_a\) of the real torus algebra and orthonormal pairs \(U_\alpha,V_\alpha\) in its mutually orthogonal real root planes. Orient each pair so that
\[
E_\alpha=\frac{U_\alpha-iV_\alpha}{\sqrt2},\qquad
[H,E_\alpha]=2\pi i\alpha(H)E_\alpha.
\]
Then \(B(E_\alpha,\overline E_\alpha)=1\), and
\[
C_B=-\sum_a H_a^2-
\sum_{\alpha>0}(E_\alpha\overline E_\alpha+
\overline E_\alpha E_\alpha).
\]
For \(H\in\mathfrak t\), invariance gives
\[
B([E_\alpha,\overline E_\alpha],H)
=B(E_\alpha,[\overline E_\alpha,H])
=2\pi i\alpha(H).
\]
The bracket lies in \(\mathfrak t_{\mathbb C}\), so it is \(2\pi i\alpha^\sharp\).
On a highest vector \(v\), all positive \(E_\alpha\) vanish. The torus part contributes \(4\pi^2\|\lambda\|^2v\), and each root pair contributes
\[
-d\pi([E_\alpha,\overline E_\alpha])v
=4\pi^2(\lambda,\alpha)v.
\]
Their sum is (1.3). The operator commutes with \(\pi(G)\): conjugation transforms the \(X_j\)'s by a \(B\)-orthogonal basis change. Schur's lemma therefore makes this the scalar on the entire irreducible. Central torus directions are included in the torus sum; no semisimplicity was assumed.

Each \(d\pi(X_j)\) is skew-adjoint, so
\[
\langle d\pi(C_B)u,u\rangle
=\sum_j\|d\pi(X_j)u\|^2\geq0.
\]
The dual metric scales inversely, proving the final assertion. \(\square\)

Thus the familiar expression \((\lambda,\lambda+2\rho)\) has no extra \(4\pi^2\) only when the weights denote eigenvalues divided by \(i\), rather than by \(2\pi i\). The formula is also the difference of two squares,
\[
c_B(\lambda)=4\pi^2\bigl(\|\lambda+\rho\|^2-\|\rho\|^2\bigr).
\]
For the compact semisimple metric \(B=-K\), with \(K\) the Killing form, the adjoint Casimir equals one on each simple summand. One can check the normalization without root coordinates: if \(X_j\) are \(B\)-orthonormal, then
\[
\operatorname{tr}_{\mathfrak g}\left(-\sum_j\operatorname{ad}(X_j)^2\right)
=-\sum_j K(X_j,X_j)=\dim\mathfrak g.
\]
The adjoint is irreducible for a simple algebra, so its scalar is one. The metric \(-K\) is degenerate on a nonzero center and cannot be used there.

## The Laplacian and its actual eigenspaces

Use the nonpositive sign convention \(\Delta=\operatorname{div}\operatorname{grad}\). The metric obtained by left translation of \(B\) is also right invariant. Its Riemannian volume is proportional to Haar measure.

Let \(X_j^L f(g)=\left.\frac{d}{dt}\right|_0 f(g\exp(tX_j))\). These are a global orthonormal frame. Their flows are right translations and preserve volume, hence their divergences vanish. Since
\(\operatorname{grad}f=\sum_j(X_j^Lf)X_j^L\), the product rule for divergence gives directly
\[
\Delta f=\sum_j(X_j^L)^2f. \tag{2.1}
\]
This proves the Casimir–Laplacian identification with the stated sign.

For a matrix coefficient \(f(g)=\phi(\pi_\lambda(g)v)\), differentiation in the right variable gives
\[
\Delta f(g)=\phi\left(\pi_\lambda(g)
\sum_j d\pi_\lambda(X_j)^2v\right)
=-c_B(\lambda)f(g). \tag{2.2}
\]

**Theorem 2.3.** The self-adjoint \(L^2\) realization of \(\Delta\) has pure point spectrum
\[
\{-c_B(\lambda):\lambda\in X^*(T)\text{ dominant}\}.
\]
Its eigenspace for an eigenvalue \(-c\) is
\[
\bigoplus_{\lambda:\ c_B(\lambda)=c} E_{\pi_\lambda},
\qquad
\operatorname{mult}(-c)=
\sum_{\lambda:\ c_B(\lambda)=c}(\dim\pi_\lambda)^2. \tag{2.4}
\]
Each individual coefficient block has dimension \((\dim\pi_\lambda)^2\); distinct highest weights can give the same eigenvalue.

*Proof.* Schur orthogonality supplies an orthonormal basis of suitably normalized smooth coefficients, and Peter–Weyl makes it complete. In this basis (2.2) is a real diagonal operator. Its self-adjoint realization has domain
\[
\left\{f=\sum_\lambda f_\lambda:
\sum_\lambda c_B(\lambda)^2\|f_\lambda\|_2^2<\infty\right\},
\qquad
\Delta f=-\sum_\lambda c_B(\lambda)f_\lambda. \tag{2.5}
\]
Finite coefficient sums are a core: truncation converges in both the \(L^2\) norm and the norm of the image. For a smooth \(f\), integration by parts against each coefficient gives the Fourier coefficient of \(\Delta f\) as \(-c_B(\lambda)f_\lambda\). Parseval therefore puts \(f\) in (2.5). Consequently the differential operator on all smooth functions lies between the finite-sum operator and its self-adjoint closure; its closure is that same diagonal operator. This also proves essential self-adjointness without importing a spectral theorem for elliptic operators.

For dominant \(\lambda\), \((\lambda,\rho)\geq0\), because \(\rho\) is a positive-root sum and all its pairings with \(\lambda\) are nonnegative. Hence \(c_B(\lambda)\geq4\pi^2\|\lambda\|^2\). Bounded \(c_B\) permits only finitely many lattice weights. Thus eigenspaces are finite-dimensional and the only possible spectral accumulation is toward \(-\infty\). The diagonal decomposition now gives (2.4), including all coincident values. In particular the zero eigenspace consists of the constants. \(\square\)

For \(SU(2)\), take
\[
B(X,Y)=-\tfrac12\operatorname{tr}(XY).
\]
Under the quaternion identification with the unit three-sphere, the imaginary quaternion basis is orthonormal; its left translates give precisely the round metric of radius one. If \(\pi_m=\operatorname{Sym}^m\mathbb C^2\), then
\[
c_B(m)=m(m+2),\qquad
\Delta|_{E_{\pi_m}}=-m(m+2),\qquad
\dim E_{\pi_m}=(m+1)^2. \tag{2.6}
\]
These values are strictly increasing with \(m\geq0\). Spin \(j=m/2\) notation gives \(4j(j+1)\). The basis \(-i\sigma_k/2\) used for spin operators has length \(1/2\) for this metric; its unrescaled sum of squares gives one quarter of the round Laplacian.

For the round unit two-sphere, the three infinitesimal rotation fields \(L_k\) satisfy
\[
\sum_k(L_kf)^2=\|\operatorname{grad}f\|^2,\qquad
\operatorname{div}L_k=0.
\]
The first identity follows at a point \(x\in S^2\) from the fields \(e_k\times x\): their outer products sum to \(I-xx^t\), the tangent projection. Thus \(\Delta_{S^2}=\sum_k L_k^2\). For the \(SO(3)\) rotation metric \(-\operatorname{tr}(XY)/2\), the highest angular weight is \(\ell\) and the positive root has angular value one. Proposition 1.2 gives
\[
\Delta_{S^2}|_{\mathcal H_\ell}=-\ell(\ell+1),
\qquad \dim\mathcal H_\ell=2\ell+1.
\]
Completeness of these spherical harmonics was proved in lesson four. The \(SU(2)\) metric in (2.6) induces a quotient sphere of radius \(1/2\) under its Hopf map. Indeed the differential of \(q\mapsto qiq^{-1}\) sends a horizontal imaginary quaternion \(u\) to \([u,i]\), whose length is \(2\|u\|\). Thus the quotient metric is one quarter of the unit sphere's metric; it must be rescaled to obtain this unit \(S^2\) metric.

## The radial Laplacian from the Weyl density

For \(U(n)\), take \(B(X,Y)=-\operatorname{tr}(XY)\) on its real anti-Hermitian Lie algebra. Write \(D(\theta)=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_n})\), and let \(F(\theta)=f(D(\theta))\) for a smooth class function \(f\). Put
\[
J(\theta)=\prod_{i<j}4\sin^2\frac{\theta_i-\theta_j}{2},
\qquad \delta(\theta)=\prod_{i<j}2\sin\frac{\theta_i-\theta_j}{2}.
\]
Here \(J\) is the Weyl integration density, and \(\delta^2=J\). A regular angle tuple has distinct eigenvalues modulo \(2\pi\).

**Proposition 2.4.** On the regular angle tuples the restriction of \(\Delta f\) is
\[
\begin{aligned}
\mathcal L F&=J^{-1}\sum_j\partial_j(J\partial_jF)\\
&=\sum_j\partial_j^2F\\
&\quad+\sum_{i<j}\cot\frac{\theta_i-\theta_j}{2}(\partial_i-\partial_j)F.
\end{aligned}
\]
With the angular half-sum \(r=((n-1)/2,(n-3)/2,\ldots,(1-n)/2)\), it also satisfies
\[
\delta\mathcal L F=(\Delta_{\mathfrak t}+\|r\|^2)(\delta F),
\qquad \Delta_{\mathfrak t}=\sum_j\partial_j^2.
\]
Consequently the character of integer highest weight \(m_1\geq\cdots\geq m_n\) has eigenvalue \(-\bigl(\|m+r\|^2-\|r\|^2\bigr)\).

*Proof.* At a regular diagonal matrix, the tangent space to its conjugacy orbit, translated to the identity, is \(\mathfrak t^\perp\). Indeed the differential of conjugation is \(\operatorname{Ad}(D^{-1})-1\), zero on diagonal matrices and invertible on every off-diagonal root plane. A class function is constant in these orbit directions. Its gradient is therefore toral, and the matrices \(iE_{jj}\) are an orthonormal toral basis. For another smooth class function \(h\), with restriction \(H\), this gives
\[
\langle\operatorname{grad}f,\operatorname{grad}h\rangle
=\sum_j\partial_jF\,\overline{\partial_jH}
\]
on the regular set. The omitted singular set has measure zero by the Weyl integration proof. Integration by parts on the group and then the Weyl formula yield
\[
\int_G(\Delta f)\overline h
=-\frac1{n!(2\pi)^n}\int_{[0,2\pi]^n}
\sum_j\partial_jF\,\overline{\partial_jH}\,J\,d\theta
=\frac1{n!(2\pi)^n}\int_{[0,2\pi]^n}
\sum_j\partial_j(J\partial_jF)\,\overline H\,d\theta.
\]
All boundary terms cancel by periodicity. To identify the restrictions pointwise, choose a small regular angle patch whose distinct permutation translates are disjoint, and symmetrize any smooth test function supported there. The local conjugacy coordinates from the Weyl integration proof lift this to a smooth class function on the corresponding regular conjugacy neighborhood; extension by zero is smooth because the support stays inside it. These arbitrary local tests force the displayed weighted differential expression to equal the restriction of \(\Delta f\). This argument needs no assertion that every smooth symmetric function on the torus extends smoothly across the walls.

Differentiating \(\log J\) gives the cotangent expression. Since \(J=\delta^2\), the product rule gives
\[
\delta\mathcal L F=\Delta_{\mathfrak t}(\delta F)-F\Delta_{\mathfrak t}\delta.
\]
The Weyl denominator, after multiplication by its scalar phase, is the alternating sum \(\sum_{w\in S_n}\operatorname{sgn}(w)e^{i\langle wr,\theta\rangle}\). Every frequency has squared norm \(\|r\|^2\), so \(\Delta_{\mathfrak t}\delta=-\|r\|^2\delta\). This identity holds on \(\mathbb R^n\); for even \(n\), \(\delta\) itself changes sign under some \(2\pi\) shifts, while \(J\) remains periodic. No globally single-valued denominator on the torus is being assumed.

The unitary character formula of lesson nine makes \(\delta F\), for a character of highest weight \(m\), a scalar multiple of the alternant with frequencies \(w(m+r)\). Their common squared norm proves the claimed eigenvalue. The formula agrees with Proposition 1.2 because the analytic weight is \(m/(2\pi)\), and the analytic half-sum is \(r/(2\pi)\). Thus its \(4\pi^2\) factor disappears precisely when angular weights are used. \(\square\)

The apparent poles at eigenvalue collisions cancel for the restriction of a smooth class function, since the expression equals the restriction of its smooth group Laplacian on the regular set. For \(n=1\), the products are empty and the formula is the ordinary circle Laplacian. For \(\det^k\) it gives \(-nk^2\); the defining character has eigenvalue \(-n\). For \(n\geq2\), the conjugation representation on traceless matrices has highest weight \((1,0,\ldots,0,-1)\) and eigenvalue \(-2n\). These checks include the central direction, the sign, and the metric normalization.

## Tensor multiplicities from alternating coefficients

Write \(m_\mu(\eta)\) for the weight multiplicity in \(\pi_\mu\), extended by zero outside its finite weight set. Tensor multiplicity is
\[
N_{\lambda\mu}^{\nu}
=\dim\operatorname{Hom}_G(\pi_\nu,\pi_\lambda\otimes\pi_\mu).
\]

**Theorem 3.1 (Brauer–Klimyk formula).**
\[
N_{\lambda\mu}^{\nu}
=\sum_{w\in W}\epsilon(w)\,
m_\mu\bigl(w(\nu+\rho)-(\lambda+\rho)\bigr). \tag{3.2}
\]
All three highest weights must be dominant analytic weights for the actual group.

*Proof.* Complete reducibility and the Weyl formula give a finite formal identity
\[
\chi_\lambda\chi_\mu A_\rho
=\sum_\tau N_{\lambda\mu}^{\tau}A_{\tau+\rho}
=\chi_\mu A_{\lambda+\rho}.
\]
On the middle expression, the coefficient of \(e^{\nu+\rho}\) is exactly \(N_{\lambda\mu}^{\nu}\): strictly dominant shifted weights have disjoint Weyl orbits, and the identity term has sign one. On the final expression that coefficient is
\[
\sum_w\epsilon(w)m_\mu\bigl(\nu+\rho-w(\lambda+\rho)\bigr).
\]
Weight multiplicities are Weyl invariant. Apply \(w^{-1}\) inside each argument and then replace \(w\) by \(w^{-1}\); its determinant sign is unchanged. This is (3.2).
All exponents occur in the formal coset \(\rho+X^*(T)\), as in lesson eleven. There is no integration of fractional characters. \(\square\)

Individual signed terms need not be nonnegative, even though the final multiplicity is. For example, with \(SU(2)\) labels \(\lambda=0,\mu=2,\nu=0\), the two terms are \(1-1=0\). Dropping the reflected term would create a nonexistent trivial summand.

For \(SU(3)\), use the sum-zero plane and
\[
p_1=(\tfrac23,-\tfrac13,-\tfrac13),\quad
p_2=(-\tfrac13,\tfrac23,-\tfrac13),\quad
p_3=(-\tfrac13,-\tfrac13,\tfrac23).
\]
These are the defining weights, each of multiplicity one. Their sums in \(3\otimes3\) have multiplicity one for \(2p_i\) and two for \(p_i+p_j=-p_k\), \(i\neq j\). The invariant symmetric and alternating tensor spaces have highest weights \(2\omega_1\) and \(\omega_2\) and dimensions six and three, respectively, by lessons nine and eleven. Hence
\[
3\otimes3=6\oplus\overline3.
\]
The defining-by-dual product is
\[
3\otimes\overline3=8\oplus1;
\]
its full weight and signed-sum checks are Exercise 3. Equal Casimir values of the two defining duals also illustrate (2.4): for \(SU(3)\) with metric \(-\operatorname{tr}(XY)\), both have \(c_B=8/3\). Their two distinct coefficient blocks already contribute eighteen to that eigenspace.

## Identifying a matrix group from trace moments

Tensor decomposition also lets a scalar observation detect the size of a symmetry group. This section allows arbitrary compact Hausdorff groups for the moment identities; only the subsequent matrix-group conclusion uses Lie theory. For a finite-dimensional continuous unitary representation \(V\), define
\[
M_{2k}(V)=\int_G|\chi_V(g)|^{2k}\,dg,
\qquad k\geq1.
\]
Haar measure has mass one.

**Proposition 3.6 (moments count commuting operators).** For arbitrary compact \(G\),
\[
M_{2k}(V)=\dim\operatorname{End}_G(V^{\otimes k}).
\]
In particular, if \(V\otimes V^*=\bigoplus_\sigma m_\sigma V_\sigma\), then
\[
M_4(V)=\dim\operatorname{End}_G(V\otimes V^*)
=\sum_\sigma m_\sigma^2.
\]
For compact subgroups \(K\subset H\subset U(n)\), the defining moments satisfy \(M_{2k}(H)\leq M_{2k}(K)\).

*Proof.* The character of \(V^{\otimes k}\) is \(\chi_V^k\). Its squared character norm equals its commuting-operator dimension by character orthogonality and Schur's lemma. For the second formula, \(\chi_{V\otimes V^*}=|\chi_V|^2\); its squared norm gives the same fourth moment. Finally the tensor representation on \(V^{\otimes k}\) is the same ambient one for both subgroups, and every operator commuting with \(H\) commutes with \(K\). Inclusion of these finite-dimensional spaces gives the inequality. \(\square\)

**Theorem 3.7 (Larsen's unitary alternative).** Let \(n\geq2\) and let \(K\subset SU(n)\) be a compact subgroup. If
\[
\int_K|\operatorname{tr}(g)|^4\,dg=2,
\]
then \(K\) is finite or \(K=SU(n)\). Thus an infinite compact subgroup with this fourth moment is the whole special unitary group; in particular the same conclusion holds if \(K\) is connected.

*Proof.* Under conjugation, \(\operatorname{End}(\mathbb C^n)=\mathbb CI\oplus\mathfrak{sl}_n(\mathbb C)\). The first summand is trivial. Proposition 3.6 identifies the fourth moment with the sum of squares of irreducible multiplicities in this representation. A sum equal to two forces exactly two distinct irreducibles, each once; therefore the nonzero trace-zero summand is irreducible for \(K\).

The [closed-subgroup theorem used in lesson five](RT-CPT-05.md) makes \(K\) a compact Lie group. Its real Lie algebra \(\mathfrak k\subset\mathfrak{su}(n)\) is invariant under conjugation by every element of \(K\). Moreover
\[
\mathfrak{su}(n)\otimes_{\mathbb R}\mathbb C
\simeq\mathfrak{sl}_n(\mathbb C).
\]
Indeed, a trace-zero matrix splits uniquely into a skew-Hermitian part and \(i\) times a skew-Hermitian part, by its Hermitian/skew-Hermitian decomposition; the intersection is zero. Thus \(\mathfrak k_{\mathbb C}\) is an invariant complex subspace of the irreducible trace-zero representation. It is zero or the whole space. In the zero case \(K\) is zero dimensional, hence discrete and finite by compactness. In the other case \(\mathfrak k=\mathfrak{su}(n)\). Their exponentials then give an identity neighborhood of \(SU(n)\) inside \(K\), so \(K\) is open. Connectedness of \(SU(n)\), proved with the classical matrix examples in lesson five, forces \(K=SU(n)\). \(\square\)

The finite alternative is necessary even in dimension two. In the unit quaternions, let \(Q=\{\pm1,\pm i,\pm j,\pm k\}\) and \(q=(1+i+j+k)/2\). Conjugation by \(q\) cycles \(i,j,k\), and \(q^3=-1\); hence
\[
K=Q\cup Qq\cup Qq^2
\]
is a group of order 24. The cosets are distinct, and the last sixteen elements have all four quaternion coordinates equal to \(\pm\tfrac12\). In its defining \(SU(2)\)-representation the trace is twice the real coordinate. The traces are \(2,-2\) once each, zero six times, and \(1,-1\) eight times each. Consequently
\[
M_2=\frac{8+16}{24}=1,
\qquad M_4=\frac{32+16}{24}=2.
\]
Thus this finite group and \(SU(2)\) have the same second and fourth defining trace moments. For \(SU(2)\), the latter values follow directly from \(\pi_1\otimes\pi_1^*=\pi_0\oplus\pi_2\). Two moments provide the alternative, not a complete reconstruction of the group.

## Dimension series and trace laws

For a compact semisimple group define, in a region of absolute convergence,
\[
\zeta_G(s)=\sum_{[\pi]\in\widehat G}(\dim\pi)^{-s}.
\]
This dimension series depends on the global group: only its analytic highest weights are summed. It is different from a Laplace spectral series, which uses \(c_B(\lambda)\) and includes the multiplicity \((\dim\pi_\lambda)^2\).

**Proposition 4.1.**
\[
\zeta_{SU(2)}(s)=\zeta(s)\quad(\operatorname{Re}s>1),
\]
\[
\zeta_{SU(3)}(s)=
2^s\sum_{a,b\geq0}
\bigl((a+1)(b+1)(a+b+2)\bigr)^{-s}. \tag{4.2}
\]
The latter converges absolutely exactly for \(\operatorname{Re}s>2/3\).

*Proof.* The dimensions of \(\pi_m\) are \(m+1\), proving the first identity with its convergence range. The \(SU(3)\) dimension formula proves (4.2) term by term. Put \(u=a+1,v=b+1\), and let \(\sigma=\operatorname{Re}s\). For \(\sigma>1\), domination by \(\sum u^{-\sigma}v^{-\sigma}\) gives absolute convergence.

For \(2/3<\sigma<1\), split into \(u\geq v\) and its transpose. Since \(u+v\geq u\), one half is bounded by
\[
\sum_{u\geq1}u^{-2\sigma}\sum_{v=1}^u v^{-\sigma}
\leq C_\sigma\sum_{u\geq1}u^{1-3\sigma}<\infty.
\]
At \(\sigma=1\), replace the inner bound by \(1+\log u\). Conversely, on each disjoint square \(2^k\leq u,v<2^{k+1}\), the product \(uv(u+v)\) is comparable to \(2^{3k}\). Its contribution to the absolute series is bounded below by a positive constant depending on \(\sigma\) times \(2^{k(2-3\sigma)}\). This does not tend to zero when \(\sigma\leq2/3\). \(\square\)

For contrast, the \(SO(3)\) series sums only odd dimensions:
\[
\zeta_{SO(3)}(s)=\sum_{\ell\geq0}(2\ell+1)^{-s}
=(1-2^{-s})\zeta(s),\qquad \operatorname{Re}s>1.
\]
Already \(U(1)\), and also \(U(n)\) through the determinant characters, has infinitely many one-dimensional irreducibles. Its corresponding dimension sum diverges for every \(s\); the semisimple qualification matters.

Komori–Matsumoto–Tsumura define the multivariable root-system series
\[
Z_\Phi((s_\alpha))=
\sum_{n_1,\ldots,n_r\geq1}
\prod_{\alpha>0}
\left\langle\sum_j n_j\omega_j,\alpha^\vee\right\rangle^{-s_\alpha}.
\]
For the simply connected compact semisimple group, the dimension formula makes its Witten series the specialization
\[
\zeta_G(s)=
\left(\prod_{\alpha>0}\langle\rho,\alpha^\vee\rangle\right)^s
Z_\Phi((s)_{\alpha>0}).
\]
For a quotient group one restricts the summation to the allowed shifted weights. No claim about analytic continuation or special values follows merely from this identity.

Trace distributions are a different application of Haar integration. For a real-valued character \(\tau\), its law is the pushforward measure defined by
\(\int F(x)\,d\mu_\tau(x)=\int_G F(\tau(g))\,dg\).
An arbitrary unitary character can be complex-valued; its pushforward then lives in \(\mathbb C\).

For \(SU(2)\), write \(\tau(g)=2\cos\theta\). The previously proved density \((2/\pi)\sin^2\theta\,d\theta\), \(0\leq\theta\leq\pi\), gives
\[
d\mu_\tau(x)=\frac1{2\pi}\sqrt{4-x^2}\,
\mathbf1_{[-2,2]}(x)\,dx. \tag{4.3}
\]
Indeed \(|dx|=2\sin\theta\,d\theta\). Its even moments are the Catalan numbers
\[
\int x^{2k}\,d\mu_\tau(x)
=\frac{(2k)!}{k!(k+1)!},
\]
and odd moments vanish. For the even formula substitute \(x=2t\), then \(u=t^2\); the beta integral gives
\[
\frac{2^{2k+1}}{\pi}B(k+\tfrac12,\tfrac32)
=\frac{(2k)!}{k!(k+1)!}.
\]
Here the substitution \(t=\sin\theta\) gives \(B(\tfrac12,\tfrac32)=\pi/2\), and integration by parts gives
\[
B(k+\tfrac32,\tfrac32)=
\frac{k+\tfrac12}{k+2}B(k+\tfrac12,\tfrac32).
\]
The resulting recurrence and initial value prove the displayed moment formula.

For \(USp(2g)\), eigenvalues come in pairs \(e^{\pm i\theta_j}\), so the defining trace is real and equals \(\sum_j x_j\), where \(x_j=2\cos\theta_j\). Lesson eight's symplectic integration formula therefore gives its law explicitly as
\[
\int F(x)\,d\mu_\tau(x)
=\frac1{g!(2\pi)^g}
\int_{[-2,2]^g}F\left(\sum_j x_j\right)
\prod_{i<j}(x_i-x_j)^2
\prod_j\sqrt{4-x_j^2}\,dx. \tag{4.4}
\]
The support is \([-2g,2g]\): all sums in that interval are attained, and every neighborhood of an attained sum contains torus points with positive density. For \(g=2\), a one-dimensional expression is
\[
f_\tau(s)=
\frac1{8\pi^2}
\int_{\max(-2,s-2)}^{\min(2,s+2)}
(2x-s)^2\sqrt{(4-x^2)(4-(s-x)^2)}\,dx,
\quad |s|\leq4.
\]
This follows by the determinant-one change \((x,y)\mapsto(x,s=x+y)\); it is zero outside the interval. Lachaud studies further special-function forms and arithmetic applications. The Haar law here supplies the measure used in such statements; it does not prove Frobenius equidistribution.

## Exercises with complete solutions

**Exercise 1 (easy).** Compute \(C_B\) on \(\pi_m\) of \(SU(2)\), for \(B(X,Y)=-\operatorname{tr}(XY)/2\).

*Solution.* Take \(H=\operatorname{diag}(i,-i)\), of length one. The highest vector in \(\operatorname{Sym}^m\mathbb C^2\) has derivative \(im\), so its analytic weight evaluates as \(\lambda(H)=m/(2\pi)\). The positive root evaluates as \(1/\pi\), whence \(\rho(H)=1/(2\pi)\). Formula (1.3) gives
\[
c_B(m)=4\pi^2\frac{m}{2\pi}\frac{m+2}{2\pi}=m(m+2).
\]
Equivalently the orthonormal quaternion basis is \(i\sigma_k\), whereas the angular-momentum matrices are \(S_k=\sigma_k/2\). Thus \(-\sum d\pi(i\sigma_k)^2=4\sum S_k^2=4j(j+1)\), with \(j=m/2\). The defining representation has eigenvalue three, not \(3/4\); the latter belongs to an unrescaled spin-generator sum.

**Exercise 2 (medium).** Derive Clebsch–Gordan from Theorem 3.1.

*Solution.* In integer \(SU(2)\) labels the positive root is two, \(\rho=1\), and the weights of \(\pi_n\) are \(-n,-n+2,\ldots,n\), each once. Formula (3.2) becomes, for \(k\geq0\),
\[
N_{mn}^{k}=m_n(k-m)-m_n(-k-m-2).
\]
Interchange tensor factors if necessary so that \(m\geq n\). The second argument has absolute value at least \(m+2>n\), hence contributes zero. The first is a weight exactly when \(m-n\leq k\leq m+n\) and \(k\equiv m+n\pmod2\). Therefore
\[
\pi_m\otimes\pi_n=
\bigoplus_{j=0}^{\min(m,n)}\pi_{m+n-2j}.
\]
There are no other labels and every listed multiplicity is one. The dimensions sum to
\(\sum_{j=0}^n(m+n-2j+1)=(m+1)(n+1)\) when \(m\geq n\). For instance \(\pi_2\otimes\pi_1=\pi_3\oplus\pi_1\).

**Exercise 3 (medium).** Verify \(3\otimes\overline3=8\oplus1\) by weights and by (3.2).

*Solution.* Its weights are \(p_i-p_j\): the six roots each once and zero three times. The adjoint has those six root weights and zero twice; the trivial character supplies the remaining zero. The adjoint of \(\mathfrak{sl}_3\) is irreducible, with highest root \(\omega_1+\omega_2\), so character equality and complete reducibility prove the decomposition.

For the signed calculation, take \(\lambda=\omega_1=p_1\), \(\mu=\omega_2=-p_3\), and \(\rho=(1,0,-1)\). The weights of \(\mu\) are \(-p_1,-p_2,-p_3\), each once. In the equivalent coefficient version of the proof of Theorem 3.1, a contribution requires
\[
w(\lambda+\rho)=\nu+\rho+p_j.
\]
For \(\nu=0\), the six coordinates of \(w(\lambda+\rho)\) are permutations of
\((5/3,-1/3,-4/3)\). Among the three candidates \(\rho+p_j\), only \(\rho+p_1\) has that coordinate multiset; it is the identity permutation, with positive sign. Thus the trivial multiplicity is one.

For \(\nu=\omega_1+\omega_2=(1,0,-1)\), the candidates are \(2\rho+p_j\). Only \(2\rho+p_3=(5/3,-1/3,-4/3)\) is a permutation of \(\lambda+\rho\); it is again the identity, so the adjoint multiplicity is one. Their dimensions are one and eight and sum to nine, the full tensor dimension. Since complete reducibility gives nonnegative multiplicities, no other summand can remain. This checks the signed formula without inferring a decomposition solely from dimensions.

**Exercise 4 (hard).** Prove Theorem 3.1, including its global-group restriction and its reflected signs.

*Solution.* Decompose the finite tensor representation into actual irreducibles and multiply its character identity by the formal \(A_\rho\). The Weyl formula converts every summand to \(A_{\tau+\rho}\), and strict dominance makes the coefficient of \(e^{\nu+\rho}\) isolate precisely the multiplicity of \(\nu\). On the other side, expand \(\chi_\mu A_{\lambda+\rho}\); the coefficient is the sum of the Weyl determinant signs times \(m_\mu(\nu+\rho-w(\lambda+\rho))\). Weyl invariance of the weight multiplicities and inversion in the finite group convert it into (3.2).

The weights inserted into \(m_\mu\) are actual characters: \(w\rho-\rho\in Q\subset X^*(T)\). The formal coefficient extraction is valid even if \(\rho\) itself is not analytic. Thus the argument proves the formula for the actual group without inadvertently adding representations of a cover. A term reflected across an odd number of root walls has sign minus; the example \(N_{0,2}^{0}=1-1=0\) proves that these signs cannot be replaced by positive counts.

## Source comparisons and limits

The claim following (3.4.62) about a full independent family from adjoint traces also needs qualification. On \(\mathfrak{sl}_3\), \(\operatorname{tr}(\operatorname{ad}H)^3=0\) for every diagonal \(H\), since its nonzero eigenvalues occur in opposite root pairs. This construction has zero cubic leading symbol, whereas the independent cubic invariant \(\operatorname{tr}(H^3)\) need not vanish. General higher Casimirs require suitable invariant tensors; no classification of the enveloping-algebra center is used here.

Komori–Matsumoto–Tsumura Sections 1.5–1.6 and Proposition 3.5 organize these dimension sums into root-system zeta functions. Their Lie-algebra sum corresponds to all dominant integral weights; the compact quotient's analytic lattice can select fewer. Lachaud Sections 1–3 discuss real trace laws, with \(USp(2g)\) as the principal example. The real-valued hypothesis must be retained: the defining character of \(U(1)\) takes the value \(i\). The symplectic representation has complex dimension \(2g\), with dimension four only when \(g=2\).

## What this lesson does not prove

The root-plane decomposition and highest-vector annihilation come from lessons seven and ten. Smooth coefficients, Schur orthogonality, Peter–Weyl, and the Weyl character and dimension formulas are the established results of lessons five, two and eleven. The elementary enveloping algebra construction is the prerequisite in [**RT-LIE-13**, §2](course:RT-LIE/RT-LIE-13#2-ordered-words-and-the-complete-pbw-proof); no higher-center theorem is asserted. The spherical harmonic completeness and symplectic integration formula are from lessons four and eight. The general beta integral can be replaced here by the elementary recurrence just specified. Analytic continuation, special values and functional relations for root-system zeta functions, and arithmetic Sato–Tate equidistribution, remain outside this lesson.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §27. The Casimir eigenvalue used in its character argument gives a normalization comparison. The metric-scaled compact Casimir, full self-adjoint Laplacian domain and tensor/dimension statements above are proved here.

Emmanuel Kowalski, [*An introduction to the representation theory of groups*, author 2025 edition](https://people.math.ethz.ch/~kowalski/representation-theory-2025.pdf), Lemma 6.3.3 and Theorem 6.3.2 with proof, printed pages 251–254 (accessed 3 October 2026), is the source comparison for Larsen’s unitary alternative. Michael Larsen, [*The Normal Distribution as a Limit of Generalized Sato-Tate Measures*, arXiv:0810.2012v1](https://arxiv.org/abs/0810.2012v1), §3.1, page 10, explains the tensor-moment method in its self-dual setting. Proposition 3.6 here includes the dual explicitly and proves the absolute-moment identity for arbitrary compact groups. The binary tetrahedral calculation supplies a complete finite counterexample to deciding between the two alternatives from these moments alone.

Michael E. Taylor, [*Introduction to Lie Groups*, author PDF](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2021/03/liegp.pdf), §5.1 compares Casimir and Laplace eigenvalues. Alexander Kirillov, Jr., [*Introduction to Lie Groups and Lie Algebras*, preliminary author draft](https://www.math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf), Proposition 6.15 gives invariant-form centrality (both accessed 3 October 2026). The radial differential expression in Proposition 2.4 is derived here from the already proved Weyl integration formula; its angular normalization is compared with these metric Casimir treatments.
