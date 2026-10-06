# Takai duality

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Crossing by an abelian group introduces a dual action. Crossing again restores the coefficient algebra, with a compact-operator factor. We prove this by identifying the covariant representations, removing a diagonal action, and applying the translation theorem of Lesson 7. Tracking the generators will also determine the double dual action and the invariant ideals.

Let \(G\) be a locally compact Hausdorff abelian group, \(\alpha:G\to\operatorname{Aut}(A)\) strongly continuous, and \(A\) an arbitrary C*-algebra. Fix Haar measure on \(G\) and its Plancherel dual Haar measure on \(\widehat G\). No separability or unitality hypothesis is imposed. Write
\[
 B=A\rtimes_\alpha G,\qquad C=B\rtimes_{\widehat\alpha}\widehat G.
 \tag{8.1}
\]
The dual convention from Lesson 6 is positive:
\[
 \widehat\alpha_\chi(f)(s)=\chi(s)f(s),\qquad
 \mathcal F_+g(x)=\int_{\widehat G}g(\chi)\chi(x)\,d\chi.
 \tag{8.2}
\]
Pontryagin duality identifies \(x\in G\) with the character \(\chi\mapsto\chi(x)\). Denote the canonical multiplier maps for the iterated product by \(j_A,j_G,j_{\widehat G}\). They are multiplier maps, and are not generally maps into \(C\) itself.

## Two tensor-product facts

The tensor norm in a full universal construction is initially maximal. We give the two precise facts needed to pass to ordinary function algebras and compact operators.

**Lemma 8.1.** For any locally compact Hausdorff space \(Y\), pointwise multiplication identifies
\[
 A\otimes_{\max}C_0(Y)=A\otimes_{\min}C_0(Y)=C_0(Y,A).
 \tag{8.3}
\]
Also, for any nonzero Hilbert space \(H\),
\[
 A\otimes_{\max}\mathcal K(H)=A\otimes_{\min}\mathcal K(H).
 \tag{8.4}
\]

**Proof.** Suppose \(\pi\) and \(\rho\) are commuting nondegenerate representations of \(A\) and \(C_0(Y)\). On an algebraic tensor \(F(y)=\sum_i f_i(y)a_i\), their product representation is \(\sum_i\pi(a_i)\rho(f_i)\). Approximate the finite family \(f_i\) uniformly by a common finite partition of unity on a compact neighborhood of their essential supports. More explicitly, choose compactly supported nonnegative functions \(\psi_j\) with \(\sum_j\psi_j\le1\), points \(y_j\), and
\(\|f_i-\sum_j f_i(y_j)\psi_j\|_\infty<\varepsilon\). Such functions are obtained by covering the compact set where some \(|f_i|\ge\varepsilon/3\) by finitely many neighborhoods on which every \(f_i\) varies by less than \(\varepsilon/3\), and cutting off in their union. The error in the represented tensor is at most \(\varepsilon\sum_i\|a_i\|\).

Put \(b_j=F(y_j)\). The map \(V\xi=(\rho(\psi_j)^{1/2}\xi)_j\) is a contraction. Commutation gives
\[
 \sum_j\pi(b_j)\rho(\psi_j)
       =V^*\operatorname{diag}(\pi(b_j))V,
\]
so its norm is at most \(\max_j\|b_j\|\le\|F\|_\infty\). Let \(\varepsilon\downarrow0\). This bounds the maximal norm by the supremum norm. Evaluation at points, followed by a faithful representation of \(A\), gives the reverse bound; these are spatial representations, so the minimal norm has the same lower bound. Finite partitions of unity also approximate any compactly supported \(A\)-valued continuous function by algebraic tensors. Scalar cutoffs then give density in \(C_0(Y,A)\). Isometric images are closed, proving (8.3).

For (8.4), a nondegenerate representation of \(\mathcal K(H)\) is an amplification of its defining representation, by the matrix-unit proof in Lesson 7. After that unitary identification, an operator commuting with all its rank-one matrix units has the form \(1_H\otimes T\): the diagonal matrix units force it to preserve each coordinate, and the off-diagonal units make every coordinate operator identical. Thus every commuting representation of \(A\) is \(1_H\otimes\sigma\) on the multiplicity space. The resulting tensor representation is spatial and is bounded by the minimal norm. Taking the supremum gives (8.4); the reverse inequality always holds. ∎

**Lemma 8.2 (An inactive tensor factor).** If \(\beta\) is an action of a locally compact group \(L\) on a C*-algebra \(D\), then
\[
 (A\otimes_{\max}D)\rtimes_{\operatorname{id}\otimes\beta}L
       \cong A\otimes_{\max}(D\rtimes_\beta L).
 \tag{8.5}
\]
On dense elementary functions the map sends \(t\mapsto a\otimes f(t)\) to \(a\otimes f\).

**Proof.** A nondegenerate representation of the maximal tensor product consists of commuting nondegenerate coefficient representations \(\pi_A,\pi_D\). They are recovered even for nonunital algebras from the strict canonical multiplier maps; approximate identities in both factors show nondegeneracy of each. A covariant group representation \(U\) for \(\operatorname{id}\otimes\beta\) commutes with \(\pi_A\) and is covariant for \(\pi_D\). These assertions follow first on products \(\pi_A(a)\pi_D(d)\), and then for the separate multiplier maps by nondegeneracy. Hence \(\pi_D\rtimes U\) commutes with \(\pi_A\). Conversely a commuting pair consisting of \(\pi_A\) and a nondegenerate representation of \(D\rtimes L\) recovers precisely these coefficient and group representations. This is a bijection of the universal representation families.

The two integrated forms have the same value on every \(a\otimes f\). Consequently their universal norms agree on the dense span of such functions. This span is dense on the left by compact-support partitions of unity and the density of \(A\odot D\) in the coefficient algebra; it is dense on the right by the density of \(C_c(L,D)\). The isometry therefore extends to an onto C*-isomorphism. This also proves the indicated map preserves products and adjoints, since all its represented values do. ∎

The maximal tensor products in (8.5) are part of its statement. Replacing only the left tensor product by a minimal one is not justified for arbitrary \(A,D\); even \(L=\{e\}\) would require an additional equality of tensor norms. In our application both (8.3) and (8.4) supply that equality.

## The three steps

**Theorem 8.3 (Takai duality).** There is an isomorphism
\[
 \Theta:(A\rtimes_\alpha G)\rtimes_{\widehat\alpha}\widehat G
        \longrightarrow A\otimes_{\min}\mathcal K(L^2(G)).
 \tag{8.6}
\]
We choose the version for which the double dual action becomes
\(\alpha_t\otimes\operatorname{Ad}\lambda_t\), where
\((\lambda_t\xi)(x)=\xi(t^{-1}x)\).

**Proof.** First identify the covariant representations of the left side. By the two integrated-form correspondences of Lesson 1, they are triples \((\pi,U,V)\), with \(\pi\) a nondegenerate representation of \(A\), \(U\) a strongly continuous unitary representation of \(G\), \(V\) one of \(\widehat G\), and
\[
\begin{gathered}
 U_s\pi(a)U_s^*=\pi(\alpha_s(a)),\qquad
 V_\chi\pi(a)=\pi(a)V_\chi,\\
 V_\chi U_s V_\chi^*=\chi(s)U_s.
\end{gathered}
 \tag{8.7}
\]
Recovering these relations from the second crossed product is legitimate on strict multipliers: the dual action fixes \(j_A(a)\) and multiplies \(j_G(s)\) by \(\chi(s)\), as proved in Lesson 6. Conversely (8.7) makes \((\pi\rtimes U,V)\) covariant, first on compactly supported integrals and then by density.

The integrated representation of \(V\), followed by (8.2), is a nondegenerate representation \(\rho\) of \(C_0(G)\), with its strict multiplier value on \(x\mapsto\chi(x)\) equal to \(V_\chi\). The last relation in (8.7) says
\(U_sV_\chi U_s^*=\chi(s)^{-1}V_\chi\).
For \(g\in C_c(\widehat G)\), integration gives
\[
 U_s\rho(\mathcal F_+g)U_s^*
      =\rho\bigl((\mathcal F_+g)(s^{-1}\,\cdot\,)\bigr).
 \tag{8.8}
\]
Density proves covariance for every scalar function. Commutation with \(\pi\), and (8.3), give a coefficient representation of \(C_0(G,A)\), covariant for
\[
 (\gamma_sF)(x)=\alpha_s(F(s^{-1}x)).
 \tag{8.9}
\]
Conversely such a covariant representation recovers its commuting \(A\) and \(C_0(G)\) multiplier representations, the latter recovers \(V\), and its covariance yields (8.7). Thus the universal families coincide. On the dense double core \(F\in C_c(\widehat G\times G,A)\), the integrated operator is
\(\int_{\widehat G}\int_G\pi(F(\chi,s))U_sV_\chi\,ds\,d\chi\).
Reordering \(U_sV_\chi=\chi(s)^{-1}V_\chi U_s\) gives the coefficient function
\[
 (\Psi F)(s,x)=\int_{\widehat G}F(\chi,s)\chi(s^{-1}x)\,d\chi.
 \tag{8.10}
\]
It belongs to \(C_c(G,C_0(G,A))\), by the Fourier isomorphism and finite-product approximations on compact supports. In every corresponding pair of representations, \(F\) and \(\Psi F\) have the same integrated value, so their universal norms agree. Representations separate the target algebra, which also shows that \(\Psi\) preserves products and adjoints. Its range has dense span: Fourier transforms of \(C_c(\widehat G)\) are dense in \(C_0(G)\), scalar functions times elements of \(A\) are dense in \(C_0(G,A)\), and the coordinate change \((s,x)\mapsto(s,s^{-1}x)\) is an invertible isometry on \(C_c(G,C_0(G,A))\), preserving compact supports in \(s\). Thus \(\Psi\) extends to the first isomorphism \(C\cong C_0(G,A)\rtimes_\gamma G\).

For the second step define
\[
 (\Phi F)(x)=\alpha_x^{-1}(F(x)),\qquad
 (\Phi^{-1}F)(x)=\alpha_x(F(x)).
 \tag{8.11}
\]
These are pointwise *-isomorphisms, preserve the supremum norm, and preserve vanishing at infinity. Norm continuity follows from strong continuity of \(\alpha\) and continuity of \(F\). Moreover,
\[
 \Phi(\gamma_sF)(x)
  =\alpha_{x^{-1}s}(F(s^{-1}x))
  =(\Phi F)(s^{-1}x).
 \tag{8.12}
\]
Thus \(\Phi\) is equivariant from the diagonal action to ordinary left translation with inactive \(A\). The full universal property gives the second isomorphism, applying \(\Phi\) to each coefficient value in \(C_c(G,C_0(G,A))\).

The third step is
\[
\begin{aligned}
 C_0(G,A)\rtimes_{\operatorname{lt}}G
 &\cong A\otimes_{\max}(C_0(G)\rtimes_{\operatorname{lt}}G)\\
 &\cong A\otimes_{\min}\mathcal K(L^2(G)).
\end{aligned}
 \tag{8.13}
\]
Here (8.3), Lemma 8.2, the scalar translation theorem of Lesson 7, and (8.4) justify every tensor norm and completion. Equivalently this is the coefficient version (7.40) of that translation theorem. Its dense action on the Hilbert \(A\)-module \(L^2(G)\boxtimes A\) is multiplication by coefficient functions and left translation.

This composition already gives an isomorphism, which we temporarily call \(\Theta_0\). Finally conjugate its compact factor by the unitary inversion
\[
 (J\xi)(x)=\xi(x^{-1}),\qquad
 \Theta=(\operatorname{id}_A\otimes\operatorname{Ad}J)\Theta_0.
 \tag{8.14}
\]
Abelian groups are unimodular, so Haar inversion makes \(J\) unitary. This last choice fixes the double-dual convention in the statement, as the following computation proves. ∎

## The surviving action and the generator formulas

**Proposition 8.4.** Under \(\Theta\), the strict multiplier actions on \(L^2(G)\boxtimes A\) are
\[
\begin{aligned}
 (\Theta(j_A(a))\xi)(x)&=\alpha_x(a)\xi(x),\\
 (\Theta(j_G(s))\xi)(x)&=\xi(xs),\\
 (\Theta(j_{\widehat G}(\chi))\xi)(x)&=\overline{\chi(x)}\xi(x).
\end{aligned}
 \tag{8.15}
\]
The double dual action satisfies
\[
 \Theta\widehat{\widehat\alpha}_t\Theta^{-1}
       =\alpha_t\otimes\operatorname{Ad}\lambda_t.
 \tag{8.16}
\]
This action is exterior equivalent to \(\alpha\otimes\operatorname{id}\).

**Proof.** Before the final inversion, the first step sends \(j_A(a)\) to the constant coefficient multiplier, \(j_G(s)\) to the group unitary, and \(j_{\widehat G}(\chi)\) to multiplication by \(\chi(x)\). Twisting by (8.11) changes the first to \(\alpha_x^{-1}(a)\); the translation representation sends the group unitary to \(\lambda_s\). Conjugating by \(J\) changes these to the three formulas (8.15), since \(J\lambda_sJ=\lambda_{s^{-1}}\) and \(J M_\chi J=M_{\bar\chi}\).

The double dual action fixes \(j_A,j_G\) and sends \(j_{\widehat G}(\chi)\) to \(\chi(t)j_{\widehat G}(\chi)\). At the first step it therefore acts on the scalar function factor by \(f(x)\mapsto f(tx)\). After (8.11), it acts on coefficients by
\[
 F(x)\longmapsto\alpha_t(F(tx)),
 \tag{8.17}
\]
and fixes the translation group unitaries. On the compact-operator model before inversion this is \(\alpha_t\otimes\operatorname{Ad}\lambda_{t^{-1}}\). Conjugating by \(J\) gives (8.16).

One can check (8.16) directly in the final model without representing \(\alpha\) by inner automorphisms. Define the semilinear isometry on the Hilbert \(A\)-module
\[
 (Q_t\xi)(x)=\alpha_t(\xi(t^{-1}x)).
 \tag{8.18}
\]
It sends \(\xi a\) to \((Q_t\xi)\alpha_t(a)\), and sends the inner product to its \(\alpha_t\)-image. Thus it sends \(\theta_{\xi,\eta}\) to \(\theta_{Q_t\xi,Q_t\eta}\). On elementary vectors it is \(\lambda_t\otimes\alpha_t\), so its compact-operator action is \(\alpha_t\otimes\operatorname{Ad}\lambda_t\). Applied to (8.15), it fixes the first two multipliers and multiplies the third by \(\chi(t)\). The dense integrated products determine the action on the whole algebra. Strong continuity follows first on rank-one tensors and then by density.

For later naturality checks, the final map has an explicit kernel on the double core \(F\in C_c(\widehat G\times G,A)\):
\[
\begin{aligned}
 K_F(x,y)&=\int_{\widehat G}
       \alpha_x(F(\chi,x^{-1}y))\overline{\chi(y)}\,d\chi,\\
 (\Theta(F)\xi)(x)&=\int_G K_F(x,y)\xi(y)\,dy.
\end{aligned}
 \tag{8.19}
\]
Indeed, (8.15) sends the integrated product to
\(\int\int\alpha_x(F(\chi,s))\overline{\chi(xs)}\xi(xs)ds\,d\chi\); set \(y=xs\). For compactly supported \(\xi\), Fubini is justified by the compact supports in the original integration variables. The compactness and C*-norm assertion for this operator follow from the three established isomorphisms; a Fourier-transformed kernel need not have compact support. Formula (8.19) also shows that the isomorphism commutes with equivariant coefficient homomorphisms on the dense core, in particular with invariant-ideal inclusions and quotients.

Finally set \(\eta_t=\alpha_t\otimes\operatorname{id}\) and
\[
 w_t=1_{M(A)}\otimes\lambda_t
       \in\mathcal U(M(A\otimes\mathcal K(L^2(G)))).
 \tag{8.20}
\]
These multipliers are strictly continuous: on finite sums of \(a\otimes\theta_{\xi,\zeta}\), continuity on the left uses strong continuity of \(\lambda_t\xi\), and on the right uses strong continuity of \(\lambda_t^*\zeta\). Density proves both strict seminorm limits on all compact tensors. Since \(\eta_s\) fixes \(w_t\),
\(w_{st}=w_s\eta_s(w_t)\). Moreover
\(\alpha_t\otimes\operatorname{Ad}\lambda_t=\operatorname{Ad}w_t\circ\eta_t\).
This is exactly exterior equivalence, with a strictly continuous unitary cocycle. ∎

## The invariant-ideal correspondence

We need the compact-ideal prerequisite and a crossed-product recovery fact to prove the converse promised in Lesson 6.

**Lemma 8.5 (Ideals in a compact amplification).** For nonzero \(H\), every closed two-sided ideal \(L\subseteq A\otimes\mathcal K(H)\) is \(I\otimes\mathcal K(H)\) for a unique closed two-sided ideal \(I\subseteq A\).

**Proof.** Choose an orthonormal basis and its matrix units \(e_{ij}\), fixing one index \(o\). Define
\[
 I=\{a\in A:a\otimes e_{oo}\in L\}.
 \tag{8.21}
\]
The finite-matrix ideal result in The Rieffel correspondence and induced representations, Example 5.1 supplies the coefficient recovery, including preservation of ideals by multiplier matrix units. Example 5.3 proves the stabilization statement when \(H\) is separable. We extend its compression argument to arbitrary nonzero \(H\).

Direct the finite subsets \(F\) of the chosen basis that contain \(o\) by inclusion, and let \(P_F\) be their orthogonal projections. Example 5.1 identifies each compressed ideal
\((1\otimes P_F)L(1\otimes P_F)\) with \(M_F(I)\), using the same corner (8.21). For every \(l\in A\otimes\mathcal K(H)\),
\((1\otimes P_F)l(1\otimes P_F)\to l\) in norm. Indeed \(P_F\) converges strongly to \(1\); on a rank-one operator this gives norm convergence of both compressed vectors. Finite-rank approximation proves the assertion for compact operators, and finite tensor approximation proves it for \(l\). Thus every element of \(L\) is a norm limit of elements of \(I\otimes\mathcal K(H)\). Conversely Example 5.1 puts every \(a\otimes e_{ij}\), \(a\in I\), in \(L\); their closed span is \(I\otimes\mathcal K(H)\), by the same compression argument. Formula (8.21) gives uniqueness and proves that inclusion is both preserved and reflected. This uses a net of finite subsets, rather than a countable sequence of projections. ∎

**Lemma 8.6 (Full crossed products reflect ideal inclusion).** For an action of a locally compact group \(L\) on \(D\), and invariant ideals \(I_1,I_2\subseteq D\),
\[
 I_1\rtimes L\subseteq I_2\rtimes L
       \quad\Longrightarrow\quad I_1\subseteq I_2.
 \tag{8.22}
\]

**Proof.** By full ideal exactness from Lesson 1, quotienting by \(I_2\rtimes L\) gives \((D/I_2)\rtimes L\). For \(d\in I_1\) and \(g\in C_c(L)\), the function \(s\mapsto g(s)d\) maps to zero. Its image is the product of the faithful canonical coefficient multiplier \(i_{D/I_2}(d+I_2)\) with the integrated group multiplier \(i_L(g)\). The latter representation of \(C^*(L)\) is nondegenerate, as in Lesson 1. An approximate identity in \(C^*(L)\) therefore converges strictly to the identity after applying this multiplier representation. Since the product with every \(i_L(g)\) is zero, density and this strict limit give \(i_{D/I_2}(d+I_2)=0\). Faithfulness gives \(d\in I_2\). This proof recovers coefficient multipliers and does not require them to be elements of the crossed product. ∎

**Theorem 8.7.** The map
\[
 I\longmapsto I\rtimes_\alpha G
 \tag{8.23}
\]
is an inclusion-preserving bijection from the \(\alpha\)-invariant closed ideals of \(A\) to the \(\widehat\alpha\)-invariant closed ideals of \(B=A\rtimes_\alpha G\).

**Proof.** The forward assertion is Lesson 6: full ideal embedding identifies \(I\rtimes G\) with an ideal, and character multiplication preserves its dense core. For the converse take a dual-invariant ideal \(J\subseteq B\). The full ideal
\(J\rtimes\widehat G\subseteq C\) is invariant under the double dual action, since that action multiplies its compactly supported coefficient function at \(\chi\) by \(\chi(t)\). By Lemma 8.5 there is a unique \(I\subseteq A\) with
\[
 \Theta(J\rtimes\widehat G)=I\otimes\mathcal K(L^2(G)).
 \tag{8.24}
\]
By (8.16), this ideal is carried to \(\alpha_t(I)\otimes\mathcal K(L^2(G))\). Inner conjugation on the compact factor preserves every ideal of this form. Uniqueness in Lemma 8.5 therefore gives \(\alpha_t(I)=I\).

Apply Takai duality to the system \((I,G,\alpha|_I)\). Its isomorphism is the restriction of \(\Theta\): the constructions commute with the actual dense coefficient maps, or directly with the kernel (8.19). The two full ideal embeddings from Lesson 1 then give
\[
 \Theta((I\rtimes G)\rtimes\widehat G)
       =I\otimes\mathcal K(L^2(G)).
 \tag{8.25}
\]
Thus \(J\rtimes\widehat G=(I\rtimes G)\rtimes\widehat G\). Apply Lemma 8.6 to the \(\widehat G\)-action on \(B\) to obtain \(J=I\rtimes G\). Lemma 8.6 also proves injectivity of (8.23). The forward map preserves inclusion by its compactly supported cores, and the inverse preserves inclusion by (8.24) and Lemma 8.5. ∎

In particular, this is an order isomorphism of the invariant-ideal lattices, so it preserves intersections and closed joins. It concerns dual-invariant ideals, rather than asserting that every ideal of \(B\) is dual invariant.

## Finite groups, integer and circle actions, and stability

For \(G=\mathbb Z_2\), write \(\alpha\) for the involutive automorphism. In the two coordinates \(0,1\), (8.15) gives
\[
\begin{aligned}
 j_A(a)&\longmapsto\begin{pmatrix}a&0\\0&\alpha(a)\end{pmatrix},\\
 j_G(1)&\longmapsto S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 j_{\widehat G}(-1)\longmapsto D=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\end{aligned}
 \tag{8.26}
\]
The entries \(1\) belong to \(M(A)\) when necessary. The two group unitaries anticommute, \(DSD=-S\), exactly as (8.7) requires. The target is \(M_2(A)\), with double dual action \(\alpha\otimes\operatorname{Ad}S\).

For an automorphism \(\alpha\) and \(G=\mathbb Z\), the theorem is
\[
 (A\rtimes_\alpha\mathbb Z)\rtimes_{\widehat\alpha}\mathbb T
       \cong A\otimes\mathcal K(\ell^2(\mathbb Z)).
 \tag{8.27}
\]
In (8.15), \(j_A(a)\) has diagonal entries \(\alpha^n(a)\), the integer unitary sends \(\xi(n)\) to \(\xi(n+k)\), and \(j_{\mathbb T}(z)\) multiplies the \(n\)-th coordinate by \(z^{-n}\). Let \(P_n=\int_{\mathbb T}z^n j_{\mathbb T}(z)dz\), with normalized Haar measure. Character orthogonality makes it the coordinate projection. Then
\[
 j_A(\alpha^{-m}(a))P_mj_{\mathbb Z}(n-m)P_n
       \longmapsto a\otimes e_{mn}.
 \tag{8.28}
\]
Although \(P_n\) can be only a multiplier for nonunital coefficients, the displayed product is in the double crossed product: \(j_A(a)\) belongs to the first crossed product for discrete \(G\), and its product with the integrated second group multiplier is an actual compactly supported crossed-product integral. These formulas exhibit the finite matrix corners directly.

For a circle action,
\[
 (A\rtimes_\alpha\mathbb T)\rtimes_{\widehat\alpha}\mathbb Z
       \cong A\otimes\mathcal K(L^2(\mathbb T)).
 \tag{8.29}
\]
Using the basis \(e_n(z)=z^n\) identifies the compact factor with \(\mathcal K(\ell^2(\mathbb Z))\). Left translation sends \(e_n\) to \(t^{-n}e_n\), so the surviving circle action is
\(\alpha_t\otimes\operatorname{Ad}\operatorname{diag}(t^{-n})\).
This is the double crossed-product statement used, for example, with gauge actions; no additional assertion about a particular algebra is needed for it.

For a real action and the character \(\chi_u(x)=e^{2\pi iux}\), the canonical operators in (8.15) are
\[
\begin{aligned}
 j_A(a)\xi(x)&=\alpha_x(a)\xi(x),\\
 j_{\mathbb R}(s)\xi(x)&=\xi(x+s),\\
 j_{\widehat{\mathbb R}}(u)\xi(x)&=e^{-2\pi iux}\xi(x).
\end{aligned}
 \tag{8.30}
\]
The double crossed product is \(A\otimes\mathcal K(L^2(\mathbb R))\), and its double dual action is \(\alpha_s\otimes\operatorname{Ad}\lambda_s\). The opposing translation signs in (8.30) and in the surviving \(\lambda_s\) follow from the inversion choice (8.14).

**Proposition 8.8 (When the double product is stable).** If \(G\) is infinite, then \(C\) is stable, meaning \(C\otimes\mathcal K(\ell^2(\mathbb N))\cong C\). For a finite group of order \(n\), the conclusion of Takai duality is \(C\cong M_n(A)\); stability does not follow in general.

**Proof.** For every positive integer \(m\), an infinite locally compact Hausdorff group has \(m\) pairwise disjoint relatively compact nonempty open sets. Their indicators have finite positive Haar norm and are pairwise orthogonal. Thus \(L^2(G)\) is infinite-dimensional. Any infinite Hilbert basis has the same cardinality after product with \(\mathbb N\), so \(L^2(G)\otimes\ell^2(\mathbb N)\cong L^2(G)\), without a separability assumption. The compact-operator tensor theorem, or its rank-one formula in the Hilbert-module prerequisite used in Lesson 7, gives
\(\mathcal K(H)\otimes\mathcal K(\ell^2)\cong\mathcal K(H\otimes\ell^2)\).
Together with (8.6) and associativity of the minimal tensor product this proves stability. For finite \(G\), its \(L^2\) space has dimension \(n\). Taking \(A=\mathbb C\) gives the nonzero unital algebra \(M_n(\mathbb C)\), which cannot be stable: its tensor product with the infinite compact algebra has no identity. ∎

For every \(G\), finite or infinite, (8.6) gives a Morita equivalence between \(C\) and \(A\), using the full module \(L^2(G)\boxtimes A\) of Lesson 7. This is the ordinary-action consequence corresponding to the Morita form in [Green 1978, Corollary 31, p. 236]. That paper also treats twisted covariance algebras; no twisted extension is claimed here. Since both \(G\) and \(\widehat G\) are amenable, Lesson 4 identifies the full and reduced crossed products at both steps, so the same Takai isomorphism also holds for the iterated reduced product.

## Exercises with solutions

**Exercise 1 (A flip in two-by-two matrices).** Let \(A=\mathbb C\oplus\mathbb C\), and let \(\mathbb Z_2\) exchange its two coordinates. Describe both crossed products, the Takai generators, and the double dual action explicitly.

**Solution.** In the first crossed product, represent \((a,b)\) by \(\operatorname{diag}(a,b)\) and the group generator by \(S\). These give all four matrix units, so the image is \(M_2(\mathbb C)\). The crossed-product vector space is the four-dimensional span of \(A\) and \(Au\), with faithful coefficient map and independent group coefficients (Lesson 3). The onto map to \(M_2(\mathbb C)\) is therefore injective. The dual action fixes the diagonal and sends \(S\) to \(-S\), hence is \(\operatorname{Ad}D\).

In the double product let \(v\) be the second involutive unitary. It commutes with \(D\), and \(v b v=DbD\) for \(b\in M_2(\mathbb C)\). Thus \(z=Dv\) is a central self-adjoint unitary, and \(v=Dz\). Conversely any commuting representation of \(M_2(\mathbb C)\) and such a \(z\) defines \(v\) with these relations. The universal property identifies the double product with
\(M_2(\mathbb C)\otimes C^*(\mathbb Z_2)\cong M_2(\mathbb C)\oplus M_2(\mathbb C)\).

The version \(\Theta\) in (8.15) is
\[
\begin{aligned}
 (a,b)&\longmapsto
   \bigl(\operatorname{diag}(a,b),\operatorname{diag}(b,a)\bigr),\\
 u&\longmapsto(S,S),\qquad v\longmapsto(D,D).
\end{aligned}
 \tag{8.31}
\]
Here the copy of \(D\) from the first crossed product maps to \((D,-D)\), so \(z=Dv\) maps to \((1,-1)\). Its central projections split the two full matrix blocks, confirming surjectivity directly. The double dual action fixes the first crossed product and negates \(v\), so on the target it is
\[
 (X,Y)\longmapsto(SYS,SXS).
 \tag{8.32}
\]
This is precisely the flip on \(A\) together with conjugation by \(S\) on the compact factor. ∎

**Exercise 2 (Removing the diagonal action).** Verify the equivariance of (8.11), including continuity and vanishing at infinity. Track the double dual translation through this change of coordinates.

**Solution.** The function \(x\mapsto\alpha_x^{-1}(F(x))\) is continuous: near a fixed \(x_0\), its difference from \(\alpha_{x_0}^{-1}(F(x_0))\) is bounded by
\(\|F(x)-F(x_0)\|+\|\alpha_x^{-1}(F(x_0))-\alpha_{x_0}^{-1}(F(x_0))\|\).
Both terms tend to zero. Its norm at \(x\) is \(\|F(x)\|\), so it vanishes at infinity. The inverse has the analogous properties, and both maps preserve pointwise multiplication and star. For diagonal covariance,
\(\alpha_x^{-1}\alpha_s(F(s^{-1}x))
 =\alpha_{(s^{-1}x)^{-1}}(F(s^{-1}x))\), which is exactly the left translation of \(\Phi F\).

Before this change, the double dual action is \(R_tF(x)=F(tx)\). Hence
\[
 (\Phi R_t\Phi^{-1}K)(x)
       =\alpha_x^{-1}(\alpha_{tx}(K(tx)))=\alpha_t(K(tx)).
 \tag{8.33}
\]
The right-translation factor becomes \(\operatorname{Ad}\lambda_{t^{-1}}\) under the translation compact model. Inversion (8.14) carries that to \(\operatorname{Ad}\lambda_t\). The coefficient action remains \(\alpha_t\). ∎

**Exercise 3 (The tensor norm in a full crossed product).** Prove (8.5) for arbitrary, possibly nonunital \(A,D\). Explain exactly why the tensor norms can be minimal in step three of Takai duality.

**Solution.** A covariant representation of \(A\otimes_{\max}D\) for the action trivial on \(A\) recovers commuting nondegenerate \(\pi_A,\pi_D\) and a group representation \(U\). Covariance extends to the strict multiplier representations, so \(U\) commutes with \(\pi_A\), and \((\pi_D,U)\) is covariant for \(\beta\). Integrating gives a commuting pair \(\pi_A,\pi_D\rtimes U\), hence a representation of \(A\otimes_{\max}(D\rtimes L)\). Conversely every nondegenerate representation of that maximal tensor product recovers exactly such a commuting pair; the integrated-form correspondence then recovers \(\pi_D,U\). These operations are inverse and preserve \(a\otimes f\) on the dense compactly supported tensor core. Universal norm suprema agree there, proving the completed isomorphism. This is the representation proof of Lemma 8.2, and accounts for the nonunital multiplier step.

In Takai's third step \(D=C_0(G)\). Lemma 8.1 first identifies its maximal tensor product with the coefficient function algebra, while the translation theorem gives \(D\rtimes G=\mathcal K(L^2(G))\). The second part of Lemma 8.1 makes the final maximal tensor norm equal to the minimal norm. For general \(D\), the maximal notation in (8.5) must be retained unless an additional equality of tensor norms is established. ∎

**Exercise 4 (Double dual equivariance and its cocycle).** Starting from (8.15), identify the double dual action and prove its exterior equivalence to \(\alpha\otimes\operatorname{id}\), with the required continuity of the cocycle.

**Solution.** The action \(\delta_t=\alpha_t\otimes\operatorname{Ad}\lambda_t\) fixes the first multiplier in (8.15), because its coefficient at \(x\) becomes
\(\alpha_t(\alpha_{t^{-1}x}(a))=\alpha_x(a)\).
It fixes the second because translations commute in an abelian group. For the third,
\(\overline{\chi(t^{-1}x)}=\chi(t)\overline{\chi(x)}\), so it multiplies that generator by \(\chi(t)\). These are exactly the double dual multiplier relations. The compactly supported integrated products are dense, hence the actions coincide on the whole algebra.

Set \(w_t=1\otimes\lambda_t\) and \(\eta_t=\alpha_t\otimes\operatorname{id}\). Then
\(w_{st}=w_s\eta_s(w_t)\) because \(\eta_s\) fixes the second-factor unitary, and
\(\delta_t=\operatorname{Ad}w_t\circ\eta_t\).
For a rank-one tensor \(a\otimes\theta_{\xi,\zeta}\), the left strict difference has norm at most
\(\|a\|\|(\lambda_t-\lambda_s)\xi\|\|\zeta\|\), and the right strict difference has norm at most
\(\|a\|\|\xi\|\|(\lambda_t^*-\lambda_s^*)\zeta\|\).
Strong continuity of translation makes both tend to zero. Finite sums and norm approximation establish strict continuity on every algebra element. This proves the cocycle assertion without requiring operator-norm continuity of the translation unitaries. ∎

## What this lesson does not prove

The finite-matrix and separable stabilization ideal facts are prerequisites from The Rieffel correspondence and induced representations, Examples 5.1 and 5.3. Lemma 8.5 adds the finite-subset net needed for an arbitrary Hilbert space. Lemmas 8.6 and Theorem 8.7 retain the crossed-product recovery argument and the Takai-specific invariant-ideal converse.

We use the full integrated-form correspondence, strict canonical multipliers and full ideal exactness from Lesson 1; amenability and full/reduced equality from Lesson 4; and the positive C*-Fourier isomorphism, Pontryagin identification and dual action from Lesson 6. The translation compact-operator theorem and classification of representations of compact operators are proved in Lesson 7. General existence of Haar measure, compact-support partitions of unity, Hilbert tensor products, minimal tensor-product associativity and ordinary C*-algebra functional calculus are foundational prerequisites. The compact tensor formula used in the stability argument is the exterior compact-algebra theorem Tensor products and C*-correspondences, Theorem 5.1, also used precisely in Lesson 7. This lesson proves both tensor-norm identifications needed here, the inactive-factor crossed-product identity, all three Takai steps, its explicit surviving action and cocycle, and the invariant-ideal converse. No Takai or invariant-ideal theorem is imported in place of these proofs.

[Blackadar 2006] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Theorem II.10.5.2 and Theorem II.10.5.4, p. 226. These are the duality and invariant-ideal statement locators. [Author's revised edition, 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).

[Williams] D. P. Williams, *Crossed Products of C*-Algebras*, §7.1, Theorem 7.1 and Lemmas 7.2–7.6, pp. 190–197. [Author's draft, version 3.1](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf). That formulation ends with right regular translation; the inversion in (8.14) gives our left regular formulation.

[Connes 1994] A. Connes, *Noncommutative Geometry*, Chapter II, Appendix C, Definition 5 and Theorem 6, p. 178. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). It states the double dual action up to exterior equivalence, called outer equivalence there. The explicit cocycle is proved in (8.20).

[Green 1978] P. Green, *The local structure of twisted covariance algebras*, Acta Mathematica 140 (1978), 191–250, §7, Corollary 31 and its following remark, p. 236. The ordinary-action Morita consequence above is a specialization of the stronger twisted context in that paper.

[Blackadar 1998] B. Blackadar, *K-Theory for Operator Algebras*, second edition, Theorem 10.1.2, p. 72. It distinguishes infinite-group stability from finite matrix amplification. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

The Rieffel correspondence and induced representations Hilbert C*-modules and Morita equivalence, Lesson 12, Examples 5.1 and 5.3. The former proves finite-matrix coefficient recovery for nonunital algebras; the latter gives the separable compact-amplification ideal correspondence.
