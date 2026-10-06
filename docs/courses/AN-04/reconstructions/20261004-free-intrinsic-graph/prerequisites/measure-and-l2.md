# Measure and the complete square-integrable space

This companion retains the used measure arguments of AN03-P004, *Banach
estimates, quotient spaces and compact parameter arguments*. Its original
labels LM1–LM6, GM2–GM3, GM6 and LP3–LP4, LP10–LP11 are retained. The norm,
completeness and density assertions are selected only at \(p=1,2\).
Young's inequality, weak derivatives and the rest of AN-03 are not required
by this selection. The full original AN-03 scope remains unchanged.

The scalar and compact-calculus proofs are the earlier
AN04-U001 prerequisite chain,
with its [explicit real-field axioms and notation](../../20261004-free-stationary-phase/provider-context.md).
In particular, real completeness, the Archimedean property,
finite-dimensional continuity, complex arithmetic and absolute
series are supplied there. The rational density and enumeration steps are
written in M0 below. The smooth taper used in LP11 is proved in
[U001, Appendix A.4](../../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md#a-4-finite-smooth-cutoffs).
The selection below supplies measure construction and convergence, rather
than taking those theorems as axioms.

This is a separate modified selection from the earlier AN-03 programme, under
GNU FDL 1.2 only. Original principal author and publisher: AN-03 course-writing
task / AN-03 local course project. Copyright © 2026 AN-03 course project
contributors. Earlier modification: AN-03 course-writing task and OpenAI Codex.
Selection and the explicitly identified connecting arguments: GPT-6 Astra
(OpenAI), Ultra, 4 October 2026.

Permission is granted to copy, distribute and modify this component under the
GNU Free Documentation License, Version 1.2 only, with no Invariant Sections,
no Front-Cover Texts and no Back-Cover Texts. The [licence](notices/COPYING),
[title information](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and
[rights notice](notices/RIGHTS.md) accompany it.

## M0. The declared choice input

The course chooses Zorn's maximality principle as an explicit logical axiom. Here is the exact selection map needed in the original complete-metric Baire argument. For any set-indexed family of nonempty sets \((A_i)_{i\in I}\), consider partial functions \(c\) with domain a subset of \(I\) and \(c(i)\in A_i\), ordered by extension. The empty function belongs to the poset. Every chain has an upper bound: its union is a function, since any two partial functions in the chain agree wherever both are defined, and every union value remains in its specified \(A_i\). Zorn gives a maximal partial function. If its domain omits \(i\), choose one element of that nonempty \(A_i\); adjoining that one pair extends the function, a contradiction. Consequently
\[
 c:I\longrightarrow\bigcup_{i\in I}A_i,\qquad c(i)\in A_i
                     \text{ for every }i\in I.
 \tag{BZ1}
\]
This proves the required choice consequence from the chosen axiom, without adding an unannounced sequence-selection hypothesis.

Here the selector is used only for the countable nonempty families of
near-minimal covers and of approximation choices. Subsequences of a given
Cauchy sequence can instead use the least natural index satisfying the
required tail bound. This selection makes no use of the Baire theorem.

For clarity, the elementary countability used in M2–M3 can be explicit.
Enumerate pairs \((m,k)\in\mathbb Z\times\mathbb N_{>0}\) in increasing
\(|m|+k\), with any fixed finite ordering at each level. The resulting
sequence \(m/k\) includes every rational; repetitions do not matter.
Finite tuples are enumerated by the sum of their positive indices.
Thus rational coordinate boxes form a countable family. For \(a<b\),
the Archimedean property supplies a positive integer \(N\) with
\(N(b-a)>1\). Choose the least integer \(j>Na\); it exists by bounding
\(Na\) between two integers and searching the finite integer interval.
Then \(Na<j\le Na+1<Nb\), so \(j/N\in(a,b)\).
This proves the density used to select rational endpoints on both sides
of each coordinate. These are finite integer operations and natural
enumerations, not additional measure assumptions.

## M1. The generating-class lemma

The following is the independent argument from AN03-P004, Section 16.2.
A Dynkin class on a set \(Z\) contains \(Z\), is closed under relative complements, and is closed under countable disjoint unions. It is closed under differences of nested members: if \(A\subset B\) belong, complement the disjoint union \(A\cup(Z\setminus B)\). Let \(\mathcal P\) be an intersection-closed family containing \(Z\), and let \(\mathcal L\) be the intersection of all Dynkin classes containing \(\mathcal P\). This intersection is itself a Dynkin class. For \(A\in\mathcal P\), the sets \(B\subset Z\) with \(A\cap B\in\mathcal L\) form a Dynkin class. The whole-set condition uses \(A\in\mathcal L\); the complement condition uses the proved nested-difference rule inside \(A\); disjoint unions use intersections with their disjoint parts. Intersection closure of \(\mathcal P\) makes this class contain \(\mathcal P\), so it contains \(\mathcal L\). Fix now \(B\in\mathcal L\) and make the same argument with the class of \(A\) satisfying \(A\cap B\in\mathcal L\). The first argument shows that every \(A\in\mathcal P\) belongs, and hence every \(A\in\mathcal L\) belongs. Thus \(\mathcal L\) is closed under all finite intersections. Complementation gives finite unions, and disjointifying a countable union by subtracting its preceding finite union gives every countable union. It follows that
\[
 \mathcal P\subset\mathcal D,\quad\mathcal D\ {\rm a\ Dynkin\ class}
 \quad\Longrightarrow\quad \sigma(\mathcal P)\subset\mathcal D .
 \tag{GM6}
\]
This implication has just been proved, rather than assumed as a convergence or product theorem.

## M2. Completed Lebesgue measure

We now construct the measure input used in Section 15.1. Fix the original coordinates on \(\mathbb R^n\), \(n\geq1\). The covering boxes are bounded half-open coordinate boxes \(B=\prod_{i=1}^n(a_i,b_i]\), \(a_i<b_i\), with original geometric volume \(v(B)=\prod_{i=1}^n(b_i-a_i)\). The empty box has volume zero. For every subset \(E\subset\mathbb R^n\), put
\[
 \mu^*(E)=\inf\left\{\sum_{j=1}^\infty
           \prod_{i=1}^n(b_{ji}-a_{ji}):
       E\subset\bigcup_{j=1}^\infty
                  \prod_{i=1}^n(a_{ji},b_{ji}]\right\}.
                                                               \tag{LM1}
\]
Finite covers are allowed by appending empty boxes. The empty cover gives \(\mu^*(\varnothing)=0\). Every set has a cover, since a countable collection of bounded coordinate boxes covers the whole original space. Enlarging a set only reduces the choices of covers, so \(\mu^*\) is monotone. For a countable collection \(E_k\), if \(\sum_k\mu^*(E_k)\) is finite, choose a cover of \(E_k\) with cost below \(\mu^*(E_k)+\varepsilon2^{-k}\), for \(k\geq1\). Concatenating these original covers proves \(\mu^*(\bigcup_kE_k)\leq\sum_k\mu^*(E_k)+\varepsilon\). Let \(\varepsilon\downarrow0\). If that sum is infinite, the inequality already holds. Thus
\[
        \mu^*\left(\bigcup_k E_k\right)
                         \leq\sum_k\mu^*(E_k).                 \tag{LM2}
\]
This proof uses only countable sums of nonnegative real numbers, not an integral or a convergence theorem for one.

The box volume in (LM1) is exact. One box covering itself gives \(\mu^*(B)\leq v(B)\). To prove the reverse inequality, take any countable box cover. If its cost is infinite there is nothing to show. Otherwise enlarge each covering box to an open box with added geometric volume less than \(\varepsilon2^{-j}\). This is possible by continuity of its full finite product in its endpoints. For \(0<\delta<\frac12\min_i(b_i-a_i)\), the closed coordinate box \(C_\delta=\prod_i[a_i+\delta,b_i-\delta]\) lies in the original \(B\) and has a finite subcover by these enlarged open boxes. The finite-subcover fact has a direct proof here. If a closed box had no finite subcover by an open cover, bisect all its original coordinate intervals. At least one of its \(2^n\) closed subboxes still has no finite subcover, because otherwise the union of the finite subcovers would cover the original box. Repeat inside that chosen subbox. Real completeness gives a point in all the resulting nested boxes: each coordinate's increasing lower and decreasing upper endpoints have the same limit, since their difference is its original side length times \(2^{-k}\). The diameter at step \(k\) is the full \((\sum_i 2^{-2k}(b_i-a_i-2\delta)^2)^{1/2}\), which tends to zero. One covering open set contains the limiting point and a small ball about it. Eventually the entire chosen box lies in that one set, contradicting its lack of a finite subcover. This proves exactly the compactness needed for \(C_\delta\).

For a finite family of open boxes covering \(C_\delta\), include every covering endpoint and every endpoint of \(C_\delta\) in a finite coordinate grid, inside a bounded box containing them all. The product distributive law writes the full volume of each box as the sum of the grid-cell products contained in it. On the interior of each grid cell, membership in a covering open box is constant, because all its boundary coordinates are grid endpoints. Every grid cell inside \(C_\delta\) is therefore contained, in its interior, in at least one covering box. Summing the full products, with their actual multiplicities, gives
\[
 \prod_{i=1}^n(b_i-a_i-2\delta)
       \leq\sum_{j\ {\rm in\ the\ finite\ subcover}}
                         v(B_j^{\rm enlarged})
       \leq\sum_{j=1}^\infty v(B_j)+\varepsilon .              \tag{LM3}
\]
Grid faces have a zero side length in this geometric calculation; no assertion about an already constructed measure is being used. First let \(\varepsilon\downarrow0\), then \(\delta\downarrow0\). Every covering cost is at least the original full \(v(B)\). Taking its infimum proves \(\mu^*(B)=\prod_i(b_i-a_i)\).

Define the measurable sets by the exact splitting condition
\[
 \mathcal M=\left\{A:\ 
   \mu^*(E)=\mu^*(E\cap A)+\mu^*(E\setminus A)
                        \quad\hbox{for every subset }E\right\}.
                                                               \tag{LM4}
\]
The reverse inequality to this equality always holds by (LM2), so only its other direction needs proof. Complements preserve (LM4). If \(A,B\in\mathcal M\), split first at \(A\) and then split both pieces at \(B\). The resulting four original pieces have sum of outer measures \(\mu^*(E)\). The three pieces outside \(A\cap B\) cover its complement in \(E\); (LM2) therefore proves the required inequality for \(A\cap B\). Thus finite intersections and finite unions preserve measurability.

For disjoint measurable \(A_k\), repeated finite splitting gives, for every positive integer \(N\),
\[
 \mu^*(E)\geq\sum_{k=1}^N\mu^*(E\cap A_k)
                  +\mu^*\left(E\setminus\bigcup_{k=1}^\infty A_k\right).
                                                               \tag{LM5}
\]
Let \(N\to\infty\). The full sum bounds \(\mu^*(E\cap\bigcup_k A_k)\) from below by (LM2), proving (LM4) for their union. For an arbitrary countable union of measurable sets, replace its \(k\)-th set by its difference from the preceding finite union; finite intersections and complements have already proved these disjoint differences measurable. Their union is the original union, so \(\mathcal M\) is a sigma-algebra. Taking \(E=\bigcup_k A_k\) in (LM5) and using (LM2) proves countable additivity of \(\mu=\mu^*|_{\mathcal M}\). No subtraction of two infinite numbers occurs.

Every covering box \(Q\) is in \(\mathcal M\). Indeed, subdivide any covering box \(B_j\) at all coordinate endpoints of \(Q\). The half-open grid pieces partition \(B_j\) exactly. Each is either inside \(Q\) or outside it, and the sum of their full volume products is \(v(B_j)\), by the distributive law. The inside pieces cover \(E\cap Q\), and the outside pieces cover \(E\setminus Q\), for any original cover of \(E\). Thus each covering cost is at least \(\mu^*(E\cap Q)+\mu^*(E\setminus Q)\). Taking its infimum proves (LM4). These boxes generate the Borel sigma-algebra: every open set is a countable union of coordinate boxes with rational endpoints whose closures are contained in it, since each of its points has an interior ball and rational endpoints can be chosen on both sides of each original coordinate. Hence every Borel set is measurable, with the exact box volumes proved in (LM3).

Every subset of an outer-measure-zero set is also measurable. For such a subset \(S\), \(\mu^*(E\cap S)=0\), and (LM2) and monotonicity give \(\mu^*(E)=\mu^*(E\setminus S)\). This is (LM4), with its first term zero. Therefore \(\mu\) is complete. A coordinate hyperplane has outer measure zero: its bounded part with other coordinates in \([-R,R]\) is covered by one box of thickness \(2\delta\) in its fixed coordinate and side lengths \(2R+2\delta\) in the others. Its full cost is
\[
                  (2\delta)(2R+2\delta)^{n-1}\longrightarrow0.
                                                               \tag{LM6}
\]
The whole hyperplane is a countable union of these bounded parts, so (LM2) applies. Consequently every open, closed or half-open choice of endpoints on a bounded coordinate box differs only by a measurable null subset of its faces and retains the full original volume.

The completion is exactly the completed Borel measure, rather than a larger unexplained collection. If \(E\in\mathcal M\) has finite measure, choose covers with costs tending to \(\mu(E)\), enlarge their boxes to open boxes with additional total cost tending to zero, and denote their open unions by \(O_k\supset E\). Additivity gives \(\mu(O_k\setminus E)\to0\). Thus \(G=\bigcap_kO_k\) is Borel, contains \(E\), and \(\mu(G\setminus E)=0\). Every measurable null set \(H\) has a Borel null superset: make the same open-cover construction with total cost below \(2^{-k}\), and intersect the resulting open sets. Apply this to \(H=G\setminus E\). It follows that \(E\) differs from a Borel set by a subset of a Borel null set. For infinite \(\mu(E)\), apply the finite construction to \(E\cap Q_k\), where bounded coordinate boxes \(Q_k\) increase to the whole original space. Each has finite measure by (LM3). The countable union of the resulting Borel supersets is a Borel superset of \(E\), and its difference from \(E\) lies in the countable union of the Borel null supersets just constructed. This again has measure zero. Conversely, completeness has already shown that every Borel set changed on a subset of a Borel null set belongs to \(\mathcal M\).

Finally, this construction is the unique completed Borel measure with the stated coordinate-box volumes. On a bounded coordinate box \(Q\), suppose two finite Borel measures have these volumes. The sets on which they agree form a Dynkin class: agreement holds on \(Q\), relative complements subtract from its finite original volume, and disjoint countable unions use countable additivity. The coordinate rectangles form an intersection-closed generating class. The independent Dynkin-class argument in Section M1 above, which uses only these set operations, makes agreement extend to all Borel subsets of \(Q\). Exhausting by bounded \(Q_k\) and writing their increasing union as successive disjoint differences proves agreement on all Borel sets. Both completions contain exactly the same Borel null sets and all their subsets, as proved above; their completed measures therefore agree as well. Thus (LM1)–(LM6) construct precisely the countably additive completed Lebesgue measure used in (LP1)–(LP19), with its actual original coordinates, full products, face contributions and outer-measure covers.

## M3. Measurability and the integral

For an extended real function, measurability means that all inverse images of open rays are measurable. It is enough to check rational endpoints: an arbitrary open ray is a countable union of the appropriate rational rays. Countable suprema and infima are measurable, since
\[
 \{\sup_n f_n>t\}=\bigcup_n\{f_n>t\},\qquad
 \{\inf_n f_n<t\}=\bigcup_n\{f_n<t\},\qquad
 \liminf_n f_n=\sup_N\inf_{n\geq N}f_n .
 \tag{GM2}
\]
To obtain the other ray for a given extended real function, use the complement of a non-strict ray, itself a countable intersection of strict rays. Consequently a pointwise limit of measurable real functions, including an infinite limit, is measurable. For complex functions apply the assertion to both real coordinates; the Borel sets of the complex plane are generated by the rational-coordinate rectangles. Finite sums of measurable real functions and products wherever their extended values are defined are measurable: their pair map has measurable inverse images of rational rectangles and hence of every open set, and finite real addition and multiplication are continuous. This gives in particular every finite-valued simple function and its level sets. Nonnegative sums with infinite limits follow by increasing finite sums and (GM2).

For a nonnegative finite-valued simple function \(s=\sum_{j=1}^r c_j1_{A_j}\), with disjoint measurable \(A_j\) and finite \(c_j\geq0\), define its integral to be \(\sum_j c_j\mu(A_j)\). The convention \(0\cdot\infty=0\) records the fact that a zero value contributes zero, even on a set of infinite measure. Two presentations give the same answer: intersect their finite partitions, including the zero-valued complement, and use finite additivity on each original part. On this common partition \(s\leq t\) gives \(\int s\leq\int t\); sums and finite positive scalar multiples have their exact additive integral. For a nonnegative measurable \(f\), define
\[
 \int_X f\,d\mu
 =\sup_{\substack{s\ {\rm nonnegative,\ finite\ valued,\ simple}\\s\leq f}}
       \int_Xs\,d\mu,\qquad
 s_n(x)=
 \begin{cases}
  \min(2^n,\,2^{-n}\lfloor2^n f(x)\rfloor),&f(x)<\infty,\\
  2^n,&f(x)=\infty .
 \end{cases}
 \tag{GM3}
\]
Each \(s_n\) has finitely many measurable levels. The next dyadic grid retains every earlier grid value and its truncation is higher, so \(s_n\uparrow f\). This is an approximation to the original \(f\); neither the measure nor \(f\) is replaced in the conclusion.

Here is monotone convergence directly from that definition. If \(0\leq f_n\uparrow f\), monotonicity gives \(L=\lim_n\int f_n\leq\int f\). For an arbitrary nonnegative simple \(s\leq f\) and \(0<t<1\), let \(E_n=\{f_n\geq ts\}\). These increase, and their union contains \(\{s>0\}\): at a point where \(s>0\), the limit \(f\geq s>ts\) forces an eventual such inequality. On each of the finitely many positive levels of \(s\), measure continuity gives \(\int s1_{E_n}\uparrow\int s\). This includes an infinite level-set measure; zero levels still contribute zero. Since \(\int f_n\geq t\int s1_{E_n}\), we have \(L\geq t\int s\). If \(\int s=\infty\), this already forces \(L=\infty\); otherwise let \(t\uparrow1\). Taking the supremum over \(s\) proves
\[
 0\leq f_n\uparrow f\quad\Longrightarrow\quad
       \int f_n\,d\mu\uparrow\int f\,d\mu,\qquad
 \int(f+g)\,d\mu=\int f\,d\mu+\int g\,d\mu .
 \tag{GM4}
\]
For the additive assertion, use the increasing simple approximations of both original functions in (GM3). Their sums increase to \(f+g\), and every simple integral is additive. Positive homogeneity follows first for simples and then by the same limit. Applying (GM4) to the finite partial sums proves integration of an arbitrary countable nonnegative sum. No sigma-finiteness is needed in this paragraph.

If \(\int g<\infty\), the set on which \(g=\infty\) has measure zero: \(n1_{\{g=\infty\}}\leq g\) gives \(n\mu\{g=\infty\}\leq\int g\) for every positive integer \(n\). Integrating the four nonnegative parts of a complex measurable \(h\) with \(\int|h|<\infty\) defines its integral and proves linearity, because all those integrals are finite. Its triangle inequality follows without a pointwise choice of phase: if \(I=\int h\ne0\), use the constant \(c=\overline I/|I|\) and \(\operatorname{Re}(ch)\leq|h|\); if \(I=0\), the inequality already holds.

For nonnegative \(f_n\), put \(g_N=\inf_{n\geq N}f_n\). These are measurable by (GM2), increase to \(\liminf f_n\), and satisfy \(\int g_N\leq\inf_{n\geq N}\int f_n\). Formula (GM4) proves Fatou's inequality. If \(h_n\) and \(h\) are measurable complex functions, \(h_n\to h\) almost everywhere and \(|h_n|\leq g\) almost everywhere with \(\int g<\infty\), take the countable union of their measurable exceptional null sets and the null infinite-value set of \(g\). Change all the functions to zero on that measurable null set. This preserves all original integrals. Now \(|h|\leq g\) everywhere, and Fatou applies to \(2g-|h_n-h|\). Additivity expresses its finite integral as \(2\int g-\int|h_n-h|\). Fatou therefore gives
\[
 \int|h_n-h|\,d\mu\longrightarrow0,\qquad
 \int h_n\,d\mu\longrightarrow\int h\,d\mu .
 \tag{GM5}
\]
Every subtraction here is of finite integrals. If \(\mu(X)<\infty\) and \(|h_n|\leq M<\infty\), use the original constant majorant \(M1_X\), whose integral is \(M\mu(X)\), to prove bounded convergence. For \(M=0\) or \(\mu(X)=0\) this integral is exactly zero. This proves the entire convergence entry used for one-dimensional Lebesgue measure, and also its stated general finite-measure version.

The labels GM4–GM5 above prove the monotone, Fatou and dominated convergence
statements denoted LP1–LP2 in the original Section 15.1. In the retained
paragraphs below, a reference to LP1 means exactly this proved GM4.

## M4. Product integration

Here is product integration with its actual measurability requirement. In a fixed finite coordinate box \(Q=Q_x\times Q_y\), let \(\mathcal C\) consist of the Borel sets \(E\subset Q\) whose sections \(E_x\) are measurable, whose section measure is a measurable function of \(x\), and which satisfy
\[
 |E|=\int_{Q_x}|E_x|\,dx.
 \tag{LP3}
\]
Coordinate rectangles belong to \(\mathcal C\), by the full box-volume formula. The whole box belongs. Relative complementation preserves membership because every section measure is at most the finite \(|Q_y|\), so both sides subtract from \(|Q_x||Q_y|\). Disjoint countable unions preserve membership by countable additivity and (LP1), which also proves measurability of the sum of the section measures. Thus \(\mathcal C\) is a Dynkin class containing the rectangles.

For completeness, the needed class argument is finite and exact. Let \(\mathcal L\) be the smallest Dynkin class containing the rectangles. A Dynkin class is closed under differences of nested members: if \(A\subset B\), use the disjoint union \(A\cup(Q\setminus B)\) and complement. For a rectangle \(A\), the sets \(B\) for which \(A\cap B\in\mathcal L\) form a Dynkin class and contain the rectangles, since intersections of rectangles are rectangles or empty. Hence they contain \(\mathcal L\). Fixing now any \(B\in\mathcal L\) and making the same argument in \(A\) shows that \(\mathcal L\) is closed under all finite intersections. Complements give finite unions. Disjointifying a countable union by subtracting its finitely many preceding members then shows closure under countable unions. Therefore \(\mathcal L\) is a sigma-algebra containing the rectangles, which generate the Borel sets of \(Q\). This proves (LP3) for every Borel set in the box.

Increasing simple approximation and (LP1) now prove nonnegative Tonelli on \(Q\). Exhausting both original spaces by expanding coordinate boxes proves it on \(\mathbb R^a\times\mathbb R^b\). A Lebesgue measurable set differs from a Borel set by a subset of a Borel null set. For that null set, (LP3) says that its sections are null outside a null set of \(x\)'s. Completeness of the section measure makes every subset section measurable there. On the exceptional null set one may choose the value zero for the inner integral. Thus completed Lebesgue measurability gives the same iterated identity almost everywhere; it does not assert measurable sections at every exceptional point. Applying this argument to simple approximations proves the completed version for nonnegative functions. Finally, apply it to \(|h|\) when \(\int|h|<\infty\), and to the positive and negative parts of the real and imaginary components. All these integrals are finite. We obtain the full identities
\[
 \int h(x,y)\,dx\,dy
   =\int\left(\int h(x,y)\,dy\right)dx
   =\int\left(\int h(x,y)\,dx\right)dy,
 \tag{LP4}
\]
for nonnegative \(h\), with possibly infinite integrals, and for absolutely integrable complex \(h\). Sections and inner integrals have their almost-everywhere meanings in the completed case.

## M5. The two required norms

This is the \(p=1,2\) specialization of AN03-P004, Section 15.2, with its
scalar step displayed explicitly. Functions are identified when they agree
almost everywhere. Set \(\|f\|_p=(\int|f|^p)^{1/p}\).
For a nonnegative measurable \(g\), an integral of zero forces \(g=0\)
almost everywhere: \(j^{-1}1_{\{g>1/j\}}\le g\), so each displayed level set
is null, and their countable union is \(\{g>0\}\). This proves definiteness
of both norms on those equivalence classes. Their homogeneity follows from
positive homogeneity of the integral.

For \(L^2\) functions of nonzero norms, apply
\(2ab\le a^2+b^2\), which is \((a-b)^2\ge0\), to
\(a=|f|/\|f\|_2\), \(b=|g|/\|g\|_2\), and integrate. This proves
\[
 \int |fg|\le\|f\|_2\|g\|_2. \tag{M1}
\]
If a norm is zero, its function vanishes almost everywhere, and the same
inequality holds. Since \(|f+g|^2\le2|f|^2+2|g|^2\), the sum belongs to
\(L^2\). Expansion of its squared modulus and (M1) give
\[
 \|f+g\|_2^2\le\|f\|_2^2+2\|f\|_2\|g\|_2+\|g\|_2^2.
\]
Taking nonnegative square roots proves the triangle inequality. For \(L^1\)
it follows by integrating the scalar triangle inequality. Finally, the
complex integral triangle inequality was proved in M3 by multiplication
by a single constant phase. These arguments establish every norm
inequality used below, without a general exponent or convexity theorem.

## M6. Completeness

For \(p=1\) or \(p=2\), let \((f_j)\) be norm Cauchy. Choose a subsequence \((f_{j_k})\) with \(\|f_{j_{k+1}}-f_{j_k}\|_p\leq2^{-k}\). The increasing finite sums \(G_M=|f_{j_1}|+\sum_{k=1}^M|f_{j_{k+1}}-f_{j_k}|\) have norms at most \(\|f_{j_1}\|_p+\sum_{k=1}^M2^{-k}\), by Minkowski. Equation (LP1), applied to \(G_M^p\), proves that their pointwise limit \(G\) is in \(L^p\) and finite almost everywhere. Thus the series of original differences converges absolutely almost everywhere, giving a measurable limit \(f\). The same argument for the tail gives
\[
 \|f-f_{j_k}\|_p
 \leq\sum_{\nu=k}^\infty\|f_{j_{\nu+1}}-f_{j_\nu}\|_p
 \leq\sum_{\nu=k}^\infty2^{-\nu}.
 \tag{LP10}
\]
One obtains the first bound by dominating the pointwise difference by that nonnegative tail and passing its finite partial sums through (LP1). The Cauchy property and the triangle inequality then give convergence of the entire sequence to \(f\).

## M7. Compact smooth density

The smooth density assertion has a different domain: \(p=1,2\) on \(\mathbb R^n\). First truncate the original \(f\) by \(|x|\leq R\) and \(|f(x)|\leq M\). Dominated convergence applied to \(|f|^p\) proves convergence of these truncations as \(R,M\) grow. On the resulting bounded support and bounded complex range, a finite square grid of mesh \(\delta\) gives a measurable simple function \(a=\sum_{j=1}^J c_j1_{E_j}\), with \(|f-a|\leq\sqrt2\delta\). Each \(E_j\) has finite measure, so the \(L^p\) error is at most \(\sqrt2\delta\) times the support measure to the power \(1/p\).

For a measurable \(E\) with finite measure, its outer-measure definition gives a countable coordinate-box cover with total volume less than \(|E|+\varepsilon\). Enlarge its boxes to open boxes, choosing the extra volume of box \(j\) less than \(\varepsilon2^{-j}\). Their open union \(O\) contains \(E\) and has \(|O\setminus E|<2\varepsilon\). The finite unions \(F_J\) of the first \(J\) boxes increase to \(O\). Since \(|O|<\infty\), (LP1) gives \(|O\setminus F_J|\to0\). Therefore \(|E\mathbin{\triangle} F_J|\leq|O\setminus E|+|O\setminus F_J|\), proving approximation in measure by a finite union of bounded coordinate boxes.

Write one such union as \(F=\bigcup_{j=1}^J\prod_{i=1}^n(a_{ji},b_{ji})\). For \(\delta>0\) smaller than half every side length, choose one-dimensional smooth functions between zero and one, equal to one on \([a_{ji}+\delta,b_{ji}-\delta]\) and supported in \((a_{ji}-\delta,b_{ji}+\delta)\). Their product is \(\theta_{j,\delta}\), and \(\Theta_\delta=1-\prod_{j=1}^J(1-\theta_{j,\delta})\) is compact smooth, between zero and one. The difference from \(1_F\) is supported in the union of the full box layers. Hence
\[
 \|\Theta_\delta-1_F\|_p^p
 \leq\sum_{j=1}^J\left[
       \prod_{i=1}^n(b_{ji}-a_{ji}+2\delta)
       -\prod_{i=1}^n(b_{ji}-a_{ji}-2\delta)\right]
       \longrightarrow0.
 \tag{LP11}
\]
Coordinate faces have measure zero: cover a bounded face by a box with arbitrarily small thickness and use the full volume product; unbounded faces are countable unions of bounded ones. Thus open or closed endpoint choices do not alter this estimate. Combining the finite-union approximation with (LP11) proves compact smooth approximation of each original indicator \(1_{E_j}\). Minkowski gives the full coefficient bound \(\|\sum_j c_j(1_{E_j}-\Theta_j)\|_p\leq\sum_j|c_j|\|1_{E_j}-\Theta_j\|_p\). Keeping these finitely many coefficients and then taking the preceding truncation and grid errors to zero proves density of \(C_c^\infty\) in \(L^p\).

The taper choices in LP11 use the explicit U001 construction cited above:
the product of two translated, scaled copies of its smooth step function
is one on the smaller interval and zero outside the larger interval.
Consequently the smooth density proof has no unproved mollification input.
The same construction gives **simultaneous** density for \(L^1\cap L^2\).
Truncate so that both tail norms are small, choose the range grid so that
both norm errors are small, and choose each of the finitely many box-layer
widths to meet both remaining error bounds. A finite minimum of positive
widths meets both conditions. Thus for \(f\in L^1\cap L^2\) there are
\(v_j\in C_c^\infty\) with \(\|v_j-f\|_1+\|v_j-f\|_2\to0\).

## M8. Compatibility with the earlier integral

This connecting proof identifies the new measure integral with the
continuous and Schwartz integrals used in U001. It does not assume that
the two constructions agree. On a bounded coordinate box \(Q\), partition
into smaller coordinate boxes. A continuous real function has lower and
upper simple functions on that partition, with integrals equal to its
lower and upper Darboux sums, because M2 proves the exact box volumes and
null faces. Uniform continuity on \(Q\) makes the difference of those sums
at most \(|Q|\) times the maximum cell oscillation, which tends to zero.
Monotonicity traps the Lebesgue integral between the same sums. Therefore
it equals the earlier Riemann integral. Apply this separately to the real
and imaginary parts.

For a Schwartz function \(v\), fix an integer \(N>n\). Its bound
\(|v(x)|\le C_N\langle x\rangle^{-N}\) on the dyadic regions
\(2^j\le |x|_\infty<2^{j+1}\) bounds their absolute integrals by
\(C'_N2^{j(n-N)}\), using the enclosing box volume. The convergent
geometric tail tends to zero for both constructions of the integral.
Equality on expanding finite boxes therefore proves equality of the
Schwartz integrals, including every polynomial times a Schwartz
derivative. The same reasoning on the product space treats the absolute
products in the U001 Schwartz Parseval proof. Its Fourier inversion and
Plancherel formulas consequently apply with exactly this Lebesgue
measure, including their original \(2\pi\) factors.

## Free source comparisons

Terence Tao, *An introduction to measure theory*, the
[author-linked preliminary draft hosted December 2012](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf):
Lemma 1.2.6 (box volume), Lemma 1.2.12 (outer approximation),
Theorem 1.4.44 and Corollary 1.4.47 / Theorem 1.4.49 (convergence),
Theorem 1.7.3 (outer-measure construction), and Theorems 1.7.15,
1.7.18 and 1.7.21 (product integration).
The companion proves its own completion, generating-class and null-section
steps, including steps left as exercises in that draft.

Tao, [*245B, notes 3: Lp spaces*](https://terrytao.wordpress.com/2009/01/09/245b-notes-3-lp-spaces/),
9 January 2009, Lemma 1, Propositions 1–3 and Remark 7, supplies the free
norm, completeness and simple-density comparison. M6 supplies the full
Cauchy-subsequence step; M7 supplies the smooth approximation itself.
These human readings are mathematical comparisons, not imported prose or
substitutes for the programme proofs above. The free draft and blog are
not included in this component.
