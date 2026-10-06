# Stable isomorphism: the Brown–Green–Rieffel theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Morita equivalence identifies the representation theory of two algebras. Stable isomorphism identifies the algebras themselves after adjoining countably many matrix coordinates. The bridge between these descriptions is a unitary between Hilbert modules: an equivalence module, repeated countably often, becomes the standard module. Two countability hypotheses make that unitary possible.

Throughout, tensor products of algebras are spatial, and
\[
\begin{gathered}
\mathcal K=\mathcal K(\ell^2(\mathbb N)),\\
H_A=\ell^2(\mathbb N,A).
\end{gathered}
\tag{1.1}
\]
The algebra \(A\) is **σ-unital** if it has a countable approximate identity. Two algebras are **stably isomorphic** if \(A\otimes\mathcal K\cong B\otimes\mathcal K\). This differs from saying that either algebra is already stable, which means \(A\cong A\otimes\mathcal K\). No separability of \(A\) or \(B\) is assumed.

We use stabilization from *Kasparov’s stabilization theorem*, Theorem 3.1, and the inverse evaluations from *Imprimitivity bimodules and Morita equivalence*, Theorem 3.2. Tensor transport and completion are from *Tensor products and C*-correspondences*, Theorems 1.2 and 2.1; standard-module compact matrices are from *Compact operators, multipliers and the strict topology*, Theorem 2.1. Right inner products are linear in the second variable. A module unitary preserves that inner product and is onto.

## 1. The countable amplification of an equivalence

Let \(E\) be an \(A\)–\(B\) imprimitivity bimodule. Its conjugate \(E^*\) is a \(B\)–\(A\) imprimitivity bimodule. The compact left actions and the inverse evaluations give
\[
\begin{gathered}
\mathcal K(E_B)\cong A,\qquad
\mathcal K(E^*_A)\cong B,\\
E^*\otimes_A E\cong B_B,\qquad
\bar x\otimes y\longmapsto\langle x,y\rangle_B.
\end{gathered}
\tag{1.2}
\]
The criterion proved in *Compact operators, multipliers and the strict topology*, Theorem 3.1, says that a Hilbert module is countably generated precisely when its compact-operator algebra is σ-unital. Consequently,
\[
\begin{aligned}
A\text{ σ-unital}&\Longrightarrow E_B\text{ countably generated},\\
B\text{ σ-unital}&\Longrightarrow E^*_A\text{ countably generated}.
\end{aligned}
\tag{1.3}
\]
The algebra on the opposite side controls the number of generators. Keeping these two implications separate prevents an implicit countability assumption later.

Write \(E^\infty=\bigoplus_{j\geq1}E\), with norm-convergent sums of inner products. The following identification also explains why the left algebra acquires matrix coordinates.

**Lemma 1.1.** There are canonical unitary and algebra identifications
\[
\begin{gathered}
C:H_A\otimes_A E\longrightarrow E^\infty,\\
C((a_j)\otimes x)=(a_jx)_j,\\
\mathcal K(E^\infty)\cong A\otimes\mathcal K.
\end{gathered}
\tag{1.4}
\]

*Proof.* For finitely supported columns \(a,c\), the inner product of their images is
\[
\sum_j\langle a_jx,c_jy\rangle_B
=\left\langle x,\left(\sum_j a_j^*c_j\right)y\right\rangle_B.
\tag{1.5}
\]
This is exactly the interior tensor inner product. The formula respects balancing. It therefore extends isometrically to the completed tensor product. The nondegenerate left action gives \(\overline{AE}=E\); hence every single-coordinate vector is a limit of images, and finite-coordinate vectors are dense in \(E^\infty\). The isometry is onto.

Under the exterior identification \(E^\infty=\ell^2\otimes E\), the compact-operator theorem from *Tensor products and C*-correspondences*, Theorem 5.1, gives
\[
\mathcal K(E^\infty)
\cong\mathcal K\otimes\mathcal K(E)
\cong\mathcal K\otimes A.
\tag{1.6}
\]
Flip the algebra factors. Concretely, \(a\otimes e_{ij}\) acts by inserting \(a x_j\) in coordinate \(i\) and zero elsewhere. Thus this identification agrees with the given left action, rather than merely identifying two abstract algebras. ∎

Interior tensoring also commutes with a countable orthogonal direct sum. On finite tensors the map sends \((m_j)\otimes x\) to \((m_j\otimes x)_j\); the calculation (1.5), with the \(M_j\)-inner products in place of \(a_j^*c_j\), proves isometry. Every finite-coordinate elementary tensor is in its range, proving density and surjectivity. We will use this observation for a direct sum of two modules as well.

**Lemma 1.2 (Two absorptions).** If \(A\) and \(B\) are σ-unital, then
\[
E^\infty\cong H_B
\tag{1.7}
\]
as right Hilbert \(B\)-modules.

*Proof.* Put \(F=H_A\otimes_A E\), identified with \(E^\infty\). Because \(B\) is σ-unital, \(E^*_A\) is countably generated. Stabilization supplies a unitary
\[
E^*\oplus H_A\cong H_A.
\tag{1.8}
\]
Tensor it with \(E\). An adjointable unitary remains a unitary after interior tensoring, by the tensor-operator theorem. Distribute the direct sum, use (1.2), and obtain a unitary
\[
J:B\oplus F\longrightarrow F.
\tag{1.9}
\]
Take a countable direct sum of \(J\). It gives
\[
J^\infty:H_B\oplus F^\infty\longrightarrow F^\infty.
\tag{1.10}
\]
Since \(F=E^\infty\), a bijection \(\mathbb N\times\mathbb N\to\mathbb N\) induces a unitary \(R:F^\infty\to F\). For finite arrays this is just a permutation of coordinates; norm-convergent positive inner-product sums extend it to all arrays. Therefore
\[
\begin{gathered}
V:H_B\oplus F\longrightarrow F,\\
V=R J^\infty(1_{H_B}\oplus R^{-1})
\end{gathered}
\tag{1.11}
\]
is unitary.

The other countability hypothesis now enters. Since \(A\) is σ-unital, \(E_B\) is countably generated. Putting a countable generating set into every coordinate gives a countable generating set for \(F=E^\infty\). Stabilization gives a unitary \(S:F\oplus H_B\to H_B\). Let \(\tau\) exchange the two direct summands. The desired unitary is
\[
U=S\tau V^{-1}:F\longrightarrow H_B.
\tag{1.12}
\]
Each factor is defined on the indicated module. This composes two absorption maps; it never cancels a summand from an isomorphism. ∎

The role of fullness in this proof is the inverse evaluation \(E^*\otimes_A E\cong B\). For a nonfull module that tensor product recovers its coefficient ideal, and the absorption (1.9) need not contain all of \(B\).

## 2. Brown–Green–Rieffel

**Theorem 2.1.** For σ-unital C*-algebras \(A\) and \(B\),
\[
A\sim_M B
\quad\Longleftrightarrow\quad
A\otimes\mathcal K\cong B\otimes\mathcal K.
\tag{2.1}
\]

*Proof.* Suppose first that \(E\) is an \(A\)–\(B\) imprimitivity bimodule. Apply Lemmas 1.1–1.2. Conjugation by the unitary \(U:E^\infty\to H_B\) identifies compact operators: indeed,
\[
U\theta_{\xi,\eta}U^*
=\theta_{U\xi,U\eta}.
\tag{2.2}
\]
It follows, with the standard-module compact algebra, that
\[
\begin{aligned}
A\otimes\mathcal K&\cong\mathcal K(E^\infty)\\
&\cong\mathcal K(H_B)\\
&\cong B\otimes\mathcal K.
\end{aligned}
\tag{2.3}
\]
Each arrow is onto: the first and last are the compact matrix identifications, and the middle one has inverse conjugation by \(U^*\).

Conversely, for any C*-algebra \(D\), the module \(H_D\) is full over \(D\) and has compact left algebra \(D\otimes\mathcal K\). Fullness follows because its coefficient span contains all products \(d^*c\), whose closed span is \(D\). Thus \(D\otimes\mathcal K\sim_M D\), without a σ-unitality assumption. Transport an equivalence across the given stable isomorphism and compose with these standard-module equivalences. Transitivity and conjugation of imprimitivity bimodules give \(A\sim_M B\). The zero-algebra case is immediate. ∎

This is the theorem of Brown, Green and Rieffel, presented in Blackadar, *Operator Algebras*, II.7.6.11, and Li, *Groupoid C*-algebras*, §5.1.2, Theorem 5.5. Its proof uses the stabilization theorem in exactly the form proved earlier; Blackadar, *K-Theory for Operator Algebras*, §13.6 is another reference for that input.

**Corollary 2.2.** If \(A\) and \(B\) are stable and σ-unital, they are Morita equivalent precisely when they are isomorphic.

*Proof.* In (2.3) replace each stabilization by its assumed isomorphism with the original algebra. The converse follows from the identity equivalence transported by an isomorphism. ∎

**Corollary 2.3 (Full amplification).** If \(B\) is σ-unital and \(E_B\) is full and countably generated, then \(E^\infty\cong H_B\).

*Proof.* Give \(E\) its \(\mathcal K(E)\)–\(B\) imprimitivity structure. The countable-generation criterion makes \(\mathcal K(E)\) σ-unital. Lemma 1.2 applies to these two algebras. This recovers the full-amplification theorem proved earlier, and Blackadar’s Corollary II.7.6.12. ∎

The stable isomorphism involves choices of absorption unitaries. The proof establishes existence, and does not prescribe a distinguished algebra map. In particular it gives no general permission to keep a specified hereditary inclusion pointwise fixed.

## 3. Full unital corners and the first matrix coordinate

Let \(A\) be unital and let \(p\in A\) be a **full projection**, meaning \(\overline{ApA}=A\). Put \(B=pAp\). The module \(pA\) has right inner product \(x^*y\), left inner product \(xy^*\), and compact left algebra \(B\). Its right coefficient ideal is \(\overline{ApA}=A\), while its left coefficient span is \(B\), since \(b={}_B\langle b,p\rangle\). This is the full-corner equivalence from *Imprimitivity bimodules and Morita equivalence*, Proposition 2.4.

**Theorem 3.1.** There is an isomorphism
\[
\Phi:(pAp)\otimes\mathcal K\longrightarrow A\otimes\mathcal K
\tag{3.1}
\]
such that
\[
\begin{gathered}
\Phi(b\otimes e_{11})=b\otimes e_{11}\\
(b\in pAp).
\end{gathered}
\tag{3.2}
\]

*Proof.* The algebras \(A\) and \(pAp\) are unital, hence σ-unital. Lemma 1.2 gives \((pA)^\infty\cong H_A\). To arrange (3.2), retain the first summand instead of choosing this unitary arbitrarily.

The source and target decompose as
\[
\begin{aligned}
(pA)^\infty&=pA\oplus (pA)^\infty_{\rm tail},\\
H_A&=pA\oplus G,\\
G&=(1-p)A\oplus H_{A,\rm tail}.
\end{aligned}
\tag{3.3}
\]
The second identity splits the first copy of \(A\) into two orthogonal right Hilbert submodules. Lemma 1.2, with a coordinate shift, gives a unitary from the source tail to \(H_{A,\rm tail}\). The module \((1-p)A\) is generated by \(1-p\); stabilization gives a unitary
\[
(1-p)A\oplus H_{A,\rm tail}\cong H_{A,\rm tail}.
\tag{3.4}
\]
Compose the first tail unitary with the inverse of (3.4), obtaining a unitary \(T\) from the source tail onto the target tail. Set
\[
\begin{gathered}
W:(pA)^\infty\longrightarrow H_A,\\
W=1_{pA}\oplus T.
\end{gathered}
\tag{3.5}
\]
Conjugation by \(W\) identifies \(\mathcal K((pA)^\infty)=B\otimes\mathcal K\) with \(\mathcal K(H_A)=A\otimes\mathcal K\). On the source, \(b\otimes e_{11}\) acts by left multiplication on the first \(pA\) and vanishes on the tail. On the target, its conjugate has that same action on the first \(pA\) and vanishes on \((1-p)A\) and all later coordinates. Since \(b(1-p)=0\), this is exactly the standard operator \(b\otimes e_{11}\) on \(H_A\). ∎

The canonical inclusion \((pAp)\otimes\mathcal K\subset A\otimes\mathcal K\) generally is not onto. The theorem chooses a different isomorphism which agrees with the original inclusion on the first copy of \(pAp\). Its construction uses the orthogonal complement \((1-p)A\).

## 4. Brown’s theorem and a limitation on extension

A closed C*-subalgebra \(B\subset A\) is **hereditary** if \(0\leq a\leq b\in B\) implies \(a\in B\). It is **full** if the closed ideal it generates in \(A\) is all of \(A\).

**Theorem 4.1 (Brown).** If \(B\) is a full hereditary subalgebra of \(A\), and both \(A\) and \(B\) are σ-unital, then
\[
B\otimes\mathcal K\cong A\otimes\mathcal K.
\tag{4.1}
\]
*Proof.* Proposition 2.4 of *Imprimitivity bimodules and Morita equivalence* proves that \(E=\overline{BA}\), with right inner product \(x^*y\) and left inner product \(xy^*\), is a \(B\)–\(\overline{ABA}\) imprimitivity bimodule. Heredity gives its compact left algebra exactly \(B\); fullness gives \(\overline{ABA}=A\). Both coefficient algebras are σ-unital by hypothesis, so Theorem 2.1 of this lesson, already proved by the two-absorption construction, applies to this equivalence module and gives (4.1). ∎

Brown, *Stable isomorphism of hereditary subalgebras of C*-algebras*, Theorem 2.8, p.340, formulates the hypotheses as existence of strictly positive elements. Their equivalence to σ-unitality follows from *Kasparov’s stabilization theorem*, Theorem 1.2, and the countable-generation criterion applied to \(D_D\). Theorem 3.1 proves the unital full-corner case with the additional first-coordinate property.

It is essential to distinguish (4.1) from the stronger statement that the stable isomorphism always extends the hereditary inclusion on its first copy. The following example gives a concrete obstruction to that stronger assertion.

**Proposition 4.2.** Let
\[
\begin{gathered}
A=C([0,1],M_2),\qquad P=E_{11},\\
B=\{f\in A:f(0)\in\mathbb CP\}.
\end{gathered}
\tag{4.2}
\]
Then \(B\) is full hereditary and σ-unital, but no isomorphism in (4.1) can satisfy \(\Phi(b\otimes e_{11})=b\otimes e_{11}\) for every \(b\in B\).

*Proof.* Evaluation shows that \(B\) is a closed C*-subalgebra. If \(0\leq a\leq b\in B\), then \(0\leq a(0)\leq b(0)\) forces \(a(0)\) to be supported on \(P\). Indeed its value on the vector perpendicular to \(P\) is zero; positivity then annihilates that vector and both off-diagonal entries. Thus \(a\in B\). The constant projection \(P\) belongs to \(B\). It generates all of \(A\) as an ideal, because the constant matrix units satisfy \(E_{i1}PE_{1j}=E_{ij}\). Hence \(B\) is full.

For countability use
\[
\begin{aligned}
h(t)&=\operatorname{diag}(1,t),\\
u_n(t)&=h(t)(h(t)+n^{-1})^{-1}\\
&=\operatorname{diag}\left(\frac n{n+1},\frac{nt}{1+nt}\right).
\end{aligned}
\tag{4.3}
\]
These are positive contractions in \(B\). For \(f\in B\), the entries in its second row and column vanish at zero. Given \(\varepsilon>0\), make those entries uniformly small on \([0,\delta]\); on \([\delta,1]\), \((1+nt)^{-1}\) tends uniformly to zero. The first diagonal error is \((n+1)^{-1}\). Entry by entry this proves \(u_nf\to f\) and \(fu_n\to f\) uniformly. Thus \((u_n)\) is an approximate identity. The ambient algebra \(A\) is unital.

Suppose that the asserted extension \(\Phi\) exists. An isomorphism \(D\to D'\) extends to a unital isomorphism \(M(D)\to M(D')\): transport each multiplier’s left and right multiplication maps by the isomorphism and its inverse. The double-centralizer definition and multiplier identification in *Compact operators, multipliers and the strict topology*, Section 4 and Theorem 4.1, give the extension and its inverse. In particular set
\[
\begin{gathered}
q=1_{M(B)}\otimes e_{11},\\
Q=\widetilde\Phi(q)\in M(A\otimes\mathcal K).
\end{gathered}
\tag{4.4}
\]
The extension property and the identity \(q(B\otimes\mathcal K)q=B\otimes e_{11}\) imply
\[
Q(A\otimes\mathcal K)Q=B\otimes e_{11}
\tag{4.5}
\]
as actual subalgebras of \(A\otimes\mathcal K\).

Evaluation at \(t\) is a surjective, nondegenerate map onto \(M_2\otimes\mathcal K\), so it extends to multipliers. Write \(Q(t)\) for the resulting projection on \(\mathbb C^2\otimes\ell^2\). Evaluating (4.5) yields
\[
\begin{aligned}
Q(t)&=I_2\otimes e_{11}&& (t>0),\\
Q(0)&=P\otimes e_{11}.&&
\end{aligned}
\tag{4.6}
\]
Here the equality of corners determines each projection: the ranges of the rank-one operators in \(Q(t)\mathcal K(\mathbb C^2\otimes\ell^2)Q(t)\) span its range. The corresponding corner in (4.5) has the two-dimensional first-coordinate range for \(t>0\), and the one-dimensional \(P\)-range at zero. Evaluation of \(B\) is all of \(M_2\) at any positive \(t\), since functions supported away from zero supply any prescribed value there.

Now take the constant compact-valued function \(k=E_{22}\otimes e_{11}\). By definition of a multiplier, \(Qk\) belongs to
\[
\begin{gathered}
A\otimes\mathcal K=C([0,1],D),\\
D=\mathcal K(\mathbb C^2\otimes\ell^2).
\end{gathered}
\tag{4.7}
\]
But (4.6) gives \((Qk)(t)=k\) for every \(t>0\) and \((Qk)(0)=0\), contradicting norm continuity. The continuous-function identification in (4.7) follows by uniformly approximating compact-valued functions with finite-rank compressions and finite partitions of unity, as in the continuous-field lesson. ∎

The obstruction is the change in the support of the first hereditary corner at the endpoint. Stable isomorphism still holds. What fails is preserving that corner pointwise while extending to an isomorphism of the entire stabilizations.

## 5. Why σ-unitality cannot be discarded

**Proposition 5.1.** If \(H\) is a nonseparable Hilbert space, then \(\mathcal K(H)\sim_M\mathbb C\), but
\[
\mathcal K(H)\otimes\mathcal K\not\cong\mathcal K.
\tag{5.1}
\]
Moreover \(\mathcal K(H)\) is not σ-unital.

*Proof.* The usual module \(H\) is a \(\mathcal K(H)\)–\(\mathbb C\) imprimitivity bimodule: its left inner product is the rank-one operator \(\theta_{\xi,\eta}\), its right inner product is the Hilbert-space inner product, and both spans are full. This construction does not require a countable orthonormal basis.

The exterior compact theorem gives
\[
\mathcal K(H)\otimes\mathcal K
\cong\mathcal K(H\otimes\ell^2).
\tag{5.2}
\]
Choose an uncountable orthonormal family \((\xi_i)\) in \(H\). The projections onto \(\mathbb C(\xi_i\otimes e_1)\) belong to the right side of (5.2); distinct ones have norm distance one. A separable metric space cannot contain an uncountable set with pairwise distance one: balls of radius less than one-half about a countable dense set separate such points. Thus (5.2) is nonseparable. In contrast, \(\mathcal K\) is separable, since finite matrices with rational real and imaginary parts are dense. An isomorphism preserves norm separability, proving (5.1).

Finally, the closure of the range of a compact operator lies in a separable subspace: approximate it in norm by a sequence of finite-rank operators and take the closed span of their ranges. If \((v_n)\) were a countable approximate identity of compact operators on \(H\), the ranges of all \(v_n^*\) would lie in one separable closed subspace \(L\). Choose a unit vector \(\xi\perp L\). Then \(v_n\xi=0\) for every \(n\). Hence
\[
v_n\theta_{\xi,\xi}=0
\quad\text{while}\quad
\|\theta_{\xi,\xi}\|=1,
\tag{5.3}
\]
contradicting the approximate-identity property. ∎

In this example \(B=\mathbb C\) is σ-unital but \(A=\mathcal K(H)\) is not. The conjugate module can be stabilized over \(A\); the step which fails is countable generation of \(E_B=H\), needed to stabilize \(F=H^\infty\) over \(\mathbb C\). Reversing the equivalence reverses the failed hypothesis. Countable generation of one side alone does not supply the two absorptions.

## 6. Matrix and proper-action examples

**Example 6.1 (Matrix stabilization).** For every C*-algebra \(A\) and every integer \(n\geq1\),
\[
M_n(A)\otimes\mathcal K\cong A\otimes\mathcal K.
\tag{6.1}
\]
This example does not need σ-unitality. Identify \(M_n(A)=A\otimes M_n\). The Hilbert-space unitary
\[
\begin{gathered}
T:\mathbb C^n\otimes\ell^2\longrightarrow\ell^2,\\
T(e_i\otimes e_k)=e_{n(k-1)+i}
\end{gathered}
\tag{6.2}
\]
identifies \(M_n\otimes\mathcal K\) with \(\mathcal K\) by conjugation. Tensor that isomorphism with \(1_A\). Put \(\beta(i,k)=n(k-1)+i\). On matrix coordinates it sends
\[
a\otimes E_{ij}\otimes e_{k\ell}
\longmapsto
a\otimes e_{\beta(i,k),\,\beta(j,\ell)}.
\tag{6.3}
\]
Finite matrices are dense, and conjugation is isometric and onto, so the formula extends to the completed algebras. For \(A=\mathbb C\), the finite-dimensional algebra \(M_n\) and \(\mathbb C\) have the same stabilization even though they need not be isomorphic.

**Example 6.2 (A free proper action).** Let a locally compact group \(G\) act continuously, freely and properly on a locally compact Hausdorff space \(X\). Here proper means that \((g,x)\mapsto(gx,x)\) is proper. Put \(Y=G\backslash X\). The free proper-action imprimitivity theorem gives
\[
C_0(X)\rtimes G\sim_M C_0(Y),
\tag{6.4}
\]
with the **full** crossed product. The analytic proof is Proper actions, free actions and the orbit space, Proposition 9.2 and Theorem 9.5: the completion of \(C_c(X)\) is full over \(C_0(Y)\), and its compact algebra is the full crossed product exactly when the action is free. That written proof covers the locally compact Hausdorff hypotheses here with no countability restriction. Williams, Corollary 4.11 and Remark 4.12, credits the classical theorem.

If both algebras in (6.4) are σ-unital, Theorem 2.1 proves
\[
\big(C_0(X)\rtimes G\big)\otimes\mathcal K
\cong C_0(Y)\otimes\mathcal K.
\tag{6.5}
\]
The extra tensor factor on the left is part of this conclusion. For example, take a finite group of order \(n\) acting by translation on \(X=G\times Y\). Multiplication operators on the finite \(G\)-coordinate and translations generate its matrix units, so
\[
C_0(G\times Y)\rtimes G\cong M_n(C_0(Y)).
\tag{6.6}
\]
This is also the finite-group model of the preceding lesson with trivial subgroup, tensored with \(C_0(Y)\). Formula (6.1) gives (6.5) directly. When \(Y\) is a point, the algebra in (6.6) is finite-dimensional and cannot itself be \(\mathcal K\). Thus a stable-isomorphism conclusion must retain both stabilizations unless a separate stability result is available.

## 7. Exercises with complete solutions

**Exercise 13.1.** Show directly that \(A\otimes\mathcal K\cong M_n(A)\otimes\mathcal K\), for arbitrary \(A\).

*Solution.* Use the unitary \(T\) in (6.2). It carries each orthonormal basis vector to exactly one basis vector, because every positive integer has a unique expression \(n(k-1)+i\), \(1\leq i\leq n\). Conjugation sends \(E_{ij}\otimes e_{k\ell}\) to the matrix unit in (6.3), so it is multiplicative and preserves adjoints. Every matrix unit of \(\mathcal K\) occurs. Tensoring with \(A\) gives an isometric onto map on the spatial completions. Its inverse decomposes each row and column index into these unique expressions. Reversing this map gives the requested direction. Neither approximate identities nor countable generators of \(A\) enter.

**Exercise 13.2.** Fill in the unitary \(H_A\otimes_A E\cong H_B\) used in the BGR proof. Explain why direct-sum cancellation is unnecessary.

*Solution.* First apply \(C\) from (1.4), whose inner-product verification is (1.5). Choose a stabilization unitary \(E^*\oplus H_A\to H_A\). Tensor it with \(E\), then use distribution and the inverse evaluation \(\bar x\otimes y\mapsto\langle x,y\rangle_B\), producing \(J:B\oplus F\to F\). For a fixed bijection \(\beta:\mathbb N^2\to\mathbb N\), let \(R\) send coordinate \((j,k)\) of \(F^\infty\) to coordinate \(\beta(j,k)\) of \(F\). It preserves inner products on finite arrays and has a coordinate-permutation inverse. Form \(V\) in (1.11). Choose the second stabilization unitary \(S:F\oplus H_B\to H_B\). Then
\[
S\tau V^{-1}C:H_A\otimes_A E\longrightarrow H_B
\tag{7.1}
\]
is the answer. Its inverse is \(C^{-1}V\tau^{-1}S^{-1}\). Every factor is unitary by a displayed construction or the stated stabilization prerequisite. The identity \(B\oplus F\cong F\) is amplified; no summand is removed by cancellation.

**Exercise 13.3.** Prove the full-corner case for a full projection \(p\) in a unital algebra \(A\). Can the first copy of \(pAp\) be fixed?

*Solution.* The module \(pA\) is full over \(A\), and \(\theta_{x,y}\) is left multiplication by \(xy^*\). Every \(b\in pAp\) is such an operator with \(x=b,y=p\), so \(\mathcal K(pA)=pAp\). Both algebras are unital. Apply Lemma 1.2 to the \(pAp\)–\(A\) equivalence to identify its countable amplification with \(H_A\). Refine the unitary exactly as (3.3)–(3.5): retain the first \(pA\), identify its remaining amplification with the standard tail, and absorb the one-generated complement \((1-p)A\) into that tail by stabilization. Conjugation gives the algebra isomorphism. A first-coordinate operator \(b\) stays on the retained \(pA\) and is zero on the complement; \(b(1-p)=0\) proves that it is precisely the original first-coordinate operator in \(A\otimes\mathcal K\). Thus the first copy can be fixed in this full unital corner case. Proposition 4.2 explains why that refinement is not automatic for general hereditary subalgebras.

**Exercise 13.4.** Locate both uses of σ-unitality and verify the nonseparable counterexample.

*Solution.* For an \(A\)–\(B\) equivalence, \(B\cong\mathcal K(E^*_A)\) is σ-unital precisely when \(E^*_A\) is countably generated. This permits (1.8) and hence absorption of \(H_B\) by \(F\). Independently, \(A\cong\mathcal K(E_B)\) being σ-unital makes \(E_B\), and therefore \(F=E^\infty\), countably generated. This permits the unitary \(F\oplus H_B\to H_B\). These two unitaries compose to the desired map. The converse implication in Theorem 2.1 uses neither countability hypothesis.

Take nonseparable \(H\) and \(E=H\). The rank-one identity \(\theta_{\xi,\eta}\zeta=\xi\langle\eta,\zeta\rangle\) verifies the bimodule compatibility and fullness, so \(\mathcal K(H)\sim_M\mathbb C\). Tensoring compact algebras gives (5.2). Its uncountable orthogonal rank-one projections are mutually distance one, while \(\mathcal K\) has a countable dense family of finite rational matrices; hence no stable isomorphism exists. Finally a putative countable approximate identity \((v_n)\) has adjoint ranges in one separable subspace. A unit vector perpendicular to that subspace satisfies \(v_n\xi=0\), contradicting convergence on \(\theta_{\xi,\xi}\). Thus exactly the missing hypothesis, σ-unitality of \(\mathcal K(H)\), fails.

## What this lesson does not prove

The stabilization theorem, the countable-generation criterion, compact matrix identifications, interior tensor associativity and inverse evaluation are prerequisites with the lesson locators given above. Brown’s general hereditary stable-isomorphism theorem is proved in Section 4 from the previously constructed hereditary equivalence module and the absorption proof of Section 2. The full unital corner case and the obstruction to a general inclusion extension are also proved. The general free proper-action imprimitivity theorem has the written provider Proper actions, free actions and the orbit space, Proposition 9.2 and Theorem 9.5; only the stable consequence and the finite translation example are derived here.

## References

- B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, II.7.6.10–13, especially the BGR theorem II.7.6.11.
- B. Blackadar, *K-Theory for Operator Algebras*, second edition, §13.6, stabilization.
- Y. Li, *Groupoid C*-algebras*, §5.1.2, Theorem 5.5.
- L. G. Brown, [*Stable isomorphism of hereditary subalgebras of C*-algebras*](https://msp.org/pjm/1977/71-2/pjm-v71-n2-p05-s.pdf), *Pacific Journal of Mathematics* 71 (1977), 335–348, Theorem 2.8, p.340.
- D. P. Williams, [*Crossed Products of C*-Algebras*, author’s draft, version 3.1](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf), Corollary 4.11 and Remark 4.12, p.126.
