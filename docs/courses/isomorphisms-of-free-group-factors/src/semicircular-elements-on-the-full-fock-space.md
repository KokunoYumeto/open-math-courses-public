# Semicircular elements on the full Fock space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The first four lessons proved that \(L(\mathbb F_n)\cong L(\mathbb F_{n+1})\) for \(n\ge3\). The remaining lessons prove that \(L(\mathbb F_2)\cong L(\mathbb F_3)\) as well, so that all free group factors of finite rank \(n\ge2\) are isomorphic; this is the main theorem of [OAI]. The route is Voiculescu's computation of a corner of a free group factor: for a projection \(p\) of trace \(\frac12\), \(pL(\mathbb F_n)p\cong L(\mathbb F_{4n-3})\) (last lesson). With \(n=2\) and \(n=3\) the corners are \(L(\mathbb F_5)\) and \(L(\mathbb F_9)\), which are isomorphic by the rank step, and a II₁ factor is determined by any of its corners of trace \(\frac12\).

The corner computation needs free elements with explicit distributions inside \(2\times2\) matrices. This lesson provides them. Section 1 collects facts on distributions of normal elements and shows that free elements with suitable distributions generate a free group factor. Section 2 describes the semicircle law. Section 3 proves a criterion for freeness that fits operators on the full Fock space, and Section 4 applies it: the semicircular elements \(\ell(e_j)+\ell(e_j)^*\) attached to orthonormal vectors are free, the vacuum vector gives a faithful trace, and they generate a copy of \(L(\mathbb F_m)\).

We use: from [Free independence and Haar tuples](free-independence-and-haar-tuples.md), Lemmas 1.2, 1.4 and 2.4; from [A small cocycle with a prescribed word value](a-small-cocycle-with-a-prescribed-word-value.md), the functional \(\Lambda\) and Lemma 3.1 (its moments); the Borel functional calculus of normal operators, [Lemma 1.1, Corollary 1.2, Proposition 2.1, Theorems 3.1 and 8.1 of the spectral theorem lesson](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators#OA-FND-ST-03); the double commutant theorem, [Theorem 4.4 of its lesson](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#OA-FND-BI-06); and the density of polynomials in \(z\) and \(\bar z\) among continuous functions on a compact subset of \(\mathbb C\), [Section 10 of the Stone–Weierstrass lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity#OA-FND-SW-09).

## 1. Distributions of normal elements

Throughout, \((M,\tau)\) is a von Neumann algebra with a faithful normal tracial state, acting on \(L^2(M)\) by left multiplication, with \(\Omega\) the vector of \(1\). For a normal \(z\in M\) and a bounded Borel function \(f\) on its spectrum, \(f(z)\) is the Borel functional calculus (Theorem 8.1 of the spectral theorem lesson). It commutes with every operator commuting with \(z\) and \(z^*\), so \(f(z)\in\{z,z^*\}''=W^*(z)\).

**Lemma 1.1** (composition and direct sums). Let \(z\) be a normal operator with spectrum \(S\), let \(g\colon S\to\mathbb C\) be a bounded Borel function and \(D\subset\mathbb C\) a closed disc containing \(g(S)\).

1. \(g(z)\) is normal, its spectrum lies in \(D\), and \(f(g(z))=(f\circ g)(z)\) for every bounded Borel function \(f\colon D\to\mathbb C\).
2. If \(z=z_1\oplus z_2\) is an orthogonal direct sum of normal operators and \(D\) contains the spectrum of \(z\), then \(f(z)=f(z_1)\oplus f(z_2)\) for every bounded Borel \(f\colon D\to\mathbb C\).
3. If \(\pi\) is a normal \(*\)-isomorphism of a von Neumann algebra containing \(z\) onto another von Neumann algebra, then \(\pi(f(z))=f(\pi(z))\) for every bounded Borel \(f\) on a closed disc containing \(\sigma(z)=\sigma(\pi(z))\).

**Proof.** (1) \(g(z)\) commutes with \(g(z)^*=\bar g(z)\), and its spectrum lies in the closure of \(g(S)\) (Theorem 3.1(6) of the spectral theorem lesson). Let \(\mathcal M\) be the set of bounded Borel \(f\) on \(D\) with \(f(g(z))=(f\circ g)(z)\). For \(f(w)=w^a\bar w^b\) the identity is the homomorphism property of the calculus of \(z\). Both sides are linear in \(f\) and have norm at most \(\sup_D|f|\), and polynomials in \(w\) and \(\bar w\) are uniformly dense in the continuous functions on \(D\); so \(\mathcal M\) contains every continuous function. If \(f_k\to f\) boundedly on \(D\), then \(f_k\circ g\to f\circ g\) boundedly on \(S\), and by the bounded convergence property (Theorem 3.1(4)) both sides converge strongly; so \(\mathcal M\) is closed under bounded convergence. By Lemma 1.1 of the spectral theorem lesson, \(\mathcal M\) contains every bounded Borel function on \(D\). (2) The same argument, starting from \(z^a(z^*)^b=z_1^a(z_1^*)^b\oplus z_2^a(z_2^*)^b\). (3) The same argument again: the identity holds for polynomials in \(w\) and \(\bar w\) because \(\pi\) is a \(*\)-homomorphism, both sides are contractive in the supremum norm of \(f\), and if \(f_k\to f\) boundedly, then \(f_k(z)\to f(z)\) strongly, so \(\pi(f_k(z))\to\pi(f(z))\) weakly (\(\pi\) is normal, and on bounded sets strong convergence implies \(\sigma\)-weak convergence), while \(f_k(\pi(z))\to f(\pi(z))\) strongly. \(\square\)

By (3), \(f(z)\) and the distribution defined below do not depend on the faithful normal representation in which they are computed.

For a normal \(z\in M\), the *distribution* of \(z\) is the Borel probability measure \(\mu_z(\Delta)=\tau(1_\Delta(z))\) on its spectrum. It is the spectral measure of the vector \(\Omega\) (Proposition 2.1 and (3.1) of the spectral theorem lesson), so \(\tau(f(z))=\int f\,d\mu_z\) for every bounded Borel \(f\). By Lemma 1.1, the distribution of \(g(z)\) is the image measure \(g_*\mu_z\). A unitary \(h\) is a Haar unitary exactly when \(\mu_h\) is the normalized arc length on the circle, because a finite measure on the circle is determined by its Fourier coefficients \(\int\bar w^k\,d\mu_h=\tau(h^{-k})\). Since \(\tau\) is faithful, \(\mu_z(\Delta)=0\) implies \(1_\Delta(z)=0\).

**Lemma 1.2** (Haar generators). Let \(y\in M\) be self-adjoint, and suppose its distribution function \(F(t)=\mu_y((-\infty,t])\) is continuous and strictly increasing on an interval \([a,b]\) with \(\mu_y([a,b])=1\). Then \(h=e^{2\pi iF(y)}\) is a Haar unitary and \(W^*(h)=W^*(y)\).

**Proof.** Put \(w=F(y)\in W^*(y)\). Since \(F\) restricts to an increasing bijection \([a,b]\to[0,1]\), for \(s\in[0,1]\) we have \(\mu_w([0,s])=\mu_y(\{t:F(t)\le s\})=F(F^{-1}(s))=s\): \(w\) has the uniform distribution on \([0,1]\). Hence \(\tau(h^k)=\int_0^1e^{2\pi iks}\,ds=0\) for \(k\ne0\), and \(h\in W^*(y)\). Conversely, let \(\theta(e^{2\pi is})=s\) for \(s\in[0,1)\). By Lemma 1.1, \(\theta(h)\) is the function \(x\mapsto x\,1_{[0,1)}(x)\) of \(w\), which equals \(w\) because \(1_{\{1\}}(w)=0\); so \(w\in W^*(h)\). Finally, \(1_{\mathbb R\setminus[a,b]}(y)=0\), and \(F^{-1}\circ F\) is the identity on \([a,b]\), so \(y=(F^{-1}\circ F)(y)=F^{-1}(w)\in W^*(h)\) by Lemma 1.1. \(\square\)

**Lemma 1.3** (free group factors from free generators). Let \(y_1,\ldots,y_m\in M\) be such that the von Neumann algebras \(W^*(y_j)\) form a free family that generates \(M\), and \(W^*(y_j)=W^*(h_j)\) for Haar unitaries \(h_j\). Then there is a trace-preserving normal \(*\)-isomorphism \(L(\mathbb F_m)\to M\) with \(\lambda(x_j)\mapsto h_j\).

**Proof.** The tuple \((h_1,\ldots,h_m)\) generates \(M\). For \(g\ne e\) with reduced word \(x_{j_1}^{k_1}\cdots x_{j_r}^{k_r}\) (\(k_i\ne0\), \(j_i\ne j_{i+1}\)), the value \(h_{j_1}^{k_1}\cdots h_{j_r}^{k_r}\) is a reduced product of centred elements of the free algebras \(W^*(h_j)\), of trace \(0\). So \((h_j)\) is a freely generating Haar tuple; apply Lemma 2.4 of the first lesson. \(\square\)

## 2. The semicircle law

Let \(\sigma\) be the image of the probability measure \(\frac2\pi\sin^2\phi\,d\phi\) on \([0,\pi]\) under \(\phi\mapsto2\cos\phi\). It is a probability measure on \([-2,2]\), with density \(\frac1{2\pi}\sqrt{4-t^2}\) (Exercise 5.1). A self-adjoint element \(y\) is *semicircular* if \(\mu_y=\sigma\). The *Chebyshev polynomials* are \(U_0=1\), \(U_1(t)=t\) and \(U_{n+1}(t)=tU_n(t)-U_{n-1}(t)\).

**Lemma 2.1.**

1. \(U_n\) is a monic polynomial of degree \(n\), and \(U_n(2\cos\phi)=\sin((n+1)\phi)/\sin\phi\).
2. \(\int U_nU_k\,d\sigma=\delta_{nk}\).
3. If \(t^k=\sum_{n\le k}a_nU_n(t)\), then \(\int t^k\,d\sigma=a_0\).
4. The distribution function of \(\sigma\) is continuous and strictly increasing on \([-2,2]\).
5. The image of \(\sigma\) under \(t\mapsto t^2\) is the measure \(\nu\) on \([0,4]\) with \(\int g\,d\nu=\Lambda(g)\), the limit law of the third lesson; it has no atoms and its distribution function is continuous and strictly increasing on \([0,4]\).

**Proof.** (1) Induction, using \(\sin((n+2)\phi)+\sin(n\phi)=2\cos\phi\,\sin((n+1)\phi)\). (2) \(\int U_nU_k\,d\sigma=\frac2\pi\int_0^\pi\sin((n+1)\phi)\sin((k+1)\phi)\,d\phi=\delta_{nk}\). (3) By (2), \(\int U_n\,d\sigma=\int U_nU_0\,d\sigma=\delta_{n0}\). (4) The function \(\phi\mapsto2\cos\phi\) is a decreasing homeomorphism of \([0,\pi]\) onto \([-2,2]\), and \(\sin^2\phi>0\) on \((0,\pi)\). (5) For continuous \(g\), the substitutions \(\phi=\frac\pi2-\vartheta\) and \(\phi=\frac\pi2+\vartheta\) on the two halves of \([0,\pi]\) give \(\int g(t^2)\,d\sigma(t)=\frac2\pi\int_0^\pi g(4\cos^2\phi)\sin^2\phi\,d\phi=\frac4\pi\int_0^{\pi/2}g(4\sin^2\vartheta)\cos^2\vartheta\,d\vartheta=\Lambda(g)\). As in (4), \(\vartheta\mapsto4\sin^2\vartheta\) is an increasing homeomorphism of \([0,\frac\pi2]\) onto \([0,4]\) and \(\cos^2\vartheta>0\) on \([0,\frac\pi2)\). \(\square\)

By Lemma 2.1(5) and Lemma 3.1 of the third lesson, \(\int t^{2r}\,d\sigma=\mathrm{Cat}_r\); the odd moments vanish because \(\phi\mapsto\pi-\phi\) changes the sign of \(2\cos\phi\) and preserves \(\sin^2\phi\).

## 3. A criterion for freeness

Definition 1.1 of the first lesson makes sense for any state \(\omega\) on a unital \(*\)-algebra: unital \(*\)-subalgebras \(A_i\) are free with respect to \(\omega\) if \(\omega(x_1\cdots x_r)=0\) for every reduced product of elements \(x_k\in A_{i_k}\) with \(\omega(x_k)=0\). The proofs of Lemma 1.2(2) and (3) there use only this definition and hold for states.

**Lemma 3.1** (associativity of freeness). Let \((A_i)_{i\in I}\) be unital \(*\)-subalgebras and \(I\) the disjoint union of sets \(I_l\). If each family \((A_i)_{i\in I_l}\) is free and the algebras \(B_l\) generated by \(\bigcup_{i\in I_l}A_i\) form a free family, then \((A_i)_{i\in I}\) is free.

**Proof.** Let \(x_1\cdots x_r\) be a reduced product of centred \(x_k\in A_{i_k}\). Group the factors into maximal blocks of consecutive factors whose indices lie in the same \(I_l\). Inside a block, consecutive indices differ, so the block is a reduced product for the free family \((A_i)_{i\in I_l}\) and has trace \(0\): it is a centred element of \(B_l\). Consecutive blocks belong to different \(B_l\). So \(x_1\cdots x_r\) is a reduced product of centred elements of the free family \((B_l)\), and its trace is \(0\). \(\square\)

**Theorem 3.2** (a criterion for freeness). Let \(K\) be a Hilbert space, \(\xi\in K\) a unit vector and \(\omega=\langle\,\cdot\,\xi,\xi\rangle\) on \(B(K)\). Let \(\mathcal D\subseteq B(K)\) be a unital \(*\)-subalgebra and \(L\in B(K)\) an operator with

- (a) \(L^*dL=\omega(d)1\) for every \(d\in\mathcal D\);
- (b) \(L^*\xi=0\);
- (c) \(L^*d\xi=0\) for every \(d\in\mathcal D\).

Let \(X=L+L^*\). Then \(\omega(p(X))=\int p\,d\sigma\) for every polynomial \(p\), and the algebra of polynomials in \(X\) and \(\mathcal D\) are free with respect to \(\omega\).

**Proof.** *Step 1.* If \(\eta\in K\) and \(L^*\eta=0\), then \(U_n(X)\eta=L^n\eta\) for all \(n\ge0\). This holds for \(n=0,1\). By (a) with \(d=1\), \(L^*L=1\), so \(L^*L^{n}\eta=L^{n-1}\eta\) for \(n\ge1\), and inductively
\[
U_{n+1}(X)\eta=(L+L^*)L^n\eta-L^{n-1}\eta=L^{n+1}\eta .
\]
*Step 2.* By (b) and Step 1, \(\omega(U_n(X))=\langle L^n\xi,\xi\rangle=\langle L^{n-1}\xi,L^*\xi\rangle=0\) for \(n\ge1\). Writing \(t^k=\sum_na_nU_n(t)\), we get \(\omega(X^k)=a_0=\int t^k\,d\sigma\) by Lemma 2.1(3). In particular the centred polynomials in \(X\) are the linear combinations of the \(U_n(X)\), \(n\ge1\).

*Step 3.* Let \(z_1\cdots z_r\) be a product whose factors are alternately centred polynomials in \(X\) and centred elements of \(\mathcal D\). By Step 2 and multilinearity we may assume that each polynomial factor is \(U_n(X)\) for some \(n\ge1\). Put \(\eta_{r+1}=\xi\) and \(\eta_k=z_k\eta_{k+1}\). We show by downward induction on \(k\) that \(L^*\eta_{k+1}=0\) whenever \(z_k\) is a polynomial factor, and \(L^*\eta_k=0\) whenever \(z_k\in\mathcal D\). If \(z_k=d\in\mathcal D\), then either \(\eta_{k+1}=\xi\) and \(L^*d\xi=0\) by (c), or \(z_{k+1}=U_n(X)\) and \(\eta_{k+1}=L^n\eta_{k+2}\) by Step 1, so that \(L^*\eta_k=(L^*dL)L^{n-1}\eta_{k+2}=\omega(d)L^{n-1}\eta_{k+2}=0\) by (a). If \(z_k\) is a polynomial factor, then \(\eta_{k+1}\) is \(\xi\), or \(d\eta_{k+2}\) with \(z_{k+1}=d\); in both cases \(L^*\eta_{k+1}=0\) by (b) and the case just treated. Consequently, by Step 1, \(\eta_k=L^n\eta_{k+1}\) whenever \(z_k=U_n(X)\).

Now \(\omega(z_1\cdots z_r)=\langle\eta_1,\xi\rangle\). If \(z_1=U_n(X)\), this is \(\langle L^{n-1}\eta_2,L^*\xi\rangle=0\). If \(z_1=d\) and \(r=1\), it is \(\omega(d)=0\). If \(z_1=d\) and \(r\ge2\), then \(\eta_2=L^n\eta_3\) and \(\langle dL^n\eta_3,\xi\rangle=\langle L^{n-1}\eta_3,L^*d^*\xi\rangle=0\) by (c). \(\square\)

## 4. Free semicircular families

Let \(H\) be a Hilbert space. Its *full Fock space* is \(\mathcal F(H)=\mathbb C\Omega\oplus\bigoplus_{k\ge1}H^{\otimes k}\), with the unit vector \(\Omega\). For \(e\in H\), the *creation operator* \(\ell(e)\) maps \(\Omega\) to \(e\) and \(\eta_1\otimes\cdots\otimes\eta_k\) to \(e\otimes\eta_1\otimes\cdots\otimes\eta_k\). It is bounded with \(\|\ell(e)\|=\|e\|\), its adjoint satisfies \(\ell(e)^*\Omega=0\) and \(\ell(e)^*(\eta_1\otimes\cdots\otimes\eta_k)=\langle\eta_1,e\rangle\,\eta_2\otimes\cdots\otimes\eta_k\) (with \(\Omega\) for \(k=1\)), and
\[
\ell(e)^*\ell(e')=\langle e',e\rangle1 .
\]
Put \(s(e)=\ell(e)+\ell(e)^*\), a self-adjoint operator of norm at most \(2\|e\|\), and \(\varphi=\langle\,\cdot\,\Omega,\Omega\rangle\). For a closed subspace \(K_0\subseteq H\), let \(\mathcal F(K_0)\subseteq\mathcal F(H)\) be the closed span of \(\Omega\) and the tensors of vectors in \(K_0\), and \(\mathcal S(K_0)\) the von Neumann algebra generated by the \(s(e)\), \(e\in K_0\).

**Lemma 4.1.** Let \(K_0\subseteq H\) be a closed subspace and \(g,g'\in K_0^\perp\).

1. \(\mathcal F(K_0)\) is invariant under \(\mathcal S(K_0)\), and \(\ell(g)^*\) vanishes on \(\mathcal F(K_0)\). In particular \(\ell(g)^*b\,\Omega=0\) for \(b\in\mathcal S(K_0)\).
2. \(\ell(g)^*b\,\ell(g')=\varphi(b)\langle g',g\rangle1\) for every \(b\in\mathcal S(K_0)\).
3. If \(e\in H\) is a unit vector and \(\ell(e)^*\eta=0\), then \(U_n(s(e))\eta=e^{\otimes n}\otimes\eta\) for \(n\ge0\).

**Proof.** (1) The operators \(\ell(e)\), \(\ell(e)^*\), \(e\in K_0\), map \(\mathcal F(K_0)\) into itself, so the closed subspace \(\mathcal F(K_0)\) is invariant under the \(*\)-algebra they generate and, by strong closure, under \(\mathcal S(K_0)\) (Theorem 4.4 of the double commutant lesson). Every tensor in \(\mathcal F(K_0)\) other than \(\Omega\) begins with a vector of \(K_0\perp g\), and \(\ell(g)^*\Omega=0\).

(2) Fix \(\eta\in\mathcal F(H)\) and define \(T\colon\mathcal F(K_0)\to\mathcal F(H)\) by \(T\Omega=g'\otimes\eta\) and \(T\zeta=\zeta\otimes g'\otimes\eta\) for tensors \(\zeta\) of vectors in \(K_0\); it is bounded, with \(\|T\zeta\|=\|\zeta\|\|g'\|\|\eta\|\). For \(e\in K_0\), \(\ell(e)T=T\ell(e)\) on \(\mathcal F(K_0)\), and \(\ell(e)^*T=T\ell(e)^*\): on tensors of positive length both sides remove the first factor, and \(\ell(e)^*T\Omega=\langle g',e\rangle\eta=0=T\ell(e)^*\Omega\). Hence \(bT=Tb\) on \(\mathcal F(K_0)\) for \(b\) in the \(*\)-algebra generated by the \(s(e)\), \(e\in K_0\), and, by strong limits of bounded nets (Kaplansky's density theorem), for \(b\in\mathcal S(K_0)\). Write \(b\Omega=\varphi(b)\Omega+\zeta_+\) with \(\zeta_+\) orthogonal to \(\Omega\) in \(\mathcal F(K_0)\). Then
\[
\ell(g)^*b\,\ell(g')\eta=\ell(g)^*bT\Omega=\ell(g)^*T(b\Omega)=\varphi(b)\,\ell(g)^*(g'\otimes\eta)+\ell(g)^*(\zeta_+\otimes g'\otimes\eta)=\varphi(b)\langle g',g\rangle\eta,
\]
because every tensor in \(\zeta_+\) begins with a vector of \(K_0\perp g\).

(3) This is Step 1 of the proof of Theorem 3.2 for \(L=\ell(e)\), which satisfies \(L^*L=1\). \(\square\)

**Theorem 4.2** (free semicircular families). Let \(e_1,\ldots,e_m\) be an orthonormal basis of \(H\), \(s_j=s(e_j)\) and \(\mathcal S=W^*(s_1,\ldots,s_m)\).

1. With respect to \(\varphi\), each \(s_j\) has the moments of \(\sigma\), and the algebras of polynomials in \(s_1,\ldots,s_m\) form a free family.
2. \(\Omega\) is cyclic for \(\mathcal S\), and \(\varphi\) restricts to a faithful normal tracial state on \(\mathcal S\).
3. With respect to \(\varphi\), each \(s_j\) is semicircular and \(W^*(s_1),\ldots,W^*(s_m)\) are free; there is a trace-preserving normal isomorphism \(L(\mathbb F_m)\to\mathcal S\) with \(\lambda(x_j)\mapsto e^{2\pi iF_\sigma(s_j)}\), where \(F_\sigma\) is the distribution function of \(\sigma\).

**Proof.** (1) Fix \(j\) and a set \(J\) of indices not containing \(j\); let \(K_0\) be the span of the \(e_r\), \(r\in J\), and \(\mathcal D\) the \(*\)-algebra generated by the \(s_r\), \(r\in J\), which lies in \(\mathcal S(K_0)\). By Lemma 4.1(1)-(2) with \(g=g'=e_j\), the operator \(L=\ell(e_j)\) satisfies (a)-(c) of Theorem 3.2 with \(\xi=\Omega\). So \(s_j\) has the moments of \(\sigma\), and the polynomials in \(s_j\) are free from \(\mathcal D\). By induction on the number of indices, using this and Lemma 3.1, every subfamily of \((s_1,\ldots,s_m)\) is free.

(2) Let \(\eta=e_{j_1}^{\otimes n_1}\otimes\cdots\otimes e_{j_k}^{\otimes n_k}\) with \(n_i\ge1\) and \(j_i\ne j_{i+1}\). Applying Lemma 4.1(3) from the right, \(\eta=U_{n_1}(s_{j_1})\cdots U_{n_k}(s_{j_k})\Omega\): at each step the vector already built begins with \(e_{j_{i+1}}\perp e_{j_i}\), or is \(\Omega\). These tensors span a dense subspace, so \(\Omega\) is cyclic. Now let \(h_1,\ldots,h_m\) be the free generators of \(L(\mathbb F_m)\), \(\theta(e^{2\pi is})=s\) for \(s\in[0,1)\), and \(t_j=F_\sigma^{-1}(\theta(h_j))\), where \(F_\sigma^{-1}\colon[0,1]\to[-2,2]\) is the inverse of \(F_\sigma\) (Lemma 2.1(4)). The distribution of \(\theta(h_j)\) is the uniform distribution on \([0,1]\), so \(t_j\) is semicircular, and \(W^*(t_j)\subseteq W^*(h_j)\); the \(W^*(t_j)\) are free (Corollary 2.5(3) of the first lesson). For each \(j\), \(p(s_j)\mapsto p(t_j)\) is a well-defined \(*\)-homomorphism compatible with the states: if \(p(s_j)=0\), then \(\int|p|^2d\sigma=\varphi(p(s_j)^*p(s_j))=0\), so \(p\) vanishes on \([-2,2]\) and is the zero polynomial. By Lemma 1.2(3) of the first lesson (for states),
\[
\varphi(P(s_1,\ldots,s_m))=\tau(P(t_1,\ldots,t_m))
\]
for every noncommutative polynomial \(P\). Hence \(\varphi\) is tracial on the \(*\)-algebra \(\mathcal S_0\) generated by the \(s_j\), and \(P(s)\Omega\mapsto P(t)\Omega_\tau\) is a well-defined isometry from the dense subspace \(\mathcal S_0\Omega\) of \(\mathcal F(H)\) into \(L^2(L(\mathbb F_m))\). By Lemma 1.2, \(W^*(t_j)=W^*(e^{2\pi iF_\sigma(t_j)})=W^*(h_j)\), because \(F_\sigma(t_j)=\theta(h_j)\) by Lemma 1.1; so the \(t_j\) generate \(L(\mathbb F_m)\), and the isometry has dense range (Lemma 1.4 of the first lesson). It extends to a unitary \(V\) with \(V\Omega=\Omega_\tau\) and \(Vs_jV^*=L_{t_j}\). Thus \(x\mapsto V xV^*\) is a normal \(*\)-isomorphism of \(\mathcal S\) onto the image of \(L(\mathbb F_m)\) under its left representation, with \(\varphi(x)=\tau(VxV^*)\). So \(\varphi\) is a faithful normal tracial state on \(\mathcal S\).

(3) Under this isomorphism \(s_j\) corresponds to \(t_j\), so \(s_j\) is semicircular, the \(W^*(s_j)\) are free, and \(e^{2\pi iF_\sigma(s_j)}\) corresponds to \(e^{2\pi iF_\sigma(t_j)}=h_j\). \(\square\)

We call \(\mathcal S\) the *semicircular algebra* of the basis \(e_1,\ldots,e_m\). If \(e=\sum_ja_je_j\) with real \(a_j\) and \(\|e\|=1\), then \(s(e)=\sum_ja_js_j\in\mathcal S\), and \(s(e)\) is semicircular: it has the moments of \(\sigma\) by part (1) applied to an orthonormal basis containing \(e\). Real coefficients matter. For instance \(s(ie_1)=i(\ell(e_1)-\ell(e_1)^*)\), so \(\ell(e_1)=\frac12(s(e_1)-is(ie_1))\) lies in the von Neumann algebra \(\mathcal S(H)\) generated by all \(s(e)\), \(e\in H\); but \(\ell(e_1)\notin\mathcal S\), and \(\varphi\) is not tracial on \(\mathcal S(H)\) (Exercise 5.3).

## 5. Exercises

**Exercise 5.1.** Show that \(\int f\,d\sigma=\frac1{2\pi}\int_{-2}^2f(t)\sqrt{4-t^2}\,dt\) for continuous \(f\).

**Exercise 5.2.** Compute \(\varphi(s(e)^4)\) and \(\varphi(s(e)^2s(e')^2)\), \(\varphi(s(e)s(e')s(e)s(e'))\) for orthonormal \(e,e'\), directly on the Fock space.

**Exercise 5.3.** In the setting of Theorem 4.2, show that \(\ell(e_1)\notin\mathcal S\), and that \(\varphi\) is not tracial on \(\mathcal S(H)\). (Hint: \(\varphi\) is tracial on \(\mathcal S\).)

**Exercise 5.4.** Let \(e,e'\in H\) be orthonormal and \(c=\ell(\frac{e+ie'}{\sqrt2})+\ell(\frac{e-ie'}{\sqrt2})^*\). Show that \(c=\frac1{\sqrt2}(s(e)+is(e'))\), and that \(\frac{e+ie'}{\sqrt2}\) and \(\frac{e-ie'}{\sqrt2}\) are orthonormal.

## 6. Solutions

**5.1.** Substitute \(t=2\cos\phi\): \(dt=-2\sin\phi\,d\phi\) and \(\sqrt{4-t^2}=2\sin\phi\) on \([0,\pi]\), so \(\frac1{2\pi}\sqrt{4-t^2}\,dt\) becomes \(\frac2\pi\sin^2\phi\,d\phi\).

**5.2.** Write \(\ell=\ell(e)\), \(\ell'=\ell(e')\). In \(s(e)^4\Omega\), only the words that never apply an annihilation to \(\Omega\) and end at \(\Omega\) contribute: \(\ell^*\ell^*\ell\ell\) and \(\ell^*\ell\ell^*\ell\), so \(\varphi(s(e)^4)=2=\mathrm{Cat}_2\). Similarly \(\varphi(s(e)^2s(e')^2)=\langle s(e')^2\Omega,s(e)^2\Omega\rangle=\langle e'\otimes e'+\Omega,e\otimes e+\Omega\rangle=1\), and \(\varphi(s(e)s(e')s(e)s(e'))=\langle s(e)s(e')\Omega,s(e')s(e)\Omega\rangle=\langle e\otimes e',e'\otimes e\rangle=0\), as freeness predicts (Exercise 5.1 of the first lesson).

**5.3.** If \(\ell(e_1)\in\mathcal S\), then, \(\varphi\) being tracial on \(\mathcal S\), \(1=\varphi(\ell(e_1)^*\ell(e_1))=\varphi(\ell(e_1)\ell(e_1)^*)=\|\ell(e_1)^*\Omega\|^2=0\), a contradiction. Since \(s(e_1)-is(ie_1)=2\ell(e_1)\), the operator \(\ell(e_1)\) lies in \(\mathcal S(H)\), and the same computation shows that \(\varphi\) is not tracial on \(\mathcal S(H)\).

**5.4.** \(\ell(\cdot)\) is linear and \(\ell(\cdot)^*\) conjugate linear, so \(\ell(\frac{e+ie'}{\sqrt2})+\ell(\frac{e-ie'}{\sqrt2})^*=\frac1{\sqrt2}\big(\ell(e)+i\ell(e')+\ell(e)^*+i\ell(e')^*\big)=\frac1{\sqrt2}(s(e)+is(e'))\). Also \(\langle e+ie',e-ie'\rangle=1+i\cdot i=0\) and both vectors have norm \(\sqrt2\).

## References

- [OAI] OpenAI, *An isomorphism of the free group factors* (September 23, 2026), OpenAI Math Release preprint, Theorem 1.2. https://github.com/openai/math/blob/main/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf
- [Sp] R. Speicher, *Lecture notes on "Free probability theory"*, arXiv 1908.08125, the sections on the free group factors and on the compression of free group factors, where the corner \(L(\mathbb F_2)_{1/2}\cong L(\mathbb F_5)\) is derived with random matrices. https://arxiv.org/abs/1908.08125
