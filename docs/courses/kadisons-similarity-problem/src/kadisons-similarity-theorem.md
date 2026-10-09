# Kadison's similarity theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson draws the consequences of the uniform commutator estimate of the previous lesson [OpenAI-288, Sections 1 and 7]. Every derivation of a C\*-algebra into the bounded operators, relative to any representation, is completely bounded with \(\|\Delta\|_{\rm cb}\le C\|\Delta\|\), and hence implemented by an operator of norm at most \(\frac C2\|\Delta\|\): this is the derivation problem. Every bounded unital homomorphism \(\pi\) of a unital C\*-algebra into \(B(H)\) is similar to a \(*\)-homomorphism, and the similarity can be chosen with condition number at most \(\|\pi\|^{2C}\): this is Kadison's similarity problem, with a polynomial bound in the sense of Pisier's similarity degree. Finally, every von Neumann algebra is hyperreflexive with the single constant \(2C\).

Here \(C=3C_{\rm fac}+2<6308\) is the constant of (0.1) in [The uniform commutator estimate](the-uniform-commutator-estimate.md). We use Theorem 3.1 there; Theorem 4.2 of [Row, column and cyclic estimates](row-column-and-cyclic-estimates.md); Theorem 4.3 and Corollary 4.5 of [Completely bounded homomorphisms and similarity](completely-bounded-homomorphisms-and-similarity.md); Theorem 5.1 of [From inner derivations to similarity](from-inner-derivations-to-similarity.md); Kaplansky's density theorem, [Theorem 7.1](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07); norm-preserving lifts, [Proposition 17.1 of the C\*-algebra lesson](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-29); and the spectral measure of a self-adjoint operator, [Section 2 and Theorem 3.1 of The spectral theorem for bounded self-adjoint operators](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators#OA-FND-ST-03). Throughout, \(A\) is a unital C\*-algebra.

## 1. Every derivation is completely bounded

**Lemma 1.1.** Let \(\sigma:A\to B(K)\) be a representation and \(V\in B(K)\). Put \(P=\sigma(A)''\). Then \(g_P(V)=\sup\{\|V\sigma(a)-\sigma(a)V\|:a\in A,\ \|a\|\le1\}\).

**Proof.** By Proposition 17.1 of the C\*-algebra lesson, the unit ball of \(\sigma(A)\) is the image of the unit ball of \(A\). By Kaplansky's density theorem it is strongly dense in the unit ball of \(P\), and \(x\mapsto\|Vx-xV\|\) is lower semicontinuous for the strong operator topology. \(\square\)

**Theorem 1.2** (derivations). Let \(\sigma:A\to B(K)\) and \(\lambda:A\to B(F)\) be representations and \(\Delta:A\to B(K,F)\) a bounded rectangular derivation for \(\sigma,\lambda\). Then
\[
\|\Delta\|_{\rm cb}\le C\|\Delta\|,
\]
and \(\Delta\) is implemented by an operator \(V\in B(K,F)\) with \(\|V\|\le\frac C2\|\Delta\|\).

**Proof.** First let \(F=K\) and \(\lambda=\sigma\). Decompose \(K\) into an orthogonal family \((K_i)_{i\in I}\) of cyclic subspaces reducing \(\sigma\): take a maximal orthogonal family of such subspaces, by Zorn's lemma; a nonzero vector orthogonal to all of them would generate another one. Let \(q_i\) be the projection onto \(K_i\) and \(\sigma_i=\sigma|_{K_i}\). The map \(a\mapsto\Delta(a)|_{K_i}\) is a rectangular derivation for the cyclic representation \(\sigma_i\) and for \(\sigma\), so Theorem 4.2 of the cyclic estimates lesson gives \(V_i:K_i\to K\) with \(\Delta(a)|_{K_i}=V_i\sigma_i(a)-\sigma(a)V_i\). For a finite set \(\Phi\subseteq I\) put \(q_\Phi=\sum_{i\in\Phi}q_i\) and \(V_\Phi=\sum_{i\in\Phi}V_iq_i\in B(K)\). Since \(q_i\) commutes with \(\sigma(A)\),
\[
V_\Phi\sigma(a)-\sigma(a)V_\Phi=\sum_{i\in\Phi}\big(V_i\sigma_i(a)-\sigma(a)V_i\big)q_i=\Delta(a)q_\Phi .
\]
Hence \(\|V_\Phi\sigma(a)-\sigma(a)V_\Phi\|\le\|\Delta\|\|a\|\), and by Lemma 1.1 \(g_P(V_\Phi)\le\|\Delta\|\) for \(P=\sigma(A)''\); the norms \(\|V_i\|\) play no role. The uniform commutator estimate, Theorem 3.1 of the previous lesson, gives for \(X\in M_h(A)\)
\[
\|\Delta_h(X)q_\Phi^{(h)}\|=\|[V_\Phi^{(h)},\sigma_h(X)]\|\le C\|\Delta\|\,\|\sigma_h(X)\|\le C\|\Delta\|\,\|X\| .
\]
As \(\Phi\) increases, \(q_\Phi\to1\) strongly, so \(\|\Delta_h(X)\|\le C\|\Delta\|\|X\|\). This proves \(\|\Delta\|_{\rm cb}\le C\|\Delta\|\), and Theorem 4.3 of the first lesson gives \(V\) with \(\|V\|\le\frac12\|\Delta\|_{\rm cb}\le\frac C2\|\Delta\|\).

For general \(\sigma,\lambda\), the map \(\widetilde\Delta(a)=\left(\begin{smallmatrix}0&0\\\Delta(a)&0\end{smallmatrix}\right)\) on \(K\oplus F\) is a \((\sigma\oplus\lambda)\)-derivation, with the same norm and the same completely bounded norm as \(\Delta\); an operator implementing it has a \((2,1)\) block implementing \(\Delta\), of no larger norm. \(\square\)

In particular, for a C\*-algebra \(A\subseteq B(K)\) with \(1_K\in A\), every bounded derivation \(\delta:A\to B(K)\) is inner: \(\delta(a)=Va-aV\) for some \(V\in B(K)\). By Ringrose's theorem every derivation of a C\*-algebra into a Banach bimodule is automatically bounded, so boundedness is not a real restriction; that theorem is not proved in this course and is not used.

## 2. The similarity theorem

**Theorem 2.1** (Kadison's similarity theorem). Let \(\pi:A\to B(H)\) be a bounded unital homomorphism. Then
\[
\|\pi\|_{\rm cb}\le\|\pi\|^{2C},
\]
and there is a positive invertible \(S\in B(H)\) with \(\|S\|\|S^{-1}\|\le\|\pi\|^{2C}\) such that \(a\mapsto S\pi(a)S^{-1}\) is a \(*\)-homomorphism.

**Proof.** We verify the hypothesis of Theorem 5.1 of the lesson on inner derivations with \(k=C\). Let \(\rho:A\to B(K)\) be a representation, \(t\in B(K)\) self-adjoint, and \(\Delta_t(a)=t\rho(a)-\rho(a)t\). Put \(P=\rho(A)''\). By Lemma 1.1, \(g_P(t)=\|\Delta_t\|\). For \(X\in M_h(A)\), Theorem 3.1 of the previous lesson gives
\[
\|(\Delta_t)_h(X)\|=\|[t^{(h)},\rho_h(X)]\|\le C\,g_P(t)\,\|\rho_h(X)\|\le C\|\Delta_t\|\,\|X\| .
\]
So \(\|\Delta_t\|_{\rm cb}\le C\|\Delta_t\|\), and Theorem 5.1 there gives the conclusion. \(\square\)

For a unital homomorphism, \(\|\pi\|\ge1\) unless \(H=0\), so the bound is meaningful; it equals \(1\) exactly when \(\|\pi\|=1\), in accordance with Lemma 2.1 of the first lesson.

Pisier defines the *similarity degree* \(d(A)\) of \(A\) as the infimum of the numbers \(\alpha\) for which some constant \(K_\alpha\) satisfies \(\|\pi\|_{\rm cb}\le K_\alpha\|\pi\|^\alpha\) for every bounded unital homomorphism \(\pi\) of \(A\) [Pisier-degree]. Theorem 2.1 says
\[
d(A)\le2C\qquad\text{for every unital C\*-algebra }A .
\]

## 3. Universal hyperreflexivity

For a von Neumann algebra \(M\subseteq B(H)\) with \(1_H\in M\) and \(T\in B(H)\), put
\[
\alpha_M(T)=\sup\{\|(1-e)Te\|:\ e\in M'\text{ a projection}\}.
\]
The ranges of the projections of \(M'\) are exactly the closed subspaces invariant under \(M\), which are automatically reducing. For \(m\in M\) and a projection \(e\in M'\), \((1-e)me=m(1-e)e=0\), so \(\|(1-e)Te\|=\|(1-e)(T-m)e\|\le\|T-m\|\); hence \(\alpha_M(T)\le\operatorname{dist}(T,M)\). The algebra \(M\) is *hyperreflexive* if conversely \(\operatorname{dist}(T,M)\le K\alpha_M(T)\) for some constant \(K\) and all \(T\).

**Theorem 3.1** (universal hyperreflexivity). For every Hilbert space \(H\), every von Neumann algebra \(M\subseteq B(H)\) with \(1_H\in M\) and every \(T\in B(H)\),
\[
\alpha_M(T)\le\operatorname{dist}(T,M)\le2C\,\alpha_M(T).
\]

**Proof.** Put \(P=M'\), so \(P'=M\). Let \(\alpha=\alpha_M(T)\). For a projection \(e\in P\), \([T,e]=(1-e)Te-eT(1-e)\), and the two terms map \(eH\) into \((1-e)H\) and \((1-e)H\) into \(eH\), so \(\|[T,e]\|=\max(\|(1-e)Te\|,\|eT(1-e)\|)\le\alpha\), using also the projection \(1-e\in P\).

Let \(a\in P\) be self-adjoint with \(\|a\|\le1\), and \(E_s=\mathbf 1_{(s,\infty)}(a)\in P\) for \(s\in\mathbb R\). For \(\xi,\eta\in H\), let \(\mu\) be the complex spectral measure with \(\langle f(a)\xi,\eta\rangle=\int f\,d\mu\) for bounded Borel \(f\), concentrated on \([-1,1]\). Since \(\int_{-1}^1\mathbf 1_{(s,\infty)}(\lambda)\,ds=\lambda+1\) for \(\lambda\in[-1,1]\), Fubini's theorem gives \(\langle(a+1)\xi,\eta\rangle=\int_{-1}^1\langle E_s\xi,\eta\rangle\,ds\), and the same with \(T\xi\) or \(T^*\eta\) in place of \(\xi\) or \(\eta\). Hence
\[
\langle[T,a]\xi,\eta\rangle=\langle(a+1)\xi,T^*\eta\rangle-\langle(a+1)T\xi,\eta\rangle=\int_{-1}^1\langle[T,E_s]\xi,\eta\rangle\,ds,
\]
and \(\|[T,a]\|\le2\alpha\). A contraction of \(P\) is \(a_1+ia_2\) with self-adjoint contractions \(a_1,a_2\in P\), so \(g_P(T)\le4\alpha\). By Arveson's distance formula, Corollary 4.5 of the first lesson, and the uniform commutator estimate,
\[
2\operatorname{dist}(T,M)=2\operatorname{dist}(T,P')=\|\operatorname{ad}(T)|_P\|_{\rm cb}\le C\,g_P(T)\le4C\alpha .
\qquad\square
\]

## 4. Remarks

Before [OpenAI-288], the similarity property was known for nuclear C\*-algebras (Bunce, Christensen), for C\*-algebras without tracial states (Haagerup), and for II\(_1\) factors with property \(\Gamma\) (Christensen); see [Ozawa, Theorem 1.3]. Kirchberg had shown that, for each C\*-algebra, the similarity property is equivalent to the property that all derivations into the bounded operators of its representations are inner [Kirchberg]; Theorems 1.2 and 2.1 establish both properties for every C\*-algebra, with explicit constants. The proof in this course follows the structure of [OpenAI-288], with three changes in the classical part: the finitely generated case of the similarity problem is deduced from the row and column estimates (second lesson); Kirchberg's analytic argument is carried out with the three-lines bound, which gives the exponent \(2C\) (third lesson); and the implementation bound \(\frac12\|\Delta\|_{\rm cb}\) of the first lesson, which also yields Arveson's distance formula, replaces a cruder bound. The constants are far from optimal.

## 5. Exercises

**Exercise 5.1.** Let \(A\subseteq B(K)\) be a C\*-algebra with \(1_K\in A\). Show that \(\operatorname{dist}(V,A')\le\frac C2\sup\{\|Va-aV\|:a\in A,\ \|a\|\le1\}\) for every \(V\in B(K)\).

**Exercise 5.2.** Let \(M=\mathbb C1\subseteq B(H)\). Show that \(\alpha_M(T)\) is the supremum of \(\|(1-e)Te\|\) over all projections \(e\) of \(B(H)\), and that \(\alpha_M(T)=0\) exactly when \(T\) is a scalar.

**Exercise 5.3.** Let \(\pi\) be a bounded unital homomorphism of \(A\) into \(B(H)\) and \(u\in A\) unitary. Show that \(\|\pi(u)^n\|\le\|\pi\|^{2C}\) for all \(n\in\mathbb Z\), and give a direct proof of the weaker bound \(\|\pi(u)^n\|\le\|\pi\|\).

**Exercise 5.4.** Deduce from Theorem 2.1 that a bounded unital homomorphism \(\pi\) with \(\|\pi\|<\infty\) maps every self-adjoint element to an operator similar to a self-adjoint one, through one similarity \(S\) for all of them.

## 6. Solutions

**Solution 5.1.** By Corollary 4.5 of the first lesson, \(2\operatorname{dist}(V,A')=\|\operatorname{ad}(V)|_A\|_{\rm cb}\), and \(\operatorname{ad}(V)|_A\) is a bounded derivation for the inclusion representation, so Theorem 1.2 bounds this by \(C\|\operatorname{ad}(V)|_A\|\).

**Solution 5.2.** \(M'=B(H)\). If \(T\) is not scalar, some vector \(\xi\) is not an eigenvector of \(T\), and for the projection \(e\) onto \(\mathbb C\xi\), \((1-e)Te\ne0\). Conversely scalars commute with every \(e\).

**Solution 5.3.** With \(S\) from Theorem 2.1, \(\pi(u)^n=\pi(u^n)=S^{-1}\rho(u^n)S\) with \(\rho(u^n)\) unitary, so \(\|\pi(u)^n\|\le\|S\|\|S^{-1}\|\le\|\pi\|^{2C}\). Directly, \(u^n\) is a unitary of \(A\), of norm \(1\), so \(\|\pi(u^n)\|\le\|\pi\|\).

**Solution 5.4.** With \(S\) from Theorem 2.1, \(S\pi(a)S^{-1}=\rho(a)\) is self-adjoint whenever \(a\) is, because \(\rho\) is a \(*\)-homomorphism.

## References

- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
- [Kirchberg] E. Kirchberg, The derivation problem and the similarity problem are equivalent, Journal of Operator Theory 36 (1996), 59–62. https://jot.theta.ro/jot/archive/1996-036-001/1996-036-001-004.pdf
- [Pisier-degree] G. Pisier, The similarity degree of an operator algebra, St. Petersburg Mathematical Journal 10 (1999). https://arxiv.org/abs/math/9706211
- [Ozawa] N. Ozawa, An invitation to the similarity problems (after Pisier), lecture notes, RIMS, 2006. https://www.kurims.kyoto-u.ac.jp/~narutaka/notes/similarity.pdf
- [CSSW] E. Christensen, A. M. Sinclair, R. R. Smith, S. A. White, Perturbations of C\*-algebraic invariants, Geometric and Functional Analysis 20 (2010), 368–397, Section 2 (the distance property and the derivation problem). https://arxiv.org/abs/0910.1368
