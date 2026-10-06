# Heights of algebraic numbers

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol at Ultra. Public domain (CC0).*

A small complex absolute value need not mean a small algebraic number. Another conjugate may be large, or a denominator may carry the arithmetic complexity. The absolute logarithmic Weil height sees all these contributions at once. It converts the integer obstruction of Algebraic and transcendental numbers; Liouville's theorem into a lower bound at every place of a number field.

We start with a norm bound, build a bridge between polynomial coefficients and local absolute values, and then prove the height inequalities and the theorems of Northcott and Kronecker. The exact arithmetic prerequisite is the lesson *Places of number fields in extensions and the product formula* in *Local fields*. Its required statements and normalization are given in Section 3. Its proof belongs to that course. This lesson proves the height results that use it.

Basic references are Waldschmidt's *Linear Independence of Logarithms of Algebraic Numbers*, Chapter 3, Evertse's lecture notes *Diophantine Approximation*, Chapter 3, and the paper of Cantor and Straus on Lehmer's problem. Their roles are local heights, Mahler measure and Liouville's inequality; coefficient heights and the house; and the determinant bound of Section 7.

## 1. The elementary norm obstruction

An **algebraic integer** is a root of a monic polynomial in \(\mathbb Z[X]\). We use the opening lesson *Algebraic integers and rings of integers* in *Number fields*: Proposition 1.1 identifies these numbers with those having monic integral minimal polynomial and proves that they form an integrally closed ring; Proposition 1.2 identifies the field norm with the product of conjugates and proves that the norm of an algebraic integer is integral. In particular, a rational algebraic integer is an ordinary integer. These statements apply in every number field, and hence in a finite field containing any specified finite collection of algebraic numbers.

For an algebraic number \(\gamma\), let

\[
 \operatorname{house}(\gamma)=\max_\sigma|\sigma(\gamma)|,
\]

where \(\sigma\) ranges over the embeddings of \(\mathbb Q(\gamma)\) into \(\mathbb C\). The **denominator** \(\operatorname{den}(\gamma)\) is the least positive integer \(\delta\) for which \(\delta\gamma\) is an algebraic integer. It exists: if \(P_\gamma\) has leading coefficient \(a_d\), then \(a_d\gamma\) satisfies the monic integer polynomial \(a_d^{d-1}P_\gamma(Y/a_d)\).

### Lemma 2.1. A bound from the norm

Suppose \(\gamma\neq0\) has degree \(D\), and \(\delta\gamma\) is an algebraic integer. For every embedding \(\sigma\),

\[
 |\sigma(\gamma)|\geq
 \delta^{-D}\operatorname{house}(\gamma)^{-(D-1)}.
\]

**Proof.** The product of the \(D\) conjugates of \(\delta\gamma\) is a nonzero rational integer, up to sign the constant coefficient of its monic minimal polynomial. Its absolute value is at least one. Bounding the other \(D-1\) conjugates by the house gives

\[
 1\leq\delta^D\prod_\tau|\tau(\gamma)|
 \leq\delta^D|\sigma(\gamma)|\operatorname{house}(\gamma)^{D-1}.
\]

Rearrange. \(\square\)

The estimate uses a single maximum for all the other conjugates. Heights keep their individual contributions and also measure denominators.

## 2. Measuring a polynomial on the unit circle

For a nonzero complex polynomial

\[
 P(X)=a_d\prod_{j=1}^d(X-\alpha_j)=\sum_{k=0}^d a_kX^k,
\]

define

\[
 H(P)=\max_k|a_k|,\qquad L(P)=\sum_k|a_k|,\qquad
 M(P)=|a_d|\prod_{j=1}^d\max(1,|\alpha_j|).
\]

These are the coefficient **height**, **length**, and **Mahler measure**. Roots are counted with multiplicity. For a nonzero constant, \(M(P)=|P|\). Factorization gives \(M(PQ)=M(P)M(Q)\).

### Proposition 2.2. The coefficient and circle bounds

For \(0\leq k\leq d\),

\[
 |a_k|\leq\binom dkM(P),\qquad
 M(P)\leq\left(\sum_{k=0}^d|a_k|^2\right)^{1/2}.
\]

In particular,

\[
 2^{-d}H(P)\leq M(P)\leq\sqrt{d+1}\,H(P).
\]

**Proof.** Express \(a_k\) as \(a_d\) times an elementary symmetric sum of \(d-k\) roots. There are \(\binom dk\) products, each bounded by \(\prod_j\max(1,|\alpha_j|)\). This proves the first inequality. Its consequence follows from \(\binom dk\leq2^d\).

The analytic bridge is the circle-mean identity

\[
 \frac1{2\pi}\int_0^{2\pi}\log|e^{it}-a|\,dt
 =\log\max(1,|a|).
\]

For \(|a|<1\), the power series for \(\log(1-ae^{-it})\) converges uniformly, and each nonconstant Fourier term has mean zero. Integrate its real part. For \(|a|>1\), factor out \(a\) and use the first case with \(1/a\). For \(|a|=1\), rotate to \(a=1\) and take radial limits. Away from zero these limits are uniform. Near zero, for \(1/2\leq r<1\), the identity

\[
 |e^{it}-r|^2=(1-r)^2+2r(1-\cos t)
\]

bounds the negative logarithm by \(C+|\log|t||\); the positive logarithm is bounded by \(\log2\). Dominated convergence therefore applies, because \(|\log|t||\) is integrable near zero.

Sum the circle-mean identities over the roots. They give

\[
 \log M(P)=\frac1{2\pi}\int_0^{2\pi}\log|P(e^{it})|\,dt.
\]

Concavity of \(\log\), followed by orthogonality of \(e^{ikt}\), yields

\[
 \log M(P)\leq\frac12\log\left(
 \frac1{2\pi}\int_0^{2\pi}|P(e^{it})|^2\,dt\right)
 =\frac12\log\sum_{k=0}^d|a_k|^2.
\]

If \(P\) has a root on the circle, first apply concavity to \(|P|^2+\varepsilon\) and let \(\varepsilon\downarrow0\). The root factorization shows that the logarithmic singularities are integrable. Exponentiation proves Landau's inequality. Finally, \(\sum|a_k|^2\leq(d+1)H(P)^2\). \(\square\)

*Reference:* Waldschmidt, Chapter 3, formula (3.8) and Lemma 3.11, for Mahler measure and coefficient comparisons.

## 3. The arithmetic normalization and the Weil height

Let \(K\) be a number field, \(D=[K:\mathbb Q]\). We use absolute values extending those of \(\mathbb Q\). At a finite place over \(p\), \(|p|_v=p^{-1}\). At a real place use the usual absolute value; at a complex place use the usual modulus, without squaring it. Write

\[
 d_v=[K_v:\mathbb Q_v].
\]

The degree is one at a real place and two at a complex place. A sum over places has one term for each complex-conjugate pair, with weight two.

The precise inputs from the *Local fields* lesson *Places of number fields in extensions and the product formula* are the following. For a finite extension \(L/K\) and every place \(v\),

\[
 L\otimes_K K_v\simeq\prod_{w\mid v}L_w,\qquad
 \sum_{w\mid v}[L_w:K_v]=[L:K].
\]

Factoring a primitive element's minimal polynomial over \(K_v\) identifies the factors with these completions. In particular, for \(K=\mathbb Q(\alpha)\), its roots in \(\overline{\mathbb Q}_p\) account for each place above \(p\) with multiplicity \(d_v\). The archimedean analogue counts real embeddings individually and complex embeddings in pairs. The product formula, in our normalization, is

\[
 \sum_v d_v\log|\alpha|_v=0\qquad(\alpha\in K^\times).
\]

Here only finitely many terms are nonzero. The internal lesson's fully weighted normalization is \(\|\alpha\|_v=|\alpha|_v^{d_v}\): at a finite prime ideal \(\mathfrak p\), it is \(N\mathfrak p^{-v_{\mathfrak p}(\alpha)}\), and at a complex place it is the squared modulus. Thus its unweighted product \(\prod_v\|\alpha\|_v=1\) is exactly the formula above. This conversion, together with the extension-of-absolute-values theorem in *Extensions of complete valued fields* in the same course, supplies the normalization used here.

For \(\mathbb Q\), the product formula itself follows immediately from prime factorization: \(\log|a/b|=\sum_p(v_p(a)-v_p(b))\log p\), cancelling the finite-place terms.

### Definition 2.3. Absolute logarithmic Weil height

For \(\alpha\in K\), set

\[
 h(\alpha)=\frac1D\sum_v d_v\log\max(1,|\alpha|_v).
\]

The sum is finite and nonnegative. In particular, \(h(0)=0\).

### Theorem 2.4. Independence of field and the polynomial formula

The height is independent of the number field containing \(\alpha\). If \(\alpha\) has degree \(d\) and primitive minimal polynomial \(P_\alpha\), then

\[
 h(\alpha)=\frac1d\log M(P_\alpha).
\]

**Proof.** In an extension \(L/K\), the absolute values agree on \(K\), and the local-degree identity gives

\[
 \sum_{w\mid v}[L_w:\mathbb Q_v]\log\max(1,|\alpha|_w)
 =[L:K]d_v\log\max(1,|\alpha|_v).
\]

Divide by \([L:\mathbb Q]=[L:K]D\). The height is unchanged. Two arbitrary containing fields can both be compared with their compositum.

Take \(K=\mathbb Q(\alpha)\), write \(P_\alpha=a_d\prod_i(X-\alpha_i)\), and count the embeddings at infinity. Their total contribution is \(\log M(P_\alpha)-\log a_d\). We must recover \(\log a_d\) from the finite places.

Over a nonarchimedean valued field the Gauss norm \(\|\sum b_kX^k\|=\max_k|b_k|\) is multiplicative. To prove this, divide each polynomial by a coefficient of maximal modulus. Its coefficients then belong to the valuation ring and its reduction in the residue field is nonzero. The product of the reductions is nonzero, so the product has norm one. Undo the rescaling.

Fix a rational prime \(p\), and factor \(P_\alpha\) in a finite extension of \(\mathbb Q_p\) containing all its roots. Its integer coefficients have maximum \(p\)-adic modulus one, because they are primitive. Multiplicativity gives

\[
 1=|a_d|_p\prod_i\max(1,|\alpha_i|_p).
\]

The root-place correspondence therefore gives

\[
 \sum_{v\mid p}d_v\log\max(1,|\alpha|_v)=-\log|a_d|_p.
\]

Summing over \(p\) produces \(\log a_d\) by prime factorization. Add this to the infinite contribution and divide by \(d\). For \(\alpha=0\), its polynomial is \(X\) and \(M(X)=1\), so the same conclusion holds. \(\square\)

If \(p,q\) are coprime integers, \(q>0\), the primitive polynomial \(qX-p\) gives

\[
 h(p/q)=\log\max(|p|,q).
\]

For a nonzero rational the finite contribution is \(\log q\), while the infinite contribution is \(\log\max(1,|p|/q)\). This explains directly why height measures denominators.

## 4. Height arithmetic and finite sets

### Proposition 2.5. Sums, products, powers and conjugates

For algebraic numbers \(\alpha_1,\ldots,\alpha_n\),

\[
 h(\alpha_1\cdots\alpha_n)\leq\sum_i h(\alpha_i),\qquad
 h(\alpha_1+\cdots+\alpha_n)\leq\log n+\sum_i h(\alpha_i).
\]

For \(\alpha\neq0\), \(m\in\mathbb Z\), one has \(h(\alpha^m)=|m|h(\alpha)\). Conjugates have equal height.

**Proof.** Use one field containing all the numbers. At every place,

\[
 \max(1,|\alpha_1\cdots\alpha_n|_v)
 \leq\prod_i\max(1,|\alpha_i|_v).
\]

For sums the ultrametric inequality gives the same bound at finite places; the triangle inequality requires a factor \(n\) at infinite places. Take weighted logarithms and use \(\sum_{v\mid\infty}d_v=D\). This proves the inequalities. Nonnegative powers follow directly from the definition. For inverses, \(\log\max(1,t^{-1})=\log\max(1,t)-\log t\), and the product formula gives \(h(\alpha^{-1})=h(\alpha)\). Conjugates have the same primitive minimal polynomial, so Theorem 2.4 proves their height equality. \(\square\)

The term \(\log n\) cannot generally be removed: \(h(1)=0\), but \(h(1+1)=\log2\).

### Theorem 2.6. Northcott's finite box

For \(D\geq1\) integral and \(X\geq0\), the number of algebraic numbers of degree at most \(D\) and height at most \(X\) is at most

\[
 D^2(2^{D+1}e^{DX}+1)^{D+1}.
\]

**Proof.** For degree \(d\leq D\), Proposition 2.2 and Theorem 2.4 imply \(H(P_\alpha)\leq2^de^{dh(\alpha)}\leq2^De^{DX}=:B\). A polynomial of degree \(d\) with integer coefficients in \([-B,B]\) has at most \((2\lfloor B\rfloor+1)^{d+1}\) possible coefficient tuples, and at most \(d\) roots. With \(C=2^{D+1}e^{DX}+1\), the total number is bounded by \(\sum_{d=1}^D dC^{d+1}\leq D(D+1)C^{D+1}/2\leq D^2C^{D+1}\). Counting reducible and nonprimitive polynomials only increases this upper bound. \(\square\)

### Theorem 2.7. Kronecker's theorem

A nonzero algebraic number has height zero if and only if it is a root of unity. An algebraic integer whose conjugates all lie in the closed unit disc is zero or a root of unity.

**Proof.** If a positive power is one, Proposition 2.5 forces height zero. Conversely, \(h(\alpha)=0\) gives \(M(P_\alpha)=1\). Its positive integer leading coefficient is one and all roots have modulus at most one. Every positive power of \(\alpha\) is again an algebraic integer, of degree at most \(d=\deg\alpha\), with all conjugates in the unit disc. Its monic minimal polynomial has integer coefficients bounded by \(2^d\), by elementary symmetric sums. Only finitely many such polynomials, and therefore only finitely many such roots, exist. Two positive powers are equal. Cancel the lower power, since \(\alpha\neq0\), to obtain a root of unity. The second assertion follows from the same bounded-powers argument, allowing zero separately. \(\square\)

Integrality matters. The number \(\alpha=(3+4i)/5\) has two conjugates of modulus one, but its primitive polynomial is \(5X^2-6X+5\), its Mahler measure is five and \(h(\alpha)=\tfrac12\log5\). The monic minimal polynomial has nonintegral coefficients. The denominator prevents this number from having height zero.

## 5. A lower bound at every place

### Theorem 2.8. Liouville's inequality

Let \([K:\mathbb Q]=D\). For \(\eta\in K^\times\) and every place \(v\),

\[
 d_v\log|\eta|_v\geq-Dh(\eta).
\]

If \(f\in\mathbb Z[X_1,\ldots,X_t]\) is nonzero and \(\gamma_i\in K\), then, with \(e_i=\deg_{X_i}f\),

\[
 h(f(\gamma))\leq\log L(f)+\sum_i e_i h(\gamma_i).
\]

If additionally \(f(\gamma)\neq0\), then

\[
 d_v\log|f(\gamma)|_v\geq
 -D\left(\log L(f)+\sum_i e_i h(\gamma_i)\right).
\]

**Proof.** The nonnegative sum defining \(Dh(\eta^{-1})\) bounds each summand. Hence \(-d_v\log|\eta|_v\leq d_v\log\max(1,|\eta^{-1}|_v)\leq Dh(\eta)\).

At a finite place each integer coefficient has modulus at most one, and the ultrametric inequality bounds \(\max(1,|f(\gamma)|_v)\) by \(\prod_i\max(1,|\gamma_i|_v)^{e_i}\). At an infinite place, sum the coefficient moduli to obtain the same bound multiplied by \(L(f)\geq1\). Weighted logarithmic summation gives the height bound. Apply the first inequality to the nonzero value and insert its height bound. \(\square\)

*Reference:* Waldschmidt, Chapter 3, inequality (3.13) and Lemma 3.14. The nonzero-value condition in the last statement is essential.

At a specified complex embedding the local weight is one or two. Thus \(\log|\sigma(\eta)|\geq-Dh(\eta)/d_v\), and the weaker bound \(\log|\sigma(\eta)|\geq-Dh(\eta)\) is always valid. Distinguishing these normalizations prevents a factor two from being lost in determinant estimates.

For example, let \(\gamma=\sqrt[3]2\) and \(f(X)=qX-p\), with \(p,q\in\mathbb Z\), \(q\neq0\). At the real embedding of \(\mathbb Q(\gamma)\), the theorem gives

\[
 \log|q\gamma-p|\geq-3\log(|p|+|q|)-\log2.
\]

This is coarser than a specialized rational-approximation bound, but the same method applies to multivariable polynomials and all places.

## 6. Converting conventions without losing a degree

Put \(d=\deg\alpha\), \(H=H(P_\alpha)\), \(R=\operatorname{house}(\alpha)\), and \(\delta=\operatorname{den}(\alpha)\). Our formulas give

\[
 H\leq2^de^{dh(\alpha)},\qquad
 dh(\alpha)\leq\log H+\tfrac12\log(d+1),\qquad
 L(P_\alpha)\leq(d+1)H.
\]

Also,

\[
 \log\max(1,R)\leq dh(\alpha),\quad
 \log\delta\leq dh(\alpha),\quad
 h(\alpha)\leq\log\delta+\log\max(1,R).
\]

For the first two bounds, each root factor and the leading coefficient are at most \(M(P_\alpha)\), and \(\delta\leq a_d\). For the last, a monic integral relation implies \(|\delta\alpha|_v\leq1\) at every finite place: otherwise its highest power strictly dominates all other terms. Thus the finite contribution to \(h(\alpha)\) is at most \(\log\delta\), by the product formula for the rational integer \(\delta\). The infinite contribution is at most \(\log\max(1,R)\).

| Source convention | Quantity | Conversion used here |
|---|---|---|
| Evertse's height of a number | Primitive coefficient height \(H\) | \(\log H\leq d(h+\log2)\) |
| Evertse's house of a number | House \(R\) | \(\log\max(1,R)\leq dh\); retain the denominator separately |
| Waldschmidt's polynomial height and length | \(H(P),L(P)\) | \(H(P)\leq L(P)\leq(d+1)H(P)\) |
| Waldschmidt's logarithmic height | Absolute Weil height \(h\) | \(M(P_\alpha)=e^{dh}\) |

These comparisons are bounds, not equalities between the conventions. An exponential in a coefficient height can have a quite different appearance after the degree enters the conversion.

For example, \(M(P_\alpha)\leq\|P_\alpha\|_2\leq L(P_\alpha)\) gives \(h(\alpha)\leq\log L(P_\alpha)/\deg\alpha\). Substituting this in Theorem 2.8, for \(K=\mathbb Q(\gamma_1,\ldots,\gamma_t)\), yields the following length form:

\[
 |f(\gamma)|\geq L(f)^{-[K:\mathbb Q]}
 \prod_i L(P_{\gamma_i})^{-e_i[K:\mathbb Q(\gamma_i)]}
 \qquad(f(\gamma)\neq0).
\]

Indeed, \([K:\mathbb Q]/\deg\gamma_i=[K:\mathbb Q(\gamma_i)]\). At a complex place we use the weaker unweighted embedding bound from Section 5. Thus the coefficient-length version follows from the placewise height statement with every degree factor accounted for.

### Examples

For \(\sqrt2\), the polynomial \(X^2-2\) has \(H=2\), house \(\sqrt2\), denominator one, and Mahler measure two; hence \(h=\tfrac12\log2\). For \(\varphi=(1+\sqrt5)/2\), the polynomial \(X^2-X-1\) has coefficient height one. Its roots are \(\varphi\) and \(-1/\varphi\), so its house and Mahler measure are \(\varphi\), and \(h(\varphi)=\tfrac12\log\varphi\). Small integer coefficients therefore do not force height zero.

For \(\alpha=2^{1/n}\), \(X^n-2\) is irreducible. Here is the argument needed for this family. A factorization into monic rational polynomials would have integral coefficients: their coefficients are symmetric sums of subsets of the integral roots, hence rational algebraic integers. Reducing modulo two, both positive-degree factors of \(X^n-2\) must be powers of \(X\). Their constant coefficients would both be even, whereas their product is \(-2\), a contradiction. Thus the degree is \(n\). All conjugates have modulus \(2^{1/n}\), so \(M=2\) and

\[
 h(2^{1/n})=\frac{\log2}{n}.
\]

For \(\sqrt[3]2\), the four sizes are \(H=2\), \(L=3\), \(R=2^{1/3}\), and \(h=\log2/3\). The denominator is one. In contrast, for \((3+4i)/5\), they are \(H=6\), \(L=16\), \(R=1\), and \(h=\tfrac12\log5\). Its denominator is five: this value works, and integrality of the trace \(6\delta/5\) forces \(5\mid\delta\). These examples check both the degree factor and the information that the house omits.

## 7. Lehmer's problem and the determinant bound

Kronecker separates measure one from measure greater than one. It does not give a separation uniform in the degree. **Lehmer's problem** asks whether there is an absolute \(c>1\) such that every nonzero algebraic integer that is not a root of unity has Mahler measure at least \(c\). We do not assume an answer. The polynomial

\[
 P(X)=X^{10}+X^9-X^7-X^6-X^5-X^4-X^3+X+1
\]

illustrates the difficulty. To check its measure, put \(Y=X+X^{-1}\). Direct expansion gives

\[
 X^{-5}P(X)=R(Y),\qquad
 R(Y)=Y^5+Y^4-5Y^3-5Y^2+4Y+3.
\]

The signs at \(-2,-3/2,-1,0,1,2,21/10\) show one root in each of \((-2,-3/2)\), \((-3/2,-1)\), \((-1,0)\), \((0,1)\), and \((2,21/10)\). These exhaust its five roots. The first four yield eight roots of \(P\) on the unit circle; the last yields \(\lambda>1\) and \(\lambda^{-1}\). Hence \(M(P)=\lambda\). Numerical bisection of the last root and the formula \(\lambda=(Y+\sqrt{Y^2-4})/2\) give \(M(P)\approx1.176280818\).

The polynomial is irreducible as well. Modulo two, \(R\) is \(Y^5+Y^4+Y^3+Y^2+1\). It has no linear factor, and division by the only irreducible quadratic \(Y^2+Y+1\) leaves remainder \(Y\). A reducible polynomial of degree five without a linear factor must have a quadratic factor, so this reduction is irreducible. It follows that \([\mathbb Q(Y):\mathbb Q]=5\). If \(\lambda\) had degree five, it would lie in \(\mathbb Q(Y)\). Every embedding of that field is real because all five conjugates of \(Y\) are real. But at a conjugate in \((-2,2)\), the equation \(\lambda^2-Y\lambda+1=0\) has no real root. Therefore \(\lambda\) has degree ten, proving the assertion.

Dobrowolski's theorem gives a lower bound that tends to one very slowly. The proof explains why primes and repeated columns improve the simple integer obstruction. Its analytic input is the lesson *The prime number theorem* in *The Riemann zeta function*, which proves \(p_j\sim j\log j\) for the \(j\)-th prime. We use that result only in this section. All determinant and arithmetic arguments are supplied here.

### Lemma 2.9. Removing quotients that are roots of unity

If a nonzero algebraic integer \(\alpha\) of degree \(d\) has distinct conjugates with a root-of-unity quotient, there is an algebraic integer \(\beta\) of degree less than \(d\), with \(M(\beta)=M(\alpha)\), whose distinct conjugates have no such quotient.

**Proof.** In a splitting field, partition the conjugates into classes under the relation that their quotient is a root of unity. The Galois group acts transitively on conjugates and permutes the classes, so all classes have the same size \(r>1\). For each class take its product \(\beta_j\). These products are integral and form one Galois orbit. Writing a representative as \(\alpha_j\), we have \(\beta_j=\zeta_j\alpha_j^r\), with \(\zeta_j\) a root of unity. If two products had a root-of-unity quotient, then \((\alpha_j/\alpha_k)^r\), and hence \(\alpha_j/\alpha_k\), would be a root of unity. This contradicts their belonging to distinct classes. Thus the products are distinct, and any one has degree \(d/r\). All elements in a class have the same modulus, so

\[
 \prod_j\max(1,|\beta_j|)
 =\prod_i\max(1,|\alpha_i|)=M(\alpha).
\]

This proves the lemma. The Galois fact used here is the elementary splitting-field theorem from the algebra prerequisite: embeddings of a simple separable extension extend to the splitting field by successively choosing roots of the transported minimal polynomials. Since the field contains all these roots, the resulting embeddings are automorphisms; they can send any conjugate to any other. \(\square\)

### Lemma 2.10. Prime divisibility

Suppose distinct conjugates of a nonzero algebraic integer \(\alpha\) have no root-of-unity quotient, and \(\alpha\) is not a root of unity. For every prime \(p\),

\[
 \left|\prod_{i,j=1}^d(\alpha_i^p-\alpha_j)\right|\geq p^d.
\]

**Proof.** Let \(f(X)=\prod_i(X-\alpha_i)\), and let \(f_p(X)=\prod_i(X-\alpha_i^p)\). The latter is monic integral: its coefficients are integral symmetric expressions invariant under the Galois group, hence rational integers. Moreover \(f_p\equiv f\pmod p\). For completeness, if \(e_k\) is the \(k\)-th elementary symmetric polynomial, then \(e_k(X_1^p,\ldots,X_d^p)-e_k(X_1,\ldots,X_d)^p\) has all coefficients divisible by \(p\), by the multinomial theorem. Dividing by \(p\) gives an integral symmetric polynomial. Such a polynomial is an integer polynomial in the elementary symmetric polynomials: subtract the corresponding product of the \(e_k\)'s to cancel its largest monomial in lexicographic order, then repeat; the leading exponent tuple of a symmetric polynomial is decreasing, so this procedure terminates. Evaluate at the conjugates, and use \(a^p\equiv a\pmod p\) for integers \(a\). This proves the congruence.

Consequently \(f_p(\alpha)=p\gamma\) for an algebraic integer \(\gamma\). It is nonzero. Indeed, an equality \(\alpha_i^p=\alpha_j\) would give \(p h(\alpha)=h(\alpha)\), contradicting \(h(\alpha)>0\) from Kronecker. Its norm is therefore a nonzero integer divisible by \(p^d\), and its absolute value is the displayed product. \(\square\)

### Lemma 2.11. A determinant with repeated nodes

Given distinct complex nodes \(v_1,\ldots,v_k\), positive multiplicities \(m_1,\ldots,m_k\), and \(N=\sum m_i\), form a matrix whose block at \(v_i\) has columns indexed by \(0\leq r<m_i\), with entries indexed by \(0\leq n<N\):

\[
 W_{n,(i,r)}=\binom nr v_i^{n-r},
\]

where entries with \(n<r\) are zero. Then

\[
 |\det W|=\prod_{i<j}|v_i-v_j|^{m_im_j}.
\]

A column indexed by \(r\) has squared Euclidean norm at most

\[
 N^{2r+1}\max(1,|v_i|)^{2N}.
\]

**Proof.** For all multiplicities one, the determinant is the Vandermonde product: it vanishes when two nodes agree, has exactly the sum of the degrees of the pairwise factors, and comparison of the diagonal monomial fixes its coefficient as one. For a larger multiplicity, split the block of size \(m\) into a block of size \(m-1\) at \(v\) and a single column at \(v+t\). Subtract the first \(m-1\) terms in the Taylor expansion of that column. Divide the determinant by \(t^{m-1}\) and let \(t\to0\). Its new column tends to the column with entries \(\binom n{m-1}v^{n-m+1}\). The Vandermonde product has the same limit and the stated cross-node exponents. Induction on the number of blocks proves the formula. For the norm bound, each entry is at most \(N^r\max(1,|v_i|)^N\), and there are \(N\) entries. \(\square\)

We also use Hadamard's inequality: the squared modulus of a determinant is at most the product of the squared column norms. Gram–Schmidt proves it directly: subtraction of previous orthogonal projections preserves the determinant and can only decrease each column length; the orthogonal columns have determinant modulus equal to the product of their lengths. A dependent matrix has determinant zero, so is included.

### Theorem 2.12. Dobrowolski's lower bound

For every \(\varepsilon>0\), there is \(d_0(\varepsilon)\) such that every nonzero algebraic integer \(\alpha\) of degree \(d\geq d_0(\varepsilon)\), not a root of unity, satisfies

\[
 M(\alpha)>1+(2-\varepsilon)
 \left(\frac{\log\log d}{\log d}\right)^3.
\]

**Proof.** It suffices to consider \(0<\varepsilon<2\). First assume that distinct conjugates have no root-of-unity quotient. Take the nodes \(\alpha_i\) with multiplicity \(S\), and the nodes \(\alpha_i^{p_j}\), for the first \(T\) primes, with multiplicity one. All nodes are distinct: within a prime power this follows from the quotient condition; between powers with different exponents it follows from their unequal heights \(p_jh(\alpha)\). Put \(N=d(S+T)\), and let \(V\) be the determinant in Lemma 2.11.

The columns at \(\alpha_i\), summed over their derivative orders, contribute at most \(N^{dS^2}M(\alpha)^{2NS}\) to the product of squared norms. The remaining columns contribute at most \(N^{dT}M(\alpha)^{2N\sum_{j\leq T}p_j}\). Hadamard therefore gives

\[
 |V|^2\leq N^{d(S^2+T)}
 M(\alpha)^{2N(S+\sum_{j\leq T}p_j)}.
\]

On the other hand the squared Vandermonde formula contains the original discriminant to power \(S^2\), the discriminant of the polynomial with all roots \(\alpha_i^{p_j}\), and the cross products between the original roots and each prime-power set to power \(2S\). The first two discriminants are nonzero integers: their monic polynomials have integral coefficients and their roots are distinct. Their absolute values are at least one. Lemma 2.10 bounds the remaining factors, giving

\[
 |V|^2\geq\prod_{j\leq T}p_j^{2Sd}.
\]

Thus

\[
 \log M(\alpha)\geq
 \frac{2S\sum_{j\leq T}\log p_j-(S^2+T)\log(d(S+T))}
 {2(S+T)(S+\sum_{j\leq T}p_j)}. \tag{*}
\]

The internal prime number theorem input gives

\[
 \sum_{j\leq T}p_j=\tfrac12T^2\log T\,(1+o(1)),\qquad
 \sum_{j\leq T}\log p_j=T\log T\,(1+o(1)).
\]

Here are the summation details. From \(p_j\sim j\log j\), the first sum differs by a relative \(o(1)\) from \(\sum j\log j\); comparison with its integral gives \(\tfrac12T^2\log T+O(T^2)\). For the second, \(\log p_j=\log j+O(\log\log j)\) for all large \(j\), and integral comparison gives \(\sum\log j=T\log T+O(T)\). Finite initial terms do not change either asymptotic.

Write \(u=\log d\), \(\ell=\log\log d\), choose \(S=\lceil u/\ell\rceil\), and \(T=\lfloor S^2/2\rfloor\). Then

\[
 \log T=2\ell(1+o(1)),\quad
 \log(d(S+T))=u(1+o(1)),\quad
 S+T=\frac{u^2}{2\ell^2}(1+o(1)).
\]

The numerator in (*) is \(\tfrac12u^3\ell^{-2}(1+o(1))\), and its denominator is \(\tfrac14u^6\ell^{-5}(1+o(1))\). The errors depend only on \(d\), not on \(\alpha\). Consequently

\[
 \log M(\alpha)\geq(2+o(1))(\ell/u)^3.
\]

Now allow root-of-unity quotients. Lemma 2.9 replaces \(\alpha\) by a number \(\beta\) of degree \(e\leq d\) and the same measure, with no such quotients. For all sufficiently large \(e\), the just-proved estimate holds uniformly with coefficient \(2-\varepsilon/2\). The function \((\log\log x/\log x)^3\) is positive and decreasing for \(x>e^e\), by differentiation. Thus that estimate at degree \(e\) implies the required bound at degree \(d\).

For the finitely many remaining degrees \(e\), there is a uniform positive lower bound on \(\log M(\beta)\) among nonroots of unity. Indeed, those with \(M\leq2\) have bounded degree and bounded height and form a finite set by Northcott; each has positive height by Kronecker. Those with \(M>2\) already have \(\log M>\log2\). Their common positive lower bound eventually exceeds \((2-\varepsilon/2)(\log\log d/\log d)^3\). This handles every degree reduction. Finally \(e^x>1+x\) for \(x>0\), and the margin \(\varepsilon/2\) gives the strict inequality stated in the theorem. \(\square\)

*Reference:* Dobrowolski's theorem, in the determinant form of Cantor and Straus, *On a conjecture of D. H. Lehmer*, §2, Lemmas 1–2 and the theorem. Since \(h=\log M/d\), the same argument gives \(h(\alpha)>(2-\varepsilon)d^{-1}(\log\log d/\log d)^3\) for all sufficiently large \(d\). It does not give a positive degree-independent lower bound on \(M\).

## 8. Exercises

1. **Easy — compare three sizes.** Compute \(h\), \(H\), and the house for \((1+\sqrt{-3})/2\), \(3/2\), and \(1+\sqrt2\). Check the two comparisons between \(H\) and \(M\).

2. **Easy — the archimedean cost of addition.** Prove \(h(\alpha+\beta)\leq\log2+h(\alpha)+h(\beta)\), and give a pair for which the \(\log2\) term cannot be removed.

3. **Medium — bounded powers.** Prove that an algebraic integer with all conjugates in the closed unit disc is zero or a root of unity, using coefficient bounds and powers rather than local heights.

4. **Medium — the circle estimate.** Deduce \(M(P)\leq\|P\|_2\) from the circle mean of \(\log|P|\), including roots on the unit circle.

5. **Medium — why degree matters.** Exhibit infinitely many distinct algebraic numbers of height at most \(\log2\), and explain precisely which hypothesis of Northcott prevents a contradiction.

6. **Hard — a difference from one.** For \(\alpha\neq1\) of degree \(d\), prove for every complex embedding \(\sigma\) that

\[
 \log|\sigma(\alpha)-1|\geq-d(\log2+h(\alpha)).
\]

Explain why the nonzero-value condition is needed, and why the bound is also valid at a complex place even though that place has weight two.

## 9. Solutions

**1.** The first number has polynomial \(X^2-X+1\); both roots have modulus one. Thus \(H=1\), house one, \(M=1\), and \(h=0\). For \(3/2\), the primitive polynomial is \(2X-3\); \(H=3\), house \(3/2\), \(M=3\), and \(h=\log3\). For \(1+\sqrt2\), the polynomial is \(X^2-2X-1\); its other root is \(1-\sqrt2\), of modulus less than one. Hence \(H=2\), house \(1+\sqrt2\), \(M=1+\sqrt2\), and \(h=\tfrac12\log(1+\sqrt2)\). The comparisons \(2^{-d}H\leq M\leq\sqrt{d+1}H\) become, respectively, \(1/4\leq1\leq\sqrt3\), \(3/2\leq3\leq3\sqrt2\), and \(1/2\leq1+\sqrt2\leq2\sqrt3\); each is true.

**2.** At finite places use \(|\alpha+\beta|_v\leq\max(|\alpha|_v,|\beta|_v)\); at infinite places insert a factor two. The weighted infinite degrees sum to the field degree, so the contribution of that factor is exactly \(\log2\). Take \(\alpha=\beta=1\): the separate heights are zero and the height of their sum is \(\log2\).

**3.** If \(\alpha=0\), there is nothing to prove. Otherwise each \(\alpha^n\) is integral of degree at most \(d\), with all conjugates in the unit disc. The coefficients of its monic minimal polynomial are bounded by the corresponding binomial coefficients, hence by \(2^d\). Only finitely many integer coefficient tuples occur, each supplying finitely many roots. Two positive powers of \(\alpha\) coincide. Division by the lower power proves that a positive power is one.

**4.** Root factorization and the circle-mean identity give \(\log M(P)=\frac1{2\pi}\int\log|P(e^{it})|\,dt\). Jensen's inequality for the concave logarithm, applied to \(|P(e^{it})|^2+\varepsilon\), bounds this mean by half the logarithm of its mean square plus \(\varepsilon\). The logarithmic singularities at the finitely many circle roots are integrable, as shown in Proposition 2.2; taking \(\varepsilon\downarrow0\) is valid. Orthogonality of the exponentials makes the mean square \(\sum|a_k|^2\). Exponentiate. This is the concavity step after the circle formula; no assumption of a zero-free unit circle is needed.

**5.** The positive numbers \(2^{1/n}\) are strictly decreasing and distinct, and their heights are \(\log2/n\). Their degrees are \(n\), by the irreducibility proof in Section 6. They meet a fixed height bound but not a fixed degree bound. Northcott requires both.

**6.** In \(K=\mathbb Q(\alpha)\), apply Theorem 2.8 to the nonzero value of \(f(X)=X-1\). Its length is two and degree one, so \(d_v\log|\alpha-1|_v\geq-d(\log2+h(\alpha))\). At the place corresponding to \(\sigma\), divide by \(d_v\), which is one or two. Since the right side is nonpositive, replacing \(1/d_v\) by one weakens the bound and gives the claimed inequality. If \(\alpha=1\), the left side is \(\log0\), and no finite lower bound exists.

## Prerequisite theorems

The opening lesson *Algebraic integers and rings of integers* in *Number fields* supplies the ring of algebraic integers, monic minimal polynomials, and the norm formula, as specified in Section 1. *Extensions of complete valued fields* and *Places of number fields in extensions and the product formula* in *Local fields* supply the local extension, local-degree and product-formula statements of Section 3. *The prime number theorem* in *The Riemann zeta function* supplies \(p_j\sim j\log j\) in Section 7. The required statements are specified at their points of use. The height inequalities, finiteness and zero-height theorems, placewise lower bounds and Dobrowolski's determinant argument are proved in this lesson.

## References

- **Waldschmidt.** Michel Waldschmidt, [*Linear Independence of Logarithms of Algebraic Numbers*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/LIL.pdf), IMSc Report 116, The Institute of Mathematical Sciences, Madras, 1992, Chapter 3: absolute values and the absolute logarithmic height, Mahler measure (formula (3.8) and Lemma 3.9), the usual height, house and denominator with their comparisons (Lemma 3.11), Liouville's inequality in height and length form ((3.13) and Lemma 3.14), and a survey of Lehmer's problem.
- **Cantor–Straus.** D. C. Cantor and E. G. Straus, [“On a conjecture of D. H. Lehmer”](https://matwbn.icm.edu.pl/ksiazki/aa/aa42/aa4219.pdf), *Acta Arithmetica* 42 (1982), 97–100: the confluent Vandermonde determinant, Hadamard's inequality and the constant \(2\) in Dobrowolski's bound.
- **Evertse.** J.-H. Evertse, [*Diophantine Approximation*, Chapter 3: Algebraic numbers and algebraic number fields](https://pub.math.leidenuniv.nl/~evertsejh/dio19-3.pdf), Leiden course notes: the height of an algebraic number as the largest coefficient of its primitive minimal polynomial, the house, and Siegel's lemma with coefficients measured by the house (Theorem 3.20).
- **Waldschmidt, IMPA notes.** M. Waldschmidt, *Diophantine approximation, irrationality and transcendence*, IMPA course notes, Course 3 (2010), §4.1, Lemma 24 and Proposition 26: Liouville's inequality for polynomial values in coefficient notation. [Course 3](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/IMPA2010Cours3.pdf).
- **Historical credit.** E. Dobrowolski, [“On a question of Lehmer and the number of irreducible factors of a polynomial”](https://matwbn.icm.edu.pl/ksiazki/aa/aa34/aa34411.pdf), *Acta Arithmetica* 34 (1979), 391–401. The determinant route and the improved asymptotic coefficient are those of Cantor and Straus, listed above.

- **Milne.** J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, July 19, 2020: Chapter 2 for algebraic integers and norms; Theorem 7.38 for finite separable extensions of complete discretely valued fields; Proposition 8.2 for decomposition into completions; Proposition 8.7 and Theorem 8.8 for the norm and product formulas. These are parallel treatments of the number-field prerequisites.
- **Sutherland.** Andrew V. Sutherland, [*Number Theory I*, Lecture 16](https://math.mit.edu/classes/18.785/2021fa/LectureNotes16.pdf), MIT, Fall 2021: Theorem 16.15 and its proof for the prime number theorem used in Section 7.
