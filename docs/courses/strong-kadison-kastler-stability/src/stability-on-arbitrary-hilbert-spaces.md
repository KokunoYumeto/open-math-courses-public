# Stability on arbitrary Hilbert spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves strong Kadison–Kastler stability, Theorem 2.1 of [Close operator algebras](close-operator-algebras.md), on Hilbert spaces of every dimension. Finite sets of operators and vectors lie in separable restrictions of the two algebras that are still close (Lemma 1.1). On each restriction the separable theorem gives a small unitary, extended by the identity. These unitaries are not chosen compatibly, but their conjugation maps have a pointwise weak limit, a UCP map into the second algebra. The completely positive criterion turns it into one unitary on the whole space (Theorem 2.1). The lesson ends with the consequences for matrix distances and commutants (Corollary 3.1) and a summary of the quantifiers [OpenAI-289, Sections 9 and 10].

We use: [Close operator algebras](close-operator-algebras.md) (Lemma 1.4 and Proposition 2.2); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Proposition 4.1); [Centers and measurable assembly](centers-and-measurable-assembly.md) (Theorem 5.1, with \(\delta_{\rm sep}\)); [Kaplansky's density theorem](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07); the [weak compactness of the unit ball of \(B(H)\)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10); and the [quotient norms of C\*-algebras](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-26) (a \(*\)-homomorphism induces an isometry of the quotient onto its closed range).

## 1. Separable tests

**Lemma 1.1** (separable tests). Let \(M,N\subseteq B(H)\) be unital von Neumann algebras and \(g>d(M,N)\). For finite sets \(E\subseteq M\), \(F\subseteq N\) and \(V\subseteq H\), with \(V\) containing a nonzero vector, there are norm-separable unital C\*-subalgebras \(A\subseteq M\), \(B\subseteq N\) and a nonzero separable closed subspace \(K\subseteq H\) such that:

1. \(E\subseteq A\), \(F\subseteq B\) and \(V\subseteq K\);
2. \(K\) reduces \(A\) and \(B\);
3. \(d(A,B)<g\) and \(d\bigl((A|_K)'',(B|_K)''\bigr)<g\).

The restriction maps \(A\to A|_K\) and \(B\to B|_K\) need not be injective.

**Proof.** Choose \(r\) with \(d(M,N)<r<g\). Put \(A_0=C^*(E\cup\{1\})\) and \(B_0=C^*(F\cup\{1\})\). Given separable \(A_j\subseteq M\) and \(B_j\subseteq N\), choose for each element of a countable dense subset of \((A_j)_1\) an element of \(N_1\) within \(r\), and adjoin all of them to \(B_j\); symmetrically, adjoin to \(A_j\) elements of \(M_1\) within \(r\) of a countable dense subset of \((B_j)_1\). Let \(A_{j+1},B_{j+1}\) be the unital C\*-algebras generated, and \(A,B\) the norm closures of \(\bigcup_jA_j\) and \(\bigcup_jB_j\). They are separable. The unit balls of the stages are dense in the unit balls of the closures (approximate in norm and rescale), so the chosen approximants give \(d(A,B)\le r<g\).

Let \(K\) be the closed span of \(C^*(A\cup B)V\). It is separable, contains \(V\) and reduces both algebras. For \(x\in(A|_K)_1\) and \(s>0\), the quotient norm gives \(a\in A\) with \(a|_K=x\) and \(\|a\|\le1+s\); an element \(b\in B_1\) within \(r\) plus a small slack of \(a/(1+s)\) restricts to an element of \((B|_K)_1\) within \(s/(1+s)+r\) plus that slack of \(x\). Letting \(s\to0\) and exchanging the algebras gives \(d(A|_K,B|_K)\le r\). For a contraction \(y\in(A|_K)''\), Kaplansky's density theorem gives a net of contractions of \(A|_K\) converging strongly to \(y\); approximate each within \(r\) plus a vanishing slack in \((B|_K)_1\), and take a weak operator cluster point, which lies in the unit ball of \((B|_K)''\) and is within \(r\) of \(y\). Exchanging the algebras finishes the proof. \(\square\)

## 2. The main theorem

**Theorem 2.1** (strong Kadison–Kastler stability). For every \(\varepsilon>0\) there is \(\delta>0\) such that, for every Hilbert space \(H\) and unital von Neumann algebras \(M,N\subseteq B(H)\) with \(d(M,N)<\delta\), there is a unitary \(u\in B(H)\) with \(uMu^*=N\) and \(\|u-1\|<\varepsilon\).

**Proof.** *The tolerance.* Let \(a=\min\{\varepsilon/65,10^{-4}\}\) and \(\delta=\min\{1/2,\delta_{\rm sep}(a)\}\), where \(\delta_{\rm sep}\) is the function of Theorem 5.1 of [Centers and measurable assembly](centers-and-measurable-assembly.md). Let \(d(M,N)<\delta\). If \(H=\{0\}\), take \(u=1\). Otherwise fix a unit vector \(\xi_0\in H\) and \(g\) with \(d(M,N)<g<\delta_{\rm sep}(a)\).

*Local conjugations.* Consider the set of quadruples \(i=(E_i,F_i,V_i,k_i)\) with finite \(E_i\subseteq M\), \(F_i\subseteq N\), \(V_i\subseteq H\) containing \(\xi_0\), and \(k_i\in\mathbb N\), directed by inclusion of the three sets and the order of \(k_i\). For each \(i\), Lemma 1.1 gives \(A_i,B_i,K_i\). The algebras \(P_i=(A_i|_{K_i})''\) and \(Q_i=(B_i|_{K_i})''\) are unital von Neumann algebras on the nonzero separable space \(K_i\) with \(d(P_i,Q_i)<g\), so Theorem 5.1 of the previous lesson gives a unitary \(u_i\) of \(K_i\) with \(u_iP_iu_i^*=Q_i\) and \(\|u_i-1\|<a\). Extend it by the identity on \(K_i^\perp\) to a unitary \(U_i\) of \(H\). At every matrix level,
\[
\begin{aligned}
&\|\operatorname{Ad}(U_i)|_M-\mathrm{id}_M\|_{\rm cb}\\
&\quad \le2\|U_i-1\|<2a .\quad(2.1)
\end{aligned}
\]

*Finite tests.* Let \(x\in E_i\). Then \(K_i\) reduces \(x\), and the restriction of \(U_ixU_i^*\) to \(K_i\) is \(u_i(x|_{K_i})u_i^*\in Q_i\), of norm at most \(\|x\|\). By Kaplansky's density theorem there is an element of \(B_i|_{K_i}\), of norm at most \(\|x\|\) plus a small slack, whose coefficients on the finitely many pairs of vectors of \(V_i\) are within \(1/(2k_i)\) of those of \(u_i(x|_{K_i})u_i^*\). Lifting it through the restriction gives \(b_{i,x}\in B_i\subseteq N\) with
\[
\begin{gathered}
\|b_{i,x}\|\le\|x\|+1,\\
\begin{aligned}
&|\langle(U_ixU_i^*-b_{i,x})\xi,\eta\rangle|\\
&\quad <1/k_i\quad(\xi,\eta\in V_i).
\end{aligned}\quad(2.2)
\end{gathered}
\]
These are coefficients on \(H\), since all the vectors lie in \(K_i\).

*A UCP limit.* For each \(x\in M\), the operators \(U_ixU_i^*\) lie in the weakly compact ball of radius \(\|x\|\). By Tychonoff's theorem a subnet satisfies: \(F(x)=\lim_iU_ixU_i^*\) exists in the weak operator topology for every \(x\in M\). Linearity and unitality pass to the limit, positivity at each matrix size is preserved because positive operators form a weakly closed cone, and (2.1) passes to the limit because norm balls are weakly closed:
\[
\|F-\mathrm{id}_M\|_{\rm cb}\le2a .
\]

*The range.* Fix \(x\in M\). Along the subnet, eventually \(x\in E_i\), every fixed pair \(\xi,\eta\in H\) eventually lies in \(V_i\), and \(k_i\to\infty\). So (2.2) and the definition of \(F\) give \(\langle b_{i,x}\xi,\eta\rangle\to\langle F(x)\xi,\eta\rangle\) for all \(\xi,\eta\). The \(b_{i,x}\) lie in \(N\), which is weakly closed, so \(F(x)\in N\). Thus \(F:M\to N\) is UCP; it need not be normal.

*Conclusion.* The inclusion of \(M\) in \(B(H)\) is a faithful normal representation, every element of \(N_1\) is within \(d(M,N)<1/2\) of \(M_1\), and \(2a<10^{-3}\). Proposition 4.1 of the averaging lesson gives a unitary \(u\) with \(uMu^*=N\) and \(\|u-1\|\le32\cdot2a<\varepsilon\). The tolerance \(\delta\) depends only on \(\varepsilon\). \(\square\)

## 3. Consequences and quantifiers

**Corollary 3.1** (matrix distances and commutants). For every \(\varepsilon>0\) there is \(\delta>0\) such that unital von Neumann algebras \(M,N\subseteq B(H)\), on any Hilbert space, with \(d(M,N)<\delta\) satisfy
\[
d_{\rm cb}(M,N)<\varepsilon,\qquad d(M',N')<\varepsilon .
\]

**Proof.** Take \(\delta\) from Theorem 2.1 for \(\varepsilon/2\); the resulting unitary has \(\|u-1\|<\varepsilon/2\), and Proposition 2.2 of [Close operator algebras](close-operator-algebras.md) gives both bounds. \(\square\)

Since \(d\le d_{\rm cb}\), Corollary 3.1 says that the ordinary and the completely bounded distances define the same uniform structure on the unital von Neumann algebras of \(B(H)\), with moduli independent of \(H\), and that taking commutants is uniformly continuous for the ordinary distance. These facts are consequences of the existence of one small implementing unitary. Before that unitary exists, the proof must keep three kinds of control apart: ordinary closeness of unit balls, closeness at every matrix level, and implementation on the given Hilbert space.

The order of the quantifiers is the content of the theorem. For a fixed factor \(M\), a tolerance \(\delta_M(\varepsilon)>0\) valid in all representations of \(M\) would not give \(\inf_M\delta_M(\varepsilon)>0\). Here the tolerance is chosen before the algebras. In the course this uniformity enters through absolute constants: Christensen's theorem, the common-position theorem, the uniform commutator estimate, the graph comparison, the infinitesimal estimates, and the modulus \(\eta_{\rm fin}\) of the finite-factor theorem. The last of these is reused on a corner of a crossed product, and Section 4 of [Centers and measurable assembly](centers-and-measurable-assembly.md) needs one bound for almost every fiber. [OpenAI-289, Section 3] proves the amplification step for II\(_1\) factors by a separate argument, a randomization over free words; this course uses instead the uniform commutator estimate of the course [Kadison's similarity problem](course:kadisons-similarity-problem/the-uniform-commutator-estimate#3-removing-separability), which holds for all von Neumann algebras.

## 4. Exercises

**Exercise 4.1.** Let \(A\subseteq B(H)\) be a norm-separable C\*-algebra and \(V\subseteq H\) finite. Show that the closed span of \(C^*(A\cup\{1\})V\) is separable and reduces \(A\).

**Exercise 4.2.** Let \(H\) be separable. Show that Theorem 2.1 for such \(H\) follows directly from Theorem 5.1 of the previous lesson, without the limit argument.

**Exercise 4.3.** Show that the pointwise weak limit \(F\) in the proof of Theorem 2.1 need not be multiplicative in general. On \(H=\ell^2(\mathbb Z)\otimes\ell^2(\mathbb N)\), with \(S\) the bilateral shift, find unitaries \(U_m\) with \(U_m(S\otimes1)U_m^*=S^m\otimes1\), and compute the weak limits of the conjugations of \(x=S\otimes1\) and of \(x^*x\).

**Exercise 4.4.** Let \(\delta\) be given by Theorem 2.1 for \(\varepsilon/2\). Show that \(d(M,N)<\delta\) implies \(d(Z(M),Z(N))<\varepsilon\).

## 5. Solutions

**Solution 4.1.** \(C^*(A\cup\{1\})\) is norm separable, so the set of vectors \(cv\), with \(c\) in a countable dense subset and \(v\in V\), is countable with dense span in the closed span. The closed span is invariant under the self-adjoint set \(A\), hence reducing.

**Solution 4.2.** For separable \(H\), Theorem 5.1 of the previous lesson applies to \(M\) and \(N\) themselves, with \(a=\varepsilon\).

**Solution 4.3.** Decomposing \(\mathbb Z\) into residue classes modulo \(m\) shows that \(S^m\) is unitarily equivalent to \(S\otimes1_{\mathbb C^m}\); so \(S^m\otimes1\) and \(S\otimes1\) are both bilateral shifts of infinite multiplicity, and are unitarily equivalent by some \(U_m\). As \(m\to\infty\), \(S^m\otimes1\to0\) in the weak operator topology, so any pointwise weak limit \(F\) of the maps \(\operatorname{Ad}U_m\) has \(F(x)=0\), while \(F(x^*x)=F(1)=1\ne F(x)^*F(x)\). The limit is UCP but not multiplicative.

**Solution 4.4.** The unitary \(u\) of Theorem 2.1 satisfies \(uZ(M)u^*=Z(N)\) and \(\|u-1\|<\varepsilon/2\), and Lemma 1.5 of [Close operator algebras](close-operator-algebras.md) gives \(d(Z(M),Z(N))\le2\|u-1\|<\varepsilon\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Sections 9 and 10. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
