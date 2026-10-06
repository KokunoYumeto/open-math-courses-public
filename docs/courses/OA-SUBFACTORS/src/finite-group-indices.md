# A finite symmetry group gives two kinds of index

An outer action of a finite group produces an inclusion by taking fixed points and another by adjoining the group unitaries. Both indices count cosets. The first calculation uses the projection that averages the symmetry; the second uses an actual basis of coset unitaries.

We assume [A projection that remembers an inclusion](projection-and-basic-construction.md), [Measuring an inclusion through modules and corners](module-dimension-and-local-index.md), and [Finite bases, bounded vectors and a positive-operator inequality](finite-bases-and-positive-index.md). For crossed products we use the regular representation displayed in the section “Crossed products by discrete groups” of Injective von Neumann algebras. The finite-group Fourier and index arguments are developed below. References are [Jones] and [Watatani].

Let \(M\) be a II₁ factor and \(\alpha:G\to\operatorname{Aut}(M)\) an action of a finite group. Its automorphisms preserve the normalized trace. The action is **outer** if \(\alpha_g\) is not implemented by a unitary of \(M\) for every \(g\ne e\). For a subgroup \(H\), write \(M^H\) for its fixed algebra.

## The finite Fourier expansion

On \(\ell^2(G,L^2(M))\), use the regular coefficient representation and group unitaries

\[
(\pi(a)\xi)(t)=\alpha_{t^{-1}}(a)\xi(t),\qquad
(u_g\xi)(t)=\xi(g^{-1}t).
\tag{18.1}
\]

They satisfy \(u_g\pi(a)u_g^*=\pi(\alpha_g(a))\). We suppress \(\pi\) when writing coefficients.

**Lemma 18.1.** Every element of \(B=M\rtimes_\alpha G\) has a unique finite expansion

\[
x=\sum_{g\in G}a_gu_g,\qquad a_g\in M.
\tag{18.2}
\]

The map \(E_M(x)=a_e\) is a faithful normal conditional expectation. The formula \(\tau_B(x)=\tau_M(a_e)\) is a faithful normal tracial state, with

\[
\|x\|_{2,B}^2=\sum_{g\in G}\|a_g\|_{2,M}^2.
\tag{18.3}
\]

**Proof.** In the regular representation, the \((t,s)\) matrix entry of (18.2) is \(\alpha_{t^{-1}}(a_{ts^{-1}})\). Thus the \((e,g^{-1})\) entry recovers \(a_g\), proving uniqueness and \(\|a_g\|\leq\|x\|\). The matrices whose entries have this form constitute an ultraweakly closed linear subspace: their entries belong to the ultraweakly closed coefficient algebra, and the equalities between entries use only normal automorphisms. Finite sums are closed under products and adjoints by the covariance relation. They therefore form the whole generated von Neumann algebra, proving existence.

The \((e,e)\) compression is a normal completely positive map and returns \(a_e\). It is unital and \(M\)-bimodular. If \(x\geq0\) and \(a_e=0\), all diagonal entries of \(x\) vanish. Positivity of each two-by-two operator corner then forces all off-diagonal entries to vanish as well. Thus this expectation is faithful.

The coefficient of the identity in a product is

\[
E_M(xy)=\sum_g a_g\alpha_g(b_{g^{-1}}).
\]

Trace invariance and cyclicity turn its trace into \(\sum_h\tau_M(b_h\alpha_h(a_{h^{-1}}))\), the trace of \(yx\). This proves traciality. Applying the same coefficient rule to \(x^*x\) gives (18.3), proving positivity and faithfulness of the trace; normality follows from the compression. \(\square\)

## Outerness makes the crossed product a factor

**Lemma 18.2.** If the action is outer, then \(M'\cap B=\mathbb C1\), so \(B\) is a II₁ factor.

**Proof.** If \(x=\sum_g a_gu_g\) commutes with every \(b\in M\), uniqueness of coefficients gives

\[
a_g\alpha_g(b)=ba_g\quad(b\in M).
\tag{18.4}
\]

If \(a_g\ne0\), its two absolute squares commute with the relevant copies of \(M\), by (18.4) and its adjoint. Factoriality makes both squares positive scalars; their traces make the scalars equal. Thus \(a_g\) is a nonzero scalar multiple of a unitary \(v\), and (18.4) says \(\alpha_g(b)=v^*bv\). For \(g\ne e\) this contradicts outerness, so only \(a_e\) survives. It is scalar. This proves the relative-commutant assertion, which contains the center of \(B\). The faithful trace makes \(B\) finite, and its subalgebra \(M\) is diffuse, excluding a matrix factor. \(\square\)

## Cosets form a unitary basis

**Theorem 18.3.** For an outer action and any subgroup \(H\subseteq G\),

\[
[M\rtimes G:M\rtimes H]=[G:H].
\tag{18.5}
\]

**Proof.** The restricted action is outer, so both crossed products are II₁ factors. The trace-preserving expectation onto \(M\rtimes H\) retains exactly the coefficients whose group labels belong to \(H\): this follows by the orthogonality (18.3) and the trace-pairing characterization of the expectation.

Choose one representative \(t\) for each left coset \(tH\). Distinct representatives satisfy

\[
E_{M\rtimes H}(u_s^*u_t)=\delta_{st}1.
\]

For \(g=th\), the term \(a_gu_g\) is

\[
u_t\bigl(\alpha_{t^{-1}}(a_g)u_h\bigr).
\]

This supplies the exact right-module expansion

\[
x=\sum_{t\in G/H}u_tE_{M\rtimes H}(u_t^*x).
\tag{18.6}
\]

The basis is orthonormal and all its entries are unitaries. Its module unitary identifies \(L^2(M\rtimes G)\) over \(M\rtimes H\) with \([G:H]\) copies of the standard module, by the norm calculation of Corollary 3.4. Their dimension is \([G:H]\), proving (18.5). \(\square\)

## The averaging projection computes the fixed-point index

On \(L^2(M)\), let \(U_g\widehat x=\widehat{\alpha_g(x)}\). These unitaries normalize both the left and right coefficient algebras. Put \(P=M^G\) and

\[
f=\frac1{|G|}\sum_{g\in G}U_g.
\tag{18.7}
\]

This is the orthogonal projection onto the fixed vectors. The normal trace-preserving expectation \(E_P(x)=|G|^{-1}\sum_g\alpha_g(x)\) shows that its range is \(L^2(P)\).

**Theorem 18.4.** For an outer action, \(M^G\) is a II₁ factor and

\[
[M:M^G]=|G|,\qquad
[M^H:M^G]=[G:H].
\tag{18.8}
\]

**Proof.** Apply Lemmas 18.1–18.2 to the induced action on the right coefficient factor \(R(M)\cong M^{\mathrm{op}}\). It is outer: a right-unitary implementation would, on taking opposites, implement \(\alpha_g\) by a unitary of \(M\). Its crossed product \(A=R(M)\rtimes G\) is therefore a finite factor.

The covariant pair \(R(M),U_g\) defines a normal unital representation \(\sigma\) of this finite crossed product on \(L^2(M)\). Here is a direct verification of its boundedness, avoiding any identification of this representation with the regular one. Send \(\sum_g a_gu_g\) to \(\sum_g a_gU_g\). This is an algebraic *-homomorphism, and

\[
\left\|\sum_g a_gU_g\right\|
\leq\sum_g\|a_g\|\leq|G|\left\|\sum_g a_gu_g\right\|.
\]

Lemma 18.1 makes the algebraic domain the entire von Neumann algebra \(A\). Each recovered coefficient map and its represented right action is normal, so the finite sum defines a normal homomorphism. Its kernel is a central ideal of the factor \(A\); unitality makes it faithful. Its image is consequently the von Neumann algebra generated by \(R(M)\) and \(U(G)\).

The commutant of this image is

\[
R(M)'\cap U(G)'=M\cap U(G)'=P.
\]

Hence \(P\) is a factor: its center equals the center of its factor commutant. It is finite as a subalgebra of \(M\). Normal representation comparison realizes it as a corner of an amplification of \(A^{\mathrm{op}}\), a II factor, so it is not a matrix factor. Thus \(P\) is II₁.

The basic construction of \(P\subseteq M\) is \(R(P)'\). Since the group unitaries commute with tracial conjugation, \(J\sigma(A)J\) is generated by \(M\) and \(U(G)\); it is \(R(P)'\). Equivalently \(\langle M,f\rangle=R(P)'\), by the basic-construction theorem, and the group-average projection belongs to this finite factor. Its normalized trace is \(1/|G|\), since the faithful crossed-product representation transports the trace of the group average in the regular algebra, whose only identity coefficient is \(1/|G|\). Conjugation by \(J\) preserves this trace on self-adjoint elements, and fixes \(f\).

The canonical basic-construction trace has value one on \(f\). Its normalized version therefore gives

\[
[M:P]^{-1}=\tau_1(f)=|G|^{-1}.
\]

This proves the first formula. Apply it to the restricted \(H\)-action to get \([M:M^H]=|H|\), then use index multiplicativity in \(M^G\subseteq M^H\subseteq M\). It yields the second formula in (18.8). \(\square\)

## An explicit outer action

For a finite group \(G\) with \(|G|\geq2\), take the tracial infinite tensor product

\[
M=\overline{\bigotimes_{n\geq1}M_{|G|}(\mathbb C)}^{\,\mathrm{weak}}
\]

and on each tensor coordinate act by the left regular permutation representation of \(G\). The product action is outer. To prove this, let \(p_n\) be the rank-one projection labelled by the identity in coordinate \(n\). For \(g\ne e\), its image is the orthogonal projection labelled by \(g\), so

\[
\|\alpha_g(p_n)-p_n\|_2=\sqrt{2/|G|}.
\tag{18.9}
\]

If \(\alpha_g=\operatorname{Ad}v\) for a unitary \(v\in M\), approximate \(v\) in \(L^2\) by an element \(a\) of a finite tensor prefix. For later \(n\), \([a,p_n]=0\), and

\[
\|\alpha_g(p_n)-p_n\|_2=\|[v,p_n]\|_2
\leq2\|v-a\|_2.
\]

Arbitrarily good approximation contradicts (18.9). The tensor product is a II₁ factor: expectations onto finite full matrix prefixes approximate every central element and make each expected central element scalar. The trace is faithful and the increasing matrix sizes exclude finite type I. This constructs the required action on the separable hyperfinite II₁ factor.

For the trivial group, use the identity action on any II₁ factor; its outerness condition has no nonidentity element to test, and both index formulas give one.

For \(G=S_3\) and \(H\) a subgroup generated by one transposition, the subgroup has order two and index three. Both inclusions in (18.5) and the second formula of (18.8) have index three; the fixed-point inclusion \(M^{S_3}\subseteq M\) has index six.

## Exercises

**Exercise 18.1 — introductory.** For \(G=\mathbb Z/6\mathbb Z\) and its subgroup of order three, list a coset-unitary basis and compute both subgroup indices.

**Solution.** Representatives are zero and one. The crossed-product basis is \(1,u_1\), and both \([M\rtimes G:M\rtimes H]\) and \([M^H:M^G]\) are two. The ambient fixed-point index is six, while \([M:M^H]=3\).

**Exercise 18.2 — intermediate.** Why does a trivial action fail the factor argument?

**Solution.** Every \(u_g\) then commutes with \(M\), so \(M'\cap(M\rtimes G)\) contains the finite group algebra rather than only scalars. Also \(M^G=M\), whose fixed-point index is one rather than \(|G|\). Outerness is essential to the fixed-point conclusion.

**Exercise 18.3 — intermediate.** In (18.6), explain why right coefficients require representatives of \(tH\), rather than merely switching to \(Ht\) in the same formula.

**Solution.** The expression \(u_t b\), with \(b\in M\rtimes H\), has group labels \(th\). Thus its support is in \(tH\). For representatives of \(Ht\), the corresponding expansion places the subgroup coefficients on the left, and its expectation formula changes accordingly. The two numbers of cosets agree, but the module conventions must be retained.

**Exercise 18.4 — advanced.** Derive \((M^G)'=\langle R(M),U(G)\rangle\) on \(L^2(M)\), and distinguish it from the basic construction.

**Solution.** The proof of Theorem 18.4 identifies the commutant of \(\sigma(A)=\langle R(M),U(G)\rangle\) with \(M^G\). Taking the second commutant gives the asserted equality. The basic construction is \(R(M^G)'=J(M^G)'J\), hence \(\langle M,U(G)\rangle\), with \(f\) its Jones projection. The first formula uses the left fixed algebra's commutant; the second uses the right fixed action's commutant. Both have normalized trace \(1/|G|\) on \(f\).

## References

- Vaughan F. R. Jones, [*Index for subfactors*](https://doi.org/10.1007/BF01389127), Inventiones Mathematicae 72 (1983), 1–25.
- Yasuo Watatani, [*Index for C*-subalgebras*](https://doi.org/10.1090/memo/0424), Memoirs of the American Mathematical Society 83 (1990), no. 424.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Self-checked by the writing AI. Public domain (CC0).*
