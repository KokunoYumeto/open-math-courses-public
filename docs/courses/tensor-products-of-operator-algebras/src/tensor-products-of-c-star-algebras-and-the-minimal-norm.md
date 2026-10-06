# Tensor products of C\*-algebras and the minimal norm

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The algebraic tensor product \(A\odot B\) of two C\*-algebras is a \(*\)-algebra. Represent \(A\) and \(B\) faithfully on Hilbert spaces \(H\) and \(K\), let \(A\odot B\) act on \(H\otimes K\), and take the operator norm. This lesson proves four facts about this norm. It does not depend on the representations (Theorem 2.2); it is the *minimal* norm, written \(\|\cdot\|_{\min}\). It is the smallest C\*-norm on \(A\odot B\), and every C\*-norm on \(A\odot B\) satisfies \(\gamma(a\otimes b)=\|a\|\|b\|\) (Theorem 4.4). For a factor \(M\) on \(H\), the product map \(M\odot M'\to B(H)\), \(a\otimes b\mapsto ab\), is injective (Theorem 5.1). And the completion \(A\otimes_{\min}B\) of two simple C\*-algebras is simple (Theorem 5.2).

The minimal norm goes back to [Turumaru 1952]; its minimality and the simplicity theorem are due to Takesaki [Takesaki 1958], [Takesaki 1964], and the injectivity for factors to Murray and von Neumann. The proof of minimality follows the outline in [Blackadar, II.9.5.1]: product states of a pure state and an arbitrary state extend to every C\*-completion, first for a commutative second factor. The proofs of Theorems 5.1 and 5.2 follow Takesaki's textbook treatment. The general treatment of C\*-tensor products is in [Blackadar, Section II.9].

We assume the lessons C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients, Representations and positive linear functionals, Spatial tensor products of von Neumann algebras (Sections 1 and 2 only), and the results listed in Section 1.

## 1. Conventions and results used

C\*-algebras are complex. For a C\*-algebra \(A\), \(\tilde A\) is \(A\) itself if \(A\) has a unit and the unitization \(A\oplus\mathbb C\) otherwise; in both cases \(A\) is an ideal of \(\tilde A\). The *algebraic tensor product* \(A\odot B\) is the tensor product of vector spaces, with the product \((a\otimes b)(a'\otimes b')=aa'\otimes bb'\) and the involution \((a\otimes b)^*=a^*\otimes b^*\). If \(b_1,\dots,b_n\) are linearly independent and \(\sum_ia_i\otimes b_i=0\), then all \(a_i=0\); and if \(\alpha\) and \(\beta\) are injective linear maps, so is \(\alpha\odot\beta\). A *C\*-seminorm* on a \(*\)-algebra is a seminorm \(\gamma\) with \(\gamma(xy)\le\gamma(x)\gamma(y)\), \(\gamma(x^*)=\gamma(x)\) and \(\gamma(x^*x)=\gamma(x)^2\); a *C\*-norm* if it is a norm. The completion of a \(*\)-algebra in a C\*-norm is a C\*-algebra. A *representation* is a \(*\)-homomorphism into some \(B(H)\); it is *faithful* if it is injective and *nondegenerate* if the vectors \(\pi(x)\xi\) span a dense subspace.

**Fact 1.1** (C\*-algebras). From C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients:

- (a) a \(*\)-homomorphism between C\*-algebras is contractive, and an injective one is isometric with closed range (Theorem 4.2 and Corollary 4.6); consequently a C\*-norm on a C\*-algebra is its norm, because the identity map into the completion is an injective \(*\)-homomorphism;
- (b) a commutative C\*-algebra \(D\) with unit is \(*\)-isomorphic to \(C(\Omega)\) by the Gelfand transform \(d\mapsto(\chi\mapsto\chi(d))\), \(\Omega\) its compact space of characters; the characters of \(C(X)\), \(X\) compact, are the point evaluations (Theorem 2.1 and Proposition 2.2); the spectrum of an element is the same in every C\*-subalgebra containing it (Theorem 3.2); a \(*\)-homomorphism \(\rho\) satisfies \(\rho(p(h))=p(\rho(h))\) for self-adjoint \(h\) and continuous \(p\) on the spectrum with \(p(0)=0\) when no unit is present (Corollary 5.4); and \(\|p(h)\|=\max_{\sigma(h)}|p|\);
- (c) \(x^*x\ge0\) for every \(x\); if \(0\le s\le t\) then \(\|s\|\le\|t\|\) and \(y^*sy\le y^*ty\); if \(0\le z\le1\) commutes with \(a\ge0\), then \(0\le a^{1/2}za^{1/2}\le a\); every \(t\ge0\) has a positive square root, and \(\|t\|1-t\ge0\) in \(\tilde A\) for self-adjoint \(t\) (Theorem 8.2 and Proposition 8.5);
- (d) every C\*-algebra has an approximate identity \((e_\lambda)\) of positive contractions: \(e_\lambda x\to x\) and \(xe_\lambda\to x\) for every \(x\) (Theorem 11.4);
- (e) the quotient of a C\*-algebra by a closed ideal is a C\*-algebra, and the kernel of a \(*\)-homomorphism is a closed ideal (Theorem 15.1 and Corollary 15.4).

**Fact 1.2** (states and representations). From Representations and positive linear functionals, for a C\*-algebra \(A\):

- (a) a positive functional \(\omega\) on a unital \(A\) has \(\|\omega\|=\omega(1)\) (Theorem 4.7);
- (b) every state \(\omega\) has a GNS triple \((\pi_\omega,H_\omega,\xi_\omega)\): a representation with a cyclic vector and \(\omega(x)=\langle\pi_\omega(x)\xi_\omega,\xi_\omega\rangle\) (Theorems 5.3 and 5.4);
- (c) a state \(\varphi\) is *pure* if every positive functional \(\psi\le\varphi\) is a multiple of \(\varphi\); if \(A\) is unital, the set \(S(A)\) of states is weak\*-compact and convex and is the weak\*-closed convex hull of the set \(P(A)\) of pure states (Definition 8.2 and Proposition 8.4);
- (d) the direct sum of the GNS representations of all pure states is faithful; a nonzero C\*-algebra has an irreducible representation; a representation is irreducible exactly when it is nonzero and its commutant is \(\mathbb C1\) (Theorem 8.5 and Corollary 2.3); every C\*-algebra has a faithful nondegenerate representation, for instance the direct sum of the GNS representations of all states (Theorem 7.2).

**Fact 1.3** (extending states). Let \(D\) be a C\*-subalgebra of a unital C\*-algebra \(E\) with \(1\in D\). A bounded functional \(f\) on \(E\) with \(f(1)=\|f\|\) is positive (Projections and types of von Neumann algebras, Lemma 17.1, with \(h=1\)). So a state of \(D\) extends to a state of \(E\): extend it with the same norm by the Hahn–Banach theorem (Hahn–Banach, Baire and the basic theorems on Banach spaces, Corollary 2.3). By the same theorem, applied in the locally convex space \(E^*\) with the weak\* topology, whose continuous linear functionals are the evaluations at elements of \(E\) (Weak topologies, Tychonoff, Banach–Alaoglu, Krein–Milman and Eberlein–Šmulian), a point outside a weak\*-closed convex set of functionals is separated from it by the real part of evaluation at some element.

**Fact 1.4** (Hilbert tensor products). From Spatial tensor products of von Neumann algebras:

- (a) for \(a\in B(H)\) and \(b\in B(K)\) there is a unique \(a\otimes b\in B(H\otimes K)\) with \((a\otimes b)(\xi\otimes\eta)=a\xi\otimes b\eta\); \(\|a\otimes b\|=\|a\|\|b\|\), \((a\otimes b)(c\otimes d)=ac\otimes bd\) and \((a\otimes b)^*=a^*\otimes b^*\); the vectors \(\xi\otimes\eta\) with \(\xi\) and \(\eta\) in total sets are total (Propositions 1.3(1) and 2.1(1));
- (b) for an orthonormal basis \((f_j)\) of \(K\), with \(R_j\xi=\xi\otimes f_j\), every \(X\in B(H\otimes K)\) is determined by its matrix \(X_{jk}=R_j^*XR_k\in B(H)\), and \(X\) commutes with every \(s\otimes1\), \(s\in S\), exactly when every \(X_{jk}\) lies in \(S'\) (Proposition 2.1(2), (3)).

**Fact 1.5** (commutants). From The double commutant theorem: the projection onto a closed subspace invariant under a self-adjoint set \(S\) lies in \(S'\) (Proposition 2.1(5)). If \(M\) is a factor on \(H\), then \((M\cup M')''=B(H)\): indeed \((M\cup M')'=M'\cap M''=M'\cap M=\mathbb C1\).

## 2. The spatial norm

For representations \(\pi\) of \(A\) on \(H\) and \(\rho\) of \(B\) on \(K\), the bilinear map \((a,b)\mapsto\pi(a)\otimes\rho(b)\) defines a linear map \(\pi\otimes\rho:A\odot B\to B(H\otimes K)\), and by Fact 1.4(a) it is a \(*\)-homomorphism.

**Lemma 2.1.** If \(\pi\) and \(\rho\) are faithful, then \(\pi\otimes\rho\) is injective.

**Proof.** Let \(x=\sum_{i=1}^na_i\otimes b_i\) with linearly independent \(b_i\), and suppose \((\pi\otimes\rho)(x)=0\). For \(\xi,\xi'\in H\) and \(\eta,\eta'\in K\),
\[
0=\langle(\pi\otimes\rho)(x)(\xi\otimes\eta),\xi'\otimes\eta'\rangle=\sum_i\langle\pi(a_i)\xi,\xi'\rangle\langle\rho(b_i)\eta,\eta'\rangle .
\]
The operators \(\rho(b_i)\) are linearly independent, so the vectors \((\langle\rho(b_i)\eta,\eta'\rangle)_{i=1}^n\in\mathbb C^n\) span \(\mathbb C^n\): a vector \((c_i)\) with \(\sum_ic_i\langle\rho(b_i)\eta,\eta'\rangle=0\) for all \(\eta,\eta'\) has \(\sum_ic_i\rho(b_i)=0\), so \(c=0\). Hence \(\langle\pi(a_i)\xi,\xi'\rangle=0\) for all \(i\), \(\xi\) and \(\xi'\), so \(\pi(a_i)=0\) and \(a_i=0\). \(\square\)

**Theorem 2.2** (Independence of the representations). Let \(x\in A\odot B\). The number \(\|(\pi\otimes\rho)(x)\|\) is the same for all faithful representations \(\pi\) of \(A\) and \(\rho\) of \(B\). It defines a C\*-norm on \(A\odot B\), the *minimal* or *spatial* norm \(\|x\|_{\min}\). The completion \(A\otimes_{\min}B\) is identified with the norm closure of \((\pi\otimes\rho)(A\odot B)\) in \(B(H\otimes K)\).

**Proof.** Let \(x=\sum_{i=1}^na_i\otimes b_i\), let \(\rho\) be a representation of \(B\) on \(K\), and let \(\sigma\) be any representation of \(A\) on \(L\). For a finite orthonormal family \(\eta=(\eta_1,\dots,\eta_m)\) in \(K\), let \(X_\eta\) be the \(m\times m\) matrix over \(A\) with entries \(X_{\eta,kl}=\sum_ia_i\langle\rho(b_i)\eta_l,\eta_k\rangle\), and let \(\sigma_m(X_\eta)\) be the operator on \(L^m\) with the matrix \([\sigma(X_{\eta,kl})]\). Identify \(L^m\) with the subspace \(L\otimes\operatorname{span}\{\eta_k\}\) of \(L\otimes K\) by \((\xi_k)\mapsto\sum_k\xi_k\otimes\eta_k\). Since
\[
\langle(\sigma\otimes\rho)(x)(\xi\otimes\eta_l),\xi'\otimes\eta_k\rangle=\sum_i\langle\sigma(a_i)\xi,\xi'\rangle\langle\rho(b_i)\eta_l,\eta_k\rangle=\langle\sigma(X_{\eta,kl})\xi,\xi'\rangle ,
\]
\(\sigma_m(X_\eta)\) is the compression of \(T=(\sigma\otimes\rho)(x)\) to this subspace, and \(\|\sigma_m(X_\eta)\|\le\|T\|\). Every finite sum of elementary tensors in \(L\otimes K\) lies in such a subspace: apply the Gram–Schmidt process to the vectors of \(K\) that occur. These finite sums are dense (Fact 1.4(a)), and two of them lie in a common subspace of this kind. As \(\|T\|=\sup|\langle T\zeta,\zeta'\rangle|\) over unit vectors \(\zeta,\zeta'\) in a dense subspace, \(\|T\|=\sup_\eta\|\sigma_m(X_\eta)\|\).

Now let \(\pi_1\) and \(\pi_2\) be faithful representations of \(A\) on \(H_1\) and \(H_2\). The matrices with entries in \(\pi_k(A)\) form a \(*\)-subalgebra \(M_m(\pi_k(A))\) of \(B(H_k^m)\). It is norm closed, since \(\pi_k(A)\) is closed (Fact 1.1(a)) and every entry of a matrix operator has norm at most the norm of the operator. So it is a C\*-algebra, and \([\pi_1(y_{kl})]\mapsto[\pi_2(y_{kl})]\) is an injective \(*\)-homomorphism between two C\*-algebras, hence isometric (Fact 1.1(a)). Therefore \(\|(\pi_1)_m(X_\eta)\|=\|(\pi_2)_m(X_\eta)\|\) for every \(\eta\), and \(\|(\pi_1\otimes\rho)(x)\|=\|(\pi_2\otimes\rho)(x)\|\). The unitary \(H\otimes K\to K\otimes H\), \(\xi\otimes\eta\mapsto\eta\otimes\xi\), carries \((\pi\otimes\rho)(\sum a_i\otimes b_i)\) to \((\rho\otimes\pi)(\sum b_i\otimes a_i)\); so the norm does not depend on \(\rho\) either. Faithful representations exist (Fact 1.2(d)). By Lemma 2.1 and Fact 1.4(a), \(x\mapsto\|(\pi\otimes\rho)(x)\|\) is a C\*-norm. \(\square\)

**Corollary 2.3.**

1. \(\|a\otimes b\|_{\min}=\|a\|\|b\|\).
2. Let \(\alpha:A\to A_1\) and \(\beta:B\to B_1\) be \(*\)-homomorphisms. Then \(\alpha\odot\beta\) extends to a \(*\)-homomorphism \(A\otimes_{\min}B\to A_1\otimes_{\min}B_1\). If \(\alpha\) and \(\beta\) are injective, it is isometric. In particular \(A\otimes_{\min}B\subseteq A_1\otimes_{\min}B_1\) isometrically when \(A\subseteq A_1\) and \(B\subseteq B_1\) are C\*-subalgebras, and \(\alpha\otimes\mathrm{id}\) is isometric for every \(*\)-automorphism \(\alpha\) of \(A\).

**Proof.** (1) is Fact 1.4(a). (2) If \(\pi_1\) and \(\rho_1\) are faithful representations of \(A_1\) and \(B_1\) and \(\alpha,\beta\) are injective, then \(\pi_1\circ\alpha\) and \(\rho_1\circ\beta\) are faithful representations of \(A\) and \(B\), and \(((\pi_1\circ\alpha)\otimes(\rho_1\circ\beta))(x)=(\pi_1\otimes\rho_1)((\alpha\odot\beta)(x))\); Theorem 2.2 gives \(\|(\alpha\odot\beta)(x)\|_{\min}=\|x\|_{\min}\). In general, \(\alpha\) is the composite of the quotient map \(q:A\to A/\ker\alpha\) with an injective \(*\)-homomorphism (Fact 1.1(e)), and likewise \(\beta\). So it remains to show that \(q\odot\mathrm{id}\) is contractive for the minimal norms. Let \(\pi\) be a faithful representation of \(A\) on \(H\), \(\sigma\) one of \(A/\ker\alpha\) on \(L\), and \(\rho\) one of \(B\) on \(K\). Then \(\pi\oplus(\sigma\circ q)\) is a faithful representation of \(A\) on \(H\oplus L\), and \(((\pi\oplus\sigma q)\otimes\rho)(x)=(\pi\otimes\rho)(x)\oplus(\sigma q\otimes\rho)(x)\) on \((H\otimes K)\oplus(L\otimes K)\). Hence \(\|(q\odot\mathrm{id})(x)\|_{\min}=\|(\sigma\otimes\rho)((q\odot\mathrm{id})(x))\|=\|(\sigma q\otimes\rho)(x)\|\le\|x\|_{\min}\). \(\square\)

## 3. C\*-norms on tensor products with a unit

**Lemma 3.1** (Cross norms). Let \(A\) and \(B\) be unital, \(\gamma\) a C\*-norm on \(A\odot B\), and \(E\) the completion. Then \(a\mapsto a\otimes1\) and \(b\mapsto1\otimes b\) are isometric \(*\)-homomorphisms of \(A\) and \(B\) into \(E\) with commuting ranges, and \(\gamma(a\otimes b)=\|a\|\|b\|\) for all \(a\in A\), \(b\in B\).

**Proof.** The map \(a\mapsto a\otimes1\) is an injective \(*\)-homomorphism of the C\*-algebra \(A\) into \(E\), hence isometric (Fact 1.1(a)); so is \(b\mapsto1\otimes b\). The ranges commute, since \((a\otimes1)(1\otimes b)=a\otimes b=(1\otimes b)(a\otimes1)\). Hence \(\gamma(a\otimes b)\le\|a\|\|b\|\).

For the reverse inequality it suffices to show \(\gamma(h\otimes k)\ge\|h\|\|k\|\) for \(h\ge0\) and \(k\ge0\), because \(\gamma(a\otimes b)^2=\gamma(a^*a\otimes b^*b)\), \(\|a^*a\|=\|a\|^2\) and \(\|b^*b\|=\|b\|^2\). Put \(s=h\otimes1\) and \(t=1\otimes k\), commuting positive elements of \(E\). The C\*-subalgebra \(D\) of \(E\) generated by \(1\), \(s\) and \(t\) is commutative, so \(D\cong C(\Omega)\) (Fact 1.1(b)). The spectra of \(s\) and \(t\) are \(\sigma(h)\) and \(\sigma(k)\), by Fact 1.1(b) and the isometric embeddings. A character of \(D\) is determined by its values at \(s\) and \(t\), so \(\chi\mapsto(\chi(s),\chi(t))\) is a continuous injection of the compact space \(\Omega\) into \(\sigma(h)\times\sigma(k)\), a homeomorphism onto a closed set \(\Omega'\). Suppose some \((\lambda_0,\mu_0)\in\sigma(h)\times\sigma(k)\) is not in \(\Omega'\). Choose open sets \(U\ni\lambda_0\) and \(V\ni\mu_0\) with \((U\times V)\cap\Omega'=\varnothing\), and continuous functions \(p,q\) on \(\mathbb R\) with values in \([0,1]\), \(p(\lambda_0)=q(\mu_0)=1\), vanishing outside \(U\) and \(V\). Then \(p(h)\ne0\) and \(q(k)\ne0\), so \(p(h)\otimes q(k)\ne0\) in \(A\odot B\). Its image in \(E\) is \(p(s)q(t)\) (Fact 1.1(b)), whose Gelfand transform \(\chi\mapsto p(\chi(s))q(\chi(t))\) vanishes on \(\Omega\). So \(\gamma(p(h)\otimes q(k))=0\), which contradicts that \(\gamma\) is a norm. Hence \(\Omega'=\sigma(h)\times\sigma(k)\), and
\[
\gamma(h\otimes k)=\|st\|=\max_{\chi\in\Omega}|\chi(s)\chi(t)|=\max_{\lambda\in\sigma(h),\ \mu\in\sigma(k)}|\lambda\mu|=\|h\|\|k\| . \qquad\square
\]

**Lemma 3.2** (A commutative factor). Let \(A\) be unital and \(X\) a compact Hausdorff space. For \(x=\sum_ia_i\otimes f_i\in A\odot C(X)\) and \(t\in X\) put \(x(t)=\sum_if_i(t)a_i\). Then \(\|x\|_{\min}=\max_{t\in X}\|x(t)\|\), and \(\gamma(x)\ge\|x\|_{\min}\) for every C\*-norm \(\gamma\) on \(A\odot C(X)\).

**Proof.** Let \(\pi\) be a faithful representation of \(A\) on \(H\), and represent \(C(X)\) faithfully on \(\ell^2(X)\) by \(M_f\delta_s=f(s)\delta_s\). With the basis \((\delta_s)\), Fact 1.4(b) shows that \((\pi\otimes M)(x)\) maps each subspace \(H\otimes\delta_s\) into itself and acts there as \(\pi(x(s))\): \((\pi(a)\otimes M_f)(\xi\otimes\delta_s)=f(s)\pi(a)\xi\otimes\delta_s\). So it is the direct sum of the \(\pi(x(s))\), and its norm is \(\sup_s\|x(s)\|\), a maximum because \(s\mapsto x(s)\) is continuous. This is \(\|x\|_{\min}\) by Theorem 2.2.

Let \(\gamma\) be a C\*-norm, \(t\in X\) and \(\varepsilon>0\). Choose an open \(U\ni t\) with \(|f_i(s)-f_i(t)|\le\varepsilon/(1+\sum_j\|a_j\|)\) for \(s\in U\) and every \(i\), and \(g\in C(X)\) with \(0\le g\le1\), \(g(t)=1\) and \(g=0\) outside \(U\). Then
\[
x(1\otimes g)-x(t)\otimes g=\sum_ia_i\otimes(f_i-f_i(t))g ,
\]
and by Lemma 3.1 each term has \(\gamma\)-norm \(\|a_i\|\,\|(f_i-f_i(t))g\|_\infty\le\|a_i\|\varepsilon/(1+\sum_j\|a_j\|)\). Lemma 3.1 also gives \(\gamma(x(t)\otimes g)=\|x(t)\|\) and \(\gamma(x(1\otimes g))\le\gamma(x)\gamma(1\otimes g)=\gamma(x)\). Hence \(\|x(t)\|\le\gamma(x)+\varepsilon\). \(\square\)

## 4. Minimality of the spatial norm

**Lemma 4.1** (Pure states and commuting elements). Let \(E\) be a unital C\*-algebra, \(A\subseteq E\) a C\*-subalgebra with \(1\in A\), and \(\omega\) a state of \(E\) whose restriction \(\varphi\) to \(A\) is pure. If \(z\in E\) commutes with \(A\), then \(\omega(az)=\varphi(a)\omega(z)\) for every \(a\in A\).

**Proof.** Both sides are linear in \(z\). Since \(A\) is self-adjoint, \(z^*\) commutes with \(A\), and so do the real and imaginary parts of \(z\) and, for self-adjoint \(w\) commuting with \(A\), the positive and negative parts \(w_\pm\), which are norm limits of polynomials in \(w\) without constant term. So we may assume \(0\le z\le1\). For \(a\ge0\) in \(A\), \(az=a^{1/2}za^{1/2}\) and \(0\le a^{1/2}za^{1/2}\le a\) (Fact 1.1(c)). So \(\psi(a)=\omega(az)\) is a positive functional on \(A\) with \(\psi\le\varphi\). By purity \(\psi=\lambda\varphi\), and \(a=1\) gives \(\lambda=\omega(z)\). \(\square\)

**Theorem 4.2** (Minimality with units). Let \(A\) and \(B\) be unital and \(\gamma\) a C\*-norm on \(A\odot B\). Then \(\|x\|_{\min}\le\gamma(x)\) for every \(x\in A\odot B\).

**Proof.** Let \(E\) be the completion. Say that a pair of states \((\varphi,\psi)\) of \(A\) and \(B\) *extends* if some state \(\omega\) of \(E\) has \(\omega(a\otimes b)=\varphi(a)\psi(b)\) for all \(a,b\).

*Step 1.* Fix a pure state \(\varphi\) of \(A\), and let \(S_\varphi\) be the set of states \(\psi\) of \(B\) such that \((\varphi,\psi)\) extends. It is convex: a convex combination of extensions extends the convex combination. It is weak\*-closed: if \(\psi_\alpha\to\psi\) and \(\omega_\alpha\) extends \((\varphi,\psi_\alpha)\), a weak\*-cluster point of \((\omega_\alpha)\) in the weak\*-compact state space of \(E\) extends \((\varphi,\psi)\).

*Step 2: \(S_\varphi\) is large.* Let \(b\in B\) be positive. The C\*-subalgebra \(C\) of \(B\) generated by \(1\) and \(b\) is \(C(\sigma(b))\) (Fact 1.1(b)), and evaluation at \(\|b\|\in\sigma(b)\) is a character \(\chi\) of \(C\) with \(\chi(b)=\|b\|\). The restriction of \(\gamma\) to \(A\odot C\) is a C\*-norm, so by Lemma 3.2, for \(x\in A\odot C\),
\[
|\varphi(x(\|b\|))|\le\|x(\|b\|)\|\le\|x\|_{\min}\le\gamma(x),
\]
where \(x(\|b\|)=(\mathrm{id}\odot\chi)(x)\). So the functional \(x\mapsto\varphi((\mathrm{id}\odot\chi)(x))\) extends to the closure \(D\) of \(A\odot C\) in \(E\) with norm at most \(1\) and value \(1\) at the unit; it is a state of \(D\) (Fact 1.3). Extend it to a state \(\omega\) of \(E\) (Fact 1.3). The restriction of \(\omega\) to \(A\otimes1\cong A\) is the pure state \(\varphi\), and the elements \(1\otimes y\), \(y\in B\), commute with \(A\otimes1\). By Lemma 4.1, \(\omega(a\otimes y)=\varphi(a)\omega(1\otimes y)\). So \(\psi=\omega(1\otimes\,\cdot\,)\) is a state of \(B\) in \(S_\varphi\), and \(\psi(b)=\omega(1\otimes b)=\chi(b)=\|b\|\).

*Step 3: \(S_\varphi=S(B)\).* Let \(\sigma\) be a state of \(B\) outside \(S_\varphi\). By Fact 1.3 there is \(b\in B\) with \(\operatorname{Re}\sigma(b)>\sup_{\psi\in S_\varphi}\operatorname{Re}\psi(b)\). States are hermitian, so with \(h=\frac12(b+b^*)\) this reads \(\sigma(h)>\sup_{S_\varphi}\psi(h)\), and with the positive element \(c=h+\|h\|1\) it reads \(\sigma(c)>\sup_{S_\varphi}\psi(c)=\|c\|\), by Step 2. But \(\sigma(c)\le\|c\|\). So \(S_\varphi=S(B)\).

*Step 4: the estimate.* Let \(\varphi\) and \(\psi\) be pure states of \(A\) and \(B\), with GNS triples \((\pi_\varphi,H_\varphi,\xi_\varphi)\) and \((\pi_\psi,H_\psi,\xi_\psi)\), and let \(\omega\) be a state of \(E\) extending \((\varphi,\psi)\) (Step 3). For \(x,y\in A\odot B\) put \(\zeta=(\pi_\varphi\otimes\pi_\psi)(y)(\xi_\varphi\otimes\xi_\psi)\). Since \(\langle(\pi_\varphi\otimes\pi_\psi)(a\otimes b)(\xi_\varphi\otimes\xi_\psi),\xi_\varphi\otimes\xi_\psi\rangle=\varphi(a)\psi(b)=\omega(a\otimes b)\),
\[
\|(\pi_\varphi\otimes\pi_\psi)(x)\zeta\|^2=\omega(y^*x^*xy)\le\gamma(x^*x)\,\omega(y^*y)=\gamma(x)^2\|\zeta\|^2 ,
\]
using \(y^*x^*xy\le\|x^*x\|\,y^*y\) in \(E\) (Fact 1.1(c)). The vectors \(\zeta\) span the algebraic tensor product of the dense subspaces \(\pi_\varphi(A)\xi_\varphi\) and \(\pi_\psi(B)\xi_\psi\), which is dense in \(H_\varphi\otimes H_\psi\) (Fact 1.4(a)). So \(\|(\pi_\varphi\otimes\pi_\psi)(x)\|\le\gamma(x)\). Let \(\pi=\bigoplus_\varphi\pi_\varphi\) and \(\rho=\bigoplus_\psi\pi_\psi\), over all pure states; they are faithful (Fact 1.2(d)). On \((\bigoplus H_\varphi)\otimes(\bigoplus H_\psi)=\bigoplus_{\varphi,\psi}H_\varphi\otimes H_\psi\), the operator \((\pi\otimes\rho)(x)\) is the direct sum of the \((\pi_\varphi\otimes\pi_\psi)(x)\). By Theorem 2.2, \(\|x\|_{\min}=\sup_{\varphi,\psi}\|(\pi_\varphi\otimes\pi_\psi)(x)\|\le\gamma(x)\). \(\square\)

**Lemma 4.3** (Adjoining units). Let \(E\) be a C\*-algebra that contains \(A\odot B\) as a dense \(*\)-subalgebra, with a C\*-norm, and let \(\pi\) be a nondegenerate representation of \(E\) on \(H\).

1. There is a representation \(\tilde\pi\) of \(\tilde A\odot\tilde B\) on \(H\) with \(\tilde\pi(x)=\pi(x)\) for \(x\in A\odot B\). So \(\pi_1(a)=\tilde\pi(a\otimes1)\) and \(\pi_2(b)=\tilde\pi(1\otimes b)\) are representations of \(A\) and \(B\) with commuting ranges and \(\pi(a\otimes b)=\pi_1(a)\pi_2(b)\).
2. If \(\pi\) is faithful, then \(\tilde\pi\) is injective, and \(\tilde\gamma(z)=\|\tilde\pi(z)\|\) is a C\*-norm on \(\tilde A\odot\tilde B\) that agrees with the norm of \(E\) on \(A\odot B\).

**Proof.** (1) *Left multiplication is bounded.* Write \(\gamma\) for the norm of \(E\) on \(A\odot B\). For \(z\in\tilde A\odot\tilde B\) and \(x\in A\odot B\), \(zx\in A\odot B\), because \(A\) and \(B\) are ideals of \(\tilde A\) and \(\tilde B\). Let \(\alpha\in\tilde A\). By Fact 1.1(c), \(\|\alpha\|^21-\alpha^*\alpha=c^*c\) for some \(c\in\tilde A\). For \(x\in A\odot B\) this gives the identity
\[
((\alpha\otimes1)x)^*((\alpha\otimes1)x)=\|\alpha\|^2x^*x-((c\otimes1)x)^*((c\otimes1)x)
\]
in \(A\odot B\), hence \(((\alpha\otimes1)x)^*((\alpha\otimes1)x)\le\|\alpha\|^2x^*x\) in \(E\) and \(\gamma((\alpha\otimes1)x)\le\|\alpha\|\gamma(x)\) (Fact 1.1(c)). The same holds for \(1\otimes\beta\), \(\beta\in\tilde B\). Every \(z\) is a finite sum of products \((\alpha\otimes1)(1\otimes\beta)\), so \(x\mapsto zx\) extends to a bounded operator \(L_z\) on \(E\), and \(L_z(uv)=L_z(u)v\) for \(u,v\in E\), by continuity from \(A\odot B\).

*The representation.* Let \((e_\lambda)\) be an approximate identity of \(E\) (Fact 1.1(d)). For \(u_1,\dots,u_r\in E\) and \(\xi_1,\dots,\xi_r\in H\), put \(\zeta=\sum_j\pi(u_j)\xi_j\). Then
\[
\sum_j\pi(L_zu_j)\xi_j=\lim_\lambda\sum_j\pi(L_z(e_\lambda u_j))\xi_j=\lim_\lambda\pi(L_z(e_\lambda))\zeta ,
\]
and \(\|\pi(L_z(e_\lambda))\|\le\|L_z\|\). So \(\tilde\pi(z)\zeta=\sum_j\pi(L_zu_j)\xi_j\) is well defined on the dense subspace of such vectors (nondegeneracy) and bounded by \(\|L_z\|\); it extends to \(H\). The map \(\tilde\pi\) is linear and multiplicative, since \(L_{zz'}=L_zL_{z'}\). It preserves adjoints: \(\langle\tilde\pi(z)\pi(u)\xi,\pi(v)\eta\rangle=\langle\pi(v^*(zu))\xi,\eta\rangle=\langle\pi((z^*v)^*u)\xi,\eta\rangle=\langle\pi(u)\xi,\tilde\pi(z^*)\pi(v)\eta\rangle\), where \(v^*(zu)=(z^*v)^*u\) holds on \(A\odot B\) and extends by continuity. For \(x\in A\odot B\), \(L_xu=xu\), so \(\tilde\pi(x)=\pi(x)\). The rest of (1) follows, since \(a\otimes b=(a\otimes1)(1\otimes b)=(1\otimes b)(a\otimes1)\) in \(\tilde A\odot\tilde B\).

(2) Let \(\tilde\pi(z)=0\). Then \(\pi(zx)=\tilde\pi(z)\pi(x)=0\), so \(zx=0\) for every \(x\in A\odot B\). Write \(z=\sum_i\alpha_i\otimes\beta_i\) with linearly independent \(\alpha_i\). For \(a\in A\), \(b\in B\) and a linear functional \(\ell\) on \(\tilde B\), applying \(\mathrm{id}\odot\ell\) to \(z(a\otimes b)=0\) gives \(wa=0\) for \(w=\sum_i\ell(\beta_ib)\alpha_i\in\tilde A\). An element \(w\) of \(\tilde A\) with \(wA=0\) is \(0\): if \(A\) is unital, \(w=w1=0\); otherwise \(w=a_0+\lambda1\) with \(a_0\in A\), and \(\lambda\ne0\) would make \(e=-a_0/\lambda\) a left identity of \(A\), so that \(ee^*=e^*\), hence \(e=e^*\) and \(e\) would be an identity of \(A\); so \(\lambda=0\), \(a_0a_0^*=0\) and \(a_0=0\). By linear independence, \(\ell(\beta_ib)=0\) for all \(i\), \(\ell\) and \(b\), so \(\beta_iB=0\), and \(\beta_i=0\) by the same argument in \(\tilde B\). So \(z=0\). As \(\tilde\pi\) is an injective representation, \(\tilde\gamma\) is a C\*-norm, and \(\tilde\gamma(x)=\|\pi(x)\|\) is the norm of \(x\) in \(E\) because \(\pi\) is faithful, hence isometric (Fact 1.1(a)). \(\square\)

**Theorem 4.4** (Takesaki). For all C\*-algebras \(A\) and \(B\), the minimal norm is the smallest C\*-norm on \(A\odot B\): \(\|x\|_{\min}\le\gamma(x)\) for every C\*-norm \(\gamma\). Every C\*-norm \(\gamma\) on \(A\odot B\) satisfies \(\gamma(a\otimes b)=\|a\|\|b\|\).

**Proof.** Let \(E\) be the completion for \(\gamma\) and \(\pi\) a faithful nondegenerate representation of \(E\) (Fact 1.2(d)). Lemma 4.3 gives a C\*-norm \(\tilde\gamma\) on \(\tilde A\odot\tilde B\) that agrees with \(\gamma\) on \(A\odot B\). By Theorem 4.2, \(\tilde\gamma\ge\|\cdot\|_{\min}\) on \(\tilde A\odot\tilde B\), and by Corollary 2.3(2) the minimal norm of \(\tilde A\odot\tilde B\) restricts to that of \(A\odot B\). So \(\gamma\ge\|\cdot\|_{\min}\). The second statement is Lemma 3.1 for \(\tilde\gamma\). \(\square\)

## 5. Factors and simple algebras

**Theorem 5.1** (Murray–von Neumann). Let \(M\) be a factor on \(H\), and let \(a_1,\dots,a_n\in M\) and \(b_1,\dots,b_n\in M'\) satisfy \(\sum_ia_ib_i=0\). Then \(\sum_ia_i\otimes b_i=0\) in \(M\odot M'\). Consequently the product map \(M\odot M'\to B(H)\), \(a\otimes b\mapsto ab\), is an injective \(*\)-homomorphism, \(x\mapsto\|\sum a_ib_i\|\) is a C\*-norm on \(M\odot M'\), and \(\|\sum_ia_i\otimes b_i\|_{\min}\le\|\sum_ia_ib_i\|\).

**Proof.** Let \(L=H\otimes\mathbb C^n=H^n\), with the standard basis \((\varepsilon_i)\) of \(\mathbb C^n\), and let \(\mathfrak M\) be the closed linear span of the vectors \(v(c,\xi)=\sum_icb_i\xi\otimes\varepsilon_i\), \(c\in M'\), \(\xi\in H\). For \(\eta\in H\) put \(w(\eta)=\sum_ja_j^*\eta\otimes\varepsilon_j\). Since each \(a_i\) commutes with \(c\in M'\),
\[
\langle v(c,\xi),w(\eta)\rangle=\sum_i\langle a_icb_i\xi,\eta\rangle=\Big\langle c\sum_ia_ib_i\xi,\eta\Big\rangle=0,
\]
so every \(w(\eta)\) is orthogonal to \(\mathfrak M\). For \(m\in M\), \((m\otimes1)v(c,\xi)=v(c,m\xi)\), because \(m\) commutes with \(c\) and with the \(b_i\); and for \(c'\in M'\), \((c'\otimes1)v(c,\xi)=v(c'c,\xi)\). So the projection \(e\) onto \(\mathfrak M\) commutes with the self-adjoint set \((M\cup M')\otimes1\) (Fact 1.5). By Fact 1.4(b), the matrix entries \(e_{ij}\) of \(e\) lie in \((M\cup M')'=\mathbb C1\) (Fact 1.5). So \(e_{ij}=\lambda_{ij}1\) with scalars \(\lambda_{ij}\), and \(\lambda_{ji}=\overline{\lambda_{ij}}\) because \(e=e^*\).

Since \(ev(1,\xi)=v(1,\xi)\), we get \(b_i\xi=\sum_j\lambda_{ij}b_j\xi\) for all \(\xi\), that is, \(b_i=\sum_j\lambda_{ij}b_j\). Since \(ew(\eta)=0\), we get \(\sum_j\lambda_{ij}a_j^*=0\) for every \(i\), and taking adjoints, \(\sum_j\lambda_{ji}a_j=0\) for every \(i\). Therefore
\[
\sum_ia_i\otimes b_i=\sum_ia_i\otimes\sum_j\lambda_{ij}b_j=\sum_j\Big(\sum_i\lambda_{ij}a_i\Big)\otimes b_j=0 .
\]
The product map is a \(*\)-homomorphism because \(M\) and \(M'\) commute; it is injective by what we proved; so the operator norm of \(\sum a_ib_i\) is a C\*-norm on \(M\odot M'\), and Theorem 4.4 gives the inequality. \(\square\)

**Theorem 5.2** (Takesaki). If \(A\) and \(B\) are simple C\*-algebras, then \(A\otimes_{\min}B\) is simple.

**Proof.** Put \(C=A\otimes_{\min}B\) and let \(J\ne C\) be a closed ideal. The quotient \(C/J\) is a nonzero C\*-algebra (Fact 1.1(e)); composing an irreducible representation of it (Fact 1.2(d)) with the quotient map gives an irreducible representation \(\pi\) of \(C\) on \(H\) with \(J\subseteq\ker\pi\). Being irreducible, \(\pi\) is nondegenerate. Lemma 4.3(1) gives representations \(\pi_1\) of \(A\) and \(\pi_2\) of \(B\) with commuting ranges and \(\pi(a\otimes b)=\pi_1(a)\pi_2(b)\). Since \(\pi\ne0\) and \(A\odot B\) is dense, \(\pi_1\ne0\) and \(\pi_2\ne0\); their kernels are closed ideals other than \(A\) and \(B\), hence \(0\): \(\pi_1\) and \(\pi_2\) are faithful.

Let \(M=\pi_1(A)''\). Then \(\pi_2(B)\subseteq M'\). The centre of \(M\) commutes with \(\pi_1(A)\subseteq M\) and with \(\pi_2(B)\subseteq M'\), hence with \(\pi(A\odot B)\) and with \(\pi(C)\); as \(\pi\) is irreducible, it is \(\mathbb C1\) (Fact 1.2(d)). So \(M\) is a factor. Let \(x=\sum_ia_i\otimes b_i\in A\odot B\) with \(\pi(x)=\sum_i\pi_1(a_i)\pi_2(b_i)=0\). By Theorem 5.1, \(\sum_i\pi_1(a_i)\otimes\pi_2(b_i)=0\) in \(M\odot M'\), so \((\pi_1\odot\pi_2)(x)=0\), and \(x=0\) because \(\pi_1\odot\pi_2\) is injective. So \(x\mapsto\|\pi(x)\|\) is a C\*-norm on \(A\odot B\). By Theorem 4.4 it is at least \(\|x\|_{\min}\), and it is at most \(\|x\|_{\min}\) because \(\pi\) is a representation of \(C\) (Fact 1.1(a)). So \(\pi\) is isometric on the dense subalgebra \(A\odot B\), hence on \(C\), and \(J\subseteq\ker\pi=0\). \(\square\)

## 6. Examples

**Example 6.1** (Commutative algebras). For compact Hausdorff spaces \(X\) and \(Y\), \(C(X)\otimes_{\min}C(Y)\cong C(X\times Y)\), with \(f\otimes g\) corresponding to \((s,t)\mapsto f(s)g(t)\). Indeed, by Lemma 3.2, applied with \(A=C(X)\) and the space \(Y\), the minimal norm of \(\sum f_i\otimes g_i\) is \(\max_{s,t}|\sum_if_i(s)g_i(t)|\); and the functions \((s,t)\mapsto\sum_if_i(s)g_i(t)\) form a self-adjoint subalgebra of \(C(X\times Y)\) that contains the constants and separates points, hence is dense by the Stone–Weierstrass theorem (The Stone–Weierstrass theorem for functions vanishing at infinity). Every C\*-norm on \(C(X)\odot C(Y)\) is the minimal one, by Exercise 7.3.

**Example 6.2** (Matrices). Let \(D=M_n(\mathbb C)\). For a C\*-algebra \(C\) on \(K\), \(D\odot C\) is the \(*\)-algebra \(M_n(C)\) of \(n\times n\) matrices over \(C\), and its minimal norm is the norm of \(M_n(C)\subseteq B(K^n)\), which is complete (the proof of Theorem 2.2). So \(D\otimes_{\min}C=D\odot C\). It has only one C\*-norm: another C\*-norm \(\gamma\) makes the identity map from the C\*-algebra \((M_n(C),\|\cdot\|_{\min})\) into the \(\gamma\)-completion an injective \(*\)-homomorphism, hence isometric (Fact 1.1(a)). The same holds for a finite-dimensional C\*-algebra \(D=\bigoplus_kM_{n_k}(\mathbb C)\), since \(D\odot C=\bigoplus_kM_{n_k}(C)\).

**Example 6.3** (Compact operators). Let \(\mathcal K(H)\) be the compact operators on \(H\). The closure of \(\mathcal K(H)\odot\mathcal K(K)\) in \(B(H\otimes K)\) contains every rank-one operator \(\zeta\mapsto\langle\zeta,\xi'\otimes\eta'\rangle\,\xi\otimes\eta\), which is the tensor product of two rank-one operators. Rank-one operators of this form span a dense subspace of the finite-rank operators, so \(\mathcal K(H)\otimes_{\min}\mathcal K(K)=\mathcal K(H\otimes K)\). Both factors are simple, and Theorem 5.2 recovers the simplicity of \(\mathcal K(H\otimes K)\).

**Example 6.4** (The factor condition). Theorem 5.1 fails without the factor hypothesis. Let \(M=\mathbb C1\oplus\mathbb C1\) on \(H=\mathbb C\oplus\mathbb C\), with the projections \(p=1\oplus0\) and \(q=0\oplus1\). Then \(M'=M\), and \(p\cdot q=0\) while \(p\otimes q\ne0\) in \(M\odot M'\).

## 7. Exercises

**Exercise 7.1.** Show that \(a\otimes b\mapsto b\otimes a\) extends to an isomorphism \(A\otimes_{\min}B\cong B\otimes_{\min}A\).

*Solution.* The unitary \(H\otimes K\to K\otimes H\), \(\xi\otimes\eta\mapsto\eta\otimes\xi\), carries \((\pi\otimes\rho)(\sum a_i\otimes b_i)\) to \((\rho\otimes\pi)(\sum b_i\otimes a_i)\). So the flip is isometric for the minimal norms (Theorem 2.2) and extends to the completions; its inverse is the flip in the other order.

**Exercise 7.2.** Let \(B\ne0\). Show that if \(A\otimes_{\min}B\) is simple, then \(A\) is simple.

*Solution.* Let \(J\) be a closed ideal of \(A\) with \(J\ne0\) and \(J\ne A\), and let \(q:A\to A/J\) be the quotient map. The closure \(I\) of \(J\odot B\) in \(A\otimes_{\min}B\) is a closed ideal, nonzero because \(\|j\otimes b\|_{\min}=\|j\|\|b\|\) (Corollary 2.3). The \(*\)-homomorphism \(A\otimes_{\min}B\to(A/J)\otimes_{\min}B\) extending \(q\odot\mathrm{id}\) (Corollary 2.3(2)) vanishes on \(I\) and not on \(a\otimes b\) with \(a\notin J\), \(b\ne0\). So \(I\ne A\otimes_{\min}B\), and \(A\otimes_{\min}B\) is not simple.

**Exercise 7.3.** Let \(A\) be unital and \(X\) compact Hausdorff. Show that \(A\odot C(X)\) has only one C\*-norm.

*Solution.* Let \(\gamma\) be a C\*-norm and \(E\) its completion. Lemma 3.2 gives \(\gamma\ge\|\cdot\|_{\min}\). For the reverse inequality, let \(\pi\) be an irreducible representation of \(E\). The elements \(1\otimes f\) commute with \(A\odot C(X)\), so \(\pi(1\otimes f)\) lies in \(\pi(E)'=\mathbb C1\) (Fact 1.2(d)); thus \(\pi(1\otimes f)=\chi(f)1\), where \(\chi\) is a character of \(C(X)\) because \(\pi(1\otimes1)=1\) (an irreducible representation is nondegenerate), so \(\chi\) is evaluation at a point \(t\) (Fact 1.1(b)). Then \(\pi(x)=\pi(x(t)\otimes1)\), and \(\|\pi(x)\|\le\|x(t)\|\le\|x\|_{\min}\) (Lemma 3.1). As \(\gamma(x)\) is the supremum of \(\|\pi(x)\|\) over irreducible representations (Fact 1.2(d)), \(\gamma\le\|\cdot\|_{\min}\).

## Where this leads

The lessons on injective factors use these results for a factor \(N\) and its commutant: the operator norm of \(\sum a_ib_i\) dominates the minimal norm of \(\sum a_i\otimes b_i\) (Theorem 5.1); automorphisms act isometrically on \(N\otimes_{\min}N'\) (Corollary 2.3); and \(N\otimes_{\min}N'\) is simple when \(N\) is a factor that is simple as a C\*-algebra, as a factor of type II\(_1\) is (Theorem 5.2; the simplicity of type II\(_1\) factors is proved in the lesson on property \(\Gamma\)). Whether the minimal norm is the only C\*-norm on \(A\odot B\) for every \(B\) is the question of *nuclearity* of \(A\); Exercise 7.3 and Example 6.2 show that \(A\odot C(X)\), with \(A\) unital, and \(D\odot C\), with \(D\) finite-dimensional, have only one C\*-norm.

## References

- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, revised and corrected edition with hyperlinks, free from the author: https://bruceblackadar.com/Mathematics/Cycr.pdf (first published as Encyclopaedia of Mathematical Sciences 122, 2006; the numbering is the same).
- [Takesaki 1958] M. Takesaki, A note on the cross-norm of the direct product of operator algebras, *Kōdai Mathematical Seminar Reports* 10 (1958), 137–140. Free at https://projecteuclid.org/journals/kodai-mathematical-seminar-reports/volume-10/issue-3/A-note-on-the-cross-norm-of-the-direct-product/10.2996/kmj/1138844027.pdf
- [Takesaki 1964] M. Takesaki, On the cross-norm of the direct product of C\*-algebras, *Tôhoku Mathematical Journal* (2) 16 (1964), 111–122. Free at https://doi.org/10.2748/tmj/1178243737
- [Turumaru 1952] T. Turumaru, On the direct-product of operator algebras I, *Tôhoku Mathematical Journal* (2) 4 (1952), 242–251. Free at https://doi.org/10.2748/tmj/1178245371
