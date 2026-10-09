# Formal groups and Lubin–Tate modules

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

The multiplicative expression \(X+Y+XY\) becomes a group law near zero because \(1+(X+Y+XY)=(1+X)(1+Y)\). A formal group retains such a law as a power series, before choosing the elements on which it will be evaluated. Lubin–Tate theory builds one whose multiplication by a uniformizer reduces to Frobenius. Its division points will furnish explicit abelian extensions in the next lesson.

Two congruences drive the construction. The linear coefficient is a uniformizer \(\pi\), while reduction of the entire series is \(X^q\). One controls the coefficient to be solved; the other makes the obstruction divisible by \(\pi\). We prove that coefficient calculation, derive the group and its scalar action, and then compare different uniformizers using Frobenius on the completed unramified tower.

We use [Completions, the p-adic numbers and complete discretely valued fields](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-LOC-02), Theorem 2.1 and Proposition 2.2, for completion, extension of isometries and integer approximation in \(\mathbf Z_p\); [Extensions of complete valued fields](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-LOC-04), Theorem 1.2, for completeness of finite extensions and their uniquely extended valuation; and [Unramified and totally ramified extensions](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-LOC-07), Theorem 2.1 and Corollary 3.1, for the unramified tower and its arithmetic Frobenius. The construction is algebraic in its power-series variables; convergence will enter only when we evaluate them or complete a coefficient ring.


**Prerequisite proof availability.** The named results below identify specific programme lessons. The [prerequisite record](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#lesson-7) shows which results are proved in published lessons and which full proofs are still missing. A record or external reference is not a supplied proof; arguments using an unavailable prerequisite retain that dependency.

## 1. Formal laws and their inverses

Let \(R\) be a commutative ring with 1. A **one-dimensional commutative formal group law** is \(F(X,Y)\in R[[X,Y]]\) with

\[
\begin{gathered}
F(X,Y)=X+Y+\text{terms of total degree at least 2},\\
F(X,0)=X,\quad F(0,Y)=Y,\quad F(X,Y)=F(Y,X),\\
F(F(X,Y),Z)=F(X,F(Y,Z)).
\end{gathered}
\tag{1}
\]

Substitution of series with zero constant term is well defined: a coefficient of a given total degree involves only finitely many terms. No analytic convergence is needed for these identities.

A series \(h(X)=cX+\cdots\) with \(c\in R^\times\) has a unique compositional inverse. Solve \(h(k(X))=X\) degree by degree: \(k_1=c^{-1}\), and at degree \(m\) the unknown coefficient of \(k\) has coefficient \(c\), hence has a unique value. The same recursion constructs a left inverse; associativity of substitution identifies left and right inverses. If one starts with the linear, commutative and associative conditions alone, the identity conditions in (1) follow: \(h(X)=F(X,0)\) satisfies \(h\circ h=h\), and its invertible linear coefficient is 1, so composing with its inverse gives \(h=X\). The other identity follows by commutativity.

### Proposition 7.1. The formal group inverse

There is a unique \(\iota_F(X)=-X+\cdots\in R[[X]]\) satisfying

\[
F(X,\iota_F(X))=0.
\tag{2}
\]

It also satisfies \(F(\iota_F(X),X)=0\).

**Proof.** The degree-one term forces \(-X\). Once coefficients below degree \(m\) are chosen, adding a new term \(bX^m\) to that truncation adds exactly \(bX^m\) to \(F(X,\iota_F(X))\) in degree \(m\). The coefficient comes from the linear \(Y\) term; every nonlinear term involving the change has higher degree. Choose \(b\) to cancel the known coefficient. This recursion works over any \(R\), proves uniqueness, and commutativity proves the other identity. \(\square\)

If \(S\) is a separated complete \(R\)-algebra for the powers of an ideal \(I\), evaluation on \(x,y\in I\) converges in the \(I\)-adic topology. Its degree-\(m\) terms lie in \(I^m\). The identities (1)–(2) make \(I\) an abelian group, denoted \(F(I)\), with operation \(x+_F y=F(x,y)\). In a finite extension of a complete valued field, integral coefficients likewise converge on its maximal ideal, since terms of increasing degree have valuation tending to infinity.

The additive law is \(G_a(X,Y)=X+Y\). The multiplicative law is
\(G_m(X,Y)=X+Y+XY\); associativity and commutativity follow from multiplication of \(1+X,1+Y,1+Z\), and its inverse is \(-X/(1+X)\).

A homomorphism \(h:F\to H\) is a zero-constant series satisfying
\[
h(F(X,Y))=H(h(X),h(Y)).
\]
It is an isomorphism if its linear coefficient is a unit, since its compositional inverse then satisfies the reverse homomorphism identity by substitution. The endomorphisms of \(F\) form a ring, with sum \(F(h(X),k(X))\), product \(h\circ k\), zero series 0 and identity \(X\). Associativity of \(F\) supplies additive associativity; \(\iota_F\circ h\) supplies the negative; the homomorphism identity and associativity of composition give distributivity. This ring need not be commutative for an arbitrary formal group.

## 2. The coefficient lemma

Let \(K\) be a nonarchimedean local field, \(\mathcal O=\mathcal O_K\), \(\pi\) a uniformizer, and \(\mathcal O/\pi\mathcal O=\mathbf F_q\). A **Lubin–Tate series for \(\pi\)** is \(f\in\mathcal O[[X]]\) with

\[
f(X)\equiv\pi X\pmod{\text{degree }2},
\qquad f(X)\equiv X^q\pmod\pi.
\tag{3}
\]

Write \(\mathcal F_\pi\) for their set. The series \(\pi X+X^q\) is an example.

### Lemma 7.2. The Lubin–Tate coefficient lemma

For \(f,g\in\mathcal F_\pi\) and \(L(X_1,\ldots,X_d)=\sum_i a_iX_i\), \(a_i\in\mathcal O\), there is a unique zero-constant series \(H\in\mathcal O[[X_1,\ldots,X_d]]\) with linear part \(L\) and

\[
f(H(X))=H(g(X_1),\ldots,g(X_d)).
\tag{4}
\]

**Proof.** Suppose a polynomial \(H_{<m}\) with the prescribed linear part satisfies (4) through degrees below \(m\), where \(m\geq2\). Let \(E_m\) be the homogeneous degree-\(m\) part of the left side minus the right side. Its coefficients are divisible by \(\pi\). Indeed, reducing either side modulo \(\pi\) gives
\(\overline H_{<m}(X)^q\) and \(\overline H_{<m}(X_1^q,\ldots,X_d^q)\), which agree: in characteristic \(p\) the \(q\)-th power respects sums, and each coefficient in \(\mathbf F_q\) satisfies \(a^q=a\).

Adding a homogeneous polynomial \(C_m\) of degree \(m\) changes this error in degree \(m\) by

\[
(\pi-\pi^m)C_m.
\]

On the left only the linear coefficient of \(f\) contributes the change in that degree; on the right substitute the linear terms \(\pi X_i\) into \(C_m\). Nonlinear terms contribute only to later degrees. The unique correction is

\[
C_m=-\frac{E_m}{\pi(1-\pi^{m-1})}.
\tag{5}
\]

It has integral coefficients because \(E_m\) is divisible by \(\pi\) and \(1-\pi^{m-1}\) is a unit. The initial linear equation holds because multiplication by \(\pi\) commutes with \(L\). Induction constructs every homogeneous part and proves (4). If two solutions first differ in degree \(m\), their difference there is killed by \(\pi-\pi^m\), a nonzero element of the domain \(\mathcal O\); hence that difference is zero. This also proves uniqueness. \(\square\)

The coefficients are determined by algebraic degree induction. We are not substituting large elements into the series or assuming that \(\pi\) is an invertible coefficient.

**Computing the first nonlinear part.** For \(f=g=\pi X+X^q\), let \(F\) be the solution with linear part \(X+Y\). All homogeneous parts of degrees \(2,\ldots,q-1\) are zero: the initial error has no terms in those degrees, and (5) then gives zero at each step. In degree \(q\) the initial error is
\((X+Y)^q-X^q-Y^q\). Therefore
\[
F(X,Y)=X+Y+
\frac{\displaystyle\sum_{j=1}^{q-1}\binom qj X^jY^{q-j}}
     {\pi^q-\pi}
\pmod{\text{degree }q+1}.
\]
Each displayed coefficient is integral: reduction modulo \(\pi\) kills the numerator, and \((\pi^q-\pi)/\pi\) is a unit. In equal characteristic the numerator is identically zero. Indeed, in that case the full additive law commutes with \(\pi X+X^q\), so uniqueness proves \(F=X+Y\) in every degree. Over \(\mathbf Q_2\) with \(\pi=2\), the formula gives the coefficient 1 of \(XY\). Here \(2X+X^2=(1+X)^2-1\) commutes with \(X+Y+XY\), and uniqueness proves that this is the full law. The same coefficient construction thus yields different group laws in the two characteristics.

## 3. The group and its scalar action

For \(f\in\mathcal F_\pi\), apply the lemma with two variables, source series \(f\) and linear form \(X+Y\). Denote the resulting series by \(F_f(X,Y)\). For \(f,g\in\mathcal F_\pi\) and \(a\in\mathcal O\), let \([a]_{f,g}\) be the one-variable solution with target \(f\), source \(g\), and linear term \(aX\). Put \([a]_f=[a]_{f,f}\).

### Theorem 7.3. Lubin–Tate formal modules

The series \(F_f\) is a formal group law, and

\[
\mathcal O\longrightarrow\operatorname{End}_{\mathcal O}(F_f),
\qquad a\longmapsto[a]_f
\tag{6}
\]

is an injective ring homomorphism with \([\pi]_f=f\). Each \([a]_{f,g}:F_g\to F_f\) is a homomorphism compatible with these scalar actions. When \(a\) is a unit it is an isomorphism. In particular, all \(F_f\), \(f\in\mathcal F_\pi\), are isomorphic over \(\mathcal O\).

**Proof.** In the following comparisons, the coefficient lemma applies to the indicated linear part and the indicated source series.

The two series \(F_f(X,Y)\) and \(F_f(Y,X)\) satisfy (4) with target \(f\), source \(f\) and linear part \(X+Y\). They are equal. The specialization \(F_f(X,0)\) and the identity \(X\) both commute with \(f\) and have linear term \(X\), so they agree. Finally,
\(F_f(F_f(X,Y),Z)\) and \(F_f(X,F_f(Y,Z))\) both commute with simultaneous substitution of \(f\) in the three variables and have linear part \(X+Y+Z\). Uniqueness gives associativity. Thus \(F_f\) satisfies (1), and Proposition 7.1 supplies its inverse.

The homomorphism identity for \(h=[a]_{f,g}\) follows by comparing
\[
h(F_g(X,Y))\quad\text{and}\quad F_f(h(X),h(Y)).
\]
Both have linear part \(a(X+Y)\), target \(f\) and simultaneous source \(g\). For the first, commute \(h\) with \(g,f\) and use the defining identity for \(F_g\); for the second, use it for \(F_f\). The lemma makes them equal.

Likewise, the identities

\[
\begin{aligned}
[a+b]_{f,g}&=F_f([a]_{f,g},[b]_{f,g}),\\
[a]_{f,g}\circ[b]_{g,h}&=[ab]_{f,h}
\end{aligned}
\tag{7}
\]

follow by comparing their linear parts and commuting equations. Explicitly, for the composition, \(f[a]_{f,g}[b]_{g,h}=[a]_{f,g}g[b]_{g,h}=[a]_{f,g}[b]_{g,h}h\); the sum commutes because \(f\) is an endomorphism of \(F_f\). The solutions of linear parts \(0,X,\pi X\) for target and source \(f\) are respectively \(0,X,f\). These facts prove the ring assertions in (6); injectivity follows by reading the linear coefficient.

Equation (7) also gives
\([a]_{f,g}[b]_g=[ab]_{f,g}=[b]_f[a]_{f,g}\),
so scalar actions are respected. If \(a\) is a unit, \([a^{-1}]_{g,f}\) is the inverse by (7). Taking \(a=1\) gives the final isomorphism assertion. \(\square\)

A formal \(\mathcal O\)-module means a formal group with an \(\mathcal O\)-action whose scalar \(a\) has linear coefficient \(a\). The construction is unique for prescribed \(f=[\pi]\): its law must satisfy (4) with linear part \(X+Y\), and its scalar series must commute with \([\pi]\) and have the prescribed linear coefficient. The lemma determines both. We write \(F_f[\pi^n]\) for its \(\pi^n\)-division points when the series are evaluated in algebraic maximal ideals.

## 4. Frobenius on the completed unramified ring

Let \(\widehat{K^{\mathrm{ur}}}\) be the completion of the maximal unramified extension and \(\widehat{\mathcal O}\) its valuation ring. The uniformizer remains \(\pi\), its residue field is \(\overline{\mathbf F}_q\), and its value group is \(\mathbf Z\). To see that completion does not alter these assertions, a Cauchy sequence representing a nonzero element of the completion has eventually constant valuation, and an integral Cauchy sequence has eventually constant residue. Conversely every algebraic residue element appears in a finite unramified extension. These observations also show that \(\widehat{\mathcal O}\) is a complete discrete valuation ring.

Arithmetic Frobenius is an isometry on the unramified union, so it extends, together with its inverse, to an automorphism \(\varphi\) of the completion. It fixes \(K\) and \(\pi\), and reduces to \(x\mapsto x^q\).

### Lemma 7.4. Additive and multiplicative Frobenius equations

The maps

\[
x\longmapsto\varphi(x)-x
\quad\text{on }\widehat{\mathcal O},\qquad
x\longmapsto\varphi(x)/x
\quad\text{on }\widehat{\mathcal O}^{\times}
\tag{8}
\]

are surjective. Their kernels are \(\mathcal O_K\) and \(\mathcal O_K^\times\), respectively.

**Proof.** For an additive target \(c\), solve \(y^q-y=\bar c\) in the algebraically closed residue field. Lift a solution to \(x_0\). If \(\varphi(x_r)-x_r-c\in\pi^r\widehat{\mathcal O}\), solve \(y^q-y=b\), where \(b\) is the negative residue of \(\pi^{-r}(\varphi(x_r)-x_r-c)\). A correction \(\pi^r y\) removes that error modulo \(\pi^{r+1}\). Inductively the error tends to zero, the corrections tend to zero, and completeness gives an exact solution.

For a unit target \(c\), first solve \(y^{q-1}=\bar c\) with \(y\ne0\) and lift to a unit \(x_0\). Its quotient \(\varphi(x_0)/x_0\) matches \(c\) modulo \(\pi\). If the residual target ratio is \(1+\pi^r b\) modulo \(\pi^{r+1}\), multiply the tentative solution by \(1+\pi^r y\). Its Frobenius ratio is
\[
1+\pi^r(\varphi(y)-y)\pmod{\pi^{r+1}}.
\]
Solving \(y^q-y=\bar b\) improves the agreement. The successive unit corrections form a convergent product, giving an exact preimage of \(c\).

For the kernels, suppose \(\varphi(x)=x\), \(x\in\widehat{\mathcal O}\). Its residue lies in \(\mathbf F_q\), so choose \(a_0\in\mathcal O_K\) with that residue. Then \(x=a_0+\pi x_1\), and \(x_1\) is again fixed. Repeat to express \(x\) as the convergent series \(\sum_{r\geq0}\pi^r a_r\), with all \(a_r\) chosen in a fixed finite set of residue representatives in \(\mathcal O_K\). Completeness of \(K\) puts its limit in \(\mathcal O_K\). The reverse inclusion is fixed by \(\varphi\). For a unit, the same assertion gives precisely \(\mathcal O_K^\times\). \(\square\)

It is the completion that guarantees convergence of the corrections. Their residues can lie in larger and larger finite fields, so there is no reason for the limit to belong to the algebraic unramified union.

## 5. Changing the uniformizer

We need a twisted version of the coefficient lemma. Let \(\pi,\pi'\) be uniformizers, \(f\in\mathcal F_\pi\), \(f'\in\mathcal F_{\pi'}\), and let \(L(X)\) be a linear form over \(\widehat{\mathcal O}\) such that
\[
\pi'L=\pi L^\varphi.
\tag{9}
\]
Superscript \(\varphi\) means that it acts on coefficients, leaving variables alone. Then there is a unique series \(H\) with linear part \(L\) satisfying
\[
f'(H(X))=H^\varphi(f(X_1),\ldots,f(X_d)).
\tag{10}
\]

Here is the full additional coefficient calculation. In degree \(m\geq2\), the error is divisible by \(\pi'\): modulo the maximal ideal the two sides are \(\overline H(X)^q\) and \(\overline H^\varphi(X_1^q,\ldots,X_d^q)\), equal because \(\varphi\) raises residue coefficients to the \(q\)-th power. For a correction coefficient \(a\), the equation is

\[
\pi'a-\pi^m\varphi(a)=-e_m,\qquad e_m\in\pi'\widehat{\mathcal O}.
\]

Put \(\alpha=\pi^m/\pi'\), \(b=-e_m/\pi'\). Since \(v(\alpha)=m-1>0\), the unique solution of \(a-\alpha\varphi(a)=b\) is

\[
a=\sum_{j\geq0}\alpha^j\varphi^j(b).
\tag{11}
\]

The coefficients \(\alpha\) are fixed by \(\varphi\), so substitution telescopes and proves the equation. The terms tend to zero and the ring is complete. A difference of two solutions would satisfy \(a=\alpha\varphi(a)\), impossible for a nonzero element because \(\varphi\) preserves valuation. This proves existence and uniqueness in every homogeneous degree. Condition (9) is exactly the degree-one equation. We have proved (10) without appealing to a formal logarithm.

### Theorem 7.5. Comparison over the completed unramified extension

Suppose \(\pi'=u\pi\), \(u\in\mathcal O_K^\times\). For any \(f\in\mathcal F_\pi\) and \(f'\in\mathcal F_{\pi'}\), there is an isomorphism of formal \(\mathcal O_K\)-modules

\[
\theta:F_f\longrightarrow F_{f'}
\quad\text{over }\widehat{\mathcal O}
\]

with linear term \(\varepsilon X\), where \(\varepsilon\) is a unit satisfying
\[
\varphi(\varepsilon)=u\varepsilon.
\]
It satisfies

\[
\theta^\varphi=\theta\circ[u]_f.
\tag{12}
\]

**Proof.** Lemma 7.4 supplies \(\varepsilon\). Equation (9) holds for \(L=\varepsilon X\), so the twisted lemma constructs \(\theta\) satisfying \(f'\theta=\theta^\varphi f\).

Compare \(\theta(F_f(X,Y))\) and \(F_{f'}(\theta(X),\theta(Y))\). The coefficients of \(F_f,F_{f'}\) are fixed by \(\varphi\). Their commuting identities and \(f'\theta=\theta^\varphi f\) therefore show that both compared series satisfy (10), with linear part \(\varepsilon(X+Y)\). Uniqueness proves the formal group homomorphism identity. Likewise, \(\theta[a]_f\) and \([a]_{f'}\theta\) satisfy (10) with linear term \(\varepsilon aX\), so they agree for every \(a\in\mathcal O_K\). Since \(\varepsilon\) is a unit, the formal compositional inverse exists and makes \(\theta\) an isomorphism.

Finally, \(\theta^\varphi\) satisfies (10) by applying \(\varphi\) to its defining equality. The series \(\theta[u]_f\) satisfies the same equation because \([u]_f\) commutes with \(f\) and has fixed coefficients. Their linear terms agree, \(\varphi(\varepsilon)X=\varepsilon uX\), so uniqueness gives (12). \(\square\)

The direction matters: with \(\pi'=u\pi\), the source of \(\theta\) is the group for \(\pi\), and \([u]_f\) in (12) acts on that source. Inverting the direction changes the corresponding unit equation.

## 6. The multiplicative example over \(\mathbf Z_p\)

For \(a\in\mathbf Z_p\), the binomial series

\[
[a](X)=(1+X)^a-1=\sum_{j\geq1}\binom aj X^j
\tag{13}
\]

has integral coefficients. For fixed \(j\), \(\binom aj\) is a continuous polynomial function of \(a\) over \(\mathbf Q_p\). Approximate \(a\) by nonnegative integers, whose binomial coefficients are integral; closedness of \(\mathbf Z_p\) proves the assertion.

For nonnegative integers, (13) respects \(G_m\) by the ordinary power identity. Taking coefficientwise limits proves the homomorphism identity for \(a\in\mathbf Z_p\), since each coefficient of a substituted identity depends on finitely many coefficients. The same reasoning applied to integer pairs gives
\[
[a+b]=G_m([a],[b]),\qquad [ab]=[a]\circ[b].
\]
The series \(f=(1+X)^p-1\) has linear term \(pX\) and reduction \(X^p\), so belongs to \(\mathcal F_p\). The group \(G_m\) and its series (13) satisfy the defining equations of Theorem 7.3; uniqueness identifies them with \(F_f\) and \([a]_f\). The other choice \(pX+X^p\) therefore yields a formal group isomorphic to \(G_m\) over \(\mathbf Z_p\).

Every endomorphism \(h\) of \(G_m\) over \(\mathbf Z_p\) commutes with its integer multiplication \([p]\), because a homomorphism preserves a repeated group sum. If its linear coefficient is \(a\), Lemma 7.2 makes it the unique series commuting with \(f=[p]\) and starting with \(aX\). Thus it is (13), proving

\[
\operatorname{End}_{\mathbf Z_p}(G_m)=\mathbf Z_p
\]

with the ring operations already described. This argument does not assert an analogous derivative classification for arbitrary formal groups in positive characteristic.

## Exercises

1. **Easy.** Verify the formal group identities for \(G_m\), its inverse, and the integral scalar series \((1+X)^a-1\), \(a\in\mathbf Z_p\).
2. **Medium.** Construct the formal inverse of an arbitrary \(F\) over an arbitrary commutative ring, proving uniqueness without division by integers.
3. **Medium.** Prove that every endomorphism of \(G_m\) over \(\mathbf Z_p\) is \((1+X)^a-1\) for a unique \(a\in\mathbf Z_p\).
4. **Hard.** Prove both surjectivities in Lemma 7.4, identify both kernels, and explain why completing the unramified union is part of the argument.

## Solutions

1. Multiplying \(1+X,1+Y\) yields \(1+G_m(X,Y)\), so commutativity, associativity and the identity follow from multiplication in \(R[[X,Y,Z]]\). The inverse is \(-X/(1+X)=-X+X^2-\cdots\). For fixed \(j\), the continuous polynomial \(\binom aj\) takes integral values at nonnegative integers dense in \(\mathbf Z_p\); its value at \(a\) is therefore integral. The integer power identity gives the scalar homomorphism identity, and coefficientwise continuity extends it to every \(a\). The same extension for addition and composition gives the scalar ring action.
2. Write the desired inverse as \(-X+\sum_{m\geq2}b_mX^m\). After coefficients below \(m\) are set, the degree-\(m\) coefficient of \(F(X,\iota(X))\) is a known element plus \(b_m\). A new \(b_mX^m\) entering a nonlinear term has degree at least \(m+1\), so its only contribution at degree \(m\) comes from the linear \(Y\). Set \(b_m\) to the negative of the known coefficient. This recursion uses no division and gives existence and uniqueness in every degree. Commutativity gives the left inverse identity as well.
3. An endomorphism preserves \(p\) repeated sums, hence commutes with \(f=(1+X)^p-1\). Its linear coefficient \(a\) lies in \(\mathbf Z_p\). Lemma 7.2 with one variable says that exactly one series with linear part \(aX\) commutes with \(f\). The integral series (13) is such a series, so it is the endomorphism. Conversely all those series are endomorphisms by solution 1. Linear coefficients distinguish \(a\), and the addition and composition identities identify the endomorphism ring with \(\mathbf Z_p\).
4. Reduce an additive target modulo \(\pi\) and solve \(y^q-y=c\) in \(\overline{\mathbf F}_q\); successive corrections \(\pi^r y_r\) solve the next residue error, producing a Cauchy sequence. For a unit target, first solve \(y^{q-1}=c\) with \(y\ne0\), then correct with factors \(1+\pi^r y_r\). Their Frobenius quotients have residue correction \(y_r^q-y_r\), so this also improves the error one depth at a time. The product is Cauchy and remains a unit; continuity gives the exact solution. A fixed integral element has residue in \(\mathbf F_q\); subtract its ground-field representative, divide by \(\pi\), and repeat. Its resulting ground-field digit series converges in \(K\), proving the additive kernel is \(\mathcal O_K\), and the unit kernel is \(\mathcal O_K^\times\). The correction residues need not stay in one finite residue extension, so their limit is guaranteed in the completion, not in the uncompleted algebraic union.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

Sections 1–3 prove inversion, coefficient correction, every formal-group identity and scalar compatibility. The first nonlinear coefficients are computed explicitly. Sections 4–6 prove the Frobenius equations and the twisted construction over the completed unramified ring.

- [J. S. Milne, Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf).
- [Teruyoshi Yoshida, Local class field theory via Lubin–Tate theory, arXiv:math/0606108v2](https://arxiv.org/abs/math/0606108v2).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
