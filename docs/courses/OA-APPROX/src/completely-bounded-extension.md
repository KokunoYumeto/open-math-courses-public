# Completely bounded extension and factorization

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

Complete positivity requires a map to preserve every matrix positive cone. Complete boundedness asks a different question: how much can the map enlarge a matrix norm? A completely bounded map can reverse the sign of a positive element. Its extension theorem must therefore control matrix norms without imposing positivity on the extension.

The connection between the two notions comes from a two-by-two block. We place the map in an off-diagonal corner and use scalar diagonal corners to turn a norm estimate into positivity. Arveson's theorem extends the resulting positive map, and Stinespring's theorem recovers the original map as a coefficient of a representation.

Prerequisites are [Completely positive finite models](completely-positive-finite-models.md), including Arveson's extension theorem, and [Completely positive maps](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/completely-positive-maps.html), including Stinespring dilation and the multiplicative domain. We also use the elementary decomposition of a representation of a matrix algebra. The free extension and block-method sources are identified in the references below. No separability hypothesis occurs in this lesson.

## 1. Matrix norms on a subspace

Let \(V\) be a linear subspace of a C*-algebra \(A\). The norm on \(M_n(V)\) is its norm as a subspace of \(M_n(A)\). For \(\theta:V\to B(H)\), write
\[
\theta^{(n)}([v_{ij}])=[\theta(v_{ij})],\qquad
\|\theta\|_{\rm cb}=\sup_{n\ge1}\|\theta^{(n)}\|.
\]
The map is **completely bounded** if this supremum is finite, and a **complete contraction** if it is at most one. A **complete isometry** preserves the norm at every matrix size.

The map \(z\mapsto-z\) on \(\mathbb C\) has completely bounded norm one. It is not positive, since its value at \(1\) is \(-1\). Thus a completely bounded extension theorem cannot promise a completely positive extension for an arbitrary original map.

We will repeatedly use the following block criterion.

**Lemma 1.1.** For an operator \(X:L\to K\),
\[
\begin{pmatrix}1_K&X\\X^*&1_L\end{pmatrix}\ge0
\quad\Longleftrightarrow\quad \|X\|\le1.
\]
More generally, if \(P,Q\) are positive invertible operators, then
\[
\begin{pmatrix}P&X\\X^*&Q\end{pmatrix}\ge0
\quad\Longleftrightarrow\quad
\|P^{-1/2}XQ^{-1/2}\|\le1.
\]

**Proof.** In the first assertion, the quadratic form on \((\xi,\eta)\) is
\(\|\xi\|^2+2\operatorname{Re}\langle\xi,X\eta\rangle+\|\eta\|^2\).
Minimizing over \(\xi\), with \(\eta\) fixed, gives
\(\|\eta\|^2-\|X\eta\|^2\). It is nonnegative for every \(\eta\) exactly when \(\|X\|\le1\). Conjugation by \(\operatorname{diag}(P^{-1/2},Q^{-1/2})\) gives the second assertion. \(\square\)

Inner products here and below are linear in the second variable.

## 2. The scalar-diagonal operator system

Assume temporarily that \(A\) is unital. Define
\[
\mathcal S(V)=
\left\{
\begin{pmatrix}\lambda1_A&v\\w^*&\mu1_A\end{pmatrix}:
\lambda,\mu\in\mathbb C,\ v,w\in V
\right\}\subset M_2(A).
\]
It is an operator system: it is linear, closed under adjoints, and contains the identity of \(M_2(A)\). Closure of \(V\) is unnecessary. For a linear map \(\theta:V\to B(H)\), set
\[
\Phi_\theta\begin{pmatrix}\lambda1_A&v\\w^*&\mu1_A\end{pmatrix}
=\begin{pmatrix}\lambda1_H&\theta(v)\\\theta(w)^*&\mu1_H\end{pmatrix}.
\]

**Theorem 2.1 (The two-by-two device).** The map \(\theta\) is a complete contraction if and only if \(\Phi_\theta\) is completely positive. In that case \(\Phi_\theta\) is unital.

**Proof.** At matrix size \(n\), rearrange the matrix coordinates so that the two diagonal corners are grouped together. A positive element of \(M_n(\mathcal S(V))\) then has the form
\[
Z=\begin{pmatrix}\Lambda\otimes1_A&X\\X^*&\mathsf M\otimes1_A\end{pmatrix},
\qquad \Lambda,\mathsf M\in M_n(\mathbb C)_+,\quad X\in M_n(V).
\]
Add \(\varepsilon\) times the identity to both diagonal blocks. Lemma 1.1 gives
\[
\| (\Lambda+\varepsilon1_n)^{-1/2}
       X(\mathsf M+\varepsilon1_n)^{-1/2}\|\le1.
\]
Multiplication by scalar matrices preserves \(M_n(V)\), and amplification of \(\theta\) commutes with this multiplication. If \(\theta\) is a complete contraction, the same inequality holds after applying \(\theta^{(n)}\). The block criterion makes the image of the regularized \(Z\) positive. Let \(\varepsilon\downarrow0\); the positive cone is norm closed, so \(\Phi_\theta^{(n)}(Z)\ge0\). This proves complete positivity at every size.

Conversely, if \(X\in M_n(V)\) has norm at most one, Lemma 1.1 makes
\(\begin{pmatrix}1&X\\X^*&1\end{pmatrix}\)
positive. Complete positivity of \(\Phi_\theta\), followed by the same criterion, gives \(\|\theta^{(n)}(X)\|\le1\). Hence \(\theta\) is a complete contraction. The formula for \(\Phi_\theta\) gives its unitality. \(\square\)

The scalar diagonals are essential. Complete contractivity alone does not permit keeping arbitrary diagonal products unchanged while replacing the off-diagonal entries by \(\theta\). Exercise 3 gives a concrete failure.

## 3. Recover the off-diagonal coefficient

**Lemma 3.1.** Let \(A\) be unital and let
\(\Psi:M_2(A)\to B(H\oplus H)\) be ucp. Suppose
\[
\Psi(E_{11}\otimes1_A)=\begin{pmatrix}1_H&0\\0&0\end{pmatrix},\qquad
\Psi(E_{22}\otimes1_A)=\begin{pmatrix}0&0\\0&1_H\end{pmatrix}.
\]
There are a unital representation \(\pi:A\to B(K)\) and isometries \(V_1,V_2:H\to K\) such that the upper-right corner of \(\Psi(E_{12}\otimes a)\) is
\(V_1^*\pi(a)V_2\).

**Proof.** Take a unital Stinespring dilation
\(\Psi(X)=W^*\Pi(X)W\), where \(W:H\oplus H\to L\) is an isometry. Put
\(p_i=E_{ii}\otimes1_A\), and let \(P_i\) be the corresponding projection on \(H\oplus H\). A projection mapped to a projection belongs to the multiplicative domain. More directly,
\[
\|(\Pi(p_i)W-WP_i)\eta\|^2=0
\]
follows by expanding the square and using \(W^*\Pi(p_i)W=P_i\). Therefore \(\Pi(p_i)W=WP_i\).

The matrix units of \(\Pi(M_2\otimes1_A)\) identify \(L\) with \(K\oplus K\), so that
\[
\Pi([a_{ij}])=[\pi(a_{ij})]
\]
for a unital representation \(\pi\) of \(A\). The intertwining identities make \(W\) diagonal in this decomposition, with diagonal entries \(V_1,V_2\). Because \(W\) is an isometry, both entries are isometries. Compressing \(\Pi(E_{12}\otimes a)\) by \(W\) now gives the asserted formula. \(\square\)

## 4. Extension with the same completely bounded norm

**Theorem 4.1 (Completely bounded extension and factorization).** Let \(V\subset A\) be a linear subspace of a C*-algebra and let \(\theta:V\to B(H)\) be completely bounded. There are a representation \(\pi:A\to B(K)\) and operators \(S,T:H\to K\) such that
\[
\theta(v)=S^*\pi(v)T\quad(v\in V),\qquad
\|S\|\|T\|=\|\theta\|_{\rm cb}.
\]
Consequently,
\[
\widetilde\theta(a)=S^*\pi(a)T\quad(a\in A)
\]
extends \(\theta\) and satisfies
\(\|\widetilde\theta\|_{\rm cb}=\|\theta\|_{\rm cb}\).
If \(\theta\ne0\), one may choose \(\|S\|=\|T\|=\|\theta\|_{\rm cb}^{1/2}\).

**Proof.** The zero map has a zero extension and zero factorization. Otherwise put \(c=\|\theta\|_{\rm cb}>0\) and \(\theta_0=\theta/c\).

First suppose \(A\) is unital. Theorem 2.1 makes \(\Phi_{\theta_0}\) ucp on \(\mathcal S(V)\). Arveson's extension theorem gives a ucp map
\(\Psi:M_2(A)\to B(H\oplus H)\)
extending it. The two diagonal matrix units already belong to \(\mathcal S(V)\), so their values meet Lemma 3.1. That lemma gives
\[
\theta_0(v)=V_1^*\pi(v)V_2.
\]
Set \(S=c^{1/2}V_1\) and \(T=c^{1/2}V_2\). Then the required factorization holds and both norms are \(c^{1/2}\).

At every matrix size,
\[
\|[S^*\pi(a_{ij})T]\|
\le\|S\|\,\|[a_{ij}]\|\,\|T\|.
\]
Thus the extension has completely bounded norm at most \(c\). Restriction to \(V\) gives the reverse inequality, hence equality.

For nonunital \(A\), embed it in the algebra \(A^\dagger\) obtained by adjoining a unit. Matrix norms on \(V\) are unchanged. Apply the unital argument there and restrict the representation and extension to \(A\). The representation on \(A\) may be degenerate, which is allowed. Its coefficient formula still gives the same upper bound, and restriction to \(V\) still gives equality. No countability or closure of \(V\) was used. \(\square\)

The two operators generally differ. Requiring \(S=T\) would make the coefficient map completely positive, which is impossible for \(v\mapsto-v\) on a subspace containing the unit.

**Corollary 4.2 (A positive block completion).** A completely bounded map \(\theta:A\to B(H)\), of norm \(c\), has completely positive maps \(\phi_1,\phi_2:A\to B(H)\), each of norm at most \(c\), such that
\[
a\longmapsto
\begin{pmatrix}
\phi_1(a)&\theta(a)\\
\theta(a^*)^*&\phi_2(a)
\end{pmatrix}
\]
is completely positive.

**Proof.** Use the balanced factorization in Theorem 4.1 and put
\(\phi_1(a)=S^*\pi(a)S\), \(\phi_2(a)=T^*\pi(a)T\).
The displayed map is compression of \(\pi(a)\) by the row operator \((S\ T):H\oplus H\to K\). Hence it is completely positive, and the separate norms are bounded by \(\|S\|^2=\|T\|^2=c\). For \(c=0\) use zero maps. \(\square\)

This completion adjusts the diagonal entries. It does not claim that arbitrary diagonal expressions from \(A\) can be copied into the target algebra.

**Corollary 4.3 (Self-adjoint maps).** If \(\theta:A\to B(H)\) is completely bounded and satisfies \(\theta(a^*)=\theta(a)^*\), then it is a difference of two completely positive maps.

**Proof.** Take \(\theta(a)=S^*\pi(a)T\). Set
\[
\psi_\pm(a)=\tfrac14(S\pm T)^*\pi(a)(S\pm T).
\]
Both maps are completely positive. Their difference is
\(\tfrac12(S^*\pi(a)T+T^*\pi(a)S)\).
The second term is \(\theta(a^*)^*\), so self-adjointness makes the difference \(\theta(a)\). \(\square\)

## 5. Surjective two-isometries are rigid

A linear isometry of C*-algebras can preserve the scalar norm while reversing multiplication. Preserving the norm at matrix size two rules out that possibility when the map is surjective.

**Lemma 5.1.** A linear functional \(f\) on a unital C*-algebra with \(\|f\|=f(1)=1\) is positive. Consequently a unital contractive map between unital C*-algebras is positive.

**Proof.** For self-adjoint \(h\) and real \(t\),
\[
|1+itf(h)|^2\le\|1+ith\|^2\le1+t^2\|h\|^2.
\]
The linear term in \(t\) forces \(\operatorname{Im}f(h)=0\). For \(0\le h\le1\), we then have
\(|1-f(h)|=|f(1-h)|\le1\), so \(f(h)\ge0\). Rescaling proves positivity on every positive element.

For a unital contraction \(\rho\), compose with any state of the target. The resulting functional has norm at most one and value one at the unit, so is a state by the first assertion. States detect positivity in a C*-algebra, hence \(\rho\) is positive. \(\square\)

**Theorem 5.2.** Let \(\theta:A\to B\) be a surjective linear isometry of C*-algebras, and suppose \(\theta^{(2)}\) is also an isometry. There are a unitary \(u\in M(B)\) and a surjective *-isomorphism \(\pi:A\to B\) such that
\[
\theta(a)=u\pi(a)\quad(a\in A).
\]
In particular \(\theta\) is a complete isometry.

**Proof.** Pass to the bidual map \(T=\theta^{**}:A^{**}\to B^{**}\). A surjective linear isometry has a surjective isometric bidual map. We use the canonical identifications \(M_2(A)^{**}=M_2(A^{**})\) and \(M_2(B)^{**}=M_2(B^{**})\), from the enveloping von Neumann algebra construction. They show that \(T^{(2)}\) is an isometry as well. Both bidual algebras are unital.

Put \(u=T(1)\), so \(\|u\|=1\). For every \(x\in A^{**}\), the squared norm of the row \((1\ x)\), placed in a two-by-two matrix with second row zero, is \(1+\|x\|^2\). Its image has squared norm \(\|uu^*+T(x)T(x)^*\|\). Surjectivity therefore gives
\[
\|uu^*+bb^*\|=1+\|b\|^2\quad(b\in B^{**}).
\]
Since \(0\le uu^*\le1\), choose \(b=(1-uu^*)^{1/2}\). The left side is one, forcing \(1-uu^*=0\). Apply the same argument to the column \((1\ x)^{\mathsf T}\) and choose \(b=(1-u^*u)^{1/2}\). It gives \(u^*u=1\). Thus \(u\) is unitary in \(B^{**}\).

The map \(P=u^*T\) is a unital surjective two-isometry, and its inverse has the same properties. Lemma 5.1, at matrix sizes one and two, makes \(P\) and \(P^{-1}\) 2-positive. Here the Schwarz estimate uses only 2-positivity: the matrix
\[
\begin{pmatrix}x^*x&x^*\\x&1\end{pmatrix}
=\begin{pmatrix}x^*\\1\end{pmatrix}\begin{pmatrix}x&1\end{pmatrix}
\]
is positive. Applying \(P^{(2)}\) keeps it positive. Since \(P\) preserves adjoints and the unit, testing the resulting quadratic form on \((\xi,-P(x)\xi)\) gives
\[
P(x^*x)\ge P(x)^*P(x).
\]
Apply \(P^{-1}\) to this inequality and then use its Schwarz inequality on \(P(x)\). The two inequalities sandwich \(x^*x\) between identical endpoints. Applying \(P\) back gives equality:
\[
P(x^*x)=P(x)^*P(x)\quad(x\in A^{**}).
\]
Polarization yields \(P(x^*y)=P(x)^*P(y)\). A positive linear map preserves adjoints, so replacing \(x\) by \(x^*\) proves multiplicativity. Hence \(P\) is a *-isomorphism of the biduals.

It remains to locate the original algebras and the multiplier. Let \(C=P(A)\subset B^{**}\), a closed C*-subalgebra. Since \(\theta\) is onto, \(B=uC\). It follows that
\[
\overline{\operatorname{span}}(B^*B)
=\overline{\operatorname{span}}(C^*C)=C.
\]
The left side is \(B\), because a C*-algebra is the closed linear span of its products. Thus \(C=B\). In particular \(uB=B\), and multiplying this equality by \(u^*\) gives \(u^*B=B\). Taking adjoints gives \(Bu=B\) and \(Bu^*=B\). These two-sided multiplier conditions place \(u\) and \(u^*\) in \(M(B)\); they remain mutual inverses there. Restricting \(P\) gives the claimed \(\pi:A\to B\).

A *-isomorphism is isometric at every matrix size, as is multiplication by the diagonal unitary with entries \(u\). Hence \(\theta\) is a complete isometry. \(\square\)

For the zero algebras the assertion is interpreted in their zero multiplier algebra and is vacuous. The proof for nonzero algebras uses no unit in \(A\) or \(B\) themselves.

## 6. A matrix norm detects transposition

Transposition on \(M_n\) is an isometry at scalar size. Its second amplification can already enlarge norms.

**Example 6.1.** Let \(t:M_2\to M_2\) be transposition and set
\[
F=\sum_{i,j=1}^2 E_{ij}\otimes E_{ji}\in M_2(M_2).
\]
On \(\mathbb C^2\otimes\mathbb C^2\), \(F\) exchanges the tensor factors, so it is a unitary of norm one. Applying transposition to the second factor gives
\[
(\operatorname{id}_{M_2}\otimes t)(F)
=\sum_{i,j}E_{ij}\otimes E_{ij}
=|\Omega\rangle\langle\Omega|,
\qquad \Omega=e_1\otimes e_1+e_2\otimes e_2.
\]
The last operator has norm \(\|\Omega\|^2=2\). Thus transposition is neither a complete contraction nor a complete isometry.

It is also not completely positive. The positive operator \(|\Omega\rangle\langle\Omega|\) is sent by the same partial transpose to \(F\), whose value on the antisymmetric vector
\(e_1\otimes e_2-e_2\otimes e_1\) is its negative.

## 7. Exercises with solutions

**Exercise 1 (A sign can be completely bounded; introductory).** Factor \(\theta(z)=-z\) on \(\mathbb C\) in the form of Theorem 4.1 with product of operator norms one. Explain why no positive extension exists.

*Solution.* Take \(\pi(z)=z\), \(S=-1\), \(T=1\) on \(\mathbb C\). Then \(S^*\pi(z)T=-z\) and \(\|S\|\|T\|=1\). Any extension on the same algebra must still send \(1\) to \(-1\), preventing positivity.

**Exercise 2 (The regularization step; intermediate).** In Theorem 2.1, why may we add \(\varepsilon1\) to the diagonal blocks, and why must the matrices multiplying \(X\) have scalar entries?

*Solution.* Adding a positive diagonal matrix preserves positivity and makes both diagonal blocks invertible. Scalar matrix multiplication takes finite linear combinations of entries of \(X\), so stays in \(M_n(V)\) and commutes with \(\theta^{(n)}\). Multiplication by arbitrary elements of \(A\) need not preserve \(V\), and \(\theta\) need not respect it.

**Exercise 3 (Enlarging the diagonals fails; intermediate).** Let \(A=B=\mathbb C^2\), let \(e=(1,0)\), and let \(\theta\) exchange the two coordinates. Show that \(\theta\) is a complete isometry, but the rule that keeps the diagonal entries and applies \(\theta\) only to the off-diagonal entries need not preserve positivity in \(M_2(A)\).

*Solution.* Coordinate exchange is a *-automorphism, hence a complete isometry. The matrix
\(Z=\begin{pmatrix}e&e\\e&e\end{pmatrix}\)
is positive: at the first coordinate it is the scalar positive matrix of all ones, and at the second it is zero. The proposed image is
\(\begin{pmatrix}e&1-e\\1-e&e\end{pmatrix}\).
At the second coordinate it equals \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\), which has eigenvalue \(-1\). Thus even a complete isometry does not justify arbitrary unchanged diagonal products. Scalar multiples of the identity, as in \(\mathcal S(V)\), avoid this obstruction.

**Exercise 4 (The corner formula; intermediate).** With the notation of Lemma 3.1, compute all four corners of \(\Psi([a_{ij}])\).

*Solution.* The diagonal Stinespring operator gives
\[
\Psi([a_{ij}])=
\begin{pmatrix}
V_1^*\pi(a_{11})V_1&V_1^*\pi(a_{12})V_2\\
V_2^*\pi(a_{21})V_1&V_2^*\pi(a_{22})V_2
\end{pmatrix}.
\]
This also displays the positive block completion before restoring the scale.

**Exercise 5 (Balance a coefficient; intermediate).** Suppose a nonzero coefficient map has a factorization \(S^*\pi(\,\cdot\,)T\) with positive \(s=\|S\|\), \(t=\|T\|\). Rescale it so that the two operator norms agree without changing the coefficient or their product.

*Solution.* Replace \(S\) by \(\sqrt{t/s}\,S\) and \(T\) by \(\sqrt{s/t}\,T\). The scalar factors multiply to one, and both new norms are \(\sqrt{st}\). This balances an existing factorization; equality with the completely bounded norm still requires the theorem's optimal construction.

**Exercise 6 (Positive and negative coefficients; intermediate).** For a self-adjoint completely bounded map, verify Corollary 4.3 by expanding \(\psi_+\) and \(\psi_-\). If \(A\) is unital and the balanced factorization comes from isometries, compute \((\psi_++\psi_-)(1)\).

*Solution.* The pure \(S\)- and \(T\)-terms cancel in the difference, leaving \(\tfrac12(\theta(a)+\theta(a^*)^*)=\theta(a)\). The sum at the unit is
\(\tfrac12(S^*S+T^*T)=c1_H\)
when \(S\) and \(T\) are \(\sqrt c\) times isometries and \(\pi\) is unital. Thus \(\|\psi_++\psi_-\|=c\) in this construction.

**Exercise 7 (A scalar norm misses a matrix norm; intermediate).** Verify the action of \(F\) and of \(|\Omega\rangle\langle\Omega|\) in Example 6.1, and determine their spectra on \(\mathbb C^2\otimes\mathbb C^2\).

*Solution.* On an elementary tensor, \(F(e_p\otimes e_q)=e_q\otimes e_p\). It has eigenvalue \(1\) on the three-dimensional symmetric subspace and \(-1\) on the one-dimensional antisymmetric subspace. The rank-one operator has eigenvalue two on \(\mathbb C\Omega\) and zero on its orthogonal complement. Their norms are one and two, respectively.

**Exercise 8 (The row test for a unitary; intermediate).** Explain why a contraction \(u\) in a unital C*-algebra satisfying \(\|uu^*+bb^*\|=1+\|b\|^2\) for every \(b\) must be a coisometry. What extra test makes it unitary?

*Solution.* Insert \(b=(1-uu^*)^{1/2}\). The equality reads \(1=1+\|1-uu^*\|\), so \(uu^*=1\). The corresponding column identity \(\|u^*u+b^*b\|=1+\|b\|^2\), with \(b=(1-u^*u)^{1/2}\), gives \(u^*u=1\).

**Exercise 9 (Why surjectivity matters; intermediate).** Let \(V:H\to K\) be an isometry whose range is a proper subspace. Show that \(a\mapsto VaV^*\) is a complete isometry \(B(H)\to B(K)\), but does not send the unit to a unitary of \(B(K)\). Explain why this does not contradict Theorem 5.2.

*Solution.* Compression by \(V^*\) recovers \(a\), while the original map is contractive; the same argument with the amplified isometry gives equality at every size. Its value at the unit is the proper projection \(VV^*\), which is not a unitary. The map is not surjective onto \(B(K)\). In Theorem 5.2, surjectivity is what allows the decisive choice of \(b\) in the row and column tests.

## References

Edward G. Effros and Zhong-Jin Ruan, [*On matricially normed spaces*](https://msp.org/pjm/1988/132-2/pjm-v132-n2-p05-s.pdf), *Pacific Journal of Mathematics* 132(2) (1988), 243–264, Section 3, especially the full proof of Theorem 3.7, printed pp.251–257 (PDF pp.10–16). The proof uses finite matrix extensions and a point-weak* net for arbitrary Hilbert spaces.

Ved Prakash Gupta, Prabha Mandayam and V. S. Sunder, [*The Functional Analysis of Quantum Information Theory*, arXiv:1410.7188v3](https://arxiv.org/pdf/1410.7188v3), Lemma 1.1.13, Proposition 1.1.14 and Theorem 1.1.17, printed pp.10–14 (PDF pp.15–19), gives the block method. Its printed corner and coefficient notation requires correction; Sections 2–3 here give the full correct matrix entries and dilation decomposition. Lemma 5.1 also proves the scalar positivity fact that the notes leave by reference.

William B. Arveson, [*Subalgebras of C\*-algebras*](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224, Theorems 1.1.1 and 1.2.3, gives the dilation and extension methods. The [preceding lesson](completely-positive-finite-models.md#theorem-2-3) proves extension for systems that need not be closed. Sections 4–5 here prove exact norm equality, nonunital restriction and surjective two-isometry rigidity, including the multiplier conclusion.
