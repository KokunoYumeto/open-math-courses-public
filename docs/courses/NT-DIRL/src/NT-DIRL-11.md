# The Siegel–Walfisz theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The prime number theorem with an exceptional term was effective. Siegel's theorem removes that term uniformly when the modulus grows like a fixed power of \(\log x\). This gives an ineffective uniform theorem in a much more useful range. The same zero-free input controls cancellation of the Möbius function, but that assertion needs a reciprocal \(L\)-function bound and its own contour argument.

We use the classical zero-free region and local analytic theory from *Zero-free regions and the exceptional zero*, the truncated Perron kernel and GRH estimates from *Counting zeros and the explicit formula for character sums over prime powers*, the exceptional-term prime theorem from *The prime number theorem for arithmetic progressions*, and the real-axis bound proved in *Siegel's theorem*. The deeper class-number discussion is not an input. Write \(\operatorname{li}(x)=\int_2^x du/\log u\); changing its additive normalization only changes bounded terms.

## 1. Removing the exceptional term

Put \(v=\log x\). The earlier theorem gives absolute effective \(a,k>0\) such that for \(q\le\exp(a\sqrt v)\),

\[
\psi(x,\chi)=\mathbf1_{\chi=\chi_0}x
-E(\chi)\frac{x^{\beta_1}}{\beta_1}
+O(xe^{-k\sqrt v}).
\tag{1.1}
\]

Here \(E(\chi)\) is 1 only for the possible exceptional real character, including its induced copies, and \(\beta_1>1/2\). For the principal character, the omitted prime powers dividing \(q\) contribute \(O(\log(2q)\log(2x))\), already absorbed in this range.

Fix \(A>0\) and suppose \(q\le v^A\). For sufficiently large \(x\), effectively in \(A\), this range is contained in the range of (1.1). Apply Siegel's real-axis estimate with exponent \(\varepsilon=1/(4A)\). If a zero occurs, its primitive conductor \(d\le q\) gives

\[
1-\beta_1\ge c(\varepsilon)d^{-\varepsilon}
\ge c(\varepsilon)v^{-1/4}.
\]

Consequently

\[
\frac{x^{\beta_1}}{\beta_1}
\le2x\exp(-c(\varepsilon)v^{3/4})
=O_A(xe^{-k\sqrt v}).
\tag{1.2}
\]

The last comparison holds beyond an ineffective threshold depending on \(A\), because \(v^{3/4}/\sqrt v\to\infty\). This choice of exponent keeps the final exponential constant absolute: its possible ineffectivity can be put entirely in the threshold or the implied constant. The frequently used choice \(1/(2A)\) also proves the theorem, but immediately produces an exponential constant depending on \(A\).

## 2. The uniform prime theorem

**Theorem 2.1 (Siegel–Walfisz).** There is an absolute \(c>0\) such that, for every \(A>0\), uniformly for \(x\ge3\), \(q\le(\log x)^A\), and \((b,q)=1\),

\[
\psi(x;q,b)=\frac{x}{\varphi(q)}
+O_A(xe^{-c\sqrt{\log x}}),
\tag{2.1}
\]

\[
\theta(x;q,b)=\frac{x}{\varphi(q)}
+O_A(xe^{-c\sqrt{\log x}}),
\tag{2.2}
\]

and

\[
\pi(x;q,b)=\frac{\operatorname{li}(x)}{\varphi(q)}
+O_A\left(\frac{x}{\log x}e^{-c\sqrt{\log x}}\right).
\tag{2.3}
\]

In particular the weaker error \(O_A(xe^{-c\sqrt{\log x}})\) holds for \(\pi\). The implied constants are ineffective.

**Proof.** Equations (1.1)–(1.2) give the character estimate with no exceptional term. Average against \(\overline{\chi(b)}\) by orthogonality and divide by \(\varphi(q)\). The sum of the absolute error bounds has exactly \(\varphi(q)\) terms, so this averaging does not introduce a factor \(\varphi(q)\). It gives (2.1) for large \(x\).

For the bounded interval below the required threshold, use \(\psi(x;q,b)\le\psi(x)\ll x\), proved earlier by the elementary Chebyshev bound. Enlarging the implied constant extends (2.1) to \(x\ge3\); this is where an ineffective threshold becomes an ineffective constant.

Higher prime powers contribute \(O(\sqrt x\log^2(2x))\), uniformly in \(q,b\). They are smaller than the displayed error after decreasing \(c\), proving (2.2).

For (2.3), split the exact partial summation at \(z=\sqrt x\):

\[
\pi(x;q,b)=\pi(z;q,b)
+\frac{\theta(x;q,b)}{\log x}
-\frac{\theta(z;q,b)}{\log z}
+\int_z^x\frac{\theta(u;q,b)}{u\log^2u}\,du.
\tag{2.4}
\]

For \(u\ge z\), the endpoint hypothesis \(q\le(\log x)^A\) implies \(q\le(\log u)^{2A}\) once \(\log x\ge4\). Thus apply (2.2) with parameter \(2A\) throughout that upper interval. The contributions at \(z\), including \(\pi(z;q,b)\) and the lower main-term normalization, are \(O(\sqrt x)\), by the elementary global estimates. They are negligible for (2.3).

The upper main terms integrate to \(\operatorname{li}(x)/\varphi(q)+O(\sqrt x)\). The endpoint error is \(O_A(xe^{-c\sqrt{\log x}}/\log x)\). Since \(\log u\ge(\log x)/2\) and \(\sqrt{\log u}\ge\sqrt{\log x}/\sqrt2\), the upper error integral is bounded by

\[
\frac{O_A(1)}{\log^2x}
\int_{\sqrt x}^x e^{-c\sqrt{\log x}/\sqrt2}\,du
\ll_A\frac{x}{\log^2x}e^{-c\sqrt{\log x}/\sqrt2}.
\]

Choose a smaller common absolute \(c\), and enlarge constants for the bounded initial range. This proves (2.3). \(\square\)

In this modulus range the error is small relative to the main term. For example, its relative size for \(\psi\) is at most
\(O_A((\log x)^A e^{-c\sqrt{\log x}})\), which tends to zero. The same holds for \(\pi\) using the stronger error in (2.3) and \(\operatorname{li}(x)\sim x/\log x\).

## 3. Bounding the reciprocal L-function

The Möbius Dirichlet series is

\[
\sum_{n\ge1}\frac{\mu(n)\chi(n)}{n^s}
=\frac1{L(s,\chi)}
\quad(\Re s>1).
\tag{3.1}
\]

Zeros of \(L\) become poles here; at the principal pole \(s=1\), its reciprocal instead has a zero. We need a bound throughout a zero-free strip, including its horizontal edges.

**Lemma 3.1.** Let \(q\ge1\), \(T\ge3\), and \(H=\log(q(T+3))\). There are absolute \(h,K>0\) with the following property. If the primitive \(L\)-function inducing a character modulo \(q\) has no zeros in

\[
\sigma\ge1-\frac{8h}{H},\qquad |t|\le T+1,
\tag{3.2}
\]

then

\[
\left|\frac1{L(\sigma+it,\chi)}\right|
\ll q^2(2H)^K
\quad\left(\sigma\ge1-\frac hH,\ |t|\le T,\ \sigma\le2\right).
\tag{3.3}
\]

For the principal primitive factor, use the zeta function and interpret its reciprocal holomorphically at 1. The constants are effective.

**Proof.** Decrease the absolute \(h\) so that all points considered have \(\sigma\ge1/2\). First treat a nonprincipal primitive character of conductor \(d\le q\).

Truncate its periodic partial-summation formula at the integer \(N=\lceil q(T+3)\rceil\). The boundary term has magnitude at most \(dN^{-\sigma}\), and the integral tail at most \(|s|dN^{-\sigma}/\sigma\). For \(\sigma\ge1-8h/H\), \(|t|\le T+1\), and \(\sigma\le2\), these are \(O(1)\): \(N^{1-\sigma}\le e^{O(h)}\), \(d\le q\), and \(|s|\ll T+3\). The finite sum is \(O(H)\), because

\[
\sum_{n\le N}n^{-\sigma}
\le N^{\max(1-\sigma,0)}\sum_{n\le N}\frac1n
\ll H.
\]

Hence \(|L(s)|\ll H\) in this band.

For each \(|t|\le T\), consider the disk with center
\(s_0=1+2h/H+it\) and radius \(R=4h/H\).
It lies inside the zero-free box (3.2). Choose its holomorphic logarithm \(g=\log L\) to agree at the center with the Euler-product logarithm. There

\[
|g(s_0)|\le\log\zeta(1+2h/H)\ll\log(2H),
\]

and throughout the disk \(\Re g\le\log(CH)\).

Here is the required elementary bound for a holomorphic logarithm. If \(g\) is holomorphic in a disk of radius \(R\), \(\Re g\le M\), and \(g_0\) is its central value, the function

\[
w(z)=\frac{g(z)-g_0}{2M-g(z)-\overline{g_0}}
\]

has modulus at most 1 and central value zero, provided \(M>\Re g_0\). The maximum principle applied to \(w(z)/z\) gives \(|w(z)|\le r/R\) on radius \(r<R\). Solving this inequality yields

\[
|g(z)-g_0|\le
\frac{2r}{R-r}(M-\Re g_0).
\tag{3.4}
\]

One can increase \(M\) slightly if necessary. Take \(r=3h/H\), so \(r/R=3/4\). Formula (3.4) gives \(|g(z)|\ll\log(2H)\). At the same ordinate \(t\), every real part from \(1-h/H\) to \(1+2h/H\) lies in this smaller disk. Therefore \(|1/L(z)|\ll(2H)^K\) there. To its right, the absolutely convergent reciprocal Euler product gives
\(|1/L(z)|\le\zeta(\sigma)\ll H\), covering the remaining real parts up to 2.

For the principal primitive factor, apply the same argument to

\[
Z(s)=\frac{s-1}{s+1}\zeta(s).
\tag{3.5}
\]

It is holomorphic and nonzero on the disks, including at 1. Its magnitude is \(O(H)\): when \(|t|\le1\), use (2.4) of *Siegel's theorem* after multiplying by \((s-1)/(s+1)\); when \(|t|>1\), truncate

\[
\zeta(s)=\sum_{n\le N}n^{-s}
+\frac{N^{1-s}}{s-1}
-s\int_N^\infty\{u\}u^{-s-1}\,du
\]

and use the same bounds as above. At \(s_0\), the logarithm of \((s_0-1)/(s_0+1)\) has magnitude \(O(\log(2H))\): its modulus lies between a fixed multiple of \(1/H\) and 1, and its argument is bounded. Thus the logarithm bound applies to \(Z\). Since
\(1/\zeta=((s-1)/(s+1))/Z\)
and the prefactor is bounded for \(\sigma\ge1/2\), the conclusion follows for \(1/\zeta\).

Finally restore the extra Euler factors for an imprimitive character:

\[
\frac1{L(s,\chi)}
=\frac1{L(s,\chi^*)}
\prod_{p\mid q,\ p\nmid d}(1-\chi^*(p)p^{-s})^{-1}.
\]

For \(\sigma\ge1/2\), each factor is at most
\((1-p^{-1/2})^{-1}\le p^2\) in magnitude. Their product is at most \((\prod_{p\mid q}p)^2\le q^2\), proving (3.3). \(\square\)

The polynomial in \(H\) matters. A bound of size \(T^K\) would spoil the horizontal Perron integrals and would not prove the asserted exponential cancellation.

## 4. Siegel–Walfisz for the Möbius function

**Theorem 4.1.** There is an absolute \(c>0\) such that, for every \(A>0\), uniformly for \(q\le(\log x)^A\) and all residue classes \(b\),

\[
\sum_{n\le x,\ n\equiv b\pmod q}\mu(n)
=O_A(xe^{-c\sqrt{\log x}}).
\tag{4.1}
\]

The implied constant is ineffective. In particular this holds for every reduced residue class.

**Proof.** First prove, for every character modulo \(q\),

\[
M(x,\chi):=\sum_{n\le x}\mu(n)\chi(n)
\ll_A xe^{-c\sqrt{\log x}}.
\tag{4.2}
\]

Put \(v=\log x\), choose an absolute small \(\kappa>0\), and let \(T=\exp(\kappa\sqrt v)\). The classical zero-free region excludes every nonreal zero and every nonexceptional real zero from a box of the form (3.2), after choosing \(h\) sufficiently small. The only possible remaining zero has distance

\[
1-\beta_1\ge c(1/(4A))v^{-1/4}.
\]

For large \(x\), ineffectively in \(A\), this exceeds \(8h/H\), since
\(H=\log(q(T+3))\asymp\kappa\sqrt v\).
Thus the box is entirely zero-free and Lemma 3.1 applies. The principal zeta factor has no exceptional real zero.

Use the truncated Perron kernel from the explicit-formula lesson, with coefficients \(\mu(n)\chi(n)\) of magnitude at most 1. Taking \(x\) halfway between integers avoids an endpoint term. On \(c_x=1+1/\log x\), absolute summation of the kernel error gives

\[
M(x,\chi)=\frac1{2\pi i}\int_{c_x-iT}^{c_x+iT}
\frac{x^s}{sL(s,\chi)}\,ds
+O\left(\frac{x\log(2x)}T\right).
\tag{4.3}
\]

For clarity, the error bound follows by separating \(x/2<n<2x\), where
\(|\log(x/n)|\gg|x-n|/x\) and the half-integer distances have a harmonic sum \(O(\log(2x))\), from the remaining integers, where \(|\log(x/n)|\) is bounded below and \(\sum n^{-c_x}\ll\log(2x)\). The error kernel is \(O((x/n)^{c_x}\min(1,(T|\log(x/n)|)^{-1}))\). This proves the bound in both ranges.

Shift to \(\sigma_0=1-h/H\). The integrand is holomorphic throughout the rectangle: there are no \(L\)-zeros, \(s=0\) is outside it, and for the principal character the pole of \(L\) gives a zero of its reciprocal. Therefore there is no residue and no main term.

By Lemma 3.1 the new vertical side is

\[
O\left(x^{1-h/H}q^2(2H)^K\log(T+2)\right);
\tag{4.4}
\]

the factor \(\log(T+2)\) bounds \(\int_{-T}^T|\sigma_0+it|^{-1}dt\).
The two horizontal sides are

\[
O\left(\frac{xq^2(2H)^K}{T}\right),
\tag{4.5}
\]

since \(x^{c_x}=ex\) and their lengths are bounded.

For sufficiently large \(x\), \(H\le2\kappa\sqrt v\), while \(q^2(2H)^K\log(T+2)\) is at most a fixed power of \(v\), with exponent depending on \(A\). Choose, for example, \(\kappa\) small enough that \(h/(2\kappa)\ge2\kappa\). Then (4.3)–(4.5) are \(O_A(xe^{-\kappa\sqrt v/2})\), after absorbing that power of \(v\). Extending below the threshold by the trivial bound \(|M(x,\chi)|\le x\) gives (4.2).

For arbitrary real \(x\), apply the half-integer argument at \(X=\lfloor x\rfloor+1/2\), which has the same integer summands. Here \(\log X\sim\log x\) and \(q\le2^A(\log X)^A\) for large \(x\); the proof and its thresholds also apply with this fixed factor in the modulus hypothesis. Decrease \(c\) and cover the bounded initial interval. This justifies (4.2) at every \(x\ge3\).

For \((b,q)=1\), orthogonality and averaging (4.2) prove (4.1) without a factor \(\varphi(q)\).

To cover a nonreduced class, put \(g=(b,q)\). If \(g\) is not squarefree, every summand has \(\mu(n)=0\). Otherwise write \(n=gk\), \(q=gr\), \(b=gb'\). Then

\[
\mu(gk)=\mu(g)\mu(k)\mathbf1_{(k,g)=1},\qquad
k\equiv b'\pmod r,\quad (b',r)=1.
\tag{4.6}
\]

The allowed \(k\)'s form at most \(g\) reduced residue classes modulo \(R=\operatorname{lcm}(r,\operatorname{rad}g)\), with \(R\mid q\). Apply the proved reduced-class theorem at \(x/g\), with parameter \(2A\): for large \(x\), \(R\le(\log(x/g))^{2A}\) since \(g\le q\le(\log x)^A\). Sum the at most \(g\) bounds. Their factors \(x/g\) cancel that number, and \(\log(x/g)\ge(\log x)/2\) for large \(x\), giving (4.1) after another absolute decrease of \(c\). Initial bounded \(x\) is absorbed as before. \(\square\)

## 5. Mertens sums in progressions

**Corollary 5.1.** For each reduced class there is a real constant \(B(q,b)\) such that, for every fixed \(A>0\),

\[
\sum_{p\le x,\ p\equiv b\pmod q}\frac1p
=\frac{\log\log x}{\varphi(q)}+B(q,b)
+O_A(e^{-c\sqrt{\log x}})
\tag{5.1}
\]

uniformly for \(q\le(\log x)^A\). The error constant is ineffective; the constants \(B(q,b)\) are allowed to depend on the class.

**Proof.** Put \(R(u)=\pi(u;q,b)-\operatorname{li}(u)/\varphi(q)\). Partial summation gives

\[
\sum_{p\le x,\ p\equiv b\pmod q}\frac1p
=\frac{\pi(x;q,b)}x+\int_2^x\frac{\pi(u;q,b)}{u^2}\,du.
\]

For the \(\operatorname{li}\) part, the derivative identity
\((\operatorname{li}(u)/u)'=1/(u\log u)-\operatorname{li}(u)/u^2\)
makes this
\((\log\log x-\log\log2)/\varphi(q)\).
For fixed \(q\), Theorem 2.1 ensures that \(\int_2^\infty R(u)u^{-2}du\) converges absolutely. Thus define

\[
B(q,b)=-\frac{\log\log2}{\varphi(q)}
+\int_2^\infty\frac{R(u)}{u^2}\,du.
\tag{5.2}
\]

The remaining error is \(R(x)/x-\int_x^\infty R(u)u^{-2}du\). If \(q\le(\log x)^A\), the hypothesis remains valid at every \(u\ge x\), so its magnitude is bounded by

\[
O_A\left(\frac{e^{-c\sqrt{\log x}}}{\log x}
+\int_{\log x}^\infty \frac{e^{-c\sqrt v}}v\,dv\right)
\ll_A e^{-c\sqrt{\log x}}.
\]

For the integral use \(v=t^2\) and \(1/t\le1/\sqrt{\log x}\). This proves uniformity without applying the modulus bound at smaller arguments where it might fail. \(\square\)

The corresponding Mertens product is

\[
\prod_{p\le x,\ p\equiv b\pmod q}(1-1/p)^{-1}
=C(q,b)(\log x)^{1/\varphi(q)}
\left(1+O_A(e^{-c\sqrt{\log x}})\right)
\tag{5.3}
\]

for a positive \(C(q,b)\). Indeed its logarithm differs from the reciprocal-prime sum by the convergent series
\(\sum_{p\equiv b}\sum_{j\ge2}1/(jp^j)\);
its tail beyond \(x\) is \(O(1/x)\), uniformly in the class. Exponentiating (5.1) proves (5.3).

## 6. The size of the range and of the error

Siegel's conclusion is available for every *fixed* \(\varepsilon>0\), with an uncontrolled constant \(c(\varepsilon)\). At \(q\le(\log x)^A\) we can fix an exponent in advance and make
\((1-\beta_1)\log x\gg_A(\log x)^{3/4}\).

If instead \(q\le\exp((\log x)^\delta)\) for fixed \(\delta>0\), the lower bound furnished by a fixed exponent gives only

\[
c(\varepsilon)\log x\,
\exp(-\varepsilon(\log x)^\delta)\longrightarrow0.
\tag{6.1}
\]

It supplies no useful uniform decay for the exceptional term at that endpoint. Taking an exponent that changes with \(x\) would introduce the uncontrolled varying constant \(c(\varepsilon(x))\), so is not a repair. This is a limitation of this method of removing the term; it does not contradict the much wider effective theorem that keeps the term visible.

At \(x=10^{100}\),

\[
\log x=230.2585093,\quad
\sqrt{\log x}=15.17427129,\quad
\log_{10}(\log x)=2.362215689.
\tag{6.2}
\]

Thus the formal scale \(xe^{-c\sqrt{\log x}}\) has decimal logarithm \(100-6.590102290c\). At the endpoint \(q=(\log x)^A\), the relative \(\psi\) error bound \(C_Aq e^{-c\sqrt{\log x}}\) has decimal logarithm at most

\[
\log_{10}C_A+2.362215689A-6.590102290c.
\tag{6.3}
\]

| \(A\) | Endpoint modulus scale | Relative error bound, decimal logarithm |
|---:|---:|---|
| 1 | \(2.3026\cdot10^2\) | \(\log_{10}C_A+2.3622-6.5901c\) |
| 2 | \(5.3019\cdot10^4\) | \(\log_{10}C_A+4.7244-6.5901c\) |
| 3 | \(1.2208\cdot10^7\) | \(\log_{10}C_A+7.0866-6.5901c\) |

These are recomputed scales, not numerical error guarantees: the proof does not give a usable value for \(C_A\). Substituting \(C_A=1\) or an arbitrary \(c\) would not turn the table into a certified accuracy statement.

Under GRH the explicit formula gives the effective estimate

\[
\psi(x;q,b)=\frac{x}{\varphi(q)}
+O(\sqrt x\log^2(qx)).
\tag{6.4}
\]

For \(q\le x\), partial summation also gives

\[
\pi(x;q,b)=\frac{\operatorname{li}(x)}{\varphi(q)}
+O(\sqrt x\log x).
\tag{6.5}
\]

To check (6.5), remove higher powers and use (2.4) split at \(\sqrt x\). The lower terms are \(O(\sqrt x)\). On the upper interval \(\log(qu)\le2\log x\), so the integral of the \(\theta\) error is \(O(\sqrt x)\) and its endpoint is \(O(\sqrt x\log x)\).

For any fixed \(\delta>0\), if

\[
q\le\frac{\sqrt x}{(\log x)^{2+\delta}},
\tag{6.6}
\]

the relative errors in both (6.4) and (6.5) tend to zero: each is at most \(O((\log x)^{-\delta})\), using \(\varphi(q)\le q\). The coarser bound \(O(\sqrt x\log^2x)\) for \(\pi\) is true but by itself would lose a logarithm in this comparison.

## 7. A stronger error from the wider zero-free region

The wider Vinogradov–Korobov region assigned to *Zero-free regions and the exceptional zero* has denominator

\[
\log q+(\log\tau)^{2/3}(\log\log\tau)^{1/3},
\qquad \tau=|t|+4.
\tag{7.1}
\]

Its proof remains planned within that lesson. Given this precise region, the explicit formula proves, for \(q\le(\log x)^A\),

\[
\psi(x;q,b)=\frac{x}{\varphi(q)}
+O_A\left(x\exp\left(-c
\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}\right)\right),
\tag{7.2}
\]

and the same error, with an additional \(1/\log x\), for \(\pi\). For (7.2) take \(x\) sufficiently large; all constants may again be extended to the initial range. The wider-region proof is an exact internal prerequisite of this refinement, rather than a consequence of the classical region alone.

**Derivation from (7.1).** Put
\(W=(\log x)^{3/5}(\log\log x)^{-1/5}\)
and take \(T=\exp(\kappa W)\). For \(|t|\le T\), the denominator in (7.1) is
\(O_A((\log x)^{2/5}(\log\log x)^{1/5})\):
its conductor part \(A\log\log x\) is smaller. Thus every nonexceptional zero has
\((1-\beta)\log x\gg W\).
The stable explicit formula and the local reciprocal-ordinate bounds from the zero-count lesson make their total \(O_A(xe^{-cW})\), after absorbing logarithmic factors. Low zeros near 0 are treated by
\((x^\rho-1)/\rho=\int_1^x u^{\rho-1}du\);
their contribution is \(O(\sqrt x\log x\log(2q))\). The truncation error \(O(x\log^2(qx)/T)\) has the same required scale.

For the remaining real zero, Siegel with exponent \(1/(5A)\) gives \((1-\beta_1)\log x\gg_A(\log x)^{4/5}\), which eventually dominates \(W\). Average characters as before. The passage to \(\pi\) uses the upper-interval modulus check with parameter \(2A\); on that interval \(W(u)\gg W(x)\), giving the stated error after an absolute decrease of \(c\). This proves the refinement from the exact planned input. \(\square\)

The Möbius theorem and the classical Theorem 2.1 need only the already written classical region, not this sharper prerequisite.

## 8. Exercises

1. **Easy.** Derive the \(\theta\) and \(\pi\) assertions from the \(\psi\) assertion. Check the modulus condition inside the integration interval.
2. **Medium.** Explain why Siegel's lower distance bound alone does not remove the exceptional term uniformly up to \(q=\exp((\log x)^\delta)\).
3. **Medium.** Under GRH, prove the relative asymptotic throughout (6.6) for both \(\psi\) and \(\pi\). Keep the appropriate logarithm in each error.
4. **Hard.** Prove the Möbius theorem, including a bound for \(1/L\) on the horizontal sides of the Perron rectangle.

## 9. Solutions

**1.** The difference \(\psi-\theta\) is \(O(\sqrt x\log^2x)\), absorbed by the exponential error, so (2.2) follows. Apply the exact identity (2.4). At \(u\ge\sqrt x\), \(q\le(\log x)^A\le(\log u)^{2A}\) for \(\log x\ge4\), permitting the theorem with parameter \(2A\). The lower range is \(O(\sqrt x)\). The endpoint upper error is \(O_A(xe^{-c\sqrt{\log x}}/\log x)\), and the upper integral at most \(O_A(xe^{-c\sqrt{\log x}/\sqrt2}/\log^2x)\). Decrease the absolute constant to obtain (2.3). Using the original endpoint range at every smaller \(u\) without this check would be unjustified.

**2.** For fixed \(\varepsilon>0\), the available lower bound for \((1-\beta_1)\log x\) at that endpoint is exactly the scale in (6.1), which tends to zero. It cannot imply a growing exponent such as \(c\sqrt{\log x}\). Allowing \(\varepsilon\) to decrease with \(x\) leaves an uncontrolled changing constant and does not justify uniform decay. This proves a limitation of the given bound, without asserting that an exceptional zero actually exists or that no other method can enlarge the range.

**3.** GRH gives \(O(\sqrt x\log^2(qx))\) for \(\psi\), hence \(O(\sqrt x\log^2x)\) for \(q\le x\). Divide by \(x/\varphi(q)\) and use (6.6) to get \(O((\log x)^{-\delta})\). For \(\pi\), partial summation as in (6.5) gives \(O(\sqrt x\log x)\); divide by \(\operatorname{li}(x)/\varphi(q)\sim x/(\varphi(q)\log x)\), producing the same relative bound. The error for \(\pi\) is also bounded by \(O(\sqrt x\log^2x)\), but that weaker form alone would not prove this relative range for every \(\delta>0\).

**4.** Use (3.1), and put \(T=e^{\kappa\sqrt{\log x}}\), \(H=\log(q(T+3))\). The classical region excludes every zero in (3.2) except a possible real one; Siegel with exponent \(1/(4A)\) makes its distance \(\gg_A(\log x)^{-1/4}\), larger than \(8h/H\) beyond an ineffective threshold. Lemma 3.1 follows from the bounded logarithm on overlapping disks, not from a crude power of \(T\); it gives \(q^2(2H)^K\) uniformly on all three new sides.

The truncated Perron error is \(O(x\log(2x)/T)\) at half-integers. Shift the rectangle to \(1-h/H\) with no residue. The new sides have the bounds (4.4) and (4.5). Since \(q^2(2H)^K\log(T+2)\) is only a power of \(\log x\), choose \(\kappa\) so \(h/(2\kappa)\ge2\kappa\) and absorb this power into half the exponential decay. Thus \(M(x,\chi)\ll_A xe^{-c\sqrt{\log x}}\). Moving to the half-integer with the same integer summands proves it for general \(x\). Character orthogonality proves the reduced-class theorem; (4.6) and the at most \(g\) unit lifts prove its extension to all residue classes. The threshold, and therefore the extended implied constant, is ineffective.

## References

The theorem goes back to A. Walfisz's 1936 work. D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorem 12.1 and the discussion after Theorem 12.10, specifies the absolute exponential constant and the ineffective uniformity; Exercise 12.1 gives the Möbius target. Section 7 gives a stronger error scale. Its exact wider-region input remains planned in the preceding zero-free-region lesson. The classical prime and Möbius proofs, the reciprocal bound, both partial-summation range checks, and the solutions are supplied here.
