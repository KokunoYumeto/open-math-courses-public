# Measurable equivalence and constant fibres

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

An isomorphism available at each point is useful in a direct integral only after it can be chosen measurably. A spatial isomorphism is described by a unitary. An abstract isomorphism may change the multiplicity of the representation, so it needs an amplification and a faithful compression before a unitary can describe it. We make both choices using countable operator equations.

Prerequisites are [Base changes and disintegration](../reader/base-changes-and-disintegration.html), [Measurable fields and direct integrals](../reader/supplements/measurable-fields-direct-integrals.html), and [The Effros Borel structure](../reader/supplements/effros-borel-structure.html). We use the measurable-section theorem, Theorem 7.7, and the injective Borel-image theorem, Theorem 4.3, of [Polish spaces and standard Borel spaces](../../foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces.html). For normal representations we use the complete amplification-and-induction proof in [Spatial tensor products](../reader/supplements/spatial-tensor-products.html), Theorem 8.2 and Proposition 6.1(2). The linked programme lessons contain the complete prerequisite proofs. Elliott’s freely readable paper treats the assembly of fibre equivalences, and Takesaki’s book provides further context. Here Lemma 1.1 and Theorems 2.1–3.1 give the full countable relations, both isomorphism directions and measurable inverse, under the standard sigma-finite base and separable-fibre hypotheses.

Throughout, \(X\) is a standard Borel space with a sigma-finite measure \(\mu\); measurability may be taken in its completion. All Hilbert fibres are separable. A von Neumann algebra on a nonzero fibre contains that fibre's identity. Zero Hilbert fibres are allowed. We work outside one common null set whenever countably many field identities are involved.

## 1. From operator equations to measurable choices

We first collect the precise form of the measurable machinery.

**Lemma 1.1.** Let \(Y\) be Polish and \(R\subseteq X\times Y\) Borel. If its sections
\[
R_x=\{y:(x,y)\in R\}
\]
are nonempty almost everywhere, there is a \(\mu\)-measurable choice \(s(x)\in R_x\) almost everywhere. It can be made Borel after deleting a Borel null set.

**Proof.** Apply the imported measurable-section theorem to the projection \(R\to X\). The Borel set \(R\) is a standard Borel space and hence has a compatible Polish realization. The theorem gives a selection on the projection of \(R\) that is measurable for the completed sigma-finite measure. Its domain contains a conull Borel subset of \(X\).

For clarity, a completed-measurable map into a Polish space has a Borel version almost everywhere. Choose, for each \(n\), a countable partition of the target into Borel sets of diameter at most \(2^{-n}\), refining the preceding partition. Replace all the inverse images by Borel representatives. Outside the union of their countably many null discrepancies, choose one target point in the cell containing the original value. These choices are Borel maps converging to that value; their limit, defined arbitrarily where convergence fails, is a Borel version. Delete also a Borel null envelope of any exceptional set. The selection identities hold on what remains. \(\square\)

Here are the operator spaces in which we use the lemma. On the unit ball of \(B(K)\), for separable \(K\) with dense sequence \((e_j)\), the metric
\[
d(s,t)=\sum_{j\geq1}2^{-j}
\left(
\frac{\|(s-t)e_j\|}{1+\|(s-t)e_j\|}
+\frac{\|(s^*-t^*)e_j\|}{1+\|(s^*-t^*)e_j\|}
\right)
\tag{1.1}
\]
defines the strong-star topology. This ball is Polish. Indeed, a Cauchy sequence has strong limits for both the operators and their adjoints; the limits are contractions, and the inner-product identity shows that they are adjoints. Separability follows by embedding the ball into the countable product of the separable spaces containing \((se_j,s^*e_j)\). On bounded sets, multiplication and adjoint are continuous in this topology. For multiplication use
\[
\|(s_nt_n-st)e_j\|
\leq\|s_n\|\,\|(t_n-t)e_j\|+\|(s_n-s)te_j\|,
\]
and apply the same argument to the adjoints. The unitary group is the closed subset given by \(u^*u=uu^*=1\), so it is Polish as well.

A measurable Hilbert field has measurable dimension strata. On each stratum a measurable orthonormal basis identifies the fibres with one fixed Hilbert space. There are only countably many dimensions \(0,1,2,\ldots,\infty\). Thus a construction performed on every such stratum gives a measurable construction on the original field. Countably many measurable operator generators, including generators of the commutants, can be chosen by the imported Effros results. Their matrix coefficients have Borel versions on a common conull set.

These observations explain why a countable list of commutator, projection and range equations defines a Borel relation. They do not require the equivalence relation of the fibres themselves to have a Borel classification.

## 2. Choosing spatial equivalences

**Theorem 2.1.** Suppose
\[
H_i=\int_X^\oplus H_i(x)\,d\mu(x),\qquad
M_i=\int_X^\oplus M_i(x)\,d\mu(x),\quad i=1,2.
\]
If \(M_1(x)\) and \(M_2(x)\) are spatially isomorphic almost everywhere, there is a measurable field of unitaries
\[
U_x:H_1(x)\longrightarrow H_2(x),\qquad
U_xM_1(x)U_x^*=M_2(x).
\tag{2.1}
\]
Its direct integral is a unitary carrying \(M_1\) onto \(M_2\).

The same assertion holds for two measurable fields of representations of one separable C*-algebra that are unitarily equivalent almost everywhere: the unitaries can be chosen to intertwine every element of that algebra.

**Proof.** Discard the null set on which spatial equivalence fails. The dimension functions agree there. Trivialize on their common dimension strata. The zero stratum has its unique zero-space unitary; elsewhere both Hilbert fibres are one fixed \(K\).

Choose countable generators \(a_j(x)\) and \(b_j(x)\) of \(M_1(x)\) and \(M_2(x)\), and \(c_j(x)\), \(d_j(x)\) of their respective commutants. Let \(R\) consist of \((x,u)\), with \(u\) unitary on \(K\), satisfying
\[
[ua_j(x)u^*,d_k(x)]=0,\qquad
[u^*b_j(x)u,c_k(x)]=0
\quad(j,k\geq1).
\tag{2.2}
\]
It is Borel by Section 1. The first set of equations says that \(uM_1(x)u^*\subseteq M_2(x)\); the second gives the reverse inclusion. To pass from the generators to the algebras, use commutants and the bicommutant theorem. Every section is nonempty by hypothesis. Lemma 1.1 supplies \(U_x\).

The operator field \(U_x\) and its adjoint are measurable and have norm one. Their direct integrals are inverse unitaries. Conjugation takes measurable bounded algebra fields to measurable bounded algebra fields and has the inverse conjugation, so it carries the entire direct-integral algebra onto the other one.

For representations \(\pi_i(x)\) of a separable C*-algebra \(A\), choose a countable norm-dense subset \((r_j)\subseteq A\). Replace (2.2) by
\[
u\pi_1(x)(r_j)=\pi_2(x)(r_j)u\quad(j\geq1).
\]
This is again a Borel relation with nonempty sections. Norm continuity extends all the selected intertwining identities from \((r_j)\) to every \(a\in A\), outside the same null set. \(\square\)

## 3. Choosing abstract isomorphisms

An abstract isomorphism need not be implemented by a unitary between the original representation spaces. For instance, \(M_2(\mathbb C)\) acting on \(\mathbb C^2\) and acting with multiplicity three on \(\mathbb C^2\otimes\mathbb C^3\) have different Hilbert-space dimensions.

We therefore retain two requirements that a faithful compression must satisfy:
\[
u^*u=p,\qquad uu^*=q,
\tag{3.1}
\]
where \(q\) is the identity of the target Hilbert space inside an ambient space, and
\[
[N'pK]=K,
\tag{3.2}
\]
where \(N\) is the amplified source algebra and \(p\in N'\). Condition (3.1) gives the whole target range. Condition (3.2) ensures that no central part of the source algebra is lost. Both have countable Borel tests.

**Theorem 3.1.** In the setting of Theorem 2.1, suppose only that \(M_1(x)\) and \(M_2(x)\) are abstractly *-isomorphic almost everywhere. There are normal *-isomorphisms
\[
\Theta_x:M_1(x)\longrightarrow M_2(x)
\tag{3.3}
\]
such that applying \(\Theta_x\), or its inverse, to a measurable bounded algebra field gives a measurable bounded field. Consequently
\[
\Theta:M_1\longrightarrow M_2,\qquad
(\Theta a)(x)=\Theta_x(a(x)),
\tag{3.4}
\]
is a normal *-isomorphism preserving the diagonal \(L^\infty(X,\mu)\).

**Proof.**

*Step 1: put all choices in fixed operator spaces.* An abstract *-isomorphism between von Neumann algebras is normal: it and its inverse preserve the positive order, hence every bounded increasing supremum. Apply the imported normal-representation theorem to each fibre isomorphism, without yet trying to choose it measurably. Since the target fibre is separable, its orthogonal family of nonzero cyclic subspaces is countable. The proof of that theorem therefore uses a countable amplification. Enlarging the multiplicity space if necessary, we can always use \(\ell^2(\mathbb N)\).

Stratify by the two original dimensions. On a nonzero stratum identify
\[
H_1(x)\otimes\ell^2(\mathbb N)=K=\ell^2(\mathbb N)
\]
using a fixed enumeration of the tensor-product bases, and identify \(H_2(x)\) with the fixed subspace \(qK\). Set
\[
N_x=M_1(x)\otimes1_{\ell^2}.
\]
The imported theorem supplies, at each point, a projection \(p\in N_x'\) with (3.2) and a partial isometry \(u:pK\to qK\) such that
\[
\Theta_x(a)=u(a\otimes1)u^*.
\tag{3.5}
\]
Extend \(u\) by zero on \((1-p)K\). The zero-dimensional stratum is treated separately by its unique algebra map.

*Step 2: write a Borel relation that captures precisely these choices.* Choose measurable contraction generators \(a_j(x)\) of \(N_x\) and \(c_j(x)\) of \(N_x'\). Choose likewise \(b_j(x)\) of \(M_2(x)\) and \(d_j(x)\) of its commutant on \(qK\), extending them by zero on \((1-q)K\). Include the identities of the relevant algebras.

For \((x,p,u)\in X\times B(K)_1\times B(K)_1\), impose
\[
\begin{aligned}
&p=p^*=p^2,\qquad [p,a_j(x)]=0,\\
&u^*u=p,\qquad uu^*=q,\\
&[ua_j(x)u^*,d_k(x)]=0,\\
&[u^*b_j(x)u,\,pc_k(x)p]=0
\qquad(j,k\geq1).
\end{aligned}
\tag{3.6}
\]
The last equation uses the compressed commutant. The imported induction formula says that the commutant of the algebra \(N_x\) induced on \(pK\) is exactly \(pN_x'p|_{pK}\). Compression is normal and onto that corner; generators can be replaced by a countable ultraweakly dense family, so these equations test commutation with the entire corner. Equivalently, take \(c_j\) to enumerate a countable ultraweakly dense subset of its unit ball before compression.

For the faithfulness requirement, let \((v_j(x))\) enumerate the identity and every word in a countable generating family of \(N_x'\) and its adjoints. If \((e_l)\) is the standard basis of \(K\), the closed linear span of
\[
\{v_j(x)pe_l:j,l\geq1\}
\]
is exactly \([N_x'pK]\). To verify this, that span contains \(pK\) and reduces every chosen generator of \(N_x'\); its projection therefore commutes with \(N_x'\), so the span is invariant under the whole algebra. The opposite inclusion follows because each word belongs to \(N_x'\).

Thus (3.2) is equivalent to the following countable condition: for each \(r,k\geq1\), some finite linear combination, with coefficients in \(\mathbb Q+i\mathbb Q\), of the vectors \(v_j(x)pe_l\) is within \(1/k\) of \(e_r\). This is a countable intersection of countable unions of Borel norm inequalities. Along with (3.6), it defines a Borel relation \(R\).

*Step 3: check both directions of the test.* Every pointwise isomorphism supplied in Step 1 gives a point in \(R_x\). Conversely, a point of \(R_x\) gives the normal unital map (3.5) into \(M_2(x)\), by the third line of (3.6). The last line implies
\[
u^*M_2(x)u\subseteq N_x|_{pK},
\]
using the induction commutant formula and the bicommutant theorem. Since \(uu^*=q\), this inclusion proves that (3.5) is onto. Requirement (3.2), again by the imported induction theorem, proves that it is injective. Thus \(R_x\) parametrizes suitable faithful isomorphisms.

Lemma 1.1 supplies measurable \(p_x,u_x\), Borel on a common conull set. Formula (3.5) immediately shows that \(\Theta_x(a(x))\) is measurable whenever \(a(x)\) is a measurable field. It also preserves the norm at each point.

*Step 4: verify measurability of the inverse rather than assume it.* On one dimension stratum and the retained Borel base, let \(b(x)\in M_2(x)_1\) be a Borel operator field. Consider
\[
G_b=\{(x,a):a\in M_1(x)_1,\
u_x(a\otimes1)u_x^*=b(x)\}.
\tag{3.7}
\]
Membership in \(M_1(x)\) is tested by commutation with countably many commutant generators. Amplification, multiplication and adjoint on these balls are Borel, so \(G_b\) is Borel in the product with \(B(H_1)_1\). Its projection to the base is one-to-one and onto, because every \(\Theta_x\) is an isometric bijection. The imported injective Borel-image theorem makes the inverse of this projection Borel. Its second coordinate is the desired field \(\Theta_x^{-1}(b(x))\). A bounded field of arbitrary norm is reduced to the unit ball by a constant scaling, and a completed-measurable field is first given a Borel version.

Steps 3 and 4 show that (3.4) is an onto isometric *-homomorphism with inverse given fibrewise. An algebra isomorphism of von Neumann algebras is normal by the order argument in Step 1. Since the maps are unital on each fibre,
\[
\Theta_x(f(x)1)=f(x)1,
\]
so the global map preserves the diagonal. \(\square\)

The theorem chooses some isomorphisms. If a separate pointwise choice has been prescribed without any measurable dependence, this proof does not assert that the prescribed choice is measurable.

## 4. When all fibres have one algebraic type

**Corollary 4.1.** If \(M(x)\) is abstractly isomorphic to one fixed von Neumann algebra \(M_0\) almost everywhere on a standard sigma-finite base, then
\[
\int_X^\oplus M(x)\,d\mu(x)
\cong L^\infty(X,\mu)\,\bar\otimes\,M_0,
\tag{4.1}
\]
by an isomorphism preserving \(L^\infty(X,\mu)\).

**Proof.** If the base is null, both sides are zero. Otherwise a retained fibre supplies a faithful representation of \(M_0\) on a separable Hilbert space \(H_0\). Use this concrete representation for the constant field. Theorem 3.1 identifies the original integral with the constant-field integral. The zero algebra is handled by zero fibres.

Here is the constant-field identification on the stated sigma-finite base. The map taking \(f\otimes\xi\) to the section \(x\mapsto f(x)\xi\) preserves inner products. Its range is dense in \(L^2(X;H_0)\): expand a square-integrable section in a countable orthonormal basis of \(H_0\) and truncate its coordinates; the squared tail norm tends to zero by monotone convergence. It therefore extends to a unitary
\[
L^2(X,\mu)\otimes H_0\longrightarrow L^2(X;H_0).
\]
In this representation let \(D\) be the diagonal algebra and let \(\mathcal N=(D\cup(1\otimes M_0))''\), the spatial tensor product.

By the full diagonal-commutant theorem, Theorem 5.1 of [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html), an operator in \(\mathcal N'\) is a bounded measurable operator field. Choose a countable strong-star dense family in the unit ball of \(M_0\). Commutation with its constant fields holds fibrewise outside one common null set, by uniqueness of decomposable fields. Strong continuity on bounded sets extends these identities to all of \(M_0\). Thus \(\mathcal N'\) consists exactly of bounded measurable fields with values in \(M_0'\).

Every bounded measurable \(M_0\)-valued field commutes pointwise with these fields, so its direct integral belongs to \((\mathcal N')'=\mathcal N\). Conversely, \(\mathcal N\) commutes with \(D\) and every constant operator from \(M_0'\). The same theorem and a countable strong-star dense family in \((M_0')_1\) show that its representing field has values in \((M_0')'=M_0\) almost everywhere. These are precisely the two inclusions needed for the constant-field identification. The diagonal is preserved throughout. This also gives the constant-field assertion of [Vector-valued functions and preduals](../reader/measurable-equivalence-and-constant-fibres.html#4-when-all-fibres-have-one-algebraic-type), Theorem 9.1(1), in the present base setting. \(\square\)

This statement concerns the algebra and its diagonal. It places no condition that the original representation have constant multiplicity.

## 5. Graded exercises with complete solutions

### Exercise 5.1 — Multiplicity changes without changing the algebra (basic)

Use Lebesgue measure on \([0,1]\). On the first half let \(M(x)=M_2(\mathbb C)\) act on \(\mathbb C^2\); on the second half let it act as \(M_2(\mathbb C)\otimes1_3\) on \(\mathbb C^2\otimes\mathbb C^3\). Identify the direct-integral algebra. Can it be identified with the constant \(\mathbb C^2\) representation by a measurable field of fibre unitaries?

**Solution.** The matrix units give measurable fields on each half. Write a field on the second half uniquely as \(a(x)\otimes1_3\). The map that keeps \(a(x)\) on the first half and removes the multiplicity factor on the second is a measurable *-isomorphism, with measurable inverse. Thus the algebra is \(L^\infty([0,1])\bar\otimes M_2(\mathbb C)\). A unitary from a six-dimensional fibre to a two-dimensional fibre cannot exist. Consequently no field of fibre unitaries implements this particular constant-representation identification. Theorem 3.1 applies nevertheless.

### Exercise 5.2 — Why the commutant must be compressed (intermediate)

On \(K=\mathbb C^2\otimes\mathbb C^2\), take \(N=M_2(\mathbb C)\otimes1_2\) and \(p=1_2\otimes e_{11}\). Show that induction by \(p\) is faithful. For \(u=p\), viewed as a unitary from \(pK\) onto the target \(pK\) and extended by zero, compare commutation of \(u^*(a\otimes1_2)u\) with \(N'\) and with \(pN'p\).

**Solution.** Here \(N'=1_2\otimes M_2(\mathbb C)\). Its orbit of \(pK\) spans both multiplicity coordinates, so \([N'pK]=K\). Induction is faithful and its image is the usual two-dimensional representation of \(M_2(\mathbb C)\).

The zero-extended induced operator is \(a\otimes e_{11}\). For \(a\ne0\),
\[
[a\otimes e_{11},\,1_2\otimes e_{12}]
=a\otimes e_{12}\ne0.
\]
Thus it need not commute with the uncompressed commutant. On the other hand,
\[
pN'p=\mathbb C p,
\]
which commutes with every induced operator. The fourth line of (3.6) therefore uses \(pc_kp\). It permits faithful compressions by noncentral projections such as this one.

### Exercise 5.3 — Onto compression can still lose a central summand (advanced)

Let \(N=\mathbb C\oplus\mathbb C\) act diagonally on \(K=\mathbb C^2\), and let \(p=q=e_{11}\), \(u=p\). Show that the range and commutation equations in (3.6), with the target algebra \(\mathbb C\) on \(qK\), hold. Identify the missing condition and the kernel of the resulting map.

**Solution.** The projections satisfy \(u^*u=p\), \(uu^*=q\), and \(p\in N'=N\). The induced algebra on the one-dimensional space is \(\mathbb C\), so both commutation tests hold. The map is
\[
(\lambda,\nu)\longmapsto\lambda,
\]
with kernel \(0\oplus\mathbb C\). But \([N'pK]=pK\), not \(K\). The countable test for (3.2) fails already for the second basis vector: every allowed orbit vector is a multiple of the first. This illustrates why a range condition alone proves surjectivity but does not prove faithfulness.

## References

- [Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979.
- [Elliott 1971] George A. Elliott, [An extension of some results of Takesaki in the reduction theory of von Neumann algebras](https://msp.org/pjm/1971/39-1/pjm-v39-n1-p12-s.pdf), *Pacific Journal of Mathematics* 39(1) (1971), 145–148.
- The prerequisite lessons cited above contain the selection, Borel-image and induction theorems used here, with their proofs and source attributions.
