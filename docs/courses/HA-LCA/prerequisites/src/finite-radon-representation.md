# Finite Radon representation on locally compact spaces

This reading precedes the main lessons of this course. Self-checked by the writing AI.

We prove the finite-measure representation needed in Bochner's theorem on an arbitrary locally compact Hausdorff space. No countability assumption is made. This is the finite version: the statements about regularity below must not be applied without qualification to an infinite Haar measure.

The freely accessible sources are D. H. Fremlin, [*Measure Theory*, Volume 4, §§436I–436K](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt436.tex), for the representation theorem and its function spaces, and [§§4A2F–4A2G](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt4a2.tex), for compact separation and cutoffs. These files in the 2013 source collection are dated 9 May 2011 and 21 April 2013 respectively, both with copyright 2002. Some source statements refer elsewhere for their proofs; the arguments needed here are supplied below. We use an open-set construction for the finite measure, in place of the source's general smooth-functional construction.

Adaptation and additional proofs: GPT-6 Astra (OpenAI), Ultra, 4 October 2026. Fremlin's original source and its copyright notices are preserved in the source package. This combined reading is under the [Design Science License](../../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt), including its warranty disclaimer. The starting foundations are ordinary set theory with choice, the complete real and complex fields, and the definitions of topology, continuity and countable additivity; the auxiliary topological and measure-construction results used below are proved here.

## 1. Compact separation and continuous cutoffs

Recall that a space is **compact** if each open cover has a finite subcover. It is **Hausdorff** if distinct points have disjoint open neighbourhoods, and **locally compact** here means that each point has a compact neighbourhood. The support of a function is the closure of the set where it is nonzero.

<a id="ha-lca-pre-radon-lemma-1-1"></a>
**Lemma 1.1 (compact separation).** In a Hausdorff space, compact sets are closed and two disjoint compact sets have disjoint open neighbourhoods. In particular a compact Hausdorff space is normal: disjoint closed sets have disjoint open neighbourhoods.

**Proof.** If \(x\notin K\) and \(K\) is compact, separate \(x\) from each \(y\in K\) by open sets \(U_y,V_y\). Finitely many \(V_y\) cover \(K\). The intersection of their corresponding \(U_y\) is an open neighbourhood of \(x\) disjoint from \(K\). Thus the complement of \(K\) is open.

For disjoint compact sets \(A,B\), fix \(a\in A\). The same finite-cover construction gives disjoint open sets \(U_a,V_a\) with \(a\in U_a\) and \(B\subset V_a\). Choose finitely many \(U_a\) covering \(A\). Their union and the intersection of the corresponding \(V_a\) are the desired disjoint open sets. A closed subset of a compact space is compact: add its open complement to any cover and take a finite subcover. Applying the preceding construction proves the last assertion. \(\square\)

Consequently, in a compact Hausdorff space, if \(A\) is closed and \(O\) is open with \(A\subset O\), there is an open \(V\) with \(A\subset V\subset\overline V\subset O\). Indeed separate \(A\) and the closed set \(X\setminus O\); the closure of the neighbourhood of \(A\) misses the other neighbourhood.

<a id="ha-lca-pre-radon-lemma-1-2"></a>
**Lemma 1.2 (continuous separation).** In a compact Hausdorff space \(Y\), disjoint closed sets \(A,B\) can be separated by a continuous function \(u:Y\to[0,1]\) with \(u=0\) on \(A\) and \(u=1\) on \(B\).

**Proof.** Put \(U_1=Y\setminus B\) and choose an open \(U_0\) containing \(A\) whose closure lies in \(U_1\). Between any already chosen adjacent dyadic indices \(r<s\), the preceding shrinking property provides an open \(U_{(r+s)/2}\) with
\[
 \overline{U_r}\subset U_{(r+s)/2}
 \subset\overline{U_{(r+s)/2}}\subset U_s.
\]
Continuing over the dyadic levels gives \(\overline{U_r}\subset U_s\) whenever \(r<s\). Define
\[
 u(y)=\inf\bigl(\{r\in[0,1]:r\text{ dyadic and }y\in U_r\}\cup\{1\}\bigr).
\]
Then \(u=0\) on \(A\) and \(u=1\) on \(B\). For \(0<a\le1\),
\(\{u<a\}=\bigcup_{r<a}U_r\).
For \(0\le a<1\),
\(\{u>a\}=\bigcup_{r>a}(Y\setminus\overline{U_r})\),
where indices in both unions are dyadic. For the second equality, if \(u(y)>a\), choose \(a<r<s<u(y)\); membership in \(\overline{U_r}\subset U_s\) would contradict the definition of \(u\). The converse follows from the nesting. These sets are open, proving continuity, including the endpoint cases. \(\square\)

<a id="ha-lca-pre-radon-lemma-1-3"></a>
**Lemma 1.3 (compact cutoffs).** Let \(X\) be locally compact Hausdorff. For compact \(K\subset O\), with \(O\) open, there is an open \(W\) with compact closure such that
\(K\subset W\subset\overline W\subset O\).
There is also \(h\in C_c(X;\mathbb R)\) such that \(0\le h\le1\), \(h=1\) on \(K\), and \(\operatorname{supp}h\subset O\).

**Proof.** At \(x\in K\), choose a compact neighbourhood \(C\). In the compact Hausdorff space \(C\), shrink a relative neighbourhood of \(x\) so that its closure lies in \(O\cap\operatorname{int}_X C\). This relative neighbourhood is open in \(X\), since it lies in \(\operatorname{int}_X C\); its closure in \(X\) is the same compact closure in \(C\), because \(C\) is closed. Finitely many such neighbourhoods cover \(K\). Their union is \(W\); its closure is compact and lies in \(O\). Finite unions of compact sets are compact by taking finite subcovers on each member.

Put \(D=\overline W\). The compact subsets \(K\) and \(D\setminus\operatorname{int}_X D\) are disjoint. Lemma 1.2 supplies a continuous function on \(D\) that is one on \(K\) and zero on \(D\setminus\operatorname{int}_X D\). Extend it by zero to \(X\). The extension is continuous: its definitions agree on the overlap of the two closed sets \(D\) and \(X\setminus\operatorname{int}_X D\), and the inverse image of any closed set is a union of two closed sets. Its support is contained in the compact set \(D\subset O\). \(\square\)

<a id="ha-lca-pre-radon-lemma-1-4"></a>
**Lemma 1.4 (finite decomposition).** Suppose a compact set \(K\) is covered by open sets \(O_i\), and \(f\in C_c(X;\mathbb R)\) satisfies \(0\le f\le1\) and \(\operatorname{supp}f\subset K\). There are finitely many functions \(f_i\in C_c(X;\mathbb R)\), attached to finitely many of the distinct \(O_i\), such that
\[
 f=\sum_i f_i,\qquad 0\le f_i\le1,\qquad \operatorname{supp}f_i\subset O_i.
\]

**Proof.** For each \(x\in K\), first choose a compact neighbourhood of \(x\) inside some \(O_i\), and then a cutoff \(h_x\) that is one on that neighbourhood and has compact support in \(O_i\), using Lemma 1.3 twice. Select finitely many of the neighbourhoods covering \(K\), and add their cutoffs when they belong to the same \(O_i\). Denote the resulting nonnegative functions by \(h_i\), and put \(S=\sum_i h_i\). Then \(S\ge1\) on \(K\).

Set \(f_i=fh_i/S\) where \(S>0\), and set \(f_i=0\) where \(S=0\). These functions are continuous even at a point with \(S=0\): there \(f=0\), and \(|f_i|\le |f|\) controls the limit. Their supports lie in \(\operatorname{supp}f\cap\operatorname{supp}h_i\), which is compact and contained in \(O_i\). They add to \(f\) and satisfy the required bounds. \(\square\)

<a id="ha-lca-pre-radon-lemma-1-5"></a>
**Lemma 1.5 (the function spaces).** With the uniform norm, \(C_0(X;\mathbb C)\) is complete and \(C_c(X;\mathbb C)\) is dense in it. Every positive real-linear functional on \(C_0(X;\mathbb R)\) is bounded.

**Proof.** Here vanishing at infinity means that \(\{|f|\ge\varepsilon\}\) is compact for every \(\varepsilon>0\). The inequality
\(\{|f+g|\ge\varepsilon\}\subset\{|f|\ge\varepsilon/2\}\cup\{|g|\ge\varepsilon/2\}\)
and scalar rescaling show closure under linear combinations. Continuous absolute values, real and imaginary parts, and pointwise minima or maxima of real functions also vanish at infinity, since their level sets lie in the corresponding finite unions of compact level sets. Such functions are bounded: their absolute value is less than one off a compact set, and a continuous function on a compact set is bounded, as follows by a finite subcover of the inverse images of bounded intervals. A uniformly Cauchy sequence has a pointwise limit in the complete field \(\mathbb C\), and the Cauchy estimate proves uniform convergence. The limit is continuous by the triangle inequality. If \(\|f-f_n\|_\infty<\varepsilon/2\), its closed level set \(\{|f|\ge\varepsilon\}\) lies in the compact set \(\{|f_n|\ge\varepsilon/2\}\), so the limit vanishes at infinity. This proves completeness.

For real nonnegative \(f\in C_0\), the function \((f-\varepsilon)_+\) has support in \(\{f\ge\varepsilon\}\) and differs from \(f\) by at most \(\varepsilon\). Applying this to the positive and negative parts of the real and imaginary parts proves \(C_c\)-density.

For a positive real-linear functional \(I\), order gives \(|I(f)|\le I(|f|)\). If \(I\) were unbounded, for each positive integer \(n\) one could choose \(g_n\ge0\) with \(\|g_n\|_\infty\le2^{-n}\) and \(I(g_n)>n\). The uniformly convergent sum \(g=\sum_n g_n\) lies in \(C_0\), and \(g\ge g_n\). Positivity would give \(I(g)>n\) for every \(n\), impossible for a real-valued functional. \(\square\)

<a id="ha-lca-pre-radon-lemma-1-6"></a>
**Lemma 1.6 (finite compact-product estimates).** The product of two compact spaces is compact. If \(K\) is compact and \(H:K\times K\to\mathbb C\) is continuous, then, for every \(\varepsilon>0\), there is a finite Borel partition \(K=\coprod_i E_i\) with chosen points \(x_i\in E_i\) such that
\[
 |H(s,t)-H(x_i,x_j)|<\varepsilon
 \quad(s\in E_i,\ t\in E_j).
\]
If \(H:Z\times K\to\mathbb C\) is continuous and \(H(z_0,k)=0\) for all \(k\in K\), then \(\sup_{k\in K}|H(z,k)|\to0\) as \(z\to z_0\).

**Proof.** Refine an open cover of \(A\times B\) to open rectangles. For fixed \(a\in A\), finitely many second-coordinate sets cover the compact space \(B\). Intersect their first-coordinate neighbourhoods of \(a\). The resulting rectangle strip is covered by finitely many of the original cover members. Finitely many such first-coordinate neighbourhoods cover compact \(A\), proving product compactness.

For the partition assertion, continuity provides an open rectangle around each pair on which the oscillation of \(H\) is less than \(\varepsilon\); choose the initial deviations from the centre less than \(\varepsilon/2\). Product compactness gives finitely many such rectangles \(U_r\times V_r\). Partition \(K\) according to the finitely many membership decisions in all the sets \(U_r,V_r\), discarding empty pieces. These are Borel sets. If \((s,t)\) belongs to one of the rectangles, its chosen representatives \((x_i,x_j)\) belong to that same rectangle, since their membership decisions agree. The oscillation bound proves the assertion.

For the last assertion, continuity at each \((z_0,k)\) gives a rectangle on which \(|H|<\varepsilon\). Choose finitely many of the second-coordinate neighbourhoods covering \(K\), and intersect their first-coordinate neighbourhoods of \(z_0\). The bound then holds for every \(k\) simultaneously. In particular, applying this to \(H(a,x)=h(x+a)-h(x)\) proves uniform translation continuity of a continuous function \(h\) on a compact topological group. \(\square\)

## 2. Constructing a measure from its outer values

<a id="ha-lca-pre-radon-lemma-2-1"></a>
**Lemma 2.1 (finite outer-measure construction).** Let \(m^*\) be a nonnegative function on all subsets of a set \(X\), with \(m^*(\varnothing)=0\), monotonicity, countable subadditivity, and \(m^*(X)<\infty\). Call \(E\) measurable when
\[
 m^*(A)=m^*(A\cap E)+m^*(A\setminus E)\quad\text{for every }A\subset X. \tag{1}
\]
These measurable sets form a sigma-algebra, and the restriction of \(m^*\) to it is a finite countably additive measure.

**Proof.** Subadditivity always gives the inequality \(\le\) in (1). Complements preserve the definition. If \(E,F\) are measurable, split \(A\) first by \(E\) and then split each piece by \(F\). The resulting four nonnegative terms, together with subadditivity on their unions, give (1) for \(E\cap F\) and for \(E\cup F\). This also gives finite additivity on disjoint measurable sets.

For disjoint measurable \(E_n\), write \(E=\bigcup_n E_n\). Iterated splitting and monotonicity give, for every \(N\),
\[
 m^*(A)\ge\sum_{n=1}^N m^*(A\cap E_n)+m^*(A\setminus E).
\]
Take the supremum over \(N\). Subadditivity gives \(m^*(A\cap E)\le\sum_n m^*(A\cap E_n)\), so the preceding inequality implies the missing direction in (1). Thus \(E\) is measurable. Any countable union of measurable sets can be made disjoint by removing preceding members, proving closure under countable unions. Finally, take \(A=E\) in the displayed estimate and use subadditivity for the reverse inequality. This proves countable additivity. \(\square\)

For a finite measure, countable additivity implies continuity from below: write an increasing union as the disjoint union of its successive differences and take partial sums. Continuity from above follows by taking complements inside a set of finite measure. We will use these consequences only in this finite setting.

<a id="ha-lca-pre-radon-lemma-2-2"></a>
**Lemma 2.2 (bounded integration).** A finite positive measure \(\mu\) has a positive linear integral on bounded measurable complex functions, uniquely specified by
\(\int 1_E\,d\mu=\mu(E)\)
and continuity in the uniform norm. It satisfies
\[
 \left|\int g\,d\mu\right|\le\int |g|\,d\mu
 \le\mu(X)\|g\|_\infty. \tag{2}
\]

**Proof.** On a simple function \(s=\sum_{j=1}^n c_j1_{E_j}\) with disjoint measurable pieces, define the integral as \(\sum_j c_j\mu(E_j)\). Common refinements of partitions prove that this is well-defined and linear; the triangle inequality proves (2) there. Each bounded measurable function has uniform simple approximations, obtained by dividing a bounded interval or rectangle containing its values into increasingly small half-open cells. The estimate in (2) makes the simple integrals Cauchy and independent of the approximations. Their limit defines the integral, and the same estimates give linearity, positivity and (2). For the first inequality apply the simple-function inequality and also approximate \(|g|\) uniformly; the bound \(\bigl||z|-|w|\bigr|\le|z-w|\) justifies this passage. \(\square\)

The bounded monotone and dominated convergence statements also follow here without an additional theorem. If \(0\le g_n\uparrow g\le M\), then \(E_n=\{g-g_n>\varepsilon\}\) decreases to the empty set and
\(0\le\int(g-g_n)\le\varepsilon\mu(X)+M\mu(E_n)\to\varepsilon\mu(X)\).
Let \(\varepsilon\downarrow0\). If \(|g_n|,|g|\le M\) and \(g_n\to g\), use instead \(E_N=\bigcup_{n\ge N}\{|g_n-g|>\varepsilon\}\), which decreases to the empty set, and bound the error for \(n\ge N\) by \(\varepsilon\mu(X)+2M\mu(E_N)\).

## 3. Positive finite Radon representation

A **finite Radon measure** here means a finite positive Borel measure \(\mu\) satisfying
\[
 \mu(E)=\sup_{K\subset E,\ K\text{ compact}}\mu(K)
       =\inf_{E\subset U,\ U\text{ open}}\mu(U)
 \quad(E\text{ Borel}). \tag{3}
\]
Its completion can be taken by adjoining subsets of Borel null sets; the integrals of continuous functions are unchanged.

<a id="ha-lca-pre-radon-theorem-3-1"></a>
**Theorem 3.1 (positive finite representation).** On a locally compact Hausdorff space \(X\), every positive real-linear functional \(I:C_0(X;\mathbb R)\to\mathbb R\) is integration against a unique finite Radon measure \(\mu\), and
\[
 \mu(X)=\|I\|. \tag{4}
\]

**Proof.** By Lemma 1.5, \(M=\|I\|<\infty\). For open \(U\), define
\[
 m(U)=\sup\{I(f): f\in C_c(X;\mathbb R),\ 0\le f\le1,
                         \operatorname{supp}f\subset U\}.
\]
The zero function is allowed. Thus \(0\le m(U)\le M\), \(m(\varnothing)=0\), and \(m\) is monotone.

If open sets \(U_n\) cover an open \(U\), decompose an admissible \(f\) for \(U\) using Lemma 1.4 on its compact support. Then \(I(f)\le\sum_n m(U_n)\), hence \(m(U)\le\sum_n m(U_n)\). For disjoint open \(V,W\), sums of their admissible functions are admissible for \(V\cup W\), so \(m(V\cup W)\ge m(V)+m(W)\); the reverse inequality follows from the just-proved subadditivity.

For arbitrary \(A\subset X\), put
\[
 m^*(A)=\inf\{m(U):A\subset U,\ U\text{ open}\}.
\]
This is an outer measure. Indeed, choose open \(U_n\supset A_n\) with \(m(U_n)\le m^*(A_n)+\varepsilon2^{-n}\); subadditivity on their open union proves countable subadditivity of \(m^*\) after \(\varepsilon\downarrow0\). Its other defining properties are immediate, and \(m^*(U)=m(U)\) for open \(U\) by monotonicity. Moreover
\[
 m(U)=\sup_{K\subset U,\ K\text{ compact}}m^*(K). \tag{5}
\]
The inequality \(\ge\) is monotonicity. For the reverse, the support \(K\) of an admissible \(f\) lies in \(U\), and \(I(f)\le m(V)\) for every open \(V\supset K\). Therefore \(I(f)\le m^*(K)\). Take the supremum over \(f\).

We next prove every open \(U\) measurable for \(m^*\). Fix \(A\subset X\), open \(V\supset A\), and \(\varepsilon>0\). By (5), choose compact \(K\subset V\cap U\) with
\(m^*(K)>m(V\cap U)-\varepsilon\).
Lemma 1.3 supplies an open \(W\) with \(K\subset W\subset\overline W\subset V\cap U\). The open sets \(W\) and \(V\setminus\overline W\) are disjoint, so
\[
 \begin{aligned}
 m(V)&\ge m(W)+m(V\setminus\overline W)\\
 &\ge m^*(K)+m^*(A\setminus U)\\
 &\ge m^*(A\cap U)+m^*(A\setminus U)-\varepsilon.
 \end{aligned}
\]
Taking the infimum over \(V\), then letting \(\varepsilon\downarrow0\), gives the required splitting inequality. Lemma 2.1 now supplies a measure on a sigma-algebra containing the open sets; restrict it to the Borel sets and call it \(\mu\).

Outer regularity follows from the definition of \(m^*\), and (5) proves inner regularity on open sets, including \(X\). For any Borel \(E\), choose an open \(V\supset X\setminus E\) with \(\mu(V\setminus(X\setminus E))<\varepsilon\). Then the closed set \(F=X\setminus V\) lies in \(E\) with \(\mu(E\setminus F)<\varepsilon\). Choose compact \(C\subset X\) with \(\mu(X\setminus C)<\varepsilon\) using (5) for \(X\). The compact set \(F\cap C\subset E\) misses at most \(2\varepsilon\) of its measure. This proves (3). Finiteness is crucial in taking these complements.

It remains to prove the integral identity. Let \(f\in C_c\), \(f\ge0\). For \(\delta>0\), choose an integer \(n\) with \(n\delta\ge\|f\|_\infty\), and define
\[
 g_j=\min\bigl(1,\max(0,f/\delta-j+1)\bigr),\quad 1\le j\le n.
\]
These are in \(C_c\) and \(f=\delta\sum_{j=1}^n g_j\). Put \(a_j=\mu(\{f>j\delta\})\). Since \(g_j=1\) wherever \(f\ge j\delta\), each admissible cutoff for \(\{f>j\delta\}\) is at most \(g_j\); hence \(a_j\le I(g_j)\). For \(j\ge2\), the compact support of \(g_j\) lies in \(\{f>(j-2)\delta\}\), so \(I(g_j)\le a_{j-2}\), while \(I(g_1)\le M\). Consequently
\[
 \delta\sum_{j=1}^n a_j\le I(f)
 \le\delta M+\delta\sum_{j=0}^{n-2}a_j. \tag{6}
\]
The elementary step-function bounds on \(f\) give
\[
 \delta\sum_{j=1}^n a_j\le\int f\,d\mu
 \le\delta\sum_{j=0}^{n-1}a_j.
\]
For \(n=1\), (6) gives the error bound directly. For \(n\ge2\), subtract the displayed sums, using \(0\le a_j\le\mu(X)\le M\), to obtain
\(\int f\,d\mu-\delta M\le I(f)\le\int f\,d\mu+2\delta M\).
Letting \(\delta\downarrow0\) proves the identity for nonnegative \(C_c\). Decompose real functions into their positive and negative parts, then use Lemma 1.5 and the uniform bound (2) to extend to real \(C_0\).

The construction gives \(\mu(X)\le M\). The identity and (2) give \(M\le\mu(X)\), proving (4). Finally any finite Radon measure representing \(I\) must have, for open \(U\), exactly the value \(m(U)\): the upper bound follows by integration of cutoffs, and the lower bound follows from Lemma 1.3 and compact inner regularity. Outer regularity then determines its value on every Borel set. This proves uniqueness. \(\square\)

## 4. Complex measures and their exact norm

For a countably additive complex-valued Borel measure \(\sigma\), define
\[
 |\sigma|(E)=\sup\left\{\sum_{j=1}^n|\sigma(E_j)|:
          E=\coprod_{j=1}^n E_j,\ E_j\text{ Borel}\right\}. \tag{7}
\]
We use the term **finite complex Radon measure** when \(|\sigma|(X)<\infty\) and \(|\sigma|\) is a Radon measure. Its norm is \(\|\sigma\|=|\sigma|(X)\).

<a id="ha-lca-pre-radon-lemma-4-1"></a>
**Lemma 4.1 (variation).** If \(|\sigma|(X)<\infty\), (7) is a finite positive measure, \(|\sigma(E)|\le|\sigma|(E)\), and
\[
 \left|\int g\,d\sigma\right|\le\int|g|\,d|\sigma|
 \quad(g\text{ bounded Borel}). \tag{8}
\]
If \(\sigma\) is a finite linear combination of finite positive Radon measures, then it is a finite complex Radon measure.

**Proof.** For disjoint Borel \(E,F\), combining finite partitions chosen within any prescribed error of the two suprema gives \(|\sigma|(E\cup F)\ge|\sigma|(E)+|\sigma|(F)\). Refining each cell of a partition of \(E\cup F\) by its intersections with \(E,F\) gives the reverse inequality. This also proves monotonicity by writing a larger set as a set and its disjoint remainder. For disjoint \(E_n\) with union \(E\), finite additivity and monotonicity give \(|\sigma|(E)\ge\sum_n|\sigma|(E_n)\). Conversely, for a finite partition \(E=\coprod_j A_j\), countable additivity of \(\sigma\) and the triangle inequality give
\[
 \sum_j|\sigma(A_j)|
 \le\sum_n\sum_j|\sigma(A_j\cap E_n)|
 \le\sum_n|\sigma|(E_n).
\]
Taking the supremum over partitions proves the reverse inequality. Thus \(|\sigma|\) is a measure. The one-piece partition gives its bound on \(|\sigma(E)|\). For simple \(g\), the triangle inequality on its defining sum proves (8). Uniform simple approximation, as in Lemma 2.2, defines the bounded integral and proves (8) in general.

If \(\sigma=\sum_j c_j\mu_j\) for finite positive Radon \(\mu_j\), put \(\nu=\sum_j|c_j|\mu_j\). This finite positive measure is Radon: simultaneous compact inner approximations can be combined by finite union, and simultaneous open outer approximations by finite intersection. On every Borel set the resulting errors are bounded by the sum of the chosen errors. Every partition in (7) gives \(|\sigma|(E)\le\nu(E)\), so variation is finite. Given Borel \(E\), choose compact \(K\subset E\) and open \(U\supset E\) with \(\nu(U\setminus K)<\varepsilon\). Then
\( |\sigma|(E)-|\sigma|(K)\le\nu(E\setminus K)<\varepsilon\)
and
\( |\sigma|(U)-|\sigma|(E)\le\nu(U\setminus E)<\varepsilon\).
Thus \(|\sigma|\) is Radon. \(\square\)

<a id="ha-lca-pre-radon-lemma-4-2"></a>
**Lemma 4.2 (positive parts of a functional).** Every bounded real-linear functional \(A\) on \(C_0(X;\mathbb R)\) is a difference \(A=A_+-A_-\) of bounded positive functionals.

**Proof.** For \(f\ge0\) in \(C_0\), put
\[
 A_+(f)=\sup\{A(g):g\in C_0(X;\mathbb R),\ 0\le g\le f\}.
\]
It is nonnegative and at most \(\|A\|\|f\|_\infty\). Positive homogeneity follows by scaling. To prove additivity on the positive cone, if \(0\le g\le f+h\), write
\(g=g_1+g_2\), where \(g_1=\min(g,f)\) and \(g_2=g-g_1\). These continuous functions vanish at infinity, with \(0\le g_1\le f\) and \(0\le g_2\le h\). Therefore \(A_+(f+h)\le A_+(f)+A_+(h)\). In the other direction, choose admissible functions for \(f\) and \(h\) with values within \(\varepsilon\) of their suprema, and add them. Let \(\varepsilon\downarrow0\) to obtain equality.

Extend to real functions by differences of nonnegative functions. This is independent of the difference decomposition: if \(f_1-f_2=h_1-h_2\), then \(f_1+h_2=h_1+f_2\), and cone additivity gives the same difference of values. It also proves linearity. Positivity and
\(|A_+(f)|\le A_+(|f|)\le\|A\|\|f\|_\infty\)
show boundedness. Finally \(A_-=A_+-A\) is positive, since the choice \(g=f\) is admissible for \(f\ge0\), and is bounded as a difference of bounded functionals. \(\square\)

<a id="ha-lca-pre-radon-theorem-4-3"></a>
**Theorem 4.3 (complex finite representation).** Integration is an isometric bijection
\[
 M(X)\longrightarrow C_0(X;\mathbb C)^*,\qquad
 \sigma\longmapsto\left(g\longmapsto\int g\,d\sigma\right), \tag{9}
\]
where \(M(X)\) is the space of finite complex Radon measures. In particular this measure space is complete in total variation.

**Proof.** First let \(\Lambda\) be a bounded complex-linear functional. On real functions define \(A(f)=\operatorname{Re}\Lambda(f)\) and \(B(f)=\operatorname{Im}\Lambda(f)\). Lemma 4.2 expresses each as a difference of bounded positive functionals. Theorem 3.1 represents these four positive functionals by finite positive Radon measures. Their combination
\(\sigma=\mu_{A,+}-\mu_{A,-}+i\mu_{B,+}-i\mu_{B,-}\)
is a finite complex Radon measure by Lemma 4.1. It represents \(\Lambda\) on real functions and hence, by complex linearity, on all \(C_0(X;\mathbb C)\).

For any finite complex Radon \(\sigma\), (8) gives a functional \(\Lambda_\sigma\) with norm at most \(|\sigma|(X)\). To prove equality, fix a finite Borel partition \(X=\coprod_{j=1}^n E_j\). Choose \(|z_j|=1\) so that \(z_j\sigma(E_j)=|\sigma(E_j)|\). Inner regularity gives compact \(K_j\subset E_j\) whose union misses less than \(\varepsilon\) of \(|\sigma|\).

The disjoint compact sets \(K_j\) have pairwise disjoint open neighbourhoods \(U_j\). To see this, separate each pair by Lemma 1.1 and for each fixed \(j\) intersect its finitely many chosen neighbourhoods. Lemma 1.3 then gives \(h_j\in C_c\), \(0\le h_j\le1\), equal to one on \(K_j\), supported in \(U_j\). Empty compact sets may be assigned the zero cutoff. The function \(g=\sum_j z_jh_j\) belongs to \(C_c\) and satisfies \(|g|\le1\), because the supports are disjoint. It agrees on \(\bigcup_j K_j\) with the simple function \(s=\sum_j z_j1_{E_j}\). Thus (8) gives
\[
 \left|\int g\,d\sigma-\sum_j|\sigma(E_j)|\right|
 =\left|\int(g-s)\,d\sigma\right|<2\varepsilon.
\]
It follows that \(\|\Lambda_\sigma\|\ge\sum_j|\sigma(E_j)|-2\varepsilon\). Take the supremum over partitions, then let \(\varepsilon\downarrow0\), proving equality of norms. In particular a measure giving the zero functional has zero variation and is zero. This proves uniqueness and injectivity in (9).

For completeness, sums of finite complex Radon measures are still such measures: the triangle inequality for every partition gives \(|\sigma+\tau|\le|\sigma|+|\tau|\), and the regularity argument at the end of Lemma 4.1 applies with this dominating finite Radon measure. Homogeneity and the triangle inequality for the norm follow in the same way. The dual of a normed space is complete: a norm-Cauchy sequence \(\Lambda_n\) has scalar limits \(\Lambda(f)=\lim_n\Lambda_n(f)\); these give a bounded linear functional, and the uniform Cauchy estimate on the unit ball gives \(\|\Lambda_n-\Lambda\|\to0\). Apply this to (9) to obtain completeness of \(M(X)\). \(\square\)

<a id="ha-lca-pre-radon-proposition-4-4"></a>
**Proposition 4.4 (Jordan decomposition).** A finite real signed Radon measure \(\sigma\) has unique mutually singular positive Radon measures \(\sigma^+,\sigma^-\) such that
\[
 \sigma=\sigma^+-\sigma^-,\qquad
 |\sigma|=\sigma^++\sigma^-,\qquad
 \sigma^\pm=\tfrac12(|\sigma|\pm\sigma). \tag{10}
\]
Every finite complex Radon measure is a linear combination \(\mu_1-\mu_2+i\mu_3-i\mu_4\) of four finite positive Radon measures.

**Proof.** The expressions in (10) are countably additive and nonnegative because \(|\sigma(E)|\le|\sigma|(E)\). They are at most \(|\sigma|\) and hence Radon by the same compact and open approximations as in Lemma 4.1.

Choose finite Borel partitions for which the sums in (7) approach \(|\sigma|(X)\), with error less than \(2^{1-n}\). Let \(P_n\) be the union of the cells on which \(\sigma\) is nonnegative, and \(N_n=X\setminus P_n\). Then
\[
 \sigma^+(N_n)+\sigma^-(P_n)
 =\tfrac12\left(|\sigma|(X)-\sum_j|\sigma(E_{n,j})|\right)<2^{-n}.
\]
Put \(P=\liminf_n P_n\). For each \(N\), the limsup of the \(P_n\) is contained in \(\bigcup_{n\ge N}P_n\), whose \(\sigma^-\)-measure is at most \(\sum_{n\ge N}2^{-n}\). Hence \(\sigma^-(P)=0\). Also \(X\setminus P=\limsup_n N_n\), and the same estimate gives \(\sigma^+(X\setminus P)=0\). This proves mutual singularity and the asserted decomposition.

For uniqueness, any positive decomposition \(\sigma=\alpha-\beta\) concentrated on complementary measurable sets has variation \(\alpha+\beta\): domination gives the upper bound, while partitioning a Borel set by the two concentration sets gives the lower bound in (7). Solving the sum and difference equations forces (10). Finally the real and imaginary parts of a complex measure have variation bounded by \(|\sigma|\), since \(|\operatorname{Re}z|,|\operatorname{Im}z|\le|z|\). They are finite signed Radon measures, and applying (10) to each gives the four-measure decomposition. \(\square\)

<a id="ha-lca-pre-radon-corollary-4-5"></a>
**Corollary 4.5 (compact tails and completion).** For each finite complex Radon measure \(\sigma\) and \(\varepsilon>0\), a compact \(K\) satisfies \(|\sigma|(X\setminus K)<\varepsilon\). The measure has a completion on all sets differing from a Borel set by a subset of a Borel \(|\sigma|\)-null set. Its bounded continuous integrals are unchanged.

**Proof.** Compact tails are (3) for \(|\sigma|\) and \(E=X\). For completion, define the extended value of \(E\) to be \(\sigma(B)\) whenever \(E\mathbin\triangle B\subset Z\), with \(B,Z\) Borel and \(|\sigma|(Z)=0\). Two such choices differ by a subset of a Borel null union; their Borel difference has zero variation, so their values agree. Complements and countable unions preserve this description, using the union of the null exceptional sets. For disjoint extended-measurable sets, the chosen Borel representatives overlap only inside such a null union. Remove those overlaps successively to obtain disjoint Borel representatives with the same values; countable additivity follows from that of \(\sigma\). Bounded continuous functions were Borel measurable already, so their simple approximations and integrals are unchanged. \(\square\)

This reading has supplied the finite positive and complex representation theorems, their exact norm, Jordan decomposition, compact tails, and the cutoff arguments used in their proofs. Products of Radon measures, sigma-finite integration, and the construction of Haar measure are separate prerequisites; they are not inferred from the finite representation theorem proved here.
