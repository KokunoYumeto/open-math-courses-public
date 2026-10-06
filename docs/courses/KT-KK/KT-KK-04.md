# The index pairing between K-theory and K-homology

*Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A Fredholm module supplies an operator that almost intertwines the algebra action. A projection selects two subspaces on which that operator is Fredholm; a unitary supplies a Fredholm compression on the positive spectral subspace. Their finite-dimensional defects are the even and odd index pairings.

Our convention is
\[
\operatorname{index}T=\dim\ker T-\dim\ker T^*.
\tag{0.1}
\]
For an odd exact involution \(F\), the projection is \(P=(1+F)/2\). With these two choices the Hardy module pairs with the circle coordinate \(z\) to \(-1\). This agrees with the positive-compression convention in *The local index formula*.

We use the preceding lesson's normalization, group laws and bounded transform, the Hilbert-space Fredholm facts specified there, and the projection and unitary definitions of K-theory from the operator K-theory course. For the boundary map we use its published lesson *The index map and the exact sequence at \(K_0\)*, Definition 2.1 and Theorem 2.2. We compute its sign here from a doubled lift.

## 1. The even compression

Let \(A\) first be unital and let \(x=(H,\pi,F)\) be an even cycle. Matrix amplification means \(H^n=H\otimes\mathbb C^n\), with grading \(\Gamma\otimes1\), operator \(F^{(n)}=F\otimes1\), and matrix representation \(\pi^{(n)}([a_{ij}])=[\pi(a_{ij})]\). For a projection \(p\in M_n(A)\), put
\[
\begin{aligned}
P_\pm&=\pi_\pm^{(n)}(p),\\
T_p&=P_-F_+^{(n)}|_{P_+H_+^n}.
\end{aligned}
\tag{1.1}
\]
The domain and codomain in this formula are \(P_+H_+^n\) and \(P_-H_-^n\); they can have different dimensions.

### Lemma 1.1. The even compression is Fredholm

\(T_p\) is Fredholm, with inverse modulo compacts
\(S_p=P_+F_-^{(n)}|_{P_-H_-^n}\). Its index is unchanged by the preceding lesson's normalization.

**Proof.** Suppress the amplification notation. The off-diagonal blocks of \([F,\pi(p)]\) give
\[
\begin{aligned}
F_+P_+-P_-F_+&\in\mathcal K,\\
F_-P_--P_+F_-&\in\mathcal K.
\end{aligned}
\]
The two inverse errors have the exact typed expansions
\[
\begin{aligned}
S_pT_p-P_+
&=P_+F_-(P_-F_+-F_+P_+)P_+
  +P_+(F_-F_+-1)P_+,\\
T_pS_p-P_-
&=P_-F_+(P_+F_--F_-P_-)P_-
  +P_-(F_+F_--1)P_- .
\end{aligned}
\]
The first terms are compact by the preceding commutators; the second terms are the represented corners of the square defect in (1.1). The adjoint defect also gives \(T_p^*-S_p=P_+(F_+^*-F_-)P_-\in\mathcal K\). All these compact operators have the indicated represented ranges as their domain and target. The Fredholm criterion in the first extension lesson therefore applies even when the two ranges have different dimensions or the representation is degenerate.

Replacing \(F\) by its self-adjoint clipped contraction changes its product with \(\pi(p)\) by a compact. Thus the compressed block changes compactly. In the doubled exact normalization the representation is \(\pi\oplus0\), so the projection \(p\) selects only the first represented copy. Its compressed operator is exactly that clipped block; the off-diagonal square-root entries are killed by the zero representation. Index invariance under compact perturbation proves the last assertion. \(\square\)

Define \(\langle[p],x\rangle=\operatorname{index}T_p\), and extend to differences of projections by subtraction.

### Theorem 1.2. The even pairing for unital algebras

This defines a bilinear pairing
\[
K_0(A)\times K^0(A)\longrightarrow\mathbb Z.
\tag{1.2}
\]
It is invariant under projection equivalence and homotopy, operator homotopy, compact perturbations, and addition of degenerate cycles.

**Proof.** A block sum \(p\oplus q\) gives \(T_p\oplus T_q\), so the index is additive in projections and insensitive to zero padding. If \(v\) is a partial isometry implementing \(v^*v=p\), \(vv^*=q\), its two represented blocks give unitaries \(W_\pm:P_\pm H_\pm^n\to Q_\pm H_\pm^m\). Rectangular matrix entries of the cycle commutator give
\[
W_-T_p-T_qW_+\in\mathcal K.
\]
In detail that difference is \(Q_-(\pi_-^{(m,n)}(v)F_+^{(n)}-F_+^{(m)}\pi_+^{(m,n)}(v))P_+\), whose finitely many matrix entries are the cycle commutators. The two compressions therefore agree up to compact error after these unitary identifications, and have equal index. This proves independence under stable projection equivalence and hence extension to the Grothendieck group.

For a norm-continuous path of projections, their represented ranges are locally identified by the continuous close-projection unitaries proved in the preceding lesson, Lemma 7.1. Use those unitaries separately in the two graded spaces. The transported compressions are a norm-continuous Fredholm path, so the index is constant. An operator homotopy of \(F\) gives such a path on the fixed represented projection ranges directly. A locally compact change of \(F\) is compact on those ranges, and a compact perturbation is a special case.

Unitary equivalence of cycles conjugates the typed operator. A direct sum of cycles gives a direct sum of typed operators, so the index is additive in cycles. For a degenerate cycle, the two compressed blocks are actual inverse adjoints: the commutator, adjoint defect and square defect are all zero on the represented ranges. Thus \(T_p\) is unitary from one range to the other and its index is zero. Every generating K-homology relation preserves the index. Additivity in each variable proves bilinearity. \(\square\)

For a unital representation, testing \(p=1\) gives \(\operatorname{index}F_+\). A finite-dimensional scalar cycle with graded dimensions \(r,s\) therefore gives \(r-s\), as announced in the preceding lesson.

## 2. The odd compression

First take an odd cycle with \(F=F^*\), \(F^2=1\), and unital representation. Put \(P=(1+F)/2\). For \(u\in M_n(A)\) unitary define
\[
T_u=P^{(n)}\pi^{(n)}(u)|_{P^{(n)}H^n},
\qquad
\langle[u],x\rangle=\operatorname{index}T_u.
\tag{2.1}
\]

### Lemma 2.1. Fredholmness and the product rule

The operator \(T_u\) is essentially unitary, and
\[
T_{uv}-T_uT_v\in\mathcal K,\qquad
\operatorname{index}T_{uv}
=\operatorname{index}T_u+\operatorname{index}T_v.
\tag{2.2}
\]

**Proof.** Write \(U=\pi^{(n)}(u)\). Since \([P^{(n)},U]\) is compact, the differences
\[
T_u^*T_u-1_{PH^n}
=-P^{(n)}U^*(1-P^{(n)})U|_{PH^n}
\]
and \(T_uT_u^*-1_{PH^n}\) are compact. Thus \(T_{u^*}=T_u^*\) is an inverse modulo compacts. For another represented unitary \(V\),
\[
T_{uv}-T_uT_v
=P^{(n)}U(1-P^{(n)})V|_{PH^n}
\]
is compact. Compact invariance and Fredholm composition additivity give (2.2). \(\square\)

### Theorem 2.2. The odd pairing for unital algebras

Formula (2.1) extends to a bilinear pairing
\[
K_1(A)\times K^1(A)\longrightarrow\mathbb Z,
\tag{2.3}
\]
using the continuous exact normalization for a general cycle. It is invariant under all K-theory and K-homology relations.

**Proof.** For a possibly degenerate representation, replace the represented unitary by
\(U=\pi^{(n)}(u)+1-\pi^{(n)}(1)\). This is an actual unitary and acts as the identity on the representation's zero part. For a general \(F\), use the exact doubled normalization of the preceding lesson, Proposition 2.3, and this same unitary completion. Its Lemma 7.1, applied at each matrix size, proves invariance under operator homotopy, unitary equivalence, degeneracy and direct sum of cycles, and proves that removing the zero-representation part contributes zero index.

A unitary path \(u_t\) gives a norm-continuous Fredholm compression path on the fixed \(PH^n\). Its index is constant. Matrix padding by an identity adds an identity compression of index zero; block sums add the indices. These are the stable-unitary relations defining \(K_1(A)\). The product rule is consistent with that group law: the path
\[
\operatorname{diag}(u,1)R_t\operatorname{diag}(1,v)R_t^*,
\quad
R_t=\begin{pmatrix}\cos t&-\sin t\\
                         \sin t&\cos t\end{pmatrix},
\]
for \(0\leq t\leq\pi/2\), joins \(\operatorname{diag}(u,v)\) to \(\operatorname{diag}(uv,1)\). Thus addition may be computed by either block sum or product. Additivity in the cycle and unitary variables proves the theorem. Compact perturbations of \(F\) give operator homotopies by the preceding lesson, Proposition 2.2, so they preserve the pairing. \(\square\)

Replacing \(u\) by \(u^*\) negates the index. Replacing \(F\) by \(-F\) negates the cycle and hence the pairing. These are two different operations with the same sign effect.

## 3. Nonunital algebras and the scalar part

Write \(A^+=A\oplus\mathbb C\) for the forced unitization, adjoining a unit even when \(A\) already has one. Let \(\epsilon:A^+\to\mathbb C\) be its scalar quotient. The existing [Nonunital algebras: unitization, relative classes and half-exactness](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/nonunital-algebras-unitization-relative-classes-and-half-exactness.html), Section 1 and Theorem 1.1, gives
\[
K_0(A)=\ker\epsilon_*,
\tag{3.1}
\]
and represents a class there as \([p]-[q]\) for projections over \(A^+\) whose scalar ranks agree. The existing [Invertibles, unitaries and \(K_1\)](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/invertibles-unitaries-and-k1.html), Definition 1.1 and Proposition 1.2, gives stable unitary representatives over \(A^+\); their scalar part may be normalized to the identity.

A raw nonunital cycle need not extend to a cycle over \(A^+\), because its global square defect may fail to be compact. This is the reason for normalizing before extending.

### Theorem 3.1. Relative pairings

For every separable \(A\), the preceding pairings have natural extensions
\[
K_i(A)\times K^i(A)\longrightarrow\mathbb Z,\qquad i=0,1.
\tag{3.2}
\]
For an exact normalized cycle they are the unitization compression formulas, with subtraction for a relative projection class. Scalar projection and unitary classes contribute zero.

**Proof.** Given any cycle, perform the particular exact normalization \(N(F)\) of the preceding lesson on \(\widetilde H=H\oplus H\), using the opposite second grading in the even case and representation \(\rho=\pi\oplus0\). Define the unital representation
\[
\rho^+(a+\lambda1)=\rho(a)+\lambda1_{\widetilde H}.
\tag{3.3}
\]
The normalized operator is an exact self-adjoint involution and its commutators with \(\rho(A)\) are compact; scalar multiplication commutes with it. Thus it is a cycle over \(A^+\).

In the even case let \(E_x(p)\) be the even compression index for \(\rho^+(p)\), and define
\[
\langle[p]-[q],x\rangle=E_x(p)-E_x(q).
\tag{3.4}
\]
Theorem 1.2 shows that \(E_x\) is a homomorphism on \(K_0(A^+)\), so its restriction to (3.1) is independent of the particular equal-rank representatives. For a scalar projection \(p_0\in M_n(\mathbb C)\), its representation commutes exactly with \(N(F)\). The positive-to-negative block of this exact odd involution is a unitary, and restricts to a unitary on the two scalar-selected graded ranges. Hence \(E_x(p_0)=0\).

In the odd case define the index using \(\rho^{+,(n)}(u)\), for \(u\in M_n(A^+)\), and the positive projection of \(N(F)^{(n)}\). Theorem 2.2 proves independence of stable-unitary representatives. A scalar unitary acts only on the matrix factor, commutes exactly with that projection and has a unitary compression, so its index is zero. Multiplying \(u\) by \(\epsilon(u)^*\) therefore changes neither its K-theory class nor its index. The scalar matrix has a path to the identity, by finite-dimensional spectral diagonalization and exponentiation, justifying the normalized representative convention.

It remains to check dependence only on the original \(A\)-cycle class, since unitization of an arbitrary homotopy was not available before normalization. The construction \(F\mapsto N(F)\) is continuous. Thus an operator homotopy over \(A\) becomes one over \(A^+\): its square and adjoint defects are exactly zero, and its compact commutators are those over \(A\). Unitary equivalence and direct sum commute with the construction up to permutations. For a degenerate original cycle, the proof in the preceding lesson, Lemma 7.1, shows that its normalized operator commutes exactly with \(\rho(A)\), hence also with (3.3). The normalized cycle over \(A^+\) is then degenerate, so both its pairings vanish. This verifies every generating relation.

If an exact representative was already used, the further normalization adds a zero \(A\)-representation on which the operator is \(-F\). On extending to \(A^+\), this second summand has only scalar action and an exact involution; all its compression indices are zero by the preceding scalar checks. Thus (3.4) and the odd formula can be evaluated directly on any exact representative, and agree with the canonical construction. For projections already in \(A\), Lemma 1.1 recovers the original even compression. For a unital algebra and \(u\in M_n(A)\), its normalized forced-unitization representative is \(u+1-1_A\), whose representation is \(\rho(u)+1-\rho(1_A)\). This recovers precisely the earlier unital formulas. \(\square\)

For a \*-homomorphism \(\alpha:A\to B\), these pairings satisfy
\[
\langle\alpha_*k,x\rangle=\langle k,\alpha^*x\rangle.
\tag{3.5}
\]
Indeed \(\alpha\) extends unitally to the forced unitizations, and the amplified represented projections or unitaries on both sides are identical. The normalized operator depends on \(F\), which is also identical. This proves naturality by the compression formulas.

## 4. The extension boundary and its sign

Let an exact odd cycle give the compression Busby map
\(\tau:A\to\mathcal Q(PH)\). Its pullback extension is semisplit. After the infinite zero-representation padding described in the preceding lesson, we may assume that \(PH\) is infinite dimensional.

### Lemma 4.0. The rank identification for the compact ideal

For an infinite-dimensional Hilbert space \(L\), finite rank gives an isomorphism
\(K_0(\mathcal K(L))\cong\mathbb Z\), taking a rank-one projection to \(1\).
Matrix amplification preserves this identification. In particular the class
\([p_k]-[p_c]\) of finite-rank projections has value
\(\operatorname{rank}p_k-\operatorname{rank}p_c\).

**Proof.** A compact projection has finite-dimensional range: an infinite orthonormal family in its range would contradict compactness of its image of the unit ball. Two finite-rank projections of equal rank are Murray–von Neumann equivalent by any isometry between their ranges, extended by zero. The implementing operator is finite rank. Thus their classes equal the appropriate multiple of a fixed rank-one class.

We must also account for all relative projections and show that no extra relation kills that class. Represent \(M_n(\mathcal K(L)^+)\) on \(L^n\), and for a projection \(p\) denote its scalar projection by \(p_0\). The difference \(p-p_0\) is compact. The map
\[
A_p=pp_0:p_0L^n\longrightarrow pL^n
\]
is Fredholm: \(p_0p\) is an inverse modulo compact operators, since the errors are products with \(p-p_0\). Define \(r(p)=-\operatorname{index}A_p\).
This integer is additive under block sums. It is unchanged under stable projection equivalence: if \(v^*v=p,\ vv^*=q\), its scalar part \(v_0\) satisfies \(v_0^*v_0=p_0,\ v_0v_0^*=q_0\). Hence \(v\) and \(v_0\) are unitaries between the corresponding represented ranges, and
\[
vA_p-A_qv_0=q(v-v_0)p_0
\]
is compact. Unitary identifications and compact invariance of the index give \(r(p)=r(q)\). This also treats rectangular matrices after padding. Along a projection path, both \(p\) and \(p_0\) vary in norm; the close-projection unitaries from the preceding lesson transport both ranges locally to fixed spaces, so index invariance makes \(r\) constant. Consequently \(r\) descends to the projection Grothendieck group. It is zero on scalar projections and equals the rank on finite-rank projections, whose scalar part is zero.

Direct all finite-dimensional subspaces of \(L\) by inclusion and denote their projections by \(e_\alpha\). This net converges strongly to \(1_L\), since each vector belongs to one of those subspaces. Put \(E_\alpha=1_n\otimes e_\alpha\); these commute with \(p_0\). A finite-rank approximation followed by convergence on its finite-dimensional domain and range proves
\[
\|E_\alpha(p-p_0)E_\alpha-(p-p_0)\|\longrightarrow0.
\]
Thus the self-adjoint \(b_\alpha=p_0+E_\alpha(p-p_0)E_\alpha\) converges to \(p\). Eventually its spectrum is confined to disjoint neighborhoods of \(0,1\); this follows from the Neumann series for \(b_\alpha-\lambda\) whenever the distance from \(\lambda\) to \(\{0,1\}\) exceeds \(\|b_\alpha-p\|\). A continuous spectral cutoff gives a projection \(q_\alpha\) with \(\|q_\alpha-p\|\to0\). Continuity here follows by uniformly approximating that fixed cutoff by polynomials. The construction respects the blocks \(E_\alpha L^n\) and its complement; on the complement \(q_\alpha=p_0\).

Choose such an \(\alpha\) with \(\|q_\alpha-p\|<1\). These close projections are conjugate by the explicit unitary
\(X(X^*X)^{-1/2}\), where \(X=q_\alpha p+(1-q_\alpha)(1-p)\). It belongs to \(M_n(\mathcal K(L)^+)\): \(q_\alpha-p\) is compact, so \(X-1\) and, by quotient functional calculus, \((X^*X)^{-1/2}-1\) are compact. Write the finite-dimensional restriction of \(q_\alpha\) as \(q_f\). For orthogonal projections \(a,b\), the row \((a,b)\) has products \(a+b\) and \(\operatorname{diag}(a,b)\), so implements their stable equivalence and proves direct-sum addition. Applying this to the two blocks yields
\[
[p]-[p_0]=[q_\alpha]-[p_0]=[q_f]-[p_0E_\alpha].
\]
Both projections on the right are finite rank.

Every relative class in \(K_0(\mathcal K(L))\), defined as the kernel of the scalar quotient on the forced unitization, is \([p]-[q]\) with equal scalar ranks. The finite-dimensional scalar projections \(p_0,q_0\) are stably equivalent, so the preceding reduction writes this class as a difference of finite-rank projection classes. All classes are therefore integer multiples of the rank-one class. The integer \(r\) constructed above sends that class to \(1\), so there is no additional relation. This proves the isomorphism. All arguments on \(L^n\) use ordinary finite rank and give exactly the same integer after amplification. \(\square\)

### Theorem 4.1. The odd pairing is the index boundary

For this extension,
\[
\partial:K_1(A)\longrightarrow K_0(\mathcal K(PH))\cong\mathbb Z
\]
is exactly \(k\mapsto\langle k,x\rangle\), when the rank-one compact projection is the positive generator of \(K_0(\mathcal K)\).

**Proof.** Use a normalized unitary \(u\) over \(A^+\). Its compression \(T\) is a lift of the unitary \(\tau^{+,(n)}(u)\) in the Calkin algebra. By Lemma 2.1 it is essentially unitary and Fredholm. Its polar partial isometry \(V\) has
\[
V^*V=1-p_k,\qquad VV^*=1-p_c,
\tag{4.1}
\]
where \(p_k,p_c\) are the finite-rank projections onto its kernel and cokernel. For an explicit construction, Fredholm closed range gives a gap in the spectrum of \(|T|\) off zero. The continuous function \(h\) on that spectrum, with \(h(0)=0\) and \(h(t)=1/t\) for \(t>0\), gives \(V=Th(|T|)\) and the identities (4.1). Also \(T-V\) is compact. To check this, \(|T|^2-1\) is compact, so \(|T|-1\) is compact by continuous functional calculus in the Calkin quotient. The identity \(T=V|T|\) gives \(T-V=V(|T|-1)\).

There is an explicit doubled unitary lift:
\[
W=\begin{pmatrix}V&-p_c\\p_k&V^*\end{pmatrix}.
\tag{4.2}
\]
The relations \(Vp_k=0\), \(p_cV=0\), and their adjoints show by multiplication that \(WW^*=W^*W=1\). Its quotient has diagonal entries \(\tau^{+,(n)}(u)\) and its adjoint, and zero off-diagonal entries. With \(P_0=\operatorname{diag}(1,0)\),
\[
WP_0W^*=\operatorname{diag}(1-p_c,p_k).
\tag{4.3}
\]
The boundary definition in the operator K-theory prerequisite is the difference of this projection and \(P_0\), in the compact ideal's relative \(K_0\). It therefore gives
\[
\partial[u]=[p_k]-[p_c]
\quad\longmapsto\quad
\dim\ker T-\dim\ker T^*.
\tag{4.4}
\]
This is the pairing by definition.

The computation is compatible with the forced-unitization convention even though the Calkin extension is already unital. In the forced unitization of \(\mathcal B(PH^n)\), use the normalized doubled lift \(w=W+(1_{\mathrm{ext}}-1_{\mathcal B})1_2\) and the reference projection \(P_0^{\mathrm{ext}}=\operatorname{diag}(1_{\mathrm{ext}},0)\). The two orthogonal central summands \(1_{\mathcal B}\) and \(1_{\mathrm{ext}}-1_{\mathcal B}\) make their products split. Thus
\[
wP_0^{\mathrm{ext}}w^*-P_0^{\mathrm{ext}}
=WP_0W^*-P_0=\operatorname{diag}(-p_c,p_k).
\]
In the compact ideal's unitization the resulting projection is \(\operatorname{diag}(1-p_c,p_k)\), with reference \(\operatorname{diag}(1,0)\). Orthogonal-sum addition, proved in Lemma 4.0, makes its relative class exactly \([p_k]-[p_c]\). This verifies the scalar convention directly rather than identifying the two units silently.

Formally, this Calkin boundary is the boundary of the pullback extension by naturality: its projection to the multiplier algebra is the identity on the compact ideal and induces the Busby map on the quotient. [The index map and the exact sequence at \(K_0\)](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/the-index-map-and-the-exact-sequence-at-k0.html), Definition 2.1 and Theorem 2.2, proves that naturality and the doubled-lift formula, including choice of lift, normalized homotopy and block-sum addition. Lemma 4.0 proves the rank identification and its invariance under matrix amplification here. Scalar unitary parts give zero, by Theorem 3.1, so the argument proves the assertion for every class in \(K_1(A)\). \(\square\)

In particular, for the Toeplitz extension the lift is \(S\), so \(p_k=0\), \(p_c=p_0\), and \(\partial[z]=-[p_0]\). The boundary sign agrees with \(-1\) in our Fredholm convention; no change of orientation is hidden in the identification with \(\mathbb Z\).

## 5. Why a bundle test is a twisted Dirac index

An index pairing with a bundle is an analytic assertion before it is a characteristic-class formula. We prove the analytic comparison here.

### Lemma 5.1. A bounded perturbation changes the transform compactly

Suppose \(D_0,D_1\) are self-adjoint with the same domain and compact resolvents, and \(D_1-D_0=B\) is bounded. Their bounded transforms differ by a compact operator.

**Proof.** Use the resolvent integral (4.5) of the preceding lesson, with \(\alpha(s)=\sqrt{1+s^2}\). The resolvent identity gives
\[
(D_1\pm i\alpha)^{-1}-(D_0\pm i\alpha)^{-1}
=-(D_1\pm i\alpha)^{-1}B(D_0\pm i\alpha)^{-1}.
\]
Each difference is compact and has norm at most \(\|B\|/(1+s^2)\). The integral of the two differences therefore converges in norm to a compact. The individual truncated transform integrals converge strongly; their difference must have this compact norm limit. \(\square\)

### Lemma 5.1a. The domain under a bounded self-adjoint perturbation

If \(D\) is self-adjoint and \(B=B^*\) is bounded, then \(D+B\), with domain \(\operatorname{Dom}D\), is self-adjoint. Its graph norm is equivalent to that of \(D\). If \(D\) has compact resolvent, so does \(D+B\). Oddness for a grading is preserved when both \(D\) and \(B\) are odd.

**Proof.** A vector \(v\) is in the adjoint domain of \(D+B\) exactly when \(u\mapsto\langle (D+B)u,v\rangle\) is bounded on \(\operatorname{Dom}D\) in the ambient Hilbert norm. The \(B\)-term is already bounded, so this is exactly the adjoint-domain condition for \(D\). Self-adjointness of \(D,B\) proves the assertion and the equality of actions. The two triangle inequalities
\(\|(D+B)u\|\leq\|Du\|+\|B\|\|u\|\) and
\(\|Du\|\leq\|(D+B)u\|+\|B\|\|u\|\)
give graph-norm equivalence. For \(t>\|B\|\),
\[
D+B-it=(1+B(D-it)^{-1})(D-it).
\]
The first factor is invertible by its norm-convergent Neumann series, since \(\|(D-it)^{-1}\|\leq1/t\). Hence \((D+B-it)^{-1}\) is compact. The resolvent identity expresses the resolvent at any other nonreal point as this compact operator plus its product with bounded resolvents, so all such resolvents are compact. Their product gives compact \((1+(D+B)^2)^{-1}\). The grading assertions are identities on the common domain. \(\square\)

### Theorem 5.2. The twisted Dirac comparison

Let \(D\) be the graded spin\(^{c}\) Dirac operator on a closed even-dimensional manifold \(M\), and let \(E\) be a smooth Hermitian vector bundle with a Hermitian connection. With \(x=[D]\) the bounded-transform class,
\[
\langle[E],x\rangle=\operatorname{index}D_E^+.
\tag{5.1}
\]
The operator on the right has domain \(H^1(M,S^+\otimes E)\) and target \(L^2(M,S^-\otimes E)\). No topological index formula is assumed.

**Proof.** The spinor Dirac operator has the local expression \(D=\sum_j c(e_j)\nabla^S_{e_j}\), where \(c(e_j)^*=-c(e_j)\), \(c(\xi)^2=-|\xi|^2\), and the spinor connection is Hermitian and compatible with Clifford multiplication. Its principal symbol is \(ic(\xi)\), whose square is \(|\xi|^2\), proving ellipticity. Integration by parts on the closed manifold makes its formal adjoint equal to itself: the connection differentiates \(c(e_j)\) as \(c(\nabla_{e_j}e_j)\), and the zero-order correction is
\(c(\sum_j\nabla_{e_j}e_j+\sum_j\operatorname{div}(e_j)e_j)=0\),
since metric compatibility gives \(\sum_j\operatorname{div}(e_j)e_j=-\sum_j\nabla_{e_j}e_j\). There is no boundary term. Clifford multiplication is odd and the connection preserves the grading. The preceding lesson, Corollary 4.2, with the complete finite-chart and Friedrichs-mollifier proofs of Lemmas 4.1a–4.1c, therefore gives the self-adjoint \(H^1\) realization with compact resolvent used below.

Embed \(E\) smoothly and isometrically in a trivial finite-rank bundle. One direct construction chooses finitely many local orthonormal frames and smooth real cutoffs \(\chi_j\) supported in their charts, with \(\sum_j\chi_j^2=1\). Send a vector to the direct sum of its frame coordinates multiplied by the \(\chi_j\), extending each product by zero. This is a smooth isometry, so its image has smooth orthogonal projection \(p\in M_N(C^\infty(M))\).

On \(L^2(M,S)\otimes\mathbb C^N\), with the amplified \(D\), multiplication by \(p\) is even and preserves \(H^1\). Its commutator with \(D\) is bounded by the first-order formula in the preceding lesson. Put
\[
D^\mathrm{diag}=pDp+(1-p)D(1-p).
\]
This has the same domain as \(D\) and differs by the bounded off-diagonal part
\(pD(1-p)+(1-p)Dp\). The latter is bounded because \(pD(1-p)=-p[D,p]\), and the other term is its adjoint. The off-diagonal part is self-adjoint because its two blocks are adjoints, and it is odd because \(p\) is even. Lemma 5.1a therefore gives self-adjointness of \(D^{\mathrm{diag}}\) on the same \(H^1\) domain and its compact resolvent, without requiring a second elliptic-domain assertion.

Lemma 5.1 shows that its bounded transform differs compactly from that of \(D\). Since \(p\) preserves the domain and commutes with the diagonal operator there, it commutes with each resolvent: apply \((D^{\mathrm{diag}}\pm i)^{-1}\) to the domain identity. The restrictions to \(pH\) and its complement therefore have surjective nonreal resolvents and are self-adjoint, with compact resolvent. The resolvent integral of the preceding lesson, Theorem 4.1, restricts on \(pH\) to the same integral for \(D_p=pDp\), so the restricted transform is precisely its bounded transform on \(S\otimes E\). Hence the even compression defining \(\langle[p],[D]\rangle\) has the same index as \(F_{D_p}^+\).

The operator \(D_p\) is the Dirac operator for the projected connection on \(E\). Replacing that connection by the given Hermitian connection changes the Dirac operator by a smooth bundle endomorphism, hence a bounded self-adjoint odd operator. Explicitly the connection difference is an endomorphism-valued one-form \(B_j\), with \(B_j^*=-B_j\) because both connections preserve the Hermitian metric. The operator difference is \(\sum_j c(e_j)\otimes B_j\). Its factors act on different bundle factors and commute, so the product of these two skew-adjoint factors is self-adjoint. Its smooth coefficients are bounded on \(M\), and its Clifford factor makes it odd. Lemma 5.1a proves that their domains remain the same \(H^1\) and that the compact resolvent is retained. Lemma 5.1 makes their transforms compactly different, preserving the compressed index.

Finally \(R_+=(1+D_E^2|_{H_+})^{-1/2}\) is an isomorphism from \(L^2(S^+\otimes E)\) onto the domain of \(D_E^+\), with its graph norm. The spectral-domain formula proves this exactly: the graph norm squared is the weighted eigenvector sum of \(1+\lambda_j^2\) in the preceding lesson, Lemma 4.0, and multiplication by \((1+\lambda^2)^{-1/2}\) gives an isometry onto that domain, with inverse the reciprocal multiplier. The estimate in the preceding lesson, Lemma 4.1b, identifies its graph norm with \(H^1\). The equality \(F_{D_E}^+=D_E^+R_+\) therefore identifies kernels and ranges with those of the Sobolev realization of \(D_E^+\). Their indices agree. This proves (5.1). \(\square\)

The same argument shows independence from the connection. The full topological expression for this index, with its orientation hypotheses and symbol class, remains a proof obligation in *Dirac classes, Poincaré duality and the index theorem in KK*. It is not a premise of the analytic comparison proved here.

## 6. Circle and noncommutative-torus calculations

For the Hardy module \(h\) on the circle, multiplication by \(z^k\) compresses to \(S^k\) for \(k\geq0\), or \((S^*)^{-k}\) for \(k<0\). The former has zero kernel and cokernel dimension \(k\); the latter has kernel dimension \(-k\) and zero cokernel. Thus
\[
\langle[z^k],h\rangle=-k.
\tag{6.1}
\]
For the matrix unitary \(\operatorname{diag}(z^2,z^{-5},1)\), direct-sum additivity gives
\[
-2+5+0=3.
\tag{6.2}
\]
More generally the published prerequisite *Toeplitz operators and the index theorem on the circle*, Theorem 3.1, computes the matrix Toeplitz index as minus the winding of its determinant. Formula (6.1) already fixes the sign without using that more general calculation.

There is also an explicit Dirac-type cycle for a noncommutative torus. Let \(A_\theta\) be the universal C\*-algebra generated by unitaries \(U,V\) with \(UV=e^{2\pi i\theta}VU\). On \(\ell^2(\mathbb Z^2)\), with basis \(e_{m,n}\), represent them by
\[
Ue_{m,n}=e_{m+1,n},\qquad
Ve_{m,n}=e^{-2\pi i\theta m}e_{m,n+1}.
\tag{6.3}
\]
These are unitaries and satisfy the relation: on a basis vector the two orders have phases differing by \(e^{2\pi i\theta}\). The universal property therefore gives a representation. Its faithfulness is not needed for the cycle.

On \(H=\ell^2(\mathbb Z^2)\otimes\mathbb C^2\), graded by \(\sigma_3\), let
\[
D(e_{m,n}\otimes v)
=e_{m,n}\otimes(m\sigma_1+n\sigma_2)v,
\tag{6.4}
\]
with the square-summable graph domain from the preceding torus example. That example's Fourier argument gives self-adjointness and compact resolvent. Direct calculation gives
\[
[D,U]=\sigma_1U,\qquad [D,V]=\sigma_2V.
\tag{6.5}
\]
The shift bound \(1+(m\pm1)^2+n^2\leq3(1+m^2+n^2)\), and its counterpart for shifting \(n\), prove domain preservation for \(U,U^*,V,V^*\); the phase in \(V\) has modulus one and changes no graph norm. The adjoint commutators are \([D,U^*]=-\sigma_1U^*\) and \([D,V^*]=-\sigma_2V^*\). The product rule now proves domain preservation and bounded commutators for every finite Laurent polynomial. It is norm dense in \(A_\theta\) by its defining generation. The bounded transform is therefore an even Fredholm module by the preceding lesson, Theorem 4.1, for every real \(\theta\).

Testing the identity projection gives zero, since the two constant-mode kernels each have dimension one, exactly as on the ordinary flat torus. A smooth nontrivial projection \(p\) is tested by the typed compression (1.1); this construction makes its index well defined without presupposing a trace or a cyclic formula for that integer.

## 7. Comparison with the Fredholm character

The analytic pairing is defined for every cycle in this lesson. Additional summability hypotheses allow it to be computed by trace expressions. The published lesson [The local index formula](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-LOCAL-INDEX/the-local-index-formula.html) proves the precise comparison: Theorem 9.2 identifies its residue cocycle with the bounded Fredholm character under that lesson's explicitly stated hypotheses of Theorem 8.4; Theorems 10.2 and 10.3 compute its odd and even K-theory evaluations as the compression indices used here. For an odd kernel the paragraph after Theorem 9.2 replaces \(D\) by \(D+P_0\) and proves invariance of positive-degree residues; Theorem 10.2 explicitly uses that phase. The even kernel comparison is Theorem 9.4, with the harmonic degree-zero completion of Corollary 7.3, and the full even index is Theorem 10.4. These additional hypotheses and completions are required for the character assertion.

In particular its odd formula (10.3) has the leading minus sign that converts its alternating cyclic evaluation into \(\operatorname{index}(PUP)\). Its even formula (10.6) counts the positive-to-negative block. Thus our circle value \(-1\) and even index convention agree with that course. We use those exact internal character theorems for this comparison; compactness alone does not justify a trace of an arbitrary product of commutators.

The further identity of these pairings with Kasparov products remains a proof obligation for *Homotopy, associativity, the index pairing and KK-equivalence*. Its required statement is that, under \(K_i(A)=KK^i(\mathbb C,A)\) and \(K^i(A)=KK^i(A,\mathbb C)\), their product in \(KK^0(\mathbb C,\mathbb C)=\mathbb Z\) is the compression index above, with these signs. The present Fredholm and boundary proofs do not require that product construction.

## 8. Exercises

**Exercise 8.1 (basic).** Compute \(\langle[z^k],h\rangle\) for every integer \(k\), including zero. Compute the pairing of \(\operatorname{diag}(z^2,z^{-5},1)\).

**Exercise 8.2 (intermediate).** Prove that a compact perturbation of the odd cycle operator preserves the pairing. Explain why one cannot simply call \((1+F_t)/2\) a projection along an arbitrary perturbation segment.

**Exercise 8.3 (intermediate).** Prove \(\langle[uv],x\rangle=\langle[u],x\rangle+\langle[v],x\rangle\) for unitaries of a common matrix size. Include the stable-unitary group law.

**Exercise 8.4 (advanced).** Use an essentially unitary Fredholm lift \(T\) to prove that the odd pairing equals the extension boundary. Keep track of both defect projections and evaluate the result for the unilateral shift.

## 9. Solutions

**Solution 8.1.** For \(k>0\), \(S^k\) has cokernel spanned by \(e_0,\ldots,e_{k-1}\) and zero kernel, giving \(-k\). For \(k=-\ell<0\), \((S^*)^\ell\) is surjective with kernel spanned by \(e_0,\ldots,e_{\ell-1}\), giving \(\ell=-k\). For \(k=0\) the compression is the identity, giving zero. The three diagonal entries contribute \(-2,+5,0\), so the matrix pairing is \(3\).

**Solution 8.2.** Let \(F'=F+K\) with \(K\) compact and both endpoints cycles. The segment \(F_t=F+tK\) is a cycle homotopy by the explicit defect expansion in the preceding lesson, Solution 8.2. Its exact normalizations \(N(F_t)\) form a norm-continuous path of self-adjoint involutions. Their positive projections \(P_t\) therefore form a norm-continuous projection path. The close-projection unitaries in that lesson's Lemma 7.1 transport their ranges locally to a fixed space, giving norm-continuous Fredholm compressions, with constant index. This proves the claim. Without normalization the defect
\[
\left(\frac{1+F_t}{2}\right)^2-\frac{1+F_t}{2}
=\frac{F_t^2-1}{4}
\]
need not be zero. Compactness, or local compactness, of this defect does not make the operator an actual projection.

**Solution 8.3.** For exact normalization let \(U,V\) be the represented unitary completions. Compactness of \([P,V]\) gives
\[
PUVP-(PUP)(PVP)=PU(1-P)VP\in\mathcal K(PH).
\]
The compressions \(PUP\), \(PVP\) are Fredholm. Compact invariance and composition additivity make the index of the left product equal the sum of their indices. The rotation path in Theorem 2.2 identifies the stable block sum of \(u,v\) with \(uv\) plus an identity block, so this index sum is the addition in \(K_1(A)\), not a different operation on representatives. The unitization formulas of Theorem 3.1 give the same proof for a nonunital algebra.

**Solution 8.4.** Fredholm closed range gives a spectral gap for \(|T|\) off its finite-dimensional kernel. Define \(h(0)=0\), \(h(t)=1/t\) on the nonzero spectrum, and \(V=Th(|T|)\). This is the polar partial isometry, with \(V^*V=1-p_k\), \(VV^*=1-p_c\). Essential unitarity gives \(|T|-1\) compact and \(T-V=V(|T|-1)\) compact. Thus \(V\) lifts the same quotient unitary. The matrix \(W\) in (4.2) is unitary: its diagonal products are \(VV^*+p_c=1\), \(p_k+V^*V=1\), and its off-diagonal products vanish because \(Vp_k=p_cV=0\). It is a doubled lift, and (4.3) gives boundary \([p_k]-[p_c]\). The rank identification gives the Fredholm index. For \(T=S\), the kernel projection is zero and the cokernel projection is \(p_0\), so the boundary is \(-[p_0]\) and the integer pairing is \(-1\).

## Internal proof dependencies and source credit

The preceding lesson, Lemma 2.1 and Propositions 2.2–2.3, proves the locally compact ideal and continuous normalization; its Lemma 7.1 proves range transport by explicit close-projection unitaries. Lemma 1.1 here gives all typed even inverse and adjoint errors, Lemma 2.1 gives the odd errors and product rule, Lemma 4.0 proves the full relative compact-rank identification, and Lemmas 5.1–5.1a give the compact transform comparison and domain preservation used for twisting. The operator K-theory lessons *Nonunital algebras: unitization, relative classes and half-exactness* and *Invertibles, unitaries and \(K_1\)* supply the exact relative and stable-unitary definitions; *The index map and the exact sequence at \(K_0\)*, Definition 2.1 and Theorem 2.2, supplies the doubled-lift boundary and its naturality. *Toeplitz operators and the index theorem on the circle*, Theorem 3.1, supplies the general matrix-symbol calculation. The Hilbert-space Fredholm prerequisites are those identified in the preceding lesson. Its local Lemmas 4.1a–4.1c and Corollary 4.2 prove the entire closed-manifold Sobolev, elliptic-estimate and adjoint-domain foundation used by Theorem 5.2 here.

The character comparison uses the exact published results and their additional hypotheses identified in Section 7. The Kasparov-product interpretation and topological Dirac index formula remain proof obligations in the course lessons named there and in Section 5. The pairings, their invariance, the relative scalar check, the extension boundary sign, the analytic twisting bridge, and all examples and exercises above are proved here.

## References

- B. Blackadar, *K-Theory for Operator Algebras*, freely accessible author-corrected second-edition PDF. Sections 16.3.2, 17.5 and 18.10 develop the Fredholm, boundary and index-pairing pictures. [Free author version](https://www.bruceblackadar.com/Mathematics/book6.pdf). The typed compression, relative scalar check, doubled boundary lift, compact-rank identification and analytic twisting argument required here are proved in this lesson.

- J. Rosenberg, *Examples and Applications of Noncommutative Geometry and K-Theory*, author notes dated 2010, Sections 1.2 and 4.2. [Free author notes](https://math.umd.edu/~jmr/BuenosAires/NCGexamples.pdf). These sections supply the source comparison for Fredholm cycles and smooth noncommutative tori; the exact representation, graph domain and commutators of Section 6 are verified here.

These free source PDFs retain their authors' copyrights. The CC0 notice applies to this lesson's original text.
