# Haar measure on locally compact groups

*Originally written by Claude Opus 5.5 (Anthropic), September 2026, with a separate historical AI spot-check of that text. Repaired and self-checked by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. No human review is claimed. Original programme content is dedicated under CC0, except the explicitly marked Fremlin adaptation in Theorem 8.3, Lemma 8.4 and the proof of Theorem 9.2, which are distributed under the Design Science License.*

This lesson constructs Haar measure on an arbitrary locally compact group and develops the measure theory that goes with it. Sections 2–6 work on locally compact spaces. They prove the Riesz representation theorem for Radon measures, treat image measures and densities, build the product of two Radon measures with its Tonelli and Fubini theorems, and identify \(L^2\) of a product with a Hilbert tensor product. Sections 7–11 turn to groups: topological groups, existence and uniqueness of Haar measure, the modular function, and the inversion formula. Sections 12–15 treat products of groups, groups that are not \(\sigma\)-compact, convolution, and approximate identities. Section 16 has exercises with solutions.

The general construction imposes no countability assumption. The group need not be \(\sigma\)-compact, second countable or unimodular, and its Haar measure need not be \(\sigma\)-finite. Additional results state their hypotheses explicitly, including the unimodularity condition in Theorem 14.4. This generality needs care: a Borel set of infinite measure can have only null compact subsets, and Fubini's theorem can fail. Section 13 shows what goes wrong, and the rest of the lesson is arranged so that it does no harm.

Haar measure makes a locally compact group \(G\) into a measure space on which \(G\) acts by translations. Then \(L^1(G)\) is a Banach \(*\)-algebra under convolution, and \(L^2(G)\) carries the left and right regular representations. These objects are the starting point of abstract harmonic analysis, and of the group von Neumann algebras studied in the course on modular theory and weights.

The lesson builds on four sources, cited where they are used:
- [Measure and Hilbert space tools for Haar integration](measure-and-hilbert-space-tools.md), Theorems 1.1–4.2, for the full measure-theory proofs; the measure convention is compared with Fremlin below;
- [The Stone–Weierstrass theorem for functions vanishing at infinity](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity), for locally compact spaces and Urysohn's lemma;
- [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian), for Tychonoff's theorem;
- [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators), for Hilbert tensor products and multiplication operators.

The exact statements are collected at the end, under "Results used from other lessons". Core preparation is [Point-Set Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90); [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) provides Fremlin’s broader measure-theory setting. The arbitrary-product and Hilbert-space proofs used here are the advanced programme results named above.

Freely accessible complementary treatments are Fremlin’s [Measure Theory](https://www1.essex.ac.uk/maths/people/fremlin/mtcont.htm) and F. van Doorn’s [Formalized Haar Measure](https://arxiv.org/abs/2102.07636v1). Fischer and Ruzhansky’s freely accessible [*Quantization on Nilpotent Lie Groups*](https://biblio.ugent.be/publication/8585474) supplies further convolution and Heisenberg-group examples. F. van Doorn’s freely accessible paper also discusses the historical development and distinguishes the scopes of the classical constructions.

## 1. Conventions

*Spaces.* An *LCH space* is a Hausdorff space that is locally compact. Its compact subsets are closed. \(C_c(X)\) is the space of continuous complex functions with compact support, \(C_c^+(X)\) is the set of \(f\in C_c(X)\) with \(f\geq0\) and \(f\neq0\), and \(\|f\|_{\sup}=\sup_x|f(x)|\). For an open set \(U\) we write \(f\prec U\) when \(f\in C_c(X)\), \(0\leq f\leq1\) and \(\operatorname{supp}f\subseteq U\). For a compact set \(K\) we write \(K\prec f\) when \(f\in C_c(X)\), \(0\leq f\leq 1\) and \(f=1\) on \(K\). A function \(h\colon X\to[0,\infty]\) is *lower semicontinuous* (lsc) if every set \(\{h>c\}\) is open; lsc functions are Borel.

*Four tools from topology.* The first two tools are proved in the lesson on the Stone–Weierstrass theorem; we derive the other two from them.

- **(T1)** (*Shrinking*) If \(K\subseteq U\) with \(K\) compact and \(U\) open, there is an open \(V\) with compact closure such that \(K\subseteq V\subseteq\overline V\subseteq U\). This is [Proposition 4.2(2) of the Stone–Weierstrass lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity#oa-fnd-sw-15).
- **(T2)** (*Urysohn's lemma*) If \(K\subseteq U\) as in (T1), there is \(f\) with \(K\prec f\prec U\). *Proof.* Take \(V\) from (T1). [Corollary 5.2 of the Stone–Weierstrass lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity#oa-fnd-sw-16), applied to the compact set \(K\) and the closed set \(X\setminus V\), gives \(f\in C_c(X)\) with \(0\leq f\leq1\), \(f=1\) on \(K\) and \(f=0\) off \(V\). Then \(\operatorname{supp}f\subseteq\overline V\subseteq U\). \(\square\)
- **(T3)** (*Partitions of unity*) If \(K\) is compact and \(K\subseteq U_1\cup\dots\cup U_n\) with each \(U_i\) open, there are \(h_i\prec U_i\) with \(\sum_ih_i=1\) on \(K\) and \(\sum_ih_i\leq1\) everywhere. *Proof.* For each \(x\in K\) pick an index \(i\) with \(x\in U_i\), and by (T1) an open \(V_x\ni x\) whose compact closure lies in \(U_i\). Finitely many \(V_x\) cover \(K\). Let \(F_i\) be the union of the closures of the chosen \(V_x\) that were assigned to \(i\). Then \(F_i\) is compact, \(F_i\subseteq U_i\), and \(K\subseteq\bigcup_iF_i\). Choose \(F_i\prec g_i\prec U_i\) by (T2) and set \(h_1=g_1\) and \(h_k=(1-g_1)\cdots(1-g_{k-1})g_k\). By induction, \(\sum_{k\leq m}h_k=1-\prod_{k\leq m}(1-g_k)\). This lies in \([0,1]\), and it equals \(1\) on each \(F_i\). \(\square\)
- **(T4)** (*Tube lemma*) If \(K\subseteq X\) and \(L\subseteq Y\) are compact and \(K\times L\subseteq W\) with \(W\) open in \(X\times Y\), there are open \(U\supseteq K\) and \(V\supseteq L\) with \(U\times V\subseteq W\). *Proof.* Fix \(x\in K\). Each \((x,y)\), \(y\in L\), lies in an open box inside \(W\); finitely many boxes \(P_j\times Q_j\) of this kind have \(Q_j\) covering \(L\). Put \(P^x=\bigcap_jP_j\) and \(Q^x=\bigcup_jQ_j\); then \(P^x\times Q^x\subseteq W\). Cover \(K\) by finitely many \(P^{x_i}\), and let \(U=\bigcup_iP^{x_i}\) and \(V=\bigcap_iQ^{x_i}\). \(\square\)

*Measures and functions.* A measure is positive and countably additive. \(\mathcal B(X)\) denotes the Borel sets of \(X\), the \(\sigma\)-algebra generated by the open sets; functions on \(X\) are Borel unless said otherwise. A Borel set is *\(\sigma\)-finite* for a measure when countably many Borel sets of finite measure cover it. For \(1\leq p<\infty\), \(L^p(\mu)\) consists of the Borel functions with \(\int|f|^p\,d\mu<\infty\), modulo functions that vanish almost everywhere. Hilbert spaces are complex, and the inner product \(\langle\xi,\eta\rangle=\int\xi\bar\eta\,d\mu\) is linear in \(\xi\). For a Borel \(f\colon X\to[0,\infty]\) we use the *layer functions*
\[
s_n=2^{-n}\sum_{i=1}^{n2^n}1_{\{f>i2^{-n}\}} .
\tag{1.1}
\]
They are simple Borel functions, and they vanish where \(f\) does. They increase, \(s_n\leq s_{n+1}\), because the \(i\)-th term of \(s_n\) is at most the sum of the terms of \(s_{n+1}\) with indices \(2i-1\) and \(2i\). And \(s_n(x)\to f(x)\) at every point: if \(f(x)<n\), then \(f(x)-2^{-n}\leq s_n(x)\leq f(x)\), and if \(f(x)=\infty\), then \(s_n(x)=n\). The monotone and dominated convergence theorems, Hölder's inequality, and the completeness of \(L^p\) are proved in [Measure and Hilbert space tools for Haar integration](measure-and-hilbert-space-tools.md), Theorems 2.1, 2.2, 3.1 and 3.2. The exact uses are listed under "Results used from other lessons".

*Groups.* A group \(G\) is a *locally compact group* when it carries a locally compact Hausdorff topology for which \((x,y)\mapsto xy\) and \(x\mapsto x^{-1}\) are continuous; \(e\) is its identity. For a function \(f\) on \(G\) and \(y\in G\) put
\[
L_yf(x)=f(y^{-1}x),\qquad R_yf(x)=f(xy),\qquad \check f(x)=f(x^{-1}).
\]
Then \(L_{yz}=L_yL_z\) and \(R_{yz}=R_yR_z\). The *left and right regular representations* of \(G\) on \(L^2(G)\) are \(\lambda(g)=L_g\) and \(\rho(g)=\Delta(g)^{1/2}R_g\), where \(\Delta\) is the modular function of Section 10; Exercise 16.3 shows that they are unitary representations.

## 2. Radon measures and the Riesz representation theorem

**Definition 2.1** (Radon measure). A *Radon measure* on an LCH space \(X\) is a measure \(\mu\) on \(\mathcal B(X)\) with the following three properties.

- **(R1)** \(\mu(K)<\infty\) for every compact \(K\).
- **(R2)** (*outer regularity*) \(\mu(E)=\inf\{\mu(U):U\supseteq E\ \text{open}\}\) for every Borel set \(E\).
- **(R3)** (*inner regularity on open sets*) \(\mu(U)=\sup\{\mu(K):K\subseteq U\ \text{compact}\}\) for every open \(U\).

This is the notion of regularity used throughout the lesson. Inner regularity is not required on all Borel sets, because it can fail (Example 13.4). Proposition 2.3 shows that it holds on every \(\sigma\)-finite set.

**Theorem 2.2** (Riesz representation theorem). Take a positive linear functional \(I\) on \(C_c(X)\). There is exactly one Radon measure \(\mu\) on \(X\) with \(I(f)=\int f\,d\mu\) for every \(f\in C_c(X)\). Moreover, every Radon measure \(\mu\) satisfies, with \(I(f)=\int f\,d\mu\),
\[
\mu(U)=\sup\{I(f):f\prec U\}\quad(U\ \text{open}),\qquad
\mu(K)=\inf\{I(f):f\in C_c(X),\ 1_K\leq f\}\quad(K\ \text{compact}).
\tag{2.1}
\]

*Regularity warning:* The stronger requirement that a measure be inner and outer regular on every Borel set is inappropriate here. In that form it fails for the Haar integral of \(\mathbb R\times\mathbb R_d\) (Example 13.4).

**Proof.** *Step 1: formula (2.1) and uniqueness.* Let \(\mu\) be Radon. If \(f\prec U\), then \(\int f\,d\mu\leq\mu(U)\). If \(K\subseteq U\) is compact, Urysohn's lemma (T2) gives \(K\prec f\prec U\), and then \(\mu(K)\leq\int f\,d\mu\). With (R3) this proves the first formula. If \(1_K\leq f\), then \(\mu(K)\leq\int f\,d\mu\); if \(U\supseteq K\) is open, (T2) gives \(K\prec f\prec U\) with \(\int f\,d\mu\leq\mu(U)\). With (R2) this proves the second formula. By the first formula, two Radon measures that give every \(f\in C_c(X)\) the same integral agree on open sets, and then on all Borel sets by (R2).

*Step 2: an outer measure.* For open \(U\) define \(\mu(U)=\sup\{I(f):f\prec U\}\), and for any \(A\subseteq X\) put \(\mu^*(A)=\inf\{\mu(U):U\supseteq A\ \text{open}\}\). Then \(\mu^*=\mu\) on open sets, and \(\mu^*\) is monotone. Let \(U=\bigcup_jU_j\) with \(U_j\) open, and let \(f\prec U\). The compact set \(\operatorname{supp}f\) lies in \(U_1\cup\dots\cup U_n\) for some \(n\). The partition of unity (T3) gives \(h_j\prec U_j\) with \(\sum_{j\leq n}h_j=1\) on \(\operatorname{supp}f\). So \(f=\sum_{j\leq n}fh_j\) with \(fh_j\prec U_j\), and \(I(f)\leq\sum_j\mu(U_j)\). Hence \(\mu(U)\leq\sum_j\mu(U_j)\). For arbitrary sets \(A_j\), choose open \(U_j\supseteq A_j\) with \(\mu(U_j)\leq\mu^*(A_j)+\varepsilon2^{-j}\); this gives \(\mu^*(\bigcup_jA_j)\leq\sum_j\mu^*(A_j)+\varepsilon\). So \(\mu^*\) is an outer measure.

*Step 3: open sets are measurable.* Let \(U\) be open. By Carathéodory's theorem [the preceding tools lesson, Theorem 1.1](measure-and-hilbert-space-tools.md#1-from-an-outer-measure-to-a-measure) it is enough to show \(\mu^*(A)\geq\mu^*(A\cap U)+\mu^*(A\setminus U)\) whenever \(\mu^*(A)<\infty\). First let \(A=V\) be open. Given \(\varepsilon>0\), choose \(f\prec V\cap U\) with \(I(f)>\mu(V\cap U)-\varepsilon\). The set \(V\setminus\operatorname{supp}f\) is open; choose \(g\prec V\setminus\operatorname{supp}f\) with \(I(g)>\mu(V\setminus\operatorname{supp}f)-\varepsilon\). The supports of \(f\) and \(g\) are disjoint, so \(f+g\prec V\) and
\[
\mu(V)\geq I(f+g)>\mu(V\cap U)+\mu(V\setminus\operatorname{supp}f)-2\varepsilon\geq\mu^*(V\cap U)+\mu^*(V\setminus U)-2\varepsilon ,
\]
since \(V\setminus U\subseteq V\setminus\operatorname{supp}f\). For general \(A\), take an open \(V\supseteq A\) with \(\mu(V)\leq\mu^*(A)+\varepsilon\), apply the open case, and use monotonicity. By Carathéodory's theorem the \(\mu^*\)-measurable sets form a \(\sigma\)-algebra on which \(\mu^*\) is countably additive. It contains the open sets, hence \(\mathcal B(X)\). Let \(\mu\) be the restriction of \(\mu^*\) to \(\mathcal B(X)\). It satisfies (R2) by construction.

*Step 4: compact sets.* Let \(K\) be compact and \(1_K\leq f\in C_c(X)\); in particular \(f\geq0\). For \(0<c<1\) the open set \(U_c=\{f>c\}\) contains \(K\), and every \(g\prec U_c\) satisfies \(g\leq f/c\). So \(\mu(K)\leq\mu(U_c)\leq I(f)/c\), and letting \(c\to1\) gives \(\mu(K)\leq I(f)\). Some \(f\) with \(K\prec f\) exists by (T2) with \(U=X\), so \(\mu(K)<\infty\), which is (R1). Given \(\varepsilon>0\), choose an open \(U\supseteq K\) with \(\mu(U)\leq\mu(K)+\varepsilon\) and then \(f\) with \(K\prec f\prec U\): \(I(f)\leq\mu(U)\leq\mu(K)+\varepsilon\). This proves the second formula of (2.1).

*Step 5: (R3).* If \(f\prec U\), then \(f\prec V\) for every open \(V\supseteq\operatorname{supp}f\), so \(I(f)\leq\mu(V)\), and \(I(f)\leq\mu(\operatorname{supp}f)\) by (R2). Taking the supremum over \(f\prec U\) gives \(\mu(U)\leq\sup\{\mu(K):K\subseteq U\ \text{compact}\}\). The reverse inequality is monotonicity.

*Step 6: \(\mu\) represents \(I\).* By linearity it suffices to treat real \(f\in C_c(X)\) with \(0\leq f\leq1\). Fix \(N\geq1\). Put \(K_0=\operatorname{supp}f\), \(K_j=\{f\geq j/N\}\) for \(1\leq j\leq N\) (compact sets), and \(f_j=\min(\max(f-\frac{j-1}N,0),\frac1N)\). Then \(f=\sum_{j=1}^Nf_j\), each \(f_j\) is in \(C_c(X)\) with \(\operatorname{supp}f_j\subseteq K_{j-1}\), and \(\frac1N1_{K_j}\leq f_j\leq\frac1N1_{K_{j-1}}\). Integrating, \(\frac1N\mu(K_j)\leq\int f_j\,d\mu\leq\frac1N\mu(K_{j-1})\). On the other side, \(\mu(K_j)\leq I(Nf_j)\) by Step 4. Also \(Nf_j\prec U\) for every open \(U\supseteq K_{j-1}\), so \(I(Nf_j)\leq\mu(U)\), and \(I(Nf_j)\leq\mu(K_{j-1})\) by (R2). Summing over \(j\), both \(I(f)\) and \(\int f\,d\mu\) lie between \(\frac1N\sum_{j=1}^N\mu(K_j)\) and \(\frac1N\sum_{j=0}^{N-1}\mu(K_j)\). These bounds differ by at most \(\mu(\operatorname{supp}f)/N\). Let \(N\to\infty\). \(\square\)

**Proposition 2.3** (Regularity on \(\sigma\)-finite sets). Every Radon measure \(\mu\) on \(X\) has the following properties.

1. If \(E\) is Borel and \(\mu(E)<\infty\), then \(\mu(E)=\sup\{\mu(K):K\subseteq E\ \text{compact}\}\).
2. The same holds for every Borel set that is \(\sigma\)-finite for \(\mu\).
3. Every \(\sigma\)-finite Borel set \(E\) is the union of a \(\sigma\)-compact set and a Borel null set.

**Proof.** (1) Let \(\varepsilon>0\). By (R2) choose an open \(U\supseteq E\) with \(\mu(U)<\mu(E)+\varepsilon\), so \(\mu(U\setminus E)<\varepsilon\). Again by (R2) choose an open \(W\supseteq U\setminus E\) with \(\mu(W)<\varepsilon\). By (R3) choose a compact \(F\subseteq U\) with \(\mu(F)>\mu(U)-\varepsilon\). The compact set \(K=F\setminus W\) lies in \(E\): a point of \(F\) outside \(E\) is in \(U\setminus E\subseteq W\). And \(\mu(K)\geq\mu(F)-\mu(W)>\mu(E)-2\varepsilon\).
(2) Write \(E\) as an increasing union of Borel sets \(E_n\) of finite measure; then \(\mu(E)=\lim\mu(E_n)\), and (1) applies to each \(E_n\).
(3) With \(E_n\) as in (2), choose compact \(K_{n,m}\subseteq E_n\) with \(\mu(E_n\setminus K_{n,m})<1/m\). The \(\sigma\)-compact set \(S=\bigcup_{n,m}K_{n,m}\) lies in \(E\), and \(\mu(E_n\setminus S)=0\) for every \(n\), so \(\mu(E\setminus S)=0\). \(\square\)

*Where the hypotheses enter.* Local compactness and the Hausdorff property are used only through (T1)–(T3): they supply enough functions \(f\prec U\). No countability is used, and the measure \(\mu\) need not be \(\sigma\)-finite. A measure that is inner and outer regular on every Borel set would be more convenient, but Example 13.4 shows that on the group \(\mathbb R\times\mathbb R_d\) no measure of that kind represents Haar integration. So the lesson never uses inner regularity on arbitrary Borel sets.

### Bounded functionals on \(C_0(X)\)

The operator-algebra lessons also use the bounded, not necessarily positive, linear functionals on \(C_0(X)\), the space of continuous functions vanishing at infinity with the norm \(\|\cdot\|_{\sup}\). Call a functional \(\varphi\) *hermitian* if \(\varphi(f)\) is real for every real \(f\). Two facts are used below.
- *\(C_c(X)\) is dense in \(C_0(X)\).* For \(f\in C_0(X)\) and \(\varepsilon>0\), the set \(K=\{|f|\geq\varepsilon\}\) is compact. Choose \(K\prec u\) by (T2). Then \(uf\in C_c(X)\) and \(\|f-uf\|_{\sup}\leq\varepsilon\).
- *Norms of positive functionals.* A positive linear functional \(\psi\) on \(C_0(X)\) is hermitian, since every real \(f\) is \(f^+-f^-\). If \(\psi\) is bounded, then \(\|\psi\|=\sup\{\psi(f):0\leq f\leq1\}\), and by (2.1) this is \(\nu(X)\) for the Radon measure \(\nu\) that represents \(\psi\) on \(C_c(X)\). Indeed, for \(\|f\|_{\sup}\leq1\) choose \(\theta\) with \(e^{i\theta}\psi(f)\geq0\), and write \(e^{i\theta}f=u+iv\) with \(u,v\) real. Then \(|\psi(f)|=\psi(u)+i\psi(v)\) forces \(\psi(v)=0\), and \(|\psi(f)|=\psi(u)\leq\psi(u^+)\) with \(0\leq u^+\leq1\). The functions \(f\prec X\) suffice, by the density just proved.

**Theorem 2.4** (Bounded functionals on \(C_0(X)\)). Let \(X\) be an LCH space and \(\varphi\) a bounded linear functional on \(C_0(X)\).
1. (*Jordan decomposition.*) Let \(\varphi\) be hermitian. For \(f\geq0\) put \(\varphi_+(f)=\sup\{\varphi(g):g\in C_0(X),\ 0\leq g\leq f\}\). Then \(\varphi_+\) extends to a bounded positive linear functional, \(\varphi_-=\varphi_+-\varphi\) is positive, and \(\|\varphi\|=\|\varphi_+\|+\|\varphi_-\|\). Every bounded \(\varphi\) is \(\varphi_1+i\varphi_2\) with \(\varphi_1,\varphi_2\) bounded and hermitian.
2. (*Representation.*) There are finite Radon measures \(\nu_0,\dots,\nu_3\) with \(\varphi(f)=\sum_{k=0}^3i^k\int f\,d\nu_k\) for every \(f\in C_0(X)\). The set function \(\mu=\sum_ki^k\nu_k\) on \(\mathcal B(X)\) does not depend on the choice of the \(\nu_k\). It is the *complex Radon measure* of \(\varphi\), and we write \(\varphi(f)=\int f\,d\mu\). Conversely, every such \(\mu\) defines a bounded functional in this way.
3. (*Norm.*) \(\|\varphi\|=|\mu|(X)\), where \(|\mu|(E)=\sup\sum_j|\mu(E_j)|\), the supremum over the finite partitions of \(E\) into Borel sets.
4. (*Positivity.*) \(\varphi\) is positive if and only if \(\mu\geq0\); then \(\mu\) is the measure of Theorem 2.2. If \(\varphi\) is hermitian, then \(\mu=\nu_+-\nu_-\), where \(\nu_\pm\) are the Radon measures of \(\varphi_\pm\), and \(|\mu|=\nu_++\nu_-\). In particular \(|\mu|\) is a finite Radon measure.

**Proof.** (1) *Additivity.* For \(f_1,f_2\geq0\), clearly \(\varphi_+(f_1+f_2)\geq\varphi_+(f_1)+\varphi_+(f_2)\). Conversely, let \(0\leq g\leq f_1+f_2\). Put \(g_1=\min(g,f_1)\) and \(g_2=g-g_1\). Then \(0\leq g_1\leq f_1\) and \(0\leq g_2\leq f_2\), and \(\varphi(g)=\varphi(g_1)+\varphi(g_2)\leq\varphi_+(f_1)+\varphi_+(f_2)\).
- \(\varphi_+\) is positively homogeneous, and \(0\leq\varphi_+(f)\leq\|\varphi\|\,\|f\|_{\sup}\).
- So \(\varphi_+(f^+)-\varphi_+(f^-)\) for real \(f\), and then real and imaginary parts, extend \(\varphi_+\) to a positive linear functional. The extension is well defined: if \(f=a-b\) with \(a,b\geq0\), then \(a+f^-=b+f^+\).
- \(\varphi_+(f)\geq\varphi(f)\) for \(f\geq0\), so \(\varphi_-\) is positive.

*The norm.* \(\|\varphi\|\leq\|\varphi_+\|+\|\varphi_-\|\). Conversely, let \(\varepsilon>0\).
- Choose \(0\leq f,h\leq1\) with \(\varphi_+(f)>\|\varphi_+\|-\varepsilon\) and \(\varphi_-(h)>\|\varphi_-\|-\varepsilon\).
- Choose \(0\leq g\leq f\) with \(\varphi(g)>\varphi_+(f)-\varepsilon\).
- Since \(\varphi_-(h)=\sup\{-\varphi(g'):0\leq g'\leq h\}\) (substitute \(g'=h-g''\) in the definition), choose \(0\leq g'\leq h\) with \(-\varphi(g')>\varphi_-(h)-\varepsilon\).
- Then \(g-g'\) takes values in \([-1,1]\), and \(\|\varphi\|\geq\varphi(g-g')>\|\varphi_+\|+\|\varphi_-\|-4\varepsilon\).

*General \(\varphi\).* Put \(\varphi^\dagger(f)=\overline{\varphi(\bar f)}\), \(\varphi_1=\frac12(\varphi+\varphi^\dagger)\) and \(\varphi_2=\frac1{2i}(\varphi-\varphi^\dagger)\). For real \(f\), \(\varphi_1(f)=\operatorname{Re}\varphi(f)\) and \(\varphi_2(f)=\operatorname{Im}\varphi(f)\).

(2) Apply (1) to \(\varphi_1\) and \(\varphi_2\), and Theorem 2.2 to the four positive parts restricted to \(C_c(X)\). This gives Radon measures \(\nu_0,\nu_2\) for \(\varphi_{1,+},\varphi_{1,-}\) and \(\nu_1,\nu_3\) for \(\varphi_{2,+},\varphi_{2,-}\). They are finite, with \(\nu_k(X)\) the norm of the corresponding positive part. The identity \(\varphi(f)=\sum_ki^k\int f\,d\nu_k\) holds on \(C_c(X)\), and both sides are continuous for \(\|\cdot\|_{\sup}\), so it holds on \(C_0(X)\).

*Independence.* Let \(\sum_ki^k\int f\,d\nu_k=\sum_ki^k\int f\,d\nu_k'\) on \(C_0(X)\), with finite Radon measures.
- Taking real parts at real \(f\), the finite measures \(\nu_0+\nu_2'\) and \(\nu_0'+\nu_2\) give the same integrals on \(C_c(X)\).
- A sum of two finite Radon measures is Radon: (R1) is clear; for (R2) intersect the two open sets; for (R3) take the union of the two compact sets.
- By the uniqueness in Theorem 2.2 the two sums are equal, so \(\nu_0-\nu_2=\nu_0'-\nu_2'\) as set functions. The imaginary parts are treated in the same way.

*Integrals.* For a bounded Borel \(h\), put \(\int h\,d\mu=\sum_ki^k\int h\,d\nu_k\). This depends only on \(\mu\): it does for simple functions, and every bounded Borel function is a uniform limit of simple ones. Also \(|\int h\,d\mu|\leq\int|h|\,d\nu\) with \(\nu=\sum_k\nu_k\). The converse statement of (2) is clear, with \(\|\varphi\|\leq\nu(X)\).

(3) *\(\|\varphi\|\leq|\mu|(X)\).* For a Borel simple function \(s=\sum_jc_j1_{E_j}\), with the \(E_j\) a partition of \(X\), \(|\int s\,d\mu|\leq\max_j|c_j|\sum_j|\mu(E_j)|\leq\|s\|_{\sup}|\mu|(X)\). Let \(f\in C_0(X)\). Cutting the range of \(f\) into small Borel pieces, and taking on each piece a value of \(f\), gives simple \(s_n\to f\) uniformly with \(\|s_n\|_{\sup}\leq\|f\|_{\sup}\). So \(|\varphi(f)|\leq\|f\|_{\sup}|\mu|(X)\).

*\(|\mu|(X)\leq\|\varphi\|\).* Let \(E_1,\dots,E_n\) be a Borel partition of \(X\) and \(\varepsilon>0\). The measure \(\nu=\sum_k\nu_k\) is a finite Radon measure.
- By Proposition 2.3(1), choose compact \(K_j\subseteq E_j\) with \(\nu(E_j\setminus K_j)<\varepsilon/n\).
- Disjoint compact sets in a Hausdorff space have disjoint open neighbourhoods: separate each point of one from the other set by compactness of the other, then use compactness of the first. Doing this for each pair and intersecting, we get disjoint open \(W_j\supseteq K_j\). By (R2) choose open \(U_j\) with \(K_j\subseteq U_j\subseteq W_j\) and \(\nu(U_j\setminus K_j)<\varepsilon/n\).
- By (T2) choose \(K_j\prec g_j\prec U_j\). Let \(c_j=\overline{\mu(E_j)}/|\mu(E_j)|\), or \(c_j=0\) if \(\mu(E_j)=0\), and \(f=\sum_jc_jg_j\). The supports are disjoint, so \(\|f\|_{\sup}\leq1\).
- \(|g_j-1_{E_j}|\leq1_{U_j\setminus K_j}+1_{E_j\setminus K_j}\), so \(|\int g_j\,d\mu-\mu(E_j)|<2\varepsilon/n\).
- Hence \(\sum_j|\mu(E_j)|=\sum_jc_j\mu(E_j)\leq|\varphi(f)|+2\varepsilon\leq\|\varphi\|+2\varepsilon\).

The variation is itself a finite Radon measure, also for complex \(\mu\). Refining finite partitions proves finite additivity of \(|\mu|\) on disjoint Borel sets, and \(|\mu|(E)\leq\nu(E)\) with the finite Radon measure \(\nu=\sum_k\nu_k\). For a disjoint sequence, the \(\nu\)-measure of the union of the tail tends to zero. The same domination makes its variation tend to zero, turning finite additivity into countable additivity. To check regularity, approximate a Borel \(E\) from within by a compact \(K\) and from outside by an open \(U\) in \(\nu\)-measure, using Proposition 2.3(1) and (R2). Then \(|\mu|(E\setminus K)\leq\nu(E\setminus K)\) and \(|\mu|(U\setminus E)\leq\nu(U\setminus E)\), proving inner and outer regularity.

(4) If \(\varphi\) is positive, then \(\varphi_+=\varphi\), \(\varphi_-=0\) and \(\varphi_2=0\), so \(\mu\) is the measure of Theorem 2.2. If \(\mu\geq0\), then \(\int s\,d\mu\geq0\) for simple \(s\geq0\), and every \(f\geq0\) in \(C_0(X)\) is a uniform limit of such \(s\); so \(\varphi\) is positive.

Let \(\varphi\) be hermitian, so \(\varphi_2=0\) and \(\mu=\nu_+-\nu_-\).
- \(|\mu|(E)\leq\nu_+(E)+\nu_-(E)\) for every Borel \(E\), since \(|\mu(E_j)|\leq\nu_+(E_j)+\nu_-(E_j)\).
- \(|\mu|\) is additive on disjoint Borel sets: partitions of \(E\) and \(F\) combine to a partition of \(E\cup F\), and a partition of \(E\cup F\) can be refined by \(E\) and \(F\) without decreasing the sum.
- By (3) and (1), \(|\mu|(X)=\|\varphi\|=\|\varphi_+\|+\|\varphi_-\|=\nu_+(X)+\nu_-(X)\).
- So \(|\mu|(E)+|\mu|(X\setminus E)=(\nu_++\nu_-)(E)+(\nu_++\nu_-)(X\setminus E)\), with \(\leq\) in each term. Hence \(|\mu|(E)=(\nu_++\nu_-)(E)\). \(\square\)

For compact \(X\), \(C_0(X)=C(X)\), and the finite Radon measures are regular: outer regular by (R2), and inner regular on all Borel sets by Proposition 2.3(1). So Theorem 2.4 identifies the dual of \(C(X)\) with the complex regular Borel measures on \(X\), normed by total variation.

## 3. Image measures, densities, and approximation by continuous functions

This section collects four operations on a Radon measure that the rest of the lesson uses constantly: moving it by a homeomorphism, multiplying it by a positive continuous density, integrating lower semicontinuous functions, and approximating \(L^p\) functions by continuous ones.

**Proposition 3.1.** Fix a Radon measure \(\mu\) on an LCH space \(X\).

1. (*Homeomorphisms*) Let \(\theta\colon X\to X'\) be a homeomorphism onto an LCH space. Then \(\theta_*\mu(E)=\mu(\theta^{-1}(E))\) defines a Radon measure on \(X'\), and \(\int f\,d\theta_*\mu=\int f\circ\theta\,d\mu\) for every Borel \(f\geq0\) and every \(f\in L^1(\theta_*\mu)\).
2. (*Positive continuous densities*) Let \(\varphi\colon X\to(0,\infty)\) be continuous. Then \(\varphi\mu(E)=\int_E\varphi\,d\mu\) defines a Radon measure; \(\int f\,d(\varphi\mu)=\int f\varphi\,d\mu\) for every Borel \(f\geq0\); and \(\varphi\mu\) has the same null sets and the same \(\sigma\)-finite sets as \(\mu\). Consequently, if a Radon measure \(\nu\) satisfies \(\int f\,d\nu=\int f\varphi\,d\mu\) for all \(f\in C_c(X)\), then \(\nu=\varphi\mu\).
3. (*Lower semicontinuous functions*) For every lsc \(h\colon X\to[0,\infty]\),
\[
\int h\,d\mu=\sup\Big\{\int g\,d\mu:g\in C_c(X),\ 0\leq g\leq h\Big\}.
\tag{3.1}
\]
4. (*Density*) Let \(1\leq p<\infty\). Every \(f\in L^p(\mu)\) vanishes outside a \(\sigma\)-finite Borel set, and hence, after a change on a null set, outside a \(\sigma\)-compact set. The space \(C_c(X)\) is dense in \(L^p(\mu)\).

**Proof.** (1) Since \(\theta\) is a homeomorphism, \(\theta^{-1}\) maps compact, open and Borel sets of \(X'\) onto sets of the same kind in \(X\), and it preserves inclusions. So (R1)–(R3) transfer from \(\mu\) to \(\theta_*\mu\). The integral formula holds for indicators by definition, and by linearity for simple functions. The layer functions (1.1) and monotone convergence extend it to Borel \(f\geq0\), and splitting \(f\) into four nonnegative parts extends it to integrable \(f\).

(2) The formula for integrals holds for indicators by definition, hence for Borel \(f\geq0\) by the layer functions (1.1) and monotone convergence; in particular \(\varphi\mu\) is countably additive, so it is a measure. Since \(\varphi>0\), \(\int_E\varphi\,d\mu=0\) exactly when \(\mu(E)=0\). The sets \(\{1/n\leq\varphi\leq n\}\) cover \(X\), and on each of them the two measures are comparable, so the \(\sigma\)-finite sets agree. It remains to check (R1)–(R3) for \(\varphi\mu\). (R1) holds because \(\varphi\) is bounded on compact sets.
(R2): Let \(E\) be Borel with \(\varphi\mu(E)<\infty\) (otherwise take \(U=X\)), and let \(\varepsilon>0\). For \(j\in\mathbb Z\), the open sets \(V_j=\{2^{j-1}<\varphi<2^{j+1}\}\) cover \(X\). Put \(E_j=E\cap V_j\). Then \(\mu(E_j)\leq2^{1-j}\varphi\mu(E_j)<\infty\), so by (R2) for \(\mu\) there is an open \(U_j\) with \(E_j\subseteq U_j\subseteq V_j\) and \(\mu(U_j\setminus E_j)<\varepsilon2^{-|j|-j-3}\). Then \(\varphi\mu(U_j\setminus E_j)\leq2^{j+1}\mu(U_j\setminus E_j)<\varepsilon2^{-|j|-2}\). The set \(U=\bigcup_jU_j\) is open, contains \(E\), and \(U\setminus E\subseteq\bigcup_j(U_j\setminus E_j)\). So \(\varphi\mu(U\setminus E)<\varepsilon\sum_j2^{-|j|-2}<\varepsilon\).
(R3): Let \(U\) be open and \(c<\varphi\mu(U)\). If \(\mu(U\cap\{\varphi>s\})=\infty\) for some \(s>0\), then (R3) for \(\mu\) gives a compact \(K\subseteq U\cap\{\varphi>s\}\) with \(\mu(K)>c/s\), and \(\varphi\mu(K)\geq s\mu(K)>c\). Otherwise all these sets have finite \(\mu\)-measure. Put \(D_j=U\cap\{2^j<\varphi\leq2^{j+1}\}\) for \(j\in\mathbb Z\). These Borel sets are disjoint, cover \(U\), and have finite \(\mu\)-measure. Choose a finite set \(J\subseteq\mathbb Z\) with \(\sum_{j\in J}\varphi\mu(D_j)>c+\eta\) for some \(\eta>0\). By inner regularity on sets of finite measure (Proposition 2.3(1)), choose compact \(K_j\subseteq D_j\) with \(2^{j+1}\mu(D_j\setminus K_j)<\eta/|J|\). The compact set \(K=\bigcup_{j\in J}K_j\subseteq U\) satisfies \(\varphi\mu(K)\geq\sum_{j\in J}\big(\varphi\mu(D_j)-2^{j+1}\mu(D_j\setminus K_j)\big)>c\).
The last sentence of (2) follows from the uniqueness in the Riesz theorem 2.2.

(3) The inequality \(\geq\) is clear. For \(\leq\), let \(c<\int h\,d\mu\). The layer functions (1.1) of \(h\) have the form \(\sum_i(t_i-t_{i-1})1_{\{h>t_i\}}\) with \(t_i=i2^{-n}\), and their integrals tend to \(\int h\,d\mu\) by monotone convergence. So there is a partition \(0=t_0<t_1<\dots<t_k\) with \(\sum_i(t_i-t_{i-1})\mu(\{h>t_i\})>c\). Each set \(\{h>t_i\}\) is open, so (R3) gives compact \(K_i\subseteq\{h>t_i\}\) with \(\sum_i(t_i-t_{i-1})\mu(K_i)>c\). Choose \(K_i\prec\varphi_i\prec\{h>t_i\}\) by (T2) and put \(g=\sum_i(t_i-t_{i-1})\varphi_i\in C_c(X)\). At a point \(x\), \(\varphi_i(x)\neq0\) forces \(h(x)>t_i\), so \(g(x)\) is at most the sum of \(t_i-t_{i-1}\) over the indices \(i\) with \(t_i<h(x)\), which is less than \(h(x)\) (or is \(0\)). So \(0\leq g\leq h\) and \(\int g\,d\mu\geq\sum_i(t_i-t_{i-1})\mu(K_i)>c\).

(4) The set \(\{f\neq0\}\) is the union of the sets \(\{|f|>1/n\}\), and by Chebyshev's inequality each has measure at most \(n^p\|f\|_p^p\). So \(\{f\neq0\}\) is \(\sigma\)-finite, and Proposition 2.3(3) gives the \(\sigma\)-compact set. Simple functions are dense in \(L^p(\mu)\), and a simple function in \(L^p\) is a combination of indicators of Borel sets of finite measure. So it suffices to approximate \(1_E\) with \(\mu(E)<\infty\). Given \(\varepsilon>0\), inner regularity (Proposition 2.3(1)) and outer regularity (R2) give a compact \(K\) and an open \(U\) with \(K\subseteq E\subseteq U\) and \(\mu(U\setminus K)<\varepsilon\). Take \(K\prec f\prec U\). Then \(|f-1_E|\leq1_{U\setminus K}\), so \(\|f-1_E\|_p\leq\varepsilon^{1/p}\). \(\square\)

Part (4) needs no \(\sigma\)-finiteness of \(\mu\): an \(L^p\) function with \(p<\infty\) automatically lives on a \(\sigma\)-finite set, and there inner regularity holds. For a Haar measure (Section 8) and \(p=2\), it says that \(C_c(G)\) is dense in \(L^2(G)\). In (2) the density must be strictly positive; Exercise 16.1 shows what goes wrong with a density that vanishes on a closed set.

## 4. Products of Radon measures

Let \(X,Y\) be LCH spaces with Radon measures \(\mu,\nu\). For \(F\in C_c(X\times Y)\) write \(F_x=F(x,\cdot)\), and let \(K_F\) and \(L_F\) be the projections of \(\operatorname{supp}F\) to \(X\) and \(Y\); they are compact. The product of \(\mu\) and \(\nu\) is built from iterated integrals of such \(F\), and the first step is to approximate \(F\) by sums of products.

**Lemma 4.1** (Tensor approximation). Let \(F\in C_c(X\times Y)\).

1. The map \(x\mapsto F_x\) is continuous from \(X\) to \(C_c(Y)\) with the norm \(\|\cdot\|_{\sup}\), and \(F_x\) vanishes outside \(L_F\).
2. Let \(U\supseteq K_F\) be open with compact closure. For every \(\varepsilon>0\) there are \(\varphi_1,\dots,\varphi_n\prec U\) and \(g_1,\dots,g_n\in C_c(Y)\) vanishing outside \(L_F\) such that \(|F(x,y)-\sum_i\varphi_i(x)g_i(y)|\leq\varepsilon\) for all \((x,y)\).

**Proof.** (1) Fix \(x_0\) and \(\varepsilon>0\). For each \(y\in L_F\), continuity of \(F\) at \((x_0,y)\) gives open \(P_y\ni x_0\) and \(Q_y\ni y\) with \(|F(x,y')-F(x_0,y)|<\varepsilon/4\) on \(P_y\times Q_y\). Finitely many \(Q_{y_k}\) cover \(L_F\); let \(P=\bigcap_kP_{y_k}\). For \(x\in P\) and \(y'\in L_F\), pick \(k\) with \(y'\in Q_{y_k}\); comparing both \(F(x,y')\) and \(F(x_0,y')\) with \(F(x_0,y_k)\) gives \(|F(x,y')-F(x_0,y')|<\varepsilon/2\). Off \(L_F\) both values are \(0\).
(2) By (1), each \(x\in K_F\) has an open neighbourhood \(P_x\subseteq U\) with \(\|F_{x'}-F_x\|_{\sup}<\varepsilon\) for \(x'\in P_x\). Cover \(K_F\) by \(P_{x_1},\dots,P_{x_n}\), take a partition of unity \(\varphi_i\prec P_{x_i}\) from (T3), and let \(g_i=F_{x_i}\). Then
\[
F(x,y)-\sum_i\varphi_i(x)F(x_i,y)=\Big(1-\sum_i\varphi_i(x)\Big)F(x,y)+\sum_i\varphi_i(x)\big(F(x,y)-F(x_i,y)\big).
\]
The first term vanishes: \(\sum_i\varphi_i=1\) on \(K_F\), and \(F_x=0\) off \(K_F\). In the second, \(\varphi_i(x)\neq0\) forces \(x\in P_{x_i}\), so the term is at most \(\varepsilon\sum_i\varphi_i(x)\leq\varepsilon\) in absolute value. \(\square\)

**Proposition 4.2** (Iterated integrals). Let \(F\in C_c(X\times Y)\).

1. The function \(x\mapsto\int F(x,y)\,d\nu(y)\) is in \(C_c(X)\) and vanishes off \(K_F\); similarly with the roles of the factors exchanged.
2. The two iterated integrals agree:
\[
\int\Big(\int F(x,y)\,d\nu(y)\Big)d\mu(x)=\int\Big(\int F(x,y)\,d\mu(x)\Big)d\nu(y).
\tag{4.1}
\]
3. \(F\) is measurable for the product \(\sigma\)-algebra \(\mathcal B(X)\otimes\mathcal B(Y)\).

**Proof.** (1) \(\big|\int F(x,y)\,d\nu(y)-\int F(x_0,y)\,d\nu(y)\big|\leq\|F_x-F_{x_0}\|_{\sup}\,\nu(L_F)\), which tends to \(0\) as \(x\to x_0\) by Lemma 4.1(1). (2) Choose an open \(U\supseteq K_F\) with compact closure by (T1). For a sum \(F'=\sum_i\varphi_i\otimes g_i\) as in Lemma 4.1(2), both sides equal \(\sum_i\int\varphi_i\,d\mu\int g_i\,d\nu\). All these functions vanish outside the compact set \(\overline U\times L_F\), and \(|F-F'|\leq\varepsilon\), so each side of (4.1) for \(F\) differs from the same side for \(F'\) by at most \(\varepsilon\,\mu(\overline U)\,\nu(L_F)\). Let \(\varepsilon\to0\). (3) The approximants are \(\mathcal B(X)\otimes\mathcal B(Y)\)-measurable, and \(F\) is their pointwise limit as \(\varepsilon=1/m\to0\). \(\square\)

**Definition 4.3** (Radon product). The *Radon product* \(\mu\hat\times\nu\) is the Radon measure on \(X\times Y\) that the Riesz theorem 2.2 gives for the positive linear functional \(F\mapsto\int\big(\int F(x,y)\,d\nu(y)\big)d\mu(x)\) on \(C_c(X\times Y)\). By (4.1) it also represents the other iterated integral.

**Proposition 4.4** (Rectangles). For open \(U\subseteq X\), \(V\subseteq Y\) and compact \(K\subseteq X\), \(L\subseteq Y\), with the convention \(0\cdot\infty=0\),
\[
(\mu\hat\times\nu)(U\times V)=\mu(U)\,\nu(V),\qquad(\mu\hat\times\nu)(K\times L)=\mu(K)\,\nu(L).
\tag{4.2}
\]

**Proof.** If \(F\prec U\times V\), then \(x\mapsto\int F(x,y)\,d\nu(y)\) vanishes off \(U\) and is at most \(\nu(V)\), so \(\int F\,d(\mu\hat\times\nu)\leq\mu(U)\nu(V)\); when \(\mu(U)=0\) the integral is \(0\). If \(f\prec U\) and \(g\prec V\), then \(f\otimes g\prec U\times V\) and its integral is \(\int f\,d\mu\int g\,d\nu\). Taking suprema and using (2.1) for \(\mu\), \(\nu\) and \(\mu\hat\times\nu\) gives the first formula. For the second, if \(F\in C_c(X\times Y)\) and \(1_{K\times L}\leq F\), then \(\int F(x,y)\,d\nu(y)\geq\nu(L)1_K(x)\), so \(\int F\,d(\mu\hat\times\nu)\geq\mu(K)\nu(L)\). If \(1_K\leq f\) and \(1_L\leq g\), then \(1_{K\times L}\leq f\otimes g\), whose integral is \(\int f\,d\mu\int g\,d\nu\). Taking infima and using (2.1) gives the second formula. \(\square\)

## 5. Tonelli's and Fubini's theorems for Radon products

Let \(X,Y\) be LCH spaces with Radon measures \(\mu,\nu\), and let \(\pi=\mu\hat\times\nu\) be their Radon product (Definition 4.3). For \(E\subseteq X\times Y\) put \(E_x=\{y:(x,y)\in E\}\) and \(E^y=\{x:(x,y)\in E\}\); if \(E\) is Borel, so are all sections, because \(y\mapsto(x,y)\) is continuous. A function on \(X\) is *\(\mu\)-a.e. Borel* if it agrees with a Borel function outside a Borel \(\mu\)-null set; its integral is that of the Borel function.

**Theorem 5.1.** Everything below also holds with the roles of \(X\) and \(Y\) exchanged, since \(\pi\) represents both iterated integrals (4.1).

1. For every open \(W\subseteq X\times Y\), the function \(x\mapsto\nu(W_x)\) is lsc and \(\pi(W)=\int\nu(W_x)\,d\mu(x)\).
2. For every compact \(C\subseteq X\times Y\), the function \(x\mapsto\nu(C_x)\) is Borel and \(\pi(C)=\int\nu(C_x)\,d\mu(x)\).
3. For every Borel \(E\) with \(\pi(E)<\infty\), the function \(x\mapsto\nu(E_x)\) is \(\mu\)-a.e. Borel and \(\pi(E)=\int\nu(E_x)\,d\mu(x)\). If \(\pi(E)=0\), then \(\nu(E_x)=0\) for \(\mu\)-almost every \(x\).
4. (*Tonelli*) Let \(F\colon X\times Y\to[0,\infty]\) be Borel and vanish outside a set that is \(\sigma\)-finite for \(\pi\). Then \(x\mapsto\int F(x,y)\,d\nu(y)\) is \(\mu\)-a.e. Borel, \(y\mapsto\int F(x,y)\,d\mu(x)\) is \(\nu\)-a.e. Borel, and
\[
\int F\,d\pi=\int\Big(\int F(x,y)\,d\nu(y)\Big)d\mu(x)=\int\Big(\int F(x,y)\,d\mu(x)\Big)d\nu(y).
\tag{5.1}
\]
5. (*Fubini*) Let \(F\in L^1(\pi)\). Then \(F(x,\cdot)\in L^1(\nu)\) for \(\mu\)-almost every \(x\), the \(\mu\)-a.e. defined function \(x\mapsto\int F(x,y)\,d\nu(y)\) is \(\mu\)-integrable, and (5.1) holds.
6. (*Rectangles*) Let \(A\subseteq X\) and \(B\subseteq Y\) be Borel and \(\sigma\)-finite for \(\mu\) and \(\nu\). Then \(A\times B\) is \(\sigma\)-finite for \(\pi\), and \(\pi(A\times B)=\mu(A)\nu(B)\) with \(0\cdot\infty=0\). In particular \(A\times B\) is \(\pi\)-null when \(A\) is \(\mu\)-null.
7. If \(X\) and \(Y\) are \(\sigma\)-compact, \(\pi(E)=\int\nu(E_x)\,d\mu(x)\) for every \(E\in\mathcal B(X)\otimes\mathcal B(Y)\), so \(\pi\) extends the usual product measure. If \(X\) and \(Y\) are second countable, then \(\mathcal B(X\times Y)=\mathcal B(X)\otimes\mathcal B(Y)\).

*Scope warning:* Functions vanishing outside a \(\sigma\)-compact set meet the support hypothesis, but (4) and (5) need only a \(\sigma\)-finite set. Omitting this hypothesis and requiring a product measure that is inner and outer regular on every Borel set would be incorrect; Example 13.5 shows that no such product measure exists on \(\mathbb R_d\times\mathbb R\).

**Proof.** (1) *Lower semicontinuity.* Let \(c<\nu(W_{x_0})\). The section \(W_{x_0}\) is open, so (R3) gives a compact \(L\subseteq W_{x_0}\) with \(\nu(L)>c\). By the tube lemma (T4) applied to \(\{x_0\}\times L\subseteq W\), there is an open \(P\ni x_0\) with \(P\times L\subseteq W\). For \(x\in P\), \(L\subseteq W_x\), so \(\nu(W_x)>c\).
*The inequality \(\leq\).* If \(F\prec W\), then \(\int F(x,y)\,d\nu(y)\leq\nu(W_x)\), and integrating gives \(\int F\,d\pi\leq\int\nu(W_x)\,d\mu(x)\). Take the supremum over \(F\) and use (2.1).
*The inequality \(\geq\).* Put \(h(x)=\nu(W_x)\) and let \(c<\int h\,d\mu\). By (3.1) choose \(g\in C_c(X)\) with \(0\leq g\leq h\) and \(\int g\,d\mu>c\). Let \(K=\operatorname{supp}g\), and choose \(\eta>0\) with \(\int g\,d\mu-\eta\,\mu(K)>c\). For each \(x\in K\), (R3) gives a compact \(L_x\subseteq W_x\) with \(\nu(L_x)\geq g(x)-\eta/2\) (empty if \(g(x)\leq\eta/2\)). By (T4) there are open \(P_x\ni x\) and \(Q_x\supseteq L_x\) with \(P_x\times Q_x\subseteq W\); shrinking \(P_x\), we may also assume \(g<g(x)+\eta/2\) on \(P_x\). Cover \(K\) by \(P_{x_1},\dots,P_{x_n}\), take a partition of unity \(\alpha_i\prec P_{x_i}\) with \(\sum_i\alpha_i=1\) on \(K\) (T3), and \(L_{x_i}\prec\beta_i\prec Q_{x_i}\) (T2). The function \(F=\sum_i\alpha_i\otimes\beta_i\) satisfies \(0\leq F\leq1\) and \(\operatorname{supp}F\subseteq\bigcup_i P_{x_i}\times Q_{x_i}\subseteq W\), so \(F\prec W\). For \(x\in K\),
\[
\int F(x,y)\,d\nu(y)=\sum_i\alpha_i(x)\int\beta_i\,d\nu\geq\sum_i\alpha_i(x)\,\nu(L_{x_i})\geq g(x)-\eta ,
\]
because \(\alpha_i(x)\neq0\) forces \(x\in P_{x_i}\), and then \(\nu(L_{x_i})\geq g(x_i)-\eta/2>g(x)-\eta\). Hence \(\pi(W)\geq\int F\,d\pi\geq\int_K(g-\eta)\,d\mu>c\).
(2) Let \(K\) and \(L\) be the projections of \(C\). By (T1) choose open \(U\supseteq K\) and \(V\supseteq L\) with compact closures, and put \(W=U\times V\). Then \(\nu(W_x)=1_U(x)\nu(V)<\infty\), \(\pi(W)=\mu(U)\nu(V)<\infty\) by (4.2), and \(W\setminus C\) is open. So \(\nu(C_x)=\nu(W_x)-\nu((W\setminus C)_x)\) is a difference of finite lsc functions, hence Borel, and by (1), \(\pi(C)=\pi(W)-\pi(W\setminus C)=\int\nu(C_x)\,d\mu(x)\).
(3) By outer regularity (R2) and inner regularity on sets of finite measure (Proposition 2.3(1)), choose open \(W_n\supseteq E\) and compact \(C_n\subseteq E\) with \(\pi(W_n)<\pi(E)+1/n\) and \(\pi(C_n)>\pi(E)-1/n\). Replacing \(W_n\) by \(W_1\cap\dots\cap W_n\) and \(C_n\) by \(C_1\cup\dots\cup C_n\), we may assume \(W_n\) decreases and \(C_n\) increases. Let \(a(x)=\lim_n\nu((W_n)_x)\) and \(b(x)=\lim_n\nu((C_n)_x)\); both are Borel, and \(b(x)\leq\nu(E_x)\leq a(x)\). By (1), \(\int\nu((W_1)_x)\,d\mu=\pi(W_1)<\infty\). Its infinite-value set is therefore Borel and null; define all section bounds as zero on that exceptional set before taking differences. Dominated convergence now gives \(\int a\,d\mu=\lim\pi(W_n)=\pi(E)\). By (2) and monotone convergence, \(\int b\,d\mu=\lim\pi(C_n)=\pi(E)\). The finite-a.e. nonnegative difference \(a-b\) has integral zero, so \(a=b\) outside a Borel \(\mu\)-null set, and there \(\nu(E_x)=b(x)\). If \(\pi(E)=0\), then \(\int b\,d\mu=0\), so \(b=0\) almost everywhere.
(4) By (3), (5.1) holds for \(F=1_E\) when \(\pi(E)<\infty\). If \(E\) is \(\sigma\)-finite, write it as an increasing union of Borel sets of finite measure and use monotone convergence on all three terms; countably many null sets have a null union. By linearity (5.1) holds for nonnegative simple Borel functions vanishing outside a \(\sigma\)-finite set. For general \(F\), the layer functions (1.1) of \(F\) are such simple functions and increase to \(F\); apply monotone convergence again.
(5) Split \(F\) into the four nonnegative functions \((\operatorname{Re}F)^\pm\) and \((\operatorname{Im}F)^\pm\), and apply (4) to each. They vanish outside \(\{F\neq0\}\), which is \(\sigma\)-finite by Proposition 3.1(4), and their iterated integrals are finite, so their inner integrals are finite almost everywhere. Subtract.
(6) By Proposition 2.3(3), write \(A=S_A\cup N_A\) and \(B=S_B\cup N_B\) with \(S_A,S_B\) \(\sigma\)-compact and \(N_A,N_B\) null. For compact \(L\subseteq Y\) and \(\varepsilon>0\), choose an open \(U\supseteq N_A\) with \(\mu(U)<\varepsilon\) and an open \(V\supseteq L\) with compact closure; by (4.2), \(\pi(N_A\times L)\leq\mu(U)\nu(V)\leq\varepsilon\,\nu(\overline V)\). So \(N_A\times L\) is null, and so is \(N_A\times S_B\). Choosing also an open \(V'\supseteq N_B\) with \(\nu(V')<\varepsilon\), we get \(\pi(N_A\times N_B)\leq\mu(U)\nu(V')<\varepsilon^2\). In the same way \(S_A\times N_B\) is null. So \(A\times B\) differs from the \(\sigma\)-compact set \(S_A\times S_B\) by a null set, and it is \(\sigma\)-finite by (R1). Now (4) with \(F=1_{A\times B}\) gives \(\pi(A\times B)=\int1_A(x)\nu(B)\,d\mu(x)=\mu(A)\nu(B)\).
(7) If \(X\) and \(Y\) are \(\sigma\)-compact, so is \(X\times Y\), and every Borel set is \(\sigma\)-finite by (R1); apply (4) to \(1_E\), noting \(\mathcal B(X)\otimes\mathcal B(Y)\subseteq\mathcal B(X\times Y)\) because the projections are continuous. For \(E\) in the product \(\sigma\)-algebra, \(\int\nu(E_x)\,d\mu(x)\) is the usual product measure of \(\sigma\)-finite factors. If \(X\) and \(Y\) have countable bases, every open \(W\subseteq X\times Y\) is the union of the countably many products of basic sets contained in \(W\), so \(W\in\mathcal B(X)\otimes\mathcal B(Y)\). \(\square\)

*Where the hypotheses enter, and why they are needed.* Parts (1)–(3) use only the Radon properties. \(\sigma\)-finiteness enters in (4)–(6), and it cannot be dropped. Example 13.5 gives a closed set in \(\mathbb R_d\times\mathbb R\) whose two iterated integrals are \(0\) and \(\infty\), and Example 13.6 gives a set \(\{e\}\times G\) with \(\pi(\{e\}\times G)=\infty\) although \(\mu(\{e\})=0\). In particular, (4) applies to every Borel \(F\geq0\) that vanishes outside a \(\sigma\)-compact set, since \(\sigma\)-compact sets are \(\sigma\)-finite by (R1).

**Example 5.2** (Borel sets of products). If \(X\) and \(Y\) are second countable, \(\mathcal B(X\times Y)=\mathcal B(X)\otimes\mathcal B(Y)\) (Theorem 5.1(7)). Without second countability this fails even for discrete groups. Let \(G\) be a discrete group of cardinality greater than \(2^{\aleph_0}\), for instance a free abelian group on such a set. The diagonal \(\Delta_G\subseteq G\times G\) is open, but it is not in \(\mathcal B(G)\otimes\mathcal B(G)\), which here is the \(\sigma\)-algebra generated by all rectangles. Proof: a set in the \(\sigma\)-algebra generated by a family \(\mathcal C\) lies in the \(\sigma\)-algebra generated by some countable subfamily, because the sets with this property form a \(\sigma\)-algebra containing \(\mathcal C\). So \(\Delta_G\) lies in the \(\sigma\)-algebra generated by countably many rectangles \(A_n\times B_n\). Put \(\varphi(x)=(1_{A_n}(x))_n\) and \(\psi(y)=(1_{B_n}(y))_n\) in \(\{0,1\}^{\mathbb N}\). The sets \((\varphi\times\psi)^{-1}(S)\), \(S\subseteq\{0,1\}^{\mathbb N}\times\{0,1\}^{\mathbb N}\), form a \(\sigma\)-algebra containing each \(A_n\times B_n\), so \(\Delta_G=(\varphi\times\psi)^{-1}(S)\) for some \(S\). If \(\varphi(x)=\varphi(x')\), then \((x,x')\in\Delta_G\) because \((\varphi(x),\psi(x'))=(\varphi(x'),\psi(x'))\in S\); so \(x=x'\). Hence \(\varphi\) is injective and \(|G|\leq2^{\aleph_0}\), a contradiction. So the Radon product (here counting measure on \(G\times G\)) lives on a \(\sigma\)-algebra strictly larger than the product \(\sigma\)-algebra. This is why Theorem 5.1 and Theorem 6.2 are proved for Borel functions on \(X\times Y\), not only for product-measurable ones.

## 6. Hilbert tensor products and L² of a product

*Hilbert tensor products.* For Hilbert spaces \(H,K\), \(H\otimes K\) is the Hilbert tensor product of [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators), Theorem 8.1. It carries a bilinear map \((\xi,\eta)\mapsto\xi\otimes\eta\) with \(\langle\xi\otimes\eta,\xi'\otimes\eta'\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle\), and the elementary tensors span a dense subspace.

**Lemma 6.1** (Isometric extension). Suppose \(B\colon H\times K\to\mathcal K\) is bilinear, where \(\mathcal K\) is a third Hilbert space, and \(\langle B(\xi,\eta),B(\xi',\eta')\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle\). There is a unique isometry \(U\colon H\otimes K\to\mathcal K\) with \(U(\xi\otimes\eta)=B(\xi,\eta)\).

**Proof.** For finite sums, \(\|\sum_iB(\xi_i,\eta_i)\|^2=\sum_{i,j}\langle\xi_i,\xi_j\rangle\langle\eta_i,\eta_j\rangle=\|\sum_i\xi_i\otimes\eta_i\|^2\). So \(\sum_i\xi_i\otimes\eta_i\mapsto\sum_iB(\xi_i,\eta_i)\) is well defined (a sum of tensors that is \(0\) goes to a vector of norm \(0\)) and isometric on the span of the elementary tensors. It extends by continuity to the closure, which is \(H\otimes K\). Uniqueness holds because the elementary tensors are total. \(\square\)

**Theorem 6.2** (\(L^2\) of the Radon product). Let \(\mu,\nu\) be Radon measures on LCH spaces \(X,Y\), and \(\pi=\mu\hat\times\nu\). For functions \(\xi\) on \(X\) and \(\eta\) on \(Y\) write \((\xi\boxtimes\eta)(x,y)=\xi(x)\eta(y)\).

1. For \(\xi\in L^2(\mu)\) and \(\eta\in L^2(\nu)\), \(\xi\boxtimes\eta\in L^2(\pi)\); its class depends only on the classes of \(\xi\) and \(\eta\); and \(\langle\xi\boxtimes\eta,\xi'\boxtimes\eta'\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle\).
2. There is a unique unitary \(U\colon L^2(\mu)\otimes L^2(\nu)\to L^2(\pi)\) with \(U(\xi\otimes\eta)=\xi\boxtimes\eta\).
3. Every \(\zeta\in L^2(\pi)\) satisfies \(\zeta(x,\cdot)\in L^2(\nu)\) for \(\mu\)-almost every \(x\), and \(\|\zeta\|^2=\int\|\zeta(x,\cdot)\|_{L^2(\nu)}^2\,d\mu(x)\); likewise in the other variable.
4. For a bounded Borel function \(a\) on \(X\), the operator \(U^*M_{a\circ\mathrm{pr}_1}U\), where \(M\) denotes multiplication on \(L^2(\pi)\), is the unique bounded operator on \(L^2(\mu)\otimes L^2(\nu)\) that sends every \(\xi\otimes\eta\) to \((a\xi)\otimes\eta\). It is the operator \(m_a\otimes1\). The same holds for the second factor.

**Proof.** (1) Take Borel representatives. The sets \(S_\xi=\{\xi\neq0\}\) and \(S_\eta=\{\eta\neq0\}\) are \(\sigma\)-finite by Proposition 3.1(4). The function \(\xi\boxtimes\eta\) is Borel on \(X\times Y\) and vanishes outside \(S_\xi\times S_\eta\), which is \(\sigma\)-finite by Theorem 5.1(6). Tonelli's theorem 5.1(4) gives \(\int|\xi\boxtimes\eta|^2\,d\pi=\|\xi\|^2\|\eta\|^2\). If \(\xi=\xi'\) outside a \(\mu\)-null Borel set \(N\), then \(\xi\boxtimes\eta=\xi'\boxtimes\eta\) outside \(N\times S_\eta\), which is \(\pi\)-null by Theorem 5.1(6); similarly in the second variable. The function \((\xi\bar\xi')\boxtimes(\eta\bar\eta')\) is in \(L^1(\pi)\) by the Cauchy–Schwarz inequality, and Fubini's theorem 5.1(5) gives the inner product formula.
(2) Lemma 6.1, with \(B(\xi,\eta)=\xi\boxtimes\eta\), gives the isometry \(U\). Its range is closed, because \(U\) is an isometry on a complete space, and it contains \(\varphi\boxtimes g\) for \(\varphi\in C_c(X)\) and \(g\in C_c(Y)\). These span a dense subspace of \(L^2(\pi)\). Indeed, let \(\zeta\in L^2(\pi)\) and \(\varepsilon>0\). Since \(C_c\) is dense in \(L^2\) (Proposition 3.1(4)), there is \(F\in C_c(X\times Y)\) with \(\|\zeta-F\|_2<\varepsilon\). Choose an open \(O\supseteq K_F\) with compact closure (T1). The tensor approximation (Lemma 4.1(2)), applied with \(O\), gives \(F'=\sum_i\varphi_i\boxtimes g_i\) with \(|F-F'|\leq\delta\), where \(F\) and \(F'\) vanish outside the compact set \(\overline O\times L_F\). Then \(\|F-F'\|_2\leq\delta\,\pi(\overline O\times L_F)^{1/2}=\delta\,(\mu(\overline O)\nu(L_F))^{1/2}\) by (4.2), which is less than \(\varepsilon\) for small \(\delta\). So \(U\) is onto. Uniqueness holds because elementary tensors are total.
(3) Apply Tonelli's theorem 5.1(4) to \(|\zeta|^2\). It vanishes outside the set \(\{\zeta\neq0\}\), which is \(\sigma\)-finite by Proposition 3.1(4) applied to \(\pi\).
(4) \(M_{a\circ\mathrm{pr}_1}(\xi\boxtimes\eta)=(a\xi)\boxtimes\eta\), so \(U^*M_{a\circ\mathrm{pr}_1}U(\xi\otimes\eta)=(a\xi)\otimes\eta\). Two bounded operators that agree on a total set are equal. \(\square\)

In words: **\(L^2(\mu)\otimes L^2(\nu)\cong L^2(X\times Y,\mu\hat\times\nu)\) through \(\xi\otimes\eta\mapsto\xi\boxtimes\eta\), for arbitrary Radon measures, with the Radon product and not the ordinary product measure.** Every element of \(L^2(\pi)\) has \(\sigma\)-finite support, so the pathological sets of Examples 13.5 and 13.6 never carry \(L^2\) mass.

## 7. Topological groups

**Proposition 7.1.** Let \(G\) be a group, topologized so that multiplication \(G\times G\to G\) and inversion are continuous. The Hausdorff property is not assumed in this proposition.

1. Left and right translations and inversion are homeomorphisms of \(G\). If \(U\) is open and \(A\subseteq G\) is any set, then \(AU\) and \(UA\) are open.
2. Every neighbourhood \(U\) of \(e\) contains a neighbourhood \(V\) of \(e\) with \(V=V^{-1}\) and \(VV\subseteq U\).
3. The closure of a subgroup is a subgroup. An open subgroup is closed.
4. If \(A\) and \(B\) are compact, so is \(AB\).
5. Let \(H\) be a subgroup, \(G/H\) the set of left cosets with the quotient topology, and \(q\colon G\to G/H\) the quotient map. Then \(q\) is open. If \(H\) is closed, \(G/H\) is Hausdorff. If \(G\) is locally compact, every point of \(G/H\) has a compact neighbourhood. If \(H\) is normal, \(G/H\) is a group with continuous multiplication and inversion.
6. If \(\{e\}\) is closed, \(G\) is Hausdorff. In general \(N=\overline{\{e\}}\) is a normal subgroup as well as closed, and \(G/N\) is Hausdorff.

**Proof.** (1) Translation by \(x\) has the continuous inverse translation by \(x^{-1}\), and inversion is its own inverse. Also \(AU=\bigcup_{a\in A}aU\), and each \(aU\) is open.
(2) Continuity of multiplication at \((e,e)\) gives neighbourhoods \(W_1,W_2\) of \(e\) with \(W_1W_2\subseteq U\). Put \(W=W_1\cap W_2\) and \(V=W\cap W^{-1}\).
(3) The continuous map \((x,y)\mapsto xy^{-1}\) sends \(H\times H\) into \(H\), hence sends \(\overline H\times\overline H=\overline{H\times H}\) into \(\overline H\). If \(H\) is open, its complement is a union of cosets \(xH\), which are open by (1).
(4) Multiplication is continuous and maps the compact set \(A\times B\) onto \(AB\).
(5) For open \(V\subseteq G\), \(q^{-1}(q(V))=VH\) is open by (1), so \(q(V)\) is open. Let \(H\) be closed and \(y\notin xH\). The coset \(xH\) is closed, so some neighbourhood \(U\) of \(e\) has \(Uy\cap xH=\varnothing\); by (2) take \(V\) symmetric with \(VV\subseteq U\). If \(q(Vx)\) and \(q(Vy)\) met, we would have \(v_1xh_1=v_2yh_2\) with \(v_i\in V\) and \(h_i\in H\), so \(v_1^{-1}v_2\,y=xh_1h_2^{-1}\in xH\) with \(v_1^{-1}v_2\in VV\subseteq U\), which is impossible. So \(q(Vx)\) and \(q(Vy)\) are disjoint neighbourhoods of \(xH\) and \(yH\) (\(q\) is open). If \(C\) is a compact neighbourhood of \(e\) in \(G\), then \(q(xC)\) is compact and contains the open set \(q(x\operatorname{int}C)\ni xH\). If \(H\) is normal and \(W\) is an open neighbourhood of \(q(xy)\), continuity of multiplication in \(G\) gives open \(V_1\ni x\) and \(V_2\ni y\) with \(V_1V_2\subseteq q^{-1}(W)\), so \(q(V_1)q(V_2)\subseteq W\) with \(q(V_i)\) open. Inversion is handled the same way.
(6) If \(\{e\}\) is closed, apply (5) with \(H=\{e\}\). In general \(N\) is a subgroup by (3), and it lies in every closed subgroup. For \(z\in G\), \(zNz^{-1}\) is a closed subgroup (conjugation is a homeomorphism and an automorphism), so it contains \(N\). Applying this to \(z^{-1}\) gives \(zNz^{-1}=N\). Now apply (5) with \(H=N\). \(\square\)

By (6), dividing by \(\overline{\{e\}}\) removes any failure of the Hausdorff property, which is why we may assume it throughout.

From now on \(G\) is a locally compact group. Two more facts are needed: \(G\) splits into \(\sigma\)-compact pieces, and compactly supported continuous functions are uniformly continuous.

**Proposition 7.2** (An open \(\sigma\)-compact subgroup). Some subgroup \(G_0\) of \(G\) is at once open, closed and \(\sigma\)-compact. Its left cosets \(xG_0\) partition \(G\) into open, closed, \(\sigma\)-compact pieces.

**Proof.** Let \(C\) be a compact neighbourhood of \(e\) and \(U=C\cap C^{-1}\), a compact symmetric neighbourhood of \(e\). The sets \(U^n=U\cdots U\) (\(n\) factors) are compact by Proposition 7.1(4), and \(G_0=\bigcup_nU^n\) is the subgroup generated by \(U\). It contains the neighbourhood \(xU\) of each of its points \(x\), since \(xU\subseteq U^{n+1}\) when \(x\in U^n\). So it is open, hence closed by Proposition 7.1(3), and it is \(\sigma\)-compact. If \(G\) is connected, the open and closed subgroup \(G_0\) is all of \(G\), so every connected locally compact group is \(\sigma\)-compact. \(\square\)

**Proposition 7.3** (Uniform continuity). For every \(f\in C_c(G)\), \(\|R_yf-f\|_{\sup}\to0\) and \(\|L_yf-f\|_{\sup}\to0\) as \(y\to e\).

**Proof.** Let \(K=\operatorname{supp}f\) and \(\varepsilon>0\). For \(x\in K\) choose a neighbourhood \(U_x\) of \(e\) with \(|f(xz)-f(x)|<\varepsilon/2\) for \(z\in U_x\), and a symmetric neighbourhood \(V_x\) with \(V_xV_x\subseteq U_x\); note \(V_x\subseteq U_x\). Finitely many sets \(x_jV_{x_j}\) cover \(K\); let \(V=\bigcap_jV_{x_j}\), a symmetric neighbourhood of \(e\). Let \(y\in V\). If \(x\in K\), write \(x=x_ju\) with \(u\in V_{x_j}\). Then \(xy=x_j(uy)\) with \(uy\in V_{x_j}V_{x_j}\subseteq U_{x_j}\), so \(f(xy)\) and \(f(x)\) are both within \(\varepsilon/2\) of \(f(x_j)\), and \(|f(xy)-f(x)|<\varepsilon\). If \(xy\in K\), the same argument applied to the point \(xy\) and to \(y^{-1}\in V\) gives \(|f(x)-f(xy)|<\varepsilon\). Otherwise both values are \(0\). So \(\|R_yf-f\|_{\sup}\leq\varepsilon\) for \(y\in V\). For left translations, \(L_yf(x)=\check f(x^{-1}y)=R_y\check f(x^{-1})\), so \(\|L_yf-f\|_{\sup}=\|R_y\check f-\check f\|_{\sup}\) with \(\check f\in C_c(G)\). \(\square\)

Proposition 7.3 underlies the continuity of translation in \(L^p\) (Theorem 14.2(6)), and with it the strong continuity of the regular representations (Exercise 16.3). A bounded function \(f\) with \(\|L_yf-f\|_{\sup}\to0\) as \(y\to e\) is called *left uniformly continuous*, and one with \(\|R_yf-f\|_{\sup}\to0\) *right uniformly continuous*. The two names are also used the other way round, so this lesson always writes the condition out.

## 8. Existence of Haar measure

**Definition 8.1.** Fix a locally compact group \(G\). We call a Radon measure \(\mu\neq0\) on \(G\) a *left* (*right*) *Haar measure* when \(\mu(xE)=\mu(E)\) (\(\mu(Ex)=\mu(E)\)) for every Borel set \(E\) and every \(x\in G\). A *left Haar integral* is a left-invariant positive linear functional \(I\neq0\) on \(C_c(G)\), that is, \(I(L_yf)=I(f)\) for all \(f\) and \(y\).

**Proposition 8.2** (Invariance through integrals). Fix a Radon measure \(\mu\) on \(G\).

1. \(\mu\) is a left Haar measure exactly when \(\tilde\mu(E)=\mu(E^{-1})\) is a right Haar measure.
2. \(\mu(yE)=\mu(E)\) for all Borel \(E\) and all \(y\) exactly when \(\int L_yf\,d\mu=\int f\,d\mu\) for all \(f\in C_c(G)\) and all \(y\). In that case \(\int f(yx)\,d\mu(x)=\int f\,d\mu\) for all \(y\), all Borel \(f\geq0\), and all \(f\in L^1(\mu)\).

So, through the Riesz theorem 2.2, left Haar measures and left Haar integrals are the same objects.

**Proof.** (1) Inversion \(\iota\) is a homeomorphism, so \(\tilde\mu=\iota_*\mu\) is Radon by Proposition 3.1(1). Also \(\tilde\mu(Ex)=\mu(x^{-1}E^{-1})\), and this equals \(\tilde\mu(E)=\mu(E^{-1})\) for all \(E\) and \(x\) exactly when \(\mu\) is left invariant. (2) Let \(\ell_z(x)=zx\) and \(\mu_y=(\ell_{y^{-1}})_*\mu\), so \(\mu_y(E)=\mu(yE)\). By Proposition 3.1(1), \(\mu_y\) is Radon and \(\int f\,d\mu_y=\int f(y^{-1}x)\,d\mu(x)=\int L_yf\,d\mu\). If \(\int L_yf\,d\mu=\int f\,d\mu\) on \(C_c(G)\), the Radon measures \(\mu_y\) and \(\mu\) agree by the uniqueness in Theorem 2.2. The converse and the last sentence follow from the same integral formula, applied to \(y^{-1}\). \(\square\)

**Theorem 8.3** (Existence). Every locally compact Hausdorff group has a left Haar measure. It also has a right Haar measure.

*Free source and terms.* The compact-set covering construction below adapts the freely accessible proof of [Fremlin, §§441C(b–f), 441E](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt441.tex). Copyright © 1998 D. H. Fremlin; adaptation and expanded proofs by GPT-6.1 Sol (OpenAI), Ultra, 5 October 2026. This replacement is separately distributed under the [Design Science License](licenses/design-science-license.txt), with editable Markdown source. It replaces the source's measure-conversion invocation by the complete Borel construction in Lemma 8.4. The compact normalization and open-envelope viewpoint are also compared with [F. van Doorn, *Formalized Haar Measure*, existence section](https://arxiv.org/abs/2102.07636v1). No formal verification of this proof is claimed.

The proof uses only the already proved topology facts (T1), compactness of finite products, and Tychonoff's theorem, together with the preceding tools lesson's Carathéodory theorem. In particular it uses neither Haar uniqueness nor a modular function. We first prove exactly the conversion of compact-set data that is needed.

**Lemma 8.4** (From a compact content to a Borel Radon measure). Let \(X\) be LCH. Suppose \(c\) assigns a finite nonnegative real number to every compact subset of \(X\), with the following properties:
\[
c(\varnothing)=0,\qquad
K\subset L\Longrightarrow c(K)\leq c(L),\qquad
c(K\cup L)\leq c(K)+c(L),
\]
and \(c(K\cup L)=c(K)+c(L)\) when \(K\cap L=\varnothing\).
For open \(O\subset X\) and arbitrary \(A\subset X\), define
\[
m(O)=\sup\{c(K):K\subset O,\ K\text{ compact}\},\qquad
m^*(A)=\inf\{m(O):A\subset O,\ O\text{ open}\}.
\tag{8.3}
\]
Then \(m^*\) is an outer measure and every Borel set is \(m^*\)-measurable. Its Borel restriction \(\mu\) is finite on compact sets, outer regular on all Borel sets and inner regular on open sets. Moreover
\[
\mu(O)=m(O)\quad(O\text{ open}),\qquad
c(K)\leq\mu(K)\quad(K\text{ compact}).
\]
If a homeomorphism \(\theta\) of \(X\) satisfies \(c(\theta K)=c(K)\) for every compact \(K\), then \(\mu(\theta E)=\mu(E)\) for every Borel \(E\).

*Proof.* First record a compact decomposition consequence of (T1). If a compact \(K\) is covered by finitely many open sets \(O_1,\ldots,O_r\), choose, for each \(x\in K\), an index \(i(x)\) and an open neighborhood \(V_x\) such that
\[
x\in V_x\subset\overline{V_x}\subset O_{i(x)},\qquad
\overline{V_x}\text{ compact}.
\]
Finitely many \(V_{x_j}\) cover \(K\). For each \(i\), let
\[
K_i=K\cap\bigcup_{\{j:i(x_j)=i\}}\overline{V_{x_j}},
\]
using the empty set when no \(j\) has that index. These are compact, \(K_i\subset O_i\), and \(K=\bigcup_{i=1}^r K_i\).

The functions \(m,m^*\) are monotone and zero at the empty set. Also \(m^*(O)=m(O)\) for open \(O\): every open superset has at least its \(m\)-value, and \(O\) itself is an admissible superset. If \(O=\bigcup_{n\geq1}O_n\) is a union of open sets, each compact \(K\subset O\) is covered by finitely many of them. Use the compact decomposition just proved, and repeat the two-set subadditivity of \(c\), to obtain
\[
c(K)\leq\sum_{n\geq1}m(O_n).
\]
Taking the supremum over \(K\) proves countable subadditivity of \(m\) on open unions. To obtain it for \(m^*\), it suffices to consider sets \(A_n\) with \(\sum_n m^*(A_n)<\infty\). For \(\varepsilon>0\), choose open \(O_n\supset A_n\) with
\(m(O_n)<m^*(A_n)+\varepsilon2^{-n}\). Their union gives
\[
m^*\Bigl(\bigcup_n A_n\Bigr)
 \leq m\Bigl(\bigcup_n O_n\Bigr)
 \leq\sum_n m(O_n)
 \leq\sum_n m^*(A_n)+\varepsilon.
\]
Let \(\varepsilon\) decrease to zero. If the sum is infinite, the required inequality is automatic. Thus \(m^*\) is an outer measure.

We now prove measurability of every open \(O\); it is not inferred merely from the words “outer measure.” Let \(V\) be open with \(m(V)<\infty\). Choose compact \(K\subset V\cap O\) with
\[
c(K)>m(V\cap O)-\varepsilon.
\]
This is possible also when \(m(V\cap O)=0\), by taking \(K=\varnothing\). For any compact \(L\subset V\setminus K\), disjoint additivity and monotonicity give
\[
c(K)+c(L)=c(K\cup L)\leq m(V).
\]
Taking the supremum over these \(L\) yields
\[
m(V)\geq c(K)+m(V\setminus K)
 \geq m(V\cap O)-\varepsilon+m^*(V\setminus O),
\]
since \(V\setminus K\) is an open superset of \(V\setminus O\).

For arbitrary \(A\) with \(m^*(A)<\infty\), choose open \(V\supset A\) with
\(m(V)<m^*(A)+\varepsilon\), and apply the preceding inequality. Monotonicity gives
\[
m^*(A)+2\varepsilon
 \geq m^*(A\cap O)+m^*(A\setminus O).
\]
Let \(\varepsilon\) decrease to zero. Subadditivity supplies the reverse inequality. For \(m^*(A)=\infty\), the greater-than-or-equal Carathéodory inequality is automatic. The tools lesson's Theorem 1.1 therefore makes every open set measurable, and makes the measurable sets a sigma-algebra on which \(m^*\) is countably additive. It contains the Borel sigma-algebra. Let \(\mu=m^*|_{\mathcal B(X)}\).

Outer regularity on every Borel set follows from the definition of \(m^*\), because its value on an open set is \(m\). For a compact \(K\), (T1) supplies an open \(W\supset K\) with compact closure \(C\). Every compact \(L\subset W\) satisfies \(c(L)\leq c(C)\), so
\[
\mu(K)\leq m(W)\leq c(C)<\infty.
\]
For every open \(V\supset K\), \(m(V)\geq c(K)\); taking the infimum proves \(c(K)\leq\mu(K)\). Consequently, for an arbitrary open \(O\),
\[
\mu(O)=m(O)=\sup_{K\subset O}c(K)
 \leq\sup_{K\subset O}\mu(K)\leq\mu(O),
\]
where both suprema run over compact sets. This proves inner regularity on open sets, also when the value is infinite. It does not assert \(c(K)=\mu(K)\) for every compact set, or inner regularity on every Borel set.

Finally \(\theta\) maps the compact subsets of \(O\) bijectively onto the compact subsets of \(\theta O\); hence \(m(\theta O)=m(O)\). It also maps the open supersets of \(A\) bijectively onto those of \(\theta A\), so \(m^*(\theta A)=m^*(A)\) for every \(A\subset X\). Restricting to Borel sets proves the last assertion. \(\square\)

**Proof of Theorem 8.3.** Choose a compact neighborhood \(K_0\) of the identity \(e\), and choose an open identity neighborhood \(V_0\subset K_0\). Let \(\mathcal N\) be the family of relatively compact open identity neighborhoods. It is a neighborhood base by (T1); a finite intersection of its members is again a member.

For a compact \(K\) and \(U\in\mathcal N\), let
\[
(K:U)=\min\left\{n\geq0:
 K\subset\bigcup_{j=1}^n x_jU,\quad x_j\in G\right\}.
\]
The translates \(xU\) cover \(G\), and compactness gives a finite cover of \(K\). Thus the minimum exists as a nonnegative integer; it is zero precisely when \(K=\varnothing\). Directly from finite covers,
\[
K\subset L\Longrightarrow (K:U)\leq(L:U),\qquad
(K\cup L:U)\leq(K:U)+(L:U),\qquad
(aK:U)=(K:U).
\tag{8.1}
\]
The last equality follows by translating a cover by \(a\), and then using \(a^{-1}\) for the reverse inequality.

Put \(M_K=(K:V_0)\) and
\[
c_U(K)=\frac{(K:U)}{(K_0:U)}.
\]
The denominator is a positive finite integer because \(K_0\ne\varnothing\). Cover \(K\) by \(M_K\) translates of \(V_0\), and cover \(K_0\) by \((K_0:U)\) translates of \(U\). Since \(V_0\subset K_0\), the translated second covers cover every member of the first cover. Therefore
\[
0\leq c_U(K)\leq M_K,\qquad c_U(K_0)=1.
\tag{8.2}
\]
Each \(M_K\) is finite; for the empty compact set it is zero.

For disjoint compact \(K,L\), the compact set \(K^{-1}L\) does not contain \(e\) and is closed. Continuity of \((u,v)\mapsto u^{-1}v\) at \((e,e)\) supplies an identity neighborhood \(V\in\mathcal N\) such that
\[
V^{-1}V\cap K^{-1}L=\varnothing.
\]
If \(U\subset V\), no left translate \(xU\) can meet both \(K\) and \(L\): points \(k=xu\in K\), \(l=xv\in L\) would give \(k^{-1}l=u^{-1}v\) in the forbidden intersection. Split a minimal finite cover of \(K\cup L\) into the members meeting \(K\) and those meeting \(L\). The two index sets are disjoint, and each covers its indicated compact set. Hence
\[
(K\cup L:U)\geq(K:U)+(L:U).
\]
Together with (8.1), this proves equality for every sufficiently small \(U\). The claim is immediate when one of \(K,L\) is empty.

Let \(\mathcal K\) be the set of compact subsets of \(G\). The product
\[
\Omega=\prod_{K\in\mathcal K}[0,M_K]
\]
is compact Hausdorff by the earlier programme's proved Tychonoff theorem and compactness of closed bounded real intervals. Each \(c_U\) is a point of \(\Omega\). For \(V\in\mathcal N\), take the closed subset
\[
F_V=\overline{\{c_U:U\in\mathcal N,\ U\subset V\}}\subset\Omega.
\]
It is nonempty, since \(U=V\) is allowed. A finite intersection \(F_{V_1}\cap\cdots\cap F_{V_r}\) contains \(F_{V_1\cap\cdots\cap V_r}\). Compactness therefore supplies
\[
c\in\bigcap_{V\in\mathcal N}F_V:
\]
if that intersection were empty, the complements would form an open cover with a finite subcover, contradicting the preceding finite-intersection property.

For fixed finitely many compact sets, coordinate equalities and inequalities describe closed subsets of \(\Omega\). The properties in (8.1) and (8.2), holding for every \(c_U\), therefore hold for \(c\). The disjoint-additivity equality holds for every \(c_U\) with \(U\subset V\) for the \(V\) just constructed, so its closed equality set contains \(F_V\) and contains \(c\). We have obtained a finite nonnegative compact content satisfying all the hypotheses of Lemma 8.4, and in addition
\[
c(aK)=c(K),\qquad c(K_0)=1.
\]

Apply Lemma 8.4 to this \(c\). Left translation is a homeomorphism and preserves \(c\), so the resulting Borel Radon measure \(\mu\) satisfies
\(\mu(aE)=\mu(E)\) for every \(a\in G\) and Borel \(E\). Moreover
\[
1=c(K_0)\leq\mu(K_0)<\infty,
\]
so it is nonzero. Thus it is a left Haar measure in the exact convention of this lesson.

This construction also proves positivity on every nonempty open set. Given such an \(O\), choose a nonempty compact \(K\subset O\) with nonempty interior, using (T1). Finitely many left translates of \(\operatorname{int}K\) cover \(K_0\), say \(K_0\subset\bigcup_{j=1}^n a_jK\), with \(n\geq1\). Compact-content monotonicity, finite subadditivity and invariance give
\[
1=c(K_0)\leq\sum_{j=1}^n c(a_jK)=nc(K).
\]
Hence \(\mu(O)\geq c(K)\geq1/n>0\). No sigma-compactness or countability of the neighborhood base has entered.

Finally define \(\nu(E)=\mu(E^{-1})\) for Borel \(E\). Inversion is a homeomorphism, so this is a nonzero Radon measure: compact sets, open supersets and compact subsets of open sets correspond under inversion, preserving all three regularity properties. For \(a\in G\),
\[
\nu(Ea)=\mu((Ea)^{-1})=\mu(a^{-1}E^{-1})=\mu(E^{-1})=\nu(E).
\]
It is therefore a right Haar measure. \(\square\)

*Source correspondence.* Fremlin's §441C(b–f) supplies the finite translate-cover index, normalized bounded compact data, eventual disjoint additivity and compact limiting idea; §441E supplies the separation argument for the group action. We use a compact \(K_0\) rather than the source's relatively compact open normalization set, and use the proved Tychonoff closed-intersection argument instead of invoking an ultrafilter. Lemma 8.4 gives a full own proof of the open-envelope/Borel conversion in this course's convention, replacing Fremlin's invocation of §416M. Van Doorn's existence section separately confirms the compact normalization and compact-content/open-envelope route; its Lean links are not treated as proof bodies or as certification of this text. The normalized content need not equal the final measure on every compact set; the bounds used above suffice.

## 9. Positivity and uniqueness of Haar measure

**Proposition 9.1** (Positivity). A left Haar measure \(\mu\) satisfies \(\mu(U)>0\) for every nonempty open set \(U\), and \(\int f\,d\mu>0\) for every \(f\in C_c^+(G)\).

**Proof.** Suppose \(U\neq\varnothing\) is open and \(\mu(U)=0\). Fix \(u\in U\). For compact \(K\), the null open sets \(xu^{-1}U\), \(x\in K\), cover \(K\), and finitely many suffice; so \(\mu(K)=0\). Then \(\mu(G)=0\) by (R3), which contradicts \(\mu\neq0\). For \(f\in C_c^+(G)\), the open set \(\{f>\|f\|_{\sup}/2\}\) is nonempty, so \(\int f\,d\mu\geq\frac12\|f\|_{\sup}\,\mu(\{f>\|f\|_{\sup}/2\})>0\). \(\square\)

**Theorem 9.2** (Uniqueness). Any two left Haar measures \(\mu,\nu\) on \(G\) are proportional: \(\mu=c\nu\) for some \(c\in(0,\infty)\). Equivalently, every left Haar integral is a positive multiple of \(f\mapsto\int f\,d\mu\).

*Free source and licence.* The following complete proof adapts Fremlin’s freely accessible [Volume 4, §442B](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt442.tex) to the Radon convention of this lesson. This proof is separately distributed under the [Design Science License](licenses/design-science-license.txt). Copyright © 1998 D. H. Fremlin; adaptation and expanded compact shrinking/Borel conclusion by GPT-6.1 Sol (OpenAI), Ultra. The [source companion](supplements/fremlin-neighbourhood-uniqueness.md#haar-fremlin-neighbourhood-uniqueness) records the source edition, changes and terms.

*Proof.* By [Proposition 9.1](#oa-fnd-hm-06), each nonempty open set has positive measure for both measures. Relatively compact open sets have finite measure for both. Let \(\mathcal U\) be the symmetric relatively compact open neighborhoods of the identity, ordered by reverse inclusion. These form a neighborhood base: intersect an identity neighborhood with its inverse and with a relatively compact identity neighborhood.

Fix a nonempty relatively compact open set \(O\), and \(0<\varepsilon<1\). Inner regularity gives a compact \(K\subset O\) with
\[
\mu(K)>(1-\varepsilon)\mu(O).
\]
There are an open \(H\supset K\) and an identity neighborhood \(V\) such that \(HV\subset O\). Indeed, continuity of multiplication supplies a box \(H_x\times V_x\) whose product lies in \(O\) for each \(x\in K\); take finitely many \(H_x\) covering \(K\), their union for \(H\), and the intersection of the corresponding \(V_x\) for \(V\). Shrink \(V\) to a member of \(\mathcal U\).

For \(U\in\mathcal U\) with \(U\subset V\), put
\[
 W=\{(x,y)\in O\times O:x^{-1}y\in U\}.
\]
This is open in \(G\times G\). [Theorem 5.1(1)](#oa-fnd-hm-10) identifies the two integrals of its sections with \((\mu\widehat\times\nu)(W)\); its open-set assertion does not require sigma-finiteness. If \(x\in H\), the vertical section contains \(xU\). A horizontal section at \(y\in O\) is contained in \(yU\), since \(U=U^{-1}\). Left invariance therefore gives
\[
 (1-\varepsilon)\mu(O)\nu(U)
 <\mu(H)\nu(U)
 \le (\mu\widehat\times\nu)(W)
 \le\mu(U)\nu(O).
\]
All the factors being divided by are positive and finite. Repeating the argument with the two measures exchanged gives, for all sufficiently small \(U\in\mathcal U\),
\[
 (1-\varepsilon)\frac{\mu(O)}{\nu(O)}
 \le\frac{\mu(U)}{\nu(U)}
 \le\frac1{1-\varepsilon}\frac{\mu(O)}{\nu(O)}.
\]
Thus the neighborhood net of ratios has limit \(\mu(O)/\nu(O)\). The net is the same for every such \(O\), so these ratios all have one common value \(c>0\).

Let \(A\) be any open set and \(K\subset A\) any compact set. Compact shrinking supplies a relatively compact open \(O\) with \(K\subset O\subset A\). Hence \(\mu(K)\le\mu(O)=c\nu(O)\le c\nu(A)\). Taking the supremum over \(K\), and then exchanging the measures, proves \(\mu(A)=c\nu(A)\), also when this value is infinite. Finally outer regularity gives \(\mu(E)=c\nu(E)\) for every Borel \(E\). Evaluating any nonempty relatively compact open set proves uniqueness of \(c\). \(\square\)

This argument uses only the open-set assertion of Theorem 5.1, which has already been proved without sigma-finiteness. It uses neither a modular function nor the uniqueness being established. From now on, \(\mu\) denotes a fixed left Haar measure on \(G\), and we write \(\int f(t)\,dt=\int f\,d\mu\).

## 10. The modular function

A left Haar measure need not be right invariant. The modular function measures how far it is from right invariance.

**Theorem 10.1.** Let \(\mu\) be a left Haar measure on \(G\).

1. For each \(x\in G\), \(E\mapsto\mu(Ex)\) is a left Haar measure. So there is a unique \(\Delta(x)\in(0,\infty)\) with \(\mu(Ex)=\Delta(x)\mu(E)\) for every Borel \(E\). Another left Haar measure in place of \(\mu\) gives the same \(\Delta(x)\).
2. \(\Delta\) is a continuous homomorphism from \(G\) to the multiplicative group \((0,\infty)\).
3. For every Borel \(f\geq0\), and for every \(f\in L^1(\mu)\),
\[
\int f(tx)\,dt=\Delta(x)^{-1}\int f(t)\,dt .
\tag{10.1}
\]
In particular \(\|R_xf\|_p=\Delta(x)^{-1/p}\|f\|_p\) for \(f\in L^p(\mu)\), \(1\leq p<\infty\).
4. \(\Delta=1\) on every compact subgroup. Every compact, abelian or discrete group is *unimodular* (\(\Delta\equiv1\)). \(G\) is unimodular exactly when \(\mu\) is right invariant as well. If \(G/[G,G]\) is compact, where \([G,G]\) is the closure of the subgroup generated by the commutators \(xyx^{-1}y^{-1}\), then \(G\) is unimodular.

**Proof.** (1) Right translation by \(x\) is a homeomorphism, so \(\mu_x(E)=\mu(Ex)\) is Radon by Proposition 3.1(1). It is nonzero and left invariant, since \(y(Ex)=(yE)x\). By uniqueness (Theorem 9.2), \(\mu_x=\Delta(x)\mu\) with \(\Delta(x)>0\). Replacing \(\mu\) by \(c\mu\) does not change \(\Delta\).
(2) Let \(E\) be a compact neighbourhood of \(e\), so \(0<\mu(E)<\infty\) by Proposition 9.1 and (R1). Then \(\Delta(xy)\mu(E)=\mu(Exy)=\Delta(y)\mu(Ex)=\Delta(y)\Delta(x)\mu(E)\). So \(\Delta\) is a homomorphism, and \(\Delta(x^{-1})=\Delta(x)^{-1}\). Continuity is proved after (3).
(3) For \(f=1_E\), \(\int1_E(tx)\,dt=\mu(Ex^{-1})=\Delta(x)^{-1}\mu(E)\). Linearity, then the layer functions (1.1) with monotone convergence, then splitting into four nonnegative parts extend this to simple functions, to Borel \(f\geq0\), and to \(L^1\). Apply it to \(|f|^p\) for the norm formula.
*Continuity of \(\Delta\).* Fix \(f\in C_c^+(G)\); by (3), \(\Delta(x)^{-1}=\int R_xf\,dt/\int f\,dt\), where the denominator is positive by Proposition 9.1. Let \(W\) be a compact neighbourhood of \(e\) and \(x\in x_0W\). Then \(R_xf\) vanishes off the compact set \((\operatorname{supp}f)W^{-1}x_0^{-1}\), and \(\|R_xf-R_{x_0}f\|_{\sup}=\|R_{x_0}(R_{x_0^{-1}x}f-f)\|_{\sup}=\|R_{x_0^{-1}x}f-f\|_{\sup}\), which tends to \(0\) as \(x\to x_0\) by uniform continuity (Proposition 7.3). So \(\int R_xf\,dt\to\int R_{x_0}f\,dt\).
(4) \(\Delta(K)\) is a compact subgroup of \((0,\infty)\) for a compact subgroup \(K\). If it contained some \(r\neq1\), it would contain all powers \(r^n\), \(n\in\mathbb Z\), which form an unbounded set. So \(\Delta(K)=\{1\}\); take \(K=G\) for compact \(G\). For abelian \(G\), \(\mu(Ex)=\mu(xE)=\mu(E)\). On a discrete group, counting measure is invariant on both sides, and it is Radon: compact sets are finite and every set is open. The equivalence with right invariance is the definition of \(\Delta\). Finally, \(\Delta\) takes values in an abelian group, so it is \(1\) on every commutator, hence on the subgroup they generate, and by continuity on its closure \(N=[G,G]\). This \(N\) is closed, and it is normal because conjugates of commutators are commutators and conjugation is a homeomorphism. So \(\Delta=\bar\Delta\circ q\) for a homomorphism \(\bar\Delta\) on the locally compact group \(G/N\) (Proposition 7.1(5)), and \(\bar\Delta\) is continuous because \(q\) is open: \(\bar\Delta^{-1}(W)=q(\Delta^{-1}(W))\). If \(G/N\) is compact, \(\Delta(G)=\bar\Delta(G/N)\) is a compact subgroup of \((0,\infty)\), hence \(\{1\}\). \(\square\)

In shorthand, (10.1) reads \(d\mu(tx)=\Delta(x)\,d\mu(t)\).

## 11. Inversion and right Haar measure

**Theorem 11.1** (Inversion). For every Borel \(f\colon G\to[0,\infty]\),
\[
\int f(t^{-1})\,dt=\int f(t)\,\Delta(t)^{-1}\,dt ,
\tag{11.1}
\]
and the same holds for every Borel \(f\) with \(\int|f|\Delta^{-1}\,d\mu<\infty\). Equivalently, the right Haar measure \(\tilde\mu(E)=\mu(E^{-1})\) equals \(\Delta^{-1}\mu\), that is, \(\tilde\mu(E)=\int_E\Delta(t)^{-1}\,dt\). Moreover \(\int f(t^{-1})\Delta(t)^{-1}\,dt=\int f(t)\,dt\) for every Borel \(f\geq0\).

**Proof.** For \(f\in C_c(G)\) put \(f^\natural(t)=f(t^{-1})\Delta(t)^{-1}\), again in \(C_c(G)\), and \(J(f)=\int f^\natural\,d\mu\). The functional \(J\) is linear, and \(J(f)>0\) for \(f\in C_c^+(G)\) by Proposition 9.1. It is left invariant: with \(k=f^\natural\) and \(y\in G\),
\[
(L_yf)^\natural(t)=f\big((ty)^{-1}\big)\Delta(t)^{-1}=f\big((ty)^{-1}\big)\Delta(ty)^{-1}\Delta(y)=\Delta(y)\,k(ty),
\]
so \(J(L_yf)=\Delta(y)\Delta(y)^{-1}\int k\,d\mu=J(f)\) by (10.1). So \(J\) is a left Haar integral, and by Proposition 8.2 and uniqueness (Theorem 9.2), \(J=c\int\cdot\,d\mu\) on \(C_c(G)\) for some \(c>0\). Now \((f^\natural)^\natural(t)=f^\natural(t^{-1})\Delta(t)^{-1}=f(t)\Delta(t)\Delta(t)^{-1}=f(t)\). So for \(f\in C_c^+(G)\),
\(\int f\,d\mu=J(f^\natural)=c\int f^\natural\,d\mu=cJ(f)=c^2\int f\,d\mu\), and \(c=1\). Apply \(J=\int\cdot\,d\mu\) to \(g=f\Delta^{-1}\in C_c(G)\): since \(g(t^{-1})\Delta(t)^{-1}=f(t^{-1})\), this gives (11.1) for \(f\in C_c(G)\).

The measure \(\tilde\mu=\iota_*\mu\) is Radon (Proposition 3.1(1)) with \(\int f\,d\tilde\mu=\int f(t^{-1})\,dt\). The measure \(\Delta^{-1}\mu\) is Radon by Proposition 3.1(2), because \(\Delta^{-1}\) is continuous and positive. By the previous paragraph they integrate every \(f\in C_c(G)\) alike, so they are equal by the uniqueness in Theorem 2.2. Integrating a Borel \(f\geq0\) against both (Proposition 3.1(1) and (2)) gives (11.1). For \(f\) with \(\int|f|\Delta^{-1}d\mu<\infty\), apply this to the four nonnegative parts of \(f\). For the last formula apply (11.1) to the Borel function \(t\mapsto f(t)\Delta(t)\), using \(\Delta(t^{-1})=\Delta(t)^{-1}\). \(\square\)

Formula (11.1) holds for all nonnegative Borel functions, whatever their support.

**Corollary 11.2.**

1. \(\mu\) and \(\tilde\mu\) have the same null sets and the same \(\sigma\)-finite sets.
2. For \(1\leq p<\infty\), \((S_pf)(t)=\Delta(t)^{-1/p}f(t^{-1})\) defines a linear isometry of \(L^p(\mu)\) onto itself with \(S_p^2=1\). For \(p=2\), \((J\xi)(t)=\Delta(t)^{-1/2}\overline{\xi(t^{-1})}\) is a conjugate-linear isometric involution of \(L^2(G)\).
3. \(f\mapsto\check f\) and \(f\mapsto\Delta^{1/p}f\) are isometries of \(L^p(\mu)\) onto \(L^p(\tilde\mu)\).
4. If \(G\) is not unimodular, \(\Delta\) is unbounded above and below.
5. The measure \((1+\Delta)\mu\) is a Radon measure, and \(C_c(G)\) is dense in \(L^2((1+\Delta)\mu)\). Consequently \(C_c(G)\) is a core for multiplication by \(\Delta^{1/2}\) on its maximal domain \(\{\xi\in L^2(G):\Delta^{1/2}\xi\in L^2(G)\}\), whose graph norm is \(\big(\int|\xi|^2(1+\Delta)\,d\mu\big)^{1/2}\).

**Proof.** (1) Since \(\tilde\mu=\Delta^{-1}\mu\) with a continuous positive density, this is Proposition 3.1(2). (2) By the last formula of the theorem applied to \(|f|^p\), \(\int\Delta(t)^{-1}|f(t^{-1})|^p\,dt=\int|f|^p\,dt\). Also \(S_p(S_pf)(t)=\Delta(t)^{-1/p}\Delta(t^{-1})^{-1/p}f(t)=f(t)\), so \(S_p\) is onto. Complex conjugation commutes with \(S_2\) and is a conjugate-linear isometry. (3) \(\int|\check f|^p\,d\tilde\mu=\int|f(t)|^p\,dt\) by the definition of \(\tilde\mu\), and \(\int\Delta|f|^p\,d\tilde\mu=\int|f|^p\,d\mu\) by the theorem; the inverse maps have the same form. (4) \(\Delta(G)\) is a subgroup of \((0,\infty)\) containing some \(r\neq1\), hence all \(r^n\). (5) Apply Proposition 3.1(2) with the positive continuous density \(1+\Delta\), and then the density of \(C_c\) in \(L^2\) (Proposition 3.1(4)). The graph norm identity is immediate, and a function \(\xi\) lies in the maximal domain exactly when it lies in \(L^2((1+\Delta)\mu)\). \(\square\)

**Example 11.3** (Explicit Haar measures on \(\mathbb R^\times\) and on the \(ax+b\) group). Integrals of continuous compactly supported functions of one real variable below are Riemann integrals, and substitutions use the change-of-variables rule for Riemann integrals (see "Results used from other lessons").
(a) On the multiplicative group \(\mathbb R^\times=\mathbb R\setminus\{0\}\), \(I(f)=\int f(x)\,dx/|x|\) is a Haar integral: the substitution \(u=cx\) gives \(\int f(cx)\,dx/|x|=\int f(u)\,du/|u|\) for \(c\neq0\). The group is abelian, so \(\Delta\equiv1\).
(b) Let \(G=\{(a,b):a>0,\ b\in\mathbb R\}\) with \((a,b)(a',b')=(aa',ab'+b)\), identity \((1,0)\), inverse \((a,b)^{-1}=(1/a,-b/a)\), and the topology of the open half-plane. Put \(I(f)=\int_0^\infty\big(\int_{\mathbb R}f(a,b)\,db\big)a^{-2}\,da\). For \(x_0=(a_0,b_0)\), the substitutions \(u=a_0b+b_0\) (inner) and \(v=a_0a\) (outer) give
\[
\int_0^\infty\!\!\int_{\mathbb R}f(a_0a,a_0b+b_0)\,db\,\frac{da}{a^2}=\int_0^\infty\frac1{a_0}\int_{\mathbb R}f(a_0a,u)\,du\,\frac{da}{a^2}=\int_0^\infty\!\!\int_{\mathbb R}f(v,u)\,du\,\frac{dv}{v^2},
\]
so \(I\) is a left Haar integral, \(d\mu=a^{-2}\,da\,db\). The substitutions \(u=ab_0+b\) and \(v=aa_0\) give \(\int f(tx_0)\,d\mu(t)=a_0\int f\,d\mu\), so by (10.1)
\[
\Delta(a,b)=1/a .
\]
The inversion formula (11.1) can be checked directly: the substitutions \(u=-b/a\) and \(v=1/a\) give \(\int f(t^{-1})\,d\mu(t)=\int_0^\infty\int_{\mathbb R}f(v,u)\,du\,v^{-1}\,dv\), which is \(\int f\Delta^{-1}\,d\mu\). So the right Haar measure is \(a^{-1}\,da\,db\). The commutators \((a,b)(a',b')(a,b)^{-1}(a',b')^{-1}\) have first coordinate \(1\), and they fill the normal subgroup \(\{1\}\times\mathbb R\); the quotient \(G/(\{1\}\times\mathbb R)\cong(0,\infty)\) is not compact, in line with Theorem 10.1(4). This group is a good test case for the signs in (10.1) and (11.1).

## 12. Products of groups

The Radon product of Haar measures is a Haar measure. For two copies of \(G\) this gives the measure on \(G\times G\) behind convolution (Section 14); for infinitely many compact groups it gives the Haar measure of an infinite product.

**Proposition 12.1** (The group \(G\times G\)). Keep \(G\) and its left Haar measure \(\mu\), and let \(\pi=\mu\hat\times\mu\) on \(G\times G\).

1. On the locally compact group \(G\times G\), \(\pi\) is invariant under left translations, so it is a left Haar measure; its modular function is \((s,t)\mapsto\Delta(s)\Delta(t)\). In the same way, if each \(G_j\) (\(j=1,\dots,n\)) carries a left Haar measure \(\mu_j\), the iterated Radon product \((\cdots(\mu_1\hat\times\mu_2)\cdots)\hat\times\mu_n\) is one on \(G_1\times\dots\times G_n\), and it integrates functions in \(C_c\) by iterated integrals.
2. For every continuous \(a\colon G\to G\), the map \(\Phi_a(s,t)=(s,a(s)t)\) is a homeomorphism of \(G\times G\) that preserves \(\pi\). So \((W_a\zeta)(s,t)=\zeta(s,a(s)t)\) is a unitary on \(L^2(G\times G,\pi)\), with inverse \(\zeta\mapsto\zeta(s,a(s)^{-1}t)\).
3. Under the unitary \(U\) of Theorem 6.2, the operator \(1\otimes\lambda(g)\) is \(W_a\) for the constant \(a\equiv g^{-1}\): \(\zeta(s,t)\mapsto\zeta(s,g^{-1}t)\). For \(a(s)=s\), \(W_a\) is the operator \((W\zeta)(s,t)=\zeta(s,st)\), with inverse \(\zeta(s,s^{-1}t)\).

**Proof.** (1) For \(F\in C_c(G\times G)\) and \((g,h)\in G\times G\), \(\int\big(\int F(gs,ht)\,dt\big)ds=\int\big(\int F(gs,t)\,dt\big)ds=\int\big(\int F(s,t)\,dt\big)ds\), by left invariance applied first to the inner function \(t\mapsto F(gs,t)\) and then to the outer function \(s\mapsto\int F(s,t)\,dt\), which lies in \(C_c(G)\) by Proposition 4.2(1). So \(\pi\) is a left Haar measure by Proposition 8.2 (it is nonzero by (4.2)). In the same way, (10.1) gives \(\iint F(sg,th)\,dt\,ds=\Delta(g)^{-1}\Delta(h)^{-1}\iint F\,dt\,ds\), which identifies the modular function by Theorem 10.1(3). The statement for \(n\) factors follows by induction, using Proposition 4.2 for the iterated integral.
(2) \(\Phi_a\) is continuous, with continuous inverse \((s,t)\mapsto(s,a(s)^{-1}t)\). For \(F\in C_c(G\times G)\), also \(F\circ\Phi_a\in C_c(G\times G)\), and \(\int F\circ\Phi_a\,d\pi=\int\big(\int F(s,a(s)t)\,dt\big)ds=\int\big(\int F(s,t)\,dt\big)ds\) by left invariance in \(t\) for each fixed \(s\). So the Radon measures \((\Phi_a)_*\pi\) (Proposition 3.1(1)) and \(\pi\) agree by the uniqueness in Theorem 2.2. Hence \(\zeta\mapsto\zeta\circ\Phi_a\) preserves null sets and the \(L^2(\pi)\) norm, and its inverse is composition with \(\Phi_a^{-1}\).
(3) \(U(\xi\otimes L_g\eta)(s,t)=\xi(s)\eta(g^{-1}t)=U(\xi\otimes\eta)(s,g^{-1}t)\). Both operators are bounded and agree on elementary tensors. \(\square\)

**Example 12.2** (Infinite products of compact groups, and \((\mathbb Z_2)^{\mathbb N}\) versus \([0,1]\)). Let \((G_\alpha)_{\alpha\in A}\) be compact groups with Haar measures \(\mu_\alpha(G_\alpha)=1\) (compact groups are unimodular by Theorem 10.1(4)). The product \(G=\prod_\alpha G_\alpha\), with the product topology and the group law taken coordinate by coordinate, is a compact group by Tychonoff's theorem. Write \(C_F(G)\) for the continuous functions that depend on only finitely many coordinates, \(f(x)=f_0(x_{\alpha_1},\dots,x_{\alpha_n})\) with \(f_0\) continuous. It is a self-adjoint algebra, it contains the constant functions, and it separates the points of \(G\): if \(x_\alpha\neq x'_\alpha\), (T2) on \(G_\alpha\) gives a continuous function of the coordinate \(x_\alpha\) that separates them. By the Stone–Weierstrass theorem, \(C_F(G)\) is dense in \(C(G)\). Put \(I(f)=\int f_0\,d(\mu_{\alpha_1}\hat\times\cdots\hat\times\mu_{\alpha_n})\). The value is independent of how \(f\) is written: by (4.1) the order of the factors is irrelevant, and a coordinate on which \(f_0\) does not depend contributes a factor \(\mu_\beta(G_\beta)=1\). So \(I\) is linear and positive on \(C_F(G)\), \(|I(f)|\leq\|f\|_{\sup}\), \(I(1)=1\), and \(I\) is left invariant because each finite product measure is a left Haar measure (Proposition 12.1(1)). It extends uniquely to a positive, left-invariant, norm-one functional on \(C(G)\) (positivity passes to the limit because \(\operatorname{Re}f_n+\|f-f_n\|_{\sup}\geq0\) when \(f\geq0\)). Its Radon measure is the Haar measure of \(G\) with total mass \(1\).

For \(G=(\mathbb Z_2)^{\mathbb N}\), each factor with mass \(\frac12\) on each point, let \(\Phi(a)=\sum_ja_j2^{-j}\in[0,1]\). This map is continuous and onto, and it is one-to-one except over the dyadic rationals \(j2^{-k}\) in \((0,1)\), each of which has two preimages. It carries Haar measure to Lebesgue measure \(\lambda_1\) on \([0,1]\): \(\lambda_1(E)=\mu(\Phi^{-1}(E))\) for every Borel \(E\). Proof: \(\Phi_*\mu\) is a finite Borel measure on \([0,1]\). It is outer regular: by (R2) for \(\mu\) there is an open \(O\supseteq\Phi^{-1}(E)\) with \(\mu(O\setminus\Phi^{-1}(E))<\varepsilon\); then \(U=[0,1]\setminus\Phi(G\setminus O)\) is open (\(\Phi\) is a closed map, since \(G\) is compact), contains \(E\), and satisfies \(\Phi^{-1}(U)\subseteq O\), so \(\Phi_*\mu(U\setminus E)<\varepsilon\). A finite outer regular measure on a compact space is also inner regular on open sets (take complements), so \(\Phi_*\mu\) is Radon. For continuous \(f\) on \([0,1]\), the cylinder sets fixing \(a_1,\dots,a_k\) have measure \(2^{-k}\) and are mapped onto the intervals \([j2^{-k},(j+1)2^{-k}]\), so \(\int f\circ\Phi\,d\mu\) differs from the Riemann sum \(\sum_j2^{-k}f(j2^{-k})\) by at most the oscillation of \(f\) on intervals of length \(2^{-k}\). Letting \(k\to\infty\), \(\int f\,d\Phi_*\mu=\int_0^1f\,dx\). By the uniqueness in Theorem 2.2, \(\Phi_*\mu=\lambda_1\).

### The Heisenberg group and its volume scaling

**Example 12.3.** Let \(N=\mathbb R^3\) with multiplication
\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy').
\tag{12.3}
\]
This is the group of matrices \(\begin{pmatrix}1&x&z\\0&1&y\\0&0&1\end{pmatrix}\), with the ordinary Euclidean topology. Its identity is \((0,0,0)\) and its inverse is
\[
(x,y,z)^{-1}=(-x,-y,-z+xy).
\]
Matrix multiplication proves associativity, or one can check that the third coordinate of either association is \(z+z'+z''+xy'+xy''+x'y''\). The polynomial multiplication and inverse are continuous, so this is an LCH group.

Lebesgue measure \(dx\,dy\,dz\) is both left and right Haar measure. Indeed, left and right multiplication by \((a,b,c)\) are respectively
\[
(x,y,z)\longmapsto(a+x,b+y,c+z+ay),\qquad
(x,y,z)\longmapsto(x+a,y+b,z+c+xb).
\]
For \(f\in C_c(\mathbb R^3)\), integrate in \(z\) first. Each added third-coordinate term is a translation depending only on \(x,y\), so it leaves that inner integral unchanged. Translate \(x\) and \(y\) next. Fubini and the one-variable substitution rule give invariance of the full integral in both cases. The transported Radon measures consequently agree on all Borel sets by Riesz uniqueness. Thus \(\Delta_N=1\). The group is nonabelian: with the commutator convention \([u,v]=uvu^{-1}v^{-1}\),
\[
[(a,0,0),(0,b,0)]=(0,0,ab).
\]

For \(r>0\), set \(D_r(x,y,z)=(rx,ry,r^2z)\). Substitution in (12.3) proves \(D_r(uv)=D_r(u)D_r(v)\), and \(D_{1/r}\) is its inverse. Three one-variable substitutions give
\[
\int_N f(D_ru)\,du=r^{-4}\int_Nf(u)\,du,
\qquad \mu(D_rE)=r^4\mu(E)
\tag{12.4}
\]
for every Borel \(E\); the second identity follows from the first by equality of Radon measures. The powers \(r,r,r^2\) explain why the **homogeneous dimension** is \(4\), even though the underlying manifold has dimension \(3\).

Fischer and Ruzhansky use symmetric coordinates \(t=z-xy/2\). The coordinate change is a shear preserving Lebesgue measure, by integration in the third coordinate, and converts (12.3) into
\[
(x,y,t)(x',y',t')=(x+x',y+y',t+t'+(xy'-yx')/2).
\]
These two descriptions therefore have the same Haar normalization. Integer matrix coordinates give the lattice computed in [the arithmetic lesson](finite-covolume-and-arithmetic-quotients.md#heisenberg-lattice-volume); in the symmetric coordinates its third coordinate is \(k-mn/2\), rather than always an integer. This distinction prevents a spurious factor of two in a fundamental domain.

## 13. Groups that are not σ-compact

When \(G\) is not \(\sigma\)-compact, its Haar measure is not \(\sigma\)-finite, and several familiar facts need care: inner regularity, the duality between \(L^1\) and \(L^\infty\), and Fubini's theorem. This section describes the measure through the cosets of an open \(\sigma\)-compact subgroup, sets up the right notion of \(L^\infty\), and ends with the examples that show what fails.

Fix an open, closed, \(\sigma\)-compact subgroup \(G_0\) (Proposition 7.2) and a set \(Y\subseteq G\) that contains exactly one point of each left coset of \(G_0\). So the open \(\sigma\)-compact sets \(yG_0\), \(y\in Y\), partition \(G\), and \(\mu\) restricted to any one of them is \(\sigma\)-finite by (R1). The restriction of \(\mu\) to the Borel subsets of \(G_0\) is a left Haar measure of the locally compact group \(G_0\): the restriction of a Radon measure to an open set is Radon there, it is nonzero by Proposition 9.1, and it is invariant under left translation by elements of \(G_0\).

**Proposition 13.1** (Cosets). Let \(E\subseteq G\) be Borel.

1. If \(E\) lies in countably many cosets \(y_jG_0\), then \(\mu(E)=\sum_j\mu(E\cap y_jG_0)\).
2. If \(E\) meets uncountably many cosets, then \(\mu(E)=\infty\).
3. Hence a Borel set is \(\sigma\)-finite exactly when it lies in countably many cosets. In particular every Borel set of finite measure does. Moreover \(G\) is \(\sigma\)-compact \(\iff\) \(\mu\) is \(\sigma\)-finite \(\iff\) \(Y\) is countable.

**Proof.** First recover the measure of an open set directly from the coset partition. Write \(C_y=yG_0\), and define the sum of nonnegative numbers over \(Y\) as the supremum of its finite subsums. For an open \(U\), finite additivity gives
\[
\sum_{y\in Y}\mu(U\cap C_y)\leq\mu(U).
\]
Every compact \(K\subset U\) meets finitely many cosets, since the cosets are an open cover of \(K\). Splitting \(K\) among them bounds \(\mu(K)\) by the same sum. Inner regularity on \(U\) gives the reverse inequality. Outer regularity now gives an exact envelope formula for every Borel \(E\):
\[
\mu(E)=\inf_{U\supset E\text{ open}}\sum_{y\in Y}\mu(U\cap C_y).
\tag{13.1}
\]
If \(E\) is contained in countably many cosets, countable additivity proves (1). If an open \(U\) meets uncountably many cosets, all their open intersections have positive measure by Proposition 9.1. A family of positive numbers with finite supremum of finite subsums has only countably many members: for each \(n\), only finitely many can exceed \(1/n\). Thus the sum in (13.1) is infinite for every open superset of an \(E\) meeting uncountably many cosets. This proves (2).

Each coset is sigma-finite, so countably many cosets give a sigma-finite set. Conversely, every finite-measure Borel set meets countably many cosets by (2), and a countable union of those sets still does. This proves the first claim of (3). Finally a compact set meets finitely many cosets, so sigma-compactness forces \(Y\) countable; countably many sigma-compact cosets give sigma-compactness, and the established sigma-finite criterion gives the remaining equivalences. \(\square\)

The freely accessible coset-local viewpoint in [Fremlin, §443J](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt443.tex) motivates the distinction used here. Formula (13.1) has been derived from the course’s own outer-regular Borel measure. The locally determined measure in Fremlin’s convention is constructed and compared explicitly in Proposition 13.7 below; its value on an arbitrary Borel set is not assumed to equal (13.1).

**Definition 13.2.** A set \(E\subseteq G\) is *locally Borel* when its intersection with each Borel set of finite measure is Borel, and *locally null* when, in addition, all these intersections are null. A property holds *locally almost everywhere* when the points where it fails form a locally null set. Call \(f\colon G\to\mathbb C\) *locally measurable* when the preimage of each Borel subset of \(\mathbb C\) is locally Borel. \(L^\infty(G)\) consists of the locally measurable \(f\) with \(|f|\leq c\) locally almost everywhere for some constant \(c\); two such functions are identified when they agree locally almost everywhere; and \(\|f\|_\infty\) is the infimum of those constants \(c\).

Why the local notions? With the ordinary definitions, \(L^\infty\) need not be the dual of \(L^1\) when the measure is not \(\sigma\)-finite. For Haar measure on \(\mathbb R\times\mathbb R_d\), the indicator of the locally null set \(Y\) of Example 13.4 is a nonzero element of the ordinary \(L^\infty\), yet it integrates every \(L^1\) function to \(0\). The local versions repair this.

**Theorem 13.3.**

1. \(E\) is locally Borel exactly when every \(E\cap yG_0\) is Borel, and locally null exactly when every \(E\cap yG_0\) is null. \(f\) is locally measurable exactly when every restriction \(f|_{yG_0}\) is Borel. A Borel set is locally null exactly when all its compact subsets are null. A locally null Borel set is null exactly when it is \(\sigma\)-finite. Countable unions of locally null sets are locally null, and \(|f|\leq\|f\|_\infty\) locally almost everywhere.
2. For \(f\in L^\infty(G)\) and \(g\in L^p(G)\), \(1\leq p<\infty\), the product \(fg\) is Borel, its class depends only on the classes of \(f\) and \(g\), and \(\|fg\|_p\leq\|f\|_\infty\|g\|_p\).
3. (*\(L^1{}^*=L^\infty\)*) For every bounded linear functional \(\Phi\) on \(L^1(G)\) there is a unique \(f\in L^\infty(G)\) with \(\Phi(g)=\int fg\,d\mu\) for all \(g\in L^1(G)\), and \(\|\Phi\|=\|f\|_\infty\).
4. The map \(f\mapsto m_f\), \(m_f\xi=f\xi\), is an isometric \(*\)-isomorphism of \(L^\infty(G)\) onto a von Neumann algebra on \(L^2(G)\) that is maximal abelian.
5. (*Radon–Nikodym, restricted form*) Let \(\nu\) and \(\mu'\) be Radon measures on an LCH space \(X\), with \(\nu\) \(\sigma\)-finite and \(\nu(E)=0\) whenever \(\mu'(E)=0\). Then \(\nu(E)=\int_Eh\,d\mu'\) for all Borel \(E\), for some Borel \(h\geq0\).

**Proof.** (1) Each coset \(yG_0\) is the union of countably many compact sets \(yK_n\), each of finite measure, so \(E\cap yG_0=\bigcup_nE\cap yK_n\) is Borel (null) if \(E\) is locally Borel (locally null). Conversely, a Borel \(F\) of finite measure lies in countably many cosets \(y_jG_0\), so \(E\cap F=\bigcup_j(E\cap y_jG_0)\cap F\) is Borel (null). The statement about functions follows. If every compact subset of a Borel set \(E\) is null and \(\mu(F)<\infty\), then \(\mu(E\cap F)=0\) by inner regularity on sets of finite measure (Proposition 2.3(1)); conversely, compact sets have finite measure. A \(\sigma\)-finite locally null Borel set is the union of its intersections with countably many sets of finite measure, each null. If \(E_n\) are locally null and \(\mu(F)<\infty\), then \(\mu(\bigcup_nE_n\cap F)\leq\sum_n\mu(E_n\cap F)=0\). Finally \(\{|f|>\|f\|_\infty\}=\bigcup_n\{|f|>\|f\|_\infty+1/n\}\) is a countable union of locally null sets.
(2) By Proposition 3.1(4), \(\{g\neq0\}\) is a disjoint union of Borel sets \(F_n\) of finite measure. Each \(f1_{F_n}\) is Borel, so \(fg=\sum_n(f1_{F_n})g\) is Borel (at each point at most one term is nonzero). If \(f=f'\) locally a.e., the set \(\{f\neq f'\}\cap\{g\neq0\}\) is Borel, \(\sigma\)-finite and locally null, hence null by (1); so \(fg=f'g\) a.e. In the same way \(|fg|\leq\|f\|_\infty|g|\) a.e.
(3) For \(y\in Y\), the functions in \(L^1(G)\) that vanish off \(yG_0\) form a copy of \(L^1(yG_0,\mu)\), and \(\mu\) is \(\sigma\)-finite there. The duality \(L^1{}^*=L^\infty\) for \(\sigma\)-finite measures provides a Borel function \(f_y\) on \(yG_0\) with \(|f_y|\leq\|\Phi\|\) and \(\Phi(g)=\int_{yG_0}f_yg\,d\mu\) for those \(g\). Let \(f=f_y\) on \(yG_0\). By (1), \(f\) is locally measurable, and \(\|f\|_\infty\leq\|\Phi\|\). Let \(g\in L^1(G)\). The set \(\{g\neq0\}\) is \(\sigma\)-finite, so it lies in countably many cosets \(y_jG_0\), and \(g=\sum_jg1_{y_jG_0}\) in \(L^1\) by dominated convergence. Hence \(\Phi(g)=\sum_j\int_{y_jG_0}fg\,d\mu=\int fg\,d\mu\), again by dominated convergence, since \(|fg|\leq\|\Phi\||g|\). By (2) with \(p=1\), \(\|\Phi\|\leq\|f\|_\infty\). For uniqueness, suppose \(\int hg\,d\mu=0\) for all \(g\in L^1(G)\) but \(h\neq0\) on a set that is not locally null. Then for some \(c>0\) and some Borel \(F\) of finite measure, \(D=\{|h|>c\}\cap F\) has positive measure; with \(g=1_D\bar h/|h|\) we get \(\int hg\,d\mu=\int_D|h|\,d\mu>0\), a contradiction.
(4) By (2), \(m_f\) is bounded with \(\|m_f\|\leq\|f\|_\infty\). If \(c<\|f\|_\infty\), the set \(\{|f|>c\}\) is not locally null, so for some Borel \(F\) of finite measure the set \(D=\{|f|>c\}\cap F\) has \(\mu(D)>0\); then \(\|m_f1_D\|_2^2\geq c^2\mu(D)=c^2\|1_D\|_2^2\). So \(m\) is isometric. Clearly \(m_{fg}=m_fm_g\) and \(m_{\bar f}=m_f^*\). Let \(T\) commute with every \(m_f\). Then \(T\) commutes with the projections \(P_y=m_{1_{yG_0}}\), so it maps each \(H_y=P_yL^2(G)\cong L^2(yG_0,\mu)\) into itself. On \(H_y\) it commutes with multiplication by every bounded Borel function on \(yG_0\) (extended by \(0\), such a function lies in \(L^\infty(G)\)). On a \(\sigma\)-finite measure space the multiplication operators form a maximal abelian algebra ([Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators), Theorem 9.1). Applied to the \(\sigma\)-finite measure space \(yG_0\), this shows that \(T|_{H_y}\) is multiplication by a bounded Borel function \(f_y\) on \(yG_0\), which we may take with \(|f_y|\leq\|T\|\) by the norm formula just proved. Let \(f=f_y\) on \(yG_0\); then \(f\in L^\infty(G)\). A vector \(\xi\in L^2(G)\) lives on countably many cosets (Proposition 3.1(4) and Proposition 13.1(3)), so \(\xi=\sum_jP_{y_j}\xi\) and \(T\xi=\sum_jf_{y_j}P_{y_j}\xi=f\xi\). So \(T=m_f\). Thus \(m(L^\infty)'\subseteq m(L^\infty)\), and the reverse inclusion holds because \(m(L^\infty)\) is abelian. Hence \(m(L^\infty)'=m(L^\infty)\), which is maximal abelian, and \(m(L^\infty)''=m(L^\infty)\).
(5) We construct the density by disjoint finite blocks, using only Proposition 2.3(3) and the proved sigma-finite Radon–Nikodym theorem of the measure-tools lesson. The first result supplies compact sets \(K_n\) whose union has full \(\nu\)-measure. Put
\[
D_1=K_1,\qquad D_n=K_n\setminus\bigcup_{j<n}K_j\quad(n>1).
\]
These are disjoint Borel sets, each contained in a compact set. Consequently both restricted measures \(\nu|_{D_n}\) and \(\mu'|_{D_n}\) are finite. Absolute continuity is preserved by restriction. The finite-measure density theorem gives a nonnegative Borel \(h_n\) on \(D_n\) such that
\[
\nu(E\cap D_n)=\int_{E\cap D_n}h_n\,d\mu'
\quad(E\text{ Borel}).
\]
Extend each \(h_n\) by zero to \(X\), and set \(h=\sum_nh_n\). Countable sums of nonnegative Borel functions are Borel. The part of any \(E\) outside the blocks is \(\nu\)-null, so countable additivity and the already proved nonnegative integral-sum identity give
\[
\nu(E)=\sum_n\nu(E\cap D_n)=\sum_n\int_Eh_n\,d\mu'
=\int_Eh\,d\mu'.
\]
This explicitly constructs one global density without assuming that the reference measure \(\mu'\) is sigma-finite on \(X\). \(\square\)

Part (4) carries the maximal abelian property of \(L^\infty\) from \(\sigma\)-finite measure spaces to Haar measure on every locally compact group, and no lifting theorem is needed.

The following examples show what fails without \(\sigma\)-finiteness. In each of them the bad set is locally null, so it carries no \(L^p\) mass for \(p<\infty\).

**Example 13.4** (An uncountable discrete factor). Take an uncountable discrete group \(D\) and \(G=\mathbb R\times D\). Lebesgue measure on \(\mathbb R\) is Radon by the construction in the preceding measure-tools lesson. Counting measure on \(D\) is Radon: compact sets are finite, every set is open, and the supremum of the sizes of its finite subsets is its counting measure. Their Radon product \(\mu\) is a Haar measure by Proposition 12.1. This constructs the example entirely from the already proved product theorem.

Each \(C_d=\mathbb R\times\{d\}\) is an open sigma-compact component. The rectangle identity (4.2) shows that the restriction of \(\mu\) to \(C_d\) is Lebesgue measure. For any open \(U\subset G\), write \(U_d=\{x:(x,d)\in U\}\). The open-set computation and envelope formula in Proposition 13.1 therefore become
\[
\mu(U)=\sum_{d\in D}\lambda_1(U_d),\qquad
\mu(E)=\inf_{U\supset E\text{ open}}\sum_{d\in D}\lambda_1(U_d)
\quad(E\text{ Borel}).
\]
In particular a set contained in countably many components has the sum of its component measures. A set meeting uncountably many components has infinite outer-regular Borel measure, even if every component section is null.

For the closed set \(Y=\{0\}\times D\), every open superset has a nonempty real open section in every component. Each such section has positive length, so the preceding sum is infinite: \(\mu(Y)=\infty\). On the other hand every compact subset of \(Y\) is finite and has measure zero. Thus \(\mu\) is not inner regular on this Borel set, and is not sigma-finite. A measure both inner and outer regular on every Borel set could not represent the same Haar integral: uniqueness in Theorem 2.2 would identify it with \(\mu\), contradicting this computation.

The original concrete case \(D=\mathbb R_d\) gives \(G=\mathbb R\times\mathbb R_d\). Here \(Y\) is locally null by Theorem 13.3(1), but is not null. Every finite-\(p\) integrable function is supported in countably many components by Proposition 3.1(4) and Proposition 13.1, and \(C_c(G)\) remains dense in \(L^p(G)\). The local \(L^\infty(G)\) consists of componentwise Borel functions with a common essential bound, modulo componentwise null functions; Theorem 13.3 proves its duality with \(L^1(G)\). These assertions rely on the complete internal proofs, not on a cited example. \(\square\)

**Example 13.5** (The diagonal of \(\mathbb R_d\times\mathbb R\): Tonelli's theorem needs \(\sigma\)-finiteness). Let \(X=\mathbb R_d\) with counting measure \(c\) and \(Y=\mathbb R\) with Lebesgue measure \(m\). Their Radon product is the Haar measure of the group \(\mathbb R_d\times\mathbb R\) (Proposition 12.1(1)). The diagonal \(D=\{(t,t)\}\) is a closed subgroup. Its sections are single points: \(m(D_s)=0\) for every \(s\), while \(c(D^t)=1\) for every \(t\). So
\[
\int m(D_s)\,dc(s)=0,\qquad\int c(D^t)\,dm(t)=\infty,\qquad(c\hat\times m)(D)=\infty,
\]
the last because \(D\) meets every coset \(\{s\}\times\mathbb R\) of the open subgroup \(\{0\}\times\mathbb R\) (Proposition 13.1(2)). Thus Tonelli's theorem 5.1(4) fails for \(1_D\), whose support is not \(\sigma\)-finite. The compact subsets of \(D\) are finite, and each point has measure \(c(\{s\})m(\{s\})=0\) by (4.2); so \(D\) is locally null (Theorem 13.3(1)). The example also shows that the rectangle function \(A\times B\mapsto c(A)m(B)\) has no extension to a measure \(m'\) on \(\mathcal B(X\times Y)\) that is inner and outer regular on every Borel set. Such an \(m'\) would be Radon. It would integrate \(\varphi\boxtimes g\) to \(\int\varphi\,dc\int g\,dm\) for \(\varphi\in C_c(X)\) and \(g\in C_c(Y)\), by uniform approximation with simple functions on the compact rectangle \(\operatorname{supp}\varphi\times\operatorname{supp}g\), which has finite \(m'\)-measure. By the tensor approximation (Lemma 4.1) it would then agree with \(c\hat\times m\) on \(C_c(X\times Y)\), hence equal it by the uniqueness in Theorem 2.2. But inner regularity would force \(m'(D)=0\).

**Example 13.6** (\(\{e\}\times G\): the rectangle rule needs \(\sigma\)-finite factors). Let \(G=\mathbb R\times\mathbb R_d\) and \(\pi=\mu\hat\times\mu\). The closed set \(\{e\}\times G\) has \(\mu(\{e\})=0\) but \(\pi(\{e\}\times G)=\infty\). Indeed \(\pi\) is a Haar measure on \(G\times G\) (Proposition 12.1(1)), \(G_0\times G_0\) is an open \(\sigma\)-compact subgroup of \(G\times G\), and \(\{e\}\times G\) meets each of the uncountably many cosets \(G_0\times(\mathbb R\times\{d\})\); apply Proposition 13.1(2). So Theorem 5.1(6) fails when \(B\) is not \(\sigma\)-finite, and "\(\pi(A\times B)=\mu(A)\mu(B)\) with \(0\cdot\infty=0\)" is false for the Radon product. The set is locally null by Theorem 13.3(1): its intersection with a compact \(K\subseteq G\times G\) lies in \(\{e\}\times\mathrm{pr}_2(K)\), which is null by (4.2). So, like \(Y\) and \(D\), it carries no \(L^2\) mass.

### Two regularity conventions for Haar measure

Fremlin's *Measure Theory* uses a complete, locally determined measure that is inner regular on every measurable set. Our Borel measure is outer regular on every Borel set and inner regular on open sets. On a sigma-compact group these conventions agree after completion. On an arbitrary group, the following construction explains the difference and the common integration theory.

**Proposition 13.7** (The locally determined measure). With the open sigma-compact cosets \(yG_0\) used above, define for Borel \(E\subset G\)
\[
 m(E)=\sum_{y\in Y}\mu(E\cap yG_0),
 \qquad
 \sum_{y\in Y}a_y:=\sup_{F\subset Y\text{ finite}}\sum_{y\in F}a_y.
\]
Then \(m\) is left invariant, locally finite and inner regular on every Borel set. It agrees with \(\mu\) on open sets, compact sets and sigma-finite Borel sets, and integrates every \(C_c(G)\) function in the same way. There is a canonical isometric identification \(L^p(\mu)\cong L^p(m)\) for \(1\le p<\infty\). Nevertheless \(m\) can fail outer regularity on Borel sets. Completing each coset measure and allowing sets measurable on every coset gives a Radon measure in Fremlin's convention.

*Proof.* A sum of nonnegative numbers is the supremum of its finite subsums. The two suprema in a sum over \(Y\times\mathbb N\) commute: each finite collection of pairs is contained in the product of finite subsets, and the converse products are finite. Applying countable additivity on each coset therefore proves countable additivity of \(m\). Left translation permutes the cosets and preserves \(\mu\) on their Borel subsets, so it preserves \(m\).

A compact set meets only finitely many cosets, since the cosets form an open cover. Thus \(m\) and \(\mu\) agree on compact sets. They agree on each sigma-finite Borel set by Proposition 13.1, since such a set lies in countably many cosets. Local finiteness follows by taking a relatively compact neighborhood inside a single coset.

The restriction of \(\mu\) to each coset is sigma-finite and inner regular on every Borel set by Proposition 2.3. Given \(a<m(E)\), with \(a\ge0\), choose a finite set of cosets whose contributions exceed \(a\). In each of those cosets choose compact subsets of \(E\) whose measures still have sum exceeding \(a\). Their finite union is compact. This proves inner regularity of \(m\) on every Borel set. If \(U\) is open, inner regularity of both measures on \(U\), and their equality on compact sets, give \(m(U)=\mu(U)\). A \(C_c\) function is supported on a compact set, so its two integrals agree.

The identity on Borel representatives maps \(L^p(\mu)\) isometrically into \(L^p(m)\): a \(\mu\)-integrable function is supported on a sigma-finite set, where the measures agree. For surjectivity, take a Borel \(f\) with \(\int|f|^p\,dm<\infty\). The sum of its coset integrals is finite, so only countably many of those integrals are nonzero. Set \(f\) to zero outside those cosets. The resulting Borel function \(f_0\) equals \(f\) \(m\)-almost everywhere, is supported on a sigma-finite set and has the same norm for \(\mu\). This also proves independence of representatives and surjectivity.

For the last assertion, let \(\Sigma_{\mathrm{loc}}\) consist of the subsets whose intersections with every coset are measurable for its completed sigma-finite measure. Define the measure by the same sum. It is complete because a subset of a null set is null on every coset. It is locally determined: if a set has measurable intersections with every measurable set of finite measure, intersect it with a countable compact exhaustion of each coset to see that its coset sections are measurable. Completion preserves compact inner approximation on each coset: a completed measurable set contains a Borel subset of the same measure, and the latter has compact approximants. The preceding finite-subsum argument now gives compact inner regularity on all of \(\Sigma_{\mathrm{loc}}\). These properties, local finiteness and the Hausdorff topology give Fremlin's Radon convention.

Finally, in Example 13.4 the closed set \(Z=\{0\}\times\mathbb R_d\) satisfies \(m(Z)=0\), while every open neighborhood of \(Z\) has infinite \(m\)-measure because \(m\) and \(\mu\) agree on open sets. Thus \(m\) is not outer regular there. \(\square\)

The finite-\(p\) spaces for \(\Sigma_{\mathrm{loc}}\) have the same identification: an integrable function has nonzero coset integrals on only countably many cosets. Choose a Borel representative on each of those cosets and set it to zero elsewhere; this gives a global Borel representative of its class, with the same integral.

The construction also identifies the local \(L^\infty\) of Definition 13.2 with the \(L^\infty\) of the completed, locally determined measure: both take essentially bounded measurable functions on each coset, with a common bound, modulo functions null on every coset. Completed coset functions have Borel representatives there, so the completed version gives the same classes. This explains why the duality in Theorem 13.3 agrees with Fremlin's localizable-measure duality, despite the difference between the two global Borel measures.

## 14. Convolution and continuity of translation

In this section and the next, \(\pi=\mu\hat\times\mu\) on \(G\times G\), and integrals over \(G\) are taken with respect to \(\mu\). Convolution integrals are iterated integrals over \(G\times G\) in disguise, so we first record how \(\pi\) behaves under the changes of variables that occur.

**Lemma 14.1** (Changes of variables on \(G\times G\)). The maps
\[
\Theta_1(x,y)=(y,y^{-1}x),\qquad\Theta_2(x,y)=(y,xy^{-1}),\qquad\Theta_3(x,y)=(y,xy),\qquad\sigma(x,y)=(y,x)
\]
are homeomorphisms of \(G\times G\) with \((\Theta_1)_*\pi=\sigma_*\pi=\pi\), \((\Theta_2)_*\pi=(\Delta\circ\mathrm{pr}_1)\,\pi\) and \((\Theta_3)_*\pi=(\Delta^{-1}\circ\mathrm{pr}_1)\,\pi\). Consequently each of them pulls \(\pi\)-null sets back to \(\pi\)-null sets and \(\sigma\)-finite sets back to \(\sigma\)-finite sets, and for every Borel \(H\geq0\) on \(G\times G\)
\[
\int H\circ\Theta_1\,d\pi=\int H\,d\pi,\qquad\int H\circ\Theta_2\,d\pi=\int H(y,z)\Delta(y)\,d\pi(y,z),\qquad\int H\circ\Theta_3\,d\pi=\int H(y,z)\Delta(y)^{-1}\,d\pi(y,z).
\]

**Proof.** The inverses are \((y,z)\mapsto(yz,y)\), \((zy,y)\) and \((zy^{-1},y)\), all continuous. For \(F\in C_c(G\times G)\), (4.1) lets us integrate first in \(x\); left invariance and (10.1) in the inner integral give
\[
\int F\circ\Theta_1\,d\pi=\int\!\!\int F(y,y^{-1}x)\,dx\,dy=\int F\,d\pi,\qquad
\int F\circ\Theta_2\,d\pi=\int\!\!\int F(y,xy^{-1})\,dx\,dy=\int\Delta(y)\!\int F(y,x)\,dx\,dy,
\]
and similarly \(\int F\circ\Theta_3\,d\pi=\int\Delta(y)^{-1}\int F(y,x)\,dx\,dy\) and \(\int F\circ\sigma\,d\pi=\int F\,d\pi\). The image measures are Radon by Proposition 3.1(1), and so are \((\Delta^{\pm1}\circ\mathrm{pr}_1)\pi\) by Proposition 3.1(2). The uniqueness in Theorem 2.2 gives the four identities of measures. Densities that are continuous and positive do not change null sets or \(\sigma\)-finite sets (Proposition 3.1(2)). The integral formulas follow from Proposition 3.1(1) and (2). \(\square\)

For Borel functions \(f,g\) on \(G\), put
\[
f*g(x)=\int f(y)\,g(y^{-1}x)\,dy
\tag{14.1}
\]
at every \(x\) where the integral converges absolutely. For \(f,g\geq0\) the integral is defined at every \(x\), with values in \([0,\infty]\).

**Theorem 14.2.**

1. (*Tonelli for convolutions*) If \(f,g\geq0\) are Borel and vanish outside \(\sigma\)-finite sets, then \(f*g\) is \(\mu\)-a.e. Borel and \(\int f*g\,dx=\int f\,dx\int g\,dx\).
2. For \(f,g\in L^1(G)\), (14.1) converges absolutely for almost every \(x\), \(\|f*g\|_1\leq\|f\|_1\|g\|_1\), and the class of \(f*g\) depends only on the classes of \(f\) and \(g\). If one of the following integrals converges absolutely, so do the others, and
\[
f*g(x)=\int f(xy)g(y^{-1})\,dy=\int f(y^{-1})g(yx)\Delta(y^{-1})\,dy=\int f(xy^{-1})g(y)\Delta(y^{-1})\,dy.
\tag{14.2}
\]
3. With the involution \(f^*(x)=\Delta(x)^{-1}\overline{f(x^{-1})}\), \(L^1(G)\) is a Banach \(*\)-algebra: convolution is associative, \(\|f^*\|_1=\|f\|_1\), \(f^{**}=f\) and \((f*g)^*=g^**f^*\). Moreover \(L_z(f*g)=(L_zf)*g\) and \(R_z(f*g)=f*(R_zg)\).
4. Let \(1\leq p<\infty\), \(f\in L^1(G)\) and \(g\in L^p(G)\). Then \(f*g(x)\) converges absolutely for almost every \(x\), and \(\|f*g\|_p\leq\|f\|_1\|g\|_p\). If also \(\int|f|\Delta^{-1}\,dx<\infty\) (for instance if \(f\) has compact support, or if \(G\) is unimodular), then \(g*f(x)=\int g(xy^{-1})f(y)\Delta(y^{-1})\,dy\) converges absolutely for almost every \(x\), and
\[
\|g*f\|_p\leq\|\Delta^{-1}f\|_1^{1-1/p}\,\|f\|_1^{1/p}\,\|g\|_p .
\tag{14.3}
\]
For \(p=1\) the condition on \(f\) is not needed, and \(\|g*f\|_1\leq\|g\|_1\|f\|_1\).
5. If \(G\) is unimodular, \(1<p<\infty\), \(\frac1p+\frac1q=1\), \(f\in L^p(G)\) and \(g\in L^q(G)\), then \(f*g(x)\) converges absolutely for every \(x\), \(f*g\in C_0(G)\), and \(\|f*g\|_{\sup}\leq\|f\|_p\|g\|_q\).
6. (*Continuity of translation*) For \(1\leq p<\infty\) and \(f\in L^p(G)\), \(\|L_yf-f\|_p\to0\) and \(\|R_yf-f\|_p\to0\) as \(y\to e\).
7. Let \(f\in L^1(G)\) and \(g\in L^\infty(G)\) (Section 13). Then \(f*g(x)\) is defined for every \(x\), \(|f*g|\leq\|f\|_1\|g\|_\infty\), and \(\|L_z(f*g)-f*g\|_{\sup}\to0\) as \(z\to e\). If also \(\Delta^{-1}f\in L^1(G)\), then \(g*f(x)=\int g(y)f(y^{-1}x)\,dy\) is defined for every \(x\), \(|g*f|\leq\|g\|_\infty\|\Delta^{-1}f\|_1\), and \(\|R_z(g*f)-g*f\|_{\sup}\to0\). Without that condition \(g*f\) can be infinite everywhere (Exercise 16.4).

*Scope warning:* The second half of (7) cannot be asserted for every \(f\in L^1(G)\), with the bound \(\|g\|_\infty\|R_zf-f\|_1\); that version fails on every group that is not unimodular (Remark 14.3 and Exercise 16.4).

**Proof.** (1) The function \((x,y)\mapsto f(y)g(y^{-1}x)\) is \((f\boxtimes g)\circ\Theta_1\). The function \(f\boxtimes g\) vanishes outside a product of \(\sigma\)-finite sets, which is \(\sigma\)-finite by Theorem 5.1(6); so \((f\boxtimes g)\circ\Theta_1\) vanishes outside a \(\sigma\)-finite set by Lemma 14.1. By Tonelli's theorem 5.1(4) and Lemma 14.1, \(\int\big(\int f(y)g(y^{-1}x)\,dy\big)dx=\int(f\boxtimes g)\circ\Theta_1\,d\pi=\int f\boxtimes g\,d\pi=\int f\int g\).
(2) Apply (1) to \(|f|\) and \(|g|\): the inner integral is finite for almost every \(x\), and \(|f*g|\leq|f|*|g|\) gives the bound. By Fubini's theorem 5.1(5), \(f*g\) is \(\mu\)-a.e. Borel. Changing \(g\) on a null set \(N\) changes the integrand only on \(\Theta_1^{-1}(\{f\neq0\}\times N)\), which is \(\pi\)-null by Theorem 5.1(6) and Lemma 14.1; by Theorem 5.1(3) this affects, for almost every \(x\), only a null set of \(y\). The same holds for \(f\). For (14.2), fix \(x\). The substitution \(y\mapsto xy\), allowed by left invariance (Proposition 8.2(2)), turns (14.1) into the first form. The inversion formula (11.1), applied to \(h(y)=f(y^{-1})g(yx)\) and to \(h(y)=f(xy^{-1})g(y)\), turns (14.1) and the first form into the second and third forms. Each step preserves absolute convergence.
(3) For \(f,g\in C_c(G)\), \(f*g\) vanishes off \((\operatorname{supp}f)(\operatorname{supp}g)\), and \(|f*g(xz)-f*g(x)|\leq\|f\|_1\|R_zg-g\|_{\sup}\to0\) as \(z\to e\) by uniform continuity (Proposition 7.3), so \(f*g\in C_c(G)\). For \(f,g,h\in C_c(G)\) and fixed \(x\), the substitution \(w\mapsto y^{-1}w\) in the inner integral gives
\[
f*(g*h)(x)=\int f(y)\Big(\int g(y^{-1}z)h(z^{-1}x)\,dz\Big)dy,\qquad (f*g)*h(x)=\int\Big(\int f(y)g(y^{-1}z)\,dy\Big)h(z^{-1}x)\,dz ,
\]
and the integrand is in \(C_c(G\times G)\), so (4.1) makes them equal. For \(f,g\in C_c(G)\), a direct computation with \(\Delta(y)^{-1}\Delta(y^{-1}x)^{-1}=\Delta(x)^{-1}\) and the substitution \(y\mapsto xy\) gives \((f*g)^*=g^**f^*\). By the last formula of Theorem 11.1, \(\|f^*\|_1=\int\Delta(x)^{-1}|f(x^{-1})|\,dx=\|f\|_1\); and \(f^{**}(x)=\Delta(x)^{-1}\Delta(x^{-1})^{-1}f(x)=f(x)\). By (2), convolution is a bounded bilinear map on \(L^1\), and the involution is a conjugate-linear isometry; since \(C_c(G)\) is dense (Proposition 3.1(4)), the identities pass to \(L^1(G)\), which is complete. The translation rules follow from the substitution \(y\mapsto zy\) in (14.1), and directly for \(R_z\).
(4) The case \(p=1\) of the first claim is (2). Let \(1<p<\infty\) and \(\frac1p+\frac1q=1\). For fixed \(x\), Hölder's inequality for the measure \(|f(y)|\,dy\) gives
\[
\Big(\int|f(y)||g(y^{-1}x)|\,dy\Big)^p\leq\|f\|_1^{p-1}\int|f(y)||g(y^{-1}x)|^p\,dy .
\]
By (1) for \(|f|\) and \(|g|^p\in L^1\), the right side has integral \(\|f\|_1^{p-1}\|f\|_1\|g\|_p^p\) over \(x\). This gives absolute convergence almost everywhere and the bound. For \(g*f\), put \(w=|f|\Delta^{-1}\). The function \((x,y)\mapsto|g(xy^{-1})|^pw(y)\) is \((w\boxtimes|g|^p)\circ\Theta_2\), so by Tonelli's theorem and Lemma 14.1,
\[
\int\Big(\int|g(xy^{-1})|^pw(y)\,dy\Big)dx=\int w(y)\Delta(y)\,dy\int|g|^p=\|f\|_1\|g\|_p^p .
\]
For \(p=1\) this is the claim. For \(p>1\), Hölder's inequality for the measure \(w(y)\,dy\) of mass \(\|\Delta^{-1}f\|_1\) gives \(\big(\int|g(xy^{-1})|w(y)\,dy\big)^p\leq\|\Delta^{-1}f\|_1^{p-1}\int|g(xy^{-1})|^pw(y)\,dy\), and integrating in \(x\) gives (14.3). If \(f\) vanishes off a compact set \(K\), then \(\|\Delta^{-1}f\|_1\leq(\sup_K\Delta^{-1})\|f\|_1\), and (14.3) gives \(\|g*f\|_p\leq(\sup_K\Delta^{(1/p)-1})\|f\|_1\|g\|_p\).
(5) For every \(x\), Hölder's inequality gives \(|f*g(x)|\leq\|f\|_p\big(\int|g(y^{-1}x)|^q\,dy\big)^{1/q}\). By (11.1) and unimodularity, \(\int|g(y^{-1}x)|^q\,dy=\int|g(yx)|^q\Delta(y)^{-1}\,dy=\|g\|_q^q\). For \(f,g\in C_c(G)\), \(f*g\in C_c(G)\) by (3). For general \(f,g\), take \(f_n,g_n\in C_c(G)\) with \(f_n\to f\) in \(L^p\) and \(g_n\to g\) in \(L^q\) (Proposition 3.1(4)). The bound gives \(f_n*g_n\to f*g\) uniformly, and a uniform limit of functions in \(C_c(G)\) lies in \(C_0(G)\). The endpoint cases fail on every noncompact \(G\): for \(f\geq0\) with \(\int f=1\) and \(g\equiv1\), \(f*g\equiv1\notin C_0(G)\).
(6) Fix a compact neighbourhood \(V\) of \(e\). For \(g\in C_c(G)\) and \(y\in V\), \(L_yg\) and \(R_yg\) vanish outside the compact set \(K=V(\operatorname{supp}g)\cup(\operatorname{supp}g)V^{-1}\), so \(\|L_yg-g\|_p\leq\mu(K)^{1/p}\|L_yg-g\|_{\sup}\to0\) by uniform continuity (Proposition 7.3), and the same for \(R_y\). For \(f\in L^p\) and \(\varepsilon>0\), choose \(g\in C_c(G)\) with \(\|f-g\|_p<\varepsilon\). Since \(\|L_y\|=1\), and \(\|R_y\|=\Delta(y)^{-1/p}\leq C\) on \(V\) by Theorem 10.1(3) and the continuity of \(\Delta\), we get \(\|R_yf-f\|_p\leq(C+1)\varepsilon+\|R_yg-g\|_p\), and similarly for \(L_y\).
(7) Left and right translations and inversion map Borel sets to Borel sets and preserve null sets and \(\sigma\)-finite sets (Theorem 10.1(1) and Corollary 11.2(1)). Hence they map locally Borel and locally null sets to sets of the same kind: for such a map \(\theta\) and \(\mu(F)<\infty\), the set \(\theta^{-1}(F)\) is covered by countably many sets of finite measure, so \(\theta(E)\cap F=\theta\big(E\cap\theta^{-1}(F)\big)\) is Borel (null) when \(E\) is locally Borel (locally null). The map \(y\mapsto y^{-1}x\) and its inverse \(z\mapsto xz^{-1}\) are composites of an inversion and a translation, so \(y\mapsto g(y^{-1}x)\) is locally measurable and bounded by \(\|g\|_\infty\) locally almost everywhere. As in the proof of Theorem 13.3(2), multiplying by \(f\) gives an integrable function with \(|f*g(x)|\leq\|f\|_1\|g\|_\infty\). By (3), \(L_z(f*g)-f*g=(L_zf-f)*g\), and \(\|L_zf-f\|_1\to0\) by (6). For \(g*f\), the substitutions of (2) give \(\int|g(y)||f(y^{-1}x)|\,dy\leq\|g\|_\infty\int|f(y^{-1}x)|\,dy=\|g\|_\infty\int|f(y)|\Delta(y)^{-1}\,dy\). Also \(R_z(g*f)-g*f=g*(R_zf-f)\), and \(\Delta^{-1}R_zf=\Delta(z)R_z(\Delta^{-1}f)\), so
\[
\|\Delta^{-1}(R_zf-f)\|_1\leq|\Delta(z)-1|\,\|R_z(\Delta^{-1}f)\|_1+\|R_z(\Delta^{-1}f)-\Delta^{-1}f\|_1\to0
\]
by (6) applied to \(\Delta^{-1}f\in L^1\). \(\square\)

**Remark 14.3** (The factor \(\Delta^{-1}\) in (7) is needed). In the second half of (7) the bound is \(|R_z(g*f)-g*f|\leq\|g\|_\infty\|\Delta^{-1}(R_zf-f)\|_1\), with \(\Delta^{-1}(R_zf-f)\) where one might expect \(R_zf-f\). This cannot be improved. For \(h\in L^1\) and fixed \(x\), the third form of (14.2) gives \(g*h(x)=\int g(xy^{-1})h(y)\Delta(y)^{-1}\,dy\). The choice \(g(w)=\overline{\operatorname{sgn}h(w^{-1}x)}\) shows that the supremum of \(|g*h(x)|\) over \(\|g\|_\infty\leq1\) is \(\|\Delta^{-1}h\|_1\), which exceeds \(\|h\|_1\) whenever \(h\neq0\) lives where \(\Delta<1\). Such \(h=R_zf-f\) occur on every group that is not unimodular: take \(f\in C_c^+(G)\) supported in the nonempty open set \(\{\Delta<1\}\), and \(z\) with \(\Delta(z)>1\). Then \(R_zf\) is supported in \((\operatorname{supp}f)z^{-1}\), where \(\Delta\) is smaller still, and \(R_zf\neq f\) because \(\int R_zf=\Delta(z)^{-1}\int f\). So the bound \(\|g\|_\infty\|R_zf-f\|_1\) fails for this \(f\), this \(z\) and a suitable \(g\). The extra hypothesis \(\Delta^{-1}f\in L^1\) cannot be dropped either: Exercise 16.4 gives \(f\in L^1\) on the \(ax+b\) group with \(1*f\equiv\infty\). For unimodular groups \(\Delta\equiv1\), and nothing changes. The first half of (7), and (4) for \(f*g\), hold for all groups.

### The full Young inequality on a unimodular group

**Theorem 14.4 (Young).** Suppose \(G\) is unimodular, \(1\leq p,q,r\leq\infty\), and
\[
\frac1p+\frac1q=1+\frac1r,
\]
where \(1/\infty=0\). For \(f\in L^p(G)\) and \(g\in L^q(G)\), convolution defines an element of \(L^r(G)\), with
\[
\|f*g\|_r\leq\|f\|_p\|g\|_q.
\tag{14.4}
\]
It converges absolutely almost everywhere if \(r<\infty\), and at every point if \(r=\infty\), using locally bounded representatives at the \(L^\infty\) endpoints. Fischer and Ruzhansky state this general inequality in their freely accessible monograph. Here is a direct proof, requiring no interpolation theorem.

*Proof.* If \(p=1\), the relation gives \(q=r\), and Theorem 14.2(4),(7) gives the result. If \(q=1\), then \(p=r\); the same theorem applies with its modular factors equal to one. These include \(r=1\) and all cases with an infinite input exponent. If \(r=\infty\) and \(1<p,q<\infty\), the exponents are conjugate. Hölder and unimodular inversion give, for every \(x\),
\[
\int_G|f(y)g(y^{-1}x)|\,dy
\leq\|f\|_p\left(\int_G|g(y^{-1}x)|^q\,dy\right)^{1/q}
=\|f\|_p\|g\|_q.
\]
These cases are unchanged by alterations on null sets, since translations and inversion preserve null sets.

It remains to consider \(1<p,q<r<\infty\). The exponent relation implies \(p<r\) and \(q<r\). Apply Hölder with the three exponents
\[
r,\qquad \frac{p}{1-p/r},\qquad \frac{q}{1-q/r},
\]
whose reciprocals sum to one, to the product
\[
\bigl(|f(y)|^p|g(y^{-1}x)|^q\bigr)^{1/r}
|f(y)|^{1-p/r}|g(y^{-1}x)|^{1-q/r}.
\]
This gives
\[
|f*g(x)|^r
\leq \|f\|_p^{r-p}\|g\|_q^{r-q}
\int_G|f(y)|^p|g(y^{-1}x)|^q\,dy.
\]
Integrating in \(x\), left translation gives
\[
\int_G\int_G|f(y)|^p|g(y^{-1}x)|^q\,dy\,dx
=\|f\|_p^p\|g\|_q^q.
\]
These interchanges do not impose sigma-finiteness on \(G\). The nonzero supports of \(f\) and \(g\) are sigma-finite because their finite powers are integrable. Their product is sigma-finite by Theorem 5.1(6), and its inverse image under \(\Theta_1\) is sigma-finite by Lemma 14.1. The sigma-finite Tonelli theorem therefore applies to the displayed integrand, and Fubini gives a measurable convolution where it is absolutely convergent. The finite double integral also makes the inner integral finite almost everywhere. The three-factor estimate then proves absolute convergence there and (14.4). If either input norm is zero, apply the same Tonelli calculation to obtain the zero convolution class. \(\square\)

The unimodular hypothesis belongs to this symmetric form of the inequality. The preceding weighted estimates remain the applicable bounds on a general group; the affine counterexample in Exercise 16.4 explains why their modular factors cannot be discarded.

## 15. Approximate identities

**Theorem 15.1.** Let the neighbourhoods \(U\) of \(e\) be directed by reverse inclusion.

1. For every neighbourhood \(U\) of \(e\) there is \(\psi_U\in C_c(G)\) with \(\psi_U\geq0\), \(\operatorname{supp}\psi_U\subseteq U\), \(\int\psi_U=1\) and \(\psi_U(x^{-1})=\psi_U(x)\).
2. Let \((\psi_U)\) be any family with \(\psi_U\geq0\), \(\int\psi_U=1\), and \(\psi_U\) vanishing outside a compact subset of \(U\) (continuity is not required). For \(1\leq p<\infty\) and \(f\in L^p(G)\),
\[
\|\psi_U*f-f\|_p\leq\sup_{y\in U}\|L_yf-f\|_p\longrightarrow0 .
\tag{15.1}
\]
If \(f\) is bounded with \(\|L_yf-f\|_{\sup}\to0\) as \(y\to e\), then \(\|\psi_U*f-f\|_{\sup}\to0\).
3. If moreover \(\psi_U(x^{-1})=\psi_U(x)\), then \(\|f*\psi_U-f\|_p\leq\sup_{y\in U}\|R_yf-f\|_p\to0\), and \(\|f*\psi_U-f\|_{\sup}\to0\) for bounded \(f\) with \(\|R_yf-f\|_{\sup}\to0\).
4. (*Weak-integral form*) For \(\psi\in L^1(G)\) and \(\xi,\eta\in L^2(G)\),
\[
\langle\psi*\xi,\eta\rangle=\int\psi(s)\,\langle L_s\xi,\eta\rangle\,ds ,
\tag{15.2}
\]
where \(s\mapsto\langle L_s\xi,\eta\rangle\) is continuous and bounded by \(\|\xi\|\|\eta\|\). So the operator \(\xi\mapsto\psi*\xi\) is the weak integral \(\int\psi(s)\lambda(s)\,ds\) of the left regular representation, its norm is at most \(\|\psi\|_1\), and \(\psi_U*\xi\to\xi\) in \(L^2\) for every \(\xi\).

**Proof.** (1) The set \(U'=\operatorname{int}U\cap(\operatorname{int}U)^{-1}\) is an open neighbourhood of \(e\). By (T2) choose \(\varphi\) with \(\{e\}\prec\varphi\prec U'\), put \(\varphi'=\varphi+\check\varphi\), which vanishes off \(\operatorname{supp}\varphi\cup(\operatorname{supp}\varphi)^{-1}\subseteq U'\), and \(\psi_U=\varphi'/\int\varphi'\); the integral is positive by Proposition 9.1.
(2) Let \(C\) be a compact set outside of which \(\psi=\psi_U\) vanishes. For almost every \(x\), (14.1) converges absolutely by Theorem 14.2(4), and since \(\int\psi=1\), \(\psi*f(x)-f(x)=\int\psi(y)\big(f(y^{-1}x)-f(x)\big)dy\). Hölder's inequality for the probability measure \(\psi(y)\,dy\) gives \(|\psi*f(x)-f(x)|^p\leq\int\psi(y)|f(y^{-1}x)-f(x)|^p\,dy\). The function \((x,y)\mapsto\psi(y)|f(y^{-1}x)-f(x)|^p\) is Borel and vanishes outside \((\{f\neq0\}\times C)\cup\Theta_1^{-1}(C\times\{f\neq0\})\), which is \(\sigma\)-finite by Theorem 5.1(6) and Lemma 14.1. By Tonelli's theorem,
\[
\|\psi*f-f\|_p^p\leq\int\psi(y)\Big(\int|f(y^{-1}x)-f(x)|^p\,dx\Big)dy=\int\psi(y)\,\|L_yf-f\|_p^p\,dy\leq\sup_{y\in U}\|L_yf-f\|_p^p ,
\]
which tends to \(0\) by the continuity of translation (Theorem 14.2(6)). For the uniform statement, \(|\psi*f(x)-f(x)|\leq\int\psi(y)|L_yf(x)-f(x)|\,dy\leq\sup_{y\in U}\|L_yf-f\|_{\sup}\) at every \(x\).
(3) By the first form of (14.2) and the symmetry of \(\psi\), \(f*\psi(x)=\int f(xy)\psi(y)\,dy\), so \(f*\psi(x)-f(x)=\int\psi(y)(R_yf(x)-f(x))\,dy\); the integral converges absolutely for almost every \(x\) by Theorem 14.2(4), since \(\psi\) has compact support. Repeat the argument of (2), with \(\Theta_3\) in place of \(\Theta_1\) and \(\int|f(xy)-f(x)|^p\,dx=\|R_yf-f\|_p^p\).
(4) The function \((x,s)\mapsto\psi(s)\xi(s^{-1}x)\overline{\eta(x)}\) is Borel, vanishes outside a \(\sigma\)-finite set (as in (2)), and by Tonelli's theorem and the Cauchy–Schwarz inequality in \(x\) it is \(\pi\)-integrable with integral of its absolute value at most \(\int|\psi(s)|\,\|L_s\xi\|\,\|\eta\|\,ds=\|\psi\|_1\|\xi\|\|\eta\|\). Fubini's theorem 5.1(5) gives (15.2). Continuity: \(|\langle L_s\xi-L_{s_0}\xi,\eta\rangle|\leq\|L_{s_0^{-1}s}\xi-\xi\|\,\|\eta\|\to0\) by Theorem 14.2(6). The norm bound is Theorem 14.2(4) with \(p=2\), and the convergence is (2). \(\square\)

*Units.* If \(G\) is discrete (with counting measure), \(\delta=1_{\{e\}}\) satisfies \(\delta*f=f*\delta=f\). If \(G\) is not discrete, \(L^1(G)\) has no unit, which is why approximate identities are needed. Indeed, suppose \(u*f=f\) for all \(f\in L^1(G)\). Taking \(f=\psi_U\) symmetric, \(\psi_U=u*\psi_U\to u\) in \(L^1\) by (3). For a compact \(K\) with \(e\notin K\), \(\int_K|\psi_U|=0\) as soon as \(U\cap K=\varnothing\), so \(\int_K|u|=0\). By inner regularity on the \(\sigma\)-finite set \(\{u\neq0\}\) (Proposition 2.3(2)), \(u=0\) almost everywhere off \(\{e\}\). And \(\mu(\{e\})=0\): otherwise every point would have the same positive measure (by left invariance), a compact neighbourhood of \(e\) would be finite by (R1), and \(\{e\}\) would be open. So \(u=0\) almost everywhere, and \(u*f=0\neq f\) for \(f\neq0\), a contradiction.

A family as in (1) is a *compactly supported approximate identity*. Its translates behave well: for \(g\in G\), \((L_g\psi_U)*\xi=L_g(\psi_U*\xi)\) by Theorem 14.2(3), so convolution by \(L_g\psi_U\) is \(\lambda(g)\) composed with convolution by \(\psi_U\).

## 16. Exercises

**Exercise 16.1** (A density that vanishes on a closed set). On \(G=\mathbb R\times\mathbb R_d\) with Haar measure \(\mu\) (Example 13.4), let \(\varphi(x,d)=|x|\) and \(\nu(E)=\int_E\varphi\,d\mu\). Show that \(\nu\) is a Borel measure, finite on compact sets, with \(\nu(Y)=0\) for \(Y=\{0\}\times\mathbb R_d\) but \(\nu(U)=\infty\) for every open \(U\supseteq Y\). Conclude that the positivity of the density in Proposition 3.1(2) cannot be dropped.

*Solution.* \(\nu\) is a measure because \(\varphi\) is a nonnegative Borel function. A compact set \(K\) meets finitely many lines and \(\varphi\) is bounded on it, so \(\nu(K)\leq\max_K\varphi\cdot\mu(K)<\infty\). Since \(\varphi=0\) on \(Y\), \(\nu(Y)=0\). If \(U\supseteq Y\) is open, then for each \(d\) there is \(\delta_d>0\) with \((-\delta_d,\delta_d)\times\{d\}\subseteq U\), and \(\nu\big((-\delta_d,\delta_d)\times\{d\}\big)=\int_{-\delta_d}^{\delta_d}|x|\,dx=\delta_d^2>0\), because \(\mu\) is Lebesgue measure on each line. These sets are disjoint and uncountably many, so, as in the proof of Proposition 13.1(2), \(\nu(U)=\infty\). So \(\nu\) fails (R2) at \(Y\).

**Exercise 16.2** (Closed ideals of \(L^1(G)\)). Let \(\mathcal J\subseteq L^1(G)\) be a closed subspace. Show that \(\mathcal J\) is a left ideal (\(g*f\in\mathcal J\) for \(g\in L^1\), \(f\in\mathcal J\)) exactly when \(L_x\mathcal J\subseteq\mathcal J\) for all \(x\), and a right ideal exactly when \(R_x\mathcal J\subseteq\mathcal J\) for all \(x\).

*Solution.* *Left, only if.* For \(f\in\mathcal J\) and \(x\in G\), \(L_x(\psi_U*f)=(L_x\psi_U)*f\in\mathcal J\) by Theorem 14.2(3), and \(L_x(\psi_U*f)\to L_xf\) in \(L^1\) by Theorem 15.1(2), since \(L_x\) is isometric. As \(\mathcal J\) is closed, \(L_xf\in\mathcal J\).
*Left, if.* Since \(C_c(G)\) is dense in \(L^1\) and \(\|g*f\|_1\leq\|g\|_1\|f\|_1\), it suffices to take \(g\in C_c(G)\). Let \(K=\operatorname{supp}g\) and \(\varepsilon>0\). By Theorem 14.2(6), \(y\mapsto L_yf\) is continuous into \(L^1\), so each \(y\in K\) has an open neighbourhood \(O_y\) with \(\|L_{y'}f-L_yf\|_1<\varepsilon\) for \(y'\in O_y\). Cover \(K\) by \(O_{y_1},\dots,O_{y_n}\), and let \(E_j=(K\cap O_{y_j})\setminus\bigcup_{i<j}O_{y_i}\). Put \(h=\sum_j\big(\int_{E_j}g\big)L_{y_j}f\in\mathcal J\). For almost every \(x\), \(g*f(x)-h(x)=\sum_j\int_{E_j}g(y)\big(f(y^{-1}x)-f(y_j^{-1}x)\big)dy\). The integrands vanish outside \(\sigma\)-finite sets (Lemma 14.1), so Tonelli's theorem gives \(\|g*f-h\|_1\leq\sum_j\int_{E_j}|g(y)|\,\|L_yf-L_{y_j}f\|_1\,dy\leq\varepsilon\|g\|_1\). Hence \(g*f\in\overline{\mathcal J}=\mathcal J\).
*Right.* If \(\mathcal J\) is a right ideal, take symmetric \(\psi_U\) (Theorem 15.1(1)); then \(R_x(f*\psi_U)=f*(R_x\psi_U)\in\mathcal J\), and \(f*\psi_U\to f\) by Theorem 15.1(3), while \(R_x\) is bounded on \(L^1\). Conversely, for \(g\in C_c(G)\) the first form of (14.2) reads \(f*g(x)=\int g(y^{-1})R_yf(x)\,dy\), and the same Riemann-sum argument, with the continuous map \(y\mapsto R_yf\) and \(\Theta_3\) for the \(\sigma\)-finiteness, shows \(f*g\in\mathcal J\).

**Exercise 16.3** (The regular representations). Show that \(\lambda(g)=L_g\) and \(\rho(g)=\Delta(g)^{1/2}R_g\) are unitary representations of \(G\) on \(L^2(G)\), continuous for the strong operator topology, and that \(\lambda(g)\rho(h)=\rho(h)\lambda(g)\).

*Solution.* \(\lambda(g)\) is isometric by left invariance (Proposition 8.2(2)), and \(\rho(g)\) is isometric because \(\|R_g\xi\|_2=\Delta(g)^{-1/2}\|\xi\|_2\) (Theorem 10.1(3)). Since \(L_{gh}=L_gL_h\), \(R_{gh}=R_gR_h\) and \(\Delta\) is multiplicative, both are homomorphisms, so each \(\lambda(g)\), \(\rho(g)\) has the inverse \(\lambda(g^{-1})\), \(\rho(g^{-1})\) and is unitary. They commute: \(L_gR_h\xi(t)=\xi(g^{-1}th)=R_hL_g\xi(t)\). At \(e\), \(\|\lambda(g)\xi-\xi\|\to0\) by Theorem 14.2(6), and \(\|\rho(g)\xi-\xi\|\leq|\Delta(g)^{1/2}-1|\,\|R_g\xi\|+\|R_g\xi-\xi\|\to0\) by the continuity of \(\Delta\) (Theorem 10.1(2)) and Theorem 14.2(6). At \(g_0\), \(\|\lambda(g)\xi-\lambda(g_0)\xi\|=\|\lambda(g_0^{-1}g)\xi-\xi\|\), and likewise for \(\rho\).

**Exercise 16.4** (The \(ax+b\) group: left against right, and a failure of \(L^\infty*L^1\)). On the \(ax+b\) group of Example 11.3, with \(d\mu=a^{-2}da\,db\), \(d\tilde\mu=a^{-1}da\,db\) and \(\Delta(a,b)=1/a\):
(a) find Borel sets \(E,E'\) with \(\mu(E)<\infty=\tilde\mu(E)\) and \(\tilde\mu(E')<\infty=\mu(E')\), and conclude that neither of \(L^2(\mu)\), \(L^2(\tilde\mu)\) contains the other;
(b) for \(g\equiv1\in L^\infty(G)\) and \(f=1_E\) with \(E\) from (a), show \(f\in L^1(\mu)\) and \(g*f(x)=\infty\) for every \(x\).

*Solution.* By Proposition 3.1(2), \(\mu\) and \(\tilde\mu\) are the measures with densities \(a^{-2}\) and \(a^{-1}\) with respect to the Radon product of Lebesgue measures on \((0,\infty)\times\mathbb R\): both sides are Radon and integrate \(C_c\) alike. Measures of regions are then iterated integrals by Tonelli's theorem 5.1(4). (a) Let \(E=\{a>1,\ 0<b<1\}\): \(\mu(E)=\int_1^\infty a^{-2}\,da=1\) and \(\tilde\mu(E)=\int_1^\infty a^{-1}\,da=\infty\). Let \(E'=\{0<a<1,\ 0<b<a\}\): \(\tilde\mu(E')=\int_0^1a\cdot a^{-1}\,da=1\) and \(\mu(E')=\int_0^1a\cdot a^{-2}\,da=\infty\). So \(1_E\in L^2(\mu)\setminus L^2(\tilde\mu)\) and \(1_{E'}\in L^2(\tilde\mu)\setminus L^2(\mu)\). Corollary 11.2(3) gives isometries between the two spaces, but they are different spaces. (b) \(\|f\|_1=\mu(E)=1\). For every \(x\), left invariance and (11.1) give \(g*f(x)=\int f(y^{-1}x)\,dy=\int f(y^{-1})\,dy=\int f\Delta^{-1}\,d\mu=\tilde\mu(E)=\infty\). Here \(\Delta^{-1}f\notin L^1\), which is exactly the extra hypothesis in Theorem 14.2(7).

## Results used from other lessons

*Topology*, from [The Stone–Weierstrass theorem for functions vanishing at infinity](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity) and from [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian).

- **Compact closures** ([Proposition 4.2(2) of the Stone–Weierstrass lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity#oa-fnd-sw-15)). If \(K\) is a compact subset of an LCH space and \(V\) is a neighbourhood of \(K\), some open \(U\supseteq K\) has compact closure contained in \(V\). This is (T1).
- **Urysohn's lemma** ([Corollary 5.2 of the Stone–Weierstrass lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity#oa-fnd-sw-16)). If \(K\) is compact, \(B\) is closed and \(K\cap B=\varnothing\) in an LCH space \(X\), some \(f\in C_c(X)\) with \(0\leq f\leq1\) equals \(1\) on \(K\) and \(0\) on \(B\).
- **The Stone–Weierstrass theorem** ([Theorem 10.1 of that lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity#oa-fnd-sw-09)). Let \(X\) be an LCH space and \(A\) a subalgebra of \(C_0(X)\) that is closed under complex conjugation, separates the points of \(X\), and contains for each \(x\in X\) a function that does not vanish at \(x\). Then \(A\) is dense in \(C_0(X)\). It is used only in Example 12.2.
- **Compact Tietze extension** (Proposition 16.1(2) of the Stone–Weierstrass lesson). On a compact Hausdorff space, a continuous real function on a closed subset extends continuously with the same supremum bound; real and imaginary extensions give the complex version. Its proof uses the compact Stone–Weierstrass theorem and a uniformly summable correction series. This supplies compact extension whenever needed; no normality of an arbitrary LCH space is assumed.
- **Tychonoff's theorem** (Theorem 2.3 of the lesson on weak topologies). Every product of compact spaces is compact in the product topology.

*Measure theory*, from [Measure and Hilbert space tools for Haar integration](measure-and-hilbert-space-tools.md): Theorem 1.1 proves Carathéodory; Section 2 proves measurability of sequential limits; Theorems 2.1–2.2 prove monotone and dominated convergence; Theorems 3.1–3.2 prove Hölder, completeness and simple approximation; Theorems 4.1–4.2 prove Radon–Nikodym and the sigma-finite dual of \(L^1\). Fremlin is a complementary human source for these classical statements.

- **Carathéodory's theorem** [the preceding tools lesson, Theorem 1.1](measure-and-hilbert-space-tools.md#1-from-an-outer-measure-to-a-measure). For an outer measure \(\mu^*\) on \(X\), the sets \(A\) with \(\mu^*(Y)=\mu^*(Y\cap A)+\mu^*(Y\setminus A)\) for every \(Y\subseteq X\) form a \(\sigma\)-algebra on which \(\mu^*\) is countably additive. To check the condition it suffices to show \(\mu^*(Y)\geq\mu^*(Y\cap A)+\mu^*(Y\setminus A)\) when \(\mu^*(Y)<\infty\): the reverse inequality is subadditivity, and the case \(\mu^*(Y)=\infty\) is trivial.
- **Measurable functions** [Fremlin]. The supremum, the infimum and the pointwise limit of a sequence of Borel functions with values in \(\mathbb R\) or in \([0,\infty]\) are Borel.
- **Convergence theorems.** Monotone convergence for functions with values in \([0,\infty]\) [Fremlin], and for integrable functions [Fremlin]. Dominated convergence [Fremlin]: if \(f_n\to f\) almost everywhere and \(|f_n|\leq g\) with \(g\) integrable, then \(\int f_n\,d\mu\to\int f\,d\mu\); applied to \(|f_n-f|\leq2g\) it gives \(\int|f_n-f|\,d\mu\to0\).
- **\(L^p\) spaces.** Hölder's inequality [Fremlin]. For \(1\leq p<\infty\), \(L^p(\mu)\) is complete [Fremlin], and the simple functions in \(L^p(\mu)\) are dense in it [Fremlin].
- **The dual of \(L^1\)** [Fremlin]. If \(\mu\) is \(\sigma\)-finite, every bounded linear functional \(\Phi\) on \(L^1(\mu)\) has the form \(\Phi(g)=\int fg\,d\mu\) for a unique \(f\in L^\infty(\mu)\), and \(\|\Phi\|=\|f\|_\infty\).
- **The Radon–Nikodym theorem** [Fremlin]. Let \(\mu\) and \(\nu\) be measures on the same \(\sigma\)-algebra, \(\nu\) finite and \(\mu\) \(\sigma\)-finite, with \(\nu(E)=0\) whenever \(\mu(E)=0\). Then \(\nu(E)=\int_Eh\,d\mu\) for an integrable \(h\geq0\). In Theorem 13.3(5) both measures are \(\sigma\)-finite on the set considered; the set is split into countably many Borel pieces of finite measure for both, and the theorem is applied on each piece.
- **Substitution in Riemann integrals.** If \(\phi\colon[\alpha,\beta]\to\mathbb R\) is continuously differentiable and \(f\) is continuous on \(\phi([\alpha,\beta])\), then \(\int_{\phi(\alpha)}^{\phi(\beta)}f(u)\,du=\int_\alpha^\beta f(\phi(t))\,\phi'(t)\,dt\). The integral identity is proved in [Measure and Hilbert space tools for Haar integration](measure-and-hilbert-space-tools.md), Lemma 6.1, from the elementary differential-calculus prerequisites.

*Hilbert spaces*, from [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators).

- **Hilbert tensor products** (Theorem 8.1). For Hilbert spaces \(H\) and \(K\) there is a Hilbert space \(H\otimes K\) with a bilinear map \((\xi,\eta)\mapsto\xi\otimes\eta\) such that \(\langle\xi\otimes\eta,\xi'\otimes\eta'\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle\) and the elementary tensors span a dense subspace.
- **Multiplication operators on \(\sigma\)-finite spaces** (Theorem 9.1). For a \(\sigma\)-finite measure space \((Z,\nu)\), the operators \(m_f\xi=f\xi\) on \(L^2(\nu)\) with \(f\in L^\infty(\nu)\) form an algebra that is maximal abelian: every bounded operator on \(L^2(\nu)\) that commutes with all \(m_f\) is itself some \(m_f\).

## Where this leads

- The lesson *The Plancherel weight and Fourier coefficients of a locally compact group*, in the course on modular theory and weights, is built on this one and, like it, works for every locally compact group. It uses the normalization (10.1) of the modular function and the inversion formula (11.1); the regular representations of Exercise 16.3, whose strong continuity rests on Proposition 7.3 and Theorem 14.2(6), and the conjugation \(J\) of Corollary 11.2(2); the density of \(C_c(G)\) in \(L^2(G)\) (Proposition 3.1(4)) and the core of Corollary 11.2(5); the approximate identities and weak integrals of Theorem 15.1; the identification \(L^2(G)\otimes L^2(G)\cong L^2(G\times G,\mu\hat\times\mu)\) of Theorem 6.2, with the operators \(m_a\otimes1\) of part (4), the unitary \(W\) of Proposition 12.1, and Tonelli's theorem 5.1(4) for norm computations on elementary tensors; and the von Neumann algebra \(L^\infty(G)\) of Theorem 13.3(4). The unitarity of \(W\) can also be checked on compactly supported tensors, one \(s\) at a time, and then extended by density; Theorem 6.2(3) is what justifies working with one \(s\) at a time.
- Tensor products of \(L^\infty(G)\) with other von Neumann algebras are spatial tensor products; see the lesson [Spatial tensor products of von Neumann algebras](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras).
- For a Radon measure that is not \(\sigma\)-finite and does not come from a group, the maximal abelian property of \(L^\infty\) (Theorem 13.3(4) for Haar measure) needs a decomposition of the space into disjoint compact pieces; for Haar measure, the open \(\sigma\)-compact cosets of Section 13 play that role. The lesson on vector-valued functions and preduals constructs [the decomposition](course:measurable-fields-and-direct-integrals/vector-valued-functions-tensor-products-with-lp-and-preduals#oa-fnd-vv-03) and proves [the maximal abelian property for every Radon measure](course:measurable-fields-and-direct-integrals/vector-valued-functions-tensor-products-with-lp-and-preduals#oa-fnd-vv-08).

## References

- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1, 2 and 4, [author’s freely accessible text and editable TeX](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm). Volume 4 uses complete, locally determined Radon measures; Proposition 13.7 relates that convention to ours.
- [van Doorn] F. van Doorn, *Formalized Haar Measure*, 2021, [arXiv version 1](https://arxiv.org/abs/2102.07636v1). The paper constructs Haar measure on arbitrary LCH groups; its uniqueness proof assumes second countability. The [current mathlib uniqueness development](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Haar/Unique.html) also distinguishes regularity hypotheses.

- [Fischer–Ruzhansky] V. Fischer and M. Ruzhansky, [*Quantization on Nilpotent Lie Groups*](https://biblio.ugent.be/publication/8585474), Birkhäuser, 2016, freely accessible under CC BY 4.0. Its Heisenberg and homogeneous-group treatment complements Example 12.3; its convolution discussion includes the full Young bound of Theorem 14.4. The calculations and proof here are independently written.

## Terms for the marked Fremlin adaptations

THE WORK IS PROVIDED "AS IS," AND COMES WITH ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED, TO THE EXTENT PERMITTED BY APPLICABLE LAW. The full warranty and liability terms are in the accompanying Design Science License.
