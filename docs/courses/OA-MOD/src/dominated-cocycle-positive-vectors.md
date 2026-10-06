# Positive vectors at half and quarter modular time

**Independently written mathematical draft.**

A domination inequality between two normal positive functionals gives a bounded imaginary-time cocycle. Its half-time value sends one positive implementing vector to the other. Its quarter-time value does the same through a left and a right action. We will prove both statements when either functional can have a kernel, without assuming that the ambient algebra has a faithful normal state.

The source problem is Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(4). The argument here first constructs an intrinsic supported cocycle, then proves a general quarter-time vector identity by Gaussian approximation. Its prerequisites are the written standard-form corner and comparison proofs, the four-slot matrix construction, balanced modular orbits, the centralizer and restriction criteria, and the operator half-strip criterion. The spectral vector strips and Gaussian integrals supply the exact limiting domains used below.

Inner products are linear in the first variable. In a standard form \((M,H,J,P)\), write \(\xi_\rho\in P\) for the unique vector representing \(\rho\in M_*^+\). For \(v\in H\) and \(b\in M\), right multiplication means

\[
 v b=Jb^*Jv.
 \tag{CQ.1}
\]

In particular, \(a v a^*=aJaJv\); the second action is a commutant action, not another left multiplication.

## Keep both vectors in the denominator's support

Suppose \(\varphi,\psi\in M_*^+\) and \(\varphi\le C\psi\), where \(0\le C<\infty\). Let \(e=s(\psi)\) and \(p=s(\varphi)\). Since \(\varphi(1-e)=0\), the support characterization gives \(p\le e\). For completeness, if a positive functional \(\rho\) vanishes on a projection \(1-r\), its Cauchy–Schwarz inequality gives \(\rho((1-r)x)=\rho(x(1-r))=0\); hence \(\rho(x)=\rho(rxr)\). The support is the least such projection. This Cauchy–Schwarz inequality follows by expanding the nonnegative scalar \(\rho((u+\lambda v)^*(u+\lambda v))\) and minimizing in \(\lambda\).

By SE-01/03 the corner \(eMe\) has its faithful standard representation on

\[
 H_e=eJeJH,\qquad P_e=P\cap H_e.
\]

Both \(\xi_\varphi\) and \(\xi_\psi\) lie in \(P_e\): their left supports are at most \(e\), and applying \(J\) gives the same assertion for the right support. Their vector functionals there are the restrictions of \(\varphi,\psi\); uniqueness in SE-11 identifies the corner representatives with these same vectors. The restricted \(\psi\) is faithful. Indeed, for \(x\in(eMe)_+\) with \(\psi(x)=0\), the spectral projections of \(x\) away from zero have zero \(\psi\)-value, so their orthogonality to \(e=s(\psi)\) forces them all to vanish.

Until CQ-06, replace \(M,H,J,P\) by this corner, so that \(\psi\) is faithful and \(e=1\). We retain \(p=s(\varphi)\), which need not be the identity. If \(\varphi=0\), define its supported cocycle to be zero; both desired vector identities are then zero identities. This also covers \(C=0\), and \(\psi=0\) forces \(\varphi=0\). Hence the construction below may assume \(\varphi\ne0\) and \(C>0\).

## Construct the cocycle without losing a kernel

Put \(q=1-p\) and introduce the auxiliary finite functional

\[
 \chi(x)=\varphi(x)+\psi(qxq).
\]

It is positive and normal. It is faithful: if \(x\ge0\) and \(\chi(x)=0\), faithfulness of \(\varphi\) on \(pMp\) gives \(pxp=0\), and faithfulness of \(\psi\) gives \(qxq=0\). Thus \(x^{1/2}p=x^{1/2}q=0\), and \(x=0\). Moreover, for every \(x\in M\),

\[
 \chi(px)=\chi(xp)=\varphi(x).
\]

All finite linear domains equal \(M\) here. The centralizer criterion CZ-05 therefore gives \(p\in M_\chi\).

Write \(\theta=\xi_\chi\) and \(\zeta=\xi_\varphi\). We will need the exact vector identity

\[
 p\theta=\zeta.
 \tag{CQ.2}
\]

Since \(\sigma_t^\chi(p)=p\) and \(\Delta_\chi^{it}\theta=\theta\), the vector \(p\theta\) is fixed by every \(\Delta_\chi^{it}\). A vector fixed by all the imaginary powers of an injective positive operator has spectral measure supported at \(1\): integrate \(|\lambda^{it}-1|^2\) for rational \(t\), and use continuity in \(t\). Consequently \(\Delta_\chi^{1/2}p\theta=p\theta\). The finite Tomita identity \(S_\chi(p\theta)=p\theta\), with \(S_\chi=J\Delta_\chi^{1/2}\), now gives \(Jp\theta=p\theta\). Hence \(p\theta=pJpJ\theta\in P\). Its functional is \(x\mapsto\chi(pxp)=\varphi(x)\); uniqueness proves (CQ.2).

On \(N=M_2(M)\) take the faithful finite functional and the off-diagonal operator

\[
 \begin{gathered}
 \Omega(X)=\chi(X_{11})+\psi(X_{22}),\\
 a=pE_{12}.
 \end{gathered}
\]

Here \(E_{ij}\) are the scalar matrix units. GC-03/04 prove that \(\alpha_t=\sigma_t^\Omega\) fixes the diagonal matrix units, restricts to \(\sigma^\chi,\sigma^\psi\) on the two diagonal corners, and has

\[
 \begin{gathered}
 \alpha_t(E_{12})=d_tE_{12},\\
 d_t=[D\chi:D\psi]_t,\\
 \alpha_t(a)=c_tE_{12},\qquad c_t=p d_t.
 \end{gathered}
\]

The fixedness of \(p\) under \(\sigma^\chi\) also gives \(p d_t=d_t\sigma_t^\psi(p)\). Thus

\[
 \begin{gathered}
 c_0=p,\\
 c_tc_t^*=p,\\
 c_t^*c_t=\sigma_t^\psi(p),\\
 c_s\sigma_s^\psi(c_t)\\
 =c_{s+t}.
 \end{gathered}
 \tag{CQ.3}
\]

For the last equality, expand the left side as \(p d_s\sigma_s^\psi(p)\sigma_s^\psi(d_t)\), use \(d_s\sigma_s^\psi(p)=p d_s\), and then the faithful cocycle identity for \(d\). Strong-star continuity follows from that of \(d\). If \(x\in pMp\), the same calculation and CZ-09 give

\[
 c_t\sigma_t^\psi(x)c_t^*=\sigma_t^{\varphi|_{pMp}}(x).
\]

**Why the auxiliary extension disappears.** The projection \(Q=pE_{11}+E_{22}\) belongs to \(N_\Omega\). The restricted faithful functional on \(QNQ\) is

\[
 \Omega_Q(X)=\varphi(X_{11})+\psi(X_{22}).
\]

This algebra and functional depend only on \(\varphi,\psi\), and \(a\in QNQ\). CZ-09 identifies its modular group with the restriction of \(\alpha\). Hence \(c_tE_{12}=\sigma_t^{\Omega_Q}(a)\) is intrinsic. Any other faithful extension satisfying \(p\in M_\chi\) and \(\chi(pxp)=\varphi(x)\) gives exactly this group and orbit. This defines the supported cocycle \([D\varphi:D\psi]_t=c_t\); when \(p=1\) it is the faithful cocycle of GC-04. In general its identity-time value is \(p\), not \(1\). The support identities in (CQ.3) are assertions about real time.

## Domination supplies the closed half-strip

For \(X\in N_+\), direct matrix multiplication gives

\[
 \begin{aligned}
 \Omega(aXa^*)&=\chi(pX_{22}p)\\
 &=\varphi(X_{22})\\
 &\le C\psi(X_{22})\le C\Omega(X).
 \end{aligned}
\]

HS-02, applied to \(a/\sqrt C\) in the faithful \(\Omega\)-GNS representation, gives an \(N\)-valued extension \(A(z)\) of \(\alpha_t(a)\) to

\[
 \mathcal S=\{z:-1/2\le\operatorname{Im}z\le0\}.
\]

It is bounded and sigma-weakly continuous on \(\mathcal S\), norm holomorphic inside, and \(\|A(-i/2)\|\le\sqrt C\). Since \(\|a\|=1\), the weighted strip estimate HS-01 gives

\[
 \|A(t-iy)\|\le C^y\qquad(0\le y\le1/2).
\]

Apply the scalar boundary uniqueness of MA-08 to the normal matrix-entry maps. The real orbit has only a \((1,2)\) entry, and its left multiplication by \(pE_{11}\) leaves it unchanged. These identities therefore hold throughout the strip. Write

\[
 A(z)=c_zE_{12},\qquad pc_z=c_z.
\]

The family \(c_z\in M\) has the same topologies and norm bound. It is the unique bounded closed-strip continuation of (CQ.3), so it is independent of \(\chi\) on the entire strip as well. The symbols \(c_{-i/2}\) and \(c_{-i/4}\) now denote bounded operators with specified domains, not formal products of unbounded imaginary powers. No norm continuity of the real boundary is asserted.

## A general vector identity at quarter time

We prove the analytic fact that will turn the matrix orbit into positive vectors. Let \(\omega\) be the positive cyclic separating vector of any faithful finite normal functional on a von Neumann algebra \(L\). Write its modular objects as \(D,J_0\), and \(\beta_t=\operatorname{Ad}(D^{it})\). Suppose \(a\in L\) has a bounded closed lower half-strip continuation \(A(z)\) of \(\beta_t(a)\), in the topologies of CQ-03. Then

\[
 \begin{gathered}
 A(-i/2)\omega\\
 =J_0a^*\omega.
 \end{gathered}
 \tag{CQ.4}
\]

Indeed, \(a\omega\in D(D^{1/2})\) by the finite Tomita domain, and \(D^{1/2}a\omega=J_0a^*\omega\). MA-09 gives the bounded continuous vector strip \(D^{iz}a\omega\). On its real edge it is \(A(t)\omega\), since \(D^{it}\omega=\omega\). Scalar boundary uniqueness against every Hilbert vector identifies the two strips and proves (CQ.4).

Put \(b=A(-i/4)\). The stronger identity is

\[
 \begin{gathered}
 bJ_0bJ_0\omega\\
 =D^{1/4}aa^*\omega.
 \end{gathered}
 \tag{CQ.5}
\]

It includes the assertion \(aa^*\omega\in D(D^{1/4})\). First suppose \(a\) is an entire element for \(\beta\). Then \(b=\beta_{-i/4}(a)\), and adjoint reflection gives \(b^*=\beta_{i/4}(a^*)\). The finite Tomita formula and the spectral vector identities for entire elements give

\[
 \begin{aligned}
 J_0bJ_0\omega
 &=D^{1/2}b^*\omega\\
 &=\beta_{-i/4}(a^*)\omega.
 \end{aligned}
\]

Multiplying by \(b\) proves (CQ.5), because the entire extension preserves products. To see this last assertion without a domain convention, extend \(\beta_t(xy)=\beta_t(x)\beta_t(y)\) by the scalar identity theorem. Likewise \(\beta_z(x)\omega=D^{iz}x\omega\) follows from MA-09 on every finite strip; it supplies the actual power domains just used.

For general \(a\), use the Gaussian kernels and the entire elements of MA-16:

\[
 \begin{gathered}
 g_r(t)=\sqrt{r/\pi}\,e^{-rt^2},\\
 a_r=\int_{\mathbb R}g_r(t)\beta_t(a)\,dt,\\
 b_r=\int_{\mathbb R}g_r(t)\beta_t(b)\,dt.
 \end{gathered}
\]

The integrals are vectorwise strong integrals. Real modular orbits are strongly-star continuous; applying the approximate-identity estimate of MA-16 to the operator and its adjoint gives \(a_r\to a\) and \(b_r\to b\) strongly-star, with \(\|a_r\|\le\|a\|\) and \(\|b_r\|\le\|b\|\).

Here it is essential that \(b_r\) really is the quarter-time value of \(a_r\). Boundary uniqueness first gives \(A(t+z)=\beta_t(A(z))\). The sigma-weak integral

\[
 F_r(z)=\int_{\mathbb R}g_r(t)A(t+z)\,dt
\]

is bounded and sigma-weakly continuous on the closed strip and holomorphic inside: boundedness controls the tails, scalar dominated convergence gives continuity, and local Cauchy estimates justify differentiation under the integral. On the real edge it agrees with \(\beta_s(a_r)\). The Gaussian entire continuation of \(a_r\) is bounded on this strip by the explicit MA-16 estimate, so uniqueness identifies it with \(F_r\). Thus \(\beta_{-i/4}(a_r)=b_r\).

The entire-element case gives \(D^{1/4}a_ra_r^*\omega=b_rJ_0b_rJ_0\omega\). Uniform boundedness and strong-star convergence imply convergence of both products to their unsmoothed products. Closedness of \(D^{1/4}\) now proves its asserted domain and (CQ.5). No passage through an unbounded operator has been justified by weak convergence alone.

In particular, if \(aa^*\in L_\omega\), the spectral fixed-vector argument of CQ-02 gives \(D^{1/4}aa^*\omega=aa^*\omega\). Hence in this case

\[
 bJ_0bJ_0\omega=aa^*\omega.
\]

## Read the two identities in matrix coordinates

Return to \(\Omega,a,A\) of CQ-02/03, and set \(\eta=\xi_\psi\). We need the conjugation in the matrix GNS space, including its off-diagonal entries. SF-08 identifies that Hilbert space with four copies of the two column GNS spaces. After the canonical comparisons of SF-09/13 and SE-10, all four slots are copies of \(H\), with

\[
 \begin{gathered}
 \Lambda_\Omega(X)_{ij}=X_{ij}\xi_j,\\
 \xi_1=\theta,\qquad \xi_2=\eta,\\
 \omega=\Lambda_\Omega(1)
   =\begin{pmatrix}\theta&0\\0&\eta\end{pmatrix}.
 \end{gathered}
\]

The identification is unitary because the squared GNS norm is \(\sum_{i,j}\|X_{ij}\xi_j\|^2\), and each column GNS range is dense. Left multiplication is ordinary matrix multiplication on the slots. The modular conjugation is

\[
 (J_\Omega V)_{ij}=J V_{ji}.
\]

This is the transported polar conjugation, not an arbitrary choice: in SF-08 the slot polar map is \(K_{ij}:H_j\to H_i\), and SF-13 proves \(I_iK_{ij}=JI_j\) for the canonical comparisons into \(H\). These equalities give the displayed formula in every slot. The finite GNS identity vector is its positive implementing vector; SE-10/11 identifies each diagonal vector with the corresponding \(\xi_j\).

Apply (CQ.4). The matrix \(a^*\omega\) has only entry \((2,1)\), equal to \(p\theta=\zeta\). Its conjugate therefore has only entry \((1,2)\), equal to \(J\zeta=\zeta\). The same entry of \(A(-i/2)\omega\) is \(c_{-i/2}\eta\). Consequently

\[
 c_{-i/2}\eta=\zeta.
\]

For quarter time, write \(B=A(-i/4)=c_{-i/4}E_{12}\). Since \(aa^*=pE_{11}\in N_\Omega\), (CQ.5) gives

\[
 BJ_\Omega BJ_\Omega\omega=pE_{11}\omega.
\]

Its only nonzero entry is \((1,1)\). On the left that entry is

\[
 c_{-i/4}Jc_{-i/4}J\eta
   =c_{-i/4}\eta c_{-i/4}^*;
\]

on the right it is \(p\theta=\zeta\). This proves the second identity with the correct right action.

## The full supported theorem and a singular matrix test

Restore the original algebra and \(e=s(\psi)\). Define the supported cocycle in \(eMe\) as in CQ-02, and embed its coefficients into \(M\) by zero off \(e\). The faithful corner representation is a normal isomorphism onto its represented algebra (SE-03 and UB-08), so the closed-strip topology and holomorphy are preserved by this identification. The restricted conjugation is the original \(J\) on \(H_e\), and both vectors lie in \(H_e\). Thus the corner identities proved above are exactly the ambient identities

\[
 \begin{gathered}
 \xi_\varphi=c_{-i/2}\xi_\psi,\\
 \xi_\varphi\\
 =c_{-i/4}\xi_\psi c_{-i/4}^*.
 \end{gathered}
 \tag{CQ.6}
\]

Here \(c_t=[D\varphi:D\psi]_t\) and \(c_0=s(\varphi)\). For \(C>0\), the estimate is \(\|c_{t-iy}\|\le C^y\) for \(0\le y\le1/2\). At zero functionals use the zero continuation from CQ-01, whose norm is zero everywhere; no expression \(0^{it}\) or \(0^0\) is needed. This proves both formulas for all normal positive bounded functionals with the stated domination, including kernels and an ambient algebra of arbitrary cardinality.

**A singular, noncommuting test.** In the Hilbert–Schmidt standard form of \(M_2(\mathbb C)\), let

\[
 h=\begin{pmatrix}1&0\\0&4\end{pmatrix},\qquad
 k=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

and \(\psi(x)=\operatorname{Tr}(hx)\), \(\varphi(x)=\operatorname{Tr}(kx)\). Set \(p=k/2\), a rank-one projection. Direct calculation gives

\[
 h^{-1/2}kh^{-1/2}
   =\begin{pmatrix}1&1/2\\1/2&1/4\end{pmatrix}.
\]

Its eigenvalues are \(0,5/4\). Congruence and rank-one tests therefore show that the least domination constant is \(C=5/4\). On \(pH\) the positive density \(k\) has the single eigenvalue \(2\). The cocycle is

\[
 c_z=2^{iz}p h^{-iz}.
\]

To verify the expression directly, the auxiliary faithful density in CQ-02 is \(k+qhq\), whose restriction to \(p\) is \(2p\). The faithful finite-matrix formula of GC-09 gives \(d_t=(k+qhq)^{it}h^{-it}\); multiplication by \(p\) gives the stated \(c_t\). Uniqueness then identifies its displayed entire continuation on the half-strip. In particular \(c_0=p\), and \(p\) does not commute with \(h\). Since \(\xi_\psi=h^{1/2}\) and \(\xi_\varphi=k^{1/2}=\sqrt2\,p\), multiplication gives

\[
 \begin{gathered}
 c_{-i/2}=\sqrt2\,p h^{-1/2},\\
 c_{-i/2}h^{1/2}=\sqrt2\,p,
 \end{gathered}
\]

and

\[
 \begin{gathered}
 c_{-i/4}h^{1/2}c_{-i/4}^*\\
 =\sqrt2\,p\bigl(h^{-1/4}h^{1/2}h^{-1/4}\bigr)p\\
 =\sqrt2\,p.
 \end{gathered}
\]

Both formulas yield the required positive vector. This example also detects two possible mistakes: the real cocycle is a partial isometry with identity-time value \(p\), and the quarter-time formula needs the adjoint on the right even though its output is positive.
