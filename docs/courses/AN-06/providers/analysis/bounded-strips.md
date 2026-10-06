# Bounded strips and the three-lines inequality

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

The circle mean-value formula is proved in Cauchy's theorem for cycles and its consequences, Lemma 1.1 and Theorems 2.1–2.3. That CC0 lesson is credited to Claude Opus 5.5 (Anthropic) and GPT-6.1 Sol (OpenAI). [Elementary functions](elementary-functions-and-cutoffs.md#scalar-exponential) supplies the complex exponential and real logarithm; [compactness and scalar integration](hilbert-valued-integration.md#compact-scalar-calculus) supplies the maxima and continuous-integral facts. The strip argument is proved below.

<a id="finite-rectangle-maximum"></a>

## The finite-rectangle maximum principle

A function continuous on a closed rectangle and holomorphic inside it has its maximum modulus on the boundary. Indeed compactness supplies a maximum $M$. If it is attained at an interior point $c$, the Cauchy formula on each sufficiently small circle about $c$ gives
\[
 f(c)=\frac1{2\pi}\int_0^{2\pi}f(c+re^{it})\,dt.
\]
When $M>0$, multiply by the unit complex number that makes $f(c)=M$. The real part of the integrand is at most $M$ and has mean $M$, so continuity forces it to be $M$ everywhere on the circle. The modulus bound then forces the imaginary part to vanish. Every sufficiently small circle is therefore constant with value $f(c)$, so $f$ is constant on a neighbourhood of $c$. More generally the set of interior points where $|f|=M$ is closed and, by this argument, open. The rectangle interior is connected: the segment between any two of its points stays inside, and a nonempty subset of a segment that is both open and closed cannot have a first exit, by the least-upper-bound property of the real interval. Thus the maximum-modulus set is the whole interior if nonempty. Continuity gives the same value $M$ on the boundary. For $M=0$ the assertion is immediate. This proves the rectangle principle from the actual mean-value proof, with no bounded-domain theorem left implicit.

<a id="bounded-strip-maximum"></a>
## Bounded-strip maximum principle

Let $S=\{z\in\mathbb C:0\leq\operatorname{Re}z\leq1\}$. Let $f$ be bounded and continuous on $S$, holomorphic on its interior, and satisfy $|f(it)|,|f(1+it)|\leq1$ for all real $t$. Then $|f(z)|\leq1$ everywhere on $S$.

For $\varepsilon>0$ put $f_\varepsilon(z)=f(z)e^{\varepsilon z^2}$. On the vertical boundaries its modulus is at most $e^\varepsilon$. On the horizontal boundaries $\operatorname{Im}z=\pm R$ it is at most $\|f\|_\infty e^{\varepsilon(1-R^2)}$. Choose $R$ large enough that the latter is at most $e^\varepsilon$. The finite-rectangle principle gives $|f_\varepsilon(z)|\leq e^\varepsilon$ on that rectangle. For each fixed $z=x+iy$ choose such an $R>|y|$; then
\[
 |f(z)|\leq e^{\varepsilon(1-x^2+y^2)}.
\]
Let $\varepsilon\downarrow0$. The boundary points already satisfy the claim. This proves the full strip principle including the horizontal exhaustion estimate.

<a id="three-lines"></a>
## Independent boundary bounds

Under the same continuity, holomorphy and boundedness hypotheses, suppose
\[
 |f(it)|\leq M_0,\qquad |f(1+it)|\leq M_1,
 \qquad M_0,M_1\geq0.
\]
Then for $0<x<1$ and every real $y$,
\[
 |f(x+iy)|\leq M_0^{1-x}M_1^x.
\]
If both constants are positive, set
\[
 g(z)=f(z)\exp(-(1-z)\log M_0-z\log M_1).
\]
The logarithms are real. Thus the factor has modulus $M_0^{x-1}M_1^{-x}$, uniformly bounded for $0\leq x\leq1$, so $g$ is bounded on the whole strip. Its two boundary moduli are at most one. Apply the preceding theorem and rearrange. If a boundary constant vanishes, apply the positive case with $M_j+\delta$ and let $\delta\downarrow0$; for interior $x$ the resulting bound is zero if either constant is zero. On each boundary retain its own original bound. The two constants are never replaced by a single maximum in the interior inequality.

Translation and positive horizontal rescaling give the same result on any strip $a\leq\operatorname{Re}z\leq b$, $a<b$, with $x$ replaced by $(\operatorname{Re}z-a)/(b-a)$. The two boundary constants remain separate after rescaling as well.
