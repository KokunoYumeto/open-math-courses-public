# Minimal invariant sets and diametral sequences

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A map \(F:C\to C\) of a subset of a normed space is *nonexpansive* if \(\|F(a)-F(b)\|\le\|a-b\|\) for all \(a,b\in C\). In 1965 Browder and Göhde proved that every nonexpansive self-map of a nonempty closed bounded convex subset of a uniformly convex Banach space has a fixed point [Br], and Kirk proved the same in reflexive spaces for sets with *normal structure* (Theorem 3.2 below). Whether the conclusion holds in every reflexive Banach space, with the given norm, remained open; partial answers, examples without normal structure such as Karlovitz's [Ka], and examples showing that some hypothesis is needed (Exercise 5.3) accumulated over the following decades. OpenAI proved in September 2026 [OpenAI-K]:

**Theorem.** Let \(X\) be a real reflexive Banach space and \(C\subseteq X\) nonempty, closed, bounded and convex. Every nonexpansive map \(F:C\to C\) has a fixed point.

This course gives the proof. The present lesson contains the classical reduction to a minimal invariant set \(K\) of diameter \(1\) (Lemma 2.1), the lemma of Goebel and Karlovitz that approximate fixed points in \(K\) are at distance nearly \(1\) from every point of \(K\) (Lemma 3.1), Kirk's theorem as a first consequence, and a uniform version of the diametral lemma for compact sets (Lemma 3.3). The lesson [Resolvents and an anchor point](resolvents-and-an-anchor-point.md) finds a point \(x\in K\) to which convex combinations of approximate fixed points chosen one after another can return; the lesson [A tree of predicted outputs](a-tree-of-predicted-outputs.md) organizes such choices on an infinite tree; the lesson [Kirk's problem](kirks-problem.md) derives a contradiction.

We use: from the Banach space lesson of the foundations course, Zorn's lemma, [Theorem 1.1](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-01), and the Hahn–Banach theorem with norming functionals, [Corollary 2.3](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-02); from the [weak topologies lesson](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian#OA-FND-WT-03), the Banach–Alaoglu theorem (Theorem 3.1) and Mazur's theorem (Theorem 4.1: convex sets have the same weak and norm closures; norm-closed convex sets are weakly closed); and the existence of a free ultrafilter on \(\mathbb N\), [Lemma 1.1 of Ultrapowers and Darbo's fixed-point theorem](course:tingleys-problem/ultrapowers-and-darbos-fixed-point-theorem#1-ultrafilters-and-limits-along-them).

## 1. Weak compactness

Throughout, \(X\) is a real Banach space, \(X^*\) its dual, \(j:X\to X^{**}\) the canonical isometry, and the *weak topology* of \(X\) is the coarsest topology making every \(\ell\in X^*\) continuous. \(X\) is *reflexive* if \(j\) is onto.

**Lemma 1.1.** If \(X\) is reflexive, every closed bounded convex subset of \(X\) is weakly compact.

**Proof.** The weak\* topology of \(X^{**}=(X^*)^*\) is the coarsest topology making the evaluations at elements of \(X^*\) continuous, and \(j(x)(\ell)=\ell(x)\). So \(j\) is a homeomorphism from \(X\) with its weak topology onto \(X^{**}\) with its weak\* topology. It maps the closed unit ball of \(X\) onto that of \(X^{**}\), which is weak\* compact by the Banach–Alaoglu theorem applied to the normed space \(X^*\). Hence closed balls of \(X\) are weakly compact. A closed bounded convex set lies in such a ball and is weakly closed by Mazur's theorem, so it is weakly compact. \(\square\)

Fix a free ultrafilter \(\mathcal U\) on \(\mathbb N\). For a sequence \((a_j)\) in a topological space, write \(a=\lim_{j\to\mathcal U}a_j\) if \(\{j:a_j\in V\}\in\mathcal U\) for every neighbourhood \(V\) of \(a\).

**Lemma 1.2.** In a compact Hausdorff space every sequence has exactly one limit along \(\mathcal U\). A continuous map preserves limits along \(\mathcal U\).

**Proof.** For \(A\in\mathcal U\) let \(F_A\) be the closure of \(\{a_j:j\in A\}\). These closed sets have the finite intersection property, because \(\mathcal U\) is closed under finite intersections and does not contain \(\varnothing\); by compactness some point \(a\) lies in all of them. If \(V\) is an open neighbourhood of \(a\) with \(\{j:a_j\in V\}\notin\mathcal U\), then \(A=\{j:a_j\notin V\}\in\mathcal U\) and \(F_A\) lies in the closed set outside \(V\), which contradicts \(a\in F_A\). Two limits with disjoint neighbourhoods would give disjoint members of \(\mathcal U\). The last statement follows from the definition. \(\square\)

In particular, a sequence in a weakly compact set has a weak limit along \(\mathcal U\); and if \(a_j\to a\) in the usual sense, then \(\lim_{j\to\mathcal U}a_j=a\), since cofinite sets lie in \(\mathcal U\).

## 2. Minimal invariant sets

**Lemma 2.1** (reduction). Suppose some nonexpansive self-map of a nonempty closed bounded convex subset of a reflexive space \(X\) has no fixed point. Then there are a nonempty, separable, weakly compact convex set \(K\subseteq X\) of diameter \(1\) and a nonexpansive \(T:K\to K\) without fixed points, after multiplying the norm by a positive constant, such that:

(a) no nonempty closed convex proper subset of \(K\) is mapped into itself by \(T\) (\(K\) is *minimal*);

(b) the weak topology on \(K\) is metrizable;

(c) \(Y=\overline{\operatorname{span}}(K-K)\) is separable, and its closed unit ball \(B_Y\) is weakly compact.

**Proof.** Let \(F:C\to C\) be nonexpansive without fixed points and \(a\in C\). Put \(C_0=\{a\}\) and \(C_{n+1}=\overline{\operatorname{conv}}(C_n\cup F(C_n))\). By induction the \(C_n\) are separable: a continuous image of a separable set is separable, and rational convex combinations of a countable dense subset are dense in its convex hull. Their union is convex and separable, so \(C'=\overline{\bigcup_nC_n}\subseteq C\) is a separable closed bounded convex set, and \(F(C')\subseteq C'\) by continuity of \(F\). By Lemma 1.1, \(C'\) is weakly compact.

Consider the nonempty closed convex subsets of \(C'\) mapped into themselves by \(F\), ordered by reverse inclusion. Each is weakly closed by Mazur's theorem, so a chain has nonempty intersection by weak compactness of \(C'\), and the intersection is again closed, convex and invariant. Zorn's lemma gives a minimal such set \(K\), and \(T=F|_K\) has no fixed point. In particular \(K\) is not a single point, and its diameter is positive; after multiplying the norm by a constant it is \(1\). This changes neither the topologies nor nonexpansiveness. Being a closed convex subset of \(C'\), \(K\) is separable and weakly compact.

(c) If \((z_i)\) is dense in \(K\), the differences \(z_i-z_j\) span a dense subspace of \(Y\), so \(Y\) is separable. \(B_Y\) is closed, bounded and convex, so it is weakly compact by Lemma 1.1; its weak topology as a subset of \(X\) is the weak topology of the normed space \(Y\), since functionals on \(Y\) are restrictions of functionals on \(X\) (Hahn–Banach).

(b) Let \((u_j)\) be dense in the unit sphere of \(Y\) and choose \(g_j\in X^*\) with \(\|g_j\|\le1\) and \(g_j(u_j)=1\). If \(a\neq a'\) in \(K\), put \(e=(a-a')/\|a-a'\|\) and choose \(u_j\) with \(\|e-u_j\|<\frac12\); then \(g_j(e)>\frac12\), so \(g_j(a)\neq g_j(a')\). Hence \(a\mapsto(g_j(a))_{j\ge1}\) is a continuous injection of the weakly compact space \(K\) into \(\mathbb R^{\mathbb N}\), which is metrizable by \(\sum_j2^{-j}\min\{1,|s_j-t_j|\}\). A continuous injection of a compact space into a Hausdorff space is a homeomorphism onto its image. \(\square\)

## 3. Diametral sequences

From now on in this course, \(K\), \(T\), \(Y\) are as in Lemma 2.1 (under the hypothesis that a counterexample exists), and \((z_i)_{i\ge1}\) is a fixed norm-dense sequence in \(K\). A sequence \((u_j)\) in \(K\) is an *approximate fixed point sequence* if \(\|Tu_j-u_j\|\to0\).

**Lemma 3.1** (Goebel, Karlovitz). For every approximate fixed point sequence \((u_j)\) and every \(z\in K\), \(\|u_j-z\|\to1\).

**Proof.** First, \(K=\overline{\operatorname{conv}}\,T(K)\): the right side is a nonempty closed convex subset of \(K\), and \(T\) maps it into \(T(K)\), which lies in it; minimality applies. For \(z\in K\) put
\[
s(z)=\sup_{w\in K}\|z-w\|,\qquad r(z)=\limsup_j\|z-u_j\|.
\]
Both are convex and \(1\)-Lipschitz. The function \(w\mapsto\|Tz-w\|\) is convex and continuous, so its supremum over \(K=\overline{\operatorname{conv}}\,T(K)\) equals its supremum over \(T(K)\), and \(s(Tz)=\sup_{w\in K}\|Tz-Tw\|\le s(z)\). Also \(r(Tz)\le\limsup_j(\|Tz-Tu_j\|+\|Tu_j-u_j\|)\le r(z)\). Hence every nonempty sublevel set \(\{s\le c\}\) or \(\{r\le c\}\) is a closed convex subset of \(K\) mapped into itself by \(T\). If \(s\) or \(r\) took two values \(c_1<c_2\), the sublevel set at \(c_1\) would be a nonempty proper such subset, contradicting minimality. So \(s\) and \(r\) are constant. The supremum of \(s\) is \(\operatorname{diam}K=1\), so \(s\equiv1\); let \(r\equiv R\le1\).

Let \(a=\lim_{j\to\mathcal U}u_j\) weakly (Lemma 1.2). For \(z\in K\) and \(\eta>0\), all large \(j\) satisfy \(\|z-u_j\|\le R+\eta\); the ball \(\{w:\|z-w\|\le R+\eta\}\) is weakly closed (Mazur) and contains \(u_j\) for \(j\) in a cofinite set, so it contains \(a\). Hence \(1=s(a)\le R\), and \(R=1\). Every subsequence of \((u_j)\) is again an approximate fixed point sequence, so its \(\limsup_j\|u_j-z\|\) is \(1\) too. As \(\|u_j-z\|\le1\), this means \(\|u_j-z\|\to1\). \(\square\)

A convex set \(D\) has *normal structure* if every convex subset \(D'\subseteq D\) with more than one point contains a point \(a\) with \(\sup_{w\in D'}\|a-w\|<\operatorname{diam}D'\).

**Theorem 3.2** (Kirk). Let \(X\) be reflexive and \(C\subseteq X\) nonempty, closed, bounded and convex with normal structure. Every nonexpansive \(F:C\to C\) has a fixed point.

**Proof.** Otherwise Lemma 2.1, applied to \(F\), gives a minimal set \(K\subseteq C\) with more than one point (before the rescaling, which does not affect normal structure). The proof of Lemma 3.1 shows that \(s(z)=\sup_{w\in K}\|z-w\|\) is constant equal to \(\operatorname{diam}K\) on \(K\), contradicting normal structure. \(\square\)

Hilbert spaces, and more generally uniformly convex spaces, have normal structure (Exercise 5.2), so Theorem 3.2 contains the Hilbert space case of the Browder–Göhde theorem. Karlovitz showed that normal structure is not necessary [Ka].

**Lemma 3.3** (compact detector). Let \(E\subseteq K\) be nonempty and norm compact and \(\varepsilon>0\). There is \(\delta>0\) such that every \(y\in K\) with \(\|Ty-y\|\le\delta\) has a functional \(f\in X^*\), \(\|f\|\le1\), with
\[
f(y-z)\ge1-\varepsilon\qquad(z\in E).
\]

**Proof.** Choose \(a_1,\dots,a_m\in E\) such that every point of \(E\) has distance less than \(\varepsilon/2\) from some \(a_i\), and put \(a=\frac1m\sum_ia_i\in K\). By Lemma 3.1 there is \(\delta>0\) such that \(\|Ty-y\|\le\delta\) implies \(\|y-a\|\ge1-\frac\varepsilon{2m}\): otherwise points \(y_j\) with \(\|Ty_j-y_j\|\le1/j\) and \(\|y_j-a\|<1-\frac\varepsilon{2m}\) would form an approximate fixed point sequence violating Lemma 3.1. Let \(f\) be a norming functional for \(y-a\). Each \(f(y-a_i)\le\|y-a_i\|\le1\), and \(\sum_if(y-a_i)=mf(y-a)\ge m-\frac\varepsilon2\), so every \(f(y-a_i)\ge1-\frac\varepsilon2\). For \(z\in E\) choose \(a_i\) with \(\|z-a_i\|<\varepsilon/2\); then \(f(y-z)\ge f(y-a_i)-\|z-a_i\|>1-\varepsilon\). \(\square\)

A single functional thus sees an approximate fixed point at distance nearly \(1\) from all the points of a compact set at once.

## 4. Remarks

The minimal invariant set method goes back to Kirk, with the normal structure idea of Brodskiĭ and Milman. The argument of the next three lessons uses only Lemmas 1.1–3.3, the compactness of the weak topology and the convexity of the norm.

## 5. Exercises

**Exercise 5.1** (easy). Show that \(T\) has *approximate fixed points*: for every \(\delta>0\) some \(y\in K\) has \(\|Ty-y\|\le\delta\). (Consider \(T_n=(1-\frac1n)T+\frac1nw\) for a fixed \(w\in K\) and Banach's contraction principle.)

**Exercise 5.2** (medium). Show that every bounded convex subset of a Hilbert space has normal structure: if \(D'\) has more than one point and diameter \(\Delta\), choose \(u,w\in D'\) with \(\|u-w\|>\frac\Delta2\) and show that the midpoint \(a=\frac12(u+w)\) satisfies \(\sup_{z\in D'}\|a-z\|<\Delta\), using the parallelogram law.

**Exercise 5.3** (medium). In the Banach space \(c_0\) of real null sequences with the maximum norm, let \(C=\{x\in c_0:0\le x_i\le1\}\) and \(F(x)=(1,x_1,x_2,\dots)\). Show that \(C\) is closed, bounded and convex, that \(F\) is a nonexpansive self-map of \(C\), and that \(F\) has no fixed point. Which hypothesis of the theorem fails?

**Exercise 5.4** (easy). Show that the functions \(s\) and \(r\) in the proof of Lemma 3.1 are convex and \(1\)-Lipschitz.

## 6. Solutions

**5.1.** \(T_n\) maps \(K\) into \(K\) by convexity and is a contraction with constant \(1-\frac1n\); \(K\) is complete, so \(T_n\) has a fixed point \(y_n\). Then \(\|Ty_n-y_n\|=\|Ty_n-T_ny_n\|=\frac1n\|Ty_n-w\|\le\frac1n\).

**5.2.** For \(z\in D'\), the parallelogram law gives \(\|a-z\|^2=\frac12\|u-z\|^2+\frac12\|w-z\|^2-\frac14\|u-w\|^2\le\Delta^2-\frac14\|u-w\|^2\). With \(\|u-w\|>\frac\Delta2\), \(\sup_z\|a-z\|^2\le\Delta^2-\frac{\Delta^2}{16}<\Delta^2\).

**5.3.** \(C\) is an intersection of closed half-spaces with the closed set \(c_0\), and is bounded by \(1\). \(F(x)\) is a null sequence with entries in \([0,1]\), and \(\|F(x)-F(y)\|_\infty=\|x-y\|_\infty\). A fixed point would satisfy \(x_1=1\) and \(x_{i+1}=x_i\), so \(x=(1,1,\dots)\notin c_0\). The space \(c_0\) is not reflexive: Lemma 1.1 fails, and indeed \(C\) is not weakly compact.

**5.4.** Each \(z\mapsto\|z-w\|\) is convex and \(1\)-Lipschitz; suprema, and limits superior of bounded families, of convex \(1\)-Lipschitz functions keep both properties.

## References

- [Br] F. E. Browder, *Nonexpansive nonlinear operators in a Banach space*, Proc. Nat. Acad. Sci. USA 54 (1965), 1041–1044. https://doi.org/10.1073/pnas.54.4.1041
- [Ka] L. A. Karlovitz, *Existence of fixed points of nonexpansive mappings in a space without normal structure*, Pacific J. Math. 66 (1976), 153–159. https://doi.org/10.2140/pjm.1976.66.153
- [OpenAI-K] OpenAI, *Fixed points of nonexpansive maps in reflexive Banach spaces*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 2 and Appendix A. https://github.com/openai/math/blob/main/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026
