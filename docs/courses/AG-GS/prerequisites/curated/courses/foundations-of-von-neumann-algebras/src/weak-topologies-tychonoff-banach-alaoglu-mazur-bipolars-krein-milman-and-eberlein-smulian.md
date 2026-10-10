# Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian

*Originally written and self-checked by Claude Opus 5.5 (Anthropic), October 2026. GPT-6.1 Sol (OpenAI), at the Ultra setting, read and self-checked the full lesson and all four solutions, corrected the zero-space cases and supplied the complex-duality and extreme-point details, October 2026. Public domain (CC0).*

This lesson proves the facts about weak topologies that the operator-algebra lessons use:
- the continuous functionals of a weak topology are exactly the functionals that define it;
- Tychonoff's theorem, and from it the Banach–Alaoglu theorem;
- Mazur's theorem: convex sets have the same weak and norm closures, and more generally the same closures in all locally convex topologies with the same continuous functionals;
- annihilators and bipolars, Goldstine's theorem, and the dual of a quotient;
- second adjoints;
- the Krein–Milman theorem and Milman's converse;
- the Eberlein–Šmulian theorem, which says that weak compactness of a subset of a Banach space can be tested with sequences.

It builds on the lesson [Hahn–Banach, Baire and the basic theorems on Banach spaces](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md), cited below as *the previous lesson*.

## Conventions

As in the previous lesson. For a set \(S\) of linear functionals, \(\bigcap_{f\in S}\ker f\) is written \(\ker S\). A *net* is a family indexed by a directed set. A subset of a topological space is *relatively compact* if its closure is compact.

## 1. Weak topologies

Let \(X\) be a vector space and \(Y\) a vector space of linear functionals on \(X\). The *weak topology* \(\sigma(X,Y)\) is the locally convex topology given by the seminorms \(x\mapsto|y(x)|\), \(y\in Y\). It is the coarsest topology making every \(y\in Y\) continuous. It is Hausdorff exactly when \(Y\) separates the points of \(X\).

For a normed space \(E\):
- the *weak topology* on \(E\) is \(\sigma(E,E^*)\);
- the *weak\* topology* on \(E^*\) is \(\sigma(E^*,j(E))\), where \(j(x)(\varphi)=\varphi(x)\).

A net \(x_i\to x\) weakly when \(\varphi(x_i)\to\varphi(x)\) for every \(\varphi\in E^*\), and \(\varphi_i\to\varphi\) weak\* when \(\varphi_i(x)\to\varphi(x)\) for every \(x\in E\).

**Lemma 1.1.** Let \(f,f_1,\dots,f_n\) be linear functionals on a vector space \(X\) with \(\ker\{f_1,\dots,f_n\}\subseteq\ker f\). Then \(f\) is a linear combination of \(f_1,\dots,f_n\).

**Proof.** The map \(\pi:X\to\mathbb K^n\), \(x\mapsto(f_1(x),\dots,f_n(x))\), has kernel inside \(\ker f\). So \(g(\pi(x))=f(x)\) defines a linear functional \(g\) on the subspace \(\pi(X)\subseteq\mathbb K^n\). Extend \(g\) linearly to \(\mathbb K^n\); then \(g(t)=\sum_ic_it_i\), and \(f=\sum_ic_if_i\). \(\square\)

**Theorem 1.2.** The linear functionals on \(X\) that are continuous for \(\sigma(X,Y)\) are exactly the elements of \(Y\).

**Proof.** Elements of \(Y\) are continuous by definition. Let \(f\) be continuous. Then \(\{x:|f(x)|<1\}\) contains a basic neighbourhood \(\{x:|y_i(x)|<\varepsilon,\ i\le n\}\) with \(y_i\in Y\). If \(y_i(x)=0\) for all \(i\), then \(tx\) lies in this neighbourhood for every scalar \(t\), so \(|f(tx)|<1\) for all \(t\), and \(f(x)=0\). By Lemma 1.1, \(f\) is a linear combination of the \(y_i\), so \(f\in Y\). \(\square\)

**Corollary 1.3.** The weak topology of a normed space has continuous dual \(E^*\). The weak\* topology of \(E^*\) has continuous dual \(j(E)\). Both topologies are Hausdorff: \(E^*\) separates points of \(E\) by the previous lesson, Corollary 2.3, and \(j(E)\) separates points of \(E^*\) trivially.

## 2. Tychonoff's theorem

A *filter* on a set \(S\) is a nonempty family \(\mathcal F\) of subsets with three properties:
- \(\varnothing\notin\mathcal F\);
- \(A\cap B\in\mathcal F\) whenever \(A,B\in\mathcal F\);
- \(B\in\mathcal F\) whenever \(B\supseteq A\in\mathcal F\).

An *ultrafilter* is a filter not properly contained in another. A filter on a topological space *converges* to \(x\) if it contains every neighbourhood of \(x\).

**Lemma 2.1.**
1. Every filter is contained in an ultrafilter.
2. A filter \(\mathcal U\) is an ultrafilter iff for every \(A\subseteq S\), either \(A\in\mathcal U\) or \(S\setminus A\in\mathcal U\).
3. If \(f:S\to T\) and \(\mathcal U\) is an ultrafilter on \(S\), then \(f_*\mathcal U=\{B\subseteq T:f^{-1}(B)\in\mathcal U\}\) is an ultrafilter on \(T\).

**Proof.** 1. Filters containing the given one, ordered by inclusion, have unions of chains as upper bounds. Zorn's lemma (previous lesson, Theorem 1.1) gives a maximal one.

2. Suppose \(\mathcal U\) is an ultrafilter and \(A\notin\mathcal U\). If \(A\cap U\neq\varnothing\) for all \(U\in\mathcal U\), then the sets containing some \(A\cap U\) form a filter that contains \(\mathcal U\) and \(A\), contradicting maximality. So \(A\cap U=\varnothing\) for some \(U\in\mathcal U\), and then \(S\setminus A\supseteq U\) lies in \(\mathcal U\). Conversely, a filter with this property is maximal: a larger filter would contain some \(A\notin\mathcal U\) together with \(S\setminus A\in\mathcal U\), hence \(\varnothing\).

3. \(f_*\mathcal U\) is a filter, and 2 applies because \(f^{-1}(T\setminus B)=S\setminus f^{-1}(B)\). \(\square\)

**Lemma 2.2.** A topological space \(K\) is compact iff every ultrafilter on \(K\) converges.

**Proof.** *Compact implies convergence.* Suppose an ultrafilter \(\mathcal U\) converges to no point. Every \(x\) then has an open neighbourhood \(V_x\notin\mathcal U\), so \(K\setminus V_x\in\mathcal U\) by Lemma 2.1(2). Finitely many \(V_{x_1},\dots,V_{x_n}\) cover \(K\). Then \(\bigcap_j(K\setminus V_{x_j})=\varnothing\) lies in \(\mathcal U\), which is impossible.

*Convergence implies compact.* Let \(\mathcal O\) be an open cover with no finite subcover. The complements of finite unions of members of \(\mathcal O\) are nonempty and closed under finite intersections. So they generate a filter, contained in an ultrafilter \(\mathcal U\) (Lemma 2.1(1)). Let \(\mathcal U\) converge to \(x\), and pick \(O\in\mathcal O\) with \(x\in O\). Then \(O\in\mathcal U\) and \(K\setminus O\in\mathcal U\), so \(\varnothing\in\mathcal U\), a contradiction. \(\square\)

**Theorem 2.3** (Tychonoff). A product \(\prod_{i\in I}K_i\) of compact spaces is compact in the product topology.

**Proof.** Let \(\mathcal U\) be an ultrafilter on the product and \(\pi_i\) the projections. By Lemma 2.1(3) each \((\pi_i)_*\mathcal U\) is an ultrafilter on \(K_i\). By Lemma 2.2 it converges to some \(x_i\); this uses the axiom of choice to choose the limits.

The point \(x=(x_i)\) is a limit of \(\mathcal U\). A basic neighbourhood of \(x\) has the form \(\bigcap_{i\in F}\pi_i^{-1}(V_i)\), with \(F\) finite and \(V_i\) a neighbourhood of \(x_i\). Each \(\pi_i^{-1}(V_i)\in\mathcal U\), since \(V_i\in(\pi_i)_*\mathcal U\), and \(\mathcal U\) is closed under finite intersections. By Lemma 2.2 the product is compact. \(\square\)

## 3. The Banach–Alaoglu theorem

**Theorem 3.1** (Banach–Alaoglu). For every normed space \(E\), the closed unit ball \(B^*\) of \(E^*\) is weak\* compact.

**Proof.** For \(x\in E\) let \(D_x=\{\lambda\in\mathbb K:|\lambda|\le\|x\|\}\), and \(P=\prod_{x\in E}D_x\), compact by Theorem 2.3. The map \(\Phi:B^*\to P\), \(\varphi\mapsto(\varphi(x))_x\), is injective.

\(\Phi\) is a homeomorphism onto its image, with \(B^*\) carrying the weak\* topology: both topologies are the topology of pointwise convergence.

The image is closed in \(P\). It is the set of points \((\lambda_x)\) satisfying \(\lambda_{x+y}=\lambda_x+\lambda_y\) and \(\lambda_{tx}=t\lambda_x\) for all \(x,y,t\), and each of these conditions defines a closed set: such a point is a linear functional bounded by \(\|x\|\) at \(x\), hence an element of \(B^*\).

A closed subset of a compact space is compact. \(\square\)

**Proposition 3.2.** If \(E\) is separable, the weak\* topology on \(B^*\) is metrizable.

**Proof.** Let \((x_n)\) be dense in the unit ball of \(E\). Put \(d(\varphi,\psi)=\sum_n2^{-n}|\varphi(x_n)-\psi(x_n)|\) on \(B^*\).
- \(d\) is a metric: if \(d(\varphi,\psi)=0\), then \(\varphi=\psi\) on a dense subset of the ball, so \(\varphi=\psi\).
- The identity map from \((B^*,\text{weak}^*)\) to \((B^*,d)\) is continuous: each term is continuous, and the series converges uniformly because \(|\varphi(x_n)-\psi(x_n)|\le2\).
- A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism. \(\square\)

## 4. Mazur's theorem

**Theorem 4.1** (Mazur). A convex subset \(C\) of a normed space has the same closure in the weak and in the norm topology. In particular, norm-closed convex sets are weakly closed. If \(x_n\to x\) weakly, then some sequence of convex combinations of the \(x_n\) converges to \(x\) in norm.

**Proof.** The weak topology is coarser, so the norm closure \(\overline C\) lies in the weak closure. Conversely, if \(x\notin\overline C\), the previous lesson, Corollary 6.4(2), gives \(\varphi\in E^*\) and \(t\) with \(\operatorname{Re}\varphi\le t\) on \(\overline C\) and \(\operatorname{Re}\varphi(x)>t\). The weakly open set \(\{\operatorname{Re}\varphi>t\}\) contains \(x\) and misses \(C\), so \(x\) is not in the weak closure.

For the last statement, apply this to the convex hull of \(\{x_n:n\ge1\}\). The point \(x\) lies in its weak closure, hence in its norm closure. \(\square\)

The same argument works in every locally convex space.

**Theorem 4.2** (Closures of convex sets). Let \((X,\tau)\) be a locally convex space with continuous dual \(X^*\). A convex set \(C\subseteq X\) has the same closure for \(\tau\) and for \(\sigma(X,X^*)\). Consequently, two locally convex topologies on \(X\) with the same continuous linear functionals have the same closed convex sets.

**Proof.** Every \(\varphi\in X^*\) is \(\tau\)-continuous, so \(\sigma(X,X^*)\subseteq\tau\), and the \(\tau\)-closure \(\overline C\) lies in the \(\sigma(X,X^*)\)-closure. Let \(x\notin\overline C\). The set \(\overline C\) is closed and convex. The previous lesson, Corollary 6.4(2), gives \(\varphi\in X^*\) and \(t\) with \(\operatorname{Re}\varphi\le t\) on \(\overline C\) and \(\operatorname{Re}\varphi(x)>t\). The \(\sigma(X,X^*)\)-open set \(\{\operatorname{Re}\varphi>t\}\) contains \(x\) and misses \(C\). For the last claim, both topologies give the closure of \(C\) that \(\sigma(X,X^*)\) gives. \(\square\)

## 5. Annihilators, bipolars and Goldstine's theorem

For \(L\subseteq E\) let \(L^\perp=\{\varphi\in E^*:\varphi|_L=0\}\). For \(N\subseteq E^*\) let \(N_\perp=\{x\in E:\varphi(x)=0\ \forall\varphi\in N\}\).

**Theorem 5.1.** Let \(E\) be a normed space.
1. For a subspace \(L\subseteq E\), the norm closure of \(L\) is \((L^\perp)_\perp\).
2. For a subspace \(N\subseteq E^*\), the weak\* closure of \(N\) is \((N_\perp)^\perp\).

**Proof.** 1. The set \((L^\perp)_\perp\) is norm closed and contains \(L\). If \(x\notin\overline L\), the previous lesson, Corollary 2.3(3), gives \(\varphi\in L^\perp\) with \(\varphi(x)\ne0\), so \(x\notin(L^\perp)_\perp\).

2. The set \((N_\perp)^\perp\) is weak\* closed and contains \(N\). Let \(\psi\) lie outside the weak\* closure \(\overline N\), a weak\* closed subspace. The weak\* topology is locally convex. By the previous lesson, Corollary 6.4(2), there is a weak\* continuous functional \(F\) with \(\operatorname{Re}F(\psi)>t\ge\operatorname{Re}F(\overline N)\) for some \(t\).

Since \(\overline N\) is a subspace, \(F\) vanishes on it: if \(F(\varphi)\neq0\) for some \(\varphi\in\overline N\), suitable multiples \(s\varphi\) would make \(\operatorname{Re}F(s\varphi)\) as large as we like. So \(t\ge0\) and \(\operatorname{Re}F(\psi)>0\).

By Corollary 1.3, \(F=j(x)\) for some \(x\in E\). Then \(x\in N_\perp\) and \(\psi(x)\ne0\), so \(\psi\notin(N_\perp)^\perp\). \(\square\)

**Theorem 5.2** (Goldstine). The image \(j(B)\) of the closed unit ball \(B\) of \(E\) is weak\* dense in the closed unit ball of \(E^{**}\).

**Proof.** Let \(K\) be the weak\* closure of \(j(B)\). It is convex and lies in the unit ball of \(E^{**}\), which is weak\* closed.

Suppose \(\Phi\) is in the unit ball of \(E^{**}\) but not in \(K\). The space \((E^{**},\sigma(E^{**},E^*))\) is locally convex with continuous dual \(E^*\) (Theorem 1.2). The previous lesson, Corollary 6.4(2), gives \(\varphi\in E^*\) and \(t\) with \(\operatorname{Re}\Phi(\varphi)>t\ge\operatorname{Re}j(x)(\varphi)=\operatorname{Re}\varphi(x)\) for all \(x\in B\).

Taking the supremum over \(B\), and using that \(B\) is balanced, gives \(\|\varphi\|\le t\). Then \(\operatorname{Re}\Phi(\varphi)>t\ge\|\varphi\|\ge\|\Phi\|\,\|\varphi\|\), which is impossible. \(\square\)

**Proposition 5.3** (second adjoints). For \(T\in B(E,F)\) let \(T^*\in B(F^*,E^*)\), \(T^*\psi=\psi\circ T\), and \(T^{**}=(T^*)^*\).
1. \(\|T^*\|=\|T\|\) and \(\|T^{**}\|=\|T\|\).
2. \(T^{**}\circ j_E=j_F\circ T\).
3. \((ST)^{**}=S^{**}T^{**}\).
4. \(T^{**}\) is weak\*–weak\* continuous.

**Proof.** 1. \(\|T^*\psi\|=\sup_{\|x\|\le1}|\psi(Tx)|\le\|\psi\|\|T\|\). Conversely, for \(\|x\|\le1\) choose \(\psi\) of norm at most \(1\) with \(\psi(Tx)=\|Tx\|\) (previous lesson, Corollary 2.3(2)); then \(\|Tx\|\le\|T^*\|\). Apply the same to \(T^*\).

2. \[
\begin{gathered}
T^{**}(j_Ex)(\psi)\\
=j_Ex(T^*\psi)\\
=\psi(Tx)\\
=j_F(Tx)(\psi).
\end{gathered}
\]

3. \((ST)^*=T^*S^*\), so \((ST)^{**}=S^{**}T^{**}\).

4. If \(\Phi_i\to\Phi\) weak\*, then \[
\begin{gathered}
T^{**}\Phi_i(\psi)\\
=\Phi_i(T^*\psi)\to\Phi(T^*\psi)\\
=T^{**}\Phi(\psi)
\end{gathered}
\] for every \(\psi\in F^*\). \(\square\)

**Proposition 5.4** (The dual of a quotient). Let \(M\) be a closed subspace of a normed space \(E\), with quotient map \(q:E\to E/M\) and quotient norm \(\|x+M\|=\operatorname{dist}(x,M)\). Then \(g\mapsto g\circ q\) is an isometric isomorphism of \((E/M)^*\) onto \(M^\perp\).

**Proof.**
- \(g\circ q\) is bounded and vanishes on \(M\).
- *Isometry.* \(q\) maps the open unit ball of \(E\) onto the open unit ball of \(E/M\): if \(\|x+M\|<1\), some \(m\in M\) has \(\|x-m\|<1\). Hence \(\|g\circ q\|=\|g\|\).
- *Onto \(M^\perp\).* Let \(\varphi\in M^\perp\). Then \(g(x+M)=\varphi(x)\) is well defined and linear. For every \(m\in M\), \(|g(x+M)|=|\varphi(x-m)|\le\|\varphi\|\,\|x-m\|\). Taking the infimum over \(m\) gives \(|g(x+M)|\le\|\varphi\|\,\|x+M\|\), so \(g\in(E/M)^*\) and \(g\circ q=\varphi\). \(\square\)

## 6. The Krein–Milman theorem

A point \(e\) of a convex set \(K\) is *extreme* if \(e=tx+(1-t)y\) with \(x,y\in K\) and \(0<t<1\) forces \(x=y=e\). A nonempty closed subset \(F\subseteq K\) is a *face* (an *extreme subset*) if whenever \(tx+(1-t)y\in F\) with \(x,y\in K\) and \(0<t<1\), both \(x,y\in F\).

**Theorem 6.1** (Krein–Milman). Let \(X\) be a Hausdorff locally convex space and \(K\subseteq X\) a nonempty compact convex set. Then \(K\) has an extreme point, and \(K\) is the closed convex hull of its extreme points.

**Proof.** *Faces contain extreme points.* Faces of \(K\), ordered by reverse inclusion, satisfy the hypothesis of Zorn's lemma. The intersection of a chain is nonempty, by compactness and the finite intersection property, and it is closed and a face. So there is a minimal face \(F\).

Suppose \(F\) has two points \(x\ne y\). Choose a continuous \(\varphi\) with \(\operatorname{Re}\varphi(x)\ne\operatorname{Re}\varphi(y)\); this exists by the previous lesson, Corollary 6.4(1), replacing \(\varphi\) by \(i\varphi\) if needed. The set \(F'=\{z\in F:\operatorname{Re}\varphi(z)=\max_F\operatorname{Re}\varphi\}\) is then:
- nonempty, because \(F\) is compact;
- closed, and a face of \(F\), hence of \(K\): if \(tx'+(1-t)y'\in F'\) with \(x',y'\in K\), then \(x',y'\in F\) because \(F\) is a face, and both attain the maximum, since a strict average of two values at most the maximum equals the maximum only if both do;
- smaller than \(F\), since it cannot contain both \(x\) and \(y\).

This contradicts minimality. So \(F=\{e\}\), and \(e\) is an extreme point of \(K\), because \(\{e\}\) is a face.

*The closed convex hull.* Let \(C\) be the closed convex hull of the extreme points; it lies in \(K\). If some \(x\in K\setminus C\) existed, the previous lesson, Theorem 6.3, would give a continuous \(\varphi\) and \(t\) with \(\operatorname{Re}\varphi<t\) on \(C\) and \(\operatorname{Re}\varphi(x)>t\).

The set \(F=\{z\in K:\operatorname{Re}\varphi(z)=\max_K\operatorname{Re}\varphi\}\) is a face of \(K\) disjoint from \(C\), because its points have \(\operatorname{Re}\varphi\ge\operatorname{Re}\varphi(x)>t\). By the first part, applied to the compact convex set \(F\), it contains an extreme point of \(F\), which is an extreme point of \(K\) because \(F\) is a face, and so lies in \(C\). This is a contradiction. \(\square\)

**Theorem 6.2** (Milman). Let \(X\) be a Hausdorff locally convex space, \(Q\subseteq X\) compact, and suppose that the closed convex hull \(K\) of \(Q\) is compact. Then every extreme point of \(K\) lies in \(Q\).

**Proof.** Let \(e\in K\) be extreme, and suppose \(e\notin Q\).

*A neighbourhood that keeps \(e\) away from \(Q\).* For each \(q\in Q\), \(e-q\neq0\). Since \(X\) is Hausdorff and locally convex, there is a convex balanced open neighbourhood \(U_q\) of \(0\) with \(e-q\notin U_q+U_q\). Finitely many sets \(q_j+U_{q_j}\) cover \(Q\). Put \(W=\bigcap_jU_{q_j}\). Then \(e\notin Q+W\): if \(e=q+w\) with \(q\in q_j+U_{q_j}\) and \(w\in W\), then \(e-q_j\in U_{q_j}+U_{q_j}\).
- Choose a convex balanced open neighbourhood \(W'\) of \(0\) with \(W'+W'\subseteq W\), and let \(V\) be the closure of \(W'\). Then \(V\) is closed and convex, and \(V\subseteq W'+W'\subseteq W\), because every point of the closure of \(W'\) lies in \(y+W'\) for some \(y\in W'\). So \(e\notin Q+V\).

*Splitting \(K\).* Finitely many sets \(p_k+W'\), \(p_k\in Q\), cover \(Q\). Let \(K_k\) be the closed convex hull of \(Q\cap(p_k+V)\).
- \(K_k\subseteq p_k+V\), because \(p_k+V\) is closed and convex. And \(K_k\subseteq K\) is closed, hence compact.
- The convex hull \(K'\) of \(K_1\cup\dots\cup K_n\) is the image of the compact set \(K_1\times\dots\times K_n\times\Delta_n\), where \(\Delta_n\) is the simplex of weights, under the continuous map \((x_1,\dots,x_n,t)\mapsto\sum_kt_kx_k\). So \(K'\) is compact, hence closed. It is convex and contains \(Q\), so it contains \(K\).

*Conclusion.* So \(e=\sum_kt_kx_k\) with \(x_k\in K_k\) and weights \(t_k\). Since \(e\) is extreme in \(K\), \(e=x_k\) for every \(k\) with \(t_k>0\): if \(0<t_1<1\), write \(e=t_1x_1+(1-t_1)y\) with \(y\in K\), so \(x_1=y=e\), and continue with \(y\). Hence \(e\in K_k\subseteq p_k+V\subseteq Q+V\) for some \(k\), a contradiction. \(\square\)

## 7. The Eberlein–Šmulian theorem

**Lemma 7.1.** Let \(E\) be a normed space and \(M\subseteq E^{**}\) a finite-dimensional subspace. Then there are finitely many \(\varphi_1,\dots,\varphi_m\in E^*\) of norm \(1\) with \(\max\{0,|\Phi(\varphi_1)|,\dots,|\Phi(\varphi_m)|\}\ge\frac12\|\Phi\|\) for every \(\Phi\in M\). The family may be empty when \(M=\{0\}\).

**Proof.** If \(M=\{0\}\), the empty family works. Otherwise the unit sphere \(S_M\) of \(M\) is nonempty and compact (previous lesson, Theorem 7.1). For each \(\Phi\in S_M\), choose \(\varphi_\Phi\) of norm \(1\) with \(|\Phi(\varphi_\Phi)|>3/4\). The open sets \(\{\Psi\in S_M:\|\Psi-\Phi\|<1/4\}\) cover \(S_M\), so finitely many centres \(\Phi_1,\dots,\Phi_m\) suffice. For \(\Psi\in S_M\) with \(\|\Psi-\Phi_k\|<1/4\), \(|\Psi(\varphi_{\Phi_k})|\ge|\Phi_k(\varphi_{\Phi_k})|-\|\Psi-\Phi_k\|>1/2\). Scale for general \(\Phi\in M\). \(\square\)

**Theorem 7.2** (Eberlein–Šmulian). For a subset \(A\) of a Banach space \(E\), the following are equivalent:
1. \(A\) is relatively weakly compact;
2. every sequence in \(A\) has a subsequence that converges weakly to a point of \(E\);
3. every sequence in \(A\) has a weak cluster point in \(E\).

**Proof.** If \(E=\{0\}\) or \(A=\varnothing\), all three assertions are immediate. Suppose otherwise. *2 implies 3.* The limit of a weakly convergent subsequence is a weak cluster point.

*1 implies 3.* A sequence in the compact set \(\overline A^{\,w}\), the weak closure of \(A\), has a cluster point there. The terms \(\{x_n:n\ge m\}\) form a decreasing family of sets with the finite intersection property, so their closures meet.

*3 implies 1.*

**Step 1: \(A\) is bounded.** Otherwise there is \(\varphi\in E^*\) with \(\sup_{x\in A}|\varphi(x)|=\infty\), by the previous lesson, Corollary 4.3(2). So there are \(x_n\in A\) with \(|\varphi(x_n)|\ge n\). A weak cluster point \(x\) of \((x_n)\) would make \(\varphi(x)\) a cluster point of \((\varphi(x_n))\), which has none.

**Step 2: the weak\* closure of \(j(A)\) lies in \(j(E)\).** The weak\* closure \(\overline{j(A)}^{w*}\) is weak\* compact by Theorem 3.1, since \(A\) is bounded. Let \(\Phi\) be in it. We build \(x_n\in A\) and functionals of norm \(1\) inductively.
- Let \(\varphi_1\) be any functional of norm \(1\), and choose \(x_1\in A\) with \(|(\Phi-jx_1)(\varphi_1)|<1\).
- Given \(x_1,\dots,x_n\), let \(M_n=\operatorname{span}\{\Phi,\Phi-jx_1,\dots,\Phi-jx_n\}\). Lemma 7.1 gives finitely many functionals of norm \(1\) that norm \(M_n\) up to the factor \(\frac12\). Append them to the list \(\varphi_1,\varphi_2,\dots\).
- Since \(\Phi\) lies in the weak\* closure of \(j(A)\), choose \(x_{n+1}\in A\) with \(|(\Phi-jx_{n+1})(\varphi_k)|<1/(n+1)\) for all functionals \(\varphi_k\) listed so far.

Let \(x\) be a weak cluster point of \((x_n)\).

**Step 3: \(\Phi=j(x)\).**
- *\(\Psi=\Phi-jx\) lies in \(\overline{\bigcup_nM_n}\).* The point \(x\) is in the weak closure of \(\{x_n\}\), hence in the norm-closed linear span of \(\{x_n\}\) by Theorem 4.1. So \(jx\) is a norm limit of combinations \(\sum c_kjx_k\). Then \(\Psi\) is a norm limit of \(\Phi-\sum c_kjx_k\). Each of these lies in \(M_n\) for large \(n\): write \[
\begin{gathered}
\Phi-\sum c_kjx_k\\
=(1-\sum c_k)\Phi+\sum c_k(\Phi-jx_k).
\end{gathered}
\]
- *\(\|\Psi\|\le2\sup_k|\Psi(\varphi_k)|\).* For \(G\in M_n\), \(\|G\|\le2\max_k|G(\varphi_k)|\), with \(k\) running over the functionals chosen for \(M_n\). Approximating \(\Psi\) by such \(G\) gives \(\|\Psi\|\le2\sup_k|\Psi(\varphi_k)|+3\|\Psi-G\|\), and the last term tends to \(0\).
- *\(\Psi(\varphi_k)=0\) for every \(k\).* For \(n\) large, \(|\Phi(\varphi_k)-\varphi_k(x_n)|<1/n\). Since \(\varphi_k(x)\) is a cluster point of \((\varphi_k(x_n))\), we get \(\Phi(\varphi_k)=\varphi_k(x)\).

Hence \(\Psi=0\), that is, \(\Phi=jx\in j(E)\).

**Step 4: conclusion.** The map \(j\) is a homeomorphism from \((E,\text{weak})\) onto \((j(E),\text{weak}^*)\): both topologies are pointwise convergence on \(E^*\). By Step 2, \(\overline{j(A)}^{w*}=j(K)\) for some \(K\subseteq E\). This \(K\) is weakly compact and contains \(A\), so \(A\) is relatively weakly compact.

*1 implies 2.* Let \((x_n)\) be a sequence in \(A\).
- Let \(E_0\) be the norm-closed span of \(\{x_n\}\), a separable closed subspace. By Theorem 4.1 it is weakly closed. The weak closure \(K\) of \(\{x_n\}\) is weakly compact by 1 and lies in \(E_0\).
- Let \((y_m)\) be dense in \(E_0\). Choose \(\psi_m\in E^*\) of norm \(1\) with \(\psi_m(y_m)=\|y_m\|\). The family \((\psi_m)\) separates the points of \(E_0\): if \(z\ne0\) in \(E_0\), choose \(y_m\) with \(\|z-y_m\|<\|z\|/3\); then \(|\psi_m(z)|\ge\|y_m\|-\|z-y_m\|>\|z\|/3\).
- By 1 implies 3 and Step 1, \(A\) is norm bounded. The weakly closed norm ball containing it also contains \(K\), so this series is uniformly convergent on \(K\times K\). The topology on \(K\) induced by \(d(u,v)=\sum_m2^{-m}|\psi_m(u-v)|\) is Hausdorff and coarser than the weak topology. A compact topology admits no strictly coarser Hausdorff topology, so the weak topology on \(K\) is this metric topology.
- In a compact metric space the closures of the sequence tails have a common point \(x\), by the finite intersection property. Every ball about \(x\) contains arbitrarily late terms. Choose successively increasing indices whose terms lie in the balls of radii \(1/k\); the subsequence converges in the metric. Thus \((x_n)\) has a subsequence converging weakly in \(K\subseteq E\). \(\square\)

## Exercises

**Exercise 1** (medium). Show that in an infinite-dimensional normed space the weak closure of the unit sphere \(\{\|x\|=1\}\) is the closed unit ball.

*Solution.*
- *The closure lies in the ball:* the closed unit ball is convex and norm closed, so weakly closed (Theorem 4.1).
- *Every point with \(\|x_0\|<1\) is in the closure.* A basic weak neighbourhood \(U=\{x:|\varphi_i(x-x_0)|<\varepsilon,\ i\le n\}\) contains \(x_0+\ker\{\varphi_1,\dots,\varphi_n\}\). This kernel is a nonzero subspace, because a linear map from an infinite-dimensional space to \(\mathbb K^n\) has nonzero kernel. Pick \(y\ne0\) in it. The function \(t\mapsto\|x_0+ty\|\) is continuous, equals \(\|x_0\|<1\) at \(t=0\), and tends to infinity. Choose \(T>0\) with \(\|x_0+Ty\|>1\). Bisect the interval \([0,T]\), retaining endpoint values that bracket one. Its nested endpoints converge to a common real number \(t\); continuity gives \(\|x_0+ty\|=1\). This produces a point of the sphere in \(U\).
- *Every point with \(\|x_0\|=1\) is on the sphere itself.* \(\square\)

**Exercise 2** (medium). Let \(E=c_0\), the null sequences with the supremum norm. Show that \(\delta_n\to0\) weakly but not in norm, and find convex combinations of the \(\delta_n\) that converge to \(0\) in norm.

*Solution.*
- *Weak convergence:* put \(a_k=\varphi(\delta_k)\) for \(\varphi\in c_0^*\). On a finite set \(F\), choose \(\theta_k=\overline{a_k}/|a_k|\) when \(a_k\ne0\), and zero otherwise. Then \(\|\sum_{k\in F}\theta_k\delta_k\|_\infty\leq1\), so \(\sum_{k\in F}|a_k|\leq\|\varphi\|\). Hence \(a\in\ell^1\). Finite cutoffs approximate each \(x\in c_0\) in supremum norm, giving \(\varphi(x)=\sum_ka_kx_k\). Conversely this series defines a bounded functional for every \(a\in\ell^1\), with norm at most \(\|a\|_1\); the same finite phase tests give the reverse inequality. Thus \(c_0^*=\ell^1\) isometrically, and \(\varphi_a(\delta_n)=a_n\to0\).
- *No norm convergence:* \(\|\delta_n\|=1\).
- *Convex combinations:* \(\frac1N(\delta_1+\dots+\delta_N)\) has norm \(1/N\to0\), as Theorem 4.1 predicts. \(\square\)

**Exercise 3** (medium). Show that the closed unit ball of \(\ell^1\) has extreme points \(\{\lambda\delta_n:|\lambda|=1\}\), but that the closed unit ball of \(c_0\) has none. Deduce that \(c_0\) is not isometrically isomorphic to the dual of any normed space.

*Solution.*
- *\(\ell^1\):* if \(\|x\|_1<1\), choose \(0<\varepsilon<1-\|x\|_1\); the distinct vectors \(x\pm\varepsilon\delta_1\) belong to the ball and average to \(x\). If \(\|x\|_1=1\) and \(x_i,x_j\ne0\) with \(i\ne j\), put \(u_i=x_i/|x_i|\), \(u_j=x_j/|x_j|\), and choose \(0<\varepsilon<\min(|x_i|,|x_j|)\). The two vectors \(x\pm\varepsilon(u_i\delta_i-u_j\delta_j)\) both have norm one, since their two altered coordinate magnitudes add to \(|x_i|+|x_j|\). They are distinct and average to \(x\). The remaining points are \(\lambda\delta_n\), \(|\lambda|=1\), and these are extreme: if \(\lambda\delta_n=(x+y)/2\) with \(\|x\|_1,\|y\|_1\leq1\), multiply the nth coordinate by \(\bar\lambda\). The real parts of both resulting numbers are at most one and average to one, so both numbers equal one. Hence \(x_n=y_n=\lambda\), and the norm bounds force every other coordinate of \(x,y\) to vanish.
- *\(c_0\):* given \(x\) in the unit ball, \(|x_k|<1/2\) for some \(k\). Then \(x\pm\frac12\delta_k\) are in the ball and average to \(x\).
- *Deduction:* the unit ball of a dual space is weak\* compact and convex (Theorem 3.1), so by Theorem 6.1 it has extreme points. A linear isometric isomorphism preserves convex combinations and therefore extreme points of balls. \(\square\)

**Exercise 4** (easy). Show that a reflexive Banach space (one with \(j(E)=E^{**}\)) has a weakly compact closed unit ball, and deduce that every bounded sequence in it has a weakly convergent subsequence.

*Solution.*
- *Weak compactness:* the ball of \(E^{**}=j(E)\) is weak\* compact by Theorem 3.1, applied to \(E^*\). By Step 4 of the proof of Theorem 7.2, \(j\) is a homeomorphism from the weak topology to the weak\* topology. So the unit ball of \(E\) is weakly compact.
- *Sequences:* Theorem 7.2, 1 ⇒ 2, gives the weakly convergent subsequence. \(\square\)

## Where this leads

The lesson [Hilbert spaces and compact operators](hilbert-spaces-and-compact-operators.md) uses these results for operators on Hilbert space. The operator topologies on \(B(H)\) are weak topologies in the sense of Section 1, and the predual of a von Neumann algebra is studied with Theorems 5.1 and 7.2 in Polar decomposition of functionals and weak compactness in preduals.

## References

The results are classical: Tychonoff (1930, 1935), Banach (1932) and Alaoglu (1940), Mazur (1933), Goldstine (1938), Krein and Milman (1940), Eberlein (1947) and Šmulian (1940). The proof of the Eberlein–Šmulian theorem follows R. Whitley, "An elementary proof of the Eberlein–Šmulian theorem", *Mathematische Annalen* 172 (1967) 116–118, written here in our own words.

*Freely accessible reading:* [H. Vogt, *An Eberlein–Šmulian type result for the weak* topology*, Theorems 3–4](https://user.math.uni-bremen.de/hvogt/papers/vo09a.pdf) gives a route through weak-star tail-convex-hull criteria; the extra hull hypothesis is essential. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.

Whitley’s original proof is also freely readable in [Göttingen’s digitized volume, printed pp. 116–118](https://gdz.sub.uni-goettingen.de/id/PPN235181684_0172?tify=%7B%22pages%22:%5B126%5D%7D).
