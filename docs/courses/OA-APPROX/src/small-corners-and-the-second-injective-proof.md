# Small corners and the second injective proof

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

A small corner can carry a good matrix model without occupying most of the algebra. We first choose one such corner which also almost commutes with the prescribed operators. A maximality argument then fills the complement with further good corners. Orthogonality makes the squared errors add, giving approximation on the whole identity.

We use [finite-rank models](invariant-states-and-finite-rank-projections.md) and repaired internal matrix systems, together with the normal trace-preserving expectation: it is the \(L^2\) orthogonal projection and is contractive in operator norm. Its exact prerequisite is [Modular-invariant subalgebras and conditional expectations](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#modular-expectations), ME-01, ME-04 and ME-08, specialized to a faithful finite trace.

Sections 1–2 concern a separable injective \(\mathrm{II}_1\) factor \(M\), with normalized trace \(\tau\). Section 3 proves a local-to-global implication for every finite algebra with a faithful normal tracial state. The final sequential conclusion retains separable predual. The scalar pinching input uses only the earlier finite expected-subfactor and contained-AFD constructions, so the second proof has its own route to the finite injective conclusion.

## 1. Selecting one almost invariant matrix corner

Fix a finite \(F\subset\mathcal U(M)\) containing \(1\), and first choose a finite-rank model
\[
q=\sum_{i=1}^m K_{x_i,x_i},\qquad
\sum_{v\in F}\|v q v^*-q\|_{\mathrm{HS}}^2<a^2m,
\tag{1}
\]
with \(x_i\in M\) orthonormal in \(L^2\). The number \(a>0\) is the first approximation parameter. This choice fixes \(m\) and \(B\ge\max(1,\|x_i\|)\). Only after that choice do we make the Gram and pinching parameter \(b\) small.

Use the preceding lesson's Corollary 3.1, and abbreviate its moduli by \(D=D_m(b)\), \(d=d_m(b)\). It gives orthogonal initial projections \(e_k\), repaired vectors \(w_i(k)\), matrix units \(E_{ij}(k)\) and their supports \(s_k\). Write \(p=\sum_k e_k\). By making \(b\) small with \(m,B\) fixed, arrange
\[
\tau(1-p)<\frac1{2B^2}.
\tag{2}
\]
Then each \(\|x_i p\|_2^2\ge1-B^2\tau(1-p)>1/2\).

**Lemma 1.1.** For some \(k\), putting \(s=s_k\) and
\[
C_v=\sum_{i,j}\tau(x_i^*v x_j)E_{ij}(k),
\]
we have, for every \(v\in F\),
\[
\begin{aligned}
\|s v s-C_v\|_2&\le\sqrt m\,d\sqrt{\tau(s)},\\
\|v s v^*-s\|_2&\le
\sqrt{\eta^2+2\sqrt m\,d}\sqrt{\tau(s)},\\
\eta&=2D+\sqrt2\,a(1+D).
\end{aligned}
\tag{3}
\]

**Proof.** Let \(Q_k=\sum_i K_{x_i e_k,x_i}=R_{e_k}q\), where \(R_{e_k}\) means right multiplication on the output vector. The operator \(R_{e_k}\) is an orthogonal projection on \(H\), commuting with every \(L_v\). For each \(v\), the operators \(R_{e_k}(v q v^*-q)\) are orthogonal in Hilbert–Schmidt space. Thus
\[
\sum_{k,v}\|v Q_kv^*-Q_k\|_{\mathrm{HS}}^2<a^2m.
\tag{4}
\]
Orthonormality of the second vectors in \(Q_k\) gives
\[
\sum_k\|Q_k\|_{\mathrm{HS}}^2
=\sum_i\|x_i p\|_2^2>m/2.
\tag{5}
\]
Consequently there is \(k\) with summed error less than \(2a^2\|Q_k\|_{\mathrm{HS}}^2\). This \(Q_k\) is nonzero.

Put \(V=\sum_i K_{w_i(k),x_i}\). The same orthonormality and the repaired vector errors give
\[
\|V-Q_k\|_{\mathrm{HS}}\le D\|V\|_{\mathrm{HS}},\qquad
\|V\|_{\mathrm{HS}}^2=m\tau(e_k)=\tau(s).
\tag{6}
\]
The triangle inequality, applied to each test and to its conjugate, therefore gives
\[
\|v Vv^*-V\|_{\mathrm{HS}}\le\eta\sqrt{\tau(s)}.
\tag{7}
\]
The first inequality in (3) is the matrix coefficient estimate already proved. To obtain the second, expand the rank-one Hilbert–Schmidt pairing:
\[
\|v Vv^*-V\|_{\mathrm{HS}}^2
=2\tau(s)-2\operatorname{Re}\tau(C_v^*v).
\tag{8}
\]
Indeed its cross term is
\(\sum_{i,j}\tau(w_i^*v w_j)\overline{\tau(x_i^*v x_j)}\), equal to \(\tau(C_v^*v)\). Both \(C_v\) and \(s v s\) are supported by \(s\). Hence
\[
\begin{aligned}
|\tau((C_v-s v s)^*v)|
&\le\|C_v-s v s\|_2\|s v s\|_2\\
&\le\sqrt m\,d\,\tau(s).
\end{aligned}
\tag{9}
\]
Also
\[
2\tau(s)-2\tau(s v^*s v)=\|v s v^*-s\|_2^2.
\tag{10}
\]
Combining (7)–(10) proves the second bound in (3). \(\square\)

Let \(A_k=\operatorname{span}\{E_{ij}(k)\}\), a matrix algebra with identity \(s\). The \(L^2\) nearest-point property of its trace expectation gives
\[
\|s v s-E_{A_k}(s v s)\|_2\le\sqrt m\,d\sqrt{\tau(s)}.
\tag{11}
\]
Given any desired small tolerance \(c>0\), first choose \(a\) so \(\sqrt2\,a<c/2\). Then fix the model (1), and decrease \(b\) until (2) holds and both \(\sqrt m\,d<c\) and \(\sqrt{\eta^2+2\sqrt m\,d}<c\). This is possible because \(m,B\) are now fixed and \(D,d\to0\). Allowing the dimension of the first model to vary while taking the second limit would not justify these inequalities.

## 2. The small-corner condition

**Definition 2.1.** A faithfully tracial finite algebra has the small-corner approximation property if, for every nonzero projection \(e\), finite \(F\subset eMe\), and \(\varepsilon>0\), there are a nonzero projection \(f\le e\) and a finite-dimensional algebra \(A\subset fMf\), with identity \(f\), such that
\[
\|xf-fx\|_2\le\varepsilon\sqrt{\tau(f)},\qquad
\|fxf-E_A(fxf)\|_2\le\varepsilon\sqrt{\tau(f)}
\quad(x\in F).
\tag{12}
\]
This is the local finite-dimensional condition used in the references below. It is stronger than merely finding good matrix coefficients in some corner: the corner must also almost commute with the tests, and the condition is required inside every nonzero corner.

**Proposition 2.2.** Every injective \(\mathrm{II}_1\) factor with separable predual has this property.

**Proof.** For finite unitary tests in \(M\), Lemma 1.1, (11) and the two-parameter choice give (12), since \(\|v s-sv\|_2=\|v s v^*-s\|_2\).

Every bounded element is a scalar linear combination of at most four unitaries. For a self-adjoint contraction \(h\), write \(h=(u+u^*)/2\) with \(u=h+i(1-h^2)^{1/2}\); apply this to the real and imaginary parts and rescale. For a finite operator list, take the union of these unitary lists. Divide the unitary tolerance by the largest sum of absolute coefficients, using \(1\) if that sum is zero. Linearity, the triangle inequality and linearity of \(E_A\) give (12) for the operator list.

Finally every nonzero \(eMe\) is an injective \(\mathrm{II}_1\) factor with separable predual, by corner compression of a retraction and finite factor comparison. Repeat the argument with its normalized trace \(\tau_e=\tau/\tau(e)\). Both sides of (12) acquire the same factor \(\sqrt{\tau(e)}\) when converted to the ambient trace. \(\square\)

## 3. Filling the identity by maximality

**Theorem 3.1.** A finite von Neumann algebra with faithful normal tracial state and the small-corner property is locally AFD. This implication requires neither factoriality nor separable predual.

**Proof.** Fix a finite contraction list \(F\subset M\) and \(\varepsilon>0\). Consider all locally AFD von Neumann subalgebras \(A\subset M\), permitting identity \(f\ne1\) and the zero algebra, which satisfy
\[
\|x-(1-f)x(1-f)-E_A(fxf)\|_2
\le\varepsilon\sqrt{\tau(f)}
\qquad(x\in F).
\tag{13}
\]
Here \(E_A(fxf)\) is the normal trace expectation in \(fMf\), extended to \(M\) by compression. Order these algebras by inclusion.

We verify the chain condition. For an increasing chain \(A_i\), let \(f_i\) be its supports and \(f=\sup_i f_i\). Take \(A\) to be the nonunital strong operator closure of \(\bigcup_i A_i\) in \(M\). If \(f=0\), this is the zero algebra and already an upper bound. If \(f\ne0\), the union acts nondegenerately on \(fH\), since \(f_i\to f\) strongly. Its bicommutant on \(fH\), extended by zero on \((1-f)H\), is precisely \(A\), with identity \(f\). In particular we do not take the ambient bicommutant on all of \(H\), which would adjoin the complementary scalar identity.

This \(A\) is locally AFD: Kaplansky approximation for the nondegenerate algebra on \(fH\) gives bounded \(L^2\) approximants from the union to any finite list in \(A\); approximate that finite list further inside one chain member. Add the scalar algebra \(\mathbb C(f-f_i)\) to make the resulting finite algebra unital in \(A\).

The closed spaces \(L^2(A_i)\) increase to \(L^2(A)\), so their orthogonal projections converge strongly. These projections are precisely \(x\mapsto E_{A_i}(f_i x f_i)\). Also \((1-f_i)x(1-f_i)\to(1-f)x(1-f)\) in \(L^2\), by bounded strong convergence and the finite trace. Therefore (13) passes to \(A\). Every chain has an upper bound in the set, and Zorn's lemma supplies a maximal \(A\).

Suppose \(f\ne1\), and put \(e=1-f\). Apply (12) in \(eMe\) to \(eFe\), with tolerance \(\varepsilon/2\). Obtain \(g\ne0\), \(g\le e\), and a finite-dimensional \(B\subset gMg\). For \(y=exe\), set
\[
R=x-e x e-E_A(fxf),\qquad
S=y-(e-g)y(e-g)-E_B(gyg).
\tag{14}
\]
Every block of \(R\) has at least one \(f\) coordinate, whereas \(S\in eMe\); they are orthogonal in \(L^2\). The three blocks of \(S\) are
\[
(e-g)yg,\quad gy(e-g),\quad gyg-E_B(gyg).
\]
They are mutually orthogonal. The first two squared norms sum to \(\|yg-gy\|_2^2\). Condition (12) therefore gives
\[
\|S\|_2^2\le\frac{\varepsilon^2}{2}\tau(g).
\tag{15}
\]
For \(L=A\oplus B\), identity \(h=f+g\), its residual in (13) is \(R+S\), so
\[
\|R+S\|_2^2\le\varepsilon^2\tau(f)
+\frac{\varepsilon^2}{2}\tau(g)
\le\varepsilon^2\tau(h).
\tag{16}
\]
The direct sum is locally AFD and strictly contains \(A\), contradicting maximality. Thus \(f=1\), and (13) gives \(\|x-E_A(x)\|_2\le\varepsilon\) for all \(x\in F\).

Approximate the finitely many \(E_A(x)\)'s by a finite-dimensional unital algebra of \(A\). Choosing both this new error and the original \(\varepsilon\) arbitrarily small proves local AFD of \(M\). The expectation onto the final finite algebra supplies approximants of norm at most one. \(\square\)

For a separable \(\mathrm{II}_1\) factor, local AFD also implies the small-corner property. The [finite amplification and corner permanence proof](hyperfinite-finite-factors.md#corollary-5-2) is valid without separability. Inside a nonzero corner approximate the finite tests by a unital finite-dimensional algebra and take \(f=e\); its commutator error is zero. Thus the source's LAFD and AFD conditions are equivalent at their stated hypotheses.

## 4. The second finite-injective conclusion

**Theorem 4.1.** Every injective \(\mathrm{II}_1\) factor with separable predual is generated by an increasing sequence of finite-dimensional unital algebras, and is isomorphic to the tracial matrix product \(R\).

**Proof.** Proposition 2.2 gives small corners in every nonzero corner. Theorem 3.1 makes \(M\) locally AFD. The earlier [exact containment and dyadic construction](hyperfinite-finite-factors.md#theorem-5-1) then supplies an increasing generating dyadic sequence and its trace-GNS identification with \(R\). \(\square\)

The first proof reaches internal matrix approximation through balanced Kraus families and unitary couplings. This proof reaches it through external finite-rank projections, scalar pinching, partial-isometry repair and maximality. Haagerup's matrix-factorization method and Popa's small-corner method give two approaches to Connes' injectivity and AFD theorem. The general nonfactor finite converse is proved in [Central disintegration and measurable matrix assembly](central-disintegration-and-measurable-matrix-assembly.md) and [Injective algebras and separable tracial envelopes](injective-algebras-and-separable-tracial-envelopes.md). Its central argument retains the distinction from the factor proof above.

## 5. Exercises with complete solutions

**Exercise 1.** Why is the right multiplication projection \(R_{e_k}\) orthogonal on \(L^2(M,\tau)\)?

*Solution.* It is idempotent because \(e_k^2=e_k\). Its adjoint is itself: \(\tau((\xi e_k)^*\zeta)=\tau(e_k\xi^*\zeta)=\tau(\xi^*\zeta e_k)\). For orthogonal \(e_k,e_l\), the corresponding projections have zero product. Left multiplication commutes with them, since \(v(\xi e_k)=(v\xi)e_k\).

**Exercise 2.** Prove the lower bound in (5).

*Solution.* Orthonormality of the second rank-one vectors \(x_i\) removes all cross terms, giving \(\|Q_k\|_{\mathrm{HS}}^2=\sum_i\|x_i e_k\|_2^2\). Summing over the orthogonal \(e_k\)'s gives \(\sum_i\|x_i p\|_2^2\). Each is \(1-\tau(x_i^*x_i(1-p))\ge1-B^2\tau(1-p)>1/2\).

**Exercise 3.** Justify selection of \(k\) between (4) and (5).

*Solution.* If every nonzero \(Q_k\) had summed error at least \(2a^2\|Q_k\|_{\mathrm{HS}}^2\), the total error would exceed \(a^2m\) by (5), contradicting (4). A zero \(Q_k\) has zero conjugation error and contributes nothing, so it does not affect this argument.

**Exercise 4.** Check the conjugates in the cross term (8).

*Solution.* The rank-one pairing gives \(\tau(w_i^*v w_j)\tau((v x_j)^*x_i)=\tau(w_i^*v w_j)\overline{\tau(x_i^*v x_j)}\). Since \(E_{ji}=w_jw_i^*\), cyclicity gives \(\tau(E_{ji}v)=\tau(w_i^*v w_j)\). Summing yields \(\tau(C_v^*v)\).

**Exercise 5.** Explain the two independent parameters in the proof.

*Solution.* The finite-rank model chosen at tolerance \(a\) determines \(m\) and \(B\). The Gram repair moduli tend to zero with \(b\) only for those fixed values. First choose \(a\) to make \(\sqrt2a\) small, then fix the model, then make \(b\) small enough to control \(D_m(b)\), \(\sqrt m\,d_m(b)\) and the uncovered trace. This proves every bound in (3) simultaneously.

**Exercise 6.** Convert (12) from a normalized corner trace to the ambient trace.

*Solution.* In \(eMe\), \(\|z\|_{2,e}=\|z\|_2/\sqrt{\tau(e)}\), while \(\tau_e(f)=\tau(f)/\tau(e)\). Multiply an inequality \(\|z\|_{2,e}\le\varepsilon\sqrt{\tau_e(f)}\) by \(\sqrt{\tau(e)}\). Both factors cancel, leaving (12).

**Exercise 7.** Why is chain closure of the algebras alone insufficient for the Zorn argument?

*Solution.* An upper bound must also satisfy the quantitative residual condition (13). The increasing \(L^2\) subspaces give strong convergence of their expectation projections, while the increasing supports give convergence of the complementary compressions. These two limits and normality of the trace pass the inequality to the generated algebra.

**Exercise 8.** Verify the squared error budget (15).

*Solution.* The two off-diagonal blocks have squared sum \(\|yg-gy\|_2^2\le(\varepsilon^2/4)\tau(g)\). The diagonal approximation error has the same squared bound. Orthogonality gives their sum at most \((\varepsilon^2/2)\tau(g)\). Its normalization uses the new support \(g\).

**Exercise 9.** Why does the maximal algebra supply bounded finite-dimensional approximants to the original \(x\)'s?

*Solution.* At full support its expectation approximates the \(x\)'s within the first tolerance. Its local AFD property supplies a finite algebra \(D\) approximating those finitely many expectations. The triangle inequality bounds the distance of each \(x\) to \(D\). The tracial nearest-point property bounds \(\|x-E_D(x)\|_2\) by that distance, and contractivity gives \(\|E_D(x)\|\le\|x\|\).

**Exercise 10.** Which nonfactor statement is proved here, and what remains open?

*Solution.* The small-corner-to-local-AFD implication of Theorem 3.1 holds in every finite algebra with faithful normal trace. The proof that an injective algebra has small corners uses scalar pinching in a separable \(\mathrm{II}_1\) factor. Thus this route proves the full second factor argument, while the general nonfactor injective converse and its central decomposition consequences still need their separate proof.

## References and proof scope

Sorin Popa, [*A short proof of “injectivity implies hyperfiniteness” for finite von Neumann algebras*](https://www.theta.ro/jot/archive/1986-016-002/1986-016-002-005.pdf), Section 2, Proposition 2.2, and Section 3. These develop almost invariant matrix corners and the maximality proof of finite approximation. Popa works with an abelian-module construction and proves the finite nonfactor theorem. Our selection lemma instead uses an external Hilbert-space finite-rank model and the scalar pinching input; this route to the small-corner condition retains the separable factor hypothesis.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*, author draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf), Definition 11.1.4, Theorem 11.1.5 and its proof, and Theorem 11.1.17. Theorem 3.1 above gives the full local-to-global argument for arbitrary faithfully tracial finite algebras, including chain closure, the expectation limit and the orthogonal error budget. The sequential identification with R uses the earlier exact-containment theorem; it is a separate dependency from this maximality argument.
