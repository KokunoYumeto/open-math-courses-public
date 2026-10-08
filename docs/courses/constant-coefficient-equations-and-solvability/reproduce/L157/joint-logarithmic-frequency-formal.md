# Joint logarithmic-frequency limits

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Public domain (CC0 1.0).*

Fourier transforms record singularities through their behavior at large real frequencies. A logarithmically growing complex observation window reveals a compact convex set from each limiting profile. For several distributions, the windows must have the same center. This requirement contains information that disappears if we choose a different sequence for each distribution.

Basic references are Alex Kruckman's *Notes on Ultrafilters*, Terence Tao's *Ultrafilters, nonstandard analysis, and epsilon management*, and Lars Hörmander's *The Analysis of Linear Partial Differential Operators II*. The arguments below provide the proofs used here. Our exact prerequisites are:

- [Compact Fourier division, the compact-support growth criterion](../../AN02-L122.html#2-the-compact-support-growth-criterion): the entire Fourier transform of a compact distribution, its polynomial-times-support-function bound, and Fourier injectivity.
- [Entire logarithms, the scalar holomorphic logarithm proof](../../AN02-L147.html#gd4-scalar-holomorphic-logarithms-are-proper-psh-and-locally-integrable): a nonzero holomorphic scalar function has a proper, locally integrable PSH logarithm.
- [Local compactness and Hartogs bounds](../../AN02-L143.html#psh-local-compactness): a locally upper-bounded PSH sequence has a proper local integral limit along a subsequence or collapses uniformly to minus infinity; canonical representatives are recovered by positive radial averages.
- [Plurisubharmonic envelopes and support functions](../../AN02-L139.html#psh-envelope-theorem): a proper PSH function bounded by a constant plus a linear imaginary-height bound has a finite convex horizontal envelope and a compact convex recession support set.
- [Compact smooth Fourier decay](../../AN02-L153.html#tp2-exact-entire-decay-on-a-fixed-smooth-support): arbitrary polynomial decay holds in the whole complex space, with the exact support function in the exponential factor.
- [Fourier endpoints and asymptotic zeros](../../AN02-L137.html#asymptotic-zero-count): the local integral limit of a dilated Fourier logarithm of a nonzero compact complex measure on the line.

All norms on real and complex finite-dimensional spaces are Euclidean. Integration on \(\mathbb C^n\) means Lebesgue measure in real dimension \(2n\). A proper PSH function may take the value \(-\infty\) on a null set; proper means it is not identically \(-\infty\).

## 2. The compactness and support statement

Let \(u\) be a compactly supported distribution on \(\mathbb R^n\), \(n\ge1\). Its Fourier convention and the observation family are

\[
F_u(\zeta)=\langle u(x),e^{-ix\cdot\zeta}\rangle,\qquad
R=|\xi|>2,\quad s=\log R,\qquad
L_u(z,\xi)=\frac{\log|F_u(\xi+s z)|}{s}.
\tag{2.1}
\]

The pairing is defined by multiplying the exponential by a compact smooth function equal to one near the support. It is independent of that choice. At a zero of the transform the logarithm is \(-\infty\). For \(u=0\), the whole function \(L_u\) is identically \(-\infty\).

**Theorem 2.1.** From every real frequency sequence \(|\xi_j|\to\infty\), one can extract a subsequence on which \(L_u\) either converges in \(L^1_{\mathrm{loc}}(\mathbb C^n)\) to a proper PSH function \(v\), or tends to \(-\infty\) uniformly on every compact set. In the proper case, if \(K\) is a nonempty compact convex carrier of \(u\) and the compact-support Fourier estimate uses polynomial order \(N\), then

\[
v(z)\le N+H_K(\operatorname{Im}z),\qquad
M_v(\eta)=\sup_{x\in\mathbb R^n}v(x+i\eta),\qquad
h_v(\eta)=\lim_{t\to\infty}\frac{M_v(t\eta)}t.
\tag{2.2}
\]

The function \(M_v\) is finite and convex. The function \(h_v\) is the support function of a nonempty compact convex set \(C_v\subset K\). In the collapsed case write \(v\equiv-\infty\), \(C_v=\varnothing\), and \(h_v\equiv-\infty\). A finite constant profile, including \(v\equiv0\), instead has \(C_v=\{0\}\).

**Proof.** For \(u\ne0\), Fourier injectivity and the scalar logarithm theorem make every \(L_u(\cdot,\xi)\) proper PSH. Multiplication of the logarithm by the positive number \(1/s\), and the invertible affine complex change \(z\mapsto\xi+s z\), preserve that property. The compact-support estimate gives

\[
|F_u(\zeta)|\le C(1+|\zeta|)^N e^{H_K(\operatorname{Im}\zeta)},\qquad
L_u(z,\xi)\le H_K(\operatorname{Im}z)
 +\frac{\log C+N\log(1+|\xi+s z|)}s.
\tag{2.3}
\]

Positive homogeneity gives \(H_K(s\operatorname{Im}z)=sH_K(\operatorname{Im}z)\). On \(|z|\le A\), \(|\xi+s z|\le R+A\log R\). For all \(R>2\), \((\log R)/R\le1/e\), so

\[
1+R+A\log R\le R(3/2+A/e),\qquad
\frac{\log(1+R+A\log R)}{\log R}
\le1+\frac{\log(3/2+A/e)}{\log2}.
\tag{2.4}
\]

Replacing \(\log C\) by its nonnegative part gives a finite common upper bound on every compact set for the entire parameter range \(R>2\). The PSH compactness theorem therefore gives the asserted alternatives on a subsequence. It applies also to \(u=0\), which directly has the collapsed alternative.

For fixed \(A\), the upper bound in (2.3) improves as \(R\to\infty\): the extra constant beyond \(N+H_K(\operatorname{Im}z)\) is at most

\[
\frac{\log C}{\log R}
 +\frac{N}{\log R}\log\!\left(1+\frac1R+\frac{A\log R}{R}\right)
\longrightarrow0.
\tag{2.5}
\]

If the selected limit is proper, extract an almost-everywhere convergent subsequence from the \(L^1_{\mathrm{loc}}\) convergence. It gives the bound (2.2) almost everywhere on each compact ball, hence on the whole space. To recover the bound at every point, use the positive radial averages of \(v\). Their averages are bounded by the averages of the continuous function \(N+H_K(\operatorname{Im}z)\). Let the averaging radius decrease to zero. Canonical radial recovery gives \(v\), and continuity gives the desired upper bound everywhere.

Set \(r_K=\max_{x\in K}|x|\). Then \(v(z)\le N+r_K|\operatorname{Im}z|\), so the proved PSH envelope theorem gives \(M_v\), its finite recession function, and its nonempty compact convex set \(C_v\). The sharper bound yields \(M_v(t\eta)\le N+tH_K(\eta)\), hence \(h_v\le H_K\).

For clarity, this order of support functions implies inclusion of the sets. If \(q\notin K\), choose a closest point \(p\in K\). Convexity gives \((q-p)\cdot(x-p)\le0\) for every \(x\in K\), by differentiating the squared distance along the segment from \(p\) to \(x\) at its minimum. Thus \(q\cdot(q-p)>H_K(q-p)\). No point of \(C_v\), whose every pairing is at most \(h_v\le H_K\), can equal \(q\). Therefore \(C_v\subset K\). The collapsed convention and the finite-constant calculation follow directly from their definitions. \(\square\)

## 3. Smooth perturbations preserve the full limiting profile

**Lemma 3.1.** If \(b\in C_c^\infty(\mathbb R^n)\), then

\[
\sup_{z\in Q}L_b(z,\xi)\longrightarrow-\infty
\quad\text{as }|\xi|\to\infty
\quad\text{for every compact }Q\subset\mathbb C^n.
\tag{3.1}
\]

**Proof.** Enclose \(Q\) in \(|z|\le A\), and let \(S\) be a compact carrier of \(b\). Whole-complex smooth Fourier decay gives, for every integer \(m\ge0\),
\(|F_b(\zeta)|\le C_m(1+|\zeta|)^{-m}e^{H_S(\operatorname{Im}\zeta)}\).
For sufficiently large \(R\), \(|\xi+s z|\ge R-A\log R\ge R/2\). With \(r_S=\max_{x\in S}|x|\), it follows that

\[
L_b(z,\xi)\le
-m+r_S A+\frac{\log C_m+m\log2}{\log R}.
\tag{3.2}
\]

For any desired finite negative bound, first choose \(m\) large enough, then choose \(R\) large enough. This proves uniform collapse; zeros only lower the logarithm. For \(b=0\) the result is immediate. \(\square\)

**Theorem 3.2.** Fix one escaping frequency sequence. If \(L_u\) has a proper local integral limit \(v\), then \(L_{u+b}\) has the same local integral limit on that same sequence. If \(L_u\) collapses uniformly on compact sets, then so does \(L_{u+b}\). Consequently all these limits depend only on the compact distribution modulo compact smooth functions.

**Proof.** Write \(a_j=L_u(\cdot,\xi_j)\), \(c_j=L_{u+b}(\cdot,\xi_j)\), \(d_j=L_b(\cdot,\xi_j)\), and \(s_j=\log|\xi_j|\). The triangle inequality and its reverse decomposition \(F_u=F_{u+b}-F_b\) give, with extended values permitted,

\[
c_j\le\frac{\log2}{s_j}+\max(a_j,d_j),
\qquad
a_j\le\frac{\log2}{s_j}+\max(c_j,d_j).
\tag{3.3}
\]

If \(a_j\) collapses, Lemma 3.1 and the first inequality imply uniform collapse of \(c_j\).

Suppose now that \(a_j\to v\) in local \(L^1\), with \(v\) proper. Theorem 2.1 supplies common local upper bounds for \(c_j\). Every subsequence of \(c_j\) thus has a further subsequence with a proper local integral limit \(w\), or with uniform collapse. The latter is impossible: the second inequality in (3.3) would force \(a_j\) to collapse on that further subsequence. On a ball of positive volume its integrals would tend to \(-\infty\), whereas its local \(L^1\) limit \(v\) has a finite integral.

In the proper case pass, if needed, to a further subsequence along which both \(a_j\to v\) and \(c_j\to w\) almost everywhere. At almost every point both limits are finite, while \(d_j\to-\infty\) and \((\log2)/s_j\to0\). The two inequalities give \(w\le v\) and \(v\le w\). Hence the two proper PSH functions agree almost everywhere. Their positive radial averages agree, and canonical recovery makes them agree at every point.

This identifies the limit of every further compactness extraction as \(v\). To prove convergence of the whole original sequence, a failure on a compact ball would provide a subsequence on which \(\int|c_j-v|\ge\varepsilon>0\). Its further compactness extraction converges in local \(L^1\) to \(v\), which contradicts that lower bound. The collapsed and proper conclusions are therefore proved on the original common sequence. Apply the same argument with \(-b\) to reverse the perturbation. \(\square\)

The assertion concerns full profiles, not just their support functions. It does not assert pointwise convergence at Fourier zeros.

## 4. One frequency sequence for a finite list

Let \(\mathcal H\) consist of the support functions of nonempty compact convex subsets of \(\mathbb R^n\), together with the function identically \(-\infty\) for the empty set.

**Definition 4.1.** For compact distributions \(u_1,\ldots,u_k\), \(k\ge1\), let \(\mathcal J(u_1,\ldots,u_k)\subset\mathcal H^k\) consist of tuples \((h_1,\ldots,h_k)\) for which there is **one** real sequence \(|\xi_j|\to\infty\) such that every \(L_{u_i}(\cdot,\xi_j)\) has a proper local \(L^1\) limit or a locally uniform collapsed limit, and \(h_i\) is the support function of that limit. Different coordinates may have different types of limit.

**Theorem 4.2.** This family is nonempty. For \(1\le\ell<k\), dropping the last \(k-\ell\) coordinates gives a surjection

\[
\mathcal J(u_1,\ldots,u_k)\longrightarrow
\mathcal J(u_1,\ldots,u_\ell).
\tag{4.1}
\]

The family is unchanged when any coordinate is changed by a compact smooth function.

**Proof.** Begin with \(\xi_j=(j+3)e_1\), where \(e_1\) is the first coordinate unit vector. Apply Theorem 2.1 to \(u_1\), then to \(u_2\) on the selected subsequence, and continue finitely many times. A subsequence preserves both proper local \(L^1\) convergence and locally uniform collapse. The final sequence realizes a tuple, proving nonemptiness.

For surjectivity, begin with a witnessing sequence for a prescribed tuple in the smaller family, rather than with an arbitrary sequence. Extract successively for \(u_{\ell+1},\ldots,u_k\). All the prescribed limiting functions remain the same on the final subsequence, so their support functions remain the prescribed ones. The extra coordinates supply the desired lift. Conversely every tuple in the larger family restricts to a tuple in the smaller one, using its existing witnessing sequence.

For smooth invariance, keep that witnessing sequence and apply Theorem 3.2 in each coordinate. This proves inclusion of the families. Replacing each perturbation by its negative proves equality. \(\square\)

Surjectivity does not mean that every independently chosen list of one-coordinate limits is jointly realizable. The cross-shaped example below proves this distinction.

## 5. Countably many coordinates can still use a sequence

**Theorem 5.1.** A countable family of compact distributions has a simultaneous profile limit along a common escaping frequency sequence. A prescribed simultaneous limit on any countable subfamily can be retained while extending to a larger countable family.

**Proof.** Start with any escaping sequence, or the existing witness for the prescribed subfamily. Enumerate the coordinates that still require extraction. Repeated application of Theorem 2.1 produces nested infinite subsequences. Coordinate \(i\) has its limit on every subsequence from the \(i\)-th stage onward.

Take the compact exhaustion \(B_m=\{|z|\le m\}\) of \(\mathbb C^n\). At stage \(j\), choose a sufficiently late frequency from the \(j\)-th nested subsequence so that its norm exceeds \(j\), its original index exceeds all indices previously chosen, and, for all of the first \(j\) coordinates and balls \(B_1,\ldots,B_j\), the following requirements hold:

\[
\begin{cases}
\displaystyle\int_{B_m}|L_{u_i}(\cdot,\xi_j)-v_i|<1/j,
 &v_i\text{ proper},\\[4pt]
\displaystyle\sup_{B_m}L_{u_i}(\cdot,\xi_j)<-j,
 &v_i\equiv-\infty.
\end{cases}
\tag{5.1}
\]

There are only finitely many requirements at this stage. Each holds on a sufficiently late part of the \(j\)-th subsequence, so such a choice exists. Include the first \(j\) already prescribed coordinates too, if there are countably many of them. For fixed \(i,m\), the requirements eventually hold at every stage, and prove the required convergence. Every original prescribed limit is retained because the chosen sequence is a subsequence of its witness. \(\square\)

The construction uses countability. We now give a different construction for arbitrary index sets.

## 6. A compact space for each distribution

The identically minus-infinite function does not belong to \(L^1_{\mathrm{loc}}\). We place it together with the proper limits by exponentiating: set \(q_v=e^v\), with \(e^{-\infty}=0\). Use the metric

\[
d(q,r)=\sum_{m=1}^\infty 2^{-m}
 \min\!\left(1,\int_{B_m}|q-r|\right)
\tag{6.1}
\]

on locally integrable functions modulo almost-everywhere equality. The triangle inequality follows from the integral triangle inequality and \(\min(1,a+b)\le\min(1,a)+\min(1,b)\). The metric is zero exactly when the functions agree almost everywhere on every ball. Convergence in this metric is equivalent to local \(L^1\) convergence: each fixed summand controls its ball integral, and a finite sum plus its geometric tail proves the converse.

**Lemma 6.1.** On any family with common local upper bounds, proper PSH local \(L^1\) convergence \(v_j\to v\) implies \(e^{v_j}\to e^v\) in the metric. Locally uniform collapse implies convergence to zero. Conversely, metric convergence to \(e^v\), with \(v\) proper, implies proper local \(L^1\) convergence of the profiles; metric convergence to zero implies locally uniform collapse.

**Proof.** On a ball with common finite upper bound \(M\), the exponential is Lipschitz with constant \(e^M\) on \((-\infty,M]\). Thus \(\int|e^{v_j}-e^v|\le e^M\int|v_j-v|\) in the proper case. In the collapsed case \(e^{v_j}\) tends uniformly to zero on each ball.

For the converse, every subsequence of the profiles has a further compactness extraction. Its exponentials converge either to the exponential of its proper limit, or to zero. A proper PSH function is finite almost everywhere, so its exponential is positive almost everywhere. It cannot equal zero as a local integral class. Two proper profiles whose exponentials agree almost everywhere agree almost everywhere themselves, and then everywhere by radial recovery.

If the metric limit is \(e^v\ne0\), these facts exclude collapse and identify every proper extraction with \(v\). Failure of local \(L^1\) convergence is contradicted by a further extraction as in Theorem 3.2. If the metric limit is zero and uniform collapse failed, the compactness theorem would supply a proper local \(L^1\) extraction, whose exponential would be both positive almost everywhere and equal to zero. This is impossible. \(\square\)

Here and below, a common upper bound for a sequence and a proper limit follows from radial recovery, so including the limit does not change the premise.

For each compact distribution \(u\), define

\[
\mathcal K_u=\overline{\{e^{L_u(\cdot,\xi)}:\xi\in\mathbb R^n,\ |\xi|>2\}}^{\,d}.
\tag{6.2}
\]

**Proposition 6.2.** The space \(\mathcal K_u\) is compact and metrizable. Every one of its points is the exponential of a unique proper PSH function or is zero for the collapsed profile.

**Proof.** Estimate (2.4) bounds the entire parameter family locally above. Any sequence of its members has a profile extraction by the PSH compactness theorem, and hence a metric-convergent exponential extraction by Lemma 6.1. Its limit is of the stated form.

For a sequence \(q_j\) in the closure, choose original parameter members \(p_j\) with \(d(p_j,q_j)<1/j\). A profile extraction of \(p_j\) gives a metric limit; the corresponding \(q_j\) has the same limit by the triangle inequality. It lies in the closure, and is of the stated form. Thus \(\mathcal K_u\) is sequentially compact. This also proves the description of an individual point of the closure, by approximating that point and extracting. Uniqueness follows from the exponential argument in Lemma 6.1.

We supply the metric compactness step. If a sequentially compact metric space were not totally bounded, some \(\varepsilon>0\) would allow an infinite sequence of pairwise distances at least \(\varepsilon\), which has no convergent subsequence. Finite \(1/j\)-nets therefore exist. Their countable union, with rational-radius balls, gives a countable basis: for a point inside an open set choose a small ball inside that set, then a net point close enough to give a basis ball containing the point and contained in the set.

Every open cover has a countable subcover: for each basis element contained in a cover member, choose one such member. If that subcover \((O_j)\) had no finite subcover, choose \(x_j\) outside \(O_1\cup\cdots\cup O_j\). A convergent subsequence has a limit in some \(O_m\); openness puts all its sufficiently late members in \(O_m\), contradicting their choice. Thus every cover has a finite subcover, as required. \(\square\)

The closure includes limits of frequencies that stay bounded. Those points need not satisfy the global affine-growth conclusion of Theorem 2.1. We assign a recession support function only to limits that escape to infinity.

## 7. Arbitrary families through one ultrafilter

The arbitrary-family extension uses the axiom of choice in the form of Zorn's lemma. The finite and countable results above use their explicit subsequence constructions.

Let \(I=\{\xi\in\mathbb R^n:|\xi|>2\}\). A proper filter on \(I\) is a collection of subsets containing \(I\), excluding the empty set, closed under finite intersections and passage to supersets. An ultrafilter is a proper filter that, for every subset \(A\subset I\), contains exactly one of \(A\) and \(I\setminus A\). We call it escaping if it contains every tail

\[
I_T=\{\xi\in I:|\xi|>T\}\qquad(T>2).
\tag{7.1}
\]

Such an ultrafilter exists. The supersets of tails form a proper filter. Order the proper filters extending it by inclusion. The union of a chain is again a proper filter: finitely many given members all belong to one member of the chain, and the empty set belongs to none. Zorn's lemma gives a maximal proper filter \(\mathcal U\).

To verify the ultrafilter property, if \(A\notin\mathcal U\) and every \(F\in\mathcal U\) met \(A\), the supersets of the sets \(F\cap A\) would form a proper filter strictly extending \(\mathcal U\). Thus some \(F\in\mathcal U\) is disjoint from \(A\), and \(I\setminus A\in\mathcal U\). Both a set and its complement cannot belong to a proper filter. This proves the assertion.

**Lemma 7.1.** For every map \(q:I\to K\) into a compact metric space and every ultrafilter \(\mathcal U\), there is a unique point \(q_\mathcal U\in K\) such that \(q^{-1}(O)\in\mathcal U\) for every open neighborhood \(O\) of \(q_\mathcal U\).

**Proof.** The closed sets \(\overline{q(F)}\), \(F\in\mathcal U\), have the finite intersection property: \(q(F_1\cap\cdots\cap F_m)\) is nonempty and lies in every one of their closures. Compactness gives a point in their whole intersection; otherwise their open complements would have a finite subcover, contradicting that property.

If a neighborhood \(O\) of this point had \(q^{-1}(O)\notin\mathcal U\), its complement would belong to \(\mathcal U\), and the point would lie in the closed set \(K\setminus O\), a contradiction. For uniqueness, two different points have disjoint open neighborhoods. Their preimages cannot both belong to a proper filter. \(\square\)

Apply the lemma to \(q_u(\xi)=e^{L_u(\cdot,\xi)}\in\mathcal K_u\). One escaping ultrafilter simultaneously gives a limit for every compact distribution. Each such limit is an escaping profile from Theorem 2.1. Indeed choose \(\xi_j\) in
\(I_j\cap q_u^{-1}(B_d(q_{u,\mathcal U},1/j))\), interpreting \(I_j=I\) for \(j\le2\). This finite intersection belongs to \(\mathcal U\) and is nonempty. The resulting sequence escapes and converges in the metric. Proposition 6.2 and Lemma 6.1 identify its proper local \(L^1\) or collapsed limit. Theorem 2.1 supplies its support function.

**Definition 7.2.** For a family \((u_\alpha)_{\alpha\in A}\) indexed by any set, let \(\mathcal J_{\mathrm{uf}}((u_\alpha))\subset\mathcal H^A\) consist of the tuples of support functions obtained from a single escaping ultrafilter in this way.

**Theorem 7.3.** This family is nonempty. For every subset \(B\subset A\), coordinate restriction is a surjection onto \(\mathcal J_{\mathrm{uf}}((u_\beta)_{\beta\in B})\). For finite or countable families the ultrafilter definition agrees with the common-sequence definition. It is invariant under a compact smooth perturbation of every coordinate.

**Proof.** Existence of an escaping ultrafilter and uniqueness of every compact-space limit prove nonemptiness. Given a tuple for the subfamily, retain its witnessing ultrafilter and take the remaining compact-space limits with that same ultrafilter. The already assigned limits cannot change by uniqueness. This proves surjectivity, also for empty subfamilies.

For a finite or countable ultrafilter family, enumerate the coordinates. For each \(j\), choose \(\xi_j\) from the intersection of \(I_j\) and the preimages of the radius-\(1/j\) metric balls about the first \(j\) limiting coordinates. All these finitely many sets belong to the ultrafilter, so their intersection is nonempty. For each fixed coordinate its metric limit holds on this one escaping sequence. Lemma 6.1 gives the required profile convergence.

Conversely, a common-sequence witness defines a proper filter consisting of all subsets of \(I\) containing every sufficiently late \(\xi_j\). This filter contains every escaping tail and every preimage neighborhood of every limiting coordinate. The maximal-filter construction above extends it to an ultrafilter. Lemma 7.1 then gives exactly the original coordinate limits, proving equality of the two definitions.

For smooth invariance we first show, for each \(u,b\),

\[
d\!\left(e^{L_u(\cdot,\xi)},e^{L_{u+b}(\cdot,\xi)}\right)
\longrightarrow0\quad\text{as }|\xi|\to\infty.
\tag{7.2}
\]

If this failed, some escaping sequence would have distance at least a fixed \(\varepsilon>0\). Extract a profile limit of \(L_u\). Theorem 3.2 gives the same profile limit for \(L_{u+b}\) on this subsequence, whether proper or collapsed. Lemma 6.1 makes both exponentials converge to the same metric point, contradicting the positive separation.

On an escaping ultrafilter every sufficiently large frequency tail belongs to it. By (7.2) the two coordinate maps therefore have the same limit: any ball about the first limit contains the second map on the intersection of a smaller first-map ball and a tail where their mutual distance is small. Both sets belong to the ultrafilter. This argument applies separately to every coordinate, even for an uncountable family. Negative perturbations give equality. \(\square\)

For an uncountable family this result gives a common ultrafilter, not a promised ordinary sequence. No topology or compactness assertion for the space of support functions is needed: taking a recession function need not preserve the metric convergence just used for profiles.

## 8. What the construction retains

The constant part of a proper profile disappears when taking its recession support function. Translation survives: multiplying the Fourier transform by \(e^{-ia\cdot\zeta}\) adds \(a\cdot\operatorname{Im}z\) to each profile, so it translates every associated compact set by \(a\). A smooth summand disappears before this final recession step, by Theorem 3.2. An identically zero distribution and a nonzero smooth compact distribution both give the collapsed profile, while a point mass gives a proper linear profile.

The next singular-support arguments can use the surjective projection theorem to preserve already chosen limits while adding an extra distribution. They must keep one common frequency sequence, or one common ultrafilter. This is the exact joint information that separate one-coordinate families cannot supply.

## References

1. Alex Kruckman, [*Notes on Ultrafilters*](https://akruckman.faculty.wesleyan.edu/files/2019/07/ultrafilters.pdf), Berkeley Math Toolbox Seminar, 7 November 2012. Background on filters and convergence.
2. Terence Tao, [*Ultrafilters, nonstandard analysis, and epsilon management*](https://terrytao.wordpress.com/2007/06/25/ultrafilters-nonstandard-analysis-and-epsilon-management/), *What's New*, 25 June 2007. Background on choosing one limiting procedure for many quantities.
3. Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983; second revised printing 1990; reprint 2005. The logarithmic Fourier observation and joint supporting-function construction are classical. All proofs, examples, solutions and illustrations in this lesson are supplied here or by the exact linked preceding lessons.
