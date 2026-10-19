# Pure states and common maximal abelian subalgebras

A finite family of sufficiently separated pure states on a separable C*-algebra can be read on one maximal abelian subalgebra, without losing any information about how those states extend. We construct commuting positive contractions that isolate the states, then put those contractions into a maximal abelian subalgebra. The construction works without an identity and gives uniqueness among all state extensions.

## Pure states and their supports

Let \(A\) be a norm-separable C*-algebra, and let \(\varphi_1,\ldots,\varphi_n\) be pure states, where \(1\le n<\infty\), such that

\[
\|\varphi_i-\varphi_j\|=2\qquad(i\ne j).
\tag{1.1}
\]

Realize \(M=A^{**}\) in the universal representation on \(H\), and write \(\widehat\varphi_i\) for the normal extension. Its support \(p_i\in M\) is minimal, and

\[
p_iXp_i=\widehat\varphi_i(X)p_i\qquad(X\in M).
\tag{1.2}
\]

Minimality is a statement about the corner \(p_iMp_i\); it does not assert that \(p_i\) has rank one on the entire universal Hilbert space.

The programme inputs are the universal bidual and normal-extension proofs, the orthogonality of the supports in a norm-additive Jordan decomposition, Proposition 3.4, pure states and minimal supports, Lemma 1.1, Kaplansky density and the noncommutative Lusin theorem, the state Cauchy–Schwarz inequalities, Proposition 3.2 and Theorem 4.7, and continuous functional calculus. Below, finite atomic interpolation and the separable construction are proved explicitly from those results.

**Lemma 1.1.** The projections \(p_1,\ldots,p_n\) are pairwise orthogonal.

**Proof.** For \(i\ne j\), the decomposition \(\varphi_i-\varphi_j\) is norm additive, since the two states have norm one and (1.1) holds. Proposition 3.4 of the bidual lesson says that the normal supports of the positive and negative terms of any such decomposition are orthogonal. Those terms are precisely \(\varphi_i\) and \(\varphi_j\). Thus \(p_ip_j=0\). \(\square\)

Put \(p=\sum_{i=1}^np_i\), a projection, and \(\tau=\sum_{i=1}^n\widehat\varphi_i\), a positive normal functional on \(M\).

## Exact interpolation on finitely many minimal supports

**Lemma 2.1 — a projection cannot have arbitrarily small mass.** Every nonzero projection \(r\le p\) satisfies

\[
\tau(r)\ge\frac1n.
\tag{2.1}
\]


**Proof.** By (1.2),

\[
\|rp_i\|^2=\|p_irp_i\|=\widehat\varphi_i(r).
\]

Since \(r=r^2\),

\[
\|p_irp_j\|
 =\|(rp_i)^*(rp_j)\|
 \le\widehat\varphi_i(r)^{1/2}
       \widehat\varphi_j(r)^{1/2}.
\]

Expand \(r=prp=\sum_{i,j}p_irp_j\), use the triangle inequality, and then finite-dimensional Cauchy–Schwarz:

\[
\begin{aligned}
1=\|r\|
&\le\left(\sum_i\widehat\varphi_i(r)^{1/2}\right)^2\\
&\le n\sum_i\widehat\varphi_i(r)=n\tau(r).
\end{aligned}
\tag{2.2}
\]

This proves (2.1). The bound need not be sharp; its strict positivity is the useful fact. \(\square\)

**Theorem 2.2 — finite atomic interpolation.** For every \(X\in M\), there is \(a\in A\) such that

\[
ap=Xp,\qquad \|a\|\le2\|Xp\|.
\tag{2.3}
\]

If \(X=X^*\), then \(a\) can be chosen self-adjoint.

**Proof.** Apply the noncommutative Lusin theorem, Theorem 10.6 in the density lesson, with projection \(e=p\), normal functional \(\tau\), error \(\varepsilon=1/(2n)\), and multiplicative norm tolerance \(\delta=1\). It produces \(a\in A\) and a projection \(f\le p\) with

\[
af=Xf,\qquad \tau(p-f)<\frac1{2n},
\qquad \|a\|\le2\|Xf\|.
\]

If \(p-f\ne0\), Lemma 2.1 gives \(\tau(p-f)\ge1/n\), a contradiction. Hence \(f=p\), proving (2.3). Part 2 of that same Lusin theorem makes \(a\) self-adjoint when \(X\) is. If \(Xp=0\), one can also simply take \(a=0\). \(\square\)

No finite-rank assertion about \(pH\), and no assumption that the pure states have inequivalent GNS representations, enters this argument.

## A positive element with a prescribed kernel

Consider the closed C*-subalgebra

\[
D=A\cap(1-p)M(1-p)
 =\{d\in A:dp=pd=0\}.
\tag{3.1}
\]

It is a C*-subalgebra because these annihilation identities are preserved by sums, products, adjoints and norm limits.

**Lemma 3.1.** There is a bounded net of positive elements of \(D\) converging strongly to \(1-p\).

**Proof.** By positive Kaplansky density, choose positive contractions \(u_\alpha\in A\) converging strongly to \(1-p\). For each \(j\), (1.2) gives

\[
\|u_\alpha p_j\|^2
 =\widehat\varphi_j(u_\alpha^2)\longrightarrow0.
\tag{3.2}
\]

Here bounded strong convergence gives \(u_\alpha^2\to1-p\) strongly, and normal functionals are continuous on bounded strongly convergent nets. Since there are only finitely many \(p_j\),
\(\|u_\alpha p\|\le\sum_j\|u_\alpha p_j\|\to0\).

Theorem 2.2 supplies \(v_\alpha\in A\) with

\[
v_\alpha p=u_\alpha p,\qquad
\|v_\alpha\|\le2\|u_\alpha p\|\longrightarrow0.
\]

Thus \(z_\alpha=u_\alpha-v_\alpha\) satisfies \(z_\alpha p=0\) and converges strongly* to \(1-p\). Its norm is at most three. The positive elements
\(d_\alpha=z_\alpha^*z_\alpha\) lie in \(D\), have norm at most nine, and converge strongly to \(1-p\). Indeed \(d_\alpha p=0\) and its adjoint gives \(pd_\alpha=0\); bounded strong* convergence permits multiplication. \(\square\)

**Proposition 3.2 — separability supplies one kernel detector.** There exists a positive contraction \(h\in D\) such that

\[
\ker h=pH.
\tag{3.3}
\]


**Proof.** The metric subspace \(D\) of the separable normed space \(A\) is separable. To justify this inherited property, take a countable base for \(A\) and choose a point from each basic open set that meets \(D\); these points are dense in \(D\). The same argument makes the positive unit ball of \(D\) separable. Choose a dense sequence \((d_k)_{k\ge1}\) in that ball, with repetitions if necessary, and set

\[
h=\sum_{k=1}^\infty2^{-k}d_k.
\tag{3.4}
\]

The series converges in norm, and \(0\le h\le1\). Since every \(d_kp=0\), we have \(pH\subseteq\ker h\).

Conversely, if \(h\eta=0\), then

\[
0=\langle h\eta,\eta\rangle
 =\sum_k2^{-k}\langle d_k\eta,\eta\rangle.
\]

All summands are nonnegative, so \(d_k^{1/2}\eta=0\), hence \(d_k\eta=0\), for every \(k\). Density and scaling show that every positive element of \(D\) annihilates \(\eta\). In particular the bounded positive net in Lemma 3.1 annihilates it. Passing to its strong limit gives \((1-p)\eta=0\), or \(\eta\in pH\).

If \(D=0\), take every \(d_k=0\). Lemma 3.1 then implies \(1-p=0\), so the same conclusion holds with \(h=0\). \(\square\)

This is the only step that uses separability. It replaces a family of vanishing conditions by the kernel of one element of \(A\).

## Commuting selectors for the states

**Lemma 4.1.** There exist pairwise orthogonal positive contractions \(b_1,\ldots,b_n\in A\) such that

\[
b_ip_j=\delta_{ij}p_j.
\tag{4.1}
\]


**Proof.** Choose distinct \(\lambda_1,\ldots,\lambda_n\in(0,1)\), and let
\(X=\sum_j\lambda_jp_j\in M_{\mathrm{sa}}\). By Theorem 2.2 there is \(a=a^*\in A\) with \(ap=Xp=X\). Taking adjoints gives \(pa=X\), so \(a\) commutes with \(p\) and acts by \(\lambda_j\) on \(p_jH\).

Apply the continuous clipping function
\(g(t)=\max(0,\min(t,1))\). It vanishes at zero, so \(b=g(a)\in A\), even if \(A\) is nonunital. It is a positive contraction and
\(bp_j=\lambda_jp_j\), by functional calculus on the reducing subspace \(p_jH\).

Choose disjoint open intervals \(I_j\) around the \(\lambda_j\), with closures inside \((0,1)\), and continuous functions \(f_j:[0,1]\to[0,1]\), supported in \(I_j\), with \(f_j(\lambda_j)=1\). For example use triangular functions on sufficiently small symmetric intervals. Put \(b_j=f_j(b)\). Each \(f_j(0)=0\), so \(b_j\in A\). Disjoint supports give \(b_ib_j=0\) for \(i\ne j\), while evaluation at the \(\lambda_j\) gives (4.1). \(\square\)

## Positive contractions peaking at minimal supports

Keep \(h\) from Proposition 3.2 and \(b_i\) from Lemma 4.1. Define

\[
c_i=b_i-b_i h b_i\in A.
\tag{5.1}
\]


**Theorem 5.1.** The \(c_i\) are pairwise orthogonal positive contractions, and their spectral projections at the point \(1\), computed in \(M\), satisfy

\[
1_{\{1\}}(c_i)=p_i.
\tag{5.2}
\]

In particular \(\varphi_j(c_i)=\delta_{ij}\).

**Proof.** Since \(0\le h\le1\) and \(0\le b_i\le1\),

\[
0\le b_i h b_i\le b_i^2\le b_i.
\]

Consequently \(0\le c_i\le b_i\le1\). Expanding \(c_ic_j\), each of its four terms contains the adjacent product \(b_ib_j=0\) when \(i\ne j\); hence \(c_ic_j=0\). Since \(hp=0\), (4.1) also gives \(c_ip_j=\delta_{ij}p_j\). Thus \(p_iH\) is contained in the eigenspace of \(c_i\) at \(1\).

For the reverse inclusion, suppose \(c_i\eta=\eta\). From (5.1),

\[
\begin{aligned}
0
&=\|\eta\|^2-\langle c_i\eta,\eta\rangle\\
&=\langle(1-b_i)\eta,\eta\rangle
  +\|h^{1/2}b_i\eta\|^2.
\end{aligned}
\tag{5.3}
\]

Both terms are nonnegative. Their vanishing gives \(b_i\eta=\eta\) and \(h^{1/2}\eta=0\), hence \(\eta\in pH\) by (3.3). But \(b_ip=p_i\), so \(\eta=b_i\eta=b_ip\eta=p_i\eta\). The eigenspace is exactly \(p_iH\), proving (5.2). Finally (1.2) applied to \(c_i\) proves its stated values on the states. \(\square\)

## A peaking contraction determines its state

**Lemma 6.1.** Let \(\varphi\) be a pure state of \(A\), let \(e\in M\) be its minimal normal support, and let \(c\in A\) be a positive contraction with \(1_{\{1\}}(c)=e\). If a state \(\psi\) of \(A\) satisfies \(\psi(c)=1\), then \(\psi=\varphi\).

**Proof.** Extend \(\psi\) normally to \(M\); its value at \(1\) is one. Put \(d=1-c\ge0\), so \(\widehat\psi(d)=0\). For \(\varepsilon>0\), functional calculus gives

\[
0\le d(d+\varepsilon1)^{-1}\le\varepsilon^{-1}d.
\]

Hence \(\widehat\psi(d(d+\varepsilon1)^{-1})=0\). These positive contractions increase strongly to the projection onto \(\overline{dH}\), which is \(1-e\). Indeed they vanish on \(\ker d=eH\), and on a vector \(d\eta\) their difference from the identity has norm at most \(\varepsilon\|\eta\|\), since \(\|\varepsilon(d+\varepsilon1)^{-1}d\|\le\varepsilon\). Their uniform norm bound extends convergence from \(dH\) to its closure. Normality gives \(\widehat\psi(1-e)=0\), and therefore \(\widehat\psi(e)=1\).

Cauchy–Schwarz for the positive functional \(\widehat\psi\) now gives

\[
\widehat\psi((1-e)Y)=\widehat\psi(Y(1-e))=0
\quad(Y\in M).
\]

Thus \(\widehat\psi(Y)=\widehat\psi(eYe)\). Minimality and the support identity for \(\varphi\) give

\[
eYe=\widehat\varphi(Y)e,
\qquad
\widehat\psi(Y)=\widehat\varphi(Y)\widehat\psi(e)
 =\widehat\varphi(Y).
\]

Restricting to \(A\) proves the assertion. No purity assumption on \(\psi\) was used. \(\square\)

## The common maximal abelian subalgebra

A maximal abelian C*-subalgebra, or **MASA**, of \(A\) means an abelian C*-subalgebra maximal among abelian C*-subalgebras of \(A\). No identity is required in this definition.

**Theorem 7.1.** Under (1.1), there is a MASA \(B\subseteq A\) such that every \(\varphi_i|_B\) is a pure state and \(\varphi_i\) is its unique state extension to \(A\).

**Proof.** The positive contractions \(c_1,\ldots,c_n\) commute. Among the abelian C*-subalgebras containing them, every chain has an upper bound: take the norm closure of its union. Products and adjoints lie in that union because it is a chain, and commutativity survives norm limits. Zorn's lemma therefore gives an abelian C*-subalgebra \(B\) maximal among those containing the \(c_i\). Any abelian enlargement of \(B\) would still contain them, so \(B\) is a MASA of \(A\).

For \(b\in B\), both \(b\) and \(b^*\) commute with \(c_i\), and hence with its spectral projection \(p_i=1_{\{1\}}(c_i)\). One can see the latter commutation directly: \(c_i^m\) is the identity on \(\ker(1-c_i)=p_iH\), while \(\|c_i^m(1-c_i)\|\le1/(m+1)\) by scalar functional calculus. Since \(\overline{(1-c_i)H}=(1-p_i)H\) and \(\|c_i^m\|\le1\), it follows that \(c_i^m\to p_i\) strongly. Commutation passes to this limit. Equation (1.2) therefore gives

\[
bp_i=p_ib=p_ibp_i=\varphi_i(b)p_i.
\tag{7.1}
\]

For \(b,d\in B\), multiplication of (7.1) shows

\[
\varphi_i(bd)=\varphi_i(b)\varphi_i(d).
\]

Thus \(\chi_i=\varphi_i|_B\) is multiplicative and positive. It has norm one because it is contractive and \(\chi_i(c_i)=1\), with \(\|c_i\|\le1\).

Here is a direct proof that \(\chi_i\) is pure, including the nonunital case. Suppose
\(\chi_i=t\rho+(1-t)\sigma\), where \(0<t<1\) and \(\rho,\sigma\) are states of \(B\). Since \(0\le c_i\le1\) and \(\chi_i(c_i)=1\), both \(\rho(c_i)\) and \(\sigma(c_i)\) equal one. For \(b\in B\), put \(z=b-\chi_i(b)c_i\). Multiplicativity gives \(\chi_i(z^*z)=0\), so positivity gives \(\rho(z^*z)=\sigma(z^*z)=0\). The state Cauchy–Schwarz inequality
\( |\rho(z)|^2\le\rho(z^*z)\), valid also without an identity by a contractive approximate identity, gives \(\rho(z)=0\). Hence \(\rho(b)=\chi_i(b)\rho(c_i)=\chi_i(b)\); the same holds for \(\sigma\). This is extremality of \(\chi_i\).

Finally, any state \(\psi\) on \(A\) extending \(\chi_i\) has \(\psi(c_i)=1\). Lemma 6.1 and Theorem 5.1 imply \(\psi=\varphi_i\). Thus the extension is unique even among all states. \(\square\)

For an empty family there are no state conditions; the same chain argument, starting from the zero subalgebra, gives a MASA. The zero algebra has no states, so it occurs only in this empty-family case.

## Four examples

**Example 8.1 — one vector state in a matrix algebra.** Let \(A=M_d(\mathbb C)\), \(\xi\) a unit vector and \(p\) the rank-one projection onto \(\mathbb C\xi\). Take \(h=1-p\) and \(b=p\). Then \(c=b-bhb=p\), and its top eigenspace is \(p\mathbb C^d\). A diagonal MASA in an orthonormal basis beginning with \(\xi\) has the required restriction and unique extension. Indeed a state taking value one at \(p\) has support under \(p\), exactly as in Lemma 6.1.

**Example 8.2 — several orthogonal vector states.** For orthonormal \(\xi_1,\ldots,\xi_n\in\mathbb C^d\), let \(p_i\) be their rank-one projections. Taking \(b_i=c_i=p_i\) and \(h=1-\sum_i p_i\) realizes the construction directly. Extend the vectors to an orthonormal basis and take its diagonal algebra. If \(n=d\), then \(p=1\), \(D=0\), and \(h=0\); this is the zero-kernel-algebra case explicitly allowed in Proposition 3.2.

**Example 8.3 — a nonunital commutative algebra.** In \(A=C_0(\mathbb R)\), choose distinct points \(t_1,\ldots,t_n\) and disjoint small intervals about them. Continuous triangular functions \(c_i\), supported in those intervals and equal to one only at \(t_i\), are orthogonal positive contractions. Point evaluations are multiplicative states; the extremality argument in Theorem 7.1 proves their purity. Here the common MASA is \(A\) itself, so extending any of these restrictions back to \(A\) has only one possible meaning. The disjoint triangular functions illustrate why the selectors can belong to the nonunital algebra rather than merely to its unitization.

**Example 8.4 — separation matters.** In \(M_2(\mathbb C)\), take the vector states for \(e_1\) and \((e_1+e_2)/\sqrt2\). They cannot both restrict to pure states on one MASA. To see this, every MASA of \(M_2\) contains the identity and a nonscalar self-adjoint matrix; diagonalizing that matrix makes the MASA the entire diagonal algebra, because the matrix has two distinct eigenvalues and its commutant is diagonal. The restriction of a unit vector state to this algebra has weights given by the squared absolute values of its two coordinates. It is pure only when one coordinate is zero. Two distinct such vector states therefore come from orthogonal lines, whereas the displayed vectors are neither parallel nor orthogonal.

The finite-family theorem appears as Theorem 1.1 in C. A. Akemann, [*Approximate units and maximal abelian C*-subalgebras*, Pacific Journal of Mathematics 33 (1970), 543–550](https://msp.org/pjm/1970/33-3/pjm-v33-n3-p01-s.pdf). The proof above supplies the finite-support interpolation, kernel construction and uniqueness arguments used here.
