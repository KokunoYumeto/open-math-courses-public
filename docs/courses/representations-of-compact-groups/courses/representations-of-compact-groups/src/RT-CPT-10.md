# Weights and the theorem of the highest weight

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

A highest weight determines an irreducible representation of a compact connected Lie group. Its integrality has two distinct parts: the root subgroups impose integer coroot pairings, and the actual torus imposes all period conditions. The second part distinguishes groups with the same Lie algebra.

Throughout, \(G\) is compact and connected, \(T\) is a maximal torus, and \(\mathfrak t\) is its real Lie algebra. Representations are continuous and complex. They are finite-dimensional when irreducible, unitary after averaging, and smooth, by the earlier lessons. We use the roots, normalizer, and root \(SU(2)\) homomorphisms from [Roots and the Weyl group](RT-CPT-07.md). The exact simple-root and chamber proofs are [**RT-LIE-08**, Theorem 2.1, Lemma 4.1 and Theorem 5.1](course:RT-LIE/RT-LIE-08#2-a-positive-halfspace-produces-a-base), including the simple-reflection permutation of other positive roots and the identity for the pairings of \(
ho\).

One algebraic import is needed: for
\[
\mathfrak g_{\mathbb C}=\mathfrak n_-\oplus\mathfrak t_{\mathbb C}\oplus\mathfrak n_+,
\qquad
\mathfrak n_\pm=\bigoplus_{\alpha\in\Phi^+}\mathfrak g_{\pm\alpha},
\]
the ordered-monomial consequence of PBW says
\[
U(\mathfrak g_{\mathbb C})
=\operatorname{span}\{u_-u_0u_+:
u_\pm\in U(\mathfrak n_\pm),\
u_0\in U(\mathfrak t_{\mathbb C})\}. \tag{0.1}
\]
The full PBW proof is [**RT-LIE-13**, §2, Theorem 2.1](course:RT-LIE/RT-LIE-13#2-ordered-words-and-the-complete-pbw-proof); its §4 proves ordered triangular multiplication. Only spanning is used here. A positive central torus causes no difficulty: order a basis of the full \(\mathfrak t_{\mathbb C}\) between the negative and positive root bases, and the same PBW proof applies to this reductive algebra. The algebraic Verma-module classification belongs to **RT-LIE-14**. Here we prove the compact-group consequences, including why Lie invariance implies group invariance.

## Characters and the two integrality conditions

Put \(\Lambda=\ker(\exp:\mathfrak t\to T)\). We identify a torus character with its real differential divided by \(2\pi i\):
\[
\chi_\lambda(\exp X)=e^{2\pi i\lambda(X)},\qquad
X^*(T)=\{\lambda\in\mathfrak t^*:\lambda(\Lambda)\subset\mathbb Z\}. \tag{1.1}
\]
The preceding torus lesson proves this identification and that \(X^*(T)\) is a full lattice. Angular differentials used in the roots lesson are \(2\pi\lambda\); this factor must be retained.

For a unitary representation \(V\), simultaneous diagonalization of the commuting torus action gives
\[
V=\bigoplus_{\lambda\in X^*(T)}V_\lambda,\qquad
V_\lambda=\{v:\pi(t)v=\chi_\lambda(t)v\text{ for all }t\in T\}, \tag{1.2}
\]
with finitely many nonzero summands. The weight multiplicity is \(\dim V_\lambda\).

**Proposition 1.3.** Weight multiplicities are \(W=N_G(T)/T\)-invariant. In the complexified adjoint representation, the nonzero weights are precisely the roots, each with multiplicity one; the zero-weight space is \(\mathfrak t_{\mathbb C}\).

*Proof.* For \(n\in N_G(T)\), \(v\in V_\lambda\), and \(t\in T\),
\[
\pi(t)\pi(n)v
=\pi(n)\pi(n^{-1}tn)v
=\chi_\lambda(n^{-1}tn)\pi(n)v.
\]
Thus the invertible map \(\pi(n)\) takes \(V_\lambda\) onto \(V_{w\lambda}\), where \(\chi_{w\lambda}(t)=\chi_\lambda(n^{-1}tn)\). The adjoint statement is the root-space decomposition proved in lesson seven. Its zero space centralizes \(\mathfrak t\) and is exactly \(\mathfrak t_{\mathbb C}\), since the maximal torus centralizer has Lie algebra \(\mathfrak t\). In particular its multiplicity is \(\dim T\), including central directions. For the trivial group this space has dimension zero and there are no weights. \(\square\)

For a root \(\alpha\), write \(A_\alpha\in\mathfrak t\) for the derivative of its coroot cocharacter
\[
c_\alpha:\mathbb R/\mathbb Z\to T,\qquad
c_\alpha(s)=\exp(sA_\alpha),\qquad \alpha(A_\alpha)=2. \tag{1.4}
\]
The root \(SU(2)\) construction proves \(A_\alpha\in\Lambda\). In the invariant metric, \(A_\alpha=2\alpha^\sharp/\|\alpha\|^2\), where \(\alpha\) is normalized as in (1.1). Define \(\langle\lambda,\alpha^\vee\rangle=\lambda(A_\alpha)\). Every analytic weight therefore has integer coroot pairings.

When \(G\) is semisimple, the roots span \(\mathfrak t^*\), and the root-system weight lattice is
\[
P=\{\lambda\in\mathfrak t^*:
\langle\lambda,\alpha^\vee\rangle\in\mathbb Z\text{ for every }\alpha\}.
\]
With \(Q=\mathbb Z\Phi\), we have \(Q\subset X^*(T)\subset P\). The first inclusion holds because adjoint roots are actual torus characters; the second follows from (1.4).

For a group with a positive-dimensional center, the same displayed integrality condition defines a larger set \(P_{\mathrm{full}}\), which is **not a lattice**. In the orthogonal decomposition into the central dual and the span of the roots,
\[
P_{\mathrm{full}}=\mathfrak z^*\oplus P_{\mathrm{ss}}. \tag{1.5}
\]
Coroots impose no condition on the central dual. For example, in \(U(n)\) every vector \((c,\ldots,c)\), \(c\in\mathbb R\), has zero coroot pairings, whereas it is an analytic weight only when \(c\in\mathbb Z\). Thus the name “algebraic weight lattice” refers to \(P_{\mathrm{ss}}\); the full compact group always requires (1.1).

## Positive roots and highest vectors

Choose \(Y\in\mathfrak t\) with \(\alpha(Y)\neq0\) for every root. Set
\[
\Phi^+=\{\alpha:\alpha(Y)>0\},\qquad
\lambda\geq\mu\iff
\lambda-\mu\in\sum_{\alpha\in\Phi^+}\mathbb Z_{\geq0}\alpha. \tag{2.1}
\]
The root-system prerequisite supplies simple roots \(\alpha_1,\ldots,\alpha_r\), and every positive root is a nonnegative integer combination of them. The positive cone is pointed: a nonempty positive sum evaluates positively on \(Y\). Hence (2.1) is a partial order. Maximizing \(\lambda(Y)\) is a useful way to find a maximal weight; numerical comparison alone is not this partial order.

A weight is dominant when \(\langle\lambda,\alpha_i^\vee\rangle\geq0\) for every simple root, equivalently for every positive root. Central components are unrestricted by dominance. Put
\[
\rho=\frac12\sum_{\alpha\in\Phi^+}\alpha. \tag{2.2}
\]
Each simple reflection permutes the positive roots other than its own simple root and negates that root. Thus \(s_i\rho=\rho-\alpha_i\), and the reflection formula gives \(\langle\rho,\alpha_i^\vee\rangle=1\). In particular \(\rho\in P_{\mathrm{ss}}\); it need not be an actual torus character.

For \(E_\alpha\in\mathfrak g_\alpha\), differentiation of the conjugation relation gives
\[
d\pi(E_\alpha)V_\mu\subset V_{\mu+\alpha}. \tag{2.3}
\]
A highest vector is a nonzero \(v\in V_\lambda\) annihilated by every positive root space. The following consequence of (0.1) will also be used in a reducible representation.

**Lemma 2.4 (cyclic highest vector).** If \(v\) is a highest vector of weight \(\lambda\), its Lie-generated subspace
\(M=U(\mathfrak g_{\mathbb C})v\) is spanned by products of negative root operators applied to \(v\). Its weights are \(\lambda-\sum_i m_i\alpha_i\), \(m_i\geq0\), and \(M_\lambda=\mathbb Cv\).

*Proof.* In an ordered product \(u_-u_0u_+v\), the positive-root factor kills \(v\) unless it contributes its scalar term. Cartan factors act by scalars on \(v\). What remains is a linear combination of negative-root monomials. A nonempty monomial subtracts a nonzero positive sum, by evaluation on \(Y\), so cannot have weight \(\lambda\). The empty monomial supplies exactly its original line. This proves all assertions from the stated PBW spanning import. \(\square\)

Every such \(M\) is \(G\)-invariant. Indeed it is invariant under \(d\pi(X)\) for real \(X\in\mathfrak g\), hence under their exponentials. Since \(\pi(\exp X)=\exp(d\pi(X))\), it is invariant under a neighborhood of the identity. That neighborhood generates the connected group: the generated subgroup is open, its cosets are open, and connectedness leaves only one coset. This proves the passage from Lie action to group action without assuming \(G\) simply connected.

**Theorem 2.5 (highest weight).** An irreducible representation has a unique highest weight \(\lambda\). Its highest-weight space is one-dimensional, it is generated by that line under \(\mathfrak g_{\mathbb C}\), and \(\lambda\) is dominant.

*Proof.* Choose a weight \(\lambda\) maximizing \(\lambda(Y)\), and a nonzero \(v\in V_\lambda\). Formula (2.3) forces all positive root operators to kill \(v\). Its cyclic subspace is \(G\)-invariant and nonzero, so equals \(V\). Lemma 2.4 gives \(V_\lambda=\mathbb Cv\) and every other weight strictly below \(\lambda\).

If \(v'\) is another highest vector of weight \(\mu\), the same argument makes it cyclic, so \(\lambda\leq\mu\) and \(\mu\leq\lambda\). Pointedness gives \(\lambda=\mu\), and the one-dimensional space makes the vectors proportional.

For a simple root choose the normalized root triple \(E,F,H\), with \([E,F]=H\) and \(H=A_{\alpha_i}/(2\pi i)\). On the unitary root \(SU(2)\) representation, \(d\pi(F)=d\pi(E)^*\) and \(d\pi(H)\) is Hermitian. Since \(Ev=0\),
\[
\|Fv\|^2
=\langle v,EFv\rangle
=\langle\lambda,\alpha_i^\vee\rangle\,\|v\|^2.
\]
Therefore the pairing is nonnegative. It is an integer by the coroot period (1.4); equivalently it is the nonnegative top weight of a root \(SU(2)\) summand. This proves dominance. The argument also covers a torus: there are no lowering operators, so \(V=\mathbb Cv\). \(\square\)

**Theorem 3.1 (uniqueness from the weight).** Two irreducible representations with the same highest weight are equivalent.

*Proof.* Choose highest vectors \(v_1\in V_1\), \(v_2\in V_2\) of weight \(\lambda\), and let
\[
M=U(\mathfrak g_{\mathbb C})(v_1,v_2)\subset V_1\oplus V_2.
\]
It is \(G\)-invariant. Both coordinate projections \(p_i:M\to V_i\) are surjective: their images are nonzero invariant subspaces. Lemma 2.4 says
\[
M_\lambda=\mathbb C(v_1,v_2).
\]
The kernel of \(p_2\) is an invariant subspace of \(V_1\oplus0\). If nonzero it equals \(V_1\oplus0\), by irreducibility, and contains \((v_1,0)\), contradicting the displayed highest line. Thus \(p_2\) is injective. The same argument makes \(p_1\) injective. The composition \(p_2p_1^{-1}:V_1\to V_2\) is the required group intertwiner. Conversely an equivalence preserves every torus weight, and hence the highest weight. \(\square\)

These theorems prove uniqueness and the necessary condition \(\lambda\in X^*(T)\), dominant. **Existence for every such \(\lambda\)** will be proved in the next lesson by the character formula and completeness. It is not assumed here. We also make no general unproved identification of \(X^*(T)\) with \(P\); the requested classical equalities are proved directly below.

## Computing the lattices

**Proposition 4.1.** In the \(SU(2)\) coordinate \(t_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta})\), analytic weights are the integers \(m\), dominant when \(m\geq0\). On its quotient \(SO(3)\), only the even \(m\)'s are analytic. For \(SU(n)\), \(n\geq2\), and \(Sp(r)=USp(2r)\), \(r\geq1\), the analytic lattice equals the root-system lattice \(P\).

*Proof.* For \(SU(2)\), a character is \(e^{im\theta}\), with \(m\in\mathbb Z\); the positive root has exponent two and the coroot pairing is \(m\). The torus map to \(SO(3)\) identifies \(\theta\) with \(\theta+\pi\). A character descends exactly when \(e^{im\pi}=1\), so \(m\) is even. The earlier polynomial representations realize every \(m\geq0\), and precisely the even ones descend. In this coordinate \(\rho=1\), an algebraic weight that does not descend to \(SO(3)\).

For \(SU(n)\), write
\[
X=2\pi i\operatorname{diag}(x_1,\ldots,x_n),\qquad\sum_i x_i=0.
\]
Its period lattice consists of integer \(x_i\) of sum zero. Identify a real weight with a vector \(a\in\mathbb R^n\) of sum zero, by \(\lambda(X)=\sum_i a_ix_i\). The periods \(e_i-e_j\) generate that integer lattice. Thus
\[
X^*(T)=\{a:\sum_i a_i=0,\ a_i-a_j\in\mathbb Z\}.
\]
Roots are \(e_i-e_j\) and their coroots have the same coordinate vectors. Their integrality conditions give exactly the same set \(P\).

For \(Sp(r)\), use the torus \(\operatorname{diag}(e^{2\pi ix_j})\) in quaternionic coordinates, or the corresponding paired complex eigenvalues. Its periods are precisely \(\mathbb Z^r\), so \(X^*(T)=\mathbb Z^r\). The type \(C_r\) roots are \(\pm e_i\pm e_j\) and \(\pm2e_i\). The coroot of \(2e_i\) is \(e_i\), forcing every coordinate of a weight in \(P\) to be integral. Conversely integral coordinates pair integrally with all the other coroots \(e_i\pm e_j\). Hence \(P=\mathbb Z^r=X^*(T)\). \(\square\)

For \(U(n)\), the analytic lattice is \(\mathbb Z^n\), dominant tuples are nonincreasing, and the preceding character lesson proves all occur. On \(SU(n)\), the corresponding sum-zero weight is
\[
a=\lambda-\frac{|\lambda|}{n}(1,\ldots,1). \tag{4.2}
\]
Integer determinant shifts vanish on the trace-zero torus, exactly as the earlier restriction theorem requires.

The highest vectors of \(\bigwedge^k\mathbb C^n\) and \(\operatorname{Sym}^k\mathbb C^n\) are respectively
\[
e_1\wedge\cdots\wedge e_k,\qquad e_1^k.
\]
Upper matrix units kill the wedge because they either hit no occupied index or create a repeated factor; they kill \(e_1^k\) because their column index is greater than one. Their \(U(n)\) weights are \((1^k,0^{n-k})\) and \((k,0,\ldots,0)\). Their irreducibility is already proved in lesson nine. After (4.2), the exterior weights for \(1\leq k<n\) are the fundamental weights
\[
\omega_k=e_1+\cdots+e_k-\frac{k}{n}\sum_{j=1}^n e_j,\qquad
\langle\omega_k,\alpha_i^\vee\rangle=\delta_{ki}. \tag{4.3}
\]
The symmetric weight is \(k\omega_1\). The top exterior power is the determinant and becomes trivial on \(SU(n)\).

## Spin and the obstruction to descent

In \(SO(2r+1)\), \(r\geq1\), the torus has \(r\) independently periodic rotation angles. Consequently \(X^*(T)=\mathbb Z^r\). The roots are \(\pm e_i\pm e_j,\ \pm e_i\); their coroot conditions give
\[
P=\mathbb Z^r\ \cup\ \bigl((\tfrac12,\ldots,\tfrac12)+\mathbb Z^r\bigr). \tag{5.1}
\]
Indeed \(2a_i\in\mathbb Z\) and \(a_i-a_j\in\mathbb Z\) force all coordinates to have the same parity; conversely these two cosets satisfy all coroot pairings. For \(r=1\) this is \(\tfrac12\mathbb Z\) in the rotation-angle coordinate.

The spin highest weight is \(\omega_r=(\tfrac12,\ldots,\tfrac12)\). We use the Clifford construction of the compact double cover
\(\operatorname{Spin}(2r+1)\to SO(2r+1)\), with kernel \(\{1,-1\}\): the group consists of even products of real unit Clifford vectors, acting on vectors by conjugation.

For completeness, the Clifford cover in this example has an internal proof. Put \(d=2r+1\geq3\) and use the real Clifford relations \(uv+vu=2(u,v)\). Ordered products of distinct basis vectors are linearly independent: represent the Clifford algebra on its exterior space by exterior multiplication plus contraction, which satisfies these relations; their products applied to the vacuum have their distinct leading exterior monomials. These products also span by swapping generators and removing repeated indices.

For a unit vector \(u\), the map \(x\mapsto-uxu^{-1}=x-2(u,x)u\) is its orthogonal hyperplane reflection. Even products therefore act by conjugation in \(SO(d)\). Every orthogonal map is a product of at most \(d\) such reflections. To prove this, if its image of the first basis vector differs from that vector, reflection normal to their difference makes them agree; otherwise use no reflection. Restrict to their orthogonal complement and induct. Determinant one forces an even number of reflections. Thus the conjugation map from even products is onto.

An even Clifford element commuting with every basis vector is scalar: conjugating each even monomial by a basis vector negates it exactly when that basis index occurs in the monomial. The ordered basis therefore excludes every nonempty even monomial from the common commutant. If an even product is scalar \(a\), reversing the product shows \(a^2=1\). Hence the kernel is exactly \(\{1,-1\}\); the second element is itself the product \(u(-u)\).

Any lift differs by this kernel from an even product of at most \(d\) unit vectors. Thus the whole group is the image of a finite union of compact products of spheres, allowing two extra vectors for the sign, and is compact. It is a closed matrix Lie subgroup of the units in the finite-dimensional Clifford algebra by the closed-subgroup theorem. Plane bivectors exponentiate as \(\cos(t/2)+e_ie_j\sin(t/2)\); their conjugations give all coordinate-plane infinitesimal rotations, so the derivative is onto \(\mathfrak{so}(d)\). Its kernel is zero because the group kernel is discrete. The inverse function theorem and the two kernel translates prove that it is a smooth two-sheeted covering. Finally each even product can be grouped into pairs; each pair is joined to the identity by paths of its unit vectors, using connectedness of \(S^{d-1}\). The group is connected. This proves exactly the compact cover needed for the spin calculation, without a classification theorem.

Here is that calculation. On \(S=\bigwedge^\bullet\mathbb C^r\), let \(a_j\) mean exterior multiplication and \(b_j\) contraction. They satisfy \(\{a_j,b_k\}=\delta_{jk}\), \(\{a_j,a_k\}=\{b_j,b_k\}=0\). The Hermitian operators
\[
\Gamma_{2j-1}=a_j+b_j,\qquad
\Gamma_{2j}=i(a_j-b_j),\qquad
\Gamma_{2r+1}=(-1)^{\deg}
\]
satisfy \(\{\Gamma_k,\Gamma_\ell\}=2\delta_{k\ell}\). Restricting this Clifford action to the spin group defines its representation on \(S\). Orient the rotation planes so that a lifted angle \(\theta_j\) acts by
\[
\exp\!\left(\frac{\theta_j}{2}\Gamma_{2j-1}\Gamma_{2j}\right)
=\exp\!\left(i\theta_j(\tfrac12-N_j)\right),\qquad N_j=a_jb_j. \tag{5.2}
\]
The occupation basis therefore has all \(2^r\) weights \((\pm\tfrac12,\ldots,\pm\tfrac12)\), each once. The vacuum has the largest weight \(\omega_r\) for the positive \(B_r\) roots and is a highest vector. The representation is irreducible: any invariant subspace decomposes into these distinct torus weight lines, and the bivector combinations \(a_j\Gamma_{2r+1}\), \(b_j\Gamma_{2r+1}\) connect every occupation vector to every other by adding or removing one index. A nonzero invariant subspace thus contains the entire basis.

At \(\theta_j=2\pi\), (5.2) is \(-I\). The lift ends at the nontrivial kernel element, whereas the \(SO\) rotation is the identity. Hence the spin representation does not descend to \(SO(2r+1)\).

Here
\[
\rho=(r-\tfrac12,r-\tfrac32,\ldots,\tfrac12)\notin X^*(T).
\]
It is a distinct highest weight from \(\omega_r\) when \(r>1\). It is realized on the spin cover: tensor the spin highest vector with the highest wedge vectors of degrees \(1,\ldots,r-1\) in the defining orthogonal representation. For a chamber vector with strictly decreasing positive coordinates, each wedge vector maximizes its weight evaluation among all wedges of defining weights \(\pm e_i,0\); (2.3) therefore kills it by every positive root operator. Their total weight is
\(\omega_r+\sum_{k=1}^{r-1}(e_1+\cdots+e_k)=\rho\), and positive root operators kill the tensor. Its cyclic subrepresentation is irreducible: complete reducibility projects this highest vector to highest vectors of the same weight in all contributing irreducibles; Lemma 2.4 leaves only one highest line. The central kernel acts as minus one on this tensor as well, so it too cannot descend. Saying that \(\rho\) fails to descend should not identify it with the spin fundamental weight.

## Exercises with complete solutions

**Exercise 1 (easy).** Find all weights of the adjoint representation, including their multiplicities.

*Solution.* Complexify the real adjoint action. Its decomposition is
\[
\mathfrak g_{\mathbb C}
=\mathfrak t_{\mathbb C}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
\]
The torus fixes \(\mathfrak t_{\mathbb C}\) and acts on \(\mathfrak g_\alpha\) by its root character. Root multiplicity one was proved in lesson seven. Thus every root has multiplicity one, and zero has multiplicity \(\dim T\); the dimension check is \(\dim G=\dim T+|\Phi|\). When there are no roots, the adjoint representation is entirely trivial. Connectedness and maximality are used to identify the zero space, not an assumption that the group is semisimple.

**Exercise 2 (medium).** Prove the analytic-weight distinction between \(SU(2)\) and \(SO(3)\), and verify the lattice equalities for \(SU(n)\) and \(Sp(r)\).

*Solution.* The \(SU(2)\) torus has period \(2\pi\), so its character exponents are all integers \(m\). The positive adjoint root has exponent two, and its coroot pairing is \(m\), making dominance exactly \(m\geq0\). The quotient torus identifies angles differing by \(\pi\). Descending requires \(e^{im\pi}=1\), hence even \(m\). The representation \(\operatorname{Sym}^m\mathbb C^2\) has central value \((-1)^m\), proving both realization and the obstruction.

For \(SU(n)\), the integer sum-zero period lattice is generated by the vectors \(e_i-e_n\), \(i<n\). Its dual consists of sum-zero vectors whose coordinate differences are integers. The root coroots impose these identical conditions, proving \(X^*(T)=P\). For \(Sp(r)\), periods are independent integer coordinates; the long-root coroots \(e_i\) already force the entire weight to lie in \(\mathbb Z^r\). The other coroots pair integrally with that lattice, so again equality holds. Coroot integrality alone cannot be substituted for the quotient-period check in the orthogonal example.

**Exercise 3 (medium).** Find all fundamental highest weights and their representations for \(SU(n)\).

*Solution.* With \(\alpha_i=e_i-e_{i+1}\), solve \(a_i-a_{i+1}=\delta_{ik}\) and \(\sum_i a_i=0\). The unique solution is (4.3): its first \(k\) entries are \(1-k/n\), and its last \(n-k\) entries are \(-k/n\). The character of the line \(e_1\wedge\cdots\wedge e_k\) is the product of the first \(k\) torus coordinates. Upper matrix units kill it by the repeated-factor argument, so it is a highest vector of weight \(\omega_k\). Lesson nine proves the exterior-power representation irreducible, and its restriction remains irreducible. Therefore the fundamental representations are precisely \(\bigwedge^k\mathbb C^n\), \(1\leq k<n\), of dimensions \(\binom nk\). The two endpoints \(k=0,n\) are trivial and are not additional fundamental representations. The highest-weight uniqueness theorem rules out any different irreducible with one of these weights.

**Exercise 4 (hard).** Prove uniqueness of an irreducible representation from its highest weight using a subrepresentation of a direct sum.

*Solution.* Given \(V_1,V_2\) with highest vectors \(v_1,v_2\) of the same weight, generate \(M\) from \((v_1,v_2)\) by the complexified Lie algebra. Connectedness turns its Lie invariance into \(G\)-invariance. PBW ordering shows its highest-weight space is exactly the diagonal line \(\mathbb C(v_1,v_2)\). Both coordinate projections are surjective because their images contain the nonzero highest vector.

If the second projection had a nonzero kernel, that kernel would be a nonzero invariant subspace of \(V_1\oplus0\), hence the entire first summand. It would contain \((v_1,0)\), a second independent vector of the highest weight, which is impossible. Its kernel is therefore zero. Interchanging the factors proves the first projection is also injective. Both projections are group isomorphisms, and composing their inverse and forward maps gives an equivalence. This argument proves compatibility of all lowering relations without assuming that a proposed word-by-word map is well defined.

## Source comparisons

Milne Section 22a gives the split-reductive algebraic counterpart: Proposition 22.17, Theorems 22.18–22.20 and the torus/central-isogeny distinctions in 22.8–22.12. Milne's algebraic existence proof is not a proof of our compact analytic existence statement; that will be supplied next. PBW spanning and the Clifford double cover are declared imports, with their scope specified above.

The tensor subspace in Remark 2 of Section 3.4.2 retains the antisymmetry in each fixed exterior-power factor: the diagonal Lie action commutes with those permutations. A different Young-symmetrizer realization can change its embedding into the full tensor power. Also the symplectic fundamental representations are generally summands of exterior powers, not the entire exterior powers as the opening of item 5 suggests. The following \(sp(4)\) example in the same source makes the correction explicit: \(\bigwedge^2\mathbb C^4\) has dimension six and contains an invariant line; its fundamental summand has dimension five. None of these qualifications changes the compact highest-weight theorem proved here.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §27. Its highest-weight character argument is an algebraic comparison for the representation-theoretic setting. The global character lattice, analytic existence and explicit spin-cover construction are proved here, with exact PBW and root-system providers.
