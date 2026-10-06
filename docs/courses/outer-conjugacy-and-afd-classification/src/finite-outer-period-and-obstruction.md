# Finite outer period and obstruction

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026; revised by GPT-6 Astra (OpenAI), Ultra, October 2026, with writing-AI self-checking. New original text is public domain (CC0).*

## Introduction

An automorphism can have a finite order in the outer automorphism group even when its ordinary powers never return to the identity. At its first inner power, a unitary implements that power. The automorphism moves this implementing unitary by a scalar phase. That phase is an invariant of outer conjugacy and measures whether an inner perturbation can turn the automorphism into a genuine finite cyclic action.

We define the invariant on arbitrary factors, check its behavior under inner perturbation and tensor product, and construct every possible pair of invariants on the hyperfinite II₁ factor.

The outer-period and phase invariants originate in [Connes periodic], Section 1; [Connes outer] places them in the general outer-conjugacy problem. For the operator preliminaries, [Peterson], Corollary 2.5.8 and Theorem 2.7.6, supplies polar decomposition and bounded Borel calculus in a von Neumann algebra. Factor intertwiners and the extension from an invariant corner are proved below. Our basic operator inputs are the [bounded Borel calculus for normal operators, Theorem 8.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators.html#oa-fnd-st-08), its [unitary logarithm, Exercise 3](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators.html#exercises), and [polar decomposition inside a von Neumann algebra, Proposition 7.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-09). We use the [normal regular crossed-product representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/averaging-crossed-products-injectivity.html#3-the-regular-crossed-product); Section 4 constructs its discrete coefficient expectation, trace and Fourier expansion directly, as well as the needed aperiodic product automorphism. The crossed-product realization in Section 4 follows [Takesaki III], Proposition XVII.3.15, with its coefficient expectation, Fourier expansion and minimal-period calculation supplied below. For this realization, [amenable crossed-product injectivity, Corollary 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/averaging-crossed-products-injectivity.html#corollary-3-1), and [injective II₁ uniqueness, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/unitary-couplings-and-finite-injective-factors.html#theorem-5-1), give the exact imports. The latter also has the independently written [small-corner proof, Theorem 4.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/small-corners-and-the-second-injective-proof.html#theorem-4-1).

## 1. The implementing phase

For a factor \(M\), the **outer period** \(p_o(\theta)\) is the nonnegative integer determined by
\[
\{k\in\mathbb Z:\theta^k\in\operatorname{Inn}M\}=p_o(\theta)\mathbb Z.
\tag{1.1}
\]
The value \(0\) means that no nonzero power is inner. This differs from the asymptotic period \(p_a\), which tests central triviality of powers. Since inner automorphisms are centrally trivial, finite positive outer period implies \(p_a(\theta)\mid p_o(\theta)\). Finite asymptotic period alone does not imply that any positive power is inner.

Suppose \(p=p_o(\theta)>0\), and choose \(U\in\mathcal U(M)\) with \(\theta^p=\operatorname{Ad}U\).

**Proposition 1.1.** There is a unique scalar \(\gamma\in\mathbb T\) with
\[
\theta(U)=\gamma U,\qquad \gamma^p=1.
\tag{1.2}
\]
It is independent of the choice of implementing unitary. The pair \((p,\gamma)\) is invariant under outer conjugacy.

*Proof.* Commutativity of \(\theta\) with its \(p\)-th power gives
\[
\operatorname{Ad}\theta(U)
=\theta\circ\operatorname{Ad}U\circ\theta^{-1}
=\operatorname{Ad}U.
\]
Thus \(U^*\theta(U)\) is central, hence a scalar of modulus one. Iteration gives \(\theta^p(U)=\gamma^pU\). But \(\operatorname{Ad}U(U)=U\), so \(\gamma^p=1\). Any other implementing unitary is \(zU\) with \(z\in\mathbb T\); its phase is the same.

Conjugation by an isomorphism transports both the implementing unitary and equation (1.2), so it preserves \(p,\gamma\). For an inner perturbation \(\eta=\operatorname{Ad}v\circ\theta\), set
\[
v_k=v\,\theta(v)\cdots\theta^{k-1}(v)\quad(k\geq1).
\tag{1.3}
\]
Then \(\eta^k=\operatorname{Ad}v_k\circ\theta^k\). The outer period is unchanged, and \(\eta^p=\operatorname{Ad}(v_pU)\). Finally
\[
\begin{aligned}
\eta(v_pU)&=v\theta(v_p)\theta(U)v^*\\
&=\gamma v_{p+1}Uv^*\\
&=\gamma v_p\theta^p(v)Uv^*\\
&=\gamma v_pU.
\end{aligned}
\tag{1.4}
\]
We used \(\theta^p(v)=UvU^*\). Hence the phase is unchanged. Inner perturbation followed by isomorphism is outer conjugacy, proving the assertion. \(\square\)

We call \(\gamma=\operatorname{Ob}(\theta)\) the **obstruction**. Its definition requires finite positive outer period. When \(p=1\), necessarily \(\gamma=1\).

## 2. When a cyclic action can be obtained

**Proposition 2.1 (vanishing obstruction).** If \(p_o(\theta)=p>0\), the following are equivalent:

1. \(\operatorname{Ob}(\theta)=1\).
2. An inner perturbation \(\eta=\operatorname{Ad}v\circ\theta\) satisfies \(\eta^p=\mathrm{id}\).

In that case, \(\eta\) defines a faithful, properly outer action of \(\mathbb Z/p\mathbb Z\) when \(p>1\).

*Proof.* Suppose the obstruction is \(1\). The unitary \(U\) implementing \(\theta^p\) is fixed by \(\theta\). Choose a bounded self-adjoint logarithm \(h\) of \(U\) by Borel functional calculus, so \(U=e^{ih}\). The logarithm belongs to \(W^*(U)\subset M\). Since \(\theta(U)=U\), the automorphism fixes every polynomial in \(U,U^*\); normality then makes it the identity on their ultraweak closure \(W^*(U)\). In particular \(\theta(h)=h\). Put \(v=e^{-ih/p}\). Then \(\theta(v)=v\) and \(v^p=U^*\). Equation (1.3) gives
\[
(\operatorname{Ad}v\circ\theta)^p
=\operatorname{Ad}(v^pU)=\mathrm{id}.
\tag{2.1}
\]
Its first \(p-1\) powers are outer, since its outer period remains \(p\). To check proper outerness on an arbitrary factor, suppose an automorphism \(\beta\) has a nonzero projection \(e\) with \(\beta(e)=e\) and \(\beta|_{eMe}=\operatorname{Ad}u\), where \(u\in eMe\) is unitary for the corner unit \(e\). We show that \(\beta\) is inner on \(M\).

In a faithful representation of \(M\), the projection onto \(\overline{MeH}\) commutes with both \(M\) and \(M'\), and is nonzero. Factoriality makes it \(1\); this is the central-support identity \(c(e)=1\). By Zorn's lemma choose a maximal family \((v_i)_{i\in I}\) of nonzero partial isometries with \(q_i=v_i^*v_i\leq e\) and mutually orthogonal ranges \(r_i=v_iv_i^*\). If \(f=1-\sum_i r_i\ne0\), then \(fMe\ne\{0\}\): otherwise \(f\) annihilates the dense subspace \(MeH\). Choose \(0\ne y\in fMe\). Its polar partial isometry has initial projection at most \(e\) and range at most \(f\), contradicting maximality. Hence \(\sum_i r_i=1\). Every sum here is the strong limit over finite subsets of \(I\); no countability is assumed.

Set \(t_i=\beta(v_i)uv_i^*\). The corner identity \(\beta(q_i)=u q_i u^*\) and \(v_i^*v_j=0\) for \(i\ne j\) give
\[
\begin{aligned}
t_i^*t_i&=v_i u^*\beta(q_i)u v_i^*\\
&=v_iq_iv_i^*=r_i,\\
t_it_i^*&=\beta(v_i)u q_i u^*\beta(v_i^*)\\
&=\beta(v_iq_iv_i^*)=\beta(r_i),\\
t_i^*t_j&=t_it_j^*=0\quad(i\ne j).
\end{aligned}
\]
Both families of support projections sum strongly to \(1\), so the finite sums of \(t_i\), and of their adjoints, converge strongly to a unitary
\[
W=\sum_i\beta(v_i)uv_i^*\in M.
\]
Indeed, multiplying these bounded strong limits gives \(W^*W=\sum_i r_i=1\) and \(WW^*=\sum_i\beta(r_i)=1\).
For \(x\in M\), one has \(v_i^*xv_j\in eMe\), so \(\beta(v_i^*xv_j)u=u(v_i^*xv_j)\). Using \(\sum_i r_i=1\), normality of \(\beta\), and \(\beta(q_j)u=u q_j\), we obtain
\[
\begin{aligned}
\beta(x)Wv_j
&=\beta(xv_j)u q_j=\beta(xv_j)u\\
&=\sum_i\beta(v_i)\beta(v_i^*xv_j)u\\
&=\sum_i\beta(v_i)u v_i^*xv_j=Wxv_j.
\end{aligned}
\]
These are strong limits over finite subsets. Since the ranges of the \(v_j\) span \(H\), \(\beta(x)W=Wx\), and \(\beta=\operatorname{Ad}W\). Thus an outer automorphism has no nonzero invariant inner corner; applying this to the first \(p-1\) powers gives the asserted properly outer cyclic action.

Conversely, if \(\eta^p=\mathrm{id}\), its outer period is still \(p\). The implementer \(1\) has phase \(1\). Proposition 1.1 transfers this phase back to \(\theta\). \(\square\)

For \(p=1\), the result simply says that an inner automorphism can be perturbed to the identity.

**Lemma 2.2 (the full-period cocycle condition).** If \(\theta^p=\mathrm{id}\), then \(\operatorname{Ad}v\circ\theta\) has \(p\)-th power equal to the identity exactly when
\[
v\theta(v)\cdots\theta^{p-1}(v)\in\mathbb T1.
\tag{2.2}
\]
After multiplying \(v\) by a suitable scalar, that product can be made \(1\). The resulting iterated products form a unitary cocycle for \(\mathbb Z/p\mathbb Z\).

*Proof.* Equation (1.3) gives the \(p\)-th power as conjugation by the product in (2.2). On a factor this conjugation is the identity exactly when its implementer is scalar. If its value is \(z1\), choose \(\lambda\in\mathbb T\) with \(\lambda^p=z^{-1}\) and replace \(v\) by \(\lambda v\). The new product is \(1\), and the identity \(v_{j+k}=v_j\theta^j(v_k)\) then passes to indices modulo \(p\). \(\square\)

The scalar normalization in this lemma is necessary before applying a finite-group coboundary theorem.

## 3. Tensor products and powers

We first record a factor argument used to check the tensor product's outer period.

**Lemma 3.1 (slicing an inner tensor action).** Let \(M,N\) be factors and \(\alpha,\beta\) their automorphisms. If \(\alpha\otimes\beta\) is inner on \(M\overline\otimes N\), both \(\alpha\) and \(\beta\) are inner.

*Proof.* If \(V\) implements the tensor action, then
\[
V(x\otimes1)=(\alpha(x)\otimes1)V.
\]
Some normal slice \(a=(\mathrm{id}\otimes\psi)(V)\) is nonzero, since product normal functionals separate points. It satisfies \(ax=\alpha(x)a\). Taking adjoints and multiplying shows \(a^*a\in Z(M)\) and \(aa^*\in Z(M)\). Thus \(a^*a=c1\) with \(c>0\), and the polar isometry \(c^{-1/2}a\) has a nonzero scalar range projection, hence range projection \(1\). It is a unitary implementing \(\alpha\). Slice in the other direction to obtain the same conclusion for \(\beta\). \(\square\)

**Proposition 3.2.** If \(\alpha,\beta\) have the same finite positive outer period \(p\), then
\[
\begin{gathered}
p_o(\alpha\otimes\beta)=p,\\
\operatorname{Ob}(\alpha\otimes\beta)
=\operatorname{Ob}(\alpha)\operatorname{Ob}(\beta).
\end{gathered}
\tag{3.1}
\]

*Proof.* If \(U,V\) implement their \(p\)-th powers, \(U\otimes V\) implements the \(p\)-th power of their tensor action. No smaller positive power is inner, by Lemma 3.1. On this implementer, the tensor action multiplies the two phases. Proposition 1.1 therefore gives (3.1). \(\square\)

**Proposition 3.3.** Suppose \(p_o(\theta)=p>0\). If \(r\in\mathbb Z\) is relatively prime to \(p\), then
\[
p_o(\theta^r)=p,\qquad
\operatorname{Ob}(\theta^r)=\operatorname{Ob}(\theta)^{r^2}.
\tag{3.2}
\]
In particular \(\operatorname{Ob}(\theta^{-1})=\operatorname{Ob}(\theta)\).

*Proof.* The class of \(\theta\) has order \(p\) in \(\operatorname{Out}M\), so its \(r\)-th power also has order \(p\). If \(\theta^p=\operatorname{Ad}U\) and \(\theta(U)=\gamma U\), then
\[
\begin{gathered}
(\theta^r)^p=\operatorname{Ad}(U^r),\\
\theta^r(U^r)=(\gamma^rU)^r=\gamma^{r^2}U^r.
\end{gathered}
\]
These identities also hold for negative \(r\), by inversion. This proves (3.2). \(\square\)

Thus tensoring with the inverse automorphism does not generally cancel the obstruction: it gives the square of the phase. Cancellation requires an automorphism with the reciprocal phase.

## 4. Constructing every period and phase on the hyperfinite factor

### An aperiodic product model

Choose integers \(n_v\geq2\) with \(n_v\to\infty\), for example \(n_v=2^v\). In the tracial infinite product
\[
R=\overline{\bigotimes_{v\geq1}}(M_{n_v},\operatorname{tr}_{n_v}),
\qquad
a=\bigotimes_{v\geq1}\operatorname{Ad}c_v,
\]
let \(c_v\) be the cyclic shift on the \(v\)-th coordinate. The product is the hyperfinite II₁ factor by the tracial product construction and [finite AFD uniqueness theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/hyperfinite-finite-factors.html#theorem-5-1). The coordinate automorphisms preserve the product trace. Their action on the algebraic finite tensor union therefore extends by its trace-GNS unitary to a normal automorphism \(a\), with inverse given by the inverse coordinate actions.

**Aperiodicity of the model.** Every nonzero power of \(a\) is outer.

*Proof.* Fix \(q\in\mathbb Z\setminus\{0\}\). In a Fourier basis \((\xi_l)_{l\in\mathbb Z/n_v\mathbb Z}\), choose the orientation so that
\[
c_v\xi_l=e^{2\pi il/n_v}\xi_l.
\]
Let \(r_v\) be an integer nearest to \(n_v/(2|q|)\), and let \(x_v\) be the unitary in the \(v\)-th coordinate given by \(x_v\xi_l=\xi_{l+r_v}\). Matrix multiplication gives
\[
\begin{gathered}
\operatorname{Ad}c_v(x_v)=e^{2\pi ir_v/n_v}x_v,\\
\left|\frac{qr_v}{n_v}-\frac{\operatorname{sgn}(q)}2\right|
\leq\frac{|q|}{2n_v}.
\end{gathered}
\]
Consequently \(e^{2\pi iqr_v/n_v}\to-1\), and, since \(\|x_v\|_2=1\),
\[
\|a^q(x_v)-x_v\|_2
=|e^{2\pi iqr_v/n_v}-1|\longrightarrow2.
\]
The tail embeddings of \(x_v\) form a central sequence. Indeed they eventually commute with each fixed finite tensor product. For \(y\in R\), approximate \(y\) in \(L^2\) by such an element \(y_0\); the unitary bound gives \(\|[x_v,y]\|_2\leq2\|y-y_0\|_2\) for all sufficiently large \(v\). If \(a^q=\operatorname{Ad}w\) for one \(w\in\mathcal U(R)\), centrality would give
\[
\|a^q(x_v)-x_v\|_2=\|[w,x_v]\|_2\longrightarrow0,
\]
contradicting the limit \(2\). This proves the assertion for each nonzero \(q\), including negative powers. \(\square\)

Fix \(p\geq1\) and \(\gamma\in\mathbb T\) with \(\gamma^p=1\), and use this aperiodic automorphism \(a\) in the realization below.

Form the crossed product
\[
P=R\rtimes_{a^p}\mathbb Z.
\tag{4.1}
\]
Write \(V\) for its canonical unitary, with
\[
VxV^*=a^p(x),\quad x\in R,
\]
and \(E:P\to R\) for the normal conditional expectation. Its trace is \(\tau_P=\tau_R\circ E\).

### The discrete coefficient expectation

Here is the required expectation and Fourier interface in the regular model, with \(b=a^p\). Represent \(R\) by left multiplication on \(L^2(R,\tau_R)\), and write
\[
\begin{gathered}
\mathcal H=\ell^2(\mathbb Z,L^2(R,\tau_R)),\\
(\pi(x)\xi)_k=b^{-k}(x)\xi_k,\\
(V\xi)_k=\xi_{k-1}.
\end{gathered}
\]
Let \(J_k\) embed \(L^2(R,\tau_R)\) as the \(k\)-th coordinate. On finite sums \(z=\sum_m V^m x_m\), direct multiplication gives
\[
J_k^*zJ_l=b^{-l}(x_{k-l}),\qquad J_0^*zJ_0=x_0.
\]
Finite sums form an ultraweakly dense *-algebra in \(P\). Compression is ultraweakly continuous, and the coefficient algebra is ultraweakly closed, so \(E(z)=J_0^*zJ_0\in R\) is defined for every \(z\in P\). It is normal, unital, completely positive, fixes \(R\), and is \(R\)-bimodular because \(\pi(x)J_0=J_0x\). Thus it is a normal conditional expectation. Ultraweak continuity extends the matrix identity to
\[
J_k^*zJ_l=b^{-l}\bigl(E(V^{-(k-l)}z)\bigr)
\qquad(z\in P).
\]
If \(z\geq0\) and \(E(z)=0\), each diagonal block is zero, hence \(z^{1/2}J_l=0\) for every \(l\), and \(z=0\). This proves faithfulness. The same matrix identity shows that all coefficients \(E(V^{-m}z)\) determine \(z\).

**Lemma 4.1.** The algebra \(P\) is a hyperfinite II₁ factor with separable predual.

*Proof.* The crossed-product expectation is faithful. Invariance of \(\tau_R\) under \(a^p\) makes \(\tau_R\circ E\) a faithful normal trace; on finite Fourier sums its trace identity follows directly from the multiplication rule
\[
(xV^m)(yV^l)=x\,a^{pm}(y)V^{m+l}.
\]
For each fixed finite Fourier sum, ultraweak continuity extends the trace identity in the other variable to \(P\); repeating with the variables reversed extends it to every pair in \(P\).

Put \(\Omega=J_0\widehat1\). Then \(\tau_P(z)=\langle\Omega,z\Omega\rangle\), and \(\Omega\) is cyclic because \(V^m x\Omega=J_m\widehat x\) spans a dense subspace. Consequently \(z\mapsto z\Omega\) identifies \(L^2(P,\tau_P)\) with \(\mathcal H\). The matrix identity gives \(J_m^*z\Omega=\widehat{E(V^{-m}z)}\), so coordinate orthogonality yields
\[
\begin{gathered}
\|z\|_{2,\tau_P}^2
=\sum_{m\in\mathbb Z}\|E(V^{-m}z)\|_{2,\tau_R}^2,\\
z=\sum_{m\in\mathbb Z}V^m E(V^{-m}z)\\
\text{in }L^2(P,\tau_P).
\end{gathered}
\]

If \(z\in Z(P)\), set \(z_m=E(V^{-m}z)\in R\). Commutation with \(x\in R\) gives
\[
z_mx=a^{-pm}(x)z_m.
\tag{4.2}
\]
For \(m\ne0\), a nonzero \(z_m\) would implement the outer automorphism \(a^{-pm}\) by the polar argument in Lemma 3.1, which is impossible. For \(m=0\), (4.2) gives \(z_0\in\mathbb C1\). Uniqueness of the \(L^2\) Fourier expansion
\[
z=\sum_{m\in\mathbb Z}V^m E(V^{-m}z)
\tag{4.3}
\]
then shows \(z=z_0\). Hence \(P\) is a factor. It is infinite dimensional, since it contains \(R\); being finite, it has type II₁. Its regular crossed-product representation is on a separable Hilbert space.

The increasing finite tensor algebras generating \(R\) make it injective by [Corollary 5.2 of the averaging lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/averaging-crossed-products-injectivity.html#corollary-5-2). The discrete group \(\mathbb Z\) is amenable. [Amenable crossed-product injectivity, Corollary 3.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/averaging-crossed-products-injectivity.html#corollary-3-1), therefore makes \(P\) injective. The hypotheses of [injective II₁ uniqueness, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/unitary-couplings-and-finite-injective-factors.html#theorem-5-1), now apply: \(P\) is a II₁ factor with separable predual, so \(P\cong R\). \(\square\)

Extend \(a\) to an automorphism \(\widetilde a\) of \(P\) by
\[
\widetilde a(x)=a(x),\qquad \widetilde a(V)=V.
\]
This extension is normal for a concrete reason. On \(L^2(R,\tau_R)\), let \(T\widehat{x}=\widehat{a(x)}\). Trace preservation makes \(T\) unitary. On \(\mathcal H\), the diagonal unitary \((\mathcal T\xi)_k=T\xi_k\) commutes with \(V\), and \(ab=ba\) gives
\[
\mathcal T\pi(x)\mathcal T^*=\pi(a(x)).
\]
Conjugation by \(\mathcal T\) therefore restricts to \(\widetilde a\) on \(P\); its inverse uses \(a^{-1}\). On the generating algebra \(R\) and the unitary \(V\), we have
\[
\widetilde a^{\,p}=\operatorname{Ad}V.
\tag{4.4}
\]
There is also the dual-phase automorphism \(d_\gamma\), fixing \(R\) and sending \(V\) to \(\gamma V\). In the regular representation it is implemented on the \(\mathbb Z\) coordinate by multiplication by \(\gamma^m\). It commutes with \(\widetilde a\), and \(d_\gamma^p=\mathrm{id}\). Define
\[
\theta_{p,\gamma}=d_\gamma\circ\widetilde a.
\tag{4.5}
\]

**Theorem 4.2 (realization).** On \(P\cong R\), this automorphism satisfies
\[
p_o(\theta_{p,\gamma})=p,\qquad
\operatorname{Ob}(\theta_{p,\gamma})=\gamma.
\tag{4.6}
\]

*Proof.* Commutation and \(d_\gamma^p=\mathrm{id}\) give \(\theta_{p,\gamma}^p=\operatorname{Ad}V\). Moreover \(\theta_{p,\gamma}(V)=\gamma V\), so its implementing phase is \(\gamma\).

Suppose a power \(1\leq j<p\) were inner, with implementer \(z\). On \(R\), its restriction is \(a^j\), so \(zx=a^j(x)z\). Taking Fourier coefficients gives
\[
\begin{gathered}
E(V^{-m}z)x=a^{j-pm}(x)E(V^{-m}z)\\
(m\in\mathbb Z).
\end{gathered}
\tag{4.7}
\]
Every exponent \(j-pm\) is nonzero. Every corresponding automorphism is outer; the same polar argument makes all these coefficients zero. Fourier uniqueness would give \(z=0\), contradicting unitarity. Thus \(p\) is the first inner power, and (4.6) follows. \(\square\)

For \(p=1\), the only phase is \(1\); (4.4) makes the model inner, as required. The construction prescribes outer period. It does not assert that the ordinary period is \(p\).

**Example 4.3.** For \(p=3\), the possible phases are \(1,e^{2\pi i/3},e^{4\pi i/3}\). The realization gives three distinct outer-conjugacy classes because Proposition 1.1 distinguishes their phases. For the nontrivial phases, Proposition 2.1 excludes any inner perturbation whose third power is the identity.

## 5. Exercises with solutions

**Exercise 5.1 (introductory: the phase restriction).** If \(\theta^4=\operatorname{Ad}U\) and \(\theta(U)=\gamma U\), list the possible \(\gamma\). Does this alone prove \(p_o(\theta)=4\)?

*Solution.* Iterating on \(U\) gives \(\gamma^4=1\), so \(\gamma\in\{1,i,-1,-i\}\). The hypothesis only gives an inner fourth power. An earlier power could be inner; for example \(\theta=\mathrm{id}\) and \(U=1\) satisfy it. To call \(\gamma\) the obstruction at outer period four, one must separately verify that four is the first inner power.

**Exercise 5.2 (intermediate: tensor cancellation).** Let \(\alpha,\beta\) each have outer period five and obstruction phases \(e^{2\pi i/5}\) and \(e^{-2\pi i/5}\), respectively. Find the outer period and obstruction of their tensor product, and determine whether an inner perturbation can become a five-periodic action.

*Solution.* Proposition 3.2 gives outer period five and phase \(1\). Proposition 2.1 supplies an inner perturbation with fifth power equal to the identity. Its first four powers remain outer, so it gives a free cyclic action.

**Exercise 5.3 (intermediate: scalar normalization).** Suppose \(\theta^3=\mathrm{id}\) and \(v\theta(v)\theta^2(v)=-1\). Find a scalar multiplying \(v\) that makes the iterated product \(1\).

*Solution.* Choose \(\lambda=e^{i\pi/3}\), so \(\lambda^3=-1\). Replacing \(v\) by \(\lambda v\) multiplies the product by \(\lambda^3\), turning \(-1\) into \(1\). The associated products are now a cocycle on \(\mathbb Z/3\mathbb Z\).

**Exercise 5.4 (advanced: the inverse has the same phase).** Suppose \(p=p_o(\theta)>0\), \(\theta^p=\operatorname{Ad}U\), and \(\theta(U)=\gamma U\). Check the obstruction of \(\theta^{-1}\) directly, without Proposition 3.3.

*Solution.* The \(p\)-th power of \(\theta^{-1}\) is \(\operatorname{Ad}U^*\). From \(\theta(U)=\gamma U\), we get \(\theta^{-1}(U)=\gamma^{-1}U\), and hence \(\theta^{-1}(U^*)=\gamma U^*\). Thus the implementing phase of the inverse is \(\gamma\), not \(\gamma^{-1}\).

**Exercise 5.5 (advanced: the Fourier exponent).** Derive (4.7) from \(zx=a^j(x)z\) and explain why the range \(1\leq j<p\) matters.

*Solution.* Multiply the intertwining equation on the left by \(V^{-m}\). Since \(V^{-m}a^j(x)=a^{j-pm}(x)V^{-m}\), applying the \(R\)-bimodular expectation gives (4.7). In the specified range, \(j\) cannot be a multiple of \(p\), so no integer \(m\) makes \(j-pm=0\). All coefficients therefore intertwine genuinely outer powers. At \(j=p\), the coefficient for \(m=1\) has exponent zero, and the argument permits the actual implementer \(V\).

## References

[Connes periodic] Alain Connes, *Periodic automorphisms of the hyperfinite factor of type II₁*, Acta Scientiarum Mathematicarum 39 (1977), 39–66. The introduction and Section 1 distinguish outer period, implementing phase and ordinary period. [Open original text](https://alainconnes.org/wp-content/uploads/szego.pdf).

[Connes outer] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. This supplies the centralizer and aperiodic comparison mechanisms used by the prerequisites. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Peterson] Jesse Peterson, *Notes on von Neumann algebras*, 2013, Corollary 2.5.8 (polar decomposition inside the algebra), Theorem 2.7.6 and Corollary 2.7.8 (bounded Borel calculus and unitary logarithms). [Author's notes](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003, Proposition XVII.3.13, Definition XVII.3.14, Proposition XVII.3.15 and the cyclic reduction on p.285. [Publisher edition](https://doi.org/10.1007/978-3-662-10453-8).
