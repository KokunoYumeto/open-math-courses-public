# Automorphic forms, modules and Hilbert constituents

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A classical eigenform supplies a function and a system of Hecke eigenvalues. To make it a representation, we must specify which translations are allowed, which vectors we retain, and which topology we use. Real compact finiteness is an algebraic condition; square integrability supplies a Hilbert completion. They give compatible descriptions of the cuspidal spectrum after we fix a unitary central character.

We use the quotient and measures of Adèles for GL₂ and strong approximation and the lift and real vector fields of From modular forms to adelic functions. Arithmetic finiteness at fixed level, compact type and enveloping-centre ideal is proved in Section 4 of the spectrum lesson. Section 2 proves admissibility for every irreducible unitary adelic GL₂ representation by compact transpose conjugacy and convolution, and also gives a separate cuspidal proof through arithmetic finiteness. We prove the stability, irreducibility and cuspidal comparison arguments. The analytic estimate used in the comparison is proved in Why the cuspidal spectrum is discrete, Theorems 3.1, 4.2 and 5.2. This forward reference isolates the analytic proof rather than treating square integrability as part of the definition.

## 1. Functions and the algebraic actions

Put \(G=\mathrm{GL}_2\), \(\mathfrak g=\mathfrak{gl}_2(\mathbb C)\), \(K_\infty=\mathrm O(2)\), \(K_f=G(\widehat{\mathbb Z})\), and \(K=K_\infty K_f\). The enveloping algebra \(U(\mathfrak g)\) records iterated right Lie derivatives; its centre is denoted \(\mathcal Z\).

Here is a concrete group height. At infinity use the maximum of one and the operator norms of \(g_\infty\) and \(g_\infty^{-1}\). At a finite prime use the maximum of one and the absolute values of the entries of \(g_p\) and \(g_p^{-1}\). Let \(h(g)\) be their product. Almost every factor is one. Matrix multiplication gives \(h(gt)\leq h(g)h(t)\); the finite-place estimate uses the ultrametric inequality. This height includes the inverse and controls both directions in the real centre.

An **automorphic form** is a function \(\phi\) on \(G(\mathbb Q)\backslash G(\mathbb A)\) with the following properties:

- It is smooth at infinity and fixed by some compact open finite subgroup \(J\).
- Its right \(K_\infty\)-orbit spans a finite-dimensional space.
- \(\mathcal Z\phi\) is finite dimensional, equivalently a cofinite ideal \(I\subset\mathcal Z\) annihilates it.
- \(|\phi(g)|\leq C h(g)^r\) for some \(C,r\).

Write \(\mathcal A\) for their space. Smoothness at finite places means local constancy with a common right open stabilizer. This is equivalent to finite compact orbit: an open subgroup of a compact group has finite index, and a finite-dimensional smooth compact representation factors through a finite quotient. Thus these conditions are the usual right \(K\)-finiteness condition. The finite subgroup chosen in the definition can be replaced by another maximal compact without changing the space.

Let \(N=\{n(t):t\in\mathbb A\}\), where \(n(t)=\begin{pmatrix}1&t\\ 0&1\end{pmatrix}\). A form is **cuspidal** if

\[
C_N\phi(g):=\int_{\mathbb Q\backslash\mathbb A}\phi(n(t)g)\,dt=0
\quad\text{for every }g.
\tag{1.1}
\]

The quotient is compact with volume one. For GL₂ all proper rational parabolics are conjugate to this one. Rational invariance and allowing every \(g\) therefore test every cusp. Denote the space by \(\mathcal A_0\). A subscript \(\omega\) specifies \(\phi(gz)=\omega(z)\phi(g)\) for a character of \(\mathbb Q^\times\backslash\mathbb A^\times\).

The actions are \(R(a)\phi(g)=\phi(ga)\), and
\(R(X)\phi(g)=\left.\frac d{dt}\phi(g\exp(tX))\right|_{t=0}\).
The two commute when one is a finite adelic translation and the other a real operation. A \((\mathfrak g,K_\infty)\times G(\mathbb A_f)\)-module carries these compatible algebraic actions; its vectors have finite compact orbit and a finite open stabilizer. It is **admissible** if each compact isotypic space fixed by each \(J\) is finite dimensional. A submodule need not be closed: there is no Hilbert topology in this definition.

**Arithmetic finiteness.** For a cofinite \(I\), finite \(K_\infty\)-type packet and compact open \(J\), the corresponding space of automorphic forms is finite dimensional. The complete rational GL₂ proof is the arithmetic-finiteness theorem in Section 4 of Why the cuspidal spectrum is discrete, using local elliptic estimates, cusp Fourier equations and the fixed-weight compact resolvent. Getz–Hahn, Theorem 6.3.2, is the original general reference.

**Proposition 1.1 — stability.** Both \(\mathcal A\) and \(\mathcal A_0\) are \((\mathfrak g,K_\infty)\times G(\mathbb A_f)\)-modules. All real derivatives of any one form have a common polynomial-growth exponent.

**Proof.** The reproducing-kernel proof in the spectrum lesson, Lemma 4.1, uses the arithmetic finiteness proved there: on the finite-dimensional fixed-type, level and ideal space, compact-type-preserving approximate-identity convolution eventually becomes invertible. Cayley–Hamilton expresses its inverse as a polynomial. Consequently \(\phi=R(f_0)\phi\) for a smooth compact kernel, and \(R(D)\phi=R(f_D)\phi\) for every real enveloping operator \(D\). Submultiplicativity of \(h\) bounds each derivative by the original growth exponent. This supplies the potentially missing growth condition in the stability assertion.

The compact orbit of \(R(D)\phi\) is finite because it lies in the span of the finite adjoint orbit of \(D\) applied to the finite compact orbit of \(\phi\). The same \(I\) annihilates it, since it is central. A finite translation changes the stabilizer to a conjugate open subgroup, leaves the real compact condition unchanged and preserves the central ideal. Its growth changes only by the fixed factor \(h(a)^r\). Compact translations satisfy the same conditions. Rational invariance is retained by every right operation. Finally the compact-domain integral (1.1) commutes with all right operations and real derivatives. This proves cuspidal stability as well. \(\square\)

A general real translation conjugates the compact group and can introduce infinitely many rotation weights. It therefore acts on a smooth completion but need not act on \(\mathcal A\). Solution 7.1 gives an explicit cuspidal example.

## 2. The unitary Hilbert picture

Fix a unitary \(\omega\). Write

\[
X=G(\mathbb Q)Z(\mathbb A)\backslash G(\mathbb A),\qquad
H_\omega=L^2(X,\omega).
\tag{2.1}
\]

These are central-equivariant functions whose absolute square descends to \(X\), rather than ordinary functions on \(X\) when \(\omega\ne1\). The inner product uses the quotient Haar measure of volume \(\pi/3\). Right translation is a strongly continuous unitary representation.

For an \(L^2\) vector, its constant term is defined locally almost everywhere on the group, or as a distribution. It is not obtained from a global left \(N(\mathbb A)\)-action on \(X\). Define \(H_{\omega,0}\) by the vanishing of that distribution. Equivalently, require \(C_NR(f)u(g)=0\) for every smooth compact kernel \(f\) and every \(g\). Local boundedness of constant terms and an approximate identity prove equivalence. The spectrum lesson, Lemma 1.1, gives the details and proves that this is a closed invariant subspace.

An irreducible Hilbert constituent means a nonzero closed invariant subspace with no proper nonzero closed invariant subspace. In a unitary representation every closed invariant subspace has an invariant orthogonal complement. A Hilbert subquotient thus occurs as a closed subrepresentation. On the cuspidal space the spectrum lesson proves

\[
H_{\omega,0}=\widehat\bigoplus_i\mathcal H_i,
\tag{2.2}
\]

with irreducible summands and finite multiplicity for each isomorphism class. This assertion is a proved forward dependency, not a formal consequence of finite quotient volume.

**Theorem — general adelic unitary admissibility.** Every irreducible strongly continuous unitary representation of \(\mathrm{GL}_2(\mathbb A)\) is admissible on its finite vectors. More precisely each irreducible type of the full compact group
\[
K=O(2)\times\prod_p\mathrm{GL}_2(\mathbb Z_p)
\]
occurs at most once. Consequently fixing a finite open level and an infinity compact-type packet leaves a finite-dimensional space.

**Proof.** We apply the general compact-convolution multiplicity lemma proved in Smooth local representations and the Hecke-module dictionary, Lemma 3.2. We verify its conjugacy hypothesis globally rather than assume a tensor-product decomposition.

Every real \(2\times2\) matrix is orthogonally conjugate to its transpose. Write it as \(A=S+cJ\), with \(S\) symmetric and
\(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\).
Orthogonally diagonalize \(S\), and reflect one eigenaxis. This reflection commutes with \(S\) and sends \(J\) to \(-J\), so it conjugates \(A\) to \(A^{\mathsf T}\), including when the symmetric part has repeated eigenvalues. At every finite prime, the integral transpose-conjugacy lemma of that same lesson, Lemma 3.3, supplies a conjugator in \(\mathrm{GL}_2(\mathbb Z_p)\).

Choose those conjugators component by component. Their product is in the compact group \(K\), and sends any adelic \(g\) to \(g^{\mathsf T}\). Transpose is a continuous anti-automorphism of the adelic group. It preserves Haar measure: at each place it permutes the additive matrix coordinates and leaves the density \(|\det g|_v^{-2}d^4g\) unchanged; at finite places it also preserves the compact normalization. These local assertions give the restricted-product measure assertion. The group is unimodular by the same local densities. Lemma 3.2 therefore proves the joint compact multiplicity bound.

Let \(J_f\) be a compact open finite level and set \(L=J_f\cap K_f\). It has finite index in \(K_f\) because that compact coset space is discrete. Its normal core \(L_0\) is a finite intersection of conjugates and is open. The \(J_f\)-fixed space is contained in the \(L_0\)-fixed space. For a fixed infinity compact type \(\tau\), only joint types
\(\tau\otimes\rho\), with \(\rho\) an irreducible representation of the finite group \(K_f/L_0\), can contribute. Indeed the \(L_0\)-fixed part of a compact irreducible is invariant under \(K_f\), so is either zero or the whole type. Irreducibles of a product of compact groups are tensors of their irreducibles: decompose for the first factor; its isotypic multiplicity space carries the commuting second factor, and simplicity forces one simple factor on each side. The multiplicity bound now gives
\[
\dim\bigl(\mathcal H(\tau)^{J_f}\bigr)
 \le\dim\tau\sum_{\rho\in\widehat{K_f/L_0}}\dim\rho
 \le\dim\tau\,[K_f:L_0].
\]
The finite-group bound is the matrix-coefficient regular-space bound proved in Lesson 5, Theorem 3.4. A finite packet of \(\tau\)'s gives a finite sum of these bounds. This is exactly adelic admissibility, established without assuming local factorization or first declaring the finite-vector module irreducible. Lemma 2.1 and Theorem 3.2 below then prove smoothness, scalar Casimir and finite-vector irreducibility. Getz–Hahn, Theorem 6.6.2, remains the general historical reference rather than a proof input for this GL₂ assertion. \(\square\)


For such a Hilbert representation \(\mathcal H\), let \(\mathcal H_{\rm fin}\) be the vectors fixed by some finite \(J\) and finite under \(K_\infty\). These vectors are dense: normalized finite-level averages approach the identity; Fejér averages on rotations approach the identity and have finite Fourier support. Including the reflection keeps the compact orbit finite.

**Lemma — admissibility of a cuspidal Hilbert constituent.** For an irreducible closed constituent \(\mathcal H_i\subset H_{\omega,0}\), its finite vectors are smooth and admissible, and the Casimir acts on them by one scalar. These conclusions follow independently of the general unitary admissibility theorem.

**Proof.** Choose a nonzero fixed-level rotation-weight space in \(\mathcal H_i\); density of the compact projections supplies one. The compact cuspidal resolvent at that weight and level is proved in the spectrum lesson, Section 4. The orthogonal projection to \(\mathcal H_i\) commutes with the full right group action and its closed real generators. It therefore reduces the corresponding closed form and its self-adjoint operator. Some finite-dimensional Casimir eigenspace consequently has a nonzero vector \(v\) in \(\mathcal H_i\), of eigenvalue \(\lambda\).

We first smooth this eigenvector, without assuming its whole fixed space is finite dimensional. Take the real approximate identities averaged under compact conjugation, times the normalized finite-level average. They preserve the chosen weight, level and the finite-dimensional \(\lambda\)-eigenspace: the central Casimir commutes with convolution, including in its weak differential realization. Their restrictions converge to the identity on that eigenspace and are eventually invertible. Their images are real-smooth. Cayley–Hamilton expresses the inverse as a polynomial, so \(v=R(f_0)v\) for a smooth compact kernel. The spectrum lesson, Theorem 3.1, makes this vector and all its derivatives rapidly decreasing. Thus \(v\) is an automorphic cusp form.

Let \(V\) be the algebraic module generated by \(v\), under real Lie operations, compact operations and finite adelic translations. Stability from Proposition 1.1 gives \(V\subset\mathcal A_{0,\omega}\). The Casimir stays equal to \(\lambda\). The ladder norm equations and analytic-vector argument in Lemma 3.1 apply: they use smoothness, that eigenvalue and unitarity, without any fixed-space dimension assumption. They make the Hilbert closure of \(V\) invariant under the connected real group. Reflection and finite translations supply the other operations. Irreducibility gives \(\overline V=\mathcal H_i\).

Fix any new finite level and compact-type packet. Its orthogonal projection preserves \(V\) algebraically: each vector has a finite-dimensional compact orbit, so its compact average is a finite linear combination of orbit vectors. The projected vectors are automorphic cusp forms with that level, packet, central character and Casimir eigenvalue. The independent PBW computation following Theorem 3.2 shows that the scalar direction and Casimir generate the enveloping centre, so these vectors share a cofinite central ideal. The arithmetic-finiteness theorem proved in Section 4 of the spectrum lesson puts them in a finite-dimensional function space. Their span is therefore finite dimensional and, inside \(L^2\), closed in the Hilbert norm. On the other hand, projection of the dense \(V\) is dense in the corresponding fixed space of \(\mathcal H_i\). The fixed space therefore equals that projected finite-dimensional space.

This proves admissibility. It also proves that every finite vector belongs to \(V\), hence is smooth and has the same Casimir eigenvalue. The analytic-vector lemma and the same finite-dimensional projections applied to any nonzero algebraic submodule prove its irreducibility as well. There is no use of general Hilbert admissibility in these steps. \(\square\)

**Lemma 2.1 — finite-vector smoothing.** Every vector of \(\mathcal H_{\rm fin}\) is real-smooth, and is fixed by a smooth compact convolution.

**Proof.** Put it in its finite-dimensional compact-type and \(J\)-fixed space \(E\), using admissibility. A real approximate identity averaged under compact conjugation, times the normalized finite \(J\)-average, preserves \(E\). Strong convergence becomes matrix convergence on this finite-dimensional space, so the operator is eventually invertible there. Its image consists of real-smooth vectors: differentiating the compact kernel gives a norm derivative at every order. Thus all of \(E\) is smooth. Cayley–Hamilton again expresses the inverse as a polynomial, yielding a compact reproducing convolution. \(\square\)

## 3. Real ladders and algebraic irreducibility

Use the rotation orientation from the lift lesson:
\(r(\theta)=\begin{pmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{pmatrix}\).
Write \(J_0=r'(0)\), \(H=\operatorname{diag}(1,-1)\), \(S=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}\), and

\[
P=\tfrac12R(H+iS),\quad L=\tfrac12R(H-iS),\quad M=-iR(J_0).
\]

On rotation weight \(m\), \(M=m\), \(P\) raises the weight by two and \(L\) lowers it by two. With the Casimir normalization of the lift lesson, the matrix commutators or its explicit vector fields give

\[
PL=-\Omega-\frac{m(m-2)}4,
\qquad LP=-\Omega-\frac{m(m+2)}4,
\qquad [L,P]=-M.
\tag{3.1}
\]

The first two formulas mean restriction to weight \(m\). In a unitary representation the real Lie generators are skew-adjoint on smooth vectors, so \(P^*=-L\). For \(\Omega v=\lambda v\) of weight \(m\),

\[
\|Pv\|^2=\left(\lambda+\frac{m(m+2)}4\right)\|v\|^2,
\qquad
\|Lv\|^2=\left(\lambda+\frac{m(m-2)}4\right)\|v\|^2.
\tag{3.2}
\]

In particular \(\lambda\) is real. These identities prove the analytic property needed to pass between algebraic and closed subspaces.

**Lemma 3.1 — analytic vectors.** Finite-compact vectors with a fixed Casimir eigenvalue and unitary central character have convergent real one-parameter-group Taylor series. For a fixed real \(X\), their convergence radius can be chosen independently of their starting finite weight packet.

**Proof.** A word of length \(n\) in \(P,L,M\) stays at the given Casimir value and has weights at most \(m_0+2n\) in absolute value. Equation (3.2) bounds its norm by \(\|v\|\) times a product \(\prod_{j=1}^n C(1+m_0+2j)\); the fixed \(\lambda\) is absorbed in \(C\). The real central generator is scalar by the central character, so including it only changes \(C\). Expanding \(R(X)^n\) into words and comparing that product with a factorial gives

\[
\|R(X)^nv\|\leq C_v A_X^n n!\,n^{b_v}.
\tag{3.3}
\]

For \(c\geq0\), dividing \(\prod_{j=1}^n(j+c)\) by \(n!\) gives \(\prod_{j=1}^n(1+c/j)\leq \exp(c\sum_{j=1}^n1/j)\leq e^c n^c\). The starting weights affect \(C_v,b_v\); the exponential constant \(A_X\) need not depend on them. Finite sums of weight vectors satisfy the same conclusion.

Taylor's formula for the unitary one-parameter group has norm remainder at most \(|t|^n\|R(X)^nv\|/n!\), using its integral remainder and unitarity. Equation (3.3) makes it tend to zero when \(|t|A_X<1\). Its Taylor partial sums are Lie polynomials applied to \(v\). This proves the assertion and its common-radius statement. \(\square\)

**Theorem 3.2.** The finite vectors of an irreducible unitary adelic representation form an irreducible \((\mathfrak g,K_\infty)\times G(\mathbb A_f)\)-module. The Casimir acts by a scalar.

**Proof.** Choose a nonzero finite weight and level space. It is finite dimensional and smooth by Lemma 2.1, and \(\Omega\) preserves it. Choose a Casimir eigenvector \(v\). Its algebraically generated module \(V\) has the same eigenvalue, including after finite translations and reflection. Lemma 3.1 puts sufficiently small real exponentials of every vector of \(V\) in its Hilbert closure. The common radius and continuity extend invariance to that closure. Repeating small exponentials generates the real connected group; reflection supplies its other component, and finite translations are already included. Irreducibility makes \(\overline V=\mathcal H\).

Every compact-type and finite-level projection preserves \(V\) algebraically. On a finite vector the compact orbit is finite dimensional and a finite compact orbit factors through a finite quotient; its averaging integral is therefore a finite linear combination of orbit vectors. Project the dense \(V\) to any admissible finite-dimensional weight-and-level space \(E'\). Its image is a dense linear subspace of \(E'\), hence all of \(E'\). Every finite vector belongs to a finite sum of such spaces, so \(V=\mathcal H_{\rm fin}\). In particular the Casimir is scalar on all finite vectors.

For any nonzero algebraic submodule \(W\subset\mathcal H_{\rm fin}\), the same analytic argument makes its closure invariant and thus all of \(\mathcal H\). The same finite-dimensional projections give \(W=\mathcal H_{\rm fin}\). This proves algebraic irreducibility. \(\square\)

For GL₂, \(\mathcal Z\) is generated by the scalar Lie direction and the special-linear Casimir. One way to check this familiar enveloping-algebra fact is to take the leading PBW symbol of a central element: on traceless matrices an invariant polynomial is a polynomial in the quadratic determinant, since the distinct-eigenvalue conjugacy classes are dense. Subtracting a polynomial in the Casimir lowers its degree; induction, with the scalar direction adjoined, gives the assertion. Hence Theorem 3.2 also gives enveloping-centre finiteness.

**Lemma 3.3 — uniqueness of completion.** If two irreducible unitary representations have isomorphic finite-vector modules, they are unitarily equivalent.

**Proof.** Let \(F\) be such a module isomorphism on the dense finite vectors. It is closable. Indeed if \(v_n\to0\) and \(Fv_n\to w\), project to any fixed weight-and-level space in the target. Commutation with its projection and boundedness of \(F\) on the corresponding finite-dimensional source space make the projected limit zero. These spaces are dense, so \(w=0\).

The closure of its graph is invariant under the group. Compact and finite operations preserve the graph directly. For real operations apply Lemma 3.1 to graph vectors in the direct sum of the two representations; their common Casimir and central character give the common radius, and both Taylor series respect \(F\). Thus the closed operator \(\overline F\) intertwines the full group. Its positive operator \(\overline F^*\overline F\) has invariant spectral projections. Irreducibility makes every such projection zero or the identity, so this operator is \(cI\) for a finite \(c>0\). Its polar part is a unitary intertwiner: its range is dense and closed, and its kernel is zero. Scaling by \(c^{-1/2}\) proves the claim. This is the spectral-theorem proof of unitary Schur's lemma, applied to a closed intertwiner. \(\square\)

## 4. The two cuspidal definitions

An **automorphic representation** in the algebraic sense is an irreducible admissible module isomorphic to a subquotient of \(\mathcal A\). A **cuspidal** one is isomorphic to a submodule of \(\mathcal A_0\). In the unitary Hilbert sense it is an irreducible closed constituent of \(H_{\omega,0}\). In this comparison we fix unitary \(\omega\) on both sides.

**Theorem 4.1 — cuspidal comparison.** Passage to finite vectors gives a bijection between the isomorphism classes of Hilbert cuspidal constituents with central character \(\omega\) and algebraic cuspidal representations with that character. Moreover,

\[
\mathcal A_{0,\omega}=\bigoplus_i(\mathcal H_i)_{\rm fin}
\subset H_{\omega,0},
\tag{4.1}
\]

where the index includes the finite multiplicities in (2.2). In particular irreducible cuspidal subquotients also occur as submodules.

**Proof, from Hilbert vectors to forms.** Let \(u\in(\mathcal H_i)_{\rm fin}\). Lemma 2.1 supplies \(u=R(f_0)u\). The bounded modified kernel of the spectrum lesson, Theorem 3.1, gives a smooth representative bounded on the quotient, rapidly decreasing in all cusp charts. Repeating with differentiated kernels gives the same conclusion for every real derivative. There is no assumed point evaluation of an arbitrary \(L^2\) class in this argument: convolution supplies the representative. Its central character is unitary, so the bound holds on the whole group, including the centre; it is in particular of moderate growth. It is finite under the enveloping centre by Theorem 3.2 and the fixed central character. Its constant term vanishes everywhere by the smooth-convolution form of cuspidality. It is an automorphic cusp form. The cuspidal Hilbert lemma in Section 2 and Theorem 3.2 prove that this module is irreducible admissible.

**Proof, from forms to Hilbert constituents.** By the rapid-decay theorem of the spectrum lesson, Theorem 4.2, every \(u\in\mathcal A_{0,\omega}\) and every derivative is in \(L^2\). It therefore embeds in \(H_{\omega,0}\). Decompose it using (2.2), with orthogonal projections \(P_i\). They commute with group operations, compact-type and level projections, and closed real generators. Since \(u=R(f_0)u\) by Proposition 1.1, each \(u_i=P_i u\) is a smooth finite vector in its irreducible constituent, and has the same level, compact packet and annihilating ideal as \(u\). By the forward argument each \(u_i\) is an automorphic cusp form. They all lie in the finite-dimensional space supplied by the arithmetic-finiteness theorem proved in the spectrum lesson, Section 4. As nonzero \(u_i\) are mutually orthogonal, only finitely many are nonzero. This proves that every \(u\) lies in the algebraic direct sum in (4.1). The reverse inclusion was just proved.

For an irreducible algebraic submodule, one of these projections is nonzero and is a module map to \((\mathcal H_i)_{\rm fin}\). Its kernel and image, by irreducibility on both sides, make it an isomorphism. Equivalently (4.1) is a sum of simple modules and is semisimple; the elementary direct-sum characterization of a semisimple module shows that its irreducible subquotients are the same simple modules. Such a module acquires a unitary completion from \(\mathcal H_i\). Lemma 3.3 makes its isomorphism class unique, proving the bijection. \(\square\)

This proof also gives density of \(\mathcal A_{0,\omega}\) in \(H_{\omega,0}\), since finite vectors are dense in every Hilbert summand. The finiteness of Hilbert multiplicities is proved by compact convolution, not asserted as a consequence of the definition of an automorphic form.

The unitary-character hypothesis matters. If \(\phi\) is a cusp form, then \(|\det g|_{\mathbb A}^s\phi(g)\) remains an automorphic cusp form; the determinant norm is rational-invariant, and unipotents have determinant one. For \(\operatorname{Re}s\ne0\), its positive central character is nonunitary, so that module cannot be a constituent of a unitary representation with that central action. The broader algebraic definition allows these twists. It also allows Eisenstein representations. Only a unitary completion, when supplied, has the full adelic group action on its Hilbert space.

## 5. Holomorphic and Maass ladders

**Proposition 5.1 — holomorphic real module.** Let \(f\ne0\) be a holomorphic cusp form of integral weight \(k\geq1\), with its lift \(v=\phi_f\). Its cyclic \((\mathfrak g,\mathrm{SO}(2))\)-module has one-dimensional weights \(k+2n\), \(n\geq0\), and is irreducible. Reflection adds the opposite ray; the resulting \((\mathfrak g,\mathrm O(2))\)-module is irreducible and has lowest absolute compact weight \(k\).

**Proof.** The lift lesson proves \(Lv=0\), weight \(k\), and \(\Omega v=\frac k2(1-\frac k2)v\). Its lift is in the unitary cuspidal Hilbert space. Equations (3.1)–(3.2) give

\[
\|P^{n+1}v\|^2=(n+1)(k+n)\|P^nv\|^2,
\qquad \|P^nv\|^2=n!(k)_n\|v\|^2,
\tag{5.1}
\]

where \((k)_n=k(k+1)\cdots(k+n-1)\). All these vectors are nonzero. Reorder any Lie word by (3.1); lowering past raising reduces it to a multiple of a power of \(P\) applied to \(v\). Thus the powers are a basis, distinguished by their weights. A nonzero submodule contains a weight vector: its finite weight packet can be separated by a polynomial in \(M\). Repeated lowering, with nonzero factors from (5.1), recovers \(v\), and then all powers. This proves irreducibility for rotations.

The reflection \(\epsilon=\operatorname{diag}(1,-1)\) changes \(M\) to \(-M\) and interchanges \(P,L\). It supplies the weights \(-k-2n\), disjoint from the positive ray, and exchanges the two cyclic rays. A nonzero full compact submodule contains a weight vector on one ray, hence that entire ray, and reflection gives the other. The scalar Lie direction already acts scalarly. This proves the assertion. Newform status is unnecessary for this real cyclic assertion; global irreducibility involves the finite places as well. \(\square\)

**Proposition 5.2 — Maass real module.** A nonzero weight-zero Maass cusp vector with \(\Omega v=\lambda v\) has \(\lambda>0\). Its cyclic \((\mathfrak g,\mathrm{SO}(2))\)-module is irreducible with the even-weight ladder. If it has reflection parity \(\epsilon v=\eta v\), \(\eta=\pm1\), its full \((\mathfrak g,\mathrm O(2))\)-module is irreducible too.

**Proof.** Equation (3.2) at weight zero gives \(\lambda\geq0\). If \(\lambda=0\), both \(P,L\) vanish, and so does the rotation generator. The vector is invariant under the connected real special-linear group. At any fixed finite component its real cusp integral is its value; the full adelic cusp condition, expressed as that real period average, forces it to be zero. Thus \(\lambda>0\).

At every even weight \(m\), both ladder factors in (3.2) are positive: \(m(m\pm2)/4\geq0\) for even \(m\). Reordering words shows that the cyclic module has at most one vector at each even weight, generated by successive raises above zero and lowers below zero. The positive factors make all these vectors nonzero. Any weight vector can be taken back to \(v\), so a nonzero submodule is the whole module. With the parity hypothesis, reflection stays in this module by interchanging raises and lowers, proving the full compact assertion. Without that hypothesis a sum of the two parity extensions can generate a reducible full compact module. This is why an unqualified full \(\mathrm O(2)\) assertion for a Maass eigenfunction needs correction. \(\square\)

## 6. Three concrete examples

For \(\Delta=q\prod_{n\geq1}(1-q^n)^{24}\), the lift has weight twelve, lowering zero and Casimir \(6(1-6)=-30\). The classical input \(S_{12}(\mathrm{SL}_2(\mathbb Z))=\mathbb C\Delta\) belongs to the modular-form prerequisite; its dimension can also be checked in the [LMFDB level-one weight-twelve space](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/1/12/a/). We now deduce the receiving representation claim. Orthogonal constituent projections of \(\phi_\Delta\) retain finite maximal-compact invariance, weight twelve and lowering zero. The dictionary identifies this joint space with that one-dimensional classical cusp space. At most one orthogonal projection is nonzero, so \(\phi_\Delta\) lies in one irreducible Hilbert constituent. Its algebraic adelic cyclic module is the entire constituent's finite-vector module by Theorem 3.2. There is only one copy of that constituent: every equivalent copy would contribute a nonzero vector to the same one-dimensional joint space. At infinity Proposition 5.1 supplies the weights \(\pm(12+2n)\).

For a smooth Hecke character \(\chi\), the function \(\chi(\det g)\) is rational-invariant, has a finite-level stabilizer and a one-dimensional real compact orbit. Its enveloping centre acts scalarly. Its absolute value has polynomial growth: a character of the idèle class group has a unitary compact part and a real norm power. Thus it is an automorphic form with central character \(\chi^2\). Its constant term is itself, since \(\det n(t)=1\). It is never cuspidal. If \(\chi\) is unitary, it is nevertheless in \(H_{\chi^2}\), because the quotient has finite volume. Solution 7.2 proves its orthogonality to the entire cuspidal space.

Here is an Eisenstein example with convergence and growth visible before analytic continuation. For a rational projective row \([v]=[(c,d)]\), define
\(H(vg)=\|v g_\infty\|_2\prod_p\max(|(vg_p)_1|_p,|(vg_p)_2|_p)\).
It is independent of rescaling \(v\) by a nonzero rational, by the product formula. Put

\[
E(g)=\sum_{[v]\in\mathbb P^1(\mathbb Q)}
\frac{|\det g|_{\mathbb A}^{2}}{H(vg)^4}.
\tag{6.1}
\]

Choose primitive integer rows up to sign. Their finite height is one and their real height is \(\sqrt{c^2+d^2}\). The inequality \(H(vg)\geq H(v)/h(g)\), and \(|\det g|_{\mathbb A}\leq h(g)^2\), bound (6.1) by \(C h(g)^8\sum_{[v]}H(v)^{-4}\), with the sum finite. The same comparison is uniform on compact sets and after every real derivative, because derivatives of the positive quadratic denominator contribute bounded ratios there. Hence (6.1) is smooth and of moderate growth. Rational left multiplication permutes the projective rows, central scalars cancel between numerator and denominator, and the finite maximal compact and real orthogonal group preserve the relevant local row norms. These observations prove all invariances.

On the level-one real slice it is the usual absolutely convergent \(E(z,2)\):

\[
E(z,2)=\tfrac12\sum_{\gcd(c,d)=1}\frac{y^2}{|cz+d|^4}.
\tag{6.2}
\]

Each summand is a hyperbolic translate of \(y^2\), so its Laplace eigenvalue is \(2(1-2)=-2\). Termwise differentiation just justified gives the same eigenvalue for the sum, proving centre finiteness. The two \(c=0\) terms give \(y^2\), and the terms with \(c\ne0\) are \(O(y^{-1})\), uniformly on a strip: the bound
\(\sum_d((d+cx)^2+(cy)^2)^{-2}\leq C(|c|y)^{-3}\)
follows by a nearest-integer term and comparison with the real integral. Sum \(|c|^{-3}\) and multiply by \(y^2\). Positivity gives \(E(z,2)\geq y^2\), so its constant term is nonzero and its squared norm dominates \(\int_Y^\infty y^2dy\). This is an automorphic form outside \(L^2\). Continuation and the unitary Eisenstein spectrum are developed later; neither is used here.

## 7. Exercises with complete solutions

**Exercise 7.1 — a real translation.** Give an explicit finite-compact cuspidal vector whose translate by a noncompact real element has infinitely many rotation weights.

**Solution 7.1.** Use the lowest vector of weight \(k=12\) supplied by \(\phi_\Delta\). Its real positive-weight Hilbert cyclic space can be realized on the holomorphic disk with norm
\(\frac{k-1}{\pi}\int_{|z|<1}|F(z)|^2(1-|z|^2)^{k-2}\,dxdy\).
Polar integration gives \(\|z^n\|^2=n!/(k)_n\). On polynomials the ladder operators are \(P=z^2\partial_z+kz\), \(L=-\partial_z\), \(M=2z\partial_z+k\). Their commutators and adjoints agree with (3.1)–(3.2), and \(P^n1=(k)_nz^n\) has exactly the norm in (5.1). Thus the basis identification extends to a unitary identification with the cyclic space; Lemma 3.1 identifies the real group actions by their Taylor series.

The noncompact group \(a_t=\operatorname{diag}(e^t,e^{-t})\) acts on its lowest vector by

\[
R(a_t)1=(\cosh t-z\sinh t)^{-k}
=(\cosh t)^{-k}\sum_{n=0}^\infty\frac{(k)_n}{n!}(\tanh t)^nz^n.
\tag{7.1}
\]

One can verify the formula by the disk Möbius action, or differentiate it using \(R(H)=P+L\) with value one at \(t=0\). For real \(t\ne0\), every coefficient is nonzero. Since the monomials have distinct weights \(k+2n\), the translated vector has infinite compact orbit. Transferring (7.1) to the automorphic cyclic space gives the claimed cuspidal smooth vector. The norm is preserved by the Möbius change of variables. Its finite adelic level is unchanged, but it leaves the finite-vector space.

**Exercise 7.2 — orthogonality to characters.** For unitary \(\chi\) with \(\chi^2=\omega\), show that every \(u\in H_{\omega,0}\) is orthogonal to \(\chi(\det g)\).

**Solution 7.2.** The full right \(\chi\circ\det\)-isotypic space in \(H_\omega\) is the line spanned by this function. Dividing an isotypic function by it gives a right-invariant function on the transitive homogeneous quotient, and hence a constant almost everywhere. This can be seen without pointwise assumptions by smoothing that quotient function: its smooth right-invariant representatives are constant, and an approximate identity gives the same conclusion in \(L^2\).

The orthogonal projection \(P_c\) onto the closed invariant cuspidal space commutes with all right translations. It therefore preserves this line and acts there by zero or one. The line is not cuspidal: its constant term equals itself, or a compact convolution with nonzero \(\chi\)-integral gives a nonzero multiple whose constant term is nonzero. Thus \(P_c\) is zero on the line. For \(u=P_cu\), self-adjointness of \(P_c\) gives the required zero inner product. No global left-unipotent action on the rational quotient was assumed.

**Exercise 7.3 — a Maass generator.** Let a nonzero cuspidal Maass vector have weight zero, Casimir eigenvalue \(\lambda\), and reflection parity \(\eta\). Prove irreducibility of its real compact module. Explain the role of parity.

**Solution 7.3.** The weight-zero norm equations give \(\lambda\geq0\); equality would annihilate all special-linear generators and make the real cusp average equal the vector itself, so \(\lambda>0\). At each even weight the factors \(\lambda+m(m\pm2)/4\) are positive. Successive raises and lowers therefore generate a nonzero vector at every even weight. Reordering Lie words with (3.1) shows each weight space is one dimensional. A polynomial in \(M\) extracts a weight component from any nonzero submodule, and the nonzero ladder factors take it back to weight zero and then to every other weight. This proves rotation-module irreducibility. Reflection interchanges the ladders and, since \(\epsilon v=\eta v\), preserves the cyclic space; it remains irreducible for the full compact group. If a weight-zero generator has nonzero components in both parity extensions, its full compact cyclic space can contain both irreducible modules. The parity assumption is needed for the stated full-compact conclusion, while the rotation-module assertion needs no parity assumption.

**Exercise 7.4 — reconcile the definitions.** Prove the comparison for fixed unitary central character, including uniqueness of the completion. Identify what fails for a nonunitary central twist.

**Solution 7.4.** For an irreducible Hilbert cusp constituent, admissibility and a finite-dimensional approximate identity smooth every finite vector and supply a reproducing convolution. The basic estimate makes it a bounded smooth cusp form, and the real analytic-vector argument proves algebraic irreducibility and scalar Casimir. Thus its finite vectors give an irreducible admissible submodule of \(\mathcal A_{0,\omega}\).

Conversely rapid decay embeds every form and its derivatives in the cuspidal Hilbert space. Decompose there by compact convolution. Orthogonal projections commute with its type, level and central ideal; each projected finite vector is an automorphic form by the forward argument. Harish-Chandra finiteness makes only finitely many of these mutually orthogonal projections nonzero. Hence \(\mathcal A_{0,\omega}\) is the algebraic sum of the finite-vector modules. A nonzero projection of an irreducible submodule is an isomorphism onto one such simple module. The same direct-sum description treats simple subquotients.

For uniqueness, an algebraic isomorphism is closable by the finite-dimensional type-and-level projections. Its closed graph is real-group invariant by the common analytic radius, and finite-group invariant directly. Polar decomposition and invariant spectral projections of its squared absolute value reduce it to a positive scalar times a unitary intertwiner, as in Lemma 3.3. These steps prove both directions and the isomorphism-class bijection. A nonunitary determinant twist remains algebraically cuspidal but has a central scalar of absolute value different from one; a unitary operator cannot have that action. It therefore lies outside this fixed-unitary-character Hilbert comparison.

## References

- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §§6.2–6.6 and 9.6–9.7. Theorem 6.3.2 is the general arithmetic-finiteness reference; its rational GL₂ case is proved in Lesson 4. Section 2 here proves its admissibility assertion for arbitrary unitary adelic GL₂ representations, and gives an independent cuspidal proof. The [author's graduate-text page](https://sites.duke.edu/jgetz/graduate-text/) supplies the reference. The full comparison is Theorems 6.5.1 and 9.7.3 there; the GL₂ receiving proof here uses explicit ladders and the separately proved compact-kernel estimate.
- P. Deligne, *Formes modulaires et représentations de GL(2)* (1973), §§1.2–1.3, for holomorphic lifts and compact weights.
- The spectrum lesson, Lemma 1.1, Theorems 3.1, 4.2 and 5.2, for closedness, basic estimate, rapid decay and discrete decomposition; the lift lesson, Proposition 3.1 and Theorem 4.1, for the lowering equation and classical dictionary.
