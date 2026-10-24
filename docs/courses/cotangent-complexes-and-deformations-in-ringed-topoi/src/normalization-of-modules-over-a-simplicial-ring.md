# Normalization of modules over a simplicial ring

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

Let \(R\) be a simplicial ring of a topos. Normalization carries simplicial \(R\)-modules to differential graded modules over \(A=NR\), and quasi-isomorphisms to quasi-isomorphisms. This lesson proves the following.

- The induced functor \(D_\bullet(R)\to D(A)\) is fully faithful.
- Its essential image consists of the objects whose cohomology vanishes in positive degrees.
- This holds for every topos, with or without enough points, and for associative rings that need not be commutative.

The proof has three steps:

1. Construct the left adjoint \(L\) of normalization on module categories, with explicit unit and counit. On a free module the unit is the shuffle map, so the Eilenberg–Zilber theorem makes it a quasi-isomorphism.
2. Resolve every connective differential graded module by successive attachments of free modules. The functor \(L\) is exact on these attachments.
3. Pass to the derived categories.

All constructions take place in the sheaf categories themselves.

**Prerequisites.**
- [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md): Conventions, Proposition 2.1 and its proof.
- [*Differential graded modules in a topos*](differential-graded-modules-in-a-topos.md): Conventions, Lemma 1.1, Propositions 1.2 and 1.3.
- From the programme lesson [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution): Theorems 1.1–1.3 (normalization, Dold–Kan, the shuffle map and Eilenberg–Zilber, with natural homotopies passing to sheaves).
- From the AI-integrated Stacks project: Dold–Kan in abelian categories and its splitting [[Stacks, Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan)]; maps out of bounded above complexes of projectives [[Tag 064B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-from-projective-complex)].

## Conventions

\(T\) is the topos of sheaves on a small site. \(R\) is a simplicial ring of \(T\), associative and unital. An \(R\)-module is a simplicial left \(R\)-module. These modules form an abelian category \(R\text{-}\operatorname{Mod}\) in which filtered colimits are formed degreewise and are exact, as in the Conventions of the lesson on simplicial rings. A map is a *quasi-isomorphism* if it induces isomorphisms on the sheaves \(\pi_n=H_n(N-)\). \(D_\bullet(R)\) is the localization of \(R\text{-}\operatorname{Mod}\) at the quasi-isomorphisms.

Complexes are graded cohomologically. \(N_nX=\bigcap_{i=1}^n\ker d_i\) is placed in degree \(-n\), with differential \(d_0\). Tensor products of complexes of abelian sheaves are taken over \(\mathbb Z\), with \(d(x\otimes y)=dx\otimes y+(-1)^{|x|}x\otimes dy\). \(\operatorname{Ch}^{\leq0}(T)\) is the category of complexes of abelian sheaves vanishing in positive degrees.

For a differential graded ring \(A\), a left module \(M\) satisfies \(d(am)=(da)m+(-1)^{|a|}a\,dm\). Left modules are right modules over the opposite ring, as in the lesson on differential graded modules. \(C(A)\), \(C^{\leq0}(A)\), \(D(A)\) and \(D^{\leq0}(A)\) are as there, formed with left modules; the opposite ring is in nonpositive degrees when \(A\) is.

For a complex \(V\) of abelian sheaves, \(A\otimes V\) is the *free* left module on \(V\). Restriction to \(1\otimes V\) is a bijection
\[
\operatorname{Hom}_A(A\otimes V,M)\cong\operatorname{Hom}(V,M)
\]
onto the chain maps. Its inverse sends \(\varphi\) to \(a\otimes v\mapsto a\varphi(v)\), a chain map by the Leibniz rule. For an object \(U\), \(\mathbb Z_U\) is the free abelian sheaf on \(U\); maps \(\mathbb Z_U\to F\) are the sections \(F(U)\).

**Dold–Kan.** Normalization is an equivalence from simplicial abelian sheaves to \(\operatorname{Ch}^{\leq0}(T)\) (Theorems 1.1, 1.2 of *The cotangent complex*; [Tag 019G]). Fix a quasi-inverse \(\Gamma\) and a natural isomorphism \(u_K\colon K\to N\Gamma K\). Since \(N\) is fully faithful,
\[
g\longmapsto N(g)\circ u_K \tag{0.1}
\]
is a bijection from maps \(\Gamma K\to X\) to chain maps \(K\to NX\), natural in \(K\) and \(X\).

The Dold–Kan splitting \(X_m=\bigoplus_{\theta\colon[m]\twoheadrightarrow[r]}\theta^*N_rX\) [Tag 019G], applied to \(X=\Gamma K\), gives \((\Gamma K)_m\cong\bigoplus_{[m]\twoheadrightarrow[r]}K^{-r}\), naturally in \(K\). Hence \(\Gamma\) carries a short exact sequence of complexes split in each degree to a sequence split in each simplicial degree.

Let \(CX\) be the complex with the alternating face differential and \(DX\subseteq CX\) the degenerate subcomplex. The composite \(NX\to CX\to CX/DX\) is an isomorphism of complexes, natural in \(X\) (Theorem 1.1 of *The cotangent complex*).

## 1. Shuffle maps

For simplicial abelian sheaves \(X,Y\), \(x\in N_pX\) and \(y\in N_qY\), the shuffle map is
\[
\operatorname{sh}(x\otimes y)=\sum_{(\mu,\nu)}(-1)^{\epsilon(\mu,\nu)}s_\nu x\otimes s_\mu y.
\]
Here:
- \((\mu,\nu)\) runs over the partitions of \(\{0,\dots,p+q-1\}\) into increasing lists of lengths \(p\) and \(q\);
- \(\epsilon(\mu,\nu)\) is the number of pairs with \(\mu_i>\nu_j\);
- \(s_J=s_{j_t}\cdots s_{j_1}\) for \(J=(j_1<\dots<j_t)\).

**Lemma 1.1.** \(\operatorname{sh}\) carries \(N_pX\otimes N_qY\) into \(N_{p+q}(X\otimes Y)\).

**Proof.** Put \(n=p+q\). The operator \(s_J\) is \(\alpha^*\) for the surjection \(\alpha\colon[n]\to[n-|J|]\) with \(\alpha(k+1)=\alpha(k)\) exactly for \(k\in J\). So the term of \((\mu,\nu)\) is \(\alpha^*x\otimes\beta^*y\), where:
- \(\alpha\colon[n]\to[p]\) increases exactly at the steps \(k\to k+1\) with \(k\in\mu\);
- \(\beta\colon[n]\to[q]\) increases exactly at the steps in \(\nu\).

Let \(1\leq i\leq n\). Then \(d_i\) gives \((\alpha\delta^i)^*x\otimes(\beta\delta^i)^*y\). If \(\alpha\delta^i\) misses a value \(j\), then \(\alpha\delta^i=\delta^j\alpha'\), and the term contains \(d_jx\). The value \(0=\alpha\delta^i(0)\) is never missed, so \(j\geq1\) and \(d_jx=0\). The same holds for \(\beta\).

- If \(i=n\) and the last step lies in \(\mu\), then \(\alpha\delta^n\) misses \(p\). If it lies in \(\nu\), then \(\beta\delta^n\) misses \(q\).
- If \(i<n\) and both steps at the vertex \(i\) lie in \(\mu\), then \(\alpha\delta^i\) misses \(\alpha(i)\geq1\). If both lie in \(\nu\), then \(\beta\delta^i\) misses \(\beta(i)\geq1\).

In these cases the term vanishes. Otherwise the steps \(i-1\) and \(i\) lie in different lists. Exchanging the two is a fixed-point-free involution on such shuffles, and deleting the vertex \(i\) gives the same pair \((\alpha\delta^i,\beta\delta^i)\). The exchange changes \(\epsilon\) by one, so the two terms cancel. \(\square\)

**Proposition 1.2.**

1. \(\operatorname{sh}\colon NX\otimes NY\to N(X\otimes Y)\) is a natural chain map and a chain homotopy equivalence.
2. The shuffle maps are associative and unital: \(\operatorname{sh}(1\otimes w)=1\otimes w\) for \(1\in N_0\mathbb Z\).
3. \(A=NR\), with the product \(N(\mu_R)\circ\operatorname{sh}\), is a differential graded ring in nonpositive degrees. For an \(R\)-module \(E\), \(NE\) is a left \(A\)-module through \(\alpha_{NE}=N(\alpha_E)\circ\operatorname{sh}\), where \(\alpha_E\) is the action. For an \(R\)-linear \(f\), \(N(f)\) is \(A\)-linear.
4. \(N\colon R\text{-}\operatorname{Mod}\to C^{\leq0}(A)\) is exact and commutes with filtered colimits, and \(f\) is a quasi-isomorphism if and only if \(N(f)\) is one.

**Proof.** (1) The formula defines a natural chain map \(CX\otimes CY\to C(X\otimes Y)\). It carries \(DX\otimes CY+CX\otimes DY\) into \(D(X\otimes Y)\), and the map it induces on the quotients is a natural chain homotopy equivalence (Theorem 1.3 of *The cotangent complex*, whose homotopies are universal formulas and so apply to sheaves). By Lemma 1.1 the formula carries \(NX\otimes NY\) into \(N(X\otimes Y)\). Under the natural isomorphisms \(N\cong C/D\) of the Conventions, this restriction is the map induced on the quotients. On \(N(X\otimes Y)\) the alternating differential is \(d_0\).

(2) The proof of Proposition 2.1 of the lesson on simplicial rings shows, without using any ring structure, the following. Both iterated shuffle maps \(NV\otimes NW\otimes NX\to N(V\otimes W\otimes X)\) are the sum over the \((p,q,r)\)-shuffles with the sign of the shuffle permutation. The only \((0,q)\)-shuffle applies all degeneracies to the degree-\(0\) factor, with sign \(+1\), and all degeneracies of \(1\) are \(1\).

(3) By naturality of \(\operatorname{sh}\) and (2),
\[
\begin{aligned}
&N(\mu)\operatorname{sh}(N(\mu)\operatorname{sh}(a\otimes b)\otimes c)\\
&\quad=N(\mu(\mu\otimes1))\operatorname{sh}(\operatorname{sh}(a\otimes b)\otimes c),
\end{aligned}
\]
and similarly for the other bracketing. Associativity of \(\mu\) gives associativity of the product. The product is a chain map, which is the Leibniz rule. The action is associative in the same way, with \(\alpha_E\) in place of one \(\mu\). Naturality of \(\operatorname{sh}\) gives the \(A\)-linearity of \(N(f)\).

(4) \(N\) is an exact equivalence of abelian categories. Filtered colimits are exact and so commute with the finite limits defining \(N_n\); colimits in \(C(A)\) are formed on underlying complexes. The last statement is the definition. \(\square\)

## 2. The left adjoint

**Construction 2.1.** For \(K\in\operatorname{Ch}^{\leq0}(T)\), let \(R\otimes\Gamma K\) be the free \(R\)-module, with \(R_m\otimes(\Gamma K)_m\) in degree \(m\). Put
\[
\begin{aligned}\eta'_K&=\operatorname{sh}_{R,\Gamma K}\circ(1_A\otimes u_K)\colon\\&\quad A\otimes K\to N(R\otimes\Gamma K).\end{aligned}
\]
By (0.1) there is a unique map \(\chi_K\colon\Gamma(A\otimes K)\to R\otimes\Gamma K\) with \(N(\chi_K)u_{A\otimes K}=\eta'_K\).

For \(M\in C^{\leq0}(A)\), with underlying complex \(UM\) and action \(\alpha_M\), define \(R\)-linear maps
\[
b^0,b^1\colon R\otimes\Gamma(A\otimes UM)\to R\otimes\Gamma UM
\]
by \(b^0=1\otimes\Gamma(\alpha_M)\) and \(b^1(r\otimes z)=r\,\chi_{UM}(z)\). Put \(L(M)=\operatorname{coker}(b^0-b^1)\), with projection \(\ell_M\), and let \(j\colon\Gamma UM\to R\otimes\Gamma UM\) be the map \(z\mapsto1\otimes z\).

**Proposition 2.2 (adjunction).** For \(M\in C^{\leq0}(A)\) and an \(R\)-module \(E\), the map
\[
\Phi(h)=N(h\,\ell_Mj)\circ u_{UM}
\]
is a bijection \(\operatorname{Hom}_R(L(M),E)\to\operatorname{Hom}_A(M,NE)\), natural in \(M\) and \(E\). So \(L\) is a functor left adjoint to \(N\).

Put \(\eta_M=\Phi(1_{L(M)})\) and \(\varepsilon_E=\Phi^{-1}(1_{NE})\). Then:
- \(\Phi(h)=N(h)\eta_M\) for all \(h\);
- \(\Phi(\varepsilon_E\circ L(f))=f\) for every \(A\)-linear \(f\colon M\to NE\);
- in particular \(N(\varepsilon_E)\eta_{NE}=1\).

**Proof.** An \(R\)-linear \(\hat g\colon R\otimes\Gamma UM\to E\) is determined by \(g=\hat gj\), and \(g\) corresponds by (0.1) to \(c=N(g)u_{UM}\). Two \(R\)-linear maps out of a free module agree exactly when their restrictions to the generators agree, that is, when the transposes of these restrictions by (0.1) agree.

The restriction of \(\hat gb^0\) is \(g\,\Gamma(\alpha_M)\). Its transpose is \(N(g)u_{UM}\alpha_M=c\,\alpha_M\), by naturality of \(u\).

The restriction of \(\hat gb^1\) is \(\alpha_E(1\otimes g)\chi_{UM}\). By naturality of \(\operatorname{sh}\), its transpose is
\[
\begin{aligned}&N(\alpha_E)N(1\otimes g)\operatorname{sh}(1\otimes u_{UM})\\&\quad=N(\alpha_E)\operatorname{sh}(1\otimes c)=\alpha_{NE}(1\otimes c).\end{aligned}
\]
So \(\hat g\) factors through \(L(M)\) exactly when \(c\) is \(A\)-linear, which gives the bijection.

Naturality in \(E\) is clear. For \(m\colon M'\to M\), the maps \(1\otimes\Gamma(Um)\) commute with \(b^0\) (since \(m\) is \(A\)-linear) and with \(b^1\) (by naturality of \(\chi\)). They induce \(L(m)\), and \(\Phi(hL(m))=\Phi(h)m\) by naturality of \(u\).

Naturality in \(E\) applied to \(1_{L(M)}\) gives \(\Phi(h)=N(h)\eta_M\). Naturality in \(M\) applied to \(\varepsilon_E\) gives \(\Phi(\varepsilon_EL(f))=\Phi(\varepsilon_E)f=f\). \(\square\)

**Proposition 2.3 (free modules).** For \(K\in\operatorname{Ch}^{\leq0}(T)\), the map \(\eta'_K\) is an \(A\)-linear quasi-isomorphism. There is a unique isomorphism \(\phi_K\colon L(A\otimes K)\to R\otimes\Gamma K\) with \(N(\phi_K)\eta_{A\otimes K}=\eta'_K\), and it is natural in \(K\). In particular \(\eta_{A\otimes K}\) is a quasi-isomorphism.

**Proof.** By associativity and naturality of shuffle maps,
\[
\begin{aligned}&N(\mu\otimes1)\operatorname{sh}(a\otimes\operatorname{sh}(b\otimes w))\\&\quad=\operatorname{sh}(N(\mu)\operatorname{sh}(a\otimes b)\otimes w),\end{aligned}
\]
which is the \(A\)-linearity of \(\eta'_K\). It is a quasi-isomorphism by Proposition 1.2 (1), \(u_K\) being an isomorphism.

By the unit property, \(\eta'_K(1\otimes k)=N(j)u_K(k)\). Hence, for \(R\)-linear \(\hat g\) with \(g=\hat gj\), the \(A\)-linear map \(N(\hat g)\eta'_K\) is the extension of \(N(g)u_K\). So \(\hat g\mapsto N(\hat g)\eta'_K\) is a bijection \(\operatorname{Hom}_R(R\otimes\Gamma K,E)\to\) \(\operatorname{Hom}_A(A\otimes K,NE)\), natural in \(E\).

Let \(\phi_K\) be the unique map with \(N(\phi_K)\eta_{A\otimes K}=\eta'_K\) (Proposition 2.2), and \(\psi\) the unique \(\hat g\) with \(N(\psi)\eta'_K=\eta_{A\otimes K}\). Then:
- \(N(\psi\phi_K)\eta_{A\otimes K}=\eta_{A\otimes K}\);
- \(N(\phi_K\psi)\eta'_K=\eta'_K\).

By the two uniqueness statements, \(\psi\) is inverse to \(\phi_K\).

For a chain map \(c\colon K\to K'\), the maps \(\phi_{K'}L(A\otimes c)\) and \((1\otimes\Gamma c)\phi_K\) both satisfy \(N(-)\eta_{A\otimes K}=\eta'_{K'}(1\otimes c)\), by naturality of \(\eta\), \(\operatorname{sh}\) and \(u\). So they are equal. \(\square\)

## 3. Cell resolutions

**Definition 3.1.** For \(K\in\operatorname{Ch}^{\leq0}(T)\), let \(K^\flat\) and \(E(K)\) be the complexes vanishing in positive degrees with, for \(n\leq0\),
\[
\begin{gathered}(K^\flat)^n=K^{n-1},\quad d=-d_K,\\ E(K)^n=K^{n-1}\oplus K^n,\\ d(y,x)=(-dy+x,\,dx),\end{gathered}
\]
the differentials into degree \(1\) being zero. The maps \(\iota\colon y\mapsto(y,0)\) and \(\pi\colon(y,x)\mapsto x\) are chain maps, and \(0\to K^\flat\to E(K)\to K\to0\) is exact and split in each degree.

**Lemma 3.2.** \(L(A\otimes\iota)\) is a monomorphism, with cokernel map \(L(A\otimes\pi)\).

**Proof.** By naturality of \(\phi\) (Proposition 2.3), these maps are \(1\otimes\Gamma(\iota)\) and \(1\otimes\Gamma(\pi)\). By the Conventions, \(\Gamma K^\flat\to\Gamma E(K)\to\Gamma K\) is split exact in each simplicial degree, so it stays exact after \(R_m\otimes-\). \(\square\)

**Lemma 3.3 (attachments).** Let \(0\to X\to Y\to A\otimes K\to0\) be exact in \(C^{\leq0}(A)\), with \(K\in\operatorname{Ch}^{\leq0}(T)\). Let \(s\colon A\otimes K\to Y\) be an \(A\)-linear graded section of the projection \(e\). Then:
- \(L(X)\to L(Y)\) is a monomorphism with cokernel map \(L(e)\);
- if \(\eta_X\) is a quasi-isomorphism, so is \(\eta_Y\).

**Proof.** For \(k\in K^n\) put \(f(k)=d\,s(1\otimes k)-s(1\otimes dk)\). It maps to \(0\) under \(e\), so \(f(k)\in X^{n+1}\). Moreover \(f=0\) on \(K^0\), since \(X^1=0\), and \(df(k)=-f(dk)\). Hence:
- \(y\mapsto f(y)\) is a chain map \(K^\flat\to X\);
- \((y,x)\mapsto f(y)+s(1\otimes x)\) is a chain map \(E(K)\to Y\), since both sides of the chain-map equation give \(-f(dy)+f(x)+s(1\otimes dx)\).

Let \(g\colon A\otimes K^\flat\to X\) and \(h\colon A\otimes E(K)\to Y\) be their \(A\)-linear extensions. Then \(h\circ(A\otimes\iota)\) is \(g\) followed by the inclusion of \(X\), and \(e\circ h=A\otimes\pi\).

As graded modules, \(A\otimes E(K)=(A\otimes K^\flat)\oplus(A\otimes K)\). Colimits in \(C(A)\) are formed on graded modules. So the pushout of \(g\) and \(A\otimes\iota\) is \(X\oplus(A\otimes K)\) as a graded module, and its map to \(Y\) is \((x,w)\mapsto x+s(w)\). This map is bijective, so the square is cocartesian.

The functor \(L\) preserves pushouts. A pushout of a monomorphism in an abelian category is a monomorphism with the same cokernel. By Lemma 3.2, \(L(X)\to L(Y)\) is therefore a monomorphism, and its cokernel is \(L(A\otimes K)\), through the map induced by \(L(h)\) and \(L(A\otimes\pi)\). That map is \(L(e)\), since \(e\) vanishes on \(X\) and \(eh=A\otimes\pi\).

Applying the exact functor \(N\), the units \(\eta_X\), \(\eta_Y\), \(\eta_{A\otimes K}\) form a morphism of short exact sequences, by naturality of \(\eta\). Since \(\eta_{A\otimes K}\) is a quasi-isomorphism (Proposition 2.3), the five lemma gives the last statement. \(\square\)

**Lemma 3.4 (resolutions).** There is a functor \(M\mapsto\widetilde M\) on \(C^{\leq0}(A)\) with the following properties:
- a natural quasi-isomorphism \(p_M\colon\widetilde M\to M\);
- a filtration by submodules \(0=\widetilde M_{\leq-1}\subseteq\widetilde M_{\leq0}\subseteq\cdots\) with union \(\widetilde M\), each inclusion \(\widetilde M_{\leq s-1}\subseteq\widetilde M_{\leq s}\) being as in Lemma 3.3.

**Proof.** *Free surjections.* For \(k<0\) let \(D^k\) be \(\mathbb Z\xrightarrow{1}\mathbb Z\) in degrees \(k,k+1\), and let \(D^0=\mathbb Z\) in degree \(0\). Let \(V(M)\) be the sum of the complexes \(\mathbb Z_U\otimes D^k\), one for each object \(U\) and each section \(\sigma\in M^k(U)\), \(k\leq0\). Map this summand to \(M\) by sending the generator to \(\sigma\) and, for \(k<0\), its differential to \(d\sigma\). For \(k=0\), \(\sigma\) is a cycle because \(M^1=0\). The extension \(F(M)=A\otimes V(M)\to M\) is surjective in each degree, functorial in \(M\), and lies in \(C^{\leq0}(A)\).

*The resolution.* Put \(P_{-1}=M\), \(P_0=F(M)\) and \(P_s=F(\ker(P_{s-1}\to P_{s-2}))\), with \(P_{-2}=0\). This gives an exact sequence \(\cdots\to P_1\xrightarrow{\partial}P_0\xrightarrow{\varepsilon}M\to0\), with \(P_s=A\otimes V_s\).

Let \(\widetilde M\) have the degree-\(n\) term \(\bigoplus_{s\geq0}P_s^{n+s}\). This is a finite sum (\(0\leq s\leq-n\)), zero for \(n>0\). For \(x\) of total degree \(n\) in \(P_s\), put
\[
d(x)=d_{P_s}x+(-1)^n\partial x,
\]
with \(\partial=0\) on \(P_0\). Then \(d^2=0\), because \(\partial\) is a chain map with \(\partial^2=0\). For \(a\in A^i\), \(\partial(ax)=a\partial x\), so
\[
d(ax)=(da)x+(-1)^ia\,dx,
\]
the Leibniz rule.

*The map \(p_M\).* Let \(p_M\) be \(\varepsilon\) on \(P_0\) and \(0\) on the other columns. It is \(A\)-linear and natural. It is a chain map because \(\varepsilon d_P=d_M\varepsilon\) and \(\varepsilon\partial=0\).

*Acyclicity of the augmented complex.* Let \(T\) be the complex with \(T^n=\bigoplus_{s\geq-1}P_s^{n+s}\), with the same formula for \(d\) and \(\partial=\varepsilon\) on \(P_0\). Let \(z\) be a cycle of degree \(n\) over \(U\), with components \(z_s\).
- The component of \(dz\) in the column \(-1\) is \(dz_{-1}\pm\varepsilon z_0\). Locally \(z_{-1}=\varepsilon w\) with \(w\in P_0^{n-1}\), \(\varepsilon\) being onto. Subtracting \(\pm dw\) kills \(z_{-1}\).
- Then the cycle condition in the column \(-1\) reads \(\varepsilon z_0=0\). By exactness, locally \(z_0=\partial w'\), and subtracting \(\pm dw'\) kills \(z_0\).
- Continuing, the last step uses \(w''\in P_{S+1}^{0}\) with \(S=-n\). It introduces \(d_Pw''\in P_{S+1}^1=0\) and nothing else.

After finitely many local steps \(z\) becomes \(0\). So every cycle of \(T\) is locally a boundary, and \(T\) is acyclic.

*The quasi-isomorphism.* The column \(-1\) is a subcomplex of \(T\), with \(M^{n-1}\) in degree \(n\) and differential \(d_M\); the quotient is \(\widetilde M\). In the long exact sequence, the connecting map \(H^n(\widetilde M)\to H^{n+1}\) of the subcomplex, which is \(H^n(M)\), is \((-1)^nH^n(p_M)\): lift a cycle \(x\) to \(T\) and apply \(d\). Since \(T\) is acyclic, this map is an isomorphism, so \(p_M\) is a quasi-isomorphism.

*The filtration.* Let \(\widetilde M_{\leq s}\) be the sum of the columns \(t\leq s\), a submodule. Its quotient by \(\widetilde M_{\leq s-1}\) is \(P_s\) regraded, with differential \(d_P\). This is \(A\otimes V'_s\) with \(V'^m_s=V^{m+s}_s\) and the same differential, and \(V'_s\in\operatorname{Ch}^{\leq0}(T)\). The inclusion of the column is an \(A\)-linear graded section. \(\square\)

**Proposition 3.5.** For every \(M\in C^{\leq0}(A)\), the unit \(\eta_{\widetilde M}\) is a quasi-isomorphism.

**Proof.** By Lemma 3.3 and induction on \(s\), starting from \(\eta_0\), every \(\eta_{\widetilde M_{\leq s}}\) is a quasi-isomorphism. \(L\) preserves colimits, and \(N\) and cohomology commute with filtered colimits (Proposition 1.2 (4)). So \(\eta_{\widetilde M}=\varinjlim_s\eta_{\widetilde M_{\leq s}}\) is a quasi-isomorphism. \(\square\)

## 4. The equivalence

**Theorem 4.1.** Normalization induces an equivalence \(D_\bullet(R)\to D^{\leq0}(A)\). The composite \(N\colon D_\bullet(R)\to D(A)\) is fully faithful, and its essential image consists of the objects \(M\) with \(H^iM=0\) for \(i>0\).

**Proof.** Put \(G(M)=L(\widetilde M)\).

*\(G\) preserves quasi-isomorphisms.* Let \(f\colon M\to M'\) be a quasi-isomorphism. Then \(p_{M'}\widetilde f=fp_M\) shows that \(\widetilde f\) is one. Next \(NG(f)\eta_{\widetilde M}=\eta_{\widetilde M'}\widetilde f\) and Proposition 3.5 show that \(NG(f)\) is one, so \(G(f)\) is one by Proposition 1.2 (4). Hence \(G\) induces \(\bar G\colon D^{\leq0}(A)\to D_\bullet(R)\).

*The counit.* For an \(R\)-module \(E\), put \(e_E=\varepsilon_E\circ L(p_{NE})\). By naturality of \(\eta\) and Proposition 2.2,
\[
\begin{aligned}N(e_E)\eta_{\widetilde{NE}}&=N(\varepsilon_E)\eta_{NE}\,p_{NE}\\&=p_{NE},\end{aligned}
\]
so \(e_E\) is a quasi-isomorphism.

*Conclusion.* Natural transformations between functors preserving quasi-isomorphisms remain natural on the localizations, since the morphisms there are composites of maps and inverses of quasi-isomorphisms. So
\[
[\eta_{\widetilde M}][p_M]^{-1}\colon M\to N\bar GM
\]
and \([e_E]\colon\bar GNE\to E\) are natural isomorphisms, and \(N\) and \(\bar G\) are quasi-inverse equivalences. By Proposition 1.2 of the lesson on differential graded modules, applied to the opposite ring, \(D^{\leq0}(A)\to D(A)\) is fully faithful with the stated essential image. \(\square\)

**Corollary 4.2.** \(D_\bullet(R)\) is additive. For \(R\)-modules \(E\) and \(F\), normalization is an isomorphism of groups
\[
\operatorname{Hom}_{D_\bullet(R)}(E,F)\to\operatorname{Hom}_{D(A)}(NE,NF).
\]

**Proof.** \(N\) carries \(E\oplus F\), with its injections and projections, to a biproduct of \(D(A)\). An equivalence onto a full subcategory reflects biproduct diagrams, so finite sums are biproducts in \(D_\bullet(R)\). The addition \(a+b=\nabla(a\oplus b)\Delta\) is therefore defined, and \(N\) preserves it. It makes \(D_\bullet(R)\) additive, since it corresponds to the addition of \(D(A)\) under the bijections of Theorem 4.1. \(\square\)

## 5. Unbounded modules

**Proposition 5.1.** The essential image of \(N\colon D_\bullet(R)\to D(A)\) is all of \(D(A)\) if and only if \(\pi_0(R)=0\). In that case both categories are zero.

**Proof.** Since \(A^1=0\), \(t_0(A)=A^0/dA^{-1}=H^0(A)=\pi_0(R)\), and \(A\to t_0(A)\) is a map of differential graded rings (Proposition 1.3 of the lesson on differential graded modules). If \(H^0(A)\neq0\), the module \(H^0(A)\) placed in degree \(1\), with \(A\) acting through \(t_0(A)\), has \(H^1\neq0\). By Theorem 4.1 it is not in the essential image.

Conversely, let \(M\) be a module. For \(a\in A^0\) and a cycle \(m\), \(d(am)=a\,dm=0\), and \(a\,dm'=d(am')\). For \(b\in A^{-1}\), \((db)m=d(bm)\). So each \(H^iM\) is a unital \(H^0(A)\)-module, and it vanishes if \(H^0(A)=0\). Then every module is acyclic, every object of \(D(A)\) is zero, and so is \(D_\bullet(R)\cong D^{\leq0}(A)\). \(\square\)

**Example 5.2.** Let \(T\) be the topos of sets and \(R=\mathbb Z\), constant. Then \(N_n\mathbb Z=0\) for \(n\geq1\), so \(A=\mathbb Z\) in degree \(0\). Put \(X=\mathbb Z[-1]\), that is, \(\mathbb Z\) in degree \(1\).
- For every simplicial abelian group \(E\), \(\operatorname{Hom}_{D(\mathbb Z)}(NE,X)=0\), by Proposition 1.2 (1) of the lesson on differential graded modules with \(n=0\).
- Shifting is an automorphism of \(D(\mathbb Z)\), so \(\operatorname{End}(X)=\operatorname{End}(\mathbb Z)\). This is \(\mathbb Z\), because the one-term complex \(\mathbb Z\) is a bounded complex of projectives [Tag 064B] and there are no nonzero homotopies.

If \(NE\) were isomorphic to \(X\), the identity of \(X\) would be zero. So \(X\) is not a normalization.

## 6. Exercises

**Exercise 6.1.** For \(x\in N_1X\) and \(y\in N_1Y\), write out \(\operatorname{sh}(x\otimes y)\). Check directly that \(d_1\) and \(d_2\) kill it, and that \(d_0\operatorname{sh}(x\otimes y)=\operatorname{sh}(dx\otimes y)-\operatorname{sh}(x\otimes dy)\).

**Exercise 6.2.** Let \(R\) be the constant simplicial ring of a ring \(\Lambda\) of \(T\). Show that \(L(M)\cong\Gamma(M)\) for every complex \(M\) of \(\Lambda\)-modules in nonpositive degrees.

## 7. Complete solutions

**6.1.** The \((1,1)\)-shuffles are \(\mu=(0),\nu=(1)\), with \(\epsilon=0\), and \(\mu=(1),\nu=(0)\), with \(\epsilon=1\). So
\[
\operatorname{sh}(x\otimes y)=s_1x\otimes s_0y-s_0x\otimes s_1y.
\]
- From \(d_1s_1=d_1s_0=1\), \(d_1\) gives \(x\otimes y-x\otimes y=0\).
- From \(d_2s_1=1\) and \(d_2s_0=s_0d_1\), \(d_2\) gives \(x\otimes s_0d_1y-s_0d_1x\otimes y=0\).
- From \(d_0s_1=s_0d_0\) and \(d_0s_0=1\), \(d_0\) gives \(s_0d_0x\otimes y-x\otimes s_0d_0y\).

The last expression is \(\operatorname{sh}(d_0x\otimes y)-\operatorname{sh}(x\otimes d_0y)\), since the only \((0,1)\)-shuffle applies \(s_0\) to the factor of degree \(0\). The sign \(-1\) is \((-1)^{|x|}\) for \(|x|=-1\).

**6.2.** Here \(A=\Lambda\) in degree \(0\). A shuffle with a factor of degree \(0\) applies all degeneracies to that factor, so \(\Lambda\) acts on \(NE\) degreewise. Hence \(A\)-linear maps \(M\to NE\) are the \(\Lambda\)-linear chain maps. Dold–Kan in the abelian category of \(\Lambda\)-modules [Tag 019G] gives a bijection, natural in \(E\),
\[
\operatorname{Hom}_\Lambda(\Gamma M,E)\cong\operatorname{Hom}(M,NE),
\]
where \(\Gamma\) is formed in \(\Lambda\)-modules. Its underlying simplicial sheaf is the \(\Gamma\) of abelian sheaves, by the splitting of the Conventions. By Proposition 2.2, \(L(M)\) represents the same functor, so \(L(M)\cong\Gamma(M)\).

## Sources

The question whether normalization identifies the derived category of modules over a simplicial ring of a topos with the connective part of the derived category of differential graded modules is due to Illusie, in his work on the cotangent complex. For the punctual topos the statement is contained in the Quillen equivalence of Schwede and Shipley, *Equivalences of monoidal model categories*, [arXiv:math/0209342](https://arxiv.org/abs/math/0209342), whose left adjoint is the same coequalizer. The Dold–Kan correspondence and the Eilenberg–Zilber theorem are taken from the programme lesson *The cotangent complex* and the Stacks project. The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
