# Scalar powers and the inequality used by Hölder

*Original proof sections by GPT-6 Astra (OpenAI), under CC0.
Self-checked by the writing AI; independent human review is not claimed.*

These are lines 7–86, equations EF1–EF9, of the
exact AN-06 elementary-function provider.
They retain the original geometric-series, exponential,
logarithm, real-power and Young-inequality proofs.
The inputs are ordered-real completeness and the one-variable
calculus declared in the course preparation, together with
the product and chain rules used in Lesson 1.
The later angular-coordinate and cutoff sections are outside
this selected component; those functions are already part
of the course preparation and earlier lessons.

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
