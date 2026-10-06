# Representations of compact groups: unitarity, complete reducibility and finite dimension

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. A correction from a separate AI check has been applied and checked by the writing AI; a separate AI recheck is not claimed. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

A symmetry can act on a signal space without giving us a preferred coordinate system. The useful question is which parts of the signal have different transformation laws, and which coordinates merely describe repeated copies of the same law. We will answer it for continuous unitary actions of a compact Hausdorff group on any complex Hilbert space.

Begin with a small repeated-frequency example. It separates three tasks: choose a metric respected by the action, find invariant pieces, and identify the pieces that do not depend on a choice of basis. In finite dimension these tasks use ordinary linear algebra. In a large Hilbert space the extra issue is to produce even one finite-dimensional piece. A positive compact operator built from an orbit will provide it. Orthogonal complements then let us assemble all pieces, including arbitrary Hilbert multiplicities.

The prerequisites are [Haar measure on locally compact groups](#what-this-lesson-does-not-prove) and [Hilbert spaces and compact operators](#what-this-lesson-does-not-prove). The general spectral proof of Schur’s lemma also uses [bounded self-adjoint spectral theory and its functional-calculus foundations](#what-this-lesson-does-not-prove). A [complete compact-averaging proof](https://kokunoyumeto.github.io/open-math-courses-public/courses/representations-of-compact-groups/reader/compact-schur-proof.html) gives a second route. Exact proof homes and checked freely accessible comparisons are listed at the end. Earlier versions also used [Gruson–Serganova 2018]; its recorded source uses are retained.

## Repeated frequencies and the choices they leave

Let the circle act on \(\mathbb C^3\) by
\[
\rho(z)(v_1,v_2,v_3)=(zv_1,zv_2,z^{-1}v_3),\qquad |z|=1.
\]
The first two coordinates have the same transformation law. Any orthonormal basis of their plane gives two invariant lines; replacing \(e_1,e_2\) by \((e_1+e_2)/\sqrt2,(e_1-e_2)/\sqrt2\) changes those lines. The plane itself is intrinsic. For example, at \(z=i\) it is the \(i\)-eigenspace, whereas the third coordinate is the \(-i\)-eigenspace. An operator commuting with every \(\rho(z)\) is an arbitrary matrix on that plane and a scalar on the third coordinate: commuting with \(\rho(i)\) removes the off-diagonal blocks, and each diagonal block then commutes with the scalar action.

Thus repeated copies permit mixing, while distinct transformation laws cannot mix. The terms **isotypic component** and **multiplicity space** will make this observation precise for every compact group. A decomposition into individual irreducibles is useful, but uniqueness belongs to these larger components.

The finite-dimensional algebra used here can be checked without an infinite-dimensional basis theorem. Over either \(\mathbb R\) or \(\mathbb C\), write a vector \(v=\sum c_jb_j\) in a basis. If \(c_i\ne0\), replacing \(b_i\) by \(v\) preserves the span, by solving for \(b_i\); it preserves independence, since substitution into a relation first forces the coefficient of \(v\) to vanish. Successive exchanges show that an independent list has at most as many members as any finite basis. Adding a vector outside the current span therefore extends any independent list to a basis after finitely many steps. The same construction, choosing each new vector from the original spanning set, extracts a basis from it. It also proves the usual subspace dimension and basis-extension assertions. These are the exchange and dimension proofs in the programme's **B40** foundation section *Basis and Dimension*, labels `lm:ExchangeLemma`, `th:AllBasesSameSize`, and `cor:LIExpBas`; the field-independent argument above supplies their complex form. The credited structured [Hefferon foundation source](https://github.com/KokunoYumeto/program-matematika-indonesia/releases/download/b40-foundations-2026.10.02/PUBLIC_DEPENDENCY_INTEGRATION_SOURCE.zip) also records that the spanning-set reduction must choose its added vectors from the spanning set itself.

For completeness, the topology does not depend on the chosen finite basis or norm. For a norm \(N\), the triangle inequality gives \(N(\sum x_jb_j)\le C\|x\|_2\). Thus \(N\) is continuous in Euclidean coordinates; on the compact Euclidean unit sphere its positive minimum is \(c>0\), giving \(c\|x\|_2\le N(\sum x_jb_j)\). Gram–Schmidt subtracts the already chosen orthogonal projections and divides by the nonzero remainder norm; independence makes each remainder nonzero. It produces an orthonormal basis, and the finite orthogonal projection is its explicit coordinate sum. The arbitrary-Hilbert-space projection and basis arguments are the full Hilbert prerequisite linked below.

## Making symmetry preserve lengths

Throughout, \(G\) is a compact Hausdorff group. Its Haar measure \(dg\) has total mass \(1\), is invariant under both left and right translations, and gives positive measure to every nonempty open set. Write \(\mu\) for this measure. These are the Haar-measure facts recalled at the end. Inner products are linear in the first variable.

A **unitary representation** on a complex Hilbert space \(H\) is a homomorphism

\[
\pi:G\longrightarrow U(H)
\]

such that \(g\mapsto\pi(g)v\) is continuous for each \(v\in H\). This is **strong continuity**. We impose neither separability of \(H\) nor metrizability of \(G\). The zero space is allowed, but an irreducible representation is always nonzero. **Irreducible** means that the only closed invariant subspaces are \(0\) and \(H\).

**Lemma 1.1 (orthogonal complements).** If \(M\subseteq H\) is a closed invariant subspace of a unitary representation, then \(M^\perp\) is invariant and the orthogonal projection \(P_M\) commutes with every \(\pi(g)\). Conversely, a commuting orthogonal projection has invariant range.

**Proof.** Invariance under both \(g\) and \(g^{-1}\) gives \(\pi(g)M=M\). For \(v\in M^\perp\) and \(w\in M\),

\[
\langle\pi(g)v,w\rangle
=\langle v,\pi(g^{-1})w\rangle=0.
\]

Thus both summands of \(H=M\oplus M^\perp\) are preserved, so their projection commutes with the action. Conversely, if \(P\pi(g)=\pi(g)P\), then \(\pi(g)Pv=P\pi(g)v\) lies in the range of \(P\). ∎

**Proposition 1.2 (unitarization).** Every continuous representation \(\rho:G\to GL(V)\) on a finite-dimensional complex vector space preserves a positive definite Hermitian inner product. Consequently, \(V\) is a direct sum of irreducible representations.

**Proof.** Start with any inner product \(\langle\ ,\ \rangle_0\), and set

\[
\langle v,w\rangle_G
=\int_G\langle\rho(g)v,\rho(g)w\rangle_0\,dg.
\]

The integral is finite because its integrand is continuous on a compact space. It is sesquilinear and Hermitian. For \(v\ne0\), the continuous function \(g\mapsto\|\rho(g)v\|_0^2\) is strictly positive near the identity, so its integral is positive. Right invariance gives

\[
\langle\rho(h)v,\rho(h)w\rangle_G
=\int_G\langle\rho(gh)v,\rho(gh)w\rangle_0\,dg
=\langle v,w\rangle_G.
\]

All norms on \(V\) give the same topology, so this change of inner product preserves continuity. If \(V\ne0\), choose an invariant subspace of smallest positive dimension. It is irreducible. Lemma 1.1 splits it off, and induction on dimension finishes the decomposition. ∎

For a finite group, the formula is \( |G|^{-1}\sum_g\langle\rho(g)v,\rho(g)w\rangle_0\). The compact-group proof has exactly the same geometric meaning: first choose an invariant way to measure lengths, then take orthogonal complements.

**Worked example 1.3.** Put \(z=e^{i\theta}\) and consider

\[
\rho(z)=\begin{pmatrix}1&z-1\\0&z\end{pmatrix}
=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\0&z\end{pmatrix}
\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
\]

This is a continuous circle representation. Its matrices need not preserve the Euclidean inner product. Averaging that inner product gives \(\langle v,w\rangle_G=w^*Qv\), where

\[
Q=\int_{\mathbb T}\rho(z)^*\rho(z)\,dz
=\begin{pmatrix}1&-1\\-1&3\end{pmatrix}.
\]

Here \(\int z\,dz=0\) and \(\int|z-1|^2\,dz=2\), obtained by integrating the elementary exponentials over \(0\le\theta\le2\pi\). The determinant of \(Q\) is \(2\), and its leading entry is positive. The invariant lines spanned by \((1,0)\) and \((1,1)\) are orthogonal for this new inner product. Their normalized generators are \((1,0)\) and \(2^{-1/2}(1,1)\), displaying the two irreducible pieces explicitly.

## Intertwiners detect irreducibility

The commutant gives an irreducibility test without assuming finite dimension. It is worth establishing that test now: later, the finite-dimensional pieces we construct will be classified by their intertwining maps rather than by their chosen bases.

For unitary representations \(\sigma\) on \(V\) and \(\pi\) on \(H\), let

\[
\operatorname{Hom}_G(\sigma,\pi)
=\{T\in B(V,H):T\sigma(g)=\pi(g)T\text{ for all }g\}.
\]

The **commutant** is \(\pi(G)'=\operatorname{Hom}_G(\pi,\pi)\). Equivalence means equivalence by a unitary intertwiner.

**Theorem 4.1 (Schur's lemma).** A nonzero unitary representation is irreducible if and only if its commutant is \(\mathbb CI\). Between two irreducible unitary representations every nonzero bounded intertwiner is a positive scalar times a unitary intertwiner. Consequently, the intertwiner space is zero for inequivalent irreducibles and one-dimensional for equivalent ones.

**Proof.** A proper nonzero closed invariant subspace gives a nonscalar commuting projection by Lemma 1.1. Conversely, suppose the representation is irreducible. The commutant is closed under adjoints, since \(\pi(g)^*=\pi(g^{-1})\). If it contained a nonscalar \(A\), at least one of

\[
\frac{A+A^*}{2},\qquad\frac{A-A^*}{2i}
\]

would be a nonscalar self-adjoint operator \(B\). Its spectrum cannot be a singleton, since the isometric continuous functional calculus would then make \(B\) scalar. Choose disjoint neighborhoods of two different spectral points. The spectral projection of either neighborhood is nonzero: choose a continuous function on the spectrum supported in that neighborhood and nonzero at its chosen point. Its image under the isometric calculus is nonzero and equals its product with that projection. The two projections are orthogonal, so neither can be \(I\). Every operator commuting with \(B\) commutes with its spectral projections. Such a projection therefore commutes with \(\pi(G)\), contradicting irreducibility.

Now let \(T:V\to W\) intertwine irreducibles \(\sigma,\tau\). Its adjoint intertwines in the reverse direction, so \(T^*T=cI_V\) and \(TT^*=dI_W\), with \(c,d\ge0\). If \(T\ne0\), both are positive, and

\[
dT=(TT^*)T=T(T^*T)=cT
\]

gives \(c=d\). Thus \(c^{-1/2}T\) is unitary. Finally, fixing one unitary intertwiner \(U\), every other one has \(U^*T\) scalar by the commutant assertion. ∎

## Finding a finite-dimensional subspace

The finite-dimensional argument cannot simply be repeated in an arbitrary Hilbert space: there need not be an invariant subspace of smallest positive dimension. We need a construction that forces a finite-dimensional range.

Think of a unit vector \(u\) as one measurement direction. The quantity \(|\langle v,\pi(g)u\rangle|^2\) measures the response of \(v\) to that direction after a symmetry. Integrating it will produce a positive operator that cannot vanish, because the response of \(u\) at the identity is one. Compactness of the orbit allows approximation by finitely many measurements. The spectral theorem then extracts a finite-dimensional invariant space.

Strong continuity alone does not give operator-norm continuity of \(\pi\). For example, on \(\ell^2(\mathbb Z)\) let \(\pi(e^{it})e_n=e^{int}e_n\). Finite-support approximation proves strong continuity. At \(t=\pi/N\), however, the \(N\)-th basis vector is sent to its negative, so \(\|\pi(e^{i\pi/N})-I\|=2\) for every \(N\). Averaging a rank-one measurement avoids this obstruction: its operator-valued orbit is norm continuous.

For \(a\in H\), write \(P_a v=\langle v,a\rangle a\). When \(\|a\|=1\), this is the orthogonal projection onto \(\mathbb Ca\). If \(a,b\) are unit vectors, then

\[
\|(P_a-P_b)v\|
\le |\langle v,a-b\rangle|\|a\|
   +|\langle v,b\rangle|\|a-b\|
\le2\|v\|\|a-b\|.
\tag{2.1}
\]

Thus \(\|P_a-P_b\|\le2\|a-b\|\).

**Lemma 2.2 (averaging a projection).** Let \(u\in H\) be a unit vector and define

\[
T_u=\int_G\pi(g)P_u\pi(g)^*\,dg.
\tag{2.2}
\]

This integral exists in operator norm. The operator \(T_u\) is positive, compact, nonzero, and commutes with \(\pi(G)\).

**Proof.** Set \(F(g)=P_{\pi(g)u}\). Strong continuity and (2.1) make \(F:G\to B(H)\) norm continuous.

Here is a construction of its integral valid on any compact Hausdorff group. Given \(\varepsilon>0\), a finite open cover makes the oscillation of \(F\) less than \(\varepsilon\) on each member. Successive differences of the cover members give a finite Borel partition \(E_1,\ldots,E_N\), with each nonempty cell contained in one member. Choose \(g_j\in E_j\) and form

\[
S_\varepsilon=\sum_{j=1}^N\mu(E_j)F(g_j).
\tag{2.3}
\]

The corresponding simple function differs from \(F\) uniformly by less than \(\varepsilon\). Two such sums differ in norm by at most the sum of their errors: refine their partitions and use the triangle inequality and \(\mu(G)=1\). Taking errors tending to zero gives a Cauchy sequence in \(B(H)\). Such a sequence converges in operator norm: its pointwise limits exist by completeness of \(H\), define a bounded linear operator, and the uniform Cauchy bounds pass to the limit. The resulting operator is independent of the approximations. This defines (2.2), with \(\|T_u-S_\varepsilon\|\le\varepsilon\), and its scalar matrix entries are the scalar integrals of those of \(F\).

Every \(S_\varepsilon\) has finite rank. Their norm limit is compact: its image of the unit ball lies within \(\varepsilon\) of a bounded set in a finite-dimensional space. That gives a finite net of arbitrarily small radius, hence a totally bounded image and compact closure.

Since \(F(g)v=\langle v,\pi(g)u\rangle\pi(g)u\),

\[
\langle T_uv,v\rangle
=\int_G|\langle v,\pi(g)u\rangle|^2\,dg\ge0.
\tag{2.4}
\]

In particular, the integrand for \(v=u\) equals \(1\) at the identity. Continuity and positivity of Haar measure on open sets give \(\langle T_uu,u\rangle>0\). Finally,

\[
\pi(h)T_u\pi(h)^*
=\int_G\pi(hg)P_u\pi(hg)^*\,dg=T_u
\]

by left invariance. The integrand consists of self-adjoint operators, so the norm integral is self-adjoint as well. ∎

The argument uses compactness of the operator-valued orbit, not a countable basis for \(H\). In particular, no separability assumption has entered.

**Proposition 2.5 (a small invariant subspace).** Every nonzero unitary representation of \(G\) contains a nonzero finite-dimensional invariant subspace, and therefore an irreducible subrepresentation.

**Proof.** Apply Lemma 2.2. The compact self-adjoint spectral theorem supplies an orthonormal eigenbasis for \(T_u\). Since \(T_u\ne0\) and is positive, some eigenvalue \(\lambda\) is positive. Its eigenspace \(E_\lambda\) is invariant, because \(T_u\) commutes with the action.

We can check its finite dimension directly. For any orthonormal vectors \(v_1,\ldots,v_n\in E_\lambda\), Bessel's inequality gives

\[
n\lambda
=\sum_{j=1}^n\langle T_uv_j,v_j\rangle
=\int_G\sum_{j=1}^n|\langle v_j,\pi(g)u\rangle|^2\,dg
\le1.
\tag{2.6}
\]

Thus \(\dim E_\lambda\le1/\lambda\). Proposition 1.2, or its orthogonal-complement induction, supplies an irreducible subspace inside \(E_\lambda\). ∎

**Theorem 2.7 (finite dimension of irreducibles).** Every irreducible unitary representation of a compact Hausdorff group is finite-dimensional.

**Proof.** The nonzero invariant finite-dimensional subspace provided by Proposition 2.5 is closed. Irreducibility forces it to be the entire representation space. ∎

Finite-dimensional invariant subspaces are the crucial intermediate conclusion. An argument using irreducibility from the outset would not suffice for the decomposition theorem that follows.

## Completing an orthogonal decomposition

For a family of Hilbert spaces \((H_i)_{i\in I}\), the **Hilbert direct sum** is

\[
\widehat{\bigoplus}_{i\in I}H_i
=\left\{(v_i):\sum_{i\in I}\|v_i\|^2<\infty\right\},
\qquad
\sum_{i\in I}\|v_i\|^2
=\sup_{F\subseteq I\text{ finite}}\sum_{i\in F}\|v_i\|^2.
\]

Every such vector has countable support: for each positive integer \(n\), only finitely many coordinates can have norm at least \(1/n\). Finite-support vectors are dense, but they need not exhaust the sum. This differs from the algebraic direct sum, which requires finite support.

**Theorem 3.1 (complete reducibility).** Every strongly continuous unitary representation of \(G\) is a Hilbert direct sum of irreducible finite-dimensional subrepresentations. This holds without separability assumptions.

**Proof.** Consider collections of mutually orthogonal nonzero irreducible invariant subspaces of \(H\), ordered by inclusion. The union along a chain is again such a collection. Zorn's lemma therefore gives a maximal collection \((H_i)_{i\in I}\).

Let \(K\) be the closure of their algebraic sum. It is invariant: the action preserves each summand and is bounded. Its orthogonal complement is invariant by Lemma 1.1. If \(K^\perp\ne0\), the restricted representation remains strongly continuous and Proposition 2.5 supplies an irreducible subspace in \(K^\perp\). Adding it contradicts maximality. Hence \(K=H\).

Orthogonality identifies \(H\) isometrically with the Hilbert direct sum of the \(H_i\), and every \(H_i\) is finite-dimensional by Theorem 2.7. The identification intertwines the actions, first on finite sums and then by continuity. For \(H=0\), take the empty sum. ∎

Conversely, any Hilbert direct sum of strongly continuous unitary representations is strongly continuous. Given \(v\) and \(\varepsilon>0\), choose a finite-support approximation \(w\) with \(\|v-w\|<\varepsilon\). Near the identity the finite sum satisfies \(\|\pi(g)w-w\|<\varepsilon\). Unitarity then gives \(\|\pi(g)v-v\|<3\varepsilon\). This also justifies forming examples with uncountably many summands.

## Identifying the pieces and counting them

Let \(\widehat G\) be the set of equivalence classes of irreducible unitary representations. Choose a representative \(\sigma\) on \(V_\sigma\) for each class. The **isotypic component** \(H_\sigma\) is the closed linear span of all irreducible invariant subspaces equivalent to \(\sigma\).

**Proposition 4.2 (canonical isotypic components).** For any decomposition \(H=\widehat\bigoplus_iH_i\) from Theorem 3.1,

\[
H_\sigma=\widehat{\bigoplus}_{i:\,\pi|_{H_i}\simeq\sigma}H_i,
\qquad
H=\widehat{\bigoplus}_{[\sigma]\in\widehat G}H_\sigma.
\tag{4.3}
\]

These components are independent of the decomposition, and distinct ones are orthogonal.

**Proof.** Write \(P_i\) for projection onto \(H_i\). It commutes with the action. If \(L\) is any irreducible subspace of type \(\sigma\), then \(P_i|_L\) intertwines irreducibles. Schur's lemma makes it zero unless \(H_i\) has that type. Thus \(L\) lies in the indicated closed subsum. Conversely, every summand in that subsum is included in the definition of \(H_\sigma\). Equality follows. Grouping the orthogonal summands proves the remaining claims. ∎

**Proposition 4.4 (multiplicity).** The space \(M_\sigma=\operatorname{Hom}_G(\sigma,\pi)\) has a canonical Hilbert inner product, determined by

\[
S^*T=\langle T,S\rangle_{M_\sigma}I_{V_\sigma}.
\tag{4.5}
\]

The number of summands of type \(\sigma\) in any irreducible decomposition is

\[
m_\sigma=\dim_{\mathrm{Hilb}}M_\sigma,
\tag{4.6}
\]

where Hilbert dimension means the cardinality of an orthonormal basis. In particular, multiplicity is independent of the decomposition.

**Proof.** Schur's lemma makes \(S^*T\) scalar, and (4.5) is sesquilinear, Hermitian and positive definite. For any unit vector \(v\in V_\sigma\),

\[
\|T\|^2=\|Tv\|^2=\langle T,T\rangle_{M_\sigma}.
\]

The intertwiner equations are closed under operator-norm limits, so this space is complete. More explicitly, an operator-norm Cauchy sequence has a pointwise limit on \(V_\sigma\); its uniform bounds make the limit a bounded linear operator, and the intertwining equations pass to that limit.

Fix a decomposition and let \(I_\sigma\) index its summands of type \(\sigma\). Choose unitary intertwiners \(U_i:V_\sigma\to H_i\). For \(T\in M_\sigma\), Schur's lemma gives

\[
P_iT=a_iU_i\quad(i\in I_\sigma),
\qquad P_iT=0\quad(i\notin I_\sigma).
\]

Taking a unit vector \(v\) gives \(\|T\|^2=\sum_i|a_i|^2\). Conversely, any \(a\in\ell^2(I_\sigma)\) defines

\[
T_av=\sum_{i\in I_\sigma}a_iU_iv.
\]

Orthogonality gives convergence and \(\|T_av\|^2=\|v\|^2\sum_i|a_i|^2\). The sums intertwine, and their limits do too. Hence \(a\mapsto T_a\) is a unitary identification of \(\ell^2(I_\sigma)\) with \(M_\sigma\). Its Hilbert dimension is \( |I_\sigma|\). Formula (4.5) is intrinsic, proving independence. ∎

For finite multiplicity, (4.6) also uses ordinary complex vector-space dimension. For infinite multiplicity, it uses Hilbert dimension. The coordinate vectors in \(\ell^2(I_\sigma)\) span only the finite-support sequences algebraically, so counting them as a vector-space basis would be incorrect.

There is a useful intrinsic form of (4.3):

\[
H\simeq\widehat{\bigoplus}_{[\sigma]\in\widehat G}
\bigl(M_\sigma\widehat\otimes V_\sigma\bigr),
\qquad
\pi(g)\simeq\widehat{\bigoplus}_{[\sigma]}(I\otimes\sigma(g)).
\tag{4.7}
\]

Indeed, evaluation \(T\otimes v\mapsto Tv\) preserves inner products because

\[
\langle Tv,Sw\rangle
=\langle S^*Tv,w\rangle
=\langle T,S\rangle_{M_\sigma}\langle v,w\rangle.
\]

It extends isometrically to the completed Hilbert tensor product. Each nonzero \(T\in M_\sigma\) is a scalar multiple of an isometry onto an irreducible subspace of type \(\sigma\), by (4.5), so evaluation takes values in \(H_\sigma\). Its range is closed and contains every copy of \(\sigma\), and hence equals \(H_\sigma\). Thus the group acts on \(V_\sigma\), while \(M_\sigma\) records how many copies occur.

A dense invariant algebraically semisimple subspace need not be unique. For example, under the trivial action on \(\ell^2(\mathbb N)\), both the finite-support sequences and the full space are dense invariant algebraically semisimple subspaces: a vector-space basis decomposes either into trivial lines. They are different. Even individual orthogonal copies are not canonical: changing an orthonormal basis of a multiplicity space changes those copies while preserving \(H_\sigma\).

## Finite actions and functions on a group

**Example 5.1 (the circle and rotations).** Every irreducible unitary representation of an abelian group is one-dimensional. Indeed, each \(\pi(g)\) lies in the commutant, so Schur's lemma makes it scalar. Then every line is invariant, forcing dimension one.

For \(\mathbb T=\mathbb R/2\pi\mathbb Z\), all continuous characters are

\[
\chi_k(e^{i\theta})=e^{ik\theta},\qquad k\in\mathbb Z.
\tag{5.2}
\]

Here we import the character classification from [*Characters and the dual group*, Theorem 3.1 and Corollary 3.2](course:HA-LCA/HA-LCA-02#section-3): every continuous character of the additive real line is uniquely \(x\mapsto e^{2\pi itx}\), \(t\in\mathbb R\), and every continuous character of the circle is uniquely \(z\mapsto z^k\), \(k\in\mathbb Z\). That lesson uses \(z=e^{2\pi ix}\). Setting \(x=\theta/(2\pi)\) gives exactly (5.2), with our angle convention. The representation-theoretic deduction from Schur's lemma above is separate from this imported classification.

The map sending \(e^{i\theta}\) to the real rotation matrix through angle \(\theta\) identifies \(\mathbb T\) with \(SO(2)\). Thus the same list describes its complex irreducibles. For instance, the complexified plane rotation representation has eigenvectors \((1,-i)\) and \((1,i)\), carrying \(\chi_1\) and \(\chi_{-1}\).

**Worked example 5.3 (a finite permutation action).** Let a cyclic group of order three act on five points: it cycles \(x_0,x_1,x_2\) and fixes \(a,b\). On the space with orthonormal basis \(\delta_{x_0},\delta_{x_1},\delta_{x_2},\delta_a,\delta_b\), the generator \(r\) permutes basis vectors. Hence its action is unitary.

Put \(\omega=e^{2\pi i/3}\) and

\[
v_j=\frac1{\sqrt3}\sum_{k=0}^2\omega^{-jk}\delta_{x_k},
\qquad j=0,1,2.
\]

A shift of the index gives \(rv_j=\omega^jv_j\). The geometric sum \(\sum_{k=0}^2\omega^{mk}\) equals \(3\) if \(3\mid m\) and \(0\) otherwise, proving orthonormality. Thus the trivial character has multiplicity three, with component \(\operatorname{span}(v_0,\delta_a,\delta_b)\), and each other character has multiplicity one. This illustrates how an isotypic space can be canonical while its decomposition into equivalent lines is not.

More generally, a finite group's action on a finite set gives a unitary permutation representation, since it permutes an orthonormal basis. Haar integration is normalized counting. Proposition 1.2 recovers complete reducibility of all finite-dimensional complex representations in this case.

**Example 5.4 (regular representations).** On \(L^2(G,dg)\), define

\[
(L_gf)(x)=f(g^{-1}x),\qquad (R_gf)(x)=f(xg).
\]

Both are homomorphisms, and Haar invariance gives \(\|L_gf\|_2=\|R_gf\|_2=\|f\|_2\). Translation continuity in \(L^2\), recalled at the end, makes them strongly continuous. Theorem 3.1 therefore applies even when \(L^2(G)\) is not separable. Determining their general compact-group multiplicities belongs to *Matrix coefficients and the Peter–Weyl theorem*.

For the circle, those multiplicities can already be computed. Write \(e_n(\theta)=e^{in\theta}\), with measure \(d\theta/(2\pi)\). Direct integration gives an orthonormal family and

\[
L_{e^{i\alpha}}e_n=e^{-in\alpha}e_n.
\tag{5.5}
\]

The minus sign comes from the inverse in left translation. To prove completeness, let \(f\in L^2(\mathbb T)\) transform by \(\chi_k\). Averaging its eigenvector equation gives, in \(L^2\),

\[
f(\theta)=\int_0^{2\pi}e^{-ik\alpha}f(\theta-\alpha)\frac{d\alpha}{2\pi}
=e^{-ik\theta}\int_0^{2\pi}e^{ikt}f(t)\frac{dt}{2\pi}.
\tag{5.6}
\]

The first integral is a Hilbert-space integral of a continuous vector-valued function. The scalar calculation is justified by \(L^2\subseteq L^1\) on this probability space and Fubini's theorem. Thus every subrepresentation of type \(\chi_k\) is the line \(\mathbb Ce_{-k}\). Theorem 3.1 and Example 5.1 force their closed sum to exhaust \(L^2(\mathbb T)\). Therefore

\[
L^2(\mathbb T)=\widehat{\bigoplus}_{n\in\mathbb Z}\mathbb Ce_n,
\qquad m_{\chi_k}=1.
\]

In particular, \(f=\sum_n\langle f,e_n\rangle e_n\) with convergence in \(L^2\), and \(\|f\|_2^2=\sum_n|\langle f,e_n\rangle|^2\). These are Hilbert-space expansions; pointwise convergence is a separate question.

**Corollary 5.7 (irreducibility on a locally convex space).** Let \(V\ne0\) be a Hausdorff locally convex complex vector space, and let \(\rho:G\to GL(V)\) have a jointly continuous action. If \(V\) has no proper nonzero closed invariant subspace, then \(V\) is finite-dimensional, admits an invariant inner product, and is isomorphic as a topological representation to a subrepresentation of \(R\) on \(L^2(G)\).

**Proof.** A nonzero continuous linear functional \(\ell\) exists by the locally convex consequence of Hahn–Banach recalled below. Define

\[
(\Phi v)(g)=\ell(\rho(g)v).
\]

This is continuous in \(g\), and \(\Phi\) is a continuous linear map from \(V\) to \(C(G)\) with the supremum norm. Indeed, continuity at each \((g,0)\) bounds the expression on a product of neighborhoods; a finite cover of \(G\) and intersection of the corresponding neighborhoods of zero give one uniform bound. Thus \(\Phi:V\to L^2(G)\) is continuous too. It is nonzero, since \(\ell(v)\ne0\) for some \(v\), and a continuous function nonzero at the identity is nonzero in \(L^2\). Also,

\[
\Phi(\rho(h)v)(g)=\ell(\rho(gh)v)=(R_h\Phi v)(g).
\]

By Theorem 3.1, \(R\) is an orthogonal sum of finite-dimensional irreducibles. At least one summand projection \(P_i\) makes \(P_i\Phi\ne0\). Its kernel is a closed invariant subspace of \(V\), so irreducibility makes the kernel zero. This injects \(V\) into the finite-dimensional space \(H_i\); hence \(V\) is finite-dimensional.

Its topology is the usual finite-dimensional topology. Indeed, let \(A:\mathbb C^d\to V\) be the continuous linear bijection given by a basis. The image of the unit sphere is compact and does not contain zero, so a neighborhood \(U\) of zero avoids it. Joint scalar continuity and compactness of the closed unit disk give a neighborhood \(W\) of zero with \(cW\subseteq U\) for every \(|c|\le1\). Every \(v\in W\) has \(\|A^{-1}v\|<1\), since otherwise rescaling it into the sphere would put a point of \(A(\text{sphere})\) in \(U\). Scaling \(W\) proves inverse continuity. Proposition 1.2 now unitarizes \(\rho\). The nonzero intertwiner \(\Phi\) itself has zero kernel, and its finite-dimensional image is closed; its inverse on that image is continuous. This proves the claimed topological embedding. ∎

## Exercises with complete solutions

**Exercise 6.1 — Easy.** Show that every continuous representation of \(\mathbb T\) on \(\mathbb C^n\) has a basis in which all matrices are diagonal, with entries \(e^{ik_j\theta}\), \(k_j\in\mathbb Z\). Decide whether \(\theta\mapsto\begin{pmatrix}1&\theta\\0&1\end{pmatrix}\) gives a circle representation.

**Solution.** Proposition 1.2 gives an invariant inner product and an irreducible decomposition. Example 5.1 makes each summand one-dimensional and identifies its character with some \(\chi_{k_j}\). Choosing one basis vector in each summand diagonalizes the whole action simultaneously; repeated integers are permitted. The displayed shear is a homomorphism from the additive group \(\mathbb R\), but the matrices at \(0\) and \(2\pi\) differ. It therefore does not descend to the quotient circle. For \(n=0\), the diagonal list is empty.

**Exercise 6.2 — Medium.** Let \(Q\) be an orthogonal projection of finite rank \(r\) in a strongly continuous unitary representation of \(G\). Prove that

\[
T_Q=\int_G\pi(g)Q\pi(g)^*\,dg
\]

is compact by approximating it in norm by finite weighted sums of finite-rank operators. Do this without a metric on \(G\). Show also that a positive eigenvalue \(\lambda\) satisfies \(\dim\ker(T_Q-\lambda I)\le r/\lambda\).

**Solution.** For \(r=0\), the operator is zero and there is no positive eigenvalue. Otherwise choose an orthonormal basis \(u_1,\ldots,u_r\) of the range of \(Q\). Then \(Q=\sum_{a=1}^rP_{u_a}\), so (2.1) gives

\[
\|\pi(g)Q\pi(g)^*-\pi(h)Q\pi(h)^*\|
\le2\sum_{a=1}^r\|\pi(g)u_a-\pi(h)u_a\|.
\]

The orbit is norm continuous. Choose a finite open cover with oscillation less than \(\varepsilon\), turn it into a disjoint Borel partition by successive differences, and choose a tag in each nonempty cell. The weighted sum has rank at most \(Nr\), and its distance from the integral is at most \(\varepsilon\), exactly as in (2.3). The image-of-the-unit-ball argument in Lemma 2.2 proves compactness of the limit. These are tagged approximation sums; neither intervals nor a mesh size are needed.

If \(v_1,\ldots,v_n\) are orthonormal eigenvectors for \(\lambda>0\), Bessel's inequality gives

\[
n\lambda
=\int_G\sum_{a=1}^r\sum_{j=1}^n
 |\langle v_j,\pi(g)u_a\rangle|^2\,dg\le r.
\]

There cannot be an orthonormal family larger than \(r/\lambda\) in that eigenspace. Taking \(Q=P_u\) recovers the operator and estimate used in Section 2.

**Exercise 6.3 — Medium.** Prove that every compact subgroup \(K\subseteq GL(n,\mathbb C)\) is conjugate to a subgroup of \(U(n)\). Give the conjugating matrix in terms of an averaged Gram matrix.

**Solution.** Equip \(K\) with normalized Haar measure and put \(Q=\int_Kk^*k\,dk\). For \(v\ne0\), \(v^*Qv=\int_K\|kv\|^2\,dk>0\), so \(Q\) is positive definite. Right invariance gives \(h^*Qh=Q\) for \(h\in K\). By the finite-dimensional spectral theorem, \(Q\) has a positive definite square root \(S=Q^{1/2}\). Then

\[
(ShS^{-1})^*(ShS^{-1})
=S^{-1}h^*QhS^{-1}
=S^{-1}QS^{-1}=I.
\]

Hence \(SKS^{-1}\subseteq U(n)\). This includes the empty-dimensional case with the unique transformation on the zero space.

**Exercise 6.4 — Hard.** Suppose every irreducible in a unitary representation of \(G\) occurs with finite multiplicity. Prove that its isotypic components form a unique orthogonal decomposition and are finite-dimensional. Is finite multiplicity needed for uniqueness? Give an infinite-multiplicity example, and explain why its individual irreducible summands are not unique.

**Solution.** Proposition 4.2 characterizes each \(H_\sigma\) as the closed span of all copies of \(\sigma\), without choosing a decomposition. It therefore forces every grouping by irreducible type to give the same components. Proposition 4.4, or (4.7), gives

\[
\dim H_\sigma=m_\sigma\dim V_\sigma<\infty
\]

when \(m_\sigma\) is finite. The orthogonal sum of those components is all of \(H\). Finite multiplicity ensures this dimension conclusion, but Proposition 4.2 shows uniqueness for arbitrary multiplicities too.

For an infinite-multiplicity example take \(H=\ell^2(\mathbb N)\) and \(\pi(e^{i\theta})=e^{i\theta}I_H\). Every line is an irreducible copy of \(\chi_1\), so \(H_{\chi_1}=H\), all other components are zero, and \(M_{\chi_1}\simeq H\). Its multiplicity is countably infinite. Each orthonormal basis splits \(H\) into irreducible lines. Replacing the first two basis vectors by their normalized sum and difference changes those lines and leaves the unique isotypic component intact. Replacing \(\mathbb N\) by an uncountable index set gives the same example with that Hilbert dimension; the action remains strongly continuous since \(\|(e^{i\theta}-1)v\|=|e^{i\theta}-1|\|v\|\).

## What this lesson does not prove

The following analysis results are used. Each link leads to a full proof with the conditions needed here.

- **Haar measure.** A compact Hausdorff group has a unique normalized left-invariant Radon measure; it is right invariant and positive on nonempty open sets. See [*Haar measure on locally compact groups*](course:harmonic-analysis-on-locally-compact-groups/haar-measure-on-locally-compact-groups#oa-fnd-hm-05), Theorem 8.3, Proposition 9.1, Theorem 9.2, Theorem 10.1(4) and Theorem 11.1. Radon finiteness and positivity on a compact group give finite positive total mass, so normalization is legitimate.
- **Bounded self-adjoint spectral theory.** On any complex Hilbert space a bounded self-adjoint operator \(A\) has a projection-valued spectral measure with \(A=\int\lambda\,dE_A(\lambda)\). Its support is the spectrum, and a bounded operator commuting with \(A\) commutes with every spectral projection. [*The spectral theorem for bounded self-adjoint operators*](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators#oa-fnd-st-03), Theorem 3.1 and Theorem 4.4, supply the full Borel-calculus and spectral-measure proofs. The continuous-calculus input is identified below.
- **Compact spectral theory.** A compact self-adjoint operator on any complex Hilbert space admits an orthonormal basis of eigenvectors. See [*Hilbert spaces and compact operators*](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators#oa-fnd-hs-06), Lemma 6.1 and Theorem 6.2. The nonzero eigenspace bound used here is proved in (2.6). No separability hypothesis is imposed.
- **Translation continuity.** For \(1\le p<\infty\) and \(f\in L^p(G)\), both \(\|L_gf-f\|_p\) and \(\|R_gf-f\|_p\) tend to zero as \(g\to e\). See [*Haar measure on locally compact groups*](course:harmonic-analysis-on-locally-compact-groups/haar-measure-on-locally-compact-groups#oa-fnd-hm-12), Theorem 14.2(6), including its density argument. We use \(p=2\).
- **Hilbert dimension.** Every Hilbert space has an orthonormal basis, and any two such bases have the same cardinality. See [*Hilbert spaces and compact operators*](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators#oa-fnd-hs-04), Theorem 4.1, including finite-subset sums and arbitrary cardinalities.
- **Locally convex functionals.** A nonzero Hausdorff locally convex complex vector space admits a nonzero continuous complex linear functional. For a nonzero vector \(v\), choose a continuous seminorm \(p\) with \(p(v)>0\). On \(\mathbb Cv\), set \(\ell_0(tv)=tp(v)\); then \(|\ell_0|\leq p\). [*Hahn–Banach, Baire and the basic theorems on Banach spaces*](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#oa-fnd-hb-02), Theorem 2.2, extends it to \(\ell\) with \(|\ell|\leq p\), making \(\ell\) continuous and nonzero. This consequence is used only in Corollary 5.7.
- **Real and circle characters.** Every continuous character of \(\mathbb R\) is \(x\mapsto e^{2\pi itx}\) for a unique real \(t\), and every continuous character of \(\mathbb T\) is an integral power. See [*Characters and the dual group*](course:HA-LCA/HA-LCA-02#section-3), Theorem 3.1 and Corollary 3.2. Example 5.1 states the conversion to our angle convention.

### Functional calculus in the spectral proof

For a bounded self-adjoint operator \(h\), apply [*C*-algebras: continuous functional calculus, automatic continuity and positive cones*, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-07) to the unital complex C*-algebra \(B(H)\). Its continuous calculus is isometric: \(\|f(h)\|=\sup_{\lambda\in\sigma(h)}|f(\lambda)|\). Part (6) gives commutation with every operator commuting with both \(h\) and \(h^*\); here \(h=h^*\), so the two requirements coincide. These facts supply the exact isometry and commutation used to establish spectral support in Theorem 4.1. The chapter proves the normal-element norm formula, real self-adjoint spectra, spectral permanence and the commutative Gelfand–Naimark theorem before constructing this calculus.

The Banach-algebra inputs are [*Banach algebras: spectrum, holomorphic functional calculus and Gelfand theory*](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html): Theorem 5.2 (nonempty spectrum in a nontrivial unital complex Banach algebra), Theorem 5.4 (spectral radius), Proposition 10.3 (characters) and Theorem 11.1 (Gelfand representation). These are required foundations of this spectral proof route. Their proofs apply to \(B(H)\) and its commutative unital C*-subalgebras for arbitrary \(H\); neither Hilbert separability nor group metrizability is needed. The linked spectral chapter then constructs the Borel calculus using the included Riesz/Radon and Hilbert-space proofs.

The [compact-averaging proof of Schur’s lemma](https://kokunoyumeto.github.io/open-math-courses-public/courses/representations-of-compact-groups/reader/compact-schur-proof.html) uses Haar integration and the compact self-adjoint spectral theorem through Lemma 2.2, Proposition 2.5 and Theorem 2.7. It supplies a complete alternative to this general functional-calculus route. The trace/predual, C*-GNS and bicommutant chapters linked from the support reader discuss further operator-algebra applications. Their theorems are not inputs to the Schur proof or to the spectral chapter’s Sections 1–4.

Elementary Hilbert-space geometry and scalar integration, including Bessel’s inequality and Fubini’s theorem, are assumed. Zorn’s lemma selects a maximal orthogonal family. Schur orthogonality, the general Peter–Weyl theorem and the general regular-representation multiplicity formula are proved in *Matrix coefficients and the Peter–Weyl theorem*.

## References

### Freely accessible proof comparisons

- **Pavel Etingof**, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/pdf/2201.09397v5), 23 May 2026, accessed 3 October 2026. Lemma 11.9 (printed p. 61) gives finite-dimensional complex Schur; Propositions 11.13–11.14 and Corollary 11.15 (p. 62) give invariant complements and finite-group averaging. Proposition 35.1 and Corollary 35.2 (p. 175) give finite-dimensional averaging and complete reducibility for compact Lie groups. These are checked comparisons for the corresponding finite-dimensional arguments here. Section 37 assumes a countable base, so it is not the proof source for our arbitrary compact Hausdorff scope.
- **Emmanuel Kowalski**, [*An introduction to the representation theory of groups*, author-hosted 2025 edition](https://people.math.ethz.ch/~kowalski/representation-theory-2025.pdf), accessed 3 October 2026. Proposition 2.7.15 (printed p. 67) gives finite-dimensional Schur over an algebraically closed field. The forward averaging argument of Theorem 4.1.1 (pp. 117–118), for fields whose characteristic does not divide the group order, gives the finite-group invariant-complement proof; Theorem 5.2.11(1) (p. 214) gives continuous finite-dimensional compact-group averaging. These passages provide complete comparisons at their stated scope. The arbitrary-Hilbert arguments here retain the full programme analysis proofs linked above.

### Historical sources used in earlier versions

Gruson–Serganova was used in earlier versions, and its source-use locators remain recorded. The current representation-theoretic arguments are proved in this lesson, with the required analysis supplied by the full programme proofs above.

- **[Gruson–Serganova 2018]** Caroline Gruson and Vera Serganova, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Universitext, Springer, 2018. Recorded uses: chapter 3, §1, Theorem 1.1, Definitions 1.5–1.6, Lemma 1.19, Theorem 1.20, Corollaries 1.21–1.28, Theorem 1.29 and Lemma 1.31; §§1.2–1.3 for locally convex and Hilbert-space facts. [Publisher’s record](https://doi.org/10.1007/978-3-319-98271-7).

## Accessible source notes

The free human comparisons above concern the exact finite-dimensional passages listed. The arbitrary compact Hausdorff and arbitrary-Hilbert conclusions have the complete proofs and exact prerequisites stated here. Historical source use is distinguished from the current proof dependencies in the accompanying provenance records.
