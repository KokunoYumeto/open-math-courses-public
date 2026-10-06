# Averaging, crossed products, and injectivity

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

An invariant mean turns the orbit of an operator into a completely positive average. We will use that average to preserve injectivity under fixed points and crossed products by amenable groups. We will then prove that a spatial tensor bound for a regular crossed product gives the same bound for its coefficient algebra. Applied to the continuous core, these results complete the implication from injectivity to semidiscreteness.

Prerequisites are [Finite models of a von Neumann algebra](semidiscrete-finite-models.md) and [Hypertraces and finite injective algebras](hypertraces-finite-injectivity.md). We use precisely a standard representation \((M,H_0,J)\) with \(JMJ=M'\), in which every normal positive functional is a vector functional, from [The positive cone of a standard representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#standard-form-natural-cone). The comparison with other normal representations is proved below. Section 3 verifies the regular representation and its independence from the coefficient representation. Section 4 constructs a faithful normal semifinite weight and proves that its modular crossed product carries a faithful normal semifinite trace. The modular inputs are Tomita–Takesaki theory for weights, the dual-weight construction, and the centralizer identities for bounded densities, including their bounded invertible perturbation formula. The unbounded trace is obtained from bounded spectral corners. Exact source locators are given below; the broader flow construction is developed in [Crossed products and the flow of weights](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#crossed-products-and-the-flow-of-weights).

The regular model and the precise way we use the core theorem are explained below. No factor, countability, separable predual, or faithful normal state assumption is imposed. The zero algebra is handled trivially. Hilbert-space inner products are linear in the second variable. The retraction and commutant arguments use Arveson's completely positive methods and Haagerup's standard form, with locators in the references. The continuous-core argument uses the exact modular and crossed-product prerequisites stated here. The commutant and averaging constructions are also developed for general algebras in [Injective von Neumann algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#injective-von-neumann-algebras).

### Normal representations inside standard amplifications

Let \(M\) act in standard form on \(H_0\), and let \(\pi:M\to B(K)\) be any normal unital representation. Choose a maximal orthogonal family of nonzero reducing cyclic subspaces \(K_\alpha\subseteq K\). Such a family exists by Zorn's lemma. Its sum is \(K\): otherwise its reducing orthogonal complement contains a unit vector \(\eta\), and \(\overline{\pi(M)\eta}\) supplies another reducing cyclic subspace. Write \(\eta_\alpha\) for a cyclic unit vector in each \(K_\alpha\).

The state \(f_\alpha(x)=\langle\eta_\alpha,\pi(x)\eta_\alpha\rangle\) is normal. The standard-form vector theorem supplies \(\xi_\alpha\in H_0\) with \(f_\alpha(x)=\langle\xi_\alpha,x\xi_\alpha\rangle\). The rule
\[
U_\alpha(\pi(x)\eta_\alpha)=x\xi_\alpha
\]
is well defined and isometric: both squared norms are \(f_\alpha(x^*x)\), and polarization gives all inner products. It extends onto \(L_\alpha=\overline{M\xi_\alpha}\) and intertwines the representations. The projection \(p_\alpha\) onto this reducing subspace belongs to \(M_0'\).

Taking their direct sum identifies \(K\) unitarily with
\[
P(H_0\otimes\ell^2(I)),\qquad
P=\bigoplus_{\alpha\in I}p_\alpha\in M_0'\bar\otimes B(\ell^2(I)),
\]
and identifies \(\pi(x)\) with the restriction of \(x\otimes1\) to that space. This covers arbitrary Hilbert dimension; the zero representation space is immediate. The commutant of the restricted algebra is exactly
\[
P\bigl(M_0'\bar\otimes B(\ell^2(I))\bigr)P.
\]
Indeed, each operator in this corner commutes with the restriction. Conversely, extend an operator in the restricted commutant by zero on \((1-P)(H_0\otimes\ell^2(I))\). Since \(P\) commutes with every \(x\otimes1\), that extension commutes with the amplification and hence belongs to the displayed commutant corner. This representation comparison uses only the standard-form vector theorem, without a cyclic or separating vector assumption on \(K\).

The starting faithful normal representation can also be arbitrary. Identify it with \(M\subset B(H_1)\). A normal positive functional \(f\) on \(M\) is continuous for the induced ultraweak topology. The continuous linear Hahn–Banach theorem extends it to an ultraweakly continuous linear functional on \(B(H_1)\), so
\[
f(x)=\operatorname{Tr}(sx)\qquad(x\in M)
\]
for a trace-class operator \(s\). Replacing \(s\) by \((s+s^*)/2\) retains this equality, because \(f\) is hermitian. We do not require that this extension be positive. The positive part \(s_+\) gives a normal positive functional \(g(x)=\operatorname{Tr}(s_+x)\) satisfying \(f\leq g\) on \(M_+\).

The positive trace-class spectral decomposition is a finite or countable sum
\(s_+=\sum_j\lambda_j|e_j\rangle\langle e_j|\), with \(\sum_j\lambda_j<\infty\). Thus \(g\) is the vector functional of \(\zeta=\sum_j\sqrt{\lambda_j}\,e_j\otimes\delta_j\) in \(H_1\otimes\ell^2(\mathbb N)\), for the amplified action \(\rho(x)=x\otimes1\). On \(L=\overline{\rho(M)\zeta}\), the form
\[
\langle\rho(a)\zeta,z\rho(b)\zeta\rangle=f(a^*b)
\]
is well defined and bounded by domination and Cauchy–Schwarz. It determines \(0\leq z\leq1_L\). Replacing \(a\) by \(c^*a\) in this equality shows \(z\rho(c)=\rho(c)z\) on \(L\). Extend \(z\) by zero off this reducing subspace. Then \(z\) belongs to the amplified commutant, and
\[
f(x)=\langle z^{1/2}\zeta,\rho(x)z^{1/2}\zeta\rangle.
\]
Apply this construction to the normal cyclic states \(f_\alpha\) above. The same isometric intertwining maps embed each cyclic summand into \(H_1\otimes\ell^2(\mathbb N)\); their direct sum embeds the whole representation into \(H_1\otimes\ell^2(\mathbb N\times I)\). The reducing projection and the commutant corner are obtained exactly as before. This proves the comparison between any two faithful normal representations using the trace-class predual and the explicitly constructed dominated form.

## 1. Amplifications and commutants

**Proposition 1.1.** If \(M\) is injective and \(K\) is any nonzero Hilbert space, then \(M\bar\otimes B(K)\) is injective. Conversely, injectivity of this amplification implies injectivity of \(M\).

**Proof.** Represent \(M\subseteq B(H)\) faithfully and normally, and take a ucp retraction \(E:B(H)\to M\). Choose an arbitrary orthonormal basis \((e_j)_{j\in I}\) of \(K\), and set \(V_j\xi=\xi\otimes e_j\). For \(x\in B(H\otimes K)\), write \(x_{ij}=V_i^*xV_j\).

For each finite \(F\subseteq I\), the finite matrix \([E(x_{ij})]_{i,j\in F}\) has norm at most \(\|x\|\), by complete contractivity of \(E\). Regard it as an operator \(y_F\) supported on \(H\otimes\operatorname{span}\{e_j:j\in F\}\). On vectors with finitely many coordinates, all coefficients of \(y_F\) stabilize once \(F\) contains those coordinates. The uniform norm bound therefore gives a unique bounded operator \(\widetilde E(x)\) with
\[
V_i^*\widetilde E(x)V_j=E(x_{ij}),\qquad
\|\widetilde E(x)\|\leq\|x\|.
\]
Every entry lies in \(M\); equivalently \(\widetilde E(x)\) commutes with \(M'\otimes1\). Thus it belongs to \(M\bar\otimes B(K)=(M'\otimes1)'\). Linearity follows from entries. It is unital, and complete positivity follows by the same finite-coordinate construction for positive matrices over \(B(H\otimes K)\). On the amplification it is the identity, since every entry already belongs to \(M\). It is therefore a ucp retraction, proving injectivity.

For the converse, compress by \(1\otimes p\), with \(p\) rank one. This corner is isomorphic to \(M\), and corners of injective algebras are injective. \(\square\)

This construction does not assume that \(E\) is normal. Each finite matrix is evaluated before the bounded operator with all those entries is constructed.

Here is the corner retraction used in the converse and below. If \(p\in M\) is a nonzero projection, view \(B(pH)\) inside \(B(H)\) by extending each operator by zero. Then
\[
E_p:B(pH)\longrightarrow pMp,\qquad E_p(x)=pE(x)p
\]
is completely positive, has \(E_p(p)=p\), and fixes every element of \(pMp\). It is a ucp retraction for the corner's unit \(p\); the retraction criterion proves injectivity of \(pMp\). For \(p=0\), the corner is the zero algebra. This construction also works for central summands and makes no normality claim about the retraction.

**Lemma 1.2.** A von Neumann algebra is injective if and only if its opposite algebra is injective.

**Proof.** The map
\[
M_n(C^{\mathrm{op}})\longrightarrow M_n(C)^{\mathrm{op}},
\qquad [c_{ij}]\longmapsto[c_{ji}]
\]
is a \*-isomorphism, so it preserves positive elements. Entrywise application of a linear map commutes with this transposition. A map between C\*-algebras, or from an operator system inside one, is therefore completely positive exactly when the corresponding map between the opposite systems is completely positive. Opposite systems have the same unit and Banach norm. Apply the extension property into \(M\) to an inclusion of opposite systems, then take opposites again. This proves injectivity of \(M^{\mathrm{op}}\); applying the same argument twice proves the converse. \(\square\)

**Theorem 1.3.** In every faithful normal concrete representation, \(M\) is injective if and only if its commutant \(M'\) is injective.

**Proof.** First use a standard representation \((M,H_0,J)\). The map \(x\mapsto Jx^*J\) is a linear \*-anti-isomorphism of \(M\) onto its commutant. Lemma 1.2 makes that commutant injective.

For another faithful normal representation, the comparison just proved realizes it as a commutant restriction of an amplification of the standard representation. Its commutant is consequently a corner of
\[
M_0'\bar\otimes B(K).
\]
This is injective by Proposition 1.1, and so is its corner. Thus injectivity passes from \(M\) to its commutant in the prescribed representation. Applying this implication to \(M'\) and using \(M''=M\) proves the reverse implication. \(\square\)

Products of injective algebras are injective as well. To see this, represent them on \(\bigoplus_\alpha H_\alpha\), compress an operator to each \(H_\alpha\), apply the corresponding ucp retraction, and assemble the bounded diagonal operator. At every matrix size positivity is checked coordinatewise. Each coordinate algebra is conversely an injective corner of the product.

## 2. Averaging with an invariant mean

For a locally compact Hausdorff group \(G\), write \(C_b(G)\) for the bounded continuous functions. We use **amenability** in its invariant-mean form: there is a positive functional \(m\) on \(C_b(G)\) with \(m(1)=1\) and
\[
m(g\mapsto f(hg))=m(f)\qquad(h\in G).
\]
For a locally compact amenable group this mean is obtained by restricting a left-invariant mean on \(L^\infty(G)\). Haar measure is positive on nonempty open sets, so continuous functions embed faithfully in that space.

**Example 2.1.** The real line is amenable. Define
\[
m_R(f)=\frac1{2R}\int_{-R}^R f(t)\,dt.
\]
These are states on \(C_b(\mathbb R)\). A weak* cluster point as \(R\to\infty\) is translation invariant, since for each fixed \(s\),
\[
|m_R(f(s+\cdot))-m_R(f)|
\leq\frac{|s|}{R}\|f\|_\infty
\]
once \(R>|s|\). State-space compactness supplies the cluster point.

Let \(\alpha:G\to\operatorname{Aut}(M)\) be pointwise ultraweakly continuous, with each automorphism normal. The fixed algebra is
\(M^\alpha=\{x:\alpha_g(x)=x\text{ for every }g\}\).

**Theorem 2.2.** An invariant mean gives a ucp retraction \(P:M\to M^\alpha\). In particular, if \(M\) is injective and \(G\) amenable, then \(M^\alpha\) is injective.

**Proof.** For \(x\in M\), define a bounded functional on \(M_*\) by
\[
\omega(P(x))=m\bigl(g\mapsto\omega(\alpha_g(x))\bigr).
\]
The orbit coefficient is continuous and bounded by \(\|\omega\|\|x\|\). Since \(M=(M_*)^*\), the formula defines a unique \(P(x)\in M\), with \(\|P(x)\|\leq\|x\|\). It is linear and unital.

If \([x_{ij}]\geq0\), each \([\alpha_g(x_{ij})]\) is positive. For every normal positive functional \(\Omega\) on \(M_n(M)\), finite entry expansion gives
\[
\Omega([P(x_{ij})])
=m\bigl(g\mapsto\Omega([\alpha_g(x_{ij})])\bigr)\geq0.
\]
Normal positive functionals detect the positive cone, so \(P\) is completely positive.

Normality of \(\alpha_h\) allows testing \(\alpha_h(P(x))\) with its preadjoint. The action law and left invariance give
\[
\omega(\alpha_h(P(x)))
=m\bigl(g\mapsto\omega(\alpha_{hg}(x))\bigr)
=\omega(P(x)).
\]
Thus \(P(x)\in M^\alpha\). For a fixed element the coefficient functions are constant, so \(P(x)=x\). Composing \(P\) with a ucp retraction \(B(H)\to M\) proves injectivity of \(M^\alpha\). \(\square\)

The average need not be normal. For the shift action of \(\mathbb Z\) on \(\ell^\infty(\mathbb Z)\), every invariant mean kills finite-support projections but takes value one on the unit. Finite-support projections increase to one; this average does not preserve their supremum.

**Theorem 2.3.** Suppose \(N\subseteq B(H)\) is injective and \(u:G\to\mathcal U(H)\) is strongly continuous, with \(u_gNu_g^*=N\). If \(G\) is amenable, the von Neumann algebra \(Q=\{N,u(G)\}''\) is injective.

**Proof.** The commutant is \(Q'=N'\cap u(G)'\). By Theorem 1.3, \(N'\) is injective. Conjugation by \(u_g\) defines a normal, point-ultraweakly continuous action on \(N'\): vector coefficients are continuous by strong continuity of \(u\), and the normal-functional expansion into summable vector coefficients extends this to every normal coefficient. Its fixed algebra is exactly \(Q'\). Theorem 2.2 makes \(Q'\) injective, and Theorem 1.3 makes \(Q\) injective. \(\square\)

## 3. The regular crossed product

Represent \(M\subseteq B(H)\) faithfully and normally. With left Haar measure on \(G\), the regular model acts on
\(\mathcal H=H\otimes L^2(G)\cong L^2(G,H)\) by
\[
(\pi(x)\xi)(t)=\alpha_{t^{-1}}(x)\xi(t),
\qquad (\lambda_s\xi)(t)=\xi(s^{-1}t).
\]
These formulas define the regular representation; we verify that \(\pi\) is faithful and normal, \(\lambda\) is strongly continuous and unitary, and
\[
\lambda_s\pi(x)\lambda_s^*=\pi(\alpha_s(x)).
\]
It defines \(M\rtimes_\alpha G=\{\pi(M),\lambda(G)\}''\), independently up to normal isomorphism of the chosen faithful normal unital coefficient representation. These statements retain arbitrary Hilbert spaces and arbitrary locally compact groups. The measure is left Haar; the displayed left translations need no modular-function factor.

For completeness, point-ultraweak continuity of the action gives the vector continuity needed below. For \(t\to e\), \(x\in M\), and \(f\in M_*^+\),
\[
\begin{aligned}
f((\alpha_t(x)-x)^*(\alpha_t(x)-x))
&=f(\alpha_t(x^*x))-2\operatorname{Re}f(x^*\alpha_t(x))+f(x^*x)\\
&\longrightarrow0.
\end{aligned}
\]
Apply the same argument to \(x^*\). Thus the action is pointwise sigma-strong* continuous, and hence strongly continuous on every fixed vector in a normal concrete representation. Translation of the parameter gives continuity at every group element.

### Verifying the regular representation

This argument is an instructional expansion of the canonical OA-FLOW statements [OA-FLOW.REG.CONSTRUCTION](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#15-regular-model-independence), [OA-FLOW.REG.NORMALITY](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#15-regular-model-independence), and [OA-FLOW.REG.INDEPENDENCE](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#15-regular-model-independence). The theorems themselves belong to the course *Crossed products and the flow of weights* (OA-FLOW). We spell out the needed construction and comparison here to apply them to averaging and semidiscreteness transfer.

For fixed \(x\) and \(\xi\in H\), the field \(t\mapsto\alpha_{t^{-1}}(x)\xi\) is norm continuous and bounded by \(\|x\|\|\xi\|\). It therefore defines multiplication on elementary sections \(f(t)\xi\), \(f\in C_c(G)\), and extends to \(L^2(G,H)\) with norm at most \(\|x\|\). Multiplication and adjoints hold pointwise, giving a unital *-representation. If \(x\ne0\), choose \(\xi\) with \(x\xi\ne0\). Continuity makes \(\|\alpha_{t^{-1}}(x)\xi\|\) positive on an identity neighborhood; a nonzero \(f\in C_c(G)\) supported there shows \(\pi(x)\ne0\). This proves faithfulness.

To check normality, let \(0\le x_i\uparrow x\) be a bounded increasing net. For each \(\xi\), the continuous functions
\[
d_i(t)=\langle\xi,\alpha_{t^{-1}}(x-x_i)\xi\rangle
\]
decrease pointwise to zero. On a compact set they decrease uniformly: for a positive tolerance, the open sets where \(d_i\) is below that tolerance cover the compact set, and finitely many of them have a common later index. Thus
\[
\langle f\xi,\pi(x-x_i)f\xi\rangle\longrightarrow0
\qquad(f\in C_c(G)).
\]
For finite sums of elementary sections, positivity and Cauchy–Schwarz bound cross terms by the corresponding diagonal terms. Density and the common operator bound give the same limit on every vector. Hence \(\pi(x_i)\uparrow\pi(x)\), proving normality for arbitrary nets.

Left invariance of Haar measure proves that \(\lambda_s\) is unitary. Translation is norm continuous on \(C_c(G)\): near a fixed \(s\), the translated supports lie in one compact set, and the functions converge uniformly there. Density gives strong continuity on \(L^2(G)\), then on \(H\otimes L^2(G)\). Direct substitution gives the displayed covariance formula.

Finally take two faithful normal coefficient representations. The representation comparison proved above realizes the second on \(P(H\otimes K)\), with \(P\in M'\,\bar\otimes\,B(K)\). This projection has central support one in that commutant amplification: a nonzero central complement would give a nonzero central element of \(M\) killed by the second representation, contradicting faithfulness. The constant copy of \(M'\,\bar\otimes\,B(K)\) commutes with the amplified regular algebra, since it commutes with every coefficient field and acts independently of the group coordinate. Thus \(P\) also has central support one in the regular commutant. Compression to \(P(H\otimes K)\otimes L^2(G)\) is consequently faithful and normal on the amplified regular algebra. Under the intertwining unitary its generators are exactly the second regular generators. Their generated algebra is therefore normally isomorphic to the first. This proves representation independence for arbitrary \(H,K,G\).

**Corollary 3.1.** If \(M\) is injective and \(G\) amenable, then \(M\rtimes_\alpha G\) is injective.

**Proof.** The faithful normal coefficient copy \(\pi(M)\) is injective. The unitaries \(\lambda_s\) normalize it and are strongly continuous. Apply Theorem 2.3. \(\square\)

**Theorem 3.2.** If \(M\rtimes_\alpha G\) is semidiscrete, then \(M\) is semidiscrete. Amenability of \(G\) is not needed for this implication.

**Proof.** Put \(Q=M\rtimes_\alpha G\) in the regular representation. The constant embedding
\[
\iota:M'\longrightarrow Q',\qquad
(\iota(y)\xi)(t)=y\xi(t)
\]
is a faithful normal representation: it commutes with all coefficient fields because \(\alpha_{t^{-1}}(x)\in M\), and with all left translations because it is constant in \(t\).

Semidiscreteness of \(Q\) gives its commutant tensor estimate in this faithful normal representation. Minimal tensor products preserve faithful inclusions. Thus, for \(x_i\in M\), \(y_i\in M'\),
\[
\left\|\sum_i\pi(x_i)\iota(y_i)\right\|
\leq\left\|\sum_i\pi(x_i)\otimes\iota(y_i)\right\|_{\min}
=\left\|\sum_i x_i\otimes y_i\right\|_{\min}=C.
\]
For \(\xi\in H\) and \(f\in C_c(G)\), apply this bound to the elementary section \(t\mapsto f(t)\xi\). It gives
\[
\int_G |f(t)|^2
\left\|\sum_i\alpha_{t^{-1}}(x_i)y_i\xi\right\|^2\,dt
\leq C^2\|\xi\|^2\|f\|_2^2.
\]
The squared vector norm in the integrand is continuous in \(t\). If its value at the identity exceeded \(C^2\|\xi\|^2\), it would exceed that bound on an open identity neighborhood. A nonzero compactly supported continuous \(f\) inside that neighborhood has positive \(L^2\) norm and would contradict the integral estimate. Consequently
\[
\left\|\sum_i x_iy_i\xi\right\|\leq C\|\xi\|,
\qquad
\left\|\sum_i x_iy_i\right\|
\leq\left\|\sum_i x_i\otimes y_i\right\|_{\min}.
\]
The commutant criterion for \(M\) proves semidiscreteness. \(\square\)

A single identity point can have Haar measure zero. Continuity and a whole open neighborhood are what make the last argument valid.

## 4. The continuous core completes the converse

### Constructing a weight without countability

This is an instructional expansion of the canonical weight-existence theorem [OA-MOD-WH-13](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#weight-hilbert-algebra). OA-MOD owns that theorem; its arbitrary-cardinality statement is the input used here.

Choose a maximal family of nonzero normal states \((\omega_\alpha)\) whose support projections \(p_\alpha\) are orthogonal. If their sum were less than one, a nonzero normal positive functional supported on the complementary projection, normalized to a state, would enlarge the family. Thus \(\sum_\alpha p_\alpha=1\). Define
\[
\varphi(x)=\sum_\alpha\omega_\alpha(x)
=\sup_{F\ \mathrm{finite}}\sum_{\alpha\in F}\omega_\alpha(x),
\qquad x\in M_+.
\]
The sum is a weight. It is normal, since the supremum over finite \(F\) commutes with the supremum over any increasing positive net. If \(\varphi(x)=0\), then \(x^{1/2}p_\alpha=0\) for every \(\alpha\), by faithfulness of \(\omega_\alpha\) on its support. The sum of the supports is one, so \(x=0\). For \(p_F=\sum_{\alpha\in F}p_\alpha\),
\[
\varphi((yp_F)^*yp_F)\le |F|\,\|y\|^2<\infty
\qquad(y\in M).
\]
Since \(yp_F\to y\) strongly, the finite left ideal of \(\varphi\) is strongly dense. This proves semifiniteness. The family can be uncountable; no faithful normal state on \(M\) is required.

### Removing the modular density by bounded corners

The generator calculation expands [OA-FLOW.CORE.INNER](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#04-core-and-flow); the bounded-density argument expands the trace-existence conclusion of [OA-FLOW.CORE.TRACE](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#04-core-and-flow). These are instructional proofs of the selected canonical OA-FLOW statements. The derivative characterization and the rest of the flow construction remain in OA-FLOW. This lesson owns their application to the injectivity–semidiscreteness converse.

Let \(\varphi\) be any faithful normal semifinite weight, and put
\[
C=C_\varphi(M)=M\rtimes_{\sigma^\varphi}\mathbb R.
\]
The dual-weight construction gives a faithful normal semifinite weight \(\Phi=\widetilde\varphi\) on \(C\). Its generator formulas are
\[
\sigma_t^\Phi(\pi(x))=\pi(\sigma_t^\varphi(x)),\qquad
\sigma_t^\Phi(\lambda_s)
=\lambda_s\pi((D\varphi\circ\sigma_s^\varphi:D\varphi)_t)=\lambda_s.
\]
Here \(\mathbb R\) is unimodular and \(\varphi\circ\sigma_s^\varphi=\varphi\). Covariance gives
\(\pi(\sigma_t^\varphi(x))=\lambda_t\pi(x)\lambda_t^*\), and the \(\lambda_s\)'s commute with one another. Equality on both generator families, followed by normality, proves
\[
\sigma_t^\Phi=\operatorname{Ad}(\lambda_t).
\]

Stone's theorem writes \(\lambda_t=e^{itP}\). Every operator in the core's commutant commutes with this unitary group and hence with the spectral projections of \(P\). Thus \(h=e^P\) is positive, has zero kernel, and is affiliated with \(C\), with \(h^{it}=\lambda_t\). Its spectral projections are fixed by \(\operatorname{Ad}(h^{it})\). Put \(B=h^{-1}\), also affiliated with the centralizer of \(\Phi\), and
\[
e_n=1_{[1/n,n]}(B),\qquad b_n=Be_n,\qquad
\tau(x)=\sup_n\Phi(b_n^{1/2}xb_n^{1/2})\quad(x\ge0).
\]
The bounded centralizer identities say that \(\Phi_a\) is a normal weight for \(a\ge0\) in the centralizer, and that \(a\mapsto\Phi_a\) is additive and order preserving. Since \(b_n\uparrow B\), this formula is an increasing supremum of normal weights, so it defines a normal weight. If \(\tau(x)=0\), faithfulness of \(\Phi\) gives \(x^{1/2}b_n^{1/2}=0\) for every \(n\). The range of \(b_n^{1/2}\) is \(e_nH\), and \(e_n\uparrow1\); hence \(x=0\).

For \(y\) in the finite left ideal of \(\Phi\), the bounded centralizer identity also gives
\[
\tau((ye_n)^*ye_n)
=\Phi(b_n^{1/2}y^*yb_n^{1/2})
\le n\,\Phi(y^*y)<\infty.
\]
Indeed on \(e_n\) every later density \(b_m\), \(m\ge n\), restricts to \(b_n\). The elements \(ye_n\) are strongly dense, first as \(n\to\infty\), then as \(y\) ranges over that left ideal. Thus \(\tau\) is semifinite.

On the corner \(e_nCe_n\), the density \(Be_n\) is bounded and invertible for the unit \(e_n\). The restricted weight \(\Phi|_{e_nCe_n}\) has the restricted modular action. The bounded invertible perturbation formula therefore gives
\[
\sigma_t^{\tau|_{e_nCe_n}}
=\operatorname{Ad}((Be_n)^{it})
  \sigma_t^{\Phi|_{e_nCe_n}}
=\operatorname{id}.
\]
So \(\tau\) is a trace on each of these corners. The following double cutoff proves traciality on the whole algebra.

For any \(y\in C\) and \(n,m\), both \(e_my e_n\) and its adjoint lie in the corner \(e_kCe_k\), \(k=\max(n,m)\). Traciality there gives
\[
\tau(e_ny^*e_my e_n)=\tau(e_my e_ny^*e_m).
\]
For fixed \(n\), normality and \(e_m\uparrow1\) make the left side increase to \(\tau(e_ny^*y e_n)\). Taking the supremum over \(n\), the defining density formula gives \(\tau(y^*y)\). Reversing the two suprema gives \(\tau(yy^*)\) on the right. Consequently \(\tau(y^*y)=\tau(yy^*)\), including infinite values. The weight \(\tau\) is a faithful normal semifinite trace on \(C\).

This is the affiliated perturbation \(\Phi_{h^{-1}}\), constructed here through its bounded spectral densities. The proof uses the bounded centralizer identities and perturbation formula; it does not require an unsymmetrized product with an unbounded operator.

**Theorem 4.1.** Every injective von Neumann algebra is semidiscrete.

**Proof.** Choose a faithful normal semifinite weight \(\varphi\). Its modular action is point-ultraweakly continuous. The real line is amenable by Example 2.1, so Corollary 3.1 makes \(C_\varphi(M)\) injective. The core theorem makes it semifinite. Corollary 6.3 of the hypertrace lesson therefore makes it semidiscrete. Finally, Theorem 3.2 transfers semidiscreteness from this regular crossed product to \(M\). \(\square\)

**Corollary 4.2.** For an arbitrary von Neumann algebra \(M\), the following are equivalent:

1. \(M\) is injective.
2. In one, hence every, faithful normal representation, multiplication \(M\odot M'\to B(H)\) is bounded for the minimal tensor norm.
3. The identity is a pointwise ultraweak limit of cpc matrix factorizations \(M\to M_n\to M\), with normal incoming maps.
4. The identity on \(M_*\) is a pointwise norm limit of cpc factorizations \(M_*\to M_n^*\to M_*\), in the dual matrix orders and Banach dual norms.

The factorizations in (3) also converge pointwise sigma-strong*, and their incoming maps can be chosen unital.

**Proof.** Theorem 4.1 supplies the remaining implication from (1) to semidiscreteness. The equivalence of the three approximation conditions, the implication to injectivity, normality, unit normalization and strong* convergence were proved in the finite-model lesson. \(\square\)

In (4), the middle norm is the trace-class norm. Replacing \(M_n^*\) by operator-norm matrices without adjusting the maps would change the statement.

## 5. Increasing algebras and type I examples

**Proposition 5.1.** A directed decreasing intersection of injective concrete von Neumann algebras is injective. A von Neumann algebra generated by a directed increasing union of injective von Neumann algebras is injective.

**Proof.** For the decreasing case, choose ucp retractions \(E_i:B(H)\to M_i\). Product ultraweak compactness of the pointwise norm balls gives a subnet converging pointwise ultraweakly to a ucp map \(E\). For each fixed \(j\), its tail values lie in \(M_j\), hence so does the limit. Thus \(E\) takes values in \(\bigcap_j M_j\) and fixes that intersection. It is a ucp retraction.

For an increasing family, its commutants form a decreasing injective family by Theorem 1.3. Their intersection is the commutant of the algebra generated by the original union. Apply the decreasing case and then Theorem 1.3 again. \(\square\)

**Corollary 5.2.** If \(M\) is generated by a directed increasing family of finite-dimensional unital *-subalgebras, then it is injective and semidiscrete.

**Proof.** A finite-dimensional C*-algebra is injective: represent it as a direct sum of full matrix algebras, each of which has the extension property by Arveson's theorem. Products preserve injectivity. Proposition 5.1 and Corollary 4.2 give the assertions. \(\square\)

This statement allows an arbitrary directed index set. The construction of finite-dimensional subalgebras from injectivity requires the later AFD arguments.

**Proposition 5.3.** Every type I von Neumann algebra is semidiscrete and injective.

**Proof.** We use the precise type I structure theorem: a type I algebra has a faithful normal representation with abelian commutant. In that representation \(M'\) is a commutative C*-algebra, hence nuclear by the sampling proof in [Completely positive finite models](completely-positive-finite-models.md). Its nuclearity implies
\(M\otimes_{\min}M'=M\otimes_{\max}M'\). Commuting representations give a contractive multiplication representation for the maximal norm, hence for the minimal norm. The commutant criterion makes \(M\) semidiscrete, and semidiscreteness gives injectivity. \(\square\)

The word *semidiscrete* reflects the type I examples: their multiplication representation has the spatial tensor bound. Semidiscreteness is the approximation property in Corollary 4.2; it does not require the approximating matrix maps to give subalgebras of \(M\).

Amenability in the averaging theorems is an explicit group hypothesis. The core argument uses it for \(\mathbb R\). It supplies no assertion that all connected locally compact groups are amenable.

## 6. Exercises with solutions

**Exercise 1.** Why does the entrywise amplification of a possibly singular retraction in Proposition 1.1 fix every element of \(M\bar\otimes B(K)\), rather than only its algebraic tensor subalgebra?

*Solution.* Every matrix entry of an element of the spatial von Neumann tensor product lies in \(M\), by its description as \((M'\otimes1)'\). The original retraction fixes each such entry exactly. The constructed amplified map therefore has precisely the original entries. Equality of all entries implies equality of bounded operators, since finite-coordinate vectors are dense. No continuity of the retraction on an ultraweak limit is used.

**Exercise 2.** Verify that entry transposition \(M_n(C^{\mathrm{op}})\to M_n(C)^{\mathrm{op}}\) is multiplicative with the indicated opposite products. Why does this prove the completely positive statement in Lemma 1.2?

*Solution.* The \((i,j)\) entry of the transposed product in the domain is \(\sum_k b_{ki}a_{jk}\), which is the \((i,j)\) entry of \(t(b)t(a)\), the product \(t(a)\circ t(b)\) in the codomain's opposite algebra. Adjoints are preserved as well, so the map is a *-isomorphism and preserves positivity in both directions. Applying a linear map to entries commutes with transposition, so positivity of every matrix amplification is equivalent on the two opposite systems.

**Exercise 3.** For the shift action on \(\ell^\infty(\mathbb Z)\), prove that an invariant mean kills every finite-support projection. Show explicitly why its average to the fixed algebra is not normal.

*Solution.* All singleton projections have the same mean value \(c\geq0\) by invariance. The sum of any \(n\) distinct ones is at most one, so \(nc\leq1\) for every \(n\); hence \(c=0\). Finite sums also have mean zero. The fixed algebra is the constant sequences, and the average sends \(x\) to \(m(x)1\). The projections of the finite intervals \([-n,n]\) increase to one, but all have averaged value zero, whereas the unit has averaged value one. Thus the map fails the increasing-supremum criterion for normality.

**Exercise 4.** Check the covariance formula in Section 3 using left Haar measure. Does a modular-function factor belong in the displayed left translation?

*Solution.* Left Haar invariance makes \(\xi(t)\mapsto\xi(s^{-1}t)\) unitary. Its adjoint translates by \(s\). The conjugated coefficient at \(t\) is
\(\alpha_{(s^{-1}t)^{-1}}(x)=\alpha_{t^{-1}s}(x)=\alpha_{t^{-1}}(\alpha_s(x))\), giving covariance. No modular factor belongs to this left translation. Right translations relative to left Haar measure require their own modular normalization.

**Exercise 5.** Prove directly that the constant embedding of \(M'\) in Theorem 3.2 commutes with each regular generator. Why would it be wrong to replace the coefficient field by the constant field \(x\)?

*Solution.* For \(y\in M'\), \(y\alpha_{t^{-1}}(x)=\alpha_{t^{-1}}(x)y\) at every \(t\), so the two multiplication fields commute. Also \(y\xi(s^{-1}t)\) is the result in either order with a left translation. A constant coefficient field \(x\) would commute with every translation and would implement only the trivial action; its covariance would require \(x=\alpha_s(x)\) for all \(s\). It does not describe a general action.

**Exercise 6.** Let \(F:G\to[0,\infty)\) be continuous and suppose
\(\int |f|^2F\leq C\int|f|^2\) for all \(f\in C_c(G)\). Prove \(F(t)\leq C\) at every point, without assigning positive Haar mass to singletons.

*Solution.* If \(F(t_0)>C\), continuity supplies an open neighborhood \(U\) on which \(F>C+\delta\) for some \(\delta>0\). Choose a nonzero compactly supported continuous function inside \(U\). It has positive \(L^2\) norm by Haar positivity, so \(\int|f|^2F\geq(C+\delta)\|f\|_2^2>C\|f\|_2^2\), a contradiction. This is the neighborhood argument in Theorem 3.2.

**Exercise 7.** In Theorem 2.2, why is normality of the automorphism \(\alpha_h\) needed, although normality of the averaged retraction is not asserted?

*Solution.* To compute \(\omega(\alpha_h(P(x)))\), we use the normal functional \(\omega\circ\alpha_h\) in the defining formula for \(P\). Normality makes that functional an element of \(M_*\), where the definition applies. It then gives the coefficient function \(g\mapsto\omega(\alpha_{hg}(x))\), which left invariance averages to the original value. This argument constructs the range in the fixed algebra without requiring \(P\) itself to preserve increasing suprema.

**Exercise 8.** Explain why the increasing-family argument in Proposition 5.1 passes through commutants. What is missing from taking a point-ultraweak cluster point of retractions onto the increasing algebras directly?

*Solution.* The direct cluster point fixes every element of the algebraic union, since each such element belongs to a sufficiently late algebra. Fixing its ultraweak closure would require continuity of that cluster map for the ultraweak topology, which a singular ucp retraction need not have. The commutants instead form a decreasing family. Tail values of their retractions belong to each fixed member of that family, and closedness therefore forces the cluster map's entire range into the intersection. That is enough to obtain a retraction onto the intersection and then return to the original algebra by the commutant theorem.

**Exercise 9.** List the exact steps that apply the continuous core to an injective algebra, including which step uses amenability and which uses semifiniteness. Why is no faithful normal state required?

*Solution.* Choose a faithful normal semifinite weight \(\varphi\), available on every von Neumann algebra. Its modular action defines the core. Amenability of \(\mathbb R\) and Corollary 3.1 make the core injective. The continuous-core trace theorem makes it semifinite. The semifinite hypertrace theorem then makes it semidiscrete. Finally, the regular crossed-product transfer theorem makes the coefficient algebra semidiscrete. The starting weight can be infinite on the unit, so existence of a finite or tracial faithful normal state is not needed.

**Exercise 10.** Let the action be trivial and \(G\) be the one-element group. Identify all maps in Theorem 3.2. Then identify the regular coefficient and group generators for a trivial action of a general group.

*Solution.* For the one-element group, \(L^2(G)\cong\mathbb C\), the regular representation is the original representation of \(M\), the group unitary is one, and \(\iota\) is the original commutant inclusion. The tensor estimate is exactly the commutant criterion for \(M\). For a general trivial action, \(\pi(x)=x\otimes1\) and \(\lambda_s=1\otimes\lambda_s^G\), so the generated algebra is \(M\bar\otimes\operatorname{VN}(G)\). The transfer conclusion still uses a tensor norm estimate in that regular representation.

## References

Fumio Hiai, [Concise lectures on selected topics of von Neumann algebras](https://arxiv.org/pdf/2004.02383v1), arXiv:2004.02383v1 (2020), Lemma 10.1 and Proposition 10.6, pp.89–91, give the regular formulas and change of representation. Lemmas 9.1–9.2 and Proposition 9.3, pp.80–84, give the bounded centralizer identities, corner restriction and spectral-density construction; Theorems 9.4 and 9.9, pp.84–88, give the affiliated perturbation and inner-modular trace argument. Theorem 10.15(1)–(2), pp.99–100, proves semifiniteness of the core for a general von Neumann algebra. Section 4 above includes weight existence, the bounded-corner construction and its double-cutoff trace proof.

Uffe Haagerup, [On the dual weights for crossed products of von Neumann algebras I: Removing separability conditions](https://journals.msp.org/mscand/article/download/1879/1878/1910), *Mathematica Scandinavica* 43 (1978), 99–118. Lemmas 2.5 and 2.8–2.12, pp.104–111, construct the coefficient GNS domain and close its involution without separability assumptions; Theorem 3.2(1)–(2), pp.112–113, gives the dual weight and its modular formulas. These supply the dual-weight input used in Section 4. Hiai's Theorem 10.12 states that general construction without its proof; his Theorem 10.13, pp.96–98, gives a separate operator-valued-weight proof for abelian groups.

William B. Arveson, [Subalgebras of C*-algebras](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224. Theorem 1.2.3 gives the completely positive extension method. Section 1 above proves the amplification, corner and product retractions directly, including arbitrary basis index sets and singular retractions.

Uffe Haagerup, [The standard form of von Neumann algebras](https://doi.org/10.7146/math.scand.a-11606), *Mathematica Scandinavica* 37 (1975), 271–283. Theorem 1.6 and Definition 2.1 give a standard representation for an arbitrary von Neumann algebra with \(JMJ=M'\). Theorem 1.3 uses that representation, the explicitly proved opposite-algebra argument, and the stated normal representation comparison.

Haagerup's Lemma 2.10, printed pp.278–279, represents every normal positive functional by a vector in the standard cone. The cyclic decomposition above gives the standard-form representation comparison from that theorem. The proof of Lemma 2.10 invokes Araki's cone theorem for its cyclic separating case; that prerequisite retains its own source record. The subsequent trace-class extension and dominated-form argument gives the comparison from any faithful normal starting representation; the form method is also proved in Anantharaman–Popa, Lemma 2.5.3, printed p.41.

Claire Anantharaman and Sorin Popa, [An introduction to II1 factors](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author-hosted draft, Exercises 10.2–10.6 and 10.10, printed pp.169–170. These pose corner, amplification, commutant, invariant-mean and increasing finite-dimensional consequences. They do not supply the proofs of those exercises or the general continuous-core theorem. Sections 1–3 and 5 here give the retractions, normal-action averaging, arbitrary decreasing/intersecting nets and regular crossed-product transfer at their stated generality.

- [Injectivity] *Injective von Neumann algebras*, Proposition 1.4, Proposition 2.3, Theorems 4.2–4.3 and 5.1, in the existing open course on injective factors. Those particular results apply to arbitrary von Neumann algebras; their use here does not import factor classification.
- [Crossed products] *Changing the Hilbert space of a regular crossed product*, the regular construction and normality theorem; *Building an intrinsic flow from modular coordinates*, the theorem removing the modular density. The latter uses the dual-weight construction and generator formulas from *Extending the dual weight beyond the common involution domain* and *How the dual weight moves crossed-product generators*, together with the stated modular prerequisites.
- [Modular theory] *General weights: finite domains, GNS spaces, and normal representations*, WG-008; *Weights and the Hilbert spaces of multiplication*, WH-13; *The positive cone of a standard representation*, SF-05; *Fixed elements and changes of density*, CZ-08 and CZ-11. These provide the arbitrary-algebra weight, standard-representation and affiliated-perturbation inputs.
- [Type I structure] *Projections and types of von Neumann algebras*, Proposition 11.2 and Corollary 11.3, in the existing foundations course. Only the faithful normal representation with abelian commutant is used in Proposition 5.3.
