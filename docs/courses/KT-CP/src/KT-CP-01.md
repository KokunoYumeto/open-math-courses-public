# C*-dynamical systems and full crossed products

*Written by GPT-6.1 Sol (OpenAI), October 2026. Contributions by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Public domain (CC0).*

An action on an algebra describes how its observables change under a symmetry. A crossed product puts the observables and the operators implementing that symmetry into one algebra. Its defining relation is covariance. Its defining norm allows every continuous covariant representation, which explains the word **full**.

This lesson develops the multiplier version of that construction, proves its universal property and exactness for invariant ideals, and computes several first examples. The translation action on a discrete group will turn into the algebra of compact operators. That calculation gives a concrete way to see how functions and translations produce matrix entries.

Preparatory reading is [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20), and [Haar measure on locally compact groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups.html). We also use [Unitary representations and the two group C* completions](../prerequisites/src/OA-FLOW/repaired-20261004/group-representations-and-completions.md), [Covariance and crossed products with nonunital coefficients](../prerequisites/src/OA-FLOW/repaired-20261004/covariance-and-crossed-products.md), and *Compact operators, multipliers and the strict topology*. The precise statements used from these subjects are collected under “What this lesson does not prove”. Basic references are [Schulz-Baldes–Stoiber], [Connes], [Blackadar, Operator Algebras], and [Blackadar, K-Theory].

Throughout, \(G\) is a locally compact Hausdorff group, \(A\) is a C*-algebra, and Haar measure is on the left. No separability, countability or unimodularity assumption is imposed. We fix the modular function by

\[
\int_G h(rs)\,dr=\Delta(s)^{-1}\int_G h(r)\,dr.
\]

Consequently inversion contributes the factor \(\Delta(t^{-1})\). Integrals of coefficient functions are Bochner integrals. The integrals of operators below are evaluated on vectors, or strictly in a multiplier algebra.

## 1. Covariance dictates multiplication

A **C*-dynamical system** is a triple \((A,G,\alpha)\), where \(\alpha:G\to\operatorname{Aut}(A)\) is a homomorphism and \(s\mapsto\alpha_s(a)\) is norm continuous for each \(a\in A\). This continuity condition is called point-norm continuity.

A **covariant representation** consists of a nondegenerate *-representation \(\pi:A\to B(H)\) and a strongly continuous unitary representation \(U:G\to\mathcal U(H)\) satisfying

\[
U_s\pi(a)U_s^*=\pi(\alpha_s(a)).
\tag{1.1}
\]

Nondegeneracy means \(\overline{\pi(A)H}=H\). It is essential for recovering both members of the pair from their integrated operators.

For a continuous left action on a locally compact Hausdorff space \(X\), the coefficient action is

\[
\alpha_s(a)(x)=a(s^{-1}x),\qquad a\in C_0(X).
\tag{1.2}
\]

This is point-norm continuous. For \(a\in C_c(X)\), translations near the identity have their supports in a common compact set: if \(W\) is a compact identity neighborhood and \(K=\operatorname{supp}a\), that set is \(WK\). Joint continuity and a finite-cover argument give uniform convergence of the translates on it. Approximation of \(C_0(X)\) by \(C_c(X)\), and the isometry of each translate, give the assertion for all \(a\).

Moving \(\pi(b)\) past \(U_s\) in a product \(\pi(a)U_s\pi(b)U_t\) produces \(\pi(a\alpha_s(b))U_{st}\). Thus on \(C_c(G,A)\) define

\[
\begin{aligned}
(f*g)(t)&=\int_G f(s)\alpha_s(g(s^{-1}t))\,ds,\\
f^*(t)&=\Delta(t^{-1})\alpha_t(f(t^{-1})^*),\\
\|f\|_1&=\int_G\|f(s)\|\,ds.
\end{aligned}
\tag{1.3}
\]

**Proposition 1.1.** These operations make \(C_c(G,A)\) a *-algebra. They extend to its \(L^1\)-completion, with

\[
\|f*g\|_1\leq\|f\|_1\|g\|_1,
\qquad \|f^*\|_1=\|f\|_1.
\tag{1.4}
\]

**Proof.** If \(f,g\) have supports \(K,L\), the convolution has support in \(KL\). The integrand depends continuously on its parameters. Restriction to a compact integration set and uniform continuity there prove continuity of the convolution. The involution is continuous and has support in \(K^{-1}\).

Both associative bracketings, after the left Haar substitution in the inner integral, equal

\[
\int_G\!\int_G f(r)\alpha_r(g(s))\alpha_{rs}(h(s^{-1}r^{-1}t))\,ds\,dr.
\tag{1.5}
\]

For compact supports this is an absolutely integrable Bochner integral. Fubini therefore applies. The same estimate integrated also in \(t\) bounds its absolute integral by \(\|f\|_1\|g\|_1\|h\|_1\).

Conjugate linearity is immediate, and multiplicativity of \(\Delta\) gives \((f^*)^*=f\). To check reversal of products, expansion gives

\[
(g^**f^*)(t)=\Delta(t^{-1})
\int_G\alpha_s(g(s^{-1})^*)\alpha_t(f(t^{-1}s)^*)\,ds.
\]

Putting \(s=tr\) turns this into the adjoint of the convolution at \(t^{-1}\), followed by \(\Delta(t^{-1})\alpha_t\). Hence it is \((f*g)^*(t)\). Finally, isometry of \(\alpha_s\) and left invariance prove the product estimate in (1.4); inversion proves the involution estimate. Completion now extends all the algebra identities. \(\square\)

Write \(L^1(G,A)\) for this completion. For a covariant pair its **integrated form** is

\[
(\pi\rtimes U)(f)\xi=\int_G\pi(f(s))U_s\xi\,ds.
\tag{1.6}
\]

The vector integrand is continuous on compact supports, and

\[
\|(\pi\rtimes U)(f)\xi\|
\leq\int_G\|f(s)\|\|\xi\|\,ds.
\tag{1.7}
\]

Thus \(\|\pi\rtimes U(f)\|\leq\|f\|_1\). Covariance and inversion show that (1.6) preserves products and adjoints; this integrated-form theorem and its nondegeneracy are supplied by the coefficient-recovery lesson. We use its converse too: every nondegenerate representation of \(L^1(G,A)\) is the integrated form of exactly one such pair. We do not repeat the recovery argument.

## 2. The universal algebra and its multipliers

The universal norm is

\[
\|f\|_u=\sup_{(\pi,U)}\|(\pi\rtimes U)(f)\|.
\tag{2.1}
\]

It is finite by (1.7). The regular-faithfulness theorem in *Covariance and crossed products with nonunital coefficients* says that it is a norm, rather than only a seminorm. That lesson also establishes the set-sized interpretation of this supremum and the C*-identity. Its completion is the **full crossed product**

\[
C=A\rtimes_\alpha G.
\]

We use that established completion. Our task is to put its generators in \(M(C)\) and formulate the universal property there.

For a C*-algebra \(B\), a homomorphism \(\pi:A\to M(B)\) is nondegenerate when \(\overline{\pi(A)B}=B\). A unitary map \(U:G\to\mathcal U(M(B))\) is **strictly continuous** when \(U_sb\) and \(bU_s\) vary in norm for every \(b\in B\). A multiplier covariant pair satisfies (1.1) with values in \(M(B)\).

**Theorem 2.1.** There are a nondegenerate injective homomorphism \(i_A:A\to M(C)\) and a strictly continuous unitary homomorphism \(i_G:G\to\mathcal U(M(C))\) satisfying covariance. If \(A\ne0\), the group homomorphism is injective. On \(C_c(G,A)\) their actions are

\[
\begin{aligned}
(i_A(a)f)(t)&=af(t),& (fi_A(a))(t)&=f(t)\alpha_t(a),\\
(i_G(s)f)(t)&=\alpha_s(f(s^{-1}t)),&
(fi_G(s))(t)&=\Delta(s)^{-1}f(ts^{-1}).
\end{aligned}
\tag{2.2}
\]

**Proof.** Realize \(C\) faithfully and nondegenerately by the direct sum of a set of covariant representations sufficient to compute (2.1). The set restriction and nondegeneracy are among the completion results just recalled. Let \(P(a)\) and \(V_s\) be the direct sums of their coefficients and unitaries. Finite-summand approximation proves strong continuity of \(V\).

Multiplying an integrated operator on its left or right by \(P(a)\) or \(V_s\), using covariance and a Haar substitution, gives precisely (2.2). Each resulting function is in \(C_c(G,A)\). The four operations are bounded in universal norm: coefficient multiplication has bound \(\|a\|\), and group multiplication is isometric. Their extensions therefore idealize the concrete algebra \(C\). The multiplier idealizer theorem identifies \(P(a),V_s\) with elements of \(M(C)\). Their algebraic relations already hold in the faithful representation, so they give the claimed homomorphisms and covariance.

If \((e_j)\) is a contractive approximate identity of \(A\), then \(e_jf(t)\to f(t)\) uniformly on the compact norm image of \(f\). Hence \(i_A(e_j)f\to f\) in \(L^1\), and then in \(C\). Uniform boundedness extends convergence to all of \(C\), proving nondegeneracy of \(i_A\).

The two group formulas in (2.2) are continuous in \(L^1\) as functions of \(s\), by point-norm continuity, continuity on compact sets, and the Haar translation rules. Their norms are uniformly bounded in \(C\). Density therefore proves strict continuity of \(i_G\).

To prove injectivity, use the existing regular covariant pair associated to a faithful nondegenerate \(\rho:A\to B(K)\):

\
[\widetilde\rho(a)\xi=\rho(\alpha_{r^{-1}}(a))\xi(r),
\qquad \lambda_s\xi=\xi(s^{-1}r).
\tag{2.3}
\]

If \(i_A(a)=0\), then \(\widetilde\rho(a)=0\). For \(a\ne0\), a vector detecting \(\rho(a)\), continuity near the identity, and a scalar compactly supported test function contradict this. Thus \(i_A\) is faithful. If \(A\ne0\), choose \(K\ne0\). Distinct left translations act differently on a function supported in a small neighborhood whose two translates are disjoint. Consequently \(\lambda_s\ne\lambda_t\) for \(s\ne t\), proving the assertion for \(i_G\). \(\square\)

The group correspondence in *Unitary representations and the two group C* completions* integrates \(i_G\) to a nondegenerate homomorphism

\[
j_G:C^*(G)\longrightarrow M(C),\qquad
j_G(\varphi)=\int_G\varphi(s)i_G(s)\,ds.
\tag{2.4}
\]

Here nondegeneracy follows directly from integral-one functions with supports shrinking to the identity and strict continuity in Theorem 2.1. The bounded extension from \(L^1(G)\) to \(C^*(G)\) follows by composing with a faithful representation of \(C\) and applying the group universal norm. The map \(j_G\) is not asserted to be injective. Injectivity of the group elements and injectivity of their full group-algebra integration are different statements.

**Proposition 2.2.** For \(a\in A\) and \(\varphi\in C_c(G)\),

\[
i_A(a)j_G(\varphi)=[t\mapsto\varphi(t)a]\in C.
\tag{2.5}
\]

These products have dense linear span in \(C\). Also \(i_A(a)j_G(x)\in C\) for every \(x\in C^*(G)\).

**Proof.** The equality follows by integration in the faithful realization above. For a general \(f\in C_c(G,A)\), its compact norm image can be approximated uniformly by finitely many values \(a_k\). Choose a finite partition of unity on its compact support, extended with compact support to a neighborhood, and approximate \(f\) by \(\sum_k\varphi_k a_k\). Include a region where the value is zero so the approximation also holds off the original support. All supports lie in a fixed compact set, so uniform error gives arbitrarily small \(L^1\) error. Since \(\|\cdot\|_u\leq\|\cdot\|_1\), (2.5) proves density. Approximate \(x\) in \(C^*(G)\) by \(C_c(G)\) and use closedness of \(C\subset M(C)\) for the last assertion. \(\square\)

This is the meaning of generation by coefficients and group multipliers. For a nondiscrete group the individual generators need not belong to \(C\); their integrated products do.

**Theorem 2.3 (multiplier universal property).** For every nondegenerate multiplier covariant pair \((\pi,U)\) into \(M(B)\), there is a unique nondegenerate homomorphism

\[
\Phi=\pi\rtimes U:C\longrightarrow M(B)
\tag{2.6}
\]

whose strict unital extension satisfies

\[
\overline\Phi(i_A(a))=\pi(a),\qquad
\overline\Phi(i_G(s))=U_s.
\tag{2.7}
\]

Every nondegenerate homomorphism \(C\to M(B)\) arises from a unique pair this way.

**Proof.** For \(f\in C_c(G,A)\) form the strict integral

\[
T(f)=\int_G\pi(f(s))U_s\,ds.
\]

To specify it, multiply the integrand by \(b\in B\) on either side and take norm integrals in \(B\). These bounded left and right operations satisfy the double-centralizer relation, and their adjoints are supplied by the involution calculation. Hence they define a multiplier.

Choose a faithful nondegenerate representation \(\sigma\) of \(B\). Its multiplier extension is faithful and isometric. The composed pair \((\overline\sigma\pi,\overline\sigma U)\) is a nondegenerate Hilbert-space covariant pair, so

\[
\|T(f)\|=\|\overline\sigma(T(f))\|\leq\|f\|_u.
\]

The product and adjoint identities for integration therefore extend \(T\) to (2.6).

For \(\varphi_V\geq0\) of integral one supported in a shrinking identity neighborhood, strict continuity gives \(U(\varphi_V)\to1\) strictly. Also \(\pi(e_j)\to1\) strictly by nondegeneracy. The bounded product net

\[
T(\varphi_V e_j)=\pi(e_j)U(\varphi_V)\longrightarrow1
\]

is strictly convergent. Thus \(\Phi(C)B\) is dense in \(B\). The multiplier extension theorem supplies \(\overline\Phi\). Apply (2.2) inside the integral to obtain (2.7), first after multiplication by \(\Phi(f)b\), and then on a dense subspace of \(B\). Equation (2.5) and its density prove uniqueness.

Conversely extend a nondegenerate \(\Phi\) strictly to \(M(C)\), and compose with \(i_A,i_G\). Nondegeneracy of \(i_A\) and strict continuity of \(i_G\) give the required pair. Passing the strict extension through the integral on compact supports shows its integrated form is \(\Phi\). This proves existence and uniqueness in the converse without repeating coefficient or group recovery from \(L^1\). \(\square\)

For a Hilbert \(B\)-module \(E\), replace \(M(B)\) by \(\mathcal L(E)=M(\mathcal K(E))\). A nondegenerate coefficient representation and a unitary group continuous on every vector give such a pair. To see strict continuity, use the compact module operators \(\theta_{x,y}(z)=x\langle y,z\rangle\): the estimates for \((U_s-U_t)\theta_{x,y}\) and \(\theta_{x,y}(U_s-U_t)\) are respectively bounded by \(\|(U_s-U_t)x\|\|y\|\) and \(\|x\|\|(U_s^*-U_t^*)y\|\). The latter tends to zero because \(U_s^*=U_{s^{-1}}\). Finite sums are dense in \(\mathcal K(E)\), and the operators are uniformly bounded, so both strict seminorms tend to zero. Theorem 2.3 applies with \(B\) replaced by \(\mathcal K(E)\). This includes arbitrary Hilbert modules, with no countable-generation assumption.

## 3. Passing to an invariant ideal or quotient

First consider an equivariant homomorphism \(\theta:A\to B\), with actions \(\alpha,\beta\) and \(\theta\alpha_s=\beta_s\theta\). Pointwise application defines a *-homomorphism on compactly supported coefficient functions.

**Proposition 3.1.** There is a homomorphism

\[
\theta\rtimes G:A\rtimes_\alpha G\longrightarrow B\rtimes_\beta G,
\qquad f\mapsto[t\mapsto\theta(f(t))].
\tag{3.1}
\]

It respects identities and composition. It is nondegenerate if \(\theta\) is nondegenerate, and is surjective if \(\theta\) is surjective.

**Proof.** In a covariant representation \((\sigma,V)\) of \(B\), the coefficient map \(\sigma\theta\) may be degenerate. Its essential space \(H_0=\overline{\sigma\theta(A)H}\) is invariant under \(V_s\) and \(V_s^*\), by equivariance. On \(H_0\) there is a nondegenerate covariant pair; on \(H_0^\perp\) every integrated coefficient is zero. Thus its norm is bounded by the full norm for \(A\). Taking suprema proves that the pointwise map is contractive and extends to (3.1). Algebraic identities on the dense functions prove functoriality.

If \(\theta\) is nondegenerate, \(\theta(e_j)b\to b\); uniform approximation on compact coefficient images proves nondegeneracy of (3.1). If \(\theta\) is surjective, every function \(\varphi(t)b\) has a lift \(\varphi(t)a\). Such functions span a dense subspace by Proposition 2.2. A C*-homomorphism has closed range, so (3.1) is surjective. \(\square\)

**Theorem 3.2 (full exactness).** Let \(I\) be a closed \(G\)-invariant ideal of \(A\). With the restricted and quotient actions, the sequence

\[
0\longrightarrow I\rtimes G
\overset{\iota\rtimes G}{\longrightarrow} A\rtimes G
\overset{q\rtimes G}{\longrightarrow}(A/I)\rtimes G
\longrightarrow0
\tag{3.2}
\]

is exact.

**Proof.** We prove injectivity before identifying the kernel. Every nondegenerate representation \(\sigma\) of \(I\) extends uniquely to a representation \(\widetilde\sigma\) of \(A\) characterized by

\[
\widetilde\sigma(a)\sigma(i)\xi=\sigma(ai)\xi.
\tag{3.3}
\]

The complete proof is [Exercise 5 in Section 7 of the multiplier reading](../prerequisites/src/hilbert-c-star-modules-and-morita-equivalence/compact-operators-multipliers-and-the-strict-topology.md#7-exercises-and-complete-solutions). Apply it to the nondegenerate map \(\sigma:I\to\mathcal L(H)=B(H)\), viewing \(H\) as a Hilbert module over \(\mathbb C\), to obtain its multiplier extension \(\overline\sigma:M(I)\to B(H)\). The double-centralizer homomorphism is \(\mu:A\to M(I)\), \(a\mapsto(i\mapsto ai,\ i\mapsto ia)\). Their composition is \(\widetilde\sigma=\overline\sigma\circ\mu:A\to B(H)\); the solution proves boundedness, the adjoint and product identities, and uniqueness on the dense span \(\sigma(I)H\). Neither unitality nor separability is required. If \((\sigma,U)\) is covariant for \(I\), then (3.3), covariance on \(I\), and density of \(\sigma(I)H\) show that \((\widetilde\sigma,U)\) is covariant for \(A\). The extended coefficient map is nondegenerate because it contains \(\sigma(I)\).

In the other direction, a covariant representation of \(A\) restricts to a covariant representation of \(I\) on the essential space of \(I\), which is reducing for both parts of the pair. Its integrated \(I\)-functions vanish on the complementary subspace. These two observations show that the universal norms on \(C_c(G,I)\) agree. Therefore \(\iota\rtimes G\) is isometric.

Its closed image

\[
J=\overline{C_c(G,I)}^{\,A\rtimes G}
\]

is an ideal: convolution of an \(A\)-function with an \(I\)-function in either order remains \(I\)-valued. Invariance is used for the translated coefficient. Clearly \(J\subseteq\ker(q\rtimes G)\), and Proposition 3.1 makes \(q\rtimes G\) surjective.

Now let \(\tau\) be a faithful nondegenerate representation of \((A\rtimes G)/J\), pulled back to \(A\rtimes G\). Let \((\pi,U)\) be its covariant pair. For \(i\in I\),

\[
0=\tau(t\mapsto\varphi_V(t)i)=\pi(i)U(\varphi_V).
\]

The group approximate identity satisfies \(U(\varphi_V)\to1\) strongly, so \(\pi(i)=0\). Consequently \(\pi\) factors through a nondegenerate covariant coefficient representation of \(A/I\). Theorem 2.3 factors \(\tau\) through the surjection

\[
(A\rtimes G)/J\longrightarrow(A/I)\rtimes G.
\]

Faithfulness of \(\tau\) forces that surjection to be injective. Hence \(\ker(q\rtimes G)=J\), proving (3.2). \(\square\)

*Reference:* [Connes].

For example, if \(Y\) is a closed invariant subset of a locally compact \(G\)-space \(X\), use \(I=C_0(X\setminus Y)\) and \(A/I=C_0(Y)\) in (3.2). The quotient identification follows by restriction of functions, using extension on the one-point compactifications. For the dilation action \(\eta_a(f)(\xi)=f(\xi/a)\) of \(G=\mathbb R^\times\) on \(\mathbb R\), the fixed subset \(\{0\}\) gives the quotient crossed product \(\mathbb C\rtimes G=C^*(G)\). This is the exactness mechanism in *Phase transition in the Bost–Connes system*, Proposition 20.1 and equation (20.6). No condition on amenability is needed for full exactness.

## 4. When is there an identity?

**Theorem 4.1.** Suppose \(A\ne0\). Then \(A\rtimes_\alpha G\) is unital if and only if \(A\) is unital and \(G\) is discrete.

**Proof.** If \(G\) is discrete, let \(m=\mu(\{e\})>0\). If \(A\) is unital, the function supported at \(e\) with value \(m^{-1}1_A\) is an identity for (1.3), and remains one in the completion. For counting measure its value is \(1_A\).

For the converse use the regular representation (2.3), with \(\rho\) faithful and \(K\ne0\). Its integration \(T\) is nondegenerate, so a crossed-product identity would act as the identity on \(L^2(G,K)\).

Assume first that \(G\) is nondiscrete. Haar measure has \(\mu(\{e\})=0\): if its value were positive, every point would have that value, and a finite-measure compact neighborhood would contain only finitely many points, forcing the identity to be isolated. Regularity therefore gives relatively compact identity neighborhoods \(V\) with arbitrarily small positive measure. Keep all of them inside one relatively compact neighborhood \(W\) on which \(\Delta^{-1}\) is bounded by \(c\).

Fix \(\eta\in K\) of norm one and set \(\xi_V(r)=\mu(V)^{-1/2}1_V(r)\eta\). For \(f\in C_c(G,A)\), with compact support \(L\), (2.3) gives

\
\|[T(f)\xi_V\|
\leq\frac{\|f\|_\infty}{\sqrt{\mu(V)}}\mu(rV^{-1})
\leq c\|f\|_\infty\sqrt{\mu(V)}.
\]

This vector function is supported in \(LV\subset L\overline W\). Thus

\[
\|T(f)\xi_V\|_2
\leq c\|f\|_\infty\sqrt{\mu(L\overline W)}\sqrt{\mu(V)}\longrightarrow0.
\tag{4.1}
\]

The inversion formula justifies \(\mu(V^{-1})\leq c\mu(V)\), so this argument also covers nonunimodular groups. If the crossed product had an identity, choose \(f\) within \(1/2\) of it in full norm. Contractivity of \(T\) would give \(\|T(f)\xi_V\|_2>1/2\) for every \(V\), contradicting (4.1).

It follows that \(G\) is discrete. Compress \(T\) to the coordinate at \(e\), a copy of \(K\), using its normalized coordinate embedding. For a finitely supported function the compression is \(m\rho(f(e))\), where \(m=\mu(\{e\})\). By continuity, compression of every element of the crossed product belongs to the norm-closed algebra \(\rho(A)\). Compression of an identity is \(1_K\), so \(1_K\in\rho(A)\). Faithfulness of \(\rho\) implies that its preimage is an identity for \(A\). \(\square\)

If \(A=0\), the crossed product is zero for every \(G\). Whether one calls the zero algebra unital is a convention; it cannot be used to recover discreteness of \(G\). Also, when \(A\) is unital but \(G\) is nondiscrete, (2.5) gives \(j_G(C^*(G))\subset C\), although the individual \(i_G(s)\) still belong to its multipliers.

## 5. Examples controlled by the universal property

**Theorem 5.1 (trivial action).** For every \(A,G\),

\[
A\rtimes_{\mathrm{id}}G\cong A\otimes_{\max}C^*(G).
\tag{5.1}
\]

**Proof.** Covariance for the trivial action says that \(\pi(A)\) commutes with every \(U_s\). It therefore commutes with the integrated representation of \(C^*(G)\). Conversely, commuting nondegenerate representations of \(A\) and \(C^*(G)\) yield, by group recovery, a covariant pair for the trivial action: commutation with the recovered unitaries follows on the dense vectors generated by integrated group functions. The maximal tensor product is universal for precisely these commuting pairs by [Theorem 1.1 and its essential-subspace paragraph](../../OA-FOUND-REMAINDER/src/tensor-norms-and-independent-systems.md#1-recovering-the-two-actions) and [Propositions 2.1–2.2](../../OA-FOUND-REMAINDER/src/tensor-norms-and-independent-systems.md#2-two-norms-from-two-kinds-of-representation). Restricting a product representation to its essential subspace leaves its norm unchanged; the two recovered factor representations there are nondegenerate. Thus allowing degenerate pairs in the maximal norm does not enlarge the supremum used here. On the dense simple coefficient functions the correspondence is

\[
[t\mapsto\varphi(t)a]\longleftrightarrow a\otimes\varphi.
\]

Both universal norms are computed by the same pairs, so this correspondence is isometric. It respects products and adjoints for the trivial action. Its image is dense, and completion gives (5.1). \(\square\)

**Proposition 5.2 (finite groups).** If \(G\) is finite of order \(n\), its full crossed product embeds into \(M_n(A)\). For counting measure, the embedding sends \(f\) to

\[
R(f)_{r,t}=\alpha_{r^{-1}}(f(rt^{-1})),\qquad r,t\in G.
\tag{5.2}
\]

**Proof.** Matrix multiplication and (1.3) show that \(R\) is a *-homomorphism. For any covariant pair \((\pi,U)\), define the isometry

\[
V:H\longrightarrow\ell^2(G,H),\qquad
(V\xi)(r)=n^{-1/2}U_r^*\xi.
\]

The finite regular pair built from \(\pi\) has coefficient \(\pi(\alpha_{r^{-1}}(a))\) at \(r\) and left translation. Covariance gives \(\widetilde\pi(a)V=V\pi(a)\) and \(\lambda_sV=VU_s\). Consequently \(\|\pi\rtimes U(f)\|\leq\|R(f)\|\). With \(\pi\) faithful, the regular integrated matrix is the faithful amplification of \(R(f)\), giving the reverse inequality after taking the universal supremum. Thus \(\|f\|_u=\|R(f)\|\). Completion extends \(R\) isometrically into \(M_n(A)\). It is a subalgebra of that matrix algebra, not generally the whole matrix algebra. \(\square\)

Here the argument is only a finite-group computation. The general reduced crossed product and Fell absorption are treated in *Reduced crossed products and Fell’s absorption principle*.

**Example 5.3 (a homeomorphism).** Let \(X\) be nonempty compact Hausdorff and \(h:X\to X\) a homeomorphism. Set \(\alpha_k(a)=a\circ h^{-k}\). The crossed product is unital by Theorem 4.1. With \(u=i_{\mathbb Z}(1)\), its dense polynomials are \(\sum_k a_ku^k\), and

\[
(a u^k)(b u^l)=a(b\circ h^{-k})u^{k+l},
\qquad uau^*=a\circ h^{-1}.
\tag{5.3}
\]

A representation is exactly a unital representation of \(C(X)\) with a unitary satisfying this relation. For instance, on the orbit of \(x\in X\), the formulas

\
[\pi_x(a)\xi=a(h^m x)\xi(m),\qquad
U\xi=\xi(m-1)
\]

give covariance on \(\ell^2(\mathbb Z)\). For \(h(z)=\omega z\) on the circle and the coordinate unitary \(v(z)=z\), the relation is \(uvu^*=\overline\omega v\), equivalently \(vu=\omega uv\). This checks the sign fixed by (1.2).

**Theorem 5.4 (discrete translation).** Give a discrete group counting measure and let \(\alpha_t(a)(s)=a(t^{-1}s)\) on \(c_0(G)\). Then

\[
c_0(G)\rtimes_\alpha G\cong\mathcal K(\ell^2(G)).
\tag{5.4}
\]

**Proof.** Let \(p_s\) be the coefficient indicator of \(\{s\}\), and write \(u_t=i_G(t)\). The products \(p_su_t\) are crossed-product elements. Define

\[
e_{s,r}=p_su_{sr^{-1}}.
\]

Covariance says \(u_tp_ru_t^*=p_{tr}\). Therefore

\[
e_{s,r}e_{v,w}=\delta_{r,v}e_{s,w},\qquad
e_{s,r}^*=e_{r,s}.
\tag{5.5}
\]

Multiplication and left translation on \(\ell^2(G)\) form a covariant pair, and their integration sends \(e_{s,r}\) to the rank-one matrix unit \(E_{s,r}\). In particular none of the diagonal units is zero. For a finite subset \(F\subset G\), the span of \(e_{s,r}\), \(s,r\in F\), is thus a copy of \(M_{|F|}(\mathbb C)\). Its norm is the usual matrix norm, since the displayed map on this finite-dimensional C*-algebra is injective.

Every compactly supported group function has finitely many coefficients in \(c_0(G)\); approximating those coefficients by finitely supported ones proves that the union of these finite matrix spans is dense. The displayed integration is isometric on that union and its image is the finite matrix operators. Their norm closure is \(\mathcal K(\ell^2(G))\), also for uncountable \(G\). It therefore extends to (5.4). \(\square\)

Under (5.4), the group multipliers act by left translation. Thus \(j_G\) is the integrated left regular representation of \(C^*(G)\). For the free group on two generators, the strict full-versus-regular norm gap established in *Unitary representations and the two group C* completions*, section “A strict gap: the free group on two generators”, proves that this \(j_G\) is not injective. All distinct group elements still give distinct unitaries.

In particular, if \(\delta_s\) denotes the coefficient point mass and \(\delta_t\) the group point mass, then

\[
\delta_s\otimes\delta_t=p_su_t\longmapsto E_{s,t^{-1}s}.
\tag{5.6}
\]

For \(G=\mathbb Z/2\mathbb Z\), this proves \((\mathbb C\oplus\mathbb C)\rtimes_{\mathrm{flip}}G\cong M_2(\mathbb C)\): coefficient indicators give the diagonal projections, and their products with the flip give the off-diagonal matrix units.

For any locally compact Hausdorff \(G\), the corresponding statement is

\[
C_0(G)\rtimes_{\mathrm{lt}}G\cong\mathcal K(L^2(G)),
\tag{5.7}
\]

via multiplication and left translation. We state (5.7) with the precise reference [Blackadar, Operator Algebras]. Its nondiscrete case is proved later in *Induced algebras and Green’s imprimitivity theorem*, using the subgroup \(\{e\}\). The discrete matrix-unit proof above is not a proof of that case.

**Proposition 5.5 (semidirect products).** Let \(N,H\) be locally compact Hausdorff groups and \(\theta\) a jointly continuous action of \(H\) by automorphisms of \(N\). If \(\beta_h\) is the induced action on \(C^*(N)\), characterized on canonical group multipliers by \(\beta_h(v_n)=v_{\theta_h(n)}\), then

\[
C^*(N\rtimes_\theta H)\cong C^*(N)\rtimes_\beta H.
\tag{5.8}
\]

**Proof.** The induced action is point-norm continuous. Indeed, if \(\mu_N(\theta_h E)=c(h)\mu_N(E)\), transport on compactly supported functions is \(f(n)\mapsto c(h)^{-1}f(\theta_{h^{-1}}(n))\). The modulus \(c\) is continuous, as follows by integrating a fixed nonzero nonnegative test function. Common compact supports near the identity give \(L^1\) continuity, hence full-norm continuity, and density extends it to \(C^*(N)\).

A unitary representation \(W\) of \(N\rtimes H\) restricts to representations \(V_n=W(n,e)\), \(U_h=W(e,h)\) with \(U_hV_nU_h^*=V_{\theta_h(n)}\). Integrate \(V\) to a representation of \(C^*(N)\); this is a covariant pair for \(\beta\). Conversely a covariant pair gives the strongly continuous representation \(W(n,h)=V_nU_h\), since

\[
(n,h)(m,k)=(n\theta_h(m),hk).
\]

The two operations are inverse. To check that the universal maps have values in the algebras themselves, rather than just in their multipliers, use left Haar measure \(c(h)^{-1}\,dn\,dh\) on \(N\rtimes H\). Left translation preserves this measure: the change \(n\mapsto n_0\theta_{h_0}(n)\) multiplies \(dn\) by \(c(h_0)\), which cancels the change in \(c(h)^{-1}\). A product of integrated \(N\)- and \(H\)-functions corresponds to the group function \(c(h)f(n)g(h)\). These functions have dense span in \(L^1(N\rtimes H)\), by compact-support tensor approximation and multiplication by the positive continuous factor \(c\). On the crossed-product side their images are exactly \(i_{C^*(N)}(f)j_H(g)\), whose span is dense by Proposition 2.2 and density of \(C_c(N)\) in \(C^*(N)\). The group universal property and Theorem 2.3 therefore give homomorphisms between the two algebras themselves. Their multiplier extensions preserve the canonical \(N\) and \(H\) unitaries, so the two composites are identities by integration and density. This proves (5.8). \(\square\)

*Reference:* [Blackadar, K-Theory].

## 6. Exercises with complete solutions

**Exercise 6.1 (basic).** Give a discrete group counting measure. Prove associativity directly on elementary terms \(a\delta_s\), then on all finitely supported functions.

**Solution.** Formula (1.3) gives \((a\delta_s)*(b\delta_t)=a\alpha_s(b)\delta_{st}\). The left-associated product with \(c\delta_r\) has coefficient \(a\alpha_s(b)\alpha_{st}(c)\). The right-associated product has coefficient \(a\alpha_s(b\alpha_t(c))\), which is the same because \(\alpha_s\) is multiplicative and \(\alpha_s\alpha_t=\alpha_{st}\). Both terms are supported at \(str\). Bilinearity and finite expansion prove the general assertion.

**Exercise 6.2 (basic).** Compute the flip crossed product of \(\mathbb C\oplus\mathbb C\) by \(\mathbb Z/2\mathbb Z\). Exhibit four matrix units and prove injectivity of the resulting map.

**Solution.** Write \(p,q\) for the two coefficient projections and \(w\) for the flip unitary. Then \(wpw=q\), \(wqw=p\), and \(w^2=1\). Set \(e_{11}=p\), \(e_{22}=q\), \(e_{12}=pw\), \(e_{21}=qw\). Covariance and \(pq=0\) give \(e_{ij}e_{kl}=\delta_{jk}e_{il}\) and \(e_{ij}^*=e_{ji}\). Represent \(p,q\) as the two coordinate projections on \(\mathbb C^2\), and \(w\) as their interchange. The four images are the usual matrix units, so they are linearly independent. Their span is a finite-dimensional closed algebra and contains every dense polynomial \(a+bw\). It is the entire crossed product, and the representation is an isomorphism onto \(M_2(\mathbb C)\).

**Exercise 6.3 (intermediate).** Prove (3.2) using covariant representations. Explain separately why the ideal map is injective and why the quotient kernel is its image.

**Solution.** Extend a nondegenerate \(I\)-representation by (3.3). On vectors \(\sigma(i)\xi\), conjugating the extension by \(U_s\) gives multiplication by \(\alpha_s(a)\); thus covariance extends. Conversely restrict an \(A\)-pair to the reducing essential space of \(I\). Suprema over these pairs show equality of the two norms on \(C_c(G,I)\), so its completed inclusion is injective. Its image \(J\) is an ideal by convolution. The quotient map is onto because simple coefficient functions lift. Finally, if an integrated \(A\)-pair annihilates \(J\), then \(\pi(i)U(\varphi_V)=0\), so \(\pi(I)=0\) by the group approximate identity. It factors through \(A/I\). Apply this to a faithful representation of \((A\rtimes G)/J\): it proves that the induced surjection to \((A/I)\rtimes G\) has zero kernel. These steps establish all three exactness assertions.

**Exercise 6.4 (intermediate).** Assume \(A\ne0\). Prove the unitality criterion, and identify the role of this assumption.

**Solution.** For discrete \(G\) and unital \(A\), \(\mu(\{e\})^{-1}1_A\delta_e\) is an identity; with counting measure this is \(1_A\delta_e\). Conversely, in the faithful-coefficient regular representation, a crossed-product identity acts as the identity. If \(G\) were nondiscrete, the normalized vectors \(\xi_V\) in Theorem 4.1 would satisfy \(\|T(f)\xi_V\|\to0\) for every fixed compactly supported \(f\). Choosing \(f\) within \(1/2\) of the putative identity contradicts this. Thus \(G\) is discrete. Compression to its identity coordinate belongs to \(\rho(A)\) by density and closedness and takes the identity to \(1_K\). Its preimage under faithful \(\rho\) is an identity for \(A\). The hypothesis \(A\ne0\) ensures \(K\ne0\) and hence the existence of the unit test vectors. For zero coefficients the crossed product is zero regardless of the group.

**Exercise 6.5 (advanced).** Prove (5.4) for an arbitrary discrete group and calculate the image of \(\delta_s\otimes\delta_t\). Include the injectivity argument.

**Solution.** Multiplication by \(c_0(G)\) and left translation on \(\ell^2(G)\) satisfy covariance. The element \(p_su_t\) takes the basis vector at \(r\) to the basis vector at \(s\) exactly when \(tr=s\). Its image is therefore \(E_{s,t^{-1}s}\). Reindex by \(e_{s,r}=p_su_{sr^{-1}}\). Covariance gives the matrix-unit identities (5.5). For each finite \(F\), their span is a copy of \(M_{|F|}\) and the displayed representation is faithful on it, hence isometric. The union of these spans is dense by finite-support approximation in every coefficient. The representation is consequently isometric on a dense subalgebra and then on its completion. Its image is the closure of the finite matrix operators, which is exactly the compact operators. This proves surjectivity and injectivity, including when \(G\) is uncountable.

## What this lesson does not prove

The general analysis used here includes Bochner integration and absolutely integrable Fubini, with the support hypotheses proved in [Lemma 0.1 of the GNS reading](../prerequisites/src/exact/foundations-of-von-neumann-algebras/DD4372862B2D/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#lemma-0-1). The locally compact cutoff and finite-partition proofs are in [Section H0 of the compact-topology reading](../prerequisites/src/OA-FLOW/repaired-20261004/compact-topology-and-hilbert-tensors.md#h0-cutoffs-compact-partitions-and-product-approximation). The exact C*-algebra inputs are [Theorem 4.2 (contractivity)](../prerequisites/src/exact/foundations-of-von-neumann-algebras/50F1FFA37C83/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#theorem-4-2), [Corollary 4.6 (faithful isometry)](../prerequisites/src/exact/foundations-of-von-neumann-algebras/50F1FFA37C83/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#corollary-4-6), [Corollary 15.4 (closed range)](../prerequisites/src/exact/foundations-of-von-neumann-algebras/50F1FFA37C83/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#corollary-15-4), [Theorem 11.4 (positive contractive approximate identities)](../prerequisites/src/exact/foundations-of-von-neumann-algebras/50F1FFA37C83/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#theorem-11-4). A faithful nondegenerate representation is obtained from [Theorem 7.2 (faithful representations)](../prerequisites/src/exact/foundations-of-von-neumann-algebras/DD4372862B2D/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#theorem-7-2) and [Proposition 1.4 (restriction to the nondegenerate part)](../prerequisites/src/exact/foundations-of-von-neumann-algebras/DD4372862B2D/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#proposition-1-4). The extension of a nondegenerate ideal representation in (3.3) is the closed-ideal conclusion of [Exercise 5 in Section 7 of the multiplier reading](../prerequisites/src/hilbert-c-star-modules-and-morita-equivalence/compact-operators-multipliers-and-the-strict-topology.md#7-exercises-and-complete-solutions), with its full solution. [Blackadar, Operator Algebras] is further reading for these constructions.

The Haar prerequisites are existence, regularity and full support of left Haar measure, the modular and inversion formulas, translation continuity, and integral-one compactly supported approximate identities. Precise locators in *Haar measure on locally compact groups* are Proposition 2.3, Theorem 5.1 for the compact-support Fubini calculations, Theorem 8.3, §9, Theorems 10.1 and 11.1, and §§14–15. Our integrable functions are obtained by completion from compactly supported functions; no Fubini claim for arbitrary Borel functions on an unrestricted non-sigma-finite product is needed. A further reference is [Blackadar, Operator Algebras].

The group representation correspondence, group approximate identity in a nondegenerate representation, and full group C*-algebra are used from *Unitary representations and the two group C* completions*, sections “Integrating a continuous unitary representation”, “Recovering a group action”, and “Full and reduced group completions”. Its section “A strict gap: the free group on two generators” supplies the free-group example mentioned after (5.4). For coefficients we use the exact correspondence, the regular pair (2.3), its faithfulness on \(L^1(G,A)\), and the full completion from *Covariance and crossed products with nonunital coefficients*, sections “Integrating a nondegenerate covariant pair”, “Recovering the two actions on an actual vector domain”, “The regular pair and its two faithfulness assertions”, and “Full and reduced crossed products and their canonical actions”. Faithfulness on the convolution algebra does not assert faithfulness on its full completion.

The multiplier idealizer, strict topology, strict extension of nondegenerate homomorphisms, and \(\mathcal L(E)=M(\mathcal K(E))\) are assumed under the preparatory topic *Compact operators, multipliers and the strict topology*; the source statements used here are [Blackadar, Operator Algebras]. Strict continuity of the extension on bounded sets follows by testing on the dense products \(\pi(a)b\): strict convergence \(m_\lambda\to m\) makes \(\pi((m_\lambda-m)a)b\to0\), and uniform boundedness extends this to every \(b\); the right products follow by taking adjoints. For the maximal tensor product's commuting-representation characterization, [Theorem 1.1](../../OA-FOUND-REMAINDER/src/tensor-norms-and-independent-systems.md#1-recovering-the-two-actions) proves nonunital recovery of both commuting actions, and [Propositions 2.1–2.2](../../OA-FOUND-REMAINDER/src/tensor-norms-and-independent-systems.md#2-two-norms-from-two-kinds-of-representation) prove the maximal norm and its universal property. These arguments require neither units nor separability; the essential-subspace paragraph includes degenerate representations. Blackadar, II.9.2.1–II.9.2.3, remains further reading.

Finally, (5.7) for nondiscrete groups is stated from [Blackadar, Operator Algebras]. Its proof by Green's theorem is deferred to *Induced algebras and Green’s imprimitivity theorem*. General reduced-crossed-product arguments, amenability comparisons, expectations, simplicity, and duality belong to later lessons.

## References

- **[Schulz-Baldes–Stoiber]** H. Schulz-Baldes and T. Stoiber, *Harmonic Analysis in Operator Algebras and its Applications to Index Theory and Topological Solid State Systems*, Springer, 2022, §1.1. [Author manuscript](https://arxiv.org/abs/2206.07781).
- **[Connes]** A. Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter II, Appendix C, Definition 1 and Proposition 2. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
- **[Blackadar, Operator Algebras]** B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006; author's revised edition, 2017. [Author's revised edition, 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).
- **[Blackadar, K-Theory]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998, §10.1. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Rosenberg]** J. Rosenberg, “Examples and applications of noncommutative geometry and K-theory”, in G. Cortiñas, ed., *Topics in Noncommutative Geometry*, Clay Mathematics Proceedings 16, AMS and Clay Mathematics Institute, 2012, §2.2. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).
