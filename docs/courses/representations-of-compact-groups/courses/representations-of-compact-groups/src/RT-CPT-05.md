# Compact Lie groups, their Lie algebras and the adjoint representation

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

A compact group has unitary representations. When it is also a Lie group, differentiation turns that global fact into a local one: its adjoint operators are skew-adjoint. This gives a concrete decomposition of its Lie algebra and explains both the usefulness and the limitations of passing from groups to Lie algebras.

We use the exact Lie-group background below, with geometric orientation from core course **D50, Smooth Manifolds and Differential Geometry**, and unitarization from [Representations of compact groups](RT-CPT-01.md). All Lie algebras in this lesson are real until explicitly complexified. Representations act on finite-dimensional complex vector spaces. Dimensions of real Lie groups and their Lie algebras are real dimensions. We take \(n\geq1\).

## Lie-group background and hypotheses

The exponential and closed-subgroup proofs are [*Local tools for bundles and transport*, §2](course:DG-FND/local-tools-for-bundles-and-transport#section-2) and [*Invariant connections on homogeneous bundles*, Theorem 1.1](course:DG-FND/invariant-connections-on-homogeneous-bundles#section-1). The latter also constructs smooth quotients with local sections. The immersed-subgroup correspondence is [*Flat connections and infinitesimal holonomy*, Lemma 3.2](course:DG-FND/flat-connections-and-infinitesimal-holonomy#section-3), using the complete smoothly generated subgroup proof in [*Curvature and holonomy groups*, Lemma 4.1](course:DG-FND/curvature-and-holonomy-groups#section-4). Their statements are:

- A Lie group \(G\) has Lie algebra \(\mathfrak g=T_eG\), whose bracket comes from left-invariant vector fields. The exponential is smooth, is a diffeomorphism between neighborhoods of \(0\) and \(e\), and \(t\mapsto\exp(tX)\) is the unique one-parameter subgroup with initial derivative \(X\).
- A closed subgroup of a finite-dimensional real Lie group is an embedded Lie subgroup. For a closed matrix subgroup \(G\subset GL_N(\mathbb C)\), viewed as a real Lie group,
  \[
  \mathfrak g=\{X:\exp(tX)\in G\text{ for every }t\in\mathbb R\},
  \qquad [X,Y]=XY-YX. \tag{1.1}
  \]
  Each Lie subalgebra is the Lie algebra of a unique connected **immersed** Lie subgroup. That subgroup need not be closed.
- A smooth homomorphism \(f:G\to H\) differentiates to a real Lie-algebra homomorphism, and \(f(\exp X)=\exp(df_eX)\).
- A connected Lie group has a simply connected covering Lie group \(p:\widetilde G\to G\). Its kernel is discrete and central and is naturally isomorphic to \(\pi_1(G,e)\).
- If \(G\) is connected and simply connected, every Lie-algebra homomorphism \(\mathfrak g\to\mathfrak h\) integrates to a unique smooth homomorphism \(G\to H\). The target \(H\) need not be simply connected. For a general connected \(G\), integrate first on \(\widetilde G\); descent to \(G\) requires that the resulting homomorphism kill \(\ker p\).

The internal providers just linked prove the exponential, embedded and immersed subgroup assertions with the stated generality. The covering and integration assertions are proved next. Etingof's [*Lie Groups and Lie Algebras*, version 5](https://arxiv.org/abs/2201.09397v5), §10, supplies a freely readable comparison for the graph construction; its closed-subgroup statement alone is not used as a proof of the general closed-subgroup theorem.

**Theorem 1.2 (integration and the covering group).** The covering and integration statements in the preceding list hold for arbitrary connected finite-dimensional real Lie groups; the target of the integration theorem is unrestricted.

*Proof.* The full path and homotopy lifting construction is [*Flat connections and infinitesimal holonomy*, Lemma 2.1](course:DG-FND/flat-connections-and-infinitesimal-holonomy#section-2). For a Lie group, multiply its based path classes pointwise, \([\gamma][\eta]=[t\mapsto\gamma(t)\eta(t)]\), and invert them pointwise. Homotopies with endpoints fixed make these operations well defined; the group laws follow from those of \(G\). The covering charts make multiplication and inversion smooth: they are the unique local lifts of the corresponding smooth operations in \(G\). The constant path is the identity. Projection is a Lie-group homomorphism with discrete kernel. Conjugation of a fixed kernel element is a continuous map from the connected cover into this discrete kernel and therefore constant, proving centrality. Kernel classes are precisely based loops. Pointwise multiplication and concatenation of loops are homotopic: use \((s,t)\mapsto\gamma(s)\eta(t)\) on the square and deform its diagonal to its bottom and right edges. Thus the kernel is the fundamental group with its usual multiplication.

For a Lie-algebra homomorphism \(\phi:\mathfrak g\to\mathfrak h\), the graph \(\{(X,\phi X)\}\) is a Lie subalgebra of \(\mathfrak g\oplus\mathfrak h\). The immersed-subgroup theorem just identified supplies a connected Lie subgroup \(S\subset G\times H\) with this algebra. The projection \(p:S\to G\) has invertible differential. It is a local diffeomorphism and its image is an open subgroup; connectedness makes it onto.

This projection is a covering, even when the immersed subgroup is not closed in the product. Choose an identity neighbourhood \(U\) on which \(p\) is a diffeomorphism onto an open \(V\), small enough that \(U^{-1}U\cap\ker p=\{e\}\). Every point of \(p^{-1}(V)\) differs from the unique point of \(U\) above it by a kernel element. The resulting kernel translates of \(U\) are disjoint, by the displayed intersection property. They give evenly covered neighbourhoods, translated at other points. When \(G\) is simply connected, path and homotopy lifting make this connected covering a diffeomorphism: lifting paths from the identity is independent of their chosen representatives and gives its inverse. Compose that inverse with the other projection \(S\to H\). Its derivative is \(\phi\), so it is the required smooth homomorphism.

Uniqueness follows because the derivative determines a homomorphism on exponential curves, and an exponential identity neighbourhood generates a connected group. For a general connected domain, integrate on its simply connected cover. A homomorphism descends exactly when it kills the covering kernel; then constancy on fibres gives the descended map, and the covering charts make it smooth. This proves all the assertions. \(\square\)

The graph argument is also the proof of the second fundamental theorem in Etingof's freely accessible [2026 version](https://arxiv.org/abs/2201.09397v5), §10. Here the precise immersed-subgroup and covering proofs are internal.

## The classical compact groups

Put
\[
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}.
\]
We use the definitions
\[
\begin{aligned}
U(n)&=\{g:g^*g=I_n\},&
SU(n)&=\{g\in U(n):\det g=1\},\\
O(n)&=\{g\in M_n(\mathbb R):g^tg=I_n\},&
SO(n)&=\{g\in O(n):\det g=1\},\\
Sp(n)&=\{g\in U(2n):g^tJg=J\}.
\end{aligned} \tag{2.1}
\]
Here \(Sp(n)\) is the compact symplectic group. In particular its defining complex representation has dimension \(2n\). All five groups are closed and bounded subsets of their finite-dimensional matrix spaces, hence compact. They are Lie groups by the closed subgroup theorem.

**Proposition 2.2 (classical Lie algebras).** Their Lie algebras and dimensions are

| Group | Lie algebra | Dimension |
| --- | --- | --- |
| \(U(n)\) | \(X^*=-X\) | \(n^2\) |
| \(SU(n)\) | \(X^*=-X,\ \operatorname{tr}X=0\) | \(n^2-1\) |
| \(O(n),SO(n)\) | \(X\in M_n(\mathbb R),\ X^t=-X\) | \(n(n-1)/2\) |
| \(Sp(n)\) | \(X^*=-X,\ X^tJ+JX=0\) | \(n(2n+1)\) |

*Proof.* Differentiating each equation at the identity gives the displayed necessary conditions; the determinant condition uses \(d(\det)_I(X)=\operatorname{tr}X\). Conversely a skew-Hermitian \(X\) satisfies
\[
(e^{tX})^*e^{tX}=I,
\]
and a real skew-symmetric \(X\) satisfies the real analogue. Moreover \(\det e^{tX}=e^{t\operatorname{tr}X}\). If \(X^tJ+JX=0\), differentiation gives
\[
\frac{d}{dt}\big((e^{tX})^tJe^{tX}\big)
=(e^{tX})^t(X^tJ+JX)e^{tX}=0.
\]
Thus all the conditions are sufficient by (1.1). The real skew-symmetric exponential has determinant one, so \(O(n)\) and \(SO(n)\) have the same Lie algebra.

A skew-Hermitian matrix has \(n\) imaginary diagonal parameters and \(n(n-1)/2\) arbitrary complex entries above the diagonal, giving \(n^2\). Trace zero removes one real parameter. A real skew-symmetric matrix has \(n(n-1)/2\) parameters. Finally the symplectic conditions are equivalent to the block description
\[
X=\begin{pmatrix}A&B\\-\overline B&\overline A\end{pmatrix},
\qquad A^*=-A,\quad B^t=B. \tag{2.3}
\]
The first block contributes \(n^2\) real parameters; the symmetric complex block contributes \(n(n+1)\). Their sum is \(n(2n+1)\). \(\square\)

We need the quaternionic interpretation to prove connectedness of \(Sp(n)\). Write each quaternion uniquely as \(z+jw\), with \(z,w\in\mathbb C\). On the resulting \(\mathbb C^{2n}\), right multiplication by \(i\) is ordinary multiplication by \(i\), and right multiplication by \(j\) is the anti-linear map
\[
C(z,w)=(-\overline w,\overline z)=-J\overline{(z,w)}.
\]
A complex-linear unitary map is right quaternion-linear exactly when it commutes with \(C\). This commutation says \(gJ=J\overline g\), which, using unitarity and conjugating once, is equivalent to \(g^tJg=J\). Such maps preserve the quaternionic Hermitian form \(\sum\overline{q_i}r_i\): its real part is the real inner product, and its other components are recovered by pairing against right multiplication by \(i,j,k\). Hence \(Sp(n)\) is exactly the group of quaternionic unitary maps on \(\mathbb H^n\).

**Proposition 2.4 (connectedness).** The groups \(U(n),SU(n),SO(n),Sp(n)\) are path connected. The group \(O(n)\) has exactly two connected components, its two determinant fibers.

*Proof.* We spell out the sphere argument. Orthonormal-frame completion by Gram–Schmidt over \(\mathbb R,\mathbb C,\mathbb H\) shows that the first-column maps are onto:
\[
\begin{array}{c|c|c}
G&\text{sphere of first columns}&\text{stabilizer of the first standard vector}\\
\hline
U(n)&S^{2n-1}&U(n-1)\\
SU(n),\ n\geq2&S^{2n-1}&SU(n-1)\\
SO(n),\ n\geq2&S^{n-1}&SO(n-1)\\
Sp(n)&S^{4n-1}&Sp(n-1).
\end{array} \tag{2.5}
\]
Set \(U(0)=Sp(0)=\{1\}\). In the special unitary case, multiply the last column of a completed unitary frame by the inverse of its determinant; it leaves the first column fixed. In the real oriented case, change the last column's sign if needed.

These maps have continuous local sections. At a given first column \(v_0\), fix a frame completing it. For \(v\) near \(v_0\), Gram–Schmidt applied to \(v\) followed by the remaining fixed frame vectors has no zero denominators and depends continuously on \(v\). Make the same determinant or orientation adjustment just described.

Here is the precise path argument these sections permit. Choose a path \(\gamma\) on the sphere from the first standard vector to the first column of \(g\). Cover its compact parameter interval by finitely many section neighborhoods and subdivide so each segment lies in one neighborhood. On such a segment beginning at \(t_0\), if \(h_0\) is the already constructed lift, set
\[
h(t)=s(\gamma(t))s(\gamma(t_0))^{-1}h_0.
\]
Its first column is \(\gamma(t)\), and its initial value is \(h_0\). Starting at the identity constructs a path to \(h(1)\). The element \(h(1)^{-1}g\) belongs to the stabilizer. If that stabilizer is path connected, join it to the identity there and concatenate the corresponding translated path.

Induction now applies because all the displayed spheres are path connected. The base cases are \(U(1)=S^1\), \(SU(1)=SO(1)=\{1\}\), and \(Sp(0)=\{1\}\). This proves every claimed connectedness statement. Finally, determinant gives a continuous surjection \(O(n)\to\{1,-1\}\). Its positive fiber is \(SO(n)\); its negative fiber is any fixed reflection times \(SO(n)\). Each fiber is path connected and both are open and closed. \(\square\)

## Adjoint operators and the centre

Conjugation \(h\mapsto ghg^{-1}\) differentiates to \(\operatorname{Ad}_g\in GL(\mathfrak g)\). This gives a smooth representation
\[
\operatorname{Ad}:G\longrightarrow GL(\mathfrak g).
\]
For matrices, \(\operatorname{Ad}_gX=gXg^{-1}\). Its derivative is
\[
\operatorname{ad}_XY=[X,Y]. \tag{3.1}
\]
Indeed differentiating \(e^{tX}Ye^{-tX}\) at zero gives the commutator; the same formula follows from the left-invariant definition of the bracket for general Lie groups.

Write \(\mathfrak z=\{Z:[Z,X]=0\ \forall X\}\), and let \([\mathfrak g,\mathfrak g]\) mean the linear span of all brackets. This span is an ideal by the Jacobi identity.

**Theorem 3.2 (compact Lie-algebra structure).** For a compact Lie group \(G\), including a disconnected one, its Lie algebra has an \(\operatorname{Ad}(G)\)-invariant positive definite real inner product. Relative to it,
\[
\mathfrak g=\mathfrak z\ \mathbin{\perp}\ [\mathfrak g,\mathfrak g]. \tag{3.3}
\]
The Killing form
\[
B(X,Y)=\operatorname{tr}_{\mathbb R}(\operatorname{ad}_X\operatorname{ad}_Y)
\]
is negative semidefinite, has kernel \(\mathfrak z\), and is negative definite on the semisimple ideal \([\mathfrak g,\mathfrak g]\).

*Proof.* Average any positive definite inner product:
\[
\langle X,Y\rangle=\int_G
\langle\operatorname{Ad}_gX,\operatorname{Ad}_gY\rangle_0\,dg.
\]
For nonzero \(X\), the integrand with \(Y=X\) is positive everywhere; compactness even gives a positive minimum. Haar invariance proves invariance. Differentiating invariance along \(\exp(tX)\) gives
\[
\langle[X,Y],Z\rangle=-\langle Y,[X,Z]\rangle. \tag{3.4}
\]
Thus every \(\operatorname{ad}_X\) is skew-adjoint. Its complexification is diagonalizable with purely imaginary eigenvalues, by the spectral theorem for a skew-Hermitian matrix. “Diagonalizable” here refers to complexification; over \(\mathbb R\) there may be rotation blocks.

If \(Z\) is orthogonal to all brackets, (3.4) yields \(\langle Y,[X,Z]\rangle=0\) for all \(X,Y\), so \(Z\in\mathfrak z\). The converse follows from the same identity. Hence \([\mathfrak g,\mathfrak g]^\perp=\mathfrak z\), proving (3.3), with both summands ideals. In an orthonormal basis,
\[
B(X,X)=-\|\operatorname{ad}_X\|_{\mathrm{HS}}^2. \tag{3.5}
\]
This proves semidefiniteness, and equality holds exactly for \(X\in\mathfrak z\). Such an \(X\) pairs to zero with every \(Y\) under \(B\); conversely membership in the kernel forces \(B(X,X)=0\). The restriction to the orthogonal complementary ideal is therefore negative definite.

We give an independent proof of semisimplicity, so no converse Killing-form criterion is being assumed. Every ideal \(I\) has an ideal orthogonal complement by (3.4). Consequently \(\mathfrak g=I\oplus I^\perp\), and \([I,I^\perp]=0\), since the bracket belongs to both ideals. Choose a minimal nonzero ideal \(I\). Every ideal of \(I\) is then an ideal of \(\mathfrak g\), because \(I^\perp\) commutes with \(I\). Thus \(I\) is either simple and nonabelian, or abelian. In the abelian case it is central; minimality makes it one-dimensional. Repeat on \(I^\perp\), decreasing the dimension each time.

We have expressed \(\mathfrak g\) as an orthogonal sum of central lines and nonabelian simple ideals. Each simple ideal equals its own derived algebra; the central lines have zero brackets. Therefore \([\mathfrak g,\mathfrak g]\) is precisely the sum of the simple ideals, which is semisimple. Equivalently it has no nonzero solvable ideal: projecting such an ideal to any simple summand would give a solvable ideal there, necessarily zero. \(\square\)

A real Lie algebra admitting an invariant positive definite inner product is often called **of compact type**. This includes abelian Lie algebras. Negative definiteness of its Killing form characterizes the centre-free case among these algebras; it does not cover every compact Lie algebra.

## Differentiating representations

We first justify smoothness without assuming compactness.

**Lemma 4.1.** Every continuous homomorphism \(\pi:G\to GL(V)\), with \(G\) a finite-dimensional Lie group and \(V\) finite-dimensional, is smooth.

*Proof.* Left Haar measure on a Lie group is given by a smooth left-invariant density. Choose a nonnegative smooth compactly supported function \(\phi\), of integral one, in a sufficiently small identity neighborhood that \(\|\pi(g)-I\|<1/2\) on its support. Then
\[
A=\int_G\phi(g)\pi(g)\,dg
\]
satisfies \(\|A-I\|<1/2\), so is invertible. For \(v\in V\), left invariance gives
\[
\pi(x)Av=\int_G\phi(x^{-1}h)\pi(h)v\,dh. \tag{4.2}
\]
This is smooth in \(x\): on each compact coordinate neighborhood the relevant \(h\)'s lie in a fixed compact set, and every derivative of the smooth factor can be passed under the integral there. Since \(A\) is onto, every orbit map \(x\mapsto\pi(x)w\) is smooth. Its matrix entries in a basis of \(V\) are smooth, proving the lemma. \(\square\)

Differentiation thus defines
\[
d\pi:\mathfrak g\to\operatorname{End}_{\mathbb C}(V),\qquad
d\pi(X)=\left.\frac{d}{dt}\right|_{t=0}\pi(\exp tX),
\quad
\pi(\exp X)=e^{d\pi(X)}. \tag{4.3}
\]
It preserves real linear combinations and brackets. When \(G\) is compact, choose the invariant Hermitian inner product supplied by unitarization. Differentiating \(\pi(\exp tX)^*\pi(\exp tX)=I\) then gives \(d\pi(X)^*=-d\pi(X)\). Thus \(d\pi\) lands in \(\mathfrak u(V)\) **for that inner product**.

**Proposition 4.4.** If \(G\) is connected, \(\pi\) is determined by \(d\pi\). A complex subspace \(W\subset V\) is \(G\)-invariant if and only if it is \(d\pi(\mathfrak g)\)-invariant.

*Proof.* The subgroup generated by an exponential identity neighborhood is open. Every coset is open, so its complement is also open. Connectedness forces it to be all of \(G\). Consequently the exponential formula (4.3) determines \(\pi\) on generators and hence everywhere. If \(W\) is \(G\)-invariant, differentiating its orbit curves keeps the derivative in \(W\), since \(W\) is closed. Conversely derivative invariance implies invariance under all powers of \(d\pi(X)\), hence under its exponential, and then under all of \(G\). \(\square\)

Connectedness cannot be omitted: the determinant and the trivial character of \(O(n)\) have identical zero derivatives but differ on the reflection component.

Let \(\mathfrak g_{\mathbb C}=\mathfrak g\otimes_{\mathbb R}\mathbb C\). A representation of the real Lie algebra on complex \(V\) means a real-linear bracket-preserving map to \(\operatorname{End}_{\mathbb C}(V)\). It extends uniquely by
\[
\rho_{\mathbb C}(X+iY)=\rho(X)+i\rho(Y). \tag{4.5}
\]
Complex bilinearity verifies preservation of the bracket. Restriction and this extension are inverse operations, also on intertwining maps and invariant subspaces.

If \(G\) is simply connected, the integration theorem applied to \(GL(V)\) integrates every such representation. For a general connected compact group there is a period condition. For example, with \(S^1=\{e^{it}\}\), a Lie-algebra representation specified by \(d\pi(1)=A\) integrates to \(S^1\) precisely when
\[
e^{2\pi A}=I. \tag{4.6}
\]
This follows by first integrating on the covering group \(\mathbb R\), where \(\pi(t)=e^{tA}\), and checking its kernel \(2\pi\mathbb Z\). Even the one-dimensional map \(1\mapsto1\) is a representation of the abelian Lie algebra of \(S^1\), but it neither integrates to \(S^1\) nor becomes skew-Hermitian under a change of inner product. Hence the unitarity assertion for derivatives of compact-group representations cannot be extended to arbitrary representations of compact Lie algebras with centre.

For a concrete complexification, put
\[
I=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
K=\begin{pmatrix}0&i\\i&0\end{pmatrix}.
\]
These form a real basis of \(\mathfrak{su}(2)\), with
\[
[I,J_0]=2K,\quad[J_0,K]=2I,\quad[K,I]=2J_0. \tag{4.7}
\]
Inside its complexification set
\[
H=-iI,\qquad E=(J_0-iK)/2,\qquad F=(-J_0-iK)/2.
\]
These are respectively \(\operatorname{diag}(1,-1),E_{12},E_{21}\). They span \(\mathfrak{sl}_2(\mathbb C)\), giving an isomorphism
\[
\mathfrak{su}(2)_{\mathbb C}\simeq\mathfrak{sl}_2(\mathbb C),
\qquad [H,E]=2E,\quad[H,F]=-2F,\quad[E,F]=H. \tag{4.8}
\]
Classification of its highest-weight modules belongs to the Lie-algebra representation course; here (4.5) specifies exactly how the two representation problems are related.

## The adjoint covering and explicit Killing forms

**Proposition 5.1.** The adjoint homomorphism \(SU(2)\to SO(\mathfrak{su}(2))\simeq SO(3)\) is onto and has kernel \(\{\pm I_2\}\). It is a two-sheeted universal covering. In particular \(\pi_1(SO(3))\simeq\mathbb Z/2\mathbb Z\).

*Proof.* On \(\mathfrak{su}(2)\) take \(\langle X,Y\rangle=-\operatorname{tr}(XY)/2\). It is a positive definite invariant real inner product, and \(I,J_0,K\) are orthonormal. Conjugation is orthogonal. Its determinant is one because \(SU(2)\) is connected and it equals one at the identity.

By (4.7), the centre of \(\mathfrak{su}(2)\) is zero. Thus \(d\operatorname{Ad}=\operatorname{ad}\) is injective, and it is an isomorphism onto \(\mathfrak{so}(3)\) by dimensions. The inverse function theorem makes the image contain an identity neighborhood in \(SO(3)\). An open subgroup of a connected group is the whole group, proving surjectivity. A matrix in the kernel commutes with \(I\), so is diagonal; commuting also with \(J_0\) makes its two diagonal entries equal. Unitarity and determinant one then give \(I_2\) or \(-I_2\).

[The three-sphere description](RT-CPT-04.md) identifies \(SU(2)\) with \(S^3\). The quotient by \(q\mapsto-q\) is a two-sheeted covering: choose a neighborhood \(U\) of any \(q\) disjoint from \(-U\); the quotient is a homeomorphism on each of \(U,-U\). The induced continuous bijection from the compact quotient to Hausdorff \(SO(3)\) is a homeomorphism; the local differential isomorphism makes the covering smooth.

For completeness, the topological input that \(S^3\) is simply connected follows from the Seifert–van Kampen theorem: the complements of the north and south poles are each \(\mathbb R^3\), while their intersection is path connected. Their union therefore has trivial fundamental group. Thus this is the universal covering. The covering-group statement of Section 1 identifies its two-element kernel with \(\pi_1(SO(3))\). \(\square\)

In quaternion coordinates \(X=x_1I+x_2J_0+x_3K\), (4.7) says \(\operatorname{ad}_XY=2x\times y\). Hence
\[
B_{\mathfrak{su}(2)}(X,Y)=-8\,x\cdot y
=4\operatorname{tr}_2(XY). \tag{5.2}
\]
Indeed for \(A_v(w)=v\times w\), the vector triple-product identity gives
\[
A_vA_w=w v^t-(v\cdot w)I_3,\qquad
\operatorname{tr}_3(A_vA_w)=-2v\cdot w.
\]
Since \([A_v,A_w]=A_{v\times w}\), the adjoint representation of \(\mathfrak{so}(3)\), in the \(v\)-coordinates, is \(A_v\) itself. Consequently
\[
B_{\mathfrak{so}(3)}(A_v,A_w)=-2v\cdot w
=\operatorname{tr}_3(A_vA_w). \tag{5.3}
\]
The differential of the covering sends \(X\) to \(A_{2x}\); (5.2) and (5.3) therefore agree under this isomorphism.

The group centre of \(U(n)\) is \(\{zI_n:|z|=1\}\): commuting with every diagonal unitary forces a matrix to be diagonal, and commuting with permutation matrices makes its diagonal entries equal. The analogous argument for its Lie algebra, using diagonal skew-Hermitian matrices and the matrices \(E_{ab}-E_{ba}\), gives \(\mathfrak z(\mathfrak u(n))=i\mathbb R I_n\). Explicitly
\[
X=\frac{\operatorname{tr}X}{n}I_n+
\left(X-\frac{\operatorname{tr}X}{n}I_n\right),
\qquad
\mathfrak u(n)=i\mathbb R I_n\ \mathbin{\perp}\ \mathfrak{su}(n), \tag{5.4}
\]
for the inner product \(-\operatorname{tr}(XY)\). This displays the central directions on which the Killing form vanishes.

Finally every \(2\times2\) matrix satisfies \(g^tJg=(\det g)J\). Thus \(Sp(1)=SU(2)\), consistently of real dimension three.

## Exercises with complete solutions

**Exercise 1 (easy).** Compute explicit Lie algebras and dimensions for \(SO(3),SU(3),Sp(2)\).

*Solution.* The first consists of
\[
\begin{pmatrix}0&-c&b\\c&0&-a\\-b&a&0\end{pmatrix},
\qquad a,b,c\in\mathbb R,
\]
and has dimension three. For \(SU(3)\) take
\[
\begin{pmatrix}
ia&z&w\\-\overline z&ib&u\\-\overline w&-\overline u&-i(a+b)
\end{pmatrix},
\qquad a,b\in\mathbb R,\quad z,w,u\in\mathbb C.
\]
This gives dimension \(2+6=8\). For \(Sp(2)\) use (2.3) with
\[
A=\begin{pmatrix}ia&z\\-\overline z&ib\end{pmatrix},\qquad
B=\begin{pmatrix}u&v\\v&w\end{pmatrix}.
\]
The parameters in \(A\) contribute four real dimensions and those in \(B\) six, so the answer is ten. Necessity and sufficiency of all three descriptions were proved by differentiation and exponentiation in Proposition 2.2.

**Exercise 2 (medium).** Prove the adjoint surjection \(SU(2)\to SO(3)\) and its kernel by computing rotations.

*Solution.* The basis (4.7) gives
\[
\begin{aligned}
\operatorname{Ad}_{e^{tI}}I&=I,\\
\operatorname{Ad}_{e^{tI}}J_0&=\cos(2t)J_0+\sin(2t)K,\\
\operatorname{Ad}_{e^{tI}}K&=-\sin(2t)J_0+\cos(2t)K.
\end{aligned}
\]
These follow either by multiplying \((\cos t+I\sin t)J_0(\cos t-I\sin t)\) or by exponentiating \(\operatorname{ad}_I\). Cyclically, the image contains rotations about all three coordinate axes with every angle.

These rotations generate \(SO(3)\). To see this explicitly, coordinate-axis rotations can first move \(e_1\) to any given unit vector: a rotation about the second axis chooses its third coordinate, and one about the third chooses the direction of its first two coordinates. For \(R\in SO(3)\), choose their product \(Q\) with \(Qe_1=Re_1\). Then \(Q^{-1}R\) fixes \(e_1\) and is a planar rotation on \(e_1^\perp\), hence is a rotation about the first axis. Therefore \(R\) is in the image. The kernel computation in Proposition 5.1 uses commutation with \(I,J_0\), forcing a scalar matrix; determinant one gives exactly \(\pm I_2\). This proves both assertions directly and agrees with the differential proof.

**Exercise 3 (medium).** Compute \(B_{\mathfrak{su}(n)}\) as a multiple of \(\operatorname{tr}(XY)\).

*Solution.* First work on \(M_n(\mathbb C)\). Let \(L_X(Z)=XZ\), \(R_X(Z)=ZX\). In the basis \(E_{ab}\), direct diagonal-entry counting yields
\[
\operatorname{tr}(L_XL_Y)=n\operatorname{tr}(XY),\quad
\operatorname{tr}(R_XR_Y)=n\operatorname{tr}(XY),\quad
\operatorname{tr}(L_XR_Y)=\operatorname{tr}X\,\operatorname{tr}Y.
\]
For example the coefficient of \(E_{ab}\) in \(XE_{ab}Y\) is \(X_{aa}Y_{bb}\), which proves the last identity by summing. Since \(\operatorname{ad}_X=L_X-R_X\),
\[
\operatorname{tr}_{M_n}(\operatorname{ad}_X\operatorname{ad}_Y)
=2n\operatorname{tr}(XY)-2\operatorname{tr}X\,\operatorname{tr}Y. \tag{6.1}
\]
For traceless \(X,Y\), the scalar line in \(M_n=\mathbb CI_n\oplus\mathfrak{sl}_n(\mathbb C)\) contributes zero, so the trace on \(\mathfrak{sl}_n\) is \(2n\operatorname{tr}(XY)\).

The natural complexification of \(\mathfrak{su}(n)\) is \(\mathfrak{sl}_n(\mathbb C)\): a traceless complex matrix \(Z\) decomposes as
\[
Z=\frac{Z-Z^*}{2}+i\frac{Z+Z^*}{2i},
\]
with both summands before multiplication by \(i\) traceless and skew-Hermitian. The trace of the complexification of a real endomorphism equals its real trace. Therefore
\[
\boxed{B_{\mathfrak{su}(n)}(X,Y)=2n\operatorname{tr}(XY).} \tag{6.2}
\]
The right side is real, since conjugation of the trace gives \(\operatorname{tr}(YX)\). For \(X=Y\neq0\) it is negative, since \(\operatorname{tr}(X^2)=-\operatorname{tr}(X^*X)\). For \(n=1\) the algebra is zero, so the formula is still valid. The same calculation on \(\mathfrak u(n)\) gives (6.1); it vanishes when either argument is a scalar imaginary matrix.

**Exercise 4 (hard).** Prove that \(Sp(1)\) is connected and simply connected, and that \(Sp(n)\) is connected for every \(n\).

*Solution.* By the \(2\times2\) determinant identity, \(Sp(1)=SU(2)\). Its matrices are
\[
\begin{pmatrix}a&b\\-\overline b&\overline a\end{pmatrix},
\qquad |a|^2+|b|^2=1,
\]
so this is \(S^3\). The sphere is path connected and simply connected by the two-chart van Kampen argument in Proposition 5.1.

For the general case, quaternionic Gram–Schmidt completes any unit \(v\in\mathbb H^n\) to an orthonormal frame. One may use the right-linear projection
\[
w\longmapsto w-\sum_j u_j\langle u_j,w\rangle_{\mathbb H}
\]
and divide each nonzero remainder by its positive real norm. The resulting frame is an element of \(Sp(n)\) with first column \(v\), and the fiber at \(e_1\) is \(\operatorname{diag}(1,Sp(n-1))\). Near any fixed \(v_0\), retain the other columns of a frame at \(v_0\); the same construction gives a continuous section because its remainders remain nonzero.

Given \(g\), choose a sphere path from \(e_1\) to \(ge_1\). Lift it on finitely many section neighborhoods by the explicit formula in Proposition 2.4. This joins the identity to \(h\) with \(he_1=ge_1\). Then \(h^{-1}g\) lies in \(Sp(n-1)\). Induction joins that element to the identity inside the fiber and completes a path to \(g\). This proves connectedness for every \(n\), without assuming an unproved global frame section. The exercise claims simple connectedness only for \(n=1\).

## Source and course connections

Milne, *Algebraic Groups*, Section 10d, Definitions 10.18 and 10.20 and Theorem 10.23, gives the algebraic-group analogue of Lie algebra, adjoint action and bracket. Its scheme-theoretic construction is distinct from the analytic compactness and Haar averaging used here.

The orthogonal ideal decomposition was proved directly, leaving general Cartan criteria to the Lie-algebra course. The next lessons use the invariant inner product for maximal tori, roots and Weyl integration. The period obstruction (4.6) will remain essential when deciding which highest weights belong to a particular compact group.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §10. The graph-subgroup construction gives a proof comparison for Lie algebra integration. The complete internal immersed-subgroup and covering proofs are linked above, and the full integration/descent theorem is proved here.
