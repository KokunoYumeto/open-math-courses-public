# Group MASAs and singular affine examples

*Written by GPT-6.1 Sol (OpenAI), Ultra. Course exposition: CC0-1.0 to the extent of rights held. Earlier programme and human-source notices retain their own terms.*

A subgroup determines a Fourier-support projection in its group von Neumann algebra. Infinite conjugacy orbits characterize maximal abelianness. For affine groups, malnormality gives finite exceptional sets, and trace-norm estimates turn that group geometry into a proof of singularity for every unitary normalizer. Double cosets and independent coefficient tests describe further features of the same examples.

The [regular-group operator foundations](regular-group-operator-foundations.md) prove the regular commutant, faithful normal trace, Fourier-support test and subgroup expectation directly. Its H03 proves separable predual for a countable group, and H04 proves that an infinite-dimensional tracial factor has type \(\mathrm{II}_1\). The group trace and expectation require no ICC hypothesis; ICC enters only in the factor conclusion.

The freely readable comparison is [Sinclair–Smith, *The Pukánszky invariant for masas in group von Neumann factors*](https://people.tamu.edu/~rrsmith/papers/pukanszky.pdf), Example 5.1, manuscript pp.15–17. Its rational affine groups satisfy a finite-set condition used there to invoke a stronger singularity criterion. The complete mixing and normalizer argument below proves ordinary singularity for every countably infinite field and every infinite dilation subgroup. For the group trace, regular commutation and trace expectation, see [Anantharaman–Popa, *An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), §1.3.1, Lemma 1.3.4 through Proposition 1.3.9, and Theorem 9.1.2 with Remark 9.1.3. Their exact local constructions are linked in the foundations paragraph above.

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

For a subgroup \(H\), write \(A=L(H)\subset M\). The subgroup compression proved in [G04](regular-group-operator-foundations.md#g04) gives the trace expectation \(E_A\). On trace vectors it is the orthogonal projection onto \(\overline{A\delta_e}=\ell^2(H)\). Consequently
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

## Singularity from malnormal mixing

A MASA \(A\subset M\) is **singular** if every unitary \(u\) satisfying \(uAu^*=A\) belongs to \(A\).

**Theorem 5.1.** The affine dilation MASA of Proposition 3.1 is singular for every infinite \(H\subset K^\times\).

**Proof.** We use the infinite abelian subgroup \(H\) and its malnormality from Proposition 3.1. The subgroup expectation \(E_A\) is the bounded normal trace expectation of (4). It deletes the Fourier coefficients outside \(H\) and is an orthogonal projection in trace \(2\)-norm.

First fix \(s,t\in G\setminus H\). There is at most one \(h\in H\) with \(sht\in H\). Indeed, if \(sh_1t\) and \(sh_2t\) both belong to \(H\), then
\[
 s h_1h_2^{-1}s^{-1}
       =(sh_1t)(sh_2t)^{-1}\in H.
\]
Thus \(h_1h_2^{-1}\in H\cap s^{-1}Hs=\{e\}\), and \(h_1=h_2\). For finite sets \(S,T\subset G\setminus H\), at most \(|S||T|\) elements of \(H\) can satisfy any of the conditions \(sht\in H\). Consequently, for Fourier polynomials \(x_0,y_0\) supported respectively in \(S,T\),
\[
 E_A(x_0\lambda_h y_0)=0
       \quad\text{outside a finite subset of }H.
\tag{GM1}
\]
This is a statement about the whole expected operator, not just one of its coefficients.

We extend it to arbitrary bounded \(x,y\in M\) with \(E_A(x)=E_A(y)=0\). Given \(\eta>0\), choose a finite Fourier polynomial \(y_0\), supported outside \(H\), with
\[
 \|y-y_0\|_2<\frac{\eta}{2(1+\|x\|)}.
\]
Such polynomials exist by (3); the coefficients on \(H\) vanish. The chosen polynomial is bounded, since its operator norm is at most the finite sum of the absolute values of its coefficients. After choosing it, choose another finite Fourier polynomial \(x_0\), also supported outside \(H\), with
\[
 \|x-x_0\|_2<\frac{\eta}{2(1+\|y_0\|)}.
\]
The order of these choices matters: no common operator-norm bound on the Fourier polynomials is needed.

The trace gives \(\|ab\|_2\le\|a\|\|b\|_2\) and \(\|ab\|_2\le\|a\|_2\|b\|\). The first follows from \(a^*a\le\|a\|^2 1\) inside \(\tau(b^*a^*ab)\); the second follows by traciality from \(bb^*\le\|b\|^2 1\). Using these estimates, unitary invariance of the \(2\)-norm and contractivity of \(E_A\) in that norm gives, for every \(h\in H\),
\[
\begin{aligned}
 \|E_A(x\lambda_h y-x_0\lambda_h y_0)\|_2
 &\le \|x\|\|y-y_0\|_2
          +\|x-x_0\|_2\|y_0\|\\
 &<\eta.
\end{aligned}
\tag{GM2}
\]
Combining (GM1) and (GM2) proves
\[
 \|E_A(x\lambda_h y)\|_2\longrightarrow0
       \qquad(h\in H,\ h\longrightarrow\infty),
\tag{GM3}
\]
where the limit means that every positive error bound holds outside a finite subset of \(H\). Infinitude of \(H\) ensures that those complements are nonempty.

Now let \(u\in M\) be a unitary with \(uAu^*=A\). Put
\[
 b=E_A(u),\qquad a=u-b.
\]
Then \(E_A(a)=0\), \(E_A(a^*)=0\), and \(\|b\|\le1\). For \(h\in H\), the normalizer identity puts \(u\lambda_hu^*\) in \(A\). Expanding \(u=b+a\), bimodularity kills the two mixed terms:
\[
\begin{aligned}
 u\lambda_hu^*
 &=E_A(u\lambda_hu^*)\\
 &=b\lambda_hb^*+E_A(a\lambda_h a^*)\\
 &=|b|^2\lambda_h+E_A(a\lambda_h a^*).
\end{aligned}
\tag{GM4}
\]
The last equality uses the abelianness of \(A\). Equation (GM3) makes the last term tend to zero in \(2\)-norm. The left side is unitary and has \(2\)-norm one, whereas
\[
 \||b|^2\lambda_h\|_2
       =\|b^*b\|_2
       \le\|b\|\|b\|_2
       \le\|b\|_2.
\]
It follows that \(1\le\|b\|_2\). Orthogonal projection contractivity gives the reverse inequality. The Pythagorean identity now yields
\[
 \|u-b\|_2^2=\|u\|_2^2-\|b\|_2^2=0.
\]
Faithfulness of the trace gives \(u=b\in A\), proving singularity. \(\square\)

The argument controls every unitary of \(L(G)\) that normalizes \(A\). The group calculation supplies the finite exceptional sets; the two successive Fourier approximations supply the bounded-operator limit. No classification, amenability, hyperfiniteness or stronger singularity criterion is used.

## Double cosets of the affine action

**Proposition 6.1.** If \([K^\times:H]=n\), the double-coset set \(H\backslash G/H\) has \(n+1\) elements: one is \(H\), and the others are indexed by \(K^\times/H\).

**Proof.** Left and right dilation multiplication sends
\[
(a,b)\longmapsto(sa/t,sb),\qquad s,t\in H.
\tag{20}
\]
If \(b=0\), the element belongs to \(H\). If \(b\ne0\), the multiplicative coset \(bH\) is unchanged. Conversely, for \(b'=sb\) with \(s\in H\), choose \(t=sa/a'\in H\) to carry \((a,b)\) to \((a',b')\). Thus \(bH\) completely identifies the double coset. \(\square\)

The number \(n\) will become the homogeneous type I multiplicity of the left/right MASA commutant on the orthogonal complement of \(L^2(A)\). The [next lesson](double-cosets-and-intrinsic-masa-multiplicity.md) proves this and its invariance under isomorphisms of the ambient factors.

## Independent finite-support coefficient tests

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

**Exercise 8.** Fix a unitary normalizer \(u\) and \(g_0\notin H\). For each finite Fourier truncation \(x_B\) from (17), choose \(g_1\) by Lemma 4.2 for \(Bg_0^{-1}\). Prove that these choices may vary with \(B\), while their coefficient estimates still force \(\widehat u(g_0)=0\).

*Solution.* Put \(r_0=g_0^{-1}g_1g_0\notin H\). The inverse normalizer relation gives \(u^*\lambda_{g_1}u\in A\), so its \(r_0\)-coefficient is zero. Lemma 4.1 and the uniform estimate (18), with \(v=\lambda_{r_0}\) and \(w=\lambda_{g_1}\), give
\[
 |\widehat u(g_0)|^2
 \le\widehat{x_B^*\lambda_{g_1}x_B}(r_0)
 \le 2\|u-x_B\|_2.
\tag{19}
\]
The middle coefficient is real and nonnegative. The first inequality retains the fixed \(g_0\)-coefficient because \(g_0\in B\); the second is uniform in both group unitaries, even when they change with the truncation. Fourier square summability makes the final bound tend to zero. This proves the claimed vanishing without choosing one parameter that works for every support.

**Exercise 9.** For the full affine group over a countably infinite field, compute the double-coset count and the normalizer algebra of its dilation MASA.

*Solution.* Here \(H=K^\times\) has index \(1\), so Proposition 6.1 gives exactly two double cosets, \(H\) and the set of elements with nonzero translation coordinate. Theorem 5.1 says every unitary normalizer lies in \(A\). Conversely every unitary of the abelian algebra \(A\) normalizes it, and those unitaries generate \(A\). Hence the normalizer algebra is \(A\), not a factor.

**Exercise 10.** Suppose \(H\subset K^\times\) has finite index in an infinite field. Prove that \(H\) is infinite, and identify which parts of the arguments require finite index.

*Solution.* If \(H\) were finite, its finitely many cosets would make \(K^\times\) finite, contrary to infinitude of \(K\). ICC, malnormality, the MASA criterion and singularity use only that \(H\) is infinite. Finite index enters solely to make the double-coset count a prescribed finite number \(n+1\). The same proof works with an infinite double-coset count when the index is infinite.

## References

Lajos Pukánszky, [*On Maximal Abelian Subrings of Factors of Type II₁*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9B7B38999C7306E6047079CB68C937B6/S0008414X00009949a.pdf/on-maximal-abelian-subrings-of-factors-of-type-ii.pdf), *Canadian Journal of Mathematics* 12 (1960), 289–296. Lemma 3, p. 293, uses the affine conjugation and finite excluded-parameter mechanism; Lemmas 4–5, pp. 293–296, connect regular product representations and multiplicative index to double cosets.

Allan M. Sinclair and Roger R. Smith, [*The Pukánszky invariant for masas in group von Neumann factors*](https://people.tamu.edu/~rrsmith/papers/pukanszky.pdf), author-hosted manuscript of the 2005 *Illinois Journal of Mathematics* article, 49, 325–343. Example 5.1, manuscript pp. 15–17, gives the rational affine construction, trivial off-subgroup stabilizers and double-coset count. Its singularity route invokes a stronger externally cited criterion. The malnormal-mixing proof above writes out finite exceptional sets, two successive bounded Fourier approximations and the subgroup-expectation normalizer calculation, proving ordinary singularity at the stated general field hypotheses.

Sorin Popa, [*Orthogonal pairs of subalgebras in finite factors*](https://imar.ro/~increst/1981/89_1981.pdf), INCREST preprint 89/1981, October 1981. Lemma 1.3 and the opening of §2, printed pp. 2–3 (PDF pp. 6–7), prove normalizer confinement using orthogonality for malnormal subgroups. Theorem 2.1, printed pp. 3–4, is a subfactor construction that uses the rational full affine group as an auxiliary group.

Claire Anantharaman and Sorin Popa, [*An introduction to II1 factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author-hosted draft. §1.3.1, printed pp. 6–9 (PDF pp. 12–15), develops the group trace, convolution adjoint, regular commutation and ICC criterion; Theorem 9.1.2 and Remark 9.1.3, printed p. 140 (PDF p. 146), prove the trace expectation and its orthogonal-projection interpretation. The subgroup-orbit criterion and the extension to arbitrary infinite dilation subgroups are proved above in full.

## Bounded subgroup operators and normalizers

The subgroup algebra in (4) is the actual algebra on \(\ell^2(G)\), not just a copy of its Hilbert space. [G03](regular-group-operator-foundations.md#g03) identifies it through the right-coset amplification
\[
\iota_H(b)=\bigoplus_{Ht}U_t bU_t^*,
\qquad U_t\delta_h=\delta_{ht}.
\]
Every block has norm \(\|b\|\), and restricting to the identity coset gives the reverse norm inequality. Thus this amplification is an isometric unital star homomorphism. The full block-commutant calculation in G03 identifies its range with \(\lambda_G(H)''\). In [G04](regular-group-operator-foundations.md#g04), compression of \(x\in L(G)\) to \(\ell^2(H)\) commutes with the right regular representation of \(H\); [G00](regular-group-operator-foundations.md#g00) puts that compression in \(L(H)\). Amplifying it gives the bounded operator \(E_A(x)\), with \(E_A(x)\delta_e=P_Hx\delta_e\). Compression and amplification preserve positivity at every matrix level. Their series-vector pullbacks prove ultraweak continuity, and the identity vector proves trace preservation and faithfulness. These complete arguments establish the expectation used in (4) without the general positive-cone theorem for arbitrary finite subalgebras.

For an abelian subgroup, \(A\) really is abelian under the double-commutant definition. Put \(S=\lambda(H)\). Commutativity gives \(S\subset S'\), hence \(S''\subset S'\). If \(x,y\in S''\), then \(x\in S'\) and \(y\) commutes with every element of \(S'\). Therefore \(xy=yx\). Also an operator commuting with \(S\) commutes with all of \(S''\): it belongs to \(S'\), whose elements commute with \(S''\) by definition. This justifies both directions of the orbit argument without assuming an operator-norm Fourier approximation. [G01](regular-group-operator-foundations.md#g01) supplies the trace for all bounded operators, [G02](regular-group-operator-foundations.md#g02) supplies the square-summable coefficients, and [H03](regular-group-operator-foundations.md#h03) and [H04](regular-group-operator-foundations.md#h04) supply respectively the separable predual and the infinite-dimensional finite-factor classification used in Proposition 3.1.

The finite exclusions in Lemma 4.2 work in every characteristic. For an ordered distinct pair \((a,b),(a',b')\), different first coordinates give no collision. With equal first coordinates, \(b'=0\) permits a collision only if \(b=0\), which would make the pair equal; if \(b'\ne0\), the only possible parameter is \(t=b/b'\). There are at most \(|B|(|B|-1)\) parameters from distinct ordered pairs. Removing those and \(1\) from the infinite set \(H\) leaves an admissible parameter. The same argument applies to the finite translated set \(Bg_0^{-1}\). It uses no ordering of the field, no assumption of characteristic zero and no finite-index hypothesis.

<a id="uniform-fourier-coefficient-control"></a>

The independent coefficient tests use the following uniform trace estimate. For a unitary \(u\), choose finite sets \(B\) exhausting \(G\), and put
\[
 x_B=\sum_{s\in B}\widehat u(s)\lambda_s,\qquad
 \delta_B=\|u-x_B\|_2\longrightarrow0,\qquad
 \|x_B\|_2\le1.
\tag{17}
\]
Each \(x_B\) is bounded because \(\|x_B\|\le\sum_{s\in B}|\widehat u(s)|<\infty\). No common bound on these operator norms is used. For arbitrary group unitaries \(v,w\),
\[
 \left|\tau\bigl(v^*(u^*wu-x_B^*wx_B)\bigr)\right|
 \le\delta_B(\|u\|_2+\|x_B\|_2)
 \le2\delta_B.
\tag{18}
\]
To prove it, expand the difference as \((u-x_B)^*wu+x_B^*w(u-x_B)\). Cyclicity turns the first trace term into the Hilbert pairing of \(u-x_B\) with \(wuv^*\), whose \(2\)-norm is \(\|u\|_2\). The second trace term is exactly
\[
 \tau\bigl((x_Bv)^*w(u-x_B)\bigr),
\]
whose absolute value is at most \(\|x_B\|_2\delta_B\). Trace Cauchy–Schwarz and unitary invariance give both estimates independently of \(v,w\). The inverse normalizer relation used in Exercise 8 follows by multiplying \(uAu^*=A\) by \(u^*\) and \(u\), giving \(u^*Au=A\). Thus this coefficient argument has all its bounded-operator and norm inputs even when the selected group elements vary.

Finally the unitaries of \(A\) generate \(A\). If \(h=h^*\in A\) is a contraction, continuous functional calculus gives \(v=h+i(1-h^2)^{1/2}\in A\). Its two factors commute, so \(vv^*=v^*v=1\), and \(h=(v+v^*)/2\). Scaling and taking real and imaginary parts expresses every element as a linear combination of unitaries. Theorem 5.1 therefore makes the entire normalizer algebra equal to \(A\), as used in Exercise 9. The double-coset calculation has no hidden finiteness requirement: \((a,b)\), with \(a\in H\), is carried to \((1,b)\) by taking \(s=1,t=a\) in (20). Nonzero representatives are consequently classified exactly by \(bH\), for finite or infinite multiplicative index.
