# Semicontinuity and Grauert's theorem

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Public domain (CC0).*

The dimensions of fiber cohomology can increase at special parameters. A finite complex explains both this increase and the stronger conditions that prevent it. Matrix ranks control semicontinuity; lifting fiber classes controls the comparison map; and a reduced base turns pointwise vanishing of matrix entries into actual vanishing.

We use [Base change and the Grothendieck complex](base-change-and-the-grothendieck-complex.md). First take a proper morphism \(f:X\to S\) with \(S\) Noetherian and \(F\) coherent and flat over \(S\). All conclusions also apply to a proper morphism of finite presentation over an arbitrary scheme, with \(F\) finitely presented and flat over \(S\). For this extension of the setting, the finite projective model is supplied by the exact open finite-presentation theorem [Stacks, Tag 0B91], proved through [Tag 0A1H]. Its Noetherian approximation descends the finitely presented scheme and sheaf, flatness and proper support, then applies the Noetherian theorem. We use this precise extension as a foundation; the matrix arguments below prove the conclusions in both settings.

Locally on an affine base, therefore, a finite projective complex \(K\) represents \(Rf_*F\) and computes \(H^q(X_B,F_B)\) after every algebra base change. It may be chosen in nonnegative degrees. In the Noetherian case this was proved in the preceding lesson. In the general case, start with a perfect model. Its derived tensor with every module has no negative cohomology: apply the universal comparison to the square-zero algebra \(A\oplus M\) and take the \(M\)-summand. Truncating a finite projective model below zero as in the preceding lesson produces a finitely presented quotient \(Q\) with \(\operatorname{Tor}_1(Q,M)=0\) for all \(M\). Thus \(Q\) is finite projective, giving the same nonnegative model. This truncation uses finite presentation, not Noetherianness of the base.

We denote the canonical fiber comparison by
\[
\varphi^q(s):(R^qf_*F)\otimes\kappa(s)\longrightarrow H^q(X_s,F_s).
\]
On an affine neighborhood it is the cocycle map \(H^q(K)\otimes\kappa(s)\to H^q(K\otimes\kappa(s))\). Comparing these two expressions for cohomology is the purpose of this lesson.

## 1. Semicontinuity from minors

After restricting to an affine open where every projective term is free, write \(r_q=\operatorname{rank}K^q\). Let \(d^q\) be its differential and \(\rho_q(s)\) the rank of the matrix over \(\kappa(s)\). Since \(d^qd^{q-1}=0\), linear algebra gives
\[
h^q(s):=\dim_{\kappa(s)}H^q(X_s,F_s)
=r_q-\rho_{q-1}(s)-\rho_q(s).
\]
The rank of a matrix is lower semicontinuous: the locus of rank at least \(r\) is the union of the principal opens where some \(r\times r\) minor is invertible. The sum of the two ranks is the rank of their block diagonal matrix, so it too is lower semicontinuous.

**Theorem 1.1 (semicontinuity).** Under the stated proper flat-sheaf hypotheses, every \(h^q:S\to\mathbf Z_{\geq0}\) is upper semicontinuous. Its level sets are locally constructible, and its values commute with arbitrary base change of parameter schemes.

**Proof.** On each trivializing affine, the displayed formula makes \(\{h^q\geq n\}\) the locus where the block diagonal matrix has rank at most \(r_q-n\). This is closed, defined by the minors of size \(r_q-n+1\), with the usual empty or whole-locus conventions at the extreme bounds. The closed-locus assertion is local, so holds on \(S\). Each equality locus \(\{h^q=n\}\) is the difference of the closed loci \(\{h^q\geq n\}\) and \(\{h^q\geq n+1\}\), hence locally constructible. For a parameter \(s'\) above \(s\), the new geometric cohomology complex is the old fiber complex tensored with \(\kappa(s')\). Extending a field preserves its ranks and cohomology dimensions, proving the final assertion. \(\square\)

Upper semicontinuity allows an increase on a closed locus. It does not say that every special fiber acquires new cohomology or that individual cohomology modules over the parameter ring are locally free. Those require further information about the matrices.

## 2. Remove the invertible blocks

**Lemma 2.1 (a minimal complex near a point).** For a fixed \(s\), after restricting to an affine neighborhood and trivializing the terms, the complex can be replaced by a finite free complex whose differentials are all zero over \(\kappa(s)\). The replacement preserves its cohomology after every base change.

**Proof.** If a differential matrix has an entry invertible at \(s\), shrink so that it is a unit and use elementary row and column operations to make it the sole nonzero entry in its row and column, equal to one. The relation between consecutive differentials forces the incoming differential's component in the corresponding source summand to be zero, and the outgoing differential's component from the corresponding target summand to be zero. Thus the two copies of \(A\), with identity between them, split off as a direct summand complex in consecutive degrees. This summand is contractible, including after every tensor product. Remove it. Each removal reduces the sum of the term ranks by two, so after finitely many removals no entry is invertible at \(s\). All remaining entries lie in the maximal ideal of \(\mathcal O_{S,s}\), which means the residue-field differentials are zero. All operations and splittings occurred on a neighborhood of \(s\), proving the lemma. \(\square\)

Here minimality refers to the chosen point. Other points of the neighborhood may still have nonzero residue-field differentials. At the chosen point,
\[
H^q(K\otimes\kappa(s))=K^q\otimes\kappa(s).
\]
Surjectivity of a cohomology comparison now says that a basis of this space lifts to actual cocycles.

**Lemma 2.2 (lifting cocycles kills a differential).** For a complex as in Lemma 2.1, \(\varphi^q(s)\) is surjective if and only if \(d^q=0\) in the local ring at \(s\). If it is surjective, \(d^q\) is zero on a smaller neighborhood.

**Proof.** If the map is surjective, choose finitely many actual cocycles in \(K^q\) whose reductions give a basis of \(K^q\otimes\kappa(s)\). The square matrix having these cocycles as columns has determinant invertible in the local ring, so they form a basis of \(K^q\) there. The differential kills every basis vector, hence is zero. Its finitely many entries vanish in the localization and consequently on some smaller neighborhood. Conversely, if \(d^q=0\) locally, every element of \(K^q\) is a cocycle. Its reduction maps onto the fiber cohomology because the incoming differential reduces to zero by minimality. Thus \(\varphi^q(s)\) is surjective. \(\square\)

This proof does not need finite generation of the entire cocycle module over an arbitrary base. Surjectivity selects finitely many cocycles, and an invertible determinant already makes them a basis of the finite free term.

## 3. Cohomology and base change

**Theorem 3.1 (the surjectivity criterion).** Suppose \(\varphi^q(s)\) is surjective. There is an open neighborhood \(U\) of \(s\) on which formation of \(R^qf_*F\) commutes with every base change. In particular the comparison is an isomorphism at every point of \(U\). Under this hypothesis, the following are equivalent:

1. \(\varphi^{q-1}(s)\) is surjective;
2. \(R^qf_*F\) is locally free on a neighborhood of \(s\).

For \(q=0\), set all negative direct images and fiber cohomology to zero; the first condition is automatic.

**Proof.** Apply Lemmas 2.1–2.2 and shrink so that \(d^q=0\). Then
\[
H^q(K)=\operatorname{coker}(d^{q-1}:K^{q-1}\to K^q).
\]
Tensor is right exact, so for every \(A\)-algebra \(B\) on this neighborhood,
\[
H^q(K)\otimes_A B
\cong\operatorname{coker}(d^{q-1}\otimes B)
=H^q(K\otimes_A B).
\]
This is exactly the canonical comparison. The identity localizes and glues for arbitrary scheme base changes, proving the first part.

If \(\varphi^{q-1}(s)\) is surjective, Lemma 2.2 kills \(d^{q-1}\) after a further shrinking. Now \(H^q(K)=K^q\), so it is finite free there.

Conversely assume \(H^q(K)\) is free over the local ring \(A_s\). The sequence
\[
0\to N:=\operatorname{im}d^{q-1}\to K^q\to H^q(K)\to0
\]
splits, since its quotient is free. Thus \(N\) is a finite direct summand of \(K^q\). Minimality gives \(N\subset\mathfrak m_sK^q\), so its inclusion is zero after tensoring with the residue field. But a split inclusion remains injective after tensoring. Hence \(N/\mathfrak m_sN=0\), and Nakayama gives \(N=0\). Therefore \(d^{q-1}=0\) locally and Lemma 2.2 proves surjectivity of \(\varphi^{q-1}(s)\). In degree zero the nonnegative model already has \(K^{-1}=0\), giving the stated convention. \(\square\)

The hypothesis refers to the comparison map, not merely to equality of dimensions of two spaces. Once it holds, right exactness of a cokernel supplies arbitrary base change in that degree. Local freeness adds a condition on the preceding differential. These are two distinct conclusions of the theorem.

## 4. Grauert's theorem and the reduced base

**Theorem 4.1 (Grauert).** Suppose \(S\) is reduced and \(h^q\) is locally constant. Then \(R^qf_*F\) is finite locally free and its formation commutes with every base change.

**Proof.** Fix \(s\) and choose a minimal complex near it. Let \(r=\operatorname{rank}K^q\). The two residue-field differentials at \(s\) vanish, so \(h^q(s)=r\). Restrict to a neighborhood where \(h^q\) is this constant. For every point \(u\) there,
\[
r=h^q(u)=r-\rho_{q-1}(u)-\rho_q(u).
\]
Both ranks are nonnegative, hence both are zero at every point. Every matrix entry of \(d^{q-1}\) and \(d^q\) therefore belongs to every prime of the affine coordinate ring. Such entries lie in its nilradical. Reducedness makes that nilradical zero, so both differentials actually vanish. Consequently \(H^q(K)=K^q\), and the same is true after every tensor product. This gives finite local freeness and comparison with every base change on a neighborhood of \(s\); these assertions glue on \(S\). \(\square\)

Reducedness is doing precise work: residue fields detect whether an entry is nilpotent, but do not detect whether that nilpotent entry is zero. Over \(A=k[\epsilon]/(\epsilon^2)\), the complex
\[
[\,A\xrightarrow{\epsilon}A\,]\quad\text{in degrees }0,1
\]
has fiber dimensions one in each degree on the one-point base. Yet its cohomology modules are \((\epsilon)\) and \(A/(\epsilon)\), neither free over \(A\), and its degree-zero comparison is zero. This complex is realized by the flat rank-two extension of \(\mathcal O\) by \(\mathcal O(-2)\) on \(\mathbf P^1_A\) with class \(\epsilon\). Thus the failure occurs for a proper flat family with a vector bundle, not only for an unrelated algebraic complex.

## 5. Vanishing and the structure sheaf

**Corollary 5.1 (vanishing gives local freeness).** If \(R^qf_*F=0\) for every \(q>0\), then \(f_*F\) is finite locally free and commutes with arbitrary base change. Its higher direct images also vanish after every base change.

**Proof.** On an affine neighborhood, use the nonnegative finite projective complex \(K\). It is exact in positive degrees. Begin at the last term: the preceding differential surjects onto a projective module, so splits. Its kernel is a finite projective direct summand of the preceding term. Exactness in the next degree gives another surjection onto this kernel, which again splits. Continue down to degree zero. It follows that \(K\) is the direct sum of contractible projective pairs and its finite projective \(H^0\) in degree zero. All these splittings survive every tensor product. The universal comparison of the Grothendieck complex proves the assertions. \(\square\)

**Theorem 5.2 (constants in a proper flat family).** Let \(f\) be proper, flat and of finite presentation, with nonempty geometrically reduced and geometrically connected fibers. Then the unit is an isomorphism
\[
\mathcal O_S\xrightarrow{\sim}f_*\mathcal O_X,
\]
and remains an isomorphism after every base change. No reducedness assumption on \(S\) is required.

**Proof.** By the global-functions calculation in the proper-image lesson, a nonempty geometrically reduced and geometrically connected proper scheme over a field has that field as its constants. Thus
\(H^0(X_s,\mathcal O_{X_s})=\kappa(s)\). The unit section is an actual global section and maps to \(1\) in this fiber space. Therefore \(\varphi^0(s)\) is surjective at every point. Theorem 3.1 applies in degree zero, where the preceding comparison is automatically surjective: \(f_*\mathcal O_X\) is finite locally free, with arbitrary base change. Its fibers all have dimension one. The unit map between these rank-one locally free sheaves is an isomorphism on every residue field; its coefficient is consequently a unit in every local ring, so it is an isomorphism. Its universal comparison identifies the base-changed unit with the same isomorphism over every \(S'\). \(\square\)

The nonempty convention is stated explicitly; the Stacks convention for geometrically connected schemes already includes it [Tag 0362]. Over an imperfect field, geometric reducedness is essential in the constants assertion. The purely inseparable field example in the proper-image lesson shows why ordinary reducedness is insufficient. Universality here includes nilpotent base changes, which would not follow from checking only reduced parameter schemes.

## 6. A line bundle with jumping sections

Let \(E\) be a smooth projective geometrically connected genus-one curve over an algebraically closed field \(k\), and fix \(p\in E(k)\). On \(E\times E\), let \(\Delta\) be the diagonal and consider
\[
\mathcal L=\mathcal O_{E\times E}(\{p\}\times E-\Delta).
\]
Both divisors are Cartier. For the second projection its fiber at \(q\) is \(L_q=\mathcal O_E(p-q)\), and \(\mathcal L\) is flat over the base: it is invertible on a scheme flat over \(E\).

We use one curve-theoretic input for this example: on an integral proper Cohen–Macaulay genus-\(g\) curve, a line bundle of degree greater than \(2g-2\) has no \(H^1\), the case of empty \(Z\) in the exact open [Stacks, Tag 0E3B]. Its proof uses curve duality; none of the matrix theorems above depend on this additional example input. On our smooth curve, it gives \(H^1(\mathcal O_E(p))=0\). The point sequence and \(\chi(\mathcal O_E)=0\) then give \(h^0(\mathcal O_E(p))=1\).

An invertible sheaf of degree zero with a nonzero section is trivial: its section has an effective zero divisor of degree zero, hence no zeros, so trivializes the sheaf. If \(L_q\) is trivial, \(\mathcal O_E(p)\cong\mathcal O_E(q)\). Each has its canonical section vanishing at its indicated point. Their section space is one-dimensional, so the isomorphism identifies these sections up to scalar; their zero divisors coincide and \(p=q\). Conversely \(L_p\) is trivial. This argument is preserved after extension of the ground field, so also applies at the generic parameter. Therefore
\[
h^0(E,L_q)=\begin{cases}1&q=p,\\0&q\ne p.\end{cases}
\]
The Euler characteristic is zero for all \(q\): adding the point \(p\) and subtracting the point \(q\) in the two divisor sequences cancel their length-one Euler contributions. Since the curve has cohomological dimension one, \(h^1(E,L_q)=h^0(E,L_q)\). Both jump at the closed point \(p\), consistently with semicontinuity and Euler constancy.

This family also illustrates the hypothesis in Theorem 3.1. Its degree-zero direct image is zero. Indeed it is torsion-free on the integral base, because multiplication by a nonzero base function is injective on the flat sheaf at every stalk, and taking sections preserves this injection; it has zero generic rank, and it is finite by proper coherence, so it is zero. Thus at \(p\) the comparison is \(0\to k\), which is not surjective. The exceptional fiber section cannot be lifted from a neighborhood.

## 7. Exercises with solutions

**Exercise 7.1 (easy: minors).** Prove upper semicontinuity of the middle cohomology dimension of a three-term complex of finite free modules, and write its jump locus as a determinantal locus.

**Solution.** For ranks \(a,b,c\) and differential ranks \(r_1,r_2\), the dimension is \(b-r_1-r_2\). The sum is the rank of the block diagonal matrix formed by the two differentials. Thus dimension at least \(n\) is defined by all minors of size \(b-n+1\) of that matrix. This is closed. Subtracting the next such closed locus gives a locally closed equality locus.

**Exercise 7.2 (medium: the genus-one family).** Compute \(h^0\), \(h^1\), and the degree-zero comparison at the special point of the family \(\mathcal O_E(p-q)\).

**Solution.** A nonzero section of a degree-zero bundle trivializes it. The one-dimensional section space of \(\mathcal O(p)\), established in Section 6, shows triviality occurs exactly when \(q=p\). Thus both dimensions are one there and zero elsewhere, since their Euler difference is zero. The flat sheaf gives torsion-free direct-image sections on the integral base, and generic vanishing makes that direct image zero. Its comparison at \(p\) is therefore \(0\to k\), not a surjection. This identifies the precise missing hypothesis of the base-change criterion.

**Exercise 7.3 (medium: geometrically integral fibers).** Deduce universal \(f_*\mathcal O_X=\mathcal O_S\) for a proper flat finitely presented morphism with geometrically integral fibers. Explain whether the base must be reduced.

**Solution.** Geometrically integral fibers are nonempty, geometrically reduced and geometrically connected. Theorem 5.2 applies directly and proves the universal equality. The base may have nilpotents. In its proof the unit provides a lift of the fiber's constant section, so degree-zero comparison is surjective without using reducedness or Grauert's theorem.

**Exercise 7.4 (hard: Grauert from a minimal model).** Starting with a finite free complex minimal at \(s\), prove the reduced-base theorem and identify the exact step that fails on a nonreduced base.

**Solution.** Minimality makes the fiber dimension in degree \(q\) equal to the rank of the corresponding term. If this dimension is constant nearby, both adjacent differential ranks must be zero at every point. Their entries vanish in every residue field, hence lie in the nilradical. A reduced coordinate ring has zero nilradical, so both matrices vanish and the cohomology is the free middle term, before and after every tensor product. Without reducedness this only proves that the entries are nilpotent. Multiplication by a nonzero nilpotent need not be a zero differential, so its kernels and cokernels need not be free.

**Exercise 7.5 (hard: a nonreduced counterexample).** Use the extension with class \(\epsilon\) over \(k[\epsilon]/(\epsilon^2)\) to verify failure of Grauert's conclusion despite constant fiber dimensions.

**Solution.** The extension is a vector bundle on \(\mathbf P^1_A\), so is flat over \(A\). Its cohomology model is \([A\xrightarrow{\epsilon}A]\) in degrees zero and one. The sole fiber has zero differential, with both dimensions one. Over \(A\), the kernel is \((\epsilon)\) and the cokernel is \(k\); both have length one, while a nonzero finite free \(A\)-module has length a positive even integer. Hence neither is free. In degree zero the cocycle \(\epsilon\) reduces to zero, so the comparison \((\epsilon)\otimes_A k\to k\) is the zero map. This verifies the geometric counterexample completely.

**Exercise 7.6 (challenging: the adjacent comparison).** For \(K=[A\xrightarrow{t}A]\) in degrees zero and one over \(A=k[t]\), check both parts of Theorem 3.1 at \(t=0\), taking \(q=1\).

**Solution.** The outgoing degree-one differential is zero, so \(H^1(K)=A/(t)\), and its comparison with \(H^1(K\otimes B)=B/tB\) is an isomorphism for every \(B\). In particular \(\varphi^1(0)\) is surjective. The degree-zero comparison is \(0\to k\), since multiplication by \(t\) is injective over \(A\) and becomes zero on that fiber. It is not surjective, consistently with \(A/(t)\) not being locally free near zero. The first comparison criterion gives universal base change in degree one, while the second correctly rejects local freeness there.

## References and hypotheses

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition. The finite-presentation extension of the Grothendieck complex is [Tag 0B91](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-flat-proper-perfect-direct-image-general); its full Noetherian-approximation proof is [Tag 0A1H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-base-change-tensor-perfect). Semicontinuity is [Tag 0BDI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-jump-loci); vanishing and local freeness [Tag 0D4E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-vanishing-implies-locally-free); universal constants [Tag 0E0L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-proper-flat-geom-red-connected). Sections 1–5 provide the matrix proofs and both parts of the surjectivity theorem used here.
- The example's extra curve input is [Tag 0E3B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-degree-more-than-2g-2). The nonempty convention for geometric connectedness is [Tag 0362](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-definition-geometrically-connected). These are explicit routine inputs; the reduced-base Grauert theorem and comparison criterion have complete proofs in this lesson.
- The open reference treatments retain GNU FDL 1.2. This exposition, proofs, examples and solutions are independently written CC0. AI Integrated Stacks Project includes AI-proposed additions and corrections and is not reviewed by maintainers of the [official Stacks project](https://stacks.math.columbia.edu/). Reducedness is required for the pointwise-rank argument in Grauert's theorem; it is not required for the surjectivity criterion or the universal constants theorem.
