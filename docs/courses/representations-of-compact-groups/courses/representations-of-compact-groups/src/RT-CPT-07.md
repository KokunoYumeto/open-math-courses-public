# Roots and the Weyl group of a compact Lie group

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

Choosing a maximal torus reduces conjugacy to a finite symmetry problem. The nontrivial weights of its adjoint action are roots. Each root supplies a three-dimensional compact Lie algebra and a reflection, and these reflections account for every symmetry arising from conjugation.

Let \(G\) be compact and connected, let \(T\subset G\) be a maximal torus, and put \(\mathfrak t=\operatorname{Lie}(T)\). We import the invariant inner product and integration theorem from [Compact Lie groups and Lie algebras](RT-CPT-05.md), and all maximal-torus and centralizer results from [Tori and the maximal torus theorem](RT-CPT-06.md).

Characters of \(T\) are written additively, so \(-\alpha\) means \(\alpha^{-1}\). To distinguish a character from its differential, set
\[
d\alpha=i\,a_\alpha=2\pi i\,\alpha_{\mathbb R},
\qquad a_\alpha=2\pi\alpha_{\mathbb R}\in\mathfrak t^*. \tag{1.1}
\]
Thus \(\alpha(\exp X)=e^{ia_\alpha(X)}\). Reflection and root-system formulas below use the real angular covectors \(a_\alpha\). No factor \(2\pi\) is suppressed in passing back to characters or exponential lattices.

## The finite normalizer quotient

Write \(N=N_G(T)=\{g:gTg^{-1}=T\}\) and
\[
W(G,T)=N/T.
\]
The subgroup \(T\) is normal in \(N\), so this is a group.

**Proposition 1.2.** The Weyl group \(W(G,T)\) is finite and acts faithfully on \(T\), on \(\mathfrak t\), and on \(X^*(T)\).

*Proof.* The normalizer is closed: if \(g_j\to g\) with \(g_jTg_j^{-1}=T\), closedness of \(T\) gives \(gTg^{-1}\subset T\), and using \(g_j^{-1}\to g^{-1}\) gives equality. It is therefore a compact Lie group.

Conjugation by \(n\in N\) preserves the exponential lattice \(\Lambda=\ker(\exp:\mathfrak t\to T)\). In a lattice basis its derivative is an integral invertible matrix. Those matrix entries depend continuously on \(n\). Hence the identity component \(N^0\) acts trivially on the lattice and thus on \(\mathfrak t\) and \(T\). The preceding lesson proves \(C_G(T)=T\), so \(N^0\subset T\). Conversely connected \(T\) lies in \(N^0\), giving \(N^0=T\). A compact Lie group has finitely many components: they are open, and compactness gives a finite subcover by them. Thus \(N/T\) is finite.

The kernel of its action on \(T\) is \(C_G(T)/T\), hence trivial. An automorphism acting trivially on \(\mathfrak t\) acts trivially on \(\exp\mathfrak t=T\). Finally characters' differentials span \(\mathfrak t^*\), because the dual lattice has full rank. Trivial action on all characters therefore implies trivial action on \(\mathfrak t\). \(\square\)

The action is orthogonal for the invariant inner product. On characters we use \((w\alpha)(t)=\alpha(w^{-1}t)\), and the corresponding dual action on covectors.

## Roots and their compact rank-one groups

Extend the real invariant inner product complex bilinearly to \(b\) on \(\mathfrak g_{\mathbb C}\). Its associated positive Hermitian form is
\[
(U,V)=b(U,\overline V).
\]
Complex conjugation refers to the real form \(\mathfrak g\).

The finite-dimensional unitary representation \(\operatorname{Ad}|_T\) is a sum of simultaneous character spaces, by simultaneous diagonalization of commuting unitary operators. Its zero-character space is \(\mathfrak t_{\mathbb C}\), since \(\mathfrak z_{\mathfrak g}(\mathfrak t)=\mathfrak t\). Let \(\Phi\) be its nontrivial characters. Then
\[
\mathfrak g_{\mathbb C}=\mathfrak t_{\mathbb C}
\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha,\qquad
[H,U]=ia_\alpha(H)U\quad(U\in\mathfrak g_\alpha). \tag{2.1}
\]
Conjugation exchanges \(\mathfrak g_\alpha\) and \(\mathfrak g_{-\alpha}\), so \(\Phi=-\Phi\). The bracket satisfies
\[
[\mathfrak g_\alpha,\mathfrak g_\beta]\subset\mathfrak g_{\alpha+\beta},
\]
where an absent character space means zero. In particular opposite root spaces bracket into \(\mathfrak t_{\mathbb C}\).

Fix \(\alpha\), abbreviate \(a=a_\alpha\), and let \(a^\sharp\in\mathfrak t\) be its metric dual. Put \(q=\|a\|^2>0\). The strict inequality follows because a character of a connected torus with zero differential is trivial.

Take \(e\in\mathfrak g_\alpha\setminus\{0\}\), with \(c=b(e,\overline e)>0\). Invariance gives, for \(Z\in\mathfrak t\),
\[
b([e,\overline e],Z)=b(e,[\overline e,Z])
=ia(Z)c.
\]
Since the bracket lies in \(\mathfrak t_{\mathbb C}\), this identifies it exactly:
\[
[e,\overline e]=ic\,a^\sharp.
\]
Define
\[
E=\sqrt{\frac{2}{cq}}\,e,\qquad
F=-\overline E,\qquad
H=-\frac{2i}{q}a^\sharp. \tag{2.2}
\]
Direct substitution proves
\[
[H,E]=2E,\quad[H,F]=-2F,\quad[E,F]=H. \tag{2.3}
\]
These three independent vectors span a copy of \(\mathfrak{sl}_2(\mathbb C)\). Its real form in \(\mathfrak g\) has basis
\[
I_\alpha=iH=\frac{2a^\sharp}{q},\qquad
J_\alpha=E-F,\qquad K_\alpha=i(E+F). \tag{2.4}
\]
Their brackets are \([I_\alpha,J_\alpha]=2K_\alpha\) and its cyclic companions, exactly the quaternion basis of \(\mathfrak{su}(2)\) in the preceding Lie-algebra lesson.

**Lemma 2.5 (root multiplicity).** Every \(\mathfrak g_\alpha\) has complex dimension one.

*Proof.* For the adjoint operators on \(\mathfrak g_{\mathbb C}\), metric invariance gives
\[
(\operatorname{ad}U)^*=-\operatorname{ad}(\overline U).
\]
Thus \(\operatorname{ad}E\) and \(\operatorname{ad}F\) are adjoints, while \(\operatorname{ad}H\) is self-adjoint.

If \(v\in\mathfrak g_\alpha\) is orthogonal to \(E\), the same bracket computation used above gives \([v,\overline E]=0\): its pairing with \(Z\in\mathfrak t\) is \(ia(Z)b(v,\overline E)=0\), and it lies in \(\mathfrak t_{\mathbb C}\). Therefore \((\operatorname{ad}F)v=0\), while \((\operatorname{ad}H)v=2v\). Write \(A=\operatorname{ad}E\), \(B=\operatorname{ad}F=A^*\). Relation (2.3) implies
\[
2\|v\|^2=((AB-BA)v,v)=\|Bv\|^2-\|Av\|^2\leq0.
\]
Hence \(v=0\). There is no nonzero vector orthogonal to \(E\) in that root space, proving dimension one. \(\square\)

**Theorem 2.6 (root homomorphism and reflection).** There is a smooth homomorphism
\[
\varphi_\alpha:SU(2)\longrightarrow G
\]
whose differential identifies \(\mathfrak{su}(2)\) with the real span in (2.4). Its image of \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) normalizes \(T\) and acts on \(\mathfrak t\) by
\[
s_\alpha(Z)=Z-\frac{2a(Z)}{\|a\|^2}a^\sharp. \tag{2.7}
\]

*Proof.* The basis correspondence in (2.4) is a real Lie-algebra homomorphism. The simply connected domain \(SU(2)=S^3\) permits its integration by Theorem 1.2 of lesson five. Its image is compact and hence closed. Injectivity of this group homomorphism is not asserted; a root subgroup can have the topology of \(SO(3)\).

In \(SU(2)\), the displayed matrix is \(\exp(\frac\pi2J_0)\), and its conjugation sends \(I\) to \(-I\). Under \(\varphi_\alpha\) it therefore sends \(a^\sharp\) to \(-a^\sharp\). Every \(Z\in\ker a\subset\mathfrak t\) commutes with \(E,F,H\), by (2.1), and is fixed by \(\exp(\frac\pi2\operatorname{ad}J_\alpha)\). Thus the action is exactly (2.7). It preserves \(\mathfrak t\), hence preserves \(T=\exp\mathfrak t\). This gives a root reflection in \(W(G,T)\). \(\square\)

The **coroot** is the homomorphism
\[
\alpha^\vee:S^1\to T,\qquad
\alpha^\vee(e^{i\theta})=\varphi_\alpha(\operatorname{diag}(e^{i\theta},e^{-i\theta}))
=\exp(\theta I_\alpha). \tag{2.8}
\]
It need not be primitive. Since \(\exp(2\pi I_\alpha)=e\), every character \(\beta\) satisfies
\[
\langle\beta,\alpha^\vee\rangle
=a_\beta(I_\alpha)
=\frac{2(a_\beta,a_\alpha)}{\|a_\alpha\|^2}\in\mathbb Z. \tag{2.9}
\]
Here the integer is the degree of \(\beta\circ\alpha^\vee:S^1\to S^1\). In lattice language \(2\pi I_\alpha\in\Lambda\), and \(\beta_{\mathbb R}(2\pi I_\alpha)\) is that same integer.

## The root system and all normalizer symmetries

Identify \(\Phi\) with the finite set of its angular covectors in the Euclidean space \(V=\operatorname{span}_{\mathbb R}\{a_\alpha\}\subset\mathfrak t^*\).

**Theorem 3.1.** This is a reduced crystallographic root system in \(V\). Its reflection group equals \(W(G,T)\). It acts simply transitively on the Weyl chambers.

*Proof.* Finiteness, nonzero roots, spanning and opposite roots were established in (2.1). A normalizer element permutes the torus character spaces under the adjoint action, so its dual action preserves \(\Phi\). In particular every reflection (2.7) preserves \(\Phi\). Equation (2.9) proves the crystallographic integrality axiom.

We prove reducedness explicitly. Suppose \(2\alpha\) were a root, and take \(v\in\mathfrak g_{2\alpha}\). The three-dimensional subspace \(S=\operatorname{span}_{\mathbb C}\{E,F,H\}\) is invariant under the compact rank-one Lie algebra in (2.4); its orthogonal complement is invariant as well because that algebra acts skew-adjointly. Distinct \(T\)-characters have orthogonal spaces, so \(v\in S^\perp\). Now \([F,v]\in\mathfrak g_\alpha=\mathbb CE\), but it also lies in \(S^\perp\), and is therefore zero. On the other hand \([H,v]=4v\). The norm identity in Lemma 2.5 gives \(4\|v\|^2\leq0\), so \(v=0\), a contradiction.

If \(a_\beta=k a_\alpha\) with \(k>0\), integrality applied in both directions says \(2k\) and \(2/k\) are positive integers. Their product is four, so \(k\in\{1/2,1,2\}\). The two nonunit possibilities would give a root twice another root, already excluded. Negative multiples are treated using \(-\beta\). This proves reducedness.

We import the following exact finite-root-system facts from [**RT-LIE-08, Root systems and their Weyl groups**, §§2–5, Theorem 2.1, Lemmas 4.1–4.2 and Theorem 5.1](course:RT-LIE/RT-LIE-08#5-simple-transitivity-and-the-longest-element): the reflection hyperplanes divide \(V\) into open convex chambers; the group generated by all root reflections acts simply transitively on these chambers and is generated by the reflections in the simple roots of any chosen chamber. Those combinatorial facts are not reproved here.

Let \(W_\Phi\) denote that reflection group. Theorem 2.6 gives \(W_\Phi\subset W(G,T)\). We show that no extra chamber stabilizer exists. Identify \(V\) with its metric-dual subspace \(V^\sharp\subset\mathfrak t\). Its orthogonal complement is the centre \(\mathfrak z(\mathfrak g)\): a vector annihilated by every root commutes with every space in (2.1). Connected \(G\) fixes this centre pointwise, since it is generated by exponentials and each infinitesimal adjoint operator vanishes there.

If \(w\in W(G,T)\) preserves a chamber \(C\subset V^\sharp\), choose \(Y_0\in C\) and average its finite \(w\)-orbit. Convexity and the strict chamber inequalities put the average \(Y\) in \(C\), and \(wY=Y\). Every root is nonzero on \(Y\), so its Lie centralizer is \(\mathfrak t\). Crucially, Lemma 4.1 of the preceding lesson proves the group centralizer \(C_G(Y)\) connected; therefore it is \(T\), since its Lie algebra is \(\mathfrak t\). A representative of \(w\) fixes \(Y\), lies in this group centralizer, and hence lies in \(T\). Thus \(w=1\).

For arbitrary \(w\), choose \(u\in W_\Phi\) taking the chamber \(wC\) back to \(C\). Then \(uw\) stabilizes \(C\), so is trivial. Hence \(w=u^{-1}\in W_\Phi\), proving equality and simple transitivity. If \(\Phi\) is empty, \(\mathfrak g=\mathfrak t\), connected \(G\) is the torus \(T\), and both groups are trivial; the zero-dimensional space has its single chamber. \(\square\)

## Conjugacy and continuous class functions

**Theorem 4.1.** Two elements of \(T\) are conjugate in \(G\) if and only if they belong to the same \(W(G,T)\)-orbit. Restriction induces a bijection
\[
C(G)^{\mathrm{class}}\longrightarrow C(T)^W. \tag{4.2}
\]

*Proof.* Normalizer conjugation is certainly group conjugation. Conversely suppose \(gtg^{-1}=t'\), with \(t,t'\in T\). Both \(T\) and \(gTg^{-1}\) are connected subgroups of \(C_G(t')\), so lie in its identity component \(C_G(t')^0\). They are maximal tori there: a larger torus there would be a larger torus in \(G\). The identity component is compact and connected. Its maximal torus theorem supplies \(h\in C_G(t')^0\) with \(hgTg^{-1}h^{-1}=T\). Then \(hg\) normalizes \(T\) and sends \(t\) to \(t'\), proving the first assertion. The full group \(C_G(t')\) need not be connected.

Restriction of a class function is \(W\)-invariant and is injective by the maximal torus theorem. For \(f\in C(T)^W\), consider the continuous function \((g,t)\mapsto f(t)\) on \(G\times T\). It is constant on fibers of the surjection
\[
G\times T\to G,\qquad(g,t)\mapsto gtg^{-1},
\]
by the conjugacy statement just proved. This surjection is a quotient map because its domain is compact and its target Hausdorff. The function thus descends to a continuous class function on \(G\), giving surjectivity. \(\square\)

## Measuring the distance between adjoint orbits

The Weyl group also measures how far two conjugacy classes in the Lie algebra lie apart. Let \(B\) be any invariant positive inner product on \(\mathfrak g\), and give the orbit space the distance
\[
d([X],[Y])=\min_{g\in G}\|X-\operatorname{Ad}_gY\|_B.
\]
Compactness attains the minimum. Invariance and composition prove the triangle inequality; a zero minimum means that the orbits coincide. Thus this is a metric on the set of adjoint orbits.

**Proposition 4.3 (the torus quotient is an isometry).** For compact connected \(G\), inclusion induces an isometry \(\mathfrak t/W\to\mathfrak g/G\). In particular, for \(X,Y\in\mathfrak t\),
\[
\min_{g\in G}\|X-\operatorname{Ad}_gY\|_B
=\min_{w\in W}\|X-wY\|_B.
\]
Central directions and singular toral elements are included.

*Proof.* Every Lie algebra element is conjugate into \(\mathfrak t\), by the Lie algebra form of the maximal-torus theorem proved in lesson six. Suppose \(gY=Z\) in adjoint notation, with \(Y,Z\in\mathfrak t\). The maximal tori \(T\) and \(gTg^{-1}\) lie in \(C_G(Z)^0\) and remain maximal there. Conjugating them inside this compact connected group gives \(c\in C_G(Z)^0\) such that \(cg\in N_G(T)\). Then \(cgY=Z\). This proves that the toral intersections of adjoint orbits are exactly their Weyl orbits; it is the Lie algebra version of Theorem 4.1, using a vector centralizer rather than the centralizer of one exponential.

Choose \(Z=\operatorname{Ad}_gY\) minimizing the distance from \(X\). Differentiation in every direction \(A\in\mathfrak g\) gives
\[
0=\left.\frac{d}{dt}\right|_{t=0}
\|X-\operatorname{Ad}_{\exp(tA)}Z\|_B^2
=-2B(X,[A,Z])=-2B([Z,X],A).
\]
Hence \([Z,X]=0\). The subgroup \(C_G(X)^0\) is compact and connected, has \(T\) as a maximal torus, and has Lie algebra \(\{A:[A,X]=0\}\). Its maximal-torus theorem conjugates \(Z\) into \(\mathfrak t\) by some \(c\) fixing \(X\). This conjugation does not change the minimizing distance. The preceding toral-orbit argument identifies \(\operatorname{Ad}_cZ\) with \(wY\) for some \(w\in W\). A minimum over the whole group is therefore achieved by a Weyl representative. The reverse inequality follows since all Weyl representatives occur in the group. \(\square\)

For \(U(n)\), choose \(B(X,Y)=-\operatorname{tr}(XY)\) on skew-Hermitian matrices. If \(A,B_0\) are Hermitian matrices with real eigenvalues \(a_i,b_i\), the result reads
\[
\min_{u\in U(n)}\|A-uB_0u^{-1}\|_{\mathrm{HS}}^2
=\min_{\sigma\in S_n}\sum_i(a_i-b_{\sigma(i)})^2.
\]
Ordering both eigenvalue lists the same way gives the minimum. Indeed a crossed pair costs an additional \(2(a_i-a_j)(b_i-b_j)\geq0\); successive removal of inversions proves the claim. Taking \(u=I\) then gives the Hoffman–Wielandt bound
\[
\sum_i(a_i-b_i)^2\leq\|A-B_0\|_{\mathrm{HS}}^2
\]
for the ordered lists. Repeated eigenvalues cause no exception. The Weyl quotient records both the conjugacy class and the optimal distance between classes.

## Classical examples and exercises

For \(U(n)\), conjugation on a matrix unit is
\[
\operatorname{Ad}_{\operatorname{diag}(z_1,\ldots,z_n)}E_{ij}
=z_i z_j^{-1}E_{ij}.
\]
Thus \(\Phi=\{\varepsilon_i-\varepsilon_j:i\neq j\}\) and \(W=S_n\); permutation matrices give every permutation, and a normalizer must permute the one-dimensional coordinate weight spaces of the defining representation. The roots span the sum-zero hyperplane, and the scalar central direction is fixed. The same Weyl group occurs for \(SU(n)\), using phase adjustments to make a permutation representative have determinant one. Continuous class functions on \(U(n)\) are precisely continuous symmetric functions of its \(n\) unit-circle eigenvalues.

For the rotation-block tori of the preceding lesson, the defining complex weights are \(\pm\varepsilon_j\), with an extra zero weight for \(SO(2n+1)\). The orthogonal adjoint representation is the second exterior power, so its nonzero weights are sums of two distinct defining weight lines. The symplectic adjoint representation is the second symmetric power, which also permits twice a single weight; the equivariant matrix identification is proved in Exercise 2. Thus the roots of \(SO(2n+1)\) are \(\pm\varepsilon_i\pm\varepsilon_j\) and \(\pm\varepsilon_i\), those of \(SO(2n)\) are \(\pm\varepsilon_i\pm\varepsilon_j\), and those of \(Sp(n)\) are \(\pm\varepsilon_i\pm\varepsilon_j\) and \(\pm2\varepsilon_i\), with \(i<j\) in the two-index expressions. Their Weyl groups are
\[
\begin{aligned}
W(SO(2n+1))=W(Sp(n))&=(\mathbb Z/2\mathbb Z)^n\rtimes S_n,\\
W(SO(2n))&=(\mathbb Z/2\mathbb Z)^{n-1}\rtimes S_n. \tag{5.1}
\end{aligned}
\]
To see the normalizers directly, the orthogonal groups' defining representation has distinct complex weights \(\pm\varepsilon_j\), with an extra zero line in odd dimension. A normalizer must permute the corresponding real planes and may reverse each plane's orientation. Plane permutations have determinant one. In even dimension an even number of orientation reversals is required; in odd dimension the last axis can absorb their determinant. In \(Sp(n)\), quaternionic coordinate permutations and left multiplication by \(j\) on each coordinate realize arbitrary signed permutations. The defining complex weights again allow no additional actions.

**Exercise 1 (easy).** Compute \(\Phi\) and \(W\) for \(U(3)\) and \(SU(2)\).

*Solution.* For \(U(3)\) there are the six roots
\[
\pm(\varepsilon_1-\varepsilon_2),\quad
\pm(\varepsilon_1-\varepsilon_3),\quad
\pm(\varepsilon_2-\varepsilon_3),
\]
each on its matrix-unit line. Reflection in \(\varepsilon_i-\varepsilon_j\) swaps the two coordinates. They generate \(S_3\), of order six.

For \(SU(2)\), write \(T=\{\operatorname{diag}(z,z^{-1}):|z|=1\}\). Its character lattice is \(\mathbb Z\), with generator \(z\). Conjugation on \(E_{12}\) has character \(z^2\), and on \(E_{21}\) has \(z^{-2}\), so the roots are \(\{2,-2\}\) in that lattice. The matrix \(J_0\) sends \(z\) to \(z^{-1}\), giving \(W\simeq\mathbb Z/2\mathbb Z\). The coroot for \(2\) is \(z\mapsto\operatorname{diag}(z,z^{-1})\). For comparison, the rotation-angle torus of \(SO(3)\) has roots \(\{1,-1\}\) in its own character lattice, and its coroot has degree two. The double cover changes the lattice even though the real root-system type is the same.

**Exercise 2 (medium).** Compute the roots, Weyl groups and coroots for \(SO(5)\) and \(Sp(2)\).

*Solution.* Use angular coordinates \(\theta_1,\theta_2\) on the tori, with each coordinate of period \(2\pi\). The invariant metric \(-\operatorname{tr}(XY)/2\) in each defining representation makes these torus coordinates Euclidean. For \(SO(5)\), the complex defining representation has weights \(0,\pm\varepsilon_1,\pm\varepsilon_2\). The adjoint representation is its second exterior power: the invariant symmetric form identifies an infinitesimal skew map with an alternating tensor. Adding two distinct weights gives
\[
\Phi_{B_2}=\{\pm\varepsilon_1,\pm\varepsilon_2,
\ \pm\varepsilon_1\pm\varepsilon_2\}.
\]
The two zero-weight wedges supply the two-dimensional torus algebra. There are no roots \(2\varepsilon_j\), because wedging a one-dimensional weight line with itself gives zero.

For \(Sp(2)\), the defining weights are \(\pm\varepsilon_1,\pm\varepsilon_2\). Its complex adjoint representation is the second symmetric power: \(X\mapsto XJ^{-1}\) is symmetric and transforms as \(XJ^{-1}\mapsto g(XJ^{-1})g^t\). This gives
\[
\Phi_{C_2}=\{\pm2\varepsilon_1,\pm2\varepsilon_2,
\ \pm\varepsilon_1\pm\varepsilon_2\}.
\]
Again the zero weight occurs twice, and all eight nonzero weights occur once.

For either system, reflection in a coordinate root reverses one sign, and reflection in \(\varepsilon_1-\varepsilon_2\) swaps the coordinates. Thus both Weyl groups are the eight signed permutations of two coordinates, isomorphic to the dihedral group of a square. Their coroots differ: for \(B_2\) the short \(\varepsilon_j\) has coroot vector \(2\varepsilon_j\), while \(\varepsilon_1\pm\varepsilon_2\) has coroot vector \(\varepsilon_1\pm\varepsilon_2\). For \(C_2\) the long \(2\varepsilon_j\) has coroot vector \(\varepsilon_j\), while the two-coordinate coroots are unchanged. These vectors specify the loops \(e^{i\theta}\mapsto\exp(\theta I_\alpha)\) of (2.8). Thus their root and coroot systems are interchanged: the groups have isomorphic Weyl groups, but their root lengths and analytic coroot maps are different.

**Exercise 3 (medium).** Prove the conjugacy assertion of Theorem 4.1 using a centralizer, and explain precisely which component is used.

*Solution.* From \(gtg^{-1}=t'\), both \(T\) and \(gTg^{-1}\) commute with \(t'\). Because each torus is connected and contains the identity, both lie in \(C_G(t')^0\). Each is maximal there by its maximality in \(G\). Apply the maximal torus theorem to this compact connected identity component to find \(h\) conjugating \(gTg^{-1}\) to \(T\). Since \(h\) commutes with \(t'\), \(hg\) still sends \(t\) to \(t'\), and now normalizes \(T\). Its class in \(N/T\) gives the required Weyl conjugation. Applying the theorem to the entire centralizer without passing to its identity component would incorrectly assume connectedness, disproved by the half-turn example in the preceding lesson.

**Exercise 4 (hard).** Prove root multiplicity one without invoking a highest-weight classification.

*Solution.* Construct \(E,F,H\) by (2.2), so \(F=-\overline E\), \([E,F]=H\), and \([H,v]=2v\) on \(\mathfrak g_\alpha\). For a vector \(v\) in that root space orthogonal to \(E\), the opposite-root bracket lies in \(\mathfrak t_{\mathbb C}\) and satisfies
\[
b([v,\overline E],Z)=ia_\alpha(Z)b(v,\overline E)=0
\qquad(Z\in\mathfrak t).
\]
The restriction of \(b\) to \(\mathfrak t_{\mathbb C}\) is nondegenerate, hence \([v,\overline E]=0\) and \([F,v]=0\). Invariance of the positive Hermitian form makes \(\operatorname{ad}F=(\operatorname{ad}E)^*\). Therefore
\[
2\|v\|^2
=\|[F,v]\|^2-\|[E,v]\|^2
=-\|[E,v]\|^2\leq0.
\]
Thus \(v=0\), and the nonzero line \(\mathbb CE\) is the entire root space. This proves the assertion using only the constructed rank-one brackets and compact positivity.

## Sources and the combinatorial import

Milne, *Algebraic Groups*, Sections 21a–d and 21j, gives the algebraic root-datum counterpart. Davis, *The Geometry and Topology of Coxeter Groups*, Chapter 6, especially Theorem 6.6.3, treats geometric reflection groups and their chamber action. Our construction proves the analytic roots, multiplicities, coroot integrality and rank-one homomorphisms directly; the finite-root-system chamber and simple-reflection facts stated in Theorem 3.1 are the RT-LIE-08 prerequisite import.

For a group that is not simply connected, its character lattice is not automatically the full abstract weight lattice. The \(SU(2)\)/\(SO(3)\) comparison already shows the distinction. Connectedness of \(G\) is likewise essential to identify the full normalizer quotient with root reflections; the next lesson uses that identification in the Weyl integration formula.

Our coroot is the actual circle homomorphism (2.8), whose differential is \(2a_\alpha^\sharp/\|a_\alpha\|^2\) and whose pairing with \(\alpha\) is two. Its analytic period must be retained when comparing lattices.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §32. The SU(2) type example is a companion to the rank-one representations used here. The general root-system/chamber proofs are the exact internal RT-LIE-08 results, not an inference from that rank-one example.

Claudio Gorodski, [*A metric approach to representations of compact Lie groups*, revised11 January 2016](https://www.ime.usp.br/~gorodski/ps/orbit-spaces-revision2016.pdf), §1.1, pages2–4, gives the diagonal real-symmetric quotient example. His [*Lecture Notes on Compact Lie Groups and Their Representations*, author file 26 May 2025](https://www.ime.usp.br/~gorodski/teaching/mat6001-2025/master05-26-2025.pdf), Theorem 4.1.3 gives the invariant-pairing conjugacy argument (both accessed 3 October 2026). Proposition 4.3 supplies the full general adjoint quotient isometry, and the Hermitian eigenvalue bound is derived here.
