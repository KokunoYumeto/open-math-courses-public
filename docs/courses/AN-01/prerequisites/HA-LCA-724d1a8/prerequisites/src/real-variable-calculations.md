# Real-variable calculations for the Fourier examples

**Programme reading HA-LCA-PRE-REAL.** This reading follows HA-LCA-02 and precedes HA-LCA-03. It supplies the calculus and normalization used in the explicit Fourier and Bochner calculations. Self-checked by the writing AI.

We use the complete proofs of [elementary calculus and the exponential](banach-spectrum.md), [Lebesgue integration and convergence](integration-and-l1.md), and [the circle parametrization and Lebesgue normalization in HA-LCA-02](../../src/characters-and-the-dual-group.md). Thus \(dx\) denotes the completed Lebesgue measure constructed in that lesson's Lemma 3.3, and \(e^{it}\), \(\pi\), and \(E(t)=e^{2\pi it}\) have the meanings proved there.

Freely accessible sources for comparison are Jiří Lebl, [*Basic Analysis*, §5.3, Theorems 5.3.1, 5.3.3 and 5.3.5](https://www.jirka.org/ra/html/sec_ftc.html), read in the author's online version on 4 October 2026, and D. H. Fremlin, [*Measure Theory*, §283N and Exercise 283Y(c), version of 31 March 2013](https://www1.essex.ac.uk/maths/people/fremlin/mt2.2016/mt283.tex), in the 2016 source collection. The source Gaussian transform uses another normalization; all constants below are derived with \(e^{2\pi iux}\). We give the Gaussian normalization by one-dimensional substitutions and positive Fubini.

Adaptation and additional proofs: GPT-6 Astra (OpenAI), Ultra, October 2026. The combined reading is under the [Design Science License](../../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt). Fremlin's copyright 1994 and notices are retained in the unchanged original source package. Lebl's mathematical statements are compared; his prose and figures are not reproduced.

## 1. Calculus with the constructed Lebesgue measure

<a id="ha-lca-pre-real-lemma-1-1"></a>
### Lemma 1.1. Continuous and monotone Riemann integrals

A continuous complex function on a compact real interval has equal Riemann and Lebesgue integrals. A bounded monotone real function on that interval is Borel measurable, Riemann integrable, and has the same integral in both senses. For a monotone function, the difference between its endpoint upper and lower sums on a partition of mesh at most \(\delta\) is at most \(\delta\) times its total change.

**Proof.** For a continuous function \(f:[a,b]\to\mathbb C\), let \(P\) be a partition and select one tagged value on each half-open subinterval, defining a simple function \(s_P\). Give it any bounded endpoint value at \(a\). If the mesh is at most \(\delta\), uniform continuity from the Banach reading, Lemma 1.1, gives
\[
 |s_P(x)-f(x)|\le\omega_f(\delta)
 \quad(x\ne a),\qquad \omega_f(\delta)\longrightarrow0 .
\]
The Lebesgue integral of \(s_P\) is its tagged Riemann sum, because intervals have their length as measure and endpoints have measure zero by HA-LCA-02, Lemma 3.3. Therefore its difference from \(\int f\,dx\) is at most
\((b-a)\omega_f(\delta)\).
The Riemann sums converge to the integral proved in the Banach reading, Lemma 1.2, so the two values agree.

For increasing real \(f\), each strict upper or lower level set is an interval, possibly with an endpoint included, and hence is Borel. On a partition \(a=x_0<\cdots<x_n=b\), define the left- and right-endpoint step functions on \((x_{j-1},x_j]\). Except at finitely many endpoints, they bound \(f\) below and above. Their integrals are
\[
 L_P=\sum_j f(x_{j-1})(x_j-x_{j-1}),\qquad
 U_P=\sum_j f(x_j)(x_j-x_{j-1}).
\]
Monotonicity gives
\[
 0\le U_P-L_P
 \le\delta\sum_j(f(x_j)-f(x_{j-1}))
 =\delta(f(b)-f(a)).
\]
Both the Lebesgue integral and every tagged sum lie between these endpoint sums. Taking partitions of mesh tending to zero proves all the assertions, including the existence and value of the Riemann integral. Apply the result to \(-f\) for decreasing functions. \(\square\)

<a id="ha-lca-pre-real-lemma-1-2"></a>
### Lemma 1.2. Exponentials, powers and the arctangent integral

The exponential constructed by its power series satisfies
\[
 \frac{d}{dt}e^{zt}=ze^{zt}\quad(z\in\mathbb C).
\]
The real exponential is a strictly increasing bijection from \(\mathbb R\) to \((0,\infty)\). Its inverse \(\log\) is differentiable with derivative \(1/x\). Consequently, for real \(a\) and \(x>0\), \(x^a=e^{a\log x}\) satisfies
\((x^a)'=ax^{a-1}\). Also
\[
 \lim_{t\to0}\frac{1-\cos t}{t^2}=\frac12,\qquad
 \int_0^\infty\frac{dt}{1+t^2}=\frac\pi2,\qquad
 \int_{\mathbb R}\frac{dt}{1+t^2}=\pi.                 \tag{1.1}
\]

**Proof.** On every bounded \(t\)-interval, the exponential series and the series of its derivatives have uniform summable majorants, as in the Banach reading, Lemma 1.3: beyond a fixed index the ratios of consecutive majorants are at most \(1/2\). Its Lemma 1.2 permits termwise differentiation, giving the first identity. The already proved multiplication law gives \(e^t e^{-t}=1\), while \(e^t=(e^{t/2})^2>0\) for real \(t\). The fundamental theorem then makes \(e^t\) strictly increasing. For \(t\ge0\), its series gives \(e^t\ge1+t\), so \(e^t\to\infty\) as \(t\to\infty\); the reciprocal identity gives limit zero at \(-\infty\). Continuity and the intermediate-value theorem prove bijectivity.

A continuous strictly increasing bijection between intervals has continuous inverse: the images of two points on either side of a given point enclose an open neighbourhood of its image. If its derivative at that point is nonzero, the inverse difference quotient is the reciprocal of the original difference quotient, using inverse continuity to pass to the limit. Apply this to \(e^t\) to obtain \((\log x)'=1/x\). The product and chain rules, proved in the Banach reading, Lemma 1.2, give the power derivative. In particular \(x^a\) has limit zero at \(0+\) when \(a>0\), because \(\log x\to-\infty\) and the real exponential tends to zero there.

The exponential series gives
\(\cos t=1-t^2/2+R(t)\), where \(|R(t)|\le C|t|^4\) for \(|t|\le1\): bound the remaining even-power series by \(|t|^4\sum_{n\ge2}1/(2n)!\). Division by \(t^2\) proves the first limit in (1.1).

For the integral, put \(c(\theta)=\cos\theta\), \(s(\theta)=\sin\theta\) as the real and imaginary parts of \(e^{i\theta}\). The circle construction in HA-LCA-02, Lemma 1.3, gives \(c>0\) on \((-\pi/2,\pi/2)\), with endpoint limits \(s\to\pm1\) and \(c\to0+\). On this interval the function
\(T(\theta)=s(\theta)/c(\theta)\)
has derivative
\[
 T'(\theta)=\frac{c(\theta)^2+s(\theta)^2}{c(\theta)^2}
           =\frac1{c(\theta)^2}>0 .
\]
It is therefore a continuous strictly increasing bijection onto \(\mathbb R\). Its inverse \(A(t)\), called the arctangent, has derivative
\(A'(t)=c(A(t))^2=1/(1+t^2)\)
by the inverse difference-quotient argument above. Also \(A(0)=0\) and \(A(t)\to\pi/2\) as \(t\to+\infty\). The fundamental theorem on \([0,R]\), followed by monotone convergence and Lemma 1.1, gives the half-line integral in (1.1). Evenness gives the whole-line integral. \(\square\)

<a id="ha-lca-pre-real-lemma-1-3"></a>
### Lemma 1.3. Integration by parts and substitution

For complex \(C^1\) functions \(u,v\) on \([a,b]\),
\[
 \int_a^b u'v\,dx=u(b)v(b)-u(a)v(a)-\int_a^b uv'\,dx.  \tag{1.2}
\]
For a real \(C^1\) map \(\phi:[a,b]\to\mathbb R\) and a continuous complex \(f\) on an interval containing its image,
\[
 \int_a^b f(\phi(x))\phi'(x)\,dx
       =\int_{\phi(a)}^{\phi(b)}f(t)\,dt.               \tag{1.3}
\]
Integrals with reversed endpoints have the usual negative orientation. These identities extend to open or unbounded interval endpoints whenever the integrals involved are absolutely convergent and the boundary values in (1.2) have limits. For nonnegative integrands on increasing intervals, finite-interval identities may instead be passed to the limit by monotone convergence.

**Proof.** The product rule gives \((uv)'=u'v+uv'\). Integrate this identity using the fundamental theorem in the Banach reading, Lemma 1.2, and use Lemma 1.1 to identify its continuous Riemann integrals with Lebesgue integrals. Rearranging proves (1.2).

For (1.3), define \(F(t)=\int_{t_0}^t f(s)\,ds\), with any base point \(t_0\) in the target interval. The same fundamental theorem gives \(F'=f\). The chain rule yields
\((F\circ\phi)'=(f\circ\phi)\phi'\).
Integrating gives \(F(\phi(b))-F(\phi(a))\), which is the oriented integral on the right. Applying the argument to real and imaginary parts justifies complex \(f\).

For the endpoint statements, choose finite closed subintervals increasing to the desired interval. On each one the already proved identity holds. Dominated convergence with the absolute value of each integrable integrand passes its integral to the limit; the assumed boundary limits handle the remaining terms. Nonnegative integrands use monotone convergence instead. These are the earlier integration reading, Theorems 1.2 and 2.2. \(\square\)

<a id="ha-lca-pre-real-lemma-1-4"></a>
### Lemma 1.4. Differentiation with an integrable bound

Let \((X,\Sigma,\mu)\) be any measure space and \(J\) an open real interval. Suppose \(F(t,\cdot)\) is measurable for every \(t\in J\), \(F(t_0,\cdot)\) is integrable at some \(t_0\in J\), and outside one fixed null set the function \(t\mapsto F(t,x)\) is differentiable on \(J\). Suppose there is \(M\in L^1(\mu)\), \(M\ge0\), such that
\[
 |\partial_tF(t,x)|\le M(x)\quad(t\in J)
\]
outside that fixed null set. Then \(F(t,\cdot)\) is integrable for every \(t\in J\), and
\[
 \frac{d}{dt}\int_XF(t,x)\,d\mu(x)
      =\int_X\partial_tF(t,x)\,d\mu(x).                 \tag{1.4}
\]
Local bounds on neighbourhoods of each parameter point suffice for the corresponding local conclusion.

**Proof.** Enlarge the fixed null set to include the null set where \(M\) is infinite, and change \(F\) and \(M\) to zero there. The norm-valued derivative estimate proved in the Banach reading, Lemma 1.2, gives
\[
 |F(t,x)-F(s,x)|\le |t-s|M(x).
\]
Together with integrability at \(t_0\), this proves integrability at all \(t\). For fixed \(t\), the derivative is measurable as a pointwise limit of measurable difference quotients along a sequence tending to zero within \(J-t\). It is dominated by \(M\), so is integrable.

Every sufficiently small nonzero \(h\) has
\[
 \left|\frac{F(t+h,x)-F(t,x)}h\right|\le M(x).
\]
The quotient tends pointwise to \(\partial_tF(t,x)\). Along any sequence of such \(h\) tending to zero, dominated convergence from the integration reading, Theorem 2.2, therefore permits passage under the integral. This proves the full real-parameter derivative limit: if it failed, one could choose a sequence with \(0<|h_n|<1/n\) on which the error exceeded a fixed positive number, contradicting the sequence result. Linearity of the integral identifies the integrated quotient with the difference quotient of the integral. This proves (1.4), with no assumption of sigma-finiteness. Restricting \(J\) proves the local version. \(\square\)

## 2. The Gaussian integral and transform

<a id="ha-lca-pre-real-theorem-2-1"></a>
### Theorem 2.1. Gaussian normalization, transform and second moment

With \(g(x)=e^{-\pi x^2}\),
\[
 \int_{\mathbb R}g(x)\,dx=1,\qquad
 \int_{\mathbb R}g(x)e^{2\pi iux}\,dx=e^{-\pi u^2},     \tag{2.1}
\]
\[
 \int_{\mathbb R}xg(x)\,dx=0,\qquad
 \int_{\mathbb R}x^2g(x)\,dx=\frac1{2\pi}.              \tag{2.2}
\]
For \(a>0\), \(b\in\mathbb R\), the density
\(p_{a,b}(x)=a^{-1/2}e^{-\pi(x-b)^2/a}\)
has mass one, mean \(b\), variance \(a/(2\pi)\), and
\[
 \int_{\mathbb R}p_{a,b}(x)e^{2\pi iux}\,dx
       =e^{2\pi ibu}e^{-\pi a u^2}.                   \tag{2.3}
\]
All these integrals are absolutely convergent.

**Proof.** Lemmas 1.2–1.3 give
\(\int_0^\infty e^{-cx}\,dx=1/c\) for \(c>0\).
For \(|x|\ge1\), \(e^{-cx^2}\le e^{-c|x|}\), so a Gaussian is integrable. Every polynomial times a Gaussian is integrable and tends to zero at infinity. Indeed, choose an integer \(k\) with \(2k>m\). The positive exponential series gives, for \(|x|\ge1\),
\[
 e^{cx^2/2}\ge\frac{(cx^2/2)^k}{k!},\qquad
 |x|^m e^{-cx^2}\le k!(2/c)^k e^{-cx^2/2}.
\]
The last bound is integrable and tends to zero by comparison with \(e^{-c|x|/2}\); bounded compact intervals cause no problem.

Put \(A=\int_0^\infty e^{-x^2}\,dx>0\). Positive Fubini for Lebesgue measure is proved in the integration reading, Theorem 4.4, using finite interval restrictions. For fixed \(x>0\), the affine substitution \(y=xt\) from HA-LCA-02, Lemma 3.3, gives
\[
 \begin{aligned}
 A^2
 &=\int_0^\infty\int_0^\infty e^{-x^2-y^2}\,dy\,dx\\
 &=\int_0^\infty\int_0^\infty
       x e^{-(1+t^2)x^2}\,dt\,dx\\
 &=\int_0^\infty\left(\int_0^\infty
       x e^{-(1+t^2)x^2}\,dx\right)dt.
 \end{aligned}
\]
All integrands are nonnegative Borel functions, so positive Fubini justifies the interchanges before their integral is evaluated. Since
\((e^{-(1+t^2)x^2})'=-2(1+t^2)x e^{-(1+t^2)x^2}\),
Lemma 1.3 evaluates the inner integral as \(1/(2(1+t^2))\). Lemma 1.2 gives \(A^2=\pi/4\), hence
\(\int_{\mathbb R}e^{-x^2}\,dx=2A=\sqrt\pi\).
The affine substitution \(x=\sqrt\pi\,y\) proves the first equality in (2.1).

Set \(J(u)=\int g(x)e^{2\pi iux}\,dx\). The parameter derivative is bounded by the integrable function \(2\pi|x|g(x)\). Lemma 1.4 yields
\[
 J'(u)=2\pi i\int xg(x)e^{2\pi iux}\,dx
      =-i\int g'(x)e^{2\pi iux}\,dx.
\]
Integration by parts from Lemma 1.3 applies first on finite intervals and then on the whole line: the boundary values of \(g(x)e^{2\pi iux}\) tend to zero, and both resulting integrands are absolutely integrable. Therefore
\[
 \int g'(x)e^{2\pi iux}\,dx=-2\pi iuJ(u),\qquad
 J'(u)=-2\pi uJ(u).
\]
The derivative of \(e^{\pi u^2}J(u)\) is zero. The zero-derivative result in the Banach reading, Lemma 1.2, makes it constant, with value \(J(0)=1\). This proves the transform formula.

Oddness and \(x\mapsto-x\) prove \(\int xg(x)\,dx=0\). Integrating
\((xg(x))'=g(x)-2\pi x^2g(x)\), with zero boundary values and the established absolute integrability, gives the second moment in (2.2).

Finally substitute \(x=b+\sqrt a\,y\). Mass one follows from (2.1), and that same formula at frequency \(\sqrt a\,u\) gives (2.3). The centered first and second moments become
\(\sqrt a\int yg(y)\,dy=0\) and
\(a\int y^2g(y)\,dy=a/(2\pi)\).
This proves the mean and variance assertions. \(\square\)

## 3. Convex functions and triangular mixtures

<a id="ha-lca-pre-real-lemma-3-1"></a>
### Lemma 3.1. Right derivatives of a convex function

Let \(h\) be continuous and convex on an open real interval \(I\). Its right derivative exists and is finite at each \(r\in I\), and equals
\[
 d(r)=\inf_{\substack{s\in I\\s>r}}
              \frac{h(s)-h(r)}{s-r}.
\]
It is increasing and right-continuous. For \(a<b\) in \(I\),
\[
 d(a)\le\frac{h(b)-h(a)}{b-a}\le d(b),\qquad
h(b)-h(a)=\int_a^b d(r)\,dr.                           \tag{3.1}
\]

Conversely, a \(C^1\) function with increasing derivative is convex. In particular a \(C^2\) function with nonnegative second derivative is convex.

**Proof.** For \(u<v<w\), write \(v\) as the convex combination
\(((w-v)u+(v-u)w)/(w-u)\).
The convex inequality rearranges to
\[
 \frac{h(v)-h(u)}{v-u}
 \le\frac{h(w)-h(u)}{w-u}
 \le\frac{h(w)-h(v)}{w-v}.                             \tag{3.2}
\]
For fixed \(r\), slopes to points on its right decrease as those points decrease to \(r\). They are bounded below by the slope from any fixed point on its left to \(r\), and bounded above, near \(r\), by the slope to any fixed point on its right. Thus the infimum is finite and is the right derivative. Formula (3.2), with \(a,b\) as its first two points and any point beyond \(b\) as its third, gives the two inequalities in (3.1) after taking infima. These also give \(d(a)\le d(b)\).

If \(r_n\downarrow r\), monotonicity gives a limit \(\ell\ge d(r)\). For fixed \(s>r\) and all large \(n\),
\(d(r_n)\le(h(s)-h(r_n))/(s-r_n)\).
Continuity of \(h\) gives \(\ell\le(h(s)-h(r))/(s-r)\). Taking the infimum over \(s>r\) shows \(\ell\le d(r)\). Monotonicity then proves right continuity for the full right-hand limit.

On a partition \(a=x_0<\cdots<x_n=b\), the chord bounds give
\[
 \sum_j d(x_{j-1})(x_j-x_{j-1})
 \le h(b)-h(a)
 \le\sum_j d(x_j)(x_j-x_{j-1}).
\]
The bounded monotone function \(d\) has both endpoint sums tending to its integral by Lemma 1.1. This proves (3.1).

For the converse, let \(u<v<w\). The fundamental theorem expresses the slopes on \([u,v]\) and \([v,w]\) as averages of the derivative on those intervals. An increasing derivative has every value on the first interval at most every value on the second; hence the first average is at most the second. Multiplying by the positive interval lengths and rearranging gives
\[
 h(v)\le\frac{w-v}{w-u}h(u)+\frac{v-u}{w-u}h(w),
\]
which is the convex inequality. If \(h''\ge0\) and is continuous, the fundamental theorem applied to \(h'\) makes \(h'\) increasing, proving the final assertion. \(\square\)

<a id="ha-lca-pre-real-proposition-3-2"></a>
### Proposition 3.2. Constructing a triangular mixing measure

Let \(q:(0,\infty)\to[0,\infty)\) be finite-valued, decreasing and right-continuous, with \(\int_0^\infty q(s)\,ds=1\). There is a probability measure \(\rho\) on the Borel sets of \((0,\infty)\) such that
\[
 \int_r^\infty q(s)\,ds
 =\int_{(0,\infty)}\left(1-\frac rt\right)_+d\rho(t)
 \quad(r\ge0).                                       \tag{3.3}
\]
No bound on \(q\) near zero is assumed.

**Proof.** Monotonicity and integrability imply \(q(s)\to0\) at infinity, since a positive limiting value would give an infinite integral. For \(u>0\), define
\(\tau(u)=\sup\{s>0:q(s)>u\}\), with empty supremum zero. This is finite. For \(s>0\),
\[
 \{u>0:\tau(u)>s\}=(0,q(s)).                           \tag{3.4}
\]
Indeed \(\tau(u)>s\) gives a \(t>s\) with \(q(t)>u\), hence \(q(s)>u\). Conversely, \(u<q(s)\) and right continuity give a \(t>s\) with \(q(t)>u\). Thus \(\tau\) is Borel measurable. So is \(D=\{\tau>0\}=\bigcup_n\{\tau>1/n\}\).

Define a Borel measure on \((0,\infty)\) by
\[
 \nu(B)=\lambda\{u\in D:\tau(u)\in B\}.
\]
Disjoint inverse images prove countable additivity. Equation (3.4) gives
\(\nu((s,\infty))=q(s)\); in particular \(\nu\) is sigma-finite, since it is finite on each \((1/n,\infty)\). For every nonnegative Borel \(v\),
\[
 \int v(t)\,d\nu(t)=\int_D v(\tau(u))\,du.              \tag{3.5}
\]
This is the definition for indicators, follows by addition for simple functions, and extends by monotone convergence.

Positive Fubini for the two Lebesgue variables gives, for \(r\ge0\),
\[
 \begin{aligned}
 \int_D(\tau(u)-r)_+\,du
 &=\int_0^\infty\int_r^\infty
           \mathbf1_{\{s<\tau(u)\}}\,ds\,du\\
 &=\int_r^\infty\lambda\{u:\tau(u)>s\}\,ds
  =\int_r^\infty q(s)\,ds. 
 \end{aligned}                                      \tag{3.6}
\]
The integrand is Borel, and the half-lines have the sigma-finite Radon restrictions required by the integration reading, Theorem 4.4. This calculation uses only Lebesgue variables; it assumes no unproved regularity or product theorem for \(\nu\).

At \(r=0\), (3.5)–(3.6) give \(\int t\,d\nu(t)=1\). Put
\(\rho(B)=\int_Bt\,d\nu(t)\).
Monotone convergence proves countable additivity and the mass is one. Again indicator approximation gives
\(\int w\,d\rho=\int wt\,d\nu\)
for every nonnegative Borel \(w\). Apply this with \(w(t)=(1-r/t)_+\), and use (3.5)–(3.6), to obtain (3.3). \(\square\)
