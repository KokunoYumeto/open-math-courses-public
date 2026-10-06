# Discrete regular crossed products and their normal model comparison

*Scoped adaptation of the original OA-FLOW lesson 15 proof, under its exact published CC0 component grant. The discrete specialization and prerequisite bindings are by GPT-6.1 Sol (OpenAI), Ultra, October 2026; original contributions CC0. The source component supplies no individual model attribution in this section.*

The complete scope is the regular construction and normal comparison for a discrete group. It supplies precisely R1–R3 and R13–R17 consumed by *Crossed-product coefficients and factor tests*. The coefficient Hilbert spaces may have arbitrary dimension. The group may have any cardinality in this supplement; the consuming lesson fixes a countable group. No invariant state is needed.

We use the complete Hilbert tensor and matrix constructions in the companion spatial tensor supplement, Sections 1–2 and 5–8. Its Corollary 8.4 supplies the tensor extension of a normal isomorphism and its normal inverse. The published universal-enveloping chapter supplies the scalar normality criterion and positive-map criterion in Section 11. A faithful normal unital representation has a von Neumann image and normal inverse: the complete compact-ball, Kaplansky and preadjoint argument is Lemma 2.1 of that published chapter, or Section 6.6 of *Normal products and closed operator graphs*. These statements have arbitrary Hilbert-space scope.

<a id="OA-FLOW.REG.CONSTRUCTION"></a>
## The regular construction

Let M be a nonzero von Neumann algebra, G a discrete group with identity e, and alpha an action of G by normal unital automorphisms. Let rho:M→B(H_rho) be a normal unital representation. On the Hilbert direct sum K_rho=ell²(G;H_rho)=H_rho⊗ell²(G), define

\[
(\pi_\rho(a)\xi)(s)=\rho(\alpha_{s^{-1}}(a))\xi(s),
\qquad (L_g^\rho\xi)(s)=\xi(g^{-1}s).
\tag{R1--R2}
\]

Each vector has countable support in the Hilbert direct sum, even if G or H_rho is uncountable. Since rho and each alpha_s are contractive, summing squared coordinate norms gives \(\|\pi_\rho(a)\xi\|\leq\|a\|\|\xi\|\). Coordinatewise multiplication, adjoints and the unit show that pi_rho is a unital star representation. Permuting the coordinates makes each L_g^rho unitary, with inverse L_(g^-1)^rho and the group law. Strong continuity is automatic for a discrete group. Direct substitution gives

\[
L_g^\rho\pi_\rho(a)(L_g^\rho)^*
=\pi_\rho(\alpha_g(a)).
\tag{R3}
\]

The representation pi_rho is normal. Indeed, if \(0\leq a_i\uparrow a\) is an arbitrary bounded increasing net, each coordinate positive operator \(\rho(\alpha_{s^{-1}}(a-a_i))\) decreases strongly to zero. For a fixed vector xi and a finite subset F of its coordinates, the sum of quadratic forms on F tends to zero by directedness. The remaining sum is at most \(\|a\|\sum_{s\notin F}\|\xi(s)\|^2\), uniformly in i. Choose F to make that tail small, then choose one index dominating the finitely many coordinate requirements. Thus the full quadratic form tends to zero. The bounded positive differences then tend strongly to zero, using \(T^2\leq\|a\|T\), and pi_rho preserves the stated supremum. The complete published positive-map criterion makes it ultraweakly continuous. This argument does not interchange scalar integration with an arbitrary net.

If rho is faithful, the e-coordinate of pi_rho(a) is rho(a), so pi_rho is faithful and hence isometric. Put

\[
N_\rho^\alpha=\{\pi_\rho(M),L_g^\rho:g\in G\}''.
\]

Covariance makes the finite sums \(\sum_g\pi_\rho(a_g)L_g^\rho\) a unital star algebra containing both generator families. The bicommutant theorem in the spatial supplement, Section 4, makes these sums ultraweakly dense in N_rho^alpha.

## Matrix location

Let J_s put H_rho into coordinate s. Then

\[
J_s^*\pi_\rho(a)J_t=\delta_{s,t}\rho(\alpha_{s^{-1}}(a)).
\]

Every entry belongs to the concrete von Neumann algebra rho(M). The finite-corner matrix test in the spatial supplement, Proposition 2.1 and Section 5, therefore places pi_rho(a) in \(\rho(M)\bar\otimes B(\ell^2(G))\): compress by \(1\otimes p_F\), write its finite matrix as an algebraic tensor sum, and let the finite subsets F increase. These compressions have norm at most \(\|a\|\) and converge strongly to the original operator. Also \(L_g^\rho=1\otimes L_g\) lies in that tensor product. Consequently N_rho^alpha is contained in it.

<a id="OA-FLOW.REG.INDEPENDENCE"></a>
## Normal comparison and uniqueness

Let rho and sigma be faithful normal unital representations of M, on arbitrary H_rho and H_sigma. Their concrete coefficient algebras are normally isomorphic through \(\gamma=\sigma\rho^{-1}\). The spatial supplement, Corollary 8.4, supplies a normal isomorphism with normal inverse

\[
\Theta=\gamma\bar\otimes\operatorname{id}:
\rho(M)\bar\otimes B(\ell^2(G))
\longrightarrow\sigma(M)\bar\otimes B(\ell^2(G)).
\tag{R15}
\]

The entry at (s,t) of Theta(T) is gamma applied to the entry of T. For finite corners this follows from the prescribed action on elementary tensors. For an arbitrary T, the bounded finite compressions tend ultraweakly to T, and normality and normal coordinate compression extend that equality to every entry. Therefore the entries of Theta(pi_rho(a)) are

\[
\delta_{s,t}\gamma(\rho(\alpha_{s^{-1}}(a)))
=\delta_{s,t}\sigma(\alpha_{s^{-1}}(a)),
\tag{R16}
\]

which are the entries of pi_sigma(a). Entries determine an operator because finite-coordinate vectors form a dense subspace. Similarly Theta(1⊗L_g)=1⊗L_g. Theta and its normal inverse therefore transport both generated von Neumann algebras onto each other. Restriction gives

\[
C_{\sigma,\rho}^\alpha:N_\rho^\alpha\longrightarrow N_\sigma^\alpha,
\quad C_{\sigma,\rho}^\alpha(\pi_\rho(a))=\pi_\sigma(a),
\quad C_{\sigma,\rho}^\alpha(L_g^\rho)=L_g^\sigma.
\tag{R13}
\]

Two normal maps with these generator values agree on the ultraweakly dense finite-word algebra, and hence everywhere. The composites for three models have the same generator values, proving

\[
C_{\tau,\sigma}^\alpha C_{\sigma,\rho}^\alpha
=C_{\tau,\rho}^\alpha,
\qquad C_{\rho,\rho}^\alpha=\operatorname{id}.
\tag{R14}
\]

<a id="OA-FLOW.REG.SYSTEMNATURALITY"></a>
## Relabeling the coefficient system

Let eta:M→P be a normal isomorphism intertwining alpha with an action beta of the same discrete group. Given faithful normal unital rho of M and sigma of P, replace gamma by \(\sigma\eta\rho^{-1}\) in the preceding tensor construction. Its diagonal entries are

\[
\sigma(\eta\alpha_{s^{-1}}(a))
=\sigma(\beta_{s^{-1}}(\eta(a))).
\]

It follows that there is a unique normal isomorphism

\[
C_\eta:N_\rho^\alpha\longrightarrow N_\sigma^\beta,
\quad C_\eta(\pi_\rho^\alpha(a))=\pi_\sigma^\beta(\eta(a)),
\quad C_\eta(L_g^\rho)=L_g^\sigma.
\tag{R17}
\]

Uniqueness proves composition compatibility. A degenerate coefficient representation must first be compressed to rho(1)H_rho: its uncompressed regular algebra can have an extra group-algebra summand, so the displayed unital comparison is not asserted there. The zero algebra has its unique zero interpretation.

The result here is normal model independence. It does not assert the arbitrary-covariant commutant formula E9, a standard-form commutant, or a normal extension of every covariant representation. Those statements retain their separate proof obligations.
