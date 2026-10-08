# Coordinate inverses, integration and surface measure

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

A regular energy surface can be described by its energy and its tangential coordinates. To integrate in those coordinates, we need both an inverse map and the correct volume factor. We construct these two ingredients, then identify the surface measure that appears when an approximate delta function concentrates on one energy level.

The starting measure results are [Euclidean measure and products](finite-derivative-l2.md#euclidean-products). The continuous scalar fundamental theorem is proved in [Banach-valued integration, through equation (13)](hilbert-valued-integration.md#continuous-primitives); only its real scalar case is needed here. The same reading proves [finite-dimensional compactness and extrema](hilbert-valued-integration.md#compact-scalar-calculus). These arguments precede Fourier normalization: the polar substitution proved below is an input to the Gaussian calculation in the Fourier reading. We use field operations, completeness of the ordered real numbers and set theory with choice as the underlying axioms. Further reading is given at the end.

<a id="coordinate-linear-algebra"></a>
## 1. Matrices and first-order approximations

We first establish the finite-dimensional rules used in the constructions. For real vectors, the quadratic inequality $|v-tu|^2\geq0$, with $t\in\mathbb R$, gives $|v\cdot u|\leq|v|\,|u|$ by minimization when $u\ne0$; when $u=0$ the assertion is immediate. Applying this bound to the cross term in $|v+w|^2$ proves the triangle inequality. The maximum norm and Euclidean norm satisfy $|v|_\infty\leq|v|\leq\sqrt n\,|v|_\infty$. A Cauchy sequence therefore converges by taking each of its finitely many coordinate limits. A matrix defines a bounded map: its $i$th output coordinate has absolute value at most the absolute row sum times $|v|_\infty$. Applying two matrix bounds successively proves $\|AB\|\leq\|A\|\|B\|$.

The signed permutation sum defines an alternating multilinear determinant, normalized to be one on the standard basis. Conversely, expand the columns of any alternating multilinear function in that basis. Terms with a repeated basis vector vanish; the remaining terms are determined by their permutation signs. This proves uniqueness of the determinant. Apply uniqueness to the columns $Av_1,\ldots,Av_n$ to obtain $\det(AB)=\det A\det B$. The permutation formula also gives $\det A^T=\det A$. Expansion along a row or column proves $A\operatorname{adj}A=(\det A)I$ and its reversed product: off-diagonal entries are determinants with a repeated row or column. Hence $\det A\ne0$ gives an inverse.

We also need the converse without assuming it. If a square matrix has zero kernel, its first column contains a nonzero pivot. Row interchange, nonzero row scaling and subtraction of row multiples reduce it to a first pivot above a smaller square block. That block has zero kernel: a vector annihilated by it could be extended, by solving the first row, to a vector in the original kernel. Induction, starting with a nonzero scalar, reduces the whole matrix to the identity. Thus zero kernel implies invertibility. Each elimination operation has nonzero determinant by the alternating rule, so an invertible matrix has nonzero determinant. These operations also express it as a product of coordinate permutations, single-coordinate scalings and shears.

For independent columns, subtract the orthogonal projections onto the columns already normalized, and divide each residual by its positive norm. Independence prevents a zero residual. This gives an orthonormal basis for their span. Add standard basis vectors outside that span until it is the whole space to obtain an orthonormal extension. In particular, if $M$ has $d$ independent columns, this construction gives $M=QR$, with $Q^TQ=I_d$ and $R$ upper triangular with positive diagonal. Consequently $\det(M^TM)=(\det R)^2>0$. The positive square roots used here are supplied by the earlier scalar measure foundations. In dimension zero the determinant is one and the space consists of one point; all inverse and volume formulas below then have their evident counting-measure meaning.

<a id="coordinate-differential-rules"></a>

Let differentiability mean $F(x+h)=F(x)+Ah+o(|h|)$ with a linear map $A$. This implies continuity and the bound $F(x+h)-F(x)=O(|h|)$. For a differentiable $G$ at $F(x)$, substitute this expansion in the corresponding expansion of $G$. Its linear part is $DG(F(x))A$ and its remaining term is $o(|h|)$, since the intermediate increment is $O(|h|)$. Thus, with $A=DF(x)$ and $B=DG(F(x))$,
\[
 \begin{gathered}
 (G\circ F)(x+h)-(G\circ F)(x)\\
 =BAh+o(|h|).
 \end{gathered}
 \tag{DC1}
\]
The case of a zero intermediate increment causes no exception: the second remainder is then zero. For a bounded bilinear map, expansion of its two arguments leaves the product of their increments after the two first-order terms. That product is $O(|h|^2)$, proving the product rule. Sums and fixed linear maps follow by adding their remainders. For the reciprocal, the exact identity
\[
 \frac1{z+h}-\frac1z+\frac h{z^2}
 =\frac{h^2}{z^2(z+h)}
\]
proves differentiability at every nonzero real or complex $z$. These rules give the usual derivatives of polynomials and rational functions, and their continuous derivatives at every finite order. In particular, the adjugate formula makes matrix inversion smooth where the determinant is nonzero.

Apply the earlier scalar fundamental theorem to each component of $F$ along the segment from $x'$ to $x$. With $v=x-x'$ and $\gamma(t)=x'+tv$, a $C^1$ map defined on a neighborhood of this segment satisfies
\[
 \begin{gathered}
 F(x)-F(x')=\int_0^1 DF(\gamma(t))v\,dt,\\
 |F(x)-F(x')|\le
 |v|\sup_{0\le t\le1}\|DF(\gamma(t))\|.
 \end{gathered}
 \tag{DC2}
\]
To justify the vector norm bound using only scalar integration, pair a nonzero integral with its own unit direction and apply the scalar integral inequality and the vector inequality proved above. A zero integral already satisfies the bound. The same argument applies to either of the equivalent finite-dimensional norms.

<a id="coordinate-inverse"></a>
## 2. Solving for coordinates

Suppose $F:U\to\mathbb R^n$ is $C^1$, $U$ is open and $DF(x_0)$ is invertible. Translate $x_0$ and $F(x_0)$ to zero, then multiply the output by $DF(x_0)^{-1}$. It is enough to construct an inverse when $F(0)=0$ and $DF(0)=I$. Choose $r>0$ so that $\overline B(0,r)\subset U$ and $\|DF-I\|\leq1/2$ on that ball. The segment formula applied to $F-I$ gives
\[
 \begin{gathered}
 |F(x)-F(x')-(x-x')|\le\tfrac12|x-x'|,\\
 |F(x)-F(x')|\ge\tfrac12|x-x'|.
 \end{gathered}
 \tag{CI1}
\]
In particular $F$ is injective there. Also $|DF(x)v|\geq|v|/2$, so each $DF(x)$ has zero kernel and hence an inverse of norm at most two, by the finite linear algebra above.

One can also construct this matrix inverse explicitly. Write $DF(x)=I-H$, where $\|H\|\leq1/2$. The partial sums $\sum_{j=0}^N H^j$ are Cauchy in the finite-dimensional matrix space, and multiplication by $I-H$ on either side gives $I-H^{N+1}$. Their limit is therefore the two-sided inverse, with norm at most $\sum_{j\geq0}2^{-j}=2$.

**Existence by a minimum.** Fix $|y|<r/4$ and minimize $|F(x)-y|^2$ on the closed ball. A minimum exists by the earlier compactness and extreme-value proof. At $x=0$ its value is less than $r^2/16$. On the boundary, (CI1) gives $|F(x)-y|\geq r/2-|y|>r/4$. A minimizing point is therefore interior. Each directional derivative there vanishes: its one-variable difference quotients from the positive and negative sides have opposite signs and the same limit. Differentiating the square gives
\[
 DF(x)^T(F(x)-y)=0.
\]
The transpose is invertible, so $F(x)=y$. Injectivity makes this solution unique; denote it by $G(y)$. Formula (CI1) gives $|G(y)|\leq2|y|<r$ and $|G(y)-G(z)|\leq2|y-z|$. The open set $B(0,r)\cap F^{-1}(B(0,r/4))$ is thus mapped bijectively onto $B(0,r/4)$, with a continuous inverse.

**A convergent alternative.** The same normalized equation can be solved on the larger target ball $|y|<r/2$ by iteration. Set $T_y(x)=x-F(x)+y$. Equation (CI1) shows that $T_y$ maps the closed ball of radius $r$ into itself and has Lipschitz constant at most $1/2$. Choose $x_1$ in that ball and put $x_{j+1}=T_y(x_j)$. Then $|x_{j+1}-x_j|\leq2^{1-j}|x_2-x_1|$. Summing this geometric bound proves that the iterates are Cauchy. Their limit is in the closed ball and solves $T_y(x)=x$ by continuity. The contraction inequality excludes two distinct fixed points. This gives the same inverse on the smaller ball, and extends the construction to $B(0,r/2)$, still with $|G(y)|\leq2|y|<r$. It also gives an explicit tail bound by summing the remaining successive differences.

To obtain the derivative, let $x=G(y)$ and $h=G(y+k)-G(y)$. The Lipschitz bound gives $|h|\leq2|k|$, whereas differentiability of $F$ gives $k=DF(x)h+o(|h|)$. Multiply by the bounded matrix inverse to obtain
\[
 G(y+k)-G(y)=DF(G(y))^{-1}k+o(|k|).
 \tag{CI2}
\]
The identity $A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}$ proves continuity of matrix inversion here. Hence (CI2) gives a continuous derivative. Undoing the initial affine transformations proves the $C^1$ inverse theorem at $x_0$. Applying it at every point shows that an everywhere nonsingular $C^1$ map is locally open. If it is also injective, its local inverse maps agree on overlaps and give a $C^1$ diffeomorphism onto its open image.

<a id="coordinate-holder-inverse"></a>

**Finite regularity.** If $F$ is $C^k$, differentiate $DG=(DF\circ G)^{-1}$ repeatedly. The identity obtained by differentiating $A^{-1}A=I$ is $d(A^{-1})=-A^{-1}(dA)A^{-1}$. Together with the product and chain rules it shows inductively that every derivative of $G$ of order $j\leq k$ is a finite sum of products of factors $(DF\circ G)^{-1}$ and $(D^\ell F)\circ G$, with $\ell\leq j$. This both proves $G\in C^k$ and identifies precisely the required derivatives of $F$.

Now let $F\in C^{k,\alpha}_{\mathrm{loc}}$, where $k\geq1$ and $0<\alpha<1$. The [real-power construction](elementary-functions-and-cutoffs.md#logarithm-and-real-powers) supplies the powers in these seminorms. On smaller compact coordinate neighborhoods, $G$ is Lipschitz, all factors in the preceding formulas are bounded, and the inverse matrices have a uniform bound. A Hölder function composed with an $L$-Lipschitz map has Hölder seminorm multiplied by at most $L^\alpha$. The difference of a finite product is the sum of terms obtained by replacing one factor at a time, so products of bounded Hölder functions are Hölder. Derivatives $D^\ell F$ with $\ell<k$ are locally Lipschitz by (DC2). On a set of diameter $D>0$, a Lipschitz bound implies a Hölder bound through $d\leq D^{1-\alpha}d^\alpha$; a singleton needs no estimate. For $k=1$, the matrix inverse difference identity directly preserves the Hölder bound of $DF\circ G$. For $k>1$ it does the same, with local Lipschitz control available. Therefore the formula for $D^kG$ is Hölder. All constants depend only on the chosen chart sizes, the inverse first-derivative bound and the stated finite bounds for $F$. Applying the finite-order argument for every $k$ proves the smooth case.

For a real function $p(\tau,\eta)$ with $\partial_\tau p\ne0$, the map $(\tau,\eta)\mapsto(p(\tau,\eta),\eta)$ has an invertible triangular derivative. Its local inverse is $(\lambda,\eta)\mapsto(\Sigma(\lambda,\eta),\eta)$. Differentiating $p(\Sigma(\lambda,\eta),\eta)=\lambda$ gives
\[
 \begin{gathered}
 \partial_\lambda\Sigma=(\partial_\tau p)^{-1},\\
 \partial_{\eta_j}\Sigma=-\partial_{\eta_j}p/(\partial_\tau p).
 \end{gathered}
 \tag{CI3}
\]
The derivatives on the right are evaluated at $(\Sigma,\eta)$. The inverse has the same $C^1$, $C^{k,\alpha}$ or smooth regularity just proved, according to the hypothesis on $p$.

<a id="coordinate-integration"></a>
## 3. The local volume factor

Let $F:U\to V$ be a $C^1$ diffeomorphism between open subsets of $\mathbb R^n$. We will prove
\[
 \int_V h(y)\,dy=\int_U h(F(x))\,|\det DF(x)|\,dx
 \tag{CI4}
\]
for every nonnegative completed-Lebesgue-measurable function, and for every absolutely integrable complex function. We use a volume estimate first, then extend the resulting identity from continuous tests to measures.

**Linear maps and null sets.** A coordinate permutation preserves product measure. Multiplying one coordinate by a nonzero number scales length, first for intervals and then for outer measure by scaling the interval covers; it therefore scales product measure by that number's absolute value. For a shear, fix all coordinates except the coordinate being changed. The fiber is translated, so its length is unchanged, and the product theorem gives unchanged volume. The elimination factorization from Section 1 consequently shows that an invertible linear map $A$ scales Borel volume by $|\det A|$. Applying the same operations to nonnegative simple functions, and then their increasing limits, gives the corresponding integral identity.

Here is the null-set fact needed for completed measures. If a map is $L$-Lipschitz on a bounded cube, intersect that cube with a cover of a null subset by cubes of side lengths $s_j$. In every nonempty intersection choose one point. The image of the intersection lies in a cube centered at its image point, of side $2L\sqrt n\,s_j$. Thus its image has outer measure at most $(2L\sqrt n)^n s_j^n$. Summing and letting the covering volume tend to zero proves that the image is null. If $L=0$, the image is a singleton and the conclusion follows directly. Cube covers of arbitrarily small volume are available from the rectangular definition of null sets: a rectangle with side lengths $l_i$ can be covered by fine mesh cubes with total volume approaching $\prod_i l_i$; for a countable collection of rectangles assign excess less than $\varepsilon2^{-j}$ to its $j$th member. A $C^1$ map is Lipschitz on each sufficiently small closed cube, by (DC2). Rational cubes give a countable cover of its open domain. Hence both $F$ and $F^{-1}$ preserve null sets locally and therefore globally. In particular the images of cube faces are null, and linear volume scaling extends to completed measurable sets.

**Small cubes.** Work on a compact neighborhood contained in $U$. There $DF$ is uniformly continuous and its inverse is bounded. For a closed cube $Q$ of side $s$, center $a$, contained in this neighborhood, set $A=DF(a)$ and $H(x)=a+A^{-1}(F(x)-F(a))$. Given $0<\varepsilon<1/2$, all sufficiently small such cubes satisfy $\|DH-I\|_\infty\leq\varepsilon$ uniformly. The segment formula gives $|H(x)-x|_\infty\leq\varepsilon s$. Thus $H(Q)$ is contained in the cube with each face moved outward by $\varepsilon s$.

The cube with each face moved inward by $\varepsilon s$ is also contained in $H(Q)$; we prove this rather than assuming that an almost linear image has no holes. Let $Q^-$ be the open inner cube. A boundary point $x$ of $Q$ has a coordinate equal to a face coordinate, so $H(x)$ cannot lie in $Q^-$ by the preceding bound. The set $H(Q)\cap Q^-$ is relatively closed in $Q^-$ because $H(Q)$ is compact. It is also relatively open: any preimage of a point of $Q^-$ is in the interior of $Q$, where the inverse theorem makes $H$ locally open. It contains the center, since $H(a)=a$. For $y\in Q^-$, the segment $a+t(y-a)$ stays in $Q^-$. Its parameters lying in $H(Q)$ form a closed and relatively open subset of $[0,1]$ containing zero. Such a subset is all of $[0,1]$: otherwise the supremum of its initial interval belongs to the subset by closedness and can be extended by openness, a contradiction. Therefore $y\in H(Q)$.

The inner inclusion also admits a convergent construction. For $y\in Q^-$, the map $x\mapsto x-H(x)+y$ takes $Q$ into itself, since each coordinate changes from $y$ by at most $\varepsilon s$. Its Lipschitz constant in the maximum norm is at most $\varepsilon<1$. The geometric Cauchy argument of Section 2 gives a fixed point in the complete closed cube, and that point satisfies $H(x)=y$.

Linear scaling and the two inclusions now give
\[
 \begin{gathered}
 (1-2\varepsilon)^n |\det DF(a)|\,|Q|\le |F(Q)|,\\
 |F(Q)|\le (1+2\varepsilon)^n |\det DF(a)|\,|Q|.
 \end{gathered}
 \tag{CI5}
\]
All images used here are compact, hence measurable. The constants are uniform over the chosen compact neighborhood. The absolute determinant is essential; no orientation assumption was made.

**Continuous functions.** For $h\in C_c(V)$, the set $F^{-1}(\operatorname{supp}h)$ is compact. Enclose it in the interior of a finite union $S$ of closed grid cubes contained in $U$. To construct $S$, use the positive distance of this compact set from the complement of $U$ and a sufficiently fine grid, including the neighboring cubes that meet its boundary. When $U=\mathbb R^n$, any sufficiently large finite grid neighborhood suffices; when $h=0$, the identity is immediate. Subdivide $S$ into cubes $Q$. Injectivity makes their image interiors disjoint except for images of their faces, which have measure zero. On each image, replace $h$ by its value $h(F(a))$ at the center image. The error is at most the oscillation of $h\circ F$ on $Q$ times $|F(Q)|$. Uniform continuity makes the sum of these errors tend to zero, since the total image volume is $|F(S)|<\infty$. Equation (CI5) replaces $|F(Q)|$ by $|\det DF(a)||Q|$, again with total error tending to zero. The resulting sums tend to the integral of the continuous function $h(F(x))|\det DF(x)|$ on $S$, by uniform convergence of its cube step approximations. Both sides vanish outside the relevant unions. This proves (CI4) for continuous compactly supported complex $h$.

**Measurable functions.** Define $\nu(E)=\int_{F^{-1}(E)}|\det DF|\,dx$ for Borel $E\subset V$. This is a measure by monotone convergence and is finite on compact subsets. For an open $O\subset V$, the continuous functions
\[
 h_j(y)=\min\{1,(j\operatorname{dist}(y,\mathbb R^n\setminus O)-1)_+\}
        \min\{1,(j-|y|)_+\}
\]
increase to $1_O$ and have compact support in $O$. If $O=\mathbb R^n$, use one for the first factor. The continuous case and monotone convergence imply $\nu(O)=|O|$. Exhaust $V$ by bounded open sets whose closures are compact in $V$, for example by imposing $|y|<j$ and distance greater than $1/j$ from its complement; omit the distance condition when $V=\mathbb R^n$. On each, the two finite measures agree on all relatively open sets. These sets are closed under finite intersections and generate the Borel sets, so the earlier [measure uniqueness proof](finite-derivative-l2.md#general-product-measures) by the pi-lambda argument gives equality on every Borel set. Exhaustion gives equality throughout $V$. Pullback by $F$ also preserves completed measurability, since $F^{-1}$ takes null sets to null sets. The equality therefore extends to the completed measures. Increasing simple approximation proves (CI4) for nonnegative $h$. Applying it to $|h|$ and then to the positive and negative real and imaginary parts proves the absolutely integrable complex case.

<a id="polar-substitution"></a>
## 4. Polar and surface coordinates

The map $(r,\theta)\mapsto(r\cos\theta,r\sin\theta)$, on $(0,\infty)\times(0,2\pi)$, has determinant $r$. The [trigonometric identities and circle parametrization](elementary-functions-and-cutoffs.md#trigonometry-and-period) prove this calculation and show that its image is the plane with the nonnegative horizontal ray removed. Its radius and angle are unique there. Local inversion and this bijectivity make it a $C^1$ diffeomorphism onto that open image. The omitted ray is null: its bounded pieces lie in products of intervals with a zero-length singleton. Equation (CI4) gives
\[
 \begin{gathered}
 \int_{\mathbb R^2}h(x,y)\,dx\,dy\\
 =\int_0^{2\pi}\!\int_0^\infty
 h(r\cos\theta,r\sin\theta)r\,dr\,d\theta.
 \end{gathered}
 \tag{CI8}
\]
This holds for nonnegative measurable $h$ and for absolutely integrable complex $h$, with completed-measure interpretation. It supplies the polar normalization used in the Fourier Gaussian integral.

<a id="surface-coordinates"></a>

Let $M$ be a $C^1$ embedded hypersurface in $\mathbb R^n$, $n\geq1$. A chart $\kappa$ is a rank-$n-1$ map from an open subset of $\mathbb R^{n-1}$ that is a homeomorphism onto a relatively open subset of $M$. Define the chart area element by
\[
 dS=\sqrt{\det(D\kappa^TD\kappa)}\,d\eta.
 \tag{CI6}
\]
Its Gram determinant is positive by the orthogonalization in Section 1. For $n=1$ the empty determinant is one and the chart consists of one point, with counting measure.

We check coordinate independence, including differentiability of the transition map. At a common point of two charts, choose an orthonormal matrix $Q$ spanning the tangent image of $D\kappa_1$. The map $a\mapsto Q^T\kappa_1(a)$ has invertible derivative there. Let $g$ be its local $C^1$ inverse. Shrink the overlap using the two chart homeomorphisms; then the transition from chart 2 to chart 1 is $g\circ Q^T\kappa_2$. It is $C^1$, and the reversed construction proves that its inverse is $C^1$. If $\kappa_2=\kappa_1\circ\psi$, the chain rule and determinant multiplication give
\[
 \sqrt{\det(D\kappa_2^TD\kappa_2)}
 =|\det D\psi|\,
   \sqrt{\det(D\kappa_1^TD\kappa_1)}\circ\psi.
\]
Equation (CI4) identifies the chart integrals on overlaps. The rational-ball base of ambient Euclidean space gives a countable chart cover: for each base member whose intersection with $M$ is contained in some chart, choose one such chart. Subtract the earlier chart domains from each successive domain to form disjoint Borel pieces, and sum their chart measures. The overlap identity and countable additivity show that this gives each original chart measure and is independent of the chosen cover. Complete this Borel measure. Orthogonal changes of ambient coordinates preserve the Gram matrix, so the resulting measure is Euclidean surface measure. No orientation or second derivative of $M$ is required.

The tangent-plane graph also follows from the same inverse construction. At $\xi\in M$, choose orthonormal tangent columns $Q$ and a unit normal $\nu$. Projection of a chart onto $Q$ has invertible derivative. Use $v=Q^T(\kappa-\xi)$ as coordinates. Then the chart is
\[
 \kappa(v)=\xi+Qv+\nu h(v),\qquad h(0)=0,\quad Dh(0)=0.
\]
The final derivative vanishes because the tangent image is orthogonal to $\nu$. For a graph $(\varphi(\eta),\eta)$ the Gram matrix is $I+\nabla\varphi\,\nabla\varphi^T$. In a basis beginning with the gradient direction its diagonal eigenvalues are $1+|\nabla\varphi|^2,1,\ldots,1$; for a zero gradient it is the identity. Thus $dS=\sqrt{1+|\nabla\varphi|^2}\,d\eta$, including the zero-dimensional convention.

## 5. Integrating by energy

Suppose $p\in C^1(\Omega;\mathbb R)$ and $\partial_\tau p\ne0$ on a coordinate patch where $\Phi(\tau,\eta)=(p(\tau,\eta),\eta)$ is a diffeomorphism. Write its inverse as $a(\lambda,\eta)=(\Sigma(\lambda,\eta),\eta)$. Its Jacobian, the graph formula above and (CI3) imply
\[
 \begin{gathered}
 d\xi=|\partial_\tau p|^{-1}\,d\lambda\,d\eta,\\
 dS=\frac{|\nabla p|}{|\partial_\tau p|}\,d\eta,\qquad
 d\sigma_\lambda=\frac{dS}{|\nabla p|}.
 \end{gathered}
 \tag{CI7}
\]
Every factor on the right is evaluated at the inverse point. The absolute values include either sign of $\partial_\tau p$.

For a nonnegative measurable $f$ on this patch $U$, extend $f(a(t,\eta))|\partial_\tau p(a(t,\eta))|^{-1}$ by zero off $\Phi(U)$. Change of variables and the product theorem identify its full integral with its iterated integral in $t$ and $\eta$. At each regular slice the graph Gram determinant gives exactly the area factor in (CI7). Hence
\[
 \begin{gathered}
 \int_U f(\xi)\,d\xi\\
 =\int_{\mathbb R}\left(\int_{U\cap p^{-1}(t)}
              f\,\frac{dS}{|\nabla p|}\right)dt.
 \end{gathered}
 \tag{CI9}
\]
For completed-measurable $f$, the slice statement and inner integrals are interpreted for almost every $t$, as in the completed product theorem. Apply the formula first to $|f|$ and then to its four nonnegative real components for absolutely integrable complex $f$. This proves the full local coarea formula used here.

<a id="finite-partitions"></a>
## 6. Localizing a compact set

Let $K$ be compact and covered by open coordinate neighborhoods. For each of its points choose a ball whose doubled closed ball remains in one assigned neighborhood. Finitely many smaller balls cover $K$. The [smooth plateau construction](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs) gives $0\leq\varphi_j\leq1$, equal to one on each smaller ball and supported in its doubled ball. The function $s=\sum_j\varphi_j$ is positive on an open neighborhood $W$ of $K$, and $\varphi_j/s$ sum to one there. Alternatively, $\varphi_j/(\sum_l\varphi_l^2)^{1/2}$ have squared sum one; the positive square root is smooth by the proved real-power calculus. Restriction to a $C^1$ surface gives continuous weights on that surface. An alternative bump, positive throughout the unit ball, is $e^{-1/(1-|x|^2)}$ inside that ball and zero outside; the same flat-function proof establishes smoothness across its boundary, and translation and scaling give the corresponding bump on any ball.

To obtain functions defined on the whole ambient open set, cover $K$ by finitely many further plateau regions with functions $0\leq\psi_l\leq1$ supported compactly inside $W$. Set $\chi=1-\prod_l(1-\psi_l)$. Then $0\leq\chi\leq1$, its support is compact in $W$, and it is one near $K$. Define $w_j=\chi\varphi_j/s$ on $W$, extending it by zero outside. This is smooth because $\chi$ vanishes on a neighborhood of the complement of $W$. Each $w_j$ is compactly supported in its assigned chart and $\sum_jw_j=\chi$. The same multiplication gives compactly supported squared partitions that have squared sum one near $K$. An empty compact set requires no terms.

We will also need intersecting supports to share a chart. For a finite cover $U_j$ of a nonempty compact set, first dispose of the case where one $U_j$ is the entire ambient space. Otherwise each distance to its closed complement is a continuous function: the triangle inequality makes distance to a fixed nonempty set 1-Lipschitz. The maximum of these finitely many distances has a positive minimum $\delta$ on $K$. A subset of diameter less than $\delta$ meeting $K$ at $x$ lies in any cover member whose complement has distance at least $\delta$ from $x$. Choose the supporting balls above centered in $K$ with radii less than $\delta/4$. The union of two intersecting closed supports has diameter less than $\delta$ and contains one of those centers. It is therefore contained in a common chart. This is the finite localization property used when combining radiation formulas.

<a id="regular-level-limit"></a>
## 7. Concentration on a regular level

Let $p\in C^1(\Omega;\mathbb R)$, let $\lambda$ be a regular value, and let $f\in C_c(\Omega)$ be complex valued. Thus $\nabla p\ne0$ on $p^{-1}(\lambda)$; other levels may have critical points. Put $P_\varepsilon(t)=\varepsilon/(\pi(t^2+\varepsilon^2))$.

First assume that $f$ has compact support in one energy-coordinate patch $U$ from Section 5. Set $g(t,\eta)=f(a(t,\eta))|\partial_\tau p(a(t,\eta))|^{-1}$. Its support is compact inside $\Phi(U)$, so its extension by zero is a continuous compactly supported function on the entire coordinate space. In particular it is uniformly continuous and supported in a fixed box. Therefore
\[
 q(t)=\int_{\mathbb R^{n-1}}g(t,\eta)\,d\eta
 \tag{CI10}
\]
is continuous and compactly supported: the difference at two values of $t$ is bounded by the projected box volume times the uniform modulus of continuity of $g$. For $n=1$, this integral is evaluation in the zero-dimensional variable and the volume is one. The slice identity gives $q(\lambda)=\int_{p^{-1}(\lambda)}f\,dS/|\nabla p|$. By (CI9), the integral of $P_\varepsilon(p-\lambda)f$ is the integral of $P_\varepsilon(t-\lambda)q(t)$. The [proved Poisson-kernel approximate identity](elementary-functions-and-cutoffs.md#arctangent-and-poisson-kernel) makes the latter tend to $q(\lambda)$.

For general $f$, let $K=\operatorname{supp}f$ and $S=K\cap p^{-1}(\lambda)$. If $S$ is nonempty, it is compact, and some partial derivative of $p$ is nonzero near each of its points. Finitely many energy-coordinate patches cover it. Section 6 supplies smooth functions $w_j$ compactly supported in those patches, with sum $\chi=1$ near $S$. Apply the patch result to $fw_j$. The remaining function $f(1-\chi)$ has compact support disjoint from $p^{-1}(\lambda)$. If it is nonzero, compactness gives $|p-\lambda|\geq\delta>0$ on its support, and its integral against $P_\varepsilon(p-\lambda)$ has absolute value at most $\varepsilon\|f(1-\chi)\|_1/(\pi\delta^2)$, which tends to zero. If $S$ is empty, the same argument applies directly to $f$; if $f=0$, there is nothing to prove. The surface integrals of the chart pieces add to the integral of $f$ because their weights sum to one near $S$. We conclude that
\[
 \begin{gathered}
 \lim_{\varepsilon\downarrow0}
   \int_\Omega P_\varepsilon(p(\xi)-\lambda)f(\xi)\,d\xi\\
 =\int_{p^{-1}(\lambda)}f\,\frac{dS}{|\nabla p|}.
 \end{gathered}
 \tag{CI11}
\]
The surface integral is finite: its support is covered by finitely many compact chart pieces, on which the Jacobian and reciprocal gradient are bounded. This proves the identity $\delta(p-\lambda)=d\sigma_\lambda$ against every compactly supported continuous test, including empty levels and either sign of the graph derivative.

## Further reading

Jiří Lebl, [*Basic Analysis II*, version 6.3, 15 May 2026](https://www.jirka.org/ra/realanal2.pdf), Section 8.5, printed pages 51–57, treats inverse and implicit functions; Section 10.7, printed pages 134–137, treats change of variables. The complete programme arguments above also supply the completed-measure, finite Hölder, surface and regular-level forms used by the later lessons.
