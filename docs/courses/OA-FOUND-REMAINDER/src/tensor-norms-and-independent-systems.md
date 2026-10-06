# Tensor norms and independent systems

*Self-checked by the writing AI. Original text: CC0 1.0.*

Two algebras of observables can act on separate Hilbert spaces, or they can act on one Hilbert space with commuting ranges. These constructions answer different questions. The spatial tensor product records separate actions. The maximal tensor product allows every commuting action. Their comparison is a useful way to measure independence.

This lesson assumes the GNS construction, approximate identities, continuous functional calculus and the Hilbert tensor product. The proof inputs are the [GNS construction](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#OA-FND-GN-05), the [directed approximate-identity construction](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-19), [operator tensors and their exact norm](../reader/supplements/spatial-tensor-products.html#2-tensor-products-of-operators-and-operator-matrices), and [Stinespring's theorem, including the commutant action](../../foundations-of-von-neumann-algebras/completely-positive-maps.html#OA-FND-CM-05). The bounded-functional estimate needed in Section 4 is the [polar-decomposition theorem](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-03). These programme results are used under their stated background assumptions.

Freely readable treatments are Courtney, Gillaspy and Ismert’s *Notes on C\*-algebras* and Blackadar’s *Operator Algebras*. Sections 1 and 4 prove nonunital recovery and maximal completely positive tensoring. Section 3 uses arbitrary representations and weak-* approximation. Section 5 gives the explicit pairing for algebraic matrix order. Here \(A\odot B\) means the algebraic tensor product. Its multiplication and involution satisfy
\[
(a\otimes b)(c\otimes d)=ac\otimes bd,
\qquad (a\otimes b)^*=a^*\otimes b^*.
\]
No separability assumption is made. Hilbert-space inner products are linear in the first variable.

## 1. Recovering the two actions

For unital algebras, a unital representation \(r:A\odot B\to B(L)\) determines commuting representations by \(r_A(a)=r(a\otimes1)\) and \(r_B(b)=r(1\otimes b)\). Approximate identities supply the same construction when units are absent.

**Theorem 1.1.** Every nondegenerate algebraic *-representation \(r\) of \(A\odot B\) on a Hilbert space \(L\) has unique commuting nondegenerate *-representations \(r_A,r_B\) such that
\[
r(a\otimes b)=r_A(a)r_B(b).
\]
For positive contractive approximate identities \((e_i)\) in \(A\) and \((f_j)\) in \(B\),
\[
r_A(a)=\operatorname{s-lim}_j r(a\otimes f_j),
\qquad
r_B(b)=\operatorname{s-lim}_i r(e_i\otimes b).
\]

**Proof.** On the dense subspace \(D=\operatorname{span}r(A\odot B)L\), define
\[
T_a\Big(\sum_k r(c_k\otimes d_k)\xi_k\Big)
=\sum_k r(ac_k\otimes d_k)\xi_k.
\]
To prove this is well defined and bounded, fix the indicated finite sum \(v\). On the unitization \(\widetilde A\), put
\[
F(x)=\sum_{k,l}
\langle r(xc_k\otimes d_k)\xi_k,
r(c_l\otimes d_l)\xi_l\rangle.
\]
Every factor \(xc_k\) belongs to \(A\). Multiplication and the adjoint identity for \(r\) give
\[
F(x^*x)=\Big\|\sum_k r(xc_k\otimes d_k)\xi_k\Big\|^2\ge0.
\]
Thus \(F\) is a positive functional on the unital C*-algebra \(\widetilde A\). Positivity gives \(F(a^*a)\le\|a\|^2F(1)\), so \(\|T_av\|\le\|a\|\|v\|\). In particular, a zero presentation of \(v\) produces zero. Extend \(T_a\) to \(L\).

The identities \(T_aT_c=T_{ac}\) and \(T_a^*=T_{a^*}\) follow on \(D\) and then on \(L\). The construction in the other factor gives bounded operators \(S_b\). On \(D\), \(T_aS_b=S_bT_a=r(a\otimes b)\). If every \(T_a\) annihilates \(\xi\), then every \(r(a\otimes b)\) annihilates \(\xi\); nondegeneracy of \(r\) implies \(\xi=0\). Hence \(a\mapsto T_a\) is nondegenerate, as is \(b\mapsto S_b\). Their approximate identities converge strongly to \(1\), proving the limit formulas. Those formulas also prove uniqueness. \(\square\)

An arbitrary representation first splits as a nondegenerate representation on \(\overline{r(A\odot B)L}\) and the zero representation on its orthogonal complement. Theorem 1.1 applies on the first summand. Uniqueness on the zero summand requires choosing both recovered representations to be zero.

## 2. Two norms from two kinds of representation

Choose faithful representations \(\pi:A\to B(H)\) and \(\sigma:B\to B(K)\). On \(A\odot B\), the operator
\[
(\pi\odot\sigma)\Big(\sum_i a_i\otimes b_i\Big)
=\sum_i\pi(a_i)\otimes\sigma(b_i)
\]
is well defined. The algebraic map is injective: if the \(b_i\) are linearly independent, matrix coefficients of \(\sigma(B)\) separate their finite-dimensional span, so applying suitable linear combinations of those coefficients shows \(\pi(a_i)=0\) for every \(i\). Faithfulness then gives \(a_i=0\).

For now, define
\[
\|x\|_{\min}=\sup_{\pi,\sigma}\|(\pi\odot\sigma)(x)\|,
\qquad
\|x\|_{\max}=\sup_{r_A,r_B}\Big\|\sum_i r_A(a_i)r_B(b_i)\Big\|.
\tag{2.1}
\]
The second supremum runs over commuting representations on one Hilbert space; degenerate representations are allowed. The first runs over representations on separate spaces.

**Proposition 2.1.** Both expressions in (2.1) are C*-norms. For every finite tensor sum,
\[
\|x\|_{\min}\le\|x\|_{\max}
\le\inf_{x=\sum_i a_i\otimes b_i}\sum_i\|a_i\|\|b_i\|.
\tag{2.2}
\]
Both norms have the cross-norm property
\[
\|a\otimes b\|=\|a\|\|b\|.
\]

**Proof.** Theorem 1.1 bounds every commuting action by the right side of (2.2). A spatial representation is a commuting action via \(\pi(a)\otimes1\) and \(1\otimes\sigma(b)\), giving the first inequality. Faithful spatial representations separate algebraic tensors, so both seminorms are norms. Each is the supremum of operator norms of *-representations; therefore it is submultiplicative and
\[
\|x^*x\|=\sup_r\|r(x)^*r(x)\|=\sup_r\|r(x)\|^2=\|x\|^2.
\]
For an elementary tensor, the upper estimate is \(\|a\|\|b\|\), while faithful spatial representations give this value by the operator tensor norm formula. \(\square\)

Their completions are denoted \(A\otimes_{\min}B\) and \(A\otimes_{\max}B\). The identity on algebraic tensors extends to a surjective *-homomorphism from the maximal completion onto the minimal completion. Surjectivity follows because the range of a *-homomorphism between C*-algebras is closed, and this range contains the dense algebraic tensors.

**Proposition 2.2.** Let \(\alpha:A\to C\) and \(\beta:B\to C\) be *-homomorphisms with commuting ranges. There is a unique *-homomorphism
\[
\alpha\cdot\beta:A\otimes_{\max}B\longrightarrow C,
\qquad a\otimes b\longmapsto\alpha(a)\beta(b).
\]
Its range is the norm closure of the span of these products. If both algebras and maps are unital, this is the C*-algebra generated by the two ranges.

**Proof.** Represent \(C\) faithfully on a Hilbert space. Formula (2.1) bounds the algebraic product map, so it extends to the completion. Multiplication and involution extend by continuity. The range is closed and contains the algebraic product span; density proves the range description and uniqueness. In the unital case each range is already among those products. \(\square\)

For example, take \(A=B=C_0(\mathbb R)\), both mapped identically into \(C_0(\mathbb R)\). The product map is onto because each \(f\in C_0(\mathbb R)\) is a product: write \(f=(f/\sqrt{|f|})\sqrt{|f|}\), with the first factor set to zero at zeros of \(f\). This illustrates why products, rather than formal missing units, describe a nonunital commuting action.

## 3. Product states determine the spatial norm

For states \(\varphi\) and \(\psi\), their product functional has GNS representation
\[
(\pi_\varphi\otimes\pi_\psi,
H_\varphi\otimes H_\psi,
\xi_\varphi\otimes\xi_\psi).
\tag{3.1}
\]
Indeed, its vector functional agrees with \(\varphi(a)\psi(b)\), and its cyclic subspace contains the tensor product of the two dense cyclic subspaces. Consequently product states are positive and norm one on both completions.

**Theorem 3.1.** For \(x\in A\otimes_{\min}B\),
\[
\|x\|_{\min}^2=
\sup_{\varphi,\psi,y}
\frac{(\varphi\otimes\psi)(y^*x^*xy)}
{(\varphi\otimes\psi)(y^*y)},
\tag{3.2}
\]
where \(\varphi,\psi\) are states and \(y\in A\odot B\) has positive denominator. Moreover every pair of faithful representations computes this norm.

**Proof.** Every nondegenerate representation is an orthogonal sum of cyclic representations: choose a maximal orthogonal family of cyclic invariant subspaces; their complement must be zero. Tensoring the two sums reduces the supremum in (2.1) to cyclic pairs. In each such pair the vectors \(\pi(y)(\xi_\varphi\otimes\xi_\psi)\), with algebraic \(y\), are dense. The operator norm evaluated on those vectors is exactly (3.2).

Now fix faithful nondegenerate \(\pi\) and \(\sigma\). The convex hull of their unit-vector states is weak-* dense in the corresponding state space. To see this for \(\pi\), separation of a missing state would give a self-adjoint \(a\) whose value at that state exceeds \(\sup_{\|\xi\|=1}\langle\pi(a)\xi,\xi\rangle\). That supremum is the upper spectral bound of \(a\), because \(\pi\) is faithful, and no state can exceed that bound. For nonunital algebras use their canonical unital extensions; those extensions remain faithful.

Let \(c=\|(\pi\odot\sigma)(x)\|\) for algebraic \(x\). For product vector states \(f,g\) and algebraic \(y\),
\[
(f\otimes g)(y^*x^*xy)\le c^2(f\otimes g)(y^*y).
\]
Finite convex combinations preserve this inequality. Weak-* approximation in both factors preserves it too, since its two sides involve only finitely many evaluations in each factor. Thus it holds for all states \(\varphi,\psi\). Equation (3.2) gives \(\|x\|_{\min}\le c\); the reverse inequality is built into (2.1). Extend by density to the completion. A faithful degenerate representation has an active nondegenerate summand with the same operator norms, so it gives the same conclusion. \(\square\)

**Corollary 3.2.** *-Homomorphisms \(u:A\to A_1\) and \(v:B\to B_1\) induce *-homomorphisms on both minimal and maximal tensor products. On the minimal tensor product the induced map is injective when both maps are injective.

**Proof.** For the minimal norm, compose faithful representations of the target algebras with \(u,v\) and apply (2.1). If both maps are injective, the composed representations are faithful, so Theorem 3.1 gives equality of norms. For the maximal norm, compose every commuting representation of the target pair with \(u,v\), and use (2.1). \(\square\)

## 4. Positive maps pass to the appropriate completion

The distinction between the two norms persists for completely positive maps. On separate spaces, tensor the dilations. On one space, lift the second action through the commutant of the first dilation.

**Theorem 4.1.** If \(\Phi:A\to C\) and \(\Psi:B\to D\) are completely positive, then their algebraic tensor product extends uniquely to a completely positive map
\[
\Phi\otimes\Psi:A\otimes_{\min}B\longrightarrow C\otimes_{\min}D
\]
with norm \(\|\Phi\|\|\Psi\|\). If instead \(\Phi:A\to C\) and \(\Psi:B\to C\) have commuting ranges, multiplication extends to a completely positive map
\[
\Phi\cdot\Psi:A\otimes_{\max}B\longrightarrow C,
\qquad a\otimes b\longmapsto\Phi(a)\Psi(b),
\]
whose norm is at most \(\|\Phi\|\|\Psi\|\).

**Proof.** Represent \(C,D\) faithfully. Stinespring's theorem gives \(\Phi(a)=V^*\pi(a)V\) and \(\Psi(b)=W^*\sigma(b)W\), with \(\|V\|^2=\|\Phi\|\) and \(\|W\|^2=\|\Psi\|\). The formula
\[
x\longmapsto(V\otimes W)^*(\pi\otimes\sigma)(x)(V\otimes W)
\]
is completely positive and has the required bound. On algebraic tensors its values lie in \(C\odot D\); continuity puts all values in \(C\otimes_{\min}D\). Testing elementary tensors shows that its norm is at least \(\sup_{\|a\|,\|b\|\le1}\|\Phi(a)\|\|\Psi(b)\|=\|\Phi\|\|\Psi\|\).

For the second assertion represent \(C\) faithfully on \(H\). Use the [commutant form of Stinespring's theorem](../../foundations-of-von-neumann-algebras/completely-positive-maps.html#OA-FND-CM-05), Theorem 6.1(2): there is a *-representation
\[
\rho:\Phi(A)'\to\pi(A)',\qquad \rho(c)V=Vc,
\]
where \(\Phi(a)=V^*\pi(a)V\). The map \(b\mapsto\rho(\Psi(b))\) is completely positive on the dilation space. Apply the same theorem to it. This gives a representation \(\tau\) of \(B\), an operator \(W\), and a *-representation of its commutant that lifts \(\pi(A)\). Denote the lifted representation of \(A\) by \(\widehat\pi\). Then
\[
\widehat\pi(A)\subseteq\tau(B)',
\quad \widehat\pi(a)W=W\pi(a),
\quad W^*\tau(b)W=\rho(\Psi(b)),
\quad \|W\|^2\le\|\Psi\|.
\]
The commuting representations \(\widehat\pi,\tau\) define a representation \(R\) of the maximal product. Compression by \(WV\) gives
\[
(WV)^*R(a\otimes b)(WV)
=V^*\pi(a)\rho(\Psi(b))V
=\Phi(a)\Psi(b).
\]
This proves complete positivity, continuity and the norm bound. All values lie in the norm-closed algebra \(C\), by approximation with algebraic tensors. No faithfulness of the auxiliary commutant representations is needed. \(\square\)

**Corollary 4.2.** For \(\varphi\in A^*_+\), the slice
\[
S_\varphi:A\otimes_{\min}B\to B,
\qquad S_\varphi(a\otimes b)=\varphi(a)b
\]
is completely positive, has norm \(\|\varphi\|\) when \(B\ne0\), and satisfies
\[
S_\varphi((1\otimes b)x(1\otimes c))=bS_\varphi(x)c.
\]
In the nonunital case the displayed multiplications mean the continuous left and right actions on the tensor product; they are defined first on algebraic tensors.

**Proof.** Apply Theorem 4.1 to \(\varphi\) and the identity of \(B\). The bimodule identity holds on elementary tensors and extends by density. \(\square\)

For arbitrary bounded functionals \(f\in A^*,g\in B^*\),
\[
\|f\otimes g\|_{(A\otimes_{\min}B)^*}=\|f\|\|g\|.
\tag{4.1}
\]
Here is the vector realization with its exact norm. Put \(\omega=|f|\) and take its GNS triple \((\pi,H,\xi_0)\). By [polar decomposition, Theorem 2.7](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-03), \(|f(a)|^2\le\|f\|\omega(aa^*)\) and \(\|\xi_0\|^2=\|\omega\|=\|f\|\). Consequently \(\pi(a^*)\xi_0\mapsto\overline{f(a)}\) is a well-defined bounded linear functional on a dense subspace of \(H\), of norm at most \(\|f\|^{1/2}\). Riesz representation supplies \(\eta_0\) with \(f(a)=\langle\pi(a)\eta_0,\xi_0\rangle\) and \(\|\eta_0\|\le\|f\|^{1/2}\). Thus \(\|\eta_0\|\|\xi_0\|\le\|f\|\); the opposite inequality follows by taking the norm of this coefficient functional. If \(f=0\), take zero vectors. Apply the same construction to \(g\). Their tensor vectors give the upper bound in (4.1), and almost norm-attaining elementary tensors give the lower bound.

**Proposition 4.3.** A finite sum \(w\in A^*\odot B^*\) has the same functional norm on the minimal and maximal tensor products.

**Proof.** Each product functional is bounded on the minimal product by (4.1), hence so is \(w\). Let \(q:A\otimes_{\max}B\to A\otimes_{\min}B\) be the quotient. On algebraic tensors, the maximal extension of \(w\) is \(w\circ q\). A C*-quotient is an isometric identification of its target with the quotient by its kernel, so its Banach adjoint is an isometry. Therefore \(\|w\circ q\|=\|w\|\). \(\square\)

The statement concerns finite sums of product functionals and their norm closure. It does not assert equality of the full dual spaces.

## 5. Algebraic positivity and dual matrix order

Suppose in this section that \(A,B\) are unital. Call an algebraic functional \(w\) positive when \(w(x^*x)\ge0\) for every \(x\in A\odot B\).

**Lemma 5.1.** Every self-adjoint algebraic tensor is a real sum of elementary tensors with self-adjoint factors. The cone of finite sums of algebraic squares has \(1\otimes1\) as an order unit: every self-adjoint \(x\) satisfies \(-c1\le x\le c1\) for some finite \(c\).

**Proof.** Writing \(a=\operatorname{Re}a+i\operatorname{Im}a\) and similarly for \(b\) gives
\[
\tfrac12(a\otimes b+a^*\otimes b^*)
=\operatorname{Re}a\otimes\operatorname{Re}b
-\operatorname{Im}a\otimes\operatorname{Im}b.
\]
Apply this termwise to a self-adjoint tensor sum. For self-adjoint \(a,b\), put \(M=\|a\|,N=\|b\|\). Then
\[
MN1\pm a\otimes b
=\tfrac12\big((M1+a)\otimes(N1\pm b)
+(M1-a)\otimes(N1\mp b)\big).
\]
Every tensor of two positive elements is an algebraic square, by taking their square roots. Sum these bounds over a self-adjoint presentation of \(x\). \(\square\)

**Proposition 5.2.** Every positive algebraic functional extends uniquely to a positive functional on \(A\otimes_{\max}B\). Its norm is \(w(1\otimes1)\).

**Proof.** Algebraic Cauchy–Schwarz makes \(\langle x,y\rangle=w(y^*x)\) a semidefinite inner product. Quotient its null space and complete. Left multiplication by \(a\otimes1\) is bounded by \(\|a\|\), since
\[
\|a\|^2\|[x]\|^2-\|[(a\otimes1)x]\|^2
=w\big(x^*((\|a\|^21-a^*a)\otimes1)x\big)\ge0.
\]
The last expression is a square: use the positive square root of \(\|a\|^21-a^*a\) in \(A\). The same argument applies to \(1\otimes b\). These two bounded actions commute, and the class of \(1\otimes1\) is cyclic. Thus (2.1) extends their representation to the maximal product, with vector functional \(w\). Its norm equals its value at the identity. Uniqueness follows from density. \(\square\)

Here is a useful interpretation. Give \(M_n(B^*)\) the dual matrix order defined by
\[
[f_{ij}]\ge0
\quad\Longleftrightarrow\quad
\sum_{i,j} f_{ij}(b_{ij})\ge0
\quad\text{for every }[b_{ij}]\in M_n(B)_+.
\tag{5.1}
\]
This specifies the pairing, including its indices. Associate to a bilinear functional \(w\) the map \(T_w:A\to B^*\), \(T_w(a)(b)=w(a\otimes b)\).

**Proposition 5.3.** A bounded bilinear functional \(w\) is an algebraic state exactly when \(T_w\) is completely positive for (5.1) and \(T_w(1)\) is a state of \(B\).

**Proof.** The dual matrix cone can be tested on the Gram matrices \([b_i^*b_j]\), since every positive matrix is a sum of matrices of that form. If \(w\) is positive, then
\[
\sum_{i,j}T_w(a_i^*a_j)(b_i^*b_j)
=w\Big(\big(\sum_i a_i\otimes b_i\big)^*
\big(\sum_j a_j\otimes b_j\big)\Big)\ge0.
\]
Every positive matrix over \(A\) is also a sum of Gram matrices, so this proves complete positivity. Conversely the same formula gives positivity on every algebraic square. Finally \(T_w(1)(1)=w(1\otimes1)\), so the stated normalization is exactly the state normalization. Proposition 5.2 supplies continuity on the maximal product. \(\square\)

## 6. Matrix operations behind positivity

**Lemma 6.1.** Let \([a_{ij}]\) and \([b_{ij}]\) be positive matrices over a C*-algebra, and assume every entry of the first commutes with every entry of the second. Then their entrywise product \([a_{ij}b_{ij}]\) is positive. Also, if \(X=[x_{ik;jl}]\) is a positive matrix indexed by pairs \((i,k)\), then \([\sum_{k,l}x_{ik;jl}]\) is positive.

**Proof.** Write \([a_{ij}]=C^*C\) and \([b_{ij}]=D^*D\). The entries of the two square roots lie in the respective C*-algebras generated by the entries of the original matrices; these algebras commute. Hence
\[
a_{ij}b_{ij}=\sum_{r,s}(c_{ri}d_{si})^*(c_{rj}d_{sj}),
\]
a sum of Gram matrices. For the second assertion, represent the algebra faithfully and let \(V:H^m\to H^{mn}\) repeat each coordinate \(n\) times. The displayed matrix is \(V^*XV\). \(\square\)

## 7. Exercises with solutions

**Exercise 7.1 (first step).** Let \(\varphi(a)=\operatorname{Tr}(Da)\) on \(M_3\), where \(D=\operatorname{diag}(1/2,1/3,1/6)\). Compute the slice of \(\sum_{i,j=1}^3e_{ij}\otimes b_{ij}\), its norm as a map, and its value on the identity.

**Solution.** Since \(\varphi(e_{ij})=D_{ji}\), the slice is \(\frac12b_{11}+\frac13b_{22}+\frac16b_{33}\). The functional is a state, so Corollary 4.2 gives slice norm one on any nonzero second factor. Its value on the identity is the identity of that factor.

**Exercise 7.2 (application).** On \(M_n\otimes M_n\), let \(\tau\) transpose the second factor. Show that \(\mathrm{id}\otimes\tau\) has norm exactly \(n\). Deduce that tensoring transpose with the identity on the compact operators of an infinite-dimensional Hilbert space is unbounded in the spatial norm.

**Solution.** The swap operator \(F=\sum_{i,j}e_{ij}\otimes e_{ji}\) interchanges the two Hilbert factors, so is unitary and has norm one. Its partial transpose is
\[
P=\sum_{i,j}e_{ij}\otimes e_{ij}=|\Omega\rangle\langle\Omega|,
\qquad \Omega=\sum_i e_i\otimes e_i.
\]
Thus \(\|P\|=\|\Omega\|^2=n\), proving the lower bound. Conversely
\[
(\mathrm{id}\otimes\tau)(X)=\sum_{i,j}(1\otimes e_{ij})X(1\otimes e_{ij}).
\]
Factor this map as a row operator, the diagonal repetition of \(X\), and a column operator. Their norms are \(\sqrt n,\|X\|,\sqrt n\), because both relevant sums of matrix-unit squares are \(n1\). Hence the norm is at most \(n\). In infinite dimension each \(n\)-dimensional corner supplies a swap of norm one whose image has norm \(n\). A bounded extension would bound these values uniformly, which is impossible.

**Exercise 7.3 (further step).** Take \(\Phi(\lambda)=\lambda p\) and \(\Psi(\mu)=\mu q\), where \(p,q\) are commuting positive contractions in a unital C*-algebra. Find the norm of their maximal product map. Explain why the bound in Theorem 4.1 need not be equality for commuting ranges.

**Solution.** Since \(\mathbb C\otimes\mathbb C=\mathbb C\), the product map is \(z\mapsto zpq\), of norm \(\|pq\|\). Its bound is \(\|p\|\|q\|\). Orthogonal nonzero projections give product norm zero and bound one. The separate-space tensor map instead has value \(z\mapsto z(p\otimes q)\), whose norm is one for such projections. The two target constructions therefore have different norm behavior even in this elementary case.

## References

- [Courtney–Gillaspy–Ismert] K. Courtney, E. Gillaspy and L. Ismert, *Notes on C\*-algebras*, GOALS lecture notes, available from [IPAM, UCLA](https://www.ipam.ucla.edu/wp-content/uploads/2024/07/Notes_and_Exercises_for_GOALS.pdf).
- [Stinespring] W. F. Stinespring, [“Positive functions on C*-algebras,”](https://www.ams.org/journals/proc/1955-006-02/S0002-9939-1955-0069403-4/S0002-9939-1955-0069403-4.pdf) *Proceedings of the American Mathematical Society* **6** (1955), 211–216.
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, freely accessible corrected manuscript, [author's PDF](https://bruceblackadar.com/Mathematics/Cycr.pdf). The entangled vector tests in Sections 3 and 7 distinguish arbitrary spatial states from limits of product-state mixtures; compare the assertion in II.9.3.6.
