# Integration and \(L^1\) without a countability assumption

**Programme reading HA-LCA-PRE-INTEGRAL.** This prerequisite proves the convergence, density and completeness statements needed for Haar integration. Sections 1–2 apply to an arbitrary measure space: neither finiteness nor sigma-finiteness is implicit. Topological regularity enters only in Section 3.

The freely accessible source material is D. H. Fremlin, *Measure Theory*, [§123, version of 18 November 2004](https://www1.essex.ac.uk/maths/people/fremlin/mt1.2011/mt123.tex), especially 123A–C, and [§242, version of 19 November 2003](https://www1.essex.ac.uk/maths/people/fremlin/mt2.2016/mt242.tex), especially 242D–F, 242M and 242P. The measure and simple-integral constructions that those sections use are proved below. No cited result substitutes for a proof.

This adapted component is distributed under the [Design Science License](../../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt). The original volume 1 source package and volume 2 source package are retained with their notices. Fremlin's original copyright notices for §§123 and 242 are 1994 and 1997, respectively.

## 1. Measure and the nonnegative integral

We use the usual set-theoretic foundations, the complete ordered real field and the complex field. A measure space \((X,\Sigma,\mu)\) consists of a sigma-algebra and a countably additive map \(\mu:\Sigma\to[0,\infty]\) with \(\mu(\varnothing)=0\). In nonnegative sums and integrals, \(0\cdot\infty=0\). A null set is a measurable set of measure zero. “Almost everywhere” means outside a subset of a measurable null set.

<a id="ha-lca-pre-integral-lemma-1-1"></a>
### Lemma 1.1. Measure continuity, measurable operations and completion

Measures are monotone and countably subadditive. If \(E_n\uparrow E\), then \(\mu E_n\uparrow\mu E\). If \(E_n\downarrow E\) and \(\mu E_1<\infty\), then \(\mu E_n\downarrow\mu E\).

Finite sums, products, absolute values and continuous functions of finitely many measurable finite real or complex functions are measurable. Countable suprema, infima, limit superiors and limit inferiors of measurable extended real functions are measurable.

The ordinary completion of \(\mu\) is a complete measure. Every function measurable for that completion has an original-\(\Sigma\)-measurable representative equal almost everywhere.

**Proof.** If \(A\subseteq B\), countable additivity applied to \(B=A\sqcup(B\setminus A)\) gives monotonicity. Replacing a sequence \(A_n\) by the disjoint sets \(A_n\setminus\bigcup_{j<n}A_j\) proves subadditivity. For increasing \(E_n\), split the union into \(E_1,E_2\setminus E_1,\ldots\); its measure is the limit of the partial sums \(\mu E_n\). For decreasing sets, apply this result to \(E_1\setminus E_n\) and subtract from the finite number \(\mu E_1\).

An open subset of \(\mathbb R^m\) is a union of a countable family of boxes with rational endpoints: each point in the open set lies in such a box contained in it, and the collection of all rational boxes is countable. Thus a vector of finitely many measurable real functions is measurable into \(\mathbb R^m\). Inverse images under a continuous real-valued function are then measurable. This proves the assertions about sums, products and absolute values; complex functions are treated by their real and imaginary parts. Moreover,
\[
 \{\sup_n f_n>a\}=\bigcup_n\{f_n>a\}.
\]
Negation gives infima, and successive countable suprema and infima give limit superiors and inferiors. Piecewise definition on a measurable set preserves measurability.

Define the completed sigma-algebra to consist of sets \(E\) for which
\[
 E\mathbin{\triangle}B\subseteq N,\qquad B,N\in\Sigma,\quad\mu N=0,
\]
and assign \(E\) the measure \(\mu B\). If \(B'\) is another such representative, then \(B\triangle B'\) is null. Splitting each into the intersection and its null remainder shows \(\mu B=\mu B'\), even if both are infinite. Complements and countable unions preserve the displayed description. For pairwise disjoint completed sets \(E_n\) with representatives \(B_n\), all overlaps \(B_n\cap B_m\), \(n\ne m\), are null. The measurable sets
\[
 C_n=B_n\setminus\bigcup_{j<n}B_j
\]
are disjoint and differ from \(B_n\) by null sets. Their union represents \(\bigcup_n E_n\), so original countable additivity proves completed countable additivity. Every completed null set is contained in an original measurable null set, and every subset of that latter set is completed measurable. This proves completeness.

For a completed-measurable extended real \(f\), choose for each rational \(q\) an original measurable representative \(B_q\) of \(\{f>q\}\). All differences lie in one original null set \(N\). Put
\[
 f_0(x)=\sup\{q\in\mathbb Q:x\in B_q\},\qquad \sup\varnothing=-\infty.
\]
The identity \(\{f_0>a\}=\bigcup_{q>a}B_q\) proves measurability, and outside \(N\) the rational cuts show \(f_0=f\). If \(f\) is finite-valued, set \(f_0=0\) on \(N\); this gives an everywhere finite measurable representative. Apply the real construction separately to real and imaginary parts for a complex function. \(\square\)

For a nonnegative simple function \(s=\sum_{j=1}^m a_j1_{E_j}\), with disjoint measurable \(E_j\) and \(a_j\ge0\), define
\[
 \int s\,d\mu=\sum_{j=1}^m a_j\mu E_j.
\]
For nonnegative measurable \(f\), possibly infinite, define
\[
 \int f\,d\mu=\sup\left\{\int s\,d\mu:
          s\text{ nonnegative simple},\ 0\le s\le f\right\}.
\]

<a id="ha-lca-pre-integral-theorem-1-2"></a>
### Theorem 1.2. Construction and monotone convergence

The definition agrees with the simple integral and is monotone. If \(0\le f_n\uparrow f\), then
\[
 \int f\,d\mu=\lim_n\int f_n\,d\mu.
\]
Every nonnegative measurable function is an increasing limit of nonnegative simple functions.

**Proof.** Intersecting the finitely many cells in two simple representations, including their complements, gives a common finite partition. Finite additivity on that partition shows that the simple integral is independent of representation, additive, nonnegatively homogeneous and monotone. It follows directly that the supremum definition agrees with it and is monotone.

Let \(I=\sup_n\int f_n\,d\mu\). Monotonicity gives \(I\le\int f\,d\mu\). Fix a simple \(s\le f\) and \(0<c<1\). On \(\{s>0\}\), the increasing sets
\[
 E_n=\{f_n\ge cs\}
\]
eventually contain every point. On each positive cell of \(s\), Lemma 1.1 gives continuity from below. Consequently
\[
 I\ \ge\ \lim_n c\int s1_{E_n}\,d\mu
       \ =\ c\int s\,d\mu.
\]
If the last integral is infinite, this already says \(I=\infty\). Otherwise let \(c\uparrow1\). Taking the supremum over \(s\) yields the reverse inequality.

For an explicit simple approximation, let \(s_n(x)\) be the largest multiple of \(2^{-n}\) not exceeding \(\min(f(x),n)\). For \(f(x)=\infty\), take this minimum to be \(n\). Each \(s_n\) is measurable and takes finitely many values. Refining the grid and raising the cap show \(s_{n+1}\ge s_n\). The error tends to zero at every finite value, and \(s_n\to\infty\) at every infinite value. \(\square\)

<a id="ha-lca-pre-integral-corollary-1-3"></a>
### Corollary 1.3. Positive integral rules and Fatou's lemma

The nonnegative integral is additive and nonnegatively homogeneous. For nonnegative measurable \(f_n\),
\[
 \int\sum_n f_n\,d\mu=\sum_n\int f_n\,d\mu,\qquad
 \int\liminf_n f_n\,d\mu\le\liminf_n\int f_n\,d\mu.
\]
It is unchanged by almost-everywhere equality of measurable functions. A nonnegative function has integral zero exactly when it vanishes almost everywhere. A nonnegative function with finite integral is finite almost everywhere.

**Proof.** Increasing simple approximations to \(f\) and \(g\) have sums increasing to \(f+g\). Simple additivity and Theorem 1.2 prove additivity. Homogeneity follows from scaling the simple minorants, with the scalar-zero case immediate. Applying monotone convergence to the partial sums proves the series formula.

A nonnegative measurable function supported on a measurable null set has every simple minorant of integral zero, and hence has integral zero. Splitting a function into its parts on and off a common null set proves invariance under almost-everywhere equality. For \(f\ge0\),
\[
 \frac1m\mu\{f\ge1/m\}\le\int f\,d\mu.
\]
Thus zero integral implies that \(\{f>0\}=\bigcup_m\{f\ge1/m\}\) is null; the converse was just proved. If \(\int f=C<\infty\), the inequality \(m1_{\{f=\infty\}}\le f\) gives \(\mu\{f=\infty\}\le C/m\) for every positive integer \(m\), so that set is null.

Finally \(g_n=\inf_{k\ge n}f_k\) is measurable and increases to \(\liminf_k f_k\). Since \(g_n\le f_k\) for every \(k\ge n\), monotone convergence gives
\[
 \int\liminf_k f_k\,d\mu
 =\lim_n\int g_n\,d\mu
 \le\lim_n\inf_{k\ge n}\int f_k\,d\mu.
\]
All assertions with almost-everywhere hypotheses follow by removing the union of the countably many exceptional null sets and applying the everywhere statements. \(\square\)

## 2. Complex integration and \(L^1\)

<a id="ha-lca-pre-integral-lemma-2-1"></a>
### Lemma 2.1. The complex integral and its norm estimate

If \(f:X\to\mathbb C\) is measurable and \(\int|f|\,d\mu<\infty\), its integral is well-defined by the four nonnegative parts of its real and imaginary components. It is complex-linear and
\[
 \left|\int f\,d\mu\right|\le\int|f|\,d\mu.
\]
The equivalence classes of such functions under almost-everywhere equality form a normed complex vector space \(L^1(\mu)\), with \(\|f\|_1=\int|f|\,d\mu\). For bounded functions and finite positive measures, this integral agrees with the earlier finite-measure integral.

**Proof.** Each of \((\Re f)^+,(\Re f)^-,(\Im f)^+,(\Im f)^-\) is bounded by \(|f|\), and therefore has finite integral. For an integrable real function, the expression \(\int p-\int q\) is independent of its decomposition \(f=p-q\) into nonnegative integrable functions: if also \(f=p'-q'\), then \(p+q'=p'+q\), and Corollary 1.3 permits finite subtraction of the integrals. Decomposing sums and real scalar multiples in this way proves real linearity and order preservation. Define
\[
 \int f=\int\Re f+i\int\Im f.
\]
Real linearity and the identity \(if=-\Im f+i\Re f\) prove complex linearity.

If \(z=\int f\ne0\), take \(\alpha=\overline z/|z|\). Then
\[
 |z|=\Re\int\alpha f=\int\Re(\alpha f)
       \le\int|\alpha f|=\int|f|.
\]
The zero case is immediate. On a finite measure space, a bounded complex measurable function has uniform simple approximations, by finite grids for its real and imaginary parts. The bound just proved makes the integral error at most the uniform error times \(\mu X\). The integral therefore agrees with the uniform-simple-limit construction in [Lemma 2.2 of the finite-Radon reading](finite-radon-representation.md#ha-lca-pre-radon-lemma-2-2).

Pointwise scalar homogeneity and
\(|f+g|\le|f|+|g|\) give homogeneity and the triangle inequality for \(\|\cdot\|_1\). Corollary 1.3 shows that this quantity is unchanged by the equivalence relation and is zero only on its zero class. It also shows that addition, scalar multiplication and the integral are well-defined on classes. \(\square\)

<a id="ha-lca-pre-integral-theorem-2-2"></a>
### Theorem 2.2. Dominated convergence

Suppose \(f_n\) are measurable complex functions, \(f_n\to f\) almost everywhere, and \(|f_n|\le g\) almost everywhere for a nonnegative integrable \(g\). Then \(f\) has a measurable representative, belongs to \(L^1\), and
\[
 \|f_n-f\|_1\longrightarrow0,\qquad
 \int f_n\,d\mu\longrightarrow\int f\,d\mu.
\]

**Proof.** Remove one measurable null set containing all exceptions and \(\{g=\infty\}\), and set all functions to zero there. The limit is then measurable by Lemma 1.1, and \(|f|\le g\). The nonnegative functions
\[
 h_n=2g-|f_n-f|
\]
tend pointwise to \(2g\). Fatou's lemma and finite additivity of the integral give
\[
 2\int g\le\liminf_n\left(2\int g-\int|f_n-f|\right).
\]
Subtract the finite number \(2\int g\); the result is
\(\limsup_n\int|f_n-f|\le0\). The integral bound from Lemma 2.1 proves the second convergence. An originally specified limit on the exceptional set represents the same almost-everywhere class. \(\square\)

<a id="ha-lca-pre-integral-lemma-2-3"></a>
### Lemma 2.3. Simple density and finite-measure level sets

For \(f\in L^1(\mu)\), every set \(\{|f|\ge1/m\}\) has finite measure. The class \(f\) can be approximated in \(L^1\) by finite-valued simple functions supported on sets of finite measure. If \(f\ge0\), the approximants can be nonnegative. In particular, an \(L^1\) function is zero outside a sigma-finite measurable subset, irrespective of whether \(X\) itself is sigma-finite.

**Proof.** The integral inequality
\[
 \mu\{|f|\ge1/m\}\le m\|f\|_1
\]
follows by integrating \(1_{\{|f|\ge1/m\}}\le m|f|\). The increasing finite-measure sets
\[
 E_m=\{1/m\le|f|\le m\}
\]
exhaust the nonzero set of an everywhere finite representative. Theorem 2.2 gives \(f1_{E_m}\to f\) in \(L^1\). On a fixed \(E_m\), round the bounded real and imaginary parts to a finite grid fine enough that the complex pointwise error is at most \(\delta\). Extend the rounded function by zero off \(E_m\). Its \(L^1\) error is at most \(\delta\mu E_m\), which can be made arbitrarily small; if \(\mu E_m=0\), use zero. For nonnegative \(f\), use a grid in \([0,m]\). Finally the union of the finite-measure level sets \(\{|f|\ge1/m\}\) contains the whole nonzero set. \(\square\)

<a id="ha-lca-pre-integral-theorem-2-4"></a>
### Theorem 2.4. Absolute series and completeness of \(L^1\)

If \(\sum_n\|u_n\|_1<\infty\), the series \(\sum_nu_n\) converges absolutely almost everywhere and converges in \(L^1\) to that sum. Its integral is the sum of its integrals. The space \(L^1(\mu)\) is complete.

**Proof.** Choose measurable finite representatives. Corollary 1.3 gives
\[
 \int\sum_n|u_n|\,d\mu=\sum_n\|u_n\|_1<\infty.
\]
Hence the pointwise series is absolutely convergent outside a measurable null set. Define its sum to be zero on that exceptional set. Lemma 1.1 gives measurability, and the pointwise tail estimate and the series rule give
\[
 \left\|u-\sum_{n=1}^N u_n\right\|_1
       \le\sum_{n>N}\|u_n\|_1\longrightarrow0.
\]
The integral assertion follows from the bound in Lemma 2.1.

For a Cauchy sequence \(f_n\), choose a subsequence \(f_{n_k}\) with
\(\|f_{n_{k+1}}-f_{n_k}\|_1\le2^{-k}\). Apply the series result to
\(f_{n_1}\) and the consecutive differences. The resulting partial sums are \(f_{n_k}\), so this subsequence has a limit \(f\) in \(L^1\). Given \(\varepsilon>0\), first make \(\|f_n-f_{n_k}\|_1<\varepsilon/2\) for all sufficiently large \(n,n_k\) by the Cauchy property, and then choose such a \(k\) with \(\|f_{n_k}-f\|_1<\varepsilon/2\). The triangle inequality proves convergence of the whole sequence. \(\square\)

<a id="ha-lca-pre-integral-lemma-2-5"></a>
### Lemma 2.5. Change of variables for a measure-preserving map

Let \(T:(X,\Sigma,\mu)\to(Y,\mathcal T,\nu)\) be measurable and satisfy
\(\mu(T^{-1}E)=\nu(E)\) for every \(E\in\mathcal T\). For nonnegative measurable \(h\),
\[
 \int_X h(Tx)\,d\mu(x)=\int_Yh(y)\,d\nu(y).
\]
The same formula holds for integrable complex \(h\). Pullback is an isometry \(L^1(\nu)\to L^1(\mu)\). If \(T\) is a bijection whose inverse is also measurable and measure-preserving, the isometry is onto.

**Proof.** The hypothesis is precisely the formula for indicator functions. Finite sums prove it for nonnegative simple functions, and increasing simple approximations with Theorem 1.2 prove it for nonnegative functions. Apply that statement to the four nonnegative parts to obtain the complex formula. Applying it to \(|h|\) proves the norm identity; preimages of null sets are null, so the map is defined on equivalence classes. The inverse pullback gives surjectivity in the last assertion. \(\square\)

## 3. Topological density without global outer regularity

In this section \(X\) is locally compact Hausdorff, and \(\mu\) is a Borel measure finite on compact sets and inner regular on Borel sets of finite measure. We may also use its ordinary completion. No global outer-regularity or countability hypothesis is imposed.

<a id="ha-lca-pre-integral-theorem-3-1"></a>
### Theorem 3.1. Compactly supported continuous density and representatives

The space \(C_c(X)\) is dense in \(L^1(\mu)\). Nonnegative integrable functions can be approximated by nonnegative members of \(C_c(X)\). Every \(L^1\) class has a Borel representative that is zero outside a countable union of compact sets.

**Proof.** Lemma 1.1 replaces a completed-measurable function by a Borel representative. By Lemma 2.3, density reduces to approximating \(1_E\) for a Borel set \(E\) of finite measure. Fix \(\varepsilon>0\). Inner regularity supplies compact \(K\subseteq E\) with \(\mu(E\setminus K)<\varepsilon\). If \(K=\varnothing\), the zero function already has the required error.

Otherwise the [compact cutoff lemma](finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3) gives \(v\in C_c(X)\), \(0\le v\le1\), equal to one on \(K\). Put \(L=\operatorname{supp}v\) and \(V=\{v>1/2\}\). Then \(L\) is compact and \(K\subseteq V\subseteq L\). By [compact localization of the measure](finite-radon-products.md#ha-lca-pre-product-corollary-2-3), the finite Borel measure \(\mu_L(A)=\mu(A\cap L)\) is Radon. Its outer regularity supplies an open \(W\supseteq K\) with \(\mu_L(W\setminus K)<\varepsilon\). Thus \(U=W\cap V\) is open, contains \(K\), and satisfies
\[
 \mu(U\setminus K)=\mu_L(U\setminus K)<\varepsilon.
\]
A second compact cutoff gives \(u\in C_c(X)\), \(0\le u\le1\), equal to one on \(K\), with support contained in \(U\). Therefore
\[
 \|u-1_E\|_1\le\mu(E\setminus K)+\mu(U\setminus K)<2\varepsilon.
\]
Approximating the finitely many indicators in a simple function proves density. If the simple function is nonnegative, so is the resulting finite linear combination of cutoffs. Notice that outer regularity was used only for the finite restricted measure.

For the representative assertion, choose an everywhere finite Borel representative \(f\) and set \(E_m=\{|f|\ge1/m\}\). Each \(E_m\) has finite measure. For every \(m,k\ge1\), choose compact \(K_{m,k}\subseteq E_m\) with
\(\mu(E_m\setminus K_{m,k})<1/k\). The countable union
\(S=\bigcup_{m,k}K_{m,k}\) is Borel, and for fixed \(m\),
\(\mu(E_m\setminus S)\le1/k\) for every \(k\). Thus \(f=f1_S\) almost everywhere, and \(f1_S\) is the desired Borel representative. \(\square\)

## 4. Fubini on the full Borel sigma-algebra

Let \(X,Y\) be locally compact Hausdorff. We now extend the [finite Radon product construction](finite-radon-products.md#ha-lca-pre-product-theorem-2-1) to measurable integrands. The same results are treated in Fremlin, [§417, version of 9 March 2010](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt417.tex), 417H and 417P; its original volume 4 source package is retained. The proof below works with all Borel sets of \(X\times Y\), even when Borel rectangles do not generate that sigma-algebra.

<a id="ha-lca-pre-integral-lemma-4-1"></a>
### Lemma 4.1. The pi-lambda argument

A family \(\mathcal P\) of subsets of a set \(\Omega\) is a pi-system if it contains \(\Omega\) and is closed under finite intersections. A lambda-system contains \(\Omega\) and is closed under complements in \(\Omega\) and countable disjoint unions. Every lambda-system containing \(\mathcal P\) contains the sigma-algebra generated by \(\mathcal P\).

**Proof.** Intersections of lambda-systems are lambda-systems; let \(\mathcal D\) be the smallest one containing \(\mathcal P\). A lambda-system is closed under \(B\setminus C\) whenever \(C\subseteq B\) and both belong to it, since \(C\) and \(B^c\) are disjoint and \(B\setminus C=(C\cup B^c)^c\).

For \(A\in\mathcal P\), the family
\(\mathcal D_A=\{B\subseteq\Omega:A\cap B\in\mathcal D\}\)
is a lambda-system: it contains \(\Omega\) because \(A\in\mathcal D\), the complement rule follows by nested difference inside \(A\), and the disjoint-union rule follows by intersecting each member with \(A\). It contains \(\mathcal P\) by the intersection hypothesis, and thus contains \(\mathcal D\). Consequently \(A\cap B\in\mathcal D\) for \(A\in\mathcal P,B\in\mathcal D\).

Fix now \(B\in\mathcal D\). The same argument shows that
\(\{A\subseteq\Omega:A\cap B\in\mathcal D\}\)
is a lambda-system containing \(\mathcal P\), and hence contains \(\mathcal D\). Thus \(\mathcal D\) is closed under finite intersections. Complements give finite unions and differences. A countable union can be written as a disjoint union by subtracting preceding finite unions, so \(\mathcal D\) is a sigma-algebra. It therefore contains the sigma-algebra generated by \(\mathcal P\); any original lambda-system containing \(\mathcal P\) contains \(\mathcal D\). \(\square\)

<a id="ha-lca-pre-integral-theorem-4-2"></a>
### Theorem 4.2. Finite Radon Tonelli and Fubini

Let \(\mu,\nu\) be positive finite Radon measures on \(X,Y\), and let \(\lambda=\mu\otimes\nu\) be their finite Radon product. If \(h:X\times Y\to[0,\infty]\) is Borel measurable, both section-integral functions are Borel measurable and
\[
 \int h\,d\lambda
 =\int_X\left(\int_Yh(x,y)\,d\nu(y)\right)d\mu(x)
 =\int_Y\left(\int_Xh(x,y)\,d\mu(x)\right)d\nu(y).       \tag{4.1}
\]
The integrals may be infinite. If \(h\) is complex Borel measurable and \(\int|h|\,d\lambda<\infty\), almost every section in either direction is integrable; setting the corresponding section integral to zero on the exceptional null set gives an integrable measurable function, and (4.1) holds for these functions.

**Proof.** All sections of a Borel set or function are Borel because each coordinate inclusion is continuous. We first prove the positive assertion for an open set \(U\subseteq X\times Y\).

Put \(b(x)=\nu(U_x)\). This is lower semicontinuous. Indeed, if \(a<b(x_0)\), compact inner regularity gives compact \(K\subseteq U_{x_0}\) with \(\nu K>a\) when \(a\ge0\). Each \((x_0,y)\), \(y\in K\), has an open rectangle contained in \(U\). A finite subcover of \(K\), followed by intersection of its first-coordinate neighbourhoods, gives a neighbourhood \(N\) of \(x_0\) with \(N\times K\subseteq U\). Hence \(b(x)>a\) on \(N\). For \(a<0\) the assertion is immediate from nonnegativity. Thus \(b\) is Borel.

Let \(\mathcal F\) be the set of \(f\in C_c(X\times Y)\) with \(0\le f\le1_U\), and put \(g_f(x)=\int f(x,y)\,d\nu(y)\). The earlier product reading, Lemma 1.1, proves that \(g_f\in C_c(X)\). This family is upward directed: the function \(\max(f_1,f_2)\) lies in \(\mathcal F\) and its section integral dominates both. We claim that
\[
 b(x)=\sup_{f\in\mathcal F}g_f(x).                     \tag{4.2}
\]
The upper bound is immediate. For the lower bound, fix \(x\) and compact \(K\subseteq U_x\). The same finite rectangle argument gives open \(N\ni x,V\supseteq K\) with \(N\times V\subseteq U\). The earlier compact cutoff lemma supplies \(u\in C_c(X)\), \(v\in C_c(Y)\), valued in \([0,1]\), with \(u(x)=1\), \(\operatorname{supp}u\subseteq N\), \(v=1\) on \(K\), and \(\operatorname{supp}v\subseteq V\). Then \(f=u\otimes v\) is in \(\mathcal F\), and \(g_f(x)\ge\nu K\). Taking the supremum over \(K\) proves (4.2), including the case \(b(x)=0\).

By the already proved continuous-kernel identity,
\[
 \int g_f\,d\mu=\int f\,d\lambda\le\lambda U.
\]
We justify passage from the directed supremum in (4.2) without invoking an unproved convergence theorem for nets. Let \(s=\sum_{i=1}^m a_i1_{E_i}\le b\) be simple, with disjoint Borel cells and positive \(a_i\), and fix \(0<c<1\). Inner regularity supplies compact \(K_i\subseteq E_i\) with the weighted sum \(\sum_i a_i\mu(E_i\setminus K_i)\) arbitrarily small. At each point of \(K_i\), (4.2) supplies some \(g_f>ca_i\). These strict inequalities define open sets. Compactness, then directedness, supplies a single \(f\in\mathcal F\) for which \(g_f>ca_i\) throughout each \(K_i\). Therefore
\[
 \lambda U\ge\int g_f\,d\mu\ge c\sum_i a_i\mu K_i.
\]
Let the approximation error tend to zero, then \(c\uparrow1\), and take the supremum over simple \(s\le b\). This proves \(\int b\,d\mu\le\lambda U\). Conversely, every compact \(C\subseteq U\) has a cutoff \(f\in\mathcal F\) equal to one on \(C\). Thus
\(\lambda C\le\int f\,d\lambda=\int g_f\,d\mu\le\int b\,d\mu\).
Inner regularity of \(\lambda\) gives the reverse inequality. We have proved (4.1) for open-set indicators in the first order of integration.

Let \(\mathcal D\) be the family of Borel sets \(E\subseteq X\times Y\) for which \(x\mapsto\nu(E_x)\) is Borel and
\(\lambda E=\int\nu(E_x)\,d\mu(x)\). It contains the whole product. For complements, the section function is \(\nu(Y)-\nu(E_x)\); finiteness permits subtraction, and the known total mass \(\lambda(X\times Y)=\mu(X)\nu(Y)\) proves the identity. For a countable disjoint union, section measures add, and Corollary 1.3 proves measurability and the integral identity. Hence \(\mathcal D\) is a lambda-system. It contains all opens, a pi-system generating the full Borel sigma-algebra. Lemma 4.1 proves the assertion for every Borel indicator.

Nonnegative simple linear combinations and increasing simple approximations now give the first equality of (4.1), including measurability of the section integrals, by Theorem 1.2. Reversing the coordinates gives the second order.

For complex integrable \(h\), apply the nonnegative result to \(|h|\). The section norm is finite outside a measurable null set by Corollary 1.3. There the four-part definition of the complex integral applies. Integrate these four parts in the iterated identities; all their integrals are finite and bounded by \(\int|h|\,d\lambda\). Their signed complex sum proves (4.1) and the integral bound for the section-integral functions. \(\square\)

<a id="ha-lca-pre-integral-corollary-4-3"></a>
### Corollary 4.3. Completed products

In Theorem 4.2, a function measurable for the ordinary completion of \(\lambda\) has measurable sections for the ordinary completions of \(\nu\) and \(\mu\), respectively, outside a null set of the other variable. The nonnegative identity and the integrable complex identity still hold, with completed integrals and almost-everywhere defined section-integral functions. This assertion concerns almost every section, not every section.

**Proof.** Lemma 1.1 gives a Borel representative \(h_0\) equal to \(h\) off a subset of a Borel \(\lambda\)-null set \(N\). For nonnegative functions choose \(h_0\ge0\), changing its values on the null exception if necessary. Theorem 4.2 applied to \(1_N\) gives \(\nu(N_x)=0\) for \(\mu\)-almost every \(x\). For these \(x\), the sections \(h(x,\cdot)\) and \(h_0(x,\cdot)\) agree off a subset of a Borel \(\nu\)-null set. Completeness makes the first section measurable, and Corollary 1.3 makes its integral agree with that of the second. The exceptional \(x\)-set can be included in a measurable null set; assigning zero there gives a completed-measurable section-integral function with the same integral. Interchange \(X,Y\) for the other order. Theorem 4.2 applied to \(h_0\), and invariance under null changes, prove all the assertions. \(\square\)

<a id="ha-lca-pre-integral-theorem-4-4"></a>
### Theorem 4.4. The sigma-finite Radon extension

Suppose \(\mu,\nu\) are sigma-finite positive Borel measures, finite on compact sets and inner regular on Borel sets of finite measure. There is a Borel product measure \(\lambda\) on \(X\times Y\) for which (4.1) holds for every nonnegative Borel function and for every integrable complex Borel function. It is finite on compact sets and inner regular on finite-measure Borel sets. Its ordinary completion has the almost-everywhere section property of Corollary 4.3.

This theorem assumes sigma-finiteness of its two measures. It does not assert that an arbitrary Haar measure has that property.

**Proof.** Choose countable disjoint Borel partitions \(X=\bigsqcup_i A_i\) and \(Y=\bigsqcup_j B_j\) with \(\mu A_i,\nu B_j<\infty\). Such partitions come from disjointifying the finite-measure covers in the sigma-finiteness hypothesis. The finite Borel measures
\[
 \mu_i(E)=\mu(E\cap A_i),\qquad \nu_j(F)=\nu(F\cap B_j)
\]
are Radon. To see this, inner regularity of the original measure on \(E\cap A_i\) supplies compact subsets there that approximate \(\mu_i(E)\). The resulting inner regularity of \(\mu_i\) on every Borel set gives outer regularity by applying it to the complement and subtracting from the finite total mass. The same argument applies to \(\nu_j\).

Construct the finite Radon products \(\lambda_{ij}=\mu_i\otimes\nu_j\), and define
\[
 \lambda(E)=\sum_{i,j}\lambda_{ij}(E).
\]
Countable additivity follows by interchanging nonnegative series. For completeness, that interchange is valid because either iterated sum is the supremum of sums over finite subsets of the countable index product; every such subset is contained in a finite rectangle of indices. For any nonnegative Borel \(h\), the defining equality of measures gives
\(\int h\,d\lambda=\sum_{i,j}\int h\,d\lambda_{ij}\):
first check indicators and simple functions, then apply monotone convergence and the same nonnegative series rule.

Theorem 4.2 makes \(b_j(x)=\int h(x,y)\,d\nu_j(y)\) Borel. The sum \(b=\sum_jb_j\) is Borel and equals \(\int h(x,y)\,d\nu(y)\), by the disjoint partition and Corollary 1.3. Consequently
\[
 \int h\,d\lambda
 =\sum_{i,j}\int_X b_j\,d\mu_i
 =\sum_i\int_X b\,d\mu_i
 =\int_Xb\,d\mu.
\]
The same disjoint-partition argument proves the final equality, first for nonnegative simple functions and then by monotone convergence. Reversing the coordinates gives the other order. This formula for indicators also shows that the construction is independent of the chosen finite-measure partitions and uniquely determined by the nonnegative iterated identity. The four-part argument in Theorem 4.2 supplies complex Fubini. In particular,
\[
 \lambda(E\times F)=\mu(E)\nu(F)
\]
with the convention \(0\cdot\infty=0\).

For compact \(C\subseteq X\times Y\), its compact projections \(K,L\) have finite measure, so \(\lambda C\le\mu K\,\nu L<\infty\). Let now \(E\) be Borel with \(\lambda E<\infty\). Choose a finite set of index pairs with
\(\sum_{\text{other }i,j}\lambda_{ij}E<\varepsilon/2\). For each chosen pair use Radon regularity to choose compact \(K_{ij}\subseteq E\) so that the sum of their individual errors is less than \(\varepsilon/2\). Their finite union \(K\) is compact and lies in \(E\). Each chosen measure assigns \(E\setminus K\) no more than its own error, and the remaining measures contribute at most the omitted tail. Thus \(\lambda(E\setminus K)<\varepsilon\), proving the stated inner regularity.

Finally, the proof of Corollary 4.3 uses only the Borel nonnegative identity, Borel representatives and the fact that zero integral implies vanishing almost everywhere. These have all been proved here for the present measures, so the same proof applies to their ordinary completions. \(\square\)
