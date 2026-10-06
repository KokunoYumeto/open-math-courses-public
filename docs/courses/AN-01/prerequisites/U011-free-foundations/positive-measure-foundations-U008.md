# Positive functionals and locally finite measures

*Prepared by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original programme exposition: CC0. This proof adapts the earlier CC0 programme lesson **Haar measure on locally compact groups**, Section 2, to the open Euclidean sets needed by AN-01. The measure construction and all required prerequisites are supplied here; no group theorem is used.*

Let \(X\subset\mathbb R^n\) be open, with \(n\ge1\). We use the included [scalar calculus and Euclidean topology](metric-foundation-bridges.md), [finite algebra](stable-prerequisite-bridges.md) and [measure and integral constructions](banach-foundation-bridges.md). In particular, the last text proves the nonnegative integral, monotone convergence, dominated convergence and the generating-class argument. All pairings are complex linear, without conjugating the test. The empty open set has only the zero functional and zero measure; below we treat the nonempty case.

## Compact cutoffs and finite partitions

The scalar prerequisite, Section 13.10, gives a smooth function between zero and one which equals one on a specified closed ball and vanishes outside any specified larger concentric ball. If \(K\subset U\subset X\), with \(K\) compact and \(U\) open, cover \(K\) by finitely many inner balls whose larger closed balls lie in \(U\). Such balls exist by openness, and a finite subcover exists by compactness. For their cutoffs \(b_1,\ldots,b_N\), put

\[
 b=1-\prod_{j=1}^N(1-b_j).
 \tag{M1}
\]

Then \(0\le b\le1\), \(b=1\) on a neighborhood of \(K\), and \(b\) has compact support in \(U\). If \(K\) is empty, use zero.

We also need a partition for a finite open cover \(K\subset U_1\cup\cdots\cup U_N\). Choose the preceding finite collection of ball cutoffs, each assigned to one \(U_j\), with inner balls covering \(K\). For each \(j\), combine its assigned cutoffs by (M1), calling the result \(g_j\), and use zero if there are none. Define

\[
 h_j=g_j\prod_{i<j}(1-g_i).
 \tag{M2}
\]

Each \(h_j\) is smooth, nonnegative and compactly supported in \(U_j\). The telescoping identity \(\sum_jh_j=1-\prod_j(1-g_j)\) shows that this sum is at most one everywhere and equals one on a neighborhood of \(K\).

For later exhaustions we may take

\[
 K_j=\{x\in X:|x|\le j,\ 
       \operatorname{dist}(x,\mathbb R^n\setminus X)\ge1/j\}.
 \tag{M3}
\]

When \(X=\mathbb R^n\), omit the distance condition. Distance to a nonempty closed set is continuous: the triangle inequality bounds the difference of two distances by the distance between the points. Thus \(K_j\) is compact, \(K_j\subset\operatorname{int}K_{j+1}\), and these interiors exhaust \(X\). Every compact subset of \(X\) is in one such interior, since its norm is bounded and its distance to the complement has a positive minimum. Choosing \(b_j=1\) near \(K_j\), supported in \(\operatorname{int}K_{j+1}\), the functions \(1-\prod_{i\le j}(1-b_i)\) increase to one. Applying the same construction to any open \(U\subset X\) gives compact smooth cutoffs increasing pointwise to \(1_U\), extended by zero outside \(U\).

## Positive Riesz representation on an open Euclidean set

A positive Radon measure here is a Borel measure finite on compact sets, outer regular on Borel sets and inner regular on open sets. We will prove inner regularity on every Borel set as well. Write \(f\prec U\) when \(f\in C_c(X)\), \(0\le f\le1\), and \(\operatorname{supp}f\subset U\).

**Theorem M.** Let \(I:C_c(X;\mathbb R)\to\mathbb R\) be positive and linear. There is a unique positive Radon measure \(\mu\) with

\[
 I(f)=\int_X f\,d\mu.
 \tag{M4}
\]

Its masses satisfy

\[
 \begin{aligned}
 \mu(U)&=\sup_{f\prec U}I(f),\qquad U\text{ open},\\
 \mu(K)&=\inf\{I(f):f\in C_c(X),\ f\ge1_K\},
                 \qquad K\text{ compact}.
 \end{aligned}
 \tag{M5}
\]

In the second infimum \(f\ge1_K\) includes nonnegativity off \(K\). Complexifying \(I\) extends (M4) to complex continuous tests.

**Proof.** Positivity implies monotonicity, since \(f\le g\) gives \(I(g)-I(f)=I(g-f)\ge0\). Put

\[
 m(U)=\sup_{f\prec U}I(f),\qquad
 m^*(A)=\inf_{U\supset A,\ U\text{ open}}m(U).
 \tag{M6}
\]

These quantities may be infinite. They are nonnegative and monotone, and \(m^*(U)=m(U)\) for open \(U\). Also \(m(\varnothing)=0\).

If \(U=\bigcup_j U_j\) and \(f\prec U\), compactness gives a finite subcover of \(\operatorname{supp}f\). The partition (M2) yields \(f=\sum_jfh_j\) over that finite collection, with \(fh_j\prec U_j\). Therefore \(I(f)\le\sum_jm(U_j)\), and taking the supremum proves open-set subadditivity. For arbitrary \(A_j\), if \(\sum_jm^*(A_j)<\infty\), choose open \(U_j\supset A_j\) with \(m(U_j)<m^*(A_j)+\varepsilon2^{-j}\). Their union proves \(m^*(\bigcup_jA_j)\le\sum_jm^*(A_j)+\varepsilon\). Let \(\varepsilon\downarrow0\). An infinite sum needs no estimate. Thus \(m^*\) is an outer measure.

We give the measurability step explicitly. Call \(E\) measurable if every \(A\subset X\) satisfies

\[
 m^*(A)=m^*(A\cap E)+m^*(A\setminus E).
 \tag{M7}
\]

The inequality at most always holds by subadditivity. Complements preserve this condition. If \(E,F\) satisfy it, splitting first by \(E\) and then by \(F\) decomposes \(m^*(A)\) as the sum for four pieces. Subadditivity bounds the three pieces outside \(E\cap F\) below by the outer measure of their union. This proves (M7) for \(E\cap F\), and hence finite unions as well. For disjoint measurable \(E_j\), repeated finite splitting gives

\[
 m^*(A)\ge\sum_{j=1}^N m^*(A\cap E_j)
                +m^*\left(A\setminus\bigcup_{j=1}^\infty E_j\right).
 \tag{M8}
\]

Let \(N\) increase. Countable subadditivity bounds \(m^*(A\cap\bigcup_jE_j)\) by the resulting sum, giving (M7) for the union. Disjointifying an arbitrary countable union proves that the measurable sets form a sigma-algebra. Taking \(A=\bigcup_jE_j\) in (M8), with subadditivity for the reverse inequality, proves countable additivity on this sigma-algebra.

Every open \(U\) is measurable. First take an open \(V\) with \(m(V)<\infty\). Choose \(f\prec V\cap U\) within \(\varepsilon\) of its supremum in (M6), and \(g\prec V\setminus\operatorname{supp}f\) within \(\varepsilon\) of that supremum. Both suprema are finite. The disjoint supports give \(f+g\prec V\), so

\[
 \begin{aligned}
 m(V)&\ge I(f)+I(g)\\
 &>m(V\cap U)+m(V\setminus\operatorname{supp}f)-2\varepsilon\\
 &\ge m^*(V\cap U)+m^*(V\setminus U)-2\varepsilon.
 \end{aligned}
\]

Let \(\varepsilon\downarrow0\). For arbitrary \(A\) of finite outer measure, choose open \(V\supset A\) with \(m(V)<m^*(A)+\varepsilon\), use this inequality and monotonicity, and then let \(\varepsilon\downarrow0\) again. If \(m^*(A)=\infty\), the required lower inequality is automatic. This proves (M7) for \(U\). All Borel sets are therefore measurable. Define \(\mu=m^*\) on them. Outer regularity follows from (M6).

If \(K\) is compact and \(f\in C_c(X)\) satisfies \(f\ge1_K\), then for \(0<c<1\), the open set \(U_c=\{f>c\}\) contains \(K\). Every \(g\prec U_c\) satisfies \(cg\le f\), so \(\mu(K)\le m(U_c)\le I(f)/c\). Letting \(c\uparrow1\) gives \(\mu(K)\le I(f)\). By (M1) some such \(f\) exists, so compact sets have finite mass. Conversely, outer regularity and (M1) give, for every \(\varepsilon>0\), a cutoff equal to one on \(K\) whose functional value is at most \(\mu(K)+\varepsilon\). This proves the compact formula in (M5).

For \(f\prec U\), every open neighborhood of \(\operatorname{supp}f\) has \(m\)-value at least \(I(f)\). Hence \(I(f)\le\mu(\operatorname{supp}f)\). Taking the supremum gives

\[
 \mu(U)=\sup_{K\subset U,\ K\text{ compact}}\mu(K).
 \tag{M9}
\]

To prove (M4), first take \(0\le f\le1\) and an integer \(N\ge1\). Let \(K_0=\operatorname{supp}f\), \(K_j=\{f\ge j/N\}\) for \(1\le j\le N\), and

\[
 f_j=\min\{\max(f-(j-1)/N,0),1/N\}.
\]

These functions sum to \(f\), are supported in \(K_{j-1}\), and lie between \(1_{K_j}/N\) and \(1_{K_{j-1}}/N\). The compact formula and outer regularity therefore put both \(I(f_j)\) and \(\int f_j\,d\mu\) between \(\mu(K_j)/N\) and \(\mu(K_{j-1})/N\). Summing, both \(I(f)\) and its integral lie in one interval of length at most \(\mu(K_0)/N\). Let \(N\to\infty\). Scaling and positive-minus-negative parts give (M4) for every real test.

For uniqueness, any Radon measure representing \(I\) has the open formula (M5): one inequality follows from \(0\le f\le1_U\), and the other follows by placing a cutoff between any compact \(K\subset U\) and \(U\), then using inner regularity. Thus two representing Radon measures agree on open sets. Outer regularity gives equality on every Borel set. \(\square\)

**Inner regularity on Borel sets.** Suppose \(E\) is Borel and \(\mu(E)<\infty\). Given \(\varepsilon>0\), choose open \(U\supset E\) with \(\mu(U)<\mu(E)+\varepsilon\). Then \(\mu(U\setminus E)<\varepsilon\). Choose open \(W\supset U\setminus E\) with \(\mu(W)<\varepsilon\), and compact \(F\subset U\) with \(\mu(F)>\mu(U)-\varepsilon\). The compact set \(F\setminus W\) lies in \(E\) and has mass greater than \(\mu(E)-2\varepsilon\). For arbitrary \(E\), the sets \(E\cap K_j\) have finite measure and increase to \(E\). Countable additivity gives continuity from below, so the preceding compact approximations prove inner regularity on all Borel sets.

## Complex measures, variation and continuous weights

A finite complex measure in this text is a linear combination \(\mu=\mu_1-\mu_2+i\mu_3-i\mu_4\) of finite positive Radon measures. Its integrals against bounded Borel functions are defined by that combination. The definition is independent of the representation: equality as set functions gives equality on simple functions, and uniformly approximating a bounded Borel function by simple functions gives the same integrals. Such approximations come from a finite grid of small rectangles in the bounded complex range. Put \(\lambda=\sum_{j=1}^4\mu_j\); then \(|\int f\,d\mu|\le\int|f|\,d\lambda\).

The total variation is

\[
 |\mu|(E)=\sup_{\{E_l\}}\sum_l|\mu(E_l)|,
 \tag{M10}
\]

where the supremum is over finite Borel partitions of \(E\). Refining a partition cannot decrease its sum, by the scalar triangle inequality. Combining partitions of disjoint sets proves one direction of finite additivity; refining any partition by those sets proves the other. Also \(|\mu|(E)\le\lambda(E)\). For a disjoint sequence, the \(\lambda\)-mass of the union of its tail tends to zero because \(\lambda\) is finite. The domination turns finite additivity into countable additivity of \(|\mu|\). Compact and open approximations in \(\lambda\)-measure also approximate in variation, so \(|\mu|\) is a finite positive Radon measure. The simple-function inequality and uniform approximation give

\[
 \left|\int f\,d\mu\right|
      \le\int|f|\,d|\mu|.
 \tag{M11}
\]

A finite sum of positive Radon measures is Radon: take the union of finitely many compact inner approximations and the intersection of finitely many open outer approximations. Consequently two finite complex Radon measures with equal integrals on \(C_c(X)\) are equal. Indeed, after taking real parts on real tests, move the negative parts to the opposite side. This gives equal integrals for two positive Radon measures, to which Theorem M's uniqueness applies. Treat imaginary parts in the same way.

We use a *locally finite complex Radon measure* to mean compatible finite complex Radon measures on relatively compact open subsets. Integration against a compactly supported continuous test is then unambiguous. The variation measures agree on overlaps by (M10). To construct their global positive Radon measure, integrate a real compact test against the local variation in any relatively compact open neighborhood of its support. Compatibility makes this independent of the neighborhood; choosing one neighborhood for two supports proves linearity. It is a positive functional, so Theorem M represents it by a positive Radon measure. On each relatively compact open subset, Theorem M's uniqueness identifies its restriction with the given local variation. This constructs the global variation and proves its local finiteness and regularity. This local convention does not assign an expression such as \(\infty-\infty\) to an arbitrary unbounded Borel set. Equality can be checked on compactly supported continuous tests, by the finite uniqueness argument on each relatively compact open subset and its exhaustion.

If \(\rho\ge0\) is continuous and \(\lambda\) is positive Radon, the Borel measure

\[
 \nu(E)=\int_E\rho\,d\lambda
 \tag{M12}
\]

is Radon and finite on compact sets. Here are the regularity details. Monotone convergence proves countable additivity, and boundedness of \(\rho\) on compacts proves local finiteness. Apply Theorem M to the positive functional \(f\mapsto\int\rho f\,d\lambda\), obtaining a Radon measure \(\eta\). For any open \(U\), its increasing compact cutoffs constructed after (M3), together with monotone convergence, give \(\eta(U)=\nu(U)\) by (M5). To extend equality to Borel sets, exhaust \(X\) by relatively compact open sets. On each such set the two measures are finite, agree on the intersection-closed class of relative open sets, and hence agree on all Borel sets by the generating-class proof in Section 16.2 of the integration prerequisite. Continuity from below then gives equality on \(X\). Thus \(\nu=\eta\), proving the claim.

Apply (M12) to the four positive parts of a complex measure to define \(\rho\mu\) locally. Inequality (M11), or the dominating sum of the four weighted positive parts, gives finite variation on each compact set. On any open set where \(\rho=0\), the weighted measure is zero; hence its support lies in \(\operatorname{supp}\rho\). The support here is the complement of the union of open sets on which the measure is zero. A countable Euclidean base makes that union a countable union of such zero regions, so the measure really vanishes off its support.

## Source comparison

The earlier programme proof adapted here is **Haar measure on locally compact groups**, Theorem 2.2, Proposition 2.3 and the finite-variation part of Theorem 2.4. It is CC0. Its use of general locally compact topology has been replaced by (M1)–(M3), and the required outer-measure argument is included in (M7)–(M8). This selection proves precisely the open-Euclidean scope used by U008.

D. H. Fremlin's freely accessible author edition of [*Measure Theory*, Chapter 43](https://www1.essex.ac.uk/maths/people/fremlin/chap43.pdf), 436J, supplies a human comparison for positive representation. His general Radon convention includes completion and local determination. The construction above explicitly uses Borel measures and proves the regularity needed here; none of Fremlin's broader representation machinery is an unproved input.
