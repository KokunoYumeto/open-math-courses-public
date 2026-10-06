# Order, local units and quotients of C*-algebras

*Public domain (CC0).*

The practical problem is to manipulate elements of an abstract C*-algebra as reliably as matrices. Can we take a square root, cut off the small spectrum of a positive element, remove an ideal, and recover positive elements from the quotient? Each operation needs a norm or order guarantee. This lesson develops those guarantees and uses them to connect functional calculus with localization and quotients.

Use \(C_0(\mathbb R)\) as a running example of an algebra without an identity. Its functions can be cut off on larger compact sets, but no single function is identically one. For a closed set \(F\), functions that vanish on \(F\) form an ideal; passing to the quotient retains exactly the values on \(F\). The commutative ideal theorem proves this description, including the quotient norm. General C*-algebras have the same local-unit and quotient mechanisms even when there is no underlying point space.

The first part builds the calculus and order. The second uses local units immediately to construct quotients and solve lifting problems. The third asks when local units can be chosen in a sequence, studies convolution as a concrete model, and finishes with the asymmetric decomposition theorem. The theorem labels give precise references within each part.

The Banach-algebra lesson supplies unitization, spectra and Gelfand theory. The Stone–Weierstrass lesson supplies its \(C_0\) form and Urysohn functions. Haar integration is used by the convolution examples; the exact internal providers are linked where needed.

## Conventions

*Algebras.* We use the conventions of [Banach algebras, involutions and C\*-algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-01). All algebras are complex. An *involutive Banach algebra* is a Banach algebra with an isometric involution, and a *C\*-algebra* is an involutive Banach algebra with \(\|x^*x\|=\|x\|^2\) for all \(x\). The zero algebra \(\{0\}\) is a C\*-algebra; it is unital with \(1=0\). A unital algebra is *nontrivial* if \(1\neq0\). In a nontrivial unital C\*-algebra \(\|1\|=1\), since \(1^*=1\) and so \(\|1\|=\|1^*1\|=\|1\|^2\) ([the norm of the identity](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-03)). \(A_h\) is the set of self-adjoint elements, \(G(A)\) the group of invertible elements and \(U(A)\) the set of unitaries of a unital \(A\). "Ideal" means two-sided ideal; one-sided ideals are called left or right ideals.

*The unitization.* For every C\*-algebra \(A\), \(\widetilde A\) denotes the *forced unitization*. As an algebra it is \(A_1=A\oplus\mathbb C\) with the product of [adjoining an identity](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-04); a new identity is adjoined even when \(A\) already has one. We identify \(a\in A\) with \((a,0)\) and write \(a+\lambda\) for \((a,\lambda)\). The norm is \(\|a+\lambda\|=\max\big(\|L_{a+\lambda}\|,|\lambda|\big)\), where \(L_{a+\lambda}\) is the operator \(b\mapsto ab+\lambda b\) of left multiplication on \(A\). This is a C\*-norm in both cases:
- If \(A\) is not unital, \(\|L_{a+\lambda}\|\) alone is a C\*-norm on \(A_1\) and dominates \(|\lambda|\) ([the C\*-norm on the unitization](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-05)), so taking the maximum changes nothing.
- If \(A\) is unital, the map \(a+\lambda\mapsto(a+\lambda1_A,\lambda)\) is a \(*\)-isomorphism of \(\widetilde A\) onto the direct sum \(A\oplus\mathbb C\) with the norm \(\max(\|b\|,|\lambda|)\), which is a C\*-algebra because the C\*-identity holds in each coordinate. The map is an algebra isomorphism by [adjoining an identity](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-04). It is isometric because \(L_{a+\lambda}=L_c\) with \(c=a+\lambda1_A\), and \(\|L_c\|=\|c\|\) (test at \(1_A\)).

So \(\widetilde A\) is a unital C\*-algebra, \(A\) is a closed ideal of codimension one in it, and \(q(a+\lambda)=\lambda\) is a unital \(*\)-homomorphism \(q:\widetilde A\to\mathbb C\) with kernel \(A\). None of this uses the functional calculus, so there is no circularity below.

*Spectra.* For unital \(A\), \(\sigma_A(x)\) is the spectrum. For every \(A\), the *quasi-spectrum* is \(\sigma'_A(x)=\sigma_{\widetilde A}(x)\), computed in the forced unitization. Invertibility is an algebraic property, so this is the quasi-spectrum of [spectrum and quasi-spectrum](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-06). It always contains \(0\), and \(\sigma'_A(x)=\sigma_A(x)\cup\{0\}\) when \(A\) is unital. \(r(x)\) is the spectral radius. [Example 3.3](#oa-fnd-cf-06) shows why an identity is adjoined to unital algebras too. \(\operatorname{Ch}(A)\) is the set of characters, and \(\hat x(\omega)=\omega(x)\) is the Gelfand transform ([characters](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-16), [the Gelfand representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-18)).

*Functions and spaces.* LCH means locally compact Hausdorff. For an LCH space \(\Omega\), \(C_0(\Omega)\) and \(C_c(\Omega)\) are the continuous functions on \(\Omega\) that vanish at infinity and that have compact support, and \(C_b(\Gamma)\) is the algebra of bounded continuous functions on a space \(\Gamma\). For a compact \(K\subseteq\mathbb C\) and \(f\in C(K)\), \(\|f\|_K=\max_K|f|\). From the lesson on the Stone–Weierstrass theorem we use [Urysohn's lemma](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-16), the complex [Stone–Weierstrass theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09) with its compact form, and the [density of the polynomials](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-17) \(p(\lambda,\bar\lambda)\) in \(C(K)\) for compact \(K\subseteq\mathbb C\). Hilbert spaces are complex, and inner products are linear in the first variable. \(B(H)\) is the C\*-algebra of bounded operators on a Hilbert space \(H\).

*The zero algebra.* For \(A=\{0\}\): \(1=0\), \(\sigma(0)=\varnothing\), \(\sigma'(0)=\{0\}\), \(C(\sigma(0))=\{0\}\), and the square root of \(0\) is \(0\). This algebra has no states, which is why the facts about states used in Section 13 assume \(A\neq0\). Every result below holds for the zero algebra, some with empty data; \(B(H)\) with \(H=0\) is an example.

## A. Build the calculus and the order

Begin with the spectral radius of a normal element. The commutative representation theorem turns continuous scalar functions into algebra elements, and spectral permanence ensures that the answer is independent of the C*-subalgebra used to compute it. Square roots and positive parts then turn scalar inequalities into an order on the algebra. The continuity and automatic-continuity results justify these operations under limits and homomorphisms. The order tests at the end show where matrix intuition must be used carefully.

### 1. Self-adjoint, normal and unitary elements

**Definition 1.1.** In an involutive Banach algebra \(A\), call \(x\) *self-adjoint* (or *hermitian*) if \(x^*=x\), and *normal* if \(x^*x=xx^*\). If \(A\) is unital, \(x\) is *unitary* if \(x^*x=xx^*=1\). A *projection* is an element \(p\) with \(p=p^*=p^2\).

**Proposition 1.2.**
1. (*Cartesian decomposition.*) Every \(x\in A\) can be written in exactly one way as \(x=x_1+ix_2\) with \(x_1,x_2\in A_h\), namely \(x_1=\frac12(x+x^*)\) and \(x_2=\frac1{2i}(x-x^*)\). Moreover \(\|x_1\|\leq\|x\|\) and \(\|x_2\|\leq\|x\|\). The set \(A_h\) is a closed real subspace, and \(A=A_h\oplus iA_h\) as real Banach spaces.
2. \(x\) is normal exactly when \(x_1\) and \(x_2\) commute. Self-adjoint and unitary elements are normal.
3. If \(A\) is unital, then \(1\in A_h\), and \(U(A)\) is a closed subgroup of \(G(A)\) with \(u^{-1}=u^*\in U(A)\). If \(A\) is a nontrivial unital C\*-algebra, then \(\|u\|=1\) for every unitary \(u\).
4. In a C\*-algebra, every projection has norm \(0\) or \(1\).

**Proof.** (1) If \(x=x_1+ix_2\) with \(x_1,x_2\) self-adjoint, then \(x^*=x_1-ix_2\), and solving gives the two formulas. Conversely, these formulas define self-adjoint elements with \(x_1+ix_2=x\). Since the involution is isometric, \(\|x_1\|\leq\frac12(\|x\|+\|x^*\|)=\|x\|\), and the same holds for \(x_2\). \(A_h\) is the set of fixed points of the continuous real-linear map \(x\mapsto x^*\), so it is closed.
(2) Expanding gives
\[
\begin{gathered}
x^*x\\
=x_1^2+x_2^2+i(x_1x_2-x_2x_1),\\
xx^*\\
=x_1^2+x_2^2-i(x_1x_2-x_2x_1).
\end{gathered}
\]
So \(x^*x=xx^*\) exactly when \(x_1x_2=x_2x_1\). A self-adjoint element commutes with its adjoint, and so does a unitary \(u\), since \(u^*u=1=uu^*\).
(3) The adjoint \(1^*\) is again an identity, because \(1^*x=(x^*1)^*=x\) and \(x1^*=(1x^*)^*=x\); so \(1^*=1\). If \(u,v\) are unitary, then \((uv)^*(uv)=v^*u^*uv=1\) and \((uv)(uv)^*=1\); and \(u^{-1}=u^*\) is unitary. If unitaries \(u_n\) converge to \(u\), continuity of the product and of the involution gives \(u^*u=uu^*=1\). In a nontrivial unital C\*-algebra, \(\|u\|^2=\|u^*u\|=\|1\|=1\).
(4) \(\|p\|=\|p^*p\|=\|p\|^2\). \(\square\)

In the zero algebra, \(0\) is a unitary and a projection.

**Theorem 1.3** (The norm of a normal element is its spectral radius). Let \(A\) be a C\*-algebra.
1. For \(h\in A_h\), \(\|h^{2^k}\|=\|h\|^{2^k}\) for all \(k\geq0\), and \(r(h)=\|h\|\).
2. For every normal \(x\in A\), \(r(x)=\|x\|\).
3. For every \(x\in A\), \(\|x\|^2=\|x^*x\|=r(x^*x)\).
4. (*The norm is determined by the algebra.*) If an algebra with involution is a C\*-algebra for two norms, the two norms are equal.

**Proof.** (1) \(\|h^2\|=\|h^*h\|=\|h\|^2\), and \(h^{2^k}\) is again self-adjoint, so induction gives the first claim. The [spectral radius formula](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-09) \(r(h)=\lim_n\|h^n\|^{1/n}\), taken along \(n=2^k\), gives \(r(h)=\|h\|\).
(2) The element \(x^*x\) is self-adjoint, so \(\|x\|^2=\|x^*x\|=r(x^*x)\) by (1). If \(x\) is normal, \(x^*\) and \(x\) commute, and the spectral radius is submultiplicative on commuting elements (a corollary of the [spectral radius formula](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-09)); so \(r(x^*x)\leq r(x^*)r(x)\). In \(\widetilde A\), \(\lambda-x\) has an inverse \(w\) exactly when \(\bar\lambda-x^*\) has the inverse \(w^*\). So \(\sigma'_A(x^*)=\overline{\sigma'_A(x)}\) and \(r(x^*)=r(x)\). Hence \(\|x\|^2\leq r(x)^2\leq\|x\|^2\), where the last step uses \(r(x)\leq\|x\|\) ([the spectrum is compact](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-07)).
(3) This was shown in the proof of (2).
(4) The quasi-spectrum of an element depends only on the algebra, because invertibility in \(A_1\) is an algebraic property. So the spectral radius \(r\) does not depend on the norm. By (3), both norms satisfy \(\|x\|^2=r(x^*x)\). \(\square\)

**Example 1.4** (Normality is needed). In \(M_2(\mathbb C)\), \(E_{12}^2=0\), so \(r(E_{12})=0\), while \(\|E_{12}\|=1\).

**Proposition 1.5** (Spectra of adjoints, unitaries and self-adjoint elements). Let \(A\) be a C\*-algebra.
1. For every \(x\in A\), \(\sigma'_A(x^*)=\{\bar\lambda:\lambda\in\sigma'_A(x)\}\).
2. If \(A\) is unital and \(u\in U(A)\), then \(\sigma_A(u)\subseteq\mathbb T=\{\lambda:|\lambda|=1\}\).
3. For \(h\in A_h\), \(\sigma'_A(h)\subseteq[-\|h\|,\|h\|]\), and \(\sigma'_A(h)\) contains \(\|h\|\) or \(-\|h\|\). If \(A\) is unital and nontrivial, the same holds for \(\sigma_A(h)\).

**Proof.** (1) was shown in the proof of Theorem 1.3(2).
(2) In the zero algebra \(\sigma_A(u)=\varnothing\). Otherwise \(\|u\|=\|u^{-1}\|=1\) by Proposition 1.2(3). The spectrum of an element lies in the closed disc whose radius is its norm ([the spectrum is compact](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-07)), and \(\sigma_A(u^{-1})=\{\lambda^{-1}:\lambda\in\sigma_A(u)\}\) ([spectrum and quasi-spectrum](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-06)). So \(\sigma_A(u)\) and \(\sigma_A(u^{-1})\) lie in the closed unit disc, and every \(\lambda\in\sigma_A(u)\) has \(|\lambda|\leq1\) and \(|\lambda|^{-1}\leq1\).
(3) Work in the nontrivial unital C\*-algebra \(\widetilde A\). Put \(u=\exp(ih)=\sum_n(ih)^n/n!\) ([the exponential](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-14)). The involution is continuous and conjugate linear, so applying it to the partial sums gives \(u^*=\exp(-ih)\). Since \(ih\) and \(-ih\) commute, \(\exp(ih)\exp(-ih)=\exp(-ih)\exp(ih)=1\). So \(u\) is unitary, and by the [spectral mapping theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-12) and (2),
\[
\{e^{i\lambda}:\lambda\in\sigma'_A(h)\}=\sigma_{\widetilde A}(u)\subseteq\mathbb T .
\]
Since \(|e^{i\lambda}|=e^{-\operatorname{Im}\lambda}\), every \(\lambda\in\sigma'_A(h)\) is real. By Theorem 1.3, \(r(h)=\|h\|\). The quasi-spectrum is compact and not empty ([the spectrum is compact](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-07)), so the supremum \(\|h\|\) of \(|\lambda|\) over it is attained. For nontrivial unital \(A\), \(\sigma_A(h)\) is not empty ([the spectrum is not empty](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-08)) and \(\sigma'_A(h)=\sigma_A(h)\cup\{0\}\). If \(h\neq0\), the point of modulus \(\|h\|\) lies in \(\sigma_A(h)\); if \(h=0\), then \(\sigma_A(h)=\{0\}\). \(\square\)

**Exercise 1.6** (easy; Powers of normal elements). Show that \(\|x^n\|=\|x\|^n\) for normal \(x\) and all \(n\geq1\). Show by examples that the equality can fail for nonnormal \(x\), and that it can hold for all \(n\) without \(x\) being normal.

*Solution.* \(x^n\) is normal, so \(\|x^n\|=r(x^n)=r(x)^n=\|x\|^n\), by Theorem 1.3 and the identity \(r(x^n)=r(x)^n\), which follows from the [spectral radius formula](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-09). For \(E_{12}\in M_2(\mathbb C)\), \(\|E_{12}^2\|=0<1\). The unilateral shift \(S\) on \(\ell^2(\mathbb N)\) is an isometry, so \(\|S^n\|=1=\|S\|^n\), but \(S^*S=1\neq SS^*\).

### 2. Commutative C\*-algebras

**Theorem 2.1** (Commutative Gelfand–Naimark theorem). For an abelian C\*-algebra \(A\), put \(\Omega=\operatorname{Ch}(A)\).
1. Every character of \(A\) is a \(*\)-homomorphism: \(\omega(x^*)=\overline{\omega(x)}\).
2. The Gelfand representation \(\mathcal G(x)=\hat x\) is an isometric \(*\)-isomorphism of \(A\) onto \(C_0(\Omega)\). In particular \(A\) is semisimple.
3. If \(A\) is unital, \(\Omega\) is compact and \(A\cong C(\Omega)\).


**Proof.** Every element of \(A\) is normal. The [Gelfand representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-18) satisfies \(\|\hat x\|_\infty=r(x)\), and \(r(x)=\|x\|\) by Theorem 1.3. Thus \(\mathcal G\) is an isometric homomorphism, and in particular injective. Let \(h\in A_h\) and \(\omega\in\Omega\). Then \(\omega(h)\in\sigma'_A(h)\), because characters take their values in the quasi-spectrum ([characters are contractive](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-17)), and \(\sigma'_A(h)\) is real by Proposition 1.5(3). For \(x=x_1+ix_2\) as in Proposition 1.2, \(\omega(x^*)=\omega(x_1)-i\omega(x_2)=\overline{\omega(x)}\). This is (1), and it says \(\widehat{x^*}=\overline{\hat x}\). The image \(\mathcal G(A)\) is complete, hence closed. It is a self-adjoint subalgebra of \(C_0(\Omega)\). It separates the points of \(\Omega\), since distinct characters differ at some \(x\), and it vanishes nowhere, since characters are not zero. By the [Stone–Weierstrass theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09), \(\mathcal G(A)=C_0(\Omega)\). Part (3) holds because the character space of a unital commutative Banach algebra is compact ([characters are contractive](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-17)). \(\square\)

For \(A=\{0\}\) the statement reads \(\{0\}\cong C_0(\varnothing)\).

**Proposition 2.2** (The characters of \(C_0(\Omega)\)). Let \(\Omega\) be an LCH space, and let \(\operatorname{ev}_p(f)=f(p)\) for \(p\in\Omega\) and \(f\in C_0(\Omega)\).
1. \(p\mapsto\operatorname{ev}_p\) is a homeomorphism of \(\Omega\) onto \(\operatorname{Ch}(C_0(\Omega))\) with the weak\* topology. Under it, the Gelfand transform of \(f\) is \(f\) itself.
2. Two LCH spaces \(\Omega\) and \(\Omega'\) are homeomorphic if and only if \(C_0(\Omega)\) and \(C_0(\Omega')\) are isomorphic as algebras; a \(*\)-isomorphism is not needed.
3. Every abelian C\*-algebra \(A\) is \(*\)-isomorphic to \(C_0(\Omega)\) for an LCH space \(\Omega\), unique up to homeomorphism; one choice is \(\Omega=\operatorname{Ch}(A)\).

**Proof.** (1) This is proved in [the characters of \(C_0(\Omega)\)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-19), by a compactness argument that uses no measure theory. Remark 2.3 gives a second proof.
(2) If \(\Phi:C_0(\Omega)\to C_0(\Omega')\) is an algebra isomorphism, then \(\chi\mapsto\chi\circ\Phi\) is a bijection of \(\operatorname{Ch}(C_0(\Omega'))\) onto \(\operatorname{Ch}(C_0(\Omega))\). It and its inverse \(\chi'\mapsto\chi'\circ\Phi^{-1}\) are weak\* continuous, because they are continuous in each evaluation. Composing with the homeomorphisms of (1) gives a homeomorphism \(\Omega'\to\Omega\). The converse is clear: a homeomorphism \(\tau\) gives \(f\mapsto f\circ\tau\).
(3) Existence is Theorem 2.1; uniqueness is (2). \(\square\)

**Remark 2.3** (A second proof of (1), through measure theory). Let \(\rho\) be a character of \(C_0(\Omega)\). We show in four steps that \(\rho=\operatorname{ev}_p\) for some \(p\in\Omega\).
- *\(\rho\) is positive.* For \(f\geq0\), \(\rho(f)=\rho(f^{1/2})^2\geq0\), because \(\rho(f^{1/2})\) is real by Theorem 2.1(1). So by the [Riesz representation theorem](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-01) there is a positive Radon measure \(\mu\) on \(\Omega\) with \(\rho(x)=\int x\,d\mu\) for \(x\in C_c(\Omega)\).
- *\(\mu(\Omega)=1\).* By the same theorem, \(\mu(\Omega)\) is the supremum of \(\rho(k)\) over \(k\in C_c(\Omega)\) with \(0\leq k\leq1\), and each such \(\rho(k)\) is at most \(\|\rho\|\leq1\), because characters are contractive ([characters are contractive](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-17)). Conversely, pick \(g\) with \(\rho(g)\neq0\) and put \(f=\bar gg/\|g\|^2\). Then \(0\leq f\leq1\) and \(\rho(f)=|\rho(g)|^2/\|g\|^2=t>0\), so \(\rho(f^{1/n})=t^{1/n}\to1\) while \(0\leq f^{1/n}\leq1\). Here \(\rho(f^{1/n})=\rho(f)^{1/n}\), because the root \(f^{1/n}\) is a uniform limit of polynomials in \(f\) without constant term (the compact form of the [Stone–Weierstrass theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09)), and \(\rho\) is continuous and multiplicative. For \(\eta>0\), \(k=\max(f^{1/n}-\eta,0)\) lies in \(C_c(\Omega)\), has \(0\leq k\leq1\) and \(\|k-f^{1/n}\|\leq\eta\), so \(\mu(\Omega)\geq\rho(k)\geq t^{1/n}-\eta\).
- *The formula holds on \(C_0(\Omega)\).* Since \(\mu\) is finite, both sides of \(\rho(x)=\int x\,d\mu\) are continuous for the supremum norm, and \(C_c(\Omega)\) is dense in \(C_0(\Omega)\) ([spaces of continuous functions](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-01)).
- *\(\mu\) is a point mass.* With \(\mu(\Omega)=1\), \(\int|x-\rho(x)|^2\,d\mu=\rho(\bar xx)-|\rho(x)|^2=0\) for every \(x\in C_0(\Omega)\). Let \(S\) be the set of points every open neighbourhood of which has positive measure. Each point outside \(S\) has an open null neighbourhood, so \(\Omega\setminus S\) is open. Every compact subset of this open set has a finite cover by those null neighbourhoods and hence has measure zero. Radon inner regularity on the open set gives \(\mu(\Omega\setminus S)=0\). Since \(\mu(\Omega)=1\), \(S\) is nonempty. If \(p\in S\) and \(x(p)\ne\rho(x)\), continuity gives an open neighbourhood of \(p\) on which \(|x-\rho(x)|^2\) is bounded below by a positive number; its positive measure contradicts the displayed integral identity. Thus \(x(p)=\rho(x)\) for every \(p\in S\) and every \(x\in C_0(\Omega)\). Two distinct points of \(S\) would be separated by a compactly supported continuous function, by the earlier Urysohn lemma, which is impossible. Hence \(S=\{p\}\), its complement is null, and \(\mu=\delta_p\). Therefore \(\rho=\operatorname{ev}_p\).

The full argument above proves positivity, total mass and the extension from compactly supported functions before identifying the point mass.

**Exercise 2.4** (hard; The Stone–Čech compactification). Let \(\Gamma\) be a completely regular Hausdorff space and \(A=C_b(\Gamma)\) with the supremum norm. For \(\gamma\in\Gamma\) let \(\omega_\gamma(x)=x(\gamma)\), and let \(\iota:\Gamma\to\operatorname{Ch}(A)\), \(\iota(\gamma)=\omega_\gamma\).
(a) \(A\) is a C\*-algebra with identity.
(b) \(\iota\) is a homeomorphism of \(\Gamma\) onto a dense subset of \(\operatorname{Ch}(A)\).
(c) \(\iota(\Gamma)\) is open in \(\operatorname{Ch}(A)\) if and only if \(\Gamma\) is locally compact.
(d) Every continuous map \(f\) of \(\Gamma\) into a compact Hausdorff space \(K\) is \(g\circ\iota\) for exactly one continuous \(g:\operatorname{Ch}(A)\to K\).

*Solution.* (a) \(C_b(\Gamma)\) is a Banach space ([spaces of continuous functions](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-01)), closed under pointwise products and conjugation, with \(\sup|\bar xx|=(\sup|x|)^2\), and the constant \(1\) is its identity.
(b) \(\omega_\gamma\) is a character. \(\iota\) is injective because points of a completely regular Hausdorff space are separated by bounded continuous functions. It is weak\* continuous because each \(\gamma\mapsto x(\gamma)\) is continuous. It is open onto its image: for \(\gamma\in U\) open, complete regularity gives \(x\in A\) with \(0\leq x\leq1\), \(x(\gamma)=1\) and \(x=0\) off \(U\); then \(W=\{\omega:\operatorname{Re}\omega(x)>\frac12\}\) is weak\* open and \(\iota^{-1}(W)\subseteq U\) contains \(\gamma\). *Density.* If some \(\omega_0\) had a neighbourhood missing \(\iota(\Gamma)\), [Urysohn's lemma](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-16) on the compact Hausdorff space \(\operatorname{Ch}(A)\) would give a continuous \(F\) with \(F(\omega_0)=1\) and \(F=0\) on \(\overline{\iota(\Gamma)}\). By Theorem 2.1, \(F=\hat x\) for some \(x\in A\); then \(x(\gamma)=F(\omega_\gamma)=0\) for all \(\gamma\), so \(x=0\) and \(F=0\), a contradiction.
(c) If \(\iota(\Gamma)\) is open in the compact Hausdorff space \(\operatorname{Ch}(A)\), it is locally compact, since open subspaces of compact Hausdorff spaces are ([locally compact spaces](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-15)); so \(\Gamma\cong\iota(\Gamma)\) is locally compact. Conversely let \(\Gamma\) be locally compact and \(\gamma_0\in\Gamma\). Urysohn's lemma in its locally compact form gives \(x\in C_c(\Gamma)\) with \(0\leq x\leq1\), \(x(\gamma_0)=1\) and support in a compact set \(C\). The set \(V=\{\omega:\operatorname{Re}\omega(x)>\frac12\}\) is open and contains \(\omega_{\gamma_0}\). If \(\omega\in V\), density gives a net \(\omega_{\gamma_\alpha}\to\omega\), eventually in \(V\), so eventually \(x(\gamma_\alpha)>\frac12\) and \(\gamma_\alpha\in C\); hence \(\omega\) lies in the compact, hence closed, set \(\iota(C)\). So \(V\subseteq\iota(C)\subseteq\iota(\Gamma)\), and \(\iota(\Gamma)\) is open.
(d) For \(\omega\in\operatorname{Ch}(A)\), \(\varphi\mapsto\omega(\varphi\circ f)\) is a character of \(C(K)\) (it is \(1\) at \(1\)), hence evaluation at a unique point \(g(\omega)\in K\) (Proposition 2.2). For \(\varphi\in C(K)\), \(\varphi\circ g(\omega)=\omega(\varphi\circ f)\) is continuous in \(\omega\), and by Urysohn's lemma the topology of \(K\) is the weak topology defined by \(C(K)\), so \(g\) is continuous. Also \(\omega_\gamma(\varphi\circ f)=\varphi(f(\gamma))\), so \(g(\omega_\gamma)=f(\gamma)\). Two continuous maps into a Hausdorff space that agree on a dense set agree everywhere, which gives uniqueness.

*The Hausdorff condition.* In this lesson "completely regular" includes the Hausdorff (\(T_1\)) axiom. Without that axiom, (b) fails: on a two-point space with the indiscrete topology, every continuous function is constant, and \(\iota\) is not injective.

**Exercise 2.5** (medium; Separability). Let \(A\) be an abelian C\*-algebra with character space \(\Omega\). Show that \(A\) has a countable dense subset exactly when \(\Omega\) has a countable base.

*Solution.* By Theorem 2.1, \(A=C_0(\Omega)\). If \(\Omega\) has a countable base, its one-point compactification \(\Omega_\infty\) is compact metrizable (the metrizability theorem in [Urysohn's lemma, complete regularity and metrizability](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-16)). So \(C(\Omega_\infty)\) is separable ([density results](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-17)), and so is its subspace \(C_0(\Omega)\), the functions on \(\Omega_\infty\) that vanish at \(\infty\) ([\(C_0(X)\) and the one-point compactification](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-03)). Conversely, let \((x_n)\) be dense in \(C_0(\Omega)\), and put \(V_n=\{|x_n|>\frac23\}\), an open set. Let \(p\in U\) with \(U\) open. Urysohn's lemma gives \(f\in C_c(\Omega)\) with \(0\leq f\leq1\), \(f(p)=1\) and support in \(U\). Take \(n\) with \(\|x_n-f\|<\frac13\). Then \(p\in V_n\), and on \(V_n\), \(|f|>\frac13\), so \(V_n\subseteq U\). So \((V_n)\) is a countable base.

### 3. C\*-subalgebras and spectral permanence

**Definition 3.1.** In a C\*-algebra \(A\), a *C\*-subalgebra* is a norm-closed subalgebra \(B\) with \(B^*=B\); with the inherited structure, \(B\) is itself a C\*-algebra. If \(A\) is unital, \(B\) is a *unital C\*-subalgebra* when \(1_A\in B\). Intersections of C\*-subalgebras are C\*-subalgebras. So every \(E\subseteq A\) lies in a smallest C\*-subalgebra \(C^*(E)\), the C\*-subalgebra *generated* by \(E\); for unital \(A\), \(C^*(1,E)\) is the smallest unital one. \(C^*(E)\) is the closure of the set of noncommutative polynomials without constant term in the elements of \(E\cup E^*\). If \(x\) is normal, \(C^*(x)\) and \(C^*(1,x)\) are commutative, because \(x\), \(x^*\) and \(1\) commute and closures of commutative algebras are commutative.

**Theorem 3.2** (Spectral permanence). Let \(A\) be a C\*-algebra, \(B\subseteq A\) a C\*-subalgebra, and \(x\in B\).
1. If \(A\) is unital and \(1_A\in B\), then \(\sigma_B(x)=\sigma_A(x)\). Equivalently, an element of \(B\) that is invertible in \(A\) has its inverse in \(B\).
2. \(\sigma'_B(x)=\sigma'_A(x)\).
3. If \(A\) and \(B\) are both unital, possibly with different identities, then \(\sigma_B(x)\cup\{0\}=\sigma_A(x)\cup\{0\}\).

Example 3.3 explains why spectra in algebras with different identities must be compared after adjoining zero, as in (3).

**Proof.** (1) Always \(\sigma_A(x)\subseteq\sigma_B(x)\), because an inverse in \(B\) is an inverse in \(A\). It is enough to show that \(y\in B\cap G(A)\) implies \(y^{-1}\in B\); apply this to \(y=\lambda-x\).
*First, \(y\) self-adjoint.* Then \(0\notin\sigma_A(y)\), and \(\sigma_B(y)\subseteq\mathbb R\) by Proposition 1.5(3), applied in the C\*-algebra \(B\). So \(y-i/n\) is invertible in \(B\) for every \(n\geq1\). In \(A\), \(y-i/n\to y\in G(A)\), and inversion is continuous on \(G(A)\) ([invertible elements and the Neumann series](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-02)). So \((y-i/n)^{-1}\to y^{-1}\), and \(y^{-1}\in B\) because \(B\) is closed.
*General \(y\).* The elements \(y^*y\) and \(yy^*\) of \(B\) are self-adjoint and invertible in \(A\). By the first step their inverses lie in \(B\). Then \((y^*y)^{-1}y^*\) is a left inverse and \(y^*(yy^*)^{-1}\) a right inverse of \(y\) in \(B\), so \(y\) is invertible in \(B\).
(2) Let \(B'=B+\mathbb C1\subseteq\widetilde A\). It is a unital C\*-subalgebra of \(\widetilde A\): it is \(*\)-closed, and closed because \(B\) is closed and has codimension at most one in it. Since \(q(1)=1\) and \(q(B)=0\), \(B\cap\mathbb C1=\{0\}\). So \(b+\lambda1\mapsto(b,\lambda)\) is an algebra isomorphism of \(B'\) onto the unitization \(B_1\) of \(B\), and spectra agree under algebra isomorphisms. By (1) in \(\widetilde A\),
\[
\sigma'_B(x)=\sigma_{B_1}(x)=\sigma_{B'}(x)=\sigma_{\widetilde A}(x)=\sigma'_A(x).
\]
(3) combines (2) with the relation \(\sigma'=\sigma\cup\{0\}\) for unital algebras ([spectrum and quasi-spectrum](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-06)). \(\square\)

**Example 3.3** (Why an identity is adjoined to every algebra). Part (2) needs the quasi-spectrum of a unital algebra to be computed after adjoining a new identity, as in the Conventions. If instead \(\sigma'_B=\sigma_B\) for unital \(B\), then (2) fails. Take \(A=c_0\), the null sequences, which is not unital, \(B=\mathbb Ce_1\), which is unital with identity \(e_1\), and \(x=e_1\). Then \(\sigma'_A(e_1)=\{0,1\}\) but \(\sigma_B(e_1)=\{1\}\).

**Example 3.4** (Closure under the involution is needed). Let \(A=C(\mathbb T)\), and let \(B\) be the closure in \(A\) of the polynomials in \(z\). It is a closed unital subalgebra, but not \(*\)-closed. By the maximum modulus principle (Theorem 3.6 and Exercise 4 of [Cauchy's theorem for cycles and its consequences](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html)), a sequence of polynomials that converges uniformly on \(\mathbb T\) converges uniformly on the closed disc \(\bar{\mathbb D}\); so each \(g\in B\) extends to a function \(G\) continuous on \(\bar{\mathbb D}\) and holomorphic inside. If \(|\lambda|<1\) and \((z-\lambda)g=1\) on \(\mathbb T\), then \((w-\lambda)G(w)-1\) is holomorphic in \(\mathbb D\), continuous on \(\bar{\mathbb D}\) and zero on \(\mathbb T\), hence zero; at \(w=\lambda\) this says \(-1=0\). So \(\sigma_B(z)\) contains the open disc, and \(\sigma_B(z)=\bar{\mathbb D}\), while \(\sigma_A(z)=\mathbb T\).

### 4. Homomorphisms: contractivity, isometry and automatic continuity

**Definition 4.1.** A *\(*\)-homomorphism* between algebras with involution is an algebra homomorphism \(\pi\) with \(\pi(x^*)=\pi(x)^*\).

**Theorem 4.2** (\(*\)-homomorphisms are contractive). Let \(A\) be a Banach algebra with an involution that is not assumed to be continuous, \(B\) a C\*-algebra, and \(\pi:A\to B\) a \(*\)-homomorphism. Then for every \(x\in A\)
\[
\begin{gathered}
\sigma'_B(\pi(x))\\
\subseteq\sigma'_A(x),\\
\|\pi(x)\|^2\\
\leq r_A(x^*x)\\
\leq\|x^*x\|\\
\leq\|x^*\|\,\|x\| .
\end{gathered}
\tag{4.1}
\]
Consequently:
1. if \(\|x^*\|\leq C\|x\|\) for all \(x\), then \(\|\pi(x)\|\leq C^{1/2}\|x\|\);
2. if the involution is isometric, then \(\|\pi(x)\|\leq\|x\|\);
3. in particular every \(*\)-homomorphism between C\*-algebras is contractive, whatever is assumed about its continuity.

**Proof.** The map \(\pi_1(a+\lambda)=\pi(a)+\lambda\) is a unital homomorphism from \(A_1\) to \(\widetilde B\), and unital homomorphisms map invertible elements to invertible elements. So \(\lambda\notin\sigma'_A(x)\) implies \(\lambda\notin\sigma'_B(\pi(x))\), and \(r_B(\pi(y))\leq r_A(y)\) for all \(y\). The element \(\pi(x)^*\pi(x)=\pi(x^*x)\) is self-adjoint, so by Theorem 1.3(1)
\[
\begin{gathered}
\|\pi(x)\|^2\\
=\|\pi(x^*x)\|\\
=r_B(\pi(x^*x))\\
\leq r_A(x^*x)\\
\leq\|x^*x\| ,
\end{gathered}
\]
where the last step uses \(r_A(y)\leq\|y\|\) ([the spectrum is compact](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-07)). \(\square\)

**Example 4.3** (An isometric involution is needed for contractivity). Let \(t>1\), \(S=\operatorname{diag}(1,t)\in M_2(\mathbb C)\), and \(\|x\|_S=\|SxS^{-1}\|\) (operator norm). This is a complete algebra norm on \(M_2(\mathbb C)\), and the usual adjoint is an involution for it, continuous but not isometric. The identity map \(\pi\) from \((M_2(\mathbb C),\|\cdot\|_S)\) to the C\*-algebra \(M_2(\mathbb C)\) is a \(*\)-homomorphism. Since \(SE_{12}S^{-1}=t^{-1}E_{12}\) and \(SE_{21}S^{-1}=tE_{21}\), we get \(\|\pi(E_{12})\|=1>t^{-1}=\|E_{12}\|_S\). The bound (4.1) is sharp here: \(\|E_{12}^*\|_S\|E_{12}\|_S=t\cdot t^{-1}=1\).

**Theorem 4.4** (Injective homomorphisms do not shrink normal elements). Let \(A\) be a C\*-algebra, \(B\) a Banach algebra and \(\pi:A\to B\) an injective algebra homomorphism. Neither continuity nor compatibility with an involution is assumed.
1. \(\|\pi(x)\|\geq\|x\|\) for every normal \(x\in A\).
2. If \(B\) has an involution and \(\pi\) is a \(*\)-homomorphism, then \(\|x\|^2\leq\|\pi(x)^*\|\,\|\pi(x)\|\) for all \(x\). If moreover the involution of \(B\) is isometric, then \(\|\pi(x)\|\geq\|x\|\) for all \(x\).
3. If, in (2), \(\pi(A)\) is closed, the last inequality also follows from Theorem 4.2 applied to \(\pi^{-1}:\pi(A)\to A\).

The proof below uses the closure of \(\pi(C^*(h))\), so it makes no continuity assumption on \(\pi\).

**Proof.** (1) Let \(x\) be normal. Put \(A_0=C^*(x)\), a commutative C\*-algebra (Definition 3.1), and let \(B_0\) be the closure of \(\pi(A_0)\) in \(B\), a commutative Banach algebra. Adjoin identities: \(\widetilde{A_0}\) is a commutative unital C\*-algebra (Conventions), \(\widetilde{B_0}=B_0\oplus\mathbb C\) with the sum norm is a commutative unital Banach algebra ([adjoining an identity](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-04)), and \(\tilde\pi(a+\lambda)=\pi(a)+\lambda\) is an injective unital homomorphism. The character spaces \(X=\operatorname{Ch}(\widetilde{A_0})\) and \(Y=\operatorname{Ch}(\widetilde{B_0})\) are compact, because the algebras are unital ([characters are contractive](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-17)). The map \(\tau(\chi)=\chi\circ\tilde\pi\) from \(Y\) to \(X\) is weak\* continuous, so \(F=\tau(Y)\) is compact, hence closed.
*Claim: \(F=X\).* Suppose \(\omega_0\in X\setminus F\). The space \(X\) is compact Hausdorff, hence regular, so it has an open \(U\ni\omega_0\) whose closure misses \(F\). By Urysohn's lemma and Theorem 2.1, there are \(a,b\in\widetilde{A_0}\) with \(\hat a(\omega_0)=1\), \(\hat a=0\) off \(U\), \(\hat b=1\) on \(F\) and \(\hat b=0\) on \(\overline U\). Then \(\hat a\hat b=0\), so \(ab=0\), and \(a\neq0\). For every \(\chi\in Y\), \(\chi(\tilde\pi(b))=\hat b(\tau\chi)=1\). So no character of \(\widetilde{B_0}\) vanishes at \(\tilde\pi(b)\), and \(\tilde\pi(b)\) is invertible, since in a unital commutative Banach algebra an element at which no character vanishes is invertible ([the Gelfand representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-18)). Hence \(\tilde\pi(a)=\tilde\pi(ab)\tilde\pi(b)^{-1}=0\), and \(a=0\) by injectivity, a contradiction.
Now, in a commutative Banach algebra the spectral radius is the largest modulus of the Gelfand transform ([the Gelfand representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-18)). Using this in both algebras, the fact that \(\tau\) maps \(Y\) onto \(X\), and Theorem 1.3 in \(\widetilde{A_0}\),
\[
\begin{gathered}
\|\pi(x)\|\\
\geq r_{\widetilde{B_0}}(\pi(x))\\
=\max_{\chi\in Y}|\chi(\tilde\pi(x))|\\
=\max_{\omega\in X}|\omega(x)|\\
=r_{\widetilde{A_0}}(x)\\
=\|x\| .
\end{gathered}
\]
(2) \(x^*x\) is normal, so by (1), \[
\begin{gathered}
\|x\|^2\\
=\|x^*x\|\\
\leq\|\pi(x^*x)\|\\
=\|\pi(x)^*\pi(x)\|\\
\leq\|\pi(x)^*\|\|\pi(x)\|.
\end{gathered}
\]
(3) \(\pi(A)\) is then a closed \(*\)-subalgebra of \(B\), an involutive Banach algebra, and \(\pi^{-1}\) is a \(*\)-homomorphism from it to the C\*-algebra \(A\). By Theorem 4.2, \(\|x\|=\|\pi^{-1}(\pi(x))\|\leq\|\pi(x)\|\). \(\square\)

**Example 4.5** (Normality is needed in (1)). With \(S=\operatorname{diag}(1,t)\), \(t>1\), the map \(\pi(x)=SxS^{-1}\) is an algebra automorphism of the C\*-algebra \(M_2(\mathbb C)\), not \(*\)-preserving. It satisfies \(\|\pi(E_{12})\|=t^{-1}<1=\|E_{12}\|\).

**Corollary 4.6.** An injective \(*\)-homomorphism from a C\*-algebra into a C\*-algebra is isometric. Its range is closed.

**Proof.** The map is contractive by Theorem 4.2 and does not decrease norms by Theorem 4.4(2). An isometric image of a complete space is complete, hence closed. \(\square\)

**Theorem 4.7** (Automatic continuity). Let \(A\) be a Banach algebra, \(B\) a C\*-algebra, and \(\pi:A\to B\) an injective algebra homomorphism whose range is self-adjoint: \(\pi(A)^*=\pi(A)\). Then \(\pi\) is continuous.

**Proof.** For \(x\in A\), \(\pi(x)^*\) lies in \(\pi(A)\), so \(x^\sharp=\pi^{-1}(\pi(x)^*)\) is well defined. It is an involution on \(A\): it is conjugate linear, \((xy)^\sharp=\pi^{-1}(\pi(y)^*\pi(x)^*)=y^\sharp x^\sharp\), and \(x^{\sharp\sharp}=x\). By construction \(\pi\) is a \(*\)-homomorphism for \(\sharp\). By (4.1), which does not need a continuous involution,
\[
\|\pi(x)\|^2\leq\|x^\sharp\|\,\|x\|\qquad(x\in A).
\tag{4.2}
\]
We show that \(\sharp\) has a closed graph. Let \(x_n\to x\) and \(x_n^\sharp\to y\). By (4.2),
\[
\begin{gathered}
\|\pi(x)-\pi(x_n)\|^2\\
\leq\|x^\sharp-x_n^\sharp\|\,\|x-x_n\|\to0,\\
\|\pi(y)-\pi(x_n^\sharp)\|^2\\
\leq\|y^\sharp-x_n\|\,\|y-x_n^\sharp\|\to0 ,
\end{gathered}
\]
because in each product the first factor stays bounded and the second tends to \(0\). Since \(\pi(x_n^\sharp)=\pi(x_n)^*\to\pi(x)^*\), we get \(\pi(y)=\pi(x)^*=\pi(x^\sharp)\), and \(y=x^\sharp\). By the closed graph theorem, applied to the real-linear map \(\sharp\), there is \(k\) with \(\|x^\sharp\|\leq k\|x\|\). Then (4.2) gives \(\|\pi(x)\|\leq k^{1/2}\|x\|\). \(\square\)

**Corollary 4.8.** Let \(\pi\) be an algebra isomorphism of a C\*-algebra \(A\) onto a C\*-algebra \(B\), not assumed to preserve the involution. Then \(\pi\) and \(\pi^{-1}\) are continuous: \(c\|x\|\leq\|\pi(x)\|\leq C\|x\|\) with constants \(c,C>0\). Moreover \(\|\pi(x)\|\geq\|x\|\) for every normal \(x\).

**Proof.** The range \(B\) is self-adjoint, so \(\pi\) is continuous by Theorem 4.7. The inverse is an algebra isomorphism of \(B\) onto \(A\), so it is continuous for the same reason. The last claim is Theorem 4.4(1). \(\square\)

**Example 4.9** (A self-adjoint range is needed). Let \(E=\ell^2(\mathbb N)\) with the zero product; it is a commutative Banach algebra. Choose a discontinuous linear functional \(\varphi\) on \(E\). One exists by the axiom of choice: extend the linearly independent unit vectors \(e_1,e_2,\dots\) to a Hamel basis, and put \(\varphi(e_n)=n\) and \(\varphi=0\) on the other basis vectors. Let \(D(\xi)\) be the diagonal operator on \(\ell^2(\mathbb N)\) with entries \(\xi_n\); it is bounded, and \(\xi\mapsto D(\xi)\) is injective. Put \(T(\xi)=D(\xi)+\varphi(\xi)E_{12}\), where \(E_{12}e_2=e_1\), and on \(\ell^2\oplus\ell^2\) put
\[
\pi(\xi)=\begin{pmatrix}0&T(\xi)\\0&0\end{pmatrix}.
\]
Then \(\pi(\xi)\pi(\eta)=0=\pi(\xi\eta)\), so \(\pi\) is a homomorphism into \(B(\ell^2\oplus\ell^2)\). It is injective, since the diagonal of \(T(\xi)\) is \(\xi\). It is not continuous, since the matrix entry \(\langle T(\xi)e_2,e_1\rangle=\varphi(\xi)\) is not. Its range consists of nonzero nilpotents and zero, and is not self-adjoint.

### 5. The continuous functional calculus

**Theorem 5.1** (The continuous functional calculus). Let \(A\) be a unital C\*-algebra, \(x\in A\) normal, \(S=\sigma_A(x)\), and \(\iota\in C(S)\) the function \(\iota(\lambda)=\lambda\).
1. There is exactly one unital \(*\)-homomorphism \(\Phi_x:C(S)\to A\) with \(\Phi_x(\iota)=x\). It is an isometric \(*\)-isomorphism of \(C(S)\) onto \(C^*(1,x)\). We write \(f(x)=\Phi_x(f)\).
2. For \(f,g\in C(S)\) and scalars \(\alpha,\beta\): \((\alpha f+\beta g)(x)=\alpha f(x)+\beta g(x)\), \((fg)(x)=f(x)g(x)\), \(\bar f(x)=f(x)^*\), \(1(x)=1\), and \(p(x)=\sum c_{jk}x^j(x^*)^k\) for \(p(\lambda)=\sum c_{jk}\lambda^j\bar\lambda^k\).
3. (*Spectral mapping.*) \(\sigma_A(f(x))=f(S)\), and \(f(x)\) is normal.
4. \(\|f(x)\|=\|f\|_S\).
5. (*Composition.*) If \(g\in C(f(S))\), then \((g\circ f)(x)=g(f(x))\).
6. \(f(x)\) commutes with every \(y\in A\) that commutes with \(x\) and \(x^*\).
7. (*Independence of the algebra.*) If \(B\) is a unital C\*-subalgebra of \(A\) containing \(x\), the calculus of \(x\) in \(B\) is the same map.
8. (*Characters.*) If \(D\) is a commutative unital C\*-subalgebra containing \(x\) and \(\chi\in\operatorname{Ch}(D)\), then \(\chi(f(x))=f(\chi(x))\).
9. (*Real form.*) If \(f\) is real, \(f(x)\) is self-adjoint. For \(x\in A_h\), \(f\mapsto f(x)\) maps \(C(S;\mathbb R)\) isometrically onto the self-adjoint part of \(C^*(1,x)\).
10. (*Agreement with the holomorphic calculus.*) If \(F\) is holomorphic on an open set \(U\supseteq S\), the element \(F(x)\) given by the [holomorphic functional calculus](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-10) equals \(\Phi_x(F|_S)\).

**Proof.** If \(A=\{0\}\), then \(S=\varnothing\), \(C(S)=\{0\}\), and everything is trivial. Let \(A\) be nontrivial.

(1) *Existence.* \(B=C^*(1,x)\) is a commutative unital C\*-algebra (Definition 3.1). Put \(\Omega=\operatorname{Ch}(B)\), a compact space, and \(\psi(\omega)=\omega(x)\). By Theorem 2.1, \(\mathcal G_B:B\to C(\Omega)\) is an isometric \(*\)-isomorphism. The map \(\psi\) is continuous, and \(\psi(\Omega)=\sigma_B(x)\), because in a unital commutative Banach algebra the spectrum of an element is the range of its Gelfand transform ([the Gelfand representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-18)). By spectral permanence (Theorem 3.2(1)), \(\sigma_B(x)=S\). The map \(\psi\) is injective: if \(\omega(x)=\omega'(x)\), then also \(\omega(x^*)=\omega'(x^*)\) by Theorem 2.1(1), and \(\omega(1)=\omega'(1)=1\); so \(\omega\) and \(\omega'\) agree on the polynomials in \(x\) and \(x^*\), which are dense in \(B\), and characters are continuous ([characters are contractive](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-17)). A continuous bijection of a compact space onto a Hausdorff space is a homeomorphism. So \(f\mapsto f\circ\psi\) is an isometric \(*\)-isomorphism of \(C(S)\) onto \(C(\Omega)\), and \(\Phi_x(f)=\mathcal G_B^{-1}(f\circ\psi)\) is an isometric \(*\)-isomorphism of \(C(S)\) onto \(B\). It is unital, and \(\Phi_x(\iota)=\mathcal G_B^{-1}(\hat x)=x\).
*Uniqueness.* A unital \(*\)-homomorphism \(\Phi':C(S)\to A\) with \(\Phi'(\iota)=x\) agrees with \(\Phi_x\) on the polynomials in \(\iota\) and \(\bar\iota\), which are dense in \(C(S)\) ([density results](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-17)). It is contractive by Theorem 4.2. So \(\Phi'=\Phi_x\).
(2) holds because \(\Phi_x\) is a unital \(*\)-homomorphism with \(\Phi_x(\bar\iota)=x^*\).
(3) \(\sigma_A(f(x))=\sigma_B(f(x))\) by Theorem 3.2(1), and this equals \(\sigma_{C(S)}(f)\) because \(\Phi_x\) is an algebra isomorphism onto \(B\). In \(C(S)\), \(f-\mu\) is invertible exactly when it has no zero on \(S\), so \(\sigma_{C(S)}(f)=f(S)\). Images of commuting elements commute, so \(f(x)\) is normal.
(4) \(\Phi_x\) is isometric.
(5) By (3), \(f(x)\) is normal with spectrum \(f(S)\). The map \(g\mapsto(g\circ f)(x)\) is a unital \(*\)-homomorphism \(C(f(S))\to A\) that sends \(\iota\) to \(f(x)\). By the uniqueness in (1), applied to \(f(x)\), it is \(g\mapsto g(f(x))\).
(6) \(y\) commutes with every polynomial in \(x\) and \(x^*\), hence with their limits.
(7) \(\sigma_B(x)=\sigma_A(x)\) by Theorem 3.2(1). The calculus of \(x\) in \(B\) is a unital \(*\)-homomorphism into \(A\) sending \(\iota\) to \(x\); apply the uniqueness in (1).
(8) \(\chi\) restricts to a character of \(C^*(1,x)\subseteq D\), since \(\chi(1)=1\). So \(\chi\circ\Phi_x\) is a character of \(C(S)\), hence evaluation at some \(s\in S\) (Proposition 2.2(1)), and \(s=\chi(\Phi_x(\iota))=\chi(x)\).
(9) If \(f=\bar f\), then \(f(x)^*=\bar f(x)=f(x)\). If \(y\in C^*(1,x)\) is self-adjoint and \(y=f(x)\), then \(\bar f(x)=y^*=y=f(x)\), and injectivity gives \(f=\bar f\).
(10) For \(\lambda\notin S\), both \((\lambda-x)^{-1}\) and \(\Phi_x((\lambda-\iota)^{-1})\) are inverses of \(\lambda-x\), so they are equal. Choose a cycle \(\Gamma\) that surrounds \(S\) in \(U\), as in the definition of the holomorphic calculus. The map \(\lambda\mapsto F(\lambda)(\lambda-\iota)^{-1}\) from \(\Gamma^*\) to \(C(S)\) is continuous. At each \(s\in S\), \(\frac1{2\pi i}\) times its integral takes the value \(\frac1{2\pi i}\int_\Gamma F(\lambda)(\lambda-s)^{-1}\,d\lambda=F(s)\), by Cauchy's integral formula, since \(\operatorname{Ind}_\Gamma(s)=1\); here evaluation at \(s\) is a bounded functional, so it passes through the integral. The bounded linear map \(\Phi_x\) also passes through the integral, so
\[
\begin{gathered}
\Phi_x(F|_S)\\
=\frac1{2\pi i}\int_\Gamma F(\lambda)\,\Phi_x\big((\lambda-\iota)^{-1}\big)\,d\lambda\\
=\frac1{2\pi i}\int_\Gamma F(\lambda)(\lambda-x)^{-1}\,d\lambda\\
=F(x).\\
\square
\end{gathered}
\]

**Remark 5.2.** The uniqueness in (1) holds even among unital algebra homomorphisms of \(C(S)\) *into* \(C^*(1,x)\) that send \(\iota\) to \(x\), with no continuity or \(*\) assumed. If \(\Phi'\) is one, \(\sigma=\Phi_x^{-1}\circ\Phi'\) is a unital algebra endomorphism of \(C(S)\) fixing \(\iota\). For \(s\in S\), \(\operatorname{ev}_s\circ\sigma\) is a character, so it is \(\operatorname{ev}_t\) for some \(t\) (Proposition 2.2), and \(t=\operatorname{ev}_s(\sigma(\iota))=s\). So \(\sigma\) is the identity.
#### Fuglede’s theorem

The continuous-calculus proof in Theorem 5.1(6) assumes commutation with both \(x\) and \(x^*\). Commutation with \(x\) alone implies the second condition, as follows. This theorem is used later in the [joint functional calculus, Sections 3.2–3.3 of the Kaplansky lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#oa-fnd-kd-03).

**Theorem (Fuglede).** If \(x\) is normal in a C*-algebra \(A\) and \(xy=yx\), then \(x^*y=yx^*\).

**Proof.** Work in the forced unitization \(\widetilde A\). The [exponential laws of Proposition 7.1 of the Banach-algebra lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-14) give
\[
F(z)=e^{zx^*}y e^{-zx^*}\qquad(z\in\mathbb C).
\]
Because \(y\) commutes with \(x\), it commutes with the exponential series \(e^{\bar z x}\). Inserting \(y=e^{-\bar z x}y e^{\bar z x}\), and using normality to combine commuting exponentials, gives
\[
F(z)=U(z)yU(z)^{-1},
\qquad U(z)=e^{zx^*-\bar z x}.
\]
The exponent \(X=zx^*-\bar z x\) satisfies \(X^*=-X\). Applying the adjoint to the norm-convergent exponential series gives \(U(z)^*=e^{-X}=U(z)^{-1}\), so \(U(z)\) is unitary. The C*-identity gives \(\|U(z)\|=\|U(z)^*\|=1\). Submultiplicativity, applied to this conjugation and its inverse, therefore gives \(\|F(z)\|=\|y\|\).

The absolutely convergent product series is
\[
\begin{gathered}
F(z)\\
=\sum_{m\geq0}z^m c_m,
\\
c_m\\
=\sum_{j+k=m}\frac{(-1)^k}{j!\,k!}(x^*)^j y(x^*)^k .
\end{gathered}
\]
For every \(R>0\), \(\sum_mR^m\|c_m\|\leq\|y\|e^{2R\|x\|}\). Thus, for each bounded linear functional \(\varphi\) on \(\widetilde A\), the function \(\varphi(F(z))=\sum_mz^m\varphi(c_m)\) is entire by [Lemma 3.1 of the Cauchy lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html#oa-fnd-ct-03). It is bounded by \(\|\varphi\|\|y\|\), hence constant by [Liouville’s theorem, Corollary 3.3 there](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html#oa-fnd-ct-03). Its coefficient of \(z\) is zero: \(\varphi(c_1)=0\), where \(c_1=x^*y-yx^*\). [Hahn–Banach separation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-02) now gives \(c_1=0\). \(\square\)

This is the exponential and Liouville proof of the operator version in the Kaplansky lesson, using bounded linear functionals in place of vector coefficients. It works directly in every C*-algebra and requires no representation theorem.

**Theorem 5.3** (The calculus without an identity). Let \(A\) be a C\*-algebra, \(x\in A\) normal and \(S'=\sigma'_A(x)\), a compact set containing \(0\). For \(f\in C(S')\), let \(f(x)\in\widetilde A\) be given by Theorem 5.1 in \(\widetilde A\). Identify \(C_0(S'\setminus\{0\})\) with \(\{f\in C(S'):f(0)=0\}\).
1. \(q(f(x))=f(0)\). So \(f(x)\in A\) if and only if \(f(0)=0\).
2. \(f\mapsto f(x)\) is an isometric \(*\)-isomorphism of \(C_0(S'\setminus\{0\})\) onto \(C^*(x)\).
3. If \(A\) is unital and \(f(0)=0\), then \(f(x)\) equals the unital calculus \((f|_{\sigma_A(x)})(x)\) of Theorem 5.1 in \(A\). So the two calculi never disagree.
4. If \(D\subseteq A\) is a commutative C\*-subalgebra containing \(x\), \(\chi\in\operatorname{Ch}(D)\) and \(f(0)=0\), then \(\chi(f(x))=f(\chi(x))\).

**Proof.** (1) \(q\) is a character of the commutative unital C\*-subalgebra \(C^*(1,x)\) of \(\widetilde A\), and \(q(x)=0\). Apply Theorem 5.1(8). The kernel of \(q\) is \(A\).
(2) The map is an isometric \(*\)-homomorphism into \(A\) by (1) and Theorem 5.1. The polynomials \(p(\lambda,\bar\lambda)\) without constant term form a self-adjoint subalgebra of \(C(S')\) that separates points (through \(\iota\)) and whose common zero set is \(\{0\}\). By the compact form of the [Stone–Weierstrass theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09), they are dense in \(\{f:f(0)=0\}\). Their images, the polynomials in \(x\) and \(x^*\) without constant term, are dense in \(C^*(x)\). The image of an isometry defined on a complete space is closed, so it is exactly \(C^*(x)\).
(3) By the Conventions, \(\widetilde A\cong A\oplus\mathbb C\) with \(x\mapsto(x,0)\), and \(S'=\sigma_A(x)\cup\{0\}\). The map \(f\mapsto\big((f|_{\sigma_A(x)})(x),\,f(0)\big)\) is a unital \(*\)-homomorphism \(C(S')\to A\oplus\mathbb C\) that sends \(\iota\) to \((x,0)\). By uniqueness it is the calculus of \((x,0)\). For \(f(0)=0\) its second coordinate is \(0\).
(4) By (2), \(\chi\circ(f\mapsto f(x))\) is a \(*\)-homomorphism from \(C_0(S'\setminus\{0\})\) to \(\mathbb C\). If it is zero, then \(\chi(x)=0\), and \(\chi(f(x))=0=f(0)=f(\chi(x))\). Otherwise it is a character, hence evaluation at a point \(s\) (Proposition 2.2(1)), and \(s=\chi(x)\). \(\square\)

**Corollary 5.4** (The calculus commutes with \(*\)-homomorphisms). Let \(\pi:A\to B\) be a \(*\)-homomorphism of C\*-algebras, and \(a\in A\) normal. Let \(\tilde\pi:\widetilde A\to\widetilde B\), \(\tilde\pi(x+\lambda)=\pi(x)+\lambda\), be its unital extension. In each statement, \(f(\pi(a))\) is the calculus of the restriction of \(f\) to the smaller spectrum.
1. \(\sigma'_B(\pi(a))\subseteq\sigma'_A(a)\).
2. \(\tilde\pi(f(a))=f(\pi(a))\) for every \(f\in C(\sigma'_A(a))\).
3. \(\pi(f(a))=f(\pi(a))\) for every \(f\in C(\sigma'_A(a))\) with \(f(0)=0\).
4. If \(A\) and \(B\) are unital and \(\pi(1)=1\), then \(\sigma_B(\pi(a))\subseteq\sigma_A(a)\), and \(\pi(f(a))=f(\pi(a))\) for every \(f\in C(\sigma_A(a))\).

**Proof.** (1) is part of (4.1). (4) The maps \(f\mapsto\pi(f(a))\) and \(f\mapsto f(\pi(a))\) are unital \(*\)-homomorphisms from \(C(\sigma_A(a))\) into \(B\). The first is a composition. The second is restriction to \(\sigma_B(\pi(a))\), which lies in \(\sigma_A(a)\) because unital homomorphisms map invertible elements to invertible elements, followed by the calculus of \(\pi(a)\). They agree at \(\iota\), hence on polynomials in \(\iota\) and \(\bar\iota\), which are dense ([density results](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-17)), and both are contractive by Theorem 4.2. (2) is (4) for the unital \(*\)-homomorphism \(\tilde\pi\) of C\*-algebras. (3) follows from (2) and Theorem 5.3(1): \(f(a)\in A\), and \(\tilde\pi=\pi\) on \(A\). \(\square\)

### 6. Continuity of the functional calculus

For a C\*-algebra \(A\) and a compact \(K\subseteq\mathbb C\), let \(A_K\) be the set of normal \(x\in A\) with \(\sigma'_A(x)\subseteq K\). For \(f\in C(K)\) and \(x\in A_K\), \(f(x)\) is the calculus of Theorem 5.3, computed in \(\widetilde A\); it lies in \(A\) when \(f(0)=0\). If \(A\) is unital, the same statements hold, with the same proofs, for the unital calculus on the set of normal \(x\) with \(\sigma_A(x)\subseteq K\).

**Theorem 6.1** (Continuity of the calculus).
1. (*Uniform continuity.*) For \(f\in C(K)\), the map \(x\mapsto f(x)\) is uniformly continuous on \(A_K\).
2. (*Joint continuity.*) For \(f,g\in C(K)\) and \(x,y\in A_K\), \[
\begin{gathered}
\|f(x)-g(y)\|\\
\leq\|f-g\|_K+\|g(x)-g(y)\|.
\end{gathered}
\]
3. (*Spectra move little.*) If \(x_0\in A\) is normal and \(y\in A\) is arbitrary, then every point of \(\sigma'_A(y)\) lies within \(\|y-x_0\|\) of \(\sigma'_A(x_0)\).
4. (*Open sets.*) Let \(U\subseteq\mathbb C\) be open and \(f\in C(U)\). Then \(x\mapsto f(x)\) is continuous on the set of normal \(x\) with \(\sigma'_A(x)\subseteq U\), which is relatively open in the set of normal elements.

**Proof.** In the unital calculus on \(A=\{0\}\), all conclusions have the immediate zero interpretation. Otherwise all the spectra in use are nonempty. (1) If \(K=\varnothing\), the domain \(A_K\) is empty, so the assertion is vacuous. Let \(M=\max_K|\lambda|\). If \(M=0\), every \(x\in A_K\) has norm zero by Theorem 1.3; the domain contains at most the element zero and the assertion is immediate. Now suppose \(M>0\), and let \(\varepsilon>0\). For \(x\in A_K\), \(\|x\|=r(x)\leq M\) by Theorem 1.3. Choose \(p(\lambda)=\sum_{j,k\leq n}c_{jk}\lambda^j\bar\lambda^k\) with \(\|f-p\|_K<\varepsilon/3\) ([density results](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-17)). For \(x\in A_K\), \(p(x)=\sum c_{jk}x^j(x^*)^k\) and \(\|f(x)-p(x)\|\leq\|f-p\|_K<\varepsilon/3\), by Theorem 5.1(2) and (4) in \(\widetilde A\). The constant term cancels. For \(j+k\geq1\) and \(\|x\|,\|y\|\leq M\), telescoping each factor gives \(\|x^j(x^*)^k-y^j(y^*)^k\|\leq(j+k)M^{j+k-1}\|x-y\|\). Thus \(\|p(x)-p(y)\|\leq L\|x-y\|\), where \(L=\sum_{j+k\geq1}|c_{jk}|(j+k)M^{j+k-1}\), and
\[
\begin{gathered}
\|f(x)-f(y)\|<\tfrac{2\varepsilon}3+L\|x-y\|<\varepsilon\\
\text{when }\|x-y\|<\varepsilon/(3\max(1,L)) .
\end{gathered}
\]
(2) \(\|f(x)-g(x)\|=\|(f-g)(x)\|\leq\|f-g\|_K\) by Theorem 5.1(4).
(3) Let \(d=\|y-x_0\|\) and let \(\lambda\) have distance \(\delta>d\) from \(\sigma'(x_0)\). In \(\widetilde A\), \(x_0-\lambda\) is normal and invertible, and its inverse is the calculus of \(t\mapsto(t-\lambda)^{-1}\), of norm \(1/\delta\) by Theorem 5.1(4). Then \(y-\lambda=(x_0-\lambda)\big(1+(x_0-\lambda)^{-1}(y-x_0)\big)\). The bracket is invertible by the [Neumann series](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-02), because \(\|(x_0-\lambda)^{-1}(y-x_0)\|\leq d/\delta<1\). So \(\lambda\notin\sigma'(y)\).
(4) Let \(x_0\) be normal with \(\sigma'(x_0)\subseteq U\). The compact set \(\sigma'(x_0)\) has a positive distance \(3\eta\) from the closed set \(\mathbb C\setminus U\) (take \(\eta=1\) if \(U=\mathbb C\)). The set \(K=\{\lambda:\operatorname{dist}(\lambda,\sigma'(x_0))\leq\eta\}\) is compact and lies in \(U\). By (3), every normal \(x\) with \(\|x-x_0\|<\eta\) lies in \(A_K\). Apply (1) to \(f|_K\). \(\square\)

The compact set \(K\) cannot be dropped from (1): for \(f(t)=t^2\) and self-adjoint \(h\), \(\|(h+\delta)^2-h^2\|=\|2\delta h+\delta^2\|\) is unbounded in \(h\). For the powers \(t^\alpha\) with \(0<\alpha\leq1\), Corollary 9.2 gives a modulus of continuity on all positive elements at once. Part (4) is the continuous analogue of the [continuity of the holomorphic calculus](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-13).

### 7. Absolute value, Jordan decomposition and unitaries

**Definition 7.1.** For \(h\in A_h\) put \(|h|=(h^2)^{1/2}\), \(h_+=\frac12(|h|+h)\) and \(h_-=\frac12(|h|-h)\). By the composition rule (Theorem 5.1(5)), these are the calculi of \(t\mapsto|t|\), \(t\mapsto\max(t,0)\) and \(t\mapsto\max(-t,0)\) at \(h\). They vanish at \(0\), so they lie in \(C^*(h)\subseteq A\) (Theorem 5.3). They are the *absolute value*, the *positive part* and the *negative part* of \(h\), and \(h=h_+-h_-\) is its *Jordan decomposition*.

**Proposition 7.2.** Let \(h\in A_h\).
1. \(h=h_+-h_-\), \(|h|=h_++h_-\), \(h_+h_-=h_-h_+=0\), and the quasi-spectra of \(h_+\), \(h_-\) and \(|h|\) lie in \([0,\infty)\). Also \(\|h_\pm\|\leq\|h\|=\||h|\|=\max(\|h_+\|,\|h_-\|)\).
2. (*Uniqueness.*) If \(h=a-b\) with \(a,b\in A_h\), \(\sigma'(a)\cup\sigma'(b)\subseteq[0,\infty)\) and \(ab=0\), then \(a=h_+\) and \(b=h_-\).

**Proof.** (1) These are identities between continuous functions on \(\sigma'(h)\subseteq\mathbb R\) (Proposition 1.5): \(t=t_+-t_-\), \(|t|=t_++t_-\), \(t_+t_-=0\), \(t_\pm\geq0\), \(t_\pm\leq|t|\), and \(\max|t|=\max(\max t_+,\max t_-)\). Apply Theorem 5.1(2)–(4) in \(\widetilde A\).
(2) From \(ab=0\) we get \(ba=(ab)^*=0\), so \(a\) and \(b\) commute, and \(D=C^*(a,b)\) is commutative. By Theorem 2.1, identify \(D\) with \(C_0(\Omega)\). The functions \(\hat a,\hat b\) are real, and their values lie in \(\sigma'_D(a)=\sigma'_A(a)\) and \(\sigma'_A(b)\): the values of a Gelfand transform lie in the quasi-spectrum ([the Gelfand representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-18)), and quasi-spectra do not depend on the C\*-subalgebra (Theorem 3.2(2)). So \(\hat a,\hat b\geq0\), and \(\hat a\hat b=0\). Hence \(\max(\hat h,0)=\hat a\) at every point. By Theorem 5.3(4), \(\widehat{h_+}=\max(\hat h,0)\). Since \(\mathcal G\) is injective, \(h_+=a\), and then \(h_-=h_+-h=b\). \(\square\)

Part (1) says in particular that every self-adjoint element is a difference of two elements with nonnegative quasi-spectrum, each of norm at most \(\|h\|\).

**Proposition 7.3** (Unitaries span a unital C\*-algebra). Let \(A\) be a C\*-algebra with identity.
1. If \(h\in A_h\) and \(\|h\|\leq1\), then \(u=h+i(1-h^2)^{1/2}\) is unitary and \(h=\frac12(u+u^*)\).
2. If \(\|x\|\leq1\), then \(x=\frac12(u_1+u_2)+\frac i2(u_3+u_4)\) with unitaries \(u_j\). Every \(x\) is a combination \(\sum_{j=1}^4c_ju_j\) of four unitaries with \(\sum_j|c_j|\leq2\|x\|\).
3. If \(A\) is not unital, every element of \(A\) is such a combination of unitaries of \(\widetilde A\).

**Proof.** (1) \(\sigma(h)\subseteq[-1,1]\) by Proposition 1.5(3). Let \(f(t)=t+i\sqrt{1-t^2}\) there. Then \(|f|=1\) and \(\operatorname{Re}f(t)=t\), so Theorem 5.1(2) gives \(u^*u=uu^*=|f|^2(h)=1\) and \(\frac12(u+u^*)=(\operatorname{Re}f)(h)=h\).
(2) Write \(x=x_1+ix_2\) with \(\|x_j\|\leq1\) (Proposition 1.2(1)). By (1), \(x_1=\frac12(u_1+u_1^*)\) and \(x_2=\frac12(u_3+u_3^*)\); take \(u_2=u_1^*\) and \(u_4=u_3^*\). For general \(x\neq0\), apply this to \(x/\|x\|\).
(3) Apply (2) in \(\widetilde A\). \(\square\)

**Exercise 7.4** (medium; Unitaries with a gap in the spectrum). In a C\*-algebra \(A\) with identity, let \(u\in U(A)\) with \(\sigma(u)\neq\mathbb T\). Prove that \(u=\exp(ih)\) for some \(h\in A_h\).

*Solution.* In the zero algebra take \(h=0\). Otherwise pick \(\theta_0\) with \(e^{i\theta_0}\notin\sigma(u)\). The map \(\theta\mapsto e^{i\theta}\) is a homeomorphism of \((\theta_0,\theta_0+2\pi)\) onto \(\mathbb T\setminus\{e^{i\theta_0}\}\); let \(g\) be its inverse, a real continuous function on the compact set \(\sigma(u)\subseteq\mathbb T\setminus\{e^{i\theta_0}\}\) (Proposition 1.5(2)). Put \(h=g(u)\), which is self-adjoint by Theorem 5.1(9). The power series \(\exp(ih)\) is the holomorphic calculus of \(e^{i\lambda}\) at \(h\) ([the exponential](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-14)), which equals the continuous calculus by Theorem 5.1(10). By the composition rule (Theorem 5.1(5)), \(\exp(ih)=(e^{ig})(u)=\iota(u)=u\), since \(e^{ig(\lambda)}=\lambda\) on \(\sigma(u)\).

**Exercise 7.5** (medium; Not every unitary is an exponential). In \(C(\mathbb T)\), the unitary \(u(\lambda)=\lambda\) is not \(\exp(ih)\) for any \(h\in C(\mathbb T)\), self-adjoint or not.

*Solution.* In \(C(\mathbb T)\), \(\exp(ih)\) is the function \(e^{ih}\), because evaluation at a point is a character and passes through the power series. So \(u=\exp(ih)\) would give \(\lambda=e^{ih(\lambda)}\) with \(h\) continuous. This is the case \(g=ih\) of the [example on the index group of \(C(\mathbb T)\)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-14), which shows that the identity function is not \(e^g\) for any \(g\in C(\mathbb T)\): the continuous function \(t\mapsto g(e^{it})-it\) on \([0,2\pi]\) takes values in \(2\pi i\mathbb Z\), so it is constant, but its values at \(0\) and \(2\pi\) differ by \(2\pi i\). So Exercise 7.4 cannot be extended to all unitaries.

**Exercise 7.6** (medium; Self-adjointness through the norm). In a nontrivial C\*-algebra \(A\) with identity, prove that \(x\in A\) is self-adjoint exactly when \(\lim_{t\to0}\frac1t(\|1+itx\|-1)=0\). (In the zero algebra \(\|1+itx\|=0\), so the quotient is \(-1/t\) and the statement fails.)

*Solution.* If \(x=h\) is self-adjoint, then \[
\begin{gathered}
\|1+ith\|^2\\
=\|(1-ith)(1+ith)\|\\
=\|1+t^2h^2\|\\
=1+t^2\|h\|^2
\end{gathered}
\] by Theorem 5.1(4), so \(0\leq\|1+ith\|-1\leq\frac12t^2\|h\|^2\), and the quotient tends to \(0\). Conversely, write \(x=h+ik\) with \(h,k\in A_h\) and \(k\neq0\). For real \(t\), the self-adjoint part of \(1+itx=(1-tk)+ith\) is \(1-tk\), and a self-adjoint part has norm at most that of the element (Proposition 1.2(1)). By Proposition 1.5(3) there is \(\mu\in\sigma(k)\) with \(|\mu|=\|k\|>0\), and \(\|1-tk\|\geq|1-t\mu|\), because \(1-t\mu\in\sigma(1-tk)\). For real \(t\) of sign opposite to \(\mu\), \(|1-t\mu|=1+|t|\|k\|\). Along such \(t\to0\), \(\big|\frac1t(\|1+itx\|-1)\big|\geq\|k\|\), so the limit is not \(0\).

### 8. The positive cone and the order

**Lemma 8.1.** Let \(h\in A_h\) and \(t\geq\|h\|\). Then \(\sigma'_A(h)\subseteq[0,\infty)\) if and only if \(\|t-h\|\leq t\), the norm taken in \(\widetilde A\).

**Proof.** \(\sigma'(h)\subseteq[-\|h\|,\|h\|]\subseteq[-t,t]\) by Proposition 1.5(3). The element \(t-h\) of \(\widetilde A\) is self-adjoint, and by Theorem 5.1(4), \[
\begin{gathered}
\|t-h\|\\
=\max_{\lambda\in\sigma'(h)}|t-\lambda|\\
=\max_{\lambda\in\sigma'(h)}(t-\lambda).
\end{gathered}
\] This is at most \(t\) exactly when every \(\lambda\in\sigma'(h)\) is \(\geq0\). \(\square\)

**Theorem 8.2** (The positive cone). For \(h\in A_h\) the following are equivalent:
- (i) \(\sigma'_A(h)\subseteq[0,\infty)\);
- (ii) \(h=y^*y\) for some \(y\in A\);
- (iii) \(h=k^2\) for some \(k\in A_h\).

These elements form a closed convex cone \(A_+\subseteq A_h\), and \(A_+\cap(-A_+)=\{0\}\).

**Proof.** *\(A_+\), defined by (i), is a closed convex cone.* It is closed under multiplication by \(c\geq0\), since \(\sigma'(ch)=c\sigma'(h)\). Let \(a,b\) satisfy (i), and put \(s=\|a\|\), \(t=\|b\|\). By the lemma, \[
\begin{gathered}
\|(s+t)-(a+b)\|\\
\leq\|s-a\|+\|t-b\|\\
\leq s+t,
\end{gathered}
\] and \(s+t\geq\|a+b\|\); so \(a+b\) satisfies (i). If \(h_n\to h\) with \(h_n\) satisfying (i), fix \(t\geq\sup_n\|h_n\|\). Then \(\|t-h_n\|\leq t\) for all \(n\), so \(\|t-h\|\leq t\) and \(t\geq\|h\|\), and \(h\) satisfies (i). If \(h\) and \(-h\) satisfy (i), then \(\sigma'(h)=\{0\}\) and \(\|h\|=r(h)=0\) by Theorem 1.3.
*(i) ⇒ (iii).* \(k=h^{1/2}\) lies in \(A_h\) by Theorem 5.3, since \(\sqrt t\) vanishes at \(0\).
*(iii) ⇒ (ii).* Take \(y=k\).
*(iii) ⇒ (i).* \(\sigma'(k^2)=\{\lambda^2:\lambda\in\sigma'(k)\}\subseteq[0,\infty)\), by spectral mapping (Theorem 5.1(3) in \(\widetilde A\)) and because \(\sigma'(k)\) is real (Proposition 1.5(3)).
*(ii) ⇒ (i).* Let \(h=y^*y\). By Proposition 7.2, \(h=u^2-v^2\) with \(u=h_+^{1/2}\), \(v=h_-^{1/2}\) in \(A_h\) and \(uv=vu=0\). Put \(w=yv\). Then
\[
w^*w=vy^*yv=v(u^2-v^2)v=-v^4 .
\]
Write \(w=k_1+ik_2\) with \(k_1,k_2\in A_h\). Then \(ww^*=-w^*w+2k_1^2+2k_2^2=v^4+2k_1^2+2k_2^2\), which lies in the convex cone \(A_+\) by (iii) ⇒ (i). Since \(\sigma'(w^*w)=\sigma'(ww^*)\) ([spectrum and quasi-spectrum](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-06)), also \(\sigma'(w^*w)\subseteq[0,\infty)\). So \(w^*w=-v^4\) lies in \(A_+\cap(-A_+)=\{0\}\). Hence \(v^4=0\), so \(v=0\) (because \(\|v\|^4=\|v^4\|\) by Theorem 1.3(1)), \(h_-=0\), and \(h=h_+\) satisfies (i). \(\square\)

**Definition 8.3.** An element of \(A_+\) is *positive*, written \(h\geq0\). For \(h,k\in A_h\), \(h\leq k\) means \(k-h\in A_+\); by the theorem this is a partial order on \(A_h\), compatible with sums and with multiplication by nonnegative scalars. The *absolute value* of \(x\in A\) is \(|x|=(x^*x)^{1/2}\). For \(h\in A_h\) it agrees with Definition 7.1, by the composition rule (Theorem 5.1(5)).

**Remark 8.4** (Where positivity is computed). Condition (i) uses the quasi-spectrum, which is the same in every C\*-subalgebra containing \(h\) and in \(\widetilde A\) (Theorem 3.2(2)). So \(A_+=A\cap\widetilde A_+\), and \(B_+=B\cap A_+\) for a C\*-subalgebra \(B\).

The next proposition collects the rules for working with the order; they are used constantly below. Inequalities involving scalars are read in \(\widetilde A\).

**Proposition 8.5** (Working with the order). Let \(A\) be a C\*-algebra.
1. For \(h\in A_h\) and \(t\in\mathbb R\), \(h\leq t\) in the forced unitization if and only if \(\sigma'(h)\subseteq(-\infty,t]\). If \(A\) is unital, comparison with its own identity instead gives \(h\leq t1_A\) if and only if \(\sigma_A(h)\subseteq(-\infty,t]\). In particular \(-\|h\|\leq h\leq\|h\|\). If \(b\geq0\) and \(-b\leq h\leq b\), then \(\|h\|\leq\|b\|\).
2. \(x^*x\leq\|x\|^2\) for \(x\in\widetilde A\).
3. If \(h\leq k\), then \(c^*hc\leq c^*kc\) for every \(c\in\widetilde A\).
4. If \(0\leq a\leq b\), then \(\|a\|\leq\|b\|\). For \(a\geq0\): \(a\leq1\) if and only if \(\|a\|\leq1\).
5. If \(a\geq0\), \(c\in\widetilde A\) and \(c^*ac=0\), then \(a^{1/2}c=0\) and \(ac=0\).
6. (*Support.*) If \(0\leq v\leq a\) and \(ab=0\) for some \(b\in\widetilde A\), then \(vb=0\).
7. Let \(A\) be unital and nontrivial, \(\varepsilon>0\), and \(\varepsilon1_A\leq a\leq b\). Then \(a,b\) are invertible in \(A\) and \(b^{-1}\leq a^{-1}\). In this item all scalar bounds and inverses use \(A\) and its own identity \(1_A\), not a second forced unitization.
8. Every \(h\in A_h\) is \(h_+-h_-\) with \(h_\pm\in A_+\) and \(\|h_\pm\|\leq\|h\|\). Every \(x\in A\) is a combination of four positive elements of norm at most \(\|x\|\).
9. If \(a,b\geq0\) commute, then \(ab\geq0\).
10. (*Positive square roots.*) Every \(a\in A_+\) has exactly one \(b\in A_+\) with \(b^2=a\), namely \(b=a^{1/2}\). It lies in \(C^*(a)\) and commutes with every element that commutes with \(a\). No unit and no invertibility are needed; for \(A=\{0\}\), \(b=0\).
11. (*Positivity in \(B(H)\).*) For \(a\in B(H)\), \(a\geq0\) if and only if \(\langle a\xi,\xi\rangle\geq0\) for every \(\xi\in H\); in that case \(a=a^*\) automatically. The same holds in every C\*-subalgebra of \(B(H)\).
12. A \(*\)-homomorphism \(\pi:A\to B\) of C\*-algebras maps \(A_+\) into \(B_+\). If \(\pi\) is injective and \(h\in A_h\) has \(\pi(h)\geq0\), then \(h\geq0\).

**Proof.** (1) \(\sigma_{\widetilde A}(t-h)=t-\sigma'(h)\). For the comparison inside a unital \(A\), use \(\sigma_A(t1_A-h)=t-\sigma_A(h)\) and Theorem 8.2: adjoining \(0\) to a spectrum does not change whether it is contained in \([0,\infty)\). The scalar norm bounds follow from Proposition 1.5(3). Finally, \(h\leq b\leq\|b\|\) and \(-h\leq\|b\|\) give \(\sigma'(h)\subseteq[-\|b\|,\|b\|]\), so \(\|h\|=r(h)\leq\|b\|\).
(2) \(\sigma'(x^*x)\subseteq[0,\|x^*x\|]=[0,\|x\|^2]\) by Theorem 8.2 and Proposition 1.5(3); apply (1).
(3) \(k-h=y^*y\), so \(c^*(k-h)c=(yc)^*(yc)\geq0\).
(4) \(a\leq b\leq\|b\|\) gives \(\sigma'(a)\subseteq[0,\|b\|]\), so \(\|a\|=r(a)\leq\|b\|\). The second claim is (1) with \(t=1\).
(5) \(\|a^{1/2}c\|^2=\|c^*ac\|=0\), and \(ac=a^{1/2}(a^{1/2}c)\).
(6) By (3), \(0\leq b^*vb\leq b^*ab=0\), so \(b^*vb=0\), because \(A_+\cap(-A_+)=\{0\}\) (Theorem 8.2). Then (5) gives \(vb=0\).
(7) \(\sigma(a)\subseteq[\varepsilon,\infty)\) by (1), so \(a\) is invertible, and likewise \(b\). Put \(c=a^{-1/2}ba^{-1/2}\). By (3), \(c\geq a^{-1/2}aa^{-1/2}=1\), so \(\sigma(c)\subseteq[1,\infty)\). The spectrum of an inverse consists of the inverses of the points of the spectrum ([spectrum and quasi-spectrum](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-06)), so \(\sigma(c^{-1})\subseteq(0,1]\). So \(c^{-1}=a^{1/2}b^{-1}a^{1/2}\leq1\), and conjugating by \(a^{-1/2}\) gives \(b^{-1}\leq a^{-1}\).
(8) This is Proposition 7.2(1) together with the Cartesian decomposition (Proposition 1.2(1)).
(9) \(C^*(a,b)\) is commutative. By Theorem 2.1 its elements are functions, and positivity there is pointwise nonnegativity; positivity in it agrees with positivity in \(A\) (Remark 8.4). The product of two nonnegative functions is nonnegative.
(10) Existence is Theorem 8.2, (i) ⇒ (iii). Uniqueness: let \(b\geq0\) with \(b^2=a\). Then \(b\) commutes with \(a\), and \(D=C^*(b)\) is commutative and contains \(a\) and \(a^{1/2}\in C^*(a)\). In \(D\cong C_0(\Omega)\), \(\hat b\geq0\) and \(\hat b^2=\hat a\), so \(\hat b=\sqrt{\hat a}=\widehat{a^{1/2}}\) by Theorem 5.3(4). Hence \(b=a^{1/2}\). The commutation claim is Theorem 5.1(6), since \(a=a^*\).
(11) If \(a=y^*y\), then \(\langle a\xi,\xi\rangle=\|y\xi\|^2\geq0\). Conversely, suppose \(\langle a\xi,\xi\rangle\geq0\) for all \(\xi\). For an inner product linear in the first variable, polarization reads \(4\langle T\xi,\eta\rangle=\sum_{k=0}^3i^k\langle T(\xi+i^k\eta),\xi+i^k\eta\rangle\). Since \(\langle a\zeta,\zeta\rangle=\langle\zeta,a\zeta\rangle=\langle a^*\zeta,\zeta\rangle\) for every \(\zeta\), polarization gives \(a=a^*\). Let \(\lambda<0\). Then \(\|(a-\lambda)\xi\|\|\xi\|\geq\langle(a-\lambda)\xi,\xi\rangle\geq|\lambda|\|\xi\|^2\). So \(a-\lambda\) is bounded below; it is injective with closed range, and the orthogonal complement of its range is the kernel of \((a-\lambda)^*=a-\lambda\), which is \(\{0\}\). So \(a-\lambda\) is invertible. Hence \(\sigma(a)\subseteq[0,\infty)\), since it is real (Proposition 1.5). For a C\*-subalgebra, use Remark 8.4.
(12) \(\pi(y^*y)=\pi(y)^*\pi(y)\). If \(\pi\) is injective, it is an isometric \(*\)-isomorphism onto the closed range \(\pi(A)\) (Corollary 4.6), so \(\sigma'_A(h)=\sigma'_{\pi(A)}(\pi(h))=\sigma'_B(\pi(h))\) by Theorem 3.2(2). \(\square\)

### 9. Operator monotone powers and a Hölder estimate

**Theorem 9.1** (Löwner–Heinz inequality). Let \(A\) be a C\*-algebra, \(0\leq b\leq a\) and \(0<\alpha\leq1\). Then \(b^\alpha\leq a^\alpha\).

Here \(t^\alpha\) vanishes at \(0\), so \(a^\alpha,b^\alpha\in A\). The statement also makes sense for \(\alpha=0\) when \(a\) and \(b\) are invertible, with \(a^0=b^0=1\).

**Proof.** We may work in \(\widetilde A\) (Theorem 5.3(3) and Remark 8.4), so let \(A\) be unital and nontrivial.
*Step 1: \(b\geq\varepsilon\) for some \(\varepsilon>0\).* Then \(a\geq b\geq\varepsilon\), and both are invertible (Proposition 8.5(7)). Let \(E=\{\alpha\in[0,1]:b^\alpha\leq a^\alpha\}\), with \(a^0=b^0=1\). It contains \(0\) and \(1\). It is closed: on a compact interval \([\varepsilon,M]\), \(t^\beta\to t^\alpha\) uniformly as \(\beta\to\alpha\), so \(\alpha\mapsto a^\alpha\) and \(\alpha\mapsto b^\alpha\) are norm continuous (Theorem 5.1(4)), and \(A_+\) is closed. Let \(\alpha,\beta\in E\) and \(\gamma=\frac12(\alpha+\beta)\). From \(b^\alpha\leq a^\alpha\) and Proposition 8.5(3), \(a^{-\alpha/2}b^\alpha a^{-\alpha/2}\leq1\), so by Proposition 8.5(4)
\[
\|b^{\alpha/2}a^{-\alpha/2}\|^2=\|a^{-\alpha/2}b^\alpha a^{-\alpha/2}\|\leq1,
\]
and likewise \(\|b^{\beta/2}a^{-\beta/2}\|\leq1\). Hence
\[
T=(b^{\beta/2}a^{-\beta/2})^*(b^{\alpha/2}a^{-\alpha/2})=a^{-\beta/2}b^\gamma a^{-\alpha/2}
\]
has \(\|T\|\leq1\). Put \(S=a^{-\gamma/2}b^\gamma a^{-\gamma/2}\) and \(c=a^{(\alpha-\beta)/4}\). Then \(T=cSc^{-1}\), because \(\frac{\alpha-\beta}4-\frac\gamma2=-\frac\beta2\) and \(-\frac\gamma2-\frac{\alpha-\beta}4=-\frac\alpha2\). Similar elements have the same spectrum, so \(r(S)=r(T)\leq1\). But \(S=(b^{\gamma/2}a^{-\gamma/2})^*(b^{\gamma/2}a^{-\gamma/2})\geq0\), so \(\|S\|=r(S)\leq1\), \(S\leq1\), and conjugating by \(a^{\gamma/2}\) gives \(b^\gamma\leq a^\gamma\). So \(E\) is closed under midpoints. It contains every dyadic rational of \([0,1]\), and being closed, all of \([0,1]\).
*Step 2: the general case.* For \(\varepsilon>0\), \(\varepsilon\leq b+\varepsilon\leq a+\varepsilon\), so \((b+\varepsilon)^\alpha\leq(a+\varepsilon)^\alpha\) by Step 1. For \(t\geq0\), \(0\leq(t+\varepsilon)^\alpha-t^\alpha\leq\varepsilon^\alpha\) (see the proof of Corollary 9.2), so \(\|(a+\varepsilon)^\alpha-a^\alpha\|\leq\varepsilon^\alpha\), and the same holds for \(b\). Let \(\varepsilon\to0\) and use that \(A_+\) is closed. \(\square\)

**Corollary 9.2** (A Hölder estimate). For all \(a,b\in A_+\) and \(0<\alpha\leq1\),
\[
\|a^\alpha-b^\alpha\|\leq\|a-b\|^\alpha .
\tag{9.1}
\]
In particular \(\|a^{1/2}-b^{1/2}\|\leq\|a-b\|^{1/2}\), and \(a\mapsto a^\alpha\) is uniformly continuous on the whole cone \(A_+\).

**Proof.** First, \((s+t)^\alpha\leq s^\alpha+t^\alpha\) for \(s,t\geq0\): if \(s+t>0\), then \(u^\alpha\geq u\) on \([0,1]\) gives \(\big(\frac s{s+t}\big)^\alpha+\big(\frac t{s+t}\big)^\alpha\geq1\). Put \(c=\|a-b\|\). Then \(a\leq b+c\) by Proposition 8.5(1), so by the theorem in \(\widetilde A\), \(a^\alpha\leq(b+c)^\alpha\leq b^\alpha+c^\alpha\); the second inequality is the scalar one applied through the calculus of \(b\). So \(a^\alpha-b^\alpha\leq c^\alpha\), and by symmetry \(b^\alpha-a^\alpha\leq c^\alpha\). Proposition 8.5(1) gives (9.1). \(\square\)

**Example 9.3** (No exponent greater than 1 is allowed). In \(M_2(\mathbb C)\) let \(a=\begin{pmatrix}2&1\\1&1\end{pmatrix}\) and \(b=\begin{pmatrix}1&0\\0&0\end{pmatrix}\). Then \(a-b=\begin{pmatrix}1&1\\1&1\end{pmatrix}\geq0\), so \(0\leq b\leq a\). But \(a^2-b^2=\begin{pmatrix}4&3\\3&2\end{pmatrix}\) has determinant \(-1\), so it is not positive.

The same obstruction occurs for every \(\alpha>1\). Set
\[
\begin{gathered}
t=(\alpha^2+1)^{1/(\alpha-1)}>1,\qquad
D=\begin{pmatrix}t&0\\0&1\end{pmatrix},\\
J=\begin{pmatrix}1&1\\1&1\end{pmatrix}\geq0 .
\end{gathered}
\]
We compute the first-order change of the power using only the two-dimensional spectral calculus. The eigenvalues of \(D+\varepsilon J\) are
\[
\lambda_\pm(\varepsilon)
=\frac{t+1+2\varepsilon
\ \pm\sqrt{(t-1)^2+4\varepsilon^2}}2 .
\]
At zero they are \(t,1\), respectively, and both have derivative \(1\). Its upper spectral projection is
\[
P_+(\varepsilon)
=\frac{D+\varepsilon J-\lambda_-(\varepsilon)1}
{\lambda_+(\varepsilon)-\lambda_-(\varepsilon)} .
\]
This formula follows by applying the scalar function that equals \(1\) at \(\lambda_+\) and \(0\) at \(\lambda_-\); thus \(P_-=1-P_+\). At zero the diagonal entries of \(P_+\) have derivative \(0\), and both off-diagonal entries have derivative \(1/(t-1)\). Differentiating
\((D+\varepsilon J)^\alpha=\lambda_+^\alpha P_++\lambda_-^\alpha P_-\)
therefore gives the norm limit
\[
\begin{gathered}
\frac{(D+\varepsilon J)^\alpha-D^\alpha}{\varepsilon}
\longrightarrow
L=\begin{pmatrix}\alpha t^{\alpha-1}&q\\q&\alpha\end{pmatrix},\\
q=\frac{t^\alpha-1}{t-1}.
\end{gathered}
\]
Since \(t>1\), \(t^\alpha-1\geq t^{\alpha-1}(t-1)\), so \(q\geq t^{\alpha-1}\). Consequently
\[
\det L
=\alpha^2t^{\alpha-1}-q^2
\leq t^{\alpha-1}(\alpha^2-t^{\alpha-1})<0 .
\]
The two eigenvalues of the self-adjoint matrix \(L\) have opposite signs. Choose a unit eigenvector for its negative eigenvalue. The displayed norm limit shows that the quadratic form of \((D+\varepsilon J)^\alpha-D^\alpha\) on that vector is negative for every sufficiently small positive \(\varepsilon\). Yet \(D\leq D+\varepsilon J\), and both matrices are positive. Thus \(s\mapsto s^\alpha\) fails to be operator monotone on \([0,\infty)\) for every \(\alpha>1\).

The Löwner–Heinz theorem for \(0<\alpha\leq1\), Theorem 9.1 above, proves the complementary range in full. Theorem 10.2 shows that in a C*-algebra where \(t^2\) is monotone, all elements commute.

The next proposition gives a second two-by-two argument, using an affine interpolant on the spectrum, and records the complete range for real exponents.

**Proposition 9.4** (The full range of monotone powers). On positive definite matrices of every size, \(x\mapsto x^\alpha\), for real \(\alpha\), preserves order exactly when \(0\leq\alpha\leq1\). For every \(\alpha>1\) there are already positive definite two-by-two matrices \(0<b\leq a\) for which \(b^\alpha\not\leq a^\alpha\). For \(0<\alpha\leq1\), the order-preserving statement holds on the entire positive cone of every C\*-algebra, including nonunital algebras, by Theorem 9.1. At \(\alpha=0\) on positive definite matrices the function is the constant identity.

**Proof.** The affirmative cases are Theorem 9.1 and the constant function. If \(\alpha<0\), the scalar inequality \(1<2\) gives \(1^\alpha>2^\alpha\), so even scalar monotonicity fails.

Fix \(\alpha>1\), and choose
\[
\begin{gathered}
s=(2\alpha^2)^{-1/(\alpha-1)},\\
b=\begin{pmatrix}s&0\\0&1\end{pmatrix},\qquad
h=\begin{pmatrix}1&1\\1&1\end{pmatrix},\\
a_t=b+th .
\end{gathered}
\]
Here \(0<s<1\), \(h\geq0\), and \(a_t\geq b>0\) for every \(t>0\). We calculate the first-order change of \(a_t^\alpha\) directly, rather than assuming a criterion for matrix monotonicity.

Put \(d=1-s>0\). The two distinct eigenvalues of \(a_t\) are
\[
\lambda_\pm(t)=\frac{1+s+2t\pm\sqrt{d^2+4t^2}}2 .
\]
Since
\[
0\leq\sqrt{d^2+4t^2}-d
=\frac{4t^2}{\sqrt{d^2+4t^2}+d}\leq\frac{2t^2}{d},
\]
we have \(\lambda_-(t)=s+t+O(t^2)\) and \(\lambda_+(t)=1+t+O(t^2)\). For sufficiently small \(t\), all these numbers stay in a fixed compact subinterval of \((0,\infty)\).

For \(f(u)=u^\alpha\), set
\[
c_t=\frac{f(\lambda_+(t))-f(\lambda_-(t))}
{\lambda_+(t)-\lambda_-(t)} .
\]
The affine polynomial \(f(\lambda_-)+c_t(u-\lambda_-)\) agrees with \(f\) on the two-point spectrum of \(a_t\). Functional calculus therefore gives
\[
f(a_t)=f(\lambda_-(t))I+
c_t\bigl(a_t-\lambda_-(t)I\bigr).
\]
This is precisely Theorem 5.1 applied to two functions with equal values on the spectrum. As \(t\to0\),
\[
c_t\longrightarrow c=\frac{1-s^\alpha}{1-s}>1.
\]
The upper-left entry is \(f(s)+t f'(s)+o(t)\): indeed \(s+t-\lambda_-(t)=O(t^2)\), \(c_t\) stays bounded, and \(f(\lambda_-(t))=f(s)+t f'(s)+o(t)\). Using the equivalent formula
\(f(a_t)=f(\lambda_+(t))I+c_t(a_t-\lambda_+(t)I)\)
gives the lower-right entry \(f(1)+t f'(1)+o(t)\). The off-diagonal entries are \(t c_t\). Thus, entrywise and hence in matrix norm,
\[
\frac{a_t^\alpha-b^\alpha}{t}
\longrightarrow
L=\begin{pmatrix}\alpha s^{\alpha-1}&c\\c&\alpha\end{pmatrix}.
\]
But
\[
\det L=\alpha^2s^{\alpha-1}-c^2
=\frac12-c^2<0.
\]
By continuity of the determinant, the self-adjoint matrix
\((a_t^\alpha-b^\alpha)/t\) has negative determinant for all sufficiently small positive \(t\). It cannot be positive: a positive two-by-two matrix has nonnegative eigenvalues and therefore nonnegative determinant, by Theorem 8.5(11) and the finite-dimensional spectral calculus. Consequently \(a_t^\alpha-b^\alpha\not\geq0\), although \(a_t\geq b>0\). This supplies a counterexample for each \(\alpha>1\), and completes the classification. \(\square\)

The matrices of divided differences that appear here are studied more generally in [Hiai and Sano's freely accessible paper](https://arxiv.org/html/1007.2478v2). Its Proposition 3.1 treats power functions; the argument above proves the monotonicity range within this programme and does not require the paper's external prerequisites.

*Original text: CC0.*

### 10. Order properties that force commutativity

In an abelian C\*-algebra the self-adjoint part behaves like a space of real functions: it is a lattice, and the order is compatible with products and squares. This section shows that each of these properties, and several related ones, forces the algebra to be abelian. The proofs use only the functional calculus and the order.

**Definition 10.1.** \(A_h\) is a *lattice* if every pair \(h,k\in A_h\) has a least upper bound \(h\vee k\) for \(\leq\); then \(h\wedge k=-((-h)\vee(-k))\) is a greatest lower bound. \(A_h\) has the *Riesz decomposition property* (RDP) if \(0\leq x\leq y_1+y_2\) with \(y_1,y_2\geq0\) implies \(x=x_1+x_2\) with \(0\leq x_j\leq y_j\). It has the *interpolation property* (RIP) if, whenever \(u_1,u_2\leq v_1,v_2\), some \(w\) has \(u_1,u_2\leq w\leq v_1,v_2\).

**Theorem 10.2** (Order and commutativity). For a C\*-algebra \(A\), the following are equivalent:
- (a) \(A\) is abelian;
- (b) \(A_h\) is a lattice;
- (c) \(A_h\) has the RDP;
- (c′) \(A_h\) has the RIP;
- (d) \(0\leq b\leq a\) implies \(b^2\leq a^2\);
- (e) \(ab+ba\geq0\) for all \(a,b\in A_+\);
- (f) \(azb=0\) whenever \(a,b\in A_+\), \(ab=0\) and \(z\in A\).

If \(A\) is abelian, the real space \(A^*_h\) of bounded hermitian functionals, ordered by \(\varphi\leq\psi\) when \(\psi-\varphi\) is positive, is a lattice.

The proof uses three lemmas.

**Lemma 10.3** (Orthogonal sums). Let \(p_1,\dots,p_n\) and \(q_1,\dots,q_n\) be positive elements of \(\widetilde A\) of norm at most \(1\), with \(p_kp_l=0\) and \(q_kq_l=0\) for \(k\neq l\). Then \(\|\sum_kp_kyq_k\|\leq\|y\|\) for every \(y\in\widetilde A\).

**Proof.** Put \(T=\sum_kp_kyq_k\). Since \(p_kp_l=0\) for \(k\neq l\), \(T^*T=\sum_kq_ky^*p_k^2yq_k\). Since \(\|p_k\|\leq1\), \(p_k^2\leq1\) (Proposition 8.5(1)). Conjugation preserves the order (Proposition 8.5(3)), and \(y^*y\leq\|y\|^2\) (Proposition 8.5(2)); so \(y^*p_k^2y\leq y^*y\leq\|y\|^2\), and \(q_ky^*p_k^2yq_k\leq\|y\|^2q_k^2\). So \(0\leq T^*T\leq\|y\|^2Q\) with \(Q=\sum_kq_k^2\). The \(q_k^2\) are positive and \(q_k^2q_l^2=0\) for \(k\neq l\), so \(Q^m=\sum_kq_k^{2m}\). By Theorem 1.3(1), \(\|Q\|^m=\|Q^m\|\leq n\) for every power \(m\) of \(2\), and letting \(m\to\infty\) gives \(\|Q\|\leq1\). By Proposition 8.5(4), \(\|T\|^2=\|T^*T\|\leq\|y\|^2\). \(\square\)

**Lemma 10.4** ((f) implies (a)). Assume (f).
1. If \(a\in A_+\), \(c\in\widetilde A\) and \(ca=0\), then \(azc=0\) for all \(z\in A\). If \(ac=0\), then \(cza=0\) for all \(z\in A\).
2. Every \(x\in A_+\) commutes with every \(y\in A\). Hence \(A\) is abelian.

**Proof.** (1) Let \(ca=0\) and \(z\in A\). Then \(ca^{1/2}=0\), since \(\|ca^{1/2}\|^2=\|cac^*\|=0\); so \(a^{1/2}c^*=0\). Put \(Y=a^{1/2}zc\in A\). The positive elements \(a^{1/2}\) and \(Y^*Y=c^*z^*azc\) satisfy \(a^{1/2}Y^*Y=0\). By (f), applied to them and to \(zc\in A\), \(a^{1/2}(zc)Y^*Y=YY^*Y=0\). Then \((Y^*Y)^2=Y^*(YY^*Y)=0\), so \(Y^*Y=0\) by Theorem 1.3(1), and \(Y=0\). Hence \(azc=a^{1/2}Y=0\). If \(ac=0\), apply this to \(c^*\) (note \(c^*a=(ac)^*=0\)) and take adjoints.
(2) Let \(x\in A_+\), \(x\neq0\), \(y\in A\) and \(\delta>0\). Let \(N\) be an integer with \(N\delta\geq\|x\|\), and for \(j=0,\dots,N\) let \(\phi_j(t)=\max(0,1-|t-j\delta|/\delta)\) on \([0,N\delta]\). On \([0,N\delta]\), \(\sum_j\phi_j=1\) and \(\sum_jj\delta\,\phi_j(t)=t\), because both sides are linear between consecutive nodes \(j\delta\) and agree there. Also \(0\leq\phi_j\leq1\), \(\phi_j\phi_k=0\) when \(|j-k|\geq2\), and \(\phi_j(0)=0\) for \(j\geq1\). Put \(e_j=\phi_j(x)\in\widetilde A\), so \(e_j\in A_+\) for \(j\geq1\), \(\sum_je_j=1\) and \(\sum_jj\delta e_j=x\). For \(|j-k|\geq2\), \(e_jye_k=0\): if \(j,k\geq1\) this is (f); if \(j=0\) it is (1) with \(a=e_k\), \(c=e_0\) and \(e_ke_0=0\); if \(k=0\) it is (1) with \(a=e_j\), \(c=e_0\) and \(e_0e_j=0\). Therefore
\[
\begin{gathered}
xy-yx\\
=\sum_{j,k}(j-k)\delta\,e_jye_k\\
=\delta\sum_j\big(e_{j+1}ye_j-e_jye_{j+1}\big).
\end{gathered}
\]
Split each of the two sums into the terms with \(j\) even and those with \(j\) odd. In each of the four parts, the left factors are pairwise orthogonal and so are the right factors, since their indices differ by at least \(2\). Lemma 10.3 bounds each part by \(\|y\|\). So \(\|xy-yx\|\leq4\delta\|y\|\) for every \(\delta>0\), and \(xy=yx\). Since \(A\) is spanned by \(A_+\) (Proposition 8.5(8)), \(A\) is abelian. \(\square\)

**Lemma 10.5** ((c′) implies (f)). Assume (c′). Let \(p,q\in A_+\) with \(pq=0\), and \(z\in A\). Then \(p^2zq^2=0\).

**Proof.** Put \(W=pzq+qz^*p\in A_h\). *Positivity test:* if \(\alpha,\beta>0\) and \(\alpha\beta\geq\|z\|^2\), then \(\alpha p^2+\beta q^2+W\geq0\). Indeed, with \(v=\alpha^{1/2}p+\alpha^{-1/2}zq\),
\[
\begin{gathered}
v^*v\\
=\alpha p^2+W+\alpha^{-1}qz^*zq\\
\leq\alpha p^2+W+\alpha^{-1}\|z\|^2q^2\\
\leq\alpha p^2+W+\beta q^2,
\end{gathered}
\]
using Proposition 8.5(2)–(3).
Fix \(s>0\) and choose \(\lambda>0\) with \(s(s+2\lambda)\geq\|z\|^2\). Put \(u=\lambda(p^2-q^2)\). Since \(p^2q^2=q^2p^2=0\), \(u^2=(\lambda(p^2+q^2))^2\), so \(|u|=\lambda(p^2+q^2)\) by the uniqueness of positive square roots (Proposition 8.5(10)), and \(u_+=\lambda p^2\), \(u_-=\lambda q^2\) by the uniqueness of the Jordan decomposition (Proposition 7.2(2)). Put \(n=s(p^2+q^2)+W\) and \(m=|u|+n\). By the positivity test,
\[
\begin{gathered}
m-u\\
=sp^2+(s+2\lambda)q^2+W\\
\geq0,\\
m+u\\
=(s+2\lambda)p^2+sq^2+W\\
\geq0 .
\end{gathered}
\]
So \(u,-u\leq m\), and also \(u,-u\leq|u|\). By (c′) there is \(w\) with \(u,-u\leq w\leq m,|u|\). Put \(e=|u|-w\geq0\). From \(w\geq-u\), \(e\leq|u|+u=2\lambda p^2\); from \(w\geq u\), \(e\leq2\lambda q^2\). The first bound and \(p^2q^2=0\) give \(eq^2=0\) (Proposition 8.5(6)). The second, conjugated by \(e\), gives \(0\leq e^3\leq2\lambda eq^2e=0\). So \(e^3=0\), \(e=0\), \(w=|u|\), and \(n=m-w\geq0\).
For \(n\geq0\) and \(c,d\in A\), \[
\begin{gathered}
\|cnd\|\\
\leq\|n^{1/2}c^*\|\|n^{1/2}d\|\\
=\|cnc^*\|^{1/2}\|d^*nd\|^{1/2}.
\end{gathered}
\] Here \(pnp=sp^4\), \(qnq=sq^4\) and \(pnq=p^2zq^2\), because \(pq=qp=0\). So \(\|p^2zq^2\|\leq s\|p\|^2\|q\|^2\). As \(s>0\) was arbitrary, \(p^2zq^2=0\). \(\square\)

**Proof of Theorem 10.2.** (a) ⇒ (b): by Theorem 2.1, \(A=C_0(\Omega)\), where positivity is pointwise nonnegativity, because the quasi-spectrum of \(f\) is \(f(\Omega)\cup\{0\}\) ([the Gelfand representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-18)). The pointwise maximum \(\max(h,k)\) lies in \(C_0(\Omega;\mathbb R)\) and is the least upper bound.
(b) ⇒ (c′): \(w=u_1\vee u_2\) works.
(c′) ⇒ (c): let \(0\leq x\leq y_1+y_2\) with \(y_j\geq0\). Then \(0,\,x-y_2\leq x,\,y_1\). An interpolant \(w\) gives \(x_1=w\) and \(x_2=x-w\), with \(0\leq x_1\leq y_1\) and \(0\leq x_2\leq y_2\).
(c) ⇒ (c′): let \(u_1,u_2\leq v_1,v_2\). Then \(0\leq v_1-u_1\leq(v_1-u_2)+(v_2-u_1)\), because the difference is \(v_2-u_2\geq0\). The RDP gives \(v_1-u_1=a_1+a_2\) with \(0\leq a_1\leq v_1-u_2\) and \(0\leq a_2\leq v_2-u_1\). Then \(w=u_1+a_2=v_1-a_1\) satisfies \(u_1\leq w\), \(w\leq v_1\), \(u_2=v_1-(v_1-u_2)\leq w\) and \(w\leq u_1+(v_2-u_1)=v_2\).
(c′) ⇒ (f): let \(a,b\in A_+\) with \(ab=0\). Then \(ba=0\), \(C^*(a,b)\) is commutative, and there \(\widehat{a^{1/2}}\widehat{b^{1/2}}=\sqrt{\hat a\hat b}=0\) (Theorem 5.3(4)); so \(p=a^{1/2}\) and \(q=b^{1/2}\) satisfy \(pq=0\). Lemma 10.5 gives \(azb=p^2zq^2=0\).
(f) ⇒ (a): Lemma 10.4.
(a) ⇒ (d), (e): in \(C_0(\Omega)\), \(0\leq g\leq f\) gives \(g^2\leq f^2\) pointwise, and \(ab+ba=2ab\geq0\).
(d) ⇒ (e): let \(a,b\geq0\) and \(t>0\). Then \(a\leq a+tb\), so \(a^2\leq(a+tb)^2=a^2+t(ab+ba)+t^2b^2\), that is \(ab+ba+tb^2\geq0\). Let \(t\to0\).
(e) ⇒ (f): let \(a,b\in A_+\) with \(ab=0\), and \(y\in A_+\). Then \(w=ay+ya\geq0\) and \(bwb=bayb+byab=0\). By Proposition 8.5(5), \(wb=0\), that is \(ayb=-yab=0\). Since \(A\) is spanned by \(A_+\), \(azb=0\) for every \(z\in A\).

*The dual lattice.* A bounded linear functional \(\varphi\) is *hermitian* if \(\varphi(x^*)=\overline{\varphi(x)}\), and *positive* if \(\varphi(A_+)\subseteq[0,\infty)\). Let \(A\) be abelian and \(\varphi,\psi\in A^*_h\). For \(x\in A_+\) put
\[
S(x)=\sup\{\varphi(y)+\psi(x-y):\ 0\leq y\leq x\}.
\]
Since \(0\leq y\leq x\) implies \(\|y\|,\|x-y\|\leq\|x\|\) (Proposition 8.5(4)), \(-\|\psi\|\|x\|\leq\psi(x)\leq S(x)\leq(\|\varphi\|+\|\psi\|)\|x\|\). \(S\) is positively homogeneous. It is additive on \(A_+\). If \(0\leq y_j\leq x_j\), then \(y_1+y_2\) is admissible for \(x_1+x_2\), so \(S(x_1+x_2)\geq S(x_1)+S(x_2)\). Conversely, if \(0\leq y\leq x_1+x_2\), the RDP, which holds by (a) ⇒ (c), splits \(y=y_1+y_2\) with \(0\leq y_j\leq x_j\), and \(\varphi(y)+\psi(x_1+x_2-y)\) is the sum of the two admissible values for \(x_1\) and \(x_2\). So \(S(u-v)=S(u)-S(v)\) is a well-defined real-linear functional on \(A_h=A_+-A_+\), bounded by \(2(\|\varphi\|+\|\psi\|)\|h\|\) at \(h=h_+-h_-\). Its complexification \(S(x_1+ix_2)=S(x_1)+iS(x_2)\) is a bounded hermitian functional. Taking \(y=x\) and \(y=0\) shows \(S\geq\varphi\) and \(S\geq\psi\). If \(\theta\in A^*_h\) and \(\theta\geq\varphi,\psi\), then \(\varphi(y)+\psi(x-y)\leq\theta(y)+\theta(x-y)=\theta(x)\), so \(S\leq\theta\). Thus \(S=\varphi\vee\psi\). \(\square\)

*The converse.* If \(A^*_h\) is a lattice, then \(A\) is abelian. By the Hahn–Banach theorem, the lattice property of \(A^*_h\) yields the interpolation property of \(A_h\) up to an arbitrarily small error, and the proof of Lemma 10.5 survives such an error.

*Step 1: approximate interpolation.* Let \(A^*_h\) be a lattice. The steps (b) ⇒ (c′) ⇒ (c) of the proof of Theorem 10.2 use only the order, so they show that \(A^*_h\) has the RDP. Let \(u_1,u_2\leq v_1,v_2\) in \(A_h\), and \(\varepsilon>0\). We show that some \(w\in A_h\) satisfies \(u_i-\varepsilon\leq w\leq v_j+\varepsilon\) for \(i,j=1,2\). In the real Banach space \((A_h)^4\), normed by the largest of the four norms, let \(P=(A_+)^4\), a convex cone, and let \(K\) be the set of the points \((w-u_1,\,w-u_2,\,v_1-w,\,v_2-w)\) with \(w\in A_h\). A self-adjoint element of norm less than \(\varepsilon\) is \(\geq-\varepsilon\) (Proposition 8.5(1)). So if the point of \(K\) given by \(w\) is at distance less than \(\varepsilon\) from some point of \(P\), then this \(w\) works. Suppose that no point of \(K\) is. Then the open convex set \(U\) of the points at distance less than \(\varepsilon\) from some point of \(K\) does not meet \(P\). By the separation theorem for an open convex set (Theorem 6.2 of [Hahn–Banach, Baire and the basic theorems on Banach spaces](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html), over the real numbers), there are bounded real-linear functionals \(\varphi_1,\dots,\varphi_4\) on \(A_h\) and a real \(\gamma\) with \(\sum_l\varphi_l(x_l)<\gamma\leq\sum_l\varphi_l(y_l)\) for all \(x\in U\) and \(y\in P\). Since \(P\) is a cone containing \(0\), each \(\varphi_l\) is nonnegative on \(A_+\), and \(\gamma\leq0\). At the point of \(K\) given by \(w\), the sum is
\[
\begin{gathered}
(\varphi_1+\varphi_2-\varphi_3-\varphi_4)(w)\\
+\varphi_3(v_1)+\varphi_4(v_2)\\
-\varphi_1(u_1)-\varphi_2(u_2),
\end{gathered}
\]
and it is negative for every \(w\in A_h\). A nonzero real-linear functional takes arbitrarily large values, so \(\varphi_1+\varphi_2=\varphi_3+\varphi_4\), and \(\varphi_3(v_1)+\varphi_4(v_2)<\varphi_1(u_1)+\varphi_2(u_2)\). Extended by \(\varphi_l(x+iy)=\varphi_l(x)+i\varphi_l(y)\) for \(x,y\in A_h\), the \(\varphi_l\) are positive functionals. As \(0\leq\varphi_1\leq\varphi_3+\varphi_4\), the RDP gives \(\varphi_1=\psi_{13}+\psi_{14}\) with \(0\leq\psi_{13}\leq\varphi_3\) and \(0\leq\psi_{14}\leq\varphi_4\). Then \(\psi_{23}=\varphi_3-\psi_{13}\) and \(\psi_{24}=\varphi_4-\psi_{14}\) are positive, and their sum is \(\varphi_2\). Since each \(u_i\) lies below \(v_1\) and \(v_2\),
\[
\begin{gathered}
\varphi_1(u_1)+\varphi_2(u_2)\\
=\sum_{i=1,2}\big(\psi_{i3}(u_i)+\psi_{i4}(u_i)\big)\\
\leq\sum_{i=1,2}\big(\psi_{i3}(v_1)+\psi_{i4}(v_2)\big)\\
=\varphi_3(v_1)+\varphi_4(v_2),
\end{gathered}
\]
a contradiction.

*Step 2: Lemma 10.5 with an error.* Let \(p,q\in A_+\) with \(pq=0\), and \(z\in A\). Take \(s\), \(\lambda\), \(u\), \(n\) and \(m\) as in the proof of Lemma 10.5, so that \(u,-u\leq m,|u|\), \(pnp=sp^4\), \(qnq=sq^4\) and \(pnq=p^2zq^2\). Let \(\varepsilon>0\). Step 1 gives \(w\in A_h\) with \(u-\varepsilon,\,-u-\varepsilon\leq w\leq m+\varepsilon,\,|u|+\varepsilon\). Put \(e=|u|+\varepsilon-w\geq0\). Then \(n+e=m+\varepsilon-w\geq0\). Also \(e\leq|u|+u+2\varepsilon=2\lambda p^2+2\varepsilon\) and \(e\leq|u|-u+2\varepsilon=2\lambda q^2+2\varepsilon\). Conjugating (Proposition 8.5(3)) and using \(pq=qp=0\) gives \(qeq\leq2\varepsilon q^2\) and \(pep\leq2\varepsilon p^2\). The norm inequality at the end of the proof of Lemma 10.5, applied to \(n+e\) and to \(e\), and Proposition 8.5(4) give
\[
\begin{gathered}
\|p^2zq^2\|\\
\leq\|p(n+e)q\|+\|peq\|\\
\leq\big(s\|p\|^4+2\varepsilon\|p\|^2\big)^{1/2}\big(s\|q\|^4+2\varepsilon\|q\|^2\big)^{1/2}\\
+2\varepsilon\|p\|\|q\|.
\end{gathered}
\]
Letting \(\varepsilon\to0\) and then \(s\to0\) gives \(p^2zq^2=0\). As in the step (c′) ⇒ (f), this gives (f), and Lemma 10.4 shows that \(A\) is abelian. \(\square\)

**Example 10.6** (\(2\times2\) matrices violate every condition of Theorem 10.2). In \(M_2(\mathbb C)\):
- (f) fails: \(E_{11}E_{22}=0\), but \(E_{11}E_{12}E_{22}=E_{12}\neq0\).
- (e) fails: for \(p=E_{11}\) and \(q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\), \(pq+qp=\frac12\begin{pmatrix}2&1\\1&0\end{pmatrix}\), whose determinant is \(-\frac14\).
- (d) fails: see Example 9.3.
- (c) fails: \(q\leq E_{11}+E_{22}=1\), but if \(q=q_1+q_2\) with \(0\leq q_1\leq E_{11}\) and \(0\leq q_2\leq E_{22}\), then \(q_1E_{22}=0\) and \(q_2E_{11}=0\) by Proposition 8.5(6), so \(q_1\) and \(q_2\) are diagonal, and so is \(q\), which it is not.

**Exercise 10.7** (medium; The positive part is not monotone). In \(M_2(\mathbb C)\), find self-adjoint \(h\leq k\) with \(h_+\not\leq k_+\). Explain why this cannot happen in an abelian C\*-algebra.

*Solution.* Take \(h=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\) and \(k=h+\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}2&1\\1&0\end{pmatrix}\), so \(h\leq k\). Here \(h_+=E_{11}\). The eigenvalues of \(k\) are \(1\pm\sqrt2\), so \(k_+=(1+\sqrt2)P\), where \(P\) is the projection onto the line spanned by \(v=(1,\sqrt2-1)\). If \(E_{11}\leq k_+\), then for a unit vector \(w\perp v\), \(|\langle w,e_1\rangle|^2=\langle E_{11}w,w\rangle\leq\langle k_+w,w\rangle=0\), so \(e_1\perp w\) and \(e_1\) would be a multiple of \(v\), which it is not. In an abelian algebra, \(h_+=\max(h,0)\) pointwise, which is monotone. More generally, if \(A_h\) is a lattice, then \(h\vee0=h_+\). Indeed, put \(c=h\vee0\). Since \(h_+\) is an upper bound of \(h\) and \(0\), we have \(0\leq c\leq h_+\) and \(0\leq c-h\leq h_+-h=h_-\). By Proposition 8.5(6), \(ch_-=0\) and \((c-h)h_+=0\), so \(ch_+=hh_+=h_+^2\). Then \(e=h_+-c\) satisfies \(0\leq e\leq h_+\) and \(eh_+=0\), so \(0\leq e^3\leq eh_+e=0\), and \(e=0\). In a lattice \(h\mapsto h\vee0\) is monotone, so the example is one more witness that \(M_2(\mathbb C)_h\) is not a lattice.

## B. Localize, form a quotient, and lift back

**Running computation.** In \(A=C_0((0,1])\), let \(h(t)=t\) and \(e_\varepsilon(t)=t/(t+\varepsilon)\). Each \(e_\varepsilon\) belongs to \(A\) and is a positive contraction. For \(f\in A\) and \(\delta>0\), choose \(s>0\) so that \(|f(t)|<\delta\) for \(0<t<s\). On that interval \(|(1-e_\varepsilon)f|<\delta\); on \([s,1]\) it is at most \(\varepsilon\|f\|/(s+\varepsilon)\). Thus \(e_\varepsilon f\to f\) uniformly as \(\varepsilon\downarrow0\). The cutoff estimates below abstract this calculation. They also work for one-sided ideals without requiring those ideals to be closed.

Once local units exist, the quotient norm can be computed by removing the part supported in a closed two-sided ideal. This gives the C*-identity on the quotient rather than assuming it. The commutative hull-and-kernel theorem identifies the geometry of this operation. We then return to general quotients to lift norm bounds, positivity and order intervals. These three questions belong together: what is forgotten, what norm survives, and which constrained representatives can be recovered?

### 11. Approximate identities

Adjoining an identity is not always enough: the unitization of an ideal is no longer an ideal, so statements about ideals cannot be reduced to the unital case. Approximate identities replace the identity in such cases.

**Definition 11.1.** Let \(A\) be a Banach algebra and \(J\subseteq A\). A net \((u_i)\) in \(A\) is a *right approximate identity for \(J\)* if \(\|xu_i-x\|\to0\) for every \(x\in J\), a *left* one if \(\|u_ix-x\|\to0\), and an *approximate identity for \(J\)* if both hold; for \(J=A\) we say "of \(A\)". It is *bounded* if \(\sup_i\|u_i\|<\infty\). In a C\*-algebra one often also asks that \(0\leq u_i\leq u_j\) for \(i\leq j\) and \(\|u_i\|\leq1\); we call such a net *increasing and contractive*.

For \(h\in A_+\), the *closed right ideal generated by \(h\)* is the smallest closed right ideal of \(A\) containing \(h\), the closure of \(hA+\mathbb Ch\); similarly on the left. For \(\varepsilon>0\) and \(t\geq0\) put \(f_\varepsilon(t)=t/(t+\varepsilon)\).

**Lemma 11.2.** Let \(A\) be a C\*-algebra and \(\varepsilon>0\).
1. If \(0\leq h\leq k\), then \(f_\varepsilon(h)\leq f_\varepsilon(k)\).
2. Let \(h\in A_+\). Then \(f_\varepsilon(h)\in A_+\), \(\|f_\varepsilon(h)\|<1\), and \(f_\varepsilon(h)\) increases as \(\varepsilon\) decreases. For every \(x\) in the closed right ideal generated by \(h\), \(\|f_\varepsilon(h)x-x\|\to0\) as \(\varepsilon\to0\). For every \(x\) in the closed left ideal generated by \(h\), \(\|xf_\varepsilon(h)-x\|\to0\). For \(x=hy+\mu h\) with \(y\in A\), \(\|f_\varepsilon(h)x-x\|\leq\varepsilon(\|y\|+|\mu|)\).

**Proof.** (1) \(\varepsilon\leq h+\varepsilon\leq k+\varepsilon\), so \((k+\varepsilon)^{-1}\leq(h+\varepsilon)^{-1}\) by Proposition 8.5(7). Since \(f_\varepsilon(t)=1-\varepsilon(t+\varepsilon)^{-1}\),
\[
\begin{gathered}
f_\varepsilon(h)\\
=1-\varepsilon(h+\varepsilon)^{-1}\\
\leq1-\varepsilon(k+\varepsilon)^{-1}\\
=f_\varepsilon(k).
\end{gathered}
\]
(2) \(f_\varepsilon\) vanishes at \(0\) and takes values in \([0,1)\), so \(f_\varepsilon(h)\in A_+\) and \(\|f_\varepsilon(h)\|=\|h\|/(\|h\|+\varepsilon)<1\) (Theorem 5.3 and Theorem 5.1(4)). For \(\varepsilon'<\varepsilon\), \(f_{\varepsilon'}\geq f_\varepsilon\) on \([0,\infty)\), so \(f_{\varepsilon'}(h)\geq f_\varepsilon(h)\). Next, \((1-f_\varepsilon(t))t=\varepsilon f_\varepsilon(t)\), so \(\|(1-f_\varepsilon(h))h\|\leq\varepsilon\), which gives the bound for \(x=hy+\mu h\). Let \(\mathfrak m\) be the set of \(x\in\widetilde A\) with \(\|f_\varepsilon(h)x-x\|\to0\). It is a right ideal of \(\widetilde A\), it contains \(h\), and it is closed: if \(x_n\to x\) with \(x_n\in\mathfrak m\), then \(\|f_\varepsilon(h)x-x\|\leq2\|x-x_n\|+\|f_\varepsilon(h)x_n-x_n\|\), because \(\|f_\varepsilon(h)\|\leq1\). So every element of the closed right ideal of \(A\) generated by \(h\) lies in \(\mathfrak m\). The left statement follows by taking adjoints. \(\square\)

**Corollary 11.3** (The closed one-sided ideal generated by a positive element). Let \(h\in A_+\) and let \(\mathfrak m\) be the closed right ideal generated by \(h\).
1. \(x\in\mathfrak m\) if and only if \(\|f_\varepsilon(h)x-x\|\to0\).
2. If \(xx^*\leq\lambda h\) for some \(\lambda>0\), then \(x\in\mathfrak m\), and \(\|x-f_\varepsilon(h)x\|\leq\frac12(\lambda\varepsilon)^{1/2}\).
3. \(\mathfrak m\) is the closure of \(hA\), and it is also the closed right ideal generated by \(h^\alpha\), for every \(\alpha>0\).

The mirror statements hold for left ideals, with \(x^*x\leq\lambda h\) in (2).

**Proof.** (1) One direction is the Lemma. Conversely, \(f_\varepsilon(h)x=h\big((h+\varepsilon)^{-1}x\big)\in hA\), because \(A\) is an ideal of \(\widetilde A\). So a limit of such elements lies in the closure of \(hA\), which is inside \(\mathfrak m\).
(2) By Proposition 8.5(3)–(4),
\[
\begin{gathered}
\|(1-f_\varepsilon(h))x\|^2\\
=\|(1-f_\varepsilon(h))xx^*(1-f_\varepsilon(h))\|\\
\leq\lambda\|(1-f_\varepsilon(h))h(1-f_\varepsilon(h))\|\\
=\lambda\max_{t\in\sigma'(h)}\frac{\varepsilon^2t}{(t+\varepsilon)^2}\\
\leq\frac{\lambda\varepsilon}4 ,
\end{gathered}
\]
since \(4\varepsilon t\leq(t+\varepsilon)^2\). Now apply (1).
(3) \(f_\varepsilon(h)h\in hA\) and \(\|h-f_\varepsilon(h)h\|\leq\varepsilon\), so \(h\) lies in the closure of \(hA\). That closure is a closed right ideal, so it is \(\mathfrak m\). For \(\alpha>0\), \(\|(1-f_\varepsilon(h))h^\alpha\|=\max_t\varepsilon t^\alpha/(t+\varepsilon)\), which is at most \(\delta^\alpha\) on \(t\leq\delta\) and at most \(\|h\|^\alpha\varepsilon/\delta\) on \(t\geq\delta\); so it tends to \(0\), and \(h^\alpha\in\mathfrak m\) by (1). Exchanging the roles of \(h\) and \(h^\alpha\) (with the exponent \(1/\alpha\)) gives \(h\) in the closed right ideal generated by \(h^\alpha\). \(\square\)

Since \(h^2\leq\|h\|h\), the condition \(xx^*\leq\lambda h^2\) implies the hypothesis of (2). The converse fails: \(x=h^{1/2}\) satisfies \(xx^*=h\), but \(h\leq\lambda h^2\) fails for every \(\lambda\) when \(\sigma'(h)\) accumulates at \(0\) without being \(\{0\}\).

The weaker domination in (2) is the exact form used in Proposition 17.2; the preceding counterexample distinguishes it from domination by the square.

**Theorem 11.4** (Approximate identities of one-sided ideals). Let \(A\) be a C\*-algebra, \(S_0\) its open unit ball, and \(\mathfrak m\) a left ideal of \(A\), not necessarily closed, with \(\mathfrak m_+=\mathfrak m\cap A_+\). Order \(\Lambda=\mathfrak m_+\cap S_0\) by \(\leq\).
1. \(\Lambda\) is upward directed.
2. The net \((u)_{u\in\Lambda}\), which is increasing and contractive, satisfies \(\|x-xu\|\to0\) for every \(x\) in the closure \(\overline{\mathfrak m}\); that is, it is a right approximate identity for \(\overline{\mathfrak m}\).
3. If \(\mathfrak m\) is a right ideal, the same set \(\Lambda\) is upward directed and is a left approximate identity for \(\overline{\mathfrak m}\). If \(\mathfrak m\) is a two-sided ideal, \(\Lambda\) is an increasing contractive approximate identity for \(\overline{\mathfrak m}\).

**Proof.** A left ideal of \(A\) is also a left ideal of \(\widetilde A\), since \(\widetilde Ax=Ax+\mathbb Cx\).
(1) Let \(u_1,u_2\in\Lambda\). Since \(\|u_j\|<1\), \(1-u_j\) is invertible in \(\widetilde A\), and \(h_j=(1-u_j)^{-1}u_j\) lies in \(\mathfrak m\). It is the calculus of \(t/(1-t)\) at \(u_j\), so \(h_j\geq0\). From \(1+h_j=(1-u_j)^{-1}\) we get \(u_j=(1+h_j)^{-1}h_j=f_1(h_j)\). Put \(h=h_1+h_2\) and \(u=f_1(h)=(1+h)^{-1}h\). Then \(u\in\mathfrak m\), \(u\geq0\), \(\|u\|=\|h\|/(1+\|h\|)<1\), and \(u\geq f_1(h_j)=u_j\) by Lemma 11.2(1).
(2) Let \(x\in\mathfrak m\) and \(\varepsilon>0\). Then \(k=x^*x\in\mathfrak m_+\), and \(u_\varepsilon=f_\varepsilon(k)=(k+\varepsilon)^{-1}k\in\Lambda\). Since \((1-f_\varepsilon(t))t=\varepsilon f_\varepsilon(t)\),
\[
\begin{gathered}
\|x(1-u_\varepsilon)^{1/2}\|^2\\
=\|(1-u_\varepsilon)^{1/2}k(1-u_\varepsilon)^{1/2}\|\\
=\|(1-u_\varepsilon)k\|\\
\leq\varepsilon .
\end{gathered}
\tag{11.1}
\]
Let \(v\in\Lambda\) with \(v\geq u_\varepsilon\). Since \(0\leq1-v\leq1-u_\varepsilon\leq1\),
\[
\begin{gathered}
\|x-xv\|\\
\leq\|x(1-v)^{1/2}\|\,\|(1-v)^{1/2}\|\\
\leq\|x(1-v)x^*\|^{1/2}\\
\leq\|x(1-u_\varepsilon)x^*\|^{1/2}\\
=\|x(1-u_\varepsilon)^{1/2}\|\\
\leq\varepsilon^{1/2},
\end{gathered}
\]
by Proposition 8.5(3)–(4). So \(xv\to x\) along \(\Lambda\) for \(x\in\mathfrak m\). For \(x\in\overline{\mathfrak m}\), use \(\|x-xv\|\leq2\|x-y\|+\|y-yv\|\) with \(y\in\mathfrak m\) close to \(x\), since \(\|v\|\leq1\).
(3) For a right ideal \(\mathfrak m\), \(\mathfrak m^*=\{x^*:x\in\mathfrak m\}\) is a left ideal with the same positive part, because positive elements are self-adjoint. Apply (1)–(2) to \(\mathfrak m^*\) and take adjoints. A two-sided ideal is both. \(\square\)

**Corollary 11.5** (Existence; the separable case).
1. Every C\*-algebra has an increasing contractive approximate identity, for instance \(A_+\cap S_0\) itself.
2. If \(A\) is separable, it has one that is an increasing sequence \((u_n)\).

**Proof.** (1) is the theorem with \(\mathfrak m=A\). (2) \(A_+\cap S_0\) is a subset of a separable metric space, so it has a dense sequence \((v_n)\). Choose \(u_1=v_1\), and by (1) of the theorem choose inductively \(u_{n+1}\in A_+\cap S_0\) with \(u_{n+1}\geq u_n\) and \(u_{n+1}\geq v_1,\dots,v_{n+1}\). Let \(x\in A\) and \(\varepsilon>0\), and let \(u_\varepsilon\) be as in (11.1), so \(\|x(1-u_\varepsilon)^{1/2}\|\leq\varepsilon^{1/2}\). Pick \(n\) with \(\|v_n-u_\varepsilon\|\leq\varepsilon/(1+\|x\|)^2\). By the Hölder estimate (9.1), applied in \(\widetilde A\) to \(1-v_n\) and \(1-u_\varepsilon\),
\[
\begin{gathered}
\|x(1-v_n)^{1/2}\|\\
\leq\|x(1-u_\varepsilon)^{1/2}\|+\|x\|\,\|v_n-u_\varepsilon\|^{1/2}\\
\leq2\varepsilon^{1/2}.
\end{gathered}
\]
For \(k\geq n\), \(u_k\geq v_n\), and the chain of inequalities in the theorem's proof gives \(\|x-xu_k\|\leq\|x(1-v_n)^{1/2}\|\leq2\varepsilon^{1/2}\). So \(xu_k\to x\) for every \(x\), and since each \(u_k\) is self-adjoint, \(\|x-u_kx\|=\|x^*-x^*u_k\|\to0\) too. \(\square\)

A separable C\*-algebra even has a sequential approximate identity whose members commute with each other (Proposition 13.3(7)).

**Exercise 11.6** (medium; Closed one-sided ideals are hereditary). If \(\mathfrak m\) is a closed ideal of \(A\), \(0\leq x\leq y\) and \(y\in\mathfrak m\), then \(x\in\mathfrak m\). In fact this holds for every closed left ideal \(\mathfrak m\).

*Solution.* \((x^{1/2})^*x^{1/2}=x\leq y\). By Corollary 11.3(2), in its left form, \(x^{1/2}\) lies in the closed left ideal generated by \(y\), which is inside \(\mathfrak m\). Then \(x=x^{1/2}x^{1/2}\in\mathfrak m\), since \(\mathfrak m\) is a left ideal. A second solution uses the approximate identity \((u_i)\) of \(\mathfrak m\) from Theorem 11.4: \[
\begin{gathered}
\|x^{1/2}-x^{1/2}u_i\|^2\\
=\|(1-u_i)x(1-u_i)\|\\
\leq\|(1-u_i)y(1-u_i)\|\\
\leq\|y-yu_i\|\to0,
\end{gathered}
\] and \(x^{1/2}u_i\in\mathfrak m\).

**Example 11.7** (A nonclosed ideal need not be self-adjoint). In \(A=C([-1,1])\), put \(f(t)=t+i|t|\) and \(I=fA\). This is a two-sided algebraic ideal. For \(t>0\) the ratio \(\overline{f(t)}/f(t)\) is \(-i\), and for \(t<0\) it is \(i\). A continuous function cannot have these two one-sided limits at \(0\), so \(\bar f\notin I\), although \(f\in I\). Thus \(I^*\ne I\).

Its closure is precisely \(J=\{h\in A:h(0)=0\}\). Certainly \(I\subseteq J\). Conversely, for \(h\in J\) and \(\varepsilon>0\), set
\[
h_\varepsilon(t)=\frac{h(t)|f(t)|^2}{|f(t)|^2+\varepsilon}
=f(t)\frac{h(t)\overline{f(t)}}{|f(t)|^2+\varepsilon}\in I.
\]
Given \(\delta>0\), continuity of \(h\) makes \(|h|<\delta\) on some interval about \(0\). There \(|h-h_\varepsilon|\leq\delta\); on the compact complement, \(|f|^2\) has a positive minimum, so \(h_\varepsilon\to h\) uniformly. Hence \(\overline I=J\). In particular \(\bar f\in\overline I\setminus I\), so \(I\) is not closed.

Theorem 11.4 still supplies positive approximate identities inside \(I\) for its closure. It does not assert that \(I\) is self-adjoint. The closedness hypothesis in Theorem 15.1 is what permits a C*-algebra quotient. For related examples and the closed-ideal proof, see [Blackadar, *Operator Algebras*, II.5.2.1 and II.5.1.1, corrected author version](https://bruceblackadar.com/Mathematics/Cycr.pdf).

### 15. Closed ideals and quotients

**Theorem 15.1** (Quotients of C\*-algebras). Let \(A\) be a C\*-algebra and \(\mathfrak m\subseteq A\) a closed ideal.
1. \(\mathfrak m^*=\mathfrak m\), so \(\mathfrak m\) is a C\*-subalgebra.
2. \(A/\mathfrak m\), with the quotient norm and \((x+\mathfrak m)^*=x^*+\mathfrak m\), is a C\*-algebra, and the quotient map is a \(*\)-homomorphism.
3. (*Quotient norm.*) Let \((e_i)\) be any net of positive contractions in \(\mathfrak m\) with \(\|y-ye_i\|\to0\) for every \(y\in\mathfrak m\), for instance the net of Theorem 11.4. Then for every \(x\in A\),
\[
\|x+\mathfrak m\|=\lim_i\|x-xe_i\| .
\tag{15.1}
\]

**Proof.** (1) By Theorem 11.4(3), \(\Lambda=\mathfrak m_+\cap S_0\) is a two-sided approximate identity for \(\mathfrak m\). For \(x\in\mathfrak m\) and \(u\in\Lambda\), \(x^*u\in\mathfrak m\) and \(\|x^*-x^*u\|=\|x-ux\|\to0\). So \(x^*\in\mathfrak m\), as \(\mathfrak m\) is closed.
(3) Let \(y\in\mathfrak m\). In \(\widetilde A\), \(0\leq1-e_i\leq1\), so \(\|1-e_i\|\leq1\), and
\[
\begin{gathered}
\|x-xe_i\|\\
=\|(x+y)(1-e_i)-(y-ye_i)\|\\
\leq\|x+y\|+\|y-ye_i\| .
\end{gathered}
\]
So \(\limsup_i\|x-xe_i\|\leq\|x+y\|\) for every \(y\in\mathfrak m\), that is, \(\limsup_i\|x-xe_i\|\leq\|x+\mathfrak m\|\). Since \(xe_i\in\mathfrak m\), \(\|x+\mathfrak m\|\leq\|x-xe_i\|\) for every \(i\). Hence the limit exists and equals \(\|x+\mathfrak m\|\).
(2) \(A/\mathfrak m\) is a Banach algebra ([quotient algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-15)). By (1) the involution is well defined, and it is isometric: \(\|x^*+\mathfrak m\|=\inf_{y\in\mathfrak m}\|x^*+y^*\|=\|x+\mathfrak m\|\). Write \(\dot x=x+\mathfrak m\), and let \((e_i)\) be as in (3). For \(z\in\mathfrak m\), \(\|(1-e_i)z(1-e_i)\|\leq\|z-ze_i\|\to0\). So by (15.1)
\[
\begin{gathered}
\|\dot x\|^2\\
=\lim_i\|(x-xe_i)^*(x-xe_i)\|\\
=\lim_i\|(1-e_i)(x^*x+z)(1-e_i)\|\\
\leq\|x^*x+z\| .
\end{gathered}
\]
Taking the infimum over \(z\), \(\|\dot x\|^2\leq\|\dot x^*\dot x\|\leq\|\dot x^*\|\|\dot x\|=\|\dot x\|^2\). So the C\*-identity holds. \(\square\)

The proof of (3) uses only positivity, contractivity and the approximation property of \((e_i)\); whether the net increases plays no part.

**Examples 15.2** (The two hypotheses of (1) are needed).
- *A closed left ideal need not be self-adjoint.* In \(M_2(\mathbb C)\), \(L=\{x:xE_{11}=x\}\), the matrices with zero second column, is a closed left ideal. It contains \(E_{21}\) but not \(E_{21}^*=E_{12}\).
- *An ideal that is not closed need not be self-adjoint.* In \(C([0,1])\), let \(h(t)=te^{i/t}\) for \(t>0\) and \(h(0)=0\), and let \(I=hC([0,1])\), an ideal. If \(\bar h=hg\) with \(g\) continuous, then \(g(t)=e^{-2i/t}\) for \(t>0\), which has no limit at \(0\). So \(\bar h\notin I\).

**Example 15.3** (The quotient norm formula). In \(A=C([0,1])\), let \(\mathfrak m=\{g:g(0)=0\}\) and \(e_n(t)=\min(1,nt)\), a positive contractive (and increasing) approximate identity of \(\mathfrak m\). For \(f\in A\), \[
\begin{gathered}
\|f-fe_n\|\\
=\sup_{t\leq1/n}|f(t)|(1-nt)\to|f(0)|\\
=\|f+\mathfrak m\|,
\end{gathered}
\] as (15.1) says.

**Corollary 15.4** (Kernels and ranges of \(*\)-homomorphisms). Let \(\pi:A\to B\) be a \(*\)-homomorphism of C\*-algebras. Then \(\ker\pi\) is a closed ideal, the range \(\pi(A)\) is closed, hence a C\*-subalgebra of \(B\), and \(\tilde\pi(x+\ker\pi)=\pi(x)\) is an isometric \(*\)-isomorphism of \(A/\ker\pi\) onto \(\pi(A)\). In particular \(\|\pi(x)\|=\|x+\ker\pi\|\).

**Proof.** \(\pi\) is continuous (Theorem 4.2), so \(\ker\pi\) is a closed ideal, and \(A/\ker\pi\) is a C\*-algebra (Theorem 15.1). The induced map \(\tilde\pi\) is an injective \(*\)-homomorphism into \(B\), hence isometric with closed range (Corollary 4.6). \(\square\)

**Exercise 15.5** (easy; Ideals of ideals). Let \(I\) be a closed ideal of \(A\) and \(J\) a closed ideal of the C\*-algebra \(I\). Show that \(J\) is an ideal of \(A\).

*Solution.* Let \(x\in J\), \(a\in A\), and let \((u)\) be the approximate identity of Theorem 11.4 for the closed ideal \(J\) of the C\*-algebra \(I\). Then \(ux\to x\), and \(au\in I\), since \(u\in J\subseteq I\) and \(I\) is an ideal of \(A\). So \((au)x\in IJ\subseteq J\), and \(ax=\lim(au)x\in J\), as \(J\) is closed. Similarly \(xa=\lim x(ua)\in J\).

**Exercise 15.6** (easy; A C\*-subalgebra plus a closed ideal). If \(B\) is a C\*-subalgebra and \(\mathfrak m\) a closed ideal of \(A\), then \(B+\mathfrak m\) is a C\*-subalgebra.

*Solution.* \(B+\mathfrak m\) is a \(*\)-subalgebra, because \((b+x)(b'+x')=bb'+(bx'+xb'+xx')\) and \(\mathfrak m\) is a self-adjoint ideal (Theorem 15.1). Let \(\pi:A\to A/\mathfrak m\). By Corollary 15.4, applied to \(\pi|_B\), the set \(\pi(B)\) is closed. So \(B+\mathfrak m=\pi^{-1}(\pi(B))\) is closed.

### 16. Ideals of commutative C\*-algebras

**Proposition 16.1** (Hull and kernel). Let \(A\) be abelian, with character space \(\Omega\). For a closed set \(\Gamma\subseteq\Omega\) and a closed ideal \(\mathfrak m\) put
\[
\begin{gathered}
\mathfrak m_\Gamma\\
=\{x\in A: \ \omega(x)=0\ \text{for all }\omega\in\Gamma\},\\
\Gamma_{\mathfrak m}\\
=\{\omega\in\Omega: \ \omega(x)=0\ \text{for all }x\in\mathfrak m\}.
\end{gathered}
\]
1. \(\Gamma\mapsto\mathfrak m_\Gamma\) and \(\mathfrak m\mapsto\Gamma_{\mathfrak m}\) are mutually inverse bijections, reversing inclusion, between the closed subsets of \(\Omega\) and the closed ideals of \(A\).
2. If \(\rho:A\to A/\mathfrak m\) is the quotient map, then \(\omega'\mapsto\omega'\circ\rho\) is a homeomorphism of \(\operatorname{Ch}(A/\mathfrak m)\) onto \(\Gamma_{\mathfrak m}\).
3. Restriction \(\omega\mapsto\omega|_{\mathfrak m}\) is a homeomorphism of \(\Omega\setminus\Gamma_{\mathfrak m}\) onto \(\operatorname{Ch}(\mathfrak m)\).

Identifying \(A\) with \(C_0(\Omega)\) (Theorem 2.1 and Proposition 2.2): \(\mathfrak m_\Gamma\) is the set of functions vanishing on \(\Gamma\); restriction to \(\Gamma\) identifies \(A/\mathfrak m_\Gamma\) with \(C_0(\Gamma)\); and \(\mathfrak m_\Gamma\) is \(C_0(\Omega\setminus\Gamma)\). The ideal \(\mathfrak m_\Gamma\) is called the *kernel* of \(\Gamma\), and \(\Gamma_{\mathfrak m}\) the *hull* of \(\mathfrak m\).

**Proof.** \(\mathfrak m_\Gamma\) is an intersection of kernels of characters, so it is a closed ideal; \(\Gamma_{\mathfrak m}\) is weak\* closed. Clearly \(\mathfrak m\subseteq\mathfrak m_{\Gamma_{\mathfrak m}}\) and \(\Gamma\subseteq\Gamma_{\mathfrak m_\Gamma}\).
(1) *\(\mathfrak m_{\Gamma_{\mathfrak m}}\subseteq\mathfrak m\).* Let \(x_0\notin\mathfrak m\). Then \(\rho(x_0)\neq0\) in the abelian C\*-algebra \(A/\mathfrak m\) (Theorem 15.1). By Theorem 2.1 its Gelfand transform is not zero, so some character \(\omega'\) of \(A/\mathfrak m\) has \(\omega'(\rho(x_0))\neq0\). Then \(\omega=\omega'\circ\rho\) is a character of \(A\) that vanishes on \(\mathfrak m\), so \(\omega\in\Gamma_{\mathfrak m}\), and \(\omega(x_0)\neq0\); so \(x_0\notin\mathfrak m_{\Gamma_{\mathfrak m}}\).
*\(\Gamma_{\mathfrak m_\Gamma}\subseteq\Gamma\).* Let \(\omega_0\notin\Gamma\). By [Urysohn's lemma](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-16) in its locally compact form, there is \(f\in C_c(\Omega)\) with \(f(\omega_0)=1\) and \(f=0\) on \(\Gamma\). The element \(x\) with \(\hat x=f\) lies in \(\mathfrak m_\Gamma\) and \(\omega_0(x)\neq0\), so \(\omega_0\notin\Gamma_{\mathfrak m_\Gamma}\).
(2) A character \(\omega\) of \(A\) vanishing on \(\mathfrak m\) factors as \(\omega=\omega'\circ\rho\), with \(\omega'(x+\mathfrak m)=\omega(x)\) a character of \(A/\mathfrak m\); conversely \(\omega'\circ\rho\) is a character (nonzero because \(\rho\) is onto) vanishing on \(\mathfrak m\). So the map is a bijection onto \(\Gamma_{\mathfrak m}\). It is weak\* continuous, and so is its inverse: if \(\omega'_\alpha\circ\rho\to\omega'\circ\rho\) pointwise on \(A\), then \(\omega'_\alpha\to\omega'\) pointwise on \(A/\mathfrak m\).
(3) For \(\omega\in\Omega\), \(\omega|_{\mathfrak m}\) is a homomorphism, nonzero exactly when \(\omega\notin\Gamma_{\mathfrak m}\). The restriction map \(I\) is weak\* continuous.
*Injective.* For \(\omega_1\neq\omega_2\) in \(\Omega\setminus\Gamma_{\mathfrak m}\), Urysohn's lemma gives \(f\in C_c(\Omega)\) with \(f(\omega_1)=1\) and \(f=0\) on the closed set \(\Gamma_{\mathfrak m}\cup\{\omega_2\}\). By (1), the element with transform \(f\) lies in \(\mathfrak m\), and it separates \(I(\omega_1)\) from \(I(\omega_2)\).
*Surjective.* Let \(\chi\in\operatorname{Ch}(\mathfrak m)\) and \(e\in\mathfrak m\) with \(\chi(e)=1\). Put \(\omega(x)=\chi(ex)\) for \(x\in A\), which makes sense because \(ex\in\mathfrak m\). Since \(A\) is commutative, \(\omega(xy)=\chi(exy)\chi(e)=\chi(ex\cdot ey)=\omega(x)\omega(y)\), and for \(x\in\mathfrak m\), \(\omega(x)=\chi(e)\chi(x)=\chi(x)\). So \(\omega\) is a character with \(I(\omega)=\chi\).
*Open.* Let \(\omega_0\in W\subseteq\Omega\setminus\Gamma_{\mathfrak m}\) with \(W\) open. Choose \(f\in C_c(\Omega)\) with \(f(\omega_0)=1\) and support in \(W\), and let \(x\in\mathfrak m\) have \(\hat x=f\). The set \(\{\chi\in\operatorname{Ch}(\mathfrak m):\chi(x)\neq0\}\) is open, contains \(I(\omega_0)\), and lies in \(I(W)\), because \(\chi=I(\omega)\) with \(\omega(x)=f(\omega)\neq0\) forces \(\omega\in W\). So \(I\) is open, hence a homeomorphism.
*The concrete description.* Under \(A=C_0(\Omega)\), (1) says that \(\mathfrak m_\Gamma\) is the set of functions vanishing on \(\Gamma\). The map \(f\mapsto f|_\Gamma\) is a \(*\)-homomorphism into \(C_0(\Gamma)\) with kernel \(\mathfrak m_\Gamma\). Its range is closed (Corollary 15.4), separates the points of \(\Gamma\) and vanishes nowhere on it (Urysohn), so it is \(C_0(\Gamma)\) by the [Stone–Weierstrass theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09). Likewise \(\mathfrak m_\Gamma\), as a C\*-algebra, has character space \(\Omega\setminus\Gamma\) by (3), so it is \(C_0(\Omega\setminus\Gamma)\) by Theorem 2.1. \(\square\)

**Example 16.2** (\(C_0(\mathbb R)\)). Let \(A=C_0(\mathbb R)\). By Proposition 2.2, the characters are the evaluations, so \(\sigma'(x)=x(\mathbb R)\cup\{0\}\), and by Theorem 5.3(4), \(f(x)=f\circ x\) for \(f(0)=0\). Positivity is pointwise. The function \(a(t)=e^{-t^2}\) is strictly positive: \(f_\varepsilon(a)=a/(a+\varepsilon)\) tends to \(1\) uniformly on compact sets, and for \(g\in C_0(\mathbb R)\) and \(\eta>0\), \(|g|<\eta\) off a compact set \(C\), so \[
\begin{gathered}
\|g-f_\varepsilon(a)g\|\\
\leq\max(\eta,\|g\|\max_C|1-f_\varepsilon(a)|)\to\eta;
\end{gathered}
\] this is Proposition 13.3(3) seen directly. The closed ideals correspond to closed \(F\subseteq\mathbb R\) (Proposition 16.1): for \(F=\{0\}\), \(\mathfrak m_F=\{g:g(0)=0\}\cong C_0(\mathbb R\setminus\{0\})\), and \(A/\mathfrak m_F\cong\mathbb C\) through \(g\mapsto g(0)\).

### 17. Lifting through quotients

**Proposition 17.1** (Lifting self-adjoint, positive and arbitrary elements). Let \(\pi:A\to B\) be a surjective \(*\)-homomorphism of C\*-algebras.
1. Every \(k\in B_h\) is \(\pi(h)\) for some \(h\in A_h\) with \(\|h\|=\|k\|\). If \(k\geq0\), \(h\) can be chosen with \(h\geq0\) and \(\|h\|=\|k\|\).
2. Every \(k\in B\) is \(\pi(x)\) for some \(x\in A\) with \(\|x\|=\|k\|\).
3. \(\pi(A_+)=B_+\).

**Proof.** (1) Let \(h'\in A\) with \(\pi(h')=k\). Then \(h''=\frac12(h'+h'^*)\) is self-adjoint with \(\pi(h'')=k\). Put \(c=\|k\|\) and \(\tau(t)=\max(-c,\min(t,c))\), a continuous function with \(\tau(0)=0\) and \(|\tau|\leq c\). Let \(h=\tau(h'')\in A_h\). Then \(\|h\|\leq c\), and by Corollary 5.4(3), \(\pi(h)=\tau(k)=k\), since \(\sigma'(k)\subseteq[-c,c]\), where \(\tau\) is the identity. So \(c=\|\pi(h)\|\leq\|h\|\leq c\). If \(k\geq0\), use \(\tau_+(t)=\min(\max(t,0),c)\) instead; then \(h\geq0\).
(2) Let \(x'\in A\) with \(\pi(x')=k\), and \(c=\|k\|\); if \(c=0\) take \(x=0\). Let \(g(t)=\min(1,ct^{-1/2})\) for \(t>0\) and \(g(0)=1\), a continuous function on \([0,\infty)\) that equals \(1\) on \([0,c^2]\). Put \(x=x'g(x'^*x')\), which lies in \(A\) because \(A\) is an ideal of \(\widetilde A\). Then
\[
\begin{gathered}
\|x\|^2\\
=\|g(x'^*x')\,x'^*x'\,g(x'^*x')\|\\
=\max_{t\in\sigma'(x'^*x')}tg(t)^2\\
\leq c^2 ,
\end{gathered}
\]
since \(tg(t)^2=\min(t,c^2)\). By Corollary 5.4(2), \(\pi(x)=k\,g(k^*k)=k\), because \(\sigma'(k^*k)\subseteq[0,c^2]\), where \(g=1\). So \(\|x\|=c\).
(3) \(\pi(A_+)\subseteq B_+\) by Proposition 8.5(12), and (1) gives the rest. \(\square\)

A second proof of (1) uses Tietze's extension theorem. The C\*-algebra \(C^*(h'')\) is abelian, and restricting \(\pi\) to it reduces (1) to the abelian case. There, by Proposition 16.1, the quotient map is restriction \(C_0(\Omega)\to C_0(\Gamma)\), and a bounded extension exists by [Tietze's theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-18) on the one-point compactification, which is compact Hausdorff but need not be metrizable. Neither proof needs separability.

**Proposition 17.2** (Lifting \(\{y^*y\leq\pi(a)\}\)). Let \(\pi:A\to B\) be a surjective \(*\)-homomorphism of C\*-algebras and \(a\in A_+\). Then
\[
\begin{gathered}
\pi\big(\{x\in A: \ x^*x\leq a\}\big)\\
=\{y\in B: \ y^*y\leq\pi(a)\}.
\end{gathered}
\]

**Proof.** Put \(b=\pi(a)\). If \(x^*x\leq a\), then \(\pi(x)^*\pi(x)=\pi(x^*x)\leq b\) (Proposition 8.5(12)). Conversely let \(y^*y\leq b\).
*Step 1: a self-adjoint \(h\leq a\) with \(\pi(h)=y^*y\).* Choose \(h_0\in A_h\) with \(\pi(h_0)=y^*y\) (Proposition 17.1(1)). Then \(\pi(a-h_0)=b-y^*y\geq0\). By Corollary 5.4(3), \(\pi((a-h_0)_\pm)=(b-y^*y)_\pm\), which is \(b-y^*y\) for the sign \(+\) and \(0\) for the sign \(-\). Put \(h=a-(a-h_0)_+\). Then \(h\leq a\) and \(\pi(h)=b-(b-y^*y)=y^*y\).
*Step 2: a dominating element.* Choose \(z\in A\) with \(\pi(z)=y\), and put \(k=z^*z-h\in A_h\). Then \(\pi(k)=0\), so \(\pi(k_+)=\pi(k)_+=0\). Put \(c=a+k_+\geq0\). Since \(k\leq k_+\), \(z^*z=h+k\leq a+k_+=c\), and \(\pi(c)=b\).
*Step 3: the approximation.* For \(s>0\) put \(v_s=f_s(c)=(s+c)^{-1}c\) and \(x_s=z(s+c)^{-1}c^{1/2}a^{1/2}\in A\). With \(d=(s+c)^{-1}-(t+c)^{-1}\), which commutes with \(c\) and has \(dc=v_s-v_t\),
\[
\begin{gathered}
(x_s-x_t)^*(x_s-x_t)\\
=a^{1/2}c^{1/2}d\,z^*z\,d\,c^{1/2}a^{1/2}\\
\leq a^{1/2}c^{1/2}dcdc^{1/2}a^{1/2}\\
=\big((v_s-v_t)a^{1/2}\big)^*\big((v_s-v_t)a^{1/2}\big).
\end{gathered}
\]
So \(\|x_s-x_t\|\leq\|a^{1/2}v_s-a^{1/2}v_t\|\). Since \((a^{1/2})^*a^{1/2}=a\leq c\), Corollary 11.3(2), in its left form, gives \(a^{1/2}v_s\to a^{1/2}\) as \(s\to0\). So \((x_s)\) is Cauchy; let \(x=\lim_{s\to0}x_s\in A\). In the same way, \(x_s^*x_s\leq a^{1/2}v_s^2a^{1/2}\leq a\), and so \(x^*x\leq a\), because \(A_+\) is closed. Finally, by Corollary 5.4(2),
\[
\pi(x_s)=y(s+b)^{-1}b^{1/2}b^{1/2}=yf_s(b)\longrightarrow y ,
\]
by Corollary 11.3(2) again, since \(y^*y\leq b\). So \(\pi(x)=y\). \(\square\)

**Corollary 17.3** (Order intervals; sums of closed ideals).
1. (*Order intervals.*) \[
\begin{gathered}
\pi(\{p\in A:0\leq p\leq a\})\\
=\{q\in B:0\leq q\leq\pi(a)\}.
\end{gathered}
\]
2. For closed ideals \(\mathfrak m\) and \(\mathfrak n\) of \(A\), \(\mathfrak m+\mathfrak n\) is a closed ideal and \((\mathfrak m+\mathfrak n)_+=\mathfrak m_++\mathfrak n_+\).

**Proof.** (1) If \(0\leq q\leq\pi(a)\), then \(y=q^{1/2}\) satisfies \(y^*y=q\leq\pi(a)\). The Proposition gives \(x\) with \(x^*x\leq a\) and \(\pi(x)=q^{1/2}\), and \(p=x^*x\) works. The other inclusion is Proposition 8.5(12).
(2) *Closed.* Let \(\rho_{\mathfrak m}:A\to A/\mathfrak m\). By Corollary 15.4, applied to the restriction of \(\rho_{\mathfrak m}\) to the C\*-algebra \(\mathfrak n\), the set \(\rho_{\mathfrak m}(\mathfrak n)\) is closed, and \(\mathfrak m+\mathfrak n=\rho_{\mathfrak m}^{-1}(\rho_{\mathfrak m}(\mathfrak n))\) is closed. It is clearly an ideal.
*Positive parts.* \(\mathfrak m_++\mathfrak n_+\subseteq(\mathfrak m+\mathfrak n)_+\) is clear. Let \(a\in(\mathfrak m+\mathfrak n)_+\), and let \(\rho:A\to A/(\mathfrak m\cap\mathfrak n)\) be the quotient map. The sets \(I=\rho(\mathfrak m)\) and \(J=\rho(\mathfrak n)\) are closed ideals (Corollary 15.4, and \(\rho\) is onto), and \(I\cap J=0\): if \(\rho(u)=\rho(v)\) with \(u\in\mathfrak m\) and \(v\in\mathfrak n\), then \(u-v\in\mathfrak m\cap\mathfrak n\), so \(u\in\mathfrak n\), \(u\in\mathfrak m\cap\mathfrak n\) and \(\rho(u)=0\). Write \(\rho(a)=i+j\) with \(i\in I\) and \(j\in J\). Then \(i-i^*=j^*-j\in I\cap J=0\), so \(i\) and \(j\) are self-adjoint, and \(ij\) and \(ji\) lie in \(I\cap J\), so they vanish. In the commutative C\*-algebra \(C^*(i,j)\), the functions \(\hat i\) and \(\hat j\) have disjoint nonzero sets and their sum is \(\geq0\); so \(i,j\geq0\). Lift \(i\) to some \(x_0\in\mathfrak m_+\) (Proposition 17.1(3), for the surjection \(\mathfrak m\to I\)). Since \(\rho(x_0^{1/2})^*\rho(x_0^{1/2})=i\leq\rho(a)\), the Proposition gives \(x\in A\) with \(x^*x\leq a\) and \(\rho(x)=\rho(x_0^{1/2})\). Then \(x-x_0^{1/2}\in\mathfrak m\cap\mathfrak n\subseteq\mathfrak m\), so \(x\in\mathfrak m\) and \(p=x^*x\in\mathfrak m_+\), with \(p\leq a\) and \(\rho(p)=i\). The element \(q=a-p\geq0\) has \(\rho(q)=j=\rho(n_0)\) for some \(n_0\in\mathfrak n\), so \(q\in n_0+\mathfrak m\cap\mathfrak n\subseteq\mathfrak n\). Thus \(a=p+q\) with \(p\in\mathfrak m_+\) and \(q\in\mathfrak n_+\). \(\square\)

The point of the proof of (2) is to apply Proposition 17.2 to the quotient by \(\mathfrak m\cap\mathfrak n\), so that the correction term falls into \(\mathfrak m\).

**Exercise 17.4** (medium; Lifting unitaries). Let \(A\) be unital, \(\mathfrak m\) a closed ideal and \(\pi:A\to A/\mathfrak m\). (a) If \(\dot u\in U(A/\mathfrak m)\) and \(\sigma(\dot u)\neq\mathbb T\), then \(\dot u=\pi(u)\) for a unitary \(u\in A\). (b) More generally, every unitary in the connected component \(U_0(A/\mathfrak m)\) of \(1\) in \(U(A/\mathfrak m)\) is the image of a unitary in \(U_0(A)\).

*Solution.* If \(\mathfrak m=A\), then \(A/\mathfrak m=0\) and \(u=1\) works; so let \(\mathfrak m\neq A\).
*A lemma: in a nontrivial unital C\*-algebra \(D\), \(U_0(D)\) is the set \(E\) of finite products \(\exp(ih_1)\cdots\exp(ih_n)\) with \(h_k\in D_h\).* Each \(\exp(ih)\) is unitary (proof of Proposition 1.5(3)), and \(\exp(ih)^{-1}=\exp(-ih)\), so \(E\) is a subgroup of \(U(D)\). It is path connected through \(t\mapsto\prod_k\exp(ith_k)\), so \(E\subseteq U_0(D)\). It is open in \(U(D)\): if \(w\in E\), \(v\in U(D)\) and \(\|v-w\|<2\), then \(\|w^{-1}v-1\|=\|v-w\|<2\), so every \(\lambda\in\sigma(w^{-1}v)\) has \(|\lambda-1|<2\) and \(-1\notin\sigma(w^{-1}v)\); Exercise 7.4 gives \(w^{-1}v=\exp(ih)\), so \(v\in E\). An open subgroup is also closed, since its complement is a union of open cosets. So \(E\) is open and closed in \(U(D)\) and contains \(1\), and \(E\supseteq U_0(D)\). This is the unitary counterpart of the description of [the principal component](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-14) of the invertible group.
(b) Write \(\dot u=\prod_k\exp(i\dot h_k)\), lift each \(\dot h_k\) to \(h_k\in A_h\) (Proposition 17.1(1)), and put \(u=\prod_k\exp(ih_k)\in U_0(A)\). The unital homomorphism \(\pi\) is continuous, so it passes through the exponential series, and \(\pi(u)=\dot u\).
(a) By Exercise 7.4, \(\dot u=\exp(i\dot h)\), which lies in \(U_0(A/\mathfrak m)\); apply (b).

**Exercise 17.5** (medium; A unitary that does not lift). Let \(\bar{\mathbb D}\) be the closed unit disc, \(A=C(\bar{\mathbb D})\), and \(\mathfrak m\) the closed ideal of functions vanishing on \(\mathbb T\) (Proposition 16.1), so that \(A/\mathfrak m=C(\mathbb T)\) by restriction. The unitary \(\dot u(\lambda)=\lambda\) of \(C(\mathbb T)\) is not the image of a unitary of \(A\).

*Solution.* Suppose \(u\in C(\bar{\mathbb D})\), \(|u|=1\), and \(u=\dot u\) on \(\mathbb T\). By uniform continuity choose \(N\) with \(|u(p)-u(p')|<1\) whenever \(|p-p'|\leq1/N\). For \(w\in\bar{\mathbb D}\), the numbers \(u(kw/N)/u((k-1)w/N)\), \(k=1,\dots,N\), lie in \(\{\zeta\in\mathbb T:|\zeta-1|<1\}\), where the principal argument \(\operatorname{Arg}\) is continuous. Fix \(\theta_0\) with \(e^{i\theta_0}=u(0)\) and put
\[
h(w)=\theta_0+\sum_{k=1}^N\operatorname{Arg}\frac{u(kw/N)}{u((k-1)w/N)} .
\]
Then \(h\) is real and continuous, and the product telescopes: \(e^{ih(w)}=u(w)\). Restricted to \(\mathbb T\), this gives \(\lambda=e^{ih(\lambda)}\), which Exercise 7.5 rules out. By Exercise 17.4, \(\dot u\notin U_0(C(\mathbb T))\); here \(\sigma(\dot u)=\mathbb T\).

## C. Choose local units and divide a positive element

A net of local units always exists, but a sequence requires additional structure. Strictly positive elements provide a single element whose spectral cutoffs approximate the whole algebra; the countability theorem states the exact equivalence. Convolution gives another instructive family: concentration of a kernel near the group identity replaces a pointwise unit, and the involution and Haar conventions must be checked.

The last question is an order decomposition. If a positive element is dominated by a sum, can it be divided among the summands? Commuting functions suggest a pointwise answer, while general C*-algebras require the asymmetric bounds proved below. The full theorem retains arbitrary families, unconditional norm convergence and the support conclusions for closed one-sided ideals.

### 13. Strictly positive elements and countable approximate identities

A C\*-algebra has a sequential approximate identity exactly when it has a strictly positive element (Proposition 13.3). We first collect the facts about positive linear functionals that are needed. A linear functional \(\varphi\) on a C\*-algebra \(A\) is *positive* if \(\varphi(A_+)\subseteq[0,\infty)\), and a *state* is a positive linear functional of norm one.

**Lemma 13.1** (Positive linear functionals). Let \(A\) be a C\*-algebra and \(\varphi\) a positive linear functional on \(A\).
1. \(\varphi\) is bounded.
2. \(\varphi\) is hermitian, and \(|\varphi(y^*x)|^2\leq\varphi(x^*x)\varphi(y^*y)\) for all \(x,y\in A\).
3. \(|\varphi(x)|^2\leq\|\varphi\|\varphi(x^*x)\) for all \(x\in A\).
4. The set \(Q\) of positive linear functionals of norm at most one is weak\* compact.
5. If \(A\) is unital and nontrivial, then \(\|\varphi\|=\varphi(1)\).
6. (*States.*) If \(A\) is unital and nontrivial, \(h\in A_h\) and \(\lambda\in\sigma(h)\), some state \(\omega\) has \(\omega(h)=\lambda\).
7. (*States.*) If \(A\neq0\) and \(a\in A_+\), some state \(\omega\) has \(\omega(a)=\|a\|\).

**Proof.** (1) If not, since every element is a combination of four positive elements of no larger norm (Proposition 8.5(8)), there are \(a_n\in A_+\) with \(\|a_n\|\leq1\) and \(\varphi(a_n)\geq4^n\). The series \(a=\sum2^{-n}a_n\) converges, \(a\geq2^{-n}a_n\) because the rest of the series is positive, and so \(\varphi(a)\geq2^n\) for every \(n\), which is absurd.
(2) For \(h\in A_h\), \(\varphi(h)=\varphi(h_+)-\varphi(h_-)\) is real (Proposition 8.5(8)), so \(\varphi\) is hermitian. The form \((x,y)\mapsto\varphi(y^*x)\) is sesquilinear and positive semidefinite, so the inequality is the Cauchy–Schwarz inequality, Proposition 1.1(3) of [Hilbert spaces and compact operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html).
(3) For \(u\) in the approximate identity of Theorem 11.4, \(|\varphi(ux)|^2\leq\varphi(u^2)\varphi(x^*x)\leq\|\varphi\|\varphi(x^*x)\), and \(\varphi(ux)\to\varphi(x)\).
(4) \(Q\) lies in the closed unit ball of the dual of \(A\), which is weak\* compact by the Banach–Alaoglu theorem (Theorem 3.1 of [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html)), and positivity is a weak\*-closed condition.
(5) Let \(\|x\|\leq1\). By (2) with \(y=1\), \(|\varphi(x)|^2\leq\varphi(x^*x)\varphi(1)\). Since \(x^*x\leq\|x\|^2\leq1\) (Proposition 8.5(2)), \(\varphi(x^*x)\leq\varphi(1)\). So \(|\varphi(x)|\leq\varphi(1)\), and \(\|\varphi\|\leq\varphi(1)\leq\|\varphi\|\,\|1\|=\|\varphi\|\).
(6) *A state of \(C^*(1,h)\).* By Theorem 5.1, \(f(h)\mapsto f(\lambda)\) is a well-defined linear functional \(\omega_0\) on \(B=C^*(1,h)\). It is positive, because the positive elements of \(B\) are the \(f(h)\) with \(f\geq0\) (Theorem 5.1 and Remark 8.4). By (5), \(\|\omega_0\|=\omega_0(1)=1\).
*Extension.* By the Hahn–Banach theorem (Corollary 2.3(1) of [Hahn–Banach, Baire and the basic theorems on Banach spaces](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html)), \(\omega_0\) extends to \(\omega\in A^*\) with \(\|\omega\|=1=\omega(1)\).
*Such an \(\omega\) is positive.* Let \(a\in A_+\) with \(\|a\|\leq1\), and write \(\omega(a)=\alpha+i\beta\).
- For real \(t\), \[
\begin{gathered}
\|a+it\|^2\\
=\|(a-it)(a+it)\|\\
=\|a^2+t^2\|\\
\leq1+t^2,
\end{gathered}
\] so \(\alpha^2+(\beta+t)^2=|\omega(a+it)|^2\leq1+t^2\). That is, \(\alpha^2+\beta^2+2\beta t\leq1\) for every \(t\), so \(\beta=0\).
- \(\sigma(1-a)\subseteq[0,1]\), so \(\|1-a\|\leq1\) (Theorem 1.3). Hence \(|1-\omega(a)|\leq1\), and \(\omega(a)\geq0\).

So \(\omega\) is a state, and \(\omega(h)=\omega_0(h)=\lambda\).
(7) In \(\widetilde A\), \(\sigma'(a)\subseteq[0,\|a\|]\), and \(\|a\|=r(a)\) lies in \(\sigma'(a)\) (Theorem 1.3). By (6) in \(\widetilde A\), some state \(\tilde\omega\) of \(\widetilde A\) has \(\tilde\omega(a)=\|a\|\). Its restriction \(\omega\) to \(A\) is positive with \(\|\omega\|\leq1\). If \(a\neq0\), then \(\omega(a)=\|a\|\) forces \(\|\omega\|=1\). If \(a=0\), take any nonzero \(b\in A_+\), for instance \(b=x^*x\) with \(x\neq0\), and a state \(\omega\) with \(\omega(b)=\|b\|\); then \(\omega(a)=0=\|a\|\). \(\square\)

Parts (6) and (7) say that states exist in abundance.

**Definition 13.2.** An element \(a\in A_+\) is *strictly positive* if \(\varphi(a)>0\) for every nonzero positive linear functional \(\varphi\).

**Proposition 13.3** (Strictly positive elements). Let \(A\) be a C\*-algebra, \(a\in A_+\), and \(f_t(\lambda)=\lambda/(\lambda+t)\).
1. If \(A\) is unital and nontrivial, \(a\) is strictly positive if and only if it is invertible.
2. Every separable C\*-algebra has a strictly positive element.
3. \(a\) is strictly positive if and only if \(\|f_t(a)x-x\|\to0\) as \(t\to0\), for every \(x\in A\).
4. Let \(a\) be strictly positive, and let \(\pi:A\to B(H)\) be a *nondegenerate representation*: a \(*\)-homomorphism such that \(\pi(A)H\) spans a dense subspace. Then \(\pi(f_t(a))\xi\to\xi\) for every \(\xi\in H\).
5. If \(a\) is strictly positive, \((f_{1/n}(a))_{n\geq1}\) is an increasing, contractive, commuting approximate identity.
6. (*Converse of (5).*) If some sequence \((e_n)\) in \(A\) satisfies \(\|e_nx-x\|\to0\) for every \(x\in A\), for instance a sequential approximate identity, then \(a=\sum_n2^{-n}(1+\|e_n\|^2)^{-1}e_ne_n^*\) is strictly positive. If the \(e_n\) are positive contractions, \(a=\sum_n2^{-n}e_n\) is strictly positive as well.
7. Every separable C\*-algebra has an increasing, contractive approximate identity made of a commuting sequence.

**Proof.** (1) If \(a\) is invertible, then \(a\geq m\) with \(m=\min\sigma(a)>0\), and \(\varphi(a)\geq m\varphi(1)=m\|\varphi\|>0\) for \(\varphi\neq0\). If \(a\) is not invertible, \(0\in\sigma(a)\), and some state \(\omega\) has \(\omega(a)=0\).
(2) If \(A=0\), \(a=0\) will do. Otherwise let \((v_n)\) be dense in \(A_+\cap\{\|x\|\leq1\}\) and \(a=\sum_n2^{-n}v_n\). Let \(\varphi\neq0\) be positive. Since \(A_+\) spans \(A\), \(\varphi(v)>0\) for some positive \(v\) of norm at most one, and by Lemma 13.1(1) and density, \(\varphi(v_n)>0\) for some \(n\). Then \(\varphi(a)\geq2^{-n}\varphi(v_n)>0\).
(3) *Only if.* Fix \(x\in A\). For \(t>0\) put \(y_t=x^*(1-f_t(a))^2x\in A_+\) and \(g_t(\varphi)=\varphi(y_t)\) on \(Q\). Each \(g_t\) is weak\* continuous. Since \(1-f_t(\lambda)=t/(\lambda+t)\) increases with \(t\), \(y_s\leq y_t\) for \(s<t\), so \(g_t\) decreases as \(t\downarrow0\), to a limit \(g\geq0\).
*Claim: \(g=0\).* Suppose \(g(\varphi)=L>0\) for some \(\varphi\in Q\); then \(\varphi\neq0\). For \(t>0\) define \(\rho_t(y)=\varphi\big(x^*(1-f_t(a))\,y\,(1-f_t(a))x\big)\) for \(y\in A\). It is a positive functional with \(\|\rho_t\|\leq\|x\|^2\). First,
\[
\rho_t(a)\leq\|x\|^2\,\|(1-f_t(a))^2a\|\leq\|x\|^2t/4 ,
\]
since \(\lambda t^2/(\lambda+t)^2\leq t/4\). Second, with \(w_t=x^*(1-f_t(a))x\in A_h\), \(\rho_t(xx^*)=\varphi(w_t^2)\geq\varphi(w_t)^2/\|\varphi\|\) by Lemma 13.1(3), and \(\varphi(w_t)\geq\varphi(y_t)=g_t(\varphi)\geq L\) because \(1-f_t\geq(1-f_t)^2\). So \(\rho_t(xx^*)\geq L^2/\|\varphi\|\). By Lemma 13.1(4) the net \((\rho_t)_{t\downarrow0}\) has a weak\* cluster point \(\rho\), a positive functional with \(\rho(a)=0\) and \(\rho(xx^*)\geq L^2/\|\varphi\|>0\). This contradicts strict positivity.
*Dini.* For \(\eta>0\) the open sets \(\{g_t<\eta\}\) increase as \(t\downarrow0\) and cover the compact set \(Q\), so one of them is all of \(Q\), and \(g_t<\eta\) on \(Q\) for all smaller \(t\). By the existence of states, \(\|(1-f_t(a))x\|^2=\|y_t\|=\sup_{\varphi\in Q}\varphi(y_t)\to0\) (for \(A=0\) there is nothing to prove).
*If.* Let \(\varphi\geq0\) with \(\varphi(a)=0\). Since \(f_t(\lambda)^2\leq f_t(\lambda)\leq\lambda/t\), \(0\leq\varphi(f_t(a)^2)\leq\varphi(a)/t=0\). By Lemma 13.1(2), \(|\varphi(f_t(a)x)|^2\leq\varphi(f_t(a)^2)\varphi(x^*x)=0\). Since \(\varphi\) is continuous (Lemma 13.1(1)), \(\varphi(x)=\lim_t\varphi(f_t(a)x)=0\). So \(\varphi=0\).
(4) For \(x\in A\) and \(\eta\in H\), \[
\begin{gathered}
\|\pi(f_t(a))\pi(x)\eta-\pi(x)\eta\|\\
\leq\|f_t(a)x-x\|\,\|\eta\|\to0
\end{gathered}
\] by (3) and Theorem 4.2. Such vectors span a dense subspace, and \(\|\pi(f_t(a))\|\leq1\), so the convergence extends to all \(\xi\).
(5) The \(f_{1/n}(a)\) are positive, of norm less than one, functions of \(a\) (so they commute), and increasing in \(n\) (Lemma 11.2(2)). By (3) they form a left approximate identity, and as they are self-adjoint, a right one too.
(6) Let \(\varphi\geq0\) with \(\varphi(a)=0\). Each term of the series defining \(a\) is positive, and \(a\) minus that term is positive, so \(\varphi(e_ne_n^*)=0\) for every \(n\). By Lemma 13.1(2) with \(y=e_n^*\), \(|\varphi(e_nx)|^2\leq\varphi(x^*x)\varphi(e_ne_n^*)=0\) for all \(x\), and \(\varphi(x)=\lim_n\varphi(e_nx)=0\) by Lemma 13.1(1). For positive contractions and \(a=\sum_n2^{-n}e_n\), the same argument gives \(\varphi(e_n)=0\), and \(\varphi(e_ne_n^*)=\varphi(e_n^2)\leq\varphi(e_n)=0\) because \(e_n^2\leq e_n\).
(7) combines (2) and (5). \(\square\)

So a C\*-algebra has a strictly positive element exactly when it has a sequential approximate identity; such algebras are called *\(\sigma\)-unital*. Proposition 13.4 gives a C\*-algebra with no strictly positive element. That algebra is commutative, so all its approximate identities commute: the converse of (5) fails for commuting approximate identities that are not sequences.

**Proposition 13.4** (A C\*-algebra without a strictly positive element). Let \((\Gamma,\Sigma,\mu)\) be a \(\sigma\)-finite measure space without atoms, with \(\mu(\Gamma)=\infty\). Let \(A\subseteq L^\infty(\Gamma,\mu)\) be the C\*-subalgebra generated by the projections \(1_E\) with \(\mu(E)<\infty\), that is, the closed linear span of these projections. Then:
1. for \(h\in A\) and \(\eta>0\), \(\mu(\{|h|>\eta\})<\infty\); in particular \(A\) is not unital;
2. for every \(h\in A_+\) there is a state \(\varphi\) of \(A\) with \(\varphi(h)=0\);
3. hence \(A\) has no strictly positive element and no sequential approximate identity (Proposition 13.3(6)), although it has the approximate identity of Theorem 11.4.

**Proof.** The span of the \(1_E\) is a \(*\)-algebra because \(1_E1_F=1_{E\cap F}\), so its closure is a commutative C\*-algebra.
(1) Choose a simple \(s=\sum_kc_k1_{E_k}\) with \(\mu(E_k)<\infty\) and \(\|h-s\|_\infty<\eta/2\). Up to a null set, \(\{|h|>\eta\}\subseteq\{|s|>\eta/2\}\subseteq\bigcup_kE_k\). If \(A\) had an identity \(e\), then \(e1_E=1_E\) for every \(E\) of finite measure, so \(e=1\) almost everywhere on each such \(E\), hence almost everywhere on \(\Gamma\) (\(\sigma\)-finiteness), and \(\mu(\{|e|>1/2\})=\infty\), contradicting (1).
(2) Let \(h\in A_+\), so \(h\geq0\) almost everywhere. By (1), \(F_n=\{h\leq1/n\}\) has infinite measure. Choose inductively \(E_n\subseteq F_n\setminus(E_1\cup\dots\cup E_{n-1})\) with \(0<\mu(E_n)<\infty\). This is possible because the set on the right has infinite measure, and a set of infinite measure in a \(\sigma\)-finite space contains a subset of positive finite measure. Since there are no atoms, \(E_n\) contains a set \(e_n\) with \(0<\mu(e_n)<2^{-n}\): a set of positive measure that is not an atom splits into two parts of positive measure, one of them of at most half the measure, and we repeat. The sets \(e_n\) are disjoint, and \(e=\bigcup_ne_n\) has \(\mu(e)\leq1\), so \(1_e\in A\). The functional \(\varphi_n(y)=\mu(e_n)^{-1}\int_{e_n}y\,d\mu\) is a state of \(A\), with \(\varphi_n(1_e)=1\) and \(0\leq\varphi_n(h)\leq1/n\). By the Banach–Alaoglu theorem the sequence has a weak\* cluster point \(\varphi\). It is positive, \(\|\varphi\|\leq1\), and \(\varphi(1_e)=1\), so \(\varphi\) is a state. For every \(N\) and \(\varepsilon>0\) there is \(n\geq N\) with \(|\varphi_n(h)-\varphi(h)|<\varepsilon\), so \(0\leq\varphi(h)<1/N+\varepsilon\). Hence \(\varphi(h)=0\).
(3) follows from (2) and Proposition 13.3(6). \(\square\)

**Example 13.5** (\(c_0\)). In \(c_0\), the sequences \(e_n=(1,\dots,1,0,0,\dots)\) (\(n\) ones) form an increasing contractive sequential approximate identity, and \(a=(1,\frac12,\frac13,\dots)\) is strictly positive. Indeed, a positive functional is \(\varphi(x)=\sum_k\varphi_kx_k\) with \(\varphi_k=\varphi(\delta_k)\geq0\) and \(\sum_k\varphi_k<\infty\) (by Lemma 13.1(1) and \(\|e_n\|=1\)), and \(\varphi(a)=\sum_k\varphi_k/k>0\) unless all \(\varphi_k=0\). Here \(\varphi(x)=\lim_n\varphi(e_nx)=\sum_k\varphi_kx_k\) uses that \((e_n)\) is an approximate identity.

**Exercise 13.6** (medium; \(\sigma\)-unital commutative algebras). Let \(X\) be an LCH space. Show that \(C_0(X)\) has a strictly positive element if and only if \(X\) is \(\sigma\)-compact. Deduce that \(C_0(X)\) has a sequential approximate identity exactly when \(X\) is \(\sigma\)-compact.

*Solution.* If \(a\in C_0(X)_+\) is strictly positive, then \(a(p)>0\) for every \(p\), since evaluation at \(p\) is a nonzero positive functional. So \(X=\bigcup_n\{a\geq1/n\}\), a countable union of compact sets. Conversely, let \(X=\bigcup_nK_n\) with \(K_n\) compact, and choose \(f_n\in C_c(X)\) with \(0\leq f_n\leq1\) and \(f_n=1\) on \(K_n\) ([Urysohn's lemma](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-16)). Then \(a=\sum_n2^{-n}f_n\) is positive at every point. For \(g\in C_0(X)\) and \(\eta>0\), \(|g|<\eta\) off a compact set \(C\), and \(a\geq c>0\) on \(C\). So \(\|g-f_\varepsilon(a)g\|\leq\max\big(\eta,\|g\|\varepsilon/(c+\varepsilon)\big)\), which is at most \(\eta\) for small \(\varepsilon\). By Proposition 13.3(3), \(a\) is strictly positive. The last claim is Proposition 13.3(5)–(6). So the algebra of Proposition 13.4 is \(C_0\) of a space that is not \(\sigma\)-compact.

### 12. Approximate identities of convolution algebras

Two Banach \(*\)-algebras built from a locally compact group, the group algebra \(L^1(G)\) and the transformation-group algebra, need not have an identity; both are constructed in [group algebras and transformation-group algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#oa-fnd-bn-20). This section shows that both have approximate identities of norm at most one. We use the lesson on Haar measure: \(G\) is a locally compact group with left Haar measure \(ds\) and modular function \(\Delta\) ([the modular function](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-07)). \(L^1(G)\), with convolution \(f*g(x)=\int f(y)g(y^{-1}x)\,dy\) and involution \(f^*(x)=\Delta(x)^{-1}\overline{f(x^{-1})}\), is a Banach \(*\)-algebra ([convolution and continuity of translation](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-12)). Translations are \(L_yf(x)=f(y^{-1}x)\) and \(R_yf(x)=f(xy)\).

**Proposition 12.1** (Approximate identities of \(L^1(G)\)). For each neighbourhood \(V\) of \(e\), let \(u_V\in L^1(G)\) satisfy \(u_V\geq0\), \(u_V=0\) off \(V\) and \(\int u_V=1\); continuity, compact support and symmetry are not required. Direct the neighbourhoods by reverse inclusion. Then \((u_V)\) is an approximate identity of \(L^1(G)\) with \(\|u_V\|_1=1\).

**Proof.** *Left.* For \(f\in L^1(G)\), \(\|u_V*f-f\|_1\leq\sup_{y\in V}\|L_yf-f\|_1\). This is the computation in the proof of [compactly supported approximate identities](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-13). That proof uses of \(\psi_U\) only that it is nonnegative with integral one and vanishes off \(U\); compact support serves only to make its nonzero set \(\sigma\)-finite, which holds for every integrable function. The right side tends to \(0\) by the continuity of translation in \(L^1(G)\).
*Right.* By the third formula for convolution in [convolution and continuity of translation](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-12), \(f*u(x)=\int f(xy^{-1})\,u(y)\,\Delta(y)^{-1}\,dy\). Put \(T_yf=\Delta(y)^{-1}R_{y^{-1}}f\). Right translation satisfies \(\|R_{y^{-1}}f\|_1=\Delta(y)\|f\|_1\) ([the modular function](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-07)), so \(T_y\) is an isometry of \(L^1(G)\), and
\[
\begin{gathered}
\|T_yf-f\|_1\\
\leq|\Delta(y)^{-1}-1|\,\|R_{y^{-1}}f\|_1+\|R_{y^{-1}}f-f\|_1\to0\\
(y\to e)
\end{gathered}
\]
by the continuity of \(\Delta\) and of translation. Since \(f*u_V-f=\int u_V(y)(T_yf-f)\,dy\) almost everywhere, the same Tonelli argument gives \(\|f*u_V-f\|_1\leq\sup_{y\in V}\|T_yf-f\|_1\to0\). \(\square\)

The lesson on Haar measure proves the right-hand statement for symmetric \(\psi_U\); the modular factor in \(T_y\) removes the need for symmetry.

**Proposition 12.2** (Approximate identities of the transformation-group algebra). Let \(\Omega\) be an LCH space on which \(G\) acts continuously from the right, \((\omega,s)\mapsto\omega s\). Let \(A\) be the completion of \(C_c(\Omega\times G)\) for \(\|x\|=\int_G\sup_\omega|x(\omega,s)|\,ds\), with the product \((xy)(\omega,s)=\int_Gx(\omega,t)\,y(\omega t,t^{-1}s)\,dt\). For each compact \(K\subseteq\Omega\) let \(f_K\in C_c(\Omega)\) with \(0\leq f_K\leq1\) and \(f_K=1\) on \(K\). For each neighbourhood \(V\) of \(e\) inside a fixed compact neighbourhood \(V_0\), let \(u_V\) be continuous, \(u_V\geq0\), \(u_V=0\) off \(V\), \(\int u_V=1\). Put \(u_{K,V}(\omega,s)=f_K(\omega)u_V(s)\), and direct the pairs by \(K\) increasing and \(V\) decreasing. Then \((u_{K,V})\) is an approximate identity of \(A\) with \(\|u_{K,V}\|\leq1\).

Restricting to \(V\subseteq V_0\) only makes \(u_{K,V}\) compactly supported; the directed set is unchanged far out, which is all that matters for convergence.

**Proof.** \(\|u_{K,V}\|=\int u_V\sup_\omega f_K\leq1\). Because the net is bounded, it is enough to prove \(u_{K,V}x\to x\) and \(xu_{K,V}\to x\) for \(x\in C_c(\Omega\times G)\) (a \(3\varepsilon\) argument). Let \(C\) be the support of \(x\), with projections \(C_\Omega\) and \(C_G\).
*Uniform continuity.* As \(t\to e\) and \(y\to e\),
\[
\begin{gathered}
\sup_{\omega,s}|x(\omega t,t^{-1}s)-x(\omega,s)|\to0,\\
\sup_{\omega,s}|x(\omega,sy^{-1})-x(\omega,s)|\to0 .
\end{gathered}
\]
If the first fails, there are \(\varepsilon>0\), a net \(t_\alpha\to e\) and points \((\omega_\alpha,s_\alpha)\) with the difference at least \(\varepsilon\). Then \((\omega_\alpha,s_\alpha)\) or \((\omega_\alpha t_\alpha,t_\alpha^{-1}s_\alpha)\) lies in \(C\) for every \(\alpha\); passing to a subnet, the same alternative holds throughout and those points converge in the compact set \(C\). By continuity of the action and of the group operations, the other point converges to the same limit, and both values of \(x\) converge to its value there, a contradiction. The second statement is proved the same way.
*Left.* For \(t\in V\subseteq V_0\), \(x(\omega t,t^{-1}s)\neq0\) forces \(\omega\in C_\Omega V_0^{-1}\) and \(s\in V_0C_G\), both compact. Once \(K\supseteq C_\Omega V_0^{-1}\cup C_\Omega\), \(f_K=1\) wherever either \(x(\omega,s)\) or the integrand is nonzero, so
\[
\begin{gathered}
(u_{K,V}x-x)(\omega,s)\\
=\int u_V(t)\big(x(\omega t,t^{-1}s)-x(\omega,s)\big)\,dt ,
\end{gathered}
\]
which vanishes for \(s\notin V_0C_G\) and is bounded by the first supremum, over \(t\in V\). So \[
\begin{gathered}
\|u_{K,V}x-x\|\\
\leq|V_0C_G|\sup_{t\in V,\omega,s}|x(\omega t,t^{-1}s)-x(\omega,s)|\to0,
\end{gathered}
\] where \(|\cdot|\) is Haar measure.
*Right.* \((xu_{K,V})(\omega,s)=\int x(\omega,t)f_K(\omega t)u_V(t^{-1}s)\,dt\). If \(x(\omega,t)\neq0\), then \(\omega t\in C_\Omega C_G\), a compact set; once \(K\supseteq C_\Omega C_G\), the factor \(f_K(\omega t)\) is \(1\). The change of variables behind the third formula for convolution ([convolution and continuity of translation](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-12)) gives
\[
\begin{gathered}
(xu_{K,V}-x)(\omega,s)\\
=\int u_V(y)\big(\Delta(y)^{-1}x(\omega,sy^{-1})-x(\omega,s)\big)\,dy ,
\end{gathered}
\]
which vanishes for \(s\notin C_GV_0\), and whose modulus is at most \[
\begin{gathered}
\sup_{y\in V}\big(|\Delta(y)^{-1}-1|\,\|x\|_\infty\\
+\sup_{\omega,s}|x(\omega,sy^{-1})-x(\omega,s)|\big).
\end{gathered}
\] This tends to \(0\), and so does \(\|xu_{K,V}-x\|\), which is at most \(|C_GV_0|\) times it. \(\square\)

### 14. The asymmetric Riesz decomposition

In an abelian C\*-algebra, \(A_h\) has the Riesz decomposition property, and by Theorem 10.2 no other C\*-algebra does. The following weaker decomposition holds in every C\*-algebra. We state it for families whose sums converge in norm; finite families are a special case.

**Theorem 14.1** (Asymmetric Riesz decomposition). Let \((x_i)_{i\in I}\) and \((y_j)_{j\in J}\) be families in a C\*-algebra \(A\) such that the sums \(\sum_ix_i^*x_i\) and \(\sum_jy_j^*y_j\) converge unconditionally in norm (the nets of finite partial sums converge) to the same element \(a\). Then there are \(z_{ij}\in A\) with
\[
\begin{gathered}
x_ix_i^*\\
=\sum_jz_{ij}^*z_{ij}\\
(i\in I),\\
y_jy_j^*\\
=\sum_iz_{ij}z_{ij}^*\\
(j\in J),
\end{gathered}
\tag{14.1}
\]
both sums converging unconditionally in norm.

**Proof.** Work in \(\widetilde A\). For \(t>0\) put \(u_t=f_t(a)=(a+t)^{-1}a\) and \(z_{ij,t}=y_j(a+t)^{-1}a^{1/2}x_i^*\in A\).
*Each \(z_{ij,t}\) converges as \(t\to0\).* Since \(y_j^*y_j\leq a\), Corollary 11.3(2), in its left form, gives \(\|y_j-y_ju_t\|\to0\). For \(s,t>0\) put \(d=(a+s)^{-1}-(a+t)^{-1}\), a self-adjoint function of \(a\) with \(da=u_s-u_t\). Using \(x_i^*x_i\leq a\) and Proposition 8.5(3),
\[
\begin{gathered}
(z_{ij,s}-z_{ij,t})(z_{ij,s}-z_{ij,t})^*\\
=y_jda^{1/2}x_i^*x_ia^{1/2}dy_j^*\\
\leq y_jda^2dy_j^*\\
=\big(y_j(u_s-u_t)\big)\big(y_j(u_s-u_t)\big)^* .
\end{gathered}
\]
So \(\|z_{ij,s}-z_{ij,t}\|\leq\|y_ju_s-y_ju_t\|\to0\) as \(s,t\to0\). Let \(z_{ij}=\lim_{t\to0}z_{ij,t}\).
*The second identity.* Fix \(j\), and for a finite \(F\subseteq I\) put \(R_F=a-\sum_{i\in F}x_i^*x_i\), which is positive, as a norm limit of finite sums of positive elements, and \(\|R_F\|\to0\) along \(F\). Since \[
\begin{gathered}
(y_ju_t)(y_ju_t)^*\\
=y_j(a+t)^{-1}a^{1/2}\,a\,a^{1/2}(a+t)^{-1}y_j^*,
\end{gathered}
\]
\[
\begin{gathered}
(y_ju_t)(y_ju_t)^*-\sum_{i\in F}z_{ij,t}z_{ij,t}^*\\
=g_tR_Fg_t^*,\\
g_t\\
=y_j(a+t)^{-1}a^{1/2}.
\end{gathered}
\]
Here \[
\begin{gathered}
\|g_t\|^2\\
=\|(a+t)^{-1}a^{1/2}y_j^*y_ja^{1/2}(a+t)^{-1}\|\\
\leq\|a^2(a+t)^{-2}\|\\
\leq1,
\end{gathered}
\] so the right side has norm at most \(\|R_F\|\). Let \(t\to0\): \(\|y_jy_j^*-\sum_{i\in F}z_{ij}z_{ij}^*\|\leq\|R_F\|\), which tends to \(0\).
*The first identity.* In the same way, with \(R'_{F'}=a-\sum_{j\in F'}y_j^*y_j\) and \(g'_t=x_ia^{1/2}(a+t)^{-1}\), we get \((x_iu_t)(x_iu_t)^*-\sum_{j\in F'}z_{ij,t}^*z_{ij,t}=g'_tR'_{F'}g_t'^*\), with \(\|g'_t\|\leq1\) because \(x_i^*x_i\leq a\). Since \(x_iu_t\to x_i\), the limit gives \(\|x_ix_i^*-\sum_{j\in F'}z_{ij}^*z_{ij}\|\leq\|R'_{F'}\|\). \(\square\)

For operators on a Hilbert space there is also a direct proof in the style of the polar decomposition; Exercise 14.3 gives it for finite families.

**Corollary 14.2.** If \(\sum_jy_j^*y_j\leq\sum_ix_i^*x_i\), with both sums as in the theorem, there are \(z_{ij}\) with \(y_jy_j^*=\sum_iz_{ij}z_{ij}^*\) and \(x_ix_i^*\geq\sum_jz_{ij}^*z_{ij}\).

**Proof.** Add to the family \((y_j)\) one element \(y_\star=\big(\sum_ix_i^*x_i-\sum_jy_j^*y_j\big)^{1/2}\), so that the two sums become equal. The theorem gives \(z_{ij}\) and \(z_{i\star}\) with \(x_ix_i^*=\sum_jz_{ij}^*z_{ij}+z_{i\star}^*z_{i\star}\geq\sum_jz_{ij}^*z_{ij}\). \(\square\)

**Exercise 14.3** (medium; Factorization of operators). (a) Let \(x:H\to K_1\) and \(y:H\to K_2\) be bounded operators between Hilbert spaces with \(x^*x\leq y^*y\). Then \(x=cy\) for some \(c:K_2\to K_1\) with \(\|c\|\leq1\), and \(c\) can be taken to vanish on the orthogonal complement of the range of \(y\). (b) Prove Theorem 14.1 for finite families in \(A=B(H)\) from (a).

*Solution.* (a) By Proposition 8.5(11) in \(B(H)\), \(\|x\xi\|^2=\langle x^*x\xi,\xi\rangle\leq\langle y^*y\xi,\xi\rangle=\|y\xi\|^2\). So \(c_0(y\xi)=x\xi\) is well defined and linear on the range of \(y\), with norm at most one. Extend it by continuity to the closure of the range, and by \(0\) on the orthogonal complement.
(b) Let \(\sum_{i\leq m}x_i^*x_i=\sum_{j\leq n}y_j^*y_j=a\) in \(B(H)\). The column operators \(X\xi=(x_i\xi)_i\) from \(H\) to \(H^m\) and \(Y\xi=(y_j\xi)_j\) from \(H\) to \(H^n\) satisfy \(X^*X=Y^*Y=a=(a^{1/2})^2\). By (a), \(X=Ca^{1/2}\), with \(C\) isometric on the closure of the range of \(a^{1/2}\), since \(\|X\xi\|=\|a^{1/2}\xi\|\), and zero on its complement. So \(C^*C=P\), the projection onto that closure, and \(Pa^{1/2}=a^{1/2}\). Writing \(C\) as a column \((c_i)\) gives \(x_i=c_ia^{1/2}\) and \(\sum_ic_i^*c_i=P\). In the same way \(y_j=d_ja^{1/2}\) with \(\sum_jd_j^*d_j=P\). Put \(z_{ij}=d_ja^{1/2}c_i^*\). Then
\[
\begin{gathered}
\sum_iz_{ij}z_{ij}^*\\
=d_ja^{1/2}Pa^{1/2}d_j^*\\
=d_jad_j^*\\
=y_jy_j^*,\\
\sum_jz_{ij}^*z_{ij}\\
=c_ia^{1/2}Pa^{1/2}c_i^*\\
=x_ix_i^* .
\end{gathered}
\]

## Results used from other lessons

- *Haar integration and convolution.* [Theorem 8.3 and Theorems 9.2–11.1 of the Haar lesson](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-05) give existence, uniqueness, the modular function and inversion for every locally compact group. [Theorem 5.1 there](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-10) proves Tonelli and Fubini for Borel functions with sigma-finite support in a Radon product; [Theorem 14.2](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-12) proves convolution bounds and translation continuity, and [Theorem 15.1](haar-measure-on-locally-compact-groups.md#oa-fnd-hm-13) proves compactly supported approximate identities. Section 12 extends the L1 approximate-identity argument to all nonnegative normalized functions supported in shrinking neighbourhoods, retaining the correct modular factor on the right.
- *Compact extension.* [Proposition 16.1(2) of the Stone–Weierstrass lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-18) proves norm-preserving extension from a closed subset of a compact Hausdorff space. It supplies the alternative commutative lifting argument in Section 17; the main lifting proof works for every C*-algebra.
- *The Banach–Alaoglu theorem* (Theorem 3.1 of [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html)). The closed unit ball of the dual of a normed space is compact for the weak\* topology. It is used in Section 13.
- *The closed graph theorem* (Theorem 5.3 and Remark 5.4 of [Hahn–Banach, Baire and the basic theorems on Banach spaces](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html)). A linear map between Banach spaces whose graph is closed is bounded. It holds for real Banach spaces too, so it applies to conjugate-linear maps between complex Banach spaces. It is used in Theorem 4.7.
- *Separation of convex sets* (Theorem 6.2 of the same lesson). It is used, over the real numbers, in the proof of Theorem 10.2.
- *The maximum modulus principle* (Theorem 3.6, Corollary 3.5 and Exercise 4 of [Cauchy's theorem for cycles and its consequences](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html)). A function that is continuous on the closed unit disc and holomorphic in the open disc attains the maximum of its modulus on the unit circle; and a uniform limit of holomorphic functions on an open set is holomorphic. They are used in Example 3.4.
- *Hilbert spaces* (Proposition 1.1 of [Hilbert spaces and compact operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html)). The Cauchy–Schwarz inequality for positive semidefinite sesquilinear forms, used in Lemma 13.1.

## Where this leads

The next step is the theory of states and representations: the Gelfand–Naimark–Segal construction, and the theorem that every C\*-algebra has a faithful representation on a Hilbert space . In von Neumann algebras the continuous functional calculus of normal elements extends to bounded Borel functions.

## References

- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).

*Freely accessible reading:* [B. Blackadar, *Operator Algebras*, II.1.6, II.2.2–II.3.2 and II.4–II.5](https://bruceblackadar.com/Mathematics/Cycr.pdf) gives a route through automatic continuity, continuous calculus, positive cones, ideals and quotients; the asymmetric Riesz proof is given fully here. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.

- [Emerson] H. Emerson, *An Introduction to C\*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts Basler Lehrbücher, Birkhäuser, Cham, 2024.
- [Fuglede 1950] B. Fuglede, A commutativity theorem for normal operators, *Proc. Nat. Acad. Sci. U.S.A.* 36 (1950), 35–40. https://pmc.ncbi.nlm.nih.gov/articles/PMC1063127/
- [Fukamiya 1952] M. Fukamiya, [On a theorem of Gelfand and Neumark and the B\*-algebra](https://www.sci.kumamoto-u.ac.jp/~kjm/BKS/kjmpdf/KJSM/v1-4-fukamiya.pdf), *Kumamoto J. Sci. Ser. A* 1 (1952), 17–22.
- [Fukamiya–Misonou–Takeda 1954] M. Fukamiya, M. Misonou and Z. Takeda, On order and commutativity of B\*-algebras, *Tôhoku Math. J.* (2) 6 (1954), 89–93. https://www.jstage.jst.go.jp/article/tmj1949/6/1/6_1_89/_article
- [Gelfand–Naimark 1943] I. Gelfand and M. Naimark, On the imbedding of normed rings into the ring of operators in Hilbert space, *Mat. Sbornik* 12 (1943), 197–217. https://www.mathnet.ru/eng/sm6155
- [Heinz 1951] E. Heinz, Beiträge zur Störungstheorie der Spektralzerlegung, *Math. Ann.* 123 (1951), 415–438. https://resolver.sub.uni-goettingen.de/purl?PPN235181684_0123%7CLOG_0037
- [Kelley–Vaught 1953] J. L. Kelley and R. L. Vaught, The positive cone in Banach algebras, *Trans. Amer. Math. Soc.* 74 (1953), 44–55. https://doi.org/10.1090/S0002-9947-1953-0054175-2
- [Löwner 1934] K. Löwner, Über monotone Matrixfunktionen, *Math. Z.* 38 (1934), 177–216. https://resolver.sub.uni-goettingen.de/purl?PPN266833020_0038%7CLOG_0014
- [Ogasawara 1955] T. Ogasawara, [A theorem on operator algebras](https://projecteuclid.org/journals/hiroshima-mathematical-journal/volume-18/issue-3/A-Theorem-on-Operator-Algebras/10.32917/hmj/1556935304.full), *J. Sci. Hiroshima Univ. Ser. A* 18 (1955), 307–309.
- [Sherman 1951] S. Sherman, Order in operator algebras, *Amer. J. Math.* 73 (1951), 227–232.
- [Takesaki I] M. Takesaki, *Theory of Operator Algebras I*, Springer, New York, 1979; reprinted as Encyclopaedia of Mathematical Sciences 124, Springer, Berlin, 2002.
