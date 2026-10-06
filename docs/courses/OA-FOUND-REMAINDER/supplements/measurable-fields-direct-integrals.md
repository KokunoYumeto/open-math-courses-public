# Measurable fields of Hilbert spaces and their direct integrals

*Written by Claude Opus 5.5 (Anthropic), September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A direct integral of Hilbert spaces is a continuous version of a direct sum. One attaches a Hilbert space \(H(\gamma)\) to each point \(\gamma\) of a measure space and forms the space of square-integrable sections \(\gamma\mapsto\xi(\gamma)\in H(\gamma)\). When all fibres equal one separable space \(\mathcal K\), this is \(L^2(\Gamma,\mu;\mathcal K)\). When the base is countable, it is a weighted direct sum. Direct integrals are the standard tool for decomposing representations and von Neumann algebras into simpler pieces. The spectral theorem, for instance, can be stated this way: a self-adjoint operator on a separable Hilbert space is unitarily equivalent to multiplication by the variable on a direct integral of Hilbert spaces over its spectrum.

The difficulty is measurability. The fibres are different spaces, their dimension may vary from point to point, and some of them may be zero. So there is no single space in which to measure a section. The remedy is to fix a space of sections that count as measurable, subject to three axioms. This lesson develops that framework over an arbitrary \(\sigma\)-finite measure space. Sections 2 to 5 treat fields of Hilbert spaces: the axioms, measurable orthonormal bases and the dimension function, a criterion that generates a field from a sequence of sections, fields of subspaces, and the identification of a field with a constant field on each set where the dimension is constant. Sections 6 and 7 treat measurable fields of bounded operators, conjugate fields and direct sums. Sections 8 to 10 construct the direct integral Hilbert space and study the diagonal and the decomposable operators on it. Section 11 works out four examples, among them the field of GNS spaces over the quasi-state space of a separable C\*-algebra, and Section 12 has exercises with solutions.

We assume measure and integration theory and the elementary theory of Hilbert spaces. Example 11.2 uses the Hilbert tensor product from [Spatial tensor products of von Neumann algebras](../reader/supplements/spatial-tensor-products.html), and Example 11.4 uses the GNS construction. The facts we use without proof are stated in full near the end, in the section *Background used without proof*.

Direct integrals go back to von Neumann's reduction theory (1949; see [Blackadar, Section III.1.6]), and the axioms for measurable fields used here are Dixmier's. Other basic references are [Takesaki I] and [Blackadar].

## 1. Conventions

Throughout, \((\Gamma,\Sigma,\mu)\) is a \(\sigma\)-finite measure space, and *measurable* means \(\Sigma\)-measurable. We do not assume that \(\mu\) is complete or that \(\Gamma\) is a standard Borel space, and we make no countability assumption on \(\Sigma\), except in Theorem 9.1(3), which says so. When \(\Sigma\) is complete for \(\mu\), "measurable" means "\(\mu\)-measurable" in the usual sense.

Hilbert spaces are complex, inner products are linear in the first variable, and the zero space is allowed. The Gaussian rationals \(\mathbb Q+i\mathbb Q\) form a countable dense subset of \(\mathbb C\).

Let \((H(\gamma))_{\gamma\in\Gamma}\) be a family of Hilbert spaces. A *section* is a map \(\xi\) with \(\xi(\gamma)\in H(\gamma)\) for every \(\gamma\). Under pointwise operations the sections form a vector space, \(\prod_\gamma H(\gamma)\). For sections \(\xi,\eta\) we write \(\langle\xi,\eta\rangle\) for the function \(\gamma\mapsto\langle\xi(\gamma),\eta(\gamma)\rangle\), and \(\|\xi\|\) for the function \(\gamma\mapsto\|\xi(\gamma)\|\).

## 2. Measurable fields of Hilbert spaces

**Definition 2.1** (Measurable field of Hilbert spaces). A *measurable field of Hilbert spaces* over \((\Gamma,\Sigma,\mu)\) is a family \((H(\gamma))_{\gamma\in\Gamma}\) together with a linear subspace \(\mathfrak M\subseteq\prod_\gamma H(\gamma)\), whose elements are called *measurable sections*, such that:

- **(F1)** for every \(\xi\in\mathfrak M\), the function \(\|\xi\|\) is measurable;
- **(F2)** (*saturation*) a section \(\eta\) belongs to \(\mathfrak M\) whenever \(\langle\eta,\xi\rangle\) is measurable for every \(\xi\in\mathfrak M\);
- **(F3)** there is a sequence \((\xi_n)_{n\geq1}\) in \(\mathfrak M\) such that, for every \(\gamma\), the vectors \(\xi_n(\gamma)\) have dense linear span in \(H(\gamma)\). Such a sequence is called *fundamental*.

*Reference:* [Takesaki I, Definition IV.8.9] works with \(\mu\)-measurable sections over a Borel space with a \(\sigma\)-finite measure, that is, with the completion of the Borel \(\sigma\)-algebra; Definition 2.1 allows any \(\sigma\)-algebra.

By (F3) every fibre \(H(\gamma)\) is separable: the finite combinations of the \(\xi_n(\gamma)\) with Gaussian-rational coefficients are dense. Exercise 12.1 shows that (F2) does not follow from (F1) and (F3).

**Lemma 2.2** (Closure properties). Let \((H(\gamma)),\mathfrak M\) be a measurable field.

1. For \(\xi,\eta\in\mathfrak M\), the function \(\langle\xi,\eta\rangle\) is measurable.
2. If \(f:\Gamma\to\mathbb C\) is measurable and \(\xi\in\mathfrak M\), then \(f\xi\in\mathfrak M\).
3. If \(\xi_k\in\mathfrak M\) and \(\xi_k(\gamma)\to\xi(\gamma)\) weakly in \(H(\gamma)\) for every \(\gamma\), then \(\xi\in\mathfrak M\).
4. (*Gluing*) If \((\Gamma_k)\) is a countable measurable partition of \(\Gamma\) and \(\xi^{(k)}\in\mathfrak M\), the section equal to \(\xi^{(k)}\) on \(\Gamma_k\) belongs to \(\mathfrak M\).

**Proof.** (1) Since \(\mathfrak M\) is a linear subspace, \(\xi+i^k\eta\in\mathfrak M\) for \(k=0,1,2,3\). The polarization identity
\(\langle\xi,\eta\rangle=\tfrac14\sum_{k=0}^3 i^k\|\xi+i^k\eta\|^2\)
expresses \(\langle\xi,\eta\rangle\) through four functions that are measurable by (F1).

(2) For every \(\eta\in\mathfrak M\), the function \(\langle f\xi,\eta\rangle=f\langle\xi,\eta\rangle\) is measurable by (1). Saturation (F2) gives \(f\xi\in\mathfrak M\).

(3) Let \(\eta\in\mathfrak M\). Weak convergence gives \(\langle\xi,\eta\rangle=\lim_k\langle\xi_k,\eta\rangle\) pointwise, and each \(\langle\xi_k,\eta\rangle\) is measurable by (1). A pointwise limit of measurable functions is measurable, so (F2) gives \(\xi\in\mathfrak M\).

(4) The partial sums \(\sum_{k\leq m}1_{\Gamma_k}\xi^{(k)}\) lie in \(\mathfrak M\) by (2). At each point they are eventually constant, because the point lies in exactly one \(\Gamma_k\). So they converge pointwise to the glued section, and (3) applies. \(\square\)

## 3. Orthonormal fundamental sequences, dimension and generation

**Theorem 3.1** (Orthonormal fundamental sequences). Let \((H(\gamma)),\mathfrak M\) be a measurable field with fundamental sequence \((\xi_j)\).

1. There is a sequence \((e_k)_{k\geq1}\) in \(\mathfrak M\) with the following property. For every \(\gamma\), let \(n(\gamma)\in\{0,1,2,\ldots,\infty\}\) be the number of indices \(k\) with \(e_k(\gamma)\neq0\). Then \(e_k(\gamma)\neq0\) exactly for \(k\leq n(\gamma)\), and \((e_k(\gamma))_{k\leq n(\gamma)}\) is an orthonormal basis of \(H(\gamma)\). In particular \(n(\gamma)=\dim H(\gamma)\), and the dimension function \(\gamma\mapsto\dim H(\gamma)\) is measurable.
2. Each \(e_k\) has the form \(e_k=\sum_j c_{kj}\xi_j\), where the \(c_{kj}\) are measurable functions and, at each \(\gamma\), only finitely many \(c_{kj}(\gamma)\) are nonzero. The coefficients are built from the Gram functions \(\langle\xi_j,\xi_i\rangle\) alone.
3. (*Testing*) A section \(\eta\) belongs to \(\mathfrak M\) if and only if \(\langle\eta,\xi_j\rangle\) is measurable for every \(j\).
4. (*Generation*) Conversely, let \((\xi_j)\) be any sequence of sections of a family \((H(\gamma))\) such that all Gram functions \(\langle\xi_j,\xi_i\rangle\) are measurable and \((\xi_j(\gamma))_j\) is total in \(H(\gamma)\) for every \(\gamma\). Then
\[
\mathfrak M=\{\eta :\ \langle\eta,\xi_j\rangle\ \text{is measurable for every }j\}
\tag{3.1}
\]
is a measurable field with fundamental sequence \((\xi_j)\), and it is the only measurable field containing every \(\xi_j\).

A sequence \((e_k)\) as in (1) is called an *orthonormal fundamental sequence*.

**Proof.** (1)–(2) *The recursion.* We build \(e_1,e_2,\ldots\) recursively. At each stage \(k\) we maintain two properties:

- at every \(\gamma\), the nonzero vectors among \(e_1(\gamma),\ldots,e_k(\gamma)\) are orthonormal and form an initial segment \(e_1(\gamma),\ldots,e_m(\gamma)\);
- each \(e_i\) with \(i\leq k\) has the form stated in (2).

We start with \(k=0\) and no vectors.

Suppose \(e_1,\ldots,e_k\) have been built. Let \(P_k(\gamma)v=\sum_{i\leq k}\langle v,e_i(\gamma)\rangle e_i(\gamma)\). By the orthonormality property, \(P_k(\gamma)\) is the orthogonal projection onto the span of \(e_1(\gamma),\ldots,e_k(\gamma)\). Put \(r_j=\xi_j-P_k\xi_j\). These sections lie in \(\mathfrak M\), because the coefficients \(\langle\xi_j,e_i\rangle\) are measurable (Lemma 2.2(1)) and \(\mathfrak M\) is closed under multiplication by measurable functions (Lemma 2.2(2)). By Pythagoras, \(\|r_j\|^2=\|\xi_j\|^2-\sum_{i\leq k}|\langle\xi_j,e_i\rangle|^2\). Define
\[
E_j=\{\gamma :\ r_i(\gamma)=0\ \text{for } i<j,\ r_j(\gamma)\neq0\},
\]
which are pairwise disjoint, and measurable because the norm functions \(\|r_i\|\) are measurable. Set
\[
e_{k+1}=\sum_{j\geq1}1_{E_j}\,\|r_j\|^{-1}r_j .
\tag{3.2}
\]
Here the \(j\)-th term is read as \(0\) off \(E_j\). Each term lies in \(\mathfrak M\) by Lemma 2.2(2), and at each point at most one term is nonzero. So the partial sums converge pointwise, and Lemma 2.2(3) gives \(e_{k+1}\in\mathfrak M\).

We check the two properties at stage \(k+1\).

- On \(E_j\), \(e_{k+1}(\gamma)\) is a unit vector orthogonal to \(e_1(\gamma),\ldots,e_k(\gamma)\).
- Off \(\bigcup_jE_j\), every \(r_j(\gamma)\) vanishes. So every \(\xi_j(\gamma)\) already lies in the span of \(e_1(\gamma),\ldots,e_k(\gamma)\), and \(e_{k+1}(\gamma)=0\).
- Suppose \(e_k(\gamma)=0\). Then at stage \(k\) the point \(\gamma\) lay outside all the sets \(E_j\), so every \(\xi_j(\gamma)\) lay in the span of the earlier vectors \(e_1(\gamma),\ldots,e_{k-1}(\gamma)\). Hence \(\gamma\notin\bigcup_jE_j\) at stage \(k+1\) as well, and \(e_{k+1}(\gamma)=0\). So the initial-segment property persists.
- Expanding \(P_k\xi_j\) by the form of \(e_1,\ldots,e_k\) shows that \(e_{k+1}\) again has the form (2): at each point only one \(j\) contributes, and each \(e_i\) has only finitely many nonzero coefficients there. The coefficients of \(e_{k+1}\) involve only \(1_{E_j}\), the norms \(\|r_j\|\) and the functions \(\langle\xi_j,e_i\rangle=\sum_l\overline{c_{il}}\langle\xi_j,\xi_l\rangle\). By the Pythagoras formula these are measurable functions of the Gram functions, and so are the sets \(E_j\).

In particular, the recursion uses nothing about \(\mathfrak M\) beyond the Gram functions. This is what (4) needs.

*The vectors span.* Fix \(\gamma\). When \(\gamma\in E_{j}\) at stage \(k+1\), write \(j_k=j\). After that stage, the vectors \(\xi_1(\gamma),\ldots,\xi_{j_k}(\gamma)\) all lie in the span of \(e_1(\gamma),\ldots,e_{k+1}(\gamma)\). Indeed, those with index below \(j_k\) already lay in the smaller span, and \(\xi_{j_k}=P_k\xi_{j_k}+r_{j_k}\), where \(r_{j_k}(\gamma)\) is a multiple of \(e_{k+1}(\gamma)\). Hence the indices \(j_k\) strictly increase. If the recursion never produces a zero vector at \(\gamma\), every \(\xi_j(\gamma)\) therefore eventually lies in the span of finitely many \(e_i(\gamma)\). If it produces \(e_{m+1}(\gamma)=0\), every \(\xi_j(\gamma)\) lies in the span of \(e_1(\gamma),\ldots,e_m(\gamma)\). In both cases the closed span of the nonzero \(e_i(\gamma)\) contains the total family \((\xi_j(\gamma))\), so it is \(H(\gamma)\). This proves (1), apart from measurability of \(n\), which follows from \(\{n\geq k\}=\{\|e_k\|=1\}\).

(3) If \(\eta\in\mathfrak M\), the functions \(\langle\eta,\xi_j\rangle\) are measurable by Lemma 2.2(1). Conversely, suppose they are measurable. By (2), \(\langle\eta,e_k\rangle=\sum_j\overline{c_{kj}}\langle\eta,\xi_j\rangle\). At each point this is a finite sum, so it is a pointwise limit of measurable functions, hence measurable. For \(\zeta\in\mathfrak M\), Parseval's identity in \(H(\gamma)\) gives
\[
\langle\eta,\zeta\rangle(\gamma)=\sum_{k\leq n(\gamma)}\langle\eta(\gamma),e_k(\gamma)\rangle\langle e_k(\gamma),\zeta(\gamma)\rangle
=\sum_{k\geq1}\langle\eta,e_k\rangle(\gamma)\,\langle e_k,\zeta\rangle(\gamma),
\]
since \(e_k(\gamma)=0\) for \(k>n(\gamma)\). The series converges absolutely at every point, so \(\langle\eta,\zeta\rangle\) is measurable, and (F2) gives \(\eta\in\mathfrak M\).

(4) Each \(\xi_i\) belongs to \(\mathfrak M\), since its inner products with the \(\xi_j\) are Gram functions. Clearly \(\mathfrak M\) is a linear subspace. Run the recursion of (1)–(2) on \((\xi_j)\). It uses only the Gram functions and the operations of (2), so it produces sections \(e_k\) of the form (2) whose nonzero values form an orthonormal basis at every point. For \(\eta\in\mathfrak M\), the functions \(\langle\eta,e_k\rangle\) are measurable as in (3), hence so is \(\|\eta\|^2=\sum_k|\langle\eta,e_k\rangle|^2\). This is (F1). For (F2), suppose \(\langle\eta,\zeta\rangle\) is measurable for every \(\zeta\in\mathfrak M\). Then it is measurable in particular for every \(\zeta=\xi_j\), so \(\eta\in\mathfrak M\). (F3) holds by hypothesis. Finally, let \(\mathfrak M'\) be any measurable field containing all \(\xi_j\). Then \(\mathfrak M'\subseteq\mathfrak M\) by Lemma 2.2(1), applied in \(\mathfrak M'\), and \(\mathfrak M\subseteq\mathfrak M'\) by the testing criterion (3), applied to \(\mathfrak M'\). \(\square\)

## 4. Fields of subspaces and measurable projections

**Proposition 4.1** (Subspace fields). Let \((H(\gamma)),\mathfrak M\) be a measurable field with fundamental sequence \((\xi_n)\). Let \((\eta_j)\) be a sequence in \(\mathfrak M\), and let \(K(\gamma)\) be the closed linear span of \(\{\eta_j(\gamma)\}\).

1. Let \(P(\gamma)\) be the orthogonal projection of \(H(\gamma)\) onto \(K(\gamma)\). Then \(P\xi\in\mathfrak M\) for every \(\xi\in\mathfrak M\).
2. \((K(\gamma))\) with \(\mathfrak M_K=\{\xi\in\mathfrak M:\ \xi(\gamma)\in K(\gamma)\ \text{for all }\gamma\}\) is a measurable field with fundamental sequence \((\eta_j)\). In particular \(\gamma\mapsto\dim K(\gamma)\) is measurable.
3. The orthogonal complements \(K(\gamma)^\perp\), with \(\{\xi\in\mathfrak M:\ \xi(\gamma)\perp K(\gamma)\ \text{for all }\gamma\}\), form a measurable field with fundamental sequence \(((1-P)\xi_n)\).

**Proof.** Run the recursion from the proof of Theorem 3.1 on the sequence \((\eta_j)\) inside \(\mathfrak M\). Totality was used there only at the end, to identify the closed span of the new vectors with the whole fibre. So the recursion produces sections \(f_k\in\mathfrak M\) whose nonzero values are orthonormal and have a closed span containing every \(\eta_j(\gamma)\). Each \(f_k(\gamma)\) lies in \(K(\gamma)\), because the recursion gives \(f_k\) the form of Theorem 3.1(2): at each point it is a finite combination of the \(\eta_j(\gamma)\). So the nonzero values of the \(f_k\) form an orthonormal basis of \(K(\gamma)\) at each point. Then
\(P\xi=\sum_k\langle\xi,f_k\rangle f_k\)
is a pointwise norm-convergent series. Its terms lie in \(\mathfrak M\) by Lemma 2.2(1)–(2), so \(P\xi\in\mathfrak M\) by Lemma 2.2(3). This proves (1).

For (2), \(\mathfrak M_K\) is a linear subspace satisfying (F1). For (F2), let \(\zeta\) be a section of \((K(\gamma))\) such that \(\langle\zeta,\xi\rangle\) is measurable for every \(\xi\in\mathfrak M_K\). For arbitrary \(\xi\in\mathfrak M\) we have \(\langle\zeta,\xi\rangle=\langle\zeta,P\xi\rangle\), because \(\zeta(\gamma)\in K(\gamma)\), and \(P\xi\in\mathfrak M_K\) by (1). So \(\langle\zeta,\xi\rangle\) is measurable for every \(\xi\in\mathfrak M\). Then (F2) for the ambient field gives \(\zeta\in\mathfrak M\), hence \(\zeta\in\mathfrak M_K\). The \(\eta_j\) form a fundamental sequence by definition of \(K(\gamma)\). The dimension function is measurable by Theorem 3.1(1), applied to this field.

Part (3) is the same argument with \(1-P\) in place of \(P\). The vectors \((1-P(\gamma))\xi_n(\gamma)\) are total in \(K(\gamma)^\perp\), because the \(\xi_n(\gamma)\) are total in \(H(\gamma)\) and \(1-P(\gamma)\) maps \(H(\gamma)\) continuously onto \(K(\gamma)^\perp\). \(\square\)

**Remark 4.2** (Null sets). Suppose we only know that the vectors \(\eta_j(\gamma)\) span a dense subspace of some intended subspace \(K(\gamma)\) for \(\gamma\) outside a measurable null set \(N\). Apply Proposition 4.1 to the sections \(1_{\Gamma\setminus N}\eta_j\). The resulting projection field is measurable, and it agrees with the projection onto \(K(\gamma)\) almost everywhere. For operators on the direct integral this is enough, because measurable fields that agree almost everywhere define the same operator (Theorem 10.1(2)). This situation arises, for instance, when certain sections are known to be dense in the graphs of a field of closed operators only at almost every point.

## 5. Reduction to constant fields

For \(d\in\{0,1,2,\ldots,\infty\}\), let \(\ell^2_d\) be \(\mathbb C^d\) (\(\ell^2(\mathbb N)\) when \(d=\infty\)) with standard orthonormal basis \((\varepsilon_k)\).

**Theorem 5.1** (Reduction to constant fields). Let \((H(\gamma)),\mathfrak M\) be a measurable field, let \(n(\gamma)=\dim H(\gamma)\), and let \(\Gamma_d=\{\gamma: n(\gamma)=d\}\). These sets form a countable measurable partition of \(\Gamma\). Let \((e_k)\) be an orthonormal fundamental sequence as in Theorem 3.1(1), and define for \(\gamma\in\Gamma_d\)
\[
U(\gamma):H(\gamma)\to\ell^2_d,\qquad U(\gamma)v=\sum_{k\leq d}\langle v,e_k(\gamma)\rangle\varepsilon_k .
\tag{5.1}
\]
Each \(U(\gamma)\) is unitary. A section \(\xi\) is measurable if and only if, for every \(d\), all coordinates \(\gamma\mapsto\langle U(\gamma)\xi(\gamma),\varepsilon_k\rangle\) are measurable on \(\Gamma_d\). Consequently, the restriction of the field to \(\Gamma_d\) is carried by the measurable unitary field \(U\) onto the constant field \(\ell^2_d\), whose measurable sections are the maps \(\Gamma_d\to\ell^2_d\) with measurable coordinates.

**Proof.** The partition is measurable because the dimension function is measurable (Theorem 3.1(1)). \(U(\gamma)\) maps an orthonormal basis onto an orthonormal basis, so it is unitary. On \(\Gamma_d\), the coordinates of \(U\xi\) are the functions \(\langle\xi,e_k\rangle\), \(k\leq d\). If \(\xi\) is measurable, they are measurable by Lemma 2.2(1). Conversely, suppose they are measurable on every \(\Gamma_d\), and fix \(k\). On \(\Gamma_d\) with \(d\geq k\), the function \(\langle\xi,e_k\rangle\) is one of these coordinates. On \(\Gamma_d\) with \(d<k\) it vanishes, because \(e_k(\gamma)=0\) there. So \(\langle\xi,e_k\rangle=\sum_d1_{\Gamma_d}\langle\xi,e_k\rangle\) is measurable on \(\Gamma\). The Parseval argument in the proof of Theorem 3.1(3) then shows that \(\langle\xi,\zeta\rangle\) is measurable for every \(\zeta\in\mathfrak M\), and (F2) gives \(\xi\in\mathfrak M\). For the constant field, the constant sections \(\varepsilon_k\) form a fundamental sequence with constant Gram functions, and Theorem 3.1(4) identifies its measurable sections with the maps that have measurable coordinates. \(\square\)

**Remark 5.2.** A map into the separable space \(\ell^2_d\) with measurable coordinates is weakly measurable, by Parseval's identity. By Pettis's theorem (see *Background used without proof*), it is then Borel measurable and a pointwise limit of measurable maps with finitely many values. So in the constant case the usual notions of measurability agree. One can also embed all fibres at once into one fixed infinite-dimensional Hilbert space by a measurable field of isometries. That form uses a Borel structure on the set of closed subspaces, and it is treated in [The Effros Borel structure](../reader/supplements/effros-borel-structure.html). The form above, on the sets of constant dimension, needs no Borel structure on spaces of subspaces, and it is the form used in later lessons.

## 6. Measurable fields of bounded operators

**Definition 6.1** (Measurable operator field). Let \((H(\gamma)),\mathfrak M\) and \((K(\gamma)),\mathfrak N\) be measurable fields. A family \(x=(x(\gamma))\) with \(x(\gamma)\in B(H(\gamma),K(\gamma))\) is a *measurable field of bounded operators* if the section \(x\xi:\gamma\mapsto x(\gamma)\xi(\gamma)\) belongs to \(\mathfrak N\) for every \(\xi\in\mathfrak M\). No bound on \(\|x(\gamma)\|\) that is uniform in \(\gamma\) is assumed.

**Theorem 6.2** (Properties of measurable operator fields). Let \(x\) be a family of bounded operators as in Definition 6.1.

1. (*Testing*) \(x\) is measurable if and only if \(x\xi_j\in\mathfrak N\) for every member of one fundamental sequence \((\xi_j)\) of \(\mathfrak M\).
2. (*Adjoints*) If \(x\) is measurable, so is \(x^*=(x(\gamma)^*)\) from \((K(\gamma))\) to \((H(\gamma))\).
3. (*Norms*) If \(x\) is measurable, the function \(\gamma\mapsto\|x(\gamma)\|\in[0,\infty)\) is measurable.
4. (*Algebra*) Sums, products with measurable scalar functions, and composites of measurable operator fields are measurable. The identity field and the projection fields of Proposition 4.1 are measurable.

**Proof.** (1) Necessity is clear. For sufficiency, apply Theorem 3.1(2) to the fundamental sequence \((\xi_j)\). It gives \(e_k=\sum_jc_{kj}\xi_j\) with measurable coefficients, only finitely many of them nonzero at each point. Hence \(xe_k=\sum_jc_{kj}\,x\xi_j\) is a countable sum of sections of \(\mathfrak N\), with finitely many nonzero terms at each point, and it lies in \(\mathfrak N\) by Lemma 2.2(2)–(3). Now let \(\xi\in\mathfrak M\). The expansion \(\xi(\gamma)=\sum_k\langle\xi,e_k\rangle(\gamma)e_k(\gamma)\) converges in norm, and \(x(\gamma)\) is bounded, so
\[
x\xi=\sum_k\langle\xi,e_k\rangle\,xe_k
\]
converges pointwise in norm. Each term lies in \(\mathfrak N\) by Lemma 2.2(1)–(2), so \(x\xi\in\mathfrak N\) by Lemma 2.2(3).

(2) For \(\eta\in\mathfrak N\) and \(\xi\in\mathfrak M\),
\(\langle x^*\eta,\xi\rangle=\langle\eta,x\xi\rangle\),
which is measurable by Lemma 2.2(1) because \(x\xi\in\mathfrak N\). Saturation (F2) for \(\mathfrak M\) gives \(x^*\eta\in\mathfrak M\).

(3) Let \((e_k)\) be an orthonormal fundamental sequence of \(\mathfrak M\) (Theorem 3.1(1)). Let \(Q\) be the countable set of finitely supported sequences \(q=(q_1,\ldots,q_m)\) of Gaussian rationals with \(\sum|q_k|^2\leq1\), and let \(v_q=\sum_kq_ke_k\in\mathfrak M\). At every \(\gamma\), \(\|v_q(\gamma)\|\leq1\), because the nonzero \(e_k(\gamma)\) are orthonormal and the others vanish. Moreover \(\{v_q(\gamma):q\in Q\}\) is dense in the closed unit ball of \(H(\gamma)\). Since \(x(\gamma)\) is continuous,
\[
\|x(\gamma)\|=\sup_{q\in Q}\|x(\gamma)v_q(\gamma)\|,
\tag{6.1}
\]
a countable supremum of functions that are measurable by (F1) for \(\mathfrak N\). If \(H(\gamma)=0\), both sides are \(0\).

(4) Sums and products with measurable scalar functions are measurable because \(\mathfrak N\) is a linear subspace closed under multiplication by measurable functions (Lemma 2.2(2)). Composites are measurable because \((yx)\xi=y(x\xi)\). The identity field is measurable by definition, and the projection fields are measurable by Proposition 4.1(1). \(\square\)

## 7. Conjugate fields, direct sums and block operators

**Proposition 7.1** (Conjugates, direct sums and blocks). Let \((H(\gamma)),\mathfrak M\) and \((K(\gamma)),\mathfrak N\) be measurable fields with fundamental sequences \((\xi_n)\) and \((\eta_n)\).

1. (*Conjugate field*) Let \(\overline{H(\gamma)}\) be the conjugate Hilbert space, the same set with scalar multiplication \(\lambda\cdot\overline v=\overline{\bar\lambda v}\) and \(\langle\overline v,\overline w\rangle=\langle w,v\rangle\). Let \(\overline{\mathfrak M}=\{\overline\xi:\xi\in\mathfrak M\}\), where \(\overline\xi(\gamma)=\overline{\xi(\gamma)}\). Then \((\overline{H(\gamma)}),\overline{\mathfrak M}\) is a measurable field with fundamental sequence \((\overline{\xi_n})\). The canonical antiunitaries \(\kappa(\gamma):v\mapsto\overline v\) carry measurable sections exactly onto measurable sections.
2. (*Direct sums*) \((H(\gamma)\oplus K(\gamma))\) with \(\mathfrak M\oplus\mathfrak N=\{(\xi,\eta):\xi\in\mathfrak M,\eta\in\mathfrak N\}\) is a measurable field. A fundamental sequence is obtained by interleaving \((\xi_n,0)\) and \((0,\eta_n)\).
3. (*Blocks*) A field of bounded operators on \((H(\gamma)\oplus K(\gamma))\), or between two such direct sums, is measurable if and only if its four matrix blocks are measurable.

**Proof.** (1) \(\overline{\mathfrak M}\) is a complex linear subspace, since \(\lambda\cdot\overline\xi=\overline{\bar\lambda\xi}\), and \(\|\overline\xi\|=\|\xi\|\) gives (F1). Every section of the conjugate family has the form \(\overline\zeta\) for a unique section \(\zeta\) of \((H(\gamma))\). If \(\langle\overline\zeta,\overline\xi\rangle=\langle\xi,\zeta\rangle\) is measurable for every \(\xi\in\mathfrak M\), then so is its complex conjugate \(\langle\zeta,\xi\rangle\), so \(\zeta\in\mathfrak M\) and \(\overline\zeta\in\overline{\mathfrak M}\). This is (F2). Totality of \((\overline{\xi_n(\gamma)})\) is the same statement as totality of \((\xi_n(\gamma))\). The last clause restates the definition of \(\overline{\mathfrak M}\).

(2) (F1) holds since \(\|(\xi,\eta)\|^2=\|\xi\|^2+\|\eta\|^2\). For (F2), suppose \(\langle(\zeta_1,\zeta_2),(\xi,\eta)\rangle\) is measurable for all measurable pairs. Taking \(\eta=0\) shows that \(\langle\zeta_1,\xi\rangle\) is measurable for every \(\xi\in\mathfrak M\), so \(\zeta_1\in\mathfrak M\); similarly \(\zeta_2\in\mathfrak N\). Totality of the interleaved sequence is clear.

(3) The inclusions \(\xi\mapsto(\xi,0)\) and \(\eta\mapsto(0,\eta)\) and the coordinate projections are measurable operator fields by (2). Each block is a composite of the given field with these, hence measurable by Theorem 6.2(4). Conversely, suppose the four blocks \(x_{11},x_{12},x_{21},x_{22}\) are measurable. Then the field maps a measurable section \((\xi,\eta)\) to \((x_{11}\xi+x_{12}\eta,\ x_{21}\xi+x_{22}\eta)\), which is measurable by (2). \(\square\)

## 8. The direct integral Hilbert space

**Definition 8.1** (Direct integral). Let \((H(\gamma)),\mathfrak M\) be a measurable field, and let \(\mathcal L^2\) be the set of \(\xi\in\mathfrak M\) with \(\int_\Gamma\|\xi(\gamma)\|^2\,d\mu(\gamma)<\infty\). The *direct integral*
\[
\int_\Gamma^\oplus H(\gamma)\,d\mu(\gamma)
\]
is \(\mathcal L^2\) modulo equality \(\mu\)-almost everywhere, with
\[
\langle\xi,\eta\rangle=\int_\Gamma\langle\xi(\gamma),\eta(\gamma)\rangle\,d\mu(\gamma).
\tag{8.1}
\]

We use the same letter for a section in \(\mathcal L^2\) and for its class, and we also write \(\|\xi\|\) for the norm of \(\xi\) in the direct integral. When \(\|\xi\|\) appears as a function of \(\gamma\), or inside a set such as \(\{\|\xi\|\leq m\}\), it is the pointwise norm function of Section 1.

**Theorem 8.2** (Completeness).

1. (8.1) is a well-defined inner product.
2. The direct integral is complete, hence a Hilbert space.
3. (*Almost-everywhere subsequences*) If \(\xi_k\to\xi\) in the direct integral, some subsequence satisfies \(\xi_{k_j}(\gamma)\to\xi(\gamma)\) in \(H(\gamma)\) for almost every \(\gamma\).

**Proof.** (1) The integrand is measurable by Lemma 2.2(1). It is integrable, since \(|\langle\xi(\gamma),\eta(\gamma)\rangle|\leq\|\xi(\gamma)\|\|\eta(\gamma)\|\) and the right side is integrable by the Cauchy–Schwarz inequality in \(L^2(\Gamma,\mu)\). \(\mathcal L^2\) is a linear subspace because \(\|\xi+\eta\|^2\leq2\|\xi\|^2+2\|\eta\|^2\) pointwise. Changing \(\xi\) on a null set does not change (8.1), and \(\langle\xi,\xi\rangle=0\) forces \(\xi=0\) almost everywhere.

(2) Let \((\xi_k)\) be a Cauchy sequence, with representatives in \(\mathcal L^2\). Choose \(k_1<k_2<\cdots\) with \(\|\xi_{k_{j+1}}-\xi_{k_j}\|\leq2^{-j}\), and put
\[
G(\gamma)=\sum_{j\geq1}\|\xi_{k_{j+1}}(\gamma)-\xi_{k_j}(\gamma)\|\in[0,\infty].
\]
\(G\) is measurable, as a countable sum of nonnegative measurable functions. The \(j\)-th term of \(G\) has norm \(\|\xi_{k_{j+1}}-\xi_{k_j}\|\leq2^{-j}\) in \(L^2(\Gamma,\mu)\). By Minkowski's inequality in \(L^2(\Gamma,\mu)\) and monotone convergence, \(\|G\|_{L^2}\leq\sum_j2^{-j}\leq1\). So \(N=\{G=\infty\}\) is a measurable null set. For \(\gamma\notin N\), the sequence \((\xi_{k_j}(\gamma))_j\) is Cauchy in \(H(\gamma)\), because the distances between consecutive terms have a finite sum. Let \(\xi(\gamma)\) be its limit, and set \(\xi(\gamma)=0\) on \(N\). Then \(\xi\) is the pointwise limit of the sections \(1_{\Gamma\setminus N}\,\xi_{k_j}\), so \(\xi\in\mathfrak M\) by Lemma 2.2(2)–(3). For each \(i\), Fatou's lemma gives
\[
\int\|\xi-\xi_{k_i}\|^2\,d\mu\leq\liminf_{j\to\infty}\int\|\xi_{k_j}-\xi_{k_i}\|^2\,d\mu=\liminf_{j\to\infty}\|\xi_{k_j}-\xi_{k_i}\|^2 .
\]
The right side is finite, and it tends to \(0\) as \(i\to\infty\) because the sequence is Cauchy. Hence \(\xi\in\mathcal L^2\) and \(\xi_{k_i}\to\xi\). A Cauchy sequence with a convergent subsequence converges, so \(\xi_k\to\xi\).

(3) A convergent sequence is Cauchy. Applied to \((\xi_k)\), the proof of (2) produces a subsequence that converges at almost every point to a section representing the limit of the sequence, and that limit is \(\xi\). \(\square\)

## 9. Diagonal operators, localization and separability

**Theorem 9.1** (Diagonal operators, localization, separability). Let \((H(\gamma)),\mathfrak M\) be a measurable field.

1. (*Diagonal operators*) For \(f\in L^\infty(\Gamma,\mu)\), the formula \((m_f\xi)(\gamma)=f(\gamma)\xi(\gamma)\) defines a bounded operator on the direct integral with \(\|m_f\|\leq\|f\|_\infty\). The map \(f\mapsto m_f\) is a unital \(*\)-homomorphism.
2. (*Finite-measure localization*) Let \((\xi_n)\) be a fundamental sequence. For every \(E\in\Sigma\) with \(\mu(E)<\infty\) and every \(n,m\), the section \(1_{E\cap\{\|\xi_n\|\leq m\}}\,\xi_n\) belongs to \(\mathcal L^2\). A vector of the direct integral orthogonal to all of them is zero, so their linear span is dense.
3. (*Separability*) Suppose \(\Sigma\) is countably generated modulo \(\mu\)-null sets: there is a countable algebra \(\mathcal A\subseteq\Sigma\) such that every set in \(\Sigma\) differs by a null set from a set in the \(\sigma\)-algebra generated by \(\mathcal A\). This holds, for example, on a standard Borel space. Then the direct integral is separable.

**Proof.** (1) \(f\xi\in\mathfrak M\) by Lemma 2.2(2), and \(\|f\xi\|^2\leq\|f\|_\infty^2\|\xi\|^2\) pointwise almost everywhere. Changing \(f\) on a null set does not change \(m_f\). Pointwise, \(\langle f\xi,\eta\rangle=\langle\xi,\bar f\eta\rangle\) and \((fg)\xi=f(g\xi)\), so \(m_f^*=m_{\bar f}\), \(m_{fg}=m_fm_g\) and \(m_1=1\).

(2) The integral of \(\|1_{E\cap\{\|\xi_n\|\leq m\}}\xi_n\|^2\) is at most \(m^2\mu(E)\), so these sections lie in \(\mathcal L^2\). Let \(\eta\) be a vector of the direct integral orthogonal to all of them. Put \(h_{n,m}=1_{\{\|\xi_n\|\leq m\}}\langle\eta,\xi_n\rangle\). This function is measurable, and \(|h_{n,m}|\leq m\|\eta\|\) pointwise. Since the function \(\|\eta\|\) lies in \(L^2(\Gamma,\mu)\), \(h_{n,m}\) is integrable over every set of finite measure. The orthogonality hypothesis says exactly that \(\int_Eh_{n,m}\,d\mu=0\) whenever \(\mu(E)<\infty\). By \(\sigma\)-finiteness there are sets \(F_k\) of finite measure with union \(\Gamma\). Apply the hypothesis to \(E=F_k\cap\{\operatorname{Re}h_{n,m}>0\}\). Taking real parts, the integral of \(\operatorname{Re}h_{n,m}\) over this set vanishes, while \(\operatorname{Re}h_{n,m}>0\) on it, so the set is null. Hence \(\{\operatorname{Re}h_{n,m}>0\}\) is null. The same argument applies to \(\{\operatorname{Re}h_{n,m}<0\}\), \(\{\operatorname{Im}h_{n,m}>0\}\) and \(\{\operatorname{Im}h_{n,m}<0\}\), so \(h_{n,m}=0\) almost everywhere. Discarding countably many null sets, we get \(\langle\eta(\gamma),\xi_n(\gamma)\rangle=0\) for all \(n\) at almost every \(\gamma\), since every point lies in \(\{\|\xi_n\|\leq m\}\) for large \(m\). Totality of \((\xi_n(\gamma))\) gives \(\eta(\gamma)=0\) almost everywhere.

(3) Fix an increasing sequence \((F_k)\) of sets of finite measure with union \(\Gamma\). For \(E\) of finite measure, \(\|1_{E\setminus F_k}1_{\{\|\xi_n\|\leq m\}}\xi_n\|^2\leq m^2\mu(E\setminus F_k)\to0\) as \(k\to\infty\). So it suffices to approximate the vectors of (2) with \(E\subseteq F_k\) for some \(k\).

Fix \(k\). We show first that every measurable \(E\subseteq F_k\) can be approximated by sets from \(\mathcal A\): for every \(\delta>0\) there is \(A\in\mathcal A\) with \(\mu\big((A\cap F_k)\,\triangle\,E\big)<\delta\). Call a set \(B\in\Sigma\) *approximable* if for every \(\delta>0\) there is \(A\in\mathcal A\) with \(\mu\big((A\,\triangle\,B)\cap F_k\big)<\delta\).

- Every set in \(\mathcal A\) is approximable.
- The complement of an approximable set is approximable, because \(\mathcal A\) is closed under complements and \((\Gamma\setminus A)\,\triangle\,(\Gamma\setminus B)=A\,\triangle\,B\).
- A countable union \(B=\bigcup_iB_i\) of approximable sets is approximable. Indeed, since \(\mu(F_k)<\infty\), there is \(N\) with \(\mu\big((B\setminus\bigcup_{i\leq N}B_i)\cap F_k\big)<\delta/2\). Choose \(A_i\in\mathcal A\) with \(\mu\big((A_i\,\triangle\,B_i)\cap F_k\big)<\delta/(2N)\) for \(i\leq N\). Then \(A=\bigcup_{i\leq N}A_i\) lies in \(\mathcal A\), and \(\mu\big((A\,\triangle\,B)\cap F_k\big)<\delta\).

So the approximable sets form a \(\sigma\)-algebra containing \(\mathcal A\), and every set in the \(\sigma\)-algebra generated by \(\mathcal A\) is approximable. Now let \(E\subseteq F_k\) be measurable, and choose \(B\) in the \(\sigma\)-algebra generated by \(\mathcal A\) with \(\mu(E\,\triangle\,B)=0\). Since \(E\subseteq F_k\), we have \((A\cap F_k)\,\triangle\,E\subseteq\big((A\,\triangle\,B)\cap F_k\big)\cup(B\,\triangle\,E)\) for every \(A\). So a set \(A\in\mathcal A\) that approximates \(B\) within \(\delta\) also satisfies \(\mu\big((A\cap F_k)\,\triangle\,E\big)<\delta\).

For such \(E\) and \(A\),
\[
\big\|(1_E-1_{A\cap F_k})\,1_{\{\|\xi_n\|\leq m\}}\xi_n\big\|^2\leq m^2\,\mu\big(E\,\triangle\,(A\cap F_k)\big).
\]
So the countable family of vectors \(q\,1_{A\cap F_k\cap\{\|\xi_n\|\leq m\}}\xi_n\), with \(q\) Gaussian rational, \(A\in\mathcal A\) and \(k,n,m\geq1\), approximates the spanning vectors of (2). Their finite sums form a countable dense set. \(\square\)

## 10. Decomposable operators

**Theorem 10.1** (Decomposable operators). Let \((H(\gamma)),\mathfrak M\) and \((K(\gamma)),\mathfrak N\) be measurable fields, and let \(x\) be a measurable field of bounded operators from \((H(\gamma))\) to \((K(\gamma))\) with \(\gamma\mapsto\|x(\gamma)\|\) essentially bounded. (That function is measurable by Theorem 6.2(3).) Then:

1. \((x\xi)(\gamma)=x(\gamma)\xi(\gamma)\) defines a bounded operator
\[
\int_\Gamma^\oplus x(\gamma)\,d\mu(\gamma):\ \int_\Gamma^\oplus H(\gamma)\,d\mu\longrightarrow\int_\Gamma^\oplus K(\gamma)\,d\mu,
\]
and its norm is exactly \(\operatorname*{ess\,sup}_\gamma\|x(\gamma)\|\).
2. The assignment \(x\mapsto\int^\oplus x\) is linear and multiplicative on composable fields, and \(\big(\int^\oplus x\big)^*=\int^\oplus x^*\). Two fields define the same operator if and only if they agree almost everywhere.
3. When \(K=H\), every such operator commutes with every diagonal operator \(m_f\) of Theorem 9.1(1). Operators of this form are called *decomposable*, and the \(m_f\) are the *diagonal* operators.

**Proof.** (1) \(x\xi\in\mathfrak N\) by definition, and \(\|x(\gamma)\xi(\gamma)\|\leq c\|\xi(\gamma)\|\) almost everywhere, where \(c=\operatorname{ess\,sup}\|x(\gamma)\|\). So the operator is well defined on classes, with norm at most \(c\).

For the reverse inequality we may assume \(c>0\); let \(0<\varepsilon<c\). The set \(\{\|x(\gamma)\|>c-\varepsilon\}\) has positive measure, and by \(\sigma\)-finiteness it contains a measurable set \(F\) with \(0<\mu(F)<\infty\). Let \((e_k)\), \(Q\) and \(v_q\) be as in the proof of Theorem 6.2(3), and enumerate \(Q\). For \(\gamma\in F\), let \(q(\gamma)\) be the first \(q\) with \(\|x(\gamma)v_q(\gamma)\|>c-\varepsilon\); it exists by (6.1). The sets \(F_q=\{\gamma\in F: q(\gamma)=q\}\) are measurable, being defined by countably many measurable conditions. The section \(\zeta=\sum_q1_{F_q}v_q\) lies in \(\mathfrak M\) by the gluing property, Lemma 2.2(4), applied to the partition of \(\Gamma\) into the sets \(F_q\) and \(\Gamma\setminus F\). It satisfies \(0<\|\zeta(\gamma)\|\leq1\) on \(F\), since \(x(\gamma)\zeta(\gamma)\neq0\) there, and \(\zeta=0\) off \(F\). Hence
\[
\|x\zeta\|^2=\int_F\|x(\gamma)v_{q(\gamma)}(\gamma)\|^2d\mu\geq(c-\varepsilon)^2\mu(F)\geq(c-\varepsilon)^2\|\zeta\|^2,
\]
with \(\|\zeta\|>0\). So the norm is at least \(c-\varepsilon\).

(2) Linearity and multiplicativity hold pointwise. For the adjoint, \(x^*\) is measurable by Theorem 6.2(2) and has the same norm function, and
\(\langle x\xi,\eta\rangle=\int\langle x(\gamma)\xi(\gamma),\eta(\gamma)\rangle d\mu=\int\langle\xi(\gamma),x(\gamma)^*\eta(\gamma)\rangle d\mu\).
Fields that agree almost everywhere clearly define the same operator. Conversely, if two fields \(x\) and \(y\) define the same operator, the norm formula (1) applied to \(x-y\) gives \(x(\gamma)=y(\gamma)\) almost everywhere.

(3) Pointwise, \(x(\gamma)(f(\gamma)v)=f(\gamma)x(\gamma)v\). \(\square\)

**Remark 10.2** (The converse). The converse of Theorem 10.1(3) also holds: every bounded operator on the direct integral that commutes with all diagonal operators is decomposable. It is proved in [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html#oa-fnd-dg-04).

## 11. Examples

**Example 11.1** (Countable base). Let \(\Gamma\) be countable, \(\Sigma\) all subsets, and \(\mu\) a measure with \(0<\mu(\{\gamma\})<\infty\) for every \(\gamma\). Let \(H(\gamma)\) be arbitrary separable Hilbert spaces. With \(\mathfrak M\) all sections, (F1) and (F2) hold trivially, since every function on \(\Gamma\) is measurable. For (F3), choose a dense sequence \((d_{\gamma,n})_n\) in each \(H(\gamma)\), with \(d_{\gamma,n}=0\) if \(H(\gamma)=0\), and let \(\xi_n(\gamma)=d_{\gamma,n}\). The direct integral is the Hilbert direct sum \(\bigoplus_\gamma H(\gamma)\), with inner product weighted by \(\mu(\{\gamma\})\). The map \(\xi\mapsto(\mu(\{\gamma\})^{1/2}\xi(\gamma))_\gamma\) is a unitary onto the unweighted sum. The diagonal operators are the bounded scalar sequences, acting on each summand by multiplication.

**Example 11.2** (Constant field). Let \(H(\gamma)=\mathcal K\) for a fixed separable \(\mathcal K\) with orthonormal basis \((\varepsilon_k)\), and let \(\mathfrak M\) be generated by the constant sections \(\varepsilon_k\) as in Theorem 3.1(4). The measurable sections are the maps with measurable coordinates, equivalently, by Pettis's theorem, the Borel (or weakly measurable) maps \(\Gamma\to\mathcal K\). The direct integral is the space \(L^2(\Gamma,\mu;\mathcal K)\) of classes of such maps \(\xi\) with \(\int\|\xi(\gamma)\|^2\,d\mu<\infty\). The map \(f\otimes v\mapsto(\gamma\mapsto f(\gamma)v)\) extends to a unitary \(L^2(\Gamma,\mu)\otimes\mathcal K\cong L^2(\Gamma,\mu;\mathcal K)\). Indeed, it preserves the inner products of elementary tensors, so it extends to an isometry. For any orthonormal basis \((g_i)\) of \(L^2(\Gamma,\mu)\), it carries the orthonormal basis \((g_i\otimes\varepsilon_k)\) onto the orthonormal family \((g_i\varepsilon_k)\), which is complete: if \(\xi\) is orthogonal to every \(g_i\varepsilon_k\), then each coordinate \(\langle\xi,\varepsilon_k\rangle\in L^2(\Gamma,\mu)\) is orthogonal to every \(g_i\), so \(\xi=0\) almost everywhere. So the isometry is onto.

**Example 11.3** (Varying dimension). Let \(\Gamma=(0,1]\) with Lebesgue measure, and \(d(\gamma)=k\) for \(\gamma\in(\tfrac1{k+1},\tfrac1k]\). Let \(H(\gamma)=\mathbb C^{d(\gamma)}\), and let \(\xi_n(\gamma)\) be the \(n\)-th standard basis vector if \(n\leq d(\gamma)\), else \(0\). The Gram functions \(\langle\xi_n,\xi_m\rangle=\delta_{nm}1_{\{d\geq n\}}\) are measurable, so Theorem 3.1(4) produces a measurable field. The sets of constant dimension in Theorem 5.1 are the intervals \(\Gamma_k=(\tfrac1{k+1},\tfrac1k]\), and the direct integral is \(\bigoplus_kL^2(\Gamma_k)\otimes\mathbb C^k\). The field \(x(\gamma)=\operatorname{diag}(1,\tfrac12,\ldots,\tfrac1{d(\gamma)})\) is measurable by Theorem 6.2(1), since \(x\xi_n=\tfrac1n\xi_n\). Its norm function is identically \(1\), so the decomposable operator \(\int^\oplus x\) has norm \(1\) by Theorem 10.1(1). The inverse field \(x(\gamma)^{-1}\) has norm \(d(\gamma)\), which is unbounded. So a measurable field of invertible operators need not define a bounded decomposable inverse.

**Example 11.4** (GNS spaces of a separable C\*-algebra). Let \(A\) be a separable C\*-algebra with a dense sequence \((x_n)\), and let \(Q(A)=\{\varphi\in A^*_+:\|\varphi\|\leq1\}\) be its quasi-state space. It is a weak\*-closed subset of the closed unit ball of \(A^*\), so it is compact and metrizable in the weak\* topology (see *Background used without proof*). Give it a finite positive Borel measure \(\mu\). For \(\varphi\in Q(A)\), let \(H(\varphi)\) be the GNS space of \(\varphi\) and \(\eta_\varphi:A\to H(\varphi)\) the canonical map, so that \(\langle\eta_\varphi(x),\eta_\varphi(y)\rangle=\varphi(y^*x)\). The sections \(\xi_n(\varphi)=\eta_\varphi(x_n)\) have Gram functions \(\varphi\mapsto\varphi(x_m^*x_n)\), which are weak\*-continuous, hence Borel. They are total in every fibre: \(\eta_\varphi(A)\) is dense in \(H(\varphi)\), and \(\|\eta_\varphi(x)\|^2=\varphi(x^*x)\leq\|x\|^2\) since \(\|\varphi\|\leq1\), so the \(\eta_\varphi(x_n)\) are dense in \(\eta_\varphi(A)\). By Theorem 3.1(4), there is exactly one measurable field of Hilbert spaces over \(Q(A)\) containing these sections. Its fibre at \(\varphi=0\) is the zero space.

## 12. Exercises

**Exercise 12.1** (Saturation cannot be dropped). On \(\Gamma=[0,1]\) with Lebesgue measure and \(H(\gamma)=\mathbb C\), let \(\mathfrak M_0\) be the constant sections. Show that \(\mathfrak M_0\) satisfies (F1) and (F3) but not (F2), and identify the unique measurable field containing it.

*Solution.* Norms of constant sections are constant, and the section \(1\) is fundamental. The section \(\gamma\mapsto\gamma\) has measurable inner product \(\gamma\bar c\) with every constant \(c\), yet is not constant, so (F2) fails. By Theorem 3.1(4) with fundamental sequence \((1)\), the unique measurable field containing \(\mathfrak M_0\) consists of all measurable functions \([0,1]\to\mathbb C\).

**Exercise 12.2** (Norm of a diagonal operator). Show that \(\|m_f\|=\operatorname*{ess\,sup}\{|f(\gamma)|:\ H(\gamma)\neq0\}\). In particular, \(m_f=0\) if and only if \(f=0\) almost everywhere on \(\{\dim H\geq1\}\).

*Solution.* The scalar field \(x(\gamma)=f(\gamma)1_{H(\gamma)}\) is measurable by Theorem 6.2(4), and it defines the operator \(m_f\). Its norm function is \(|f(\gamma)|\) where \(H(\gamma)\neq0\) and \(0\) where \(H(\gamma)=0\). Apply Theorem 10.1(1).

**Exercise 12.3** (Graphs of bounded fields). Let \(y\) be a measurable field of bounded operators from \((H(\gamma))\) to \((K(\gamma))\). Show that the graphs \(G(\gamma)=\{(v,y(\gamma)v)\}\subseteq H(\gamma)\oplus K(\gamma)\) form a measurable subspace field, and that the graph projections are a measurable operator field.

*Solution.* Let \((\xi_n)\) be a fundamental sequence of \((H(\gamma))\). The sections \((\xi_n,y\xi_n)\) are measurable in the direct-sum field of Proposition 7.1(2). At every point they span a dense subspace of \(G(\gamma)\), because \(v\mapsto(v,y(\gamma)v)\) is continuous and the \(\xi_n(\gamma)\) are total. So Proposition 4.1 applies. This bounded case needs no functional calculus. Fields of closed unbounded operators are also studied through their graph projections; there one often knows only that suitable sections are dense in the graphs at almost every point, which is the situation of Remark 4.2.

**Exercise 12.4** (Why subsequences). In \(L^2([0,1])=\int^\oplus_{[0,1]}\mathbb C\,d\gamma\), give a sequence converging to \(0\) in norm that converges at no point.

*Solution.* Enumerate the dyadic intervals \([j2^{-m},(j+1)2^{-m}]\), \(m\geq0\), \(0\leq j<2^m\), in order, and let \(\xi_k\) be the indicator of the \(k\)-th one. Then \(\|\xi_k\|^2=2^{-m}\to0\), while every point lies in infinitely many of these intervals and outside infinitely many others, so \(\xi_k(\gamma)\) takes both values \(0\) and \(1\) infinitely often.

## Background used without proof

- **Measure theory.** Sums, products, pointwise limits and countable suprema of measurable functions are measurable. The monotone convergence theorem and Fatou's lemma hold for nonnegative measurable functions. In \(L^2(\Gamma,\mu)\), the Cauchy–Schwarz inequality \(\int|fg|\,d\mu\leq\|f\|_2\|g\|_2\) and Minkowski's inequality \(\|f+g\|_2\leq\|f\|_2+\|g\|_2\) hold. See Section 2 and Theorems 2.1, 2.2 and 3.1 of [*Measure and Hilbert space tools for Haar integration*](../../harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools.html#2-integration-and-convergence-without-countability-assumptions).
- **Hilbert spaces.** Every Hilbert space has an orthonormal basis, that is, an orthonormal family with dense linear span. If \((e_k)\) is an orthonormal basis of \(H\), then every \(v\in H\) satisfies \(v=\sum_k\langle v,e_k\rangle e_k\), with convergence in norm, and Parseval's identity \(\langle v,w\rangle=\sum_k\langle v,e_k\rangle\langle e_k,w\rangle\) holds for all \(v,w\in H\), with absolute convergence; in particular \(\|v\|^2=\sum_k|\langle v,e_k\rangle|^2\). If \((f_k)\) is an orthonormal family with closed linear span \(K\), the orthogonal projection onto \(K\) is \(v\mapsto\sum_k\langle v,f_k\rangle f_k\), and for finitely many \(f_1,\ldots,f_k\) Pythagoras' theorem gives \(\|v-\sum_{i\leq k}\langle v,f_i\rangle f_i\|^2=\|v\|^2-\sum_{i\leq k}|\langle v,f_i\rangle|^2\). A bounded linear map between Hilbert spaces that carries an orthonormal basis onto an orthonormal basis is unitary. See Theorems 2.2 and 4.1 of [*Hilbert spaces and compact operators*](../../foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html#oa-fnd-hs-04).
- **Pettis's measurability theorem, separable case.** Let \(\mathcal K\) be a separable Hilbert space and \(f:\Gamma\to\mathcal K\) a map. The following are equivalent: (a) \(\gamma\mapsto\langle f(\gamma),v\rangle\) is measurable for every \(v\in\mathcal K\); (b) \(f^{-1}(U)\in\Sigma\) for every open set \(U\subseteq\mathcal K\); (c) \(f\) is a pointwise limit of measurable maps with finitely many values. [Pettis 1938]
- **Weak\* compactness.** The closed unit ball of the dual of a Banach space \(X\) is compact in the weak\* topology (Alaoglu's theorem). If \(X\) is separable, the weak\* topology on this ball is metrizable. See Theorem 3.1 and Proposition 3.2 of [*Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian*](../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#oa-fnd-wt-03).
- **The GNS construction.** Let \(\varphi\) be a bounded positive linear functional on a C\*-algebra \(A\). There are a Hilbert space \(H(\varphi)\) and a linear map \(\eta_\varphi:A\to H(\varphi)\) with dense range such that \(\langle\eta_\varphi(x),\eta_\varphi(y)\rangle=\varphi(y^*x)\) for all \(x,y\in A\). One takes for \(H(\varphi)\) the completion of \(A\) modulo the null space \(\{x:\varphi(x^*x)=0\}\), with the inner product \(\varphi(y^*x)\). See Theorem 5.4 and Definition 5.6 of [*Building representations from positive functionals*](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#oa-fnd-gn-05).
- **Hilbert tensor products.** For Hilbert spaces \(H\) and \(K\), the Hilbert tensor product \(H\otimes K\) is a Hilbert space in which the elementary tensors span a dense subspace and \(\langle f\otimes v,g\otimes w\rangle=\langle f,g\rangle\langle v,w\rangle\). If \((g_i)\) and \((\varepsilon_k)\) are orthonormal bases of \(H\) and \(K\), then \((g_i\otimes\varepsilon_k)\) is an orthonormal basis of \(H\otimes K\). This is proved in [Spatial tensor products of von Neumann algebras](../reader/supplements/spatial-tensor-products.html).
- **Standard Borel spaces.** The Borel \(\sigma\)-algebra of a standard Borel space is generated by a countable family of sets, hence by the countable algebra that this family generates. So it is countably generated modulo null sets in the sense of Theorem 9.1(3), and so is its completion for \(\mu\). See [Polish spaces and standard Borel spaces](../../foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces.html).

## Where this leads

- [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html) proves the converse of Theorem 10.1(3). It follows that the diagonal and the decomposable operators form von Neumann algebras, each the commutant of the other.
- [The Effros Borel structure](../reader/supplements/effros-borel-structure.html) embeds all fibres into one fixed Hilbert space by a measurable field of isometries, and treats measurable families of von Neumann algebras.
- [Vector-valued functions, tensor products with \(L^p\), and preduals](../reader/supplements/measurable-fields-direct-integrals.html#11-examples) works with a Radon measure on a locally compact space. When that measure is \(\sigma\)-finite and \(\Sigma\) is the \(\mu\)-completion of the Borel sets, it shows that the direct integral of the constant field of Example 11.2 is the space of square-integrable \(\mathcal K\)-valued functions studied there, with the same vectors and the same inner product.
- Fields of closed unbounded operators, handled through their graph projections with Proposition 4.1 and Remark 4.2, are the subject of the lesson *Measurable graphs and left multipliers in direct-integral fields* in the course on modular theory and weights.
- Beyond these lessons, the theory continues with direct integrals of von Neumann algebras and the decomposition of a von Neumann algebra over its centre; see [*Direct integrals of von Neumann algebras*](../reader/supplements/direct-integrals-of-von-neumann-algebras-commutants-and-centres-takesa.html).

## References

- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).
- [Pettis 1938] B. J. Pettis, On integration in vector spaces, *Transactions of the American Mathematical Society* 44 (1938), 277–304. https://doi.org/10.1090/S0002-9947-1938-1501970-8
- [Takesaki I] M. Takesaki, *Theory of Operator Algebras I*, Springer, New York, 1979; reprinted as Encyclopaedia of Mathematical Sciences 124, Springer, Berlin, 2002.
