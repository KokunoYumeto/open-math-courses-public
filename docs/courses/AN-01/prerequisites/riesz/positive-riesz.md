# Haar measure on locally compact groups

*Originally written by Claude Opus 5.5 (Anthropic), September 2026, with a separate historical AI spot-check of that text. Repaired and self-checked by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. The current edition has no separately recorded independent AI or human review. Original programme content is dedicated under CC0.*

**Bounded prerequisite selection (October 2026).** This companion selects the original header and credits (lines 1–19) and the full conventions and positive Riesz argument (lines 21–96), including all six construction steps, regularity on sigma-finite sets, compactly supported density and the positive-functional norm argument. Original introductory references to later parts of the full Haar lesson are retained as source context. The required topology and measure proofs are available locally in [topology-cutoffs](topology-cutoffs.md) and [measure-tools](measure-tools.md). References to later Haar sections, Hilbert spaces and arbitrary-product results concern unselected material. The later Fremlin Design Science License supplement is not included. The selected source prose and mathematics are unchanged apart from link destinations and line-ending normalization. Selection and link repair: GPT-6.1 Sol (OpenAI), Ultra reasoning effort, for the AN-01 course project.

This lesson constructs Haar measure on an arbitrary locally compact group and develops the measure theory that goes with it. Sections 2–6 work on locally compact spaces. They prove the Riesz representation theorem for Radon measures, treat image measures and densities, build the product of two Radon measures with its Tonelli and Fubini theorems, and identify \(L^2\) of a product with a Hilbert tensor product. Sections 7–11 turn to groups: topological groups, existence and uniqueness of Haar measure, the modular function, and the inversion formula. Sections 12–15 treat products of groups, groups that are not \(\sigma\)-compact, convolution, and approximate identities. Section 16 has exercises with solutions.

No countability assumption is made anywhere. The group need not be \(\sigma\)-compact, second countable or unimodular, and its Haar measure need not be \(\sigma\)-finite. This generality needs care: a Borel set of infinite measure can have only null compact subsets, and Fubini's theorem can fail. Section 13 shows what goes wrong, and the rest of the lesson is arranged so that it does no harm.

Haar measure makes a locally compact group \(G\) into a measure space on which \(G\) acts by translations. Then \(L^1(G)\) is a Banach \(*\)-algebra under convolution, and \(L^2(G)\) carries the left and right regular representations. These objects are the starting point of abstract harmonic analysis, and of the group von Neumann algebras studied in the course on modular theory and weights.

The lesson builds on four sources, cited where they are used:
- [Measure and Hilbert space tools for Haar integration](measure-tools.md), Theorems 1.1–4.2, for the full measure-theory proofs; the measure convention is compared with Fremlin below;
- [The Stone–Weierstrass theorem for functions vanishing at infinity](topology-cutoffs.md), for locally compact spaces and Urysohn's lemma;
- [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html), for Tychonoff's theorem;
- [Hilbert spaces and compact operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html), for Hilbert tensor products and multiplication operators.

The exact statements are collected at the end, under "Results used from other lessons". Core preparation is [Point-Set Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90); [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) provides Fremlin’s broader measure-theory setting. The arbitrary-product and Hilbert-space proofs used here are the advanced programme results named above.

Freely accessible complementary treatments are Fremlin’s [Measure Theory](https://www1.essex.ac.uk/maths/people/fremlin/mtcont.htm) and F. van Doorn’s [Formalized Haar Measure](https://arxiv.org/abs/2102.07636v1). Fischer and Ruzhansky’s freely accessible [*Quantization on Nilpotent Lie Groups*](https://biblio.ugent.be/publication/8585474) supplies further convolution and Heisenberg-group examples. The historical development from Haar and von Neumann to Weil and Cartan is discussed in F. van Doorn’s paper; the original accessible von Neumann and Cartan papers are linked below.

## 1. Conventions

*Spaces.* An *LCH space* is a Hausdorff space that is locally compact. Its compact subsets are closed. \(C_c(X)\) is the space of continuous complex functions with compact support, \(C_c^+(X)\) is the set of \(f\in C_c(X)\) with \(f\geq0\) and \(f\neq0\), and \(\|f\|_{\sup}=\sup_x|f(x)|\). For an open set \(U\) we write \(f\prec U\) when \(f\in C_c(X)\), \(0\leq f\leq1\) and \(\operatorname{supp}f\subseteq U\). For a compact set \(K\) we write \(K\prec f\) when \(f\in C_c(X)\), \(0\leq f\leq 1\) and \(f=1\) on \(K\). A function \(h\colon X\to[0,\infty]\) is *lower semicontinuous* (lsc) if every set \(\{h>c\}\) is open; lsc functions are Borel.

*Four tools from topology.* The first two tools are proved in the lesson on the Stone–Weierstrass theorem; we derive the other two from them.

- **(T1)** (*Shrinking*) If \(K\subseteq U\) with \(K\) compact and \(U\) open, there is an open \(V\) with compact closure such that \(K\subseteq V\subseteq\overline V\subseteq U\). This is [Proposition 4.2(2) of the Stone–Weierstrass lesson](topology-cutoffs.md#oa-fnd-sw-15).
- **(T2)** (*Urysohn's lemma*) If \(K\subseteq U\) as in (T1), there is \(f\) with \(K\prec f\prec U\). *Proof.* Take \(V\) from (T1). [Corollary 5.2 of the Stone–Weierstrass lesson](topology-cutoffs.md#oa-fnd-sw-16), applied to the compact set \(K\) and the closed set \(X\setminus V\), gives \(f\in C_c(X)\) with \(0\leq f\leq1\), \(f=1\) on \(K\) and \(f=0\) off \(V\). Then \(\operatorname{supp}f\subseteq\overline V\subseteq U\). \(\square\)
- **(T3)** (*Partitions of unity*) If \(K\) is compact and \(K\subseteq U_1\cup\dots\cup U_n\) with each \(U_i\) open, there are \(h_i\prec U_i\) with \(\sum_ih_i=1\) on \(K\) and \(\sum_ih_i\leq1\) everywhere. *Proof.* For each \(x\in K\) pick an index \(i\) with \(x\in U_i\), and by (T1) an open \(V_x\ni x\) whose compact closure lies in \(U_i\). Finitely many \(V_x\) cover \(K\). Let \(F_i\) be the union of the closures of the chosen \(V_x\) that were assigned to \(i\). Then \(F_i\) is compact, \(F_i\subseteq U_i\), and \(K\subseteq\bigcup_iF_i\). Choose \(F_i\prec g_i\prec U_i\) by (T2) and set \(h_1=g_1\) and \(h_k=(1-g_1)\cdots(1-g_{k-1})g_k\). By induction, \(\sum_{k\leq m}h_k=1-\prod_{k\leq m}(1-g_k)\). This lies in \([0,1]\), and it equals \(1\) on each \(F_i\). \(\square\)
- **(T4)** (*Tube lemma*) If \(K\subseteq X\) and \(L\subseteq Y\) are compact and \(K\times L\subseteq W\) with \(W\) open in \(X\times Y\), there are open \(U\supseteq K\) and \(V\supseteq L\) with \(U\times V\subseteq W\). *Proof.* Fix \(x\in K\). Each \((x,y)\), \(y\in L\), lies in an open box inside \(W\); finitely many boxes \(P_j\times Q_j\) of this kind have \(Q_j\) covering \(L\). Put \(P^x=\bigcap_jP_j\) and \(Q^x=\bigcup_jQ_j\); then \(P^x\times Q^x\subseteq W\). Cover \(K\) by finitely many \(P^{x_i}\), and let \(U=\bigcup_iP^{x_i}\) and \(V=\bigcap_iQ^{x_i}\). \(\square\)

*Measures and functions.* A measure is positive and countably additive. \(\mathcal B(X)\) denotes the Borel sets of \(X\), the \(\sigma\)-algebra generated by the open sets; functions on \(X\) are Borel unless said otherwise. A Borel set is *\(\sigma\)-finite* for a measure when countably many Borel sets of finite measure cover it. For \(1\leq p<\infty\), \(L^p(\mu)\) consists of the Borel functions with \(\int|f|^p\,d\mu<\infty\), modulo functions that vanish almost everywhere. Hilbert spaces are complex, and the inner product \(\langle\xi,\eta\rangle=\int\xi\bar\eta\,d\mu\) is linear in \(\xi\). For a Borel \(f\colon X\to[0,\infty]\) we use the *layer functions*
\[
s_n=2^{-n}\sum_{i=1}^{n2^n}1_{\{f>i2^{-n}\}} .
\tag{1.1}
\]
They are simple Borel functions, and they vanish where \(f\) does. They increase, \(s_n\leq s_{n+1}\), because the \(i\)-th term of \(s_n\) is at most the sum of the terms of \(s_{n+1}\) with indices \(2i-1\) and \(2i\). And \(s_n(x)\to f(x)\) at every point: if \(f(x)<n\), then \(f(x)-2^{-n}\leq s_n(x)\leq f(x)\), and if \(f(x)=\infty\), then \(s_n(x)=n\). The monotone and dominated convergence theorems, Hölder's inequality, and the completeness of \(L^p\) are proved in [Measure and Hilbert space tools for Haar integration](measure-tools.md), Theorems 2.1, 2.2, 3.1 and 3.2. The exact uses are listed under "Results used from other lessons".

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

*Step 3: open sets are measurable.* Let \(U\) be open. By Carathéodory's theorem [the preceding tools lesson, Theorem 1.1](measure-tools.md#1-from-an-outer-measure-to-a-measure) it is enough to show \(\mu^*(A)\geq\mu^*(A\cap U)+\mu^*(A\setminus U)\) whenever \(\mu^*(A)<\infty\). First let \(A=V\) be open. Given \(\varepsilon>0\), choose \(f\prec V\cap U\) with \(I(f)>\mu(V\cap U)-\varepsilon\). The set \(V\setminus\operatorname{supp}f\) is open; choose \(g\prec V\setminus\operatorname{supp}f\) with \(I(g)>\mu(V\setminus\operatorname{supp}f)-\varepsilon\). The supports of \(f\) and \(g\) are disjoint, so \(f+g\prec V\) and
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

## Original source bibliography, retained

## References

- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1, 2 and 4, [author’s freely accessible text and editable TeX](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm). Volume 4 uses complete, locally determined Radon measures; Proposition 13.7 relates that convention to ours.
- [van Doorn] F. van Doorn, *Formalized Haar Measure*, 2021, [arXiv version 1](https://arxiv.org/abs/2102.07636v1). The paper constructs Haar measure on arbitrary LCH groups; its uniqueness proof assumes second countability. The [current mathlib uniqueness development](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Haar/Unique.html) also distinguishes regularity hypotheses.
- [Cartan 1940] H. Cartan, Sur la mesure de Haar, *Comptes Rendus de l'Académie des Sciences de Paris* 211 (1940), 759–762. https://gallica.bnf.fr/ark:/12148/bpt6k3163d/f759.item
- [von Neumann 1936] J. von Neumann, The uniqueness of Haar's measure, *Matematicheskii Sbornik* (N.S.) 1(43) (1936), 721–734. https://www.mathnet.ru/eng/sm5481

- [Fischer–Ruzhansky] V. Fischer and M. Ruzhansky, [*Quantization on Nilpotent Lie Groups*](https://biblio.ugent.be/publication/8585474), Birkhäuser, 2016, freely accessible under CC BY 4.0. Its Heisenberg and homogeneous-group treatment complements Example 12.3; its convolution discussion includes the full Young bound of Theorem 14.4. The calculations and proof here are independently written.

## Source and rights

The selected original programme exposition is dedicated under CC0 1.0. Historical authorship and checking statements remain exactly as supplied in the source header. External references retain their own rights; their text is not reproduced here. The [CC0 legal text](LICENSE-CC0.txt) and [component provenance](component-provenance.json) accompany this selection. The full transparent source remains available at [its original source location](https://raw.githubusercontent.com/KokunoYumeto/open-math-courses/main/docs/courses/harmonic-analysis-on-locally-compact-groups/src/haar-measure-on-locally-compact-groups.md).
