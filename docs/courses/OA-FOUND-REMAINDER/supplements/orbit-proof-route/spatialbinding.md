<span id="exact-spatial-tensor-bindings-for-bf77-and-the-haar-tensor-commutant"></span>
# Tensor commutants and arbitrary representation amplification

[Spatial tensor products](../../reader/supplements/spatial-tensor-products.html) proves the tensor commutant theorem on arbitrary Hilbert spaces. The application below combines it with representation amplification, a normal slice and the Haar multiplication algebra.

The spatial tensor product theorem proves

\[
(M\bar\otimes N)'=M'\bar\otimes N'
\]

for concrete von Neumann algebras on arbitrary Hilbert spaces, in **Theorem 11.4, equation (11.1)**. Consequently, if \(\mathcal D\subseteq B(K_0)\) is already a multiplication MASA, then

\[
(M'\bar\otimes\mathcal D)'=M''\bar\otimes\mathcal D'
=M\bar\otimes\mathcal D.
\tag{T}
\]

This closes the precise `TENSOR.COMMUTANT` application. The tensor theorem has no standard-form, faithful-state, weight, modular-operator, Haar-measure or semifiniteness hypothesis. Haar analysis is needed to establish that the actual multiplication algebra used in the application is \(\mathcal D\) and satisfies \(\mathcal D'=\mathcal D\). It is a separate proof. The Haar result is proved in [Haar multiplication and its maximal abelian algebra](../../reader/orbit-proof-route/support.html#orbit-bridge-haar-masa).

<span id="exact-existing-provider-and-proof-bodies"></span>
## Tensor results used in the argument

The required results are proved in [Spatial tensor products](../../reader/supplements/spatial-tensor-products.html) at the following sections:

| Required fact | Full existing proof | Proof section |
| --- | --- | --- |
| Arbitrary orthonormal-basis columns; product-vector totality; tensor adjoints | Proposition 1.3 | [The Hilbert tensor product](../../reader/supplements/spatial-tensor-products.html#1-the-hilbert-tensor-product) |
| Matrix entries, commutation, bounded finite-subset truncations | Proposition 2.1(2)–(5) | [Tensor products of operators and operator matrices](../../reader/supplements/spatial-tensor-products.html#2-tensor-products-of-operators-and-operator-matrices) |
| Normal amplification; bounded strong continuity; positive normal vector series | Proposition 3.1 | [Normal functionals and amplification](../../reader/supplements/spatial-tensor-products.html#3-normal-functionals-and-the-amplification) |
| Bicommutant and normal extension from generators | Lemma 4.1, Theorem 4.2, Proposition 4.3 | [Bicommutants and normal extension](../../reader/supplements/spatial-tensor-products.html#4-the-bicommutant-theorem-and-the-normal-extension-principle) |
| Generated tensor algebra; amplification; matrices over a von Neumann algebra | Theorem 5.2(2), (4), (5) | [The spatial tensor product](../../reader/supplements/spatial-tensor-products.html#5-the-spatial-tensor-product) |
| Reduced and induced corner commutants; tensor corners | Proposition 6.1 | [Reduced and induced algebras](../../reader/supplements/spatial-tensor-products.html#6-reduced-and-induced-algebras) |
| \((A\otimes1)'=A'\bar\otimes B(L)\) and \((A\bar\otimes B(L))'=A'\otimes1\) | Proposition 7.1, equation (7.1) | [Tensor products with B(K), commutants and matrix units](../../reader/supplements/spatial-tensor-products.html#7-tensor-products-with-bk-commutants-and-matrix-units) |
| Associativity, flip, spatial transport, normal leg maps | Proposition 8.1 | [Tensor maps and normal homomorphisms](../../reader/supplements/spatial-tensor-products.html#8-maps-between-tensor-products-and-normal-homomorphisms) |
| Tensoring normal homomorphisms and isomorphisms with given normal inverses | Theorem 8.2, Corollary 8.4 | Same Section 8 anchor |
| Slice membership, norm, module laws, normality, both legs and Fubini | Lemma 9.1, Theorem 9.2 | [Slice maps](../../reader/supplements/spatial-tensor-products.html#9-slice-maps) |
| Product normal functionals and norm-density/separation | Theorem 10.1(1)–(2) | [Product functionals and the predual](../../reader/supplements/spatial-tensor-products.html#10-product-functionals-and-the-predual) |
| General tensor commutation, intersections, centres and slice criterion | Lemmas 11.1–11.3, Theorem 11.4, Corollary 11.5 | [The commutation theorem and its consequences](../../reader/supplements/spatial-tensor-products.html#11-the-commutation-theorem-and-its-consequences) |

Theorem 10.1(3), concerning the norm of restriction to the algebraic tensor product, separately uses the published Kaplansky and closed-predual providers; Theorem 10.1(4), concerning supports, separately uses the published normal-functional support provider. Neither part is needed for BF77 E8–E9 or (T). Those two parts have additional prerequisites beyond the tensor commutant and slice arguments used here.

Theorem 10.1(2) proves more than separation: every normal functional on the spatial tensor product is approximated in norm by finite sums of product vector functionals. Its proof restricts a square-summable vector-pair series, truncates its tail, approximates each of the finitely many vectors by finite sums of product vectors, and expands sesquilinearly. No separability of either Hilbert space follows from a countable series representing one functional. For separation itself, if all product vector pairings of an operator vanish, product-vector totality gives that the operator is zero. Theorem 11.4 also supplies the double-polarization proof that vanishing of all complex diagonal product-vector pairings suffices.

<span id="why-the-general-tensor-theorem-has-the-required-scope"></span>
## Why the general tensor theorem has the required scope

The full argument in Section 11 is independent of modular theory. Lemma 11.1 gives real orthogonality of \(M_h\xi\) and \(iM'_h\xi\). Lemma 11.2(b) proves the corresponding density for a cyclic vector by a two-by-two projection matrix in \(M'\bar\otimes B(\mathbb C^2)\), using the previously proved matrix commutant. It does not assume a faithful state or a separating vector for \(M\); cyclicity only implies the separating property for \(M'\) used in that argument.

Lemma 11.3 proves the tensor density statement for real subspaces. A real-orthogonal obstruction defines a bounded conjugate-linear map \(t\); its positive complex-linear square \(t't\) is treated by real-polynomial approximation to the square root of its square. The two orthogonality conditions force \(t=0\), so the obstruction is zero. This uses bounded continuous functional calculus and real Hilbert-space projection/Riesz theory, not a Tomita involution.

Theorem 11.4 first applies these lemmas when the two factors have cyclic vectors. In the general case it fixes an arbitrary product vector \(\xi\otimes\eta\), compresses to \([M\xi]\otimes[N\eta]\), and uses Proposition 6.1 to identify the induced and reduced commutants on that corner. The cyclic theorem makes the two compressed test operators commute. Equality of the original diagonal pairings follows because the corner fixes the product vector and one test operator commutes with the corner. Double complex polarization then gives equality on all pairs of product vectors and hence everywhere. This is a vector-by-vector corner argument; it does not require a countable family of cyclic corners. It includes arbitrary cardinality and the trivial zero-space case.

Thus the exact incoming mathematical chain for (T) is the ordinary Hilbert-space/functional-calculus foundation together with the supplement's matrix, bicommutant, corner, and Section 11 proofs. `MF.COMMUTANT` and `TENSOR.CONSTRUCTION` are not needed for (T). The modular argument provides an alternative route; the tensor equality here uses the bounded Hilbert-space and corner arguments just described.

<span id="complete-application-to-bf77-e3e9"></span>
## Complete application to BF77 E3–E9

Let \(\rho_i:M\to B(K_i)\) be faithful normal unital representations of nonzero \(M\). BF77 E1–E2 already constructs reducing intertwining isometries by implementing each cyclic normal positive functional as a countable vector series. The positive-vector-series result is Theorem 10.1 with Lemma 1.2(b) of [The double commutant theorem](../../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html). The normal image and inverse correspondence is Proposition 12.1 of [The universal enveloping von Neumann algebra of a C*-algebra and W*-algebras](../../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-19). The supplement's Proposition 3.1(4) also supplies a fully written arbitrary-Hilbert-space positive-vector-series theorem; it is an available alternative, to that double-commutant argument. Both proofs use their stated Hilbert-space and operator-topology prerequisites.

Choose an infinite cardinal \(\kappa\geq\max(\aleph_0,|I_1|,|I_2|)\), where \(I_i\) index the reducing cyclic decompositions, and put \(L=\ell^2(\kappa)\). Amplifying an embedding into \(K_j\otimes\ell^2(I_i\times\mathbb N)\) by \(L\), and using \(\kappa\cdot|I_i|\cdot\aleph_0=\kappa\), gives reducing intertwining isometries both ways between \(L\otimes K_1\) and \(L\otimes K_2\). A unitary on these multiplicity spaces commutes with the coefficient representation. This is E3; no countable cyclic decomposition is assumed.

For E4–E5, use the representation Cantor–Bernstein construction actually written in BF77. For intertwining isometries \(i:H_1\to H_2\), \(j:H_2\to H_1\), put \(q=ji\), \(A=H_1\ominus jH_2\), and \(E=\bigoplus_{n\geq0}q^nA\). These subspaces reduce the representations; the summands are orthogonal because \(A\perp qH_1\). Since \(E=A\oplus qE\),

\[
j(H_2\ominus iE)=(H_1\ominus A)\ominus qE=H_1\ominus E.
\]

Therefore \(i\) on \(E\) and \(j^*\) on \(H_1\ominus E\) combine into a surjective intertwining isometry. This produces the E5 unitary on the amplified spaces. The use of a countable orbit of one isometry in this construction does not restrict either Hilbert dimension.

For the tensor application, write \(K_0=L^2(G)\) and set

\[
P_\rho=(\pi_{\alpha,\rho}(M)\cup\lambda(G))'',\qquad
A_\rho=(\rho(M)'\otimes1\ \cup\ \{V_g\otimes R_g:g\in G\})''.
\]

BF75 I5 is the distinct standard-representation input \(P_\pi'=A_\pi\). It requires the coefficient Hilbert algebra and its closed polar conjugation. The tensor argument below assumes that input has been supplied; tensor theory itself cannot establish it.

For any von Neumann algebra \(A\subseteq B(Q)\), Proposition 7.1 followed by the flip gives

\[
(1_L\otimes A)'=B(L)\bar\otimes A'.
\tag{A1}
\]

The proof chooses an arbitrary orthonormal basis of \(L\), places matrix entries in \(A'\), and compresses to finite basis subsets. Each compression lies in \(B(L)\odot A'\), has norm at most that of the original operator, and the net of these compressions converges strongly. Strong closure yields the required inclusion; elementary tensors give the reverse inclusion. This is a proof by a net of finite subsets, with no basis enumeration.

In the coordinate order \(L\otimes H\otimes K_0\), the amplified regular algebra is \(1_L\otimes P_\pi\): regular coefficient and group generators are the original generators with \(1_L\) added, and Theorem 5.2(4) identifies their double commutant. Its proposed commutant generator algebra is exactly

\[
\begin{aligned}
Q_0
&=((B(L)\bar\otimes\pi(M)')\otimes1\ \cup\
\{1_L\otimes U_g\otimes R_g:g\in G\})''\\
&=(B(L)\otimes1\otimes1\ \cup\ 1_L\otimes A_\pi)''
=B(L)\bar\otimes A_\pi.
\end{aligned}
\]

Here (A1) identifies the coefficient commutant; Proposition 8.1(1) identifies the three tensor legs; Theorem 5.2(2) and Proposition 4.3 identify generation after adjoining the multiplicity algebra. Therefore BF75 I5 gives

\[
(1_L\otimes P_\pi)'=B(L)\bar\otimes P_\pi'
=B(L)\bar\otimes A_\pi=Q_0.
\tag{A2}
\]

Let the E5 unitary \(T:L\otimes K\to L\otimes H\) transport \(1_L\otimes\rho\) to \(\sigma=1_L\otimes\pi\), and write \(\widehat V_g=T(1_L\otimes V_g)T^*\). Both \(\widehat V_g\) and \(U_g^{L}=1_L\otimes U_g\) implement \(\alpha_g\) on \(\sigma(M)\). Direct covariance gives

\[
w_g\sigma(x)w_g^*=\sigma(x),\qquad
w_g=\widehat V_g(U_g^L)^*,
\]

so \(w_g\in\sigma(M)'\), as asserted in E7. Moreover

\[
\widehat V_g\otimes R_g=(w_g\otimes1)(U_g^L\otimes R_g).
\]

Multiplying by \(w_g^*\otimes1\) gives the converse expression. Thus replacing the implementers in \(Q_0\) preserves the generated algebra. This argument does not require \(w_g\) to be a representation: its membership in the coefficient commutant is sufficient for both inclusions.

Transport by \(T\otimes1_{K_0}\) carries every regular coefficient generator and every left translation to the corresponding generator for \(\sigma\). Proposition 8.1(4) and bounded equality on product vectors justify this spatial transport. After transport back, (A2) becomes precisely

\[
B(L)\bar\otimes P_\rho'=B(L)\bar\otimes A_\rho,
\tag{E8}
\]

because the coefficient commutant is \(B(L)\bar\otimes\rho(M)'\), and the remaining generators are \(1_L\otimes(V_g\otimes R_g)\). Theorem 5.2(2) makes this last generated algebra \(B(L)\bar\otimes A_\rho\).

Finally fix a unit vector \(e\in L\). Put \(W_e\xi=e\otimes\xi\). Theorem 9.2(4) gives the normal first-leg slice

\[
s_e(X)=(\omega_e\otimes\iota)(X)=W_e^*XW_e,
\qquad s_e(B(L)\bar\otimes A)\subseteq A,
\qquad s_e(1_L\otimes x)=x.
\tag{A3}
\]

Membership also follows directly: \(W_ey=(1_L\otimes y)W_e\) for \(y\in A'\), so the compression commutes with \(A'\) and belongs to \(A''=A\). For normality, each normal vector-pair series on the output pulls back to the square-summable pairs \((e\otimes\xi_n,e\otimes\eta_n)\). This is valid on arbitrary \(L\) and \(Q\). Applying (A3) to \(1_L\otimes x\) in each direction of E8 gives

\[
P_\rho'=A_\rho,
\tag{E9}
\]

with the claimed full arbitrary-multiplicity scope. In fact membership and the elementary-tensor identity already suffice to cancel the amplification; the written slice provider additionally proves normality.

If \(K=0\), both concrete algebras in E9 are \(\{0\}\), and the equality is immediate. If \(M\ne0\) and \(\rho\) is faithful unital, \(K\ne0\). The multiplicity space used above is always nonzero. For a nonfaithful normal unital representation, BF77's invariant central-kernel quotient argument is a separate step. This preserves the distinction between the general concrete commutant formula and the abstract quotient crossed product in E10.

<span id="integration-delta-and-remaining-distinctions"></span>
## Distinct tensor-weight identities

The tensor commutant identity uses the spatial theorem and the Haar multiplication MASA theorem. The amplification and cancellation argument uses Proposition 7.1, the generator and flip identities, and Theorem 9.2 on slices. The direct matrix-and-compression argument also gives this amplification and slice calculation.

[The regular crossed-product commutant in arbitrary representations](../../reader/orbit-proof-route/owned-4.html) applies the amplified generating-algebra equality before E8. It uses the positive vector-series theorem, permits general locally compact groups, retains the central-kernel quotient for nonfaithful representations, and requires the standard commutant identity of BF75.

This result does not close `TENSOR.NATURALITY` for all-positive tensor weights, `TENSOR.COCYCLE`, or the general original-weight/relative-Tomita chain. Those are mathematically different assertions. No full proof of them is supplied by Theorem 11.4. Conversely they must not be imported as prerequisites of (T). The bounded tensor arguments and the distinct BF75 modular argument have the different mathematical premises stated above.
