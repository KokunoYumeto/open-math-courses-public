# General Haar integration and the modular \(L^1\) algebra

**Programme reading HA-LCA-PRE-NONABELIAN-HAAR.** Self-checked by the writing AI. This reading treats an arbitrary locally compact Hausdorff group \(G\), with multiplication written in its given order and identity \(e\). No abelianness, unimodularity, countability or separability hypothesis is imposed.

The freely accessible source material is Terence Tao's [2011 notes on Haar measure, §1](https://terrytao.wordpress.com/2011/09/27/254a-notes-3-haar-measure-and-the-peter-weyl-theorem/), especially Theorem 3 and Exercises 6–7; D. H. Fremlin's *Measure Theory*, [§442, version of 21 March 2007](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt442.tex), 442C–K, [§443, version of 14 January 2013](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt443.tex), 443G, and [§444, version of 4 June 2013](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt444.tex), 444O–Q; and B. Bekka, P. de la Harpe and A. Valette's [free author draft dated 23 February 2007](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf), A.3.2–A.3.4, A.4 and the integrated-representation statement on printed page 436 in F.4. Source exercises and external references are not proof providers. Every result used below is proved here or linked to its complete proof in an earlier programme reading.

Original text: public domain (CC0). Fremlin's original copyright notices for §§442, 443 and 444 are 1998, 2001 and 1999. The unchanged volume 4 source package is retained. The other sources' prose and figures are not reproduced.

## 1. Compact control in a group

Put \(L_af(x)=f(a^{-1}x)\) and \(R_af(x)=f(xa)\). Products of compact subsets are compact: multiplication is continuous and the finite product is compact by the earlier [compact-product lemma](finite-radon-representation.md#ha-lca-pre-radon-lemma-1-6). Inversion and translations are homeomorphisms, with their stated group-theoretic inverses.

<a id="ha-lca-pre-nonabelian-haar-lemma-1-1"></a>
### Lemma 1.1. Compact neighbourhoods, subgroups and uniform translations

The group has an open and closed sigma-compact subgroup \(H\) with a compact exhaustion \(K_n\subseteq\operatorname{int}K_{n+1}\). Every compact subset of \(G\) meets only finitely many left cosets of \(H\). Any specified countable union of compact subsets of \(G\) lies in some open sigma-compact subgroup.

For \(f\in C_c(G)\),
\[
 \|L_af-f\|_\infty\longrightarrow0,\qquad
 \|R_af-f\|_\infty\longrightarrow0\quad(a\to e).
 \tag{1}
\]
For \(a\) in a fixed sufficiently small neighbourhood of \(e\), all supports in these differences lie in one compact set. The uniform convergence in (1) also holds for \(f\in C_0(G)\).

**Proof.** Given a neighbourhood \(U\) of \(e\), continuity of multiplication gives neighbourhoods \(U_1,U_2\) with \(U_1U_2\subseteq U\). Intersect them and their inverses to get a symmetric open neighbourhood \(V\) with \(V^2\subseteq U\). It can also have compact closure, using the earlier [locally compact shrinking lemma](finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3) and another such intersection.

Fix a relatively compact symmetric open \(V\ni e\), and let \(K=\bar V\). If \(x\in K\), the open neighbourhood \(xV\) meets \(V\), so \(x\in VV^{-1}=V^2\). Thus
\[
 H=\bigcup_{n\ge1}V^n=\bigcup_{n\ge1}K^n.
\]
It is a subgroup because \(V=V^{-1}\), and is open. All its other left cosets are open, making its complement open and hence \(H\) closed. The compact sets \(K_n=K^n\) satisfy \(K_nV\subseteq K_{n+1}\); since \(K_nV\) is open and contains \(K_n\), this is the asserted exhaustion. The disjoint open left cosets cover \(G\), so a compact set has a finite subcover.

For compact sets \(C_1,C_2,\ldots\), set
\[
 A_n=K\cup\bigcup_{j\le n}(C_j\cup C_j^{-1}),\qquad
 J=\bigcup_{n\ge1}A_n^n.
\]
Each \(A_n\) is compact, symmetric and contains \(e\). The sets \(A_n^n\) increase. Inverses preserve each; a product of an element of \(A_n^n\) and one of \(A_m^m\) belongs to \(A_k^k\) for \(k\ge n+m\). Thus \(J\) is a subgroup containing all \(C_j\). It contains \(V\), and each translate \(xV\), \(x\in J\), stays in \(J\); hence it is open. It is sigma-compact by construction, and closed as above.

Let \(C=\operatorname{supp}f\), and choose a compact symmetric neighbourhood \(W\ni e\). For \(a\in W\), the support of \(L_af-f\) lies in \(WC\cup C\), while that of \(R_af-f\) lies in \(CW\cup C\). Both are compact. The functions \((a,x)\mapsto f(a^{-1}x)-f(x)\) and \((a,x)\mapsto f(xa)-f(x)\) are continuous and vanish at \(a=e\). The earlier [compact-parameter uniformity proof](finite-radon-representation.md#ha-lca-pre-radon-lemma-1-6) makes their suprema on these compact \(x\)-sets tend to zero. They vanish outside those sets, proving (1). Finally \(C_c(G)\) is uniformly dense in \(C_0(G)\) by the earlier [cutoff approximation](finite-radon-representation.md#ha-lca-pre-radon-lemma-1-5); left and right translation are isometries of the uniform norm, so a two-error triangle estimate extends (1) to \(C_0(G)\). \(\square\)

## 2. Constructing the left invariant integral

<a id="ha-lca-pre-nonabelian-haar-theorem-2-1"></a>
### Theorem 2.1. A positive left invariant functional

There is a nonzero positive linear functional \(I:C_c(G)\to\mathbb C\) satisfying \(I(L_af)=I(f)\). For each compact \(C\), there is \(M_C<\infty\) such that \(|I(f)|\le M_C\|f\|_\infty\) whenever \(\operatorname{supp}f\subseteq C\).

**Proof.** Fix \(0\ne b\in C_c(G)\), \(b\ge0\), using the compact cutoff lemma. For \(g\in C_c(G)\), \(g\ge0\), \(g\ne0\), and \(f\in C_c(G)\), \(f\ge0\), define
\[
 (f:g)=\inf\left\{\sum_{j=1}^m c_j:
       f\le\sum_{j=1}^m c_jL_{a_j}g,\ c_j\ge0,\ a_j\in G\right\},
 \qquad A_g(f)=\frac{(f:g)}{(b:g)}.                       \tag{2}
\]
For \(f\ne0\), \(0<(f:g)<\infty\). Indeed \(g\) is bounded below by some \(c>0\) on a nonempty open set, whose left translates cover the compact support of \(f\). A finite subcover, each with coefficient \(\|f\|_\infty/c\), gives a finite cost. At a point where \(f(x)>0\), any cover has total coefficient at least \(f(x)/\|g\|_\infty>0\). For \(f=0\) the cost is zero.

The cost is monotone and positively homogeneous in \(f\). Combining covers gives subadditivity. Applying \(L_a\) to a cover and then using \(L_{a^{-1}}\) proves invariance, since \(L_aL_c=L_{ac}\); no factors have been interchanged. Replacing each occurrence of a translate of \(h\) in a cover of \(f\) by its translated cover by \(g\) gives
\[
 (f:g)\le(f:h)(h:g).
\]
To justify the infima, choose covers with costs arbitrarily close to each of the two finite infima, multiply their costs, and let the two errors decrease to zero. Taking \(h=b\) yields \(0\le A_g(f)\le(f:b)\) and \(A_g(b)=1\).

We prove approximate additivity when \(g\) is supported near \(e\). Fix \(f_1,f_2\ge0\), put \(f=f_1+f_2\), and suppose \(f\ne0\). Choose \(v\in C_c(G)\), \(0\le v\le1\), equal to one on \(\operatorname{supp}f\). For \(\delta>0\) put
\[
 r_i(x)=\frac{f_i(x)}{f(x)+\delta}\quad(i=1,2).
\]
Then \(0\le r_i\le v\), \(r_1+r_2\le1\), and \(f_i=r_if+\delta r_i\). Given \(\eta>0\), Lemma 1.1 supplies a neighbourhood \(U\) with
\[
 |r_i(au)-r_i(a)|<\eta\qquad(a\in G,\ u\in U,\ i=1,2).
\]
If \(\operatorname{supp}g\subseteq U\) and \(f\le\sum_jc_jL_{a_j}g\), a nonzero summand at \(x\) has \(a_j^{-1}x\in U\), or \(x=a_ju\). Multiplying the cover by \(r_i\) therefore gives
\[
 f_i\le\sum_jc_j(r_i(a_j)+\eta)L_{a_j}g+\delta r_i.
\]
Apply monotonicity and subadditivity, add the two inequalities, and take the infimum over covers of \(f\). It follows that
\[
 0\le A_g(f_1)+A_g(f_2)-A_g(f)
 \le2\eta(f:b)+2\delta(v:b).                            \tag{3}
\]
First choosing \(\delta\) and then \(\eta\) makes the right side as small as desired. For \(f=0\) the assertion is immediate.

The product \(P=\prod_{f\in C_c(G)^+}[0,(f:b)]\) is compact by the earlier [arbitrary product compactness theorem](banach-spectrum.md#ha-lca-pre-banach-lemma-4-1). Each \(A_g\) belongs to it. For each neighbourhood \(U\) of \(e\), let \(F_U\) be the closure in \(P\) of the \(A_g\) with nonzero \(g\ge0\) supported in \(U\). Cutoffs make \(F_U\) nonempty. Intersections of finitely many neighbourhoods show that these closed sets have the finite-intersection property, so their total intersection is nonempty. Choose \(A\) in it. Normalization, homogeneity and translation invariance are closed coordinate equalities and pass to \(A\). For each pair \(f_1,f_2\), (3) gives arbitrarily small closed bounds on the additivity defect in an appropriate \(F_U\). Thus \(A\) is additive.

Define \(I(p-q)=A(p)-A(q)\) for nonnegative \(p,q\). This is independent of the decomposition, because \(p-q=p'-q'\) implies \(p+q'=p'+q\), to which additivity applies. It gives a positive real linear functional on the real part of \(C_c(G)\); complexification gives the asserted complex linear functional. It is left invariant and \(I(b)=1\). If \(v\ge0\) is a cutoff equal to one on a compact \(C\), order bounds \(|I(f)|\le I(v)\|f\|_\infty\) for real \(f\) supported there. For complex \(f\), choose a scalar \(\alpha\) of modulus one with \(\alpha I(f)=|I(f)|\) and apply the same order bound to \(\operatorname{Re}(\alpha f)\). Thus \(M_C=I(v)\) works. \(\square\)

<a id="ha-lca-pre-nonabelian-haar-theorem-2-2"></a>
### Theorem 2.2. Haar measure on a sigma-compact subgroup

A sigma-compact locally compact Hausdorff group \(H\) has a nonzero left invariant Borel measure \(\mu_H\), finite on compact sets and inner and outer regular on all Borel sets. Its ordinary completion is left invariant, complete and inner regular by compact sets on every measurable set. Every nonempty open set has positive measure.

**Proof.** Apply Theorem 2.1 on \(H\), then the earlier [positive \(C_c\) representation theorem on a sigma-compact space](haar-measure.md#ha-lca-pre-haar-theorem-3-1). That earlier result is a theorem about general locally compact Hausdorff spaces, and its proof does not assume a group law. It gives the stated Borel measure and its regularity. It is nonzero because \(\int b\,d\mu_H=1\).

For \(a\in H\), the measure \(E\mapsto\mu_H(aE)\) has the same regularity, since translation is a homeomorphism. Its integral of \(f\) is \(\int f(a^{-1}x)\,d\mu_H(x)\): verify this first for indicators, then for nonnegative simple functions and increasing limits, and then for integrable complex functions. Left invariance of \(I\) makes this integral equal to \(I(f)\) for \(f\in C_c(H)\). Uniqueness in the representation theorem gives \(\mu_H(aE)=\mu_H(E)\).

Inner regularity and nontriviality supply a compact set \(C\) of positive measure. If \(U\ne\varnothing\) is open, its left translates cover \(C\), so a finite subcover gives \(0<\mu_H(C)\le m\mu_H(U)\). Thus \(\mu_H(U)>0\). In particular every nonzero nonnegative continuous compactly supported function has a positive integral, since it is bounded below by a positive number on some nonempty open set.

The earlier [completion construction](integration-and-l1.md#ha-lca-pre-integral-lemma-1-1) gives the ordinary completion. Left translations preserve Borel null sets and their subsets, so preserve the completed domain and measure. For a completed set \(E\), choose Borel \(B,N\) with \(\mu_H(N)=0\) and \(E\triangle B\subseteq N\). Then \(B\setminus N\subseteq E\) has the same measure as \(E\); compact inner approximation of \(B\setminus N\) proves inner regularity of the completed measure. \(\square\)

## 3. The full domain and uniqueness

Choose an open sigma-compact subgroup \(H\), a measure \(\mu_H\) from Theorem 2.2, and one representative \(r\) of each left coset \(rH\). For \(E\subseteq G\), put \(E_r=r^{-1}E\cap H\). Define
\[
 \Sigma=\{E\subseteq G:E_r\text{ is completed-}\mu_H
                 \text{-measurable for every }r\},\qquad
 \mu(E)=\sum_r\mu_H(E_r),                               \tag{4}
\]
where a nonnegative sum over an arbitrary index set means the supremum of its finite subsums.

<a id="ha-lca-pre-nonabelian-haar-theorem-3-1"></a>
### Theorem 3.1. The complete locally determined Haar domain

Formula (4) defines a nonzero complete left invariant measure. Its domain contains all Borel sets; it is finite on compact sets, inner regular by compact sets on every measurable set, and positive on every nonempty open set. Changing the representative in a left coset changes neither the domain nor the measure.

Let \(\mathcal D\) be the ordinary completion of the Borel restriction of \(\mu\). Then
\[
 E\in\Sigma
 \quad\Longleftrightarrow\quad
 E\cap K\in\mathcal D\text{ for every compact }K\subseteq G.
 \tag{5}
\]
Equivalently, \(\Sigma\) is the locally determined extension of \(\mathcal D\): \(E\in\Sigma\) exactly when \(E\cap F\in\mathcal D\) for every \(F\in\mathcal D\) of finite measure. If \(E\cap F\in\Sigma\) for every finite-measure \(F\in\Sigma\), then \(E\in\Sigma\). A measurable set whose intersection with every compact set is null is null. Global outer regularity is not assumed.

**Proof.** Each left coset is open and closed and homeomorphic to \(H\); hence Borel sets have Borel sections. Taking sections commutes with complements and countable unions, so \(\Sigma\) is a sigma-algebra. For pairwise disjoint measurable \(E_n\), countable additivity reduces to
\[
 \sum_r\sum_n\mu_H((E_n)_r)=\sum_n\sum_r\mu_H((E_n)_r).
\]
Both sides equal the supremum of sums over finite subsets of the index product: every finite subset lies in a finite rectangle, and countable partial sums exhaust the countable coordinate. Thus \(\mu\) is a measure. It is complete because a set is null exactly when all its sections are null.

Replacing \(r\) by \(rh\), \(h\in H\), replaces the section by \(h^{-1}E_r\), preserving both measurability and measure. For \(a\in G\), write \(ar=sh\), where \(s\) is the chosen representative of the left coset \(arH\) and \(h\in H\). The map \(rt\mapsto art=sht\) sends the section in \(rH\) to its left translate \(hE_r\) in \(sH\). Left multiplication permutes the cosets, and Theorem 2.2 gives the left invariance of (4). Normality of \(H\) has not been used.

A compact set meets finitely many cosets by Lemma 1.1, and its sections are compact, so it has finite measure. For \(E\in\Sigma\), first approximate its arbitrary sum in (4) by finite subsums, then approximate each of those finitely many section measures by compact subsets. Their translates have compact finite union inside \(E\). This proves
\[
 \mu(E)=\sup\{\mu(K):K\subseteq E,\ K\text{ compact}\},   \tag{6}
\]
also when the left side is infinite, by exceeding any prescribed finite bound. A nonempty open set has a nonempty open section in some coset, and therefore positive measure.

We have \(\mathcal D\subseteq\Sigma\) by completeness and inclusion of the Borel sets. If \(E\in\Sigma\) and \(K\) is compact, only finitely many sections of \(E\cap K\) are nonempty. Each such section has a Borel representative modulo a Borel null envelope in \(H\). Translate these finitely many representatives and envelopes to \(G\). Their unions show \(E\cap K\in\mathcal D\). Conversely, if every compact intersection belongs to \(\mathcal D\), intersect with the translated compact exhaustion \(rK_n\) of each coset. Restricting a Borel representative and its Borel null envelope to \(rH\) shows that each resulting section is completed-measurable in \(H\). Taking the union over \(n\) gives measurability of \(E_r\), and proves (5).

Now suppose \(E\in\Sigma\) and \(F\) is Borel with \(\mu F<\infty\). Only countably many sections \(F_r\) have positive measure: for each integer \(n\ge1\), only finitely many can have measure at least \(1/n\). Let \(T\) be the union of those countably many cosets. The set \(F\setminus T\) is Borel and null. On each selected coset, \((E\cap F)_r\) has a Borel representative and Borel null envelope; their countable unions show \(E\cap F\cap T\in\mathcal D\). Every subset of \(F\setminus T\) belongs to \(\mathcal D\), so \(E\cap F\in\mathcal D\). If \(F\in\mathcal D\) has finite measure, put it inside a Borel finite-measure set by adjoining its Borel null envelope; the same conclusion follows by intersection with \(F\). The converse follows by choosing compact \(F\) in (5).

If intersections with all finite-measure members of \(\Sigma\) are only assumed to belong to \(\Sigma\), apply this to compact \(K\). A member of \(\Sigma\) supported in \(K\) belongs to \(\mathcal D\) by the first implication of (5). Thus (5) again gives \(E\in\Sigma\). Finally (6) proves the assertion about null intersections. \(\square\)

<a id="ha-lca-pre-nonabelian-haar-lemma-3-2"></a>
### Lemma 3.2. Determination by \(C_c\), images and positive weights

On a locally compact Hausdorff space, two positive Borel measures finite on compact sets and inner regular on all Borel sets are equal if they have equal integrals on \(C_c\). The image of such a measure under a homeomorphism has the same properties.

For the measure in Theorem 3.1 and a continuous function \(w:G\to(0,\infty)\), the measure
\[
 \nu(E)=\int_E w\,d\mu\qquad(E\in\Sigma)                 \tag{7}
\]
is finite on compact sets and inner regular on all members of \(\Sigma\). It has exactly the same null sets as \(\mu\), and
\[
 \int f\,d\nu=\int fw\,d\mu                             \tag{8}
\]
for nonnegative measurable \(f\), and for complex functions whenever the corresponding absolute integral is finite.

**Proof.** Let the two Borel measures be \(\alpha,\beta\). For compact \(K\), choose an open neighbourhood \(V\supseteq K\) with compact closure \(L\), by finitely many locally compact neighbourhoods and the shrinking lemma. The earlier [compact-localization proof](finite-radon-products.md#ha-lca-pre-product-corollary-2-3) makes both restrictions to \(L\) finite Radon measures. Their outer regularity supplies open neighbourhoods \(U_\alpha,U_\beta\) of \(K\), contained in \(V\), whose excess over \(K\) has respective measure less than \(\varepsilon\). A cutoff \(u\), equal to one on \(K\), between zero and one, with support in \(U_\alpha\cap U_\beta\), gives
\[
 \alpha K\le\int u\,d\alpha<\alpha K+\varepsilon,\qquad
 \beta K\le\int u\,d\beta<\beta K+\varepsilon.
\]
Equality of the integrals and arbitrariness of \(\varepsilon\) give \(\alpha K=\beta K\). Inner regularity on every Borel set proves equality there. A homeomorphism takes compact sets to compact sets and Borel sets to Borel sets in both directions, so the assertion for images follows by taking inverse images in the defining measure and in its compact approximations.

For (7), countable additivity follows from the nonnegative series rule in the earlier [integral construction](integration-and-l1.md#ha-lca-pre-integral-theorem-1-2). Formula (8) holds for indicators by definition, for simple functions by addition, and for nonnegative functions by monotone convergence; decomposition into four nonnegative parts proves the complex case. The function \(w\) is bounded on each compact set, so \(\nu\) is finite there. Its strict positivity gives equivalence of null sets: if \(\int_Ew=0\), then each \(E\cap\{w\ge1/n\}\) is \(\mu\)-null, and their countable union is \(E\).

To prove inner regularity, choose any finite \(a<\nu(E)\), with \(a\ge0\). By the definition of the nonnegative integral, there is a nonnegative finite simple function \(s\le w1_E\) with integral greater than \(a\). Write \(s=\sum_{j=1}^m c_j1_{E_j}\), with disjoint measurable \(E_j\subseteq E\) and \(c_j>0\). Equation (6) and the finite sum supply compact \(K_j\subseteq E_j\) with \(\sum_jc_j\mu K_j>a\), even if a summand of the simple integral is infinite. The compact union \(K\subseteq E\) then has \(\nu K\ge\sum_jc_j\mu K_j>a\). This proves the required supremum identity, for finite or infinite \(\nu(E)\). \(\square\)

<a id="ha-lca-pre-nonabelian-haar-theorem-3-3"></a>
### Theorem 3.3. Uniqueness of left and right Haar measure

Any two nonzero left invariant Borel measures on \(G\), finite on compact sets and inner regular on all Borel sets, are positive scalar multiples. The same assertion holds for right invariant measures with these regularity properties.

Consequently the Borel measure obtained in Theorem 3.1 is independent, up to a positive scalar, of the chosen open subgroup and its Haar measure. The full domain \(\Sigma\) is independent of those choices, and the complete measures on it have the same proportionality.

**Proof.** Let \(\mu,\nu\) be two such left invariant Borel measures. Each is positive on every nonempty open set: compact inner regularity supplies a compact set of positive measure, and finitely many translates of the chosen open set cover it, as in Theorem 2.2. Thus both integrate each nonzero nonnegative member of \(C_c(G)\) to a positive number.

Fix a compact neighbourhood \(V\ni e\). For each sufficiently small neighbourhood \(U\subseteq V\) choose \(u_U\in C_c(G)\), nonnegative and nonzero, supported in \(U\), and normalize \(\int u_U\,d\mu=1\). For \(h\in C_c(G)\), write
\[
 A_U(h)=\int_G u_U(z)\left(\int_G h(yz)\,d\nu(y)\right)d\mu(z).
\]
For \(z\in V\), the difference \(h(yz)-h(y)\) is supported in the fixed compact set \(D=(\operatorname{supp}h)V^{-1}\cup\operatorname{supp}h\). Hence
\[
 |A_U(h)-\textstyle\int h\,d\nu|
 \le \nu(D)\sup_{z\in U}\|R_zh-h\|_\infty\longrightarrow0. \tag{9}
\]
Lemma 1.1 proves this limit for the neighbourhood net.

The kernel \(u_U(z)h(yz)\) is continuous and compactly supported in the two variables: \(z\in\operatorname{supp}u_U\) and \(y\in(\operatorname{supp}h)(\operatorname{supp}u_U)^{-1}\). Thus the earlier compactly supported Fubini theorem, [Corollary 2.3 of the product reading](finite-radon-products.md#ha-lca-pre-product-corollary-2-3), permits reversing the integrals. For fixed \(y\), replace \(z\) by \(y^{-1}x\), using only left invariance of \(\mu\). The new kernel \(h(x)u_U(y^{-1}x)\) also has compact support. Another application of the same Fubini theorem gives
\[
 \begin{aligned}
 A_U(h)
 &=\int_G h(x)\left(\int_G u_U(y^{-1}x)\,d\nu(y)\right)d\mu(x)\\
 &=\left(\int_G h\,d\mu\right)
       \left(\int_G u_U(t^{-1})\,d\nu(t)\right).
 \end{aligned}                                         \tag{10}
\]
In the second line the substitution \(y=xt\) uses left invariance of \(\nu\). No invariance under inversion or right translation has been assumed.

Choose once and for all \(k\in C_c(G)\), \(k\ge0\), \(k\ne0\). Applying (9)–(10) to \(k\) shows that the second factor in (10) tends to
\[
 c=\frac{\int k\,d\nu}{\int k\,d\mu}>0.
\]
Applying the same identity to every \(h\) gives \(\int h\,d\nu=c\int h\,d\mu\). Lemma 3.2 now gives equality of the Borel measures up to \(c\).

If \(\nu\) is right invariant, the image \(E\mapsto\nu(E^{-1})\) is left invariant because \((aE)^{-1}=E^{-1}a^{-1}\). Inversion is a homeomorphism, so Lemma 3.2 preserves regularity. Apply left uniqueness to the two inverted measures and then invert again. This proves right uniqueness.

Two constructions in Theorem 3.1 therefore have proportional Borel restrictions, with identical Borel null sets and hence identical ordinary completions \(\mathcal D\). Characterization (5) gives identical full domains. Their compact values are proportional; compact inner regularity (6) then gives the same proportionality on the full domain. \(\square\)

## 4. The modular function and inversion

<a id="ha-lca-pre-nonabelian-haar-theorem-4-1"></a>
### Theorem 4.1. Modular change of variables

There is a continuous homomorphism \(\Delta:G\to(0,\infty)\), independent of the normalization of Haar measure, such that for every \(E\in\Sigma\) and \(a\in G\),
\[
 \mu(Ea)=\Delta(a)\mu(E),\qquad
 \mu(E^{-1})=\int_E\Delta(x^{-1})\,d\mu(x).              \tag{11}
\]
Right translations and inversion preserve \(\Sigma\) and its null sets. For nonnegative measurable functions, and for complex functions with finite corresponding absolute integral,
\[
 \begin{aligned}
 \int f(ax)\,d\mu(x)&=\int f(x)\,d\mu(x),\\
 \int f(xa)\,d\mu(x)&=\Delta(a)^{-1}\int f(x)\,d\mu(x),\\
 \int f(x^{-1})\,d\mu(x)&=\int f(x)\Delta(x^{-1})\,d\mu(x),\\
 \int f(x)\,d\mu(x)&=\int f(x^{-1})\Delta(x^{-1})\,d\mu(x).
 \end{aligned}                                         \tag{12}
\]
If \(G\) is abelian or compact, then \(\Delta=1\).

**Proof.** First work on Borel sets. For fixed \(a\), \(E\mapsto\mu(Ea)\) is a nonzero left invariant Borel measure: \(b(Ea)=(bE)a\). It is finite on compact sets and inner regular because right translation is a homeomorphism. Theorem 3.3 gives a unique positive scalar \(\Delta(a)\) such that \(\mu(Ea)=\Delta(a)\mu(E)\). There is a compact set \(K\) with \(0<\mu K<\infty\), so evaluating \(\mu(Kab)\) in two steps proves \(\Delta(ab)=\Delta(a)\Delta(b)\). In particular \(\Delta(e)=1\) and \(\Delta(a^{-1})=\Delta(a)^{-1}\). Rescaling \(\mu\) cancels from the definition.

The right-translation integral formula on Borel functions follows from the set formula, first on indicators:
\(\mu(\{x:xa\in E\})=\mu(Ea^{-1})=\Delta(a)^{-1}\mu(E)\).
Simple approximation and the earlier monotone convergence theorem extend it to nonnegative functions, and four-part decomposition gives the integrable complex case. Choose \(0\ne h\in C_c(G)\), \(h\ge0\). Then
\[
 \Delta(a)=\frac{\int h(xa^{-1})\,d\mu(x)}{\int h\,d\mu}.
\]
Lemma 1.1 gives uniform convergence of the numerator's integrand to \(h\), with all differences supported in a fixed compact set as \(a\to e\). Compact finiteness makes the integrals converge. Hence \(\Delta\) is continuous at \(e\). Its homomorphism law gives continuity at every point.

On Borel sets put \(\nu_1(E)=\mu(E^{-1})\) and \(\nu_2(E)=\int_E\Delta(x^{-1})\,d\mu(x)\). The first is right invariant. The second has the required compact finiteness and inner regularity by Lemma 3.2. It is right invariant as well: the already proved right substitution gives
\[
 \nu_2(Ea)=\Delta(a)\int_E\Delta((xa)^{-1})\,d\mu(x)
          =\nu_2(E).
\]
Both are nonzero. Right uniqueness gives \(\nu_1=c\nu_2\) for some \(c>0\). Write \(w(x)=\Delta(x^{-1})\) and \(\check f(x)=f(x^{-1})\). The equality of these measures gives
\[
 \int\check f\,d\mu=c\int fw\,d\mu\qquad(f\in C_c(G)).
 \tag{13}
\]
Apply it to \(\check f\), obtaining \(\int f=c\int w\check f\). To evaluate the latter integral, put \(k(x)=\Delta(x)f(x)\), which is again in \(C_c(G)\). Then \(\check k=w\check f\) and \(wk=f\), so (13) gives \(\int w\check f=c\int f\). Thus \(\int f=c^2\int f\). Taking a nonzero nonnegative \(f\) forces \(c=1\). This proves the inversion formula on Borel sets.

The strict positivity of \(w\) and Lemma 3.2 show that \(\mu(E^{-1})=0\) exactly when \(\mu(E)=0\) for Borel \(E\). Right translation has the same null-set equivalence by its positive scaling factor. Since these maps are homeomorphisms with the same properties for their inverses, they preserve the ordinary completed Borel domain \(\mathcal D\): transform a Borel representative and its Borel null envelope. They therefore preserve \(\Sigma\) by (5), since for a homeomorphism \(T\) of this kind,
\[
 T(E)\cap K=T(E\cap T^{-1}K),
\]
and \(T^{-1}K\) is compact.

For a general \(E\in\Sigma\), inner regularity yields
\[
 \mu(Ea)=\sup_{\substack{K\subseteq E\\K\text{ compact}}}\mu(Ka)
         =\Delta(a)\mu(E).
\]
Likewise \(\mu(E^{-1})=\sup_{K\subseteq E}\mu(K^{-1})\), which equals
\(\sup_{K\subseteq E}\int_Kw\,d\mu=\int_Ew\,d\mu\) by the inner regularity of the weighted measure in Lemma 3.2. This proves (11) on the full domain and also equivalence of its null sets under both maps.

All four formulas in (12) now follow for indicators, for simple functions, and for increasing limits; the last is the inversion formula applied to \(x\mapsto f(x^{-1})\). Complex integrable functions follow by decomposition, with the absolute integral deciding integrability. In an abelian group, \(Ea=aE\), so the right scaling factor is one. In a compact group, \(0<\mu(G)<\infty\), and \(\mu(Ga)=\mu(G)\) likewise forces \(\Delta(a)=1\). \(\square\)

## 5. Function spaces and localization

All \(L^p\) spaces below use \((G,\Sigma,\mu)\). Functions are identified modulo measurable null sets. We need \(p=1,2\); \(L^\infty\) means the essentially bounded measurable classes.

<a id="ha-lca-pre-nonabelian-haar-lemma-5-1"></a>
### Lemma 5.1. Representatives, density and justified product integration

Every \(L^1\) or \(L^2\) class has a finite Borel representative zero outside a countable union of compact sets. The space \(C_c(G)\) is dense in both norms, with nonnegative approximants for nonnegative functions. Both spaces are complete.

Given finitely or countably many such representatives, their supports lie in a common open sigma-compact subgroup \(J\). On \(J\), the restriction of \(\Sigma\) is the ordinary completion of the restricted Borel measure, which is sigma-finite, finite on compact sets and inner regular. Consequently the earlier full-Borel Tonelli and Fubini theorems apply on \(J\times J\) and to its completed product measure.

If \(q:G\to\mathbb C\) is \(\Sigma\)-measurable, its restriction to \(J\) has a Borel representative modulo a null set. The functions \(q(ab)\) and \(q(b^{-1}a)\), for \(a,b\in J\), are measurable for the completed product measure. Replacing \(q\) by an almost-everywhere equal measurable function changes these two functions only on product-null sets.

**Proof.** Let \(p=1\) or \(2\), and let \(f\) be a finite measurable representative with \(\int|f|^p<\infty\). For \(E_m=\{|f|\ge1/m\}\), the inequality \(\mu(E_m)\le m^p\int|f|^p\) gives finite measure. By (6), choose compact \(C_{m,k}\subseteq E_m\) with \(\mu(E_m\setminus C_{m,k})<1/k\). The Borel set \(S=\bigcup_{m,k}C_{m,k}\) contains the nonzero set of \(f\) up to a null set: for each \(m\), the measure of \(E_m\setminus S\) is at most \(1/k\) for every \(k\), and hence zero.

Each of these compact sets meets finitely many left cosets of the original subgroup \(H\). Thus \(S\) lies in a countable union \(T\) of these cosets. This union is open and closed, and is sigma-compact. The restriction of \(\Sigma\) to \(T\) is the ordinary completion of its Borel restriction: choose a Borel representative and Borel null envelope in each selected coset and take their countable unions. The earlier [Borel-representative lemma for completion](integration-and-l1.md#ha-lca-pre-integral-lemma-1-1) supplies a Borel representative of \(f1_S\) on \(T\). Multiply it by \(1_S\) and extend it by zero off \(T\); it remains Borel and represents \(f\) on \(G\).

For \(L^1\), apply the earlier [\(C_c\)-density proof](integration-and-l1.md#ha-lca-pre-integral-theorem-3-1) to this Borel representative. The Borel measure has the required compact finiteness and inner regularity. For \(L^2\), the stronger full-domain version was proved in [Proposition 6.2 of the Hilbert reading](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-6-2); Theorem 3.1 supplies exactly its hypotheses. Both proofs preserve nonnegativity. Completeness follows from the earlier [\(L^1\) completeness theorem](integration-and-l1.md#ha-lca-pre-integral-theorem-2-4) and [\(L^2\) completeness theorem](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-6-1), which apply to arbitrary measure spaces.

The union of the compact support sets of a countable family is still a countable union of compact sets. Lemma 1.1 puts it in an open sigma-compact subgroup \(J\). On \(J\), a countable compact cover and (5) show that every \(\Sigma\)-measurable set is in the ordinary Borel completion: its intersections with the compact cover have Borel representatives and Borel null envelopes, and their countable unions provide these on \(J\). The reverse inclusion follows from completeness. The compact cover proves sigma-finiteness. Compact finiteness and inner regularity are inherited from \(\mu\). Thus the earlier [sigma-finite full-Borel Fubini theorem](integration-and-l1.md#ha-lca-pre-integral-theorem-4-4), including its completion assertion, applies to the restricted measures. This uses all Borel sets of \(J\times J\), without assuming they are generated by measurable rectangles.

Finally replace \(q|_J\) by a Borel function \(q_0\) equal to it off a subset of a Borel null set \(N\subseteq J\), using the same completion lemma. Both maps \((a,b)\mapsto ab\) and \((a,b)\mapsto b^{-1}a\) are continuous, so their inverse images of \(N\) are Borel. For the first map, each section at fixed \(a\) has measure \(\mu(a^{-1}N)=0\). For the second, each section at fixed \(b\) has measure \(\mu(bN)=0\). Tonelli makes both inverse images product-null. Off these sets the pullbacks of \(q\) equal those of \(q_0\); completeness proves their measurability and the assertion about changing representatives. \(\square\)

<a id="ha-lca-pre-nonabelian-haar-proposition-5-2"></a>
### Proposition 5.2. Translation continuity

For \(p=1,2\) and \(a\in G\), left and right translations act on \(L^p\) with
\[
 \|L_af\|_p=\|f\|_p,\qquad
 \|R_af\|_p=\Delta(a)^{-1/p}\|f\|_p.                    \tag{14}
\]
For every \(f\in L^p\), \(a\mapsto L_af\) and \(a\mapsto R_af\) are norm-continuous. The two actions are jointly continuous in \(a,f\). Left and right translation, and unweighted inversion \(f(x)\mapsto f(x^{-1})\), preserve essential supremum norms on \(L^\infty\).

**Proof.** Theorem 4.1 makes all the relevant maps measurable and preserves the null sets on which representatives may differ. Apply (12) to \(|f|^p\) to obtain (14). For \(f\in C_c(G)\), Lemma 1.1 gives a common compact support \(D\) for the differences near \(e\); hence their \(L^p\) norms are bounded by \(\mu(D)^{1/p}\) times their uniform norms and tend to zero.

For general \(f\), choose \(v\in C_c(G)\) with \(\|f-v\|_p\) small, using Lemma 5.1. The left-translation error is at most
\[
 \|L_af-f\|_p\le2\|f-v\|_p+\|L_av-v\|_p.
\]
The corresponding right error is at most
\[
 \|R_af-f\|_p\le(1+\Delta(a)^{-1/p})\|f-v\|_p
                 +\|R_av-v\|_p.
\]
Continuity of \(\Delta\) bounds the coefficient near \(e\), proving continuity there. The identities \(L_aL_b=L_{ab}\), \(R_aR_b=R_{ab}\), verified directly from their definitions, and their fixed operator norms in (14) transfer this to every \(a_0\). Joint continuity follows from
\(\|T_af-T_{a_0}f_0\|_p\le\|T_a\|\|f-f_0\|_p+\|T_af_0-T_{a_0}f_0\|_p\),
where \(T_a\) is either action and its norms are locally bounded. For \(L^\infty\), each level set \(\{|f|>c\}\) is null exactly when its image or inverse image under any of the three transformations is null, by Theorem 4.1. This proves equality of essential suprema. \(\square\)

## 6. The convolution algebra and approximate identities

<a id="ha-lca-pre-nonabelian-haar-theorem-6-1"></a>
### Theorem 6.1. The modular Banach star algebra \(L^1(G)\)

For \(f,g\in L^1(G)\), the convolution
\[
 (f*g)(x)=\int_G f(y)g(y^{-1}x)\,d\mu(y)                \tag{15}
\]
exists absolutely for almost every \(x\), defines an \(L^1\) class independently of representatives, and satisfies
\[
 \|f*g\|_1\le\|f\|_1\|g\|_1.
 \tag{16}
\]
With the involution
\[
 f^*(x)=\Delta(x^{-1})\overline{f(x^{-1})},              \tag{17}
\]
this makes \(L^1(G)\) a Banach star algebra:
\[
 (f*g)*h=f*(g*h),\quad (f*g)^*=g^**f^*,\quad
 f^{**}=f,\quad\|f^*\|_1=\|f\|_1.
 \tag{18}
\]
For \(f,g\in C_c(G)\), \(f*g\in C_c(G)\) and
\(\operatorname{supp}(f*g)\subseteq(\operatorname{supp}f)(\operatorname{supp}g)\).
Where the absolute integrals exist, there is also the formula
\[
 (f*g)(x)=\int_G\Delta(z^{-1})f(xz^{-1})g(z)\,d\mu(z).
 \tag{19}
\]
For any bounded \(\Sigma\)-measurable \(q\),
\[
 \int_G(f*g)(x)q(x)\,d\mu(x)
 =\iint f(a)g(b)q(ab)\,d\mu(a)\,d\mu(b).               \tag{20}
\]
The double integral in (20) is taken on a common open sigma-compact subgroup supporting Borel representatives of \(f,g\); it is absolutely integrable and independent of that choice.

**Proof.** Start with \(f,g\in C_c(G)\). Formula (15) is absolutely integrable for every \(x\). A nonzero integrand requires \(y\in C=\operatorname{supp}f\) and \(y^{-1}x\in D=\operatorname{supp}g\), so \(x\in CD\). For \(x\to x_0\), continuity of \((y,x)\mapsto g(y^{-1}x)\) and compact-parameter uniformity on \(C\) give
\[
 |(f*g)(x)-(f*g)(x_0)|
 \le\|f\|_1\sup_{y\in C}|g(y^{-1}x)-g(y^{-1}x_0)|
 \longrightarrow0.
\]
Thus the function is continuous with compact support in \(CD\). Compactly supported Fubini, applied to \(|f(y)g(y^{-1}x)|\), and the substitution \(x=yz\), give
\[
 \int|(f*g)(x)|\,d\mu(x)
 \le\int|f(y)|\left(\int|g(y^{-1}x)|\,d\mu(x)\right)d\mu(y)
 =\|f\|_1\|g\|_1.
\]

For three compactly supported continuous functions, expand \(((f*g)*h)(x)\), reverse the \(t,y\) integrals, and put \(t=yz\). The result is
\[
 \iint f(y)g(z)h(z^{-1}y^{-1}x)\,d\mu(z)\,d\mu(y)
 =(f*(g*h))(x).
\]
Before the substitution, the integrand has support in
\((\operatorname{supp}f)(\operatorname{supp}g)\times\operatorname{supp}f\)
in the \(t,y\) variables; after it, the support lies in
\(\operatorname{supp}f\times\operatorname{supp}g\).
Both interchanges are therefore justified by compactly supported continuous Fubini.

Theorem 4.1 makes (17) measurable and shows, by the last identity of (12),
\[
 \int|f^*|\,d\mu=\int|f|\,d\mu,\qquad
 \int f^*\,d\mu=\overline{\int f\,d\mu}.
 \tag{21}
\]
The involution is conjugate-linear and \(f^{**}=f\), because
\(\Delta(x^{-1})\Delta(x)=1\). It takes \(C_c\) to \(C_c\). For \(f,g\in C_c\), expansion gives
\[
 \begin{aligned}
 (g^**f^*)(x)
 &=\Delta(x^{-1})\int
       \overline{g(y^{-1})}\,\overline{f(x^{-1}y)}\,d\mu(y)\\
 &=\Delta(x^{-1})\int
       \overline{g(z^{-1}x^{-1})}\,\overline{f(z)}\,d\mu(z)
  =(f*g)^*(x),
 \end{aligned}
\]
where \(y=xz\) is a left translation. This proves the required reversal of factors.

Density and completeness from Lemma 5.1 extend convolution to all of \(L^1\): if \(f_n\to f\), \(g_n\to g\) in \(L^1\), with \(f_n,g_n\in C_c\), then
\[
 \|f_n*g_n-f_m*g_m\|_1
 \le\|f_n-f_m\|_1\|g_n\|_1+\|f_m\|_1\|g_n-g_m\|_1.
\]
The products are Cauchy and their limit is independent of the approximants, by the same estimate. Bilinearity and (16) pass to limits. The isometric involution passes to limits as well. Associativity and the star identity follow by approximating all their inputs: an error in any input of a triple product is bounded by its norm times the norms of the other two inputs, and convergent approximants have bounded norms.

To verify (15) for these limits, choose finite Borel representatives of \(f,g\) supported in a common open sigma-compact subgroup \(J\), by Lemma 5.1. On \(J\times J\) the kernel \(f(y)g(y^{-1}x)\) is Borel. It is zero off \(J\) in either integration variable when viewed on \(G\): if \(f(y)\ne0\) and \(g(y^{-1}x)\ne0\), both \(y\) and \(y^{-1}x\) belong to \(J\), so \(x\in J\). The full-Borel Tonelli theorem on \(J\) gives
\[
 \iint |f(y)g(y^{-1}x)|\,d\mu(x)\,d\mu(y)
 =\int_J|f(y)|\|g\|_1\,d\mu(y)
 =\|f\|_1\|g\|_1.
\]
Fubini supplies a Borel section integral, with value zero assigned on the Borel exceptional null set and off \(J\). The same estimate for input differences makes this integral construction continuous in both \(L^1\) inputs. It agrees with the previous construction on \(C_c\), hence everywhere by density.

If \(f',g'\) are other finite measurable representatives, choose measurable null sets \(N_f,N_g\) outside which they agree with the chosen ones. For each fixed \(x\), the two section integrands agree off \(N_f\cup xN_g^{-1}\), a measurable null set by Theorem 4.1. Each section is measurable, because \(y\mapsto y^{-1}x\) preserves the full measurable domain. Therefore its absolute integrability and integral are unchanged. This proves representative independence.

Formula (19) follows by \(y=xz^{-1}\), using the left and inversion formulas in (12). Those formulas apply to nonnegative absolute values first, so the equality is valid whenever either absolute integral is finite. Finally, for (20), use the same subgroup \(J\). If \(q\) is Borel there, Fubini and \(x=ab\) in (15) give the identity, and the absolute double integral is at most \(\|q\|_\infty\|f\|_1\|g\|_1\). For a general measurable \(q\), Lemma 5.1 supplies a Borel representative and proves that its multiplication pullback differs only on a completed-product null set. The single integral also ignores the null difference. Thus (20) holds. Enlarging or changing \(J\) leaves the left side unchanged, proving independence. \(\square\)

<a id="ha-lca-pre-nonabelian-haar-corollary-6-2"></a>
### Corollary 6.2. A two-sided self-adjoint approximate identity

For each neighbourhood \(U\) of \(e\), there is \(u_U\in C_c(G)\) with
\[
 u_U\ge0,\quad u_U^*=u_U,\quad
 \operatorname{supp}u_U\subseteq U,\quad
 \int u_U\,d\mu=\|u_U\|_1=1.
 \tag{22}
\]
For neighbourhoods directed by reverse inclusion,
\[
 u_U*f\longrightarrow f,\qquad f*u_U\longrightarrow f
 \quad\hbox{in }L^1(G)\quad(f\in L^1(G)).
 \tag{23}
\]
For \(h\in C_0(G)\), both convolutions belong to \(C_0(G)\) and converge uniformly to \(h\).

**Proof.** Choose \(v\in C_c(G)\), \(v\ge0\), \(v(e)>0\), with support in an open neighbourhood contained in \(U\cap U^{-1}\). The continuous nonnegative function \(w=v+v^*\) is self-adjoint and supported in \(U\). It has positive finite integral by Theorem 3.1. Define \(u_U=w/\int w\). Equation (21) and conjugate-linearity of the involution give all properties in (22).

For \(f\in L^1\), localize its Borel representative and \(u_U\) in a common open sigma-compact subgroup. Positive Fubini there, applied to \(u_U(a)|f(a^{-1}x)-f(x)|\), gives
\[
 \|u_U*f-f\|_1
 \le\int u_U(a)\|L_af-f\|_1\,d\mu(a)
 \le\sup_{a\in U}\|L_af-f\|_1\longrightarrow0.
\]
The last limit is Proposition 5.2. The reversed product follows without changing modular conventions:
\[
 \|f*u_U-f\|_1
 =\|(f*u_U-f)^*\|_1
 =\|u_U*f^*-f^*\|_1\longrightarrow0.
\]

For \(h\in C_0(G)\), (15) gives
\[
 \|u_U*h-h\|_\infty\le\sup_{a\in U}\|L_ah-h\|_\infty\longrightarrow0
\]
by Lemma 1.1. This convolution is in \(C_0\): approximate \(h\) uniformly by \(h_n\in C_c\), for which \(u_U*h_n\in C_c\), and use
\(\|u_U*(h-h_n)\|_\infty\le\|h-h_n\|_\infty\)
and the earlier completeness of \(C_0\).

Formula (19), initially for \(h_n\), passes to the uniform limit because
\[
 m_U=\int u_U(z)\Delta(z^{-1})\,d\mu(z)<\infty.
\]
It defines \(h*u_U\), with \(\|(h-h_n)*u_U\|_\infty\le m_U\|h-h_n\|_\infty\); hence \(h*u_U\in C_0\). This agrees with (15): for each fixed \(x\), that integrand is bounded and supported in the compact set \(x(\operatorname{supp}u_U)^{-1}\), so uniform approximation of \(h\) passes to its integral. Moreover
\[
 \|h*u_U-h\|_\infty
 \le m_U\sup_{z\in U}\|R_{z^{-1}}h-h\|_\infty
       +|m_U-1|\|h\|_\infty.
\]
Continuity of \(\Delta\) at \(e\) and \(\int u_U=1\) give
\(|m_U-1|\le\sup_{z\in U}|\Delta(z^{-1})-1|\to0\),
while Lemma 1.1 makes the other error tend to zero. This proves uniform convergence on both sides. \(\square\)

## 7. Unitary representations and integration

Inner products are linear in the first variable. All Hilbert-space facts used here have their complete proofs in the earlier [Hilbert reading](hilbert-spaces-and-unitary-representations.md).

<a id="ha-lca-pre-nonabelian-haar-proposition-7-1"></a>
### Proposition 7.1. Left and right regular representations

On \(L^2(G)\), define
\[
 (\lambda(a)f)(x)=f(a^{-1}x),\qquad
 (\rho(a)f)(x)=\Delta(a)^{1/2}f(xa).
 \tag{24}
\]
These are commuting strongly continuous unitary representations of \(G\).

**Proof.** Proposition 5.2 gives well-defined actions on classes and shows that both operators in (24) are isometries. Their inverses are the operators at \(a^{-1}\), by the homomorphism property of \(\Delta\). Their group laws follow from \(L_aL_b=L_{ab}\), \(R_aR_b=R_{ab}\) and \(\Delta(ab)^{1/2}=\Delta(a)^{1/2}\Delta(b)^{1/2}\). The positive square root is continuous on \((0,\infty)\), as proved in the Hilbert reading's [continuous-calculus argument](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-3-2). Proposition 5.2 and continuity of \(\Delta\) therefore give strong continuity. Finally
\[
 L_aR_bf(x)=f(a^{-1}xb)=R_bL_af(x)
\]
for representatives, so the two unitary actions commute on classes. \(\square\)

<a id="ha-lca-pre-nonabelian-haar-theorem-7-2"></a>
### Theorem 7.2. Integrating a unitary representation

Let \(\pi:G\to U(\mathcal H)\) be strongly continuous on an arbitrary Hilbert space. For every \(f\in L^1(G)\) there is a unique bounded operator \(\pi(f)\) satisfying
\[
 \langle\pi(f)\xi,\eta\rangle
 =\int_G f(a)\langle\pi(a)\xi,\eta\rangle\,d\mu(a).
 \tag{25}
\]
It depends linearly on \(f\), and
\[
 \|\pi(f)\|\le\|f\|_1,\quad
 \pi(f*g)=\pi(f)\pi(g),\quad
 \pi(f^*)=\pi(f)^*,\quad
 \pi(L_af)=\pi(a)\pi(f).                               \tag{26}
\]
For (22), \(\pi(u_U)\xi\to\xi\) for every \(\xi\). Thus the closed span of \(\pi(L^1(G))\mathcal H\) is \(\mathcal H\).

A bounded operator commutes with all \(\pi(a)\) if and only if it commutes with all \(\pi(f)\). For any \(\xi\), the closed linear span of \(\{\pi(a)\xi:a\in G\}\) equals that of \(\{\pi(f)\xi:f\in L^1(G)\}\).

**Proof.** On the zero Hilbert space every assertion is immediate; assume \(\mathcal H\ne\{0\}\). The coefficient in (25) is continuous by strong continuity and Cauchy–Schwarz, and has absolute value at most \(\|\xi\|\|\eta\|\). The integral defines a bounded sesquilinear form, independent of the representative of \(f\), with bound \(\|f\|_1\|\xi\|\|\eta\|\). The earlier [bounded-form representation theorem](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-2-4) supplies the unique operator, its norm bound and linear dependence on \(f\).

For fixed \(\xi,\eta\), unitarity gives
\[
 \begin{aligned}
 \langle\pi(f)\pi(g)\xi,\eta\rangle
 &=\int f(a)\langle\pi(g)\xi,\pi(a^{-1})\eta\rangle\,d\mu(a)\\
 &=\iint f(a)g(b)\langle\pi(ab)\xi,\eta\rangle\,d\mu(b)\,d\mu(a).
 \end{aligned}
\]
The coefficient is continuous on \(G\times G\), and the absolute integrand is bounded by
\(|f(a)g(b)|\|\xi\|\|\eta\|\).
Lemma 5.1 justifies Fubini on a common open sigma-compact subgroup supporting representatives of \(f,g\). Equation (20), with the bounded continuous function \(q(x)=\langle\pi(x)\xi,\eta\rangle\), identifies the result with \(\langle\pi(f*g)\xi,\eta\rangle\). This proves multiplicativity.

Using the adjoint identity, the scalar convention and (12),
\[
 \begin{aligned}
 \langle\pi(f)^*\xi,\eta\rangle
 &=\langle\xi,\pi(f)\eta\rangle
   =\int\overline{f(a)}\,\langle\pi(a^{-1})\xi,\eta\rangle\,d\mu(a)\\
 &=\int\Delta(a^{-1})\overline{f(a^{-1})}
                  \langle\pi(a)\xi,\eta\rangle\,d\mu(a)
   =\langle\pi(f^*)\xi,\eta\rangle.
 \end{aligned}
\]
The absolute integral is finite by (21). Left substitution \(x=ab\) in (25) similarly gives \(\pi(L_af)=\pi(a)\pi(f)\), completing (26).

For a unit vector \(\eta\), (25) and (22) give
\[
 |\langle(\pi(u_U)-I)\xi,\eta\rangle|
 \le\int u_U(a)\|\pi(a)\xi-\xi\|\,d\mu(a)
 \le\sup_{a\in U}\|\pi(a)\xi-\xi\|.
\]
The norm equals the supremum over unit \(\eta\), as proved with Hilbert Riesz representation. Strong continuity makes the last bound tend to zero. The assertion about the closed span follows.

If \(T\) commutes with every \(\pi(a)\), then bounded adjoints and (25) give
\[
 \begin{aligned}
 \langle T\pi(f)\xi,\eta\rangle
 &=\int f(a)\langle\pi(a)\xi,T^*\eta\rangle\,d\mu(a)\\
 &=\int f(a)\langle\pi(a)T\xi,\eta\rangle\,d\mu(a)
  =\langle\pi(f)T\xi,\eta\rangle.
 \end{aligned}
\]
Conversely, if \(T\) commutes with every \(\pi(f)\), apply this to \(L_au_U\). By (26) and the convergence just proved,
\[
 \pi(L_au_U)\xi=\pi(a)\pi(u_U)\xi\longrightarrow\pi(a)\xi.
 \]
Passing to limits in \(T\pi(L_au_U)\xi=\pi(L_au_U)T\xi\) yields \(T\pi(a)\xi=\pi(a)T\xi\).

Finally let \(M\) be the closed orbit span of \(\xi\). If \(\eta\in M^\perp\), every coefficient \(\langle\pi(a)\xi,\eta\rangle\) vanishes, so (25) gives \(\langle\pi(f)\xi,\eta\rangle=0\). The earlier [double-orthogonal-complement theorem](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-corollary-2-2) gives \(\pi(f)\xi\in M\). Conversely the displayed approximation puts every \(\pi(a)\xi\) in the closed span of the integrated orbit. Both closed spans are therefore equal. \(\square\)
