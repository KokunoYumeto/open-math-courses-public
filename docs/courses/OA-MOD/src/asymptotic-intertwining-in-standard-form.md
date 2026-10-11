# Asymptotic intertwining in standard form

A normal positive functional has a unique positive vector in a standard form. Approximate algebraic relations between two functionals can therefore be compared with relations between their vectors. The comparison works in both directions for uniformly bounded operator families, even when the functionals are nonfaithful and the algebra has no separability hypothesis.

Let \((M,H,J,P)\) be a standard form, with inner product linear in the first variable. Write \(\xi_\varphi\in P\) for the vector representing \(\varphi\in M_*^+\). Our actions are


\[
\begin{aligned}
\eta x&=Jx^*J\eta,\\
(\varphi x)(a)&=\varphi(xa),\\
(x\varphi)(a)&=\varphi(ax).
\end{aligned}
\]


Left and right actions commute. In particular the vector expression corresponding to \(\varphi x-x\psi\) is \(\xi_\varphi x-x\xi_\psi\), in that order.

The required standard-form facts, including existence and uniqueness of these vectors, are proved in The standard-form axioms and positive vectors, Sections 5–11. We use its norm estimates


\[
\|\xi-\eta\|^2
\leq\|\omega_\xi-\omega_\eta\|
\leq\|\xi-\eta\|\,\|\xi+\eta\|,
\qquad \xi,\eta\in P,
\]


proved in Norm estimates and uniqueness. The matrix standard form used below is constructed in Positivity seen through two components. Bounded functional calculus and the elementary C*-algebra facts are proved in Bounded operator kernel.

## 1. The direct estimate for two functionals

**Proposition 1.1.** For \(x\in M\) and \(\varphi,\psi\in M_*^+\),


\[
\begin{aligned}
\|\varphi x-x\psi\|
&\leq
\bigl(\varphi(1)^{1/2}+\psi(1)^{1/2}\bigr)\\
&\qquad\cdot\|\xi_\varphi x-x\xi_\psi\|.
\end{aligned}
\tag{1.1}
\]


**Proof.** Put \(\xi=\xi_\varphi\), \(\eta=\xi_\psi\), and \(d=\xi x-x\eta\). Since \(J\xi=\xi\) and \(J\eta=\eta\),
\(Jd=x^*\xi-\eta x^*\). For \(a\in M\), move the left adjoint in the first term and the right adjoint in the second to obtain


\[
\begin{aligned}
\varphi(xa)-\psi(ax)
&=\langle a\xi,x^*\xi\rangle
 -\langle ax\eta,\eta\rangle\\
&=\langle a\xi,Jd\rangle
 +\langle a\xi,\eta x^*\rangle
 -\langle ax\eta,\eta\rangle\\
&=\langle a\xi,Jd\rangle
 +\langle ad,\eta\rangle.
\end{aligned}
\]


Here \(\langle a\xi,\eta x^*\rangle=\langle(a\xi)x,\eta\rangle\), and \((a\xi)x=a(\xi x)\). Cauchy–Schwarz bounds the last line by \(\|a\|(\|\xi\|+\|\eta\|)\|d\|\). Take the supremum over the unit ball. \(\square\)

This implication needs no bound on a family \((x_i)\): if its vector differences tend to zero, then its functional differences tend to zero. The uniform bound will enter the converse.

## 2. Two algebras of bounded families

Fix a directed set \(I\) and one normal positive functional \(\rho\), with representing vector \(\zeta\). Let \(\ell^\infty(I,M)\) denote the C*-algebra of uniformly bounded families, with pointwise operations and supremum norm. It is complete because uniform limits of bounded families exist coordinatewise in the complete space \(M\); its C*-identity follows by taking the supremum of \(\|x_i^*x_i\|=\|x_i\|^2\).

Define


\[
\begin{aligned}
\mathcal A_\rho
&=\{(x_i):\|\rho x_i-x_i\rho\|\to0\},\\
\mathcal B_\zeta
&=\{(x_i):\|\zeta x_i-x_i\zeta\|\to0\}.
\end{aligned}
\]


**Lemma 2.1.** These are closed unital C*-subalgebras of \(\ell^\infty(I,M)\).

**Proof.** Linearity and the identity family are immediate. Set
\(D(x)=\rho x-x\rho\) and \(E(x)=\zeta x-x\zeta\). Both satisfy the product rule


\[
\begin{aligned}
D(xy)&=D(x)y+xD(y),\\
E(xy)&=E(x)y+xE(y).
\end{aligned}
\]


The module actions have norm at most the operator norm, so uniformly bounded families with vanishing defects retain that property under multiplication. Positivity of \(\rho\) gives \(D(x^*)=-D(x)^*\), where the adjoint of a functional is \(f^*(a)=\overline{f(a^*)}\). Likewise
\(JE(x)=-E(x^*)\), so the vector defect has the same norm for \(x\) and \(x^*\). Thus both sets are closed under adjoints.

Finally


\[
\begin{aligned}
\|D(x)-D(y)\|&\leq2\|\rho\|\|x-y\|,\\
\|E(x)-E(y)\|&\leq2\|\zeta\|\|x-y\|.
\end{aligned}
\]


If a family is approximated in supremum norm by families in either set, these estimates bound the eventual defect by an arbitrarily small constant. They prove closedness. This argument uses convergence of nets on the prescribed directed set; no countable cofinal subset is required. \(\square\)

## 3. Why testing unitaries suffices

**Lemma 3.1.** One has \(\mathcal A_\rho=\mathcal B_\zeta\).

**Proof.** For a unitary \(u\in M\), the vector \(u\zeta u^*\) belongs to \(P\) by the standard-form cone axiom and represents the functional \(a\mapsto\rho(u^*au)\), denoted \(u\rho u^*\). Right multiplication by \(u^*\) preserves both the Hilbert norm and the functional norm. The standard-form estimates therefore give


\[
\begin{aligned}
\|\zeta u-u\zeta\|^2
&=\|\zeta-u\zeta u^*\|^2\\
&\leq\|\rho-u\rho u^*\|\\
&=\|\rho u-u\rho\|\\
&\leq2\|\zeta\|\,\|\zeta u-u\zeta\|.
\end{aligned}
\tag{3.1}
\]


Thus a family of unitaries belongs to one of the two algebras exactly when it belongs to the other. A unitary of either unital subalgebra is a coordinatewise unitary, since its inverse is its adjoint and the identities agree. Their unitary groups consequently coincide.

Every unital C*-algebra is linearly spanned by its unitaries. Here is the needed formula. For a self-adjoint contraction \(h\), functional calculus gives


\[
v=h+i(1-h^2)^{1/2},\qquad
v^*v=vv^*=1,\qquad
h=(v+v^*)/2.
\]


Scaling treats an arbitrary self-adjoint element; splitting an element into real and imaginary self-adjoint parts expresses it as a linear combination of four unitaries. Apply this argument inside each of the closed unital algebras from Lemma 2.1. Equality of their unitary groups now implies equality of the algebras. \(\square\)

The uniform bound is used in the product rule and in forming the C*-algebra of families. Formula (3.1) alone concerns unitaries and cannot simply be asserted for arbitrary operators.

## 4. Passing from one functional to a pair

**Theorem 4.1.** For \(\varphi,\psi\in M_*^+\) and a uniformly bounded net \((x_i)\) in \(M\),


\[
\begin{aligned}
\|\varphi x_i-x_i\psi\|\to0
\quad\Longleftrightarrow\quad
\|\xi_\varphi x_i-x_i\xi_\psi\|\to0.
\end{aligned}
\tag{4.1}
\]


Both zero and nonfaithful functionals are included, and \(M\) need not be a factor.

**Proof.** Use the standard form of \(\widetilde M=M_2(M)\) on \(H^4\) constructed in Amplifying a standard form. Vectors are two-by-two matrices; the left and right actions are ordinary matrix multiplication using the respective actions on their entries, and the conjugation transposes the entries and applies \(J\).

The diagonal vector


\[
\zeta=\begin{pmatrix}\xi_\varphi&0\\0&\xi_\psi\end{pmatrix}
\]


is in the positive cone by that construction. It represents the normal positive functional
\(\rho(A)=\varphi(A_{11})+\psi(A_{22})\): multiplying \(A\zeta\) and pairing against \(\zeta\) leaves exactly these diagonal terms. Define the bounded net


\[
Y_i=\begin{pmatrix}0&x_i\\0&0\end{pmatrix}.
\]


Its functional defect is


\[
(\rho Y_i-Y_i\rho)(A)
=(\varphi x_i-x_i\psi)(A_{21}).
\]


The map \(A\mapsto A_{21}\) is contractive and maps the unit ball onto the unit ball of \(M\), by matrices supported only in the \((2,1)\) slot. Thus the two functional defects have exactly the same norm. The vector defect has just one nonzero slot:


\[
\zeta Y_i-Y_i\zeta
=\begin{pmatrix}
0&\xi_\varphi x_i-x_i\xi_\psi\\0&0
\end{pmatrix}.
\]


Its Hilbert norm is exactly the norm on the right of (4.1). Lemma 3.1 for \(\rho\) proves the equivalence. \(\square\)

The equivalence is uniform on any fixed operator-norm ball for fixed \(\varphi,\psi\), in the following qualitative sense. For every \(C<\infty\) and \(\varepsilon>0\), there is \(\delta>0\) such that


\[
\begin{gathered}
\|x\|\leq C,\qquad
\|\varphi x-x\psi\|<\delta\\
\Longrightarrow
\|\xi_\varphi x-x\xi_\psi\|<\varepsilon.
\end{gathered}
\]


Otherwise choose one counterexample for each \(\delta=1/n\); the resulting bounded sequence contradicts Theorem 4.1. The reverse direction has the explicit constant (1.1). This argument does not assert a universal reverse constant independent of the two functionals.

## 5. Moving functionals and modular eigenvectors

**Corollary 5.1.** Suppose \(\varphi_i\to\varphi\) and \(\psi_i\to\psi\) in predual norm, all functionals positive, and \(\sup_i\|x_i\|\leq C\). Then


\[
\|\varphi_i x_i-x_i\psi_i\|\to0
\quad\Longleftrightarrow\quad
\|\xi_{\varphi_i}x_i-x_i\xi_{\psi_i}\|\to0.
\]


**Proof.** Replacing the varying functionals by their limits changes the functional defect by at most
\(C(\|\varphi_i-\varphi\|+\|\psi_i-\psi\|)\). By the standard-form estimate, the corresponding vector defect changes by at most


\[
C\bigl(\|\varphi_i-\varphi\|^{1/2}
+\|\psi_i-\psi\|^{1/2}\bigr).
\]


Both errors tend to zero; apply Theorem 4.1 to the limits. \(\square\)

In particular, for a fixed normal positive functional \(\varphi\) and \(\lambda\geq0\), uniqueness of positive representing vectors gives \(\xi_{\lambda\varphi}=\sqrt\lambda\,\xi_\varphi\). Thus (4.1) becomes


\[
\|\varphi x_i-\lambda x_i\varphi\|\to0
\quad\Longleftrightarrow\quad
\|\xi_\varphi x_i-\sqrt\lambda\,x_i\xi_\varphi\|\to0.
\tag{5.1}
\]


The square root of \(\lambda\) is essential. This remains true for convergent nonnegative \(\lambda_i\), by Corollary 5.1.

**Corollary 5.2.** Let \(\varphi\) be a faithful normal state and \(\lambda>0\). If a uniformly bounded net satisfies the left side of (5.1), then, for every finite \(T\),


\[
\sup_{|t|\leq T}
\|(\sigma_t^\varphi(x_i)-\lambda^{it}x_i)\xi_\varphi\|
\longrightarrow0.
\tag{5.2}
\]


**Proof.** Write \(\xi=\xi_\varphi\) and \(\Delta=\Delta_\varphi\). The Tomita domain identity and modular covariance, proved in Modular time from a faithful normal state, give


\[
\begin{aligned}
\Delta^{1/2}x\xi&=Jx^*\xi=\xi x,\\
\Delta^{it}x\xi&=\sigma_t^\varphi(x)\xi.
\end{aligned}
\]


In particular \(x\xi\) is in the domain of \(\Delta^{1/2}\). We claim, for \(r>0\) and \(|t|\leq T\),


\[
|r^{it}-\lambda^{it}|
\leq \frac{4\max(1,T)}{\sqrt\lambda}
\,|\sqrt r-\sqrt\lambda|.
\tag{5.3}
\]


If \(|\sqrt r-\sqrt\lambda|\geq\sqrt\lambda/2\), the right side is at least two and the claim follows. Otherwise \(\sqrt r\) lies between \(\sqrt\lambda/2\) and \(3\sqrt\lambda/2\). The derivative of \(2\log s\) there is at most \(4/\sqrt\lambda\), so
\(|\log r-\log\lambda|\leq4|\sqrt r-\sqrt\lambda|/\sqrt\lambda\). Combine this with \(|e^{ita}-e^{itb}|\leq |t||a-b|\) to get (5.3).

The positive operator \(\Delta\) has no kernel. Integrate the square of (5.3) against its spectral measure at \(x_i\xi\), using the spectral calculus from Spectral kernel. This bounds the left side of (5.2) by


\[
\frac{4\max(1,T)}{\sqrt\lambda}
\,\|\xi x_i-\sqrt\lambda\,x_i\xi\|,
\]


which tends to zero by (5.1). \(\square\)

## 6. Two boundaries of the theorem

**An unbounded family.** On \(M=\ell^\infty(\mathbb N)\), let
\(\varphi(a)=\sum_{n\geq1}3\cdot4^{-n}a_n\), a faithful normal state, and put \(\psi=0\). In the diagonal standard form on \(\ell^2(\mathbb N)\), the positive vectors are coordinatewise nonnegative vectors and
\(\xi_\varphi(n)=\sqrt3\,2^{-n}\). These claims follow directly by pairing against diagonal operators; conjugation is coordinatewise complex conjugation and the right action is also diagonal multiplication. This is indeed a standard form: an operator commuting with all coordinate projections is diagonal, so the algebra is its own commutant. Testing against the positive coordinate vectors proves self-duality of the nonnegative cone, and multiplication by \(aJaJ\) multiplies coordinate \(n\) by \(|a_n|^2\), preserving that cone.

Let \(e_n\) be the coordinate projection and \(x_n=2^n e_n\). Then


\[
\begin{aligned}
\|\varphi x_n-x_n\psi\|&=3\cdot2^{-n}\to0,\\
\|\xi_\varphi x_n-x_n\xi_\psi\|&=\sqrt3.
\end{aligned}
\]


The functional norm in the first line is the absolute value of its single nonzero coefficient. The vector in the second has a single entry of modulus \(\sqrt3\). Thus the uniform boundedness hypothesis cannot be removed from the converse in Theorem 4.1, even for a commutative algebra and a faithful normal state on one side.

**One-sided modular displacement is weaker.** Let \(M=B(\ell^2(\mathbb N))\), and let \(\varphi(a)=\operatorname{Tr}(da)\) with diagonal density \(d_{nn}=2^{-n}\). The Hilbert–Schmidt standard form gives \(\xi=d^{1/2}\) and \(\sigma_t^\varphi(a)=d^{it}ad^{-it}\). For \(x_n=e_{1n}\), \(n\geq2\), one has \(\|x_n\|=1\) and


\[
\begin{aligned}
\|(\sigma_t^\varphi(x_n)-x_n)\xi\|_2
&\leq2\cdot2^{-n/2},\\
\|\varphi x_n-x_n\varphi\|
&=2^{-1}-2^{-n}.
\end{aligned}
\]


The first bound is uniform for all real \(t\), because \(x_n\xi=2^{-n/2}e_{1n}\) and modular time only multiplies this matrix unit by a scalar of modulus one. For the second, direct evaluation gives
\((\varphi x_n-x_n\varphi)(a)=(2^{-1}-2^{-n})a_{n1}\). A matrix entry has absolute value at most \(\|a\|\), and equality is attained at \(a=e_{n1}\). This proves the stated functional norm. Consequently (5.2), tested only on this one vector, does not imply (5.1). It cannot replace the square-root-domain estimate.

The basic equivalence is the general standard-form lemma of Takesaki, *Theory of Operator Algebras III*, XVIII.4, Lemma 4.2. The proof here includes arbitrary directed nets, the varying-functional version, the scaled modular consequence, and explicit checks of its hypotheses.

*Mathematical exposition by GPT-6 Astra (OpenAI), October 2026, at Ultra. CC0 1.0.*
