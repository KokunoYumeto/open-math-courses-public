# Complete inputs for completely positive finite models

Finite matrix models have to work before a unit is available, on Hilbert spaces of arbitrary cardinality, and for operator systems that need not be closed. This component supplies those inputs for [Completely positive finite models](../completely-positive-finite-models.html). It also proves the representation of an arbitrary commutative C*-algebra needed for the lesson's unnumbered nuclearity assertion.

The scalar boundary is the complete CF1–10 constructions: choice, Hahn–Banach, compact products, continuous C*-calculus, order, forced unitization and Hilbert/Banach completion. The complete [MG01–06 arguments](../scalar-gns-and-matrix-cstar-norms.html#mg01) then construct scalar GNS representations, faithful representations, canonical matrix C*-norms, positive scalar functionals and complete contractivity of star homomorphisms. Matrix square roots are used only after that matrix construction. CP1–6 supplies the whole concrete coefficient predual. Inner products in the dilation arguments below are linear in their second variable.

<a id="fcp0"></a>
## FCP0. Approximate identities for every algebra and ideal

Let \(A\) be any C*-algebra, and let \(J\) be a norm-closed two-sided ideal; \(J=A\) is allowed. For a finite \(F\subset J\) and \(t>0\), form in the forced unitization

\[
h_F=\sum_{x\in F}(x^*x+xx^*),\qquad
e_{F,t}=h_F(h_F+t1)^{-1}.
\]

The summands belong to \(J\) by its two-sided ideal property. Continuous calculus, with a function vanishing at zero, gives \(e_{F,t}\in J\) and \(0\le e_{F,t}\le1\). Both \(x^*x\) and \(xx^*\) are at most \(h_F\) for \(x\in F\). Congruence by \(1-e_{F,t}=t(h_F+t1)^{-1}\) and the C*-identity give

\[
\begin{aligned}
\|(1-e_{F,t})x\|^2
&=\|(1-e_{F,t})xx^*(1-e_{F,t})\|\\
&\le\|t^2h_F(h_F+t1)^{-2}\|\le t/4,\\
\|x(1-e_{F,t})\|^2
&\le\|t^2h_F(h_F+t1)^{-2}\|\le t/4.
\end{aligned}
\]

The scalar bound follows from \(t^2s/(s+t)^2\le t/4\), \(s\ge0\). Direct the pairs by enlarging \(F\) and decreasing \(t\). Every later pair retains the bound for each previously selected \(x\), so these are positive contractive two-sided approximate identities. This construction uses nets for an arbitrary algebra; it makes no separability assumption. The empty finite set gives zero. The zero algebra and zero ideal are included.

This construction also proves self-adjointness if “ideal” initially means only a closed two-sided algebraic ideal. For \(x\in J\), \(e_i x^*=(xe_i)^*\to x^*\), and each \(e_i x^*\in J\). Hence \(J=J^*\).

For any representation \(\pi:A\to B(K)\), set \(K_0=\overline{\pi(A)K}\). This space and its orthogonal complement reduce \(\pi\). If \(\xi\perp K_0\), testing against \(\pi(a^*)\eta\) proves \(\pi(a)\xi=0\). Moreover \(\pi(e_i)\pi(a)\eta\to\pi(a)\eta\), and the common bound one extends convergence to all of \(K_0\). Thus \(\pi(e_i)\to P_{K_0}\) strongly. No nondegeneracy is silently imposed on a representation.

We will also use boundedness of an algebraically positive map. If a positive linear map \(T:A\to D\) had unbounded norms on the positive unit ball, choose \(a_m\ge0\), \(\|a_m\|\le2^{-m}\), with \(\|T(a_m)\|\ge m\). The norm-convergent sum \(a=\sum_m a_m\) satisfies \(a-a_m\ge0\). Positivity and order monotonicity would force \(\|T(a)\|\ge m\) for every \(m\), which is impossible. Boundedness on the positive unit ball therefore holds. Decompose the real and imaginary parts of an arbitrary element into their positive and negative parts to obtain a finite bound on \(\|T\|\). No continuity was used in moving through a sum: only the order relations \(a-a_m\ge0\) were used.

<a id="fcp0-finite"></a>
### Every finite-dimensional C*-algebra and its actual unit

Let \(F\ne0\) be a finite-dimensional C*-algebra, possibly a subalgebra with a different unit from its ambient algebra. For a fixed vector-space basis, the coordinate map from Euclidean space has an upper norm bound by the sum of the basis norms. On the Euclidean unit sphere its image norm is continuous and positive, so compactness gives a positive lower bound. Thus both norms are equivalent and the closed unit ball of \(F\) is compact. Its positive contractive approximate identity has a norm-convergent subnet. Its limit \(p\in F\) satisfies \(pa=ap=a\) for all \(a\in F\). The positive cone is closed, and testing \(a=p\) gives \(p^2=p\); thus \(p=p^*\) is its actual unit and is an ambient projection.

Every nonzero projection \(e\in F\) contains a minimal projection. If \(eFe\ne\mathbb Ce\), split a nonscalar element into real and imaginary parts to obtain a nonscalar self-adjoint \(h\in eFe\). Finite-dimensional linear dependence gives a nonzero polynomial \(P\) with \(P(h)=0\). If \(P(\lambda)\ne0\), the identity
\(P(t)-P(\lambda)=(t-\lambda)Q(t)\) makes \(h-\lambda e\) invertible in \(eFe\); hence \(\sigma(h)\) is contained in the finite root set of \(P\). It has at least two points, since otherwise continuous calculus would make \(h\) scalar. Interpolate the function equal to one at one spectral point and zero at the others. Continuous calculus produces a nonzero proper projection \(q<e\). Repeating this descent must terminate, since the dimensions of the corners strictly decrease, at a projection \(e_i\) with \(e_iFe_i=\mathbb Ce_i\).

Starting in \(pFp\), then in the successive residual corners, gives finitely many orthogonal minimal projections \(e_1,\ldots,e_N\) summing to \(p\). The process stops because nonzero orthogonal projections are linearly independent. If \(e_iFe_j\ne0\), choose a nonzero \(x\) there. Then

\[
x^*x=\alpha e_j,\qquad xx^*=\alpha e_i,\qquad \alpha=\|x\|^2>0.
\]

Thus \(v=x/\sqrt\alpha\) is a partial isometry from \(e_j\) to \(e_i\). Every \(y\in e_iFe_j\) equals \(v(v^*y)\), and \(v^*y\) is scalar on \(e_j\); this corner is one-dimensional. The relation \(e_iFe_j\ne0\) is an equivalence relation: adjoints give symmetry, and products of the displayed partial isometries give transitivity.

In one equivalence class choose a reference projection \(e_r\), partial isometries \(v_i\in e_iFe_r\), and \(v_r=e_r\). Then \(E_{ij}=v_iv_j^*\) are full matrix units, and every corner in that class is their scalar span. Corners between distinct classes are zero. The identity \(a=\sum_{i,j}e_i a e_j\) therefore gives an algebraic star isomorphism

\[
F\cong\bigoplus_{\nu=1}^k M_{n_\nu}.
\]

MG04 constructs the matrix norms and MG06 makes this star isomorphism and its inverse isometric. This proves the entire finite-dimensional structure assertion used in the block retraction, Corollary 2.4 and Theorem 3.2. For \(F=0\), use zero maps through \(M_1\); no nonzero unit is needed.

<a id="fcp1"></a>
## FCP1. The two complete tensor norms

The entire [TN01–03 construction](../tensor-positivity-nuclearity.html#tn01) gives the Hilbert tensor completion, algebraic injectivity for a faithful pair, and the bound for **every** spatial pair. Its matrix-state approximation step uses the complete scalar and matrix constructions MG01–04. In particular,

\[
\|(\pi\odot\sigma)(z)\|
\le\|z\|_{\min}
\]

for arbitrary coefficient representations, including degenerate and nonfaithful ones. A faithful pair defines the same norm at any Hilbert cardinality; it is a C*-norm and satisfies \(\|a\otimes b\|_{\min}=\|a\|\|b\|\). Its completion is the minimal tensor product. This result does not use a completely positive tensor contraction.

For the maximal norm, let \(A,B\) be arbitrary, possibly zero or nonunital C*-algebras. A commuting pair \(\pi,\sigma\) on one Hilbert space defines

\[
R_{\pi,\sigma}\left(\sum_i a_i\otimes b_i\right)
=\sum_i\pi(a_i)\sigma(b_i).
\]

The algebraic tensor relations make this well defined. Commutation, multiplication and the adjoint identities make it a star representation. MG06 gives

\[
\|R_{\pi,\sigma}(z)\|
\le\sum_i\|a_i\|\|b_i\|.
\tag{FCP1a}
\]

The supremum of these norms can be taken over a set. Adjoin identities to the two coefficient actions by \(a+\lambda1\mapsto\pi(a)+\lambda I\) and similarly for \(B\). For a vector \(\xi\), the closed span of all \(\pi^\dagger(a)\sigma^\dagger(b)\xi\) reduces both actions. A dense set has cardinal at most \(\kappa=\max(\aleph_0,|A^\dagger|,|B^\dagger|)\): use finite rational complex linear combinations of the displayed vectors. A maximal orthonormal set, obtained by choice, has dense span, since a nonzero orthogonal complement would supply an additional unit vector. Its cardinal is at most \(\kappa\): choose a distinct point of the dense set in the disjoint radius-\(1/3\) balls around its unit vectors. Identifying these bases with subsets of one fixed set of size \(\kappa\) gives a set of Hilbert spaces and pairs. Testing \(R_{\pi,\sigma}(z)\) on individual unit vectors shows that these pairs attain the same supremum as all pairs.

Define \(\|z\|_{\max}\) by that supremum. Spatial coefficient actions commute, so

\[
\|z\|_{\min}\le\|z\|_{\max}
\le\sum_i\|a_i\|\|b_i\|.
\tag{FCP1b}
\]

If either algebra is zero the algebraic tensor is zero and its completion is the zero algebra. Otherwise the faithful spatial pair makes this a norm. The triangle inequality, submultiplicativity and star invariance hold for every pair and hence for their supremum. Also

\[
\|z^*z\|_{\max}
=\sup_{\pi,\sigma}\|R_{\pi,\sigma}(z)^*R_{\pi,\sigma}(z)\|
=\|z\|_{\max}^2.
\]

The two elementary-tensor bounds give \(\|a\otimes b\|_{\max}=\|a\|\|b\|\). Complete the normed algebra. Products extend by the submultiplicative estimate, adjoints extend isometrically, and the C*-identity passes to limits, producing \(A\otimes_{\max}B\). Each commuting pair extends contractively to this completion. These facts are exactly the norm construction and finite projective error bound required in Lemmas 4.1–4.2 and Theorem 4.3 of the lesson.

<a id="fcp2"></a>
## FCP2. The full dilation, commuting action and embedded unitization

Let \(\psi:A\to B(H)\) be completely positive. FCP0 proves boundedness; put \(c=\|\psi\|\). On \(A\odot H\) use

\[
\left\langle\sum_i a_i\otimes\xi_i,\sum_j b_j\otimes\eta_j\right\rangle_\psi
=\sum_{i,j}\langle\xi_i,\psi(a_i^*b_j)\eta_j\rangle.
\]

The tensor relations preserve this form. The Gram matrix \([a_i^*a_j]\) is positive: for the rectangular row \(R=(a_1,\ldots,a_n)\), it is \(R^*R\), equivalently the corresponding corner of a square Gram product. Complete positivity therefore makes the form positive. Positive-form Cauchy–Schwarz makes its null vectors a linear subspace orthogonal to all vectors. Quotient by that subspace and complete to \(L\).

Left multiplication by \(d\in A\) has norm at most \(\|d\|\). Its squared norm defect is the positive form of

\[
[a_i^*(\|d\|^2 1-d^*d)a_j].
\]

The positive square root of the middle element is taken in \(A^\dagger\); its products with the \(a_j\) lie in the ideal \(A\). Thus the matrix is a Gram matrix over \(A\). Left multiplication descends and extends to \(\rho(d)\in B(L)\). Direct substitution gives the product and adjoint identities. This is a contractive star representation.

If \(A\) is unital, set \(V\xi=[1\otimes\xi]\). Then \(\rho(1)=I_L\),

\[
V^*\rho(a)V=\psi(a),\qquad
V^*V=\psi(1),\qquad
\|V\|^2=\|\psi(1)\|=\|\psi\|.
\]

The last equality follows either from the size-two block norm estimate in the lesson or from the compression formula and its reverse bound at the unit. Complete positivity of a unital map makes \(V\) an isometry. For a cpc map \(V\) is a contraction; no injectivity is required.

For nonunital \(A\), use the whole approximate identity in FCP0. The vectors \([e_i\otimes\xi]\) have norms at most \(c^{1/2}\|\xi\|\). Their pairing with every \([a\otimes\eta]\) converges because \(e_i a\to a\) in norm. Uniform boundedness extends these pairings from the dense algebraic vectors to a bounded functional on all of \(L\). The Hilbert representation theorem supplies a unique weak-limit vector \(V\xi\); it depends linearly on \(\xi\) and \(\|V\|\le c^{1/2}\). Further,

\[
\rho(a)[e_i\otimes\xi]=[ae_i\otimes\xi]\longrightarrow[a\otimes\xi]
\]

in norm, since its squared error is at most \(c\|ae_i-a\|^2\|\xi\|^2\). Weak limits give \(\rho(a)V\xi=[a\otimes\xi]\). Pairing this with \(V\eta\), using the limiting pairings just constructed, gives \(V^*\rho(a)V=\psi(a)\). Hence \(\|\psi\|\le\|V\|^2\), and together with the first bound this proves \(\|V\|^2=c\). When \(c=0\), the quotient and \(V\) are zero. This includes \(H=0\).

Now suppose \(\sigma:B\to B(H)\) is any star representation whose range commutes with \(\psi(A)\). On algebraic vectors define

\[
\widehat\sigma(b)[a\otimes\xi]=[a\otimes\sigma(b)\xi].
\]

For a finite vector, its squared norm is the quadratic form of \(P=[\psi(a_i^*a_j)]\ge0\). This matrix commutes with \(D=\operatorname{diag}(\sigma(b),\ldots,\sigma(b))\), and also with \(D^*\). Continuous calculus gives commutation with \(P^{1/2}\), whence

\[
D^*PD\le\|b\|^2P.
\]

Thus the operation preserves the nullspace and is bounded by \(\|b\|\). The form itself gives \(\widehat\sigma(b)^*=\widehat\sigma(b^*)\), and products and linear combinations agree on the dense algebraic vectors. It extends to a star representation commuting with \(\rho\). In the unital case the definition gives \(\widehat\sigma(b)V=V\sigma(b)\). In the nonunital case it gives that identity on each \(e_i\otimes\xi\), and bounded operators preserve the weak limits defining \(V\). No faithfulness of \(\sigma\), \(\widehat\sigma\), or \(V\) enters any step.

For a cpc map \(\phi:A\to D\), compose with a target representation and apply this construction. A commuting target pair gives

\[
\sum_i\pi(\phi(a_i))\sigma(b_i)
=V^*\left(\sum_i\rho(a_i)\widehat\sigma(b_i)\right)V.
\]

FCP1 bounds its norm by \(\|\sum_i a_i\otimes b_i\|_{\max}\). Taking the supremum over all target pairs proves the maximal contraction in the entire Lemma 4.1. For the minimal contraction use faithful target representations on separate Hilbert spaces, tensor \(V\) with the identity, and apply the entire TN03 spatial bound. Both contractions extend from algebraic tensors by completion. Neither argument requires a unit.

The same dilation gives the extension actually required for a nonunital subalgebra \(A_0\subset A\) in Proposition 5.4. Work in \(A\) when it is unital, or in \(A^\dagger\) otherwise, and write \(1\) for that ambient identity and \(C=A_0+\mathbb C1\). The displayed quotient dilation is minimal: its dense vectors are \(\rho(a)V\xi=[a\otimes\xi]\). In particular its representation is nondegenerate. If the ambient identity belongs to \(A_0\), then \(\rho(1)=I_L\) by FCP0; use the existing unital algebra. Otherwise each element of \(C\) has a unique expression \(a+\lambda1\), and

\[
\rho_C(a+\lambda1)=\rho(a)+\lambda I_L
\]

is an algebraic unital star homomorphism. MG06 makes it completely positive and contractive, without an assumed representation norm. The map \(\psi_C(x)=V^*\rho_C(x)V\) is completely positive at every matrix size, since it is a matrix congruence. It extends \(\psi\) and has value \(V^*V\le I_H\) at \(1\) when \(\psi\) is cpc. The size-two norm estimate makes its norm at most one. A proper intrinsic unit \(p\) of \(A_0\) causes no ambiguity: \(\rho(p)=I_L\) on the minimal space, so this representation kills \(1-p\). The extension theorem applies to this actual embedded unital algebra and then restricts back to \(A\). Thus the unitization step covers every subalgebra case in the directed-union proof.

<a id="fcp3"></a>
## FCP3. Every commutative C*-algebra is a full \(C_0(X)\)

We prove the whole representation needed for the lesson's commutative-algebra assertion. First let \(C\ne0\) be unital and commutative. Its state space \(S(C)\) is compact Hausdorff for pointwise convergence: embed the dual unit ball in the product of the discs \(\{|z|\le\|a\|\}\), impose the closed linearity equations, and then the closed equations and inequalities \(s(1)=1\), \(s(a^*a)\ge0\). MG01 supplies states and their norm bounds.

For every \(a\in C\), the compact set

\[
F_a=\{s\in S(C):s(a^*a)=\|a\|^2\}
\]

is nonempty by the norming state in MG01. It is a face: equality with the maximal possible value in a nontrivial convex combination forces equality in both summands. Among its nonempty compact faces, choose a minimal one by the axiom of choice in its Zorn form. Indeed, the intersection of a nested family of such faces is nonempty by compactness, compact, and a face; this is the chain condition for that choice.

If the minimal face contained two different states, evaluation at some self-adjoint element would distinguish them: split a distinguishing complex element into real and imaginary parts. This real continuous affine evaluation attains its maximum on the face. Its maximizing set is a nonempty compact proper face, a contradiction. Hence the minimal face is a singleton \(\{s\}\). Faces are transitive under inclusion, so \(s\) is an extreme state of all \(S(C)\), with \(s(a^*a)=\|a\|^2\). This proves the required pure-state existence without assuming a representation theorem or a general extreme-point theorem.

Every extreme state of commutative \(C\) is multiplicative. To see this, take \(0\le b\le1\), put \(t=s(b)\), and consider the positive functionals

\[
\ell_1(c)=s(bc),\qquad \ell_2(c)=s((1-b)c).
\]

They are positive because positive commuting products are positive, and their norms are \(t\) and \(1-t\) by the scalar norm estimate. If \(0<t<1\), the identity \(s=t(\ell_1/t)+(1-t)(\ell_2/(1-t))\) and extremality imply \(\ell_1/t=\ell_2/(1-t)=s\). If \(t=0\), the norm-zero functional \(\ell_1\) vanishes. If \(t=1\), \(\ell_2\) vanishes. Thus in every case

\[
s(bc)=s(b)s(c).
\]

Positive contractions linearly span \(C\), by scalar calculus and decomposition of real and imaginary parts. The identity therefore holds for all \(b,c\in C\). Since states are Hermitian and take value one at the identity, \(s\) is a unital star homomorphism into \(\mathbb C\), called a character.

Let \(K\) be the set of these characters. It is the closed subset of \(S(C)\) specified by \(s(bc)=s(b)s(c)\) for all \(b,c\). Thus \(K\) is compact Hausdorff. For each \(a\), the preceding construction gives a character with

\[
|s(a)|^2=s(a^*a)=\|a\|^2.
\]

Consequently the map

\[
\Gamma:C\to C(K),\qquad \Gamma(a)(s)=s(a)
\]

is an isometric unital star homomorphism. Its range is closed, contains constants, and separates points of \(K\).

Here is the entire surjectivity step. Let \(\mathcal R=\Gamma(C_{\rm sa})\), a closed real linear space of real continuous functions. It contains the constants and separates points. It also contains \(|f|\) for every \(f\in\mathcal R\), by continuous calculus of a self-adjoint preimage; hence it contains the pointwise minima and maxima of every finite family.

Given \(g\in C(K,\mathbb R)\) and \(\varepsilon>0\), for any \(x,y\in K\) there is \(f_{xy}\in\mathcal R\) with \(f_{xy}(x)=g(x)\) and \(f_{xy}(y)=g(y)\). For distinct points rescale a separating real function and add a constant; for identical points use a constant. For fixed \(x\), the open sets \(f_{xy}>g-\varepsilon\), as \(y\) varies, cover \(K\). Take a finite subcover and let \(f_x\) be the maximum of its functions. Then \(f_x>g-\varepsilon\) on \(K\), while \(f_x(x)=g(x)\). The open sets \(f_x<g+\varepsilon\), as \(x\) varies, also cover \(K\). Take a finite subcover and let \(f\) be the minimum of its \(f_x\)'s. At every point,

\[
g-\varepsilon<f<g+\varepsilon.
\]

Thus \(\mathcal R\) is uniformly dense in the real continuous functions; closedness makes it all of them. Splitting real and imaginary parts proves \(\Gamma(C)=C(K)\). The empty-space issue does not arise for this nonzero unital \(C\), whose state/character construction already made \(K\ne\varnothing\).

Now let \(A\) be an arbitrary commutative C*-algebra, possibly nonunital or zero. Its forced unitization \(C=A^\dagger\) is nonzero, unital and commutative. Under the isomorphism just proved, the scalar quotient character \(s_\infty(a+\lambda1)=\lambda\) is a point of \(K\), and the ideal \(A=\ker s_\infty\) becomes exactly

\[
\{f\in C(K):f(s_\infty)=0\}.
\]

Set \(X=K\setminus\{s_\infty\}\). This is locally compact Hausdorff. For completeness, in a compact Hausdorff space, if \(x\in O\) is open, separate \(x\) from each point of \(K\setminus O\) by disjoint open neighborhoods. A finite cover of \(K\setminus O\) makes their corresponding intersection a neighborhood \(U\) of \(x\) with compact closure contained in \(O\). Apply this with \(O\subset X\) to obtain compact neighborhoods in \(X\).

Restriction identifies the displayed ideal with all of \(C_0(X)\). A continuous function on \(K\) vanishing at \(s_\infty\) has compact nonzero level sets lying in \(X\). Conversely, for \(f\in C_0(X)\), extend it by zero at \(s_\infty\). Each \(\varepsilon\)-level set is compact in \(X\), hence closed in \(K\); its complement is a neighborhood of \(s_\infty\) on which \(|f|<\varepsilon\). This proves continuity of the extension and the onto assertion. When \(A=0\), \(K\) is the singleton \(s_\infty\), \(X=\varnothing\), and \(C_0(X)=0\). When \(A\) has its own unit \(p\), every character has \(s(p)\in\{0,1\}\); a character with \(s(p)=0\) annihilates all of \(A\), so is \(s_\infty\). The open condition \(s(p)<1/2\) therefore isolates \(s_\infty\). Thus \(X\) is compact, giving the familiar \(C(X)\) case.

The all-LCH finite-list construction in Theorem 3.3 of the lesson therefore applies to **every** commutative C*-algebra, with no countability condition. Transfer its cpc maps through this star isomorphism using MG06, then apply the entire Theorem 4.3. This proves the original unnumbered nuclearity assertion at its full scope.

<a id="fcp4"></a>
## FCP4. Operator-system order, compactness and all matrix tests

Let \(S\subset C\) be any operator system, without a closedness assumption, and let \(\phi:S\to D\) be completely positive. Represent \(D\) faithfully by MG03–04. If \(\|x\|\le1\), the size-two matrix

\[
\begin{pmatrix}1&x\\x^*&1\end{pmatrix}
=
\begin{pmatrix}1&x\\0&(1-x^*x)^{1/2}\end{pmatrix}^{\!*}
\begin{pmatrix}1&x\\0&(1-x^*x)^{1/2}\end{pmatrix}
\]

is positive. The positive image block has diagonal entries \(\phi(1)\). Positive-form Cauchy–Schwarz on a pair of Hilbert vectors gives \(\|\phi(x)\|\le\|\phi(1)\|\). The reverse bound at \(1\) proves \(\|\phi\|=\|\phi(1)\|\). Applying exactly the same argument to \(M_m(S)\) gives \(\|\phi^{(m)}\|=\|\phi(1)\|\) for every \(m\). This is also the norm control for the direct sum of finite-matrix coordinate maps, the block-diagonal retraction, and both repaired ucp maps in Exercise 7.

For a positive scalar functional \(\omega\) and a fixed \(d\in D_+\), the map \(x\mapsto\omega(x)d\) is completely positive. MG05 makes \(S=[\omega(x_{ij})]\) a positive scalar matrix whenever \([x_{ij}]\ge0\). In \(M_m(D^\dagger)\), the matrices \(S\otimes1\) and \(\operatorname{diag}(d^{1/2},\ldots,d^{1/2})\) give the congruence \([\omega(x_{ij})d]\ge0\), whose entries lie in \(D\). This proves the positivity of the added kernel term in Proposition 2.5 and both state terms in Exercise 7.

The scalar functional in Lemma 2.1 is taken on the **entire** matrix operator system \(M_n(S)\). Its quadratic-form calculation uses the canonical matrix norm and order in MG04; all scalar compressions preserve positive cones by congruence. Lemma 2.2's order-dominating Hahn–Banach construction is precisely the positive extension of MG01 and uses no closedness. Theorem 2.3 then extends each finite-dimensional compression and takes a pointwise ultraweak cluster map over all finite-dimensional subspaces of \(H\). Positivity at every matrix size is tested on every finite tuple of vectors, so no separability or finite-target restriction remains.

The compactness and limit assertions used here have full concrete proofs. The dual ball embeds into the product of the closed scalar discs, with closed linearity equations. CF compactness and the whole coefficient predual CP1–6 make the bounded balls of \(B(H)\) ultraweakly compact. A concrete von Neumann algebra \(M\subset B(H)\) is weak-operator closed and therefore ultraweakly closed, so its bounded balls and products of these balls are compact as well. For a uniformly bounded strongly convergent net, each vector coefficient converges. In any square-summable coefficient series, Cauchy–Schwarz bounds the tail uniformly by the common operator bound times the two square-sum tails. Split into a finite part and its tail to prove ultraweak convergence. This justifies every compression limit and support-cutoff limit in Theorem 2.3 and Proposition 2.5.

Multiplication on either side by a fixed operator is ultraweakly continuous by transforming the coefficient vectors and keeping their square sums finite. Strong convergence of uniformly bounded nets is preserved by products: expand \((x_i y_i-xy)\xi=x_i(y_i-y)\xi+(x_i-x)y\xi\).

These facts justify the whole identity \(b^{1/2}\psi_0(x)b^{1/2}=\phi(x)\) in Proposition 2.5, even when \(b\) has nonclosed range or kernel. The constructed support projection belongs to \(M\); no spectral probability measure or invertibility of \(b\) is assumed.

Finally, MG04 and scalar continuous calculus give every positive matrix over \(D\) a square root in that matrix algebra. Rectangular congruences are positive by embedding in a square matrix with zero unused rows and columns. This supplies both directions of the full Choi-matrix calculation in Exercise 3 at every output matrix size.

The function space \(C_0(X)\) is itself a complete C*-algebra. A uniformly Cauchy net has a uniform continuous limit \(f\). For each \(\varepsilon>0\), a sufficiently close member \(f_i\) makes \(\{|f|\ge\varepsilon\}\) a closed subset of the compact set \(\{|f_i|\ge\varepsilon/2\}\), so \(f\) vanishes at infinity. Sums, products and conjugates stay in this space, and the supremum norm gives \(\|\overline f f\|=\|f\|^2\). Pointwise nonnegative functions have their pointwise square roots in \(C_0(X)\), while squares are pointwise nonnegative.

For \(C_0(X)\), the direct sum of the evaluation representations over all \(x\in X\) is faithful: a function whose values all vanish is zero. Its amplified representation is the direct sum of all pointwise scalar matrices. MG03–04 reflect order through this faithful representation. Thus pointwise matrix positivity is equivalent to positivity in \(M_m(C_0(X))\), proving the exact complete-positivity tests for the weights in Theorem 3.3 and Exercise 4. For the interval tent model, only adjacent sample weights are nonzero at a point; their sum is one and each sample distance is at most the mesh width \(h\). A function with Lipschitz constant at most \(L\) therefore has interpolation error at most \(Lh\), as stated in the original example.

The compact-operator and uncountable-Hilbert examples also have their full elementary inputs. If \(T\) sends the unit ball of an arbitrary Hilbert space into a relatively compact set, take a finite \(\varepsilon\)-net of that set and let \(K\) be its finite-dimensional span. Orthogonal projection gives \(\|T-P_KT\|\le\varepsilon\), so \(T\) is a norm limit of finite-rank operators. Conversely, a norm limit of finite-rank operators has a totally bounded unit-ball image: at any tolerance approximate it by a finite-rank image and use a finite net in that finite-dimensional ball. Its closure is complete and totally bounded. Successive finite nets select a Cauchy subsequence of every sequence, which has a limit by completeness. To prove compactness for open covers, if no uniform radius has all its balls contained in cover members, choose \(x_n\) whose radius-\(1/n\) ball is not so contained. A convergent subsequence tends to a point in an open cover member, which contains a fixed ball about that limit; eventually it contains the entire radius-\(1/n\) ball about \(x_n\), a contradiction. A uniform radius therefore exists, and a finite net gives a finite subcover. Thus both definitions of compact operator agree at every Hilbert cardinality. A finite-rank operator \(S\) and its adjoint have finite-dimensional ranges; putting both ranges in one finite \(K'\) gives \(P_{K'}SP_{K'}=S\). Contractivity then gives \(\|T-P_{K'}TP_{K'}\|\le2\|T-S\|\), proving the entire directed compression example.

For \(\xi\in\ell^2(I)\), every set \(\{i:|\xi_i|\ge1/m\}\) is finite: arbitrarily large finite subsets would make the sum of squares unbounded. Their countable union contains the entire nonzero support. A countable dense family in the closed span of the finite-dimensional \(K_n\)'s therefore has support in one countable \(J\subset I\), and continuity of each coordinate puts the entire closed span in \(\ell^2(J)\). If \(I\) is uncountable, a coordinate outside \(J\) supplies the norm-one rank-one projection whose every compression vanishes. This proves the whole obstruction in Exercise 5.

<a id="fcp4-separation"></a>
The convexity step in Exercise 6 also has a complete separation proof. In a real normed space \(E\), let \(V\) be a nonempty convex set, and let \(y\) lie outside its norm closure. Put \(\delta=\operatorname{dist}(y,V)>0\), choose \(v_0\in V\), and set \(U=V+B(0,\delta/2)-v_0\). This is open, convex, contains zero, and excludes \(y-v_0\). Its gauge

\[
p(x)=\inf\{t>0:x\in tU\}
\]

is finite, nonnegative, sublinear, and bounded above by \(\|x\|/\eta\) for a ball \(B(0,\eta)\subset U\). Convexity proves subadditivity by rescaling two points into \(U\); rescaling proves positive homogeneity. Openness gives \(U=\{p<1\}\): for \(x\in U\) slightly enlarge \(x\) and then rescale, and for \(p(x)<1\) use convexity with zero. Hence \(p(y-v_0)\ge1\). On the real line through \(y-v_0\), prescribe \(\ell(t(y-v_0))=t\,p(y-v_0)\). For \(t\ge0\) this equals the gauge, and for \(t<0\) it is at most the nonnegative gauge. Hahn–Banach extends \(\ell\le p\) to \(E\). The two bounds on \(\ell(x)\) and \(-\ell(x)\) make it continuous. For \(v\in V\), testing every \(u\in B(0,\delta/2)\) in \(v+u-v_0\in U\) gives

\[
\ell(v-v_0)+(\delta/2)\|\ell\|\le1
\le\ell(y-v_0).
\]

Since \(\ell\ne0\), this strictly separates \(y\) from \(V\), so \(y\) is also outside the weak closure. Norm closure is contained in weak closure by continuity, proving equality of both closures for a convex set. In a complex space the functional \(L(x)=\ell(x)-i\ell(ix)\) is complex linear and continuous with \(\operatorname{Re}L=\ell\), giving the same separation in the complex weak topology.

For \(E=D^r\) with its maximum norm, every continuous linear functional is the sum of its \(r\) coordinate functionals: apply it to the sum of the coordinate inclusions. Thus pointwise weak closure of the maps in Exercise 6 puts the evaluated tuple in the weak closure of their convex image in \(D^r\). The separation just proved puts it in the norm closure, at every finite list and tolerance. The image is nonempty because the zero map factors through \(M_1\); an empty test list is automatic. This completes the whole weak-to-norm approximation argument.

<a id="fcp5"></a>
## FCP5. The whole lesson and every solved exercise

The finite-set definitions are used throughout, including nonseparable algebras. Zero maps treat the zero algebra and the empty/all-zero finite function lists. The following routes include complete statements, proofs and solutions.

| Original assertion | Complete inputs |
| --- | --- |
| Propositions 1.1–1.2 | Directed finite sets/tolerances, finite upper bounds, and the exact \(2\|a-a_j\|\) contraction estimate. |
| Lemmas 2.1–2.2 | MG01–04 and FCP4: all matrix-functional quadratic forms and the full scalar order extension. |
| Theorem 2.3, Corollary 2.4 | The full arbitrary-Hilbert compression proof, CP1–6, finite-coordinate compactness, all matrix levels and the actual \(pAp\) coordinate retractions. |
| Proposition 2.5 | FCP4, scalar calculus and state existence: entire support construction, both cutoff limits, arbitrary von Neumann target, kernel, \(b=0\), cluster map and the full ucp completion. |
| Example 3.1, Theorem 3.2 | Entire finite-rank/compact approximation on arbitrary \(H\), complete finite-dimensional retraction, all directed finite algebra families and the two reconstruction errors. |
| Theorem 3.3 and its tent example | The original whole finite-list \(w_0,w_j,W,g_j\) construction on every LCH \(X\), FCP4's pointwise matrix order, and the exact \(Lh\) error. |
| Lemmas 4.1–4.2 | Whole TN01–03 and FCP1–2; the original complete matrix-unit decomposition with its zero-action space, arbitrary second representation and every direct summand. |
| Theorem 4.3 and all three nuclearity examples | FCP1's entire finite projective error bound, both full tensor contractions, finite-matrix min=max, and FCP3's full commutative representation. |
| Propositions 5.1–5.4 | Full cpc compositions/retractions, FCP0's entire ideal approximate identity, actual corners, and FCP2's exact embedded unitization in every directed-union case. |
| Exercises 1–2 | The whole \(2,1,3\) block retraction and the Banach/net contraction error argument. |
| Exercise 3 | Every matrix square root and rectangular congruence in FCP4, both implications, and all output matrix sizes. |
| Exercise 4 | Both complete pointwise-positive maps, their unit values, the two reconstructed functions and the exact \(1/2\) versus \(1/4\) comparison. |
| Exercise 5 | Full countable-support argument in uncountable \(\ell^2(I)\), the common separable span, an omitted coordinate, norm-one rank-one obstruction, and the directed family that does work. |
| Exercise 6 | The entire convex combination through a finite direct sum, its matrix realization, and Hahn–Banach separation in every finite product \(D^r\). |
| Exercise 7 | Scalar state positivity at every matrix level by MG05; both ucp repair maps and the exact \(2\|a\|\|1-\beta\alpha(1)\|\) additional error, with \(1\) included in the finite set. |
| Exercise 8 | The whole bounded map \(z\mapsto-z\), its norm-one amplifications and failure of positivity at the unit. |

## Human comparison and terms

Arveson's publisher-open [Subalgebras of C*-algebras](https://projecteuclid.org/journals/acta-mathematica/volume-123/issue-none/Subalgebras-of-C-algebras/10.1007/BF02392388.full), *Acta Mathematica* 123 (1969), 141–224, provides the complete unital Stinespring comparison in Theorem 1.1.1, pp.145–146; extension in Theorem 1.2.3 with Lemmas 1.2.4–1.2.6, pp.149–152; the all-matrix norm estimate in Proposition 1.2.10, pp.153–154; and the whole commuting-action comparison in Theorem 1.3.1, pp.154–156. The source extension has a closed-system hypothesis and uses general BW compactness and Krein–Smulyan. The lesson's matrix-functional proof and the exact local coefficient/compactness constructions supply its broader nonclosed-system case. FCP2 supplies the entire nonunital and proper-unit cases.

Only the extra isomorphism clause in the source commuting-action theorem assumes an injective dilation operator. The tensor contraction here does not make that assumption and does not consume the source's referred-out normality assertion. The finite models, the full commutative representation, the CPAP-to-nuclearity direction, permanence and whole solved exercises are proved at their stated local scopes.

This component is an original course exposition by GPT-6.1 Sol (OpenAI), Ultra, released under CC0-1.0. Human sources retain their own terms. Free access grants no additional licence for their expression.
