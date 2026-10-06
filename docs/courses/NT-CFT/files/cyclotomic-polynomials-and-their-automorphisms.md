# Cyclotomic polynomials and their automorphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

A supporting excerpt: definitions and the complete Theorem 12.1 proof, not the full parent lesson.

Fix the complex embedding and write
\[
\zeta_n=e^{2\pi i/n},\qquad K_n=\mathbf Q(\zeta_n),\qquad
U_n=(\mathbf Z/n\mathbf Z)^\times.
\tag{1}
\]
We take \(U_1\) to be the trivial group and \(\varphi(1)=1\). Both \(K_1\) and \(K_2\) are \(\mathbf Q\).

## Cyclotomic polynomials and their automorphisms

Define
\[
\Phi_n(X)=\prod_{\substack{1\leq a\leq n\\(a,n)=1}}(X-\zeta_n^a).
\]
Grouping roots by their exact orders gives
\[
X^n-1=\prod_{d\mid n}\Phi_d(X).
\tag{2}
\]
Inductively, every \(\Phi_n\) is monic and integral. Indeed, divide \(X^n-1\) by the product of the already integral monic factors for proper divisors. Monic division has integer quotient and remainder; the identity over \(\mathbf C\) makes that remainder zero.

**Monic factor lemma.** If a monic polynomial in \(\mathbf Z[X]\) is a product of two monic polynomials \(f,g\in\mathbf Q[X]\), then \(f,g\in\mathbf Z[X]\).

**Proof.** After clearing denominators and dividing the resulting coefficients by their greatest common divisor, write \(f_0=af\), \(g_0=bg\), where \(f_0,g_0\) are primitive integer polynomials and \(a,b\) are positive integers: they are the leading coefficients because \(f,g\) are monic. The product of two primitive polynomials is primitive. Indeed, for each prime \(p\) their reductions are nonzero polynomials over \(\mathbf F_p\); the product is nonzero because that polynomial ring is a domain. Thus no prime divides every coefficient of the product. But \(f_0g_0=abfg\) has coefficient greatest common divisor \(ab\), since \(fg\) is monic and integral. Consequently \(ab=1\), so both factors were integral. \(\square\)

**Theorem 12.1.** The polynomial \(\Phi_n\) is irreducible over \(\mathbf Q\). Its degree is \(\varphi(n)\), and the map
\[
U_n\xrightarrow{\sim}\operatorname{Gal}(K_n/\mathbf Q),
\qquad a\longmapsto\sigma_a,\quad \sigma_a(\zeta_n)=\zeta_n^a
\tag{3}
\]
is an isomorphism.

**Proof.** Let \(f\) be the monic minimal polynomial of \(\zeta_n\). It divides the monic integral polynomial \(\Phi_n\); the monic factor lemma makes its coefficients integers. Suppose \(p\nmid n\) is prime and \(\zeta_n^p\) is not a root of \(f\). Let \(g\) be its monic minimal polynomial, a distinct irreducible factor of \(\Phi_n\). Since \(g(\zeta_n^p)=0\), we have \(f(X)\mid g(X^p)\) in \(\mathbf Z[X]\).

Reduce modulo \(p\). The identity \(g(X^p)=g(X)^p\) there shows that any irreducible factor of \(\overline f\) also divides \(\overline g\). Since \(fg\mid X^n-1\), the latter polynomial would have a repeated factor modulo \(p\). Its derivative \(nX^{n-1}\) is relatively prime to it, which is a contradiction.

The same argument works for any primitive root that is already a root of \(f\). Every positive integer \(a\) coprime to \(n\) is a product of primes not dividing \(n\). Repeated application therefore puts every \(\zeta_n^a\) among the roots of \(f\). Thus \(f=\Phi_n\). All these roots lie in \(K_n\); sending \(\zeta_n\) to any one of them defines an automorphism. Composition multiplies exponents, proving (3). The cases \(n=1,2\) are linear polynomials and trivial groups. \(\square\)

The isomorphism (3) follows from the action on roots of unity. Throughout this lesson Frobenius means the **arithmetic** automorphism acting on residue fields by \(x\mapsto x^p\).

## References

The cyclotomic irreducibility argument is compared with J. S. Milne’s freely available [Fields and Galois Theory](https://www.jmilne.org/math/CourseNotes/FT.pdf), section on cyclotomic extensions, and [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf). The monic factor argument and complete Theorem 12.1 proof are written above.
