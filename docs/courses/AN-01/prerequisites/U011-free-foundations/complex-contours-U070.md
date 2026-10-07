# Cauchy integrals, zeros and contour indices

*Selected AN-03 programme proof; CC0 1.0. Original ownership is retained. See [licence](https://creativecommons.org/publicdomain/zero/1.0/), [rights](notices/RIGHTS.md), and selection history.*

The [scalar calculus and topology](metric-foundation-bridges.md), §§12–13, [finite algebra](stable-prerequisite-bridges.md), §§10.1–10.6, and [integration proofs](banach-foundation-bridges.md), §§15.0–15.1 and 16, supply the stated foundational inputs.

### 16.1. The actual contour integral and triangle theorem

Let \(\Omega\subset\mathbb C\) be open. Holomorphic means complex differentiable at every point of \(\Omega\); continuity of the derivative is not assumed. A contour is a finite concatenation of continuously differentiable maps \(\gamma:[a,b]\to\Omega\). Its integral is the original oriented Riemann integral

\[
\int_\gamma f(\zeta)\,d\zeta
 =\int_a^b f(\gamma(t))\gamma'(t)\,dt,\qquad
\left|\int_\gamma f\,d\zeta\right|
 \leq \sup_{\gamma([a,b])}|f|\int_a^b|\gamma'(t)|\,dt.
\tag{CX1}
\]

This is defined for continuous \(f\). The real and imaginary coordinate integrals, their triangle inequality and the limit of Riemann sums prove the bound. Reversing the original parameter endpoints reverses the sign. Concatenation adds the integrals, including their endpoints. A continuously differentiable increasing reparameterization retains its derivative factor by substitution; reversing the orientation changes its sign. These assertions apply to each piece separately. A zero-length piece contributes zero.

For an oriented triangle \(T\) whose closed interior lies in \(\Omega\), let \(I(T)=\int_{\partial T}f\,d\zeta\). Join the side midpoints, forming four triangles with the inherited positive orientation. Each interior edge occurs twice with opposite orientation, so \(I(T)\) is the sum of their four boundary integrals. Choose a child whose integral has modulus at least \(|I(T)|/4\), then repeat. At each step choose the first child in a fixed finite ordering satisfying that inequality; no additional infinite-choice assumption is needed. The resulting closed triangles \(T_k\) are nested, with diameter \(2^{-k}d\) and perimeter \(2^{-k}L\), where \(d,L\) are the original diameter and perimeter. Compactness gives a common point \(z_*\), and the shrinking diameter makes it unique.

Complex differentiability at \(z_*\) gives

\[
f(\zeta)=f(z_*)+f'(z_*)(\zeta-z_*)
                 +(\zeta-z_*)\epsilon(\zeta),\qquad
\epsilon(\zeta)\longrightarrow0\quad(\zeta\longrightarrow z_*).
\tag{CX2}
\]

The boundary integrals of the first two terms are zero: the fundamental theorem on each side evaluates the respective primitives \(f(z_*)\zeta\) and \(f'(z_*)(\zeta-z_*)^2/2\), and the endpoint values cancel. Therefore CX1 gives

\[
|I(T)|\leq4^k|I(T_k)|
\leq dL\sup_{\zeta\in T_k}|\epsilon(\zeta)|
\longrightarrow0.
\tag{CX3}
\]

Thus every such triangle integral is zero. A degenerate triangle has zero integral directly by cancellation of its collinear oriented sides. No real partial derivative or continuity of \(f'\) has been used.

There is a point-removal version needed below. Suppose \(g\) is continuous on a disk and holomorphic except possibly at one point \(w\). Its triangle integrals are still zero. For a triangle having \(w\) as a vertex, remove the homothetic small triangle of ratio \(\delta>0\) at that vertex. The remaining quadrilateral splits into two triangles avoiding \(w\), whose integrals vanish by CX3. Interior-edge cancellation makes the original integral equal the small triangle integral. On its compact neighborhood \(g\) is bounded, so CX1 bounds this by \(\delta L\sup|g|\), tending to zero. If \(w\) is inside a triangle, split it into the three triangles joining \(w\) to its vertices. If it is on an edge, split into the two triangles with \(w\) as a vertex. Opposite internal sides cancel in both cases. If \(w\) is outside, CX3 already applies.

For any continuous \(g\) with zero triangle integrals on a disk centered at \(a\), define \(F(z)=\int_{[a,z]}g\,d\zeta\) on that disk. The triangle with vertices \(a,z,z+h\) gives

\[
F(z+h)-F(z)=h\int_0^1g(z+th)\,dt,\qquad F'(z)=g(z).
\tag{CX4}
\]

Continuity makes the quotient tend to \(g(z)\). The complex derivative is also the real coordinate derivative, since the remainder is \(o(|h|)\). Along every contour piece the already proved real chain rule gives \((F\circ\gamma)'=g(\gamma)\gamma'\). Consequently every closed contour in this disk has integral zero. This applies to the point-removal function as well; it does not assume in advance that the derivative of a holomorphic function is holomorphic.

### 16.2. The circle formula, every coefficient and both continuation principles

Let the closed disk \(|\zeta-a|\leq R\) lie in \(\Omega\), and let \(|z-a|<R\). Set

\[
g(\zeta)=
 \begin{cases}
 (f(\zeta)-f(z))/(\zeta-z),&\zeta\ne z,\\
 f'(z),&\zeta=z.
 \end{cases}
\tag{CX5}
\]

It is continuous at \(z\) by complex differentiability and holomorphic elsewhere by the proved field/product rules. The point-removal argument and CX4 give zero circle integral for \(g\). Use the original positively oriented circle \(\zeta=a+Re^{i\theta}\), \(0\leq\theta\leq2\pi\). The original complex exponential is its everywhere convergent series; the full binomial product gives \(e^{u+v}=e^ue^v\), and termwise differentiation gives \((e^u)'=e^u\). Its real and imaginary restrictions agree with the circle parameter constructed in the metric companion by their first-order equations and initial values. Thus this circle uses that companion's actual \(\pi\), rather than a new convention.

The geometric series for \((\zeta-z)^{-1}\) converges uniformly on the circle. With its derivative factor \(iRe^{i\theta}\), its term of index zero integrates to \(2\pi i\); each other term integrates to zero by the fundamental theorem for \(e^{-im\theta}/(-im)\). It follows that

\[
\int_{|\zeta-a|=R}\frac{d\zeta}{\zeta-z}=2\pi i,\qquad
f(z)=\frac1{2\pi i}\int_{|\zeta-a|=R}
                          \frac{f(\zeta)}{\zeta-z}\,d\zeta .
\tag{CX6}
\]

Let \(M=\sup_{|\zeta-a|=R}|f(\zeta)|\). Expanding the same full denominator and using CX1 proves

\[
\begin{aligned}
f(z)&=\sum_{m=0}^\infty c_m(z-a)^m,&
c_m&=\frac1{2\pi i}\int_{|\zeta-a|=R}
                     \frac{f(\zeta)}{(\zeta-a)^{m+1}}\,d\zeta,\\
|c_m|&\leq MR^{-m},&
\sup_{|z-a|\leq r}\left|f(z)-\sum_{m=0}^Nc_m(z-a)^m\right|
 &\leq \frac{M(r/R)^{N+1}}{1-r/R}\quad(0\leq r<R).
\end{aligned}
\tag{CX7}
\]

At \(r=0\), the remainder is exactly zero for \(N\geq0\). For every derivative order \(j\), the differentiated terms on a compact disk of positive radius \(r<R\) are bounded by the summable series

\[
M\sum_{m\geq j}\frac{m!}{(m-j)!}r^{m-j}R^{-m}.
\tag{CX8}
\]

Its successive ratio tends to \(r/R<1\). The metric companion's uniform differentiation theorem now proves all derivatives, including at the center by continuity. Hence

\[
f^{(j)}(a)=j!c_j,\qquad |f^{(j)}(a)|\leq j!MR^{-j}.
\tag{CX9}
\]

In particular complex differentiability implies a convergent local power series and continuous derivatives of every order; these have been proved rather than included in the definition.

If the first nonzero coefficient of a nonzero local power series at \(a\) has index \(m\), factor it as \((z-a)^m(c_m+\sum_{\ell>m}c_\ell(z-a)^{\ell-m})\). The parenthesis tends to \(c_m\ne0\), so the zero at \(a\) is isolated and has exactly that multiplicity. A holomorphic function on a connected open set which vanishes on a set with an accumulation point in that open set vanishes everywhere. Indeed the series at that point cannot have a first nonzero coefficient, so it vanishes on a disk. The set of points with a zero neighborhood is open. At a limit point inside the domain it has either an eventual equal point or distinct zeros accumulating there; the same series argument makes it closed relative to the domain. Connectedness makes it the whole domain. Applying this to the difference proves the identity theorem with the actual common connected domain.

Finally, if holomorphic \(f_n\) converge uniformly on every compact subset of \(\Omega\), their limit \(f\) is holomorphic and every \(f_n^{(j)}\) converges to \(f^{(j)}\) uniformly on smaller compact disks. On each fixed circle uniform convergence permits passage through CX6 and CX7. The limit therefore has the same circle representation and coefficient formula. The bound in CX8 with the uniformly bounded circle values proves differentiation and convergence on every smaller disk, for every fixed \(j\). A finite disk cover gives the result on an arbitrary compact subset. This proves the required locally uniform continuation principle without assuming it.

### 16.3. The full dominated holomorphic integral map

Let \((S,\mu)\) be an arbitrary positive measure space. The compact envelopes below restrict every required product integral to an actual sigma-finite positive-envelope part; Section16.3.1 proves that reduction and the completed joint measurability before Fubini is used. Suppose \(f(z,x)\) is measurable in \(x\) for every \(z\in\Omega\), and \(f(\,\cdot\,,x)\) is holomorphic on \(\Omega\) for every \(x\) outside one fixed null set. For every compact \(K\subset\Omega\), assume an actual integrable \(M_K\geq0\) bounds \(|f(z,x)|\) for all \(z\in K\), almost everywhere. Define the original integral \(F(z)=\int_S f(z,x)d\mu(x)\).

Dominated convergence proves continuity of \(F\) on every smaller compact neighborhood. Take a closed disk \(|\zeta-a|\leq R\subset\Omega\), and \(|z-a|\leq r<R\). CX6 for the integrand has denominator of modulus at least \(R-r\) on that circle. The integral of its absolute value over the original circle and \(S\) is at most \(2\pi R\|M_K\|_1/(R-r)\). Thus the proved absolute Fubini theorem gives

\[
\begin{aligned}
F(z)&=\frac1{2\pi i}\int_{|\zeta-a|=R}
                    \frac{F(\zeta)}{\zeta-z}\,d\zeta,\\
F^{(m)}(a)&=\int_S\partial_z^m f(a,x)\,d\mu(x),&
\int_S|\partial_z^m f(a,x)|\,d\mu(x)
 &\leq m!R^{-m}\|M_K\|_1 .
\end{aligned}
\tag{CX10}
\]

The first line gives a convergent power series by the actual geometric denominator expansion, hence holomorphy of \(F\). For the second line use CX9 for each integrand and its circle formula for the derivative. The full absolute bound is integrable, so the same Fubini interchange identifies the coefficient with the integral of the integrand derivative. Differentiability under the integral is therefore a consequence, not an extra assumption.

For \(d\) complex parameters on an actual product of disks, the same argument applied successively to their circle integrals gives, with multiindex \(\alpha=(\alpha_1,\ldots,\alpha_d)\) and original radii \(R_j\),

\[
\partial^\alpha F(a)=\int_S\partial^\alpha f(a,x)d\mu(x),
\qquad
\int_S|\partial^\alpha f(a,x)|d\mu(x)
 \leq\left(\prod_{j=1}^d\alpha_j!R_j^{-\alpha_j}\right)\|M_K\|_1 .
\tag{CX11}
\]

Every circle contributes its own \(1/(2\pi i)\), derivative factorial and radius. The iterated geometric series converges absolutely on every smaller product of disks, because its bound is the product of the \(d\) geometric sums times \(\|M_K\|_1\). It therefore supplies a joint power series, including every mixed derivative, rather than only separate differentiability. Additional continuous real parameters can be carried through this proof when the actual envelope is common on their compact parameter sets; dominated convergence supplies their continuity. Their derivatives can be passed through only when their full differentiated integrands have corresponding integrable envelopes, exactly as in the real dominated-integral provider.

#### 16.3.1. The actual circle and product measurability

To interchange the original parameter and circle integrals, first establish their joint measurability and absolute envelope bounds. It retains the original measure space \((S,\mu)\), the integrand \(f(z,x)\), every compact envelope and the original integral \(F(z)=\int_S f(z,x)\,d\mu(x)\). Its purpose is to prove the product measurability needed for the stated Fubini steps, rather than assume that separate measurability has already supplied it.

Fix the original closed disk \(K=\{|z-a|\leq R\}\subset\Omega\), \(R>0\), and the original circle parametrization
\(\zeta(t)=a+Re^{it}\), \(0\leq t\leq2\pi\). The hypotheses give one fixed null set \(N\) outside which \(f(\,\cdot\,,x)\) is holomorphic, hence continuous on the circle. Enlarge it by the null set for this compact envelope, so
\(|f(z,x)|\leq M_K(x)\) for every \(z\in K\), \(x\notin N\), with \(\int_S M_K\,d\mu<\infty\). A finite modification of the envelope on its own null exceptional set can be covered by this same \(N\); the original integral is unchanged.

For \(k\geq1\), partition \([0,2\pi)\) into its \(2^k\) half-open intervals
\(I_{k,j}=[2\pi j/2^k,2\pi(j+1)/2^k)\), and retain the endpoint \(\{2\pi\}\) separately. Define the actual finite sum

\[
f_k(t,x)=\sum_{j=0}^{2^k-1}
\boldsymbol1_{I_{k,j}}(t)
f\!\left(a+Re^{2\pi i j/2^k},x\right)
\ +\boldsymbol1_{\{2\pi\}}(t)f(a+R,x).
\tag{CMI1}
\]

Each function \(x\mapsto f(a+Re^{2\pi i j/2^k},x)\) is measurable by the original hypothesis. The corresponding function on the product is measurable: the inverse image of a Borel set on each strip is that strip times a measurable subset of \(S\), and the sum is finite. Thus every \(f_k\) is measurable for the product sigma-algebra. For each original \(t\) and \(x\notin N\), continuity on the circle gives \(f_k(t,x)\to f(\zeta(t),x)\). The countable limit is measurable off the product cylinder \([0,2\pi]\times N\). That cylinder has product measure zero, and its entire subsets are measurable in the completed product. Hence the original function \((t,x)\mapsto f(\zeta(t),x)\), with its actual values on that cylinder retained, is measurable for the completed product. No pointwise values of the working integrand have been substituted.

The product argument can be confined to an actual sigma-finite part even when the whole original measure space is not sigma-finite. Put
\[
S_K=\bigcup_{j=1}^\infty\{x:M_K(x)\geq1/j\}.
\tag{CMI2}
\]
Every set in this union has measure at most \(j\int_S M_K\,d\mu\), by the proved integral of its indicator and the pointwise inequality
\(\boldsymbol1_{\{M_K\geq1/j\}}\leq jM_K\).
Thus \(\mu|_{S_K}\) is sigma-finite. On \(S\setminus S_K\) the original \(M_K\) is zero and \(f(z,x)=0\) for every \(z\in K\), outside \(N\). The original integral therefore retains the entire decomposition
\[
\int_S f(z,x)\,d\mu(x)
=\int_{S_K}f(z,x)\,d\mu(x)
 +\int_{S\setminus S_K}f(z,x)\,d\mu(x),
\qquad
\int_{S\setminus S_K}f(z,x)\,d\mu(x)=0 .
\tag{CMI3}
\]
The zero complement is proved from the actual envelope; it is not a dropped contribution. Product measurability and completed complex Fubini on the sigma-finite factor \(S_K\) are supplied by the original measure chapter. The finite circle parameter is the other factor. Null exceptional cylinders are measurable in its completion, with measure zero as stated above.

For \(|z-a|\leq r<R\), the exact circle differential is
\(d\zeta=iRe^{it}\,dt\) and its modulus is \(R\,dt\). The original kernel has denominator of modulus at least \(R-r\). Consequently
\[
\int_0^{2\pi}\int_{S_K}
\left|
\frac{f(a+Re^{it},x)}{a+Re^{it}-z}
iRe^{it}
\right|d\mu(x)\,dt
\leq
\frac{2\pi R}{R-r}\int_S M_K(x)\,d\mu(x).
\tag{CMI4}
\]
Every circle factor and the zero-complement equality in CMI3 remain. This is precisely the absolute envelope required to interchange the original \(S\)-integral and the positively oriented circle in CX10. For its \(m\)-th coefficient the additional original Cauchy multiplier is
\(m!/(2\pi i)\) and the denominator is \((\zeta-a)^{m+1}\). The absolute parameter integral is bounded by
\[
\frac{m!}{2\pi}2\pi R R^{-m-1}
\int_S M_K\,d\mu
=m!R^{-m}\int_S M_K\,d\mu .
\tag{CMI5}
\]
This proves both product measurability and the complete bound before the derivative/Fubini step. Each derivative \(x\mapsto\partial_z^m f(a,x)\) is measurable outside \(N\), because it is a pointwise limit of countably many measurable difference quotients on the original coordinate disk. Define its extension to the exceptional set \(N\) to be zero, since a holomorphic derivative was required only off \(N\). This is a measurable extension on the original measure space, agrees with every required derivative, and changes no integral.

For the \(d\)-parameter extension, take the original product of closed disks centered at \(a_j\) with radii \(R_j>0\). The precise hypotheses are measurability in \(x\) for every parameter tuple, separate holomorphy in each complex coordinate outside one fixed null set, and one actual integrable \(M_K\) for the whole compact product. These suffice; joint holomorphy is the conclusion.

Joint measurability on the product of its circles follows by induction on their number. For one circle it is CMI1. For \(d>1\), replace only the first circle parameter by its finite dyadic endpoints. Each resulting summand is measurable in the remaining \(d-1\) parameters and \(x\) by the induction hypothesis, because fixing that endpoint preserves the original measurability and separate continuity. Multiplication by its first-parameter interval indicator gives product measurability. As its mesh tends to zero, separate continuity in that first coordinate gives pointwise convergence to the original function for every remaining parameter tuple and every \(x\notin N\). The completed null-cylinder argument proves the claim, with the entire original tuple retained. There is no assumption that separate continuity already gives joint continuity.

Apply the original one-variable Cauchy formula successively for the fixed other coordinates. The absolute completed Fubini bound on the circle product is
\[
\left(\prod_{j=1}^d\frac{2\pi R_j}{R_j-r_j}\right)
\int_S M_K\,d\mu,\qquad 0\leq r_j<R_j .
\tag{CMI6}
\]
It comes from the full product of the \(d\) differentials \(iR_je^{it_j}\,dt_j\), not a unit circle substitute. The resulting original multiple formula is
\[
F(z)=\left(\prod_{j=1}^d\frac1{2\pi i}\right)
\int_{|\zeta_1-a_1|=R_1}\cdots
\int_{|\zeta_d-a_d|=R_d}
\frac{F(\zeta_1,\ldots,\zeta_d)}
     {\prod_{j=1}^d(\zeta_j-z_j)}
\ d\zeta_d\cdots d\zeta_1 .
\tag{CMI7}
\]
All factors have their original positive orientations; Fubini justifies reversing the iterated order as well. In each denominator use its full convergent geometric expansion with its original numerator powers. On a smaller product of disks the absolute majorant is the product of the \(d\) geometric series, each of ratio \(r_j/R_j<1\). Its sum times \(\int_S M_K\,d\mu\) bounds the whole series, so the actual multiple Cauchy integral is a joint convergent power series. Differentiation of this joint series and the full coefficient integrals give
\[
\partial^\alpha F(a)
=\int_S\partial^\alpha f(a,x)\,d\mu(x),\qquad
\int_S|\partial^\alpha f(a,x)|\,d\mu(x)
\leq
\left(\prod_{j=1}^d\alpha_j!R_j^{-\alpha_j}\right)
\int_S M_K\,d\mu .
\tag{CMI8}
\]
Mixed derivatives of the integrand itself are supplied by the same multiple circle representation before integration in \(x\). Each is measurable by its countable original difference quotients off the fixed null set, and CMI8 gives its absolute integral bound. This closes the actual measurability, Fubini, mixed-derivative and joint-power-series steps used in CX10--CX11, including the full original radius and factorial factors. Additional real parameters still need their actual continuity and differentiated envelopes on compact parameter sets, as the original source states; no real derivative hypothesis is invented.

### 16.4. The original winding number

For a closed contour \(\Gamma\) and a point \(w\) off its image define

\[
n_\Gamma(w)=\frac1{2\pi i}\int_\Gamma\frac{d\zeta}{\zeta-w}.
\tag{CX12}
\]

On each contour piece set \(U(t)=\gamma(t)-w\), which never vanishes. Define the continuous accumulated integral \(A(t)=\int_{\Gamma|_{[a,t]}}d\zeta/(\zeta-w)\), with the pieces concatenated in their original order. The fundamental theorem and product rule give
\((U(t)e^{-A(t)})'=0\) on each piece, since \(A'=U'/U\). Endpoint continuity makes the constant the same on all pieces. Hence

\[
U(t)=U(a)e^{A(t)},\qquad e^{A(b)}=1 .
\tag{CX13}
\]

The complex exponential has modulus \(e^{\operatorname{Re}z}\), by its product law and conjugate series. Its purely imaginary restriction is the original circle parameter. That circle traverses the unit circle once during \(0\leq\theta<2\pi\), as proved by the arctangent chart and arc-length calculation in the metric companion. Consequently \(e^z=1\) holds exactly for \(z=2\pi i k\), \(k\in\mathbb Z\). CX13 therefore proves that CX12 is an integer, with its sign fixed by the original contour orientation.

The contour image is compact. On a neighborhood of any \(w\) outside it the denominator has a positive uniform lower bound. CX1 or dominated convergence proves continuity of CX12 there. Its integer values make it locally constant, and therefore constant on every connected component of the complement of the contour. If the image lies in \(|\zeta|\leq L\) and \(|w|>L\), the full geometric expansion gives

\[
\frac1{\zeta-w}
 =-\sum_{m=0}^{\infty}\frac{\zeta^m}{w^{m+1}}.
\tag{CX14}
\]

It converges uniformly on the contour. Each numerator \(\zeta^m\) has the global primitive \(\zeta^{m+1}/(m+1)\), so every term has zero closed-contour integral. Thus \(n_\Gamma(w)=0\) on the unbounded outside component. Reversing \(\Gamma\) negates its winding number; concatenating closed contours adds their winding numbers. These are exact oriented-integral identities.

### 16.5. The complete contour theorem and every finite-pole residue

A finite integer sum of closed contours is also allowed: add the original integrals and winding numbers with precisely those integer coefficients. In an integral bound use the sum of each length times the absolute value of its integer coefficient. Suppose \(\Gamma\) lies in \(\Omega\) and
\(n_\Gamma(w)=0\) for every \(w\notin\Omega\). For holomorphic \(f\) on \(\Omega\), define off the contour

\[
\Phi(w)=\frac1{2\pi i}\int_\Gamma\frac{f(\zeta)}{\zeta-w}\,d\zeta .
\tag{CX15}
\]

It is holomorphic there by CX10, with the positive distance to the compact contour supplying the actual local envelope. For \(w\in\Omega\), the function

\[
H(w)=\frac1{2\pi i}\int_\Gamma
             \frac{f(\zeta)-f(w)}{\zeta-w}\,d\zeta
\tag{CX16}
\]

is holomorphic even at points on the contour. At \(\zeta=w\) the quotient is defined as \(f'(w)\). To prove its required holomorphy in \(w\), expand \(f\) on a small disk at a diagonal point. Each divided power has the full polynomial
\(((\zeta-a)^m-(w-a)^m)/(\zeta-w)
=\sum_{j=0}^{m-1}(\zeta-a)^{m-1-j}(w-a)^j\).
The coefficient bounds in CX7 make this sum locally uniformly convergent, with every derivative on smaller disks by CX8. Away from the diagonal the quotient is a quotient of holomorphic functions with nonzero denominator. On a compact \(w\)-set and the compact contour, a finite disk cover of the diagonal supplies a uniform bound for those divided differences; on its compact complement the denominator is bounded away from zero. CX10 therefore proves the asserted integral holomorphy.

Off the contour, CX12 gives \(H=\Phi-n_\Gamma f\). Let \(V\) be the open set of points off the contour with \(n_\Gamma=0\). It is open by local constancy. The hypothesis places every point outside \(\Omega\) in \(V\). On \(V\), define \(H=\Phi\); this agrees with CX16 on the overlap. Since \(\Omega\cup V=\mathbb C\), these definitions construct one entire \(H\), including every contour point.

If the contour lies in \(|\zeta|\leq L\), let \(\ell\) be its total length with absolute integer multiplicities. For \(|w|>L\), CX14 gives \(n_\Gamma(w)=0\) and

\[
|H(w)|=|\Phi(w)|
\leq \frac{\ell\,\sup_\Gamma|f|}{2\pi(|w|-L)}
\longrightarrow0.
\tag{CX17}
\]

Continuity bounds \(H\) on the remaining compact disk, so it is bounded on the whole plane. CX9 at any center and any radius gives \(|H'(a)|\leq \sup_{\mathbb C}|H|/R\); letting \(R\to\infty\) proves \(H'=0\). The fundamental theorem on each straight segment makes \(H\) constant, and CX17 makes that constant zero. This is the full Liouville argument, including its actual Cauchy factor.

Consequently both original contour conclusions are

\[
\frac1{2\pi i}\int_\Gamma\frac{f(\zeta)}{\zeta-w}\,d\zeta
       =n_\Gamma(w)f(w)\quad(w\in\Omega\setminus\Gamma),
\qquad
\int_\Gamma f(\zeta)\,d\zeta=0 .
\tag{CX18}
\]

For the second conclusion use \(\Phi(w)=0\) at sufficiently large \(w\), multiply CX15 by \(w\), and pass to the uniform limit \(w/(\zeta-w)\to-1\) on the compact contour. All prefactors remain in that calculation. The winding hypothesis is necessary: for \(f(\zeta)=1/\zeta\) on \(\mathbb C\setminus\{0\}\), a positive circle has winding one at the omitted point and integral \(2\pi i\). This example identifies precisely the domain condition; it does not supply that condition by assuming away a pole.

For a deformation \(\gamma_s\) of closed contours within \(\Omega\), with a fixed finite piece decomposition and jointly continuous \(\gamma_s,\partial_t\gamma_s\), the winding at every point outside \(\Omega\) is continuous in \(s\), by its uniform positive denominator bound on the compact parameter/contour product. It is integer-valued, so it is constant. The cycle \(\gamma_1-\gamma_0\) thus has winding zero outside \(\Omega\). Applying CX18 proves equality of their holomorphic integrals. This proves the contour-deformation rule with the exact domains and actual orientation.

Now let \(f\) be meromorphic on \(\Omega\) with exactly the finite poles \(a_1,\ldots,a_p\), of actual orders \(m_1,\ldots,m_p\geq1\), and let \(\Gamma\) avoid them. At \(a_j\) the holomorphic function \(g_j(\zeta)=(\zeta-a_j)^{m_j}f(\zeta)\), with \(g_j(a_j)\ne0\), has the power series proved in CX7. Its entire principal part and residue are

\[
\begin{aligned}
P_j(\zeta)&=\sum_{\ell=1}^{m_j}
        \frac{g_j^{(m_j-\ell)}(a_j)}{(m_j-\ell)!}
                         (\zeta-a_j)^{-\ell},\\
\operatorname{Res}_{a_j}f
 &=\frac{g_j^{(m_j-1)}(a_j)}{(m_j-1)!}.
\end{aligned}
\tag{CX19}
\]

Subtracting every \(P_j\) gives a holomorphic function on \(\Omega\): its local residual power series has only nonnegative exponents at each original pole, and all the other subtracted principal parts are holomorphic there. CX18 gives zero integral for this difference when the same winding condition outside \(\Omega\) holds. Every term with \(\ell\geq2\) has the global primitive
\(-(\zeta-a_j)^{1-\ell}/(\ell-1)\) away from that pole, so its closed-contour integral is zero by the full chain and fundamental theorem. Each \(\ell=1\) term has integral \(2\pi i n_\Gamma(a_j)\) by CX12. Thus

\[
\int_\Gamma f(\zeta)d\zeta
 =2\pi i\sum_{j=1}^p n_\Gamma(a_j)
                  \frac{g_j^{(m_j-1)}(a_j)}{(m_j-1)!}.
\tag{CX20}
\]

Every original pole, order, derivative factorial and winding multiplicity is retained. Empty pole sets give CX18. A rational function is covered by \(\Omega=\mathbb C\), where the exterior winding condition is empty; its polynomial part has a global polynomial primitive and contributes zero.

For later orientation checks, a positive full circle has winding one inside and zero outside by the exact geometric integral in CX6 and CX14. A positive upper half-disk boundary runs along the real interval from \(-R\) to \(R\), then counterclockwise along the upper arc from \(R\) to \(-R\). Its winding is zero outside the closed half-disk: such points can be joined to infinity through the lower half-plane or outside the radius without crossing the contour. Its winding is constant on the connected open upper half-disk. At \(w=i\delta\), \(0<\delta<R\), the real segment integral has imaginary part
\(\int_{-R}^R\delta/(t^2+\delta^2)dt\to\pi\) and zero real part. The upper arc integral tends to \(i\pi\), uniformly away from its denominator as \(\delta\downarrow0\). The winding tends to one, so its integer value is one throughout that half-disk. Reversal negates this value. This proves the half-plane residue orientation used in T17 directly.

### 16.6. Bounded and exhausted maximum principles in the original domains

Suppose \(|f|\) has a local maximum at an interior point \(a\). If \(f(a)=0\), it vanishes on that neighborhood. Otherwise, if the local power series is nonconstant, let \(m\geq1\) be its first nonconstant coefficient. Choose a complex unit \(u\) so that \(c_m u^m\) is a positive real multiple of \(f(a)\); existence follows from the actual circle parameter by dividing that argument by the integer \(m\). For small positive \(r\),
\(f(a+ru)=f(a)+c_m u^m r^m+o(r^m)\).
Its component in the direction of \(f(a)\) is strictly greater than \(|f(a)|\), contradicting the maximum. Thus \(f\) is constant locally, and CX7's identity theorem makes it constant on the connected component. This proves the interior maximum-modulus principle.

If \(\Omega\) is bounded, \(f\) is holomorphic in it and continuous on its closure, compactness gives a maximum on that closure. If it is attained in the interior, the preceding argument makes \(f\) constant on that component. That bounded open component has a boundary point: follow a ray from one of its points until the first exit from a containing bounded ball and take the first component-exit limit. Its boundary lies in \(\partial\Omega\), because any interior ball meeting the component at a limit point would be connected to it and hence belong to the same component. Continuity therefore makes the constant value a boundary value. Consequently

\[
\sup_{\overline\Omega}|f|\leq\sup_{\partial\Omega}|f|.
\tag{CX21}
\]

The reverse inequality is immediate. Disconnected bounded domains cause no exception, since the argument applies to the component where the attained maximum lies.

## 6. Indices of rectangles and circles

Let \(a<b\), \(c<d\), and let \(\partial R\) be the positively oriented boundary of the closed rectangle
\[
R=\{x+iy:a\leq x\leq b,\ c\leq y\leq d\}.
\]
For every \(\zeta\notin\partial R\),
\[
\operatorname{ind}_{\partial R}(\zeta)=
\begin{cases}
1,&\zeta\in\operatorname{int}R,\\
0,&\zeta\notin R.
\end{cases}
\]

**Proof for an interior point.** Translate \(\zeta\) to zero. Write the positive distances to the left, right, bottom and top sides as \(A,B,C,D\), respectively. The translated rectangle is \([-A,B]\times[-C,D]\). For each angle \(\theta\), take the applicable positive numbers in the following list:
\[
\frac{B}{\cos\theta}\ (\cos\theta>0),\qquad
\frac{A}{-\cos\theta}\ (\cos\theta<0),\qquad
\frac{D}{\sin\theta}\ (\sin\theta>0),\qquad
\frac{C}{-\sin\theta}\ (\sin\theta<0).
\]
Let \(r(\theta)\) be their minimum. At least one number is applicable. The inequalities defining the rectangle say exactly that its intersection with this ray is the segment of radii \(0\leq\rho\leq r(\theta)\). Thus \(r(\theta)e^{i\theta}\) is its unique boundary point on the ray.

The active side changes only at the four corner directions. On an interval between corner directions, the relevant displayed quotient is smooth with a nonzero denominator. Near an axis, a quotient with denominator tending to zero cannot be the minimum because the other applicable quotient stays bounded. At a corner the two active quotients have the same positive value. These facts prove that \(r\) is positive, continuous, \(2\pi\)-periodic and piecewise \(C^1\). They also give a finite partition on which its parametrization is smooth.

As \(\theta\) increases by \(2\pi\), these boundary points traverse each of the four sides once in positive order. To check the orientation directly, on the right side the height is \(B\tan\theta\) and increases; on the top side the horizontal coordinate is \(D\cot\theta\) and decreases; on the left side the height is \(-A\tan\theta\) and decreases; on the bottom side the horizontal coordinate is \(-C\cot\theta\) and increases. On each relevant angular interval these are monotone parametrizations of the corresponding full side or its part split at the starting ray. The real change-of-variable rule therefore identifies this radial integral with the usual positively oriented rectangle integral.

On every smooth piece, with \(\gamma(\theta)=r(\theta)e^{i\theta}\),
\[
\frac{\gamma'(\theta)}{\gamma(\theta)}
=\frac{r'(\theta)}{r(\theta)}+i.
\]
The integrals of \(r'/r\) are real logarithm differences. They telescope across the finitely many endpoints and total zero because \(r(2\pi)=r(0)\). The integral of \(i\) is \(2\pi i\). Division by \(2\pi i\) proves the index is \(1\).

**Proof for an exterior point.** If \(\zeta\notin R\), at least one real coordinate lies strictly outside the corresponding closed interval. Translate by \(-\zeta\), then multiply by some \(\alpha\in\{1,-1,i,-i\}\) so that the entire translated rectangle lies in the open right half-plane. For \(w=x+iy\) with \(x>0\), define the single-valued function
\[
L(w)=\tfrac12\log(x^2+y^2)+i\arctan(y/x).
\]
Real differentiation gives \(L_x=1/w\) and \(L_y=i/w\). Hence along any piecewise \(C^1\) path \(w(s)\) in that half-plane, \(\frac{d}{ds}L(w(s))=w'(s)/w(s)\). With \(w(s)=\alpha(\gamma(s)-\zeta)\), this is \(\gamma'(s)/(\gamma(s)-\zeta)\). The primitive rule gives zero around the closed rectangle. This proves the exterior case. Points on its boundary were excluded because the integrand would be singular there.

For clarity, a positively oriented circle of center \(c_0\) and radius \(R_0>0\) has the same inside/outside index rule. Put \(w=\zeta-c_0\) and parametrize by \(c_0+R_0e^{i\theta}\). If \(|w|<R_0\), the integrand with its parameter differential is
\[
\frac{i}{1-(w/R_0)e^{-i\theta}}\,d\theta
=i\sum_{n\geq0}(w/R_0)^n e^{-in\theta}\,d\theta.
\]
Uniform geometric convergence permits integration; only the constant term remains, giving \(2\pi i\). If \(|w|>R_0\), write it instead as
\[
-i\sum_{n\geq1}(R_0/w)^n e^{in\theta}\,d\theta;
\]
every term integrates to zero. The elementary exponential integrals follow from their explicit primitives. Boundary points are again excluded. Reversing any contour's orientation negates the index, and taking integer sums adds indices, directly from the definition.

