# States, ideals and the smallest tensor norm

*Self-checked by the writing AI. Original text: CC0 1.0.*

The spatial tensor norm has a concrete operator formula. Its minimality is a different assertion: every C*-norm on the same algebraic tensor product must dominate that formula. The difficulty is that a positive algebraic product functional need not be continuous for an arbitrary norm merely because it is continuous for the maximal one.

We will resolve this using pure states and ideals. Along the way, the same tools explain why tensor products of simple algebras are simple and why a pure state can still describe an entangled pair of systems.

Read [Tensor norms and independent systems](../reader/tensor-norms-and-independent-systems.html) first. The further proof inputs are [pure-state GNS irreducibility and enough pure states](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#OA-FND-GN-10), [unitary strong-* density](../../foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#OA-FND-KD-10), the [compact-convex barycentre construction and extreme-point criterion](../../foundations-of-von-neumann-algebras/integral-representations-of-states.html#OA-FND-IR-04), and [spatial tensor closure and operator matrices](../reader/supplements/spatial-tensor-products.html#5-the-spatial-tensor-product). State extension uses Hahn–Banach and the [compact-convex Krein–Milman proof](../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-06), under the stated programme background assumptions.

Freely readable treatments are Courtney, Gillaspy and Ismert’s *Notes on C\*-algebras* and Blackadar’s *Operator Algebras*. Sections 1–3 and 5 supply the full minimality and unitization arguments, including both directions of the pure-set/ideal correspondence. Inner products are linear in the first variable. Until Section 5, algebras are unital and nonzero. Pure-state spaces carry their relative weak-* topologies.

## 1. A commutative factor leaves no choice of norm

We begin with a fact about two commutative algebras. It gives the elementary-tensor estimate needed later without assuming minimality.

**Lemma 1.1.** Every C*-norm on \(C(X)\odot C(Y)\), for compact Hausdorff spaces \(X,Y\), is the supremum norm of the corresponding function on \(X\times Y\).

**Proof.** Complete for the given norm to obtain a commutative C*-algebra \(E=C(Z)\). Restriction of a character of \(E\) to the two unital subalgebras gives a point of \(X\times Y\). Thus \(Z\) has a continuous map into \(X\times Y\), with compact image \(F\), and the norm of an algebraic tensor is its supremum on \(F\).

If \(F\ne X\times Y\), its complement contains a nonempty open rectangle \(U\times V\). Choose nonzero continuous functions supported in \(U\) and \(V\). Their elementary tensor is a nonzero algebraic tensor but vanishes on \(F\), contradicting that the given seminorm is a norm. Hence \(F=X\times Y\). \(\square\)

**Corollary 1.2.** Every C*-norm \(\gamma\) on \(A\odot B\) is a cross norm.

**Proof.** Its restriction to \(C^*(1,a^*a)\odot C^*(1,b^*b)\) is a C*-norm, so Lemma 1.1 gives
\[
\|a\otimes b\|_\gamma^2
=\|a^*a\otimes b^*b\|_\gamma
=\|a^*a\|\|b^*b\|.
\]
The inclusions of the two factors into the completion are faithful: their restrictions are injective \*-homomorphisms of C\*-algebras, hence isometric. This justifies using the original spectra in Lemma 1.1. \(\square\)

**Theorem 1.3.** If \(X\) is compact Hausdorff and \(B\) is a C*-algebra, then
\[
C(X)\otimes_{\max}B=C(X)\otimes_{\min}B=C(X,B)
\tag{1.1}
\]
canonically. Every C*-norm on \(C(X)\odot B\) is this norm.

**Proof.** For \(x=\sum_{j=1}^r f_j\otimes b_j\), put \(F(t)=\sum_j f_j(t)b_j\). Its spatial norm is \(\sup_t\|F(t)\|\), by taking the direct sum of point evaluations on \(C(X)\) and a faithful representation of \(B\).

Given \(\varepsilon>0\), choose a finite open cover and subordinate continuous partition of unity \(h_1,\ldots,h_m\), with points \(t_k\) in the cover, so that
\[
\Big\|f_j-\sum_k f_j(t_k)h_k\Big\|<\varepsilon
\qquad(1\le j\le r).
\]
The maps \(u:C(X)\to\mathbb C^m\), \(u(f)=(f(t_k))_k\), and \(v:\mathbb C^m\to C(X)\), \(v(c)=\sum_k c_kh_k\), are unital completely positive: their matrix amplifications are pointwise positive, and \(u\) is a *-homomorphism. The direct product \(\mathbb C^m\odot B=B^m\) has a unique C*-norm, the largest coordinate norm. Indeed the coordinate embeddings are isometric *-homomorphisms, their units are orthogonal central projections, and the norm of a block-diagonal element is the largest block norm.

The commuting-map part of Theorem 4.1 of *Tensor norms and independent systems*, applied inside \(C(X)\otimes_{\max}B\), makes \(v\otimes\mathrm{id}\) contractive for the maximal norms. Consequently
\[
\Big\|\sum_k h_k\otimes F(t_k)\Big\|_{\max}
\le\max_k\|F(t_k)\|.
\]
The projective upper bound shows that this tensor sum tends to \(x\) in the maximal norm as \(\varepsilon\to0\). Hence \(\|x\|_{\max}\le\sup_t\|F(t)\|\), proving (1.1). Partitions of unity also approximate every continuous \(B\)-valued function uniformly by finite tensor sums, so the completion is all of \(C(X,B)\).

Now let \(q:C(X,B)\to E\) be the quotient associated to an arbitrary C*-norm \(\gamma\). Suppose \(0\ne F\in\ker q\). Choose \(t_0\) and \(\delta>0\) with \(\|F(t_0)\|>4\delta\), and an algebraic \(x\) with \(\|x-F\|_\infty<\delta\). Continuity gives a neighborhood \(U\) of \(t_0\) on which \(\|x(t)-x(t_0)\|<\delta\). Choose \(h\in C(X)\), \(0\le h\le1\), \(h(t_0)=1\), supported in \(U\). Then
\[
\|q(hx)\|<\delta,
\qquad
\|q(hx-h\otimes x(t_0))\|<\delta.
\]
But Corollary 1.2 gives \(\|q(h\otimes x(t_0))\|=\|x(t_0)\|>3\delta\), a contradiction. Thus \(q\) is injective. \(\square\)

## 2. Closed collections of pure states describe ideals

For a state \(\varphi\) and unitary \(u\in A\), write \(\varphi^u(a)=\varphi(u^*au)\). This action changes the cyclic vector in a representation.

**Lemma 2.1.** Let \(K\) be a relatively weak-* closed subset of \(P(A)\), invariant under \(\varphi\mapsto\varphi^u\). Then
\[
J_K=\{a\in A:\varphi(a)=0\text{ for all }\varphi\in K\}
\]
is a closed two-sided ideal, and
\[
K=\{\varphi\in P(A):\varphi(J_K)=0\}.
\tag{2.1}
\]
Conversely every closed ideal is recovered in this way from its pure-state annihilator.

**Proof.** The cases \(K=\varnothing\) and \(K=P(A)\) allow \(J_K=A\) and \(J_K=0\). In general let \(\Pi=\bigoplus_{\varphi\in K}\pi_\varphi\). If \(a\in J_K\), then
\[
\langle\pi_\varphi(a)\pi_\varphi(u)\xi_\varphi,
\pi_\varphi(u)\xi_\varphi\rangle=0
\quad(u\in U(A)).
\]
Each \(\pi_\varphi\) is irreducible. The unitary density theorem implies that these unitary orbit vectors are dense in its unit sphere. Its proof uses exponentials of self-adjoint elements in the concrete image; those elements have self-adjoint lifts in \(A\), so the approximating unitaries can be chosen as images of unitaries of \(A\). By continuity and polarization, \(\pi_\varphi(a)=0\). Therefore \(J_K=\ker\Pi\), an ideal.

Regard \(K\) as a collection of states of \(A/J_K\). For a self-adjoint quotient element \(a\), faithfulness of \(\Pi\) and the same unitary density show
\[
\max\operatorname{spec}(a)=\sup_{\varphi\in K}\varphi(a).
\]
Hahn–Banach separation now says that the closed convex hull of \(K\) is the whole state space of \(A/J_K\).

We spell out the compact-convex step. If a compact subset \(L\) of a compact convex set has that set as its closed convex hull, every extreme point belongs to \(L\). Finite convex combinations from \(L\) define probability measures on \(L\); take a weak-* cluster measure whose barycentre is the chosen extreme point. If a continuous affine function has a nonconstant value on a set of positive measure, splitting the measure above and below an intermediate value expresses that barycentre as a proper convex combination of two different barycentres. Extremality forbids this. Hence every continuous affine function equals its value at the extreme point almost everywhere. If the point were outside \(L\), finitely many such functions would, by compactness of \(L\) and separation of points, distinguish it from every point of \(L\); the preceding almost-everywhere conclusions would then contradict total mass one.

Apply this with \(L\) the compact weak-* closure of \(K\) in the quotient state space. Every pure quotient state lies in \(L\). Its pullback is a pure state of \(A\), so relative closedness of \(K\) puts it in \(K\). This proves (2.1). Finally, pure states of a quotient separate its elements, because their irreducible GNS representations form a faithful family. Thus an ideal is recovered from its annihilator. \(\square\)

**Lemma 2.2.** Let \(A\subseteq C\) be a unital C*-subalgebra. If a state \(w\) of \(C\) restricts to a pure state \(\varphi\) of \(A\), then
\[
w(ab)=\varphi(a)w(b)
\qquad(a\in A,\ b\in A'\cap C).
\tag{2.2}
\]

**Proof.** For a positive contraction \(b\) in the relative commutant, \(a\mapsto w(ab)\) and \(a\mapsto w(a(1-b))\) are positive and sum to \(\varphi\). Purity means each is a scalar multiple of \(\varphi\); evaluating at \(1\) gives those scalars. The endpoint cases with one scalar zero follow as well: a positive functional of norm zero is zero. Every element of the relative commutant is a linear combination of positive contractions, so (2.2) follows. \(\square\)

A pure state of a unital subalgebra has a pure extension: norm-preserving Hahn–Banach gives a state extension, and the extensions form a nonempty compact face of the state space. An extreme point of that face is extreme in the whole state space. This uses only the compactness and Krein–Milman theorem stated in *Representations and positive functionals*.

## 3. The lower bound for every C*-norm

**Theorem 3.1 (Takesaki's minimality theorem).** For any C*-norm \(\gamma\) on \(A\odot B\),
\[
\|x\|_{\min}\le\|x\|_\gamma\le\|x\|_{\max}.
\tag{3.1}
\]

**Proof.** The upper bound follows by faithfully representing the \(\gamma\)-completion and applying Theorem 1.1 of *Tensor norms and independent systems*. For the lower bound, let
\[
S=\{(\varphi,\psi)\in P(A)\times P(B):
\varphi\otimes\psi\text{ is }\gamma\text{-continuous}\}.
\]
A continuous product state has norm one in the completion. Thus \(S\) is relatively closed: pointwise limits preserve the inequalities \(|(\varphi\otimes\psi)(x)|\le\|x\|_\gamma\) for every algebraic \(x\). Conjugation by \(u\otimes v\) shows invariance under independent unitary conjugations.

Suppose \(S\) is proper. Its complement contains a nonempty open rectangle \(U\times V\). Enlarge \(U,V\) separately by their unitary translates; the enlarged rectangle still misses \(S\), because \(S\) is invariant. Put \(K_A=P(A)\setminus U\), \(K_B=P(B)\setminus V\). Lemma 2.1 supplies nonzero ideals \(J_A,J_B\) with these annihilators. Choose nonzero positive \(a\in J_A,b\in J_B\). Every pair in \(S\) belongs to \((K_A\times P(B))\cup(P(A)\times K_B)\), so every such product state vanishes at \(a\otimes b\).

Let \(C=C^*(1,a)\subseteq A\). The restriction of \(\gamma\) to \(C\odot B\) is a C*-norm. Theorem 1.3 identifies its completion with \(C\otimes_{\min}B\). Choose a character \(\chi\) of \(C\) with \(\chi(a)>0\), and a pure state \(\psi\) of \(B\) with \(\psi(b)>0\). The state \(\chi\otimes\psi\) is pure: its GNS representation is the irreducible representation \(\pi_\psi\) multiplied by the character \(\chi\). Extend it to a pure state \(w\) of the \(\gamma\)-completion.

Its restriction to \(B\) is the pure state \(\psi\). Lemma 2.2 therefore gives \(w=\varphi\otimes\psi\) on algebraic tensors, where \(\varphi=w|_A\). This \(\varphi\) is pure. Otherwise a proper decomposition of \(\varphi\) would decompose \(w\): each positive summand is dominated by a scalar multiple of \(\varphi\), hence its product functional is dominated on algebraic positive squares by the same scalar multiple of \(w\). Algebraic Cauchy–Schwarz then makes those summands continuous for \(\gamma\), so they extend to states. This contradicts purity of \(w\).

Thus \((\varphi,\psi)\in S\), but
\[
(\varphi\otimes\psi)(a\otimes b)=\chi(a)\psi(b)>0,
\]
a contradiction. Hence \(S=P(A)\times P(B)\).

The direct sum of all pure-state GNS representations is faithful in each factor. Its spatial tensor representation computes \(\|\cdot\|_{\min}\) by Theorem 3.1 of *Tensor norms and independent systems*. Every block is the GNS representation of one product pure state, by (3.1) there. These states extend to the \(\gamma\)-completion, so their GNS representations are contractive for \(\gamma\). Taking the supremum over blocks proves the lower bound. \(\square\)

The proof also shows that every product of pure states is continuous for every C*-norm. Arbitrary product states have the same property, by weak-* approximation with finite convex combinations of pure states and the norm-one inequalities.

## 4. Pure states and entanglement

**Proposition 4.1.** If \(\pi:A\to B(H)\) and \(\sigma:B\to B(K)\) are nondegenerate, then
\[
(\pi\otimes\sigma)(A\otimes_{\min}B)''
=\pi(A)''\bar\otimes\sigma(B)''.
\tag{4.1}
\]
If both representations are irreducible, their tensor representation is irreducible.

**Proof.** The approximate identities in the two factors show that the left side contains \(\pi(a)\otimes1\) and \(1\otimes\sigma(b)\). Bounded strong approximation then puts \(\pi(A)''\otimes1\) and \(1\otimes\sigma(B)''\) in it. Conversely every algebraic tensor, and hence the norm closure of their span, lies in the right side. Taking weak closures proves equality. If the factors are irreducible, the right side is \(B(H)\bar\otimes B(K)=B(H\otimes K)\). \(\square\)

**Theorem 4.2.** The following conditions are equivalent:

1. At least one of \(A,B\) is commutative.
2. Every pure state of \(A\otimes_{\min}B\) is a product of pure states.
3. The minimal C*-norm equals the Banach injective norm
   \[
   \lambda(x)=\sup_{\|f\|,\|g\|\le1}|(f\otimes g)(x)|.
   \]

**Proof.** If \(A\) is commutative, it is central in the tensor product. In an irreducible representation central elements are scalar, so a pure state's restriction to \(A\) is a character. Lemma 2.2 gives a product decomposition, and its other factor is pure by the domination argument in Theorem 3.1.

If both algebras are noncommutative, each has an irreducible representation of dimension at least two. Otherwise their faithful family of irreducible representations would all be one-dimensional, forcing all commutators to vanish. Choose orthonormal vectors \(e_1,e_2\in H\), \(f_1,f_2\in K\), and put
\[
\zeta=\sqrt{2/3}\,e_1\otimes f_1+\sqrt{1/3}\,e_2\otimes f_2.
\]
Its vector state is pure by Proposition 4.1. If it were a product, all its mixed expectations would factor. Bounded strong density would give the same factorization for all operators in \(B(H)\) and \(B(K)\). But the rank-one projections onto \(e_1\) and \(f_2\) have joint expectation zero and marginal expectations \(2/3\) and \(1/3\), whose product is \(2/9\). Thus the state is not a product. This proves equivalence of 1 and 2.

When \(A=C(X)\), Theorem 1.3 gives \(\|x\|_{\min}=\sup_t\|x(t)\|\). Evaluation at \(t\) followed by a norm-one functional of \(B\) gives \(\lambda(x)\ge\sup_t\|x(t)\|\); the reverse inequality follows from the vector-functional realization (4.1) in *Tensor norms and independent systems*. Hence 1 implies 3.

Finally assume 3. The set
\[
L=\{f\otimes g:\|f\|,\|g\|\le1\}
\]
is weak-* compact in the dual of the minimal tensor product. Continuity of the product map first holds on algebraic tensors and extends uniformly to all elements by the uniform norm bound. Condition 3 and Hahn–Banach separation make the dual unit ball the closed convex hull of \(L\); balance is already included in \(L\). The compact-convex fact proved in Lemma 2.1 puts every extreme point of that ball in \(L\). A pure state is such an extreme point: a decomposition in the dual ball restricts, by evaluation at the unit and the norm bound, to a decomposition into states.

Thus every pure state is \(f\otimes g\) with \(\|f\|,\|g\|\le1\). Its value one at the unit implies \(|f(1)|=|g(1)|=1\). Rescale the two factors by opposite phases to make both values one. Norm-one unital functionals are states, and purity of the product forces purity of both factors. Hence 3 implies 2. \(\square\)

## 5. Removing units without changing the result

**Lemma 5.1.** Any C*-norm \(\gamma\) on \(A\odot B\) extends to a C*-norm on \(\widetilde A\odot\widetilde B\), where a unit is adjoined only to a factor that lacks one.

**Proof.** Faithfully and nondegenerately represent the \(\gamma\)-completion. Recover its commuting representations by Theorem 1.1 of *Tensor norms and independent systems*, and extend each by sending its new unit to the identity. Their product representation \(R\) extends the original one.

We must verify that it is algebraically faithful. The ideal \(A\odot B\) is an essential algebraic ideal in \(\widetilde A\odot\widetilde B\). Here is the needed justification. If a finite tensor \(z\) annihilates \(A\odot B\), choose finite linearly independent presentations of its coefficients. The maps \(a\mapsto ca\) from \(A\) to \(A\), with \(c\in\widetilde A\), distinguish the coefficients: a coefficient annihilating every \(a\) is zero, since an approximate identity tends to the identity in the multiplier action. The analogous maps in the other factor have the same property. On each finite-dimensional coefficient space finitely many of these evaluation maps jointly are injective. Their tensor products are jointly injective, so \(z=0\).

If \(R(z)=0\), then \(R(zw)=0\) for every \(w\in A\odot B\). Original faithfulness gives \(zw=0\); essentiality gives \(z=0\). Thus \(\|R(z)\|\) is the required extended norm. \(\square\)

Applying the unital minimality theorem to this extension and restricting gives (3.1) for arbitrary C*-algebras. The minimal norm on the unitized pair restricts to the original minimal norm by injectivity of minimal tensoring. The maximal norm also restricts to the original one: every commuting representation extends to the unitizations on its active support, and restriction of a commuting representation gives the opposite inequality.

Theorem 4.2 also holds for nonzero nonunital algebras. A pure state has a unique unital extension to its unitization, with the same irreducible GNS representation. Product representations extend similarly. The central-character argument and the entangled-vector argument apply in those representations. For the Banach norm, unitization is not needed: \(C_0(X)\otimes_{\min}B=C_0(X,B)\) follows by restricting (1.1) and using compactly supported partitions of unity, and its supremum norm is \(\lambda\).

For the converse, a pure state is still extreme in the dual unit ball. Indeed, if \(\omega=(f+g)/2\) with \(\|f\|,\|g\|\le1\), a positive approximate identity satisfies \(\omega(e_i)\to1\), which forces \(f(e_i),g(e_i)\to1\). Realize \(f\) by vectors with product of norms \(\|f\|\), as in (4.1) of *Tensor norms and independent systems*. The limit of \(f(e_i)\) is their inner product. Equality in Cauchy–Schwarz makes that functional positive of norm one; the same holds for \(g\). Purity then gives \(f=g=\omega\). The compact dual-ball argument therefore expresses \(\omega=f_1\otimes f_2\). Positivity on elementary positive tensors makes the two factors positive after opposite phase rescalings: fix a positive element on which one factor is nonzero to determine the phase of the other, then reverse the roles. Formula (4.1) gives \(\|f_1\|\|f_2\|=1\); rescale by opposite positive constants to make both norms one. They are states, and purity forces both to be pure.

## 6. Exercises with solutions

**Exercise 6.1 (first step).** Let \(A=C([0,2])\) and let \(K\) consist of evaluations at points of \([0,1]\). Compute \(J_K\). What happens if \(K\) contains evaluations only at rational points of \([0,1]\)?

**Solution.** The ideal is \(\{f:f|_{[0,1]}=0\}\). Evaluations are the pure states and unitary conjugation acts trivially. For the rational set the same ideal is obtained by continuity, but the pure-state annihilator is all evaluations in \([0,1]\), not only the rational ones. Relative closedness in Lemma 2.1 is therefore necessary.

**Exercise 6.2 (application).** In \(M_2\otimes M_2\), use \(\zeta=\sqrt{2/3}\,e_1\otimes e_1+\sqrt{1/3}\,e_2\otimes e_2\). Compute both marginal density matrices and the covariance of \(e_{11}\otimes1\) and \(1\otimes e_{22}\). Is the joint state pure?

**Solution.** Each marginal density matrix is \(\operatorname{diag}(2/3,1/3)\), hence mixed. The product of the indicated observables has expectation zero, while their marginal expectations are \(2/3\) and \(1/3\). Their covariance is \(-2/9\). The joint density matrix is the rank-one projection onto \(\zeta\), so the joint state is pure. Purity of a joint state does not imply purity of its restrictions.

**Exercise 6.3 (further step).** Let \(A=C_0(\mathbb R)\), \(B=M_2\), and
\[
x(t)=\begin{pmatrix}e^{-t^2}&0\\0&2e^{-(t-1)^2}\end{pmatrix}.
\]
Compute its tensor norm and exhibit a product state that attains it. Explain why adding a unit to \(A\) does not change this norm.

**Solution.** The norm is \(\sup_t\max\{e^{-t^2},2e^{-(t-1)^2}\}=2\). Evaluation at \(t=1\), paired with the vector state of \(e_2\), gives value two. The function extends continuously by zero to the one-point compactification, so the same supremum norm computes it inside the unitization. Minimal tensoring preserves that inclusion isometrically.

## References

- [Courtney–Gillaspy–Ismert] K. Courtney, E. Gillaspy and L. Ismert, *Notes on C\*-algebras*, GOALS lecture notes, available from [IPAM, UCLA](https://www.ipam.ucla.edu/wp-content/uploads/2024/07/Notes_and_Exercises_for_GOALS.pdf).
- [Kadison] R. V. Kadison, [“Irreducible operator algebras,”](https://pmc.ncbi.nlm.nih.gov/articles/PMC528430/) *Proceedings of the National Academy of Sciences of the United States of America* **43** (1957), 273–276.
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, freely accessible corrected manuscript, [author's PDF](https://bruceblackadar.com/Mathematics/Cycr.pdf).
