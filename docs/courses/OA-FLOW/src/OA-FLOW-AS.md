# Bounded strip comparison from scalar proofs

*Fresh local reconstruction, GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

This proof supplies only the analytic comparison needed for operator-valued weight transport. All dual spaces below have a specified predual. A group of isometries means a group of complex-linear surjective isometries whose individual maps are weak-star continuous and whose real orbits are weak-star continuous. No algebra or positivity property of that group is assumed.

The exact earlier written proofs are [SF4 scalar Cauchy, maximum, Morera, identity and zero-edge proofs](OA-FLOW-SF.md#oa-flow.sf.sf4); [FF2 scalar Fourier transform and Plancherel](OA-FLOW-FF.md#oa-flow.ff.3); [CP1](OA-FLOW-CP.md#oa-flow.cp.1), [CP2](OA-FLOW-CP.md#oa-flow.cp.2), [CP3](OA-FLOW-CP.md#oa-flow.cp.3), [CP4](OA-FLOW-CP.md#oa-flow.cp.4), [CP5](OA-FLOW-CP.md#oa-flow.cp.5), [CP6](OA-FLOW-CP.md#oa-flow.cp.6) for the concrete predual and its dual; [scalar interchange](OA-FLOW-FF.md#oa-flow.ff.1), [SC4 monotone convergence](OA-FLOW-SC.md#sc-04) and [SC5 dominated convergence](OA-FLOW-SC.md#sc-05) for the scalar integrals. The transform convention is \(\widehat p(s)=(2\pi)^{-1/2}\int p(x)e^{-isx}\,dx\), as fixed in [FF2](OA-FLOW-FF.md#oa-flow.ff.3). The proofs below do not import three-lines, Carlson, Paley–Wiener, Stone, or a theorem about closed analytic generators.

The development source for the exponential kernel and the comparison question is F. Hiai, [free author manuscript, arXiv:2004.02383v1](https://arxiv.org/pdf/2004.02383v1), printed pp. 75–77. The bounded-half-plane zero argument below replaces its printed Carlson footnote; only the stronger horizontal-band bound proved here is used.

<a id="oa-flow.as.1"></a><a id="as-1"></a>

## AS1. Two elementary analytic bounds

Let \(h>0\), and let \(f\) be scalar, continuous on \(-h\leq\operatorname{Im}z\leq0\), holomorphic inside, with a finite bound \(M\) on the entire strip. If both boundary lines have modulus at most \(C\), then

<a id="equation-as1"></a>

\[
 |f(z)|\leq C\qquad(-h\leq\operatorname{Im}z\leq0).                 \tag{AS1}
\]
Indeed, multiply by \(e^{-\varepsilon z^2}\), not by a function growing in the horizontal direction. On the horizontal sides of the rectangle \([-R,R]\times[-h,0]\) the modulus is at most \(Ce^{\varepsilon h^2}\); on the vertical sides it is at most \(Me^{-\varepsilon R^2+\varepsilon h^2}\). [SF4](OA-FLOW-SF.md#oa-flow.sf.sf4) maximum modulus, followed by \(R\to\infty\), gives
\[
 |f(z)e^{-\varepsilon z^2}|\leq Ce^{\varepsilon h^2}.
\]
Now let \(\varepsilon\downarrow0\). Translation gives the same statement on every horizontal strip. This argument needs the finite bound on the whole strip; a bound on the two edges alone is not the premise.

We also need the following zero statement:

<a id="equation-as2"></a>

\[
 \begin{gathered}
 g\text{ holomorphic and bounded on }\operatorname{Im}z>0,\qquad
 g(in)=0\quad(n=1,2,\ldots)\\
 \Longrightarrow\quad g=0.                                      \tag{AS2}
 \end{gathered}
\]
If \(g\neq0\), the identity theorem gives a noninteger \(y>0\) with \(g(iy)\neq0\). Set
\[
 H(w)=g\!\left(iy\,\frac{1+w}{1-w}\right),\qquad |w|<1.
\]
The displayed map has positive imaginary part \(y(1-|w|^2)/|1-w|^2\), so \(H\) is bounded by some \(M\). It vanishes at
\[
 a_n=\frac{n-y}{n+y}\in(-1,1),\qquad n\geq1.
\]
For any finite selection of these zeros, divide \(H\) by the product of the factors
\[
 B_{a_n}(w)=\frac{w-a_n}{1-a_nw}.
\]
The quotient has removable singularities at the selected zeros. The maximum principle on \(|w|\leq r\), followed by \(r\uparrow1\), bounds its modulus by \(M\), because each finite product has boundary modulus tending uniformly to \(1\). Consequently
\[
 |H(0)|\leq M\prod_{n=1}^{N}|a_n|.
\]
The finite factors are nonzero. For \(n>y\),
\[
 \log a_n=\log\!\left(1-\frac{2y}{n+y}\right)
 \leq-\frac{2y}{n+y},
\]
so the product tends to zero. This contradicts \(H(0)\neq0\), proving ([AS2](OA-FLOW-AS.md#equation-as2)). The disk maximum principle here has the same elementary proof as [SF4](OA-FLOW-SF.md#oa-flow.sf.sf4)'s rectangle version: the local power series makes \(|H|^2\) twice differentiable with nonnegative Laplacian; adding \(\varepsilon|w|^2\) excludes an interior maximum on a closed disk, and then \(\varepsilon\downarrow0\) gives the boundary maximum.

It follows in particular that an entire \(f\) satisfying

<a id="equation-as3"></a>

\[
 |f(z)|\leq K e^{c|\operatorname{Im}z|},\qquad f(in)=0\quad(n\geq1),       \tag{AS3}
\]
vanishes: \(e^{icz}f(z)\) is bounded in the upper half-plane, so ([AS2](OA-FLOW-AS.md#equation-as2)) applies there and the identity theorem finishes. The horizontal-band exponent, rather than a radial exponential bound, is essential to this proof.

<a id="oa-flow.as.2"></a><a id="as-2"></a>

## AS2. Weak-star analytic maps and integration

For a dual Banach space \(X=E^*\), a bounded weak-star continuous function of a real variable can be integrated against any \(L^1\) scalar kernel: its value is the functional
\[
 e\longmapsto \int k(s)\langle F(s),e\rangle\,ds,\qquad e\in E.
\]
This defines an element of \(X\), of norm at most \(\int|k(s)|\,\|F(s)\|\,ds\). The same construction defines circle integrals for weak-star continuous, norm-bounded curves.

A locally norm-bounded weak-star holomorphic map is norm holomorphic. To see this without an additional vector-valued theorem, take a closed circle of radius \(r\) in its domain, use the preceding integrals to form its Cauchy coefficients \(A_n\), and apply the scalar circle formula to every \(e\in E\). If the bound on the circle is \(M\), then \(\|A_n\|\leq Mr^{-n}\). The norm-convergent power series on every smaller disk equals the original map after pairing with all \(e\), hence equals it in \(X\). The same argument proves the norm Cauchy formula. Scalar continuity on a closed strip, uniform norm bounds, and scalar holomorphy inside are sufficient for every use of this observation below.

For bounded scalar functions, two adjacent closed-strip holomorphic functions that agree on the shared line glue holomorphically across it. Subdivide a small rectangle meeting the line into upper and lower rectangles with a gap of width \(2\delta\). Their boundary integrals vanish; continuity makes the gap contributions cancel as \(\delta\downarrow0\). [SF4](OA-FLOW-SF.md#oa-flow.sf.sf4) Morera applies. Testing by every \(e\), and then using the preceding local norm bounds, proves the corresponding assertion for dual-valued maps.

<a id="oa-flow.as.3"></a><a id="as-3"></a>

## AS3. A dense class with a horizontal exponential bound

Let \((\alpha_t)_{t\in\mathbb R}\) be a group of isometries of \(X=E^*\) in the opening sense. An element \(a\) is called exponential here if its orbit is the restriction of a norm-entire map \(A:\mathbb C\to X\) satisfying

<a id="equation-as4"></a>

\[
 A(t)=\alpha_t(a),\qquad
 \|A(z)\|\leq K e^{c|\operatorname{Im}z|}                           \tag{AS4}
\]
for finite \(K,c\geq0\). Such an extension is unique by scalar identity. It satisfies \(A(z+t)=\alpha_t(A(z))\) for real \(t\): both sides are weak-star holomorphic and agree when \(z\) is real. In particular \(A(z_0)\) is exponential, with extension \(z\mapsto A(z+z_0)\).

For \(R>0\) put

<a id="equation-as5"></a>

\[
 p_R(x)=R^{-1/2}1_{[-R/2,R/2]}(x),\qquad
 q_R(z)=\widehat p_R(z)^2
       =\frac{1-\cos(Rz)}{\pi Rz^2},\quad q_R(0)=\frac R{2\pi}.     \tag{AS5}
\]
The apparent singularity is removable by the scalar power series. Direct integration of \(p_R\) gives
\[
 \widehat p_R(z)=\sqrt{\frac2{\pi R}}\,\frac{\sin(Rz/2)}z.
\]
Since \(p_R\in L^1\cap L^2\), [FF2](OA-FLOW-FF.md#oa-flow.ff.3) gives

<a id="equation-as6"></a>

\[
 q_R(s)\geq0,\quad \int_{\mathbb R}q_R(s)\,ds=1,\quad
 \int_{|s|>\delta}q_R(s)\,ds\leq\frac4{\pi R\delta}\quad(\delta>0).
                                                                    \tag{AS6}
\]
The last bound uses \(1-\cos(Rs)\leq2\). For every real \(v\), apply [FF2](OA-FLOW-FF.md#oa-flow.ff.3) to the compactly supported function \(p_R(x)e^{vx}\); its Fourier transform is the same directly evaluated integral \(\widehat p_R(s+iv)\). Therefore

<a id="equation-as7"></a>

\[
 \begin{split}
 \int_{\mathbb R}|q_R(s+iv)|\,ds
 &=\int_{\mathbb R}|\widehat p_R(s+iv)|^2\,ds\\
 &=\frac1R\int_{-R/2}^{R/2}e^{2vx}\,dx
 =\frac{\sinh(Rv)}{Rv}\leq e^{R|v|},                              \tag{AS7}
 \end{split}
\]
where the ratio is \(1\) at \(v=0\).

For \(a\in X\), define the weak-star integral

<a id="equation-as8"></a>

\[
 A_R(z)=\int_{\mathbb R}q_R(s-z)\alpha_s(a)\,ds,\qquad a_R=A_R(0).
                                                                    \tag{AS8}
\]
On each compact set of \(z\)'s the kernel is bounded by \(C/(1+s^2)\): for large \(|s|\) this follows from ([AS5](OA-FLOW-AS.md#equation-as5)), and on the remaining compact set it follows from removal of the singularity. Cauchy estimates on slightly larger compact sets give the same integrable domination for each local Taylor coefficient and its remainder. Thus \(z\mapsto q_R(\,\cdot-z)\) is holomorphic in \(L^1\), and ([AS8](OA-FLOW-AS.md#equation-as8)) is norm entire. Change of variable and weak-star continuity of \(\alpha_t\) give

<a id="equation-as9"></a>

\[
 A_R(t)=\alpha_t(a_R),\qquad
 \|A_R(z)\|\leq\|a\|e^{R|\operatorname{Im}z|}.                    \tag{AS9}
\]
Finally ([AS6](OA-FLOW-AS.md#equation-as6)), continuity at zero of \(s\mapsto\langle\alpha_s(a),e\rangle\), and its uniform bound prove \(\langle a_R,e\rangle\to\langle a,e\rangle\) for every \(e\in E\). Hence the exponential elements are weak-star dense. Also \(\|a_R\|\leq\|a\|\); no unbounded approximation is being used.

<a id="oa-flow.as.4"></a><a id="as-4"></a>

## AS4. Comparison from one-strip continuations

Let \(Y\subset X\) be a weak-star closed subspace, with its inherited predual topology. Let \(\alpha_t\) on \(X\) and \(\gamma_t\) on \(Y\) be groups as above. Suppose that for every norm-entire \(\gamma\)-orbit \(A(z)=\gamma_z(a)\) there is an \(X\)-valued function \(B_a\) on the closed lower unit strip that is weak-star continuous, holomorphic inside, bounded on the whole strip, and satisfies

<a id="equation-as10"></a>

\[
 B_a(t)=\alpha_t(a),\qquad
 B_a(t-i)=\alpha_t(\gamma_{-i}(a))\quad(t\in\mathbb R).             \tag{AS10}
\]
Then

<a id="equation-as11"></a>

\[
 \alpha_t(y)=\gamma_t(y)\qquad(y\in Y,\ t\in\mathbb R).             \tag{AS11}
\]

Fix an exponential \(y\in Y\), and write its entire extension as \(A(z)\), with bound ([AS4](OA-FLOW-AS.md#equation-as4)). For every integer \(k\), apply ([AS10](OA-FLOW-AS.md#equation-as10)) to \(a_k=A(ik)\), whose entire orbit is \(A(z+ik)\). Put

<a id="equation-as12"></a>

\[
 F(z)=B_{a_k}(z-ik)
 \quad\text{on }k-1\leq\operatorname{Im}z\leq k.                 \tag{AS12}
\]
At the shared line of adjacent strips both definitions equal \(\alpha_t(a_k)\), so [AS2](OA-FLOW-AS.md#oa-flow.as.2) glues them. For \(e\in E\), [AS1](OA-FLOW-AS.md#oa-flow.as.1) bounds its scalar values on the strip by
\[
 |\langle F(z),e\rangle|
 \leq \max(\|a_k\|,\|a_{k-1}\|)\,\|e\|.
\]
Duality therefore gives \(\|F(z)\|\leq K e^{c(|\operatorname{Im}z|+1)}\). The function \(F\) is norm entire by [AS2](OA-FLOW-AS.md#oa-flow.as.2), satisfies \(F(t)=\alpha_t(y)\), and \(F(ik)=A(ik)\) for all integers \(k\).

For every \(e\), the scalar function \(\langle F(z)-A(z),e\rangle\) satisfies ([AS3](OA-FLOW-AS.md#equation-as3)), with possibly a larger constant \(K\). [AS1](OA-FLOW-AS.md#oa-flow.as.1)'s half-plane zero proof shows that it is zero. Thus \(F=A\), proving ([AS11](OA-FLOW-AS.md#equation-as11)) on all exponential elements. By [AS3](OA-FLOW-AS.md#oa-flow.as.3) those elements are weak-star dense in \(Y\), and the individual maps \(\alpha_t,\gamma_t\) are weak-star continuous. This proves ([AS11](OA-FLOW-AS.md#equation-as11)) for every \(y\).

The theorem uses a bounded continuation separately for each entire element and each of its imaginary translates. It does not assume, or claim to prove, a general closed analytic-generator calculus. That narrower statement is sufficient for the modular and cocycle applications.
