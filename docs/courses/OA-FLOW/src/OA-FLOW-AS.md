# Bounded strip comparison from scalar proofs

*CC0-1.0 to the extent of rights held.*

This proof supplies only the analytic comparison needed for operator-valued weight transport. All dual spaces below have a specified predual. A group of isometries means a group of complex-linear surjective isometries whose individual maps are weak-star continuous and whose real orbits are weak-star continuous. No algebra or positivity property of that group is assumed.

The exact earlier written proofs are [SF4 scalar Cauchy, maximum, Morera, identity and zero-edge proofs](OA-FLOW-SF.md#oa-flow.sf.sf4); [FF-1 Gaussian normalization and transform](OA-FLOW-FF.md#oa-flow.ff.2); [CP1](OA-FLOW-CP.md#oa-flow.cp.1), [CP2](OA-FLOW-CP.md#oa-flow.cp.2), [CP3](OA-FLOW-CP.md#oa-flow.cp.3), [CP4](OA-FLOW-CP.md#oa-flow.cp.4), [CP5](OA-FLOW-CP.md#oa-flow.cp.5), [CP6](OA-FLOW-CP.md#oa-flow.cp.6) for the concrete predual and its dual; [scalar interchange](OA-FLOW-FF.md#oa-flow.ff.1), [SC4 monotone convergence](OA-FLOW-SC.md#sc-04) and [SC5 dominated convergence](OA-FLOW-SC.md#sc-05) for the scalar integrals. The proofs below do not import three-lines, Carlson, Paley–Wiener, Stone, or a theorem about closed analytic generators.

The comparison theorem is discussed in F. Hiai's [free author manuscript, printed pp.75–77](https://arxiv.org/pdf/2004.02383v1#page=75). Here a fourth-power sine kernel is normalized by direct Gaussian integration, and comparison is confined to the upper half-plane, where an elementary zero theorem applies.

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

## AS3. Contractive approximation by directly integrated entire kernels

Let \((\alpha_t)_{t\in\mathbb R}\) be a group of isometries of \(X=E^*\) in the opening sense. We construct a bounded approximate identity whose entire translates have an exponential bound in the imaginary direction. An element \(a\) is called exponential if its real orbit has a norm-entire extension \(A\) with

<a id="equation-as4"></a>

\[
 A(t)=\alpha_t(a),\qquad
 \|A(z)\|\leq K e^{c|\operatorname{Im}z|}
 \quad(z\in\mathbb C)                                           \tag{AS4}
\]
for finite \(K,c\geq0\). Scalar identity gives uniqueness and
\(A(z+t)=\alpha_t(A(z))\) for real \(t\). Consequently \(A(z_0)\) is again exponential, with extension \(z\mapsto A(z+z_0)\).

**A positive kernel with an elementary normalization.** Put
\[
 k(t)=\frac3{2\pi}\left(\frac{\sin t}{t}\right)^4,\qquad
 k_R(z)=Rk(Rz)\quad(R>0),
\]
using the removable value \(k(0)=3/(2\pi)\). We first prove \(\int_{\mathbb R}k(t)\,dt=1\).

For real \(a\), set \(J(a)=\int_{\mathbb R}(1-\cos(at))/t^2\,dt\). The integral is finite by the quadratic bound near zero and the \(t^{-2}\) bound at infinity. Since \(t^{-2}=\int_0^\infty e^{-ut^2}\,du\) for \(t\ne0\), nonnegative scalar interchange and the Gaussian transform from [FF-1](OA-FLOW-FF.md#oa-flow.ff.2) give
\[
 J(a)=\sqrt\pi\int_0^\infty u^{-1/2}
           (1-e^{-a^2/(4u)})\,du.
\]
For \(a\ne0\), substitute \(v=|a|/(2\sqrt u)\). Integration by parts, with both boundary terms zero, gives
\[
 J(a)=\sqrt\pi\,|a|\int_0^\infty\frac{1-e^{-v^2}}{v^2}\,dv
 =2\sqrt\pi\,|a|\int_0^\infty e^{-v^2}\,dv
 =\pi|a|.
\]
For \(a=0\) the equality is immediate. Now let \(f(t)=\sin^4t\). Since
\(f''(t)=2\cos(2t)-2\cos(4t)\), two integrations by parts on intervals avoiding zero yield

<a id="equation-as5"></a>

\[
 \int_{\mathbb R}\frac{\sin^4t}{t^4}\,dt
 =\frac16\int_{\mathbb R}\frac{f''(t)}{t^2}\,dt
 =\frac{J(4)-J(2)}3=\frac{2\pi}3.                               \tag{AS5}
\]
The boundary terms vanish at infinity by boundedness of \(f,f'\), and at zero by \(f(t)=O(t^4)\), \(f'(t)=O(t^3)\). Thus \(k\) is a nonnegative probability density. Also \(k(t)\leq3/(2\pi t^4)\) for \(t\ne0\). Scaling gives

<a id="equation-as6"></a>

\[
 k_R(s)\geq0,\qquad \int_{\mathbb R}k_R(s)\,ds=1,\qquad
 \int_{|s|>\delta}k_R(s)\,ds\leq\frac1{\pi R^3\delta^3}.
                                                                    \tag{AS6}
\]

**Entire translates and their integrable bounds.** The exponential formula for sine gives
\(|\sin(t+iv)|\leq e^{|v|}\). The identity
\(\sin z=z\int_0^1\cos(uz)\,du\) also gives
\(|\sin z/z|\leq e^{|\operatorname{Im}z|}\).
Combining these estimates and using \(|t+iv|\geq|t|\) yields
\[
 |k(t+iv)|\leq\frac3{2\pi}e^{4|v|}
                   \min(1,|t|^{-4}).
\]
The right side is integrable in \(t\). Its integral, followed by scaling, proves

<a id="equation-as7"></a>

\[
 \int_{\mathbb R}|k_R(s+iv)|\,ds
 \leq\frac4\pi e^{4R|v|}.                                      \tag{AS7}
\]
On every compact set of complex shifts, the kernels \(k_R(s-z)\) have a common integrable bound of the form \(C/(1+|s|^4)\). Cauchy estimates on a slightly larger compact set give such bounds for their derivatives and Taylor remainders. The map \(z\mapsto k_R(\,\cdot-z)\) is therefore holomorphic in \(L^1(\mathbb R)\).

**Approximation of the orbit.** Define the weak-star integral from AS2 by

<a id="equation-as8"></a>

\[
 A_R(z)=\int_{\mathbb R}k_R(s-z)\alpha_s(a)\,ds,\qquad a_R=A_R(0).
                                                                    \tag{AS8}
\]
The integral map from \(L^1(\mathbb R)\) into \(X\) has norm at most \(\|a\|\), so \(A_R\) is norm entire. Real substitution and weak-star continuity of each \(\alpha_t\) give

<a id="equation-as9"></a>

\[
 A_R(t)=\alpha_t(a_R),\qquad
 \|A_R(z)\|\leq\frac4\pi\|a\|e^{4R|\operatorname{Im}z|},\qquad
 \|a_R\|\leq\|a\|.                                             \tag{AS9}
\]
For \(e\in E\), split
\(\langle a_R-a,e\rangle=\int k_R(s)\langle\alpha_s(a)-a,e\rangle\,ds\)
at \(|s|=\delta\). Continuity of the scalar orbit makes the first part small when \(\delta\) is small; the explicit tail in AS6 makes the second part tend to zero as \(R\to\infty\). Thus \(a_R\to a\) weak-star. The exponential elements are weak-star dense, with contractive approximation and no separability hypothesis.

<a id="oa-flow.as.4"></a><a id="as-4"></a>

## AS4. Comparison from one-strip continuations

Let \(Y\subset X\) be a weak-star closed subspace with its inherited predual topology. Let \(\alpha_t\) on \(X\) and \(\gamma_t\) on \(Y\) be groups as above. Suppose that for every norm-entire \(\gamma\)-orbit \(A(z)=\gamma_z(a)\) there is an \(X\)-valued function \(B_a\), weak-star continuous on the closed lower unit strip, holomorphic inside, bounded on the whole strip, with

<a id="equation-as10"></a>

\[
 B_a(t)=\alpha_t(a),\qquad
 B_a(t-i)=\alpha_t(\gamma_{-i}(a))
 \quad(t\in\mathbb R).                                         \tag{AS10}
\]

Then

<a id="equation-as11"></a>

\[
 \alpha_t(y)=\gamma_t(y)\qquad(y\in Y,\ t\in\mathbb R).            \tag{AS11}
\]

It suffices, by AS3 and weak-star continuity, to prove this for an exponential \(y\in Y\). Write \(A\) for its entire \(\gamma\)-orbit, with \(\|A(z)\|\leq K e^{c|\operatorname{Im}z|}\), and put \(a_k=A(ik)\) for \(k\geq0\). These are exponential elements and \(\gamma_{-i}(a_k)=a_{k-1}\) for \(k\geq1\).

We construct only an upper-half-plane comparison. On \(k-1\leq\operatorname{Im}z\leq k\), for \(k=1,2,\ldots\), put

<a id="equation-as12"></a>

\[
 F(z)=B_{a_k}(z-ik).                                           \tag{AS12}
\]
At each seam \(z=t+ik\), the two definitions are both \(\alpha_t(a_k)\), by AS10. AS2's local rectangle argument glues their scalar pairings holomorphically. Consequently \(F\) is weak-star continuous on the closed upper half-plane, holomorphic in its interior, and \(F(t)=\alpha_t(y)\).

Apply AS1 to each scalar pairing on the \(k\)-th strip. Its two boundary norms are at most \(\|a_k\|\) and \(\|a_{k-1}\|\), because the real action is isometric. Duality gives
\[
 \|F(t+iv)\|\leq K e^{ck}\leq K e^{c(v+1)}
 \qquad(k-1\leq v\leq k).
\]
Also \(F(in)=a_n=A(in)\) for every positive integer \(n\).

Fix \(e\in E\). The scalar function
\[
 g_e(z)=e^{icz}\langle F(z)-A(z),e\rangle
 \qquad(\operatorname{Im}z>0)
\]
is holomorphic and bounded by \(K(e^c+1)\|e\|\). It vanishes at every \(in\), \(n\geq1\). AS1's bounded-half-plane zero theorem therefore makes \(g_e=0\). Continuity to the real boundary gives
\(\langle\alpha_t(y)-\gamma_t(y),e\rangle=0\) for every \(e\), proving AS11 on exponential elements. The contractive weak-star approximation in AS3 and continuity of the two real maps extend it to all \(Y\).

Only the continuations of the positive imaginary translates \(A(ik)\) were used. No negative-half-plane construction, global entire extension of the competing orbit, or closed analytic-generator calculus is required.
