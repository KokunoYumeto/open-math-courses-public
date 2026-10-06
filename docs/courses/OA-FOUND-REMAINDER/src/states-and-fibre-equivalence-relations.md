# States and fibre equivalence relations

*Self-checked by the writing AI. Original text: CC0 1.0.*

An orthogonal representing measure realizes the GNS representation as the full direct integral of the GNS representations of its states. The diagonal algebra then records which components are irreducible or factorial. A related question concerns the relation “these two fibre representations are unitarily equivalent.” We prove that this relation is independent, outside one common null set, of both the separable algebra used to describe a commutant and the faithful normal representation used for the ambient von Neumann algebra.

Prerequisites are [Integral representations of states](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html), specifically Proposition 9.2 and Theorem 10.2 on the operator map of a measure, and [Representations and positive functionals](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html) for GNS. We also use [Base changes and disintegration](../reader/base-changes-and-disintegration.html), especially the simultaneous representation-field theorem and Lemma 3.2 on fibrewise strong subsequences; [Direct integrals of von Neumann algebras](../reader/supplements/direct-integrals-of-von-neumann-algebras-commutants-and-centres-takesa.html), Theorems 4.1 and 4.3 and Lemma 5.1; and the normal-representation theorem, Theorem 8.2, of [Spatial tensor products](../reader/supplements/spatial-tensor-products.html), together with Proposition 6.1 on commutant corners. Diagonal-intertwining unitaries are decomposable by Proposition 6.1 of [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html).

Kostecki’s freely accessible [W*-algebras and noncommutative integration](https://arxiv.org/abs/1307.4818v5) surveys factorial states, orthogonal measures and central decomposition. The proofs below use the linked programme prerequisites and include the nonunital argument in Section 1 and the common-null-set constructions in Sections 4–5. Takesaki’s book and the references in Section 7 provide scholarly context.

Hilbert-space inner products are linear in the first variable. A representation is nondegenerate. Zero fibres can be deleted; assertions about the diagonal are made on the essential base where the Hilbert fibre is nonzero.

## 1. The measurable GNS field, including nonunital algebras

Let \(A\) be a separable C*-algebra and \(S(A)\) its state space. Choose a countable norm-dense subset \((a_n)\) of \(A\). For each state \(\omega\), write
\[
(H_\omega,\pi_\omega,\xi_\omega),\qquad
\eta_\omega(a)=\pi_\omega(a)\xi_\omega
\]
for its GNS construction. Even if \(A\) is nonunital, its GNS vector has norm one and \(\eta_\omega(A)\) is dense in \(H_\omega\).

**Lemma 1.1.** These spaces form a measurable Hilbert field on \(S(A)\), with fundamental sections \(\eta_\omega(a_n)\). Each \(a\in A\) defines the measurable bounded operator field \(\pi_\omega(a)\), of norm at most \(\|a\|\).

**Proof.** The Gram coefficients are
\[
\langle\eta_\omega(a_n),\eta_\omega(a_m)\rangle
=\omega(a_m^*a_n).
\tag{1.1}
\]
They are weak-star continuous functions of the state. The sections are total in every GNS space; the measurable-field construction from a countable positive Gram matrix therefore applies. For any \(a\in A\), approximate \(a\) in norm by elements of the chosen dense set. Since \(\|\eta_\omega(a)\|\leq\|a\|\), the approximation is uniform in \(\omega\), showing that \(\eta_\omega(a)\) is measurable. Finally
\[
\pi_\omega(a)\eta_\omega(b)=\eta_\omega(ab)
\]
is measurable for each fundamental section, and the uniform operator bound proves measurability of the operator field. \(\square\)

Here is how to use the imported state-measure results when \(A\) has no identity. Let \(A^+\) be its unitization, and fix an increasing sequential positive contractive approximate identity \((e_n)\). A state extends canonically to
\[
\omega^+(a+\lambda1)=\omega(a)+\lambda.
\]
The extensions constitute the Borel subset of the compact metrizable \(S(A^+)\) given by
\[
\sup_n\omega^+(e_n)=1.
\tag{1.2}
\]
Restriction identifies this subset with \(S(A)\). A finite Radon measure on \(S(A)\), pushed into \(S(A^+)\), is a finite Borel measure and hence Radon there. Its GNS field and resultant have the same nondegenerate restriction to \(A\).

We also need to preserve the definition of orthogonality used in the state-measure lesson: two positive functionals have no nonzero positive functional dominated by both. This property is preserved by canonical extension. Indeed, the canonical extension of any positive functional \(f\) satisfies
\[
f^+(1)=\|f\|=\lim_n f(e_n).
\]
The extension operation is linear and order preserving: it is obtained from the normal extension to \(A^{**}\) and the unital homomorphism \(A^+\to A^{**}\). A common positive minorant on \(A\) therefore extends to a common minorant on \(A^+\). Conversely, if \(g\leq f^+\) is positive on \(A^+\), then
\[
0\leq g(1-e_n)\leq f^+(1-e_n)\longrightarrow0.
\]
Thus \(g(1)=\lim_n g(e_n)\), and \(g\) is the canonical extension of its restriction. In particular a dominated \(g\) restricting to zero is zero. This proves the reverse implication for common minorants. Consequently the imported characterization of orthogonal measures applies to nonunital \(A\) through this extension, without imposing a new unital hypothesis.

## 2. Orthogonality is exactly surjectivity of the canonical GNS map

Let \(\mu\) be a Radon representing probability measure on \(S(A)\), with resultant
\[
\varphi(a)=\int_{S(A)}\omega(a)\,d\mu(\omega).
\]
If a finite positive representing measure has a state as its resultant, it is necessarily a probability measure: integrate \(\omega(e_n)\uparrow1\) and use \(\varphi(e_n)\uparrow1\). For a unital algebra the same fact follows by evaluating at \(1\).

Put
\[
\mathcal H=\int_{S(A)}^\oplus H_\omega\,d\mu(\omega),\qquad
\pi=\int^\oplus\pi_\omega\,d\mu.
\]
There is a canonical isometry
\[
U:H_\varphi\longrightarrow\mathcal H,\qquad
U\eta_\varphi(a)=(\eta_\omega(a))_\omega.
\tag{2.1}
\]
Equality of inner products follows from the resultant identity and (1.1). The isometry intertwines \(\pi_\varphi(a)\) and \(\pi(a)\).

For \(f\in L^\infty(S(A),\mu)\), let \(m_f\) denote multiplication on \(\mathcal H\). The operator map \(\kappa_\mu\) of the imported state-measure lesson satisfies
\[
\langle\kappa_\mu(f)\eta_\varphi(a),\eta_\varphi(b)\rangle
=\int f(\omega)\omega(b^*a)\,d\mu(\omega).
\]
Thus, without assuming orthogonality,
\[
U^*m_fU=\kappa_\mu(f).
\tag{2.2}
\]

**Theorem 2.1.** The measure \(\mu\) is orthogonal if and only if \(U\) is onto. In that case \(U\) is the canonical unitary equivalence
\[
\pi_\varphi\cong\int^\oplus\pi_\omega\,d\mu(\omega).
\]

**Proof.** Suppose first that \(\mu\) is orthogonal. The imported theorem says precisely that \(\kappa_\mu\) is a *-homomorphism. For \(\zeta\in H_\varphi\), (2.2) gives
\[
\begin{aligned}
\|m_fU\zeta\|^2
&=\langle\kappa_\mu(|f|^2)\zeta,\zeta\rangle\\
&=\|\kappa_\mu(f)\zeta\|^2
=\|U^*m_fU\zeta\|^2.
\end{aligned}
\tag{2.3}
\]
For an isometry \(U\), equality \(\|v\|=\|U^*v\|\) means \(v\in UH_\varphi\), by the orthogonal projection \(UU^*\). Hence the range of \(U\) is invariant under every \(m_f\); applying this to \(\bar f\) makes it reducing.

Let \(\zeta=(\zeta(\omega))\) be perpendicular to this range. For each \(n\) and every bounded measurable \(f\),
\[
0=\langle m_fU\eta_\varphi(a_n),\zeta\rangle
=\int f(\omega)
\langle\eta_\omega(a_n),\zeta(\omega)\rangle\,d\mu(\omega).
\]
The integrand without \(f\) is integrable by Cauchy–Schwarz and the uniform bound on \(\eta_\omega(a_n)\). Testing all indicators shows that it is zero almost everywhere. Outside the union of these countably many null sets, \(\zeta(\omega)\) is perpendicular to every fundamental section, and so is zero. Therefore \(UH_\varphi=\mathcal H\).

Conversely, if \(U\) is onto, (2.2) makes \(\kappa_\mu\) a unitary conjugate of the multiplication representation. It is multiplicative, so the imported characterization says that \(\mu\) is orthogonal. \(\square\)

The countable total family is essential to the proof: the null sets for the individual sections must be combined before concluding that a vector vanishes on almost every fibre.

## 3. Irreducible and factorial components

Let
\[
\pi=\int_X^\oplus\pi_x\,d\mu(x)
\]
be a measurable field of nondegenerate representations of a separable \(A\) over a standard sigma-finite essential base. Write \(D=L^\infty(X,\mu)\) for its diagonal algebra and set
\[
P_x=\pi_x(A)'',\qquad
N=\pi(A)''\vee D,\qquad
C=\pi(A)'\cap D'.
\]
The imported measurable-generation and commutant theorems give
\[
N=\int^\oplus P_x\,d\mu(x),\qquad
C=N'=\int^\oplus P_x'\,d\mu(x).
\tag{3.1}
\]
The common-null-set representation construction justifies testing commutation against a countable dense subset of \(A\).

**Theorem 3.1.**

1. Almost every \(\pi_x\) is irreducible if and only if \(D\) is maximal abelian in \(\pi(A)'\).
2. Almost every \(P_x\) is a factor if and only if
\[
D=C'\cap\pi(A)'.
\tag{3.2}
\]
Equivalently, \(D=Z(C)\).

**Proof.** Since \(D\subseteq\pi(A)'\), maximal abelianness says exactly that \(D'\cap\pi(A)'=D\), or \(C=D\). By (3.1) and uniqueness of measurable algebra fields, this is equivalent to \(P_x'=\mathbb C1\) almost everywhere. That is irreducibility of the nondegenerate fibre representation.

For the second assertion, the centre formula gives
\[
Z(C)=\int^\oplus Z(P_x')\,d\mu(x).
\]
For any von Neumann algebra \(P\), \(Z(P')=P'\cap P=Z(P)\), using \(P''=P\). Thus \(Z(C)=D\) is equivalent to \(Z(P_x)=\mathbb C1\) almost everywhere. Finally \(D\subseteq C\), so an element of \(C'\cap\pi(A)'\) commutes with \(D\) and therefore belongs to \(C\). Hence
\[
C'\cap\pi(A)'=C'\cap C=Z(C),
\]
which proves the claimed equivalence with (3.2). \(\square\)

The algebra \(C\) contains the decomposable operators in the full commutant. A factorial decomposition concerns its centre; it does not require the full commutant to be abelian.

## 4. Changing the separable algebra that describes the commutant

Let \(H=\int_X^\oplus H(x)\,d\mu(x)\) be separable, with diagonal \(D\). Let \(A,B\subseteq B(H)\) be separable C*-algebras commuting with \(D\), and suppose
\[
A''=B''.
\tag{4.1}
\]
Disintegrate their identity representations. Denote the fibre operators by \(a(x)=\pi_x^A(a)\) and \(b(x)=\pi_x^B(b)\).

**Theorem 4.1.** There is one null set \(E\) such that, for every pair \(x,z\notin E\), the unitary intertwiners
\[
V:H(x)\longrightarrow H(z)
\]
of \(\pi_x^A,\pi_z^A\) are exactly the unitary intertwiners of \(\pi_x^B,\pi_z^B\). In particular the two unitary-equivalence relations agree on the entire conull set, including all pairs of its points.

**Proof.** Choose countable norm-dense sets \((a_j)\subseteq A\), \((b_j)\subseteq B\). By Kaplansky density and separability of \(H\), every \(b_j\) is a strong limit of a uniformly bounded sequence \((a_{j,n})\subseteq A\). A bounded net supplied by Kaplansky can be converted to a sequence by testing a countable dense set of Hilbert vectors. For a general \(b_j\), approximate its real and imaginary parts separately.

Lemma 3.2 of the base-changes lesson gives a subsequence with
\[
a_{j,n_k}(x)\longrightarrow b_j(x)
\quad\hbox{strongly for almost every }x.
\tag{4.2}
\]
Apply the same construction to each \(a_j\) using a bounded sequence from \(B\). Delete the union of all these null sets, and the countable null sets needed to identify the selected elements with their representation fields. All the resulting limit identities hold on one conull set.

Suppose \(V\) intertwines the \(A\)-representations at two points \(x,z\) in that set. It intertwines each selected \(a_{j,n_k}\), so (4.2) at both points gives
\[
Vb_j(x)=b_j(z)V.
\]
Norm density extends this identity to all \(b\in B\). The converse uses the selected sequences approximating the \(a_j\). The null set was chosen before the pair and before \(V\), so the conclusion holds for every pair and every unitary intertwiner. \(\square\)

In the source application, \(A'=B'=M\) and \(D\subseteq M\). These hypotheses imply (4.1), and imply that both algebras commute with \(D\).

## 5. Changing the faithful normal ambient representation

We now keep an abstract diagonal inclusion fixed. Let \(M\) have separable predual, and let
\[
\theta:L^\infty(X,\mu)\longrightarrow M
\]
be a faithful normal unital embedding over a standard finite measure base. Let \(\rho_i:M\to B(H_i)\) be faithful normal representations. Choose separable C*-algebras \(A_i\subseteq B(H_i)\) with
\[
A_i'=\rho_i(M).
\tag{5.1}
\]
Decompose \(H_i\) over \(\rho_i\theta(L^\infty)\), using the given base \(X\), and disintegrate the identity representation of \(A_i\).

**Lemma 5.1.** The Hilbert spaces \(H_i\) in this setting are separable.

**Proof.** A von Neumann algebra with separable predual has a faithful normal state. One direct construction is to choose countably many normal functionals separating its positive cone, decompose them into positive normal functionals, and take a norm-convergent positive weighted sum. The positive functionals can be obtained from vector-functional decompositions and polarization. After normalization the sum is a state, and it is faithful because the chosen functionals separate nonzero positive elements.

Adjoin the identity to \(A_i\) if necessary; this preserves (5.1). Choose a maximal orthogonal family of nonzero cyclic \(A_i\)-subspaces. Each is separable, and its projection belongs to \(A_i'=\rho_i(M)\). A faithful normal state permits at most countably many nonzero orthogonal projections: each has positive value, and finite subsums of their values are at most one. Maximality makes the orthogonal sum of the cyclic subspaces all of \(H_i\). It is a countable sum of separable spaces. \(\square\)

The following elementary corner argument is the key to avoiding an unjustified assumption that the ambient representations are spatially equivalent.

**Lemma 5.2.** Let \(C\) be a C*-algebra, \(p\in C\) a projection, and let \(\sigma_1,\sigma_2\) be representations on \(L_1,L_2\) such that
\[
[\sigma_i(C)\sigma_i(p)L_i]=L_i.
\tag{5.2}
\]
Then \(\sigma_1,\sigma_2\) are unitarily equivalent if and only if the induced representations of \(pCp\) on \(\sigma_i(p)L_i\) are unitarily equivalent.

**Proof.** A unitary intertwining \(C\) also intertwines \(p\), so restrict it to the two projection ranges. Conversely let \(W\) intertwine \(pCp\) on those ranges. Define on their algebraic orbit spans
\[
\sum_j\sigma_1(c_j)\xi_j
\longmapsto
\sum_j\sigma_2(c_j)W\xi_j,
\qquad \xi_j\in\sigma_1(p)L_1.
\tag{5.3}
\]
The inner products of two summands are determined by
\[
\langle\sigma_i(c)\xi,\sigma_i(d)\eta\rangle
=\langle\sigma_i(pd^*cp)\xi,\eta\rangle.
\]
Since \(W\) intertwines every \(pd^*cp\), (5.3) preserves inner products. It is well defined and extends to an isometry. Its range is dense by (5.2), hence it is unitary. Multiplying the labels \(c_j\) on the left shows that it intertwines \(C\). \(\square\)

**Theorem 5.3.** There is one null set \(E\subseteq X\) such that, for all \(x,z\notin E\),
\[
\pi_x^{A_1}\cong\pi_z^{A_1}
\quad\Longleftrightarrow\quad
\pi_x^{A_2}\cong\pi_z^{A_2}.
\tag{5.4}
\]
Thus the relation is determined, up to deletion of a null set, by the abstract inclusion \(\theta(L^\infty(X,\mu))\subseteq M\).

**Proof.**

*Step 1: represent the second ambient algebra by faithful induction.* Use the imported normal-representation theorem for \(\rho_2\rho_1^{-1}\). Lemma 5.1 allows a countable amplification; enlarge it to \(K=\ell^2(\mathbb N)\). There are
\[
L=H_1\otimes K,\qquad
N=\rho_1(M)'\bar\otimes B(K),\qquad p\in N,
\]
and a unitary from \(H_2\) onto \(pL\) implementing
\[
\rho_2(m)\longleftrightarrow(\rho_1(m)\otimes1)|_{pL}.
\tag{5.5}
\]
Faithfulness says
\[
[NpL]=L.
\tag{5.6}
\]
The commutant of the algebra on the right of (5.5) is \(pNp|_{pL}\), by the induction commutant formula.

All operators of \(N\), including \(p\), commute with the amplified diagonal. They are therefore decomposable over the same \(X\). The unitary in (5.5) intertwines the two actions of every \(\theta(f)\). Proposition 6.1 of the decomposable-operator lesson makes it a measurable field of fibre unitaries over this same base. We may transport \(A_2\) and its fields to \(pL\); it now has bicommutant \(pNp\).

*Step 2: insert one separable algebra containing the projection.* We may assume \(A_1\) is unital by adjoining the identity. Set
\[
C_0=C^*(A_1\otimes\mathcal K(K),1_L),\qquad
C=C^*(C_0,p),\qquad B=pCp|_{pL}.
\tag{5.7}
\]
These are separable C*-algebras. The matrix units on \(K\) show that
\[
C_0''=N.
\]
Since \(p\in N\), also \(C''=N\); compressing a bounded strongly dense family gives \(B''=pNp\). All three algebras commute with the relevant diagonal and so have simultaneous measurable representation fields.

Apply Theorem 4.1 first to \(C_0,C\) on \(L\), then to \(B\) and the transported \(A_2\) on \(pL\). Outside a common null set their respective equivalence relations agree. Adjoining identities has not altered any unitary intertwining relation.

*Step 3: pass faithfulness to every retained fibre.* Choose a countable norm-dense set \((c_j)\subseteq C\) and a measurable orthonormal fundamental family \((e_l(x))\) for \(L(x)=H_1(x)\otimes K\). The closed fibre span
\[
Q(x)=[\,c_j(x)p(x)e_l(x):j,l\geq1\,]
\]
is measurable, by the Gram–Schmidt construction for a countable field family. Its orthogonal projection defines a decomposable global projection \(Q\). Every vector \(cp\xi\), \(c\in C\), lies in its range. By strong density of \(C\) in \(N\), (5.6) implies
\[
[CpL]=[NpL]=L.
\]
Consequently \(Q=1\), hence \(Q(x)=1\) almost everywhere. This is exactly the hypothesis (5.2) for each retained representation of \(C\).

For any two such fibres, Lemma 5.2 says that their \(C\)-representations are equivalent exactly when their \(B\)-representations on the projection ranges are equivalent. This assertion uses the same algebraic labels \(c\) and \(pcp\) at both points; it requires no measurable choice of a pairwise intertwiner.

*Step 4: remove the amplification.* On \(L(x)\), the representation of \(C_0\) contains the fixed operators \(1\otimes e_{jk}\). A unitary intertwining two \(C_0\)-representations must intertwine all these matrix units. Its matrix entries therefore have the form
\[
V\otimes1_K
\]
for one unitary \(V:H_1(x)\to H_1(z)\): the diagonal matrix units force preservation of the individual coordinates, and the off-diagonal ones force the coordinate operators to agree. Such a unitary intertwines \(C_0\) exactly when \(V\) intertwines \(A_1\), by testing \(a\otimes e_{jk}\).

Combining this fact with Steps 2 and 3 and the fibre unitary transport in Step 1 proves (5.4). All null sets used for the countable algebra fields, projection spans and two applications of Theorem 4.1 were deleted in advance. Their union is independent of the pair \(x,z\), as required. \(\square\)

## 6. Graded exercises with complete solutions

### Exercise 6.1 — Orthogonal measures and nonorthogonal vectors (basic)

In \(A=M_2(\mathbb C)\), let \(v_1=e_1\), \(v_2=(e_1+e_2)/\sqrt2\), and \(\omega_v(a)=\langle av,v\rangle\). Show that
\[
\mu=\tfrac13\delta_{\omega_{v_1}}+\tfrac23\delta_{\omega_{v_2}}
\]
is an orthogonal representing measure, although \(\langle v_1,v_2\rangle\ne0\). What happens for the equal-weight measure on the three states belonging to \(v_1,v_2,e_2\)?

**Solution.** Let
\[
R=\tfrac13v_1v_1^*+\tfrac23v_2v_2^*.
\]
Since the two vectors are linearly independent, \(R\) is positive definite. The GNS space of \(\varphi(a)=\operatorname{Tr}(Ra)\) has dimension four and can be realized by matrices \(aR^{1/2}\) with the Hilbert–Schmidt norm. The canonical map is
\[
aR^{1/2}\longmapsto
\big(\sqrt{1/3}\,av_1,\sqrt{2/3}\,av_2\big).
\]
It is an isometry because the squared norm on either side is \(\operatorname{Tr}(Ra^*a)\). It is onto because prescribing the two images \(av_1,av_2\) determines a unique linear operator \(a\). Theorem 2.1 proves orthogonality. The term concerns the representing measure and its operator map, and does not assert that the vectors in this particular realization are perpendicular.

For three distinct pure states, the direct integral has dimension six. The resultant is still faithful, so its GNS space has dimension four. Its canonical isometry cannot be onto; hence this measure is not orthogonal. One can also see a common positive minorant: the sum of the states of \(v_2,e_2\) has positive definite density, so it dominates a sufficiently small positive multiple of the state of \(v_1\).

### Exercise 6.2 — Factorial fibres with a nonabelian commutant (intermediate)

On \(X=[0,1]\), let every fibre representation of \(M_2(\mathbb C)\) be \(a\mapsto a\otimes1_2\) on \(\mathbb C^2\otimes\mathbb C^2\). Compute \(C=\pi(A)'\cap D'\) and its centre. Decide whether \(D\) is maximal abelian in \(\pi(A)'\).

**Solution.** The fibre algebra and commutant are
\[
P_x=M_2(\mathbb C)\otimes1_2,\qquad
P_x'=1_2\otimes M_2(\mathbb C).
\]
The direct-integral commutant formula gives
\[
C=L^\infty(X)\bar\otimes(1_2\otimes M_2(\mathbb C)).
\]
Its centre is \(D=L^\infty(X)1\). Each \(P_x\) is a factor, so the factorial criterion holds. But \(C\ne D\); for example the constant operator \(1_2\otimes e_{11}\) lies in \(C\setminus D\). Thus \(D\) is not maximal abelian in the full commutant, and the fibres are not irreducible.

### Exercise 6.3 — A full orbit without a full norm ideal (advanced)

Let \(C=\mathcal K(\ell^2)+\mathbb C1\) act on \(\ell^2\), and let \(p\) project onto the first basis vector. Show that \([Cp\ell^2]=\ell^2\), although the norm-closed ideal generated by \(p\) is only \(\mathcal K(\ell^2)\). Extend a unitary of the one-dimensional corner that intertwines \(pCp\) to an intertwiner of this representation of \(C\). Explain the failure for the scalar quotient representation.

**Solution.** The matrix units \(e_{j1}\in C\) send \(p\ell^2\) onto each basis direction, so the orbit span is dense. The operators \(e_{j1}pe_{1k}=e_{jk}\) show that the norm ideal generated by \(p\) contains all finite-rank operators and hence all compacts. Conversely every product \(cpd\) is compact. This ideal does not contain the identity.

The corner is \(pCp=\mathbb C p\). Its unitary is multiplication by a scalar \(\lambda\) with \(|\lambda|=1\). Formula (5.3) sends every \(e_j=e_{j1}e_1\) to \(\lambda e_j\), so its extension is \(\lambda1\), which intertwines all of \(C\). This demonstrates that the dense orbit hypothesis, rather than a norm-full ideal hypothesis, is what Lemma 5.2 uses.

In the scalar quotient representation \(C/\mathcal K\cong\mathbb C\), the projection \(p\) acts as zero. Its corner space is zero and cannot recover the nonzero quotient representation. The dense orbit hypothesis fails there.

## 7. From reduction theory to state measures

There are two ways to organize the same decomposition problem. One starts with a representation and seeks a measurable family of simpler representations. The other starts with a state and seeks a measure whose barycentre is that state. The GNS construction and orthogonality connect them: Theorem 2.1 turns an orthogonal state measure into a direct-integral representation, and the commutant criteria in Section 3 determine whether its fibres are factors or irreducible representations. A measure with the correct barycentre alone does not provide that orthogonal decomposition; Exercise 6.1 exhibits the extra requirement.

Takesaki's Chapter IV Notes place the early representation decompositions of Godement, Mautner and Segal in the setting of von Neumann's reduction theory. The modern organization used in Chapter IV, Section 8 follows Effros's treatment. In our direct-integral lessons this perspective appears concretely in measurable operator fields, the diagonal algebra and its commutant, the passage to fibre commutants, and the construction of a common exceptional null set. The fibre equivalence relation in Theorem 5.3 survives a change of faithful normal representation because amplification and induction preserve the represented algebra and its diagonal action. It therefore belongs to the pair consisting of the algebra and the chosen abelian subalgebra, rather than to a choice of coordinates on each Hilbert fibre.

In the historical account of [Takesaki, Chapter IV Notes, pp. 287–288], the state-space route begins with Tomita's work on representing states by boundary measures. Takesaki credits Ruelle with bringing Choquet boundary integrals into this setting. The operational point is the correspondence between orthogonal representing measures and abelian von Neumann subalgebras of the GNS commutant. In *Integral representations of states*, Proposition 9.2 constructs the operator map, Theorem 10.2 recognizes orthogonality, and Theorem 13.1 proves the correspondence. The Notes specifically attribute their Theorem 6.25 to Ruelle. Recognition of orthogonality by multiplicativity and the equivalence between Choquet ordering of orthogonal measures and inclusion of their abelian algebras are proved in Sections 10 and 14 of that prerequisite. In particular, an ordering of measures has a concrete meaning as an inclusion of subalgebras of the same commutant.

Choosing a maximal abelian subalgebra of the GNS commutant gives the pure-state decomposition in Theorem 19.1 of *Integral representations of states*. The Notes credit Mautner and Segal for the separable case of Takesaki's Theorem 6.28, and Bishop–de Leeuw for the general compact-convex boundary result. These hypotheses change the conclusion. In the general case, every Baire set disjoint from the extreme boundary has measure zero. If the algebra is separable, the state space is metrizable and the pure-state boundary is a Borel set, so the representing measure is actually concentrated there. Theorem 19.1 and Remark 6.7 keep these two statements distinct. No Borel measurability of an arbitrary nonmetrizable extreme boundary is inferred.

Choosing the centre instead of a maximal abelian subalgebra gives the central measure, defined in Section 20 of *Integral representations of states*. Its natural fibre objects are factors. The Notes attribute the formulation for states to Sakai and mention the earlier representation treatments of Ernest and Dixmier. They credit Mautner and Segal for the separable version of Takesaki's Theorem 6.32, and Wils for the general statement. Theorem 20.4 of the prerequisite gives the precise general conclusion: every Baire set missing the factorial states is null. Its Section 21 supplies the additional Borel conclusion for separable algebras. The Notes attribute that factorial-state Borel theorem, Takesaki's Theorem 6.34, to Ernest and Feldman. The countable quantifiers matter in that proof; the prerequisite records and corrects the source's order of intersections and unions.

These choices need not give the same measure. For the normalized trace on \(M_n(\mathbb C)\), the GNS representation is a factor, so the central measure is the single point mass at that trace. A diagonal maximal abelian subalgebra of the right-multiplication commutant instead gives the uniform orthogonal measure on the \(n\) diagonal vector states. The first measure expresses factor decomposition; the second expresses irreducible decomposition. This is Example 22.2 of *Integral representations of states*, and also explains why factorial fibres in Exercise 6.2 need not be irreducible.

A lifting selects measurable representatives compatibly with algebra operations, allowing pointwise construction even when countably many coefficient tests do not control a fibre. *Vector-valued integration and preduals*, Proposition 3.3 and Theorems 8.3 and 9.1, make that use explicit; its separable-fibre arguments use countable tests instead. The programme now supplies the existence argument in [The lifting theorem, Theorem 6.2 and Corollary 6.3](../../measurable-fields-and-direct-integrals/the-lifting-theorem.html#OA-FND-LF-06). Theorem 6.2 assumes a complete, strictly localizable measure space of positive total measure; Corollary 6.3 gives a unital, multiplicative, conjugation-preserving and norm-preserving choice of bounded measurable representatives. For a probability measure, completion adds only subsets of null sets: each completed measurable set differs from an original measurable set by a null set, so the measure algebra is unchanged. Using countably many simple approximations, and enclosing all their exceptional sets in one original measurable null set, likewise identifies the two spaces of essentially bounded function classes. The completed space is strictly localizable with one finite piece, and its total measure is one. Thus the theorem applies without requiring a separable measure algebra. This ordinary lifting does not assert that continuous functions are fixed or that translations commute with it.

The Sakai number in the Notes is \([310]\), but that bibliography entry is his paper on weakly compact operators. The central-decomposition title is the adjacent entry \([311]\), listed below and confirmed by the journal. This bibliographic identification does not change any theorem or transfer a historical paper's proof into this lesson.

## References

- [Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. Chapter IV, Notes, pp. 287–288 (1979 first edition, softcover reprint).
- The historical discussion follows Takesaki’s chapter notes; the mathematical dependencies are the explicitly located programme proofs.
- Representation decompositions of Godement (1951), Mautner (1950) and Segal (1951), and von Neumann's reduction theory (1949): B. Bekka and P. de la Harpe, *Unitary representations of groups, duals, and characters*, [arXiv:1912.07262](https://arxiv.org/abs/1912.07262), Sections 1.G, 1.I and 6.C; B. Blackadar, [*Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*](https://bruceblackadar.com/Mathematics/Cycr.pdf), Sections III.1.6 and III.5.1.
- M. Tomita, [“On rings of operators in non-separable Hilbert spaces,”](https://www.jstage.jst.go.jp/article/kyushumfs/7/2/7_2_129/_pdf) *Memoirs of the Faculty of Science, Kyushu University* **7** (1953), 129–168.
- D. Ruelle, [“States of physical systems,”](https://projecteuclid.org/euclid.cmp/1103839390) *Communications in Mathematical Physics* **3** (1966), 133–150.
- E. Bishop and K. de Leeuw, [“The representation of linear functionals by measures on sets of extreme points,”](https://www.numdam.org/item/10.5802/aif.95.pdf) *Annales de l'Institut Fourier* **9** (1959), 305–331.
- S. Sakai, “On the central decomposition for positive functionals on C*-algebras,” *Transactions of the American Mathematical Society* **118** (1965), 406–419. [Journal record](https://www.ams.org/journals/tran/1965-118-00/home.html?active=allissues), [DOI](https://doi.org/10.1090/S0002-9947-1965-0179640-7).
- J. Ernest, [“A decomposition theory for unitary representations of locally compact groups,”](https://www.ams.org/journals/tran/1962-104-02/S0002-9947-1962-0139959-X/S0002-9947-1962-0139959-X.pdf) *Transactions of the American Mathematical Society* **104** (1962), 252–277.
- J. Dixmier, [“Dual et quasi-dual d'une algèbre de Banach involutive,”](https://www.ams.org/journals/tran/1962-104-02/S0002-9947-1962-0139960-6/S0002-9947-1962-0139960-6.pdf) *Transactions of the American Mathematical Society* **104** (1962), 278–283.
- W. Wils, [“Désintégration centrale des formes positives sur les C*-algèbres,”](https://gallica.bnf.fr/ark:/12148/bpt6k480295b/f837.item) *Comptes Rendus de l'Académie des Sciences, Paris* **267** (1968), 810–812.
- J. Feldman, [“Borel sets of states and of representations,”](https://projecteuclid.org/journals/michigan-mathematical-journal/volume-12/issue-3/Borel-sets-of-states-and-of-representations/10.1307/mmj/1028999373.full) *Michigan Mathematical Journal* **12** (1965), 363–366.
- E. G. Effros, [“Global structure in von Neumann algebras,”](https://www.ams.org/journals/tran/1966-121-02/S0002-9947-1966-0192360-9/S0002-9947-1966-0192360-9.pdf) *Transactions of the American Mathematical Society* **121** (1966), 434–454.
- The prerequisite lessons give the orthogonal-measure, field-commutant, strong-subsequence and amplification results used above, with complete proofs and source attributions.
