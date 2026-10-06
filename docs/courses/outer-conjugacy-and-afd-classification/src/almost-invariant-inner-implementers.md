# Almost invariant inner implementers

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Mathematical and source review by GPT-6 Astra (OpenAI), Ultra, October 2026, under the stated prerequisites. New original text is public domain (CC0).*

## Introduction

Approximate innerness supplies unitaries whose conjugations approach an automorphism. Those unitaries need not be approximately fixed by that same automorphism. An outer-conjugacy construction needs both properties at once.

The difference is measured by a central unitary sequence. The first cohomology theorem removes this difference, producing implementers that are almost invariant under every fixed integer power. This prepares the later comparison of approximately inner actions.

The defect-and-correction argument is [Connes, Lemma 3.1.1]; see also [Takesaki III, Lemma XVII.3.2]. We give the moving-multiplier estimates and ordinary subsequence selection explicitly. The cohomology input is [Central towers and unitary cocycles](central-towers-and-unitary-cocycles.md), Theorem 5.1, with its full cyclic-tower prerequisites. For the quotient and exact unitary lifts we use Central sequence algebras and exact lifts, Theorem 3.1 and Theorem 5.1 with both coordinate endpoints equal to 1. Their functional-calculus, projection and bounded strong-star topology foundations retain their stated scope. [Ando–Haagerup] supplies modern quotient context; [Connes periodic] is background for the subsequent periodic classification.

The faithful normal state and bounded strong-star tests are constructed and proved in [Bounded topology and tracial representations, Section 3A](bounded-topology-and-tracial-representations.md#3a-faithful-state-tests-and-ordinary-extraction). That section also proves the uniform finite-test and ultrafilter subsequence statements used below, with its exact earlier foundations supplied in the accompanying [proof companion](../foundations/bounded-topology-foundations.md).

Throughout, \(M\) is a factor with separable predual. A bounded sequence \((x_n)\) is strongly central when \(\|[x_n,\psi]\|\to0\) for every \(\psi\in M_*\). An automorphism is centrally trivial when it fixes every such sequence modulo strong-star null sequences. We write \(p_a(\theta)=0\) when no nonzero integer power of \(\theta\) is centrally trivial. Theorem 3.1 below needs no strong-stability hypothesis: the stated cohomology theorem applies to every separable-predual factor.

## 1. The topology that controls moving multipliers

The **\(u\)-topology** on \(\operatorname{Aut}M\) is pointwise norm convergence on the predual:
\[
\begin{gathered}
\alpha_n\longrightarrow\alpha
\\\Longleftrightarrow\quad
\|\psi\circ\alpha_n-\psi\circ\alpha\|\longrightarrow0
\\(\psi\in M_*).
\end{gathered}
\tag{1.1}
\]
An automorphism is approximately inner if it belongs to the closure of the inner automorphisms for this topology. To obtain a sequence, choose a norm-dense sequence \((\psi_j)\) in the unit ball of \(M_*\), and choose an inner automorphism meeting the first \(n\) tests within \(1/n\). Precomposition by an automorphism is an isometry, so
\[
\begin{aligned}
\|\psi\circ\alpha_n-\psi\circ\alpha\|
&\leq 2\|\psi-\psi_j\|\\
&\quad+\|\psi_j\circ\alpha_n-\psi_j\circ\alpha\|.
\end{aligned}
\]
Density and scaling therefore give convergence for every normal functional.

The same isometry proves the group continuity needed below. If \(\alpha_n\to\alpha\) and \(\beta_n\to\beta\), then
\[
\begin{aligned}
&\|\psi\circ\alpha_n\circ\beta_n-\psi\circ\alpha\circ\beta\|\\
&\quad\leq\|\psi\circ\alpha_n-\psi\circ\alpha\|\\
&\qquad+\|(\psi\circ\alpha)\circ\beta_n-(\psi\circ\alpha)\circ\beta\|,
\end{aligned}
\]
and
\[
\begin{aligned}
&\|\psi\circ\alpha_n^{-1}-\psi\circ\alpha^{-1}\|\\
&\qquad=\|\psi-(\psi\circ\alpha^{-1})\circ\alpha_n\|\longrightarrow0.
\end{aligned}
\]
Thus composition, inversion and every fixed integer power preserve convergence. All later subsequence selections use only countably many predual tests and a faithful normal state; no separability of the asymptotic centralizer is required.

**Lemma 1.1 (transporting null sequences).** Suppose \(a_n\) is bounded and tends to zero strongly-star, and \(\operatorname{Ad}u_n\to\theta\) in the \(u\)-topology. For every fixed integer \(j\), the sequences \(a_nu_n^j\), \(u_n^ja_n\), and their adjoints tend strongly to zero.

*Proof.* Composition and inversion are continuous in the automorphism group, so \(\operatorname{Ad}(u_n^j)\to\theta^j\). If \(\psi\) is positive and normal,
\[
\|a_nu_n^j\|_\psi^2
=(\psi\circ\operatorname{Ad}(u_n^{-j}))(a_n^*a_n).
\]
Replacing the moving functional by \(\psi\circ\theta^{-j}\) changes this by at most
\[
\|\psi\circ\operatorname{Ad}(u_n^{-j})-\psi\circ\theta^{-j}\|\,
\|a_n\|^2,
\]
which tends to zero. Its value on \(a_n^*a_n\) also tends to zero. Left multiplication by a unitary preserves \(\|\cdot\|_\psi\). Apply the same arguments to \(a_n^*\) to get all the adjoint seminorms. \(\square\)

This lemma is why strong-star convergence alone is not the whole argument. Multiplication on the right by a varying bounded sequence need not preserve strong convergence. The convergent automorphisms supply the needed predual control.

## 2. The defect is central

**Lemma 2.1.** If \(\operatorname{Ad}v_n\to\theta\), then
\[
w_n=v_n^*\theta(v_n)
\tag{2.1}
\]
is a strongly central sequence of unitaries.

*Proof.* Conjugating the convergence by \(\theta\) gives
\[
\operatorname{Ad}\theta(v_n)
=\theta\circ\operatorname{Ad}v_n\circ\theta^{-1}
\longrightarrow\theta.
\]
Thus \(\operatorname{Ad}w_n=(\operatorname{Ad}v_n)^{-1}\circ\operatorname{Ad}\theta(v_n)\to\mathrm{id}\). For a unitary \(w\), put \(f=\psi\circ\operatorname{Ad}w-\psi\). The bimodule convention gives, for every \(a\in M\),
\[
\begin{aligned}
(w\psi-\psi w)(a)&=\psi(aw)-\psi(wa)\\
&=-f(aw).
\end{aligned}
\]
Right multiplication by \(w\) maps the unit ball of \(M\) onto itself, so \(\|w\psi-\psi w\|=\|f\|\). Applying this to \(w_n\) gives \(\|[w_n,\psi]\|\to0\) for every \(\psi\in M_*\). \(\square\)

Notice that \(w_n\) is central although \(v_n\) generally is not. A central correction can change the defect without changing the limiting automorphism.

## 3. Correcting the implementers

**Theorem 3.1.** Suppose \(\theta\) is approximately inner and \(p_a(\theta)=0\). There are unitaries \(u_n\in M\) such that
\[
\operatorname{Ad}u_n\longrightarrow\theta,
\tag{3.1}
\]
and, for every fixed integer \(k\),
\[
\theta(u_n^k)-u_n^k\longrightarrow0
\quad\text{strongly-star}.
\tag{3.2}
\]

*Proof.* Fix a free ultrafilter \(\omega\) on \(\mathbb N\), and start with unitaries \(v_n\) implementing approximate innerness. By Lemma 2.1, \(W=[(w_n)]\) is a unitary in \(M_\omega\), where \(w_n\) is given by (2.1). Write \(\gamma=\theta_\omega\).

Theorem 5.1 of the central-tower lesson applies because \(p_a(\theta)=0\). Applied to \(W^*\), it gives a unitary \(V\) with \(\gamma(V)=W^*V\). Set \(X=V^*\). Then
\[
\gamma(X)=XW,\qquad W=X^*\gamma(X).
\tag{3.3}
\]
Lift \(X\) to a strongly \(\omega\)-central unitary sequence \(x_n\), using the exact-lift theorem with initial and final coordinate projections both equal to \(1\). At the same coordinate \(n\), set
\[
u'_n=v_nx_n^*.
\]
Its defect is
\[
\begin{aligned}
(u'_n)^*\theta(u'_n)
&=x_n v_n^*\theta(v_n)\theta(x_n^*)\\
&=x_nw_n\theta(x_n^*).
\end{aligned}
\tag{3.4}
\]
The class of (3.4) is \(XW\gamma(X^*)=1\). It is therefore strongly-star close to \(1\) along \(\omega\). Also \(\operatorname{Ad}x_n\to\mathrm{id}\) along \(\omega\), so \(\operatorname{Ad}u'_n\to\theta\) along \(\omega\).

Here is the ordinary subsequence selection. Fix a faithful normal state \(\varphi\), put
\[
\begin{gathered}
\|a\|_\varphi^\sharp
=\bigl(\varphi(a^*a)+\varphi(aa^*)\bigr)^{1/2},\\
b'_n=(u'_n)^*\theta(u'_n)-1,
\end{gathered}
\]
and keep the dense normal-functional tests \((\psi_j)\) from Section 1. Set \(n_0=0\). For each \(r\), the indices satisfying
\[
\begin{gathered}
\|\psi_j\circ\operatorname{Ad}u'_n-\psi_j\circ\theta\|<1/r
\quad(j\leq r),\\
\|b'_n\|_\varphi^\sharp<1/r
\end{gathered}
\]
form a set in \(\omega\). Intersecting with \(\{n>n_{r-1}\}\), choose one index \(n_r\). Define
\[
u_r=u'_{n_r}=v_{n_r}x_{n_r}^*.
\]
Both factors retain that same chosen coordinate. The predual density estimate in Section 1 gives \(\operatorname{Ad}u_r\to\theta\) ordinarily. Since \(b'_{n_r}\) is uniformly bounded, the faithful-state criterion for bounded strong-star convergence gives \(b'_{n_r}\to0\) strongly-star. Relabel the output index as \(n\), and put \(b_n=u_n^*\theta(u_n)-1\). We have obtained both ordinary limits without resampling either factor separately.

Since \(\theta(u_n)-u_n=u_nb_n\), Lemma 1.1 proves strong-star convergence for \(k=1\). For a positive integer \(k\), use
\[
\begin{aligned}
&\theta(u_n)^k-u_n^k\\
&\quad=\sum_{j=0}^{k-1}\theta(u_n)^j
\bigl(\theta(u_n)-u_n\bigr)u_n^{k-1-j}.
\end{aligned}
\tag{3.5}
\]
The two families of inner automorphisms implemented by \(u_n\) and \(\theta(u_n)\) both tend to \(\theta\), since
\[
\operatorname{Ad}\theta(u_n)
=\theta\circ\operatorname{Ad}u_n\circ\theta^{-1}\longrightarrow\theta.
\]
For each summand first apply Lemma 1.1 to the right factor \(u_n^{k-1-j}\) and the strongly-star-null sequence \(\theta(u_n)-u_n\). Apply it again to the resulting null sequence and the left factor \(\theta(u_n)^j\). Every summand is strongly-star null, and their finite sum stays null. If \(k=-m<0\), its difference is exactly \((\theta(u_n^m)-u_n^m)^*\), so the positive-power result gives the conclusion. The case \(k=0\) is immediate. \(\square\)

The statement is for each fixed \(k\). It gives no bound uniform over all integers. The telescope (3.5) has \(k\) terms, so allowing \(k\) to grow with \(n\) needs further estimates.

## 4. Consequences for finite tests

**Corollary 4.1.** Fix finitely many normal functionals, finitely many integers, and finitely many strong-star seminorms. The implementer in Theorem 3.1 can satisfy the prescribed approximate-innerness and power-invariance tests simultaneously to any positive tolerance.

*Proof.* Each test converges to zero by Theorem 3.1 and the definition of the \(u\)-topology. A finite intersection of eventual tails is an eventual tail. Choose any index in that tail. \(\square\)

This is the form used in an iterative outer-conjugacy argument. At one stage only finitely many tests matter. The next stage enlarges their list and decreases their tolerances.

**Example 4.2 (a central change of phase).** Multiplying an implementer \(v_n\) by a scalar \(\lambda_n\in\mathbb T\) leaves both \(\operatorname{Ad}v_n\) and its defect \(v_n^*\theta(v_n)\) unchanged. Indeed \(\theta(\lambda_n1)=\lambda_n1\). Thus scalar phase adjustments alone cannot remove a nontrivial defect. The correcting sequence \(x_n\) in (3.4) represents a unitary in the asymptotic centralizer; its coordinates need not be scalar.

## 5. Exercises with solutions

**Exercise 5.1 (introductory: check the product order).** In (3.4), replace \(u'_n=v_nx_n^*\) by \(x_n^*v_n\). Calculate its defect and decide whether (3.3) immediately removes it.

*Solution.* The new defect is
\[
v_n^*x_n\theta(x_n^*)\theta(v_n).
\]
It does not have the expression \(x_nw_n\theta(x_n^*)\) at the same coordinate. Because \(v_n\) varies and is not central, commuting the factors requires an additional argument. The original order gives (3.4) exactly and uses (3.3) directly.

**Exercise 5.2 (intermediate: a two-power estimate in a tracial factor).** Suppose \(M\) is tracial, \(u\) is unitary, and \(\|\theta(u)-u\|_2\leq a\). Show \(\|\theta(u^k)-u^k\|_2\leq |k|a\) for every integer \(k\).

*Solution.* For \(k>0\), expand as in (3.5). Left and right multiplication by unitaries preserve the tracial \(L^2\) norm, so each of the \(k\) terms has norm at most \(a\). For \(k<0\), apply the same argument to \(u^*\); its initial error equals \(\|\theta(u)-u\|_2\) and is therefore at most \(a\). The case \(k=0\) has error zero.

**Exercise 5.3 (intermediate: moving functionals).** Let \(\psi_n\to\psi\) in predual norm and \(a_n\) be bounded with \(\psi(a_n^*a_n)\to0\). Prove \(\psi_n(a_n^*a_n)\to0\).

*Solution.* If \(\|a_n\|\leq C\), then
\[
|\psi_n(a_n^*a_n)|\leq |\psi(a_n^*a_n)|+C^2\|\psi_n-\psi\|.
\]
Both terms tend to zero. Positivity of the moving functionals is unnecessary for this estimate.

**Exercise 5.4 (advanced: fixed powers versus varying powers).** In the scalar algebra take \(u_n=e^{i/n}\). Show that \(u_n^k\to1\) for each fixed \(k\), whereas \(u_n^n\) does not tend to \(1\).

*Solution.* For fixed \(k\), \(u_n^k=e^{ik/n}\to1\). But \(u_n^n=e^i\ne1\). This example does not concern a defect automorphism; it isolates the quantifier distinction that prevents a fixed-power convergence statement from being used uniformly over growing powers.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. Lemma 3.1.1 and its proof give the central-defect correction and invariance of fixed powers. Its cohomology input is Theorem 2.1.3 stated for every factor with separable predual. That scope supports the formulation here; the strong-stability assumption surrounding Lemma 3.1.1 is not needed in this proof. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Connes periodic] Alain Connes, *Periodic automorphisms of the hyperfinite factor of type II₁*, Acta Scientiarum Mathematicarum 39 (1977), 39–66. Background for periodic outer-conjugacy classification; no theorem from this paper is imported in the implementer proof above. [Open original text](https://alainconnes.org/wp-content/uploads/szego.pdf).

[Ando–Haagerup] Hiroshi Ando and Uffe Haagerup, *Ultraproducts of von Neumann algebras*, Journal of Functional Analysis 266 (2014), 6842–6913. Definition 4.34 and Proposition 4.35, pages 38–39 of arXiv version 3, provide modern context for the asymptotic-centralizer quotient. The exact quotient and lifting proofs consumed here are the programme provider named in the introduction. [Open author version](https://arxiv.org/abs/1212.5457v3).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. Lemma XVII.3.2 presents the same implementer result in its strongly stable setting. Sections 1 and 3 here give separate predual transport and paired-coordinate subsequence arguments. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10453-8).
