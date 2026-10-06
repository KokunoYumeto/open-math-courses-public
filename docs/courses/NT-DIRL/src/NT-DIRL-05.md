# The functional equation of Dirichlet L-functions

*Written by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra. Public domain (CC0).*

The functional equation connects a Dirichlet series in its original half-plane to values on the other side of the critical strip. Its constant remembers the phase of the Gauss sum. A theta integral makes both the continuation and that constant explicit; the same integral controls the order of the completed function, and hence its product over zeros.

Throughout this lesson, \(\chi\) is primitive of conductor \(q>1\),
\(\chi(-1)=(-1)^a\), with \(a\in\{0,1\}\), and

\[
\xi(s,\chi)=\left(\frac q\pi\right)^{(s+a)/2}
\Gamma\left(\frac{s+a}2\right)L(s,\chi),\qquad
\varepsilon(\chi)=\frac{\tau(\chi)}{i^a\sqrt q}.
\tag{1.1}
\]

The square root of \(q\) is positive real. We use the character Poisson identity from *Character sums: the Pólya–Vinogradov inequality*, with \(\widehat f(\eta)=\int f(u)e(-u\eta)\,du\). The Gamma identities used below are proved in *The Gamma function and Stirling's formula*, in the course *The Riemann zeta function*: continuation and residues in Theorem 1.1, nonvanishing in Theorem 1.2, reflection and duplication in Theorems 2.2–2.3, sector Stirling in Theorem 3.1 and its vertical consequence in Corollary 4.1. The general Hadamard theorem used in Section 4 belongs to that course's planned lesson *Entire functions of order one and the Hadamard product of ξ*; its exact hypothesis and conclusion are stated there and below.

## 1. A theta series with the right parity

For \(x>0\), define

\[
\theta(x,\chi)=\sum_{n\in\mathbb Z}
\chi(n)n^a\exp(-\pi n^2x/q).
\tag{1.2}
\]

The term at \(n=0\) is zero, also when \(a=0\). Since
\(\chi(-n)(-n)^a=\chi(n)n^a\), the series is twice its positive-index part. It and all its derivatives with respect to \(x\) converge locally uniformly on \(x>0\).

**Theorem 1.1 (theta transformation).** For every \(x>0\),

\[
\theta(x,\chi)=\varepsilon(\chi)x^{-a-1/2}
\theta(1/x,\overline\chi).
\tag{1.3}
\]

Equivalently,
\(\theta(1/x,\chi)=\varepsilon(\chi)x^{a+1/2}\theta(x,\overline\chi)\).

**Proof.** The Gaussian Fourier transform proved in *Gauss sums* gives
\(\widehat{\exp(-\pi u^2)}(\eta)=\exp(-\pi\eta^2)\).
Differentiation under the integral is justified by the Gaussian majorant and gives

\[
\widehat{u\exp(-\pi u^2)}(\eta)
=-i\eta\exp(-\pi\eta^2).
\]

Thus \(f(u)=u^a\exp(-\pi u^2)\) satisfies \(\widehat f=(-i)^a f\). Put \(N=\sqrt{q/x}\). Character Poisson summation says

\[
\begin{aligned}
\theta(x,\chi)
&=N^a\sum_n\chi(n)f(n/N)\\
&=\frac{\tau(\chi)N^{a+1}}q
\sum_m\overline{\chi(m)}(-i)^a(mN/q)^a
\exp(-\pi m^2N^2/q^2)\\
&=\frac{\tau(\chi)(-i)^a}{\sqrt q}
x^{-a-1/2}\theta(1/x,\overline\chi).
\end{aligned}
\]

Since \((-i)^a=i^{-a}\), the prefactor is \(\varepsilon(\chi)\). \(\square\)

The Gauss identities also give

\[
|\varepsilon(\chi)|=1,\qquad
\varepsilon(\chi)\varepsilon(\overline\chi)=1,
\tag{1.4}
\]

because \(\tau(\chi)\tau(\overline\chi)=(-1)^a q\) and \(i^{2a}=(-1)^a\). In particular \(\varepsilon(\overline\chi)=\overline{\varepsilon(\chi)}\).

## 2. Mellin transformation and continuation

For \(\Re s>1\), absolute convergence permits termwise integration:

\[
\begin{aligned}
\frac12\int_0^\infty\theta(x,\chi)x^{(s+a)/2-1}\,dx
&=\sum_{n\ge1}\chi(n)n^a
\Gamma\left(\frac{s+a}2\right)
\left(\frac q{\pi n^2}\right)^{(s+a)/2}\\
&=\xi(s,\chi).
\end{aligned}
\tag{2.1}
\]

For \(x\ge1\), the series in (1.2) is \(O_q(e^{-c_qx})\), for some \(c_q>0\). For example,
\(n^2x\ge(n^2+x)/2\) when \(n\ge1\), \(x\ge1\), so summing
\(n^a e^{-\pi n^2/(2q)}e^{-\pi x/(2q)}\) proves such an estimate. Formula (1.3) gives the corresponding exponential decay in \(1/x\) as \(x\downarrow0\), with only a fixed power of \(x\) in front. Consequently the integral in (2.1) converges locally uniformly for every complex \(s\); its derivatives introduce only powers of \(\log x\), which remain integrable with these exponential bounds.

Splitting at 1, applying (1.3) on \((0,1)\), and substituting \(u=1/x\), we obtain the particularly useful entire representation

\[
\begin{aligned}
\xi(s,\chi)
={}&\frac12\int_1^\infty\theta(x,\chi)x^{(s+a)/2-1}\,dx\\
&+\frac{\varepsilon(\chi)}2
\int_1^\infty\theta(x,\overline\chi)x^{(1-s+a)/2-1}\,dx.
\end{aligned}
\tag{2.2}
\]

**Theorem 2.1 (functional equation).** Both \(\xi(s,\chi)\) and \(L(s,\chi)\) are entire, and

\[
\boxed{\xi(s,\chi)=\varepsilon(\chi)\xi(1-s,\overline\chi).}
\tag{2.3}
\]

For real primitive characters, \(\varepsilon(\chi)=1\).

**Proof.** Representation (2.2) proves that \(\xi\) is entire. Apply it to \(1-s,\overline\chi\), multiply by \(\varepsilon(\chi)\), and use (1.4). The two integrals exchange positions, proving (2.3). Since \(1/\Gamma\) is entire,

\[
L(s,\chi)=\left(\frac q\pi\right)^{-(s+a)/2}
\frac{\xi(s,\chi)}{\Gamma((s+a)/2)}
\tag{2.4}
\]

is entire and agrees with the original series where \(\Re s>1\). Finally, Theorem 5.1 of *Gauss sums* proves the phase identity \(\tau(\chi)=i^a\sqrt q\) for every real primitive character. It makes the root number exactly 1, not merely a sign of modulus 1. \(\square\)

An equivalent inverse form of (2.3) has coefficient \(i^a\sqrt q/\tau(\chi)\). This is another common convention. The theta coefficient \(i^a\sqrt q/\tau(\overline\chi)\) is also equivalent to (1.3), since \(\tau(\overline\chi)=(-1)^a q/\tau(\chi)\). The conjugation in the denominator must be retained when converting that version.

The version directly involving the uncompleted functions is

\[
L(s,\chi)=\varepsilon(\chi)
\left(\frac q\pi\right)^{1/2-s}
\frac{\Gamma((1-s+a)/2)}{\Gamma((s+a)/2)}
L(1-s,\overline\chi).
\tag{2.5}
\]

Apparent singularities of the right side cancel as prescribed by the entire left side.

## 3. Where the zeros can be

The Euler product proved earlier excludes zeros when \(\Re s>1\). To exclude zeros on the boundary too, a positivity argument is needed. Merely knowing \(L(1,\chi)\ne0\) does not settle the other points \(1+it\).

**Lemma 3.1 (nonvanishing on the line 1).** Every Dirichlet character \(\chi\) has \(L(1+it,\chi)\ne0\) for \(t\ne0\). For a nonprincipal character it is also nonzero at \(t=0\).

**Proof.** The assertion at \(t=0\) was proved in *Dirichlet's theorem on primes in arithmetic progressions*. Fix \(t\ne0\). The functions \(L(s,\chi)\) and \(L(s,\chi^2)\) are holomorphic near \(1+it\) and \(1+2it\), respectively. For nonprincipal characters this follows from periodic continuation to \(\Re s>0\); for principal ones it follows from
\(L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s})\), with the only pole in that half-plane at \(s=1\).

For real \(\sigma>1\), expand the logarithms of the absolutely convergent Euler products. For \(p\nmid q\) and \(k\ge1\), put \(z=\chi(p)^k p^{-ikt}\), so \(|z|=1\). The contribution of this prime power to the logarithm of

\[
\zeta(\sigma)^3
|L(\sigma+it,\chi)|^4
|L(\sigma+2it,\chi^2)|
\tag{3.1}
\]

is \((3+4\Re z+\Re z^2)/(kp^{k\sigma})\). If \(z=e^{iu}\), its numerator is \(2(1+\cos u)^2\ge0\). For \(p\mid q\), only the positive contribution from \(\zeta^3\) remains. Thus (3.1) is at least 1.

If \(L(1+it,\chi)=0\), holomorphy gives
\(|L(\sigma+it,\chi)|=O_t(\sigma-1)\). The final factor of (3.1) stays bounded, and \(\zeta(\sigma)=O((\sigma-1)^{-1})\). The whole product tends to zero as \(\sigma\downarrow1\), contradicting its lower bound 1. \(\square\)

**Theorem 3.2 (trivial zeros and symmetry).** For a primitive character of conductor \(q>1\), the zeros of \(L(s,\chi)\) in \(\Re s\le0\) are exactly

\[
s=-a-2k,\qquad k=0,1,2,\ldots,
\tag{3.2}
\]

and they are simple. All other zeros, counted with multiplicity, lie in \(0<\Re s<1\). If \(\rho\) is one of these nontrivial zeros, so is \(1-\overline\rho\), with the same multiplicity.

**Proof.** Gamma has no zeros, so \(\xi\) is nonzero on \(\Re s\ge1\) by the Euler product and Lemma 3.1. The functional equation makes it nonzero on \(\Re s\le0\) as well. In (2.4), the only zeros in that half-plane are therefore the simple zeros of \(1/\Gamma((s+a)/2)\), exactly (3.2). This includes \(s=0\) precisely for even characters. Elsewhere in the plane the Gamma factor is finite and nonzero, so the zeros of \(L\) are those of \(\xi\).

Conjugating the original Dirichlet series, and then continuing, gives
\(\overline{\xi(\overline s,\chi)}=\xi(s,\overline\chi)\).
Combine this with (2.3) to see that
\(\xi(s,\chi)=\varepsilon(\chi)\overline{\xi(1-\overline s,\chi)}\).
It reflects each zero, preserving its order. A complex character need not have symmetry under \(\rho\mapsto\overline\rho\) by itself; conjugation also changes the character. \(\square\)

For an imprimitive character induced by \(\chi^*\), the extra factors

\[
L(s,\chi)=L(s,\chi^*)
\prod_{p\mid q\atop p\nmid q^*}(1-\chi^*(p)p^{-s})
\tag{3.3}
\]

can have additional zeros on \(\Re s=0\). Indeed \(p^s=\chi^*(p)\) has real part of its logarithm zero. Those zeros are separate from the nontrivial zeros of the primitive completed function. Formula (3.2) is a primitive-character statement.

## 4. The entire-function product and its constant

An entire function has order at most 1 if, for every \(\eta>0\), its maximum modulus is eventually bounded by \(\exp(C_\eta R^{1+\eta})\) on \(|s|\le R\). The general theorem assigned to the planned lesson *Entire functions of order one and the Hadamard product of ξ* says that, for such a nonzero function with \(f(0)\ne0\),

\[
f(s)=e^{A+Bs}\prod_{f(\rho)=0}
(1-s/\rho)e^{s/\rho},
\tag{4.1}
\]

with multiplicities; the product converges normally on compact sets, and
\(\sum_\rho|\rho|^{-1-\eta}<\infty\) for every \(\eta>0\). This theorem is an exact planned prerequisite in the zeta course, rather than an unproved factorization specific to this lesson. We now verify its hypotheses and determine the part of \(B\) controlled by the functional equation.

**Proposition 4.1.** For fixed \(q\), \(\xi(s,\chi)\) has order exactly 1, and

\[
\xi(s,\chi)=e^{A(\chi)+B(\chi)s}
\prod_\rho(1-s/\rho)e^{s/\rho},
\quad e^{A(\chi)}=\xi(0,\chi),
\tag{4.2}
\]

where \(\rho\) runs over its nontrivial zeros. Moreover,

\[
B(\chi)=\frac{\xi'(0,\chi)}{\xi(0,\chi)},\qquad
\boxed{\Re B(\chi)=-\sum_\rho\Re\frac1\rho.}
\tag{4.3}
\]

The last sum converges absolutely. It is a statement about the real part only.

**Proof.** The two exponentially decaying integrals in (2.2) bound the maximum modulus on \(|s|\le R\) by
\(C_q\int_1^\infty e^{-c_qx}x^{(R+a)/2}\,dx\).
Enlarging the domain to \((0,\infty)\) expresses this bound by a Gamma value; real Stirling gives

\[
\log\max_{|s|\le R}|\xi(s,\chi)|
\le C_q R\log(R+2).
\tag{4.4}
\]

Hence the order is at most 1. As real \(\sigma\to+\infty\), the original series gives \(L(\sigma,\chi)=1+O(2^{-\sigma})\), while real Stirling in (1.1) gives
\(\log|\xi(\sigma,\chi)|=(\sigma/2)\log\sigma+O_q(\sigma)\).
The order is consequently at least 1. Theorem 3.2 gives \(\xi(0,\chi)\ne0\). Applying (4.1) proves (4.2); logarithmic differentiation at zero gives its formula for \(B\).

Normal convergence permits logarithmic differentiation away from zeros:

\[
\frac{\xi'}{\xi}(s,\chi)
=B(\chi)+\sum_\rho
\left(\frac1{s-\rho}+\frac1\rho\right).
\tag{4.5}
\]

The terms in parentheses are \(O_s(|\rho|^{-2})\). Since \(0<\Re\rho<1\),
\(0<\Re(1/\rho)<|\rho|^{-2}\). This proves absolute convergence of the real sum in (4.3). The reflection \(\rho\mapsto1-\overline\rho\) permutes all zeros, so

\[
\sum_\rho\Re\frac1{1-\rho}
=\sum_\rho\Re\frac1\rho=:H.
\]

At \(s=1\), the real part of (4.5) is therefore \(\Re B+2H\). On the other hand, the logarithmic derivative of the reflected functional equation gives
\(\Re(\xi'/\xi)(1,\chi)=-\Re(\xi'/\xi)(0,\chi)=-\Re B\).
Thus \(\Re B+2H=-\Re B\), proving (4.3). Every reindexing here involved an absolutely convergent real sum. \(\square\)

Taking the logarithmic derivative of (1.1) also gives, away from zeros and poles of the displayed individual terms,

\[
\frac{L'}L(s,\chi)=B(\chi)
-\frac12\log(q/\pi)
-\frac12\frac{\Gamma'}\Gamma((s+a)/2)
+\sum_\rho\left(\frac1{s-\rho}+\frac1\rho\right).
\tag{4.6}
\]

The cancellations at trivial zeros are interpreted meromorphically. This formula will be the starting point for zero-free regions.

## 5. Bernoulli numbers and the values at integers

Define the Bernoulli polynomials by the convergent power series near \(t=0\),

\[
\frac{t e^{ut}}{e^t-1}=\sum_{n\ge0}B_n(u)\frac{t^n}{n!},
\]

so \(B_0(u)=1\) and \(B_1(u)=u-1/2\). The generalized Bernoulli numbers are defined by

\[
\sum_{b=1}^q\chi(b)\frac{t e^{bt}}{e^{qt}-1}
=\sum_{n\ge0}B_{n,\chi}\frac{t^n}{n!}.
\tag{5.1}
\]

Substituting \(qt\) in the polynomial generating series gives the useful finite formula

\[
B_{n,\chi}=q^{n-1}\sum_{b=1}^q\chi(b)B_n(b/q).
\tag{5.2}
\]

In particular \(B_{0,\chi}=0\) and
\(B_{1,\chi}=q^{-1}\sum_b b\chi(b)\).

**Theorem 5.1.** For every integer \(n\ge1\),

\[
\boxed{L(1-n,\chi)=-\frac{B_{n,\chi}}n.}
\tag{5.3}
\]

In particular,

\[
L(0,\chi)=-\frac1q\sum_{b=1}^q b\chi(b),
\tag{5.4}
\]

which is zero for even \(\chi\).

**Proof.** For \(t>0\), periodicity gives the exact exponentially convergent sum

\[
\Phi_\chi(t)=\sum_{m\ge1}\chi(m)e^{-mt}
=\frac{\sum_{b=1}^q\chi(b)e^{-bt}}{1-e^{-qt}}.
\]

It has a removable singularity at zero, since \(\sum_b\chi(b)=0\). Evaluating (5.1) at \(-t\) gives its Taylor series

\[
\Phi_\chi(t)=\sum_{n\ge1}
\frac{(-1)^n B_{n,\chi}}{n!}t^{n-1}.
\tag{5.5}
\]

For \(\Re s>1\), termwise integration yields
\(\Gamma(s)L(s,\chi)=\int_0^\infty\Phi_\chi(t)t^{s-1}\,dt\).
Choose \(r>0\) within the Taylor radius. Split the integral at \(r\). Its upper part is entire in \(s\), by exponential decay. In the lower part subtract the first \(K\) terms of (5.5); its remainder is \(O(t^K)\), so the remainder integral is holomorphic on \(\Re s>-K\). The subtracted terms contribute

\[
\sum_{n=1}^{K}
\frac{(-1)^n B_{n,\chi}}{n!}
\frac{r^{s+n-1}}{s+n-1}.
\tag{5.6}
\]

This continues \(\Gamma(s)L(s,\chi)\) to the plane. At \(s=1-n\) its residue is \((-1)^nB_{n,\chi}/n!\). Gamma has residue \((-1)^{n-1}/(n-1)!\) there. Since \(L\) is entire, division of these residues proves (5.3), also when the numerator residue is zero.

For even \(\chi\), pairing \(b\) and \(q-b\) gives
\(\sum_b b\chi(b)=(q/2)\sum_b\chi(b)=0\), proving the last assertion. \(\square\)

The generating function itself records the parity: replacing \(t\) by \(-t\) and \(b\) by \(q-b\) shows that its left side is multiplied by \(\chi(-1)\). Therefore

\[
B_{n,\chi}=0\quad\text{if }n\not\equiv a\pmod2.
\tag{5.7}
\]

These vanishing values agree exactly with the trivial-zero pattern in (3.2).

### The Hurwitz continuation gives the same values

For \(0<u\le1\), the Hurwitz function initially means
\(\zeta(s,u)=\sum_{k\ge0}(k+u)^{-s}\), \(\Re s>1\). Its Mellin representation is

\[
\Gamma(s)\zeta(s,u)
=\int_0^\infty\frac{e^{-ut}}{1-e^{-t}}t^{s-1}\,dt.
\tag{5.8}
\]

The Laurent series of the kernel at zero is
\(\sum_{n\ge0}B_n(1-u)t^{n-1}/n!\). The same subtraction argument as (5.6), now including \(n=0\), continues the right side meromorphically with possible simple poles at \(1,0,-1,\ldots\). Multiplication by \(1/\Gamma(s)\) cancels all except the pole at 1, whose residue is 1. At \(s=1-n\), \(n\ge1\), division of residues gives

\[
\zeta(1-n,u)=-\frac{B_n(u)}n,
\tag{5.9}
\]

because \(B_n(1-u)=(-1)^nB_n(u)\). That polynomial identity follows immediately by replacing \(t\) by \(-t\) in its generating function. These arguments establish the continuation and the values, rather than presupposing a formula for the Hurwitz function.

Splitting a Dirichlet series into residue classes gives, initially on \(\Re s>1\) and hence everywhere by continuation,

\[
L(s,\chi)=q^{-s}\sum_{b=1}^q\chi(b)\zeta(s,b/q).
\tag{5.10}
\]

The residue at 1 vanishes because \(\sum_b\chi(b)=0\); thus this route also proves that \(L\) is entire. Equations (5.2) and (5.9) reproduce (5.3). The theta route supplies the functional equation directly; the Hurwitz route supplies the integer values directly. Their entire continuations agree on the original half-plane and therefore agree everywhere.

## 6. Convexity with a logarithm

**Theorem 6.1.** Uniformly for primitive characters of conductor \(q>1\) and real \(t\),

\[
L(1/2+it,\chi)
\ll\bigl(q(|t|+1)\bigr)^{1/4}
\log\bigl(q(|t|+2)\bigr).
\tag{6.1}
\]

The implied constant is absolute.

**Proof.** Fix \(0<\delta\le1/2\). Absolute convergence gives

\[
|L(1+\delta+iu,\chi)|\le\zeta(1+\delta)
\le1+\delta^{-1}\ll\delta^{-1}.
\tag{6.2}
\]

The functional equation (2.5) and uniform vertical Stirling give

\[
|L(-\delta+iu,\chi)|
\ll\delta^{-1}\bigl(q(|u|+2)\bigr)^{1/2+\delta}.
\tag{6.3}
\]

The Gamma ratio used here has bound

\[
\left|\frac{\Gamma((1+\delta+a-iu)/2)}
{\Gamma((-\delta+a+iu)/2)}\right|
\ll(|u|+2)^{1/2+\delta}
\tag{6.4}
\]

uniformly for \(a\in\{0,1\}\), \(0\le\delta\le1/2\). For \(|u|\ge1\), this follows from Corollary 4.1 of *The Gamma function and Stirling's formula*: the exponential decays cancel and the powers subtract to \(1/2+\delta\). For \(|u|\le1\), the numerator's argument stays in a compact set away from Gamma poles, and the reciprocal Gamma in the denominator is entire and bounded on its compact argument set. This proves (6.4), including the limit \(\delta=0\).

To interpolate while keeping the height uniform, fix \(t\) and apply the bounded three-lines principle on \(-\delta\le\Re z\le1+\delta\) to

\[
G(z)=L(z+it,\chi)\exp((z-1/2)^2).
\]

The required principle is assigned to *Growth in the critical strip: convexity and the Lindelöf hypothesis*, the planned zeta-course prerequisite: for a bounded holomorphic function on a closed vertical strip with boundary suprema \(A_0,A_1\), its modulus at a point a fraction \(v\) of the way across is at most \(A_0^{1-v}A_1^v\). Here boundedness follows from (2.4), (4.4), and the reciprocal-Gamma bound \(\log\max_{|z|\le R}|1/\Gamma(z)|=O(R\log(R+2))\), proved in Proposition 4.2 of the Gamma lesson. The Gaussian damping dominates that growth as \(|\Im z|\to\infty\).

On the right boundary (6.2) bounds \(G\) by \(C/\delta\). On the left, put \(u=t+\Im z\) in (6.3). Since
\(|t+v|+2\le(|t|+2)(1+|v|)\), and
\(\sup_v(1+|v|)^{1/2+\delta}e^{-v^2}\) is bounded absolutely for our range of \(\delta\), the left boundary bound is
\(C\delta^{-1}(q(|t|+2))^{1/2+\delta}\).
The point \(z=1/2\) is halfway across this strip and its damping factor is 1. Hence

\[
|L(1/2+it,\chi)|
\ll\delta^{-1}(q(|t|+2))^{1/4+\delta/2}.
\tag{6.5}
\]

Put \(H=q(|t|+2)\) and choose \(\delta=\min(1/2,1/\log H)\). Then \(\delta^{-1}\ll\log H\) and \(H^{\delta/2}\le e^{1/2}\). Finally \(|t|+2\le2(|t|+1)\). This proves (6.1). \(\square\)

The parameter \(\delta\) is chosen after establishing an estimate with an absolute constant uniform on \(0<\delta\le1/2\). A bound with an uncontrolled \(\delta\)-dependent interpolation constant would not justify this last optimization.

## 7. Two root-number examples

For \(\chi_{-4}\), the conductor is 4, the parity is odd, and \(\tau(\chi_{-4})=2i\). Thus

\[
\xi(s,\chi_{-4})=(4/\pi)^{(s+1)/2}
\Gamma((s+1)/2)L(s,\chi_{-4}),\qquad
\varepsilon(\chi_{-4})=1.
\]

The finite value formula gives
\(L(0,\chi_{-4})=-(1-3)/4=1/2\).
Also \(L(-1,\chi_{-4})=0\), a simple trivial zero. The entire completed function has no zero there, because its Gamma pole cancels that zero.

For the quartic character modulo 5 with \(\chi(2)=i\), the values at \(1,2,3,4\) are \(1,i,-i,-1\), so \(a=1\). Directly pairing exponentials gives

\[
\tau(\chi)=-2\sin(\pi/5)+2i\sin(2\pi/5),
\quad
\varepsilon(\chi)=\frac{2\sin(2\pi/5)+2i\sin(\pi/5)}{\sqrt5}.
\tag{7.1}
\]

Numerically the root number is
\(0.8506508084+0.5257311121i\). Its modulus is 1, since
\(4(\sin^2(\pi/5)+\sin^2(2\pi/5))=5\).
For this character \(L(0,\chi)=(3+i)/5\), also directly from (5.4). Its functional equation connects \(\chi\) with \(\overline\chi\); the real-character root number 1 cannot be transferred to this example.

## 8. Exercises

1. **Easy.** Show that \(\varepsilon(\chi)=1\) for every real primitive character, including both parity cases.
2. **Medium.** Derive the asymmetric functional equation

   \[
   L(1-s,\chi)=\frac{\tau(\chi)}q
   \left(\frac q{2\pi}\right)^s\Gamma(s)
   \bigl(e^{-\pi is/2}+\chi(-1)e^{\pi is/2}\bigr)
   L(s,\overline\chi).
   \tag{8.1}
   \]

3. **Medium.** Prove (5.4), and prove its vanishing for even nonprincipal characters.
4. **Medium.** Continue \(L\) by (5.10), prove cancellation of its possible pole, and compare this continuation with the theta integral.
5. **Hard.** Prove
\(L(1/2+it,\chi)\ll_\eta(q(|t|+1))^{1/4+\eta}\)
for each \(\eta>0\), with a constant independent of the primitive character.

## 9. Solutions

**1.** The exact real Gauss phase proved in *Gauss sums* is \(\sqrt q\) when \(a=0\), and \(i\sqrt q\) when \(a=1\). In both cases division by \(i^a\sqrt q\) gives 1. The weaker fact \(|\tau|=\sqrt q\) would prove only a modulus statement and would not answer the exercise.

**2.** Apply (2.3) at \(1-s\) and divide by its completion factors. This gives

\[
L(1-s,\chi)=\frac{\tau(\chi)}{i^a\sqrt q}
\left(\frac q\pi\right)^{s-1/2}
\frac{\Gamma((s+a)/2)}{\Gamma((1-s+a)/2)}
L(s,\overline\chi).
\]

For \(a=0\), reflection at \((1+s)/2\) and duplication at \(s/2\) yield

\[
\frac{\Gamma(s/2)}{\Gamma((1-s)/2)}
=\frac{2^{1-s}}{\sqrt\pi}\Gamma(s)\cos(\pi s/2).
\]

For \(a=1\), reflection at \(s/2\) and the same duplication yield

\[
\frac{\Gamma((s+1)/2)}{\Gamma(1-s/2)}
=\frac{2^{1-s}}{\sqrt\pi}\Gamma(s)\sin(\pi s/2).
\]

Inserting these ratios gives the common prefactor
\((\tau(\chi)/q)(q/(2\pi))^s\Gamma(s)\), times \(2\cos(\pi s/2)\) in the even case and \(-2i\sin(\pi s/2)\) in the odd case. Those two factors are exactly the parentheses in (8.1). The calculation first holds away from the individual Gamma poles; continuation gives the identity of meromorphic expressions everywhere, with removable singularities determined by the entire left side.

**3.** The coefficient of \(t\) in (5.1) is
\(B_{1,\chi}=\sum_b\chi(b)(b/q-1/2)=q^{-1}\sum_b b\chi(b)\).
The equality \(L(0,\chi)=-B_{1,\chi}\) follows by the explicit Mellin-subtraction proof of Theorem 5.1: the residue of \(\Gamma(s)L(s,\chi)\) at zero is \(-B_{1,\chi}\), and the residue of \(\Gamma(s)\) there is 1. For even \(\chi\), substituting \(b\mapsto q-b\) gives
\(\sum_b b\chi(b)=\sum_b(q-b)\chi(b)\). Thus twice that sum equals \(q\sum_b\chi(b)=0\), proving the vanishing.

**4.** The residue-class splitting on \(\Re s>1\) is absolutely convergent and proves (5.10). To continue each Hurwitz term, use its integral (5.8), choose a radius within the Taylor disk of its kernel, and subtract any desired number of Laurent terms in the integral from zero to that radius. The remainder becomes holomorphic on a correspondingly larger left half-plane. Dividing by Gamma cancels the simple possible poles at \(0,-1,\ldots\), leaving just a simple pole at 1 of residue 1. In (5.10) the sum of these residues is \(q^{-1}\sum_b\chi(b)=0\). The resulting entire function agrees with the original series, and so with the theta continuation by the identity theorem. The subtraction also proves (5.9), rather than using the Hurwitz values without their continuation.

**5.** Establish the uniform boundary bounds (6.2) and (6.3) for \(0<\delta\le1/2\), with the compact-argument treatment of the Gamma ratio in (6.4). Damping about the desired height gives (6.5) by bounded three-lines, with an absolute constant. Fix \(\delta=\min(1/2,\eta)\); then \(\delta/2\le\eta\), and its reciprocal can be absorbed into the \(\eta\)-dependent constant. Replacing \(|t|+2\) by at most \(2(|t|+1)\) proves the requested estimate. Alternatively (6.1) implies it because \(\log(2X)\ll_\eta X^\eta\) for \(X\ge1\), as follows by maximizing \((\log(2X))/X^\eta\).

## What this lesson takes from the zeta course

The Gamma continuation, residues, nonvanishing, reflection, duplication, Stirling estimates and reciprocal-Gamma growth come from the written lesson *The Gamma function and Stirling's formula*, at the locators specified above. The general factorization (4.1) for an entire function of order at most 1 with nonzero value at zero comes from the planned lesson *Entire functions of order one and the Hadamard product of ξ*. The bounded three-lines principle used in Section 6 comes from the planned lesson *Growth in the critical strip: convexity and the Lindelöf hypothesis*. These are analytical prerequisites with existing course assignments; the character theta transformation, completion, boundary nonvanishing, zero locations, real part of the product constant, integer values and character convexity estimate are proved here. Generalized Riemann hypothesis remains a conjecture: it asserts that the nontrivial zeros are all on \(\Re s=1/2\), not merely in the open strip proved here.

## References

D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorem 11.1, gives the theta route, and Lemma 11.2 gives related bounds from character sums. The residue-subtraction and interpolation arguments above supply their details for our stated conventions. The finite integer-value formula is the classical generalized-Bernoulli formula. E. Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen*, Chapter VIII, develops the historical theta approach; the phase used here was proved in the preceding Gauss-sum lesson.
