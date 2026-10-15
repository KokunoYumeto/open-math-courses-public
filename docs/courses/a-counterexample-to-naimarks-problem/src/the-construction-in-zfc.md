# The construction in ZFC

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the construction of a counterexample to Naimark's problem. A bridge iteration of length \(\mathfrak c^+\), the successor cardinal of the continuum, joins the class of every pure state that ever appears to one fixed class. A fixed schedule, chosen before any algebra is built, guarantees that every pure state of every stage is treated at some later stage; countable determination, from [Closed subiterations and countable determination](closed-subiterations-and-countable-determination.md), guarantees that every pure state of the final algebra already appears at some stage. The peaking sequences needed at each step come from a homogeneity theorem of Kishimoto, Ozawa and Sakai, which this course uses without proof. The lesson follows [OpenAI-NA, Section 6].

- Cardinals and the schedule (Section 1).
- The homogeneity theorem (Section 2).
- The construction (Section 3).
- The theorem (Section 4).

## 1. Cardinals and the schedule

We use the facts on ordinals of Theorem 0.1 of [Numerical ranges, positive matrices and co-Souslin sets](course:foundations-of-von-neumann-algebras/numerical-ranges-positive-matrices-and-co-souslin-sets), and the cardinal arithmetic of Section 8 of [Hahn–Banach, Baire and the basic theorems on Banach spaces](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces). Write \(|X|\le|Y|\) if there is an injection \(X\to Y\). Let \(\mathfrak c=2^{\aleph_0}\), the cardinality of the set \(\{0,1\}^{\mathbb N}\), which we also denote by \(\mathfrak c\).

**Lemma 1.1.** There is an ordinal \(\kappa\) with \(|\kappa|\not\le\mathfrak c\) such that \(|\beta|\le\mathfrak c\) for every \(\beta<\kappa\). It has the following properties.

1. \(|\mathfrak c|\le|\kappa|\), and \(|\kappa\times\kappa|=|\kappa|\).
2. For \(\beta<\kappa\), the set \([\beta,\kappa)=\{\gamma:\beta\le\gamma<\kappa\}\) satisfies \(|[\beta,\kappa)|\not\le\mathfrak c\).
3. Every countable subset of \(\kappa\) is bounded: it is contained in some \(\beta<\kappa\).

We write \(\kappa=\mathfrak c^+\).

*Proof.* The well-orderings of subsets of \(\mathfrak c\) form a set, and by Theorem 0.1 of the numerical-ranges lesson each is isomorphic to exactly one ordinal; by Replacement these ordinals form a set \(\kappa\). It contains every ordinal below each of its members, since an initial segment of a well-ordering of a subset of \(\mathfrak c\) is again one. A set of ordinals with this property is an ordinal (Theorem 0.1 there). If \(|\kappa|\le\mathfrak c\), an injection would carry the order of \(\kappa\) to a well-ordering of a subset of \(\mathfrak c\), so \(\kappa\in\kappa\), which is impossible. Every \(\beta<\kappa\) is the type of a well-ordering of a subset of \(\mathfrak c\), so \(|\beta|\le\mathfrak c\).

(1) By Theorem 8.5 of the Hahn–Banach lesson, \(\mathfrak c\) has a well-ordering, of some type \(\alpha\); then \(\alpha\in\kappa\) and \(\alpha\subseteq\kappa\), so \(|\mathfrak c|\le|\kappa|\). As \(\kappa\) is infinite, \(|\kappa\times\kappa|=|\kappa|\) by Theorem 8.5 there.

(2) Otherwise \(\kappa=\beta\cup[\beta,\kappa)\) injects into \(\mathfrak c\times\{0,1\}\), and \(|\mathfrak c\times\{0,1\}|\le|\mathfrak c\times\mathbb N|=\mathfrak c\) by Theorem 8.4 there.

(3) Let \(S\subseteq\kappa\) be countable. If \(S\) were contained in no \(\beta<\kappa\), every \(\gamma<\kappa\) would lie in some \(s\in S\), so \(\kappa=\bigcup_{s\in S}s\). Choosing injections \(s\to\mathfrak c\) gives \(|\kappa|\le|S\times\mathfrak c|\le|\mathbb N\times\mathfrak c|=\mathfrak c\), a contradiction. \(\square\)

**Lemma 1.2** (the schedule). There is an injection \(\sigma\colon\kappa\times\kappa\to\kappa\) with \(\sigma(\beta,\eta)\ge\beta\) for all \(\beta,\eta\).

*Proof.* By Lemma 1.1(1), there is a bijection \(\xi\mapsto(\beta_\xi,\eta_\xi)\) from \(\kappa\) onto \(\kappa\times\kappa\). Define \(\sigma(\beta_\xi,\eta_\xi)\) by recursion on \(\xi<\kappa\) as the least ordinal \(\gamma\ge\beta_\xi\) that is not among the values \(\sigma(\beta_\zeta,\eta_\zeta)\), \(\zeta<\xi\). Such \(\gamma\) exists: the values already used form a set \(U\) with \(|U|\le|\xi|\le\mathfrak c\), while \(|[\beta_\xi,\kappa)|\not\le\mathfrak c\) by Lemma 1.1(2). The map is injective because each value is new. \(\square\)

Here and below, definitions by recursion on ordinals are transfinite recursions: a rule that determines the value at \(\xi\) from the values at all \(\zeta<\xi\) has exactly one solution on \(\kappa\). This is proved as the construction of order types in the proof of Theorem 0.1 of the numerical-ranges lesson: two partial solutions agree on their common domain, and by Replacement their union is a solution.

## 2. The homogeneity theorem

The peaking sequence that joins a given pure state to the fixed class is obtained by moving a fixed peaking sequence with an automorphism. The required automorphism comes from the following theorem, which is used without proof.

**(KOS)** [Kishimoto–Ozawa–Sakai 2003, Theorem 1.1]. *Let \(B\) be a separable C\(^*\)-algebra. If pure states \(h,k\) of \(B\) have GNS representations with the same kernel, there is an automorphism \(\gamma\) of \(B\) with \(h\circ\gamma=k\).*

The theorem provides an asymptotically inner automorphism. For a simple \(B\), the kernel of every irreducible representation is \(\{0\}\), so any two pure states are related by an automorphism. The proof of (KOS) combines a path-lifting argument of Futamura, Kataoka and Kishimoto with a theorem of Haagerup on invariant means for injective von Neumann algebras; these tools are not developed in this programme.

## 3. The construction

Fix \(\kappa=\mathfrak c^+\) and the schedule \(\sigma\) of Lemma 1.2. Let \(A_0\), \((p_n)\) and \(f_0\) be as in Section 2 of the closed-subiteration lesson. We construct a bridge iteration \((X_\beta)_{\beta\le\kappa}\) in the sense of Section 3 there, by recursion on \(\beta\), together with lists of pure states.

*Lists.* Once \(X_\beta\) is constructed, \(\beta<\kappa\), choose a family \((h_{\beta,\eta})_{\eta<\kappa}\) that contains every pure state of \(X_\beta\), repetitions allowed. This is possible: \(|\beta|\le\mathfrak c\), so \(X_\beta\) has at most \(\mathfrak c\) pure states (Corollary 5.2 of the closed-subiteration lesson), at least one exists, and \(|\mathfrak c|\le|\kappa|\).

*Step \(j\).* Let \(j<\kappa\), with \(X_j\) and the lists \((h_{\beta,\eta})\), \(\beta\le j\), constructed. Let \(f\) be the state of \(X_j\) peaked by \((p_n)\), the unique extension of \(f_0\). If \(j\) is not a value of \(\sigma\), the step is inactive. Otherwise \(j=\sigma(\beta,\eta)\) with \(\beta\le j\), and the list for \(\beta\) is available. Let \(g\) be the unique extension of \(h_{\beta,\eta}\) to \(X_j\) (Lemma 1.1 of the closed-subiteration lesson). If \(g\sim f\), the step is inactive.

Suppose \(g\not\sim f\). By Lemma 5.1 of the closed-subiteration lesson there is a countable dependency-closed \(S\subseteq j\) such that \(g|_{A[S]}\) is pure and \(g\) is its only extension to \(X_j\). The restriction \(f|_{A[S]}\) is pure, since \((p_n)\) peaks in \(X_j\) (Lemma 2.5 of [Pure states, excision and peaking projections](pure-states-excision-and-peaking-projections.md)). By Lemma 3.1 of the closed-subiteration lesson, \(A[S]\) is separable, simple and unital. By (KOS) there is an automorphism \(\gamma\) of \(A[S]\) with
\[
(g|_{A[S]})\circ\gamma=f|_{A[S]} .
\]
Put \(q^j_n=\gamma(p_n)\), a decreasing sequence of projections with \(q^j_0=1\).

- *Peaking.* If a state \(k\) of \(A[S]\) takes the value one on every \(q^j_n\), then \(k\circ\gamma\) takes the value one on every \(p_n\), so \(k\circ\gamma=f|_{A[S]}=(g|_{A[S]})\circ\gamma\) and \(k=g|_{A[S]}\). So \((q^j_n)\) peaks to \(g|_{A[S]}\) in \(A[S]\). A state of \(X_j\) taking the value one on every \(q^j_n\) restricts to \(g|_{A[S]}\), hence is the only extension \(g\): the sequence peaks to \(g\) in \(X_j\).
- *Traces.* For each \(n\), \(\gamma\) carries the unital matrix subalgebra \(M_{2^n}(\mathbb C)\subseteq A_0\) onto a unital subalgebra of \(A[S]\) isomorphic to \(M_{2^n}(\mathbb C)\), and \(p_n\), a projection of rank one there, to \(q^j_n\). The trace \(\tau\) restricts to a tracial state of this matrix algebra, which is its normalized trace. Hence \(\tau(q^j_n)=2^{-n}\).

So the hypotheses of an active step hold, with the dependency set \(I_j=S\), and \(X_{j+1}\) is the bridge over \(X_j\) for \((p_n)\) and \((q^j_n)\). At a limit \(\gamma\le\kappa\), \(X_\gamma\) is the completion of \(\bigcup_{\beta<\gamma}X_\beta\).

*Choices.* The recursion makes choices at every stage: a list, a set \(S\), an automorphism, and an algebra realizing the bridge. Each stage is generated by \(A_0\) and at most \(|\kappa|\) unitaries, so it has a dense subset of cardinality at most \(|\kappa|\), and cardinality at most \(\lambda=|\kappa|^{\aleph_0}\), since every element is a limit of a sequence from the dense subset. Fix a set \(\Lambda\) with \(|\Lambda|=\lambda\). Every stage, with its embeddings, norm, trace, states, automorphisms and lists, can be realized on subsets of \(\Lambda\); these structures form a set, and a well-ordering of it (Theorem 8.5 of the Hahn–Banach lesson) lets every choice be the least admissible one. The recursion therefore takes place in ZFC.

## 4. The theorem

**Theorem 4.1** ([OpenAI-NA, Theorem 1.1]). Assume (KOS). There is a unital, infinite-dimensional, simple C\(^*\)-algebra \(A\) with a faithful tracial state, all of whose nonzero irreducible representations are unitarily equivalent. In particular, \(A\) is not isomorphic to \(K(H)\) for any Hilbert space \(H\).

*Proof.* Let \(A=X_\kappa\). By Lemma 3.1 of the closed-subiteration lesson, \(A\) is simple and has a faithful tracial state; it contains the infinite-dimensional algebra \(A_0\).

*Every pure state is joined to the fixed class.* Let \(h\) be a pure state of \(A\), and let \(f_A\) be the state of \(A\) peaked by \((p_n)\). By Lemma 5.1 of the closed-subiteration lesson there is a countable dependency-closed \(S\subseteq\kappa\) such that \(h|_{A[S]}\) is pure and \(h\) is its only extension to \(A\). By Lemma 1.1(3), \(S\subseteq\beta\) for some \(\beta<\kappa\), so \(A[S]\subseteq X_\beta\). The restriction \(h|_{X_\beta}\) is the only extension of \(h|_{A[S]}\) to \(X_\beta\), since any other would extend further to \(A\); so it is pure (Lemma 2.1 of the first lesson). Choose \(\eta\) with \(h_{\beta,\eta}=h|_{X_\beta}\), and put \(j=\sigma(\beta,\eta)\ge\beta\). The unique extension of \(h_{\beta,\eta}\) to \(X_j\) is \(h|_{X_j}\). At step \(j\), either \(h|_{X_j}\) is equivalent to the state peaked by \((p_n)\), or the bridge makes the unique extensions of the two states to \(X_{j+1}\) equivalent. By Lemma 1.1 of the closed-subiteration lesson, the unique extensions to \(A\) are equivalent; they are \(h\) and \(f_A\). So every pure state of \(A\) is equivalent to \(f_A\).

*Irreducible representations.* A nonzero irreducible representation \(\pi\) of \(A\) is unital, and the vector state of any unit vector is a pure state whose GNS representation is equivalent to \(\pi\) (Lemma 1.1 of the first lesson). That state is equivalent to \(f_A\), so \(\pi\cong\pi_{f_A}\). Hence \(A\) has exactly one nonzero irreducible representation up to unitary equivalence.

*Not \(K(H)\).* If \(H\) is infinite-dimensional, the identity of \(H\) is not compact, since an orthonormal sequence has no norm-convergent subsequence; so \(K(H)\) is not unital. If \(H\) is finite-dimensional, \(K(H)\) is finite-dimensional. In neither case is \(K(H)\cong A\). \(\square\)

**What the proof assumed.** The proof used one published theorem without proof: the homogeneity theorem (KOS) of Kishimoto, Ozawa and Sakai, at every active step. Everything else is proved in this course or in the programme lessons cited along the way: excision and cross-excision of pure states, the expectations from peaking projections, reduced amalgamated free products and reduced HNN adjunctions, the bridge, closed subiterations and countable determination, and the cardinal arithmetic of the schedule.

The construction has length \(\mathfrak c^+\); this is not claimed to be the density of \(A\).

## 5. Exercises

**5.1.** Show that \(\kappa=\mathfrak c^+\) is uncountable, and that \(\omega_1\le\kappa\), where \(\omega_1\) is the least uncountable ordinal.

**5.2.** Show that the identity operator of an infinite-dimensional Hilbert space is not compact.

**5.3.** Let \(B\) be a unital C\(^*\)-algebra all of whose pure states are equivalent. Show that every pure state of \(B\) is the vector state of a unit vector in one fixed irreducible representation.

**5.4.** In Step \(j\), show that \(\gamma\) maps the matrix units of \(M_{2^n}(\mathbb C)\subseteq A_0\) to a system of matrix units of \(A[S]\) summing to \(1\), and deduce \(\tau(q^j_n)=2^{-n}\) directly from the trace property.

**5.5.** Why does the construction need every countable subset of \(\kappa\) to be bounded? Point to the place in the proof where Lemma 1.1(3) is used.

## 6. Solutions

**5.1.** \(\mathbb N\) and every countable ordinal inject into \(\mathfrak c\), so they lie below \(\kappa\) by the construction of \(\kappa\); in particular \(\omega_1\le\kappa\). If \(\kappa\) were countable it would inject into \(\mathfrak c\), against Lemma 1.1.

**5.2.** Let \((e_n)\) be an orthonormal sequence. Then \(\|e_n-e_m\|=\sqrt2\) for \(n\ne m\), so the bounded sequence \((1e_n)\) has no convergent subsequence, and the identity is not compact.

**5.3.** Fix a pure state \(f\) and let \(\pi=\pi_f\). Every pure state \(h\) is equivalent to \(f\), so by Lemma 1.1(2) of the first lesson it is a vector state of \(\pi\).

**5.4.** \(\gamma\) is a unital \(*\)-isomorphism of \(A[S]\), so it preserves the relations \(e_{ab}e_{cd}=\delta_{bc}e_{ad}\), \(e_{ab}^*=e_{ba}\) and \(\sum_ae_{aa}=1\). With \(f_{ab}=\gamma(e_{ab})\), the trace property gives \(\tau(f_{aa})=\tau(f_{ab}f_{ba})=\tau(f_{ba}f_{ab})=\tau(f_{bb})\), so all \(2^n\) diagonal units have equal trace, with sum \(1\), hence trace \(2^{-n}\); one of them is \(q^j_n=\gamma(p_n)\).

**5.5.** In the proof of Theorem 4.1, a pure state \(h\) of \(A\) is determined by its restriction to \(A[S]\) with \(S\) countable. Lemma 1.1(3) places \(S\) below some \(\beta<\kappa\), so \(h|_{X_\beta}\) appears in a list at stage \(\beta\), and the schedule treats it at a later stage \(j\). Without boundedness the restriction would not appear at any stage.

## References

- [OpenAI-NA] OpenAI, *A counterexample to Naimark's problem in ZFC*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 6. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026
- [Kishimoto–Ozawa–Sakai 2003] A. Kishimoto, N. Ozawa, S. Sakai, *Homogeneity of the pure state space of a separable C\(^*\)-algebra*, Canad. Math. Bull. 46 (2003), 365–372. https://arxiv.org/abs/math/0110152
