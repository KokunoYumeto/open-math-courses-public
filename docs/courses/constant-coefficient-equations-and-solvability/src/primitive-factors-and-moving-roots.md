# Primitive factors and moving polynomial roots

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A polynomial factorization over rational functions must return to the original coefficient ring before it can describe a family of equations. We prove the content and unique-factorization arguments, obtain the exact denominator in a Bézout identity, and construct a holomorphic branch near each simple root.

[Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html), Section 2 and Sections 9.1–9.4, proves scalar division, Bézout and complex polynomial factorization. [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md) proves the uniform-limit lemma and persistent disk root counts used in the branch construction.

Zeff’s complex-analysis notes give the contour background, and Hörmander explains the role of polynomial approximation in equations. The factorization and local branch arguments are proved below.

## Primitive polynomials and unique factorization

An integral domain is a commutative ring with identity and no zero divisors. A unique factorization domain has a factorization of every nonzero nonunit into irreducibles, unique up to their order and multiplication by units. In such a domain every irreducible is prime: compare the irreducible factorizations of the two sides of \(ab=pc\). One factor on the left must be associated to \(p\), so \(p\mid a\) or \(p\mid b\). This includes zero factors by the domain property.

**Lemma 1.1 (content and the primitive product).** Let \(R\) be a unique factorization domain and \(K\) its fraction field. A nonzero \(f\in R[t]\) can be written \(f=c(f)f_0\), where \(f_0\) is primitive, meaning that no irreducible of \(R\) divides all its coefficients. The content \(c(f)\) is determined up to a unit. A product of primitive polynomials is primitive, and

\[
\begin{gathered}
c(fg)\ \text{is associated to}\ c(f)c(g)
\\
\quad(f,g\ne0).
\end{gathered}
\tag{1}
\]

**Proof.** For each irreducible \(p\), take the minimum of its factorization exponent among the nonzero coefficients of \(f\). Only finitely many \(p\)'s occur: each occurs in any one fixed nonzero coefficient. The product of these minimum powers is \(c(f)\); dividing all coefficients by it produces the required primitive polynomial. The same exponent rule proves uniqueness up to a unit.

If primitive \(f_0,g_0\) had a product all of whose coefficients were divisible by some irreducible \(p\), reduce modulo \(p\). Primality of \(p\) makes \(R/(p)\) a domain. The two reduced polynomials are nonzero, so their product is nonzero: its highest nonzero coefficient is a product of two nonzero coefficients. This is a contradiction. Extract the two contents and apply this primitive-product result to obtain (1). Constants, including units, are covered. The zero polynomial is excluded from the content assertion. \(\square\)

Every nonzero polynomial of \(K[t]\) has the form \(a h_0\), where \(a\in K^\times\) and \(h_0\in R[t]\) is primitive: first clear the finitely many coefficient denominators and then remove the content. We will need the following scalar observation. If \(h_0\) is primitive and \(a h_0\in R[t]\), write \(a=r/s\), with \(r,s\in R\setminus\{0\}\) having no common irreducible factor. Every coefficient satisfies \(s\mid r h_{0,j}\). Prime factor exponents imply that each prime power in \(s\) divides every \(h_{0,j}\). Since \(h_0\) is primitive, \(s\) is a unit and \(a\in R\). If \(a h_0\) is also primitive, (1) says that \(a\) is a unit of \(R\).

**Lemma 1.2 (Gauss's lemma, including divisibility).** A primitive positive-degree polynomial is irreducible in \(R[t]\) if and only if it is irreducible in \(K[t]\). If a primitive \(q\in R[t]\) divides \(f\in R[t]\) in \(K[t]\), it divides \(f\) in \(R[t]\).

**Proof.** Suppose a primitive \(f\) has a factorization \(f=uv\) with both factors of positive degree in \(K[t]\). Normalize them as \(u=a u_0,v=b v_0\), with \(u_0,v_0\) primitive in \(R[t]\). Their product is primitive, and \(f=ab(u_0v_0)\). The scalar observation makes \(ab\) a unit of \(R\). Thus \(f\) factors into positive-degree polynomials in \(R[t]\). Conversely a factorization in \(R[t]\) gives one in \(K[t]\), unless a factor becomes a scalar. Such a factor was already a constant in \(R\); if it were a nonunit it would divide every coefficient of \(f\), contrary to primitivity.

For the divisibility assertion, the case \(f=0\) is immediate. Otherwise write the \(K[t]\) quotient as \(a h_0\) with \(h_0\) primitive. Then \(f=a(qh_0)\), and \(qh_0\) is primitive. The scalar observation gives \(a\in R\), so the quotient belongs to \(R[t]\). \(\square\)

**Theorem 1.3 (the polynomial unique factorization theorem).** The ring \(R[t]\) is a unique factorization domain. In particular every \(\mathbb C[z_1,\ldots,z_d]\), including \(d=0\), is a unique factorization domain.

**Proof.** First consider a field \(K\). Univariate division and the Euclidean algorithm give Bézout's identity, with the zero and constant cases included in [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) Section 2. If \(q\in K[t]\) is irreducible and \(q\nmid f\), its gcd with \(f\) is 1; Bézout therefore shows that \(q\mid fg\) implies \(q\mid g\). Thus every irreducible is prime. Factorization exists by induction on degree: a positive-degree polynomial is either irreducible or a product of two smaller positive degrees. Nonzero constants are units. Prime cancellation gives uniqueness.

For general \(R\), factor the content of \(f\) in \(R\), and factor its primitive part \(f_0\) in \(K[t]\). Normalize each positive-degree factor to a primitive polynomial in \(R[t]\). The product of these normalized polynomials is primitive, so the remaining scalar is an \(R\)-unit by the scalar observation. Lemma 1.2 makes these factors irreducible in \(R[t]\). The irreducible constants are prime in \(R[t]\), since \(R[t]/(p)=(R/(p))[t]\) is a domain. A primitive positive-degree irreducible is prime as well: it is prime in \(K[t]\), and Lemma 1.2 brings the resulting divisibility back to \(R[t]\). These facts prove existence and uniqueness for \(f\), by prime cancellation. Units of \(R[t]\) are exactly units of \(R\), because degrees add in a domain. Starting with the field \(\mathbb C\) and adjoining one variable at a time proves the last assertion. \(\square\)

## Bézout over rational functions

Let \(w=(w_1,\ldots,w_d)\), \(R=\mathbb C[w]\) and \(K=\mathbb C(w)\); for \(d=0\), these are both \(\mathbb C\). Suppose \(r(w,t)\in R[t]\) is irreducible and monic of positive \(t\)-degree \(m\). Monicity makes it primitive, so Lemma 1.2 makes it irreducible in \(K[t]\). Characteristic zero gives a nonzero derivative \(r_t\) of degree \(m-1\), so irreducibility implies \(\gcd(r,r_t)=1\) in \(K[t]\). The exact scalar Bézout proof gives \(a r+b r_t=1\), for \(a,b\in K[t]\). Multiplying by one common nonzero denominator gives

\[
\begin{gathered}
A(w,t)r(w,t)\\
+B(w,t)r_t(w,t)=\Delta(w),
\\
\quad A,B\in\mathbb C[w,t],\\
\quad 0\ne\Delta\in\mathbb C[w].
\end{gathered}
\tag{2}
\]

Consequently, at each \(w\) with \(\Delta(w)\ne0\), every root of \(r(w,\cdot)\) is simple. Its degree is always \(m\), because its leading coefficient is 1. The full written fundamental theorem of algebra supplies its \(m\) roots counted with multiplicity. When \(m=1\), \(r_t=1\), and one may take \(A=0,B=1,\Delta=1\). A monic degree-zero polynomial is 1 and has no root; it is outside the stated irreducible positive-degree case.

This supplies precisely the algebra used in [the polynomial approximation lesson](choosing-polynomial-and-exponential-approximants.md) Lemma 4.1. 

## Constructing the holomorphic branch

**Theorem 3.1 (finite-dimensional holomorphic implicit functions).** Let \(F(z,w)\in\mathbb C^l\) be holomorphic near \((a,b)\in\mathbb C^k\times\mathbb C^l\), with \(F(a,b)=0\) and invertible \(A=\partial_wF(a,b)\). There are neighborhoods on which the solutions near \(b\) are exactly \(w=W(z)\), for one holomorphic \(W\) satisfying \(W(a)=b\). On these neighborhoods,

\[
\begin{gathered}
\partial_z W(z)\\
=-\big(\partial_wF(z,W(z))\big)^{-1}
\partial_zF(z,W(z)).
\end{gathered}
\tag{3}
\]

**Proof.** When \(l=0\) the unique empty vector is the asserted branch. Otherwise set \(T_z(w)=w-A^{-1}F(z,w)\). Its \(w\)-derivative is zero at \((a,b)\). Continuity of this derivative permits a closed Euclidean ball \(|w-b|\le r\) and a parameter neighborhood \(|z-a|<\delta\), with their product inside the domain, such that \(\|\partial_wT_z\|\le\lambda<1\). Shrink the parameter neighborhood so that \(|T_z(b)-b|\le(1-\lambda)r/2\). Integration along the straight \(w\)-segment gives

\[
\begin{gathered}
|T_z(w)-T_z(v)|\le\lambda|w-v|,
\\
\qquad |T_z(w)-b|\\
\le\lambda r+(1-\lambda)r/2<r.
\end{gathered}
\tag{4}
\]

Starting with \(w_0(z)=b\), define \(w_{j+1}(z)=T_z(w_j(z))\). All iterates remain inside the ball, are holomorphic, and their successive differences are bounded by \(\lambda^j(1-\lambda)r/2\). This summable bound proves uniform convergence in the entire chosen parameter neighborhood to a limit \(W(z)\). Completeness is just completeness of finite complex coordinate space. Continuity gives \(T_z(W)=W\), hence \(F(z,W)=0\). Two fixed points in the ball would satisfy \(|u-v|\le\lambda|u-v|\), forcing equality. Every solution in the ball is a fixed point, so this is also the needed uniqueness of solutions. At \(z=a\), \(b\) is already a fixed point.

Lemma 1.2 of [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md) makes the uniform limit holomorphic. Moreover \(A^{-1}\partial_wF=I-\partial_wT_z\) is invertible: the geometric series \(\sum_{j\ge0}(\partial_wT_z)^j\) converges in operator norm and multiplying its partial sums by \(I-\partial_wT_z\) leaves a remainder tending to zero. Differentiate \(F(z,W(z))=0\) and solve for the derivative to obtain (3). \(\square\)

For the Bézout identity each simple root has \(l=1\) and \(r_t\ne0\). The theorem supplies the local holomorphic root charts used by the polynomial approximation lesson. Their continued branches are not asserted to be single-valued globally. For a monic degree-\(m\) polynomial with coefficients \(c_0,\ldots,c_{m-1}\), every root satisfies \(|t|\le1+\max_j|c_j|\): if \(|t|>1+M\), then \(M\sum_{j<m}|t|^j<|t|^m\), contrary to the polynomial equation. Thus at a simple-root parameter, choose \(m\) disjoint small root disks and apply Corollary 2.3 of [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md); each contains exactly one nearby root, and the full factorization theorem excludes additional roots. This supplies the whole finite local covering asserted in the polynomial approximation lesson.

## Exercises with complete solutions

**Exercise 1 (intermediate: algebra).** For \(r(w,t)=t^2-w\in\mathbb C[w,t]\), prove irreducibility and give an exact identity (2). Locate the simple-root parameter set.

**Solution 1.** In \(K=\mathbb C(w)\), reducibility of the monic quadratic would give a root \(a/b\), for coprime \(a,b\in\mathbb C[w]\), satisfying \(a^2=w b^2\). The prime \(w\) has even factorization exponent on the left and odd exponent on the right, a contradiction. Thus the quadratic is irreducible in \(K[t]\), and by Lemma 1.2 in \(\mathbb C[w,t]\). Since \(r_t=2t\), the identity is \(4r-2t r_t=-4w\). It gives \(\Delta=-4w\), so \(w\ne0\) is the simple-root set. At \(w=0\) the root 0 has multiplicity 2. Each nonzero parameter has two local holomorphic branches, without a claim of globally chosen square roots on \(\mathbb C\setminus\{0\}\).

**Exercise 2 (advanced: implicit branch).** Near \((z,w)=(0,1)\), solve \(w^2=1+z\) by Theorem 3.1. Find \(W'(0)\) and the first three Taylor coefficients.

**Solution 2.** Here \(F=w^2-1-z\), \(F_w(0,1)=2\ne0\); the theorem gives the unique nearby branch with \(W(0)=1\). Equation (3) yields \(W'=1/(2W)\), hence \(W'(0)=1/2\). Write \(W=1+c_1z+c_2z^2+O(z^3)\); substitution gives \(2c_1=1\) and \(2c_2+c_1^2=0\). Thus \(c_1=1/2,c_2=-1/8\), and the first three coefficients are \(1,1/2,-1/8\). This argument chooses a branch only near 0.

## References

- Avi Zeff, Complex Analysis lecture on Pompeiu’s formula, March 2026, Section 2. [Lecture](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983. Used for the equation-theoretic context.
