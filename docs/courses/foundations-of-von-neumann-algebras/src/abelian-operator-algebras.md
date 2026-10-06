# Commutative operator algebras: measure, order and duality

*Original lesson by Claude Opus 5.5 (Anthropic). Learner routes, explanatory checkpoints and proof self-checks by GPT-6.1 Sol (OpenAI), at Ultra, October 2026. Original course contributions: CC0.*

A commutative algebra can be described by continuous functions, by multiplication operators, or by bounded measurable functions with an equivalence relation. These descriptions answer different questions. A measure describes the vectors in a cyclic representation. The order describes suprema inside the algebra. Its Banach dual describes every bounded scalar observation, including observations that do not respect monotone limits. The aim is to learn how to pass between the descriptions without confusing them.

Keep two models in view: diagonal operators on \(\ell^2(I)\), and multiplication by \(L^\infty[0,1]\) on \(L^2[0,1]\). In the first, singleton projections detect coordinates; in the second, every nonzero projection can be split. Doubling either representation changes its commutant and cyclic vectors while leaving the abstract algebra unchanged. The four examples below make these distinctions explicit before the classification theorems.

The route has four stages. First recover a measure model from a cyclic vector and examine its scalar observations. Then ask what order completeness means for the Gelfand spectrum, and which measures see that order. Next use normal measures to characterize the von Neumann algebras and separate atomic from diffuse models. Finally construct order-complete algebras that fail the normal-measure test, and study the extension property of stonean spaces. Result numbers are also used in the cross-references between these stages.

The prerequisites are the continuous functional calculus and quotient theorem for C*-algebras, the GNS construction, the double commutant and density theorems, and the measure tools proved below. The later classification of countably generated diffuse algebras uses the spectral theorem and standard Borel measure models. Exact proof links accompany their uses.

## A. Recover a measure model and test its observations

For a cyclic vector \(\xi\), the scalar data are \(f\mapsto\langle\pi(f)\xi,\xi\rangle\). Positivity turns these data into a measure; the map \(f\mapsto\pi(f)\xi\) then recovers the Hilbert space. This is more information than a bare abstract isomorphism, because it remembers how the algebra acts. After constructing the model, we examine the full dual of \(L^\infty\) before imposing normality.

**Checkpoint: what can the observations detect?** On \(\ell^\infty(\mathbb N)\), put \(p_n=1_{\{1,\ldots,n\}}\). These projections increase strongly to the identity on \(\ell^2(\mathbb N)\): for \(\eta\in\ell^2\), the squared norm of \((1-p_n)\eta\) is the tail of its convergent square sum. A countably additive finite measure therefore has \(\mu(p_n)\to\mu(1)\). A general bounded finitely additive measure need not have this property. The dual theorem below explains why boundedness alone leaves that possibility open. Phillips' lemma tests all subsets, and Example 10.5 shows concretely why testing finite subsets would miss it.

Here is such an observation. On the real space of convergent sequences, the limit functional has norm one and takes the constant sequence \(1\) to \(1\). The [real Hahn–Banach theorem](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-02) extends it to a real functional \(L\) of norm one on all bounded real sequences. If \(g\ge0\) and \(R=\|g\|>0\), then \(\|1-g/R\|\le1\), so \(L(g)=R(1-L(1-g/R))\ge0\); the zero case is immediate. Its complexification \(\Phi(h+ik)=L(h)+iL(k)\) is complex linear. Choose \(|\lambda|=1\) with \(\lambda\Phi(z)=|\Phi(z)|\); then \(|\Phi(z)|=L(\operatorname{Re}(\lambda z))\le\|z\|\). Thus \(\|\Phi\|=\Phi(1)=1\). The set function \(\nu(E)=\Phi(1_E)\) is positive and finitely additive, with \(\nu(\mathbb N)=1\). But each \(p_n\) is a convergent sequence with limit zero, so \(\nu(\{1,\ldots,n\})=0\). This gives a bounded positive observation that fails the increasing-net test, and proves the claimed distinction.

The order of study matters: distinguish the full dual from the normal observations before asking which compact spectra carry enough normal measures.

### 1. Four examples

The following examples show the phenomena that the lesson explains. When an example uses a later result, the result is named.

**Example 1.1** (Diagonal operators). Let \(I\) be a set, \(H=\ell^2(I)\) with its standard basis \((\delta_i)_{i\in I}\), and for a bounded function \(f\) on \(I\) let \(M_f\) be the diagonal operator \(M_f\delta_i=f(i)\delta_i\). The algebra \(\mathcal A=\{M_f:f\in\ell^\infty(I)\}\) is abelian, and it is its own commutant. Indeed, if \(T\) commutes with each rank-one projection \(M_{1_{\{i\}}}\), then \(T\) maps \(\mathbb C\delta_i\) into itself, so \(T\delta_i=t_i\delta_i\) with \(|t_i|\le\|T\|\), and \(T=M_t\). So \(\mathcal A\) is a maximal abelian von Neumann algebra. In \(\ell^\infty(I)\) a bounded increasing net of real functions \(f_\alpha\) has its pointwise supremum \(f\) as least upper bound, and \(M_{f_\alpha}\to M_f\) strongly. Indeed, for a fixed vector, choose a finite set of coordinates with arbitrarily small squared-norm tail. Pointwise convergence handles the finite set, and the uniform bound on \(f_\alpha-f\) controls the tail.

If \(I=\{i_1,i_2,\dots\}\) is countable (listed without repetitions, with a finite sum when \(I\) is finite), the vector \(\xi=\sum_k2^{-k}\delta_{i_k}\) is cyclic for \(\mathcal A\), because \(M_{1_{\{i_k\}}}\xi=2^{-k}\delta_{i_k}\). For \(I=\varnothing\), \(H=\{0\}\) and the zero vector is cyclic. If \(I\) is uncountable, no vector is cyclic: a vector \(\xi\in\ell^2(I)\) has only countably many nonzero coordinates (the sets where \(|\xi_i|\geq1/n\) are finite), and \(\mathcal A\xi\) lies in the closed subspace spanned by the corresponding basis vectors. The spectrum of \(\ell^\infty(I)\) is the Stone–Čech compactification \(\beta I\) of the discrete space \(I\).

**Example 1.2** (Multiplication operators on the unit interval). Let \(m\) be Lebesgue measure on \([0,1]\) and \(\mathcal A=\{M_f:f\in L^\infty[0,1]\}\) on \(L^2[0,1]\), where \(M_f\xi=f\xi\). This is a maximal abelian von Neumann algebra, and the constant function \(1\) is a cyclic vector (Theorem 3.1). The multiplications by continuous functions form a C\*-subalgebra that is not a von Neumann algebra. For instance, \(g_n(t)=\min\{1,\max\{0,n(t-\frac12)\}\}\) increases to the indicator function of \((\frac12,1]\), and \(M_{g_n}\) converges strongly to multiplication by that indicator. In \(C[0,1]\) itself the sequence \((g_n)\) has no least upper bound. An upper bound \(g\) satisfies \(g\ge1\) on \((\frac12,1]\), so \(g(\frac12)\ge1\) by continuity, and \(g\ge0\). Hence \(g>\frac12\) on some interval \([\frac12-\delta,\frac12]\). Subtracting a continuous bump \(b\) with \(0\le b\le\frac12\), supported in \((\frac12-\delta,\frac12)\) and not identically zero, gives a smaller upper bound, because every \(g_n\) vanishes on \([0,\frac12]\). So \(C[0,1]\) lacks least upper bounds that \(L^\infty[0,1]\) has. The reason is topological: \([0,1]\) is connected, while spectra of von Neumann algebras are extremally disconnected (Sections 4 and 7).

**Example 1.3** (Multiplicity two). On \(L^2[0,1]\oplus L^2[0,1]\) let \(\mathcal A_2=\{M_f\oplus M_f:f\in L^\infty[0,1]\}\). This abelian von Neumann algebra is isomorphic to the algebra of Example 1.2 by \(M_f\mapsto M_f\oplus M_f\). But its commutant contains the operators \(\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}\) with scalar entries, which do not commute with each other. So \(\mathcal A_2\) is not maximal abelian, and by Corollary 3.3 it has no cyclic vector. The two algebras are isomorphic but not spatially isomorphic, since their commutants differ (see Exercise 12.4).

**Example 1.4** (An \(L^\infty\) space that is not a von Neumann algebra on its \(L^2\) space). Let \(X\) be an uncountable set, \(\Sigma\) the \(\sigma\)-algebra of sets that are countable or have countable complement, and \(\nu(E)\) the number of points of \(E\) if \(E\) is countable and \(\nu(E)=\infty\) otherwise. This is a measure, and only the empty set has measure zero.

*Measurable functions are constant off a countable set.* Let \(f:X\to\mathbb R\) be \(\Sigma\)-measurable. If \(\{f>r\}\) had countable complement for every rational \(r\), then \(\bigcap_r\{f>r\}=\varnothing\) would have countable complement, which is absurd. If \(\{f>r\}\) were countable for every rational \(r\), then \(X=\bigcup_r\{f>r\}\) would be countable. The sets \(\{f>r\}\) decrease in \(r\), so there is a number \(c\) with \(\{f>r\}\) co-countable for rational \(r<c\) and countable for rational \(r>c\). Then \(\{f\ne c\}\) is contained in \(\bigcup_{r<c}\{f\le r\}\cup\bigcup_{r>c}\{f>r\}\), a countable set. The same holds for complex functions, by taking real and imaginary parts.

*The spaces.* If \(\int|f|^2d\nu<\infty\), the constant \(c\) must be \(0\), since the co-countable set \(\{f=c\}\) has infinite measure. Conversely, every function with countable support is measurable. So \(L^2(X,\Sigma,\nu)=\ell^2(X)\), with the same norm. Since only \(\varnothing\) is null, \(L^\infty(X,\Sigma,\nu)\) consists of the bounded functions that are constant off a countable set, acting on \(\ell^2(X)\) by diagonal operators.

*The algebra is too small.* Every singleton is measurable, so an operator that commutes with \(L^\infty(X,\Sigma,\nu)\) commutes with the projections onto the basis vectors, and it is diagonal, as in Example 1.1. So the commutant of the multiplication algebra is the algebra of all diagonal operators \(M_t\), \(t\in\ell^\infty(X)\), and its bicommutant is again this algebra. [Proposition 8.5 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-08) supplies a partition of \(X\) into two uncountable sets. The multiplication operator by the indicator of one of them lies in the bicommutant but not in the multiplication algebra. So the multiplication algebra of \(L^\infty(X,\Sigma,\nu)\) is not a von Neumann algebra.

Whether \(L^\infty\) acts on \(L^2\) as a von Neumann algebra is therefore a property of the measure. It holds for finite measures (Remark 3.2), for sigma-finite measures and for Radon measures on locally compact spaces with the local conventions (Proposition 3.2a below). Proposition 3.2b proves the finite-piece gluing criterion used here; Example 3.2c shows why a local-null convention matters.

### 2. Tools from topology, measure theory and operator theory

This section fixes conventions and supplies the measure, category and order tools used throughout.

*Spaces.* Compact and locally compact spaces are Hausdorff. For a subset \(A\) of a topological space, \(\overline A\) is its closure and \(A^\circ\) its interior. A set is *clopen* if it is closed and open. A set \(R\) is *rare* (or nowhere dense) if \(\overline R\) has empty interior. A set is *meager* (or of the first category) if it is a countable union of rare sets. A space is a *Baire space* if every meager subset has empty interior. For a compact space \(\Omega\), \(C(\Omega)\) is the C\*-algebra of continuous complex functions and \(C_{\mathbb R}(\Omega)\) its real part. For a locally compact space \(\Gamma\), \(C_0(\Gamma)\) and \(C_c(\Gamma)\) are the continuous functions that vanish at infinity and those with compact support. For any set \(X\), \(\ell^\infty(X)\) denotes the C\*-algebra formed by the bounded complex functions on \(X\). Real functions are ordered pointwise.

*Regularizations.* For a bounded real function \(f\) on a topological space \(X\) put
\[
\begin{gathered}
f_*(x)=\sup_{U\ni x}\,\inf_{y\in U}f(y),\\
f^*(x)=\inf_{U\ni x}\,\sup_{y\in U}f(y),
\end{gathered}
\tag{2.1}
\]
where \(U\) runs over the open neighbourhoods of \(x\). We call \(f_*\) the *lower* and \(f^*\) the *upper regularization* of \(f\). A real function \(g\) is *lower semicontinuous* (lsc) if every set \(\{g>t\}\) is open, and *upper semicontinuous* (usc) if \(-g\) is lsc.

*Measures.* For a compact space \(\Omega\), a *Radon measure* on \(\Omega\) is a finite positive Borel measure that is outer regular and inner regular on open sets, as in Haar measure on locally compact groups. We identify it with the positive linear functional \(x\mapsto\mu(x)=\int x\,d\mu\) on \(C(\Omega)\), which determines it (Riesz representation theorem, see Background). A finite Radon measure is inner regular on all Borel sets: \(\mu(E)=\sup\{\mu(K):K\subseteq E\text{ compact}\}\). A set is *\(\mu\)-null* if it lies in a Borel set of measure zero, and *\(\mu\)-measurable* if it differs from a Borel set by a \(\mu\)-null set. The *support* of \(\mu\) is the complement of the union of all open \(\mu\)-null sets. For Radon measures on locally compact spaces that need not be finite, \(L^\infty(\Gamma,\mu)\) is formed with locally null sets, as in Vector-valued functions, tensor products with \(L^p\), and preduals; for finite measures on compact spaces this is the usual space.

*Operators.* Hilbert spaces are complex, and inner products are linear in the first variable. For a von Neumann algebra \(M\), \(M_h\) is the set of its self-adjoint elements and \(M_+\) the set of its positive elements. A von Neumann algebra \(M\) is *generated* by a subset \(S\) if \(M=(S\cup S^*)''\), the smallest von Neumann algebra containing \(S\). A \(*\)-isomorphism is a bijective \(*\)-homomorphism. For a vector \(\xi\), \(\omega_\xi(x)=\langle x\xi,\xi\rangle\).

#### Regularity after completing the measure

**Completed regularity.** The inner and outer regularity of a finite Radon measure also hold for its completed measurable sets. Indeed, write \(E\triangle B\subseteq Z\), where \(B,Z\) are Borel and \(\mu(Z)=0\). Given \(\varepsilon>0\), choose a compact \(K_0\subseteq B\) with \(\mu(B\setminus K_0)<\varepsilon/2\), and an open \(U\supseteq Z\) with \(\mu(U)<\varepsilon/2\). Then \(K=K_0\setminus U\) is compact, \(K\subseteq E\), and \(\mu(E\setminus K)<\varepsilon\). Choose also an open \(V\supseteq B\) with \(\mu(V\setminus B)<\varepsilon/2\). The open set \(V\cup U\) contains \(E\) and satisfies \(\mu((V\cup U)\setminus E)<\varepsilon\). Thus every completed measurable set admits the same compact and open approximations as a Borel set. This argument applies to finite Radon measures on locally compact spaces as well.

#### Densities of complex measures

The measure tools for Haar integration, Theorem 4.1, prove Radon–Nikodym for positive sigma-finite measures. We need its complex version as well. The finite complex Radon measures used here have finite total variation, by Theorem 2.4 of the Haar lesson. The following argument works on any sigma-algebra and requires no topology.

**Lemma (Small sets have small integrals).** If \(g\geq0\) is integrable, then for every \(\varepsilon>0\) there is \(\delta>0\) such that \(\int_Eg\,d\mu<\varepsilon\) whenever \(\mu(E)<\delta\).

*Proof.* The integrable functions \(g1_{\{g>n\}}\) tend to zero almost everywhere and are bounded by \(g\). Dominated convergence, Theorem 2.2 of the measure-tools lesson, gives an integer \(n\geq1\) for which their integral is less than \(\varepsilon/2\). Take \(\delta=\varepsilon/(2n)\). Splitting \(E\) at the level \(n\) gives \(\int_Eg\leq n\mu(E)+\int_{\{g>n\}}g<\varepsilon\). \(\square\)

In particular an integrable density against a finite Radon measure on a compact space again gives a finite Radon measure. Approximate a Borel set from inside by a compact set and from outside by an open set in the original measure; the lemma makes the corresponding errors small for the density measure.

**Theorem (Complex Radon–Nikodym).** Let \(\mu\) be a positive sigma-finite measure, and let \(\nu\) be a countably additive complex measure on the same sigma-algebra with finite total variation. Suppose \(\nu(E)=0\) whenever \(\mu(E)=0\). There is a unique \(h\in L^1(\mu)\), up to almost-everywhere equality, with
\[
\nu(E)=\int_Eh\,d\mu
\]
for every measurable \(E\). Its variation satisfies \(|\nu|(E)=\int_E|h|\,d\mu\).

*Proof.* Define \(|\nu|(E)\) as the supremum of \(\sum_j|\nu(E_j)|\) over finite measurable partitions of \(E\). It is a finite positive measure. To see countable additivity, let \(E=\bigcup_nE_n\) be disjoint. Restrict a finite partition of \(E\) to each \(E_n\); countable additivity of \(\nu\) and the triangle inequality give \(|\nu|(E)\leq\sum_n|\nu|(E_n)\). Conversely, combine partitions of the first \(N\) sets whose costs are arbitrarily close to their variations, and add the remaining part of \(E\) as one piece. This gives \(|\nu|(E)\geq\sum_{n\leq N}|\nu|(E_n)\). Let \(N\) increase.

If \(\mu(E)=0\), every measurable subset of \(E\) is also \(\mu\)-null and therefore \(\nu\)-null. The partition definition gives \(|\nu|(E)=0\). The four set functions
\[
\begin{gathered}
\alpha_\pm=\tfrac12\bigl(|\nu|\pm\operatorname{Re}\nu\bigr),\\
\beta_\pm=\tfrac12\bigl(|\nu|\pm\operatorname{Im}\nu\bigr)
\end{gathered}
\]
are finite positive measures, because \(|\operatorname{Re}\nu(E)|\) and \(|\operatorname{Im}\nu(E)|\) are at most \(|\nu|(E)\). They are absolutely continuous with respect to \(\mu\). Apply the positive Radon–Nikodym theorem to obtain their nonnegative densities \(a_\pm,b_\pm\). Each is integrable, since its integral over the whole space is the finite mass of its measure. Then
\[
h=a_+-a_-+i(b_+-b_-)
\]
is integrable and gives the asserted formula.

If an integrable \(k\) has zero integral on every measurable set, its real part cannot be positive on a set of positive measure: test the sets \(\{\operatorname{Re}k>1/n\}\). These sets have finite measure by integrability, and their integrals would be strictly positive. Apply the same argument to the negative real part and both signs of the imaginary part. Thus \(k=0\) almost everywhere, proving uniqueness.

For every finite partition of \(E\), \(\sum_j|\int_{E_j}h|\leq\int_E|h|\), so \(|\nu|(E)\leq\int_E|h|\). For the reverse inequality let \(u=1_E\overline h/|h|\), with value zero where \(h=0\). Approximate this bounded measurable function uniformly by simple functions of supremum norm at most one. For such a simple function supported on \(E\), the partition definition bounds the absolute value of its \(\nu\)-integral by \(|\nu|(E)\). Uniform convergence is valid both against the finite variation measure and against \(|h|\mu\). Hence
\[
\int_E|h|\,d\mu=\int u\,d\nu\leq|\nu|(E).
\]
The integral on the left is real and nonnegative. This proves the variation identity. \(\square\)

**Example.** For Lebesgue measure \(\lambda\) on \([0,1]\), put \(\nu(E)=i\lambda(E\cap[0,1/2])-i\lambda(E\cap(1/2,1])\). Its density is \(i\) on the first half and \(-i\) on the second. Thus \(|\nu|([0,1])=1\), although \(\nu([0,1])=0\). Cancellation affects the complex mass but not its variation.

**Exercise (medium): equivalent weighted representations.** Let \(\mu\) be a finite measure and \(h>0\) almost everywhere with \(\int h\,d\mu<\infty\). Put \(\nu=h\mu\). Prove that \(V:L^2(\nu)\to L^2(\mu)\), \(Vf=h^{1/2}f\), is unitary and intertwines multiplication by every bounded measurable function.

*Solution.* The identity \(\|Vf\|_{L^2(\mu)}^2=\int|f|^2h\,d\mu=\|f\|_{L^2(\nu)}^2\) gives isometry and well-definedness. The null sets of the two measures agree: if \(\int_Eh=0\), each \(E\cap\{h\geq1/n\}\) is \(\mu\)-null, and their union differs from \(E\) only by the null set where \(h=0\). The inverse is \(g\mapsto h^{-1/2}g\), with arbitrary value on that null set; its norm identity is the reverse one. Finally \(h^{1/2}(ag)=a(h^{1/2}g)\). This is the mechanism used in Corollary 3.4.

#### Category and operator order


**Lemma 2.1** (Rare and meager sets). Let \(X\) be a topological space.

1. A set is rare exactly when its closure is rare. Subsets of rare sets and finite unions of rare sets are rare. For an open set \(G\) the set \(\overline G\setminus G\) is rare, and for a closed set \(F\) the set \(F\setminus F^\circ\) is rare.
2. (*Baire category theorem for compact spaces.*) Every compact space is a Baire space. Equivalently, a countable intersection of dense open subsets is dense, and the complement of a meager set is dense.
3. Let \((G_j)_{j\in J}\) be pairwise disjoint open sets and \(R_j\subseteq G_j\). If every \(R_j\) is rare, then \(\bigcup_jR_j\) is rare. If every \(R_j\) is meager, then \(\bigcup_jR_j\) is meager.

**Proof.** (1) The first two statements follow from the definition. If \(R\) and \(S\) are rare, the complements of \(\overline R\) and \(\overline S\) are dense open sets. A dense open set meets every nonempty open set \(U\) in a nonempty open set, and this set meets the second dense open set. So the intersection of the two complements is dense, and \(\overline R\cup\overline S\) has empty interior. If an open set \(V\) lies in \(\overline G\setminus G\), then \(V\subseteq\overline G\) and \(V\cap G=\varnothing\), which forces \(V=\varnothing\). If an open set \(V\) lies in \(F\setminus F^\circ\), then \(V\subseteq F\), so \(V\subseteq F^\circ\), and again \(V=\varnothing\).

(2) Let \(D_1,D_2,\dots\) be dense open sets and \(V\) a nonempty open set. A compact space is regular: a point and a closed set not containing it have disjoint neighbourhoods (by Urysohn's lemma, see Background). So there is a nonempty open \(V_1\) with \(\overline{V_1}\subseteq V\cap D_1\), then a nonempty open \(V_2\) with \(\overline{V_2}\subseteq V_1\cap D_2\), and so on. The compact sets \(\overline{V_n}\) decrease and are nonempty, so they have a common point, which lies in \(V\cap\bigcap_nD_n\). If \(M=\bigcup_nR_n\) is meager, the sets \(D_n=X\setminus\overline{R_n}\) are dense and open, and \(\bigcap_nD_n\) is disjoint from \(M\); so \(X\setminus M\) is dense and \(M\) has empty interior. The complete-metric Baire theorem, although not needed for this compact-space argument, has its full nested-ball proof in [Theorem 3.1 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-03).

(3) Put \(R=\bigcup_jR_j\) and \(G=\bigcup_jG_j\). Suppose a nonempty open \(U\) lies in \(\overline R\). Since \(R\subseteq G\), \(U\) meets \(G\), so \(W=U\cap G_j\) is nonempty for some \(j\). Let \(x\in W\) and let \(V\subseteq W\) be an open neighbourhood of \(x\). Then \(V\) meets \(R\), and \(V\cap R=V\cap R_j\) because the sets \(G_k\) are disjoint. So \(x\in\overline{R_j}\). Hence \(W\subseteq\overline{R_j}\), which is impossible for a rare set \(R_j\). For the meager case write \(R_j=\bigcup_nR_{j,n}\) with rare sets \(R_{j,n}\subseteq G_j\). By the rare case each \(\bigcup_jR_{j,n}\) is rare, and \(\bigcup_jR_j=\bigcup_n\bigcup_jR_{j,n}\). \(\square\)

**Lemma 2.2** (Regularizations). Let \(f\) be a bounded real function on a topological space \(X\).

1. \(f_*\le f\le f^*\). The function \(f_*\) is lsc, and it is the largest lsc function below \(f\); likewise \(f^*\) is the smallest usc function above \(f\). If \(f\) is continuous at \(x\), then \(f_*(x)=f(x)=f^*(x)\).
2. If \(f\) is lsc, then \(\{f^*\ne f\}\) is meager. If \(f\) is usc, then \(\{f_*\ne f\}\) is meager.

No separation axiom is needed.

**Proof.** (1) The inequalities hold because every neighbourhood of \(x\) contains \(x\). If \(f_*(x)>t\), there is an open \(U\ni x\) with \(\inf_Uf>t\), and then \(f_*(y)\ge\inf_Uf>t\) for every \(y\in U\). So \(\{f_*>t\}\) is open. If \(g\le f\) is lsc and \(t<g(x)\), the open set \(U=\{g>t\}\) contains \(x\) and \(\inf_Uf\ge t\), so \(f_*(x)\ge t\); hence \(g\le f_*\). The statements on \(f^*\) follow by applying these to \(-f\). Continuity at \(x\) means that \(\inf_Uf\) and \(\sup_Uf\) tend to \(f(x)\) as \(U\) shrinks.

(2) Let \(f\) be lsc. The function \(f^*-f\) is usc, so \(A_n=\{f^*-f\ge1/n\}\) is closed. Suppose a nonempty open \(U\) lies in \(A_n\). For \(y\in U\), \(U\) is a neighbourhood of \(y\), so \(f^*(y)\le\sup_Uf\); hence \(\sup_Uf^*=\sup_Uf\). On \(U\) we have \(f\le f^*-1/n\), so \(\sup_Uf\le\sup_Uf-1/n\), which is absurd. So every \(A_n\) is rare, and \(\{f^*\ne f\}=\bigcup_nA_n\) is meager. The usc case follows by applying this to \(-f\), since \((-f)^*=-f_*\). \(\square\)

**Lemma 2.3** (Radon measures and increasing nets). Let \(\mu\) be a Radon measure on a compact space \(\Omega\).

1. If \((U_i)\) is an increasing net of open sets, then \(\mu(\bigcup_iU_i)=\sup_i\mu(U_i)\).
2. Let \((f_i)\) be an increasing net of real continuous functions with \(\sup_i\|f_i\|<\infty\), and let \(f\) be its pointwise supremum. Then \(f\) is lsc and \(\int f\,d\mu=\sup_i\mu(f_i)\).
3. \(C(\Omega)\) is dense in \(L^2(\Omega,\mu)\).

**Proof.** (1) Put \(U=\bigcup_iU_i\). By inner regularity on open sets, \(\mu(U)\) is the supremum of \(\mu(K)\) over compact \(K\subseteq U\). Each such \(K\) is covered by finitely many \(U_i\), hence by a single one, since the net increases.

(2) A supremum of continuous functions is lsc. Adding a constant, we may assume \(0\le f_i\le c\) for all \(i\). Fix \(\varepsilon>0\) and an integer \(N\geq1\) with \(N\ge c/\varepsilon\). For a function \(g\) with values in \([0,c]\) put \(s(g)=\varepsilon\sum_{k=1}^N1_{\{g>k\varepsilon\}}\). If \(j\varepsilon<g(x)\le(j+1)\varepsilon\), exactly the terms with \(k\le j\) are present, so \(s(g)(x)=j\varepsilon\). Hence \(g-\varepsilon\le s(g)\le g\). The sets \(\{f>k\varepsilon\}=\bigcup_i\{f_i>k\varepsilon\}\) are unions of increasing nets of open sets. By (1), and since the net is directed and there are only \(N\) values of \(k\), there is an index \(i\) with \(\mu(\{f_i>k\varepsilon\})\ge\mu(\{f>k\varepsilon\})-\varepsilon/N\) for all \(k\le N\). Then
\[
\begin{gathered}
\mu(f_i)\\
\ge\int s(f_i)\,d\mu\\
\ge\int s(f)\,d\mu-\varepsilon^2\\
\ge\int f\,d\mu-\varepsilon\mu(\Omega)-\varepsilon^2 .
\end{gathered}
\]
Since \(f_i\le f\) for all \(i\), this proves (2).

(3) This is the density of \(C_c\) in \(L^p\) for Radon measures, proved in Haar measure on locally compact groups. \(\square\)

**Lemma 2.4** (Increasing nets of operators). Let \((x_i)\) be an increasing net of self-adjoint operators on a Hilbert space \(H\) with \(\sup_i\|x_i\|<\infty\). Then \((x_i)\) converges strongly to a self-adjoint operator \(x\), and among the self-adjoint operators on \(H\) the net has \(x\) as its least upper bound. If all \(x_i\) lie in a von Neumann algebra \(M\), then \(x\in M\), and \(x\) is also its least upper bound in \(M_h\).

**Proof.** For each \(\xi\), the numbers \(\langle x_i\xi,\xi\rangle\) increase and are bounded, so they converge. By polarization, \(\langle x_i\xi,\eta\rangle\) converges for all \(\xi,\eta\), and the limit is a bounded hermitian sesquilinear form. [Theorem 3.1 of the Hilbert-space lesson](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-03) gives a self-adjoint \(x\) with \(\langle x_i\xi,\eta\rangle\to\langle x\xi,\eta\rangle\), and \(x\ge x_i\) for every \(i\). For a positive operator \(T\), [Proposition 1.1 of the Hilbert-space lesson](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-01), applied to the positive form \((\eta,\zeta)\mapsto\langle T\eta,\zeta\rangle\) gives \[
\begin{gathered}
\|T\xi\|^2\\
=\langle T\xi,T\xi\rangle\\
\le\langle T\xi,\xi\rangle^{1/2}\langle T^2\xi,T\xi\rangle^{1/2}\\
\le\langle T\xi,\xi\rangle^{1/2}\|T\|^{1/2}\|T\xi\|,
\end{gathered}
\] and hence \(\|T\xi\|^2\le\|T\|\,\langle T\xi,\xi\rangle\). With \(T=x-x_i\), whose norm stays bounded, this shows \(\|(x-x_i)\xi\|\to0\). If \(y\) is self-adjoint and \(y\ge x_i\) for all \(i\), then \(\langle y\xi,\xi\rangle\ge\lim_i\langle x_i\xi,\xi\rangle=\langle x\xi,\xi\rangle\), so \(y\ge x\). A von Neumann algebra is strongly closed, so \(x\in M\) when all \(x_i\) are. \(\square\)

### 3. Measures and cyclic representations

In this section \(\Omega\) is locally compact and \(\mu\) is a finite positive Radon measure on it. For \(f\in L^\infty(\Omega,\mu)\) let \(M_f\) be the operator \(\xi\mapsto f\xi\) on \(L^2(\Omega,\mu)\). The *multiplication representation* of \(C_0(\Omega)\) is \(\pi_\mu(x)=M_x\). The Riesz representation theorem identifies finite positive Radon measures on \(\Omega\) with positive linear functionals on \(C_0(\Omega)\), and complex Radon measures with bounded linear functionals (see Background). A representation \(\pi\) of a C\*-algebra on \(H\) has a *cyclic vector* \(\xi\) if \(\pi(A)\xi\) is dense in \(H\).

**Theorem 3.1** (Cyclic representations of \(C_0(\Omega)\)). Let \(\Omega\) be locally compact, with a finite positive Radon measure \(\mu\).

1. The constant function \(1\) is a cyclic vector for \(\pi_\mu\), and \(\langle\pi_\mu(x)1,1\rangle=\int x\,d\mu\) for \(x\in C_0(\Omega)\).
2. Let \(\pi\) be a representation of \(C_0(\Omega)\) on \(H\) with a cyclic vector \(\xi\) such that \(\langle\pi(x)\xi,\xi\rangle=\int x\,d\mu\) for all \(x\). Then there is exactly one unitary \(U:L^2(\Omega,\mu)\to H\) with \(U\pi_\mu(x)=\pi(x)U\) for all \(x\) and \(U1=\xi\).
3. \[
\begin{gathered}
\pi_\mu(C_0(\Omega))'\\
=\{M_f:f\in L^\infty(\Omega,\mu)\}\\
=\pi_\mu(C_0(\Omega))''.
\end{gathered}
\] So the von Neumann algebra generated by \(\pi_\mu(C_0(\Omega))\) is the algebra of multiplications by \(L^\infty(\Omega,\mu)\), it is maximal abelian, and \(f\mapsto M_f\) is an isometric \(*\)-isomorphism of \(L^\infty(\Omega,\mu)\) onto it.

Part (2) identifies \(\pi_\mu\) with the GNS representation of the positive functional \(x\mapsto\int x\,d\mu\). Its cyclic vector has squared norm \(\mu(\Omega)\); the functional is a state when this mass is one. The nonunital construction and its uniqueness are proved in [the GNS lesson, Theorems 5.4–5.5](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-05).

**Proof.** (1) Since \(\mu\) is finite, \(1\in L^2(\Omega,\mu)\) and \(\pi_\mu(C_0(\Omega))1=C_0(\Omega)\), which contains \(C_c(\Omega)\) and is therefore dense in \(L^2(\Omega,\mu)\) by the density theorem for Radon measures in Haar measure on locally compact groups. The formula is the definition of \(\pi_\mu\).

(2) For \(x\in C_0(\Omega)\), \(\|\pi(x)\xi\|^2=\langle\pi(\bar xx)\xi,\xi\rangle=\int|x|^2d\mu=\|x\|_{L^2}^2\). So \(x\mapsto\pi(x)\xi\), defined on the dense subspace \(C_0(\Omega)\) of \(L^2(\Omega,\mu)\), is well defined and isometric, and its range \(\pi(C_0(\Omega))\xi\) is dense in \(H\). It extends to a unitary \(U\). For \(x,y\in C_0(\Omega)\), \(U\pi_\mu(x)y=\pi(xy)\xi=\pi(x)Uy\), and by density \(U\pi_\mu(x)=\pi(x)U\). For every \(x\), \(\langle U1,\pi(x)\xi\rangle=\langle U1,Ux\rangle=\int\bar x\,d\mu=\langle\xi,\pi(x)\xi\rangle\), since \(\langle\pi(\bar x)\xi,\xi\rangle=\int\bar x\,d\mu\). The vectors \(\pi(x)\xi\) are dense, so \(U1=\xi\). Any unitary with the two properties maps \(x=\pi_\mu(x)1\) to \(\pi(x)\xi\), so it equals \(U\).

(3) Let \(T\) commute with every \(M_x\), \(x\in C_0(\Omega)\), and put \(g=T1\in L^2(\Omega,\mu)\). For \(x\in C_0(\Omega)\), \(Tx=TM_x1=M_xT1=xg\). Let \(h\) be a bounded completed measurable function, and choose \(x_n\in C_0(\Omega)\) with \(x_n\to h\) in \(L^2(\Omega,\mu)\). Then \(Tx_n\to Th\) in \(L^2\), and \(x_ng\to hg\) in \(L^1\) by the Cauchy–Schwarz inequality. Choose a subsequence whose squared \(L^2\) errors in the first convergence and \(L^1\) errors in the second have finite sums. Monotone convergence shows that both error series are finite almost everywhere, so this subsequence converges almost everywhere in both cases and gives \(Th=hg\). Let \(c>\|T\|\) and \(E=\{|g|>c\}\). Then
\[
c^2\mu(E)\le\int_E|g|^2\,d\mu=\|T1_E\|^2\le\|T\|^2\mu(E),
\]
so \(\mu(E)=0\). Hence \(g\in L^\infty(\Omega,\mu)\) with \(\|g\|_\infty\le\|T\|\). The operators \(T\) and \(M_g\) agree on the bounded functions, which are dense in \(L^2\), so \(T=M_g\).

Write \(\mathcal A=\{M_f:f\in L^\infty\}\). We have shown \(\pi_\mu(C_0(\Omega))'\subseteq\mathcal A\), and the converse inclusion holds because multiplication operators commute. \(\mathcal A\) is abelian, so \(\mathcal A\subseteq\mathcal A'\). Since \(\pi_\mu(C_0(\Omega))\subseteq\mathcal A\), taking commutants gives \(\mathcal A'\subseteq\pi_\mu(C_0(\Omega))'=\mathcal A\). So \(\mathcal A'=\mathcal A\), and \(\pi_\mu(C_0(\Omega))''=\mathcal A'=\mathcal A\). Clearly \(\|M_f\|\le\|f\|_\infty\). If \(c<\|f\|_\infty\), the set \(F=\{|f|>c\}\) has positive measure and \(\|M_f1_F\|\ge c\|1_F\|\), so \(\|M_f\|=\|f\|_\infty\). The algebraic properties hold pointwise. \(\square\)

**Remark 3.2** (Finite measure spaces). The proof of (3) uses only one property of \(C_0(\Omega)\): it consists of bounded functions and is dense in \(L^2\). So for every finite measure space \((X,\Sigma,\nu)\) and every set \(S\) of bounded measurable functions whose span is dense in \(L^2(X,\nu)\), the commutant of \(\{M_s:s\in S\}\) is \(\{M_f:f\in L^\infty(X,\nu)\}\). Taking \(S=L^\infty\), the algebra \(L^\infty(X,\nu)\) is maximal abelian on \(L^2(X,\nu)\) for every finite measure. Proposition 3.2a extends this argument to sigma-finite measures and to arbitrary Radon measures on locally compact spaces. Example 1.4 shows that it fails for some measure spaces.

#### Multiplication for sigma-finite and Radon measures

**Proposition 3.2a** (Multiplication beyond finite measures). Multiplication gives an isometric unital \(*\)-isomorphism of \(L^\infty\) onto a maximal abelian von Neumann algebra on \(L^2\) in either of the following settings: an arbitrary sigma-finite measure space, or a positive Radon measure on a locally compact Hausdorff space, with measurable functions and equality understood locally in the second setting.

*Proof.* For a sigma-finite measure space, partition the space into countably many measurable sets \(E_i\) of finite measure. The projections \(P_i=M_{1_{E_i}}\) are pairwise orthogonal and their sum is \(1\) strongly, because the squared norm of the omitted tail is the tail of the convergent series \(\sum_i\int_{E_i}|\xi|^2\). If \(T\) commutes with every bounded multiplication, it commutes with these projections. On \(P_iL^2=L^2(E_i)\), Remark 3.2 gives \(T|_{P_iL^2}=M_{g_i}\) with \(\|g_i\|_\infty\leq\|T\|\). Choose measurable representatives bounded everywhere by \(\|T\|\), and glue them on the \(E_i\). The resulting bounded measurable \(g\) satisfies \(T=M_g\), first on finite sums of the subspaces and then on all of \(L^2\) by continuity. The multiplication algebra is therefore its own commutant. Its operator norm equals the essential supremum norm: a level set of positive measure meets some \(E_i\) in a set of positive finite measure, and the indicator of that intersection tests the required lower bound.

For a Radon measure, Lemma 2.1 of the vector-valued-functions lesson proves a decomposition into pairwise disjoint compact pieces \(K_i\), with locally null complement \(N\), such that every compact set meets only countably many pieces. Its gluing assertion says that scalar functions measurable on the pieces are locally measurable after being set to zero on \(N\); Lemma 1.2(4) identifies measurability on each compact piece with completed Borel measurability. These conclusions use only Radon regularity and Zorn's lemma, and their full proofs are given there. Lemma 2.3(2)–(3) of the same lesson proves
\[
\|\xi\|_2^2=\sum_i\int_{K_i}|\xi|^2\,d\mu.
\]
Thus \(L^2\) is the Hilbert sum of the finite-measure spaces \(L^2(K_i)\). The identification is onto: a square-summable family of piecewise \(L^2\) classes has only countably many nonzero components; choose completed measurable representatives on those pieces, put zero on all others and on \(N\), and apply the scalar gluing assertion. The displayed integral identity gives its squared norm and its prescribed components. In the compact-set approximation used by that gluing proof, a test set of measure zero needs no pieces: take the approximating compact subset to be empty, with error zero. For a test set of positive measure, the list of meeting pieces is nonempty, and the finite-tail approximation uses an integer \(J\geq1\). In particular every vector has only countably many nonzero components, and the finite partial sums of \(P_i=M_{1_{K_i}}\) converge strongly to \(1\).

Again an operator commuting with every multiplication restricts on each piece to \(M_{g_i}\), by Remark 3.2. Truncate representatives on each piece so that \(|g_i|\leq\|T\|\) everywhere. The gluing assertion gives a locally measurable bounded function \(g\), zero on \(N\), and the Hilbert-sum identity gives \(T=M_g\). Conversely all scalar multiplications commute, so the multiplication algebra equals its commutant and is a von Neumann algebra. If \(0<c<\|g\|_\infty\), the level set \(\{|g|>c\}\) is not locally null. It therefore meets a compact set in a completed measurable set \(F\) with \(0<\mu(F)<\infty\); testing on \(1_F\) gives \(\|M_g\|\geq c\). Together with the upper bound this proves isometry and faithfulness. If the norm is zero, the assertion is immediate. No lifting or general decomposable-operator theorem is used. \(\square\)

The local integral used here is the supremum of integrals over compact subsets, as defined and justified in Definitions 2.2–2.4 of the same provider. It ignores locally null sets even when their outer-regular Borel measure is not zero. For a finite measure on a compact space it is the usual integral.

**Proposition 3.2b** (Finite-piece gluing beyond sigma-finiteness). Let \((X,\Sigma,\mu)\) admit a partition \((E_i)_{i\in I}\) into measurable sets of finite measure such that a set \(S\subseteq X\) belongs to \(\Sigma\) exactly when each \(S\cap E_i\) is measurable, and then
\[
\mu(S)=\sum_{i\in I}\mu(S\cap E_i).
\]
The sum means the supremum of the finite partial sums. Such a measure space is called *strictly localizable*. No countability of \(I\) is required. Multiplication is an isometric unital *-isomorphism of \(L^\infty(X,\mu)\) onto a maximal abelian von Neumann algebra on \(L^2(X,\mu)\).

**Proof.** Integrals of nonnegative simple functions split over the pieces by the measure identity. Increasing simple approximations and monotone convergence give the same identity for every nonnegative measurable function. In particular,
\[
\begin{gathered}
L^2(X,\mu)=\bigoplus_{i\in I}L^2(E_i,\mu),\\
\|\xi\|_2^2=\sum_i\|\xi|_{E_i}\|_2^2.
\end{gathered}
\]
Each square-summable family has only countably many nonzero components: for every positive integer \(n\), only finitely many components have squared norm at least \(1/n\). Representatives on those components glue measurably by the partition hypothesis. Thus the displayed identification is onto, and the finite sums of \(P_i=M_{1_{E_i}}\) tend strongly to the identity.

Suppose \(T\) commutes with every multiplication. It commutes with every \(P_i\), so its restriction \(T_i\) acts on \(L^2(E_i)\) and commutes with all bounded multipliers there; a function on \(E_i\), extended by zero, is measurable on \(X\). The finite-measure argument of Remark 3.2 gives \(T_i=M_{g_i}\) with \(\|g_i\|_\infty\leq\|T\|\). Choose measurable representatives bounded everywhere by \(\|T\|\), putting zero on their measurable exceptional null sets. Piecewise gluing yields a measurable bounded \(g\) on \(X\). On finite-component vectors \(T=M_g\), and density gives this equality on all of \(L^2\). Hence the multiplication algebra is its own commutant, and consequently is weakly closed.

For \(0<c<\|g\|_\infty\), the measurable set \(S=\{|g|>c\}\) has positive measure. The measure identity gives an \(i\) with \(0<\mu(S\cap E_i)<\infty\). Testing \(M_g\) on \(1_{S\cap E_i}\) gives \(\|M_g\|\geq c\). The reverse inequality follows from \(\int|g\xi|^2\leq\|g\|_\infty^2\int|\xi|^2\), proving isometry. Algebra, adjoint and identity are preserved pointwise. \(\square\)

This isolates the gluing mechanism used in Proposition 3.2a. In its Radon case the exact compact-piece provider and the local integral remain essential: one cannot silently replace local equality by equality for an arbitrary outer-regular Borel measure. For the distinction between localizability, strict localizability and gluing, see [Bouafia and De Pauw, *Localizable locally determined measurable spaces with negligibles*, §§4.1–4.7 and 6.1–6.4](https://arxiv.org/html/2105.11331v1). Their terminology for measurable spaces with negligible sets is broader; the finite-piece operator proof above concerns the stated measure-space hypothesis.

**Example 3.2c** (A measure whose multiplication representation loses the identity). Let \(X\) be uncountable, let \(\Sigma\) consist of the countable and co-countable subsets, and put \(\mu(S)=0\) for countable \(S\), \(\mu(S)=\infty\) otherwise. This is countably additive: a disjoint sequence contains at most one co-countable member; if it contains none, its union is countable. Every integrable squared modulus has null positive level sets, since \(\mu(\{|\xi|>1/n\})\leq n^2\int|\xi|^2<\infty\), and every finite-measure set here is null. Thus \(L^2(X,\mu)=\{0\}\), whereas the constant function \(1\) has \(L^\infty\)-norm one. Multiplication is not faithful. The measure is not semi-finite: its positive-measure sets contain no subsets of positive finite measure. Finite-piece gluing in Proposition 3.2b prevents this loss, and Proposition 3.2a already specifies conventions that prevent it in the Radon model.

**Corollary 3.3** (Abelian algebras with a cyclic vector). Suppose that the abelian von Neumann algebra \(M\subseteq B(H)\) has a cyclic vector \(\xi\). Let \(K\) be the spectrum of \(M\), write \(x\mapsto\hat x\) for the Gelfand isomorphism of \(M\) onto \(C(K)\), and let \(\mu\) be the Radon measure on \(K\) with \(\int\hat x\,d\mu=\langle x\xi,\xi\rangle\). Then:

1. there is a unitary \(U:L^2(K,\mu)\to H\) with \(U1=\xi\) and \(UM_{\hat x}U^*=x\) for \(x\in M\);
2. \(M\) is maximal abelian, \(M'=M\);
3. every bounded Borel function on \(K\) agrees \(\mu\)-almost everywhere with a continuous function.

**Proof.** Since \(M\) is a unital abelian C\*-algebra, \(K\) is compact and \(M\cong C(K)\). The map \(\pi(\hat x)=x\) is a representation of \(C(K)\) on \(H\) with cyclic vector \(\xi\), and \(\langle\pi(\hat x)\xi,\xi\rangle=\int\hat x\,d\mu\). Theorem 3.1(2) gives (1). By Theorem 3.1(3), \(M'=U\pi_\mu(C(K))'U^*\) is abelian, so \(M'\subseteq M''=M\). Since \(M\) is abelian, \(M\subseteq M'\). Hence \(M=M'\). Finally \[
\begin{gathered}
U\pi_\mu(C(K))U^*\\
=M\\
=M'\\
=U\{M_f:f\in L^\infty\}U^*,
\end{gathered}
\] so every \(M_f\) is some \(M_{\hat x}\), which is (3). \(\square\)

Part (3) is a first sign of the special topology of \(K\): on \([0,1]\) with Lebesgue measure, the indicator of \([0,\frac12]\) agrees almost everywhere with no continuous function. Section 5 explains (3) through normal measures.

**Corollary 3.4** (Equivalent measures give equivalent representations). Let \(\Omega\) be locally compact, and let \(\mu\) and \(\nu\) be finite positive Radon measures on it. The representations \(\pi_\mu\) and \(\pi_\nu\) are unitarily equivalent if and only if \(\mu\) and \(\nu\) have the same null sets.

**Proof.** Suppose they have the same null sets. By the Radon–Nikodym theorem (see Background) \(\nu=h\mu\) with \(h\ge0\) integrable. The set \(\{h=0\}\) is \(\nu\)-null, hence \(\mu\)-null. The map \(V\xi=h^{1/2}\xi\) from \(L^2(\Omega,\nu)\) to \(L^2(\Omega,\mu)\) is isometric, since \(\int|\xi|^2d\nu=\int|\xi|^2h\,d\mu\). It is onto, since \(\eta=V(h^{-1/2}\eta)\) for \(\eta\in L^2(\Omega,\mu)\). It commutes with every multiplication operator, so \(V\pi_\nu(x)=\pi_\mu(x)V\).

Conversely, let \(U:L^2(\Omega,\mu)\to L^2(\Omega,\nu)\) be unitary with \(U\pi_\mu(x)=\pi_\nu(x)U\), and put \(g=U^*1\in L^2(\Omega,\mu)\). For \(x\in C_0(\Omega)\),
\[
\begin{gathered}
\int x\,d\nu\\
=\langle\pi_\nu(x)1,1\rangle\\
=\langle U\pi_\mu(x)U^*1,1\rangle\\
=\langle\pi_\mu(x)g,g\rangle\\
=\int x|g|^2d\mu .
\end{gathered}
\]
The finite measure \(\lambda=|g|^2\mu\) is again a Radon measure. Indeed, for \(\varepsilon>0\) there is \(\delta>0\) with \(\lambda(E)<\varepsilon\) whenever \(\mu(E)<\delta\), because \(|g|^2\) is integrable. So the outer regularity and the inner regularity of \(\mu\) pass to \(\lambda\). By the uniqueness in the Riesz representation theorem, \(\nu=\lambda\), so every \(\mu\)-null set is \(\nu\)-null. By symmetry the converse holds. \(\square\)

**Example 3.5.** On \([0,1]\) let \(m\) be Lebesgue measure and \(\delta_{1/2}\) the point mass at \(\frac12\). The measures \(m+\delta_{1/2}\) and \(2m+3\delta_{1/2}\) have the same null sets, so their multiplication representations are equivalent. The measures \(m\) and \(m+\delta_{1/2}\) do not, and indeed \(\pi_{m+\delta_{1/2}}(C[0,1])''\) contains a rank-one projection, multiplication by \(1_{\{1/2\}}\), while \(\pi_m(C[0,1])''=L^\infty[0,1]\) contains none.

### 10. The dual of \(L^\infty\)

Integrable functions give bounded linear functionals on \(L^\infty\). When \(L^\infty\) is infinite-dimensional they are not all of its dual: the dual consists of finitely additive measures. We prove this in a setting that covers \(L^\infty\) of a Radon measure, the algebras \(\ell^\infty(X)\), and the algebras \(\mathcal D(\Gamma)\) of Section 9.

Let \(X\) be a set, \(\Sigma\) a \(\sigma\)-algebra of subsets of \(X\), and \(\mathcal I\subseteq\Sigma\) a \(\sigma\)-ideal: countable unions of members of \(\mathcal I\) lie in \(\mathcal I\), and so do the members of \(\Sigma\) that are contained in a member of \(\mathcal I\). Let \(L^\infty(\Sigma,\mathcal I)\) be the space of bounded \(\Sigma\)-measurable complex functions, modulo those that vanish outside a member of \(\mathcal I\), with the norm
\[
\|f\|_\infty=\min\{c\ge0:\{|f|>c\}\in\mathcal I\};
\]
the minimum is attained because \(\mathcal I\) is closed under countable unions. It is an abelian C\*-algebra. Three examples:

- for a locally compact \(\Gamma\) with a Radon measure \(\mu\), \(\Sigma\) the \(\mu\)-measurable sets and \(\mathcal I\) the locally null ones, this is \(L^\infty(\Gamma,\mu)\);
- for \(\Sigma\) the set of all subsets of \(X\) and \(\mathcal I=\{\varnothing\}\), it is \(\ell^\infty(X)\);
- for \(\Sigma\) the Borel sets of a topological space \(\Gamma\) and \(\mathcal I\) the meager Borel sets, it is \(\mathcal D(\Gamma)\).

Let \(\operatorname{ba}(\Sigma,\mathcal I)\) be the set of functions \(\nu:\Sigma\to\mathbb C\) that are finitely additive, bounded (\(\sup_{E\in\Sigma}|\nu(E)|<\infty\)), and vanish on \(\mathcal I\). The *variation* of \(\nu\) on \(E\in\Sigma\) is \(|\nu|(E)=\sup\sum_k|\nu(E_k)|\), over the finite partitions of \(E\) into sets \(E_k\in\Sigma\).

**Lemma 10.1.** Let \(\nu\in\operatorname{ba}(\Sigma,\mathcal I)\). Then \(|\nu|(X)\le4\sup_E|\nu(E)|\). If \(E_1,\dots,E_n\in\Sigma\) are disjoint, then \(\sum_k|\nu|(E_k)=|\nu|(\bigcup_kE_k)\). So \(|\nu|\) is a bounded, positive, finitely additive function on \(\Sigma\), and \(\|\nu\|=|\nu|(X)\) is a norm on \(\operatorname{ba}(\Sigma,\mathcal I)\).

**Proof.** Let \((E_k)\) be a finite partition of \(X\). Let \(P\) be the union of the \(E_k\) with \(\operatorname{Re}\nu(E_k)\ge0\) and \(Q\) the union of the others. Then \[
\begin{gathered}
\sum_k|\operatorname{Re}\nu(E_k)|\\
=\operatorname{Re}\nu(P)-\operatorname{Re}\nu(Q)\\
\le2\sup|\nu|,
\end{gathered}
\] and the same holds for the imaginary parts. Since \(|z|\le|\operatorname{Re}z|+|\operatorname{Im}z|\), the first claim follows. For the second, partitions of the sets \(E_k\) together form a partition of their union, which gives \(\le\). Conversely, if \((A_l)\) is a finite partition of the union, then \[
\begin{gathered}
\sum_l|\nu(A_l)|\\
\le\sum_l\sum_k|\nu(A_l\cap E_k)|\\
\le\sum_k|\nu|(E_k).
\end{gathered}
\] Finally, \(|\nu+\nu'|(X)\le|\nu|(X)+|\nu'|(X)\), and \(|\nu(E)|\le|\nu|(X)\) for every \(E\), so \(|\nu|(X)=0\) only for \(\nu=0\). \(\square\)

**Theorem 10.2** (The dual of \(L^\infty\)). Let \(\nu\in\operatorname{ba}(\Sigma,\mathcal I)\). For a simple function \(s=\sum_kc_k1_{E_k}\), with \((E_k)\) a finite partition of \(X\) into sets of \(\Sigma\), put \(\int s\,d\nu=\sum_kc_k\nu(E_k)\). This extends to a bounded linear functional \(\varphi_\nu\) on \(L^\infty(\Sigma,\mathcal I)\). The map \(\nu\mapsto\varphi_\nu\) is a linear bijection of \(\operatorname{ba}(\Sigma,\mathcal I)\) onto the dual of \(L^\infty(\Sigma,\mathcal I)\), and it is isometric for the norm \(\|\nu\|=|\nu|(X)\); in particular \(\operatorname{ba}(\Sigma,\mathcal I)\) is a Banach space. The functional \(\varphi_\nu\) is positive if and only if \(\nu\ge0\).

**Proof.** The value \(\sum_kc_k\nu(E_k)\) does not depend on the partition, since two partitions have a common refinement and \(\nu\) is additive. It is linear in \(s\). If \(E_k\in\mathcal I\), then \(\nu(E_k)=0\); if not, then \(|c_k|\le\|s\|_\infty\), because \(E_k\subseteq\{|s|>\|s\|_\infty\}\in\mathcal I\) would hold otherwise. So
\[
\Big|\int s\,d\nu\Big|\le\sum_{E_k\notin\mathcal I}|c_k||\nu(E_k)|\le\|s\|_\infty\,|\nu|(X).
\]
Every bounded measurable function is a uniform limit of simple functions, so \(\int\cdot\,d\nu\) extends by continuity to a functional \(\varphi_\nu\) on \(L^\infty(\Sigma,\mathcal I)\) with \(\|\varphi_\nu\|\le|\nu|(X)\); it vanishes on functions that vanish outside a member of \(\mathcal I\), by the estimate. Conversely, take any \(\varphi\) in the dual of \(L^\infty(\Sigma,\mathcal I)\), and put \(\nu(E)=\varphi(1_E)\). Then \(\nu\) is finitely additive, \(|\nu(E)|\le\|\varphi\|\), and \(\nu\) vanishes on \(\mathcal I\). For a finite partition \((E_k)\) choose numbers \(c_k\) of modulus one with \(c_k\nu(E_k)=|\nu(E_k)|\). Then
\[
\sum_k|\nu(E_k)|=\varphi\Big(\sum_kc_k1_{E_k}\Big)\le\|\varphi\| ,
\]
so \(|\nu|(X)\le\|\varphi\|\). The functionals \(\varphi\) and \(\varphi_\nu\) agree on simple functions, hence everywhere. Different \(\nu\) give different functionals, since \(\varphi_\nu(1_E)=\nu(E)\). So the map is bijective and isometric. If \(\nu\ge0\), then \(\int s\,d\nu\ge0\) for simple \(s\ge0\), and by approximation \(\varphi_\nu\ge0\); conversely \(\nu(E)=\varphi_\nu(1_E)\). \(\square\)

For a finite measure \(\mu\) with \(\mathcal I\) its null sets, the countably additive members of \(\operatorname{ba}\) are exactly the measures \(h\,d\mu\) with \(h\in L^1(\mu)\), by the [complex Radon–Nikodym theorem of Section 2](#oa-fnd-ao-23); so \(L^1(\mu)\) is the part of the dual of \(L^\infty(\mu)\) that consists of countably additive measures. For \(\ell^\infty(\mathbb N)\), the countably additive members are the functions \(E\mapsto\sum_{n\in E}c_n\) with \(c\in\ell^1(\mathbb N)\). The dual of \(\ell^\infty(\mathbb N)\) is much larger (Exercise 12.2).

**Theorem 10.3** (Phillips' lemma). Let \(\Gamma\) be a set and \((\nu_n)\) a sequence in \(\operatorname{ba}(2^\Gamma,\{\varnothing\})=\ell^\infty(\Gamma)^*\) with \(\sup_n|\nu_n|(\Gamma)<\infty\). If \(\nu_n(E)\to0\) for every \(E\subseteq\Gamma\), then
\[
\lim_{n\to\infty}\sum_{\gamma\in\Gamma}|\nu_n(\{\gamma\})|=0 .
\]


**Proof.** Put \(C=\sup_n|\nu_n|(\Gamma)\) and \(\sigma_n=\sum_\gamma|\nu_n(\{\gamma\})|\). By Lemma 10.1, applied to finite sets of points, \(\sigma_n\le C\). Since \((\nu_n)\) is bounded and \(\nu_n(E)\to0\) for every \(E\), also \(\nu_n(f)\to0\) for every \(f\in\ell^\infty(\Gamma)\): approximate \(f\) uniformly by simple functions. Suppose the conclusion fails. Passing to a subsequence, we may assume \(\sigma_n>5\delta\) for all \(n\), for some \(\delta>0\).

*Step 1: a sliding hump.* We choose indices \(n_1<n_2<\cdots\) and pairwise disjoint finite sets \(F_1,F_2,\dots\subseteq\Gamma\) with
\[
\sum_{\gamma\notin F_k}|\nu_{n_k}(\{\gamma\})|<\delta\qquad(k\ge1).
\tag{10.1}
\]
Take \(n_1=1\) and a finite \(F_1\) that carries all but \(\delta\) of the convergent sum \(\sigma_1\). Given \(n_1,\dots,n_k\) and \(F_1,\dots,F_k\), let \(P=F_1\cup\dots\cup F_k\), a finite set. Since \(\nu_n(\{\gamma\})\to0\) for each \(\gamma\in P\), there is \(n_{k+1}>n_k\) with \(\sum_{\gamma\in P}|\nu_{n_{k+1}}(\{\gamma\})|<\delta/2\). Then choose a finite \(F_{k+1}\subseteq\Gamma\setminus P\) with \(\sum_{\gamma\notin P\cup F_{k+1}}|\nu_{n_{k+1}}(\{\gamma\})|<\delta/2\). This gives (10.1) for \(k+1\).

*Step 2: thinning out.* Write \(\lambda_k=\nu_{n_k}\). We find an infinite set \(K\subseteq\mathbb N\) such that
\[
\begin{gathered}
|\lambda_k|\Big(\\
\bigcup\{F_j:j\in K,\ j>k\}\Big)<\delta\\
(k\in K).
\end{gathered}
\tag{10.2}
\]
Put \(K_0=\mathbb N\) and \(k_1=\min K_0\). Choose an integer \(N>C/\delta\), and split \(K_0\setminus\{k_1\}\) into \(N\) disjoint infinite sets. The corresponding unions of the \(F_j\) are disjoint, so by Lemma 10.1 their \(|\lambda_{k_1}|\)-variations add up to at most \(C\), and one of them, indexed by an infinite set \(K_1\), has variation less than \(\delta\). Put \(k_2=\min K_1\), split \(K_1\setminus\{k_2\}\) in the same way with respect to \(\lambda_{k_2}\), and obtain \(K_2\subseteq K_1\); and so on. The set \(K=\{k_1,k_2,\dots\}\) is infinite, and the elements of \(K\) after \(k_i\) lie in \(K_i\). So (10.2) holds for \(k=k_i\).

*Step 3: a test function.* For \(k\in K\) and \(\gamma\in F_k\) let \(f(\gamma)\) be the number of modulus one with \(f(\gamma)\lambda_k(\{\gamma\})=|\lambda_k(\{\gamma\})|\), and let \(f=0\) elsewhere. Then \(f\in\ell^\infty(\Gamma)\), \(\|f\|\le1\). Fix \(k\in K\), let \(P_k\) be the union of the \(F_j\) with \(j\in K\), \(j<k\), and \(Q_k\) the union of those with \(j>k\). Then
\[
\begin{gathered}
\lambda_k(f)\\
=\sum_{\gamma\in F_k}|\lambda_k(\{\gamma\})|\\
+\sum_{\gamma\in P_k}f(\gamma)\lambda_k(\{\gamma\})\\
+\lambda_k(f1_{Q_k}).
\end{gathered}
\]
The first term exceeds \(5\delta-\delta=4\delta\), by (10.1). The second is at most \(\delta\) in modulus, again by (10.1), because the finite set \(P_k\) misses \(F_k\). The third is at most \(|\lambda_k|(Q_k)\|f\|<\delta\), by the estimate in the proof of Theorem 10.2 and (10.2). So \(|\lambda_k(f)|>2\delta\) for every \(k\in K\). But \(\lambda_k(f)=\nu_{n_k}(f)\to0\). This contradiction proves the theorem. \(\square\)

**Corollary 10.4** (Weak and norm convergence in \(\ell^1\)). Let \(\Gamma\) be a set. Every weakly convergent sequence in \(\ell^1(\Gamma)\) converges in norm. More generally, every weakly Cauchy sequence in \(\ell^1(\Gamma)\) converges in norm.


**Proof.** Let \(g_n\to0\) weakly in \(\ell^1(\Gamma)\), whose dual is \(\ell^\infty(\Gamma)\). By the [uniform boundedness principle, Theorem 4.1 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-04) the sequence is bounded. Put \(\nu_n(E)=\sum_{\gamma\in E}g_n(\gamma)\). Then \(\nu_n\in\ell^\infty(\Gamma)^*\), \(|\nu_n|(\Gamma)\le\|g_n\|_1\), and \(\nu_n(E)=\langle g_n,1_E\rangle\to0\) for every \(E\). By Theorem 10.3, \(\|g_n\|_1=\sum_\gamma|\nu_n(\{\gamma\})|\to0\). If \((f_n)\) converges weakly to \(f\), apply this to \(g_n=f_n-f\). If \((f_n)\) is only weakly Cauchy and not norm Cauchy, there are \(\varepsilon>0\) and indices \(p_k<q_k\), both tending to infinity, with \(\|f_{p_k}-f_{q_k}\|_1\ge\varepsilon\). The sequence \(f_{p_k}-f_{q_k}\) converges weakly to \(0\), hence in norm, which is a contradiction. So \((f_n)\) is norm Cauchy and converges, since \(\ell^1(\Gamma)\) is complete. \(\square\)

**Example 10.5** (The hypotheses matter). The unit vectors \(e_n\in\ell^1(\mathbb N)\) have norm one. They converge to \(0\) against every element of \(c_0\), the predual of \(\ell^1\), but not weakly: pairing with the constant function \(1\in\ell^\infty\) gives \(1\). Correspondingly, the point evaluations \(\nu_n=\delta_n\in\ell^\infty(\mathbb N)^*\) satisfy \(\nu_n(E)\to0\) for every finite set \(E\), but not for \(E=\mathbb N\), and \(\sum_k|\nu_n(\{k\})|=1\) for all \(n\). So in Theorem 10.3 the hypothesis is needed for all subsets \(E\), not only for the finite ones.

## B. Which measures see the order on the spectrum?

The Gelfand representation replaces an abelian unital C*-algebra by \(C(\Omega)\). A bounded pointwise supremum of continuous functions need not be continuous, so the supremum *in this ordered algebra* cannot simply be assumed to be the pointwise one. The stonean criterion below resolves that question through the closure of open sets. Normality then asks whether integration preserves those algebraic suprema.

For a finite spectrum the distinction disappears: all functions are continuous, all sets are clopen, and every finite measure preserves increasing bounded nets. On an infinite spectrum, the distinction is the main issue. A sufficient family of normal measures must detect every nonzero positive function; one measure need not suffice. The support criterion expresses detection geometrically and is the bridge to the operator representation.

### 4. Stonean spaces

Abelian von Neumann algebras have many projections, and the projections of \(C(\Omega)\) are the indicators of clopen sets. So the spectrum of such an algebra has many clopen sets. This section studies the compact spaces that have enough of them to make \(C_{\mathbb R}(\Omega)\) complete as an ordered set. A reference for this section and the next two is [Kostecki, Sections 5.6 and 5.8].

**Definition 4.1.** A Hausdorff space \(X\) is called *extremally disconnected* when each open set \(U\subseteq X\) has an open closure \(\overline U\). A compact extremally disconnected space is called *stonean*.

**Lemma 4.2.** Let \(X\) be a Hausdorff space.

1. \(X\) is extremally disconnected if and only if any two disjoint open subsets have disjoint closures. In that case the interior of every closed set is clopen.
2. An open subspace of an extremally disconnected space is extremally disconnected. A clopen subset of a stonean space is stonean.
3. In a stonean space the clopen sets form a base of the topology. So every open set is the union of the clopen sets it contains, and these form an increasing net under inclusion.

**Proof.** (1) Let \(X\) be extremally disconnected and let \(U,V\) be disjoint open sets. Then \(V\cap\overline U=\varnothing\), because \(V\) is open. Since \(\overline U\) is open, \(X\setminus\overline U\) is closed, and it contains \(V\), hence \(\overline V\). Conversely, assume the condition, and let \(U\) be open. Then \(V=X\setminus\overline U\) is open and disjoint from \(U\), so \(\overline U\cap\overline V=\varnothing\). Since \(\overline U\cup V=X\), this gives \(\overline U=X\setminus\overline V\), which is open. For a closed set \(F\), \(F^\circ=X\setminus\overline{X\setminus F}\), the complement of the closure of an open set; so \(F^\circ\) is clopen.

(2) If \(W\) is open in an open subspace \(U\), then \(W\) is open in \(X\), and its closure in \(U\) is \(\overline W\cap U\), which is open. A clopen subset of a compact space is compact.

(3) Let \(x\in U\) with \(U\) open. A compact space is regular, so there is an open \(V\) with \(x\in V\subseteq\overline V\subseteq U\), and \(\overline V\) is clopen. Finite unions of clopen sets are clopen. \(\square\)

**Theorem 4.3** (Order completeness and stonean spaces). For a compact space \(\Omega\) the following are equivalent.

1. \(\Omega\) is stonean.
2. Every nonempty subset of \(C_{\mathbb R}(\Omega)\) that is bounded above has a supremum in \(C_{\mathbb R}(\Omega)\), that is, a least upper bound for the pointwise order.
3. Every bounded lsc function on \(\Omega\) agrees with a continuous function outside a meager set.

When they hold, the following is true as well. For every bounded lsc function \(g\), the continuous function in (3) is unique, it is the upper regularization \(g^*\), and \(g^*\ge g\). For every nonempty set \(S\subseteq C_{\mathbb R}(\Omega)\) that is bounded above, the supremum of \(S\) in \(C_{\mathbb R}(\Omega)\) is \(g^*\), where \(g=\sup_{s\in S}s\) is the pointwise supremum; so it agrees with the pointwise supremum outside a meager set.


**Proof.** *Uniqueness in (3).* Two continuous functions that agree outside a meager set agree on a dense set, by Lemma 2.1(2), hence everywhere.

*Identification of the continuous function.* Let \(g\) be bounded and lsc, and let \(f\) be continuous with \(f=g\) outside a meager set \(M\). The function \(g-f\) is lsc, so \(\{g>f\}\) is open. It lies in \(M\), so it is empty by Lemma 2.1(2), and \(f\ge g\). Since \(f\) is usc, Lemma 2.2(1) gives \(f\ge g^*\). Conversely, fix \(\omega\) and \(\varepsilon>0\), and let \(U\) be an open neighbourhood of \(\omega\) on which \(f>f(\omega)-\varepsilon\). The set \(U\setminus M\) is not empty, again by Lemma 2.1(2), and \(g=f\) there. So \(\sup_Ug\ge f(\omega)-\varepsilon\), and the same holds for every smaller neighbourhood. Hence \(g^*(\omega)\ge f(\omega)-\varepsilon\). So \(f=g^*\).

(1)\(\Rightarrow\)(3). Let \(g\) be bounded and lsc. After an affine change we may assume \(0\le g\le1\). For real \(\lambda\) let \(F(\lambda)=\{g\le\lambda\}\), a closed set, and \(C(\lambda)=F(\lambda)^\circ\), which is clopen by Lemma 4.2(1). Both increase with \(\lambda\), \(F(1)=C(1)=\Omega\), and \(C(\lambda)\subseteq F(\lambda)\). For \(n\ge1\) define
\[
f_n=\sum_{k=1}^{2^n}\frac k{2^n}\big(1_{C(k2^{-n})}-1_{C((k-1)2^{-n})}\big).
\]
It is continuous, because the sets \(C(\lambda)\) are clopen. The sets \(C(0)\) and \(C(k2^{-n})\setminus C((k-1)2^{-n})\), \(1\le k\le2^n\), partition \(\Omega\); \(f_n\) is \(0\) on the first and \(k2^{-n}\) on the others. A point of \(C(k2^{-n})\setminus C((k-1)2^{-n})\) lies in exactly one of the two sets \(C((2k-1)2^{-n-1})\setminus C((2k-2)2^{-n-1})\) and \(C(2k\,2^{-n-1})\setminus C((2k-1)2^{-n-1})\), so \(f_{n+1}\) takes the value \(k2^{-n}-2^{-n-1}\) or \(k2^{-n}\) there. Hence \(\|f_n-f_{n+1}\|\le2^{-n-1}\), and the sequence \((f_n)\) is uniformly Cauchy; its uniform limit \(f\) is continuous.

Let \(M\) be the union of the sets \(F(\lambda)\setminus C(\lambda)\) over the dyadic rationals \(\lambda\in[0,1]\). Each of them is rare by Lemma 2.1(1), so \(M\) is meager. Let \(\omega\notin M\). If \(\omega\in C(0)\), then \(g(\omega)=0=f_n(\omega)\). Otherwise \(\omega\in C(k2^{-n})\setminus C((k-1)2^{-n})\) for some \(k\ge1\). Then \(g(\omega)\le k2^{-n}\), and \(\omega\notin F((k-1)2^{-n})\), because on the dyadic levels \(F\) and \(C\) agree outside \(M\); so \(g(\omega)>(k-1)2^{-n}\). Hence \(|g(\omega)-f_n(\omega)|\le2^{-n}\) for every \(n\), and \(g(\omega)=f(\omega)\). So \(g=f\) outside the meager set \(M\).

(3)\(\Rightarrow\)(2). Let \(S\) be nonempty and bounded above by \(b\), fix \(s_0\in S\), and let \(g=\sup_{s\in S}s\). Then \(g\) is lsc and \(s_0\le g\le b\). Let \(f\) be the continuous function given by (3). As shown above, \(f\ge g\), so \(f\) is an upper bound of \(S\). If \(h\in C_{\mathbb R}(\Omega)\) is an upper bound of \(S\), then \(h\ge g=f\) outside a meager set, that is, on a dense set, so \(h\ge f\). Hence \(f\) is the least upper bound, and \(f=g^*\).

(2)\(\Rightarrow\)(1). Let \(G\) be open, and let \(S\) be the set of \(x\in C_{\mathbb R}(\Omega)\) with \(0\le x\le1_G\). It is bounded above by \(1\); let \(f\) be its least upper bound. By Urysohn's lemma, for every \(\omega\in G\) some \(x\in S\) has \(x(\omega)=1\). Hence \(0\le f\le1\), \(f=1\) on \(G\), and \(f=1\) on \(\overline G\) by continuity. Suppose \(f(\omega_0)>0\) for some \(\omega_0\notin\overline G\). By Urysohn's lemma there is \(h\in C_{\mathbb R}(\Omega)\) with \(0\le h\le1\), \(h=1\) on \(\overline G\) and \(h(\omega_0)=0\). Then \(fh\) is an upper bound of \(S\): on \(\overline G\) it equals \(f\), and outside \(G\) every \(x\in S\) vanishes. But \(fh\le f\) and \(fh(\omega_0)=0<f(\omega_0)\), which contradicts the choice of \(f\). So \(f=1_{\overline G}\). Since \(f\) is continuous, \(\overline G\) is open. \(\square\)

**Theorem 4.4** (Extending continuous functions). Let \(\Omega\) be a stonean space and \(D\subseteq\Omega\) a subset that is dense or open. Every bounded continuous function on \(D\) extends to a continuous function on \(\Omega\). If \(D\) is dense, the extension is unique, and \(x\mapsto x|_D\) is an isometric \(*\)-isomorphism of \(C(\Omega)\) onto \(C_b(D)\). So \(\Omega\) is the Stone–Čech compactification of every dense subset.

**Proof.** First let \(D\) be dense and \(f:D\to[0,1]\) continuous; the general case follows by taking real and imaginary parts and an affine change. For a rational \(r\) let \(O_r\) be the union of all open \(V\subseteq\Omega\) with \(V\cap D\subseteq\{f<r\}\), and let \(C_r=\overline{O_r}\), a clopen set.

*Step 1.* \(O_r\cap D=\{d\in D:f(d)<r\}\). One inclusion is the definition. If \(f(d)<r\), continuity of \(f\) at \(d\) gives an open \(V\ni d\) with \(f<r\) on \(V\cap D\), so \(d\in O_r\).

*Step 2.* If \(r<s\), then \(O_r\subseteq O_s\) and \(C_r\subseteq C_s\). If \(r\le0\), then \(O_r\cap D=\varnothing\), so the open set \(O_r\) is empty because \(D\) is dense, and \(C_r=\varnothing\). If \(r>1\), then \(O_r=\Omega\).

*Step 3.* Define \(F(\omega)=\inf\{r\in\mathbb Q:\omega\in C_r\}\). By Step 2, \(0\le F\le1\). For real \(t\),
\[
\{F<t\}=\bigcup_{r<t}C_r,\qquad\{F>t\}=\bigcup_{s>t}(\Omega\setminus C_s),
\]
with \(r,s\) rational. The first identity is the definition of an infimum. For the second, if \(F(\omega)>t\), choose a rational \(s\) with \(t<s<F(\omega)\); then \(\omega\notin C_s\). If \(\omega\notin C_s\) with \(s>t\), then \(\omega\notin C_r\) for every \(r\le s\), and \(F(\omega)\ge s>t\). Both unions consist of clopen sets, so \(F\) is continuous.

*Step 4.* \(F=f\) on \(D\). If \(d\in D\) and \(f(d)<r\), then \(d\in O_r\subseteq C_r\) by Step 1, so \(F(d)\le f(d)\). Let \(r<f(d)\), choose \(s\) with \(r<s<f(d)\), and an open \(V\ni d\) with \(f>s\) on \(V\cap D\). If \(d\in C_r=\overline{O_r}\), then \(V\cap O_r\) is a nonempty open set, and it contains a point \(d'\in D\). But then \(f(d')<r\) by Step 1 and \(f(d')>s>r\), which is impossible. So \(d\notin C_r\) whenever \(r<f(d)\), and \(F(d)\ge f(d)\).

Now let \(D\) be open. Its closure \(\overline D\) is clopen, hence stonean, and \(D\) is dense in it. Extend \(f\) to \(\overline D\) as above and by \(0\) on \(\Omega\setminus\overline D\); the result is continuous because \(\overline D\) is clopen.

For dense \(D\), two continuous extensions agree on \(D\), hence everywhere. Restriction to \(D\) is an injective \(*\)-homomorphism of \(C(\Omega)\) into \(C_b(D)\). It preserves the supremum norm, since \(D\) is dense, and it is onto by what we proved. The spectrum of \(C_b(D)\) is the Stone–Čech compactification of \(D\), with \(D\) embedded by point evaluations; [Exercise 2.4 of the C\*-algebra lesson](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-04) proves the construction and its universal compact-target extension property. A subspace of a compact Hausdorff space is completely regular: an open neighbourhood in the subspace is the intersection with an ambient open set, and an ambient Urysohn function separating the point from the complement restricts to the required bounded function. Thus this provider applies to \(D\). Under the isomorphism the evaluation at \(d\in D\) corresponds to the evaluation at \(d\), so \(\Omega\) is \(\beta D\). \(\square\)

**Example 4.5.** (a) For every set \(I\) the Stone–Čech compactification \(\beta I\) of the discrete space \(I\) is stonean. Indeed \(C(\beta I)\cong\ell^\infty(I)\), and every nonempty set of real functions on \(I\) that is bounded above has a pointwise supremum, which is its least upper bound in \(\ell^\infty(I)\); Theorem 4.3 applies.

(b) \([0,1]\) is not stonean: the closure of \([0,\frac12)\) is not open. In fact no infinite compact metrizable space is stonean (Exercise 12.1), and so the Cantor set, although it has a base of clopen sets, is not stonean.

(c) If \(\Omega\) is stonean and \(\omega\) is not an isolated point, then \(\Omega\setminus\{\omega\}\) is open and dense, and by Theorem 4.4 it has \(\Omega\) as its Stone–Čech compactification.

### 5. Normal measures

**Definition 5.1.** Let \(\Omega\) be stonean. A Radon measure \(\mu\) on \(\Omega\) is *normal* if \(\mu(f)=\sup_i\mu(f_i)\) for every increasing net \((f_i)\) in \(C_{\mathbb R}(\Omega)\) with \(\sup_i\|f_i\|<\infty\), where \(f\) is its least upper bound in \(C_{\mathbb R}(\Omega)\). A complex Radon measure is called *normal* when it is a finite sum of complex multiples of positive normal measures.

The least upper bound \(f\) exists by Theorem 4.3. Normality asks that the integral see \(f\), and not only the pointwise supremum, which may be smaller on a meager set.

**Theorem 5.2** (Normal measures kill rare sets). Let \(\Omega\) be stonean. For a Radon measure \(\mu\) on \(\Omega\) the following are equivalent.

1. \(\mu\) is normal.
2. Every rare set is \(\mu\)-null.
3. Every meager set is \(\mu\)-null.

**Proof.** (1)\(\Rightarrow\)(2). A rare set lies in its closure, which is a closed rare set, so let \(R\) be closed and rare. The open set \(\Omega\setminus R\) is dense. By Lemma 4.2(3) it is the union of the increasing net \((C_i)\) of clopen sets contained in it. The net \((1_{C_i})\) in \(C_{\mathbb R}(\Omega)\) has least upper bound \(1\): an upper bound is at least \(1\) on the dense set \(\Omega\setminus R\), hence everywhere. By normality and Lemma 2.3(1), \(\mu(\Omega)=\sup_i\mu(C_i)=\mu(\Omega\setminus R)\). So \(\mu(R)=0\).

(2)\(\Rightarrow\)(3). A meager set lies in a countable union of closed rare sets.

(3)\(\Rightarrow\)(1). Let \((f_i)\) be as in Definition 5.1 with least upper bound \(f\), and let \(g=\sup_if_i\) pointwise. By Theorem 4.3, \(f=g\) outside a meager set, which is null. By Lemma 2.3(2), \(\mu(f)=\int g\,d\mu=\sup_i\mu(f_i)\). \(\square\)

**Lemma 5.3** (Open kernels of measurable sets). Let \(\Omega\) be stonean, \(\mu\) a normal measure on \(\Omega\), and \(E\) a \(\mu\)-measurable set. There is an open set \(G\subseteq E\) with \(\mu(E\setminus G)=0\).

**Proof.** By inner regularity there are compact sets \(K_n\subseteq E\) with \(\mu(E\setminus K_n)<1/n\). The interior \(K_n^\circ\) is clopen (Lemma 4.2(1)), and \(K_n\setminus K_n^\circ\) is rare (Lemma 2.1(1)), hence null (Theorem 5.2). The open set \(G=\bigcup_nK_n^\circ\) lies in \(E\), and \(\mu(E\setminus G)\le\mu(E\setminus K_n)+\mu(K_n\setminus K_n^\circ)<1/n\) for every \(n\). \(\square\)

**Corollary 5.4.** Let \(\Omega\) be stonean and \(\mu\) a normal measure on \(\Omega\).

1. The closure of a \(\mu\)-null set is \(\mu\)-null.
2. If \(E\) is \(\mu\)-measurable, the sets \(E\), \(\overline E\), \(E^\circ\), \((\overline E)^\circ\) and \(\overline{E^\circ}\) differ from each other by null sets. The last two are clopen. So every measurable set agrees up to a null set with a clopen set.
3. The support of \(\mu\) is clopen.
4. Let \(S\) be the support of \(\mu\). A \(\mu\)-measurable set \(E\) is null if and only if \(E\cap S\) is rare. In particular, two normal measures with the same support have the same null sets, and if \(S=\Omega\), the measurable null sets are exactly the measurable rare sets.

**Proof.** (1) Let \(N\) be null. It is measurable, so Lemma 5.3 applied to \(\Omega\setminus N\) gives an open \(G\subseteq\Omega\setminus N\) with \(\mu(\Omega\setminus G)=0\). The closed set \(\Omega\setminus G\) contains \(N\), hence \(\overline N\).

(2) Lemma 5.3 gives an open \(G\subseteq E\) with \(E\setminus G\) null, and \(G\subseteq E^\circ\); so \(E\setminus E^\circ\) is null. Applied to \(\Omega\setminus E\), it gives an open \(G'\subseteq\Omega\setminus E\) with \((\Omega\setminus E)\setminus G'\) null. Then \(\overline E\subseteq\Omega\setminus G'\), so \(\overline E\setminus E\) is null. The other two sets lie between \(E^\circ\) and \(\overline E\). They are clopen by Lemma 4.2(1) and Definition 4.1.

(3) Let \(V\) be the union of all open null sets. By Lemma 2.3(1), applied to the net of finite unions, \(V\) is null. By (1) so is \(\overline V\), which is open because \(\Omega\) is stonean. So \(\overline V\subseteq V\), and \(V\) is clopen. The support \(\Omega\setminus V\) is clopen.

(4) \(\mu(E)=\mu(E\cap S)\). If \(E\cap S\) is null, so is its closure by (1), and the interior of that closure is an open null set inside \(S\). An open subset of the support with measure zero is empty, since it lies in \(V\). So \(E\cap S\) is rare. The converse is Theorem 5.2. \(\square\)

**Theorem 5.5** (Measurable functions are almost continuous). Let \(\Omega\) be stonean, \(\mu\) a normal measure on \(\Omega\), and \(f\) a bounded real \(\mu\)-measurable function. Then \(f=f_*=f^*\) almost everywhere, the functions \((f_*)^*\) and \((f^*)_*\) are continuous, and both agree with \(f\) almost everywhere. Consequently, every element of \(L^\infty(\Omega,\mu)\) contains a continuous function. Let \(S\) be the support of \(\mu\). The map that sends \(x\in C(S)\) to the class of its extension by \(0\) is an isometric \(*\)-isomorphism
\[
C(S)\longrightarrow L^\infty(\Omega,\mu).
\tag{5.1}
\]
If \(S=\Omega\), the map \(x\mapsto[x]\) from \(C(\Omega)\) onto \(L^\infty(\Omega,\mu)\) is an isometric \(*\)-isomorphism.

**Proof.** *Step 1.* Choose simple functions \(s_n\) with \(|f-s_n|\le1/n\) everywhere, each of the form \(s_n=\sum_kc_k1_{E_k}\) for a finite partition of \(\Omega\) into measurable sets \(E_k\). Lemma 5.3 gives open sets \(G_k\subseteq E_k\) with \(\mu(E_k\setminus G_k)=0\). Their union \(W_n\) is open, \(\mu(\Omega\setminus W_n)=0\), and \(s_n\) is constant on each \(G_k\). Put \(W=\bigcap_nW_n\); then \(\mu(\Omega\setminus W)=0\). Let \(\omega\in W\) and \(n\ge1\). The point \(\omega\) lies in one of the sets \(G_k\) that make up \(W_n\), and for \(\omega'\in G_k\),
\[
\begin{gathered}
|f(\omega')-f(\omega)|\\
\le|f(\omega')-s_n(\omega')|+|s_n(\omega)-f(\omega)|\le2/n .
\end{gathered}
\]
So \(f\) is continuous at \(\omega\), and \(f_*(\omega)=f(\omega)=f^*(\omega)\) by Lemma 2.2(1).

*Step 2.* The function \(f_*\) is bounded and lsc. By Theorem 4.3, \((f_*)^*\) is continuous and agrees with \(f_*\) outside a meager set, which is null (Theorem 5.2). Applying this to \(-f\), and using \((-f)^*=-f_*\) and \((-f)_*=-f^*\), shows that \((f^*)_*\) is continuous and agrees with \(f^*\) almost everywhere. With Step 1, all five functions agree almost everywhere.

*Step 3.* For continuous \(x\), the set \(\{|x|>c\}\) is open, so it is null exactly when it misses \(S\). Hence \(\|[x]\|_\infty=\sup_S|x|\). Since \(S\) is clopen, every continuous function on \(S\) is the restriction of a continuous function on \(\Omega\) (extend by \(0\)). So (5.1) is well defined and isometric, and by Step 2 it is onto. \(\square\)

**Theorem 5.6** (Normal and singular parts). Let \(\Omega\) be stonean. Every Radon measure \(\mu\) on \(\Omega\) can be written in exactly one way as \(\mu=\mu_n+\mu_s\), where \(\mu_n\) is a normal measure and \(\mu_s\) is a Radon measure concentrated on a meager set, that is, \(\mu_s(\Omega\setminus M)=0\) for some meager Borel set \(M\).

**Proof.** *Existence.* Let \(\alpha\) be the supremum of \(\mu(R)\) over closed rare sets \(R\). Finite unions of closed rare sets are closed and rare, so there are closed rare sets \(R_1\subseteq R_2\subseteq\cdots\) with \(\mu(R_n)\to\alpha\). Their union \(M\) is a meager Borel set with \(\mu(M)=\alpha\). Put \(\mu_s(E)=\mu(E\cap M)\) and \(\mu_n(E)=\mu(E\setminus M)\). Both are finite Borel measures below \(\mu\), and they inherit outer regularity and inner regularity on open sets from \(\mu\), since for instance \(\mu_s(U\setminus E)\le\mu(U\setminus E)\). Let \(R\) be closed and rare. Each \(R\cup R_n\) is closed and rare, so \(\mu(R\cup R_n)\le\alpha\), and letting \(n\to\infty\) gives \(\mu(R\cup M)\le\alpha=\mu(M)\). Hence \(\mu_n(R)=\mu(R\setminus M)=0\). By Theorem 5.2, \(\mu_n\) is normal.

*Uniqueness.* Let \(\mu=\nu_n+\nu_s\) be another such decomposition, with \(\nu_s\) concentrated on the meager set \(M'\). The set \(M\cup M'\) is meager, so \(\mu_n\) and \(\nu_n\) vanish on it. For a Borel set \(E\), \[
\begin{gathered}
\mu_s(E)\\
=\mu_s(E\cap(M\cup M'))\\
=\mu(E\cap(M\cup M')),
\end{gathered}
\] and in the same way \(\nu_s(E)=\mu(E\cap(M\cup M'))\). So \(\mu_s=\nu_s\) and \(\mu_n=\nu_n\). \(\square\)

**Corollary 5.7.** If a stonean space carries no normal measure other than \(0\), every Radon measure on it is concentrated on a meager set.

**Proof.** In the decomposition \(\mu=\mu_n+\mu_s\) of Theorem 5.6 the normal part \(\mu_n\) is \(0\), so \(\mu=\mu_s\). \(\square\)

**Example 5.8** (The space \(\beta I\)). Let \(I\) be a set and \(\Omega=\beta I\), which is stonean by Example 4.5. The points of \(I\) are isolated in \(\beta I\). Indeed, the indicator \(1_{\{i\}}\in\ell^\infty(I)=C(\beta I)\) is the indicator of a clopen set, and a character \(\omega\) of \(\ell^\infty(I)\) with \(\omega(1_{\{i\}})=1\) satisfies \(\omega(f)=\omega(f1_{\{i\}})=f(i)\) for all \(f\), so this clopen set is \(\{i\}\). So a set that contains a point of \(I\) is not rare. A set \(R\subseteq\beta I\setminus I\) is rare: its closure lies in the closed set \(\beta I\setminus I\), which has empty interior because \(I\) is dense. So the rare sets are exactly the subsets of \(\beta I\setminus I\), and by Theorem 5.2 the normal measures are the Radon measures \(\mu\) with \(\mu(\beta I\setminus I)=0\), that is, \(\mu=\sum_{i\in I}c_i\delta_i\) with \(c_i\ge0\) and \(\sum_ic_i<\infty\). The decomposition of Theorem 5.6 is \(\mu_n=\mu(\,\cdot\cap I)\) and \(\mu_s=\mu(\,\cdot\cap(\beta I\setminus I))\). For instance, a point mass at a point of \(\beta I\setminus I\) is purely singular.

### 6. Hyperstonean spaces and the decomposition of a stonean space

**Definition 6.1.** Let \(\Omega\) be stonean. A family \(\mathfrak F\) of normal measures is *sufficient* if for every nonzero \(x\in C(\Omega)\) with \(x\ge0\) some \(\mu\in\mathfrak F\) has \(\mu(x)>0\). The space \(\Omega\) is *hyperstonean* if the family of all normal measures on \(\Omega\) is sufficient.

**Lemma 6.2.** A family \(\mathfrak F\) of normal measures is sufficient exactly when the supports of its members have a dense union.

**Proof.** Suppose these supports have a dense union, and let \(x\ge0\) be nonzero. Then the open set \(\{x>0\}\) meets the support of some \(\mu\in\mathfrak F\). A nonempty open subset of the support has positive measure, so \(\mu(x)>0\). If the union is not dense, there is a nonempty clopen set \(C\) disjoint from all supports (Lemma 4.2(3)), and \(\mu(1_C)=0\) for every \(\mu\in\mathfrak F\). \(\square\)

**Proposition 6.3** (Rare sets in a hyperstonean space). Let \(\Omega\) be hyperstonean and \(\mathfrak F\) a sufficient family of normal measures.

1. A set \(A\subseteq\Omega\) is rare exactly when it is \(\mu\)-null for all \(\mu\in\mathfrak F\). In particular every meager set is rare.
2. If \(E\) is \(\mu\)-measurable for every \(\mu\in\mathfrak F\), then \((\overline E)^\circ=\overline{E^\circ}\), and the sets \(E\), \(\overline E\), \(E^\circ\) and \((\overline E)^\circ\) differ from each other by rare sets.
3. If \(f\) is bounded, real and \(\mu\)-measurable for every \(\mu\in\mathfrak F\), then \((f_*)^*=(f^*)_*\). This function is continuous, and it agrees with \(f\), \(f_*\) and \(f^*\) outside a rare set.

**Proof.** (1) A rare set is null for every normal measure (Theorem 5.2). Conversely, let \(A\) be null for every \(\mu\in\mathfrak F\). By Corollary 5.4(1), \(\overline A\) is null for every \(\mu\in\mathfrak F\), and so is the open set \((\overline A)^\circ\). If it were not empty, it would contain a nonempty clopen set \(C\), and \(1_C\) would contradict sufficiency. So \(A\) is rare. A meager set is null for every normal measure, hence rare.

(2) Both \((\overline E)^\circ\) and \(\overline{E^\circ}\) are clopen, and each differs from \(E\) by a set that is null for every \(\mu\in\mathfrak F\) (Corollary 5.4(2)). So their symmetric difference is a clopen set that is null for every \(\mu\in\mathfrak F\); by (1) it is rare and open, hence empty. The differences in the second statement are null for every \(\mu\in\mathfrak F\), hence rare by (1).

(3) Both functions are continuous (Theorem 5.5) and agree \(\mu\)-almost everywhere for every \(\mu\in\mathfrak F\). The set where they differ is open and null for every \(\mu\in\mathfrak F\), hence empty by (1). The exceptional sets in Theorem 5.5 are null for every \(\mu\in\mathfrak F\), hence rare. \(\square\)

## C. Recognize von Neumann algebras and classify their models

We can now combine two independent tests: order completeness gives a stonean spectrum, while enough normal observations give a hyperstonean spectrum. The equivalence theorem constructs a von Neumann representation from these observations and recovers them from vector functionals in the opposite direction. It also explains why an abstract isomorphism need not be implemented by a unitary in a particular representation.

**Checkpoint: multiplicity versus the algebra.** Multiplication by \(f\) on \(L^2[0,1]\) and by \(f\oplus f\) on its doubled Hilbert space obey the same algebraic rules. In the doubled space the operator swapping the summands commutes with every multiplication operator. The commutant has therefore changed. The spatial-isomorphism theorem needs its cyclicity and maximality hypotheses; Example 7.5 records the failures when they are removed. Atomic and diffuse decomposition concerns the algebra's projections, whereas this multiplicity concerns its action.

The countable-generation results then compress many commuting observables into one self-adjoint generator. The interval model for the diffuse case retains its separate sigma-finiteness and nonzero hypotheses.

### 7. Spectra of abelian von Neumann algebras

We can now say which compact spaces are spectra of abelian von Neumann algebras, and describe the algebras as \(L^\infty\) spaces. For a family \((B_i)_{i\in I}\) of C\*-algebras, \(\prod_iB_i\) denotes the C\*-algebra of bounded families \((b_i)\) with the supremum norm.

**Theorem 7.1** (Abelian von Neumann algebras and hyperstonean spaces). Let \(A\) be an abelian C\*-algebra and \(\Omega\) its spectrum. The following are equivalent.

1. \(\Omega\) is hyperstonean.
2. \(A\) is \(*\)-isomorphic to some von Neumann algebra: it has a faithful representation \(\pi\) such that \(\pi(A)\) is a von Neumann algebra.
3. \(A\cong L^\infty(\Gamma,\mu)\) for a locally compact space \(\Gamma\) and a positive Radon measure \(\mu\) on \(\Gamma\).
4. \(A\cong L^\infty(\Gamma,\mu)\), where \(\Gamma\) is the union of pairwise disjoint compact open sets \(\Gamma_i\), \(i\in I\), each of them hyperstonean, and \(\mu\) is a Radon measure on \(\Gamma\) whose restriction \(\mu_i\) to each \(\Gamma_i\) is a normal measure with support \(\Gamma_i\).

In (4) one can take \(\Gamma\) to be an open dense subset of \(\Omega\), and then \(A\cong C(\Omega)\cong\prod_iC(\Gamma_i)\cong\prod_iL^\infty(\Gamma_i,\mu_i)\).

*Reference:* the result goes back to Dixmier (1951); [Kostecki, Sections 5.6 and 5.8] defines hyperstonean spaces and states the Dixmier–Grothendieck theorem.

**Proof.** If \(A=0\), its spectrum is empty, which is hyperstonean; take \(\Gamma=\varnothing\) and the zero Hilbert space to obtain all four conditions. Assume henceforth that \(A\ne0\). (2)\(\Rightarrow\)(1). We may assume that \(A=M\) acts on a Hilbert space \(H\) as a von Neumann algebra. The Gelfand isomorphism is an isomorphism of ordered spaces from \(M_h\) onto \(C_{\mathbb R}(\Omega)\), because the positive elements of \(C(\Omega)\) are the nonnegative functions. Let \(S\subseteq M_h\) be nonempty and bounded above by \(b\), and fix \(s_0\in S\). The maxima of the finite subsets of \(S\) that contain \(s_0\) form an increasing net with the same upper bounds as \(S\), and it is bounded in norm, since it lies between \(s_0\) and \(b\). By Lemma 2.4 its strong limit is its least upper bound in \(M_h\). So \(C_{\mathbb R}(\Omega)\) is conditionally complete, and \(\Omega\) is stonean by Theorem 4.3. For \(\xi\in H\) let \(\mu_\xi\) be the Radon measure on \(\Omega\) given by the positive functional \(\omega_\xi\). If \((x_i)\) is a bounded increasing net in \(M_h\) with least upper bound \(x\), then \(x_i\to x\) strongly by Lemma 2.4, so \(\omega_\xi(x_i)\to\omega_\xi(x)\). So \(\mu_\xi\) is normal. If \(x\in M_+\) is not zero, then \(\omega_\xi(x)>0\) for some \(\xi\). So the measures \(\mu_\xi\) form a sufficient family, and \(\Omega\) is hyperstonean.

(1)\(\Rightarrow\)(4). The space \(\Omega\) is compact, so \(A\) is unital and \(A\cong C(\Omega)\). By Zorn's lemma choose a maximal family \((\mu_i)_{i\in I}\) of nonzero normal measures with pairwise disjoint supports \(\Gamma_i\). These supports are clopen (Corollary 5.4(3)), so \(\Gamma=\bigcup_i\Gamma_i\) is open. It is dense. Otherwise the clopen set \(W=\Omega\setminus\overline\Gamma\) is not empty, some normal measure \(\mu\) has \(\mu(W)>0\) because \(\Omega\) is hyperstonean, and the restriction of \(\mu\) to \(W\) is a nonzero normal measure whose support lies in \(W\); adding it to the family contradicts maximality.

Restriction \(x\mapsto(x|_{\Gamma_i})_i\) is a \(*\)-homomorphism from \(C(\Omega)\) to \(\prod_iC(\Gamma_i)\). It is isometric because \(\Gamma\) is dense. It is onto: a bounded family \((x_i)\) defines a bounded continuous function on the open set \(\Gamma\), since the \(\Gamma_i\) are open, and Theorem 4.4 extends it to \(\Omega\). Each \(\Gamma_i\) is clopen, hence stonean, and \(\mu_i\) is a normal measure on it with full support; so \(\Gamma_i\) is hyperstonean by Lemma 6.2. By Theorem 5.5, \(C(\Gamma_i)\cong L^\infty(\Gamma_i,\mu_i)\). The subspace \(\Gamma\) is locally compact and is the topological disjoint union of the compact open sets \(\Gamma_i\). For \(x\in C_c(\Gamma)\) the compact support of \(x\) meets only finitely many \(\Gamma_i\), so \(\mu(x)=\sum_i\int_{\Gamma_i}x\,d\mu_i\) is a finite sum. It is a positive linear functional on \(C_c(\Gamma)\), hence a Radon measure on \(\Gamma\), and its restriction to \(\Gamma_i\) is \(\mu_i\). A set \(N\subseteq\Gamma\) is locally \(\mu\)-null if and only if every \(N\cap\Gamma_i\) is \(\mu_i\)-null, and a function on \(\Gamma\) is \(\mu\)-measurable if and only if each restriction to \(\Gamma_i\) is \(\mu_i\)-measurable, because every compact subset of \(\Gamma\) lies in finitely many \(\Gamma_i\). So restriction is an isometric \(*\)-isomorphism of \(L^\infty(\Gamma,\mu)\) onto \(\prod_iL^\infty(\Gamma_i,\mu_i)\). Composing, \[
\begin{gathered}
A\\
\cong C(\Omega)\\
\cong\prod_iC(\Gamma_i)\\
\cong\prod_iL^\infty(\Gamma_i,\mu_i)\\
\cong L^\infty(\Gamma,\mu).
\end{gathered}
\]

(4)\(\Rightarrow\)(3) is clear.

(3)\(\Rightarrow\)(2). The representation of \(L^\infty(\Gamma,\mu)\) on \(L^2(\Gamma,\mu)\) by multiplication operators is faithful, and its image is a maximal abelian von Neumann algebra, for every Radon measure; both facts are proved in Proposition 3.2a. \(\square\)

**Remark 7.2** (Examples). The spectrum of \(\ell^\infty(I)\) is \(\beta I\), and its normal measures were found in Example 5.8. The spectrum of \(L^\infty[0,1]\) is a hyperstonean space without isolated points, since \(L^\infty[0,1]\) has no minimal projections (Exercise 12.3). Every abelian von Neumann algebra of infinite dimension has an infinite hyperstonean space as its spectrum, and such a space is never metrizable (Exercise 12.1). The algebra \(C[0,1]\) is isomorphic to no von Neumann algebra, since \([0,1]\) is not stonean. Section 9 gives an abelian C\*-algebra whose spectrum is stonean but carries no normal measure at all; it is monotone complete but isomorphic to no von Neumann algebra.

**Proposition 7.3** (Isomorphisms preserve monotone limits). Let \(\theta:M\to N\) be a \(*\)-isomorphism between von Neumann algebras on Hilbert spaces \(H\) and \(K\). Then \(\theta\) maps \(M_+\) onto \(N_+\), and for every bounded increasing net \((x_i)\) in \(M_h\) with strong limit \(x\), the net \((\theta(x_i))\) converges strongly to \(\theta(x)\). In particular \(\omega_\eta\circ\theta\) preserves the limits of such nets, for every \(\eta\in K\).

**Proof.** The positive elements of a C\*-algebra are the elements \(y^*y\), so \(\theta(M_+)\subseteq N_+\) and \(\theta^{-1}(N_+)\subseteq M_+\). Hence \(\theta\) is an isomorphism of ordered spaces from \(M_h\) onto \(N_h\). By Lemma 2.4, the net \((x_i)\) has \(x\) as least upper bound in \(M_h\), and \((\theta(x_i))\) has its strong limit \(y\) as least upper bound in \(N_h\). Since \(\theta(x)\) is an upper bound of \((\theta(x_i))\), \(y\le\theta(x)\). Since \(\theta^{-1}(y)\) is an upper bound of \((x_i)\), \(x\le\theta^{-1}(y)\), that is, \(\theta(x)\le y\). \(\square\)

So \(*\)-isomorphisms of von Neumann algebras need no continuity assumption: they automatically respect monotone limits.

**Theorem 7.4** (Cyclic vectors and spatial isomorphisms).

1. Let \(M\subseteq B(H)\) and \(N\subseteq B(K)\) be abelian von Neumann algebras with cyclic vectors \(\xi\) and \(\eta\). Every \(*\)-isomorphism \(\theta:M\to N\) is spatial: there is a unitary \(U:H\to K\) with \(\theta(x)=UxU^*\) for all \(x\in M\).
2. An abelian von Neumann algebra has a cyclic vector exactly when it is both maximal abelian and \(\sigma\)-finite.
3. Every \(*\)-isomorphism between maximal abelian von Neumann algebras is spatial.

**Proof.** If one algebra or Hilbert space is zero, the isomorphism forces both algebras to be zero; their units are the identity operators, so both Hilbert spaces are zero and the unique empty unitary applies. The zero vector is cyclic and the zero algebra is maximal abelian and sigma-finite. We may therefore assume the spaces in use are nonzero. (1) Let \(\Omega\) be the spectrum of \(M\), which is stonean by Theorem 7.1, and \(x\mapsto\hat x\) the Gelfand isomorphism of \(M\) onto \(C(\Omega)\). Let \(\mu\) and \(\nu\) be the Radon measures on \(\Omega\) with \(\int\hat x\,d\mu=\langle x\xi,\xi\rangle\) and \(\int\hat x\,d\nu=\langle\theta(x)\eta,\eta\rangle\); the second functional is positive by Proposition 7.3. Both measures are normal, by Lemma 2.4 and Proposition 7.3, because the supremum in \(C_{\mathbb R}(\Omega)\) of an increasing net that is bounded in norm corresponds to its least upper bound in \(M_h\). Both have support \(\Omega\). Indeed, \(\xi\) is cyclic for \(M\), hence for the larger algebra \(M'\), so \(\xi\) separates \(M\) (see [The double commutant theorem](the-double-commutant-theorem.md), Proposition 9.2). Thus \(\langle x\xi,\xi\rangle=\|x^{1/2}\xi\|^2>0\) for nonzero \(x\in M_+\). In the same way \(\eta\) separates \(N\), and \(\theta\) is injective. If the support of a positive functional on \(C(\Omega)\) were not all of \(\Omega\), Urysohn's lemma would give a nonzero \(x\ge0\) that vanishes on the support, with integral \(0\). By Corollary 5.4(4), \(\mu\) and \(\nu\) have the same null sets. By Corollary 3.4 there is a unitary \(V:L^2(\Omega,\mu)\to L^2(\Omega,\nu)\) with \(V\pi_\mu(f)=\pi_\nu(f)V\). The representations \(\hat x\mapsto x\) on \(H\) and \(\hat x\mapsto\theta(x)\) on \(K\) have the cyclic vectors \(\xi\) and \(\eta\), so Theorem 3.1(2) gives unitaries \(U_1:L^2(\Omega,\mu)\to H\) and \(U_2:L^2(\Omega,\nu)\to K\) with \(U_1\pi_\mu(\hat x)U_1^*=x\) and \(U_2\pi_\nu(\hat x)U_2^*=\theta(x)\). Then \(U=U_2VU_1^*\) satisfies \[
\begin{gathered}
UxU^*\\
=U_2V\pi_\mu(\hat x)V^*U_2^*\\
=U_2\pi_\nu(\hat x)U_2^*\\
=\theta(x).
\end{gathered}
\]

(2) Let \(M\) have a cyclic vector \(\xi\). It is maximal abelian by Corollary 3.3. If \((p_j)\) are pairwise orthogonal nonzero projections in \(M\), then \(\langle p_j\xi,\xi\rangle>0\) because \(\xi\) separates \(M\), and every finite sum of these numbers is at most \(\|\xi\|^2\). So the family is countable, and \(M\) is \(\sigma\)-finite.

Conversely, let \(M\) be maximal abelian and \(\sigma\)-finite. By Zorn's lemma choose a maximal family of unit vectors \(\xi_k\) such that the subspaces \([M\xi_k]\) are pairwise orthogonal. The projection \(p_k\) onto \([M\xi_k]\) lies in \(M'\), because the subspace is invariant under the self-adjoint algebra \(M\), and \(M'=M\). The \(p_k\) are nonzero and pairwise orthogonal, so there are countably many; list them without repetitions as \(p_1,p_2,\dots\), using a finite list and finite sum when the family is finite. Their sum is \(1\). Indeed, let \(\zeta\) be orthogonal to every \([M\xi_k]\). Each \(p_k\) commutes with \(M\), so \(p_kx\zeta=xp_k\zeta=0\) for \(x\in M\), and \([M\zeta]\) is orthogonal to all \([M\xi_k]\). By maximality \(\zeta=0\). Put \(\xi=\sum_k2^{-k}\xi_k\). Then \(p_k\xi=2^{-k}\xi_k\) and \(p_k\in M\), so \([M\xi]\) contains every \([M\xi_k]\). Hence \(\xi\) is cyclic.

(3) Let \(\theta:M\to N\) be a \(*\)-isomorphism, where \(M\subseteq B(H)\) and \(N\subseteq B(K)\) are maximal abelian. As in the proof of (2), without the countability, choose unit vectors \(\xi_k\), \(k\in\Lambda\), such that the projections \(e_k\) onto \([M\xi_k]\) are pairwise orthogonal, lie in \(M\), and have sum \(1\). Put \(f_k=\theta(e_k)\), pairwise orthogonal projections in \(N\). By Proposition 7.3, applied to the finite partial sums, \(\sum_kf_k=\theta(1)=1\). Since \(e_k\in M=M'\) and \(f_k\in N=N'\), the algebras \(M_k=\{x|_{e_kH}:x\in M\}\) and \(N_k=\{y|_{f_kK}:y\in N\}\) are von Neumann algebras on \(e_kH\) and \(f_kK\), and their commutants are \(\{x'|_{e_kH}:x'\in M'\}=M_k\) and \(N_k\) (see [The double commutant theorem](the-double-commutant-theorem.md), Theorem 5.8). So both are maximal abelian. The kernel of \(x\mapsto x|_{e_kH}\) is \(M(1-e_k)\), which \(\theta\) maps onto \(N(1-f_k)\), the kernel of \(y\mapsto y|_{f_kK}\). So \(\theta\) induces a \(*\)-isomorphism \(\theta_k:M_k\to N_k\). The algebra \(M_k\) has the cyclic vector \(\xi_k\), so it is \(\sigma\)-finite by (2); \(\sigma\)-finiteness is defined through orthogonal projections, so \(N_k\) is \(\sigma\)-finite too, and by (2) it has a cyclic vector. By (1) there is a unitary \(U_k:e_kH\to f_kK\) with \(\theta_k(z)=U_kzU_k^*\). The unitary \(U=\bigoplus_kU_k:H\to K\) satisfies, for \(x\in M\),
\[
\begin{gathered}
\theta(x)\\
=\sum_k\theta(x)f_k\\
=\sum_k\theta(xe_k)\\
=\sum_kU_k(x|_{e_kH})U_k^*\\
=UxU^*,
\end{gathered}
\]
with sums converging strongly. \(\square\)

**Example 7.5.** (a) The algebra \(\ell^\infty(I)\) on \(\ell^2(I)\), for uncountable \(I\), is maximal abelian but not \(\sigma\)-finite, and it has no cyclic vector (Example 1.1). (b) The algebra \(\mathcal A_2\) of Example 1.3 is \(\sigma\)-finite but not maximal abelian, and the isomorphism \(M_f\mapsto M_f\oplus M_f\) from the algebra of Example 1.2 onto it is not spatial. So maximality cannot be dropped in Theorem 7.4(3). (c) On \(\mathbb C^4\) the map \(\operatorname{diag}(a,b,b,b)\mapsto\operatorname{diag}(a,a,b,b)\) is a \(*\)-isomorphism of abelian von Neumann algebras that is not spatial, since it sends a projection of rank one to a projection of rank two.

### Atomic and diffuse regions

**Proposition 6.5** (Atomic and diffuse parts). Let \(\Omega\) be stonean, let \(I\) be the set of its isolated points, and put \(\Omega_d=\overline I\) and \(\Omega_c=\Omega\setminus\Omega_d\).

1. \(\Omega_d\) and \(\Omega_c\) are clopen. \(I\) is an open discrete subset of \(\Omega_d\) that is dense in \(\Omega_d\), and \(\Omega_c\) has no isolated points. The space \(\Omega_d\) is the Stone–Čech compactification of the discrete space \(I\), so \(C(\Omega_d)\cong\ell^\infty(I)\).
2. If \(\Omega=A\cup B\) is a partition into clopen sets such that some open discrete subset of \(A\) is dense in \(A\) and \(B\) has no isolated points, then \(A=\Omega_d\) and \(B=\Omega_c\).
3. If \(\Omega\) is hyperstonean, so are \(\Omega_d\) and \(\Omega_c\).

The clopen hypothesis in (2) is essential, as the complete counterexample in Example 6.6 proves.

**Proof.** (1) \(I\) is open, as a union of open points, so \(\Omega_d=\overline I\) is clopen, and so is \(\Omega_c\). An isolated point of the open set \(\Omega_c\) would be isolated in \(\Omega\) and so lie in \(I\subseteq\Omega_d\). The space \(\Omega_d\) is stonean and \(I\) is dense in it, so Theorem 4.4 identifies \(\Omega_d\) with \(\beta I\) and \(C(\Omega_d)\) with \(C_b(I)=\ell^\infty(I)\).

(2) Let \(D\) be an open discrete subset of \(A\) that is dense in \(A\). Each point of \(D\) is open in \(D\), \(D\) is open in \(A\), and \(A\) is open in \(\Omega\); so \(D\subseteq I\). As \(A\) is closed, \(A=\overline D\subseteq\overline I=\Omega_d\). A point of \(I\) lying in the open set \(B\) would be isolated in \(B\), so \(I\subseteq A\), and \(\Omega_d\subseteq A\) because \(A\) is closed.

(3) If \(\mathfrak F\) is a sufficient family of normal measures on \(\Omega\) and \(C\) is clopen, the restrictions of its members to \(C\) form a sufficient family on \(C\), by Lemma 6.2. \(\square\)

**Example 6.6** (The parts must be clopen). In \(\beta\mathbb N\) the isolated points are the points of \(\mathbb N\), so \(\Omega_d=\beta\mathbb N\) and \(\Omega_c=\varnothing\). The partition into \(A=\mathbb N\) and \(B=\beta\mathbb N\setminus\mathbb N\) also has the two properties of Proposition 6.5(2), except that the parts are not clopen. Clearly \(\mathbb N\) is open, discrete and dense in itself. To see that \(B\) has no isolated points, let \(p\in B\) and let \(C\) be a clopen neighbourhood of \(p\) in \(\beta\mathbb N\). The set \(C\cap\mathbb N\) is infinite: otherwise \(C=\overline{C\cap\mathbb N}\), which holds because \(\mathbb N\) is dense and \(C\) is open, would be a finite subset of \(\mathbb N\) and could not contain \(p\). Split \(C\cap\mathbb N\) into two disjoint infinite sets \(N_1,N_2\). They are open, so their closures are disjoint (Lemma 4.2(1)) and lie in \(C\). The closure of an infinite subset of \(\mathbb N\) is compact and so is not a subset of the discrete set \(\mathbb N\); hence each closure contains a point of \(B\). So \(C\cap B\) has at least two points, and \(p\) is not isolated in \(B\).

### 8. Countably generated abelian von Neumann algebras

This section shows that an abelian von Neumann algebra generated by countably many operators is generated by one self-adjoint operator, and that the nonzero \(\sigma\)-finite ones without minimal projections are all isomorphic to \(L^\infty[0,1]\). Separability of the Hilbert space is one way to ensure countable generation, but it is not needed.

**Lemma 8.1** (Singly generated algebras of functions). Let \(\Gamma\) be a compact space.

1. \(C(\Gamma)\) is generated as a C\*-algebra by a single self-adjoint element if and only if \(\Gamma\) is homeomorphic to a compact subset of \(\mathbb R\).
2. Suppose a sequence \((E_n)\) of clopen sets separates the points of \(\Gamma\): for \(\gamma\ne\gamma'\) some \(E_n\) contains exactly one of them. Then \(a=\sum_n3^{-n}(2\cdot1_{E_n}-1)\) generates \(C(\Gamma)\) as a C\*-algebra.

**Proof.** If \(\Gamma=\varnothing\), then \(C(\Gamma)=0\), generated by its zero self-adjoint element, and \(\Gamma\) is the empty compact subset of \(\mathbb R\); (2) also gives the zero generator. Assume now that \(\Gamma\ne\varnothing\). (1) Let \(a\) generate \(C(\Gamma)\). The C\*-algebra generated by \(a\) consists of uniform limits of polynomials in \(a\) without constant term, so its members are constant on the level sets of \(a\). It is all of \(C(\Gamma)\), which separates the points of \(\Gamma\) by Urysohn's lemma. So the real function \(a\) is injective, and a continuous injection of a compact space into \(\mathbb R\) is a homeomorphism onto its image. Conversely, let \(h:\Gamma\to\mathbb R\) be a homeomorphism onto its image, and put \(a=h-\min h+1\). The C\*-algebra generated by \(a\) separates points and vanishes nowhere, so it is \(C(\Gamma)\) by the Stone–Weierstrass theorem.

(2) The series converges uniformly, so \(a\) is continuous and real. Let \(\gamma\ne\gamma'\), and let \(n\) be the first index for which \(E_n\) contains exactly one of them. The terms before \(n\) agree at \(\gamma\) and \(\gamma'\), so
\[
\begin{gathered}
|a(\gamma)-a(\gamma')|\\
\ge2\cdot3^{-n}-\sum_{k>n}2\cdot3^{-k}\\
=3^{-n}>0 .
\end{gathered}
\]
So \(a\) is injective, and \(|a|\ge\frac13-\sum_{k\ge2}3^{-k}=\frac16\) everywhere. The proof of (1) applies to \(a\) directly. \(\square\)

**Theorem 8.2** (Countable generation). For an abelian von Neumann algebra \(M\) the following are equivalent.

1. \(M\) is generated by countably many elements.
2. \(M\) is generated by countably many projections.
3. \(M\) is generated by one self-adjoint element.

On a separable Hilbert space, every abelian von Neumann algebra has these properties.

**Proof.** For \(M=0\), all three assertions hold with the zero generator and zero projection. Assume \(M\ne0\); finite generating lists can be extended to sequences by appending zeros. (3)\(\Rightarrow\)(1) is clear.

(1)\(\Rightarrow\)(2). Replacing each generator \(x\) by \(\frac12(x+x^*)\) and \(\frac1{2i}(x-x^*)\), we may assume the generators \(h_1,h_2,\dots\) are self-adjoint. By Theorem 7.1 the spectrum \(\Omega\) of \(M\) is stonean; write \(\hat x\) for the Gelfand transform. For self-adjoint \(h\in M\) and rational \(\lambda\), let \(e_h(\lambda)\in M\) be the projection whose transform is the indicator of the clopen set \(C_\lambda=\overline{\{\hat h<\lambda\}}\). Then \(\{\hat h<\lambda\}\subseteq C_\lambda\subseteq\{\hat h\le\lambda\}\). Given \(\varepsilon>0\), choose rationals \(\lambda_0<\lambda_1<\dots<\lambda_N\) with \(\lambda_0<\min\hat h\), \(\lambda_N>\max\hat h\) and \(\lambda_k-\lambda_{k-1}<\varepsilon\). Then \(C_{\lambda_0}=\varnothing\) and \(C_{\lambda_N}=\Omega\). On \(C_{\lambda_k}\setminus C_{\lambda_{k-1}}\) we have \(\lambda_{k-1}\le\hat h\le\lambda_k\). Hence
\[
\Big\|h-\sum_{k=1}^N\lambda_k\big(e_h(\lambda_k)-e_h(\lambda_{k-1})\big)\Big\|\le\varepsilon .
\]
So each \(h_n\) is a norm limit of linear combinations of the countably many projections \(e_{h_n}(\lambda)\), and these projections generate \(M\).

(2)\(\Rightarrow\)(3). Let the projections \(P_1,P_2,\dots\) generate \(M\), and put \(a=\sum_k3^{-k}(2P_k-1)\in M_h\). Let \(C\) be the C\*-algebra generated by \(1\) and the \(P_k\), and \(\Gamma\) its spectrum. The transforms of the \(P_k\) are indicators of clopen sets \(E_k\), and they separate the points of \(\Gamma\), since a character of \(C\) is determined by its values on generators. By Lemma 8.1(2) the transform of \(a\) generates \(C(\Gamma)\), so every \(P_k\) lies in the C\*-algebra generated by \(a\). Hence \(M\) is generated by \(a\).

*Separable Hilbert spaces.* Let \((\zeta_k)\) be dense in \(H\). On the unit ball of \(B(H)\), the strong topology is the topology of the map \(b\mapsto(b\zeta_k)_k\) into \(H^{\mathbb N}\), because on bounded sets strong convergence follows from convergence on a dense set. The space \(H^{\mathbb N}\) is separable and metrizable, and so is every subspace of it. So the unit ball of \(M\) has a countable strongly dense subset. The von Neumann algebra that this subset generates contains the unit ball of \(M\), hence equals \(M\). \(\square\)

**Lemma 8.3** (Diffuse measures on the unit interval). Let \(\nu\) be a Radon probability measure on \([0,1]\) with no atoms, let \(m\) be Lebesgue measure, and put \(F(t)=\nu([0,t])\). Then \(V\varphi=\varphi\circ F\) defines a unitary \(V:L^2([0,1],m)\to L^2([0,1],\nu)\), and
\[
\begin{gathered}
V\{M_\varphi:\varphi\in L^\infty(m)\}V^*\\
=\{M_f:f\in L^\infty(\nu)\},\\
VM_\varphi V^*\\
=M_{\varphi\circ F}.
\end{gathered}
\tag{8.1}
\]
In particular \(L^\infty([0,1],\nu)\) is isomorphic to \(L^\infty[0,1]\).

**Proof.** Since \(\nu\) has no atoms, \(F\) is continuous and nondecreasing, with \(F(0)=0\) and \(F(1)=1\).

*The image of \(\nu\) under \(F\) is \(m\).* For \(s\in[0,1]\) let \(t_s\) be the largest \(t\) with \(F(t)\le s\). Then \(\{F\le s\}=[0,t_s]\), and \(F(t_s)=s\): this is clear if \(t_s=1\), and otherwise \(F>s\) to the right of \(t_s\), so \(F(t_s)\ge s\) by continuity. Hence \(\nu(\{F\le s\})=s=m([0,s])\). The intervals \([0,s]\) are closed under intersections and generate the Borel sets, so \(\nu(F^{-1}(B))=m(B)\) for every Borel set \(B\), by the [finite-measure uniqueness lemma in the double-commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-18). Consequently \(\int\varphi\circ F\,d\nu=\int\varphi\,dm\) for bounded or nonnegative Borel \(\varphi\), and \(V\) is a well-defined isometry.

*\(V\) is onto.* Let \(q(s)\) be the least \(t\) with \(F(t)\ge s\). It is nondecreasing, hence Borel. For every \(t\), \(q(F(t))\le t\) and \(F(q(F(t)))=F(t)\). If \(q(F(t))<t\), then \(F\) is constant on the nondegenerate interval \([q(F(t)),t]\), and \(t\) is not the left end of the maximal interval of constancy that contains it. The maximal nondegenerate intervals of constancy are disjoint, so there are countably many, and each has \(\nu\)-measure \(0\), because \(\nu\) has no atoms. So \(q\circ F=\mathrm{id}\) \(\nu\)-almost everywhere. For a polynomial \(p\), the function \(p\circ q\) is bounded and Borel, and \(V(p\circ q)=p\) \(\nu\)-almost everywhere. So the range of \(V\) contains the polynomials. These are dense in \(C[0,1]\) and hence in \(L^2([0,1],\nu)\) (Lemma 2.3(3)). The range of an isometry is closed, so \(V\) is onto.

*The algebras.* Clearly \(VM_\varphi=M_{\varphi\circ F}V\) for bounded Borel \(\varphi\). So \(V\{M_\varphi\}V^*\) is a maximal abelian algebra (Theorem 3.1(3)) contained in the abelian algebra \(\{M_f:f\in L^\infty(\nu)\}\). If \(\mathcal A\subseteq\mathcal B\) with \(\mathcal A\) maximal abelian and \(\mathcal B\) abelian, then \(\mathcal B\subseteq\mathcal A'=\mathcal A\). This gives (8.1). \(\square\)

**Theorem 8.4** (Diffuse countably generated algebras). For an abelian von Neumann algebra \(M\) the following are equivalent.

1. \(M\) is isomorphic to \(L^\infty[0,1]\), with Lebesgue measure.
2. \(M\ne0\), and \(M\) is countably generated, \(\sigma\)-finite, and without minimal projections.

In particular, if a nonzero separable Hilbert space carries an abelian von Neumann algebra without minimal projections, that algebra is isomorphic to \(L^\infty[0,1]\). The condition \(M\ne0\) excludes the zero algebra on the zero space, which has the other three properties.


**Proof.** (2)\(\Rightarrow\)(1). *Step 1: a cyclic vector.* Let \(M\) act on \(H\). Choose a maximal family of unit vectors \(\xi_k\) such that the subspaces \([M'\xi_k]\) are pairwise orthogonal. Their projections \(p_k\) lie in \(M''=M\) and are pairwise orthogonal, so they are countably many, listed without repetitions and with finite sums for a finite family, and their sum is \(1\) by maximality. Put \(\xi=\sum_k2^{-k}\xi_k\). Since \(M\) is abelian, \(p_k\in M'\), and \(p_k\xi=2^{-k}\xi_k\); so \([M'\xi]\) contains every \([M'\xi_k]\), and \(\xi\) is cyclic for \(M'\). Hence \(\xi\) separates \(M\). Let \(e\) be the projection onto \([M\xi]\); it lies in \(M'\). The map \(x\mapsto x|_{eH}\) is a \(*\)-isomorphism of \(M\) onto the von Neumann algebra \(M_e=\{x|_{eH}:x\in M\}\) (see [The double commutant theorem](the-double-commutant-theorem.md), Theorem 5.8); it is injective because \(xe\xi=x\xi=0\) forces \(x=0\). The vector \(\xi\) is cyclic for \(M_e\). The algebra \(M_e\) again has the properties in (2). Being \(\sigma\)-finite and having minimal projections are properties defined through projections, so they pass through \(*\)-isomorphisms. By Theorem 8.2, \(M\) is generated by one self-adjoint element \(a\), and \(a|_{eH}\) generates \(M_e\). Indeed, the restriction map is strongly continuous and maps the \(*\)-algebra generated by \(1\) and \(a\) onto the one generated by \(1\) and \(a|_{eH}\); since \(M\) is the strong closure of the former, \(M_e\) lies in the von Neumann algebra generated by \(a|_{eH}\), and the converse inclusion is clear. So we may assume that \(M\) has a cyclic vector \(\xi\) with \(\|\xi\|=1\).

*Step 2: a multiplication algebra.* By Theorem 8.2, \(M\) is generated by a self-adjoint \(a\). \(M\) is not \(\mathbb C1\), since \(1\) would then be a minimal projection. After an affine change we may assume that the spectrum \(\sigma(a)\) lies in \([0,1]\). The continuous functional calculus identifies \(C(\sigma(a))\) with the C\*-algebra generated by \(1\) and \(a\). Let \(\nu\) be the Radon probability measure on \(\sigma(a)\), extended by \(0\) to \([0,1]\), with \(\int g\,d\nu=\langle g(a)\xi,\xi\rangle\). The vector \(\xi\) is cyclic for the C\*-algebra generated by \(1\) and \(a\), because its strong closure is \(M\). Theorem 3.1(2) gives a unitary \(U:L^2([0,1],\nu)\to H\) with \(UM_gU^*=g(a)\) for continuous \(g\). By Theorem 3.1(3), \(U\{M_f:f\in L^\infty(\nu)\}U^*\) is the von Neumann algebra generated by \(a\), which is \(M\).

*Step 3: no atoms.* If \(\nu(\{t\})>0\), then \(M_{1_{\{t\}}}\) is a nonzero projection, and \(M_fM_{1_{\{t\}}}=f(t)M_{1_{\{t\}}}\) for every \(f\). So it is a minimal projection, and so is its image in \(M\), which is excluded.

*Step 4.* By Lemma 8.3, \(M\cong L^\infty([0,1],\nu)\cong L^\infty[0,1]\).

(1)\(\Rightarrow\)(2). The algebra \(L^\infty[0,1]\) on \(L^2[0,1]\) is \(\sigma\)-finite, because \(\sum_jm(E_j)\le1\) for disjoint sets. It has no minimal projection: if \(m(E)>0\), the continuous function \(t\mapsto m(E\cap[0,t])\) takes the value \(\frac12m(E)\), so \(E\) splits into two sets of positive measure. Both properties are defined through projections, so they pass to every algebra \(M\) isomorphic to \(L^\infty[0,1]\). Let \(\theta:L^\infty[0,1]\to M\) be a \(*\)-isomorphism and \(a=\theta(\iota)\), where \(\iota(t)=t\). Let \(N\subseteq M\) be the von Neumann algebra generated by \(a\), and \(B=\theta^{-1}(N)\). Then \(B\) is a C\*-subalgebra of \(L^\infty[0,1]\) that contains \(1\) and \(\iota\), hence all continuous functions. Whenever an increasing net in \(B_h\) is bounded in norm, its least upper bound lies in \(B\): the image net in \(N\) converges strongly to an element of \(N\), and by Proposition 7.3 its preimage is the least upper bound in \(L^\infty[0,1]\). Let \(\mathcal S\) be the family of Borel sets \(E\) with \(1_E\in B\). For open \(U\ne[0,1]\) the functions \(g_n(t)=\min\{1,n\operatorname{dist}(t,[0,1]\setminus U)\}\) are continuous and increase to \(1_U\), and \(M_{g_n}\to M_{1_U}\) strongly by dominated convergence, so \(U\in\mathcal S\); and \([0,1]\in\mathcal S\) because \(1\in B\). The family \(\mathcal S\) is closed under complements (\(1-1_E\)), finite intersections (products) and increasing countable unions (least upper bounds), so it is a \(\sigma\)-algebra containing the open sets, and it contains every Borel set. Then \(B\) contains all simple Borel functions and, being norm closed, all of \(L^\infty[0,1]\). So \(N=M\), and \(M\) is generated by \(a\).

The last statement follows from Theorem 8.2 and the fact that von Neumann algebras acting on separable Hilbert spaces are \(\sigma\)-finite: an uncountable family of pairwise orthogonal nonzero projections would give an uncountable orthonormal family of vectors. \(\square\)

**Example 8.5** (Each hypothesis is needed).

(a) *\(\sigma\)-finiteness.* Let \(M=\prod_{t\in[0,1]}L^\infty[0,1]\), acting on the Hilbert sum \(\bigoplus_{t\in[0,1]}L^2[0,1]\) by \((f_t)_t\mapsto\bigoplus_tM_{f_t}\). It is a von Neumann algebra, because each summand is maximal abelian and the commutant of a direct sum is the direct sum of the commutants ([The double commutant theorem](the-double-commutant-theorem.md), Proposition 5.2). It has no minimal projection: a nonzero projection of \(M\) has a coordinate \(1_E\) with \(m(E)>0\), and \(E\) splits into two sets of positive measure, as in the proof of Theorem 8.4. It is not \(\sigma\)-finite: the projections onto the summands are uncountably many. It is countably generated. Let \(a\) act as the scalar \(t\) on the summand with index \(t\), and \(b\) as \(M_\iota\) on every summand. An operator commuting with \(a\) maps each eigenspace \(\ker(a-t)\), which is the summand with index \(t\), into itself, so the projections onto the summands lie in the von Neumann algebra generated by \(a\). An operator commuting with \(a\) and \(b\) is therefore a bounded family of operators that commute with \(M_\iota\), hence of multiplication operators (Theorem 3.1(3)). So the commutant of \(\{a,b\}\) is \(M\), and \(\{a,b\}''=M'=M\). So \(M\) is not isomorphic to \(L^\infty[0,1]\).

(b) *Countable generation.* Let \(J\) be uncountable, \(P\) the product of the fair coin measures on \(\{0,1\}^J\), defined on the product \(\sigma\)-algebra, and \(M=L^\infty(P)\) on \(L^2(P)\). By Remark 3.2 it is maximal abelian, and \(1\) is a cyclic vector because \(L^\infty(P)\) is dense in \(L^2(P)\); so it is \(\sigma\)-finite (Theorem 7.4(2)). It has no minimal projection. Every measurable set \(E\) depends only on the coordinates in some countable set \(J_E\), because the sets with this property form a \(\sigma\)-algebra containing the cylinder sets. For \(j\notin J_E\), independence of the coordinates gives \(P(E\cap\{\gamma_j=0\})=\frac12P(E)\), which splits \(E\). Finally, \(M\) is not countably generated. Otherwise \(M\) is generated by one self-adjoint \(a\) (Theorem 8.2), and \(L^2(P)=[M1]\) is the closure of the set of vectors \(p(a)1\), with \(p\) a polynomial whose coefficients have rational real and imaginary parts; so \(L^2(P)\) would be separable. But it is not ([The double commutant theorem](the-double-commutant-theorem.md), Exercise 9.9).

(c) *No minimal projections.* \(\ell^\infty(\mathbb N)\) is countably generated and \(\sigma\)-finite, but each point gives a minimal projection.

## D. Find the limits of the measure picture

An algebra can have every bounded increasing supremum and still fail to be a von Neumann algebra. To see the obstruction rather than just its name, partition a stonean spectrum by where normal measures can live, then build the other regions using Borel functions modulo meager functions. Here the negligible sets come from category, not from a fixed measure. The quotient remains a C*-algebra and is order complete, but its normal observations can all vanish.

This construction also makes the three-region decomposition useful: it predicts precisely which part an example realizes. The final extension theorem asks a different question—when continuous functions defined on a closed subspace can be extended by a positive norm-one operator—and identifies stonean spaces through that property.

### The three clopen regions of a stonean space

**Theorem 6.4** (Decomposition of a stonean space). Let \(\Omega\) be stonean. There is exactly one partition of \(\Omega\) into three clopen sets \(\Omega_1\), \(\Omega_2\), \(\Omega_3\) with the following properties.

1. \(\Omega_1\) is hyperstonean.
2. \(\Omega_2\) contains a dense meager subset.
3. Every meager subset of \(\Omega_3\) is rare, and every Radon measure on \(\Omega_3\) is concentrated on a closed rare subset of \(\Omega_3\).

Moreover, \(\Omega_1\) is the closure of the union of all supports of normal measures on \(\Omega\), and \(\Omega_2\cup\Omega_3\) carries no normal measure other than \(0\). Any of the three parts may be empty; Section 9 gives stonean spaces with \(\Omega=\Omega_2\) and with \(\Omega=\Omega_3\).

**Proof.** We use two facts about a clopen set \(C\). A subset of \(C\) is rare in \(C\) exactly when it is rare in \(\Omega\), because closures in \(C\) are closures in \(\Omega\) and \(C\) is open. Consequently the normal measures on \(C\) are the normal measures on \(\Omega\) that vanish outside \(C\), and the restriction \(\mu(\,\cdot\cap C)\) of a normal measure to \(C\) is normal.

*The first part.* Let \(F\) be the union of all supports of normal measures on \(\Omega\). The supports are clopen (Corollary 5.4(3)), so \(F\) is open, and \(\Omega_1=\overline F\) is clopen. The normal measures on \(\Omega_1\) have supports whose union \(F\) is dense in \(\Omega_1\), so \(\Omega_1\) is hyperstonean by Lemma 6.2.

*The second part.* Call a nonempty open set \(U\) *thin* if it contains a meager subset that is dense in \(U\). By Zorn's lemma there is a maximal family \((G_j)_{j\in J}\) of pairwise disjoint thin sets. Let \(G=\bigcup_jG_j\) and \(\Omega_2=\overline G\), a clopen set. For each \(j\) choose a meager \(M_j\subseteq G_j\) that is dense in \(G_j\). By Lemma 2.1(3) the union \(\bigcup_jM_j\) is meager, and it is dense in \(\Omega_2\).

*The first two parts are disjoint.* Let \(\mu\) be normal and suppose \(W=G_j\cap\operatorname{supp}\mu\) is not empty. Then \(M_j\cap W\) is dense in the open set \(W\) and meager, hence null, and by Corollary 5.4(1) its closure is null. This closure contains \(W\), a nonempty open subset of the support, which is impossible. So \(F\cap G=\varnothing\). Since \(F\) is open, \(F\cap\overline G=\varnothing\), and since \(\overline G\) is open, \(\overline F\cap\overline G=\varnothing\).

*The third part.* Put \(\Omega_3=\Omega\setminus(\Omega_1\cup\Omega_2)\), a clopen set. Let \(M\subseteq\Omega_3\) be meager, and suppose that \(\overline M\) has a nonempty interior \(U\). Then \(U\subseteq\Omega_3\), and \(M\cap U\) is a meager subset dense in \(U\), so \(U\) is thin and disjoint from every \(G_j\). This contradicts maximality, so \(M\) is rare. A normal measure is supported in \(\Omega_1\), so \(\Omega_2\cup\Omega_3\) carries no normal measure other than \(0\). Let \(\mu\) be a Radon measure on \(\Omega_3\), extended by \(0\) to \(\Omega\). In the decomposition of Theorem 5.6 the normal part is supported in \(\Omega_1\cap\Omega_3=\varnothing\), so \(\mu\) is concentrated on a meager set \(M\), which we may take inside \(\Omega_3\). Then \(M\) is rare, and \(\mu\) is concentrated on the closed rare set \(\overline M\).

*Uniqueness.* Let \(\Omega_1',\Omega_2',\Omega_3'\) be another clopen partition with properties 1–3. A normal measure on \(\Omega_1'\) is a normal measure on \(\Omega\), so its support lies in \(F\); as \(\Omega_1'\) is hyperstonean, these supports are dense in \(\Omega_1'\), and \(\Omega_1'\subseteq\overline F=\Omega_1\). If the open set \(W=\Omega_2'\setminus\Omega_2\) were not empty, it would be thin, because the dense meager subset of \(\Omega_2'\) meets it in a dense meager subset; and it would be disjoint from \(G\), against maximality. So \(\Omega_2'\subseteq\Omega_2\). If \(W=\Omega_1\cap\Omega_3'\) were not empty, some normal measure would give \(W\) positive measure, since \(\Omega_1\) is hyperstonean; its restriction to \(W\) would be a nonzero normal measure concentrated on the rare set of property 3, which is impossible. If \(W=\Omega_2\cap\Omega_3'\) were not empty, the dense meager subset of \(\Omega_2\) would meet \(W\) in a meager set dense in \(W\); by property 3 this set is rare, and a rare set is dense in no nonempty open set. So \(\Omega_3'\subseteq\Omega_3\). Since both triples are partitions of \(\Omega\), the three inclusions are equalities. \(\square\)

In particular, three conditions on a stonean space are equivalent: it has no nonempty clopen subset that is hyperstonean; \(\Omega_1=\varnothing\); it carries no normal measure other than \(0\). Indeed, \(\Omega_1\) is itself a clopen hyperstonean set; a nonempty clopen hyperstonean set carries a nonzero normal measure, which is also normal on the whole space; and the support of a nonzero normal measure is a nonempty clopen set that is hyperstonean by Lemma 6.2. When the three conditions hold, Corollary 5.7 shows that every Radon measure on the space is concentrated on a meager set.

### 9. Borel functions modulo meager functions

This section builds stonean spaces that carry no normal measure: one kind for the part \(\Omega_2\) and one for the part \(\Omega_3\) of Theorem 6.4. The construction goes back to Dixmier (1951); see [Blackadar, III.1.8.3].

Let \(\Gamma\) be a topological space. No separation axiom is needed for the construction, for Lemmas 9.1 and 9.2 or for Theorem 9.3; Theorems 9.5 and 9.6 say which ones they use. Let \(\mathcal B(\Gamma)\) be the C\*-algebra of bounded complex Borel functions on \(\Gamma\), with pointwise operations and the supremum norm. Let \(\mathcal B_0(\Gamma)\) be the set of \(f\in\mathcal B(\Gamma)\) for which \(\{f\ne0\}\) is meager. It is a two-sided ideal, closed under conjugation, and norm closed: a uniform limit of functions \(f_n\in\mathcal B_0(\Gamma)\) vanishes outside the meager set \(\bigcup_n\{f_n\ne0\}\). So
\[
\mathcal D(\Gamma)=\mathcal B(\Gamma)/\mathcal B_0(\Gamma)
\]
is an abelian C\*-algebra with unit. We write \(\tilde f\) for the class of \(f\), and \(\Omega_\Gamma\) for the spectrum of \(\mathcal D(\Gamma)\).

*Order.* For real \(f\in\mathcal B(\Gamma)\), \(\tilde f\ge0\) if and only if \(\{f<0\}\) is meager. Indeed, if \(\{f<0\}\) is meager, then the negative part of \(f\) lies in \(\mathcal B_0(\Gamma)\), and \(\tilde f\) is the square of the class of \(\sqrt{\max(f,0)}\). Conversely, if \(\tilde f\ge0\), then \(\tilde f=\tilde g^*\tilde g\) for some \(g\), so \(f-|g|^2\in\mathcal B_0(\Gamma)\), and \(f\ge0\) outside a meager set. The self-adjoint elements are the classes of real functions, and the class of \(\max(f,g)\) is the supremum of \(\tilde f\) and \(\tilde g\) in the order.

**Lemma 9.1** (The Baire property). Every bounded real Borel function on \(\Gamma\) agrees outside a meager set with a bounded lsc function, and also with a bounded usc function. In particular, for every Borel set \(E\) there is an open set \(U\) such that the symmetric difference \(E\triangle U\) is meager.

**Proof.** Let \(\mathcal K\) be the set of bounded real functions on \(\Gamma\) that agree outside a meager set with a bounded lsc function.

*Step 1.* \(\mathcal K\) contains the bounded lsc functions, trivially, and the bounded usc functions: a bounded usc \(f\) agrees with the lsc function \(f_*\) outside a meager set, by Lemma 2.2(2).

*Step 2.* \(\mathcal K\) is a real vector space, closed under \(\max\) and \(\min\), and contains the constants. Sums, positive multiples, maxima and minima of lsc functions are lsc, and a countable union of meager sets is meager. If \(f\) agrees with an lsc \(g\) outside a meager set, then \(-f\) agrees with the usc function \(-g\), hence with a bounded lsc function, outside a meager set.

*Step 3.* \(\mathcal K\) is closed under pointwise limits of uniformly bounded sequences. Let \(f_k\in\mathcal K\), \(|f_k|\le c\), and \(f_k\to f\) pointwise. For \(n<m\) put \(h_{n,m}=\max(f_{n+1},\dots,f_m)\in\mathcal K\), and choose an lsc \(g_{n,m}\) with values in \([-c,c]\) that agrees with \(h_{n,m}\) outside a meager set \(M_{n,m}\); truncating an lsc function at \(\pm c\) keeps it lsc. The function \(g_n=\sup_mg_{n,m}\) is lsc, and outside the meager set \(M_n=\bigcup_mM_{n,m}\) it equals \(H_n=\sup_{k>n}f_k\). By Lemma 2.2(2), \(g_n\) agrees with its upper regularization \(u_n=(g_n)^*\) outside a meager set \(M_n'\). Put \(v_n=\min(u_1,\dots,u_n)\), a usc function. Outside the meager set \(M^\sharp=\bigcup_n(M_n\cup M_n')\) we have \(v_n=\min(H_1,\dots,H_n)=H_n\), because \(H_n\) decreases in \(n\). So \(v=\inf_nv_n\) is usc, and outside \(M^\sharp\) it equals \(\lim_nH_n=\limsup_kf_k=f\). By Step 1, \(v\in\mathcal K\), hence \(f\in\mathcal K\).

*Step 4.* The sets \(E\) with \(1_E\in\mathcal K\) contain the open sets (whose indicators are lsc). They are closed under complements, by Step 2, and under countable unions, since \(1_{E_1\cup\dots\cup E_n}\) is a maximum and increases to \(1_{\bigcup_nE_n}\) (Steps 2 and 3). So they include all Borel sets. Hence \(\mathcal K\) contains the simple Borel functions, and by Step 3 their uniform limits, which are all bounded real Borel functions. The statement about usc functions follows by applying this to \(-f\). Finally, if \(1_E\) agrees with an lsc \(g\) outside a meager set \(M\), then \(U=\{g>\frac12\}\) is open and \(E\triangle U\subseteq M\). \(\square\)

**Lemma 9.2** (Clopen subsets of \(\Omega_\Gamma\)). For a Borel set \(E\subseteq\Gamma\), the class \(\tilde1_E\) is a projection; let \(\widehat E\subseteq\Omega_\Gamma\) be the clopen set on which its Gelfand transform equals \(1\).

1. \(\widehat E=\varnothing\) if and only if \(E\) is meager, and \(\widehat E\subseteq\widehat F\) if and only if \(E\setminus F\) is meager. Moreover \(\widehat{E\cap F}=\widehat E\cap\widehat F\) and \(\widehat{\Gamma\setminus E}=\Omega_\Gamma\setminus\widehat E\).
2. Every clopen subset of \(\Omega_\Gamma\) is \(\widehat U\) for some open set \(U\subseteq\Gamma\).
3. If \(\Gamma\) is a Baire space, then \(\widehat U\ne\varnothing\) for every nonempty open set \(U\).

**Proof.** (1) \(\tilde1_E=0\) means \(1_E\in\mathcal B_0(\Gamma)\). By the description of the order, \(\tilde1_E\le\tilde1_F\) means \(1_E\le1_F\) outside a meager set. The other two statements follow from \(1_{E\cap F}=1_E1_F\) and \(1_{\Gamma\setminus E}=1-1_E\). (2) A clopen set is the set where the transform of a projection \(\tilde p\) equals \(1\), with \(p\) real. Since \(\tilde p^2=\tilde p\), the set \(\{p^2\ne p\}\) is meager, so \(p=1_E\) outside a meager set, with \(E=\{p=1\}\). By Lemma 9.1 there is an open \(U\) with \(E\triangle U\) meager, and then \(\widehat E=\widehat U\). (3) In a Baire space a nonempty open set is not meager. \(\square\)

**Theorem 9.3** (Every stonean space is a space of this kind).

1. For every topological space \(\Gamma\), the space \(\Omega_\Gamma\) is stonean. More precisely, let \((\tilde f_i)\) be an increasing net in \(\mathcal D(\Gamma)_h\) that is bounded in norm, and let the \(f_i\) be lsc representatives with a common bound. Then the supremum of \((\tilde f_i)\) in \(\mathcal D(\Gamma)_h\) is the class of the pointwise supremum \(\sup_if_i\).
2. If \(\Omega\) is stonean, then \(x\mapsto\tilde x\) is a \(*\)-isomorphism of \(C(\Omega)\) onto \(\mathcal D(\Omega)\). So every stonean space \(\Omega\) is homeomorphic to \(\Omega_\Omega\).

**Proof.** (1) Take an increasing net \((\tilde f_i)\) in \(\mathcal D(\Gamma)_h\) that is bounded in norm. By Lemma 9.1 and truncation we may choose lsc representatives \(f_i\) with \(|f_i|\le c\). Put \(f=\sup_if_i\), a bounded lsc function. Since \(f\ge f_i\), \(\tilde f\) is an upper bound. Let \(\tilde g\) be another upper bound, with \(g\) a bounded usc representative (Lemma 9.1). For each \(i\), \(f_i\le g\) outside a meager set. The set \(A=\{f>g\}\) is open, since \(f-g\) is lsc. By Zorn's lemma choose a maximal family \((G_j)\) of pairwise disjoint nonempty open sets such that each \(G_j\cap A\) is meager, and put \(G=\bigcup_jG_j\).

We claim that \(G\) is dense. If not, \(V=\Gamma\setminus\overline G\) is a nonempty open set. If \(V\cap A=\varnothing\), then \(V\) could be added to the family. Otherwise pick \(\gamma\in V\cap A\). Then \(f(\gamma)>g(\gamma)\), so \(f_i(\gamma)>g(\gamma)\) for some \(i\). The set \(W=V\cap\{f_i>g\}\) is open, because \(f_i-g\) is lsc, and it contains \(\gamma\). It is meager, since \(f_i\le g\) outside a meager set. So \(W\cap A\) is meager, and \(W\) could be added to the family. Both cases contradict maximality.

So \(\Gamma\setminus G\) is closed with empty interior, that is, rare. By Lemma 2.1(3), \(\bigcup_j(G_j\cap A)\) is meager. Hence \(A=\bigcup_j(G_j\cap A)\cup(A\setminus G)\) is meager, which means \(\tilde f\le\tilde g\). So \(\tilde f\) is the least upper bound. For a nonempty set \(S\subseteq\mathcal D(\Gamma)_h\) that is bounded above, the classes of maxima of finitely many representatives form a bounded increasing net with the same upper bounds, as in the proof of Theorem 7.1. So \(\mathcal D(\Gamma)_h\) is conditionally complete. Through the Gelfand isomorphism, which preserves order, so is \(C_{\mathbb R}(\Omega_\Gamma)\), and \(\Omega_\Gamma\) is stonean by Theorem 4.3.

(2) The map is a \(*\)-homomorphism. It is injective: if \(x\) is continuous and \(\{x\ne0\}\) is meager, this open set is empty by Lemma 2.1(2). It is onto: a bounded real Borel function agrees outside a meager set with an lsc function (Lemma 9.1), which agrees outside a meager set with a continuous function (Theorem 4.3). Isomorphic commutative C\*-algebras have homeomorphic spectra. \(\square\)

**Remark 9.4.** If \(\Gamma\) is a Baire space, the proof of Theorem 9.3(1) shows more: the set \(A\) is empty. Indeed, if \(\gamma\in A\), then the nonempty open set \(\{f_i>g\}\) is meager for a suitable \(i\), which is impossible in a Baire space. So then \(f\le g\) everywhere.

**Theorem 9.5** (A stonean space with a dense meager subset). Let \(\Gamma\) be a regular Baire space that contains a dense meager subset; here *regular* means that a point and a closed set not containing it have disjoint open neighbourhoods. Then \(\Omega_\Gamma\) contains a dense meager subset. So \(\Omega_\Gamma\) is its own second part in Theorem 6.4, and it carries no normal measure other than \(0\). If moreover \(\Gamma\) is Hausdorff, has no isolated points and has a countable family of nonempty open sets such that every nonempty open set contains one of them, then \(\Omega_\Gamma\) has no isolated points and has a countable dense subset. All of this applies to \(\Gamma=[0,1]\).

**Proof.** Let \(A=\bigcup_nA_n\) be dense, with each \(A_n\) rare. Replacing \(A_n\) by its closure, we may assume that each \(A_n\) is closed. For each \(n\) let \(B_n\) be the intersection of the sets \(\widehat U\) over all open \(U\supseteq A_n\). It is closed.

*Each \(B_n\) is rare.* Suppose \(B_n\) contains a nonempty open set. Then it contains a nonempty clopen set, of the form \(\widehat V\) with \(V\) open and not meager (Lemma 9.2). For every open \(U\supseteq A_n\), \(\widehat V\subseteq\widehat U\), so \(V\setminus U\) is meager. The open set \(V\setminus A_n\) is not meager, because \(V\) is not and \(A_n\) is rare; so it contains a point \(\gamma\). As \(\Gamma\) is regular and \(A_n\) is closed, there are disjoint open sets \(P\ni\gamma\) and \(U\supseteq A_n\). The set \(V\cap P\) is open and nonempty, hence not meager, because \(\Gamma\) is a Baire space. But \(V\cap P\subseteq V\setminus U\), which is meager. This is a contradiction.

*The union \(B=\bigcup_nB_n\) is dense.* Suppose a nonempty clopen set \(\widehat V\), with \(V\) open and not meager, misses every \(B_n\). The open sets \(U\supseteq A_n\) are closed under finite intersections, and so are the sets \(\widehat U\) (Lemma 9.2(1)). The compact set \(\widehat V\) misses their intersection \(B_n\), so it misses one of them: there is an open \(U_n\supseteq A_n\) with \(\widehat V\cap\widehat{U_n}=\varnothing\), that is, \(V\cap U_n\) is meager. The open set \(U=\bigcup_nU_n\) contains \(A\), so it is dense, and \(V\cap U=\bigcup_n(V\cap U_n)\) is meager. But \(V\cap U\) is a nonempty open set, because \(V\) is open and nonempty and \(U\) is dense. This contradicts the Baire property of \(\Gamma\).

So \(B\) is a dense meager subset of \(\Omega_\Gamma\). A normal measure vanishes on \(B\) (Theorem 5.2), hence on \(\overline B=\Omega_\Gamma\) (Corollary 5.4(1)).

*Separability.* Let \((V_n)\) be the countable family, and choose \(\omega_n\in\widehat{V_n}\), which is not empty by Lemma 9.2(3). A nonempty clopen subset of \(\Omega_\Gamma\) is \(\widehat U\) with \(U\) open and not meager, and \(U\) contains some \(V_n\); so \(\omega_n\in\widehat{V_n}\subseteq\widehat U\). So \(\{\omega_n\}\) is dense. If \(\{\omega\}\) were open, it would be clopen, say \(\{\omega\}=\widehat U\) with \(U\) nonempty and open. Since \(\Gamma\) is Hausdorff without isolated points, \(U\) contains two disjoint nonempty open sets \(U_1,U_2\), and \(\widehat{U_1}\), \(\widehat{U_2}\) would be disjoint nonempty subsets of \(\{\omega\}\).

For \(\Gamma=[0,1]\): it is a compact metric space, hence regular, Hausdorff and a Baire space; the rational points form a dense meager set; the open intervals with rational end points form the countable family; and there are no isolated points. \(\square\)

So \(C(\Omega_{[0,1]})\cong\mathcal D([0,1])\) is an abelian C\*-algebra in which every nonempty bounded set of self-adjoint elements has a least upper bound, but which is isomorphic to no von Neumann algebra.

**Theorem 9.6** (Stonean spaces on which every measure lives on a rare set). Let \(\Gamma\) be a topological space with a base \(\mathfrak B\) of nonempty open sets such that

\((\ast)\) for every decreasing sequence \(B_1\supseteq B_2\supseteq\cdots\) in \(\mathfrak B\), the intersection \(\bigcap_nB_n\) contains a member of \(\mathfrak B\).

1. If \(G_1,G_2,\dots\) are dense open subsets of \(\Gamma\), the interior of \(\bigcap_nG_n\) is dense. So \(\Gamma\) is a Baire space, and every meager subset of \(\Gamma\) is rare.
2. The sets \(\widehat B\), \(B\in\mathfrak B\), are nonempty clopen sets, and every nonempty open subset of \(\Omega_\Gamma\) contains one of them. Every nonempty clopen subset of \(\widehat B\) contains \(\widehat C\) for some \(C\in\mathfrak B\) with \(C\subseteq B\). For every decreasing sequence \(B_1\supseteq B_2\supseteq\cdots\) in \(\mathfrak B\) there is \(C\in\mathfrak B\) with \(\widehat C\subseteq\bigcap_n\widehat{B_n}\).
3. Every meager subset of \(\Omega_\Gamma\) is rare.
4. If \(\Gamma\) is Hausdorff and has no isolated points, every nonempty clopen subset of \(\Omega_\Gamma\) is uncountable, and every Radon measure on \(\Omega_\Gamma\) has a rare support.

If \(\Gamma\) is a nonempty Hausdorff space without isolated points, \(\Omega_\Gamma\) is a nonempty stonean space that is its own third part in Theorem 6.4.

Example 9.8 proves that for the space of Example 9.7 no base of \(\Omega_\Gamma\) satisfies \((\ast)\), so (2) is stated for sequences that decrease in \(\Gamma\).

**Proof.** (1) Let \(V\) be a nonempty open set. Choose \(B_1\in\mathfrak B\) with \(B_1\subseteq V\cap G_1\), then \(B_2\in\mathfrak B\) with \(B_2\subseteq B_1\cap G_2\), and so on; each of these open sets is nonempty because the \(G_n\) are dense. By \((\ast)\), \(\bigcap_nB_n\) contains some \(B\in\mathfrak B\), and \(B\) is an open subset of \(V\cap\bigcap_nG_n\). So the interior of \(\bigcap_nG_n\) meets \(V\). If \(M=\bigcup_nR_n\) is meager, the sets \(G_n=\Gamma\setminus\overline{R_n}\) are dense and open, and \(M\) lies in the complement of the interior of \(\bigcap_nG_n\), a closed set with empty interior. So \(M\) is rare, and in particular has empty interior.

(2) By (1) and Lemma 9.2(3), \(\widehat B\ne\varnothing\). A nonempty open subset of \(\Omega_\Gamma\) contains a nonempty clopen set, which is \(\widehat E\) for an open \(E\) that is not meager (Lemma 9.2); \(E\) contains some \(B\in\mathfrak B\), and \(\widehat B\subseteq\widehat E\). If a nonempty clopen set \(\widehat E\), with \(E\) open, lies in \(\widehat B\), then \(E\setminus B\) is meager. So \(E\cap B\) is not meager, hence not empty, and it contains some \(C\in\mathfrak B\); then \(C\subseteq B\) and \(\widehat C\subseteq\widehat E\). Finally, if \(B_1\supseteq B_2\supseteq\cdots\), then \((\ast)\) gives \(C\in\mathfrak B\) with \(C\subseteq B_n\), hence \(\widehat C\subseteq\widehat{B_n}\), for all \(n\).

(3) Let \(R_1,R_2,\dots\) be rare subsets of \(\Omega_\Gamma\) and \(W\) a nonempty open set. The open set \(W\setminus\overline{R_1}\) is not empty, so by (2) it contains \(\widehat{B_1}\) for some \(B_1\in\mathfrak B\). The open set \(\widehat{B_1}\setminus\overline{R_2}\) is not empty and contains a nonempty clopen set; by (2) this contains \(\widehat{B_2}\) with \(B_2\in\mathfrak B\) and \(B_2\subseteq B_1\). Continuing, we get \(B_1\supseteq B_2\supseteq\cdots\) in \(\mathfrak B\) with \(\widehat{B_n}\cap R_n=\varnothing\). By (2) some nonempty \(\widehat C\) lies in every \(\widehat{B_n}\). It is an open subset of \(W\) that misses \(\bigcup_nR_n\). So \(\bigcup_nR_n\) is dense in no nonempty open set, that is, it is rare.

(4) Let \(W\) be a nonempty clopen subset of \(\Omega_\Gamma\). It contains some \(\widehat B\). The open set \(B\) contains two disjoint nonempty open sets, since \(\Gamma\) is Hausdorff and has no isolated points, and they give two disjoint nonempty clopen subsets of \(\widehat B\) (Lemma 9.2). So no clopen set is a single point; since the clopen sets form a base, \(W\) has no isolated points. A compact space without isolated points is uncountable: if it were countable, it would be a countable union of rare singletons, against Lemma 2.1(2).

Now let \(\mu\) be a Radon measure on \(\Omega_\Gamma\). Only countably many points have positive measure, so every nonempty clopen set contains a point \(\omega\) with \(\mu(\{\omega\})=0\). By outer regularity and Lemma 4.2(3), such a point has clopen neighbourhoods of arbitrarily small measure. Start from a nonempty clopen \(W\), and choose \(B_1\in\mathfrak B\) with \(\widehat{B_1}\subseteq W\). Given \(B_n\), choose \(\omega\in\widehat{B_n}\) with \(\mu(\{\omega\})=0\), a clopen neighbourhood \(Q\subseteq\widehat{B_n}\) of \(\omega\) with \(\mu(Q)<1/(n+1)\), and, by (2), \(B_{n+1}\in\mathfrak B\) with \(B_{n+1}\subseteq B_n\) and \(\widehat{B_{n+1}}\subseteq Q\). By (2) again some nonempty \(\widehat C\) lies in all \(\widehat{B_n}\), so \(\mu(\widehat C)=0\). Thus every nonempty clopen set contains a nonempty open null set. If the support \(S\) of \(\mu\) had interior points, its interior would contain a nonempty clopen set, and hence a nonempty open null set, which is impossible inside the support. So \(S\) is rare.

The final statement: \(\Omega_\Gamma\) is not empty, because \(\Gamma\) is a nonempty Baire space and so is not meager in itself (Lemma 9.2(1)). By (3), no meager set is dense in a nonempty open set, so the second part is empty. The support of a nonzero normal measure is a nonempty clopen set (Corollary 5.4(3)), which is not rare; by (4) there is no such measure, so the first part is empty. \(\square\)

**Example 9.7** (A space satisfying \((\ast)\)). Let \(I\) be an uncountable set and \(\Gamma=\{0,1\}^I\). For a countable set \(J\subseteq I\) and \(\alpha\in\{0,1\}^J\) put \(U(J,\alpha)=\{\gamma\in\Gamma:\gamma_j=\alpha_j\text{ for all }j\in J\}\). The intersection of two such sets is empty or again of this form, so they form a base \(\mathfrak B\) of a topology. Two different points differ at some coordinate \(i\), and the sets \(U(\{i\},\cdot)\) through them are disjoint; so \(\Gamma\) is Hausdorff. Each \(U(J,\alpha)\) is also closed, since its complement is the union of the sets \(U(\{j\},1-\alpha_j)\), \(j\in J\). So \(\Gamma\) has a base of clopen sets, and it is completely regular, because the indicators of these sets are continuous. No point is isolated, because a basic set fixes only countably many of the uncountably many coordinates. If \(U(J_1,\alpha_1)\supseteq U(J_2,\alpha_2)\supseteq\cdots\), then \(J_1\subseteq J_2\subseteq\cdots\) and each \(\alpha_{n+1}\) extends \(\alpha_n\), so the intersection is \(U(\bigcup_nJ_n,\bigcup_n\alpha_n)\), which lies in \(\mathfrak B\). So Theorem 9.6 applies: \(\Omega_\Gamma\) is a stonean space in which every meager set is rare and every Radon measure has a rare support.

**Example 9.8** (No base of \(\Omega_\Gamma\) satisfies \((\ast)\)). Keep \(\Gamma\) of Example 9.7, and choose distinct indices \(j_1,j_2,\dots\) in \(I\). Let \(V_k\) be the set of \(\gamma\) with \(\gamma_{j_1}=\dots=\gamma_{j_{k-1}}=0\) and \(\gamma_{j_k}=1\); these are disjoint basic sets. Put \(R_n=\bigcup_{k\ge n}V_k\). It is the intersection of \(U(\{j_1,\dots,j_{n-1}\},0)\) with the complement of the basic set \(Z=U(\{j_k:k\ge1\},0)\), so it is clopen. The sets \(R_n\) decrease, they are nonempty, and \(\bigcap_nR_n=\varnothing\), because a point of \(R_n\) lies in exactly one \(V_k\), and then \(k\ge n\).

In \(\Omega_\Gamma\) the clopen sets \(\widehat{R_n}\) decrease and are nonempty, by Lemma 9.2(3), since \(\Gamma\) is a Baire space by Theorem 9.6(1). By compactness they have a common point \(\omega\). Their intersection has empty interior. Otherwise it contains a nonempty clopen set \(\widehat E\), with \(E\) not meager, and \(E\setminus R_n\) is meager for every \(n\); then \(E\subseteq\bigcup_n(E\setminus R_n)\cup\bigcap_nR_n\) is meager. Now let \(\mathfrak G\) be any base of \(\Omega_\Gamma\). Choose \(W_1\in\mathfrak G\) with \(\omega\in W_1\subseteq\widehat{R_1}\), and inductively \(W_{n+1}\in\mathfrak G\) with \(\omega\in W_{n+1}\subseteq W_n\cap\widehat{R_{n+1}}\). Then \((W_n)\) decreases in \(\mathfrak G\), and \(\bigcap_nW_n\subseteq\bigcap_n\widehat{R_n}\) has empty interior, so it contains no nonempty member of \(\mathfrak G\). This is why Theorem 9.6(2) speaks of the sets \(\widehat B\), which form a base for the nonempty open sets in the weaker sense that every nonempty open set contains one of them, and of sequences that decrease in \(\Gamma\).

### 11. Stonean spaces and injectivity

A Banach space \(Y\) is *injective* if for every Banach space \(E\), every subspace \(F\subseteq E\) and every bounded linear map \(T:F\to Y\), there is a linear \(\tilde T:E\to Y\) that extends \(T\) with \(\|\tilde T\|=\|T\|\). The scalars are injective by the Hahn–Banach theorem, and so is \(\ell^\infty(X)\), by extending coordinate by coordinate. We show that \(C(\Omega)\) is injective when \(\Omega\) is stonean. The key is a positive projection of \(\ell^\infty(\Omega)\) onto \(C(\Omega)\), obtained from a Hahn–Banach argument with values in the ordered space \(C_{\mathbb R}(\Omega)\).

**Lemma 11.1** (Extending into \(C_{\mathbb R}(\Omega)\)). Let \(\Omega\) be stonean, \(V\) a real vector space, \(W\subseteq V\) a subspace, and \(p:V\to C_{\mathbb R}(\Omega)\) sublinear, that is, \(p(v+w)\le p(v)+p(w)\) and \(p(tv)=tp(v)\) for \(t\ge0\). If \(T_0:W\to C_{\mathbb R}(\Omega)\) is linear and \(T_0\le p\) on \(W\), then \(T_0\) has a linear extension \(T:V\to C_{\mathbb R}(\Omega)\) with \(T\le p\) on \(V\).

**Proof.** *One step.* Let \(v_0\notin W\). For \(w,w'\in W\),
\[
\begin{gathered}
T_0(w)+T_0(w')\\
=T_0(w+w')\\
\le p(w+w')\\
\le p(w-v_0)+p(w'+v_0),
\end{gathered}
\]
so every element of \(L=\{T_0(w)-p(w-v_0):w\in W\}\) lies below every element of \(U=\{p(w'+v_0)-T_0(w'):w'\in W\}\). By Theorem 4.3, \(L\) has a least upper bound \(a\), and \(a\le u\) for every \(u\in U\). Define \(T_1(w+tv_0)=T_0(w)+ta\) on \(W+\mathbb Rv_0\). For \(t>0\), \(a\le p(w/t+v_0)-T_0(w/t)\) gives \(T_1(w+tv_0)\le p(w+tv_0)\). For \(t=-s<0\), \(a\ge T_0(w/s)-p(w/s-v_0)\) gives \(T_1(w-sv_0)\le p(w-sv_0)\). So \(T_1\le p\).

*Zorn.* Order the pairs \((W',T')\), with \(W\subseteq W'\) a subspace and \(T'\) a linear extension of \(T_0\) with \(T'\le p\), by extension. A chain has an upper bound, its union. A maximal pair has \(W'=V\), by the first step. \(\square\)

**Theorem 11.2** (A positive projection onto \(C(\Omega)\), and injectivity). Let \(\Omega\) be stonean. For a bounded real function \(f\) on \(\Omega\) let \(m(f)\) be the supremum in \(C_{\mathbb R}(\Omega)\) of \(\{g\in C_{\mathbb R}(\Omega):g\le f\}\), and \(M(f)\) the infimum there of \(\{g\in C_{\mathbb R}(\Omega):g\ge f\}\); both exist by Theorem 4.3, and \(M(f)=-m(-f)\).

1. \(m(f)\le M(f)\). The map \(m\) is superadditive and \(M\) is subadditive; both are positively homogeneous and equal to the identity on \(C_{\mathbb R}(\Omega)\). Moreover \(m(f)=(f_*)^*\), which agrees with \(f_*\) outside a meager set.
2. There is a linear map \(\varepsilon:\ell^\infty(\Omega)\to C(\Omega)\) such that \(\varepsilon(g)=g\) for \(g\in C(\Omega)\), \(m(f)\le\varepsilon(f)\le M(f)\) for real \(f\), \(\varepsilon(f)\ge0\) for \(f\ge0\), \(\|\varepsilon\|\leq1\), with equality when \(\Omega\ne\varnothing\), and \(\varepsilon(gf)=g\,\varepsilon(f)\) for \(g\in C(\Omega)\) and \(f\in\ell^\infty(\Omega)\).
3. \(C(\Omega)\) is injective: for every complex Banach space \(E\), every subspace \(F\subseteq E\) and every bounded linear \(T:F\to C(\Omega)\) there is a linear \(\tilde T:E\to C(\Omega)\) extending \(T\) with \(\|\tilde T\|=\|T\|\).

The real and complex cases are both proved below. No converse is used in the subsequent arguments.

**Proof.** (1) If \(g\le f\le h\) with \(g,h\) continuous, then \(g\le h\); so \(m(f)\le h\) for every such \(h\), and \(m(f)\le M(f)\). For continuous \(g_1\le f_1\) and \(g_2\le f_2\), \(g_1+g_2\le m(f_1+f_2)\). Taking the least upper bound over \(g_1\) gives \(m(f_1)\le m(f_1+f_2)-g_2\), and then over \(g_2\) gives \(m(f_1)+m(f_2)\le m(f_1+f_2)\). Homogeneity and \(m(g)=g\) for continuous \(g\) are clear, and the statements on \(M\) follow from \(M(f)=-m(-f)\). A continuous \(g\) satisfies \(g\le f\) exactly when \(g\le f_*\) (Lemma 2.2(1)). The pointwise supremum of these \(g\) is \(f_*\). Indeed, the constant \(-\|f\|\) is one of them, and given \(\omega\) and \(t\) with \(-\|f\|<t<f_*(\omega)\), Urysohn's lemma gives \(u\in C(\Omega)\) with \(0\le u\le1\), \(u(\omega)=1\) and \(u=0\) outside the open set \(\{f_*>t\}\), and \(g=-\|f\|+(t+\|f\|)u\) satisfies \(g\le f_*\) and \(g(\omega)=t\). By Theorem 4.3, \(m(f)=(f_*)^*\), and Lemma 2.2(2) gives the last claim.

(2) Apply Lemma 11.1 to the real bounded functions \(V\), the subspace \(W=C_{\mathbb R}(\Omega)\), \(p=M\) and \(T_0=\mathrm{id}\); \(M\) is sublinear by (1), and \(T_0\le M\) on \(W\). We get a linear \(\varepsilon_{\mathbb R}\le M\) that is the identity on \(C_{\mathbb R}(\Omega)\). Then \(\varepsilon_{\mathbb R}(f)=-\varepsilon_{\mathbb R}(-f)\ge-M(-f)=m(f)\). If \(f\ge0\), then \(0\) is a continuous minorant, so \(\varepsilon_{\mathbb R}(f)\ge m(f)\ge0\). Put \(\varepsilon(f_1+if_2)=\varepsilon_{\mathbb R}(f_1)+i\varepsilon_{\mathbb R}(f_2)\) for real \(f_1,f_2\); this is complex linear.

*Norm.* If \(\Omega=\varnothing\), both function spaces and the projection are zero, and \(\|\varepsilon\|=0\). Otherwise, for \(\omega\in\Omega\), \(\varphi(f)=\varepsilon(f)(\omega)\) is a positive linear functional on \(\ell^\infty(\Omega)\) with \(\varphi(1)=1\). It is real on real functions, so \((f,h)\mapsto\varphi(\bar hf)\) is a positive hermitian form, and the [positive-form Cauchy–Schwarz proof](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-01) gives \(|\varphi(f)|^2\le\varphi(|f|^2)\varphi(1)\le\|f\|^2\). So \(\|\varepsilon(f)\|\le\|f\|\), and \(\|\varepsilon\|=1\) since \(\varepsilon(1)=1\).

*Module property.* Let \(C\) be clopen and \(0\le f\le1\). Then \(0\le\varepsilon(1_Cf)\le\varepsilon(1_C)=1_C\), so \(\varepsilon(1_Cf)\) vanishes outside \(C\), that is, \(\varepsilon(1_Cf)=1_C\varepsilon(1_Cf)\). In the same way \(\varepsilon((1-1_C)f)=(1-1_C)\varepsilon((1-1_C)f)\). Adding, \(\varepsilon(f)=1_C\varepsilon(1_Cf)+(1-1_C)\varepsilon((1-1_C)f)\), and multiplying by \(1_C\) gives \(1_C\varepsilon(f)=\varepsilon(1_Cf)\). Every \(f\in\ell^\infty(\Omega)\) is a linear combination of four functions with values in \([0,1]\), so \(\varepsilon(gf)=g\varepsilon(f)\) whenever \(g\) is a linear combination of indicators of clopen sets. These combinations form a unital self-adjoint subalgebra of \(C(\Omega)\) that separates points (Lemma 4.2(3)), hence a dense one (Stone–Weierstrass). By continuity the identity holds for all \(g\in C(\Omega)\).

(3) For each \(\omega\in\Omega\), \(x\mapsto T(x)(\omega)\) is a linear functional on \(F\) of norm at most \(\|T\|\). By [the complex Hahn–Banach extension theorem, Corollary 2.3 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-02) it has an extension to \(E\) of the same norm; call its value at \(x\in E\) \(T'(x)(\omega)\). This defines a linear map \(T':E\to\ell^\infty(\Omega)\) that extends \(T\), with \(\|T'\|\le\|T\|\). Put \(\tilde T=\varepsilon\circ T'\). It takes values in \(C(\Omega)\), it extends \(T\) because \(\varepsilon\) is the identity on \(C(\Omega)\), and \(\|\tilde T\|\le\|\varepsilon\|\|T'\|\le\|T\|\). The reverse inequality holds for every extension. \(\square\)

**Example 11.3** (The map \(m\) is not additive). Let \(\Omega=\Omega_{[0,1]}\), the stonean space of Theorem 9.5. It has a countable dense subset \(D\) and no isolated points. Each point of \(D\) is a rare set, so \(D\) is meager and \(\Omega\setminus D\) is dense (Lemma 2.1(2)). A continuous \(g\le1_D\) satisfies \(g\le0\) on the dense set \(\Omega\setminus D\), hence everywhere; so \(m(1_D)=0\). In the same way \(m(1_{\Omega\setminus D})=0\), because \(D\) is dense. But \(m(1_D+1_{\Omega\setminus D})=m(1)=1\). So \(m\) is not additive, and the linear projection \(\varepsilon\) of Theorem 11.2 cannot be taken to be \(m\). For this \(\varepsilon\), \(\varepsilon(1_D)+\varepsilon(1_{\Omega\setminus D})=1\), so at least one of the two values differs from the value of \(m\).

Example 11.3 proves that \(m\) need not be linear; the linear projection \(\varepsilon\) therefore comes from Lemma 11.1.

## 12. Exercises

**Exercise 12.1** (medium; No convergent sequences). Let \(X\) be an extremally disconnected Hausdorff space.

(a) Show that every convergent sequence in \(X\) is eventually constant.

(b) Deduce that an infinite stonean space is not metrizable, and that an abelian von Neumann algebra of infinite dimension is never norm separable.

*Solution.* (a) Let \(x_n\to x\), and suppose the sequence is not eventually constant. Infinitely many terms differ from \(x\), and a value \(y\ne x\) occurs only finitely often, since a constant subsequence equal to \(y\) cannot converge to \(x\) in a Hausdorff space. So, passing to a subsequence, we may assume that the \(x_n\) are distinct and different from \(x\). Put \(n_1=1\) and choose disjoint open sets \(U_1\ni x_{n_1}\) and \(O_1\ni x\). Since \(x_n\to x\), some \(n_2>n_1\) has \(x_{n_2}\in O_1\). Separate \(x_{n_2}\) from \(x\) by disjoint open sets and intersect them with \(O_1\); this gives disjoint open sets \(U_2\ni x_{n_2}\) and \(O_2\ni x\) inside \(O_1\). Continuing, we get open sets \(U_k\ni x_{n_k}\) and \(O_k\ni x\) with \(U_{k+1}\cup O_{k+1}\subseteq O_k\) and \(U_k\cap O_k=\varnothing\). The \(U_k\) are pairwise disjoint: for \(j<k\), \(U_k\subseteq O_j\), which misses \(U_j\). Put \(U=\bigcup_kU_{2k}\) and \(V=\bigcup_kU_{2k+1}\). These are disjoint open sets, and \(x\) lies in the closure of both, because \(x_{n_{2k}}\to x\) and \(x_{n_{2k+1}}\to x\). This contradicts Lemma 4.2(1).

(b) An infinite compact metric space contains a sequence of distinct points, and by compactness this sequence has a convergent subsequence, which is not eventually constant. So an infinite stonean space is not metrizable, by (a). Take an abelian von Neumann algebra \(M\) of infinite dimension, and let \(\Omega\) be its spectrum. If \(\Omega\) were finite, \(M\cong C(\Omega)\) would have dimension equal to the number of points. So \(\Omega\) is infinite, and it is stonean (Theorem 7.1). If \(C(\Omega)\) had a dense sequence \((x_n)\) in its unit ball, then \(d(\omega,\omega')=\sum_n2^{-n}|x_n(\omega)-x_n(\omega')|\) would be a metric, because the \(x_n\) separate points, and it would define the topology of \(\Omega\), since the identity from the compact space \(\Omega\) to the metric space \((\Omega,d)\) is continuous and bijective. This is impossible, so \(M\) is not separable.

**Exercise 12.2** (easy; States of \(\ell^\infty\) that vanish on \(c_0\)). Let \(\varphi\) be a state of \(\ell^\infty(\mathbb N)\) with \(\varphi(x)=0\) for all \(x\in c_0\), and let \(\mu\) be the Radon measure on \(\beta\mathbb N\) with \(\varphi(x)=\int\hat x\,d\mu\).

(a) Show that \(\mu(\mathbb N)=0\). Conclude that \(\mu\) is purely singular in the sense of Theorem 5.6, and that \(\varphi\) is not of the form \(x\mapsto\sum_nc_nx_n\) with \(c\in\ell^1\).

(b) Show that such states exist.

*Solution.* (a) By Example 5.8, the transform of \(1_{\{n\}}\) is the indicator of the isolated point \(n\). Since \(1_{\{n\}}\in c_0\), \(\mu(\{n\})=\varphi(1_{\{n\}})=0\), and \(\mu(\mathbb N)=\sum_n\mu(\{n\})=0\). So \(\mu\) is concentrated on \(\beta\mathbb N\setminus\mathbb N\), which is rare (Example 5.8), and its normal part is \(0\). If \(\varphi(x)=\sum_nc_nx_n\), then \(c_n=\varphi(1_{\{n\}})=0\) for all \(n\), so \(\varphi=0\), which contradicts \(\varphi(1)=1\).

(b) The space \(\beta\mathbb N\) is compact and \(\mathbb N\) is an infinite discrete subset, so \(\beta\mathbb N\setminus\mathbb N\) is not empty; let \(p\) be one of its points. Put \(\varphi(x)=\hat x(p)\), a character and hence a state. If \(x\) has finite support, \(\hat x\) vanishes outside finitely many isolated points of \(\mathbb N\), so \(\hat x(p)=0\). Every \(x\in c_0\) is a uniform limit of such functions, so \(\varphi(x)=0\).

**Exercise 12.3** (medium; Minimal projections and isolated points). Let \(M\) be a commutative von Neumann algebra, with spectrum \(\Omega\). For a projection \(e\in M\) let \(C_e\) be the clopen set on which its transform is \(1\).

(a) Show that \(e\ne0\) is a minimal projection if and only if \(C_e\) is a single point, which is then isolated.

(b) Show that \(M\) is *atomic*, that is, every nonzero projection majorizes a minimal projection, if and only if \(\Omega=\Omega_d\) in Proposition 6.5, and that then \(M\cong\ell^\infty(I)\), where \(I\) is the set of minimal projections.

(c) Show that \(M\cong\ell^\infty(I)\oplus M_c\), where the abelian von Neumann algebra \(M_c\) has no minimal projections; \(I\) may be empty and \(M_c\) may be \(0\).

(d) Show that the spectrum of \(L^\infty[0,1]\) has no isolated points.

*Solution.* (a) The projections of \(C(\Omega)\) are the indicators of clopen sets, and \(e\le f\) exactly when \(C_e\subseteq C_f\). If \(C_e=\{\omega\}\), a nonzero projection \(f\le e\) has \(\varnothing\ne C_f\subseteq\{\omega\}\), so \(f=e\). If \(C_e\) has two points, Lemma 4.2(3) gives a clopen \(C\subseteq C_e\) that contains one of them and not the other, and \(1_C\) is a nonzero projection strictly below \(e\). A clopen singleton is an isolated point.

(b) By (a), minimal projections correspond to isolated points. Every nonzero projection majorizes a minimal one exactly when every nonempty clopen set contains an isolated point, that is, when the isolated points are dense (Lemma 4.2(3)), that is, when \(\Omega_d=\Omega\). Then Proposition 6.5(1) gives \(M\cong C(\Omega_d)\cong\ell^\infty(I)\).

(c) Since \(\Omega_d\) and \(\Omega_c\) are clopen, \(C(\Omega)=C(\Omega_d)\oplus C(\Omega_c)\). The first summand is \(\ell^\infty(I)\), and the second has no minimal projections by (a), since \(\Omega_c\) has no isolated points. Both summands are von Neumann algebras: they are \(Mz\) and \(M(1-z)\) for the projection \(z\) with \(C_z=\Omega_d\).

(d) \(L^\infty[0,1]\) has no minimal projection (proof of Theorem 8.4), so by (a) its spectrum has no isolated points.

**Exercise 12.4** (easy; Multiplicity). Let \(M_1=\{M_f:f\in L^\infty[0,1]\}\) on \(L^2[0,1]\), and let \(M_2=\mathcal A_2\) be the algebra of Example 1.3 on \(L^2[0,1]\oplus L^2[0,1]\).

(a) Show that \(M_2'\) consists of the operator matrices \(\begin{pmatrix}M_{f_{11}}&M_{f_{12}}\\M_{f_{21}}&M_{f_{22}}\end{pmatrix}\) with \(f_{ij}\in L^\infty[0,1]\).

(b) Show that \(M_1\) and \(M_2\) are isomorphic but not spatially isomorphic, and name the hypothesis of Theorem 7.4(3) that fails.

*Solution.* (a) An operator on \(L^2\oplus L^2\) is a matrix \((T_{ij})\) of operators on \(L^2[0,1]\). It commutes with \(M_f\oplus M_f\) exactly when each \(T_{ij}\) commutes with \(M_f\). For all \(f\in L^\infty\), this means \(T_{ij}\in M_1'=M_1\) (Theorem 3.1(3)). (b) \(M_f\mapsto M_f\oplus M_f\) is a \(*\)-isomorphism onto \(M_2\). A spatial isomorphism \(x\mapsto UxU^*\) carries commutants onto commutants. \(M_1'=M_1\) is abelian, while \(M_2'\) is not, by (a). So no unitary implements an isomorphism between them. The hypothesis that fails is maximality: \(M_2\) is not maximal abelian.

**Exercise 12.5** (easy; A sliding hump without Phillips' lemma). Let \((g_n)\) be a sequence in \(\ell^1(\mathbb N)\) that converges weakly to \(0\), and suppose the \(g_n\) have pairwise disjoint finite supports \(F_n\). Show directly that \(\|g_n\|_1\to0\).

*Solution.* Otherwise there are \(\varepsilon>0\) and infinitely many \(n\), forming a set \(N\), with \(\|g_n\|_1\ge\varepsilon\). Define \(x\in\ell^\infty\) by letting \(x(k)\) be the number of modulus one with \(x(k)g_n(k)=|g_n(k)|\) for \(k\in F_n\) and \(n\in N\), and \(x(k)=0\) elsewhere. The supports are disjoint, so \(x\) is well defined and \(\|x\|\le1\). For \(n\in N\), \(\langle g_n,x\rangle=\sum_{k\in F_n}|g_n(k)|=\|g_n\|_1\ge\varepsilon\), which contradicts weak convergence to \(0\). Steps 1 and 2 of the proof of Theorem 10.3 reduce the general case to almost disjoint supports of this kind.

## Background proofs

Each background statement below has a full programme proof. Historical books remain further reading; they do not carry a missing prerequisite. The scalar multiplication extension is proved in Proposition 3.2a, and the elementary summable-family tools are proved after this list.

- **Commutative C\*-algebras.** The Gelfand transform maps every abelian C\*-algebra \(A\) isometrically and \(*\)-isomorphically onto \(C_0(\Omega)\), where \(\Omega\) is its space of characters; \(\Omega\) is compact if \(A\) has a unit, and isomorphic algebras have homeomorphic spectra. A self-adjoint element is positive exactly when its transform is nonnegative, and the positive elements of a C\*-algebra are the elements \(y^*y\). The quotient of a C\*-algebra by a closed two-sided ideal is a C\*-algebra. For a self-adjoint \(a\) in a unital C\*-algebra, \(g\mapsto g(a)\) is an isometric \(*\)-isomorphism of \(C(\sigma(a))\) onto the C\*-algebra generated by \(1\) and \(a\). All this is proved in [C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md).
- **Topology.** Urysohn's lemma: in a compact space, or for a compact and a disjoint closed set in a locally compact space, there are continuous functions with values in \([0,1]\) that are \(1\) on the first set and \(0\) on the second; in particular compact spaces are regular. The Stone–Weierstrass theorem: a self-adjoint subalgebra of \(C_0(X)\) that separates points and vanishes nowhere is dense; in particular polynomials are dense in \(C[0,1]\). Both are proved in The Stone–Weierstrass theorem for functions vanishing at infinity. The Stone–Čech compactification of a completely regular space \(D\) is the spectrum of \(C_b(D)\), with \(D\) embedded by point evaluations; [Exercise 2.4 of the C\*-algebra lesson](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-04) proves the full construction, topological embedding, density, and unique extension of every continuous map to a compact Hausdorff target. This last property defines the Stone–Čech compactification.
- **Riesz representation theorem.** For a locally compact Hausdorff space \(X\), a positive linear functional on \(C_c(X)\) is integration against a unique Radon measure. The measure is finite on compact sets, outer regular on Borel sets and inner regular on open sets. It is also inner regular on every Borel set of finite measure, hence on all Borel sets when the measure is finite. These are Theorem 2.2 and Proposition 2.3 of the Haar lesson. Its Theorem 2.4 proves that every bounded functional on \(C_0(X)\) is integration against a unique finite complex Radon measure \(\nu\), with norm \(|\nu|(X)\), and that the measure is positive exactly when the functional is. The density of \(C_c(X)\) in \(L^p\), \(1\leq p<\infty\), is Proposition 3.1(4); it needs no global sigma-finiteness.
- **Measure theory.** Theorems 2.1–2.2 of the measure-tools lesson prove monotone and dominated convergence and Fatou on arbitrary measure spaces. Small-set control of integrable densities and the complex Radon–Nikodym theorem, with a sigma-finite reference measure and finite total variation, are proved in [Section 2 above](#oa-fnd-ao-23). For positive sigma-finite measures the density theorem is Theorem 4.1 of the measure-tools lesson. The [finite-measure uniqueness lemma and arbitrary probability product theorem](the-double-commutant-theorem.md#oa-fnd-bi-18) are proved in Section 9 of the double-commutant lesson, on the coordinate sigma-algebra and without topological assumptions on the factors.
- **Radon measures that are not \(\sigma\)-finite.** Let \(\Gamma\) be locally compact and \(\mu\) a positive Radon measure on it. The space \(L^\infty(\Gamma,\mu)\) is formed from \(\mu\)-measurable functions modulo locally null sets; its multiplication representation on \(L^2(\Gamma,\mu)\) is faithful, and its image is a maximal abelian von Neumann algebra. Proposition 3.2a proves this directly, using the full Radon decomposition and local integration proofs in Sections 1–2 of Vector-valued functions, tensor products with \(L^p\), and preduals.
- **Von Neumann algebras.** The double commutant theorem: a \(*\)-algebra of operators that contains \(1\) is strongly dense in its bicommutant, and \(S''\) is the smallest von Neumann algebra containing a self-adjoint set \(S\). A closed subspace is invariant under a self-adjoint set \(S\) exactly when its projection lies in \(S'\). The commutant of a direct sum of von Neumann algebras is the direct sum of the commutants. For a projection \(e\) in the commutant of a von Neumann algebra \(M\), the operators \(x|_{eH}\), \(x\in M\), form a von Neumann algebra on \(eH\), with commutant \(\{ex'e|_{eH}:x'\in M'\}\). A vector is cyclic for \(M\) exactly when it is separating for \(M'\). The Hilbert space \(L^2\) of a product of uncountably many nontrivial probability spaces is not separable. All of these are proved in [The double commutant theorem](the-double-commutant-theorem.md) (Propositions 2.1, 5.2 and 9.2, Theorems 4.4 and 5.8, and Exercise 9.9).
- **Functional analysis.** The complex Hahn–Banach theorem extends every bounded functional from a subspace of a normed space with the same norm: [Theorem 2.2 and Corollary 2.3 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-02) give the full proof. Its [Theorem 4.1](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-04) proves that a pointwise bounded family of bounded operators on a Banach space is bounded in operator norm. Its [Theorem 1.1](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-01) proves Zorn's lemma from the axiom of choice. The [Hilbert-space lesson, Sections 1–3](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-01), supplies full polarization, positive-form Cauchy–Schwarz and bounded-form representation proofs used in Lemma 2.4 and Theorem 11.2.

### The elementary duality of summable families

For any set \(J\), define \(\sum_{j\in J}|a_j|\) as the supremum of its finite partial sums. A family with finite sum has countable support: for each positive integer \(n\), only finitely many coordinates have \(|a_j|\geq1/n\), and their union contains every nonzero coordinate. Finite truncations are consequently dense in \(\ell^1(J)\).

The space \(\ell^1(J)\) is complete. For a norm-Cauchy sequence \(a^{(n)}\), each coordinate has a limit \(a_j\). If \(\|a^{(n)}-a^{(m)}\|_1\leq\varepsilon\) for \(m,n\geq N\), then for every finite \(F\subseteq J\), taking the coordinate limits gives \(\sum_{j\in F}|a^{(n)}_j-a_j|\leq\varepsilon\) for \(n\geq N\). Taking the supremum over \(F\) shows that \(a-a^{(N)}\in\ell^1(J)\), so \(a\in\ell^1(J)\), and that \(a^{(n)}\to a\) in norm.

Every \(b\in\ell^\infty(J)\) defines a bounded linear functional \(a\mapsto\sum_ja_jb_j\) on \(\ell^1(J)\), of norm \(\|b\|_\infty\), by absolute convergence and testing individual coordinates. Conversely, if \(\Lambda\in\ell^1(J)^*\), put \(b_j=\Lambda(\delta_j)\). Then \(|b_j|\leq\|\Lambda\|\), and linearity on finite truncations followed by norm continuity gives \(\Lambda(a)=\sum_ja_jb_j\). Thus \(\ell^1(J)^*=\ell^\infty(J)\) isometrically, including the empty index set. This is the full duality and completeness argument used in Corollary 10.4.

## References

- [Kostecki] R. P. Kostecki, *W\*-algebras and noncommutative integration*, survey, version 5, 2014, arXiv:1307.4818. https://arxiv.org/abs/1307.4818v5
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
- [van Neerven] J. van Neerven, *Functional Analysis*, [corrected author version, arXiv:2112.11166v7](https://arxiv.org/pdf/2112.11166v7).

*Freely accessible reading:* [Jesse Peterson, *Notes on operator algebras*, §3.8](https://math.vanderbilt.edu/peters10/teaching/spring2015/OperatorAlgebras.pdf) gives a route through cyclic abelian models; the arbitrary decomposition, local-null convention and finite-piece gluing are fully proved here. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.
