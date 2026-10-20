# Descent to a Verlinde category

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lesson 7 produced an exact symmetric tensor functor \(\Phi\colon\mathcal C\to\mathcal C\boxtimes\mathcal W\), with \(\mathcal W=\operatorname{Ver}_q(k)\) and \(q=p^r\), which is semilinear for \(a\mapsto a^q\). Its target still contains \(\mathcal C\). This lesson removes that factor and proves the main theorem (Theorem 5.1 of Lesson 1). The idea goes back to Etingof and Ostrik, who iterated their ordinary Frobenius functor [EO, Section 10]. For a simple object \(S\) and a composition factor \(A\boxtimes B\) of \(\Phi(S)\), the Frobenius–Perron dimension of \(A\) is at most that of \(S\), and equality forces \(S\) into the subcategory \(\mathcal C_{\mathrm{ex}}\) on which the Frobenius functor of Etingof and Ostrik is exact (Lemma 3.1); the proof compares Frobenius–Perron dimensions with a congruence modulo \(p\) in the Grothendieck ring. Iterating \(\Phi\) at most as many times as there are simple objects therefore lands every first component in \(\mathcal C_{\mathrm{ex}}\), and the closure of \(\mathcal C_{\mathrm{ex}}\) under extensions admits a fibre functor to \(\operatorname{Ver}_p\), or to \(\operatorname{Ver}_4^+\) when \(p=2\).

**Prerequisites.** [*Finite symmetric tensor categories and fibre functors*](finite-symmetric-tensor-categories-and-fibre-functors.md), Sections 1 to 4; [*Higher Frobenius functors*](higher-frobenius-functors.md); [*Rank varieties and an exact higher Frobenius functor*](rank-varieties-and-an-exact-higher-frobenius-functor.md), Theorem 5.1.

## 1. The Frobenius functor of Etingof and Ostrik

Let \(\mathcal C\) be a finite symmetric tensor category. For an object \(Y\), let \(c\) be the cyclic permutation of the \(p\) factors of \(Y^{\otimes p}\) and \(D=1-c\), so that \(D^p=1-c^p=0\). For \(1\le i\le p-1\) put
\[
F_i(Y)=\frac{\ker D\cap\operatorname{im}D^{i-1}}{\ker D\cap\operatorname{im}D^i},
\]
a subquotient of \(Y^{\otimes p}\), hence an object of \(\mathcal C\). With \(L_1,\dots,L_{p-1}\) the simple objects of \(\operatorname{Ver}_p\) (Lesson 1, Section 4), the *Frobenius functor* is
\[
F(Y)=\bigoplus_{i=1}^{p-1}F_i(Y)\boxtimes L_i\in\mathcal C\boxtimes\operatorname{Ver}_p .
\]
It is additive, semilinear for \(a\mapsto a^p\), and symmetric monoidal, but in general not exact [EO, Sections 3 to 5, Proposition 5.1]. We write \(d=\operatorname{FPdim}\).

**Theorem 1.1** (named result N8 [EO]). Let \(\mathcal C\) be a finite symmetric tensor category.

1. \(d(F(Y))\le d(Y)\) for every object \(Y\) [EO, Proposition 6.3].
2. The full subcategory \(\mathcal C_{\mathrm{ex}}=\{Y:d(F(Y))=d(Y)\}\) is a tensor subcategory, that is, it contains \(\mathbf 1\) and is closed under tensor products, duals, finite direct sums and subquotients, and \(F\) is exact on it [EO, Proposition 7.4].
3. A finite symmetric tensor category on which \(F\) is exact admits a fibre functor to \(\operatorname{Ver}_p(k)\) [EO, Theorem 8.1].
4. If \(p>2\), then \(\mathcal C_{\mathrm{ex}}\) is closed under extensions in \(\mathcal C\) [EO, Corollary 9.5].

**Theorem 1.2** (named result N9 [EG, Theorem 2.21(2)]; see [EO, Theorem 9.6 and Corollary 9.8]). Let \(p=2\), let \(\mathcal D\) be a finite symmetric tensor category, and let \(\mathcal E\subset\mathcal D\) be a tensor subcategory containing every simple object of \(\mathcal D\). If \(\mathcal E\) admits a fibre functor to \(\operatorname{Vec}_k\), then \(\mathcal D\) admits a fibre functor to the category \(\mathcal C_1\) of Theorem 4.2(5) of Lesson 1.

## 2. A congruence in the Grothendieck ring

**Lemma 2.1.** In the commutative ring \(K_0(\mathcal C)/pK_0(\mathcal C)\),
\[
[Y]^p=\sum_{i=1}^{p-1}i\,[F_i(Y)].
\]
Consequently, for every \(r\ge1\),
\[
\begin{array}{r}
\begin{aligned}
&[Y]^{p^r}=\sum_{i_1,\dots,i_r=1}^{p-1}(i_1\cdots i_r)\\
&\qquad\cdot[F_{i_r}\cdots F_{i_1}(Y)]\pmod p .
\end{aligned}\\
(2.1)
\end{array}
\]

*Proof.* Put \(Z=Y^{\otimes p}\) and \(K_j=\ker D\cap\operatorname{im}D^j\) for \(0\le j\le p\). The exact sequences
\[
\begin{gathered}
0\to K_j\to\operatorname{im}D^j\xrightarrow{\ D\ }\operatorname{im}D^{j+1}\to0\\
(0\le j<p)
\end{gathered}
\]
give \([\operatorname{im}D^j]=[K_j]+[\operatorname{im}D^{j+1}]\), and with \(\operatorname{im}D^0=Z\), \(\operatorname{im}D^p=0\), they give \([Z]=\sum_{j=0}^{p-1}[K_j]\). The chain \(K_0\supseteq K_1\supseteq\cdots\supseteq K_p=0\) has quotients \(K_{i-1}/K_i=F_i(Y)\) for \(1\le i\le p-1\) and \(K_{p-1}/K_p=K_{p-1}\). Since \(K_j\) is filtered by the quotients \(K_{i-1}/K_i\) with \(i>j\),
\[
\begin{aligned}
[Z]&=\sum_{j=0}^{p-1}\sum_{i=j+1}^{p}[K_{i-1}/K_i]\\
&=\sum_{i=1}^{p-1}i\,[F_i(Y)]+p\,[K_{p-1}].
\end{aligned}
\]
Reducing modulo \(p\) proves the first identity, since \([Y]^p=[Z]\). In a commutative ring of characteristic \(p\), \((x+y)^p=x^p+y^p\), and \(i^p\equiv i\) modulo \(p\). Raising the first identity to the \(p\)-th power and applying it to each object \(F_{i_1}(Y)\) gives (2.1) for \(r=2\), and induction gives the general case. Only classes of actual objects \(F_{i_s}\cdots F_{i_1}(Y)\) occur, so the nonexactness of \(F_i\) plays no role. \(\square\)

## 3. Equality of dimensions forces Frobenius exactness

Fix the exact functor \(\Phi\colon\mathcal C\to\mathcal C\boxtimes\mathcal W\) of Theorem 5.1 of Lesson 7 and the symmetric tensor functor \(\Theta\colon\operatorname{Rep}_k(E_r)\to\mathcal W\) used in its construction. By Lemma 3.2(3) of Lesson 1, \(d(\Phi(X))=d(X)\) for every \(X\). The simple objects of \(\mathcal C\boxtimes\mathcal W\) are the objects \(A\boxtimes B\) with \(A,B\) simple (Lemma 2.2 of Lesson 1), and \(d(A\boxtimes B)=d(A)d(B)\).

**Lemma 3.1** ([OpenAI-208, Lemma 7.2]). Let \(S\) be a simple object of \(\mathcal C\) and \(A\boxtimes B\) a composition factor of \(\Phi(S)\). Then \(d(A)\le d(S)\). If \(d(A)=d(S)\), then \(\Phi(S)\cong A\boxtimes B\), the object \(B\) is invertible, and \(S\in\mathcal C_{\mathrm{ex}}\); in particular \(A\) is then the only first component of a composition factor of \(\Phi(S)\).

*Proof.* Every nonzero object has \(d\ge1\), so \(d(S)=d(\Phi(S))\ge d(A)d(B)\ge d(A)\). If \(d(A)=d(S)\), then \(d(B)=1\) and \(A\boxtimes B\) is the only composition factor of \(\Phi(S)\), because the dimensions of the composition factors are positive and add up to \(d(S)\). By Lemma 3.2(4) of Lesson 1, \(B\) is invertible.

Let \(Q_A\) be a projective cover of \(A\). The functor \(\operatorname{Hom}(Q_A,-)\) is exact, has dimension one on \(A\) and zero on the other simple objects, so \(\dim_k\operatorname{Hom}(Q_A,X)=[X:A]\) for every \(X\). The evaluation formula of Theorem 5.1 of Lesson 7, applied to \(X=S\), gives
\[
\begin{aligned}
&\Theta\bigl(\operatorname{Hom}(Q_A,S^{\otimes q})\bigr)\\
&\quad\cong(\operatorname{Hom}(Q_A,-)\boxtimes\mathrm{Id})(A\boxtimes B)\\
&\quad=B .
\end{aligned}
\]
By Lemma 3.4 of Lesson 1, the categorical dimension of the left side is \(\dim_k\operatorname{Hom}(Q_A,S^{\otimes q})\) modulo \(p\), and that of the invertible object \(B\) is nonzero. Hence
\[
[S^{\otimes q}:A]\not\equiv0\pmod p .\tag{3.1}
\]
The coefficient of \([A]\) on the left of (2.1), with \(Y=S\), is \([S^{\otimes q}:A]\). By (3.1) the coefficient of \([A]\) on the right is nonzero modulo \(p\), so there are \(i_1,\dots,i_r\) such that \(A\) is a composition factor of \(Y_r\), where \(Y_0=S\) and \(Y_t=F_{i_t}(Y_{t-1})\). For every \(t\), Theorem 1.1(1) and \(d(L_{i_t})\ge1\) give
\[
\begin{aligned}
&d(Y_{t-1})\ge d(F(Y_{t-1}))\\
&\quad=\sum_id(F_i(Y_{t-1}))\,d(L_i)\ge d(Y_t).
\end{aligned}
\]
Since \(d(Y_r)\ge d(A)=d(S)=d(Y_0)\), all these inequalities are equalities. In particular \(d(F(S))=d(S)\), that is, \(S\in\mathcal C_{\mathrm{ex}}\). \(\square\)

The categorical dimension takes values in \(k\) and serves only to prove the congruence (3.1); \(d\) is always the real-valued Frobenius–Perron dimension.

## 4. The graph of simple objects

Let \(N\) be the number of isomorphism classes of simple objects of \(\mathcal C\). Form the directed graph \(\Gamma\) whose vertices are these classes, with an arrow \(S\to A\) whenever \(A\boxtimes B\) is a composition factor of \(\Phi(S)\) for some simple \(B\). Every vertex has at least one outgoing arrow, because \(\Phi(S)\ne0\).

**Lemma 4.1.** Every path \(S_0\to S_1\to\cdots\to S_N\) in \(\Gamma\) ends in \(\mathcal C_{\mathrm{ex}}\).

*Proof.* By Lemma 3.1, \(d\) does not increase along arrows. A path with \(N\) arrows visits \(N+1\) vertices, so some vertex repeats: \(S_i=S_j\) with \(i<j\). Along the cycle \(S_i\to\cdots\to S_j\) the dimension cannot decrease, so every arrow of the cycle preserves \(d\). By Lemma 3.1, every vertex of the cycle lies in \(\mathcal C_{\mathrm{ex}}\) and has exactly one outgoing arrow, namely the next vertex of the cycle. So the path after \(S_i\) is forced to follow the cycle, and \(S_N\) lies on it. \(\square\)

Before the cycle the dimension may stay constant along some arrows; what traps the path is the uniqueness of the outgoing arrow at each vertex of the cycle.

## 5. Iteration with scalar twists

Let \(\sigma\) be the automorphism \(a\mapsto a^q\) of \(k\), an automorphism because \(k\) is perfect. For a \(k\)-linear category \(\mathcal A\), let \(\mathcal A^{[\sigma]}\) be the same category with the scalar action \(a\cdot_{[\sigma]}f=\sigma^{-1}(a)f\). A \(\sigma\)-semilinear functor \(\mathcal A\to\mathcal B\) is the same as a \(k\)-linear functor \(\mathcal A^{[\sigma]}\to\mathcal B\), and the universal property of Deligne products gives \((\mathcal A\boxtimes\mathcal B)^{[\sigma]}\simeq\mathcal A^{[\sigma]}\boxtimes\mathcal B^{[\sigma]}\). So two \(\sigma\)-semilinear exact tensor functors have a Deligne product, again \(\sigma\)-semilinear, exact and tensor (Lemma 2.3(2) of Lesson 1, applied to the \(k\)-linear versions). A composite of a \(\sigma\)-semilinear and a \(\tau\)-semilinear functor is \(\tau\sigma\)-semilinear.

Let \(J_\sigma\) be a \(\sigma\)-semilinear exact symmetric tensor autoequivalence of \(\mathcal W\) (Theorem 4.2(4) of Lesson 1). It is a scalar transport, not a Frobenius functor. Put \(\Psi_1=\Phi\) and
\[
\begin{gathered}
\Psi_{j+1}=\bigl(\Phi\boxtimes J_\sigma^{\boxtimes j}\bigr)\circ\Psi_j\colon\\
\mathcal C\to\mathcal C\boxtimes\mathcal W^{\boxtimes(j+1)} .
\end{gathered}
\]
By induction, \(\Psi_j\) is an exact symmetric tensor functor, semilinear for \(\sigma^j\).

**Lemma 5.1.** For every object \(X\), every composition factor \(A\boxtimes B_1\boxtimes\cdots\boxtimes B_N\) of \(\Psi_N(X)\) has \(A\in\mathcal C_{\mathrm{ex}}\).

*Proof.* We show by induction on \(j\) that for simple \(S\) the first components of the composition factors of \(\Psi_j(S)\) are endpoints of paths of length \(j\) in \(\Gamma\) starting at \(S\). For \(j=1\) this is the definition of \(\Gamma\). The functor \(\Phi\boxtimes J_\sigma^{\boxtimes j}\) is exact, so it carries a composition series of \(\Psi_j(S)\) to a filtration of \(\Psi_{j+1}(S)\) whose quotients are
\[
\Phi(A)\boxtimes J_\sigma(B_1)\boxtimes\cdots\boxtimes J_\sigma(B_j).
\]
The objects \(J_\sigma(B_i)\) are simple, so the composition factors of this quotient have first components \(A'\) with an arrow \(A\to A'\). For \(j=N\), Lemma 4.1 places the first components in \(\mathcal C_{\mathrm{ex}}\). For general \(X\), use a composition series of \(X\) and exactness of \(\Psi_N\). \(\square\)

## 6. The closure under extensions

**Lemma 6.1.** Let \(A\) be a finite-dimensional algebra and \(\mathcal B\) a full subcategory of finite-dimensional \(A\)-modules, closed under finite direct sums, submodules and quotients. Let \(I\) be the intersection of the annihilators of the modules in \(\mathcal B\). Then \(\mathcal B\) is the category of finite-dimensional \(A/I\)-modules.

*Proof.* The annihilators form a family of ideals of the finite-dimensional algebra \(A\), so \(I\) is already the intersection of finitely many of them, and \(I=\operatorname{Ann}(M)\) for the direct sum \(M\in\mathcal B\) of the corresponding modules. Let \(A\) act on \(\operatorname{End}_k(M)\) by \(a\cdot u=\rho_M(a)\circ u\); as an \(A\)-module, \(\operatorname{End}_k(M)\cong M^{\oplus\dim M}\), which lies in \(\mathcal B\). The map \(a\mapsto\rho_M(a)\) embeds the regular module \(A/I\) into it, so \(A/I\in\mathcal B\). Every finite-dimensional \(A/I\)-module is a quotient of some \((A/I)^n\), hence in \(\mathcal B\); conversely every module in \(\mathcal B\) is annihilated by \(I\). \(\square\)

Applied to \(\mathcal C_{\mathrm{ex}}\), which is closed under finite direct sums and subquotients by Theorem 1.1(2), Lemma 6.1 shows that \(\mathcal C_{\mathrm{ex}}\) is a finite abelian category with enough projectives; with the inherited structure it is a finite symmetric tensor category.

Let \(\mathcal D\subset\mathcal C\) be the full subcategory of objects all of whose composition factors lie in \(\mathcal C_{\mathrm{ex}}\), the *Serre closure* of \(\mathcal C_{\mathrm{ex}}\). It is closed under subobjects, quotients and extensions. It is closed under tensor products, since \(X\otimes Y\) has a filtration with quotients \(S\otimes T\) for composition factors \(S\) of \(X\) and \(T\) of \(Y\), and these lie in \(\mathcal C_{\mathrm{ex}}\) together with their composition factors. It is closed under duals, since the composition factors of \(X^*\) are the duals of those of \(X\). So \(\mathcal D\) is a symmetric tensor category containing \(\mathcal C_{\mathrm{ex}}\) and all its simple objects lie in \(\mathcal C_{\mathrm{ex}}\).

**Lemma 6.2.** The category \(\mathcal D\) is finite, and \(\Psi_N\) takes values in the full subcategory \(\mathcal D\boxtimes\mathcal W^{\boxtimes N}\) of \(\mathcal C\boxtimes\mathcal W^{\boxtimes N}\).

*Proof.* Choose a basic finite-dimensional algebra \(H\) with \(\mathcal C\simeq H\text{-mod}\) (replace \(A\) of Lemma 1.3 of Lesson 1 by the endomorphism algebra of the sum of the projective covers of the simple objects, each taken once), and let \(e\) be the sum of the primitive idempotents corresponding to the simple objects outside \(\mathcal C_{\mathrm{ex}}\). The functor \(M\mapsto eM\cong\operatorname{Hom}(He,M)\) is exact and vanishes exactly on the simple objects of \(\mathcal C_{\mathrm{ex}}\). By exactness it vanishes on \(M\) exactly when all composition factors of \(M\) lie in \(\mathcal C_{\mathrm{ex}}\). So \(\mathcal D\) consists of the modules with \(eM=0\), that is, \(HeH\,M=0\), and \(\mathcal D\simeq(H/HeH)\text{-mod}\) is finite. If \(\mathcal W^{\boxtimes N}\simeq J\text{-mod}\), then \(\mathcal D\boxtimes\mathcal W^{\boxtimes N}\simeq((H/HeH)\otimes J)\text{-mod}\) is the full subcategory of \((H\otimes J)\)-modules annihilated by \(e\otimes1\). The same exactness argument shows that it consists of the objects whose composition factors have first components in \(\mathcal C_{\mathrm{ex}}\), and Lemma 5.1 places \(\Psi_N(X)\) there. \(\square\)

## 7. A fibre functor on the closure

**Proposition 7.1.** The category \(\mathcal D\) admits a fibre functor to \(\operatorname{Ver}_p(k)\) if \(p>2\), and to \(\operatorname{Ver}_4^+(k)\subset\operatorname{Ver}_4(k)\) if \(p=2\).

*Proof.* The finite symmetric tensor category \(\mathcal C_{\mathrm{ex}}\) admits a fibre functor to \(\operatorname{Ver}_p(k)\) by Theorem 1.1(2) and (3). If \(p>2\), then \(\mathcal C_{\mathrm{ex}}\) is closed under extensions by Theorem 1.1(4), so \(\mathcal D=\mathcal C_{\mathrm{ex}}\). If \(p=2\), then \(\operatorname{Ver}_2(k)=\operatorname{Vec}_k\), and \(\mathcal C_{\mathrm{ex}}\subset\mathcal D\) is a tensor subcategory containing every simple object of the finite category \(\mathcal D\). Theorem 1.2 gives a fibre functor from \(\mathcal D\) to \(\mathcal C_1\), which is equivalent to \(\operatorname{Ver}_4^+(k)\) by Theorem 4.2(5) of Lesson 1. \(\square\)

## 8. Proof of the main theorem

**Theorem 8.1** (Theorem 5.1 of Lesson 1). Every finite symmetric tensor category \(\mathcal C\) over \(k\) admits a fibre functor to \(\operatorname{Ver}_{p^n}(k)\) for some \(n\ge1\).

*Proof.* Let \(r\) and \(\Phi\) be as in Theorem 5.1 of Lesson 7, \(N\) the number of simple objects of \(\mathcal C\), and \(\Psi_N\colon\mathcal C\to\mathcal D\boxtimes\mathcal W^{\boxtimes N}\) as in Lemma 6.2. Put \(n=\max(2,r)\) and \(\mathcal Z=\operatorname{Ver}_{p^n}(k)\). Proposition 7.1 followed by inclusions of the tower (Theorem 4.2(3) of Lesson 1) gives an exact \(k\)-linear symmetric tensor functor \(E\colon\mathcal D\to\mathcal Z\); the inclusion of the tower gives \(I\colon\mathcal W=\operatorname{Ver}_{p^r}(k)\to\mathcal Z\). By Lemma 2.3(1) of Lesson 1 they combine to an exact \(k\)-linear symmetric tensor functor
\[
\begin{aligned}
&H\colon\mathcal D\boxtimes\mathcal W^{\boxtimes N}\to\mathcal Z,\\
&H(Y\boxtimes W_1\boxtimes\cdots\boxtimes W_N)\\
&\quad=E(Y)\otimes I(W_1)\otimes\cdots\otimes I(W_N).
\end{aligned}
\]
The composite \(H\circ\Psi_N\) is an exact symmetric tensor functor, semilinear for \(\sigma^N\). Let \(J'\) be a \(\sigma^{-N}\)-semilinear exact symmetric tensor autoequivalence of \(\mathcal Z\) (Theorem 4.2(4) of Lesson 1). Then
\[
\mathcal F=J'\circ H\circ\Psi_N\colon\mathcal C\to\operatorname{Ver}_{p^n}(k)
\]
is \(k\)-linear, exact and a symmetric tensor functor, and it is faithful by Lemma 1.5 of Lesson 1. So \(\mathcal F\) is a fibre functor. \(\square\)

The level \(n\) is \(\max(2,r)\), with \(r\) the least nonprojective rank of Lesson 6; the exponent \(2\) is needed only when \(p=2\), for the category \(\operatorname{Ver}_4^+\).

## 9. Exercises

**9.1.** Let \(\mathcal C=\operatorname{Vec}_k\) and \(Y=k^m\). Show that \(F_1(Y)\) has dimension \(m\) and \(F_i(Y)=0\) for \(i\ge2\), and check Lemma 2.1 directly.

**9.2.** In the proof of Lemma 2.1, check the identity \(\sum_{j=0}^{p-1}[K_j]=\sum_{i=1}^{p}i\,[K_{i-1}/K_i]\) for \(p=3\) by writing out both sides.

**9.3.** Let \(A=k[x]/(x^2)\) and let \(\mathcal B\) be the semisimple \(A\)-modules. Find the ideal \(I\) of Lemma 6.1 and check its conclusion.

**9.4.** Draw a directed graph on four vertices in which every vertex has an outgoing arrow, the dimension does not increase along arrows, and a path of three arrows reaches a cycle of length two after one arrow that preserves the dimension. Explain why Lemma 4.1 still applies.

## 10. Solutions

**9.1.** The basis vectors \(e_{a_1}\otimes\cdots\otimes e_{a_p}\) of \(Y^{\otimes p}\) are permuted by \(c\). The \(m\) constant tuples are fixed and span copies of the trivial representation \(J_1\) of \(\mathbb Z/p\); the remaining \((m^p-m)/p\) orbits have size \(p\) and span copies of the regular representation \(J_p\). On \(J_1\), \(D=0\), so \(B_1=k\) and \(B_i=0\) for \(i\ge2\). On \(J_p\), \(D\) is a single nilpotent Jordan block of size \(p\), so \(\ker D=\operatorname{im}D^{p-1}\) and \(\ker D\cap\operatorname{im}D^j=\ker D\) for \(j\le p-1\); all \(B_i\) vanish for \(i\le p-1\). So \(F_1(Y)\) has dimension \(m\) and the other \(F_i(Y)\) vanish. Lemma 2.1 says \(m^p\equiv m\pmod p\), Fermat's little theorem.

**9.2.** For \(p=3\): the left side is \([K_0]+[K_1]+[K_2]\). Filtering, \([K_0]=[K_0/K_1]+[K_1/K_2]+[K_2/K_3]\), \([K_1]=[K_1/K_2]+[K_2/K_3]\), \([K_2]=[K_2/K_3]\), with \(K_3=0\). The sum is \(1\cdot[K_0/K_1]+2[K_1/K_2]+3[K_2/K_3]\), the right side.

**9.3.** The semisimple \(A\)-modules are the direct sums of the trivial module \(k=A/(x)\), whose annihilator is \((x)\). So \(I=(x)\), \(A/I=k\), and the finite-dimensional \(A/I\)-modules are the vector spaces on which \(x\) acts by zero, which are exactly the semisimple \(A\)-modules.

**9.4.** Take vertices \(S_0,S_1,S_2,S_3\) with \(d(S_0)=3\) and \(d(S_1)=d(S_2)=d(S_3)=2\), and arrows \(S_0\to S_1\), \(S_1\to S_2\), \(S_2\to S_3\), \(S_3\to S_2\). The path \(S_0\to S_1\to S_2\to S_3\) has three arrows; the arrow \(S_1\to S_2\) preserves the dimension without lying on a cycle. Lemma 4.1 only uses that a path with as many arrows as vertices repeats a vertex and that a cycle cannot be left. In a graph coming from \(\Phi\), Lemma 3.1 would place \(S_2\) and \(S_3\) in \(\mathcal C_{\mathrm{ex}}\) and give each of them exactly one outgoing arrow.

## Sources

- [OpenAI-208] OpenAI, *Fiber functors for finite symmetric tensor categories in positive characteristic*, OpenAI Math Release preprint, 24 September 2026, Section 7 (Lemmas 7.1 and 7.2, the finite graph, scalar twists, the Serre closure and the completion of the fiber functor). https://github.com/openai/math/tree/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026
- [EO] P. Etingof and V. Ostrik, *On the Frobenius functor for symmetric tensor categories in positive characteristic*, J. reine angew. Math. 773 (2021), numbering of arXiv:1912.12947v2: Sections 3 to 5, Propositions 5.1, 6.3 and 7.4, Theorem 8.1, Definition 8.13, Corollary 9.5, Theorem 9.6, Corollary 9.8, Section 10. https://arxiv.org/abs/1912.12947v2
- [EG] P. Etingof and S. Gelaki, *Finite symmetric tensor categories with the Chevalley property in characteristic 2*, J. Algebra Appl. 20 (2021), numbering of arXiv:1904.07576v2: Theorem 2.21(2). https://arxiv.org/abs/1904.07576v2
- [BEO] D. Benson, P. Etingof and V. Ostrik, *New incompressible symmetric tensor categories in positive characteristic*, numbering of arXiv:2003.10499v4: Theorems 4.5(iii) and 4.34, Section 4.9. https://arxiv.org/abs/2003.10499v4
