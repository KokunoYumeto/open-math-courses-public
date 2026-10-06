# Elementary functions, angular coordinates and smooth cutoffs

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

This reading supplies the elementary functions used in the measure, Fourier and coordinate arguments. Its inputs are the field operations and ordered-real completeness, the [finite-dimensional product and chain rules](coordinate-inverses-and-integration.md#coordinate-differential-rules), the [compactness and scalar mean-value proof](hilbert-valued-integration.md#compact-scalar-calculus), and the [continuous scalar fundamental theorem](hilbert-valued-integration.md#continuous-primitives). Those scopes precede this reading; none uses exponential, logarithmic or trigonometric functions. The later polar and smooth-partition sections of the coordinate reading use the results proved here.

<a id="elementary-limits"></a>
## Limits and intermediate values

We first record the elementary limit arguments used below. The natural numbers are unbounded in the reals: if their supremum were $s$, some natural number would exceed $s-1$, and its successor would exceed $s$. Hence every real number has a unique integer part. For $0<q<1$, the binomial expansion gives $q^{-n}=(1+(q^{-1}-1))^n\ge 1+n(q^{-1}-1)$, so $q^n\to0$. For every fixed nonnegative integer $k$, the ratio of successive terms of $n^kq^n$ tends to $q$; choosing $q<r<1$ bounds the tail by a constant times $r^n$. In particular $n^kq^n\to0$, and its series converges. The ratio assertion follows by expanding $(1+1/n)^k$, a finite polynomial. The finite geometric identity and completeness show that a series whose absolute terms are bounded by $Cr^n$, $r<1$, converges, with tail at most $Cr^N/(1-r)$ from index $N$.

If continuous $f:[a,b]\to\mathbb R$ satisfies $f(a)<v<f(b)$, bisect the interval, retaining endpoints with values on the two sides of $v$, and stop if a midpoint has value $v$. Otherwise the nested intervals have lengths tending to zero and a common point by real completeness. Continuity there gives $f=v$. Replacing $f$ by $-f$ covers the reverse ordering. This proves the intermediate-value theorem used below. A strictly increasing continuous function consequently has a continuous inverse on its image: for a point $x$ in its domain, the values at $x-\delta$ and $x+\delta$ bracket its value by strict inequalities, so sufficiently close values have inverse within that interval. Use one-sided brackets at endpoints.

We will multiply absolutely convergent scalar series. If $\sum|a_j|=A$ and $\sum|b_k|=B$ are finite, the sum of $|a_jb_k|$ over a finite rectangle is bounded by $AB$. Outside the square $0\le j,k\le N$, all finite sums of absolute values are bounded by
\[
 B\sum_{j>N}|a_j|+A\sum_{k>N}|b_k|.
 \tag{EF1}
\]
This tends to zero. Thus the rectangular and diagonal finite sums have the same limit; a diagonal sum with $j+k\le 2N$ contains the square with $j,k\le N$. Passing to the limit in the finite rectangular product proves the usual product-by-diagonals identity, without any rearrangement assumption.

<a id="scalar-exponential"></a>
## The exponential and its derivative

For $z\in\mathbb C$, define
\[
 E(z)=\sum_{n=0}^{\infty}\frac{z^n}{n!}.
 \tag{EF2}
\]
Here $0!=1$ and $(n+1)!=(n+1)n!$. On every disk $|z|\le R$, the ratio of successive absolute majorants $R^n/n!$ is at most $1/2$ once $n+1\ge2R$. The preceding geometric tail estimate proves absolute and uniform convergence. It proves the same statement with an additional fixed polynomial in $n$ in the numerator. In particular, for any $R>0$ the series $\sum_{n\ge2}n^2R^{n-2}/n!$ is finite.

For distinct $z,w$ with $|z|,|w|\le R$, factor the difference of the two $n$th powers. For $n\ge2$ this gives
\[
 \begin{gathered}
 \left|\frac{z^n-w^n}{z-w}-nw^{n-1}\right|\\
 \le n^2R^{n-2}|z-w|.
 \end{gathered}
 \tag{EF3}
\]
Indeed, subtract $nw^{n-1}$ from $\sum_{j=0}^{n-1}z^{n-1-j}w^j$ and apply $|z^m-w^m|\le mR^{m-1}|z-w|$ to each term. Summing (EF3) after division by $n!$ proves complex differentiability with
\[
 E'(w)=\sum_{n\ge1}\frac{nw^{n-1}}{n!}=E(w).
 \tag{EF4}
\]
Consequently $E$ is smooth and every derivative equals $E$. Continuity can also be seen directly from the uniform series, since its partial sums are polynomials and its tails are uniformly small.

Apply (EF1) to the series at $z$ and $w$. The terms with total degree $n$ sum to $(z+w)^n/n!$: the binomial coefficients follow by induction from multiplying a polynomial by $z+w$. Thus
\[
 \begin{gathered}E(z+w)=E(z)E(w),\\ E(z)E(-z)=1.\end{gathered}
 \tag{EF5}
\]
Conjugating the absolutely convergent series gives $E(\bar z)=\overline{E(z)}$. For real $x$, $E(x)$ is real and $E(x)=E(x/2)^2>0$, the strict inequality following from its nonvanishing in (EF5). Its derivative is therefore positive, so the mean-value theorem makes it strictly increasing. For $x\ge0$, its nonnegative series gives $E(x)\ge1+x$. Hence $E(x)\to\infty$ as $x\to\infty$, and $E(-x)=1/E(x)\to0$. The intermediate-value theorem shows that $E:\mathbb R\to(0,\infty)$ is onto. We write $\exp z=e^z=E(z)$.

<a id="logarithm-and-real-powers"></a>
## Logarithm, real powers and Young's inequality

Define $\log:(0,\infty)\to\mathbb R$ to be the real inverse of $E$. It is continuous by the inverse argument above. If $x=E(t)$ and $x+h=E(t+k)$, then $k\to0$ with $h\to0$ and
\[
 \begin{gathered}\frac{\log(x+h)-\log x}{h}\\ =\frac{k}{E(t+k)-E(t)}\longrightarrow\frac1x.\end{gathered}
 \tag{EF6}
\]
The denominator divided by $k$ tends to the nonzero number $E(t)=x$. This proves the derivative and, by the reciprocal and chain rules, smoothness. Injectivity and (EF5) imply $\log(xy)=\log x+\log y$. In particular $\log1=0$, and its limits at zero and infinity are respectively $-\infty$ and $+\infty$, by the range and monotonicity of $E$.

For any real $a$ and $x>0$, set $x^a=E(a\log x)$. The addition law, chain rule and (EF6) give
\[
 \begin{gathered}
 x^{a+b}=x^ax^b,\\ (xy)^a=x^ay^a,\quad (x^a)^b=x^{ab},\\
 \frac{d}{dx}x^a=ax^{a-1}.
 \end{gathered}
 \tag{EF7}
\]
These definitions agree with positive integral powers and their reciprocals, and $x^{1/n}$ is the positive $n$th root because its $n$th power is $x$ and the positive integral power is strictly increasing. For $a>0$, define $0^a=0$; the logarithmic limit proves continuity at zero. If $a>1$, the right difference quotient there is $h^{a-1}\to0$. On $(0,\infty)$ all real powers are smooth. Positive powers are increasing, and $x^a\to\infty$ as $x\to\infty$ for $a>0$.

Let $1<p<\infty$ and $q=p/(p-1)$. For $b\ge0$, the function $u\mapsto u^p/p-bu$ on $[0,\infty)$ has derivative $u^{p-1}-b$ in the interior. If $b>0$, this derivative is negative before $u=b^{1/(p-1)}$ and positive after it; continuity at zero and the mean-value theorem give its global minimum there. Its value is $-b^q/q$. If $b=0$ its minimum is zero at zero. Thus for all $a,b\ge0$,
\[
 ab\le\frac{a^p}{p}+\frac{b^q}{q}.
 \tag{EF8}
\]
This supplies the real-exponent step in the full Hölder proof. Also, monotonicity gives $(a+b)^p\le2^p(a^p+b^p)$ for $p\ge1$, since $a+b\le2\max(a,b)$.

For later cutoff estimates, if $M\ge0$ is real, choose an integer $N>M$. The nonnegative exponential series gives $E(y)\ge y^N/N!$ for $y>0$. Therefore
\[
 0\le y^Me^{-y}\le N!y^{M-N}\longrightarrow0
 \quad (y\to\infty).
 \tag{EF9}
\]
The final limit follows from the already proved negative-power limit. No asymptotic expansion is required.

<a id="trigonometry-and-period"></a>
## Trigonometry and the period of the exponential

For real $t$, define
\[
 \begin{gathered}C(t)=\frac{E(it)+E(-it)}2,\\ S(t)=\frac{E(it)-E(-it)}{2i}.\end{gathered}
 \tag{EF10}
\]
Conjugation makes both real. They satisfy $C(0)=1$, $S(0)=0$, $C'=-S$, $S'=C$, and $C^2+S^2=1$, by (EF4)–(EF5). Also $C$ is even and $S$ odd. Multiplying $E(it)E(iu)$ and taking real and imaginary parts proves both addition formulas. In particular $|E(it)|=1$ and all derivatives of $C,S$ have absolute value at most one.

There is a first positive zero $c$ of $C$. Here is an existence proof. If there were no positive zero, continuity and $C(0)=1$ would imply $C>0$ on $[0,\infty)$. Then $S'=C$ would make $S$ strictly increasing, with $S(a)>0$ for any $a>0$. For $t>a$, the fundamental theorem would give $C(t)=C(a)-\int_a^tS(u)du\le C(a)-(t-a)S(a)$, contradicting positivity for large $t$. Thus the zero set is nonempty; continuity makes it closed and excludes a neighborhood of zero. Taking a sequence of zeros approaching its positive infimum shows that the infimum $c>0$ is itself a zero. The intermediate-value theorem gives $C>0$ on $[0,c)$, so $S$ increases from zero there and $S(c)=1$ by $C^2+S^2=1$. In that interval $C'=-S<0$ away from zero.

Define $\pi=2c$. The addition formulas now give
\[
 C(t+c)=-S(t),\qquad S(t+c)=C(t).
 \tag{EF11}
\]
Four successive shifts prove period $4c=2\pi$. On $[0,c]$, $S$ takes every value in $[0,1]$ exactly once and $C$ is the nonnegative square root of $1-S^2$. Thus $(C,S)$ parametrizes the first quadrant of the unit circle once. Formula (EF11) rotates this parametrization through the other three quadrants. Their interiors are disjoint and their endpoints are precisely the four axis points. Consequently it parametrizes the whole unit circle exactly once on $[0,2\pi)$, with the endpoint $2\pi$ repeating the initial point. Reduction by an integer multiple of $2\pi$ then proves
\[
 \begin{gathered}
 E(it)=1\quad\Longleftrightarrow\quad t\in2\pi\mathbb Z,\\
 E(z)=1\quad\Longleftrightarrow\quad z\in2\pi i\mathbb Z.
 \end{gathered}
 \tag{EF12}
\]
For the second line, write $z=x+it$. Equation (EF5) gives $|E(z)|=E(x)$, which is one exactly when $x=0$. We write $\cos t=C(t)$ and $\sin t=S(t)$. The unit-circle parametrization has speed one because $(C',S')=(-S,C)$ has norm one; its full length is $2\pi$. Thus the normalization agrees with the circumference definition of $\pi$.

<a id="arctangent-and-poisson-kernel"></a>
## Arctangent and the normalized Poisson kernel

On $(-c,c)$, $C$ is positive by evenness and the first-zero property. The quotient $T=S/C$ has derivative $1/C^2>0$. Its limits at the two endpoints are $-\infty$ and $+\infty$, since $S(\pm c)=\pm1$ and $C\to0$ through positive values. It is therefore a continuous increasing bijection onto $\mathbb R$. Its inverse $A=\arctan$ is continuous. The difference-quotient inverse argument used in (EF6) gives
\[
 A'(x)=\frac1{1+x^2},\qquad A(0)=0.
 \tag{EF13}
\]
Indeed $T'=1+T^2$. The fundamental theorem yields $A(x)=\int_0^x(1+t^2)^{-1}dt$. Evenness of the integrand makes $A$ odd. Formula (EF11) and parity give $C(c-t)=S(t)$; at $t=c/2$ the sine and cosine are positive and equal. Hence $T(c/2)=1$ and $A(1)=c/2=\pi/4$. The endpoint limits of the inverse give
\[
 \int_{\mathbb R}\frac{dt}{1+t^2}=2c=\pi.
 \tag{EF14}
\]
This improper integral agrees with the nonnegative Lebesgue integral by monotone convergence. For $R>0$, the integral over $|t|>R$ is at most $2/R$, by comparison with $t^{-2}$ and the primitive $-t^{-1}$.

For $\varepsilon>0$ define $P_\varepsilon(t)=\varepsilon/[\pi(t^2+\varepsilon^2)]$. Linear substitution, already supplied by length scaling and the scalar fundamental theorem, gives integral one, and
\[
 \int_{|t|>\delta}P_\varepsilon(t)dt
 \le\frac{2\varepsilon}{\pi\delta}\quad(\delta>0).
 \tag{EF15}
\]
If $h$ is bounded, measurable and continuous at $a$, subtract $h(a)$ inside $\int P_\varepsilon(t)h(a+t)dt$. On $|t|\le\delta$ the absolute error is at most $\sup_{|t|\le\delta}|h(a+t)-h(a)|$, since the kernel has total mass one. On the complement it is at most $2\|h\|_\infty$ times (EF15). First fix small $\delta$, then let $\varepsilon\to0$. This proves convergence to $h(a)$, including complex $h$.

<a id="smooth-flat-cutoffs"></a>
## Flat functions and smooth cutoffs

Define the real function
\[
 b(t)=\begin{cases}e^{-1/t},&t>0,\\0,&t\le0.\end{cases}
 \tag{EF16}
\]
On $t>0$, repeated product and chain rules express every derivative as a finite linear combination of $t^{-m}e^{-1/t}$ for nonnegative integers $m$. Equation (EF9), with $y=1/t$, shows that each such expression, even after division by any fixed positive power of $t$, tends to zero as $t\downarrow0$. This proves smoothness across zero by induction: the proposed $k$th derivative is zero on $t\le0$, continuous at zero, and its difference quotient at zero tends to zero by the same bound with one extra factor $t^{-1}$. Its derivative away from zero is the proposed $(k+1)$st expression. Thus $b\in C^\infty(\mathbb R)$ and every derivative at zero vanishes.

The denominator in
\[
 \Theta(t)=\frac{b(t)}{b(t)+b(1-t)}
 \tag{EF17}
\]
is positive everywhere: if $t\le0$ then $1-t>0$, and if $t>0$ the first term is positive. Hence $\Theta$ is smooth, takes values in $[0,1]$, equals zero on $(-\infty,0]$ and equals one on $[1,\infty)$. In $\mathbb R^n$, the function $\eta(x)=b(1-|x|^2)$ is smooth, positive in the unit ball and zero outside it. It has finite positive integral: it is bounded with compact support, and continuity and positivity at zero bound it below by a positive constant on a small cube of positive volume. Dividing by that integral gives a nonnegative smooth function of integral one. Translations and positive dilations give the usual compactly supported mollifiers, with normalization verified by the [linear volume-scaling proof](coordinate-inverses-and-integration.md#coordinate-integration).

For $0<r<R$, a smooth cutoff equal to one on the ball of radius $r$ and zero outside the ball of radius $R$ is
\[
 \chi(x)=\Theta\!\left(\frac{R^2-|x|^2}{R^2-r^2}\right).
 \tag{EF18}
\]
Translation gives the same construction about any center. Finite sums of these functions and division by a positive sum give the finite partitions in the coordinate reading. Division by the positive square root of a sum of squares is smooth by (EF7). The entire construction uses the explicit functions above.

<a id="programme-source-comparison"></a>

## Earlier readings

The general power-series differentiation argument is also proved in *Cauchy's theorem for cycles and its consequences*, Lemma 3.1, written by Claude Opus 5.5 and expanded by GPT-6.1 Sol, under CC0. That lesson's index proof uses the exponential period and the arctangent normalization. Both are proved here directly. The arguments (EF1)–(EF18) and their stated prerequisite links are the proof route for this reading; the comparison citation does not substitute for a proof.
