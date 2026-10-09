# Row, column and cyclic estimates

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The noncommutative little Grothendieck inequality bounds a linear map from a C\*-algebra into a Hilbert space by two states, one evaluated on \(x^*x\) and one on \(xx^*\). Applied to a bounded homomorphism, it controls the homomorphism uniformly on rows and on columns of arbitrary length; this estimate is due to Christensen and appears in Dickson's work on the Kadison–Kastler row metric [Dickson, Lemmas 2.8–2.9]. Two consequences follow. A bounded homomorphism with a finite cyclic set is completely bounded, hence similar to a \(*\)-homomorphism; this is the finitely generated case of the similarity problem, first proved by Haagerup. And a rectangular derivation whose domain representation is cyclic is completely bounded and implemented by an operator, with absolute constants [OpenAI-288, Section 2]. The second statement is the form in which cyclicity enters the rest of the course.

We use: Theorem 1.1 of [The sharp noncommutative bilinear inequality](course:OA-APPROX/sharp-noncommutative-bilinear-inequality#theorem-1-1); Lemma 1.1, Theorem 3.1, Lemma 4.2 and Theorem 4.3 of [Completely bounded homomorphisms and similarity](completely-bounded-homomorphisms-and-similarity.md), whose notation for amplifications and for the norms \(\|\cdot\|_{\rm cb},\|\cdot\|_{\rm row},\|\cdot\|_{\rm col}\) we keep; Kaplansky's density theorem, [Theorem 7.1 of its lesson](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07); norm-preserving lifts along surjective \(*\)-homomorphisms, [Proposition 17.1](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-29); and [Proposition 18.2 of Projections and types of von Neumann algebras](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-08): if a von Neumann algebra \(N\) on \(K\) has a separating vector \(\Omega\), every positive normal functional on \(N\) is a vector functional \(\omega_\zeta\) with \(\zeta\in\overline{N\Omega}\). Throughout, \(A\) is a unital C\*-algebra.

## 1. The noncommutative little Grothendieck inequality

**Theorem 1.1** (Haagerup). Let \(T:A\to H\) be a bounded linear map into a Hilbert space. There are states \(f,g\) on \(A\) such that
\[
\|Tx\|^2\le\|T\|^2\big(f(x^*x)+g(xx^*)\big)\qquad(x\in A).
\tag{1.1}
\]
Consequently, for every finite family \(x_1,\dots,x_n\) in \(A\),
\[
\sum_j\|Tx_j\|^2\le\|T\|^2\Big(\Big\|\sum_jx_j^*x_j\Big\|+\Big\|\sum_jx_jx_j^*\Big\|\Big).
\tag{1.2}
\]

**Proof.** The form \(V(x,y)=\langle Tx,T(y^*)\rangle\) on \(A\times A\) is bilinear: it is linear in \(x\), and \(y\mapsto T(y^*)\) is conjugate linear, entering the conjugate linear slot. Also \(\|V\|\le\|T\|^2\). Theorem 1.1 of the sharp bilinear inequality lesson, with \(B=A\), gives states \(\varphi_1,\varphi_2,\psi_1,\psi_2\) with
\[
|V(x,y)|\le\|V\|\big[\varphi_1(x^*x)+\varphi_2(xx^*)\big]^{1/2}\big[\psi_1(y^*y)+\psi_2(yy^*)\big]^{1/2}.
\]
Put \(y=x^*\). Then \(V(x,x^*)=\|Tx\|^2\), \(y^*y=xx^*\) and \(yy^*=x^*x\); the inequality \(\sqrt{st}\le\frac12(s+t)\) gives (1.1) with \(f=\frac12(\varphi_1+\psi_2)\) and \(g=\frac12(\varphi_2+\psi_1)\). Summing (1.1) over the family and using \(f(\sum_jx_j^*x_j)\le\|\sum_jx_j^*x_j\|\), and likewise for \(g\), gives (1.2). \(\square\)

## 2. Rows and columns of a bounded homomorphism

For a homomorphism \(\varphi:A\to B(H)\) put \(\varphi^\sharp(a)=\varphi(a^*)^*\). It is linear, \(\|\varphi^\sharp\|=\|\varphi\|\), \((\varphi^\sharp)^\sharp=\varphi\), and it is again a homomorphism:
\[
\varphi^\sharp(ab)=\big(\varphi(b^*)\varphi(a^*)\big)^*=\varphi^\sharp(a)\varphi^\sharp(b).
\]
For a column \(c=(c_1,\dots,c_h)^T\) the operator \(\varphi_{h,1}(c):H\to H^h\) has adjoint \((\eta_i)\mapsto\sum_i\varphi(c_i)^*\eta_i\), that is,
\[
\varphi_{h,1}(c)^*=\varphi^\sharp_{1,h}(c^*),\qquad c^*=(c_1^*,\dots,c_h^*).
\tag{2.1}
\]

**Theorem 2.1** (row and column estimate). Every bounded unital homomorphism \(\varphi:A\to B(H)\) satisfies
\[
\|\varphi\|_{\rm row}\le\sqrt2\,\|\varphi\|^2,\qquad \|\varphi\|_{\rm col}\le\sqrt2\,\|\varphi\|^2 .
\]

**Proof.** Fix a unit vector \(\xi\in H\) and let \(T:A\to H\), \(T(y)=\varphi(y^*)^*\xi\). It is linear with \(\|T\|\le\|\varphi\|\). Theorem 1.1 gives states \(f,g\) with \(\|T(y)\|^2\le\|\varphi\|^2(f(y^*y)+g(yy^*))\).

Let \(x\in A\) and \(\varepsilon>0\). Put \(h=(xx^*+\varepsilon)^{1/2}\), positive and invertible, and \(v=h^{-1}x\). Then \(vv^*=h^{-1}xx^*h^{-1}=xx^*(xx^*+\varepsilon)^{-1}\le1\), so \(\|v\|\le1\), and \(x=hv\). Hence \(\varphi(x)^*=\varphi(v)^*\varphi(h)^*\) and
\[
\|\varphi(x)^*\xi\|\le\|\varphi\|\,\|\varphi(h)^*\xi\|=\|\varphi\|\,\|T(h)\|,
\]
because \(h=h^*\). As \(h^*h=hh^*=xx^*+\varepsilon\),
\[
\|\varphi(x)^*\xi\|^2\le\|\varphi\|^4\big(f(xx^*)+g(xx^*)+2\varepsilon\big),
\]
and \(\varepsilon\) is arbitrary. For a row \(x=(x_1,\dots,x_h)\), the adjoint of \(\varphi_{1,h}(x):H^h\to H\) is \(\xi\mapsto(\varphi(x_j)^*\xi)_j\), so by (1.1) of the first lesson
\[
\|\varphi_{1,h}(x)^*\xi\|^2=\sum_j\|\varphi(x_j)^*\xi\|^2\le\|\varphi\|^4(f+g)\Big(\sum_jx_jx_j^*\Big)\le2\|\varphi\|^4\|x\|^2 .
\]
Taking the supremum over \(\xi\) gives \(\|\varphi_{1,h}(x)\|\le\sqrt2\|\varphi\|^2\|x\|\). For columns, apply the row estimate to the bounded unital homomorphism \(\varphi^\sharp\) and use (2.1), with \(\|c^*\|=\|c\|\). \(\square\)

Set
\[
c_{\rm row}=4\sqrt2 .
\tag{2.2}
\]

**Proposition 2.2** (rectangular derivations). Let \(\sigma:A\to B(K)\) and \(\lambda:A\to B(F)\) be representations and \(\Delta\) a bounded rectangular derivation for \(\sigma,\lambda\). Then
\[
\|\Delta\|_{\rm row}\le c_{\rm row}\|\Delta\|,\qquad \|\Delta\|_{\rm col}\le c_{\rm row}\|\Delta\|.
\]

**Proof.** Let \(d=\|\Delta\|>0\) (the case \(\Delta=0\) is trivial). The triangular homomorphism \(\Phi=\Phi_{1/d}\) of Lemma 4.2 of the first lesson is unital, with \(\|\Phi\|\le\beta(1)\le2\). By Theorem 2.1, \(\|\Phi\|_{\rm row},\|\Phi\|_{\rm col}\le\sqrt2\cdot4=c_{\rm row}\). The upper right block of \(\Phi_{p,q}(x)\) is \(d^{-1}\Delta_{p,q}(x)\), and a block of an operator has norm at most that of the operator. Hence \(\|\Delta_{1,h}(x)\|\le c_{\rm row}d\|x\|\) and \(\|\Delta_{h,1}(x)\|\le c_{\rm row}d\|x\|\). \(\square\)

## 3. Homomorphisms with a finite cyclic set

A set \(\{\xi_1,\dots,\xi_m\}\subseteq H\) is *cyclic* for a homomorphism \(\pi:A\to B(H)\) if the vectors \(\pi(a)\xi_k\) span a dense subspace of \(H\).

**Theorem 3.1.** Let \(\pi:A\to B(H)\) be a bounded unital homomorphism with a cyclic set of \(m\) vectors. Then \(\pi\) is completely bounded and
\[
\|\pi\|_{\rm cb}\le m\,\|\pi\|_{\rm row}\,\|\pi\|_{\rm col}\le2m\|\pi\|^4 .
\]

**Proof.** Let \(\vec\xi=(\xi_1,\dots,\xi_m)^T\in H^m\) be the cyclic set. Fix \(n\) and \(X\in M_n(A)\). For \(a\in M_{n,m}(A)\), the vector \(\eta=\pi_{n,m}(a)\vec\xi\in H^n\) has coordinates \(\sum_k\pi(a_{ik})\xi_k\); since the coordinates can be chosen independently in a dense subspace of \(H\), these vectors are dense in \(H^n\). It suffices to show \(\|\pi_n(X)\eta\|\le m\|\pi\|_{\rm row}\|\pi\|_{\rm col}\|X\|\|\eta\|\) for them.

Let \(\varepsilon>0\), \(b=(a^*a+\varepsilon1_m)^{1/2}\in M_m(A)\), positive and invertible, and let \(\tilde a\in M_{n+m,m}(A)\) be \(a\) with the \(m\times m\) block \(\sqrt\varepsilon\,1_m\) added below. Then \(\tilde a^*\tilde a=b^2\), so \(\tilde w=\tilde ab^{-1}\) satisfies \(\tilde w^*\tilde w=1_m\); its first \(n\) rows form \(w=ab^{-1}\in M_{n,m}(A)\), with \(\|w\|\le\|\tilde w\|=1\). Put \(\vec\zeta=\pi_m(b)\vec\xi\in H^m\). By Lemma 1.1(1) of the first lesson,
\[
\pi_{n+m,m}(\tilde w)\vec\zeta=\pi_{n+m,m}(\tilde a)\vec\xi=(\eta,\sqrt\varepsilon\,\vec\xi),\qquad
\vec\zeta=\pi_m(\tilde w^*\tilde w)\vec\zeta=\pi_{m,n+m}(\tilde w^*)\pi_{n+m,m}(\tilde w)\vec\zeta .
\]
The \(m\times(n+m)\) matrix \(\tilde w^*\) has \(m\) rows of norm at most \(1\); an operator with \(m\) row blocks has norm at most \(\sqrt m\) times the largest norm of its row blocks, so \(\|\pi_{m,n+m}(\tilde w^*)\|\le\sqrt m\|\pi\|_{\rm row}\). Therefore
\[
\|\vec\zeta\|\le\sqrt m\,\|\pi\|_{\rm row}\big(\|\eta\|^2+\varepsilon\|\vec\xi\|^2\big)^{1/2}.
\]
Next \(a=wb\) gives \(\pi_n(X)\eta=\pi_{n,m}(Xa)\vec\xi=\pi_{n,m}(Xw)\vec\zeta\). The matrix \(Xw\in M_{n,m}(A)\) has \(m\) columns of norm at most \(\|X\|\), and an operator with \(m\) column blocks has norm at most \(\sqrt m\) times the largest norm of its column blocks; so \(\|\pi_{n,m}(Xw)\|\le\sqrt m\|\pi\|_{\rm col}\|X\|\). Combining,
\[
\|\pi_n(X)\eta\|\le m\,\|\pi\|_{\rm row}\|\pi\|_{\rm col}\|X\|\big(\|\eta\|^2+\varepsilon\|\vec\xi\|^2\big)^{1/2},
\]
and \(\varepsilon\to0\) gives the first inequality. The second is Theorem 2.1. \(\square\)

**Corollary 3.2** (Haagerup). A bounded unital homomorphism \(\pi:A\to B(H)\) with a cyclic set of \(m\) vectors is similar to a \(*\)-homomorphism, through a positive invertible \(S\) with \(\|S\|\|S^{-1}\|\le2m\|\pi\|^4\).

**Proof.** Theorem 3.1 and Theorem 3.1 of the first lesson. \(\square\)

The bound grows with \(m\). A general bounded homomorphism need not have any finite cyclic set, and its restrictions to the invariant subspaces generated by finite sets have unbounded \(m\); lesson three shows how a uniform estimate for inner derivations removes this dependence.

## 4. Cyclic domains

**Lemma 4.1** (column factorization). Let \(P\subseteq B(K)\) be a von Neumann algebra with a cyclic vector. For every \(h\ge1\) and every unit vector \(\xi=(\xi_1,\dots,\xi_h)\in K^h\) there are a unit vector \(\zeta\in K\) and a column \(v=(v_1,\dots,v_h)^T\in M_{h,1}(P)\) with \(\|v\|\le1\) and \(\xi_i=v_i\zeta\) for every \(i\).

**Proof.** Let \(\Omega\) be cyclic for \(P\) and \(N=P'\). Then \(\Omega\) is separating for \(N\): if \(x\in N\) and \(x\Omega=0\), then \(xa\Omega=ax\Omega=0\) for all \(a\in P\), so \(x=0\). The functional \(\omega(x)=\sum_i\langle x\xi_i,\xi_i\rangle\) on \(N\) is positive, normal and \(\omega(1)=1\). By Proposition 18.2 of the projections lesson there is \(\zeta\in K\) with \(\omega(x)=\langle x\zeta,\zeta\rangle\) for \(x\in N\); then \(\|\zeta\|^2=\omega(1)=1\). The assignment \(x\zeta\mapsto(x\xi_1,\dots,x\xi_h)\), \(x\in N\), is well defined and isometric, because both squared norms equal \(\omega(x^*x)\); it extends to an isometry of \(\overline{N\zeta}\) into \(K^h\). Extend it by \(0\) on \(\overline{N\zeta}^{\perp}\) to a contraction \(v:K\to K^h\). The subspace \(\overline{N\zeta}\) reduces \(N\) and the isometry intertwines \(N\) with its diagonal action, so \(vx=x^{(h)}v\) for every \(x\in N\). Each coordinate \(v_i\) therefore lies in \(N'=P\), and \(v\zeta=\xi\) by construction (take \(x=1\)). \(\square\)

**Theorem 4.2** (implementation on a cyclic domain). Let \(\sigma:A\to B(K)\) and \(\lambda:A\to B(F)\) be representations, with \(\sigma\) having a cyclic vector, and let \(\Delta:A\to B(K,F)\) be a bounded rectangular derivation for \(\sigma,\lambda\). Then
\[
\|\Delta\|_{\rm cb}\le2c_{\rm row}\|\Delta\|,
\]
and \(\Delta\) is implemented by some \(V\in B(K,F)\) with
\[
\|V\|\le c_0\|\Delta\|,\qquad c_0=c_{\rm row}=4\sqrt2 .
\tag{4.1}
\]

**Proof.** Put \(P=\sigma(A)''\), which has the cyclic vector of \(\sigma\). Fix \(h\), \(X\in M_h(A)\) with \(\|X\|\le1\), and a unit vector \(\xi\in K^h\). Lemma 4.1 gives a unit vector \(\zeta\) and a contraction \(v\in M_{h,1}(P)\) with \(v\zeta=\xi\). Let \(\tilde v\in M_h(P)\) have first column \(v\) and zero other columns. The C\*-algebra \(\sigma_h(M_h(A))=M_h(\sigma(A))\) on \(K^h\) has strong closure \(M_h(P)\), so by Kaplansky's density theorem there is a net \(Z_\alpha\) in its unit ball converging strongly to \(\tilde v\). By Proposition 17.1 of the C\*-algebra lesson, applied to the surjective \(*\)-homomorphism \(\sigma_h\) of \(M_h(A)\) onto \(M_h(\sigma(A))\), each \(Z_\alpha=\sigma_h(W_\alpha)\) with \(\|W_\alpha\|\le1\). Let \(w_\alpha\in M_{h,1}(A)\) be the first column of \(W_\alpha\). Then \(\|w_\alpha\|\le1\) and \(\sigma_{h,1}(w_\alpha)\zeta=Z_\alpha(\zeta,0,\dots,0)\to\tilde v(\zeta,0,\dots,0)=\xi\).

Entrywise application of (4.1) of the first lesson gives
\[
\Delta_h(X)\sigma_{h,1}(w_\alpha)=\Delta_{h,1}(Xw_\alpha)-\lambda_h(X)\Delta_{h,1}(w_\alpha).
\]
By Proposition 2.2 and \(\|\lambda_h(X)\|\le1\),
\[
\|\Delta_h(X)\sigma_{h,1}(w_\alpha)\zeta\|\le c_{\rm row}\|\Delta\|\big(\|Xw_\alpha\|+\|w_\alpha\|\big)\le2c_{\rm row}\|\Delta\|.
\]
The operator \(\Delta_h(X)\) is bounded, so passing to the limit gives \(\|\Delta_h(X)\xi\|\le2c_{\rm row}\|\Delta\|\). Hence \(\|\Delta\|_{\rm cb}\le2c_{\rm row}\|\Delta\|\), and Theorem 4.3 of the first lesson gives \(V\) with \(\|V\|\le\frac12\|\Delta\|_{\rm cb}\le c_{\rm row}\|\Delta\|\). \(\square\)

Only the domain representation needs a cyclic vector; the output representation \(\lambda\) is arbitrary. The constants are not optimal, and any absolute constants would serve the later lessons; the preprint [OpenAI-288] works with the larger constant \((1+4c_{\rm row})^2\) in place of \(c_0\).

## 5. Exercises

**Exercise 5.1.** Let \(A=M_n(\mathbb C)\) and \(T:A\to\mathbb C^n\) send a matrix to its first row, read as a vector. Show that \(\|T\|=1\), and that for \(x_j=e_{1j}\) the left side of (1.2) is \(n\) while \(\|\sum_jx_j^*x_j\|=1\). Conclude that no inequality \(\sum_j\|Tx_j\|^2\le C\|T\|^2\|\sum_jx_j^*x_j\|\) with \(C\) independent of \(n\) can hold: both terms in (1.2) are needed.

**Exercise 5.2.** Let \(\pi:A\to B(H)\) be a bounded unital homomorphism with a cyclic set \(\{\xi_1,\dots,\xi_m\}\). Show that \(\vec\xi=(\xi_1,\dots,\xi_m)^T\) is a cyclic vector for the unital homomorphism \(\pi_m:M_m(A)\to B(H^m)\), that \(\|\pi_m\|\le m\|\pi\|\) and \(\|\pi_m\|_{\rm cb}=\|\pi\|_{\rm cb}\). Deduce from the case of one cyclic vector the bound \(\|\pi\|_{\rm cb}\le2m^4\|\pi\|^4\).

**Exercise 5.3.** Let \(P=\mathbb C1\) on \(K=\mathbb C^2\). Show that the conclusion of Lemma 4.1 fails for \(h=2\) and \(\xi=\frac1{\sqrt2}(e_1,e_2)\). Which hypothesis fails?

**Exercise 5.4.** Let \(\sigma\) be a representation of \(A\) with a cyclic vector and \(\Delta\) a bounded \(\sigma\)-derivation implemented by \(V\). Show that \(\|\Delta\|\le2\operatorname{dist}(V,\sigma(A)')\le2c_0\|\Delta\|\).

## 6. Solutions

**Solution 5.1.** The first row of \(x\) has norm \(\|e_{11}x\|\le\|x\|\), with equality for \(x=e_{11}\); so \(\|T\|=1\). For \(x_j=e_{1j}\), \(Tx_j\) is the \(j\)th basis vector, so \(\sum_j\|Tx_j\|^2=n\); \(\sum_jx_j^*x_j=\sum_je_{jj}=1\) has norm \(1\), and \(\sum_jx_jx_j^*=ne_{11}\) has norm \(n\). An inequality with only the first term would give \(n\le C\).

**Solution 5.2.** The matrix with \(a\) in entry \((i,k)\) and zeros elsewhere is sent by \(\pi_m\) to an operator mapping \(\vec\xi\) to the vector with \(\pi(a)\xi_k\) in coordinate \(i\) and zeros elsewhere; such vectors span a dense subspace of \(H^m\). The map \(\pi_m\) is a unital homomorphism by Lemma 1.1(1) of the first lesson. For \(x\in M_m(A)\) with \(\|x\|\le1\), every entry has norm at most \(1\), so each row operator \(\pi_{1,m}(x_{i\cdot})\) has norm at most \((\sum_k\|\pi(x_{ik})\|^2)^{1/2}\le\sqrt m\|\pi\|\), and \(\pi_m(x)\), which has \(m\) such rows, has norm at most \(m\|\pi\|\). The amplifications of \(\pi_m\) are amplifications of \(\pi\) under the identification \(M_n(M_m(A))=M_{nm}(A)\), so the completely bounded norms agree. Theorem 3.1 with one cyclic vector gives \(\|\pi\|_{\rm cb}=\|\pi_m\|_{\rm cb}\le2\|\pi_m\|^4\le2m^4\|\pi\|^4\).

**Solution 5.3.** \(v_i\) would be scalars, so \(\xi_1=v_1\zeta\) and \(\xi_2=v_2\zeta\) would be parallel, whereas \(e_1\perp e_2\). The algebra \(\mathbb C1\) has no cyclic vector on \(\mathbb C^2\).

**Solution 5.4.** If \(y\in\sigma(A)'\), then \(V-y\) also implements \(\Delta\), so \(\|\Delta(a)\|\le2\|V-y\|\|a\|\); taking the infimum over \(y\) gives the first inequality. For the second, Theorem 4.2 gives an implementing \(V'\) with \(\|V'\|\le c_0\|\Delta\|\). Then \(V-V'\) commutes with \(\sigma(A)\), so \(\operatorname{dist}(V,\sigma(A)')\le\|V-(V-V')\|=\|V'\|\le c_0\|\Delta\|\).

## References

- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
- [Dickson] L. Dickson, A Kadison Kastler row metric and intermediate subalgebras, International Journal of Mathematics 25 (2014), 1450082, Lemmas 2.8–2.9. https://arxiv.org/abs/1404.3070
- [Pisier-GT] G. Pisier, Grothendieck's theorem, past and present, Bulletin of the AMS 49 (2012), 237–323, Sections 7–8 (the noncommutative Grothendieck inequalities). https://arxiv.org/abs/1101.4195
- [Ozawa] N. Ozawa, An invitation to the similarity problems (after Pisier), lecture notes, RIMS, 2006, Section 1.2. https://www.kurims.kyoto-u.ac.jp/~narutaka/notes/similarity.pdf
