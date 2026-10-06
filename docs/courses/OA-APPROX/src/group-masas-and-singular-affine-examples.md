# Group MASAs and singular affine examples

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text: public domain (CC0).*

Fourier coefficients turn commutation with a subgroup into a condition on conjugacy orbits. A second coefficient calculation detects unitary normalizers: a finite support can be moved so that a chosen coefficient contributes its squared absolute value without cancellation. For affine groups over infinite fields, this proves singularity of a MASA.

The [regular-group operator foundations](regular-group-operator-foundations.md) prove the regular commutant, faithful normal trace, Fourier-support test and subgroup expectation directly. Its H03 proves separable predual for a countable group, and H04 proves that an infinite-dimensional tracial factor has type \(\mathrm{II}_1\). The group trace and expectation require no ICC hypothesis; ICC enters only in the factor conclusion.

The freely readable comparison is [Sinclair–Smith, *The Pukánszky invariant for masas in group von Neumann factors*](https://people.tamu.edu/~rrsmith/papers/pukanszky.pdf), Example 5.1, manuscript pp. 15–17: it treats rational affine groups and particular infinite dilation subgroups. Sections 3–6 below prove the extension to every countably infinite field and every infinite dilation subgroup. The finite-support coefficient argument in Sections 4–5 is given in full. For the group trace, regular commutation and trace expectation used in Section 1, see [Anantharaman–Popa, *An introduction to II1 factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), §1.3.1, Lemma 1.3.4 through Proposition 1.3.9, and Theorem 9.1.2 with Remark 9.1.3.

## 1. Fourier coefficients and subgroup expectations

Let \(G\) be a countable discrete group with identity \(e\). Our conventions are
\[
\lambda_g\delta_t=\delta_{gt},\qquad
\rho_g\delta_t=\delta_{tg^{-1}},\qquad
M=L(G)=\lambda(G)''.
\tag{1}
\]
Both are representations, and their operators commute. The vector \(\delta_e\) is cyclic for each. It is therefore separating for \(M\), and
\[
\tau(x)=\langle\delta_e,x\delta_e\rangle
\tag{2}
\]
is faithful and normal. The direct matrix calculation in [G01](regular-group-operator-foundations.md#g01) proves traciality for all bounded operators of \(M\). Inner products are linear in the second variable.

For \(x\in M\), define
\[
\widehat x(g)=\tau(\lambda_g^*x),\qquad
x\delta_e=\sum_{g\in G}\widehat x(g)\delta_g,
\qquad \|x\|_2^2=\sum_g|\widehat x(g)|^2.
\tag{3}
\]
These are Hilbert-space expansions, not assertions of operator-norm Fourier convergence. In particular, \(\tau(x^*y)=\langle x\delta_e,y\delta_e\rangle\), so trace Cauchy–Schwarz follows from Hilbert-space Cauchy–Schwarz.

For a subgroup \(H\), write \(A=L(H)\subset M\). The subgroup compression proved in [G03](regular-group-operator-foundations.md#g03) gives the trace expectation \(E_A\). On trace vectors it is the orthogonal projection onto \(\overline{A\delta_e}=\ell^2(H)\). Consequently
\[
\widehat{E_A(x)}(g)=1_H(g)\widehat x(g).
\tag{4}
\]
In particular, a bounded operator of \(M\) whose coefficients vanish outside \(H\) lies in \(A\): it has the same vector at \(\delta_e\) as \(E_A(x)\), and that vector determines the operator.

If every nonidentity conjugacy class of \(G\) is infinite, a central operator has coefficients constant on those classes. Square summability kills all coefficients except the identity coefficient. Thus \(M\) is a factor. For infinite \(G\), its group unitaries are an infinite orthonormal family in \(L^2(M,\tau)\), so the finite factor is infinite dimensional and has type \(\mathrm{II}_1\).

## 2. The subgroup-orbit MASA criterion

**Theorem 2.1.** For an abelian subgroup \(H\subset G\), \(L(H)\) is maximal abelian in \(L(G)\) if and only if
\[
\{hgh^{-1}:h\in H\}\text{ is infinite for every }g\notin H.
\tag{5}
\]
The theorem does not require that \(G\) be ICC.

**Proof.** If \(x\in A'\cap M\), the equality \(\lambda_hx\lambda_h^*=x\) makes its coefficients constant on the \(H\)-conjugacy orbits. Under (5), (3) forces \(\widehat x(g)=0\) outside \(H\). Equation (4) gives \(x\in A\). Since \(A\) is abelian, this is the MASA property.

Conversely suppose the orbit \(\mathcal O\) of some \(g\notin H\) is finite. The operator
\[
s=\sum_{t\in\mathcal O}\lambda_t
\tag{6}
\]
commutes with every \(\lambda_h\), because conjugation permutes its summands. It is nonzero, since \(s\delta_e\) is a nonzero finite sum of distinct basis vectors. None of those basis vectors belongs to \(\ell^2(H)\): if \(hgh^{-1}\in H\), then \(g\in H\). Hence \(s\notin A\), and \(A\) is not maximal abelian. \(\square\)

In an infinite group, this criterion immediately excludes finite abelian subgroups from being MASAs. Every orbit of a finite subgroup is finite, and the group has an element outside that subgroup.

## 3. Affine groups and malnormal dilations

Let \(K\) be a countably infinite field and \(H\subset K^\times\) an infinite multiplicative subgroup. Use the same letter for its embedded dilation subgroup, and put
\[
G=K\rtimes H=\{(a,b):a\in H,\ b\in K\},
\qquad (a,b)(c,d)=(ac,b+ad),
\qquad H=\{(a,0):a\in H\}.
\tag{7}
\]
The element \((a,b)\) represents the affine map \(t\mapsto at+b\). Its inverse is \((a^{-1},-a^{-1}b)\).

**Proposition 3.1.** This group is ICC, and its dilation algebra \(A=L(H)\) is a MASA in the separable \(\mathrm{II}_1\) factor \(L(G)\). Moreover,
\[
h g k^{-1}=g,\quad g\notin H,\ h,k\in H
\quad\Longrightarrow\quad h=k=e.
\tag{8}
\]

**Proof.** Conjugation by a translation gives
\[
(1,c)(a,b)(1,c)^{-1}=(a,b+(1-a)c).
\tag{9}
\]
If \(a\ne1\), this yields infinitely many conjugates as \(c\) varies in \(K\). For a nonidentity translation \((1,b)\), conjugating by dilations gives \((1,hb)\), \(h\in H\), an infinite set because \(b\ne0\). This proves ICC.

For any \(g=(a,b)\notin H\), we have \(b\ne0\), and its \(H\)-conjugacy orbit contains all \((a,hb)\). Theorem 2.1 gives the MASA conclusion. [H03](regular-group-operator-foundations.md#h03) proves separable predual from countability.

Finally, write \(h=(s,0)\), \(k=(t,0)\). The left side of (8) is \((sa/t,sb)\). Equality with \((a,b)\), with \(b\ne0\), forces \(s=1\) and then \(t=1\). This is the malnormality condition \(H\cap gHg^{-1}=\{e\}\). \(\square\)

The full affine group is the case \(H=K^\times\). Keeping an arbitrary infinite dilation subgroup will also give all the finite multiplicities constructed in the [field-tower lesson](finite-field-towers-and-masa-multiplicities.md).

## 4. A collision-free coefficient estimate

For finite-support functions, convolution and involution are
\[
(x*y)(r)=\sum_{st=r}x(s)y(t),\qquad
x^*(s)=\overline{x(s^{-1})}.
\tag{10}
\]
Thus \(\lambda(x^*)=\lambda(x)^*\). The complex conjugate in (10) is essential: it makes the adjoint coefficient products squared absolute values. The same involution appears in Anantharaman–Popa, Proposition 1.3.5, printed p. 7; this is the printed source referred to in Exercise 5.

**Lemma 4.1.** Let \(x\) be supported by a finite set \(B\subset G\). Suppose \(g_0,g_1\in G\) have the property
\[
r^{-1}g_1r'=g_1,\quad r,r'\in Bg_0^{-1}
\quad\Longrightarrow\quad r=r'.
\tag{11}
\]
Then the following coefficient is a nonnegative real number and satisfies
\[
|x(g_0)|^2\le (x^**\delta_{g_1}*x)(g_0^{-1}g_1g_0).
\tag{12}
\]

**Proof.** Expand the right side as
\[
\sum_{\substack{s,t\in B\\s^{-1}g_1t=g_0^{-1}g_1g_0}}
\overline{x(s)}x(t).
\tag{13}
\]
Putting \(r=sg_0^{-1}\), \(r'=tg_0^{-1}\) turns the constraint into (11). Hence every surviving pair has \(s=t\), and every surviving term is \(|x(s)|^2\). The pair \(s=t=g_0\) survives if \(g_0\in B\). If it does not, \(x(g_0)=0\), and the same nonnegativity proves the inequality. \(\square\)

**Lemma 4.2.** In the affine group (7), for every finite \(B\subset G\) and \(g_0\notin H\), there is \(g_1\in H\) such that
\[
g_0^{-1}g_1g_0\notin H,
\qquad r^{-1}g_1r'=g_1\ (r,r'\in B)\Longrightarrow r=r'.
\tag{14}
\]

**Proof.** Write \(g_1=(t,0)\). For \(r=(a,b)\), \(r'=(a',b')\), the equation in (14) is equivalent to \(g_1r'=rg_1\), hence to
\[
a'=a,\qquad tb'=b.
\tag{15}
\]
For a distinct pair with \(a'=a\), either it has no solution in \(K^\times\), or it excludes just one value of \(t\). Only finitely many values are excluded by all pairs in \(B\).

If \(g_0=(a_0,b_0)\), \(b_0\ne0\), then
\[
g_0^{-1}(t,0)g_0=(t,a_0^{-1}(t-1)b_0).
\tag{16}
\]
It lies outside \(H\) whenever \(t\ne1\). The infinite subgroup \(H\) contains a value avoiding \(1\) and the finitely many pair exclusions. \(\square\)

To use Lemma 4.1, apply Lemma 4.2 to \(Bg_0^{-1}\). This translated support, rather than \(B\) itself, is exactly the support required in (11).

## 5. Singularity without an operator-norm truncation assumption

A MASA \(A\subset M\) is **singular** if every unitary \(u\) satisfying \(uAu^*=A\) belongs to \(A\).

**Theorem 5.1.** The affine dilation MASA of Proposition 3.1 is singular for every infinite \(H\subset K^\times\).

**Proof.** Let \(u\) be a unitary normalizer and fix \(g_0\notin H\). Choose finite sets \(B\) containing \(g_0\) and exhausting \(G\), and define the Fourier truncations
\[
x_B=\sum_{s\in B}\widehat u(s)\lambda_s.
\tag{17}
\]
Equation (3) gives \(\delta_B=\|u-x_B\|_2\to0\) and \(\|x_B\|_2\le1\). No uniform bound on \(\|x_B\|\) is asserted or needed.

Choose \(g_1\) from Lemma 4.2 for \(Bg_0^{-1}\), and let \(r_0=g_0^{-1}g_1g_0\notin H\). Since \(u^*\lambda_{g_1}u\in A\), its coefficient at \(r_0\) is zero. For arbitrary group unitaries \(v,w\), trace Cauchy–Schwarz gives
\[
\left|\tau\bigl(v^*(u^*wu-x_B^*wx_B)\bigr)\right|
\le \|u-x_B\|_2\bigl(\|u\|_2+\|x_B\|_2\bigr)
\le2\delta_B.
\tag{18}
\]
Indeed, expand the difference as \((u-x_B)^*wu+x_B^*w(u-x_B)\); cyclicity and multiplication by the unitaries put both terms into the ordinary \(L^2\) pairing. This estimate is uniform in \(v,w\), even though \(g_1\) depends on \(B\).

Apply (18) with \(v=\lambda_{r_0}\), \(w=\lambda_{g_1}\). Lemma 4.1 yields
\[
|\widehat u(g_0)|^2
\le\widehat{x_B^*\lambda_{g_1}x_B}(r_0)
\le2\delta_B.
\tag{19}
\]
The coefficient is real and nonnegative by that lemma. Letting \(B\) increase proves \(\widehat u(g_0)=0\). Every coefficient outside \(H\) vanishes, so (4) gives \(u\in A\). \(\square\)

Group-theoretic malnormality alone would control normalizers that are single group unitaries. The finite-support argument is what controls all unitaries of the von Neumann algebra.

## 6. Counting the affine double cosets

**Proposition 6.1.** If \([K^\times:H]=n\), the double-coset set \(H\backslash G/H\) has \(n+1\) elements: one is \(H\), and the others are indexed by \(K^\times/H\).

**Proof.** Left and right dilation multiplication sends
\[
(a,b)\longmapsto(sa/t,sb),\qquad s,t\in H.
\tag{20}
\]
If \(b=0\), the element belongs to \(H\). If \(b\ne0\), the multiplicative coset \(bH\) is unchanged. Conversely, for \(b'=sb\) with \(s\in H\), choose \(t=sa/a'\in H\) to carry \((a,b)\) to \((a',b')\). Thus \(bH\) completely identifies the double coset. \(\square\)

The number \(n\) will become the homogeneous type I multiplicity of the left/right MASA commutant on the orthogonal complement of \(L^2(A)\). The [next lesson](double-cosets-and-intrinsic-masa-multiplicity.md) proves this and its invariance under isomorphisms of the ambient factors.

## 7. Exercises with complete solutions

**Exercise 1.** Why does (4) characterize membership in \(L(H)\) for bounded operators, rather than merely describe a subspace of \(\ell^2(G)\)?

*Solution.* The trace expectation produces a bounded element \(E_A(x)\in A\), with its vector equal to the orthogonal projection of \(x\delta_e\). If the latter is already supported on \(H\), then \((x-E_A(x))\delta_e=0\). The vector \(\delta_e\) is separating for \(M\), so \(x=E_A(x)\). The existence of a vector supported on \(H\) alone would not assert boundedness of its convolution operator; the argument starts with \(x\in M\).

**Exercise 2.** Let \(G\) be abelian and \(H\subsetneq G\). Use Theorem 2.1 to decide whether \(L(H)\) is a MASA in \(L(G)\).

*Solution.* Every subgroup conjugacy orbit is a singleton. Any \(g\notin H\) violates (5), and \(\lambda_g\) is a commuting operator outside \(L(H)\). Hence the subalgebra is not maximal abelian. This agrees with the fact that the entire ambient algebra is abelian.

**Exercise 3.** For \(K=\mathbb Q\), compute the conjugates of \((2,3)\) by translations and of \((1,3)\) by nonzero rational dilations.

*Solution.* Formula (9) gives \((2,3-c)\) for \(c\in\mathbb Q\), all distinct. Dilation conjugation gives \((1,3h)\), \(h\in\mathbb Q^\times\), also all distinct. These verify the two ICC cases separately.

**Exercise 4.** Derive the malnormality statement (8) directly from the affine multiplication law.

*Solution.* For \(g=(a,b)\), \(b\ne0\), and \(h=(s,0)\), \(k=(t,0)\), we obtain \(hgk^{-1}=(sa/t,sb)\). Equality forces \((s-1)b=0\), so \(s=1\). The first coordinate then gives \(a/t=a\), hence \(t=1\). This uses only the field property and the fact that \(a,b\ne0\).

**Exercise 5.** Explain why omitting conjugation from the involution in (10) destroys the squared-coefficient estimate, even for a support with one element.

*Solution.* Take \(x=i\delta_{g_0}\). The correct involution produces \((-i)i=1\) in the coefficient at \(g_0^{-1}g_1g_0\). Without conjugation, the product would be \(i^2=-1\), which cannot bound \(|x(g_0)|^2=1\) from above as in (12). The printed source uses the conjugated involution.

**Exercise 6.** In the rational affine group, let \(B=\{(1,1),(1,2),(2,0)\}\). Find the forbidden dilation parameters coming from distinct-pair collisions in (15), and choose an admissible parameter with \(t\ne1\).

*Solution.* Only the two elements with first coordinate \(1\) can collide. Their ordered pairs exclude \(t=1/2\) and \(t=2\). The element with first coordinate \(2\) has no distinct partner with that first coordinate. Thus \(t=3\) avoids those values and \(1\). For any \(g_0\notin H\), (16) then lies outside \(H\).

Here the stated parameter \(3\) is available in the full rational affine group, \(H=\mathbb Q^\times\). For an arbitrary dilation subgroup containing this support, its element \((2,0)\) forces \(2\in H\), hence \(4\in H\). The parameter \(t=4\) then avoids the same three forbidden values and supplies an admissible choice even when \(3\notin H\).

**Exercise 7.** Check the first bound in (18) for the term \(\tau(v^*x_B^*w(u-x_B))\).

*Solution.* Write the term as \(\tau((x_Bv)^*w(u-x_B))\). Cauchy–Schwarz bounds it by \(\|x_Bv\|_2\|w(u-x_B)\|_2=\|x_B\|_2\delta_B\). For the other term, cyclicity gives \(\tau((u-x_B)^*wu v^*)\), bounded by \(\delta_B\|u\|_2\). Both equalities use unitary invariance of the trace norm.

**Exercise 8.** Why is it legitimate for the element \(g_1\) in the singularity proof to change with every Fourier truncation?

*Solution.* The normalizer condition makes the relevant coefficient of \(u^*\lambda_{g_1}u\) zero for every choice in \(H\). The collision lemma gives nonnegativity for each finite support separately, and (18) is uniform over both group unitaries. Thus the fixed number \(|\widehat u(g_0)|^2\) is bounded by \(2\delta_B\to0\), regardless of which admissible \(g_1\) is chosen.

**Exercise 9.** For the full affine group over a countably infinite field, compute the double-coset count and the normalizer algebra of its dilation MASA.

*Solution.* Here \(H=K^\times\) has index \(1\), so Proposition 6.1 gives exactly two double cosets, \(H\) and the set of elements with nonzero translation coordinate. Theorem 5.1 says every unitary normalizer lies in \(A\). Conversely every unitary of the abelian algebra \(A\) normalizes it, and those unitaries generate \(A\). Hence the normalizer algebra is \(A\), not a factor.

**Exercise 10.** Suppose \(H\subset K^\times\) has finite index in an infinite field. Prove that \(H\) is infinite, and identify which parts of the arguments require finite index.

*Solution.* If \(H\) were finite, its finitely many cosets would make \(K^\times\) finite, contrary to infinitude of \(K\). ICC, malnormality, the MASA criterion and singularity use only that \(H\) is infinite. Finite index enters solely to make the double-coset count a prescribed finite number \(n+1\). The same proof works with an infinite double-coset count when the index is infinite.

## References

Lajos Pukánszky, [*On Maximal Abelian Subrings of Factors of Type II₁*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9B7B38999C7306E6047079CB68C937B6/S0008414X00009949a.pdf/on-maximal-abelian-subrings-of-factors-of-type-ii.pdf), *Canadian Journal of Mathematics* 12 (1960), 289–296. Lemma 3, p. 293, uses the affine conjugation and finite excluded-parameter mechanism; Lemmas 4–5, pp. 293–296, connect regular product representations and multiplicative index to double cosets.

Allan M. Sinclair and Roger R. Smith, [*The Pukánszky invariant for masas in group von Neumann factors*](https://people.tamu.edu/~rrsmith/papers/pukanszky.pdf), author-hosted manuscript of the 2005 *Illinois Journal of Mathematics* article, 49, 325–343. Example 5.1, manuscript pp. 15–17, gives the rational affine construction, trivial off-subgroup stabilizers and double-coset count. Its singularity route invokes a stronger externally cited criterion; Sections 4–5 above supply a complete direct proof of ordinary singularity at the stated general field hypotheses.

Sorin Popa, [*Orthogonal pairs of subalgebras in finite factors*](https://imar.ro/~increst/1981/89_1981.pdf), INCREST preprint 89/1981, October 1981. Lemma 1.3 and the opening of §2, printed pp. 2–3 (PDF pp. 6–7), prove normalizer confinement using orthogonality for malnormal subgroups. Theorem 2.1, printed pp. 3–4, is a subfactor construction that uses the rational full affine group as an auxiliary group.

Claire Anantharaman and Sorin Popa, [*An introduction to II1 factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author-hosted draft. §1.3.1, printed pp. 6–9 (PDF pp. 12–15), develops the group trace, convolution adjoint, regular commutation and ICC criterion; Theorem 9.1.2 and Remark 9.1.3, printed p. 140 (PDF p. 146), prove the trace expectation and its orthogonal-projection interpretation. The subgroup-orbit criterion and the extension to arbitrary infinite dilation subgroups are proved above in full.
