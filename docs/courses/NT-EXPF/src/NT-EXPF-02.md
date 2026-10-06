# Explicit formulas for Dirichlet L-functions and primes in progressions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The zeros of a Dirichlet \(L\)-function measure a signed prime sum. Averaging these identities over characters isolates a residue class. There are two details to retain throughout: the completed function uses the **conductor**, and reflection sends a residue class to its **inverse**. Smoothing then makes the zero sum absolutely convergent and gives the GRH bound for the least prime in a progression. At the end, the same contour argument is applied to Hecke characters, and its local terms are assembled into Weil's idèlic formula.

## 1. Completion, reflection and admissible functions

We use the conventions of The explicit formula with general test functions:

\[
H(s)=\widetilde f(s)=\int_0^\infty f(x)x^s\frac{dx}{x},
\qquad f^\sharp(x)=x^{-1}f(x^{-1}). \tag{1.1}
\]

The class used for the symmetric zero sums below is the following. Put \(F(u)=e^{u/2}f(e^u)\). Away from finitely many jumps, \(F\) is continuously differentiable, has finite one-sided derivatives, and, for some \(\delta>0\),

\[
|F(u)|+|F'(u)|\leq C e^{-(1/2+\delta)|u|}.
\tag{1.2}
\]

At a jump, \(F\) is assigned the average of its one-sided values. The weighted bounded-variation extension proved in the preceding lesson also applies. In particular, every smooth compactly supported \(f\), and the interval test used below, is allowed. Value bounds alone on an otherwise unrestricted piecewise smooth function do not imply the Mellin decay needed here. For that broader class, the iterated cutoff formula of the preceding lesson remains available; we do not interchange its limits.

Let \(\chi\) be primitive of conductor \(q>1\), and write \(\chi(-1)=(-1)^a\), \(a=0\) or (1). Set

\[
\Lambda_\chi(s)=
\left(\frac q\pi\right)^{(s+a)/2}
\Gamma\left(\frac{s+a}{2}\right)L(s,\chi).
\tag{1.3}
\]

This is entire, of order one, and satisfies

\[
\Lambda_\chi(s)=\epsilon_\chi\Lambda_{\bar\chi}(1-s),
\qquad
\epsilon_\chi=\frac{\tau(\chi)}{i^a\sqrt q},\quad |\epsilon_\chi|=1.
\tag{1.4}
\]

Its zeros are the nontrivial zeros of \(L(s,\chi)\). They occur with multiplicity; no critical-line hypothesis is being made. Their reflection \(\rho\mapsto1-\rho\) changes \(\chi\) to \(\bar\chi\). Conjugation does the same, so \(\rho\mapsto1-\bar\rho\) preserves the zeros of the given character.

The internal prerequisite *The functional equation of Dirichlet L-functions*, lesson 5 of *Dirichlet L-functions and primes in progressions*, supplies (1.3)–(1.4), the simple trivial zeros \(-a-2j\), and the order-one product. Lesson 8, *Counting zeros and the explicit formula for ψ(x, χ)*, supplies the zero count

\[
\#\{\rho:|\Im\rho|\leq T\}
=\frac T\pi\log\frac{qT}{2\pi e}+O(\log(q(T+2))).
\tag{1.5}
\]

These are existing planned internal lessons; a published proof version has not been linked here. We use these precise prerequisite statements, while proving the test-function formula and its applications below. The last section additionally uses the existing planned lessons *Idèles and the idèle class group*, *Additive characters, self-dual measures and Poisson summation on the adèles*, and *Hecke L-functions and the Dedekind zeta function* in *Adèles, idèles and Tate's thesis*.

For clarity about the contour estimates, (1.5) implies

\[
\#\{\rho: t\leq|\Im\rho|\leq t+1\}
\ll\log(q(t+2)). \tag{1.6}
\]

Indeed the main term changes by \(O(\log(q(t+2)))\) on an interval of length one, and the two error terms have that size. In each \([T,T+1]\) we can therefore select a height whose distance from every zero ordinate is at least \(c/\log(q(T+2))\). Subtracting the order-one logarithmic derivative at \(2+it\) from its value at \(\sigma+it\), the zeros with ordinate distance greater than one contribute

\[
O\left(\sum_{j\geq1}
\frac{\log(q(|t|+j+2))}{j^2}\right)=O(\log(q(|t|+2)))
\]

on any fixed bounded strip. The remaining \(O(\log(q(|t|+2)))\) zeros each contribute \(O(\log(q(|t|+2)))\). The Euler product at \(2+it\) and Stirling's formula bound the subtracted value. Thus the logarithmic derivative is \(O(\log^2(q(T+2)))\) at the selected heights. The same choice works for both \(\chi\) and \(\bar\chi\), since their ordinates are negatives of one another.

## 2. The explicit formula and its two parities

Write \(\psi_\Gamma=\Gamma'/\Gamma\), reserving \(\psi(x,\chi)\) for a prime counting function. Define

\[
P_\chi(f)=\sum_{n\geq2}\Lambda(n)
\bigl(\chi(n)f(n)+\bar\chi(n)f^\sharp(n)\bigr),
\tag{2.1}
\]

and

\[
A_{q,a}(f)=\log(q/\pi)f(1)+G_a(f), \tag{2.2}
\]

where the following two expressions for \(G_a\) agree:

\[
G_a(f)=\frac1{2\pi}\lim_{T\to\infty}
\int_{-T}^{T}
\Re\psi_\Gamma\left(\frac{1/2+a+it}{2}\right)
H(1/2+it)\,dt, \tag{2.3}
\]

\[
G_a(f)=-\gamma f(1)+
\int_0^\infty
\frac{2e^{-2u}f(1)-e^{-au}\bigl(f(e^u)+f^\sharp(e^u)\bigr)}
{1-e^{-2u}}\,du. \tag{2.4}
\]

Here \(\gamma\) is Euler's constant. Near zero, the numerator of (2.4) is \(O(u)\), including when \(f\) jumps at \(1\): the sum of the two one-sided limits is \(2f(1)\). At infinity, (1.2) makes the integral convergent.

**Theorem 2.1.** For a primitive character of conductor \(q>1\),

\[
\boxed{\displaystyle
\lim_{T\to\infty}\sum_{|\Im\rho|<T}H(\rho)
=-P_\chi(f)+A_{q,a}(f).}
\tag{2.5}
\]

There are no pole terms because \(\Lambda_\chi\) is entire. For the primitive principal character of conductor \(1\), which gives \(\zeta\), the corresponding identity has the additional term \(H(0)+H(1)\), and \(A_{1,0}=-W_{\mathbb R}\) in the preceding lesson's notation.

*Proof.* Mellin integration by parts, treating the jumps as atoms of \(dF\), gives \(H(\sigma+it)=O((1+|t|)^{-1})\) uniformly on a closed strip slightly larger than \([0,1]\). Integrate \(H(s)\Lambda_\chi'/\Lambda_\chi(s)\) round a rectangle with vertical sides \(c\) and \(1-c\), where \(1<c<1+\delta\), and the selected heights from Section 1. The horizontal integrals tend to zero, being \(O(\log^2(qT)/T)\). The functional equation turns the left side into a second right-side integral. Hence the residue theorem gives

\[
\sum_\rho H(\rho)=\frac1{2\pi i}\int_{(c)}
\left(H(s)\frac{\Lambda_\chi'}{\Lambda_\chi}(s)
+H(1-s)\frac{\Lambda_{\bar\chi}'}{\Lambda_{\bar\chi}}(s)\right)ds.
\tag{2.6}
\]

All integrals with only \(1/t\) decay in this proof are symmetric integrals. The inversion and convolution justification for the Dirichlet series is exactly the one proved in Lemma 1.2 and the contour proof of the preceding lesson: the derivative measure has finite weighted variation, and the coefficients \(\Lambda(n)n^{-c}\) are summable. Expanding the Euler logarithmic derivatives therefore gives

\[
-\sum_n\Lambda(n)\left(\chi(n)f(n)
+\bar\chi(n)n^{-1}f(n^{-1})\right).
\]

The two constants \(\tfrac12\log(q/\pi)\) give \(\log(q/\pi)f(1)\). Move the gamma integrals to the critical line; no gamma pole lies between the lines in question. Substitution \(t\mapsto-t\) in the reflected integral gives (2.3), since \(\psi_\Gamma(\bar z)=\overline{\psi_\Gamma(z)}\).

To evaluate it, use, for \(\Re z>0\),

\[
\psi_\Gamma(z)=-\gamma+
\int_0^\infty\frac{e^{-v}-e^{-zv}}{1-e^{-v}}\,dv.
\tag{2.7}
\]

This identity follows by logarithmically differentiating Euler's gamma product, expanding \(1/(1-e^{-v})\), and integrating each exponential; the cancellation at zero justifies the passage to the limit. Put \(v=2u\). Fourier inversion for \(F\) turns \(e^{-(a+1/2)u}\cos(tu)\) into \(\tfrac12e^{-au}(f(e^u)+f^\sharp(e^u))\), giving (2.4).

The limiting interchange at a jump is not an appeal to absolute convergence of (2.3). The jump argument in Section 4 of the preceding lesson applies: after subtracting a smooth function with the same value at zero, the singular Fourier kernel is bounded by \(C(1+|\log|u||)\), integrable against the remaining derivative measure near zero and its exponentially decaying tails. Replacing the di\gamma parameter \(1/4\) by \(3/4\) changes its large-\(t\) expansion by \(O((1+|t|)^{-2})\), an absolutely integrable change after multiplication by \(H\). This proves the asserted symmetric limit for each parity.

Finally, passing from the selected heights to arbitrary symmetric heights changes at most \(O(\log(qT))\) terms of size \(O(1/T)\). This tends to zero. ∎

The parity dependence is especially simple:

\[
\boxed{G_1(f)-G_0(f)=
\int_0^\infty\frac{f(e^u)+f^\sharp(e^u)}{1+e^{-u}}\,du.}
\tag{2.8}
\]

Subtract (2.4) for \(a=0\) and \(a=1\); the factor \(1-e^{-u}\) cancels. The conductor and parity are separate: the first changes the coefficient of \(f(1)\), while the second changes an actual kernel.

## 3. Isolating a progression

For a character \(\chi\bmod q\), let \(\chi^*\) be its primitive inducing character of conductor \(q_\chi\mid q\). Then

\[
L(s,\chi)=L(s,\chi^*)
\prod_{p\mid q}(1-\chi^*(p)p^{-s}). \tag{3.1}
\]

Factors with \(\chi^*(p)=0\) are (1). Their other zeros are not nontrivial zeros of the primitive completed function and must not be put into (2.5). Instead retain the missing Euler terms

\[
E_\chi(f)=\sum_{p\mid q}\log p\sum_{m\geq1}
\left(\chi^*(p)^m f(p^m)
+\bar\chi^*(p)^m f^\sharp(p^m)\right).
\tag{3.2}
\]

Thus \(P_\chi=P_{\chi^*}-E_\chi\). If \(f\) is compactly supported, (3.2) is finite. More generally its absolute value is bounded by the same expression with the character values replaced by \(1\); (1.2) makes each geometric tail convergent.

Fix \((b,q)=1\), and put

\[
S_b(f)=\sum_{n\equiv b\ (q)}\Lambda(n)f(n).
\]

Character orthogonality gives

\[
\frac1{\varphi(q)}\sum_{\chi\bmod q}\bar\chi(b)P_\chi(f)
=S_b(f)+S_{b^{-1}}(f^\sharp). \tag{3.3}
\]

Indeed \(\bar\chi(b)\chi(n)\) averages to the indicator of \(n\equiv b\), whereas \(\bar\chi(b)\bar\chi(n)=\overline{\chi(bn)}\) averages to the indicator of \(n\equiv b^{-1}\). The two classes coincide exactly when \(b^2\equiv1\bmod q\).

For convenience let \(Z_\chi(f)=\sum_{\rho\ {\rm of}\ \chi^*}H(\rho)\), with the symmetric convention, and let \(a_\chi\) be the parity. Combining (2.5) and (3.2)–(3.3) proves the following identity, including the principal character:

\[
\boxed{\begin{aligned}
S_b(f)+S_{b^{-1}}(f^\sharp)
={1\over\varphi(q)}\bigg(&H(0)+H(1)
-\sum_{\chi\bmod q}\bar\chi(b)Z_\chi(f)\\
&+\sum_{\chi\bmod q}\bar\chi(b)
\bigl(A_{q_\chi,a_\chi}(f)-E_\chi(f)\bigr)\bigg).
\end{aligned}} \tag{3.4}
\]

The pole term occurs once, from the character whose primitive conductor is \(1\). Its coefficient is \(1\).

A formula with **both** terms in class \(b\) is obtained without changing conventions. Split \(f=f_++f_-\), with \(f_+\) zero for \(x<1\), \(f_-\) zero for \(x>1\), and each assigned half of \(f(1)\) at \(1\). Apply (3.4) to \(f_+\) and class \(b\), and to \(f_-\) and class \(b^{-1}\). Since \(n\geq2\), their left sides add to

\[
\sum_{n\equiv b\ (q)}\Lambda(n)
\bigl(f(n)+n^{-1}f(n^{-1})\bigr). \tag{3.5}
\]

Their right sides are the corresponding two displayed right sides of (3.4). This splitting is essential when \(b\ne b^{-1}\). For example, modulo (5), the unsplit reflected term for \(b=2\) belongs to class (3).

## 4. Why one smoothing removes a logarithm

The unsmoothed GRH estimate for a prime counting function has a squared logarithm. Applying that estimate directly to the existence of a prime loses a logarithm in the resulting bound. We instead use the triangular weight

\[
S(X,\chi)=\sum_{n\leq X}\Lambda(n)\chi(n)(1-n/X),
\qquad X\geq2. \tag{4.1}
\]

**Lemma 4.1.** Assume GRH for the primitive function inducing \(\chi\bmod q\), including \(\zeta\) for the principal character. With \(\delta_\chi=1\) for the principal character and \(0\) otherwise,

\[
S(X,\chi)=\delta_\chi X/2
-\sum_\rho{X^\rho\over\rho(\rho+1)}
+O(\log(q+2)\log X). \tag{4.2}
\]

The zero sum is over the primitive function, and is absolutely convergent. Its absolute value is \(O(\sqrt X\log(q+2))\), with absolute constants.

*Proof.* Elementary inverse Mellin integration gives

\[
{1\over2\pi i}\int_{(c)}{y^s\over s(s+1)}\,ds
=\begin{cases}1-y^{-1},&y>1,\\0,&0<y\leq1,
\end{cases}\qquad c>0. \tag{4.3}
\]

Close left for \(y>1\), picking the residues at \(0,-1\), and right for \(y<1\); the \(1/t^2\) decay kills the horizontal sides. At \(y=1\), dominated convergence gives (0). Expanding \(-L'/L\) on \(c=2\) therefore proves

\[
S(X,\chi^*)={1\over2\pi i}\int_{(2)}
-{L'\over L}(s,\chi^*){X^s\over s(s+1)}\,ds.
\tag{4.4}
\]

Move the line to \(-1/2\). The good-height estimate of Section 1 kills the horizontal integrals. A nontrivial zero contributes \(-X^\rho/(\rho(\rho+1))\). The pole of \(\zeta\) contributes \(X/2\). At (0), write

\[
{L'\over L}(s,\chi^*)=
\begin{cases}s^{-1}+c_\chi+O(s),&\chi^*\text{ even and nonprincipal},\\
c_\chi+O(s),&\chi^*\text{ odd}.
\end{cases} \tag{4.5}
\]

The resulting residues are \(-\log X+1-c_\chi\) and \(-c_\chi\), respectively. For \(\zeta\), the residue is \(-\log(2\pi)\). There are no other trivial zeros between these lines, and the kernel's pole at \(-1\) is outside.

Here is a uniform bound for \(c_\chi\), rather than an unestimated constant hidden in the formula. Subtract the order-one logarithmic derivative at \(2\) from the one at \(s\), canceling its exponential constant:

\[
{L'\over L}(s)-{L'\over L}(2)
=-{1\over2}\left[
\psi_\Gamma((s+a)/2)-\psi_\Gamma((2+a)/2)\right]
+\sum_\rho\left({1\over s-\rho}-{1\over2-\rho}\right).
\tag{4.6}
\]

Under GRH, \(\rho=1/2+i\gamma\). At \(s=0\), the summand is bounded by \(C/(1+\gamma^2)\). Equation (1.6), summed over unit intervals, bounds its absolute sum by \(C\log(q_\chi+2)\). Subtract \(1/s\) from the gamma term when \(a=0\); its remaining constant is absolute. The Euler product bounds \(L'/L(2)\) absolutely. Thus \(|c_\chi|\ll\log(q_\chi+2)\).

On \(\Re s=-1/2\), logarithmic differentiation of the functional equation expresses \(L'/L(s)\) through the absolutely convergent Euler series at \(1-s\) and the gamma derivatives. The line avoids all trivial gamma poles, so its size is \(O(\log(q_\chi(|t|+2)))\). The remaining integral in (4.4) is consequently \(O(X^{-1/2}\log(q_\chi+2))\).

Also, by (1.6),

\[
\sum_\rho{1\over|\rho(\rho+1)|}
\ll\sum_{j\geq0}{\log(q_\chi(j+2))\over1+j^2}
\ll\log(q_\chi+2). \tag{4.7}
\]

This proves absolute convergence and the claimed square-root bound. Finally, removing the prime powers at \(p\mid q\) changes (4.1) by at most

\[
\sum_{p\mid q}\log p\left\lfloor{\log X\over\log p}\right\rfloor
\leq\omega(q)\log X\ll\log(q+2)\log X.
\]

The lemma follows. ∎

**Theorem 4.2.** Under GRH for every Dirichlet \(L\)-function modulo \(q\geq2\), every reduced class \(b\bmod q\) contains a prime \(p\) with

\[
\boxed{p\ll\bigl(\varphi(q)\log(q+2)\bigr)^2.} \tag{4.8}
\]

Thus the power of \(\log q\) is **two**, not four. The implied constant is absolute.

*Proof.* Average (4.2) with weight \(\bar\chi(b)/\varphi(q)\). Orthogonality gives

\[
S_b(X):=\sum_{n\equiv b\ (q)}\Lambda(n)(1-n/X)_+
={X\over2\varphi(q)}
+O\bigl(\sqrt X\log(q+2)+\log(q+2)\log X\bigr).
\tag{4.9}
\]

We must distinguish a prime from a higher prime power. The elementary estimate \(\psi(y)\ll y\) suffices. To prove it, for an integer \(n\), every prime power in ((n,2n]) contributes its prime's logarithm to (log\binom{2n}{n}): in the factorial valuation, the term belonging to that power is \(1\), and all the other terms are nonnegative. Hence (psi(2n)-psi(n)\leq2n\log2). Summing at powers of two and enclosing a general (y) between two such powers gives (psi(y)\leq4y\log2). Therefore

\[
\sum_{\substack{p^m\leq X\\m\geq2}}\log p
\leq\psi(\sqrt X)+
\sum_{3\leq m\leq\log_2 X}\psi(X^{1/m})
\ll\sqrt X+X^{1/3}\log X\ll\sqrt X. \tag{4.10}
\]

Put \(L=\log(q+2)\) and \(X=K\varphi(q)^2L^2\). The main term in (4.9) is \(K\varphi(q)L^2/2\). The square-root error is at most \(C\sqrt K\varphi(q)L^2\), and the contribution (4.10) is at most \(C\sqrt K\varphi(q)L\). Since \(\varphi(q)\leq q\), the remaining error is at most \(C L(\log K+4L)\). Choose one sufficiently large absolute \(K\): its linear growth dominates both \(\sqrt K\) and \(\log K\), uniformly for \(q\geq2\). Equation (4.9) then exceeds (4.10). Some positive-weight term must be a prime in the desired class. ∎

## 5. The odd character modulo four and prime squares

Let \(\chi_{-4}(n)=0\) for even \(n\), (1) for \(n\equiv1\bmod4\), and \(-1\) for \(n\equiv3\bmod4\). It is primitive, odd, and real. Its formula is

\[
\sum_\rho H(\rho)
=-\sum_n\Lambda(n)\chi_{-4}(n)
\bigl(f(n)+f^\sharp(n)\bigr)
+\log(4/\pi)f(1)+G_1(f). \tag{5.1}
\]

For the one-sided triangular weight in (4.1), define

\[
\Theta_j(X)=\sum_{p\equiv j\ (4)}\log p\,(1-p/X)_+,
\quad j=1,3.
\]

Then the exact elementary decomposition is

\[
S(X,\chi_{-4})=
\Theta_1(X)-\Theta_3(X)
+\sum_{\substack{p\ {
m odd},\ m\geq2}}\log p\,
\chi_{-4}(p)^m(1-p^m/X)_+. \tag{5.2}
\]

All even exponents have sign \(+1\), including squares of primes in class (3). Solving (5.2) for \(Theta_3-Theta_1\) therefore produces a **positive square contribution**. The zeros govern the remaining oscillation through (4.2). This explains the direction of the familiar Chebyshev bias without claiming that this finite computation proves a density theorem for the bias.

At \(X=100\), direct finite summation gives the following reproducible values; logarithms are natural:

| Quantity | Value |
|---|---:|
| \(S(100,\chi_{-4})\) | -1.493642350 |
| \(Theta_3(100)-Theta_1(100)\) | 4.099621507 |
| contribution of \(p^2\), \(p\) odd | 3.199229793 |
| contribution of all higher powers \(p^m\), \(m\geq3\) | -0.593250636 |

The last two rows minus the first equal the second, as (5.2) requires. Squares make a systematic positive contribution; higher odd powers and zeros retain their signs.

## 6. Hecke characters: the same contour, all local factors

Let \(k\) be a number field of degree \(d=r_1+2r_2\), with discriminant \(D_k\). A unitary Hecke character is a continuous unitary character of \(C_k=\mathbb A_k^\times/k^\times\). At a real place write

\[
\chi_v(x)=\operatorname{sgn}(x)^{a_v}|x|^{i\tau_v};
\]

at a complex place use the local norm \(|z|_v=|z|^2\) and write

\[
\chi_v(z)=(z/|z|)^{m_v}|z|_v^{i\tau_v}.
\]

Let \(\mathfrak f_\chi\) be its finite conductor, and put

\[
Q_\chi=|D_k|N\mathfrak f_\chi,
\qquad
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),
\quad\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
\]

The archimedean product and completed function are

\[
G_\chi(s)=
\prod_{v\ {\rm real}}\Gamma_{\mathbb R}(s+a_v+i\tau_v)
\prod_{v\ {\rm complex}}\Gamma_{\mathbb C}(s+|m_v|/2+i\tau_v),
\quad
\Lambda_\chi(s)=Q_\chi^{s/2}G_\chi(s)L(s,\chi).
\tag{6.1}
\]

For an unramified prime ideal, \(\chi(\mathfrak p)\) means \(\chi_v(\varpi_v)\); it is set to zero at a ramified prime. Thus

\[
L(s,\chi)=\prod_{\mathfrak p}(1-\chi(\mathfrak p)(N\mathfrak p)^{-s})^{-1}.
\]

The internal lesson *Hecke L-functions and the Dedekind zeta function*, lesson 10 of *Adèles, idèles and Tate's thesis*, proves the continuation and functional equation

\[
\Lambda_\chi(s)=\epsilon_\chi\Lambda_{\bar\chi}(1-s).
\tag{6.2}
\]

It is an existing planned proof provider. Its Tate-theoretic proof, using lessons 5 and 7–9 of that course, supplies rapid-decay integral representations away from the pole terms. Those representations give order at most one after the poles are removed: splitting the norm integral at \(1\), differentiating under its rapidly decreasing tails, bounds growth by \(\exp(C|s|\log(|s|+2))\). They also give polynomial growth in bounded strips, by integration by parts in the norm variable. These are the analytic inputs needed for the following contour proof. When \(\chi=|\cdot|^{i\tau}\), the completed function has poles at \(-i\tau,1-i\tau\). Otherwise it is entire. Write \(\mathcal P_\chi\) for these poles, with multiplicities.

We will also need a bound uniform as the archimedean character varies. Set \(B=10+\sum_v(|\tau_v|+|m_v|+a_v)\), with \(m_v=0\) at real places and \(a_v=0\) at complex places. On \(\Re s=2\), the Euler product bounds both \(|L(s,\chi)|\) and its reciprocal by constants depending only on \(k\). On any fixed line left of zero, (6.2) and Stirling's formula bound \(L(s,\chi)\) by \(C_k Q_\chi^{C_k}(B+|\Im s|)^{C_k}\): the exponential factors in the gamma quotient cancel, and the remaining ratio is a fixed power of its shifted argument. This bound remains uniform at zeros of reciprocal gamma factors, since the quotient is entire there. Remove the possible pole at \(1-i\tau\) by multiplying \(L\) by \(s-1+i\tau\). The same polynomial bound holds throughout any fixed strip. Indeed divide the pole-removed function by \((B+s)^M\), with a sufficiently large fixed \(M\) and, if necessary, \(B\) enlarged to put \(-B\) outside the strip, and multiply by \(e^{\varepsilon s^2}\). The maximum principle applies on rectangles: the order-one growth bound kills the horizontal sides for each \(\varepsilon>0\), and the vertical bounds are uniform. Let \(\varepsilon\downarrow0\).

Jensen's formula in the disk centered at \(2+it\), with outer radius \(4\) and inner radius \(3\), now bounds zeros in a unit interval. Its center has an absolute lower bound from the Euler product; the removed pole factor has modulus at least \(1\) there. The larger disk lies in a fixed strip, so the polynomial estimate gives

\[
\#\{\rho:t\leq\Im\rho\leq t+1\}
\ll_k \log Q_\chi+\log(B+|t|+2).
\tag{6.4}
\]

The smaller disk contains that portion of the critical strip. A completed zero is a zero of \(L\), with no larger multiplicity: a gamma pole cancels zeros of \(L\), rather than adding completed zeros. Thus the same estimate counts completed zeros, including possible boundary zeros. This is the uniform input for the character sum in the next section.

**Theorem 6.1 (Hecke explicit formula).** If \(f\in C_c^\infty(\mathbb R_+^\times)\), then

\[
\boxed{\begin{aligned}
\sum_\rho H(\rho)
={}&\sum_{\pi\in\mathcal P_\chi}H(\pi)
-\sum_{\mathfrak p,m\geq1}\log N\mathfrak p
\left(\chi(\mathfrak p)^m f((N\mathfrak p)^m)
+\bar\chi(\mathfrak p)^m f^\sharp((N\mathfrak p)^m)\right)\\
&+\log Q_\chi\,f(1)
+\frac1{2\pi}\int_{\mathbb R}
2\Re\frac{G_\chi'}{G_\chi}(1/2+it)H(1/2+it)\,dt.
\end{aligned}} \tag{6.3}
\]

Both the zero sum and the integral are absolutely convergent. The prime-ideal sum is finite.

*Proof.* Repeated integration by parts in \(u=\log x\) gives \(H(\sigma+it)=O_N((1+|t|)^{-N})\) on every bounded strip. We record why the contour can avoid zeros here as well. The order-one bound above and Jensen's formula give \(O_\chi(T\log(T+2))\) zeros up to height \(T\). At heights in \([T,T+1]\), delete intervals of radius \(T^{-3}\) around the ordinates of the zeros with height at most \(2T\). Their total length is \(O_\chi(T^{-2}\log T)\), so a remaining height exists. Subtract logarithmic derivatives at a fixed point to the right of the critical strip. The order-one partial fractions and the zero count bound the terms at that height by a polynomial in \(T\); the tail is bounded by the convergent sum of \(O(1/|\rho|^2)\). Choosing \(N\) larger than that polynomial exponent kills the horizontal integrals. Removed poles are included as negative residues of \(\Lambda'/\Lambda\).

Choose the right side farther right than every archimedean shift's pole; all gamma poles have real part at most zero. Use (6.2) to replace the left side by the right-side integral for the dual character, exactly as in (2.6). The Euler expansions give the two finite prime-ideal sums. The constants \(\tfrac12\log Q_\chi\) give \(\log Q_\chi f(1)\). Move only the gamma terms to \(\Re s=1/2\); their poles remain to the left. The dual factors obey \(G_{\bar\chi}(\bar s)=\overline{G_\chi(s)}\); changing \(t\) to \(-t\) gives the last line of (6.3). Mellin inversion and absolute convergence now justify every step without a jump-limit argument. The zero count and rapid decrease of \(H\) give absolute convergence. Compact support bounds \(N\mathfrak p^m\) above and below, so there are finitely many prime ideals involved. ∎

For finite-order characters all \(\tau_v=0\), and the gamma density is even in \(t\). For general unitary characters it need not be even. The real-part expression in (6.3), with the displayed shifts retained, is the appropriate one. Weil's 1952 formula (11) has the same content with its conductor and gamma constants grouped differently.

## 7. The idèlic formula and the meaning of its principal values

This section makes the local normalizations explicit, so that an unspecified principal value cannot conceal a conductor or discriminant. Normalize Haar measure on \(C_k^1=\ker|\cdot|\) to mass \(1\), and choose a splitting \(C_k\simeq C_k^1\times\mathbb R_+^\times\). Use \(dt/t\) in the second factor. At a finite place of residue cardinality \(q_v\), use multiplicative Haar measure with unit group mass \(\log q_v\); at a real place use \(dx/(2|x|)\); at a complex place use \(2\,dr/r\,d\theta/(2\pi)\). These local measures are the ones for which volume accumulated through successive norm shells grows as \(\log\Lambda\). They are not the restricted-product measures of unit mass used when forming Tate's zeta integral.

Fix the standard global additive character obtained from the rational one by the trace. Its real component is \(e^{-2\pi ix}\), its complex component is \(e^{-2\pi i(z+\bar z)}\), and its finite component is trivial on the inverse different \(\mathfrak D_v^{-1}\). The internal lesson *Additive characters, self-dual measures and Poisson summation on the adèles* establishes these conductors and self-dual measures.

For a smooth compactly supported function \(h\) on \(C_k\), define

\[
\widehat h(\chi,s)=\int_{C_k}h(u)\chi(u)|u|^s\,d^*u.
\tag{7.1}
\]

Here \(\chi\) runs through the characters of \(C_k^1\), each extended to be trivial on the chosen norm splitting. Write \(\widehat h(s)=\widehat h(1,s)\). The local test function is the restriction of \(h\) along \(k_v^\times\to C_k\).

We now define \(\int'\), rather than leaving a cutoff implicit. At a finite place first take an additive character of conductor \(\mathcal O_v\). For a compactly supported locally constant test \(b\) on \(k_v^\times\), set

\[
W_v(b)=\int_{\mathcal O_v^\times}
\frac{b(u^{-1})-b(1)}{|1-u|_v}\,d^*u
+\int_{k_v^\times\setminus\mathcal O_v^\times}\frac{b(u^{-1})}{|1-u|_v}\,d^*u.
\tag{7.2}
\]

The integrand vanishes in a neighborhood of (1). For the trace character, whose conductor is \(\mathfrak D_v^{-1}\), replace (7.2) by

\[
W_v(b)-\operatorname{ord}_v(\mathfrak D_v)\log q_v\,b(1).
\tag{7.3}
\]

At an infinite place choose any smooth radial compactly supported \(r(|u|_v)\) with \(r(1)=1\). Define

\[
W_v(b)=\int_{k_v^\times}
\frac{b(u^{-1})-b(1)r(|u|_v^{-1})}{|1-u|_v}\,d^*u
+b(1)C_v(r), \tag{7.4}
\]

where \(C_{\mathbb R}(r)=W_{\mathbb R}(r)\) is the real-place formula in the preceding lesson, and

\[
C_{\mathbb C}(r)=2(\log(2\pi)+\gamma)
+\int_0^\infty
\frac{r(e^u)+e^{-u}r(e^{-u})-2e^{-u}}{1-e^{-u}}\,du.
\tag{7.5}
\]

The integral in (7.4) is locally absolutely convergent: its numerator is \(O(|u-1|)\). In two real dimensions this cancels enough of the denominator \(|u-1|^2\). Independence of \(r\) follows by subtracting two choices and using the radial kernel computations just below. If an additive character is changed to \(x\mapsto\alpha_v(ax)\), add \(\log|a|_v b(1)\) to these definitions. Globally a change by \(a\in k^\times\) changes their sum by zero, by the product formula. Equations (7.2)–(7.5) specify the additive-character-normalized principal value denoted by \(\int'\).

**Local calculation.** For \(b(u)=\bar\chi_v(u)f(|u|_v)\), these distributions equal the prime terms minus the local conductor term at finite places, and minus the gamma-density term at infinite places.

At an unramified finite place, the unit-shell contribution in (7.2) vanishes. On \(|u|_v=q_v^{-m}<1\), the denominator is \(1\), giving \((\log q_v)\chi_v(\varpi_v)^m f(q_v^m)\). On \(|u|_v=q_v^m>1\), the denominator is \(q_v^m\), giving the reflected term. Thus the total is the local summand of \(P_\chi(f)\).

Suppose instead that the character has conductor exponent \(n\geq1\). All nonunit shells integrate to zero by unit-character orthogonality. On the units, \(f(|u|)=f(1)\). Put \(U_j=1+\mathfrak p_v^j\), \(j\geq1\), and \(U_0=\mathcal O_v^\times\). The integral of \(\chi_v\) on \(U_j\) is zero for \(j<n\), and is \(\mu(U_j)\) for \(j\geq n\). Since \(\mu(U_j)=(\log q_v)q_v^{-j}/(1-q_v^{-1})\), summing the annuli \(U_j\setminus U_{j+1}\) gives

\[
\int_{\mathcal O_v^\times}
\frac{\chi_v(u)-1}{|1-u|_v}\,d^*u=-n\log q_v. \tag{7.6}
\]

For \(n=1\), only the first annulus contributes and its value is \(-\log q_v\). For \(n>1\), the first contributes \(-\log q_v+\log q_v/(q_v-1)\), the \(n-2\) middle annuli each contribute \(-\log q_v\), and the last contributes \(-q_v\log q_v/(q_v-1)\); their sum is (7.6). Including (7.3) gives \(-(n+\operatorname{ord}_v\mathfrak D_v)\log q_v f(1)\).

At a real place first set \(\tau_v=0\). Pair the positive and negative half-lines in (7.4). The even kernel is \(W_{\mathbb R}(f)=-A_{1,0}(f)\). Changing to the odd character changes its value by

\[
-\int_0^\infty\frac{f(e^u)+f^\sharp(e^u)}{1+e^{-u}}\,du,
\]

so (2.8) gives \(-A_{1,1}(f)\). This is

\[
-\frac1{2\pi}\int_\mathbb R
2\Re\frac{\Gamma_{\mathbb R}'}{\Gamma_{\mathbb R}}(1/2+a_v+it)
H(1/2+it)\,dt.
\tag{7.7}
\]

A norm twist is obtained by replacing \(f(x)\) with \(x^{-i\tau_v}f(x)\), then changing \(t\) in the integral. This inserts \(+i\tau_v\) in the gamma argument, as in (6.1).

At a complex place the angular integral is elementary:

\[
\int_0^{2\pi}\frac{e^{im\theta}}{1-2r\cos\theta+r^2}\frac{d\theta}{2\pi}
=\begin{cases}
r^{|m|}/(1-r^2),&r<1,\\
r^{-|m|}/(r^2-1),&r>1.
\end{cases} \tag{7.8}
\]

Expand the two geometric series for \(r<1\) and select the coefficient of \(e^{-im\theta}\); the case \(r>1\) follows by replacing \(r\) with \(1/r\). In the definition (7.4), change variables \(r=e^{\pm u/2}\). Equation (7.8) and (7.5) give

\[
W_v(b)=2(\log(2\pi)+\gamma)f(1)
+\int_0^\infty
\frac{e^{-|m_v|u/2}(f(e^u)+f^\sharp(e^u))-2e^{-u}f(1)}{1-e^{-u}}\,du.
\tag{7.9}
\]

Using (2.7), now without the change \(v=2u\), this is minus the density for \(\Gamma_{\mathbb C}(s+|m_v|/2)\). Twisting inserts \(i\tau_v\) as before. These computations also prove the asserted independence of the radial reference \(r\). They identify the local principal values completely, including constants; no general trace formula has been assumed.

**Theorem 7.1 (Weil's idèlic explicit formula).** For \(h\in C_c^\infty(C_k)\), with smoothness meaning ordinary smoothness at infinity and local constancy at finite places,

\[
\boxed{\widehat h(0)+\widehat h(1)
-\sum_{\chi\in\widehat{C_k^1}}\sum_{\rho\ {\rm of}\ \Lambda_\chi}
\widehat h(\chi,\rho)
=\sum_v\int'_{k_v^\times}
\frac{h(u^{-1})}{|1-u|_v}\,d^*u.} \tag{7.10}
\]

*Proof.* First take \(h(u)=\bar\chi(u)f(|u|)\). Orthogonality on \(C_k^1\) makes every Mellin coefficient vanish except the one for \(\chi\), which equals \(H(s)\). Pole terms occur only for the trivial character, since our extensions are trivial on the norm splitting. The finite local computations give \(P_\chi(f)-\log Q_\chi f(1)\): the sum of the different exponents is \(\log|D_k|\). The infinite computations give minus the last integral in (6.3). Hence (7.10) for this \(h\) is precisely Theorem 6.1, with terms rearranged.

For a general \(h\), expand on the compact group \(C_k^1\). At the finite places, compact support and local constancy provide an open subgroup on which \(h\) is invariant. The remaining compact quotient is a torus times a finite group: its real torus comes from the archimedean units modulo the unit lattice, and the finite group from the fixed-level ray classes. These structural statements are supplied by *Idèles and the idèle class group*. Repeated integration by parts on the torus shows that the coefficient functions \(f_\chi(t)\), with all their norm derivatives, decrease faster than every power of the integer frequency of \(\chi\); their norm supports lie in one compact interval. Repeated norm integration gives the same rapid decrease in \(t=\Im s\).

To check summability against zeros, use (6.4). The finite conductors are bounded at the fixed level, and \(B\) grows at most linearly with the torus frequency. Summing the unit-interval count against \((1+|t|)^{-N}\), with \(N>2\), bounds each zero sum by a constant times \(1+\log B\) times the appropriate rapidly decreasing coefficient seminorm. The gamma densities have the same logarithmic bound by Stirling's formula. These bounds are summable over all torus frequencies, so character expansion may be integrated and summed term by term. Only finitely many finite places have nonzero local terms: outside the different and fixed finite level, the unit term is zero, and a nonunit can meet the norm support only when its residue cardinality lies in a fixed bounded interval. The equality for each Fourier component therefore sums to (7.10). ∎

The formula is independent of the chosen norm splitting: another extension translates the imaginary coordinates of the zeros and the Mellin coefficient together. This is the adelic formula displayed in Connes's *An essay on the Riemann Hypothesis*, subsection *Weil's explicit formulas*. Our proof has explained its normalization through explicit local calculations and the Hecke functional equation.

## 8. Exercises with solutions

### 1. Checking the odd gamma factor

Write \(A_{q,1}\) explicitly and check that reflecting the completed function does not change the conductor coefficient.

**Solution.** Equations (2.2) and (2.4) give

\[
A_{q,1}(f)=(\log(q/\pi)-\gamma)f(1)
+\int_0^\infty
\frac{2e^{-2u}f(1)-e^{-u}(f(e^u)+f^\sharp(e^u))}{1-e^{-2u}}\,du.
\]

Logarithmically differentiating (1.3) gives \(\tfrac12\log(q/\pi)+\tfrac12\psi_\Gamma((s+1)/2)+L'/L(s,\chi)\). Differentiating (1.4) introduces a minus sign and \(1-s\) on the dual side. Reversing that side of the contour introduces the second minus sign. The two half-conductor constants add, giving exactly \(\log(q/\pi)f(1)\); a root number has zero logarithmic derivative.

### 2. Recovering the unsmoothed character formula

Let \(x>1\), and use the interval test \(f=1_{[1,x]}\), with half endpoint values. Recover the odd and even formulas for \(\psi_0(x,\chi)\).

**Solution.** Here \(H(s)=(x^s-1)/s\), and \(P_\chi(f)=\psi_0(x,\chi)\). Direct evaluation of (2.4) gives

\[
A_{q,0}(f)=\tfrac12(\log(q/\pi)-\gamma)-\log x-\tfrac12\log(1-x^{-2}),
\]

\[
A_{q,1}(f)=\tfrac12(\log(q/\pi)-\gamma)-\log2
+\tfrac12\log\frac{x+1}{x-1}.
\]

For example, in the even case the integrand below \(u=\log x\) is \(-1\); its remaining tail is \(-\tfrac12\log(1-x^{-2})\). This already gives \(\psi_0=-\sum_\rho(x^\rho-1)/\rho+A_{q,a}\), with the symmetric sum understood as in Theorem 2.1.

To put the constant in the customary local form, define \(c_\chi\) by (4.5), without imposing GRH. The exact result is

\[
\boxed{\psi_0(x,\chi)=
-\sum_\rho\frac{x^\rho}{\rho}-c_\chi
-(1-a)\log x+
\begin{cases}
-\tfrac12\log(1-x^{-2}),&a=0,\\
\tfrac12\log\frac{x+1}{x-1},&a=1.
\end{cases}} \tag{8.1}
\]

Here is a contour verification of the constant, which also avoids assigning a value to a separated zero sum without justification. Invert \(-L'/L(s)\,x^s/s\) on \(\Re s=2\). The truncated inverse Mellin integral for \(y=x/n\) tends to \(1,0,\tfrac12\) according as \(y>1,y<1,y=1\). Its error away from (1) is bounded by \(C y^2\min(1,(T|\log y|)^{-1})\), by one integration by parts. The summable coefficients \(\Lambda(n)n^{-2}\), separating finitely many \(n\) near the fixed \(x\), justify inversion with the half weight at equality.

Shift the rectangle to \(-U\), with \(U\to\infty\) avoiding the trivial zeros by distance \(1/4\), and use the good heights of Section 1. On the bounded central strip the horizontal integrals are \(O_x(\log^2(qT)/T)\); farther left, the functional equation and its gamma derivatives give \(O(\log(q(|s|+2)))\), and the factor \(x^{\Re s}\) is integrable in that direction. Taking \(U\asymp T\), the left integral is \(O_x(x^{-U}\log(qT))\), and the remaining horizontal pieces also tend to zero. The residues at nontrivial zeros are \(-x^\rho/\rho\). At (0), (4.5) gives \(-c_\chi\) for odd parity and \(-\log x-c_\chi\) for even parity. At \(-a-2j<0\), the residue is \(x^{-a-2j}/(a+2j)\). Their geometric logarithm sums are exactly the last line of (8.1). Arbitrary symmetric heights follow from (1.6) as before. This proves (8.1) and identifies the constants in the interval-test version.

### 3. Averaging and the inverse class

Prove the progression identity and write the missing-Euler-factor correction for the principal character modulo \(q\).

**Solution.** The two orthogonality calculations in (3.3) prove the progression identity term by term; all prime series are absolutely convergent under (1.2). Substitute \(P_\chi=P_{\chi^*}-E_\chi\) and Theorem 2.1, adding the pole term for the single conductor-(1) character. This gives exactly (3.4). For the principal character, \(\chi^*=1\), so

\[
E_{\chi_0}(f)=\sum_{p\mid q}\log p\sum_{m\geq1}
\bigl(f(p^m)+f^\sharp(p^m)\bigr).
\]

Its archimedean term is \(A_{1,0}\), not \(A_{q,0}\). Formula (3.5), obtained by the two half-line tests, puts both prime terms in the same desired class.

### 4. Least prime, with higher powers excluded

Prove (4.8) from the smoothed explicit formula, explaining why the unsmoothed squared-logarithm error is insufficient for this argument.

**Solution.** The kernel \(1/(s(s+1))\) makes the zero weights summable, so (4.7) gives error \(C\sqrt X\log(q+2)\). Averaging gives (4.9). The binomial proof of \(\psi(y)\ll y\) and (4.10) bound all higher powers by \(C\sqrt X\). With \(X=K\varphi(q)^2\log^2(q+2)\), the main term grows as \(K\), both square-root errors as \(\sqrt K\), and the residual local terms as \(\log K\). One fixed large \(K\) forces a prime contribution. In contrast, an error \(\sqrt X\log^2(qX)\) would require \(\sqrt X\gg\varphi(q)\log^2(qX)\), giving a fourth power of the logarithm by this direct comparison. Smoothing is the step that removes the extra logarithm.

## 9. Proof dependencies and references

The new explicit formulas, local principal values, progression identity and least-prime deduction are proved above. Their internal analytic prerequisites are the completed Dirichlet and Hecke functional equations, their growth and zero-count inputs, and the structure and additive normalization of the idèle class group. The exact existing planned providers are identified in Sections 1, 6 and 7; their public proof versions are not asserted to be complete here. A density theorem for Chebyshev bias is not asserted or used.

The sources consulted for mathematical comparison and credit are:

- A. Weil, *Sur les « formules explicites » de la théorie des nombres premiers* (1952), beginning of the paper for Hecke characters and gamma factors, and formula (11) for the general explicit formula.
- A. Connes, *An essay on the Riemann Hypothesis* (2015/2016), subsections *Adeles and global fields* and *Weil's explicit formulas*, for the idèlic form and its additive-character normalization.
- The preceding lesson, *The explicit formula with general test functions*, for Mellin inversion at jumps and the symmetric gamma integral.

All exposition and proofs in this lesson are independently written. The cited works receive mathematical credit; their expression and licences are not incorporated into this CC0 text.
