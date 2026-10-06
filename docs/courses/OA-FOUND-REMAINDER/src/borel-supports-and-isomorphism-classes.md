# Borel supports and isomorphism classes

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

To choose a projection measurably, it helps to describe its range by countably many vectors. This simple method makes supports and central carriers Borel as the algebra varies. We then use a Borel choice from closed cosets to prove that each fixed unitary equivalence class of von Neumann algebras is Borel. Infinite amplification gives the corresponding result for each fixed abstract isomorphism class.

Our fixed Hilbert space \(H\) is infinite dimensional and separable. Write \(\mathcal V(H)\) for the unital von Neumann subalgebras of \(B(H)\), with the Effros Borel structure, and \(\mathcal P(H)\) for the projections with the strong operator Borel structure. We use [The Effros Borel structure](../reader/supplements/effros-borel-structure.html), particularly Theorems 5.3, 6.1, 8.2, 9.1 and 10.3 and the unitary-conjugation exercise. These prove standardness, dense Borel choices, measurable closed spans, and Borel algebra operations. The injective Borel image theorem is Theorem 4.3 of [Polish spaces and standard Borel spaces](../../foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces.html).

For amplification we use Theorem 4.1 of [Multiplicity](../reader/supplements/normal-representation-comparison.html): two faithful normal representations whose commutants are sigma-finite and properly infinite are unitarily equivalent. Its full projection-comparison proof applies here. [Spatial tensor products](../reader/supplements/spatial-tensor-products.html) supplies the normal tensor representation and commutant formula; the formula also follows directly from operator matrix entries in Lemma 8.2 of [Projections and types](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html). Normal positive functionals have positive vector expansions by Theorem 10.1 of [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html). Normality of isomorphisms is proved in Corollary 11.4 of [The universal enveloping algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html).

The linked programme lessons supply the complete prerequisites for these constructions. Effros’s freely readable paper develops fixed-space Borel coding, dense choices and commutants. Takesaki’s book and the further works listed below provide scholarly context for reduction theory.

## 1. Countable choices and measurable ranges

The Effros lesson supplies Borel choices dense in the unit ball of every algebra for the weak-star topology. Taking all rational convex combinations gives a sequence
\[
a_n:\mathcal V(H)\longrightarrow B(H)_1
\]
which is dense in \(M_1\) for the strong-star topology, for every \(M\). Here the rational coefficients are nonnegative and sum to one. The reason is the equality of weak and strong-star closures of convex bounded sets: the real continuous linear functionals for the strong-star topology are finite sums of vector coefficients of \(x\) and \(x^*\), hence are weak-operator continuous. A Hahn–Banach separation argument gives the equality. The weak-star-dense choices and their convex combinations therefore have the required closure.

On a bounded operator ball, the Borel structures of the weak, strong and strong-star topologies agree. Indeed a countable dense set of vectors supplies their coordinates, weak coordinates determine the norm of each image through a supremum over countably many scalar coordinates, and adjoint coordinates are obtained by reversing and conjugating the weak coordinates. We use the strong-star structure when multiplying operators.

The correspondence
\[
p\longmapsto pH
\tag{1.1}
\]
is a Borel isomorphism between \(\mathcal P(H)\) and the Effros space of closed subspaces of \(H\). This is exactly Theorem 6.1 of the Effros lesson, so we reuse its proof. In particular, if \((\xi_n(t))\) is a sequence of Borel \(H\)-valued maps, the projection onto their closed linear span is Borel in \(t\). One may compute it by measurable Gram–Schmidt, discarding zero residual vectors; the projection is the strong limit of the resulting finite-rank projections.

## 2. The least projection belonging to an algebra

For \(M\in\mathcal V(H)\) and \(p\in\mathcal P(H)\), define
\[
e_M(p)=\text{the projection onto }[M'pH].
\tag{2.1}
\]
It is the smallest projection of \(M\) majorizing \(p\).

To verify this, the closed subspace in (2.1) is invariant under \(M'\) and its adjoints, so its projection belongs to \(M''=M\). It contains \(pH\). If \(q\in M\) is a projection with \(q\geq p\), then \(q\) commutes with \(M'\), so \(M'pH\subseteq qH\), and hence \(e_M(p)\leq q\).

**Proposition 2.1.** The map \((M,p)\mapsto e_M(p)\) is Borel.

**Proof.** The commutant map \(M\mapsto M'\) is Borel by the Effros theorem. Fix a countable norm-dense set \((\eta_k)\subset H\). Then
\[
[M'pH]=[a_n(M')p\eta_k:n,k\geq1].
\tag{2.2}
\]
For the inclusion from right to left, every displayed vector belongs to \(M'pH\). For the reverse inclusion, first approximate a vector of \(pH\) by \(p\eta_k\), then approximate an element of \(M'_1\) strongly by the \(a_n(M')\). Scalar multiples handle arbitrary elements of \(M'\). Each vector in (2.2) is jointly Borel in \((M,p)\), since multiplication and evaluation are continuous on bounded strong-star balls. Apply the measurable-span result in Section 1. \(\square\)

When \(p\in M\), (2.1) is simply \(p\): \(p\) itself is the least majorant. A more interesting use lets the algebra be the centre. Its central carrier is
\[
c_M(p)=e_{Z(M)}(p)\qquad(p\in M).
\tag{2.3}
\]
The centre map is Borel:
\[
Z(M)=(M\vee M')',
\]
and the join and commutant maps are Borel. Thus the relation \(c_M(p)=1\) is a Borel condition on pairs with \(p\in M\). Membership \(p\in M\) is Borel as well: it means that \(p\) commutes with every \(a_n(M')\).

There are two different projection conditions here. The support of a state must equal \(1\) for the state to be faithful. Its central carrier can equal \(1\) even when its support is a proper projection; Exercise 6.2 gives a finite-dimensional calculation.

## 3. Supports of normal functionals

Identify a positive normal functional on \(B(H)\) with a positive trace-class operator \(D\):
\[
\varphi_D(x)=\operatorname{Tr}(Dx).
\]
The positive trace-class cone, with trace norm, is a standard Borel space. Its support projection is
\[
s(D)=\operatorname*{s\!-\!lim}_{m\to\infty}
D(D+m^{-1}1)^{-1}.
\tag{3.1}
\]
For each fixed \(m\), this operator is norm-continuous in \(D\) on the positive cone; trace-norm convergence implies operator-norm convergence, and the resolvent identity supplies continuity of the inverse. The strong limit in (3.1) makes \(D\mapsto s(D)\) Borel.

**Proposition 3.1.** The support of the restriction of \(\varphi_D\) to \(M\) is
\[
s(\varphi_D|_M)=e_M(s(D)).
\tag{3.2}
\]
Consequently it is jointly Borel in \((M,D)\), and faithfulness of the restriction is the Borel condition \(e_M(s(D))=1\).

**Proof.** For a projection \(q\in M\),
\[
\varphi_D(1-q)
=\|(1-q)D^{1/2}\|_{\mathrm{HS}}^2.
\]
It is zero exactly when the range of \(D^{1/2}\), hence its closure \(s(D)H\), is contained in \(qH\). The support of the restriction is the least such \(q\), which is (3.2). Borelness follows from (3.1) and Proposition 2.1. \(\square\)

Every positive normal functional on \(M\) is the restriction of some positive trace-class functional on \(B(H)\). In fact its positive vector expansion
\[
\varphi(x)=\sum_n\langle x\xi_n,\xi_n\rangle,
\qquad\sum_n\|\xi_n\|^2<\infty,
\]
gives the trace-norm-convergent positive series \(D=\sum_n|\xi_n\rangle\langle\xi_n|\). This observation allows normal states on varying algebras to be encoded in one fixed Polish space.

## 4. One Borel representative from each closed coset

We need a selection lemma in a form whose proof is independent of quotient topology.

**Lemma 4.1.** Let \(X\) be a Polish space. There is a Borel map selecting a point \(s(F)\in F\) from each nonempty closed set \(F\), when closed sets have the Effros structure.

**Proof.** Choose a complete compatible metric, a countable dense set of centres, and the countable family of open balls with positive rational radii. For each \(F\), choose the first ball \(B_1\) of radius less than \(1/2\) that meets \(F\). Inductively choose the first ball \(B_n\), of radius less than \(2^{-n}\), that meets \(F\) and whose closed ball is contained in the previously chosen open ball. Enforce the latter by the sufficient inequality
\[
d(\text{centre}(B_n),\text{centre}(B_{n-1}))
+\text{radius}(B_n)
<\text{radius}(B_{n-1}).
\]
Such a ball exists: choose a point of \(F\) in the preceding open ball, a sufficiently close dense centre and a small rational radius. Every choice is Borel, since “meets \(F\)” is an Effros generator and the containment inequality compares countably many fixed balls.

The centres form a Cauchy sequence and converge in \(X\). Their distances from the closed set \(F\) tend to zero, so their limit belongs to \(F\). Pointwise limits of Borel maps to a metric space are Borel. This limit is the required \(s(F)\). \(\square\)

**Corollary 4.2.** If \(L\) is a closed subgroup of a Polish group \(U\), there is a Borel subset \(C\subseteq U\) meeting every coset \(uL\) in exactly one point. The same holds for cosets \(Lu\).

**Proof.** The closed-set map \(u\mapsto uL\) is Effros-Borel. For an open \(O\subseteq U\),
\[
uL\cap O\ne\varnothing
\quad\Longleftrightarrow\quad u\in OL^{-1},
\]
and the latter set is open. Apply Lemma 4.1 and put \(t(u)=s(uL)\). This is Borel, belongs to \(uL\), and is constant on each coset. Hence
\[
C=\{u:t(u)=u\}
\]
is Borel and meets each coset once: \(t(u)\) is that point and \(t(t(u))=t(u)\). Inversion converts left cosets to right cosets and preserves Borelness. \(\square\)

## 5. Fixed equivalence classes are Borel

Fix \(M\in\mathcal V(H)\). Define its unitary class and abstract isomorphism class by
\[
\mathcal O_M=\{uMu^*:u\in\mathcal U(H)\},\qquad
\mathcal I_M=\{N\in\mathcal V(H):N\cong M\}.
\]
An isomorphism between von Neumann algebras is automatically normal, as proved in the universal-enveloping lesson.

**Theorem 5.1.** The set \(\mathcal O_M\) is Borel in \(\mathcal V(H)\).

**Proof.** The unitary group \(\mathcal U(H)\) is Polish in its strong-star topology. A complete metric is obtained from a countable dense family of vectors by recording both \(u\xi_k\) and \(u^*\xi_k\); a Cauchy limit preserves both unitary identities. It is separable as a subspace of a countable product of separable Hilbert spaces. On the unitary group, strong and strong-star topologies agree.

The stabilizer
\[
L_M=\{u:uMu^*=M\}
\]
is closed. If \(u_i\to u\) strongly-star and \(u_iMu_i^*=M\), then for every \(a\in M\), \(u_i a u_i^*\to uau^*\) strongly, so \(uau^*\in M\). Applying the same argument to the inverses gives equality.

Choose the Borel transversal \(C\) for cosets \(uL_M\) from Corollary 4.2. The map \(u\mapsto uMu^*\) is Borel by the Effros conjugation result, and is injective on \(C\): equal images mean \(v^*u\in L_M\), hence equal cosets and representatives. The injective Borel image theorem makes its image \(\mathcal O_M\) Borel. \(\square\)

**Theorem 5.2.** The set \(\mathcal I_M\) is Borel in \(\mathcal V(H)\).

**Proof.** Let \(K=H\otimes\ell^2(\mathbb N)\) and put
\[
\Phi(N)=N\otimes1\subseteq B(K).
\]
This is a Borel map into \(\mathcal V(K)\): the Borel choices \(a_n(N)\otimes1\) generate its image, and the Effros generation theorem applies. Its commutant is
\[
\Phi(N)'=N'\bar\otimes B(\ell^2(\mathbb N)).
\tag{5.1}
\]
It is sigma-finite because it acts on the separable Hilbert space \(K\). It is properly infinite, since the identity on the second factor has two orthogonal isometric copies.

If \(N\cong M\), this normal isomorphism identifies the two faithful normal amplified representations of the same abstract algebra. The multiplicity theorem, with (5.1), makes them spatially equivalent. Conversely spatial equivalence of \(\Phi(N)\) and \(\Phi(M)\) gives \(N\cong M\). Therefore
\[
\mathcal I_M=\Phi^{-1}(\mathcal O_{\Phi(M)}).
\]
Theorem 5.1 applies on \(K\) too; the right side is Borel. \(\square\)

These results describe each class for a fixed algebra. They do not supply a simultaneous Borel classification of all von Neumann algebras.

## 6. Exercises with solutions

**Exercise 6.1 — Basic: a pure state can become faithful on a subalgebra.** In \(H=\mathbb C^2\), let \(v=(1,1)/\sqrt2\), \(D=|v\rangle\langle v|\), and let \(A\) be the diagonal algebra. Compute \(s(D)\), \(e_A(s(D))\), and \(e_{M_2}(s(D))\). Which restrictions of \(\varphi_D\) are faithful?

**Solution.** The support \(s(D)\) is the rank-one projection onto \(\mathbb Cv\). The least diagonal projection containing that line is \(1\), since both coordinates of \(v\) are nonzero. Hence \(e_A(s(D))=1\); explicitly \(\varphi_D(\operatorname{diag}(a,b))=(a+b)/2\), a faithful state of \(A\). For \(M_2\), every projection is already in the algebra, so \(e_{M_2}(s(D))=s(D)<1\). The projection onto \(v^\perp\) is nonzero and has value zero; this restriction is not faithful.

**Exercise 6.2 — Intermediate: support versus central carrier.** Let \(M=M_2(\mathbb C)\oplus M_3(\mathbb C)\), and let \(\varphi\) be half the first-coordinate vector state on each summand. Find its support and central carrier. Does full central carrier imply faithfulness?

**Solution.** In the direct-sum representation,
\[
s(\varphi)=(e_{11}^{(2)},e_{11}^{(3)}).
\]
The centre consists of \((\lambda1_2,\mu1_3)\). Every central projection above this support has both coordinates equal to the corresponding identity, so \(c_M(s(\varphi))=1\). But, for example, \((e_{22}^{(2)},0)\) is positive, nonzero and annihilated by \(\varphi\). Full central carrier means that the associated normal representation has no central kernel; faithfulness of the functional itself requires support \(1\), which fails here.

**Exercise 6.3 — Advanced: an entangled vector and its Borel support.** Let \(H=\mathbb C^r\otimes\mathbb C^s\), \(M=M_r(\mathbb C)\otimes1_s\), and let a unit vector \(\xi\) have coefficient matrix \(V\in M_{r,s}(\mathbb C)\) in the product bases. Compute \(e_M(|\xi\rangle\langle\xi|)\), and determine when the vector state is faithful on \(M\). Specialize to \(\xi=(e_1\otimes f_1+e_2\otimes f_2)/\sqrt2\).

**Solution.** Direct expansion gives
\[
\langle(a\otimes1)\xi,\xi\rangle
=\operatorname{Tr}(aVV^*).
\]
Thus the restricted state has density \(VV^*\) on \(M_r\) and support \(s(VV^*)\otimes1_s\). Proposition 3.1 identifies this with \(e_M(|\xi\rangle\langle\xi|)\). It is faithful exactly when \(VV^*\) is invertible, or equivalently \(V\) has row rank \(r\); in particular this requires \(s\geq r\).

For the stated vector with \(r=s=2\), \(V=1_2/\sqrt2\), so \(VV^*=1_2/2\). Its restriction is the normalized trace and is faithful, despite the rank-one ambient support. The least majorant has rank four and equals the identity. Formula (3.1) also makes the support Borel as \(V\) varies, even when its rank drops.

## Historical setting

An abstract algebra and the multiplicity of its represented action are different pieces of information. Theorems 5.1–5.2 express that difference: fixed unitary classes use the represented algebra, whereas fixed abstract classes are recovered after identity amplification makes the commutant properly infinite. The full representation-comparison proof is in the multiplicity lesson, with both its proper-infiniteness and sigma-finiteness hypotheses.

Related constructions have their own proof locations. [Central averaging and maximal ideals](../reader/central-averaging-and-maximal-ideals.html) proves the norm-closed orbit-hull assertions. [Finite type II and separable representations](../reader/finite-type-ii-and-separable-representations.html) proves the automatic-normality result, and [Finite maximal quotients](../reader/finite-maximal-quotients.html) treats the finite quotient construction. The historical bibliography includes Feldman–Fell, Takesaki, Wright, Feldman and Misonou. Those identities are bibliographic context for the subjects; the proof inputs are the complete named lessons.

Effros's 1965 paper develops the Borel space on a fixed separable Hilbert space. Schwartz's *Type II factors in a central decomposition* and Nielsen's *Borel sets of von Neumann algebras* are further historical references. The full proofs of measurable type loci and fibre transfer used here are in [Borel types and fibre types](../reader/borel-types-and-fibre-types.html); their Borel and analytic conclusions retain their precise scope. [Crossed-product coefficients and factor tests](../reader/crossed-product-coefficients-and-factor-tests.html) and [Expected MASAs and factor types](../reader/expected-masas-and-factor-types.html) develop the factor examples separately.

The mathematical dependencies are supplied by the exact programme proof locators above.

## References

[Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer. The projection, Effros and multiplicity results cited above are the prerequisites for these Borel constructions.

- [Effros 1965] Edward G. Effros, [The Borel space of von Neumann algebras on a separable Hilbert space](https://msp.org/pjm/1965/15-4/pjm-v15-n4-p07-s.pdf), *Pacific Journal of Mathematics* 15(4) (1965), 1153–1164. Also, [Global structure in von Neumann algebras](https://doi.org/10.1090/S0002-9947-1966-0192360-9), *Transactions of the American Mathematical Society* 121 (1966), 434–454.
- J. T. Schwartz, [Type II factors in a central decomposition](https://doi.org/10.1002/cpa.3160160302), *Communications on Pure and Applied Mathematics* 16 (1963), 247–252.
- Ole A. Nielsen, [Borel sets of von Neumann algebras](https://doi.org/10.2307/2373648), *American Journal of Mathematics* 95 (1973), 145–164.
- J. Feldman and J. M. G. Fell, [Separable representations of rings of operators](https://doi.org/10.2307/1969960), *Annals of Mathematics* 65 (1957), 241–249.
- Masamichi Takesaki, [On the conjugate space of operator algebra](https://doi.org/10.2748/tmj/1178244713), *Tohoku Mathematical Journal* 10 (1958), 194–203; [On the non-separability of singular representation of operator algebra](https://doi.org/10.2996/kmj/1138844294), *Kodai Mathematical Seminar Reports* 12 (1960), 102–108.
- Fred B. Wright, [A reduction for algebras of finite type](https://doi.org/10.2307/1969851), *Annals of Mathematics* 60 (1954), 560–570; Jacob Feldman, [Embedding of AW*-algebras](https://doi.org/10.1215/S0012-7094-56-02329-8), *Duke Mathematical Journal* 23 (1956), 303–308.
- Yosinao Misonou, [On a weakly central operator algebra](https://doi.org/10.2748/tmj/1178245422), *Tohoku Mathematical Journal* 4 (1952), 194–202.

