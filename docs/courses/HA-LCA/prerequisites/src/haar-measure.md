# Haar measure on arbitrary locally compact abelian groups

**Programme reading HA-LCA-PRE-HAAR.** We construct Haar measure, including its measurable domain, before using its analytic consequences. The group \(G\) is Hausdorff, locally compact and abelian, written additively. No separability, metrizability or sigma-compactness of \(G\) is assumed.

The source material is Terence Tao's freely accessible [254A, Notes 3, §1](https://terrytao.wordpress.com/2011/09/27/254a-notes-3-haar-measure-and-the-peter-weyl-theorem/), dated 27 September 2011, for the normalized covering-functional construction and the open sigma-compact subgroup reduction; and D. H. Fremlin's [§441](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt441.tex), version of 3 January 2006, copyright 1997, for the unrestricted invariant-measure setting. We supply the representation and extension arguments below instead of importing either source's earlier theorems.

Original text: public domain (CC0). Fremlin's original notices and source are retained in the volume 4 source package. The proofs below use mathematical ideas from the cited free notes with new exposition; the notes themselves are not republished here.

Our earlier proofs are in [finite Radon representation](finite-radon-representation.md), [Banach spectra and compact products](banach-spectrum.md), [finite Radon products](finite-radon-products.md), and [integration and \(L^1\)](integration-and-l1.md). Each invocation below identifies the result needed.

## 1. Compact control of translations

Put \(L_af(x)=f(x-a)\).

<a id="ha-lca-pre-haar-lemma-1-1"></a>
### Lemma 1.1. Small neighbourhoods, open subgroups and uniform continuity

There is an open and closed sigma-compact subgroup \(H\subseteq G\). It has compact sets \(K_n\) with
\[
 K_n\subseteq\operatorname{int}_H K_{n+1},\qquad
 H=\bigcup_nK_n.
\]
Every compact subset of \(G\) meets only finitely many cosets of \(H\).

For \(f\in C_c(G)\),
\[
 \sup_x|f(x+a)-f(x)|\longrightarrow0\quad(a\to0).
\]
The supports of these differences, for \(a\) in a sufficiently small fixed neighbourhood of zero, all lie in one compact set.

**Proof.** Translations are homeomorphisms, with inverse translation by the negative element. Inversion is also a homeomorphism. Continuity of subtraction at \((0,0)\) shows that for each neighbourhood \(U\) of zero there is a symmetric open neighbourhood \(V\) with \(V+V\subseteq U\): intersect sufficiently small neighbourhoods in the two coordinates and their negatives. By the compact-neighbourhood shrinking proved in the finite-Radon reading, Lemma 1.3, such a \(V\) may be chosen with compact closure.

Fix symmetric open \(V\ni0\) with compact closure \(K\). Then
\[
 H=\bigcup_{n\ge1}nV=\bigcup_{n\ge1}nK.
\]
For the second equality, \(K\subseteq V+V\): if \(x\in\overline V\), the neighbourhood \(x+V\) meets \(V\), giving \(x\in V-V=V+V\). Thus each \(nK\subseteq2nV\). Finite products of compact spaces and continuous images are compact, as proved in the earlier readings, so \(nK\) is compact. The set \(H\) is a subgroup because \(V=-V\) and the sum of two finite sums is another finite sum. It is open, and its other cosets are open; their union is its complement, making \(H\) closed. With \(K_n=nK\), every point of \(K_n\) has its translate of \(V\) inside \(K_{n+1}\), so \(K_n\subseteq\operatorname{int}K_{n+1}\). The open cosets form a disjoint cover of \(G\); compactness of a set gives a finite subcover and hence the finite-coset assertion.

For uniform continuity let \(C=\operatorname{supp}f\), and fix a relatively compact neighbourhood \(W\) of zero. If \(a\in W\) and \(f(x+a)-f(x)\ne0\), then
\[
 x\in C\cup(C-\overline W)=:D,
\]
a compact set. The continuous function \((a,x)\mapsto f(x+a)-f(x)\) vanishes for \(a=0\). The compact-parameter uniformity proved in the finite-Radon reading, Lemma 1.6, makes its supremum on \(D\) tend to zero. Outside \(D\) it is already zero. This proves both assertions without a sequential assumption on \(G\). \(\square\)

## 2. An invariant positive functional

Write \(C_c(G)^+\) for the nonnegative real members of \(C_c(G)\), including zero. Fix \(b\in C_c(G)^+\setminus\{0\}\), whose existence follows from the compact cutoff lemma. For \(g\in C_c(G)^+\setminus\{0\}\), define
\[
 (f:g)=\inf\left\{\sum_{j=1}^m c_j:
       f\le\sum_{j=1}^m c_jL_{a_j}g,\quad c_j\ge0,\ a_j\in G\right\},
 \qquad (0:g)=0.
\]

<a id="ha-lca-pre-haar-lemma-2-1"></a>
### Lemma 2.1. Covering costs and approximate additivity

For \(f,g\ne0\), \(0<(f:g)<\infty\). Covering costs are monotone and positively homogeneous in \(f\), translation invariant in \(f\), and subadditive in \(f\). For nonzero \(g,h\),
\[
 (f:g)\le(f:h)(h:g).
\]
Consequently
\[
 A_g(f)=\frac{(f:g)}{(b:g)}
 \quad\hbox{satisfies}\quad
 0\le A_g(f)\le(f:b),\qquad A_g(b)=1.                 \tag{2.1}
\]
For any fixed \(f_1,f_2\in C_c(G)^+\) and \(\varepsilon>0\), there is a neighbourhood \(U\) of zero such that
\[
 0\le A_g(f_1)+A_g(f_2)-A_g(f_1+f_2)<\varepsilon       \tag{2.2}
\]
whenever \(g\ne0\) is supported in \(U\).

**Proof.** Some open set has \(g>c>0\). Translates of this set cover \(\operatorname{supp}f\); finitely many suffice. Giving each of the corresponding translates of \(g\) coefficient \(\|f\|_\infty/c\) covers \(f\). Conversely, evaluating any cover at a point \(x\) with \(f(x)>0\) gives \(\sum_jc_j\ge f(x)/\|g\|_\infty>0\).

Order and homogeneity follow directly by inclusion or scaling of covers. Translating a cover and then using the inverse translation proves invariance. Combining two covers and taking their infima proves subadditivity. For the multiplicative inequality, replace each translate of \(h\) in a cover of \(f\) by the corresponding translate of a cover of \(h\) by \(g\). The total cost is the product of the two costs. Approximate their finite infima and let both errors tend to zero. This proves the inequality, and (2.1) follows by taking \(h=b\).

For (2.2), put \(f=f_1+f_2\). If \(f=0\), there is nothing to prove. Choose \(v\in C_c(G)^+\) equal to one on \(\operatorname{supp}f\), with \(0\le v\le1\). Fix \(\delta>0\), to be decreased below, and define
\[
 r_i(x)=\frac{f_i(x)}{f(x)+\delta}\quad(i=1,2).
\]
These are in \(C_c(G)^+\), satisfy \(r_i\le v\) and \(r_1+r_2\le1\), and obey \(f_i=r_if+\delta r_i\). Given \(\eta>0\), Lemma 1.1 supplies a neighbourhood \(U\) with
\[
 |r_i(a+u)-r_i(a)|<\eta
 \quad(a\in G,\ u\in U,\ i=1,2).
\]
If \(g\) is supported in \(U\) and \(f\le\sum_jc_jL_{a_j}g\), multiplying by \(r_i\) gives
\[
 f_i\le\sum_j c_j\bigl(r_i(a_j)+\eta\bigr)L_{a_j}g+\delta r_i.
\]
By monotonicity and subadditivity of the covering cost,
\[
 A_g(f_1)+A_g(f_2)
 \le (1+2\eta)\frac{\sum_jc_j}{(b:g)}
       +\delta\bigl(A_g(r_1)+A_g(r_2)\bigr).
\]
Take the infimum over the covers of \(f\), and use (2.1) and \(r_i\le v\). The excess over \(A_g(f)\) is at most
\[
 2\eta(f:b)+2\delta(v:b).
\]
First choose \(\delta>0\) and then \(\eta>0\) so this is less than \(\varepsilon\). The resulting \(U\) works for all such \(g\). The lower bound in (2.2) is subadditivity. \(\square\)

<a id="ha-lca-pre-haar-theorem-2-2"></a>
### Theorem 2.2. Existence of a normalized invariant integral

There is a positive real linear functional \(I:C_c(G;\mathbb R)\to\mathbb R\) with
\[
 I(b)=1,\qquad I(L_af)=I(f)\quad(a\in G).
\]
It extends complex-linearly to \(C_c(G)\). For each compact \(K\), there is a finite constant \(M_K\) such that
\[
 |I(f)|\le M_K\|f\|_\infty
 \quad\hbox{if }\operatorname{supp}f\subseteq K.
\]

**Proof.** For each \(f\in C_c(G)^+\), the interval \([0,(f:b)]\) is compact; for \(f=0\) it is the singleton \(\{0\}\). The arbitrary-product compactness proved in the Banach reading, Lemma 4.1, makes
\[
 P=\prod_{f\in C_c(G)^+}[0,(f:b)]
\]
compact. Each \(A_g\) is a point of \(P\). For a neighbourhood \(U\) of zero, let \(F_U\) be the closure in \(P\) of the points \(A_g\) with \(g\ne0\) supported in \(U\). Cutoffs make this set nonempty. Finite intersections of neighbourhoods show that the closed sets \(F_U\) have the finite intersection property. Their intersection is nonempty: otherwise their open complements would cover compact \(P\) and a finite subcover would contradict that property.

Choose \(A\in\bigcap_UF_U\). The normalization, homogeneity and translation-invariance equalities for \(A_g\) are closed conditions on finitely many coordinates, so hold for \(A\). For each \(f_1,f_2\), (2.2) gives arbitrarily small closed bounds on its additivity defect throughout an appropriate \(F_U\). Therefore \(A(f_1+f_2)=A(f_1)+A(f_2)\).

For real \(f\), define \(I(f)=A(f^+)-A(f^-)\). This is independent of a decomposition \(f=p-q\) with \(p,q\ge0\): another such decomposition gives \(p+q'=p'+q\), and additivity of \(A\) equates their values. This proves real linearity, positivity and translation invariance. Extend by \(I(f)=I(\Re f)+iI(\Im f)\); the identities for multiplication by \(i\) give complex linearity.

Choose a cutoff \(v\ge0\) equal to one on \(K\). For real \(f\) supported in \(K\), order gives \(|I(f)|\le\|f\|_\infty I(v)\). For complex \(f\), rotate \(I(f)\) by a scalar of modulus one so its real part is \(|I(f)|\). Positivity applied to that real part gives the same bound. Thus \(M_K=I(v)\) works. \(\square\)

## 3. Representing the integral on a sigma-compact space

<a id="ha-lca-pre-haar-theorem-3-1"></a>
### Theorem 3.1. Positive \(C_c\) representation on a sigma-compact space

Let \(X\) be sigma-compact, locally compact and Hausdorff, and let \(I\) be a positive real linear functional on \(C_c(X;\mathbb R)\). There is a unique Borel measure \(\mu\), finite on compact sets, inner regular on all Borel sets and outer regular on all Borel sets, such that
\[
 I(f)=\int_X f\,d\mu\quad(f\in C_c(X;\mathbb R)).
\]
It is sigma-finite. Complexification gives the same identity for complex \(f\).

**Proof.** First obtain a compact exhaustion \(K_n\subseteq\operatorname{int}K_{n+1}\). Starting with a countable compact cover \(C_n\), use finitely many relatively compact open neighbourhoods to cover \(C_1\); their compact closures have compact union \(K_1\). Inductively cover \(K_n\cup C_{n+1}\) by finitely many relatively compact open neighbourhoods and take their compact closures as \(K_{n+1}\). This proves the required properties.

Choose \(u_n\in C_c(X)\), \(0\le u_n\le1\), equal to one on \(K_n\), with support in \(\operatorname{int}K_{n+1}\). Set
\[
 a_n=\frac{2^{-n}}{1+I(u_n)},\qquad
 w=\sum_{n\ge1}a_nu_n.
\]
The series converges uniformly, because \(a_n\le2^{-n}\). The finite-Radon reading, Lemma 1.5, proves that its limit belongs to \(C_0(X)\). At each point some \(u_n=1\), so \(w>0\) everywhere.

Define \(J(f)=I(wf)\) for real \(f\in C_c(X)\). Although \(w\) need not be compactly supported, \(wf\) is. On functions supported in a fixed compact set \(K\), positivity bounds \(I\) by \(I(v)\|\cdot\|_\infty\), where \(v\) is a cutoff equal to one on \(K\). Thus uniform convergence of the partial sums of \(wf\) permits
\[
 |J(f)|\le\sum_n a_n|I(u_nf)|
          \le\|f\|_\infty\sum_na_nI(u_n)\le\|f\|_\infty.
\]
The real functional \(J\) extends uniquely and positively to \(C_0(X;\mathbb R)\): \(C_c\) is uniformly dense by the finite-Radon reading, Lemma 1.5, and nonnegative approximants preserve positivity. Its positive representation theorem, Theorem 3.1, gives a finite positive Radon measure \(\rho\) with \(J(f)=\int f\,d\rho\).

Use the nonnegative integral already constructed in the integration reading to define
\[
 \mu(E)=\int_E w^{-1}\,d\rho\qquad(E\text{ Borel}).
\]
The positive series rule proves countable additivity. On every compact \(K\), \(w\) has a positive lower bound: finitely many neighbourhoods on which \(w>w(x)/2\) cover \(K\). Hence \(\mu K<\infty\). Weighted integration gives
\[
 \int h\,d\mu=\int h/w\,d\rho\quad(h\ge0\text{ Borel}),
\]
first for indicators, then simple functions, then increasing limits. The four-part complex definition gives the same identity for integrable functions. If \(f\in C_c(X)\), then \(f/w\in C_c(X)\), and
\[
 \int f\,d\mu=\int f/w\,d\rho=J(f/w)=I(f).
\]

For inner regularity, put \(E_n=\{w\ge1/n\}\). Each \(E_n\) is compact and they increase to \(X\). The finite measure \(\mu_n(B)=\mu(B\cap E_n)\) is bounded above by \(n\rho\), hence Radon by Lemma 1.2 of the finite-product reading. Monotone convergence gives \(\mu(B)=\lim_n\mu_n(B)\). A compact subset \(C\subseteq B\) approximating \(\mu_n(B)\) satisfies \(\mu(C)\ge\mu_n(C)\). Taking suprema proves inner regularity of \(\mu\) on every Borel \(B\), including sets of infinite measure.

For outer regularity, fix Borel \(B\) and \(\varepsilon>0\). The finite restriction \(\mu_{K_{n+1}}\) is Radon by compact localization in the finite-product reading, Corollary 2.3. Choose open \(W_n\supseteq B\cap K_n\) such that
\[
 \mu_{K_{n+1}}\bigl(W_n\setminus(B\cap K_n)\bigr)
       <\varepsilon 2^{-n}.
\]
Then \(V_n=W_n\cap\operatorname{int}K_{n+1}\) contains \(B\cap K_n\) and \(\mu(V_n\setminus B)<\varepsilon2^{-n}\). The open union \(V=\bigcup_nV_n\) contains \(B\), with \(\mu(V\setminus B)<\varepsilon\). This proves outer regularity at finite-measure \(B\); at infinite-measure \(B\), every superset already has infinite measure. The compact exhaustion and local finiteness give sigma-finiteness.

Finally every such representing measure has, for open \(U\),
\[
 \mu(U)=\sup\{I(f):f\in C_c(X),\ 0\le f\le1,\
                                      \operatorname{supp}f\subseteq U\}.
\]
The upper bound is integration; compact inner approximation and cutoffs give the lower bound. Outer regularity then determines \(\mu\) on every Borel set, proving uniqueness. \(\square\)

## 4. Existence, uniqueness and inversion on the open subgroup

<a id="ha-lca-pre-haar-theorem-4-1"></a>
### Theorem 4.1. Sigma-compact abelian Haar measure

A sigma-compact locally compact Hausdorff abelian group \(H\) has a nonzero translation-invariant Borel measure \(\mu_H\) that is finite on compact sets and inner and outer regular. Every nonempty open set has positive measure. Any two such nonzero invariant measures are positive scalar multiples. Inversion preserves each such measure. All these assertions extend to its ordinary completion.

**Proof.** Apply Theorem 2.2 on \(H\), then Theorem 3.1. For \(a\in H\), the measure \(E\mapsto\mu_H(E+a)\) is again locally finite and inner and outer regular, because translation is a homeomorphism. The change-of-variables formula for this image follows first on indicators and then by simple approximation, as in the integration reading, Lemma 2.5. Invariance of \(I\) makes this measure represent the same functional; Theorem 3.1 gives equality. Nontriviality follows from \(\int b\,d\mu_H=1\).

For any nonzero such measure \(\mu\), inner regularity supplies compact \(K\) with \(\mu K>0\). If \(U\) is nonempty open, its translates cover \(K\), and a finite subcover and translation invariance give \(\mu K\le m\mu U\). Thus \(\mu U>0\). A nonnegative nonzero member of \(C_c(H)\) is bounded below by a positive constant on some nonempty open set, so its integral is strictly positive.

We prove inversion and uniqueness without assuming either in a change of variables. For two such measures \(\mu,\nu\), and \(f,g\in C_c(H)\), apply compactly supported Fubini from the finite-product reading, Corollary 2.3, to \(f(x+y)g(y)\). This kernel has compact support: \(y\) belongs to \(\operatorname{supp}g\) and \(x\) to \(\operatorname{supp}f-\operatorname{supp}g\). Integrating first in \(x\) gives
\[
 \iint f(x+y)g(y)\,d\mu(x)\,d\nu(y)=I_\mu(f)I_\nu(g).
\]
In the other order, for fixed \(x\) substitute \(z=x+y\), which uses only translation invariance of \(\nu\). The kernel \(f(z)g(z-x)\) also has compact support. Interchange its two integrals, and in its \(x\)-integral translate \(x\) by \(z\). The result is
\[
 I_\mu(f)I_\nu(g)=I_\nu(f)I_\mu(g^-),
 \qquad g^-(x)=g(-x).                                  \tag{4.1}
\]
Set \(\nu=\mu\), and take nonnegative nonzero \(f\). Its integral is positive, so (4.1) gives \(I_\mu(g)=I_\mu(g^-)\) for all \(g\in C_c(H)\). The inverted measure \(E\mapsto\mu(-E)\) has the same regularity and the same \(C_c\) integrals. Theorem 3.1 gives \(\mu(-E)=\mu(E)\).

Now (4.1) becomes \(I_\mu(f)I_\nu(g)=I_\nu(f)I_\mu(g)\). Fix nonnegative nonzero \(g\); both integrals are positive. Hence \(I_\nu=cI_\mu\), where \(c=I_\nu(g)/I_\mu(g)>0\), and Theorem 3.1 proves \(\nu=c\mu\).

Ordinary completion is constructed in the integration reading, Lemma 1.1. Translation and inversion preserve Borel null sets, so preserve their subsets, the completed domain and the completed measure. Completed sets retain inner regularity: remove a Borel null envelope from a Borel representative, and approximate the remaining Borel set by compact subsets. They retain outer regularity by adding that null envelope and using Borel outer regularity. \(\square\)

## 5. The measure and its domain on the whole group

Fix an open sigma-compact subgroup \(H\) from Lemma 1.1 and a Haar measure \(\mu_H\) from Theorem 4.1. Choose one representative \(r\) for each coset in \(G/H\), and denote the set of representatives by \(R\). For \(E\subseteq G\), write \(E_r=(E-r)\cap H\). Let
\[
 \Sigma_G=\{E\subseteq G:E_r
               \text{ is measurable for the ordinary completion of }\mu_H
               \text{ for every }r\in R\},
 \qquad
 \mu(E)=\sum_{r\in R}\mu_H(E_r).                        \tag{5.1}
\]
For a family of nonnegative numbers, the sum over an arbitrary index set is the supremum of its sums over finite subsets.

<a id="ha-lca-pre-haar-theorem-5-1"></a>
### Theorem 5.1. Arbitrary-group Haar measure

Formula (5.1) defines a complete, translation- and inversion-invariant measure on \(\Sigma_G\). Its domain contains every Borel subset of \(G\); it is finite on compact sets and inner regular on every measurable set. Every nonempty open set has positive measure.

The measure is locally determined: if a set has measurable intersection with every measurable set of finite measure, then it belongs to \(\Sigma_G\). In fact, measurable intersections with every compact set already suffice for membership in \(\Sigma_G\). If a measurable set has null intersection with every compact set, it is null. We do not require global outer regularity on arbitrary \(G\).

Among nonzero translation-invariant Borel measures finite on compact sets and inner regular on all Borel sets, this measure is unique up to a positive scalar. Its domain (5.1) is equivalently the complete locally determined extension of its Borel restriction.

**Proof.** Each coset is open and closed and is homeomorphic to \(H\), so Borel sets have Borel sections \(E_r\). The section definition makes \(\Sigma_G\) a sigma-algebra. Countable additivity of (5.1) follows by interchanging the sum over \(R\) with a nonnegative countable sum. To verify the interchange, both orders equal the supremum of sums over finite subsets of \(R\times\mathbb N\); finite subsets lie in finite rectangles, and increasing partial sums exhaust the countable coordinate. A set is null exactly when every section is null, so completeness follows from completeness on \(H\).

Changing a representative within its coset translates the section by an element of \(H\), and does not change measurability or measure. Translation by any \(a\in G\) permutes the cosets; its map on each section is a translation within \(H\). Thus it preserves \(\Sigma_G\) and (5.1). Inversion also permutes the cosets and on each section is inversion followed by a translation in \(H\). Theorem 4.1 proves its invariance.

A compact set meets only finitely many cosets by Lemma 1.1, and has a compact section in each. It therefore has finite measure. For a measurable \(E\), the supremum of finite sums in (5.1), followed by compact inner approximation in each of the finitely many selected sections, proves
\[
 \mu(E)=\sup\{\mu K:K\subseteq E,\ K\text{ compact}\}.
\]
This argument also applies when \(\mu E=\infty\): to exceed any prescribed finite bound, first choose an appropriate finite sum and then compact approximations. A nonempty open set meets some coset in a nonempty open set, which has positive \(\mu_H\)-measure.

Let now \(E\subseteq G\) have measurable intersections with all finite-measure measurable sets, or just with all compact sets. In each coset, use the translated compact exhaustion \(r+K_n\) of \(H\). Every \(E\cap(r+K_n)\) is measurable by hypothesis; the union over \(n\) proves that \(E_r\) is completed-measurable in \(H\). Hence \(E\in\Sigma_G\). The null assertion follows either by the same countable exhaustion on each coset or directly from inner regularity.

For uniqueness let \(\nu\) be another nonzero invariant Borel measure with the stated compact finiteness and full inner regularity. A compact set of positive \(\nu\)-measure exists. Its finite covering by translates of any nonempty open set proves that every such open set has positive \(\nu\)-measure. In particular, \(\nu|_H\ne0\). Its restriction to \(H\) is sigma-finite and inner regular. It is also outer regular: the compact-exhaustion argument in the proof of Theorem 3.1 uses only local finiteness and inner regularity, and therefore applies to this restriction. Theorem 4.1 gives \(\nu|_H=c\mu_H\). Translation invariance and the finite-coset property give \(\nu K=c\mu K\) for every compact \(K\subseteq G\). Full inner regularity now gives equality on every Borel set.

For the domain assertion, start with the ordinary completion of the Borel measure, and declare \(E\) locally measurable when its intersection with each completed measurable finite-measure set is completed measurable. Such an \(E\) has completed-measurable sections by the compact exhaustions, so belongs to (5.1). In the other direction, if \(E\in\Sigma_G\) and \(F\) is Borel of finite measure, only countably many sections of \(F\) have positive measure: for each positive integer \(m\), only finitely many can have measure at least \(1/m\). On their union \(E\cap F\) has a Borel representative modulo a null set, since the union has countably many sigma-compact cosets.

The residual part of \(F\) is Borel and null: remove that countable union of open-and-closed cosets from \(F\). Any subset of it is in the ordinary completion. The null exceptions within the countably many selected cosets have a Borel null envelope by ordinary completion in each coset. Thus \(E\cap F\) is in the ordinary completion on \(G\). Replacing a completed finite-measure \(F\) by a Borel representative and a Borel null envelope gives the same conclusion. This proves the claimed equivalence of domains. \(\square\)

<a id="ha-lca-pre-haar-lemma-5-2"></a>
### Lemma 5.2. \(L^1\) functions on the completed locally determined domain

Every \(L^1(\mu)\) class for (5.1) has an everywhere finite Borel representative zero outside a sigma-compact subset of \(G\). The integration reading's \(C_c\)-density theorem therefore applies to this \(L^1\), and \(L^1(\mu)\) is complete.

**Proof.** For an integrable measurable \(f\), the level sets
\(E_m=\{|f|\ge1/m\}\) have finite measure by the integration reading, Lemma 2.3. Inner regularity in Theorem 5.1 supplies compact \(C_{m,k}\subseteq E_m\) with
\(\mu(E_m\setminus C_{m,k})<1/k\). Their countable union \(S\) contains the nonzero set of \(f\) up to a null set.

Every compact \(C_{m,k}\) meets finitely many cosets. Thus \(S\) lies in a countable union \(T\) of cosets, and \(T\) is open, closed and sigma-compact. The countable disjoint union of the completed measures on these cosets is the ordinary completion of their Borel sum: choose a Borel representative and a Borel null envelope on each coset and take their countable unions. Lemma 1.1 of the integration reading consequently supplies an everywhere finite Borel representative of \(f1_S\) on \(T\). Multiplying it by \(1_S\) and extending by zero off \(T\) gives the required global Borel representative, still zero off \(S\).

The Borel restriction of \(\mu\) is finite on compact sets and inner regular on finite-measure Borel sets by Theorem 5.1. Theorem 3.1 of the integration reading now approximates this representative by \(C_c(G)\) in \(L^1\). Completeness for the full domain follows directly from that reading's Theorem 2.4, which applies to every measure space. \(\square\)

## 6. Translation and the \(L^1\) algebra

The free-source comparisons for this section are Fremlin, [§443, 14 January 2013](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt443.tex), 443G, and [§444, 23 July 2007 / 4 June 2013](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt444.tex), 444O and 444R. The earlier proofs of integration and product measures give the required complex and arbitrary-LCA versions below.

<a id="ha-lca-pre-haar-lemma-6-1"></a>
### Lemma 6.1. Continuity of translations in \(L^1\)

Each \(L_a\) is an isometry of \(L^1(\mu)\), and
\[
 \|L_af-f\|_1\longrightarrow0\quad(a\to0).
\]
The map \((a,f)\mapsto L_af\) is jointly continuous from \(G\times L^1(\mu)\) to \(L^1(\mu)\).

**Proof.** Theorem 5.1 and the integration reading's change-of-variables Lemma 2.5 give the isometry, including well-definedness on almost-everywhere classes. For \(f\in C_c(G)\), Lemma 1.1 puts all sufficiently small translation differences in a fixed compact set \(D\), with their uniform norms tending to zero. Thus
\(\|L_af-f\|_1\le\mu(D)\|L_af-f\|_\infty\to0\).
For general \(f\), choose \(h\in C_c(G)\) with \(\|f-h\|_1<\varepsilon\), using Lemma 5.2. Then
\[
 \|L_af-f\|_1\le2\varepsilon+\|L_ah-h\|_1.
\]
This proves continuity at zero. The group law and the isometry give continuity at any \(a_0\). Finally
\[
 \|L_af-L_{a_0}f_0\|_1
 \le\|f-f_0\|_1+\|L_{a-a_0}f_0-f_0\|_1,
\]
which proves joint continuity. \(\square\)

<a id="ha-lca-pre-haar-theorem-6-2"></a>
### Theorem 6.2. The commutative Banach star algebra \(L^1(G)\)

For \(f,g\in L^1(\mu)\), the integral
\[
 (f*g)(x)=\int_G f(y)g(x-y)\,d\mu(y)                    \tag{6.1}
\]
exists absolutely for almost every \(x\). It defines a class in \(L^1(\mu)\), independent of representatives, with
\[
 \|f*g\|_1\le\|f\|_1\|g\|_1.
\]
Together with \(f^*(x)=\overline{f(-x)}\), convolution makes \(L^1(\mu)\) a commutative Banach star algebra:
\[
 (f*g)*h=f*(g*h),\quad
 (f*g)^*=g^**f^*,\quad
 \|f^*\|_1=\|f\|_1,\quad f^{**}=f.
\]
For \(f,g\in C_c(G)\), their convolution is in \(C_c(G)\) and
\(\operatorname{supp}(f*g)\subseteq\operatorname{supp}f+\operatorname{supp}g\).
Furthermore
\[
 L_a(f*g)=(L_af)*g=f*(L_ag).                            \tag{6.2}
\]

**Proof.** First let \(f,g\in C_c(G)\). Each section in (6.1) is integrable. Lemma 1.1 gives
\[
 |(f*g)(x+a)-(f*g)(x)|
 \le\|f\|_1\sup_z|g(z+a)-g(z)|\longrightarrow0.
\]
The support inclusion follows because the integrand is zero unless \(y\in\operatorname{supp}f\) and \(x-y\in\operatorname{supp}g\); their sum is compact and closed. The nonnegative continuous kernel \(|f(y)g(x-y)|\) has compact support in \(G\times G\). Compactly supported Fubini and translation invariance give
\[
 \|f*g\|_1
 \le\int_G|f(y)|\left(\int_G|g(x-y)|\,d\mu(x)\right)d\mu(y)
 =\|f\|_1\|g\|_1.                                      \tag{6.3}
\]
Substitution \(y\mapsto x-y\), using both translation and inversion invariance, gives commutativity.

For \(f,g,h\in C_c(G)\) and fixed \(x\), expand \(((f*g)*h)(x)\), interchange its two integrals, and substitute \(z=t-y\) in the integral originally indexed by \(t\). The result is
\[
 \iint f(y)g(z)h(x-y-z)\,d\mu(z)\,d\mu(y)
   =\bigl(f*(g*h)\bigr)(x).
\]
Every interchange is justified by compactly supported continuous Fubini: before substitution the variables lie in the compact sets supplied by \(\operatorname{supp}f\), \(\operatorname{supp}g\) and their sum; afterwards they lie in their compact product. Conjugating (6.1) at \(-x\) and substituting \(y=-z\) gives \((f*g)^*=f^**g^*\); commutativity puts the factors in the displayed reversed order. The same substitutions prove (6.2). Inversion invariance proves \(\|f^*\|_1=\|f\|_1\); applying the formula twice proves \(f^{**}=f\).

For general \(f,g\in L^1\), choose \(f_n,g_n\in C_c(G)\) converging in \(L^1\), by Lemma 5.2. The estimate
\[
 \|f_n*g_n-f_m*g_m\|_1
 \le\|f_n-f_m\|_1\|g_n\|_1+\|f_m\|_1\|g_n-g_m\|_1
\]
shows that the products form a Cauchy sequence. Completeness of \(L^1\) gives a limit independent of the approximants, by the same estimate comparing two choices. This extends convolution bilinearly with (6.3). The isometric involution also passes to the limit. Associativity, commutativity, the star identity and (6.2) pass to the limit in these bounded operations. For associativity, for example, the error in replacing an input of a triple product is bounded by its \(L^1\) error times the two other norms; convergent approximating sequences have bounded norms.

It remains to verify the integral formula (6.1) for these limits without a global sigma-finiteness assumption. By Lemma 5.2 choose finite Borel representatives supported on sigma-compact sets \(S_f,S_g\). The set \(T=S_f+S_g\) is sigma-compact: write it as a countable union of compact sums. The restrictions of the Borel measure to \(T\) and \(S_f\), regarded as measures on \(G\) that vanish outside those sets, are sigma-finite, finite on compact sets and inner regular on finite-measure Borel sets. For the last assertion, a finite-measure set under the restriction is the intersection with its restricting set, and inner regularity of \(\mu\) supplies compact subsets of that intersection.

The kernel \(f(y)g(x-y)\) is Borel and zero off \(T\times S_f\). Theorem 4.4 of the integration reading applies to these two restricted measures. For \(y\in S_f\), the function \(x\mapsto g(x-y)\) is supported in \(y+S_g\subseteq T\), and its unrestricted integral norm equals \(\|g\|_1\). Thus the absolute double integral is
\[
 \int_{S_f}|f(y)|\int_T|g(x-y)|\,d\mu(x)\,d\mu(y)
 =\|f\|_1\|g\|_1.
\]
Fubini supplies a Borel section integral on \(T\) outside a null set, and it is zero off \(T\). Defining it to be zero on the exceptional set makes an \(L^1\) representative satisfying (6.3). The same bound applied to differences proves that this bilinear integral construction is continuous in both \(L^1\) inputs. It agrees with the already defined convolution on \(C_c(G)\), hence on all of \(L^1\) by density.

Finally take any other finite measurable representatives \(f',g'\) of the two classes. There are measurable null sets \(N_f,N_g\) outside which they agree with the Borel representatives. For fixed \(x\), the two integrands agree except on
\(N_f\cup(x-N_g)\), a measurable null set by Theorem 5.1. Both sections are measurable because translation and inversion preserve the full measurable domain. Their absolute integrability and integrals therefore agree for that \(x\). This proves representative independence for (6.1), as well as its almost-everywhere existence on the full domain. \(\square\)

<a id="ha-lca-pre-haar-corollary-6-3"></a>
### Corollary 6.3. A symmetric approximate identity of norm one

For every open neighbourhood \(U\) of zero there is \(e_U\in C_c(G)\) with
\[
 e_U\ge0,\quad e_U^*=e_U,\quad
 \operatorname{supp}e_U\subseteq U,\quad
 \int e_U\,d\mu=\|e_U\|_1=1.
\]
With neighbourhoods directed by reverse inclusion, these functions satisfy
\[
 e_U*f\longrightarrow f\quad\hbox{in }L^1(G)
 \qquad(f\in L^1(G)).
\]
For \(h\in C_0(G)\), the convolution \(e_U*h\) belongs to \(C_0(G)\) and converges uniformly to \(h\).

**Proof.** Choose \(v\in C_c(G)\), \(0\le v\le1\), with \(v(0)=1\) and support in \(U\cap(-U)\). Put \(w(x)=v(x)+v(-x)\). This is symmetric, nonnegative and supported in \(U\); its integral is finite and positive by compact finiteness and positivity on nonempty open sets. Define \(e_U=w/\int w\). Inversion invariance proves every displayed property.

For \(f\in L^1\), use a Borel representative supported on a sigma-compact set \(S\). Put \(K=\operatorname{supp}e_U\), which contains zero, and \(T=S+K\), which is sigma-compact and contains \(S\). Apply positive Fubini, Theorem 4.4 of the integration reading, to the restrictions of \(\mu\) to \(T\) and \(K\), and to the Borel kernel
\(e_U(y)|f(x-y)-f(x)|\). It vanishes off \(T\times K\). The resulting estimate is
\[
 \begin{split}
 \|e_U*f-f\|_1
 &\le\int_K e_U(y)\,\|L_yf-f\|_1\,d\mu(y)\\
 &\le\sup_{y\in U}\|L_yf-f\|_1.
 \end{split}
\]
The first line also proves that the required iterated integrals are finite, since \(\|L_yf-f\|_1\le2\|f\|_1\). Lemma 6.1 makes the last supremum tend to zero as \(U\) shrinks. This is a neighbourhood net, with no countable neighbourhood basis assumed.

For \(h\in C_0(G)\), the pointwise integral defining \(e_U*h\) exists and has norm at most \(\|h\|_\infty\). Approximate \(h\) uniformly by \(h_n\in C_c(G)\), using the finite-Radon reading, Lemma 1.5. Theorem 6.2 gives \(e_U*h_n\in C_c(G)\), and
\[
 \|e_U*h_n-e_U*h\|_\infty\le\|h_n-h\|_\infty.
\]
Since \(C_0(G)\) is uniformly closed by that same earlier lemma, \(e_U*h\in C_0(G)\). Uniform approximation and Lemma 1.1 also show
\[
 \|L_yh-h\|_\infty
 \le2\|h-h_n\|_\infty+\|L_yh_n-h_n\|_\infty\longrightarrow0
 \quad(y\to0).
\]
Finally
\(\|e_U*h-h\|_\infty\le\sup_{y\in U}\|L_yh-h\|_\infty\),
which proves uniform convergence. \(\square\)
