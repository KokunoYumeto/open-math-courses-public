# The double commutant theorem

*Originally written by Claude Opus 5.5 (Anthropic), September 2026, with a separate historical AI spot-check. GPT-6.1 Sol (OpenAI), at the Ultra setting, read, replayed and revised the full lesson and all eight original solutions, supplied the probability-product and polar-limit arguments, and compared the exact programme prerequisites, October 2026. Public domain (CC0).*

This lesson proves von Neumann's double commutant theorem and builds the first tools that rest on it. Let \(M\) be a \(*\)-algebra of operators on a Hilbert space \(H\). The theorem says that \(M\) is dense in its bicommutant \(M''\) for each of the six usual operator topologies, once the projection onto the subspace \([MH]\) is split off. In particular, a nondegenerate \(*\)-algebra satisfies \(M=M''\) exactly when it is closed in one of these topologies. So an algebraic condition and a topological condition describe the same algebras, the von Neumann algebras, and later lessons use both descriptions.

From the theorem we build the basic toolkit: amplification by copies of a Hilbert space, direct sums, reduced and induced algebras, the polar decomposition inside the algebra, closed one-sided ideals, cyclic and separating vectors, \(\sigma\)-finiteness, and positive normal functionals written as sums of vector functionals. The degenerate case of the theorem is reduced to the nondegenerate case by restricting to the subspace \([MH]\). Closed one-sided ideals are handled with an explicit approximate unit. Examples show which hypotheses cannot be dropped, and every exercise has a complete solution.

We assume basic Hilbert space theory and the continuous functional calculus, as in the lesson [C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md). The remaining prerequisites are stated under *Results used from other lessons*, with full programme proofs. The optional convex-set extension in Remark 1.4 is explicitly unused and unproved here.

The commutant records every bounded operator compatible with the algebra. The double commutant theorem identifies that algebraic condition with operator-topology closure. The proof below handles arbitrary Hilbert spaces and nonunital algebras; freely readable comparisons are Blackadar and Peterson’s notes.

## Conventions

Hilbert spaces are complex. No separability is assumed, and the zero space is allowed. Inner products are linear in the first variable.

\(B(H)\) is the algebra of bounded operators on \(H\), and \(K(H)\) is the ideal of compact operators. A *projection* is an operator \(p\) with \(p=p^*=p^2\). For projections, \(p\le q\) means \(pH\subseteq qH\), or equivalently \(p=pq\). For \(\xi,\eta\in H\) we write \(\omega_{\xi,\eta}(x)=\langle x\xi,\eta\rangle\), \(\omega_\xi=\omega_{\xi,\xi}\), and \(\theta_{\xi,\eta}\) for the rank-one operator \(\zeta\mapsto\langle\zeta,\eta\rangle\xi\). For \(S\subseteq B(H)\) and \(X\subseteq H\), \([SX]\) is the closed linear span of \(\{s\xi:s\in S,\ \xi\in X\}\), and \([X]\) is the closed linear span of \(X\). An operator \(x\) is positive, \(x\ge0\), when \(\langle x\xi,\xi\rangle\ge0\) for all \(\xi\); \(M_+\) is the set of positive elements of \(M\). A sum over an arbitrary index set is the limit of the net of its finite partial sums.

## Results used from other lessons

The functional-analytic facts below are proved in the earlier lessons named with them. The probability product theorem is proved in Section 9, before its use in Exercise 9.9. The labels in bold are used throughout the lesson.

- **(H) Hilbert spaces** ([Hilbert spaces and compact operators](hilbert-spaces-and-compact-operators.md)).
  1. *Projection theorem* ([Theorem 2.2](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-02)). In a real or complex Hilbert space \(H\), every closed subspace \(L\) gives an orthogonal decomposition \(H=L\oplus L^\perp\). Hence the closure of any subspace \(Y\) is \((Y^\perp)^\perp\).
  2. *Riesz representation* ([Theorem 2.3](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-02)). Every bounded linear functional \(f\) on \(H\) has the form \(f(\xi)=\langle\xi,\eta\rangle\) for a unique \(\eta\in H\).
  3. *Bounded sesquilinear forms* ([Theorem 3.1](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-03)). If \(B\) is a sesquilinear form on \(H\) with \(\lvert B(\xi,\eta)\rvert\le C\|\xi\|\,\|\eta\|\), then there is a unique \(t\in B(H)\) with \(B(\xi,\eta)=\langle t\xi,\eta\rangle\), and \(\|t\|\le C\). If moreover \(B(\xi,\xi)\ge0\) for all \(\xi\), then \(t\ge0\), because \(\langle t\xi,\xi\rangle=B(\xi,\xi)\).
  4. *Cauchy–Schwarz inequality* ([Proposition 1.1(3)](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-01)). Let \(B\) be a sesquilinear form on a complex vector space with \(B(\eta,\xi)=\overline{B(\xi,\eta)}\) and \(B(\xi,\xi)\ge0\) for all \(\xi,\eta\). Then \(\lvert B(\xi,\eta)\rvert^2\le B(\xi,\xi)\,B(\eta,\eta)\).
- **(C) C\*-algebra facts.** These are proved in the lesson on C\*-algebras: see [the continuous functional calculus](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-07), [the calculus without an identity](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-08), [working with the order and square roots](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-16) and [isometry of injective homomorphisms](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-14).
  1. Let \(A\subseteq B(H)\) be a norm-closed \(*\)-subalgebra and \(a\in A\) self-adjoint. For \(g\) continuous on the spectrum of \(a\), with \(g(0)=0\) when \(1\notin A\), the operator \(g(a)\) lies in \(A\). The map \(g\mapsto g(a)\) is a \(*\)-homomorphism that preserves order and the supremum norm on the spectrum. Each \(g(a)\) commutes with every operator that commutes with \(a\). The case \(1\notin A\) is used only in Exercise 6.2.
  2. Positive square roots exist and are unique.
  3. If \(m1\le a\le b\) with \(m>0\), then \(a\) and \(b\) are invertible and \(b^{-1}\le a^{-1}\): inversion reverses order.
  4. An injective \(*\)-homomorphism between C\(^*\)-algebras is isometric, so its range is norm closed.
- **(U) Unitaries.** Every element of a unital norm-closed \(*\)-subalgebra \(A\) of \(B(H)\) is a combination \(\sum_{k=1}^4\lambda_ku_k\) of four unitaries \(u_k\in A\) with scalar coefficients \(\lambda_k\); see [unitaries span a unital C\*-algebra](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-10). So an operator that commutes with every unitary of \(A\) commutes with all of \(A\).
- **(P) Polar decomposition** (Proposition 5.2 of [The spectral theorem for bounded self-adjoint operators](the-spectral-theorem-for-bounded-self-adjoint-operators.md), cited below as *the spectral-theorem lesson*). Its [full polar-decomposition proof](the-spectral-theorem-for-bounded-self-adjoint-operators.md#oa-fnd-st-05) shows that every \(x\in B(H)\) can be written \(x=u|x|\), where \(|x|=(x^*x)^{1/2}\) and \(u\) is a partial isometry with \(\ker u=\ker x\). Uniqueness is proved again in Lemma 7.1.
- **(V) Vigier's theorem** (the spectral-theorem lesson, Theorem 6.1). The [full monotone-net proof](the-spectral-theorem-for-bounded-self-adjoint-operators.md#oa-fnd-st-06) shows that a norm-bounded increasing net of positive operators converges strongly to its least upper bound. If the net lies in a von Neumann algebra \(M\), so does the limit, because \(M\) is strongly closed (Proposition 2.4).
- **(K) Compact operators** (the Hilbert-space lesson, Theorems 5.1, 6.2 and 7.1(4)). \(K(H)\) is a norm-closed two-sided ideal of \(B(H)\), and it is the norm closure of the finite-rank operators. Every positive compact operator \(a\) has the form \(a=\sum_n\alpha_n\theta_{\varepsilon_n,\varepsilon_n}\), with norm convergence, for an orthonormal family \((\varepsilon_n)\), finite or countably infinite, and numbers \(\alpha_n>0\) that tend to \(0\) if there are infinitely many. Moreover \(\sigma(a)\subseteq\{\alpha_n\}\cup\{0\}\).
- **Set theory and measure theory.** Zorn's lemma ([Theorem 1.1](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-01), with its full choice-to-well-ordering-to-Zorn proof). For every family \((\Gamma_i,\mu_i)_{i\in I}\) of probability spaces, the product \(\Gamma=\prod_i\Gamma_i\) carries a unique probability measure \(\mu\) on the product \(\sigma\)-algebra with \(\mu\big(\prod_{i\in F}B_i\times\prod_{i\notin F}\Gamma_i\big)=\prod_{i\in F}\mu_i(B_i)\) for every finite \(F\subseteq I\) and all measurable \(B_i\subseteq\Gamma_i\). The [probability product theorem in Section 9](#oa-fnd-bi-18) proves this statement, including uniqueness and a complete extension. Its proof uses the full Carathéodory proof, Theorem 1.1, and arbitrary-measure monotone convergence, Theorem 2.1, in *Measure and Hilbert space tools for Haar integration*. The product measure is used only in Exercise 9.9.

## 1. Operator topologies

Six topologies on \(B(H)\) are used throughout. This section compares them and shows that on linear subspaces they produce at most two different closures.

**Definition 1.1.** Each of the six topologies below is the locally convex topology on \(B(H)\) given by a family of seminorms. In the table, \((\xi_n)\) and \((\eta_n)\) are sequences in \(H\) with \(\sum_n\|\xi_n\|^2<\infty\) and \(\sum_n\|\eta_n\|^2<\infty\).

| topology | seminorms |
|---|---|
| weak | \(x\mapsto\lvert\langle x\xi,\eta\rangle\rvert\) |
| strong | \(x\mapsto\lVert x\xi\rVert\) |
| strong\(^*\) | \(x\mapsto(\lVert x\xi\rVert^2+\lVert x^*\xi\rVert^2)^{1/2}\) |
| \(\sigma\)-weak | \(x\mapsto\lvert\sum_n\langle x\xi_n,\eta_n\rangle\rvert\) |
| \(\sigma\)-strong | \(x\mapsto(\sum_n\lVert x\xi_n\rVert^2)^{1/2}\) |
| \(\sigma\)-strong\(^*\) | \(x\mapsto(\sum_n\lVert x\xi_n\rVert^2+\lVert x^*\xi_n\rVert^2)^{1/2}\) |

The \(\sigma\)-weak topology is also called the *ultraweak* topology. With \(\omega=\sum_n\omega_{\xi_n}\), the \(\sigma\)-strong and \(\sigma\)-strong\(^*\) seminorms read \(\omega(x^*x)^{1/2}\) and \((\omega(x^*x)+\omega(xx^*))^{1/2}\). By Theorem 10.1, every positive \(\sigma\)-weakly continuous functional on \(B(H)\) has this form \(\omega\). For a set \(S\subseteq B(H)\) we write \(\overline S^{\,w}\), \(\overline S^{\,s}\), \(\overline S^{\,s*}\), \(\overline S^{\,\sigma w}\), \(\overline S^{\,\sigma s}\), \(\overline S^{\,\sigma s*}\) for its closures.

**Lemma 1.2** (elementary facts).

(a) *One seminorm is enough.* In the \(\sigma\)-strong and \(\sigma\)-strong\(^*\) topologies, finitely many seminorms are dominated by a single seminorm of the same kind: concatenate the sequences. In the strong and strong\(^*\) topologies, the seminorms of finitely many vectors \(\xi_1,\dots,\xi_m\) are dominated by \((\sum_{j=1}^m\lVert x\xi_j\rVert^2)^{1/2}\), respectively \((\sum_{j=1}^m\lVert x\xi_j\rVert^2+\lVert x^*\xi_j\rVert^2)^{1/2}\), the \(\sigma\)-type seminorm of a finite sequence. So in each of the four strong-type topologies, every neighbourhood of \(a\) contains a set \(\{x:p(x-a)<\varepsilon\}\) for one such seminorm \(p\).

(b) *Comparisons.* A sequence with one nonzero term shows that each \(\sigma\)-topology is finer than its plain counterpart. The Cauchy–Schwarz inequality \(\lvert\sum_n\langle x\xi_n,\eta_n\rangle\rvert\le(\sum_n\|x\xi_n\|^2)^{1/2}(\sum_n\|\eta_n\|^2)^{1/2}\) shows that the \(\sigma\)-strong topology is finer than the \(\sigma\)-weak one; in the same way the strong topology is finer than the weak one. Each starred topology is finer than its unstarred version. So the weak topology is the coarsest of the six and the \(\sigma\)-strong\(^*\) topology is the finest, and all six are coarser than the norm topology. A finer topology has smaller closures:
\[
\begin{gathered}
\overline S^{\,\sigma s*}\subseteq\overline S^{\,\sigma s}\subseteq\overline S^{\,\sigma w}\subseteq\overline S^{\,w},\\
\overline S^{\,\sigma s*}\subseteq\overline S^{\,s*}\subseteq\overline S^{\,s}\subseteq\overline S^{\,w},\\
\overline S^{\,\sigma s}\subseteq\overline S^{\,s}.
\end{gathered}
\]

(c) *Continuity of the operations.* Addition and scalar multiplication are continuous. For fixed \(a,b\in B(H)\), the map \(x\mapsto axb\) is continuous in all six topologies. Indeed \(\|axb\xi_n\|\le\|a\|\,\|x(b\xi_n)\|\), \(\langle axb\xi_n,\eta_n\rangle=\langle x(b\xi_n),a^*\eta_n\rangle\), and \(\|(axb)^*\xi_n\|\le\|b\|\,\|x^*(a^*\xi_n)\|\), where \((b\xi_n)\) and \((a^*\eta_n)\) are again square summable. The adjoint \(x\mapsto x^*\) is continuous for the weak, \(\sigma\)-weak, strong\(^*\) and \(\sigma\)-strong\(^*\) topologies, because it maps their seminorms to seminorms of the same kind. (When \(\dim H=\infty\) it is not \(\sigma\)-strongly continuous. For an orthonormal sequence \((\xi_n)\), \(\theta_{\xi_1,\xi_n}\to0\) \(\sigma\)-strongly, while \(\|\theta_{\xi_1,\xi_n}^*\xi_1\|=1\). The same example shows that it is not strongly continuous. We do not need this.)

(d) *Bounded nets.* Let \(x_\lambda\to x\) strongly, with \(C=\sup_\lambda\|x_\lambda\|+\|x\|<\infty\). Then \(x_\lambda\to x\) \(\sigma\)-strongly. Given \((\xi_n)\) and \(\varepsilon>0\), choose \(N\) with \(C^2\sum_{n>N}\|\xi_n\|^2<\varepsilon^2/2\); then \(\sum_n\|(x_\lambda-x)\xi_n\|^2<\varepsilon^2\) as soon as the finitely many terms with \(n\le N\) add up to less than \(\varepsilon^2/2\). If moreover \(x_\lambda^*\to x^*\) strongly, the same argument gives \(\sigma\)-strong\(^*\) convergence. A bounded weakly convergent net converges \(\sigma\)-weakly, by the same tail estimate.

(e) *Increasing nets.* If \(0\le x_\lambda\) increases and \(\sup_\lambda\|x_\lambda\|<\infty\), then \(x_\lambda\) converges strongly to its least upper bound, by Vigier's theorem (V). The operators are self-adjoint, so by (d) the convergence is also \(\sigma\)-strong\(^*\) and \(\sigma\)-weak.

**Lemma 1.3** (closures of subspaces). Let \(S\subseteq B(H)\) be a complex linear subspace. Then

1. \(\overline S^{\,w}=\overline S^{\,s}=\overline S^{\,s*}\), and
2. \(\overline S^{\,\sigma w}=\overline S^{\,\sigma s}=\overline S^{\,\sigma s*}\).

**Proof.** (2) By Lemma 1.2(b), \(\overline S^{\,\sigma s*}\subseteq\overline S^{\,\sigma s}\subseteq\overline S^{\,\sigma w}\). For the reverse inclusion let \(a\in\overline S^{\,\sigma w}\), let \((\xi_n)\) be square summable, and let \(\varepsilon>0\). By Lemma 1.2(a), it is enough to find \(x\in S\) with \(\sum_n\|(a-x)\xi_n\|^2+\|(a-x)^*\xi_n\|^2<\varepsilon^2\).

Let \(\mathcal K=\ell^2(\mathbb N;H)\oplus\ell^2(\mathbb N;H)\). We regard it as a *real* Hilbert space, with inner product \(\operatorname{Re}\langle\cdot,\cdot\rangle\). The map \(\Phi(x)=((x\xi_n)_n,(x^*\xi_n)_n)\) from \(B(H)\) to \(\mathcal K\) is real linear, and \(\|\Phi(x)\|^2\le2\|x\|^2\sum_n\|\xi_n\|^2\). It is not complex linear, because of the adjoint. \(\Phi(S)\) is a real subspace of \(\mathcal K\). By the projection theorem (H), its closure is the set of vectors that are real-orthogonal to \(\Phi(S)^\perp\), the real orthogonal complement.

Take \((\eta,\zeta)\in\Phi(S)^\perp\), with \(\eta=(\eta_n)\) and \(\zeta=(\zeta_n)\). For \(x\in S\) put \(A(x)=\sum_n\langle x\xi_n,\eta_n\rangle\) and \(B(x)=\sum_n\langle x^*\xi_n,\zeta_n\rangle\). Orthogonality to \(\Phi(x)\) says \(\operatorname{Re}A(x)+\operatorname{Re}B(x)=0\). The operator \(ix\) also lies in \(S\), and \((ix)^*=-ix^*\). So orthogonality to \(\Phi(ix)\) says \(\operatorname{Re}(iA(x))+\operatorname{Re}(-iB(x))=0\), that is, \(\operatorname{Im}A(x)=\operatorname{Im}B(x)\). Together, \(A(x)=-\overline{B(x)}\). Since \(\overline{B(x)}=\sum_n\langle\zeta_n,x^*\xi_n\rangle=\sum_n\langle x\zeta_n,\xi_n\rangle\), the complex linear functional
\[
\begin{gathered}
f(x)\\
=\sum_n\langle x\xi_n,\eta_n\rangle+\sum_n\langle x\zeta_n,\xi_n\rangle
\end{gathered}
\tag{1.1}
\]
vanishes on \(S\). It is \(\sigma\)-weakly continuous, being the sum of two functionals of the form \(\sum_n\langle x\alpha_n,\beta_n\rangle\) with square-summable sequences. Since \(f\) vanishes on \(S\) and \(a\) lies in the \(\sigma\)-weak closure of \(S\), also \(f(a)=0\). Reading the computation backwards, \(\operatorname{Re}A(a)+\operatorname{Re}B(a)=0\): the vector \(\Phi(a)\) is real-orthogonal to \((\eta,\zeta)\). As \((\eta,\zeta)\) was arbitrary, \(\Phi(a)\) lies in the closure of \(\Phi(S)\). Choose \(x\in S\) with \(\|\Phi(a)-\Phi(x)\|<\varepsilon\). Since \(\Phi(a)-\Phi(x)=\Phi(a-x)\), this is the required estimate.

(1) Run the same argument with finitely many vectors \(\xi_1,\dots,\xi_m\) in place of a square-summable sequence, starting from \(a\) in the weak closure of \(S\). The functional \(f\) is then weakly continuous, so again \(f(a)=0\). \(\square\)

*Remark 1.4 (unused extension, not proved here).* The equalities of part (2) also hold for convex sets, by the separation theory of locally convex spaces. This stronger statement is background context and is never used in this lesson. The linear-subspace result needed below has the full real-Hilbert projection proof above. The two triples of closures can differ for a subspace: [Exercise 1.5](#oa-fnd-bi-01) gives a subspace that is \(\sigma\)-weakly closed but not weakly closed. For \(*\)-subalgebras all six closures agree ([Theorem 4.4](#oa-fnd-bi-07)).

**Exercise 1.5** (medium; the two triples of closures differ for subspaces). On \(H=\ell^2(\mathbb N)\) with basis \((\delta_n)\), let \(\omega(x)=\sum_n2^{-n}\langle x\delta_n,\delta_n\rangle\). Show that \(\ker\omega\) is \(\sigma\)-weakly closed but not weakly closed. So Lemma 1.3 cannot be extended to all six topologies for subspaces, while [Theorem 4.4](#oa-fnd-bi-07) does this for \(*\)-subalgebras.

*Solution.* \(\omega\) is \(\sigma\)-weakly continuous, so its kernel is \(\sigma\)-weakly closed.

*A linear functional with closed kernel is continuous.* Let \(f\neq0\) be a linear functional on \(B(H)\) whose kernel is weakly closed, and pick \(x_0\) with \(f(x_0)=1\). There are weak seminorms \(p_1,\dots,p_k\) and \(\delta>0\) such that the set \(x_0+U\), where \(U=\{x:p_j(x)<\delta\text{ for all }j\}\), misses \(\ker f\). The set \(U\) is balanced: \(tU\subseteq U\) for \(|t|\le1\). If some \(u\in U\) had \(|f(u)|\ge1\), then \(u'=-u/f(u)\in U\) and \(f(x_0+u')=0\), which is impossible. So \(|f|<1\) on \(U\), and by homogeneity \(|f(x)|\le\delta^{-1}\max_jp_j(x)\). So \(f\) is weakly continuous.

*\(\omega\) is not weakly continuous.* Otherwise there would be vectors \(\xi_j,\eta_j\) (\(j=1,\dots,k\)) and \(C>0\) with \(|\omega(x)|\le C\max_j|\langle x\xi_j,\eta_j\rangle|\). The span of \(\delta_1,\dots,\delta_{k+1}\) has dimension \(k+1\), so it contains a nonzero \(v\) orthogonal to \(\xi_1,\dots,\xi_k\). For \(x=\theta_{v,v}\), \(\langle x\xi_j,\eta_j\rangle=\langle\xi_j,v\rangle\langle v,\eta_j\rangle=0\) for all \(j\), while \(\omega(x)=\sum_n2^{-n}|\langle v,\delta_n\rangle|^2>0\). This is a contradiction. By the previous paragraph, \(\ker\omega\) is not weakly closed. \(\square\)

## 2. Commutants and von Neumann algebras

The commutant of a set of operators is the algebraic side of the theorem. This section collects its basic properties and the definitions built on it.

For \(S\subseteq B(H)\), the *commutant* is \(S'=\{y\in B(H):ys=sy\text{ for all }s\in S\}\), and \(S''=(S')'\), \(S'''=(S'')'\), and so on.

**Proposition 2.1.** Let \(S,T\subseteq B(H)\).

1. \(S'\) is a subalgebra of \(B(H)\) that contains \(1\). It is closed in the weak topology, hence in each of the six topologies of Section 1 and in norm.
2. \(S\subseteq S''\). If \(S\subseteq T\), then \(T'\subseteq S'\). Moreover \(S'=S'''\). So all commutants of odd order equal \(S'\), and all commutants of even order, from the second on, equal \(S''\).
3. \((S\cup T)'=S'\cap T'\).
4. If \(S^*=S\), then \(S'\) is a \(*\)-subalgebra with \((S')''=S'\). In particular \(S''\) is a \(*\)-subalgebra with \((S'')''=S''\) that contains \(S\). Every \(*\)-subalgebra \(N\) with \(S\subseteq N=N''\) contains \(S''\).
5. (*Invariant subspaces.*) Let \(S^*=S\), let \(L\subseteq H\) be a closed subspace, and let \(p\) be its projection. Then \(SL\subseteq L\) if and only if \(p\in S'\). In that case \(SL^\perp\subseteq L^\perp\) as well.

**Proof.** (1) If \(y_1,y_2\in S'\) and \(s\in S\), then \(y_1y_2s=y_1sy_2=sy_1y_2\). Linear combinations are handled the same way, and \(1\in S'\). Let \(y_\lambda\in S'\) converge weakly to \(y\). For \(s\in S\) and \(\xi,\eta\in H\),
\[
\begin{gathered}
\langle(ys-sy)\xi,\eta\rangle\\
=\lim_\lambda\big(\langle y_\lambda(s\xi),\eta\rangle-\langle y_\lambda\xi,s^*\eta\rangle\big)\\
=\lim_\lambda\langle(y_\lambda s-sy_\lambda)\xi,\eta\rangle\\
=0 .
\end{gathered}
\]
So \(y\in S'\). The other five topologies and the norm topology are finer than the weak one ([Lemma 1.2](#oa-fnd-bi-01)(b)), so \(S'\) is closed in them too.

(2) Each \(s\in S\) commutes with every element of \(S'\), so \(s\in S''\). The reversal of inclusions is immediate from the definition. Applying the first statement to \(S'\) gives \(S'\subseteq S'''\). Applying the reversal to \(S\subseteq S''\) gives \(S'''\subseteq S'\).

(3) This is the definition.

(4) Let \(y\in S'\) and \(s\in S\). Then \(s^*\in S\), so \(ys^*=s^*y\). Taking adjoints, \(sy^*=y^*s\). So \(y^*\in S'\), and \(S'\) is a \(*\)-subalgebra by (1). Next, \((S')''=(S'')'=S'''=S'\) by (2). The set \(S'\) is self-adjoint, so the same statements hold for \(S''=(S')'\). Finally, if \(S\subseteq N=N''\), then (2) gives \(S''\subseteq N''=N\).

(5) Suppose \(SL\subseteq L\). For \(\eta\in L^\perp\), \(\zeta\in L\) and \(s\in S\) we have \(\langle s\eta,\zeta\rangle=\langle\eta,s^*\zeta\rangle=0\), because \(s^*\in S\). So \(SL^\perp\subseteq L^\perp\). Hence, for every \(\xi\), \(sp\xi\in L\) and \(s(1-p)\xi\in L^\perp\). The first gives \(psp=sp\), the second \(ps(1-p)=0\), that is \(ps=psp\). So \(ps=sp\). Conversely, if \(p\in S'\), then \(s(p\xi)=p(s\xi)\in L\). \(\square\)

*Remark 2.2* (non-self-adjoint sets). Part (4) needs \(S^*=S\). On \(\mathbb C^2\) let \(N\) be the matrix unit with \(Ne_2=e_1\) and \(Ne_1=0\), and \(S=\{N\}\). A direct computation gives \(S'=\{\alpha1+\beta N\}\), and then \(S''=\{1,N\}'=S'\). This algebra contains \(N\) but not \(N^*\).

**Definition 2.3.** A *\(*\)-subalgebra* \(M\) of \(B(H)\) is a subalgebra closed under adjoints. It is *nondegenerate* if \([MH]=H\). We call a \(*\)-subalgebra \(M\) with \(M=M''\) a *von Neumann algebra*, and write \(\{M,H\}\) when the Hilbert space matters. The *centre* of \(M\) is \(Z(M)=M\cap M'\), and \(M\) is a *factor* if \(Z(M)=\mathbb C1\). For a self-adjoint set \(S\subseteq B(H)\) we say that \(S''\) is *generated* by \(S\). By [Proposition 2.1](#oa-fnd-bi-02)(4), \(S''\) is a von Neumann algebra, and every von Neumann algebra that contains \(S\) also contains \(S''\).

Two von Neumann algebras \(\{M_1,H_1\}\) and \(\{M_2,H_2\}\) are *spatially isomorphic* if there is a unitary \(U:H_1\to H_2\) (an isometry of \(H_1\) onto \(H_2\)) with \(UM_1U^*=M_2\); the map \(x\mapsto UxU^*\) is then a *spatial isomorphism*. They are *isomorphic* if there is a bijective linear map \(\pi:M_1\to M_2\) that is multiplicative and satisfies \(\pi(x^*)=\pi(x)^*\). A spatial isomorphism is an isomorphism, but not conversely ([Example 5.5](#oa-fnd-bi-15)).

**Proposition 2.4.**

1. For a \(*\)-subalgebra \(M\), \([MH]^\perp=\{\xi\in H:x\xi=0\text{ for all }x\in M\}\). So \(M\) is nondegenerate exactly when no nonzero vector is killed by all of \(M\). Every \(*\)-subalgebra that contains \(1\) is nondegenerate.
2. A von Neumann algebra \(M\) contains \(1\), is nondegenerate, and is closed in norm and in all six topologies. So it is a nondegenerate norm-closed \(*\)-algebra. \(M'\) is a von Neumann algebra, \(Z(M)\) is a commutative von Neumann algebra, and \(Z(M')=Z(M)\). In particular \(M\) is a factor if and only if \(M'\) is.
3. A spatial isomorphism carries commutants to commutants and centres to centres: \(UM_1'U^*=M_2'\) and \(UZ(M_1)U^*=Z(M_2)\).
4. \(B(H)'=\mathbb C1\). So \(B(H)\) and \(\mathbb C1\) are factors, each the commutant of the other.

**Proof.** (1) A vector \(\eta\) is orthogonal to every \(x\xi\) exactly when \(x^*\eta=0\) for every \(x\in M\). As \(M^*=M\), this says \(x\eta=0\) for every \(x\in M\). If \(1\in M\), then \(\eta=1\eta=0\).

(2) \(1\in M'\) gives \(1\in M''=M\), and (1) gives nondegeneracy. \(M=(M')'\) is a commutant, so it is closed by [Proposition 2.1](#oa-fnd-bi-02)(1). \(M'\) is the commutant of the self-adjoint set \(M\), so it is a von Neumann algebra by [Proposition 2.1](#oa-fnd-bi-02)(4). Also \(Z(M)=M''\cap M'=(M'\cup M)'\) by [Proposition 2.1](#oa-fnd-bi-02)(3); this is the commutant of a self-adjoint set, hence a von Neumann algebra. It is commutative, because elements of \(M'\) commute with elements of \(M\). Finally \(Z(M')=M'\cap M''=M'\cap M=Z(M)\).

(3) For \(y\in B(H_1)\), \(y\) commutes with every \(x\in M_1\) if and only if \(UyU^*\) commutes with every \(UxU^*\in M_2\). So \(UM_1'U^*=M_2'\), and intersecting with \(UM_1U^*=M_2\) gives the centres.

(4) If \(H=\{0\}\) there is nothing to prove. Let \(y\in B(H)'\). For \(\xi,\eta\in H\), \(y\theta_{\xi,\eta}=\theta_{y\xi,\eta}\) and \(\theta_{\xi,\eta}y=\theta_{\xi,y^*\eta}\), so \(\theta_{y\xi,\eta}=\theta_{\xi,y^*\eta}\). Fix a unit vector \(\eta\) and apply both operators to \(\eta\): \(y\xi=\langle\eta,y^*\eta\rangle\xi=\langle y\eta,\eta\rangle\xi\) for every \(\xi\). So \(y\) is a scalar. Trivially \((\mathbb C1)'=B(H)\). \(\square\)

## 3. Amplification

To pass from approximation at one vector to approximation at a square-summable sequence of vectors, we replace \(H\) by a direct sum of copies of \(H\). Operators on the larger space are described by matrices with entries in \(B(H)\).

Let \(I\) be a nonempty set and \(\tilde H=\ell^2(I;H)\), the space of families \((\xi_i)_{i\in I}\) in \(H\) with \(\sum_i\|\xi_i\|^2<\infty\). It is the direct sum of copies of \(H\) indexed by \(I\). Let \(U_j:H\to\tilde H\) put a vector in place \(j\) and zeros elsewhere. Then \(U_i^*U_j=\delta_{ij}1_H\), \(U_i^*(\xi_k)_k=\xi_i\), and \(\sum_iU_iU_i^*=1\), with unconditional convergence on each vector: \(\|\tilde\xi-\sum_{i\in F}U_iU_i^*\tilde\xi\|^2=\sum_{i\notin F}\|\xi_i\|^2\to0\). For \(X\in B(\tilde H)\) define its *matrix entries*
\[
X_{ij}=U_i^*XU_j\in B(H).
\tag{3.1}
\]

**Lemma 3.1** (matrices).

1. \(X\) is determined by its entries, and \(\|X_{ij}\|\le\|X\|\).
2. \((\alpha X+\beta Y)_{ij}=\alpha X_{ij}+\beta Y_{ij}\) and \((X^*)_{ij}=(X_{ji})^*\). For each \(\xi\in H\),
\[
(XY)_{ij}\xi=\sum_kX_{ik}Y_{kj}\xi ,
\tag{3.2}
\]
with unconditional convergence in norm.
3. The operators \(E_{ij}=U_iU_j^*\) (the *matrix units*) have entries \((E_{ij})_{kl}=\delta_{ki}\delta_{jl}1_H\).

**Proof.** (1) \(\langle XU_j\xi,U_i\eta\rangle=\langle X_{ij}\xi,\eta\rangle\), and the vectors \(U_j\xi\) span a dense subspace (the finitely supported families). If all entries vanish, \(\langle X\zeta,\zeta'\rangle=0\) on this dense subspace, so \(X=0\). The norm bound holds because \(U_i^*\) and \(U_j\) have norm at most \(1\).

(2) Linearity is clear, and \((X^*)_{ij}=U_i^*X^*U_j=(U_j^*XU_i)^*\). For the product, \[
\begin{gathered}
(XY)_{ij}\xi\\
=U_i^*X\big(\sum_kU_kU_k^*\big)YU_j\xi\\
=\sum_kU_i^*XU_k\,U_k^*YU_j\xi.
\end{gathered}
\] The sum converges unconditionally because \(\sum_kU_kU_k^*\eta\) does and \(U_i^*X\) is bounded.

(3) \(U_k^*U_iU_j^*U_l=\delta_{ki}\delta_{jl}1_H\). \(\square\)

The *amplification* \(\pi:B(H)\to B(\tilde H)\) is
\[
\begin{gathered}
\pi(x)(\xi_i)_i\\
=(x\xi_i)_i,\\
\text{that is,}\\
\pi(x)_{ij}\\
=\delta_{ij}x .
\end{gathered}
\tag{3.3}
\]
It is an injective unital \(*\)-homomorphism with \(\|\pi(x)\|=\|x\|\), and \(\pi(x)U_j=U_jx\), \(U_i^*\pi(x)=xU_i^*\).

**Proposition 3.2** (the range of the amplification). An operator \(X\in B(\tilde H)\) lies in \(\pi(B(H))\) if and only if it commutes with every matrix unit \(E_{ij}\).

**Proof.** \(\pi(x)E_{ij}=U_ixU_j^*=E_{ij}\pi(x)\). Conversely, let \(X\) commute with every \(E_{ij}\). Since \(U_j=E_{jj}U_j\),
\[
X_{ij}=U_i^*XE_{jj}U_j=U_i^*E_{jj}XU_j=\delta_{ij}X_{jj}.
\]
Since \(U_i=E_{ij}U_j\) and \(U_i^*E_{ij}=U_j^*\), also \(X_{ii}=U_i^*XE_{ij}U_j=U_i^*E_{ij}XU_j=X_{jj}\). So all diagonal entries equal one operator \(x\), and the other entries vanish. By Lemma 3.1(1), \(X=\pi(x)\). \(\square\)

**Proposition 3.3** (the commutant of an amplified set). For every subset \(S\subseteq B(H)\),
\[
\begin{gathered}
\pi(S)'\\
=\{X\in B(\tilde H):\\
X_{ij}\in S'\text{ for all }i,j\in I\}.
\end{gathered}
\tag{3.4}
\]

**Proof.** For \(s\in S\), \((X\pi(s))_{ij}=U_i^*XU_js=X_{ij}s\) and \((\pi(s)X)_{ij}=sX_{ij}\). By Lemma 3.1(1), \(X\) commutes with \(\pi(s)\) exactly when \(X_{ij}s=sX_{ij}\) for all \(i,j\). \(\square\)

**Corollary 3.4.** \(\pi(S)''=\pi(S'')\) for every subset \(S\subseteq B(H)\).

**Proof.** The entries of each \(E_{ij}\) are \(0\) or \(1_H\), which lie in \(S'\). So \(E_{ij}\in\pi(S)'\) by (3.4). Every \(Y\in\pi(S)''\) therefore commutes with every \(E_{ij}\), and \(Y=\pi(y)\) for some \(y\) by Proposition 3.2. For \(y\in B(H)\) and \(X\in B(\tilde H)\), the entries of \(\pi(y)X\) and \(X\pi(y)\) are \(yX_{ij}\) and \(X_{ij}y\), by (3.2) and (3.3). So \(\pi(y)\in\pi(S)''\) exactly when \(y\) commutes with every entry of every \(X\in\pi(S)'\). By (3.4) these entries lie in \(S'\), and every \(z\in S'\) occurs, as a diagonal entry of \(\pi(z)\in\pi(S)'\). Hence \(\pi(y)\in\pi(S)''\) if and only if \(y\in S''\). \(\square\)

**Lemma 3.5** (nondegeneracy survives amplification). If \(M\) is a nondegenerate \(*\)-subalgebra of \(B(H)\), then \(\pi(M)\) is a nondegenerate \(*\)-subalgebra of \(B(\tilde H)\).

**Proof.** \([\pi(M)\tilde H]\supseteq[\pi(M)U_jH]=U_j[MH]=U_jH\) for every \(j\), and these subspaces together span a dense subspace of \(\tilde H\). \(\square\)

## 4. The double commutant theorem

The proof rests on one observation: for a nondegenerate \(*\)-algebra \(M\), every vector \(\xi\) lies in the closed span of its orbit \(M\xi\). Amplification then turns approximation at one vector into approximation in the \(\sigma\)-strong topology.

**Lemma 4.1.** Let \(S\subseteq B(H)\) be closed under products and adjoints, and suppose no nonzero vector is killed by every element of \(S\). Then \(\xi\in[S\xi]\) for every \(\xi\in H\). By [Proposition 2.4](#oa-fnd-bi-03)(1), this applies to every nondegenerate \(*\)-subalgebra.

**Proof.** Let \(L=[S\xi]\) and let \(p\) be its projection. Since \(s(t\xi)=(st)\xi\), the subspace \(L\) is invariant under \(S\). As \(S^*=S\), [Proposition 2.1](#oa-fnd-bi-02)(5) gives \(p\in S'\). For \(s\in S\), \(s\xi\in L\), so \(0=(1-p)s\xi=s(1-p)\xi\). Thus every \(s\in S\) kills \((1-p)\xi\), and so \((1-p)\xi=0\). \(\square\)

Both hypotheses matter; [Example 4.2](#oa-fnd-bi-06) shows what fails without them.

**Example 4.2** (Lemma 4.1 needs adjoints and nondegeneracy). On \(\mathbb C^2\), let \(S\) be the set of matrices whose second column is zero. It is closed under products, and \([S\mathbb C^2]=\mathbb C^2\), since \(S\xi=\mathbb C^2\) whenever the first coordinate of \(\xi\) is nonzero. For \(\xi=(0,1)\), however, \(S\xi=\{0\}\), so \(\xi\notin[S\xi]\). Here \(S\) is not closed under adjoints, and some nonzero vectors are killed by all of \(S\): for non-self-adjoint algebras, the spanning condition and the kernel condition of [Proposition 2.4](#oa-fnd-bi-03)(1) differ. Adjoints are needed even when the kernel condition holds. The set \(T\) of matrices whose second row is zero is closed under products and kills no nonzero vector, but for \(\xi=(0,1)\), \([T\xi]=\mathbb C(1,0)\) does not contain \(\xi\). For the \(*\)-algebra \(M=\{0\}\) on \(H\neq\{0\}\), \([M\xi]=\{0\}\) for every \(\xi\), so nondegeneracy is needed too.

**Lemma 4.3.** Let \(M\) be a nondegenerate \(*\)-subalgebra of \(B(H)\). Then \([M\xi]=[M''\xi]\) for every \(\xi\in H\). Consequently, for \(a\in M''\), \(\xi\in H\) and \(\varepsilon>0\) there is \(b\in M\) with \(\|(a-b)\xi\|<\varepsilon\).

**Proof.** \(M\subseteq M''\) gives \(\subseteq\). The projection \(p\) onto \([M\xi]\) lies in \(M'\), as in the previous proof. Each \(a\in M''\) commutes with \(p\), so \(a\) maps \([M\xi]\) into itself ([Proposition 2.1](#oa-fnd-bi-02)(5)). By Lemma 4.1, \(\xi\in[M\xi]\), so \(a\xi\in[M\xi]\). Hence \(M''\xi\subseteq[M\xi]\). Since \(M\xi\) is a linear subspace, \([M\xi]\) is its norm closure, and some \(b\xi\) with \(b\in M\) lies within \(\varepsilon\) of \(a\xi\). \(\square\)

We state the theorem for an arbitrary \(*\)-subalgebra, closed or not, degenerate or not.

**Theorem 4.4** (the double commutant theorem). Let \(M\) be a \(*\)-subalgebra of \(B(H)\), and let \(e\) be the projection onto \([MH]\).

1. \(e\in M'\cap M''\), and \(x=ex=xe\) for every \(x\in M\).
2. The closures of \(M\) in the weak, strong, strong\(^*\), \(\sigma\)-weak, \(\sigma\)-strong and \(\sigma\)-strong\(^*\) topologies coincide. Call this common closure \(\overline M\). It is a \(*\)-subalgebra. The projection \(e\) lies in \(\overline M\), is its unit (\(x=ex=xe\) for \(x\in\overline M\)), and is the greatest projection in \(\overline M\).
3. \(M''\) consists of the operators \(x+\alpha1\) with \(x\in\overline M\) and \(\alpha\in\mathbb C\), and
\[
\begin{gathered}
M''\\
=\overline M+\mathbb C1,\\
\overline M\\
=eM''\\
=M''e .
\end{gathered}
\tag{4.1}
\]
4. \(\overline M=M''\) if and only if \(M\) is nondegenerate.
5. \(M\) is a von Neumann algebra if and only if \(M\) is nondegenerate and closed in at least one of the six topologies. It is then closed in all of them.


*Remark 4.5.* Suppose that \(M\) is closed in one of the six topologies. Since the \(\sigma\)-strong\(^*\) topology is the finest of the six, closedness for it is the weakest hypothesis of this kind. Then \(\overline M=M\), and parts (2)–(4) say: \(e\) is the greatest projection of \(M\) and its unit; \(M''=M+\mathbb C1\); and \(M=M''\) when \(M\) is nondegenerate. Part (2) is von Neumann's density theorem: a nondegenerate \(*\)-algebra is dense in its bicommutant, even \(\sigma\)-strongly\(^*\).

**Proof.** *Step 1 (the nondegenerate case).* Assume \(M\) is nondegenerate. Let \(a\in M''\), let \((\xi_n)_{n\in\mathbb N}\) be square summable, and let \(\varepsilon>0\). Use the amplification of [Section 3](#oa-fnd-bi-05) with \(I=\mathbb N\), and put \(\tilde\xi=(\xi_n)\in\tilde H\). By Lemma 3.5, \(\pi(M)\) is a nondegenerate \(*\)-subalgebra of \(B(\tilde H)\), and \(\pi(a)\in\pi(M'')=\pi(M)''\) by Corollary 3.4. Lemma 4.3 on \(\tilde H\) gives \(b\in M\) with \(\|(\pi(a)-\pi(b))\tilde\xi\|<\varepsilon\), that is,
\[
\Big(\sum_n\|(a-b)\xi_n\|^2\Big)^{1/2}<\varepsilon .
\tag{4.2}
\]
Since \((\xi_n)\) and \(\varepsilon\) were arbitrary, [Lemma 1.2](#oa-fnd-bi-01)(a) shows that every \(\sigma\)-strong neighbourhood of \(a\) meets \(M\), so \(a\in\overline M^{\,\sigma s}\). Thus \(M''\subseteq\overline M^{\,\sigma s}\). On the other hand \(M''\) is weakly closed, being a commutant, and it contains \(M\), so \(\overline M^{\,w}\subseteq M''\). The comparisons of [Lemma 1.2](#oa-fnd-bi-01)(b) now give
\[
\begin{gathered}
M''\subseteq\overline M^{\,\sigma s}\subseteq\overline M^{\,\sigma w}\\
\subseteq\overline M^{\,w}\subseteq M'',\\
\overline M^{\,\sigma s}\subseteq\overline M^{\,s}\subseteq\overline M^{\,w}.
\end{gathered}
\]
So the weak, strong, \(\sigma\)-weak and \(\sigma\)-strong closures all equal \(M''\). Since \(M\) is a linear subspace, [Lemma 1.3](#oa-fnd-bi-01) adds \(\overline M^{\,s*}=\overline M^{\,w}\) and \(\overline M^{\,\sigma s*}=\overline M^{\,\sigma w}\). So all six closures equal \(M''\). Here \(e=1\).

*Step 2 (part 1).* \([MH]\) is invariant under \(M\), since \(x(y\xi)=(xy)\xi\), and \(M^*=M\); so \(e\in M'\) by [Proposition 2.1](#oa-fnd-bi-02)(5). \([MH]\) is also invariant under \(M'\), since \(y'(x\xi)=x(y'\xi)\), and \(M'\) is self-adjoint; so \(e\in M''\). For \(x\in M\), \(xH\subseteq[MH]\), so \(ex=x\). Applying this to \(x^*\in M\) and taking adjoints, \(xe=x\).

*Step 3 (reduction to \(eH\)).* Put \(K=eH\). By Step 2, each \(x\in M\) maps \(K\) into \(K\) and vanishes on \(K^\perp\). Let \(x_K\in B(K)\) be the restriction of \(x\) to \(K\), and \(M_K=\{x_K:x\in M\}\). Define \(\iota:B(K)\to B(H)\) by \(\iota(y)\xi=y(e\xi)\), extension by zero. Then \(\iota\) is an injective \(*\)-homomorphism onto \(eB(H)e\), and \(\iota(x_K)=x\) for \(x\in M\). So \(M_K\) is a \(*\)-subalgebra of \(B(K)\) with \(\iota(M_K)=M\), and it is nondegenerate: \([M_KK]=[MeH]=[MH]=K\).

For each of the six topologies \(\mathcal T\), the map \(\iota\) is a homeomorphism from \(B(K)\) onto \(eB(H)e\), and \(eB(H)e\) is \(\mathcal T\)-closed in \(B(H)\). Indeed \(\iota(y)\xi=y(e\xi)\), \(\iota(y)^*\xi=y^*(e\xi)\) and \(\langle\iota(y)\xi,\eta\rangle=\langle y(e\xi),e\eta\rangle\). So every \(\mathcal T\)-seminorm of \(\iota(y)\), built from vectors \(\xi_n,\eta_n\) of \(H\), is the \(\mathcal T\)-seminorm of \(y\) built from \(e\xi_n,e\eta_n\in K\); and every \(\mathcal T\)-seminorm on \(B(K)\) arises this way. Also \(eB(H)e=\{z:z-eze=0\}\) is closed, because \(z\mapsto z-eze\) is continuous by [Lemma 1.2](#oa-fnd-bi-01)(c). Hence the \(\mathcal T\)-closure of \(M=\iota(M_K)\) in \(B(H)\) is \(\iota\) of the \(\mathcal T\)-closure of \(M_K\) in \(B(K)\). By Step 1 on \(K\), the latter is \((M_K)''\) for every \(\mathcal T\). So all six closures of \(M\) are equal:
\[
\overline M=\iota\big((M_K)''\big).
\]
This is a \(*\)-subalgebra, and it contains \(\iota(1_K)=e\). Every \(z\in\overline M\) satisfies \(z=eze\), so \(e\) is the unit of \(\overline M\). If \(f\in\overline M\) is a projection, then \(f=efe\), so \(\langle f\xi,\xi\rangle=\langle fe\xi,e\xi\rangle\le\|e\xi\|^2=\langle e\xi,\xi\rangle\), and \(f\le e\). This proves (2).

*Step 4 (part 3).* \(M''\) is closed and contains \(M\), so \(\overline M\subseteq M''\); and \(1\in M''\). So \(\overline M+\mathbb C1\subseteq M''\). Conversely, let \(y\in M''\). By Step 2, \(e\in M'\), so \(y\) commutes with \(e\) and maps \(K\) and \(K^\perp\) into themselves.

- *On \(K^\perp\).* Let \(d\in B(H)\) satisfy \(d=(1-e)d(1-e)\). For \(x\in M\), \(xd=x(1-e)d(1-e)=0\) and \(dx=d(1-e)x=0\). So \(d\in M'\), and \(y\) commutes with \(d\). Every operator on \(K^\perp\) extends by zero to such a \(d\). So the restriction of \(y\) to \(K^\perp\) commutes with all of \(B(K^\perp)\), and by [Proposition 2.4](#oa-fnd-bi-03)(4) it is a scalar \(\alpha1_{K^\perp}\) with \(\alpha\in\mathbb C\). (If \(K^\perp=\{0\}\), take \(\alpha=0\).)
- *On \(K\).* Let \(c\in(M_K)'\). For \(x\in M\) and \(\xi\in H\), the vector \(c(e\xi)\) lies in \(K\), and \(x\xi\in K\) equals \(ex\xi\). So
\[
\begin{gathered}
x\,\iota(c)\xi\\
=x_Kc(e\xi)\\
=c\,x_K(e\xi)\\
=c(xe\xi)\\
=c(ex\xi)\\
=\iota(c)x\xi .
\end{gathered}
\]
So \(\iota(c)\in M'\), and \(y\) commutes with \(\iota(c)\). Restricting to \(K\), \(y_Kc=cy_K\). So \(y_K\in(M_K)''\).

Now \(y-\alpha1\) vanishes on \(K^\perp\), and its restriction to \(K\) is \(y_K-\alpha1_K\in(M_K)''\). So \(y-\alpha1=\iota(y_K-\alpha1_K)\in\overline M\). This proves \(M''=\overline M+\mathbb C1\). For \(x\in\overline M\), \(e(x+\alpha1)=x+\alpha e\in\overline M\); hence \(eM''\subseteq\overline M=e\overline M\subseteq eM''\). The same holds with \(e\) on the right.

*Step 5 (parts 4 and 5).* If \(M\) is nondegenerate, \(e=1\) and \(\overline M=M''\) by Step 1. If not, \(e\neq1\). Then \(1\notin\overline M\), because \(1\cdot e\neq1\), while \(1\in M''\). For (5): if \(M=M''\), then \(M\) contains \(1\), is nondegenerate, and is closed in all six topologies ([Proposition 2.4](#oa-fnd-bi-03)(2)). Conversely, if \(M\) is nondegenerate and closed in some \(\mathcal T\), then \(M=\overline M^{\,\mathcal T}=\overline M=M''\). \(\square\)

**Example 4.6** (compact operators). Let \(\dim H=\infty\). Then \(K(H)\) is a norm-closed \(*\)-subalgebra that contains every \(\theta_{\xi,\xi}\), so it is nondegenerate. The proof of [Proposition 2.4](#oa-fnd-bi-03)(4) uses only rank-one operators, so \(K(H)'=\mathbb C1\) and \(K(H)''=B(H)\). By [Theorem 4.4](#oa-fnd-bi-07), \(K(H)\) is dense in \(B(H)\) for all six topologies; for instance, the finite-rank projections onto spans of finitely many vectors of an orthonormal basis increase strongly to \(1\). But \(1\notin K(H)\), so \(K(H)\) is not a von Neumann algebra. Being norm closed is not enough.

## 5. Direct sums, reduced and induced algebras

Two constructions produce new von Neumann algebras from old ones: direct sums, and cutting down by a projection of the algebra or of its commutant. For both we compute the commutant and the centre.

Let \(\{M_i,H_i\}_{i\in I}\) be von Neumann algebras, \(I\) any set. Let \(H=\bigoplus_iH_i\) be the Hilbert sum, whose vectors are the families \(\bigoplus_i\xi_i\) with \(\sum_i\|\xi_i\|^2<\infty\), and let \(P_i\) be the projection onto \(H_i\). For a family \(x_i\in B(H_i)\) with \(\sup_i\|x_i\|<\infty\), put \((\bigoplus_ix_i)(\bigoplus_i\xi_i)=\bigoplus_ix_i\xi_i\). This is a bounded operator with \(\|\bigoplus_ix_i\|=\sup_i\|x_i\|\): the bound \(\sum_i\|x_i\xi_i\|^2\le\sup_i\|x_i\|^2\sum_i\|\xi_i\|^2\) gives \(\le\), and testing on vectors in a single \(H_i\) gives \(\ge\).

**Definition 5.1.** The *direct sum* \(\sum^\oplus_iM_i\), also written \(\sum^\oplus_i\{M_i,H_i\}\), is the set of operators \(\bigoplus_ix_i\) with \(x_i\in M_i\) and \(\sup_i\|x_i\|<\infty\).

**Proposition 5.2.**

1. \(T\in B(H)\) commutes with every \(P_i\) if and only if \(T=\bigoplus_iT_i\) for a bounded family \(T_i\in B(H_i)\).
2. \(\big(\sum^\oplus_iM_i\big)'=\sum^\oplus_iM_i'\).
3. \(\sum^\oplus_iM_i\) is itself a von Neumann algebra, and its centre is \(\sum^\oplus_iZ(M_i)\).
4. If at least two of the spaces \(H_i\) are nonzero, \(\sum^\oplus_iM_i\) is not a factor. If exactly one, \(H_{i_0}\), is nonzero, then \(\sum^\oplus_iM_i\) is spatially isomorphic to \(M_{i_0}\).

**Proof.** (1) If \(T\) commutes with every \(P_i\), then \(TH_i\subseteq H_i\) by [Proposition 2.1](#oa-fnd-bi-02)(5). Let \(T_i\) be the restriction of \(T\) to \(H_i\); then \(\|T_i\|\le\|T\|\). Since \(\xi=\sum_iP_i\xi\) and \(T\) is continuous, \(T\xi=\sum_iTP_i\xi=\bigoplus_iT_i\xi_i\). The converse is clear.

(2) Each \(P_i\) lies in \(\sum^\oplus M_i\): take \(1\) in place \(i\) and \(0\) elsewhere. So \(T\in(\sum^\oplus M_i)'\) commutes with every \(P_i\), and \(T=\bigoplus T_i\) by (1). For \(x\in M_i\), the operator with \(x\) in place \(i\) and \(0\) elsewhere lies in \(\sum^\oplus M_i\). Commuting with it gives \(T_ix=xT_i\). So \(T_i\in M_i'\). Conversely, \(\bigoplus y_i\) with \(y_i\in M_i'\) commutes with every \(\bigoplus x_i\), place by place.

(3) \(\sum^\oplus M_i\) is a \(*\)-subalgebra: sums, products and adjoints are taken place by place, and the norms stay bounded. Each \(M_i'\) is a von Neumann algebra ([Proposition 2.4](#oa-fnd-bi-03)(2)), so (2) applies to the family \((M_i')\). It gives \((\sum^\oplus M_i)''=(\sum^\oplus M_i')'=\sum^\oplus M_i''=\sum^\oplus M_i\). The centre is \((\sum^\oplus M_i)\cap(\sum^\oplus M_i')\); comparing places, this is \(\sum^\oplus(M_i\cap M_i')\).

(4) If \(H_i\neq0\neq H_j\) with \(i\neq j\), then \(P_i\) is central by (3), and \(P_i\) is neither \(0\) nor \(1\). If only \(H_{i_0}\) is nonzero, the identification of \(H\) with \(H_{i_0}\) is a unitary that carries \(\sum^\oplus M_i\) onto \(M_{i_0}\), since the other places act on zero spaces. \(\square\)

*Remark 5.3.* The proof of (2) uses only that each \(M_i\) contains \(0\) and \(1_{H_i}\). Without units the formula can fail: for \(S_1=S_2=\{0\}\) on \(\mathbb C\oplus\mathbb C\), the commutant of the direct sum is all of \(B(\mathbb C^2)\), not the diagonal matrices.

**Example 5.4** (a degenerate algebra). Let \(p\) be a projection with \(p\neq0\) and \(p\neq1\), and \(M=\mathbb Cp\). This is a closed \(*\)-subalgebra, \([MH]=pH\), and \(e=p\). An operator commutes with \(p\) exactly when it is block diagonal for \(H=pH\oplus(1-p)H\), so \(M'=B(pH)\oplus B((1-p)H)\). By [Proposition 5.2](#oa-fnd-bi-04)(2) and [Proposition 2.4](#oa-fnd-bi-03)(4), \(M''=\{\alpha p+\beta(1-p)\}=M+\mathbb C1\). So \(M''\neq M=\overline M=eM''\), as (4.1) and [Theorem 4.4](#oa-fnd-bi-07)(4) predict.

**Example 5.5** (an isomorphism that is not spatial). On \(\mathbb C^4\) let \(M_1=\{\operatorname{diag}(a,b,b,b)\}\) and \(M_2=\{\operatorname{diag}(a,a,b,b)\}\), with \(a,b\in\mathbb C\). By [Proposition 5.2](#oa-fnd-bi-04) and [Proposition 2.4](#oa-fnd-bi-03)(4), these are von Neumann algebras: \(M_1=\mathbb C1_{\mathbb C}\oplus\mathbb C1_{\mathbb C^3}\) and \(M_2=\mathbb C1_{\mathbb C^2}\oplus\mathbb C1_{\mathbb C^2}\). The map \(\operatorname{diag}(a,b,b,b)\mapsto\operatorname{diag}(a,a,b,b)\) is a \(*\)-isomorphism. It is not spatial. A unitary \(U\) with \(UM_1U^*=M_2\) would carry the rank-one projection \(\operatorname{diag}(1,0,0,0)\in M_1\) to a rank-one projection in \(M_2\), but the projections of \(M_2\) have rank \(0\), \(2\) or \(4\).

**Example 5.6** (commutants of direct sums with a common summand). Suppose \(H\neq\{0\}\), and let \(M=\{x\oplus x:x\in B(H)\}\) on \(H\oplus H\). This is \(\pi(B(H))\) for \(I=\{1,2\}\) in [Section 3](#oa-fnd-bi-05), so \(M''=M\) by Corollary 3.4, and by (3.4) \(M'\) consists of the \(2\times2\) scalar matrices tensored with \(1_H\). An operator in both \(M\) and \(M'\) is \(\pi(x)\) with \(x\) scalar. So \(M\) is a factor, while the direct sum \(B(H)\oplus B(H)\) of [Definition 5.1](#oa-fnd-bi-04) is not: its central projection \(1_H\oplus0\) is neither zero nor the identity, by \(H\neq\{0\}\). The two algebras are different subalgebras of \(B(H\oplus H)\) built from the same summands. If \(H=\{0\}\), both constructions give the same zero algebra; its centre is \(\mathbb C1_H=\{0\}\), so it satisfies this lesson's centre-based factor convention. Thus the contrast between the two constructions requires a nonzero summand.

Now fix a von Neumann algebra \(\{M,H\}\) and a projection \(e\in M\), and put \(K=eH\). For \(x\in M\), the operator \(exe\) maps \(K\) into \(K\); write \(x_e\) for its restriction to \(K\). Each \(x'\in M'\) commutes with \(e\), so it maps \(K\) into \(K\); write \(x'_e\) for its restriction. Put \(M_e=\{x_e:x\in M\}\) and \(M'_e=\{x'_e:x'\in M'\}\). Both are \(*\)-subalgebras of \(B(K)\) containing \(1_K\). The map \(x'\mapsto x'_e\) is a unital \(*\)-homomorphism from \(M'\) onto \(M'_e\), because \(e\) commutes with \(M'\). Let \(z\) be the projection onto \([MK]=[MeH]\).

**Definition 5.7.** On \(K\), the algebra \(M_e\) is called *reduced* (from \(M\)) and \(M'_e\) is called *induced* (from \(M'\)). The map \(x'\mapsto x'_e\) from \(M'\) onto \(M'_e\) is the *induction*. (Part (3) of Theorem 5.8 shows that both algebras are von Neumann algebras.)

**Theorem 5.8.**

1. \((M'_e)'=M_e\).
2. \((M_e)'=M'_e\).
3. \(M_e\) and \(M'_e\) are von Neumann algebras on \(K\).
4. \(z\in Z(M)\), \(e\le z\), and \(z\) is the smallest projection of \(Z(M)\) that majorizes \(e\). The kernel of the induction is \(M'(1-z)\). So the induction is injective if and only if \([MeH]=H\).
5. \(Z(M_e)=\{c_e:c\in Z(M)\}\). In particular, if \(M\) is a factor, so are \(M_e\) and \(M'_e\).

By symmetry, the same statements hold for a projection \(e'\in M'\), with the roles of \(M\) and \(M'\) exchanged: apply the theorem to the von Neumann algebra \(M'\), whose commutant is \(M\).

**Proof.** *The easy inclusions.* Each \(x'\in M'\) commutes with each \(exe\), so \(x'_e\) commutes with \(x_e\). Thus \(M'_e\subseteq(M_e)'\) and \(M_e\subseteq(M'_e)'\).

(1) Let \(T\in(M'_e)'\), and define \(\tilde T\in B(H)\) by \(\tilde T\xi=T(e\xi)\). For \(x'\in M'\) and \(\xi\in H\),
\[
\begin{gathered}
\tilde Tx'\xi\\
=T(ex'\xi)\\
=T(x'e\xi)\\
=Tx'_e(e\xi)\\
=x'_eT(e\xi)\\
=x'\tilde T\xi .
\end{gathered}
\]
So \(\tilde T\in M''=M\). Since \(\tilde T=e\tilde Te\), we get \(T=\tilde T_e\in M_e\).

(2) Let \(u'\) be a unitary in \((M_e)'\). On the linear span \(L_0\) of the vectors \(x\xi\) with \(x\in M\) and \(\xi\in K\), try to define \(u'_0\big(\sum_kx_k\xi_k\big)=\sum_kx_ku'\xi_k\). For finitely many \(x_k\in M\) and \(\xi_k\in K\),
\[
\begin{gathered}
\Big\|\sum_kx_ku'\xi_k\Big\|^2\\
=\sum_{j,k}\langle(ex_j^*x_ke)_e\,u'\xi_k,u'\xi_j\rangle\\
=\sum_{j,k}\langle u'(ex_j^*x_ke)_e\xi_k,u'\xi_j\rangle\\
=\Big\|\sum_kx_k\xi_k\Big\|^2 .
\end{gathered}
\]
The first equality uses \(u'\xi_k\in K\); the second uses that \(u'\) commutes with \(M_e\); the third uses \(u'^*u'=1_K\). So \(u'_0\) is well defined on \(L_0\) (apply the identity to a difference of two representations of the same vector) and isometric. It extends to an isometry of \(L=[MK]\) into itself. Its range contains \(L_0\), because \(u'\) maps \(K\) onto \(K\); being closed, the range is all of \(L\). Put \(u'_0=0\) on \(L^\perp\). The subspaces \(L\) and \(L^\perp\) are invariant under \(M\) ([Proposition 2.1](#oa-fnd-bi-02)(5)). For \(y\in M\), on \(L_0\) we have \(u'_0y\sum_kx_k\xi_k=\sum_kyx_ku'\xi_k=yu'_0\sum_kx_k\xi_k\), and by continuity this holds on \(L\); on \(L^\perp\) both \(u'_0y\) and \(yu'_0\) vanish. So \(u'_0\in M'\). For \(\xi\in K\), \(\xi=e\xi\) with \(e\in M\), so \(u'_0\xi=eu'\xi=u'\xi\). Thus \(u'=(u'_0)_e\in M'_e\).

\((M_e)'\) is a unital norm-closed \(*\)-algebra ([Proposition 2.1](#oa-fnd-bi-02)). By (U), each of its elements has the form \(\sum_{k=1}^4\lambda_ku_k\) with scalars \(\lambda_k\) and unitaries \(u_k\in(M_e)'\). \(M'_e\) is a linear space that contains all these unitaries, so \((M_e)'\subseteq M'_e\).

(3) By (1) and (2), \(M_e\) and \(M'_e\) are commutants of self-adjoint subsets of \(B(K)\). So both are von Neumann algebras ([Proposition 2.1](#oa-fnd-bi-02)(4)).

(4) \([MK]\) is invariant under \(M\). It is invariant under \(M'\) too: for \(y'\in M'\), \(x\in M\) and \(\xi\in K\), \(y'x\xi=xy'\xi\) and \(y'\xi\in K\). Both sets are self-adjoint, so \(z\in M''\cap M'=Z(M)\). Since \(e\in M\), \(K=eK\subseteq[MK]\), so \(e\le z\). If \(c\in Z(M)\) is a projection with \(e\le c\), then \(cxe\xi=xce\xi=xe\xi\), so \([MK]\subseteq cH\) and \(z\le c\). For the kernel: if \(x'_e=0\), that is \(x'e=0\), then \(x'xe\xi=xx'e\xi=0\) for \(x\in M\); so \(x'\) vanishes on \(zH\), and \(x'=x'(1-z)\in M'(1-z)\). Conversely \(y'(1-z)e=y'(e-ze)=0\), since \(ze=e\). The kernel \(M'(1-z)\) is zero exactly when \(1-z=0\).

(5) For \(c\in Z(M)\), \(c_e\in M_e\) and \(c_e=c|_K\in M'_e=(M_e)'\) by (2); so \(c_e\in Z(M_e)\). Conversely, let \(t\in Z(M_e)=M_e\cap M'_e\). Choose \(x'\in M'\) with \(x'_e=t\). Replacing \(x'\) by \(x'z\) changes nothing on \(K\), so we may assume \(x'=x'z=zx'\). Let \(w'\in M'\). Then \((x'w'-w'x')_e=tw'_e-w'_et=0\), since \(t\in M_e=(M'_e)'\) by (1). So \(q=x'w'-w'x'\) lies in the kernel \(M'(1-z)\) by (4), that is \(q=q(1-z)\). Also \(q=zq\), because \(z\) is central and \(x'=zx'=x'z\). Hence \(q=zq(1-z)=qz(1-z)=0\). So \(x'\) commutes with \(M'\), \(x'\in M''=M\), and \(x'\in Z(M)\) with \(x'_e=t\). If \(M\) is a factor, \(Z(M_e)=\mathbb C1_K\). The centre of \(M'_e\) is \(M'_e\cap(M'_e)'=M'_e\cap M_e=Z(M_e)\) by (1), so \(M'_e\) is a factor as well. \(\square\)

*Remark 5.9.* An unused alternative proof of (2), with square roots of operator matrices in place of unitaries, is in the lesson Spatial tensor products of von Neumann algebras. The induction need not be injective ([Exercise 5.10](#oa-fnd-bi-08)); parts (4) and (5) describe its kernel and the centres.

**Exercise 5.10** (easy; the induction need not be injective). Let \(H=H_1\oplus H_2\) with \(H_1,H_2\neq\{0\}\), \(M=B(H_1)\oplus B(H_2)\), and \(e=1\oplus0\). Compute \(M'\), \(M_e\), \(M'_e\), the central projection \(z\) of Theorem 5.8(4), and the kernel of the induction.

*Solution.* By [Proposition 5.2](#oa-fnd-bi-04)(2) and [Proposition 2.4](#oa-fnd-bi-03)(4), \(M'=\{\alpha1\oplus\beta1\}\). Here \(K=H_1\), \(M_e=B(H_1)\) and \(M'_e=\mathbb C1_{H_1}\). The subspace \([MK]=H_1\), so \(z=e\). The induction sends \(\alpha1\oplus\beta1\) to \(\alpha1_{H_1}\); its kernel is \(\{0\oplus\beta1\}=M'(1-z)\), which is nonzero. As [Theorem 5.8](#oa-fnd-bi-08)(2) requires, \((M_e)'=B(H_1)'=\mathbb C1_{H_1}=M'_e\). \(\square\)

## 6. Algebras of compact operators

By Example 4.6, \(K(H)\) is dense in \(B(H)\) when \(\dim H=\infty\). This section looks at norm-closed \(*\)-subalgebras of \(K(H)\). The double commutant theorem still recovers such an algebra, provided one intersects with \(K(H)\) only at the end. The section ends with the simple C\(^*\)-algebras that have a nonzero minimal projection: each of them is isomorphic to \(K(H)\) for some Hilbert space \(H\).

**Example 6.1** (commutants taken inside \(K(H)\)). Let \(H=\ell^2\oplus\ell^2\) and \(A=K(\ell^2)\oplus K(\ell^2)=\{a\oplus b\}\). This is a norm-closed nondegenerate \(*\)-subalgebra contained in \(K(H)\). An operator that commutes with every \(a\oplus0\) and every \(0\oplus b\) has zero off-diagonal blocks, because \(K(\ell^2)\) is nondegenerate, and its diagonal blocks lie in \(K(\ell^2)'=\mathbb C1\) (Example 4.6). So \(A'=\{\alpha1\oplus\beta1\}\). ([Proposition 5.2](#oa-fnd-bi-04)(2) does not apply directly, since \(1\notin K(\ell^2)\); nondegeneracy replaces the projections \(P_i\) used there.) None of these operators is compact unless \(\alpha=\beta=0\), so \(A'\cap K(H)=\{0\}\), and \(\{0\}'\cap K(H)=K(H)\). But \(K(H)\) contains the rank-one operator \(\theta_{0\oplus\delta_1,\,\delta_1\oplus0}\), which maps the first summand into the second and so is not in \(A\). Hence \(\{A'\cap K(H)\}'\cap K(H)\neq A\): commutants taken inside \(K(H)\) do not recover \(A\). When \(\dim H<\infty\) this identity does hold. Then \(K(H)=B(H)\), and \(A\) is finite dimensional, hence closed in every topology, so the identity reads \(A''=A\), which is [Theorem 4.4](#oa-fnd-bi-07)(5).

**Exercise 6.2** (hard; compact operators in the bicommutant). Let \(A\subseteq K(H)\) be a nondegenerate norm-closed \(*\)-subalgebra. Show that \(A''\cap K(H)=A\).

Example 6.1 proves directly that taking the first commutant inside \(K(H)\) can fail to recover the algebra.

Nondegeneracy is necessary here. For the degenerate algebra \(A=\mathbb CE_{11}\) on \(\mathbb C^2\), Example 5.4 gives \(A''\cap K(\mathbb C^2)=A''=\{\operatorname{diag}(\alpha,\beta)\}\neq A\).

*Solution.* The inclusion \(A\subseteq A''\cap K(H)\) is clear.

*Step 1 (spectral projections lie in \(A\)).* Let \(a\in A\), \(a\ge0\), and let \(t>0\) with \(t\) not in the spectrum \(\sigma(a)\). By (K), \(a=\sum_n\alpha_n\theta_{\varepsilon_n,\varepsilon_n}\) for an orthonormal family \((\varepsilon_n)\) and numbers \(\alpha_n>0\) (tending to \(0\) if there are infinitely many), and \(\sigma(a)\subseteq\{\alpha_n\}\cup\{0\}\). Only finitely many \(\alpha_n\) exceed \(t\). The indicator function \(g\) of \((t,\infty)\) is continuous on \(\sigma(a)\), because the closed set \(\sigma(a)\) misses a neighbourhood of \(t\), and \(g(0)=0\). So \(g(a)\in A\) by (C). It is the finite-rank projection \(p_t=\sum_{\alpha_n>t}\theta_{\varepsilon_n,\varepsilon_n}\), and \(\|a(1-p_t)\|\le t\).

*Step 2 (an increasing net of finite-rank projections in \(A\) with supremum \(1\)).* Let \(\mathcal P\) be the set of finite-rank projections in \(A\). For \(p,q\in\mathcal P\), \(p+q\) is a positive finite-rank element of \(A\). If \(p+q=0\), then \(p=q=0\) and their join is already in \(\mathcal P\). Otherwise choose \(t>0\) below the smallest nonzero eigenvalue of \(p+q\); Step 1 puts the projection onto the range of \(p+q\) in \(A\). That range is \((\ker p\cap\ker q)^\perp\), because \(\langle(p+q)\xi,\xi\rangle=\|p\xi\|^2+\|q\xi\|^2\); it contains \(pH\) and \(qH\). So \(\mathcal P\) is upward directed. As a net indexed by itself, it increases, so it converges strongly to its supremum \(P\) by Vigier's theorem (V). \(P\) is the projection onto the closed span of the ranges of the elements of \(\mathcal P\). For \(a\in A\) and \(t\notin\sigma(aa^*)\), Step 1 gives \(p_t\in\mathcal P\) commuting with \(aa^*\) with \(\|(1-p_t)a\|^2=\|(1-p_t)aa^*(1-p_t)\|\le t\). Since \(\sigma(aa^*)\) is countable (K), such \(t>0\) can be taken as small as we like. So each \(a\xi\) is a limit of vectors \(p_ta\xi\in PH\). Thus \([AH]\subseteq PH\), and nondegeneracy gives \(P=1\).

*Step 3 (\(A''p\subseteq A\) for \(p\in\mathcal P\)).* For \(p=0\) the assertion is immediate. Assume \(p\ne0\), and let \(\varepsilon_1,\dots,\varepsilon_n\) be an orthonormal basis of \(pH\). The set \(Ap=\{b\in A:bp=b\}\) is a norm-closed subspace of \(A\). The map \(\Phi(z)=(z\varepsilon_1,\dots,z\varepsilon_n)\) from \(B(H)p\) to \(H^n\) is linear and injective, and \(\|z\|\le\|\Phi(z)\|\le\sqrt n\,\|z\|\) for \(z\in B(H)p\), since \(z\zeta=\sum_k\langle\zeta,\varepsilon_k\rangle z\varepsilon_k\). So \(\Phi(Ap)\) is a complete, hence closed, subspace of \(H^n\), and therefore weakly closed. Let \(y\in A''\). By [Theorem 4.4](#oa-fnd-bi-07), \(y\) is the weak limit of a net \((a_\lambda)\) in \(A\). Then \(a_\lambda p\in Ap\), and \(\Phi(a_\lambda p)\to\Phi(yp)\) weakly in \(H^n\). So \(\Phi(yp)\in\Phi(Ap)\), and \(yp\in Ap\subseteq A\).

*Step 4 (conclusion).* Let \(T\in A''\cap K(H)\). Along the net \(\mathcal P\) of Step 2, \(\|T-Tp\|=\|(1-p)T^*\|\to0\). Indeed, \(T^*\) is compact, so it is a norm limit of finite-rank operators \(F=\sum_{k=1}^m\theta_{\alpha_k,\beta_k}\) (K); \(\|(1-p)F\|\le\sum_k\|(1-p)\alpha_k\|\,\|\beta_k\|\to0\), and \(\|(1-p)(T^*-F)\|\le\|T^*-F\|\). Each \(Tp\) lies in \(A\) by Step 3, and \(A\) is norm closed. So \(T\in A\). \(\square\)

**Exercise 6.3** (medium; minimal projections and simple C\(^*\)-algebras). Here a projection \(e\) in a C\(^*\)-algebra \(A\) is *minimal* if \(eAe=\mathbb Ce\). A representation \(\{\pi,H\}\) is *irreducible* if \(H\) and \(\{0\}\) are its only closed invariant subspaces. \(A\) is *simple* if its only closed two-sided ideals are \(\{0\}\) and \(A\). Let \(e\neq0\) be a minimal projection of \(A\). Prove (a) and (b).

(a) *If \(\pi\) is irreducible and \(\pi(e)\neq0\), then \(\pi(e)\) is a projection of rank one.* It is a projection because \(\pi\) is a \(*\)-homomorphism. Take a unit vector \(\xi\in\pi(e)H\). The subspace \([\pi(A)\xi]\) is closed, invariant and contains \(\xi=\pi(e)\xi\), so it is \(H\). Let \(\eta\in\pi(e)H\) and choose \(a_k\in A\) with \(\pi(a_k)\xi\to\eta\). Write \(ea_ke=\lambda_ke\). Then \(\eta=\pi(e)\eta=\lim_k\pi(e)\pi(a_k)\pi(e)\xi=\lim_k\lambda_k\xi\). So \(\eta\in\mathbb C\xi\), and \(\pi(e)H=\mathbb C\xi\). \(\square\)

(b) *If \(A\) is simple, then \(A\cong K(H)\) for some Hilbert space \(H\).* Let \(H=Ae=\{x\in A:xe=x\}\), a norm-closed subspace of \(A\). For \(\xi,\eta\in H\), \(\eta^*\xi=e\eta^*\xi e\in eAe\), so \(\eta^*\xi=\langle\xi,\eta\rangle e\) for a unique scalar \(\langle\xi,\eta\rangle\). This is linear in \(\xi\) and conjugate linear in \(\eta\). Since \(\xi^*\xi\ge0\) and \(e\neq0\), \(\langle\xi,\xi\rangle\ge0\), and \(\|\xi\|_A^2=\|\xi^*\xi\|=\langle\xi,\xi\rangle\|e\|=\langle\xi,\xi\rangle\). So the Hilbert norm equals the C\(^*\)-norm, and \(H\) is complete: a Hilbert space, nonzero because \(e\in H\). Put \(\pi(x)\xi=x\xi\). Then \(\|\pi(x)\|\le\|x\|\), \(\pi\) is multiplicative, and \(\langle\pi(x)\xi,\eta\rangle e=\eta^*x\xi=(x^*\eta)^*\xi=\langle\xi,\pi(x^*)\eta\rangle e\). So \(\pi\) is a representation.

For \(\zeta,\eta\in H\), \(\pi(\zeta\eta^*)\xi=\zeta\eta^*\xi=\langle\xi,\eta\rangle\zeta e=\theta_{\zeta,\eta}\xi\). So \(\pi(A)\) contains every rank-one operator, hence every finite-rank operator. In particular \(\pi(e)=\theta_{e,e}\) has rank one. The kernel of \(\pi\) is a closed two-sided ideal that does not contain \(e\), so it is \(\{0\}\) by simplicity. The set \(J=\{x\in A:\pi(x)\in K(H)\}\) is a closed two-sided ideal, since \(\pi\) is continuous and \(K(H)\) is a closed ideal of \(B(H)\). It contains \(e\), so \(J=A\) and \(\pi(A)\subseteq K(H)\). An injective \(*\)-homomorphism between C\(^*\)-algebras is isometric (C), so \(\pi(A)\) is norm closed. It contains the finite-rank operators, whose closure is \(K(H)\) (K). So \(\pi(A)=K(H)\), and \(\pi:A\to K(H)\) is a \(*\)-isomorphism. \(\square\)

*Remarks.* (i) The definition \(eAe=\mathbb Ce\) matters. A minimal projection in this sense majorizes no nonzero projection other than itself. The converse fails in C\(^*\)-algebras, and with that weaker definition (a) is false. The algebra \(B=\{f\in C([0,1],M_2(\mathbb C)):f(0),f(1)\in\mathbb C1\}\) has only the projections \(0\) and \(1\): the rank of a continuous projection-valued function is constant on \([0,1]\), and at \(t=0\) it is \(0\) or \(2\). Evaluation at \(t=1/2\) is an irreducible representation on \(\mathbb C^2\), since every matrix is \(f(1/2)\) for some \(f\in B\). But it sends the projection \(1\) to a projection of rank two. (ii) If "simple" is read as having no two-sided ideals other than \(\{0\}\) and \(A\), closed or not, then the ideal \(AeA\) of finite sums \(\sum x_iey_i\) equals \(A\). Since \(\pi(xey)\) has rank at most one, \(\pi(A)\) then consists of finite-rank operators, so \(K(H)\) consists of finite-rank operators and \(\dim H<\infty\): \(A\cong M_n(\mathbb C)\).

## 7. Polar decomposition inside a von Neumann algebra

The polar decomposition of an element of a von Neumann algebra stays inside the algebra. The reason is uniqueness: conjugating by a unitary of the commutant gives another polar decomposition, which must be the same one. As a consequence, every two-sided ideal of a von Neumann algebra is self-adjoint.

**Lemma 7.1** (uniqueness of the polar decomposition). Let \(x=wk\), where \(k\ge0\) and \(w\) is a partial isometry with \(\ker w=\ker k\). Then \(k=|x|\), and \(w\) is the partial isometry \(u\) of (P).

**Proof.** \(w^*w\) is the projection onto \((\ker w)^\perp=(\ker k)^\perp\), which is the closure of \(kH\) because \(k\) is self-adjoint. So \(w^*wk=k\), and \(x^*x=kw^*wk=k^2\). By uniqueness of positive square roots (C), \(k=|x|\). On \(kH\), \(w(k\xi)=x\xi=u(|x|\xi)=u(k\xi)\), so \(w=u\) on the closure of \(kH\). Both vanish on \(\ker k=\ker|x|=\ker x\); here \(\ker|x|=\ker x\) because \(\||x|\xi\|^2=\langle x^*x\xi,\xi\rangle=\|x\xi\|^2\). So \(w=u\). \(\square\)

**Proposition 7.2.** Let \(x\) be an element of a von Neumann algebra \(M\), with polar decomposition \(x=u|x|\). Then \(u\in M\) and \(|x|\in M\).

**Proof.** Let \(v\) be a unitary in \(M'\). Then \(x=vxv^*=(vuv^*)(v|x|v^*)\). Here \(v|x|v^*\ge0\), and \(vuv^*\) is a partial isometry with \[
\begin{gathered}
\ker(vuv^*)\\
=v\ker u\\
=v\ker x\\
=v\ker|x|\\
=\ker(v|x|v^*).
\end{gathered}
\] By Lemma 7.1, \(vuv^*=u\) and \(v|x|v^*=|x|\). So \(u\) and \(|x|\) commute with every unitary of \(M'\). Since \(M'\) is a von Neumann algebra ([Proposition 2.4](#oa-fnd-bi-03)(2)), it is spanned by its unitaries (U). Hence \(u,|x|\in M''=M\). \(\square\)

That \(|x|\in M\) also follows from (C). Here is the full strong-limit argument for \(u\in M\). Let \(p\) be the projection onto \([|x|H]\) and put \(h_\varepsilon=|x|(|x|+\varepsilon1)^{-1}\). The calculus gives \(0\le h_\varepsilon\le1\), and \(h_\varepsilon\) vanishes on \(\ker|x|\). For \(\xi\in H\),
\[
\begin{gathered}
\|(h_\varepsilon-1)|x|\xi\|\\
=\|\varepsilon(|x|+\varepsilon1)^{-1}|x|\xi\|\\
\le\varepsilon\|\xi\|.
\end{gathered}
\]
Thus \(h_\varepsilon\to p\) on the dense subspace \(|x|H\) of \(pH\), and the uniform contraction bound extends this convergence to \(pH\). It is zero on \((1-p)H\), so the convergence is strong on \(H\). Consequently \(x(|x|+\varepsilon1)^{-1}=uh_\varepsilon\to up=u\) strongly. Each approximant lies in \(M\) by (C), and \(M\) is strongly closed, so \(u\in M\).

**Corollary 7.3** (ideals and the polar decomposition). Fix a von Neumann algebra \(M\) and \(x\in M\) with \(x=u|x|\). No closure assumption is made on the ideals below.

1. If \(l\) is a left ideal of \(M\) (a linear subspace with \(Ml\subseteq l\)) and \(x\in l\), then \(|x|=u^*x\in l\).
2. If \(r\) is a right ideal (\(rM\subseteq r\)) and \(x\in r\), then \(|x^*|=xu^*\in r\).
3. Every two-sided ideal \(m\) of \(M\) is self-adjoint.

**Proof.** (1) \(u^*x=u^*u|x|=|x|\), since \(u^*u\) is the projection onto the closure of \(|x|H\), and \(u^*\in M\). (2) \(xx^*=u|x|^2u^*=(u|x|u^*)^2\) and \(u|x|u^*\ge0\), so \(|x^*|=u|x|u^*=xu^*\), with \(u^*\in M\). (3) For \(x\in m\), (1) gives \(|x|\in m\), and then \(x^*=|x|u^*\in m\). \(\square\)

The polar decomposition inside \(M\) is essential in (3). In C\(^*\)-algebras, two-sided ideals that are not closed need not be self-adjoint ([Example 7.4](#oa-fnd-bi-09)).

**Example 7.4** (a two-sided ideal that is not self-adjoint, outside von Neumann algebras). In the C\(^*\)-algebra \(C[0,1]\), let \(g(t)=te^{i/t}\) for \(t>0\) and \(g(0)=0\); \(g\) is continuous. The ideal \(gC[0,1]\) is two-sided, but it does not contain \(\bar g\). Indeed, \(\bar g=gk\) would force \(k(t)=e^{-2i/t}\) for \(t>0\), which has no limit as \(t\downarrow0\): it equals \(1\) at \(t=1/(\ell\pi)\) and \(-i\) at \(t=1/(\ell\pi+\pi/4)\) for every integer \(\ell\ge1\). In the von Neumann algebra \(L^\infty[0,1]\) of multiplication operators on \(L^2[0,1]\) (its full multiplication-commutant proof is [Theorem 9.1 of the Hilbert-space lesson](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-09)), the same ideal does contain \(\bar g\), because \(e^{-2i/t}\) is bounded and measurable. This matches [Corollary 7.3](#oa-fnd-bi-09)(3).

**Exercise 7.5** (hard; asymmetric Riesz decomposition). In a von Neumann algebra \(M\), suppose that \(\sum_{i\in I}x_i^*x_i=\sum_{j\in J}y_j^*y_j\), the sums converging \(\sigma\)-strongly. Show that there are \(z_{ij}\in M\) with
\[
\begin{gathered}
\sum_jz_{ij}^*z_{ij}\\
=x_ix_i^*\quad(i\in I),\\
\sum_iz_{ij}z_{ij}^*\\
=y_jy_j^*\quad(j\in J).
\end{gathered}
\]

*Solution.* Let \(a\) be the common sum. For finite \(G\subseteq I\), \(\langle\sum_{i\in G}x_i^*x_i\xi,\xi\rangle\le\langle a\xi,\xi\rangle\), because the partial sums increase and converge weakly to \(a\). So \(\|x_i\xi\|\le\|a^{1/2}\xi\|\) for each \(i\). (Only weak convergence of the sums was used. For increasing nets of positive operators, weak convergence to \(a\) already implies convergence in all six topologies by [Lemma 1.2](#oa-fnd-bi-01)(e).)

*The factors \(s_i\).* Let \(p\) be the projection onto the closure of \(a^{1/2}H\), which is the closure of \(aH\) because \(\ker a^{1/2}=\ker a\). The rule \(s_i(a^{1/2}\xi)=x_i\xi\) is well defined and contractive on \(a^{1/2}H\), by the bound above. Extend it by continuity to \(pH\), and by \(0\) on \((1-p)H\). Then \(x_i=s_ia^{1/2}\) and \(s_i=s_ip\). To see \(s_i\in M\), let \(v\) be a unitary in \(M'\). It commutes with \(a^{1/2}\) and \(x_i\), and it maps \(a^{1/2}H\), hence \(pH\) and \((1-p)H\), onto themselves. So \[
\begin{gathered}
vs_iv^*(a^{1/2}\xi)\\
=vs_ia^{1/2}v^*\xi\\
=vx_iv^*\xi\\
=x_i\xi\\
=s_i(a^{1/2}\xi),
\end{gathered}
\] and both \(vs_iv^*\) and \(s_i\) vanish on \((1-p)H\). Thus \(vs_iv^*=s_i\) for every unitary \(v\in M'\). Since \(M'\) is spanned by its unitaries (U), \(s_i\in M''=M\).

*The sum \(\sum_is_i^*s_i\).* For finite \(G\), \[
\begin{gathered}
\langle\sum_{i\in G}s_i^*s_ia^{1/2}\xi,a^{1/2}\xi\rangle\\
=\sum_{i\in G}\|x_i\xi\|^2\\
\le\|a^{1/2}\xi\|^2.
\end{gathered}
\] Since \(a^{1/2}H\) is dense in \(pH\) and the operators vanish on \((1-p)H\), \(\sum_{i\in G}s_i^*s_i\le p\). The partial sums increase, so they converge strongly to some \(c\le p\), by Vigier's theorem (V). On the dense subspace, \[
\begin{gathered}
\langle ca^{1/2}\xi,a^{1/2}\xi\rangle\\
=\sum_i\|x_i\xi\|^2\\
=\langle a\xi,\xi\rangle\\
=\|a^{1/2}\xi\|^2.
\end{gathered}
\] So \((p-c)^{1/2}\) vanishes on a dense subspace of \(pH\), and \(c=p\). In the same way, \(y_j=t_ja^{1/2}\) with \(t_j\in M\) and \(\sum_jt_j^*t_j=p\).

*The decomposition.* Put \(z_{ij}=t_ja^{1/2}s_i^*\in M\). Using \(pa^{1/2}=a^{1/2}\),
\[
\begin{gathered}
\sum_jz_{ij}^*z_{ij}\\
=s_ia^{1/2}\Big(\sum_jt_j^*t_j\Big)a^{1/2}s_i^*\\
=s_ia^{1/2}pa^{1/2}s_i^*\\
=s_ias_i^*\\
=x_ix_i^*,
\end{gathered}
\]
\[
\begin{gathered}
\sum_iz_{ij}z_{ij}^*\\
=t_ja^{1/2}\Big(\sum_is_i^*s_i\Big)a^{1/2}t_j^*\\
=t_jat_j^*\\
=y_jy_j^* .
\end{gathered}
\]
The sums converge strongly: for \(R\in B(H)\), \(\|R(c_\lambda-c)R^*\xi\|\le\|R\|\,\|(c_\lambda-c)R^*\xi\|\), and the partial sums \(c_\lambda\) of \(\sum_jt_j^*t_j\) and \(\sum_is_i^*s_i\) converge strongly. Since they are increasing and bounded, the convergence is also \(\sigma\)-strong\(^*\) ([Lemma 1.2](#oa-fnd-bi-01)(e)). \(\square\)

## 8. One-sided ideals

A one-sided ideal of a von Neumann algebra need not be closed. Its closure is the same in all six topologies, and it is cut out by a single projection. The tool is an increasing approximate unit that lies in the ideal itself.

**Lemma 8.1** (approximate units for right ideals). Let \(M\) be a von Neumann algebra on \(H\) and \(r\subseteq M\) a right ideal (a linear subspace with \(rM\subseteq r\)); \(r\) need not be closed. Let \(f\) be the projection onto \([rH]\).

1. \(f\in M\), and \(fa=a\) for every \(a\in r\).
2. There is an increasing net \((u_\lambda)\) in \(r\), with \(0\le u_\lambda\le f\), such that \(\|(1-u_\lambda)a\|\to0\) for every \(a\in r\).
3. \(u_\lambda\to f\) strongly, \(\sigma\)-strongly\(^*\) and \(\sigma\)-weakly.

**Proof.** (1) \([rH]\) is invariant under \(M'\), since \(y'a\xi=ay'\xi\); and \(M'\) is self-adjoint. So \(f\in M''=M\) by [Proposition 2.1](#oa-fnd-bi-02)(5). For \(a\in r\), \(aH\subseteq[rH]\), so \(fa=a\).

(2) If \(r=\{0\}\), take the one-term net \(u=0\); then \(f=0\). Otherwise \(r\) is an infinite set, being a nonzero complex vector space. Let \(\Lambda\) be the set of finite nonempty subsets of \(r\), directed by inclusion. For \(\lambda\in\Lambda\) with \(n\) elements, put
\[
\begin{gathered}
v_\lambda\\
=\sum_{a\in\lambda}aa^*,\\
u_\lambda\\
=nv_\lambda(1+nv_\lambda)^{-1}\\
=1-(1+nv_\lambda)^{-1}.
\end{gathered}
\tag{8.1}
\]
Here \(v_\lambda\ge0\), and \(1+nv_\lambda\ge1\) is invertible in \(M\) by (C). Since \(a\in r\) and \(a^*\in M\), \(aa^*\in r\); so \(v_\lambda\in r\), and then \(u_\lambda=v_\lambda\cdot n(1+nv_\lambda)^{-1}\in r\). By (C), \(0\le u_\lambda\le1\), because \(t\mapsto nt/(1+nt)\) takes values in \([0,1)\) for \(t\ge0\). By (1), \(fu_\lambda=u_\lambda\), and taking adjoints \(u_\lambda f=u_\lambda\). So \(u_\lambda=fu_\lambda f\le f\).

*The net increases.* Let \(\lambda\subseteq\mu\), with \(n\) and \(m\ge n\) elements. Then \(v_\lambda\le v_\mu\), so \(nv_\lambda\le nv_\mu\le mv_\mu\) and \(1+nv_\lambda\le1+mv_\mu\). Inversion reverses order (C), so \((1+mv_\mu)^{-1}\le(1+nv_\lambda)^{-1}\), which says \(u_\lambda\le u_\mu\).

*The estimate.* Let \(a\in\lambda\). Then \(aa^*\le v_\lambda\), and \(1-u_\lambda=(1+nv_\lambda)^{-1}\) is self-adjoint and commutes with \(v_\lambda\). Conjugating the inequality,
\[
\begin{gathered}
(1-u_\lambda)aa^*(1-u_\lambda)\\
\le(1-u_\lambda)v_\lambda(1-u_\lambda)\\
=v_\lambda(1+nv_\lambda)^{-2}\\
\le\frac1{4n}\,1 ,
\end{gathered}
\tag{8.2}
\]
the last step by (C), since \(t/(1+nt)^2\le1/(4n)\) for \(t\ge0\) (as \((1+nt)^2\ge4nt\)). With \(b=(1-u_\lambda)a\), (8.2) and the C\(^*\)-identity \(\|b\|^2=\|bb^*\|\) give \(\|(1-u_\lambda)a\|^2\le1/(4n)\). Given \(a\in r\) and \(N\ge1\), choose \(\lambda_0\in\Lambda\) that contains \(a\) and has at least \(N\) elements. Every \(\lambda\supseteq\lambda_0\) contains \(a\) and has at least \(N\) elements, so \(\|(1-u_\lambda)a\|\le1/(2\sqrt N)\). Hence \(\|(1-u_\lambda)a\|\to0\).

(3) The net increases and is bounded by \(1\), so by Vigier's theorem (V) it converges strongly to its least upper bound \(u\in M\), and \(u\le f\). For \(a\in r\) and \(\xi\in H\), \((1-u)a\xi=\lim_\lambda(1-u_\lambda)a\xi=0\) by (2). So \(u\xi=\xi\) for all \(\xi\in[rH]=fH\), that is \(uf=f\). From \(0\le u\le f\) we get \(\|u^{1/2}(1-f)\xi\|^2\le\langle f(1-f)\xi,(1-f)\xi\rangle=0\), so \(u(1-f)=0\) and \(u=uf=f\). The other two modes of convergence follow from [Lemma 1.2](#oa-fnd-bi-01)(e). \(\square\)

*Remark 8.2.* In any C\(^*\)-algebra, the positive part of the open unit ball of a left ideal is upward directed and is a right approximate identity for the norm closure of the ideal; see [approximate identities of one-sided ideals](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-20). The net (8.1) is a direct construction with exactly the properties needed here: it is increasing, it lies in the ideal, and it converges strongly to \(f\).

**Theorem 8.3** (closures of one-sided ideals). Let \(M\) be a von Neumann algebra on \(H\).

1. Let \(l\) be a left ideal of \(M\), not necessarily closed, and let \(f\) be the projection onto \([l^*H]\), where \(l^*=\{x^*:x\in l\}\). Then the closure of \(l\) in each of the six topologies is \(Mf=\{y\in M:y=yf\}\).
2. Let \(r\) be a right ideal, and \(f\) the projection onto \([rH]\). Then the closure of \(r\) in each of the six topologies is \(fM\).
3. A left ideal that is closed in one of the six topologies is \(Me\) for exactly one projection \(e\in M\). A closed right ideal is \(eM\) for exactly one projection \(e\in M\).
4. Let \(m\) be a two-sided ideal and \(\overline m\) its closure, which is the same in all six topologies. Let \(e\) be the projection onto \([mH]\). Then \(\overline m=Me=eM\), and \(e\in Z(M)\).
5. If \(M\) is a factor, every two-sided ideal other than \(\{0\}\) is dense in \(M\) for all six topologies.

**Proof.** (2) By [Lemma 8.1](#oa-fnd-bi-10), there is an increasing net \(u_\lambda\in r\) with \(u_\lambda\to f\) strongly, and \(fa=a\) for \(a\in r\). So \(r\subseteq fM\). The set \(fM=\{y\in M:(1-f)y=0\}\) is closed in all six topologies, since \(M\) is closed ([Proposition 2.4](#oa-fnd-bi-03)(2)) and \(y\mapsto(1-f)y\) is continuous ([Lemma 1.2](#oa-fnd-bi-01)(c)). So each closure of \(r\) lies in \(fM\). Conversely, let \(y\in M\). Then \(u_\lambda y\in r\), \(\|u_\lambda y\|\le\|y\|\), \(u_\lambda y\to fy\) strongly, and \((u_\lambda y)^*=y^*u_\lambda\to y^*f\) strongly. By [Lemma 1.2](#oa-fnd-bi-01)(d), \(u_\lambda y\to fy\) \(\sigma\)-strongly\(^*\). This is the finest of the six topologies, so \(fy\) lies in every one of the six closures of \(r\).

(1) \(l^*\) is a right ideal, and its net \(u_\lambda\) from [Lemma 8.1](#oa-fnd-bi-10) consists of self-adjoint elements, which therefore lie in \(l\). For \(x\in l\), \(fx^*=x^*\), so \(x=xf\); thus \(l\subseteq Mf\), and \(Mf\) is closed as in (2). For \(y\in M\), \(yu_\lambda\in l\), and \(yu_\lambda\to yf\) \(\sigma\)-strongly\(^*\) as in (2). So every closure of \(l\) equals \(Mf\).

(3) A closed left ideal is its own closure, so it equals \(Mf\) by (1). If \(Me=Me'\) for projections \(e,e'\in M\), then \(e\in Me'\) gives \(e=ee'\), and likewise \(e'=e'e\). Hence \(e=e^*=(ee')^*=e'e=e'\). Right ideals are treated in the same way.

(4) By (1) and (2), \(\overline m=Mf=f'M\), with \(f\) the projection onto \([m^*H]\) and \(f'\) the projection onto \([mH]\). From \(f\in f'M\) we get \(f'f=f\), and from \(f'\in Mf\) we get \(f'f=f'\). So \(f=f'=e\). For \(x\in M\), \(ex\in eM=Me\) gives \(ex=exe\), and \(xe\in Me=eM\) gives \(xe=exe\). So \(ex=xe\), and \(e\in Z(M)\).

(5) In a factor, the central projection \(e\) of (4) is \(0\) or \(1\). It is not \(0\), since \(m\neq0\) and \(m\subseteq Me\). So \(e=1\) and \(\overline m=M\). \(\square\)

*Remark 8.4.* The theorem identifies the closure of any one-sided ideal. It also shows that for one-sided ideals, being closed in one of the six topologies is the same as being closed in all of them. For general subspaces this fails ([Exercise 1.5](#oa-fnd-bi-01)). Norm-closed ideals need not be weakly closed: \(K(H)\) is a norm-closed two-sided ideal of the factor \(B(H)\), and by (5) it is dense in \(B(H)\) when \(\dim H=\infty\) ([Example 4.6](#oa-fnd-bi-07)).

**Proposition 8.5** (monotone approximation in two-sided ideals). Take a two-sided ideal \(m\) in a von Neumann algebra \(M\), not assumed closed. Let \(e\) be the projection onto \([mH]\), so that \(\overline m=Me\) by Theorem 8.3, and let \((u_\lambda)\) be the net of Lemma 8.1 for the right ideal \(m\). Let \(x\in\overline m\) be positive, that is \(x\in M_+\) with \(x=xe\). Put \(x_\lambda=x^{1/2}u_\lambda x^{1/2}\). Then \(x_\lambda\in m\), \(0\le x_\lambda\le x\), the net \((x_\lambda)\) increases, and \(x_\lambda\to x\) strongly, \(\sigma\)-strongly\(^*\) and \(\sigma\)-weakly.

**Proof.** \(x^{1/2}\in M\) by (C). Since \(u_\lambda\in m\) and \(m\) is two-sided, \(x_\lambda\in m\). Conjugation by \(x^{1/2}\) preserves order, so \(x_\lambda\ge0\) and the net increases. From \(x(1-e)=0\) we get \(\|x^{1/2}(1-e)\xi\|^2=\langle x(1-e)\xi,(1-e)\xi\rangle=0\), so \(x^{1/2}=x^{1/2}e\) and, taking adjoints, \(x^{1/2}=ex^{1/2}\). Hence \(x^{1/2}ex^{1/2}=x\). As \(u_\lambda\le e\), \(x_\lambda\le x^{1/2}ex^{1/2}=x\). For \(\xi\in H\), \(x_\lambda\xi=x^{1/2}u_\lambda(x^{1/2}\xi)\to x^{1/2}ex^{1/2}\xi=x\xi\). The net is self-adjoint and bounded by \(\|x\|\), so [Lemma 1.2](#oa-fnd-bi-01)(d) gives the other two modes. \(\square\)

The bound \(x_\lambda\le x\) is automatic for an increasing net with strong limit \(x\), but the construction gives it directly. Two-sidedness cannot be dropped: [Example 8.6](#oa-fnd-bi-11) is a left ideal for which the conclusion fails.

**Example 8.6** (monotone approximation fails for one-sided ideals). Let \(H=\ell^2(\mathbb N)\) with basis \((\delta_k)\), let \(P_n\) be the projection onto the span of \(\delta_1,\dots,\delta_n\), and let \(l=\{x\in B(H):x=xP_n\text{ for some }n\}\). This is a left ideal. Its adjoint set \(l^*\) consists of the operators with range in some \(P_nH\), so \([l^*H]=H\), and by [Theorem 8.3](#oa-fnd-bi-11)(1) the closure of \(l\) is \(B(H)\). Let \(v=\sum_k2^{-k}\delta_k\) and let \(q\) be the projection onto \(\mathbb Cv\). Suppose \(y\in l\) and \(0\le y\le q\). Then \((1-q)y(1-q)\le0\), so \(y^{1/2}(1-q)=0\), and \(y=qyq=cq\) for some \(c\ge0\). Also \(y=yP_n\) for some \(n\). If \(c>0\), then \(q=qP_n\), hence \(q=P_nq\) and \(v\in P_nH\), which is false. So \(y=0\). An increasing net in \(l_+\) that converged strongly to \(q\) would lie below \(q\), since \(\langle y_\lambda\xi,\xi\rangle\le\lim_\mu\langle y_\mu\xi,\xi\rangle=\langle q\xi,\xi\rangle\). So it would be zero, and could not converge to \(q\). The positive element \(q\) of the closure of \(l\) is therefore not the limit of any increasing net in \(l_+\).

## 9. Cyclic and separating vectors; σ-finite algebras

A set of vectors can generate the whole space under an algebra, or it can detect every nonzero element of the algebra. Passing to the commutant exchanges the two properties. Countable versions of them characterize the \(\sigma\)-finite von Neumann algebras, which are those with a faithful positive normal functional.

**Definition 9.1.** Let \(S\subseteq B(H)\) and \(\mathfrak A\subseteq H\). The set \(\mathfrak A\) is *separating* for \(S\) if \(x\in S\) and \(x\mathfrak A=\{0\}\) imply \(x=0\). It is *cyclic* for \(S\) if \([S\mathfrak A]=H\). A vector \(\xi\) is separating or cyclic if \(\{\xi\}\) is.

**Proposition 9.2.** Let \(S\subseteq B(H)\) and \(\mathfrak A\subseteq H\).

1. If \(\mathfrak A\) is cyclic for \(S\), then \(\mathfrak A\) is separating for \(S'\).
2. If \(M\) is a nondegenerate \(*\)-subalgebra of \(B(H)\), closed or not, and \(\mathfrak A\) is separating for \(M'\), then \(\mathfrak A\) is cyclic for \(M\).
3. For a von Neumann algebra \(M\): \(\mathfrak A\) is cyclic for \(M\) if and only if it is separating for \(M'\), and \(\mathfrak A\) is separating for \(M\) if and only if it is cyclic for \(M'\).
4. Nondegeneracy cannot be dropped in (2). For \(M=\{0\}\) on \(H\neq\{0\}\), \(M'=B(H)\), and \(\mathfrak A=H\) is separating for \(M'\) but not cyclic for \(M\).

**Proof.** (1) Let \(x'\in S'\) with \(x'\mathfrak A=\{0\}\). For \(s\in S\) and \(\xi\in\mathfrak A\), \(x's\xi=sx'\xi=0\). So \(x'\) vanishes on the span of \(S\mathfrak A\) and, being continuous, on \([S\mathfrak A]=H\).

(2) Let \(p\) be the projection onto \([M\mathfrak A]\). This subspace is invariant under \(M\), and \(M^*=M\), so \(p\in M'\) ([Proposition 2.1](#oa-fnd-bi-02)(5)). By [Lemma 4.1](#oa-fnd-bi-06), each \(\xi\in\mathfrak A\) lies in \([M\xi]\subseteq[M\mathfrak A]\). So \((1-p)\mathfrak A=\{0\}\). Since \(1-p\in M'\) and \(\mathfrak A\) is separating for \(M'\), \(1-p=0\).

(3) \(M\) is nondegenerate ([Proposition 2.4](#oa-fnd-bi-03)(2)), so (1) and (2) give the first equivalence. For the second, apply the first to the von Neumann algebra \(M'\), whose commutant is \(M\).

(4) Here \([M\mathfrak A]=\{0\}\). \(\square\)

A vector \(\xi\) is separating for \(M\) exactly when the positive functional \(\omega_\xi\) is faithful on \(M\), since \(\omega_\xi(x^*x)=\|x\xi\|^2\). This is the idea behind the implication (2)\(\Rightarrow\)(4) of [Theorem 9.5](#oa-fnd-bi-13).

**Exercise 9.3** (medium; separating and cyclic vectors for \(M_n\otimes1_k\)). Let \(n,k\ge1\), \(I=\{1,\dots,k\}\), and \(M=\pi(B(\mathbb C^n))\) on \(\tilde H=\ell^2(I;\mathbb C^n)\) as in [Section 3](#oa-fnd-bi-05); this is \(M_n(\mathbb C)\otimes1_k\). Write a vector as \(\xi=(\xi_1,\dots,\xi_k)\), or as the \(n\times k\) matrix \(X\) with columns \(\xi_j\). Show that \(M''=M\) and that \(M'\) consists of the scalar \(k\times k\) matrices tensored with \(1_{\mathbb C^n}\). Show that \(\xi\) is separating for \(M\) if and only if \(\operatorname{rank}X=n\), and cyclic for \(M\) if and only if \(\operatorname{rank}X=k\). Deduce that \(M\) has a separating vector if and only if \(k\ge n\), a cyclic vector if and only if \(k\le n\), and a vector that is both if and only if \(k=n\).

*Solution.* By Corollary 3.4 and [Proposition 2.4](#oa-fnd-bi-03)(4), \(M''=\pi(B(\mathbb C^n)'')=M\). By (3.4), \(M'\) consists of the \(k\times k\) matrices whose entries lie in \(B(\mathbb C^n)'=\mathbb C1\). *Separating:* \(\pi(x)\xi=(x\xi_1,\dots,x\xi_k)=0\) forces \(x=0\) exactly when the columns \(\xi_j\) span \(\mathbb C^n\), that is \(\operatorname{rank}X=n\). *Cyclic:* \([M\xi]=\{(x\xi_1,\dots,x\xi_k):x\in M_n(\mathbb C)\}\), a subspace since \(M\xi\) is finite dimensional. If the \(\xi_j\) are linearly independent, extend them to a basis of \(\mathbb C^n\); a linear map \(x\) can then take any prescribed values on them, so \([M\xi]=\tilde H\). If \(\sum_jc_j\xi_j=0\) with some \(c_j\neq0\), every vector of \([M\xi]\) satisfies the same relation, so \([M\xi]\neq\tilde H\). Hence \(\xi\) is cyclic exactly when \(\operatorname{rank}X=k\). An \(n\times k\) matrix of rank \(n\) exists exactly when \(n\le k\), and one of rank \(k\) exactly when \(k\le n\). As a check against [Proposition 9.2](#oa-fnd-bi-12)(3): \(M'\) acts by \(X\mapsto XB^{\mathsf T}\) for scalar \(k\times k\) matrices \(B\), and its orbit of \(X\) is the set of matrices whose columns lie in the column space of \(X\); this is everything exactly when \(\operatorname{rank}X=n\). \(\square\)

**Definition 9.4.** A von Neumann algebra \(M\) is *\(\sigma\)-finite* (also called *countably decomposable*) if every family of mutually orthogonal nonzero projections in \(M\) is countable.

A linear functional \(\varphi\) on \(M\) is *positive* if \(\varphi(x^*x)\ge0\) for all \(x\), and a positive \(\varphi\) is *faithful* if \(\varphi(x^*x)=0\) implies \(x=0\). A *state* is a positive functional with \(\varphi(1)=1\). A linear functional on \(M\) is *normal* if it is \(\sigma\)-weakly continuous.

**Theorem 9.5** (\(\sigma\)-finite von Neumann algebras). For a von Neumann algebra \(M\) on \(H\), the following are equivalent.

1. \(M\) is \(\sigma\)-finite.
2. \(H\) contains a countable set that is separating for \(M\).
3. \(H\) contains a countable set that is cyclic for \(M'\).
4. There is a faithful positive \(\sigma\)-weakly continuous linear functional on \(M\).
5. There is a faithful positive linear functional on \(M\), with no continuity assumed.

If \(H\neq\{0\}\), the functional in (4) can be taken to be a state, that is, with \(\varphi(1)=1\).

**Proof.** (2)\(\Leftrightarrow\)(3) is [Proposition 9.2](#oa-fnd-bi-12)(3).

(1)\(\Rightarrow\)(3). Let \(\mathcal F\) be the collection of sets \(F\) of nonzero vectors such that the subspaces \([M'\xi]\), \(\xi\in F\), are mutually orthogonal. The empty set belongs to \(\mathcal F\), and the union of a chain in \(\mathcal F\) is in \(\mathcal F\), because any two of its vectors lie in one member of the chain. By Zorn's lemma there is a maximal \(F\in\mathcal F\). For \(\xi\in F\), the projection \(p_\xi\) onto \([M'\xi]\) lies in \(M\): the subspace is invariant under the self-adjoint algebra \(M'\), so \(p_\xi\in M''=M\) ([Proposition 2.1](#oa-fnd-bi-02)(5)). Also \(p_\xi\neq0\), because \(\xi\in[M'\xi]\) (as \(1\in M'\)). Distinct vectors of \(F\) give orthogonal, hence distinct, projections. By (1), \(F\) is countable. Suppose \([M'F]\neq H\), and pick a nonzero \(\eta\perp[M'F]\). For each \(\xi\in F\), \(\eta\) lies in \([M'\xi]^\perp\), which is invariant under \(M'\) ([Proposition 2.1](#oa-fnd-bi-02)(5)); so \([M'\eta]\perp[M'\xi]\). Also \(\eta\notin F\), since \(\eta\perp\xi\) for every \(\xi\in F\) and \(\eta\neq0\). So \(F\cup\{\eta\}\in\mathcal F\), contradicting maximality. Hence \(F\) is a countable cyclic set for \(M'\).

(2)\(\Rightarrow\)(4). Let \(\mathfrak A\) be a countable separating set. Removing \(0\) keeps it separating. If nothing is left, every \(x\in M\) is \(0\); then \(M=\{0\}\), so \(H=\{0\}\) (as \(1\in M\)) and \(\varphi=0\) is faithful. Otherwise list the nonzero vectors as \(\xi_1,\xi_2,\dots\) (finitely or infinitely many) and put
\[
\varphi(x)=\sum_n2^{-n}\|\xi_n\|^{-2}\langle x\xi_n,\xi_n\rangle .
\tag{9.1}
\]
This is \(\sum_n\langle x\zeta_n,\zeta_n\rangle\) with \(\zeta_n=2^{-n/2}\xi_n/\|\xi_n\|\) and \(\sum_n\|\zeta_n\|^2\le1\). So \(\varphi\) is positive and \(\sigma\)-weakly continuous. The functional (9.1) is faithful: if \(\varphi(x^*x)=\sum_n2^{-n}\|x\xi_n\|^2/\|\xi_n\|^2=0\), then \(x\xi_n=0\) for all \(n\), so \(x=0\). Dividing by \(\varphi(1)>0\) gives a faithful normal state.

(4)\(\Rightarrow\)(5) is trivial.

(5)\(\Rightarrow\)(1). Let \(\varphi\) be faithful and positive, and let \((e_i)_{i\in I}\) be mutually orthogonal nonzero projections in \(M\). Faithfulness gives \(\varphi(e_i)=\varphi(e_i^*e_i)>0\). For a finite \(G\subseteq I\), \(\sum_{i\in G}e_i\) is a projection, so \(1-\sum_{i\in G}e_i\ge0\) and \(\sum_{i\in G}\varphi(e_i)\le\varphi(1)\). Hence \(I_n=\{i:\varphi(e_i)\ge1/n\}\) has at most \(n\varphi(1)\) elements, and \(I=\bigcup_nI_n\) is countable. \(\square\)

*Remark 9.6.* A countable separating set cannot always be replaced by one vector, and \(\sigma\)-finiteness of \(M\) does not pass to \(M'\) ([Example 9.7](#oa-fnd-bi-13)). Every von Neumann algebra on a separable Hilbert space is \(\sigma\)-finite: a countable dense subset is separating, because a bounded operator that vanishes on a dense set is zero.

**Example 9.7** (separating vectors and \(\sigma\)-finiteness). \(M=B(\mathbb C^2)\) is \(\sigma\)-finite, and a basis is a separating set. No single vector separates: for \(\xi\neq0\), choose a nonzero \(\eta\perp\xi\); then \(\theta_{\eta,\eta}\xi=0\). Every nonzero vector is cyclic for \(M\). Now let \(\Gamma\) be uncountable and \(M=\mathbb C1\) on \(\ell^2(\Gamma)\). It is \(\sigma\)-finite, and every nonzero vector separates it. But \(M'=B(\ell^2(\Gamma))\) contains the uncountable family of mutually orthogonal rank-one projections onto the basis vectors, so \(M'\) is not \(\sigma\)-finite. By [Theorem 9.5](#oa-fnd-bi-13), (5)\(\Rightarrow\)(1), \(B(\ell^2(\Gamma))\) has no faithful positive functional at all.

**Exercise 9.8** (easy; no faithful functional on a large \(B(H)\)). For an uncountable set \(\Gamma\), show that \(B(\ell^2(\Gamma))\) has no faithful positive linear functional, normal or not, while its commutant \(\mathbb C1\) has a faithful normal state.

*Solution.* The rank-one projections onto the basis vectors \(\delta_\gamma\) form an uncountable family of mutually orthogonal nonzero projections, so \(B(\ell^2(\Gamma))\) is not \(\sigma\)-finite. By [Theorem 9.5](#oa-fnd-bi-13), (5)\(\Rightarrow\)(1), it has no faithful positive functional. On \(\mathbb C1\), \(\omega_\xi\) for a unit vector \(\xi\) is a normal state, and \(\omega_\xi((\lambda1)^*(\lambda1))=|\lambda|^2\) vanishes only for \(\lambda=0\). \(\square\)

### Probability products for the large-Hilbert-space example

Exercise 9.9 uses independent coordinates indexed by an arbitrary set. A finite product is insufficient when uncountably many coordinates must supply orthogonal vectors. Here we construct the required measure without assuming that the factor spaces are standard Borel, or even that they have topologies.

The measure tools are Carathéodory's theorem and monotone convergence, Theorems 1.1 and 2.1 of *Measure and Hilbert space tools for Haar integration*. In particular, monotone convergence gives \(\int\sum_n f_n=\sum_n\int f_n\) for nonnegative measurable functions. Choice is used to select points in nonempty factor spaces. Fremlin's [§254](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm) is a reference for the classical product theorem.

**Lemma (Uniqueness from a generating family).** Let \(\mathcal P\) be a family of subsets of \(X\) containing \(X\) and closed under finite intersections. Two finite measures on \(\sigma(\mathcal P)\) that agree on \(\mathcal P\) agree everywhere.

*Proof.* A *Dynkin system* contains \(X\), is closed under the difference \(B\setminus A\) when \(A\subseteq B\) are members, and is closed under countable disjoint unions. Let \(\mathcal D\) be the smallest Dynkin system containing \(\mathcal P\), obtained by intersecting all such systems.

Fix \(P\in\mathcal P\). The members \(B\in\mathcal D\) for which \(P\cap B\in\mathcal D\) form a Dynkin system. Indeed, they contain \(X\); intersections with \(P\) preserve nested differences and disjoint unions. This system contains \(\mathcal P\), so it contains \(\mathcal D\). Now fix any \(B\in\mathcal D\). The members \(A\in\mathcal D\) with \(A\cap B\in\mathcal D\) again form a Dynkin system, and the preceding conclusion says that they contain \(\mathcal P\). Thus \(\mathcal D\) is closed under finite intersections. Nested differences give complements, and finite intersections give finite unions. Disjointifying a countable union then shows that \(\mathcal D\) is a sigma-algebra. Hence \(\mathcal D=\sigma(\mathcal P)\).

For the two measures, the sets on which their values agree form a Dynkin system: the value at \(X\) agrees, subtraction is valid for nested sets because the measures are finite, and countable additivity handles disjoint unions. This system contains \(\mathcal P\), hence \(\sigma(\mathcal P)\). \(\square\)

**Theorem (Arbitrary products of probability spaces).** Let \((X_i,\Sigma_i,\mu_i)_{i\in I}\) be any family of probability spaces. On \(X=\prod_{i\in I}X_i\), let \(\Sigma\) be the sigma-algebra generated by the coordinate maps. There is a unique probability measure \(\mu\) on \(\Sigma\) such that
\[
\begin{gathered}
\mu\{x:x_i\in E_i\text{ for }i\in F\}
=\prod_{i\in F}\mu_i(E_i),\\
F\subseteq I\text{ finite},\qquad E_i\in\Sigma_i.
\end{gathered}
\]
It has a complete extension obtained by Carathéodory's construction. Each coordinate map has distribution \(\mu_i\). No cardinality, separability or completeness condition is imposed on the factors.

*Proof.* A *rectangle cylinder* is the empty set or a set
\[
C=\{x:x_i\in E_i\text{ for }i\in F\},
\]
where \(F\subseteq I\) is finite and \(E_i\in\Sigma_i\).
Give it weight \(w(C)=\prod_{i\in F}\mu_i(E_i)\), with \(w(\varnothing)=0\) and the empty product equal to one. This is well defined. For a nonempty cylinder, its projection onto each constrained coordinate is exactly \(E_i\), since points can be chosen in all the other nonempty factors. Adding a redundant full coordinate changes no weight. An empty cylinder has an empty constrained factor, and therefore weight zero.

**A cover cannot cost less than one.** Suppose rectangle cylinders \(C_n\) cover \(X\). We claim \(\sum_nw(C_n)\ge1\). Only countably many coordinates occur among their finite constraint sets. If none occur, each \(C_n\) is empty or \(X\), and the claim follows. Otherwise enumerate these coordinates as \(j_1,j_2,\ldots\), stopping after the last coordinate when the set is finite. Write \(E_{n,j}\) for the constraint of \(C_n\) at \(j\), taking \(E_{n,j}=X_j\) at unconstrained coordinates.

Let \(F_n\) be the finite constraint set chosen for \(C_n\). Assume for contradiction that \(S_0=\sum_nw(C_n)<1\). After selecting \(x_{j_1},\ldots,x_{j_k}\), put
\[
\begin{gathered}
J_k=\{j_1,\ldots,j_k\},\\
a_{n,k}=\prod_{j\in F_n\setminus J_k}\mu_j(E_{n,j}),\\
S_k=\sum_n a_{n,k}
\prod_{\ell\le k}1_{E_{n,j_\ell}}(x_{j_\ell}).
\end{gathered}
\]
The product defining \(a_{n,k}\) is finite. Regard \(S_{k+1}\) as a nonnegative measurable function of the next coordinate. Monotone convergence, applied to the series, gives
\[
\int_{X_{j_{k+1}}}S_{k+1}(t)\,d\mu_{j_{k+1}}(t)=S_k.
\]
If \(S_k<1\), some \(t\) has \(S_{k+1}(t)<1\); otherwise its integral over this probability space would be at least one. Select such a \(t\) and continue.

Once all the constrained coordinates of a particular \(C_n\) have been selected, membership in \(C_n\) would make its summand equal to one. This contradicts \(S_k<1\). The selected coordinates therefore avoid every \(C_n\). Choose arbitrary values at all remaining coordinates. The resulting point is outside their union, contradicting the cover. This proves the claim for finite as well as countably infinite sets of relevant coordinates.

**An outer measure with the correct cylinder values.** For every \(A\subseteq X\), define
\[
m^*(A)=\inf\sum_nw(C_n),
\]
where the infimum runs over all countable covers of \(A\) by rectangle cylinders \(C_n\).
This is an outer measure. Monotonicity is immediate. The empty set has a zero-cost cover, and combining covers whose errors are bounded by \(\varepsilon2^{-n}\) proves countable subadditivity. Every set has a cover of cost one, since \(X\) itself is a cylinder. The cover claim gives \(m^*(X)=1\).

We also have \(m^*(C)=w(C)\) for each cylinder \(C\). The upper bound comes from the one-member cover. It settles the case \(w(C)=0\). If \(w(C)>0\), replace the finitely many constrained factor spaces by \(E_i\) with their relative sigma-algebras and conditional probabilities
\[
\mu_i^C(B)=\frac{\mu_i(B)}{\mu_i(E_i)}
\]
for relatively measurable \(B\subseteq E_i\).
Their Cartesian product is \(C\). A cover of \(C\) by cylinders \(D_n\) induces a cylinder cover \(D_n\cap C\) in these conditional spaces. Its \(n\)-th weight is
\[
\frac{w(D_n\cap C)}{w(C)}
\le\frac{w(D_n)}{w(C)}.
\]
The cover claim, now for the conditional probability spaces, yields \(w(C)\le\sum_nw(D_n)\). Taking the infimum proves the lower bound.

**Coordinate sets are measurable.** Fix \(i\) and \(E\in\Sigma_i\), and put \(P=\{x:x_i\in E\}\). Every cylinder \(C\) splits into the cylinders \(C\cap P\) and \(C\setminus P\), with
\[
w(C\cap P)+w(C\setminus P)=w(C).
\]
Apply this splitting to any cylinder cover of \(A\). It gives
\[
m^*(A\cap P)+m^*(A\setminus P)
\le\sum_nw(C_n).
\]
Take the infimum over covers. The reverse inequality is outer subadditivity. Thus \(P\) satisfies Carathéodory's condition. Theorem 1.1 of the measure-tools lesson supplies a complete measure on all sets satisfying that condition. Its domain contains \(\Sigma\), so its restriction \(\mu\) to \(\Sigma\) is a probability measure with the asserted cylinder values. These values also give the coordinate distributions.

Rectangle cylinders form a family containing \(X\), closed under finite intersections, and generating \(\Sigma\). The uniqueness lemma proves uniqueness on \(\Sigma\). The theorem does not assert that \(\Sigma\) itself is complete; the Carathéodory extension provides completeness on its larger domain. \(\square\)

**Example (independent signs).** Give each \(X_i=\{-1,1\}\) its probability assigning mass \(1/2\) to each point. The coordinate functions \(r_i(x)=x_i\) have \(L^2\) norm one and integral zero. For \(i\ne j\), the four two-coordinate cylinders have mass \(1/4\), so \(\int r_ir_j\,d\mu=0\). An uncountable index set therefore gives an uncountable orthonormal family in \(L^2(\mu)\). Exercise 9.9 extends this computation to factors with unequal probabilities and proves the cyclic and separating assertions.

**Exercise (medium): countable coordinate dependence.** Show that every set in \(\Sigma\) belongs to the sigma-algebra generated by some countable set of coordinates. Deduce that every complex \(\Sigma\)-measurable function depends on countably many coordinates.

*Solution.* The sets with the stated property form a sigma-algebra: complements retain the same coordinates, and a countable union uses the union of countably many countable coordinate sets. This sigma-algebra contains every coordinate cylinder, so it contains \(\Sigma\). For a measurable complex function, apply the set assertion to the inverse images of a countable base of \(\mathbb C\), and take the union \(J\) of their coordinate sets. If two points have the same coordinates in \(J\), they lie in exactly the same inverse images of these basic open sets. Their function values must be equal, since the base separates distinct points. Thus the function factors through the projection to \(X_J\). This assertion concerns \(\Sigma\); completion can add null subsets involving further coordinates.


**Exercise 9.9** (medium; a cyclic and separating vector in a large Hilbert space). Let \((\Gamma_i,\mu_i)_{i\in I}\) be an uncountable family of probability spaces, let \((\Gamma,\mu)\) be the product space, \(H=L^2(\Gamma,\mu)\), and let \(M\) be the von Neumann algebra generated by the multiplication operators \(m_f\), for bounded measurable \(f\). Show that the function equal to \(1\) everywhere is cyclic and separating for \(M\). Suppose moreover that uncountably many factors are *nontrivial*: for uncountably many \(i\) there is a measurable \(B_i\subseteq\Gamma_i\) with \(0<\mu_i(B_i)<1\). Show that \(H\) is then not separable. Some hypothesis of this kind is needed: if every \(\Gamma_i\) is a one-point space, then \(\Gamma\) is one point and \(H=\mathbb C\) is separable.

The one-point example in the question proves that an uncountable index set alone does not imply nonseparability.

*Solution.* The [probability product theorem just proved](#oa-fnd-bi-18) supplies the product measure on the coordinate sigma-algebra, with no restrictions on the factors. *Cyclic:* \([M1]\) contains every bounded measurable \(f=m_f1\). These are dense in \(L^2\): for \(g\in L^2\), \(g1_{\{|g|\le k\}}\to g\) in \(L^2\) by dominated convergence. *Separating:* the operators \(m_f\) commute with each other, so \(\{m_f\}\subseteq\{m_f\}'=\{m_f\}'''=M'\) ([Proposition 2.1](#oa-fnd-bi-02)(2)). Hence \([M'1]\supseteq[\{m_f\}1]=L^2\), so \(1\) is cyclic for \(M'\) and separating for \(M=M''\) by [Proposition 9.2](#oa-fnd-bi-12)(1). (In fact \(M=\{m_f\}\), by [Theorem 9.1 of the Hilbert-space lesson](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-09), since \(\mu\) is finite.) *Not separable, under the nontriviality hypothesis:* let \(J\) be the uncountable set of nontrivial indices. For \(i\in J\) let \(c_i=\mu_i(B_i)\), let \(\gamma_i:\Gamma\to\Gamma_i\) be the coordinate map, and
\[
g_i=\frac{1_{B_i}\circ\gamma_i-c_i}{\sqrt{c_i(1-c_i)}} .
\]
Then \[
\begin{gathered}
\int|g_i|^2\,d\mu\\
=\big(c_i(1-c_i)^2+(1-c_i)c_i^2\big)/\big(c_i(1-c_i)\big)\\
=1
\end{gathered}
\] and \(\int g_i\,d\mu=0\). For \(i\neq j\) the coordinates are independent under the product measure, so \(\int g_i\bar g_j\,d\mu=\int g_i\,d\mu\int\bar g_j\,d\mu=0\). So \((g_i)_{i\in J}\) is an uncountable orthonormal family. Distinct members are at distance \(\sqrt2\), so the open balls of radius \(\sqrt2/2\) around them are disjoint, and no countable set can meet all of them. Hence \(H\) is not separable. \(\square\)

## 10. Positive normal functionals as sums of vector functionals

A vector functional \(\omega_\xi\) is positive and normal. Conversely, every positive normal functional is a sum of countably many vector functionals: on an amplification it becomes a single vector functional.

**Theorem 10.1.** Let \(M\) be a \(*\)-subalgebra of \(B(H)\) that contains \(1\), closed or not. Let \(\varphi:M\to\mathbb C\) be linear and positive, and continuous for the \(\sigma\)-strong topology restricted to \(M\). Then there is a sequence \((\xi_n)\) in \(H\) with \(\sum_n\|\xi_n\|^2<\infty\) and
\[
\begin{gathered}
\varphi(x)\\
=\sum_n\langle x\xi_n,\xi_n\rangle\\
(x\in M).
\end{gathered}
\tag{10.1}
\]
If \(\varphi\) is continuous for the strong topology, finitely many vectors suffice. Every \(\sigma\)-weakly continuous functional is \(\sigma\)-strongly continuous ([Lemma 1.2](#oa-fnd-bi-01)(b)). So the theorem applies to every positive normal functional on a von Neumann algebra.

**Proof.** *Step 1.* By continuity at \(0\) and [Lemma 1.2](#oa-fnd-bi-01)(a), there are a square-summable \((\zeta_n)\) and \(\delta>0\) such that \(p(x)=(\sum_n\|x\zeta_n\|^2)^{1/2}<\delta\) implies \(|\varphi(x)|<1\), for \(x\in M\). By homogeneity, \(|\varphi(x)|\le\delta^{-1}p(x)\). (If \(p(x)=0\), then \(p(tx)=0\) for all \(t\), so \(|\varphi(x)|<1/t\) for all \(t>0\).) Replace \(\zeta_n\) by \(\zeta_n/\delta\). With \(\tilde H=\ell^2(\mathbb N;H)\), the amplification \(\pi\) of [Section 3](#oa-fnd-bi-05), and \(\tilde\zeta=(\zeta_n)\in\tilde H\), this reads \(|\varphi(x)|\le\|\pi(x)\tilde\zeta\|\).

*Step 2.* Let \(L=[\pi(M)\tilde\zeta]\). The rule \(\pi(x)\tilde\zeta\mapsto\varphi(x)\) is well defined and bounded by Step 1. It extends to a bounded functional on \(L\), and the Riesz theorem (H) gives \(\tilde\eta\in L\) with \(\varphi(x)=\langle\pi(x)\tilde\zeta,\tilde\eta\rangle\) for \(x\in M\).

*Step 3.* A positive functional on a unital \(*\)-algebra is hermitian: \(\varphi(x^*)=\overline{\varphi(x)}\). Indeed, for \(h=h^*\in M\), the numbers \(\varphi(1)\), \(\varphi(h^2)\) and \(\varphi((1+h)^2)=\varphi(1)+2\varphi(h)+\varphi(h^2)\) are real, so \(\varphi(h)\) is real. Then write \(x=h+ik\) with \(h=(x+x^*)/2\) and \(k=(x-x^*)/(2i)\) in \(M\). Hence \(\varphi(x)=\overline{\varphi(x^*)}=\overline{\langle\pi(x^*)\tilde\zeta,\tilde\eta\rangle}=\langle\pi(x)\tilde\eta,\tilde\zeta\rangle\). Adding the two expressions for \(\varphi(x)\), with \(\tilde\theta=\tilde\zeta+\tilde\eta\) and \(\tilde\kappa=\tilde\zeta-\tilde\eta\),
\[
\begin{gathered}
4\varphi(x)\\
=2\langle\pi(x)\tilde\zeta,\tilde\eta\rangle\\
+2\langle\pi(x)\tilde\eta,\tilde\zeta\rangle\\
=\langle\pi(x)\tilde\theta,\tilde\theta\rangle\\
-\langle\pi(x)\tilde\kappa,\tilde\kappa\rangle .
\end{gathered}
\tag{10.2}
\]
Applied to \(x^*x\), (10.2) gives \(4\varphi(x^*x)\le\langle\pi(x^*x)\tilde\theta,\tilde\theta\rangle=\|\pi(x)\tilde\theta\|^2\), because \(\langle\pi(x^*x)\tilde\kappa,\tilde\kappa\rangle=\|\pi(x)\tilde\kappa\|^2\ge0\).

*Step 4.* The form \((x,y)\mapsto\varphi(y^*x)\) on \(M\) is sesquilinear, hermitian by Step 3, and positive semidefinite. The Cauchy–Schwarz inequality for such forms (H) gives \(|\varphi(y^*x)|^2\le\varphi(x^*x)\varphi(y^*y)\). With Step 3, \(|\varphi(y^*x)|\le\frac14\|\pi(x)\tilde\theta\|\,\|\pi(y)\tilde\theta\|\). Let \(L_\theta=[\pi(M)\tilde\theta]\). The rule \(B(\pi(x)\tilde\theta,\pi(y)\tilde\theta)=\varphi(y^*x)\) is therefore a well-defined sesquilinear form on the subspace \(\pi(M)\tilde\theta\), bounded by \(1/4\) and positive. It extends to \(L_\theta\). By (H) there is \(h\in B(L_\theta)\) with \(0\le h\le\tfrac14\,1\) and \(\varphi(y^*x)=\langle h\pi(x)\tilde\theta,\pi(y)\tilde\theta\rangle\) for all \(x,y\in M\).

*Step 5.* \(L_\theta\) is invariant under \(\pi(M)\), and \(h\) commutes with the restrictions: for \(x,y,z\in M\),
\[
\begin{gathered}
\langle h\pi(z)\pi(x)\tilde\theta,\pi(y)\tilde\theta\rangle\\
=\varphi(y^*zx)\\
=\varphi((z^*y)^*x)\\
=\langle h\pi(x)\tilde\theta,\pi(z^*y)\tilde\theta\rangle\\
=\langle\pi(z)h\pi(x)\tilde\theta,\pi(y)\tilde\theta\rangle .
\end{gathered}
\]
By density, \(h\pi(z)=\pi(z)h\) on \(L_\theta\). By (C), \(h^{1/2}\) commutes with \(\pi(z)\) on \(L_\theta\) as well. Since \(1\in M\), \(\tilde\theta\in L_\theta\). Put \(\tilde\xi=h^{1/2}\tilde\theta\in L_\theta\subseteq\tilde H\) and write \(\tilde\xi=(\xi_n)\). Then for \(x\in M\),
\[
\begin{gathered}
\varphi(x)\\
=\varphi(1^*x)\\
=\langle h\pi(x)\tilde\theta,\tilde\theta\rangle\\
=\langle\pi(x)h^{1/2}\tilde\theta,h^{1/2}\tilde\theta\rangle\\
=\sum_n\langle x\xi_n,\xi_n\rangle ,
\end{gathered}
\]
which is (10.1), with \(\sum_n\|\xi_n\|^2=\|\tilde\xi\|^2<\infty\).

*The finite case.* If \(\varphi\) is strongly continuous, Step 1 produces finitely many vectors \(\zeta_1,\dots,\zeta_m\). Steps 2–5 then run in \(\ell^2(\{1,\dots,m\};H)\), and the resulting \(\tilde\xi\) has \(m\) components. \(\square\)

## Where this leads

- *Kaplansky's density theorem* sharpens Theorem 4.4: the approximating nets can be chosen with the same norm bound as the operator they approximate. The density results proved here give nets with no norm bound.
- *Normal functionals and maps*, and W\*-algebras, are treated in the lesson [The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras](the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md).
- *Comparison of projections and the type decomposition* are treated in [Projections and types of von Neumann algebras](projections-and-types-of-von-neumann-algebras.md). The projection \(z\) of Theorem 5.8(4) is the *central support* of \(e\), which is studied there.
- *Tensor products* of von Neumann algebras and their commutants are treated in Spatial tensor products of von Neumann algebras.

## References

- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
- [van Neerven] J. van Neerven, *Functional Analysis*, [corrected author version, arXiv:2112.11166v7](https://arxiv.org/pdf/2112.11166v7).

*Freely accessible reading:* [Jesse Peterson, *Notes on operator algebras*, §3.5](https://math.vanderbilt.edu/peters10/teaching/spring2015/OperatorAlgebras.pdf) gives a route through the finite-amplification proof of the bicommutant theorem. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.
