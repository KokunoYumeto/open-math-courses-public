# Fourier transforms of analytic functionals on a real convex carrier

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

An analytic functional can have infinite differential order at a point. Its Fourier transform therefore need not have polynomial growth on real frequencies. The exact replacement is an arbitrarily small exponential loss, with a different constant allowed for each loss. We prove both directions of this criterion, the uniqueness statement, and the compatibility of the complex-neighborhood distribution representatives used in the construction.

Our convention is a complex-linear pairing and the negative-exponential forward transform. The dot product in a complex exponential is bilinear, without conjugation. Lengths on complex spaces are Euclidean lengths on their underlying real spaces.

The two substantive earlier inputs are [L145, E2, the proved holomorphic extension growth corollary](../../AN02-L145.html#extension-growth-corollary), and [L122, Theorem CF2.1, the full compact-distribution Fourier criterion](../../AN02-L122.html#2-the-compact-support-growth-criterion). The latter includes both growth-to-support and uniqueness, with the same forward-transform convention. Its use below is in real dimension \(2n\), not \(n\). The product Cauchy formula and uniform joint power series are proved in [L145 E3](../../AN02-L145.html#distributional-holomorphic-regularity). Smooth cutoffs and finite-order bounds for compact distributions are the written distribution foundations used in CF2.1. Every new carrier, compatibility and uniqueness step is given here.

<a id="analytic-functional-definition"></a>

## AF1. The definition and the exact theorem

Let \(n\geq1\) and let \(K\subset\mathbb R^n\subset\mathbb C^n\) be a nonempty compact convex set. It may be a point or lie in a proper affine subspace. Define its support function and radius by

\[
h_K(\eta)=\max_{a\in K}a\cdot\eta,
\qquad R_K=\max_{a\in K}|a|.
\tag{AF1}
\]

Write \(\mathcal A(\mathbb C^n)\) for the entire holomorphic functions. An **analytic functional carried by \(K\)** is a complex-linear map \(u:\mathcal A(\mathbb C^n)\to\mathbb C\) such that, for every open complex neighborhood \(\Omega\supset K\), a finite constant \(C_\Omega\) satisfies

\[
|u(h)|\leq C_\Omega\sup_{z\in\Omega}|h(z)|
\quad(h\in\mathcal A(\mathbb C^n)).
\tag{AF2}
\]

This space is denoted \(\mathcal A'(K)\). It suffices to check bounded neighborhoods: each neighborhood of the compact set contains a smaller bounded one. A supremum that is infinite gives no restriction, but all sufficiently small bounded neighborhoods must still have their own finite constants. We initially define \(u\) on entire tests, exactly as in the cited definition. An action on holomorphic germs will be a proved consequence for the convex real carrier, not an additional assumption.

<a id="analytic-functional-fourier-theorem"></a>

**Theorem AF1.** The map

\[
\widehat u(\zeta)=u\bigl(z\mapsto e^{-iz\cdot\zeta}\bigr)
\tag{AF3}
\]

is a bijection between \(\mathcal A'(K)\) and the entire functions \(F\) satisfying

\[
\text{for every }\varepsilon>0\text{ there is }C_\varepsilon<\infty:
\quad
|F(\zeta)|\leq C_\varepsilon
\exp\bigl(h_K(\operatorname{Im}\zeta)+\varepsilon|\zeta|\bigr)
\quad(\zeta\in\mathbb C^n).
\tag{AF4}
\]

The constant may depend on \(\varepsilon\). In particular, (AF4) asserts neither polynomial growth on the real axis nor one constant uniform as \(\varepsilon\downarrow0\). The support function can be negative; we keep its exact sign.

## AF2. Entire dependence and all holomorphic moments

Fix a bounded neighborhood \(\Omega\) of \(K\). On \(\Omega\), the exponential has, for \(\zeta=\zeta_0+w\), the series

\[
e^{-iz\cdot(\zeta_0+w)}
=e^{-iz\cdot\zeta_0}
\sum_{\alpha\in\mathbb N^n}
\frac{(-iz)^\alpha w^\alpha}{\alpha!}.
\tag{AF5}
\]

It is absolutely and uniformly convergent for \(z\in\Omega\) and \(w\) in any fixed bounded polydisc: bound each coordinate of \(z\) by a fixed number and multiply the ordinary exponential majorants. The same applies to any fixed parameter derivative. The bound (AF2) permits applying \(u\) to the partial sums and passing to the limit, uniformly on the parameter polydisc. Consequently \(\widehat u\) has a convergent joint power series about every \(\zeta_0\), and

\[
\partial_\zeta^\alpha\widehat u(0)
=(-i)^{|\alpha|}u(z^\alpha).
\tag{AF6}
\]

Thus the Fourier transform determines every holomorphic polynomial moment. If \(\widehat u=0\), all these moments vanish. For any entire \(h\), its Taylor polynomials about the origin converge uniformly on the bounded set \(\Omega\), by the product Cauchy expansion on a larger polydisc. Applying (AF2) shows \(u(h)=0\). This proves injectivity on the actual entire-test space.

## AF3. The precise forward growth bound

For \(\varepsilon>0\), take

\[
\Omega_\varepsilon=\{z:\operatorname{dist}(z,K)<\varepsilon\}.
\tag{AF7}
\]

It is a bounded complex neighborhood. Write \(\zeta=\xi+i\eta\). For \(z\in\Omega_\varepsilon\), choose \(a\in K\) and write \(z=a+p+iq\) with \(\sqrt{|p|^2+|q|^2}<\varepsilon\). Direct multiplication gives

\[
\operatorname{Re}(-iz\cdot\zeta)
=a\cdot\eta+p\cdot\eta+q\cdot\xi
\leq h_K(\eta)+\varepsilon\sqrt{|\xi|^2+|\eta|^2}.
\tag{AF8}
\]

Use (AF2) with this neighborhood and the exponential test to obtain (AF4). No derivative bound or distribution order is assumed.

<a id="complex-thickening-and-diagonal"></a>

## AF4. A convex complex thickening and its diagonal weight

Now let \(F\) be an entire function satisfying (AF4). Fix \(\varepsilon>0\). Identify \(z=x+iy\in\mathbb C^n\) with \((x,y)\in\mathbb R^{2n}\), and set

\[
L_\varepsilon=(K\times\{0\})+
\varepsilon\overline B_{\mathbb R^{2n}}(0,1).
\tag{AF9}
\]

This is the closed Euclidean \(\varepsilon\)-neighborhood of the real set \(K\) in \(\mathbb C^n\). To verify the equality, minimizing distance to \(K\) is possible by compactness, and the residual vector then has length at most \(\varepsilon\). It is nonempty, compact and convex. Maximizing independently over the two summands gives its exact real support function:

\[
h_{L_\varepsilon}(\eta_1,\eta_2)
=h_K(\eta_1)+\varepsilon\sqrt{|\eta_1|^2+|\eta_2|^2}.
\tag{AF10}
\]

On \(\mathbb C^{2n}\), whose complex coordinate blocks are \(Z=(\zeta_1,\zeta_2)\), define

\[
\Phi_\varepsilon(Z)
=h_{L_\varepsilon}(\operatorname{Im}\zeta_1,
                       \operatorname{Im}\zeta_2).
\tag{AF11}
\]

It is finite and continuous. It is PSH, with a direct circle proof. At the center of any disk in any complex affine line, choose a maximizer \(\ell\in L_\varepsilon\) for the support function. The real linear function \(\ell\cdot\operatorname{Im}Z\) is harmonic along that line, so its circle average equals its value at the center. On the circle it is at most \(\Phi_\varepsilon\). This proves the submean inequality at the center. Continuity supplies upper semicontinuity. Equivalently, the weight is a convex function of the imaginary coordinates.

The inequality \(|h_K(\eta)-h_K(\widetilde\eta)|\leq R_K|\eta-\widetilde\eta|\), proved by taking the maximizing linear functions in turn, and the triangle inequality for the Euclidean norm give

\[
|\Phi_\varepsilon(Z)-\Phi_\varepsilon(\widetilde Z)|
\leq(R_K+\varepsilon)|Z-\widetilde Z|.
\tag{AF12}
\]

Because \(R_K+\varepsilon>0\), this is exactly the strict unit-oscillation hypothesis of L145 E2 when \(|Z-\widetilde Z|<1\).

The complex linear graph

\[
W=\{(\zeta,i\zeta):\zeta\in\mathbb C^n\}
\subset\mathbb C^{2n}
\tag{AF13}
\]

has complex dimension \(n\) and codimension \(n\). For \(\zeta=\xi+i\eta\), its real-coordinate chart is \((\xi,\eta,-\eta,\xi)\). In particular,

\[
\operatorname{Im}(\zeta,i\zeta)=(\eta,\xi),\quad
\Phi_\varepsilon(\zeta,i\zeta)=h_K(\eta)+\varepsilon|\zeta|,
\quad |(\zeta,i\zeta)|=\sqrt2|\zeta|.
\tag{AF14}
\]

The induced real volume in this graph chart is \(2^n\,dV(\zeta)\), since the metric is twice the identity in real dimension \(2n\). The growth corollary does not require an original square integral in this chart; its pointwise hypothesis is precisely (AF4).

## AF5. Extension, then a distribution in real dimension twice as large

Apply L145 E2 to the entire function \((\zeta,i\zeta)\mapsto F(\zeta)\) on \(W\), with ambient complex dimension \(2n\), codimension \(n\), and weight \(\Phi_\varepsilon\). It supplies an entire \(G_\varepsilon\) with

\[
G_\varepsilon(\zeta,i\zeta)=F(\zeta),\qquad
|G_\varepsilon(Z)|\leq A_\varepsilon(1+|Z|)^{4n+1}
e^{h_{L_\varepsilon}(\operatorname{Im}Z)}.
\tag{AF15}
\]

The exponent is the proved choice \(2n+2n+1\); no optimality is claimed. The constant is finite for the fixed \(\varepsilon\).

L122 CF2.1, now in real dimension \(2n\), gives a compact distribution \(T_\varepsilon\) with

\[
\operatorname{supp}T_\varepsilon\subset L_\varepsilon,
\qquad
G_\varepsilon(\zeta_1,\zeta_2)
=T_\varepsilon\bigl(e^{-i(x\cdot\zeta_1+y\cdot\zeta_2)}\bigr).
\tag{AF16}
\]

A compact distribution acts on a smooth function near its support by inserting a smooth cutoff equal to one there. This value does not depend on the cutoff. Restrict (AF16) to the complex graph. The identity

\[
-i\bigl(x\cdot\zeta+y\cdot(i\zeta)\bigr)
=-i(x+iy)\cdot\zeta
\tag{AF17}
\]

proves

\[
T_\varepsilon\bigl((x,y)\mapsto e^{-i(x+iy)\cdot\zeta}\bigr)
=F(\zeta).
\tag{AF18}
\]

There is no assertion that these distributions are carried by \(K\) in real \(n\)-dimensional distribution theory. Their actual supports lie in complex neighborhoods of \(K\), viewed in real dimension \(2n\).

<a id="representative-compatibility"></a>

## AF6. All the representatives give one functional on entire tests

Differentiating (AF18) is legitimate in the finite smooth seminorms of a compact distribution, exactly as in CF2.1. Thus for every \(\alpha\),

\[
T_\varepsilon\bigl((x+iy)^\alpha\bigr)
=i^{|\alpha|}\partial^\alpha F(0).
\tag{AF19}
\]

If \(\varepsilon,\delta>0\), the compact distribution \(T_\varepsilon-T_\delta\) has all these holomorphic moments zero. Let \(h\) be entire. Its Taylor polynomials converge to \(h(x+iy)\), together with all real derivatives up to any fixed finite order, uniformly on a fixed compact neighborhood of both supports. Here is the derivative justification: on a slightly larger polydisc, the product Cauchy bounds dominate the series geometrically; differentiating a fixed number of times adds only polynomial factors to the indices, still summable on a smaller polydisc. Moreover \(\partial_{x_j}h=\partial_{z_j}h\) and \(\partial_{y_j}h=i\partial_{z_j}h\). The finite-order distribution estimate therefore permits passage to the limit. Every Taylor polynomial pairs to zero, so

\[
T_\varepsilon\bigl(h(x+iy)\bigr)
=T_\delta\bigl(h(x+iy)\bigr).
\tag{AF20}
\]

This also proves independence of the particular extension \(G_\varepsilon\) selected by E2: any other extension with the same diagonal values has the same holomorphic moments and the same entire-test action. Define

\[
u(h)=T_\varepsilon\bigl(h(x+iy)\bigr),
\qquad h\in\mathcal A(\mathbb C^n),
\tag{AF21}
\]

using any one positive \(\varepsilon\). It is one complex-linear functional, independent of every choice just discussed, and (AF18) gives \(\widehat u=F\).

## AF7. The bound on every neighborhood, with all derivative estimates supplied

Let \(\Omega\) be any open complex neighborhood of \(K\). Compactness gives \(\varepsilon>0\) with \(L_\varepsilon\subset\Omega\) and a positive gap to its complement. Choose a smooth compactly supported cutoff \(\chi\) inside \(\Omega\), equal to one near \(L_\varepsilon\). The finite-order estimate of \(T_\varepsilon\), on the fixed compact support of \(\chi\), gives constants \(B\) and an integer \(M\) with

\[
|u(h)|=|T_\varepsilon(\chi h)|
\leq B\max_{|\beta|\leq M}\sup
|\partial_{x,y}^\beta(\chi h)|.
\tag{AF22}
\]

Choose \(r>0\) such that every closed coordinate polydisc of radius \(r\) centered on \(\operatorname{supp}\chi\) lies inside \(\Omega\). Such an \(r\) exists by compactness, reducing it by \(\sqrt n\) when passing from Euclidean distance to a coordinate polydisc. The product Cauchy formula yields

\[
|\partial_z^\alpha h(z)|
\leq\alpha!\,r^{-|\alpha|}\sup_\Omega|h|
\quad(z\in\operatorname{supp}\chi).
\tag{AF23}
\]

For \(\beta=(\beta_x,\beta_y)\), the real derivative is \(i^{|\beta_y|}\partial_z^{\beta_x+\beta_y}h\). Apply the finite Leibniz rule in (AF22), bound the fixed derivatives of \(\chi\), and use (AF23) for every derivative of \(h\) that occurs. Their orders are at most \(M\). This gives a finite \(C_\Omega\) such that (AF2) holds. If \(\sup_\Omega|h|=\infty\), the inequality is automatic; otherwise the preceding argument applies verbatim. We have proved \(u\in\mathcal A'(K)\), and AF2 already proved its uniqueness. This completes Theorem AF1. \(\square\)

![The complex carrier thickening and the exact diagonal coordinates](figures/complex-carrier-and-diagonal.png)

The left diagram is the exact \(n=1\), \(K=[-1,1]\), \(\varepsilon=1/2\) carrier in the complex \(z=x+iy\) plane. The right diagram is the original frequency plane \(\zeta=\xi+i\eta\), with the full four-real-coordinate graph map written explicitly. It is not a spatial projection of that four-dimensional graph. Both panels concern the construction in AF4–AF7.

<a id="holomorphic-germ-action"></a>

## AF8. The action on holomorphic germs, proved for this convex carrier

We give the additional compatibility needed when a test is holomorphic only near \(K\). First prove the following elementary convex-carrier fact.

**Lemma AF8.** Let \(L\subset\mathbb C^n\) be nonempty compact and convex as a real set. If a compact distribution \(V\) on \(\mathbb R^{2n}\), supported in \(L\), vanishes on all holomorphic polynomials, then it vanishes on every function holomorphic in a neighborhood \(D\) of \(L\).

Choose \(a\in L\) and set

\[
\Lambda=\{\lambda\in\mathbb C:
a+\lambda(L-a)\subset D\},
\qquad h_\lambda(z)=h(a+\lambda(z-a)).
\tag{AF24}
\]

The set \(\Lambda\) is open: at any of its points, the compact image of \(L\) has a positive gap inside \(D\), and multiplication depends continuously on \(\lambda\). Convexity implies \([0,1]\subset\Lambda\). For \(\lambda\) near a fixed \(\lambda_0\in\Lambda\), the functions \(h_\lambda\) are defined on a common neighborhood of \(L\). Insert one common cutoff there. Their dependence on \(\lambda\) is holomorphic in every finite smooth seminorm: Cauchy expansion in the parameter on a slightly larger parameter disk, and the spatial derivative bounds on a compact neighborhood, give uniform convergence of the series and of its finitely many spatial derivatives. Hence \(\lambda\mapsto V(h_\lambda)\) is holomorphic near \(\lambda_0\).

For \(|\lambda|\) small, the Taylor series of \(h\) about \(a\) converges with the required finite derivatives uniformly near \(L\) after the dilation. Its terms are holomorphic polynomials in \(z\), so \(V(h_\lambda)=0\) near zero. The ordinary one-variable identity principle makes it zero on the connected component of \(\Lambda\) containing \([0,1]\). Explicitly, a nonzero power series about a zero has a first nonzero coefficient and factors as a power of the coordinate times a nonvanishing function on a small disk, so that zero is isolated. A limit point of zeros inside the domain must consequently have the zero power series. The set of points with a zero neighborhood is therefore both open and closed in the connected component and is nonempty here. At \(\lambda=1\), this gives \(V(h)=0\), proving the lemma.

Now let \(h\) be holomorphic in \(D\supset K\). Choose \(\varepsilon\) with \(L_\varepsilon\subset D\) and define \(u_D(h)=T_\varepsilon(h(x+iy))\). For two admissible radii, both supports lie in the larger of their nested convex thickenings, which is still inside \(D\). Their difference has zero polynomial moments by (AF19). Lemma AF8 proves that both choices have the same action. Different representatives give the same result by the same argument. If two holomorphic functions agree on some neighborhood of \(K\), choose a smaller thickening inside that neighborhood; their values agree. We therefore obtain a linear action on holomorphic germs at \(K\). The Cauchy estimate argument of AF7 applies to local holomorphic functions as well, giving (AF2) on every neighborhood where the representative is defined.

For completeness, this continuous germ action is unique. If two such actions agree on entire tests, their difference \(v\) vanishes on polynomials. For a local \(h\), use (AF24) with \(L=K\). Near each parameter value the functions \(h_\lambda\) are holomorphic on a common neighborhood of \(K\). Choose a smaller bounded neighborhood with closure in it; uniform Cauchy expansion in \(\lambda\), together with the neighborhood bound for \(v\), makes \(v(h_\lambda)\) holomorphic. For small \(\lambda\), Taylor polynomials about \(a\) converge uniformly there, so it is zero. The identity principle along \([0,1]\) gives \(v(h)=0\). This proves uniqueness without assuming a general approximation theorem for an arbitrary complex carrier. This argument establishes the local-test conclusion for the convex carrier used here; it is not a proof of the more general nonconvex real-carrier approximation proposition.

<a id="infinite-order-point-functional"></a>

## AF9. An actual infinite-order point functional

In one complex variable, define

\[
u_0(h)=\sum_{m=0}^\infty
\frac{i^m}{(m!)^2}h^{(m)}(0).
\tag{AF25}
\]

For any neighborhood \(\Omega\) of zero, choose \(r>0\) whose closed disk lies inside \(\Omega\). Cauchy's estimate gives absolute convergence and

\[
|u_0(h)|\leq\sup_{|z|\leq r}|h(z)|
\sum_{m=0}^\infty\frac{r^{-m}}{m!}
=e^{1/r}\sup_{|z|\leq r}|h(z)|.
\tag{AF26}
\]

Thus \(u_0\in\mathcal A'(\{0\})\). Its Fourier transform is

\[
F_0(\zeta)=\sum_{m=0}^\infty\frac{\zeta^m}{(m!)^2}.
\tag{AF27}
\]

It is entire by the ratio bound on bounded disks. With \(s=\sqrt{|\zeta|}\), the nonnegative double sum \(e^s e^s\) contains its diagonal subseries, so

\[
|F_0(\zeta)|\leq e^{2\sqrt{|\zeta|}}
\leq e^{1/\varepsilon}e^{\varepsilon|\zeta|}
\quad(\varepsilon>0).
\tag{AF28}
\]

The second inequality is \(2\sqrt t\leq\varepsilon t+1/\varepsilon\), obtained by expanding \((\sqrt{\varepsilon t}-1/\sqrt\varepsilon)^2\geq0\).

It is not the action of a distribution supported at zero. Here is the needed finite-jet argument, without citing a point-support structure theorem. Let \(T\) have support \(\{0\}\) and finite order \(M\) on a fixed compact neighborhood. For any smooth test, subtract its Taylor polynomial of total degree \(M\) at zero to get a remainder \(R\). For a fixed cutoff \(\chi\) equal to one near zero, set \(\chi_t(x)=\chi(x/t)\). Taylor's remainder estimate and the Leibniz rule give

\[
\max_{|\beta|\leq M}\sup
|\partial^\beta(\chi_tR)|=O(t)
\quad(t\downarrow0).
\tag{AF29}
\]

Indeed a term with total derivative order \(|\beta|\) is bounded by a constant times \(t^{M+1-|\beta|}\). The support property gives \(T(R)=T(\chi_tR)\), and its finite-order estimate makes this value tend to zero. Hence \(T\) depends only on the jet through order \(M\). This proof works in real dimension one or two. But

\[
u_0(z^m)=\frac{i^m}{m!}\ne0
\quad\text{for every }m,
\tag{AF30}
\]

whereas \(z^m\) has zero real jet through order \(M\) when \(m>M\). No point-supported distribution can represent \(u_0\). Consistently, \(F_0(x)\) is not polynomially bounded for \(x>0\): for any proposed degree \(N\), choose an integer \(m>N\); the single positive term \(x^m/(m!)^2\) exceeds every constant multiple of \((1+x)^N\) eventually.

An independent real-integral expression will check the plotted series numerically. With \(s=\sqrt x\), expand \(e^{s e^{it}}e^{s e^{-it}}\); the double series is absolutely uniform in \(t\). Integrating a term around the circle gives zero unless its two indices agree. Therefore

\[
F_0(x)=\frac1{2\pi}\int_0^{2\pi}e^{2\sqrt x\cos t}\,dt
\quad(x\geq0).
\tag{AF31}
\]

This identity is not needed for existence of the analytic functional. It supplies a genuinely different calculation for the numerical checks.

![Subexponential growth, with the constants and the exact positive-term obstruction](figures/infinite-order-point-growth.png)

The plotted function is the actual convergent positive series (AF27) on positive real frequencies. The curves identified as upper bounds are (AF28). A displayed single-term lower bound is one exact term of the positive series, not an asymptotic approximation. The plot is an illustration; the proofs of arbitrarily small exponential type and failure of every polynomial bound are the exact arguments above.

## AF10. Quantifiers, translation and exclusions

If \(a\in\mathbb R\), translating the preceding functional gives

\[
u_a(h)=\sum_{m=0}^\infty\frac{i^m}{(m!)^2}h^{(m)}(a),
\qquad \widehat u_a(\zeta)=e^{-ia\zeta}F_0(\zeta),
\qquad h_{\{a\}}(\eta)=a\eta.
\tag{AF32}
\]

The signed support term is retained, including when it is negative. A single exponential-loss estimate would not suffice: for \(a\ne0\), the function \(e^{-ia\zeta}\) satisfies a bound with \(K=\{0\}\) and loss \(|a|\), but fails (AF4) for \(\varepsilon<|a|\), along \(\zeta=it\operatorname{sgn}(a)\).

The real-carrier hypothesis matters. Evaluation at a nonreal point \(ib\), \(b\ne0\), is an analytic functional with that complex point as a carrier and transform \(e^{b\zeta}\). It cannot satisfy (AF4) for any compact real \(K\): along the real frequency ray of the sign of \(b\), \(h_K(0)=0\) and any \(\varepsilon<|b|\) gives a contradiction. We have not asserted this theorem for arbitrary complex carriers.

If a single constant \(C\) works for all \(\varepsilon>0\) in (AF4), taking \(\varepsilon\downarrow0\) at each fixed \(\zeta\) gives \(|F(\zeta)|\leq C e^{h_K(\operatorname{Im}\zeta)}\). CF2.1 then supplies a distribution supported in \(K\). This is a stronger hypothesis than the theorem; neither a common constant nor a real-carrier distribution representative is supplied in general.

The empty-carrier case is just the zero functional. With the convention that the supremum over the empty neighborhood is zero, its defining bound forces this. The support-function statement above is formulated for nonempty \(K\), so it does not assign a finite support function to the empty set.

## Exact human-source comparison and scope

Theorem AF1 matches Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.1, Theorem 15.1.5, printed p. 276, 1983 edition, second revised printing 1990, reprint 2005. The initial entire-test definition is Hörmander I, Definition 9.1.1, printed p. 326, 1983 edition, second edition 1990, reprint 2003. The distinction between that definition and subsequent local holomorphic tests is visible in I, Proposition 9.1.2 and its following conclusion, printed pp. 327–328. AF8 gives a separate direct proof for the convex carrier needed here, with its stated scope.

Our proof fills in the joint analyticity, exact graph metric and coordinates, PSH and global oscillation checks, diagonal sign, independence of representatives, every-neighborhood continuity, uniqueness and infinite-order example. It uses actual earlier course proofs of II, Corollary 15.1.4 and I, Theorem 7.3.1 through L145 E2 and L122 CF2.1. Protected native book text and page images are private reading evidence and are absent from the distributable original packet. This proves the stated analytic-functional target, not the remaining Chapter 15 weighted Fourier estimates or the entire course.
