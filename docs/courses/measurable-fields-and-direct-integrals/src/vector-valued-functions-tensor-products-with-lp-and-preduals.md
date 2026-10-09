# Vector-valued functions, tensor products with \(L^p\), and preduals

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions (the references, proofs added to the background section, and the lifting theorem proved in its own lesson) are self-checked by the writing AI. Public domain (CC0).*

This lesson develops integration of vector-valued functions over a positive Radon measure \(\mu\) on a locally compact space \(\Gamma\), and uses it to describe some spaces and algebras that recur in operator algebra theory. No countability is assumed: \(\mu\) need not be \(\sigma\)-finite, the Banach space \(E\) is arbitrary, and the Hilbert space \(\mathfrak h\) may have any dimension. The main results are these. The space \(L^p_E(\Gamma,\mu)\), defined as a completion of \(K(\Gamma)\otimes E\), is a space of \(E\)-valued functions, and \(L^1_E\) is the projective tensor product \(L^1\otimes_\gamma E\) (Section 5). Every bounded functional on \(L^1_E\) is integration against a bounded \(E^*\)-valued function (Section 6). On \(L^2_{\mathfrak h}(\Gamma,\mu)=L^2(\Gamma,\mu)\otimes\mathfrak h\), the operators that commute with all multiplications by bounded functions are exactly the decomposable operators, which act fibrewise through bounded operator-valued functions (Section 8). For a von Neumann algebra \(M\), the predual of \(L^\infty(\Gamma,\mu)\bar\otimes M\) is \(L^1_{M_*}(\Gamma,\mu)\) (Section 9). They are the measure-theoretic basis of direct integral theory, and they are used when a von Neumann algebra is tensored with \(L^\infty\) of a measure.

Two devices replace countability. A decomposition of \(\Gamma\) into disjoint compact pieces of positive measure (Section 2) reduces most questions to finite measures. When \(\mathfrak h\) or \(E\) is not separable, one also needs representatives of all elements of \(L^\infty\), chosen coherently. A lifting provides them, but a weaker object, which we call a *selector*, is enough (Section 3). When \(\mathfrak h\) or \(E\) is separable, no selector is needed, and on \(\mathbb R^n\) a selector comes from a Banach limit of averages, without the lifting theorem. For separable fibres, the method that avoids liftings works for every Radon measure; Section 7 shows exactly where it fails for nonseparable fibres.

We assume measure theory on finite measure spaces, basic Banach and Hilbert space theory, and von Neumann algebras on Hilbert spaces. The lesson extends Measurable fields of Hilbert spaces and their direct integrals and Decomposable operators and the diagonal algebra, which treat \(\sigma\)-finite measure spaces and separable fibres. It uses the Riesz representation theorem from Haar measure on locally compact groups and spatial tensor products from Spatial tensor products of von Neumann algebras. The other facts used from other lessons are collected at the end, with the place where each is proved.

Direct integrals and decomposable operators go back to von Neumann's reduction theory. The measurability criterion of Section 4 is due to Pettis [Pettis 1938], the identification \(L^1\otimes_\gamma E=L^1_E\) to Grothendieck, and the lifting theorem to von Neumann for Lebesgue measure and to Maharam in general (see The lifting theorem).

## Conventions

Throughout, \(\Gamma\) is a locally compact Hausdorff space, and \(K(\Gamma)\) is the space of continuous complex functions on \(\Gamma\) with compact support. A *positive Radon measure* \(\mu\) is a linear functional on \(K(\Gamma)\) with \(\mu(f)\geq0\) whenever \(f\geq0\). By the Riesz representation theorem, \(\mu(f)=\int f\,d\mu\) for a Radon measure on the Borel sets, which we also write \(\mu\). It is finite on compact sets, outer regular on Borel sets, and inner regular on open sets. The theorem is proved in the lesson Haar measure on locally compact groups. We use one consequence of regularity:

- **(R)** If \(B\) is a Borel set with \(\mu(B)<\infty\) and \(\varepsilon>0\), there are a compact \(C\subseteq B\) and an open \(U\supseteq B\) with \(\mu(U\setminus C)<\varepsilon\).

It follows from outer regularity together with inner regularity on Borel sets of finite measure, which is proved in the same lesson.

Except in the statements about \(\sigma\)-finite measures in Section 4, we use the value of \(\mu\) only on Borel subsets of compact sets.

\(E\) is a complex Banach space with dual \(E^*\); for \(x^*\in E^*\) and \(a\in E\) we write \(x^*(a)\). \(\mathfrak h\) is a complex Hilbert space of any dimension. Inner products are linear in the first variable. In this lesson, *measurable* means \(\mu\)-measurable in the sense of Definition 1.1. This differs from the lessons on direct integrals, where measurability refers to a \(\sigma\)-algebra.

## 1. Locally null sets and measurable maps

**Definition 1.1.**

1. A set \(N\subseteq\Gamma\) is *locally null* if, for every compact \(K\), the set \(N\cap K\) lies in a Borel set of measure \(0\). A property holds *locally almost everywhere* (l.a.e.) if it holds outside a locally null set.
2. Let \(X\) be a metric space. A map \(f:\Gamma\to X\) is *\(\mu\)-measurable* if for every compact \(K\) and every \(\varepsilon>0\) there is a compact \(K_0\subseteq K\) with \(\mu(K\setminus K_0)<\varepsilon\) such that \(f|_{K_0}\) is continuous. We use this for \(X=E\), for \(X=\mathbb C\), for \(X=[0,\infty]\), and for dual spaces with their norm. A set \(A\) is \(\mu\)-measurable if \(1_A\) is.

Part 2 turns the conclusion of Lusin's theorem into a definition. It refers only to compact sets, which is what makes it suitable for measures that are not \(\sigma\)-finite.

**Lemma 1.2.**

1. A countable union of locally null sets is locally null. If \(f\) is \(\mu\)-measurable and \(g=f\) l.a.e., then \(g\) is \(\mu\)-measurable.
2. (*Composition*) Let \(f_1,\ldots,f_m\) be \(\mu\)-measurable maps into metric spaces \(X_1,\ldots,X_m\), and let \(\Phi:X_1\times\cdots\times X_m\to Y\) be continuous. Then \(\Phi(f_1,\ldots,f_m)\) is \(\mu\)-measurable. In particular, sums, products and norms of \(\mu\)-measurable functions are \(\mu\)-measurable, and so is \(\gamma\mapsto x^*(f(\gamma))\) for \(\mu\)-measurable \(f:\Gamma\to E\) and fixed \(x^*\in E^*\).
3. (*Limits*) If \(f_n:\Gamma\to X\) are \(\mu\)-measurable and \(f_n(\gamma)\to f(\gamma)\) l.a.e., then \(f\) is \(\mu\)-measurable.
4. (*Borel versions*) Let \(X\) be a separable metric space. A map \(f:\Gamma\to X\) is \(\mu\)-measurable exactly when, for every compact \(K\), there is a Borel map \(g:K\to X\) that agrees with \(f\) outside a null subset of \(K\). In particular, \(A\) is \(\mu\)-measurable if and only if each \(A\cap K\) differs from a Borel set by a subset of a Borel null set.

**Proof.** (1) If \(N_n\cap K\subseteq B_n\) with \(\mu(B_n)=0\), then \(\big(\bigcup_nN_n\big)\cap K\subseteq\bigcup_nB_n\), which is a Borel null set. For the second claim, fix \(K\) and \(\varepsilon\), and choose \(K_0\) for \(f\) as in Definition 1.1. Take a Borel null set \(B\supseteq\{f\neq g\}\cap K\). By (R) there is a compact \(K_1\subseteq K_0\setminus B\) with \(\mu((K_0\setminus B)\setminus K_1)<\varepsilon\). Then \(g=f\) on \(K_1\), so \(g|_{K_1}\) is continuous, and \(\mu(K\setminus K_1)<2\varepsilon\).

(2) Choose compact sets \(K_j\subseteq K\) with \(\mu(K\setminus K_j)<\varepsilon/m\) and \(f_j|_{K_j}\) continuous, and put \(K_0=\bigcap_jK_j\). On \(K_0\) every \(f_j\) is continuous, hence so is \(\Phi(f_1,\ldots,f_m)\), and \(\mu(K\setminus K_0)<\varepsilon\).

(3) Fix \(K\) and \(\varepsilon\). Choose compact \(K_n\subseteq K\) with \(f_n|_{K_n}\) continuous and \(\mu(K\setminus K_n)<\varepsilon2^{-n-2}\). Choose a Borel null set \(B\) that contains the points of \(K\) where \(f_n(\gamma)\not\to f(\gamma)\). By (R), take a compact \(K'\subseteq\big(\bigcap_nK_n\big)\setminus B\) with \(\mu(K\setminus K')<\varepsilon/2\). On \(K'\) every \(f_n\) is continuous and \(f_n\to f\) pointwise. The functions \(h_n(\gamma)=\sup_{k,l\geq n}d(f_k(\gamma),f_l(\gamma))\) are suprema of continuous functions on \(K'\), so they are lower semicontinuous, hence Borel, and they decrease to \(0\). For each \(m\), the Borel sets \(\{h_n\geq1/m\}\) decrease to \(\emptyset\) as \(n\) grows. Since \(\mu(K')<\infty\), there is \(n_m\) with \(\mu(\{h_{n_m}\geq1/m\})<\varepsilon2^{-m-2}\). On \(B'=K'\setminus\bigcup_m\{h_{n_m}\geq1/m\}\) the sequence \((f_n)\) is uniformly Cauchy, and \(\mu(K'\setminus B')<\varepsilon/4\). By (R), take a compact \(K''\subseteq B'\) with \(\mu(B'\setminus K'')<\varepsilon/4\). On \(K''\), \(f_n\to f\) uniformly, since \(d(f_k(\gamma),f(\gamma))\leq h_k(\gamma)\). So \(f|_{K''}\) is continuous, and \(\mu(K\setminus K'')<\varepsilon\). This is Egorov's argument.

(4) Let \(f\) be \(\mu\)-measurable and \(K\) compact. Take compact \(K_n\subseteq K\) with \(\mu(K\setminus K_n)<1/n\) and \(f|_{K_n}\) continuous, put \(L=\bigcup_nK_n\), and fix \(x_0\in X\). Let \(g=f\) on \(L\) and \(g=x_0\) on \(K\setminus L\). For open \(V\subseteq X\), the set \(g^{-1}(V)\) is the union of the sets \(\big(K_n\setminus\bigcup_{m<n}K_m\big)\cap(f|_{K_n})^{-1}(V)\), together with \(K\setminus L\) when \(x_0\in V\). Each of these sets is Borel, because \((f|_{K_n})^{-1}(V)\) is relatively open in \(K_n\). So \(g\) is Borel, and \(g=f\) outside the null set \(K\setminus L\).

Conversely, let \(g:K\to X\) be Borel and equal to \(f\) outside a null set, and fix \(\varepsilon>0\). Let \(V_1,V_2,\ldots\) be a countable base of \(X\). By (R), choose compacts \(C_m\subseteq g^{-1}(V_m)\) and \(D_m\subseteq K\setminus g^{-1}(V_m)\) with \(\mu(K\setminus(C_m\cup D_m))<\varepsilon2^{-m}\). On the compact set \(K_0=\bigcap_m(C_m\cup D_m)\) we have \(g^{-1}(V_m)\cap K_0=K_0\setminus D_m\), which is relatively open. So \(g|_{K_0}\) is continuous, and \(\mu(K\setminus K_0)<\varepsilon\). Removing the null set where \(f\neq g\), as in (1), gives the compact set required for \(f\). The statement about sets is the case \(X=\{0,1\}\). \(\square\)

**Remark 1.3** (Measurability with respect to a \(\sigma\)-algebra). Let \(\Sigma_\mu\) be the family of \(\mu\)-measurable sets. By Lemma 1.2 it is a \(\sigma\)-algebra containing the Borel sets: complements and finite unions are handled by part 2, countable unions by part 3, and Borel sets by part 4. On each compact \(K\) it is the completion of the Borel \(\sigma\)-algebra of \(K\), by part 4. For a map \(f\) into a separable metric space, part 4 also shows that \(f\) is \(\mu\)-measurable exactly when it is \(\Sigma_\mu\)-measurable. Indeed, if \(f\) is \(\Sigma_\mu\)-measurable, then on each compact \(K\) the preimages \(f^{-1}(V_m)\cap K\) of a countable base differ from Borel sets by null sets. Changing \(f\) on the union \(Z\) of these null sets gives a Borel map on \(K\).

## 2. Decomposing a Radon measure, and the spaces \(L^p\)

For a measure that is not \(\sigma\)-finite, the spaces \(L^1(\Gamma,\mu)\) and \(L^\infty(\Gamma,\mu)\), and the duality between them, need care: a locally null set can have infinite measure (Example 2.7). The decomposition below reduces such questions to finite measures on compact sets.

**Lemma 2.1** (Decomposition). There is a family \((K_i)_{i\in I}\) of pairwise disjoint nonempty compact sets with the following properties.

1. Every compact set meets only countably many \(K_i\).
2. The set \(N=\Gamma\setminus\bigcup_iK_i\) is locally null.
3. For each \(i\), every nonempty relatively open subset of \(K_i\) has positive measure.
4. (*Gluing*) A map \(f:\Gamma\to X\) into a metric space is \(\mu\)-measurable as soon as, for each \(i\) and \(\varepsilon>0\), there is a compact \(C\subseteq K_i\) with \(\mu(K_i\setminus C)<\varepsilon\) and \(f|_C\) continuous.

**Proof.** *Supports.* For a compact \(C\) with \(\mu(C)>0\), let \(C'\) be the set of \(\gamma\in C\) such that \(\mu(C\cap V)>0\) for every open \(V\ni\gamma\); we call \(C'\) the *support* of \(C\). The set \(C\setminus C'=C\cap W\), where \(W\) is the union of the open sets \(V\) with \(\mu(C\cap V)=0\), is relatively open, so \(C'\) is compact. Every compact subset of \(C\cap W\) is covered by finitely many such \(V\), so it is null; by (R), \(\mu(C\setminus C')=0\). Hence \(\mu(C')=\mu(C)>0\), and \(C'\) has property 3.

*Zorn.* Consider the families of pairwise disjoint nonempty compact sets with property 3, ordered by inclusion. The union of a chain is again such a family. By Zorn's lemma there is a maximal family \((K_i)\).

*Property 1.* Let \(K\) be compact, and choose an open \(U\supseteq K\) with compact closure. If \(K_i\) meets \(U\), then \(\mu(K_i\cap U)>0\) by property 3. The sets \(K_i\cap U\) are disjoint subsets of \(\bar U\), which has finite measure. So only countably many \(K_i\) meet \(U\).

*Property 2.* Let \(K\) be compact. By property 1, \(B=K\setminus\bigcup_iK_i\) is a Borel set. If \(\mu(B)>0\), then (R) gives a compact \(C\subseteq B\) with \(\mu(C)>0\). Its support \(C'\) is disjoint from every \(K_i\), so it could be added to the family, contradicting maximality. So \(\mu(B)=0\).

*Property 4.* Let \(K\) be compact and \(\varepsilon>0\). Let \(K_{i_1},K_{i_2},\ldots\) be the pieces that meet \(K\). Since \(K\cap N\) is null, \(\sum_j\mu(K\cap K_{i_j})=\mu(K)<\infty\), so there is \(J\) with \(\sum_{j>J}\mu(K\cap K_{i_j})<\varepsilon/2\). Choose compact \(C_j\subseteq K_{i_j}\) with \(\mu(K_{i_j}\setminus C_j)<\varepsilon/(2J)\) and \(f|_{C_j}\) continuous. On the compact set \(K_0=K\cap(C_1\cup\cdots\cup C_J)\), a finite disjoint union of compact pieces, \(f\) is continuous. Moreover \(\mu(K\setminus K_0)<\varepsilon\), because \(K\cap N\) is null. \(\square\)

We fix such a family \((K_i)\), and the locally null set \(N\), for the rest of the lesson.

**Definition 2.2** (Integral). For a \(\mu\)-measurable \(f:\Gamma\to[0,\infty]\), put
\[
\int_\Gamma f\,d\mu=\sup_{K\ \mathrm{compact}}\int_Kf\,d\mu ,
\]
where \(\int_Kf\,d\mu\) is the integral of a Borel version of \(f\) on \(K\) (Lemma 1.2(4)). It does not depend on the version, since two versions agree outside a null set.

**Lemma 2.3.** Let \(f\) be a \(\mu\)-measurable function with values in \([0,\infty]\).

1. The integral is monotone, additive and positively homogeneous. It satisfies monotone convergence, and \(\int f\,d\mu=0\) if and only if \(f=0\) l.a.e. For \(f\in K(\Gamma)\) with \(f\geq0\), it equals \(\mu(f)\).
2. \(\int_\Gamma f\,d\mu=\sum_i\int_{K_i}f\,d\mu\).
3. If \(\int f\,d\mu<\infty\), then \(f=0\) l.a.e. outside the union of countably many \(K_i\).

**Proof.** (1) For additivity, note that \(\int_K(f+g)\leq\int f+\int g\) for every compact \(K\). Conversely, for compact \(K_1,K_2\), \(\int_{K_1\cup K_2}(f+g)\geq\int_{K_1}f+\int_{K_2}g\), which gives the reverse inequality. For monotone convergence, exchange the two suprema and use monotone convergence on each \(K\). The remaining claims follow from the definition; for \(f\in K(\Gamma)\), take \(K\) to contain the support of \(f\).

(2) A compact \(K\) meets only countably many \(K_i\), and \(K\cap N\) is null. So \(\int_Kf=\sum_i\int_{K\cap K_i}f\leq\sum_i\int_{K_i}f\). Conversely, finite sums on the right are integrals over compact sets, so they are at most \(\int_\Gamma f\).

(3) By (2), \(\int_{K_i}f>0\) for only countably many \(i\). On every other \(K_i\), \(f=0\) almost everywhere. A compact set meets only countably many of these pieces, so the exceptional set is locally null. \(\square\)

**Definition 2.4.** For \(1\leq p<\infty\), \(\mathcal L^p(\Gamma,\mu)\) is the space of \(\mu\)-measurable \(f:\Gamma\to\mathbb C\) with \(\int|f|^p\,d\mu<\infty\). \(\mathcal L^\infty(\Gamma,\mu)\) is the space of \(\mu\)-measurable \(f\) with \(|f|\leq c\) l.a.e. for some \(c\), and \(\|f\|_\infty\) is the least such \(c\). The spaces \(L^p(\Gamma,\mu)\), for \(1\leq p\leq\infty\), are these modulo equality l.a.e. Every class in \(L^\infty\) contains bounded functions.

**Proposition 2.5.**

1. The bounded \(\mu\)-measurable functions that vanish outside a compact set are dense in \(L^p\) for \(1\leq p<\infty\).
2. (*\(L^{1*}=L^\infty\)*) For \(g\in L^\infty\), \(\Lambda_g(f)=\int fg\,d\mu\) is a bounded functional on \(L^1\) with \(\|\Lambda_g\|=\|g\|_\infty\). Every bounded functional on \(L^1\) is \(\Lambda_g\) for exactly one \(g\in L^\infty\).
3. \(\pi_0(g)f=gf\) defines an isometric unital \(*\)-isomorphism \(\pi_0\) of \(L^\infty\) onto an algebra of operators on \(L^2(\Gamma,\mu)\).

**Proof.** (1) Let \(f\in\mathcal L^p\). By Lemma 2.3(3), applied to \(|f|^p\), \(f=\sum_jf1_{K_{i_j}}\) l.a.e. for countably many pieces. By Lemma 2.3(2), the tails of this sum tend to \(0\) in \(L^p\). Each \(f1_{K_i}1_{\{|f|\leq m\}}\) is bounded and vanishes off \(K_i\), and it tends to \(f1_{K_i}\) as \(m\to\infty\), by dominated convergence.

(2) Clearly \(\|\Lambda_g\|\leq\|g\|_\infty\). Let \(c<\|g\|_\infty\). The set \(A=\{|g|>c\}\) is not locally null, so some compact \(K\) has \(\mu(A\cap K)>0\). With \(f=1_{A\cap K}\,\bar g/|g|\) we get \(\Lambda_g(f)\geq c\|f\|_1\). This gives the norm, and uniqueness follows.

For existence, let \(\Lambda\in(L^1)^*\), and fix \(i\). The set function \(\nu(B)=\Lambda(1_B)\), for \(\mu\)-measurable \(B\subseteq K_i\), is countably additive: if \(B=\bigsqcup_nB_n\), then \(1_B=\sum_n1_{B_n}\) in \(L^1\). It satisfies \(|\nu(B)|\leq\|\Lambda\|\mu(B)\). The Radon–Nikodym theorem on the finite measure space \(K_i\) gives an integrable \(g_i\) on \(K_i\) with \(\Lambda(1_B)=\int_Bg_i\,d\mu\). Then \(\Lambda(f)=\int fg_i\) holds for simple \(f\) on \(K_i\), and for bounded \(f\) by uniform approximation. Take \(B=\{|g_i|>\|\Lambda\|\}\) and \(f=1_B\bar g_i/|g_i|\). This gives \(\int_B(|g_i|-\|\Lambda\|)\leq0\), so \(|g_i|\leq\|\Lambda\|\) almost everywhere on \(K_i\). By truncation and continuity, \(\Lambda(f)=\int fg_i\) for every integrable \(f\) that vanishes off \(K_i\). Let \(g=g_i\) on \(K_i\) and \(g=0\) on \(N\). Then \(g\) is \(\mu\)-measurable by the gluing property of Lemma 2.1, and \(|g|\leq\|\Lambda\|\). For \(f\in L^1\), write \(f=\sum_jf1_{K_{i_j}}\) as in (1). Then \(\Lambda(f)=\sum_j\int_{K_{i_j}}fg=\int fg\).

(3) Clearly \(\|\pi_0(g)\|\leq\|g\|_\infty\). With \(A\) and \(K\) as in (2), the vector \(1_{A\cap K}\) gives \(\|\pi_0(g)1_{A\cap K}\|\geq c\|1_{A\cap K}\|\). The algebraic properties hold pointwise. \(\square\)

Two examples show what the decomposition does when \(\mu\) is not \(\sigma\)-finite.

**Example 2.6** (Counting measure on an uncountable set). Let \(\Gamma\) be an uncountable discrete space and \(\mu\) the counting measure; it is Radon but not \(\sigma\)-finite. Compact sets are finite, so only the empty set is locally null, every function is \(\mu\)-measurable, and the pieces \(K_i\) of Lemma 2.1 can be taken to be the points. Then \(L^\infty=\ell^\infty(\Gamma)\), the spaces of Section 5 are \(L^p_E=\ell^p(\Gamma;E)\), and the identity map is a lifting in the sense of Section 3. Theorem 8.3 says that an operator on \(\ell^2(\Gamma;\mathfrak h)\) that commutes with all multiplications is block diagonal, and Theorem 6.4 identifies \(\ell^1(\Gamma;E)^*\) with \(\ell^\infty(\Gamma;E^*)\). Direct integrals over \(\sigma\)-finite measure spaces, as in the earlier lessons, do not cover this example.

**Example 2.7** (A locally null set that is not null). Let \(\Gamma=\mathbb R_d\times\mathbb R\), a discrete copy of the real line times the usual line, and let \(\mu(f)=\sum_t\int f(t,s)\,ds\). For \(f\in K(\Gamma)\) the sum is finite, since a compact set meets only finitely many lines. The set \(Z=\mathbb R_d\times\{0\}\) meets each compact set in finitely many points, so it is locally null. But any open \(U\supseteq Z\) contains a segment \(\{t\}\times(-\delta_t,\delta_t)\) for each of uncountably many \(t\). So the outer-regular Borel measure of the Riesz representation theorem gives \(Z\) infinite measure. This is why the integral of Definition 2.2 is taken over compact sets and ignores locally null sets: \(\int1_Z\,d\mu=0\). A decomposition as in Lemma 2.1 is obtained by copying onto each line \(\{t\}\times\mathbb R\) one for Lebesgue measure, for instance the closures of the open intervals removed in building the Cantor set inside each \([k,k+1]\). (The segments \(\{t\}\times[k,k+1]\) do not qualify: neighbouring segments share an endpoint.) And \(L^p(\Gamma,\mu)\) is the \(\ell^p\)-sum of copies of \(L^p(\mathbb R)\), one for each \(t\).

## 3. Liftings and selectors

An element of \(L^\infty(\Gamma,\mu)\) is a class of functions. Some constructions below need a representative of every class, chosen coherently for all classes at once. A lifting makes such a choice multiplicatively. We only need the weaker properties of a selector.

**Definition 3.1.** A *selector* for \((\Gamma,\mu)\) is a map \(s\) from \(L^\infty(\Gamma,\mu)\) to the bounded \(\mu\)-measurable functions on \(\Gamma\) such that:

- **(S1)** \(s(F)\) is a representative of \(F\);
- **(S2)** \(s\) is linear;
- **(S3)** \(|s(F)(\gamma)|\leq\|F\|_\infty\) for every \(\gamma\);
- **(S4)** \(s(\bar F)=\overline{s(F)}\);
- **(S5)** for every compact \(K\) there is a locally null set \(N_K\) such that \(s(F)(\gamma)=0\) for all \(\gamma\in K\setminus N_K\) and all \(F\) that vanish l.a.e. on \(K\).

A *lifting* is a \(*\)-homomorphism \(\rho\) of \(L^\infty(\Gamma,\mu)\) into the bounded \(\mu\)-measurable functions, with pointwise operations, that satisfies (S1).

**Proposition 3.2.** Every lifting is a selector.

**Proof.** (S2) and (S4) are part of the definition. For (S3), let \(e=\rho(1)\). It is a real idempotent function, so \(e\in\{0,1\}\) pointwise, and \(\rho(G)=\rho(G)e\) vanishes where \(e=0\). Let \(c=\|F\|_\infty\) and \(h=(c^2-|F|^2)^{1/2}\in L^\infty\). Then \(\rho(h)\) is real, by (S4). Where \(e=1\), we get \(c^2-|\rho(F)|^2=\rho(c^2-|F|^2)=\rho(h)^2\geq0\). For (S5), let \(N_K=\{\gamma\in K:\rho(1_K)(\gamma)\neq1\}\), which is locally null by (S1). If \(F=0\) l.a.e. on \(K\), then \(F=F\,1_{\Gamma\setminus K}\) in \(L^\infty\). So \(\rho(F)=\rho(F)\big(\rho(1)-\rho(1_K)\big)\), and this vanishes on \(K\setminus N_K\). \(\square\)

**Proposition 3.3** (Liftings exist). \(L^\infty(\Gamma,\mu)\) has a lifting.

**Proof.** By The lifting theorem, Corollary 6.3, each complete finite measure space \((K_i,\Sigma_\mu|_{K_i},\mu)\), which has positive measure, has a lifting \(\rho_i\). Put \(\rho(F)=\rho_i(F|_{K_i})\) on \(K_i\) and \(\rho(F)=0\) on \(N\). Each \(\rho(F)\) is \(\mu\)-measurable by the gluing property of Lemma 2.1, and the algebraic properties hold piece by piece. For (S1), a compact set meets only countably many \(K_i\), and on each of them \(\rho(F)\) agrees with \(F\) almost everywhere. So \(\rho\) is a lifting. \(\square\)

**Proposition 3.4** (A selector on \(\mathbb R^n\) without the lifting theorem). Let \(\Gamma=\mathbb R^n\) with Lebesgue measure. Let \(L\) be a *Banach limit at \(0\)*: a linear functional on the bounded functions \(h:(0,1]\to\mathbb C\) with \(L(\bar h)=\overline{L(h)}\) and \(|L(h)|\leq\limsup_{r\to0}|h(r)|\), and with \(L(h)=\lim_{r\to0}h(r)\) whenever the limit exists. For \(F\in L^\infty(\mathbb R^n)\), put
\[
s(F)(\gamma)=L\Big(r\mapsto\frac1{|B(\gamma,r)|}\int_{B(\gamma,r)}F\,d\mu\Big).
\]
Then \(s\) is a selector.

**Proof.** *Existence of \(L\).* On bounded real functions, \(p(h)=\limsup_{r\to0}h(r)\) is sublinear. The limit functional, on the functions that have a limit, is dominated by \(p\). The Hahn–Banach theorem extends it to a linear \(L_{\mathbb R}\leq p\), so \(-p(-h)\leq L_{\mathbb R}(h)\leq p(h)\). Put \(L(h)=L_{\mathbb R}(\operatorname{Re}h)+iL_{\mathbb R}(\operatorname{Im}h)\). Then \(L(\bar h)=\overline{L(h)}\). Write \(L(h)=e^{i\theta}|L(h)|\). Then \(|L(h)|=L(e^{-i\theta}h)=L_{\mathbb R}(\operatorname{Re}(e^{-i\theta}h))\leq\limsup|h|\).

*Selector properties.* The averages depend only on the class of \(F\), so \(s\) is well defined on \(L^\infty\). (S2) and (S4) are clear. For (S3), each average has modulus at most \(\|F\|_\infty\). (S1): by the Lebesgue differentiation theorem, the averages of a representative converge to \(F(\gamma)\) for almost every \(\gamma\), and there \(s(F)(\gamma)=F(\gamma)\). So \(s(F)=F\) a.e., and \(s(F)\) is \(\mu\)-measurable by Lemma 1.2(1). (S5): let \(N_K\) be the set of points of \(K\) at which \(K\) does not have density \(1\). It is null by the Lebesgue density theorem. If \(F=0\) a.e. on \(K\) and \(\gamma\in K\setminus N_K\), then the average over \(B(\gamma,r)\) has modulus at most \(\|F\|_\infty|B(\gamma,r)\setminus K|/|B(\gamma,r)|\), which tends to \(0\). So \(s(F)(\gamma)=0\). \(\square\)

This selector is not multiplicative (Example 3.5). The proof uses only the differentiation and density theorems, so it works for any measure for which these hold. For instance, it works for every Radon measure \(\mu\) on \(\mathbb R^n\): average with respect to \(\mu\), dividing by \(\mu(B(\gamma,r))\), and put \(s(F)=0\) off the support of \(\mu\). The completion of \(\mu\) is a Radon measure in the sense of Besicovitch's covering theorem and the differentiation of Radon measures, Lemma 1.3; the support is conegligible (Lemma 1.2 there), and Theorem 5.1 and Corollary 5.2 there are the differentiation and density theorems for \(\mu\).

**Example 3.5** (A selector that is not a lifting). On \(\mathbb R\), let \(s\) be the Banach-limit selector of Proposition 3.4 and \(F=1_{[0,\infty)}\). The averages of \(F\) over \((-r,r)\) all equal \(\tfrac12\). So \(s(F)(0)=\tfrac12\), while \(s(F^2)(0)=s(F)(0)=\tfrac12\neq s(F)(0)^2\). The selector is not multiplicative, and \(s(F)\) takes a value outside \(\{0,1\}\) at a point, although \(F\) is an indicator. Theorem 8.3 nevertheless applies to it. Exercise 4 continues this example.

## 4. Measurability of vector-valued functions

The next criterion tests whether an \(E\)-valued function is measurable through scalar functions. It is a form of Pettis's measurability theorem.

**Theorem 4.1** (Measurability criterion). A map \(f:\Gamma\to E\) is \(\mu\)-measurable if and only if:

1. \(x^*\circ f\) is \(\mu\)-measurable for every \(x^*\in E^*\); and
2. for every compact \(K\) there is a set \(K_\infty\subseteq K\) with \(K\setminus K_\infty\) null such that \(f(K_\infty)\) is separable.

(One may also require \(K_\infty\) to be \(\mu\)-measurable. This changes nothing: \(K\setminus K_\infty\) lies in a Borel null set \(Z\), and \(K\setminus Z\) is a Borel subset of \(K_\infty\).)

**Proof.** If \(f\) is \(\mu\)-measurable, condition 1 holds because \(x^*\circ f\) is the composition of \(f\) with a continuous function (Lemma 1.2(2)). For condition 2, take compact \(K_n\subseteq K\) with \(\mu(K\setminus K_n)<1/n\) and \(f|_{K_n}\) continuous, and put \(K_\infty=\bigcup_nK_n\). Each \(f(K_n)\) is compact, hence separable.

Conversely, fix \(K\) and \(\varepsilon>0\). The set \(K\setminus K_\infty\) lies in a Borel null set \(Z\subseteq K\). By (R), take a compact \(C\subseteq K\setminus Z\) with \(\mu(K\setminus C)<\varepsilon/2\). Let \(F\) be the closed linear span of \(f(C)\); it is separable. Choose a dense sequence \((y_m)\) in \(F\). By the Hahn–Banach theorem, choose \(x_m^*\in E^*\) with \(\|x_m^*\|\leq1\) and \(x_m^*(y_m)=\|y_m\|\). Then \(\|y\|=\sup_k|x_k^*(y)|\) for every \(y\in F\). Indeed, given \(\delta>0\), choose \(k\) with \(\|y-y_k\|<\delta\); then \(|x_k^*(y)|\geq\|y_k\|-\delta\geq\|y\|-2\delta\). Put \(g_m(\gamma)=\sup_k|x_k^*(f(\gamma))-x_k^*(y_m)|\). Each \(g_m\) is \(\mu\)-measurable: the functions \(|x_k^*(f(\cdot))-x_k^*(y_m)|\) are measurable by condition 1, their finite maxima by Lemma 1.2(2), and the supremum is the pointwise limit of these maxima (Lemma 1.2(3)). On \(C\), where \(f(\gamma)-y_m\in F\), \(g_m\) equals \(\|f(\gamma)-y_m\|\). Choose compacts \(C_m\subseteq C\) with \(g_m|_{C_m}\) continuous and \(\mu(C\setminus C_m)<\varepsilon2^{-m-1}\), and let \(C_0=\bigcap_mC_m\). Then \(\mu(K\setminus C_0)<\varepsilon\). We claim \(f|_{C_0}\) is continuous. Let \(\gamma_0\in C_0\) and \(\delta>0\), and choose \(m\) with \(\|f(\gamma_0)-y_m\|<\delta\). Since \(g_m\) is continuous on \(C_0\), some neighbourhood \(V\) of \(\gamma_0\) has \(g_m<\delta\) on \(V\cap C_0\). There \(\|f(\gamma)-f(\gamma_0)\|\leq g_m(\gamma)+g_m(\gamma_0)<2\delta\). \(\square\)

**Corollary 4.2.** If \(E\) is separable, \(f:\Gamma\to E\) is \(\mu\)-measurable if and only if every \(x^*\circ f\) is \(\mu\)-measurable. For a separable Hilbert space with orthonormal basis \((\varepsilon_k)\), this holds if and only if every coordinate \(\langle f(\cdot),\varepsilon_k\rangle\) is \(\mu\)-measurable.

**Proof.** Condition 2 of Theorem 4.1 is automatic, since \(E\) is separable. For the Hilbert case, every functional has the form \(\langle\cdot,\eta\rangle\), and \(\langle f(\gamma),\eta\rangle=\sum_k\langle f(\gamma),\varepsilon_k\rangle\langle\varepsilon_k,\eta\rangle\) converges at every point. So \(\langle f(\cdot),\eta\rangle\) is a pointwise limit of \(\mu\)-measurable functions, and Lemma 1.2(3) applies. \(\square\)

**Proposition 4.3** (\(\sigma\)-finite measures). Suppose \(\mu\) is \(\sigma\)-finite: \(\Gamma\) is a countable union of Borel sets of finite measure.

1. Every locally null set lies in a Borel null set.
2. Let \(\mathcal K\) be a separable Hilbert space. The measurable sections of the constant field \(\mathcal K\) over the measure space \((\Gamma,\Sigma_\mu,\mu)\), in the sense of direct integral theory, are exactly the \(\mu\)-measurable maps \(\Gamma\to\mathcal K\).
3. Every \(\mu\)-measurable map \(\Gamma\to\mathcal K\) agrees, outside a Borel null set, with a Borel map.

**Proof.** (1) Let \(\Gamma=\bigcup_nA_n\) with \(\mu(A_n)<\infty\). By (R), each \(A_n\) is, up to a Borel null set, a countable union of compact sets \(C_{n,k}\). For a locally null \(N\), each \(N\cap C_{n,k}\) lies in a Borel null set. So \(N\) does too.

(2) By part 1, \(\Gamma\) is, up to a Borel null set, the union of the compact sets \(C_{n,k}\), and on each compact set \(\Sigma_\mu\) is the completion of the Borel \(\sigma\)-algebra (Remark 1.3). So \(\Sigma_\mu\) is the \(\mu\)-completion of the Borel \(\sigma\)-algebra, \(\mu\) extends to it, and \((\Gamma,\Sigma_\mu,\mu)\) is a \(\sigma\)-finite measure space. The measurable sections of the constant field are the maps whose coordinates are \(\Sigma_\mu\)-measurable. By Remark 1.3, applied to the coordinates, and Corollary 4.2, these are the \(\mu\)-measurable maps.

(3) As in part 1, \(\Gamma\) is, up to a Borel null set, a disjoint union of countably many Borel subsets of compact sets. On each of them the map agrees with a Borel map outside a null set (Lemma 1.2(4)). Put these Borel maps together, and use a constant on the remaining Borel null set. \(\square\)

So, for \(\sigma\)-finite \(\mu\) and separable fibres, the direct-integral framework over \((\Gamma,\Sigma_\mu,\mu)\) and the framework of this lesson describe the same functions, with the same null sets (see also Corollary 5.4(3)).

## 5. The spaces \(L^p_E\) and tensor products with \(L^p\)

We define \(L^p_E\) as a completion of \(K(\Gamma)\otimes E\), and then show that it is a space of \(E\)-valued functions. For \(p=1\) it is also a completed tensor product of \(L^1\) with \(E\).

**Definition 5.1** (\(L^p_E\)). Identify \(\sum_if_i\otimes a_i\in K(\Gamma)\otimes E\) with the function \(\gamma\mapsto\sum_if_i(\gamma)a_i\). This is injective: write the element with linearly independent \(a_i\); then the function vanishes only if every \(f_i\) does. The image is the space of continuous compactly supported \(E\)-valued functions whose values lie in a finite-dimensional subspace. For \(1\leq p<\infty\),
\[
\|f\|_p=\Big(\int_\Gamma\|f(\gamma)\|^p\,d\mu(\gamma)\Big)^{1/p}
\tag{5.1}
\]
is a seminorm on \(K(\Gamma)\otimes E\). With \(N_p=\{f:\|f\|_p=0\}\), the Banach space \(L^p_E(\Gamma,\mu)\) is the completion of \((K(\Gamma)\otimes E)/N_p\).

**Proposition 5.2** (Continuous vector-valued functions). Let \(\Gamma\) be compact, and let \(C_E(\Gamma)\) be the continuous functions \(\Gamma\to E\) with \(\|f\|_\infty=\sup_\gamma\|f(\gamma)\|\).

1. \(C(\Gamma)\otimes E\) is dense in \(C_E(\Gamma)\).
2. On \(C(\Gamma)\otimes E\), \(\|\cdot\|_\infty\) equals the *injective cross-norm*, defined for \(u=\sum_if_i\otimes a_i\) by
\(\lambda(u)=\sup\{|\sum_i\varphi(f_i)x^*(a_i)|:\ \varphi\in C(\Gamma)^*,\ x^*\in E^*,\ \|\varphi\|,\|x^*\|\leq1\}\). Hence \(C_E(\Gamma)=C(\Gamma)\otimes_\lambda E\), the completion of \(C(\Gamma)\otimes E\) for \(\lambda\).

**Proof.** (1) Let \(f\in C_E(\Gamma)\) and \(\varepsilon>0\). The open sets \(U_\gamma=\{\gamma':\|f(\gamma')-f(\gamma)\|<\varepsilon\}\) cover \(\Gamma\). Choose a finite subcover \(U_{\gamma_1},\ldots,U_{\gamma_m}\) and a partition of unity \(g_1,\ldots,g_m\) subordinate to it. Then \(\|f(\gamma)-\sum_jg_j(\gamma)f(\gamma_j)\|\leq\sum_jg_j(\gamma)\|f(\gamma)-f(\gamma_j)\|<\varepsilon\).

(2) Let \(\varphi\) and \(x^*\) be in the unit balls. Then \(\sum_i\varphi(f_i)x^*(a_i)=\varphi\big(\sum_ix^*(a_i)f_i\big)\), and \(|\sum_ix^*(a_i)f_i(\gamma)|=|x^*(u(\gamma))|\leq\|u(\gamma)\|\). So \(\lambda(u)\leq\|u\|_\infty\). Taking \(\varphi\) to be evaluation at \(\gamma\) gives \(|x^*(u(\gamma))|\leq\lambda(u)\) for every \(x^*\), so \(\|u(\gamma)\|\leq\lambda(u)\). \(\square\)

**Theorem 5.3** (\(L^p_E\) as a space of functions). Let \(1\leq p<\infty\). Let \(\mathcal L^p_E\) be the space of \(\mu\)-measurable \(f:\Gamma\to E\) with \(\|f\|_p<\infty\), where \(\|f\|_p\) is defined by (5.1), and identify functions that agree l.a.e. Then this space is a Banach space, \(K(\Gamma)\otimes E\) is dense in it, and the identity map of \(K(\Gamma)\otimes E\) extends to an isometric isomorphism of \(L^p_E(\Gamma,\mu)\) onto it.

*Remark.* For \(p>1\), summable \(p\)-th powers \(\|f_{n+1}(\gamma)-f_n(\gamma)\|^p\) do not force convergence (take steps of length \(1/n\)), and \(\|a+b\|^p\leq\|a\|^p+\|b\|^p\) fails for \(a=b\neq0\); the proof below uses neither.

**Proof.** (a) \(\|f(\cdot)\|\) is \(\mu\)-measurable, as the composition of \(f\) with the norm (Lemma 1.2(2)). Minkowski's inequality on each compact set gives the triangle inequality, and \(\|f\|_p=0\) exactly when \(f=0\) l.a.e., by Lemma 2.3(1).

(b) *Completeness.* Let \((f_n)\) be Cauchy. Choose \(n_1<n_2<\cdots\) with \(\|f_{n_{k+1}}-f_{n_k}\|_p\leq2^{-k}\), and put \(G=\sum_k\|f_{n_{k+1}}(\cdot)-f_{n_k}(\cdot)\|\). Minkowski's inequality and monotone convergence give \(\|G\|_p\leq1\), so \(G<\infty\) l.a.e. There \((f_{n_k}(\gamma))\) is Cauchy in \(E\). Let \(f(\gamma)\) be its limit, and \(f(\gamma)=0\) elsewhere. Then \(f\) is \(\mu\)-measurable by Lemma 1.2(3). Also \(\|f(\gamma)-f_{n_k}(\gamma)\|\leq\sum_{j\geq k}\|f_{n_{j+1}}(\gamma)-f_{n_j}(\gamma)\|\) l.a.e., so \(\|f-f_{n_k}\|_p\leq\sum_{j\geq k}2^{-j}\to0\). Hence \(f_n\to f\).

(c) *Density.* Let \(f\in\mathcal L^p_E\) and \(\varepsilon>0\). By Lemma 2.3(2)–(3), applied to \(\|f(\cdot)\|^p\), \(f\) vanishes l.a.e. off countably many \(K_i\), and the tails of the sum over these pieces are small in \(\|\cdot\|_p\). So we may assume that \(f\) vanishes outside a compact set \(C\). The set function \(B\mapsto\int_B\|f\|^p\) on \(C\) is finite and absolutely continuous. So there is a compact \(C_0\subseteq C\) with \(f|_{C_0}\) continuous and \(\int_{C\setminus C_0}\|f\|^p<\varepsilon^p\). By Proposition 5.2 on the compact space \(C_0\), there is \(g=\sum_{k\leq m}g_k\otimes a_k\in C(C_0)\otimes E\) with \(\|f(\gamma)-g(\gamma)\|<\varepsilon(1+\mu(C))^{-1/p}\) on \(C_0\). Take an open \(U\supseteq C_0\) with compact closure and \(\mu(U\setminus C_0)<\delta\). Extend each \(g_k\) to \(\tilde g_k\in K(\Gamma)\) with support in \(U\) and \(\sup|\tilde g_k|=\sup|g_k|\) (Tietze's extension theorem; see Results used from other lessons). With \(\tilde g=\sum_k\tilde g_k\otimes a_k\), we have \(f-\tilde g=f1_{C\setminus C_0}+(f-g)1_{C_0}-\tilde g1_{U\setminus C_0}\). So
\[
\|f-\tilde g\|_p<\varepsilon+\varepsilon+\Big(\sum_k\sup|g_k|\,\|a_k\|\Big)\delta^{1/p},
\]
which is less than \(3\varepsilon\) for small \(\delta\).

(d) The map from \((K(\Gamma)\otimes E)/N_p\) is isometric, and its range is dense in a Banach space. So it extends to an isometric isomorphism of the completion. \(\square\)

**Corollary 5.4.**

1. For \(E=\mathbb C\), \(L^p_E\) is the space \(L^p(\Gamma,\mu)\) of Definition 2.4, which is therefore complete, with \(K(\Gamma)\) dense.
2. \(L^2_{\mathfrak h}(\Gamma,\mu)\) is a Hilbert space with \(\langle f,g\rangle=\int\langle f(\gamma),g(\gamma)\rangle\,d\mu\).
3. If \(\mu\) is \(\sigma\)-finite and \(\mathcal K\) is separable, \(L^2_{\mathcal K}(\Gamma,\mu)\) is the direct integral of the constant field \(\mathcal K\) over \((\Gamma,\Sigma_\mu,\mu)\). They have the same vectors and the same inner product.

**Proof.** (1) is the case \(E=\mathbb C\). (2) follows by polarization; the integrand is \(\mu\)-measurable, and integrable by the Cauchy–Schwarz inequality. (3) The two spaces consist of the same functions, by Proposition 4.3(2), and have the same null sets, by Proposition 4.3(1); the inner products are given by the same integral. \(\square\)

**Definition 5.5** (Projective tensor product). For Banach spaces \(E,F\), the *projective cross-norm* of \(u\in E\otimes F\) is \(\|u\|_\gamma=\inf\sum_i\|e_i\|\|f_i\|\), the infimum over all representations \(u=\sum_ie_i\otimes f_i\). The completion is \(E\otimes_\gamma F\).

**Theorem 5.6** (\(L^1_E\) is a projective tensor product). For every Banach space \(E\), the identity map of \(L^1(\Gamma,\mu)\otimes E\), viewed as \(E\)-valued functions, extends to an isometric isomorphism \(L^1(\Gamma,\mu)\otimes_\gamma E\cong L^1_E(\Gamma,\mu)\).

**Proof.** (a) Each element \(\sum_if_i\otimes a_i\) is an integrable \(\mu\)-measurable function. Written with linearly independent \(a_i\), it vanishes l.a.e. only if every \(f_i\) does. So \(L^1\otimes E\) is a subspace of \(L^1_E\).

(b) \(\|\sum_if_ia_i\|_1\leq\sum_i\|f_i\|_1\|a_i\|\), so \(\|u\|_1\leq\|u\|_\gamma\).

(c) For a *simple* element \(u=\sum_j1_{A_j}\otimes b_j\), with pairwise disjoint \(\mu\)-measurable \(A_j\) of finite measure, \(\|u\|_\gamma\leq\sum_j\mu(A_j)\|b_j\|=\|u\|_1\).

(d) Simple elements are \(\gamma\)-dense in \(L^1\otimes E\). Given \(u=\sum_{i\leq m}f_i\otimes a_i\), approximate each \(f_i\) in \(L^1\) by a simple function \(s_i\): first by a bounded function that vanishes off a compact set (Proposition 2.5(1)), then uniformly by simple functions. Then \(\sum_is_i\otimes a_i\) is simple after refining to a common disjoint family, and \(\|u-\sum_is_i\otimes a_i\|_\gamma\leq\sum_i\|f_i-s_i\|_1\|a_i\|\).

(e) Given \(\varepsilon>0\), pick a simple \(v\) with \(\|u-v\|_\gamma<\varepsilon\). Then \(\|u\|_\gamma\leq\|v\|_1+\varepsilon\leq\|u\|_1+2\varepsilon\), by (c) and (b). So \(\|u\|_\gamma=\|u\|_1\).

(f) \(L^1\otimes E\) contains \(K(\Gamma)\otimes E\), so it is dense in the complete space \(L^1_E\) (Theorem 5.3). \(\square\)

The proof uses no lifting. Exercise 1 shows that the injective norm is strictly smaller than \(\|\cdot\|_1\) in general, so the projective norm cannot be replaced by it here.

## 6. The dual of \(L^1_E\)

A bounded function \(\phi:\Gamma\to E^*\) whose pairings \(\phi(\cdot)(a)\) are measurable defines a functional on \(L^1_E\) by integration. We show that every bounded functional on \(L^1_E\) arises in this way when \(E\) is separable or a selector exists.

**Proposition 6.1** (Dual of the projective tensor product). Let \(E\) and \(F\) be Banach spaces. The map \(\phi\mapsto\Phi(\phi)\), \(\Phi(\phi)(e)(f)=\phi(e\otimes f)\), is an isometric isomorphism of \((E\otimes_\gamma F)^*\) onto \(B(E,F^*)\).

**Proof.** \(|\phi(e\otimes f)|\leq\|\phi\|\|e\|\|f\|\), so \(\|\Phi(\phi)\|\leq\|\phi\|\). Conversely, for \(R\in B(E,F^*)\) the formula \(\phi_R(\sum_ie_i\otimes f_i)=\sum_iR(e_i)(f_i)\) is well defined on the algebraic tensor product, since it comes from a bilinear map. It satisfies \(|\phi_R(u)|\leq\|R\|\sum_i\|e_i\|\|f_i\|\) for every representation of \(u\), so \(\|\phi_R\|\leq\|R\|\). The two maps are inverse to each other. \(\square\)

**Lemma 6.2** (Functionals on \(L^1\otimes_\gamma E\) as functions). Let \(\phi\in(L^1(\Gamma,\mu)\otimes_\gamma E)^*\). Suppose \((\Gamma,\mu)\) has a selector \(s\), or \(E\) is separable. Then there is \(\phi(\cdot):\Gamma\to E^*\) such that:

1. \(\gamma\mapsto\phi(\gamma)(a)\) is \(\mu\)-measurable for every \(a\in E\);
2. \(\phi(f\otimes a)=\int f(\gamma)\,\phi(\gamma)(a)\,d\mu(\gamma)\) for \(f\in L^1\) and \(a\in E\);
3. \(\|\phi(\gamma)\|\leq\|\phi\|\) for every \(\gamma\).

**Proof.** By Proposition 6.1, with the factors in the order \(E\), \(L^1\), and since \((L^1)^*=L^\infty\) (Proposition 2.5(2)), there is a bounded linear \(\Theta:E\to L^\infty\) with \(\phi(f\otimes a)=\int f\,\Theta(a)\,d\mu\) and \(\|\Theta\|=\|\phi\|\).

*With a selector:* put \(\phi(\gamma)(a)=s(\Theta(a))(\gamma)\). This is linear in \(a\) by (S2) and bounded by \(\|\phi\|\|a\|\) by (S3). Conditions 1 and 2 follow from (S1).

*For separable \(E\):* choose a linearly independent sequence \((a_n)\) whose span is dense (a finite basis if \(E\) is finite-dimensional), and fix bounded representatives \(t_n\) of \(\Theta(a_n)\). For \(a=\sum_nq_na_n\) with finitely many nonzero Gaussian-rational \(q_n\), put \(t_a=\sum_nq_nt_n\). This set \(D\) of vectors is countable. Each \(t_a\) represents \(\Theta(a)\), and a countable union of locally null sets is locally null. So there is a locally null set \(Z\) outside which \(|t_a(\gamma)|\leq\|\phi\|\|a\|\) for every \(a\in D\). For \(\gamma\notin Z\), the map \(a\mapsto t_a(\gamma)\) is additive, homogeneous over the Gaussian rationals, and bounded on the dense set \(D\). By continuity it extends to \(\phi(\gamma)\in E^*\) with \(\|\phi(\gamma)\|\leq\|\phi\|\). Put \(\phi(\gamma)=0\) on \(Z\). For \(a\in E\), take \(a_k\in D\) with \(a_k\to a\). Then \(\phi(\cdot)(a)=\lim_kt_{a_k}\) off \(Z\), and \(t_{a_k}\to\Theta(a)\) in \(L^\infty\). So \(\phi(\cdot)(a)\) is \(\mu\)-measurable and represents \(\Theta(a)\). \(\square\)

**Lemma 6.3** (Measurability of pairings). Let \(\phi:\Gamma\to E^*\) be such that \(\gamma\mapsto\phi(\gamma)(a)\) is \(\mu\)-measurable for every \(a\in E\). Then \(\gamma\mapsto\phi(\gamma)(x(\gamma))\) is \(\mu\)-measurable for every \(\mu\)-measurable \(x:\Gamma\to E\).

*Remark.* Restricted to a separable subspace of \(E\), \(\phi\) need not be measurable for the norm of its dual (Exercise 2), so the proof below approximates \(x\) instead.

**Proof.** Fix a compact \(K\) and \(\varepsilon>0\), and a compact \(K_0\subseteq K\) with \(\mu(K\setminus K_0)<\varepsilon\) and \(x|_{K_0}\) continuous. Then \(x(K_0)\) is compact. For each \(n\), cover it by finitely many balls \(B(b_{n,j},1/n)\), \(j\leq m_n\). The sets \(P_{n,j}=K_0\cap x^{-1}(B(b_{n,j},1/n))\setminus\bigcup_{k<j}P_{n,k}\) form a Borel partition of \(K_0\). Put \(x_n=\sum_j1_{P_{n,j}}b_{n,j}\) on \(K_0\). Then \(\gamma\mapsto1_{K_0}(\gamma)\phi(\gamma)(x_n(\gamma))=\sum_j1_{P_{n,j}}(\gamma)\,\phi(\gamma)(b_{n,j})\) is \(\mu\)-measurable: it is a finite sum of products of indicator functions of Borel sets, which are \(\mu\)-measurable by Lemma 1.2(4), with the measurable functions \(\phi(\cdot)(b_{n,j})\) (Lemma 1.2(2)). Since \(\|x_n(\gamma)-x(\gamma)\|<1/n\) and \(\phi(\gamma)\) is bounded, this tends to \(1_{K_0}(\gamma)\phi(\gamma)(x(\gamma))\) at every point. By Lemma 1.2(3), that function is \(\mu\)-measurable. So it is continuous on a compact \(K_1\subseteq K_0\) with \(\mu(K_0\setminus K_1)<\varepsilon\), and there it equals \(\phi(\gamma)(x(\gamma))\). \(\square\)

**Theorem 6.4** (The dual of \(L^1_E\)).

1. Let \(\phi:\Gamma\to E^*\) satisfy the hypothesis of Lemma 6.3, with \(c=\sup_\gamma\|\phi(\gamma)\|<\infty\). Then \(\psi_\phi(x)=\int\phi(\gamma)(x(\gamma))\,d\mu(\gamma)\) is a well-defined bounded functional on \(L^1_E\) with \(\|\psi_\phi\|\leq c\).
2. Suppose \((\Gamma,\mu)\) has a selector, or \(E\) is separable. Then every \(\psi\in(L^1_E)^*\) is \(\psi_\phi\) for some such \(\phi\) with \(\sup_\gamma\|\phi(\gamma)\|=\|\psi\|\).
3. If \(E\) is separable, then \(\gamma\mapsto\|\phi(\gamma)\|\) is \(\mu\)-measurable, and \(\|\psi_\phi\|=\operatorname{ess\,sup}_\gamma\|\phi(\gamma)\|\) for every \(\phi\) as in part 1.

**Proof.** (1) The integrand is \(\mu\)-measurable by Lemma 6.3, and it is bounded by \(c\|x(\gamma)\|\).

(2) By Theorem 5.6, \(\psi\in(L^1\otimes_\gamma E)^*\). Lemma 6.2 gives \(\phi\) with \(\|\phi(\gamma)\|\leq\|\psi\|\) and \(\psi=\psi_\phi\) on \(L^1\otimes E\). Both sides are continuous and \(L^1\otimes E\) is dense, so \(\psi=\psi_\phi\). By part 1, \(\|\psi\|\leq\sup\|\phi(\gamma)\|\leq\|\psi\|\).

(3) Take a sequence \((a_n)\) that is dense in the unit ball of \(E\). Then \(\|\phi(\gamma)\|=\sup_n|\phi(\gamma)(a_n)|\), which is \(\mu\)-measurable. The integrand in part 1 has modulus at most \(\operatorname{ess\,sup}\|\phi(\cdot)\|\,\|x(\gamma)\|\) l.a.e., which gives \(\leq\) for the norm. Conversely, let \(c'<\operatorname{ess\,sup}\|\phi(\cdot)\|\), and choose a compact \(K\) with \(\mu(A\cap K)>0\), where \(A=\{\|\phi\|>c'\}\). On \(A\cap K\), let \(x(\gamma)=\theta(\gamma)a_{n(\gamma)}\), where \(n(\gamma)\) is the first \(n\) with \(|\phi(\gamma)(a_n)|>c'\) and \(\theta\) is the phase that makes \(\phi(\gamma)(x(\gamma))\) positive. Let \(x=0\) elsewhere. This \(x\) is \(\mu\)-measurable, being glued from countably many measurable pieces. Then \(\psi_\phi(x)\geq c'\mu(A\cap K)\geq c'\|x\|_1\). \(\square\)

For nonseparable \(E\), the function \(\phi\) in part 2 need not be unique l.a.e. The phenomenon is the same as in Proposition 7.6(3).

## 7. Operator-valued functions and decomposable operators

From now on, the Banach space is a Hilbert space \(\mathfrak h\). We identify \(L^2_{\mathfrak h}(\Gamma,\mu)\) with \(L^2(\Gamma,\mu)\otimes\mathfrak h\), and study the operators given by bounded operator-valued functions.

**Proposition 7.1.**

1. The map \(f\otimes\xi\mapsto f(\cdot)\xi\), for \(f\in L^2(\Gamma,\mu)\) and \(\xi\in\mathfrak h\), extends to a unitary from the Hilbert tensor product \(L^2(\Gamma,\mu)\otimes\mathfrak h\) onto \(L^2_{\mathfrak h}(\Gamma,\mu)\).
2. For \(F\in L^\infty(\Gamma,\mu)\), \((\pi(F)\zeta)(\gamma)=F(\gamma)\zeta(\gamma)\) defines \(\pi(F)\in B(L^2_{\mathfrak h})\). Under the unitary of part 1, \(\pi(F)=\pi_0(F)\otimes1\). If \(\mathfrak h\neq0\), \(\pi\) is an isometric unital \(*\)-isomorphism of \(L^\infty\) onto its image \(\mathcal A\), the *diagonal algebra*.

**Proof.** (1) For \(f,g\in K(\Gamma)\) and \(\xi,\eta\in\mathfrak h\), \(\langle f(\cdot)\xi,g(\cdot)\eta\rangle=\int f\bar g\,d\mu\,\langle\xi,\eta\rangle=\langle f,g\rangle\langle\xi,\eta\rangle\). So the map is isometric on the algebraic tensor product \(K(\Gamma)\odot\mathfrak h\). This space is dense in \(L^2\otimes\mathfrak h\), because \(K(\Gamma)\) is dense in \(L^2\) (Corollary 5.4(1)), and its image \(K(\Gamma)\otimes\mathfrak h\) is dense in \(L^2_{\mathfrak h}\) (Theorem 5.3). So the map extends to a unitary. By continuity, the extension sends \(f\otimes\xi\) to \(f(\cdot)\xi\) for every \(f\in L^2\). (2) The operator identity is checked on elementary tensors. The norm is computed as in Proposition 2.5(3), with vectors \(1_{A\cap K}\xi_0\) for a unit vector \(\xi_0\). \(\square\)

**Lemma 7.2.** Let \(x:\Gamma\to B(\mathfrak h)\) be such that \(\gamma\mapsto x(\gamma)\xi\) is \(\mu\)-measurable for every \(\xi\in\mathfrak h\). Then \(\gamma\mapsto x(\gamma)\zeta(\gamma)\) is \(\mu\)-measurable for every \(\mu\)-measurable \(\zeta:\Gamma\to\mathfrak h\).

**Proof.** Fix a compact \(K\) and \(\varepsilon>0\), and choose a compact \(K_0\subseteq K\) with \(\mu(K\setminus K_0)<\varepsilon\) and \(\zeta|_{K_0}\) continuous. By Proposition 5.2 there are \(\zeta_n=\sum_ig_{n,i}\otimes\xi_{n,i}\in C(K_0)\otimes\mathfrak h\) with \(\zeta_n\to\zeta\) uniformly on \(K_0\). Extend each \(g_{n,i}\) by \(0\) off \(K_0\); the result is a Borel function, hence \(\mu\)-measurable (Lemma 1.2(4)). So the functions \(\gamma\mapsto\sum_ig_{n,i}(\gamma)x(\gamma)\xi_{n,i}\) are \(\mu\)-measurable, by Lemma 1.2(2). They converge at every point to \(1_{K_0}(\gamma)x(\gamma)\zeta(\gamma)\), because each \(x(\gamma)\) is bounded. By Lemma 1.2(3), \(1_{K_0}x(\cdot)\zeta(\cdot)\) is \(\mu\)-measurable. Hence it is continuous on a compact \(K_1\subseteq K_0\) with \(\mu(K_0\setminus K_1)<\varepsilon\), and there it equals \(x(\cdot)\zeta(\cdot)\). \(\square\)

**Example 7.3** (The adjoint can fail to be measurable). Let \(\Gamma=[0,1]\) with Lebesgue measure, and let \(\mathfrak h=\ell^2([0,1])\) with orthonormal basis \((\varepsilon_t)_{t\in[0,1]}\). Put \(u(t)\xi=\langle\xi,\varepsilon_t\rangle\varepsilon_0\). For each \(\xi\), \(\langle\xi,\varepsilon_t\rangle\neq0\) for only countably many \(t\), so \(u(\cdot)\xi=0\) a.e. and is \(\mu\)-measurable. But \(u(t)^*\eta=\langle\eta,\varepsilon_0\rangle\varepsilon_t\), so \(u(t)^*\varepsilon_0=\varepsilon_t\), and \(\|\varepsilon_s-\varepsilon_t\|=\sqrt2\) for \(s\neq t\). A compact set of positive measure is infinite, so it contains a limit of its other points, and \(t\mapsto\varepsilon_t\) is not continuous there. So \(u(\cdot)^*\varepsilon_0\) is not \(\mu\)-measurable.

**Definition 7.4** (Measurable operator fields). A map \(x:\Gamma\to B(\mathfrak h)\) is *measurable* if \(\gamma\mapsto x(\gamma)\xi\) and \(\gamma\mapsto x(\gamma)^*\xi\) are \(\mu\)-measurable for every \(\xi\in\mathfrak h\).

By Example 7.3, the second condition does not follow from the first.

**Proposition 7.5.**

1. Under pointwise operations, the measurable maps \(\Gamma\to B(\mathfrak h)\) form a \(*\)-algebra.
2. If \(\mathfrak h\) is separable, the adjoint condition in Definition 7.4 is automatic, and \(\gamma\mapsto\|x(\gamma)\|\) is \(\mu\)-measurable.
3. If \(x\) is measurable and bounded, that is \(\sup_\gamma\|x(\gamma)\|<\infty\), then \((X\zeta)(\gamma)=x(\gamma)\zeta(\gamma)\) defines \(X=\int^\oplus x\in B(L^2_{\mathfrak h})\) with \(\|X\|\leq\sup_\gamma\|x(\gamma)\|\). Such operators are called *decomposable*. For a bounded representative \(F_0\) of \(F\in L^\infty\), \(\pi(F)=\int^\oplus F_0(\gamma)1\); such operators are called *diagonal*.
4. The map \(x\mapsto\int^\oplus x\) is linear and multiplicative, and \((\int^\oplus x)^*=\int^\oplus x^*\). Decomposable operators commute with \(\mathcal A\).
5. If \(\mathfrak h\) is separable, then \(\|\int^\oplus x\|=\operatorname{ess\,sup}_\gamma\|x(\gamma)\|\), the essential supremum with respect to locally null sets.

**Proof.** (1) \((xy)(\cdot)\xi=x(\cdot)\big(y(\cdot)\xi\big)\) is \(\mu\)-measurable by Lemma 7.2, and so is \((xy)^*(\cdot)\xi=y^*(\cdot)(x^*(\cdot)\xi)\). Sums and adjoints are clear.

(2) \(\langle x(\gamma)^*\xi,\eta\rangle=\overline{\langle x(\gamma)\eta,\xi\rangle}\) is \(\mu\)-measurable, so Corollary 4.2 applies to \(x(\cdot)^*\xi\). For the norm, take the supremum of \(\|x(\gamma)\xi_n\|\) over a sequence \((\xi_n)\) that is dense in the unit ball.

(3) With \(c=\sup_\gamma\|x(\gamma)\|\), \(x(\cdot)\zeta(\cdot)\) is \(\mu\)-measurable by Lemma 7.2, and \(\|x(\gamma)\zeta(\gamma)\|\leq c\|\zeta(\gamma)\|\).

(4) This is pointwise; for the adjoint, \(\int\langle x(\gamma)\zeta(\gamma),\eta(\gamma)\rangle\,d\mu=\int\langle\zeta(\gamma),x(\gamma)^*\eta(\gamma)\rangle\,d\mu\).

(5) The inequality \(\leq\) is the estimate of (3), since \(\|x(\gamma)\zeta(\gamma)\|\leq\operatorname{ess\,sup}\|x(\cdot)\|\,\|\zeta(\gamma)\|\) l.a.e. Conversely, let \(c<\operatorname{ess\,sup}\|x(\cdot)\|\). Then \(A=\{\|x(\cdot)\|>c\}\) is not locally null, so some compact \(K\) has \(\mu(A\cap K)>0\). Let \((\xi_n)\) be dense in the unit ball. For \(\gamma\in A\cap K\), let \(\zeta(\gamma)=\xi_n\) for the first \(n\) with \(\|x(\gamma)\xi_n\|>c\); let \(\zeta=0\) elsewhere. This \(\zeta\) is \(\mu\)-measurable, being glued from countably many pieces, and \(\|X\zeta\|\geq c\|\zeta\|>0\). The same argument is used for decomposable operators on direct integrals. \(\square\)

Without separability, the norm formula of part 5 fails: Proposition 7.6(3) gives a field with \(\|x(t)\|=1\) for every \(t\) and \(\int^\oplus x=0\).

**Proposition 7.6** (When two fields define the same operator). Let \(x,y:\Gamma\to B(\mathfrak h)\) be bounded and measurable.

1. \(\int^\oplus x=\int^\oplus y\) if and only if, for every \(\xi\in\mathfrak h\), \(x(\gamma)\xi=y(\gamma)\xi\) l.a.e. In that case, for every countable \(S\subseteq\mathfrak h\), \(x(\gamma)|_S=y(\gamma)|_S\) l.a.e.
2. If \(\mathfrak h\) is separable, \(\int^\oplus x=\int^\oplus y\) implies \(x=y\) l.a.e.
3. Let \(\Gamma=[0,1]\) with Lebesgue measure, \(\mathfrak h=\ell^2([0,1])\) with orthonormal basis \((\varepsilon_t)\) as in Example 7.3, and let \(e(t)\) be the projection onto \(\mathbb C\varepsilon_t\). Then \(e\) is bounded and measurable and \(\int^\oplus e=0\), but \(\|e(t)\|=1\) for every \(t\).

**Proof.** (1) If the pointwise condition holds, the two operators agree on the dense set \(K(\Gamma)\otimes\mathfrak h\). Conversely, apply both operators to \(1_K\xi\) for a compact \(K\): the results agree in \(L^2_{\mathfrak h}\), so \(x(\gamma)\xi=y(\gamma)\xi\) for almost every \(\gamma\in K\), and hence l.a.e. The statement about a countable \(S\) follows because a countable union of locally null sets is locally null. (2) Take \(S\) countable and dense; bounded operators that agree on a dense set are equal. (3) \(e(t)\xi=\langle\xi,\varepsilon_t\rangle\varepsilon_t\) vanishes except for countably many \(t\). Also \(e(t)^*=e(t)\). So \(e\) is measurable, \(e(\cdot)\xi=0\) l.a.e. for every \(\xi\), and \(\int^\oplus e=0\) by (1). \(\square\)

**Remark 7.7** (Why nonseparable fibres need more). Two fields that represent one operator agree l.a.e. on every countable set of vectors, by Proposition 7.6(1). Yet they can differ at every point, by Proposition 7.6(3). The proof that operators commuting with the diagonal algebra are decomposable, for separable fibres, builds each fibre from countably many matrix coefficients. On a nonseparable \(\mathfrak h\), a bounded operator is not determined by countably many coefficients, so such a construction cannot produce the field. Some coherent choice over uncountably many null sets is needed. A selector makes that choice (Theorem 8.3).

## 8. Operators that commute with the diagonal algebra

We now prove the converse of Proposition 7.5(4): every operator that commutes with the diagonal algebra \(\mathcal A\) is decomposable. For separable \(\mathfrak h\) no selector is needed (Theorem 8.2). For arbitrary \(\mathfrak h\), a selector produces the field directly from the scalar densities of matrix coefficients in Lemma 8.1 (Theorem 8.3).

**Lemma 8.1** (Coefficient densities). Let \(T\in\mathcal A'\) on \(L^2_{\mathfrak h}(\Gamma,\mu)\). For bounded \(h\) and \(\xi\in\mathfrak h\), write \(h\xi\) for the function \(\gamma\mapsto h(\gamma)\xi\). For \(\xi,\eta\in\mathfrak h\) there is a unique \(F^T_{\xi,\eta}\in L^\infty(\Gamma,\mu)\) with
\[
\langle T(h\xi),1_K\eta\rangle=\int_\Gamma h\,F^T_{\xi,\eta}\,d\mu
\tag{8.1}
\]
for every compact \(K\) and every bounded \(\mu\)-measurable \(h\) that vanishes off \(K\). Moreover:

1. \(\|F^T_{\xi,\eta}\|_\infty\leq\|T\|\,\|\xi\|\,\|\eta\|\), and \((\xi,\eta)\mapsto F^T_{\xi,\eta}\) is sesquilinear;
2. \(F^{T^*}_{\eta,\xi}=\overline{F^T_{\xi,\eta}}\);
3. for \(a\in B(\mathfrak h)\), let \(1\otimes a\) be the decomposable operator with constant field \(a\). Then \(F^{T(1\otimes a)}_{\xi,\eta}=F^T_{a\xi,\eta}\) and \(F^{(1\otimes a)T}_{\xi,\eta}=F^T_{\xi,a^*\eta}\);
4. \(\langle T(f\xi),g\eta\rangle=\int f\bar g\,F^T_{\xi,\eta}\,d\mu\) for bounded \(f,g\) that vanish off compact sets.

**Proof.** Fix \(\xi,\eta\), and put \(\Lambda(h)=\langle T(h\xi),1_K\eta\rangle\) for \(h\) vanishing off \(K\). If \(K\subseteq K'\), then \(\langle T(h\xi),1_{K'}\eta\rangle=\langle T\pi(1_K)(h\xi),1_{K'}\eta\rangle=\langle T(h\xi),1_K\eta\rangle\), since \(T\) commutes with the projection \(\pi(1_K)\). So \(\Lambda\) does not depend on \(K\). Write \(h=u|h|\) with \(|u|=1\). Since \(T\) commutes with \(\pi(|h|^{1/2})\), we get \(\Lambda(h)=\langle T\pi(u)(|h|^{1/2}\xi),|h|^{1/2}\eta\rangle\). So \(|\Lambda(h)|\leq\|T\|\,\||h|^{1/2}\xi\|\,\||h|^{1/2}\eta\|=\|T\|\,\|h\|_1\|\xi\|\|\eta\|\). By Proposition 2.5(1), such \(h\) are dense in \(L^1\), so \(\Lambda\) extends to a bounded functional on \(L^1\). Proposition 2.5(2) then gives the unique \(F^T_{\xi,\eta}\) and the bound in part 1; sesquilinearity is clear from (8.1).

(2) Since \(T^*\in\mathcal A'\) and \(T\) commutes with \(\pi(\bar h)\), \(\langle T^*(h\eta),1_K\xi\rangle=\overline{\langle T(1_K\xi),h\eta\rangle}=\overline{\langle T(\bar h\xi),1_K\eta\rangle}=\int h\overline{F^T_{\xi,\eta}}\).

(3) \(1\otimes a\) commutes with \(\mathcal A\) and maps \(h\xi\) to \(h\,a\xi\). So \(\langle T(1\otimes a)(h\xi),1_K\eta\rangle=\langle T(h\,a\xi),1_K\eta\rangle\) and \(\langle(1\otimes a)T(h\xi),1_K\eta\rangle=\langle T(h\xi),1_K\,a^*\eta\rangle\).

(4) If \(f\) and \(g\) vanish off \(K\), then \(\langle T(f\xi),g\eta\rangle=\langle T\pi(f)(1_K\xi),\pi(g)(1_K\eta)\rangle=\langle T\pi(f\bar g)(1_K\xi),1_K\eta\rangle\), and (8.1) applies. \(\square\)

**Theorem 8.2** (Separable fibres). Let \(\mathfrak h\) be separable. Every \(T\in\mathcal A'\) is decomposable: \(T=\int^\oplus x\) with \(x\) bounded and measurable and \(\|x(\gamma)\|\leq\|T\|\) for every \(\gamma\).

**Proof.** Put \(P_i=\pi(1_{K_i})\). These projections are pairwise orthogonal, and \(\sum_iP_i\zeta=\zeta\) for every \(\zeta\), by Lemma 2.3(2)–(3) applied to \(\|\zeta(\cdot)\|^2\). \(T\) commutes with each \(P_i\). Fix \(i\). The restriction of \(\mu\) to \(K_i\) is a finite Radon measure on the compact space \(K_i\), with the same measurable functions. By Corollary 5.4(3), applied to this finite measure, \(P_iL^2_{\mathfrak h}\) is the direct integral \(H_i\) of the constant field \(\mathfrak h\) over \((K_i,\Sigma_\mu|_{K_i},\mu)\). There the operators \(\pi(F)|_{P_iL^2}\) are the diagonal operators \(m_{F|K_i}\). So \(T_i=T|_{P_iL^2}\) commutes with the diagonal operators of \(H_i\). The theorem that decomposable operators are those commuting with the diagonal algebra, for \(\sigma\)-finite measures and separable fibres, then gives a measurable field \(x_i\) on \(K_i\) with \(\|x_i(\gamma)\|\leq\|T\|\) for every \(\gamma\) and \(T_i=\int^\oplus x_i\). Since \(x_i\) is a measurable field of bounded operators, \(x_i(\cdot)\xi\) and \(x_i(\cdot)^*\xi\) are measurable sections for every \(\xi\), that is, \(\mu\)-measurable maps on \(K_i\) (Proposition 4.3(2)). Let \(x=x_i\) on \(K_i\) and \(x=0\) on \(N\). By the gluing property of Lemma 2.1, \(x\) is measurable. It is bounded by \(\|T\|\), and \(\int^\oplus x\) agrees with \(T\) on each \(P_iL^2_{\mathfrak h}\). Both operators commute with every \(P_i\), so they are equal. \(\square\)

**Theorem 8.3** (Arbitrary fibres). Suppose \((\Gamma,\mu)\) has a selector \(s\), for instance a lifting (Proposition 3.3). For \(T\in\mathcal A'\), define \(x^s_T(\gamma)\in B(\mathfrak h)\) by
\[
\langle x^s_T(\gamma)\xi,\eta\rangle=s\big(F^T_{\xi,\eta}\big)(\gamma)\qquad(\xi,\eta\in\mathfrak h,\ \gamma\in\Gamma).
\tag{8.2}
\]
Then \(x^s_T\) is bounded and measurable, \(\|x^s_T(\gamma)\|\leq\|T\|\) for every \(\gamma\), and \(T=\int^\oplus x^s_T\). Consequently, a bounded operator on \(L^2_{\mathfrak h}(\Gamma,\mu)\) is decomposable exactly when it commutes with \(\mathcal A\).

*Remark.* The last statement is often proved with a lifting. Here a selector is enough, and for separable \(\mathfrak h\) none is needed (Theorem 8.2); the same holds for the duality results of Sections 6 and 9.

**Proof.** *Step 1: fibres.* By (S2) and Lemma 8.1(1), the right side of (8.2) is sesquilinear in \((\xi,\eta)\). By (S3), it is bounded by \(\|T\|\|\xi\|\|\eta\|\). A bounded sesquilinear form is given by a bounded operator, so (8.2) defines \(x^s_T(\gamma)\), with \(\|x^s_T(\gamma)\|\leq\|T\|\).

*Step 2: adjoint.* By Lemma 8.1(2) and (S4), \(\langle x^s_{T^*}(\gamma)\eta,\xi\rangle=\overline{s(F^T_{\xi,\eta})(\gamma)}=\langle x^s_T(\gamma)^*\eta,\xi\rangle\). So \(x^s_{T^*}(\gamma)=x^s_T(\gamma)^*\) for every \(\gamma\).

*Step 3: measurability.* Fix \(\xi\). We check the two conditions of Theorem 4.1 for \(\gamma\mapsto x^s_T(\gamma)\xi\). Condition 1: \(\langle x^s_T(\cdot)\xi,\eta\rangle=s(F^T_{\xi,\eta})\) is \(\mu\)-measurable by (S1). Condition 2: fix a compact \(K\). The vector \(T(1_K\xi)\) is a \(\mu\)-measurable function (Theorem 5.3). By Theorem 4.1 there are a separable closed subspace \(\mathfrak K\subseteq\mathfrak h\) and a null set \(Z\subseteq K\) with \(T(1_K\xi)(\gamma)\in\mathfrak K\) for \(\gamma\in K\setminus Z\). Let \(\eta\perp\mathfrak K\). For bounded \(h\) vanishing off \(K\), (8.1) gives
\(\int hF^T_{\xi,\eta}=\langle\pi(h)T(1_K\xi),1_K\eta\rangle=\int_Kh(\gamma)\langle T(1_K\xi)(\gamma),\eta\rangle\,d\mu=0\).
So \(F^T_{\xi,\eta}=0\) l.a.e. on \(K\). By (S5), \(\langle x^s_T(\gamma)\xi,\eta\rangle=0\) for every \(\gamma\in K\setminus N_K\) and every \(\eta\perp\mathfrak K\); the set \(N_K\) does not depend on \(\eta\). Hence \(x^s_T(\gamma)\xi\in\mathfrak K\) for \(\gamma\in K\setminus N_K\). So \(x^s_T(\cdot)\xi\) is \(\mu\)-measurable. By Step 2, the same argument applied to \(T^*\) handles \(x^s_T(\cdot)^*\xi\).

*Step 4: \(T=\int^\oplus x^s_T\).* For \(f,g\in K(\Gamma)\), Lemma 8.1(4) and (S1) give
\(\langle(\int^\oplus x^s_T)(f\xi),g\eta\rangle=\int f\bar g\,s(F^T_{\xi,\eta})\,d\mu=\int f\bar g\,F^T_{\xi,\eta}\,d\mu=\langle T(f\xi),g\eta\rangle\).
Since \(K(\Gamma)\otimes\mathfrak h\) is dense, \(T=\int^\oplus x^s_T\). Conversely, decomposable operators commute with \(\mathcal A\), by Proposition 7.5(4). \(\square\)

**Corollary 8.4.**

1. For every positive Radon measure, \(\pi_0(L^\infty)\) is maximal abelian on \(L^2(\Gamma,\mu)\). No lifting is needed.
2. Let \(\mathcal D\) be the algebra of decomposable operators on \(L^2_{\mathfrak h}\). If \(\mathfrak h\) is separable, or if a selector exists, then \(\mathcal A'=\mathcal D\) and \(\mathcal D'=\mathcal A\). Both are von Neumann algebras, and the centre of \(\mathcal D\) is \(\mathcal A\).

**Proof.** (1) Apply Theorem 8.2 with \(\mathfrak h=\mathbb C\): every operator in \(\mathcal A'\) is multiplication by a bounded \(\mu\)-measurable function, so \(\mathcal A'=\mathcal A\).

(2) \(\mathcal A'=\mathcal D\) by Theorem 8.2 or 8.3, and \(\mathcal A\subseteq\mathcal D'\) by Proposition 7.5(4). Let \(S\in\mathcal D'\). Diagonal operators are decomposable, so \(S\in\mathcal A'\), and \(S\) commutes with every \(1\otimes a\).

*With a selector:* Lemma 8.1(3) gives \(F^S_{a\xi,\eta}=F^S_{\xi,a^*\eta}\). By (S2), \(x^s_S(\gamma)a=a\,x^s_S(\gamma)\) for every \(\gamma\) and every \(a\in B(\mathfrak h)\). So \(x^s_S(\gamma)=c(\gamma)1\) with \(c=s(F^S_{\xi_0,\xi_0})\) for a unit vector \(\xi_0\). Thus \(S=\pi(c)\).

*Separable \(\mathfrak h\):* write \(S=\int^\oplus y\) by Theorem 8.2. \(S\) commutes with the constant fields given by the matrix units of an orthonormal basis. By the uniqueness in Proposition 7.6(2), \(y(\gamma)\) commutes with these matrix units for l.a.e. \(\gamma\), so the fibres are scalar l.a.e., exactly as in [the \(\sigma\)-finite case](../OA-FOUND-REMAINDER/reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-06).

The remaining statements follow as for [mutual commutants over a \(\sigma\)-finite measure](../OA-FOUND-REMAINDER/reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-06): \(\mathcal A''=\mathcal D'=\mathcal A\) and \(\mathcal D''=\mathcal A'''=\mathcal A'=\mathcal D\), so both are von Neumann algebras; and the centre \(\mathcal D\cap\mathcal D'\) of \(\mathcal D\) is \(\mathcal A\), because \(\mathcal A\) is abelian and so \(\mathcal A\subseteq\mathcal A'=\mathcal D\). \(\square\)

**Remark 8.5** (Comparison with the \(\sigma\)-finite theory). The theorem that decomposable operators are those commuting with the diagonal algebra over a \(\sigma\)-finite measure space, and Theorem 8.3, generalize in different directions.

- The \(\sigma\)-finite theorem allows any \(\sigma\)-finite measure space \((\Gamma,\Sigma,\mu)\) without topology, and fields whose separable fibres vary.
- Theorem 8.3 allows a Radon measure that need not be \(\sigma\)-finite, and a constant fibre that need not be separable.
- Where they overlap, for a \(\sigma\)-finite Radon measure with a separable constant fibre, they are the same statement, by Proposition 4.3 and Corollary 5.4(3).
- Theorem 8.2 extends the method of test vectors and coefficient densities and the pointwise bound, which needs no lifting, to all Radon measures. It uses the decomposition of Lemma 2.1 and applies the \(\sigma\)-finite theorem on each finite piece.
- Theorem 8.3 covers nonseparable fibres. It needs a selector, for the reason given in Remark 7.7.

## 9. The predual of \(L^\infty(\Gamma,\mu)\bar\otimes M\)

Let \(M\) be a von Neumann algebra on \(\mathfrak h\), that is, a \(*\)-algebra of operators with \(M''=M\). Let \(M_*\) be the space of \(\sigma\)-weakly continuous functionals on \(M\). We use three standard facts about it (see Results used from other lessons):

- each \(\psi\in M_*\) has the form \(\psi(a)=\sum_n\langle a\xi_n,\eta_n\rangle\), with \(\sum\|\xi_n\|^2<\infty\) and \(\sum\|\eta_n\|^2<\infty\);
- \(M_*\) is norm closed in \(M^*\);
- \(M\) is the dual of \(M_*\).

Let \(\mathcal N=(\mathcal A\cup(1\otimes M))''\), where \(1\otimes M=\{1\otimes a:a\in M\}\). It is the smallest von Neumann algebra on \(L^2_{\mathfrak h}(\Gamma,\mu)\) that contains \(\mathcal A\) and \(1\otimes M\). Under the unitary of Proposition 7.1, \(\mathcal A=\pi_0(L^\infty)\otimes1\), and \(\pi_0(L^\infty)\) is a von Neumann algebra by Corollary 8.4(1). So \(\mathcal N\) is the spatial tensor product of \(\pi_0(L^\infty)\) and \(M\). As a W\(^*\)-algebra, \(\mathcal N\) is therefore the tensor product \(L^\infty(\Gamma,\mu)\bar\otimes M\), with \(\pi(F)(1\otimes a)\) corresponding to \(F\otimes a\), because the tensor product of W\(^*\)-algebras does not depend on the faithful normal representations used (see Results used from other lessons). This applies here for three reasons. \(L^\infty(\Gamma,\mu)\) is a W\(^*\)-algebra, with predual \(L^1\) by Proposition 2.5(2). \(\pi_0\) is faithful, by Proposition 2.5(3). And \(\pi_0\) is normal, since \(\langle\pi_0(F)f,g\rangle=\int Ff\bar g\,d\mu\) with \(f\bar g\in L^1\). We use this identification only to state part 3 of the next theorem in abstract form.

**Theorem 9.1** (The predual of \(L^\infty(\Gamma,\mu)\bar\otimes M\)). Suppose \((\Gamma,\mu)\) has a selector \(s\), or \(\mathfrak h\) is separable.

1. Every \(T\in\mathcal N\) is \(\int^\oplus x_T\) for a bounded measurable field \(x_T\) with \(x_T(\gamma)\in M\) and \(\|x_T(\gamma)\|\leq\|T\|\) for every \(\gamma\). With a selector we take \(x_T=x^s_T\). Conversely, every bounded measurable field with values in \(M\) l.a.e. defines an element of \(\mathcal N\).
2. For \(\omega\in L^1_{M_*}(\Gamma,\mu)\) and \(T\in\mathcal N\), the function \(\gamma\mapsto\omega(\gamma)(x_T(\gamma))\) is \(\mu\)-measurable and integrable. The integral
\[
\Psi(\omega)(T)=\int_\Gamma\omega(\gamma)\big(x_T(\gamma)\big)\,d\mu(\gamma)
\tag{9.1}
\]
does not depend on the \(M\)-valued measurable field chosen to represent \(T\).
3. The map \(\Psi\) of (9.1) is an isometric isomorphism of \(L^1_{M_*}(\Gamma,\mu)\) onto \(\mathcal N_*\). On elementary tensors, \(\Psi(f\otimes\psi)(\pi(F)(1\otimes a))=\int fF\,d\mu\,\psi(a)\). With the identification of \(\mathcal N\) with \(L^\infty(\Gamma,\mu)\bar\otimes M\) above, this says \((L^\infty(\Gamma,\mu)\bar\otimes M)_*=L^1_{M_*}(\Gamma,\mu)\).
4. The field \(x_T\) is a bounded \(M\)-valued function for which \(\gamma\mapsto\psi(x_T(\gamma))\) is \(\mu\)-measurable for every \(\psi\in M_*\), and \(\langle T,\omega\rangle=\int\omega(\gamma)(x_T(\gamma))\,d\mu\). It is measurable in the sense of Definition 7.4.

**Proof with a selector.** (1) \(\mathcal A\) is abelian and commutes with \(1\otimes M\). So both generating sets of \(\mathcal N\) lie in the von Neumann algebra \(\mathcal A'\), and \(\mathcal N\subseteq\mathcal A'\). Theorem 8.3 gives \(x^s_T\) with \(\|x^s_T(\gamma)\|\leq\|T\|\). For \(b\in M'\), the operator \(1\otimes b\) commutes with \(\mathcal A\) and with \(1\otimes M\), hence with \(\mathcal N\). By Lemma 8.1(3), \(F^T_{b\xi,\eta}=F^T_{\xi,b^*\eta}\). Applying \(s\) gives \(x^s_T(\gamma)b=b\,x^s_T(\gamma)\) for every \(\gamma\). So \(x^s_T(\gamma)\in M''=M\).

Conversely, let \(y\) be bounded and measurable with \(y(\gamma)\in M\) l.a.e., and let \(R\in\mathcal N'\). Then \(R\in\mathcal A'\) and \(R\) commutes with \(1\otimes M\). So, as above, \(x^s_R(\gamma)\in M'\) for every \(\gamma\). Hence \(y(\gamma)x^s_R(\gamma)=x^s_R(\gamma)y(\gamma)\) l.a.e., and \(\int^\oplus y\) commutes with \(R=\int^\oplus x^s_R\). Therefore \(\int^\oplus y\in\mathcal N''=\mathcal N\).

(2) For \(\psi=\sum_n\langle\cdot\,\xi_n,\eta_n\rangle\in M_*\), \(\psi(x_T(\gamma))=\sum_n\langle x_T(\gamma)\xi_n,\eta_n\rangle\), a uniformly convergent series of \(\mu\)-measurable functions. So \(x_T\) satisfies the hypothesis of Lemma 6.3 with \(E=M_*\) and \(E^*=M\). That lemma gives measurability of \(\gamma\mapsto\omega(\gamma)(x_T(\gamma))\), which is bounded by \(\|T\|\|\omega(\gamma)\|\).

*Independence.* Let \(y\) be another bounded \(M\)-valued measurable field with \(\int^\oplus y=T\), and fix a compact \(K\). By Theorem 4.1, \(\omega\) takes values in a separable closed subspace \(\mathcal S\subseteq M_*\) outside a null subset of \(K\). Pick a dense sequence \((\psi_m)\) in \(\mathcal S\), and write \(\psi_m(a)=\sum_n\langle a\xi_{m,n},\eta_{m,n}\rangle\). Let \(e\) be the projection onto the closed span of all \(\xi_{m,n}\) and \(\eta_{m,n}\), a separable space. If \(a,b\in M\) and \(eae=ebe\), then \(\psi_m(a)=\psi_m(b)\) for all \(m\), hence \(\psi(a)=\psi(b)\) for all \(\psi\in\mathcal S\). By Proposition 7.6(1), applied to a countable dense subset of \(e\mathfrak h\), we have \(e\,x_T(\gamma)e=e\,y(\gamma)e\) for almost every \(\gamma\in K\). So \(\omega(\gamma)(x_T(\gamma))=\omega(\gamma)(y(\gamma))\) almost everywhere on \(K\).

(3) *Normality.* Let \(\omega=f\otimes\omega_{\xi,\eta}\), where \(f\in L^1\) and \(\omega_{\xi,\eta}(a)=\langle a\xi,\eta\rangle\). Write \(f=f_1\bar f_2\) with \(f_1,f_2\in L^2\). Then \(\Psi(\omega)(T)=\int f\langle x_T(\gamma)\xi,\eta\rangle\,d\mu=\langle T(f_1\xi),f_2\eta\rangle\), a vector functional, which is \(\sigma\)-weakly continuous. Finite sums of such \(\omega\) are dense in \(L^1_{M_*}\), by Theorem 5.6 and the form of the elements of \(M_*\). Also \(|\Psi(\omega)(T)|\leq\|T\|\|\omega\|_1\). Since \(\mathcal N_*\) is norm closed, \(\Psi\) is a contraction into \(\mathcal N_*\).

*Isometry.* Let \(\omega=\sum_j1_{A_j}\psi_j\) be simple, with disjoint \(A_j\) of finite measure. Given \(\varepsilon>0\), pick \(a_j\in M\) with \(\|a_j\|\leq1\) and \(\psi_j(a_j)\geq\|\psi_j\|-\varepsilon\). Put \(T=\sum_j\pi(1_{A_j})(1\otimes a_j)\in\mathcal N\). Then \(T^*T=\sum_j\pi(1_{A_j})(1\otimes a_j^*a_j)\leq1\), so \(\|T\|\leq1\), and \(T\) has the \(M\)-valued field \(\sum_j1_{A_j}a_j\). By (2), \(\Psi(\omega)(T)=\sum_j\mu(A_j)\psi_j(a_j)\geq\|\omega\|_1-\varepsilon\sum_j\mu(A_j)\). Simple elements are dense in \(L^1_{M_*}\) (see the proof of Theorem 5.6), so \(\Psi\) is isometric.

*Onto.* Let \(\Xi,H\in L^2_{\mathfrak h}\), and put \(\omega(\gamma)=\omega_{\Xi(\gamma),H(\gamma)}|_M\). Since \(\|\omega_{\xi,\eta}-\omega_{\xi',\eta'}\|\leq\|\xi-\xi'\|\|\eta\|+\|\xi'\|\|\eta-\eta'\|\), this is \(\mu\)-measurable (Lemma 1.2(2)). It lies in \(L^1_{M_*}\), with norm at most \(\|\Xi\|\|H\|\). Moreover \(\Psi(\omega)(T)=\int\langle x_T(\gamma)\Xi(\gamma),H(\gamma)\rangle\,d\mu=\langle T\Xi,H\rangle\). So every vector functional on \(\mathcal N\) lies in the range of \(\Psi\). Every element of \(\mathcal N_*\) is a norm-convergent sum of vector functionals, by the form of normal functionals. The range of an isometry is closed, so \(\Psi\) is onto. On \(T=\pi(F)(1\otimes a)\), Lemma 8.1(3) gives the field \(F_0(\gamma)a\), which proves the formula on elementary tensors.

(4) This follows from parts 1 and 2 and Theorem 8.3. \(\square\)

**Proof when \(\mathfrak h\) is separable, without a selector.** Use the fields of Theorem 8.2. They are unique l.a.e. (Proposition 7.6(2)), which gives the independence in (2) directly. The unit ball of \(B(\mathfrak h)\) with the strong topology embeds in \(\mathfrak h^{\mathbb N}\) via \(b\mapsto(b\xi_k)_k\), for a dense sequence \((\xi_k)\), so every subset of it is separable. So \(M'\) and \(M\) contain countable subsets whose commutants are \(M''=M\) and \(M'\), respectively. Commuting with those countable sets holds l.a.e., by Proposition 7.6(2). This replaces the pointwise identities in (1): the field \(x\) of Theorem 8.2 for \(T\) has \(x(\gamma)\in M\) outside a locally null set \(Z\). Put \(x_T=x\) off \(Z\) and \(x_T=0\) on \(Z\). This changes neither measurability (Lemma 1.2(1)) nor the operator (Proposition 7.6(1)), and now \(x_T(\gamma)\in M\) for every \(\gamma\), as Lemma 6.3 requires in (2). Parts (3) and (4) are unchanged. \(\square\)

## Exercises

**Exercise 1** (The injective norm is too small). In \(L^1([0,1])\otimes E\), with \(E=\mathbb C^2\) under the maximum norm and standard basis \(\epsilon_1,\epsilon_2\), let \(u=1_{[0,1/2)}\otimes\epsilon_1+1_{[1/2,1]}\otimes\epsilon_2\). Show that \(\|u\|_1=\|u\|_\gamma=1\), but that the injective norm, defined as in Proposition 5.2 with \(L^1\) in place of \(C(\Gamma)\), is \(\lambda(u)=\tfrac12\). So \(L^1\otimes_\lambda E\neq L^1_E\) in general, and the projective norm in Theorem 5.6 is essential.

*Solution.* \(\|u(\gamma)\|=1\) for every \(\gamma\), so \(\|u\|_1=1\), and \(\|u\|_\gamma=1\) by Theorem 5.6. The dual of \(L^1\) is \(L^\infty\), and the dual of \((\mathbb C^2,\max)\) is \(\mathbb C^2\) with the norm \(|c_1|+|c_2|\). So \(\lambda(u)=\sup|c_1\int_0^{1/2}g+c_2\int_{1/2}^1g|\) over \(\|g\|_\infty\leq1\) and \(|c_1|+|c_2|\leq1\). Each integral is at most \(\tfrac12\) in modulus, so \(\lambda(u)\leq\tfrac12\). Equality holds for \(g=1\) and \(c=(1,0)\).

**Exercise 2** (Weak\(^*\) measurable but not measurable). Let \(r_n\) be the Rademacher functions on \([0,1]\): \(r_n(t)=1-2d_n(t)\), where \(d_n(t)\) is the \(n\)-th binary digit. Let \(\phi(t)=(r_n(t))_n\in\ell^\infty=(\ell^1)^*\). Show that \(t\mapsto\phi(t)(a)\) is measurable for every \(a\in\ell^1\), but that \(\phi\) is not \(\mu\)-measurable as a map into \(\ell^\infty\) with its norm.

*Solution.* \(\phi(t)(a)=\sum_na_nr_n(t)\) is a uniformly convergent series of step functions, so it is measurable. Two distinct points that are not dyadic rationals differ in some binary digit, so \(\|\phi(s)-\phi(t)\|_\infty=2\). A compact set of positive measure contains uncountably many non-dyadic points, and hence a non-dyadic point that is a limit of other non-dyadic points of the set. At that point \(\phi\) is not continuous on the set. So \(\phi\) is continuous on no compact set of positive measure.

**Exercise 3** (Fields modulo separable subspaces). Let \(x,y\) be bounded measurable fields. Show that \(\int^\oplus x=\int^\oplus y\) if and only if \(e\,x(\gamma)\,e=e\,y(\gamma)\,e\) l.a.e. for every projection \(e\) onto a separable closed subspace of \(\mathfrak h\).

*Solution.* If \(\int^\oplus x=\int^\oplus y\), apply Proposition 7.6(1) to a countable dense subset of \(e\mathfrak h\). Conversely, fix \(\xi\) and a compact \(K\). By Theorem 4.1, \(x(\cdot)\xi\) and \(y(\cdot)\xi\) take values in separable subspaces outside a null subset of \(K\). Let \(e\) project onto a separable closed subspace that contains these and \(\xi\). For almost every \(\gamma\in K\), \(x(\gamma)\xi=e\,x(\gamma)e\,\xi=e\,y(\gamma)e\,\xi=y(\gamma)\xi\). So \(x(\gamma)\xi=y(\gamma)\xi\) l.a.e., and Proposition 7.6(1) applies.

**Exercise 4** (The field of a projection). Let \(s\) be a selector and \(F\in L^\infty\). Show that the field \(x^s_{\pi(F)}\) of Theorem 8.3 is \(s(F)(\gamma)1\). Then take \(\mathfrak h=\mathbb C\), \(\Gamma=\mathbb R\), \(F=1_{[0,\infty)}\) and the Banach-limit selector. Show that the projection \(\pi(F)\) has the field value \(\tfrac12\) at \(\gamma=0\). Conclude that the selector field of a projection is a projection l.a.e., but not necessarily at every point.

*Solution.* For \(T=\pi(F)\), \(\langle T(h\xi),1_K\eta\rangle=\int hF\,d\mu\,\langle\xi,\eta\rangle\), so \(F^T_{\xi,\eta}=F\langle\xi,\eta\rangle\) and \(x^s_T(\gamma)=s(F)(\gamma)1\). With the Banach-limit selector, \(s(F)(0)=\tfrac12\) by Example 3.5. Since \(s(F)=F\) l.a.e., the field is a projection l.a.e.

## Results used from other lessons

The Riesz representation theorem with property (R) is proved in Haar measure on locally compact groups, and Urysohn's lemma and partitions of unity on locally compact spaces are proved at the start of the same lesson. Direct integrals over \(\sigma\)-finite measure spaces are treated in the two lessons named in the introduction. We also use the following facts.

- **The lifting theorem.** Every complete finite measure space of positive measure has a lifting in the sense of Definition 3.1. This is proved, for all complete strictly localizable measure spaces of positive measure, in The lifting theorem, Theorem 6.2 and Corollary 6.3, following [Fremlin, Measure Theory, Volume 3, Section 341](https://www1.essex.ac.uk/maths/people/fremlin/cont34.htm) (free). It enters only through Proposition 3.3, and only where no other selector is available (for instance, off \(\mathbb R^n\)): in Theorem 8.3 and Corollary 8.4(2) for nonseparable \(\mathfrak h\), in Lemma 6.2 and Theorem 6.4(2) for nonseparable \(E\), and in Theorem 9.1 for nonseparable \(\mathfrak h\).
- **Normal functionals.** Let \(M\) be a von Neumann algebra on \(\mathfrak h\), and let \(M_*\) be the space of its \(\sigma\)-weakly continuous functionals. Every \(\psi\in M_*\) has the form \(\psi(a)=\sum_n\langle a\xi_n,\eta_n\rangle\) with \(\sum_n\|\xi_n\|^2<\infty\) and \(\sum_n\|\eta_n\|^2<\infty\); the space \(M_*\) is norm closed in \(M^*\); and \(a\mapsto(\psi\mapsto\psi(a))\) identifies \(M\) with the dual of \(M_*\). Proved in Compact and trace-class operators, Theorems 9.1(ii) and 9.4; the first statement is
also proved in Spatial tensor products of von Neumann algebras.
- **Tensor products of W\(^*\)-algebras.** Let \(M_1\) and \(M_2\) be W\(^*\)-algebras with faithful normal representations \(\pi_1\) and \(\pi_2\) on Hilbert spaces \(H_1\) and \(H_2\). Up to a \(*\)-isomorphism that carries \(\pi_1(a)\otimes\pi_2(b)\) to \(\pi_1'(a)\otimes\pi_2'(b)\), the von Neumann algebra on \(H_1\otimes H_2\) generated by \(\pi_1(M_1)\otimes1\) and \(1\otimes\pi_2(M_2)\) does not depend on the choice of the representations. It is the W\(^*\)-tensor product \(M_1\bar\otimes M_2\). Proved in Spatial tensor products of von Neumann algebras, Corollaries 8.3 and 8.4. Spatial tensor products and their generators are treated in Spatial tensor products of von Neumann algebras. We use this fact only to state Theorem 9.1(3) in abstract form.
- **Measure theory.** On a finite measure space \((X,\Sigma,\nu)\): monotone convergence (if \(0\leq f_n\uparrow f\) pointwise, then \(\int f_n\,d\nu\to\int f\,d\nu\)); dominated convergence (if \(f_n\to f\) almost everywhere and \(|f_n|\leq g\) with \(g\) integrable, then \(\int|f_n-f|\,d\nu\to0\)); Minkowski's inequality (\(\|f+g\|_p\leq\|f\|_p+\|g\|_p\) for \(1\leq p<\infty\)); and the Radon–Nikodym theorem (a complex measure \(\lambda\) on \(\Sigma\) with \(|\lambda(B)|\leq C\nu(B)\) for all \(B\in\Sigma\) has the form \(\lambda(B)=\int_Bg\,d\nu\) with \(g\) integrable). Proved in Measure and Hilbert space tools for Haar integration, Theorems 2.1, 2.2, 3.1 and 4.1 (for a
complex \(\lambda\), apply Theorem 4.1 to the two parts \(E\mapsto\rho(E\cap H)\) and \(E\mapsto-\rho(E\setminus H)\)
of its real and imaginary parts \(\rho\) given by [Fremlin, Measure Theory, Volume 2, Corollary 231F](https://www1.essex.ac.uk/maths/people/fremlin/cont23.htm), which are bounded by
\(C\nu\)).
- **Differentiation of integrals.** For every locally integrable \(F\) on \(\mathbb R^n\), \(|B(\gamma,r)|^{-1}\int_{B(\gamma,r)}F\,d\mu\to F(\gamma)\) as \(r\to0\), for almost every \(\gamma\) (Lebesgue's differentiation theorem). For \(F=1_K\) this gives Lebesgue's density theorem: almost every point of a measurable set \(K\) is a point of density \(1\) of \(K\). Proved in [Fremlin, Measure Theory, Volume 2, Section 261](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm) (free; density theorems in
\(\mathbb R^r\)). Besicovitch's differentiation theorem gives the same for every Radon measure \(\mu\) on \(\mathbb R^n\), with \(\mu(B(\gamma,r))\) in place of \(|B(\gamma,r)|\) and for \(\mu\)-almost every \(\gamma\). Proved in Besicovitch's covering theorem and the differentiation of Radon measures, Theorem 5.1. Both are used only in Proposition 3.4 and the remark after it.
- **Tietze's extension theorem.** Every continuous function \(g\) on a compact subset \(C\) of a locally compact Hausdorff space \(\Gamma\) extends to a function in \(K(\Gamma)\). Proof from the compact case, Stone–Weierstrass, Proposition 16.1(2): cover \(C\) by finitely many open sets with compact closures (Proposition 4.2 there), let \(V\) be their union, and choose, by the locally compact form of Urysohn's lemma, \(\phi\in K(\Gamma)\) with \(0\le\phi\le1\), \(\phi=1\) on \(C\) and support inside \(V\). The compact case, applied to the real and imaginary parts of \(g\) on the closed subset \(C\) of the compact Hausdorff space \(\overline V\), gives a continuous \(G\) on \(\overline V\) with \(G|_C=g\). The function equal to \(\phi G\) on \(V\) and to \(0\) off the support of \(\phi\) is well defined, continuous on each of these two open sets, which cover \(\Gamma\), and lies in \(K(\Gamma)\). Multiplying by an Urysohn function for \(C\subseteq U\), and composing with the retraction of \(\mathbb C\) onto the closed disc of radius \(\sup_C|g|\), one can also make the support lie in a given open set \(U\supseteq C\) and keep the supremum.
- **Functional analysis.** The Hahn–Banach theorem, in two forms: a real-linear functional on a subspace that is dominated by a sublinear functional \(p\) extends to the whole space, still dominated by \(p\); and every vector \(y\) of a normed space has a functional \(x^*\) with \(\|x^*\|\leq1\) and \(x^*(y)=\|y\|\). Proved in Hahn–Banach, Baire and the basic theorems on Banach spaces, Section 2. Also, a sesquilinear form \(B\) on a Hilbert space with \(|B(\xi,\eta)|\leq C\|\xi\|\|\eta\|\) is \(B(\xi,\eta)=\langle T\xi,\eta\rangle\) for a unique bounded operator \(T\), and \(\|T\|\leq C\). Proved in Hilbert spaces and compact operators, Theorem 3.1.
- **Zorn's lemma.** A nonempty partially ordered set in which every chain has an upper bound has a maximal element. Proved in Hahn–Banach, Baire and the basic theorems on Banach spaces, Section 1, from the
axiom of choice.

## Where this leads

- **Fields that vary.** Direct integrals of fields of Hilbert spaces whose fibres vary, over a Radon measure that need not be \(\sigma\)-finite, and the decomposition of von Neumann algebras over such measures, extend Sections 7 and 8. For \(\sigma\)-finite measures and separable fibres they are treated in Measurable fields of Hilbert spaces and their direct integrals and Decomposable operators and the diagonal algebra.
- **Tensor products.** The commutation theorem \((M_1\bar\otimes M_2)'=M_1'\bar\otimes M_2'\), proved in Spatial tensor products of von Neumann algebras, describes the commutant of the algebra \(\mathcal N\) of Section 9.
- **Liftings.** The lifting theorem is proved in The lifting theorem. Strong liftings, which fix continuous functions, are treated in [Fremlin, Volume 4, Section 453](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm). It is natural to ask whether nonseparable fibres over a general Radon measure can be handled without the lifting theorem, for instance by constructing a selector directly; on \(\mathbb R^n\), Proposition 3.4 does this.
- **The Bochner integral.** Integrals of \(E\)-valued functions themselves are not needed here, since every pairing above is a scalar integral. They are treated in [van Neerven, Section 1.5].

## References



- [Pettis 1938] B. J. Pettis, On integration in vector spaces, *Transactions of the American Mathematical Society* 44 (1938), 277–304. https://doi.org/10.1090/S0002-9947-1938-1501970-8. Free at https://www.ams.org/journals/tran/1938-044-02/S0002-9947-1938-1501970-8/S0002-9947-1938-1501970-8.pdf
- [van Neerven] J. van Neerven, *Functional Analysis*, Cambridge Studies in Advanced Mathematics 201, Cambridge University Press,
  Cambridge, 2022; arXiv:2112.11166, version 7 (17 July 2025). Free at https://arxiv.org/abs/2112.11166
