# Coordinate inverses, integration and surface measure

**Source and terms.** This expanded prerequisite reading follows Jiří Lebl's freely available *Basic Analysis II*, version 6.3, 15 May 2026: [Section 8.5, printed pp. 51–57](https://www.jirka.org/ra/realanal2.pdf#page=51), and [Section 10.7, printed pp. 134–137](https://www.jirka.org/ra/realanal2.pdf#page=134). It is a derivative reading under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), one of the author's two offered licences, and is excluded from the course's CC0 dedication. Adapted and expanded by GPT-6 Astra (OpenAI), 4–5 October 2026. Self-checked by the writing AI. 

Read the [Euclidean measure and product proof](finite-derivative-l2.md#euclidean-products) first, then this reading, then that reading's Fourier subsection. Only its measure subsection is an input here. This order avoids using the polar-coordinate Gaussian calculation to justify change of variables. The finite linear algebra, product and chain rules used here are proved below. The one-variable fundamental theorem is supplied by the [continuous-input argument through (13)](hilbert-valued-integration.md#continuous-primitives) in the integration reading, applied to real scalars; that argument uses only the earlier measure facts. This is the order of its use here. The remaining starting axioms are the usual field operations, ordered-real completeness and set theory with choice. Every inverse, volume-change and surface-coordinate fact used below has its stated proof.

<a id="coordinate-linear-algebra"></a>
## The finite linear algebra and differential rules

The finite-dimensional facts needed here follow directly from field operations and the positive square root already proved in the measure reading. We spell them out to specify the inputs to the coordinate arguments.

For real vectors, expanding $|v-tu|^2\ge0$ and minimizing the quadratic in the real number $t$ gives $(v\cdot u)^2\le|v|^2|u|^2$; the case $u=0$ is immediate. Expanding $|v+w|^2$ then proves the triangle inequality. Also $|v|_\infty\le|v|\le\sqrt n\,|v|_\infty$. Completeness of either norm follows by taking the limits of the finitely many Cauchy coordinates. Every matrix is bounded in these norms: in the maximum norm, each output coordinate is bounded by its row's sum of absolute entries times the input norm. Products satisfy $\|AB\|\le\|A\|\|B\|$ by applying the two bounds successively. If a subspace has a finite independent spanning list, subtracting the projections onto the preceding normalized vectors and normalizing each nonzero residual constructs an orthonormal basis. The residual is nonzero precisely because the original list was independent.

Define the determinant as the alternating multilinear function of the columns taking value one on the standard basis. Existence is given by the finite signed permutation sum. Expanding each column in the standard basis proves uniqueness, since terms with repeated basis columns vanish and all other terms have their permutation sign. For fixed $A$, the function $\det(Av_1,\ldots,Av_n)$ is alternating multilinear in the $v_j$ and equals $\det A$ on the standard basis. Uniqueness proves $\det(AB)=\det A\det B$. The same column expansion gives the cofactor formula and $A\,\operatorname{adj}A=(\det A)I$: a diagonal entry is the cofactor expansion of $\det A$, and an off-diagonal entry is the expansion of a determinant with two equal rows. Transposition gives the identity in the other order. Thus nonzero determinant gives the inverse by the adjugate formula.

For completeness, elimination uses no further existence theorem. Consider a square matrix with zero kernel; invertible matrices have this property. Its first column has a nonzero entry; permute it into the first row, scale that row to make the entry one, and subtract multiples of it from the other rows. The remaining square block also has zero kernel, since a vector in its kernel would give one in the full matrix's kernel by solving the first row. The one-dimensional case is a nonzero scalar. Induction therefore reduces the remaining block to the identity; then remove the entries above the diagonal. This expresses every invertible matrix as a product of row permutations, nonzero row scalings and row additions. These operations have determinants respectively their permutation sign, their scaling factor and one, directly from alternating multilinearity. In particular an invertible matrix has nonzero determinant, and its inverse entries are smooth rational functions of its entries once the scalar differential rules below are proved. In dimension zero the determinant is one, the space is a singleton with counting measure, and the inverse and volume assertions are identities.

<a id="coordinate-differential-rules"></a>

Total differentiability at $x$ means $F(x+h)=F(x)+Ah+r(h)$, where $A$ is linear and $|r(h)|/|h|\to0$. The matrix bound above implies continuity at $x$ and $F(x+h)-F(x)=O(|h|)$. If $G$ is differentiable at $F(x)$, write its analogous expansion with linear part $B$. Substituting the first expansion into the second gives
\[
 \begin{gathered}
 (G\circ F)(x+h)-(G\circ F)(x)\\
 =BAh+o(|h|).
 \end{gathered}
 \tag{DC1}
\]
Indeed $B r(h)=o(|h|)$, and the second remainder is $o(|F(x+h)-F(x)|)=o(|h|)$, with value zero when that increment is zero. This proves the chain rule with its full hypotheses.

For a bounded bilinear map $\mathcal B$, expand $\mathcal B(u+\Delta u,v+\Delta v)-\mathcal B(u,v)$ into its two linear terms and $\mathcal B(\Delta u,\Delta v)$. For differentiable inputs the last term is $O(|h|^2)=o(|h|)$. This proves the product rule, including scalar multiplication, dot products and ordered matrix products. Sums and fixed linear maps follow directly from the definition. For $z\ne0$, subtracting the proposed linear part from the difference of reciprocals gives
\[
 \frac1{z+h}-\frac1z+\frac h{z^2}
 =\frac{h^2}{z^2(z+h)}.
\]
The denominator stays bounded away from zero near $h=0$, so the remainder divided by $|h|$ tends to zero. This proves the reciprocal rule over the reals (and over the complex numbers when needed). Repeated product and chain rules make polynomials and rational functions smooth on their domains. Continuity of the displayed derivative formulas proves the $C^1$ rules; induction proves the corresponding $C^k$ rules at every finite order.

The [continuous scalar fundamental theorem](hilbert-valued-integration.md#continuous-primitives), proved there through equation (13), uses only the earlier measure construction and the compactness argument stated there. Apply it to each component of the curve $t\mapsto F(x'+t(x-x'))$, whose derivative is given by (DC1). Write $v=x-x'$ and $\gamma(t)=x'+tv$. Whenever this segment lies in the domain of a $C^1$ map, we obtain
\[
 \begin{gathered}
 F(x)-F(x')=\int_0^1 DF(\gamma(t))v\,dt,\\
 |F(x)-F(x')|\le
 |v|\sup_{0\le t\le1}\|DF(\gamma(t))\|.
 \end{gathered}
 \tag{DC2}
\]
The norm bound for a finite-dimensional integral follows from the scalar integral inequality: for a nonzero integral vector $v$, pair with $v/|v|$ and use Cauchy–Schwarz; the zero case is immediate. This proves the line-segment estimate used in local inversion.

<a id="coordinate-inverse"></a>
## Local inversion with the full finite regularity

Let $F:U\to\mathbb R^n$ be $C^1$ on an open set, and let $DF(x_0)$ be invertible. Translate the two origins and multiply the output by $DF(x_0)^{-1}$. It suffices to treat $F(0)=0$, $DF(0)=I$. On a sufficiently small closed ball $\overline B(0,r)\subset U$, continuity gives $\|DF-I\|\le1/2$. Integrating along a line segment in that ball gives
\[
 |F(x)-F(x')-(x-x')|\le\tfrac12|x-x'|,
 \qquad |F(x)-F(x')|\ge\tfrac12|x-x'|.
 \tag{CI1}
\]
For $|y|<r/2$, the map $T_y(x)=x-F(x)+y$ takes the closed ball into itself and has Lipschitz constant at most $1/2$. Starting at any $x_1$ in the ball, set $x_{j+1}=T_y(x_j)$. Successive differences are at most $2^{1-j}|x_2-x_1|$. Their geometric sum makes the sequence Cauchy. Completeness gives a limit, continuity makes it a fixed point, and the contraction inequality makes it unique. Thus $F(x)=y$ has a unique solution $G(y)$, with $|G(y)|\le2|y|<r$.

The second inequality in (CI1) makes $G$ Lipschitz with constant two. On the open preimage of $B(0,r/2)$ within $B(0,r)$, $F$ and $G$ are mutual inverses. Every matrix $DF(x)$ there is invertible: if $A=I-H$ with $\|H\|\le1/2$, the norm-convergent series $\sum_{j\ge0}H^j$ is its two-sided inverse, by multiplication of finite partial sums and passage to the limit. Its norm is at most two.

Write $x=G(y)$ and $h=G(y+k)-G(y)$. Differentiability of $F$ gives
$k=DF(x)h+o(|h|)$. Since $|h|\le2|k|$, multiplication by the bounded inverse gives
\[
 G(y+k)-G(y)=DF(G(y))^{-1}k+o(|k|).
 \tag{CI2}
\]
This proves total differentiability. Matrix inversion is continuous on the invertible matrices: $A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}$. Hence (CI2) gives a continuous derivative and proves the $C^1$ inverse theorem. Repeating at every point shows that a map with everywhere invertible derivative is locally open. In particular a globally injective such map is a diffeomorphism onto its open image.

The positive real powers used in the Hölder bounds are constructed and differentiated in the [elementary-function reading, (EF6)–(EF7)](elementary-functions-and-cutoffs.md#logarithm-and-real-powers). Suppose now $F\in C^{k,\alpha}_{\mathrm{loc}}$, with integer $k\ge1$ and $0<\alpha<1$. Differentiating (CI2) inductively gives $G\in C^k$. Here matrix inversion is smooth wherever the determinant is nonzero, because its entries are cofactors divided by the determinant; differentiating an inverse also follows directly from $d(A^{-1})=-A^{-1}(dA)A^{-1}$. Repeated product and chain rules show that each derivative of $G$ of order $j\le k$ is a finite sum of products of inverse matrices $DF(G)^{-1}$ and derivatives $D^\ell F(G)$ with $\ell\le j$. No derivative of $F$ of order greater than $j$ occurs.

On smaller compact convex coordinate neighborhoods, $G$ is Lipschitz. Composition of an $\alpha$-Hölder function with a Lipschitz map is $\alpha$-Hölder: its seminorm is multiplied by at most the Lipschitz constant to power $\alpha$. Products of bounded Hölder functions are Hölder, by subtracting one factor at a time. A Lipschitz function on a set of finite positive diameter $D$ is $\alpha$-Hölder with bound $LD^{1-\alpha}$, since $d\le D^{1-\alpha}d^\alpha$ for $0\le d\le D$; on a singleton the assertion is immediate. Derivatives $D^\ell F$ with $\ell<k$ are locally Lipschitz by their bounded next derivatives; $D^kF$ is Hölder by assumption. The inverse-matrix difference identity gives the same Hölder control of $DF(G)^{-1}$. The preceding finite formulas therefore make $D^kG$ Hölder. This proves the full $C^{k,\alpha}$ assertion, including $k=1$. It also proves uniform bounds on a smaller chart in terms of its size, the inverse-derivative bound and the stated $C^{k,\alpha}$ bounds. Smoothness follows by applying the finite statement at every order.

For a real scalar $p(\tau,\eta)$ with $\partial_\tau p\ne0$, apply this result to $F(\tau,\eta)=(p(\tau,\eta),\eta)$. Its inverse has the form $(\Sigma(\lambda,\eta),\eta)$ and
\[
 \partial_\lambda\Sigma=(\partial_\tau p)^{-1},\qquad
 \partial_{\eta_j}\Sigma=-\partial_{\eta_j}p/(\partial_\tau p).
 \tag{CI3}
\]
The right sides are evaluated at $(\Sigma,\eta)$. These identities and the preceding proof give precisely $C^1$, $C^{k,\alpha}$ or smooth graph coordinates, according to the actual hypothesis on $p$.

<a id="coordinate-integration"></a>
## Change of variables for Lebesgue integrals

Let $F:U\to V$ be a $C^1$ diffeomorphism of open subsets of $\mathbb R^n$. We prove, for every nonnegative Lebesgue-measurable $h$, and also for every absolutely integrable complex $h$,
\[
 \int_V h(y)\,dy=\int_U h(F(x))\,|\det DF(x)|\,dx.
 \tag{CI4}
\]

First, an invertible linear map $A$ scales Lebesgue measure by $|\det A|$. Gaussian elimination expresses it as a product of coordinate permutations, multiplication of one coordinate by a nonzero scalar, and addition of a multiple of one coordinate to another. The product theorem proves the assertion for permutations. For scaling it follows from one-dimensional length scaling, first on intervals and then on measurable sets by the outer-measure definition. For a shear, fix all coordinates except the changed one; each fibre is merely translated, so the product theorem preserves its measure. These operations have determinant absolute values respectively one, the absolute scalar and one. Multiplication of their determinant factors proves the claim for $A$. This argument applies to Borel sets and nonnegative functions. For completed measurable sets it applies too, because a linear Lipschitz map takes null sets to null sets by the covering argument in the next paragraph.

A Lipschitz map on a bounded cube takes null subsets to null sets. Cover the subset by cubes of total volume less than $\varepsilon$ and intersect each covering cube with the domain cube. Any two points of such an intersection, for a covering cube of side $s$, have images at distance at most $L\sqrt n\,s$. If the intersection is nonempty, choose one image point; the entire image lies in a cube about it of side $2L\sqrt n\,s$. Here $L$ is the map's Lipschitz constant. Empty intersections contribute nothing, and for $L=0$ each nonempty image is a singleton of measure zero. Thus the outer measure of each image is at most $(2L\sqrt n)^n$ times the covering cube volume. Sum and let $\varepsilon$ tend to zero. No extension of the map outside its domain cube is needed. Cube covers suffice for this null-set argument. For a bounded rectangle with side lengths $l_i$, cover it by the finitely many cubes of a mesh of width $h$ that meet it, enlarging them arbitrarily slightly to open cubes if needed. Their total volume is at most $\prod_i(l_i+2h)$ up to that arbitrarily small enlargement. As $h\to0$ this tends to the rectangle volume. For a countable rectangular cover choose the excess for its $j$th rectangle below $\varepsilon 2^{-j}$. Thus a null set has cube covers of arbitrarily small total volume. A $C^1$ map is Lipschitz on each sufficiently small compact cube by integrating its derivative on segments. A countable cover by such cubes therefore proves local preservation of null sets for $F$ and for $F^{-1}$. In particular images of cube faces are null.

Here is the local volume estimate that supplies the Jacobian. Work in a fixed compact neighborhood on which $DF$ and $DF^{-1}$ are bounded and $DF$ is uniformly continuous. For a small cube $Q$ of side $s$ and center $a$, put $A=DF(a)$ and
\[
 H(x)=a+A^{-1}(F(x)-F(a)).
\]
Use the maximum norm and its induced matrix norm. Uniform continuity permits $s$ so small that $\|DH-I\|\le\varepsilon<1/2$ on every such cube, uniformly. Since $H(a)=a$, the segment formula gives $|H(x)-x|_\infty\le\varepsilon s$ on $Q$. Thus $H(Q)$ lies in the cube obtained by expanding every face of $Q$ by $\varepsilon s$. Conversely, if $y$ lies in the cube obtained by shrinking every face by $\varepsilon s$, the map $x\mapsto y-(H(x)-x)$ takes $Q$ into itself and has contraction constant at most $\varepsilon$. The geometric-iteration proof above gives a fixed point; hence $y\in H(Q)$. Linear volume scaling now gives
\[
 (1-2\varepsilon)^n |\det DF(a)|\,|Q|
 \le |F(Q)|\le
 (1+2\varepsilon)^n |\det DF(a)|\,|Q|.
 \tag{CI5}
\]
The images in question are compact and hence measurable. No unproved assertion that an image fills an approximate parallelepiped is needed: its inner inclusion was proved by the contraction argument.

Take $h\in C_c(V)$. The compact preimage of its support lies in the interior of a finite union $S$ of closed grid cubes contained in $U$. Such a union exists by the positive distance of this compact set from the complement of $U$. Subdivide those cubes into a common fine grid. Their interiors are disjoint; by injectivity their images overlap only on null images of faces. On each small cube $Q$, uniform continuity of $h\circ F$ makes the difference between $\int_{F(Q)}h$ and $h(F(a))|F(Q)|$ at most $\operatorname{osc}_Q(h\circ F)|F(Q)|$. The total error tends to zero since the oscillations tend uniformly to zero and the total image volume stays bounded. Estimate (CI5) then replaces $|F(Q)|$ by $|\det DF(a)||Q|$ with total error tending to zero. The resulting sums converge to $\int_S h(F(x))|\det DF(x)|dx$: the integrand is continuous and its step approximations converge uniformly. Both integrands vanish outside the respective union. This proves (CI4) for $C_c(V)$, for complex functions by their real and imaginary parts.

For completeness this equality determines the full measures. Put $\nu(E)=\int_{F^{-1}(E)}|\det DF(x)|dx$ for Borel $E\subset V$. It is a measure by monotone convergence, finite on compact subsets of $V$. For any open $O\subset V$, continuous functions with compact support in $O$ increase to $1_O$: one explicit choice is
\[
 h_j(y)=\min(1,(j\operatorname{dist}(y,\mathbb R^n\setminus O)-1)_+)
        \min(1,(j-|y|)_+).
\]
If $O=\mathbb R^n$, take the first factor to be one. Monotone convergence and the already proved continuous case give $\nu(O)=|O|$. On each bounded open exhaustion of $V$, the two measures are finite and agree on all relatively open sets, a family closed under finite intersections generating its Borel sets. The pi-lambda argument proved in the Euclidean-product reading makes the measures equal on every Borel set there. Exhaustion gives equality on all Borel sets of $V$. Local null preservation for $F^{-1}$ extends this to completed Lebesgue sets and makes composition with $F$ well defined up to null sets. Simple approximation and monotone convergence prove (CI4) for nonnegative functions. Applying it to the absolute value and then to the positive and negative real and imaginary parts proves the absolutely integrable case.

<a id="polar-substitution"></a>

For completeness, the polar map is $F(r,\theta)=(r\cos\theta,r\sin\theta)$ on $(0,\infty)\times(0,2\pi)$. The [proved trigonometric identities and complete-circle parametrization (EF10)–(EF12)](elementary-functions-and-cutoffs.md#trigonometry-and-period) give determinant $r(\cos^2\theta+\sin^2\theta)=r>0$. They also give bijectivity onto the plane with the nonnegative horizontal ray removed: the norm determines $r$, and the unit-circle parametrization determines the unique angle in that interval. The local inverse theorem and bijectivity make the inverse continuously differentiable on that open image. The removed ray is null by the Euclidean product theorem, since its intersection with each bounded box lies in a product with a singleton of length zero. Therefore (CI4) gives, for every nonnegative measurable $h$, and also for every absolutely integrable complex $h$,
\[
 \begin{gathered}
 \int_{\mathbb R^2}h(x,y)\,dx\,dy\\
 =\int_0^{2\pi}\!\int_0^\infty
 h(r\cos\theta,r\sin\theta)r\,dr\,d\theta.
 \end{gathered}
 \tag{CI8}
\]
This supplies the full polar substitution, with its actual domain and normalization, used in the Fourier Gaussian calculation.

<a id="surface-coordinates"></a>
## Surface coordinates and energy measure

For a $C^1$ embedded hypersurface with a parametrization $\kappa$ of full rank, define its Euclidean area in that chart by
\[
 dS=\sqrt{\det(D\kappa^{T}D\kappa)}\,d\eta.
 \tag{CI6}
\]
Here an embedded chart is a $C^1$ map from an open subset of $\mathbb R^{n-1}$, of rank $n-1$, which is a homeomorphism onto a relatively open part of the hypersurface. Its Gram matrix is positive definite. Indeed, applying the finite Gram–Schmidt construction to the independent columns gives $D\kappa=QR$, where $Q^TQ=I$ and $R$ is square upper triangular with positive diagonal. Thus $\det(D\kappa^TD\kappa)=(\det R)^2>0$. For a zero-dimensional chart the empty determinant is one.

This definition is independent of the parametrization. The transition map on an overlap is actually a $C^1$ diffeomorphism; we verify that before using it. At a common point choose an orthonormal matrix $Q$ spanning the image of $D\kappa_1$. The derivative of $a\mapsto Q^T\kappa_1(a)$ is invertible at that point, since $Q^T$ is an isomorphism on that image. The inverse theorem gives a $C^1$ inverse $g$ on a smaller open coordinate neighborhood. The embedded-chart homeomorphisms let us restrict the overlap so that both images lie there. The transition is then $\psi=g\circ Q^T\kappa_2$, hence is $C^1$. Reversing the two charts proves its inverse is $C^1$ as well. The local expressions agree on overlaps by uniqueness of the chart parameters. In dimension one these are maps between zero-dimensional singletons and the assertion is immediate. On an overlap, write $\kappa_2=\kappa_1\circ\psi$. The chain rule and determinant multiplication give
\[
 \sqrt{\det(D\kappa_2^{T}D\kappa_2)}
 =|\det D\psi|\,
   \sqrt{\det(D\kappa_1^{T}D\kappa_1)}\circ\psi.
\]
Formula (CI4) proves agreement of the chart integrals for nonnegative Borel functions and absolutely integrable functions; completion handles null-set modifications in either chart. Orthogonal ambient changes leave the Gram matrix unchanged, so this is Euclidean surface measure. These local measures define one measure on the hypersurface. To see this explicitly, choose a countable chart cover: the countable family of ambient rational balls is a base, and for each base member whose intersection with the surface lies in a chart choose one such chart; these chosen charts cover the surface. Replace the resulting relatively open chart domains $V_j$ by the disjoint Borel sets $V_j\setminus\bigcup_{i<j}V_i$, and sum their chart measures. On every chart this sum agrees with its own measure by countable additivity and the overlap formula. The same observation proves independence of the chosen cover. Complete the resulting Borel measure to obtain the completed surface measure.

The graph over the tangent plane used in the trace proof follows from local inversion. At a point $\xi$, let $Q:\mathbb R^{n-1}\to T_\xi M$ be an orthonormal parametrization of its tangent plane. In any embedded chart through $\xi$, the derivative of $\eta\mapsto Q^T(\kappa(\eta)-\xi)$ is invertible. Apply (CI1)–(CI2) to use this projection as the new coordinate $v$. Then
$\kappa(v)=\xi+Qv+\nu h(v)$, with $h(0)=0$ and $Dh(0)=0$, exactly as required for tangent-scale concentration. Here extend the columns of $Q$ to an orthonormal basis by finite Gram–Schmidt and let $\nu$ be the last vector. The scalar $h(v)=\nu^T(\kappa(v)-\xi)$ has derivative zero at the origin because the original tangent image is orthogonal to $\nu$. No second derivative is assumed.

For a graph $\kappa(\eta)=(\varphi(\eta),\eta)$, its Gram matrix is $I+\nabla\varphi\,\nabla\varphi^T$. A basis with its first vector parallel to the gradient gives eigenvalues $1+|\nabla\varphi|^2,1,\ldots,1$ (all are one if the gradient is zero). Hence $dS=\sqrt{1+|\nabla\varphi|^2}\,d\eta$. In dimension one this is counting measure on the zero-dimensional surface.

Apply (CI3) to a regular level of a scalar real $p$. The energy map $(\tau,\eta)\mapsto(p(\tau,\eta),\eta)$ has determinant $\partial_\tau p$. Equations (CI3), (CI4) and (CI6) therefore give
\[
 d\xi=|\partial_\tau p|^{-1}\,d\lambda\,d\eta,
 \qquad dS=\frac{|\nabla p|}{|\partial_\tau p|}\,d\eta,
 \qquad d\sigma_\lambda=\frac{dS}{|\nabla p|}.
 \tag{CI7}
\]
These identities prove the local coarea formula by nonnegative product integration, and by absolute integration for signed inputs. More explicitly, on a coordinate patch $U$ where $\Phi(\xi)=(p(\xi),\eta)$ is a diffeomorphism, set $a(t,\eta)=\Phi^{-1}(t,\eta)$ and $J(t,\eta)=|\partial_\tau p(a(t,\eta))|^{-1}$. For a nonnegative measurable $f$ on $U$, extend $f(a(t,\eta))J(t,\eta)$ by zero outside $\Phi(U)$. Applying (CI4) and then the product theorem gives its iterated integral in $t$ and $\eta$. On the slice at $t$, (CI3) and the graph Gram determinant identify $J(t,\eta)d\eta$ with $dS/|\nabla p|$. This proves
\[
 \begin{gathered}
 \int_U f(\xi)\,d\xi\\
 =\int_{\mathbb R}\left(\int_{U\cap p^{-1}(t)}
             f\,\frac{dS}{|\nabla p|}\right)dt.
 \end{gathered}
 \tag{CI9}
\]
For completed-measurable inputs the slices and their integrals are interpreted for almost every $t$, exactly as in the completed product theorem. For absolutely integrable complex $f$, apply the nonnegative formula to $|f|$ and then to the four signed real components. Thus the assertions include the same completed-measurable generality as (CI4).

<a id="regular-level-limit"></a>

We give the continuity and localization details of the regular-level limit. Let $p\in C^1(\Omega;\mathbb R)$ on an open Euclidean set, let $\lambda$ be a regular value, meaning $\nabla p\ne0$ on $p^{-1}(\lambda)$, and let $f\in C_c(\Omega)$ be complex valued. First suppose the support of $f$ is compactly contained in one patch $U$ as above. The function $g(t,\eta)=f(a(t,\eta))J(t,\eta)$ has compact support inside $\Phi(U)$. Extending it by zero gives a continuous compactly supported function on the full coordinate space: outside that compact support it already vanishes on an open neighborhood of the boundary of $\Phi(U)$. It is uniformly continuous and supported in a fixed finite box. Consequently
\[
 q(t)=\int_{\mathbb R^{n-1}}g(t,\eta)\,d\eta
 \tag{CI10}
\]
is continuous with compact support: a difference $|q(t)-q(s)|$ is bounded by the volume of the fixed projected box times the uniform modulus of continuity of $g$. In dimension one the zero-dimensional integral means evaluation and the box volume is one. The slice formula gives $q(\lambda)=\int_{p^{-1}(\lambda)}f\,dS/|\nabla p|$. Formula (CI9) now changes the integral of $P_\varepsilon(p-\lambda)f$ into the integral of $P_\varepsilon(t-\lambda)q(t)$. The [arctangent and Poisson-kernel proof (EF13)–(EF15)](elementary-functions-and-cutoffs.md#arctangent-and-poisson-kernel) therefore proves the desired limit on this patch.

For general $f$, the case $f=0$ is immediate. Otherwise its nonempty compact support $K$ meets the level in a compact set $S$. If $S$ is empty, the continuous function $|p-\lambda|$ has a positive minimum on $K$, and the entire integral tends to zero by the estimate below. Otherwise finitely many such coordinate patches cover $S$, since some partial derivative is nonzero at each point. The compactly supported partition proved in the next section provides smooth $w_j$, each supported compactly in its own patch, whose sum $\chi$ equals one on a neighborhood of $S$. Apply the patch result to each $fw_j$. If the remainder $f(1-\chi)$ is nonzero, its compact support is disjoint from the level, so $|p-\lambda|\ge\delta>0$ on that support. Its absolute integral against $P_\varepsilon(p-\lambda)$ is at most $\varepsilon\|f(1-\chi)\|_1/(\pi\delta^2)$, which tends to zero. A zero remainder contributes nothing. Since the weights sum to one on $S$, their surface integrals add to the full surface integral. We have proved
\[
 \begin{gathered}
 \lim_{\varepsilon\downarrow0}
  \int_\Omega P_\varepsilon(p(\xi)-\lambda)f(\xi)\,d\xi\\
 =\int_{p^{-1}(\lambda)}f\,\frac{dS}{|\nabla p|}.
 \end{gathered}
 \tag{CI11}
\]
The right-hand integral is finite: finitely many compact chart pieces cover its support, and the chart Jacobian and reciprocal gradient are continuous there. This proves $\delta(p-\lambda)=d\sigma_\lambda$ against every compactly supported continuous test, without any regularity requirement on other levels away from the support's neighborhood of $p=\lambda$.

<a id="finite-partitions"></a>
## Finite localization on a compact set

The partitions used above can be constructed explicitly. The [flat-function proof (EF16)–(EF18)](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs) proves the smoothness, support and positivity of the bumps used here, including at their boundary. For each point of a compact set $K$, choose a ball $B(x,r)$ whose doubled closed ball lies in an assigned open coordinate neighborhood. Compactness selects finitely many of the smaller balls covering $K$. On each use a nonnegative smooth bump $\varphi_j$ equal to one on the smaller ball and supported in the larger ball. The plateau construction (EF18) supplies these; a positive interior bump also follows from $e^{-1/(1-|x|^2)}$ inside the unit ball and zero outside, followed by translation and scaling. The sum $s=\sum_j\varphi_j$ is positive on an open neighborhood $W$ of $K$. Dividing each bump by $s$ gives a smooth partition there. Dividing instead by the square root of the sum of the squared bumps gives a partition whose squared terms sum to one. Restriction to a $C^1$ surface gives the continuous partitions needed for its amplitudes.

When functions on the entire ambient open set are required, choose finitely many additional plateau bumps $\psi_l$ with support compactly in $W$, whose regions of value one cover $K$. The same doubled-ball construction gives them. The function $\chi=1-\prod_l(1-\psi_l)$ is smooth, supported compactly in $W$ and equals one on a neighborhood of $K$, with $0\le\chi\le1$. Define $w_j=\chi\varphi_j/s$ on $W$ and zero outside it. This extension is smooth because the support of $\chi$ is a compact subset of $W$. Each $w_j$ has compact support in its assigned chart and $\sum_jw_j=\chi$. This is exactly the global compactly supported partition used in (CI11). The case of an empty compact set requires no terms.

A common patch for intersecting supports is also available. For a finite open cover of a nonempty compact set, a member equal to the whole ambient space already gives the assertion. Otherwise the continuous function $x\mapsto\max_j\operatorname{dist}(x,\mathbb R^n\setminus U_j)$ has a positive minimum $\delta$ on that set. If a subset of diameter less than $\delta$ contains a point $x$ of the compact set, choose $j$ with distance at least $\delta$ at $x$; every point of the subset then lies in $U_j$. Center the supporting balls at points of the compact set and choose their radii less than $\delta/4$. The union of two intersecting closed supports has diameter less than $\delta$ and meets the compact set at a center, so it lies in a common chart. These constructions prove the finite-cover facts used to combine the local radiation formulas.
