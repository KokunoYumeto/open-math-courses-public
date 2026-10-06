# A real coercive equation in the bounded modular construction

**Original exposition and proof: OpenAI Codex (GPT-6 Astra, Ultra), October 2026. CC0-1.0.**

A complex scalar can turn the real part of a Hilbert inner product into a nonsymmetric bilinear form. Positivity on the diagonal then gives coercivity, but does not make the form an inner product. The existence step in Rieffel and Van Daele's [Lemma 5.6, printed page 211](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf#page=26) can be justified by the following bounded-operator argument.

Positivity, Cauchy–Schwarz and the parallelogram identity are proved in the earlier Hilbert-space foundations, Section 1. Positive matrix square roots used in the example are supplied by the bounded continuous-calculus proofs identified in BK01.

Throughout, the complex inner product is linear in its first variable. Write
\[
(x,y)_{\mathbb R}=\operatorname{Re}\langle x,y\rangle.
\]
A closed real subspace is complete for this real inner product. No complex-linearity, finite dimension, or countability assumption is imposed on it.

## The real Hilbert tools used below

Let \(E\) be a closed real subspace of a Hilbert space regarded as real. Every \(x\) has a unique closest point \(P_E x\) in \(E\). Indeed, if \(d=\inf_{e\in E}\|x-e\|\) and \(e_n\) is a minimizing sequence, the parallelogram identity gives
\[
\|e_n-e_m\|^2
\leq 2\|x-e_n\|^2+2\|x-e_m\|^2-4d^2\longrightarrow0.
\]
Completeness and closedness give a minimizing limit. Varying that limit by \(t e\), for real \(t\) and \(e\in E\), shows that the residual is real-orthogonal to \(E\). This orthogonality proves uniqueness, real-linearity of \(P_E\), and \(\|P_E x\|\leq\|x\|\).

Every bounded real-linear functional \(\ell\) on a real Hilbert space has a unique vector \(v\) such that \(\ell(z)=(v,z)_{\mathbb R}\), with \(\|v\|=\|\ell\|\). To see this without an additional representation theorem, suppose \(\ell\ne0\), put \(N=\ker\ell\), and choose \(x_0\notin N\). The preceding projection construction gives \(u=x_0-P_Nx_0\ne0\), with \(u\perp_{\mathbb R}N\) and \(\ell(u)=\ell(x_0)\ne0\). Since
\[
z-\frac{\ell(z)}{\ell(u)}u\in N,
\]
one may take \(v=\ell(u)u/\|u\|^2\). The case \(\ell=0\) uses \(v=0\). The norm equality follows from Cauchy–Schwarz and testing at \(v/\|v\|\) when \(v\ne0\). Uniqueness follows by testing the difference of two representing vectors against itself.

## Solving the nonsymmetric equation

**Theorem.** Let \(E\) be a closed real subspace of a complex Hilbert space. Let \(\lambda=a+ib\), where \(a>0\), and let \(\ell:E\to\mathbb R\) be bounded and real-linear. There is exactly one \(\eta\in E\) satisfying
\[
\operatorname{Re}\bigl(\lambda\langle\eta,\zeta\rangle\bigr)
=\ell(\zeta)\qquad(\zeta\in E).
\tag{RC.1}
\]
It obeys
\[
\|\eta\|\leq\frac{\|\ell\|}{a}.
\tag{RC.2}
\]

**Proof.** The compression of multiplication by \(i\) is the bounded real-linear operator
\[
C:E\longrightarrow E,\qquad Cx=P_E(ix).
\]
It satisfies \(\|C\|\leq1\) and
\[
(Cx,y)_{\mathbb R}=-(x,Cy)_{\mathbb R}.
\tag{RC.3}
\]
The last identity follows from \(\operatorname{Re}\langle ix,y\rangle=-\operatorname{Re}\langle x,iy\rangle\), followed by real orthogonal projection. Put
\[
A=aI+bC,\qquad A^*=aI-bC.
\]
Here the star denotes the adjoint for the real inner product; its displayed formula follows directly from (RC.3). For every \(x\in E\),
\[
(Ax,x)_{\mathbb R}=(A^*x,x)_{\mathbb R}=a\|x\|^2.
\]
Cauchy–Schwarz therefore gives
\[
\|Ax\|\geq a\|x\|,\qquad
\|A^*x\|\geq a\|x\|.
\tag{RC.4}
\]
The first inequality makes \(A\) injective and its range closed: convergence of \(Ax_n\) forces \(x_n\) to be Cauchy, and continuity identifies the limit. If \(y\) is orthogonal to its range, then \((x,A^*y)_{\mathbb R}=0\) for every \(x\), hence \(A^*y=0\) and \(y=0\). A proper closed range would have a nonzero orthogonal residual by the projection construction above. Thus the range is all of \(E\), and \(\|A^{-1}\|\leq a^{-1}\).

Represent \(\ell\) in the original real inner product by \(v\). Set \(\eta=A^{-1}v\). For \(\eta,\zeta\in E\),
\[
(A\eta,\zeta)_{\mathbb R}
=\operatorname{Re}\bigl((a+ib)\langle\eta,\zeta\rangle\bigr).
\]
This proves (RC.1), uniqueness, and (RC.2). The proof also covers \(E=\{0\}\). \(\square\)

The constant \(a^{-1}\) is sharp: take \(H=\mathbb C\), \(E=\mathbb R\), and \(\ell(t)=t\). Then \(C=0\) and the solution is \(\eta=a^{-1}\), for every \(b\).

## The equation needed in the modular proof

Let \(K\) be a closed real subspace of \(H\) and set
\[
E=(iK)^{\perp_{\mathbb R}}.
\]
For \(\xi\in K\) and \(\zeta\in E\), the number \(\langle\xi,\zeta\rangle\) is real: its imaginary part is the negative of \(\operatorname{Re}\langle i\xi,\zeta\rangle\). Thus
\[
\ell_\xi(\zeta)=\langle\xi,\zeta\rangle
\]
is a bounded real-linear functional on \(E\), of norm at most \(\|\xi\|\). Applying the theorem yields a unique \(\eta\in E\) with
\[
\langle\xi,\zeta\rangle
=\operatorname{Re}\bigl(\lambda\langle\eta,\zeta\rangle\bigr)
\quad(\zeta\in E),\qquad
\|\eta\|\leq\frac{\|\xi\|}{\operatorname{Re}\lambda}.
\tag{RC.5}
\]
When \(\operatorname{Re}\lambda=1\), this is exactly the existence-and-uniqueness assertion needed at the start of Lemma 5.6. The representing real vector is \(v=P_E\xi\); no new inner product is introduced. The standard-real-subspace assumptions \(K\cap iK=\{0\}\) and \(\overline{K+iK}=H\), needed elsewhere in modular theory, are unnecessary for this equation itself.

The remaining assertion of Lemma 5.6 concerns bounded multiplication when \(\xi\) also belongs to the left Hilbert algebra. Its graph-projection and spectral-cutoff argument is on. That assertion is separate from the real equation proved here. The replacement supplies the same vector identity with the same hypotheses, so it can be used at the start of that argument. No whole modular theorem follows from (RC.5) alone.

## A matrix example showing why symmetry matters

The nonsymmetry can occur for a real subspace arising from an actual left Hilbert algebra. Let
\[
H=M_2(\mathbb C),\quad
\langle x,y\rangle=\operatorname{Tr}(xy^*),\quad
d=\begin{pmatrix}1&0\\0&2\end{pmatrix}.
\]
Identify the algebra \(M_2(\mathbb C)\) with \(H\) through \(j(a)=ad^{1/2}\). Transport its multiplication and involution along \(j\). Left multiplication by \(j(a)\) is ordinary matrix multiplication by \(a\), its adjoint is multiplication by \(a^*\), and products span \(H\). The involution is bounded in this finite-dimensional space, so this is a left Hilbert algebra.

The real span of its algebra-positive vectors and the corresponding real orthogonal space are
\[
K=\{ad^{1/2}:a=a^*\},\qquad
E=(iK)^{\perp_{\mathbb R}}
 =\{bd^{-1/2}:b=b^*\}.
\tag{RC.6}
\]
Indeed, \(\zeta\in E\) precisely when \(\operatorname{Tr}(a d^{1/2}\zeta^*)\) is real for every Hermitian \(a\). A matrix \(T\) has real \(\operatorname{Tr}(aT)\) for every Hermitian \(a\) exactly when \(T\) is Hermitian: write \(T=A+iB\) with \(A,B\) Hermitian and test the imaginary part at \(a=B\). This proves (RC.6). Also \(K\cap iK=\{0\}\) and \(K+iK=H\), by the unique Hermitian real-and-imaginary decomposition before applying \(j\).

Put
\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
r=Xd^{-1/2},\quad s=Yd^{-1/2}.
\]
Both \(r,s\) belong to \(E\). Direct multiplication gives
\[
\langle r,s\rangle=\operatorname{Tr}(Xd^{-1}Y)=-\frac i2,
\qquad \langle s,r\rangle=\frac i2.
\]
For \(\lambda=1+i\), the real bilinear form \(B(x,y)=\operatorname{Re}(\lambda\langle x,y\rangle)\) consequently satisfies
\[
B(r,s)=\frac12,\qquad B(s,r)=-\frac12,
\qquad B(x,x)=\|x\|^2.
\tag{RC.7}
\]
The last equality gives coercivity for every \(x\in E\), while the first two exclude symmetry. The original real inner product and the invertible operator \(I+C\) provide the required solution despite that nonsymmetry.

For a geometric view, normalize these two real-orthogonal vectors to \(e=r/\sqrt{3/2}\) and \(f=s/\sqrt{3/2}\). The real space \(E\) is the orthogonal sum of their plane and its diagonal-matrix part. Multiplication by \(i\) keeps off-diagonal matrices orthogonal to that diagonal part. Equation (RC.3) and the displayed pairings therefore give
\[
Ce=\tfrac13 f,\qquad Cf=-\tfrac13 e,\qquad
Ae=e+\tfrac13 f,\qquad Af=f-\tfrac13 e.
\tag{RC.8}
\]

![The image of e has a positive one-third f component, while the image of f has a negative one-third e component.](figures/real-coercivity.svg)

*Exact restriction of \(A=I+C\) to the real orthonormal \((e,f)\)-plane in this example. Gray arrows are the unit basis vectors; blue arrows are their images, and orange arrows are the skew contributions. The cross terms have opposite signs, while each diagonal pairing is one. This plane is a subspace of the four-dimensional real space \(E\). Coordinates and constants are those of (RC.8). Reproducible figure source.*

## Source and scope

Marc A. Rieffel and Alfons Van Daele, *A bounded operator approach to Tomita–Takesaki theory*, Pacific Journal of Mathematics **69** (1977), 187–221, [freely readable publisher PDF](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf). The relevant source locations are Notation 5.1, Definition 5.5, and the first proof paragraph of Lemma 5.6, printed pages 208 and 211. Its subsequent bounded-multiplication argument occupies pages 212–213.

The argument above proves the real equation and its norm bound, and gives an explicit example of the distinction between coercivity and symmetry. It does not replace the later graph-projection, commutant, spectral, or analytic parts of the modular construction. All exposition and calculations here are independently written.
