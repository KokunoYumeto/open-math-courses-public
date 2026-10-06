# Zero-free regions and the exceptional zero

*Written by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Self-checked by the writing AI; exact internal prerequisites and their written or planned state are identified below. Original material is public domain (CC0).*

The pole of the principal L-function prevents a direct zero-free argument for every character at once. Positivity nevertheless isolates the only possible obstruction: one simple real zero of one real character. A second positivity argument shows that two different primitive characters cannot both have zeros too close to 1. These are the classical zero-free-region and Landau–Page theorems. Cancellation in shifted logarithmic exponential sums then improves the dependence on height. We derive the character growth estimate and the wider Vinogradov–Korobov region, keeping both the modulus and the possible real exception explicit.

We use the completed-function product and Gamma estimates from *The functional equation of Dirichlet L-functions*, and nonvanishing at 1 from *Dirichlet's theorem on primes in arithmetic progressions*. The analogous completed zeta product is proved in Entire functions of order one and the Hadamard product of xi, Theorem 5.1 and Corollary 5.2; its classical zero-free region is proved in Nonvanishing on the line one and the zero-free region, Theorem 3.2. Section 8 identifies the exact shifted-sum prerequisite of the zeta course, including its still-planned mean-value support; the character and disc arguments needed here are supplied in full. The final effective distance bound uses the precise quadratic class-number input specified in *Values of Dirichlet L-functions at s = 1*. Its weaker analytic counterpart will be given separately.

Throughout, nontrivial zeros belong to the primitive character inducing the character under consideration. Finite Euler factors of an imprimitive character have zeros on the line \(\Re s=0\); they cannot produce the near-1 zeros discussed here. Put

\[
H_q(t)=\log(q(|t|+2)).
\]

## 1. Logarithmic derivatives and positive zero kernels

For \(s=\sigma+it\) with \(\sigma>1\), each nontrivial zero \(\rho=\beta+i\gamma\) contributes the positive kernel

\[
K_s(\rho)=\Re\frac1{s-\rho}
=\frac{\sigma-\beta}{(\sigma-\beta)^2+(t-\gamma)^2}>0.
\tag{1.1}
\]

Zeros are always repeated according to multiplicity. The absolute convergence of the real kernel sum follows from the genus-one product and \(0<\beta<1\).

**Lemma 1.1.** There is an absolute, effective constant \(C\) such that, for every character modulo \(q\) and \(1<\sigma\le2\),

\[
-\Re\frac{L'}L(s,\chi)
\le \Re\frac{\mathbf1_{\chi=\chi_0}}{s-1}
-\sum_{\rho\in Z}K_s(\rho)+C H_q(t),
\tag{1.2}
\]

where \(Z\) is any sublist of its primitive nontrivial zeros. In particular the sum can be empty, contain one zero, or contain a conjugate pair.

**Proof.** First suppose that \(\chi\) is primitive and nonprincipal. The real part of the Hadamard logarithmic derivative proved in the preceding functional-equation lesson is

\[
\Re\frac{\xi'}\xi(s,\chi)=\sum_\rho K_s(\rho).
\]

Indeed the real part of its constant cancels \(\sum_\rho\Re(1/\rho)\). Differentiating the completed function therefore gives the identity

\[
-\Re\frac{L'}L(s,\chi)
=\frac12\log\frac q\pi
+\frac12\Re\frac{\Gamma'}\Gamma\left(\frac{s+a}2\right)
-\sum_\rho K_s(\rho).
\tag{1.3}
\]

On \(1<\sigma\le2\), the Gamma logarithmic derivative is \(O(\log(|t|+2))\), uniformly for \(a=0,1\). For example its convergent expansion

\[
\frac{\Gamma'}\Gamma(z)=-\gamma_E+
\sum_{n\ge0}\left(\frac1{n+1}-\frac1{n+z}\right)
\]

gives this directly when \(\Re z\ge1/2\) and \(\Re z\le3/2\): for large \(|\Im z|\), split at \(n=2|\Im z|+2\). The initial harmonic sum is \(O(\log(|\Im z|+2))\); the other initial denominators have magnitude at least \(|\Im z|\), so their sum is \(O(1)\). The tail is \(O(|z|\sum_{n>2|\Im z|+2}n^{-2})=O(1)\). The remaining compact set is bounded by the uniformly convergent series. Dropping the positive kernels outside \(Z\) proves (1.2).

For the primitive principal character, namely the character of modulus 1, use instead
\(\Xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\).
The exact zeta-product prerequisite gives
\(\Re(\Xi'/\Xi)=\sum_\rho K_s(\rho)\), hence

\[
-\Re\frac{\zeta'}\zeta(s)
=\Re\frac1{s-1}+\Re\frac1s
-\frac12\log\pi+\frac12\Re\frac{\Gamma'}\Gamma(s/2)
-\sum_\rho K_s(\rho).
\tag{1.4}
\]

The regular terms are \(O(\log(|t|+2))\).

Finally let \(\chi\) modulo \(q\) be induced by \(\chi^*\) of conductor \(d\). The finite Euler factors give

\[
\frac{L'}L(s,\chi)-\frac{L'}L(s,\chi^*)
=\sum_{p\mid q\atop p\nmid d}
\frac{\chi^*(p)\log p}{p^s-\chi^*(p)}.
\tag{1.5}
\]

For \(\sigma\ge1\) its absolute value is at most
\(\sum_{p\mid q}\log p/(p-1)\le\log q\).
Since \(d\le q\), (1.2) follows from the primitive estimate. \(\square\)

We also record the local form needed in the next lesson.

**Lemma 1.2 (local zero count and local expansion).** Uniformly in \(q,t\),

\[
\#\{\rho:|\gamma-t|\le1\}\ll H_q(t).
\tag{1.6}
\]

For \(1/2\le\sigma\le2\), away from zeros and the principal pole,

\[
\frac{L'}L(s,\chi)
=-\frac{\mathbf1_{\chi=\chi_0}}{s-1}
+\sum_{|\gamma-t|\le1}\frac1{s-\rho}
+O(H_q(t)).
\tag{1.7}
\]

**Proof.** Evaluate (1.3), or (1.4), at \(2+it\). The absolutely convergent Euler product gives
\(|L'/L(2+it,\chi)|\le\sum_{n\ge2}\Lambda(n)n^{-2}<\infty\), an absolute bound. The Gamma terms are \(O(H_q(t))\), and the pole term is bounded. Thus
\(\sum_\rho K_{2+it}(\rho)\ll H_q(t)\).
For \(|\gamma-t|\le1\), \(1<2-\beta<2\) implies
\(K_{2+it}(\rho)\ge1/5\). This proves (1.6).

Subtract the complex Hadamard logarithmic derivatives at \(s\) and \(2+it\). Their constants cancel. For \(|\gamma-t|>1\), the difference of the zero terms has magnitude at most

\[
\left|\frac1{s-\rho}-\frac1{2+it-\rho}\right|
\le\frac{2}{|t-\gamma|^2}.
\]

Partition these ordinates into unit intervals at distance \(k\ge1\) from \(t\). By (1.6), their total contribution is

\[
\ll\sum_{k\ge1}\frac{\log(q(|t|+k+3))}{k^2}
\ll H_q(t),
\]

using \(|t|+k+3\le(|t|+2)(k+3)\) and the convergence of \(\sum\log(k+3)/k^2\). The removed base-point terms for nearby zeros are also \(O(H_q(t))\), because each has magnitude at most 1. The Gamma difference is \(O(\log(|t|+2))\), now on \(\Re((s+a)/2)\ge1/4\). The same series estimate used above covers this wider strip. Formula (1.4) retains precisely the pole term in the principal case. For an imprimitive character, (1.5) is \(O(\log q)\) even for \(\sigma\ge1/2\), since \(p^{1/2}-1\ge\sqrt2-1\). This proves (1.7). \(\square\)

## 2. Euler-product positivity

Write \(D_\chi(s)=-\Re(L'/L)(s,\chi)\). For \(\sigma>1\),

\[
D_\chi(\sigma+it)
=\sum_{n\ge1}\frac{\Lambda(n)}{n^\sigma}
\Re(\chi(n)n^{-it}).
\]

At prime powers coprime to \(q\), the number \(z=\chi(n)n^{-it}\) has modulus 1. The identity
\(3+4\Re z+\Re z^2=2(1+\Re z)^2\ge0\)
therefore gives

\[
0\le3D_{\chi_0}(\sigma)
+4D_\chi(\sigma+it)+D_{\chi^2}(\sigma+2it).
\tag{2.1}
\]

At nonunits every character term is zero, so the identity remains valid. All series converge absolutely.

For a real character, \(1+\chi(n)\ge0\) gives a second inequality:

\[
0\le-\frac{\zeta'}\zeta(\sigma)
-\frac{L'}L(\sigma,\chi).
\tag{2.2}
\]

For two real characters induced to a common modulus \(Q\),
\((1+\chi_1(n))(1+\chi_2(n))\ge0\) at its units, and the zeta term alone is positive at its nonunits. Consequently

\[
0\le-\frac{\zeta'}\zeta(\sigma)
-\frac{L'}L(\sigma,\chi_1)
-\frac{L'}L(\sigma,\chi_2)
-\frac{L'}L(\sigma,\chi_1\chi_2).
\tag{2.3}
\]

These are inequalities for logarithmic derivatives. Their positive coefficients allow us to insert the upper bounds of Lemma 1.1 and retain any chosen zeros with their negative signs.

## 3. Why the exception must be real and simple

Choose an absolute effective \(C_0\ge1\) large enough to dominate the combined error terms from Lemma 1.1 in each application of (2.1)–(2.3). We may use the same \(C_0\) because
\(H_q(2t)\le2H_q(t)\) and the common modulus in (2.3) is at most \(q_1q_2\). Put

\[
a_0=\min\left\{\frac1{100},\frac1{100C_0}\right\},
\qquad b_0=\frac{a_0}{100}.
\tag{3.1}
\]

These constants are auxiliary proof parameters. We will decrease the final region constant again when combining uniqueness with the zeta region.

**Proposition 3.1.** If a nonprincipal character modulo \(q\) has a zero

\[
\rho=\beta+i\gamma,\qquad
\beta\ge1-\frac{b_0}{H_q(\gamma)},
\tag{3.2}
\]

then the character is real and \(\gamma=0\). Within the corresponding real interval it has at most one zero, counted with multiplicity.

**Proof.** Set \(H=H_q(\gamma)\),
\(\sigma=1+a_0/H\), and \(\delta=1-\beta>0\).
The strict inequality \(\delta>0\) follows from the earlier nonvanishing on the line 1. Condition (3.2) gives
\(\sigma-\beta\le(a_0+b_0)/H\).

Suppose first that \(\chi\) is complex, so \(\chi^2\ne\chi_0\). In (2.1) retain \(\rho\) in the middle term and discard all other zero kernels. Lemma 1.1 gives

\[
0\le\frac3{\sigma-1}-\frac4{\sigma-\beta}+C_0H
\le H\left(\frac3{a_0}-\frac4{a_0+b_0}+C_0\right)<0.
\tag{3.3}
\]

The final sign holds because \(b_0=a_0/100\) and \(C_0a_0\le1/100\). This contradiction excludes every such complex-character zero, including real ones.

Now suppose that \(\chi\) is real. Its square is principal, so there is an additional possible pole contribution

\[
\Re\frac1{\sigma-1+2i\gamma}
=\frac{\sigma-1}{(\sigma-1)^2+4\gamma^2}.
\]

If \(|\gamma|\ge a_0/(2H)\), this is at most
\(1/(2(\sigma-1))=H/(2a_0)\). In place of (3.3) we then have

\[
0\le H\left(\frac{7}{2a_0}
-\frac4{a_0+b_0}+C_0\right)<0,
\tag{3.4}
\]

again impossible.

It remains to consider \(0<|\gamma|<a_0/(2H)\). A real character also has the distinct conjugate zero \(\overline\rho\). Use (2.2), evaluated at the real point \(\sigma\), and keep both zeros. Their combined kernel there is

\[
\frac{2(\sigma-\beta)}{(\sigma-\beta)^2+\gamma^2}
\ge\frac{2a_0H}{(a_0+b_0)^2+a_0^2/4}
>\frac{3H}{2a_0}.
\tag{3.5}
\]

The numerator bound uses \(\sigma-\beta\ge a_0/H\), while the denominator bound uses \(\sigma-\beta\le(a_0+b_0)/H\) and the small-height condition. Since \(H_q(0)\le H\), (2.2) and Lemma 1.1 imply
\(0\le H/a_0-3H/(2a_0)+C_0H<0\).
Thus \(\gamma=0\).

Finally, if there were two real zeros in
\([1-b_0/H_q(0),1)\), allowing repetition for multiplicity, use
\(\sigma=1+a_0/H_q(0)\) in (2.2). Their combined contribution is at least
\(2H_q(0)/(a_0+b_0)\). Hence

\[
0\le H_q(0)\left(\frac1{a_0}
-\frac2{a_0+b_0}+C_0\right)<0.
\]

This proves both uniqueness for that character and simplicity. \(\square\)

The small-height conjugate-pair step is essential. Bounding the principal pole simply by \(1/(\sigma-1)\) at every height would leave the coefficients \(3+1-4=0\), which cannot exclude a zero.

## 4. Landau, Page, and sparsity of conductors

**Theorem 4.1 (Landau).** There is an absolute effective \(c_L>0\) such that, if real nonprincipal characters modulo \(q_1,q_2\) are induced by different primitive characters and have real zeros \(\beta_1,\beta_2\), then

\[
\min(\beta_1,\beta_2)
\le1-\frac{c_L}{\log(q_1q_2)}.
\tag{4.1}
\]

**Proof.** The assertion is immediate if either zero is outside \((0,1)\), so consider zeros in that interval. Put \(Q=\operatorname{lcm}(q_1,q_2)\) and induce both characters to modulus \(Q\). Their primitive factors, and hence their zeros in \((0,1)\), are unchanged. The product character modulo \(Q\) is nonprincipal. Otherwise the two real characters modulo \(Q\) would coincide, and uniqueness of the inducing primitive character would contradict the hypothesis.

Let \(H=\log(q_1q_2)\) and suppose both
\(\beta_j>1-b_0/H\). Apply (2.3) at
\(\sigma=1+a_0/H\), retaining those two zeros. The zeta function has the only principal pole, and the product character has none. Since
\(\log(2Q)\ll H\), the definition of \(C_0\) gives

\[
0\le\frac1{\sigma-1}
-\frac1{\sigma-\beta_1}-\frac1{\sigma-\beta_2}+C_0H
\le H\left(\frac1{a_0}-\frac2{a_0+b_0}+C_0\right)<0.
\]

Taking \(c_L=b_0\) proves the claim. \(\square\)

**Corollary 4.2 (Page).** For some absolute effective \(c_P>0\), among all real primitive characters of conductor at most \(Q\ge3\), at most one has a real zero

\[
\beta>1-\frac{c_P}{\log Q}.
\tag{4.2}
\]

**Proof.** If two distinct such characters existed, their conductor product would be at most \(Q^2\). Landau gives
\(1-\min(\beta_1,\beta_2)\ge c_L/(2\log Q)\).
Choose \(c_P=c_L/2\); this contradicts (4.2). \(\square\)

**Corollary 4.3 (rapid conductor growth).** Given \(A>1\), choose
\(0<c<c_L/(A+1)\). If distinct primitive real characters of increasing conductors \(q_j\) have zeros
\(\beta_j>1-c/\log q_j\), then

\[
q_{j+1}>q_j^A.
\tag{4.3}
\]

**Proof.** If \(q_{j+1}\le q_j^A\), both zero distances are less than \(c/\log q_j\), whereas Landau requires at least one to be at least
\(c_L/((A+1)\log q_j)\). The choice of \(c\) contradicts this. \(\square\)

The word “conductor” matters. Multiples of one conductor can carry induced copies of the same exceptional character; Landau's hypothesis excludes that repetition. Sparsity refers to distinct inducing primitive characters, not to every modulus carrying a lift.

## 5. The classical product region

**Theorem 5.1.** There is an absolute effective \(c>0\) such that

\[
Z_q(s)=\prod_{\chi\bmod q}L(s,\chi)
\]

has no zero in

\[
\boxed{\sigma\ge1-\frac c{\log(q(|t|+2))},}
\tag{5.1}
\]

except possibly one simple real zero \(\beta_1<1\) of one real nonprincipal character \(\chi_1\) modulo \(q\). The principal factor has its pole at 1, which is not a zero.

**Proof.** Take \(c\le b_0\), so Proposition 3.1 excludes every nonreal zero and every complex-character zero in the region, and gives at most one simple real zero per real character. Distinct characters modulo the same \(q\) have distinct primitive inducing characters. Their simultaneous real exceptions would violate Landau if
\(c\le c_L/2\), since \(\log(q^2)=2\log q\) and
\(\log(2q)\ge\log q\).

The zeta-course classical zero-free-region theorem supplies an effective \(c_\zeta>0\) for
\(\sigma\ge1-c_\zeta/\log(|t|+2)\). If
\(c\le c_\zeta\), this excludes zeros of the principal primitive factor. Finally take \(c<\log2\), so the entire region lies in \(\sigma>0\). Extra finite Euler-factor zeros are then outside it. Choose the minimum of these positive constants, decreasing it if necessary. The preceding nonvanishing theorem gives \(\beta_1<1\). \(\square\)

For a fixed choice of \(c\), a zero in this region is called *exceptional*. The term depends on that choice. A possible sequence of Landau–Siegel zeros is more intrinsically described by distinct primitive real characters with
\((1-\beta_j)\log q_j\to0\). None of the statements here asserts that such zeros exist.

## 6. An effective power bound for the exceptional distance

**Lemma 6.1.** For a primitive nonprincipal character of conductor \(d\ge3\), uniformly on
\(1-1/\log d\le\sigma\le1\) and \(\sigma\ge1/2\),

\[
|L'(\sigma,\chi)|\ll(\log d)^2.
\tag{6.1}
\]

**Proof.** Periodicity and zero mean give
\(|\sum_{n\le u}\chi(n)|\le d\).
Truncate the Dirichlet series at \(d\), and partially sum its tail. Differentiating the finite sum contributes at most

\[
\sum_{n\le d}\frac{\log n}{n^\sigma}
\le d^{1-\sigma}\sum_{n\le d}\frac{\log n}n
\ll d^{1-\sigma}(\log d)^2.
\]

For the tail, its partial-summation representation is a boundary term of size at most \(d^{1-\sigma}\), plus
\(\sigma\int_d^\infty A(u)u^{-\sigma-1}\,du\), where \(|A(u)|\le d\). Differentiation is justified uniformly on each compact subinterval of \(\sigma>0\). Its derivative is
\(O(d^{1-\sigma}(\log d+1))\) for \(\sigma\ge1/2\), because
\(\int_d^\infty u^{-\sigma-1}\log u\,du
=d^{-\sigma}(\log d/\sigma+1/\sigma^2)\).
In the stated range \(d^{1-\sigma}\le e\). This proves (6.1). \(\square\)

**Theorem 6.2.** The possible exceptional zero in Theorem 5.1 satisfies

\[
\boxed{1-\beta_1\gg
\frac1{\sqrt q(\log q)^2},}
\tag{6.2}
\]

with an absolute effective constant.

**Proof.** Let \(\chi^*\) of conductor \(d\mid q\) induce the real exceptional character. The zero belongs to \(L(s,\chi^*)\). Decrease \(c\) in Theorem 5.1 so that
\(\beta_1\ge1/2\) and
\(\beta_1\ge1-1/\log d\); this is valid because
\(1-\beta_1\le c/\log(2q)\le c/\log d\).
By the fundamental theorem of calculus and Lemma 6.1,

\[
0<L(1,\chi^*)=\int_{\beta_1}^1L'(\sigma,\chi^*)\,d\sigma
\ll(1-\beta_1)(\log d)^2.
\tag{6.3}
\]

The preceding values-at-one lesson proves
\(L(1,\chi^*)\gg d^{-1/2}\) from the exact quadratic class-number formulas assigned to the number-fields course. Substituting that bound in (6.3) gives
\(1-\beta_1\gg d^{-1/2}(\log d)^{-2}\).
Since \(3\le d\le q\), this implies (6.2). The number-fields proof providers and their planned state are exactly those specified there; no ineffectivity enters these elementary class-number lower consequences. \(\square\)

Using instead the independently analytic lower bound from that lesson, the same argument proves, without a class-number formula,

\[
1-\beta_1\gg q^{-1/2}(\log q)^{-4}.
\tag{6.4}
\]

Its logarithmic exponent is 4: the analytic value bound already contains two logarithms, and the derivative estimate adds two more. Obtaining (6.2) by that particular analytic argument alone would incorrectly lose this distinction.

## 7. Two characters with no positive real zero

The smallest real characters illustrate why the possible exception is a qualification of a uniform theorem, rather than a zero automatically attached to each real character. For every real \(\sigma>0\), periodic summation gives

\[
L(\sigma,\chi_{-3})=
\sum_{k\ge0}\left((3k+1)^{-\sigma}-(3k+2)^{-\sigma}\right)>0,
\]

\[
L(\sigma,\chi_{-4})=
\sum_{k\ge0}\left((4k+1)^{-\sigma}-(4k+3)^{-\sigma}\right)>0.
\tag{7.1}
\]

Each summand is positive. The grouped series converges absolutely, because the mean value theorem bounds its terms by \(O_\sigma((k+1)^{-\sigma-1})\). Its sum is the periodically grouped Dirichlet series, whose ordinary convergence for \(\sigma>0\) was already proved. Thus neither L-function has any positive real zero, not just a zero in the displayed interval.

Independent evaluations give the following sample values; the exact positivity in (7.1) proves the assertion throughout the interval.

| \(\sigma\) | \(L(\sigma,\chi_{-3})\) | \(L(\sigma,\chi_{-4})\) |
|---|---:|---:|
| 0.5 | 0.480867557697 | 0.667691457190 |
| 0.6 | 0.507596088922 | 0.694887059109 |
| 0.7 | 0.533339000749 | 0.720161443687 |
| 0.8 | 0.558087597416 | 0.743607836658 |
| 0.9 | 0.581839895751 | 0.765321456756 |
| 1.0 | 0.604599788078 | 0.785398163397 |

The final row agrees with \(\pi/(3\sqrt3)\) and \(\pi/4\).

## 8. Wider regions at large height

The sharper height dependence comes from cancellation in logarithmic exponential sums. We use the uniform shifted-sum estimate already provided in Growth bounds and wider zero-free regions, Section 3, equation (3.1): for integers \(M\ge2\), real \(t\ge M\), and \(0<u\le1\), every partial sum on \([M,2M]\) satisfies

\[
\left|\sum_{M\le m\le R}(m+u)^{-it}\right|
\le C M\exp\left(-c\frac{(\log M)^3}{(\log t)^2}\right),
\qquad M<R\le2M,
\tag{8.1}
\]

with absolute \(C,c>0\). This is the exact Vinogradov prerequisite of that existing zeta-course lesson, including every \(1\le\lambda=\log t/\log M<\infty\) and every shift. It supplies Chiara Bellotti's published article, *Explicit bounds for the Riemann zeta function and a new zero-free region*, Theorem 1.5 and Sections 2–4. The unchanged published article retains its attribution, references and [CC BY 4.0 licence](https://creativecommons.org/licenses/by/4.0/). Its proof invokes earlier mean-value lemmas and Ford's analysis for \(\lambda\le84\); full support for those antecedents remains a planned prerequisite of the owning zeta lesson, rather than a proof supplied here by the licence alone. The uniform shift parameter is essential: an unshifted estimate would not cover residue classes modulo \(q\). We prove the character reduction, growth estimate, disc estimate and wider region below from this precise internal input.

### Truncation and the character growth bound

Put \(\tau=|t|+4\), \(\Delta=\max(0,1-\sigma)\), and

\[
G_\chi(s)=L(s,\chi)-\frac{\mathbf1_{\chi=\chi_0}\varphi(q)/q}{s-1}.
\]

The pole-subtracted function is holomorphic at 1. The principal indicator concerns the character modulo \(q\), rather than just the primitive conductor.

**Lemma 8.1 (a short Hurwitz truncation).** Uniformly for \(1/2\le\sigma\le2\), \(t\ge3\), \(K=\lfloor t\rfloor\), and \(0<u\le1\),

\[
\zeta(s,u)=\sum_{m=0}^{K-1}(m+u)^{-s}
+\frac{(K+u)^{1-s}}{s-1}+O(K^{-\sigma}).
\tag{8.2}
\]

**Proof.** Euler summation, first on finite intervals and then by continuation from \(\sigma>1\), gives

\[
\zeta(s,u)=\sum_{m=0}^{K-1}(m+u)^{-s}
+\frac{(K+u)^{1-s}}{s-1}
+\frac12(K+u)^{-s}
-s\int_K^\infty B_1(v)(v+u)^{-s-1}\,dv,
\]

where \(B_1(v)=\{v\}-1/2\). The integral converges absolutely for \(\sigma>0\); this is also the first-order Euler continuation proved in the functional-equation lesson's Hurwitz section. We need a stronger bound than taking its absolute value.

Its nonzero Fourier coefficients are \(-1/(2\pi i k)\). For each integer \(k\ne0\), the phase of
\((v+u)^{-it}e(kv)\) has derivative \(2\pi k-t/(v+u)\). On \(v\ge K\), \(t/K\le3/2\), so this derivative has constant sign, is monotone, and has magnitude at least \(4|k|\). Integration by parts, with the decreasing amplitude \((v+u)^{-\sigma-1}\), therefore gives

\[
\left|\int_K^\infty(v+u)^{-\sigma-1-it}e(kv)\,dv\right|
\ll K^{-\sigma-1}/|k|.
\]

Here the boundary term at infinity vanishes, and the total variation of the amplitude equals its initial value. The integral of the derivative of the reciprocal phase derivative is at most a constant times \(1/|k|\), by monotonicity. Thus the constant is uniform in \(u,\sigma,t\).

For a precise use of the Fourier series, first multiply its coefficients by \(r^{|k|}\), \(0<r<1\). These Poisson averages of the bounded sawtooth have absolute value at most \(1/2\) and converge almost everywhere to \(B_1\). Dominated convergence applies to the original integral. The estimates of the individual integrals have the summable majorant \(C K^{-\sigma-1}/k^2\) after multiplication by the Fourier coefficient. Consequently the integral is \(O(K^{-\sigma-1})\). Since \(|s|\ll K\), its contribution after multiplication by \(s\) is \(O(K^{-\sigma})\), as is the half endpoint term. This proves (8.2). \(\square\)

**Theorem 8.2 (uniform character growth).** There are absolute \(A,B>0\) such that every character modulo \(q\ge1\) satisfies, uniformly for \(\sigma\ge1/2\),

\[
|G_\chi(\sigma+it)|
\le A q^\Delta\log(2q)(\log\tau)^{2/3}
\tau^{B\Delta^{3/2}}.
\tag{8.3}
\]

**Proof.** First take \(t\ge3\) and \(1/2\le\sigma\le1\). Grouping the Dirichlet series into residue classes and then continuing gives
\(L(s,\chi)=q^{-s}\sum_{a=1}^q\chi(a)\zeta(s,a/q)\). Apply Lemma 8.1. The finite sums combine exactly into
\(\sum_{n\le qK}\chi(n)n^{-s}\). In the integral terms, replace \((K+a/q)^{1-s}/(s-1)\) by \(K^{1-s}/(s-1)\): their differences are
\(-\int_K^{K+a/q}v^{-s}\,dv\), of modulus at most \(K^{-\sigma}\). The common term has coefficient
\(\sum_a\chi(a)=\mathbf1_{\chi=\chi_0}\varphi(q)\). After subtracting the pole in \(G_\chi\), its remaining modulus is bounded by

\[
\frac{\varphi(q)}q\frac{|(qK)^{1-s}-1|}{|s-1|}
\ll q^{1-\sigma},
\]

because \(|s-1|\ge t\), \(K\le t\), and \(1-\sigma\le1/2\). The other errors total \(O(q^{1-\sigma}K^{-\sigma})\). Hence

\[
G_\chi(s)=\sum_{n\le qK}\chi(n)n^{-s}+O(q^{1-\sigma}).
\tag{8.4}
\]

The terms \(n\le2q\) contribute at most \(Cq^{1-\sigma}\log(2q)\), by writing \(n^{-\sigma}\le(2q)^{1-\sigma}/n\). Divide the rest into blocks with starting point \(N=qM\), \(M=2^j\ge2\). For each unit \(a\bmod q\), write \(n=qm+a\), so its phase is \(q^{-it}(m+a/q)^{-it}\). Estimate (8.1) bounds the partial unweighted sum for that residue class by
\(CM\exp(-c(\log M)^3/(\log t)^2)\). A cutoff containing just its first term is covered too: its modulus is 1, and \(M\le t\) implies that the displayed bound is at least a fixed positive multiple of 1. Sum over the at most \(q\) residue classes. Every partial character sum with this phase on the block is therefore bounded by

\[
CN\exp\left(-c\frac{(\log M)^3}{(\log t)^2}\right).
\]

Partial summation against \(n^{-\sigma}\) makes its weighted contribution at most
\(Cq^{1-\sigma}\exp(\delta v-cv^3/l^2)\), where \(\delta=1-\sigma\), \(v=\log M\) and \(l=\log t\). Elementary maximization gives
\(\delta v-(c/2)v^3/l^2\le C\delta^{3/2}l\). Keep the other half of the negative cubic. The remaining sum is bounded by

\[
\sum_{j\ge1}\exp\big(-c'(j/l^{2/3})^3\big)
\ll l^{2/3},
\]

by comparison with its convergent integral. This proves (8.3) on \(1/2\le\sigma\le1\) at positive large heights. Conjugating the character covers negative heights. At bounded heights the same Hurwitz representation and a fixed Euler truncation give \(O(q^{1-\sigma}\log(2q))\) after removal of the pole: the only small shift term is \((a/q)^{-s}\), and the remainder is uniformly bounded for \(0<a/q\le1\) on the fixed compact strip. For the principal character, the change of the common Hurwitz pole coefficient leaves \((\varphi(q)/q)(q^{1-s}-1)/(s-1)\); writing its quotient as \(-\int_0^{\log q}e^{(1-s)v}\,dv\) bounds it by \(q^{1-\sigma}\log q\), including the removable value at 1.

On \(\sigma=1\) we have the bound in (8.3) with \(\Delta=0\); on \(\sigma=2\) absolute convergence and the removed pole give the same bound. The strip interpolation theorem proved in Growth in the critical strip: convexity and the Lindelöf hypothesis, Theorem 2.1, applies to \(G_\chi\), with both boundary powers zero and logarithmic power \(2/3\). Its fixed-character polynomial growth follows also from the continuation and convexity already proved in our functional-equation lesson. The resulting estimate is uniform: the boundary constants are the displayed absolute constant times \(\log(2q)\), and the strip theorem introduces no further \(q\)-dependent constant. This gives (8.3) for \(1\le\sigma\le2\). For \(\sigma\ge2\), use absolute convergence directly. \(\square\)

### From growth to a logarithmic derivative on a small disc

We use the fully proved disc lemma in Growth bounds and wider zero-free regions, Theorem 1.1. If \(f\) is holomorphic on the closed disc of radius \(\Upsilon\) about \(s_0\), \(f(s_0)\ne0\), and \(M_f\) bounds its modulus, then on a smaller disc of radius \(r<R<\Upsilon\),

\[
\frac{f'}f(s)=\sum_{|\rho-s_0|\le R}\frac1{s-\rho}
+O\left(\frac{\log(M_f/|f(s_0)|)}{(R-r)\log(\Upsilon/R)}\right).
\tag{8.5}
\]

Zeros are repeated with their multiplicity, and poles cancel at the displayed zeros. This exact statement includes its proof and an absolute constant in that existing lesson.

Let \(t\ge2\), and define

\[
\begin{gathered}
x=\log(2q),\qquad l=\log(2t+6),\qquad H=\log(x+l+3),\\
V=\frac18\min\{1,(H/l)^{2/3}\},\qquad
D=x+l^{2/3}\big(\log(l+3)\big)^{1/3}.
\end{gathered}
\tag{8.6}
\]

Take discs of radius \(\Upsilon=V/2\) about \(s_j=1+\Upsilon/4+ijt\), \(j=1,2\). They are pole-free, including for the principal character. Their real parts exceed \(1-V\), and their heights lie between 1 and \(2t+1\). Applying (8.3) and adding back the bounded principal pole term gives

\[
\log\max_{|s-s_j|\le\Upsilon}|L(s,\psi)|
\le C(Vx+H+V^{3/2}l)\le C(Vx+H)
\]

for every character \(\psi\bmod q\). At the centre the absolutely convergent reciprocal Euler product gives
\(|L(s_j,\psi)|^{-1}\le\zeta(1+\Upsilon/4)\le1+4/\Upsilon\). Its logarithm is \(O(H)\), since \(\log(1/V)\ll H\). Thus the numerator in (8.5) is \(O(Vx+H)\).

Apply that lemma with \(r=\Upsilon/3\), \(R=\Upsilon/2\). Its error is

\[
O(x+H/V)=O(D).
\tag{8.7}
\]

Here are the uniform comparisons, including very large \(q\). The definition of \(V\) gives
\(H/V\le8H+8l^{2/3}H^{1/3}\). If \(x\le l^2\), then \(H\ll\log(l+3)\), which proves the bound by \(CD\). If \(x>l^2\), then \(H\ll\log(3x)\), \(H\ll x\), and
\(l^{2/3}H^{1/3}\ll(x\log(3x))^{1/3}\ll x\). This proves (8.7) in both cases. It also implies \(D\gg1/V\), since \(H>1\). Replacing \(2t+6\) by \(t+4\) and \(\log(l+3)\) by \(\log\log(t+4)\) changes these estimates only by absolute constants.

### The wider zero-free region

**Theorem 8.3 (Vinogradov–Korobov for characters).** There is an absolute effective \(c>0\) such that the character product modulo \(q\) has no zero in

\[
\sigma\ge1-
\frac{c}{\log(2q)+(\log\tau)^{2/3}(\log\log\tau)^{1/3}},
\qquad \tau=|t|+4,
\tag{8.8}
\]

apart from the possible simple real zero of a single real nonprincipal primitive inducing character already specified in Theorem 5.1. The finite Euler factors introduce no exception in this region.

**Proof.** First consider a zero \(\beta+it\) of \(L(s,\chi)\), with \(t\ge2\), and put \(d=1-\beta>0\). If \(d\ge\Upsilon/24\), the comparison \(D\gg1/V\) already gives \(d\gg1/D\). Otherwise the zero lies in the radius-\(R\) disc about \(s_1\), because \(\Upsilon/4+d<\Upsilon/3\). For \(1<\sigma\le1+\Upsilon/4\), equations (8.5)–(8.7) give

\[
-\Re\frac{L'}L(\sigma+it,\chi)
\le CD-\frac1{\sigma-\beta},
\qquad
-\Re\frac{L'}L(\sigma+2it,\chi^2)\le CD.
\tag{8.9}
\]

Every other displayed zero contributes a nonpositive real term here, since its real part is at most 1. Finite Euler-factor zeros have real part 0 and lie outside these discs. The principal pole is absent from both discs, even when \(\chi^2\) is principal.

At real \(\sigma>1\), the principal character satisfies
\(-L'/L(\sigma,\chi_0)\le-\zeta'/\zeta(\sigma)=1/(\sigma-1)+O(1)\); the omitted primes subtract positive terms. Insert this and (8.9) into the exact positivity inequality (2.1). It yields

\[
\frac4{\sigma-\beta}-\frac3{\sigma-1}\le C'D.
\]

Take \(\sigma=1+6d\), which is in the allowed interval because \(d<\Upsilon/24\). The left side is \(1/(14d)\). Hence \(d\ge c'/D\). The same argument applied to the conjugate character covers negative heights, without assuming that a complex character's zeros occur in conjugate pairs.

For \(|t|<2\), the denominator in (8.8) is comparable with \(\log(2q)\). Reduce \(c\) to make this part of the region a subset of the classical region in Theorem 5.1. Its unique possible real-character exception, simplicity and inducing-conductor qualification therefore remain exactly as stated there. The principal small moduli have no exception, by the classical zeta case already included in that theorem. Finally reduce \(c\) once more to put the whole region in \(\sigma>1/2\), away from all finite Euler-factor zeros. Taking a smaller constant turns the strict zero-distance estimate into the closed exclusion (8.8). All constants used in the shifted-sum estimate, truncation, disc lemma and positivity argument are effective. \(\square\)

The extra factor \(\log(2q)\) in (8.3) causes no extra logarithm in the final denominator. Its logarithm is absorbed into \(H\), and the two cases following (8.7) show explicitly why this remains true when the modulus dominates the height. The only exceptional zero is still the low-height real one; the wider region does not turn it into a collection of height-dependent exceptions.


For example, at a fixed modulus the height-dependent term eventually dominates, and the width is of order \((\log\tau)^{-2/3}(\log\log\tau)^{-1/3}\). If \(q\) grows with the height and \(\log q\ge (\log\tau)^{2/3}(\log\log\tau)^{1/3}\), the width instead has order \(1/\log q\). The formula covers the transition directly; no relation between \(q\) and \(t\) was imposed in the disc argument.

## 9. Exercises

1. **Easy.** Explain why a complex character cannot have a real zero sufficiently close to 1.
2. **Medium.** Prove Landau's theorem, including the hypothesis that the two inducing primitive characters differ.
3. **Medium.** Deduce Page's theorem uniformly over conductors at most \(Q\).
4. **Medium.** Prove the effective estimate \(1-\beta_1\gg q^{-1/2}(\log q)^{-2}\), specifying the value-at-one input that gives this logarithmic exponent.
5. **Hard.** Show that primitive real characters of increasing conductors \(q_j\), each with a zero \(\beta_j>1-c/\log q_j\), must satisfy \(q_{j+1}>q_j^{100}\) when \(c\) is sufficiently small. Explain why unrestricted induced moduli would require a different statement.

6. **Hard.** For \(c,l>0\) and \(\delta\ge0\), compute the maximum over \(v\ge0\) of \(\delta v-(c/2)v^3/l^2\). Deduce the character growth scale in (8.3). Then explain why the disc error is \(O(D)\) even when \(\log q\) is much larger than \((\log |t|)^2\).

## 10. Solutions

**1.** A complex character has \(\chi^2\ne\chi_0\). Set \(t=0\) in (2.1), keep a hypothetical real zero \(\beta\), and take
\(\sigma=1+a_0/\log(2q)\). If
\(1-\beta\le b_0/\log(2q)\), the upper bound is
\(\log(2q)(3/a_0-4/(a_0+b_0)+C_0)<0\), contrary to positivity. No pole from \(\chi^2\) can offset the fourth-order zero contribution.

**2.** Induce both characters to \(Q=\operatorname{lcm}(q_1,q_2)\). The product is nonprincipal precisely because different primitive inducing characters cannot become equal after induction. At unit prime powers the logarithmic derivative of
\(\zeta L(\chi_1)L(\chi_2)L(\chi_1\chi_2)\) has coefficients
\(\Lambda(n)(1+\chi_1(n))(1+\chi_2(n))\ge0\); at other prime powers only the positive zeta term remains. With
\(H=\log(q_1q_2)\) and \(\sigma=1+a_0/H\), Lemma 1.1 and two hypothetical zero distances below \(b_0/H\) yield
\(0\le H(1/a_0-2/(a_0+b_0)+C_0)<0\).
Thus at least one distance is at least \(b_0/H\), which is Landau with \(c_L=b_0\). If the inducing characters were the same, the product would be principal and contribute a second pole; this argument would no longer give a contradiction.

**3.** Two different primitive conductors \(q_1,q_2\le Q\) have
\(\log(q_1q_2)\le2\log Q\). Landau forces one zero distance to be at least \(c_L/(2\log Q)\). Taking \(c_P=c_L/2\) excludes two distances both smaller than \(c_P/\log Q\). Two different characters with the same conductor are covered as well because they remain different primitive characters.

**4.** Work at the inducing conductor \(d\), since a near-1 zero is a zero of the primitive factor. On \([\beta_1,1]\), Lemma 6.1 bounds \(|L'|\) by an absolute multiple of \((\log d)^2\). The fundamental theorem of calculus yields (6.3). The class-number consequence
\(L(1,\chi^*)\gg d^{-1/2}\) from the preceding lesson therefore gives
\(1-\beta_1\gg d^{-1/2}(\log d)^{-2}\), and \(d\le q\) gives the requested estimate. This uses the exact planned internal algebraic class-number inputs. Using only that lesson's analytic bound would give exponent 4, as in (6.4), rather than exponent 2.

**5.** Choose \(0<c<c_L/101\). If
\(q_{j+1}\le q_j^{100}\), then
\(\log(q_jq_{j+1})\le101\log q_j\), while both distances are less than \(c/\log q_j\). Landau requires one distance to be at least \(c_L/(101\log q_j)\), a contradiction. Hence \(q_{j+1}>q_j^{100}\). A single primitive character can be induced to many larger moduli without changing its near-1 zero; such repeated lifts fail Landau's distinctness hypothesis. Increasing arbitrary moduli alone does not justify the asserted sparsity.

**6.** If \(\delta=0\), the maximum is zero at \(v=0\). Otherwise differentiation gives the unique positive maximizer \(v_*=l\sqrt{2\delta/(3c)}\). The maximum is

\[
\frac{2\sqrt2}{3\sqrt{3c}}\,\delta^{3/2}l.
\]

Splitting the cubic term into two equal parts leaves this bound and the convergent sum \(\sum_{j\ge1}\exp(-c'(j/l^{2/3})^3)\ll l^{2/3}\). Multiplying by \(q^\delta\) and including the initial interval gives (8.3). For the disc, write \(x=\log(2q)\), \(H=\log(x+l+3)\). When \(x>l^2\), we have \(H\ll\log(3x)\ll x\) and \(l^{2/3}H^{1/3}\ll(x\log(3x))^{1/3}\ll x\). Thus \(x+H/V\ll x\le D\). When \(x\le l^2\), instead \(H\ll\log(l+3)\), giving the second term in \(D\). Both ranges are required for a uniform theorem with no relation between modulus and height.

## References

D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorem 12.3 and Theorem 12.5 with Corollaries 12.6–12.7, gives the product theorem, Landau's comparison and Page's consequence. The direct positive-kernel proofs, the complete two-character argument and the conductor qualification are supplied here. The wider zero-free region needs a growth bound for the characters. Section 8 supplies its character reduction, growth, local-disc and positivity proofs from the exact internal exponential-sum prerequisite. Chiara Bellotti, [*Explicit bounds for the Riemann zeta function and a new zero-free region*](https://doi.org/10.1016/j.jmaa.2024.128249), *Journal of Mathematical Analysis and Applications* 536 (2024), 128249, Theorem 1.5 and Sections 2–4, provides an explicit uniform shifted-sum treatment. The unchanged CC BY 4.0 article is linked at its existing zeta-course location; it retains its references and attribution. Its earlier mean-value and bounded-parameter antecedents are recorded there as prerequisites, rather than counted as proved by the licence.
