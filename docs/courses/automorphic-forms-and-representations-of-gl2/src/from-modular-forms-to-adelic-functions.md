# From modular forms to adelic functions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A classical cusp form carries three kinds of data: its weight at infinity, its congruence condition at finite primes, and its vanishing at every cusp. We will put these into a single function and recover the classical form from that function. The two numerical comparisons at the end are part of the dictionary: an unnormalized spherical convolution and a classical Hecke operator have different eigenvalues, and a fixed adelic Haar measure gives a level-dependent multiple of the Petersson product.

We assume the definition of a holomorphic cusp form at all rational cusps, elementary complex analysis, Dirichlet characters and the Chinese remainder theorem. We use the decomposition and measures proved in Adèles for GL₂ and strong approximation, especially Theorems 4.1–4.2 and Section 2. Classical modularity of the two forms used in Section 7 is prerequisite data; the calculations of their lifts are done here. For the adelic correspondence compare Deligne, §§1.2–1.3 and 2.1, and Getz–Hahn, §6.7. Our formulas below fix the character side, rotation orientation and convolution side explicitly.

Throughout, \(G=\mathrm{GL}_2\), \(N\geq1\), and \(k\geq1\) is an integer. Let \(\chi:(\mathbb Z/N\mathbb Z)^\times\to\mathbb C^\times\) be a Dirichlet character with \(\chi(-1)=(-1)^k\). Its values on units have absolute value one. Put

\[
K_0(N)=\left\{\begin{pmatrix}a&b\\ c&d\end{pmatrix}\in G(\widehat{\mathbb Z}):c\in N\widehat{\mathbb Z}\right\}.
\]

Our classical convention is

\[
f|_k\gamma=\chi(d_\gamma)f\quad(\gamma\in\Gamma_0(N)),\qquad
(f|_kg)(z)=(\det g)^{k/2}(cz+d)^{-k}f(gz)
\tag{1.1}
\]

for \(g\in G(\mathbb R)^+\). The positive real determinant has its positive square root. The slash operation satisfies \((f|g)|h=f|gh\), by \(j(gh,z)=j(g,hz)j(h,z)\). We write \(S_k(\Gamma_0(N),\chi)\) for this cusp-form space.

## 1. The finite character and its central extension

Regard \(\chi\) as a character of \(\widehat{\mathbb Z}^{\times}\). Define

\[
\lambda(u)=\overline{\chi(d_u)}\quad(u\in K_0(N)).
\tag{1.2}
\]

Here \(d_u\) is reduced modulo \(N\). It is a unit: modulo every prime dividing \(N\), the determinant is \(a_ud_u\). Moreover \(d_{uv}\equiv d_ud_v\pmod N\), because the other summand is \(c_ub_v\). Thus \(\lambda\) is a continuous character of \(K_0(N)\), with an open kernel.

**Proposition 1.1.** There is a unique character \(\omega\) of \(\mathbb A^\times/\mathbb Q^\times\) whose restriction to \(\widehat{\mathbb Z}^{\times}\) is \(\overline\chi\) and whose restriction to \(\mathbb R_{>0}\) is trivial. It is unitary. At infinity it is \(\operatorname{sgn}^{k}\); at a prime \(p\nmid N\) it is unramified and \(\omega_p(p)=\chi(p)\).

**Proof.** Every idèle has a unique expression

\[
z=q\,t\,u,\qquad q\in\mathbb Q^\times,\quad t\in\mathbb R_{>0},\quad u\in\widehat{\mathbb Z}^{\times},
\tag{1.3}
\]

where \(t\) has finite components one and \(u\) has real component one. To construct it, take
\(q=\operatorname{sgn}(z_\infty)\prod_p p^{v_p(z_p)}\), then \(t=z_\infty/q\) and \(u_p=z_p/q\). The product is finite. These formulas also prove uniqueness. Set \(\omega(z)=\overline\chi(u)\). Decomposition (1.3) respects multiplication, so this is a character. It is continuous, trivial on rational idèles, and has the required restrictions; the same decomposition forces uniqueness. All its values have absolute value one.

For the idèle with real component \(-1\) and finite components one, (1.3) has \(q=-1\), \(t=1\), \(u_p=-1\), giving \(\omega_\infty(-1)=\overline\chi(-1)=(-1)^k\). At \(p\nmid N\), the character on \(\mathbb Z_p^\times\) is trivial. The idèle with component \(p\) at \(p\) and one elsewhere has \(q=p\), \(t=p^{-1}\), \(u_p=1\), and \(u_\ell=p^{-1}\) for \(\ell\ne p\). Hence its character value is \(\overline{\chi(p^{-1})}=\chi(p)\). \(\square\)

Writing \(\chi=\prod_{p\mid N}\chi_p\) by the Chinese remainder theorem, we have \(\omega_p|_{\mathbb Z_p^\times}=\overline\chi_p\) at the ramified primes. Therefore the lower-right-entry character in the lift is exactly

\[
\chi_N(u):=\prod_{p\mid N}\omega_p(d_u)=\lambda(u).
\]

The inverse in (1.2) is forced by our left rational invariance and convention (1.1). Changing entries also requires care. On \(K_0(N)\),
\(\chi(a_u)=\chi(\det u)\overline\chi(d_u)\).
Thus the upper-left convention \(\chi(a_u)\) differs from \(\lambda(u)\) by a determinant character. On determinant-one matrices the two agree. A statement about conjugating the character that is valid on \(\Gamma_0(N)\) need not describe the same character of the whole finite compact group.

## 2. The lift and decomposition independence

The determinant of \(K_0(N)\) is all of \(\widehat{\mathbb Z}^{\times}\), as is seen from \(\operatorname{diag}(v,1)\). The preceding lesson therefore gives

\[
G(\mathbb A)=G(\mathbb Q)G(\mathbb R)^+K_0(N).
\tag{2.1}
\]

Real and finite factors in this formula occupy their respective places. For \(f\in S_k(\Gamma_0(N),\chi)\), define

\[
\phi_f(\gamma g_\infty u)=(f|_kg_\infty)(i)\lambda(u).
\tag{2.2}
\]

**Theorem 2.1.** Formula (2.2) is well defined and linear in \(f\). It gives a smooth function on \(G(\mathbb Q)\backslash G(\mathbb A)\) with

\[
\phi_f(gu)=\lambda(u)\phi_f(g),\qquad
\phi_f(gz)=\omega(z)\phi_f(g).
\tag{2.3}
\]

For the rotation
\(r(\theta)=\begin{pmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{pmatrix}\), it satisfies
\(\phi_f(gr(\theta))=e^{ik\theta}\phi_f(g)\).

**Proof.** Suppose \(\gamma g_\infty u=\gamma' g'_\infty u'\). Set \(\delta=\gamma'^{-1}\gamma\). Comparing finite components gives \(\delta_f=u'u^{-1}\in K_0(N)\). A rational matrix integral and invertible at all finite primes belongs to \(G(\mathbb Z)\): its entries are integers and its determinant is a rational unit at all primes, hence \(\pm1\). Comparing real components gives \(g'_\infty=\delta_\infty g_\infty\); both real determinants are positive, so \(\det\delta=1\). Consequently \(\delta\in\Gamma_0(N)\). Now

\[
(f|g'_\infty)(i)\lambda(u')
=\chi(d_\delta)(f|g_\infty)(i)\lambda(\delta_f)\lambda(u)
=(f|g_\infty)(i)\lambda(u).
\]

The two character factors cancel. Changing the left rational factor proves left invariance. Multiplication on the right by a finite \(u_0\in K_0(N)\) proves the first identity in (2.3). Smoothness follows from the real slash formula and the open kernel of \(\lambda\).

The rotation fixes \(i\), has determinant one, and has \(j(r(\theta),i)=e^{-i\theta}\). The slash formula gives the stated type. In particular the scalar \(-I=r(\pi)\) acts by \((-1)^k\). A positive real scalar acts trivially, since its determinant contribution cancels its denominator contribution. A finite unit scalar acts by \(\overline\chi(u)=\omega(u)\). Finally a rational scalar acts trivially by left invariance. Decomposition (1.3) therefore proves the central-character identity for every idèle. \(\square\)

For \(z=x+iy\), put

\[
s(z)=\begin{pmatrix}\sqrt y&x/\sqrt y\\ 0&1/\sqrt y\end{pmatrix}.
\]

The most useful real formula is

\[
\phi_f(s(z)r(\theta))=e^{ik\theta}y^{k/2}f(z).
\tag{2.4}
\]

A nonzero adelic character does not prevent recovery of \(f\): at finite component one and \(\theta=0\), multiply (2.4) by \(y^{-k/2}\).

## 3. Holomorphy as a differential equation

Let \(R(X)\) denote differentiation along \(g\exp(tX)\), extended complex linearly. In \(\mathfrak{sl}_2(\mathbb R)\) set

\[
H=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},\quad
S=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\quad
L=\tfrac12 R(H-iS).
\]

**Proposition 3.1.** In the coordinates \(s(z)r(\theta)\), on functions trivial under positive real scalars,

\[
L=e^{-2i\theta}\left(-iy\partial_x+y\partial_y+\frac i2\partial_\theta\right).
\tag{3.1}
\]

If \(\Phi(s(z)r(\theta))=e^{ik\theta}F(z)\), then

\[
L\Phi(s(z)r(\theta))
=e^{i(k-2)\theta}\left(-2iy\partial_{\bar z}-\frac k2\right)F(z).
\tag{3.2}
\]

For \(F=y^{k/2}f\), this equals
\(-2i e^{i(k-2)\theta}y^{k/2+1}\partial_{\bar z}f\).
Thus \(L\phi_f=0\), and the same equation recovers holomorphy in the inverse construction.

**Proof.** At \(\theta=0\), right multiplication by \(\exp(tH)\) changes \(y\) to \(ye^{2t}\), giving \(R(H)=2y\partial_y\). To first order right multiplication by \(\exp(tS)\) changes \(x\) to \(x+2yt\) and \(\theta\) to \(-t\), giving \(R(S)=2y\partial_x-\partial_\theta\). If \(J=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}\), then \([J,H-iS]=-2i(H-iS)\). Hence \(\operatorname{Ad}(r(\theta))(H-iS)=e^{-2i\theta}(H-iS)\), which supplies the factor in (3.1). Substitution of \(e^{ik\theta}F\) gives (3.2). Finally \(\partial_{\bar z}y^{k/2}=(ik/4)y^{k/2-1}\); its contribution cancels \(-kF/2\). \(\square\)

This also records the infinitesimal eigenvalue. With the weight-\(k\) Casimir normalization

\[
\Omega_k=-y^2(\partial_x^2+\partial_y^2)+iky\partial_x,
\]

holomorphy gives

\[
\Omega_k(y^{k/2}f)=\frac k2\left(1-\frac k2\right)y^{k/2}f.
\tag{3.3}
\]

Indeed the harmonic part of \(f\) contributes zero, the derivative of the factor \(y^{k/2}\) contributes \(-\frac k2(\frac k2-1)F\), and the two first-derivative terms cancel because \(f_y=if_x\). The positive central derivative also kills the lift. Thus these vectors have a fixed infinitesimal character, in addition to their finite compact and rotation types. For the full real maximal compact group \(\mathrm O(2)\), adjoining a reflection adds at most the opposite rotation weight, so their compact translates still span a finite-dimensional space. The convention for \(r(\theta)\) determines the sign of the weight; reversing its orientation reverses that sign and leaves the Haar probability on rotations unchanged.

## 4. All cusps and the inverse correspondence

For a smooth, left rational invariant function \(\Phi\), cuspidality means

\[
\int_{\mathbb Q\backslash\mathbb A}\Phi(n(t)g)\,dt=0
\quad\text{for every }g\in G(\mathbb A),\qquad
n(t)=\begin{pmatrix}1&t\\ 0&1\end{pmatrix}.
\tag{4.1}
\]

The additive measure has \(\operatorname{vol}(\mathbb Q\backslash\mathbb A)=1\). The integral is over a compact space. Rational conjugation gives the equivalent condition for any rational unipotent radical.

We first explain why (4.1) tests every classical cusp. Fix a finite component \(h\in G(\mathbb A_f)\). The decomposition (2.1), applied with a positive real component, gives \(h=\gamma_f u\), with \(\gamma\in G(\mathbb Q)^+\) and \(u\in K_0(N)\). On this finite component, the classical function associated with the lift is

\[
y^{-k/2}\phi_f(s(z),h)=\lambda(u)(f|\gamma^{-1})(z).
\tag{4.2}
\]

Any rational positive matrix \(\gamma^{-1}\) can be written \(\sigma b\), where \(\sigma\in\mathrm{SL}_2(\mathbb Z)\) carries \(\infty\) to the same rational cusp and \(b\) is positive upper triangular. To see this, choose the primitive first column of \(\sigma\) along the first column of \(\gamma^{-1}\), complete it to determinant one, and multiply by \(\sigma^{-1}\). Upper triangular slash merely makes a positive affine change of the variable and multiplies by a constant. Thus the cusp expansion of \(f|\sigma\) gives the expansion of (4.2).

Choose a positive integer \(D\) so that

\[
h^{-1}n(D\widehat{\mathbb Z})h\subset\ker\lambda.
\tag{4.3}
\]

Such an integer exists by continuity and compactness of the integral upper unipotents. A fundamental set for \(\mathbb Q\backslash\mathbb A\) is
\([0,D)\times D\widehat{\mathbb Z}\): the Chinese remainder theorem first adjusts the finite component by a rational number, and multiples of \(D\) then adjust the real component. Two representatives differ only by \(D\mathbb Z\) in the real variable. The finite factor has measure \(D^{-1}\). Therefore, when the real component of \(g\) is \(s(z)r(\theta)\), (4.1) is

\[
\frac{e^{ik\theta}y^{k/2}}{D}
\int_0^D F_h(z+t)\,dt,
\quad F_h(z)=y^{-k/2}\Phi(s(z),h).
\tag{4.4}
\]

This formula also applies to any \(\Phi\) with finite type \(\lambda\) and rotation type \(k\). Positive real scalars make no change. A real component of negative determinant can be changed to a positive one by a rational left multiplication, changing \(h\) as well; hence these tests exhaust \(g\).

**Theorem 4.1.** The lift \(f\mapsto\phi_f\) is a linear bijection from \(S_k(\Gamma_0(N),\chi)\) onto the following space \(A_0(N,k,\omega)\): smooth functions on \(G(\mathbb Q)\backslash G(\mathbb A)\) with central character \(\omega\), finite type \(\lambda\), rotation type \(k\), polynomial growth in the real matrix and its inverse on every fixed finite component, satisfying \(L\Phi=0\) and (4.1). Every lift is bounded modulo the centre and belongs to the corresponding cuspidal \(L^2\) space.

**Proof.** We have already proved the transformation and differential equations. In (4.2), cusp forms have a Fourier expansion with positive exponents at the indicated rational cusp. Choose \(D\) large enough to kill any character in its translation law; its constant coefficient is still zero. Formula (4.4) therefore proves (4.1).

To prove boundedness, pass to \(\ker\lambda\), a compact open subgroup of finite index in \(K_0(N)\). There are only finitely many real arithmetic components, by the determinant decomposition of the preceding lesson. Each such component has a finite-index modular group and finitely many cusp regions. On a cusp region (4.2) is a constant times an upper triangular transform of a cusp expansion, so the lift is bounded by \(C y^{k/2}e^{-cy}\), for positive \(C,c\) appropriate to that region. On the remaining compact part it is bounded by continuity. Rotations and central characters have absolute value one, and there are only finitely many components. This proves a uniform bound and thus the stated polynomial growth. Finite quotient volume from the preceding lesson then proves square integrability.

Conversely, define \(f(z)=y^{-k/2}\Phi(s(z),1)\). Positive central invariance and the rotation type imply \(\Phi(g_\infty,1)=(f|g_\infty)(i)\) for every positive real matrix: write it as a positive scalar times \(s(z)r(\theta)\). Proposition 3.1 shows that \(f\) is holomorphic. For \(\delta\in\Gamma_0(N)\), rational invariance and finite covariance give

\[
\Phi(\delta_\infty g_\infty,1)
=\Phi(g_\infty,\delta_f^{-1})
=\chi(d_\delta)\Phi(g_\infty,1).
\]

Taking the corresponding real slash proves \(f|\delta=\chi(d_\delta)f\).

We must check regularity and vanishing at every cusp, rather than only at infinity. For \(\sigma\in\mathrm{SL}_2(\mathbb Z)\), the same real-coordinate identity gives

\[
(f|\sigma)(z)=y^{-k/2}\Phi(s(z),\sigma_f^{-1}).
\tag{4.5}
\]

Take \(h=\sigma_f^{-1}\) and \(D\) as in (4.3). The function on the right is holomorphic by the lowering equation, and is \(D\)-periodic by rational invariance. Polynomial growth of \(\Phi\) gives \(|(f|\sigma)(x+iy)|\leq C y^M\) for \(0\leq x\leq D\), \(y\geq1\), after enlarging \(M\): the entries of \(s(z)\) and its inverse grow only as powers of \(y\) on that strip.

A holomorphic periodic function has a Laurent expansion in \(q_D=e^{2\pi iz/D}\). For its coefficient \(a_n\), integration along height \(y\) gives

\[
 a_n=e^{2\pi n y/D}\frac1D\int_0^D(f|\sigma)(x+iy)e^{-2\pi inx/D}\,dx.
\]

When \(n<0\), the bound \(C y^M e^{2\pi n y/D}\) tends to zero, so \(a_n=0\). Equation (4.4) and cuspidality give \(a_0=0\). The Laurent expansion consequently extends holomorphically over \(q_D=0\) and vanishes there. Since \(\sigma\) was arbitrary, \(f\) is a cusp form at every rational cusp. Its finite and real covariance, together with (2.1), now gives \(\Phi=\phi_f\) everywhere. Equation (2.4) proves injectivity. \(\square\)

This proof also shows that imposing the usual global moderate-growth bound, instead of the fixed-finite-component condition in the theorem, gives the same space: the recovered functions are bounded. Formula (3.3) supplies the infinitesimal-character condition in the usual definition of an automorphic form. These observations avoid inserting an extra spectral assumption into the dictionary.

## 5. A Hecke operator with its exact factor

Fix \(p\nmid N\), and give \(K_p=G(\mathbb Z_p)\) volume one. Write

\[
D_p=K_p\begin{pmatrix}p&0\\ 0&1\end{pmatrix}K_p,
\qquad
\mathcal H_p\Phi(g)=\int_{D_p}\Phi(gt)\,dt.
\tag{5.1}
\]

The finite matrix \(t\) is inserted at \(p\), with identity at all other places. This formula specifies the meaning of right convolution in this lesson.

Our classical Hecke convention is

\[
T_pf(z)=\frac1p\sum_{b=0}^{p-1}f\left(\frac{z+b}{p}\right)
+\chi(p)p^{k-1}f(pz).
\tag{5.2}
\]

**Theorem 5.1.** With these conventions,

\[
\phi_{T_pf}=p^{k/2-1}\mathcal H_p\phi_f.
\tag{5.3}
\]

In particular, if \(T_pf=a_pf\), then the eigenvalue of \(\mathcal H_p\) is \(a_pp^{1-k/2}\), and that of \(p^{-1/2}\mathcal H_p\) is \(a_pp^{-(k-1)/2}\).

**Proof.** The right \(K_p\)-cosets of \(D_p\) have representatives

\[
\alpha_b=\begin{pmatrix}p&b\\ 0&1\end{pmatrix}\quad(0\leq b<p),\qquad
\alpha_\infty=\begin{pmatrix}1&0\\ 0&p\end{pmatrix}.
\tag{5.4}
\]

Here a right coset \(\alpha K_p\) is determined by the lattice \(\alpha\mathbb Z_p^2\). An index-\(p\) sublattice corresponds to a line in \(\mathbb F_p^2\); the displayed lattices give the lines spanned by \((b,1)\) and \((1,0)\), once each. This proves the decomposition. Each coset has measure one by left invariance. Since the lift is right \(K_p\)-invariant, the integral is a sum over (5.4).

Evaluate first at a positive real \(g_\infty\), with finite component one. Treat each \(\alpha\) in (5.4) as a rational matrix. Rational left invariance changes the real component to \(\alpha^{-1}g_\infty\). At \(p\) the new finite component is one; at \(\ell\ne p\) it is \(\alpha^{-1}\), an integral invertible upper triangular matrix. For \(\alpha_b\) its lower-right entry is one, so its finite character factor is one. For \(\alpha_\infty\) its lower-right entry is \(p^{-1}\), so its character factor over primes dividing \(N\) is \(\overline\chi(p^{-1})=\chi(p)\).

Multiplication by a positive scalar leaves the slash operation unchanged. Hence we may replace \(\alpha_b^{-1}\) by \(p\alpha_b^{-1}=\begin{pmatrix}1&-b\\ 0&p\end{pmatrix}\), and \(\alpha_\infty^{-1}\) by \(\begin{pmatrix}p&0\\ 0&1\end{pmatrix}\). On the real section, the classical function represented by the convolution is therefore

\[
p^{-k/2}\sum_{b=0}^{p-1}f\left(\frac{z-b}{p}\right)
+\chi(p)p^{k/2}f(pz).
\tag{5.5}
\]

Since \(f(z+1)=f(z)\), changing the residues \(-b\) to \(b\) leaves the sum unchanged. Multiplication by \(p^{k/2-1}\) gives (5.2).

The convolution preserves all the defining conditions of \(A_0(N,k,\omega)\). At infinity it commutes with the differential and rotation operators; at finite places away from \(p\) it commutes with \(K_0(N)\), while at \(p\) its kernel is bi-\(K_p\)-invariant. Central and rational covariance persist. The cusp integral commutes with this finite sum, and each summand has zero constant term. The translates of a bounded lift are bounded. Theorem 4.1 therefore identifies the entire adelic function from the value calculated on the real section, proving (5.3) and also proving that (5.2) preserves cusp forms. The eigenvalue assertions follow by dividing by the factor in (5.3). \(\square\)

The frequently used classical slash normalization is

\[
(f\Vert_k\alpha)(z)=(\det\alpha)^{k-1}(cz+d)^{-k}f(\alpha z).
\]

For determinant \(p\), it is \(p^{k/2-1}(f|_k\alpha)\). Thus (5.2) is the sum of these classical slashes by \(\begin{pmatrix}1&b\\ 0&p\end{pmatrix}\) and the \(\chi(p)\)-weighted slash by \(\begin{pmatrix}p&0\\ 0&1\end{pmatrix}\). This explains the normalization difference directly. With the integral in (5.1), replacing \(gt\) by \(gt^{-1}\) would change the comparison and involve the central character; the specified side is part of (5.3).

On Fourier coefficients (5.2) reads

\[
 a_n(T_pf)=a_{pn}(f)+\chi(p)p^{k-1}a_{n/p}(f),
\tag{5.6}
\]

with \(a_{n/p}=0\) when \(p\nmid n\). This follows because the sum of \(e^{2\pi imb/p}\) over \(b\) is \(p\) if \(p\mid m\), and zero otherwise.

## 6. The Petersson constant

Let
\(X=G(\mathbb Q)Z(\mathbb A)\backslash G(\mathbb A)\).
For central character \(\omega\), use \(L^2(X,\omega)\), meaning functions on \(G(\mathbb Q)\backslash G(\mathbb A)\) transforming by \(\omega\) under the centre. The product \(\phi_f\overline{\phi_g}\) descends to an ordinary function on \(X\), because \(\omega\) is unitary. It is this product that is integrated.

Use the preceding lesson's measures: finite projective maximal compact volume one, hyperbolic density \(dx\,dy/y^2\), and probability measure \(d\theta/\pi\) on projective rotations, \(0\leq\theta<\pi\). The unnormalized Petersson product is

\[
\langle f,g\rangle_{\rm Pet}=
\int_{\Gamma_0(N)\backslash\mathbb H}f(z)\overline{g(z)}y^k\frac{dx\,dy}{y^2}.
\tag{6.1}
\]

**Theorem 6.1.** Put \(I_N=[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]\). Then

\[
I_N=N\prod_{p\mid N}(1+p^{-1}),\qquad
\langle\phi_f,\phi_g\rangle_{L^2(X,\omega)}
=\frac1{I_N}\langle f,g\rangle_{\rm Pet}.
\tag{6.2}
\]

**Proof.** Reduction modulo \(N\) identifies the compact cosets \(G(\widehat{\mathbb Z})/K_0(N)\) with \(\mathbb P^1(\mathbb Z/N\mathbb Z)\), the primitive columns modulo multiplication by a unit. A primitive column over \(\mathbb Z/p^e\mathbb Z\) can be completed to an invertible matrix, so this action is transitive; its stabilizer at the line spanned by \((1,0)\) is exactly the upper triangular group. The number of primitive columns is \(p^{2e}-p^{2e-2}\), and the unit action is free, with \(p^e-p^{e-1}\) elements. There are therefore \(p^{e-1}(p+1)\) lines. Chinese remaindering gives the displayed product.

The reduction of \(\mathrm{SL}_2(\mathbb Z)\) onto \(\mathrm{SL}_2(\mathbb Z/N\mathbb Z)\) was proved in the preceding lesson's Solution 6.3 by elementary matrices and the Chinese remainder theorem. That finite special linear group is also transitive on primitive lines, since a primitive column can be completed to determinant one. Its stabilizer is the reduction of \(\Gamma_0(N)\). Thus the same count gives \(I_N\).

Finite scalar units lie in \(K_0(N)\). Passing to the projective group consequently leaves its index unchanged, and the image of \(K_0(N)\) has Haar volume \(I_N^{-1}\). The positive-real decomposition in the preceding lesson gives the quotient represented by a fundamental region for \(\Gamma_0(N)\backslash\mathbb H\), a projective rotation, and this finite compact fibre. Except at elliptic fixed points, which have measure zero, interior representatives have no extra stabilizer. The element \(-I\) has already been accounted for by projective rotations; it supplies no further factor of two. Formula (2.4) and the finite type imply

\[
\phi_f(s(z)r(\theta)u)\overline{\phi_g(s(z)r(\theta)u)}
=y^k f(z)\overline{g(z)}.
\]

Integrating the rotation fibre gives one, and the finite fibre gives \(I_N^{-1}\). The remaining integral is (6.1), proving (6.2). Absolute convergence follows from the cusp decay established in Theorem 4.1. \(\square\)

As a consistency check, the effective modular index is also \(I_N\), because \(-I\in\Gamma_0(N)\). The hyperbolic area is \(I_N\pi/3\), while the finite fibre has measure \(I_N^{-1}\). Their product is the level-independent volume \(\pi/3\) from the preceding lesson. If Petersson measure is normalized by \(I_N^{-1}\) at each level, the comparison constant is one instead.

## 7. Two lifts and a normalization check

The classical forms used here are \(\Delta\in S_{12}(\mathrm{SL}_2(\mathbb Z))\) and the normalized newform \(f_{11}\in S_2(\Gamma_0(11))\). Their modularity and newform status are classical input. Their product formulas and coefficients can be checked against the primary [LMFDB record for \(\Delta\)](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/1/12/a/a/) and [record for \(f_{11}\)](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/). We use only the displayed initial coefficients, and the following adelic conclusions follow from the proofs above.

For \(q=e^{2\pi iz}\),

\[
\Delta(z)=q\prod_{n\geq1}(1-q^n)^{24}
=q-24q^2+252q^3-1472q^4+\cdots.
\]

Its lift has trivial central and finite characters and

\[
\phi_\Delta(s(z)r(\theta))=e^{12i\theta}y^6\Delta(z).
\]

The factor in (5.3) at \(p=2\) is \(2^5=32\), so the convolution eigenvalue is \(-24/32=-3/4\). The normalized operator \(2^{-1/2}\mathcal H_2\) has eigenvalue \(-24/2^{11/2}\). The Fourier relation is consistent at \(q^2\):
\(-1472+2^{11}=576=(-24)(-24)\).
The lowering equation holds because \(\partial_{\bar z}\Delta=0\). Here \(I_1=1\), so the adelic and unnormalized Petersson norms agree.

For the level-11 form,

\[
f_{11}(z)=q\prod_{n\geq1}(1-q^n)^2(1-q^{11n})^2
=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7+\cdots.
\]

The lift has finite type trivial on \(K_0(11)\), weight two, and
\(\phi_{f_{11}}(s(z)r(\theta))=e^{2i\theta}y f_{11}(z)\).
For every \(p\ne11\), the Hecke comparison factor is \(p^{2/2-1}=1\). Thus \(\mathcal H_2\) has eigenvalue \(-2\), and \(\mathcal H_3\) has eigenvalue \(-1\). For example the coefficient at \(q^2\) in \(T_2f_{11}\) is \(2+2=4\), agreeing with \((-2)(-2)\). Finally \(I_{11}=12\), giving
\(\|\phi_{f_{11}}\|^2=\|f_{11}\|_{\rm Pet}^2/12\).

The product coefficients above can be computed with finite products: to determine coefficients through \(q^m\), discard all factors whose nonconstant terms start beyond \(q^{m-1}\). No numerical approximation to the infinite product is needed for these checks.

## 8. Exercises with complete solutions

**Exercise 8.1 — character cancellation.** Repeat the decomposition check using \(g=\gamma g_\infty u=\gamma' g'_\infty u'\). Then take a character modulo 5 with \(\chi(2)=i\) and the matrix \(\delta=\begin{pmatrix}2&1\\ 5&3\end{pmatrix}\). Compute the two character factors. Explain why odd weight is required for this character, and what fails if (1.2) is replaced by \(\chi(d_u)\).

**Solution 8.1.** The comparison matrix \(\delta=\gamma'^{-1}\gamma\) has integral invertible finite components and positive real determinant, so it belongs to \(\Gamma_0(N)\). The real value is multiplied by \(\chi(d_\delta)\), and the finite value by \(\overline\chi(d_\delta)\); their product is one. In the numerical example \(\det\delta=6-5=1\), \(3=2^3\pmod5\), and \(\chi(3)=-i\). The finite factor is \(i\), cancelling the real factor \(-i\). Also \(\chi(-1)=\chi(2)^2=-1\); compatibility with \(-I\) forces odd \(k\). Using \(\chi(d_u)\) would instead multiply this value by \((-i)^2=-1\). Unless the form value is zero, decomposition independence fails. This exercise assumes a cusp form with the stated transformation law when making the last test; it makes no existence claim for a particular odd weight.

**Exercise 8.2 — recover holomorphy.** For a smooth function \(F\) on \(\mathbb H\), let \(\Phi(s(z)r(\theta))=e^{ik\theta}F(z)\). Prove that \(L\Phi=0\) is equivalent to holomorphy of \(y^{-k/2}F\). As a diagnostic, apply \(L\) when \(F=y^{k/2}\bar z\).

**Solution 8.2.** Formula (3.2) gives \(-2iy\partial_{\bar z}F-kF/2=0\). Write \(F=y^{k/2}h\), differentiate the factor, and cancel its contribution as in Proposition 3.1. The equation becomes \(-2iy^{k/2+1}\partial_{\bar z}h=0\). Since \(y>0\), it is equivalent to \(\partial_{\bar z}h=0\), which is the Cauchy–Riemann equation for the smooth \(h\). For \(h=\bar z\), the derivative is one, giving \(L\Phi=-2i e^{i(k-2)\theta}y^{k/2+1}\), everywhere nonzero. Rotation type by itself consequently does not enforce holomorphy.

**Exercise 8.3 — derive rather than guess the Hecke factor.** For \(p\nmid N\), derive (5.5) from the \(p+1\) cosets in (5.4), retaining their finite character factors. For weight four and \(p=3\), compute the coefficient at \(q^n\) of the classical function represented by \(\mathcal H_3\phi_f\).

**Solution 8.3.** Rational left multiplication by \(\alpha_b^{-1}\) makes its finite component at \(p\) one and all other finite components \(\alpha_b^{-1}\). Their lower-right entries are one, so the character factor is one. The real slash by \(p\alpha_b^{-1}\) gives \(p^{-k/2}f((z-b)/p)\). For \(\alpha_\infty\), the other finite lower-right entries are \(p^{-1}\); their factor is \(\chi(p)\), and its real slash gives \(p^{k/2}f(pz)\). Summing yields (5.5). To make the coefficient of the averaged first term \(p^{-1}\), multiply by \(p^{k/2-1}\); the second becomes \(\chi(p)p^{k-1}\) with the same multiplier. In the requested case, (5.5) is
\(3^{-2}\sum_{b=0}^2 f((z-b)/3)+9\chi(3)f(3z)\).
The coefficient is
\(\frac13 a_{3n}+9\chi(3)a_{n/3}\).
Multiplication by the comparison factor 3 gives \(a_{3n}+27\chi(3)a_{n/3}\), as in the classical weight-four operator.

**Exercise 8.4 — the quotient-measure constant.** Compute the comparison constant at level 18 for the preceding lesson's Haar measures and the unnormalized Petersson product. Check the total quotient volume, and explain why the count does not gain a factor of two from \(-I\).

**Solution 8.4.** The local projective-line counts are \(\#\mathbb P^1(\mathbb Z/2\mathbb Z)=3\) and \(\#\mathbb P^1(\mathbb Z/9\mathbb Z)=3(3+1)=12\). Their product is \(I_{18}=36\), also obtained from \(18(1+1/2)(1+1/3)\). The image of the finite level group has volume \(1/36\), and projective rotations have volume one. Thus \(c_{18}=1/36\). The modular area is \(36\pi/3=12\pi\), so integrating the constant function one on the entire central quotient gives \((12\pi)/36=\pi/3\). Since \(-I\) belongs to the congruence group and becomes a scalar in the central quotient, it has already disappeared in the projective description. Dividing the rotation fibre by it a second time would incorrectly halve both constants.

All five comparison results have been proved: decomposition independence, the character and differential properties, the full-cusp bijection, Hecke compatibility and the measure constant. The later representation-theoretic lessons will study the modules generated by these vectors; no irreducibility assertion about such a module is needed here.

## References

- P. Deligne, [*Formes modulaires et représentations de GL(2)*](https://publications.ias.edu/sites/default/files/Number21.pdf), in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349 (1973), pp. 55–105, §§1.2–1.3 and 2.1. Deligne uses a lattice formulation and right rational quotient; the present formulas use left rational invariance.
- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §§6.2–6.3 and 6.7–6.8. See the [author's graduate-text page](https://sites.duke.edu/jgetz/graduate-text/). The rotation orientation and finite character convention must be compared with those fixed here.
- The LMFDB Collaboration, classical modular-form records [1.12.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/1/12/a/a/) and [11.2.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/), consulted 1 October 2026, for the classical input in Section 7.
