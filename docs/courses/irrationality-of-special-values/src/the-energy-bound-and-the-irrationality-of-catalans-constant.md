# The energy bound and the irrationality of Catalan's constant

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson finishes the proof that Catalan's constant \(G\) is irrational. The previous lesson, [The real place: integral formula and two bounds](the-real-place-integral-formula-and-two-bounds.md), reduced an upper bound for \(\log|\Delta_N|\) to the supremum of an explicit function of \(2n\) points. That function is an "energy": a sum of logarithmic interactions between the points and of one-point potentials. Expanding the logarithms in Chebyshev series turns the interactions into negative sums of squares, up to the diagonal terms; completing the squares with freely chosen trial coefficients bounds the energy by a constant plus the suprema of two functions of one variable. A finite, exact certificate bounds these suprema. The result,

\[
\limsup_{N\to\infty}\Bigl(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\Bigr)\le-2.290939875,
\]

contradicts the arithmetic lower bound \(-2.29084\) of [Denominators at the odd primes](denominators-at-the-odd-primes.md) along the nonvanishing sequence of [Nonvanishing at prime scales](nonvanishing-at-prime-scales.md), if \(G\) were rational.

We use the notation of the previous lesson: \(\alpha=a/n=\frac{11}{48}\), \(\beta=b/n=\frac7{48}\), \(\gamma=g/n=q/n=\frac4{48}\), \(\eta=h/n=\frac2{48}\), the majorants \(\mathcal I_{\kappa,n}\) and the case sets \(\Omega_\kappa\). A basic reference is [OpenAI-Catalan]; the Chebyshev expansion of the logarithmic kernel is due to Haagerup, see [Garoufalidis–Popescu].

## 1. The energy

For a function \(F\) of one variable write \(\langle F(x)\rangle=\frac1n\sum_iF(x_i)\), and similarly for the \(s_j\). In a double average, \(\langle K(x,x')\rangle\) sums over all ordered pairs \((i,j)\) and divides by \(n^2\), while \(\langle K(x,x')\rangle_{\ne}\) omits the pairs \(i=j\). Put

\[
W_\kappa(x)=(\alpha+2\gamma)\log|x|+2\eta\log(1-x)-\Bigl(\frac\kappa2+\alpha+\eta+\gamma\Bigr)\log(1+x^2),\qquad
W_s(s)=\beta\log s+\gamma\log(1-s),
\]

and \(D(x)=2\gamma-2x^2/(1+x^2)\).

**Lemma 1.1** (the energy identity). With \(t_i=2x_i/(1+x_i^2)\),

\[
\begin{aligned}
\frac{\log\mathcal I_{\kappa,n}}{n^2}-\frac12\log2={}&c_{\kappa,n}\log2+\Bigl\langle W_\kappa(x)+\frac{\kappa+2}{2n}\log(1+x^2)\Bigr\rangle+\langle W_s(s)\rangle\\
&+\frac\kappa2\langle\log|x-x'|\rangle_{\ne}+\frac12\langle\log(1-xx')\rangle_{\ne}+\langle\log|s-s'|\rangle_{\ne}-\langle\log(1-2xs+x^2)\rangle,
\end{aligned}
\]

where \(c_{\kappa,n}=\frac Cn+\frac{\kappa-2}2-\frac{\kappa+1}{2n}\).

**Proof.** Substitute

\[
|t-t'|=\frac{2|x-x'|(1-xx')}{(1+x^2)(1+x'^2)},\qquad 1-ts=\frac{1-2xs+x^2}{1+x^2},\qquad 1-t=\frac{(1-x)^2}{1+x^2},\qquad|t|=\frac{2|x|}{1+x^2}
\]

into the definitions, use \(\sum_{i<j}=\frac12\sum_{i\ne j}\), and \(\mathcal V(1/x)=\mathcal V(x)\prod|x_i|^{-(n-1)}\) in case \(\kappa=2\). The total exponent of \(|x_i|\) is \((C-1)+g-(n-1)=a+2g\) in both cases; collecting the powers of \(1+x_i^2\), of \(1-x_i\) and of \(2\) gives the stated coefficients. \(\square\)

The correction \(\frac{\kappa+2}{2n}\log(1+x^2)\) is at most \(2\log2/n\).

## 2. Chebyshev expansions of three kernels

**Lemma 2.1.** For \(u=\cos\theta\), \(u'=\cos\theta'\) and \(0\le r<1\), put

\[
L_r(u,u')=-\log2+\log|1-re^{i(\theta+\theta')}|+\log|1-re^{i(\theta-\theta')}|.
\]

Then \(L_r(u,u')=-\log2-2\sum_{k\ge1}r^kT_k(u)T_k(u')/k\), and \(L_r(u,u')\to\log|u-u'|\) as \(r\uparrow1\) when \(u\ne u'\). Moreover, for real \(|z|,|z'|<1\) and \(s\in[-1,1]\),

\[
\log(1-zz')=-\sum_{k\ge1}\frac{(zz')^k}k,\qquad-\log(1-2zs+z^2)=2\sum_{k\ge1}\frac{z^kT_k(s)}k=-\log|1-ze^{i\arccos s}|^2.
\]

**Proof.** \(\log|1-re^{i\phi}|=-\sum_kr^k\cos(k\phi)/k\), and \(\cos k(\theta+\theta')+\cos k(\theta-\theta')=2\cos k\theta\cos k\theta'=2T_k(u)T_k(u')\). At \(r=1\) the product of the two chords is \(|2\sin\frac{\theta+\theta'}2|\cdot|2\sin\frac{\theta-\theta'}2|=2|u-u'|\). The other identities are the power series of \(\log(1-y)\) with \(y=zz'\), and with \(y=ze^{\pm i\theta}\) for the last one. \(\square\)

## 3. Damping, squares and the energy bound

The series of Lemma 2.1 cannot be used at the diagonal \(x=x'\) or at the endpoints. We damp them, all appearances of the same moment by the same factor, so that the squares still complete.

Fix \(0<\varepsilon<\frac18\) and put \(\tau=1-\varepsilon\), \(\rho(x)=1-\varepsilon(1-x)\) and \(\sigma(s)=1-\varepsilon\sqrt{1-s}\), all in \([1-2\varepsilon,1]\). Replace

- \(\log|x-x'|\) by \(L_{\tau^2}(x,x')\), and \(\log|s-s'|\) by \(L_{\sigma(s)\sigma(s')}(s,s')\);
- \(\log(1-xx')\) by \(\log\bigl(1-\rho(x)\rho(x')xx'\bigr)\);
- \(-\log|1-xe^{i\theta}|^2\) (with \(s=\cos\theta\)) by \(-\log|1-\rho(x)\sigma(s)xe^{i\theta}|^2\).

**Lemma 3.1.** Each original kernel is at most its replacement plus \(6\varepsilon\), with an absolute bound, for every configuration.

**Proof.** For \(|\zeta|=1\) and \(0<r\le1\), \(|1-r\zeta|^2-r|1-\zeta|^2=(1-r)^2\ge0\); so a cosine kernel exceeds its damped version by at most \(-\log r\le-2\log(1-\varepsilon)\le3\varepsilon\). For the power kernel with \(u=xx'\) and \(r=\rho(x)\rho(x')\): if \(u\ge0\), then \(\log(1-u)\le\log(1-ru)\); if \(u=-q<0\), then \(\log(1+q)-\log(1+rq)\le(1-r)q/(1+rq)\le1-r\le4\varepsilon\). For the cross kernel put \(a=1-x\), \(b=\sqrt{1-s}\), \(z=1-xe^{i\theta}\) and \(z_\varepsilon=1-\rho\sigma xe^{i\theta}\); then \(|z_\varepsilon-z|\le|x|(1-\rho\sigma)\le\varepsilon|x|(a+b)\). For \(x\le0\), \(|z|\ge\operatorname{Re}z\ge1\) (as \(\cos\theta=s>0\)) and \(|x|(a+b)\le3\); for \(0\le x\le\frac12\), \(|z|\ge\frac12\) and \(|x|(a+b)\le1\); for \(\frac12\le x<1\), \(|z|^2=a^2+2xb^2\ge a^2+b^2\) and \(|x|(a+b)\le\sqrt2|z|\). In all cases \(|z_\varepsilon-z|\le3\varepsilon|z|\), so \(-\log|z|^2\le-\log|z_\varepsilon|^2+2\log(1+3\varepsilon)\le-\log|z_\varepsilon|^2+6\varepsilon\). \(\square\)

For a real sequence \(u=(u_k)_{k\ge1}\) with \(|u_k|\le Kr^k\) for some \(K\) and \(r<1\), define

\[
\|u\|_*^2=\sum_k\frac{u_k^2}k,\qquad T(u,x)=\sum_k\frac{u_kT_k(x)}k,\qquad S(u,x)=\sum_k\frac{u_kx^k}k,
\]

uniformly convergent on \([-1,1]\).

**Proposition 3.2** (energy reduction). Let \(p,v\) be two such sequences, and \(\lambda=0\) if \(\kappa=2\), \(\lambda\ge0\) if \(\kappa=1\). Then

\[
\begin{aligned}
\limsup_{N\to\infty}\sup_{\Omega_\kappa}\Bigl(\frac{\log\mathcal I_{\kappa,n}}{n^2}-\frac12\log2\Bigr)\le{}&(-1+\alpha+\gamma)\log2+\kappa\|p\|_*^2+\frac12\|v\|_*^2\\
&+\sup_{-1\le x<1,\ x\ne0}\bigl\{W_\kappa(x)+\lambda D(x)-2\kappa T(p,x)-S(v,x)\bigr\}+\sup_{0<s<1}\bigl\{W_s(s)+2T(v,s)\bigr\}.
\end{aligned}
\]

**Proof.** *Squares.* Put \(A_k=\langle\tau^kT_k(x)\rangle\), \(B_k=\langle\rho(x)^kx^k\rangle\), \(C_k=\langle\sigma(s)^kT_k(s)\rangle\). For a fixed interior configuration all damped series converge absolutely, and averaging Lemma 2.1 over all pairs, diagonals included, gives

\[
\frac\kappa2\langle L_{\tau^2}(x,x')\rangle=-\frac\kappa2\log2-\kappa\sum_k\frac{A_k^2}k,
\]

\[
\frac12\langle\log(1-\rho\rho'xx')\rangle+\langle L_{\sigma\sigma'}(s,s')\rangle-\langle\log|1-\rho\sigma xe^{i\theta}|^2\rangle=-\log2-\frac12\sum_k\frac{(B_k-2C_k)^2}k.
\]

The same \(B_k\) and \(C_k\) appear in the pure and the cross terms, which is why the cross term completes the square.

*Diagonals.* The energy uses \(\langle\cdot\rangle_{\ne}\), which differs from the full average by \(-\frac1n\) times the average of the diagonal values. A damped cosine diagonal is at least \(-\log2+2\log(1-r)\), a constant depending on \(\varepsilon\). For the power diagonal, \(1-\rho^2x^2\ge1-x\) for \(x\ge0\) and \(\ge1-(1-\varepsilon)^2\ge\varepsilon\) for \(x\le0\). For the \(s\) diagonal, \(1-\sigma^2\ge\varepsilon\sqrt{1-s}\). Hence the omitted diagonals cost at most \(O_\varepsilon(1/n)-\frac1{2n}\langle\log(1-x)\rangle-\frac1n\langle\log(1-s)\rangle\).

*Completing squares.* The inequality \(-a^2\le b^2-2ab\) with \(b=p_k\), respectively \(b=v_k\), gives

\[
-\kappa\sum_k\frac{A_k^2}k\le\kappa\|p\|_*^2-2\kappa\langle T_\varepsilon(p,x)\rangle,\qquad
-\frac12\sum_k\frac{(B_k-2C_k)^2}k\le\frac12\|v\|_*^2-\langle S_\varepsilon(v,x)\rangle+2\langle T_\varepsilon(v,s)\rangle,
\]

where \(T_\varepsilon(p,x)\), \(S_\varepsilon(v,x)\) and \(T_\varepsilon(v,s)\) are the series with the extra factors \(\tau^k\), \(\rho(x)^k\) and \(\sigma(s)^k\).

*The multiplier.* In case \(\kappa=1\), (3.1) of the previous lesson fails: \(\sum_i(1-x_i^2)/(1+x_i^2)>n-1-2g\), that is \(\langle D(x)\rangle>-1/n\). So adding \(\lambda\langle D(x)\rangle\) with \(\lambda\ge0\) costs at most \(\lambda/n\).

*Assembly.* By Lemma 1.1 and the steps above, the quantity on the left, for a configuration in \(\Omega_\kappa\), is at most \(\bigl(-1+\alpha+\gamma-\frac{\kappa+1}{2n}\bigr)\log2+\kappa\|p\|_*^2+\frac12\|v\|_*^2+\langle X_{n,\varepsilon}(x)\rangle+\langle Y_{n,\varepsilon}(s)\rangle+O(\varepsilon)+O_\varepsilon(1/n)\), where

\[
X_{n,\varepsilon}(x)=W_\kappa(x)-\frac1{2n}\log(1-x)+\lambda D(x)-2\kappa T_\varepsilon(p,x)-S_\varepsilon(v,x),\qquad
Y_{n,\varepsilon}(s)=W_s(s)-\frac1n\log(1-s)+2T_\varepsilon(v,s);
\]

here \(C/n=1+\alpha+\gamma\) was used for the constant. Averages are at most suprema. Since \(1-(1-d)^k\le kd\), we have \(|T_\varepsilon(p,x)-T(p,x)|\le\varepsilon\sum_k|p_k|\), \(|S_\varepsilon(v,x)-S(v,x)|\le2\varepsilon\sum_k|v_k|\) and \(|T_\varepsilon(v,s)-T(v,s)|\le\varepsilon\sum_k|v_k|\), uniformly. The coefficients of \(\log|x|\), \(\log s\) are fixed, and those of \(\log(1-x)\), \(\log(1-s)\) are at least \(\frac1{24}\) for \(n\ge24\); so both functions tend to \(-\infty\) at the singular endpoints uniformly in \(n\ge24\) and small \(\varepsilon\), while their values at \(x=-\frac12\), \(s=\frac12\) are bounded below uniformly. Their suprema are therefore attained in compact sets independent of \(n\) and \(\varepsilon\), on which the functions converge uniformly as \(n\to\infty\) (with \(\varepsilon\) fixed), and then as \(\varepsilon\to0\). Taking the limits in this order proves the proposition. \(\square\)

Together with Proposition 6.1 of the previous lesson, the maximum over \(\kappa\in\{1,2\}\) of the right sides bounds \(\limsup_N\bigl(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\bigr)\).

## 4. The certificate

**Trial sequences.** Each trial sequence has the form \(u_k=l_k+\sum_zr_zz^k\), with finitely many \(l_k\) (\(l_k=0\) for \(k>d\)) and finitely many bases \(z\) of modulus less than \(1\). All integers below are to be multiplied by \(10^{-8}\).

For \(\kappa=2\): \(d=10\), \(\lambda=0\), and

- \(p\): \(l_1,\dots,l_{10}=45559127,\ -50750856,\ -6578767,\ 13970217,\ 4786184,\ -4292433,\ -576704,\ 1311615,\ 671564,\ -346453\);
- \(v\): \(l_1,\dots,l_{10}=-23910158,\ 21152432,\ -2885110,\ -11558199,\ 6485289,\ 1456821,\ -1912176,\ -2263524,\ 2742210,\ -1162454\).

For \(\kappa=1\): \(d=8\), \(\lambda=2.47405979\), no exponential terms, and

- \(p\): \(11913521,\ -79993701,\ -21956443,\ 37903579,\ 10744022,\ -2073193,\ 570246,\ -24939103\);
- \(v\): \(-89913025,\ 52874280,\ 45168341,\ -30708629,\ -19269841,\ 33922112,\ 9819141,\ -16992389\).

The exponential terms for \(\kappa=2\) are listed as a base \(z\) with a coefficient \(a\) (real base, term \(az^k\)) or a pair \((a,b)\) (non-real base, term \(a\operatorname{Re}z^k+b\operatorname{Im}z^k\), that is \(r_z=(a-ib)/2\) together with the conjugate base):

| sequence | base | coefficient(s) |
|---|---|---|
| \(p\) | \(0.85\) | \(-9338452\) |
| \(p\) | \(0.94\) | \(-2141509\) |
| \(p\) | \(0.7i\) | \(-66277922,\ -31907569\) |
| \(p\) | \(0.85i\) | \(-1231651,\ 6002645\) |
| \(p\) | \(0.092+0.92i\) | \(-3225918,\ 8928234\) |
| \(p\) | \(-0.092+0.92i\) | \(-2105536,\ -9091287\) |
| \(v\) | \(-0.8\) | \(15199211\) |
| \(v\) | \(-0.96\) | \(4451662\) |
| \(v\) | \(0.88\) | \(2545398\) |
| \(v\) | \(0.95\) | \(-4932634\) |
| \(v\) | \(0.984\) | \(11618157\) |
| \(v\) | \(0.78i\) | \(27238714,\ -38447936\) |
| \(v\) | \(0.9i\) | \(-31341084,\ -30188786\) |
| \(v\) | \(0.955i\) | \(-6693542,\ 11912254\) |
| \(v\) | \(0.984i\) | \(2055213,\ -21715849\) |

Counting conjugates, \(p\) has \(10\) and \(v\) has \(13\) bases, of moduli at most \(0.94\) and \(0.984\); all \(|l_k|\) and \(|r_z|\) are below \(1\). The series of Section 3 become finite formulas with principal logarithms, all real by conjugation:

\[
\|u\|_*^2=\sum_{k\le d}\frac{l_k^2+2l_k\sum_zr_zz^k}k-\sum_{z,z'}r_zr_{z'}\operatorname{Log}(1-zz'),\quad
T(u,x)=\sum_{k\le d}\frac{l_kT_k(x)}k-\frac12\sum_zr_z\operatorname{Log}(1-2xz+z^2),\quad
S(u,x)=\sum_{k\le d}\frac{l_kx^k}k-\sum_zr_z\operatorname{Log}(1-xz).
\]

For \(x=\cos\theta\), \(1-2xz+z^2=(1-ze^{i\theta})(1-ze^{-i\theta})\) with both factors in the right half-plane, so the principal logarithm of the product is the sum of the logarithms.

**The two functions.** Put \(X_\kappa(x)=W_\kappa(x)+\lambda D(x)-2\kappa T(p,x)-S(v,x)\) on \([-1,1)\setminus\{0\}\) and \(Y_\kappa(x)=\beta\log x+\gamma\log(1-x)+2T(v,x)\) on \((0,1)\). Their derivatives are

\[
X_\kappa'=\frac{\alpha+2\gamma}x-\frac{2\eta}{1-x}-(\kappa+2\alpha+2\eta+2\gamma)\frac x{1+x^2}-\frac{4\lambda x}{(1+x^2)^2}-2\kappa\,t_p(x)-h_v(x),\qquad Y_\kappa'=\frac\beta x-\frac\gamma{1-x}+2t_v(x),
\]

with \(t_u(x)=\sum_kl_kU_{k-1}(x)+\sum_zr_zz/(1-2xz+z^2)\) and \(h_u(x)=\sum_kl_kx^{k-1}+\sum_zr_zz/(1-xz)\). Multiplying by

\[
Q_X=x(1-x)(1+x^2)^{3-\kappa}\prod_{z\in p}(1-2xz+z^2)\prod_{z\in v}(1-xz),\qquad Q_Y=x(1-x)\prod_{z\in v}(1-2xz+z^2)
\]

gives polynomials \(A_X=Q_XX_\kappa'\) and \(A_Y=Q_YY_\kappa'\) with rational coefficients, of degrees \(36,24\) for \(\kappa=2\) and \(13,9\) for \(\kappa=1\). The factors \(1-xz\) and \(1-2xz+z^2\) do not vanish for real \(|x|\le1\) (their moduli are at least \(1-|z|\) and \((1-|z|)^2\)), conjugate factors have positive products, and so \(Q_X\) has the sign of \(x\) and \(Q_Y>0\) on the domains. The stationary points of \(X_\kappa\) and \(Y_\kappa\) are exactly the roots of \(A_X\), \(A_Y\) in the domains.

**Lemma 4.1** (Descartes' rule of signs). The number of positive roots of a nonzero real polynomial, counted with multiplicity, is at most the number of sign changes in its sequence of nonzero coefficients.

**Proof.** We may assume \(p(0)\ne0\). If \(p(r)=0\) with \(r>0\), write \(p=(t-r)q\); rescaling \(t\) we may take \(r=1\). With \(q=\sum_{h=0}^dq_ht^h\) and \(p=\sum p_ht^h\), the partial sums satisfy \(\sum_{j\le h}p_j=-q_h\) for \(h\le d\), and \(p_{d+1}=q_d\). Starting with \(p_0=-q_0\), at each sign change of the nonzero \(q_h\), between indices \(h_1<h_2\), the partial sums move from \(-q_{h_1}\) to \(-q_{h_2}\), so some \(p_j\) with \(h_1<j\le h_2\) has the sign of \(-q_{h_2}\). These choices form a subsequence of the \(p_j\) with as many sign changes as \(q\), ending with the sign of \(-q_d\); the last coefficient \(p_{d+1}=q_d\) adds one more. So \(p\) has more sign changes than \(q\), and induction on the number of positive roots proves the lemma. \(\square\)

To count roots of a polynomial \(A\) of degree \(d_0\) in an interval \((b,c)\), apply the lemma to \((1+t)^{d_0}A\bigl(\frac{b+ct}{1+t}\bigr)\); the substitution maps \(t>0\) bijectively and increasingly onto \((b,c)\) and preserves multiplicities.

**Proposition 4.2** (the root certificate). With the division points below, the numbers of sign changes on consecutive intervals are:

| case | function | division points | sign changes |
|---|---|---|---|
| \(\kappa=2\) | \(X\) | \(-1,0,1\) | \(9,\ 9\) |
| \(\kappa=2\) | \(Y\) | \(0,\frac14,\frac12,\frac34,1\) | \(5,\ 2,\ 2,\ 6\) |
| \(\kappa=1\) | \(X\) | \(-1,-\frac12,0,\frac12,1\) | \(1,\ 1,\ 2,\ 1\) |
| \(\kappa=1\) | \(Y\) | \(0,1\) | \(5\) |

For each integer \(m\) in the following lists, \(A\) changes sign between \(m\cdot10^{-10}\) and \((m+2)\cdot10^{-10}\); the brackets are disjoint, and their numbers in the intervals equal the sign changes above. Hence each bracket contains exactly one root, simple, and the open intervals contain no other roots.

- \(\kappa=2\), \(X\): \(-9601109148\), \(-8942317572\), \(-7608305633\), \(-6503394794\), \(-5185864065\), \(-4015634158\), \(-3108806646\), \(-2067921826\), \(-1589849496\), \(1531948062\), \(2072448179\), \(3208186484\), \(4381119427\), \(5851354199\), \(7269030693\), \(8390277402\), \(9332614564\), \(9709786219\).
- \(\kappa=2\), \(Y\): \(176402802\), \(330649406\), \(764952882\), \(1227250753\), \(2149465998\), \(3048189112\), \(4322699096\), \(5564757994\), \(6801929373\), \(8031988371\), \(8877037851\), \(9577761832\), \(9838463999\), \(9972727815\), \(9992037196\).
- \(\kappa=1\), \(X\): \(-9917299785\), \(-2259572153\), \(2543808026\), \(4437270259\), \(6348298970\).
- \(\kappa=1\), \(Y\): \(532669786\), \(2504239325\), \(5701738806\), \(7966939383\), \(9454490138\).

All these statements are finite computations with rational numbers.

**Values.** Logarithms and arguments of rational (complex) numbers are bounded by rational arithmetic: for \(y\in[1,2]\), \(\log y=2\sum_{j\ge0}\frac{q^{2j+1}}{2j+1}\) with \(q=\frac{y-1}{y+1}\le\frac13\), truncated after \(18\) terms with remainder at most \(2q^{37}/(37(1-q^2))\); a positive rational is first scaled by a power of \(2\). An argument is reduced by rotations through \(\pi/4\) to \(\arctan t\) with \(|t|\le\frac12\), using \(\frac\pi4=\arctan\frac12+\arctan\frac13\), and \(\arctan t\) is the alternating series truncated after \(24\) terms, with error at most \(|t|^{49}/49\). Each logarithm is thereby known to within \(10^{-15}\), far below what is needed. The resulting upper bounds, rounded upwards to twelve decimals, are:

\(\kappa=2\), \(X\) at the left ends of its brackets, in the order listed: \(-0.984034048775\), \(-0.984375363807\), \(-0.984034052640\), \(-0.984105522615\), \(-0.984034053414\), \(-0.984092061375\), \(-0.984034037901\), \(-0.984364031075\), \(-0.984034038450\), \(-0.984033385315\), \(-0.984776982913\), \(-0.984034026898\), \(-0.984264010107\), \(-0.984034029391\), \(-0.984245044505\), \(-0.984034016294\), \(-0.984567630027\), \(-0.984033926884\); at \(x=-1\): \(-0.986727371546\).

\(\kappa=2\), \(Y\) at the left ends: \(-1.608946411646\), \(-1.609949505120\), \(-1.608960295828\), \(-1.609094597854\), \(-1.608960426500\), \(-1.608992193672\), \(-1.608960428486\), \(-1.608979509517\), \(-1.608960430478\), \(-1.608990548812\), \(-1.608960429811\), \(-1.609055802895\), \(-1.608960412835\), \(-1.609694899071\), \(-1.608958123669\); at \(\frac14,\frac12,\frac34\): \(-1.608973617030\), \(-1.608971701898\), \(-1.608976908052\).

\(\kappa=1\), \(X\): \(-2.778491531574\), \(-1.324666731948\), \(-1.324655807046\), \(-1.352236629957\), \(-1.324666329425\); at \(-1,-\frac12,\frac12\): \(-2.775818077526\), \(-1.544057819905\), \(-1.347557680876\).

\(\kappa=1\), \(Y\): \(-1.428286151250\), \(-1.515602647362\), \(-1.428335732372\), \(-1.465686164672\), \(-1.428335358167\).

The same calculation gives \(\kappa\|p\|_*^2+\frac12\|v\|_*^2\le0.778415976284\) for \(\kappa=2\) and \(\le0.931985203901\) for \(\kappa=1\), and \(0.693146<\log2<0.693149\).

**From brackets to suprema.** Every bracket point has distance more than \(0.0007\) from \(0\) and \(1\) (the bracket nearest \(1\) ends at \(0.9992037198\)). There, using \(|U_{k-1}(x)|\le k\) on \([-1,1]\), the coefficient bounds, and \(|1-xz|\ge1-|z|\), \(|1-2xz+z^2|\ge(1-|z|)^2\), one gets \(|X_\kappa'|\le230+685+3+10+11924<120000\) and \(|Y_\kappa'|\le110+328+101563<120000\). By the mean value theorem, the value at the stationary point in a bracket exceeds the value at its left end by less than \(120000\cdot2\cdot10^{-10}=0.000024\). The suprema of \(X_\kappa\) and \(Y_\kappa\) are attained at stationary points or at the finite endpoint \(x=-1\), since the functions tend to \(-\infty\) at \(x\to0\), \(x\to1\) and \(s\to0\), \(s\to1\); and every stationary point lies in a bracket or is a division point, all of which are in the lists.

**Proposition 4.3** (the real upper bound).

\[
\limsup_{N\to\infty}\Bigl(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\Bigr)\le-2.290939875<-2.2909.
\]

**Proof.** By Proposition 3.2 with these trial sequences, and the bounds just obtained (rounded up to \(0.77844\), \(-0.98399\), \(-1.60890\) for \(\kappa=2\) and \(0.9321\), \(-1.3244\), \(-1.4280\) for \(\kappa=1\)), with \(-1+\alpha+\gamma=-\frac{11}{16}\) and \(\log2>0.693146\), the two cases give at most

\[
-\tfrac{11}{16}(0.693146)+0.77844-0.98399-1.60890+0.000048=-2.290939875,
\]

\[
-\tfrac{11}{16}(0.693146)+0.9321-1.3244-1.4280+0.000048=-2.296789875.
\]

The larger of the two is the claim. \(\square\)

## 5. Catalan's constant is irrational

**Theorem 5.1** (OpenAI, 2026). Catalan's constant \(G=\sum_{j\ge0}(-1)^j(2j+1)^{-2}\) is irrational.

**Proof.** Suppose \(G\) is rational. By Proposition 6.1 of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md), every \(\Delta_N\) is rational. By Proposition 1.1 of [Nonvanishing at prime scales](nonvanishing-at-prime-scales.md), \(\Delta_p\ne0\) for all sufficiently large primes \(p\). Along these primes, Proposition 6.1 of [Denominators at the odd primes](denominators-at-the-odd-primes.md) gives

\[
\liminf_{p\to\infty}\Bigl(\frac{\log|\Delta_p|}{(48p)^2}-\frac12\log2\Bigr)>-2.29084,
\]

while Proposition 4.3 gives an upper limit below \(-2.2909\). Since \(-2.29084>-2.2909\), this is a contradiction. \(\square\)

The proof gives qualitative irrationality only. The margin between the two estimates is about \(10^{-4}\); a bound for an irrationality measure would need more control of rational approximations.

**Where this leads.** By Agol's theorem, \(4G\) is the smallest volume of an orientable complete hyperbolic three-manifold of finite volume with exactly two cusps, attained by the complement of the Whitehead link [Agol]; this volume is therefore irrational. Volumes of arithmetic hyperbolic three-orbifolds defined over \(\mathbb Q(i)\) are rational multiples of \(G\) by the volume formula for quaternion orders, and so are irrational as well; for example, \(\operatorname{PSL}_2(\mathbb Z[i])\backslash\mathbb H^3\) has volume \(G/3\) [Voight, Example 39.1.16]. These consequences rest on the cited theorems, which this course does not prove.

## 6. Exercises

**Exercise 6.1 (easy).** Check that \(C/n=1+\alpha+\gamma\). Why is the coefficient of \(\langle\log|x-x'|\rangle_{\ne}\) in Lemma 1.1 equal to \(\kappa/2\)?

**Exercise 6.2 (easy).** Verify the arithmetic \(-\frac{11}{16}(0.693146)+0.77844-0.98399-1.60890+0.000048=-2.290939875\).

**Exercise 6.3 (medium).** Apply Lemma 4.1 to \(p(t)=t^3-3t^2+4\), which has the roots \(-1\) and \(2\) (double), and compare.

**Exercise 6.4 (medium).** Prove \(\sum_{k\ge1}T_k(x)z^k/k=-\frac12\log(1-2xz+z^2)\) for real \(|z|<1\) and \(|x|\le1\), by differentiating in \(z\).

**Exercise 6.5 (hard).** Explain why the damping factors for the power kernel and for the cross kernel must be the same function \(\rho(x)\) of \(x\), and the damping factors for the \(s\) cosine kernel and the cross kernel the same function \(\sigma(s)\).

## 7. Solutions

**6.1.** \(C=n+a+g\), so \(C/n=1+\alpha+\gamma\). In \(\mathcal I_{\kappa,n}\), \(\mathcal V(t)\) contributes \(\prod_{i<j}|x_i-x_j|\) once, and in case \(\kappa=2\) the factor \(\mathcal V(1/x)\) contributes it once more. Each \(\sum_{i<j}\log|x_i-x_j|\) equals \(\frac{n^2}2\langle\log|x-x'|\rangle_{\ne}\).

**6.2.** \(\frac{11}{16}\cdot0.693146=0.476537875\); then \(-0.476537875+0.77844=0.301902125\), minus \(0.98399\) gives \(-0.682087875\), minus \(1.60890\) gives \(-2.290987875\), plus \(0.000048\) gives \(-2.290939875\).

**6.3.** The coefficients \(1,-3,0,4\) have the nonzero signs \(+,-,+\): two changes, and \(p\) has two positive roots counted with multiplicity (the double root \(2\)). The bound is attained.

**6.4.** Differentiating \(-\frac12\log(1-2xz+z^2)\) in \(z\) gives \((x-z)/(1-2xz+z^2)\), while \(\sum_kT_k(x)z^{k-1}\) is the same rational function: with \(x=\cos\theta\), \(\sum_k\cos(k\theta)z^{k-1}=\operatorname{Re}\frac{e^{i\theta}}{1-ze^{i\theta}}=\frac{\cos\theta-z}{1-2z\cos\theta+z^2}\). Both sides vanish at \(z=0\).

**6.5.** The squares in the proof of Proposition 3.2 combine \(\langle\rho^kx^k\rangle\) from the power kernel with \(\langle\rho^kx^k\rangle\langle\sigma^kT_k(s)\rangle\) from the cross kernel, and \(\langle\sigma^kT_k(s)\rangle\) from the \(s\) kernel with the same factor in the cross kernel. Different damping factors would produce different moments, and the sum would no longer be a negative square, so the trial coefficients could not bound it.

## References

- [OpenAI-Catalan] OpenAI, Catalan's constant is irrational, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf
- [Garoufalidis–Popescu] S. Garoufalidis, I. Popescu, Analyticity of the planar limit of a matrix model, Annales Henri Poincaré 14 (2013), 499–565. https://arxiv.org/abs/1010.0927
- [Agol] I. Agol, The minimal volume orientable hyperbolic 2-cusped 3-manifolds, Proceedings of the American Mathematical Society 138 (2010), 3723–3732. https://arxiv.org/abs/0804.0043
- [Voight] J. Voight, Quaternion Algebras, Graduate Texts in Mathematics 288, Springer, 2021 (open access). https://link.springer.com/book/10.1007/978-3-030-56694-4
