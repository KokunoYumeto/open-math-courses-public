# Locating singularities through logarithmic Fourier strips

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Public domain (CC0 1.0).*

Ordinary support and singular support answer different questions. A compact smooth function can extend far beyond a small region containing every singularity of a distribution. Its Fourier transform still has exponential growth determined by that larger ordinary support. A logarithmic complex strip makes the smooth part arbitrarily small, and thereby detects the convex region containing the singularities.

Basic references are Terence Tao's *Some connections with the Fourier transform* and Lars Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. We supply the strip criterion, its full inversion argument, and its two applications here. The preceding [joint logarithmic-frequency lesson](../../AN02-L157.html#2-the-compactness-and-support-statement) supplies the exact compactness and profile conventions. [Compact Fourier division](../../AN02-L122.html#3-a-bounded-complex-displacement-for-polynomial-division) supplies the proved uniform radius-two division bound. [Compact smooth Fourier decay](../../AN02-L153.html#tp2-exact-entire-decay-on-a-fixed-smooth-support) and [the logarithmic contour identity](../../AN02-L153.html#tp3-the-complete-logarithmically-shifted-contour) supply their exact whole-complex estimates and Jacobian. The arguments use finite-order compact-distribution bounds, smooth cutoffs, ordinary Lebesgue integration, and finite-dimensional convex separation.

Our convention is \(F_u(\zeta)=\langle u(x),e^{-ix\cdot\zeta}\rangle\), with inverse factor \((2\pi)^{-n}\), and \(D_j=(1/i)\partial_{x_j}\). The singular support of a distribution is the closed set of points near which it is not represented by a smooth function. For a compact distribution it is compact, possibly empty. The convex hull of the empty set is empty.

## 1. A precise strip criterion

For a nonempty compact convex set \(K\subset\mathbb R^n\), write \(H_K(\eta)=\max_{x\in K}x\cdot\eta\).

**Theorem 1.1.** Let \(u\) be a compact distribution on \(\mathbb R^n\), \(n\ge1\). The inclusion \(\operatorname{sing\,supp}u\subset K\) is equivalent to the existence of a nonnegative integer \(N\), independent of \(m\), and finite constants \(C_m\) such that

\[
|F_u(\zeta)|\le C_m(1+|\zeta|)^N e^{H_K(\operatorname{Im}\zeta)}
\quad\text{whenever}\quad
|\operatorname{Im}\zeta|\le m\log(1+|\zeta|),
\qquad m=1,2,\ldots.
\tag{1.1}
\]

The constants \(C_m\) may grow with the width \(m\). The exponent \(N\) must stay fixed as the width increases.

**Necessity.** Choose a finite-order bound of order \(M\) for \(u\) on a fixed compact neighborhood of its ordinary support. For a chosen \(m\ge1\), take \(\delta=1/(m+1)\), and a compact smooth cutoff \(\chi\) equal to one near \(K\), supported in \(K+\delta\overline B\). Such a cutoff can be made explicitly by convolving the indicator of the \(\delta/2\) neighborhood of \(K\) with a nonnegative radius-\(\delta/4\) smooth kernel of integral one. It equals one on the \(\delta/4\) neighborhood and is supported in the \(3\delta/4\) neighborhood.

The kernel can be the normalized bump \(e^{-1/(1-|x|^2)}\) on \(|x|<1\), zero outside, scaled to the stated radius. Its derivatives are finite sums of a polynomial times inverse powers of \(1-|x|^2\) times the exponential. Since \(t^{-j}e^{-1/t}\to0\) for every \(j\) as \(t\downarrow0\), all derivatives extend by zero. Its positive finite integral gives the normalization.

Set \(u_1=\chi u\) and \(b=(1-\chi)u\). The second term is smooth near every point: near a singular point its multiplier is zero, and away from the singular support \(u\) already is smooth. It is also compactly supported, so \(b\in C_c^\infty\). The distribution \(u_1\) retains order at most \(M\); the cutoff derivatives change its bound's constant. Evaluating the finite-order bound on \(\chi e^{-ix\cdot\zeta}\) gives

\[
|F_{u_1}(\zeta)|\le A_m(1+|\zeta|)^M
 e^{H_K(\operatorname{Im}\zeta)+\delta|\operatorname{Im}\zeta|}
\le A_m(1+|\zeta|)^{M+1}e^{H_K(\operatorname{Im}\zeta)}
\tag{1.2}
\]

on the strip in (1.1), because \(\delta m<1\).

Let \(S_b\) be a compact carrier of \(b\), \(r_b=\max_{x\in S_b}|x|\), and \(r_K=\max_{x\in K}|x|\). If \(b=0\), omit this term. Otherwise whole-complex smooth decay gives, for every integer \(L\ge0\),

\[
|F_b(\zeta)|e^{-H_K(\operatorname{Im}\zeta)}
\le B_L(1+|\zeta|)^{-L}
 e^{(r_b+r_K)|\operatorname{Im}\zeta|}
\le B_L(1+|\zeta|)^{-L+m(r_b+r_K)}.
\tag{1.3}
\]

Choose \(L>m(r_b+r_K)\). This term is bounded by a constant on the strip. Add it to (1.2) and take \(N=M+1\). The order is independent of \(m\), while both cutoff and smooth-decay constants may depend on \(m\). This proves necessity, including a distribution that is smooth everywhere.

We prove sufficiency after establishing the inversion step with its exact normalization.

## 2. Gaussian inversion for a compact distribution

Define

\[
q_\varepsilon(x)=(4\pi\varepsilon)^{-n/2}e^{-|x|^2/(4\varepsilon)},
\qquad
u_\varepsilon(x)=\langle u(y),q_\varepsilon(x-y)\rangle,
\qquad \varepsilon>0.
\tag{2.1}
\]

These pairings use a fixed cutoff equal to one near the compact support of \(u\). Differentiating in \(x\) is legitimate by the finite-order distribution bound on that fixed support, so \(u_\varepsilon\) is smooth.

We recall the Gaussian Fourier pair directly. In one dimension the integral of \(e^{-t^2}\) is \(\sqrt\pi\): square the positive integral, apply Tonelli, and use polar coordinates to obtain \(\int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta=\pi\). If \(G(\xi)=\int e^{-x^2/(4\varepsilon)}e^{-ix\xi}\,dx\), differentiation and integration by parts give \(G'(\xi)=-2\varepsilon\xi G(\xi)\), with \(G(0)=\sqrt{4\pi\varepsilon}\). Thus \(F_{q_\varepsilon}(\xi)=e^{-\varepsilon\xi^2}\). The same computation with the roles reversed gives its inverse integral. Products give all \(n\) coordinates and yield

\[
u_\varepsilon(x)=(2\pi)^{-n}\int_{\mathbb R^n}
 e^{ix\cdot\xi}F_u(\xi)e^{-\varepsilon|\xi|^2}\,d\xi.
\tag{2.2}
\]

To justify evaluation of \(u\) inside the inverse integral, every \(y\)-derivative through its fixed order contributes a polynomial in \(\xi\); the Gaussian majorizes every such polynomial. The resulting test functions and their derivatives converge uniformly on the fixed compact support. The distribution bound therefore permits the interchange. No pairing with a second nonsmooth distribution is used.

Also \(u_\varepsilon\to u\) in distributions. For a compact smooth test \(\varphi\), its pairing is \(\langle u,q_\varepsilon*\varphi\rangle\). The test function need only be considered on a fixed compact neighborhood of \(\operatorname{supp}u\), using the same cutoff. Each derivative through the finite order of \(u\) converges there uniformly to the corresponding derivative of \(\varphi\). Indeed, split the convolution into a small ball, where uniform continuity controls the difference, and its Gaussian tail, whose mass tends to zero. The finite-order bound proves distributional convergence.

An immediate consequence will be useful:

**Lemma 2.1.** If \(F_u\) decreases faster than every polynomial on \(\mathbb R^n\), then \(u\in C_c^\infty\).

**Proof.** For every derivative order \(q\), the inverse integral \((2\pi)^{-n}\int e^{ix\cdot\xi}F_u(\xi)\,d\xi\) is absolutely convergent after multiplying by each monomial \(\xi^\alpha\), \(|\alpha|\le q\). Dominated convergence differentiates it to order \(q\) and removes the Gaussian in (2.2), uniformly on compact \(x\)-sets. The limit represents \(u\) by its distributional convergence. Since \(q\) was arbitrary it is smooth, and its distributional compact support makes it compactly supported as a smooth function. \(\square\)

## 3. Moving the Gaussian contour and removing the regularization

**Sufficiency in Theorem 1.1.** Fix \(x_0\notin K\). By the closest-point separation argument, there is a real unit vector \(\theta\) and a bounded open neighborhood \(U\) of \(x_0\), with a number \(\delta>0\), such that

\[
x\cdot\theta-H_K(\theta)\ge\delta\qquad(x\in U).
\tag{3.1}
\]

For example choose a closest point \(p\in K\), take \(\theta=(x_0-p)/|x_0-p|\), and shrink \(U\) until half the strictly positive gap remains.

Write \(r=|\xi|\), \(\ell(\xi)=\log(2+r^2)\). For \(R\ge2\) and \(0\le t\le1\), use the complex parametrization

\[
\zeta_t(\xi)=\xi+i tR\theta\,\ell(\xi),\qquad
J_t(\xi)=1+i tR\theta\cdot\nabla\ell(\xi),\qquad
|J_t|\le1+R.
\tag{3.2}
\]

The determinant formula is the rank-one identity
\(\det(I+i tR\theta(\nabla\ell)^{\mathsf T})=1+i tR\theta\cdot\nabla\ell\).
Also \(|\nabla\ell|=2r/(2+r^2)\le1\). For any entire \(A\), the exact homotopy identity proved in the logarithmic-contour lesson is

\[
\frac{\partial}{\partial t}\big[A(\zeta_t)J_t\big]
=\sum_{j=1}^n\frac{\partial}{\partial\xi_j}
 \big[iR\theta_j\ell(\xi)A(\zeta_t)\big].
\tag{3.3}
\]

Take \(A(\zeta)=e^{ix\cdot\zeta}F_u(\zeta)e^{-\varepsilon\sum_j\zeta_j^2}\). Integrate (3.3) over \(t\in[0,1]\) and a real cube \([-T,T]^n\). The boundary terms vanish as \(T\to\infty\). Here is the needed bound: the ordinary compact-support estimate for \(F_u\) is polynomial times \(e^{H_{\operatorname{supp}u}(\operatorname{Im}\zeta_t)}\); both that exponential and the \(x\)-exponential grow at most like a fixed power of \(T\) on the cube faces, since \(\ell=O(\log T)\). The modulus of the Gaussian is

\[
\left|e^{-\varepsilon\sum_j\zeta_{t,j}^2}\right|
=e^{-\varepsilon r^2+\varepsilon t^2R^2\ell(\xi)^2}.
\tag{3.4}
\]

On a face \(r\ge T\), this is bounded by \(e^{-\varepsilon T^2+O(\log^2T)}\), uniformly in \(t\), for fixed \(R,\varepsilon>0\). It dominates the polynomial factors, the face area, and the additional \(\ell\) in the boundary flux. The same bound gives absolute convergence of the interior integrals at each \(t\). Equation (2.2) therefore becomes

\[
u_\varepsilon(x)=(2\pi)^{-n}\int_{\mathbb R^n}
 e^{ix\cdot\zeta_1(\xi)}F_u(\zeta_1(\xi))
 e^{-\varepsilon\sum_j\zeta_{1,j}(\xi)^2}J_1(\xi)\,d\xi.
\tag{3.5}
\]

This was a deformation of an entire integrand with its exact complex Jacobian; it introduced no logarithm of the Fourier transform.

The final contour lies in one of the strips in (1.1). For \(r\ge1\), \(\ell\le2\log(1+r)\), so \(R\ell\le2R\log(1+|\zeta_1|)\). For \(r<1\), \(\ell\le\log3\) and \(|\zeta_1|\ge R\ell\ge2\log2>1\); hence \(R\ell\le R\log3<2R\log(1+|\zeta_1|)\). Thus \(m=\lceil2R\rceil\) suffices for the whole contour.

For \(x\in U\), the Fourier bound and (3.1) now give

\[
\left|e^{ix\cdot\zeta_1}F_u(\zeta_1)\right|
\le C_{\lceil2R\rceil}(1+|\zeta_1|)^N
 e^{-R\delta\ell(\xi)}.
\tag{3.6}
\]

For fixed \(R\), \(1+|\zeta_1|\le c_R(1+r)\), because \(\ell/(1+r)\) is bounded. Multiplication by \(\zeta_1^\alpha\) after an \(x\)-derivative therefore costs at most a factor \(c_{R,\alpha}(1+r)^{|\alpha|}\). The exponential in (3.6) is \((2+r^2)^{-R\delta}\).

The Gaussian has a bound independent of \(0<\varepsilon\le1\):

\[
\left|e^{-\varepsilon\sum_j\zeta_{1,j}^2}\right|
\le e^{B_R},\qquad
B_R=\max\!\left(0,\sup_{r\ge0}
 \{R^2\log^2(2+r^2)-r^2\}\right)<\infty.
\tag{3.7}
\]

Finiteness follows from the subquadratic growth of \(\log^2(2+r^2)\). Choose any integer derivative order \(q\ge0\), then choose \(R\ge2\) such that \(2R\delta>N+q+n+1\). Equations (3.2), (3.6) and (3.7) give an integrable bound for (3.5) and for every derivative through order \(q\), uniformly for \(x\in U\) and \(0<\varepsilon\le1\). Dominated convergence removes the Gaussian and proves convergence in \(C^q\) on every compact subset of \(U\) to

\[
g_R(x)=(2\pi)^{-n}\int_{\mathbb R^n}
 e^{ix\cdot\zeta_1(\xi)}F_u(\zeta_1(\xi))J_1(\xi)\,d\xi.
\tag{3.8}
\]

Uniformity follows by taking the supremum of the absolute difference on each compact \(x\)-set inside the same integrable bound; the Gaussian factor tending to one is independent of \(x\). The derivative integrals also show that \(g_R\) is \(C^q\).

Since \(u_\varepsilon\to u\) in distributions, \(g_R\) represents \(u\) on \(U\). Different choices of \(R\) give the same representative: two continuous functions representing the same distribution agree almost everywhere, then everywhere. For each \(q\) we can choose \(R\) large enough, so this representative is smooth. The point \(x_0\notin K\) was arbitrary. Therefore \(\operatorname{sing\,supp}u\subset K\), completing Theorem 1.1. \(\square\)

## 4. The hull recovered from all logarithmic profiles

Use the family \(\mathcal J(u)\) of support functions defined and proved in the preceding joint-frequency lesson. Each member comes from an escaping real frequency sequence and either a proper PSH profile or the collapsed profile. Let \(S=\operatorname{sing\,supp}u\).

**Theorem 4.1.** With \(H_\varnothing\equiv-\infty\),

\[
H_{\operatorname{conv}S}(\eta)
=\sup_{h\in\mathcal J(u)}h(\eta)
\qquad(\eta\in\mathbb R^n).
\tag{4.1}
\]

Equivalently, when \(S\ne\varnothing\), its convex hull is the closed convex hull of the union of the compact sets associated with the proper profiles.

The convex hull of a nonempty compact set in \(\mathbb R^n\) is compact. To recall why without presupposing a closure, a convex combination with more than \(n+1\) points has a linear dependence among their augmented vectors \((x_j,1)\). The dependence has coefficients of both signs, since their sum is zero. Subtract a multiple of it from the nonnegative combination coefficients, choosing the largest multiple that keeps them nonnegative. At least one coefficient becomes zero, while the sum and the represented point stay unchanged. Repeating gives at most \(n+1\) points. The convex hull is therefore the continuous image of the compact product of \(n+1\) copies of the set and the coefficient simplex, and is compact.

**Proof of the upper inequality.** If \(S\ne\varnothing\), use Theorem 1.1 with \(K=\operatorname{conv}S\). On a compact observation set \(|z|\le A\), the points \(\zeta=\xi+(\log|\xi|)z\) eventually belong to the strip with some fixed integer \(m>A+1\): \(|\zeta|\ge|\xi|-A\log|\xi|\), while \(|\operatorname{Im}\zeta|\le A\log|\xi|\). Dividing the logarithm of (1.1) by \(\log|\xi|\) gives, uniformly on that observation set,

\[
L_u(z,\xi)\le N+H_K(\operatorname{Im}z)+o(1).
\tag{4.2}
\]

Every proper profile limit therefore obeys \(v(z)\le N+H_K(\operatorname{Im}z)\). As in the preceding compactness proof, local \(L^1\) convergence gives this almost everywhere, and positive radial recovery gives it at every point. Taking the horizontal envelope and then its recession proves \(h_v\le H_K\). The collapsed function also satisfies this inequality. Thus the right side of (4.1) is at most its left side.

If \(S=\varnothing\), \(u\) is compact smooth, so the preceding smooth-collapse lemma makes \(\mathcal J(u)=\{-\infty\}\). Both sides of (4.1) are identically \(-\infty\), including at \(\eta=0\). This covers the zero distribution too.

**Proof of the reverse inequality.** Suppose \(S\ne\varnothing\). There must be a proper profile. Otherwise failure of arbitrary rapid real decay would supply an escaping sequence \(\xi_j\) and a finite \(A\) such that \(L_u(0,\xi_j)\ge-A\). To justify that implication precisely, if \(F_u\) were not bounded by every inverse polynomial, for some integer \(p\) the quantity \((1+|\xi|)^p|F_u(\xi)|\) would be unbounded. It is bounded on finite balls, so choose an escaping sequence on which it exceeds 1. Dividing its logarithm gives a fixed finite lower bound for \(L_u(0,\xi_j)\), eventually for example \(-2p\). Such a sequence cannot have a locally uniform collapsed extraction, so PSH compactness supplies a proper profile. If every profile were collapsed, therefore, \(F_u\) would have arbitrary rapid real decay and Lemma 2.1 would make \(S\) empty, a contradiction.

Let \(D\) be the closed convex hull of the union of all proper profile sets. It is nonempty. Every such set lies inside a fixed compact convex carrier \(K_0\) of \(u\), by the preceding compactness theorem. Hence \(D\subset K_0\) and is compact. Set

\[
G(\eta)=H_D(\eta)=\sup_{h\in\mathcal J(u)}h(\eta).
\tag{4.3}
\]

Equality holds because convex combinations and closure do not change a supremum of continuous linear functionals, and the collapsed member contributes nothing to a nonempty finite supremum. In particular \(G\) is finite and continuous.

Choose an ordinary compact-support Fourier bound of polynomial order \(M\) for \(u\). Every proper profile \(v\) satisfies \(v(x)\le M\) on the real plane by the preceding compactness theorem, so its finite horizontal envelope has \(M_v(0)\le M\). The proved envelope increment inequality then gives

\[
v(z)\le M_v(\operatorname{Im}z)
\le M_v(0)+h_v(\operatorname{Im}z)
\le M+G(\operatorname{Im}z).
\tag{4.4}
\]

We show that the strip estimate (1.1) holds with \(K=D\) and exponent \(M+1\). If it failed for a fixed \(m\), the continuous ratio
\(|F_u(\zeta)|(1+|\zeta|)^{-M-1}e^{-G(\operatorname{Im}\zeta)}\)
would be unbounded on that strip. It is bounded on each compact set, so choose \(\zeta_j=\xi_j+i\eta_j\) with \(|\zeta_j|\to\infty\), inside the strip, and ratio greater than \(j\).

The strip condition implies \(|\eta_j|/|\zeta_j|\to0\), because \(\log(1+|\zeta_j|)/|\zeta_j|\to0\). Therefore \(R_j=|\xi_j|\to\infty\), \(R_j/|\zeta_j|\to1\), and
\(z_j=i\eta_j/\log R_j\) eventually lies in the compact ball \(|z|\le m+1\). At these moving observation points the failed bound gives

\[
L_u(z_j,\xi_j)-G(\operatorname{Im}z_j)
>(M+1)\frac{\log(1+|\zeta_j|)}{\log R_j}
 +\frac{\log j}{\log R_j}>M+1.
\tag{4.5}
\]

Extract a profile limit from this real sequence. If it collapses, the left side is eventually arbitrarily negative on that compact ball, since \(G\) is continuous there. If it is proper, (4.4) and the [proved Hartogs compact comparison](../../AN02-L143.html#hartogs-compact-comparison), with continuous comparison function \(G(\operatorname{Im}z)\), give
\(\limsup_j\sup_{|z|\le m+1}(L_u(z,\xi_j)-G(\operatorname{Im}z))\le M\).
Both conclusions contradict (4.5).

Thus all strip bounds hold. Theorem 1.1 makes \(S\subset D\), whence \(\operatorname{conv}S\subset D\). The upper inequality already showed every proper profile set contained in \(\operatorname{conv}S\), by support-function separation. Their closed convex hull \(D\) is contained there too. The two compact convex sets are equal, proving (4.1). \(\square\)

The equality identifies a convex hull. It does not prove that every singular point lies in the unconvexified closed union of profile sets. That finer localization assertion requires an additional argument.

## 5. A nonzero polynomial cannot change the compact singular hull

**Theorem 5.1.** For every nonzero complex polynomial \(P\) and compact distribution \(u\),

\[
\operatorname{conv}\operatorname{sing\,supp}u
=\operatorname{conv}\operatorname{sing\,supp}P(D)u.
\tag{5.1}
\]

In particular, if \(P(D)u\) is smooth, then \(u\) is smooth. Compact support and \(P\ne0\) are part of the assertion.

**Proof.** Put \(f=P(D)u\); distributional differentiation gives the entire identity \(F_f(\zeta)=P(\zeta)F_u(\zeta)\). The radius-two division lemma gives a fixed constant \(A_P\) and, for nonconstant \(P\), a real unit vector \(\theta\) such that

\[
|F_u(\zeta)|\le A_P\sup_{|t|\le2}|F_f(\zeta+t\theta)|.
\tag{5.2}
\]

This is exactly the previously proved bound obtained by applying its root-avoiding circle to \(t\mapsto P(\zeta+t\theta)\) and the entire function \(t\mapsto F_u(\zeta+t\theta)\). Its leading coefficient \(P_{\deg P}(\theta)\) is independent of \(\zeta\). A nonzero constant \(P\) uses the immediate scalar bound instead.

If \(f\) is compact smooth, its whole-complex arbitrary polynomial decay bounds \(F_f(\xi+t\theta)\) by \(B_L(1+|\xi|)^{-L}\), uniformly for \(|t|\le2\) and real \(\xi\). The imaginary exponential is bounded on that radius-two displacement. Equation (5.2) makes \(F_u\) arbitrarily rapidly decreasing on the real plane. Lemma 2.1 gives compact smooth \(u\). Both singular supports are empty, proving this case.

Otherwise let \(K=\operatorname{conv}\operatorname{sing\,supp}f\), a nonempty compact convex set. Theorem 1.1 gives its strip estimates for \(F_f\), with one fixed exponent \(N\). These estimates transfer through (5.2).

Indeed, suppose \(|\operatorname{Im}\zeta|\le m\log(1+|\zeta|)\), and put \(w=\zeta+t\theta\), \(|t|\le2\). If \(|\zeta|\ge4\), then \(1+|w|\ge|\zeta|-1\ge(1+|\zeta|)/2\), and \(1+|w|\ge3\). Hence

\[
|\operatorname{Im}w|
\le m\log(1+|w|)+m\log2+2
\le(2m+3)\log(1+|w|).
\tag{5.3}
\]

The last inequality follows from \((m+3)\log3\ge m\log2+2\), for \(m\ge1\). Also

\[
1+|w|\le3(1+|\zeta|),\qquad
H_K(\operatorname{Im}w)
\le H_K(\operatorname{Im}\zeta)+2r_K,\qquad
r_K=\max_{x\in K}|x|.
\tag{5.4}
\]

Apply the \(2m+3\) strip estimate for \(f\) throughout the supremum in (5.2). It gives the \(m\) strip estimate for \(u\) with the same exponent \(N\), and constant at most
\(A_P3^Ne^{2r_K}C_{2m+3}\) on \(|\zeta|\ge4\). The remaining compact ball has a finite bound for the continuous weighted ratio and is absorbed into the constant.

Theorem 1.1 now gives \(\operatorname{sing\,supp}u\subset K\), hence its convex hull is contained in \(K\). Conversely differentiation of a smooth local representative stays smooth, so \(\operatorname{sing\,supp}f\subset\operatorname{sing\,supp}u\). Taking convex hulls proves the opposite inclusion and therefore equality. \(\square\)

The assertion addresses the singular hull of a compact distribution, including complex coefficients and polynomial characteristic zeros. It is separate from ordinary support-hull invariance and from regularity of arbitrary noncompact solutions.

## References

1. Terence Tao, [*246B, Notes 2: Some connections with the Fourier transform*](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), *What's New*, 23 January 2021. Background on Fourier transforms, complex contours and Paley–Wiener growth.
2. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983; second edition 1990; reprint 2003. The logarithmic-strip singular-support criterion and compact polynomial singular-hull invariance are classical.
3. Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983; second revised printing 1990; reprint 2005. The hull interpretation through logarithmic-frequency profiles is classical.
