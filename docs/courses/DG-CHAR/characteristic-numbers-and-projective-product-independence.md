# Characteristic numbers and projective-product independence

*Written by GPT-6.1 Sol (OpenAI), at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra. Independently authored text dedicated under CC0.*

Characteristic classes become integer invariants when evaluated in the top dimension of a closed manifold. A change from elementary symmetric functions to monomial symmetric functions makes their behaviour on products transparent. We use it to prove independence of Chern numbers and Pontryagin numbers, first for general families with nonzero power-sum numbers and then for projective-space products.

The [Chern chapter](DG-CHAR-09.html) proves the integral classes, their full Whitney formula, root injection and projective tangent computation. The [Pontryagin chapter](DG-CHAR-10.html) proves complexification, its integral two-torsion qualification and the projective Pontryagin formula. The [manifold chapter](DG-CHAR-07.html) supplies perfect pairings, finite generation, product fundamental classes and Euler evaluation; the [Chern evaluation foundations](DG-CHAR-09.html) give signed boundary fundamental classes. The [Schubert chapter](DG-CHAR-04.html) proves the integral symmetric-polynomial theorem and cellular facts. We use their stated hypotheses, rather than treating a reference as a proof.

## 1. Top-degree numbers and orientations

A partition \(I\) of \(n\) is an unordered multiset of positive integers with sum \(n\), written in decreasing order. Its length \(\ell(I)\) is its number of parts. The empty partition has weight zero and length zero. Concatenation \(J\sqcup K\) adds multisets. Say \(I\) **refines** \(J\) if the parts of \(I\) can be grouped into blocks whose sums are the parts of \(J\).

For a closed complex \(n\)-manifold \(K\), the complex tangent bundle and its canonical real orientation define
\[
c_I[K]=\langle c_{i_1}(TK)\cdots c_{i_r}(TK),[K]\rangle\in\mathbb Z,
\qquad |I|=n.
\tag{1.1}
\]
For a closed oriented real \(4n\)-manifold \(M\), define
\[
p_I[M]=\langle p_{i_1}(TM)\cdots p_{i_r}(TM),[M]\rangle\in\mathbb Z.
\tag{1.2}
\]
If the weight does not give the manifold's top dimension, set the corresponding number to zero as a grading convention. This does not claim that the lower-degree characteristic class vanishes. All manifolds here are smooth, Hausdorff and second countable, so their closed bases are paracompact.

The Chern monomials of weight \(n\) form an integral basis of \(H^{2n}(BU(n);\mathbb Z)\). The complex Schubert cells prove its homology free in even degrees, with no odd groups; the coefficient theorem therefore makes this basis perfectly dual to \(H_{2n}(BU(n);\mathbb Z)\). If \(f:K\to BU(n)\) classifies its tangent bundle, naturality shows its Chern numbers are precisely the evaluations of this basis on \(f_*[K]\). Thus the number vector determines this universal homology class.

Reversing the orientation of \(M\) leaves its Pontryagin classes unchanged and negates its fundamental class, so negates every \(p_I[M]\). An orientation-reversing diffeomorphism identifies tangent bundles by its derivative; naturality would then make each number equal to its negative. Any nonzero Pontryagin number rules out such a diffeomorphism. The Euler number behaves differently: reversing the positive-dimensional tangent orientation negates both its Euler class and its fundamental class, and their evaluation is unchanged.

For the positive hyperplane generator \(x\) of \(\mathbb {CP}^n\), the previous chapters give
\[
c_I[\mathbb {CP}^n]=\prod_{i\in I}\binom{n+1}{i}.
\tag{1.3}
\]
For \(\mathbb {CP}^{2n}\), with its complex orientation,
\[
p_I[\mathbb {CP}^{2n}]=\prod_{i\in I}\binom{2n+1}{i}.
\tag{1.4}
\]
Both formulas use the proved positive top evaluation. In particular its \(p_1^n\) number is \((2n+1)^n\ne0\), so \(\mathbb {CP}^{2n}\), \(n\geq1\), has no orientation-reversing diffeomorphism. Complex conjugation reverses orientation on odd complex projective spaces: in a complex \(r\)-coordinate chart its real determinant has sign \((-1)^r\).

## 2. Monomial symmetric classes, integrally

For a partition \(I\), define \(m_I(t_1,\ldots,t_N)\) to be the sum of the distinct monomials whose positive exponents, as a multiset, are \(I\). Each monomial occurs once, even when parts repeat. Set \(m_{\varnothing}=1\); if \(\ell(I)>N\), set \(m_I=0\).

**Lemma 2.1.** The polynomials \(m_I\), \(|I|=n,\ell(I)\leq N\), form an integral additive basis of the symmetric homogeneous polynomials of weight \(n\). There is a unique stable integral polynomial \(s_I(e_1,\ldots,e_n)\), with \(e_j\) given weight \(j\), satisfying
\[
s_I(e_1(t),\ldots,e_n(t))=m_I(t)
\tag{2.1}
\]
whenever \(N\geq n\). The same identity holds for smaller \(N\) after setting its nonexistent elementary functions to zero.

**Proof.** Permutations partition all degree-\(n\) monomials into disjoint orbits indexed exactly by their positive exponent partitions. A symmetric polynomial has one integer coefficient on each orbit. The orbit sums therefore give the asserted basis, without dividing by a stabilizer size. The proved integral symmetric-polynomial theorem expresses each orbit sum uniquely in the elementary functions. Homogeneity makes only \(e_1,\ldots,e_n\) occur in weight \(n\). Adding a variable equal to zero preserves each orbit sum and each elementary function already present. For \(N\geq n\), algebraic independence of those elementary functions proves the expression independent of \(N\). Setting further variables equal to zero proves the assertion for smaller \(N\). ∎

Define \(s_I(c(V))\) or \(s_I(p(\xi))\) by substituting the corresponding classes in this integral polynomial. They have degrees \(2|I|\) and \(4|I|\), respectively. Their numbers use the top-degree grading convention of Section 1.

For a one-part partition \((j)\), write \(s_j\). It is a power sum, rather than the \(j\)-th elementary class. In particular
\[
s_1=e_1,\quad s_2=e_1^2-2e_2,\quad
s_3=e_1^3-3e_1e_2+3e_3,
\]
\[
s_{1,1}=e_2,\qquad s_{2,1}=e_1e_2-3e_3,\qquad
s_{1,1,1}=e_3.
\tag{2.2}
\]
For example \(e_1e_2\) contains every monomial with exponents \(2,1\) once and each three-distinct-variable monomial three times, proving the displayed mixed formula.

All power sums can be computed without denominators. Differentiate the formal polynomial
\(E(z)=\prod_i(1+t_i z)=\sum_j e_j z^j\). Its logarithmic derivative is the formal series
\[
\frac{E'(z)}{E(z)}
=\sum_i\frac{t_i}{1+t_i z}
=\sum_{j\geq1}(-1)^{j-1}s_j z^{j-1}.
\]
Multiplying by \(E(z)\) and comparing coefficients proves
\[
s_j-e_1s_{j-1}+e_2s_{j-2}-\cdots
+(-1)^{j-1}e_{j-1}s_1+(-1)^j j e_j=0.
\tag{2.3}
\]
Here inverse series are formal, with constant coefficient one; each coefficient uses finitely many terms. This supplies an integral recursive calculation and proves (2.2)'s power-sum formulas.

In weight \(n\) with \(N\geq n\), both the elementary monomials \(e_I\) and the orbit sums \(m_I\) are bases of the same free abelian group. Their change-of-basis matrix is therefore invertible over \(\mathbb Z\), with determinant \(+1\) or \(-1\). Thus the numbers \(s_I(c)[K]\) are integral linear combinations of Chern numbers, with an integral inverse change of coordinates. The same stable polynomial change applies to Pontryagin monomials; this is an algebraic change of coordinates, without asserting a geometric splitting of every real bundle into oriented two-planes.

**Proposition 2.2 — Even Chern exponents.** If \(V\) is a complex bundle on a paracompact Hausdorff base and \(2I\) denotes the partition obtained by doubling every part of \(I\), then
\[
s_{2I}(c(V))=s_I(p(V_{\mathbb R}))
\tag{2.4}
\]
as integral classes.

**Proof.** On the injective complex flag space let \(t_j\) be the Chern line roots. The proved Pontryagin root formula gives \(p(V_{\mathbb R})=\prod_j(1+t_j^2)\). Its orbit sum \(m_I(t_1^2,\ldots,t_r^2)\) is exactly \(m_{2I}(t_1,\ldots,t_r)\): doubling every positive exponent is a bijection of the distinct monomials. Integral flag injection proves (2.4) on the base. In particular \(s_{2j}(c)=s_j(p)\), and \(s_{2,\ldots,2}(c)=p_j\) with \(j\) parts. This equality needs no two-torsion qualification because the real bundle in question underlies a complex bundle. ∎

## 3. The full product formula

**Theorem 3.1.** For complex bundles on a paracompact Hausdorff base,
\[
s_I(c(V\oplus W))
=\sum_{J\sqcup L=I}s_J(c(V))s_L(c(W)).
\tag{3.1}
\]
The sum is over distinct ordered pairs of partitions, including the empty partition. For real bundles on such a base the analogous formula with \(p\) has a difference annihilated by two.

**Proof.** In formal root variables \(t\) and \(u\), each distinct monomial contributing to \(m_I(t,u)\) has a unique multiset \(J\) of positive exponents on the \(t\) variables and a unique multiset \(L\) on the \(u\) variables. Its contribution for that pair is exactly \(m_J(t)m_L(u)\). Conversely every term of that product has exponent multiset \(I\). This proves the orbit identity with coefficient one for each pair; repeated parts create no binomial multiplicities.

Take each formal list to have at least \(|I|\) variables, so the elementary functions of that weight on each list are algebraically independent. Express the identity in them using Lemma 2.1 and the symmetric-polynomial theorem. The elementary functions of the combined variables are the coefficient convolution of the two sequences. Thus this is an integral polynomial identity in the two independent sequences. Substitute any actual Chern sequences, including their zeros above the ranks; Chern Whitney proves (3.1).

For Pontryagin classes, every difference between a direct-sum coefficient and that coefficient convolution is annihilated by two, by the proved Pontryagin Whitney theorem. Substituting in any integral polynomial changes its value by a sum of products containing at least one such difference: telescope each monomial's factors. Every product, and hence their sum, is annihilated by two. Applying the same polynomial identity proves the asserted qualification. No formal root variable was asserted to be an actual real-bundle root. ∎

In particular \(s_j(c(V\oplus W))=s_j(c(V))+s_j(c(W))\), since a one-part partition has just the two decompositions with one part empty. The same statement for \(s_j(p)\) has its two-torsion qualification.

**Corollary 3.2 — Numbers of products.** For closed complex manifolds \(K^a,L^b\),
\[
s_I(c)[K\times L]
=\sum_{\substack{J\sqcup T=I\\|J|=a,\ |T|=b}}
s_J(c)[K]\,s_T(c)[L].
\tag{3.2}
\]
For closed oriented manifolds of real dimensions \(4a,4b\), the identical formula holds for Pontryagin numbers, as an exact integer equality.

**Proof.** The tangent bundle of a product is the sum of the pulled-back tangent bundles, by differentiating the product charts; for complex charts this is a complex-linear identification. Apply Theorem 3.1. Evaluation on the ordered product fundamental class factors into the two evaluations, by the previously proved chain external product. Only terms of top degree on both factors contribute. All characteristic degrees are even, so there is no multiplication sign. The Pontryagin error is annihilated by two, whose integer evaluation is necessarily zero. This proves its exact numerical equality as well. ∎

If an oriented product of total real dimension \(4n\) has a factor whose dimension is not divisible by four, every Pontryagin number is zero. Indeed in the product expansion all classes on each factor have degree divisible by four; none can have that factor's top degree. In any nontrivial product with both factors of positive dimension, the top one-part \(s\)-number is zero: its additive formula is pulled back from degrees strictly above the dimensions of the factors.

Projective tangent stabilization gives
\[
s_j(c(T\mathbb {CP}^a))=(a+1)x^j,\qquad
s_j(p(T\mathbb {CP}^{2a}))=(2a+1)x^{2j}.
\tag{3.3}
\]
For the first equality, the stable bundle has \(a+1\) identical Chern roots \(x\), and the trivial line has zero power sum. For the second use the already proved polynomial \(p=(1+x^2)^{2a+1}\), interpreting its coefficients as elementary functions of \(2a+1\) formal copies of \(x^2\). Lemma 2.1 allows this stable polynomial substitution; it is not a real geometric splitting claim. Taking top evaluations gives
\[
s_a(c)[\mathbb {CP}^a]=a+1,\qquad
s_a(p)[\mathbb {CP}^{2a}]=2a+1.
\tag{3.4}
\]
These nonzero top power-sum numbers obstruct a nontrivial product decomposition of the corresponding complex or oriented manifold of the indicated types, by Corollary 3.2.

## 4. Triangular matrices and independence

**Theorem 4.1 — Chern numbers.** Fix \(n\geq1\). Suppose for each \(1\leq j\leq n\) a closed complex \(j\)-manifold \(K_j\) is chosen with \(s_j(c)[K_j]\ne0\). For a partition \(J=(j_1,\ldots,j_q)\) of \(n\), put \(K_J=K_{j_1}\times\cdots\times K_{j_q}\). The matrix
\[
\bigl(c_I[K_J]\bigr)_{I,J\vdash n}
\tag{4.1}
\]
is nonsingular over \(\mathbb Q\). Its determinant has absolute value
\[
\prod_{J\vdash n}\ \prod_{j\in J}|s_j(c)[K_j]|.
\tag{4.2}
\]
In particular all the Chern-number functionals of complex dimension \(n\) are linearly independent over \(\mathbb Q\), as witnessed by products of complex projective spaces.

**Proof.** Replace the row coordinates \(c_I\) by \(s_I(c)\); Lemma 2.1 gives an integral invertible change of basis, so changes the determinant only by a sign. Iterate (3.2). A nonzero term in \(s_I(c)[K_J]\) requires a tuple of partitions \(I_1,\ldots,I_q\) of weights \(j_1,\ldots,j_q\), with multiset union \(I\). Thus \(I\) refines \(J\), and necessarily \(\ell(I)\geq\ell(J)\). If these lengths are equal, every \(I_a\) has exactly one part, because its weight \(j_a\) is positive. Hence \(I=J\). The diagonal entry is precisely \(\prod_{j\in J}s_j(c)[K_j]\): there is one distinct tuple of singleton partitions, even when parts repeat.

Order partitions by increasing length, and in any order within each length. The resulting \(s\)-matrix is lower triangular, with no off-diagonal entries inside each equal-length block and with the stated nonzero diagonal. Its determinant is the diagonal product. Undoing the integral row change proves (4.1)–(4.2). Taking \(K_j=\mathbb {CP}^j\) satisfies the hypothesis by (3.4). A rational linear relation between Chern numbers valid for every complex manifold would vanish on all these columns; the nonsingular matrix makes each coefficient zero. ∎

**Theorem 4.2 — Pontryagin numbers.** If closed oriented \(4j\)-manifolds \(M_j\), \(1\leq j\leq n\), satisfy \(s_j(p)[M_j]\ne0\), the matrix
\[
\bigl(p_I[M_{j_1}\times\cdots\times M_{j_q}]\bigr)_{I,J\vdash n}
\tag{4.3}
\]
is nonsingular over \(\mathbb Q\), with absolute determinant \(\prod_{J\vdash n}\prod_{j\in J}|s_j(p)[M_j]|\). Products of the \(M_j=\mathbb {CP}^{2j}\) therefore witness rational independence of all Pontryagin-number functionals in dimension \(4n\).

**Proof.** The numerical Pontryagin product formula (3.2) is an exact integer equality, despite the two-torsion qualification of its bundle-class formula. Its iterated expansion has exactly the same partition tuples. A surviving term requires refinement; equal lengths force equal partitions; the diagonal entry is the product of the nonzero one-part numbers. The stable integral symmetric-polynomial change of coordinates takes \(p_I\) to \(s_I(p)\) and is invertible over \(\mathbb Z\). Thus the same triangular determinant argument proves the theorem. Formula (3.4) gives the projective choice \(s_j(p)[\mathbb {CP}^{2j}]=2j+1\ne0\), and nonsingularity rules out a nonzero rational relation valid on every oriented manifold. ∎

All factor dimensions are even, so permuting factors preserves their product orientation; thus the products indexed by unordered partitions are unambiguous for these numbers. The empty-partition case \(n=0\) is the one-by-one matrix of the positively oriented point, with entry one. The stated nonsingularity is over \(\mathbb Q\). Its nonunit integer determinants do not assert that all integer number vectors are attained.

For \(n=2\), use the column order \(\mathbb {CP}^2,\mathbb {CP}^1\times\mathbb {CP}^1\) and row order \(c_1^2,c_2\). The matrix is
\[
\begin{pmatrix}9&8\\3&4\end{pmatrix},\qquad \det=12.
\tag{4.4}
\]
For Pontryagin numbers, use columns \(\mathbb {CP}^4,\mathbb {CP}^2\times\mathbb {CP}^2\) and rows \(p_1^2,p_2\):
\[
\begin{pmatrix}25&18\\10&9\end{pmatrix},\qquad \det=45.
\tag{4.5}
\]
Indeed on the second product, \(p=(1+3x^2)(1+3y^2)\), where \(x^3=y^3=0\) and \(x^2y^2\) evaluates to one. Thus \(p_1^2=18x^2y^2\) and \(p_2=9x^2y^2\). Changing to the rows \(s_2,s_{1,1}\) gives respectively
\[
\begin{pmatrix}3&0\\3&4\end{pmatrix},\qquad
\begin{pmatrix}5&0\\10&9\end{pmatrix},
\]
which display the triangular mechanism directly.

## 5. Boundaries and the rational Chern character

**Proposition 5.1 — Pontryagin numbers of a boundary.** If a closed oriented \(4n\)-manifold \(M\), \(n\geq1\), is the outward-oriented boundary of a compact oriented manifold \(W\), every Pontryagin number of \(M\) is zero.

**Proof.** Choose a smooth metric on \(W\), using half-space charts and the proved smooth partitions of unity. Along \(M\) its orthogonal normal line has a unique unit vector pointing outward. The inward half-space direction in each boundary chart identifies that choice; changes of boundary chart preserve its inward sign. It is therefore a smooth global nonzero normal field. Hence \(TW|_M\cong TM\oplus\varepsilon^1\) as real bundles. Pontryagin stability is an exact equality, so each \(p_i(TM)\) is the restriction of \(p_i(TW)\). The signed relative fundamental class already proved in the Chern chapter satisfies \(\partial[W,M]=[M]\). Exactness of the pair sequence gives \(i_*[M]=0\) in \(H_{4n}(W;\mathbb Z)\). For \(I\vdash n\),
\[
p_I[M]=\langle i^*p_I(TW),[M]\rangle
=\langle p_I(TW),i_*[M]\rangle=0.
\]
This proves the assertion in integers, including all component sums. ∎

Consequently no positive multiple of \(\mathbb {CP}^{2n}\) is an oriented boundary, since its positive \(p_1^n\) number is nonzero and numbers add over disjoint unions. The Euler number supplies a different kind of information: an even-dimensional sphere bounds its disk but has Euler number two. Euler class is not stable under adding the boundary's normal line.

For a finite-rank complex bundle \(V\), define the rational **Chern character** in the degree completion of cohomology by
\[
\operatorname{ch}(V)=\operatorname{rank}V+
\sum_{j\geq1}\frac{s_j(c(V))}{j!}.
\tag{5.1}
\]
Each degree is a well-defined rational class; on a finite-dimensional manifold the sum truncates. Naturality follows from Chern naturality.

On paracompact Hausdorff bases this character is uniquely characterized by naturality, sum additivity and its value \(e^{c_1(\gamma)}\) on the universal complex line over \(\mathbb {CP}^{\infty}\). Indeed classification makes its value on every line the corresponding exponential. Pull back an arbitrary finite-rank bundle to its injective flag space, split it into lines, and use additivity. Every degree is then forced to be the sum of their exponentials, which is (5.1); injectivity proves uniqueness on the base. Conversely the definition has that line value and the additivity proved next.

**Proposition 5.2.** On a paracompact Hausdorff base,
\[
\operatorname{ch}(V\oplus W)=\operatorname{ch}(V)+\operatorname{ch}(W),
\qquad
\operatorname{ch}(V\otimes W)=\operatorname{ch}(V)\operatorname{ch}(W).
\tag{5.2}
\]
For a real bundle \(\xi\), its rational complexification character has zero odd-index components and
\[
\operatorname{ch}_{2j}(\xi_{\mathbb C})
=\frac{2s_j(p(\xi))}{(2j)!},\qquad j\geq1.
\tag{5.3}
\]

**Proof.** The one-part case of (3.1) and rank additivity prove the first formula. On a common injective flag space, \(V\) and \(W\) split with line roots \(t_i,u_l\). The proved tensor formula for complex lines makes their tensor product roots \(t_i+u_l\). Equation (5.1) on that space is \(\sum_i e^{t_i}\), so the formal binomial identity \(e^{t+u}=e^t e^u\) proves the tensor formula. Injective flag pullback with rational coefficients proves it on the base. These are formal series identities; each homogeneous coefficient is finite.

For the last statement, the conjugate isomorphism of \(\xi_{\mathbb C}\) and the Chern conjugation rule make all its odd Chern classes zero rationally. Put \(C(z)=\sum_k c_k(\xi_{\mathbb C})z^k\) and \(P(t)=\sum_i p_i(\xi)t^i\). The definition of \(p_i\) gives \(C(z)=P(-z^2)\). Taking formal logarithmic derivatives, (2.3)'s generating identity gives
\[
\frac{C'(z)}{C(z)}
=\sum_{k\geq1}(-1)^{k-1}s_k(c)z^{k-1}
=-2\sum_{j\geq1}s_j(p)z^{2j-1}.
\]
Thus the odd power sums are zero and \(s_{2j}(c)=2s_j(p)\). Divide by the factorial in (5.1) to obtain (5.3). This part is an algebraic consequence of natural complexification and works on every Hausdorff base; the flag and tensor statements have their paracompact hypotheses. ∎

The same root calculation makes dualization and conjugation transparent. On a paracompact Hausdorff base, their line roots are \(-t_i\), so in degree \(2j\), including the rank component at \(j=0\),
\[
\operatorname{ch}_j(V^*)=\operatorname{ch}_j(\overline V)
=(-1)^j\operatorname{ch}_j(V).
\]
Injective flag pullback proves the identity on the base. The already proved bundle isomorphism \((V_{\mathbb R})_{\mathbb C}\cong V\oplus\overline V\) therefore cancels the odd-index character components and doubles the even-index ones. This explains the factor two in (5.3) when the real bundle underlies a complex bundle, and the computation in Exercise 6.6.

## 6. Exercises with solutions

**Exercise 6.1 — Easy.** Compute \(s_2(c)[\mathbb {CP}^2]\) and \(s_1(c)[\mathbb {CP}^1\times\mathbb {CP}^1]\). Distinguish a lower-degree class from a number.

**Solution.** On \(\mathbb {CP}^2\), \(c_1=3x,c_2=3x^2\), so \(s_2=c_1^2-2c_2=3x^2\), whose number is three. The second requested expression has weight one on a complex two-manifold. Its number is therefore zero by the explicit grading convention; it is not an evaluation of a degree-two class on a degree-four cycle. The class itself is nonzero: with \(x,y\) the two positive factor generators, \(s_1=c_1=2x+2y\). In top degree \(s_{1,1}=c_2=4xy\) has number four, whereas \(s_2=0\) has number zero. This preserves the requested calculation while correcting its degree interpretation.

**Exercise 6.2 — Medium.** Prove the \(s\)-number product formula and explain why repeated parts do not produce extra combinatorial coefficients.

**Solution.** Each orbit monomial in the combined root variables has a unique positive-exponent multiset on the first root block and on the second. The product of the two corresponding orbit sums contains that monomial exactly once. Thus the sum is indexed by distinct partition pairs with multiset union \(I\), with coefficient one per pair. Substitute elementary Chern classes and apply tangent Whitney, then evaluate on the product fundamental class. Only partition pairs of the respective top weights survive, proving (3.2). For \(I=(1,1)\) on two complex curves, the only surviving pair is \(((1),(1))\), so its number is the product of their \(s_1\) numbers. On two projective lines this is \(2\cdot2=4\), not twice this number. Pontryagin numbers obey the same exact formula because the class error is annihilated by two and has integer evaluation zero.

**Exercise 6.3 — Medium.** Prove the Pontryagin independence theorem in weight two by computing its matrix on \(\mathbb {CP}^4\) and \(\mathbb {CP}^2\times\mathbb {CP}^2\).

**Solution.** The first space has \(p_1=5x^2,p_2=10x^4\), so its \(p_1^2,p_2\) numbers are \(25,10\). On the second, \(p_1=3x^2+3y^2,p_2=9x^2y^2\), and \(x^3=y^3=0\). Thus its numbers are \(18,9\). The specified row/column order gives (4.5), with determinant \(225-180=45\ne0\). No rational linear combination of the two functionals can vanish on both columns except the zero one. The change to \(s_2=p_1^2-2p_2,s_{1,1}=p_2\) gives the triangular matrix with diagonal \(5,9\), recovering the general proof's mechanism.

**Exercise 6.4 — Hard.** Prove general Chern-number independence from a family \(K_j\) with \(s_j(c)[K_j]\ne0\). State the projective specialization.

**Solution.** The monomial orbit sums and elementary monomials are integral bases of symmetric polynomials of weight \(n\). Their invertible integer transition matrix converts the Chern-number rows into the \(s_I\) rows. On the product \(K_J\), an iterated product term survives only if its exponent partition \(I\) splits into nonempty partitions of the factor weights. Hence \(I\) refines \(J\). Arrange the partitions by increasing length. Terms above the diagonal vanish; within equal-length blocks a surviving term forces one part per factor and therefore \(I=J\). The diagonal is \(\prod_{j\in J}s_j[K_j]\), with no factorial from repeated parts. Every diagonal entry is nonzero, so the determinant is their nonzero product; undoing the integral row change proves the theorem. With \(K_j=\mathbb {CP}^j\), the diagonal factors are \(j+1\), by (3.4). This proves independence on explicit products, and therefore independence as functionals on all closed complex \(n\)-manifolds. Its integer determinant is generally not a unit.

**Exercise 6.5 — Medium.** Prove Pontryagin boundary-number vanishing and explain why the same conclusion for Euler numbers would be false.

**Solution.** The outward-normal splitting \(TW|_M=TM\oplus\varepsilon\) and exact Pontryagin stability extend every top characteristic product from \(M\) to \(W\). The outward-boundary identity \(\partial[W,M]=[M]\) puts its fundamental class in the kernel of inclusion to \(W\). The evaluation of each extending product is therefore zero, exactly as in Proposition 5.1. On the other hand, \(S^{2r}\), \(r\geq1\), bounds the oriented disk \(D^{2r+1}\) and has Euler number two. Its tangent Euler class does not extend by the stated stable argument: Euler class is not stable on adding a nonzero trivial line.

**Exercise 6.6 — Medium.** Compute \(\operatorname{ch}(T\mathbb {CP}^2)\) and the character of its underlying real tangent bundle after complexification.

**Solution.** The complex rank is two, \(s_1=3x\) and \(s_2=3x^2\), with all higher-degree terms zero on this manifold. Hence
\[
\operatorname{ch}(T\mathbb {CP}^2)=2+3x+\frac32x^2.
\]
The complexification of its underlying real bundle is \(V\oplus\overline V\), as proved in the Pontryagin chapter. Conjugation negates the degree-two component and preserves the degree-four component. Additivity gives \(4+3x^2\). Formula (5.3) gives the same answer: its real rank is four and \(\operatorname{ch}_2=p_1=3x^2\). The rational number \(3/2\) here is a Chern-character evaluation, whereas the integral top Chern number is \(c_2[M]=3\); the definitions and their factorials are different.

## Sources and scope

Freely accessible comparisons for this pass are Allen Hatcher, [*Vector Bundles and K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), printed p.63 for the stable Newton polynomials and pp.109–110 for the Chern character and its complete sum/tensor proof, and Haynes Miller, [*Lectures on Algebraic Topology II*, Lecture 40](https://ocw.mit.edu/courses/18-906-algebraic-topology-ii-spring-2020/e8a061a73ca1a451df8809c7a7fbc846_MIT18_906S20_notes.pdf). Hatcher states the symmetric-polynomial theorem by reference; our Schubert chapter proves it integrally. Miller states the projective-generator conclusion with its number calculation abbreviated; the orbit-basis and triangular determinant proofs above supply the complete independence argument. No stable homotopy or bordism conclusion is needed for that argument. The formal completion in the character definition is explicit, including bases with unbounded cohomological dimension.

The product formula, numerical evaluation, projective calculation and rational independence theorem are proved above. The boundary-number proof uses the earlier signed relative fundamental class and the Pontryagin stability proved in the preceding chapter. The rational character and even-exponent comparison include their full algebraic arguments.

All numbers have their explicit top-degree and orientation conventions. Chern Whitney/root and Pontryagin Whitney calculations use paracompact Hausdorff bases; natural definitions and the complexification character identity have the stated broader Hausdorff scope. Two-torsion can affect the integral bundle-class formula and vanishes in these integer numerical evaluations. Independence is rational; this chapter asserts no unrestricted integral realization of number vectors. The writing AI's check is distinct from independent review. The complete assigned teaching and proof prerequisites are now supplied across the course.
