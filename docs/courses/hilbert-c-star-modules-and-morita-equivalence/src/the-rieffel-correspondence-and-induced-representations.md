# The Rieffel correspondence and induced representations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An imprimitivity module connects more than two coefficient algebras. It transports their closed ideals and their nondegenerate representations. The same inner products that recover the algebras from the module also recover ideals from submodules and representations from tensor products. This is the Rieffel correspondence.

We prove the ideal correspondence, the equivalence of representation categories and the resulting homeomorphism of primitive ideal spaces. Matrix algebras, stabilization and full corners make the maps concrete. A finite-group calculation then explains how the module construction contains classical induction and why a system of imprimitivity includes additional operators beyond the group representation. Finally, local vector modules and their overlap lines give the continuous-trace gluing class and its classification over a fixed spectrum.

Fix an \(A\)-\(B\) imprimitivity bimodule \(X\). Right inner products are conjugate linear first; left inner products are linear first. Ideals are norm-closed two-sided ideals. Representations on Hilbert spaces are nondegenerate, and irreducible representations act on nonzero spaces. No separability or countability assumption is needed for the first six sections.

## 1. An ideal determines a closed submodule

For an ideal \(I\subseteq B\), write
\[
XI=\overline{\operatorname{span}}\{xi:x\in X,\ i\in I\}.
\tag{1.1}
\]
The closed-span convention matters: an algebraic collection of finite products need not already be complete.

**Lemma 1.1.** We have
\[
XI=\{x\in X:\langle x,x\rangle_B\in I\}.
\tag{1.2}
\]
It is a closed right \(B\)-submodule invariant under the left \(A\)-action. Every \(I\)-approximate identity \((e_\lambda)\) satisfies \(xe_\lambda\to x\) for \(x\in XI\).

*Proof.* A finite sum of products from (1.1) has all its inner-product coefficients in \(I\). Continuity proves one inclusion in (1.2). Conversely, if \(c=\langle x,x\rangle_B\in I\), choose a positive contractive approximate identity of \(I\). Computing in a unitization gives
\[
\begin{gathered}
\|x-xe_\lambda\|^2\\
=\|(1-e_\lambda)c(1-e_\lambda)\|
\longrightarrow0.
\end{gathered}
\tag{1.3}
\]
Thus \(x\in XI\). Formula (1.3) also proves the last assertion. Closedness follows from continuity of \(x\mapsto\langle x,x\rangle_B\). Right invariance and left invariance follow directly from (1.1), the ideal property of \(I\), the commuting actions and their boundedness. ∎

Define the corresponding subspace of \(A\) by
\[
\mathcal R_X(I)
=\overline{\operatorname{span}}{}_A\langle XI,X\rangle.
\tag{1.4}
\]
We will usually write \(\mathcal R(I)\).

**Lemma 1.2.** The space \(J=\mathcal R(I)\) is an ideal of \(A\), and
\[
\begin{aligned}
\overline{JX}&=XI,\\
J&=\{a\in A:aX\subseteq XI\}.
\end{aligned}
\tag{1.5}
\]
Here and below a bar over a product space includes linear span.

*Proof.* Left multiplication preserves the generators in (1.4). Taking adjoints also preserves their closed span: for a generator approximated by \({}_A\langle xi,y\rangle\), its adjoint is
\({}_A\langle y,xi\rangle={}_A\langle yi^*,x\rangle\), whose first vector lies in \(XI\). Thus the span is a self-adjoint left ideal and hence a two-sided ideal.

Compatibility gives
\({}_A\langle u,y\rangle z=u\langle y,z\rangle_B\), so \(JX\subseteq XI\). For the reverse inclusion, the closed span of \(\langle X,X\rangle_B\) is \(B\). Approximate an approximate identity of \(B\) by finite sums of these coefficients. For \(xi\in XI\), this approximates \(xi\) by vectors
\[
xi\langle y,z\rangle_B
={}_A\langle xi,y\rangle z\in JX.
\tag{1.6}
\]
Taking closures proves the first equality in (1.5).

Certainly \(J\) is contained in the second set in (1.5). If \(aX\subseteq XI\), then
\(a\,{}_A\langle x,y\rangle={}_A\langle ax,y\rangle\in J\). Left fullness gives \(aA\subseteq J\), and an approximate identity of \(A\) gives \(a\in J\). ∎

## 2. The ideal lattice and its inverse

For an ideal \(J\subseteq A\), define
\[
\mathcal S_X(J)
=\overline{\operatorname{span}}\langle X,JX\rangle_B.
\tag{2.1}
\]
This is precisely the construction (1.4) applied to the conjugate \(B\)-\(A\) module \(X^*\).

**Theorem 2.1 (Rieffel correspondence).** The maps \(\mathcal R_X\) and \(\mathcal S_X\) are mutually inverse order isomorphisms between the closed ideal lattices of \(B\) and \(A\). Consequently they preserve arbitrary intersections and closed sums.

*Proof.* Lemma 1.2 applied to \(X^*\) shows that (2.1) is an ideal. Both constructions are order preserving by their definitions. For \(J=\mathcal R(I)\), equation (1.5) gives
\[
\mathcal S(J)
=\overline{\operatorname{span}}\langle X,XI\rangle_B
=I.
\tag{2.2}
\]
The first inclusion in the last equality uses
\(\langle x,yi\rangle_B=\langle x,y\rangle_Bi\). The reverse inclusion uses right fullness: the span of these products is dense in \(BI=I\). Interchanging \(A,B\) and using \(X^*\) proves \(\mathcal R(\mathcal S(J))=J\). This proves bijectivity and its order-preserving inverse. An intersection is characterized as the greatest lower bound, and a closed sum as the least upper bound; an order isomorphism preserves these characterizations. ∎

**Proposition 2.2 (Restriction and quotient).** If \(J=\mathcal R(I)\), then \(XI\) is a \(J\)-\(I\) imprimitivity module. The quotient \(X/XI\) is an \((A/J)\)-\((B/I)\) imprimitivity module, with the quotient actions and inner products.

*Proof.* The inner products of \(XI\) lie in \(J,I\). They are full there. For left fullness, if \(u\in XI\), Lemma 1.1 and the cross-adjoint identity give
\[
\begin{aligned}
{}_A\langle u,y\rangle
&=\lim_\lambda{}_A\langle ue_\lambda,y\rangle\\
&=\lim_\lambda{}_A\langle u,ye_\lambda\rangle.
\end{aligned}
\tag{2.3}
\]
Both vectors in the final product lie in \(XI\), and these generators span \(J\). On the right, (2.2) gives coefficients spanning \(I\); multiplying the first vector by the same approximate identity places it in \(XI\) and approximates each coefficient because it belongs to \(I\). Norm equality, completeness and compatibility are inherited from \(X\).

For the quotient, set
\[
\begin{aligned}
\langle[x],[y]\rangle_{B/I}
 &=\langle x,y\rangle_B+I,\\
{}_{A/J}\langle[x],[y]\rangle
 &={}_A\langle x,y\rangle+J.
\end{aligned}
\tag{2.4}
\]
The coefficient inclusions already proved make both formulas independent of representatives. Lemma 1.1 shows that the right seminorm has null space exactly \(XI\).

This is also the Banach quotient norm. Indeed, for \(c=\langle x,x\rangle_B\), computed in a unitization,
\[
\begin{gathered}
\lim_\lambda\|(1-e_\lambda)c(1-e_\lambda)\|\\
=\|c+I\|.
\end{gathered}
\tag{2.5}
\]
The quotient map gives the lower bound. For any \(i\in I\), the left side has upper limit at most \(\|c+i\|\), since \((1-e_\lambda)i(1-e_\lambda)\to0\); take the infimum over \(i\). Now \(xe_\lambda\in XI\) and (1.3) give the upper bound for the distance from \(x\) to \(XI\). Conversely every representative has squared norm at least \(\|c+I\|\), by the quotient inner product. Hence the norms agree and the Hilbert quotient is complete. Applying the same argument on the left, using \(\overline{JX}=XI\), gives the identical Banach quotient norm for its left structure. Both products are full because the original products are full, and compatibility descends from \(X\). ∎

## 3. Inducing representations and intertwiners

Let \(\pi:B\to\mathcal B(H)\) be nondegenerate. The interior tensor product
\[
H_X=X\otimes_\pi H
\tag{3.1}
\]
is a Hilbert space, with elementary inner product
\[
\begin{gathered}
\langle x\otimes h,y\otimes k\rangle\\
=\langle h,\pi(\langle x,y\rangle_B)k\rangle_H.
\end{gathered}
\tag{3.2}
\]
Tensor completion includes division by the null space. The induced representation is
\[
(\operatorname{Ind}_X\pi)(a)(x\otimes h)
=ax\otimes h.
\tag{3.3}
\]
The interior tensor theorem makes this a bounded *-representation. It is nondegenerate: an approximate identity of \(A\) sends \(x\) to itself in norm and hence sends every elementary tensor to itself. Uniform boundedness extends this to all of \(H_X\).

If \(T:H\to K\) intertwines \(\pi\) and \(\rho\), define
\[
\operatorname{Ind}_X(T)=1_X\otimes T.
\tag{3.4}
\]
It is well-defined and bounded with norm at most \(\|T\|\), and its adjoint is \(1_X\otimes T^*\). Here is a way to check boundedness without manipulating tensor presentations. On \(H\oplus K\), the adjointable off-diagonal operator
\(S(h,k)=(T^*k,Th)\) commutes with the representation \(\pi\oplus\rho\), since both \(T\) and \(T^*\) intertwine. The second-factor tensor theorem [*Tensor products and C*-correspondences*, Proposition 2.2] gives \(1_X\otimes S\) with norm at most \(\|S\|=\|T\|\). Its off-diagonal component is (3.4), with the claimed adjoint. Tensoring preserves identities, compositions and adjoints on elementary tensors and therefore on the completions.

**Theorem 3.1 (Equivalence of representations).** The functor \(\operatorname{Ind}_X\) is an equivalence from nondegenerate representations of \(B\), with bounded intertwiners, to nondegenerate representations of \(A\). Its inverse is \(\operatorname{Ind}_{X^*}\). It induces isometric bijections on intertwiner spaces, preserving adjoints. In particular it preserves and reflects unitary equivalence and irreducibility.

*Proof.* Associativity, inverse evaluation and the tensor unit give a unitary
\[
\begin{aligned}
V_\pi:X^*\otimes_A(X\otimes_\pi H)&\longrightarrow H,\\
\overline x\otimes y\otimes h
 &\longmapsto\pi(\langle x,y\rangle_B)h.
\end{aligned}
\tag{3.5}
\]
The last unitary is \(B\otimes_\pi H\to H\), \(b\otimes h\mapsto\pi(b)h\); nondegeneracy makes its range dense and inner-product preservation makes it closed. The same construction on the other side gives
\[
\begin{aligned}
W_\sigma:X\otimes_B(X^*\otimes_\sigma K)&\longrightarrow K,\\
x\otimes\overline y\otimes k
 &\longmapsto\sigma({}_A\langle x,y\rangle)k.
\end{aligned}
\tag{3.6}
\]
Both maps intertwine the coefficient representations. They are natural in bounded intertwiners: apply an intertwiner to the final vector in (3.5) or (3.6) and use its coefficient relation.

For completeness, these inverse maps recover every intertwiner, not just every object. Write \(F=\operatorname{Ind}_X\) and \(G=\operatorname{Ind}_{X^*}\). On an elementary tensor \(q=x\otimes\overline y\otimes z\otimes h\), compatibility gives the identity
\[
\begin{aligned}
F(V_\pi)q
 &=x\otimes\pi(\langle y,z\rangle_B)h\\
 &={}_A\langle x,y\rangle z\otimes h\\
 &=W_{F\pi}q.
\end{aligned}
\tag{3.7}
\]
Thus \(F(V_\pi)=W_{F\pi}\). Given an intertwiner \(S:F\pi\to F\rho\), define
\[
T=V_\rho\,G(S)\,V_\pi^*.
\tag{3.8}
\]
It intertwines \(\pi,\rho\). Naturality of \(W\) and (3.7) show \(F(T)=S\). Naturality of \(V\) also shows that (3.8) recovers the original \(T\) when \(S=F(T)\). This proves full faithfulness. The contraction bound for each tensor functor and (3.8) give
\(\|F(T)\|\leq\|T\|\leq\|F(T)\|\), hence isometry.

In particular, the commutant of \(\pi(B)\) is isomorphic as a unital *-algebra to the commutant of \((F\pi)(A)\). A closed invariant subspace of a *-representation is reducing; its orthogonal projection belongs to the commutant. Irreducibility means that this commutant has no projections other than zero and the identity. The isomorphism preserves and reflects these projections, proving irreducibility preservation. It likewise preserves and reflects unitary intertwiners, proving the unitary-equivalence assertion. ∎

This is the representation correspondence described in [Blackadar 2006, II.7.6.14]. It does not assert equality of the dimensions of the two representation spaces.

## 4. Kernels and primitive ideal spaces

**Proposition 4.1.** For every nondegenerate representation \(\pi\),
\[
\ker(\operatorname{Ind}_X\pi)
=\mathcal R_X(\ker\pi).
\tag{4.1}
\]

*Proof.* Put \(I=\ker\pi\). If \(a\) acts as zero on the induced space, then for every \(x,h\),
\[
0=\|ax\otimes h\|^2
=\langle h,\pi(\langle ax,ax\rangle_B)h\rangle.
\tag{4.2}
\]
The middle operator is positive, so testing all \(h\) makes it zero. Lemma 1.1 gives \(ax\in XI\), and Lemma 1.2 gives \(a\in\mathcal R(I)\). Conversely that membership gives \(ax\in XI\) for every \(x\), so (4.2) vanishes. Thus \(a\) kills every elementary tensor and hence the induced space. ∎

The primitive ideal space \(\operatorname{Prim}(B)\) consists of kernels of irreducible representations. Its hull-kernel topology has closed sets
\[
\operatorname{hull}_B(I)
=\{P\in\operatorname{Prim}(B):I\subseteq P\}.
\tag{4.3}
\]

**Theorem 4.2.** The map
\[
\begin{aligned}
\Phi_X:\operatorname{Prim}(B)&\longrightarrow\operatorname{Prim}(A),\\
P&\longmapsto\mathcal R_X(P)
\end{aligned}
\tag{4.4}
\]
is a homeomorphism.

*Proof.* Theorems 3.1 and Proposition 4.1 show that it sends a primitive ideal to a primitive ideal, and that induction through \(X^*\) gives its inverse. Order preservation and reflection give
\[
\Phi_X^{-1}\bigl(\operatorname{hull}_A(\mathcal R(I))\bigr)
=\operatorname{hull}_B(I).
\tag{4.5}
\]
Every ideal of \(A\) equals \(\mathcal R(I)\) for some \(I\), so (4.5) proves continuity. The identical argument for the inverse proves a homeomorphism. ∎

The homeomorphism concerns primitive kernels even when distinct irreducible representations have the same kernel. The stronger statement about unitary equivalence classes comes from the representation functor, not from identifying a representation with its kernel.

## 5. Matrix ideals, corners and stabilization

**Example 5.1 (Matrices).** Every ideal of \(M_n(B)\) is exactly \(M_n(I)\) for a unique ideal \(I\subseteq B\). The equivalence module \(B^n\) sends \(I\) to \(M_n(I)\).

To verify the ideal description directly, let \(J\subseteq M_n(B)\) and put \(I=\{b:bE_{11}\in J\}\). This is a closed ideal of \(B\). The multiplier matrix units preserve \(J\). In general a multiplier \(m\) preserves an ideal because \(mj=\lim_\lambda(mj)e_\lambda\in J\) for an approximate identity of \(J\), and similarly on the right. Therefore, for \(T=(t_{ij})\in J\),
\(E_{1i}TE_{j1}=t_{ij}E_{11}\in J\), so every entry lies in \(I\). Conversely multiplication of \(bE_{11}\in J\) by the matrix units puts every \(bE_{ij}\) in \(J\). Thus \(J=M_n(I)\), including when \(B\) has no identity. The module formula gives the same ideal since its left products are matrices of products from \(I\).

**Example 5.2 (Full corners).** Let \(p\in M(B)\) be full. For the equivalence \(X=pB\), the correspondence is
\[
\begin{aligned}
I&\longmapsto pIp,\\
J&\longmapsto\overline{\operatorname{span}}BJB.
\end{aligned}
\tag{5.1}
\]
Indeed \(XI=pI\), and its mixed left products span \(pIp\); the inverse right coefficients span \(BJB\). Fullness of \(p\) makes these maps inverse by Theorem 2.1. For a nonfull projection the corner is equivalent to \(\overline{BpB}\), and the inverse formula returns ideals inside that proper ideal of \(B\).

For a nondegenerate representation \(\pi\) of \(B\), its multiplier extension can be constructed directly. If \((e_\lambda)\) is an approximate identity of \(B\), the uniformly bounded operators \(\pi(me_\lambda)\) converge on the dense vectors \(\pi(b)h\) to \(\pi(mb)h\). They therefore converge strongly on all of \(H\); define the limit to be \(\widetilde\pi(m)\). The same calculation for adjoints gives \(\widetilde\pi(m)^*=\widetilde\pi(m^*)\), and multiplication on the dense vectors proves the product rule. This is a unital extension, uniquely determined by \(\widetilde\pi(m)\pi(b)h=\pi(mb)h\).

Put \(p_\pi=\widetilde\pi(p)\). Induction identifies \(pB\otimes_\pi H\) with \(p_\pi H\) by
\(pb\otimes h\mapsto p_\pi\pi(b)h\). The inner product is preserved because its coefficient is \(b^*pc\); nondegeneracy gives dense range in \(p_\pi H\). The corner representation is the restriction of \(\pi(a)\) to this space. Fullness ensures that a nonzero representation cannot have \(p_\pi H=0\).

**Example 5.3 (Stabilization).** The ideals of \(B\otimes\mathcal K\) are exactly \(I\otimes\mathcal K\), where \(I\) is an ideal of \(B\) and the tensor product is spatial.

Here is an explicit verification. Given an ideal \(J\) of the stabilized algebra, put
\(I=\{b:b\otimes E_{11}\in J\}\). Matrix-unit multiplication gives each coefficient of an element of \(J\) in \(I\), by the argument of Example 5.1. Let \(P_n=1_{M(B)}\otimes\sum_{i=1}^nE_{ii}\). For every \(T\in B\otimes\mathcal K\), finite-rank approximation of the compact tensor factors gives \(P_nTP_n\to T\) in norm. For \(T\in J\), each compression belongs to \(M_n(I)\), so \(T\in I\otimes\mathcal K\). Conversely all \(b\otimes E_{ij}\), \(b\in I\), belong to \(J\), and their closed span is \(I\otimes\mathcal K\). The standard-module Morita equivalence has this ideal map, since its rank ones with a vector in \(H_BI\) have precisely these finite matrix coefficients.

**Example 5.4 (A continuous field).** For locally compact Hausdorff \(Y\), the ideals of \(C_0(Y,\mathcal K)\) are
\[
C_0(U,\mathcal K),\qquad U\subseteq Y\text{ open},
\tag{5.2}
\]
with zero extension understood. Indeed \(C_0(Y)\otimes\mathcal K=C_0(Y,\mathcal K)\): the elementary tensor map is isometric by point evaluations, and compact-set partitions with finite-rank operator approximations give dense range. Example 5.3 reduces its ideals to those of \(C_0(Y)\).

To recall that last ideal description, for an ideal \(I\subseteq C_0(Y)\) set \(U=\bigcup_{f\in I}\{y:f(y)\ne0\}\). Certainly \(I\subseteq C_0(U)\). For \(h\in C_c(U)\), finitely many \(f_j\in I\) give \(g=\sum_j|f_j|^2\) bounded below by some \(\delta>0\) on \(\operatorname{supp}h\). Choose a continuous scalar function \(\chi\) that equals \(t^{-1}\) for \(t\geq\delta\) and is zero near zero. Then \(h=g(h\chi(g))\in I\). Density of \(C_c(U)\) proves \(I=C_0(U)\).

Point evaluation gives primitive ideal \(P_y\) on \(C_0(Y)\), and its induced representation on \(\ell^2\) has kernel \(P_y\otimes\mathcal K\). Theorem 4.2 identifies the primitive spaces with the same \(Y\). Their corresponding irreducible dimensions are one and infinite.

## 6. Properties that survive equivalence

**Corollary 6.1.** Morita equivalence preserves simplicity and primitivity, including the existence of a faithful irreducible representation.

*Proof.* The ideal lattices are isomorphic, with zero and the whole algebra corresponding. Thus a nonzero algebra has no proper nonzero ideal exactly when its equivalent algebra has none. A faithful irreducible representation has kernel zero. Induction preserves irreducibility and sends its kernel to \(\mathcal R(0)=0\); inverse induction proves the converse. Primitivity is precisely existence of such a representation. ∎

**Proposition 6.2.** The type I property is Morita invariant. Here we use the representation criterion for type I: the image of every irreducible representation contains the compact operators on its representation space.

*Proof.* Let \(\pi\) be irreducible on \(H\), with \(\mathcal K(H)\subseteq\pi(B)\), and put \(K=X\otimes_\pi H\). For \(x\in X\), the creation map \(C_x:H\to K\), \(h\mapsto x\otimes h\), has adjoint
\(C_x^*(y\otimes k)=\pi(\langle x,y\rangle_B)k\). Its bounded extension follows from the tensor inner-product identity, as in the tensor creation argument of *Imprimitivity bimodules and Morita equivalence*, Theorem 4.1. Compatibility gives
\[
C_x\pi(b)C_y^*
=(\operatorname{Ind}_X\pi)({}_A\langle xb,y\rangle).
\tag{6.1}
\]
Choose \(b\) with \(\pi(b)=\theta_{h,k}\). The left side of (6.1) is the rank one \(\theta_{x\otimes h,y\otimes k}\). Elementary tensors are dense, so these span the compact operators on \(K\). A C*-representation has closed image, hence that image contains \(\mathcal K(K)\). Apply the same argument through \(X^*\) for the reverse implication, and use Theorem 3.1 to cover every irreducible representation on each side. ∎

**Proposition 6.3.** Nuclearity is Morita invariant.

*Proof.* The precise programme prerequisite is [Tensor positivity and nuclearity](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/tensor-positivity-nuclearity.html), Theorem 3.1: for every C*-algebra, nuclearity is equivalent to point-norm approximation of its identity by cpc factorizations through scalar matrix algebras, with nets allowed and no unit required. That theorem is proved there relative to its stated prerequisites. Compare Blackadar, IV.3.1.5, for the classical formulation.

Matrix permanence follows directly in this approximation picture. If \(B\xrightarrow{\alpha}M_m\xrightarrow{\beta}B\) approximates finitely many matrix entries, amplify both maps to \(M_n(B)\to M_{nm}\to M_n(B)\). They remain completely positive contractions: Stinespring dilation in *Completely positive maps*, Theorem 6.1, writes a cpc map as \(V^*\pi(\cdot)V\) with \(\|V\|\leq1\); its amplification uses \(1_n\otimes V\) and therefore has norm at most one. Entrywise convergence gives matrix-norm convergence by the bound \(\|(b_{ij})\|\leq\sum_{ij}\|b_{ij}\|\). Thus \(M_n(B)\) has the approximation property and is nuclear. We now prove module permanence with these finite models.

We show that \(B\) nuclear implies \(\mathcal K(X)\) nuclear. The compact algebra has an approximate identity of positive contractions of the form
\(u=\sum_{j=1}^n\theta_{x_j,x_j}=RR^*\), where \(R:B^n\to X\) is the column creation map. To justify this choice, approximate the square root of a positive contractive compact approximate-identity element by a finite sum of rank ones. Its product with its adjoint is a finite positive sum of diagonal rank ones, by factoring the positive coefficient Gram matrix; dividing by the larger of its norm and one makes it contractive and retains convergence.

For such \(u\), the maps
\[
\begin{aligned}
\alpha_u:\mathcal K(X)&\longrightarrow M_n(B),\\
k&\longmapsto R^*kR,\\
\beta_u:M_n(B)&\longrightarrow\mathcal K(X),\\
m&\longmapsto RmR^*.
\end{aligned}
\tag{6.2}
\]
are completely positive contractions because \(\|R\|^2=\|u\|\leq1\). Their composition sends \(k\) to \(uku\), which converges to \(k\) in norm. On any finite set of images under \(\alpha_u\), nuclearity of \(M_n(B)\) gives a further arbitrarily accurate completely positive contractive factorization through a scalar matrix algebra. Composing these maps proves the approximation property for \(\mathcal K(X)\). Theorem 1.3 of the preceding lesson identifies this algebra with \(A\). Applying the argument to \(X^*\) proves the converse. The nuclearity characterization is the written programme prerequisite specified above; matrix permanence and the module argument have been proved here. ∎

**Example 6.4 (Dimensions are not invariant).** Let \(H=\ell^2(\mathbb N)\). The module \(H\) implements \(\mathcal K(H)\sim\mathbb C\), and induction sends the scalar representation to the identity representation on \(H\). That representation is irreducible: if an invariant closed subspace contains a nonzero \(h\), the rank ones \(\theta_{u,h}\) put every \(u\in H\) in it. Every nonzero irreducible representation of \(\mathbb C\) is one-dimensional, since otherwise any proper closed subspace would be invariant. Thus the property that all irreducible representations are finite-dimensional is not Morita invariant.

## 7. Classical induction and a system of imprimitivity

Take a finite group \(G\), a subgroup \(H\), and \(B=\mathbb C H=C^*(H)\). On \(X=\mathbb C G\), written as functions on \(G\), define
\[
\begin{aligned}
(x u_h)(g)&=x(gh^{-1}),\\
\langle x,y\rangle_B(h)&=\sum_{g\in G}\overline{x(g)}y(gh).
\end{aligned}
\tag{7.1}
\]
Choose representatives \(r_1,\ldots,r_d\) for \(G/H\). Every vector is uniquely \(\sum_j\delta_{r_j}b_j\), and (7.1) becomes the standard column product \(\sum_jb_j^*c_j\). Thus \(X\cong B^d\) as a full Hilbert module; positivity and completeness are explicit.

Let \(D=C(G/H)\rtimes G\), the full crossed product. Functions act by \((M_f x)(g)=f(gH)x(g)\), and group elements act by \((U_sx)(g)=x(s^{-1}g)\). These actions are adjointable and satisfy covariance. For the coset projection \(p_i\),
\[
p_iU_{r_ihr_j^{-1}}p_j
\longleftrightarrow E_{ij}\otimes u_h.
\tag{7.2}
\]
Indeed the operator sends \(\delta_{r_j}\) to \(\delta_{r_i}u_h\) and kills all other basis columns. These operators span \(M_d(B)=\mathcal K(X)\). Conversely the crossed product is spanned by the \(d|G|\) elements \(p_iU_s\). Its image has dimension \(d^2|H|=d|G|\), so the onto map is injective. Hence \(X\) is a \(D\)-\(B\) imprimitivity module.

For a unitary representation \(\sigma\) of \(H\) on \(V\), identify \(X\otimes_\sigma V\) with functions \(F:G\to V\) satisfying
\[
\begin{aligned}
F(gh)&=\sigma(h^{-1})F(g),\\
\|F\|^2&=\sum_{j=1}^d\|F(r_j)\|^2.
\end{aligned}
\tag{7.3}
\]
The identifying map on elementary tensors is
\[
\begin{aligned}
x\otimes v&\longmapsto F_{x,v},\\
F_{x,v}(g)&=\sum_{h\in H}x(gh)\sigma(h)v.
\end{aligned}
\tag{7.4}
\]
Changing variables verifies the covariance condition in (7.3). For \(x=\delta_{r_j}b\), its value at \(r_i\) is \(\delta_{ij}\sigma(b)v\); this proves balancing, inner-product preservation and surjectivity by the standard column decomposition. Under this unitary, \(U_s\) becomes left translation and \(M_f\) becomes multiplication by \(f(gH)\). This is classical finite-group induction together with its coset-function action.

The representation of \(D\) is irreducible exactly when \(\sigma\) is irreducible. Its restriction to the group need not be. For \(G=\mathbb Z/2\), \(H=\{1\}\), the induced group representation on \(\mathbb C^2\) has invariant constant vectors. The coset projections do not preserve that line, and the full crossed-product representation is the irreducible defining representation of \(M_2(\mathbb C)\).

For a locally compact Hausdorff group \(G\) and closed subgroup \(H\), Green’s theorem supplies an imprimitivity module
\[
{}_D X_{C^*(H)},
\qquad D=C_0(G/H)\rtimes G.
\tag{7.5}
\]
The programme proof is [Induced algebras and Green's imprimitivity theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-07.html), Proposition 7.3 and Theorem 7.4, specialized to scalar coefficients and trivial twisting. It constructs the actions, proves positivity and fullness and identifies the full completion, without countability or amenability assumptions. Green, Section 2, Proposition 3 and Theorem 6, credits the original theorem. Both C*-algebras in (7.5) are full versions. Inducing through this module gives the usual induced group representation together with a nondegenerate multiplication representation of \(C_0(G/H)\).

A **system of imprimitivity** on \(G/H\) is a strongly continuous unitary representation \(U\) of \(G\) and a nondegenerate representation \(M\) of \(C_0(G/H)\) satisfying
\[
\begin{aligned}
U_sM_fU_s^*&=M_{\alpha_s(f)},\\
\alpha_s(f)(gH)&=f(s^{-1}gH).
\end{aligned}
\tag{7.6}
\]
[Induced algebras and Green's imprimitivity theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-07.html), Theorem 7.5, proves that these systems arise from representations of \(H\), with the latter determined up to unitary equivalence by the system [Green 1978, Theorem 6]. Theorem 3.1 proves the category equivalence once the Green module is supplied. That written provider proves the Haar-measure and modular-factor construction and its identification with classical induction; these are not left to a book reference. The finite case above proves the mechanism directly. For closed groupoid induction, a correspondence likewise yields a tensor functor; invertibility requires an equivalence module, not merely a correspondence [Li 2024, Sections 8.1–8.4].

## 8. Continuous-trace algebras and the gluing class

The Dixmier–Douady *class* concerns gluing compact algebras, rather than trivializing one Hilbert field. We use the local rank-one formulation of continuous trace. A continuous-trace algebra over a locally compact Hausdorff spectrum \(X\) has compact-operator fibres, the associated \(C_0(X)\)-action, and the following local property: at every point a positive section has rank one and is nonzero throughout some neighborhood, with continuous nonzero eigenvalue. Equivalently, on that neighborhood division by the eigenvalue gives a full rank-one multiplier projection. This formulation allows changing fibre dimension and nonseparable algebras; it does not assume a globally trivial compact-operator bundle. We keep the base \(X\) fixed in all equivalences below.

The prerequisites are now established: *Imprimitivity bimodules and Morita equivalence*, Theorems 1.3 and 3.2, and this lesson’s Theorems 2.1 and 3.1. The ordinary module–field dictionary and finite-rank bundle theorem are *Continuous fields over locally compact spaces*, Theorems 3.1, 4.2 and 5.1. Blackadar, IV.1.7.2–IV.1.7.11, and Jacques Dixmier and Adrien Douady’s 1963 article credit the classical theory. No finite-dimensional-base hypothesis or Hilbert-field triviality theorem is needed for the following gluing argument.

**Lemma 8.1 (Local vector modules and overlap lines).** A full rank-one multiplier projection \(p\) in \(B|_U\) gives a Hilbert \(C_0(U)\)-module \(E_U\) with \(\mathcal K(E_U)=B|_U\). Two such local vector modules differ on their common domain by a Hermitian line bundle. Composition of their intertwining lines is associative.

*Proof.* The module \(B|_Up\) has right coefficient algebra \(p(B|_U)p\), inner product \(v^*w\), and compact left algebra \(B|_U\). Its rank-one maps are multiplication by \(vw^*\), whose closed span is the ideal generated by \(p\), hence all of \(B|_U\). The right algebra has one-dimensional fibres. It is commutative because every commutator vanishes in every fibre, and fibre representations separate the algebra. Its spectrum is \(U\): the Rieffel correspondence identifies its irreducible representations with those of \(B|_U\), with the same central character. The nonunital Gelfand theorem, as identified in the first lesson, therefore identifies the corner with \(C_0(U)\).

If \(E_i,E_j\) are two choices, \(L_{ij}=E_i^*\otimes_{B|_{U_i\cap U_j}}E_j\) is an imprimitivity module from \(C_0(U_i\cap U_j)\) to itself inducing the identity on its spectrum. Its fibres are one-dimensional: a nonzero Hilbert space with compact algebra \(\mathbb C\) has dimension one, since two orthogonal vectors would give two independent rank-one projections. Fibre dimension one and Theorem 5.1 of the field lesson make \(L_{ij}\) a Hermitian line bundle. Tensor associativity and inverse inner-product evaluations give

\[
L_{ij}\otimes L_{jk}\longrightarrow L_{ik}
\]

unitarily and associatively. Tensoring \(E_i\) with \(L_{ij}\) recovers \(E_j\); thus a unit section of this line gives an intertwiner of the two local vector modules, and its adjoint gives the reverse intertwiner. ∎

The paracompact patching lemma in Section 7 of the field lesson supplies locally finite closed shrinkings and subordinate partitions. We will also need a refinement adapted to finite overlaps.

Star refinement also has a direct proof. Regard this partition as a continuous map \(r:X\to c_0(I)\), and put \(m(x)=\|r(x)\|_\infty>0\). Set \(W_x=\{y:\|r(y)-r(x)\|_\infty<m(x)/8\}\). If \(W_x\cap W_y\ne\varnothing\), then \(m(y)<9m(x)/7\). For \(z\in W_y\), the triangle inequality gives \(\|r(z)-r(x)\|_\infty<m(x)/8+m(y)/4< m(x)/2\). A coordinate attaining \(m(x)\) is therefore positive throughout the union of all \(W_y\) meeting \(W_x\). That union lies in its coordinate's original cover member. Thus \((W_x)\) is a star refinement.

Let \(\mathcal S\) be the sheaf of continuous circle-valued functions. We may choose unitary intertwiners \(q_{ij}:E_j\to E_i\) on every double overlap after refinement. To justify this without a good-cover assumption, first shrink the locally finite vector-module cover, keeping the old module on the closure of each shrunk set. Near a point, only finitely many such closures occur, and all their old domains contain that point. Shrink a neighborhood to avoid the other shrunk sets and to trivialize every overlap line for those finitely many labels. A star refinement of these neighborhoods and the shrunk cover makes every double intersection lie in one of these line-trivializing neighborhoods. Choose a unit section of the relevant overlap line, and its adjoint for the reverse direction, so that \(q_{ji}=q_{ij}^{-1}\) and \(q_{ii}=1\). No covering-dimension bound has been imposed.

The two maps \(q_{ij}q_{jk}\) and \(q_{ik}\) intertwine the same compact representations, so their ratio is scalar. To verify this, an operator commuting with every rank one is scalar: fix a unit vector and apply the commutation identity to rank ones mapping it to arbitrary vectors. Write

\[
\begin{gathered}
q_{ij}q_{jk}=c_{ijk}q_{ik},\\
c_{ijk}:U_i\cap U_j\cap U_k\to\mathbb T.
\end{gathered}
\tag{8.1}
\]

The scalar is continuous by evaluating on a local unit vector. Associativity gives

\[
c_{ijk}c_{ikl}=c_{jkl}c_{ijl}.
\tag{8.2}
\]

Thus \(c\) is a Čech 2-cocycle with values in \(\mathcal S\). Replacing \(q_{ij}\) by \(b_{ij}q_{ij}\) multiplies \(c\) by the coboundary \(b_{ij}b_{jk}b_{ik}^{-1}\). Changing the local vector modules has the same effect: after a common refinement choose local unitary identifications between the old and new modules, conjugate the transition maps by them, and compare the remaining scalar overlap factors. Refinement preserves the class. This proves independence of all choices.

**Lemma 8.2 (The integer degree of the class).** On a paracompact Hausdorff \(X\), the exponential sequence of sheaves gives a canonical isomorphism

\[
\check H^2(X,\mathcal S)\cong\check H^3(X,\mathbb Z).
\tag{8.3}
\]

Here \(\mathbb Z\) means locally constant integer functions, and Čech cohomology is over refinements, not one fixed cover.

*Proof.* The sequence \(0\to\mathbb Z\to\mathcal R\to\mathcal S\to1\), with \(\mathcal R\) the continuous real functions and last map \(t\mapsto e^{2\pi it}\), is exact on germs: circle functions have local logarithms. For a locally finite cover and subordinate partition \((\rho_j)\), put on positive-degree real cochains

\[
(ha)_{i_0\ldots i_{r-1}}=\sum_j\rho_j a_{j i_0\ldots i_{r-1}}.
\]

Each product extends by zero outside its domain. Local finiteness and support subordination make the sum continuous, and cancellation in the alternating sums gives \(dh+hd=1\). Thus positive-degree Čech cohomology of \(\mathcal R\) vanishes. Local logarithms lift a circle cochain after refinement; the finite-overlap star-refinement argument applies to its finitely many local components. If \(a\) is a logarithm of a circle 2-cocycle, \(da\) is locally integer-valued. Changing the logarithm changes \(da\) by an integer coboundary; changing the circle cocycle by a coboundary does the same. This defines (8.3). Conversely an integer 3-cocycle \(n\), viewed as real, has \(n=da\) by the contraction, and \(e^{2\pi ia}\) is a circle 2-cocycle. If \(da\) is an integer coboundary, subtract its integer degree-two cochain and use vanishing of real degree-two cohomology to show that the circle cocycle is a coboundary. This proves surjectivity and injectivity. Everything commutes with refinement. ∎

Define \(\delta(B)\) to be the image of \([c]\) under (8.3).

**Theorem 8.3 (Classification over the fixed spectrum).** Two continuous-trace algebras over a paracompact locally compact Hausdorff \(X\) are \(C_0(X)\)-linearly Morita equivalent if and only if their classes \(\delta\) agree. In particular \(\delta(B)=0\) if and only if \(B\cong\mathcal K(E)\) for a full Hilbert \(C_0(X)\)-module \(E\).

*Proof.* If the cocycles for \(B,C\) agree in cohomology, refine to a common cover and adjust one set of transitions by a scalar 1-cochain so that the cocycles are equal. Form the local \(B\)-\(C\) modules

\[
M_i=E_i^B\otimes_{C_0(U_i)}(E_i^C)^*.
\]

Their transitions are \(q^B_{ij}\otimes\overline{q^C_{ij}}\), where the second map is the induced map on the conjugate module in the same direction. The triple discrepancy is \(c^B_{ijk}\overline{c^C_{ijk}}=1\). These transitions therefore glue the local Hilbert-module sections. Take the sections vanishing at infinity, with the right action and \(C\)-valued inner products specified locally. Those specifications agree on overlaps and have the same norm. A uniformly Cauchy sequence has compatible local limits and hence a global limit, so the module is complete. Cutoffs give a dense span of compactly supported sections from individual charts.

Fullness holds locally and hence globally: approximate a coefficient supported in a chart by local inner products, patch on a finite compact cover of its norm-level set, and let the norm outside that set tend to zero. The same patching identifies the left algebra with the compacts. Locally the rank-one map \(\theta_{\xi,\eta}\) is multiplication by the local left inner product; these inner products agree on overlaps. Their span is dense in \(B\), by local fullness and cutoffs. Conversely all global rank ones lie in \(B\), as is seen by approximating their vectors by finite chart-supported sums. The actions and compatibility agree locally, proving that the glued module is an imprimitivity module.

Conversely, a \(C_0(X)\)-linear \(B\)-\(C\) imprimitivity module \(M\) carries \(E_i^C\) to \(M|_{U_i}\otimes_CE_i^C\), a local vector module for \(B\). Its transitions are \(1_M\otimes q^C_{ij}\), with exactly cocycle \(c^C\). Independence of the local vector modules proves \(\delta(B)=\delta(C)\).

For \(C=C_0(X)\), use its constant line module on every chart with identity transitions, giving cocycle one. The first construction then glues a global full Hilbert \(C_0(X)\)-module \(E\) with \(\mathcal K(E)=B\) whenever \(\delta(B)=0\). Conversely a global such \(E\) restricts to a local vector module on each chart with identity transitions. Its cocycle is one, so \(\delta(\mathcal K(E))=0\) directly. ∎

For a full Hilbert field from the field lesson the compact algebra has the required spectrum and local rank-one property. Choose a section of norm one near a point and let \(p=\theta_{s,s}\). The compact-field theorem makes this a continuous rank-one multiplier projection. Its corner is \(C_0(U)\): \(p\theta_{\xi,\eta}p\) is the scalar \(\langle s,\xi\rangle\langle\eta,s\rangle\) times \(p\), and \(s\) with cutoffs produces every scalar coefficient. Its generated ideal is the whole local compact algebra, since \(\theta_{\xi,s}\theta_{s,\eta}=\theta_{\xi,\eta}\). The local spectrum is therefore \(U\), by the Rieffel correspondence. These identifications agree with fibre evaluation and identify the spectrum with \(X\). The global vector module now gives \(\delta(\mathcal K(E))=0\) by Theorem 8.3.

Classification here does not require a constant fibre dimension. A zero class supplies a global vector module; the stronger constant-field conclusion of Theorem 7.4 of the field lesson has its separate finite-dimensional-base hypotheses.

## 9. Exercises with complete solutions

**Exercise 12.1 (Matrix ideals).** Describe every closed ideal of \(M_n(B)\), including for nonunital \(B\).

*Solution.* For an ideal \(J\), set \(I=\{b:bE_{11}\in J\}\). Multiplying by elements in the first diagonal corner shows that \(I\) is a two-sided ideal of \(B\), and the isometric corner embedding shows closedness. Multiplier matrix units preserve \(J\), as proved in Example 5.1. Thus \(E_{1i}TE_{j1}\in J\) for \(T=(t_{ij})\in J\), so each \(t_{ij}\in I\). Conversely \(E_{i1}(bE_{11})E_{1j}=bE_{ij}\in J\) for \(b\in I\). Finite sums give \(J=M_n(I)\). Recovering \(I\) from the first corner proves uniqueness; the product rule shows that every \(M_n(I)\) is indeed a closed ideal. ∎

**Exercise 12.2 (Closed submodules and order).** Prove that \(XI\) is closed, characterize its vectors by their inner products, and show that the ideal correspondence preserves order.

*Solution.* The closed span in (1.1) is contained in the set in (1.2), since all cross coefficients of finite product sums lie in \(I\). If \(\langle x,x\rangle_B\in I\), equation (1.3) with an \(I\)-approximate identity makes \(xe_\lambda\to x\). This proves the reverse inclusion. The characterized set is closed by inner-product continuity, and multiplication by coefficients preserves the closed span. If \(I_1\subseteq I_2\), then \(XI_1\subseteq XI_2\), and the generators in (1.4) give \(\mathcal R(I_1)\subseteq\mathcal R(I_2)\). Formula (2.1) gives the same implication for the inverse. Thus order is both preserved and reflected. ∎

**Exercise 12.3 (Irreducibility).** Prove that induction through an imprimitivity module preserves irreducibility.

*Solution.* Tensor an intertwiner \(T\) with \(1_X\). The inverse natural unitaries (3.5)–(3.6) and identity (3.7) show that every induced intertwiner is uniquely obtained in this way, with inverse (3.8). Tensoring preserves multiplication, adjoints and identity, so the commutants are isomorphic as unital *-algebras. A closed invariant subspace of a *-representation has invariant orthogonal complement, hence an orthogonal projection in its commutant. Conversely the range of such a projection is invariant. The commutant isomorphism preserves zero, identity and all projections. Therefore there is a proper nonzero invariant subspace on one side exactly when there is one on the other. This proves the assertion and its converse. ∎

**Exercise 12.4 (Simplicity and dimensions).** Prove that simplicity is Morita invariant. Determine whether having only finite-dimensional irreducible representations is Morita invariant.

*Solution.* The order isomorphism of Theorem 2.1 sends zero to zero and the whole coefficient algebra to the whole algebra. It therefore bijects proper nonzero ideals, proving simplicity invariance for nonzero algebras. The zero algebra is equivalent only to itself, by fullness and definiteness, so either convention about calling it simple is preserved.

The finite-dimensional assertion is false. The algebra \(\mathbb C\) has only one-dimensional nonzero irreducible representations. The equivalent algebra \(\mathcal K(\ell^2)\) has its infinite-dimensional identity representation, which is irreducible since rank ones send any fixed nonzero vector to every vector. The equivalence is implemented by \(\ell^2\) itself, and its tensor induction sends the scalar representation to this identity representation. Consequently equivalence preserves irreducibility while allowing the dimension to change. The valid type I invariant in Proposition 6.2 concerns compact operators in the image, not finite-dimensional representation spaces. ∎

## What this lesson does not prove

We use the cross-adjoint identities, compact-algebra identification and inverse evaluation of *Imprimitivity bimodules and Morita equivalence*, Lemma 1.2 and Theorems 1.3 and 3.2; its Proposition 2.1 turns a full right module with compact left algebra into an equivalence module. Tensor completion, second-factor transport, associativity and unit maps are *Tensor products and C*-correspondences*, Theorem 1.2, Proposition 2.2, Theorem 3.1 and Proposition 3.2. The standard compact algebra is *Compact operators, multipliers and the strict topology*, Theorem 2.1. Approximate identities, quotient C*-norms, faithful representations and the Gelfand description of commutative primitive ideals are C*-algebra prerequisites. The type I representation criterion is the conventional definition used here.

The all-algebra cpc characterization of nuclearity is *Tensor positivity and nuclearity*, Theorem 3.1, as linked in Section 6. Matrix permanence and compact-module permanence are proved there using the programme Stinespring theorem. The general Green and Mackey constructions have the written proof provider [Induced algebras and Green's imprimitivity theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-07.html), Proposition 7.3 and Theorems 7.4–7.5, with the full crossed-product and generality conventions specified above. Green remains the historical reference. The finite-group model is proved here. General groupoid induction and disintegration are not proved or required for the ideal and representation correspondence. Section 8 constructs the continuous-trace gluing invariant, its integer cohomological degree, the fixed-spectrum Morita classification and the zero-class compact-module criterion, using the earlier field and imprimitivity proofs. Stable isomorphism and Morita invariance of K-theory belong to the following lessons.

## References

- B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006; [author revised version](https://www.bruceblackadar.com/Mathematics/Cycr.pdf), II.7.6.14 and the nuclearity locators listed above.
- P. Green, *The local structure of twisted covariance algebras*, Acta Mathematica 140 (1978), 191–250, Section 2, especially Proposition 3 and Theorem 6. [Original article](https://doi.org/10.1007/BF02392308).
- Y. Li, *Groupoid C*-algebras*, [Leiden seminar notes](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), revised February 2024, Sections 8.1–8.4.

- J. Dixmier and A. Douady, [“Champs continus d’espaces hilbertiens et de C*-algèbres”](https://numdam.org/articles/10.24033/bsmf.1596/), *Bulletin de la Société Mathématique de France* 91 (1963), 227–284; continuous-trace theory, compared with Blackadar IV.1.7.2–IV.1.7.11. The gluing proof here is independently written.
