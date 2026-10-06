# Hensel's lemma, squares and roots of unity in p-adic fields

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

An approximate solution of a polynomial equation need not have a nearby exact solution. The derivative measures whether the error can be removed. In a complete nonarchimedean field, a sufficiently small error can be corrected repeatedly, with the new error bounded by the square of the old one. This gives a useful test for roots, and a parallel argument lifts polynomial factorizations.

We first prove the root test and use it to decide squares. We then prove factorization lifting in a form that allows nondiscrete valuations and a drop in the degree after reduction. Finally we separate the finite roots of unity from the principal units. These two elementary invariants will even distinguish the fields \(\mathbb Q_p\) as abstract fields.

The prerequisite is *Completions, the p-adic numbers and complete discretely valued fields*: completeness, the valuation ring, reduction, and p-adic congruences are used throughout. Our field \(K\) is complete for a nonarchimedean absolute value. Write

\[
\mathcal O=\{x:|x|\le1\},\qquad
\mathfrak m=\{x:|x|<1\},\qquad
\kappa=\mathcal O/\mathfrak m.
\]

A bar denotes reduction to \(\kappa\). No discrete valuation or uniformizer is assumed in the lifting theorems. For \(\mathbb Q_p\), we use \(v_p(p)=1\) and \(|x|_p=p^{-v_p(x)}\). References for the lifting theory are [Milne] and [Fesenko–Vostokov]; the general local-ring definition is discussed in [Stacks, Tag 04GE].

## 1. A root from a shrinking error

For \(f\in\mathcal O[X]\) and \(x,h\in\mathcal O\), expansion of each monomial gives

\[
f(x+h)=f(x)+f'(x)h+h^2 A(x,h),
\qquad A(x,h)\in\mathcal O,
\tag{1}
\]

and \(|f'(x+h)-f'(x)|\le |h|\). The integer coefficients in these expansions have absolute value at most one. Thus these estimates work in every characteristic.

**Theorem 1.1 (Newton lifting).** Let \(f\in\mathcal O[X]\) and \(a\in\mathcal O\). Suppose

\[
|f(a)|<|f'(a)|^2.
\]

Then there is exactly one root \(b\in K\) with \(|b-a|<|f'(a)|\). It belongs to \(\mathcal O\), and

\[
|b-a|\le \left|\frac{f(a)}{f'(a)}\right|.
\tag{2}
\]

If \(f(a)\ne0\), equality holds in (2).

**Proof.** Put \(D=|f'(a)|\). The strict hypothesis implies \(D>0\), and integrality gives \(D\le1\). If \(f(a)=0\), take \(b=a\); the uniqueness argument below still applies. Otherwise put \(q=|f(a)|/D^2\), so \(0<q<1\), and define

\[
a_0=a,\qquad a_{n+1}=a_n-\frac{f(a_n)}{f'(a_n)}.
\]

We prove inductively that

\[
a_n\in\mathcal O,\qquad |f'(a_n)|=D,\qquad
|f(a_n)|\le D^2 q^{2^n}.
\tag{3}
\]

At the initial step these assertions hold by definition. If they hold at \(n\), the increment \(h_n=a_{n+1}-a_n\) has size at most \(Dq^{2^n}<D\le1\). Hence \(a_{n+1}\) is integral. The derivative changes by less than \(D\), so the ultrametric strict-dominance rule keeps its absolute value equal to \(D\). In (1), the constant and linear terms cancel. Therefore

\[
|f(a_{n+1})|\le |h_n|^2\le D^2q^{2^{n+1}},
\]

which proves (3). If an iterate is already a root, the later iterates are constant.

The increments tend to zero. The ultrametric inequality bounds every tail difference by its largest increment, so \((a_n)\) is Cauchy. Its limit \(b\) is integral and satisfies \(f(b)=0\), by continuity of polynomial evaluation. Moreover

\[
|b-a|\le Dq=|f(a)/f'(a)|<D.
\]

When \(f(a)\ne0\), the first increment has size exactly \(Dq\), and the sum of all later increments has size at most \(Dq^2<Dq\). This proves equality in (2).

For uniqueness, any point within distance \(D\) of \(a\) is integral and has derivative of size \(D\). If \(c\) is another root in this ball, then \(|c-b|<D\). Expanding at \(b\), if \(c\ne b\) the linear term \(f'(b)(c-b)\) has size \(D|c-b|\), strictly larger than the bound \(|c-b|^2\) on the remaining terms. Their sum cannot vanish. Thus \(c=b\). ∎

The radius in the uniqueness assertion matters. A larger ball may contain more than one root. For example, for

\[
f(X)=(X-2)(X-6),\qquad a=10\quad\text{in }\mathbb Q_2,
\]

we have \(|f(a)|_2=1/32\) and \(|f'(a)|_2=1/4\). The root \(2\) has distance \(1/8\) from \(10\), while \(6\) has distance \(1/4\). Only the first lies in the strict Newton ball. Both lie in the larger ball of radius \(|f(a)/f'(a)^2|_2=1/2\).

**Corollary 1.2 (simple residue roots).** If \(\bar a\in\kappa\) is a root of \(\bar f\) and \(\bar f'(\bar a)\ne0\), it has a unique lift \(b\in\mathcal O\) satisfying \(f(b)=0\) and \(\bar b=\bar a\).

**Proof.** Any representative \(a\in\mathcal O\) satisfies \(|f(a)|<1\) and \(|f'(a)|=1\). Apply Theorem 1.1. The condition \(|b-a|<1\) is precisely equality of residues. ∎

**A cube root.** For \(f(X)=X^3-2\) over \(\mathbb Q_5\), the residue \(3\) is a root, since \(27-2=25\). Its derivative is \(3\cdot3^2=27\), a unit modulo five. The lift is unique among elements congruent to \(3\) modulo five. Its first Newton iterate is \(56/27\), and its distance from \(3\) is \(1/25\). The error at this iterate has valuation at least four, by (3).

## 2. Squares and their obstructions

Every \(x\in\mathbb Q_p^\times\) is uniquely \(p^r u\), with \(r\in\mathbb Z\) and \(u\in\mathbb Z_p^\times\). A necessary condition for a square is that \(r\) be even. Once this holds, the question reduces to the unit \(u\).

**Proposition 2.1 (square test).** For odd \(p\), a unit \(u\in\mathbb Z_p^\times\) is a square exactly when its residue is a square in \(\mathbb F_p^\times\). A unit of \(\mathbb Z_2\) is a square exactly when it is congruent to \(1\) modulo \(8\).

Consequently, for a nonsquare unit \(u_0\) at odd \(p\), the four elements

\[
1,\ u_0,\ p,\ pu_0
\]

represent all square classes in \(\mathbb Q_p^\times\). At \(p=2\), the eight representatives are

\[
1,-1,5,-5,2,-2,10,-10.
\tag{4}
\]

**Proof.** At odd \(p\), a unit square reduces to a nonzero square. Conversely, if \(a^2\equiv u\pmod p\), then \(a\) is a unit and the derivative of \(X^2-u\) at \(a\) is \(2a\), also a unit. Corollary 1.2 supplies a square root.

The square map on the finite group \(\mathbb F_p^\times\) has kernel \(\{1,-1\}\), hence image of index two. Its image and its other coset distinguish the two unit square classes. The parity of the valuation distinguishes two more possibilities, giving exactly four classes.

For \(p=2\), the square of each odd residue modulo eight is one. This proves necessity for units. If \(u\equiv1\pmod8\), apply Theorem 1.1 to \(f(X)=X^2-u\) at \(a=1\):

\[
|f(1)|_2\le1/8<1/4=|f'(1)|_2^2.
\]

Thus \(u\) has a square root in \(\mathbb Z_2\). Two units have the same square class exactly when their quotient is one modulo eight, equivalently when their residues modulo eight agree. The unit representatives \(1,-1,5,-5\) have the four different residues \(1,7,5,3\). Adding valuation parity gives (4), with all eight classes distinct. ∎

This classifies nonzero elements. Zero is of course a square, but does not belong to the multiplicative square-class group.

**Four roots to test.** In \(\mathbb Q_5\), \(X^2+1\) has the simple residue root \(2\), so \(-1\) is a square. Its first Newton iterate is \(3/4\), and the root congruent to two modulo five has distance \(1/5\) from two. The residue two is not a square modulo five, so \(\sqrt2\notin\mathbb Q_5\). In \(\mathbb Q_3\), seven reduces to one and therefore is a square. Finally, for \(X^2-17\) at \(a=1\) in \(\mathbb Q_2\),

\[
|f(1)|_2=1/16<1/4=|f'(1)|_2^2.
\]

Newton lifting applies even though the derivative is not a unit. The first iterate is nine; the nearby root has distance \(1/8\) from one. The other root is its negative and does not lie in that same Newton ball.

## 3. Correcting a factorization

For a polynomial \(P=\sum a_iX^i\), write \(\|P\|=\max_i|a_i|\), with \(\|0\|=0\). Coefficientwise addition satisfies the ultrametric inequality and \(\|PQ\|\le\|P\|\|Q\|\). Thus a polynomial is integral exactly when its coefficient norm is at most one.

**Lemma 3.1 (bounded linear correction).** Let \(g\in\mathcal O[X]\) be monic of degree \(r\), and let \(h\in\mathcal O[X]\) have degree at most \(s\). Assume \(\bar g\) and \(\bar h\) are coprime. For every polynomial \(E\) of degree at most \(r+s\) there is a unique pair

\[
\deg u<r,\qquad \deg v\le s,\qquad uh+vg=E.
\tag{5}
\]

Moreover \(\max(\|u\|,\|v\|)\le\|E\|\).

**Proof.** Division by the monic polynomial \(g\) identifies \(\mathcal O[X]/(g)\) with the free module with basis \(1,X,\ldots,X^{r-1}\). Multiplication by \(h\) is represented by a matrix with entries in \(\mathcal O\). On reduction it is invertible: coprimality gives a Bézout identity in \(\kappa[X]\). Its determinant is therefore a unit of \(\mathcal O\), and its inverse, computed by the adjugate, also has integral entries.

Take \(u\) to be the unique representative of degree less than \(r\) of the inverse image of \(E\) modulo \(g\), and set \(v=(E-uh)/g\). These operations are \(K\)-linear. Monic division never increases the coefficient norm when \(\|g\|\le1\); the inverse matrix likewise has operator norm at most one for the maximum norm. Therefore \(\|u\|,\|v\|\le\|E\|\). The degree bound on \(v\) follows from division of a polynomial of degree at most \(r+s\). Uniqueness follows first modulo \(g\), and then in (5). If \(r=0\), then \(g=1\), \(u=0\), and the assertion follows directly. ∎

**Theorem 3.2 (factorization lifting).** Suppose \(f\in\mathcal O[X]\) has nonzero reduction and

\[
\bar f=\bar g\bar h,\qquad (\bar g,\bar h)=1.
\]

If \(\bar g\) is monic, there is a unique factorization \(f=gh\) with \(g\) monic, \(\deg g=\deg\bar g\), and prescribed reductions \(\bar g,\bar h\). The factors are strictly coprime: \((g,h)=\mathcal O[X]\).

For an arbitrary nonzero \(\bar g\), a factorization with the prescribed reductions and \(\deg g=\deg\bar g\) still exists. It becomes unique once the leading coefficient of \(g\) is fixed to a chosen lift of the leading coefficient of \(\bar g\).

**Proof.** First suppose \(\bar g\) monic. Put \(n=\deg f\), \(r=\deg\bar g\), \(s=n-r\). Choose a monic lift \(g_0\) of degree \(r\), and a lift \(h_0\) of degree at most \(s\). Then \(E_0=f-g_0h_0\) has coefficient norm \(\rho<1\), because each of its finitely many coefficients reduces to zero. If \(E_0=0\), this is already a factorization.

Otherwise use Lemma 3.1 successively to solve

\[
u_jh_j+v_jg_j=E_j,\qquad
g_{j+1}=g_j+u_j,\quad h_{j+1}=h_j+v_j.
\]

The new error is \(E_{j+1}=-u_jv_j\). Hence

\[
\|E_j\|\le\rho^{2^j},\qquad
\|u_j\|,\|v_j\|\le\rho^{2^j}.
\tag{6}
\]

All corrections reduce to zero. Thus the reductions remain coprime, \(g_j\) stays monic of degree \(r\), and \(\deg h_j\le s\). Completeness applied to each coefficient gives polynomials \(g,h\) with the required degrees and reductions. Formula (6) makes the error tend to zero, so \(f=gh\). There was no need for a smallest positive value of the valuation.

For uniqueness, suppose another pair \(g',h'\) has these properties. Set \(u=g'-g\), \(v=h'-h\). The degree restrictions of Lemma 3.1 apply, and \(t=\max(\|u\|,\|v\|)<1\). Subtracting the factorizations gives

\[
uh+vg=-uv.
\]

The bounded inverse in Lemma 3.1 yields \(t\le\|uv\|\le t^2\). This forces \(t=0\), proving equality of both pairs. Applying the lemma to \(E=1\) also produces \(uh+vg=1\), which proves strict coprimality.

In general, let \(c\in\mathcal O^\times\) lift the leading coefficient of \(\bar g\). Replace the residue factors by \(\bar c^{-1}\bar g\) and \(\bar c\bar h\). The first is monic. Lift them by the first part, obtaining \(G,H\), and put \(g=cG\), \(h=c^{-1}H\). These have the original reductions. The same normalization proves the final uniqueness assertion. ∎

In the usual monic form, \(f\), \(g\) and \(h\) are all monic and their degrees equal their residue degrees. The more general form is useful when the leading coefficient of \(f\) lies in \(\mathfrak m\). For example, over \(\mathbb Q_5\), the polynomial

\[
5X^2+X+1
\]

reduces to \(X+1\). Its simple root modulo five lifts to an integral root, producing a monic linear factor; the remaining linear factor has leading coefficient five and constant nonzero reduction. Dropping the degree condition on the monic factor would hide this distinction.

Coprimality cannot be removed. The reduction of \(X^2-p\) is \(X\cdot X\), yet \(X^2-p\) has no root in \(\mathbb Q_p\): a root would have valuation \(1/2\), whereas the value group of \(\mathbb Q_p^\times\) is \(\mathbb Z\).

## 4. Residues lift multiplicatively

Assume now \(\kappa=\mathbb F_q\), where \(q=p^f\). The polynomial \(X^{q-1}-1\) has every nonzero residue as a simple root: its derivative is \((q-1)X^{q-2}\), a unit at those roots.

**Proposition 4.1 (Teichmüller representatives).** Reduction induces an isomorphism

\[
\mu_{q-1}(K)\xrightarrow{\sim}\mathbb F_q^\times,
\]

where \(\mu_m(K)=\{z\in K:z^m=1\}\). Its inverse \(a\mapsto[a]\) is multiplicative. With \([0]=0\), the elements \([a]\) give representatives of all residue classes. In particular a finite extension of \(\mathbb Q_p\), with its complete extended absolute value and residue field \(\mathbb F_q\), contains all \((q-1)\)-st roots of unity.

**Proof.** Corollary 1.2 provides exactly one root over each nonzero residue. Every root of unity has absolute value one, hence lies in \(\mathcal O^\times\). The polynomial has degree \(q-1\); the \(q-1\) lifted roots exhaust its roots. The product \([a][b]\) is another \((q-1)\)-st root of unity and reduces to \(ab\), so uniqueness gives \([a][b]=[ab]\). ∎

The completeness and uniqueness of the extended value on finite extensions will be proved in *Extensions of complete valued fields*. The proposition itself proves the stronger conditional statement for every complete field with this residue field, and does not use any extension theorem. The representatives are usually not additive: for example in \(\mathbb Q_3\), \([1]+[1]=2\), while \([2]=-1\).

To determine all roots of unity of \(\mathbb Q_p\), we must also control units that reduce to one.

**Lemma 4.2 (valuation of a power).** If \(z\ne0\) and \(r=v_p(z)\ge1\) for odd \(p\), or \(r\ge2\) for \(p=2\), then for every positive integer \(m\),

\[
v_p((1+z)^m-1)=r+v_p(m).
\tag{7}
\]

**Proof.** If \(p\nmid m\), the linear term \(mz\) has valuation \(r\); all higher terms in the binomial expansion have valuation at least \(2r>r\). Thus the valuation is \(r\). For the exponent \(p\), the term \(pz\) has valuation \(r+1\). At odd \(p\), the intermediate binomial coefficients are divisible by \(p\), giving valuations at least \(1+2r>r+1\); the last term has valuation \(pr>r+1\). At two the other term is \(z^2\), of valuation \(2r>r+1\). Thus taking a \(p\)-th power increases the valuation exactly by one. Apply this repeatedly to the \(p\)-power part of \(m\), and apply the first observation to its prime-to-\(p\) part. ∎

**Proposition 4.3 (torsion in \(\mathbb Q_p^\times\)).** For odd \(p\), the group \(1+p\mathbb Z_p\) has no nonidentity element of finite order, and

\[
\mu(\mathbb Q_p)=\mu_{p-1}(\mathbb Q_p).
\]

For \(p=2\), the group \(1+4\mathbb Z_2\) is torsion-free and \(\mu(\mathbb Q_2)=\{1,-1\}\).

**Proof.** Formula (7) is finite for every positive \(m\), so \((1+z)^m\ne1\) whenever \(z\ne0\) has the stated valuation. For odd \(p\), divide a root of unity \(\xi\) by the Teichmüller lift of its residue. The quotient is a torsion element in \(1+p\mathbb Z_p\), hence one. For two, every unit has odd residue modulo four; its square is one modulo eight. Thus the square of any root of unity lies in the torsion-free group \(1+4\mathbb Z_2\), and is one. The solutions of \(X^2=1\) in a characteristic-zero field are exactly \(1,-1\). ∎

Notice why \(1+2\mathbb Z_2\) was excluded: it contains \(-1\). These elementary power estimates will later be replaced by the logarithm on sufficiently deep unit groups.

## 5. Henselian fields beyond completion

A valued field is called *henselian* when its valuation ring is henselian: every simple residue root of a monic integral polynomial lifts to a root in the valuation ring. The lift, when it exists, is unique. The equivalent coprime-factorization formulations are part of the general theory in [Stacks, Tag 04GE]. Corollary 1.2 proves directly that every complete nonarchimedean valued field is henselian, and Theorem 3.2 gives the factorization form as well.

Completeness is a sufficient condition, rather than the definition. Every valued field has a henselization: a henselian algebraic extension with the universal mapping property among henselian valued extensions. A henselization is unique up to the unique valued isomorphism compatible with the original field [Stacks, Tags 04GN and 0ASK]. This existence theorem, and henselization and strict henselization for general local rings, belong to *Henselian local rings and henselization*. We do not prove them here.

## 6. Exercises

1. Decide which of \(2,3,-1,7\) are squares in \(\mathbb Q_7\). Distinguish the residue obstruction from the valuation obstruction.
2. Prove that \(X^2-p\) is irreducible over \(\mathbb Q_p\), and explain why the repeated factor in its reduction does not lift.
3. Prove directly, without a logarithm, that \(1+p\mathbb Z_p\) for odd \(p\) and \(1+4\mathbb Z_2\) have no nonidentity roots of unity. Determine the valuation of \(u^m-1\) for \(u\ne1\) in these groups.
4. Prove that every element of \(1+8\mathbb Z_2\) is a square, and verify that the eight elements in (4) form a complete set of distinct square classes.
5. Show that \(\mathbb Q_p\) and \(\mathbb Q_\ell\) are not isomorphic as fields when \(p\ne\ell\). Do not assume that an abstract field isomorphism is continuous.

## 7. Solutions

**1.** The nonzero squares modulo seven are \(1,2,4\), obtained by squaring \(1,2,3\) and their negatives. Thus two is a square in \(\mathbb Q_7\), while three and minus one (residue six) are not, by Proposition 2.1. Seven has valuation one and therefore is not a square. All four decisions are now justified by a necessary and sufficient test.

**2.** If \(b^2=p\), then \(2v_p(b)=1\), contradicting the integer value group. A quadratic polynomial over a field is reducible exactly when it has a root, so the polynomial is irreducible. Its reduction is \(X^2\); the two factors \(X\) are not coprime, and the factorization theorem has no applicable hypothesis. This example proves that this hypothesis is needed, even for monic polynomials.

**3.** Write \(u=1+z\), with \(r=v_p(z)\) in the stated range. For \(p\nmid d\), the binomial expansion gives \(v_p(u^d-1)=r\) because its linear term has uniquely least valuation. The expansion for exponent \(p\) gives \(v_p(u^p-1)=r+1\): for odd \(p\) its intermediate terms have valuation at least \(1+2r\) and its last term has valuation \(pr\); for two the last term has valuation \(2r\). All are strictly greater than \(r+1\). Iterating and writing \(m=p^a d\), \(p\nmid d\), gives \(v_p(u^m-1)=r+a\). This is finite for every positive \(m\), so \(u\) cannot have finite order. The condition \(r\ge2\) at two is indispensable, since \(-1=1-2\) has order two.

**4.** For \(u\in1+8\mathbb Z_2\), evaluate \(X^2-u\) at one. Its error has valuation at least three, while its derivative has valuation one. The strict Newton inequality holds, so \(u\) is a square. Conversely an odd square is one modulo eight: if \(a=2k+1\), then \(a^2=1+4k(k+1)\), and \(k(k+1)\) is even. This identity holds modulo eight for every element of \(\mathbb Z_2\) by reduction. A nonzero element is \(2^r u\). Removing \(2^{2\lfloor r/2\rfloor}\) leaves valuation zero or one; removing a unit square leaves exactly one of the residues represented by \(1,-1,5,-5\). Their products with two give all eight representatives. Distinct valuation parities cannot differ by a square; within the same parity, distinct odd residues modulo eight cannot differ by a square. This proves completeness and distinctness.

**5.** A field isomorphism preserves the set of all roots of unity, because each equation \(X^m=1\) is preserved. Proposition 4.3 shows that this set has \(p-1\) elements for odd \(p\) and two elements for \(p=2\). Different odd primes therefore give different cardinalities. The same distinguishes two from every odd prime other than three. The remaining pair is \(\mathbb Q_2,\mathbb Q_3\). A field isomorphism also induces an isomorphism of multiplicative groups and of their quotients by squares. Proposition 2.1 gives cardinalities eight and four for these two quotients, respectively. Thus this pair is impossible too. The argument covers all distinct primes and uses no topology on an alleged isomorphism.

## What this lesson does not prove

We use the field-completion and value-group results from *Completions, the p-adic numbers and complete discretely valued fields*, and elementary polynomial division and matrix inversion over a field. The usual finite-field square count follows here from the kernel of the square map; cyclicity of finite-field multiplicative groups is not needed for that count.

The completeness and unique extended absolute value on a finite extension of \(\mathbb Q_p\) are proved in *Extensions of complete valued fields*. The Teichmüller construction above already proves the assertion for any complete field with finite residue field.

The general equivalence of henselian-local-ring criteria is cited from [Stacks, Tag 04GE]. Existence of henselization is cited from [Stacks, Tags 04GN and 0ASK]. These topics are developed in *Henselian local rings and henselization*. They are not prerequisites for any lifting proof in this lesson. We do not classify ramified extensions or their roots of unity beyond \(\mathbb Q_p\).

## References

- **[Milne]** J. S. Milne, [*Algebraic Number Theory*, version 3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 7, Newton's lemma, Propositions 7.31 and Theorems 7.32–7.33. Theorem 1.1 above specifies the smaller ball in which the root is unique.
- **[Fesenko–Vostokov]** I. B. Fesenko and S. V. Vostokov, *Local Fields and Their Extensions*, second edition, Chapter I, §4, on completion, and Chapter II, §1, on the Hensel lemma and Henselian fields. [Author-hosted edition](https://ivanfesenko.org/wp-content/uploads/2021/10/vol.pdf).
- **[Stacks]** *The Stacks project*, read in the AI Integrated Stacks Project English edition: [Tag 04GE, henselian local rings](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-henselian); [Tag 04GN, henselization](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-henselization); [Tag 0ASK, henselization of valuation rings](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-valuation-ring). This is an unofficial edition with AI-proposed corrections and supplements; those additions have not been reviewed by the Stacks project maintainers. The [official Stacks project](https://stacks.math.columbia.edu/) maintains the tagged source.
