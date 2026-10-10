# A determinant obstruction from field norms

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Erdős's parabola (first lesson) uses three points \((1,x,x^2)\) over \(\mathbb F_p\): distinct labels give a nonzero Vandermonde determinant. This lesson builds random integer columns, modulo a large prime power \(h=B^k\), that carry the same information in a hidden form. Every column has a random label \(\xi\) in a finite field \(K\). If the three labels of three columns are distinct, the determinant of the columns modulo \(h\) is far from zero: it has no representative in \([-\tau,\tau]\) with \(\tau\approx B^{k-1}/2\). The construction takes the norm of the Vandermonde determinant, writes the resulting polynomial over \(\mathbb F_r\) as a sum of determinants of monomials, and places each summand at a designated digit of a base-\(B\) expansion, so that one digit of the determinant equals the norm.

We use from the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40) (Judson, *Abstract Algebra: Theory and Applications*): splitting fields exist ([Theorem 21.2.3](https://judsonbooks.org/aata-files/aata-html/fields-section-splitting-fields.html)); in characteristic \(p\), \((a+b)^{p^n}=a^{p^n}+b^{p^n}\) ([Lemma 22.1.3](https://judsonbooks.org/aata-files/aata-html/finite-section-field.html)); and for every prime \(p\) and \(n\geq1\) there is a field with \(p^n\) elements, the splitting field of \(x^{p^n}-x\) over \(\mathbb F_p\) ([Theorem 22.1.6](https://judsonbooks.org/aata-files/aata-html/finite-section-field.html)). From [Small triangles and the plan](small-triangles-and-the-plan.md) we use primes in intervals (Lemma 4.3).

## 1. Finite fields and norms

Let \(r\) be an odd prime, \(d\geq1\) odd, and \(K\) a field with \(r^d\) elements (Judson, Theorem 22.1.6). It contains the prime field \(\mathbb F_r\), and is a vector space of dimension \(d\) over it. Every \(t\in K\) satisfies \(t^{r^d}=t\) (the nonzero elements form a group of order \(r^d-1\)).

The *Frobenius map* \(\sigma(t)=t^r\) is a ring homomorphism of \(K\) (Judson, Lemma 22.1.3), injective because \(K\) is a field, hence bijective; and \(\sigma^d=\mathrm{id}\). Its fixed points are the roots of \(X^r-X\), at most \(r\) of them; the \(r\) elements of \(\mathbb F_r\) are fixed (Fermat's little theorem), so the fixed field of \(\sigma\) is exactly \(\mathbb F_r\).

The *norm* of \(t\in K\) is \(\operatorname{Nm}(t)=\prod_{j=0}^{d-1}\sigma^j(t)\). Since \(\sigma\) permutes the factors cyclically, \(\sigma(\operatorname{Nm}t)=\operatorname{Nm}t\), so \(\operatorname{Nm}t\in\mathbb F_r\). It is multiplicative, and \(\operatorname{Nm}t\neq0\) for \(t\neq0\).

## 2. The norm polynomial

Fix an \(\mathbb F_r\)-basis \(\beta_1,\ldots,\beta_d\) of \(K\). A *group* of variables is an array \(X=(X_{i\nu})_{1\leq i\leq3,\,1\leq\nu\leq d}\) of \(3d\) variables; put
\[
Z(X)=\begin{pmatrix}\sum_\nu\beta_\nu X_{1\nu}\\ \sum_\nu\beta_\nu X_{2\nu}\\ \sum_\nu\beta_\nu X_{3\nu}\end{pmatrix}.
\]
For three disjoint groups \(X^{(1)},X^{(2)},X^{(3)}\) let \(\mathcal D=\det\bigl(Z(X^{(1)}),Z(X^{(2)}),Z(X^{(3)})\bigr)\), a polynomial with coefficients in \(K\), of degree one in each group. Let \(\sigma\) act on polynomials by applying \(\sigma\) to the coefficients, and put
\[
\mathcal N=\prod_{j=0}^{d-1}\sigma^j(\mathcal D).\tag{2.1}
\]

**Lemma 2.1.** (a) \(\mathcal N\) has coefficients in \(\mathbb F_r\) and is homogeneous of degree \(d\) in each group.

(b) For \(U^{(1)},U^{(2)},U^{(3)}\in\mathbb F_r^{3d}\), the value \(\mathcal N(U^{(1)},U^{(2)},U^{(3)})\) is the norm of \(\det\bigl(Z(U^{(1)}),Z(U^{(2)}),Z(U^{(3)})\bigr)\).

(c) \(\mathcal N\) is *alternating*: exchanging two groups changes its sign.

*Proof.* (a) Applying \(\sigma\) permutes the factors of (2.1) cyclically, so \(\sigma(\mathcal N)=\mathcal N\) and the coefficients are fixed by \(\sigma\). Each factor has degree one in each group. (b) Evaluating at values in \(\mathbb F_r\), which \(\sigma\) fixes, commutes with \(\sigma\): \(\sigma^j(\mathcal D)(U)=\sigma^j(\mathcal D(U))\). (c) Exchanging two groups changes the sign of \(\mathcal D\), hence of each of the \(d\) factors; \(d\) is odd. \(\square\)

Let \(m_1,\ldots,m_M\) be the monomials of degree \(d\) in \(3d\) variables, \(M=\binom{4d-1}d\), and \(T=\binom M3\).

**Lemma 2.2 (a sum of determinants).** There are polynomials \(f_{ia}\in\mathbb F_r[X]\), for \(1\leq i\leq3\) and \(0\leq a<T\), each a monomial of degree \(d\) times a scalar (the scalar being \(1\) for \(i=2,3\)), such that, with \(1\leq i,j\leq3\),
\[
\begin{aligned}
&\mathcal N(X^{(1)},X^{(2)},X^{(3)})\\
&=\sum_{a=0}^{T-1}\det\bigl(f_{ia}(X^{(j)})\bigr)_{i,j}.
\end{aligned}\tag{2.2}
\]

*Proof.* Write \(m_{pqs}=m_p(X^{(1)})\,m_q(X^{(2)})\,m_s(X^{(3)})\). By Lemma 2.1(a), \(\mathcal N=\sum_{p,q,s}c(p,q,s)\,m_{pqs}\) with \(c(p,q,s)\in\mathbb F_r\). Exchanging the first two groups and comparing coefficients, Lemma 2.1(c) gives \(c(q,p,s)=-c(p,q,s)\), and likewise for the other transpositions. If two of \(p,q,s\) coincide, the coefficient equals its own negative and vanishes, since \(r\) is odd. For \(p<q<s\) put \(c_{pqs}=c(p,q,s)\); the coefficients of the six orderings of \(\{p,q,s\}\) are \(c_{pqs}\) times the signs of the permutations, so these six terms add up to, with \(m^{(j)}_p=m_p(X^{(j)})\),
\[
c_{pqs}\det\begin{pmatrix}m^{(1)}_p&m^{(2)}_p&m^{(3)}_p\\ m^{(1)}_q&m^{(2)}_q&m^{(3)}_q\\ m^{(1)}_s&m^{(2)}_s&m^{(3)}_s\end{pmatrix}.
\]
Number the \(T\) triples \(p<q<s\) by \(a\) and put \((f_{1a},f_{2a},f_{3a})=(c_{pqs}m_p,m_q,m_s)\). \(\square\)

*Labels.* For \(\xi\in K\) let \(z(\xi)=(1,\xi,\xi^2)^{\mathsf T}\) and let \(X(\xi)\in\mathbb F_r^{3d}\) be the coordinates of its three entries in the basis \(\beta\), so that \(Z(X(\xi))=z(\xi)\). By Lemma 2.1(b) and the Vandermonde determinant, if \(\xi_1,\xi_2,\xi_3\) are distinct, then
\[
\begin{aligned}
&\mathcal N\bigl(X(\xi_1),X(\xi_2),X(\xi_3)\bigr)\\
&=\operatorname{Nm}\prod_{i<j}(\xi_j-\xi_i)\neq0.
\end{aligned}\tag{2.3}
\]
The basis and the polynomials \(f_{ia}\) depend on \(r\); the numbers \(d,M,T\) do not.

## 3. Digits

From now on fix
\[
\begin{gathered}
d=41,\quad M=\binom{4d-1}d,\\
T=\binom M3,\quad k=T^2+1,\\
L=r^{10},
\end{gathered}\tag{3.1}
\]
and, for every sufficiently large odd prime \(r\), a prime \(B\) with
\[
\begin{gathered}
100k^2L^3<B\leq200k^2L^3,\\
h=B^k,\quad\tau=\Bigl\lfloor\frac{B^{k-1}}2\Bigr\rfloor,\\
R_h=\mathbb Z/h\mathbb Z,
\end{gathered}\tag{3.2}
\]
which exists by Lemma 4.3 of the first lesson. For \(0\leq a<T\) designate the *positions* \(i_a\) in row \(1\), \(j_a\) in row \(2\) and \(\ell_a\) in row \(3\):
\[
\begin{aligned}
i_a&=a,\\
j_a&=Ta,\\
\ell_a&=T^2-(T+1)a.
\end{aligned}\tag{3.3}
\]
They lie in \(\{0,\ldots,k-1\}\) (namely in \([0,T-1]\), \([0,T^2-T]\) and \([1,T^2]\)), and are distinct within each row.

**Lemma 3.1 (matching positions).** \(i_a+j_{a'}+\ell_{a''}=k-1\) if and only if \(a=a'=a''\).

*Proof.* The equation is \(a+Ta'=(T+1)a''\). Modulo \(T\) it gives \(a\equiv a''\), so \(a=a''\) since both lie in \([0,T)\); then \(Ta'=Ta''\). Conversely \(a+Ta+T^2-(T+1)a=T^2=k-1\). \(\square\)

**The random column.** Choose a label \(\xi\) uniformly in \(K\). For every row \(1\leq i\leq3\) and position \(0\leq v<k\) choose a *digit* \(c_{iv}\in\{1,\ldots,L\}\) with a prescribed residue modulo \(r\): \(f_{1a}(X(\xi))\) at \((1,i_a)\), \(f_{2a}(X(\xi))\) at \((2,j_a)\), \(f_{3a}(X(\xi))\) at \((3,\ell_a)\), and \(0\) at all other positions. Given \(\xi\), the \(3k\) digits are independent and uniform among the \(L/r=r^9\) numbers in \(\{1,\ldots,L\}\) with the prescribed residue. The column is
\[
\begin{gathered}
c=(c_1,c_2,c_3)^{\mathsf T}\in R_h^3,\\
c_i=\sum_{v=0}^{k-1}c_{iv}B^v\bmod h .
\end{gathered}\tag{3.4}
\]
Since \(1\leq c_{i0}\leq L<B\), every entry of \(c\) is a unit of \(R_h\). Different columns use independent labels and independent digits, even if their labels coincide.

**Lemma 3.2 (determinant obstruction).** Let \(C\) be the matrix of three columns built by (3.4), with labels \(\xi_1,\xi_2,\xi_3\). If the labels are distinct, then \(\det C\in R_h\) has no integer representative in \([-\tau,\tau]\).

*Proof.* Let \(c^{(j)}_{iv}\) be the digit of column \(j\) at row \(i\) and position \(v\), and consider the integer polynomial
\[
\begin{aligned}
F(Y)&=\det\Bigl(\sum_{v=0}^{k-1}c^{(j)}_{iv}Y^v\Bigr)_{i,j\leq3}\\
&=\sum_{u=0}^{3(k-1)}\gamma_uY^u .
\end{aligned}
\]
*Size of the coefficients.* In the expansion over the six permutations, the coefficient of \(Y^u\) collects, for each permutation, products of three digits whose positions add up to \(u\); two positions determine the third, so
\[
|\gamma_u|\leq6k^2L^3 .\tag{3.5}
\]
*The coefficient of \(Y^{k-1}\).* Expanding the determinant by multilinearity in the rows, \(\gamma_{k-1}\) is the sum, over positions \(v_1+v_2+v_3=k-1\), of the determinants whose \(i\)-th row is the vector of digits of the three columns at row \(i\) and position \(v_i\). Modulo \(r\), a row taken at a non-designated position vanishes, and by Lemma 3.1 the remaining positions are \((i_a,j_a,\ell_a)\), \(0\leq a<T\). So, by the prescribed residues and (2.2), (2.3),
\[
\begin{aligned}
\gamma_{k-1}&\equiv\sum_a\det\bigl(f_{ia}(X(\xi_j))\bigr)_{i,j}\\
&=\mathcal N\bigl(X(\xi_1),X(\xi_2),X(\xi_3)\bigr)\\
&\not\equiv0\pmod r ,
\end{aligned}
\]
and in particular \(|\gamma_{k-1}|\geq1\).

*The determinant.* The integer \(S=\sum_{u=0}^{k-1}\gamma_uB^u\) represents \(\det C\) modulo \(h\): \(\det C\) is \(F(B)\) modulo \(h\), and the terms with \(u\geq k\) are divisible by \(B^k=h\). Since \(B-1\geq100k^2L^3\), (3.5) gives
\[
\begin{gathered}
|S|\leq6k^2L^3\frac{B^k-1}{B-1}\leq\frac3{50}(h-1)<\frac h2,\\
\Bigl|\sum_{u=0}^{k-2}\gamma_uB^u\Bigr|\leq\frac3{50}(B^{k-1}-1),
\end{gathered}
\]
and therefore
\[
\begin{aligned}
|S|&\geq B^{k-1}-\frac3{50}(B^{k-1}-1)\\
&=\frac{47B^{k-1}+3}{50}>\tau .
\end{aligned}
\]
Every other representative \(S+mh\), \(m\neq0\), has absolute value at least \(h-|S|>h/2>\tau\). \(\square\)

**Corollary 3.3.** If \(G\in\mathrm{SL}_3(R_h)\) and an integer matrix \(A\) satisfies \(A\bmod h=GC\) and \(|\det A|\leq\tau\), then two of the labels of \(C\) coincide. For three independent uniform labels this has probability at most \(3r^{-d}\).

*Proof.* \(\det(GC)=\det C\) in \(R_h\), and \(\det A\) represents it. Each of the three pairs of labels coincides with probability \(r^{-d}\). \(\square\)

So a small determinant needs a coincidence of labels. The rest of the course shows that, given a coincidence, a small determinant is still unlikely enough, and that the sampled columns are spread out enough for the lattice counts of the second lesson.

## 4. Exercises

**4.1.** For \(r=3\) and \(d=1\) (so \(K=\mathbb F_3\), \(\operatorname{Nm}=\mathrm{id}\)), write \(\mathcal N\) for the basis \(\beta_1=1\) and check Lemma 2.2: how many terms does (2.2) need?

**4.2.** Why must \(r\) be odd in the proof of Lemma 2.2, and why must \(d\) be odd in Lemma 2.1(c)?

**4.3.** For \(T=3\), list the positions (3.3) and check Lemma 3.1 directly.

**4.4.** Show that without the requirement \(c_{iv}\geq1\) the entries of \(c\) need not be units of \(R_h\), and point out where the proof of Lemma 3.2 would still work and where later lessons need units.

**4.5.** Show that if two columns of \(C\) are equal, then \(\det C=0\) in \(R_h\). Why does the construction draw new digits for every column, even for columns with the same label?

## 5. Solutions

**4.1.** With \(d=1\), \(Z(X)=(X_{11},X_{21},X_{31})\) and \(\mathcal N=\mathcal D\) is the determinant of the \(3\times3\) matrix of variables. The monomials of degree one are the three variables (\(M=3\), \(T=1\)), and (2.2) has the single term \(a=0\) with \((f_{10},f_{20},f_{30})=(X_{11},X_{21},X_{31})\): \(\mathcal N=\det(X^{(j)}_{i1})\).

**4.2.** Coefficients with a repeated monomial satisfy \(c=-c\), which forces \(c=0\) only when \(2\) is invertible. If \(d\) were even, exchanging two groups would multiply \(\mathcal N\) by \((-1)^d=1\), and \(\mathcal N\) would be symmetric, not alternating.

**4.3.** \(i_a=0,1,2\), \(j_a=0,3,6\), \(\ell_a=9,5,1\), and \(k-1=9\). The sums \(i_a+j_a+\ell_a\) are \(9,9,9\). For \(a'\neq a\) or \(a''\neq a\): e.g. \(i_0+j_1+\ell_2=0+3+1=4\neq9\); in general \(a+3a'=4a''\) forces \(a=a''\) modulo \(3\).

**4.4.** A column whose digits at position \(0\) are all divisible by \(B\) would have entries divisible by \(B\). Lemma 3.2 uses only the digit bounds and residues; the unit property is used in the fourth lesson, where a unit entry starts the diagonal form of a residue matrix.

**4.5.** A matrix with two equal columns has determinant zero over any commutative ring, and \(0\in[-\tau,\tau]\). With the same label, two columns get the same prescribed residues, but independent digits make them equal only with probability \((r/L)^{3k}\); the fourth lesson uses exactly this independence to show that a repeated label rarely makes the residue matrix very singular.

## References

- [OpenAI-H] OpenAI, *A power improvement in the Heilbronn triangle lower bound*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026
- [Judson] T. W. Judson, *Abstract Algebra: Theory and Applications*, online edition; the text of the core courses Abstract Algebra I and II. https://judsonbooks.org/aata-files/aata-html/
- R. Salem and D. C. Spencer (1942) and F. A. Behrend (1946) controlled carries in large bases in their constructions of progression-free sets; R. Lidl and H. Niederreiter's book on finite fields is a reference for the background. They are named for credit; the course does not use their results.
