# Groups with operators

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A representation is a group together with additional operations that its homomorphisms must respect. For a module those operations are scalar multiplications. For a vector space with a linear transformation, they include that transformation. Keeping the operations visible lets us distinguish two questions: which simple factors occur in a filtration, and which indecomposable pieces occur in a direct sum? The first has a group-theoretic answer. The second requires a stronger argument about endomorphisms.

This lesson assumes the group operations, normal subgroups and cosets taught in [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30), rings and fields from [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40), and vector spaces and linear maps from [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40). A left module is an abelian group with a unital distributive ring action; we explain how that action enters the proofs. Basic references are [Noether], [MIT] and [Voight]. The module-length terminology agrees with [Stacks, Tags 00IU and 00IX].

## 1. Operations that must survive a quotient

An **operator group** is a group \(G\) together with a set \(\Omega\) and, for each \(\omega\in\Omega\), a specified endomorphism \(g\mapsto\omega(g)\). We do not require \(\Omega\) itself to be a group or ring. A subgroup \(H\) is **admissible** if \(\omega(H)\subseteq H\) for every operator. A homomorphism \(f:G\to G'\) respects the operators if

\[
f(\omega(g))=\omega(f(g)).
\]

An admissible normal subgroup \(N\) gives an operator group \(G/N\), with \(\omega(gN)=\omega(g)N\). This is well defined: if \(gN=hN\), then \(h^{-1}g\in N\), and its image under \(\omega\) is in \(N\). Kernels, images and intersections of admissible subgroups have the expected stability properties.

For a left module \(M\) over a unital ring \(R\), take its additive group and the endomorphisms \(m\mapsto rm\), for \(r\in R\). Admissible subgroups are exactly the submodules. A vector space \(V\) with a linear map \(T\) is equivalently a \(k[t]\)-module, with \(t v=T(v)\). For a possibly noncommutative ring, its two-sided ideals are the admissible subgroups of its additive group when both left and right multiplications are included.

Another example uses the group \(S_3\) and all conjugations as operators. An admissible subgroup is then a normal subgroup. These are \(1\), \(A_3\) and \(S_3\): a normal subgroup containing a transposition contains all three and hence the whole group; a nontrivial subgroup containing only even permutations contains a three-cycle and equals \(A_3\).

### Theorem 1.1. Quotients and the isomorphism theorems

The following statements hold for operator groups and homomorphisms respecting the operators.

1. A homomorphism \(f:G\to G'\) induces an isomorphism \(G/\ker f\simeq\operatorname{im}f\).
2. If \(N\triangleleft G\) and \(H\leq G\) are admissible, then \(HN\) is admissible, \(H\cap N\triangleleft H\), and
   \[
   H/(H\cap N)\simeq HN/N.
   \]
3. For admissible normal subgroups \(N\subseteq K\) of \(G\),
   \[
   (G/N)/(K/N)\simeq G/K.
   \]
4. Subgroups of \(G/N\) correspond to subgroups of \(G\) containing \(N\). The correspondence preserves admissibility and normality.

**Proof.** For (1), send \(g\ker f\) to \(f(g)\). Equality of images is equivalent to membership of \(h^{-1}g\) in the kernel, so the map is well defined and injective; it is surjective onto the stated image. The displayed operator identity makes it an operator isomorphism.

For (2), normality of \(N\) makes \(HN\) a subgroup: \((hn)(h'n')=hh'(h'^{-1}nh')n'\). Applying an operator to a product in \(HN\) keeps it in \(HN\). Conjugating an element of \(H\cap N\) by an element of \(H\) keeps it in both subgroups. Restrict the quotient map \(G\to G/N\) to \(H\). Its image is \(HN/N\), and its kernel is \(H\cap N\); (1) gives the result.

For (3), the map \(gN\mapsto gK\) is surjective, respects operators, and has kernel \(K/N\). Apply (1). For (4), the inverse operations are image and inverse image under the quotient map. If \(H\) contains \(N\), then the inverse image of its image is \(H\). If \(U\leq G/N\), surjectivity makes the image of its inverse image equal \(U\). Applying operators or conjugations before or after the quotient map proves the two preservation assertions. \(\square\)

## 2. Refining two filtrations at once

A **subnormal admissible series** is a finite chain

\[
G=G_0\supseteq G_1\supseteq\cdots\supseteq G_r=1,
\qquad G_i\triangleleft G_{i-1},
\]

whose terms are admissible. Each term need only be normal in its predecessor. A refinement inserts more terms. Two series are **equivalent** if their lists of nontrivial factors can be matched by operator isomorphisms. A **composition series** has nontrivial simple factors: a factor has no proper nontrivial admissible normal subgroup.

### Lemma 2.1. The butterfly lemma

Let \(A'\triangleleft A\) and \(B'\triangleleft B\) be admissible subgroups of an operator group. Then the following quotients are defined and operator-isomorphic:

\[
\frac{A'(A\cap B)}{A'(A\cap B')}
\simeq
\frac{B'(A\cap B)}{B'(A'\cap B)}.
\]

**Proof.** Put \(H=A\cap B\). Both \(A'\cap B\) and \(A\cap B'\) are normal admissible subgroups of \(H\), so

\[
K=(A'\cap B)(A\cap B')
\]

is a normal admissible subgroup of \(H\). Consider \(A'H/A'\). By Theorem 1.1 this is \(H/(A'\cap H)\). The image of the normal subgroup \(A\cap B'\) in this quotient is normal. Its inverse image in \(A'H\) is \(A'(A\cap B')\), proving that the first denominator is normal in the first numerator.

The surjection from \(H\) to that first quotient has kernel

\[
H\cap A'(A\cap B')=(H\cap A')(A\cap B')=K.
\]

For the middle equality, write an element of the left side as \(a'c\), with \(c\in A\cap B'\subseteq H\); then \(a'=(a'c)c^{-1}\in H\cap A'\). The reverse containment follows directly. Thus the first quotient is \(H/K\). Exchanging the two pairs proves that the second quotient is also \(H/K\), with the same operators. \(\square\)

### Theorem 2.2. Schreier refinement and Jordan–Hölder

Any two finite subnormal admissible series have equivalent refinements. Consequently, if an operator group has a composition series, any two of its composition series have the same length and the same factors up to order and operator isomorphism.

**Proof.** Write the two series as \((G_i)_{i=0}^r\) and \((H_j)_{j=0}^s\). Between \(G_i\) and \(G_{i+1}\), insert

\[
G_{i,j}=G_{i+1}(G_i\cap H_j),\qquad 0\leq j\leq s.
\]

Their endpoints are \(G_i\) and \(G_{i+1}\). Similarly insert

\[
H_{j,i}=H_{j+1}(H_j\cap G_i),\qquad 0\leq i\leq r.
\]

Lemma 2.1, applied to \(G_{i+1}\triangleleft G_i\) and \(H_{j+1}\triangleleft H_j\), proves both that successive terms are normal in their predecessors and that

\[
G_{i,j}/G_{i,j+1}\simeq H_{j,i}/H_{j,i+1}.
\]

All terms are admissible. These isomorphisms match the factors by the pairs \((i,j)\). Repeated terms contribute trivial factors and can be deleted.

If the original series are composition series, a strict insertion between consecutive terms would produce a proper nontrivial admissible normal subgroup of a simple quotient, by correspondence. Thus the refinements only add repetitions. Deleting those repetitions gives the asserted equality of lengths and multisets of factors. \(\square\)

For a module, every submodule is normal in the additive group, so a composition series is a finite filtration with simple module quotients. Its length \(\ell(M)\) is well defined by Theorem 2.2. Submodules and quotients of a finite-length module have finite length: intersect a composition series with the submodule, or project it to the quotient; every resulting nonzero factor embeds in, or is a quotient of, a simple factor and is simple. Concatenating a series for \(N\) with the inverse images of a series for \(M/N\) then gives

\[
\ell(M)=\ell(N)+\ell(M/N).
\]

It follows that strict ascending and descending chains of submodules of \(M\) have at most \(\ell(M)\) strict steps. This is the chain condition that will control endomorphisms.

**Example 2.3.** In \(\mathbb Z/12\mathbb Z\), a descending composition series is

\[
\mathbb Z/12\mathbb Z\supset 2\mathbb Z/12\mathbb Z
\supset 4\mathbb Z/12\mathbb Z\supset0.
\]

Its factors have orders \(2,2,3\). Another series uses the subgroups of orders \(4\) and \(2\), and has factor orders \(3,2,2\). The order changes, but the simple factors do not. In contrast, \(\mathbb Z\) has arbitrarily long chains \(\mathbb Z\supset2\mathbb Z\supset4\mathbb Z\supset\cdots\); it has no composition series.

## 3. Endomorphisms separate transient and persistent parts

A nonzero module is **indecomposable** if it is not the direct sum of two nonzero submodules. This is weaker than simplicity. On \(k^2\), take \(T(e_1)=0\) and \(T(e_2)=e_1\). The line \(ke_1\) is a proper submodule. Nevertheless, a decomposition into two invariant lines would make \(T\) zero, since its restriction to a one-dimensional invariant space is nilpotent and hence zero. Thus this module is indecomposable and not simple.

### Theorem 3.1. Fitting decomposition

For an endomorphism \(f\) of a finite-length module \(M\), there is an integer \(n\) such that

\[
M=\ker(f^n)\oplus\operatorname{im}(f^n).
\]

The restriction of \(f\) to the first summand is nilpotent, and its restriction to the second is an automorphism.

**Proof.** The ascending kernels and descending images stabilize. Choose \(n\) after both stabilizations, so \(\ker f^{2n}=\ker f^n\) and \(\operatorname{im}f^{2n}=\operatorname{im}f^n\). For \(x\in M\), choose \(y\) with \(f^nx=f^{2n}y\). Then

\[
x=(x-f^ny)+f^ny
\]

is the required sum. If \(z=f^ny\) also lies in \(\ker f^n\), then \(f^{2n}y=0\). Equality of the kernels gives \(f^ny=0\), so the intersection is zero. Both summands are invariant under \(f\). On the image, surjectivity follows from stabilization of images; its kernel is contained in the zero intersection. On the kernel, \(f^n=0\). \(\square\)

A ring is **local** when its nonunits form a proper two-sided ideal. Its quotient by that ideal is a division ring: a nonzero quotient class has a representative outside the ideal, hence a unit.

### Proposition 3.2. Indecomposables have local endomorphism rings

If \(M\) is a nonzero indecomposable finite-length module, every endomorphism is either nilpotent or invertible, and \(E=\operatorname{End}_R(M)\) is local.

**Proof.** Fitting's decomposition has just one nonzero summand. If its kernel summand is all of \(M\), a power of the endomorphism is zero. Otherwise its image summand is all of \(M\), and the endomorphism is invertible.

An injective endomorphism of \(M\) is surjective by length additivity applied to its image, and a surjective one is injective by the same argument applied to its kernel. Therefore, if \(a\) is a nonunit, neither \(ra\) nor \(ar\) can be a unit: a unit \(ra\) would make \(a\) injective, and a unit \(ar\) would make \(a\) surjective. Nonunits are thus closed under multiplication on either side and under negation.

A nonunit \(a\) is nilpotent, so \(1-a\) is a unit, with inverse \(1+a+\cdots+a^{m-1}\) when \(a^m=0\). If two nonunits \(a,b\) had unit sum \(u=a+b\), the two nonunits \(u^{-1}a,u^{-1}b\) would sum to \(1\). But the complement of the first must be a unit, a contradiction. Nonunits are closed under addition. They form a proper two-sided ideal, since \(1\) is a unit. \(\square\)

### Theorem 3.3. Krull–Remak–Schmidt for finite-length modules

Every finite-length module is a finite direct sum of indecomposable modules. The multiset of isomorphism classes of the summands is independent of the decomposition.

**Proof.** For existence, split a decomposable module and apply induction on length to its two smaller nonzero summands. The zero module has the empty decomposition.

For uniqueness, suppose

\[
M=A_1\oplus\cdots\oplus A_r=B_1\oplus\cdots\oplus B_s
\]

with all summands nonzero and indecomposable. Put \(A=A_1\) and \(U=\bigoplus_{i>1}A_i\). Let \(\iota_A\) and \(p_A\) be inclusion and projection for the first decomposition, and similarly \(\iota_j,q_j\) for the second. In \(\operatorname{End}_R(A)\),

\[
1_A=\sum_{j=1}^s p_A\iota_jq_j\iota_A.
\]

Since the nonunits of this ring form an ideal, at least one summand is a unit. Choose that \(j\), and write \(\alpha=p_A\iota_j:B_j\to A\), \(\beta=q_j\iota_A:A\to B_j\). Then \(\alpha\beta\) is invertible. The map \(\beta(\alpha\beta)^{-1}\) is a section of \(\alpha\), giving

\[
B_j=\beta(A)\oplus\ker\alpha.
\]

The first summand is nonzero. Indecomposability forces \(\ker\alpha=0\), so \(\alpha\) is an isomorphism and \(B_j\simeq A\).

More is needed than matching these two factors. Projection \(M\to A\) along \(U\) restricts to the isomorphism \(\alpha\) on \(B_j\). Thus every \(m\in M\) can be made an element of \(U\) by subtracting a unique element of \(B_j\), and \(B_j\cap U=0\). Hence \(M=B_j\oplus U\). Quotienting by \(B_j\) identifies \(U\) with \(\bigoplus_{k\ne j}B_k\). Apply induction on \(\ell(M)\) to these smaller modules. This matches every remaining summand and proves \(r=s\). \(\square\)

The group version has a related statement, but requires its own hypotheses. If an operator group satisfies both ascending and descending chain conditions on its admissible normal subgroups, its finite internal direct-product decompositions into directly indecomposable admissible normal subgroups have the same factors up to operator isomorphism and permutation. The projections are **normal endomorphisms**, meaning \(f(gxg^{-1})=g f(x)g^{-1}\), and must respect the operators. This is the version recorded in [Noether, §4, note 11]. We have proved the module version, where all endomorphisms respect the additive conjugations automatically.

## 4. When every invariant subspace has a complement

### Lemma 4.1. Schur's lemma

A nonzero homomorphism between simple modules is an isomorphism. In particular, the endomorphism ring of a simple module is a division ring.

**Proof.** The kernel is a submodule of the simple domain, so a nonzero map has zero kernel. Its image is a nonzero submodule of the simple codomain, so it is the whole codomain. The inverse of a bijective module homomorphism is a module homomorphism. \(\square\)

### Theorem 4.2. Complete reducibility

For any module \(M\), including modules of infinite length, the following conditions are equivalent:

1. \(M\) is a sum of simple submodules.
2. \(M\) is a direct sum of simple submodules.
3. Every submodule of \(M\) has a complementary submodule.

Such a module is called **semisimple**. Its submodules and quotients are semisimple.

**Proof.** Suppose \(M\) is a sum of simple submodules, and fix \(N\leq M\). Choose, by Zorn's lemma, a maximal family of simple submodules whose sum \(C\) is direct and satisfies \(C\cap N=0\). Unions of chains are admissible choices because any relation or element of an intersection uses only finitely many summands. If \(N+C\ne M\), at least one simple submodule \(S\) in the given sum is not contained in \(N+C\). Its intersection with \(N+C\) is a proper submodule of \(S\), hence zero. Adjoining \(S\) contradicts maximality. Thus \(M=N\oplus C\). With \(N=0\), the same construction gives (2), and for arbitrary \(N\) it gives (3).

Condition (2) implies (1). Now suppose (3). First every nonzero submodule \(V\) contains a simple submodule. Choose \(0\ne v\in V\), and consider the cyclic module \(Rv\). It has a maximal proper submodule \(P\): a chain of proper submodules cannot have union \(Rv\), since a member of such a union containing the generator would equal \(Rv\). Zorn's lemma applies. Choose \(M=P\oplus C\). Then \(Rv=P\oplus(C\cap Rv)\), and the nonzero complement is isomorphic to the simple quotient \(Rv/P\). It is the required simple submodule.

Choose a maximal direct sum \(D\) of simple submodules of \(M\). Condition (3) supplies \(M=D\oplus V\). If \(V\ne0\), the preceding paragraph supplies another simple summand, contradicting maximality. Thus \(D=M\), proving (2).

Finally, if \(M=\bigoplus S_i\) and \(p:M\to N\) is a projection onto a direct summand, the images \(p(S_i)\) are zero or simple and sum to \(N\). So submodules are semisimple by their complements. Under a quotient map, the images of the \(S_i\) are again zero or simple and generate the quotient. The equivalences prove the quotient assertion. \(\square\)

Fix an isomorphism class of simple modules, represented by \(S\). The sum of all simple submodules isomorphic to \(S\) is the **isotypic component** \(M_S\). In a decomposition into simples, project a simple submodule onto the summands. Schur's lemma makes all projections to nonisomorphic simples zero. Therefore the simple submodule lies in the direct sum of the summands of its own type. It follows that

\[
M=\bigoplus_{[S]} M_S,
\]

independently of the chosen decomposition. Every homomorphism between semisimple modules respects these components. When \(M\) has finite length, the multiplicity of \(S\) is also determined by Jordan–Hölder.

**Example 4.3.** For the nilpotent two-dimensional module in Section 3, its simple submodule \(ke_1\) has no invariant complement. A complementary line has a vector \(e_2+ce_1\), whose image under \(T\) is \(e_1\), outside that line. This shows directly why the module is not semisimple.

For a \(k\)-algebra \(A\), a module \(V\) whose scalar action agrees with its \(k\)-vector-space structure defines an algebra map \(A\to\operatorname{End}_k(V)\). Choosing a basis of an \(n\)-dimensional \(V\) turns this into \(A\to M_n(k)\). A change of basis conjugates every matrix by the same invertible matrix. Thus equivalent representations are precisely isomorphic modules. The next lessons determine which algebras force all these modules to be semisimple.

## 5. Exercises

### Exercise 5.1. Easy: the operators on a quotient

Let \(H,N\) be as in Theorem 1.1(2). Construct the isomorphism explicitly, and verify that it respects each operator. Then take \(G=\mathbb Z\), \(H=4\mathbb Z\) and \(N=6\mathbb Z\), with the integer scalar operators, and compute both quotients.

### Exercise 5.2. Medium: a butterfly with numbers

Prove the intersection identity used in Lemma 2.1 without assuming commutativity. Then take \(A=2\mathbb Z\), \(A'=6\mathbb Z\), \(B=3\mathbb Z\), \(B'=12\mathbb Z\). Compute the two butterfly quotients and their common description.

### Exercise 5.3. Medium: why a local ring appears

For an indecomposable finite-length module \(M\), prove that the sum of two noninvertible endomorphisms cannot be invertible. Apply this to \(M=k[t]/(t^3)\): calculate its endomorphism ring, its nonunits and the inverses of its units.

### Exercise 5.4. Medium: two different eigenvalue blocks

Decompose

\[
V=k[t]/(t^2)\oplus k[t]/(t-1)
\]

into indecomposables. Compute both cross-Hom spaces and show directly that every endomorphism preserves the two displayed summands. Explain how their composition factors differ from their direct summands.

### Exercise 5.5. Hard: an actual failure outside finite length

Put \(R=\mathbb Z[\theta]\), where \(\theta^2=-5\), and define \(I=(2,1+\theta)\) and \(J=(3,1+\theta)\). Prove

\[
I\oplus J\simeq R\oplus R.
\]

Show that all four factors are indecomposable, but neither \(I\) nor \(J\) is isomorphic to \(R\). Identify the finite-length hypothesis that fails. You may use the fraction field of the domain \(R\); no ideal-class computation is needed.

## 6. Solutions

### Solution 5.1

Send \(h(H\cap N)\) to \(hN\). Changing \(h\) by an element of \(H\cap N\) keeps its image unchanged. The kernel is trivial, and every element \(hnN\) has image represented by \(h\), so the map is bijective. Applying \(\omega\) to either representative gives \(\omega(h)N\), proving operator compatibility. Here \(H+N=2\mathbb Z\) and \(H\cap N=12\mathbb Z\). The two quotients are \(4\mathbb Z/12\mathbb Z\) and \(2\mathbb Z/6\mathbb Z\), both cyclic of order three. The map sends the class of \(4\) to the class of \(4\), which generates the latter quotient.

### Solution 5.2

If \(C\leq H\), an element \(x\in H\cap A'C\) has a representation \(x=a'c\). Since \(c\in H\), also \(a'=xc^{-1}\in H\cap A'\). Therefore \(H\cap A'C\subseteq(H\cap A')C\). Every element of the right side belongs to \(H\) and \(A'C\), proving equality without commutativity. Use \(C=A\cap B'\) to obtain the kernel in the butterfly proof. The normality argument and the two quotient maps in that proof then establish the whole lemma.

In the numerical example, \(A\cap B=6\mathbb Z\), \(A\cap B'=12\mathbb Z\), and \(A'\cap B=6\mathbb Z\). The first quotient is

\[
(6\mathbb Z+6\mathbb Z)/(6\mathbb Z+12\mathbb Z)=0,
\]

and the second is \((12\mathbb Z+6\mathbb Z)/(12\mathbb Z+6\mathbb Z)=0\). The common description is \(6\mathbb Z/(6\mathbb Z+12\mathbb Z)=0\). A butterfly quotient can be trivial; Schreier refinement retains it until repeated terms are removed.

### Solution 5.3

If \(a+b=u\) were invertible, \(u^{-1}a\) and \(u^{-1}b\) would still be nonunits and would sum to \(1\). Fitting's theorem makes \(u^{-1}a\) nilpotent, so \(1-u^{-1}a=u^{-1}b\) is invertible, a contradiction.

An endomorphism of \(k[t]/(t^3)\) is determined by the image of \(1\), and every image is allowed. Thus its endomorphism ring is \(k[t]/(t^3)\), acting by multiplication. An element \(c+dt+et^2\) is a unit exactly when \(c\ne0\). In that case its inverse is

\[
c^{-1}-dc^{-2}t+(d^2c^{-3}-ec^{-2})t^2.
\]

When \(c=0\), the element is nilpotent. The nonunits form the ideal \((t)\). The module is indecomposable because a decomposition would give a nontrivial idempotent in this local ring: an idempotent \(e\) in a local ring has either \(e\) or \(1-e\) invertible, forcing respectively \(e=1\) or \(e=0\).

### Solution 5.4

The first module has endomorphism ring \(k[t]/(t^2)\), a local ring by the same calculation. It is indecomposable. The second is a one-dimensional simple module with \(t\) acting as \(1\). A homomorphism from the first to the second has image killed by \(t^2\), but \(t^2\) is the identity on the second, so its image is zero. A map in the reverse direction has image killed by \(t-1\), which is invertible on the first: its inverse there is \(-1-t\). Thus it too is zero. Every endomorphism is block diagonal. The displayed decomposition is the indecomposable decomposition, unique by Theorem 3.3. Its composition factors are two copies of \(k[t]/(t)\) and one copy of \(k[t]/(t-1)\); the first two are joined inside one nonsimple indecomposable summand.

### Solution 5.5

The map \(I\oplus J\to R\), \((x,y)\mapsto x+y\), is onto because \(-2+3=1\), with \(-2\in I\) and \(3\in J\). It has a section \(r\mapsto(-2r,3r)\). Its kernel consists of \((z,-z)\) with \(z\in I\cap J\). Since \(I+J=R\), the equality \(I\cap J=IJ\) follows: choose \(i+j=1\); for \(z\) in the intersection, \(z=zi+zj\), and both products belong to \(IJ\). The other containment always holds.

The product ideal has generators \(6,2(1+\theta),3(1+\theta),(1+\theta)^2\). They are all divisible by \(1+\theta\), because \(6=(1+\theta)(1-\theta)\). Conversely, subtracting the second generator from the third gives \(1+\theta\). Hence \(IJ=(1+\theta)R\simeq R\), and the split sequence proves \(I\oplus J\simeq R\oplus R\).

The quotient \(R/I\) has two elements: modulo \(I\), \(\theta=-1\) and integers are reduced modulo \(2\). Likewise \(R/J\) has three elements. If \(I\) were principal, say \(I=(a+b\theta)\), multiplication by its nonzero generator would have determinant \(a^2+5b^2\) on the integral basis \(1,\theta\). The index of this rank-two lattice would therefore be \(a^2+5b^2=2\), which has no integer solutions. The same argument for \(J\) would require \(a^2+5b^2=3\), also impossible. An \(R\)-module isomorphism \(R\to I\) sends \(1\) to a generator of \(I\), so neither ideal is isomorphic to \(R\).

Each nonzero ideal has dimension one after tensoring with the fraction field of \(R\). In a decomposition into two nonzero submodules, both submodules are torsion-free and have positive dimension after tensoring. Their dimensions would add to one, which is impossible. Thus \(R,I,J\) are indecomposable. Finally \(R\supset2R\supset4R\supset\cdots\) is a strictly descending chain, and multiplying it by a nonzero ideal gives the same failure for \(I\) and \(J\). None has finite length. These are two decompositions of the same module whose factors cannot be matched; absence of a composition series by itself would not have established that failure.

## What this lesson does not prove

The direct-product theorem for nonabelian operator groups is stated with its chain conditions and normal projections, but its proof is not given. Its source is [Noether, §4, note 11], referring to Krull and Otto Schmidt. All module decomposition and complete-reducibility results used here have been proved, for arbitrary unital rings and, where stated, arbitrary module cardinality.

## References

- **[MIT]** *Noncommutative Algebra*, MIT OpenCourseWare, Spring 2023, instructor Roman Bezrukavnikov. Lectures 1–4 treat semisimplicity, length and Krull–Schmidt. [Course notes](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/resources/mit18_706_s23_full_lec_pdf/).
- **[Voight]** John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288, Springer, 2021, §7.2. [Author's book page](https://jvoight.github.io/quat.html).
- **[Stacks]** The [Stacks Project](https://stacks.math.columbia.edu/), Tags [00IU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-length) and [00IX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-length-independent), linked to the companion AI Integrated Stacks Project edition. That edition contains AI-proposed corrections and additions and is not reviewed by the Stacks Project's maintainers.
- **[Noether]** Emmy Noether, *Hyperkomplexe Größen und Darstellungstheorie*, written up by B. L. van der Waerden, *Mathematische Zeitschrift* **30** (1929), 641–692, §§1–5; especially §4, note 11 for direct-product uniqueness. Also *Hyperkomplexe Größen und Darstellungstheorie in arithmetischer Auffassung*, proceedings of the Bologna International Congress of Mathematicians, **2** (1928), 71–73.
