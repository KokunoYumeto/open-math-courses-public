# The sharp noncommutative bilinear inequality

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).* 

The [preceding lesson](tensor-completion-injectivity-and-state-domination.md) supplies a universal state-domination constant. Complex interpolation and a fourth moment of independent phases improve any such constant to its geometric mean with the norm of the form. At the best constant, this forces the Grothendieck–Haagerup–Pisier bound.

We retain arbitrary C*-algebras, with no separability, nuclearity or trace hypothesis. The universal bidual and its polar decomposition are the exact foundations prerequisites already used in the [nuclear bidual lesson](nuclear-biduals-and-extensions.md); general weight and expectation theory is not needed here.

## 1. The statement and its finite-family form

**Theorem 1.1.** Let \(A,B\) be nonzero C*-algebras and \(V:A\times B\to\mathbb C\) bounded and bilinear. There are states \(\varphi_1,\varphi_2\) on \(A\) and \(\psi_1,\psi_2\) on \(B\) such that
\[
|V(x,y)|\le\|V\|
\big[\varphi_1(x^*x)+\varphi_2(xx^*)\big]^{1/2}
\big[\psi_1(y^*y)+\psi_2(yy^*)\big]^{1/2}.
\tag{1}
\]
For a zero algebra the form is zero and the numerical inequality is vacuous; there is no state of norm one on the zero algebra.

For finite families set
\[
R(x)=\Big\|\sum_jx_j^*x_j\Big\|+\Big\|\sum_jx_jx_j^*\Big\|.
\tag{2}
\]

**Lemma 1.2.** For unital \(A,B\), the existence of the four states in (1), with a constant \(C\) in place of \(\|V\|\), is equivalent to
\[
\Big|\sum_jV(x_j,y_j)\Big|\le C R(x)^{1/2}R(y)^{1/2}
\tag{3}
\]
for every pair of finite families.

**Proof.** Given the states, sum the pointwise bounds and apply scalar Cauchy–Schwarz. Each state evaluates a positive square sum below its norm, giving (3).

Conversely use the compact convex space \(Q=S(A)^2\times S(B)^2\). Write \(s(x)=\varphi_1(x^*x)+\varphi_2(xx^*)\), \(t(y)=\psi_1(y^*y)+\psi_2(yy^*)\), and impose all affine inequalities
\[
\tfrac C2[s(x)+t(y)]-\operatorname{Re}V(x,y)\ge0.
\tag{4}
\]
For a finite nonnegative combination, absorb the square roots of its coefficients into both variables. Choose the four states separately norming the four positive square sums. The combined function then has value at least \(C[R(x)+R(y)]/2-C\sqrt{R(x)R(y)}\ge0\), by (3). The compact affine argument in the preceding lesson gives one quadruple satisfying all (4). Replace \(x\) by \(-x\), rescale \((x,y)\) to \((a x,a^{-1}y)\) with \(a>0\), and minimize. Finally rotate \(x\) by a scalar phase. The quadratic functions are phase invariant, so the resulting bound controls \(|V(x,y)|\). \(\square\)

## 2. Independent phases and fourth moments

Let \(\zeta_1,\ldots,\zeta_n\) be independent uniform coordinates on \(\mathbb T^n\), with its normalized product Haar probability, and set \(X=\sum_j\zeta_jx_j\). Only finite products are used.

**Lemma 2.1.** For arbitrary, possibly noncommuting \(x_j\),
\[
\|\mathbb E(X^*X)^2\|+\|\mathbb E(XX^*)^2\|\le R(x)^2.
\tag{5}
\]

**Proof.** Put \(S=\sum x_j^*x_j\), \(T=\sum x_jx_j^*\). In the expansion of \((X^*X)^2\), a phase average is nonzero exactly when the multiset of conjugated indices equals that of unconjugated indices. The pairings \(i=j,k=l\) and \(i=l,j=k\) share their all-equal terms, which must be counted once. Thus
\[
\mathbb E(X^*X)^2
=S^2+\sum_ix_i^*T x_i-\sum_i(x_i^*x_i)^2
\le S^2+\|T\|S.
\tag{6}
\]
The adjoint calculation gives \(\mathbb E(XX^*)^2\le T^2+\|S\|T\). Taking norms and adding bounds the left side by \(\|S\|^2+2\|S\|\|T\|+\|T\|^2\), which is (5). \(\square\)

The independent phases remove the additional pairing that survives for real signs. The subtraction in (6) records the overlap of the two valid pairings, not a commuting-coefficient simplification.

## 3. Polar powers in the original algebra

**Lemma 3.1.** If \(x=u|x|\) is its polar decomposition in \(A^{**}\), then
\[
f_x(z)=u|x|^z,\qquad \operatorname{Re}z>0,
\tag{7}
\]
is an \(A\)-valued norm-holomorphic function, where the power is zero on the kernel. For \(s=\operatorname{Re}z>0\),
\[
f_x(z)^*f_x(z)=(x^*x)^s,
\quad f_x(z)f_x(z)^*=(xx^*)^s,
\quad \|f_x(z)\|=\|x\|^s.
\tag{8}
\]

**Proof.** The case \(x=0\) is immediate. The set of continuous functions \(g\) on \([0,\|x\|]\) for which \(u g(|x|)\in A\) is a closed ideal: multiply on the right by the continuous functional calculus in the unitization of \(A\). It contains the identity function \(g(t)=t\), since \(u|x|=x\). Its closed ideal therefore contains every continuous function vanishing at zero, including \(t^z\) for \(\operatorname{Re}z>0\).

Let \(p_n=1_{[1/n,\|x\|]}(|x|)\) in the bidual. On its support \(|x|p_n\) has a bounded logarithm, so \(u|x|^z p_n\) is bidual-valued entire. On a compact subset with \(\operatorname{Re}z\ge\varepsilon>0\), its distance from (7) is at most \(n^{-\varepsilon}\). Hence (7) is norm-holomorphic into the bidual and takes values in its closed subspace \(A\), so is \(A\)-valued holomorphic. The support identities for the polar decomposition and functional calculus give (8). \(\square\)

We also recall the scalar three-lines bound with its proof. If \(h\) is bounded and holomorphic in a closed strip \(a\le\operatorname{Re}z\le b\), continuous on its boundary, and bounded there by \(M_a,M_b>0\), divide it by \(M_a^{(b-z)/(b-a)}M_b^{(z-a)/(b-a)}\). The quotient has modulus at most one on the vertical boundaries and is bounded in the strip. Multiply by \(e^{\delta(z-a)^2}\), apply the maximum principle on rectangles, and let their horizontal sides tend to infinity: the new horizontal values tend to zero. The resulting bound is at most \(e^{\delta(b-a)^2}\). Let \(\delta\downarrow0\). Thus
\[
|h(s)|\le M_a^{(b-s)/(b-a)}M_b^{(s-a)/(b-a)},
\quad a\le s\le b.
\tag{9}
\]
Zero boundary bounds follow by adding a positive tolerance and taking its limit.

## 4. Improving the best constant

Assume \(A,B\) unital and \(V\ne0\). Let \(c\) be the infimum of constants admitting four-state domination. The preliminary bound proves \(c\le(81/16)\|V\|<\infty\). Also \(c\ge\|V\|/2>0\), since each quadratic sum is at most \(2\) on the unit ball. Compactness of the four state spaces, using a convergent subnet of quadruples with constants tending to \(c\), gives a quadruple attaining \(c\).

For this quadruple define
\[
P(x)=\varphi_1((x^*x)^2)+\varphi_2((xx^*)^2),
\quad Q(y)=\psi_1((y^*y)^2)+\psi_2((yy^*)^2).
\]
For \(h(z)=V(f_x(z),f_y(z))\), (8) gives
\[
|h(2+it)|\le c P(x)^{1/2}Q(y)^{1/2},
\quad
|h(\varepsilon+it)|\le\|V\|\|x\|^\varepsilon\|y\|^\varepsilon.
\tag{10}
\]
It is bounded on each closed strip \(\varepsilon\le\operatorname{Re}z\le2\). Apply (9) at \(z=1\), then let \(\varepsilon\downarrow0\). For nonzero \(x,y\), their norm powers tend to one; zero variables are immediate. We get
\[
|V(x,y)|\le\sqrt{c\|V\|}\,P(x)^{1/4}Q(y)^{1/4}.
\tag{11}
\]

Now put \(X=\sum_j\zeta_jx_j\), \(Y=\sum_j\overline{\zeta_j}y_j\). Bilinearity and phase orthogonality give
\[
\sum_jV(x_j,y_j)=\mathbb E V(X,Y).
\tag{12}
\]
Hölder, with exponents \(4,4,2\) and the third factor equal to one, bounds the expectation in (11) by
\[
\sqrt{c\|V\|}\,[\mathbb E P(X)]^{1/4}[\mathbb E Q(Y)]^{1/4}
\le\sqrt{c\|V\|}\,R(x)^{1/2}R(y)^{1/2},
\tag{13}
\]
where (5) bounds each sum of state evaluations by the sum of the two operator norms. Conjugated coordinates have the same fourth-moment calculation.

Lemma 1.2 now produces four-state domination with constant \(\sqrt{c\|V\|}\). By minimality, \(c\le\sqrt{c\|V\|}\); since \(c>0\), this gives \(c\le\|V\|\), proving (1) for unital algebras. For \(V=0\), arbitrary states give (1).

## 5. Nonunital algebras with the same constant

The nonunital case needs a norm-preserving extension of the bilinear form, rather than arbitrary coefficient projections of norm two. Define \(T:A\to B^*\) by \((Tx)(y)=V(x,y)\). Its adjoint \(T^*:B^{**}\to A^*\) gives the bilinear extension
\[
\overline V(F,G)=F(T^*G),\quad F\in A^{**},\ G\in B^{**},
\qquad \|\overline V\|=\|V\|.
\tag{14}
\]
The upper bound follows from dual norms, and restriction to \(A\times B\) gives the reverse bound. No separate normality in both variables is asserted or needed.

The canonical maps from the forced C*-unitizations into their biduals,
\(a+\lambda1\mapsto a+\lambda1_{A^{**}}\), are contractive *-homomorphisms. Restrict (14) along these maps. The resulting bilinear form on the two unitizations extends \(V\) with exactly its norm. Apply the unital theorem and restrict its four states to \(A,B\). The restrictions are positive of norm at most one. A nonzero restriction can be divided by its norm, which only increases the dominating quadratic values. Replace a zero restriction by any state of its nonzero algebra. This supplies four states and keeps the constant \(\|V\|\), completing Theorem 1.1.

## 6. A symmetric corollary and optimality

With \(\varphi=(\varphi_1+\varphi_2)/2\), \(\psi=(\psi_1+\psi_2)/2\), positivity gives
\[
|V(x,y)|\le4\|V\|\varphi(q(x))^{1/2}\psi(q(y))^{1/2}.
\tag{15}
\]
Indeed, the first bracket in (1) is at most \(4\varphi(q(x))\), and similarly for the other bracket. This is a convenient symmetric consequence; the sharp assertion concerns the four-state coefficient in (1).

That coefficient cannot be replaced universally by \(C\|V\|\) with \(C<1\). On \(B(\ell^2(\mathbb N))\), choose any state \(\omega\) and \(V(x,y)=\omega(xy)\), with \(\|V\|=1\). For every positive integer \(n\), choose isometries \(u_1,\ldots,u_n\) with orthogonal range projections summing to one, by partitioning the standard basis into \(n\) infinite sets. Apply the proposed bound to \((u_j^*,u_j)\) and sum. Its left side is \(n\); scalar Cauchy–Schwarz makes its right side at most \(C(n+1)\), since \(\sum u_j u_j^*=1\) and \(\sum u_j^*u_j=n1\). Therefore \(C\ge n/(n+1)\) for every \(n\), and \(C\ge1\).

## 7. Exercises with complete solutions

**Exercise 1.** Why are there four independent norming states in the converse of Lemma 1.2?

*Solution.* Each of the four positive sums can be normed by a state on its own algebra. The two sums in \(A\) need not have a common norming state, and the same is true in \(B\). The independent choices make the maximum of \(\sum s(x_j)\) equal to the sum of the two norms, exactly \(R(x)\). Averaging those choices prematurely can lose this equality.

**Exercise 2.** Verify the all-equal correction in (6).

*Solution.* Both pairings \(i=j,k=l\) and \(i=l,j=k\) contribute when all four indices coincide. Their two unrestricted sums therefore count \((x_i^*x_i)^2\) twice. Subtracting \(\sum_i(x_i^*x_i)^2\) leaves one copy. All other valid index patterns appear once, giving the exact expectation.

**Exercise 3.** Can the fourth moments be checked with a finite phase distribution?

*Solution.* Yes. Independent uniform third roots of unity have mean zero and second power mean zero. In a fourth-moment monomial each coordinate exponent belongs to \(\{-2,-1,0,1,2\}\); its expectation is zero unless that exponent is zero. Thus exactly the same pairings survive as for Haar phases. Finite \(3^n\)-point samples verify the fourth-moment identity exactly, although they do not prove the analytic interpolation step.

**Exercise 4.** Why does a polar power with \(0<\operatorname{Re}z<1\) still belong to \(A\)?

*Solution.* The factor \(|x|^{z-1}\) may be unbounded at zero, so the expression \(x|x|^{z-1}\) alone is not a bounded functional-calculus proof. Instead \(t^z\) is continuous and vanishes at zero. It belongs to the closed ideal generated by \(t\), whose elements \(g\) satisfy \(ug(|x|)\in A\). The ideal argument in Lemma 3.1 supplies the required membership.

**Exercise 5.** Give the uniform error estimate for the spectral cutoffs in Lemma 3.1.

*Solution.* On the omitted spectral interval \(0\le t<1/n\), \(|t^z|=t^{\operatorname{Re}z}\le n^{-\varepsilon}\) if \(\operatorname{Re}z\ge\varepsilon>0\). The partial isometry has norm at most one. Thus the cutoff error is at most \(n^{-\varepsilon}\), uniformly on any compact subset of the half-plane. A norm-uniform limit of holomorphic functions is holomorphic.

**Exercise 6.** Compute the exponents of the two boundary bounds in (10).

*Solution.* At the point \(1\) in the strip \([\varepsilon,2]\), the left and right boundary exponents are \(1/(2-\varepsilon)\) and \((1-\varepsilon)/(2-\varepsilon)\). Both tend to \(1/2\). The right boundary already contains \(P^{1/2}Q^{1/2}\), so the limiting powers are \(P^{1/4}Q^{1/4}\). This yields (11).

**Exercise 7.** Why must the phases in \(Y\) be conjugated in (12)?

*Solution.* Bilinearity gives coefficients \(\zeta_i\overline{\zeta_j}\), whose expectation is \(\delta_{ij}\). Without conjugation the coefficients would be \(\zeta_i\zeta_j\), all of which have zero expectation, including when \(i=j\). The proposed identity would then lose every diagonal term.

**Exercise 8.** Justify the zero and positivity cases when improving the constant.

*Solution.* If \(V=0\), arbitrary states work and no division is needed. Otherwise any four-state bound of constant \(C\) gives \(|V(x,y)|\le2C\) for unit-ball variables, hence \(C\ge\|V\|/2\). The attained infimum \(c\) is therefore positive, so dividing \(c\le\sqrt{c\|V\|}\) by \(\sqrt c\) is legitimate.

**Exercise 9.** Verify norm preservation in the nonunital extension.

*Solution.* The map \(T\) has norm \(\|V\|\), so \(|F(T^*G)|\le\|V\|\|F\|\|G\|\). On the canonical copies of \(A,B\), evaluation is \(V(x,y)\), giving equality of norms. Contractive maps from the unitizations cannot increase the norm; their restriction to \(A,B\) still realizes \(V\), so the unitized extension also has exactly the original norm.

**Exercise 10.** Derive \(n\le C(n+1)\) in the optimality example.

*Solution.* For \(x_j=u_j^*\), the sums \(\sum x_j^*x_j\), \(\sum x_jx_j^*\) are \(1,n1\); for \(y_j=u_j\), the sums are \(n1,1\). The sums of their state quadratic values are therefore both \(n+1\). Summing the individual bounds and applying scalar Cauchy–Schwarz gives \(\sum_j|V(u_j^*,u_j)|\le C(n+1)\). Each value is \(\omega(1)=1\), so the left side is \(n\).

## References

Gilles Pisier, [*Grothendieck's Theorem, past and present*, expanded UNCUT author version, 21 August 2013](https://webusers.imj-prg.fr/~gilles.pisier/grothendieck.UNCUT.pdf), Section 7, Theorem 7.1 and (7.1)–(7.3), printed p.25 (PDF p.27), states the four-state inequality by reference to Haagerup. Its coefficient is 1 in the sum-of-two-norms formulation, and 2 when each such sum is replaced by twice its maximum. Section 11, printed pp.35–36 (PDF pp.37–38), gives the finite CAR optimality construction in that latter normalization. Section 9 and Appendix 23 supply the actually read fourth-moment, truncation and state-selection methods.

The complete proof of Theorem 1.1 is in Sections 4–5 here, using Lemmas 1.2, 2.1 and 3.1 and the preceding two lessons. It includes the attained best constant, a proved scalar three-lines bound, polar powers in the original algebra, conjugated phase coordinates and a norm-preserving nonunital extension. Section 6 proves coefficient-one optimality by infinite orthogonal isometries; it does not substitute the CAR normalization. The survey's statement is not treated as its full proof, and its omitted complex reduction is not used to fill a local gap. Exact transitive free foundation closure remains pending; no source expression was imported.
