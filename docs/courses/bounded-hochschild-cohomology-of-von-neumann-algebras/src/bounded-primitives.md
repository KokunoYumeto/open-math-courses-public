# Bounded primitives

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 1.2 of the lesson on the cohomology problem: for a von Neumann algebra \(M\) and \(k\ge2\), every bounded Hochschild cocycle \(f\in C_b^k(M,M)\) has a bounded primitive. First let \(f\) be separately normal and \(M\) of type \(\mathrm{II}_1\) with separable predual and faithful normal tracial state. Averaging \(f\) in its last variable along the random walk gives, in the limit, a map that is harmonic in that variable. The Liouville theorem makes it a right module map, and this yields a primitive \(g\) with \(\|g\|\le\|f\|\) (Section 1). The uniform bound allows a compactness argument that removes the separability assumption (Section 2). An explicit homotopy handles inputs that mix different central pieces (Section 3). Section 4 assembles the pieces, using the classical reductions K1 and K2.

**Prerequisites.** [*The cohomology problem*](the-cohomology-problem.md): Section 1, Lemmas 2.2 and 2.3, Exercise 4.4, and the reductions K1 and K2 of Section 3. [*A random walk with asymptotically free products*](a-random-walk-with-asymptotically-free-products.md): Theorem 3.1 and Lemma 2.3. [*The Liouville theorem*](the-liouville-theorem.md): Theorem 0.1. From *Measurable fields and direct integrals*: [*The central decomposition and the types of the fibres*](course:measurable-fields-and-direct-integrals/the-central-decomposition-and-the-types-of-the-fibres) (Facts 1.1, 1.6 and 1.7, Corollary 3.6, Theorems 4.1 and 5.3). From *Traces and noncommutative integration*: [*Integration for a trace, the commutation theorem and applications*](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications), Theorem 9.1 (trace-preserving conditional expectations). From *Foundations of von Neumann algebras*: [*Kaplansky's density theorem and its consequences*](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences) (Corollary 1.4, Theorem 7.1); [*The double commutant theorem*](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem) (Theorem 4.4); [*Compact and trace-class operators, the predual of B(H) and the operator topologies*](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies) (Theorems 9.1 and 9.4); [*Weak topologies*](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian) (Theorem 2.3, Tychonoff; Theorem 3.1, Banach–Alaoglu); [*Projections and types of von Neumann algebras*](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras) (Theorem 7.2, the type decomposition); [*The universal enveloping von Neumann algebra of a C\*-algebra and W\*-algebras*](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras) (Lemma 11.1, supports of normal functionals; Corollary 11.4).

**Conventions.** As in the lesson on the cohomology problem; throughout \(k\ge2\). For \(\mathbf a=(a_1,\ldots,a_{k-1})\in M^{k-1}\) and \(x\in M\), \((\mathbf a,x)\) is the \(k\)-tuple with last entry \(x\). A net \(\Phi_\lambda\) in \(C_b^k(M,M)\) converges *pointwise ultraweakly* to \(\Phi\) if \(\Phi_\lambda(\mathbf x)\to\Phi(\mathbf x)\) ultraweakly for every \(\mathbf x\in M^k\). For a probability measure \(\mu\) on \(\mathcal U(M)\) with countable support, with atoms \(s\) of mass \(\mu_s\), put
\[
(P_\mu\Phi)(\mathbf a,x)=\sum_s\mu_s\,\Phi(\mathbf a,xs)\,s^* ,
\]
a norm-convergent sum.

## 1. Averaging the last variable

**Lemma 1.1 (compactness).** Let \(c\ge0\) and \(\mathcal C=\{\Phi\in C_b^k(M,M):\|\Phi\|\le c\}\).

1. Every net in \(\mathcal C\) has a subnet converging pointwise ultraweakly to an element of \(\mathcal C\).
2. \(P_\mu\) maps \(\mathcal C\) into itself and is continuous on \(\mathcal C\) for pointwise ultraweak convergence.

**Proof.** (1) For each \(\mathbf x\), the values \(\Phi(\mathbf x)\), \(\Phi\in\mathcal C\), lie in the ball of radius \(c\prod_i\|x_i\|\), which is ultraweakly compact (Banach–Alaoglu, the ultraweak topology being \(\sigma(M,M_*)\)). By Tychonoff's theorem the product of these balls over all \(\mathbf x\in M^k\) is compact, so a subnet converges at every \(\mathbf x\). The limit is \(k\)-linear, since addition and multiplication by scalars are ultraweakly continuous, and it lies in \(\mathcal C\), since the balls are closed.

(2) The bound \(\|P_\mu\Phi\|\le\|\Phi\|\) is clear. Let \(\Phi_\lambda\to\Phi\) in \(\mathcal C\), fix \((\mathbf a,x)\) and \(\omega\in M_*\), and enumerate the atoms as \(s_1,s_2,\ldots\). For each \(j\), \(y\mapsto\omega(ys_j^*)\) is normal, so the first \(L\) terms of \(\omega((P_\mu\Phi_\lambda)(\mathbf a,x))\) converge to those of \(\omega((P_\mu\Phi)(\mathbf a,x))\). The remaining terms are bounded in absolute value by \(c\|\omega\|\,\|x\|\prod_i\|a_i\|\sum_{j>L}\mu_{s_j}\), for \(\Phi_\lambda\) and for \(\Phi\). Letting \(L\to\infty\) proves the convergence. \(\square\)

**Proposition 1.2 (the separable case).** Let \(M\) be of type \(\mathrm{II}_1\) with separable predual and faithful normal tracial state, and let \(f\in C_b^k(M,M)\) be a separately normal cocycle. There is \(g\in C_b^{k-1}(M,M)\) with \(dg=f\) and \(\|g\|\le\|f\|\).

**Proof.** Let \(\mu\) be the measure of Theorem 3.1 of the lesson on the random walk, and \(P=P_\mu\). Let \(U_1,U_2,\ldots\) be independent with law \(\mu\), \(W_0=1\) and \(W_j=U_1\cdots U_j\); expectations are norm-convergent countable sums. By induction on \(j\),
\[
(P^jf)(\mathbf a,x)=\mathbb E\bigl[f(\mathbf a,xW_j)\,W_j^*\bigr]:
\]
applying \(P\) to the right side multiplies \(W_j\) on the left by an independent increment of law \(\mu\), and the product has the law of \(W_{j+1}\). Put
\[
F_n=\frac1n\sum_{j=0}^{n-1}P^jf,\qquad\|F_n\|\le\|f\|.
\]
By Lemma 1.1(1), a subnet \((F_{n_\lambda})\) converges pointwise ultraweakly to some \(F\in C_b^k(M,M)\) with \(\|F\|\le\|f\|\). Since
\[
\begin{gathered}
PF_n-F_n=\frac{P^nf-f}n ,\\
\|PF_n-F_n\|\le\frac{2\|f\|}n ,
\end{gathered}
\]
and \(n_\lambda\to\infty\), Lemma 1.1(2) gives \(PF=F\).

*Each \(F(\mathbf a,\cdot)\) is a left multiplication.* Fix \(\mathbf a\), and put \(T(x)=F(\mathbf a,x)\). The identity \(PF=F\) says that \(T\) is \(\mu\)-harmonic. The map \(B(x)=f(\mathbf a,x)\) is normal, so by Lemmas 2.3 and 2.2(1) of the lesson on the cohomology problem, for \(R<\infty\) and \(\varepsilon>0\) there is \(\delta>0\) with \(\|B(y)\|_2<\varepsilon\) whenever \(\|y\|\le R\) and \(\|y\|_2<\delta\). Let \(\|x\|\le R\) and \(\|x\|_2<\delta\). For every unitary \(v\), \(xv\) satisfies the same bounds, so \(\|B(xv)v^*\|_2=\|B(xv)\|_2<\varepsilon\). Averaging gives \(\|(P^jf)(\mathbf a,x)\|_2\le\varepsilon\) and \(\|F_n(\mathbf a,x)\|_2\le\varepsilon\). The \(2\)-norm is ultraweakly lower semicontinuous (proof of Lemma 2.3 there), so \(\|T(x)\|_2\le\varepsilon\). Thus \(T\) is continuous on balls for the \(2\)-norm, and the Liouville theorem gives
\[
F(\mathbf a,x)=h(\mathbf a)\,x,\qquad h(\mathbf a)=F(\mathbf a,1).
\]
So \(h\in C_b^{k-1}(M,M)\) and \(\|h\|\le\|f\|\).

*The coboundary.* Put \(h_n(\mathbf a)=F_n(\mathbf a,1)\). Evaluate \(df=0\) at \((a_1,\ldots,a_k,v)\) for a unitary \(v\), multiply on the right by \(v^*\), and average over \(v=W_j\) and over \(0\le j<n\). As \(f(a_1,\ldots,a_k)vv^*=f(a_1,\ldots,a_k)\), this gives
\[
\begin{aligned}
0={}&a_1h_n(a_2,\ldots,a_k)\\
&+\sum_{j=1}^{k-1}(-1)^jh_n(a_1,\ldots,a_ja_{j+1},\\
&\qquad\ldots,a_k)\\
&+(-1)^kF_n(a_1,\ldots,a_k)\\
&+(-1)^{k+1}f(a_1,\ldots,a_k).
\end{aligned}
\]
Along the subnet each term converges ultraweakly; left multiplication by \(a_1\) is ultraweakly continuous. In the limit \(F(a_1,\ldots,a_k)=h(a_1,\ldots,a_{k-1})a_k\), so
\[
\begin{aligned}
0={}&(dh)(a_1,\ldots,a_k)\\
&+(-1)^{k+1}f(a_1,\ldots,a_k).
\end{aligned}
\]
Hence \(g=(-1)^kh\) satisfies \(dg=f\) and \(\|g\|\le\|f\|\). \(\square\)

The proof averages the cocycle identity at fixed inputs; it uses neither a commutation relation between \(P\) and \(d\) nor normality of \(F\).

## 2. Removing separability

**Lemma 2.1.** Let \((M,\tau)\) be a tracial von Neumann algebra and \(N\subseteq M\) a von Neumann subalgebra with \(1\in N\) generated by a countable set. Then \(N\) has separable predual.

**Proof.** We may take the generating set \(S\) closed under adjoints. Let \(A_0\) be the countable set of polynomials in \(S\) with coefficients in \(\mathbb Q+i\mathbb Q\), and \(A\) its norm closure, the C\*-algebra generated by \(S\). By the double commutant theorem the strong closure of \(A\) is \(N\). By Kaplansky's density theorem every element of the unit ball of \(N\) is the strong limit of a net in the unit ball of \(A\), hence its \(2\)-norm limit (Exercise 4.4 of the lesson on the cohomology problem). So \(A_0\) is \(2\)-norm dense in \(N\), and \(L^2(N)\) is separable.

The map \(\lambda:N\to B(L^2(N))\) of Lemma 2.3(2) of the lesson on the random walk is an injective unital \(*\)-homomorphism onto a von Neumann algebra, with \(\lambda\) and \(\lambda^{-1}\) normal; that part of its proof does not use a separable predual. The predual of \(\lambda(N)\) is a quotient of \(B(L^2(N))_*\) (Theorem 9.4(a) of the lesson on operator topologies). The latter is separable: by Theorem 9.1(ii) there every normal functional is \(x\mapsto\sum_n\langle x\xi_n,\eta_n\rangle\) with square-summable sequences, so it is a norm limit of finite sums, and \(\|\langle\cdot\,\xi,\eta\rangle-\langle\cdot\,\xi',\eta'\rangle\|\)\(\le\|\xi-\xi'\|\,\|\eta\|+\|\xi'\|\,\|\eta-\eta'\|\) lets one take \(\xi,\eta\) from a countable dense set. Finally \(\omega\mapsto\omega\circ\lambda\) is an isometry of \(\lambda(N)_*\) onto \(N_*\). \(\square\)

**Lemma 2.2.** Let \(N\) be a von Neumann algebra with separable predual and a faithful normal tracial state. Suppose that for every \(m\ge2\), \(N\) contains matrix units \(e^{(m)}_{ij}\), \(1\le i,j\le m\), with \(\sum_ie^{(m)}_{ii}=1\). Then \(N\) is of type \(\mathrm{II}_1\).

**Proof.** Let \(N\) act on \(L^2(N)\) (Lemma 2.3 of the lesson on the random walk) and write \(N=\int^\oplus N(\gamma)\,d\mu(\gamma)\) with factors \(N(\gamma)\) (Theorem 4.1 of the lesson on the central decomposition). By Corollary 3.6 there, there are normal positive tracial functionals \(\varphi_\gamma\) on \(N(\gamma)\), faithful for almost every \(\gamma\). The fibre map is almost everywhere a unital \(*\)-homomorphism on the countably many matrix units.

Fix \(\gamma\) outside a null set, with \(N(\gamma)\ne0\). Then \(\varphi_\gamma\) is faithful, so \(\varphi_\gamma(1)>0\), and \(N(\gamma)\) contains the matrix units \(e^{(m)}_{ij}(\gamma)\). The projections \(e^{(m)}_{ii}(\gamma)\) are equivalent through the \(e^{(m)}_{i1}(\gamma)\), so each has \(\varphi_\gamma\)-value \(\varphi_\gamma(1)/m\). Suppose \(p\in N(\gamma)\) is a nonzero abelian projection. In the factor \(N(\gamma)\) its only subprojections are \(0\) and \(p\) (Fact 1.6(a) there), and comparison (Fact 1.6(b)) gives \(p\precsim e^{(m)}_{11}(\gamma)\) or \(e^{(m)}_{11}(\gamma)\precsim p\); in the second case \(e^{(m)}_{11}(\gamma)\) is equivalent to a nonzero subprojection of \(p\), that is to \(p\). Either way \(\varphi_\gamma(p)\le\varphi_\gamma(1)/m\), for every \(m\). Hence \(\varphi_\gamma(p)=0\), contradicting faithfulness. So \(N(\gamma)\) is not of type I; it is finite because it has a faithful tracial functional. By Theorem 5.3 there, almost every \(\gamma\) with \(N(\gamma)\ne0\) lies in the set \(E_{\mathrm{II}_1}\) of the type decomposition. Hence the central projections \(z_{\mathrm I},z_{\mathrm{II}_\infty},z_{\mathrm{III}}\) of \(N\) vanish (Fact 1.1(f)), and \(N\) is of type \(\mathrm{II}_1\). \(\square\)

**Proposition 2.3 (the tracial case).** Let \(M\) be of type \(\mathrm{II}_1\) with a faithful normal tracial state \(\tau\), and let \(f\in C_b^k(M,M)\) be a separately normal cocycle. There is \(g\in C_b^{k-1}(M,M)\) with \(dg=f\) and \(\|g\|\le\|f\|\).

**Proof.** For each \(m\ge2\), Fact 1.7(b) of the lesson on the central decomposition gives \(1=e_1+\cdots+e_m\) with mutually orthogonal, mutually equivalent projections. With partial isometries \(v_i\), \(v_i^*v_i=e_1\), \(v_iv_i^*=e_i\), the elements \(e^{(m)}_{ij}=v_iv_j^*\) are matrix units with \(\sum_ie^{(m)}_{ii}=1\).

Order the finite subsets \(E\subseteq M\) by inclusion. For each \(E\), let \(N_E\) be the von Neumann subalgebra generated by \(E\), the finite set \(f(E^k)\) and all the \(e^{(m)}_{ij}\). It is generated by a countable set, so it has separable predual (Lemma 2.1); the restriction of \(\tau\) is a faithful normal tracial state; and \(N_E\) is of type \(\mathrm{II}_1\) by Lemma 2.2. Let \(\mathcal E_E:M\to N_E\) be the trace-preserving conditional expectation of Theorem 9.1 of the integration lesson: a normal projection of norm one onto \(N_E\) with \(\mathcal E_E(axb)=a\,\mathcal E_E(x)\,b\) for \(a,b\in N_E\).

The map \(f_E=\mathcal E_E\circ f|_{N_E^k}\) is separately normal, \(\|f_E\|\le\|f\|\), and \(df_E=\mathcal E_E\circ(df)=0\) on \(N_E\), by bimodularity. By Proposition 1.2 there is \(g_E\in C_b^{k-1}(N_E,N_E)\) with \(dg_E=f_E\) and \(\|g_E\|\le\|f\|\). Put
\[
\begin{aligned}
&G_E(x_1,\ldots,x_{k-1})\\
&\quad=g_E(\mathcal E_Ex_1,\ldots,\mathcal E_Ex_{k-1}),
\end{aligned}
\]
an element of \(C_b^{k-1}(M,M)\) with \(\|G_E\|\le\|f\|\). If \(a_1,\ldots,a_k\in E\), all inputs and products of neighbours in \((dG_E)(a_1,\ldots,a_k)\) lie in \(N_E\), where \(\mathcal E_E\) is the identity, so
\[
\begin{aligned}
(dG_E)(a_1,\ldots,a_k)&=(dg_E)(a_1,\ldots,a_k)\\
&=\mathcal E_Ef(a_1,\ldots,a_k)\\
&=f(a_1,\ldots,a_k),
\end{aligned}
\]
the last because \(f(E^k)\subseteq N_E\).

By Lemma 1.1(1) a subnet of \((G_E)\) converges pointwise ultraweakly to some \(g\in C_b^{k-1}(M,M)\) with \(\|g\|\le\|f\|\). Fix \(a_1,\ldots,a_k\in M\). Along the subnet the index \(E\) eventually contains \(\{a_1,\ldots,a_k\}\), so \((dG_E)(a_1,\ldots,a_k)=f(a_1,\ldots,a_k)\) eventually. The left side converges ultraweakly to \((dg)(a_1,\ldots,a_k)\), being a finite sum in which fixed elements multiply on the left or right. So \(dg=f\). \(\square\)

## 3. Central cuts

Let \(z\in M\) be a central projection and \(q=1-z\). The ideal \(zM\) is an \(M\)-bimodule under multiplication, and \(q\) acts on it as \(0\) from both sides. Let \(C_b^n(M,zM)\) be the bounded \(n\)-linear maps \(M^n\to zM\), with \(C_b^0(M,zM)=zM\) and the differential \(d\) of the lesson on the cohomology problem; \(d\circ d=0\) by the same proof. Define \(\operatorname{cut}_z\) by
\[
(\operatorname{cut}_z\psi)(a_1,\ldots,a_n)=\psi(za_1,\ldots,za_n),
\]
with \(\operatorname{cut}_z=\mathrm{id}\) on \(C_b^0(M,zM)\). For \(n\ge2\) define \(J_z:C_b^n(M,zM)\to C_b^{n-1}(M,zM)\) by
\[
\begin{aligned}
&(J_z\psi)(a_1,\ldots,a_{n-1})\\
&=\sum_{i=1}^{n-1}(-1)^i\psi(za_1,\ldots,za_{i-1},q,\\
&\qquad qa_i,a_{i+1},\ldots,a_{n-1}),
\end{aligned}
\]
and \(J_z=0\) on \(C_b^0\) and \(C_b^1\).

**Lemma 3.1 (central homotopy).** On \(C_b^n(M,zM)\), for every \(n\ge0\),
\[
dJ_z+J_zd=\mathrm{id}-\operatorname{cut}_z ,
\]
and \(\|J_z\psi\|\le(n-1)\|\psi\|\) for \(n\ge2\). In particular, for a cocycle \(\psi\in C_b^n(M,zM)\) with \(n\ge2\), \(d(J_z\psi)=\psi-\operatorname{cut}_z\psi\).

**Proof.** The bound holds term by term, as \(\|za\|\le\|a\|\) and \(\|q\|\le1\). In degree \(0\) both sides vanish. In degree \(1\), \(J_z\psi=0\) and
\[
\begin{aligned}
(J_zd\psi)(a)&=-(d\psi)(q,qa)\\
&=-q\psi(qa)+\psi(qa)-\psi(q)qa\\
&=\psi(qa),
\end{aligned}
\]
because \(q\) annihilates \(zM\); and \(\psi(qa)=\psi(a)-\psi(za)\).

Let \(n\ge2\). Both sides are \(n\)-linear in \((a_1,\ldots,a_n)\), so it suffices to take each \(a_j\) nonzero and in \(zM\) or in \(qM\); call such tuples *pure*. Products of elements of \(zM\) and \(qM\) are in \(zM\), in \(qM\) or \(0\). Let \(b\) be a pure tuple and \(\varphi\) a cochain of degree at least \(2\). If all entries of \(b\) lie in \(zM\), then \((J_z\varphi)(b)=0\), since \(qb_i=0\). Otherwise, if \(b_r\) is the first entry in \(qM\), only the term \(i=r\) survives — \(qb_i=0\) for \(i<r\) and \(zb_r=0\) for \(i>r\) — and
\[
\begin{aligned}
&(J_z\varphi)(b)=(-1)^r\varphi(b_1,\ldots,b_{r-1},\\
&\qquad q,b_r,\ldots).\qquad(3.1)
\end{aligned}
\]

Let \(a\) be a pure \(n\)-tuple. If all entries lie in \(zM\), so do all tuples obtained by multiplying neighbours, and both sides vanish. Otherwise let \(a_r\) be the first entry in \(qM\). Then \((\operatorname{cut}_z\psi)(a)=0\), as \(za_r=0\), and by (3.1) \((J_zd\psi)(a)=(-1)^r(d\psi)(c)\) with
\[
c=(a_1,\ldots,a_{r-1},q,a_r,\ldots,a_n).
\]
Compare the terms of \((-1)^r(d\psi)(c)\) with those of \((dJ_z\psi)(a)\), evaluating the latter by (3.1).

1. Multiplying \(q\) and \(a_r\) gives \((-1)^r(-1)^r\psi(a)=\psi(a)\).
2. Multiplying \(a_{r-1}\) and \(q\) gives \(0\); so does multiplying \(a_{r-1}\) and \(a_r\) in \(dJ_z\psi\), as \(zMqM=0\).
3. Left outer terms: for \(r=1\) both vanish, as \(q\) and \(a_1\in qM\) annihilate \(zM\). For \(r\ge2\) they are \((-1)^ra_1\psi(a_2,\ldots,a_{r-1},\)\(q,a_r,\ldots,a_n)\) and \(a_1(J_z\psi)(a_2,\ldots,a_n)\), where the first \(qM\)-entry sits at position \(r-1\); they cancel.
4. Products \(a_ja_{j+1}\) with \(j\le r-2\): both have index \(j\), and the first \(qM\)-entry of the shortened tuple sits at position \(r-1\) in \(dJ_z\psi\). The signs \((-1)^{r+j}\) and \((-1)^{j+r-1}\) cancel.
5. Products \(a_ja_{j+1}\) with \(j\ge r\): index \(j+1\) in \(d\psi(c)\) and \(j\) in \(dJ_z\psi\). If the product is \(0\), both vanish. Otherwise the first \(qM\)-entry stays at position \(r\), and the signs \((-1)^{r+j+1}\) and \((-1)^{j+r}\) cancel.
6. Right outer terms: for \(r=n\) both vanish, since \(a_n\in qM\) annihilates \(zM\) and \((a_1,\ldots,a_{n-1})\) lies in \(zM\). For \(r<n\) they are \((-1)^{r+n+1}\psi(a_1,\ldots,a_{r-1},\)\(q,a_r,\ldots,a_{n-1})a_n\) and \((-1)^{n+r}\) times the same; they cancel.

This accounts for all \(n+2\) terms of \((d\psi)(c)\) and all \(n+1\) terms of \((dJ_z\psi)(a)\). The sum is \(\psi(a)=(\psi-\operatorname{cut}_z\psi)(a)\). \(\square\)

## 4. The proof of the main theorem

**Lemma 4.1 (tracial pieces).** Let \(M\ne0\) be of type \(\mathrm{II}_1\). There are mutually orthogonal nonzero central projections \(z_i\), \(i\in I\), with \(\sum_iz_i=1\), such that every \(z_iM\) is of type \(\mathrm{II}_1\) and has a faithful normal tracial state.

**Proof.** Let \(Z\) be the centre. By Zorn's lemma there is a maximal family \((z_i)\) of mutually orthogonal nonzero projections of \(Z\), each the support of a normal state of \(Z\) (Lemma 11.1 of the lesson on W\*-algebras). If \(w=1-\sum_iz_i\ne0\), a vector state \(\varphi\) of \(Z\) with \(\varphi(w)>0\) gives the normal state \(\varphi(w\,\cdot\,)/\varphi(w)\), whose support is a nonzero projection below \(w\), contradicting maximality. So \(\sum_iz_i=1\). The centre \(z_iZ\) of \(z_iM\) carries the faithful normal state given by \(z_i\), and \(z_iM\) is finite. By Fact 1.7(a) of the lesson on the central decomposition, \(z_iM\) has a faithful normal tracial state; it is of type \(\mathrm{II}_1\) as a central summand of \(M\). \(\square\)

**Lemma 4.2 (central partitions).** Let \(z_i\), \(i\in I\), be mutually orthogonal central projections of \(M\) with \(\sum_iz_i=1\). For every family \((y_i)\) with \(y_i\in z_iM\) and \(\sup_i\|y_i\|<\infty\), there is exactly one \(y\in M\) with \(z_iy=y_i\) for all \(i\); moreover \(\|y\|=\sup_i\|y_i\|\).

**Proof.** If \(z_iy=0\) for all \(i\), then \(y=\sum_iz_iy=0\), the sum converging strongly (Corollary 1.4 of the Kaplansky lesson). For existence, the finite partial sums \(y_F=\sum_{i\in F}y_i\) form a net with
\[
\begin{aligned}
&\|(y_F-y_{F'})\xi\|^2\\
&=\sum_{i\in F\triangle F'}\|y_iz_i\xi\|^2\\
&\le\sup_i\|y_i\|^2\sum_{i\in F\triangle F'}\|z_i\xi\|^2 ,
\end{aligned}
\]
which is small for large \(F,F'\), since \(\sum_i\|z_i\xi\|^2=\|\xi\|^2\). The strong limit \(y\) lies in \(M\), satisfies \(z_iy=y_i\), and \(\|y\xi\|^2=\sum_i\|y_iz_i\xi\|^2\le\sup_i\|y_i\|^2\|\xi\|^2\); also \(\|y\|\ge\|z_iy\|=\|y_i\|\). \(\square\)

**Proof of Theorem 1.2 of the lesson on the cohomology problem.** Let \(M\ne0\), \(k\ge2\), and let \(\phi\in C_b^k(M,M)\) be a cocycle. By K1 there are a separately normal cocycle \(f\) and \(b\in C_b^{k-1}(M,M)\) with \(\phi=f+db\).

Let \(z_{\mathrm{II}_1}\) be the central projection of the type \(\mathrm{II}_1\) summand (Theorem 7.2 of the lesson on projections and types) and \(z_0=1-z_{\mathrm{II}_1}\). If \(z_{\mathrm{II}_1}\ne0\), Lemma 4.1 applied to \(z_{\mathrm{II}_1}M\) gives central projections \(z_i\), \(i\in I\), of \(z_{\mathrm{II}_1}M\), hence of \(M\), with sum \(z_{\mathrm{II}_1}\). Let \(I'\) consist of \(I\) and, if \(z_0\ne0\), the index \(0\). For \(i\in I'\), the map \(\psi_i=z_if\) belongs to \(C_b^k(M,z_iM)\) and is a cocycle there, as multiplication by the central \(z_i\) commutes with \(d\). Its restriction \(f_i\) to \((z_iM)^k\) is a separately normal cocycle on the von Neumann algebra \(z_iM\), with \(\|f_i\|\le\|f\|\).

For \(i\in I\), Proposition 2.3 gives \(b_i\in C_b^{k-1}(z_iM,z_iM)\) with \(db_i=f_i\) and \(\|b_i\|\le\|f\|\). If \(z_0\ne0\), the algebra \(z_0M\) has no type \(\mathrm{II}_1\) central summand, and K2 gives \(b_0\in C_b^{k-1}(z_0M,z_0M)\) with \(db_0=f_0\). Put
\[
\tilde b_i(x_1,\ldots,x_{k-1})=b_i(z_ix_1,\ldots,z_ix_{k-1}).
\]
Since \(b_i\) takes values in \(z_iM\), \(x\,b_i(\ldots)=(z_ix)\,b_i(\ldots)\) and \(b_i(\ldots)\,x=b_i(\ldots)\,(z_ix)\); also \(z_i(x_jx_{j+1})=(z_ix_j)(z_ix_{j+1})\). Hence \(d\tilde b_i=\operatorname{cut}_{z_i}\psi_i\). Let
\[
H_i=\tilde b_i+J_{z_i}\psi_i\in C_b^{k-1}(M,z_iM).
\]
By Lemma 3.1, \(dH_i=\operatorname{cut}_{z_i}\psi_i+\psi_i-\operatorname{cut}_{z_i}\psi_i=z_if\). Moreover \(\|H_i\|\le k\|f\|\) for \(i\in I\), and \(\|H_0\|\le\|b_0\|+(k-1)\|f\|\). Let \(C\) be the larger of these two bounds.

For \(\mathbf x\in M^{k-1}\), let \(G(\mathbf x)\in M\) be the element with \(z_iG(\mathbf x)=H_i(\mathbf x)\) for all \(i\in I'\) (Lemma 4.2). By uniqueness, \(G\) is \((k-1)\)-linear, and \(\|G\|\le C\). As each \(z_i\) is central, \(z_i(dG)(\mathbf y)=(dH_i)(\mathbf y)=z_if(\mathbf y)\) for every \(\mathbf y\in M^k\), so \(dG=f\) by uniqueness in Lemma 4.2. Finally
\[
d(G+b)=f+db=\phi .
\]
So every bounded cocycle of degree \(k\ge2\) is the coboundary of a bounded cochain, and \(H_b^k(M,M)=0\). \(\square\)

The proof uses the classical theorems K1 and K2 without proof; all other steps are proved in this course or in the lessons it cites.

## 5. Exercises

**5.1** (easy). Show directly from the definition that \(f_E=\mathcal E_E\circ f|_{N_E^k}\) is a cocycle on \(N_E\).

**5.2** (medium). Show that the proof of Proposition 1.2 also works for \(k=1\), and deduce: if \(M\) is of type \(\mathrm{II}_1\) with separable predual and faithful normal tracial state, every normal derivation \(\delta\) of \(M\) is inner, \(\delta(a)=ha-ah\) with \(\|h\|\le\|\delta\|\).

**5.3** (easy). Check Lemma 3.1 in degree \(2\) on the pure tuple \((a_1,a_2)\) with \(a_1\in qM\) and \(a_2\in zM\).

**5.4** (easy). Show that \(M_n(\mathbb C)\) does not contain matrix units \(e_{ij}\), \(1\le i,j\le m\), with \(\sum_ie_{ii}=1\) when \(m>n\). Which step of the proof of Lemma 2.2 does this reflect?

**5.5** (easy). Let \(p\ne0,1\) be a projection of \(M\). Show that the von Neumann algebra generated by \(p\) is \(\mathbb Cp+\mathbb C(1-p)\), which is of type I. Why does the proof of Proposition 2.3 put matrix units of every size into \(N_E\)?

## 6. Solutions

**5.1.** For \(a_1,\ldots,a_{k+1}\in N_E\), every term of \((df_E)(a_1,\ldots,a_{k+1})\) is \(\mathcal E_E\) applied to the corresponding term of \((df)(a_1,\ldots,a_{k+1})\), because \(\mathcal E_E(a_1y)=a_1\mathcal E_E(y)\) and \(\mathcal E_E(ya_{k+1})=\mathcal E_E(y)a_{k+1}\). So \((df_E)(a)=\mathcal E_E((df)(a))=0\).

**5.2.** For \(k=1\) there is no \(\mathbf a\): \(F\) is a limit of the averages \(F_n(x)=\frac1n\sum_{j<n}\mathbb E[\delta(xW_j)W_j^*]\), it is \(\mu\)-harmonic and continuous on balls, so \(F(x)=hx\) with \(h=F(1)\) and \(\|h\|\le\|\delta\|\). The identity \((d\delta)(a,v)=a\delta(v)-\delta(av)+\delta(a)v=0\), multiplied by \(v^*\) and averaged, gives \(ah_n-F_n(a)+\delta(a)=0\) with \(h_n=F_n(1)\). In the limit \(ah-ha+\delta(a)=0\), that is \(\delta(a)=ha-ah\).

**5.3.** Here \(r=1\) and \(c=(q,a_1,a_2)\). By (3.1),
\[
\begin{aligned}
&(J_zd\psi)(a_1,a_2)=-(d\psi)(q,a_1,a_2)\\
&=-q\psi(a_1,a_2)+\psi(qa_1,a_2)\\
&\quad-\psi(q,a_1a_2)+\psi(q,a_1)a_2.
\end{aligned}
\]
The first term vanishes, \(qa_1=a_1\), and \(a_1a_2=0\), so \((J_zd\psi)(a_1,a_2)=\psi(a_1,a_2)+\psi(q,a_1)a_2\). In \(dJ_z\psi\), \((J_z\psi)(a_2)=0\) as \(a_2\in zM\), \((J_z\psi)(a_1a_2)=0\), and \((J_z\psi)(a_1)=-\psi(q,a_1)\), so
\[
\begin{aligned}
&(dJ_z\psi)(a_1,a_2)\\
&=a_1(J_z\psi)(a_2)-(J_z\psi)(a_1a_2)\\
&\quad+(J_z\psi)(a_1)a_2=-\psi(q,a_1)a_2.
\end{aligned}
\]
The sum is \(\psi(a_1,a_2)\), and \((\operatorname{cut}_z\psi)(a_1,a_2)=\psi(za_1,za_2)=0\).

**5.4.** The \(e_{ii}\) would be \(m\) mutually orthogonal nonzero projections in \(M_n(\mathbb C)\), whose ranks add up to at most \(n\). In the proof of Lemma 2.2, a factor of type I with a faithful trace is excluded in the same way: its minimal projection would have trace at most \(1/m\) for every \(m\).

**5.5.** The set \(\mathbb Cp+\mathbb C(1-p)\) is a unital \(*\)-algebra, two-dimensional and hence closed, and every von Neumann algebra containing \(p\) contains it. It is abelian, so every projection in it is abelian, and it is of type I. A subalgebra generated by \(E\) and \(f(E^k)\) alone may therefore be of type I, where Proposition 1.2 does not apply; the matrix units force \(N_E\) to be of type \(\mathrm{II}_1\) (Lemma 2.2).

## Sources

- [OpenAI-295] OpenAI, *Vanishing of higher bounded Hochschild cohomology*, OpenAI Math Release preprint, 23 September 2026, Section 5 (bounded primitives, removal of separability, central cuts, completion of the proof). https://github.com/openai/math/tree/main/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026
- E. Christensen, F. Pop, A. M. Sinclair and R. R. Smith, [*Hochschild cohomology of factors with property \(\Gamma\)*](https://arxiv.org/abs/math/0107078), Ann. of Math. 158 (2003), 635–659, Section 7: uniform primitive bounds and pointwise ultraweak compactness, used there to remove separability.
