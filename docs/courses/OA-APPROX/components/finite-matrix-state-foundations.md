# Finite matrix state foundations

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original text: public domain (CC0).*

A recording channel is tested by a linear functional on matrices. Its density can be recovered from the matrix entries of that functional. A list of vectors used to prepare the state is additional information: several different lists can give the same functional. We begin with the recovery calculation, then distinguish those preparation lists.

Throughout, \(m\ge1\), \(M_m=M_m(\mathbb C)\), \(e_{ij}\) are the matrix units, and \(\tau_m=\operatorname{Tr}/m\). Inner products are linear in their second variable. A **state** is a complex linear functional \(\varphi\) with \(\varphi(a)\ge0\) for positive \(a\) and \(\varphi(1)=1\). A state is **pure** if an equality \(\varphi=t\psi+(1-t)\chi\), with states \(\psi,\chi\) and \(0<t<1\), forces \(\psi=\chi=\varphi\). The finite selfadjoint spectral theorem, positive square roots and trace-dual test are proved in [Tracial adjoints and rational matrix models, P03](../src/tracial-adjoints-and-rational-matrix-models.md#p03). We also use finite-dimensional linear algebra.

<a id="density-recovery"></a>
## Recovering the density from the functional

Define a matrix from the measured entries by
\[
h_{ij}=m\varphi(e_{ji}).
\tag{D1}
\]
For any matrix \(a=\sum_{i,j}a_{ij}e_{ij}\), multiplication of matrix units gives
\[
\tau_m(ha)
=\frac1m\sum_{i,j}h_{ji}a_{ij}
=\varphi(a).
\tag{D2}
\]
This also proves uniqueness: any matrix representing the same functional must have every entry specified by (D1). For a vector \(v\in\mathbb C^m\),
\[
v^*hv=m\varphi(vv^*)\ge0.
\]
The quadratic form is real and nonnegative. Polarization makes \(h=h^*\); the displayed inequality then says \(h\ge0\). Finally \(\tau_m(h)=\varphi(1)=1\).

Conversely, if \(h\ge0\) and \(\tau_m(h)=1\), formula (D2) defines a state. For \(a\ge0\), cyclicity of the finite trace gives
\[
\tau_m(ha)=\tau_m(h^{1/2}ah^{1/2})\ge0,
\]
and the value at the identity is one. Consequently the positive matrices with normalized trace one and the states of \(M_m\) correspond bijectively. Formula (D1) also shows that convex combinations of states correspond to the same convex combinations of densities.

The state is faithful on positive elements exactly when \(h\) is invertible. If \(hv=0\) for a nonzero vector, then \(\varphi(vv^*)=0\) although \(vv^*\) is nonzero and positive. In the other direction an invertible positive matrix has a smallest eigenvalue \(\delta>0\). Thus, for \(a\ge0\),
\[
\varphi(a)=\tau_m(ha)\ge\delta\tau_m(a).
\]
If this is zero, every nonnegative eigenvalue of \(a\) sums to zero, so \(a=0\). The same finite spectral calculation defines \(h^{1/2}\), \(h^{1/4}\) and, in the invertible case, \(h^{-1/2}\), by the corresponding functions of its positive eigenvalues.

<a id="saturated-test"></a>
## A saturated projection test determines a vector state

For a unit vector \(u\), put \(P_u=uu^*\). The functional
\(\omega_u(a)=u^*au\) is a state. Suppose a state \(\psi\) satisfies \(\psi(P_u)=1\). Then \(\psi(1-P_u)=0\).

Here is the positive-form estimate needed to interpret that zero. If \(D=h/m\) is the ordinary trace-one density of \(\psi\), the matrices \(aD^{1/2}\) and \(bD^{1/2}\) have Hilbert–Schmidt inner product \(\operatorname{Tr}(Da^*b)=\psi(a^*b)\). Finite-dimensional Cauchy–Schwarz therefore gives, including when one vector is zero,
\[
|\psi(a^*b)|^2
\le\psi(a^*a)\psi(b^*b).
\tag{D3}
\]
Take \(a=1-P_u\), \(b=x\), and then take \(a=x^*\), \(b=1-P_u\). Since \(1-P_u\) is a projection, both bounds are zero. Hence
\[
\psi((1-P_u)x)=0,\qquad \psi(x(1-P_u))=0.
\]
Expanding the two complementary projections now gives
\[
\psi(x)=\psi(P_uxP_u)
=\psi((u^*xu)P_u)=u^*xu.
\tag{D4}
\]
Thus a state giving probability one to this rank-one projection is exactly the associated vector state.

In a convex equality \(\omega_u=t\psi+(1-t)\chi\), evaluate at \(P_u\). Positivity and unitality bound both \(\psi(P_u)\) and \(\chi(P_u)\) by one. Their strictly weighted average is one, so both are one. Formula (D4) gives \(\psi=\chi=\omega_u\). Every vector state is therefore pure.

<a id="preparation-columns"></a>
## Preparation lists come from columns of a square root

Use the ordinary trace-one matrix \(D=h/m\). Let \(b_j=D^{1/2}e_j\) be its columns. Matrix multiplication and the finite trace give
\[
D=\sum_{j=1}^m b_jb_j^*,\qquad
\sum_{j=1}^m\|b_j\|^2=\operatorname{Tr}(D)=1.
\tag{D5}
\]
For each nonzero column put \(w_j=\|b_j\|^2>0\) and \(u_j=b_j/\|b_j\|\). Then
\[
\varphi(a)=\sum_{b_j\ne0}w_j\,\omega_{u_j}(a).
\tag{D6}
\]
Thus columns of a square root give a mixture of at most \(m\) pure states, without a prior choice of eigenbasis.

If \(D\) has rank at least two, choose any nonzero column \(b_j\). Its weight lies strictly between zero and one: weight one would make all other columns zero and hence make \(D\) rank one. The matrix
\[
D'=\frac{D-w_jP_{u_j}}{1-w_j}
\]
is positive with trace one, by (D5). It differs from \(P_{u_j}\), since equality would again make \(D\) rank one. Equation (D6) is therefore a nontrivial convex decomposition of the state into two different states. Such a state is not pure. A positive rank-one matrix of ordinary trace one is \(P_u\) for a unit vector \(u\); its state was proved pure by the saturated test. Pure states are consequently exactly those whose density has rank one.

An orthogonal preparation list has an additional restriction. If
\[
D=\sum_{j=1}^r\lambda_jP_{u_j},
\qquad \lambda_j>0,\quad\sum_j\lambda_j=1,
\]
with orthonormal \(u_j\), multiplying by \(u_j\) gives \(Du_j=\lambda_j u_j\). All the vectors are eigenvectors. Conversely the finite spectral theorem gives just such a list, with \(r=\operatorname{rank}(D)\), by omitting the zero eigenvalues. Among orthogonal lists its weights and rank-one projections are unique up to order exactly when the positive eigenvalues are distinct: simple eigenspaces fix the projections, whereas a two-dimensional repeated eigenspace can be rotated to change them without changing \(D\).

<a id="phase-preparations"></a>
## Three phase preparations give the same density

Consider an ordinary density in \(M_3\):
\[
D=\operatorname{diag}\left(\frac12,\frac13,\frac16\right),
\qquad h=3D=\operatorname{diag}\left(\frac32,1,\frac12\right).
\]
Its spectral preparation uses \(e_1,e_2,e_3\) with probabilities \(1/2,1/3,1/6\). Set
\[
\zeta=-\frac12+\frac{\sqrt3}{2}i,\qquad
v_k=\begin{pmatrix}
1/\sqrt2\\ \zeta^k/\sqrt3\\ \zeta^{2k}/\sqrt6
\end{pmatrix}\quad(k=0,1,2).
\]
Each vector has norm one, and \(\zeta^3=1\), \(1+\zeta+\zeta^2=0\). These scalar identities cancel every off-diagonal entry in the average:
\[
\frac13\sum_{k=0}^2v_kv_k^*=D.
\tag{D7}
\]
The diagonal entries already have the required values. For distinct \(k,l\), with \(d=l-k\) read modulo three,
\[
\langle v_k,v_l\rangle
=\frac12+\frac13\zeta^d+\frac16\zeta^{2d}
=\frac14\ \mathbin{\pm}\ \frac{\sqrt3}{12}i.
\]
Its squared absolute value is \(1/12\), so these preparation vectors are not orthogonal. Nevertheless (D7) implies, for every observable \(a\),
\[
\frac13\sum_{k=0}^2\omega_{v_k}(a)
=\tau_3(ha)
=\frac12a_{11}+\frac13a_{22}+\frac16a_{33}.
\]
The density and the functional are the same for the two preparation lists. The density's simple spectrum makes only its orthogonal list unique. A recording map acts on the density-defined state, so choosing a different list in (D7) cannot change its state-preservation identity.

Return to [Tracial adjoints and rational matrix models](../src/tracial-adjoints-and-rational-matrix-models.md#0-a-measurement-that-preserves-the-state-but-loses-coherence).
