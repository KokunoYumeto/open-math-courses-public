# Imprimitivity bimodules and Morita equivalence

*Public domain (CC0).*

A matrix algebra and its coefficient algebra are usually different algebras, but their Hilbert-module theories are connected by a rectangular module. Strong Morita equivalence abstracts that connection. Its implementing module has two full inner products, and each inner product turns a vector pair into an operator on the other side. The resulting compatibility identifies one algebra with the compact operators of the module.

We prove this identification, construct inverse and composite equivalences, and place both algebras in a single linking algebra. The proof works for nonunital C*-algebras without separability or countable generation. Stabilization is an example of Morita equivalence; a converse involving stable isomorphism needs additional hypotheses and belongs to the later Brown–Green–Rieffel lesson.

Right inner products are conjugate linear in the first variable. Left inner products are linear in the first variable. We use the preceding results on adjointable and compact operators and the interior tensor product from *Tensor products and C*-correspondences*. The final commutative example uses the fibre and patching results of *Continuous fields over locally compact spaces*.

## 1. Two full inner products

**Definition 1.1.** An \(A\)-\(B\) **imprimitivity bimodule** is a complex vector space \(E\) with commuting left \(A\)- and right \(B\)-actions, a full left Hilbert \(A\)-module inner product \({}_A\langle\xi,\eta\rangle\), and a full right Hilbert \(B\)-module inner product \(\langle\xi,\eta\rangle_B\), satisfying
\[
{}_A\langle\xi,\eta\rangle\zeta
=\xi\langle\eta,\zeta\rangle_B.
\tag{1.1}
\]
Left fullness means that the closed linear span of the left inner products is \(A\); right fullness means the analogous span is \(B\). Each Hilbert structure is initially complete in its own norm,
\[
\|\xi\|_A=\|{}_A\langle\xi,\xi\rangle\|^{1/2},
\qquad
\|\xi\|_B=\|\langle\xi,\xi\rangle_B\|^{1/2}.
\tag{1.2}
\]
We will prove that these norms coincide. **Strong Morita equivalence**, written \(A\sim B\), means the existence of such a bimodule. Throughout this lesson, “Morita equivalence” means this C*-algebra notion.

The two coefficient actions are faithful. For example, if \(Eb=0\), then \(\langle\xi,\eta\rangle_B b=\langle\xi,\eta b\rangle_B=0\). Fullness gives \(Bb=0\), and an approximate identity yields \(b=0\). The argument for \(aE=0\) uses the left inner products. We will repeatedly use this way of detecting a coefficient from its action.

**Lemma 1.2.** The actions have cross-adjoint identities
\[
\begin{aligned}
\langle a\xi,\eta\rangle_B
&=\langle\xi,a^*\eta\rangle_B,\\
{}_A\langle\xi b,\eta\rangle
&={}_A\langle\xi,\eta b^*\rangle.
\end{aligned}
\tag{1.3}
\]
Consequently left multiplication by \(a\) is adjointable on \(E_B\), with adjoint multiplication by \(a^*\), and is contractive in the sense \(\|a\xi\|_B\leq\|a\|\|\xi\|_B\). The analogous assertions hold for right multiplication on the left Hilbert module.

*Proof.* For every \(\zeta\), compatibility and left-inner-product conjugate symmetry give
\[
\begin{aligned}
\zeta\langle a\xi,\eta\rangle_B
&={}_A\langle\zeta,a\xi\rangle\eta\\
&={}_A\langle\zeta,\xi\rangle a^*\eta
=\zeta\langle\xi,a^*\eta\rangle_B.
\end{aligned}
\tag{1.4}
\]
Faithfulness of the right coefficient action proves the first equality in (1.3). For the second, apply both coefficients to \(\zeta\): the first gives \(\xi b\langle\eta,\zeta\rangle_B\), while the second gives the same vector because
\(\langle\eta b^*,\zeta\rangle_B=b\langle\eta,\zeta\rangle_B\). Faithfulness of the left action proves equality.

An everywhere-defined map with an everywhere-defined adjoint on complete Hilbert modules is automatically bounded [*Adjointable operators*, Theorem 2.1]. Thus the formal adjoints just computed are bounded operators. Left multiplication is a *-homomorphism \(A\to\mathcal L(E_B)\), hence contractive. Right multiplication is a *-homomorphism from the opposite algebra on the left Hilbert module, so has the same bound. This reasoning has not assumed equality of the two module norms. ∎

**Theorem 1.3.** Left multiplication is an isomorphism
\[
\lambda:A\overset\cong\longrightarrow\mathcal K(E_B).
\tag{1.5}
\]
The two Hilbert-module norms are equal.

*Proof.* The coefficient faithfulness above makes \(\lambda\) injective, hence isometric. Compatibility says
\[
\lambda({}_A\langle\xi,\eta\rangle)
=\theta_{\xi,\eta}.
\tag{1.6}
\]
Fullness on the left and continuity show that every \(\lambda(a)\) is compact. Conversely the image contains every rank one; it is closed, being the image of a C*-algebra by an injective *-homomorphism. Therefore it is the entire compact algebra.

The diagonal rank-one norm is \(\|\theta_{\xi,\xi}\|=\|\xi\|_B^2\) [*Compact operators, multipliers and the strict topology*, Proposition 1.1]. Using isometry in (1.6) gives
\[
\|\xi\|_A^2
=\|{}_A\langle\xi,\xi\rangle\|
=\|\theta_{\xi,\xi}\|
=\|\xi\|_B^2.
\tag{1.7}
\]
Taking square roots proves the assertion. ∎

This also shows that both actions are nondegenerate. Approximate identities of a Hilbert module's coefficient algebra act pointwise on its vectors; apply that fact to each of the two Hilbert structures. For incomplete pre-imprimitivity modules over dense pre-C*-algebras, the automatic boundedness step in Lemma 1.2 is unavailable. One must assume suitable bounds on the actions before completing; this is the distinction in [Blackadar 2006, II.7.6.4].

## 2. Compact operators and rectangular examples

**Proposition 2.1.** Every full Hilbert \(B\)-module \(E\) is a \(\mathcal K(E)\)-\(B\) imprimitivity bimodule with its natural action and
\[
{}_{\mathcal K(E)}\langle\xi,\eta\rangle
=\theta_{\xi,\eta}.
\tag{2.1}
\]

*Proof.* The rank-one adjoint and multiplication identities give left linearity, conjugate symmetry and compatibility. Diagonal rank ones are positive, vanish only for a zero vector, and have norm \(\|\xi\|^2\). The left module is therefore complete with the original norm. Left fullness is the definition of \(\mathcal K(E)\); right fullness is assumed. The actions commute because compact operators are \(B\)-linear. ∎

Theorem 1.3 and Proposition 2.1 characterize equivalence modules by a full right module and an identification of the left algebra with its compacts. Fullness matters: for an arbitrary \(E\), the same argument gives equivalence with its inner-product ideal \(J_E\subseteq B\), rather than with all of \(B\).

**Example 2.2.** The identity module \(B\) has inner products \({}_B\langle x,y\rangle=xy^*\) and \(\langle x,y\rangle_B=x^*y\). It is full since products span a dense subspace of \(B\). This is true without a unit, by an approximate identity.

For positive integers \(m,n\), the rectangular space \(M_{m,n}(B)\) has the matrix actions and
\[
{}_{M_m(B)}\langle x,y\rangle=xy^*,
\qquad
\langle x,y\rangle_{M_n(B)}=x^*y.
\tag{2.2}
\]
Associativity of matrix multiplication proves compatibility. Both diagonal products are positive; the two norms are the same rectangular C*-norm, computed by embedding the rectangle as an off-diagonal block in \(M_{m+n}(B)\). This norm is complete. Each matrix entry on either side is approximated by sums of products from \(B\): choose rectangles with one appropriate shared row or column and use density of products in \(B\). Thus both inner products are full. In particular \(B^n=M_{n,1}(B)\) proves \(M_n(B)\sim B\).

**Example 2.3.** A nonzero Hilbert space \(H\), with its scalar inner product and its usual compact rank ones as the left inner product, gives \(\mathcal K(H)\sim\mathbb C\). Separability is unnecessary. Likewise \(H_B\) is full over \(B\): its first-coordinate vectors have inner products \(b^*c\), whose span is dense. Its compact algebra is \(B\otimes\mathcal K\) [*Compact operators, multipliers and the strict topology*, Theorem 2.1]. Therefore
\[
B\otimes\mathcal K\sim B
\tag{2.3}
\]
for every C*-algebra \(B\), with no \(\sigma\)-unitality assumption. Taking \(B=C_0(X)\) in the finite matrix example gives \(C_0(X,M_n)\sim C_0(X)\).

**Proposition 2.4 (Full corners).** For a projection \(p\in M(B)\), assume
\[
\overline{\operatorname{span}}BpB=B.
\tag{2.4}
\]
Then \(pB\), with multiplication actions and inner products \(xy^*\) and \(x^*y\), is a \(pBp\)-\(B\) imprimitivity bimodule.

*Proof.* It is a closed subspace of \(B\), the range of bounded idempotent left multiplication by \(p\). Both norms are its algebra norm, and compatibility is associativity. Left inner products span \(pBp\), because products in \(B\) are dense. Right inner products span \(\overline{BpB}\), which is \(B\) by (2.4). All the Hilbert axioms follow from the C*-algebra identities. ∎

**Example 2.5 (A Toeplitz corner).** Let \(S\) be the unilateral shift on \(\ell^2(\mathbb N_0)\), and \(\mathcal T=C^*(S)\). The proper projection \(p=SS^*\in\mathcal T\) is full, since \(S^*pS=1\) belongs to \(\mathcal T p\mathcal T\). Thus \(p\mathcal T p\sim\mathcal T\). In fact \(a\mapsto SaS^*\) is an isomorphism from \(\mathcal T\) onto this corner, with inverse \(c\mapsto S^*cS\).

The rank-one defect projection \(r=1-SS^*\) is not full. Every product \(arb\) is compact, so its generated ideal cannot contain the identity on the infinite-dimensional Hilbert space. The products \(S^irS^{*j}\) are all matrix units; they show that this ideal is exactly \(\mathcal K\). Its scalar corner is consequently equivalent to \(\mathcal K\), not to the entire Toeplitz algebra by that corner module. This example distinguishes a nonzero corner from a full one.

## 3. The conjugate module and evaluation

For an \(A\)-\(B\) imprimitivity module \(E\), let \(E^*\) be its conjugate complex vector space. Denote its elements by \(\overline\xi\), so \(z\overline\xi=\overline{\bar z\xi}\). Set
\[
b\overline\xi a=\overline{a^*\xi b^*},
\tag{3.1}
\]
and define
\[
\begin{aligned}
{}_B\langle\overline\xi,\overline\eta\rangle
&=\langle\xi,\eta\rangle_B,\\
\langle\overline\xi,\overline\eta\rangle_A
&={}_A\langle\xi,\eta\rangle.
\end{aligned}
\tag{3.2}
\]
The complex conjugation of the vector space changes which variable is linear; no extra swap of the original vectors is needed with these conventions.

**Proposition 3.1.** These formulas make \(E^*\) a \(B\)-\(A\) imprimitivity bimodule.

*Proof.* Conjugating (3.1) verifies the commuting associative actions. Conjugation of the vector space gives the required sesquilinearity in (3.2). The coefficient identities are
\(\langle\xi b^*,\eta\rangle_B=b\langle\xi,\eta\rangle_B\) and
\({}_A\langle\xi,a^*\eta\rangle={}_A\langle\xi,\eta\rangle a\), exactly as required for the left \(B\)- and right \(A\)-inner products. Positivity, definiteness, norm equality, completeness and fullness follow from those of the original inner products. Compatibility follows because
\({}_B\langle\overline\xi,\overline\eta\rangle\overline\zeta=\overline{\zeta\langle\eta,\xi\rangle_B}\), whereas
\(\overline\xi\langle\overline\eta,\overline\zeta\rangle_A=\overline{{}_A\langle\zeta,\eta\rangle\xi}\); these agree by (1.1). ∎

**Theorem 3.2 (Inverse evaluation).** The maps
\[
\begin{aligned}
U:E^*\otimes_A E&\longrightarrow B,\\
\overline\xi\otimes\eta&\longmapsto\langle\xi,\eta\rangle_B,\\
W:E\otimes_B E^*&\longrightarrow A,\\
\xi\otimes\overline\eta&\longmapsto{}_A\langle\xi,\eta\rangle.
\end{aligned}
\tag{3.3}
\]
are unitary bimodule isomorphisms.

*Proof.* For \(U\), the balancing relation follows from
\(\langle a^*\xi,\eta\rangle_B=\langle\xi,a\eta\rangle_B\), and the tensor map is complex bilinear in \(\overline\xi,\eta\). Its inner-product identity is
\[
\begin{aligned}
\langle\overline\xi\otimes\eta,
 \overline\zeta\otimes\omega\rangle_B
&=\langle\eta,{}_A\langle\xi,\zeta\rangle\omega\rangle_B\\
&=\langle\eta,\xi\rangle_B\langle\zeta,\omega\rangle_B\\
&=U(\overline\xi\otimes\eta)^*
  U(\overline\zeta\otimes\omega).
\end{aligned}
\tag{3.4}
\]
It therefore descends through the tensor null space and extends isometrically. Fullness makes its range dense in \(B\), and the range of an isometry from a complete space is closed. Thus it is onto and unitary. Left and right actions are preserved: for example,
\(\langle\xi b^*,\eta c\rangle_B=b\langle\xi,\eta\rangle_Bc\).

Apply the same proved map to the \(B\)-\(A\) module \(E^*\). Its double conjugate is canonically \(E\), and its right inner product is \({}_A\langle\xi,\eta\rangle\); the resulting map is exactly \(W\). This proves its balancing, inner-product preservation, surjectivity and both action identities as well. ∎

## 4. Composition and the equivalence relation

**Theorem 4.1.** If \(E\) is an \(A\)-\(B\) imprimitivity module and \(F\) a \(B\)-\(C\) imprimitivity module, then \(G=E\otimes_B F\) is an \(A\)-\(C\) imprimitivity module. On elementary vectors its left inner product is
\[
{}_A\langle\xi\otimes y,\zeta\otimes w\rangle
={}_A\langle\xi\,{}_B\langle y,w\rangle,\zeta\rangle.
\tag{4.1}
\]

*Proof.* The completed right Hilbert \(C\)-module and its adjointable left \(A\)-action \(\lambda_G\) exist by the interior tensor theorem. Its right inner products span \(C\). Indeed, they include
\(\langle y,\langle\xi,\zeta\rangle_Bw\rangle_C\). Since the inner products of \(E\) span \(B\), their closure includes \(\langle y,bw\rangle_C\) for every \(b\in B\). Nondegeneracy of the left action on \(F\) and an approximate identity give all \(\langle y,w\rangle_C\), whose span is dense in \(C\).

The action \(\lambda_G\) is faithful. If \(\lambda_G(a)=0\), then \((a\xi)\otimes y=0\) for every \(\xi,y\). Its squared inner product is
\(\langle y,\lambda_F(\langle a\xi,a\xi\rangle_B)y\rangle_C=0\). The middle operator is positive, so testing all \(y\) makes its square root zero. Faithfulness of \(\lambda_F\) gives \(\langle a\xi,a\xi\rangle_B=0\), hence \(a\xi=0\) for all \(\xi\). Faithfulness on \(E\) gives \(a=0\).

For \(\xi\in E\), the map \(T_\xi:F\to G\), \(y\mapsto\xi\otimes y\), is bounded by \(\|\xi\|\). Its adjoint is
\[
T_\xi^*(\zeta\otimes w)
=\lambda_F(\langle\xi,\zeta\rangle_B)w.
\tag{4.2}
\]
To justify the extension in (4.2), the tensor inner-product identity gives \(\langle T_\xi y,z\rangle=\langle y,Rz\rangle\) on finite tensors. The identity \(\|v\|=\sup_{\|y\|\leq1}\|\langle y,v\rangle\|\) proves \(\|Rz\|\leq\|T_\xi\|\|z\|\), including independence of representatives. Thus \(R\) extends and is the adjoint.

Compatibility on \(E\) now gives
\[
\lambda_G({}_A\langle\xi,\zeta\rangle)
=T_\xi T_\zeta^*.
\tag{4.3}
\]
This operator is compact. For an approximate identity \((f_i)\) of \(B\), \(\xi f_i\to\xi\) and \(T_{\xi f_i}=T_\xi\lambda_F(f_i)\). Since \(\lambda_F(B)=\mathcal K(F)\), the operators \(T_\xi\lambda_F(f_i)T_\zeta^*\) are compact on \(G\) and converge in norm to (4.3). Here compactness follows first for a rank one \(\theta_{y,w}\), whose composition is \(\theta_{T_\xi y,T_\zeta w}\), and then by norm approximation. Left fullness of \(E\) shows that \(\lambda_G(A)\subseteq\mathcal K(G)\).

Conversely, \(\theta_{y,w}=\lambda_F({}_B\langle y,w\rangle)\), and therefore
\[
\theta_{\xi\otimes y,\zeta\otimes w}
=\lambda_G({}_A\langle\xi\,{}_B\langle y,w\rangle,\zeta\rangle).
\tag{4.4}
\]
Elementary tensors span a dense submodule, so these rank ones span a dense subspace of \(\mathcal K(G)\). The faithful image \(\lambda_G(A)\) is closed. Thus \(\lambda_G(A)=\mathcal K(G)\).

Proposition 2.1 now supplies a full left inner product on \(G\), transported through this isomorphism. Formula (4.4) is exactly (4.1). In particular it is independent of all tensor presentations and extends continuously; positivity and compatibility follow from the compact-module construction. This proves the full imprimitivity assertion without assuming a left tensor norm in advance. ∎

**Corollary 4.2.** Strong Morita equivalence is an equivalence relation.

*Proof.* The identity module in Example 2.2 gives reflexivity. Proposition 3.1 gives symmetry, and Theorem 4.1 gives transitivity. The inverse evaluation in Theorem 3.2 also identifies the inverse tensor products with the identity bimodules. ∎

## 5. The linking algebra

**Theorem 5.1.** Two C*-algebras \(A,B\) are Morita equivalent if and only if they are isomorphic to complementary full corners of a C*-algebra \(L\). Precisely, there is a projection \(p\in M(L)\), with \(q=1-p\), such that
\[
A\cong pLp,
\qquad B\cong qLq,
\tag{5.1}
\]
and both closed spans \(LpL\) and \(LqL\) are \(L\).

*Proof, construction from a module.* Let \(E\) implement \(A\sim B\). On the Hilbert \(B\)-module \(E\oplus B\), take
\[
L=\mathcal K(E\oplus B).
\tag{5.2}
\]
We identify its blocks explicitly. The creation map \(T_\xi:B\to E\), \(b\mapsto\xi b\), has adjoint \(T_\xi^*\eta=\langle\xi,\eta\rangle_B\) and exact norm \(\|\xi\|\): an approximate identity gives \(\xi e_i\to\xi\), providing the lower bound. Every compact \(B\to E\) is a creation map, since a rank one \(\theta_{\xi,b}\) is \(T_{\xi b^*}\), products \(\xi b^*\) span densely in \(E\), and the isometric image is closed. Thus \(\mathcal K(B,E)=E\), with \(\mathcal K(E,B)=E^*\) by adjoints. Together with \(\mathcal K(E)=A\) and \(\mathcal K(B)=B\), this gives
\[
L=\begin{pmatrix}A&E\\E^*&B\end{pmatrix}.
\tag{5.3}
\]
These are compact-operator blocks, so (5.2) already proves the C*-algebra norm and completeness.

A block \(\ell=\left(\begin{smallmatrix}a&\xi\\\overline\eta&b\end{smallmatrix}\right)\) acts by
\[
\ell(\zeta,c)
=(a\zeta+\xi c,
  \langle\eta,\zeta\rangle_B+bc).
\tag{5.4}
\]
Multiplication is operator multiplication; in particular the two cross products are \({}_A\langle\xi,\eta\rangle\) and \(\langle\eta,\xi\rangle_B\). The adjoint is
\[
\ell^*=\begin{pmatrix}a^*&\eta\\\overline\xi&b^*\end{pmatrix}.
\tag{5.5}
\]
Faithfulness of the diagonal representations and the creation-map norm make the block identification faithful. Each block norm is at most \(\|\ell\|\), by coordinate compression, and \(\|\ell\|\leq\|a\|+\|\xi\|+\|\eta\|+\|b\|\), by summing the four blocks. These estimates also directly verify completeness of the block presentation.

The coordinate projections \(p,q\) on \(E\oplus B\) are adjointable and preserve the compact algebra on both sides. The multiplier identification \(\mathcal L(E\oplus B)=M(\mathcal K(E\oplus B))\) puts them in \(M(L)\). Their corners are the two diagonal algebras.

To prove fullness, let \(I\) be the closed span \(LpL\). It contains the upper-left corner, since products \(AA\) span \(A\). Products of lower-left and upper-right blocks through \(p\) give every bottom-right inner product \(\langle\eta,\xi\rangle_B\), so it also contains the bottom-right corner by right fullness. Multiplying these diagonal corners by off-diagonal blocks and using module approximate identities gives every off-diagonal block. Hence \(I=L\). For the closed span \(LqL\), start with the bottom-right corner and use upper-right times lower-left to obtain all \({}_A\langle\xi,\eta\rangle\). Left fullness and the same approximate-identity argument give all blocks. Thus \(q\) is full too.

*Proof, construction from corners.* Suppose \(p,q\in M(L)\) are complementary and full. Put \(A=pLp\), \(B=qLq\), and \(E=pLq\). This is a closed subspace, since \(\ell\mapsto p\ell q\) is a bounded projection. Give it multiplication actions and inner products \(xy^*\) and \(x^*y\). They are positive and definite, have the same complete algebra norm by the C*-identity, and satisfy compatibility by associativity.

Fullness of \(q\) gives
\[
pLp=\overline{\operatorname{span}}pLqLp
=\overline{\operatorname{span}}EE^*;
\tag{5.6}
\]
fullness of \(p\) gives \(qLq=\overline{\operatorname{span}}E^*E\). Thus both module inner products are full. This is the desired imprimitivity module, completing the proof. ∎

The linking algebra retains the implementing module: \(E=pLq\). Its description refers to that module as well as the diagonal algebras. One should not designate a unique linking algebra using only the symbols \(A\) and \(B\). The theorem is the complementary-full-corner characterization in [Blackadar 2006, II.7.6.9] and [Li 2024, Theorem 5.8].

## 6. Hereditary subalgebras and the commutative case

**Proposition 6.1.** A full hereditary C*-subalgebra \(H\subseteq B\) is Morita equivalent to \(B\), without a countability assumption.

*Proof.* Heredity means that \(0\leq x\leq h\in H_+\) implies \(x\in H\). It implies \(HBH\subseteq H\): for \(h\in H\) and \(b\in B_+\),
\(0\leq hbh^*\leq\|b\|hh^*\), so \(hbh^*\in H\). Polarizing in \(h\) gives \(hbk^*\in H\), and writing an arbitrary \(b\) as a linear combination of positive elements gives the inclusion.

Let \(E=\overline{HB}\subseteq B\), where the bar denotes the closed linear span. It is a closed right module and is invariant under left \(H\). Its inner products \(xy^*\) and \(x^*y\) lie in \(H\) and \(B\) respectively. The left inclusion uses \(HBH\subseteq H\). Positivity, completeness, norm equality and compatibility are inherited from \(B\). Also \(H\subseteq E\), by an approximate identity of \(B\), so the left inner products span \(H\). On the right their closed span is the ideal generated by \(H^*H\), hence by \(H\). Fullness of the hereditary subalgebra makes that ideal \(B\). Thus \(E\) implements the equivalence. ∎

**Theorem 6.2.** Two commutative C*-algebras are strongly Morita equivalent if and only if they are isomorphic. Their Gelfand spectra are consequently homeomorphic.

*Proof.* The zero algebra can be equivalent only to itself, by definiteness and fullness, so assume the algebras nonzero. Write \(B=C_0(Y)\) and let \(E\) implement \(A\sim B\). By Theorem 1.3, \(A\cong\mathcal K(E)\), which is commutative. The continuous-field dictionary gives a nonzero Hilbert fibre \(E_y\) at every \(y\), by fullness, and an onto evaluation
\(\mathcal K(E)\to\mathcal K(E_y)\). Its quotient is commutative. A Hilbert space of dimension at least two has noncommuting compact rank ones: for orthonormal \(u,v\), \(\theta_{u,u}\theta_{u,v}=\theta_{u,v}\) whereas \(\theta_{u,v}\theta_{u,u}=0\). Therefore every fibre is one-dimensional.

For \(k\in\mathcal K(E)\), write \(k_y=f_k(y)1_{E_y}\). This defines a continuous scalar function. Around any \(y\), choose a continuous section \(\xi\) nonzero nearby; then
\[
f_k(t)=
\frac{\langle\xi(t),k_t\xi(t)\rangle}
 {\langle\xi(t),\xi(t)\rangle}.
\tag{6.1}
\]
The numerator is continuous because a compact operator preserves continuous sections, and the denominator is continuous and positive on that neighborhood. Moreover \(|f_k(y)|=\|k_y\|\) vanishes at infinity, and \(\|k\|=\sup_y\|k_y\|\), by the compact-field norm theorem. Hence \(k\mapsto f_k\) is an isometric *-homomorphism into \(C_0(Y)\).

Its image is closed, is a \(C_0(Y)\)-submodule (scalar multiplication preserves module compacts), and evaluates onto \(\mathbb C\) at every point by exact compact evaluation. The compact-set patching lemma of *Continuous fields over locally compact spaces*, Lemma 1.2, therefore makes this image all of \(C_0(Y)\). We obtain \(A\cong\mathcal K(E)\cong B\). Conversely an isomorphism transports the identity bimodule of \(B\) to an \(A\)-\(B\) imprimitivity module. Gelfand duality turns the algebra isomorphism into a homeomorphism of spectra. ∎

This proof uses the rank-one fibres directly, rather than the general primitive-spectrum correspondence proved in the next lesson. It allows arbitrary locally compact Hausdorff spectra and does not assume that the implementing line field is globally trivial.

## 7. Exercises with complete solutions

**Exercise 11.1 (Equality of norms).** Prove that the left and right Hilbert norms of an imprimitivity module coincide, without using this equality to justify the boundedness of the actions.

*Solution.* Compatibility and coefficient fullness give the cross-adjoint identities (1.3). Each action is therefore an everywhere-defined adjointable map on the relevant complete Hilbert module, so is bounded by the automatic boundedness theorem. The left action is a faithful *-homomorphism: if \(aE=0\), then \(a\,{}_A\langle E,E\rangle=0\), and fullness gives \(aA=0\), hence \(a=0\). It is consequently isometric. Compatibility identifies the image of \({}_A\langle\xi,\xi\rangle\) with \(\theta_{\xi,\xi}\). The diagonal rank-one norm is \(\|\xi\|_B^2\), so \(\|\xi\|_A^2=\|\xi\|_B^2\), and square roots give the desired equality. The boundedness argument used each Hilbert structure's completeness separately, avoiding a circular use of the norm equality. ∎

**Exercise 11.2 (Rectangular modules).** Verify all imprimitivity conditions for \(M_{m,n}(B)\), with \(m,n\geq1\), over \(M_m(B)\) and \(M_n(B)\).

*Solution.* The actions commute by associativity. With inner products (2.2), matrix adjoints give conjugate symmetry and the required linearity; positivity is positivity of \(xx^*\) and \(x^*x\). Both products vanish only when \(x=0\). Embed the rectangle in the upper-right block of \(M_{m+n}(B)\). The C*-identity gives \(\|xx^*\|^{1/2}=\|x\|=\|x^*x\|^{1/2}\), and this closed block space is complete. Compatibility is \((xy^*)z=x(y^*z)\).

For left fullness, choose two rectangles supported in positions \((i,1)\) and \((j,1)\). Their product has a chosen \((i,j)\) entry \(bc^*\), with all others zero. Products \(bc^*\) span a dense subspace of \(B\), proving left fullness entry by entry. For right fullness, use positions \((1,i)\) and \((1,j)\), obtaining the chosen entry \(b^*c\). The same product-density argument proves right fullness. This works for nonunital \(B\) and proves all the axioms. ∎

**Exercise 11.3 (The inverse module).** Prove that \(E^*\otimes_A E\cong B\), giving the balancing and inner-product checks explicitly.

*Solution.* Use the conjugate module of (3.1)–(3.2), and send \(\overline\xi\otimes\eta\) to \(\langle\xi,\eta\rangle_B\). Complex conjugation in the first vector makes this linear in \(\overline\xi\). The balanced vectors \(\overline\xi a\otimes\eta\) and \(\overline\xi\otimes a\eta\) map to the same coefficient, since \(\langle a^*\xi,\eta\rangle_B=\langle\xi,a\eta\rangle_B\).

The tensor inner product of \(\overline\xi\otimes\eta\) and \(\overline\zeta\otimes\omega\) is \(\langle\eta,{}_A\langle\xi,\zeta\rangle\omega\rangle_B\). Compatibility changes this to \(\langle\eta,\xi\rangle_B\langle\zeta,\omega\rangle_B\), the product of the first image's adjoint and the second image. The identity extends to finite sums, showing that null tensors map to zero and that the map extends isometrically. Its image contains all right inner products, hence is dense by fullness; completeness makes the image closed, so it is onto. Finally the images of \(b\overline\xi\otimes\eta c\) are \(\langle\xi b^*,\eta c\rangle_B=b\langle\xi,\eta\rangle_Bc\). Thus the onto isometry preserves both actions and is unitary. ∎

**Exercise 11.4 (The linking projection).** Prove that the linking block algebra is a C*-algebra and that its first coordinate projection is a full multiplier projection, including when the coefficient algebras are nonunital.

*Solution.* Represent a block on \(E\oplus B\) by (5.4). Its adjoint is (5.5), and compatibility makes the cross products the two coefficient inner products. The corner descriptions \(\mathcal K(E)=A\), \(\mathcal K(B,E)=E\), \(\mathcal K(E,B)=E^*\), and \(\mathcal K(B)=B\) show that the block algebra is exactly \(\mathcal K(E\oplus B)\), hence a norm-closed C*-algebra. Alternatively, compression bounds each block norm by the operator norm and the sum of block norms bounds the operator norm, so completeness follows from completeness of the four block spaces.

The coordinate projection \(p\) need not belong to the compact algebra. It is adjointable and satisfies \(pL,Lp\subseteq L\), so defines a projection of \(M(L)\). The closed ideal \(\overline{LpL}\) contains products of upper-left blocks and hence all of \(A\). Multiplication of lower-left by upper-right blocks through \(p\) puts every \(\langle\eta,\xi\rangle_B\) in that ideal; right fullness puts all of \(B\) there. Approximate identities of the diagonal algebras then recover both off-diagonal blocks in the ideal, so it is \(L\). This proves fullness without requiring an identity in either diagonal algebra. Exchanging the coordinates and using left fullness proves the same for \(1-p\). ∎

**Exercise 11.5 (Commutative equivalence).** Show that two commutative C*-algebras are strongly Morita equivalent exactly when they are isomorphic.

*Solution.* The zero case follows from fullness and definiteness. Otherwise let \(E\) implement the equivalence and write the right algebra as \(C_0(Y)\). The left algebra is \(\mathcal K(E)\). Fullness makes every fibre \(E_y\) nonzero, and compact evaluation onto \(\mathcal K(E_y)\) transfers commutativity to this fibre algebra. The rank-one calculation in Theorem 6.2 rules out two independent vectors in any fibre, so each has dimension one.

Each compact operator now gives a scalar function \(f_k\). Local nonzero sections give its continuous formula (6.1); the compact norm theorem gives \(f_k\in C_0(Y)\) and \(\|f_k\|_\infty=\|k\|\). These functions form a closed \(C_0(Y)\)-submodule evaluating onto every scalar fibre. For any \(f\in C_c(Y)\), choose finitely many local approximations from that submodule on a compact neighborhood of its support; a finite partition and scalar cutoffs patch them to an arbitrarily close global approximation. Closedness and density of \(C_c(Y)\) give every function in \(C_0(Y)\). Thus the left algebra is isomorphic to the right one. Conversely transport the identity module along an algebra isomorphism. This proves both directions without assuming triviality of the line field or a countable base. ∎

## What this lesson does not prove

The Hilbert-module inputs are automatic boundedness of adjointable maps [*Adjointable operators*, Theorem 2.1], the rank-one adjoint, positivity and exact diagonal norm [*Compact operators, multipliers and the strict topology*, Proposition 1.1], and its multiplier and standard-compact identifications [there, Theorem 4.1 and Theorem 2.1]. We use the nondegenerate coefficient action on a Hilbert module [*Hilbert C*-modules*, Proposition 5.2]. Interior tensor completion and adjointable operator transport are [*Tensor products and C*-correspondences*, Theorems 1.2 and 2.1].

The commutative proof uses [*Continuous fields over locally compact spaces*, Lemma 1.2, Theorems 2.2 and 3.1, Lemma 4.1, and the fullness criterion following Theorem 4.2]. Gelfand duality identifies a commutative C*-algebra with \(C_0\) of its locally compact Hausdorff spectrum; this is Theorem 2.1 and Proposition 2.2 of *C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients*, including the nonunital and zero-algebra cases. The compactness of Hilbert-space matrix units used in the Toeplitz example follows directly from their finite-dimensional ranges.

We have proved strong Morita equivalence as an equivalence relation and the linking-algebra theorem, not the full representation-category or ideal-lattice correspondence. We proved Morita equivalence with stabilization, full multiplier corners and full hereditary subalgebras; the converse from Morita equivalence to stable isomorphism is not asserted without \(\sigma\)-unital hypotheses. The later lessons develop the Rieffel correspondence, Brown–Green–Rieffel stable isomorphism and K-theory invariance. Groupoid equivalence and symmetric crossed-product imprimitivity are separate theorems; they are not imported here. Algebraic Morita equivalence of rings is a different setting and is not being identified with this definition.

## References

- B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006; [author revised version](https://www.bruceblackadar.com/Mathematics/Cycr.pdf), II.7.6.1–II.7.6.9.
- H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, Section 6.1.
- A. Connes, [*Noncommutative Geometry*](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), Academic Press, 1994, Chapter II, Appendix A, especially Definition 7 and the discussion of equivalence bimodules.
- Y. Li, [*Groupoid C*-algebras*](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), Leiden seminar notes, revised February 2024, Section 5.2.1, Definition 5.7 and Theorem 5.8.
