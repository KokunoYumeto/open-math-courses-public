# Hermite and the transcendence of e

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol at Ultra. Public domain (CC0).*

Liouville's construction starts by making a number easy to approximate. Hermite's proof starts with a familiar number and manufactures an approximation suited to a hypothetical algebraic relation. A polynomial with many prescribed zeros makes an integral small. Its derivatives at the same points make an integer. A prime ensures that this integer is nonzero. The contradiction occurs when the analytic estimate puts it strictly between minus one and one.

We first establish the classical irrationality and quadratic obstructions, then prove Hermite's theorem in the elementary form developed by Hilbert, Hurwitz and Gordan. We finish by reading the integral as a simultaneous approximation and by adapting the proof to rational powers of \(e\). The prerequisites are Algebraic and transcendental numbers; Liouville's theorem, differentiation of polynomials, the exponential series and integration along a segment. Evertse's *Diophantine Approximation*, Chapter 4, §4.1, and Conrad's note *Transcendence of e* are basic references for the prime and integral method.

## 1. Irrationality and the quadratic obstruction

### Proposition 3.1. The first arithmetic obstructions

The number \(e\) is irrational. Neither \(e\) nor \(e^2\) is a quadratic irrational.

**Proof.** Suppose \(e=A/B\), with positive integers \(A,B\). For an integer \(N\geq\max(B,2)\), the number

\[
 N!\left(e-\sum_{j=0}^N\frac1{j!}\right)
\]

is an integer: \(B\mid N!\) and each \(j!\mid N!\). It is positive and at most

\[
 \sum_{k=1}^\infty(N+1)^{-k}=1/N<1,
\]

an impossibility.

The continued-fraction estimates in the opening lesson show that a real quadratic irrational must have bounded partial quotients. Indeed, Liouville gives \(|x-p/q|>c/q^2\), whereas a convergent gives \(|x-p_n/q_n|<1/(a_{n+1}q_n^2)\); hence \(a_{n+1}<1/c\). Euler's expansion of \(e\), proved there, has the unbounded subsequence \(2,4,6,\ldots\). Thus \(e\) is not quadratic.

For \(e^2\), we supply the corresponding expansion of a rational transform. Define

\[
 A_n=\frac{2^n}{n!}\int_0^1x^n(1-x)^ne^{2x}\,dx,\qquad
 B_n=\frac{2^n}{n!}\int_0^1x^{n+1}(1-x)^ne^{2x}\,dx.
\]

These integrals are positive and \(0<A_{n+1}/A_n\leq1/[2(n+1)]<1\). The same two integrations by parts as in Euler's expansion, now with derivative \((e^{2x})'=2e^{2x}\), give

\[
 A_n+A_{n-1}=2B_{n-1},\qquad
 (2n+1)A_n=2B_{n-1}-2B_n\qquad(n\geq1).
\]

To verify the factors, differentiate \(x^n(1-x)^n/n!\); its derivative is \((1-2x)x^{n-1}(1-x)^{n-1}/(n-1)!\). Differentiating \(x^{n+1}(1-x)^n/n!\) gives \((n+1)x^n(1-x)^n/n!-x^{n+1}(1-x)^{n-1}/(n-1)!\). Integrate these derivatives against \(e^{2x}\), whose boundary terms vanish, and then multiply by the appropriate powers of two. The second calculation uses \(x^2=x-x(1-x)\). Eliminating the \(B\)'s yields

\[
 A_{n-1}=(2n+1)A_n+A_{n+1}.
\]

Direct integration gives \(A_0=(e^2-1)/2\) and \(A_1=1\). Therefore

\[
 T:=\frac{e^2+1}{e^2-1}=1+\frac{A_1}{A_0}
 =[1;3,5,7,\ldots].
\]

The positive remainders less than one establish each step of the continued-fraction algorithm. The infinite-fraction convergence and irrationality proof in the opening lesson show that \(T\) is irrational. Its unbounded partial quotients show that it is not quadratic. If \(e^2\) were rational or quadratic, then \(T\) would belong to the same field and would have degree at most two. This contradiction proves the claim. \(\square\)

These are separate obstructions, proved before transcendence. A number of degree three or higher is not excluded by the quadratic argument. Hermite's construction will exclude every finite degree at once.

## 2. An integral that records every derivative

For a polynomial \(f\) of degree \(m\), put

\[
 F(x)=\sum_{j=0}^m f^{(j)}(x),\qquad
 \overline f(x)=\sum_{j=0}^m|c_j|x^j
 \quad\text{if }f(x)=\sum_{j=0}^m c_jx^j.
\]

The bar in \(\overline f\) means coefficient moduli, not complex conjugation.

### Lemma 3.2. Hermite's identity

For every \(t\in\mathbb C\), with integration along the segment from zero to \(t\),

\[
 I(t):=\int_0^t e^{t-u}f(u)\,du=e^tF(0)-F(t),\qquad
 |I(t)|\leq|t|e^{|t|}\overline f(|t|).
\]

**Proof.** Since the derivatives telescope, \(F-F'=f\). Consequently \((e^{-u}F(u))'=-e^{-u}f(u)\). Integrating and multiplying by \(e^t\) gives the identity. This is also repeated integration by parts, one derivative at each step, terminating when the next derivative of the polynomial is zero.

Parameterize the segment as \(u=st\), \(0\leq s\leq1\). Then \(|e^{t-u}|\leq e^{|t|}\), \(|f(u)|\leq\overline f(|t|)\), and the segment length is \(|t|\). Integration of these bounds proves the estimate, including \(t=0\). \(\square\)

The identity is useful because a polynomial can have tiny values on a segment while its endpoint derivatives carry large, rigid arithmetic information. We will normalize the derivatives by a factorial so that this information is integral rather than merely rational.

### Lemma 3.3. Derivatives and a prime

For \(g\in\mathbb Z[X]\), \(g^{(j)}/j!\in\mathbb Z[X]\). Fix integers \(n\geq1\) and a prime \(p>n\), and put

\[
 g(X)=X^{p-1}\prod_{k=1}^n(X-k)^p,qquad
 f(X)=\frac{g(X)}{(p-1)!},\qquad m=(n+1)p-1.
\]

Every \(f^{(j)}(k)\), for \(0\leq k\leq n\) and \(0\leq j\leq m\), is an integer. All are divisible by \(p\) except possibly \(k=0,j=p-1\); at that exception,

\[
 f^{(p-1)}(0)=(-1)^{np}(n!)^p\not\equiv0\pmod p.
\]

**Proof.** Differentiate a monomial: \((X^a)^{(j)}/j!=\binom ajX^{a-j}\), or zero if \(j>a\). Linearity proves the first assertion. At \(k\geq1\), the root multiplicity \(p\) makes the derivatives of orders below \(p\) zero. At zero, the root multiplicity is \(p-1\). For \(j\geq p\), write

\[
 f^{(j)}(k)=\frac{j!}{(p-1)!}\frac{g^{(j)}(k)}{j!}.
\]

The second factor is integral and the first is an integer divisible by \(p\). The only remaining derivative is obtained from the coefficient of \(X^{p-1}\) in \(g\), which is \(\prod_{k=1}^n(-k)^p\). Since \(p>n\), none of its factors is divisible by \(p\). \(\square\)

## 3. The transcendence proof

### Theorem 3.4. Hermite's theorem

The number \(e\) is transcendental.

**Proof.** Suppose it satisfies

\[
 q_0+q_1e+\cdots+q_ne^n=0,qquad
 q_k\in\mathbb Z,quad n\geq1,quad q_0\neq0.
\]

A nonzero constant term can always be arranged: remove any factor \(X\) from a hypothetical polynomial relation, since \(e\neq0\). Take arbitrarily large primes \(p>\max(n,|q_0|)\), and use \(f,F,I\) from the preceding lemmas. Set

\[
 J=\sum_{k=0}^n q_k I(k).
\]

Hermite's identity and the assumed relation cancel the terms \(e^kF(0)\), leaving

\[
 J=-\sum_{k=0}^n q_kF(k)\in\mathbb Z.
\]

Lemma 3.3 gives

\[
 J\equiv-q_0(-1)^{np}(n!)^p\not\equiv0\pmod p.
\]

Thus \(J\neq0\) and \(|J|\geq1\). Both restrictions on \(p\) matter: \(p>n\) protects the factorial product and \(p>|q_0|\) protects the coefficient.

For the upper bound, on every segment \([0,k]\), \(0\leq k\leq n\), all factors \(|u|\) and \(|u-j|\) are at most \(n\). Hence

\[
 |f(u)|\leq\frac{n^{(n+1)p-1}}{(p-1)!},\qquad
 |I(k)|\leq\frac{k e^k n^{(n+1)p-1}}{(p-1)!}.
\]

Put \(C=n^{n+1}\) and \(A=e^n\sum_{k=1}^n|q_k|\). These are independent of \(p\). Since \(k\leq n\),

\[
 |J|\leq A\frac{C^p}{(p-1)!}\longrightarrow0.
\]

For completeness, consecutive terms of \(C^p/(p-1)!\) have ratio \(C/p\), which is at most one half for all sufficiently large \(p\). Thus the sequence tends to zero, also along primes. There are arbitrarily large primes by Euclid's argument: a finite list of all primes would omit every prime divisor of one plus their product. For a sufficiently large allowed prime the upper bound is less than one, contradicting the integer lower bound. \(\square\)

The unnormalized version uses \(g\) rather than \(f\): its nonzero integer has modulus at least \((p-1)!\), while its analytic estimate is at most \(AC^p\). The two formulations are the same proof. Normalizing at the start makes the final contradiction especially transparent.

### A worked prime

For \(n=1,p=3\), the unnormalized polynomial is

\[
 g(X)=X^2(X-1)^3=X^5-3X^4+3X^3-X^2.
\]

At zero its nonzero derivatives are \(g''=-2\), \(g^{(3)}=18\), \(g^{(4)}=-72\), \(g^{(5)}=120\), summing to 64. At one, the expansion \(g(1+w)=w^3+2w^4+w^5\) gives derivatives 6, 48 and 120, summing to 174. Every derivative except \(g''(0)\) is divisible by \(3!\); that derivative is divisible by \(2!\) but not by \(3!\). The normalized sums are 32 and 87, the latter divisible by three and the former congruent to two.

Hermite's identity reads

\[
 \int_0^1e^{1-u}u^2(u-1)^3\,du=64e-174.
\]

The integral is negative, confirming \(e<87/32\). Under a hypothetical relation \(q_0+q_1e=0\), the unnormalized combination would equal \(-64q_0-174q_1\); its factorial divisibility and nonzero residue are exactly the pattern used in the proof. No particular \(q_0,q_1\) satisfying such a relation is being asserted.

## 4. Reading the integral as an approximation

For the prime construction, \(F(0)\) is a nonzero integer. The identity gives a common-denominator approximation to all the powers under consideration:

\[
 e^k-\frac{F(k)}{F(0)}=\frac{I(k)}{F(0)}\qquad(1\leq k\leq n).
\]

The integral errors tend to zero. A putative integer relation among the powers would combine these approximations into a nonzero integer smaller than one. This is the simultaneous-approximation aspect of Hermite's method. Later auxiliary functions arrange many more zeros while controlling the arithmetic size of their coefficients.

A **Padé approximant of type \([a/b]\)** to a power series \(S(x)\) is a quotient \(P(x)/Q(x)\), with \(\deg P\leq a\), \(\deg Q\leq b\), \(Q(0)=1\), and \(Q(x)S(x)-P(x)=O(x^{a+b+1})\). Two examples for \(e^x\) are

\[
 \frac{2+x}{2-x},\qquad
 \frac{12+6x+x^2}{12-6x+x^2}.
\]

Their normalized denominators are \(1-x/2\) and \(1-x/2+x^2/12\). Multiplication by the exponential series verifies agreement through degrees two and four, respectively.

Their errors also have integral signs. Apply Hermite's identity to \(f_t(u)=u(u-t)\). It gives

\[
 e^t(2-t)-(2+t)=\int_0^t e^{t-u}u(u-t)\,du.
\]

At \(t=1\) the right side is negative, so the first approximant gives the upper bound three. Applying it to \(f_t(u)=u^2(u-t)^2\) gives

\[
 2e^t(t^2-6t+12)-2(t^2+6t+12)
 =\int_0^t e^{t-u}u^2(u-t)^2\,du.
\]

At \(t=1\),

\[
 e-\frac{19}7=\frac1{14}\int_0^1 e^{1-u}u^2(1-u)^2\,du,
 \qquad \frac1{420}<e-\frac{19}7<\frac e{420}.
\]

The last bounds use \(1<e^{1-u}<e\) on the interior and \(\int_0^1u^2(1-u)^2\,du=1/30\). Thus \(19/7<e<3\), and the actual second error is about \(0.003996114\). These are approximations with rigorously controlled signs, not just decimal comparisons.

## 5. Rational powers and the boundary of the method

### Corollary 3.5. Rational powers of e

For every nonzero rational \(r\), \(e^r\) is transcendental.

**Proof.** Write \(r=a/b\), \(a\neq0\), \(b\geq1\). If \(e^{a/b}\) were algebraic, its \(b\)-th power \(e^a\) would be algebraic. If \(a>0\), \(e\) would then satisfy \(X^a-e^a=0\) over the algebraic numbers, contradicting their algebraic closure and Theorem 3.4. If \(a<0\), take the inverse first and apply the positive case. \(\square\)

The proof gives every nonzero rational exponent. It does not yet give every nonzero algebraic exponent; that is Lindemann's theorem, taught in the next lesson. It gives no algebraic-independence assertion about \(e\) and \(\pi\), and does not settle the individual status of \(e+\pi\) or \(e\pi\).

## 6. Exercises

1. **Easy — the analytic identity.** Prove Hermite's identity by repeated integration by parts and verify its bound for complex \(t\), with the integration path specified.

2. **Medium — factorial divisibility.** For the unnormalized polynomial \(g(X)=X^{p-1}\prod_{k=1}^n(X-k)^p\), prove that \(g^{(j)}(k)\) is divisible by \(p!\) at every integer \(1\leq k\leq n\), and at zero unless \(j=p-1\). Compute that exceptional derivative and explain the restrictions on the prime.

3. **Medium — a series proof for the square.** Prove that \(e^2\) is irrational directly from the series for \(e\) and \(e^{-1}\). Control both the size and the nonvanishing of the remainder.

4. **Medium — the second Padé approximant.** Solve for the normalized polynomials of type \([2/2]\) for \(e^x\), and derive a positive integral estimate for \(e-19/7\).

5. **Hard — move the arithmetic grid.** For every nonzero rational \(r\), prove that \(1,e^r,e^{2r}\) are linearly independent over \(\mathbb Q\) by adapting the prime construction to the grid \(0,r,2r\). Give an explicit exponential-over-factorial upper bound after clearing denominators.

## 7. Solutions

**1.** Integration by parts gives \(\int_0^t e^{-u}f(u)\,du=f(0)-e^{-t}f(t)+\int_0^t e^{-u}f'(u)\,du\). Repeat through the degree of \(f\) and multiply by \(e^t\). Parameterizing the segment by \(u=st\) bounds the modulus of the integrand by \(e^{|t|}\overline f(|t|)\), and the path length is \(|t|\). This proves exactly the stated bound for either real or complex endpoints.

**2.** A multiplicity-\(p\) zero has derivatives zero below order \(p\). At larger orders \(g^{(j)}(k)=j!\,(g^{(j)}(k)/j!)\), and the second factor is integral. Thus \(p!\) divides these values. At zero the same argument applies for \(j\geq p\); the smaller derivatives vanish except \(j=p-1\), whose value is \((p-1)!(-1)^{np}(n!)^p\). The prime \(p>n\) does not divide \(n!\), so this value is not divisible by \(p!\). In the linear combination, \(p>|q_0|\) additionally ensures that multiplying the exceptional value by \(q_0\neq0\) preserves its nonzero residue.

**3.** If \(e^2=a/b\), with positive integers \(a,b\), then \(a e^{-1}-b e=0\). Let \(N\) be large and even. Multiply this relation by \(N!\), and subtract the truncated series. Their finite terms are integers, so the remainder

\[
 R_N=\sum_{k=1}^\infty
 \frac{a(-1)^k-b}{(N+1)(N+2)\cdots(N+k)}
\]

is an integer. The first term is \(-(a+b)/(N+1)\). The modulus of all later terms is at most

\[
 \frac{a+b}{N+1}\sum_{j=1}^\infty(N+2)^{-j}
 =\frac{a+b}{(N+1)^2},
\]

strictly less than the first term's modulus. Thus \(R_N<0\). The whole remainder has modulus at most \((a+b)/N\), which is less than one for large \(N\). This contradicts integrality. The parity choice is what prevents cancellation of the leading remainder.

**4.** Write \(Q=1+ux+vx^2\). Vanishing of the coefficients of \(x^3,x^4\) in \(Qe^x\) gives \(1/6+u/2+v=0\) and \(1/24+u/6+v/2=0\). Subtraction after multiplying the second by two gives \(u=-1/2\), and then \(v=1/12\). The first three coefficients give \(P=1+x/2+x^2/12\). Thus \(P/Q=(12+6x+x^2)/(12-6x+x^2)\). For its error at one, the identity with \(u^2(u-1)^2\) gives \(e-19/7=\frac1{14}\int_0^1 e^{1-u}u^2(1-u)^2\,du\). The beta integral is \(1/30\); comparison with one and \(e\) gives the bounds in Section 4.

**5.** We give the adaptation for any fixed \(n\geq1\), then take \(n=2\). Write \(r=a/b\), \(a\neq0\), \(b\geq1\), and suppose \(\sum_{k=0}^n q_ke^{kr}=0\), with integer coefficients and \(q_0\neq0\). Remove initial zero coefficients and divide by a power of \(e^r\) if needed. Set

\[
 g(X)=X^{p-1}\prod_{k=1}^n(bX-ka)^p,
 \quad f=g/(p-1)!,\quad m=(n+1)p-1,
\]

with a prime \(p>\max(n,|q_0|,|a|,b)\). The roots at \(kr\), for \(k\geq1\), have multiplicity \(p\). For \(j\geq p\), the polynomial \(g^{(j)}/j!\) has integer coefficients and degree at most \(m-j\). Its value at \(ka/b\) has denominator dividing \(b^{m-j}\). Hence every \(b^m f^{(j)}(kr)\) is an integer divisible by \(p\). The smaller derivatives vanish except at zero with \(j=p-1\), where the value is

\[
 b^m(-a)^{np}(n!)^p\not\equiv0\pmod p.
\]

Hermite's identity makes \(J=b^m\sum q_k I(kr)=-b^m\sum q_kF(kr)\) an integer with nonzero residue modulo \(p\). Thus \(|J|\geq1\).

Put \(R=n|r|\), \(M=\max(1,R)\), \(C=bM+n|a|\), and \(B=b^{n+1}MC^n\). On every relevant segment, \(|u|\leq M\) and \(|bu-ka|\leq C\). Since \(b^m\leq b^{(n+1)p}\),

\[
 |J|\leq R e^R\left(\sum_{k=1}^n|q_k|\right)
 \frac{B^p}{(p-1)!}\longrightarrow0.
\]

The estimate also applies when \(r<0\), because it uses segment lengths and moduli. It contradicts the integer bound for a sufficiently large allowed prime. For \(n=2\) this proves the requested independence; for \(n=1\) it handles a relation left after removing initial zero coefficients.

## Proof scope

Every mathematical result used beyond the elementary analysis prerequisites has a proof in this lesson or in the opening lesson. Euler's continued fraction and the estimates for all rational approximations are proved there, rather than assumed from a book. The transcendence statement here covers rational exponents; the next lesson proves the algebraic-exponent generalization.

## References

- **Evertse.** J.-H. Evertse, [*Diophantine Approximation*, Chapter 4: Transcendence results](https://pub.math.leidenuniv.nl/~evertsejh/dio19-4.pdf), Leiden course notes, §4.1, Theorem 4.1 and Lemmas 4.2–4.7: Hermite's theorem by the prime and integral method, with the factorial-normalized auxiliary polynomial. The simplifications of Hermite's proof are D. Hilbert, [“Ueber die Transcendenz der Zahlen e und π”](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0043/LOG_0021.pdf), A. Hurwitz, [“Beweis der Transcendenz der Zahl e”](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0043/LOG_0022.pdf), and P. Gordan, [“Transcendenz von e und π”](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0043/LOG_0023.pdf), *Mathematische Annalen* 43 (1893), 216–219, 220–221 and 222–224.
- **Conrad.** K. Conrad, [*Transcendence of e*](https://kconrad.math.uconn.edu/blurbs/analysis/transcendence-e.pdf), expository note, §3: Hermite's identity, the factorial normalization of the derivative sums, and the simultaneous approximations to \(e,e^2,\ldots,e^m\) obtained from Hilbert's polynomials.
- **Cohn.** H. Cohn, [*A short proof of the simple continued fraction expansion of e*](https://arxiv.org/abs/math/0601660v3), arXiv:math/0601660v3, 2006: Euler's continued fraction for \(e\) from integrals of Hermite's kind, as in the opening lesson. The quadratic obstruction for \(e^2\) above uses the corresponding integrals with \(e^{2x}\).
