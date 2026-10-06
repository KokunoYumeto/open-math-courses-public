# Local measurability and Radon integration

*Mathematical exposition by Claude Opus 5.5 (Anthropic), self-checked by the writing AI. CC0 1.0. Independent review of this edition is not asserted.*

This chapter proves local measurability, compact-piece decomposition, and the compact-supremum integral for a Radon measure, without a sigma-finiteness assumption.

The complete proofs of measure convergence and Zorn’s lemma provide the background used below.

## Conventions

Throughout, \(\Gamma\) is a locally compact Hausdorff space, and \(K(\Gamma)\) is the space of continuous complex functions on \(\Gamma\) with compact support. A *positive Radon measure* \(\mu\) is a linear functional on \(K(\Gamma)\) with \(\mu(f)\geq0\) whenever \(f\geq0\). By the Riesz representation theorem, \(\mu(f)=\int f\,d\mu\) for a Radon measure on the Borel sets, which we also write \(\mu\). It is finite on compact sets, outer regular on Borel sets, and inner regular on open sets. The theorem is proved in the lesson [Haar measure on locally compact groups](course:harmonic-analysis-on-locally-compact-groups/haar-measure-on-locally-compact-groups#oa-fnd-hm-01). We use one consequence of regularity:

- **(R)** If \(B\) is a Borel set with \(\mu(B)<\infty\) and \(\varepsilon>0\), there are a compact \(C\subseteq B\) and an open \(U\supseteq B\) with \(\mu(U\setminus C)<\varepsilon\).

It follows from outer regularity together with inner regularity on Borel sets of finite measure, which is proved in the same lesson.

We use the value of \(\mu\) only on Borel subsets of compact sets.

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

*Property 4.* Let \(K\) be compact and \(\varepsilon>0\). If \(\mu(K)=0\), take \(K_0=\varnothing\). Otherwise enumerate the nonempty pieces that meet \(K\) as \(K_{i_1},K_{i_2},\ldots\), allowing a finite list, and choose \(J\geq1\) (all pieces if the list is finite) as follows. Since \(K\cap N\) is null, \(\sum_j\mu(K\cap K_{i_j})=\mu(K)<\infty\), so there is \(J\) with \(\sum_{j>J}\mu(K\cap K_{i_j})<\varepsilon/2\). Choose compact \(C_j\subseteq K_{i_j}\) with \(\mu(K_{i_j}\setminus C_j)<\varepsilon/(2J)\) and \(f|_{C_j}\) continuous. On the compact set \(K_0=K\cap(C_1\cup\cdots\cup C_J)\), a finite disjoint union of compact pieces, \(f\) is continuous. Moreover \(\mu(K\setminus K_0)<\varepsilon\), because \(K\cap N\) is null. \(\square\)

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


**Example 2.7** (A locally null set that is not null). Let \(\Gamma=\mathbb R_d\times\mathbb R\), a discrete copy of the real line times the usual line, and let \(\mu(f)=\sum_t\int f(t,s)\,ds\). For \(f\in K(\Gamma)\) the sum is finite, since a compact set meets only finitely many lines. The set \(Z=\mathbb R_d\times\{0\}\) meets each compact set in finitely many points, so it is locally null. But any open \(U\supseteq Z\) contains a segment \(\{t\}\times(-\delta_t,\delta_t)\) for each of uncountably many \(t\). So the outer-regular Borel measure of the Riesz representation theorem gives \(Z\) infinite measure. This is why the integral of Definition 2.2 is taken over compact sets and ignores locally null sets: \(\int1_Z\,d\mu=0\). A decomposition as in Lemma 2.1 is obtained by copying onto each line \(\{t\}\times\mathbb R\) one for Lebesgue measure, for instance the closures of the open intervals removed in building the Cantor set inside each \([k,k+1]\). (The segments \(\{t\}\times[k,k+1]\) do not qualify: neighbouring segments share an endpoint.) And \(L^p(\Gamma,\mu)\) is the \(\ell^p\)-sum of copies of \(L^p(\mathbb R)\), one for each \(t\).


## References



- [Pettis 1938] B. J. Pettis, On integration in vector spaces, *Transactions of the American Mathematical Society* 44 (1938), 277–304. https://doi.org/10.1090/S0002-9947-1938-1501970-8. Free at https://www.ams.org/journals/tran/1938-044-02/S0002-9947-1938-1501970-8/S0002-9947-1938-1501970-8.pdf
- [van Neerven] J. van Neerven, *Functional Analysis*, Cambridge Studies in Advanced Mathematics 201, Cambridge University Press,
  Cambridge, 2022; arXiv:2112.11166, version 7 (17 July 2025). Free at https://arxiv.org/abs/2112.11166
