# Orders and the discriminant theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A prime can divide the discriminant for two different reasons: the field extension can ramify, or an order can lose information before reduction. The trace pairing detects both. We will prove the criterion for arbitrary orders, over any Dedekind base, and keep inseparable residue fields in view.

We assume the ideal theory of Noether's axioms for Dedekind domains, elementary traces of linear maps, and the characterization of a finite étale algebra over a field as a finite product of finite separable extensions [Milne FT, Proposition 8.6 and Corollary 8.7; Stacks, Tag 00U3]. Basic references are [Noether], [Milne] and [Stacks].

## 1. The trace measures multiplication

For a finite-dimensional commutative \(k\)-algebra \(E\), multiplication by \(a\) is a linear map \(m_a:E\to E\). Define

\[
 \operatorname{Tr}_{E/k}(a)=\operatorname{trace}(m_a),\qquad
 t_E(a,b)=\operatorname{Tr}_{E/k}(ab).
\]

The regular representation, not a reduced trace from a noncommutative algebra, is meant here.

**Lemma 1.1.** Every nilpotent element of \(E\) is in the radical of \(t_E\).

**Proof.** If \(n^r=0\), then \((na)^r=0\) for every \(a\), by commutativity. Multiplication by \(na\) is nilpotent. Its characteristic polynomial is a power of \(T\), so its trace is zero. \(\square\)

**Lemma 1.2.** For a finite field extension \(F/k\), its trace pairing is nondegenerate if and only if \(F/k\) is separable.

**Proof in the separable case.** By the primitive element theorem write \(F=k(\theta)\), with distinct conjugates \(\theta_1,\ldots,\theta_n\) in a splitting field. For the power basis, the trace matrix is \(V^{\mathsf T}V\), where \(V_{ij}=\theta_i^{j-1}\). Indeed, after scalar extension multiplication is diagonal in the decomposition into embeddings, so trace is the sum of the embedded elements. The Vandermonde determinant \(\prod_{i<j}(\theta_j-\theta_i)\) is nonzero. Therefore the trace determinant is nonzero.

**Proof in the inseparable case.** The characteristic is \(p>0\). Let \(F_s\) be the maximal separable subextension. The extension \(F/F_s\) is purely inseparable and nontrivial: for every algebraic element, a sufficiently high \(p\)-power is separable, which proves the first assertion. A finite purely inseparable extension can be built as a tower of degree-\(p\) extensions. In a degree-\(p\) step with basis \(1,u,\ldots,u^{p-1}\) and \(u^p\) in the base, multiplication by \(u^j\) has zero diagonal for \(1\le j<p\), and multiplication by \(1\) has trace \(p=0\). Thus the trace map at that step is zero. Transitivity of trace makes \(\operatorname{Tr}_{F/F_s}\), and then \(\operatorname{Tr}_{F/k}\), zero. Transitivity follows by expressing a multiplication matrix in blocks over a basis of the intermediate field and summing its diagonal block traces. Hence the pairing is degenerate. \(\square\)

**Theorem 1.3.** A finite commutative \(k\)-algebra is étale over \(k\) if and only if its trace pairing is nondegenerate.

**Proof.** A nondegenerate pairing has no nonzero nilpotents by Lemma 1.1. A reduced finite-dimensional commutative algebra is a product of fields: it is Artinian, its finitely many maximal ideals are pairwise comaximal, their intersection is the zero nilradical, and the Chinese remainder theorem gives the product. On a product the trace pairing is the orthogonal direct sum of the field pairings. Lemma 1.2 now says that every factor must be separable. Conversely, a product of separable fields has a nondegenerate direct-sum pairing. This is exactly the finite étale characterization. \(\square\)

Over an imperfect field, reducedness alone is insufficient. For example, \(\mathbb F_p(t)[u]/(u^p-t)\) is a field and has identically zero trace pairing.

## 2. A determinant over the base ring

For a finite free \(R\)-algebra \(E\), define trace from its multiplication matrices and, in a basis \(e_1,\ldots,e_n\), define

\[
 \operatorname{disc}(e_1,\ldots,e_n)=
 \det\bigl(\operatorname{Tr}(e_i e_j)\bigr)_{i,j}.
\]

A basis change with matrix \(P\) changes the trace matrix to \(P^{\mathsf T}TP\), so the determinant changes by \((\det P)^2\). The discriminant generates a well-defined ideal, though its chosen generator depends on the basis.

**Proposition 2.1.** Traces, trace pairings and their determinants commute with arbitrary base change for a finite free algebra.

**Proof.** A multiplication matrix in the base-changed basis is the image of the original matrix. Its diagonal sum, every entry of the trace matrix, and its determinant are obtained by applying the ring map to the original expressions. No flatness of the ring map is needed. \(\square\)

Let \(R\) now be Dedekind, with fraction field \(K\), and let \(L/K\) be finite separable of degree \(n\). An **\(R\)-order** \(O\subseteq L\) is a subring containing \(R\), finite as an \(R\)-module, with \(KO=L\). It is torsion-free, so is locally free of rank \(n\): at a nonzero prime the base is a DVR and a finite torsion-free module over a PID is free. Thus \(O\) is finite projective. Trace lands in \(R\); it agrees locally with multiplication trace and hence agrees generically with field trace.

Define \(\mathfrak d_{O/R}\) by these local trace determinants. Equivalently, the determinant of the trace map \(O\to\operatorname{Hom}_R(O,R)\) is a section of the corresponding determinant line. A change of local basis multiplies its coefficient by a unit square, so its vanishing ideal is unambiguous. Nondegeneracy over \(K\) makes this a nonzero ideal.

## 3. Noether's theorem for orders

**Theorem 3.1.** For every nonzero prime \(\mathfrak p\subset R\),

\[
 \mathfrak p\mid\mathfrak d_{O/R}
 \quad\Longleftrightarrow\quad
 O/\mathfrak pO\text{ is not étale over }R/\mathfrak p.
\]

**Proof.** Localize at \(\mathfrak p\), choose a free basis of \(O_{\mathfrak p}\), and reduce its trace matrix modulo \(\mathfrak p\). Proposition 2.1 identifies that reduced matrix with the trace matrix of \(O/\mathfrak pO\). The discriminant ideal is contained in \(\mathfrak p\) precisely when this matrix is singular. Theorem 1.3 identifies singularity with failure of étaleness. \(\square\)

*Reference:* [Noether, Sections 6–8]. The proof applies equally to number fields, function fields, relative orders and imperfect residue fields.

For the integral closure \(B\), prime factorization and the Chinese remainder theorem give

\[
 B/\mathfrak pB\simeq\prod_{\mathfrak P\mid\mathfrak p}B/\mathfrak P^{e_{\mathfrak P}}.
\]

A factor with \(e_{\mathfrak P}>1\) has nonzero nilpotents; a factor with \(e_{\mathfrak P}=1\) is its residue field. Hence the discriminant of the maximal order vanishes precisely when some ramification index exceeds one or some residue extension is inseparable. For number fields all finite residue extensions are separable, yielding Dedekind's familiar ramification criterion. This is also Decomposition of primes in extensions, Theorem 5.4. The short deduction above places that maximal-order theorem inside the arbitrary-order criterion of Theorem 3.1.

If \(O\subseteq B\), their local bases are related by an inclusion matrix \(P\), and

\[
 \mathfrak d_{O/R}=\mathfrak i_{B/O}^{\,2}\mathfrak d_{B/R}.
\]

Here \(\mathfrak i_{B/O}\) is the index ideal with \(\mathfrak p\)-exponent \(\operatorname{length}_{R_{\mathfrak p}}(B_{\mathfrak p}/O_{\mathfrak p})\). Over a DVR, diagonal reduction of \(P\) shows that this length is \(v_{\mathfrak p}(\det P)\), and the determinant basis-change formula proves the assertion. Over \(\mathbb Z\) this is the usual square of the integer lattice index.

For a computational test of maximality, Discriminants and integral bases, Theorem 2.6, proves **Dedekind's index criterion**. Let \(\alpha\) be an integral primitive element of a number field, with monic minimal polynomial \(f\in\mathbb Z[T]\). Write \(\bar f=\prod_i\bar g_i^{e_i}\) modulo a rational prime \(p\), with distinct monic irreducible factors, choose monic integer lifts \(g_i\), and put

\[
 F=\bigl(f-\prod_i g_i^{e_i}\bigr)/p\in\mathbb Z[T].
\]

Then \(p\) does not divide \([\mathcal O_L:\mathbb Z[\alpha]]\) if and only if \(\bar g_i\nmid\bar F\) for every repeated factor \(e_i\ge2\). This stated input tests the defect of the order; Theorem 3.1 tests its entire non-étale fibre. The integer index-discriminant formula is also proved there, Theorem 2.3 and equations (2)–(3); our local determinant argument above gives its relative ideal form.

Noether's 1929 *Über Maximalbereiche aus ganzzahligen Funktionen* studies a related denominator problem: starting from a finitely generated ring of integral functions, saturate it by nonzero integer denominators and ask which primes and denominator powers are required [Noether, opening paragraphs]. In the present discriminant theorem, the maximal order means the integral closure in the field.

## 4. Four reductions worth comparing

For a quadratic field of discriminant \(d_K\), write its integer ring as \(\mathbb Z[\omega]\). The order \(O_f=\mathbb Z+f\mathbb Z\omega\) has basis \(1,f\omega\), so \(\operatorname{disc}(O_f)=f^2d_K\). This distinguishes primes dividing the conductor from primes ramifying in the maximal order.

For \(O=\mathbb Z[3i]\), set \(u=3i\). Its defining polynomial is \(T^2+9\); its trace matrix in \(1,u\) is \(\operatorname{diag}(2,-18)\). Thus its discriminant is \(-36\), and

\[
 O/3O=\mathbb F_3[u]/(u^2).
\]

The class of \(u\) is nonzero although \(u=3i\) in the ambient field: \(i\notin O\), so \(u\notin3O\). By contrast \(\mathbb Z[i]/3\mathbb Z[i]=\mathbb F_9\), since \(T^2+1\) is irreducible over \(\mathbb F_3\). The prime \(3\) is unramified in the field but divides the order's discriminant.

For \(\operatorname{char}k\ne2\), the finite free algebra \(k[t][u]/(u^2-t)\) has trace matrix \(\operatorname{diag}(2,2t)\), with discriminant \(4t\). At \(t=0\) the fibre is the dual-number algebra; at a nonzero \(t\)-value the derivative \(2u\) is invertible in the fibre, which is étale even if it does not split over the residue field.

For a relative arithmetic example, let \(K=\mathbb Q(i)\), \(R=\mathbb Z[i]\), and \(O=R[\sqrt3]\subseteq K(\sqrt3)\). In the relative basis \(1,\sqrt3\), the trace matrix is \(\operatorname{diag}(2,6)\) and the discriminant ideal is \((12)\subset R\). At the prime \((3)\), whose residue field is \(\mathbb F_9\), the fibre is \(\mathbb F_9[u]/(u^2)\). At \((1+i)\), the residue characteristic is two and the fibre is \(\mathbb F_2[u]/((u+1)^2)\). Away from these primes the trace determinant is a unit. No principal global basis is required in Theorem 3.1; this example merely happens to have one.

## 5. Exercises

1. **Easy.** Compute the discriminant and the fibre at \(3\) of \(\mathbb Z[3i]\).
2. **Medium.** For monic \(f\in k[T]\) of degree \(n\), show that the discriminant of the power basis of \(k[T]/(f)\) equals \((-1)^{n(n-1)/2}N(f'(u))\). Deduce that it is nonzero exactly when \(f\) is square-free.
3. **Medium.** Calculate the trace pairing of \(\mathbb F_p(t^{1/p})/\mathbb F_p(t)\) without invoking separability criteria.
4. **Medium.** Find the bad primes of \(O=\mathbb Z[\sqrt5]\), and describe their fibres. Compare with the maximal order.
5. **Hard.** Give the relative discriminant criterion for an \(O_K\)-order in a finite extension of number fields, allowing the order to be nonfree over \(O_K\).

## 6. Solutions

**1.** The basis \(1,3i\) gives the diagonal entries \(2,-18\), so the determinant is \(-36\). Reduction of the presentation \(\mathbb Z[T]/(T^2+9)\) gives \(\mathbb F_3[T]/(T^2)\). Its nonzero nilpotent \(T\) explains the degeneracy.

**2.** When \(f\) has distinct roots \(r_i\), the determinant is \(\prod_{i<j}(r_j-r_i)^2\). The norm of \(f'(u)\) is \(\prod_i f'(r_i)=(-1)^{n(n-1)/2}\prod_{i<j}(r_j-r_i)^2\). To include repeated roots and every characteristic, regard both sides as polynomials with integer coefficients in the coefficients of a universal monic polynomial. They agree over characteristic zero on the dense set of distinct-root polynomials, hence are the same universal polynomial. Specialization proves the formula for all \(f\). Over an algebraic closure, \(N(f'(u))\) is the resultant \(\operatorname{Res}(f,f')\); it is zero exactly when a root is repeated. This also follows directly from the root product formula by specialization.

**3.** Put \(u^p=t\). Multiplication by \(u^j\), \(1\le j<p\), cyclically shifts the power basis with factors of \(t\) on wraparound, so every diagonal entry is zero. Multiplication by \(1\) has trace \(p=0\). Linearity shows that every element has trace zero, and consequently every pairing entry is zero.

**4.** In \(1,\sqrt5\), the trace matrix is \(\operatorname{diag}(2,10)\), so the discriminant is \(20\). At \(2\), the fibre is \(\mathbb F_2[u]/((u+1)^2)\); at \(5\), it is \(\mathbb F_5[u]/(u^2)\). These are the only bad primes. The maximal order has basis \(1,(1+\sqrt5)/2\), index two and discriminant five. Its fibre at \(2\) is the field \(\mathbb F_4\), using \(T^2-T-1\) modulo two. Thus \(2\) is bad only because of the smaller order, whereas \(5\) ramifies in the field.

**5.** The ring \(O_K\) is Dedekind. A finite torsion-free order is free over each localization at a nonzero prime. Choose such a local basis, reduce its multiplication matrices, and apply Theorem 1.3 to the residue algebra. Changes between local bases multiply the discriminant coefficient by a unit square, so the criterion is independent of the choices and defines the relative discriminant ideal. It detects precisely the non-étale fibres and includes index primes of nonmaximal orders.

## What this lesson does not prove

The primitive element theorem [Milne FT, Theorem 5.1], the Artinian product structure [Stacks, Tag 00KJ], the local DVR characterization [Tag 034X], and the finite étale field-algebra characterization [Milne FT, Proposition 8.6 and Corollary 8.7; Stacks, Tag 00U3] are prerequisites. Dedekind’s index criterion is stated with the *Discriminants and integral bases*, Theorem 2.6 locator above. The trace-form criterion itself, including inseparable fields, is proved here. The quadratic integral-basis criterion supplies the maximal orders in the examples. Noncommutative orders use different trace conventions and are outside this theorem; [Voight] explains that setting.

## References

- **[Milne]** J. S. Milne, *Fields and Galois Theory*, Theorems 5.1 and 5.18, Proposition 8.6 and Corollary 8.7, and *Algebraic Number Theory*, Chapters 2–3 (quadratic bases in the Introduction, p. 8); [author's notes](https://www.jmilne.org/math/CourseNotes/).
- **[Stacks]** The Stacks Project, Tags [0BIE](https://stacks.math.columbia.edu/tag/0BIE), [0BVH](https://stacks.math.columbia.edu/tag/0BVH) and [0BJF](https://stacks.math.columbia.edu/tag/0BJF). The corresponding [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/discriminant.html) contains AI-proposed corrections and additions, not reviewed by the Stacks Project's maintainers.
- **[Noether]** Emmy Noether, *Der Diskriminantensatz für die Ordnungen eines algebraischen Zahl- oder Funktionenkörpers*, Journal für die reine und angewandte Mathematik **157** (1927), 82–104, especially Sections 6–8; and *Über Maximalbereiche aus ganzzahligen Funktionen*, Matematicheskii Sbornik **36** (1929), 65–72.
- **[Voight]** John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288, Springer, 2021, Chapters 7 and 9–15, [author's edition](https://math.dartmouth.edu/~jvoight/quat.html).
- **Additional prerequisite tags:** [00KJ](https://stacks.math.columbia.edu/tag/00KJ), [00U3](https://stacks.math.columbia.edu/tag/00U3), and [034X](https://stacks.math.columbia.edu/tag/034X).
