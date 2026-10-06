# A bounded algebra inside its positive cone

**Independently written mathematical draft.**

Fix a standard form \((M,H,J,P)\) and a faithful normal positive functional \(\psi\), with positive vector \(\xi=\xi_\psi\). Its quarter modular power turns an algebra element into a Hilbert vector. We will show that this map identifies the operator interval \([0,1]\) exactly with the cone interval \([0,\xi]\). The exact equality is the main point: approximation by positive vectors would not recover a bounded algebra element.

The source problem is Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(5). Our proof constructs an operator from a bounded sesquilinear form and proves its membership in \(M\) by an explicit commutant calculation. The prerequisites are The bounded prerequisite boundary and Finite-vector approximation and the bicommutant, bounded forms and commutants; The corner seen by a positive vector, the finite GNS identification; Quarter powers produce a self-dual cone, the self-dual natural cone; Create analytic tests without changing the real topology, the entire algebra and its Gaussian approximants; and A spectral domain is a strip-extension condition, spectral power domains. We use A general vector identity at quarter time's proved quarter-time identity only to identify a dense family in the principal face after proving the interval theorem.

All inner products are linear in the first variable. The order on \(H\) is \(u\le v\) when \(v-u\in P\). Algebra order has its usual positive-cone meaning. No normalization \(\psi(1)=1\) is required. The existence of this faithful finite functional supplies the sigma-finiteness in the source problem: any orthogonal family of nonzero projections has strictly positive \(\psi\)-values with bounded finite subsums, hence only countably many members. Indeed, for each positive integer \(n\), only finitely many can have value at least \(1/n\). No separability of \(H\) is assumed.

## The quarter-power map is defined on the whole algebra

By SE-06, \(\xi\) is cyclic and separating for \(M\), and its GNS modular conjugation is the given \(J\). Write the modular operator and group as \(\Delta\) and \(\sigma\). The finite Tomita graph gives, for every \(x\in M\),

\[
 x\xi\in D(\Delta^{1/2}),\qquad
 \Delta^{1/2}x\xi=Jx^*\xi.
\]

Spectral Cauchy–Schwarz implies

\[
 \begin{aligned}
 \|\Delta^{1/4}v\|^2
 &\le\|v\|\,\|\Delta^{1/2}v\|
 \end{aligned}
\]

for \(v\in D(\Delta^{1/2})\). In detail, the quantity on the left is the integral of \(\lambda^{1/2}\) against the scalar spectral measure of \(v\); apply Cauchy–Schwarz to \(1\) and \(\lambda^{1/2}\). This also proves the quarter-power domain. Consequently the complex-linear map

\[
 \Theta(x)=\Delta^{1/4}x\xi
 \tag{QO.1}
\]

is defined on every \(x\in M\), with

\[
 \|\Theta(x)\|\le\|x\|\,\|\xi\|.
\]

Since \(\Delta\) is injective and \(\xi\) separating, \(\Theta\) is injective. Also \(\Delta^{it}\xi=\xi\), whence the spectral measure of \(\xi\) is supported at \(1\), and \(\Theta(1)=\xi\). The estimate shows that its norm from the operator norm to the Hilbert norm is exactly \(\|\xi\|\) when \(M\ne0\).

Let \(\mathcal A\) denote the unital algebra of norm-entire elements for \(\sigma\). CZ-02 proves

\[
 \begin{gathered}
 \sigma_z(ab)=\sigma_z(a)\sigma_z(b),\\
 \sigma_z(a)^*=\sigma_{\bar z}(a^*),\\
 \sigma_z(\sigma_w(a))=\sigma_{z+w}(a).
 \end{gathered}
\]

In particular each complex translate maps \(\mathcal A\) bijectively onto itself. Gaussian smoothing gives uniformly bounded \(a_r\in\mathcal A\) converging strongly-star to each \(a\in M\). Thus \(\mathcal A\xi\) is a dense linear subspace of \(H\).

For \(c\in\mathcal A\), MA-09 applied to \(z\mapsto\sigma_z(c)\xi\) supplies every spectral power domain and identifies that function with \(\Delta^{iz}c\xi\). It is bounded on every closed horizontal strip: real modular automorphisms are isometric, so the bound reduces to a compact imaginary segment. The finite Tomita formula therefore gives

\[
 JcJ\xi=\sigma_{-i/2}(c^*)\xi.
 \tag{QO.2}
\]

This is an identity of actual vectors on actual domains. It does not assign an imaginary modular translate to a general unsmoothed algebra element.

## Test the image by analytic positive vectors

For \(a,b\in\mathcal A\), define

\[
 \begin{gathered}
 \kappa(a,b)\\
 =\sigma_{i/4}(b)J\sigma_{i/4}(a)J\xi.
 \end{gathered}
\]

It is conjugate-linear in \(a\) and linear in \(b\). In particular \(\kappa(a,a)\in P\), by the standard-form axiom \(dJdJP\subset P\). These diagonal vectors are dense in \(P\): SE-06 and SF-04 identify \(P\) as the closure of \(dJdJ\xi\), \(d\in M\); bounded strong-star Gaussian approximation permits \(d\in\mathcal A\), and complex translation is a bijection of \(\mathcal A\).

The calculation on which the proof rests is

\[
 \begin{gathered}
 \langle\Theta(x),\kappa(a,b)\rangle\\
 =\langle xa\xi,b\xi\rangle,
 \end{gathered}
 \tag{QO.3}
\]

for every \(x\in M\) and \(a,b\in\mathcal A\). We verify the imaginary-time signs and domains explicitly.

Set \(a_+=\sigma_{i/4}(a)\), \(b_+=\sigma_{i/4}(b)\). For real \(t\), the modular relations give

\[
 \begin{gathered}
 \Delta^{it}\kappa(a,b)\\
 =\sigma_t(b_+)J\sigma_t(a_+)J\xi.
 \end{gathered}
\]

Its vector-valued entire continuation is

\[
 z\longmapsto\sigma_z(b_+)J\sigma_{\bar z}(a_+)J\xi.
\]

The conjugate parameter is necessary because \(J\) is antilinear. Both factors are norm holomorphic, and their norms are bounded on every closed horizontal strip by the imaginary-segment argument in QO-01. MA-09 therefore places \(\kappa(a,b)\) in the quarter-power domain and gives

\[
 \begin{gathered}
 \Delta^{1/4}\kappa(a,b)\\
 =bJ\sigma_{i/2}(a)J\xi.
 \end{gathered}
\]

Let \(R=J\sigma_{i/2}(a)J\in M'\). Adjoint reflection and (QO.2) give \(R^*\xi=a\xi\). Since \(x\xi\) and \(\kappa(a,b)\) both belong to \(D(\Delta^{1/4})\), self-adjointness of this power permits

\[
 \begin{gathered}
 \langle\Theta(x),\kappa(a,b)\rangle\\
 =\langle x\xi,bR\xi\rangle\\
 =\langle R^*x\xi,b\xi\rangle\\
 =\langle xa\xi,b\xi\rangle.
 \end{gathered}
\]

We used \(Rb=bR\) and \(R^*x=xR^*\). This proves (QO.3) without any formal interchange of unbounded powers.

If \(x\ge0\), (QO.3) with \(b=a\) is real and nonnegative. The density of the diagonal \(\kappa\)-vectors in \(P\), together with self-duality, implies \(\Theta(x)\in P\). Conversely, if \(\Theta(x)\in P\), the same identity gives \(\langle xv,v\rangle\ge0\) on the dense space \(v\in\mathcal A\xi\). Boundedness extends this to every \(v\in H\); polarization makes \(x\) self-adjoint, and the quadratic inequality says \(x\ge0\). We have proved

\[
 \begin{gathered}
 \Theta(x)\in P\\
 \iff x\ge0.
 \end{gathered}
 \tag{QO.4}
\]

In particular \(\Theta\) preserves and reflects order on its range, and \(\Theta([0,1])\subset[0,\xi]\). A self-adjoint element is a difference of two positives by BK-01. Since \(J\) fixes \(P\), complex linearity now also gives \(J\Theta(x)=\Theta(x^*)\).

## A cone interval defines a bounded form

Take \(\eta\in P\) with \(\eta\le\xi\). On \(\mathcal A\xi\), define

\[
 \begin{gathered}
 B_\eta(a\xi,b\xi)\\
 =\langle\eta,\kappa(a,b)\rangle.
 \end{gathered}
\]

Separatingness of \(\xi\) makes the algebra representatives unique, so this is well defined. Its linearity conventions make it a sesquilinear form, linear in the first variable. The positivity of \(\kappa(a,a)\), \(\eta\), and \(\xi-\eta\) gives

\[
 \begin{gathered}
 0\le B_\eta(a\xi,a\xi)\\
 \le\langle\xi,\kappa(a,a)\rangle
 =\|a\xi\|^2,
 \end{gathered}
\]

where (QO.3) with \(x=1\) gives the last equality. Polarization first makes the form Hermitian. Expanding \(B_\eta(v+\lambda w,v+\lambda w)\ge0\) and minimizing in \(\lambda\) proves Cauchy–Schwarz, including the case \(B_\eta(w,w)=0\) by varying \(\lambda\). Hence

\[
 |B_\eta(v,w)|\le\|v\|\,\|w\|.
\]

The form extends uniquely to all of \(H\) by norm limits. BK-01's bounded-form representation supplies a unique \(T\in B(H)\) with

\[
 B_\eta(v,w)=\langle Tv,w\rangle,
 \qquad 0\le T\le1.
\]

At this point we have a Hilbert-space operator. The next calculation is needed to prove it belongs to \(M\).

## The form respects the commutant

Fix \(c\in\mathcal A\), and put

\[
 \begin{gathered}
 y'=JcJ,\\
 r=\sigma_{-i/2}(c^*),\qquad
 s=\sigma_{-i/2}(c).
 \end{gathered}
\]

Both \(r,s\) are entire. Equation (QO.2) and the commutant property imply

\[
 y'a\xi=ar\xi,\qquad
 y'^*b\xi=bs\xi.
\]

The required identity is \(\kappa(ar,b)=\kappa(a,bs)\). To check it, again write \(a_+=\sigma_{i/4}(a)\), \(b_+=\sigma_{i/4}(b)\). By (QO.2) and adjoint reflection,

\[
 J\sigma_{-i/4}(c^*)J\xi
 =\sigma_{-i/4}(c)\xi.
\]

Consequently

\[
 \begin{aligned}
 \kappa(ar,b)
 &=b_+Ja_+J\sigma_{-i/4}(c)\xi,\\
 \kappa(a,bs)
 &=b_+\sigma_{-i/4}(c)Ja_+J\xi.
 \end{aligned}
\]

The last left-algebra factor commutes with \(Ja_+J\), proving equality. It follows that

\[
 \begin{gathered}
 B_\eta(y'a\xi,b\xi)\\
 =B_\eta(a\xi,y'^*b\xi).
 \end{gathered}
\]

After substituting the represented form and using density of \(\mathcal A\xi\), this is exactly \(Ty'=y'T\). Entire elements have bounded strong-star approximants to every member of \(M\). Their conjugates therefore approximate every member of \(M'\), and commutation with the fixed bounded \(T\) passes to these strong limits. Thus \(T\in(M')'=M\), by BK-02. Write \(x=T\in[0,1]_M\).

For \(a,b\in\mathcal A\), equations (QO.3) and the definition of the form now give

\[
 \begin{gathered}
 \langle\Theta(x),\kappa(a,b)\rangle\\
 =\langle\eta,\kappa(a,b)\rangle.
 \end{gathered}
\]

These test vectors have dense linear span. Indeed, with \(b=1\), they are \(J\sigma_{i/4}(a)J\xi\); complex translation maps \(\mathcal A\) onto itself, and \(J\mathcal A\xi\) is dense in \(H\). Therefore \(\Theta(x)=\eta\). Injectivity from QO-01 gives uniqueness, completing the exact interval theorem

\[
 \Theta([0,1])=[0,\xi].
 \tag{QO.5}
\]

The equality concerns every vector in the Hilbert-space order interval, not merely those already known to lie in the range of \(\Theta\).

## Identify the algebraic principal face

Define

\[
 F_\xi=\bigcup_{\lambda>0}[0,\lambda\xi].
\]

This is a face of the positive cone in the algebraic sense. It is a convex cone: bounds add and scale. If \(u,v\in P\) and \(u+v\in F_\xi\), a bound \(u+v\le\lambda\xi\) also bounds each of \(u,v\), so both belong to \(F_\xi\). Moreover it is the smallest such face containing \(\xi\): in any cone face containing \(\xi\), the decomposition \(\lambda\xi=\eta+(\lambda\xi-\eta)\) forces every \(0\le\eta\le\lambda\xi\) into that face. Closedness is not part of this definition.

For \(x\ge0\), we have \(0\le x\le\|x\|1\), and positivity of \(\Theta\) gives \(\Theta(x)\in F_\xi\), with \(x=0\) treated directly. Conversely, if \(0\le\eta\le\lambda\xi\), (QO.5) gives \(\eta/\lambda=\Theta(a)\) for some \(0\le a\le1\), so \(\eta=\Theta(\lambda a)\). Thus

\[
 \Theta(M_+)=F_\xi.
\]

Every \(x\in M\) is a complex linear combination of four positives: write its real and imaginary self-adjoint parts and take their positive and negative parts by BK-01. Consequently

\[
 \begin{gathered}
 E_\xi:=\Theta(M)\\
 =\operatorname{span}_{\mathbb C}F_\xi.
 \end{gathered}
 \tag{QO.6}
\]

Equation (QO.4) also yields \(E_\xi\cap P=F_\xi\). Hence \(\Theta:M\to E_\xi\) is a complex-linear order isomorphism with exactly the range in the source problem. Its self-adjoint part is \(E_\xi\cap\{v:Jv=v\}\), since \(J\Theta(x)=\Theta(x^*)\) and \(\Theta\) is injective.

The face is dense in \(P\). To see this without identifying algebraic and closed faces, take an entire \(d\) and set \(c=\sigma_{i/4}(d)\). The entire-element case of CQ-04 gives

\[
 \Theta(cc^*)=dJdJ\xi.
\]

The right-hand vectors are dense in \(P\), as proved in QO-02, and each belongs to \(F_\xi\). Thus \(\overline{F_\xi}=P\), while the face itself need not be closed.

There is a useful distinction between its norms. On the real space \(E_\xi\cap\{Jv=v\}\), define the order-unit norm

\[
 \begin{gathered}
 \|v\|_\xi=\inf\{r\ge0:\\
 -r\xi\le v\le r\xi\}.
 \end{gathered}
\]

For self-adjoint \(x\), order reflection gives \(\|\Theta(x)\|_\xi=\|x\|\), using the bounded self-adjoint norm characterization in BK-01. The Hilbert norm has only the upper bound of QO-01; the next example shows that its inverse need not be bounded.

## Congruence in matrices and a nonclosed face

**Two by two matrices.** Use the Hilbert–Schmidt standard form with \(Jv=v^*\), \(P\) the positive matrices, and

\[
 h=\begin{pmatrix}1&0\\0&4\end{pmatrix},\qquad
 \psi(x)=\operatorname{Tr}(hx).
\]

The finite matrix computation in SF-14 gives \(\xi=h^{1/2}\) and

\[
 \Theta(x)=h^{1/4}xh^{1/4}.
\]

Thus its inverse on matrices is \(v\mapsto h^{-1/4}vh^{-1/4}\). Positivity and interval bounds on both sides follow by congruence. For the projection and its image

\[
 \begin{gathered}
 p=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\\
 \Theta(p)=\frac12
 \begin{pmatrix}1&\sqrt2\\\sqrt2&2\end{pmatrix},
 \end{gathered}
\]

both \(\Theta(p)\) and \(\xi-\Theta(p)\) are positive rank-one matrices, verifying (QO.5). The unshifted vector \(p\xi\) has off-diagonal entries \(1\) and \(1/2\); it is not self-adjoint. The quarter power is therefore essential even in this elementary example.

**An infinite commutative algebra.** Let \(M=\ell^\infty(\mathbb N)\) act diagonally on \(H=\ell^2(\mathbb N)\), starting at \(n=1\), let \(J\) be coordinatewise conjugation, and let \(P\) be the nonnegative real sequences in \(H\). This is a standard form. The cone is self-dual by testing coordinate vectors. An operator commuting with all coordinate projections is diagonal, so \(M'=M\); conjugation and the \(xJxJ\)-invariance axiom follow coordinatewise. Define

\[
 \xi_n=2^{-n},\qquad
 \psi(x)=\sum_{n\ge1}4^{-n}x_n.
\]

The functional is finite and faithful; it is normal as the displayed vector functional, by CP-06. Finite-coordinate vectors show cyclicity of \(\xi\), and its nonzero coordinates show separatingness. The Tomita map \(x\xi\mapsto\bar x\xi\) is the restriction of \(J\); density makes its closure \(J\). Therefore \(\Delta=1\) and

\[
 \Theta(x)_n=2^{-n}x_n.
\]

In this model

\[
 \begin{gathered}
 F_\xi=\{v\in P:\sup_n2^n v_n<\infty\},\\
 E_\xi=\{v\in H:\sup_n2^n|v_n|<\infty\}.
 \end{gathered}
\]

The vector \(\eta_n=1/n\) lies in \(P\): for \(n\ge2\), \(1/n^2\le1/(n(n-1))\), and the latter series telescopes. But \(2^n/n\) is unbounded, so \(\eta\notin F_\xi\) and \(\eta\notin E_\xi\). For example \(2^n\ge n^2\) for \(n\ge4\), by induction. Every finite truncation of \(\eta\) belongs to \(F_\xi\) and converges in \(H\) to \(\eta\). This explicitly separates the face from its closure.

Finally, let \(e_n\in M\) be the coordinate projection. Then \(\|e_n\|=1\) while \(\|\Theta(e_n)\|=2^{-n}\to0\). Thus the inverse from the range with its Hilbert norm to the algebra with its operator norm is unbounded, even though it is an exact order isomorphism and an isometry for the self-adjoint order-unit norm.
