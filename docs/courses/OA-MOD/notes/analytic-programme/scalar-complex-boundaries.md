# Closed boundaries and rectangles for scalar holomorphic functions

*Programme prerequisite for the modular analytic kernel. The proofs below are written by OpenAI Codex (GPT-6 Astra, Ultra), October 2026; CC0-1.0.*

Read [the preceding scalar complex-analysis proofs](scalar-complex-programme.md) first. That selection contains the complete programme proofs of interval integration and its norm estimate (Lemma 0.1), the index calculation for a square (Lemma 1.1), Goursat and convex Cauchy (Theorems 2.1–2.3), power series and Cauchy estimates (Lemma 3.1 and Theorem 3.2), Morera, locally uniform limits, and identity (Theorems 3.4–3.7). The numbering below is local to this supplement.

The scalar specializations of Lemma 0.1 do not require a Banach-space separation theorem: in its fundamental-theorem argument, take the real and imaginary coordinate maps on \(\mathbb C\). Real completeness and elementary real/complex arithmetic are the starting scalar conventions. The exponential and trigonometric identities, exact period, angle parametrization and kernel zeros are proved earlier in [EF1–EF6](elementary-exponential-trigonometry.md). No measure-theoretic interchange or modular theorem is used here.

## SC1 — Cauchy's theorem with continuous rectangle boundary

Let \(Q=[u,v]+i[s,t]\), with \(u<v\) and \(s<t\), and let \(f:Q\to\mathbb C\) be continuous and holomorphic on the interior. Then
\[
\int_{\partial Q}f(z)\,dz=0
\tag{SC.1}
\]
for positive orientation. Differentiability at boundary points is unnecessary.

**Proof.** Let \(c\) be the centre and \(0<\rho<1\). The contracted rectangle \(Q_\rho=c+\rho(Q-c)\) lies in the interior. Split it along a diagonal into two triangles. Goursat's theorem makes both triangular integrals zero; their common edge cancels, so the integral on \(\partial Q_\rho\) is zero. Parametrize each of the four sides of \(\partial Q\) by a fixed affine path \(\gamma:[0,1]\to Q\). The corresponding inner side is \(c+\rho(\gamma-c)\), with derivative \(\rho\gamma'\). Uniform continuity of \(f\) on \(Q\) gives
\[
\sup_{\tau\in[0,1]}
\big|\rho f(c+\rho(\gamma(\tau)-c))-f(\gamma(\tau))\big|
\longrightarrow0 .
\]
The path-length bound for integrals passes each side integral to its boundary value. Sum the four limits to obtain (SC.1). \(\square\)

## SC2 — Cauchy's formula on a closed disc

Suppose \(f\) is continuous on \(\overline{D(c,R)}\), \(R>0\), and holomorphic inside. For \(z\in D(c,R)\),
\[
f(z)=\frac1{2\pi i}\int_{|w-c|=R}\frac{f(w)}{w-z}\,dw .
\tag{SC.2}
\]
It follows that \(f(z)=\sum_{n\geq0}a_n(z-c)^n\), where
\[
a_n=\frac1{2\pi i}\int_{|w-c|=R}
 \frac{f(w)}{(w-c)^{n+1}}\,dw,\qquad
|a_n|\leq M R^{-n},\quad M=\max_{|w-c|=R}|f(w)|.
\tag{SC.3}
\]

**Proof.** For \(0<\rho<1\), the function \(f_\rho(w)=f(c+\rho(w-c))\) is holomorphic on the larger open disc of radius \(R/\rho\). Apply the programme's convex Cauchy formula to \(f_\rho\) and the circle of radius \(R\); Lemma 1.1 gives index one at \(z\). Uniform continuity on the original closed disc gives \(f_\rho\to f\) uniformly on that disc. Since \(|w-z|\geq R-|z-c|>0\) on the circle, the integral estimate passes the formula to the limit, proving (SC.2).

For \(|z-c|<R\), expand
\[
\frac1{w-z}=\sum_{n\geq0}\frac{(z-c)^n}{(w-c)^{n+1}}
\]
uniformly on the circle. Uniform-limit passage under its finite-length integral yields (SC.3) and the expansion. The bound follows because the circle length is \(2\pi R\). For every \(r<R\), the coefficient majorant is the convergent geometric series \(M\sum(r/R)^n\). Programme Lemma 3.1 proves differentiability of that series, including each derived series. Thus \(a_n=f^{(n)}(c)/n!\) and holomorphic functions have holomorphic derivatives. \(\square\)

## SC3 — Rectangle Morera and local primitives

Let \(f:U\to\mathbb C\) be continuous on an open set. If its integral on the boundary of every axis-aligned closed rectangle contained in \(U\) is zero, then \(f\) is holomorphic.

**Proof.** Choose a small open axis-aligned rectangle \(V\) whose closure lies in \(U\), a base point \(x_0+iy_0\in V\), and define
\[
P(x+iy)=\int_{x_0}^{x}f(a+iy_0)\,da
       +i\int_{y_0}^{y}f(x+ib)\,db.
\tag{SC.4}
\]
Oriented integrals handle either sign of an increment. Rectangle vanishing says that the route with the vertical segment first and horizontal segment second gives the same value. In particular, whenever the segments stay in \(V\),
\[
P(z+h)-P(z)=\int_0^h f(z+a)\,da\quad(h\in\mathbb R),
\]
and
\[
P(z+ik)-P(z)=i\int_0^k f(z+ib)\,db\quad(k\in\mathbb R).
\]
For a complex increment \(h+ik\), take first its horizontal and then its vertical segment. Subtract \(f(z)(h+ik)\). The resulting error has modulus at most
\[
(|h|+|k|)\!
\sup_{\substack{w\text{ on those}\\\text{two short segments}}}|f(w)-f(z)|
=o\bigl(|h+ik|\bigr),
\]
because \(|h|+|k|\leq\sqrt2\,|h+ik|\) and \(f\) is continuous. Hence \(P'(z)=f(z)\): \(P\) is holomorphic. SC2, or the preceding programme Theorem 3.2, proves that its derivative \(f\) is holomorphic. These rectangles cover \(U\). \(\square\)

For a holomorphic function on an open disc, programme Theorem 2.2 gives a primitive on that entire disc by integrating along the segment from its centre. If an interface asks for a function defined on all of \(\mathbb C\) whose derivative agrees with \(f\) at the points of that disc, assign arbitrary values outside the disc. Every point of the disc has an interior neighbourhood, so these assignments do not change its derivative there. No continuity outside the disc is claimed.

The triangle version of Morera is already proved in programme Theorem 3.4. Conversely, to use the rectangle criterion from triangle vanishing, split each rectangle along a diagonal and cancel the two copies of that diagonal.

## SC4 — The maximum bound on a rectangle

Let \(f\) be continuous on \(Q=[u,v]+i[s,t]\), holomorphic inside, and satisfy \(|f|\leq B\) on its boundary, where \(B\geq0\). Then \(|f|\leq B\) on all of \(Q\).

**Proof.** Compactness and continuity give a largest modulus \(M\). If it is attained on the boundary, there is nothing to prove. Otherwise let \(p\) be an interior point where \(|f(p)|=M\), and let \(d>0\) be its distance to the boundary. For \(0<r<d\), the circle Cauchy formula at \(p\), with its usual parametrization, gives
\[
f(p)=\frac1{2\pi}\int_0^{2\pi}f(p+re^{i\theta})\,d\theta.
\]
It follows that
\[
M\leq\frac1{2\pi}\int_0^{2\pi}|f(p+re^{i\theta})|\,d\theta\leq M.
\]
The continuous nonnegative function \(M-|f(p+re^{i\theta})|\) therefore has integral zero and is zero everywhere: a positive value would, by continuity, give a positive lower bound on a small interval and a positive integral. Choose a nearest boundary point \(q\), and let \(r\) increase to \(d\) along the ray from \(p\) to \(q\). Continuity gives \(|f(q)|=M\), so \(M\leq B\). This also covers \(M=0\). For a degenerate rectangle every point is on its boundary and the assertion is immediate. \(\square\)

## SC5 — The one-pole rectangle integral used by the modular kernel

Let \(Q=[-R,R]+i[-a,a]\), with \(R,a>0\). Suppose \(F\) is holomorphic on a neighbourhood of \(Q\setminus\{0\}\), and \(zF(z)\) extends holomorphically near zero with value \(b\). Then
\[
\int_{\partial Q}F(z)\,dz=2\pi i\,b.
\tag{SC.5}
\]

**Proof.** The power series of \(zF(z)\) near zero has constant term \(b\). Removing that term and dividing the remaining series by \(z\) gives a convergent power series. Thus \(G(z)=F(z)-b/z\), initially off zero, extends holomorphically over zero. By SC1, its rectangle integral is zero.

Choose a concentric square strictly inside \(Q\). Partition the closed region between the square and \(\partial Q\) into four trapezoids and then into finitely many triangles. Every triangle avoids zero. Apply Goursat to \(1/z\) on those triangles. Internal edges cancel, showing that its integral on \(\partial Q\) equals its integral on the positively oriented inner square. Programme Lemma 1.1(3) calculates the latter as \(2\pi i\). Adding the integral of \(G\) proves (SC.5). \(\square\)

For a horizontal-strip example of (SC.5), take
\[
F(z)=\frac{e^{-isz}h(z)}{e^{\pi z}-e^{-\pi z}},
\qquad s\in\mathbb R,
\]
on the rectangle of half-height \(1/2\). The denominator vanishes exactly at the points \(in\), \(n\in\mathbb Z\), so zero is its only zero in this rectangle. Its derivative at zero is \(2\pi\). Dividing its power series by \(z\) gives a holomorphic function with nonzero value \(2\pi\); therefore \(zF(z)\) is holomorphic near zero and has value \(h(0)/(2\pi)\). Formula (SC.5) yields \(i h(0)\). The vertical-strip formula used in MA05 and MA15 is instead proved in [IK1](../real-coercivity/bounded-modular-integral.md#ik1-the-integrals-and-the-scalar-strip-formula), by applying (SC.5) to its sine kernel. MA02 supplies the vector integrals and separation arguments used to pass that scalar identity to the Banach-valued functions in MA05 and MA15.

## Exact use in the modular course

The preceding programme selection and SC1–SC5 supply the scalar complex-analysis results used in MA02, MA05, MA08–09 and MA14–16. The existing MA proofs still supply the unbounded strip estimates, boundary gluing, vector contour identities, and spectral-domain conclusions. None of those conclusions is inferred merely from a reference to these scalar theorems.

This supplements only the scalar complex-analysis route. Scalar Lebesgue integration, spectral calculus, Hilbert-space representation, and the general Hilbert-algebra prerequisites remain distinct proof obligations. A comparison with a formal library is not a replacement for any of these written proofs.

