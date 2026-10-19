# A planar conformal map

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The construction of the last lesson needs a holomorphic function \(g\) on a domain \(D\subset\mathbf C\) whose horizontal slices are centred intervals, whose imaginary parts fill \((-1,1)\), and whose horizontal integrals of \(|(g^k)'|^2\) are controlled by \(|g|^{2k}\). This lesson constructs \(D\) as the image of the unit disc \(\mathbb D=\{|w|<1\}\) under the map
\[
F(w)=\frac8{\pi^2}\sum_{\ell=0}^\infty\frac{(-1)^\ell\,w^{2\ell+1}}{(2\ell+1)^2},
\]
and proves its properties (Theorem 5.2); \(g\) is the inverse of \(F\). This map appears in Gross's conformal Skorokhod embedding of the uniform distribution [Gr, Section 3.2], rotated by \(F(w)=i\psi(iw)\); OpenAI uses it in [OpenAI-SB, Section 3]. Complex analysis is cited from Lebl's guide in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50), and the implicit function theorem from Lebl's *Basic Analysis* in the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) ([Theorem 8.5.6](https://www.jirka.org/ra/html/sec_svinvfuncthm.html#thm_implicit)).

## 1. An arctangent

**Lemma 5.1.** The series \(a(w)=\sum_{\ell\ge0}(-1)^\ell w^{2\ell+1}/(2\ell+1)\) converges on \(\mathbb D\) and defines a holomorphic function with \(a'(w)=1/(1+w^2)\). For \(w\in\mathbb D\), the number \(\zeta=(1+iw)/(1-iw)\) has positive real part, and
\[
a(w)=\frac1{2i}\Bigl(\log|\zeta|+i\arctan\frac{\operatorname{Im}\zeta}{\operatorname{Re}\zeta}\Bigr).
\]
For \(w=re^{i\theta}\), \(\operatorname{Re}a(w)=\frac12\arctan\dfrac{2r\cos\theta}{1-r^2}\); and \(a(w)=0\) only for \(w=0\).

**Proof.** The series has radius of convergence \(1\), so it defines a holomorphic function on \(\mathbb D\) whose derivative is obtained termwise (Lebl, Proposition 2.4.2): \(a'(w)=\sum_\ell(-w^2)^\ell=1/(1+w^2)\). Multiplying numerator and denominator by \(\overline{1-iw}=1+i\bar w\),
\[
\begin{aligned}
\zeta&=\frac{1-|w|^2+i(w+\bar w)}{|1-iw|^2}\\
&=\frac{1-r^2+2ir\cos\theta}{|1-iw|^2},
\end{aligned}
\]
so \(\operatorname{Re}\zeta>0\). On the right half-plane \(\operatorname{Re}\zeta>0\), the function \(\Lambda(\zeta)=\log|\zeta|+i\arctan(\operatorname{Im}\zeta/\operatorname{Re}\zeta)\) satisfies the Cauchy–Riemann equations with \(\Lambda'(\zeta)=1/\zeta\): for \(\zeta=x+iy\), both \(\partial_x\log|\zeta|\) and \(\partial_y\arctan(y/x)\) equal \(x/|\zeta|^2\), and \(\partial_y\log|\zeta|=-\partial_x\arctan(y/x)=y/|\zeta|^2\). Since \(\frac d{dw}\frac{1+iw}{1-iw}=\frac{2i}{(1-iw)^2}\), the function \(b(w)=\frac1{2i}\Lambda\bigl(\frac{1+iw}{1-iw}\bigr)\) has
\[
\begin{aligned}
b'(w)&=\frac1{2i}\cdot\frac{1-iw}{1+iw}\cdot\frac{2i}{(1-iw)^2}\\
&=\frac1{1+w^2}=a'(w),
\end{aligned}
\]
and \(b(0)=0=a(0)\). The disc is connected, so \(a=b\). Taking real parts, \(\operatorname{Re}a=\frac12\arctan(\operatorname{Im}\zeta/\operatorname{Re}\zeta)\), which is the stated formula. If \(a(w)=0\), then \(\log|\zeta|=0\) and \(\operatorname{Im}\zeta=0\), so \(\zeta=1\) and \(w=0\). \(\square\)

## 2. The map

For \(w=re^{i\theta}\in\mathbb D\) put
\[
A(r,\theta)=\operatorname{Re}\bigl(wF'(w)\bigr).
\]

**Theorem 5.2.** (a) \(F\) is holomorphic and bounded on \(\mathbb D\), odd, \(F(\bar w)=\overline{F(w)}\), \(F(0)=0\), \(wF'(w)=\frac8{\pi^2}a(w)\), and \(F'(w)\ne0\) for every \(w\in\mathbb D\).

(b) \(A(r,\theta)=\dfrac4{\pi^2}\arctan\dfrac{2r\cos\theta}{1-r^2}\). On the right semicircles \(|\theta|<\pi/2\), \(0<A<2/\pi\); the real part of \(F\) is positive on the right half-disc, and \(\operatorname{Im}F(re^{i\theta})\) increases strictly with \(\theta\in(-\pi/2,\pi/2)\).

(c) \(F(ir)=iT(r)\) for \(-1<r<1\), where \(T\) is odd and strictly increasing, \(T(r)\to1\) as \(r\to1\), and
\[
T'(r)=\frac8{\pi^2}\,\frac{\operatorname{arctanh}r}r\qquad(0<r<1),
\]
so \(T'(r)\to\infty\) as \(r\to1\).

(d) \(F\) is injective. Its image \(D\) is a bounded open set, the imaginary parts of its points fill \((-1,1)\), and for each \(t\in(-1,1)\) there is \(0<V(t)<\infty\) with
\[
\{v\in\mathbf R:\ v+it\in D\}=(-V(t),V(t)).
\]
The inverse \(g=F^{-1}:D\to\mathbb D\) is holomorphic, and \(g(-\bar\zeta)=-\overline{g(\zeta)}\).

(e) Fix \(t\in(-1,1)\) and let \(r_0\in[0,1)\) be defined by \(T(r_0)=|t|\). For each \(r\in(r_0,1)\) there is exactly one \(\theta(r,t)\in(-\pi/2,\pi/2)\) with \(\operatorname{Im}F(re^{i\theta})=t\). The function \(v(r,t)=\operatorname{Re}F(re^{i\theta(r,t)})\) is continuously differentiable in \(r\), increases strictly from \(0\) (as \(r\downarrow r_0\)) to \(V(t)\) (as \(r\uparrow1\)), and
\[
\begin{aligned}
\frac{\partial v}{\partial r}(r,t)&=\frac{|wF'(w)|^2}{r\,A(r,\theta(r,t))}>0,\\
w&=re^{i\theta(r,t)}.
\end{aligned}
\]
Thus \(F\) maps the arc \(\{re^{i\theta(r,t)}:r_0<r<1\}\) onto the positive half \(\{v+it:0<v<V(t)\}\) of the slice at height \(t\).

**Proof.** (a) The coefficients are summable, so the series converges absolutely and uniformly on the closed disc; \(F\) is holomorphic on \(\mathbb D\) with termwise derivative (Lebl, Proposition 2.4.2) and bounded. Only odd powers occur, with real coefficients, which gives oddness and \(F(\bar w)=\overline{F(w)}\). Termwise, \(wF'(w)=\frac8{\pi^2}\sum_\ell(-1)^\ell w^{2\ell+1}/(2\ell+1)\), which is \(\frac8{\pi^2}a(w)\). So \(F'(0)=8/\pi^2\), and for \(w\ne0\), \(F'(w)\ne0\) by Lemma 5.1.

(b) The formula for \(A\) is Lemma 5.1. For \(\cos\theta>0\) the arctangent has a positive finite argument, so \(0<A<\frac4{\pi^2}\cdot\frac\pi2=\frac2\pi\). By the chain rule,
\[
\begin{aligned}
\partial_rF(re^{i\theta})&=\frac{wF'(w)}r,\\
\partial_\theta F(re^{i\theta})&=i\,wF'(w).
\end{aligned} \tag{5.1}
\]
Hence \(\partial_r\operatorname{Re}F(re^{i\theta})=A/r>0\) on the right half-disc, and since \(\operatorname{Re}F(0)=0\), \(\operatorname{Re}F>0\) there; and \(\partial_\theta\operatorname{Im}F(re^{i\theta})=A>0\).

(c) Since \(i^{2\ell+1}=i(-1)^\ell\), \(F(ir)=iT(r)\) with \(T(r)=\frac8{\pi^2}\sum_\ell r^{2\ell+1}/(2\ell+1)^2\), odd, and \(T'(r)=\frac8{\pi^2}\sum_\ell r^{2\ell}/(2\ell+1)\), which is \(\frac8{\pi^2}\operatorname{arctanh}(r)/r>0\) for \(0<r<1\); this tends to \(\infty\) as \(r\to1\). Since \(F(r)\) is real, (5.1) gives
\[
\begin{aligned}
T(r)&=\operatorname{Im}F(ir)-\operatorname{Im}F(r)\\
&=\int_0^{\pi/2}A(r,\theta)\,d\theta .
\end{aligned}
\]
The integrand is at most \(2/\pi\) and tends to \(2/\pi\) for every \(\theta\in[0,\pi/2)\) as \(r\to1\); by dominated convergence (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, *Measure Theory*, Volume 1, 123C](https://www1.essex.ac.uk/maths/people/fremlin/cont12.htm)), \(T(r)\to1\).

(e) Let \(r_0<r<1\). On the right semicircle of radius \(r\), \(\operatorname{Im}F\) increases strictly from \(-T(r)\) to \(T(r)\) (the endpoints \(\pm ir\) give \(\pm iT(r)\)), and \(|t|=T(r_0)<T(r)\); so there is exactly one \(\theta(r,t)\) with \(\operatorname{Im}F=t\). Since \(\partial_\theta\operatorname{Im}F=A>0\), the implicit function theorem shows that \(\theta(r,t)\) is continuously differentiable in \(r\). Write \(wF'(w)=A+iB\). By (5.1), \(\partial_r\operatorname{Im}F=B/r\), so differentiating \(\operatorname{Im}F(re^{i\theta(r,t)})=t\) gives \(\partial_r\theta=-B/(rA)\), and
\[
\begin{aligned}
\partial_rv&=\frac Ar+\operatorname{Re}\bigl(i(A+iB)\bigr)\,\partial_r\theta\\
&=\frac Ar+\frac{B^2}{rA}=\frac{A^2+B^2}{rA}.
\end{aligned}
\]
If \(r_0>0\), then as \(r\downarrow r_0\) the angle \(\theta(r,t)\) tends to the endpoint \(\pm\pi/2\) of the semicircle at which \(\operatorname{Im}F=t\), and \(v(r,t)\to\operatorname{Re}F(\pm ir_0)=0\); if \(r_0=0\), then \(t=0\), \(\theta(r,0)=0\) and \(v(r,0)=F(r)\to0\). The function \(v\) is increasing and bounded, so it tends to a finite limit \(V(t)>0\) as \(r\uparrow1\). A point \(F(re^{i\theta})\) with \(|\theta|<\pi/2\) and imaginary part \(t\) has \(T(r)>|t|\), that is \(r>r_0\), and then \(\theta=\theta(r,t)\); so the image of the right half-disc meets the line \(\operatorname{Im}=t\) exactly in \(\{v+it:0<v<V(t)\}\).

(d) By (e), \(F\) is injective on the right half-disc: equal images have the same \(t\) and the same \(v\), hence the same \(r\) and \(\theta\). Oddness and conjugation give \(F(-\bar w)=-\overline{F(w)}\), so the image of the left half-disc is the mirror image of that of the right half-disc in the imaginary axis, and \(F\) is injective there; and \(F\) is injective on the imaginary axis because \(T\) is strictly increasing. The three parts have images with positive, negative and zero real part, so \(F\) is injective on \(\mathbb D\). On the circle of radius \(r\), \(|\operatorname{Im}F|\le T(r)<1\), and every \(t\in(-1,1)\) occurs on the imaginary axis; with (e) and the mirror symmetry, the slice at height \(t\) is \((-V(t),V(t))\). By Lebl, Theorem 5.6.3, the image of the injective holomorphic map \(F\) is open and its inverse is holomorphic; the symmetry of \(g\) follows from that of \(F\). \(\square\)

## 3. Exercises

**5.1** (medium). Deduce from part (c) that \(\sum_{\ell\ge0}(2\ell+1)^{-2}=\pi^2/8\).

**5.2** (easy). Show that \(V(0)=F(1^-)=\frac8{\pi^2}G\), where \(G=\sum_{\ell\ge0}(-1)^\ell(2\ell+1)^{-2}\) is Catalan's constant, so \(V(0)\approx0.742\).

**5.3** (easy). Check numerically, from the series, that \(T(0.9)\approx0.832\), and compare with \(\int_0^{\pi/2}A(0.9,\theta)\,d\theta\).

## 4. Solutions

**5.1.** \(T(r)=\frac8{\pi^2}\sum_\ell r^{2\ell+1}/(2\ell+1)^2\) increases, as \(r\uparrow1\), to \(\frac8{\pi^2}\sum_\ell(2\ell+1)^{-2}\) by monotone convergence, and to \(1\) by part (c).

**5.2.** \(\theta(r,0)=0\) and \(v(r,0)=F(r)\); as \(r\uparrow1\), \(F(r)\to\frac8{\pi^2}\sum_\ell(-1)^\ell(2\ell+1)^{-2}\) by the uniform convergence on the closed disc. With \(G\approx0.91597\), \(8G/\pi^2\approx0.7425\).

**5.3.** The partial sums give \(T(0.9)\approx0.83159\); numerical integration of \(\frac4{\pi^2}\arctan\frac{1.8\cos\theta}{0.19}\) over \([0,\pi/2]\) gives the same value.

## References

- [OpenAI-SB] OpenAI, *Symplectic balls in symmetric polar products*, OpenAI Math Release preprint, 22 September 2026, Section 3, Lemma 3.1. https://github.com/openai/math/tree/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
- [Gr] R. Gross, *A conformal Skorokhod embedding*, Electronic Communications in Probability 24 (2019); arXiv:1905.00852. https://arxiv.org/abs/1905.00852
