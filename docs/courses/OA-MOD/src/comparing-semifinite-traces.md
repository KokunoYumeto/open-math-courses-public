# Comparing semifinite traces

Two normal semifinite traces need not be scalar multiples on an algebra with center. Their relative size is recorded by a central operator. Using their sum as reference turns that possibly unbounded operator into a pair of bounded complementary densities.

Throughout, \(M\) is a von Neumann algebra, \(\tau\) is a faithful normal semifinite trace, and \(\rho\) is a normal semifinite trace which may be nonfaithful or zero. No separability or sigma-finiteness is assumed. We allow the zero algebra. All weight values lie in \([0,\infty]\), with \(0\cdot\infty=0\). The trace axioms and finite ideals apply with these conventions.

## The density of a trace is central

The earlier Radon–Nikodym theorem relative to a semifinite trace assigns to every normal semifinite weight \(\psi\) a unique densely defined positive self-adjoint operator \(h\) affiliated with \(M\), such that
\[
 \begin{gathered}
 h_\varepsilon=h(1+\varepsilon h)^{-1},\\
 \psi(x)\\
 =\sup_{\varepsilon>0}
 \tau(h_\varepsilon^{1/2}xh_\varepsilon^{1/2}).
 \end{gathered}
\]
The supremum is the increasing limit as \(\varepsilon\downarrow0\), and \(x\in M_+\). Its support is \(s(h)=s(\psi)\). Neither integrability nor trace measurability of \(h\) is asserted.

**Lemma.** The weight \(\psi\) is a trace if and only if every spectral projection of \(h\) is central in \(M\).

**Proof of centrality.** Let \(u\in M\) be unitary. The spectral transport theorem in The spectral calculus kernel gives
\[
 (uhu^*)_\varepsilon=uh_\varepsilon u^*.
\]
Conjugating the bounded positive sandwich by \(u^*\), and using unitary invariance of \(\tau\), shows for every \(x\geq0\) that
\[
 \begin{gathered}
 \tau_{uhu^*}(x)\\
 =\tau_h(u^*xu).
 \end{gathered}
 \tag{TR.1}
\]
This equality follows at every bounded regularization before taking its supremum, so it holds at infinite values as well. If \(\psi=\tau_h\) is a trace, its unitary invariance makes the right side equal to \(\psi(x)\). Uniqueness in PT-08 gives \(uhu^*=h\), including equality of the operator domains.

Unitary transport of spectral projections now gives \(u1_B(h)u^*=1_B(h)\) for every Borel set \(B\). Thus every spectral projection commutes with every unitary of \(M\), and hence with all of \(M\), by The unitary commutation test. The projections are central.

**Proof of the converse.** If all spectral projections are central, each bounded \(h_\varepsilon\) is central. For \(v\in M\), apply the trace identity to \(v h_\varepsilon^{1/2}\). Since \(h_\varepsilon\) commutes with \(v\), this gives
\[
 \begin{gathered}
 \tau(h_\varepsilon^{1/2}v^*v h_\varepsilon^{1/2})\\
 =\tau(h_\varepsilon^{1/2}vv^* h_\varepsilon^{1/2}).
 \end{gathered}
\]
Taking suprema in \(\varepsilon\) proves \(\psi(v^*v)=\psi(vv^*)\), the trace identity. \(\square\)

Apply this lemma to \(\rho\), and keep its central affiliated density \(h\) for the rest of the lesson. Put
\[
 \begin{gathered}
 z_n=1_{[0,n]}(h),\\
 h_n=hz_n\quad(n\geq1).
 \end{gathered}
\]
The central projections \(z_n\) increase strongly to \(1\), and \(h_n\in Z(M)_+\) is bounded by \(nz_n\). Strong convergence to \(1\) uses the dense self-adjoint domain of \(h\); there is no spectral projection at an infinite eigenvalue.

For every \(y\geq0\) supported on \(z_n\), normality of \(\tau\) gives the exact cutoff identity
\[
 \rho(y)=\tau(h_ny).
 \tag{TR.2}
\]
Indeed \(h_\varepsilon y\) is positive and increases strongly to the bounded positive \(h_ny\). Centrality identifies it with the sandwich defining \(\rho(y)\). Thus (TR.2) concerns bounded positive products and remains valid even when its value is infinite.

## The sum is still semifinite

**Theorem.** The pointwise sum
\[
 \sigma(x)=\tau(x)+\rho(x)
 \qquad(x\in M_+)
\]
is a faithful normal semifinite trace.

**Proof.** Additivity, homogeneity and the trace identity pass to the sum. Faithfulness follows from \(\sigma\geq\tau\). For a bounded increasing positive net \(x_\alpha\uparrow x\), normality of each summand gives
\[
 \begin{gathered}
 \sup_\alpha\bigl(\tau(x_\alpha)+\rho(x_\alpha)\bigr)\\
 =\sup_\alpha\tau(x_\alpha)+\sup_\alpha\rho(x_\alpha).
 \end{gathered}
\]
To check the equality, choose indices making each of the two nonnegative terms as large as prescribed, and then an index above both. This also handles an infinite supremum. Thus \(\sigma\) is normal.

It remains to prove semifiniteness. Let \(0\ne x\in M_+\). Since \(z_n\uparrow1\) centrally, some \(z_nx\) is nonzero. By the order criterion for semifiniteness of a trace, there exists
\[
 0\ne b\leq z_nx,\qquad \tau(b)<\infty.
\]
Positivity and \(z_nx\leq\|x\|z_n\) imply \(b=z_nbz_n\): the inequality makes \(b^{1/2}(1-z_n)=0\). Because \(h_n\) is central and \(h_n\leq nz_n\), (TR.2) gives
\[
 \begin{gathered}
 \rho(b)=\tau(h_nb)\\
 \leq n\tau(b),\\
 \sigma(b)\\
 \leq(n+1)\tau(b)<\infty.
 \end{gathered}
 \tag{TR.3}
\]
Moreover \(b\leq z_nx\leq x\). Every nonzero positive element therefore dominates a nonzero element of finite \(\sigma\)-trace. TB-02 proves semifiniteness. \(\square\)

The countable family \(z_n\) bounds a single density. It is not a countable family of finite-trace projections exhausting the algebra: \(\tau(z_n)\) can be infinite for every \(n\).

## Bounded complementary densities and their supports

**Theorem.** There is a unique \(a\in Z(M)\), \(0\leq a\leq1\), such that, for all \(x\in M_+\),
\[
 \begin{gathered}
 \tau(x)=\sigma(ax),\\
 \rho(x)\\
 =\sigma((1-a)x).
 \end{gathered}
 \tag{TR.4}
\]
It is given by
\[
 a=(1+h)^{-1},
 \tag{TR.5}
\]
and its exact support identities are
\[
 \begin{gathered}
 s(a)=1,\\
 s(1-a)=s(h)\\
 =s(\rho).
 \end{gathered}
 \tag{TR.6}
\]

**Construction and support.** Bounded spectral calculus defines (TR.5) as a positive contraction. Its centrality follows from the central spectral projections of \(h\). On each \(z_n\), the scalar inequality \((1+t)^{-1}\geq(n+1)^{-1}\) gives
\[
 z_n\leq(n+1)a.
\]
If \(a\xi=0\), this inequality forces \(z_n\xi=0\) for every \(n\). Since \(z_n\uparrow1\), \(\xi=0\), proving \(s(a)=1\). Also \(1-a\) is the bounded spectral function \(t/(1+t)\) of \(h\), whose zero set is exactly \(\{0\}\). Hence \(s(1-a)=s(h)\), and PT-08 identifies the last support with \(s(\rho)\).

**Both identities at all positive elements.** Fix \(x\geq0\) and put \(x_n=z_nx\). Centrality makes \(0\leq x_n\uparrow x\). Formula (TR.2), additivity of the trace on positive elements, and bounded calculus on \(z_n\) give
\[
 \begin{gathered}
 \sigma(ax_n)\\
 =\tau(ax_n)+\tau(h_nax_n)\\
 =\tau((1+h_n)ax_n)=\tau(x_n).
 \end{gathered}
\]
Here \((1+h_n)az_n=z_n\), so the final identity is an identity of bounded positive operators. Similarly,
\[
 \begin{gathered}
 \sigma((1-a)x_n)\\
 =\tau((1-a)x_n)\\
 {}+\tau(h_n(1-a)x_n)\\
 =\tau(h_nx_n)=\rho(x_n),
 \end{gathered}
\]
because \((1+h_n)(1-a)z_n=h_n\). All sums are sums of nonnegative extended values. Taking increasing suprema and using normality of \(\sigma,\tau,\rho\) proves both equalities in (TR.4). In particular, the second has been proved independently, without subtracting \(\tau(x)\) from a possibly infinite \(\sigma(x)\).

**Uniqueness.** Suppose \(b\in Z(M)\), \(0\leq b\leq1\), also represents \(\tau\) through \(\sigma(bx)=\tau(x)\). If \(a-b\) has a nonzero positive spectral part, choose \(\eta>0\) such that
\[
 e=1_{[\eta,\infty)}(a-b)\ne0.
\]
This is a central projection. Since \(\sigma\) is faithful normal semifinite, Finite pieces in a prescribed projection gives a nonzero projection \(r\leq e\) with \(\sigma(r)<\infty\). Faithfulness implies \(\sigma(r)>0\). Both \(ar\) and \(br\) lie in the bounded finite trace ideal, and their \(\sigma\)-values are equal. In this finite ideal subtraction is legitimate, giving
\[
 \begin{gathered}
 0=\sigma((a-b)r)\\
 \geq\eta\sigma(r)>0,
 \end{gathered}
\]
a contradiction. Interchanging \(a\) and \(b\) excludes a negative spectral part. Thus \(a=b\). \(\square\)

If \(\rho=0\), then \(h=0\), \(a=1\) and \(\sigma=\tau\). The assertions also hold in the zero algebra, whose identity and only operator are zero. The identity \(s(a)=1\) is injectivity, not a claim that \(a\) has a bounded inverse.

## Proportionality on a factor

**Corollary.** If \(M\ne0\) is a factor with the fixed faithful normal semifinite trace \(\tau\), every normal semifinite trace \(\rho\) has the form
\[
 \begin{gathered}
 \rho=c\tau,\\
 0\leq c<\infty,
 \end{gathered}
 \tag{TR.7}
\]
for a unique scalar \(c\). It is faithful exactly when \(c>0\).

**Proof.** The center is \(\mathbb C1\), so \(a=\lambda1\). Positivity and contractivity give \(0\leq\lambda\leq1\), while \(s(a)=1\) and \(M\ne0\) exclude \(\lambda=0\). Formula (TR.4) becomes
\[
 \tau=\lambda\sigma,\qquad
 \rho=(1-\lambda)\sigma.
\]
Since \(\lambda>0\), multiplication by \(\lambda\) is invertible on \([0,\infty]\). Therefore (TR.7) holds with
\[
 c=\frac{1-\lambda}{\lambda}.
\]
When \(\lambda=1\), the second identity gives \(\rho=0\) directly, using \(0\cdot\infty=0\). Otherwise \(c>0\), and faithfulness follows from that of \(\tau\).

There is a nonzero projection \(r\) of finite \(\tau\)-trace by TI-01. Its trace is strictly positive, so \(\rho(r)=c\tau(r)\) determines \(c\) uniquely. This also proves that an infinite coefficient is impossible for a semifinite \(\rho\). \(\square\)

Any nonzero normal trace on a factor is faithful: its support is a nonzero central projection by The normal trace support theorem, hence is \(1\). Consequently any two nonzero normal semifinite traces on a factor are positive scalar multiples of each other, by using one as the reference trace. The zero trace is the zero multiple of each trace. These statements include the zero-trace case without asserting that a nonzero trace is a scalar multiple of the zero trace.

## Central variation, infinite values and nontracial weights

**An unbounded central density with a kernel.** Let \(M=\ell^\infty(\mathbb N)\) act diagonally on \(\ell^2(\mathbb N)\). For \(x\geq0\), define
\[
 \begin{gathered}
 \tau(x)=\sum_{n\geq1}x_n,\\
 \rho(x)=\sum_{n\geq1}d_nx_n,\\
 d_n=\begin{cases}n,&n\text{ even},\\0,&n\text{ odd}.\end{cases}
 \end{gathered}
\]
These are normal traces: finite coordinate sums commute with increasing suprema, and taking the supremum over finite sets gives the full sums. Finite coordinate truncations of a bounded positive element have finite values and increase to that element, proving semifiniteness. The first trace is faithful; the second has support equal to the projection onto the even coordinates.

The diagonal density \(h\) has entries \(d_n\) and maximal domain
\[
 D(h)=\{\xi:\sum_n d_n^2|\xi_n|^2<\infty\}.
\]
Finite-coordinate vectors prove density of the domain. Coordinate convergence proves closedness, and the real diagonal spectral resolution makes the operator positive self-adjoint and affiliated with this abelian algebra, by the spectral domain construction. Evaluating the bounded regularizations coordinatewise and taking increasing suprema gives \(\rho=\tau_h\).

The theorem gives the explicit coefficients
\[
 \begin{gathered}
 \sigma(x)\\
 =\sum_n(1+d_n)x_n,\\
 a_n=\frac1{1+d_n},\\
 (1-a)_n=\frac{d_n}{1+d_n}.
 \end{gathered}
 \tag{TR.8}
\]
Every \(a_n\) is positive, so \(s(a)=1\), but the even entries tend to zero. Thus \(a\) has no bounded inverse. The support of \(1-a\) is exactly the even-coordinate projection, agreeing with \(s(\rho)\). Neither trace has to have finite total mass for the two identities in (TR.4) to hold.

For every \(R>0\), the projection \(1_{(R,\infty)}(h)\) contains infinitely many even coordinates and has infinite \(\tau\)-trace. By The spectral-tail criterion, \(h\) is not \(\tau\)-measurable. Thus restricting trace comparison to measurable densities would omit this example, even though its normalized density \(a\) is bounded and central.

**A density which is not central gives a nontracial weight.** On \(M_2(\mathbb C)\), let \(\tau=\operatorname{Tr}\), \(h=\operatorname{diag}(1,2)\), and \(\psi(x)=\operatorname{Tr}(hx)\). This is a faithful finite normal positive functional: it is a positive weighted sum of the two coordinate vector functionals. For \(v=E_{12}\),
\[
 \begin{gathered}
 \psi(v^*v)=\psi(E_{22})=2,\\
 \psi(vv^*)=\psi(E_{11})=1.
 \end{gathered}
\]
Thus \(\psi\) is not a trace. This computes explicitly the obstruction detected by TR-01; a general weight density need not be central.

The comparison and factor statements are Theorem V.2.31 and Corollary V.2.32 of M. Takesaki, *Theory of Operator Algebras I*, printed pp. 328–329. The argument here uses the earlier weight-density theorem and central spectral cutoffs to keep both support projections and all infinite values explicit.
