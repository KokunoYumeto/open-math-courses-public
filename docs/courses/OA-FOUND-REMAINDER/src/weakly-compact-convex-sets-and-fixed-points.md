# Weakly compact convex sets and fixed points

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A Hilbert-space orbit has a distinguished point obtained by minimizing the norm of its closed convex hull. A general Banach norm can have flat faces, so this argument need not select a unique point. Weak compactness still supplies a common fixed point for a group of affine isometries. The proof below explains how a small portion near extreme points forces an averaged fixed point to be fixed by each of the maps being averaged.

We use the full strict separation proof in [Affine approximation and quasi-state spaces](../reader/affine-approximation-and-quasi-state-spaces.html#convex-separation-in-the-topology-being-used), Lemma 0.2. Norming, uniform boundedness, the equality of weak and norm closures of convex sets and norm-preserving extension from subspaces are proved in [Weak sequences and compact convex hulls](../reader/weak-sequences-and-convex-hull-compactness.html#0-banach-space-compactness-inputs), Lemmas 0.1–0.2. These basic arguments use no fixed-point or compact-hull conclusion from this lesson. We use ordinary compactness and the maximal principle for chains of closed faces. The category and extreme-point arguments needed below are proved here. Complex Banach spaces can be regarded as real spaces: real continuous linear functionals are real parts of complex ones, so this does not change their weak topology.

Throughout, weak means the Banach-space topology \(\sigma(X,X^*)\). A weak-star topology on a dual space can be strictly weaker; Exercise 7.3 shows why the distinction matters. Our argument is a classical proof of the Ryll-Nardzewski theorem. The geometric method is due to Namioka and Asplund; [Lurie] gives an accessible exposition.

Namioka and Asplund’s paper treats a broader locally convex noncontracting-semigroup setting. This lesson proves the Banach-space theorem for groups of affine isometries. The arguments include compact-face and compact-set extreme-point constructions, the category argument, the small-cap construction, Cesàro fixed points and the reduction from finite averages to an arbitrary group. In the small-cap construction, the coefficient of the large set is at least the chosen threshold inside the retained subset and is less than that threshold outside it. Lemma 2.1 maintains these bounds, and Lemma 1.2 supplies the compact-set extreme-point step when the omitted set contains nonextreme limit points.

## 1. Compactness, faces and extreme points

A weakly compact subset of a Banach space is norm bounded. Indeed every \(f\in X^*\) is bounded on that compact set. Apply uniform boundedness to its canonical images in \((X^*)^*\); their operator norms are their original norms.

We will use the category property of a compact Hausdorff space \(Z\): if \(Z\) is nonempty and is a countable union of closed sets, one of them has nonempty interior. Here is the argument. If closed sets \(D_n\) all had empty interior, begin with a nonempty open set and successively choose nonempty open sets \(V_n\) such that
\[
\overline V_n\subseteq V_{n-1}\setminus D_n.
\tag{1.1}
\]
Regularity of a compact Hausdorff space allows these choices. The nonempty compact sets \(\overline V_n\) are nested, so their intersection is nonempty. A point in it lies in none of the \(D_n\), contradicting the proposed covering.

Let \(K\) be a nonempty compact convex set in a Hausdorff locally convex space. A **face** of \(K\) is a convex subset \(F\) with the following property: if a point of an open segment between two points of \(K\) lies in \(F\), then both endpoints lie in \(F\). A point is **extreme** when its singleton is a face.

**Lemma 1.1.** Every nonempty closed face of \(K\) contains an extreme point of \(K\). Moreover \(K\) is the closed convex hull of its extreme points.

**Proof.** Among the nonempty closed faces contained in a given one, a descending chain has a nonempty intersection by compactness. The intersection is again a closed face. The maximal principle therefore gives a minimal such face \(F\). If \(F\) contained distinct points, a continuous real linear functional would distinguish them. Its maximizing set on \(F\) would be a proper nonempty closed face of \(F\), hence a face of \(K\). This contradicts minimality. Thus \(F\) is a singleton.

Write \(E=\operatorname{ext}K\) and \(C=\overline{\operatorname{co}}E\). The first assertion makes \(E\) nonempty. If some point of \(K\) were outside \(C\), separation would give a continuous real linear functional \(f\) with
\[
\max_K f>\sup_C f.
\]
The maximizing face of \(K\) contains an extreme point by the first assertion. This point also belongs to \(C\), a contradiction. \(\square\)

The next observation explains why an extreme point cannot be reconstructed entirely from a compact set that omits it.

**Lemma 1.2.** If \(A\subseteq K\) is compact and \(p\in\operatorname{ext}K\) belongs to \(\overline{\operatorname{co}}A\), then \(p\in A\).

**Proof.** Suppose \(p\notin A\). Choose an open balanced convex neighborhood \(V\) of zero whose closure is disjoint from \(A-p\). Such a neighborhood exists by local convexity, compactness of \(A\), and separation of \(p\) from each point of \(A\). Cover \(A\) by finitely many sets \(a_j+V\), with \(a_j\in A\). Put
\[
A_j=A\cap(a_j+\overline V),\qquad
C_j=\overline{\operatorname{co}}A_j.
\]
Each \(C_j\) is a compact convex subset of \(K\cap(a_j+\overline V)\): it is closed inside the compact set \(K\), and the translated neighborhood closure is closed and convex.

The convex join of the finitely many \(C_j\) is compact, being the image of their product with a finite-dimensional probability simplex. It is therefore closed and equals \(\overline{\operatorname{co}}A\). Express \(p\) as a convex combination of points in the \(C_j\). Extremality forces every point with a positive coefficient to equal \(p\). Thus \(p\in a_j+\overline V\) for some \(j\). Balancedness gives \(a_j\in p+\overline V\), contrary to the choice of \(V\). \(\square\)

In particular, if \(A\) is a compact subset of the weak closure of \(\operatorname{ext}K\) and omits one of those extreme points, its closed convex hull omits that point too.

## 2. Removing everything except a small part

We now combine the category property with the preceding two lemmas. Separability is needed only in this auxiliary result.

**Lemma 2.1.** Suppose \(K\subseteq X\) is weakly compact, convex and norm separable. Given \(\varepsilon>0\) with
\[
\operatorname{diam}K>\varepsilon,
\]
there is a nonempty proper weakly compact convex subset \(C\subset K\) such that
\[
\operatorname{diam}(K\setminus C)<\varepsilon.
\tag{2.1}
\]

**Proof.** Let \(Z=\overline{\operatorname{ext}K}^{\,w}\). Lemma 1.1 makes \(Z\) nonempty and gives \(K=\overline{\operatorname{co}}Z^{\,w}\). It is compact Hausdorff. Choose a countable norm-dense set in \(K\). The closed norm balls of radius \(\varepsilon/8\) about those points cover \(Z\), and each intersection with \(Z\) is weakly closed. Closed norm balls are weakly closed by Hahn–Banach. The category property gives a nonempty relatively weakly open set \(U\subseteq Z\) lying in one of these balls, say \(B\).

Set
\[
A=Z\setminus U,\qquad D=Z\cap B,\qquad
K_A=\overline{\operatorname{co}}A^{\,w},\qquad
K_D=\overline{\operatorname{co}}D^{\,w}.
\tag{2.2}
\]
If \(A\) were empty, then \(Z\subseteq B\) and hence \(K\subseteq B\), which would give \(\operatorname{diam}K\leq\varepsilon/4\). Thus \(A\) is nonempty. Both \(A\) and \(D\) are compact; both convex hull closures in (2.2) are weakly compact because they are closed subsets of \(K\). Also \(K_D\subseteq B\), so
\[
\operatorname{diam}K_D\leq\varepsilon/4.
\tag{2.3}
\]

Because \(A\cup D=Z\), compactness of the convex join gives
\[
K=\{t a+(1-t)d:a\in K_A,\ d\in K_D,\ 0\leq t\leq1\}.
\tag{2.4}
\]
The relatively open set \(U\) meets \(\operatorname{ext}K\), since the latter is dense in \(Z\). Choose an extreme point \(p\in U\). Lemma 1.2 applied to the compact set \(A\) gives \(p\notin K_A\).

Write \(R=\operatorname{diam}K\); it is finite and positive. Choose \(0<\delta<1\) with \(2\delta R<\varepsilon/2\), and define
\[
C=\{t a+(1-t)d:a\in K_A,\ d\in K_D,\ \delta\leq t\leq1\}.
\tag{2.5}
\]
This set is nonempty and weakly compact. It is convex: in a convex combination of two displayed expressions, the new coefficient of \(K_A\) is a convex combination of their coefficients and remains at least \(\delta\); regroup the \(K_A\) and \(K_D\) terms using their convexity. A vanishing coefficient of \(K_D\) causes no difficulty.

The point \(p\) is outside \(C\). Indeed a representation in (2.5), together with extremality, would force \(p=a\in K_A\) because \(t>0\). Thus \(C\) is proper.

Every \(y\in K\setminus C\) has a representation in (2.4) with \(t<\delta\); otherwise it would belong to \(C\). Its distance from the corresponding \(d\) is at most \(tR<\delta R\). Consequently for \(y,y'\in K\setminus C\), using (2.3),
\[
\|y-y'\|<2\delta R+\varepsilon/4<\varepsilon.
\]
This proves (2.1). \(\square\)

The conclusion does not say that \(C\) is invariant under any action. Its purpose is to make two orbit points outside \(C\) necessarily close in norm.

## 3. One affine map has a fixed point

**Lemma 3.1.** A weakly continuous affine map \(T:K\to K\) on a nonempty weakly compact convex subset of a Banach space has a fixed point.

**Proof.** Fix \(z\in K\) and consider its successive averages
\[
z_n=\frac1n\sum_{j=0}^{n-1}T^jz\in K.
\tag{3.1}
\]
Affineness gives
\[
Tz_n-z_n=\frac{T^nz-z}{n}.
\tag{3.2}
\]
Since \(K\) is norm bounded, the right side tends to zero in norm. A subnet of \((z_n)\) converges weakly to some \(z_\infty\in K\). Weak continuity of \(T\) and (3.2) give \(Tz_\infty=z_\infty\). \(\square\)

No isometry hypothesis was used here. For several maps that do not commute, their average can have a fixed point without an immediate reason for each map to fix it. The next argument supplies that reason when the maps belong to a group of isometries.

## 4. An averaged fixed point is fixed by each isometry

**Proposition 4.1.** Let a group \(G\) act on a nonempty weakly compact convex set \(K\subseteq X\) by weakly continuous affine bijections preserving norm distances. For \(g_1,\ldots,g_m\in G\) and positive numbers \(\lambda_i\) summing to one, a point \(x\in K\) satisfying
\[
x=\sum_{i=1}^m\lambda_i g_i x
\tag{4.1}
\]
is fixed by every \(g_i\).

**Proof.** Suppose some \(g_i\) moves \(x\). Remove the indices which fix \(x\) from (4.1), subtract their terms, and divide by the sum of the remaining coefficients. This leaves an equation of the same form with positive coefficients, and now every listed map moves \(x\).

Let \(H\) be the subgroup generated by these finitely many maps. It is countable. Its orbit \(Hx\) is countable, and
\[
L=\overline{\operatorname{co}}^{\,w}(Hx)
\tag{4.2}
\]
is a nonempty weakly compact convex subset of \(K\). It is invariant under \(H\), using weak continuity and the inverse of each group element. It is norm separable: weak and norm closures of a convex set agree, and rational convex combinations of the countable orbit are norm dense in its convex hull closure. This uses no separability assumption on \(X\) or on the original \(K\).

Choose
\[
0<\varepsilon<\min_i\|g_i x-x\|.
\tag{4.3}
\]
The diameter of \(L\) exceeds \(\varepsilon\). Lemma 2.1 gives a proper weakly closed convex subset \(C\subset L\) with \(\operatorname{diam}(L\setminus C)<\varepsilon\). Since the closed convex hull of \(Hx\) is \(L\), the orbit cannot be contained in \(C\). Choose \(h\in H\) with \(hx\notin C\). Apply this affine map to (4.1):
\[
hx=\sum_i\lambda_i h g_i x.
\tag{4.4}
\]
At least one \(hg_i x\) is outside \(C\), since otherwise convexity would put \(hx\) in \(C\). Both these points belong to \(L\setminus C\). The isometry property therefore gives
\[
\|g_i x-x\|=\|hg_i x-hx\|<\varepsilon,
\]
contradicting (4.3). Thus no listed map moves \(x\). \(\square\)

## 5. The common fixed point theorem

**Theorem 5.1 (Ryll-Nardzewski, group form).** Under the hypotheses of Proposition 4.1, there is a point of \(K\) fixed by all of \(G\).

**Proof.** Given any finite list \(g_1,\ldots,g_m\), its average
\[
T(y)=\frac1m\sum_i g_i y
\]
is a weakly continuous affine map from \(K\) into \(K\). Lemma 3.1 supplies a fixed point of \(T\); Proposition 4.1 says this point is fixed by each \(g_i\). Each set
\[
\operatorname{Fix}_K(g)=\{y\in K:gy=y\}
\]
is weakly closed. They have the finite intersection property, so compactness of \(K\) makes their total intersection nonempty. \(\square\)

The group may be uncountable. The countable group and separable convex set appeared only inside the proof for a finite list. Bounded affine isometries of a Banach space restrict to actions of the type used here: their linear parts are bounded and hence weakly continuous, and translations are weakly continuous too.

## 6. The predual application

Let \(M\) be a von Neumann algebra and \(G\subseteq\operatorname{Aut}(M)\). Its predual \(M_*\) is a Banach space. For each \(g\), the pullback
\[
T_g\varphi=\varphi\circ g^{-1}
\]
is a surjective linear isometry of \(M_*\), so it is weakly continuous. If a normal state has a weakly compact convex orbit hull \(K\) in \(M_*\), Theorem 5.1 gives an invariant normal state in \(K\). Positivity and value one at the unit are preserved on that hull, since both conditions are weakly closed.

This is the fixed-point step in [Invariant states and ergodic projections](../reader/invariant-states-and-ergodic-projections.html), Theorem 4.1. It requires compactness for \(\sigma(M_*,M)\), not merely compactness in the full dual \(M^*\) for pointwise evaluation on \(M\). When one starts with a relatively weakly compact orbit, Theorem 4.1 of [Weak sequences and compact convex hulls](../reader/weak-sequences-and-convex-hull-compactness.html) supplies the compactness of its closed convex hull. The fixed-point proof above starts with a compact convex set already provided and does not use that separate theorem.

The same fixed-point result supplies the invocation in Theorem 4.7 of [Traces, part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html). The weak compactness of the trace-conjugacy hull in that theorem has its own hypotheses and proof dependencies.

## 7. Exercises with complete solutions

**Exercise 7.1 — Basic: affine symmetries in a flat norm.** On \(\mathbb R^2\) use the maximum norm and the rectangle \(K=[1,3]\times[-2,2]\). Define
\[
g(s,t)=(4-s,t),\qquad h(s,t)=(s,-t).
\]
Verify the hypotheses of Theorem 5.1 for the group they generate, find its common fixed point, and compute the average map \((g+h)/2\).

**Solution.** The rectangle is nonempty, compact and convex; in finite dimension its weak and usual topologies agree. Both maps are affine continuous involutions preserving \(K\). On differences they change one coordinate's sign, hence preserve the maximum norm. They commute, so their group has the four elements \(1,g,h,gh\). The equations \(g(s,t)=(s,t)\) and \(h(s,t)=(s,t)\) give \(s=2\) and \(t=0\). This is the unique common fixed point. Direct calculation gives
\[
\tfrac12(g(s,t)+h(s,t))=(2,0).
\]
In this example averaging identifies the point immediately, even though the norm is not strictly convex. In the general theorem Proposition 4.1 is what justifies passing from a fixed point of an average to the individual fixed-point equations.

**Exercise 7.2 — Intermediate: the same orbit in two Banach spaces.** For \(1\leq p<\infty\), let \(e_n\) be the unit vectors in \(\ell^p(\mathbb N)\), and let all permutations of \(\mathbb N\) act by permuting coordinates. Compare the norm-closed convex hull of \(\{e_n\}\) for \(p=2\) and \(p=1\). Show that the first has a common fixed point and the second is not weakly compact.

**Solution.** In \(\ell^2\) the hull is
\[
K_2=\left\{a:a_n\geq0,\ \sum_n a_n\leq1\right\}.
\tag{7.1}
\]
The right side is weakly closed: impose positivity coordinatewise and require \(\sum_{n\in F}a_n\leq1\) for every finite set \(F\). It lies in the Hilbert-space unit ball, which is weakly compact by the Riesz representation theorem and Banach–Alaoglu. Thus it is weakly compact and contains the norm-closed hull.

For the reverse inclusion, truncate \(a\in K_2\) to its first \(N\) coordinates. Write \(c_N=1-\sum_{n\leq N}a_n\geq0\). Distribute this missing mass equally among \(m\) further coordinates. The resulting finitely supported vector is a convex combination of unit vectors, and its distance from \(a\) is at most
\[
\|(a_n)_{n>N}\|_2+c_N/\sqrt m.
\]
First take \(N\) large and then \(m\) large. This proves (7.1). In particular the averages of \(e_1,\ldots,e_m\) tend to zero in \(\ell^2\). A vector fixed by all permutations has equal coordinates, so the only such \(\ell^2\) vector is zero. It is the unique common fixed point in \(K_2\).

In \(\ell^1\) the hull instead equals
\[
K_1=\left\{a:a_n\geq0,\ \sum_n a_n=1\right\}.
\tag{7.2}
\]
The displayed set is norm closed and contains every convex combination of unit vectors. Conversely, truncate a probability vector and put its remaining mass at one further coordinate; the \(\ell^1\) error is at most twice the tail mass. This proves (7.2).

The sequence \((e_n)\) has no weakly convergent subnet in \(\ell^1\). Any subnet converging weakly would have every coordinate zero in its limit, since each fixed coordinate eventually vanishes. Its limit would therefore be zero. But the bounded functional \(a\mapsto\sum_n a_n\) has value one along the entire subnet. This is impossible. Hence \(K_1\) is not weakly compact. A permutation-fixed probability vector also cannot exist: equal nonnegative coordinates either sum to zero or have infinite sum. Norm boundedness and norm-closed convexity alone do not replace weak compactness.

**Exercise 7.3 — Advanced: weak-star compactness is insufficient.** Let \(F_2\) be the free group on generators \(a,b\), and let
\[
K=\{\mu\in\ell^\infty(F_2)^*: \mu\geq0,\ \mu(1)=1\}.
\]
Show that \(K\) is weak-star compact and that left translations act on it by affine isometries. Prove directly that this action has no common fixed point. Conclude that \(K\) is not compact for the Banach-space weak topology of \(\ell^\infty(F_2)^*\).

**Solution.** Positive unital functionals have norm one. Positivity and the equation \(\mu(1)=1\) are weak-star closed, so Banach–Alaoglu makes \(K\) compact. It is nonempty, since evaluation at any group element belongs to it. For \(g\in F_2\), set
\[
(g\mu)(f)=\mu\bigl(h\mapsto f(gh)\bigr).
\]
These maps form a group, preserve positivity and the value at one, and are surjective linear isometries because left translation bijectively preserves the unit ball of \(\ell^\infty(F_2)\). They are continuous for both the weak-star topology and the Banach-space weak topology.

Suppose a common fixed point existed. For a subset \(E\subseteq F_2\), write \(\mu(E)=\mu(1_E)\). This gives a finitely additive probability on all subsets, invariant under left translation. Every singleton has the same mass; that mass is zero, since the group contains arbitrarily large finite sets.

For each letter \(s\in\{a,a^{-1},b,b^{-1}\}\), let \(W_s\) be the nonempty reduced words beginning with \(s\). The group is the disjoint union of its identity and these four sets. Therefore
\[
\mu(W_a)+\mu(W_{a^{-1}})+\mu(W_b)+\mu(W_{b^{-1}})=1.
\tag{7.3}
\]
Cancellation of the first letter gives the disjoint decompositions
\[
F_2=W_a\sqcup aW_{a^{-1}},\qquad
F_2=W_b\sqcup bW_{b^{-1}}.
\tag{7.4}
\]
For example, multiplying a word starting with \(a^{-1}\) by \(a\) removes that initial letter and produces exactly the words not starting with \(a\), including the identity. Translation invariance and (7.4) give
\[
\mu(W_a)+\mu(W_{a^{-1}})=1,\qquad
\mu(W_b)+\mu(W_{b^{-1}})=1.
\]
Their sum contradicts (7.3). There is no common fixed point. If \(K\) were Banach-space weakly compact, Theorem 5.1 would apply to these affine isometries and produce one. Thus this weak-star compact set is not weakly compact.

## References

[Lurie] J. Lurie, *Math 261y: von Neumann Algebras*, Lecture 26, November 1, 2011, [author-hosted lecture notes](https://www.math.ias.edu/~lurie/261ynotes/lecture26.pdf). Lemma 2.1 keeps the small-cap coefficient bounds consistent: the large-set coefficient is at least the threshold inside the retained subset and less than it outside, correcting the mismatched coefficient in part (ii) of the notes’ proof.

[Namioka–Asplund] I. Namioka and E. Asplund, “A geometric proof of Ryll-Nardzewski's fixed point theorem,” *Bulletin of the American Mathematical Society* **73** (1967), 443–445, [free AMS article](https://www.ams.org/journals/bull/1967-73-03/S0002-9904-1967-11779-8/S0002-9904-1967-11779-8.pdf), [DOI](https://doi.org/10.1090/S0002-9904-1967-11779-8). The paper treats a broader locally convex noncontracting-semigroup setting.
