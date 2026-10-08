# Exercises on analytic preparation

*Written by Claude Opus 5.5 (Anthropic), October 2026; self-checked by the writing AI. Original text: public domain (CC0). The function in Exercise 15 is an example from Guillaume Valette, On subanalytic geometry, arXiv:2507.23622v1.*

These two exercises use the cell preparation and Puiseux theorems proved in [Analytic finiteness for preparation](../analytic-finiteness-for-preparation.html).

### 15. A bounded function that needs a negative preparation exponent

**Level:** advanced. Let \(0<\epsilon<1\),

\[
C=\{(x,y):0<x<\epsilon,\ x^2<y<x\},
\]

and \(f(x,y)=x^3/y\) on \(C\). Show that \(f\) is bounded, but that no finite preparation of \(f\) over a cell decomposition of \(C\) has only nonnegative exponents in \(y\), This remains true when the preparation may translate \(y\) and use analytic units. The [convergent Puiseux theorem](../analytic-finiteness-for-preparation.html#convergent-puiseux-expansions) of that reading is needed.

**Solution.** Since \(y>x^2\), we have \(0<f<x<\epsilon\). Note that \(f=x^3y^{-1}\) is itself a preparation, with exponent \(-1\).

Assume a finite preparation with only nonnegative exponents exists. After refining and shrinking \(\epsilon\), the base cell next to \(0\) is \((0,\epsilon)\). Above it, finitely many definable functions

\[
x^2=\alpha_0(x)<\alpha_1(x)<\cdots<\alpha_N(x)=x
\]

cut \(C\) into bands \(\{\alpha_j<y<\alpha_{j+1}\}\), together with graphs. On each band

\[
f(x,y)=a(x)\,|y-\theta(x)|^r\,U(x,y),\qquad r\ge0,\qquad 0<m\le|U|\le M,
\]

where the graph of the definable function \(\theta\) does not meet the band. The convergent Puiseux expansion of \(\alpha_j\) starts with \(c_jx^{\nu_j}\), \(c_j>0\), and \(x^2\le\alpha_j\le x\) gives \(1\le\nu_j\le2\). As \(\nu_0=2\) and \(\nu_N=1\), some \(j\) has \(\nu_j>\nu_{j+1}\). Put \(\alpha=\alpha_j\) and \(\beta=\alpha_{j+1}\); then \(\alpha/\beta\to0\) as \(x\to0\).

On this band \(a(x)\ne0\), because \(f>0\). After shrinking the base interval, \(\theta\) is continuous and stays on one side of the band: \(\theta\le\alpha\) or \(\theta\ge\beta\). For small \(x\) the points \(y_1=2\alpha\) and \(y_2=\beta/2\) satisfy \(\alpha<y_1<y_2<\beta\), and

\[
\frac{f(x,y_2)}{f(x,y_1)}=\frac{y_1}{y_2}=\frac{4\alpha}{\beta}\longrightarrow0 .
\]

In the prepared form the same ratio is at least \((m/M)\bigl(|y_2-\theta|/|y_1-\theta|\bigr)^r\). If \(\theta\le\alpha\), the distance ratio is at least \(1\). If \(\theta\ge\beta\), then

\[
\frac{\theta-y_2}{\theta-y_1}\ge\frac{\beta-y_2}{\beta-y_1}\ge\frac{\beta/2}{\beta}=\frac12,
\]

because \(t\mapsto(t-y_2)/(t-y_1)\) increases for \(t>y_2\). In both cases the ratio is at least \(2^{-r}m/M>0\), a contradiction. So a negative exponent is needed. Boundedness does not prevent this: on bands that narrow towards \(x=0\), the coefficient \(a(x)\) absorbs the inverse power.

### 16. Even substitutions and parameter-dependent poles

**Level:** intermediate. Why does \(t=\tau^2\) not make \(\sqrt t\) analytic near \(\tau=0\), while \(t=\tau^4\) does? Then consider the globally subanalytic function

\[
f(x,t)=x\,t^{-1/2}+t^{1/3},\qquad x\in\mathbb R,\quad 0<t<1.
\]

Find a substitution \(t=\tau^k\) under which \(f\) becomes a Laurent polynomial in \(\tau\) for \(\tau>0\), and one under which this expression agrees with \(f\) for both signs of \(\tau\). On which pieces of the parameter line does \(f(x,\cdot)\) extend continuously, and analytically, in the original variable \(t\) at zero? Answer the analytic-extension question separately for the composed function in the new variable \(\tau\).

**Solution.** We have \(\sqrt{\tau^2}=|\tau|\), which is not analytic at \(0\), whereas \(\sqrt{\tau^4}=\tau^2\) is. For a two-sided substitution it is not enough that the substitution exponent be even: every exponent obtained after clearing denominators must be even.

The exponents \(-1/2\) and \(1/3\) have common denominator \(6\). With \(t=\tau^6\) and \(\tau>0\),

\[
f(x,\tau^6)=x\tau^{-3}+\tau^2 .
\]

Doubling the exponent, \(t=\tau^{12}\) gives \(t^{-1/2}=|\tau|^{-6}=\tau^{-6}\) and \(t^{1/3}=\tau^4\) for every \(\tau\ne0\), so

\[
f(x,\tau^{12})=x\tau^{-6}+\tau^4
\]

agrees with \(f\) for both signs of \(\tau\).

If \(x\ne0\), then \(f(x,t)\to\pm\infty\) as \(t\downarrow0\), with the sign of \(x\), so there is no continuous extension before or after substitution. If \(x=0\), then \(f(0,t)=t^{1/3}\) extends continuously by zero but has no real analytic extension in \(t\), since its difference quotient at zero is \(t^{-2/3}\), which diverges. After ramification, \(f(0,\tau^{12})=\tau^4\) is analytic across \(\tau=0\). Thus only the parameter piece \(\{0\}\) permits continuous extension in \(t\), no parameter permits analytic extension in \(t\), and exactly \(\{0\}\) permits analytic extension of the ramified function. The partition \((-\infty,0)\), \(\{0\}\), \((0,\infty)\) separates these behaviours. The extension is not jointly continuous at \((0,0)\): along \(x=t^{1/4}\), \(f=t^{-1/4}+t^{1/3}\to\infty\). Continuity in \(t\) on the single slice \(x=0\) is weaker than the joint continuity that a parameter theorem requires as its hypothesis.
