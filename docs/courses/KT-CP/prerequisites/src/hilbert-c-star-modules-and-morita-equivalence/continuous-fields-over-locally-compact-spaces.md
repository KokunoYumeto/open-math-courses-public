# Continuous fields over locally compact spaces

*Written by GPT-6.1 Sol (OpenAI), October 2026; the continuous-basis and lifting proofs in Section 7 by Claude Opus 5.5 (Anthropic). Self-checked by the writing AI. Original text: CC0.*

A Hilbert module over \(C_0(X)\) packages Hilbert spaces varying over \(X\). Its inner product records all fibre inner products at once, and the module norm is the supremum of the fibre norms. The fibres alone do not determine the module: one must specify which sections are continuous. This distinction becomes visible when the fibre dimension changes.

Throughout, \(X\) is locally compact Hausdorff, \(A=C_0(X)\), and inner products are linear in the second variable. We use [Hilbert C*-modules](hilbert-c-star-modules.md), [Compact operators, multipliers and the strict topology](compact-operators-multipliers-and-the-strict-topology.md), the frame theorem in [Finite projective modules, frames and K₀](finite-projective-modules-frames-and-k0.md), and [Kasparov's stabilization theorem](kasparovs-stabilization-theorem.md). No countability assumption is needed for the basic correspondence.

## 1. Continuous sections and finite patching

**Definition 1.1.** A continuous field of Hilbert spaces consists of Hilbert spaces \(H_x\) and a vector space \(\Gamma\subseteq\prod_x H_x\) of sections with these properties:

1. \(\Gamma\) is closed under multiplication by continuous scalar functions on \(X\).
2. \(x\mapsto\|\xi(x)\|\) is continuous for every \(\xi\in\Gamma\).
3. \(\{\xi(x):\xi\in\Gamma\}\) is dense in \(H_x\).
4. If a section is uniformly approximable near each point, to every positive accuracy, by members of \(\Gamma\), it belongs to \(\Gamma\).

Polarization shows that \(\langle\xi(x),\eta(x)\rangle\) is continuous. The space
\[
\Gamma_0(H)=\{\xi\in\Gamma:\|\xi(\,\cdot\,)\|\in C_0(X)\}
\tag{1.1}
\]
has norm \(\|\xi\|=\sup_x\|\xi(x)\|\). Local sections on an open set are defined by the same local approximation rule there. Thus neither boundedness nor vanishing at infinity is required of a member of \(\Gamma\).

We will repeatedly use finite partitions on a compact set. If \(K\subseteq X\) is compact and \(U_1,\ldots,U_m\) cover it, one can choose
\[
\phi_i\in C_c(X),\quad \phi_i\geq0,\quad
\operatorname{supp}\phi_i\subseteq U_i,\quad
\sum_i\phi_i\leq1,\quad \sum_i\phi_i=1\text{ on }K.
\tag{1.2}
\]
Here is the construction from the usual locally compact cutoff property. Choose nonnegative compactly supported \(u_i\) in \(U_i\) whose sum \(s\) is positive on \(K\), by first taking a finite collection of cutoffs around its points and grouping them by \(U_i\). Choose \(0\leq\chi\leq1\), compactly supported in \(\{s>0\}\), with \(\chi=1\) on \(K\). Set \(\phi_i=\chi u_i/s\) there and zero elsewhere. The cutoff property itself follows by applying Urysohn's lemma in the one-point compactification, after taking a relatively compact neighborhood of the given compact set.

**Lemma 1.2 (Patching).** Let \(\mathcal S\subseteq\Gamma_0(H)\) be a closed \(C_0(X)\)-submodule. If \(\mathcal S(x)\) is dense in every fibre, then \(\mathcal S=\Gamma_0(H)\).

*Proof.* Given \(\xi\in\Gamma_0(H)\) and \(\varepsilon>0\), put
\(K=\{x:\|\xi(x)\|\geq\varepsilon\}\), which is compact. At each point of \(K\), choose \(\eta_i\in\mathcal S\) approximating its value within \(\varepsilon\). Continuity of \(\|\xi-\eta_i\|\) gives finitely many neighborhoods \(U_i\) covering \(K\) on which that estimate holds. Choose (1.2), and put \(\eta=\sum_i\eta_i\phi_i\in\mathcal S\). Pointwise,
\[
\xi-\eta=\sum_i\phi_i(\xi-\eta_i)
 +(1-\sum_i\phi_i)\xi .
\tag{1.3}
\]
Where the last coefficient is nonzero outside \(K\), \(\|\xi(x)\|<\varepsilon\); on \(K\) it is zero. All coefficients are nonnegative and sum to one, so \(\|\xi-\eta\|\leq\varepsilon\). The case \(K=\varnothing\) uses \(\eta=0\). Closedness proves the result. ∎

The same proof applies to a section vanishing at infinity that is locally approximable by a prescribed module of sections: local approximation supplies the \(\eta_i\). Only a finite cover of \(K\) is used, so \(X\) need not be paracompact.

## 2. Extracting fibres from a module

For a Hilbert \(A\)-module \(E\), set
\[
I_x=\{a\in A:a(x)=0\},\qquad
N_x=\{\xi\in E\mid \langle\xi,\xi\rangle(x)=0\}.
\]
Write \(EI_x\) for the closed linear span of products \(\xi a\), \(a\in I_x\).

**Proposition 2.1.** One has \(N_x=EI_x\), and
\[
E_x=E/N_x,\qquad
\langle[\xi]_x,[\eta]_x\rangle
 =\langle\xi,\eta\rangle(x)
\tag{2.1}
\]
is a complete Hilbert space. Its norm is the quotient norm:
\[
\|[\xi]_x\|=\langle\xi,\xi\rangle(x)^{1/2}.
\tag{2.2}
\]
It is canonically \(E\otimes_{\mathrm{ev}_x}\mathbb C\).

*Proof.* Evaluating the module Cauchy–Schwarz inequality shows that vectors in \(N_x\) pair to zero with every vector at \(x\). This makes (2.1) well defined and makes \(N_x\) a closed submodule. Products with \(I_x\) lie in \(N_x\).

If \(\xi\in N_x\), the function \(y\mapsto\langle\xi,\xi\rangle(y)^{1/2}\) is in \(C_0(X)\) and is zero at \(x\). The compact set on which it is at least \(\varepsilon\) misses a neighborhood of \(x\). Choose \(0\leq a\leq1\) in \(C_c(X)\), equal to one on that compact set and zero at \(x\). Then \(\|\xi-\xi a\|\leq\varepsilon\). Thus \(N_x=EI_x\).

The scalar norm in (2.2) is at most the quotient norm. For the reverse inequality, choose a neighborhood of \(x\) on which the scalar norm of \(\xi\) is below \(\|[\xi]_x\|+\varepsilon\), and a cutoff \(f\) supported there with \(f(x)=1\). The vector \(\xi f\) represents the same class and has module norm at most that bound. This proves equality. The Banach quotient is complete, proving the Hilbert-space assertion. Finally \(\xi\otimes z\mapsto[\xi]_x z\) respects balancing and the tensor inner product; its range is all of the complete quotient, so it gives the claimed unitary. ∎

Let \(\widehat\xi(x)=[\xi]_x\). Then
\[
\|\xi\|=\sup_x\|\widehat\xi(x)\|,
\qquad
\langle\widehat\xi(x),\widehat\eta(x)\rangle
=\langle\xi,\eta\rangle(x).
\tag{2.3}
\]
Define \(\Gamma_E\) to consist of sections locally uniformly approximable by the \(\widehat\xi\), \(\xi\in E\).

**Theorem 2.2 (Module to field).** The spaces \(E_x\), with \(\Gamma_E\), form a continuous field, and
\[
E\xrightarrow{\ \xi\mapsto\widehat\xi\ }
\Gamma_0(E_x)
\tag{2.4}
\]
is a unitary \(C_0(X)\)-module isomorphism.

*Proof.* Local uniform limits of continuous norm functions have continuous norms. Values of the original sections are already all of each fibre by Proposition 2.1. Sums and scalar multiples preserve local approximation. Multiplication by \(f\in C(X)\) does too: near a point \(x\), approximate a section by \(\widehat\xi\), and then approximate \(f\widehat\xi\) by \(f(x)\widehat\xi\), shrinking the neighborhood and using local boundedness of the norms. The approximation rule is idempotent, by applying it twice with half the required accuracy. Thus all four field axioms hold.

Equation (2.3) makes (2.4) isometric and inner-product preserving. Its range is a closed \(A\)-submodule, total in each fibre; Lemma 1.2 makes it all of \(\Gamma_0\). ∎

## 3. Recovering a module from a field

**Theorem 3.1 (Field to module).** For every continuous field, \(\Gamma_0(H)\) is a Hilbert \(C_0(X)\)-module under pointwise operations and inner product. Its associated field is canonically the original field. Thus these constructions are inverse, up to canonical unitary isomorphism.

*Proof.* The pointwise inner product is continuous by polarization and vanishes at infinity since
\[
|\langle\xi(x),\eta(x)\rangle|
\leq\|\xi(x)\|\|\eta(x)\|.
\]
It is positive definite on sections and has exactly the supremum norm. A uniformly Cauchy sequence has a pointwise Hilbert-space limit, approached uniformly; local uniform closure makes the limit continuous, and uniform approximation preserves vanishing at infinity. Hence the module is complete.

At \(x\), evaluation has dense range: a member of \(\Gamma\) can be multiplied by a compactly supported cutoff equal to one at \(x\), giving a member of \(\Gamma_0\) with that value. The quotient-norm cutoff argument of Proposition 2.1 applies equally to this evaluation map. It identifies the complete quotient fibre isometrically with a dense, hence closed and surjective, subspace of \(H_x\). These fibre unitaries send original sections to their values.

Finally any \(\xi\in\Gamma\) agrees near each point with a member of \(\Gamma_0\): multiply it by a cutoff equal to one on a neighborhood. Its norm is bounded on the compact support, so that product vanishes at infinity. Consequently the local approximation closure of \(\Gamma_0\) is exactly \(\Gamma\). ∎

The correspondence also preserves adjointable operators. If \(T\in\mathcal L(E,F)\), it induces \(T_x:E_x\to F_x\), with
\[
(T^*)_x=(T_x)^*,\qquad
\|T\|=\sup_x\|T_x\|.
\tag{3.1}
\]
Indeed a bounded module map preserves \(EI_x\), so descends to the quotient with norm at most \(\|T\|\); inner products give the adjoint equality. Conversely (2.3) bounds \(\|T\xi\|\) by \((\sup_x\|T_x\|)\|\xi\|\). A uniformly bounded family \(T_x\) gives an adjointable map precisely when both \(T_x\) and its pointwise adjoint send continuous sections vanishing at infinity to such sections. The inner-product identity then supplies the module adjoint. Local cutoffs give the equivalent formulation using all local continuous sections.

## 4. The continuous field of compact operators

The fibre of a rank-one operator is
\[
(\theta_{\xi,\eta})_x
=\theta_{\xi(x),\eta(x)},\qquad
\theta_{\xi,\eta}\zeta=\xi\langle\eta,\zeta\rangle.
\tag{4.1}
\]
This follows either directly on quotient vectors or by tensoring.

**Lemma 4.1.** For every \(k\in\mathcal K(E)\), \(x\mapsto\|k_x\|\) is continuous and vanishes at infinity, and \(\|k\|=\sup_x\|k_x\|\). Evaluation maps \(\mathcal K(E)\) onto \(\mathcal K(E_x)\).

*Proof.* First let \(k=\sum_{j=1}^m\theta_{\xi_j,\eta_j}\). At a fixed \(x\), let \(V,W:\mathbb C^m\to E_x\) have columns \(\xi_j(x),\eta_j(x)\), and let \(G_\xi=V^*V\), \(G_\eta=W^*W\). Then \(k_x=VW^*\) and
\[
\|k_x\|^2
=\|G_\xi^{1/2}G_\eta G_\xi^{1/2}\|.
\tag{4.2}
\]
To check it, write \(\|VW^*\|^2=\|WG_\xi W^*\|\) and use \(\|SS^*\|=\|S^*S\|\) for \(S=WG_\xi^{1/2}\). The entries of the Gram matrices are continuous. Continuous square roots and matrix norms make (4.2) continuous, even where ranks change. Also
\[
\|k_x\|\leq\sum_j\|\xi_j(x)\|\|\eta_j(x)\|,
\]
which vanishes at infinity. Norm approximation by finite ranks gives uniform approximation of these norm functions, proving the assertions for all \(k\); the norm equality is (3.1).

Evaluation is a *-homomorphism. Every vector of \(E_x\) is a section value, so its image contains all fibre rank ones. The image of a C*-homomorphism is closed, and hence is the whole compact algebra. ∎

**Theorem 4.2.** The algebras \(\mathcal K(E_x)\) form a continuous field of C*-algebras, whose algebra of sections vanishing at infinity is canonically \(\mathcal K(E)\).

*Proof.* Declare a compact-operator section continuous when it is locally uniformly approximable in operator norm by finite sums (4.1). Sums and adjoints preserve this class. Products do because
\[
\theta_{\xi,\eta}\theta_{\zeta,\omega}
=\theta_{\xi\langle\eta,\zeta\rangle,\omega};
\]
local approximation also preserves products, using local norm boundedness. Norm functions are continuous by Lemma 4.1 and local approximation. All fibre compacts are section values by its surjectivity conclusion.

An operator section in this class vanishing at infinity can be patched, exactly as in (1.3), into a uniform limit of finite-rank sections. Multiplication of a rank one by \(\phi\in C_c(X)\) is again a module rank one, since the scalar can be absorbed in its first vector. Thus the patched sections belong to \(\mathcal K(E)\); this algebra is norm closed. Conversely a module compact is locally approximable by finite ranks and has norm vanishing at infinity. The norm equality makes the identification isometric. This proves all the continuous-field axioms in [Blackadar 2006, IV.1.6.1], including exact fibre evaluation and local uniform closure for vanishing sections. Zero fibres are allowed. ∎

The kernel of evaluation at \(x\) is \(\overline{I_x\mathcal K(E)}\). Inclusion in the kernel is immediate. For the reverse inclusion, if \(k_x=0\), the continuous norm function from Lemma 4.1 allows the same cutoff argument as in Proposition 2.1 to approximate \(k\) by \(ak\), \(a(x)=0\).

The open support
\[
U=\{x:E_x\ne0\}
\tag{4.3}
\]
also records module fullness. The closed ideal generated by the inner products is exactly \(C_0(U)\). To verify the nontrivial inclusion, a compact subset of \(U\) has a finite cover on which a sum \(g=\sum_j\langle\xi_j,\xi_j\rangle\) is positive. A cutoff supported in \(\{g>0\}\) is a continuous scalar multiple of \(g\), so belongs to the inner-product ideal. Taking that cutoff equal to one on the support of a given \(f\in C_c(U)\) puts \(f\) in the ideal too, and \(C_c(U)\) is dense in \(C_0(U)\). Therefore \(E\) is full over \(C_0(X)\) exactly when every fibre is nonzero.

## 5. Finite constant rank gives a vector bundle

**Theorem 5.1.** If a continuous field has constant finite dimension \(n\), it is a Hermitian vector bundle of rank \(n\). If \(X\) is compact, its section module is finitely generated projective over \(C(X)\).

*Proof.* At \(x\), choose \(\xi_1,\ldots,\xi_n\in\Gamma_0(H)\) whose values form a basis; exact evaluation was proved in Theorem 3.1. Their Gram matrix \(G(y)\) is continuous and invertible on a neighborhood \(V\) of \(x\). Its continuous inverse square root gives local sections
\[
u_j(y)=\sum_i\xi_i(y)(G(y)^{-1/2})_{ij}.
\tag{5.1}
\]
They are orthonormal in each fibre on \(V\), and they span because the dimension is \(n\). A section on \(V\) is continuous exactly when its coordinates \(\langle u_j(y),\xi(y)\rangle\) are continuous. One implication uses continuous inner products; the other uses the local-section axioms on \(\sum_j u_j c_j\). Thus these coordinates give a local trivialization. On overlaps the coordinate changes are continuous unitary matrices, furnishing the vector-bundle structure.

For compact \(X\), choose a finite collection of these neighborhoods and nonnegative functions \(\rho_i\) supported inside them with \(\sum_i\rho_i=1\). Extend
\(\zeta_{ij}=\sqrt{\rho_i}\,u_j\) by zero. They are continuous across the boundaries since their norms are \(\sqrt{\rho_i}\). Pointwise,
\[
\sum_{i,j}\theta_{\zeta_{ij},\zeta_{ij}}=1.
\tag{5.2}
\]
Let \(N\) be their number and \(W:\Gamma(H)\to C(X)^N\) be the analysis map with coordinates \(\langle\zeta_{ij},\xi\rangle\). Equation (5.2) gives \(W^*W=1\). Hence \(p=WW^*\) is a continuous matrix projection and \(W\) identifies the module with \(pC(X)^N\), proving finite projectivity. This is precisely the frame projection of the preceding finite-projective-module lesson. The zero-rank case gives the zero module. ∎

Conversely a continuous matrix projection over compact \(X\) has locally constant rank. If \(\|p-q\|<1\), the restrictions of \(q\) to \(\operatorname{ran}p\) and of \(p\) to \(\operatorname{ran}q\) are injective: a vector in either kernel would satisfy \(\|v\|\leq\|p-q\|\|v\|\). The two finite-dimensional ranges therefore have equal dimension. Local basis sections obtained by applying the varying projection to a basis at a fixed point remain independent and hence span nearby. Its ranges and sections form a vector bundle with the field topology just described.

There is a useful constraint on changing rank.

**Proposition 5.2.** In any continuous field, for every positive integer \(m\), the set
\[
\{x:\dim H_x\geq m\}
\tag{5.3}
\]
is open.

*Proof.* At such a point choose \(m\) independent section values. Their Gram determinant is positive there, and stays positive on a neighborhood by continuity. Those values stay independent throughout the neighborhood. ∎

Thus finite fibre dimension is lower semicontinuous. A limit point cannot have two independent directions while every other nearby fibre has only one, by (5.3).

## 6. Bundles, jumping ranks and the standard module

**Example 6.1.** If \(V\to X\) is a Hermitian vector bundle, its continuous sections give a continuous field and \(\Gamma_0(V)\) is its Hilbert module. Local orthonormal frames verify the norm and local closure axioms; a cutoff extends any chosen local vector to a global section. Theorem 3.1 recovers the original fibres and continuous sections. For compact \(X\), Theorem 5.1 gives the usual projection presentation of its section module.

**Example 6.2 (A genuine dimension jump).** Let
\[
\begin{aligned}
A&=C([0,1]),\\
I&=\{b\in A:b(0)=0\},\\
E&=A\oplus I .
\end{aligned}
\tag{6.1}
\]
Its inner product is \(\overline a c+\overline b d\). Evaluation identifies
\[
E_0=\mathbb C,\qquad E_t=\mathbb C^2\quad(t>0).
\tag{6.2}
\]
At zero, the entire second summand lies in the null space; at \(t>0\) its evaluation is onto \(\mathbb C\) by cutoffs in \((0,1]\). Sections are pairs of continuous scalar functions whose second coordinate tends to zero at zero. Their norms are continuous. By Theorem 2.2 this is a continuous field with those fibres. It is not locally a vector bundle at zero, since local triviality would make rank constant there.

Its compact algebra has a particularly concrete description:
\[
\mathcal K(E)\cong
\left\{f\in C([0,1],M_2(\mathbb C)):
 f(0)=\begin{pmatrix}\lambda&0\\0&0\end{pmatrix}\right\}.
\tag{6.3}
\]
Indeed its four matrix corners are \(A,I,I,I\). Rank-one formulas give the first corner and dense spans in the other three: products of two elements of \(I\) span \(I\), using its approximate identity, and multiplication by elements of \(A\) preserves it. The resulting matrix action is isometric by (3.1), and each such matrix preserves \(A\oplus I\); hence the closed corners give exactly (6.3). Its fibre algebra is \(\mathbb C\) at zero and \(M_2\) elsewhere.

An adjointable field need not have a continuous operator-norm function. On this same module, let
\[
T(a,b)(t)=(0,\sin(1/t)b(t))\quad(t>0),\qquad
T(a,b)(0)=0.
\]
The second coordinate is continuous at zero because \(b(0)=0\); its adjoint is itself and \(\|T\|\leq1\). Nevertheless \(\|T_t\|=|\sin(1/t)|\) for \(t>0\), whereas \(\|T_0\|=0\). This contrasts with the norm continuity for module compacts in Lemma 4.1.

**Example 6.3 (The constant infinite-dimensional field).** One has
\[
H_{C_0(X)}\cong C_0(X,\ell^2),\qquad
(a_j)_j\longmapsto\bigl(x\mapsto(a_j(x))_j\bigr).
\tag{6.4}
\]
Finite columns preserve inner products and norms. A norm-convergent sum \(\sum_j|a_j|^2\) makes their vector-valued partial sums converge uniformly, giving a continuous section vanishing at infinity. Conversely the image of a \(C_0\) section, together with zero, has compact closure in \(\ell^2\). Finite-coordinate projections converge uniformly on this compact set: a finite \(\varepsilon\)-net reduces it to finitely many vectors. Thus its coordinate tails are uniformly small, which is exactly norm convergence of \(\sum_j|a_j|^2\). This proves (6.4) for arbitrary \(X\). For compact \(X\) it reads \(H_{C(X)}=C(X,\ell^2)\).

## 7. Countability, stabilization and two Dixmier–Douady results

Call a field separable when there is a countable family of continuous sections whose values have dense linear span in every fibre. This is a condition on sections. It implies that every fibre is separable.

**Proposition 7.1.** A module \(E=\Gamma_0(H)\) is countably generated exactly when it has a countable family in \(\Gamma_0(H)\) total in every fibre. If \(X\) is \(\sigma\)-compact, a separable field has a countably generated section module.

*Proof.* Generators are total after taking fibre quotients. Conversely the closed module generated by a countable total family has dense values in every fibre, so Lemma 1.2 makes it all of \(E\).

For the second assertion take total \(\xi_n\in\Gamma\) and compactly supported cutoffs \(\chi_j\) such that at least one \(\chi_j(x)\) equals one at each \(x\). Such a countable family exists by covering a compact exhaustion with relatively compact neighborhoods. The sections \(\xi_n\chi_j\) are in \(\Gamma_0\) and are fibrewise total, so the first assertion applies. ∎

**Example 7.2 (Separable fibres do not suffice).** Let \(D\) be an uncountable discrete set and \(X=D\cup\{\infty\}\) its one-point compactification. Put
\[
E=C(X)\oplus C_0(D),
\tag{7.1}
\]
regarding the second summand as the functions on \(X\) zero at \(\infty\). Every fibre is nonzero and finite dimensional: dimension one at \(\infty\), two at \(d\in D\). But \(E\) is not countably generated. Each \(b\in C_0(D)\) has countable support, since \(\{d:|b(d)|\geq1/n\}\) is finite for each \(n\). The second coordinates of any countable proposed generating family are therefore supported in a single countable subset of \(D\). Module multiplication and norm closure cannot generate the function supported at a point outside that subset. Thus even compactness of the base and separability of every fibre do not imply the section-countability hypothesis.

**Theorem 7.3 (Stabilization in field form).** For a countably generated \(E\),
\[
E\oplus C_0(X,\ell^2)\cong C_0(X,\ell^2)
\tag{7.2}
\]
by a unitary of section modules and hence by continuous fibre unitaries. If \(E\) is full as well, then \(X\) is \(\sigma\)-compact and
\[
E^\infty\cong C_0(X,\ell^2).
\tag{7.3}
\]

*Proof.* Apply *Kasparov's stabilization theorem*, Theorem 3.1, and use (6.4). For the full case, countable generators \(\xi_n\) are total at every point, with at least one nonzero value there. Consequently
\[
X=\bigcup_{n,m\geq1}
\{x:\|\xi_n(x)\|\geq1/m\},
\]
a countable union of compact sets. Thus \(C_0(X)\) is \(\sigma\)-unital: cutoffs from a compact exhaustion give a countable approximate identity. The full-amplification theorem of the stabilization lesson, Theorem 4.2, proves (7.3). ∎

Equation (7.2) requires neither fullness nor a dimension bound. Triviality of the original field is a stronger statement:

### Trivializing an infinite-dimensional field

The argument below first represents a countable-total field by projections, then builds continuous orthonormal bases of their ranges. Finite covering dimension supplies the second step.

**Sources.** The field-triviality theorem is due to Jacques Dixmier and Adrien Douady [Dixmier–Douady]. Marina Prokhorova [Prokhorova] proves the projection-lifting step with Michael's selection theorem and Kakutani's theorem on spheres; the proofs below use a covering-dimension argument instead.

**Lemma (Paracompact patching).** A paracompact Hausdorff space is normal. Every open cover has a locally finite subordinate partition of unity. A locally finite open cover \((U_i)\) has a locally finite closed shrinking \((F_i)\) that still covers the space and satisfies \(F_i\subset U_i\).

*Proof.* First fix a point \(x\) outside a closed set \(F\). Separate \(x\) from each \(y\in F\) by disjoint open neighborhoods. Refine the cover consisting of these \(y\)-neighborhoods and \(X\setminus F\) locally finitely. Assign each refined member to one containing old member. The members that meet \(F\) must be assigned to \(y\)-neighborhoods; their closures avoid \(x\). The union of these closures is closed, since the family is locally finite, and its complement is a neighborhood of \(x\). The closure of that complement misses \(F\), since \(F\) is contained in the union of the corresponding open members. This proves regularity.

For disjoint closed \(F,G\), regularity gives neighborhoods of the points of \(F\) with closures missing \(G\). Refine their union with \(X\setminus F\) locally finitely. The union of the refined members meeting \(F\) contains \(F\) and has closure disjoint from \(G\). This proves normality. The dyadic construction in Section 5 of *Finite projective modules, frames and K₀* therefore gives separating functions on this space too.

Given any open cover, first choose neighborhoods whose closures lie in its members and then take a locally finite refinement. Group refined members by their assigned old labels. Their grouped open sets \(V_i\) still cover \(X\), are locally finite, and satisfy \(\overline V_i\subset U_i\): locally finite unions of closures are closed. Thus \(F_i=\overline V_i\) is a closed shrinking of the resulting locally finite cover, with repeated labels grouped when necessary. For a cover already locally finite the same construction gives a closed shrinking indexed by that cover.

Normality lets us insert an open neighborhood \(W_i\) of \(F_i\) with \(\overline W_i\subset U_i\), and a further neighborhood between them. A separating function can consequently be chosen to equal one on \(F_i\) and have support inside \(U_i\). These functions form a locally finite family and have positive sum. Dividing by that sum gives a subordinate partition of unity. For a cover not initially locally finite, apply this construction to its locally finite refinement and sum the functions assigned to each original label. ∎

For a paracompact Hausdorff space, we use the cover-refinement formulation of \(\dim X\leq d\): every open cover admits a locally finite open refinement with no point in more than \(d+1\) members. Closed subspaces inherit paracompactness and this bound. Indeed, extend a cover of a closed subspace \(F\) to ambient open sets, add \(X\setminus F\), refine, and restrict to \(F\).

**Lemma (Avoiding zero in a finite-dimensional target).** Let \(\dim X\leq d<N\), let \(g:X\to\mathbb R^N\) be continuous, and let \(\delta:X\to(0,\infty)\) be continuous. There is continuous \(f:X\to\mathbb R^N\setminus\{0\}\) with \(\|f(x)-g(x)\|<\delta(x)\).

*Proof.* Choose a countable dense set \(D\subset\mathbb R^N\) such that every collection of at most \(N\) distinct members is linearly independent. Construct it by visiting every member of a countable base of balls and choosing the next point outside the spans of all collections of at most \(N-1\) preceding points. At each finite stage there are only finitely many proper subspaces to avoid, and their union cannot contain an open ball.

For each \(y\), choose a neighborhood \(V_y\) on which
\[
\|g(x)-g(y)\|<\delta(y)/8,\qquad \delta(x)>\delta(y)/2.
\]
Take a locally finite refinement \((U_i)\) of multiplicity at most \(d+1\), with \(U_i\subset V_{y_i}\), and a subordinate partition \((\rho_i)\). Choose \(v_i\in D\) with \(\|v_i-g(y_i)\|<\delta(y_i)/8\), and set
\[
f(x)=\sum_i\rho_i(x)v_i.
\]
The sum is locally finite and hence continuous. For each active term, \(\|v_i-g(x)\|<\delta(x)/2\), proving the approximation. At most \(d+1\leq N\) terms are active. After grouping equal \(v_i\), a vanishing value would be a nontrivial linear relation among at most \(N\) distinct members of \(D\), with positive coefficients summing to one. That contradicts their independence. ∎

**Lemma (A nowhere-zero perturbation of a section).** Let \(p:X\to B(H)\) be a strongly continuous orthogonal projection with infinite-dimensional range at every point, where \(X\) is paracompact Hausdorff and \(\dim X\leq d<\infty\). Every continuous section \(\eta(x)\in p_xH\) and every \(\varepsilon>0\) admit a continuous nowhere-zero section \(s(x)\in p_xH\) with \(\|s(x)-\eta(x)\|<\varepsilon\).

*Proof.* Choose an integer \(r\) with \(2r>d\). At each point choose \(r\) orthonormal range vectors. Project those fixed vectors by \(p_x\); their Gram matrix stays invertible nearby. Multiplication by its continuous inverse square root gives a continuous orthonormal \(r\)-frame on a neighborhood. Thus there is a locally finite cover \((U_i)\) by such frame domains.

Choose closed sets \(F_i\subset U_i\) covering \(X\). Insert neighborhoods so that there are closed \(G_i\subset U_i\) and functions \(0\leq\chi_i\leq1\), with \(\chi_i=1\) on \(F_i\) and \(\operatorname{supp}\chi_i\subset\operatorname{int}G_i\). All these families are locally finite. There is continuous \(M:X\to[1,\infty)\) that bounds the number of \(U_i\) containing any point. To construct it, cover \(X\) by neighborhoods each meeting only finitely many \(U_i\), assign to each neighborhood a positive integer bounding that number, and average those integers with a subordinate partition of unity.

Well-order the index set. We modify the section on one domain at a time. Before step \(i\), let \(t\) be the current section, nonzero on the closed set \(A_i=\bigcup_{j<i}F_j\). This union is closed by local finiteness. Put \(b(x)=\varepsilon/(2M(x))\). Take a partition \(\alpha+\beta=1\) subordinate to the two open sets \(\{\|t\|>0\}\) and \(X\setminus A_i\), respectively, and put
\[
\delta_i(x)=b(x)\left[
\alpha(x)\min\left(1,\frac{\|t(x)\|}{2b(x)}\right)+\beta(x)\right].
\]
This function is positive and continuous, at most \(b\), and at most \(\|t\|/2\) on \(A_i\). If \(t=0\), the subordinate function \(\alpha\) is zero and \(\beta=1\); if \(\beta=0\), then \(\alpha=1\) and \(t\ne0\). These observations prove strict positivity.

On \(G_i\), write \(g_i\) for the \(r\) complex frame coordinates of \(t\), identified with a map to \(\mathbb R^{2r}\). The preceding lemma, applied to the closed subspace \(G_i\), gives nonzero \(f_i\) with \(\|f_i-g_i\|<\delta_i\). Add to \(t\) the section with frame coordinates \(\chi_i(f_i-g_i)\), extending it by zero outside \(G_i\). Its support lies in \(\operatorname{int}G_i\), so the extension is continuous. On \(F_i\) the new frame coordinates are \(f_i\), so the new section is nonzero. On \(A_i\) its change has norm less than \(\|t\|/2\), preserving nonvanishing there.

At a limit stage use the accumulated modifications. Near each point only finitely many domains occur, so this definition involves finitely many modifications locally and is continuous. The same observation justifies transfinite induction and gives a continuous final section \(s\). Each point belongs to some \(F_i\); after that step it stays nonzero through the finitely many subsequent modifications affecting it. Finally, if \(k\) modifications affect \(x\), then \(k\leq M(x)\), and
\[
\|s(x)-\eta(x)\|<k\,\frac{\varepsilon}{2M(x)}
\leq\varepsilon/2<\varepsilon.
\]
The case of no modifications has error zero. ∎

Normalizing \(s\) gives a continuous unit section \(\xi=s/\|s\|\) with
\[
\operatorname{dist}\bigl(\eta(x),\mathbb C\xi(x)\bigr)<\varepsilon.
\]
This unit-section approximation is the input for the continuous orthonormal bases below.

**Lemma (A countable-total field inside a constant field).** A continuous Hilbert field over a normal Hausdorff space, with a countable family of continuous sections total in each fibre, is isomorphic to the range field of a strongly continuous projection on \(\ell^2\). The projection can be chosen with infinite-dimensional kernel at every point.

*Proof.* Let \(D=C_b(X)\). Replace each total section \(s_n\) by \(s_n/(1+\|s_n(\cdot)\|)\). These are bounded continuous sections and remain total. Bounded continuous sections form a Hilbert \(D\)-module in their supremum norm: polarization makes their inner products continuous, and uniform limits are continuous by the field's local approximation axiom. Let \(E'\) be the closed \(D\)-span of this countable family. It is countably generated even when \(X\) is not σ-compact. This auxiliary module need not contain every bounded section.

Evaluation identifies its quotient fibre with \(H_x\). To prove the exact norm statement, let \(v\in E'\). For every \(\varepsilon>0\), continuity gives a neighborhood \(U\) of \(x\) on which \(\|v(y)\|<\|v(x)\|+\varepsilon\). Normality supplies \(0\leq b\leq1\) in \(C_b(X)\), with \(b(x)=1\) and support inside \(U\). The vectors \(v\) and \(bv\) have the same quotient class modulo \(\overline{E'I_x}\), where \(I_x=\{f\in D:f(x)=0\}\), and \(\|bv\|\leq\|v(x)\|+\varepsilon\). Evaluation is contractive in the other direction. If \(v(x)=0\), the same construction makes \(bv\) arbitrarily small and proves \(v\in\overline{E'I_x}\). Thus the quotient has exactly the fibre norm. Its isometric image is closed and contains the total section values, so it is all of \(H_x\).

Apply *Kasparov's stabilization theorem*, Theorem 3.1, over the unital algebra \(D\). A unitary \(E'\oplus H_D\cong H_D\) carries \(E'\) onto \(pH_D\) for an adjointable projection \(p\). Evaluation gives \(H_x\cong p_x\ell^2\); the other summand gives \((1-p_x)\ell^2\cong\ell^2\). For every coordinate vector \(e_j\), \(pe_j\in H_D\) has continuous coefficient functions and uniformly convergent squared tails. Hence \(x\mapsto p_xe_j\) is norm continuous. The bound \(\|p_x\|\leq1\) extends this to every vector, proving strong continuity.

These fibre isometries preserve the full continuous-section structure. They carry the total \(s_n\) to continuous vector fields. At a point, approximate any given section value by a finite combination of the \(s_n\); continuity of the error norm makes that approximation valid on a neighborhood. Conversely, a continuous vector field in \(p_x\ell^2\) is locally approximable by finite combinations of those image sections by the same argument. The local approximation axiom in both fields proves continuity in both directions. ∎

**Lemma (Continuous orthonormal bases).** Let \(X\) be a paracompact Hausdorff space of finite covering dimension, and let \(r:X\to B(\ell^2)\) be a strongly continuous orthogonal projection whose range is infinite-dimensional at every point. There are continuous sections \(\xi_1,\xi_2,\ldots\) with \(\xi_k(x)\in r_x\ell^2\) such that, for every \(x\), the vectors \(\xi_1(x),\xi_2(x),\ldots\) form an orthonormal basis of \(r_x\ell^2\).

*Proof.* Fix a countable dense subset of \(\ell^2\) and a sequence \(g_1,g_2,\ldots\) in which each of its members occurs infinitely often. We choose the \(\xi_m\) one at a time. Suppose \(\xi_1,\ldots,\xi_{m-1}\) are continuous and orthonormal at every point, and put
\[
\pi_m(x)=r_x-\sum_{j<m}\xi_j(x)\xi_j(x)^*,
\]
the projection onto the orthogonal complement of \(\xi_1(x),\ldots,\xi_{m-1}(x)\) inside \(r_x\ell^2\). Each rank-one term is norm continuous, because \(\|\xi\xi^*-\zeta\zeta^*\|\le2\|\xi-\zeta\|\) for unit vectors, so \(\pi_m\) is strongly continuous; its range still has infinite dimension. The unit-section approximation above, applied to \(\pi_m\) and the section \(x\mapsto\pi_m(x)g_m\) with \(\varepsilon=1/m\), gives a continuous unit section \(\xi_m\) of \(\pi_m\) such that \(\pi_m(x)g_m\) lies within \(1/m\) of \(\mathbb C\xi_m(x)\). The new vector is orthogonal to the earlier ones. Since \(r_xg_m-\pi_m(x)g_m\) lies in the span of \(\xi_1(x),\ldots,\xi_{m-1}(x)\),
\[
\operatorname{dist}\bigl(r_xg_m,\operatorname{span}\{\xi_1(x),\ldots,\xi_m(x)\}\bigr)<1/m .
\]
The orthonormal family spans a dense subspace of \(r_x\ell^2\). Given \(v\in r_x\ell^2\) and \(\varepsilon>0\), choose a member \(h\) of the dense set with \(\|v-h\|<\varepsilon/2\), and an index \(m>2/\varepsilon\) with \(g_m=h\). Then \(\|v-r_xg_m\|=\|r_x(v-h)\|<\varepsilon/2\), and \(r_xg_m\) lies within \(1/m<\varepsilon/2\) of the span of the \(\xi_k(x)\). So the distance from \(v\) to that span is less than \(\varepsilon\). ∎

**Lemma (Lifting an infinite-rank projection).** If \(p:X\to B(\ell^2)\) is a strongly continuous projection of infinite rank and corank over a paracompact Hausdorff space of finite covering dimension, there is a strongly continuous unitary \(u_x\) with \(p_x=u_xp_0u_x^*\), for any fixed projection \(p_0\) of infinite rank and corank.

*Proof.* Apply the preceding lemma to \(p\) and to \(1-p\). This gives continuous sections \(\xi_k\) and \(\zeta_k\) whose values are orthonormal bases of \(p_x\ell^2\) and of \((1-p_x)\ell^2\). Fix orthonormal bases \((e_k)\) of \(p_0\ell^2\) and \((f_k)\) of \((1-p_0)\ell^2\), and let \(u_x\) send \(e_k\mapsto\xi_k(x)\) and \(f_k\mapsto\zeta_k(x)\). It carries an orthonormal basis of \(\ell^2\) onto one, so it is unitary, and \(u_xp_0u_x^*=p_x\). For each basis vector \(w\), the map \(x\mapsto u_xw\) is continuous, hence so is \(x\mapsto u_xw\) for every finite combination \(w\). For general \(w\), take a finite combination \(w'\) with \(\|w-w'\|<\delta\); then \(\|u_xw-u_yw\|\le2\delta+\|u_xw'-u_yw'\|\), which proves strong continuity. For the adjoint, \(\|u_x^*v-u_y^*v\|=\|u_x(u_x^*v-u_y^*v)\|=\|v-u_xu_y^*v\|\), and this tends to zero as \(x\to y\) by strong continuity at the fixed vector \(u_y^*v\). Hence \(u\) and \(u^*\) both preserve continuous vector sections. ∎

**Theorem 7.4 (Dixmier–Douady triviality).** A separable continuous field with every fibre of Hilbert dimension \(\aleph_0\), over a paracompact Hausdorff space of finite covering dimension, is unitarily isomorphic as a continuous field to the constant \(\ell^2\) field.

*Proof.* Paracompact patching gives normality. The countable-total-field lemma represents the field as \(p_x\ell^2\), with \(p\) strongly continuous and of infinite rank and corank. The projection-lifting lemma identifies this range field with the constant range of \(p_0\). The unitary and its inverse preserve norm-continuous vector sections, and the representation lemma identifies exactly the prescribed section structures. Since \(p_0\ell^2\cong\ell^2\), this is the required continuous-field unitary. ∎

For our locally compact \(X\), the unitary preserves fibre norms and hence vanishing at infinity, giving \(\Gamma_0(H)\cong C_0(X,\ell^2)\). In particular this applies to a countably generated field of infinite-dimensional fibres over a finite-dimensional compact Hausdorff space. Separability here is the countable-total-section condition; Example 7.2 explains why separable fibres alone do not suffice. Finite covering dimension is used in the finite-dimensional avoidance lemma, whereas stabilization itself needs no dimension bound.

### The continuous-trace gluing class

The Dixmier–Douady class is a different construction: it measures the scalar discrepancy in gluing local compact algebras. Its proof requires the imprimitivity and representation correspondence developed in the next lessons. After those prerequisites, [*The Rieffel correspondence and induced representations*, Section 8](the-rieffel-correspondence-and-induced-representations.md#8-continuous-trace-algebras-and-the-gluing-class) constructs the class, proves its independence and integer cohomological degree, and proves the fixed-spectrum Morita classification and zero-class compact-module criterion. Thus the ordinary module–field dictionary and the triviality theorem are established here before the Morita application.

## 8. Preview: fields on a leaf space

For a foliation, the quotient of a manifold by its leaves can fail to be Hausdorff, so the preceding theorem cannot simply be applied to that quotient as \(X\). Connes instead uses its holonomy groupoid: Hilbert spaces at points are linked by unitary maps along groupoid arrows, with compatible composition. Continuity is encoded by a chosen space of sections, using coefficients in the foliation C*-algebra and the half-density convention needed for convolution.

For a compact foliated manifold, the precise written provider is *Hilbert modules and fields on the leaf space*, Theorems 4.2, 4.7 and 4.8, in *Foliations and their operator algebras*. It uses the reduced holonomy algebra, a countably generated module, half-density sections, a countable coefficient-norm-dense and fibre-total family, and relative closure among concrete measurable sections. Its full admissible column ideal and kernel-recovery convention are Lemmas 3.2–3.3 and 4.5–4.5a. Completion is after quotienting zero coefficient seminorm; it does not give pointwise values to every completed module element. The cited theorems prove both inverse constructions, including the section structure. This is a written draft; its header leaves independent checking unclaimed. Connes, Section 7, Theorem 3, is the original source. Unitary groupoid identifications alone do not specify the continuous sections. Here the analogy is the concrete one already proved: a coefficient algebra and its inner product jointly encode which vectors vary continuously. The groupoid construction and its analytic index will be studied separately.

## 9. Exercises with solutions

**Exercise 9.1 (Basic: a zero boundary fibre).** Compute the fibres of \(I=C_0((0,1])\) as a Hilbert \(C([0,1])\)-module.

*Solution.* Identify \(I\) with continuous functions on \([0,1]\) zero at zero. For \(t>0\), evaluation is onto \(\mathbb C\), by a cutoff with value one at \(t\), and its null space is \(\{b:b(t)=0\}\). Proposition 2.1 gives \(I_t=\mathbb C\). At zero all functions have scalar norm zero, so \(I_0=0\). The continuous sections are precisely the functions continuous on \((0,1]\) whose values tend to zero at zero; their \(C_0\)-section module over the compact base is \(I\) itself. The jump obeys (5.3). ∎

**Exercise 9.2 (Intermediate: finite rank).** Prove that a field of constant finite rank is a vector bundle, and over a compact base has finite projective sections.

*Solution.* Lift a basis at a point to sections. The continuous Gram determinant remains positive on a neighborhood, and multiplying its column of sections by \(G^{-1/2}\) gives an orthonormal local frame. Inner products with the frame are continuous coordinates, and continuous coordinates reconstruct continuous sections; thus these are local trivializations with continuous unitary transitions. Over a compact base choose finitely many frames and a partition \(\rho_i\) subordinate to their domains. The global vectors \(\sqrt{\rho_i}u_j\), extended by zero, satisfy \(\sum_{i,j}\theta_{\zeta_{ij},\zeta_{ij}}=1\). Their analysis map identifies the section module with the range of its Gram projection in a finite free module. This gives the claimed finite projective module, with no infinite-dimensional triviality theorem involved. ∎

**Exercise 9.3 (Intermediate: the compact-field axioms).** Show that \(\mathcal K(E)\) is the algebra of the continuous field \(\mathcal K(E_x)\) in the sense of Blackadar IV.1.6.1.

*Solution.* Formula (4.1) gives pointwise values. Sums, products and adjoints of finite ranks remain finite ranks; their norms are continuous by the Gram formula (4.2) and vanish at infinity by the rank-one estimate. Norm limits preserve these properties. Evaluation is onto because every fibre vector is a section value, and the closed homomorphic image contains all fibre rank ones. Finally a section locally approximable by compact sections and vanishing at infinity can be patched on its compact norm-level sets using (1.2). Absorbing the scalar weights into the first rank-one vectors produces global module compacts approaching it uniformly. This proves local uniform closure and all the required axioms. Zero fibres give a nonfull continuous field in Blackadar's terminology. ∎

**Exercise 9.4 (Advanced: construct a jump).** Construct a continuous Hilbert field on \([0,1]\) with nonconstant fibre dimension, and describe its module.

*Solution.* Use \(E=C([0,1])\oplus I\) from (6.1). Its fibres have dimension one at zero and two elsewhere. A section is a pair \((a,b)\) with \(a\) continuous on \([0,1]\), \(b\) continuous on \((0,1]\), and \(b(t)\to0\) at zero. The module operations are pointwise, and
\(\langle(a,b),(c,d)\rangle=\overline a c+\overline b d\).
These functions are continuous at zero, and the supremum norm is complete, so this is precisely \(C([0,1])\oplus C_0((0,1])\). The local approximation description in Theorem 2.2 supplies the continuous-field axioms. Proposition 5.2 rules out the reversed pattern with two-dimensional fibre only at zero and one-dimensional fibres nearby. ∎

## What this lesson does not prove

The cutoff and finite-partition lemma in Section 5 of *Finite projective modules, frames and K₀* supplies the locally compact topology used here. Functional calculus is the exact foundation provider identified in the first Hilbert-module lesson. The module prerequisites supply Cauchy–Schwarz, tensor fibres, closedness of C*-homomorphic images, and the frame projection [*Finite projective modules, frames and K₀*, Theorem 1.2]. Stabilization and full amplification were proved in the stabilization lesson [Theorems 3.1 and 4.2].

Theorem 7.4 includes the countable-total-field reduction and complete projection-lifting argument. The preceding lemmas prove paracompact patching, finite-dimensional avoidance and the unit-section approximation, so neither Michael selection nor an external proof link is a required input. The continuous-trace gluing class and its classification are proved after their algebraic prerequisites in *The Rieffel correspondence and induced representations*, Section 8. The references retain credit for the classical theory. The groupoid-field correspondence has the exact written programme provider and full section conventions stated in Section 8; Connes remains the historical credit. No measurable direct-integral theory or elliptic groupoid calculus is used to prove the ordinary module–field dictionary.

## References

[Connes] Alain Connes, “A survey of foliations and operator algebras,” *Proceedings of Symposia in Pure Mathematics* 38, Part I (1982), 521–628, Section 7, “C* modules over C*(V,F) and continuous fields of Hilbert spaces on V/F,” especially Theorem 3. [Author's text](https://alainconnes.org/wp-content/uploads/foliationsfine.pdf).

[Blackadar 2006] Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006, [author's revised version](https://www.bruceblackadar.com/Mathematics/Cycr.pdf), IV.1.6 and IV.1.7.

[Blackadar 1998] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, Section 13.6. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

[Dixmier–Douady] Jacques Dixmier and Adrien Douady, “Champs continus d'espaces hilbertiens et de C*-algèbres,” *Bulletin de la Société Mathématique de France* 91 (1963), 227–284, Definition 6 and Section 15, Theorem 5. [Original article](https://numdam.org/articles/10.24033/bsmf.1596/).

[Prokhorova] Marina Prokhorova, [“From graph to Riesz continuity”](https://ems.press/content/serial-article-files/52400?nt=1), *Zeitschrift für Analysis und ihre Anwendungen* 45 (2026), 1–28, Theorem 6.1 and Lemma 6.2, pp.21–22. Another proof of the lifting step.
