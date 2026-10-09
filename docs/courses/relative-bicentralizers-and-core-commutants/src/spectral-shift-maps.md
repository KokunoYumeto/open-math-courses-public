# Spectral shift maps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson proved the binormal identity for states of \(B(L^2(M))\) concentrated at modular energy zero. This lesson moves the energy. For each \(s\in\mathbb R\) we construct a unital completely positive map \(\theta_s\) of \(B(L^2(M))\), in general not normal, that fixes the Jones projection and the right action of \(M\), acts on the left action of \(M\) by the relative bicentralizer flow composed with the expectation onto the relative bicentralizer, and translates the modular energy by \(s\) [M2, Lemma 2.2]. Composing a state concentrated at energy \(s\) with \(\theta_s\) gives a state concentrated at energy zero, and the binormal identity becomes \(\Phi(\gamma_s(a)\rho(b))=\langle a\xi b,\xi\rangle\) (Corollary 5.1).

The maps are limits of averaged conjugations: by unitaries of \(N\) that almost commute with \(\varphi\) for \(s=0\) (Proposition 3.1), and by rows of elements of \(N\) that almost satisfy \(v\varphi=e^{-s}\varphi v\) in general (Theorem 4.1). The modular energy is controlled by an explicit estimate: an element \(v\) with \(v\varphi\) close to \(e^{-s}\varphi v\) in norm is close to a modular eigenvector, \(\sigma_t(v)\approx e^{its}v\) (Proposition 1.2). It follows from the estimate for elements almost commuting with a state, proved in the ultraproduct lesson after Connes, by a two-by-two matrix trick. It also gives the equivalence of the two descriptions of modular frequency announced in the lesson on the relative flow (Corollary 1.3).

We use: Theorem 3.4(3) and formula (1.1) of [The relative bicentralizer](the-relative-bicentralizer.md); Theorem 3.1, formula (3.2) and the admissible families of Section 3 of [Transition isomorphisms and the relative flow](transition-isomorphisms-and-the-relative-flow.md); Section 1 and Theorem 5.1 of [Binormal states and the relative bicentralizer](binormal-states-and-the-relative-bicentralizer.md); Corollary 6.3 and Theorem 6.5 of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#6-almost-commuting-with-varphi-means-almost-fixed-by-the-modular-group); Proposition 4.1 of [Asymptotic centralizers of type III₁ factors](course:bicentralizers-of-type-iii1-factors/asymptotic-centralizers-of-type-iii1-factors#4-approximate-eigenoperators); Lemma 1.1 of [Modular averaging and bounded recovery](course:bicentralizers-of-type-iii1-factors/modular-averaging-and-bounded-recovery#1-notation-and-two-modular-estimates); the modular theorem, [The modular group and its analytic algebra, §MF-06](course:OA-MOD/OA-MOD-MF#OA-MOD-MF-06); the multiplicative domain theorem, Theorem 4.1(3) of [Completely positive maps](course:foundations-of-von-neumann-algebras/completely-positive-maps#OA-FND-CM-07); and Tychonoff's and the Banach–Alaoglu theorems, [Weak topologies, Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian).

## 1. Approximate eigenoperators

Throughout this section \(N\) is a von Neumann algebra with a faithful normal state \(\varphi\), GNS space \(H_\varphi\), cyclic and separating vector \(\xi_\varphi\), modular operator \(\Delta_\varphi\) and modular group \(\sigma_t=\sigma^\varphi_t\). We write \(\|y\|_\varphi=\|y\xi_\varphi\|\), \(\|y\|^\sharp_\varphi=(\|y\|_\varphi^2+\|y^*\|_\varphi^2)^{1/2}\), and use the bimodule notation \((y\varphi)(x)=\varphi(xy)\), \((\varphi y)(x)=\varphi(yx)\) for the predual.

Let \(\lambda>0\), \(P=N\otimes M_2(\mathbb C)\), whose elements are matrices \(Y=\sum_{i,j}y_{ij}\otimes e_{ij}\) with \(y_{ij}\in N\), and
\[
\theta(Y)=h_1\varphi(y_{11})+h_2\varphi(y_{22}),\qquad h_1=\frac1{1+\lambda},\quad h_2=\frac\lambda{1+\lambda}.
\]

**Lemma 1.1.** \(\theta\) is a faithful normal state of \(P\), and for \(y\in N\), \(t\in\mathbb R\) and \(i,j\in\{1,2\}\),
\[
\sigma^\theta_t(y\otimes e_{ij})=(h_i/h_j)^{it}\,\sigma_t(y)\otimes e_{ij};\qquad\text{in particular}\qquad\sigma^\theta_t(y\otimes e_{21})=\lambda^{it}\sigma_t(y)\otimes e_{21}.
\]

**Proof.** Let \(K\) be the direct sum of four copies \(H_{ij}\) of \(H_\varphi\), indexed by \(i,j\in\{1,2\}\), and let \(P\) act on \(K\) by matrix multiplication: \((Y\eta)_{ij}=\sum_ky_{ik}\eta_{kj}\). This is a faithful normal representation, and its image is a von Neumann algebra. Let \(\Xi\in K\) have components \(\Xi_{ij}=\delta_{ij}h_j^{1/2}\xi_\varphi\). Then \((Y\Xi)_{ij}=h_j^{1/2}y_{ij}\xi_\varphi\), so \(\langle Y\Xi,\Xi\rangle=\sum_ih_i\varphi(y_{ii})=\theta(Y)\). The vectors \(Y\Xi\) fill the dense subspace \(\bigoplus_{i,j}N\xi_\varphi\), and \(Y\Xi=0\) forces every \(y_{ij}\xi_\varphi=0\), hence \(Y=0\). So \(\Xi\) is cyclic and separating, \(\theta\) is a faithful normal state, and \((K,\Xi)\) is its GNS representation.

The Tomita map \(S\colon Y\Xi\mapsto Y^*\Xi\) sends the component \(h_i^{1/2}y_{ji}\xi_\varphi\) in \(H_{ji}\) to the component \(h_j^{1/2}y_{ji}^*\xi_\varphi\) in \(H_{ij}\). So \(S\) is the direct sum, over the ordered pairs \((j,i)\), of the maps \((h_j/h_i)^{1/2}S_\varphi\colon H_{ji}\to H_{ij}\), where \(S_\varphi y\xi_\varphi=y^*\xi_\varphi\). A finite direct sum of closable operators has as closure the direct sum of the closures and as adjoint the direct sum of the adjoints. Hence \(\bar S^*\bar S\) acts on \(H_{ji}\) as \((h_j/h_i)\bar S_\varphi^*\bar S_\varphi=(h_j/h_i)\Delta_\varphi\), and the modular operator of \(\theta\) is \(\Delta_\theta=\bigoplus_{i,j}(h_i/h_j)\Delta_\varphi\), with \((h_i/h_j)\Delta_\varphi\) acting on \(H_{ij}\). By the modular theorem, \(\sigma^\theta_t(Y)\Xi=\Delta_\theta^{it}Y\Xi\). For \(Y=y\otimes e_{ij}\) the vector \(Y\Xi\) is \(h_j^{1/2}y\xi_\varphi\) in \(H_{ij}\), so
\[
\Delta_\theta^{it}Y\Xi=(h_i/h_j)^{it}h_j^{1/2}\Delta_\varphi^{it}y\xi_\varphi=(h_i/h_j)^{it}h_j^{1/2}\sigma_t(y)\xi_\varphi\ \text{ in }H_{ij},
\]
which is the vector of \((h_i/h_j)^{it}\sigma_t(y)\otimes e_{ij}\). Since \(\Xi\) is separating, this proves the formula. Finally \(h_2/h_1=\lambda\). \(\square\)

**Proposition 1.2** (approximate eigenoperators). Let \(v\in N\), \(\lambda>0\) and \(\varepsilon=\|v\varphi-\lambda\varphi v\|\). For every \(t\in\mathbb R\), \(w=\lambda^{it}\sigma_t(v)-v\) satisfies
\[
\|w\|_\varphi^2+\lambda\|w^*\|_\varphi^2\le512\,(1+|t|)^2\,\|v\|\,\varepsilon .
\]
In the logarithmic parametrization \(\lambda=e^{-s}\),
\[
\|\sigma_t(v)-e^{its}v\|_\varphi^2+e^{-s}\big\|(\sigma_t(v)-e^{its}v)^*\big\|_\varphi^2\le512\,(1+|t|)^2\,\|v\|\,\|v\varphi-e^{-s}\varphi v\| .
\]

**Proof.** We may assume \(v\ne0\). Let \(V=v\otimes e_{21}\in P\) and \(Y=\sum_{i,j}y_{ij}\otimes e_{ij}\in P\). Then \(VY=\sum_jvy_{1j}\otimes e_{2j}\) and \(YV=\sum_iy_{i2}v\otimes e_{i1}\), so
\[
(V\theta-\theta V)(Y)=\theta(YV)-\theta(VY)=h_1\big(\varphi(y_{12}v)-\lambda\varphi(vy_{12})\big)=h_1(v\varphi-\lambda\varphi v)(y_{12}).
\]
Since \(\|y_{12}\|\le\|Y\|\), \(\|[V,\theta]\|\le h_1\varepsilon\). Theorem 6.5 of the ultraproduct lesson, applied to \((P,\theta)\) and \(V\), gives \(\|\sigma^\theta_t(V)-V\|^\sharp_\theta\le16\sqrt2\,(1+|t|)\,\|v\|^{1/2}(h_1\varepsilon)^{1/2}\). By Lemma 1.1, \(\sigma^\theta_t(V)-V=w\otimes e_{21}\). Its squared \(\sharp\)-norm is
\[
\theta(w^*w\otimes e_{11})+\theta(ww^*\otimes e_{22})=h_1\|w\|_\varphi^2+h_2\|w^*\|_\varphi^2=h_1\big(\|w\|_\varphi^2+\lambda\|w^*\|_\varphi^2\big).
\]
Divide by \(h_1\). The second form follows because \(\sigma_t(v)-e^{its}v=e^{its}w\) when \(\lambda=e^{-s}\). \(\square\)

**Corollary 1.3** (modular frequency). For \(v\in N\) and \(s\in\mathbb R\), \(v\varphi=e^{-s}\varphi v\) if and only if \(\sigma_t(v)=e^{its}v\) for all \(t\in\mathbb R\).

**Proof.** If \(v\varphi=e^{-s}\varphi v\), Proposition 1.2 gives \(\sigma_t(v)\xi_\varphi=e^{its}v\xi_\varphi\), and \(\xi_\varphi\) is separating. Conversely, if \(\sigma_t(v)=e^{its}v\) for all \(t\), then \(\Delta_\varphi^{it}v\xi_\varphi=e^{its}v\xi_\varphi\), so \(v\xi_\varphi\) has spectral support \(\{s\}\) for \(\log\Delta_\varphi\). Lemma 1.1 of the modular averaging lesson gives \(\|\varphi v-e^sv\varphi\|\le(1+e^{s/2})\|(e^{\log\Delta_\varphi/2}-e^{s/2})v\xi_\varphi\|=0\), that is \(v\varphi=e^{-s}\varphi v\). \(\square\)

**Corollary 1.4.** Let \((v_n)\) be a bounded sequence in \(N\) with \(\|v_n\varphi-e^{-s}\varphi v_n\|\to0\). Then for every \(T>0\),
\[
\sup_{|t|\le T}\|\sigma_t(v_n)-e^{its}v_n\|^\sharp_\varphi\to0 .
\]

**Proof.** Proposition 1.2, with \(\|v_n\|\) bounded and \((1+|t|)\le1+T\). \(\square\)

## 2. Completely positive maps on B(H)

For a Hilbert space \(H\) let \(\mathrm{UCP}(B(H))\) be the set of unital completely positive linear maps \(B(H)\to B(H)\), not required to be normal. Such a map \(\Theta\) is contractive: for \(T\in B(H)\) the operator matrix \(\begin{pmatrix}\|T\|&T\\T^*&\|T\|\end{pmatrix}\) is positive, hence so is \(\begin{pmatrix}\|T\|&\Theta(T)\\\Theta(T)^*&\|T\|\end{pmatrix}\), and testing it on vectors \((\eta,-\Theta(T)^*\eta/\|T\|)\) gives \(\|\Theta(T)^*\eta\|\le\|T\|\,\|\eta\|\). A completely positive map \(\Theta\), not necessarily unital, satisfies in the same way \(\|\Theta(T)\|\le\|\Theta(1)\|\,\|T\|\). We give \(\mathrm{UCP}(B(H))\) the *point-weak\(^*\) topology*: \(\Theta_i\to\Theta\) when \(\Theta_i(T)\to\Theta(T)\) \(\sigma\)-weakly for every \(T\). On bounded sets of \(B(H)\) the \(\sigma\)-weak topology is the weak operator topology.

**Lemma 2.1.** \(\mathrm{UCP}(B(H))\) is compact in the point-weak\(^*\) topology. If \(\Theta_i\to\Theta\) point-weak\(^*\) and \(A,B\in B(H)\), then \(A\Theta_i(T)B\to A\Theta(T)B\) \(\sigma\)-weakly for every \(T\). If \(\Theta_n\) are completely positive maps with \(\sup_n\|\Theta_n(1)\|<\infty\) and \(\Theta_n(1)\to1\) strongly, and \(\omega\) is a free ultrafilter on \(\mathbb N\), then \(\Theta(T)=\sigma\text{-weak}\lim_{n\to\omega}\Theta_n(T)\) defines an element of \(\mathrm{UCP}(B(H))\).

**Proof.** By contractivity, \(\mathrm{UCP}(B(H))\) is a subset of the product \(\prod_T\{S:\|S\|\le\|T\|\}\) of \(\sigma\)-weakly compact balls (Banach–Alaoglu), which is compact by Tychonoff's theorem. It is closed: linearity, \(\Theta(1)=1\), and positivity of the matrices \((\Theta(T_{kl}))_{k,l}\) for positive \((T_{kl})\in M_n(B(H))\) are preserved by pointwise \(\sigma\)-weak limits, positivity being tested on vectors. The second statement holds because \(S\mapsto ASB\) is \(\sigma\)-weakly continuous. For the third, the values \(\Theta_n(T)\) lie in a bounded set, so the limit along \(\omega\) exists; the limit map is linear and completely positive by the same tests, and \(\Theta(1)=1\) because \(\Theta_n(1)\to1\) strongly. \(\square\)

## 3. The zero-shift map

In this section and the next we use the setting of Section 5 of the previous lesson: \(N\subset M\) with a faithful normal conditional expectation \(E\), \(M\) countably decomposable, \(\varphi\) a faithful normal state on \(N\), \(\bar\varphi=\varphi\circ E\), \(H=L^2(M,\bar\varphi)\) with vector \(\xi\), \(X=\log\Delta\), \(\rho(b)=Jb^*J\), \(e_N\) the Jones projection, \(\mathrm B=\mathrm B(N\subset M,\varphi)\) and \(E_{\mathrm B}\) its \(\bar\varphi\)-preserving expectation. Elements of \(M\) act on \(H\) on the left, and \(N'\) denotes the commutant of \(N\) in \(B(H)\); it contains \(\rho(M)\) and \(e_N\), because the closure of \(N\xi\) is invariant under \(N\). By (1.1) of the first lesson, \(\sigma^{\bar\varphi}_t\) restricts to \(\sigma^\varphi_t\) on \(N\), and \(\|y\|_{\bar\varphi}=\|y\|_\varphi\) for \(y\in N\). We write \(\sigma_t=\sigma^{\bar\varphi}_t\).

**Proposition 3.1** (Marrakchi). There is \(\zeta\in\mathrm{UCP}(B(H))\) such that

1. \(\zeta(e_N)=e_N\);
2. \(\zeta(a)=E_{\mathrm B}(a)\) for \(a\in M\);
3. \(\zeta(T_1TT_2)=T_1\zeta(T)T_2\) for \(T\in B(H)\) and \(T_1,T_2\) in the commutant \(N'\) of the left action of \(N\) on \(H\); in particular \(\zeta\circ\rho=\rho\);
4. \(\zeta(f(X))=f(X)\) for \(f\in C_0(\mathbb R)\);
5. \(\zeta(\Delta^{it})=\Delta^{it}\) for \(t\in\mathbb R\).

**Proof.** *An averaging net.* Let \(I\) be the set of triples \(i=(\delta,S,\varepsilon)\) with \(\delta,\varepsilon>0\) and \(S\subset M\) finite, directed by \((\delta,S,\varepsilon)\le(\delta',S',\varepsilon')\) when \(\delta'\le\delta\), \(S\subset S'\) and \(\varepsilon'\le\varepsilon\). By Theorem 3.4(3) of the first lesson, for each \(i\) there is a finitely supported probability measure \(\mu_i\) on \(\mathcal U_\delta=\{u\in\mathcal U(N):\|[u,\varphi]\|<\delta\}\) with \(\|\int uxu^*\,d\mu_i(u)-E_{\mathrm B}(x)\|^\sharp_{\bar\varphi}<\varepsilon\) for \(x\in S\). For each \(x\in M\), the bounded net \(\int uxu^*\,d\mu_i(u)\) converges to \(E_{\mathrm B}(x)\) in \(\|\cdot\|^\sharp_{\bar\varphi}\), hence \(*\)-strongly: for \(y'\in M'\), \(\|(z_i-z)y'\xi\|\le\|y'\|\,\|(z_i-z)\xi\|\), and \(M'\xi\) is dense.

Put \(\Theta_i(T)=\int uTu^*\,d\mu_i(u)\), a finite convex combination of unitary conjugations, so \(\Theta_i\in\mathrm{UCP}(B(H))\). By Lemma 2.1, a subnet of \((\Theta_i)\) converges point-weak\(^*\) to some \(\zeta\in\mathrm{UCP}(B(H))\).

(1) Unitaries of \(N\) commute with \(e_N\), so \(\Theta_i(e_N)=e_N\). (2) \(\Theta_i(a)=\int uau^*\,d\mu_i\to E_{\mathrm B}(a)\) strongly. (3) Unitaries of \(N\) commute with \(T_1,T_2\in N'\), so \(\Theta_i(T_1TT_2)=T_1\Theta_i(T)T_2\); pass to the limit with Lemma 2.1. The right action \(\rho(M)\) lies in \(N'\).

(4) First let \(f(x)=\int h(t)e^{itx}dt\) with \(h\in L^1(\mathbb R)\), so that \(f(X)=\int h(t)\Delta^{it}dt\) strongly. Since \(\Delta^{it}u^*=\sigma_t(u^*)\Delta^{it}\),
\[
\Theta_i(f(X))=\int h(t)A_i(t)\Delta^{it}\,dt,\qquad A_i(t)=\int u\,\sigma_t(u)^*\,d\mu_i(u).
\]
For \(u\in\mathcal U_\delta\) and \(y'\in M'\), \((u\sigma_t(u)^*-1)y'\xi=y'u(\sigma_t(u)-u)^*\xi\), so by Corollary 6.3 of the ultraproduct lesson, applied to \((N,\varphi)\),
\[
\|(A_i(t)-1)y'\xi\|\le\|y'\|\sup_{u\in\mathcal U_\delta}\|\sigma_t(u)-u\|^\sharp_\varphi\le2\,C_t^{1/2}\delta^{1/2}\,\|y'\| ,
\]
where \(C_t=8t^2+5|t|+8\). Since \(\|A_i(t)-1\|\le2\) and \(M'\xi\) is dense, \(A_i(t)\to1\) strongly, uniformly for \(|t|\le T\) on each fixed vector, for every \(T\). For \(\eta\in H\), the set \(\{\Delta^{it}\eta:|t|\le T\}\) is norm compact; covering it by finitely many balls of radius \(r\) gives \(\limsup_i\sup_{|t|\le T}\|(A_i(t)-1)\Delta^{it}\eta\|\le2r\) for every \(r>0\). Hence
\[
\limsup_i\|(\Theta_i(f(X))-f(X))\eta\|\le\limsup_i\int_{|t|\le T}|h(t)|\,\|(A_i(t)-1)\Delta^{it}\eta\|\,dt+2\|\eta\|\int_{|t|>T}|h|=2\|\eta\|\int_{|t|>T}|h|,
\]
which tends to \(0\) as \(T\to\infty\). So \(\Theta_i(f(X))\to f(X)\) strongly and \(\zeta(f(X))=f(X)\). Such \(f\) include every \(f\in C_c^\infty(\mathbb R)\), whose inverse Fourier transform is integrable, and \(C_c^\infty(\mathbb R)\) is uniformly dense in \(C_0(\mathbb R)\). Both sides of (4) are contractive in \(f\) for the supremum norm, so (4) holds for all \(f\in C_0(\mathbb R)\).

(5) \(\Theta_i(\Delta^{it})=A_i(t)\Delta^{it}\to\Delta^{it}\) strongly, as shown in the proof of (4). \(\square\)

## 4. The shift maps

From now on \(N\) is moreover a factor of type III₁ with separable predual, so that the relative bicentralizer flow \(\gamma_s=\gamma^\varphi_s=\beta^\varphi_{e^{-s}}\) of the lesson on the relative flow is defined on \(\mathrm B\). Recall that an *admissible \(\lambda\)-family with ordinary convergence* is a finite family of bounded sequences \((v_{k,n})_n\) in \(N\), \(1\le k\le m\), with \(\|v_{k,n}\varphi-\lambda\varphi v_{k,n}\|\to0\) and \(\|1-\sum_kv_{k,n}v_{k,n}^*\|^\sharp_\varphi\to0\). Such families exist for every \(\lambda>0\) by Proposition 4.1 of the asymptotic centralizer lesson, and by Theorem 3.1(1) of the lesson on the relative flow, \(\sum_kv_{k,n}xv_{k,n}^*\to\beta^\varphi_\lambda(x)\) \(*\)-strongly for \(x\in\mathrm B\).

**Theorem 4.1** (Marrakchi). For every \(s\in\mathbb R\) there is \(\theta_s\in\mathrm{UCP}(B(H))\) such that

1. \(\theta_s(e_N)=e_N\);
2. \(\theta_s(a)=\gamma_s(E_{\mathrm B}(a))\) for \(a\in M\);
3. \(\theta_s(T_1TT_2)=T_1\theta_s(T)T_2\) for \(T\in B(H)\) and \(T_1,T_2\in N'\); in particular \(\theta_s\circ\rho=\rho\);
4. \(\theta_s(f(X))=f(X-s)\) for \(f\in C_0(\mathbb R)\);
5. \(\theta_s(\Delta^{it})=e^{-its}\Delta^{it}\) for \(t\in\mathbb R\).

**Proof.** Let \(\zeta\) be as in Proposition 3.1, let \((v_{k,n})\) be an admissible \(e^{-s}\)-family with ordinary convergence, \(\|v_{k,n}\|\le c\), and \(\omega\) a free ultrafilter on \(\mathbb N\). Put
\[
\Theta_n(T)=\sum_{k=1}^mv_{k,n}\,\zeta(T)\,v_{k,n}^*,\qquad\theta_s(T)=\sigma\text{-weak}\lim_{n\to\omega}\Theta_n(T).
\]
Each \(\Theta_n\) is completely positive with \(\Theta_n(1)=\sum_kv_{k,n}v_{k,n}^*\), of norm at most \(mc^2\). This sequence tends to \(1\) strongly: \(\|(1-\sum_kv_{k,n}v_{k,n}^*)y'\xi\|\le\|y'\|\,\|1-\sum_kv_{k,n}v_{k,n}^*\|_\varphi\to0\) for \(y'\in M'\), and the sequence is bounded. By Lemma 2.1, \(\theta_s\in\mathrm{UCP}(B(H))\).

(1) \(\Theta_n(e_N)=\sum_kv_{k,n}e_Nv_{k,n}^*=e_N\Theta_n(1)\to e_N\) strongly. (2) \(\Theta_n(a)=\sum_kv_{k,n}E_{\mathrm B}(a)v_{k,n}^*\to\beta^\varphi_{e^{-s}}(E_{\mathrm B}(a))=\gamma_s(E_{\mathrm B}(a))\) strongly. (3) The \(v_{k,n}\) commute with \(T_1,T_2\in N'\), and \(\zeta\) has property (3).

(4) Let \(f(x)=\int h(t)e^{itx}dt\) with \(h\in L^1(\mathbb R)\). By Proposition 3.1(4) and \(\Delta^{it}v^*=\sigma_t(v)^*\Delta^{it}\),
\[
\Theta_n(f(X))=\sum_kv_{k,n}f(X)v_{k,n}^*=\int h(t)A_n(t)\Delta^{it}\,dt,\qquad A_n(t)=\sum_kv_{k,n}\sigma_t(v_{k,n})^* .
\]
Now \(A_n(t)-e^{-its}\Theta_n(1)=\sum_kv_{k,n}\big(\sigma_t(v_{k,n})-e^{its}v_{k,n}\big)^*\). For \(y'\in M'\), Corollary 1.4 gives
\[
\sup_{|t|\le T}\big\|\big(A_n(t)-e^{-its}\Theta_n(1)\big)y'\xi\big\|\le\|y'\|\,c\sum_k\sup_{|t|\le T}\big\|\sigma_t(v_{k,n})-e^{its}v_{k,n}\big\|^\sharp_\varphi\to0 .
\]
Also \(\|A_n(t)\|\le\|\sum_kv_{k,n}v_{k,n}^*\|^{1/2}\|\sum_k\sigma_t(v_{k,n}v_{k,n}^*)\|^{1/2}\le mc^2\), and \(\Theta_n(1)\to1\) strongly. As in the proof of Proposition 3.1, \(\sup_{|t|\le T}\|(A_n(t)-e^{-its})\Delta^{it}\eta\|\to0\) for every \(\eta\in H\) and \(T>0\), and therefore
\[
\Theta_n(f(X))\to\int h(t)e^{-its}\Delta^{it}\,dt=f(X-s)\quad\text{strongly}.
\]
Hence \(\theta_s(f(X))=f(X-s)\) for these \(f\), and by density for all \(f\in C_0(\mathbb R)\).

(5) By Proposition 3.1(5), \(\Theta_n(\Delta^{it})=\sum_kv_{k,n}\Delta^{it}v_{k,n}^*=A_n(t)\Delta^{it}\), which tends strongly to \(e^{-its}\Delta^{it}\). \(\square\)

By the multiplicative domain theorem, [Completely positive maps, Theorem 4.1(3)](course:foundations-of-von-neumann-algebras/completely-positive-maps#OA-FND-CM-07), properties (4) and (5) give more: \(\theta_s(f(X)^*f(X))=\theta_s(f(X))^*\theta_s(f(X))\), and likewise for \(f(X)f(X)^*\) and for the unitaries \(\Delta^{it}\), so
\[
\theta_s(f(X)T)=f(X-s)\theta_s(T),\qquad\theta_s(\Delta^{it}T\Delta^{it'})=e^{-i(t+t')s}\Delta^{it}\theta_s(T)\Delta^{it'}
\tag{4.1}
\]
for \(f\in C_0(\mathbb R)\), \(T\in B(H)\) and \(t,t'\in\mathbb R\), and similarly with \(f(X)\) on the right.

The maps \(\theta_s\) depend on the choices made, and the theorem asserts only their existence. For \(s=0\) one may take \(\theta_0=\zeta\), because \(\gamma_0=\mathrm{id}\).

## 5. The binormal identity at a nonzero frequency

**Corollary 5.1.** Let \(N\) be a factor of type III₁ with separable predual, \(N\subset M\) with a faithful normal conditional expectation, \(M\) with separable predual, and \(s\in\mathbb R\). Let \(\Phi\) be a state of \(B(H)\) such that \(\Phi(y)=\Phi(\rho(y))=\bar\varphi(y)\) for \(y\in M\), \(\Phi(e_N)=1\), and \(\Phi(g(X))=g(s)\) for \(g\in C_0(\mathbb R)\). Then
\[
\Phi\big(\gamma_s(a)\rho(b)\big)=\langle a\xi b,\xi\rangle\qquad(a\in\mathrm B,\ b\in M).
\]

**Proof.** Let \(\theta_s\) be as in Theorem 4.1 and \(\Phi'=\Phi\circ\theta_s\). For \(y\in M\), \(\Phi'(y)=\bar\varphi(\gamma_s(E_{\mathrm B}(y)))=\bar\varphi(y)\), since \(\gamma_s\) preserves \(\bar\varphi\) on \(\mathrm B\) (Theorem 3.1(3) of the lesson on the relative flow) and \(E_{\mathrm B}\) preserves \(\bar\varphi\). Also \(\Phi'(\rho(y))=\Phi(\rho(y))=\bar\varphi(y)\), \(\Phi'(e_N)=\Phi(e_N)=1\), and for \(g\in C_0(\mathbb R)\), \(\Phi'(g(X))=\Phi(g(X-s))=g(0)\), because \(x\mapsto g(x-s)\) lies in \(C_0(\mathbb R)\). By Theorem 5.1 of the previous lesson, \(\Phi'(a\rho(b))=\langle a\xi b,\xi\rangle\) for \(a\in\mathrm B\) and \(b\in M\). By Theorem 4.1(2),(3), \(\Phi'(a\rho(b))=\Phi(\theta_s(a)\rho(b))=\Phi(\gamma_s(a)\rho(b))\), because \(E_{\mathrm B}(a)=a\). \(\square\)

## 6. Exercises

**Exercise 6.1.** Let \(N=M_2(\mathbb C)\) and \(\varphi=\operatorname{Tr}(k\,\cdot)\) with \(k=\operatorname{diag}(k_1,k_2)\), \(k_1,k_2>0\), \(k_1+k_2=1\). Compute \(e_{12}\varphi\) and \(\varphi e_{12}\), and check Corollary 1.3 for \(v=e_{12}\), using \(\sigma_t(x)=k^{it}xk^{-it}\).

**Exercise 6.2.** Show that \(\theta_s\circ\theta_{s'}\) satisfies (1)–(4) of Theorem 4.1 with \(s+s'\) in place of \(s\).

**Exercise 6.3.** Let \(N\) be a factor of type III₁ with separable predual. Show that \(\zeta(x)=\varphi(x)1\) for \(x\in N\), and that \(\Phi(x)=\varphi(x)\) for \(x\in N\) whenever \(\Phi\) is a state with \(\Phi\circ\zeta=\Phi\).

**Exercise 6.4.** In the setting of Section 1, let \(v\in N\), \(s\in\mathbb R\) and \(d>0\), and suppose that \(v\xi_\varphi\) has spectral support in \([s-d,s+d]\) for \(\log\Delta_\varphi\). Show that \(\|v\varphi-e^{-s}\varphi v\|\le(1+e^{-s/2})(e^{d/2}-1)\|v\|_\varphi\). Compare with Proposition 1.2.

## 7. Solutions

**6.1.** With \(\operatorname{Tr}(e_{12}A)=A_{21}\): \((e_{12}\varphi)(y)=\varphi(ye_{12})=\operatorname{Tr}(e_{12}ky)=k_2y_{21}\) and \((\varphi e_{12})(y)=\operatorname{Tr}(ke_{12}y)=k_1y_{21}\). So \(e_{12}\varphi=(k_2/k_1)\varphi e_{12}\), that is \(s=\log(k_1/k_2)\). On the other hand \(\sigma_t(e_{12})=k_1^{it}k_2^{-it}e_{12}=e^{its}e_{12}\).

**6.2.** Composition of unital completely positive maps is unital completely positive. (1) and (3) are clear. For \(a\in M\), \(\theta_s(\theta_{s'}(a))=\gamma_s(E_{\mathrm B}(\gamma_{s'}(E_{\mathrm B}(a))))=\gamma_{s+s'}(E_{\mathrm B}(a))\), because \(\gamma_{s'}(E_{\mathrm B}(a))\in\mathrm B\). For \(f\in C_0(\mathbb R)\), \(\theta_s(\theta_{s'}(f(X)))=\theta_s(g(X))\) with \(g(x)=f(x-s')\), which is \(g(X-s)=f(X-s-s')\).

**6.3.** By Corollary 2.6 of the first lesson, \(E_{\mathrm B}(x)=\varphi(x)1\) for \(x\in N\), and \(\zeta(x)=E_{\mathrm B}(x)\). Then \(\Phi(x)=\Phi(\zeta(x))=\varphi(x)\).

**6.4.** By Lemma 1.1 of the modular averaging lesson, \(\|\varphi v-e^sv\varphi\|\le(1+e^{s/2})\|(e^{\log\Delta_\varphi/2}-e^{s/2})v\xi_\varphi\|\). For \(|x-s|\le d\), \(|e^{x/2}-e^{s/2}|=e^{s/2}|e^{(x-s)/2}-1|\le e^{s/2}(e^{d/2}-1)\), so the right side is at most \((1+e^{s/2})e^{s/2}(e^{d/2}-1)\|v\|_\varphi\). Multiplying by \(e^{-s}\) gives \(\|v\varphi-e^{-s}\varphi v\|\le(1+e^{-s/2})(e^{d/2}-1)\|v\|_\varphi\). Spectral localization therefore controls the twisted commutator linearly in \(e^{d/2}-1\), while Proposition 1.2 recovers localization from a small twisted commutator only with a square root.

## References

- [M2] A. Marrakchi, Kadison's problem and ergodicity of the bicentralizer flow (2026). https://arxiv.org/abs/2606.23636
