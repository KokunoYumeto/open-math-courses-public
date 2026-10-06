# Weak sequences and compact convex hulls

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

An orbit of normal functionals may have weakly compact closure before it is convex. Averaging requires its closed convex hull. This lesson proves that passage, together with the sequence criterion used to test weak compactness. Neither theorem assumes a separable Banach space.

The Banach-space prerequisites are proved in Section 0 below, using only the full algebraic Hahn–Banach and strict separation arguments in [Affine approximation and quasi-state spaces](../reader/affine-approximation-and-quasi-state-spaces.html#convex-separation-in-the-topology-being-used), Lemmas 0.1–0.2, and the full [Baire proof](../reader/fredholm-operators-and-stable-index.html#why-the-partial-inverse-is-bounded), Lemma 0.1. Only these independently proved subsections are inputs; no affine compact-hull result is used to prove its own prerequisites. The product compactness theorem of ordinary topology is also used. We use Theorem 2.2 and Proposition 2.3 of [Haar measure on locally compact groups](../../harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups.html#oa-fnd-hm-01), restricted to a compact Hausdorff space \(L\): the positive functionals of value one on the constant function in \(C(L)\) are integration against Radon probability measures. Their proof constructs an outer measure and uses Carathéodory's outer-measure theorem to obtain a countably additive Borel measure; it then identifies the integrals and proves regularity on finite-measure Borel sets. Its needed continuous cutoffs and finite partitions are in that lesson's topology tools; Theorem 5.1 of [The Stone–Weierstrass theorem](../../foundations-of-von-neumann-algebras/support/function-algebras.html#oa-fnd-sw-16) also proves the compact-space cutoff theorem directly. Countable additivity gives the continuity from below used here. No group structure on \(L\) is involved. The finite-sum construction below proves the vector-valued integration assertion it needs.

Whitley’s freely readable 1986 paper gives a concise convex-hull argument using Eberlein–Šmulian and scalar integration. Here Theorem 2.1 proves the sequence criterion directly, and Lemma 3.1 constructs each barycenter as a norm limit of finite convex combinations, with an explicit error bound. Whitley’s 1967 paper provides further scholarly context for the sequence theorem.

Write \(J:X\to X^{**}\) for the canonical isometry, \((Jx)(f)=f(x)\). Weak means \(\sigma(X,X^*)\); weak-star on the bidual means \(\sigma(X^{**},X^*)\). We allow real or complex scalars. Convex combinations always have nonnegative real coefficients.

## 0. Banach-space compactness inputs

**Lemma 0.1 (Norming and weak closures).** Every bounded linear functional on a subspace of a real or complex normed space extends to the whole space with the same norm. Consequently

\[
\|x\|=\sup_{f\in B_{X^*}}|f(x)|,
\]

the map \(J\) is isometric, every norm-closed convex set is weakly closed, and a convex set has the same norm and weak closures. The relative weak topology on a linear subspace is its own weak topology.

**Proof.** For a real functional \(g\) of norm \(c\), apply the cited algebraic Hahn–Banach argument to the sublinear function \(p(x)=c\|x\|\). The resulting extension \(G\) satisfies \(G(x)\leq c\|x\|\) and, on applying this to \(-x\), \(|G(x)|\leq c\|x\|\). Its norm equals that of its restriction.

For a complex functional \(g\), first extend \(\operatorname{Re}g\) as a real functional \(G\) with this same bound. Define \(f(x)=G(x)-iG(ix)\). Real linearity gives \(f(ix)=if(x)\), so \(f\) is complex linear; on the original subspace this formula equals \(g\). Given \(x\), choose a scalar \(\lambda\) of modulus one with \(\lambda f(x)=|f(x)|\). Then \(|f(x)|=G(\lambda x)\leq c\|x\|\). Thus it is a norm-preserving extension.

For nonzero \(x\), the functional on its scalar span taking \(x\) to \(\|x\|\) has norm one. Extending it proves the displayed norm equality; the opposite inequality follows from the definition of the dual norm. The same equality proves that \(J\) is isometric.

If \(x\) is outside a norm-closed convex set \(C\), strict separation of the compact singleton \(\{x\}\) from \(C\) supplies a real continuous linear functional separating them. In the complex case it is the real part of a complex functional, by the formula just used. This gives a weak neighborhood of \(x\) disjoint from \(C\), so \(C\) is weakly closed. Empty sets cause no exception. The norm closure of a convex set is convex and therefore weakly closed; together with the fact that the weak topology is weaker than the norm topology, this gives equality of the two closures. Finally, every subspace functional extends, and every restriction of a whole-space functional is continuous on the subspace. Their tests therefore define the same relative weak topology. \(\square\)

**Lemma 0.2 (Uniform boundedness).** Let \(Y\) be Banach and \(Z\) normed. If a family \(\mathcal T\) of bounded linear maps \(Y\to Z\) satisfies \(\sup_{T\in\mathcal T}\|Ty\|<\infty\) for every \(y\in Y\), then \(\sup_{T\in\mathcal T}\|T\|<\infty\). In particular every weakly compact subset of a normed space is norm bounded.

**Proof.** For positive integers \(n\), the sets

\[
E_n=\{y:\|Ty\|\leq n\text{ for every }T\in\mathcal T\}
\]

are closed and cover \(Y\). The full Baire argument cited above gives an open ball \(B(y_0,r)\subseteq E_N\). For \(\|h\|<r\) and \(T\in\mathcal T\), both \(y_0+h\) and \(y_0\) belong to \(E_N\), and hence \(\|Th\|\leq2N\). Substituting \(h=tv\) for \(\|v\|=1\) and \(0<t<r\), then letting \(t\) tend to \(r\), gives \(\|T\|\leq2N/r\), uniformly in \(T\). The zero-space and empty-family cases are immediate.

For the final assertion, \(X^*\) is Banach even when \(X\) is incomplete: a norm-Cauchy sequence of functionals has a pointwise linear limit, with the same uniform bounds, and the Cauchy estimates on the unit ball give norm convergence to that limit. If \(K\subseteq X\) is weakly compact, each \(f\in X^*\) is bounded on \(K\). Apply the first assertion on \(Y=X^*\) to the evaluation maps \(Jk:X^*\to\mathbb F\), \(k\in K\). Lemma 0.1 gives \(\|Jk\|=\|k\|\), proving the required bound. \(\square\)

**Lemma 0.3 (Banach–Alaoglu).** For any normed space \(E\), its dual closed unit ball is compact for \(\sigma(E^*,E)\). Every dual ball of finite radius is compact in that topology as well.

**Proof.** Put \(D_x=\{z\in\mathbb F:|z|\leq\|x\|\}\) for \(x\in E\). Each disk is compact. The product compactness theorem makes \(P=\prod_{x\in E}D_x\) compact in its product topology. Inside it, impose all the closed equations

\[
a_{x+y}=a_x+a_y,\qquad a_{\lambda x}=\lambda a_x
\quad(x,y\in E,\ \lambda\in\mathbb F).
\]

Their common solution set is closed and therefore compact. Its points are exactly the linear functions \(f(x)=a_x\) with \(|f(x)|\leq\|x\|\), hence exactly \(B_{E^*}\). The restricted product topology is convergence on each \(x\), which is the weak-star topology in the statement. Scaling gives any positive finite radius; the radius-zero ball is a singleton. Completeness of \(E\) is not needed. Applying this with \(E=X^*\) gives precisely the bidual compactness used in Theorem 2.1. \(\square\)

## 1. Countably many tests on a separable part

**Lemma 1.1.** If \(V\) is a finite-dimensional subspace of \(X^{**}\), there is a finite set \(F\subseteq B_{X^*}\) such that

\[
\|v\|\leq2\max_{f\in F}|v(f)|\qquad(v\in V).
\]

If \(Y\) is a separable normed space, a countable set of functionals in \(B_{Y^*}\) separates its points. Every weakly compact subset of \(Y\) is metrizable for its weak topology.

**Proof.** For each unit vector \(v\in V\), the definition of the bidual norm gives \(f_v\in B_{X^*}\) with \(|v(f_v)|>3/4\). The same value exceeds \(1/2\) on a sufficiently small norm neighborhood of \(v\) in the unit sphere. That sphere is compact, so finitely many of these neighborhoods cover it. Their functionals give the inequality by homogeneity. When \(V=\{0\}\), a single zero functional suffices.

For nonzero separable \(Y\), choose a dense sequence \((y_j)\) in its unit sphere and \(f_j\in B_{Y^*}\) with \(f_j(y_j)=1\), using Hahn–Banach. If \(\|y\|=1\), choose \(j\) with \(\|y-y_j\|<1/2\); then \(|f_j(y)|>1/2\). Thus the \(f_j\) separate points. The map

\[
y\longmapsto(f_1(y),f_2(y),\ldots)
\]

is a continuous injection from a weakly compact set into a countable product of scalar spaces. A continuous bijection from a compact space to a Hausdorff image is a homeomorphism: images of closed sets are compact and hence closed. The product is metrizable, so the compact set is metrizable. The zero space is immediate. \(\square\)

The relative weak topology on a norm-closed subspace \(Y\subseteq X\) is its own weak topology. Every functional in \(Y^*\) extends to \(X^*\), and every restriction from \(X^*\) belongs to \(Y^*\).

## 2. The sequence criterion

**Theorem 2.1 (Eberlein–Šmulian).** For \(A\subseteq X\), where \(X\) is Banach, the following are equivalent:

1. The weak closure of \(A\) is weakly compact.
2. Every sequence in \(A\) has a subsequence converging weakly to an element of \(X\).
3. Every sequence in \(A\) has a weak cluster point in \(X\): each neighborhood of that point meets arbitrarily late terms.

The limit in assertion 2 need not belong to \(A\).

**Proof of 1 implies 2.** For a sequence \((a_n)\subseteq A\), let \(Y\) be its norm-closed linear span. It is separable and weakly closed. The intersection of \(Y\) with the compact weak closure of \(A\) is therefore weakly compact, and its topology agrees with the weak topology of \(Y\). Lemma 1.1 makes it a compact metric space. Every sequence in a compact metric space has a convergent subsequence: successive finite covers by balls of radii \(2^{-m}\) select nested infinite sets of indices, and a diagonal selection is Cauchy and has a limit. Its convergence here is weak convergence in \(X\).

**Proof of 2 implies 3.** The limit of a convergent subsequence is a cluster point in the stated sense.

**Proof of 3 implies 1.** For every \(f\in X^*\), its values on \(A\) are bounded. Otherwise choose \(a_n\in A\) with \(|f(a_n)|>n\); continuity of \(f\) makes a weak cluster point impossible. Uniform boundedness, applied to \(J(A)\) on the Banach space \(X^*\), makes \(A\) norm bounded. Banach–Alaoglu now makes

\[
L=\overline{J(A)}^{\,\sigma(X^{**},X^*)}
\]

compact: it is closed inside a bounded weak-star compact ball. We show \(L\subseteq J(X)\). Empty \(A\) is harmless; suppose \(z\in L\).

Choose \(a_1\in A\). Inductively let

\[
V_n=\operatorname{span}\{z,Ja_1,\ldots,Ja_n\}
\]

and choose a finite norming set for \(V_n\) by Lemma 1.1. Let \(F_n\) be the union of that set with all previously chosen sets. Since \(z\in L\), choose \(a_{n+1}\in A\) with

\[
|f(a_{n+1})-z(f)|<\frac1{n+1}\qquad(f\in F_n).
\]

Put \(F=\bigcup_nF_n\) and \(V=\overline{\bigcup_nV_n}^{\|\cdot\|}\). Passing to norm limits in the finite-dimensional estimates gives

\[
\|v\|\leq2\sup_{f\in F}|v(f)|\qquad(v\in V).
\]

For each fixed \(f\in F\), the chosen scalar values satisfy \(f(a_n)\to z(f)\). Assertion 3 supplies a weak cluster point \(a\in X\). It belongs to the norm-closed span of \((a_n)\), because that subspace is weakly closed. The scalar convergence and continuity of \(f\) force \(f(a)=z(f)\): if these values differed, a neighborhood of \(a\) defined by \(f\) would miss all sufficiently late terms. Hence \(Ja\in V\). Applying the norming estimate to \(Ja-z\) gives \(Ja=z\).

Thus \(L\subseteq J(X)\). On \(J(X)\) the relative weak-star topology is exactly the weak topology of \(X\), so \(J^{-1}(L)\) is a weakly compact set containing \(A\). Its closed subset \(\overline A^{\rm weak}\) is compact. \(\square\)

The construction makes countably many tests for one prescribed bidual point. It does not assert that the weak topology of the whole Banach space is metrizable.

## 3. Barycenters stay in a separable Banach space

**Lemma 3.1.** Let \(Y\) be separable and Banach, and let \(K\subseteq Y\) be nonempty and weakly compact. Its norm-closed convex hull is weakly compact.

**Proof.** Let \(R=\sup_{k\in K}\|k\|<\infty\), by uniform boundedness. Regard \(K\) as a compact space with its weak topology. Let \(P(K)\) be its Radon probability measures, with the topology of their integrals against continuous functions. Riesz representation identifies \(P(K)\) with the positive functionals of value one on \(1\) in \(C(K)^*\). It is a weak-star closed subset of the dual unit ball, so Banach–Alaoglu makes it compact.

We construct the barycenter of each \(\mu\in P(K)\) in \(Y\). Norm-closed balls are weakly closed, by separation. A norm-open ball is the countable union of concentric closed balls of smaller radii, so it is weakly Borel. Since \(Y\) is separable, this also makes every norm-open subset weakly Borel. Choose a norm-dense sequence \((k_j)\) in \(K\).

Fix \(\eta>0\). Partition \(K\) into disjoint Borel sets

\[
A_j=\{k\in K:\|k-k_j\|<\eta\}
\mathbin{\big\backslash}\bigcup_{i<j}\{k\in K:\|k-k_i\|<\eta\}.
\]

Their union is \(K\). Choose \(N\) so that the remaining set \(B=K\setminus\bigcup_{j\leq N}A_j\) has \(\mu(B)<\eta/(1+2R)\), by countable additivity. The vector

\[
b_\eta=\sum_{j\leq N}\mu(A_j)k_j+\mu(B)k_1
\]

is a finite convex combination of points of \(K\). For \(f\in Y^*\), integrating the differences on the sets of this partition gives

\[
\left|f(b_\eta)-\int_Kf(k)\,d\mu(k)\right|
\leq\|f\|\bigl(\eta+2R\mu(B)\bigr)<2\eta\|f\|.
\]

Take \(\eta=2^{-m}\). For two such approximants, Hahn–Banach norming gives

\[
\|b_{2^{-m}}-b_{2^{-l}}\|
\leq2(2^{-m}+2^{-l}).
\]

Completeness supplies a limit \(b(\mu)\in Y\), and

\[
f(b(\mu))=\int_K f(k)\,d\mu(k)\qquad(f\in Y^*).
\]

These identities determine the vector uniquely, independently of the partitions and choices. They also show that \(b:P(K)\to Y\) is continuous for the weak topology, because every \(f|_K\) is continuous. It is affine, and \(b(\delta_k)=k\).

Its image \(D\) is therefore weakly compact and convex and contains \(K\). Being weakly closed, it contains the norm-closed convex hull of \(K\). Conversely every barycenter was a norm limit of finite convex combinations, so \(D\) is contained in that hull. They are equal. \(\square\)

Only the temporary space \(Y\) was separable. The original set need not be norm compact, and no norm-open ball was assumed to be weakly open.

## 4. Convexification in an arbitrary Banach space

**Theorem 4.1 (Krein).** If \(K\) is weakly compact in a Banach space \(X\), then

\[
C=\overline{\operatorname{co}K}^{\|\cdot\|}
 =\overline{\operatorname{co}K}^{\rm weak}
\]

is weakly compact.

**Proof.** The equality follows from Hahn–Banach separation. For empty \(K\), both hulls are empty and compact. Otherwise take a sequence \((x_n)\subseteq C\). For each \(n,m\geq1\), choose a finite convex combination \(c_{n,m}\) of points of \(K\) with \(\|x_n-c_{n,m}\|<2^{-m}\). The points appearing in all these combinations form a countable set \(S\subseteq K\).

Let \(Y=\overline{\operatorname{span}S}^{\|\cdot\|}\). It is a closed separable Banach subspace, hence weakly closed. Thus \(K_0=K\cap Y\) is weakly compact in \(Y\). Every \(x_n\) lies in the norm-closed convex hull of \(K_0\), which is weakly compact by Lemma 3.1. Theorem 2.1 gives a subsequence converging weakly in \(Y\), hence in \(X\). Its limit lies in \(C\), since \(C\) is weakly closed.

Every sequence in \(C\) therefore has a weakly convergent subsequence. Theorem 2.1 makes \(C\) relatively weakly compact; its weak closedness makes it compact. \(\square\)

For a relatively weakly compact set, first take its weak closure. The same conclusion holds for its closed convex hull.

## 5. Use in the normal-functional arguments

Theorem 4.1 supplies the convex-hull step in Section 4 of [Invariant states and ergodic projections](../reader/invariant-states-and-ergodic-projections.html). Its orbit lives in the Banach space \(M_*\), whose weak topology is \(\sigma(M_*,M)\). The resulting compact convex hull is the domain for Theorem 5.1 of [Weakly compact convex sets and fixed points](../reader/weakly-compact-convex-sets-and-fixed-points.html).

Theorem 2.1 also supplies the sequence criterion invoked in the existing Akemann proof: Theorem 10.2, implication 3 to 1, in [Polar decomposition and weak compactness in preduals](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-17). That proof starts with a bounded family uniformly small on decreasing sequences of projections. For a chosen sequence of functionals it builds one positive normal functional controlling their supports, proves that a bidual cluster point is completely additive, and hence proves that it is normal. Theorem 2.1 then converts that sequence argument to relative weak compactness of the whole family. This is the criterion used in Step 2 of Theorem 4.7 of [Traces, part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html#oa-fnd-ta-10).

These are applications and reading references. The proofs of Sections 1–4 require none of the operator-algebra results cited in this section. The Akemann argument uses the cluster-point form of Theorem 2.1 and retains its own predual, polar-support and normality prerequisites.

## 6. Graded exercises with complete solutions

### Exercise 6.1 — An uncountable weakly compact hull (basic)

For an infinite set \(\Gamma\), let \(e_\gamma\) be the unit vectors of \(\ell^2(\Gamma)\). Prove that \(K=\{0\}\cup\{e_\gamma:\gamma\in\Gamma\}\) is weakly compact and identify its closed convex hull. Show that the hull is not norm compact. If \(\Gamma\) is uncountable, show that its weak topology is not metrizable.

**Solution.** Every vector \(h\in\ell^2(\Gamma)\) has only finitely many coordinates of modulus at least any prescribed positive number. Consequently every weak neighborhood of \(0\) contains all but finitely many of the \(e_\gamma\). Each \(e_\gamma\) is isolated in \(K\) by its coordinate functional. In any open cover, a member containing \(0\) leaves only finitely many unit vectors to cover. This proves compactness.

The hull is

\[
C=\left\{x\in\ell^2(\Gamma):x_\gamma\geq0,\ 
\sup_{F\subseteq\Gamma,\ F\text{ finite}}\sum_{\gamma\in F}x_\gamma\leq1\right\}.
\]

The displayed inequalities persist under norm limits of convex combinations. Conversely, a vector in this set has countable support: the sets of coordinates of modulus at least \(1/n\) are finite. Its finite truncations converge in \(\ell^2\) and are convex combinations of the corresponding unit vectors and \(0\). Thus this is the norm-closed convex hull. Theorem 4.1 makes it weakly compact. Distinct unit vectors have norm distance \(\sqrt2\), so it is not norm compact.

If the weak topology had a countable neighborhood base at \(0\), choose inside each member a basic neighborhood determined by finitely many dual vectors. Their supports have countable union. Choose \(\gamma\) outside that union. Then \(e_\gamma\) lies in every member of the proposed base, whereas the weak neighborhood \(\{x:|x_\gamma|<1/2\}\) excludes it. This contradicts the defining refinement property of a base. Hence the weak topology is not metrizable.

### Exercise 6.2 — Why completeness is needed (intermediate)

Equip the finite-support space \(E=c_{00}(\mathbb N)\) with the \(\ell^2\) norm. Show that \(K=\{0\}\cup\{e_n/n:n\geq1\}\) is norm compact in \(E\), but that its norm-closed convex hull in \(E\) is not weakly compact.

**Solution.** The sequence \(e_n/n\) converges to \(0\) in norm, so the same finite-cover argument as for a convergent sequence proves norm compactness. For each \(N\), the vector

\[
x_N=\sum_{n=1}^N\frac{2^{-n}}n e_n
\]

is a convex combination of points of \(K\), assigning the remaining weight to \(0\). If its hull were weakly compact, the sequence, regarded as a net, would have a convergent subnet with limit \(x\in E\). Every coordinate functional is continuous for the \(\ell^2\) norm. Its values along every subnet therefore force \(x_n=2^{-n}/n\) for all \(n\). That vector has infinite support and does not belong to \(E\), a contradiction. The ambient completion contains this limit, while the incomplete space does not. This pinpoints the role of Banach completeness in Lemma 3.1 and Theorem 4.1.

### Exercise 6.3 — Weakly compact synthesis maps (advanced)

Let \((k_i)_{i\in I}\) be a bounded family in a Banach space \(X\). Define

\[
T:\ell^1(I)\longrightarrow X,\qquad Ta=\sum_{i\in I}a_i k_i.
\]

Prove that \(T\) is weakly compact, meaning that the image of its closed unit ball is relatively weakly compact, exactly when the family \(\{k_i:i\in I\}\) is relatively weakly compact. Give a weakly compact synthesis map that is not compact in norm.

**Solution.** An \(\ell^1(I)\) vector has countable support, and the sum converges in norm with bound \(\|Ta\|\leq R\|a\|_1\), where \(R=\sup_i\|k_i\|\). If \(T\) is weakly compact, its columns \(Te_i=k_i\) belong to the image of its unit ball and are relatively weakly compact.

Conversely let \(K\) be the weakly compact closure of the columns. Over the real field, let \(S=K\cup(-K)\cup\{0\}\). Over the complex field, let \(S=\{\lambda k:|\lambda|=1,\ k\in K\}\cup\{0\}\). The scalar multiplication map from the unit circle times \(K\) is weakly continuous, as seen by applying each functional, so \(S\) is weakly compact in either case. Theorem 4.1 makes its closed convex hull \(D\) weakly compact.

For \(\|a\|_1\leq1\), each finite partial sum of \(Ta\) belongs to \(D\): use weights \(|a_i|\), vectors \((a_i/|a_i|)k_i\) for the nonzero coefficients, and place the remaining weight on \(0\). The norm limit \(Ta\) also belongs to \(D\). Thus \(T(B_{\ell^1(I)})\subseteq D\), proving weak compactness.

Take \(I=\mathbb N\), \(X=\ell^2\), and \(k_i=e_i\). Exercise 6.1 supplies their relatively weakly compact closure, so the inclusion \(\ell^1\to\ell^2\) is weakly compact. Its unit-ball image contains the unit vectors, at pairwise distance \(\sqrt2\), and is therefore not relatively norm compact. No countability restriction on \(I\) was needed in the equivalence.

## References

[Whitley 1967] R. Whitley, *An elementary proof of the Eberlein–Šmulian theorem*, Mathematische Annalen **172** (1967), 116–118. [Publisher record](https://doi.org/10.1007/BF01350091).

[Whitley 1986] R. Whitley, *The Kreĭn–Šmulian theorem*, Proceedings of the American Mathematical Society **97**, no. 2 (June 1986), 376–377. [Free published article](https://math.univ-lyon1.fr/wikis/rouge/lib/exe/fetch.php?media=rodrigues6_whitley2.pdf), [DOI](https://doi.org/10.1090/S0002-9939-1986-0835903-X). The weak-star compact convex set referred to as a dual sphere in the article is the dual ball; the probability-measure set in Lemma 3.1 is explicitly a closed subset of that ball. The convex-hull theorem is also commonly called Krein's theorem. It differs from the dual-space bounded-slice closedness theorem of Krein–Šmulian.
