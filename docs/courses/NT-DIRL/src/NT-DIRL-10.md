# Siegel's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Nonvanishing says that each real character has a positive value at 1. Siegel's theorem makes those values uniformly larger than every fixed negative power of the conductor. Its constant is ineffective. The distinction comes from a precise argument: positivity controls every character except one possible character, and positivity at 1 then absorbs that last character without bounding its conductor.

Section 8 proves the effective logarithmic class-number bound separately, using elliptic curves and exact automorphic prerequisites. It includes both explicit rank certificates, full ideal and smoothed error estimates, and all ramified twisting cases.

We use conductors and real-character classification from *Dirichlet characters*, positivity at 1 from *Dirichlet's theorem on primes in arithmetic progressions*, and the class-number normalization from *Values of Dirichlet L-functions at \(s=1\)*. The analytic proof below needs no class-number formula, functional equation, or assumption about an exceptional zero's existence. Throughout, a real primitive character is nonprincipal; its conductor \(q\) is at least 3. Different primitive characters can have the same conductor.

## 1. Positive coefficients and the product character

Let \(\chi_1,\chi_2\) be different real primitive characters of conductors \(q_1,q_2\). Put \(Q=q_1q_2\), \(m=\operatorname{lcm}(q_1,q_2)\), and

\[
F(s)=\zeta(s)L(s,\chi_1)L(s,\chi_2)L(s,\chi_1\chi_2).
\tag{1.1}
\]

The last character is the pointwise product modulo \(m\), retaining its zero values at nonunits. It is nonprincipal: otherwise the two real characters would induce the same character on units modulo \(m\), and uniqueness of the primitive inducing character would imply \(\chi_1=\chi_2\).

Its primitive conductor can be smaller than \(m\). If \(\chi_{12}^*\) is its primitive inducing character, then

\[
L(s,\chi_1\chi_2)=L(s,\chi_{12}^*)
\prod_{p\mid m,\ p\nmid q_{12}^*}
(1-\chi_{12}^*(p)p^{-s}).
\tag{1.2}
\]

We retain these factors. The Dedekind zeta function of a biquadratic field uses the three *primitive* quadratic characters, so (1.1) can differ from it by finite Euler factors. Its coefficient argument does not require an identification with a number-field zeta function.

**Proposition 1.1.** In the absolutely convergent half-plane,

\[
F(s)=\sum_{n\ge1}\frac{a(n)}{n^s},\qquad
a=1*\chi_1*\chi_2*(\chi_1\chi_2),
\]

we have \(a(n)\ge0\) and \(a(1)=1\). Also

\[
G_\chi(s)=\zeta(s)L(s,\chi)
=\sum_{n\ge1}\frac{(1*\chi)(n)}{n^s}
\tag{1.3}
\]

has nonnegative coefficients and coefficient 1 at \(n=1\).

**Proof.** At a prime put \(u=\chi_1(p)\), \(v=\chi_2(p)\) and \(z=p^{-s}\). The local factor of \(F\) is

\[
\frac1{(1-z)(1-uz)(1-vz)(1-uvz)}.
\tag{1.4}
\]

For \(u=v=1\) this is \((1-z)^{-4}\). For \(u,v\in\{-1,1\}\) with at least one value \(-1\), it is \((1-z^2)^{-2}\). If exactly one value is zero, it is \((1-z)^{-2}\) when the other is 1, and \((1-z^2)^{-1}\) when the other is \(-1\). If both are zero, it is \((1-z)^{-1}\). Each listed series has nonnegative coefficients and constant coefficient 1; multiplying proves the assertion.

For \(G_\chi\), the local factors are \((1-z)^{-2}\), \((1-z^2)^{-1}\), and \((1-z)^{-1}\), according as \(\chi(p)=1,-1,0\). The same reasoning applies. \(\square\)

Both functions are holomorphic in \(\Re s>0\) except for a simple pole at 1, with positive residues

\[
\lambda_F=L(1,\chi_1)L(1,\chi_2)L(1,\chi_1\chi_2),
\qquad \lambda_G=L(1,\chi).
\tag{1.5}
\]

Earlier nonvanishing and positivity apply to the primitive real characters; the factors in (1.2) are positive at 1 and preserve that conclusion.

## 2. An elementary analytic bound

**Lemma 2.1.** For every nonprincipal character modulo \(r\), with \(A(u)=\sum_{n\le u}\chi(n)\),

\[
L(s,\chi)=\sum_{n\le r}\frac{\chi(n)}{n^s}
+s\int_r^\infty A(u)u^{-s-1}\,du
\quad(\Re s>0).
\tag{2.1}
\]

On \(|s-2|=3/2\), this gives \(|L(s,\chi)|\le9\sqrt r\). At 1,

\[
0<L(1,\chi)\le\log r+2
\tag{2.2}
\]

for a real nonprincipal character. For \(7/8\le\sigma\le1\),

\[
|L'(\sigma,\chi)|\le5r^{1-\sigma}\log^2(2r).
\tag{2.3}
\]

**Proof.** Full periods sum to zero, so \(A(r)=0\) and \(|A(u)|\le r\). Partial summation gives (2.1); its integral and differentiated integrals converge locally uniformly for \(\Re s>0\).

On the circle, \(\sigma\ge1/2\) and \(|s|\le7/2\). The finite sum is at most \(2\sqrt r\) in magnitude, and the tail at most
\(|s|r^{1-\sigma}/\sigma\le7\sqrt r\).
At 1 the two contributions are at most \(1+\log r\) and 1.

The finite differentiated sum for real \(\sigma\) is bounded by
\(r^{1-\sigma}\log r(1+\log r)\).
Differentiating the integral bounds its derivative by
\(r^{1-\sigma}(\log r+2/\sigma)\).
Their sum is at most \(5r^{1-\sigma}\log^2(2r)\) for \(r\ge3\). This generous constant covers the whole stated interval. \(\square\)

We also have

\[
\zeta(s)=\frac{s}{s-1}
-s\int_1^\infty\{u\}u^{-s-1}\,du
\quad(\Re s>0,\ s\ne1).
\tag{2.4}
\]

For \(\Re s>1\), partial summation with \(\lfloor u\rfloor=u-\{u\}\) proves this identity. The remaining integral converges locally uniformly for \(\Re s>0\), proving the continuation. On \(|s-2|=3/2\), the distance to 1 is at least \(1/2\), and (2.4) gives \(|\zeta(s)|\le14\). Both terms are negative when \(0<s<1\) is real, so

\[
\zeta(\sigma)<0\quad(0<\sigma<1).
\tag{2.5}
\]

## 3. The key inequality from a Taylor series

**Lemma 3.1.** An absolute effective \(C\), for which \(C=200\) suffices below, satisfies, for \(7/8<\beta<1\) and \(\delta=1-\beta\),

\[
F(\beta)\ge\frac12-C\frac{\lambda_F}{\delta}Q^{4\delta}.
\tag{3.1}
\]

For a single real nonprincipal character modulo \(q\),

\[
G_\chi(\beta)\ge\frac12
-C\frac{L(1,\chi)}{\delta}q^{4\delta}.
\tag{3.2}
\]

**Proof.** Write \(P=F\) or \(G_\chi\), let \(\lambda\) be its residue, and take \(V=Q\) or \(q\), respectively. Absolute differentiation of the nonnegative Dirichlet series at 2 gives

\[
P(s)=\sum_{j\ge0}b_j(2-s)^j,\qquad
b_j=\frac1{j!}\sum_{n\ge1}\frac{a(n)(\log n)^j}{n^2}\ge0,
\quad b_0\ge1,
\tag{3.3}
\]

initially for \(|s-2|<1\). For \(G\), use its own coefficients. The function
\(H(s)=P(s)-\lambda/(s-1)\)
is holomorphic on the closed disk of radius \(3/2\) about 2. Its coefficients are \(b_j-\lambda\), because \(1/(s-1)=\sum_{j\ge0}(2-s)^j\) in the smaller disk.

On the circle, Lemma 2.1 bounds \(F\) by

\[
14\cdot9^3\sqrt{q_1q_2m}\le10206Q.
\]

Since \(\log r+2\le2\sqrt r\) for \(r\ge1\), we also have \(\lambda_F\le8Q\); its pole term has magnitude at most \(16Q\). Thus \(|H|\le11000V\). The same bound covers \(G\): its circle bound is \(126\sqrt q\), and its pole term at most \(4\sqrt q\).

Cauchy's coefficient formula gives

\[
|b_j-\lambda|\le11000V(2/3)^j.
\tag{3.4}
\]

Choose

\[
N=\left\lceil\frac{\log(88000V)}{\log(4/3)}\right\rceil.
\]

For \(z=2-\beta=1+\delta<9/8\), the tail starting at \(N\) is at most

\[
11000V\sum_{j\ge N}(2z/3)^j
\le44000V(3/4)^N\le\frac12.
\tag{3.5}
\]

In the finite part use \(b_0\ge1\) and \(b_j\ge0\). The pole at \(\beta\) contributes \(-\lambda/\delta\), giving

\[
\begin{aligned}
P(\beta)
&\ge1-\lambda\sum_{j=0}^{N-1}z^j
-\frac{\lambda}{\delta}-\frac12\\
&=\frac12-\frac{\lambda}{\delta}z^N.
\end{aligned}
\tag{3.6}
\]

Finally \(N\le41+4\log V\), whence

\[
z^N\le e^{\delta N}
\le e^{41/8}V^{4\delta}<200V^{4\delta}.
\]

This proves both inequalities. The series evaluated across the pole is the Taylor series of \(H\), not the original Taylor series of \(P\). \(\square\)

The important feature is \(V^{C\delta}\): its exponent becomes arbitrarily small when a real zero approaches 1.

## 4. An effective bound with at most one exception

**Theorem 4.1.** For every \(\varepsilon>0\) there is an effectively computable \(c_{\mathrm{eff}}(\varepsilon)>0\) such that

\[
L(1,\chi)>c_{\mathrm{eff}}(\varepsilon)q^{-\varepsilon}
\tag{4.1}
\]

for all real primitive nonprincipal characters, with at most one exceptional character. That possible exception depends on \(\varepsilon\); no bound for its conductor is asserted.

This is a qualitative effective one-exception form associated with Siegel–Tatuzawa. Tatuzawa's original paper gives much sharper numerical constants. The assertion (4.1), its effectivity, and its full conductor range are proved here directly.

**Proof.** It suffices to take \(0<\varepsilon\le1\); the case \(\varepsilon=1\) implies every larger-exponent assertion. Set \(\eta=\varepsilon/20\).

If a character has no real zero in \([1-\eta,1)\), its \(L\)-function is positive there: it is positive at 1 and cannot change sign without a zero. Thus \(G_\chi(1-\eta)<0\) by (2.5). Inequality (3.2) gives

\[
L(1,\chi)>\frac{\eta}{2C}q^{-4\eta}
\ge\frac{\eta}{2C}q^{-\varepsilon}.
\tag{4.2}
\]

If no primitive character has a zero in that interval, this proves the theorem without an exception.

Otherwise select a character \(\chi_1\) of smallest conductor \(q_1\) among those having such a zero, breaking any finite tie in a fixed way. Choose \(\beta_1\in[1-\eta,1)\) with \(L(\beta_1,\chi_1)=0\), and put \(\delta=1-\beta_1\), so \(0<\delta\le\eta\). Characters of conductor \(q<q_1\) are already covered by (4.2).

For a character \(\chi\ne\chi_1\) of conductor \(q\ge q_1\), use (1.1) with \(\chi_2=\chi\). Since \(F(\beta_1)=0\), (3.1) implies

\[
\lambda_F\ge\frac{\delta}{2C}(q_1q)^{-4\delta}.
\tag{4.3}
\]

The fundamental theorem of calculus and (2.3) give

\[
L(1,\chi_1)\le5\delta q_1^\delta\log^2(2q_1).
\tag{4.4}
\]

The product character has modulus \(m\le q_1q\le q^2\), so (2.2) gives \(L(1,\chi_1\chi)\le3\log(2q)\). Divide (4.3) by these upper bounds:

\[
L(1,\chi)\ge\frac1{30C}q^{-9\delta}\log^{-3}(2q)
\ge\frac1{30C}q^{-9\eta}\log^{-3}(2q).
\tag{4.5}
\]

This constant is independent of \(q_1\): minimality gave \(q_1\le q\), and the factor \(\delta\) canceled.

Maximizing \(y^3e^{-\varepsilon y/2}\) for \(y\ge0\) gives its maximum \((6/(e\varepsilon))^3\). With \(y=\log(2q)\), this proves

\[
\log^{-3}(2q)\ge
2^{-\varepsilon/2}(e\varepsilon/6)^3q^{-\varepsilon/2}.
\tag{4.6}
\]

As \(9\eta+\varepsilon/2=19\varepsilon/20<\varepsilon\), (4.5) implies (4.1). Any positive constant smaller than

\[
\min\left\{\frac{\eta}{2C},
\frac{2^{-\varepsilon/2}(e\varepsilon/6)^3}{30C}\right\}
\tag{4.7}
\]

covers both cases. Only \(\chi_1\) remains untreated. All constants used in (4.7) are explicit. \(\square\)

## 5. Absorbing the possible exception

**Theorem 5.1 (Siegel).** For every \(\varepsilon>0\) there is \(c(\varepsilon)>0\) such that

\[
\boxed{L(1,\chi)>c(\varepsilon)q^{-\varepsilon}}
\tag{5.1}
\]

for every real primitive nonprincipal character. This proof does not effectively compute \(c(\varepsilon)\).

**Proof.** Apply Theorem 4.1. If it has no exception, take a smaller constant than \(c_{\mathrm{eff}}(\varepsilon)\). Otherwise \(L(1,\chi_1)>0\) by nonvanishing, and

\[
c(\varepsilon)=\frac12\min\left\{
c_{\mathrm{eff}}(\varepsilon),
q_1^\varepsilon L(1,\chi_1)\right\}>0
\tag{5.2}
\]

handles every character including \(\chi_1\). \(\square\)

The finite formula in the values-at-one lesson computes \(L(1,\chi_1)\) once the character is specified. The ineffective step is the uniform selection in (5.2): this proof gives no bound for \(q_1\), nor a finite test deciding that no such character exists. A conductor search terminates if a chosen near-1 zero exists, but supplies no terminating certificate when it does not. This explains this proof's ineffectivity, without asserting that every conceivable effective improvement is logically impossible.

**Theorem 5.2 (real zero-free form).** For every \(\varepsilon>0\) there is \(c_0(\varepsilon)>0\) such that, for real \(\sigma\),

\[
L(\sigma,\chi)\ne0
\quad\text{if}\quad
\sigma>1-c_0(\varepsilon)q^{-\varepsilon},
\tag{5.3}
\]

for every real primitive nonprincipal character. The family of assertions (5.3) is equivalent to (5.1).

**Proof of (5.1) implying (5.3).** The Euler product excludes real zeros above 1, and nonvanishing excludes 1. If a zero \(\beta<1\) has \(\delta=1-\beta\ge1/\log(2q)\), then \(\delta\gg_\varepsilon q^{-\varepsilon}\), effectively: \(q^{-\varepsilon}\log(2q)\) has a finite computable supremum. Zeros below \(7/8\) also obey the claimed bound after decreasing its constant.

For a closer zero with \(\beta\ge7/8\), (2.3) gives

\[
L(1,\chi)\le5e\delta\log^2(2q).
\]

Apply (5.1) with exponent \(\varepsilon/2\) and absorb two logarithms into \(q^{\varepsilon/2}\). Then \(\delta\gg_\varepsilon q^{-\varepsilon}\), as required.

**Proof of the converse.** Assume (5.3) for a given \(\varepsilon\). Choose \(0<a\le1/16\) with \(a<c_0(\varepsilon)\), put \(\delta=aq^{-\varepsilon}\), and set \(\beta=1-\delta\). Positivity at 1 and (5.3) give \(L(\beta,\chi)>0\), hence \(G_\chi(\beta)<0\). By (3.2),

\[
L(1,\chi)>\frac{a}{2C}q^{-\varepsilon}q^{-4aq^{-\varepsilon}}.
\]

Since \(q^{-\varepsilon}\log q\le1/(e\varepsilon)\), the final factor is at least \(\exp(-4a/(e\varepsilon))>0\), proving (5.1). \(\square\)

This assertion concerns the *real axis*. The classical region has additional height dependence; (5.3) does not assert a full vertical zero-free strip of fixed width.

**Corollary 5.3.** Both the real-axis zero-free assertion and \(L(1,\chi)\gg_\varepsilon q^{-\varepsilon}\) remain valid for all real nonprincipal characters modulo \(q\), including imprimitive characters.

**Proof.** Let the primitive conductor be \(d\mid q\). Extra Euler factors have zeros only on \(\Re s=0\). Taking \(c_0(\varepsilon)\le1/2\), the asserted interval lies in \(\sigma>0\), where the primitive assertion at \(d\) applies since \(d^{-\varepsilon}\ge q^{-\varepsilon}\).

For the value, use the primitive bound with exponent \(\varepsilon/2\) and

\[
L(1,\chi)\ge L(1,\chi^*)\prod_{p\mid q}(1-1/p).
\]

For any \(\alpha>0\) this product is at least an effective \(c_\alpha q^{-\alpha}\). Choose an effective \(P_\alpha\) so that \(1-1/p\ge p^{-\alpha}\) for \(p>P_\alpha\); the smaller primes contribute a positive finite constant and \(\prod_{p\mid q}p\le q\). Take \(\alpha=\varepsilon/2\) and use \(d\le q\). \(\square\)

## 6. Imaginary quadratic class numbers

For a negative fundamental discriminant \(D\), write \(h(D)\) for the ideal class number of \(\mathbb Q(\sqrt D)\), and \(w_D\) for its number of roots of unity. The exact formula from the values-at-one lesson is

\[
L(1,\chi_D)=\frac{2\pi h(D)}{w_D\sqrt{|D|}},
\qquad w_{-3}=6,\quad w_{-4}=4,\quad w_D=2\ (D<-4).
\tag{6.1}
\]

Its exact algebraic inputs are the residue formula in the number-fields lesson *The Dedekind zeta function and the analytic class number formula*, and the primitive-character factorization in *Abelian number fields and Dirichlet L-functions at \(s=1\)*. These are existing planned lessons; their precise statements, already specified in the values-at-one lesson, are the inputs. Their use is independent of the analytic proof of Siegel's theorem above.

**Corollary 6.1.** For every \(\varepsilon>0\),

\[
\boxed{h(D)\gg_\varepsilon |D|^{1/2-\varepsilon}}
\quad(D<0\text{ fundamental}),
\tag{6.2}
\]

with an ineffective constant. In particular \(h(D)\to\infty\) as \(D\to-\infty\) through fundamental discriminants.

**Proof.** The conductor of \(\chi_D\) is \(|D|\), and (6.1) gives

\[
h(D)=\frac{w_D}{2\pi}\sqrt{|D|}L(1,\chi_D)
>\frac{c(\varepsilon)}{\pi}|D|^{1/2-\varepsilon}.
\]

Take, for example, \(\varepsilon=1/4\) for the final conclusion. \(\square\)

For each fixed \(\varepsilon>0\), only finitely many such fields satisfy

\[
h(D)<|D|^{1/2-\varepsilon}.
\tag{6.3}
\]

Indeed apply (6.2) with \(\varepsilon/2\), and put \(c'=c(\varepsilon/2)/\pi\). Inequality (6.3) forces \(c'|D|^{\varepsilon/2}<1\), hence \(|D|<(c')^{-2/\varepsilon}\). This is a finite but ineffective bound.

## 7. Nine directly computed examples

Reduced positive definite primitive forms \((a,b,c)\) of discriminant \(D=b^2-4ac<0\) obey

\[
|b|\le a\le c,\qquad
b\ge0\ \text{if }|b|=a\text{ or }a=c.
\tag{7.1}
\]

They satisfy \(1\le a\le\sqrt{|D|/3}\), since \(|D|=4ac-b^2\ge3a^2\). The planned number-fields lesson *Quadratic fields: ideal classes and binary quadratic forms* proves that these forms represent each proper class exactly once; their count for a negative fundamental discriminant is the ideal class number.

For each \(a\) in this finite range, test \(-a\le b\le a\), require \(b^2\equiv D\pmod{4a}\), and put \(c=(b^2-D)/(4a)\). Test (7.1) and \(\gcd(a,b,c)=1\). Exact enumeration gives these complete lists at the nine displayed discriminants. Independently, the finite character formula of the values-at-one lesson checks the last column.

| \(D\) | Reduced forms | \(h(D)\) | \(\sqrt{\lvert D\rvert}\) | \(L(1,\chi_D)\) |
|---:|---|---:|---:|---:|
| \(-3\) | \((1,1,1)\) | 1 | 1.732051 | 0.604599788078 |
| \(-4\) | \((1,0,1)\) | 1 | 2.000000 | 0.785398163397 |
| \(-7\) | \((1,1,2)\) | 1 | 2.645751 | 1.187410411724 |
| \(-8\) | \((1,0,2)\) | 1 | 2.828427 | 1.110720734540 |
| \(-11\) | \((1,1,3)\) | 1 | 3.316625 | 0.947225825099 |
| \(-19\) | \((1,1,5)\) | 1 | 4.358899 | 0.720730784146 |
| \(-43\) | \((1,1,11)\) | 1 | 6.557439 | 0.479088388240 |
| \(-67\) | \((1,1,17)\) | 1 | 8.185353 | 0.383806628883 |
| \(-163\) | \((1,1,41)\) | 1 | 12.767145 | 0.246068527553 |

Here \(h(D)/\sqrt{|D|}=1/\sqrt{|D|}\), which can be small before the asymptotic conclusion forces growth. These finite calculations prove class number one at the nine inputs. They do not exclude every other discriminant.

The global classification is the exact theorem assigned to the existing transcendence-course lesson *Class numbers II: class number one and two*: the nine negative fundamental discriminants in the table are the only ones of class number one. Its planned proof must include both the effective upper bound and the complete exclusion of the remaining finite range. That separate global exclusion is not inferred from this table or used to prove Siegel's theorem.

## 8. Effective class-number growth

The effective one-exception theorem leaves an unknown single field. Goldfeld's work combined with Gross–Zagier removes that obstruction by using elliptic-curve \(L\)-functions. A usual form of the resulting unconditional bound is

\[
h(D)\ge C_\varepsilon(\log|D|)^{1-\varepsilon}
\quad(D<0\text{ fundamental}),
\tag{8.1}
\]

where \(C_\varepsilon>0\) is effective. This growth scale is weaker than (6.2), but an effective version supplies a computable finite search bound for any prescribed class number.

### 8.1. A curve with two independent rational points

The analytic argument needs a particular elliptic-curve \(L\)-function with a zero of order at least three at its centre. We will use

\[
E:\quad y^2+y=x^3-7x+6,
\qquad P=(1,0),\quad Q=(2,0).
\tag{8.2}
\]

The identity element is the point at infinity, denoted by \(O\), and \(-(x,y)=(x,-1-y)\). The chord and tangent group law, including associativity, follows from the full uniformization proof in *Complex tori and elliptic curves*, Theorems 2.3 and 3.1. Restrict its rational chord and tangent formulas to \(E(\mathbf Q)\). We give the height argument and the arithmetic certificates needed here in full. In particular, an apparent pair of rational points or a numerical approximation to an \(L\)-derivative will not serve as the rank argument.

For a rational projective coordinate \([X:Z]\), choose coprime integers \(X,Z\) and put

\[
h([X:Z])=\log\max(|X|,|Z|).
\]

Thus \(h([1:0])=0\), the value used for \(x(O)\). The tangent formula for (8.2), with slope \((3x^2-7)/(2y+1)\), gives

\[
x(2R)=[A(X,Z):B(X,Z)],
\quad
\begin{aligned}
A&=X^4+14X^2Z^2-50XZ^3+49Z^4,\\
B&=4X^3Z-28XZ^3+25Z^4,
\end{aligned}
\tag{8.3}
\]

when \(x(R)=[X:Z]\). This projective formula also covers \(R=O\) and points whose double is \(O\).

**Lemma 8.1 (an explicit height error).** On this curve,

\[
|h(x(2R))-4h(x(R))|<12.
\tag{8.4}
\]

Consequently the limit

\[
H(R)=\lim_{j\longrightarrow\infty}4^{-j}h(x(2^jR))
\tag{8.5}
\]

exists, is nonnegative, and satisfies

\[
\left|H(R)-4^{-j}h(x(2^jR))\right|\le\frac4{4^j}.
\tag{8.6}
\]

Our \(H\) is twice the usual Néron–Tate canonical height.

**Proof.** Direct multiplication verifies the two integer identities

\[
\begin{aligned}
&(448Z^3-48X^2Z)A
 +(12X^3+140XZ^2-675Z^3)B=5077Z^7,\\
&(9150Z^3-18998Z^2X+4900ZX^2+5077X^3)A\\
&\hspace{9mm}
 +(-17934Z^3+35450Z^2X-13020ZX^2-1225X^3)B
 =5077X^7.
\end{aligned}
\tag{8.7}
\]

They show both that \(A,B\) have no common projective zero in characteristic zero and that their integer common divisor \(d\), at coprime \(X,Z\), divides 5077. Set \(M=\max(|X|,|Z|)\). The coefficient sums in (8.3) give

\[
\max(|A|,|B|)\le114M^4.
\]

If \(|Z|=M\), the sum of the absolute coefficients of the two multipliers in the first identity is \(496+827=1323\). If \(|X|=M\), the corresponding sum in the second identity is \(38125+67629=105754\). Hence

\[
\max(|A|,|B|)\ge\frac{5077}{105754}M^4.
\]

After division by \(d\le5077\), the primitive coordinate of \(x(2R)\) therefore has size between \(M^4/105754\) and \(114M^4\). Taking logarithms proves (8.4), since \(\log105754<12\) and \(\log114<12\).

For \(h_j=h(x(2^jR))\), (8.4) bounds the difference between consecutive terms of \(4^{-j}h_j\) by \(12/4^{j+1}\). Its remaining geometric tail is at most \(4/4^j\). This proves convergence and (8.6). Each approximating term is nonnegative. \(\square\)

We next justify the quadratic identity that makes the finite height calculation useful.

**Lemma 8.2 (the height quadratic form).** For rational points \(R,S\),

\[
H(R+S)+H(R-S)=2H(R)+2H(S).
\tag{8.8}
\]

In particular, if

\[
b=\frac{H(P+Q)-H(P)-H(Q)}2,
\]

then for every pair of integers \(n,m\),

\[
H(nP+mQ)=n^2H(P)+2nmb+m^2H(Q).
\tag{8.9}
\]

**Proof.** Replace \(y\) by \(y+1/2\) to write the curve as
\(Y^2=x^3+a x+c\), where \(a=-7\), \(c=25/4\). If \(x(R)=[U:Z]\) and \(x(S)=[V:W]\), the two coordinates \(x(R+S),x(R-S)\) are the projective roots of the binary quadratic with coefficients

\[
\begin{aligned}
c_0&=(UW-VZ)^2,\\
c_1&=-2(UV+aZW)(UW+VZ)-4cZ^2W^2,\\
c_2&=(UV-aZW)^2-4cZW(UW+VZ).
\end{aligned}
\tag{8.10}
\]

For unequal finite \(x\)-coordinates this follows by using the two chord slopes and the identities for their sum and product. Polynomial continuation gives the formula when coordinates coincide or one point is \(O\). In these cases one or both projective roots may be infinity.

These three bihomogeneous polynomials, of degrees \((2,2)\), have no common zero on \(\mathbf P^1\times\mathbf P^1\) over any field of characteristic zero. Indeed \(c_0=0\) forces the two coordinates to coincide. At a finite common coordinate \(u\), \(c_1=-4(u^3+au+c)\). If this vanishes, \(c_2=(3u^2+a)^2\), which is nonzero because the cubic is nonsingular. At the pair \((\infty,\infty)\), \(c_2\ne0\).

Here is the resulting height comparison, including the finite places. At the real place, normalize each coordinate pair to have maximum norm 1. Compactness, the absence of a common zero, and the upper coefficient bound show that the maximum norm of \((c_0,c_1,c_2)\) is bounded above and below by positive constants depending only on \(E\). At a prime where the integral forms (8.10) have no common zero after reduction, primitive input coordinates give at least one coefficient that is a unit. Only finitely many primes are excluded: the same common-zero calculation works away from 2 and the discriminant.

For each excluded prime the valuation of a common factor is still uniformly bounded. Otherwise, take input pairs with all three valuations tending to infinity, normalize the inputs to be primitive over \(\mathbf Z_p\), and successively select a subsequence constant modulo \(p,p^2,p^3,\ldots\). Its limit would be a common projective zero over \(\mathbf Q_p\), contrary to the characteristic-zero calculation. This elementary compactness argument proves

\[
h([c_0:c_1:c_2])=2h(x(R))+2h(x(S))+O_E(1).
\tag{8.11}
\]

On the other hand, a quadratic whose two projective roots are rational is proportional to the product of their primitive integer linear factors. That product is primitive: reducing two primitive factors modulo any prime gives two nonzero polynomials, whose product remains nonzero. At the real place its maximum coefficient lies between one half and twice the product of the two maximum coefficient norms. To see the lower estimate, let the two linear factors be \(rX+sZ\) and \(vX+wZ\). If the two maximum coordinates choose the same variable, the corresponding extreme product coefficient attains that product of norms. In the remaining case the cross product has that size. Either the middle coefficient has at least half that size, or cancellation forces the other cross product to have more than half that size; then one of the two extreme coefficients has at least half that size. Therefore

\[
h([c_0:c_1:c_2])
=h(x(R+S))+h(x(R-S))+O(1).
\tag{8.12}
\]

Combining (8.11)–(8.12), applying the bounded error to \(2^jR,2^jS\), dividing by \(4^j\) and taking limits proves (8.8). Also \(H(-R)=H(R)\) and \(H(O)=0\). The recurrence (8.8) with consecutive integer multiples first gives \(H(mQ)=m^2H(Q)\). For fixed \(m\), it gives

\[
H(nP+mQ)=n^2H(P)+n a_m+m^2H(Q).
\]

Applying the same recurrence in the \(Q\)-direction shows
\(a_{m+1}-2a_m+a_{m-1}=0\). Since \(a_0=0\) and
\(a_1=H(P+Q)-H(P)-H(Q)\), we have \(a_m=2mb\).
These recurrences hold for negative as well as positive indices, proving (8.9). \(\square\)

**Proposition 8.3 (a rational rank certificate).** The two points \(P,Q\) in (8.2) are independent in \(E(\mathbf Q)\).

**Proof.** The chord law gives \(P+Q=(-3,-1)\) and \(P-Q=(-2,-4)\). Iterate the integer polynomials (8.3), dividing by their common divisor at each step, six times at the respective starting coordinates. Formula (8.6) then gives the following strict rational enclosures:

| Point | Coordinate bits | Height enclosure |
| --- | ---: | --- |
| \(P\) | 3949 | \(0.667<H(P)<0.670\) |
| \(Q\) | 4533 | \(0.766<H(Q)<0.769\) |
| \(P+Q\) | 8876 | \(1.500<H(P+Q)<1.504\) |
| \(P-Q\) | 8088 | \(1.367<H(P-Q)<1.370\) |

For completeness, the logarithms in this certificate need no floating-point assumption. For the positive integer coordinate maximum \(M\), set \(k=\lfloor\log_2 M\rfloor\), and enclose \(M/2^k\) between consecutive multiples of \(2^{-40}\) in \([1,2]\). For either endpoint \(z\), put \(u=(z-1)/(z+1)\). The rational series

\[
\log z=2\sum_{j=0}^{J-1}\frac{u^{2j+1}}{2j+1}+\mathcal R_J,
\qquad
0\le\mathcal R_J\le
\frac{2u^{2J+1}}{(2J+1)(1-u^2)}
\tag{8.13}
\]

follows by integrating the geometric series for \(2/(1-u^2)\). Use \(J=24\), also at \(z=2\), to bound \(\log M=k\log2+\log(M/2^k)\), and then apply the rational error \(4/4096\) in (8.6). This gives every displayed enclosure by finite integer and rational operations.

In particular \(0<b<1/25\), and

\[
H(P)H(Q)-b^2>
\frac{667\cdot766}{10^6}-\frac1{625}>\frac12.
\tag{8.14}
\]

The matrix of (8.9) is positive definite. A nonzero integer relation \(nP+mQ=O\) would give a strictly positive left side in (8.9), whereas \(H(O)=0\). Thus no such relation exists. We only need this rank lower bound; no assertion of the exact rank or of saturation is required. \(\square\)

### 8.2. From rational rank to a triple analytic zero

We use the following precise elliptic and modular prerequisites from the existing programme. The functional equation and local sign calculations are written; the modularity and low-rank theorems have exact planned lessons. Some geometric and compatibility antecedents of the written local calculations also remain planned proof obligations in their owning courses. The full programme is therefore not yet proof-complete at these prerequisites.

| Internal lesson and actual state | Required theorem |
| --- | --- |
| *Elliptic curves over local fields*, Theorem 5.1, written; geometric antecedents planned | Good reduction has conductor exponent 0. Multiplicative reduction has exponent 1, with local factor \((1-a_pp^{-s})^{-1}\), where \(a_p=1\) in the split case and \(a_p=-1\) in the nonsplit case. |
| *Global Langlands conjectures and functoriality*, lesson 10, *Modularity of elliptic curves*, planned | Every elliptic curve over \(\mathbf Q\) has a normalized weight-two newform of level equal to its conductor, with the same Euler factors at every prime. |
| *Local–global compatibility*, Proposition 6.1, written; compatibility antecedent planned | For a weight-two newform of trivial character and prime level \(p\), its Fricke eigenvalue is \(\varepsilon_p=-a_p\). The newvector sign calculation is supported by equation (5.4) in the written *Local factors* lesson. |
| *Twists and functional equations*, Theorem 1.1, written | \(\Lambda(E,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s)\) is entire, and \(\Lambda(E,s)=-\varepsilon_N\Lambda(E,2-s)\). |
| *Global Langlands conjectures and functoriality*, lesson 13, *Elliptic-curve L-functions and Birch–Swinnerton-Dyer*, planned | The Gross–Zagier–Kolyvagin theorem: if \(\operatorname{ord}_{s=1}L(E,s)\) is 0 or 1, it equals the rational rank of \(E\). |

The last theorem concerns the two known low analytic ranks; it does not assume the Birch–Swinnerton-Dyer conjecture in higher rank. The existence of two independent points and the sign computation below are our inputs to its contrapositive.

**Proposition 8.4.** For the curve (8.2), \(L(E,s)\) has a zero of odd order at least three at \(s=1\).

**Proof.** The Weierstrass invariants are

\[
b_2=0,\quad b_4=-14,\quad b_6=25,\quad b_8=-49,
\qquad c_4=336,\quad c_6=-5400,\quad\Delta=5077.
\tag{8.15}
\]

The integer 5077 is prime: trial division by the primes up to \(\sqrt{5077}<72\) suffices. The integral model has good reduction at every other prime, including 2 and 3. At 5077 the discriminant has valuation 1 and \(c_4\) is a unit, so the reduction is nodal and multiplicative. The model is minimal there: discriminant valuations under a change of Weierstrass model differ by a multiple of 12, and a smaller nonnegative valuation is impossible. The conductor statement in the table therefore gives \(N=5077\).

The sign of the node is also explicit. Modulo \(p=5077\), put \(Y=2y+1\). The cubic

\[
Y^2=4x^3-28x+25
=4(x-r)^2(x+2r),\qquad r=92,
\tag{8.16}
\]

has its double root at \(r\equiv75/56\pmod p\). The tangent coefficient is \(12r=1104\), which is a nonsquare: its \((p-1)/2\)-th power is \(-1\pmod p\). Thus this is nonsplit multiplicative reduction. One can check the point count without summing 5077 Legendre symbols. The normalization parameter

\[
v=\frac{Y}{2(x-r)},\qquad
x=v^2-2r,\qquad Y=2v(v^2-3r)
\]

gives all nonsingular points, with \(v=\infty\) giving \(O\). The two branches over the node would have \(v^2=3r\); these are not rational over \(\mathbf F_p\), because \(3r\) and \(12r\) have the same quadratic symbol. Hence the \(p+1\) rational points of the normalization map bijectively to the nonsingular points, and the node adds one more. The singular cubic has \(p+2\) rational points, so \(a_p=p+1-(p+2)=-1\), in agreement with the nonsplit local factor.

By modularity and the two modular sign formulas in the table,

\[
\varepsilon_{5077}=-a_{5077}=1,
\qquad w(E)=-\varepsilon_{5077}=-1.
\tag{8.17}
\]

The Taylor series of the completed \(L\)-function at its centre is consequently odd; its vanishing order is odd. If this order were 1, the Gross–Zagier–Kolyvagin theorem would make the rational rank 1, contradicting Proposition 8.3. Therefore the order is at least 3. The nonzero factors multiplying \(L(E,s)\) at \(s=1\) do not change its order. \(\square\)

Mestre's *La méthode des graphes. Exemples et applications*, Section 3, discusses this conductor-5077 curve and its role in the class-number problem. Historically the needed analytic vanishing was obtained from the Gross–Zagier formula. Our deduction uses the later low-rank Gross–Zagier–Kolyvagin theorem, through its exact planned internal provider, and the explicit rank certificate just proved.

### 8.3. Small class number forces a fourth zero

Here is the algebraic step that relates the fixed curve to the varying quadratic field. In the written *Number fields* course, *Algebraic integers*, Theorem 1.4, supplies the quadratic integral basis; *Dedekind domains*, Theorem 3.2, and *Ideal norms*, Proposition 4.1, supply factorization and norm. *Finiteness of the class number*, Corollary 8.2, gives the finite class group; *Quadratic fields and forms*, Theorems 10.1–10.2, identifies its order with \(h(D)\).

**Lemma 8.5 (a split prime cannot be too small).** If \(D<0\) is fundamental, \(p\nmid D\) is a prime that splits in \(\mathbf Q(\sqrt D)\), and \(h=h(D)\), then

\[
p^h\ge |D|/4.
\tag{8.18}
\]

**Proof.** Write \((p)=\mathfrak p\overline{\mathfrak p}\), with the two prime ideals distinct and both of norm \(p\). The class of \(\mathfrak p\) has some order \(1\le k\le h\), so \(\mathfrak p^k=(\alpha)\). The ideal is integral, hence \(\alpha\) is an algebraic integer, of norm \(p^k\). It is not rational: for a rational integer the valuations at the two ideals above \(p\) agree, whereas this principal ideal has valuations \(k\) and 0.

The quadratic integral basis writes \(\alpha=(u+v\sqrt D)/2\) for integers \(u,v\), with \(v\ne0\). This notation also covers even fundamental discriminants, with the appropriate parity on \(u\). Thus

\[
p^k=N(\alpha)=\frac{u^2+|D|v^2}{4}\ge|D|/4.
\]

Since \(k\le h\), (8.18) follows. \(\square\)

**Corollary 8.6.** If \(5077\nmid D\) and

\[
h(D)<\frac{\log(|D|/4)}{\log5077},
\tag{8.19}
\]

then

\[
L(E,s)L(E\otimes\chi_D,s)
\quad\hbox{vanishes to order at least four at }s=1.
\tag{8.20}
\]

**Proof.** Lemma 8.5 excludes splitting at 5077. The prime is unramified by hypothesis, so it is inert and \(\chi_D(5077)=-1\), by the full quadratic decomposition law in *Decomposition of primes*, Corollary 5.5. Since \(D<0\), \(\chi_D(-1)=-1\); hence \(\chi_D(-5077)=1\). The full coprime twisting theorem in *Twists and functional equations*, Theorem 2.2, gives

\[
w(E\otimes\chi_D)=w(E)\chi_D(-5077)=-1.
\tag{8.21}
\]

Indeed for the real primitive character its Gauss-square factor is
\(\tau(\chi_D)^2/|D|=\chi_D(-1)\), and its completed level is \(5077|D|^2\). The twist has a central zero of odd order at least one. Proposition 8.4 supplies at least three zeros from the untwisted factor. The product has at least four. \(\square\)

If (8.19) fails, it already gives an effective lower bound proportional to \(\log|D|\), after enlarging a finite threshold. Thus the analytic fourth-zero argument is only needed in the small-class-number range. The coprimality assumption remains essential in Corollary 8.6; one cannot apply the quoted twisting formula unchanged at a ramified conductor prime.

### 8.4. Counting the primitive ideals that enter the error term

The analytic coefficients record ideals, rather than just split primes. We need a bound that keeps the class number visible even when the cutoff exceeds the smallest reduced norm. Write

\[
d=|D|/4,\qquad h=h(D),\qquad
\tau_D(n)=\sum_{a\mid n}\chi_D(a).
\tag{8.22}
\]

An integral ideal is **primitive** if it is not divisible by the ideal \((m)\) of any rational integer \(m>1\). Let \(r_D(n)\) count primitive ideals of norm \(n\), and put

\[
R_D(A)=\sum_{n\le A}r_D(n),\qquad A>0.
\]

**Lemma 8.7 (a class-sensitive ideal count).** For every real \(A>0\),

\[
R_D(A)\le h\left(1+\frac{4A}{\sqrt d}\right).
\tag{8.23}
\]

Moreover \(r_D(n)=\tau_D(n)\) at squarefree integers. Thus the same bound holds for \(\sum_{n\le A,\ n\text{ squarefree}}\tau_D(n)\).

**Proof.** Fix an ideal class \(C\), and choose an integral ideal \(I\) in its inverse class with a reduced primitive positive definite norm form

\[
q_I(u,v)=au^2+buv+cv^2,
\qquad |b|\le a\le c,\quad b^2-4ac=D.
\]

This choice and its norm interpretation are Theorems 10.1–10.2 of *Quadratic fields and forms*. Integral ideals \(J\) in \(C\) correspond to nonzero elements \(\alpha\in I\), modulo multiplication by units, through

\[
J=(\alpha)I^{-1},\qquad
N J=\frac{N\alpha}{N I}=q_I(u,v).
\tag{8.24}
\]

Conversely \(JI\) is principal, and \(J\subseteq\mathcal O_K\) makes any generator \(\alpha\) lie in \(I\), so the correspondence is onto. It is primitive exactly when \(\gcd(u,v)=1\): divisibility by \((m)\) is equivalent, by invertibility of \(I\), to \(\alpha/m\in I\). There are at least the two units \(1,-1\), and each nonzero element and its negative are distinct. Hence we may bound the number of ideals by half the number of primitive vectors, without needing the precise unit count at the two smallest discriminants.

Completing the square gives

\[
q_I(u,v)=a\left(u+\frac{b}{2a}v\right)^2
          +\frac d a v^2.
\tag{8.25}
\]

For \(v=0\), primitivity permits only \(u=\pm1\), contributing at most one ideal. For \(v\ne0\), put \(T=\lfloor\sqrt{Aa/d}\rfloor\). There are at most \(2T\) choices of \(v\), and for each one the possible \(u\)'s lie in an interval of length at most \(2\sqrt{A/a}\). Dividing the resulting count by two bounds the additional ideals by

\[
T(2\sqrt{A/a}+1)
\le\frac{2A}{\sqrt d}+\sqrt{Aa/d}.
\tag{8.26}
\]

If \(T=0\), this additional contribution is zero. Otherwise \(A\ge d/a\). Reduction also gives \(a^2\le|D|/3=4d/3\), so \(a/A\le4/3\). The last term in (8.26) is consequently at most \((2/\sqrt3)A/\sqrt d\). Since \(2+2/\sqrt3<4\), each class contributes at most \(1+4A/\sqrt d\). Summing over the \(h\) classes proves (8.23).

At an unramified split prime, a primitive ideal of norm \(p^e\), \(e\ge1\), must be one of the two pure powers of the prime ideals above \(p\); using both primes makes it divisible by \((p)\). At an inert prime, every positive power of its prime ideal is divisible by \((p)\), so there is no nontrivial primitive contribution. At a ramified prime only the first power is allowed, because its square is \((p)\). Unique ideal factorization therefore gives

\[
\sum_{n\ge1}\frac{r_D(n)}{n^s}
=\prod_{p\mid D}(1+p^{-s})
 \prod_{\chi_D(p)=1}\frac{1+p^{-s}}{1-p^{-s}}
=\frac{\zeta(s)L(s,\chi_D)}{\zeta(2s)},
\quad \operatorname{Re}s>1.
\tag{8.27}
\]

In particular, the squarefree coefficients are \(1,2,0\) at respectively ramified, split and inert primes. These are exactly the squarefree coefficients of \(\zeta(s)L(s,\chi_D)\), namely \(\tau_D(n)\). They are nonnegative, so the squarefree sum is bounded by \(R_D(A)\). \(\square\)

**Corollary 8.8 (weighted squarefree tails).** For real \(A\ge B\ge1\),

\[
\sum_{\substack{B<n\le A\\
n\text{ squarefree}}}
\frac{\tau_D(n)}{\sqrt n}
\le\frac h{\sqrt B}+\frac{8h\sqrt A}{\sqrt d},
\tag{8.28}
\]

and

\[
\sum_{\substack{B<n\le A\\
n\text{ squarefree}}}
\frac{\tau_D(n)}n
\le\frac h B+
\frac{4h}{\sqrt d}\left(1+\log\frac A B\right).
\tag{8.29}
\]

**Proof.** Set \(U(t)=\sum_{n\le t,\ n\text{ squarefree}}\tau_D(n)\), so \(U(t)\le h+4ht/\sqrt d\). For \(\theta>0\), exact Stieltjes partial summation gives

\[
\sum_{B<n\le A}\frac{\tau_D(n)\mathbf1_{n\text{ squarefree}}}{n^\theta}
=\frac{U(A)}{A^\theta}-\frac{U(B)}{B^\theta}
  +\theta\int_B^A\frac{U(t)}{t^{1+\theta}}\,dt.
\tag{8.30}
\]

Drop the nonpositive endpoint at \(B\), insert the upper bound, and evaluate the integrals. For \(\theta=1/2\), the constant term combines to \(h/\sqrt B\), and the linear term is at most \(8h\sqrt A/\sqrt d\). For \(\theta=1\), the corresponding terms are \(h/B\) and \((4h/\sqrt d)(1+\log(A/B))\). This proves both inequalities with the indicated strict lower and closed upper endpoints. \(\square\)

To absorb the divisor bound for cusp-form coefficients, one more factorization is useful. Let \(\tau(n)\) be the ordinary divisor function, and let \(C_B\) be the squarefree product of the primes dividing \(D\) and the split primes at most \(B\). Define

\[
S_D(A,B)=
\sum_{\substack{1<n\le A\\
n\text{ squarefree}\\(n,C_B)=1}}
\frac{\tau(n)\tau_D(n)}{\sqrt n}.
\tag{8.31}
\]

**Lemma 8.9 (removing the small split factors).** For \(A\ge B\ge1\),

\[
\begin{aligned}
S_D(A,B)\le{}&\frac{2h}{\sqrt B}
 +\frac{16h\sqrt A}{\sqrt d}+\frac{h^2}{B}\\
&+\frac{16h^2\sqrt A}{B\sqrt d}
 +\frac{32h^2\sqrt A}{d}(1+\log A).
\end{aligned}
\tag{8.32}
\]

**Proof.** For squarefree \(n\), multiplication of the prime factors verifies

\[
\tau(n)\tau_D(n)
=\sum_{uv=n}\tau_D(u)\tau_D(v).
\tag{8.33}
\]

At a prime both sides are \(2(1+\chi_D(p))\). If \(n\) is coprime to \(C_B\) and \(\tau_D(n)\ne0\), every prime dividing it splits and exceeds \(B\). The two factorizations with \(u=1\) or \(v=1\) therefore contribute at most twice the left side of (8.28). Every remaining factorization has \(u,v>B\). Dropping its coprimality and disjointness restrictions bounds the rest by

\[
\sum_{\substack{B<u\le A/B\\
u\text{ squarefree}}}
\frac{\tau_D(u)}{\sqrt u}
\left(\frac h{\sqrt B}
 +\frac{8h\sqrt{A/u}}{\sqrt d}\right).
\tag{8.34}
\]

If \(A<B^2\), this sum is empty. Otherwise apply (8.28) and (8.29), with upper cutoff \(A/B\), to its two terms. The first is at most

\[
\frac{h^2}B+\frac{8h^2\sqrt A}{B\sqrt d}.
\]

The second is at most

\[
\frac{8h^2\sqrt A}{B\sqrt d}
 +\frac{32h^2\sqrt A}{d}
   \left(1+\log\frac A{B^2}\right).
\]

Combine them with the two endpoint factorizations and enlarge the last logarithm to \(\log A\). The resulting positive bound also covers the empty-sum case, proving (8.32). \(\square\)

For example, at \(A\) of order \(|D|\), the square-root terms in (8.32) retain an effective bound of order \(h\), plus terms involving \(h^2/B\) and \(h^2\log|D|/\sqrt{|D|}\). Choosing the small-prime cutoff as a function of the class number is therefore compatible with the small-class-number range. The later smoothed argument must still justify its weights, main term and exact choice of cutoff.

### 8.5. Derivatives at one when the class number is small

The residue calculation will involve derivatives of the quadratic Dirichlet function. Their size must be controlled by the class number, rather than by the usual unrestricted powers of the conductor logarithm. Put \(q=|D|\), and continue to write \(h=h(D)\).

**Lemma 8.10 (a positive first derivative).** If

\[
q\ge1000,\qquad h\log q\le\frac{\sqrt q}{1000},
\tag{8.35}
\]

then \(L'(1,\chi_D)>1\). More precisely, without the small-class-number condition,

\[
L'(1,\chi_D)\ge\zeta(2)
 -L(1,\chi_D)(4\log q+1)
 -\frac{8\log q+2}{q}-\frac4{q^2}.
\tag{8.36}
\]

Under (8.35), we also have

\[
\sum_{n\le q^4}\frac{\tau_D(n)}n
\le\frac{11}{10}L'(1,\chi_D).
\tag{8.37}
\]

**Proof.** Let \(A(t)=\sum_{a\le t}\chi_D(a)\). A complete period sums to zero, so \(|A(t)|\le q\) and \(A(q^2)=0\). Write \(Y=q^2\), \(x=Y^2=q^4\). Splitting the convolution \(\tau_D=1*\chi_D\) according as its character variable is at most \(Y\) gives the exact hyperbola identity

\[
T(x):=\sum_{n\le x}\frac{\tau_D(n)}n
=\sum_{a\le Y}\frac{\chi_D(a)}a H_{\lfloor x/a\rfloor}
 +\sum_{b\le Y}\frac1b
      \sum_{Y<a\le x/b}\frac{\chi_D(a)}a,
\tag{8.38}
\]

where \(H_j=\sum_{r=1}^j1/r\).

Here are all the approximation errors in (8.38). Integral comparison shows that \(H_j-\log j\) decreases to a constant \(\gamma\) with \(0<\gamma<1\), and
\(0<H_j-\log j-\gamma<1/j\). Indeed, its consecutive differences are \(\log(1+1/j)-1/(j+1)>0\), whose tail is bounded by the integral comparison for \(1/t\); the endpoint inequalities follow by the same comparison. Consequently, for real \(z\ge2\),

\[
|H_{\lfloor z\rfloor}-\log z-\gamma|\le3/z.
\]

The error from this replacement in the first sum is at most \(3Y/x\). Partial summation starting at the zero endpoint \(A(Y)=0\) gives

\[
\left|\sum_{a>Y}\frac{\chi_D(a)}a\right|\le\frac qY,
\qquad
\left|\sum_{a>Y}\frac{\chi_D(a)\log a}a\right|
\le\frac{q\log Y}{Y}.
\tag{8.39}
\]

For the second inequality, \((\log t)/t\) decreases for \(t\ge Y\), so the integral of the absolute derivative is \((\log Y)/Y\). These convergent tails identify the infinite sums as \(L(1,\chi_D)\) and \(-L'(1,\chi_D)\). The same partial summation, now with a finite upper endpoint \(Z\ge Y\), gives

\[
\left|\sum_{Y<a\le Z}\frac{\chi_D(a)}a\right|
\le\frac qZ+q\left(\frac1Y-\frac1Z\right)=\frac qY.
\]

Since \(H_Y\le1+\log Y\), the second sum of (8.38) is at most \((q/Y)(1+\log Y)\) in absolute value. Combining these bounds yields

\[
\left|T(q^4)-L(1,\chi_D)(4\log q+\gamma)
                 -L'(1,\chi_D)\right|
\le\frac{8\log q+2}{q}+\frac3{q^2}.
\tag{8.40}
\]

Every \(\tau_D(n)\) is nonnegative, and \(\tau_D(m^2)\ge1\). At a prime this last assertion follows from the values \(2e+1,1,1\) of \(\tau_D(p^{2e})\), for split, inert and ramified primes. Thus

\[
T(q^4)\ge\sum_{m\le q^2}\frac1{m^2}
\ge\zeta(2)-q^{-2}.
\]

This and \(\gamma<1\) prove (8.36).

The class-number formula gives \(L(1,\chi_D)=2\pi h/(w_D\sqrt q)\le\pi h/\sqrt q\). Under (8.35),
\(L(1,\chi_D)(4\log q+1)<20/1000\), using \(\pi<4\) and \(\log q>1\). The function \((8\log q+2)/q\) is decreasing for \(q\ge1000\), and \(\log1000<7\), so the remaining error in (8.36) is less than \(58/1000+4/10^6\). Already \(\zeta(2)>1+1/4\), proving \(L'>1\). Finally (8.40) bounds \(T(q^4)\) above by \(L'+1/10\); since \(L'>1\), this gives (8.37). \(\square\)

**Lemma 8.11 (higher derivatives).** For every fixed integer \(k\ge1\), there is an effectively computable constant \(C_k\) such that, under (8.35),

\[
|L^{(k)}(1,\chi_D)|
\le C_k\left\{
L'(1,\chi_D)(\log(2h))^{k-1}
 +\frac h{\sqrt q}(\log q)^{k+1}\right\}.
\tag{8.41}
\]

**Proof.** We use the effective estimate
\(U(z)=\sum_{m\le z}\mu(m)/m\ll e^{-c\sqrt{\log z}}\) for \(z\ge2\), proved in *The prime number theorem with the classical error term*, Corollary 3.3, in the zeta course. Its proof is the reciprocal-zeta contour of Theorem 3.2 followed by an explicitly evaluated tail integral; it does not use Siegel's theorem. Enlarging its effective constant over \(1\le z\le2\) gives

\[
|U(z)|\le\frac{C}{\log(2z)},\qquad
\left|\sum_{m\le z}\frac{\mu(m)(\log m)^j}m\right|\le C_j
\quad(j\ge1).
\tag{8.42}
\]

For the second bound, partial summation expresses the sum as
\(U(z)(\log z)^j-j\int_1^z U(t)(\log t)^{j-1}\,dt/t\). The substitution \(v=\sqrt{\log t}\) bounds the integral by a constant multiple of \(\int_0^\infty e^{-cv}v^{2j-1}\,dv\). This integral and the endpoint supremum are explicitly finite, so the constants are effective.

Expanding \(\log(mn)^k\) by the binomial theorem in (8.42), for \(1\le n\le x\), proves

\[
\left|\sum_{m\le x/n}\frac{\mu(m)}m(\log(mn))^k\right|
\le C_k(\log(2n))^{k-1}
        \frac{\log(2x)}{\log(2x/n)}.
\tag{8.43}
\]

To check the term with no \(\log m\), use
\((\log n)^k/\log(2x/n)\); the other terms are bounded by \(C_k(\log(2n))^{k-1}\). Their combination is bounded by the right side because \(\log(2x)=\log n+\log(2x/n)\). This also covers \(n=1\) and \(x/n=1\).

We need a count for all ideals. Removing the largest rational integer divisor gives a unique expression \(J=(r)J_0\) with \(J_0\) primitive. This can be verified prime by prime: remove the common minimum of the split valuations, the whole inert valuation, and half the ramified valuation rounded down. Therefore Lemma 8.7 and \(\sum_{r\ge1}r^{-2}<2\) give, for \(t\ge1\),

\[
N_D(t):=\sum_{n\le t}\tau_D(n)
=\sum_{r\le\sqrt t}R_D(t/r^2)
\le h\sqrt t+\frac{16ht}{\sqrt q}.
\tag{8.44}
\]

Here \(\tau_D(n)\) counts all ideals by their three local factors, as in the proof of Lemma 8.7. Partial summation then gives, for \(X\ge y\ge1\),

\[
\sum_{y<n\le X}\frac{\tau_D(n)}n
\le\frac{2h}{\sqrt y}
 +\frac{16h}{\sqrt q}(1+\log(X/y)).
\tag{8.45}
\]

Also, with \(r=k-1\ge0\),

\[
\sum_{y<n\le X}\frac{\tau_D(n)(\log(2n))^r}n
\ll_k \frac h{\sqrt y}(\log(2y))^r
      +\frac h{\sqrt q}(\log(2X))^{r+1}.
\tag{8.46}
\]

For completeness, take \(f(t)=(\log(2t))^r/t\) in Stieltjes partial summation. Drop its negative lower endpoint and bound
\(|f'(t)|\le C_k(\log(2t))^r/t^2\). The \(h\sqrt t\) part of (8.44) integrates against this bound to at most
\(C_kh y^{-1/2}(\log(2y))^r\): put \(t=ye^v\), expand \((\log(2y)+v)^r\), and integrate the finitely many terms \(v^je^{-v/2}\). The linear part gives \(C_k h(\log(2X))^{r+1}/\sqrt q\). The upper endpoint satisfies the same bounds. No monotonicity of \(f\) near 1 is needed.

Set \(x=q^4\), \(y=4h^2\). Condition (8.35) implies \(y\le q^2\). The identity \(\chi_D=\mu*\tau_D\) is an exact finite convolution, so

\[
\sum_{a\le x}\frac{\chi_D(a)(\log a)^k}a
=\sum_{n\le x}\frac{\tau_D(n)}n
      \sum_{m\le x/n}\frac{\mu(m)(\log(mn))^k}m.
\tag{8.47}
\]

For \(n\le q^2\), the ratio in (8.43) is at most 2. The contribution with \(n\le y\) is consequently at most
\(C_k(\log(2y))^{k-1}T(y)\), which is bounded by
\(C_k L'(1,\chi_D)(\log(2h))^{k-1}\) by positivity and (8.37). For \(y<n\le q^2\), use (8.46). Since \(h/\sqrt y=1/2\) and \(L'>1\), its first term is absorbed by the same bound. Its second term is \(O_k(h(\log q)^k/\sqrt q)\).

For \(q^2<n\le q^4\), the right side of (8.43) is at most \(C_k(\log q)^k\). Applying (8.45) gives a contribution at most
\(C_k h(\log q)^{k+1}/\sqrt q\). Finally, partial summation of \(\chi_D(a)(\log a)^k/a\) past \(x\), using \(A(x)=0\), bounds its tail by \(q(\log x)^k/x\) when \(x\ge e^k\). This term is absorbed as well. Its signed infinite sum is \((-1)^kL^{(k)}(1,\chi_D)\), proving (8.41) in that range. For fixed \(k\), the remaining integers \(1000\le q<e^{k/4}\) form an effective finite range. The same periodic-sum tail estimates bound their derivatives and allow an effective enlargement of \(C_k\). \(\square\)

In particular, if \(h\le(\log q)^A\) for a fixed \(A\), then for all sufficiently large effective \(q\),

\[
|L^{(k)}(1,\chi_D)|\ll_{k,A}
L'(1,\chi_D)(\log\log q)^{k-1}.
\tag{8.48}
\]

Indeed (8.35) eventually holds, \(L'>1\), and the remaining term in (8.41) tends to zero. This controls the higher derivatives by a smaller logarithmic scale than the first derivative's main contribution to the residue. Sections 8.10–8.12 combine it with the smoothed errors and evaluate that residue.

### 8.6. A central derivative as a smoothed coefficient sum

We first construct the exact smoothing kernel. Its contour formula, sign and decay are all needed: a merely formal residue computation would not control the later error.

**Lemma 8.12 (the second-derivative kernel).** For \(y>0\), set

\[
V(y)=\frac2{2\pi i}\int_{(2)}
 y^{-z}\Gamma(1+z)^2\frac{dz}{z^3}.
\tag{8.49}
\]

This integral converges absolutely, \(V(y)>0\), and

\[
\left|V(y)-\{(\log(1/y)-2\gamma)^2+2\zeta(2)\}\right|
\le8\sqrt y.
\tag{8.50}
\]

In addition,

\[
V(y)\le
\begin{cases}
16(1+\log(1/y))^2,&0<y\le1,\\
32e^{-\sqrt y},&y\ge1.
\end{cases}
\tag{8.51}
\]

**Proof.** Put

\[
\phi(t)=\int_0^\infty e^{-u-t/u}\frac{du}{u},\qquad
W(y)=\int_y^\infty \phi(t)(\log(t/y))^2\,dt.
\tag{8.52}
\]

All integrands are nonnegative, and \(W(y)>0\). For real \(s>0\), Tonelli and the substitution \(t=uv\) give

\[
\int_0^\infty t^s\phi(t)\,dt=\Gamma(s+1)^2.
\]

The elementary integral
\(\int_0^t y^{s-1}(\log(t/y))^2dy=2t^s/s^3\)
therefore gives the Mellin transform \(2\Gamma(1+s)^2/s^3\) of \(W\). The same formulas hold for complex \(s\) with positive real part by absolute convergence. Mellin inversion now identifies \(W=V\): after putting \(y=e^v\), it is ordinary Fourier inversion for the continuous integrable function \(e^{2v}W(e^v)\). Its transform is integrable by the exponential vertical Gamma bound. This proves the identification and positivity.

Shift the contour in (8.49) to \(\operatorname{Re}z=-1/2\). The only crossed pole is at zero; the Gamma poles start at \(z=-1\). Uniform vertical decay makes the horizontal integrals tend to zero. The logarithmic-derivative formula of *The Gamma function and Stirling's formula*, Proposition 5.1, gives
\(\Gamma'(1)=-\gamma\) and
\((\Gamma'/\Gamma)'(1)=\sum_{n\ge1}n^{-2}=\zeta(2)\), by local uniform differentiation. Thus

\[
\Gamma(1+z)^2
=1-2\gamma z+(2\gamma^2+\zeta(2))z^2+O(z^3).
\]

Multiplication by \(2e^{z\log(1/y)}/z^3\) gives the polynomial in (8.50) as the residue. On the new line the exact reflection identity
\(|\Gamma(1/2+it)|^2=\pi/\cosh(\pi t)\)
bounds the remaining integral in absolute value by

\[
\frac{\sqrt y}{\pi}
\int_{-\infty}^\infty
\frac{\pi\,dt}{(1/4+t^2)^{3/2}}
=8\sqrt y.
\]

This proves (8.50), with an explicit error. At \(0<y\le1\), use \(0<\gamma<1\), \(\zeta(2)<2\), and \(\sqrt y\le1\) to obtain the first bound in (8.51).

For \(t\ge1\), substitute \(u=\sqrt t e^v\) in \(\phi\). Since \(\cosh v\ge1+v^2/2\),

\[
\phi(t)=\int_{\mathbf R}e^{-2\sqrt t\cosh v}\,dv
\le\sqrt\pi\,t^{-1/4}e^{-2\sqrt t}.
\]

When \(t\ge y\ge1\), \(\log(t/y)\le\log t\le2\sqrt t\). Formula (8.52), followed by \(v=\sqrt t\), now bounds \(V(y)\) by
\(8\sqrt\pi\int_{\sqrt y}^\infty v^{5/2}e^{-2v}dv\).
For \(v\ge1\), \(v^{5/2}e^{-v}\le v^3e^{-v}\le27e^{-3}<2\). Hence this is at most \(16\sqrt\pi e^{-\sqrt y}<32e^{-\sqrt y}\), proving the second bound. \(\square\)

The Mellin input for the modular functions comes from *Twists, level N and Hecke's converse theorem*, Theorems 1.1–2.2. Let \(f\) be a real-coefficient weight-two Fricke eigenform at level \(N\), normalized with first coefficient one. Write its unitary coefficients and Dirichlet series as

\[
f(z)=\sum_{n\ge1}\lambda(n)\sqrt n\,e(nz),\qquad
L_u(s,f)=\sum_{n\ge1}\lambda(n)n^{-s}.
\tag{8.53}
\]

Thus the corresponding elliptic-curve function is \(L(E,s)=L_u(s-1/2,f)\), with its center at \(s=1\). Suppose \((q,N)=1\), and let \(f_\chi\) be the coefficient twist by \(\chi=\chi_D\). Its containing level is \(Nq^2\); that level suffices for the Mellin functional equation. Define

\[
Q=\frac{Nq}{4\pi^2},\qquad
\mathcal A(s)=Q^s\Gamma(s+1/2)^2
                  L_u(s,f)L_u(s,f_\chi).
\tag{8.54}
\]

The two completed Mellin functions show that \(\mathcal A\) is entire, bounded on every closed vertical strip, and satisfies
\(\mathcal A(s)=w\mathcal A(1-s)\), where
\(w=\chi_D(-N)\). The scalar \(Q^{-1/2}\) separating (8.54) from the product of the arithmetic completions is constant in \(s\), so it does not change that equation.

**Lemma 8.13 (the exact smoothed identity).** If \(w=1\), then

\[
Q^{-1/2}\mathcal A''(1/2)
=2\sum_{n\ge1}\frac{a_D(n)}{\sqrt n}V(n/Q),\qquad
a_D(n)=\sum_{uv=n}\lambda(u)\lambda(v)\chi_D(v).
\tag{8.55}
\]

The series is absolutely convergent. If the product function has vanishing order at least four at its center, its right side is zero.

**Proof.** The elementary cusp estimate \(|\lambda(n)|\le C\sqrt n\) follows as follows. The invariant quantity \((\operatorname{Im}z)|f(z)|\) is bounded: a fundamental domain has finitely many cusps, the transformed Fourier series decays exponentially at each, and the remaining compact part gives a finite bound. Integrating the Fourier coefficient on one real period at height \(1/n\) therefore gives \(|\lambda(n)|\sqrt n\le Ce^{2\pi}n\); absorb the fixed factor into \(C\). This gives
\(|a_D(n)|\le C^2\sqrt n\,\tau(n)\). Together with (8.51), this proves absolute convergence of the smoothed series. It also permits sum–integral interchange on \(\operatorname{Re}z=2\). Put

\[
I=\frac2{2\pi i}\int_{(2)}
          \mathcal A(1/2+z)\frac{dz}{z^3}.
\tag{8.56}
\]

The interchange and (8.49) give
\(I=Q^{1/2}\sum_n a_D(n)V(n/Q)/\sqrt n\).
Move the contour to \(\operatorname{Re}z=-2\). The function \(\mathcal A\) is entire; the sole residue, at zero, is \(\mathcal A''(1/2)\). Strip boundedness makes the horizontal integrals vanish and the vertical integrals absolutely convergent. Replacing \(z\) by \(-z\) in the new integral and using \(w=1\) makes that integral \(-I\). Therefore \(I=\mathcal A''(1/2)-I\), proving (8.55). The Gamma and level factors are nonzero at the center, so product vanishing of order at least four also makes \(\mathcal A''(1/2)=0\). \(\square\)

For the conductor-5077 curve in Corollary 8.6, \(w=1\) and the fourth zero therefore give the precise coefficient equation

\[
\sum_{n\ge1}\frac{a_D(n)}{\sqrt n}V(n/Q)=0,
\qquad Q=5077|D|/(4\pi^2).
\tag{8.57}
\]

The coefficients \(a_D(n)\) need not be positive. The point of the next residue calculation is to isolate a positive main contribution and bound the rest by the class-sensitive estimates of Section 8.4.

### 8.7. A rational-rank certificate for the classical twist

The curve used in the original class-number argument allows a different treatment of the ramified conductor primes. Its arithmetic rank input can be verified with a small certificate. Consider

\[
E_0:\quad y^2=x^3+10x^2-20x+8,
\qquad E_*:\quad -139y^2=x^3+10x^2-20x+8.
\tag{8.58}
\]

The change \(x=4X-2\), \(y=8Y+4\) puts \(E_0\) into the integral equation
\(Y^2+Y=X^3+X^2-3X+1\), with discriminant 37 and \(c_4=160\). For the twist, the rational change
\(X=-139(9x+30)\), \(Y=139^2\cdot27y\)
gives

\[
\mathcal E:\quad Y^2=X^3-83466720X-291207039408.
\tag{8.59}
\]

We use the two points \((x,y)=(-18,4),(-42,20)\) of \(E_*\). On \(\mathcal E\) they are

\[
P_*=(18348,2086668),\qquad
Q_*=(48372,10433340).
\tag{8.60}
\]

**Proposition 8.14 (two independent points by quadratic characters).** The points in (8.60) are independent over \(\mathbf Z\).

**Proof.** Put \(F(X)=X^3-83466720X-291207039408\). Modulo 137 its roots are \(2,16,119\), all simple. A simple root \(r_1\) lifts to a root \(r\in\mathbf Z_{137}\): given \(r_j\) modulo \(137^j\), choose \(e\) modulo 137 satisfying

\[
F(r_j)/137^j+eF'(r_j)\equiv0\pmod{137},
\qquad r_{j+1}=r_j+e137^j.
\tag{8.61}
\]

Taylor expansion proves the new congruence modulo \(137^{j+1}\); the derivative remains a unit, so the compatible sequence converges in the completion and solves \(F(r)=0\).

For \(z\in\mathbf Q_{137}^\times\), define the multiplicative character

\[
\eta(z)=\left(\frac{137^{-v_{137}(z)}z\bmod137}{137}\right).
\tag{8.62}
\]

It is 1 on squares. The cubic \(F\) has no root modulo 7, and a rational root of a monic integral polynomial would be an integer root. Thus \(F\) has no rational root. In particular, \(\mathcal E(\mathbf Q)\) has no nonzero point of order two, and \(X(R)-r\ne0\) for every rational point \(R\ne O\).

For each lifted root \(r\), put \(\theta_r(O)=1\) and
\(\theta_r(R)=\eta(X(R)-r)\) for rational \(R\ne O\). This is a group homomorphism to \(\{1,-1\}\). To verify it, consider a nonvertical chord or tangent \(Y=\ell(X)\), with intersection abscissae \(X_1,X_2,X_3\), counted with multiplicity. Since \(F-\ell^2\) is monic,

\[
F(X)-\ell(X)^2=(X-X_1)(X-X_2)(X-X_3),
\qquad \prod_{i=1}^3(X_i-r)=\ell(r)^2.
\tag{8.63}
\]

The intersection points are rational in this chord or tangent construction. None equals \((r,0)\), so \(\ell(r)\ne0\). Applying \(\eta\), and observing that negation keeps the abscissa, proves
\(\theta_r(R+S)=\theta_r(R)\theta_r(S)\). For a vertical line the points are negatives, whose character values agree and square to 1. The case of \(O\) is immediate. These exhaust the addition cases, using the chord group law already proved in *Complex tori and elliptic curves*.

Both point abscissae are units away from the two roots \(2,119\). Their reductions are \(127,11\), respectively. The two lifted roots consequently give the values

\[
\begin{array}{c|cc}
 &P_*&Q_*\\ \hline
r\equiv2&-1&1\\
r\equiv119&1&-1
\end{array}
\tag{8.64}
\]

For example, the four unit differences are \(125,9,8,29\) modulo 137, whose quadratic characters are \(-1,1,1,-1\). A relation \(nP_*+mQ_*=O\) therefore forces both \(n\) and \(m\) even. With \(R=(n/2)P_*+(m/2)Q_*\), the relation gives \(2R=O\); absence of rational two-torsion implies \(R=O\). Repeating this argument would make any nonzero pair of integer coefficients divisible by arbitrarily high powers of two, which is impossible. Hence there is no nonzero relation. \(\square\)

This proof supplies the rational-rank lower bound without assuming the rank conjecture or a numerical central-zero calculation. To use this curve for every \(D\), the analytic argument still has to establish its local conductor and root signs, including when 37 or 139 divides \(D\). The coprime formula alone does not cover those cases.

### 8.8. How many small prime factors can occur?

The finite Euler products in the residue involve ramified primes and small split primes. Two elementary ideal-class arguments control their number. They also explain how a discriminant-dependent Euler loss can be absorbed into the final small power of a logarithm.

**Lemma 8.15 (ramified-prime classes).** For a negative fundamental discriminant \(D\) with \(|D|>4\), let \(\omega(D)\) count its distinct prime divisors. Then

\[
2^{\omega(D)-1}\le h(D).
\tag{8.65}
\]

**Proof.** Each ramified prime has a unique prime ideal \(\mathfrak p_p\) above it, with \(\mathfrak p_p^2=(p)\). Mapping a subset of the ramified primes to the class of their ideal product gives a homomorphism from \((\mathbf Z/2\mathbf Z)^{\omega(D)}\) to the class group.

Suppose a subset product is principal, say \(I=(\alpha)\), and put \(P=\prod_{p\text{ in the subset}}p\). Since \(I^2=(P)\), we have \(\alpha^2=\varepsilon P\) for a unit \(\varepsilon\). The only units here are \(1,-1\). Indeed a nonrational unit \((u+v\sqrt D)/2\) would have norm at least \(|D|/4>1\), whereas a unit in an imaginary quadratic field has positive integral norm 1. A rational integral unit is \(\pm1\).

If \(\alpha^2=P\), then \(\alpha\) is real and belongs to \(\mathbf Q(\sqrt D)\), hence is rational. The squarefree integer \(P\) is then a rational square, forcing the empty subset. If \(\alpha^2=-P\), then the field is \(\mathbf Q(\sqrt{-P})\). There is at most one squarefree positive integer \(P\) producing this fixed field: its squarefree radicand is unique. Thus the kernel has at most two elements, and its image has at least \(2^{\omega(D)-1}\) elements. They are classes in the finite group of order \(h(D)\), proving the assertion. \(\square\)

**Lemma 8.16 (small split primes).** Let \(B\ge2\), \(h=h(D)\), and \(\ell=\lfloor\log_2h\rfloor+1\). If

\[
B^\ell<|D|/4,
\tag{8.66}
\]

then at most \(\lfloor\log_2h\rfloor\) primes at most \(B\) split in \(\mathbf Q(\sqrt D)\).

**Proof.** If there were \(\ell\) such primes, choose one prime ideal above each. Form all \(2^\ell\) subset products. We show their classes are distinct. If products \(I_T,I_U\) had the same class, then \(I_T\overline{I_U}\) would be principal. Divide it by the rational integer product of the primes common to both subsets. The resulting integral ideal \(J\) is still principal and has norm the product of the primes in the symmetric difference, at most \(B^\ell<|D|/4\).

An integral generator \(\alpha\) of \(J\) must be rational: a nonrational algebraic integer has norm at least \(|D|/4\), as proved in Lemma 8.5. But a rational ideal has equal valuations at the two primes over every split prime. The ideal \(J\) has a single chosen prime factor at each prime in the symmetric difference, so this difference must be empty. Hence \(T=U\). The class group would have at least \(2^\ell>h\) elements, a contradiction. \(\square\)

For fixed positive \(A,K\), if \(h\le(\log q)^A\) and \(B=(\log q)^K\), condition (8.66) holds beyond an effective threshold: its left logarithm is \(O_{A,K}((\log\log q)^2)\), whereas its right logarithm is \(\log q-\log4\). Thus both the ramified-prime count and the small-split-prime count are at most a constant multiple of \(\log\log q\) in the range needed for the coefficient estimates.

**Corollary 8.17 (absorbing the ramified Euler loss).** For fixed real \(a,b\ge0\), set

\[
\Theta_{a,b}(D)=\prod_{p\mid D}
 (1+1/p)^{-a}
 \left(1+\frac{2\sqrt p}{p+1}\right)^{-b}.
\tag{8.67}
\]

For each \(\varepsilon>0\), there is an effectively computable \(c_{a,b,\varepsilon}>0\) such that, whenever \(q=|D|>4\) and \(h(D)\le\log q\),

\[
\Theta_{a,b}(D)\ge
c_{a,b,\varepsilon}(\log q)^{-\varepsilon}.
\tag{8.68}
\]

**Proof.** Write \(r=\omega(D)\), and order its prime factors increasingly. The \(j\)-th is at least \(j+1\), so elementary integral comparison gives

\[
\sum_{p\mid D}p^{-1/2}\le2\sqrt r,
\qquad \sum_{p\mid D}p^{-1}\le\log(r+1).
\]

Using \(\log(1+u)\le u\) and \(2\sqrt p/(p+1)\le2/\sqrt p\), we obtain

\[
\log\Theta_{a,b}(D)
\ge-a\log(r+1)-4b\sqrt r.
\tag{8.69}
\]

Lemma 8.15 gives \(r\le1+\log h/\log2\le1+\log\log q/\log2\). If \(t=\log\log q\), the negative lower bound in (8.69) is consequently no worse than
\(-a\log(2+t/\log2)-4b\sqrt{1+t/\log2}\). For large effective \(t\), its magnitude is at most \(\varepsilon t\), because each displayed term divided by \(t\) tends to zero. An explicit threshold can be found by the elementary derivatives of these two functions and increasing an integer search beyond their decreasing-ratio range. Below that threshold they have a computable finite supremum. Absorbing its exponential into \(c_{a,b,\varepsilon}\) proves (8.68), including the initial range. \(\square\)

Consequently a class-number estimate \(h(D)\ge c\Theta_{a,b}(D)\log|D|\), with fixed effective \(a,b,c\), would imply (8.1): if \(h>\log|D|\) the conclusion is immediate, and otherwise (8.68) supplies the required exponent \(1-\varepsilon\). Establishing that estimate still requires the main residue and its smoothed error.

### 8.9. A smaller conductor exponent and the square terms

The contour for the main term will pass through \(\operatorname{Re}s=1/2\) for the Dirichlet factor. A smaller conductor exponent is useful here; the already proved fourth-moment Burgess bound supplies it.

**Lemma 8.18 (a sufficient critical-line bound).** For every primitive nonprincipal character of conductor \(q\), every real \(t\), and every fixed \(\delta>0\),

\[
|L(1/2+it,\chi)|
\ll_\delta (1+|t|)q^{3/16+\delta}\log(2q).
\tag{8.70}
\]

The constant is effective. In particular \(\delta=1/64\) gives conductor exponent \(13/64<1/4\).

**Proof.** The full arbitrary-conductor \(r=2\) Burgess theorem in *Character sums: the Pólya–Vinogradov inequality*, Theorem 5.9, is already proved from its complete fourth moment and induction. Put \(A(u)=\sum_{n\le u}\chi(n)\). For \(1\le u\le q\), that theorem gives
\(|A(u)|\ll_\delta u^{1/2}q^{3/16+\delta}\).
For \(u\ge q\), remove complete periods and use the full Pólya–Vinogradov estimate to get \(|A(u)|\ll\sqrt q\log(2q)\). Partial summation continues the Dirichlet series to \(\operatorname{Re}s>0\) as
\(L(s,\chi)=s\int_1^\infty A(u)u^{-s-1}du\).
At \(s=1/2+it\), split the integral at \(q\). The first part has absolute value at most \(C_\delta q^{3/16+\delta}\int_1^qdu/u\); the second is at most \(C\sqrt q\log(2q)\int_q^\infty u^{-3/2}du=2C\log(2q)\). Multiplication by \(|s|\le1+|t|\) proves (8.70). Neither GRH nor the unfinished sixth-moment bound is used. \(\square\)

Retain the real normalized eigenform and the coprime twist from Section 8.6. At primes not dividing \(N\), its unitary Euler factor is
\((1-\lambda(p)z+z^2)^{-1}\). Let \(C\) be the squarefree product of the primes dividing \(Nq\) and the split primes at most a cutoff \(B\ge2\). The notation \(c\mid C^\infty\) means that every prime factor of \(c\) divides \(C\); it includes \(c=1\).

**Lemma 8.19 (the exact square separation).** For \((n,C)=1\),

\[
a_D(n)=\sum_{d^2m=n}\chi_D(d)\tau_D(m)\lambda(m).
\tag{8.71}
\]

Consequently the smoothed coefficient sum \(S\) in (8.57) is the absolutely convergent sum \(S_1+S_2+S_3\), where

\[
S_1=\sum_{c\mid C^\infty}\frac{a_D(c)}{\sqrt c}
 \sum_{(d,C)=1}\frac{\chi_D(d)}d
 \sum_{(m,C)=1}\frac{\lambda(m^2)}m
 V(cd^2m^2/Q),
\tag{8.72}
\]

\[
S_2=\sum_{c\mid C^\infty}\frac{a_D(c)}{\sqrt c}
 \sum_{(d,C)=1}\frac{\chi_D(d)}d
 \sum_{(m,C)=1}\frac{\{\tau_D(m^2)-1\}\lambda(m^2)}m
 V(cd^2m^2/Q),
\tag{8.73}
\]

and

\[
S_3=\sum_{c\mid C^\infty}\frac{a_D(c)}{\sqrt c}
 \sum_{(d,C)=1}\frac{\chi_D(d)}d
 \sum_{\substack{(n,C)=1\\
n\text{ not a square}}}
 \frac{\tau_D(n)\lambda(n)}{\sqrt n}V(cd^2n/Q).
\tag{8.74}
\]

**Proof.** The Euler recurrence \(u_{j+1}=\lambda(p)u_j-u_{j-1}\), \(u_0=1,u_1=\lambda(p)\), gives
\(u_a u_b=\sum_{j=0}^{\min(a,b)}u_{a+b-2j}\).
Here is an induction: for \(2\le a\le b\), replace \(u_a\) by \(\lambda(p)u_{a-1}-u_{a-2}\), and replace \(\lambda(p)u_b\) by \(u_{b+1}+u_{b-1}\). The two lower-index product formulas overlap; subtracting the one with \(a-2\) leaves exactly the indicated sum. The cases \(a=0,1\) follow directly. Multiplicativity gives

\[
\lambda(u)\lambda(v)=\sum_{d\mid(u,v)}\lambda(uv/d^2)
\quad((uv,N)=1).
\tag{8.75}
\]

Insert this into the convolution defining \(a_D(n)\), and set \(u=da,v=db\). The remaining sum over \(ab=m\) is \(\sum_{b\mid m}\chi_D(b)=\tau_D(m)\), proving (8.71). Because \(\lambda\) and \(\chi_D\) are multiplicative, so is \(a_D\); every index has a unique factorization into \(c\mid C^\infty\) and an integer coprime to \(C\). This gives the three sums after separating the remaining variable into squares and nonsquares and writing \(\tau_D(m^2)=1+(\tau_D(m^2)-1)\).

These rearrangements are absolutely justified even using only the elementary cusp bound \(|\lambda(n)|\ll\sqrt n\). Each coefficient has at most polynomial growth, and for every positive fixed \(Q\), (8.51) gives exponential decay in \(\sqrt{cd^2n/Q}\). The number of ways of factoring an index into \(c,d^2,n\) is at most a polynomial in the index. Thus the sum of the absolute values converges before any partition or rearrangement. \(\square\)

The square term has an exact Mellin expression in a right half-plane. Define there

\[
M(u)=\sum_{m\ge1}\frac{\lambda(m^2)}{m^u},\qquad
Z_C(u)=
\left(\sum_{c\mid C^\infty}\frac{a_D(c)}{c^{u/2}}\right)
\left(\sum_{(d,C)=1}\frac{\chi_D(d)}{d^u}\right)
\left(\sum_{(m,C)=1}\frac{\lambda(m^2)}{m^u}\right).
\tag{8.76}
\]

For \(\operatorname{Re}u>2\), all three series converge absolutely. Inserting (8.49) into (8.72), with its sum–integral absolute majorant, gives

\[
S_1=\frac2{2\pi i}\int_{(2)}
       Q^z\Gamma(1+z)^2Z_C(2z+1)\frac{dz}{z^3}.
\tag{8.77}
\]

In that half-plane, \(Z_C(u)=L(u,\chi_D)M(u)P_C(u)\), where \(P_C\) is the finite product obtained by removing the \(C\)-Euler factors from the last two series and inserting the first. At a prime \(p\mid C\) not dividing \(N\), write \(\alpha+\beta=\lambda(p)\), \(\alpha\beta=1\), \(x=p^{-u/2}\), and \(\chi=\chi_D(p)\). A direct even-coefficient extraction gives

\[
\sum_{e\ge0}\lambda(p^{2e})x^{2e}
=\frac{1+x^2}{(1-\alpha^2x^2)(1-\beta^2x^2)}.
\]

Consequently that factor of \(P_C\) is exactly

\[
P_p(u)=\frac{1-\chi x^2}{1+x^2}
        \frac{(1+\alpha x)(1+\beta x)}
             {(1-\chi\alpha x)(1-\chi\beta x)}.
\tag{8.78}
\]

Indeed its original expression has the four reciprocal factors for the two degree-two functions, multiplied by \((1-\chi x^2)\) and the reciprocal even-coefficient factor. Factoring \(1-\alpha^2x^2\) and \(1-\beta^2x^2\) cancels the two untwisted denominators and gives (8.78). This is an identity of convergent Euler products; moving (8.77) to its residue still requires the continuation and estimates for \(M\), and its positive main residue. The next subsection supplies the full bounds on \(S_2,S_3\).

**Corollary 8.20 (the good-prime cap is positive).** Suppose \(|\lambda(p)|\le2\) at the good primes in \(C\), and write \(P_C^{\mathrm{good}}\) for the product of (8.78) over those primes. At \(u=1\), with \(x=1/\sqrt p\), its factors are

\[
P_p(1)=\begin{cases}
\dfrac{1+\lambda(p)x+x^2}{1+x^2},&\chi_D(p)=0,\\[6pt]
\dfrac{1-x^2}{1+x^2}
 \dfrac{1+\lambda(p)x+x^2}{1-\lambda(p)x+x^2},&\chi_D(p)=1,\\[6pt]
1,&\chi_D(p)=-1.
\end{cases}
\tag{8.79}
\]

All these numbers are positive. If \(h\le\log q\), \(B=(\log q)^K\) with fixed \(K>0\), and \(q\) exceeds an effective threshold, then

\[
\exp(-C_N\sqrt{\log(2h)})
\le P_C^{\mathrm{good}}(1)
\le\exp(C_N\sqrt{\log(2h)}).
\tag{8.80}
\]

In particular, for every fixed \(\eta>0\), this product lies between effective positive constants times \(h^{-\eta}\) and \(h^\eta\).

**Proof.** Formula (8.79) is (8.78) with \(\alpha+\beta=\lambda(p)\), \(\alpha\beta=1\), including \(\chi=0\). The two quadratics \(1\pm\lambda(p)x+x^2\) lie between \((1-x)^2\) and \((1+x)^2\); their lower endpoints are positive. Since \(x\le1/\sqrt2\),
\(-\log(1-x)\le x/(1-x)<4x\), \(\log(1+x)\le x\), and \(-\log(1-x^2)\le2x^2\). These inequalities in (8.79) give \(|\log P_p(1)|\le16/\sqrt p\).

By Lemmas 8.15–8.16, the number of prime factors of \(C\) is at most \(\omega(N)+1+2\log_2h\) once (8.66) holds. Summing \(p^{-1/2}\) over that many distinct primes gives at most twice the square root of their number. This proves (8.80). Finally \(C_N\sqrt{\log(2h)}\le\eta\log h+C_{N,\eta}\) for a computable constant: set \(v=\sqrt{\log h}\), use \(\sqrt{\log(2h)}\le v+\sqrt{\log2}\), and complete the square in \(C_Nv-\eta v^2\). Exponentiation gives both power bounds. \(\square\)

**Corollary 8.21 (logarithmic derivatives of the cap).** In the same small-class-number range, for \(j=1,2\),

\[
\left|\frac{d^j}{du^j}\log P_C^{\mathrm{good}}(u)
                   \Big|_{u=1}\right|
\ll_{N,K,j}(\log\log q)^{j+1/2}.
\tag{8.81}
\]

**Proof.** Since the real numbers \(\lambda(p)\) lie in \([-2,2]\), their roots \(\alpha,\beta\) have absolute value one. Every factor \(1\pm\alpha p^{-u/2}\), \(1\pm\beta p^{-u/2}\), and \(1\pm p^{-u}\) is nonzero for \(\operatorname{Re}u>0\); use the holomorphic logarithm fixed at 1. Differentiating its convergent geometric logarithm series bounds the \(j\)-th derivative by
\(C_j(\log p)^j/\sqrt p\). The constant is uniform in the roots: the geometric sums have ratio at most \(1/\sqrt2\), also after inserting their polynomial powers of the summation index.

The small split primes contribute at most
\(C_{K,j}(\log\log q)^j\sqrt{\log(2h)}\), since \(\log p\le K\log\log q\) and their number is at most \(\log_2h\). For ramified primes divide at \(p=(\log q)^{2j+2}\). Below it, the same count from Lemma 8.15 bounds the sum by \(C_j(\log\log q)^j\sqrt{\log(2h)}\). Above it, use \(\log p\le\log q\) and \(\sum_{p\mid D}\log p\le\log q\) to get

\[
\sum_{\substack{p\mid D\\
p>(\log q)^{2j+2}}}
\frac{(\log p)^j}{\sqrt p}
\le\frac{(\log q)^{j-1}}{(\log q)^{j+1}}
      \sum_{p\mid D}\log p
\le\frac1{\log q}.
\]

The finitely many primes dividing \(N\) cost a fixed constant. Finally \(\log(2h)\ll\log\log q\) under \(h\le\log q\). This proves (8.81), with effective constants. \(\square\)

For the elliptic-curve forms used here, the bound \(|\lambda(p)|\le2\) at odd good primes follows from the complete quadratic-character bound in Lemma 5.2 of *Character sums*: the point count is \(p+1+\sum_x(\frac{F(x)}p)\), and the nonsingular cubic has three distinct geometric roots.

At 2 the required point counts are direct. An integral model of the classical twist, with \(\delta=-139\), is

\[
Y^2+Y=X^3+\delta X^2-3\delta^2X+(5\delta^3-1)/4.
\tag{8.82}
\]

It follows from (8.58) by \(X=\delta(x+2)/4\), \(Y=(\delta^2y/4-1)/2\); substitution gives the displayed equation. Its discriminant is \(37\delta^6\), so it is good at 2. Modulo 2 its right side is \(X^3+X^2+X\), giving two affine points and the origin. The integral model of \(E_0\) in Section 8.7 also has two affine points and the origin, so both traces at 2 are zero. The conductor-5077 model has four affine points and the origin, giving trace \(-2\) and normalized value \(-\sqrt2\). All satisfy the required bound. Thus the cap estimates use already proved curve support and explicit small-prime counts.

### 8.10. Bounding both smoothed error sums

The two error sums in (8.73)–(8.74) can be estimated using the ideal counts already proved. We give all the smoothing and infinite-tail steps. Throughout this subsection, \(f\) is one of the fixed elliptic-curve forms under consideration, \(q=|D|\), \(h=h(D)\), and

\[
h\le\log q,\qquad B=(\log q)^{100},\qquad
Q=\kappa q,\quad 0<\kappa<\infty\text{ fixed}.
\tag{8.83}
\]

All assertions below hold beyond an effective threshold depending on the fixed curve. Let \(C\) contain its bad primes, the primes dividing \(D\), and the split primes at most \(B\). A fixed finite enlargement of \(C\) is harmless.

Write \(d_k(n)\) for the number of ordered factorizations of \(n\) into \(k\) positive integers, so \(d_2=\tau\) and
\(d_k(p^e)=\binom{e+k-1}{k-1}\). We first establish the elementary majorants used in the sums.

**Lemma 8.22 (divisor and cap majorants).** At every prime,

\[
|\lambda(p^e)|\le e+1,\qquad
|a_D(p^e)|\le d_4(p^e),\qquad
\tau(m^2)^j\le d_{3^j}(m)\quad(j=1,2,3).
\tag{8.84}
\]

For \(\sigma=1/4,1/2,1\), put

\[
\nu_C(\sigma)=\sum_{c\mid C^\infty}
             \frac{|a_D(c)|}{c^\sigma}.
\]

Then

\[
\nu_C(1)\le\nu_C(1/2)
\le\exp(C_f\sqrt{\log(2h)}),\qquad
\nu_C(1/4)\le
\exp(C_f(\log(2h))^{3/4}).
\tag{8.85}
\]

**Proof.** At a good prime the Hecke recurrence has roots of absolute value one, and its \(e\)-th coefficient is the sum of the \(e+1\) monomials \(\alpha^{e-i}\beta^i\). At a bad elliptic-curve prime the local factor is either 1 or \((1-\epsilon p^{-1/2}p^{-s})^{-1}\), with \(\epsilon=\pm1\), by the local factors specified in Section 8.2. Its coefficients also obey the first bound. The two-factor convolution defining \(a_D\) gives
\(\sum_{i=0}^e(i+1)(e-i+1)=\binom{e+3}{3}\), proving the second.

For the last bound, \(2e+1\le\binom{e+2}{2}\), since their difference is \(e(e-1)/2\). Also
\(d_k(p^e)d_l(p^e)\le d_{kl}(p^e)\). To prove this inequality, take weak compositions of \(e\) into \(k\) row totals and into \(l\) column totals. Fill a \(k\)-by-\(l\) nonnegative integer table by repeatedly putting the smaller remaining row or column total in the current cell and advancing past each exhausted row or column. This gives a table with those margins. The table recovers both original compositions, so this map into the weak compositions of \(e\) into \(kl\) entries is injective. Applying it twice and multiplying over primes proves all three powers in (8.84).

Absolute convergence of each local geometric series now gives

\[
\nu_C(\sigma)\le\prod_{p\mid C}(1-p^{-\sigma})^{-4}.
\tag{8.86}
\]

For fixed \(\sigma>0\), \(-\log(1-p^{-\sigma})\le
p^{-\sigma}/(1-2^{-\sigma})\). If \(r\) distinct primes are ordered increasingly, their \(j\)-th member is at least \(j+1\); hence
\(\sum_{p\mid C}p^{-\sigma}\le C_\sigma r^{1-\sigma}\) for \(0<\sigma<1\), by integrating \(t^{-\sigma}\). Lemmas 8.15–8.16 give \(r\ll_f\log(2h)\). Their cutoff condition holds effectively in (8.83):
\((1+\log_2h)\log B=O((\log\log q)^2)<\log(q/4)\) eventually. Insert this bound into (8.86), at \(\sigma=1/2,1/4\), and use the termwise inequality at \(\sigma=1\). This proves (8.85). The proof still applies if finitely many factors \(a_D(p^e)\) are replaced by a convolution of two elliptic-curve local factors. \(\square\)

The positive kernel also has the precise moments needed for partial summation. Differentiation of its integral in Lemma 8.12 gives

\[
-V'(y)=\frac2y\int_y^\infty\phi(t)\log(t/y)\,dt>0.
\tag{8.87}
\]

The boundary terms vanish because the logarithm is zero at \(t=y\). Differentiation under the integral follows by domination on compact subintervals of \(y>0\); the exponential upper bound for \(\phi\) proved there handles infinity. Consequently \(V\) is decreasing. For \(s>0\), integration by parts and the Mellin transform already proved give

\[
\int_0^\infty y^s(-V'(y))\,dy
=\frac{2\Gamma(1+s)^2}{s^2},\qquad
\int_0^\infty\sqrt y(-V'(y))\,dy=2\pi.
\tag{8.88}
\]

Both endpoints vanish by (8.51). We also have
\(\int_0^\infty\sqrt y\log^+y(-V'(y))\,dy<\infty\): for example \(\log y\le y^{1/4}/(1/4)\) for \(y\ge1\), so (8.88) at \(s=3/4\) bounds it explicitly.

**Lemma 8.23 (smoothed divisor tails).** For fixed \(k\ge1\), \(X\ge1\),

\[
\sum_{r\ge1}\frac{d_k(r)}r V(r^2/X)
\le C_k(1+\log X)^{k+2}.
\tag{8.89}
\]

If \(\mathcal P\) denotes the split primes exceeding \(B\), then

\[
\sum_{r\ge1}\frac{d_k(r)}r
 \mathbf1_{\exists p\in\mathcal P:\ p\mid r} V(r^2/X)
\le C_k(1+\log X)^{k+2}
       \left(\frac hB+\frac h{\sqrt q}(1+\log X)\right).
\tag{8.90}
\]

**Proof.** For every \(T\ge1\), expanding ordered factorizations gives
\(\sum_{r\le T}d_k(r)/r\le H_{\lfloor T\rfloor}^k
\le(1+\log T)^k\). For \(r\le\sqrt X\), the bound
\(V(r^2/X)\le16(1+\log X)^2\) proves the corresponding part of (8.89). On
\(2^j\sqrt X<r\le2^{j+1}\sqrt X\), \(j\ge0\), use
\(V(r^2/X)\le32e^{-2^j}\), and bound the harmonic sum by
\((1+\tfrac12\log X+(j+1)\log2)^k\). The resulting series is at most
\(C_k(1+\log X)^k\), since
\(\sum_{j\ge0}e^{-2^j}(j+2)^k\) converges effectively. This handles the entire infinite tail.

For the second inequality, unique factorization at a fixed prime yields

\[
\begin{aligned}
\sum_{\substack{r\le T\\p\mid r}}\frac{d_k(r)}r
&\le\left((1-1/p)^{-k}-1\right)(1+\log T)^k\\
&\le\frac{C_k}{p}(1+\log T)^k.
\end{aligned}
\tag{8.91}
\]

The last constant is uniform for \(p\ge2\), by the mean value theorem on \(0\le1/p\le1/2\). Sum over \(B<p\le T\) that split; the union bound only enlarges the sum. Since \(\tau_D(p)=2\) for such primes, (8.29) gives

\[
\sum_{\substack{B<p\le T\\
p\text{ split}}}\frac1p
\le\frac hB+\frac{8h}{\sqrt q}(1+\log T).
\tag{8.92}
\]

If \(T<B\), the sum is empty, and the same upper bound remains valid. Apply (8.91)–(8.92) below \(\sqrt X\) and on every dyadic interval used above. In the latter, \(\log T\le\tfrac12\log X+(j+1)\log2\); its extra polynomial in \(j\) is still summable against \(e^{-2^j}\). This proves (8.90) and explicitly includes primes and integers beyond every finite cutoff. \(\square\)

**Proposition 8.24 (the two errors).** In the range (8.83),

\[
\begin{aligned}
|S_2|&\le C_f\nu_C(1/2)(1+\log Q)^{30}
       \left(\frac hB+\frac h{\sqrt q}(1+\log Q)\right),\\
|S_3|&\le C_f\nu_C(1/2)
       \left(\frac{2h}{\sqrt B}+\frac{h^2}B\right)
                    (1+\log Q)^{12}\\
&\quad+C_f\nu_C(1)
       \left(h+\frac{h^2}B+
                \frac{h^2}{\sqrt q}(1+\log Q)\right).
\end{aligned}
\tag{8.93}
\]

In particular, after increasing an effective threshold,

\[
|S_2|\le1,\qquad
|S_3|\le C_f h\exp(C_f\sqrt{\log(2h)})+1.
\tag{8.94}
\]

**Proof.** Outside \(C\), \(\tau_D(p^{2e})\) is \(2e+1\) at a split prime and 1 at an inert prime. Thus \(\tau_D(m^2)-1\) vanishes unless \(m\) contains a split prime exceeding \(B\), and
\[
|\lambda(m^2)|(\tau_D(m^2)-1)
\le\tau(m^2)^3\,
       \mathbf1_{\exists p\in\mathcal P:\ p\mid m}
\le d_{27}(m)\,
       \mathbf1_{\exists p\in\mathcal P:\ p\mid m}.
\]
Take absolute values in (8.73), drop coprimality restrictions, and put \(r=dm\). The divisor convolution \(1*d_{27}=d_{28}\) and the containment \(p\mid m\Rightarrow p\mid r\) bound its inner sums by
\(\sum_r d_{28}(r)r^{-1}
\mathbf1_{\exists p\in\mathcal P:p\mid r}V(cr^2/Q)\).
Since \(c\ge1\), monotonicity of \(V\) permits replacing \(c\) by 1. Summing the remaining \(c\)-weights gives \(\nu_C(1/2)\), and (8.90) with \(k=28,X=Q\) proves the first part of (8.93).

For \(S_3\), write the nonsquare variable uniquely as \(n=am^2\), with \(a>1\) squarefree. If its coefficient is nonzero, every prime of \(a\) splits and exceeds \(B\). At each prime,
\(\tau_D(am^2)\le\tau_D(a)\tau_D(m^2)\) and
\(\tau(am^2)\le\tau(a)\tau(m^2)\). Consequently its absolute coefficient is at most
\(\tau(a)\tau_D(a)d_9(m)\), by (8.84). For \(0<T\le Q\), define
\[
G(T)=\sum_{\substack{a>1\text{ squarefree}\\(a,C)=1}}
\frac{\tau(a)\tau_D(a)}{\sqrt a}V(a/T).
\]
Its counting function \(F(A)\) vanishes for \(A\le B\). Lemma 8.9, with \(d=q/4\), bounds it, for \(A\ge B\), by
\[
F(A)\le k_0+C\sqrt A
 \left(\frac h{\sqrt q}+\frac{h^2}{B\sqrt q}
                     +\frac{h^2}q(1+\log A)\right),
\quad k_0=\frac{2h}{\sqrt B}+\frac{h^2}B.
\]
Exact Stieltjes integration therefore gives
\(G(T)=\int_B^\infty F(A)(-V'(A/T))\,dA/T\).
There is no upper endpoint: its limit is zero by the kernel's exponential decay and the displayed polynomial bound. The constant part integrates to \(k_0V(B/T)\). In the other part set \(A=Ty\), use
\(\log A\le\log Q+\log^+y\), and apply (8.88). The result is

\[
G(T)\le k_0V(B/T)+C\sqrt T
 \left(\frac h{\sqrt q}+\frac{h^2}{B\sqrt q}
                  +\frac{h^2}q(1+\log Q)\right).
\tag{8.95}
\]

Insert \(T=Q/(cd^2m^2)\) in the absolute sum for \(S_3\). The \(\sqrt T\) term has the convergent majorant
\[
\sqrt Q\sum_{c\mid C^\infty}\frac{|a_D(c)|}{c}
     \sum_{d\ge1}\frac1{d^2}
     \sum_{m\ge1}\frac{d_9(m)}{m^2}
=\sqrt Q\nu_C(1)\zeta(2)^{10}.
\]
As \(Q=\kappa q\), this is the last line of (8.93). For the constant term in (8.95), putting \(r=dm\) gives \(1*d_9=d_{10}\); its kernel is
\(V(Bcr^2/Q)\le V(r^2/Q)\). Equation (8.89) with \(k=10\) gives the other line of that bound.

Finally let \(t=\log q\). Then \(h\le t\), \(B=t^{100}\), \(1+\log Q\ll_f t\), and
\(\nu_C(1/2)\le\exp(C_f\sqrt{\log(2t)})\le t\)
eventually, with a computable threshold by squaring the logarithmic inequality. All the terms in (8.93) except \(C_fh\nu_C(1)\) tend to zero: the power terms have exponents at most \(32-100\), \(14-50\), or \(15-100\), and the remaining terms are fixed powers of \(t\) times \(e^{-t/2}\). Increasing the threshold makes their finite sum at most 1 in each estimate. Use (8.85) for the surviving term to obtain (8.94). Every constant and threshold is effective. \(\square\)

This argument is unchanged when the second elliptic-curve form has coefficients \(\lambda(n)\chi_D(n)\) only for \((n,C)=1\): put the actual convolution coefficients in the \(c\)-sum. The proof used the twist identity outside \(C\) and the divisor bound (8.84) inside it. This observation will account for cancellation of a fixed ramified twisting prime without deleting its regained Euler factor.

### 8.11. Ramified twists and the fourth zero for every discriminant

We now use the rank certificate of Section 8.7 to remove the coprimality restriction. Put
\[
E_0:\ Y^2+Y=X^3+X^2-3X+1,\qquad
E_*=E_0\otimes\chi_{-139}.
\tag{8.96}
\]
The twist notation describes an elliptic curve over \(\mathbf Q\), not the series obtained by setting every coefficient at a ramified prime to zero. These agree away from the twisting conductor; at its primes we use the actual local parameter.

Here are the exact internal local inputs. In *Galois representations*, *Weil–Deligne representations and monodromy*, Section 6, equation (22) and Theorem 6.1, give the conductor, epsilon determinant and special-block formulas. They are written. *Elliptic curves over local fields*, Theorems 4.1–5.1, identify good and multiplicative parameters, with the geometric antecedents specified in Section 8.2. In *Adèles, idèles and Tate's thesis*, *Quasi-characters and Hecke characters*, Proposition 6.4 and equations (23)–(27), construct the global quadratic character and its local restrictions; *Tate's local functional equation*, Theorem 7.3 and Proposition 7.4, prove the Gauss formulas and dual-product identity. These are written. The archimedean weight-two epsilon is \(-1\), by *Local Langlands over the real numbers*, equation (4.3). The comparison of these parameters and epsilon factors with those of the modular form is the exact local–global compatibility theorem in *Local–global compatibility*, equation (3.1), and modularity in the existing *Global Langlands conjectures and functoriality* lesson 10. Their deep proof antecedents remain planned. The global modular functional equation multiplies these local epsilon factors, as required in that modularity and compatibility input. We perform the resulting twist computations in full below.

**Lemma 8.25 (the prime-level quadratic twist signs).** Let \(\rho\) be any primitive quadratic Dirichlet character, including the trivial character, and let \(m\) be its conductor. Then
\[
\begin{aligned}
N(E_0\otimes\rho)&=
\begin{cases}37m^2,&37\nmid m,\\
m^2,&37\mid m,\end{cases}\\[4pt]
w(E_0\otimes\rho)&=
\begin{cases}\rho(-1)\rho(37),&37\nmid m,\\
-\rho(-1),&37\mid m.\end{cases}
\end{aligned}
\tag{8.97}
\]

**Proof.** The invariants of \(E_0\) are \(\Delta=37,c_4=160,c_6=-2008\). Thus its model is good at every prime other than 37, including 2, and is minimal and multiplicative at 37. It is split: \(-c_6\equiv10=11^2\pmod {37}\). For completeness, the square criterion follows by changing, over the residue field of odd characteristic greater than 3, to a short nodal cubic \(y^2=(x-r)^2(x+2r)\). Its tangent coefficient is \(3r\), while \(-c_6=1728r^3=(24r)^2(3r)\). The unit changes of coordinates alter \(c_6\) by a sixth power and preserve this criterion. Hence the unitary parameter at 37 is the centered special block, with conductor 1 and root \(-1\).

Let \(\rho_p\) be the associated local quadratic character, and let \(a_p\) be its conductor exponent. At a good prime the untwisted parameter is an unramified two-dimensional representation of determinant 1. If \(a_p=0\), twisting preserves goodness, conductor 0 and root 1. If \(a_p>0\), its two Frobenius characters become ramified and have no inertia invariants. Its conductor is \(2a_p\). The unramified factors in their epsilon constants multiply to the determinant raised to \(a_p\), which is 1. The remaining root is the square of the normalized quadratic Gauss constant, and therefore
\[
w_p(E_0\otimes\rho)=\rho_p(-1).
\tag{8.98}
\]
This includes wild quadratic characters at 2: Proposition 7.4's character dual-product identity says directly that the square of their central constant is \(\rho_p(-1)\). No tame-only formula has been used.

At 37, an unramified twist has conductor 1 and root \(-\rho(37)\), by the special-block determinant. A ramified twist has no inertia invariants, so its monodromy determinant correction is 1, its conductor is \(2a_{37}\), and its smooth epsilon is the product for the two characters \(\rho_{37}|\cdot|^{1/2}\) and \(\rho_{37}|\cdot|^{-1/2}\). Their positive norm factors cancel at the center, leaving \(\rho_{37}(-1)\), by the same character dual-product identity. This is the ramified special-block formula, rather than an application of the coprime twist rule.

At infinity a quadratic sign twist leaves the weight-two parameter isomorphic to itself: on its two induced lines, changing the sign of the matrix for \(j\in W_{\mathbf R}\setminus\mathbf C^\times\) is conjugation by \(\operatorname{diag}(1,-1)\). Its root remains \(-1\). Since the global character is trivial on the rational number \(-1\),
\(\prod_{p<\infty}\rho_p(-1)=\rho(-1)\). Unramified local characters are 1 on \(-1\), so the product is over the ramified primes. Multiplying (8.98), the 37 factor and the infinity factor gives both signs in (8.97). Multiplying the prime-power conductor factors gives its two conductor formulas. \(\square\)

**Proposition 8.26 (a fixed triple zero and the full fourth-zero alternative).** The curve \(E_*\) has conductor \(37\cdot139^2\), root \(-1\), and analytic vanishing order at least three. For every negative fundamental discriminant \(D\), one of the following holds:
\[
h(D)\ge\frac{\log(|D|/4)}{\log37},
\quad\text{or}\quad
L(E_*,s)L(E_*\otimes\chi_D,s)
\text{ vanishes to order at least four at }s=1.
\tag{8.99}
\]
In the second case both individual roots are \(-1\).

**Proof.** The character \(\chi_{-139}\) is primitive and odd, of conductor 139, and \(\chi_{-139}(37)=1\), by direct quadratic reciprocity or residue evaluation. Lemma 8.25 gives its conductor and root. Proposition 8.14 proves rational rank at least two. If the odd analytic order were 1, the precise low-rank Gross–Zagier–Kolyvagin theorem in Section 8.2 would give rational rank 1. Thus the order is at least three.

If \(\chi_D(37)=1\), the prime splits and Lemma 8.5 gives the first inequality in (8.99). Otherwise \(\chi_D(37)=-1\) or 0. Form the primitive quadratic character \(\rho\) associated with the product of the two global characters \(\chi_{-139}\chi_D\). It is even. If 37 is unramified, its value there is \(-1\), since \(\chi_{-139}(37)=1\). Lemma 8.25 gives root \(-1\). If 37 is ramified, that lemma again gives root \(-1\), now from its second case. The curve \(E_*\otimes\chi_D\) is precisely \(E_0\otimes\rho\): the two isomorphism cocycles multiply. It consequently has an odd central zero of order at least one. Add the three zeros of \(E_*\) to obtain the second alternative. This argument includes simultaneous ramification at 37 and 139. \(\square\)

We make the conductor cancellation and coefficient corrections explicit, since they enter the smoothing identity. Let \(m\) again be the conductor of \(\rho\). At 139 the two ramified quadratic unit characters cancel if \(139\mid D\), and otherwise only \(\chi_{-139}\) is ramified. At every other finite prime that fixed character is unramified, so it cannot change the least unit-conductor exponent of \(\chi_D\). In particular it does not change that exponent at 2. Hence
\[
\begin{aligned}
m&=\begin{cases}139q,&139\nmid D,\\q/139,&139\mid D,\end{cases}\\[4pt]
Q&=\frac{\sqrt{N(E_*)N(E_*\otimes\chi_D)}}{4\pi^2}
=\kappa q,
\end{aligned}
\tag{8.100}
\]
where \(\kappa\) belongs to the fixed four-element set
\[
\left\{\frac{37\cdot139^2}{4\pi^2},
\frac{37}{4\pi^2},
\frac{\sqrt{37}\,139^2}{4\pi^2},
\frac{\sqrt{37}}{4\pi^2}\right\}.
\tag{8.101}
\]
The first two correspond to \(37\nmid D\); the other two to \(37\mid D\). A primitive odd-prime quadratic character has conductor exponent 1, so these are all possibilities. The trivial product when \(D=-139\) is included.

Let \(\lambda_*(n)\) and \(\lambda_g(n)\) be the actual unitary coefficients of these two curves and put
\[
\begin{aligned}
b_D(n)&=\sum_{uv=n}\lambda_*(u)\lambda_g(v),\\
C&=\operatorname{rad}(2\cdot37\cdot139\cdot D)
       \prod_{\substack{p\le B\\
p\text{ split},\ p\nmid2\cdot37\cdot139\cdot D}}p.
\end{aligned}
\tag{8.102}
\]
For \((n,C)=1\), \(\lambda_g(n)=\lambda_*(n)\chi_D(n)\). The proof of Lemma 8.13 applies to the two actual modular completions with (8.100): their product has root 1, so the second alternative of (8.99) gives
\[
\sum_{n\ge1}\frac{b_D(n)}{\sqrt n}V(n/Q)=0.
\tag{8.103}
\]
The square/nonsquare partition (8.72)–(8.74) remains exact with \(b_D(c)\) in place of \(a_D(c)\); the twist identity is used only outside \(C\). Proposition 8.24 applies with this same replacement.

The good-prime factors of the square cap are still (8.78). At 37 put \(r=37^{-1/2}\), \(x=37^{-u/2}\), \(\chi=\chi_D(37)\). The first form has factor \((1-rx)^{-1}\); the second has \((1-\chi rx)^{-1}\) if \(\chi\ne0\), and factor 1 if \(\chi=0\). Dividing by the removed character and square-series factors gives
\[
P_{37}(u)=(1-\chi x^2)\frac{1+rx}{1-\chi rx}.
\tag{8.104}
\]
At 139 the first form has factor 1. If \(139\nmid D\), the second also has factor 1, and
\(P_{139}(u)=1-\chi_D(139)139^{-u}\). If \(139\mid D\), the second regains a good factor, with real normalized trace \(\lambda_g(139)\), and
\[
P_{139}(u)=
\frac1{1-\lambda_g(139)139^{-u/2}+139^{-u}}.
\tag{8.105}
\]
At 2 the first form is good, and its trace is zero by (8.82). If \(\chi_D\) is ramified there, twisting its unramified parameter gives no invariants and factor 1; otherwise its two roots are twisted by \(\chi_D(2)\). Thus (8.78) applies at 2 as well.

Every factor (8.104)–(8.105) is positive at \(u=1\), holomorphic and nonzero for \(\operatorname{Re}u>0\). For (8.105) use the two good-prime roots of absolute value one; for (8.104) use \(|r|<1\). Their values, reciprocals and first two logarithmic derivatives at 1 are bounded by constants independent of \(D\): at 37 there are three cases, at 139 there are two ramification cases and two possible unramified quadratic twists of the fixed good parameter. On \(\operatorname{Re}u=1/2\) these fixed factors and their reciprocals are likewise uniformly bounded. This proves that the finite correction preserves (8.80)–(8.81), with constants for \(E_*\). In particular, the regained Euler factor in (8.105) has been included explicitly.

### 8.12. The positive residue and effective class-number growth

We finish the analytic reduction. Its automorphic input belongs to two existing lessons of *Global Langlands conjectures and functoriality*. Lesson 6, *Symmetric powers, tensor products and the Ramanujan conjecture*, Outline 1, supplies Gelbart–Jacquet symmetric-square automorphy with its local parameters and the criterion that the lift is cuspidal exactly when the original representation is not dihedral. Its full proof is planned in that course. In *L-functions for general linear groups*, Theorem 1.1 supplies entire standard continuation, the conductor-normalized functional equation and boundedness of the completion in closed vertical strips; Theorem 3.1 supplies the simple pole at 1 of the self Rankin–Selberg function of a unitary cuspidal representation. Those statements are written, while their integral-theory proofs are planned under the programme's full-proof requirement. Their needed generality is \(GL_3\) standard functions and \(GL_2\)-by-\(GL_2\) self-pairings at the fixed levels 37 and 5077. They do not use imaginary quadratic class-number bounds. We use their exact statements, then prove the positivity, effective constants, local corrections, residue, contour error and class-number deduction here.

The prime-level forms for \(E_0\) and the conductor-5077 curve are not dihedral. Their local parameters at their multiplicative primes have nonzero monodromy, by the local computations in Sections 8.2 and 8.11. A dihedral representation is induced from a character of a quadratic extension, and its local parameter is a sum or induction of one-dimensional parameters. These have zero monodromy, as does their induction. Thus the symmetric-square lifts of these two forms are cuspidal. The local-parameter assertion used in this test is part of the indicated symmetric-square/dihedral prerequisite, with local–global compatibility as in Section 8.11.

**Lemma 8.27 (the fixed square series).** For \(f\) corresponding to \(E_0\), \(E_*\), or the conductor-5077 curve, the series
\[
M(u)=\sum_{m\ge1}\frac{\lambda(m^2)}{m^u}
\tag{8.106}
\]
continues holomorphically to \(\operatorname{Re}u\ge1/2\), meaning a neighborhood of each point of that closed half-plane. On each fixed strip there with bounded upper real part it has a polynomial bound in the height. Moreover \(M(1)>0\), and its value and any fixed number of derivatives at 1 are effectively computable constants of the fixed curve.

**Proof.** First take a prime-level base curve, with multiplicative prime \(p_0=37\) or 5077, and write \(T(u)=L(u,\operatorname{Sym}^2f)\). At a good prime the three roots are \(\alpha^2,1,\beta^2\). The even-coefficient identity in Section 8.9 gives
\[
M_p(u)=\frac{1+p^{-u}}{(1-\alpha^2p^{-u})(1-\beta^2p^{-u})}
=\frac{T_p(u)}{\zeta_p(2u)}.
\]
At the multiplicative prime, \(\lambda(p_0^e)=(\epsilon/\sqrt{p_0})^e\), so
\(M_{p_0}(u)=(1-p_0^{-u-1})^{-1}\). The symmetric-square special parameter has a one-dimensional monodromy kernel of Frobenius eigenvalue \(p_0^{-1}\); hence its standard factor is that same expression. Therefore
\[
M(u)=\frac{T(u)}{\zeta(2u)(1-p_0^{-2u})}.
\tag{8.107}
\]
All equalities initially converge absolutely for \(\operatorname{Re}u>1\), by the divisor bounds. The denominator's finite factor has no zero for \(\operatorname{Re}u>0\). Zeta has no zero for \(\operatorname{Re}(2u)\ge1\); its pole at \(u=1/2\) makes its reciprocal holomorphic there. The required zeta-line and reciprocal results are the written *Nonvanishing on the line one and a zero-free region*, Theorems 3.2 and 4.1. The standard automorphic theorem gives the entire function \(T\), so (8.107) proves the asserted holomorphy.

Here are sufficient height bounds and their effectivity. The symmetric-square coefficients have absolute value at most \(d_3(n)\): the good roots have absolute value one, and the bad root is \(p_0^{-1}\). Its conductor is \(p_0^2\), because the special block has conductor 2. At infinity the symmetric square of the weight-two parameter is the sum of a sign character and the induction of the angular character of degree 2; its Gamma factor is
\(G(u)=\Gamma_{\mathbf R}(u+1)\Gamma_{\mathbf C}(u+1)\).
The sign character has epsilon \(i\), and the induced degree-two character has epsilon \(i^3\), so their product is 1. The length-three special block also has root 1. Thus the fixed completion
\[
\mathcal B(u)=p_0^u G(u)T(u)
\quad\text{satisfies}\quad
\mathcal B(u)=\mathcal B(1-u).
\tag{8.108}
\]
These parameter computations use the same written special-block and real-parameter formulas as Section 8.11; the automorphic theorem supplies the global equation.

On \(\operatorname{Re}u=2\), the coefficient bound gives \(|T(u)|\le\zeta(2)^3\). On \(\operatorname{Re}u=-1\), (8.108) and the vertical Gamma ratio give
\(|T(u)|\le C_{p_0}(1+|\operatorname{Im}u|)^{9/2}\); on the compact part the same quotient is regular and bounded explicitly. To extend a polynomial bound across this strip, divide \(T(u)\) by \((u+4)^6\), multiply by \(e^{\delta u^2}\), \(\delta>0\), and apply the maximum principle on expanding rectangles. Boundedness of \(\mathcal B\) in the strip and the reciprocal Gamma estimates bound \(T\) there by a fixed exponential in the height times a polynomial, so the horizontal edges tend to zero after the Gaussian multiplier. The two vertical edges have a uniform bound at most \(C_{p_0}e^{16\delta}\). Let \(\delta\downarrow0\). This proves a polynomial bound with an effective constant, determined by the boundary estimates. To the right of 2 the absolutely convergent series suffices. The reciprocal zeta bound on \(\operatorname{Re}(2u)\ge1\) costs at most a logarithm in the height; the finite factor in (8.107) is bounded on \(\operatorname{Re}u\ge1/2\). This proves the stated bound for \(M\).

We justify positivity independently of the signs of its coefficients. Put
\(D_f(u)=\sum_{n\ge1}\lambda(n)^2n^{-u}\), which has nonnegative coefficients. The Hecke identities give
\[
D_f(u)=\zeta(u)M(u)(1-p_0^{-u}),\qquad
L(u,f\times f)=\zeta(2u)D_f(u)(1+p_0^{-u}).
\tag{8.109}
\]
At a good prime these follow by summing the Hecke recurrence. At the bad prime, \(D_{f,p_0}=M_{p_0}\), while the centered special tensor square has two monodromy-kernel eigenvalues \(p_0^{-1},1\), and hence factor
\(((1-p_0^{-u-1})(1-p_0^{-u}))^{-1}\).
This tensor calculation is also written in *Local factors*, Section 5, equation (5.1). It proves the extra factor \(1+p_0^{-u}\) in (8.109).

The self Rankin–Selberg theorem gives a simple pole at 1; its archimedean factors are finite and nonzero there, so the finite function has the same pole. Its other factors in (8.109) are positive, finite and nonzero there, so \(D_f\) has a simple pole. Its residue must be positive: for real \(u>1\), \((u-1)D_f(u)>0\), its limit is the real residue, and that residue is nonzero. Taking residues in the first identity yields
\[
M(1)=\frac{\operatorname*{Res}_{u=1}D_f(u)}{1-1/p_0}>0.
\tag{8.110}
\]

For \(f=E_*\), the squared-index coefficients agree with those of \(E_0\) away from 139, and its 139 factor is 1. Thus
\[
M_*(u)=\frac{M_0(u)}{M_{0,139}(u)},\qquad
M_{0,139}(u)=
\frac{1+139^{-u}}{(1-\alpha_{139}^2 139^{-u})(1-\beta_{139}^2 139^{-u})}.
\tag{8.111}
\]
The extra reciprocal is holomorphic and bounded on each closed half-plane with positive real part, and is positive at 1: its denominator pair is a conjugate pair, with nonzero product. This transfers holomorphy, growth and positivity to \(M_*\).

Finally, positivity here gives an effective positive constant, not an ineffectively chosen value. To see computability explicitly, consider
\(I_a=(2\pi i)^{-1}\int_{(2)}\mathcal B(a+z)e^{z^2}dz/z\), for \(a=0,1\). Moving the contour for \(I_1\) to \(-2\), and using (8.108), gives
\(\mathcal B(1)=I_1+I_0\). On both right-hand integrals the series for \(T\) converges absolutely. Its coefficients are computable from finite point counts and the local polynomials. Truncating them at \(n\le R\) has an explicit error tending to zero, because
\(\sum_{n>R}d_3(n)n^{-2}\ll(1+\log R)^2/R\).
For this bound, count ordered factorizations to get
\(\sum_{n\le x}d_3(n)\le x(1+\log x)^2\), and integrate by parts. The Gamma factors on the lines of real part 2 and 3, together with \(e^{z^2}\), give an explicit Gaussian height tail. Finite-interval quadrature is effective using the Gamma integral and its derivatives. We can therefore enclose \(T(1)\), and then \(M(1)\), in rational intervals with lengths tending to zero. Since (8.110)–(8.111) prove it positive, this process eventually gives a positive rational lower bound. The same integrals with differentiated factors, or Cauchy's formula in a fixed small disk about 1, compute the needed derivatives. All constants used below can thus be found by terminating computations. \(\square\)

**Proposition 8.28 (the residue).** Use the actual coefficient product and cap of Section 8.11 in the nonsplit-at-37 alternative of (8.99). Beyond an effective threshold,
\[
S_1\ge c_*\log q\,
             e^{-C_*\sqrt{\log(2h)}}-1,
\tag{8.112}
\]
where \(c_*,C_*>0\) are effective constants of the fixed curve.

**Proof.** The right-half-plane identity (8.77) holds for the actual coefficients \(b_D(c)\), with
\(Z_C(u)=L(u,\chi_D)M_*(u)P_C(u)\).
All the bad factors in this cap were computed in (8.104)–(8.105); in particular they are positive at 1 and uniformly bounded with their first two logarithmic derivatives. The good factors satisfy (8.80)–(8.81).

Shift its \(z\)-line from 2 to \(-1/4\). In this strip, \(u=1+2z\) has real part at least \(1/2\). Lemma 8.27 and the cap formulas show that the only pole crossed is \(z=0\), from \(z^{-3}\). On the new line Lemma 8.18 gives
\[
|L(1/2+2it,\chi_D)|
\le C(1+|t|)q^{13/64}\log(2q).
\]
At every good prime of \(C\), formula (8.78), on \(\operatorname{Re}u=1/2\), bounds the absolute logarithm of the factor by \(C p^{-1/4}\): each denominator has ratio at most \(2^{-1/4}<1\), so its geometric logarithm has this bound uniformly in the height. Summing over the \(O_*(\log(2h))\) primes, and including the bounded fixed bad factors, gives
\[
|P_C(1/2+2it)|\le
\exp(C_*(\log(2h))^{3/4}).
\tag{8.113}
\]
Lemma 8.27 bounds \(M_*\) by a polynomial times a logarithm in the height. The two factors \(\Gamma(3/4+it)\) give exponential decay \(e^{-\pi|t|}\) times a polynomial. Since \(Q=\kappa q\), the integral on the shifted line consequently has error
\[
|\mathcal E|\le
C_*q^{-3/64}\log(2q)
 \exp(C_*(\log(2h))^{3/4}).
\tag{8.114}
\]
The saving is \(1/4-13/64=3/64\). The same cap bound holds uniformly across the shifting strip. The elementary periodic integral for the character gives a polynomial height bound on every \(\operatorname{Re}u\ge1/2\), so the horizontal integrals tend to zero by the Gamma decay. This justifies the shift, rather than only estimating its new edge. Under \(h\le\log q\), (8.114) tends to zero effectively; in particular it is at most 1 beyond a computable threshold.

Set
\[
R(z)=Q^z\Gamma(1+z)^2 M_*(1+2z)P_C(1+2z).
\]
Multiplication of the Taylor series, including the factor 2 in (8.77), gives the exact residue
\[
S_1=4L''(1,\chi_D)R(0)+
    4L'(1,\chi_D)R'(0)+
      L(1,\chi_D)R''(0)+\mathcal E.
\tag{8.115}
\]
The chain-rule factors 2 in the character argument are essential here. Lemma 8.27 and the cap bounds give
\[
\begin{aligned}
R(0)&\ge c_*e^{-C_*\sqrt{\log(2h)}}>0,\\
R'(0)/R(0)&=\log Q+O_*((\log\log q)^{3/2}),\\
|R''(0)|/R(0)&\ll_* (\log q)^2.
\end{aligned}
\tag{8.116}
\]
Indeed the first logarithmic derivative is
\(\log Q+2\Gamma'(1)+2M_*'(1)/M_*(1)+2P_C'(1)/P_C(1)\).
The second logarithmic derivative is
\(2(\Gamma'/\Gamma)'(1)+4(\log M_*)''(1)+4(\log P_C)''(1)\).
Its size is \(O_*((\log\log q)^{5/2})\); adding the square of the first yields the last bound in (8.116).

Lemma 8.10 gives \(L'(1)>1\), and (8.48) with \(k=2\) gives
\(|L''(1)|\ll L'(1)\log\log q\), since \(h\le\log q\). The class-number formula gives
\(0<L(1)\le\pi h/\sqrt q\). Finally \(\log Q=\log q+O_*1\). Divide the three residue terms in (8.115) by \(4R(0)L'(1)\log q\). Their sum is
\[
1+O_*\left(\frac{(\log\log q)^{3/2}}{\log q}
                  +\frac{h\log q}{\sqrt q}\right).
\tag{8.117}
\]
Both errors tend to zero effectively. Make their combined absolute value at most \(1/2\), and use (8.114)–(8.116). This proves (8.112). \(\square\)

**Theorem 8.29 (Goldfeld–Gross–Zagier effective growth).** For every \(\epsilon>0\) there is an effectively computable \(c_\epsilon>0\) such that, for every negative fundamental discriminant \(D\),
\[
h(D)\ge c_\epsilon(\log|D|)^{1-\epsilon}.
\tag{8.118}
\]

**Proof.** If \(h>\log q\), the conclusion is immediate after decreasing the constant. If the first alternative of (8.99) holds, it likewise gives \(h\ge c\log q\) beyond a fixed effective threshold. In the remaining case, take \(B=(\log q)^{100}\) and the actual coefficient product of Section 8.11. Equation (8.103) and the exact partition give \(S_1=-S_2-S_3\). Equations (8.94) and (8.112) imply
\[
c_*\log q\,e^{-C_*\sqrt{\log(2h)}}
\le C_*h e^{C_*\sqrt{\log(2h)}}+3.
\]
Since \(h\ge1\), absorb the last constant into the right side and rearrange. Enlarging the fixed constants yields
\[
h\ge c_*\log q\,e^{-C_*\sqrt{\log(2h)}}
\ge c_*\log q\,e^{-C_*\sqrt{\log(2\log q)}}.
\tag{8.119}
\]
For \(0<\epsilon<1\), put \(v=\sqrt{\log\log q}\). The inequalities
\(\sqrt{\log(2\log q)}\le v+\sqrt{\log2}\) and
\(\epsilon v^2-C_*v\ge-C_*^2/(4\epsilon)\)
give
\[
e^{-C_*\sqrt{\log(2\log q)}}
\ge e^{-C_*\sqrt{\log2}-C_*^2/(4\epsilon)}
             (\log q)^{-\epsilon}.
\]
This proves (8.118) above the effective threshold. Below it, \(h\ge1\) allows decreasing \(c_\epsilon\) by a computable factor; no ineffective finiteness theorem is needed. The cases \(\epsilon\ge1\) follow, for example, from the case \(\epsilon=1/2\), since \(q\ge3\). \(\square\)

This is the effective logarithmic growth stated in (8.1). It does not turn Siegel's power bound into an effective power bound. The elliptic input is the fixed rank-two certificate and the known analytic-rank-0-or-1 theorem; no higher-rank Birch–Swinnerton-Dyer conjecture has entered. The separate exact internal proofs of symmetric-square automorphy, general Rankin–Selberg theory, modularity and the low-rank theorem remain the indicated planned prerequisites, rather than claims that the whole surrounding programme is already proved.

## 9. Exercises

1. **Easy.** Deduce \(h(D)\gg_\varepsilon |D|^{1/2-\varepsilon}\) for negative fundamental discriminants, keeping the factors at \(-3,-4\) correct.
2. **Medium.** Prove nonnegativity of the coefficients in (1.1), including primes dividing one or both conductors. Explain the effect of replacing the product character by its primitive inducing character.
3. **Medium.** Identify exactly where \(c(\varepsilon)\) becomes ineffective. Why does computability of \(L(1,\chi)\) for each specified character not resolve that step?
4. **Hard.** Prove (3.1) by expanding at 2. Justify which series can be evaluated across \(s=1\), estimate its tail, and specify the truncation length.
5. **Hard.** Prove that only finitely many imaginary quadratic fields have \(h(D)<|D|^{1/2-\varepsilon}\). Why is using (6.2) with the same exponent insufficient?
6. **Medium.** Use the rational enclosures in Section 8.1 to bound the pairing \(b\), prove that its two-point height matrix is positive definite, and deduce independence.
7. **Hard.** Prove the split-prime bound (8.18) for even as well as odd fundamental discriminants. Deduce the fourth product zero under the exact hypotheses of Corollary 8.6, keeping the character factor at \(-1\) visible.
8. **Medium.** Deduce the all-ideal count (8.44) and reciprocal tail (8.45) from the primitive-ideal count. Explain the different rational-integer divisors at split, inert and ramified primes.
9. **Hard.** If \(h(D)\le(\log|D|)^A\) for fixed \(A>0\), derive (8.48) with an effective initial threshold. Explain why the error term in (8.41) is harmless even for \(k=1\).
10. **Medium.** Compute the residue polynomial in (8.50) from the first two logarithmic Gamma derivatives at 1, and explain the explicit remainder constant 8.
11. **Hard.** Reconstruct the independence proof of Proposition 8.14 from its two character rows. Explain why parity of the relation coefficients is sufficient even without knowing a Mordell–Weil basis.
12. **Medium.** Identify the nonempty ramified-prime relation in the fields of discriminants \(-20\) and \(-24\). Deduce (8.68) under \(h(D)\le\log|D|\), without using a prime number theorem.
13. **Hard.** Prove (8.70) directly from the fourth-moment Burgess estimate and periodic Pólya–Vinogradov bound. Explain why its linear dependence on \(1+|t|\) suffices for a contour with two Gamma factors.
14. **Medium.** Derive all three cases of (8.79), including inert and ramified primes, and prove positivity when \( |\lambda(p)|\le2\).
15. **Medium.** Prove the transport-table inequality \(d_k(p^e)d_l(p^e)\le d_{kl}(p^e)\) and deduce \(\tau(m^2)^3\le d_{27}(m)\).
16. **Hard.** Derive the moment \(\int_0^\infty\sqrt y(-V'(y))dy=2\pi\), then use it to explain why the square-root term of (8.32) contributes order \(h\), rather than an extra power of \(\log q\), in (8.93).
17. **Medium.** For \(D=-5143=-37\cdot139\), find the primitive character of \(\chi_{-139}\chi_D\), the conductor and root of \(E_*\otimes\chi_D\), and its smoothing scale. Explain why its 139 Euler factor must be restored.
18. **Hard.** Derive (8.115), including every chain-rule factor, and show directly how (8.119) gives an effective constant for each \(0<\epsilon<1\).

## 10. Solutions

**1.** Formula (6.1) and Theorem 5.1 give

\[
h(D)>\frac{w_Dc(\varepsilon)}{2\pi}|D|^{1/2-\varepsilon}.
\]

Since \(w_D\ge2\), the common constant \(c(\varepsilon)/\pi\) works. At \(-3\), \(L(1,\chi_{-3})=\pi/(3\sqrt3)\) and \(w=6\); at \(-4\), \(L(1,\chi_{-4})=\pi/4\) and \(w=4\). Both give \(h=1\). Substituting 2 for their root counts would give an incorrect class number.

**2.** With \(u=\chi_1(p)\), \(v=\chi_2(p)\), two values 1 give \((1-z)^{-4}\); other unit pairs give \((1-z^2)^{-2}\). One zero and one value 1 give \((1-z)^{-2}\); one zero and one value \(-1\) give \((1-z^2)^{-1}\). Two zeros give \((1-z)^{-1}\). Each local series is nonnegative, so their product is too. The nonunit cases are part of the proof.

For example, \(\chi_{-3}\chi_{-15}\) equals \(\chi_5\) away from multiples of 3 and vanishes on those multiples. Since \(\chi_5(3)=-1\),

\[
L(s,\chi_{-3}\chi_{-15})=(1+3^{-s})L(s,\chi_5).
\]

At \(p=3\), the local factor in (1.1) is \((1-z)^{-1}\). Replacing the third character by its primitive inducing character gives \((1-z^2)^{-1}\) instead. The primitive replacement belongs in the biquadratic Dedekind zeta factorization, but changes this auxiliary function.

**3.** Theorem 4.1 gives the computable constant (4.7), uniform over every character except at most one. Formula (5.2) takes a minimum with \(q_1^\varepsilon L(1,\chi_1)\), which is positive but whose conductor is not bounded by this argument. The finite formula computes a specified character's value. It cannot supply a finite stopping test for a conductor search when the character does not exist. This is the precise step making the final constant ineffective.

**4.** Differentiate the nonnegative Dirichlet series absolutely at 2 to get \(b_j\ge0\), \(b_0\ge1\). The pole-subtracted function has coefficients \(b_j-\lambda_F\); its bound \(11000Q\) on the radius-\(3/2\) circle gives (3.4). At \(z=2-\beta<9/8\), choose \(N=\lceil\log(88000Q)/\log(4/3)\rceil\). The tail is at most \(44000Q(3/4)^N\le1/2\). Thus

\[
F(\beta)\ge\frac12-\lambda_F\left(
\frac1\delta+\sum_{j=0}^{N-1}(1+\delta)^j\right)
=\frac12-\frac{\lambda_F}{\delta}(1+\delta)^N.
\]

As \(N\le41+4\log Q\), the last power is at most \(200Q^{4\delta}\). Only the pole-subtracted Taylor series, whose disk crosses 1, was evaluated at \(\beta<1\).

**5.** Use (6.2) with exponent \(\varepsilon/2\) to get \(h(D)>c'|D|^{1/2-\varepsilon/2}\). Combining with the proposed strict upper bound forces \(c'|D|^{\varepsilon/2}<1\); hence \(|D|<(c')^{-2/\varepsilon}\). There are only finitely many integer discriminants in that range. Using the same exponent in both inequalities would only compare \(c'\) with 1 and give no bound on \(|D|\).


**6.** The table gives
\[
\frac{1500-670-769}{2000}<b<\frac{1504-667-766}{2000},
\]
so \(61/2000<b<71/2000<1/25\). The first diagonal height is positive, and the determinant is greater than
\(667\cdot766/10^6-1/625>1/2\). Thus the quadratic form is positive definite. Formula (8.9) makes a nonzero relation \(nP+mQ=O\) impossible, since its positive height value would equal \(H(O)=0\).

**7.** If \(p\) splits, choose one of its two primes and let its class have order \(k\le h(D)\). A generator \(\alpha\) of its \(k\)-th power is integral, has norm \(p^k\), and is not rational, since its valuations at the two primes differ. Write \(\alpha=(u+v\sqrt D)/2\), with \(u,v\in\mathbf Z\), \(v\ne0\). For \(D=4d\), this means \(u=2a,v=b\) when \(\alpha=a+b\sqrt d\); thus the same norm formula applies. It gives \(p^{h(D)}\ge p^k=(u^2+|D|v^2)/4\ge|D|/4\).

Under (8.19), the prime 5077 therefore cannot split; it is unramified and hence inert. Consequently \(\chi_D(5077)=-1\) and \(\chi_D(-1)=-1\), making \(\chi_D(-5077)=1\). The coprime twist formula gives the negative sign \(w(E\otimes\chi_D)=-1\), and hence at least one central zero for the twist. The untwisted factor has at least three by Proposition 8.4, so their product has at least four. If 5077 divides \(D\), this coprime twist formula is unavailable; the proof has not established that case.


**8.** For an ideal's prime valuations, extract the same minimum from a pair of split primes, the entire inert-prime valuation, and the integer part of half a ramified-prime valuation. They give the unique integer \(r\) with \(J=(r)J_0\) and \(J_0\) primitive. Norms multiply by \(r^2\), so
\[
N_D(t)=\sum_{r\le\sqrt t}R_D(t/r^2)
\le h\sqrt t+\frac{4ht}{\sqrt d}\sum_{r\ge1}r^{-2}
\le h\sqrt t+\frac{16ht}{\sqrt q}.
\]
In Stieltjes partial summation for \(1/t\), drop the nonpositive lower endpoint. The square-root term contributes at most \(2h/\sqrt y\), and the linear term contributes \((16h/\sqrt q)(1+\log(X/y))\). This gives (8.45), including real cutoffs and their strict lower endpoint.

**9.** Put \(t=\log q\). The condition \(h\le t^A\) gives \(h\log q/\sqrt q\le t^{A+1}e^{-t/2}\), which is at most \(1/1000\) beyond an effective threshold. This can be found by increasing integer \(t>2(A+1)\), where the displayed expression is decreasing and tends to zero. Thus (8.35) and \(L'>1\) hold. Also \(\log(2h)\le\log2+A\log t\), while
\[
\frac h{\sqrt q}(\log q)^{k+1}
\le t^{A+k+1}e^{-t/2}\longrightarrow0.
\]
Its threshold is effective by the same decreasing-function test, now after \(t>2(A+k+1)\). It is eventually at most 1 and hence at most \(L'\); since \(\log\log q\ge1\) eventually, it is absorbed in the first term of (8.41). This proves (8.48). For \(k=1\), the first factor's logarithmic power is zero; absorption uses \(L'>1\) directly, without requiring a growing logarithm.


**10.** The Gamma identities give \(\Gamma'(1)=-\gamma\), \(\Gamma''(1)=\gamma^2+\zeta(2)\). Therefore the coefficient of \(z^2\) in \(\Gamma(1+z)^2\) is \(2\gamma^2+\zeta(2)\). With \(L=\log(1/y)\), multiplication by \(2e^{Lz}/z^3\) gives residue \(L^2-4\gamma L+4\gamma^2+2\zeta(2)\). On the line \(\operatorname{Re}z=-1/2\), use \(|\Gamma(1/2+it)|^2\le\pi\). The remaining integral is at most \(\sqrt y\int_{\mathbf R}(1/4+t^2)^{-3/2}dt=8\sqrt y\).

**11.** The two character rows make any relation \(nP_*+mQ_*=O\) have even \(n,m\). Their halved combination is killed by 2. A rational point killed by 2 must have ordinate zero, giving a rational root of the monic cubic; the reduction modulo 7 excludes such a root. Thus the halved combination is already zero. Infinite repetition forces both original integer coefficients to vanish. This argument proves independence directly; it neither requires a finite-generation theorem nor assumes the two points generate the full group.

**12.** For discriminant \(-20\), the squarefree negative radicand is \(-5\); the ramified prime above 5 is generated by \(\sqrt{-5}\), while 2 is not in this relation. For discriminant \(-24\), the radicand is \(-6\), so the product of the primes above 2 and 3 is generated by \(\sqrt{-6}\). In general the subset-kernel calculation gives \(\omega(D)\le1+\log h/\log2\). If \(h\le\log q\), there are at most \(1+\log\log q/\log2\) ramified primes. Ordering them and using only \(p_j\ge j+1\) gives the two sums before (8.69). The resulting logarithmic loss is \(O_{a,b}(\sqrt{\log\log q}+\log\log\log q)\), which is at most \(\varepsilon\log\log q\) beyond an effective threshold. Exponentiation and an effective adjustment over the initial range give (8.68).


**13.** In \(L(s)=s\int_1^\infty A(u)u^{-s-1}du\), split at \(q\). At real part \(1/2\), Burgess bounds the first integral by \(C_\delta q^{3/16+\delta}\log q\), and periodic Pólya–Vinogradov bounds the second by \(2C\log(2q)\). Multiply by \(|s|\le1+|t|\). On each fixed vertical line, the two Gamma factors supply exponential decay \(e^{-\pi|t|}\) times a fixed polynomial. Multiplying by the linear factor in (8.70) preserves absolute integrability, so no sharper height dependence is required there.

**14.** For \(\chi=0\), the twisted denominators in (8.78) are 1, and the numerator is \(1+\lambda(p)x+x^2\). For \(\chi=1\), retain both denominators and the scalar \((1-x^2)/(1+x^2)\). For \(\chi=-1\), the two numerator factors cancel the twisted denominators and the scalar is 1. These give (8.79). Both quadratics \(1\pm\lambda(p)x+x^2\) are at least \((1-x)^2>0\), since \(x=p^{-1/2}<1\), while \(1-x^2>0\); thus every case is positive.


**15.** Given a row composition and a column composition of \(e\), the greedy transport table has nonnegative integer entries and those margins: each step exhausts a remaining row or column, and equality exhausts both. The table uniquely recovers its margins, so distinct pairs give distinct tables. There are \(\binom{e+kl-1}{kl-1}\) possible \(kl\)-entry tables of total \(e\). This proves the inequality. Since \(2e+1\le\binom{e+2}{2}\), cubing and applying the inequality with \((k,l)=(3,3)\) and \((9,3)\) gives \((2e+1)^3\le d_{27}(p^e)\). Multiply over the prime powers of \(m\).

**16.** Integration by parts gives \(\int y^s(-V')dy=s\int y^{s-1}Vdy=2\Gamma(1+s)^2/s^2\); the endpoint terms vanish by (8.51). At \(s=1/2\), \(\Gamma(3/2)=\sqrt\pi/2\), so the value is \(2\pi\). Thus smoothing a counting bound \(C h\sqrt A/\sqrt q\) gives exactly at most \(2\pi C h\sqrt T/\sqrt q\). With \(T=Q/(cd^2m^2)\), the remaining absolute weights become \(|a_D(c)|/c\), \(d^{-2}\), and \(d_9(m)m^{-2}\). Their sums are \(\nu_C(1)\), \(\zeta(2)\), and \(\zeta(2)^9\). Since \(\sqrt{Q/q}\) is fixed, the result is \(O_f(h\nu_C(1))\), with no harmonic-sum logarithm.


**17.** Both discriminants are fundamental and their product has squarefree positive kernel 37. Thus the primitive product is \(\chi_{37}\), with conductor 37 and even parity. Lemma 8.25 gives the curve conductor \(37^2\) and root \(-1\). With \(N(E_*)=37\cdot139^2\), the scale is \(Q=139\cdot37^{3/2}/(4\pi^2)\), namely \(q\sqrt{37}/(4\pi^2)\). At 139 the two ramified quadratic characters cancel on units; the actual twist is good there. Its local factor is the quadratic good factor of \(E_0\), with its roots multiplied by the unramified value \(\chi_{37}(139)\). The coefficient twist by \(\chi_D\) alone would instead set every positive 139-power coefficient to zero. Formula (8.105) includes the actual regained factor.

**18.** Expand \(L(1+2z)=L(1)+2L'(1)z+2L''(1)z^2+O(z^3)\) and \(R(z)=R(0)+R'(0)z+R''(0)z^2/2+O(z^3)\). The coefficient of \(z^2\) in \(2LR\) is \(4L''R(0)+4L'R'(0)+LR''(0)\); this is the residue after dividing by \(z^3\). For the constant, use \(\sqrt{\log(2\log q)}\le\sqrt{\log\log q}+\sqrt{\log2}\), then complete the square in \(\epsilon v^2-C_*v\). The large-range constant is at least the fixed effective \(c_*\) times \(\exp(-C_*\sqrt{\log2}-C_*^2/(4\epsilon))\). If \(q_0\) is the effective threshold, decrease it further to at most \((\log q_0)^{\epsilon-1}\), so \(h\ge1\) covers the remaining range. Every input to this computation is effective by Lemma 8.27 and the preceding estimates.

## References

C. L. Siegel, *Über die Klassenzahl quadratischer Zahlkörper*, *Acta Arithmetica* 1 (1935), 83–86, is the original theorem. T. Estermann's positive-coefficient Taylor method and S. Chowla's alternative proof are the classical routes. D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorems 12.9–12.10, presents D. Goldfeld's minimal-conductor smoothing argument; Goldfeld's [*A Simple Proof of Siegel's Theorem*](https://doi.org/10.1073/pnas.71.4.1055) appeared in *PNAS* 71 (1974), 1055. Here the fully proved Taylor inequality is combined with the minimal-conductor choice to obtain an effective one-exception estimate before absorbing the exception.

T. Tatuzawa, [*On a Theorem of Siegel*](https://doi.org/10.4099/jjm1924.21.0_163), *Japanese Journal of Mathematics* 21 (1951), 163–178, Theorems 1–2, gives explicit one-exception bounds. H. M. Stark, *The Gauss Class-Number Problems*, in *Analytic Number Theory: A Tribute to Gauss and Dirichlet* (2007), Sections 2–4, supplies historical and arithmetic comparisons. Sections 1–5 give the complete analytic proofs here. Planned internal providers for (6.1), reduced-form classes, and the global class-number-one classification are identified at their points of use. Section 8 proves the fixed-curve rank certificate and deduces its triple central zero from precise internal prerequisites. Sections 8.4–8.12 prove the full effective class-number reduction, including the error sums, ramified twists and positive residue. The exact deep internal prerequisites retain their stated planned proof status.

J.-F. Mestre, [*La méthode des graphes. Exemples et applications*](https://wstein.org/rank4/mestre-en.pdf), Section 3, discusses the conductor-5077 curve; the linked English translation is by A. Jorza. B. H. Gross and D. B. Zagier, *Heegner points and derivatives of L-series*, *Inventiones Mathematicae* 84 (1986), 225–320, supplies the historical height formula. The low-analytic-rank consequence of their work and Kolyvagin's Euler systems is the exact internal theorem assigned to *Global Langlands conjectures and functoriality*, lesson 13. The arithmetic height certificate in Section 8.1 is derived here, using the written complex-uniformization prerequisite for the group law.

Sections 8.4–8.5 give the complete estimates used here, with an elementary reduced-form vector count, explicit periodic-sum errors and the programme’s proved effective Möbius bound. The first-derivative proof does not require the Kronecker limit formula.

The smoothing in Section 8.6 is a second-derivative Mellin construction. The conductor-37 curve and its twist by \(-139\) in Section 8.7 are the classical Gross–Zagier example. The exact two-character independence certificate is computed and proved here. Section 8.8 supplies its ideal-class and Euler-product arguments in full.

S. Gelbart and H. Jacquet, [*A relation between automorphic representations of GL(2) and GL(3)*](https://www.numdam.org/item/ASENS_1978_4_11_4_471_0/), *Annales scientifiques de l’École Normale Supérieure*, fourth series, 11 (1978), 471–542, is the original symmetric-square theorem. Its exact programme provider and the standard/Rankin–Selberg analytic providers are specified in Section 8.12. Here the full error and contour calculations use the already proved fourth-moment Burgess estimate; the final all-discriminant reduction preserves the primitive Euler factors at shared ramification.
