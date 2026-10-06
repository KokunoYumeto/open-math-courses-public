# Index selection and uniform multiplier control

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

A double sequence has a row index for an element of \(M^\omega\) and a column index for its representative in \(M\). Index selection chooses a row slowly while the column follows the ultrafilter. To produce an element of the nontracial multiplier quotient, the rows need common multiplier moduli. Separate membership of every row is insufficient.

We prove the general construction with that uniform control, and then the full finite-trace version, where the control is automatic. An explicit type I example shows why the unrestricted source assertion cannot hold.

Let \(M\) have separable predual and a faithful normal state \(\varphi\). Use \(M^\omega=N_\omega/I_\omega\), \(M_\omega=C_\omega/I_\omega\), \(E_\omega\), and \(\|\cdot\|_\#=\|\cdot\|_{\varphi,\#}\) from the preceding lessons.

## 1. Why arbitrary rows are not enough

**Proposition 1.1.** Even for a two-dimensional unital \(C^*\)-algebra \(A\subset\ell^\infty(\mathbb N,M^\omega)\) and the trivial action group, a homomorphism \(\Psi:A\to M^\omega\) fixing constant sequences need not exist with
\[
E_\omega(\Psi((X_m)))
=\operatorname*{uw-lim}_{m\to\omega}E_\omega(X_m).
\tag{1}
\]

**Proof.** Take \(M=B(\ell^2(\mathbb N_0))\). The [type I multiplier theorem](multiplier-ultraproducts-and-normal-embeddings.md#theorem-7-2) identifies \(M^\omega\) normally with constant \(M\); under that identification \(E_\omega=\mathrm{id}\).

Let \(w_m\) exchange \(\xi_0\) and \(\xi_m\) and fix all other basis vectors. Then
\[
w_m=1-p_0-p_m+|\xi_m\rangle\langle\xi_0|
                   +|\xi_0\rangle\langle\xi_m|,
\qquad w_m=w_m^*,\quad w_m^2=1.
\tag{2}
\]
The tail projection and off-diagonal terms converge ultraweakly to zero, so
\[
\operatorname*{uw-lim}_{m\to\omega}w_m=1-p_0.
\tag{3}
\]
For the off-diagonal terms, each fixed pair of vectors gives a coefficient tending to zero; uniform boundedness extends weak operator convergence to ultraweak convergence on this bounded sequence by trace-class approximation.

View each \(w_m\) as a constant element of \(M^\omega\), and put \(w=(w_m)\), \(A=C^*(1,w)\). This is a unital copy of \(\mathbb C^2\): \(w\) is a self-adjoint unitary different from either scalar sign. Fixing constants requires \(\Psi(1)=1\), so any *-homomorphism makes \(\Psi(w)\) a self-adjoint unitary. But (1) and \(E_\omega=\mathrm{id}\) force \(\Psi(w)=1-p_0\), whose square is not \(1\). This is impossible. \(\square\)

This meets the separability and trivial-action hypotheses of Ocneanu's Index Selection Trick in Section 5.5. The obstruction is to the theorem itself, rather than just one choice of diagonal.

## 2. A uniform row hypothesis

Let \(A\subset\ell^\infty(\mathbb N,M^\omega)\) be separable and unital. Write \(a=(X_m^a)\). Let \(H\) be a countable group of actual semi-lifts acting on \(A\) term by term:
\[
(\gamma a)_m=\gamma(X_m^a),\qquad
\gamma(\pi(x_k))=\pi(\gamma_k(x_k)).
\tag{4}
\]
Assume \(A\) is invariant. The family \(\gamma_k\) in the second formula is indexed by the representative column, not the outer row.

Choose a countable norm-dense unital rational *-algebra \(D\subset A\), invariant under \(H\). Arrange that \(D\) has norm-dense intersections with the closed subalgebras of constant sequences and of sequences all of whose rows belong to \(M_\omega\). These subalgebras are separable as closed subspaces of \(A\), so their dense generators can be included before taking all countable translates.

For each \(a\in D\) choose representatives
\[
x_m^a(k)\in N_\omega,\qquad
\pi(x_m^a)=X_m^a,\qquad
\|x_m^a(k)\|\le\|a\|_A.
\tag{5}
\]
For a constant row sequence \(X_m^a=X\), use the same representative \(u_X(k)\) for every row. For a sequence of centralizing quotient elements, use centralizing representatives in each row.

The additional uniform control is this: for each \(a\in D,l\ge1\), there are a positive \(\delta_l(a)\), an outer set \(R_l(a)\in\omega\), and inner sets \(W_l(a,m)\in\omega\) for \(m\in R_l(a)\), such that
\[
\begin{gathered}
m\in R_l(a),\quad k\in W_l(a,m),\quad
\|z\|\le1,\quad\|z\|_\#<\delta_l(a)\\
\Longrightarrow\
\|x_m^a(k)z\|_\#+\|zx_m^a(k)\|_\#<1/l.
\end{gathered}
\tag{6}
\]
The modulus is independent of the row. The sets can be made decreasing with \(l\) by finite intersections. Separate row membership would only give a modulus depending on both \(l\) and \(m\); that weaker information does not supply (6).

**Theorem 2.1.** Under (4)–(6), there is a unital *-homomorphism \(\Psi:A\to M^\omega\) such that:
\[
\begin{aligned}
E_\omega(\Psi(a))&=\operatorname*{uw-lim}_{m\to\omega}E_\omega(X_m^a),\\
\Psi(a)&=X&&\text{if }X_m^a=X\text{ for every }m,\\
\Psi(a)&\in M_\omega&&\text{if }X_m^a\in M_\omega\text{ for every }m,\\
\Psi(\gamma a)&=\gamma(\Psi(a))&&(\gamma\in H).
\end{aligned}
\tag{7}
\]
Injectivity is not asserted for an arbitrary \(A\). Its exact kernel will be described below.

## 3. Selecting rows, then column sets

Let \(D_n,H_n\) be increasing finite exhausting sets, with \(1\in D_n\), and let \(\psi_j\) be norm dense in \(M_*\). Put
\[
L(a)=\operatorname*{uw-lim}_{m\to\omega}E_\omega(X_m^a).
\tag{8}
\]
Each limit exists by bounded ultraweak compactness.

At stage \(n\), choose a row \(r(n)\ge n\) in all \(R_l(a)\) for \(a\in D_n,l\le n\), and satisfying
\[
|\psi_j(E_\omega(X_{r(n)}^a)-L(a))|<1/n,
\qquad a\in D_n,\ j\le n.
\tag{9}
\]
These are finitely many outer ultrafilter conditions, so their intersection is nonempty.

Having fixed that row, choose decreasing inner sets \(V_n\in\omega\), inside \(\{k\ge n\}\) and all \(W_l(a,r(n))\) for \(a\in D_n,l\le n\). Require on \(V_n\):

1. Every addition, adjoint, multiplication and rational scalar relation on the finite data has symmetric seminorm error less than \(1/n\).
2. For \(a\in D_n,j\le n\),
\[
|\psi_j(x_{r(n)}^a(k)-E_\omega(X_{r(n)}^a))|<1/n.
\tag{10}
\]
3. For \(a\in D_n,\gamma\in H_n\),
\[
\|\gamma_k(x_{r(n)}^a(k))-x_{r(n)}^{\gamma a}(k)\|_\#<1/n.
\tag{11}
\]
4. For a centralizing-row sequence \(a\in D_n\) and \(j\le n\),
\[
\|[x_{r(n)}^a(k),\psi_j]\|<1/n.
\tag{12}
\]

**Lemma 3.1.** These inner sets exist.

**Proof.** Every algebraic relation holds in the fixed row quotient, so its representative error is in \(I_\omega\). Equation (10) uses its ultraweak-limit expectation. For (11), the two representatives give the same row element \(\gamma(X_{r(n)}^a)=X_{r(n)}^{\gamma a}\), by (4). Equation (12) uses the centralizing representative of that row. Each finite test therefore holds on an inner \(\omega\)-large set. Intersect these with the finitely many uniform-modulus sets, the previous \(V_{n-1}\), and the cofinite set. \(\square\)

The moduli in this intersection are the fixed \(\delta_l(a)\) of (6). A new modulus shrinking with \(r(n)\) would not give the subsequent multiplier proof.

## 4. The diagonal and its full extension

Set \(V_0=\mathbb N\), and let \(s(k)\) be the largest \(n\ge1\) with \(k\in V_n\), or zero if none. Since \(V_n\subset\{k\ge n\}\), the level is finite; since every \(V_n\) is large, \(s(k)\to_\omega\infty\). Define
\[
y_a(k)=x_{r(s(k))}^a(k),\qquad \Psi_0(a)=\pi(y_a),
\tag{13}
\]
using \(r(0)=1\) on the initial band.

**Lemma 4.1.** Each \(y_a\) belongs to \(N_\omega\).

**Proof.** Fix \(a,l\). On an \(\omega\)-large set the level \(n=s(k)\) is high enough that \(a\in D_n,l\le n\). Its row \(r(n)\) lies in \(R_l(a)\), and its actual column \(k\in V_n\) lies in \(W_l(a,r(n))\). Thus (6) controls both products at that coordinate with the same fixed \(\delta_l(a)\).

For a contraction sequence \(z_k\in I_\omega\), the condition \(\|z_k\|_\#<\delta_l(a)\) holds on another large set. Both product seminorms have ultralimit at most \(1/l\). Let \(l\to\infty\), and rescale bounded null sequences. This proves both multiplier conditions. \(\square\)

The relation tests make \(\Psi_0\) a unital rational *-homomorphism, and (5) gives \(\|\Psi_0(a)\|\le\|a\|_A\). It extends by norm continuity to a complex unital *-homomorphism on \(A\).

Combining (9) and (10) gives scalar expectation errors below \(2/s(k)\), hence the first line of (7) on \(D\). The map \(L:A\to M\) is linear and contractive: these properties hold coordinatewise for the expectations and survive scalar ultralimits. Thus both sides extend by norm continuity to \(A\).

Constant sequences are fixed on \(D\) because their row representatives were chosen identical, making (13) exactly \(u_X(k)\). Norm density in the constant subalgebra extends this conclusion. Equation (12) gives centralizing images on the dense centralizing-row subalgebra; \(M_\omega\) is norm closed, so the entire centralizing-row subalgebra has its image there.

Finally (11) compares \(\gamma_k(y_a(k))\) with \(y_{\gamma a}(k)\) at the actual column \(k\). It gives equivariance on \(D\), and norm continuity gives it on \(A\). These arguments prove Theorem 2.1.

Define the state
\[
\rho(a)=\varphi(L(a))
=\lim_{m\to\omega}\varphi^\omega(X_m^a).
\tag{14}
\]
The expectation identity implies \(\varphi^\omega\Psi=\rho\). Faithfulness of \(\varphi^\omega\) then gives the exact formula
\[
\ker\Psi=\{a\in A:\rho(a^*a)=0\}.
\tag{15}
\]
Indeed \(\rho(a^*a)=\varphi^\omega(\Psi(a)^*\Psi(a))\) vanishes precisely when \(\Psi(a)=0\). In particular a faithful \(\rho\) makes this selection injective.

## 5. The full finite-trace version

**Corollary 5.1.** Suppose \(M\) has separable predual and a faithful normal tracial state \(\tau\). For every separable unital \(A\subset\ell^\infty(\mathbb N,M^\omega)\) invariant under a countable semi-lift group acting as in (4), a map satisfying all of (7) exists. No factor hypothesis is needed.

**Proof.** Use \(\varphi=\tau\). Every bounded sequence in \(M\) is an inner multiplier. Choose contractive row representatives as in (5); for constants use identical representatives, and for centralizing rows choose centralizing ones. For a contraction \(z\),
\[
\|x_m^a(k)z\|_2+\|zx_m^a(k)\|_2
\le2\|a\|_A\|z\|_2.
\tag{16}
\]
Thus (6) holds with \(R_l(a)=W_l(a,m)=\mathbb N\) and, for example,
\(\delta_l(a)=(4l(1+\|a\|_A))^{-1}\). All countable algebra, action and intersection data can be chosen as above, so Theorem 2.1 applies. \(\square\)

Here (15) becomes
\[
\ker\Psi
=\{a=(X_m^a)\in A:\lim_{m\to\omega}\|X_m^a\|_{\tau^\omega,2}=0\}.
\tag{17}
\]
Consequently the selection embeds the \(C^*\)-quotient by this trace-null ideal into \(M^\omega\), preserving its trace. In particular it fixes every constant \(X\in M^\omega\) whose constant sequence belongs to \(A\). This is the full tracial diagonal-selection phenomenon, including nonfactor finite algebras.

The general hypothesis (6) fails intrinsically in Proposition 1.1. Use the diagonal state (13) of the [ordinary multiplier lesson](ordinary-multipliers-and-predual-compactness.md). Its \(\|p_m\|_\#^2=\lambda_m\) tends to zero, whereas
\[
p_mw_m=|\xi_m\rangle\langle\xi_0|,
\qquad \|p_mw_m\|_\#^2=(\lambda_0+\lambda_m)/2\ge1/4.
\tag{18}
\]
For any representatives of the constant row element \(w_m\), taking the inner ultralimit preserves these fixed-row product seminorms, since multiplication by \(p_m\) is fixed within that row. Thus no common small-input modulus can hold for unbounded \(m\) in an outer ultrafilter set. Merely requiring each individual row to be a multiplier leaves precisely this gap.

## 6. Exercises with complete solutions

**Exercise 1.** Verify the swap formula (2).

*Solution.* On \(\xi_0\), its first three terms give zero and the term \(|\xi_m\rangle\langle\xi_0|\) gives \(\xi_m\). On \(\xi_m\) it gives \(\xi_0\), and on every other basis vector it gives that same vector. Thus it is the stated self-adjoint permutation unitary, with square \(1\).

**Exercise 2.** Why is the ultraweak limit in (3) not unitary?

*Solution.* It annihilates \(\xi_0\) and fixes the orthogonal complement, so it is the proper projection \(1-p_0\). Its square is itself, which differs from \(1\). A unital homomorphism cannot send the unitary \(w\) to it.

**Exercise 3.** Explain why \(A=C^*(1,w)\) is already a separable counterexample.

*Solution.* The relation \(w=w^*,w^2=1\) makes its continuous functional calculus a quotient of \(\mathbb C^2\). Both spectral projections \((1\pm w)/2\) are nonzero because every swap has both signs in its spectrum. Hence the algebra is exactly \(\mathbb C^2\), finite-dimensional and separable.

**Exercise 4.** Distinguish the row and column actions in (4).

*Solution.* The outer action sends row \(X_m\) to the same actual automorphism \(\gamma(X_m)\). Within its representative, that action is implemented by \(\gamma_k\) at column \(k\). Equation (11) therefore uses \(\gamma_k\), with the row \(r(n)\) held fixed. Replacing it by \(\gamma_{r(n)}\) would apply a different rule.

**Exercise 5.** Why do the row choices satisfy (9)?

*Solution.* For each fixed \(a,j\), the scalar \(\psi_j(E_\omega(X_m^a))\) has ultralimit \(\psi_j(L(a))\). Its error below \(1/n\) is therefore an outer large-set condition. At stage \(n\) only finitely many such conditions and row-modulus sets are intersected, together with a cofinite set.

**Exercise 6.** Why is the uniform modulus independent of the selected row essential?

*Solution.* A null input has small seminorm relative to every fixed positive threshold on a large set. It need not be small relative to thresholds that shrink with its coordinate. Lemma 4.1 needs one fixed \(\delta_l(a)\) while its selected rows vary. A row-dependent threshold cannot justify that step; the swaps in (18) exhibit its failure.

**Exercise 7.** Prove centralizing membership of the selected image.

*Solution.* For a sequence of centralizing rows, (12) bounds every fixed \(\psi_j\)-commutator by \(1/s(k)\) on a large set. Levels tend to infinity along \(\omega\). Uniform operator bounds and norm density extend the convergence to every normal functional. This is exactly membership in \(C_\omega\).

**Exercise 8.** Check constant fixing for an element of \(M^\omega\), whose inner representative may vary.

*Solution.* If every row equals \(X\), choose \(x_m(k)=u_X(k)\) independently of \(m\). The selected diagonal in (13) is then \(u_X(k)\) at every coordinate, even though that representative varies with \(k\). Its quotient is precisely \(X\).

**Exercise 9.** Derive the kernel formula (15).

*Solution.* Multiplicativity and the state identity give \(\rho(a^*a)=\varphi^\omega(\Psi(a)^*\Psi(a))\). If \(\Psi(a)=0\), the value is zero. Conversely faithfulness of the target state makes a positive square with zero state vanish, so \(\Psi(a)=0\). Both implications prove the formula.

**Exercise 10.** Establish the uniform row modulus in the finite-trace case.

*Solution.* The trace \(2\)-norm satisfies \(\|bz\|_2,\|zb\|_2\le\|b\|\|z\|_2\). The representatives have a common bound \(\|a\|_A\), so their sum is at most \(2\|a\|_A\|z\|_2\), regardless of row or column. The positive modulus in Corollary 5.1 therefore works on all indices.

**Exercise 11.** Why is injectivity inappropriate for arbitrary sequence algebras?

*Solution.* A nonzero sequence can have row \(2\)-norm tending to zero along the outer filter. For instance a sequence supported at just one row is nonzero in \(\ell^\infty\) but trace-null for a free filter. Equation (17) forces the selection to annihilate it. The correct injective object is the quotient by that ideal.

**Exercise 12.** Show that a different choice of representatives cannot repair the swap counterexample's common-modulus failure.

*Solution.* For each fixed row \(m\), an alternative representative differs from the constant \(w_m\) by an inner null sequence. Multiplication by the fixed \(p_m\) preserves that nullity, so its inner product seminorm has ultralimit equal to the value in (18). For unbounded \(m\), the input \(\|p_m\|_\#\) is arbitrarily small but the output remains at least \(1/2\). This contradicts any fixed modulus on an outer large set.

## References

Adrian Ocneanu's freely accessible [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), thesis, Chapter 5, Section 5.5, Index Selection Trick, printed pp.56–58 (PDF pp.70–72), is the comparison source for the row and column selection. Its unrestricted nontracial assertion is not used as a theorem provider: Proposition 1.1 satisfies its separability and trivial-action hypotheses and contradicts its expectation and constant-fixing conclusions.

The source's condition (6) places a selected column inside a multiplier-control set for the selected row. Separate rows can have different small-input moduli, so this does not give the common modulus required to prove that the final diagonal is a multiplier. Condition (6) of this lesson makes the missing uniform row control explicit, and Sections 3–4 prove the complete corrected construction. Corollary 5.1 proves the entire finite-trace case, including finite algebras with nontrivial center, where the common control is automatic. The final estimates also show why the type I example cannot satisfy that additional hypothesis. No source expression is imported.
