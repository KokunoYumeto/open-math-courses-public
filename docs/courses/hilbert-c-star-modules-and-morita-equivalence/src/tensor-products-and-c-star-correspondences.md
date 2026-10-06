# Tensor products and C*-correspondences

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A tensor product can change the coefficient algebra of a Hilbert module. It can also turn a module into a Hilbert space, compose two bimodules, or combine modules over unrelated algebras. These constructions share a positivity mechanism, but their balancing relations are different. Keeping those relations visible prevents a common mistake: an operator on the second factor does not automatically act on an interior tensor product.

We assume the results of Hilbert C*-modules, Adjointable operators, and Compact operators, multipliers and the strict topology. Inner products are linear in the second variable. All coefficient algebras may be nonunital. Basic references are [Li 2024], [Blackadar 1998], [Blackadar 2006] and [Connes 1994]; [Emerson 2024] discusses operator applications.

## 1. The left action is part of the data

**Definition 1.1.** An \(A\)-\(B\) correspondence consists of a right Hilbert \(B\)-module \(F\) and a *-homomorphism
\[
\varphi:A\longrightarrow\mathcal L_B(F).
\]
We write \(ay=\varphi(a)y\). It is nondegenerate when the linear span of \(\varphi(A)F\) is dense in \(F\). We allow degenerate left actions in the tensor construction and state nondegeneracy separately when it is needed.

A homomorphism \(\alpha:A\to M(B)\) gives a correspondence \(F=B_B\), with left action by multiplication. A Hilbert \(B\)-module has its canonical compact left action by \(\mathcal K(F)\); this action is nondegenerate by the compact-action lemma. An ordinary representation \(A\to\mathcal B(H)\) is a correspondence from \(A\) to \(\mathbb C\).

The left action is not generally a left Hilbert-module structure. Correspondences need neither a left inner product nor fullness. Those extra structures enter the later lesson on imprimitivity bimodules.

Let \(E\) be a Hilbert \(A\)-module. Form the balanced algebraic tensor product \(E\odot_A F\) by imposing
\[
xa\odot y=x\odot\varphi(a)y.
\tag{1.1}
\]
It is a right \(B\)-module, with \((x\odot y)b=x\odot(yb)\).

**Theorem 1.2 (Interior tensor product).** The formula
\[
\langle x\odot y,x'\odot y'\rangle
=\langle y,\varphi(\langle x,x'\rangle_A)y'\rangle_B
\tag{1.2}
\]
defines a positive semidefinite \(B\)-valued inner product on the balanced tensor product. Dividing out its null vectors and completing gives a Hilbert \(B\)-module \(E\otimes_\varphi F\).

*Proof.* Before balancing, extend the formula sesquilinearly to finite sums. In the first variable,
\[
\begin{aligned}
\langle xa\odot y,x'\odot y'\rangle
&=\langle y,\varphi(a^*)\varphi(\langle x,x'\rangle)y'\rangle\\
&=\langle\varphi(a)y,\varphi(\langle x,x'\rangle)y'\rangle.
\end{aligned}
\]
This is the value obtained from \(x\odot\varphi(a)y\). The second-variable relation follows either directly or by conjugate symmetry. Hence every balancing generator pairs to zero with every tensor, and the form descends. The right-module identity follows from the corresponding identity in \(F\).

For \(z=\sum_{i=1}^n x_i\odot y_i\), the Gram matrix
\[
G=(\langle x_i,x_j\rangle_A)_{i,j}
\]
is positive in \(M_n(A)\). Applying \(\varphi\) entrywise gives a positive adjointable operator \(\varphi_n(G)\) on \(F^n\): a square root of \(G\) gives a factorization of its image as \(C^*C\). Thus, for \(y=(y_i)\),
\[
\langle z,z\rangle
=\sum_{i,j}\langle y_i,\varphi(G_{ij})y_j\rangle
=\langle y,\varphi_n(G)y\rangle_{F^n}\geq0.
\]
This proves positivity for every finite sum, rather than only for simple tensors.

The null-quotient and completion theorem for pre-Hilbert modules now applies. Null vectors pair to zero by Cauchy–Schwarz, so the quotient form is well defined; the module action and inner product extend continuously to its completion. ∎

The image of a simple tensor satisfies
\[
\|x\otimes y\|\leq\|x\|\|y\|,
\tag{1.3}
\]
because \(0\leq\varphi(\langle x,x\rangle)\leq\|x\|^2 1_F\). It can have norm zero even when its factors are nonzero. The tensor product measures the part of the left action seen by the first module.

**Example 1.3 (The essential part).** Put \(F_{\mathrm{ess}}=\overline{\operatorname{span}}\varphi(A)F\). The formula
\[
U:A^n\otimes_\varphi F\longrightarrow F_{\mathrm{ess}}^n,
\qquad
U((a_i)\otimes y)=(\varphi(a_i)y)_i
\tag{1.4}
\]
is unitary. Balancing follows from multiplicativity. For two simple tensors, their inner product is
\[
\left\langle y,\varphi\!\left(\sum_i a_i^*b_i\right)y'\right\rangle
=\sum_i\langle\varphi(a_i)y,\varphi(b_i)y'\rangle.
\]
Sesquilinearity proves that \(U\) is isometric on all finite sums. Its range contains all coordinate vectors with an entry \(\varphi(a)y\), so it is dense in \(F_{\mathrm{ess}}^n\). The completed isometry has closed range and is onto.

In particular \(A^n\otimes_\varphi F\cong F^n\) when \(\varphi\) is nondegenerate. Without that condition, even \(n=1\) can fail: the zero action of \(\mathbb C\) on the nonzero Hilbert space \(\mathbb C\) gives a zero tensor product. No orthogonal complement for \(F_{\mathrm{ess}}\) is asserted.

## 2. Operators which respect balancing

**Theorem 2.1 (The first factor).** If \(T\in\mathcal L_A(E,E')\), then
\[
(T\otimes1)(x\otimes y)=Tx\otimes y
\]
defines an adjointable map \(E\otimes_\varphi F\to E'\otimes_\varphi F\), with adjoint \(T^*\otimes1\) and norm at most \(\|T\|\). For \(E'=E\), this is a unital *-homomorphism of adjointable operator algebras.

*Proof.* Module linearity makes the formula balanced. For \(z=\sum_i x_i\otimes y_i\), compare the two Gram matrices of \(x_i\) and \(Tx_i\). Their difference
\[
\left(\|T\|^2\langle x_i,x_j\rangle
-\langle Tx_i,Tx_j\rangle\right)_{i,j}
\]
is positive: it is the Gram matrix of
\((\|T\|^2 1_E-T^*T)^{1/2}x_i\). The positive operator exists by the adjointable-operator order theorem. Applying \(\varphi_n\) and testing against \((y_i)\) gives
\[
\langle(T\otimes1)z,(T\otimes1)z\rangle
\leq\|T\|^2\langle z,z\rangle.
\]
The formula therefore preserves null vectors and extends boundedly to the completion. On simple tensors (1.2) gives the adjoint identity with \(T^*\otimes1\); linearity and density extend it to all vectors. Products and the identity act as claimed on simple tensors, hence everywhere. ∎

**Proposition 2.2 (The second factor).** If \(S\in\mathcal L_B(F)\) commutes with \(\varphi(A)\), then
\[
(1\otimes S)(x\otimes y)=x\otimes Sy
\]
defines an adjointable operator of norm at most \(\|S\|\), with adjoint \(1\otimes S^*\).

*Proof.* Commutation makes the formula balanced; taking adjoints shows that \(S^*\) commutes too. For a Gram matrix \(G\), let \(D=\operatorname{diag}(S,\ldots,S)\) on \(F^n\). It commutes with the positive operator \(\varphi_n(G)\) and its square root. Consequently
\[
D^*\varphi_n(G)D
=\varphi_n(G)^{1/2}D^*D\varphi_n(G)^{1/2}
\leq\|S\|^2\varphi_n(G).
\]
Testing this inequality against \((y_i)\) proves the norm estimate and preservation of null vectors. The adjoint identity follows from (1.2) and commutation. ∎

Commutation is a sufficient condition and is necessary if the formula is to work for every first module when \(\varphi\) is nondegenerate. Testing \(E=A\), balancing and (1.4) force
\[
\varphi(b)(\varphi(a)S-S\varphi(a))y=0
\]
for every \(a,b,y\). Apply an approximate identity in place of \(b\). Nondegeneracy makes its action converge to the identity on \(F\), so the commutator vanishes. This argument also covers nonunital \(A\). For a particular first module, some coefficients may be invisible; for example, a zero tensor product places no such requirement.

**Example 2.3 (A formula that is not balanced).** Take \(A=M_2(\mathbb C)\), \(E=A_A\), \(F=\mathbb C^2\), and the defining left action. Let \(S\) be projection onto the first coordinate. With \(a=e_{12}\) and \(y=e_2\), balancing says
\[
a\otimes e_2=1\otimes e_1.
\]
The proposed \(1\otimes S\) sends the left expression to zero and the right expression to \(1\otimes e_1\), which is nonzero under \(A\otimes F\cong F\). The formula is not even well defined on the balanced quotient.

To describe the resulting connection problem precisely, for \(x\in E\) define
\[
R_x:F\to E\otimes_\varphi F,\qquad R_xy=x\otimes y.
\]
It is adjointable, with
\[
R_x^*(z\otimes y)=\varphi(\langle x,z\rangle)y.
\tag{2.1}
\]
Here is the boundedness detail. The map \(R_x\) is bounded by (1.3). For a finite tensor sum \(v\), the candidate on the right of (2.1) satisfies
\(\langle y,R_x^*v\rangle=\langle R_xy,v\rangle\). The norm-duality formula in a Hilbert module therefore gives
\(\|R_x^*v\|\leq\|R_x\|\|v\|\). It extends to the completion, proving the asserted adjoint.

For two modules \(M,N\), write \(\mathcal K(M,N)\) for the norm closure of maps \(z\mapsto u\langle v,z\rangle\), \(u\in N,v\in M\). Adjointable composition on either side preserves these compact maps, by the rank-one formulas.

An ungraded \(S\)-connection is an operator \(G\) on \(E\otimes_\varphi F\) for which
\[
GR_x-R_xS\in\mathcal K(F,E\otimes_\varphi F),\qquad
G^*R_x-R_xS^*\in\mathcal K(F,E\otimes_\varphi F)
\tag{2.2}
\]
for every \(x\). These compact comparison conditions replace exact tensoring of \(S\) in the connection problem used in the Kasparov product. They are not the complete definition of that product, and no existence theorem for connections is asserted here.

**Theorem 2.4 (Compact left actions).** If \(\varphi(A)\subseteq\mathcal K(F)\), then
\[
T\in\mathcal K(E)\quad\Longrightarrow\quad
T\otimes1\in\mathcal K(E\otimes_\varphi F).
\]

*Proof.* We have \(R_x^*R_x=\varphi(\langle x,x\rangle)\), which is compact by assumption. Let \(u_\lambda\) be a positive contractive approximate identity of \(\mathcal K(F)\). Then \(R_xu_\lambda\) is a compact map, and
\[
\|R_x-R_xu_\lambda\|^2
=\|(1-u_\lambda)R_x^*R_x(1-u_\lambda)\|\longrightarrow0.
\]
Thus \(R_x\) is compact. On simple tensors,
\[
(\theta_{x,z}\otimes1)(w\otimes y)
=x\otimes\varphi(\langle z,w\rangle)y
=R_xR_z^*(w\otimes y).
\]
The product is compact. Finite sums and the contractive homomorphism of Theorem 2.1 extend the conclusion to every compact \(T\). ∎

The hypothesis cannot be omitted. Take \(E=\mathbb C\) and \(F\) an infinite-dimensional Hilbert space with the scalar left action. The identity on \(E\) is compact, but its tensor image is the noncompact identity on \(F\).

## 3. Composition, units and coefficient support

**Theorem 3.1 (Associativity).** Let \(F\) be an \(A\)-\(B\) correspondence and \(G\) a \(B\)-\(C\) correspondence with left action \(\psi\). Then
\[
(E\otimes_\varphi F)\otimes_\psi G
\cong E\otimes_A(F\otimes_\psi G)
\tag{3.1}
\]
unitarily, by \((x\otimes y)\otimes z\mapsto x\otimes(y\otimes z)\). The left \(A\)-action on \(F\otimes_\psi G\) is \(\varphi(a)\otimes1\).

*Proof.* Theorem 2.1 provides that left action. Both balancing relations are respected by the displayed map. The inner product of two triple tensors on either side is
\[
\left\langle z,\psi\!\left(
\langle y,\varphi(\langle x,x'\rangle)y'\rangle
\right)z'\right\rangle_C.
\]
Finite sums therefore have identical inner products. Their spans are dense on both sides: approximate a completed intermediate vector by finite tensor sums and use (1.3) to tensor the approximation with a fixed vector. The map descends through null vectors and extends isometrically with dense, hence closed and full, range. ∎

Repeated reassociation is coherent: every composite sends a finite fourfold tensor to the same ordered four factors. Equality on their dense span gives equality of the unitaries. Tensoring also distributes over finite orthogonal direct sums, since expansion of (1.2) gives the summed inner product and the coordinate images have dense span.

**Proposition 3.2 (Units).** The map
\[
E\otimes_A A\longrightarrow E,\quad x\otimes a\longmapsto xa
\tag{3.2}
\]
is unitary, for the standard left action on \(A_A\). For a general correspondence \(F\), the left-unit map \(A\otimes_\varphi F\to F\) has range \(F_{\mathrm{ess}}\), and is unitary onto \(F\) exactly when the left action is nondegenerate.

*Proof.* In (3.2), both inner products are \(a^*\langle x,x'\rangle a'\), so the map is isometric. Its range is dense because the coefficient action is nondegenerate, \(\overline{EA}=E\), proved in the first lesson. Completion makes it onto. The other assertion is Example 1.3 with \(n=1\). ∎

Thus nondegenerate correspondences, up to unitary bimodule isomorphism, form a category with C*-algebras as objects and \(A_A\) as identity. Composition is the interior tensor product. If both left actions are nondegenerate, the composite action is nondegenerate: vectors with first factor in the dense span \(AE\) span a dense subspace of the tensor product. Degenerate correspondences still admit the associative tensor construction, but the usual left identity can fail; one cannot simply include all of them in this category with the same unit law.

Write \(J_E=\overline{\operatorname{span}}\langle E,E\rangle\) for the coefficient ideal.

**Proposition 3.3 (Fullness after tensoring).**
\[
J_{E\otimes_\varphi F}
=\overline{\operatorname{span}}
\{\langle y,\varphi(a)y'\rangle:a\in J_E,\ y,y'\in F\}.
\tag{3.3}
\]
If \(E\) is full and \(\varphi\) is nondegenerate, this is \(J_F\); consequently tensoring a full \(E\) with a full nondegenerate correspondence gives a full module.

*Proof.* Formula (1.2) shows that the left side is the closed span on the right with \(a=\langle x,x'\rangle\). Finite linear combinations and continuity allow exactly every \(a\in J_E\). When \(J_E=A\), density of \(\varphi(A)F\) implies that all inner products \(\langle y,w\rangle\) are limits of this span. This proves equality with \(J_F\). ∎

Fullness of the two underlying right modules alone is insufficient: \(E=A=\mathbb C\) and \(F=\mathbb C\) are full, but the zero left action gives a zero tensor product.

## 4. Hilbert-space localization and induction

Let \(\pi:A\to\mathcal B(H)\) be a representation. Regard \(H\) as a Hilbert \(\mathbb C\)-module. Theorem 1.2 then produces the Hilbert space \(E\otimes_\pi H\); Theorem 2.1 gives a representation
\[
\pi_E:\mathcal L(E)\to\mathcal B(E\otimes_\pi H),
\qquad T\mapsto T\otimes1.
\]

**Theorem 4.1.** If \(\pi\) is faithful, then \(\pi_E\) is faithful and
\[
\|T\otimes1\|=\|T\|.
\tag{4.1}
\]

*Proof.* If \(T\otimes1=0\), then for every \(x\in E,h\in H\),
\[
0=\|Tx\otimes h\|^2
=\langle h,\pi(\langle Tx,Tx\rangle)h\rangle.
\]
This positive operator has zero quadratic form, so it is zero. Faithfulness of \(\pi\) gives \(\langle Tx,Tx\rangle=0\), and hence \(Tx=0\). Thus the homomorphism is injective, and the C*-algebra isometry theorem gives (4.1). No fullness of \(E\) is needed. ∎

For a state \(\omega\), use its GNS triple \((H_\omega,\pi_\omega,\Omega_\omega)\), with scalar inner product linear in the second variable. The map
\[
x\longmapsto x\otimes\Omega_\omega
\]
has squared norm \(\omega(\langle x,x\rangle)\). Its image is dense, because cyclicity and balancing turn \(x\otimes\pi_\omega(a)\Omega_\omega\) into \(xa\otimes\Omega_\omega\). It therefore identifies \(E\otimes_{\pi_\omega}H_\omega\) with the state-localized Hilbert space obtained by null quotient and completion in *Adjointable operators*. Under this identification the operator representations agree. A single GNS representation need not be faithful; the equality of norms in (4.1) uses faithfulness, whereas the supremum over all state localizations always recovers the norm.

For an \(A\)-\(B\) correspondence \(F\) and a representation \(\rho:B\to\mathcal B(H)\), define
\[
\operatorname{Ind}_F(\rho)(a)=\varphi(a)\otimes1
\quad\text{on }F\otimes_\rho H.
\tag{4.2}
\]
This is a representation by Theorem 2.1. It is nondegenerate when the left action on \(F\) is nondegenerate, because the dense span of \(AF\) yields a dense span of induced vectors.

Induction is a functor on representations and bounded intertwiners. If \(V:H\to H'\) intertwines \(\rho,\rho'\), put
\((1\otimes V)(x\otimes h)=x\otimes Vh\).
To verify its norm bound, use the positive matrix \(\rho_n((\langle x_i,x_j\rangle))\) on \(H^n\). The diagonal operator with entries \(V^*V\) commutes with this matrix and is at most \(\|V\|^2\) times the identity, because \(V^*V\) commutes with \(\rho(B)\). The same square-root calculation as Proposition 2.2 proves the bound \(\|1\otimes V\|\leq\|V\|\). Balancing and the adjoint identity with \(V^*\) follow from intertwining. Identities and composition are verified on simple tensors. Associativity identifies induction through a tensor product of correspondences with successive induction.

**Example 4.2 (Tensoring bundles).** Let \(V,W\) be Hermitian vector bundles over compact Hausdorff \(X\). With pointwise left multiplication on \(\Gamma(W)\), the map
\[
\Gamma(V)\otimes_{C(X)}\Gamma(W)\longrightarrow
\Gamma(V\otimes W),\quad s\otimes t\longmapsto
(x\mapsto s(x)\otimes t(x))
\]
preserves inner products by the tensor-product metric on each fibre. It is onto. Indeed take a finite Parseval frame \(s_i\) for \(\Gamma(V)\), supplied by the preceding lesson. For any section \(u\) of \(V\otimes W\), define
\[
t_i(x)=(\langle s_i(x),\,\cdot\,\rangle\otimes1)u(x).
\]
These are continuous sections of \(W\), and the fibrewise frame identity gives \(u=\sum_i s_i\otimes t_i\). Thus the completed isometry is unitary.

## 5. Exterior tensor products and compact operators

We first establish the spatial norm facts needed for the exterior completion. The representation prerequisite is Representations and positive functionals: the GNS construction and the Gelfand–Naimark theorem, Proposition 1.5, Theorems 5.4–5.5 and Theorem 7.2: representations decompose into cyclic parts, positive functionals have their cyclic representations, and every C*-algebra has a faithful representation.

**Lemma (Hilbert-space tensors and the spatial norm).** For bounded Hilbert-space operators, \(T\otimes S\) extends to the completed Hilbert tensor product, has adjoint \(T^*\otimes S^*\), and has norm \(\|T\|\|S\|\). For C*-algebras \(A,B\), every pair of faithful representations computes the same norm on \(A\odot B\), the minimal spatial tensor norm.

*Proof.* A finite tensor sum is contained in the tensor product of two finite-dimensional subspaces. Choosing orthonormal bases there makes its tensor inner product the ordinary coefficient Euclidean inner product, proving positivity and definiteness. On finite sums, expand the second factor in an orthonormal basis to get \(\|(T\otimes1)\xi\|\leq\|T\|\|\xi\|\); expanding the first gives the analogous estimate for \(1\otimes S\). Their composition extends boundedly with the upper product bound. Unit elementary tensors whose factors nearly attain the two operator norms give the lower bound. The adjoint identity follows on elementary tensors, hence on their dense span and completion.

For the algebraic spatial norm, take the supremum over pairs of representations. This is finite, bounded by \(\sum_j\|a_j\|\|b_j\|\) for \(z=\sum_ja_j\otimes b_j\). It is a C*-norm: the C*-identity holds in each operator representation; a faithful pair is algebraically injective, because finite linearly independent operator coefficients can be separated by vector functionals. Cyclic decomposition reduces this supremum to pairs of GNS representations of states. In a cyclic pair, the vectors obtained by applying algebraic tensors \(w\) to the product cyclic vector are dense. Its squared operator norm is therefore the supremum of
\[
\frac{(\varphi\otimes\psi)(w^*z^*zw)}
{(\varphi\otimes\psi)(w^*w)},
\tag{5.0}
\]
over states and positive denominators.

Fix a faithful nondegenerate pair \(\pi,\sigma\), and set \(c=\|(\pi\odot\sigma)(z)\|\). In either faithful representation, convex combinations of unit-vector states are weak-* dense in all states. Otherwise Hahn–Banach separation produces a self-adjoint element whose value at a missing state exceeds its supremum on unit vectors. That supremum is its upper spectral bound, preserved by faithfulness, so no state can exceed it. For nonunital algebras, apply this argument to the canonical minimal unitization and its faithful representation; restriction yields the same conclusion. For unital algebras use the algebra itself.

Product vector states satisfy
\[
(\varphi\otimes\psi)(w^*z^*zw)
\leq c^2(\varphi\otimes\psi)(w^*w).
\]
Taking finite convex combinations in both factors and then their weak-* limits preserves this inequality: the two expressions involve only finitely many coefficient evaluations. It consequently holds for all pairs of states. Formula (5.0) bounds the supremum over all representations by \(c\); the reverse inequality is part of its definition. Thus every faithful nondegenerate pair realizes the same norm. A degenerate faithful representation has a faithful nondegenerate active summand, giving the same norms. If either algebra is zero the assertion is immediate. ∎

The spatial-norm argument is also developed in *Tensor norms and independent systems*, Theorem 3.1; that programme proof is original CC0 writing. The argument above supplies the bridge here, with the module course's inner-product convention. Historical references include Blackadar, II.9.1.3.

Here \(E\) is a Hilbert \(A\)-module and \(F\) a Hilbert \(B\)-module, with no left action prescribed. Their exterior tensor product, written \(E\boxtimes F\), has coefficient algebra \(A\otimes_{\min}B\).

On \(E\odot_{\mathbb C}F\), define the action of \(A\odot B\) componentwise and set
\[
\langle x\odot y,x'\odot y'\rangle
=\langle x,x'\rangle_A\otimes\langle y,y'\rangle_B.
\tag{5.1}
\]
We justify both positivity and the completion over the completed coefficient algebra.

For a finite list of elementary tensors, let \(G_E,G_F\) be the two positive Gram matrices. Their tensor product is positive in \(M_{n^2}(A\otimes_{\min}B)\): tensor their square roots to get a factorization \(C^*C\). Compress to the diagonal index pairs \((i,i)\). The resulting matrix has entries
\(\langle x_i,x_j\rangle\otimes\langle y_i,y_j\rangle\) and is positive. Multiplication on both sides by the scalar column with all entries one shows positivity of (5.1) on a finite tensor sum. For vectors \(z_\alpha=\sum_i x_{\alpha i}\odot y_{\alpha i}\), apply the same construction to the combined index \((\alpha,i)\), obtaining a positive matrix \(H\). The scalar rectangular matrix \(C_{(\alpha,i),\beta}=\delta_{\alpha\beta}\) satisfies
\[
(C^*HC)_{\alpha\beta}=\langle z_\alpha,z_\beta\rangle.
\]
Thus every Gram matrix of finite sums is positive.

A positive two-by-two Gram matrix gives Cauchy–Schwarz without requiring an action by inverses outside \(A\odot B\). In fact, for
\(\begin{pmatrix}a&c\\c^*&b\end{pmatrix}\geq0\), add \(\varepsilon1\) to its upper-left entry and multiply on both sides by the column
\((-(a+\varepsilon1)^{-1}c,1)^t\) and its adjoint in the coefficient unitization. Positivity gives
\[
c^*(a+\varepsilon1)^{-1}c\leq b.
\]
Since \((a+\varepsilon1)^{-1}\geq(\|a\|+\varepsilon)^{-1}1\), this implies \(c^*c\leq(\|a\|+\varepsilon)b\); let \(\varepsilon\) decrease to zero. Hence \(\|c\|\leq\|a\|^{1/2}\|b\|^{1/2}\). The triangle inequality, null quotient and continuous inner product now follow just as for pre-Hilbert modules.

For an algebraic coefficient \(d\in A\odot B\), compatibility gives
\[
\|zd\|^2=\|d^*\langle z,z\rangle d\|
\leq\|d\|_{\min}^2\|z\|^2.
\]
Complete the null quotient first. This estimate extends its coefficient action uniquely from the dense algebra \(A\odot B\) to \(A\otimes_{\min}B\). The extended identities and positive inner product make it a Hilbert module \(E\boxtimes F\). In particular
\(\|x\boxtimes y\|=\|x\|\|y\|\), using the spatial cross norm.

**Theorem 5.1 (Exterior compact algebra).**
\[
\mathcal K(E)\otimes_{\min}\mathcal K(F)
\cong\mathcal K(E\boxtimes F),
\tag{5.2}
\]
by the map
\[
\theta_{x,x'}\otimes\theta_{y,y'}
\longmapsto\theta_{x\boxtimes y,x'\boxtimes y'}.
\tag{5.3}
\]

*Proof.* Choose faithful nondegenerate representations \(\rho\) of \(A\) on \(H\) and \(\sigma\) of \(B\) on \(K\). Their existence is a C*-algebra prerequisite. Put \(H_E=E\otimes_\rho H\), \(K_F=F\otimes_\sigma K\). The localized representations of \(\mathcal L(E)\) and \(\mathcal L(F)\) are faithful by Theorem 4.1.

For \(x\in E\), the bounded map \(r_x:H\to H_E\), \(h\mapsto x\otimes h\), satisfies
\[
r_x^*r_{x'}=\rho(\langle x,x'\rangle).
\]
This follows from the adjoint construction (2.1); define \(s_y:K\to K_F\) similarly. For \(z=\sum_i x_i\boxtimes y_i\), set
\[
R_z=\sum_i r_{x_i}\otimes s_{y_i}:H\otimes K\to H_E\otimes K_F.
\]
Then
\[
R_z^*R_z=(\rho\otimes\sigma)(\langle z,z\rangle).
\tag{5.4}
\]
Faithfulness of the spatial coefficient representation gives \(\|R_z\|=\|z\|\), so this map extends to completed vectors.

For \(u=\sum_j T_j\otimes S_j\) in the algebraic tensor product of the two adjointable algebras, its componentwise action on \(z\) satisfies
\[
R_{uz}=\left(\sum_j(T_j\otimes1_H)\otimes(S_j\otimes1_K)\right)R_z.
\]
The faithful spatial representations show that the operator in parentheses has norm \(\|u\|_{\min}\). Thus \(\|uz\|\leq\|u\|_{\min}\|z\|\). Adjoints act componentwise by (5.1). We obtain a *-homomorphism
\[
\mathcal L(E)\otimes_{\min}\mathcal L(F)
\longrightarrow\mathcal L(E\boxtimes F).
\]
It is injective: if the image of \(u\) is zero, (5.4) shows that its faithful spatial representation annihilates every \(R_z(h\otimes k)\). Their span is dense in \(H_E\otimes K_F\), since it contains \((x\otimes h)\otimes(y\otimes k)\). Hence that spatial operator, and then \(u\), is zero. The argument extends from algebraic \(u\) by norm continuity.

Restrict to the compact algebras. Direct substitution gives (5.3), so their tensor product maps into \(\mathcal K(E\boxtimes F)\). Every vector of the exterior product is approximated by finite tensor sums. The estimate
\[
\|\theta_{\xi,\eta}-\theta_{\xi',\eta'}\|
\leq\|\xi-\xi'\|\|\eta\|+\|\xi'\|\|\eta-\eta'\|
\]
shows that their rank-one operators are approximated by sums of the operators in (5.3). The injective *-homomorphism is isometric, so its range is closed; density therefore proves surjectivity. ∎

No nuclearity, fullness or countability is needed in (5.2). Specifying the minimal tensor norm is essential to the faithful spatial-representation argument.

**Example 5.2 (The standard module).** The map from finite sums in
\(\ell^2\boxtimes A\) to \(H_A\) sending \(e_j\boxtimes a\) to the column with entry \(a\) in coordinate \(j\) preserves the inner product \(\sum_j a_j^*b_j\). Its range contains all finite columns, dense in \(H_A\). Hence
\[
\ell^2\boxtimes A\cong H_A.
\]
Theorem 5.1 then recovers \(\mathcal K(H_A)\cong\mathbb K\otimes_{\min}A\).

## 6. Exercises with solutions

**Exercise 6.1 (Basic: columns).** Identify \(A^n\otimes_\varphi F\), including a degenerate left action.

*Solution.* Map \((a_i)\otimes y\) to \((\varphi(a_i)y)_i\). Multiplicativity proves balancing, and the equality of inner products in (1.4) proves isometry for all finite sums. Single-coordinate vectors \((0,\ldots,a,\ldots,0)\otimes y\) span a dense image in \(F_{\mathrm{ess}}^n\). Completion therefore gives a unitary onto that module. For a nondegenerate action it is \(F^n\). The zero action on nonzero \(F\) gives zero instead, proving that the nondegeneracy condition cannot be dropped. ∎

**Exercise 6.2 (Interior positivity).** Prove positivity of the inner product of a finite balanced tensor sum, and explain why testing simple tensors is insufficient.

*Solution.* For \(z=\sum_i x_i\otimes y_i\), the Gram matrix \(G=(\langle x_i,x_j\rangle)\) is positive. Its entrywise image under the *-homomorphism is positive on \(F^n\); writing \(G=C^*C\) proves this directly. Therefore \(\langle z,z\rangle=\langle(y_i),\varphi_n(G)(y_i)\rangle\geq0\). The balancing check in Theorem 1.2 makes this independent of representatives. The cross terms \(i\ne j\) are part of the squared norm of a sum, so positivity on individual simple tensors alone would not establish positivity of the form. Null vectors are then removed before completion. ∎

**Exercise 6.3 (An undefined operator).** Give a bounded adjointable \(S\) for which \(x\otimes y\mapsto x\otimes Sy\) does not respect balancing.

*Solution.* Use \(E=M_2(\mathbb C)\), \(F=\mathbb C^2\), the defining left action, and \(S=\operatorname{diag}(1,0)\). Both sides of \(e_{12}\otimes e_2=1\otimes e_1\) represent \(e_1\) under the unit identification. Applying the proposed formula to the first representative gives zero; applying it to the second gives \(e_1\). The map is therefore undefined on the quotient. The obstruction is \(Se_{12}\ne e_{12}S\), not lack of boundedness or an adjoint. ∎

**Exercise 6.4 (Faithful localization).** Show that localization through a faithful representation preserves the norm of every adjointable operator.

*Solution.* Theorem 1.2 gives a complete scalar-inner-product space, hence a Hilbert space. If \(T\otimes1=0\), then \(\langle h,\pi(\langle Tx,Tx\rangle)h\rangle=0\) for every \(x,h\). Positivity and faithfulness imply \(\langle Tx,Tx\rangle=0\), so \(T=0\). Thus the contractive *-homomorphism on adjointable operators is injective and isometric. For comparison, evaluation at zero on \(A=C[0,1]\) kills the nonzero multiplication operator by the coordinate \(t\); faithfulness really is needed for this conclusion about a single localization. ∎

**Exercise 6.5 (Exterior compacts).** Prove (5.2), paying attention to its tensor norm.

*Solution.* Faithful coefficient representations localize \(E,F\) to Hilbert spaces with faithful adjointable-operator representations. Formula (5.4) embeds each completed exterior-module vector as an operator between the spatial tensor Hilbert spaces. It gives the norm bound for the action of the minimal tensor product of the two compact algebras. If that action vanishes, its faithful spatial representation vanishes on the dense span of \((x\otimes h)\otimes(y\otimes k)\), proving injectivity. Finally the rank-one product identity (5.3) puts the algebraic image in the compact algebra. Approximate arbitrary exterior-module vectors by finite tensor sums and apply the rank-one norm estimate in Theorem 5.1; the image is dense. Injectivity makes the image closed, so it is all the compact algebra. This proves the isomorphism with the minimal norm, without an assumption of nuclearity. ∎

## What this lesson does not prove

We use the preceding course proofs of Gram positivity, null quotient and completion, adjointable operator order estimates, compact approximate identities and the isometry of injective C*-homomorphisms.

The representation prerequisites are the cyclic decomposition, GNS construction and faithful representation theorem in *Representations and positive functionals*, Proposition 1.5, Theorems 5.4–5.5 and Theorem 7.2. The Hilbert-space tensor operator norm and independence of faithful spatial representations are proved in the opening lemma of Section 5. Blackadar II.6.4, II.9.1.3 and I.2.5 provide historical treatments.

The compact bundle example uses the frame constructed in *Finite projective modules, frames and K₀*. We do not construct geometric groupoid correspondences, prove existence of Kasparov connections, or prove an equivalence of representation categories: the latter requires an imprimitivity bimodule and will be developed later.

## References

[Li 2024] Y. Li, *Groupoid C*-algebras*, [Leiden Noncommutative Geometry Seminar notes](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), updated 2024, Section 4.2 for correspondences and their composition.

[Connes 1994] Alain Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter II, Appendix A, Proposition 6. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).

[Blackadar 1998] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, Section 13.5. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

[Blackadar 2006] Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006, II.7.4 for interior tensor products and correspondences, and II.9.1 for spatial tensor products. [Author's revised edition](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).

[Emerson 2024] Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, Section 5.5 for Hilbert-module operators and tensor-product applications.
