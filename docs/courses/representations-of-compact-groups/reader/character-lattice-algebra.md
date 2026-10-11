# Integer character lattices and integral cancellation

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 11 October 2026. Independent exposition of established mathematics. CC0. No independent review is claimed.*

The character arguments need divisibility in an integer Laurent ring, not just cancellation of complex-valued functions off their zero sets. This companion gives the precise algebra behind RT-CPT-09, Lemma 1.2, and RT-CPT-11, Lemma 3.1. A root need not be a primitive character, and coprime elements need not generate the unit ideal.

The polynomial factorization theorem is already proved in [*Primitive factors and moving polynomial roots*, Lemmas 1.1–1.2 and Theorem 1.3](../../constant-coefficient-equations-and-solvability/AN02-L044.html#primitive-polynomials-and-unique-factorization). Its field-division input is proved in [*Polynomial and contour interfaces for stable boundary models*, Section 2](../../constant-coefficient-equations-and-solvability/prerequisites/stable-prerequisite-bridges.html#scalar-polynomial-division-and-bezout). Only these algebraic parts are used, not the later analytic branch construction. The existing [saturated-lattice construction](../../normal-toric-orbits-and-derived-realization/normal-toric-orbits-and-derived-realization.html#the-saturated-lattice-product-at-an-orbit) uses the same integer basis argument as CA.1 below; the matrices here specify its rank-one application.

Let \(X\) be a free abelian group of finite rank \(r\). Write \(A[X]\) for the ring of finite sums \(\sum_{x\in X}a_x e^x\), with multiplication \(e^xe^y=e^{x+y}\). A basis \(b_1,\ldots,b_r\) identifies this ring with \(A[z_1^{\pm1},\ldots,z_r^{\pm1}]\) by \(e^{b_j}\mapsto z_j\). Every basis change below is an integer group isomorphism and therefore induces this actual algebra isomorphism, not a change of coefficient field. A nonzero vector is **primitive** if it is not an integer multiple \(d\beta\) with \(d>1\).

## Primitive vectors and their receiving bases

**Lemma CA.1 (primitive completion).** Every nonzero \(\alpha\in X\) has a unique expression \(\alpha=d\beta\), with \(d>0\) an integer and \(\beta\) primitive. The vector \(\beta\) extends to an integer basis of \(X\). In particular, \(X/\mathbb Z\beta\) is free, whereas \(X/\mathbb Z(d\beta)\) has a cyclic torsion summand of order \(d\).

*Proof.* Choose an initial basis and let \(a=(a_1,\ldots,a_r)^t\ne0\) be the coordinate column of \(\alpha\). The Euclidean algorithm repeatedly replaces two integers by a divisor and its remainder; the nonnegative remainder strictly decreases until zero. The last positive remainder \(g\) divides both original integers, and every common divisor divides each remainder. Reversing the substitutions gives integers \(u,v\) with \(ua+vb=g\) for a pair \((a,b)\ne(0,0)\), including pairs with a zero entry and either sign. The matrix

\[
 M=\begin{pmatrix}u&v\\-b/g&a/g\end{pmatrix},
 \qquad
 M^{-1}=\begin{pmatrix}a/g&-v\\b/g&u\end{pmatrix}
\]

has integer entries, determinant one, and sends \((a,b)^t\) to \((g,0)^t\). Permute a nonzero coordinate to the first position and apply these matrices to it and each successive nonzero coordinate. For rank one only a possible sign change is needed. This gives \(U\in\operatorname{GL}_r(\mathbb Z)\) with \(Ua=(d,0,\ldots,0)^t\), where \(d=\gcd(a_1,\ldots,a_r)>0\). All inverses remain integral. Thus \(\beta=\alpha/d\) has integer coordinates and \(U\beta=e_1\). The columns of \(U^{-1}\) are the required basis, with first column \(\beta\). Coordinate gcd one is equivalent to primitivity, proving existence and uniqueness of \(d,\beta\). In this basis the two quotients are respectively \(\mathbb Z^{r-1}\) and \((\mathbb Z/d\mathbb Z)\oplus\mathbb Z^{r-1}\). The rank-zero case has no nonzero vector to which the assertion applies. ∎

## Polynomial and Laurent factorization

**Theorem CA.2 (the exact coefficient rings).** Both \(\mathbb Z[X]\) and \(\mathbb C[X]\) are unique factorization domains. Their units are respectively \(\pm e^x\) and \(c e^x\), with \(x\in X\), \(c\in\mathbb C^\times\). In either ring, if finitely many pairwise coprime nonzero elements divide \(f\), their product divides \(f\). Here “coprime” means that no irreducible factor is shared; it does not mean comaximal.

*Proof.* The integers have unique factorization: repeated factorization of a positive composite integer terminates by strict decrease, and an integer prime dividing a product divides one factor. For the latter assertion, if \(p\nmid a\), the Euclidean Bézout identity in CA.1 gives \(up+va=1\); multiplication by \(b\) proves \(p\mid b\) when \(p\mid ab\). Prime cancellation proves uniqueness, with sign as the unit. A field is a unique factorization domain because each nonzero element is a unit.

Apply the cited polynomial theorem successively, with \(R=\mathbb Z\) or \(\mathbb C\) and then with the polynomial rings already obtained. It proves factorization over the coefficient ring itself, using primitive products and Gauss divisibility; no replacement of integer coefficients by rational coefficients is made. Thus \(A[z_1,\ldots,z_r]\) is factorial for either choice of \(A\).

Here is the localization step. Each \(z_i\) is prime, since setting \(z_i=0\) gives a polynomial domain. An irreducible polynomial \(p\) not associated to any \(z_i\) stays prime after the variables are inverted: if \(p\) divides a product of fractions, clearing their monomial denominators gives polynomial divisibility, and primality says it divides one numerator, since it divides no denominator. It does not become a unit, for that would make it divide a monomial. Every Laurent polynomial is a polynomial divided by a monomial; factor its numerator and discard exactly the variable factors, which are now units. This proves factorization and uniqueness in the Laurent ring. It also proves the assertion about units: a polynomial numerator can become invertible only if its factorization consists of coefficient units and variables.

For a nonzero \(f\), compare its prime exponents with those of each divisor. Pairwise coprimality makes those exponent requirements disjoint, so their product divides \(f\). For \(f=0\), the quotient can be zero. An empty product is one. None of this uses a Bézout identity in a multivariable ring. For example \(x,y\) are coprime in \(\mathbb Z[x,y]\), but \((x,y)\) is a proper ideal. ∎

## Vanishing on the whole root kernel

Identify the compact torus associated with \(X\) with \(T_X=\operatorname{Hom}(X,S^1)\). The function corresponding to \(e^x\) is \(t\mapsto t(x)\). A chosen integer basis gives a bijection \(T_X\simeq(S^1)^r\), since arbitrary basis values extend uniquely to a group homomorphism.

**Lemma CA.3 (nonprimitive binomial divisibility).** Let \(0\ne\alpha=d\beta\in X\), with \(d>0\) and \(\beta\) primitive. If \(f\in\mathbb Z[X]\) vanishes at every \(t\in T_X\) satisfying \(t(\alpha)=1\), then \(1-e^{-\alpha}\) divides \(f\) in \(\mathbb Z[X]\).

*Proof.* Use the basis supplied by CA.1 and put \(z=e^\beta\). Its remaining variables generate \(B=\mathbb Z[z_2^{\pm1},\ldots,z_r^{\pm1}]\). Multiply \(f\) by \(z^N\) so it lies in \(B[z]\). Division by the monic polynomial \(z^d-1\) is valid over \(B\): cancel the leading term repeatedly without dividing a coefficient, until the remainder \(q\) has degree less than \(d\). Subtracting two such divisions proves uniqueness by degree. This gives

\[
 z^N f=(z^d-1)h+q,\qquad h,q\in B[z],\quad \deg_z q<d
\]

with the zero remainder allowed. Fix any values of the other variables on their unit circles. All \(d\) numbers \(\exp(2\pi i j/d)\), \(0\le j<d\), belong to the specified kernel, so the resulting complex polynomial \(q\) vanishes at these distinct numbers. A nonzero polynomial of degree less than \(d\) cannot do so: division by each distinct linear factor reduces the degree by one. Hence every coefficient of \(q\), evaluated at every choice of the remaining circle coordinates, is zero.

A Laurent polynomial vanishing on \((S^1)^s\) is zero. For \(s=0\) this is the assertion about its constant value. For \(s>0\), clear negative powers and fix the last \(s-1\) variables; the resulting univariate polynomial has infinitely many roots, so all its coefficients vanish. Induction on \(s\) proves the claim. Apply this to the coefficients of \(q\) to obtain \(q=0\) in the integer ring, not only at torus points. Finally \(1-e^{-\alpha}=z^{-d}(z^d-1)\), and the monomial factors are units by CA.2. Thus the quotient is integral. ∎

The whole kernel is essential. The polynomial \(z-1\) vanishes on the identity component of \(\{z:z^2=1\}\), but \(z^2-1\) does not divide it. Dropping the other components would invalidate the character proof for nonprimitive roots.

## Distinct root directions and the product

**Lemma CA.4 (coprimality for nonparallel directions).** If nonzero \(\alpha,\gamma\in X\) are not proportional in \(X\otimes\mathbb R\), the elements \(1-e^{-\alpha}\) and \(1-e^{-\gamma}\) have no common irreducible factor in \(\mathbb Z[X]\). Consequently, if a finite collection of pairwise nonparallel nonzero characters has its individual binomials dividing \(f\), the product of those binomials divides \(f\) integrally.

*Proof.* Write \(\alpha=d\beta\), with \(\beta\) primitive. Over \(\mathbb C[X]\), up to the displayed Laurent unit, its factorization is

\[
 1-e^{-\alpha}=e^{-d\beta}\prod_{\zeta^d=1}(e^\beta-\zeta).
\]

Every factor \(e^\beta-\zeta\) is prime. In a basis starting with \(\beta\), evaluation of its first variable at the nonzero number \(\zeta\) is a surjective homomorphism to the Laurent ring in the remaining variables. Division by \(z-\zeta\), after clearing negative powers, shows that its kernel is exactly the principal ideal of that factor. The target is a domain, proving primality.

Two binomials \(e^\beta-\zeta\) and \(e^\eta-\xi\) can be associates only if \(\eta=\beta\) or \(\eta=-\beta\). Indeed, CA.2 says that an associating unit is \(c e^v\). Equality of the two two-point supports gives
\(\{0,\beta\}=\{v,v+\eta\}\), whose difference vectors are equal up to sign. Thus the factorizations for nonparallel \(\alpha,\gamma\) share no prime over \(\mathbb C[X]\).

Suppose an integer irreducible \(p\) divided both binomials. If its image in \(\mathbb C[X]\) were a nonunit, its complex factorization would supply a common complex prime, which was just excluded. If its image were a unit, CA.2 makes \(p=a e^v\), with a nonzero integer \(a\); because \(p\) is not an integer-ring unit, \(|a|>1\). But divisibility by \(a e^v\) would make all coefficients of \(1-e^{-\alpha}\) divisible by \(a\), contradicting its coefficients \(1,-1\). No common integer irreducible exists. The product assertion is now CA.2. This argument also covers the empty collection, including a group with no roots. ∎

## The two applications

**Corollary CA.5 (Vandermonde and Weyl receivers).** An alternating Laurent polynomial in \(z_1,\ldots,z_n\) with integer coefficients is divisible in that ring by \(\prod_{i<j}(z_i-z_j)\). For a reduced root system whose roots are characters in \(X\), if \(f\in\mathbb Z[X]\) vanishes on every positive-root kernel, then
\(\prod_{\alpha>0}(1-e^{-\alpha})\) divides \(f\) in \(\mathbb Z[X]\), even when individual roots are not primitive in \(X\).

*Proof.* In the polynomial case, alternatingness makes substitution \(z_i=z_j\) give its own negative, hence zero over the characteristic-zero ring. Division by the monic polynomial \(z_i-z_j\), in the variable \(z_i\), gives divisibility. This polynomial is prime: its quotient ring is the integer polynomial ring with those two variables identified. Factors for different unordered pairs are not associates; polynomial units are \(\pm1\), and comparison of coefficients shows that associates must use the same pair. Their product therefore divides by CA.2. An alternating Laurent polynomial becomes an alternating polynomial after multiplication by a sufficiently high power of the symmetric monomial \(z_1\cdots z_n\). Dividing that monomial back proves the Laurent assertion, including \(n=0,1\), when the product is empty. This is the exact ring argument used in RT-CPT-09, Lemma 1.2.

For the root assertion, CA.3 gives each individual divisor. Distinct positive roots of a reduced root system are not parallel; this is precisely where reducedness is used. CA.4 therefore gives their product, with all integer coefficients retained. Apply this to the numerator \(R_\lambda\) after RT-CPT-11, Lemma 3.1 proves its vanishing on the entire root kernels. The character calculation and the later analytic existence argument are unchanged. ∎
