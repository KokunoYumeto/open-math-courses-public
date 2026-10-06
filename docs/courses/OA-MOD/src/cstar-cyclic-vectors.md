# A cyclic vector for a bounded positive functional

*GPT-6 Sol (OpenAI), Codex writing thread, Ultra effort, September 2026. New original prose: CC0. This lesson is a draft awaiting course-level mathematical review.*

For an arbitrary weight, the finite-domain GNS space need not have a cyclic vector. A bounded positive functional is different: it is finite on every square. Here we specialize the programme's existing cyclic GNS theorem to that finite-domain construction. An approximate identity indexed by finite subsets makes the specialization explicit without assuming a unit or a countable approximate identity. We use the forced \(C^*\)-unitization, with \(A\) as the kernel of its scalar quotient, and continuous functional calculus. Related classical results appear in Takesaki, *Theory of Operator Algebras I*, Chapter I, §§7 and 9, and the weight context in *Theory of Operator Algebras II*, Chapter VII, §4. Inner products are linear in the first variable.

The cyclicity and approximation statements are theorems of the earlier programme GNS and functional-calculus lessons. The complete local proofs below use the already written forced unitization and inherited cone, UZ06–07, abstract calculus and positive order, AC1–4, finite-domain GNS construction, CS02, and Hilbert completion, Riesz representation and adjoints, BK01. These provide the proof route for this lesson without requiring the reader to recover a theorem from a remote programme page.

The GNS provider is originally by Claude Opus 5.5 (Anthropic), September 2026, with its October 2026 revision and full self-check by GPT-6.1 Sol (OpenAI), Ultra, CC0. The functional-calculus provider has the same original author and October revision credit. The new bridges to earlier programme lessons and solved weight comparisons here are by GPT-6.1 Sol (OpenAI), Ultra, October 2026, CC0; the earlier local prose retains the credit above. The present prerequisite binding, convergence details and arbitrary-index example are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0.

## An approximate identity indexed by finite sets

This finite-set construction applies the existing one-sided ideal estimate twice, once to an element and once to its adjoint. Its proof below keeps the same constant and uses only the declared unitization and functional calculus.

Let \(A\) be a \(C^*\)-algebra, possibly nonunital, and let \(\widetilde A\) be its forced unitization. For a finite set \(F\subset A\) and \(\varepsilon>0\), put

\[
h_F=\sum_{a\in F}(a^*a+aa^*),\qquad
e_{F,\varepsilon}=h_F(h_F+\varepsilon1)^{-1}.
\tag{BG.1}
\]

Functional calculus gives \(0\leq e_{F,\varepsilon}\leq1\). It also places \(e_{F,\varepsilon}\) in \(A\): the quotient map \(\widetilde A\to\mathbb C\) sends \(h_F\) to zero, and functional calculus commutes with that map. The scalar function \(t/(t+\varepsilon)\) vanishes at zero, so the quotient of \(e_{F,\varepsilon}\) is zero.

For \(a\in F\), the inequalities \(a^*a\leq h_F\) and \(aa^*\leq h_F\) give, with \(e=e_{F,\varepsilon}\),

\[
\begin{aligned}
\|a(1-e)\|^2
&=\|(1-e)a^*a(1-e)\|\\
&\leq\|(1-e)h_F(1-e)\|
\leq\varepsilon/4.
\end{aligned}
\tag{BG.2}
\]

The final bound comes from \(\varepsilon^2t/(t+\varepsilon)^2\leq\varepsilon/4\) for \(t\geq0\), equivalently \((t-\varepsilon)^2\geq0\). Applying the same estimate to \(a^*\) yields \(\|(1-e)a\|\leq\sqrt\varepsilon/2\).

Order the pairs by \((F,\varepsilon)\preceq(G,\delta)\) when \(F\subseteq G\) and \(\delta\leq\varepsilon\). This is a directed set. For a fixed \(a\), every sufficiently late \(F\) contains \(a\), while \(\varepsilon\) can be made arbitrarily small. Therefore

\[
e_{F,\varepsilon}a\longrightarrow a,\qquad
ae_{F,\varepsilon}\longrightarrow a
\quad\text{in norm}.
\tag{BG.3}
\]

No monotonicity of the net is required. When \(A=0\), it is the zero net.

## From a positive functional to a representing vector

We construct the representing vector inside the finite-domain Hilbert space already proved in CS02. The argument uses its first-linear convention and null quotient, and proves cyclicity in the next section.

Let \(\omega\in A^*_+\) be bounded and positive. The estimate
\(\omega(a^*a)\leq\|\omega\|\|a\|^2\)
makes every \(a\in A\) a finite GNS vector. The finite-domain quotient supplies \(H_\omega\), a dense map \(\Lambda_\omega:A\to H_\omega\), and a contractive *-representation \(\pi_\omega\), with

\[
\langle\Lambda_\omega(a),\Lambda_\omega(b)\rangle=\omega(b^*a),
\qquad
\pi_\omega(c)\Lambda_\omega(a)=\Lambda_\omega(ca).
\tag{BG.4}
\]

This includes the null quotient when \(\omega\) is not faithful.

Write \(e_i\) for the net above. Cauchy–Schwarz and \(0\leq e_i^2\leq1\) in the unitization imply

\[
|\omega(e_i a)|^2
\leq\omega(e_i^2)\omega(a^*a)
\leq\|\omega\|\omega(a^*a).
\]

Here \(e_i^2\) belongs to the original algebra and has norm at most one. Thus \(\omega(e_i^2)\leq\|\omega\|\|e_i^2\|\leq\|\omega\|\) follows from the norm of the bounded functional; no value of \(\omega\) at the adjoined unit is assumed.

As \(e_i a\to a\) in norm, boundedness of \(\omega\) gives

\[
|\omega(a)|^2\leq\|\omega\|\omega(a^*a).
\tag{BG.5}
\]

Thus \(\Lambda_\omega(a)\mapsto\omega(a)\) is a well-defined bounded linear functional on the dense GNS range, with norm at most \(\|\omega\|^{1/2}\). The Hilbert-space Riesz theorem gives a unique vector \(\xi_\omega\) such that

\[
\omega(a)=\langle\Lambda_\omega(a),\xi_\omega\rangle,\qquad
\|\xi_\omega\|\leq\|\omega\|^{1/2}.
\tag{BG.6}
\]

## Cyclicity, normalization and nondegeneracy

These are the conclusions of programme Theorems 5.3–5.4. We verify them for the particular quotient and approximate identity used in this weight route.

For \(a,b\in A\), the adjoint identity for \(\pi_\omega\), the formula above, and positivity of \(\omega\) give

\[
\begin{aligned}
\langle\pi_\omega(b)\xi_\omega,\Lambda_\omega(a)\rangle
&=\langle\xi_\omega,\Lambda_\omega(b^*a)\rangle\\
&=\overline{\omega(b^*a)}
=\omega(a^*b)
=\langle\Lambda_\omega(b),\Lambda_\omega(a)\rangle .
\end{aligned}
\tag{BG.7}
\]

Density of the GNS range proves

\[
\pi_\omega(b)\xi_\omega=\Lambda_\omega(b),\qquad
\omega(b)=\langle\pi_\omega(b)\xi_\omega,\xi_\omega\rangle .
\tag{BG.8}
\]

Hence \(\overline{\pi_\omega(A)\xi_\omega}=H_\omega\). The coefficient formula gives \(\|\omega\|\leq\|\xi_\omega\|^2\); together with (BG.6) this becomes

\[
\|\xi_\omega\|^2=\|\omega\|.
\tag{BG.9}
\]

No value at a unit was used.

The representation is nondegenerate. For \(a\in A\),

\[
\|\pi_\omega(e_i)\Lambda_\omega(a)-\Lambda_\omega(a)\|^2
\leq\|\omega\|\,\|e_i a-a\|^2\longrightarrow0.
\]

Since the \(\pi_\omega(e_i)\) are contractions, density extends the convergence to all of \(H_\omega\). Explicitly, for \(\eta\in H_\omega\) choose \(v=\Lambda_\omega(a)\) close to \(\eta\). Then

\[
 \begin{aligned}
 \|\pi_\omega(e_i)\eta-\eta\|
 &\leq 2\|\eta-v\|\\
 &\quad+\|\pi_\omega(e_i)v-v\|.
 \end{aligned}
\]

First make the first term small by density, then the second by the displayed convergence. Each \(\pi_\omega(e_i)\eta\) belongs to \(\pi_\omega(A)H_\omega\); their limits therefore prove nondegeneracy. In particular \(\Lambda_\omega(e_i)=\pi_\omega(e_i)\xi_\omega\to\xi_\omega\). For \(\omega=0\), both the Hilbert space and this vector are zero, and every formula remains valid.

This cyclic-vector argument uses boundedness in (BG.5). It does not give a cyclic vector for a general unbounded weight.

**A nonfaithful functional with a faithful representation.** This specializes [programme Examples 5.7(3)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#oa-fnd-gn-05) to distinguish the faithfulness assertions needed for weights. On \(A=M_2(\mathbb C)\), set \(\omega(a)=a_{11}\). Then

\[
 \begin{gathered}
 \omega(a^*a)=\|ae_1\|^2,\\
 \Lambda_\omega(a)\longmapsto ae_1.
 \end{gathered}
 \tag{BG.10}
\]

The null left ideal consists exactly of matrices whose first column is zero. The displayed map is an isometry onto \(\mathbb C^2\), since any first column is possible. Left multiplication becomes the usual matrix representation, which is faithful: a matrix annihilating every vector is zero. The canonical vector is \(e_1\), and its matrix orbit is all of \(\mathbb C^2\). Nevertheless the functional is not faithful, since the nonzero positive projection \(E_{22}\) has value zero. Thus the null quotient, the faithfulness of the functional, and the faithfulness of the representation are distinct assertions. The zero functional instead gives the zero Hilbert space and the zero representation.

**An unbounded faithful weight with no cyclic vector.** Let \(I\) be uncountable and \(A=c_0(I)\). Define the counting weight by

\[
 \begin{gathered}
 \tau(a)=\sum_{i\in I}a_i\quad(a\in A_+),\\
 \mathfrak n_\tau=\ell^2(I).
 \end{gathered}
 \tag{BG.11}
\]

We spell out the spaces in this example. The algebra \(c_0(I)\) consists of scalar families \(a\) for which \(\{i:|a_i|\geq\varepsilon\}\) is finite for every \(\varepsilon>0\). Such a family is bounded. Sums, products and conjugation preserve this property: use the union of the two half-threshold sets for a sum, and boundedness of one factor for a product. The supremum norm is submultiplicative and satisfies \(\|a^*a\|=\|a\|^2\). A uniformly Cauchy sequence has a uniform coordinatewise limit; a half-threshold estimate puts that limit in \(c_0(I)\). Thus this is a C*-algebra. Its positive cone is exactly the pointwise nonnegative families, because coordinatewise square roots remain in \(c_0(I)\).

Define \(\ell^2(I)\) by finiteness of \(\sup_{F\subset I,\ F\text{ finite}}\sum_{i\in F}|x_i|^2\), and let its square root be \(\|x\|_2\). Finite-sum Cauchy–Schwarz gives the triangle inequality and the pairing \(\langle x,y\rangle=\sum_i x_i\overline{y_i}\). These sums converge as nets over finite subsets: choose a finite subset capturing all but an arbitrarily small part of each square sum, then apply Cauchy–Schwarz to the remaining finite sums. If \((x^{(n)})\) is Cauchy in this norm, every coordinate converges to some \(x_i\). For a fixed late \(n\), pass to the limit in each finite sum of \(|x_i^{(n)}-x_i^{(m)}|^2\). The Cauchy bound survives uniformly over finite subsets, so \(x^{(n)}-x\) has arbitrarily small square norm. In particular \(x\in\ell^2(I)\), proving completeness. Finite-support truncations are dense by the definition of the supremum. This proves the Hilbert-space realization used below for arbitrary \(I\).

The sum defining \(\tau\) is the supremum of finite partial sums. Additivity follows in both directions: every partial sum of \(a+b\) is bounded by \(\tau(a)+\tau(b)\), while the union of finite sets for \(a\) and \(b\) bounds their two partial sums by a partial sum of \(a+b\). Taking suprema proves equality, also when a value is infinite. Nonnegative homogeneity is immediate, with \(0\cdot\infty=0\). Thus \(\tau\) is a weight. It is faithful and lower semicontinuous, being that supremum of continuous positive functionals; finite-support positive truncations make it semifinite. Indeed, these truncations lie below the original positive element, have finite weight, and their weights have supremum equal to its weight. A positive element of weight zero has every coordinate zero, proving faithfulness. Finite coordinate projections have norm one and arbitrarily large weight, so the weight is unbounded. Every square-summable family vanishes at infinity, so its finite left ideal is indeed the stated subspace of \(A\). The GNS space is the actual \(\ell^2(I)\), with \(\Lambda_\tau\) the inclusion and \(\pi_\tau\) diagonal multiplication. This representation is faithful, because its action on each coordinate vector detects that coordinate. It is nondegenerate: finite coordinate projections converge on every square-summable vector by convergence of the finite partial norm sums.

For every \(\xi\in\ell^2(I)\), its support is countable. Indeed, for each positive integer \(n\), only finitely many coordinates can have modulus at least \(1/n\); their union contains every nonzero coordinate. Diagonal multiplication cannot enlarge that support. Hence

\[
 \begin{gathered}
 \overline{\pi_\tau(A)\xi}
 \subseteq\ell^2(\operatorname{supp}\xi)\\
 \ne\ell^2(I).
 \end{gathered}
 \tag{BG.12}
\]

There is no cyclic vector. Nor could a single vector represent the counting weight: testing all coordinate projections would require every coordinate modulus to be one. This example supplies the exact finite-domain boundary of the bounded-functional theorem, without a countability assumption or a claim that every unbounded weight fails to have a cyclic GNS representation.

## References

- Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979, Chapter I: Lemma 7.2, Theorem 7.4 and Corollary 7.5 (printed pp. 26–28); Lemma 9.11 and Theorem 9.14 (printed pp. 39–41). The finite-set estimate, norm-one approximate identity and weight examples are proved above; the citation does not replace an internal proof.
- Takesaki, *Theory of Operator Algebras II*, Springer, 2003, Chapter VII, §4. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10451-4).
