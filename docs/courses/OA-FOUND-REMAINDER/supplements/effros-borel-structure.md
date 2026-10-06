# The Effros Borel structure

*Written by Claude Opus 5.5 (Anthropic), September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A direct integral of von Neumann algebras is assembled from a family \(\gamma\mapsto M(\gamma)\) of von Neumann algebras that depends measurably on a parameter \(\gamma\). To make sense of this, one needs a Borel structure on a set of von Neumann algebras, and workable tests for measurability. This lesson supplies both.

We give a Borel structure, the *Effros Borel structure*, to three sets: the weak\*-closed subspaces of the dual of a separable Banach space, the closed subspaces of a separable Hilbert space, and the von Neumann algebras acting on a fixed separable Hilbert space. We show that these Borel spaces are standard, that their elements can be chosen in a Borel way, and that adjoints, commutants, intersections, joins and the set of factors are Borel. We then embed every measurable field of Hilbert spaces isometrically into one fixed space, with ranges that depend measurably on the point. With this we show that commutants, centres, intersections and joins of measurably generated families of von Neumann algebras are again measurably generated. These are the measurability facts that direct integrals of von Neumann algebras need.

Sections 1–5 need only basic functional analysis and metric topology. Sections 6, 7 and 10 use measurable fields of Hilbert spaces and of operators, as developed in [Measurable fields of Hilbert spaces and their direct integrals](../reader/supplements/measurable-fields-direct-integrals.html), and a few facts from [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html). Sections 8–10 use the predual of \(B(\mathcal K)\) and its \(\sigma\)-weak topology. The facts used without proof are stated in full below. No measure is used anywhere: every result holds over an arbitrary measurable space.

Effros introduced the Borel space of von Neumann algebras on a separable Hilbert space in 1965 [Effros 1965]. Basic references are [Effros 1965] and [Takesaki I].

## Conventions

- \(\mathbb K\) is \(\mathbb R\) or \(\mathbb C\), and Banach spaces are over \(\mathbb K\). Hilbert spaces are complex, inner products are linear in the first variable, and the zero space is allowed. "Separable" includes finite-dimensional.
- For a Banach space \(E\), \(E^*\) is its dual with the weak\* topology, \(E^*_1\) is the closed unit ball of \(E^*\), and \(d(x,A)=\inf\{\|x-a\|:a\in A\}\). For \(S\subseteq E\), \(S^\perp=\{f\in E^*:f=0\text{ on }S\}\). For \(T\subseteq E^*\), \(T_\perp=\{x\in E:f(x)=0\text{ for all }f\in T\}\).
- \((\Gamma,\Sigma)\) is a measurable space, and *measurable* means \(\Sigma\)-measurable. A map into a topological space is measurable if the preimage of every Borel set lies in \(\Sigma\). No standardness of \(\Gamma\) is needed, and no measure is needed either.
- A *measurable field of Hilbert spaces* over \((\Gamma,\Sigma)\) is a family \((H(\gamma))_{\gamma\in\Gamma}\) of Hilbert spaces together with a linear space \(\mathfrak M\) of sections (maps \(\xi\) with \(\xi(\gamma)\in H(\gamma)\) for every \(\gamma\)), called *measurable sections*, such that:
  - **(F1)** \(\gamma\mapsto\|\xi(\gamma)\|\) is measurable for every \(\xi\in\mathfrak M\);
  - **(F2)** a section \(\eta\) belongs to \(\mathfrak M\) whenever \(\gamma\mapsto\langle\eta(\gamma),\xi(\gamma)\rangle\) is measurable for every \(\xi\in\mathfrak M\);
  - **(F3)** some sequence in \(\mathfrak M\), called *fundamental*, has values whose linear span is dense in \(H(\gamma)\) for every \(\gamma\).

  A family of bounded operators \(x(\gamma):H(\gamma)\to K(\gamma)\) between two measurable fields is a *measurable field of bounded operators* if \(\gamma\mapsto x(\gamma)\xi(\gamma)\) is a measurable section for every measurable section \(\xi\).
- The lesson [Measurable fields of Hilbert spaces and their direct integrals](../reader/supplements/measurable-fields-direct-integrals.html) develops these fields over a measure space \((\Gamma,\Sigma,\mu)\), but nothing there before the direct integral itself uses \(\mu\). So we use those results over \((\Gamma,\Sigma)\); formally this is the case \(\mu=0\). The same applies to what we use from [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html): the [matrix-unit fields](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-01), the [matrix-entry criterion](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-07) for operator fields on a constant field, and two of its [example fields](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-08).
- For a Hilbert space \(\mathcal K\), \(B(\mathcal K)_1\) is the closed unit ball of \(B(\mathcal K)\), and \(B(\mathcal K)_*\) is the space of \(\sigma\)-weakly continuous linear functionals on \(B(\mathcal K)\).
- We call a \(*\)-subalgebra \(M\subseteq B(\mathcal K)\) with \(M''=M\) a *von Neumann algebra* on \(\mathcal K\), and a *factor* if moreover \(M\cap M'=\mathbb C1\). For a set \(S\) with \(S^*=S\), \(S''\) is the von Neumann algebra generated by \(S\). The von Neumann algebra *generated* by an arbitrary set \(S\) is \((S\cup S^*)''\), and \(M\vee N=(M\cup N)''\). On the zero space, \(B(0)=\{0\}=\mathbb C1\) is the only von Neumann algebra, and it is a factor by this definition. Every commutant is \(\sigma\)-weakly closed, because \(x\mapsto xa-ax\) is \(\sigma\)-weakly continuous for each \(a\); so every von Neumann algebra is \(\sigma\)-weakly closed. The bicommutant theorem is not needed.

## Background used without proof

Let \(E\) be a Banach space and \(\mathcal K\) a Hilbert space.

- **(D1)** (*Hahn–Banach theorem*) Let \(q\) be a seminorm on a vector space \(W\) over \(\mathbb K\), \(V\subseteq W\) a subspace and \(g:V\to\mathbb K\) linear with \(|g|\leq q\) on \(V\). Then \(g\) extends to a linear functional on \(W\) with \(|g|\leq q\). Over \(\mathbb R\) it is enough that \(g\leq q\), and the extension satisfies \(g\leq q\). This is Theorems 2.1 and 2.2 of [*Hahn–Banach, Baire and the basic theorems on Banach spaces*](../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-02).
- **(D2)** (*Annihilators*) For \(S\subseteq E\), \((S^\perp)_\perp\) is the norm-closed linear span of \(S\). For \(T\subseteq E^*\), \((T_\perp)^\perp\) is the weak\*-closed linear span of \(T\). This is Theorem 5.1 of [*Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian*](../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#oa-fnd-wt-05), applied to the linear spans.
- **(D3)** (*Banach–Alaoglu theorem*) \(E^*_1\) is weak\*-compact. This is Theorem 3.1 of [*Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian*](../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#oa-fnd-wt-03).
- **(P1)** Every \(\psi\in B(\mathcal K)_*\) has the form \(\psi(x)=\sum_n\langle x\xi_n,\eta_n\rangle\) with \(\sum\|\xi_n\|^2<\infty\) and \(\sum\|\eta_n\|^2<\infty\).
- **(P2)** \(B(\mathcal K)_*\) is a Banach space whose dual is \(B(\mathcal K)\), and the weak\* topology on \(B(\mathcal K)\) is the \(\sigma\)-weak topology.
- **(P3)** On \(B(\mathcal K)_1\) the \(\sigma\)-weak and weak operator topologies coincide.

  For (P1)–(P3) see [Blackadar, Sections I.8.5 and I.8.6]. The proofs below use only (P1) and (P2); (P3) links the \(\sigma\)-weak topology with the weak operator topology used for operator fields.
- **(R)** (*Reduced algebras*, used only in Exercise 5) If \(M\) is a von Neumann algebra on \(\mathcal K\) and \(p\in M\) is a projection, then \(pMp\), acting on \(p\mathcal K\), is a von Neumann algebra. This is proved in [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-08).

Elementary facts from Hilbert space and metric space theory are used without comment: the Riesz representation of bounded functionals on a Hilbert space, Parseval's identity, the polarization identity, the compactness of \([0,1]^{\mathbb N}\), and the equivalence of all norms on a finite-dimensional space.

## 1. Borel spaces and Polish spaces

**Definitions 1.1.**

- A *Borel space* consists of a set \(X\) and a \(\sigma\)-algebra \(\mathcal B\) of subsets of \(X\), whose members are called *Borel sets*. A subset \(Y\subseteq X\) carries the *relative* Borel structure \(\{B\cap Y:B\in\mathcal B\}\).
- A map \(f:X\to Y\) of Borel spaces is *Borel* if \(f^{-1}(B)\) is Borel for every Borel \(B\subseteq Y\). A *Borel isomorphism* is a bijection \(f\) such that \(f\) and \(f^{-1}\) are Borel.
- \(\sigma(\mathcal S)\) is the \(\sigma\)-algebra generated by a family \(\mathcal S\) of sets. For maps \(f_i:X\to Y_i\) into Borel spaces, \(\sigma(f_i:i\in I)\) is the smallest \(\sigma\)-algebra that makes every \(f_i\) Borel. A family of Borel sets is *generating* if it generates \(\mathcal B\), and *separating* if for any two distinct points some member contains one of them and not the other. \(X\) is *countably generated* or *countably separated* if it has a countable family of that kind. A stronger condition asks for a single countable family that both generates and separates. [Proposition 3.2(5)](#oa-fnd-ef-03) supplies such a family, so its conclusion holds in either sense.
- The Borel structure of a topological space is the \(\sigma\)-algebra generated by its open sets.
- A topological space is *Polish* when its topology comes from a complete metric and it has a countable dense subset. A Borel space is *standard* when some Polish space, with its Borel sets, is Borel isomorphic to it.
- A *measure* on \((X,\mathcal B)\) is a countably additive map \(\mu:\mathcal B\to[0,\infty]\). It is *standard* if \(X\setminus N\), with its relative Borel structure, is standard for some Borel set \(N\) with \(\mu(N)=0\).

**Example 1.2.** A Borel map need not carry Borel sets to Borel sets. The identity map from \(\mathbb R\) with its Borel sets to \(\mathbb R\) with the \(\sigma\)-algebra of countable and co-countable sets is Borel, since every set of the second kind is Borel. It carries the Borel set \([0,1]\) to a set that is neither countable nor co-countable.

**Lemma 1.3.**

1. (*Testing on generators*) Suppose \(\mathcal B=\sigma(f_i:i\in I)\). A map \(g:\Gamma\to X\) is measurable if and only if every \(f_i\circ g\) is measurable.
2. (*Countable bases*) If a topological space has a countable base \(\mathcal U\), every open set is a countable union of members of \(\mathcal U\), so the Borel sets are \(\sigma(\mathcal U)\). The Borel structure of a product of countably many second countable spaces is generated by the coordinate maps. In particular, for a countable set \(D\), the Borel structure of \(\mathbb R^D\) is generated by the coordinates.
3. (*A stock of Polish spaces*) Closed subsets and countable products of Polish spaces are Polish, and so is the disjoint union of two Polish spaces, each piece open in the union. The space \(\mathbb N^{\mathbb N}\) is Polish. A separable metrizable space, and hence every standard Borel space, has at most \(2^{\aleph_0}\) points.
4. (*Pieces*) Let \(\Gamma\) be the union of countably many sets \(\Gamma_d\in\Sigma\). A map \(g\) on \(\Gamma\) whose restriction to every \(\Gamma_d\) is measurable for the relative \(\sigma\)-algebra is measurable.

**Proof.** (1) The sets \(B\subseteq X\) with \(g^{-1}(B)\in\Sigma\) form a \(\sigma\)-algebra. If every \(f_i\circ g\) is measurable, it contains every \(f_i^{-1}(C)\) with \(C\) Borel, so it contains \(\mathcal B\). The converse is clear.

(2) Let \(V\) be open. For each \(x\in V\) pick \(U_x\in\mathcal U\) with \(x\in U_x\subseteq V\). Only countably many distinct sets \(U_x\) occur, and their union is \(V\). For a product \(\prod_kX_k\) with countable bases \(\mathcal U_k\), the finite intersections of sets \(\pi_k^{-1}(U)\), \(U\in\mathcal U_k\), form a countable base. Each of them lies in \(\sigma(\pi_k:k)\), and the coordinates are continuous, so this \(\sigma\)-algebra is the Borel one.

(3) A closed subset of a complete metric space is complete, and a subset of a separable metric space is separable. For Polish spaces \(X_k\), choose complete compatible metrics \(d_k\leq1\) (replace \(d_k\) by \(\min(d_k,1)\)). Then \(\rho(x,y)=\sum_k2^{-k}d_k(x_k,y_k)\) is a metric for the product topology. A \(\rho\)-Cauchy sequence is Cauchy in every coordinate, so it converges in every coordinate, and then in \(\rho\), because the tails of the series are uniformly small. The points that agree with a fixed point outside finitely many coordinates, and lie in fixed countable dense sets inside them, form a countable dense set. For two Polish spaces, use their metrics bounded by \(1\) inside each piece and distance \(1\) across. \(\mathbb N^{\mathbb N}\) is a countable product of copies of the complete separable discrete space \(\mathbb N\). Finally, if \(Q\) is a countable dense set in a separable metrizable space, sending each point to a sequence in \(Q\) that converges to it is injective, and there are at most \(|Q^{\mathbb N}|\leq2^{\aleph_0}\) such sequences.

(4) For Borel \(B\), \(g^{-1}(B)=\bigcup_d(g|_{\Gamma_d})^{-1}(B)\), and each term is a subset of \(\Gamma_d\) lying in the relative \(\sigma\)-algebra, hence in \(\Sigma\). \(\square\)

## 2. Polish subspaces and Borel subsets

**Theorem 2.1** (*Polish subspaces*). Let \(X\) be a Polish space.

1. Every \(G_\delta\) subset of \(X\) is Polish in the relative topology.
2. Conversely, a subset of \(X\) that is Polish in the relative topology is a \(G_\delta\) subset of \(X\).
3. Every Polish space is homeomorphic to some \(G_\delta\) subset of \([0,1]^{\mathbb N}\), and every such subset is Polish.

**Proof.** Fix a complete compatible metric \(d\) on \(X\).

(1) Let \(Y=\bigcap_nG_n\) with \(G_n\) open. Drop every \(G_n\) equal to \(X\); if none is left, \(Y=X\). For \(y\in Y\) put \(h_n(y)=1/d(y,X\setminus G_n)\), a positive continuous function on \(G_n\), and
\[
d_Y(y,y')=d(y,y')+\sum_n2^{-n}\min\big(1,|h_n(y)-h_n(y')|\big).
\]
This is a metric on \(Y\), and it defines the relative topology: \(d_Y\geq d\), and if \(d(y_k,y)\to0\) inside \(Y\), then \(h_n(y_k)\to h_n(y)\) for each \(n\), so the series tends to \(0\) term by term under the bounds \(2^{-n}\). Let \((y_k)\) be \(d_Y\)-Cauchy. It is \(d\)-Cauchy, so it converges in \(X\) to some \(x\). For each \(n\), \((h_n(y_k))_k\) is Cauchy, hence bounded by some \(c_n\). Then \(d(y_k,X\setminus G_n)\geq1/c_n\) for all \(k\), so \(d(x,X\setminus G_n)\geq1/c_n>0\) and \(x\in G_n\). Hence \(x\in Y\) and \(d_Y(y_k,x)\to0\). Finally \(Y\) is separable, being a subset of a separable metric space.

(2) Let \(\rho\) be a complete metric on \(Y\) compatible with its relative topology. For \(n\geq1\), let \(Y_n\) be the set of points \(x\) of the closure \(\overline Y\) that have an open neighbourhood \(U\) in \(X\) with \(\rho\)-diameter of \(U\cap Y\) at most \(1/n\). Each \(Y_n\) is relatively open in \(\overline Y\), because a witness \(U\) for \(x\) is a witness for every point of \(U\cap\overline Y\). Also \(Y\subseteq Y_n\): for \(y\in Y\), the ball \(\{\rho(\cdot,y)<1/(3n)\}\) is relatively open in \(Y\), so it equals \(U\cap Y\) for some open \(U\ni y\) in \(X\). Conversely, let \(x\in\bigcap_nY_n\), with witnesses \(U_n\). The open sets \(W_n=U_1\cap\cdots\cap U_n\cap\{d(\cdot,x)<1/n\}\) contain \(x\in\overline Y\), so we can pick \(y_n\in W_n\cap Y\). Then \(y_n\to x\) in \(X\), and \(\rho(y_m,y_n)\leq1/n\) for \(m\geq n\), since both lie in \(U_n\cap Y\). So \((y_n)\) converges in \((Y,\rho)\) to some \(y\in Y\), hence to \(y\) in \(X\), and \(y=x\). Thus \(Y=\bigcap_nY_n\). Write \(Y_n=G_n\cap\overline Y\) with \(G_n\) open in \(X\). Since \(\overline Y=\bigcap_m\{d(\cdot,\overline Y)<1/m\}\) is a \(G_\delta\), so is \(Y\).

(3) \([0,1]^{\mathbb N}\) is a compact metrizable space, hence Polish, so its \(G_\delta\) subsets are Polish by (1). Conversely, let \(X\) be Polish, with compatible metric \(d\) and dense sequence \((a_n)\), and put \(\varphi(x)=(\min(1,d(a_n,x)))_n\). The map \(\varphi\) is continuous. It is injective: for \(x\neq y\) put \(\delta=\min(1,d(x,y))\) and choose \(a_n\) with \(d(a_n,x)<\delta/3\); then the \(n\)-th coordinate of \(\varphi(x)\) is below \(\delta/3\) and that of \(\varphi(y)\) is at least \(2\delta/3\). Its inverse is continuous on \(\varphi(X)\): if \(\varphi(x_k)\to\varphi(x)\) and \(0<\varepsilon<1/2\), choose \(a_n\) with \(d(a_n,x)<\varepsilon\); then eventually \(d(a_n,x_k)<\varepsilon\), so \(d(x_k,x)<2\varepsilon\). So \(\varphi(X)\) is homeomorphic to \(X\), hence Polish, hence a \(G_\delta\) subset of \([0,1]^{\mathbb N}\) by (2). \(\square\)

**Theorem 2.2** (*Borel subsets of standard spaces*). Let \((X,\tau)\) be a Polish space and \(B\subseteq X\) a Borel set. There is a Polish topology \(\tau'\supseteq\tau\) on \(X\), with the same Borel sets as \(\tau\), in which \(B\) is open and closed. Consequently \(B\), with its relative Borel structure, is a standard Borel space. The same holds for a Borel subset of any standard Borel space.

The proof uses only part (1) of Theorem 2.1.

**Proof.** Call a topology \(\tau'\) on \(X\) *admissible* if it is Polish, contains \(\tau\), and has the same Borel sets as \(\tau\).

*(a) Open sets.* Let \(U\) be \(\tau\)-open, and let \(\tau_U\) be the topology generated by \(\tau\) together with the set \(X\setminus U\). Its open sets are the unions of sets \(V\) and \(V\cap(X\setminus U)\) with \(V\in\tau\). So \((X,\tau_U)\) is the disjoint union of the open subspace \(U\) and the closed subspace \(X\setminus U\) of \((X,\tau)\), each open in \(\tau_U\). Both pieces are Polish: \(U\) by Theorem 2.1(1), since an open set is a \(G_\delta\), and \(X\setminus U\) because closed subsets of Polish spaces are Polish ([Lemma 1.3(3)](#oa-fnd-ef-01)). By the same lemma, their disjoint union is Polish. The new open sets are \(\tau\)-Borel. So \(\tau_U\) is admissible, and \(U\) is \(\tau_U\)-clopen.

*(b) Countable joins.* Let \(\tau_1,\tau_2,\ldots\) be admissible, and let \(\tau_\infty\) be the topology generated by their union. The diagonal map \(x\mapsto(x,x,\ldots)\) from \((X,\tau_\infty)\) to the Polish space \(\prod_n(X,\tau_n)\) is a homeomorphism onto the diagonal \(\Delta\), since the preimage of \(\pi_n^{-1}(V)\) is \(V\) for \(V\in\tau_n\). The diagonal is closed: if \(y\notin\Delta\), then \(y_m\neq y_n\) for some \(m,n\); since \(\tau\) is Hausdorff, there are disjoint \(\tau\)-open sets \(A\ni y_m\) and \(C\ni y_n\), and \(\pi_m^{-1}(A)\cap\pi_n^{-1}(C)\) is a neighbourhood of \(y\) that misses \(\Delta\). So \(\tau_\infty\) is Polish, because a closed subset of a Polish space is Polish. It has a countable base consisting of finite intersections of members of countable bases of the \(\tau_n\). These are \(\tau\)-Borel, and a countable base generates the Borel sets ([Lemma 1.3(2)](#oa-fnd-ef-01)). So \(\tau_\infty\) has the same Borel sets as \(\tau\), and it is admissible.

*(c) All Borel sets.* Let \(\mathcal A\) be the family of sets that are clopen for some admissible topology. It contains \(\tau\) by (a), and it is closed under complements. If \(B_n\in\mathcal A\) is clopen for an admissible \(\tau_n\), then \(\bigcup_nB_n\) is open for the \(\tau_\infty\) of (b); applying (a) to \((X,\tau_\infty)\) makes it clopen for a topology that is admissible. So \(\mathcal A\) is a \(\sigma\)-algebra containing \(\tau\), and it contains every Borel set.

Now let \(B\) be clopen for an admissible \(\tau'\). Then \(B\) is \(\tau'\)-closed, hence Polish in the relative \(\tau'\)-topology ([Lemma 1.3(3)](#oa-fnd-ef-01)). The Borel sets of a subspace are the traces of the Borel sets of the whole space: the traces form a \(\sigma\)-algebra on \(B\) containing the relatively open sets, and the sets \(C\) whose trace is Borel in \(B\) form a \(\sigma\)-algebra containing the open sets. The \(\tau'\)-Borel sets are the \(\tau\)-Borel sets, so the relative Borel structure of \(B\) is the Borel structure of a Polish space. For a standard Borel space, transport \(B\) to a Polish space by a Borel isomorphism. \(\square\)

## 3. The Effros Borel structure

Throughout, \(E\) is a separable Banach space, and \(\mathfrak W(E^*)\) is the set of weak\*-closed linear subspaces of \(E^*\). For \(F\in\mathfrak W(E^*)\) put \(F_1=F\cap E^*_1\) and
\[
p_F(x)=\sup\{|f(x)|:f\in F_1\},\qquad x\in E.
\tag{3.1}
\]
This is the norm of \(x\) as a functional on \(F\).

**Definition 3.1.** The *Effros Borel structure* on \(\mathfrak W(E^*)\) is \(\sigma(F\mapsto p_F(x):x\in E)\).

**Proposition 3.2.** Let \(F\in\mathfrak W(E^*)\), and let \(D\subseteq E\) be dense.

1. \(p_F\) is a seminorm with \(p_F\leq\|\cdot\|\). Hence \(|p_F(x)-p_F(y)|\leq\|x-y\|\). Its kernel is \(F_\perp\).
2. (*Distance formula*) \(p_F(x)=d(x,F_\perp)\) for every \(x\in E\).
3. (*Domination*) A linear functional \(f\) on \(E\), not assumed continuous, lies in \(F_1\) if and only if \(|f(x)|\leq p_F(x)\) for every \(x\in E\). For \(\mathbb K=\mathbb R\) this is the same as \(f\leq p_F\).
4. (*Subspaces of \(E\)*) \(F\mapsto F_\perp\) is a bijection of \(\mathfrak W(E^*)\) onto the set \(\mathcal S(E)\) of closed linear subspaces of \(E\), with inverse \(N\mapsto N^\perp\). It carries \(p_F\) to \(d(\cdot,F_\perp)\).
5. \(F\) is determined by the values \(p_F(x)\), \(x\in D\), and the Effros structure equals \(\sigma(F\mapsto p_F(x):x\in D)\). If \(D\) is countable, the sets \(\{F:p_F(x)<r\}\), \(x\in D\), \(r\in\mathbb Q\), are countably many Borel sets that generate and separate. So \(\mathfrak W(E^*)\) is countably generated and countably separated.
6. If \(\Phi,\Psi:X\to\mathfrak W(E^*)\) are Borel maps on a Borel space \(X\), the set \(\{x:\Phi(x)=\Psi(x)\}\) is Borel. In particular, points of \(\mathfrak W(E^*)\) are Borel sets, and so is the fixed-point set of any Borel map \(\mathfrak W(E^*)\to\mathfrak W(E^*)\).
7. (*The unit ball*) \(E^*_1\) with the weak\* topology is a compact metrizable space. For countable dense \(D\), its Borel structure is \(\sigma(f\mapsto f(x):x\in D)\). A map \(a:\Gamma\to E^*_1\) is measurable if and only if \(\gamma\mapsto a(\gamma)(x)\) is measurable for every \(x\in D\), or equivalently for every \(x\in E\).
8. (*Norm Borel structure*) Let \((\ell_j)\) be a sequence in \(E^*_1\) with \(\|x\|=\sup_j|\ell_j(x)|\) for all \(x\). Then the Borel structure of the norm topology of \(E\) is \(\sigma(\ell_j:j\geq1)\). So a map \(y:\Gamma\to E\) is measurable if and only if every \(\ell_j\circ y\) is.

**Proof.** (1) \(p_F\) is a supremum of the seminorms \(|f(\cdot)|\) with \(\|f\|\leq1\). The Lipschitz bound follows from \(p_F(x)\leq p_F(y)+p_F(x-y)\) and the same with \(x,y\) exchanged. \(p_F(x)=0\) means \(f(x)=0\) for \(f\in F_1\), hence for all \(f\in F\) by scaling; so the kernel is \(F_\perp\).

(2) For \(f\in F_1\) and \(y\in F_\perp\), \(|f(x)|=|f(x-y)|\leq\|x-y\|\), so \(p_F(x)\leq d(x,F_\perp)\). For the reverse, let \(x\neq0\) (the case \(x=0\) is trivial). \(q=d(\cdot,F_\perp)\) is a seminorm, and the functional \(\lambda x\mapsto\lambda q(x)\) on \(\mathbb Kx\) satisfies \(|\lambda q(x)|=q(\lambda x)\). By (D1) it extends to a linear \(g\) on \(E\) with \(|g|\leq q\leq\|\cdot\|\). Then \(g\in E^*_1\), and \(g\) vanishes on \(F_\perp\), so \(g\in(F_\perp)^\perp=F\) by (D2). Hence \(p_F(x)\geq|g(x)|=q(x)\).

(3) Elements of \(F_1\) satisfy the bound by (3.1). Conversely, if \(|f|\leq p_F\leq\|\cdot\|\), then \(f\in E^*_1\) and \(f\) vanishes on \(\ker p_F=F_\perp\), so \(f\in(F_\perp)^\perp=F\) by (D2). For \(\mathbb K=\mathbb R\), \(f\leq p_F\) also gives \(-f(x)=f(-x)\leq p_F(x)\).

(4) \(F_\perp\) is a closed subspace, and \((F_\perp)^\perp=F\) by (D2). For \(N\in\mathcal S(E)\), \(N^\perp\) is weak\*-closed and \((N^\perp)_\perp=N\) by (D2). The last claim is (2).

(5) \(p_F\) is continuous by (1), so its values on \(D\) determine it, and \(p_F\) determines \(F=(\ker p_F)^\perp\) by (1) and (4). For \(x\in E\) choose \(x_j\in D\) with \(x_j\to x\). Then \(p_F(x)=\lim_jp_F(x_j)\) for every \(F\), so \(F\mapsto p_F(x)\) is measurable for \(\sigma(F\mapsto p_F(y):y\in D)\). The sets \(\{F:p_F(x)<r\}\) generate this \(\sigma\)-algebra, and they separate points, because \(F\) is determined by \(p_F\) on \(D\).

(6) Take a countable dense \(D\). By (5), \(\Phi(x)=\Psi(x)\) exactly when \(p_{\Phi(x)}(y)=p_{\Psi(x)}(y)\) for all \(y\in D\). Each of these countably many conditions defines a Borel set. For points, take \(\Phi\) the identity and \(\Psi\) constant; for fixed points, take \(\Psi\) the identity.

(7) Let \(D=\{x_1,x_2,\ldots\}\). On \(E^*_1\) the weak\* topology is the weakest topology making the maps \(f\mapsto f(x_k)\) continuous: if these values converge along a net \((f_i)\) to those of \(f\), then \(|f_i(x)-f(x)|\leq|f_i(x_k)-f(x_k)|+2\|x-x_k\|\), so \(f_i(x)\to f(x)\) for all \(x\). The metric \(\sum_k2^{-k}\min(1,|f(x_k)-g(x_k)|)\) defines this topology, and \(E^*_1\) is compact by (D3). The topology has a countable base of sets defined by finitely many conditions \(|f(x_k)-c|<r\), with \(c\) Gaussian rational and \(r\) rational. Since a countable base generates the Borel sets ([Lemma 1.3(2)](#oa-fnd-ef-01)), the Borel sets are \(\sigma(f\mapsto f(x_k):k)\). The measurability test follows by testing on generators ([Lemma 1.3(1)](#oa-fnd-ef-01)); values at points outside \(D\) are limits of values on \(D\).

(8) Each \(\ell_j\) is continuous. Conversely, an open ball \(\{x:\|x-x_0\|<r\}\) equals \(\bigcup_m\bigcap_j\{x:|\ell_j(x)-\ell_j(x_0)|\leq r-1/m\}\), which lies in \(\sigma(\ell_j:j)\). \(E\) is separable, so every open set is a countable union of balls centred at points of a countable dense set. The last clause follows by testing on generators ([Lemma 1.3(1)](#oa-fnd-ef-01)). \(\square\)

## 4. A Polish topology and standardness

We now show that the Effros Borel structure is standard, by exhibiting a Polish topology that generates it.

**Theorem 4.1.** Let \(\tau_E\) be the weakest topology on \(\mathfrak W(E^*)\) for which every function \(F\mapsto p_F(x)\), \(x\in E\), is continuous. Then \((\mathfrak W(E^*),\tau_E)\) is a Polish space, and its Borel sets are exactly the Effros Borel sets. In particular, the Effros Borel structure is standard.

**Proof.** Let \(D\subseteq E\) be a countable dense subset that is a vector space over \(\mathbb Q\) (over \(\mathbb Q+i\mathbb Q\) if \(\mathbb K=\mathbb C\)), for instance the rational span of a dense sequence.

*The topology.* \(\tau_E\) is also the weakest topology making \(F\mapsto p_F(x)\) continuous for \(x\in D\): for \(x\in E\) and \(x_j\in D\) with \(x_j\to x\), the function \(F\mapsto p_F(x)\) is the uniform limit of the functions \(F\mapsto p_F(x_j)\), because every \(p_F\) is \(1\)-Lipschitz ([Proposition 3.2(1)](#oa-fnd-ef-03)). The map \(\Theta(F)=(p_F(x))_{x\in D}\in\mathbb R^D\) is injective, because \(F\) is determined by the values of \(p_F\) on \(D\) ([Proposition 3.2(5)](#oa-fnd-ef-03)). So \(\Theta\) is a homeomorphism of \((\mathfrak W(E^*),\tau_E)\) onto its image \(\Theta(\mathfrak W(E^*))\), with the product topology on \(\mathbb R^D\).

*Seminorms.* Let \(S\subseteq\mathbb R^D\) be the set of \(c\) with \(c(x)\geq0\), \(|c(x)-c(y)|\leq\|x-y\|\), \(c(x+y)\leq c(x)+c(y)\) and \(c(qx)=|q|c(x)\) for all \(x,y\in D\) and all rational (Gaussian rational) \(q\). Each condition involves finitely many coordinates, so \(S\) is closed. The elements of \(S\) are exactly the restrictions to \(D\) of the seminorms \(p\) on \(E\) with \(p\leq\|\cdot\|\). Such a restriction satisfies the conditions. Conversely, \(c\in S\) is \(1\)-Lipschitz on \(D\), so it extends uniquely to a \(1\)-Lipschitz function \(p\) on \(E\); by continuity \(p\) is subadditive, \(p(\lambda x)=|\lambda|p(x)\) for all scalars \(\lambda\), and \(p\leq\|\cdot\|\), since \(p(0)=0\).

*The condition (W).* Consider, for \(c\in S\):

> (W) for every \(x\in D\) and every rational \(\varepsilon>0\) there is \(y\in D\) with \(c(y)<\varepsilon\) and \(\|x-y\|<c(x)+\varepsilon\).

For fixed \(x,\varepsilon,y\), the set \(\{c:c(y)<\varepsilon,\ c(x)>\|x-y\|-\varepsilon\}\) is open in \(\mathbb R^D\). So the set of \(c\in S\) that satisfy (W) is a \(G_\delta\) subset of \(\mathbb R^D\).

*Claim: for \(c=p|_D\in S\), (W) holds if and only if \(p(x)=d(x,\ker p)\) for all \(x\in E\).* First, \(p(x)=p(x-z)\leq\|x-z\|\) for \(z\in\ker p\), so \(p\leq d(\cdot,\ker p)\) always. If \(p=d(\cdot,\ker p)\), let \(x\in D\) and \(\varepsilon>0\). Pick \(z\in\ker p\) with \(\|x-z\|<p(x)+\varepsilon/2\) and \(y\in D\) with \(\|y-z\|<\varepsilon/2\). Then \(c(y)=p(y)\leq p(z)+\|y-z\|<\varepsilon\) and \(\|x-y\|<p(x)+\varepsilon\). Conversely, assume (W), and let \(x\in D\) and \(\varepsilon>0\) be rational. Applying (W) first to \(x\) and \(\varepsilon/2\), and then to each \(y_j\) and \(2^{-j-1}\varepsilon\), choose \(y_1,y_2,\ldots\in D\) with
\[p(y_1)<\varepsilon/2,\quad\|x-y_1\|<p(x)+\varepsilon/2,\qquad p(y_{j+1})<2^{-j-1}\varepsilon,\quad\|y_j-y_{j+1}\|<p(y_j)+2^{-j-1}\varepsilon<2^{1-j}\varepsilon .\]
The sequence \((y_j)\) is Cauchy, so it converges to some \(z\in E\). Then \(p(z)=\lim p(y_j)=0\), and \(\|x-z\|<p(x)+\varepsilon/2+\sum_{j\geq1}2^{1-j}\varepsilon=p(x)+5\varepsilon/2\). Thus \(d(x,\ker p)\leq p(x)\) for \(x\in D\), hence for all \(x\in E\), because both sides are continuous.

*The image.* If \(F\in\mathfrak W(E^*)\), then \(\Theta(F)\in S\), and \(p_F=d(\cdot,F_\perp)=d(\cdot,\ker p_F)\) by the distance formula and the description of the kernel in [Proposition 3.2(1)–(2)](#oa-fnd-ef-03); so \(\Theta(F)\) satisfies (W). Conversely, let \(c=p|_D\in S\) satisfy (W). Put \(N=\ker p\), a closed subspace, and \(F=N^\perp\in\mathfrak W(E^*)\). Then \(F_\perp=N\) by [Proposition 3.2(4)](#oa-fnd-ef-03), and \(p_F=d(\cdot,N)=p\) by the distance formula and the claim. So \(c=\Theta(F)\). Hence the image of \(\Theta\) is the \(G_\delta\) set above.

*Conclusion.* The space \(\mathbb R^D\) is Polish, as a countable product of copies of \(\mathbb R\) ([Lemma 1.3(3)](#oa-fnd-ef-01)). The image is a \(G_\delta\) subset of it, hence Polish by [Theorem 2.1(1)](#oa-fnd-ef-02), and so is \((\mathfrak W(E^*),\tau_E)\). Its Borel sets are the preimages under \(\Theta\) of the relative Borel sets of the image, which are generated by the coordinates ([Lemma 1.3(2)](#oa-fnd-ef-01)). So they form \(\sigma(F\mapsto p_F(x):x\in D)\), which is the Effros structure by [Proposition 3.2(5)](#oa-fnd-ef-03). \(\square\)

The claim used only the metric of \(E\) and its completeness. The same argument therefore handles closed sets in any complete separable metric space.

**Corollary 4.2** (*spaces of closed sets*). Let \((X,d)\) be a complete separable metric space, and \(\mathcal C_0(X)\) the set of nonempty closed subsets of \(X\). The weakest topology on \(\mathcal C_0(X)\) that makes every function \(A\mapsto d(x,A)\), \(x\in X\), continuous is Polish. Its Borel sets form \(\sigma(A\mapsto d(x,A):x\in X)\), and this \(\sigma\)-algebra is also generated by the sets \(\{A:A\cap U\neq\emptyset\}\), \(U\) open. In particular, either description gives a standard Borel structure on \(\mathcal C_0(X)\).

This topology is also called the Wijsman topology.

**Proof.** We may assume \(X\neq\emptyset\), since otherwise \(\mathcal C_0(X)\) is empty. Let \(D\) be a countable dense subset of \(X\), and \(S'\subseteq\mathbb R^D\) the closed set of \(c\geq0\) with \(|c(x)-c(y)|\leq d(x,y)\) for \(x,y\in D\); each \(c\in S'\) extends to a \(1\)-Lipschitz function \(f\geq0\) on \(X\). Let (W') be (W) with \(d(x,y)\) in place of \(\|x-y\|\). As before, the set of \(c\in S'\) satisfying (W') is a \(G_\delta\). If \(f=d(\cdot,A)\) with \(A\in\mathcal C_0(X)\), then (W') holds: pick \(a\in A\) with \(d(x,a)<f(x)+\varepsilon/2\) and \(y\in D\) with \(d(y,a)<\varepsilon/2\). Conversely, if (W') holds, the iteration in the proof of Theorem 4.1 produces, for \(x\in D\) and rational \(\varepsilon>0\), a limit point \(z\) with \(f(z)=0\) and \(d(x,z)<f(x)+5\varepsilon/2\); it converges because \(X\) is complete. So \(A=f^{-1}(0)\) is nonempty and closed, and \(d(\cdot,A)\leq f\) on \(D\), hence everywhere. Also \(f(x)\leq f(a)+d(x,a)=d(x,a)\) for \(a\in A\), so \(f=d(\cdot,A)\). A closed set is the zero set of its distance function, so \(A\mapsto(d(x,A))_{x\in D}\) is injective, and it is a homeomorphism onto the \(G_\delta\) set just described, because \(|d(x,A)-d(x',A)|\leq d(x,x')\). The rest is as in the proof of Theorem 4.1.

For the second description of the \(\sigma\)-algebra, note that \(\{A:d(x,A)<r\}=\{A:A\text{ meets the open ball }B(x,r)\}\). Conversely, an open set \(U\) is the union of the balls \(B(x,r)\subseteq U\) with \(x\) in a countable dense set and \(r\) rational, so \(\{A:A\cap U\neq\emptyset\}\) is the countable union of the sets \(\{A:d(x,A)<r\}\) over these balls. \(\square\)

**Remark 4.3** (*closed subspaces among closed sets*). By [Proposition 3.2(4)](#oa-fnd-ef-03), \(F\mapsto F_\perp\) identifies \(\mathfrak W(E^*)\) with the set of closed subspaces of \(E\) and carries \(p_F\) to \(d(\cdot,F_\perp)\). So the Effros structure is the structure that the closed subspaces inherit from \(\mathcal C_0(E)\), with the \(\sigma\)-algebra generated by the functions \(A\mapsto d(x,A)\). The closed subspaces form a Borel subset of \(\mathcal C_0(E)\): they are the sets \(A\in\mathcal C_0(E)\) with \(d(x+y,A)\leq d(x,A)+d(y,A)\) and \(d(qx,A)\leq|q|d(x,A)\) for \(x,y\) in a countable dense set and rational (Gaussian rational) \(q\). Indeed, by continuity these inequalities then hold for all \(x,y\) and all scalars, and for \(a,b\in A\) they give \(d(a+b,A)=0\) and \(d(\lambda a,A)=0\), so \(A\) is a subspace. Together with Corollary 4.2 and [Theorem 2.2](#oa-fnd-ef-02), this gives a second proof that the Effros Borel structure is standard.

**Example 4.4** (*separability cannot be dropped*). Let \(\mathcal K=\ell^2(I)\) for a set \(I\) of cardinality \(2^{\aleph_0}\), and let \(\mathcal S(\mathcal K)\) be the set of closed subspaces of \(\mathcal K\). The closed subspaces \(\ell^2(J)\), \(J\subseteq I\), are pairwise distinct, so \(\mathcal S(\mathcal K)\) has at least \(2^{2^{\aleph_0}}\) elements. A standard Borel space has at most \(2^{\aleph_0}\) points ([Lemma 1.3(3)](#oa-fnd-ef-01)). So no \(\sigma\)-algebra on \(\mathcal S(\mathcal K)\), the Effros one included, is standard. This is one concrete reason for working with separable spaces only.

## 5. Borel choice of dense sequences

\(E\) is still a separable Banach space. The choice functions are built by extending functionals one dimension at a time, with a parameter that fixes the choice at each step. The lemma records the one-dimensional step. Its part (4) is the estimate that the density proof needs.

**Lemma 5.1** (*one step*). Let \(p\) be a seminorm on a real vector space \(W\), \(V\subseteq W\) a subspace, \(x\in W\), and \(\varphi:V\to\mathbb R\) linear with \(\varphi\leq p\) on \(V\). Put
\[
L(\varphi)=\sup_{u\in V}\big(-p(x+u)-\varphi(u)\big),\qquad M(\varphi)=\inf_{u\in V}\big(p(x+u)-\varphi(u)\big).
\tag{5.1}
\]

1. \(-p(x)\leq L(\varphi)\leq M(\varphi)\leq p(x)\), and \(M(\varphi)=-L(-\varphi)\).
2. If \(x\notin V\), then for \(c\in\mathbb R\) the formula \(\varphi_c(u+\lambda x)=\varphi(u)+\lambda c\) (\(u\in V\), \(\lambda\in\mathbb R\)) defines a linear functional on \(V+\mathbb Rx\), and \(\varphi_c\leq p\) there if and only if \(L(\varphi)\leq c\leq M(\varphi)\).
3. If \(x\in V\), then \(L(\varphi)=M(\varphi)=\varphi(x)\).
4. (*Stability away from the boundary*) Let \(0\leq s<1\) and \(R=2p(x)/(1-s)\). If \(\varphi\leq sp\) on \(V\), the supremum and the infimum in (5.1) may be taken over \(\{u\in V:p(u)\leq R\}\) only. Consequently, if \(\varphi\) and \(\psi\) are linear on \(V\) with \(\varphi\leq sp\) and \(\psi\leq sp\), then
\[
\max\big(|L(\varphi)-L(\psi)|,\ |M(\varphi)-M(\psi)|\big)\leq\sup\{|\varphi(u)-\psi(u)|:u\in V,\ p(u)\leq R\}.
\tag{5.2}
\]

**Proof.** (1) Taking \(u=0\) gives \(L(\varphi)\geq-p(x)\) and \(M(\varphi)\leq p(x)\). For \(u,u'\in V\),
\(\varphi(u)-\varphi(u')=\varphi(u-u')\leq p(u-u')\leq p(x+u)+p(x+u')\),
so \(-p(x+u')-\varphi(u')\leq p(x+u)-\varphi(u)\). Taking the supremum over \(u'\) and the infimum over \(u\) gives \(L(\varphi)\leq M(\varphi)\). The identity \(M(\varphi)=-L(-\varphi)\) is a change of sign inside the supremum.

(2) \(\varphi_c\) is well defined because \(x\notin V\). For \(\lambda=0\) the bound is the hypothesis. For \(\lambda>0\), divide by \(\lambda\) and rename \(u/\lambda\) as \(u\): the bound holds for all such \(\lambda\) exactly when \(c\leq p(x+u)-\varphi(u)\) for all \(u\in V\), that is, \(c\leq M(\varphi)\). For \(\lambda<0\), divide by \(-\lambda\): the condition becomes \(\varphi(u)-c\leq p(u-x)\) for all \(u\in V\). Replacing \(u\) by \(-u\) and using \(p(-v)=p(v)\), this reads \(c\geq-p(x+u)-\varphi(u)\) for all \(u\), that is, \(c\geq L(\varphi)\).

(3) Take \(u=-x\) in (5.1): \(L(\varphi)\geq-\varphi(-x)=\varphi(x)\) and \(M(\varphi)\leq-\varphi(-x)=\varphi(x)\). Combine with (1).

(4) If \(\varphi\leq sp\) on \(V\), then \(-\varphi(u)=\varphi(-u)\leq sp(u)\). So for \(p(u)>R\),
\[
-p(x+u)-\varphi(u)\leq p(x)-(1-s)p(u)<-p(x)\leq L(\varphi),\qquad p(x+u)-\varphi(u)\geq(1-s)p(u)-p(x)>p(x)\geq M(\varphi),
\]
using \(p(x+u)\geq p(u)-p(x)\) and \((1-s)R=2p(x)\). Such \(u\) change neither the supremum nor the infimum. On the common set \(\{p(u)\leq R\}\), two suprema differ by at most the supremum of \(|\varphi(u)-\psi(u)|\), and so do two infima. \(\square\)

Part (4) needs the room \(s<1\). The next example shows that at a functional that is dominated by \(p\) but by no \(sp\) with \(s<1\), the function \(L\) can jump.

**Example 5.2** (*the bound \(L\) can jump at the boundary*). In \(\mathbb R^3\), let \(S\) be the circle \(\{(\cos\theta,\sin\theta,0)\}\), let \(I_\pm\) be the segments \(\{(\pm1,0,z):|z|\leq1\}\), and let \(K\) be the convex hull of \(S\cup I_+\cup I_-\). \(K\) is compact, convex and symmetric. It contains a neighbourhood of \(0\), since it contains the unit disc in the plane \(z=0\) and the points \((0,0,z)=\tfrac12(1,0,z)+\tfrac12(-1,0,z)\), \(|z|\leq1\). So \(\|w\|=\max_{k\in K}\langle k,w\rangle\) is a norm on \(E=\mathbb R^3\), and, identifying functionals with vectors through the dot product, \(E^*_1=K\). Take \(F=E^*\), so that \(p_F=\|\cdot\|\), and in [Lemma 5.1](#oa-fnd-ef-04) take \(V=\operatorname{span}\{e_1,e_2\}\) and \(x=e_3\). A functional \((a,b)\) on \(V\) satisfies \(\varphi\leq p\) exactly when it is the restriction of an element of \(K\) (by (D1)), that is, when \((a,b)\) lies in the closed unit disc. By Lemma 5.1(2), \([L(a,b),M(a,b)]=\{c:(a,b,c)\in K\}\).

- At \((1,0)\): on the generating set the first coordinate is at most \(1\), with equality only at \((1,0,0)\) and on \(I_+\). A point of \(K\) with first coordinate \(1\) is a convex combination of such points, so it lies in \(I_+\). Thus \([L,M]=[-1,1]\).
- At \((\cos\theta,\sin\theta)\) with \(0<\theta<\pi/2\): the functional \((a,b,c)\mapsto a\cos\theta+b\sin\theta\) is at most \(1\) on the generating set, with equality only at \((\cos\theta,\sin\theta,0)\); it equals \(\cos(\theta'-\theta)\) on \(S\) and \(\pm\cos\theta\) on \(I_\pm\). So \([L,M]=\{0\}\).

Hence \(L(\cos\theta,\sin\theta)=0\) for small \(\theta>0\), while \(L(1,0)=-1\). \(L\) is not continuous on the set of dominated functionals, at the boundary point \((1,0)\). Lemma 5.1(4) excludes such points by asking for \(\varphi\leq sp\) with \(s<1\), and Steps 4 and 5 of the proof of [Theorem 5.3](#oa-fnd-ef-04) below use continuity only there.

**Theorem 5.3** (*Borel choice*). There are Borel maps \(a_n:\mathfrak W(E^*)\to E^*_1\), \(n\geq1\), such that for every \(F\in\mathfrak W(E^*)\), each \(a_n(F)\) lies in \(F_1\) and \(\{a_n(F):n\geq1\}\) is weak\*-dense in \(F_1\).

*Reference:* [Takesaki I, Theorem IV.8.2]. Its density argument treats the bound \(L\) as a continuous function of the functional; Example 5.2 shows that this fails at the boundary. So Steps 4 and 5 below approximate the shrunken functional \(sg\) first, and then let \(s\to1\).

**Proof.** *Step 1: the construction for \(\mathbb K=\mathbb R\).* Fix a dense sequence \((x_k)_{k\geq1}\) in \(E\), and put \(V_0=\{0\}\) and \(V_k=\operatorname{span}\{x_1,\ldots,x_k\}\). Fix \(F\) and write \(p=p_F\). For a sequence \(t=(t_k)\) in \([0,1]\), define linear functionals \(\varphi_{t,k}\) on \(V_k\) with \(\varphi_{t,k}\leq p\), recursively. Start with \(\varphi_{t,0}=0\). Given \(\varphi_{t,k-1}\), let \(L\) and \(M\) be the numbers (5.1) for \(\varphi=\varphi_{t,k-1}\), \(V=V_{k-1}\) and \(x=x_k\), and put
\[
c_k=t_kL+(1-t_k)M.
\tag{5.3}
\]
If \(x_k\notin V_{k-1}\), let \(\varphi_{t,k}=(\varphi_{t,k-1})_{c_k}\) as in Lemma 5.1(2); it is \(\leq p\), because \(c_k\) lies between \(L\) and \(M\). If \(x_k\in V_{k-1}\), let \(\varphi_{t,k}=\varphi_{t,k-1}\); then \(c_k=\varphi_{t,k-1}(x_k)\) by Lemma 5.1(3). In both cases \(\varphi_{t,k}\) extends \(\varphi_{t,k-1}\) and \(\varphi_{t,k}(x_k)=c_k\). Together these functionals define a linear functional \(\varphi\) on \(\bigcup_kV_k\) with \(|\varphi|\leq p\leq\|\cdot\|\), since \(\varphi\leq p\) and \(p(-u)=p(u)\). It extends by continuity to some \(f^F_t\in E^*\) with \(|f^F_t|\leq p_F\), because \(p_F\) is continuous. So \(f_t^F\in F_1\) by [Proposition 3.2(3)](#oa-fnd-ef-03).

*Step 2: Borel dependence on \(F\).* Fix \(t\). We show by induction on \(k\) that \(F\mapsto f^F_t(x_j)=\varphi^F_{t,k}(x_j)\) is Borel for \(j\leq k\). Suppose this holds for \(k-1\). For \(q\in\mathbb Q^{k-1}\) put \(u_q=\sum_jq_jx_j\). The function \(u\mapsto-p_F(x_k+u)-\varphi^F_{t,k-1}(u)\) is continuous on \(V_{k-1}\), and the vectors \(u_q\) are dense in \(V_{k-1}\). So \(L^F\) is the supremum of the countably many functions
\[
F\mapsto-p_F(x_k+u_q)-\textstyle\sum_jq_j\varphi^F_{t,k-1}(x_j),
\]
which are Borel, by the definition of the Effros structure and the induction hypothesis. So \(F\mapsto L^F\) is Borel, and likewise \(F\mapsto M^F\). By (5.3), \(F\mapsto\varphi^F_{t,k}(x_k)=c^F_k\) is Borel. By [Proposition 3.2(7)](#oa-fnd-ef-03), \(F\mapsto f_t^F\in E^*_1\) is Borel.

*Step 3: every element of \(F_1\) is reached.* Let \(h\in F_1\). Choose \(t^*_k\) recursively. If \(\varphi_{t^*,k-1}=h\) on \(V_{k-1}\), then \(h(x_k)\) lies between the corresponding numbers \(L\) and \(M\), by Lemma 5.1(2) if \(x_k\notin V_{k-1}\) and by Lemma 5.1(3) otherwise. So there is \(t^*_k\in[0,1]\) with \(c_k=h(x_k)\), and then \(\varphi_{t^*,k}=h\) on \(V_k\). Thus \(f^F_{t^*}=h\).

*Step 4: continuity at interior functionals.* Now let \(h\in F_1\) satisfy \(|h|\leq sp_F\) for some \(s<1\), and let \(t^*\) be as in Step 3. For \(k\geq0\) let \(N_k=V_k\cap F_\perp\), and let \(Z_k\) be the space of linear functionals on \(V_k\) that vanish on \(N_k\). A functional \(\chi\) on \(V_k\) that is \(\leq p_F\) vanishes on \(N_k\), because \(\pm\chi(u)=\chi(\pm u)\leq p_F(\pm u)=0\) for \(u\in N_k\). So all \(\varphi_{t,k}\) and \(h|_{V_k}\) lie in \(Z_k\). On the finite-dimensional space \(Z_k\),
\[
\|\chi\|_*=\sup\{|\chi(u)|:u\in V_k,\ p_F(u)\leq1\}\quad\text{and}\quad|\chi|_k=\max_{j\leq k}|\chi(x_j)|
\]
are norms. (The first is finite because \(p_F\) is a norm on the finite-dimensional space \(V_k/N_k\); the second is a norm because \(x_1,\ldots,x_k\) span \(V_k\).) All norms on a finite-dimensional space are equivalent, so \(\|\chi\|_*\leq C_k|\chi|_k\) for a constant \(C_k\). We claim: for every \(\delta>0\) there is \(\eta>0\) such that \(|\varphi_{t,k}-h|_{V_k}|_k<\delta\) whenever \(\max_{j\leq k}|t_j-t^*_j|<\eta\). For \(k=0\) there is nothing to prove. Assume the claim for \(k-1\). Put \(s'=(1+s)/2\) and \(R'=2p_F(x_k)/(1-s')\), and choose \(\delta'\leq\delta\) with \(C_{k-1}\delta'\leq(1-s)/2\) and \(R'C_{k-1}\delta'<\delta/2\). Let \(\eta'\) be the number given by the claim for \(k-1\) and \(\delta'\), and take \(\eta\leq\eta'\) with \(2p_F(x_k)\eta<\delta/2\).

Suppose \(\max_{j\leq k}|t_j-t_j^*|<\eta\). By the claim for \(k-1\), \(\chi=\varphi_{t,k-1}-h|_{V_{k-1}}\) satisfies \(|\chi|_{k-1}<\delta'\), so \(\|\chi\|_*<(1-s)/2\). Hence \(\varphi_{t,k-1}\leq h+\tfrac{1-s}2p_F\leq s'p_F\) on \(V_{k-1}\); also \(h\leq s'p_F\). Apply (5.2) with \(s'\) and \(R'\) in place of \(s\) and \(R\); by homogeneity, its right-hand side is at most \(R'\|\chi\|_*\). So the numbers \(L,M\) for \(\varphi_{t,k-1}\) differ from the numbers \(L_*,M_*\) for \(h|_{V_{k-1}}\) by at most \(R'\|\chi\|_*\leq R'C_{k-1}\delta'<\delta/2\). Since
\[
c_k-h(x_k)=t_k(L-L_*)+(1-t_k)(M-M_*)+(t_k-t_k^*)(L_*-M_*)
\]
and \(|L_*-M_*|\leq2p_F(x_k)\), we get \(|\varphi_{t,k}(x_k)-h(x_k)|<\delta/2+2p_F(x_k)\eta<\delta\). For \(j<k\), \(|\varphi_{t,k}(x_j)-h(x_j)|=|\varphi_{t,k-1}(x_j)-h(x_j)|<\delta'\leq\delta\). This proves the claim for \(k\).

*Step 5: density.* Let \(T\) be the countable set of sequences in \([0,1]\cap\mathbb Q\) with only finitely many nonzero terms. We show that \(\{f_t^F:t\in T\}\) is weak\*-dense in \(F_1\). By [Proposition 3.2(7)](#oa-fnd-ef-03), with \(D=\{x_k\}\), it suffices, given \(g\in F_1\), \(n\geq1\) and \(\varepsilon>0\), to find \(t\in T\) with \(|f_t^F(x_j)-g(x_j)|<\varepsilon\) for \(j\leq n\). Choose \(s\in(0,1)\) with \((1-s)\|x_j\|<\varepsilon/2\) for \(j\leq n\), and put \(h=sg\). Then \(|h|\leq sp_F\) by [Proposition 3.2(3)](#oa-fnd-ef-03). By Steps 3 and 4 there is \(\eta>0\) such that \(|\varphi_{t,n}-h|_{V_n}|_n<\varepsilon/2\) whenever \(\max_{j\leq n}|t_j-t_j^*|<\eta\). Choose rational \(t_1,\ldots,t_n\in[0,1]\) with \(|t_j-t^*_j|<\eta\), and \(t_j=0\) for \(j>n\). Then \(t\in T\), and for \(j\leq n\),
\[
|f^F_t(x_j)-g(x_j)|\leq|\varphi_{t,n}(x_j)-h(x_j)|+(1-s)|g(x_j)|<\varepsilon.
\]
Enumerate \(T\) as \(t^{(1)},t^{(2)},\ldots\) and put \(a_n(F)=f^F_{t^{(n)}}\). This proves the theorem for \(\mathbb K=\mathbb R\).

*Step 6: \(\mathbb K=\mathbb C\).* Let \(E_{\mathbb R}\) be \(E\) regarded as a real Banach space. The map \(\rho(f)=\operatorname{Re}f\) is a real-linear bijection of \(E^*\) onto \((E_{\mathbb R})^*\), with inverse \(\rho^{-1}(g)(x)=g(x)-ig(ix)\). It preserves norms and is a homeomorphism for the weak\* topologies. For \(F\in\mathfrak W(E^*)\), \(\rho(F)\) is a weak\*-closed real subspace with \(\rho(F)_1=\rho(F_1)\), and \(p_{\rho(F)}=p_F\): for \(f\in F_1\) and \(x\in E\), a unimodular multiple of \(f\) lies in \(F_1\) and has real part \(|f(x)|\) at \(x\). Hence \(F\mapsto\rho(F)\) is Borel, by testing on generators ([Lemma 1.3(1)](#oa-fnd-ef-01)). If \(a_n^{\mathbb R}\) are the maps for \(E_{\mathbb R}\), then \(a_n(F)=\rho^{-1}(a_n^{\mathbb R}(\rho(F)))\) have the required properties. \(\square\)

**Corollary 5.4** (*measurability through dense sequences*). A map \(F:\Gamma\to\mathfrak W(E^*)\) is measurable if and only if there are measurable maps \(f_n:\Gamma\to E^*_1\), \(n\geq1\), such that for every \(\gamma\) each \(f_n(\gamma)\) lies in \(F(\gamma)_1\) and \(\{f_n(\gamma):n\geq1\}\) is weak\*-dense in \(F(\gamma)_1\).

**Proof.** If \(F\) is measurable, take \(f_n=a_n\circ F\). Conversely, \(p_{F(\gamma)}(x)=\sup_n|f_n(\gamma)(x)|\), because \(f\mapsto f(x)\) is weak\*-continuous and the \(f_n(\gamma)\) are dense in \(F(\gamma)_1\). Each term is measurable by [Proposition 3.2(7)](#oa-fnd-ef-03), so \(F\) is measurable by testing on generators ([Lemma 1.3(1)](#oa-fnd-ef-01)). \(\square\)

**Proposition 5.5** (*annihilators of measurable families*). Let \(y_n:\Gamma\to E\), \(n\geq1\), be measurable for the norm Borel structure of \(E\). Then \(\gamma\mapsto F(\gamma)=\{y_n(\gamma):n\geq1\}^\perp\) is a measurable map into \(\mathfrak W(E^*)\), and
\[
p_{F(\gamma)}(x)=\inf_q\Big\|x-\sum_nq_ny_n(\gamma)\Big\|,
\tag{5.4}
\]
the infimum over finitely supported sequences \(q\) with entries in \(\mathbb Q\) (for \(\mathbb K=\mathbb R\)) or \(\mathbb Q+i\mathbb Q\) (for \(\mathbb K=\mathbb C\)).

**Proof.** \(F(\gamma)\) is weak\*-closed, and \(F(\gamma)_\perp\) is the closed linear span of the \(y_n(\gamma)\) by (D2). By the distance formula ([Proposition 3.2(2)](#oa-fnd-ef-03)), \(p_{F(\gamma)}(x)=d(x,F(\gamma)_\perp)\), and the rational combinations are dense in that span. For fixed \(x\) and \(q\), the map \(\gamma\mapsto x-\sum_nq_ny_n(\gamma)\) is measurable into \(E\): addition is continuous, and the Borel sets of \(E\times E\) are generated by products of Borel sets ([Lemma 1.3(2)](#oa-fnd-ef-01)). Its norm is measurable, and (5.4) is a countable infimum. \(\square\)

## 6. Closed subspaces of a Hilbert space

Let \(\mathcal K\) be a separable Hilbert space, \(\mathcal S(\mathcal K)\) the set of its closed subspaces and \(\mathcal P(\mathcal K)\) the set of orthogonal projections on it. We identify \(K\in\mathcal S(\mathcal K)\) with its projection \(P_K\).

*The Effros structure.* The map \(\eta\mapsto\langle\cdot,\eta\rangle\) is a conjugate-linear isometric bijection of \(\mathcal K\) onto \(\mathcal K^*\), and it carries the weak topology of \(\mathcal K\) to the weak\* topology of \(\mathcal K^*\). Closed subspaces of \(\mathcal K\) are weakly closed, being convex. So \(K\mapsto\widehat K=\{\langle\cdot,\eta\rangle:\eta\in K\}\) is a bijection of \(\mathcal S(\mathcal K)\) onto \(\mathfrak W(\mathcal K^*)\), with \(\widehat K_\perp=K^\perp\) and
\[
p_{\widehat K}(\xi)=\sup\{|\langle\xi,\eta\rangle|:\eta\in K,\ \|\eta\|\leq1\}=\|P_K\xi\|.
\tag{6.1}
\]
We give \(\mathcal S(\mathcal K)\) and \(\mathcal P(\mathcal K)\) the Effros structure carried over by this bijection, which by (6.1) is \(\sigma(P\mapsto\|P\xi\|:\xi\in\mathcal K)\).

**Theorem 6.1.**

1. The Effros structure on \(\mathcal P(\mathcal K)\) is \(\sigma(P\mapsto\langle P\xi,\eta\rangle:\xi,\eta\in\mathcal K)\). The topology \(\tau_{\mathcal K}\) of [Theorem 4.1](#oa-fnd-ef-05), carried over to \(\mathcal P(\mathcal K)\), is the weak operator topology, and on \(\mathcal P(\mathcal K)\) it coincides with the strong operator topology. So \(\mathcal P(\mathcal K)\) with the strong operator topology is a Polish space, and its Borel sets are the Effros Borel sets.
2. (*Continuous choice*) For each \(\zeta\in\mathcal K\), the map \(P\mapsto P\zeta\) is continuous from \(\mathcal P(\mathcal K)\), with the strong operator topology, to \(\mathcal K\) with its norm. If \((\zeta_n)\) is norm-dense in the unit ball of \(\mathcal K\), then \(\{P\zeta_n:n\}\) is norm-dense in the unit ball of \(P\mathcal K\), for every \(P\).
3. (*Criterion*) For a map \(\gamma\mapsto K(\gamma)\in\mathcal S(\mathcal K)\) with projections \(P(\gamma)\), the following are equivalent:
   - (a) \(\gamma\mapsto K(\gamma)\) is measurable for the Effros structure;
   - (b) \(\gamma\mapsto P(\gamma)\) is *weakly measurable*: \(\gamma\mapsto\langle P(\gamma)\xi,\eta\rangle\) is measurable for all \(\xi,\eta\);
   - (c) there are measurable maps \(\xi_n:\Gamma\to\mathcal K\) such that \(K(\gamma)\) is the closed linear span of \(\{\xi_n(\gamma):n\}\) for every \(\gamma\).

   In that case \(\gamma\mapsto\dim K(\gamma)\in\{0,1,2,\ldots,\infty\}\) is measurable.

Here a map \(\Gamma\to\mathcal K\) is measurable for the norm Borel structure. By [Proposition 3.2(8)](#oa-fnd-ef-03), with \(\ell_j=\langle\cdot,\eta_j\rangle\) for a sequence \((\eta_j)\) that is dense in the unit ball, this is the same as weak measurability. It is also the notion of measurable section of the constant field \(\mathcal K\), as in the [example of constant fields](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-10).

**Proof.** (1) \(\|P\xi\|^2=\langle P\xi,\xi\rangle\), and since \(\langle P\xi,\eta\rangle=\langle P\xi,P\eta\rangle\), polarization gives \(\langle P\xi,\eta\rangle=\tfrac14\sum_{k=0}^3i^k\|P(\xi+i^k\eta)\|^2\). So each function of either family is a continuous function of finitely many functions of the other. The two families therefore generate the same \(\sigma\)-algebra and the same weakest topology, and for the second family that topology is the weak operator topology. The strong operator topology is finer. Conversely, if \(P_i\to P\) weakly along a net, then
\[
\|(P_i-P)\xi\|^2=\langle P_i\xi,\xi\rangle-2\operatorname{Re}\langle P_i\xi,P\xi\rangle+\langle P\xi,\xi\rangle\ \longrightarrow\ \langle P\xi,\xi\rangle-2\langle P\xi,P\xi\rangle+\langle P\xi,\xi\rangle=0 .
\]
The rest is [Theorem 4.1](#oa-fnd-ef-05) for \(E=\mathcal K\), carried over by \(K\mapsto\widehat K\).

(2) \(\|P\zeta-Q\zeta\|\) is small when \(Q\) is strongly close to \(P\). \(P\) is norm-continuous and maps the unit ball of \(\mathcal K\) onto the unit ball of \(P\mathcal K\), since \(Pv=v\) for \(v\in P\mathcal K\).

(3) (a)\(\Leftrightarrow\)(b) follows from (1) by testing on generators ([Lemma 1.3(1)](#oa-fnd-ef-01)). (b)\(\Rightarrow\)(c): take \(\xi_n(\gamma)=P(\gamma)\zeta_n\) for a sequence \((\zeta_n)\) that is dense in the unit ball of \(\mathcal K\). These maps are weakly measurable, hence measurable, and by (2) they are dense in the unit ball of \(K(\gamma)\), so their closed linear span is \(K(\gamma)\). (c)\(\Rightarrow\)(b): over \((\Gamma,\Sigma)\), the \(\xi_n\) are measurable sections of the constant field \(\mathcal K\). The projections onto the closed spans of countably many measurable sections [carry measurable sections to measurable sections](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-03): \(\gamma\mapsto P(\gamma)\xi(\gamma)\) is a measurable section for every measurable section \(\xi\), in particular for constant ones. So \(\gamma\mapsto\langle P(\gamma)\xi,\eta\rangle\) is measurable. The dimension of such a [subspace field](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-03) is a measurable function. \(\square\)

**Remark 6.2** (*a direct view of (1)*). Let \((\zeta_m)\) be dense in the unit ball of \(\mathcal K\). Then \(d(P,Q)=\sum_m2^{-m}\|(P-Q)\zeta_m\|\) is a metric for the strong operator topology on \(\mathcal P(\mathcal K)\). If \((P_k)\) is \(d\)-Cauchy, then \(P_k\zeta_m\) converges for every \(m\), hence \(P_k\xi\) converges for every \(\xi\), because \(\|P_k\|\leq1\). The limit \(x\) is self-adjoint, as a weak limit of self-adjoint operators, and \(x^2=x\), because \(P_k^2\xi-x^2\xi=P_k(P_k\xi-x\xi)+(P_k-x)x\xi\to0\). So \(d\) is complete. The map \(P\mapsto(P\zeta_m)_m\) embeds \(\mathcal P(\mathcal K)\) homeomorphically into the separable metrizable space \(\mathcal K^{\mathbb N}\), so \(\mathcal P(\mathcal K)\) is separable.

**Example 6.3** (*projections in finite and infinite dimension*). On \(\mathcal K=\mathbb C^2\), \(\mathcal P(\mathbb C^2)\) consists of \(0\), \(1\) and the rank-one projections. In finite dimension the strong and norm topologies agree, and \(\operatorname{rank}P=\operatorname{tr}P\) is continuous, so each rank stratum is open and closed. The rank-one projections are the matrices \(\tfrac12(1+a_1\sigma_1+a_2\sigma_2+a_3\sigma_3)\), with \((a_1,a_2,a_3)\) a unit vector and \(\sigma_j\) the Pauli matrices. Indeed, \(1,\sigma_1,\sigma_2,\sigma_3\) are a real basis of the self-adjoint matrices and the \(\sigma_j\) have trace \(0\), so a rank-one projection, being self-adjoint with trace \(1\), is \(\tfrac12(1+a\cdot\sigma)\) for some \(a\in\mathbb R^3\). And \(\big(\tfrac12(1+a\cdot\sigma)\big)^2=\tfrac14(1+|a|^2)+\tfrac12a\cdot\sigma\) for real \(a\), which is \(\tfrac12(1+a\cdot\sigma)\) exactly when \(|a|=1\). So \(\mathcal P(\mathbb C^2)\) is two points and a \(2\)-sphere, and the Effros Borel sets are the Borel sets of this compact space ([Theorem 6.1(1)](#oa-fnd-ef-06)).

On \(\mathcal K=\ell^2\) with basis \((\varepsilon_k)\), the projections \(P_k\) onto \(\mathbb C\varepsilon_k\) converge strongly to \(0\), since \(\|P_k\xi\|=|\langle\xi,\varepsilon_k\rangle|\to0\). So the rank-one projections do not form a closed set, and rank can drop in a limit. Rank is lower semicontinuous (Exercise 2), so each rank stratum is still Borel. Criterion (c) of [Theorem 6.1(3)](#oa-fnd-ef-06) allows jumps too. On \(\Gamma=[0,1]\) with its Borel sets, \(\xi(\gamma)=\gamma\varepsilon_1\) is continuous, and it spans \(\mathbb C\varepsilon_1\) for \(\gamma>0\) and \(0\) for \(\gamma=0\). The map \(\gamma\mapsto K(\gamma)\) is Effros-measurable and discontinuous at \(0\).

## 7. Isometries into one fixed space

Every measurable field of Hilbert spaces can be placed, fibre by fibre, inside one fixed Hilbert space, so that the images depend measurably on the point. This turns questions about fields into questions about subspaces and operators on a single space.

Let \(\mathcal K_0\) be a separable Hilbert space with orthonormal basis \((\varepsilon_k)_{1\leq k<1+\dim\mathcal K_0}\). For a family of isometries \(V(\gamma):H(\gamma)\to\mathcal K_0\), write
\[
P(\gamma)=V(\gamma)V(\gamma)^*,
\tag{7.1}
\]
the projection onto \(V(\gamma)H(\gamma)\).

**Theorem 7.1.**

1. (*Existence*) Let \((H(\gamma)),\mathfrak M\) be a measurable field over \((\Gamma,\Sigma)\) with \(\dim H(\gamma)\leq\dim\mathcal K_0\) for every \(\gamma\); this is automatic if \(\mathcal K_0\) is infinite-dimensional. Let \((e_k)\) be its [orthonormal fundamental sequence](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-02): the \(e_k\) are measurable sections, \(e_k(\gamma)\neq0\) exactly for \(k\leq n(\gamma)=\dim H(\gamma)\), and the nonzero \(e_k(\gamma)\) form an orthonormal basis of \(H(\gamma)\). Put
\[
V(\gamma)v=\sum_{k\leq n(\gamma)}\langle v,e_k(\gamma)\rangle\varepsilon_k,\qquad v\in H(\gamma).
\tag{7.2}
\]
Then \(V(\gamma)\) is an isometry, \(V(\gamma)H(\gamma)\) is the closed span of \(\{\varepsilon_k:k\leq n(\gamma)\}\), and \(V(\gamma)^*\varepsilon_k=e_k(\gamma)\) for every \(k\). The map \(\gamma\mapsto V(\gamma)H(\gamma)\) is Effros-measurable. A section \(\xi\) is measurable if and only if \(\gamma\mapsto V(\gamma)\xi(\gamma)\) is a measurable map into \(\mathcal K_0\).
2. (*Converse*) Let \((H(\gamma))\) be any family of Hilbert spaces, and \(V(\gamma):H(\gamma)\to\mathcal K_0\) isometries such that \(\gamma\mapsto V(\gamma)H(\gamma)\) is Effros-measurable. Then
\[\mathfrak M_V=\{\xi:\ \gamma\mapsto V(\gamma)\xi(\gamma)\ \text{is measurable}\}\tag{7.3}\]
is a measurable field of Hilbert spaces with fundamental sequence \((V^*\varepsilon_k)_k\), and it is the only measurable field containing all the sections \(V^*\varepsilon_k\).
3. (*Operator fields*) Let \((H(\gamma)),\mathfrak M_V\) and \((K(\gamma)),\mathfrak M_W\) be fields as in (2), with isometries \(V\) and \(W\) into \(\mathcal K_0\). A family \(x(\gamma)\in B(H(\gamma),K(\gamma))\) is a [measurable field of bounded operators](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-05) if and only if \(\gamma\mapsto W(\gamma)x(\gamma)V(\gamma)^*\in B(\mathcal K_0)\) is weakly measurable.
4. (*Strata*) For \(d\in\{0,1,2,\ldots,\infty\}\) let \(\Gamma_d=\{\gamma:\dim H(\gamma)=d\}\), the [dimension strata](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-04) of the field, and let \(\ell^2_d\) be \(\mathbb C^d\) (\(\ell^2(\mathbb N)\) when \(d=\infty\)) with standard basis \((\varepsilon_k)\). On \(\Gamma_d\), \(V(\gamma)=J_dU(\gamma)\), where \(U(\gamma):H(\gamma)\to\ell^2_d\) is the unitary \(U(\gamma)v=\sum_{k\leq d}\langle v,e_k(\gamma)\rangle\varepsilon_k\) and \(J_d:\ell^2_d\to\mathcal K_0\) is the isometry with \(J_d\varepsilon_k=\varepsilon_k\).

By (1), every measurable field is of the form in (2), with \(\mathfrak M=\mathfrak M_V\) as in (7.3). So (3) applies to all measurable fields.

**Proof.** (1) \(V(\gamma)\) carries the orthonormal basis \((e_k(\gamma))_{k\leq n(\gamma)}\) of \(H(\gamma)\) to the orthonormal family \((\varepsilon_k)_{k\leq n(\gamma)}\), so it is an isometry with the stated range. For \(v\in H(\gamma)\), \(\langle v,V(\gamma)^*\varepsilon_k\rangle=\langle V(\gamma)v,\varepsilon_k\rangle\) equals \(\langle v,e_k(\gamma)\rangle\) if \(k\leq n(\gamma)\) and \(0\) otherwise. Since \(e_k(\gamma)=0\) for \(k>n(\gamma)\), \(V(\gamma)^*\varepsilon_k=e_k(\gamma)\) in both cases. The projection onto the range is \(P(\gamma)=\sum_k1_{\{n\geq k\}}(\gamma)\langle\cdot,\varepsilon_k\rangle\varepsilon_k\), so
\[
\langle P(\gamma)\zeta,\eta\rangle=\sum_k1_{\{n\geq k\}}(\gamma)\langle\zeta,\varepsilon_k\rangle\langle\varepsilon_k,\eta\rangle
\]
is measurable, because the dimension function \(n\) is measurable. By criterion (b) of [Theorem 6.1(3)](#oa-fnd-ef-06), \(\gamma\mapsto V(\gamma)H(\gamma)\) is Effros-measurable. Finally, \(\langle V(\gamma)\xi(\gamma),\varepsilon_k\rangle=\langle\xi(\gamma),e_k(\gamma)\rangle\). A map \(f\) into \(\mathcal K_0\) is measurable exactly when all its coordinates are, since \(\langle f,\eta\rangle=\sum_k\langle f,\varepsilon_k\rangle\langle\varepsilon_k,\eta\rangle\) and measurability is the same as weak measurability ([Proposition 3.2(8)](#oa-fnd-ef-03), as noted after [Theorem 6.1](#oa-fnd-ef-06)). So \(V\xi\) is measurable if and only if every \(\langle\xi,e_k\rangle\) is measurable, which is the [testing criterion](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-02) for \(\xi\in\mathfrak M\): a section is measurable if and only if its inner products with the members of one fundamental sequence are measurable.

(2) \(\mathfrak M_V\) is a linear subspace. (F1) holds because \(\|\xi(\gamma)\|=\|V(\gamma)\xi(\gamma)\|\), the norm of a measurable map. The sections \(\xi_k=V^*\varepsilon_k\) lie in \(\mathfrak M_V\), because \(V(\gamma)\xi_k(\gamma)=P(\gamma)\varepsilon_k\) and \(P\) is weakly measurable by [Theorem 6.1(3)](#oa-fnd-ef-06). They are total in each \(H(\gamma)\), because \(V(\gamma)^*\) maps \(\mathcal K_0\) onto \(H(\gamma)\) (as \(V(\gamma)^*V(\gamma)=1\)) and the \(\varepsilon_k\) are total. This is (F3). For (F2), let \(\eta\) be a section with \(\langle\eta,\xi\rangle\) measurable for every \(\xi\in\mathfrak M_V\). Then \(\langle V(\gamma)\eta(\gamma),\varepsilon_k\rangle=\langle\eta(\gamma),\xi_k(\gamma)\rangle\) is measurable for every \(k\), so \(V\eta\) is measurable and \(\eta\in\mathfrak M_V\). Uniqueness holds because a total sequence of sections with measurable Gram functions lies in [only one measurable field](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-02); here the Gram functions \(\langle\xi_j,\xi_k\rangle=\langle P\varepsilon_j,\varepsilon_k\rangle\) are measurable.

(3) Put \(y(\gamma)=W(\gamma)x(\gamma)V(\gamma)^*\), \(\xi_j=V^*\varepsilon_j\) and \(\zeta_k=W^*\varepsilon_k\). For all \(j,k\),
\[
\langle y(\gamma)\varepsilon_j,\varepsilon_k\rangle=\langle x(\gamma)\xi_j(\gamma),\zeta_k(\gamma)\rangle.
\tag{7.4}
\]
If \(x\) is measurable, then \(x\xi_j\in\mathfrak M_W\), so (7.4) is measurable, since inner products of measurable sections are [measurable functions](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-01). Then \(y\) is weakly measurable: \(y(\gamma)\) is bounded, so \(\langle y(\gamma)\zeta,\eta\rangle\) is the limit, as \(m\to\infty\), of the finite sums \(\sum_{j,k\leq m}\langle\zeta,\varepsilon_j\rangle\langle\varepsilon_k,\eta\rangle\langle y(\gamma)\varepsilon_j,\varepsilon_k\rangle\). Conversely, if \(y\) is weakly measurable, (7.4) shows that \(\langle x\xi_j,\zeta_k\rangle\) is measurable for all \(k\). Since \((\zeta_k)\) is a fundamental sequence of \(\mathfrak M_W\), the [testing criterion for sections](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-02) gives \(x\xi_j\in\mathfrak M_W\). Since \((\xi_j)\) is a fundamental sequence of \(\mathfrak M_V\), \(x\) is measurable by the [testing criterion for operator fields](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-05).

(4) Compare (7.2) with the formula for \(U(\gamma)\). \(\square\)

**Remarks 7.2.** (a) The dimension condition in (1) is necessary, since an isometry \(H(\gamma)\to\mathcal K_0\) exists only if \(\dim H(\gamma)\leq\dim\mathcal K_0\). (b) The stratified form (4), with unitaries onto a fixed space of dimension \(d\) on each \(\Gamma_d\), is often the convenient one; [Theorem 10.3(5)](#oa-fnd-ef-10) covers it for families of von Neumann algebras. (c) With these isometries, the passage from constant fields to general fields in the theory of [decomposable operators](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-07) applies to every measurable field.

## 8. Adjoints and commutants

Let \(\mathcal K\) be a separable Hilbert space. We apply Sections 3–5 with \(E=B(\mathcal K)_*\): [the Effros structure](#oa-fnd-ef-03), [its Polish topology](#oa-fnd-ef-05) and [the Borel choice maps](#oa-fnd-ef-04). By (P2), \(E^*=B(\mathcal K)\) and the weak\* topology is the \(\sigma\)-weak topology. So \(\mathfrak W(B(\mathcal K))=\mathfrak W(E^*)\) is the set of \(\sigma\)-weakly closed subspaces of \(B(\mathcal K)\), and
\[
p_M(\psi)=\sup\{|\psi(x)|:x\in M_1\},\qquad\psi\in B(\mathcal K)_*,\quad M_1=M\cap B(\mathcal K)_1 .
\]
For \(M\in\mathfrak W(B(\mathcal K))\), \(M^*=\{x^*:x\in M\}\), and \(M'\) is the commutant.

A map \(a:\Gamma\to B(\mathcal K)\) is *weakly measurable* if \(\gamma\mapsto\langle a(\gamma)\xi,\eta\rangle\) is measurable for all \(\xi,\eta\in\mathcal K\). These maps are exactly the measurable fields of bounded operators on the constant field \(\mathcal K\) over \((\Gamma,\Sigma)\), by the [matrix-entry criterion](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-07) together with the finite-sum argument in the proof of [Theorem 7.1(3)](#oa-fnd-ef-07).

**Lemma 8.1.**

1. \(B(\mathcal K)_*\) is separable. If \((b_j)\) is a sequence that is \(\sigma\)-weakly dense in \(B(\mathcal K)_1\), then \(\|\psi\|=\sup_j|\psi(b_j)|\) for \(\psi\in B(\mathcal K)_*\), and the norm Borel structure of \(B(\mathcal K)_*\) is \(\sigma(\psi\mapsto\psi(b_j):j\geq1)\). Such sequences exist.
2. Weakly measurable maps are closed under sums, products, adjoints, and multiplication by measurable scalar functions. If \(a\) is weakly measurable, then \(\gamma\mapsto\|a(\gamma)\|\) and \(\gamma\mapsto\psi(a(\gamma))\), \(\psi\in B(\mathcal K)_*\), are measurable. A map into \(B(\mathcal K)_1\) is weakly measurable if and only if it is measurable for the \(\sigma\)-weak Borel structure of \(B(\mathcal K)_1\).

**Proof.** (1) By (P1), \(\psi=\sum_n\omega_n\) with \(\omega_n(x)=\langle x\xi_n,\eta_n\rangle\), and \(\|\omega_n\|\leq\|\xi_n\|\|\eta_n\|\), which is summable. So the finite sums of functionals \(x\mapsto\langle x\xi,\eta\rangle\) are norm-dense. The norm of \(x\mapsto\langle x\xi,\eta\rangle-\langle x\xi',\eta'\rangle\) is at most \(\|\xi-\xi'\|\|\eta\|+\|\xi'\|\|\eta-\eta'\|\), so vectors from a countable dense set and Gaussian-rational coefficients give a countable dense set. By (P2), \(\|\psi\|=\sup\{|\psi(x)|:x\in B(\mathcal K)_1\}\), and \(\psi\) is \(\sigma\)-weakly continuous, so the supremum over \((b_j)\) is the same. The description of the Borel structure is [Proposition 3.2(8)](#oa-fnd-ef-03). Finally, \(B(\mathcal K)_1\) with the \(\sigma\)-weak topology is compact and metrizable ([Proposition 3.2(7)](#oa-fnd-ef-03) for \(E=B(\mathcal K)_*\)), hence separable, so such \((b_j)\) exist.

(2) Let \((\varepsilon_k)\) be an orthonormal basis of \(\mathcal K\). Parseval's identity gives \(\langle a(\gamma)b(\gamma)\xi,\eta\rangle=\langle b(\gamma)\xi,a(\gamma)^*\eta\rangle=\sum_k\langle b(\gamma)\xi,\varepsilon_k\rangle\langle a(\gamma)\varepsilon_k,\eta\rangle\), a pointwise convergent series of measurable functions. \(\langle a(\gamma)^*\xi,\eta\rangle\) is the conjugate of \(\langle a(\gamma)\eta,\xi\rangle\). Sums and scalar multiples are clear. \(\|a(\gamma)\|=\sup_{m,n}|\langle a(\gamma)\zeta_m,\zeta_n\rangle|\) for a sequence \((\zeta_m)\) that is dense in the unit ball of \(\mathcal K\). With (P1), \(\psi(a(\gamma))=\sum_n\langle a(\gamma)\xi_n,\eta_n\rangle\), which converges absolutely for each \(\gamma\). The last sentence follows from [Proposition 3.2(7)](#oa-fnd-ef-03): \(\sigma\)-weak measurability means that \(\gamma\mapsto\psi(a(\gamma))\) is measurable for all \(\psi\in B(\mathcal K)_*\), and the functionals \(x\mapsto\langle x\xi,\eta\rangle\) belong to \(B(\mathcal K)_*\). \(\square\)

**Theorem 8.2.**

1. \(M\mapsto M^*\) is a Borel bijection of \(\mathfrak W(B(\mathcal K))\) onto itself, equal to its own inverse.
2. (*Commutants of measurable families*) If \(a_i:\Gamma\to B(\mathcal K)\), \(i\geq1\), are weakly measurable, then \(\gamma\mapsto\{a_i(\gamma):i\geq1\}'\) is a measurable map into \(\mathfrak W(B(\mathcal K))\).
3. \(M\mapsto M'\) is a Borel map of \(\mathfrak W(B(\mathcal K))\) into itself.

Part (2) applies to any countable weakly measurable family, bounded or not, and Sections 9 and 10 rest on it.

**Proof.** (1) For \(\psi\in B(\mathcal K)_*\) put \(\psi^\sharp(x)=\overline{\psi(x^*)}\). If \(\psi(x)=\sum_n\langle x\xi_n,\eta_n\rangle\), then \(\psi^\sharp(x)=\sum_n\langle x\eta_n,\xi_n\rangle\), so \(\psi^\sharp\in B(\mathcal K)_*\). Hence the adjoint map is \(\sigma\)-weakly continuous, \(M^*\in\mathfrak W(B(\mathcal K))\), and \((M^*)_1=(M_1)^*\). So
\[
p_{M^*}(\psi)=\sup_{x\in M_1}|\psi(x^*)|=\sup_{x\in M_1}|\psi^\sharp(x)|=p_M(\psi^\sharp),
\]
and \(M\mapsto M^*\) is Borel by testing on generators ([Lemma 1.3(1)](#oa-fnd-ef-01)). Clearly \((M^*)^*=M\).

(2) For \(a\in B(\mathcal K)\) and \(\psi\in B(\mathcal K)_*\) define \(a,\psi=\psi(xa-ax)\). It lies in \(B(\mathcal K)_*\), since \(x\mapsto xa-ax\) is \(\sigma\)-weakly continuous. Let \(\Psi\) be a countable dense subset of \(B(\mathcal K)_*\). By (P2), \(\Psi\) separates the points of \(B(\mathcal K)\), so \(\psi(xa-ax)=0\) for all \(\psi\in\Psi\) exactly when \(xa=ax\). Hence
\[
\{a_i(\gamma):i\}'=\{[a_i(\gamma),\psi]:\ i\geq1,\ \psi\in\Psi\}^\perp .
\]
By [Proposition 5.5](#oa-fnd-ef-04) on annihilators, it suffices that \(\gamma\mapsto[a_i(\gamma),\psi]\) is measurable into \(B(\mathcal K)_*\). By Lemma 8.1(1), it suffices that \(\gamma\mapstoa_i(\gamma),\psi=\psi(b_ja_i(\gamma)-a_i(\gamma)b_j)\) is measurable for each \(j\), and this holds by Lemma 8.1(2).

(3) Let \(a_n\) be the maps of [Theorem 5.3](#oa-fnd-ef-04) for \(E=B(\mathcal K)_*\). For \(M\in\mathfrak W(B(\mathcal K))\), \(M'=\{a_n(M):n\}'\). One inclusion holds because \(a_n(M)\in M\). For the other, if \(x\) commutes with every \(a_n(M)\), it commutes with every element of \(M_1\), since \(y\mapsto xy-yx\) is \(\sigma\)-weakly continuous and the \(a_n(M)\) are \(\sigma\)-weakly dense in \(M_1\); so it commutes with \(M\). The \(a_n\) are weakly measurable by Lemma 8.1(2), so (2) applies with \(\Gamma=\mathfrak W(B(\mathcal K))\). \(\square\)

## 9. The Borel space of von Neumann algebras

Let \(\mathrm{vN}(\mathcal K)\) be the set of von Neumann algebras on \(\mathcal K\), with the Borel structure induced from \(\mathfrak W(B(\mathcal K))\).

**Theorem 9.1.**

1. \(\mathrm{vN}(\mathcal K)=\{M\in\mathfrak W(B(\mathcal K)):M^*=M\text{ and }M''=M\}\). It is a Borel subset of \(\mathfrak W(B(\mathcal K))\), and a standard Borel space.
2. (*Borel choice of generators*) There are Borel maps \(a_n:\mathrm{vN}(\mathcal K)\to B(\mathcal K)_1\) with \(a_n(M)\in M_1\) and \(\{a_n(M):n\}\) \(\sigma\)-weakly dense in \(M_1\). In particular \(M\) is generated by \(\{a_n(M):n\}\).
3. (*Measurability criterion*) A map \(\gamma\mapsto M(\gamma)\in\mathrm{vN}(\mathcal K)\) is measurable if and only if there are weakly measurable maps \(a_i:\Gamma\to B(\mathcal K)\), \(i\geq1\), such that \(M(\gamma)\) is generated by \(\{a_i(\gamma):i\}\) for every \(\gamma\). When \(M\) is measurable, the \(a_i\) can be chosen with values in \(B(\mathcal K)_1\) and \(\sigma\)-weakly dense in \(M(\gamma)_1\).
4. (*Intersections, joins and commutants*) The maps \((M,N)\mapsto M\cap N\) and \((M,N)\mapsto M\vee N\) are Borel from \(\mathrm{vN}(\mathcal K)\times\mathrm{vN}(\mathcal K)\) to \(\mathrm{vN}(\mathcal K)\), and \(M\mapsto M'\) is a Borel map of \(\mathrm{vN}(\mathcal K)\) into itself.
5. (*Factors*) The set of factors is a Borel subset of \(\mathrm{vN}(\mathcal K)\), and a standard Borel space.

**Proof.** (1) A von Neumann algebra is \(\sigma\)-weakly closed (see the Conventions), self-adjoint, and equal to its bicommutant. Conversely, let \(M\in\mathfrak W(B(\mathcal K))\) satisfy \(M^*=M\) and \(M''=M\). A commutant is always a unital algebra, and the commutant of a self-adjoint set is self-adjoint. So \(M'\) and \(M''=M\) are unital \(*\)-algebras, and \(M\) is a von Neumann algebra. The maps \(M\mapsto M^*\) and \(M\mapsto M''\) are Borel by [Theorem 8.2](#oa-fnd-ef-08), and fixed-point sets of Borel maps are Borel ([Proposition 3.2(6)](#oa-fnd-ef-03)); so the set is Borel. \(\mathfrak W(B(\mathcal K))\) is standard by [Theorem 4.1](#oa-fnd-ef-05), and Borel subsets of standard Borel spaces are standard by [Theorem 2.2](#oa-fnd-ef-02).

(2) Restrict the maps of [Theorem 5.3](#oa-fnd-ef-04) to \(\mathrm{vN}(\mathcal K)\). The von Neumann algebra generated by \(\{a_n(M)\}\) is \(\sigma\)-weakly closed and contains the \(a_n(M)\), hence \(M_1\) and \(M\). It is contained in \(M\), since \(M\) is a von Neumann algebra containing the \(a_n(M)\).

(3) If \(M\) is measurable, the maps \(a_i\circ M\), with \(a_i\) from (2), are measurable into \(B(\mathcal K)_1\), hence weakly measurable ([Lemma 8.1(2)](#oa-fnd-ef-08)), and they generate \(M(\gamma)\). Conversely, let \(S(\gamma)=\{a_i(\gamma),a_i(\gamma)^*:i\}\), a countable family of weakly measurable maps ([Lemma 8.1(2)](#oa-fnd-ef-08)). Then \(\gamma\mapsto S(\gamma)'\) is measurable by [Theorem 8.2(2)](#oa-fnd-ef-08), and \(\gamma\mapsto S(\gamma)''=M(\gamma)\) is measurable by [Theorem 8.2(3)](#oa-fnd-ef-08).

(4) Let \(a_n\) be as in (2), and give \(\mathrm{vN}(\mathcal K)\times\mathrm{vN}(\mathcal K)\) the product \(\sigma\)-algebra. The maps \((M,N)\mapsto a_i(M)\) and \((M,N)\mapsto a_j(N)\) are weakly measurable, and so are \((M,N)\mapsto a_i(M')\) and \((M,N)\mapsto a_j(N')\), because \(M\mapsto M'\) is Borel ([Theorem 8.2(3)](#oa-fnd-ef-08)) and maps \(\mathrm{vN}(\mathcal K)\) into itself. Now
\[
M\vee N=\big((M\cup N)'\big)'=(M'\cap N')'=\big(\{a_i(M),a_j(N):i,j\}'\big)',\qquad M\cap N=(M'\cup N')'=\{a_i(M'),a_j(N'):i,j\}' .
\]
The second formula and the inner commutant of the first are measurable by [Theorem 8.2(2)](#oa-fnd-ef-08), and the outer commutant is measurable by [Theorem 8.2(3)](#oa-fnd-ef-08). The last claim is [Theorem 8.2(3)](#oa-fnd-ef-08), since the commutant of a von Neumann algebra is one.

(5) The set is \(\{M:M\cap M'=\mathbb C1\}\). The map \(M\mapsto M\cap M'\) is Borel by (4), as the composite of \(M\mapsto(M,M')\) with the intersection map, and \(\{\mathbb C1\}\) is a point. Points are Borel ([Proposition 3.2(6)](#oa-fnd-ef-03)), so the set of factors is Borel, and it is standard by [Theorem 2.2](#oa-fnd-ef-02). \(\square\)

**Remarks 9.2.** (a) Part (3) needs no bound on the generators, and part (2) supplies generators in the unit ball. (b) The restriction of the topology \(\tau_E\) of [Theorem 4.1](#oa-fnd-ef-05), for \(E=B(\mathcal K)_*\), to \(\mathrm{vN}(\mathcal K)\) is known as the Effros–Maréchal topology. It is Polish when \(\mathcal K\) is separable; see [Ando–Haagerup–Winsløw, Section 2.4], which refers to Haagerup and Winsløw for the original definition. By [Theorem 2.1(2)](#oa-fnd-ef-02) this makes \(\mathrm{vN}(\mathcal K)\) a \(G_\delta\) subset of \((\mathfrak W(B(\mathcal K)),\tau_E)\). This lesson does not use these facts.

**Example 9.3** (*von Neumann algebras on \(\mathbb C^2\)*). Here \(\mathrm{vN}(\mathbb C^2)\) consists of \(\mathbb C1\), \(M_2(\mathbb C)\), and the algebras \(D_P=\mathbb CP+\mathbb C(1-P)\) with \(P\) a rank-one projection; note \(D_P=D_{1-P}\). Indeed, suppose a von Neumann algebra \(M\) contains a self-adjoint element \(h\) that is not scalar. Then \(h\) has two distinct eigenvalues, its spectral projections \(P\) and \(1-P\) are polynomials in \(h\), and \(M\supseteq D_P\). An operator commuting with \(P\) preserves its range and kernel, which are lines, so \(D_P'=D_P\). Hence \(M'\subseteq D_P\), and \(M'\), a unital \(*\)-subalgebra of \(D_P\cong\mathbb C^2\), is \(\mathbb C1\) or \(D_P\). Then \(M=M''\) is \(M_2(\mathbb C)\) or \(D_P\). If \(M\) contains no such \(h\), then \(M=\mathbb C1\), because \(M\) is spanned by its self-adjoint elements.

The Effros functions are explicit. The unit ball of \(D_P\) is \(\{aP+b(1-P):|a|,|b|\leq1\}\), so for every functional \(\psi\) on \(M_2(\mathbb C)\),
\[
p_{\mathbb C1}(\psi)=|\psi(1)|,\qquad p_{D_P}(\psi)=|\psi(P)|+|\psi(1-P)|,\qquad p_{M_2(\mathbb C)}(\psi)=\|\psi\| .
\]
The commutant map exchanges \(\mathbb C1\) and \(M_2(\mathbb C)\) and fixes each \(D_P\). The factors are \(\mathbb C1\) and \(M_2(\mathbb C)\). The map \(P\mapsto D_P\) on the sphere of Example 6.3 is Borel, by [Theorem 9.1(3)](#oa-fnd-ef-09) with the single generator \(P\), and it identifies \(P\) with \(1-P\), the antipodal point \(-a\).

**Example 9.4** (*one continuous generator, a wildly varying algebra*). Let \(\mathcal K=\ell^2(\mathbb Z)\) with basis \((\varepsilon_m)\), and for \(\gamma\in[0,1)\) let \(u_\gamma\) be the unitary with \(u_\gamma\varepsilon_m=e^{2\pi i\gamma m}\varepsilon_m\). Then \(\langle u_\gamma\xi,\eta\rangle=\sum_me^{2\pi i\gamma m}\langle\xi,\varepsilon_m\rangle\langle\varepsilon_m,\eta\rangle\) is continuous in \(\gamma\), so by [Theorem 9.1(3)](#oa-fnd-ef-09) the map \(\gamma\mapsto M(\gamma)=\{u_\gamma,u_\gamma^*\}''\) is Borel. Its values are these.

- An operator \(x\) commutes with \(u_\gamma\) exactly when \(\langle x\varepsilon_m,\varepsilon_{m'}\rangle\big(e^{2\pi i\gamma m}-e^{2\pi i\gamma m'}\big)=0\) for all \(m,m'\). It then commutes with \(u_\gamma^*=u_\gamma^{-1}\) as well.
- If \(\gamma\) is irrational, the eigenvalues \(e^{2\pi i\gamma m}\) are distinct. So \(\{u_\gamma\}'\) is the algebra of diagonal operators, which is its own commutant by the same computation. Thus \(M(\gamma)=\ell^\infty(\mathbb Z)\), acting diagonally, is maximal abelian.
- If \(\gamma=p/q\) in lowest terms, the eigenvalue depends only on \(m\bmod q\) and takes \(q\) distinct values. So \(\{u_\gamma\}'\) consists of the operators that preserve each subspace \(\ell^2(r+q\mathbb Z)\), and its commutant \(M(\gamma)\) is spanned by the \(q\) projections onto these subspaces. So \(\dim M(\gamma)=q\), and in particular \(M(0)=\mathbb C1\).

So \(\gamma\mapsto M(\gamma)\) is Borel although it varies wildly. The set where \(M(\gamma)\) is maximal abelian is the set of irrationals, and the set of factors is \(\{0\}\). \(\dim M(\gamma)\) is finite exactly at the rationals, where it equals the denominator, and infinite at the irrationals; both sets are dense. The two sets named are Borel, as Exercise 3 and [Theorem 9.1(5)](#oa-fnd-ef-09) predict.

## 10. Measurably generated families of von Neumann algebras

Let \((H(\gamma)),\mathfrak M\) be a measurable field over \((\Gamma,\Sigma)\). Fix isometries \(V(\gamma):H(\gamma)\to\mathcal K_0\) with \(\mathfrak M=\mathfrak M_V\), for instance those of [Theorem 7.1(1)](#oa-fnd-ef-07), and let \(P(\gamma)\) be as in (7.1). Then \(\gamma\mapsto V(\gamma)H(\gamma)\) is Effros-measurable by criterion (c) of [Theorem 6.1(3)](#oa-fnd-ef-06): for a fundamental sequence \((\xi_n)\) of \(\mathfrak M\), the maps \(V\xi_n\) are measurable, and their values at \(\gamma\) span a dense subspace of \(V(\gamma)H(\gamma)\). So [Theorem 7.1(2)–(3)](#oa-fnd-ef-07) apply to \(V\). For a von Neumann algebra \(M\) on \(H(\gamma)\) put
\[
\iota_\gamma(M)=V(\gamma)MV(\gamma)^*+\mathbb C\big(1-P(\gamma)\big)\subseteq B(\mathcal K_0).
\tag{10.1}
\]

**Definition 10.1.** A family \((M(\gamma))_{\gamma\in\Gamma}\), with \(M(\gamma)\) a von Neumann algebra on \(H(\gamma)\), is *measurably generated* if there are [measurable fields of bounded operators](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-05) \(x_n\), \(n\geq1\), such that \(M(\gamma)\) is generated by \(\{x_n(\gamma):n\}\) for every \(\gamma\).

For direct integrals one also meets the variant that asks this only for almost every \(\gamma\), with respect to a given measure. That variant is not treated here.

**Lemma 10.2** (*direct sums*). Let \(\mathcal K_0=K_1\oplus K_2\), with \(P\) the projection onto \(K_1\). For linear subspaces \(S_1\subseteq B(K_1)\) with \(1_{K_1}\in S_1\) and \(S_2\subseteq B(K_2)\), write \(S_1\oplus S_2\) for the set of operators \(s_1\oplus s_2\) with \(s_i\in S_i\). Then \((S_1\oplus S_2)'=S_1'\oplus S_2'\), where \(S_i'\) is the commutant in \(B(K_i)\). Consequently, take \(K_1=V(\gamma)H(\gamma)\), let \(V_0:H(\gamma)\to K_1\) be the unitary induced by \(V(\gamma)\), and let \(M,N\) be von Neumann algebras on \(H(\gamma)\). Then:

- (a) \(\iota_\gamma(M)=V_0MV_0^*\oplus\mathbb C1_{K_2}\) belongs to \(\mathrm{vN}(\mathcal K_0)\), and \(\iota_\gamma(M)'=V_0M'V_0^*\oplus B(K_2)\);
- (b) \(V(\gamma)^*\iota_\gamma(M)V(\gamma)=M\) and \(V(\gamma)^*\iota_\gamma(M)'V(\gamma)=M'\), and the compression \(y\mapsto V(\gamma)^*yV(\gamma)\) maps the unit balls of \(\iota_\gamma(M)\) and \(\iota_\gamma(M)'\) onto those of \(M\) and \(M'\);
- (c) \(\iota_\gamma(M\cap N)=\iota_\gamma(M)\cap\iota_\gamma(N)\), \(\iota_\gamma(M\vee N)=\iota_\gamma(M)\vee\iota_\gamma(N)\) and \(\iota_\gamma(\mathbb C1)=\mathbb CP(\gamma)+\mathbb C(1-P(\gamma))\); and \(\iota_\gamma\) is injective.

**Proof.** \(1_{K_1}\oplus0\) lies in \(S_1\oplus S_2\), so an operator \(y\) in the commutant commutes with \(P\) and has the form \(y_1\oplus y_2\). It commutes with every \(s_1\oplus0\) and \(0\oplus s_2\) exactly when \(y_1\in S_1'\) and \(y_2\in S_2'\).

(a) Apply this with \(S_1=V_0MV_0^*\), \(S_2=\mathbb C1\), and then with \(S_1=V_0M'V_0^*\), \(S_2=B(K_2)\). Since \(B(K_2)'=\mathbb C1\), we get \(\iota_\gamma(M)''=\iota_\gamma(M)\), and \(\iota_\gamma(M)\) is a \(*\)-algebra.

(b) \(V(\gamma)^*(V_0mV_0^*\oplus y_2)V(\gamma)=m\), because \(V(\gamma)^*(0\oplus y_2)V(\gamma)=0\). For \(m\) in the unit ball of \(M\) (or \(M'\)), \(V_0mV_0^*\oplus0\) lies in the unit ball of \(\iota_\gamma(M)\) (or \(\iota_\gamma(M)'\)).

(c) The operators in these algebras have the form \(y_1\oplus y_2\), which gives the first identity. For the second, \((\iota_\gamma(M)\cup\iota_\gamma(N))'=\iota_\gamma(M)'\cap\iota_\gamma(N)'=V_0(M'\cap N')V_0^*\oplus B(K_2)\) by (a). Its commutant is \(V_0(M'\cap N')'V_0^*\oplus\mathbb C1=\iota_\gamma(M\vee N)\), by the first part. The third identity is \(V(\gamma)1V(\gamma)^*=P(\gamma)\). Injectivity follows from (b). \(\square\)

**Theorem 10.3.**

1. \((M(\gamma))\) is measurably generated if and only if \(\gamma\mapsto\iota_\gamma(M(\gamma))\), with \(\iota_\gamma\) as in (10.1), is a measurable map into \(\mathrm{vN}(\mathcal K_0)\).
2. If so, the generating fields can be chosen with \(\|x_n(\gamma)\|\leq1\) and \(\{x_n(\gamma):n\}\) \(\sigma\)-weakly dense in the unit ball of \(M(\gamma)\), for every \(\gamma\).
3. If \((M(\gamma))\) and \((N(\gamma))\) are measurably generated, so are \((M(\gamma)')\), \((M(\gamma)\cap N(\gamma))\), \((M(\gamma)\vee N(\gamma))\), and the centres \((M(\gamma)\cap M(\gamma)')\).
4. If \((M(\gamma))\) is measurably generated, the sets \(\{\gamma:M(\gamma)\text{ is a factor}\}\), \(\{\gamma:M(\gamma)\text{ is abelian}\}\) and \(\{\gamma:M(\gamma)=B(H(\gamma))\}\) belong to \(\Sigma\).
5. (*Stratified form*) Let \(U(\gamma):H(\gamma)\to\ell^2_d\) be the unitaries of [Theorem 7.1(4)](#oa-fnd-ef-07) on the [dimension strata](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-04) \(\Gamma_d\). Then \((M(\gamma))\) is measurably generated if and only if, for every \(d\), the map \(\gamma\mapsto U(\gamma)M(\gamma)U(\gamma)^*\in\mathrm{vN}(\ell^2_d)\) is measurable on \(\Gamma_d\).

The definition of a measurably generated family does not mention \(V\). So by (1), the measurability of \(\gamma\mapsto\iota_\gamma(M(\gamma))\) does not depend on the choice of the isometries.

**Proof.** (1) Suppose \(M(\gamma)\) is generated by \(\{x_n(\gamma)\}\), with measurable fields \(x_n\). The maps \(\gamma\mapsto V(\gamma)x_n(\gamma)V(\gamma)^*\) and \(\gamma\mapsto P(\gamma)\) are weakly measurable, by [Theorem 7.1(3)](#oa-fnd-ef-07) and [Theorem 6.1(3)](#oa-fnd-ef-06). We claim that \(\iota_\gamma(M(\gamma))\) is generated by \(T(\gamma)=\{Vx_nV^*,Vx_n^*V^*:n\}\cup\{P\}\); then [Theorem 9.1(3)](#oa-fnd-ef-09) gives measurability. An operator that commutes with \(P\) has the form \(y_1\oplus y_2\), and it commutes with \(Vx_nV^*=V_0x_nV_0^*\oplus0\) and with \(Vx_n^*V^*\) exactly when \(y_1\) commutes with \(V_0x_nV_0^*\) and \(V_0x_n^*V_0^*\). Since \(M\) is generated by the \(x_n\), \(\{x_n,x_n^*\}'=M'\). So \(T(\gamma)'=V_0\{x_n,x_n^*\}'V_0^*\oplus B(K_2)=V_0M'V_0^*\oplus B(K_2)=\iota_\gamma(M)'\), by Lemma 10.2(a), and \(T(\gamma)''=\iota_\gamma(M)''=\iota_\gamma(M)\).

Conversely, suppose \(\gamma\mapsto\iota_\gamma(M(\gamma))\) is measurable. Let \(a_n\) be the maps of [Theorem 9.1(2)](#oa-fnd-ef-09) for \(\mathrm{vN}(\mathcal K_0)\), and put
\[
x_n(\gamma)=V(\gamma)^*\,a_n\big(\iota_\gamma(M(\gamma))\big)\,V(\gamma).
\]
Then \(Vx_nV^*=P\,a_n(\iota_\gamma(M(\gamma)))\,P\) is weakly measurable ([Lemma 8.1(2)](#oa-fnd-ef-08)), so \(x_n\) is a measurable field by [Theorem 7.1(3)](#oa-fnd-ef-07). By Lemma 10.2(b), \(x_n(\gamma)\) lies in the unit ball of \(M(\gamma)\), and the \(x_n(\gamma)\) are \(\sigma\)-weakly dense there, because compression is \(\sigma\)-weakly continuous and maps the unit ball of \(\iota_\gamma(M(\gamma))\) onto that of \(M(\gamma)\). As in [Theorem 9.1(2)](#oa-fnd-ef-09), they generate \(M(\gamma)\). This proves (1) and (2).

(3) By Lemma 10.2(c), \(\iota_\gamma(M(\gamma)\cap N(\gamma))=\iota_\gamma(M(\gamma))\cap\iota_\gamma(N(\gamma))\) and \(\iota_\gamma(M(\gamma)\vee N(\gamma))=\iota_\gamma(M(\gamma))\vee\iota_\gamma(N(\gamma))\). These are measurable in \(\gamma\) by (1) and [Theorem 9.1(4)](#oa-fnd-ef-09), and (1) applies. For commutants, let \(b_n(\gamma)=a_n(\iota_\gamma(M(\gamma))')\), which is measurable into \(B(\mathcal K_0)_1\) by [Theorem 9.1(2) and (4)](#oa-fnd-ef-09), and put \(y_n(\gamma)=V(\gamma)^*b_n(\gamma)V(\gamma)\). As in (1), the \(y_n\) are measurable fields, and by Lemma 10.2(b) they are \(\sigma\)-weakly dense in the unit ball of \(M(\gamma)'\), so they generate \(M(\gamma)'\). The centres are the intersection of \((M(\gamma))\) with the measurably generated family \((M(\gamma)')\).

(4) \(M(\gamma)\) is a factor exactly when \(\iota_\gamma(M(\gamma)\cap M(\gamma)')=\iota_\gamma(\mathbb C1)=\mathbb CP(\gamma)+\mathbb C(1-P(\gamma))\). The left side is measurable in \(\gamma\) by (3) and (1). The right side is the von Neumann algebra generated by the weakly measurable map \(P\), so it is measurable by [Theorem 9.1(3)](#oa-fnd-ef-09). The set where two measurable maps into \(\mathrm{vN}(\mathcal K_0)\) agree lies in \(\Sigma\) ([Proposition 3.2(6)](#oa-fnd-ef-03)). Likewise, \(M(\gamma)\) is abelian exactly when \(\iota_\gamma(M(\gamma)\cap M(\gamma)')=\iota_\gamma(M(\gamma))\), and \(M(\gamma)=B(H(\gamma))\) exactly when \(M(\gamma)'=\mathbb C1\), that is, \(\iota_\gamma(M(\gamma)')=\iota_\gamma(\mathbb C1)\).

(5) By the remark after the theorem, we may use the isometries of [Theorem 7.1(1)](#oa-fnd-ef-07). Then \(V(\gamma)=J_dU(\gamma)\) on \(\Gamma_d\) ([Theorem 7.1(4)](#oa-fnd-ef-07)). So \(P(\gamma)=P_d:=J_dJ_d^*\), and \(\iota_\gamma(M(\gamma))=\Theta_d(U(\gamma)M(\gamma)U(\gamma)^*)\), where \(\Theta_d(A)=J_dAJ_d^*+\mathbb C(1-P_d)\) for \(A\in\mathrm{vN}(\ell^2_d)\). The map \(\Theta_d\) is Borel: by the claim in the proof of (1), with the single space \(\ell^2_d\) and the isometry \(J_d\) in place of the field, \(\Theta_d(A)\) is generated by the weakly measurable maps \(A\mapsto J_da_n(A)J_d^*\) and the constant \(P_d\), where \(a_n\) are the maps of [Theorem 9.1(2)](#oa-fnd-ef-09) for \(\mathrm{vN}(\ell^2_d)\); so [Theorem 9.1(3)](#oa-fnd-ef-09) applies. Hence, if every \(\gamma\mapsto U(\gamma)M(\gamma)U(\gamma)^*\) is measurable on \(\Gamma_d\), then \(\gamma\mapsto\iota_\gamma(M(\gamma))\) is measurable on each \(\Gamma_d\), and on \(\Gamma\) by [Lemma 1.3(4)](#oa-fnd-ef-01). Conversely, if \(\gamma\mapsto\iota_\gamma(M(\gamma))\) is measurable, then on \(\Gamma_d\) the algebra \(U(\gamma)M(\gamma)U(\gamma)^*=J_d^*\iota_\gamma(M(\gamma))J_d\) is generated by the weakly measurable maps \(\gamma\mapsto J_d^*a_n(\iota_\gamma(M(\gamma)))J_d\), by Lemma 10.2(b) with \(J_d\) in place of \(V(\gamma)\). [Theorem 9.1(3)](#oa-fnd-ef-09), over \(\Gamma_d\) with its relative \(\sigma\)-algebra, finishes the proof. \(\square\)

**Example 10.4** (*varying and zero dimension*). (a) Take the [field of varying dimension](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-10) with \(\Gamma=(0,1]\) and \(H(\gamma)=\mathbb C^k\) on \(\Gamma_k=(\tfrac1{k+1},\tfrac1k]\). It is generated by the sections \(\xi_k\), where \(\xi_k(\gamma)\) is the \(k\)-th standard basis vector if \(k\leq\dim H(\gamma)\) and \(0\) otherwise, and its orthonormal fundamental sequence is \(e_k=\xi_k\), as [noted for this field](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-08). On \(\Gamma_k\), \(V(\gamma)\) maps \(\mathbb C^k\) onto \(\operatorname{span}\{\varepsilon_1,\ldots,\varepsilon_k\}\) and \(P(\gamma)=\sum_{j\leq k}\langle\cdot,\varepsilon_j\rangle\varepsilon_j\). Let \(M(\gamma)\) be the algebra of diagonal matrices in \(M_k(\mathbb C)=B(H(\gamma))\). It is generated by the [matrix-unit fields](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-01) \(e_{jj}\), \(e_{jj}(\gamma)v=\langle v,e_j(\gamma)\rangle e_j(\gamma)\), since \(e_{jj}(\gamma)\) is the \(j\)-th diagonal matrix unit for \(j\leq k\) and \(0\) for \(j>k\). Each \(M(\gamma)\) is maximal abelian, so \(M(\gamma)'=M(\gamma)\), and the centre field is \(M(\gamma)\) itself. \(M(\gamma)\) is a factor exactly on \(\Gamma_1=(\tfrac12,1]\). In the isometric picture, \(\iota_\gamma(M(\gamma))\) is spanned by the projections onto \(\mathbb C\varepsilon_1,\ldots,\mathbb C\varepsilon_k\) and by \(1-P(\gamma)\).

(b) Take the [field with a stratum of zero fibres](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-08): \(\Gamma=[0,2]\), with \(H(\gamma)=\mathbb C\) for \(\gamma\leq1\) and \(H(\gamma)=0\) for \(\gamma>1\). Then \(V(\gamma)v=v\varepsilon_1\) for \(\gamma\leq1\), \(V(\gamma)=0\) for \(\gamma>1\), and \(P(\gamma)=1_{[0,1]}(\gamma)\langle\cdot,\varepsilon_1\rangle\varepsilon_1\), an Effros-measurable field of projections that jumps at \(\gamma=1\). For \(M(\gamma)=B(H(\gamma))\), \(\iota_\gamma(M(\gamma))=\mathbb CP(\gamma)+\mathbb C(1-P(\gamma))\), which is \(\mathbb C1\) on \((1,2]\). With the definition \(M\cap M'=\mathbb C1\), the zero algebra on the zero space counts as a factor, so here every fibre is a factor. Whether zero fibres should count as factors is a matter of convention. The set \(\{\gamma:\dim H(\gamma)=0\}\) is measurable, because the [dimension function](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-02) is, so either choice gives measurable sets.

## 11. Exercises

**Exercise 1 (lattice operations).** Show that \(P\mapsto1-P\) is a homeomorphism of \(\mathcal P(\mathcal K)\), that \((P,Q)\mapsto P\vee Q\) and \((P,Q)\mapsto P\wedge Q\) (the projections onto the closed span of \(P\mathcal K+Q\mathcal K\) and onto \(P\mathcal K\cap Q\mathcal K\)) are Borel maps \(\mathcal P(\mathcal K)\times\mathcal P(\mathcal K)\to\mathcal P(\mathcal K)\), and that \(\{(P,Q):P\leq Q\}\) is closed.

*Solution.* \(\langle(1-P)\xi,\eta\rangle=\langle\xi,\eta\rangle-\langle P\xi,\eta\rangle\), so \(P\mapsto1-P\) is weakly continuous, and it is its own inverse. On \(\mathcal P(\mathcal K)\times\mathcal P(\mathcal K)\) with the product \(\sigma\)-algebra, the maps \((P,Q)\mapsto P\zeta_n\) and \((P,Q)\mapsto Q\zeta_n\), for a dense sequence \((\zeta_n)\), are measurable ([Theorem 6.1(2)](#oa-fnd-ef-06)), and together they span a dense subspace of \(P\mathcal K+Q\mathcal K\). So \(P\vee Q\) is Borel by criterion (c) of [Theorem 6.1(3)](#oa-fnd-ef-06). Since \(P\mathcal K\cap Q\mathcal K\) is the orthogonal complement of \((1-P)\mathcal K+(1-Q)\mathcal K\), \(P\wedge Q=1-\big((1-P)\vee(1-Q)\big)\), which is Borel. Finally, \(P\leq Q\) means \(P\mathcal K\subseteq Q\mathcal K\). This holds exactly when \(\|P\xi\|\leq\|Q\xi\|\) for all \(\xi\). If \(P\mathcal K\subseteq Q\mathcal K\), then \(P=PQ\), so \(\|P\xi\|=\|PQ\xi\|\leq\|Q\xi\|\). Conversely, let \(\xi\in P\mathcal K\) and apply the inequality to \((1-Q)\xi\): \(P(1-Q)\xi=0\), so \(\|(1-Q)\xi\|^2=\langle(1-Q)\xi,P\xi\rangle=\langle P(1-Q)\xi,\xi\rangle=0\), and \(\xi\in Q\mathcal K\). Each condition \(\|P\xi\|\leq\|Q\xi\|\) is closed for the strong operator topology.

**Exercise 2 (rank).** Show that \(P\mapsto\dim P\mathcal K\in\{0,1,\ldots,\infty\}\) is lower semicontinuous on \(\mathcal P(\mathcal K)\) with the strong operator topology, so that every set \(\{P:\dim P\mathcal K=r\}\) is Borel. Show that it is continuous if \(\dim\mathcal K<\infty\), and not if \(\dim\mathcal K=\infty\).

*Solution.* Suppose \(\dim P\mathcal K\geq r\), with \(r\) finite, and choose orthonormal \(u_1,\ldots,u_r\in P\mathcal K\). If \(Q\to P\) strongly, then \(Qu_i\to Pu_i=u_i\). So the Gram matrix \((\langle Qu_i,Qu_j\rangle)\) tends to the identity and is eventually invertible. Then \(Qu_1,\ldots,Qu_r\) are linearly independent, and \(\dim Q\mathcal K\geq r\). So \(\{\dim\geq r\}\) is open for each finite \(r\), and \(\{\dim=r\}=\{\dim\geq r\}\setminus\{\dim\geq r+1\}\) and \(\{\dim=\infty\}=\bigcap_r\{\dim\geq r\}\) are Borel. If \(\dim\mathcal K<\infty\), then \(\dim P\mathcal K=\operatorname{tr}P=\sum_k\langle P\varepsilon_k,\varepsilon_k\rangle\) is continuous. If \(\dim\mathcal K=\infty\), Example 6.3 gives rank-one projections converging to \(0\). For a map \(\gamma\mapsto K(\gamma)\) as in [Theorem 6.1(3)](#oa-fnd-ef-06), composing with the rank recovers the measurability of \(\gamma\mapsto\dim K(\gamma)\), which [Theorem 6.1(3)](#oa-fnd-ef-06) obtained from the theory of [subspace fields](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-03).

**Exercise 3 (abelian algebras and inclusions).** Show that the sets \(\{M\in\mathrm{vN}(\mathcal K):M\text{ is abelian}\}\) and \(\{M:M'=M\}\) (the maximal abelian algebras), and the relation \(\{(M,N):M\subseteq N\}\), are Borel.

*Solution.* \(M\) is abelian exactly when \(M\subseteq M'\), that is, when \(M\cap M'=M\). Similarly, \(M\subseteq N\) exactly when \(M\cap N=M\). The maps involved are Borel by [Theorem 9.1(4)](#oa-fnd-ef-09), and a set where two Borel maps into \(\mathrm{vN}(\mathcal K)\) agree is Borel by [Proposition 3.2(6)](#oa-fnd-ef-03). The same applies to \(M'=M\).

**Exercise 4 (unitary conjugation).** Let \(\mathcal U(\mathcal K)\) be the unitary group with the Borel sets of the strong operator topology. Show that \((u,M)\mapsto uMu^*\) is a Borel map \(\mathcal U(\mathcal K)\times\mathrm{vN}(\mathcal K)\to\mathrm{vN}(\mathcal K)\).

*Solution.* On the product, the maps \((u,M)\mapsto u\), \((u,M)\mapsto u^*\) and \((u,M)\mapsto a_n(M)\) (from [Theorem 9.1(2)](#oa-fnd-ef-09)) are weakly measurable: \(\langle u\xi,\eta\rangle\) is continuous in \(u\), and \(\langle u^*\xi,\eta\rangle\) is the conjugate of \(\langle u\eta,\xi\rangle\). Products of weakly measurable maps are weakly measurable ([Lemma 8.1(2)](#oa-fnd-ef-08)), so the maps \((u,M)\mapsto ua_n(M)u^*\) are weakly measurable. \(uMu^*\) is generated by \(\{ua_n(M)u^*\}\), because \(x\mapsto uxu^*\) is a \(*\)-automorphism of \(B(\mathcal K)\) that carries commutants to commutants. [Theorem 9.1(3)](#oa-fnd-ef-09) finishes the proof.

**Exercise 5 (reduced algebras).** Let \((M(\gamma))\) be a measurably generated family over a measurable field \((H(\gamma)),\mathfrak M\), and let \(p\) be a measurable field of projections with \(p(\gamma)\in M(\gamma)\) for every \(\gamma\). Show that the subspaces \(p(\gamma)H(\gamma)\) form a measurable field, and that the reduced algebras \(p(\gamma)M(\gamma)p(\gamma)\), acting on \(p(\gamma)H(\gamma)\), form a measurably generated family. Show also that compressing an arbitrary generating set does not work.

*Solution.* The sections \(pe_k\) are measurable, by the definition of a [measurable operator field](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-05), and they span a dense subspace of \(p(\gamma)H(\gamma)\) at each point. So the construction of [subspace fields](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-03) gives a measurable field \((p(\gamma)H(\gamma))\), whose measurable sections are the elements of \(\mathfrak M\) with values in \(p(\gamma)H(\gamma)\). By [Theorem 10.3(2)](#oa-fnd-ef-10), choose measurable fields \(x_n\) with \(\{x_n(\gamma)\}\) \(\sigma\)-weakly dense in the unit ball of \(M(\gamma)\). The fields \(px_np\) are measurable, since [composites of measurable operator fields](../reader/supplements/measurable-fields-direct-integrals.html#oa-fnd-hf-05) are measurable, and they carry measurable sections of the subfield to elements of \(\mathfrak M\) with values in \(p(\gamma)H(\gamma)\); so they are measurable fields on the subfield. The reduced algebra \(p(\gamma)M(\gamma)p(\gamma)\) is a von Neumann algebra acting on \(p(\gamma)H(\gamma)\), by fact (R) of the background. The map \(x\mapsto p(\gamma)xp(\gamma)\) is \(\sigma\)-weakly continuous and carries the unit ball of \(M(\gamma)\) onto that of \(p(\gamma)M(\gamma)p(\gamma)\), because \(pxp=x\) for \(x\) in the reduced algebra. So the \(p(\gamma)x_n(\gamma)p(\gamma)\) are \(\sigma\)-weakly dense in that unit ball, and they generate it. For the warning: in \(M_3(\mathbb C)\), the matrix units \(e_{11},e_{13},e_{32}\) generate \(M_3(\mathbb C)\) (with their adjoints they give \(e_{12}=e_{13}e_{32}\), \(e_{21}=e_{23}e_{31}\), \(e_{33}=e_{31}e_{13}\), \(e_{22}=e_{23}e_{32}\), and so every matrix unit). The projection \(p=e_{11}+e_{22}\) lies in \(M_3(\mathbb C)\), but \(pe_{11}p=e_{11}\), \(pe_{13}p=0\) and \(pe_{32}p=0\) generate only the diagonal algebra on \(p\mathbb C^3\), while \(pM_3(\mathbb C)p\cong M_2(\mathbb C)\). This is why the solution uses the generators of [Theorem 10.3(2)](#oa-fnd-ef-10), which are dense in the unit ball.

## Where this leads

- [Polish spaces and standard Borel spaces](../../foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces.html) continues the descriptive set theory of Sections 1, 2 and 4: Souslin spaces, the isomorphism theorem for standard Borel spaces, and measurable cross sections.
- Direct integrals of von Neumann algebras: over a measure space, a measurably generated family \((M(\gamma))\) defines the von Neumann algebra \(\int^\oplus M(\gamma)\,d\mu(\gamma)\) of decomposable operators whose fibres lie in the \(M(\gamma)\). Theorem 10.3 supplies the measurability facts behind its commutant and its centre: the families of commutants and of centres are again measurably generated, and the set of points where the fibre is a factor is measurable.

## References

- [Ando–Haagerup–Winsløw] H. Ando, U. Haagerup and C. Winsløw, *Ultraproducts, QWEP von Neumann algebras, and the Effros–Maréchal topology*, [arXiv:1306.0460](https://arxiv.org/abs/1306.0460).
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, Berlin, 2006.
- [Effros 1965] E. G. Effros, *The Borel space of von Neumann algebras on a separable Hilbert space*, Pacific Journal of Mathematics 15 (1965), 1153–1164. https://doi.org/10.2140/pjm.1965.15.1153
- [Takesaki I] M. Takesaki, *Theory of Operator Algebras I*, Springer, New York, 1979.
