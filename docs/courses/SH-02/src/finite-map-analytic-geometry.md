# SH02-FAG-UNIT — Analytic geometry for finite maps

A finite holomorphic map can ramify and can have image of positive codimension. The stratifications needed for sheaf theory must accommodate both phenomena. This lesson constructs compatible strata near a finite fibre, beginning with a prescribed coefficient stratification. It also proves the dimension and conormal consequences used in finite holomorphic microsupport.

The opening constructions use the named analytic contracts below. The later sections prove the component, dimension, finite-map, extension, normalization and Whitney-criterion results from their stated local algebra and holomorphic-calculus inputs.

## SH02-FAG-CONTRACT — Analytic inputs and conventions

All analytic spaces are reduced complex analytic spaces. Their dimensions are complex dimensions. A finite holomorphic map means a proper holomorphic map with finite fibres. A complex analytic stratification is locally finite, has connected smooth locally closed strata, and has analytic stratum closures and boundaries. No global finite number of strata is assumed.

The initial constructions use the following analytic contracts; their proof routes are developed in the subsequent sections.

| Contract | Required fact | Exact mathematical source |
| --- | --- | --- |
| Analytic components | Locally finite irreducible components, a dense regular locus, analytic singular loci, and strict dimension drop for a proper analytic subset of an irreducible space | Demailly, II.4.24, II.4.26, II.4.31 and II.5.3, pp.98, 100, 102–103 |
| Finite equations | The ideal sheaf of an analytic subset is coherent; locally it has finitely many generators | Demailly, II.4.29, pp.99–100 |
| Analytic difference | For closed analytic subsets $A,B$, the closure of $A\setminus B$ is analytic | Demailly, II.5.4, p.103 |
| One equation | On an irreducible analytic space, a holomorphic function which is not identically zero has an empty zero set or a zero set of pure codimension one | Demailly, II.6.2, p.106 |
| Finite image | A proper holomorphic image is analytic; a finite surjective holomorphic map preserves dimension | Demailly, II.8.8, pp.118–119, and II.8.1(b), p.116 |
| Whitney failure | If $H$ is reduced and equidimensional and $C\subset H$ is closed analytic, the points of $C$ where $(H_{\mathrm{reg}},C)$ fails the Whitney conditions form a closed analytic subset which is nowhere dense in $C$ | Teissier, VI.2.1, p.477 |

Demailly references mean the 21 June 2012 version of [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Teissier references mean [*Variétés polaires II*, Lecture Notes in Mathematics 961 (1982), pp.314–491](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf). The complex inverse and constant-rank theorems are also used. The cited works identify the mathematical antecedents. The proof sections below state exactly which local algebra, coherence and analytic-geometry results they use.

The dimension bound below is derived from the one-equation theorem. The inequality printed in Demailly II.6.3 in that version points in the opposite direction; it is not the assertion used here.

<a id="SH02-FAG-HOLOMORPHIC-CALCULUS"></a>


## Holomorphic calculus and local coordinates

The finite-map arguments use holomorphic coordinates at regular points. We now prove the inverse, implicit and constant-rank theorems used there, together with the Cauchy, Laurent and residue facts used in preparation and bounded removal. These are local assertions on complex manifolds. Applying them to a singular analytic space means applying them on its regular locus or to specified ambient equations; no inverse theorem at an arbitrary singular point is asserted.

The starting facts are completeness of the real numbers, finite-dimensional linear algebra, compactness of closed bounded Euclidean sets, and elementary real differentiation and integration, including the chain rule, the fundamental theorem of calculus and Fubini's theorem for continuous functions on compact domains. The contraction estimate is also proved in the smooth foundations. We give the holomorphic dependence argument explicitly here. This is an independently written proof of these local calculus statements.

### Cauchy's formula from real integration

Initially, a scalar function on an open subset of \(\mathbb C^n\) is called holomorphic if it is \(C^1\) in the real variables and its real differential is complex linear. For \(z=x+iy\) write \(\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y)\). In one variable the defining condition is \(\partial_{\bar z}f=0\). Sums, products and compositions have this property by the real chain and product rules; the reciprocal does too wherever the function is nonzero.

For a \(C^1\) function \(h\) near a closed disk with finitely many disjoint smaller closed disks removed, give its boundary the orientation with the region on the left. Real integration gives

\[
\int_{\partial K}h(z)\,dz
=\iint_K(ih_x-h_y)\,dx\,dy
=2i\iint_K\partial_{\bar z}h\,dx\,dy.
\tag{HC1}
\]

Here is the real integration step at precisely the needed domains. For a region between two graphs \(y=\ell(x)\) and \(y=u(x)\), the fundamental theorem of calculus gives \(-\iint h_y=\int(h(x,\ell(x))-h(x,u(x)))\,dx\), which is the contribution of the horizontal differential \(h\,dx\) to the positively oriented boundary. The corresponding computation between graphs in the other coordinate gives \(\iint h_x=\int_{\partial K}h\,dy\). Partition disk regions with circular holes into finitely many such strips, splitting at the horizontal and vertical extremities of their boundary circles. Internal boundary integrals cancel. The circle endpoints follow by a limit; \(h\) and its first derivatives are bounded and the omitted areas and boundary arcs tend to zero. This proves HC1 without importing a complex contour theorem.

Let \(f\) be holomorphic on a neighborhood of the closed disk \(|z-a|\leq R\), and let \(|w-a|<R\). Apply HC1 to \(h(z)=f(z)/(z-w)\) outside a small disk centered at \(w\). Its antiholomorphic derivative vanishes. The inner boundary is clockwise; writing its integral with positive circle orientation therefore gives

\[
\begin{aligned}
f(w)&=\frac1{2\pi i}\int_{|z-a|=R}\frac{f(z)}{z-w}\,dz,\\
\frac1{2\pi i}\int_{|z-w|=\varepsilon}
       \frac{f(z)}{z-w}\,dz
&=\frac1{2\pi}\int_0^{2\pi}f(w+\varepsilon e^{it})\,dt
\longrightarrow f(w).
\end{aligned}
\tag{HC2}
\]

The same integration argument proves that the integral of a holomorphic function around a disk, or around the boundary of one of these regions with holes, is zero.

For a closed polydisk \(\prod_{j=1}^n\{|z_j-a_j|\leq R_j\}\) contained in the domain, apply HC2 in each variable. The continuity of the integrand and the positive separation of the interior point from all boundary circles justify the repeated integrations and Fubini. If \(\Gamma\) is the product of the positively oriented circles, the result is

\[
f(w)=\frac1{(2\pi i)^n}
       \int_\Gamma
       \frac{f(z)\,dz_1\cdots dz_n}
       {\prod_{j=1}^n(z_j-w_j)}.
\tag{HC3}
\]

For \(|w_j-a_j|\leq r_j<R_j\), expand each denominator by its geometric series. The product series converges absolutely and uniformly on the circles and on that smaller polydisk, so it can be integrated term by term. With \(\alpha=(\alpha_1,\ldots,\alpha_n)\in\mathbb N^n\), \(R^\alpha=\prod_jR_j^{\alpha_j}\) and \(M=\sup_\Gamma|f|\), this gives

\[
\begin{aligned}
f(w)&=\sum_{\alpha\in\mathbb N^n}c_\alpha(w-a)^\alpha,\\
c_\alpha&=\frac1{(2\pi i)^n}
          \int_\Gamma
          \frac{f(z)\,dz_1\cdots dz_n}
          {\prod_j(z_j-a_j)^{\alpha_j+1}},\\
|c_\alpha|&\leq M R^{-\alpha},
\qquad
\partial^\alpha f(a)=\alpha!\,c_\alpha.
\end{aligned}
\tag{HC4}
\]

Each differentiated series converges uniformly on every smaller polydisk: its extra powers of the indices are summable against \(\prod_j(r_j/R_j)^{\alpha_j}\). Thus \(f\) is smooth, all its complex derivatives are holomorphic, and its Taylor coefficients are those in HC4. Conversely, a locally convergent power series is holomorphic by the same differentiated convergence. A continuous function separately holomorphic in each variable also satisfies HC3 by repeated one-variable integration, and therefore has such a joint power series. The continuity hypothesis is retained in this last assertion.

### Limits, parameters and analytic continuation

If holomorphic functions \(f_\nu\) converge uniformly on compact subsets to \(f\), their limit is continuous. On each product of boundary circles the convergence is uniform, so HC3 passes to the limit. Expanding its kernel on a smaller polydisk proves that \(f\) is holomorphic; HC4 also proves local uniform convergence of every derivative. These statements apply componentwise to maps with values in \(\mathbb C^m\).

More generally let \(T\) be a compact parameter interval or a finite product of parametrized circles. Suppose \(h(t,p)\) is jointly continuous on \(T\times U\) and holomorphic in \(p\in U\subset\mathbb C^n\) for every \(t\). Integrating against a fixed continuous weight on \(T\) gives a holomorphic function of \(p\). Indeed, on each compact polydisk in \(U\), HC3 for \(h(t,\cdot)\) can be integrated in \(t\). Fubini is applicable because the product integrand is continuous on a compact set. The resulting Cauchy kernel expansion is locally uniformly convergent, by the common bound for \(h\) on \(T\) times the boundary torus. This is the parameter argument needed for contour-defined coefficients. Contour derivatives such as \(g_w/g\) are covered when a common zero-free collar has been established.

If all derivatives of a holomorphic \(f\) vanish at a point, HC4 makes \(f\) zero on a neighborhood. On a connected domain, the set of points at which all derivatives vanish is both open and closed: openness follows from the local expansion, and closedness from continuity of each derivative. Therefore vanishing on a nonempty open subset implies vanishing everywhere. Connectedness here is ordinary topological connectedness, and no analytic-space component theorem is used.

In one variable a nonzero germ consequently has a least nonzero Taylor coefficient. Factoring its order gives \(f(z)=(z-a)^m u(z)\) with \(u\) holomorphic and \(u(a)\ne0\). After shrinking, \(u\) has no zeros, so the zero \(a\) is isolated and its multiplicity is \(m\). A holomorphic function not identically zero on a connected neighborhood of a closed disk and nonzero on its boundary thus has only finitely many zeros in the disk: an infinite set would have an accumulation point in that compact disk, contradicting either the boundary condition or isolation.

### Laurent coefficients, removal and residues

Let \(f\) be holomorphic on \(a<|z|<b\), where \(0\leq a<b\). For \(a<r<|w|<s<b\), remove a small disk centered at \(w\) from the annulus between the two circles. HC1 and the limiting argument for HC2 yield

\[
\begin{aligned}
f(w)&=
\frac1{2\pi i}\int_{|z|=s}\frac{f(z)}{z-w}\,dz
-\frac1{2\pi i}\int_{|z|=r}\frac{f(z)}{z-w}\,dz
=\sum_{k\in\mathbb Z}c_k w^k,\\
c_k&=\frac1{2\pi i}\int_{|z|=\rho}
             f(z)z^{-k-1}\,dz.
\end{aligned}
\tag{HC5}
\]

The circles in this formula are positively oriented, and any \(\rho\in(a,b)\) can be used for a coefficient. To see independence of \(\rho\), apply HC1 to the holomorphic function \(f(z)z^{-k-1}\) on an intervening annulus. On the outer circle expand \((z-w)^{-1}\) in nonnegative powers of \(w/z\); on the inner circle expand it in powers of \(z/w\). Both expansions converge uniformly on each smaller closed subannulus and give HC5 with its minus sign. The same geometric bounds prove absolute local uniform convergence of the Laurent series. Integrating this series against \(w^{-k-1}\,dw\) extracts exactly \(c_k\), so the coefficients are unique.

If \(a=0\) and \(|f|\leq C\) near the puncture, then for every \(m\geq1\) its negative coefficient satisfies \(|c_{-m}|\leq C\rho^m\). Radius independence and \(\rho\to0\) make it zero. The remaining power series extends \(f\) holomorphically over the puncture. The coefficient \(c_{-1}\) at a translated puncture is called the residue. Integrating around finitely many disjoint punctures and canceling the other boundary terms by HC1 gives the residue formula for a disk with finitely many isolated singularities.

In particular, suppose \(g\) is holomorphic near a closed disk \(|z-a|\leq R\), not identically zero, and nonzero on its boundary. Let its zeros in the disk be \(b_1,\ldots,b_\ell\), of multiplicities \(m_1,\ldots,m_\ell\). Locally at a zero the preceding factorization gives \(g'/g=m_i/(z-b_i)+u'/u\). For any holomorphic \(\psi\) on a neighborhood of the closed disk, its product with the first summand has residue \(m_i\psi(b_i)\), while the second summand is holomorphic. Consequently

\[
\frac1{2\pi i}\int_{|z-a|=R}
        \psi(z)\frac{g'(z)}{g(z)}\,dz
=\sum_{i=1}^{\ell}m_i\psi(b_i).
\tag{HC6}
\]

This supplies both the integer zero count (\(\psi=1\)) and the power sums (\(\psi(z)=z^j\)) used in preparation. It does not require holomorphic labels for moving zeros. If \(g(p,z)\) depends holomorphically on parameters and has a common zero-free collar on this fixed circle, the left side is holomorphic in \(p\) by the parameter integration argument. The zero count is continuous and integer valued, hence constant on each connected parameter domain. Distinct zeros may merge inside the circle; multiplicities retain the same count.

### The maximum principle

If \(|f|\) has a local maximum at \(a\) in a complex coordinate domain, choose a small closed polydisk there. Its torus lies within that maximum neighborhood. The normally convergent series in HC4 and orthogonality of the circle characters give

\[
\frac1{(2\pi)^n}\int_{[0,2\pi]^n}
 \left|f(a_1+r_1e^{it_1},\ldots,a_n+r_ne^{it_n})\right|^2\,dt
=\sum_{\alpha\in\mathbb N^n}|c_\alpha|^2 r^{2\alpha}
\leq |c_0|^2.
\tag{HC7}
\]

One can first apply this equality to finite Taylor sums and then pass to the limit by uniform convergence. Every summand is nonnegative and the term with \(\alpha=0\) is already \(|c_0|^2\). Thus all nonconstant coefficients vanish. The function is constant near \(a\), and the analytic continuation argument makes it constant on its connected domain. Dimension zero is immediate. In particular, a nonconstant holomorphic function cannot attain an interior maximum of its modulus. This is the scalar maximum principle used on normalized curve disks and on regular manifold pieces.

### Holomorphic inverse coordinates

Let \(F:U\to\mathbb C^n\) be holomorphic, \(a\in U\), and \(A=DF(a)\) invertible over \(\mathbb C\). Choose \(r>0\) with \(\overline{B}(a,r)\subset U\) and, on that ball, \(\|I-A^{-1}DF(z)\|\leq1/2\). This is possible by continuity of the derivative. For
\(V=\{y:\|A^{-1}(y-F(a))\|<r/4\}\) set

\[
\begin{aligned}
T_y(z)&=z-A^{-1}(F(z)-y),\\
\|T_y(z)-T_y(z')\|&\leq\tfrac12\|z-z'\|,
\qquad
\|T_y(z)-a\|<\tfrac34r.
\end{aligned}
\tag{HC8}
\]

The middle inequality is the integral of the real derivative along the segment in the ball. The last follows by comparing \(T_y(z)\) with \(T_y(a)\). Thus it is a contraction into the interior of the same closed ball. Set \(z_0(y)=a\) and \(z_{j+1}(y)=T_y(z_j(y))\). Completeness follows by identifying \(\mathbb C^n\) with \(\mathbb R^{2n}\) and taking coordinatewise limits of Cauchy sequences. The explicit tail bound is

\[
\|z_{j+k}(y)-z_j(y)\|
\leq\frac{2^{-j}}{1-1/2}\,\|z_1(y)-a\|
\leq 2^{-j}\,\frac r2.
\tag{HC9}
\]

The limit \(G(y)\) is in the ball and satisfies \(F(G(y))=y\) by continuity. A fixed point has distance at most \(2\|A^{-1}(y-F(a))\|<r/2\) from \(a\), so lies in the open ball. Each iterate is holomorphic in \(y\) by composition; HC9 gives local uniform convergence, and the earlier limit argument makes \(G\) holomorphic.

The same contraction inequality proves injectivity of \(F\) on the whole closed ball: if \(F(z)=F(z')=y\), then \(z-z'=T_y(z)-T_y(z')\), which forces \(z=z'\). This use of the middle inequality does not require \(y\in V\). Therefore
\(U_0=B(a,r)\cap F^{-1}(V)\) is an open neighborhood of \(a\), and \(F:U_0\to V\) is a biholomorphism with inverse \(G\). Every \(DF(z)\) on the ball is invertible, since \(A^{-1}DF(z)\) differs from the identity by an operator of norm at most \(1/2\); the convergent geometric series supplies its inverse. Differentiating \(F\circ G=\operatorname{id}\) gives
\(DG(y)=DF(G(y))^{-1}\). For \(n=0\) the assertion is immediate. Complex charts transfer the theorem to maps between complex manifolds of equal dimension.

### Implicit equations and submanifold graphs

Suppose \(h(z,w)\) is holomorphic near \((a,b)\in\mathbb C^p\times\mathbb C^q\), with values in \(\mathbb C^q\), \(h(a,b)=0\) and \(D_wh(a,b)\) invertible. The map \(H(z,w)=(z,h(z,w))\) has invertible differential: its block matrix has diagonal blocks \(I_p\) and \(D_wh\). Apply the inverse theorem. Because the first coordinates of \(H\) are unchanged, its inverse on a small product neighborhood of \((a,0)\) has the form \((z,u)\mapsto(z,\eta(z,u))\) with \(\eta\) holomorphic. Shrink a product neighborhood of \((a,b)\) inside the source chart and shrink the \(z\) neighborhood further so \(\eta(z,0)\) lies inside it. In that product all solutions near \((a,b)\) are exactly

\[
\begin{aligned}
h(z,w)=0&\quad\Longleftrightarrow\quad w=\eta(z,0),\\
D_z\eta(z,0)
&=-D_wh(z,\eta(z,0))^{-1}D_zh(z,\eta(z,0)).
\end{aligned}
\tag{HC10}
\]

Uniqueness follows from injectivity of \(H\) in its source chart. The derivative follows from the chain rule for \(h(z,\eta(z,0))=0\); shrink again if needed to retain the invertible block. The zero set is therefore a complex submanifold of dimension \(p\), with the \(z\) coordinates on its graph. Empty parameter blocks are allowed. More generally, \(q\) equations with differential rank \(q\) at a point can be put in this form by choosing a nonzero coordinate minor.

### Constant rank and its precise range

Let \(F:U\subset\mathbb C^n\to\mathbb C^m\) have constant differential rank \(r\) near \(a\). Permute source and target coordinates so an \(r\times r\) minor in the first coordinates is invertible at \(a\). The map
\(\Phi(z)=(F_1(z),\ldots,F_r(z),z_{r+1},\ldots,z_n)\) has invertible differential. After using the inverse theorem and restricting to a product of convex polydisks in coordinates \((u,v)\in\mathbb C^r\times\mathbb C^{n-r}\), write

\[
\begin{aligned}
\widetilde F&=F\circ\Phi^{-1}=(u,Q(u,v)),\\
D\widetilde F&=
\begin{pmatrix}I_r&0\\Q_u&Q_v\end{pmatrix},
\qquad
r=\operatorname{rank}D\widetilde F
=r+\operatorname{rank}Q_v.
\end{aligned}
\tag{HC11}
\]

Row elimination proves the rank equality. Thus \(Q_v=0\) throughout this product. Integrating along segments in the convex \(v\) polydisk shows \(Q(u,v)=q(u)\). In target coordinates apply the biholomorphism
\(\Psi(y',y'')=(y',y''-q(y'))\), whose inverse adds \(q(y')\). On sufficiently small neighborhoods the normal form is

\[
\Psi\circ F\circ\Phi^{-1}(u,v)=(u,0).
\tag{HC12}
\]

The local image is a smooth complex submanifold of dimension \(r\). Each nonempty local fiber in this source product is a \(v\) polydisk, of complex dimension \(n-r\). When \(r=m\) this is the submersion theorem; when \(r=n\) the map is locally a graph embedding and has a holomorphic inverse on its image. For \(r=0\), the zero derivative makes the map constant on a connected source polydisk. The formulas also allow a zero-dimensional source, target or unused block.

These assertions require constant rank on a neighborhood. A map can have rank \(r\) only at the point in question and have larger rank arbitrarily close by. In contrast, near a point where a map attains its maximum rank, a nonzero minor keeps that rank at least the maximum and hence equal to it. This is the precise neighborhood used in the finite-fiber and maximum-rank arguments. A complex linear map of rank \(r\) has real rank \(2r\): choose a complex basis of its image, whose vectors together with their multiples by \(i\) form a real basis. All dimensions in HC10–HC12 and the analytic fiber arguments are complex dimensions.

### Examples and solved problems

**1. An inverse with a parameter.** Find the inverse of \(F(z,w)=(z+w^2,w)\) and its differential, and check why a holomorphic square root through zero is a different situation.

**Solution.** The inverse is \(G(x,y)=(x-y^2,y)\) on all of \(\mathbb C^2\). Its differential is \(\begin{pmatrix}1&-2y\\0&1\end{pmatrix}\), the inverse of \(DF(G(x,y))=\begin{pmatrix}1&2y\\0&1\end{pmatrix}\). For \(h(\lambda,w)=w^2-\lambda\), however, \(D_wh(0,0)=0\). There is no holomorphic \(b(\lambda)\) near zero with \(b(\lambda)^2=\lambda\): its first nonzero Taylor coefficient would give an even order for the square, whereas \(\lambda\) has order one. At every solution with \(w\ne0\), HC10 does give a local branch. The failure at zero preserves the branch point in the finite-map stratification.

**2. Coordinate change for a rank-one map.** Put \(F(z,w)=(z+w^2,(z+w^2)^2)\) in constant-rank form and describe its local fibers. Explain why \(z\mapsto z^2\) does not have a constant-rank form near zero.

**Solution.** Set \(u=z+w^2\) and \(v=w\). The source change has inverse \((u,v)\mapsto(u-v^2,v)\). The target change \((x,y)\mapsto(x,y-x^2)\) then gives \((u,v)\mapsto(u,0)\). The rank is one everywhere; a fiber over \((c,c^2)\) is given by \(z=c-w^2\), a one-dimensional complex graph locally. The differential of \(z^2\) is zero at zero and nonzero off zero, so it is not constant on any neighborhood of zero. Its local fibers are finite; substituting its rank at zero into a constant-rank fiber formula would incorrectly give dimension one.

**3. Zeros with no common root labels.** For \(g(p,z)=z^2-p\) and \(|p|<R^2\), compute the three contour integrals in HC6 with \(\psi=1,z,z^2\) on \(|z|=R\).

**Solution.** All roots lie in the disk and the boundary is zero free. The total multiplicity is two, including the double zero at \(p=0\). The first power sum is zero and the second is \(2p\). Equivalently, on the circle expand \(2z/(z^2-p)=2\sum_{j\geq0}p^jz^{-2j-1}\) and extract residues after multiplying by \(1,z,z^2\). The resulting functions \(2,0,2p\) are holomorphic in \(p\) even though the preceding exercise rules out a holomorphic square-root label through zero.

The human source for the Cauchy and local-power-series antecedents is [Demailly, I.3.1–I.3.3 and I.3.6–I.3.11, pp.20–22](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=20); the local-uniform-limit consequence follows immediately on p.23, and the complex-linear differential characterization is stated in I.3.14 on p.24. The residue and coordinate arguments here are supplied in full rather than being attributed to an unstated proof there. [Demailly II.8.1, p.116](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=116) explicitly uses constant rank. No Montel, distributional, Dolbeault, Sard or general singular inverse theorem is imported by this section.

HC1–HC7 now supply the complex-calculus inputs of preparation and bounded removal. HC8–HC12 supply the inverse, implicit and constant-rank inputs of the local-geometry, singular-locus, finite-rank and proper-image proofs. Their analytic-space, normalization, dimension, counting and other named hypotheses retain their previously stated scopes. The geometric and categorical prerequisites elsewhere in this lesson are separate inputs.

## SH02-FAG-EQUATIONS — A lower dimension bound for simultaneous equations

**Proposition.** Let $Z$ be pure of dimension $m$, and let $g_1,\ldots,g_r$ be holomorphic functions. Every local irreducible component $D$ of their common zero set satisfies

$$
\dim D\geq m-r.
\tag{FAG1}
$$

**Proof.** For one equation, work on each local irreducible component of $Z$. If the function vanishes identically, that component is retained. Otherwise the one-equation contract gives either the empty set or components of dimension $m-1$.

Suppose the assertion has been proved for $r-1$ equations. Near a given point their zero set has finitely many irreducible components, each of dimension at least $m-r+1$. Intersect each with the zero set of $g_r$. An identically zero restriction leaves its component; a nonzero restriction lowers the dimension by exactly one whenever its zero set is nonempty. The common zero set is the finite union of these intersections. Each of its irreducible components is an irreducible component of at least one member of that union, so its dimension is at least $m-r$. This proves the induction. $\square$

Repeated equations and zero functions are included. For example, the two equations $z_1=0$ and $z_1=0$ in $\mathbb C^m$ define a set of codimension one. This also explains why a general inequality asserting codimension at least the number of equations would be false. The bound in FAG1 permits empty intersections and zero-dimensional spaces.

## SH02-FAG-IMAGE — Images and the rank away from a proper analytic subset

**Proposition.** Let $f:Y\to X$ be finite holomorphic. If $C\subset Y$ is a closed irreducible analytic subset, then $f(C)$ is closed irreducible analytic and

$$
\dim f(C)=\dim C.
\tag{FAG2}
$$

**Proof.** The restriction to $C$ is proper. The proper-image contract makes its image analytic, and a proper map between locally compact Hausdorff spaces is closed. If this image were a union of two proper closed analytic subsets, their inverse images would express $C$ as such a union. Thus the image is irreducible. The map $C\to f(C)$ is finite and surjective; the finite-dimension contract proves FAG2. $\square$

**Rank lemma.** A holomorphic map with finite fibres has differential rank $k$ on a dense open subset of the regular part of every pure $k$-dimensional irreducible source component.

**Proof.** On an open subset where the differential has its maximum rank $s$, the constant-rank theorem gives local fibres of dimension $k-s$. A positive value would contradict finite fibres. Hence $s=k$. The locus where that rank drops is a proper analytic subset of the regular part, and its complement is dense. $\square$

For the stratification construction we need a closed analytic exceptional set on the whole component. Embed a neighbourhood of $C$ into $\mathbb C^N$ and take local generators $h_j$ of its analytic ideal. At a regular point of a pure $k$-dimensional component, the matrix $dh$ has rank $N-k$. Choose coordinates for a local embedding of the target. The restriction of $df$ to $TC$ has rank less than $k$ exactly when

$$
\operatorname{rank}
\begin{pmatrix}dh\\df\end{pmatrix}<N.
\tag{FAG3}
$$

The maximal minors give holomorphic equations across the singular locus. Together with $C_{\mathrm{sing}}$, their zero set is a closed analytic exceptional subset of $C$. It is proper by the rank lemma. This construction uses generators of the reduced analytic ideal, so the Jacobian has the asserted rank on the regular locus.

## SH02-FAG-FIBRE — Restricting around an entire finite fibre

**Lemma.** Suppose $f:Y\to X$ is proper and $x\in X$. If an open set $V\subset Y$ contains $f^{-1}(x)$, then there is a neighbourhood $U$ of $x$ such that

$$
f^{-1}(U)\subset V.
\tag{FAG4}
$$

**Proof.** The closed set $Y\setminus V$ has closed image under the proper map. That image does not contain $x$. Its complement is a possible $U$. $\square$

For a finite fibre, choose one source neighbourhood at each of its finitely many points. Each neighbourhood can meet only finitely many strata of a locally finite prescribed stratification. FAG4 then places the full inverse image of a smaller target neighbourhood in their union. All the refinements below can therefore use a finite list of local analytic sets. Empty fibres are allowed: with $V=\varnothing$, the same argument gives an empty inverse image near $x$.

## SH02-FAG-ADAPTED — Constructing compatible Whitney strata

**Theorem.** Let $f:Y\to X$ be finite holomorphic, and fix a locally finite complex analytic source stratification. Near each finite fibre there are compatible Whitney stratifications of source and target refining that source partition, such that every source stratum maps locally biholomorphically onto a target stratum.

**Proof.** Use FAG4 to restrict around the whole fibre. Analytic component decompositions and the prescribed partition are locally finite, so after this restriction the construction involves finitely many local components, closures and boundaries. Shrinking further during the construction is harmless. We will use at most $\dim X+1$ stages, including dimension zero.

Proceed in descending dimension. At the stage indexed by $k$, let $Z\subset X$ be the remaining closed analytic set, with dimension at most $k$, and let $W=f^{-1}(Z)$. FAG2 applied to components shows that $\dim W\leq k$. All strata already chosen have dimension greater than $k$; each is open in the regular part of its analytic closure.

For each $k$-dimensional irreducible component $C$ of $W$, mark the following closed analytic exceptional subsets: its singular locus, intersections with other components, and the rank-drop set FAG3. Also mark every proper intersection of $C$ with a closure or boundary of the prescribed source partition. On the remaining part of $C$, membership in every such closure and boundary is constant. Since each original stratum is its closure minus its boundary, the remaining part of $C$ lies in one original stratum.

Next consider a previously chosen source stratum $S$. Its closure $H$ is pure analytic, and $S$ is open in $H_{\mathrm{reg}}$. If $C$ is not contained in $H$, mark the proper intersection $C\cap H$. If $C\subset H$, mark the Whitney-failure subset from the external contract. It is proper on each irreducible component of $C$. On the complement the pair $(H_{\mathrm{reg}},C_{\mathrm{reg}})$ satisfies the Whitney conditions. Restricting the upper regular part to its open subset $S$ keeps the same tangent spaces, so $(S,C_{\mathrm{reg}})$ satisfies them there too.

On each $k$-dimensional target component of $Z$, mark its singular locus, component intersections and its Whitney-failure subsets relative to the previously chosen target strata. Add every component of $Z$ of dimension below $k$. Finally add the images of all marked source subsets and of all source components of dimension below $k$.

Every set just added to the target is closed analytic. For the source images this follows from properness and FAG2. Their dimensions are below $k$, since each marked subset in a $k$-dimensional irreducible component was proper. Their finite union is therefore a closed analytic set

$$
Z'\subset Z,\qquad \dim Z'<k.
\tag{FAG5}
$$

Take the connected components of $Z\setminus Z'$ as the new target strata. Over each, take the connected components of its inverse image in the retained source components. Every source point is regular, lies in its prescribed original stratum, and has differential rank $k$. A $k$-dimensional component has a $k$-dimensional analytic image by FAG2; after removal of target component intersections, that image lies in one target component. The source and target strata thus have the same dimension, and the inverse function theorem makes the restriction a local biholomorphism.

Each connected source stratum maps onto its connected target stratum. Its image is open because the map is a local biholomorphism. It is also closed: the source component is closed in the full inverse image of the target stratum, and the map on that inverse image is the proper base change of $f$. A nonempty subset both open and closed in a connected target stratum is the whole stratum.

The new strata satisfy the Whitney conditions with every previously fixed higher stratum by the choice of the exceptional sets. Distinct new strata of the same dimension have disjoint closures away from $Z'$ and $f^{-1}(Z')$. Replace $Z$ by $Z'$ and continue. Later stages leave the higher strata fixed. At each later stage, a component is either contained in or disjoint from each earlier analytic closure, because every proper intersection has been removed. This gives the frontier condition as well as the Whitney conditions.

The process ends after dimension zero. Its connected-component subdivisions remain locally finite: analytic irreducible components are locally finite, and the regular connected pieces remain locally connected with finitely many branches after removal of a proper analytic subset. The regular-complement argument is the one in Demailly II.5.3 and its use of Remark II.4.2. There are only finitely many dimension stages. This proves the local theorem. $\square$

In particular, branch points are assigned to lower strata before the restriction is declared locally biholomorphic. The theorem permits several sheets, several source components, and target strata with empty inverse image. It asserts no global injectivity.

## SH02-FAG-COEFFICIENTS — Why one refinement serves all coefficients

Suppose the prescribed source partition makes the cohomology sheaves of a bounded complex $G$ locally constant. All choices in the preceding proof concern the map and that analytic partition. A restriction of a locally constant sheaf to a smaller stratum is locally constant. Therefore the refined partition is still adapted to $G$.

If scalar extension is derived and the stalk complexes are perfect, a locally constant model by perfect complexes remains locally constant after scalar extension. The geometric partition stays fixed. In particular, one refinement works for all residue-field extensions used in the finite-map coefficient argument. This statement requires no perverse t-structure over the original ring.

## SH02-FAG-CONORMAL — Closed affine conormals and their dimensions

**Proposition.** Let $S$ be a connected complex stratum in an $n$-dimensional complex manifold $M$, with analytic closure and boundary. Then $\overline{T^*_S M}$ is a closed complex analytic conic subset of $T^*M$, pure of dimension $n$.

**Proof.** Work locally on a pure $d$-dimensional component $Z$ of the closure. The stratum is dense and open in the relevant regular part. Choose generators $h_j$ for the reduced analytic ideal of $Z$. In $T^*M$ over $Z$, impose the vanishing of the $(n-d+1)$-minors of the matrix obtained by adjoining the covector row $\xi$ to the rows $dh_j$. This gives a closed analytic set $Q$.

On $Z_{\mathrm{reg}}$, the rows $dh_j$ span the annihilator of $TZ$ and have rank $n-d$. The minor condition says exactly that $\xi$ belongs to their span. Hence

$$
Q|_{Z_{\mathrm{reg}}}=T^*_{Z_{\mathrm{reg}}}M.
\tag{FAG6}
$$

The analytic-difference contract makes the closure of $Q$ minus its part over $Z_{\mathrm{sing}}$ analytic. This is the desired conormal closure, because restriction of the conormal bundle to a dense open subset of the regular component does not change its closure. That bundle has base dimension $d$ and fibre dimension $n-d$, so its components and their analytic closures have dimension $n$. Scaling covectors preserves the defining condition, which proves conicity. $\square$

This is an affine version of the conormal construction in Teissier II.4.1, pp.379–380. If $d=n$, the conormal is the zero section and the assertion concerns its closure. If $d=0$, it is the full cotangent fibre. These cases do not require a nonempty projectivized conormal.

A locally finite union of such closed conormals is analytic: locally only finitely many source strata can occur, so the union is a finite union of analytic sets near every cotangent point.

## SH02-FAG-BOUNDARY — Annihilation at a boundary stratum

For a Whitney stratification, every covector in a closed conormal based at a boundary stratum $T$ annihilates $TT$.

**Proof.** Choose covectors $\xi_i\in T^*_{S}M$ converging to a covector $\xi$ based at $y\in T$. Pass to a subsequence for which the tangent spaces $T_{y_i}S$ converge in the Grassmannian to a plane $L$. The covectors $\xi_i$ annihilate those tangent spaces, so their limit annihilates $L$. Whitney condition (a) gives $T_yT\subset L$. Thus $\xi$ annihilates $T_yT$. The case where the limiting point remains in $S$ follows directly from the same argument. $\square$

## SH02-FAG-EXAMPLES — Two small maps to test the statement

For $f:\mathbb C\to\mathbb C$, $f(z)=z^r$ with $r\geq1$, use the strata $\{0\}$ and $\mathbb C^*$ on both sides. The nonzero restriction has $r$ sheets and is locally biholomorphic; the point stratum maps isomorphically to a point. The lower stratum accommodates ramification when $r>1$.

For the closed embedding $\mathbb C\hookrightarrow\mathbb C^2$, $z\mapsto(z,0)$, take the image line and its complement as target strata. The line is the image of the sole source stratum, and the complement has empty inverse image. A finite map may therefore have positive-codimension image without violating the equal-dimension assertion for corresponding nonempty strata.

These examples check the role of strata, rather than replacing any hypothesis in the theorem.



<a id="SH02-FAG-PRESERVED-FOUNDATIONS"></a>

## Analytic foundations and their precise proof floors

The opening section lists the contracts used by FAG1–FAG6. The following foundation sections prove the indicated contracts at their more elementary inputs, retaining each theorem's hypotheses and named floors. They supply the fibre-jump, conormal, component, rank, extension, normalization and marked-family steps at the explicit lower inputs stated in each section. Local preparation, coherent-module operations and local analytic geometry use the full programme proofs linked below. The linked preparation, coherence, analytic dimension and normalization proofs supply these inputs with their stated hypotheses.

The optional polar-multiplicity route PNY9–PNY11 keeps its additional section and multiplicity inputs. The direct DPC–CSB–HN route supplies its own branch estimates and section comparisons, and therefore needs neither that general-section multiplicity formula nor the all-index test PNY9. It retains the actual critical-curve family, finite marked normalization and common normal/finite analytic inputs explicitly recorded in those sections. RLS's specialization counterexample is not an assumption that saturated algebras commute with specialization.

The arguments and the new connecting exposition are independently authored standard mathematics, dedicated to [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The linked human sources retain their own rights; their prose and images are not reproduced.

<a id="SH02-FAG-FIBRE-JUMP"></a>
<a id="sh02-fag-fibre-jump--analytic-fibre-jumps-and-the-whitney-bad-locus"></a>

## Analytic fibre jumps and the Whitney bad locus

Source analyticity of fibre jumps can be proved without first choosing a Whitney stratification. The proof below gives the exact closed analytic Whitney-failure locus from the conormal criterion established in the later sections.

### Fibre dimension is upper semicontinuous

For a holomorphic map \(F:T\to Z\) of reduced complex spaces, put

\[
q_F(x)=\dim_x F^{-1}(F(x)),\qquad
J_s(F)=\{x\in T:q_F(x)\geq s\},\quad s\in\mathbb Z_{\geq0}.
\tag{FJ1}
\]

The dimension is that of the reduced local fibre. No properness hypothesis is imposed here.

**Lemma.** The function \(q_F\) is upper semicontinuous.

**Proof.** Work near \(x=0\), embedding the source in an open subset of \(\mathbb C^n\) and the target in \(\mathbb C^p\), with \(F(0)=0\). Write \(A=F^{-1}(0)\) and \(s=\dim_0 A\). Successively choose linear forms avoiding every positive-dimensional irreducible component of the preceding intersection. The one-equation theorem decreases each such component's dimension by one; zero-dimensional components remain. After \(s\) forms the intersection germ is just \(\{0\}\). The forms can be chosen linearly independent, since the excluded conditions are finitely many proper linear subspaces. Complete them to coordinates \((u,v)\in\mathbb C^s\times\mathbb C^{n-s}\).

Choose a sufficiently small closed ball \(\overline B''\) in the second factor so that \(A\cap(\{0\}\times\overline B'')=\{0\}\). On the compact vertical boundary \(T\cap(\{0\}\times\partial B'')\), the target-coordinate vector \(F\) is nonzero. Compactness and continuity give a small ball \(B'\) and a target neighbourhood \(W\) such that

\[
F^{-1}(y)\cap(\overline B'\times\partial B'')=\varnothing
\quad(y\in W).
\tag{FJ2}
\]

An empty boundary set causes no difficulty: the same exclusion holds after shrinking. Representatives are chosen with the closed product inside the original coordinate domain.

For each \(y\in W\), projection of \(F^{-1}(y)\cap(B'\times B'')\) to \(B'\) is proper, because FJ2 excludes escape through the vertical boundary. Each projection fibre is a compact analytic subset of a coordinate ball. Coordinate functions separate points, so the compact-analytic-set theorem makes it finite. The finite-map dimension bound therefore gives fibre dimension at most \(s\). Restrict the source neighbourhood further so that \(F(x')\in W\) for its points \(x'\). Then \(q_F(x')\leq s\) there, as required. If \(n=s\), the vertical factor is a point and the bound is immediate; if \(s=0\), the same argument is a finite projection to a point. \(\square\)

This is the finite-projection argument for Demailly II.8.2, pp.116–117, written here using the precise one-equation, compact-analytic and finite-dimension inputs above. It uses neither a pre-existing equidimensional-fibre stratification nor a generic Whitney theorem.

### The jump locus is analytic in the source

**Theorem.** For every integer \(s\geq0\), the set \(J_s(F)\) is closed analytic in \(T\).

**Proof.** Analyticity is local. A reduced source has finitely many irreducible component germs near each point, and the fibre dimension of their union is the maximum of their fibre dimensions. Thus it suffices to work on a pure irreducible representative \(T\) of dimension \(m\), and to induct on \(m\). The empty source and dimension zero are immediate.

Let \(\rho\) be the maximum differential rank of \(F\) on \(T_{\mathrm{reg}}\) and set \(k=m-\rho\). If \(\rho=0\), the map is locally constant on the regular locus. An irreducible representative has connected dense regular locus after shrinking, so \(F\) is constant on it and hence on \(T\). All fibres have local dimension \(m\), proving the claim in this case.

Suppose \(\rho>0\). Embed \(T\subset\mathbb C^n\), choose generators \(h_1,\ldots,h_\ell\) of its reduced ideal, and extend the embedded target-coordinate functions of \(F\) holomorphically to functions \(g\) in the ambient source. At regular points, \(Dh\) has rank \(n-m\). Consequently

\[
\operatorname{rank}\begin{pmatrix}Dh\\Dg\end{pmatrix}
=n-m+\operatorname{rank}(dF|_{T_{\mathrm{reg}}}).
\tag{FJ3}
\]

Let \(C\) be the union of \(T_{\mathrm{sing}}\) with the common zero set of the minors of size \(n-m+\rho\) in this stacked matrix. It is a closed analytic proper subset of \(T\). On \(T\setminus C\) the rank is constantly \(\rho\), so the holomorphic constant-rank theorem gives \(q_F=k\). Upper semicontinuity and density imply \(q_F\geq k\) on all of \(T\): a smaller value would hold on a neighbourhood meeting \(T\setminus C\). Therefore \(J_s(F)=T\) when \(s\leq k\).

For \(s>k\), consider an irreducible fibre germ of dimension at least \(s\). It cannot meet \(T\setminus C\), where every fibre germ has dimension \(k<s\). More precisely, if this irreducible germ were not contained in \(C\), its complement of \(C\) would contain a point at which the same component has its original dimension, contradicting the constant-rank description. Hence every such component is contained in \(C\). Conversely, every fibre component of the restricted map on \(C\) is contained in a fibre of \(F\). These two observations give the exact equality

\[
J_s(F)=J_s(F|_C)\subset C\qquad(s>k).
\tag{FJ4}
\]

Give \(C\) its reduced structure. It has smaller dimension, so induction proves that the right side is closed analytic in \(C\), hence in \(T\). The locally finite component reduction proves the assertion for the original source. \(\square\)

The analytic rank-drop set is an intermediate exceptional set, rather than the jump locus itself. For \(F(z)=z^2\), every fibre is zero-dimensional, so \(J_1(F)=\varnothing\), even though the Jacobian vanishes at the origin. For the nonproper map \(F(u,v)=(u,uv)\), the fibre over \((0,0)\) is the line \(u=0\), and all other nonempty fibres are points. Thus \(J_1(F)=\{u=0\}\). Neither example requires properness for source analyticity.

### Proper images and the dimension estimate

**Proposition.** If \(\tau:D\to Y\) is proper holomorphic and \(\dim D\leq a\), then

\[
\tau(J_s(\tau))\ \text{is closed analytic},\qquad
\dim\tau(J_s(\tau))\leq a-s
\tag{FJ5}
\]

whenever this image is nonempty.

**Proof.** The theorem makes \(J_s(\tau)\) closed analytic. Its restriction map is proper, so the proper-image theorem gives the first assertion.

At each point of \(J_s(\tau)\), choose a fibre component germ of dimension at least \(s\). At every point of a sufficiently small representative of that component, the fibre dimension is still at least \(s\). Thus that whole germ lies in \(J_s(\tau)\). The restricted map on the jump locus therefore has fibre dimension at least \(s\) at every point.

On an irreducible component \(A\) of the jump locus, of dimension \(b\), work at a generic regular point away from its intersections with the other components. Its restricted fibre dimension is at least \(s\), so its maximum differential rank is at most \(b-s\). The exact holomorphic rank/image-dimension theorem for the surjection \(A\to\tau(A)\) gives \(\dim\tau(A)\leq b-s\leq a-s\). Components are closed and their restrictions remain proper. Near a target point only finitely many source components meet a small relatively compact inverse image, by properness and local finiteness. Their images yield the stated bound. If \(s>a\), the jump locus is empty. \(\square\)

Here the rank/image-dimension input is Demailly II.8.3–8.6, pp.117–118. Its proofs use normalization, rank under restriction, and the Baire argument; these are explicit analytic prerequisites, rather than consequences of properness alone. The new induction above proves source analyticity of fibre jumps; it does not silently prove all of those lower foundations.

### The exact conormal test

Let \(H\) be reduced and pure of dimension \(d\), and let \(Y\subset H\) be closed analytic, without a purity assumption on \(Y\). Work locally and write its irreducible components as \(Y_i\), of dimensions \(t_i\). Choose an embedding \(H\subset\mathbb C^N\) with \(N\geq d+2\), adding unused coordinates if necessary. The projectivized conormal is

\[
C(H)=\overline{\{(x,[\xi]):x\in H_{\mathrm{reg}},
\ 0\ne\xi,\ \xi|_{T_xH}=0\}}
\subset H\times\mathbb P^{N-1},
\qquad \nu:C(H)\to H.
\tag{FJ6}
\]

The same minors and analytic-difference construction as FAG6 prove analyticity. The regular conormal bundle has dimension \(d+(N-d-1)=N-1\); its closure is pure of that dimension. Projection \(\nu\) is proper.

Choose local generators \(a_1,\ldots,a_\ell\) for the ideal of \(Y_i\). Define \(e_i:B_i\to C(H)\) as the closure of the graph

\[
c\longmapsto
[a_1(\nu(c)):\cdots:a_\ell(\nu(c))]
\quad\text{on }C(H)\setminus\nu^{-1}(Y_i),
\qquad \pi_i=\nu e_i.
\tag{FJ7}
\]

This is the blow-up in the pulled-back ideal, with its reduced structure. Locally the graph is the complement of the centre in the incidence equations \(a_jv_k=a_kv_j\) in \(C(H)\times\mathbb P^{\ell-1}\). Taking its actual analytic closure discards incidence components supported entirely over the centre. In particular, a conormal component wholly in the centre contributes nothing. The analytic-difference theorem proves that this graph closure is analytic. The projective factors make \(e_i\) and \(\pi_i\) proper, and each retained component of \(B_i\) has dimension \(N-1\).

Let \(D_i=(\pi_i^{-1}(Y_i))_{\mathrm{red}}\) and \(\tau_i=\pi_i|_{D_i}:D_i\to Y_i\). In the projective chart \(v_j=1\), the pulled-back ideal is generated by \(a_j\), since \(a_k=a_jv_k\). That generator is not identically zero on any retained component meeting the chart: the defining graph is dense on each such component. The one-equation theorem therefore makes \(D_i\) pure of dimension \(N-2\) when nonempty. The map \(\tau_i\) is proper. Empty blow-ups and empty exceptional fibres are retained as empty.

The deeper input required for the Whitney deduction is precisely the following equivalence, at a regular point \(y\in(Y_i)_{\mathrm{reg}}\):

\[
(H_{\mathrm{reg}},(Y_i)_{\mathrm{reg}})
\text{ satisfies Whitney }(a,b)\text{ at }y
\quad\Longleftrightarrow\quad
D_{i,y}=\varnothing
\quad\text{or}\quad
\dim D_{i,y}=r_i,
\qquad r_i=N-2-t_i.
\tag{FJ8}
\]

This is Teissier V.1.2(ii),(iv), pp.455–470, using the conormal diagram on p.455. Its sufficiency invokes III.2.3.1, pp.398–400; its necessity is the polar argument of V.1.2.1 and the proof completing V.1.2. The contact and direct hyperplane proofs below supply both directions using the local analytic inputs they identify. The selected direct route constructs its critical-curve family and branch estimate explicitly. We do not identify it with a weaker assertion that good points merely form a dense open set, or replace its conormal and ambient-dimension threshold by an unstated Nash criterion.

For the chosen embedding, the direct hyperplane induction below proves necessity. The contact calculation supplies nonempty-fibre sufficiency at its declared normal-space floor. For an empty fibre, properness makes the image of every retained graph component closed and absent near the point. All upper components remaining there lie wholly in the smooth lower component; by purity and equal dimension the upper space locally equals that component. The Whitney conditions then hold directly. This explains the single-embedding formulation and its empty case.

At a smooth base point, each nonempty fibre of \(D_i\to Y_i\) is cut out locally by \(t_i\) base-coordinate equations in a pure \((N-2)\)-dimensional space. FAG1 gives dimension at least \(r_i\). Thus FJ8 is equivalently the upper bound \(\dim D_{i,y}\leq r_i\), with dimension of the empty set interpreted as \(-\infty\).

### Deduction of the closed analytic bad locus

Include \(Y_{\mathrm{sing}}\) in the failure set, since a Whitney lower stratum must be smooth. Relative to FJ8, the exact failure set is

\[
B(H,Y)=Y_{\mathrm{sing}}\ \cup\
\bigcup_i\tau_i\bigl(J_{r_i+1}(\tau_i)\bigr).
\tag{FJ9}
\]

**Proof.** At a regular point of \(Y\), there is only one local component \(Y_i\). A fibre has dimension greater than \(r_i\) exactly when it has a point whose local fibre dimension is at least \(r_i+1\). FJ8 and the preceding lower bound then give FJ9, including empty fibres.

By FJ5 every displayed proper image is closed analytic, and

\[
\dim\tau_i\bigl(J_{r_i+1}(\tau_i)\bigr)
\leq (N-2)-(r_i+1)=t_i-1.
\tag{FJ10}
\]

No such image contains a component of \(Y_i\). Its intersection with any other irreducible component of \(Y\) is proper as well, since distinct maximal irreducible components cannot contain one another. The singular locus is likewise proper on every component. The local finite union is therefore closed analytic and nowhere dense in \(Y\). Locally chosen embeddings and generators give the intrinsic failure set by the exact equality FJ9, so these descriptions agree on overlaps. Zero-dimensional lower components have empty jump images by FJ10. \(\square\)

This supplies the fibre-jump and proper-image steps in Teissier VI.2.1, p.477, and gives the full deduction from its exact conormal input. It proves no existence theorem for a microlocal \(\mu\)-stratification.

### Two checks on the blow-up conventions

For a smooth linear \(H=\mathbb C^d\subset\mathbb C^{d+2}\) and a proper linear subspace \(Y=\mathbb C^t\) with \(t<d\), the conormal is \(H\times\mathbb P^1\). The exceptional fibre is \(\mathbb P^{d-t-1}\times\mathbb P^1\), of dimension \(d-t=r\), as FJ8 requires. If instead \(Y=H\), the graph domain in FJ7 is empty and so is the blow-up; no fictitious negative-dimensional projective factor is introduced.

For a component-sensitive example, use coordinates \((x,y,z,w)\) in \(\mathbb C^4\) and set \(H=\{xy=0,w=0\}\), \(Y=\{x=0,w=0\}\). Here \(d=t=2\) and \(r=0\). The conormal component over the plane \(x=w=0\) is wholly in the centre, so its graph closure is empty. On the other plane \(y=w=0\), the pulled-back centre ideal is the principal ideal \((x)\); its blow-up is the identity. Its exceptional set is

\[
D=\{x=y=w=0\}\times\mathbb P(\operatorname{span}(dy,dw)).
\tag{FJ11}
\]

The fibre is a projective line at points of the intersection line and empty elsewhere in \(Y\). Thus FJ9 gives exactly \(\{x=y=w=0\}\). Directly, approaching that line along the plane \(y=w=0\) gives tangent plane \(\operatorname{span}(\partial_x,\partial_z)\), whereas \(TY=\operatorname{span}(\partial_y,\partial_z)\) is not contained in it. Whitney (a) fails there. Both the empty-fibre and the discarded-component conventions therefore have a concrete geometric test.

The proofs and examples in this section are independently written standard mathematics. Their original exposition is additionally dedicated under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); cited source text and diagrams are not adapted or included, and retain their own rights.

<a id="SH02-FAG-CONORMAL-SUFFICIENCY"></a>
<a id="sh02-fag-conormal-sufficiency--conormal-dimension-and-the-whitney-estimates"></a>

## Conormal dimension and the Whitney estimates

We now prove the sufficiency direction of FJ8, including quantitative estimates, using the contact identity on the normalized conormal blow-up. The [direct hyperplane proof](#SH02-FAG-HYPERPLANE-NECESSITY) supplies necessity using the first conormal-fibre bound at its stated polar floor. This proof uses finite normalization, extension across analytic subsets of codimension at least two in a normal space, and the analytic Nullstellensatz. It does not import idealistic Bertini, a polar equimultiplicity theorem, a resolution of singularities, a Whitney stratification or a curve-selection theorem.

**Theorem.** Let \(H\subset\mathbb C^N\) be reduced and pure of dimension \(d\), with \(N\geq d+2\). Let \(Y\subset H\) be closed analytic and smooth of dimension \(t\) near \(y_0\). Let \(C(H)\), \(B\), \(\pi:B\to H\) and \(D=(\pi^{-1}Y)_{\mathrm{red}}\) be the actual conormal and graph blow-up of FJ6–FJ7. If \(D_{y_0}\) is empty or has dimension \(N-2-t\), the pair \((H_{\mathrm{reg}},Y)\) satisfies Whitney \((a,b)\) near \(y_0\).

Choose local holomorphic coordinates \((y,z)\in\mathbb C^t\times\mathbb C^{N-t}\) flattening \(Y=\{z=0\}\), and use the Euclidean norm in these coordinates. The cotangent lift identifies the original and flattened conormal spaces and their pulled-back centre ideals; it therefore identifies their graph blow-ups and preserves exceptional-fibre dimensions. After shrinking there are \(C>0\) and an integer \(L\geq1\) such that

\[
\begin{aligned}
\operatorname{dist}(T_yY,T_xH)&\leq C\|z(x)\|,\\
\operatorname{dist}\left(
\frac{x-(y(x),0)}{\|z(x)\|},T_xH
\right)&\leq C\|z(x)\|^{1/L},
\qquad x\in H_{\mathrm{reg}}\setminus Y.
\end{aligned}
\tag{CWS1}
\]

Here \(\operatorname{dist}(A,T)\) for a subspace \(A\) is the supremum of distances to \(T\) of its unit vectors. The second line uses the displayed unit secant vector. The estimates are asserted in the chosen flattened coordinates; the ordinary Whitney conditions are independent of that choice.

### Eliminate exceptional components over a smaller base

The empty-fibre argument is the one following FJ8: properness excludes every retained graph component near \(y_0\), and the remaining upper space locally equals the smooth lower component. Hence assume the fibre is nonempty and has the stated dimension. Work with a connected small representative of \(Y\).

Every component \(A\) of \(D\) has dimension \(N-2\). Its restriction to \(Y\) is proper. If its analytic image has dimension \(p<t\), the holomorphic rank/image theorem and upper semicontinuity show that its local fibre dimension is at least \(N-2-p\) at every source point: it equals this value on the dense maximum-rank locus and cannot decrease at its boundary. If the image contained \(y_0\), this would contradict the assumed dimension \(N-2-t\) of the whole fibre.

The union of all such components is closed, by local finiteness. Its proper image is closed and misses \(y_0\). Shrink the base to its complement, and then shrink the ambient neighbourhood accordingly. Every remaining component of \(D\) now dominates \(Y\). This step uses the exact rank and fibre arguments already given above, rather than inferring dominance from properness.

Let \(\eta:\widetilde B\to B\) be a finite normalization, and put \(\widetilde\pi=\pi\eta\). Its pulled-back centre ideal is still invertible; locally it is generated by one of the normal coordinates \(z_j\). This generator is nonzero on each retained component, so its reduced zero set \(E\) is pure of codimension one. Every irreducible component of \(E\) maps finitely onto a component of \(D\): the image is irreducible analytic, has the same dimension, and a proper analytic subset of a component has smaller dimension. Consequently each component of \(E\) dominates \(Y\).

The maps actually used are

\[
\widetilde B\xrightarrow[\text{finite normalization}]{\eta}
B\xrightarrow[\text{graph blow-up}]{e}C(H)
\xrightarrow[\text{projective conormal}]{\nu}H,
\qquad
E\xrightarrow{\widetilde\pi|_E}Y,
\qquad \widetilde\pi=\nu e\eta.
\tag{CWS2}
\]

All these projection maps are proper.

### Differentiate the contact identity at a generic divisor point

Write a projective covector as \([\xi]=[b_1:\cdots:b_t:a_1:\cdots:a_{N-t}]\), using a chart in which one coefficient is normalized to \(1\). The conormal identity pulls back to

\[
\alpha=\sum_{i=1}^{t}b_i\,dy_i+
\sum_{j=1}^{N-t}a_j\,dz_j=0
\quad\text{on }\widetilde B_{\mathrm{reg}}.
\tag{CWS3}
\]

Indeed, on the dense graph over \(H_{\mathrm{reg}}\setminus Y\), the differential of the projection takes tangent vectors into \(TH\), which \(\xi\) annihilates. The coefficients and projection are holomorphic, so the identity extends to the regular locus of each normalized retained component. Multiplying the covector representative by an invertible function leaves the identity unchanged.

There is a closed analytic subset \(S\subset\widetilde B\) of codimension at least two outside which every point of \(E\) has all of the following properties: the ambient space is regular; the reduced divisor is regular and has a single local component; and its map to \(Y\) has rank \(t\). To construct \(S\), take the ambient singular locus, the divisor singular/intersection loci, and the closed analytic rank-drop subsets of its components, using the stacked-minor construction FJ3. Normality gives codimension at least two for the ambient singular locus. The other exceptional sets are proper in each divisor component: regular density handles its singular loci, and dominance gives generic rank \(t\). Thus they also have ambient codimension at least two.

At a point of \(E\setminus S\), complete the actual base coordinates \(y_1,\ldots,y_t\) and a defining coordinate \(u\) for the divisor to a coordinate system on \(\widetilde B\). Independence holds because the restricted base map is submersive. The centre ideal has positive multiplicity \(m\) along this divisor. Therefore, locally,

\[
z_j=u^m Z_j\quad(1\leq j\leq N-t),
\qquad m\geq1,
\qquad \text{at least one }Z_j\text{ is a unit}.
\tag{CWS4}
\]

A unit in a generator of the ideal is included in the functions \(Z_j\); no global choice of \(u\) or \(m\) is made.

Compare the coefficients of \(dy_i\) and \(du\) in CWS3. They give respectively

\[
\begin{aligned}
b_i&=-u^m\sum_j a_j\,\partial_{y_i}Z_j,\\
m\sum_j a_j Z_j&=-u\sum_j a_j\,\partial_u Z_j.
\end{aligned}
\tag{CWS5}
\]

Thus the tangential covector coefficient \(b_i\) is divisible by \(u^m\), and \(\sum_j a_jz_j\) is divisible by \(u^{m+1}\). The additional factor of \(u\) in the second assertion is the secant estimate's essential cancellation. We differentiated the actual projected coordinates, not an assumed product structure on the whole exceptional divisor.

### Extend the quotients and make the bounds uniform

On any blow-up chart let \(e_0=z_{j_0}\) be the local generator of the centre ideal. On the complement of \(E\), form the holomorphic quotients

\[
h_i=\frac{b_i}{e_0},
\qquad
g=\frac{\sum_j a_j z_j}{e_0}.
\tag{CWS6}
\]

CWS4–CWS5 extend them holomorphically near every point of \(E\setminus S\), and \(g\) vanishes there on \(E\). They are therefore holomorphic off \(S\). The extension theorem for a normal space across a codimension-at-least-two analytic subset extends them uniquely over \(S\). The extension of \(g\) vanishes on all of \(E\), since the regular open part of each divisor component is dense. This justifies passage from generic divisor points to the entire exceptional fibre, including singular and intersecting divisors.

The analytic Nullstellensatz now gives, in a neighbourhood of each point of \(E\), an integer \(\ell\geq1\) and a holomorphic function \(q\) with

\[
g^\ell=e_0q.
\tag{CWS7}
\]

This follows from \(g\) vanishing on the zero set of the principal ideal \((e_0)\); it is not a division assertion on an unnormalized singular space. In a singular chart, lift both functions to an ambient polydisk. The ambient analytic Nullstellensatz puts a power of the lifted numerator in the ideal generated by the lifted centre equation and the space's defining ideal. Restricting to the space gives CWS7. The exact theorem is Demailly II.4.22, p.97; the quotient step is included here.

The fibre \(\widetilde\pi^{-1}(y_0)\) is compact. Cover it by finitely many relatively compact blow-up and covector charts of this kind, small enough that the quotients and the functions \(q\) are bounded on their closures. Take \(L\) to be the largest of their finitely many exponents. Properness supplies a source neighbourhood of \(y_0\) whose entire lifted inverse image lies in this union. Shrink further so that \(\|z\|\leq1\).

In each covector chart \(\|\xi\|\geq1\), and in each blow-up chart \(|e_0|\leq\|z\|\). CWS6–CWS7 therefore give uniform bounds, for every nonzero conormal covector over a regular upper point,

\[
\frac{\|b\|}{\|\xi\|}\leq C\|z\|,
\qquad
\frac{|\sum_j a_jz_j|}{\|\xi\|\|z\|}
\leq |g|\leq C\|z\|^{1/L}.
\tag{CWS8}
\]

Using a larger \(L\) weakens a bound when \(\|z\|\leq1\), so the finite charts indeed give one exponent and one constant. Every conormal point over \(H_{\mathrm{reg}}\setminus Y\) lies in the smooth conormal-bundle graph there, where normalization is an isomorphism. It therefore lifts uniquely; no covector over the regular upper space is excluded by the cover.

For a complex linear subspace \(T\), the distance of a vector \(v\) to \(T\) is the supremum of \(|\xi(v)|\) over unit complex covectors annihilating \(T\). This follows by orthogonal projection and the dual norm on \(T^\perp\). Apply it first to unit vectors in the flat tangent space of \(Y\), then to the projected secant \((0,z)/\|z\|\). CWS8 proves CWS1.

### Recover Whitney conditions for every lower-point sequence

The projected secant estimate suffices together with the tangential estimate. For an arbitrary lower point \(y'=(y',0)\), put \(v=(y(x)-y',z(x))\). Then \(\|v\|\geq\|z(x)\|\) and

\[
\begin{aligned}
\frac{|\xi(v)|}{\|\xi\|\|v\|}
&\leq
\frac{|\sum_j a_jz_j|}{\|\xi\|\|z\|}
+\frac{\|b\|}{\|\xi\|}
\frac{\|y(x)-y'\|}{\|v\|}\\
&\leq C\bigl(\|z\|^{1/L}+\|z\|\bigr)
\leq 2C\|z\|^{1/L}.
\end{aligned}
\tag{CWS9}
\]

For sequences of upper regular points and lower points tending to any nearby point of \(Y\), these bounds tend to zero. Compactness of the Grassmannian gives convergent tangent subsequences. The first bound forces their limits to contain \(TY\); the last bound forces every limiting secant to lie in the limiting tangent plane. These are exactly Whitney \((a)\) and \((b)\). Upper regular points lying in \(Y\) themselves have \(TY\subset TH\) and cause no exception.

Finally, the ordinary conditions transfer back through the flattening coordinate map. Tangent planes transform by its continuously varying invertible differential. For two converging points, the difference of their images is the differential at the limit applied to their secant, with an error that is small relative to the secant length; integrate the difference of differentials on the segment in a small convex coordinate domain. The inverse differential supplies a local lower norm bound. Thus tangent and secant inclusions are preserved. This asserts invariance of the ordinary Whitney conditions, rather than transporting the numerical exponent unchanged to every unflattened embedding. \(\square\)

### A cusp checks the positive exponent

Let \(H\) be the cusp \(x_2^2=x_1^3,\ x_3=0\) in \(\mathbb C^3\), and let \(Y=\{0\}\). Its normalization parameter is \(s\), with \(x(s)=(s^2,s^3,0)\). On the conormal chart with second coefficient \(1\), choose the conormal covector \(\xi_s=(-3s/2,1,0)\); it annihilates \(x'(s)=(2s,3s^2,0)\). In the blow-up chart generated by \(e_0=x_1=s^2\),

\[
\sum_j a_jx_j=-\frac{s^3}{2},
\qquad
g=-\frac{s}{2},
\qquad g^2=\frac{e_0}{4}.
\tag{CWS10}
\]

The normalized divisor coordinate is \(u=s\), its centre multiplicity is \(m=2\), and CWS7 permits \(L=2\). The exact projected-secant distance to the tangent line is

\[
\operatorname{dist}\left(\frac{x(s)}{\|x(s)\|},T_{x(s)}H\right)
=
\frac{|s|}{2\sqrt{1+|s|^2}\sqrt{1+9|s|^2/4}}.
\tag{CWS11}
\]

The planar conormal is the maximizing covector; the third-coordinate covector pairs to zero with the secant. This distance is comparable to \(\|x(s)\|^{1/2}\) and is not bounded by a constant times \(\|x(s)\|\) near zero. The example checks why vanishing on the reduced divisor yields a positive exponent, while the principal centre ideal can have higher multiplicity. It also distinguishes the tangential exponent-one assertion from the secant assertion.


The normalization and extension facts have exact openly permitted proofs in [Demailly II.7.2–7.8, pp.110–113, and II.7.9–7.12, pp.114–115](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=110). In particular, II.7.8 supplies the codimension-two extension, not an unproved continuity argument at singular divisor points. The [normal analytic reconstruction](#SH02-FAG-NORMAL-ANALYTIC-FOUNDATIONS) supplies the universal denominator, normality, finite normalization and the codimension-two extension step at its stated inputs. The [holomorphic extension proof](#SH02-FAG-HOLOMORPHIC-EXTENSION-FOUNDATIONS) supplies manifold Hartogs and singular-space boundedness at its precise finite-projection and analytic-dimension floor; the coherent analytic Nullstellensatz used in CWS7 retains its named scope. Normalization is finite, not a resolution or a smoothness assumption on the whole space.

The precise geometric antecedent is [Teissier III.2.3.1, pp.398–400](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=86). The calculation above independently proves its nonempty-fibre sufficiency conclusion relative to the stated normal-space floor and retains the earlier empty case. The idealistic-Bertini and valuation route in that source is not a dependency of this proof. The direct hyperplane induction below supplies necessity at the same normal-space and dimension hypotheses. This section's independently written exposition is additionally dedicated under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); cited source prose and diagrams retain their own rights and are not included.

<a id="SH02-FAG-POLAR-NECESSITY"></a>

<a id="SH02-FAG-POLAR-SECTIONS"></a>

## Polar curves and the necessity argument

[Polar sections, integral equations and generic Lipschitz algebras](../polar-sections-and-lipschitz-algebras.html#PS0) proves the all-index section-density, actual proper polar image and empty-polar fibre threshold of PNY9. It retains the full compact projective fibre and every original index. General-section multiplicities and polar equimultiplicity are separate arguments.

The necessity direction has two different fibre questions. Write the actual conormal and blow-up maps as

\[
\kappa:C(H)\longrightarrow H,\qquad
\theta:B=\operatorname{Bl}_{\kappa^{-1}Y}C(H)\longrightarrow C(H),\qquad
\psi=\kappa\theta,\qquad D=(\psi^{-1}Y)_{\mathrm{red}}.
\tag{PNY1}
\]

The [Whitney criterion](#SH02-FAG-FIBRE-JUMP) concerns the exceptional fibre $D_{y_0}$. A bound on $\kappa^{-1}(y_0)$ alone does not give a bound on $D_{y_0}$: the blow-up also records normal directions of approach to $Y$. This section supplies the critical-secant obstruction, reconstructs the generic polar-projection argument relative to its exact family inputs, and deduces the first conormal-fibre bound. The later direct hyperplane induction supplies the exceptional-fibre argument without importing the separate upper polar-equimultiplicity theorem.

### A critical-secant obstruction

Let $M\subset\mathbb C^N$ be a smooth complex manifold of dimension $d$, and let $Y$ be a smooth curve through $0$ in its closure. The proof uses smooth retractions and limits of tangent planes. Let $p:\mathbb C^N\to\mathbb C^2$ be linear and surjective, with $p|_{T_0Y}$ injective. Choose a smooth local retraction $\rho$ to $Y$ for which

\[
\rho|_Y=\operatorname{id}_Y,\qquad
\ker p\subset\ker D\rho_0,\qquad
\mathbb C^N=T_0Y\oplus\ker D\rho_0.
\tag{PNY2}
\]

Such a retraction exists. The curve $p(Y)$ is smooth near $0$ and $p|_Y$ is a local embedding. Compose $p$ with a local retraction onto $p(Y)$ and then with $(p|_Y)^{-1}$. Its derivative is the identity on $T_0Y$ and kills $\ker p$.

Suppose there are points $x_n\in M\setminus Y$ tending to $0$ such that

\[
\operatorname{rank}(p|_{T_{x_n}M})\leq1,
\qquad
\|p(x_n-\rho(x_n))\|\geq c\|x_n-\rho(x_n)\|
\quad(c>0).
\tag{PNY3}
\]

Then $(M,Y)$ cannot satisfy both Whitney conditions at $0$. To prove this, take a subsequence for which $T_{x_n}M$ tends to a $d$-plane $T$ and the complex secant lines $\mathbb C(x_n-\rho(x_n))$ tend to a line $\ell$. Condition (a) gives $T_0Y\subset T$; condition (b), applied to the actual lower points $\rho(x_n)$, gives $\ell\subset T$. The rank inequality is closed on the Grassmannian, so $\dim p(T)\leq1$.

The normalized secants lie asymptotically in $\ker D\rho_0$. Indeed, $\rho(x_n)=\rho(\rho(x_n))$, and the integral of $D\rho$ on the segment between these two points differs from $D\rho_0$ by an operator tending to zero. Dividing that identity by the secant norm proves the assertion. The second inequality in (PNY3) gives $p(\ell)\ne0$.

The two nonzero lines $p(T_0Y)$ and $p(\ell)$ are distinct. Otherwise a nonzero vector $v\in\ell$ would satisfy $p(v)=p(w)$ for some $w\in T_0Y$. Then $v-w\in\ker p\subset\ker D\rho_0$, whereas $D\rho_0v=0$ and $D\rho_0w=w$, forcing $w=0$ and then $p(v)=0$. Consequently

\[
p(T_0Y)+p(\ell)=\mathbb C^2\subset p(T),
\qquad \dim p(T)\leq1,
\tag{PNY4}
\]

a contradiction. The noncollapse hypothesis concerns chords between the two sets. Avoiding the tangent lines to each set separately is insufficient.

### The projection input and its actual parameter calculation

For a reduced pure $d$-dimensional complex analytic germ $H$ with $d\geq2$ and a smooth lower curve $Y$, define the polar curve for a projection $p$ by

\[
P(p)=\overline{\{x\in H_{\mathrm{reg}}:
\operatorname{rank}(p|_{T_xH})<2\}}.
\tag{PNY5}
\]

All closures and curves in this section are reduced. The generic polar-family input states that a dense constructible set of projections gives either the empty germ or a one-dimensional $P(p)$, with $P(p)\cap Y\subset\{0\}$, and admits the following local family description after removing a proper parameter subset. The union $P(p)\cup Y$ and its plane image have simultaneous finite branch parametrizations. Teissier's additional algebraic route uses the simultaneous normalization of the plane family, pulled back to that of the union, and the theorem that differentiation in a projection parameter while fixing the first plane coordinate preserves its relative Lipschitz algebra. The needed coordinate differences are integral over the plane diagonal ideal on every ordered pair of covering branches. The direct root estimate below passes these equations to the selected fibre, without requiring an isomorphism for the complete fibre algebra. The generic equisaturation source theorem supplies stronger conclusions. The later direct branch-series proof obtains the required derivative and chord estimates from the curve-family normalization input alone, and does not import those additional algebraic stability conclusions. These are substantial inputs, not consequences of the word “generic.”

Here is the calculation that turns those inputs into the chord estimate needed above. Near a selected projection choose coordinates with that projection at $a=b=0$, so that the family has the form

\[
p_{a,b}(Z)=\left(Z_1+\sum_{j=3}^N a_jZ_j,
Z_2+\sum_{j=3}^N b_jZ_j\right),
\qquad
p_{a,b}(Z_\lambda(t,a,b))
=\bigl(t^{m_\lambda},v_\lambda(t,a,b)\bigr).
\tag{PNY6}
\]

Here $m_\lambda\geq1$ is fixed on a branch, the parameters range in a small open set, and all functions are holomorphic. The first plane coordinate is held fixed when differentiating in $b_k$. On a polar branch, for $t\ne0$ in its dense regular part, the differential of the first plane coordinate on $T_ZH$ is nonzero: its value on $\partial_tZ_\lambda$ is $m_\lambda t^{m_\lambda-1}$. The second plane differential is proportional to the first, because the polar rank is at most one. Since $H$ itself does not depend on the projection parameters, $\partial_{b_k}Z_\lambda$ belongs to $T_ZH$, and the first plane differential vanishes on it. Differentiating the second coordinate therefore gives

\[
\partial_{b_k}v_\lambda
=d\!\left(Z_2+\sum_{j=3}^N b_jZ_j\right)
 (\partial_{b_k}Z_\lambda)+(Z_\lambda)_k
=(Z_\lambda)_k
\quad(3\leq k\leq N).
\tag{PNY7}
\]

On the branch $Y$, the same identity holds: $\partial_{b_k}Z_\lambda$ is tangent to $Y$ and its first plane differential is zero, so it is zero where that differential is nonzero. Holomorphic continuation extends (PNY7) across the branch origin. No assumption that every defining Jacobian minor is nonzero is needed.

The plane coordinate $v$ belongs to the relative Lipschitz algebra. In the source's algebraic route, the stated stability under $\partial_{b_k}$ and (PNY7) place every remaining ambient coordinate in that same algebra. The direct integral-equation estimate below, or the later branch-series estimate at its smaller normalization floor, proves that on the selected fibre each coordinate is a Lipschitz function on the *plane image* of the union $P(p)\cup Y$. The first two coordinates are already plane coordinates. Taking the largest of their finitely many constants gives

\[
\|u-u'\|\leq C\|p(u)-p(u')\|
\qquad
\bigl(u,u'\in P(p)\cup Y\text{ near }0\bigr).
\tag{PNY8}
\]

This also makes the projection injective on the reduced union after shrinking. It is crucial that the coordinate functions descend to the plane Lipschitz algebra: holomorphic functions on a simultaneous normalization alone would not prove (PNY8). Teissier's complete key lemma [V.1.2.2, pp.462–466](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=150) provides the family route; I.6.2.1, pp.352–354 identifies the estimate with exclusion of all limiting chords from the kernel. I.6.4.2, pp.359–361 supplies the generic equisaturation mechanism using its own named lower inputs. The derivation here is relative to those exact inputs; simultaneous normalization, saturation structure, parameter stability and its generic-to-total integral-dependence specialization source have not thereby been independently discharged. The later root estimate supplies the needed restriction of known equations to a fibre, and does not import the stronger final fibre-algebra isomorphism.

If $(H_{\mathrm{reg}}\setminus Y,Y)$ is Whitney at $0$, a nonempty branch of $P(p)$ would have regular points outside $Y$ tending to $0$. Choose such a sequence and the retraction above. Apply (PNY8) with $u=x_n$ and $u'=\rho(x_n)$; the polar definition supplies the rank inequality in (PNY3). The critical-secant obstruction then gives a contradiction. Thus the general curve polar germ $P_{d-1}(H,0)$ is empty.

<a id="SH02-FAG-POLAR-MULTIPLICITY"></a>

### From the curve obstruction to the first fibre bound

[Polar multiplicity in linear sections and Whitney strata](../polar-multiplicity-in-sections.html#GM0) proves the full general-section multiplicity formula used below, including reduced singular and reducible germs and every permitted index. Its [finite-degree calculation](../polar-multiplicity-in-sections.html#MD0) proves positivity of the multiplicity of every nonempty reduced polar germ; the [Whitney-stratum theorem](../polar-multiplicity-in-sections.html#EQ0) proves constancy of all polar multiplicities using the direct conormal bounds.

The exact conormal polar-section input says that, for $0\leq k\leq d-1$ and a general projective $(d-k)$-plane $L\subset\mathbb P^{N-1}$, the conormal section is the closure of its regular-upper part and its proper image is the general polar $P_k(H,0)$. These density and actual-image assertions are part of the input. Intersecting only the fibre and assuming all its points are limits of regular polar points would omit them.

With that input, the projective dimension theorem gives the precise test

\[
P_k(H,0)=\varnothing
\quad\Longleftrightarrow\quad
\dim\kappa^{-1}(0)<N-1-d+k.
\tag{PNY9}
\]

For completeness, if the fibre dimension is below the displayed threshold, a general $L$ misses it; properness then removes the entire conormal section near $0$. If the dimension is at least the threshold, the projective dimension theorem forces the fibre to meet every $L$ of that dimension. Density of the regular polar part and the proper-image identity put $0$ in the polar germ. This is Teissier IV.4.1.1 and IV.6.1.1(a), [pp.432–433 and 451](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=120); the section input remains at its exact scope.

Now assume $0<t<d$ and $Y$ has dimension $t$. A general linear section $A$ of codimension $t-1$ meets $Y$ in a smooth curve and gives the reduced pure-dimensional germ

\[
H'=(H\cap A)_{\mathrm{red}},\qquad
Y'=Y\cap A,\qquad
d'=d-t+1\geq2.
\tag{PNY10}
\]

The generic slice input includes density of $H_{\mathrm{reg}}\cap A$ in every component of $H'$. The Whitney conditions pass to this slice as follows. Its tangent at an old regular point is $T_xH\cap T A$. Every limiting $T$ contains $T_0Y$ by (a); since $A$ is transverse to $T_0Y$, it is transverse to every such $T$. Intersection of planes is continuous at transverse pairs. Hence the sliced tangent limits are $T\cap T A$, containing $T_0Y\cap T A=T_0Y'$. Every secant between a point of $H'$ and a point of $Y'$ lies in $T A$, so (b) puts its limit in that same intersection. If a regular point of $H'$ belongs to the old singular locus, approximate it within its smooth sliced patch by old regular points, using the stipulated density and tangent continuity. A diagonal approximation preserves both tangent and secant limits. Thus no new Whitney-stratification existence theorem is invoked in this transfer.

The curve argument makes $P_{d'-1}(H',0)=P_{d-t}(H',0)$ empty. The exact general-section multiplicity formula IV.6.2.1 identifies its multiplicity with that of $P_{d-t}(H,0)$. The index is in its allowed range because $d-t=d'-1$. A nonempty reduced analytic polar germ has positive multiplicity, so $P_{d-t}(H,0)$ is empty. Applying (PNY9) yields

\[
\dim\kappa^{-1}(0)<N-1-t,
\qquad\text{hence}\qquad
\dim\kappa^{-1}(0)\leq N-2-t.
\tag{PNY11}
\]

The section dimension is $d-t+1$, not $d-t$. The proof just given is relative to the exact polar-family, saturation, conormal-section and multiplicity inputs. It reconstructs the first necessity proposition at that scope and does not prove the required dimension of $D_0$.

### The equal-dimension case and the remaining necessity step

When $d=t$, Whitney (a,b) forces $H=Y$ as germs. If there were regular upper points outside $Y$ arbitrarily close to $0$, choose a flattening retraction to $Y$ and a convergent sequence of tangent $d$-planes and projected secant lines. Condition (a) forces the limiting plane to equal $T_0Y$, since their dimensions agree. Condition (b) puts the projected secant line in that plane, while the retraction calculation puts it in the complementary kernel. This is impossible. Regular points outside $Y$ are dense in each component not equal to $Y$, so the germ equality follows. The actual graph blow-up then has no retained component and $D_0$ is empty, as required by the criterion.

This case also checks why the two fibre bounds must stay distinct. For a smooth linear $H=Y=\mathbb C^d\subset\mathbb C^N$,

\[
\kappa^{-1}(0)=\mathbb P^{N-d-1},\qquad
\dim\kappa^{-1}(0)=N-d-1>N-d-2,
\qquad D_0=\varnothing.
\tag{PNY12}
\]

Thus (PNY11) is used only for $0<t<d$; it is not silently extended to the equal-dimension empty-blow-up case. For a zero-dimensional lower stratum, the preceding principal-divisor dimension argument already gives the exceptional threshold $N-2$ whenever the divisor is nonempty, and the contact sufficiency proof applies.

For positive codimension, Teissier's source route is Whitney regularity $\Rightarrow$ polar equimultiplicity $\Rightarrow$ the expected dimension of the actual exceptional fibre. Teissier V.1.2, pp.455–470 supplies this route with hyperplane, multiplicity, finite conormal-comparison and strict-transform inputs. The first bound (PNY11), its parameter proof and the equal-dimension check are now available here at their stated scopes. The following direct hyperplane proof supplies full exceptional-fibre necessity using that first bound and the stated analytic dimension results. No source prose or image is reproduced in this independently written exposition.

<a id="SH02-FAG-RELATIVE-LIPSCHITZ-FIBRE"></a>

<a id="SH02-FAG-LIPSCHITZ-ALGEBRA"></a>

## Integral equations give the chord estimate on a fibre

[The integral-equation and relative-algebra proof](../polar-sections-and-lipschitz-algebras.html#BI0) proves the converse metric-to-ideal equation, stability of every relatively integral branch function under fixed-first-coordinate parameter derivatives, generic-to-total equations and the actual generic reduced fibre-algebra isomorphism. The connection acts on the family algebra; constant normalized-chart lifts give local parallel fibre identifications. The nongeneric contact and arbitrary-specialization counterexamples below retain their original scope.

The estimate (PNY8) needs a one-way consequence of relative saturation. It does not require an isomorphism between the fibre of the whole relative saturated algebra and the saturated algebra of the fibre. We prove the consequence directly, keeping the generic family and parameter-derivation inputs separate.

### A uniform root bound

Let $g_1,\ldots,g_q$ and $h$ be holomorphic functions on an analytic coordinate domain. Suppose that $h$ is integral over the ideal $I=(g_1,\ldots,g_q)$: on a neighbourhood it satisfies

\[
h^m+a_1h^{m-1}+\cdots+a_m=0,
\qquad m\geq1,\qquad a_j\in I^j.
\tag{RLS1}
\]

Shrink the domain so that the holomorphic coefficients in finite expressions of each $a_j$ as a sum of degree-$j$ monomials in the $g_\nu$ are bounded. Consequently there are finite constants $M_j\geq0$ such that, pointwise,

\[
\delta=\max_{1\leq\nu\leq q}|g_\nu|,
\qquad |a_j|\leq M_j\delta^j.
\tag{RLS2}
\]

If $\delta=0$, (RLS1) gives $h=0$. If $\delta>0$, put $\lambda=|h|/\delta$. For $\lambda>1$, the same equation gives

\[
\lambda^m\leq\sum_{j=1}^m M_j\lambda^{m-j}
\leq\lambda^{m-1}\sum_{j=1}^m M_j,
\qquad
|h|\leq\max\left(1,\sum_{j=1}^mM_j\right)\delta.
\tag{RLS3}
\]

For $\lambda\leq1$ the final bound also holds. This proves it at every point, including zeros of the ideal. The proof uses a given integral equation and bounded coefficients; it uses neither normality nor an equality of integral closures after specialization. Restricting that equation to any analytic fibre preserves the equation and the inclusion of each coefficient in the corresponding ideal power. Passing to the reduced fibre also preserves the pointwise bound. This restriction is a one-way implication, with no assertion that every integral element of the fibre extends to an integral element of the family.

### Apply the bound to every pair of branches

Retain the exact simultaneous branch parametrizations used in (PNY6), with parameter $s=(a,b)$ near the selected projection. They cover the actual reduced union $P(p_s)\cup Y$ near its marked point in each nearby fibre. On an ordered pair of branches, with parameters $t,u$, the plane diagonal ideal is

\[
I_{\lambda\mu}=\left(
t^{m_\lambda}-u^{m_\mu},
v_\lambda(t,s)-v_\mu(u,s)\right)
\subset\mathbb C\{t,u,s\}.
\tag{RLS4}
\]

Relative Lipschitz saturation is defined by integral dependence of the difference of a function on such same-parameter pairs over this diagonal ideal. If a relative plane function is pulled back to the normalization of the union, its integral equations pull back as well: their coefficients stay in the corresponding powers of (RLS4). Thus the needed hypothesis is an actual integral-dependence equation for each coordinate difference on every ordered pair of these covering branches.

The retained parameter-derivation stability and (PNY7) supply exactly this hypothesis for the coordinates $Z_k$, $3\leq k\leq N$. Apply (RLS3) to each of their differences. There are only finitely many branches, ordered branch pairs and ambient coordinates, so shrink to common branch discs and a common parameter neighbourhood and take the largest of their finitely many constants. The bound is uniform also when either branch parameter is zero and when the two branches are different.

The first two original coordinates satisfy the identities in (PNY6): they are the plane coordinates minus the finite sums with coefficients $a_j$ and $b_j$. Those coefficients are bounded on the chosen parameter neighbourhood. Combining their bounds with the bounds for the other coordinates and comparing the maximum norm with the Euclidean norm gives

\[
\|Z_\lambda(t,s)-Z_\mu(u,s)\|
\leq C\,
\|p_s(Z_\lambda(t,s))-p_s(Z_\mu(u,s))\|.
\tag{RLS5}
\]

Here $C$ is independent of $\lambda,\mu,t,u,s$ in these neighbourhoods. Since the parametrizations cover the actual fibre union, (RLS5) holds for every pair of its points, rather than only pairs of general points on one branch. In particular it holds on the selected fibre $s=0$, including pairs consisting of a critical-curve point and a point of $Y$. When the two plane images agree, (RLS5) forces the original points to agree. This proves the required injectivity and the precise inverse chord estimate (PNY8).

No identification of the complete fibre algebra was used. Nor did we infer integral dependence on the family from integral dependence on general fibres. The latter inference is a different theorem: the generic-to-total specialization principle used in Teissier's proof of parameter-derivation stability remains among that provider's lower sources. The present root argument does not prove that principle, simultaneous normalization or parameter-derivation stability.

### Why equality after specialization cannot be presumed

The distinction can be checked without a curve-family theorem. In the convergent power-series ring $R=\mathbb C\{x,y,s\}$, set

\[
I=(x^2,s+y^2),\qquad w=s+y^2,
\qquad R=\mathbb C\{x,y,w\}.
\tag{RLS6}
\]

The last equality means the analytic change of coordinates, with inverse $s=w-y^2$. This ideal is integrally closed. Indeed, an element integral over $I$ remains integral over $(x^2)$ after quotienting by $w$. For a nonzero convergent series $f\in\mathbb C\{x,y\}$ of $x$-order $v<2$, a monic integral equation over $(x^2)$ would have leading term of $x$-order $mv$, while every other term has order at least $2j+(m-j)v>mv$. Its unique lowest-order term cannot cancel. Hence the image of the element is divisible by $x^2$, and the original element belongs to $(x^2,w)=I$. The zero image is included.

On the fibre $s=0$, the image ideal is $I_0=(x^2,y^2)$. It does not contain $xy$, as its series have no $x^1y^1$ coefficient. Nevertheless

\[
(xy)^2-x^2y^2=0,
\qquad -x^2y^2\in I_0^2,
\qquad xy\in\overline{I_0}\setminus I_0.
\tag{RLS7}
\]

Thus specializing the integral closure of $I$ gives a strictly smaller ideal than the integral closure of its specialized image. This example disproves an unrestricted commutation claim; it says nothing against a properly hypothesized equisaturation theorem. Similarly, holomorphicity on a normalization is insufficient for the chord bound: on the cusp $(t^2,t^3)$ the function $t$ has difference of order one from its value at the origin, while the plane chord has order two. The required integral relations, and all mixed branch pairs, are essential.

Teissier defines relative Lipschitz saturation in [I.6.4, p.357](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=45). His stronger equisaturation definition is I.6.4.1, p.358; I.6.4.2, pp.359–361 derives parameter stability using the saturated-curve structure and a generic-to-total integral-dependence specialization principle. Its subsequent integration and fibre-algebra identification are stronger conclusions than this application needs. The moving-projection identity has the source antecedent [V.1.2.2, pp.465–466](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=153).

The direct conormal-slice and exceptional-fibre proofs can therefore use the exact generic family and relative integral-dependence/parameter-stability floor without separately importing the final fibre-algebra isomorphism. The subsequent normalization and direct branch-series proofs supply the corresponding inputs for this route; the stronger saturation and mixed-derivative statements have their separate linked proofs. This is an independently written proof of a standard integral-equation estimate, with no source prose or media reproduction and no original research claim.

<a id="SH02-FAG-ANALYTIC-LOCAL-ALGEBRA"></a>

## Local analytic algebra: preparation, division and finite modules

The local-algebra conclusions designated ALA1–ALA14 are supplied by these full programme proofs, with their common-neighbourhood and radius hypotheses:

- [Weierstrass preparation and division, Theorems 1, 2 and 6, Corollary 3 and Propositions 4–5](../../analytic-finiteness-and-preparation/weierstrass-preparation-and-division.html#the-statements), with the [contour preparation proof](../../analytic-finiteness-and-preparation/weierstrass-preparation-and-division.html#preparation-by-the-zeros-in-one-fibre) and [division and Noetherian proof](../../analytic-finiteness-and-preparation/weierstrass-preparation-and-division.html#division-finite-generation-and-elementary-algebra). Preparation constructs symmetric coefficients without choosing holomorphic roots. Division is unique for every holomorphic dividend on the stated open product with a common root-radius gap, and its bounds have constants independent of the dividend. The proof includes the degree-zero germ case, the finite remainder module and finite generation. [The worked coefficient and division estimates](../../analytic-finiteness-and-preparation/weierstrass-preparation-and-division.html#exercises-and-complete-solutions) retain the coefficient-order and cone bounds.
- [The local analytic algebra proof in analytification, Section 2](../../AG-QC/complex-analytic-spaces-and-analytification.html#2-local-analytic-algebra) gives contour preparation and division, the finite free remainder module and the Noetherian argument.
- [Holomorphic germ rings, Lemmas 2.3–2.4](../../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#2-weierstrass-polynomials) supply polynomial/analytic divisibility; [Theorems 3.1 and 3.4 and Lemmas 3.2–3.3](../../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#3-unique-factorization) supply unique factorization, integral closure of manifold germ rings, translated-stalk factorization and nearby coprimality. [Theorem 4.1 and Corollary 4.2](../../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#4-finiteness) supply the triangular finite-module statements.

These are local ring and module conclusions. Normalization of a singular reduced space is proved separately in the normal analytic section.

<a id="SH02-FAG-OKA-COHERENCE"></a>

## Uniform Oka coherence and coherent-module operations

The substantive coherence and module conclusions designated OCA1–OCA13 are supplied by [Proposition 1.2 and Lemma 1.3](../../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#1-coherent-modules-on-a-ringed-space), the [uniform Oka proof, Theorem 2.1 and Lemma 2.2](../../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#2-oka-s-coherence-theorem), and [Theorem 3.1 on coherent analytic sheaves](../../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#3-the-category-of-coherent-analytic-sheaves). The Oka argument constructs bounded polynomial relations generating every nearby relation stalk on one neighbourhood; Noetherianity at a single stalk is not substituted for this uniform statement. The module theorem proves coherent kernels, images, intersections, Hom, tensor products and finite partial resolutions. [Cartan coherence, Corollary 1.2](../../complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces.html#1-the-ideal-sheaf-of-an-analytic-set) and [Theorem 3.2 on closed analytic models](../../complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces.html#3-complex-spaces) provide the coherent quotient rings and their coherent modules.

These links supply the stated foundational coherence conclusions; worked calculations retain their own separate statements.

<a id="SH02-FAG-ANALYTIC-LOCAL-GEOMETRY"></a>

## Finite local projection, dimension and reduced-ideal coherence

The local geometric conclusions designated ALG1–ALG22 have these exact proof routes:

- [Analytic germs and their ideals, Section 1](../../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html#1-germs-of-analytic-sets-and-their-ideals), [coordinates adapted to a prime ideal, Section 2](../../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html#2-coordinates-adapted-to-a-prime-ideal), and [the finite extension and primitive element, Section 3 and Lemmas 3.1–3.4](../../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html#3-the-finite-extension-and-a-primitive-element) construct the prime finite projection and one discriminant denominator.
- [The local parametrization theorem, Theorem 4.1 and Lemma 4.2](../../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html#4-the-local-parametrization-theorem) supplies the proper finite covering and dense connected regular representative. [Theorem 5.1, Corollary 5.2, Theorem 5.4 and Proposition 5.5](../../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html#5-the-nullstellensatz-and-dimension) supply the analytic Nullstellensatz, finite germ decomposition and strict dimension drop for a proper analytic subset.
- [Cartan's reduced-ideal coherence theorem, Theorem 1.1 and Corollary 1.2](../../complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces.html#1-the-ideal-sheaf-of-an-analytic-set) uses actual parameter-polynomial interpolation and nearby reduced-ideal stalks. One tuple of parameter-polynomial coefficients and one nonzero discriminant coefficient describe all these stalks on a common neighbourhood; interpolation extracts the coefficients and Oka supplies the coherent ideal sheaf.

These local proofs do not replace the global component-label and compactly uniform intersection arguments in the next section.

<a id="SH02-FAG-ANALYTIC-SINGULAR-COMPONENTS"></a>

## Singular loci and global analytic components

We use the proved [analytic local geometry](#SH02-FAG-ANALYTIC-LOCAL-GEOMETRY), including uniform reduced ideal coherence, finite irreducible germ decomposition, connected dense regular representatives and strict proper-subset dimension drop. The [Oka module operations](#SH02-FAG-OKA-COHERENCE) give coherent quotients and images. The [holomorphic coordinate proof](#SH02-FAG-HOLOMORPHIC-CALCULUS) supplies the implicit function theorem on the ambient manifold. All spaces here are reduced analytic spaces; the statements do not supply nonreduced-space regularity or a proper-image theorem.

## Local singular loci and reduced charts

The local Jacobian and density statements SGC1–SGC2 use [Cartan's Theorem 2.1](../../complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces.html#2-singular-points). Fixed generators of the reduced ideal on one neighbourhood give the Jacobian-minor description of its analytic singular locus; finite component intersections and singular loci are removed to obtain a dense regular part. [Definition 3.1 and Theorems 3.2–3.3](../../complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces.html#3-complex-spaces) provide reduced complex-space charts and coherent quotient structures. The regularity/generator criterion, chart invariance, global labels, analytic closure and compact uniformity are proved below.



### Regularity and the number of ideal generators

Let $R=\mathcal O_{A,x}$, $\mathfrak m$ its maximal ideal, and $d=\dim(A,x)$. Suppose $\mathfrak m$ has $s$ generators $h_k$, lifted to ambient holomorphic germs centered at $x$. Since the coordinate classes generate $\mathfrak m$, write $z_j=\sum_ku_{jk}h_k+f_j$ with $f_j\in I_{A,x}$. Differentiation gives $dz_j=\sum_ku_{jk}(0)dh_k+df_j$. Thus the span of the $df_j$ has dimension at least $n-s$. If $s<n$, select $n-s$ independent ones. Their common zero germ is a manifold of dimension $s$ containing $A$, whence $s\geq d$. If $s\geq n$, the inequality follows from $d\leq n$. If $s=d$, the containing manifold and ALG14 force equality, so $x$ is regular. At a regular point submanifold coordinates give exactly $d$ generators, and fewer are impossible.

For completeness this minimum also equals $\dim_{\mathbf C}\mathfrak m/\mathfrak m^2$. One inequality follows by reducing generators. For the other, lift a vector-space basis and let $Q$ be the quotient of the finite $R$-module $\mathfrak m$ by their span. Then $Q=\mathfrak mQ$. On a finite generating list this has a coefficient matrix with entries in $\mathfrak m$. Its matrix $I-C$ has determinant congruent to $1$ modulo $\mathfrak m$, hence a unit; the adjugate forces $Q=0$. Thus

$$
\mu_R(\mathfrak m)=\dim_{\mathbf C}(\mathfrak m/\mathfrak m^2)\geq d,
\qquad x\text{ regular}\ \Longleftrightarrow\ \mu_R(\mathfrak m)=d.
\tag{SGC3}
$$

Let $A$ be pure $d$-dimensional and let a nonempty analytic subset $B\subset A$ have local dimension at most $d-p$ near the point under consideration. Its ideal as an $\mathcal O_A$-module is $I_B=I_{B,\mathrm{ambient}}/I_{A,\mathrm{ambient}}$, so it is coherent. If $s$ germs generate its stalk at $x$, they generate on a neighborhood: their coherent cokernel has zero stalk, and finitely many local generators of that cokernel vanish on a smaller neighborhood. Choose a nearby regular point $y$ of $B$, using SGC2, with $k=\dim(B,y)\leq d-p$. The maximal ideal of $\mathcal O_{B,y}=\mathcal O_{A,y}/I_{B,y}$ has $k$ generators. Lift them and adjoin the $s$ ideal generators to generate the maximal ideal of $\mathcal O_{A,y}$. SGC3 gives $k+s\geq d$, hence $s\geq p$. If the original $x$ itself is regular on $B$ and singular on $A$, apply the same argument at $x$: SGC3 gives $k+s>d$. Therefore

$$
\mu_{\mathcal O_{A,x}}(I_{B,x})\geq p\quad(x\in B),\qquad
\mu_{\mathcal O_{A,x}}(I_{B,x})\geq p+1\quad(x\in B_{\mathrm{reg}}\cap A_{\mathrm{sing}}).
\tag{SGC4}
$$

The first inequality uses a nearby regular point with the same finite generators; it does not replace a singular $x$ by a regular point when proving the second inequality. Purity and the local codimension hypothesis are essential to this statement.

### Reduced space charts and global component labels

A morphism of reduced analytic subsets is a map locally given by restrictions of finitely many ambient holomorphic coordinate functions. Equivalently it is continuous and pulls back every holomorphic germ: the reverse implication applies that property to each target coordinate and chooses simultaneous representatives; continuity keeps a sufficiently small source neighborhood in the target chart. Composition then gives the local ring map

$$
F_x^*:\mathcal O_{B,F(x)}\longrightarrow\mathcal O_{A,x},\qquad g\longmapsto g\circ F.
\tag{SGC5}
$$

A reduced complex space is a locally compact Hausdorff space, countable at infinity, with a sheaf of continuous functions locally isomorphic as a ringed space to an analytic subset with its reduced structure sheaf. Analytic subsets, morphisms and local ideals are defined in these charts. Regularity is invariant under chart isomorphism: if a holomorphic parametrization of a smooth source has a holomorphic inverse on its image, ambient lifts of the inverse differentiate the composition to the identity. The parametrization is an immersion and the holomorphic implicit function theorem makes its image a local submanifold; the homeomorphism identifies the entire nearby target with that image. The converse uses the inverse isomorphism. Thus the dimensions of regular charts agree, and SGC1–SGC2 glue to an intrinsic analytic singular locus.

Let $R_\alpha$ be the connected components of $X_{\mathrm{reg}}$ and put $X_\alpha=\overline{R_\alpha}$ in $X$. At a fixed point $x$ choose irreducible local representatives $A_1,\ldots,A_N$ on a chart neighborhood $U$. For each $l$ choose a possibly larger-within-$U$ neighborhood $\Omega_l$ on which $(A_l)_{\mathrm{reg}}$ is connected and dense. Delete its intersections with the other $A_k$. Those intersections are proper analytic subsets of this connected regular manifold; otherwise density would imply containment of origin germs. Their finite union is proper, and the complex-line complement argument from ALG proves that

$T_l=(A_l)_{\mathrm{reg}}\cap\Omega_l\setminus\bigcup_{k\ne l}A_k$ is connected and dense in $A_l\cap\Omega_l$. It lies in exactly one global regular component $R_{\alpha(l)}$. Now take a smaller common neighborhood $\Omega\subset\bigcap_l\Omega_l$. Its restrictions $T_l\cap\Omega$ need not be connected, but their label was fixed on the larger connected $T_l$ and remains the same. Every regular point in $\Omega$ lies in one of them. Closure inside $\Omega$, using density and the finite closed local representatives, gives

$$
X_\alpha\cap\Omega=\bigcup_{\alpha(l)=\alpha}(A_l\cap\Omega),\qquad
X=\bigcup_\alpha X_\alpha,
\quad\{X_\alpha\}_\alpha\text{ is locally finite and analytic}.
\tag{SGC6}
$$

Indeed at most $N$ labels meet $\Omega$; if a component closure meets the open neighborhood, its regular component also meets it. For the equality, any convergent regular sequence in that label eventually lies in $\Omega$, and a subsequence lies in one of its finitely many labeled $A_l$. Conversely every point in a labeled $A_l\cap\Omega$ is approached by its $T_l\cap\Omega$. These $X_\alpha$ are the global irreducible components. Their germs can be reducible.

For example the curve and its explicit parametrization are

$$
\Gamma=\{(x,y):y^2=x^2(1+x)\},\qquad
t\longmapsto(t^2-1,t(t^2-1)),\qquad
\Gamma_{\mathrm{reg}}=\Gamma\setminus\{(0,0)\}\simeq\mathbf C\setminus\{-1,1\}.
\tag{SGC7}
$$

The inverse off the node is $t=y/x$. The map's derivative $(2t,3t^2-1)$ never vanishes simultaneously; the equation's gradient has no other singular point. The displayed punctured plane is connected. Thus the curve has one global component, while at the node its two local smooth branches are $y=\pm x\sqrt{1+x}$. The two parameters $t=\pm1$ both map to the node; no global bijection at that point is claimed.

### Analytic closure and compactly uniform intersections

For closed analytic subsets $A,B$ of a reduced complex space, retain exactly the global components $A_\alpha$ not contained in $B$. Local finiteness makes their union closed and analytic. On the connected regular locus of each retained component, the intersection with $B$ is a proper analytic subset, so its complement is dense. Taking closures proves

$$
\overline{A\setminus B}=\bigcup_{A_\alpha\not\subset B}A_\alpha
\quad\text{is analytic}.
\tag{SGC8}
$$

Finally let $(A_\lambda)_{\lambda\in\Lambda}$ be any family of globally defined closed analytic subsets of $X$. Descending-chain stabilization for analytic germs chooses a minimal germ among finite intersections at $x$. Let $B$ be one such finite intersection, defined globally. Minimality says $(B,x)\subset(A_\lambda,x)$ for every $\lambda$. Keep the global components of $B$ whose closures contain $x$, obtaining $\widetilde B$. Local finiteness removes all other components on one neighborhood of $x$, so $B=\widetilde B$ there. For every kept component its connected regular part has nonempty open intersection with some neighborhood where the germ containment holds. Its intersection with $A_\lambda$ is analytic and contains that open part; the identity principle gives the whole regular component, and closedness gives the whole kept component. Thus $\widetilde B\subset A_\lambda$ for every $\lambda$, without making a common choice among infinitely many germ representatives. Hence the full intersection equals $B$ on the one chosen neighborhood. A finite cover of a compact subset and the union of their finite index selections give

$$
\forall K\subset X\text{ compact}\quad\exists J\subset\Lambda\text{ finite},\ \exists U\supset K\text{ open}:
\qquad \left(\bigcap_{\lambda\in\Lambda}A_\lambda\right)\cap U
=\left(\bigcap_{\lambda\in J}A_\lambda\right)\cap U.
\tag{SGC9}
$$

This proves both analyticity and the precise compactly uniform finite-intersection statement. The global-component step supplies uniformity that germwise Noetherianity alone would not supply. The empty family has intersection $X$.

The complete selected antecedents are [Demailly II.4.31–II.4.33 and II.5.1–II.5.5, printed/PDF pp.100–103](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=100). The Jacobian and local-purity statements use the current local providers linked above; persistence of component distinctions, generator transfer, chart invariance and larger-neighborhood global labels are explicit below. The reduced-ideal coherence proof has the linked Cartan provider. The closing observation about smooth stratifications supplies no Whitney conditions, triangulation, curve selection, proper-image theorem or holomorphic rank theorem. This is an independently written standard reconstruction relative to the stated lower providers and elementary-calculus floor.

<a id="SH02-FAG-COMPATIBLE-FINITE-FLAG"></a>

## SH02-FAG-COMPATIBLE-FINITE-FLAG — One finite coordinate flag for all component germs

**Lemma.** Let a finite collection of analytic germs at \(0\in\mathbb C^n\) be given. Choose all their finitely many irreducible component germs \(A_\lambda\), with prime ideals \(J_\lambda\) and dimensions \(d_\lambda\). There are common linear coordinates \(z_1,\ldots,z_n\), arbitrarily close to any given basis, adapted to every \(J_\lambda\). For every \(k>d_\lambda\), \(J_\lambda\) contains a triangular Weierstrass polynomial in \(z_k\), with coefficients in the preceding coordinates and coefficient orders as in ALG2.1. In particular \(\mathcal O_n/J_\lambda\) is finite over \(\mathcal O_{d_\lambda}\), which injects into it.

For every coordinate \(z_j\), \(j>d_\lambda\), there is also a monic coordinate equation
\[
 Q_{\lambda j}(z_1,\ldots,z_{d_\lambda};z_j)=0
 \quad\hbox{on }A_\lambda,\qquad
 Q_{\lambda j}(0,T)=T^{r_{\lambda j}}.
\]
These finitely many equations hold on common smaller representatives. Pure components of one common dimension \(p\) admit a single proper finite projection to a sufficiently small first-\(p\)-coordinate polydisc, each dominating that polydisc. For a deleted component \(A_\lambda\) of dimension \(d_\lambda<p\), the equations with \(d_\lambda<j\le p\) give a proper finite polynomial container over its first \(d_\lambda\) coordinates. Its intersection with the first-\(p\)-coordinate polydisc contains the projection of \(A_\lambda\) and has dimension at most \(d_\lambda\).

**Proof.** Run ALG Proposition2.2's induction simultaneously on the finite tuple of proper ideals. At dimension \(n\), choose a nonzero \(g_\lambda\in J_\lambda\) for each nonzero ideal; the zero ideal imposes no condition. The finitely many lowest nonzero homogeneous terms have nonzero product. Hence a last basis vector, as close to its prescribed value as desired, makes every selected germ regular of its exact order. Prepare each selected germ. This supplies its last-variable monic polynomial and the stated coefficient orders.

Hold that vector fixed and apply the same simultaneous induction to all contractions \(J_\lambda\cap\mathcal O_{n-1}\) in the complementary coordinate space. Subsequent linear changes use only those first \(n-1\) variables, preserving the already prepared last-variable polynomials and their coefficient orders. An ideal which becomes zero stops contributing equations; continuing for the other ideals yields one flag and integers \(d_\lambda\). The simultaneous construction is finite, and arbitrary closeness is preserved at each stage.

Successive Weierstrass division, exactly local-ring Corollary4.2, makes each quotient finite over its stopping ring, with injection because the contraction there is zero. Its stopping integer equals \(d_\lambda\) by the dimension identification already proved in ALG5.4. The case of the zero prime has \(d_\lambda=n\); a zero-dimensional component has \(d_\lambda=0\).

Each coordinate class is integral over this base ring. Apply ALG Lemma3.2 to its minimal polynomial in the finite fraction-field extension: the base germ ring is integrally closed, so the coefficients are holomorphic in the first \(d_\lambda\) variables, and since the coordinate vanishes at zero the minimal polynomial is Weierstrass. This gives the displayed equations. Only finitely many germs and identities occur; choose simultaneous representatives on one smaller chart.

The triangular root bounds in ALG2.3 give \(|z_k|\le C_{\lambda k}\max_{i<k}|z_i|\) on each germ when \(k>d_\lambda\). Choose increasing anisotropic radii with strict margins for these finitely many bounds, and scale all radii down inside the common representative. There is then no escape through any relevant vertical boundary. Each fibre is finite by the successive monic equations, and the preimage of a compact base set is closed in a compact smaller vertical trap. This proves the proper finite representative claim. For pure components of dimension \(p\), the supplied ALG4.1 primitive/discriminant proof gives a nonempty covering over a dense base complement; properness makes each component's image the whole smaller base polydisc.

For the container, allow the coordinates \(z_{d_\lambda+1},\ldots,z_p\) to range over all of \(\mathbb C^{p-d_\lambda}\) and impose their monic coordinate equations over a small first-\(d_\lambda\)-coordinate base. Root bounds make the resulting analytic set proper finite over that base. The independent finite-fibre dimension lemma FMR2 bounds its dimension by \(d_\lambda\). Restriction to the open first-\(p\)-coordinate polydisc preserves that upper bound; it need not preserve properness. Taking the finite union over deleted components gives exactly EHF's codimension-two container, or FMR1's proper codimension-one container. Empty deleted sets require no equations. □

This lemma is a finite-tuple extension of the supplied one-ideal induction, not an invocation of generic flatness, a relative Grassmannian or a general proper-mapping theorem.

The exact local inputs are [adapted-coordinate Proposition 2.2, its triangular root bound, minimal-polynomial Lemma 3.2, covering Theorem 4.1 and dimension Theorem 5.4](../../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html), [Weierstrass preparation and division](../../analytic-finiteness-and-preparation/weierstrass-preparation-and-division.html), and [local-ring finite-module Corollary 4.2](../../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#4-finiteness). The finite tuple and common representative bounds are supplied by the proof above; a single-germ statement alone would not supply them. This independently authored lemma is dedicated to [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

Here is the dependency order for the following analytic arguments. First prove FMR2 from one-germ finite projection and the regular finite-fibre rank lemma. It uses neither FMR1 nor normalization, principal purity or a proper-image theorem. The finite flag above and FMR2 then supply EHF's polynomial-container bounds, singular boundedness and principal-zero purity. Those inputs give NFA's finite normalization and normal-curve regularity. They in turn give FMR1's curve parametrization and FMR3's compact affine-analytic finiteness. The later source-jump, proper-image, marked-curve and direct CWS/DPC–CSB–HN arguments use these supplied steps in that order. The optional PNY9 all-index polar-multiplicity route has its own additional hypotheses.

The elementary algebra and complex-calculus inputs imported by the linked local proofs retain their stated hypotheses. No completion flatness, general coherent proper-direct-image theorem or delta-constant simultaneous-normalization theorem is used by this finite-flag argument.


<a id="SH02-FAG-FINITE-MAP-RANK-FOUNDATIONS"></a>

## Finite fibers, compact analytic subsets and holomorphic rank

All complex spaces in this section are reduced, Hausdorff, locally compact and countable at infinity. We use the supplied [local analytic geometry](#SH02-FAG-ANALYTIC-LOCAL-GEOMETRY), [singular loci and global components](#SH02-FAG-ANALYTIC-SINGULAR-COMPONENTS), [holomorphic extension and principal-zero purity](#SH02-FAG-HOLOMORPHIC-EXTENSION-FOUNDATIONS), and [finite normalization and normal codimension two](#SH02-FAG-NORMAL-ANALYTIC-FOUNDATIONS). The elementary analytic inputs are the holomorphic inverse and constant-rank theorems, power series and the elementary covering estimate below. Dimensions and maxima are stated on spaces of bounded dimension; all arguments used locally also apply on a neighborhood of bounded dimension. This proof supplies no general proper-image theorem.

### A nonconstant function on an irreducible space is open

Let $X$ be irreducible and $f$ a nonconstant global holomorphic function. The connected dense regular locus and the identity principle show that $f-f(x)$ is nonzero on every irreducible local component at $x$: vanishing on any such component would give a nonempty open regular part on which $f$ is constant and hence make it constant on $X$.

Choose one local component $A$ of dimension $d>0$. Its zero subset $B=V(f-f(x))$ has dimension at most $d-1$. The simultaneous compatible finite-flag proof above, also used in the codimension-two extension proof, gives a finite proper projection of $A$ to a $d$-polydisk and a finite polynomial container of $\pi(B)$ of dimension at most $d-1$. One can see the latter directly from the simultaneous flag for each component of $B$: its first $b$ coordinates, with $b=\dim B_l<d$, are free, while the remaining first $d$ coordinates satisfy monic prepared equations; this container has dimension $b$. The finite union of these containers is proper and analytic in the base.

Choose a complex line through the origin whose germ is contained in neither that container nor the discriminant. Such lines exist: choose a direction at which the first nonzero homogeneous terms of finitely many defining nonzero germs are nonzero. Its inverse image is defined in $A$ by $d-1$ independent linear equations on the base. Successive principal-zero purity gives dimension at least one for each nonempty local component. The independent FMR2 proof below, using only one-germ finite projection and constant rank, gives dimension at most one. The resulting curve germs cannot lie in $B$, since their projections would lie in the zero-dimensional intersection of the chosen line with the container, while a finite fiber cannot contain a curve.

NFA's finite normalization of the chosen reduced curve component and regularity of normal curves give a local coordinate parametrization, hence a holomorphic curve $\gamma$ through $x$ on which $f-f(x)$ is nonzero. Write its pullback as $t^k u(t)$, $k\geq1$, with $u(0)\ne0$. A holomorphic $k$th root of the unit, obtained on a small disk from its power series, changes the local coordinate to $w=t\,u(t)^{1/k}$. The inverse theorem applies since $w'(0)\ne0$. The map $w\mapsto w^k$ maps a small disk onto a disk. Thus every neighborhood of $x$ maps onto a neighborhood of $f(x)$:

$$
f\text{ nonconstant on irreducible }X
\quad\Longrightarrow\quad
f:X\longrightarrow\mathbf C\text{ is open}.
\tag{FMR1}
$$

No proper image of $B$ is invoked: the finite polynomial container is the one already constructed by compatible flags.

### Finite fibers bound the source dimension

Let $F:X\to Y$ have finite fibers, without assuming properness. Near $x$, an irreducible component $A$ of the source germ is contained in the inverse image of one component $C$ of the target germ: irreducibility applied to the finite union of those inverse images proves this. A compatible finite projection of a representative of $C$ maps it to a polydisk of dimension $p=\dim(C,F(x))$. Its composition with $F|A$ still has finite fibers. Let $m=\dim A$. Apply the [regular finite-fibre rank lemma already proved above](#sh02-fag-image-images-and-the-rank-away-from-a-proper-analytic-subset) to this composition on the connected dense regular representative of $A$. Its maximum differential rank is $m$, hence $m\leq p$. Consequently

$$
F\text{ has finite fibers}
\quad\Longrightarrow\quad
\dim_x X\leq\dim_{F(x)}Y,\qquad
\dim X\leq\dim Y.
\tag{FMR2}
$$

This argument survives source restriction because it needs finite fibers alone. An arbitrary source restriction of a proper map is not asserted proper.

If $X$ is compact and irreducible, FMR1 makes any nonconstant holomorphic image both compact and open in $\mathbf C$, which is impossible. Hence global holomorphic functions are constant on $X$. A compact analytic subset $K$ of any complex space has finitely many global components, by SGC local finiteness and a finite neighborhood cover of $K$. They are closed and compact. If global holomorphic functions of the ambient space separate points, their restrictions are constant on every such component and separation makes that component a singleton. Therefore

$$
\mathcal O(X)\text{ separates points},\quad K\subset X
\text{ compact analytic}
\quad\Longrightarrow\quad |K|<\infty.
\tag{FMR3}
$$

In a coordinate domain the coordinate functions give the separation. Compactness by itself does not: a positive-dimensional projective manifold is a counterexample.

### Countable smooth covers and finite surjections

A countable compact exhaustion and finite chart covers of its members give a countable analytic atlas. On any chart of dimension at most $D$, take the regular loci of its finitely many irreducible representatives, then repeat on their singular loci. SGC gives analytic singular loci of strictly smaller dimension. After at most $D+1$ stages these regular pieces cover the chart. Countably many chart restrictions thus cover any bounded-dimensional complex space by countably many complex manifolds of dimension at most that of the space. This is a covering argument; it claims neither a locally finite global stratification nor Whitney conditions.

A continuously differentiable map from a real $a$-dimensional compact coordinate box into $\mathbf R^b$, $a<b$, is Lipschitz there. Subdivide into boxes of side $\varepsilon$. Their number is at most $C\varepsilon^{-a}$ and each image has diameter at most $C'\varepsilon$. Enclosing those images in $b$-boxes gives an outer-volume bound

$$
\operatorname{vol}_b^{*}(\text{image})
\leq C''\varepsilon^{\,b-a}
\longrightarrow0
\qquad(a<b).
\tag{FMR4}
$$

Countably many compact boxes exhaust each coordinate patch. The same estimate applies to a smooth submanifold of smaller dimension in the target.

If $F$ is surjective and $\dim X<\dim Y=n$, choose a regular target chart of dimension $n$. Its inverse image is covered by the countable smooth pieces above, of complex dimension less than $n$. Their images have zero $2n$-dimensional measure by FMR4, whereas their union would cover the target chart. This contradiction, combined with FMR2, proves

$$
F\text{ finite and surjective}
\quad\Longrightarrow\quad \dim X=\dim Y.
\tag{FMR5}
$$

The lower bound uses only surjectivity, holomorphicity and countability. Neither Sard's theorem nor a Whitney stratification is an additional provider.

### Fiber dimensions and the intrinsic maximum rank

The proof of FJ1–FJ2 already chooses $s$ independent linear forms cutting the local fiber to an isolated point and excludes escape through a compact vertical boundary. FMR3 now supplies finiteness of the compact projection fibers, and FMR2 supplies their dimension bound. Thus that proof gives upper semicontinuity of $q_F$ without any properness assumption on $F$; its boundary projection is separately proved proper. Empty boundary sets, $s=0$ and a point vertical factor are handled there.

For pure $d$-dimensional $X$, put

$$
q_F(x)=\dim_x F^{-1}(F(x)),\qquad
\rho_F(x)=d-q_F(x),\qquad
\rho(F)=\max_{x\in X}\rho_F(x).
\tag{FMR6}
$$

The function $\rho_F$ is lower semicontinuous and integer valued. Its global maximum holds on a nonempty open subset and hence on any dense open regular subset. To identify that maximum with differential rank, work component by component and in a target embedding. The maximum Jacobian rank on a connected regular component has dense open locus, since its minors are holomorphic. On that locus the constant-rank theorem gives $q_F=d-r$. Intersect it with the open maximum-$\rho_F$ locus to obtain $\rho(F)=r$ on an irreducible space; on a pure reducible space take the maximum over components. For a nonpure source define $\rho(F)$ by the maximum of the ranks of its irreducible components. The same argument shows that the maximum can be read on any dense open subset of their regular loci. These statements concern the maximum; pointwise differential rank at a critical smooth point need not equal $\rho_F(x)$.

### Restriction cannot increase the maximum rank

We prove, by induction on the dimension of an irreducible domain, that

$$
Z\subset X\text{ analytic},\qquad
\rho(F|Z)\leq\rho(F).
\tag{FMR7}
$$

Dimension zero is immediate. Assume the assertion for all smaller-dimensional domains. First handle a normal irreducible domain of dimension $d$. If an irreducible component of $Z$ equals $X$ there is nothing to prove. For a proper component, work locally and choose a nonzero holomorphic germ $h$ vanishing on it, using the reduced ideal. Principal-zero purity puts it inside a pure $(d-1)$-dimensional hypersurface $D=V(h)$. The singular locus of the normal domain has dimension at most $d-2$, so the regular points of every component of $D$ lying in $X_{\mathrm{reg}}$ are dense. At those points the tangent-space differential of $F|D$ is a restriction of that of $F$. Its rank is at most $\rho(F)$, and density gives $\rho(F|D)\leq\rho(F)$. The induction hypothesis on the components of $D$ gives the same bound for $F|Z$. This local bound everywhere proves the global bound. No hypersurface is claimed to be smooth everywhere.

For an arbitrary irreducible domain take its supplied finite normalization $\nu:\widetilde X\to X$, and put $H=F\circ\nu$. The map is an isomorphism over $X_{\mathrm{reg}}$. This set has dense inverse image, so the maximum-rank description in FMR6 gives $\rho(H)=\rho(F)$; equivalently on each connected regular normalization component the minors propagate this bound from that dense open subset.

Let $Z$ be a proper irreducible component of the analytic subset and put $\widetilde Z=\nu^{-1}(Z)$. It is analytic, has dimension at most $\dim Z<d$ by FMR2, and maps finitely and surjectively to $Z$. The normal-domain case just proved gives $\rho(H|\widetilde Z)\leq\rho(H)$.

It remains to justify $\rho(F|Z)\leq\rho(H|\widetilde Z)$ without claiming pointwise equality of fiber germs. Choose a regular target patch $U\subset Z_{\mathrm{reg}}$ on which the differential of $F|Z$ has its maximum rank $r_Z$, and write $k=\dim Z$. Cover $\nu^{-1}(U)$ by the countable smooth pieces used above. They have dimension at most $k$. If all had dimension less than $k$, FMR4 would prevent their images from covering $U$. Thus some piece has dimension $k$. It is an open regular piece of a $k$-dimensional local analytic component $C$ of $\widetilde Z$. The finite-fiber constant-rank argument in FMR2 shows that $\nu|C$ has maximum differential rank $k$; full-rank points are dense in that piece. At such a point over $U$, its derivative is onto the tangent space of $U$, so the derivative of $H|C$ has rank $r_Z$. By the already assumed smaller-domain restriction assertion, $\rho(H|C)\leq\rho(H|\widetilde Z)$ (componentwise locally, with the ambient maximum as bound). This proves the needed inequality and completes the induction. For $k=0$ the inequality is immediate.

The argument also applies to a reducible domain by taking its components. Analytic components of a subset lie in some domain component; local bounds and the generic rank description then give FMR7.

### A fiber test for the normalization step

Use the nodal curve $\Gamma$ of SGC7 and let $X=\Gamma\times\mathbf C_s$. Its finite normalization is
$\nu(t,s)=(t^2-1,t(t^2-1),s)$, with normal source $\mathbf C^2$. The monic equation $t^2=x+1$ bounds $t$ over compact subsets, so the displayed surjection is proper with finite fibers. It is an isomorphism off the node, and the uniqueness of the supplied finite normalization identifies it with that normalization. The regular locus $(\Gamma\setminus\{0\})\times\mathbf C$ is connected and dense, so $X$ is globally irreducible. Define

$$
F(x,y,s)=(y-sx,\ s^2-1-x),\qquad
(F\circ\nu)(t,s)=((t^2-1)(t-s),\ (s-t)(s+t)).
\tag{FMR8}
$$

The zero fiber downstairs is the curve $(x,y,s)=(s^2-1,s(s^2-1),s)$ and has dimension one at $(0,0,1)$. There are two points over that point. Near $(1,1)$ the factor $s+t$ is a unit, so the fiber upstairs is $s=t$ and has dimension one. Near $(-1,1)$ both $t-1$ and $t-s$ are units; the equations give $t+1=0$ and $s+t=0$, so that fiber germ is isolated and has dimension zero. Thus finite surjectivity does not identify each individual upstairs fiber germ with the full downstairs fiber germ. FMR7 avoids exactly this false shortcut.

### Rank bounds the image and detects surjections

To cover the image of a holomorphic map on a manifold by constant-rank pieces, take its maximum-Jacobian-rank open locus, cover it by constant-rank neighborhoods, and repeat on the analytic rank-drop set. Cover that smaller set by its regular pieces and repeat. Dimension strictly drops on each exceptional analytic set, so this yields countably many constant-rank neighborhoods. For an arbitrary complex space first use its countable smooth analytic pieces. FMR7 bounds the rank on every exceptional analytic component by $\rho(F)$; open regular restrictions keep that bound.

On a constant-rank neighborhood the image is a smooth complex submanifold of that rank. If the target is a manifold of dimension $n>\rho(F)$, FMR4 shows its image has measure zero. Countable union proves the same for the whole image. For a pure-dimensional target take its dense regular locus; every nonempty open set meets that locus, so the image still has empty interior. Finally any generic constant-rank image patch inside a target embedding is a submanifold contained in the analytic target and hence has dimension at most $\dim Y$, by dimension monotonicity. This gives $\rho(F)\leq\dim Y$. If $F$ is surjective, restrict to the inverse image of a maximal-dimensional target component and use FMR7 and the empty-interior result to obtain the opposite inequality. Therefore

$$
Y\text{ pure},\ \rho(F)<\dim Y
\Longrightarrow \operatorname{int}_Y F(X)=\varnothing,
\qquad
F\text{ surjective}\Longrightarrow\rho(F)=\dim Y.
\tag{FMR9}
$$

The source antecedents are complete [Demailly II.5.7–II.5.9, p.104](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=104) and [II.8.1–II.8.6, pp.116–118](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=116). II.5.6 is context; the countable smooth cover here supplies precisely what the dimension argument uses. The p.116 preceding normalization/Grauert sentence and p.118 Remmert–Stein/proper-image statements and incomplete proof are context, not selected providers. The chosen-line construction, countable covering estimate and two-stage normal/general restriction induction make the source shortcuts explicit. The result is an independently written standard reconstruction relative to the named analytic/normal and elementary-calculus floors. Remmert–Stein extension, general proper images and the Whitney and subanalytic foundations have their separate proof sections or providers.

<a id="SH02-FAG-PROPER-IMAGE-EXTENSION"></a>

## Proper images and closure across smaller analytic sets

We now supply the two analytic image and closure theorems used earlier. The inputs are the proved [local analytic geometry](#SH02-FAG-ANALYTIC-LOCAL-GEOMETRY), [singular loci and global components](#SH02-FAG-ANALYTIC-SINGULAR-COMPONENTS), [bounded holomorphic removal and principal-zero purity](#SH02-FAG-HOLOMORPHIC-EXTENSION-FOUNDATIONS), [finite dimensions and maximum rank](#SH02-FAG-FINITE-MAP-RANK-FOUNDATIONS), and the source-side analyticity of [FJ1–FJ4](#SH02-FAG-FIBRE-JUMP). We consume only FJ's fiber-semicontinuity and source-jump arguments here, not its subsequent proper-image deduction. All spaces have their reduced analytic structures and the Hausdorff, local compactness and countability conditions stated above. The [holomorphic coordinate proof](#SH02-FAG-HOLOMORPHIC-CALCULUS) supplies constant rank. Complex-line connectivity, countability and outer-volume estimates are used with the hypotheses stated in their respective proofs.

The exact assertions are

$$
\begin{aligned}
&A\subset X\text{ analytic},\quad \dim A\leq p,\quad
Z\subset X\setminus A\text{ closed analytic},\\
&\dim_z Z>p\quad(z\in Z)
\quad\Longrightarrow\quad \overline Z^{\,X}\text{ analytic};\\
&F:X\longrightarrow Y\text{ proper and holomorphic}
\quad\Longrightarrow\quad F(X)\text{ analytic in }Y.
\end{aligned}
\tag{RMP1}
$$

The first hypothesis concerns all points of $Z$, not merely its maximum dimension. If $Z$ is pure of dimension $s>p$, its nonempty closure remains pure of dimension $s$. Empty sets are allowed; for empty $A$ the closure assertion is immediate. For nonempty $A$ we take $p\geq0$. Applying the second theorem to a closed analytic subspace also gives analyticity of its proper image.

### The induction and the target-local reduction

Let $E_m$ be the first assertion when $\dim Z\leq m$, including its pure version; $Q_m$ the proper-image theorem for maps with finite fibers and source dimension at most $m$; and $P_m$ the full proper-image theorem with that source bound. The order is

$$
P_{m-1}\Longrightarrow E_m,\qquad
(E_m,P_{m-1})\Longrightarrow Q_m,\qquad
(E_m,Q_m,P_{m-1},\mathrm{FJ},\mathrm{FMR})\Longrightarrow P_m.
\tag{RMP2}
$$

This order separates the finite case from the positive-dimensional-fiber case.

A proper map between these spaces is closed. Indeed lifts of a convergent target sequence lie in the compact preimage of that sequence together with its limit; a convergent subsequence gives a lift of the limit. Compactness and local analytic charts give the required subsequence, and charts are first countable. The same argument applies to any closed subset of the source.

For a target-local proof choose neighborhoods $V\Subset U$ of the target point, with $U$ embedded in a coordinate domain. In $F^{-1}(U)$ only finitely many global analytic components meet the compact set $F^{-1}(\overline V)$, by SGC local finiteness. Their restrictions are closed analytic subspaces, so their maps to $U$ remain proper. Each component is pure of its fixed finite dimension. It suffices to prove the assertion for each and then take their finite union over $V$. This reduces locally unbounded global dimensions to finite bounds without imposing a new global hypothesis.

In dimension zero a reduced complex space is discrete. Over a compact target neighborhood its proper preimage is a finite subset of that discrete space. The image is locally finite discrete, hence analytic. Thus $P_0$ and $Q_0$ hold. The nonempty scope of $E_0$ is vacuous, since $p\geq0$. Suppose henceforth that all $P_{m-1}$ assertions are proved.

### Extension across a smaller analytic set

Analyticity and closure are local, so embed the ambient complex space in a coordinate domain $\Omega\subset\mathbf C^n$. Its analytic subsets are analytic in that domain, and closure stays in the closed ambient space. First induct on $p=\dim A$ to reduce to $A$ smooth of dimension $p$. For a nonpure $A$, on a small chart put all components of dimension less than $p$, the singular loci of the $p$-dimensional components and their pairwise intersections into a closed analytic set $D$ of dimension at most $p-1$. Outside $D$ the remaining $A$ is locally a smooth $p$-manifold. Extend there by the smooth case. The resulting closure is analytic off $D$, remains pure $s$ for a pure-$s$ input, and extends across $D$ by the smaller-$p$ induction. For $p=0$ the analytic set is locally discrete, and there is no smaller residual set. This handles mixed dimensions rather than treating $A_{\mathrm{sing}}$ alone as the whole residual set.

We may therefore straighten $A$ to $L=\mathbf C^p\times\{0\}$ locally and work at $0\in\overline Z$. Otherwise closure is empty on a neighborhood of $0$. The global components of $Z$ are countable and locally finite in $\Omega\setminus A$. A component has regular points belonging to no other component; there its dimension is the dimension of $Z$. The hypothesis in RMP1 makes every component have dimension greater than $p$. Group them by the finitely many possible dimensions $p<s\leq m$. Each group is a closed analytic pure-$s$ union off $A$. Prove the pure case and take a finite union of closures.

If $s=n$, the pure-$n$ analytic set is the whole connected complement of $A$ when nonempty, so its closure is the coordinate neighborhood. Suppose $s<n$. Choose forms $\xi_1,\ldots,\xi_s$ successively so that

$$
\begin{aligned}
&\dim\bigl(Z\cap\{\xi_1=\cdots=\xi_j=0\}\bigr)=s-j
&&\text{on every nonempty component},\quad 1\leq j\leq s;\\
&\dim\bigl(L\cap\{\xi_1=\cdots=\xi_j=0\}\bigr)=p-j
&&1\leq j\leq p;\\
&\operatorname{rank}\bigl(d(\xi_1,\ldots,\xi_s)|_{T_{a_\alpha}Z_\alpha}\bigr)=s
&&\text{at one chosen regular point of each component }Z_\alpha.
\end{aligned}
\tag{RMP3}
$$

Here and below an empty cut has no asserted dimension. For the first condition avoid forms identically zero on each positive-dimensional component of the preceding cut; principal-zero purity then decreases dimension by one. For the last condition keep the restrictions of the first $j$ forms independent on each of the chosen $s$-dimensional tangent spaces. Until $j=p$, also keep them independent on $L$. Every excluded condition is a proper linear subspace of the space of forms. There are countably many: SGC local finiteness and a countable atlas give countably many components at every stage. A countable union of proper complex linear subspaces has zero real volume by FMR's covering estimate and cannot cover the space of forms. Thus these choices exist simultaneously. Tangent independence also ensures ambient independence.

For $j>p$ subtract a combination of the first $p$ forms to make $\xi_j|_L=0$. This invertible row operation preserves projection rank and the successive zero cuts. Complete to coordinates $(u,v)\in\mathbf C^s\times\mathbf C^{n-s}$, where $u_j=\xi_j$, so $L=\mathbf C^p\times0$. The extra tangent condition makes the projection $\pi(u,v)=u$ have generic rank $s$ on every component of $Z$; its maximum-rank locus is dense on their connected regular representatives. In particular no component can have image entirely in the $p$-dimensional linear set $A'$ of the base.

The zero slice of $Z$ is discrete off the origin. Its points are countable. Choose a small vertical sphere whose radius is none of their distances from $0$. The closed set $Z\cup A$ avoids that sphere over $u=0$. Compactness then gives a smaller base ball $B'$ and vertical ball $B''$, with closed product inside the coordinate domain, such that

$$
(Z\cup A)\cap(\overline B'\times\partial B'')=\varnothing,\qquad
\pi:(Z\cup A)\cap(B'\times B'')\longrightarrow B'
\text{ is proper}.
\tag{RMP4}
$$

The properness is precisely the vertical-boundary exclusion; the base of a compact inverse-image test stays in the interior of $B'$. Let $A'=B'\cap(\mathbf C^p\times0)$. Over $U_0=B'\setminus A'$ the restriction to $Z$ is proper and its fibers are compact analytic subsets of a coordinate ball. FMR3 makes them finite.

Let $S_1$ be the singular locus in that inverse image and put $D_1=\pi(S_1)$. By $P_{m-1}$ its image is closed analytic in $U_0$. Finite dimensions give $\dim D_1\leq s-1$. On $U_1=U_0\setminus D_1$ the source is smooth. Let $S_2$ be the locus where $d\pi$ has rank less than $s$ and put $D_2=\pi(S_2)$. It is closed analytic in $U_1$ by the same lower-dimensional induction. Again finite dimensions give

$$
\dim S_i\leq s-1\leq m-1,\qquad
\dim D_i\leq s-1,\qquad
G=U_1\setminus D_2
=B'\setminus(A'\cup D_1\cup D_2).
\tag{RMP5}
$$

The sets $D_1,D_2$ are analytic on their respective open domains. We do not presume that $D_2$ is analytic across $D_1$ or $A'$. All proper restrictions above are over open target complements of closed bad images. The complement $G$ is open, dense and connected by successive deletion of proper analytic subsets from a connected complex manifold. The whole displayed bad union is closed, as the complement of $G$, and has empty interior.

The inverse image of $G$ in $Z$ is dense: any open part of a component meets the generic full-rank projection locus; a full-rank neighborhood maps onto an open base set and therefore meets dense $G$. This also proves it is nonempty, since $0$ is in the closure of $Z$. Over $G$, $\pi$ is a proper local biholomorphism with finite fibers. Properness excludes other source points after choosing the finitely many local inverse neighborhoods of a fiber, so it is a covering of its open and closed image. Connectedness of $G$ makes that image all of $G$, with constant degree $q\geq1$.

For a linear form $\lambda$ in the vertical coordinates, form the polynomial of the $q$ actual sheet values:

$$
P_\lambda(u,T)=
\prod_{v\in Z\cap\pi^{-1}(u)}(T-\lambda(v))
=T^q-\sigma_1(u)T^{q-1}+\cdots+(-1)^q\sigma_q(u),
\qquad u\in G.
\tag{RMP6}
$$

Symmetry under sheet permutations makes the coefficients single-valued holomorphic functions. They are bounded by
$|\sigma_j|\leq\binom qj(\|\lambda\|r'')^j$.
Use bounded manifold removal successively across $D_2$ inside $U_1$, then $D_1$ inside $U_0$, then $A'$ inside $B'$. This order is valid with the relative analytic bad sets and extends each coefficient holomorphically to $B'$. It invokes EHF, not the extension theorem now being proved.

In the product define

$$
W=\bigcap_\lambda
\{(u,v):P_\lambda(u,\lambda(v))=0\},\qquad
W\cap\pi^{-1}(G)=Z\cap\pi^{-1}(G),\qquad
|\pi^{-1}(u)\cap W|\leq q^{\,n-s}.
\tag{RMP7}
$$

SGC9 applies to these globally defined analytic zero sets and makes their arbitrary intersection analytic, with a finite equation family near each compact subset. Taking coordinate forms gives the finite-fiber bound. Over $G$ the equality is exact: if a proposed vertical point differs from every one of the $q$ actual points, a linear form separates it from all of them simultaneously, by avoiding finitely many proper hyperplanes, and its polynomial does not vanish. The polynomials vanish on the dense good part of $Z$, so continuity gives $Z\subset W$ throughout the product.

FMR2 bounds every component of $W$ by dimension $s$. Every $s$-dimensional component $C$ has a generic full-rank finite-fiber projection to the $s$-dimensional base, hence an open image patch meeting $G$. Its regular locus therefore has a nonempty open part contained in $Z$. The connected regular locus of $C$ stays connected after deleting the proper analytic intersection with the original $A$, whose dimension is at most $p<s$. Since $Z$ is closed analytic on the ambient complement of $A$, the identity principle gives $C\setminus A\subset Z$, and density gives $C\subset\overline Z$.

Conversely, each local irreducible component of pure-$s$ $Z$ lies in a local component of $W$ of dimension at most $s$. Strict proper-subset dimension forces equality with a local top component. Thus every point of $Z$ lies in a global $s$-component of $W$. Their union is locally finite, closed and analytic by SGC. Hence

$$
\overline Z\cap(B'\times B'')
=\bigcup_{\dim C=s,\ C\text{ component of }W}C.
\tag{RMP8}
$$

This proves the smooth-$A$ case, including purity, and completes the induction on $p$ and the proof of $E_m$. The final propagation used the original analytic $A$; no analyticity of the composite bad base across earlier exceptional sets was assumed.

### Finite proper images first

Consider a proper finite map from an irreducible pure-$m$ source, $m>0$. FMR gives maximum rank $m$. Locally embed the source in $\mathbf C^n$, choose reduced-ideal generators $g$ and ambient representatives $f$ of target coordinates. On the regular source the conormal matrix has rank $n-m$. Therefore the closed bad set is locally

$$
B=X_{\mathrm{sing}}\ \cup\
\left(X\cap V\left(\text{all }n\text{-minors of }
\begin{pmatrix}Dg\\Df\end{pmatrix}\right)\right),\qquad
\dim B\leq m-1.
\tag{RMP9}
$$

On the regular locus these equations say exactly that $dF$ fails to be injective. The locally analytic descriptions glue to the intrinsic singular/non-immersion set. Generic full rank makes it proper. Its restriction to $B$ is proper, so $D=F(B)$ is analytic by $P_{m-1}$, and FMR applied to the surjection onto $D$ gives $\dim D\leq m-1$.

Over $Y\setminus D$ the source is regular and the map is an immersion. Each point of a finite fiber has an immersion neighborhood whose image is a closed local submanifold in a target neighborhood. Properness confines all preimages of a smaller target neighborhood to those finitely many source neighborhoods. Their images form a finite union of analytic $m$-manifolds. Thus $F(X)\setminus D$ is closed analytic and pure $m$ there. If it is empty, the image is already the analytic $D$. Otherwise its inverse image is a nonempty complement of a proper analytic subset of irreducible $X$, hence dense. Continuity and closedness of the proper image give

$$
F(X)=\overline{F(X)\setminus D},\qquad
\dim D<m,
\quad\Longrightarrow\quad F(X)\text{ analytic by }E_m.
\tag{RMP10}
$$

This proves $Q_m$. The finite component reduction proves it for all sources of the stated bound.

We will also use its purity consequence. The analytic proper image of an irreducible source is irreducible: near a regular point belonging to just one image component, its analytic inverse image contains a nonempty open part of the source; connected regular-locus propagation puts the entire source into that component. Properness and local finiteness justify this local component selection. For a finite map, FMR5 makes its image have the same dimension as that irreducible source, and SGC purity gives that dimension at every branch. A pure-$m$ source is a locally finite union of such components. Near any compact target neighborhood properness permits only finitely many of them; their images are pure $m$. Hence every finite proper image of a pure-$m$ source is pure $m$.

### Positive-dimensional fibers and the strict exceptional-image bound

Now let $F$ be an arbitrary proper map from irreducible pure-$m$ $X$. If its maximum rank is zero, it is constant on the connected regular locus and then on $X$, so its image is a point. Otherwise set $r=\rho(F)>0$ and $s=m-r=\min q_F$. The proved FJ source theorem gives the proper closed analytic set $J=\{q_F\geq s+1\}$. Its image $D=F(J)$ is analytic by $P_{m-1}$.

The required strict dimension bound uses fibers. At a generic regular point of a component $C$ of $J$, no other component meets. A fiber component of dimension at least $s+1$ lies wholly in $J$: nearby points on its pure representative have fiber dimension at least that component's dimension. Near the chosen point it therefore lies in $C$. The generic fiber dimension of $F|C$ is at least $s+1$. The open maximum-rank locus of that restriction meets these generic points, so

$$
\rho(F|C)\leq\dim C-(s+1)\leq m-s-2=r-2,\qquad
J\ne\varnothing\Longrightarrow\dim D\leq r-2<r.
\tag{RMP11}
$$

The image dimension statement follows from FMR's surjective-rank theorem on the already analytic $F(J)$. For $r=1$ the bound forces $J$ empty. Empty $J$ needs no extension across an exceptional image. If $F(J)=F(X)$, its image is already analytic. In the remaining case work on $X\setminus F^{-1}(D)$ and $Y\setminus D$, where $q_F=s$ everywhere and the restricted map remains proper.

### A constant-fiber-dimensional image is locally analytic

Fix a source point over the remaining target. The FJ construction chooses $s$ independent ambient forms $u$ cutting its local fiber to an isolated point, and a small product $(u,v)\in B'\times B''$. Its vertical-boundary exclusion gives a target neighborhood $U$ such that

$$
\begin{aligned}
&F^{-1}(y)\cap(\overline B'\times\partial B'')=\varnothing\quad(y\in U),\\
&H=(F,u):X\cap F^{-1}(U)\cap(B'\times B'')\longrightarrow U\times B'
\text{ is proper and finite}.
\end{aligned}
\tag{RMP12}
$$

Properness follows by keeping both target and $u$ in compact subsets and excluding escape through $\partial B''$. The remaining vertical fibers are compact analytic subsets of a coordinate ball, so FMR3 makes them finite. No global properness of an arbitrarily truncated source was asserted; this augmented map's properness was proved separately. If $s=0$, $B'$ is a point and the same argument is a local finite map.

Apply the already proved $Q_m$ to obtain an analytic image $W$ of $H$. The local source is pure $m$, so the finite-image purity consequence makes $W$ pure $m$. For each target $y$, the local $F$-fiber is pure $s$: a smaller-dimensional component would have regular own points away from its other components, where the whole fiber germ and hence $q_F$ had that smaller dimension, contradicting constancy.

The restriction of $H$ to that fiber is a proper finite projection to $B'$. If the fiber is nonempty, take one of its $s$-dimensional components. Its closed restriction remains proper, $Q_m$ makes its image analytic, and FMR5 gives image dimension $s$. A closed analytic subset of the connected $s$-ball with that dimension is the entire ball. Thus $W_y$ is either empty or all of $B'$, also when $s=0$. Taking the slice at $u=0$ gives an analytic subset $V\subset U$ with

$$
\begin{aligned}
&W=V\times B',\qquad V=\{y:(y,0)\in W\},\\
&V=F\bigl(X\cap F^{-1}(U)\cap(B'\times B'')\bigr),\\
&V\text{ pure of dimension }m-s=r.
\end{aligned}
\tag{RMP13}
$$

The purity follows from that of $W$ and the dimension of the smooth product factor. This local image argument accommodates singular source points and ramification; it needs neither constant Jacobian rank there nor a general proper-image theorem hidden in its augmented step.

For a target point, its original proper fiber is compact. Choose finitely many neighborhoods of the preceding type covering it. Closedness of the image of their closed source complement excludes other preimages after shrinking the target neighborhood. The local full image is then a finite union of the analytic pure-$r$ sets $V$. Hence $F(X)\setminus D$ is closed analytic, pure $r$, in $Y\setminus D$.

When it is nonempty, the inverse image of $D$ is a proper analytic subset of irreducible $X$. Its complement is dense, and the same continuity and closed-image argument gives

$$
F(X)=\overline{F(X)\setminus D},\qquad
\dim D<r,\qquad
E_m\text{ applied to the pure-}r\text{ complement}
\Longrightarrow F(X)\text{ analytic}.
\tag{RMP14}
$$

Here $r\leq m$, so the extension assertion already proved at this stage applies. This completes $P_m$ and the whole induction. The target-local component reduction covers reducible, nonpure and globally unbounded-dimensional spaces.

### A proper projection checks the singular-source shortcut

A singular subspace can have the same image rank as the entire source. Consider the compact nodal projective curve
$C=\{[X:Y:Z]\in\mathbf P^2:Y^2Z=X^2(Z+X)\}$.
The affine chart $Z=1$ is the SGC7 nodal curve; its only extra point is $[0:1:0]$, smooth since the derivative of the equation with respect to $Z$ is nonzero there. The affine regular locus is connected and dense, so the curve is irreducible. It is compact: projective space is the continuous quotient of the unit sphere by scalar phase, and this polynomial zero set is closed. For the projection of its product with the complex line,

$$
\begin{aligned}
&F:\mathbf C\times C\longrightarrow\mathbf C,\quad F(a,c)=a,\\
&X_{\mathrm{sing}}=\mathbf C\times\{\text{node}\},\qquad F(X_{\mathrm{sing}})=\mathbf C,\\
&\rho(F)=1,\quad q_F\equiv1,\quad J_2(F)=\varnothing.
\end{aligned}
\tag{RMP15}
$$

The map is proper because the inverse image of a compact set is its product with compact $C$. The singular image has dimension one, equal to the map's maximum rank. RMP11 correctly has no jump set here, and the augmented finite-image proof gives the full image across the singular fiber. Thus the general induction does not rely on a false strict rank bound for $F|X_{\mathrm{sing}}$.

The complete selected antecedent is [Demailly II.8.7–II.8.8, printed/PDF pp.118–121](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=118). The countable full-rank flags, ordered bounded coefficient extensions, exact top-dimensional component selection and finite-first fiber-jump induction are explicit here. The preceding rank proof and following Chow, Levi and scheme sections are context.  This is an independently written standard reconstruction at the declared analytic and elementary floor. Grauert's coherent proper direct-image theorem, the subanalytic foundations, normal Morse data and perverse theorems are separate results.

<a id="SH02-FAG-HOLOMORPHIC-EXTENSION-FOUNDATIONS"></a>

## Bounded removal, Hartogs extension and the one-equation bound

We supply the extension arguments used by the normal analytic construction. Bounded removal on a manifold needs only the local equations of a proper analytic subset and ordinary one-variable Cauchy theory. Hartogs extension across an arbitrary analytic subset of codimension at least two additionally uses locally finite analytic components, analytic singular/intersection sets and their strict dimension drop. Local boundedness on a singular space uses a compatible finite analytic projection, with the precise coordinate-polynomial property stated below. The finite-projection, local dimension and Cauchy arguments are used with the hypotheses stated in their respective proofs.


### Bounded removal on a manifold

If \(M\) is a complex manifold, \(S\) is a closed analytic subset containing no component of \(M\), and \(f\in\mathcal O(M\setminus S)\) is locally bounded near \(S\), then \(f\) has a unique holomorphic extension to \(M\). This bounded-removal statement, used in EHF1–EHF3, is proved by the actual Cauchy-circle argument in Theorem 4.2, with Corollaries 4.3–4.4. The uniqueness and connected-complement conclusions are included there. This provider is used only for bounded removal on a manifold; the unbounded Hartogs and reduced singular/normal-space statements are proved next with their additional hypotheses.


### Hartogs across smooth and singular analytic sets

Let $S\subset M$ be closed analytic and let every local component of $S$ have codimension at least two in the manifold. We impose no boundedness assumption on $f\in\mathcal O(M\setminus S)$.

First suppose $S$ is locally a smooth submanifold of codimension $c\geq2$. Choose a polydisk $D_R^n$ in which $S$ is given by $z_1=\cdots=z_c=0$. Put $z'=(z_2,\ldots,z_n)$ and

$$
W=D_R^{n-1},\qquad W'=W\setminus\{z_2=\cdots=z_c=0\},
\qquad
D_R^n\setminus S=((D_R\setminus\{0\})\times W)\cup(D_R\times W').
\tag{EHF4}
$$

Integrate $f(\eta,z')/(\eta-z_1)$ over any circle $|\eta|=\rho<R$. It is defined for all $z'\in W$ because $\eta\ne0$, and gives a jointly holomorphic function on $D_\rho\times W$. For $z'\in W'$ the full slice is in the original domain, so ordinary Cauchy identifies the integral with $f$ there. The set $W'$ is dense; continuity at every point outside $S$ gives equality on all of $(D_\rho\times W)\setminus S$. Such smaller polydisks cover a neighborhood of each point of $S$. Uniqueness glues the local extensions. This argument uses the second missing coordinate to make $W'$ dense; it does not assume that an unbounded function has removable one-variable punctures.

For a possibly singular $S$, work locally with its finitely many irreducible components. Let $T$ be the union of their singular loci and the intersections of distinct components. Retain the basic analytic facts that these sets are analytic and proper in the corresponding components. If $d=\dim S$, then

$$
T\subset S,\qquad \dim T\leq d-1,\qquad
S\setminus T\text{ is locally a disjoint union of smooth submanifolds.}
\tag{EHF5}
$$

The smooth argument extends $f$ across $S\setminus T$, as a function on $M\setminus T$. Every component of $T$ still has ambient codimension at least two. Induct on $d$. A zero-dimensional analytic set is locally discrete and smooth, so the smooth argument supplies the base case; the empty set requires no extension. The strict dimension drop makes the induction finite, and local dimension is bounded on each chosen chart. The induction extends across $T$. Dense-complement uniqueness glues all charts. We have therefore proved Hartogs extension for every closed analytic set of codimension at least two, relative to the stated singular-locus and dimension facts. No Whitney stratification or resolution is required.

### Boundedness on a singular space through symmetric sheet values

Let $X$ be a reduced complex analytic space of pure dimension $p$, and $A\subset X$ closed analytic with every local component of dimension at most $p-2$. Then any $f\in\mathcal O(X\setminus A)$ is locally bounded near $A$. For $p\leq1$, the condition forces $A$ to be empty.

We spell out the finite-projection input rather than treating the extension as its consequence by citation. Near an arbitrary point of $A$, embed $X$ in $\mathbb C^N$ and use the simultaneous compatible finite-flag proof above to choose one linear coordinate flag for its local components and those of $A$. On a sufficiently small product representative, projection onto the first $p$ coordinates is a proper finite map $\pi:X\to\Delta\subset\mathbb C^p$. Each local component of $X$ dominates $\Delta$. Outside a proper analytic set $R\subset\Delta$, it is a holomorphic covering with exactly $r\geq1$ distinct points per fibre, for the total collection of components under consideration.

For each component $A_\lambda$ of dimension $d_\lambda\leq p-2$, the same coordinate flag gives monic coordinate polynomials

$$
P_{\lambda j}(z_1,\ldots,z_{d_\lambda};z_j)=0
\quad\text{on }A_\lambda,
\qquad d_\lambda<j\leq p.
$$

For the dimension estimate, consider these polynomial equations with all remaining coordinates allowed in $\mathbb C^{p-d_\lambda}$. Their common zero set is finite and proper over a small neighborhood of the first $d_\lambda$ coordinates: every fibre is a finite collection of roots, and monic root bounds keep the inverse image of each compact base set compact. Hence its dimension is at most $d_\lambda$ by the finite-map dimension input. Restricting this analytic set to $\Delta$ gives $B_\lambda$ with that same upper dimension bound. No properness of this last restriction to an open polydisk is asserted. Let $B$ be the finite union of these sets. Then $\pi(A)\subset B$, and $B$ is analytic of codimension at least two. The simultaneous finite flag, monic coordinate equations and finite-map dimension bound are retained lower inputs. This step does not invoke a previously proved general proper-mapping theorem for $\pi(A)$.

For $z\in\Delta\setminus(R\cup B)$, define $\sigma_j(z)$ to be the elementary symmetric polynomial of degree $j$ in the $r$ values of $f$ on the fibre. Local holomorphic sheets show that it is holomorphic; symmetry makes it independent of their ordering. The values satisfy

$$
T^r-\sigma_1(z)T^{r-1}+\cdots+(-1)^r\sigma_r(z)=0.
\tag{EHF6}
$$

Near any $b\in R\setminus B$, take a relatively compact base neighborhood whose closure misses $B$. Its full inverse image is compact by properness and misses $A$. The continuous holomorphic function $f$ is bounded on that inverse image. Consequently all $\sigma_j$ are bounded there off $R$. The proved manifold bounded-removal theorem extends them across $R\setminus B$, giving holomorphic functions on $\Delta\setminus B$. The proved analytic Hartogs theorem then extends them across $B$ to all of $\Delta$.

Shrink to a base neighborhood on which all extended coefficients have absolute value at most some positive $C$. A root $t$ of EHF6 has

$$
|t|\leq1+C.
\tag{EHF7}
$$

Indeed, if $|t|>1+C$, then the absolute value of the sum of its lower terms is at most $C\sum_{j=1}^r|t|^{r-j}<C|t|^r/(|t|-1)<|t|^r$, contradicting the equation. This bounds $f$ over the complement of $R\cup B$. That inverse image is dense in every component of $X$. By continuity of $f$ on $X\setminus A$, the bound holds at every point of that set over the smaller base neighborhood. This proves local boundedness near the entire finite fibre, including singular and intersecting components. Applying the construction around each point proves the assertion. Nilpotent structure, if retained on $X$, cannot alter this pointwise boundedness of function values; all ring identifications elsewhere in this lesson use reduced spaces explicitly.

### The normal-space extension consumed by the contact proof

Let $X$ be normal and pure-dimensional, and let $A$ have codimension at least two. The normal analytic construction proves that $X_{\mathrm{sing}}$ has codimension at least two. Restrict $f\in\mathcal O(X\setminus A)$ to $X_{\mathrm{reg}}\setminus A$. The manifold Hartogs argument extends it holomorphically over all of $X_{\mathrm{reg}}$. The singular-space boundedness argument, applied with deleted set $X_{\mathrm{sing}}$, makes that extension locally bounded near every singular point. It is thus weakly holomorphic. Normality identifies weakly holomorphic and holomorphic germs, giving

$$
\mathcal O_X(U)\xrightarrow{\ \simeq\ }
\mathcal O_X(U\setminus A)
\quad\text{for every open }U\subset X.
\tag{EHF8}
$$

The extension agrees with the original function even at singular points of $U\setminus A$: both are holomorphic there and agree on the dense regular subset. Uniqueness and the sheaf property glue the extensions. Normal spaces are locally irreducible; for components of different dimensions the assertion is applied locally on each component with its own codimension assumption. This is precisely the extension used for the contact quotients across their codimension-two exceptional set.

The hypotheses distinguish two elementary failure cases. On a punctured disk, $1/z$ has a pole: codimension one does not give unbounded Hartogs extension. On the cusp with coordinate ring $\mathbb C\{t^2,t^3\}$, the bounded function $t=y/x$ on the regular punctured curve is weakly holomorphic but is not a holomorphic germ on the curve, since its Taylor expansion has a nonzero linear term. Boundedness alone does not identify the weak ring with the holomorphic ring; normality supplies that identification in EHF8.

### Pure dimension for the zero set of one equation

Let $X$ be an irreducible reduced analytic germ of dimension $p$, and let $g$ be a nonzero holomorphic germ. If its zero set is nonempty, every component has dimension $p-1$.

Retain the lower fact that a proper analytic subset of an irreducible germ has smaller dimension. It makes every component of $\{g=0\}$ have dimension at most $p-1$. Suppose one component $D$ had dimension at most $p-2$. Choose a point of $D$ away from all other zero-set components, and a pure $p$-dimensional representative on which the zero set is just that component. The function $1/g$ is holomorphic off it. The boundedness argument EHF6–EHF7 would give $|1/g|\leq C$ near that point. Points of the complement approach the chosen zero by density, and continuity makes $g$ tend to zero there, a contradiction. Hence

$$
\{g=0\}\ne\varnothing\quad\Longrightarrow\quad
\dim D=p-1\text{ for every component }D\subset\{g=0\}.
\tag{EHF9}
$$

A nowhere-zero function has empty zero set, and in dimension zero a nonzero function on a reduced irreducible germ is a nonzero constant. For reducible spaces, apply the argument on each component where $g$ is not identically zero; components on which it vanishes identically are retained with their original dimensions. Successive application gives the existing $k$-equation lower bound: on a pure $p$-dimensional space, every nonempty component of the common zero set of $k$ functions has dimension at least $p-k$. Repeated equations and zero functions are included. The bound points toward codimension at most $k$; two repeated equations in $\mathbb C^2$ can define a single line.

The source antecedents are [Demailly I.3.2–I.3.11, pp.21–22](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=21), [I.5.25–I.6.4, pp.45–46](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=45), [II.4.1–II.4.2, p.91](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=91), and [II.6.1–II.6.3, pp.105–106](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=105). The printed inequality in II.6.3 in this version has the opposite direction; the successive one-equation argument establishes the direction used here. The source's pluripolar removal route is an antecedent; the Cauchy-circle proof here needs no plurisubharmonic extension theorem. The preceding local algebra proof supplies the Noetherian ring and finite-submodule layer at its complex-calculus floor. Finite projection, analytic singular/component dimension, coherence and reduced-ideal theorems remain the stated local inputs to the extension and one-equation arguments.

<a id="SH02-FAG-NORMAL-ANALYTIC-FOUNDATIONS"></a>

## Normal analytic foundations from finite projection

We now reconstruct the normal-space and finite-normalization facts used by the contact and marked-family arguments. The proof identifies the finite-projection, coherent-module and holomorphic-extension inputs at each step.

### Exact input floor

Work with reduced complex analytic spaces and holomorphic local rings. Retain these lower inputs:

- Locally finite irreducible decomposition, dense regular loci, analyticity of singular loci, and a fundamental system of neighbourhoods with connected regular locus for an irreducible germ.
- The proper finite local projection of a pure irreducible analytic germ to a polydisc, a proper analytic exceptional base set, and a primitive linear coordinate separating its finitely many generic sheets. Coordinate values are bounded on a sufficiently small covering representative.
- Bounded holomorphic functions extend across proper analytic subsets of a complex manifold. The holomorphic implicit function theorem and ordinary local dimension facts are available.
- The [analytic local algebra proof](#SH02-FAG-ANALYTIC-LOCAL-ALGEBRA) supplies Noetherian local rings and their quotients, with finite generation of submodules of finite modules, at its elementary complex-calculus floor. The [Oka coherence proof](#SH02-FAG-OKA-COHERENCE) supplies coherent manifold rings, coherent quotients by finite nearby ideals and finite-presentation Hom/kernel/quotient sheaves. The [analytic local geometry proof](#SH02-FAG-ANALYTIC-LOCAL-GEOMETRY) supplies the reduced vanishing ideals, their coherence and analytic Nullstellensatz, together with compatible finite projections and connected dense regular loci. Analyticity of the finite-presentation support is checked below. A nonzero equation on an irreducible space has a pure codimension-one zero set when nonempty.

The determinant argument and the regularity criterion are proved below. Finite normalization, normality openness and normal singular codimension are conclusions, not inputs. The distinct codimension-two extension theorem needs two additional inputs stated in its own paragraph.

### A finite faithful ideal detects integrality

Let $A$ be a commutative ring, $Q(A)$ its ring obtained by inverting all nonzero divisors, and $I$ a finitely generated ideal containing a nonzero divisor. Suppose $w\in Q(A)$ and $wI\subset I$. Choose generators $u_1,\ldots,u_r$ and coefficients $a_{ij}\in A$ such that

\[
w u_i=\sum_{j=1}^{r}a_{ij}u_j.
\tag{NFA1}
\]

Let $C=(a_{ij})$ and let $u$ be the column of generators. Then $(w1_r-C)u=0$ over $Q(A)$. Multiplication by the adjugate gives $\det(w1_r-C)u_i=0$ for every $i$. Because $I$ contains a nonzero divisor, an $A$-linear combination of the $u_i$ becomes a unit in $Q(A)$. Hence $\det(w1_r-C)=0$ in $Q(A)$. This is a monic equation for $w$ over $A$. Neither freeness of $I$ nor a basis of its generators is needed.

In particular, an integrally closed domain contains every fraction preserving a nonzero finitely generated ideal. For a finite $A$-algebra, apply the same matrix argument to a finite generating module containing $1$ to obtain the usual finite-implies-integral assertion.

The exact algebraic antecedents are the Stacks Project tags 05BT, 052I and 00GK. Only these determinant and integrality assertions are used here.

### A universal denominator, including reducible germs

Let $B_{x}$ denote the ring of germs holomorphic on the regular locus near $x$ and locally bounded near the singular locus. Such germs are called weakly holomorphic. Multiplication and addition preserve that condition.

First suppose $(X,x)$ is irreducible. Use the retained finite projection $p:X\to D$, of generic sheet number $r$, and the primitive coordinate $u$. Outside its proper analytic exceptional base set $S$, write the sheet values $u_1(z'),\ldots,u_r(z')$. They are distinct. Set

\[
V_{\alpha j}=u_\alpha^{\,j},\quad
1\leq\alpha\leq r,\quad 0\leq j\leq r-1,
\qquad
\delta(z')=(\det V)^2.
\tag{NFA2}
\]

The square is invariant under permutations of the sheets. Thus it is holomorphic off $S$ and bounded, and extends holomorphically across $S$ on the base. It is not identically zero. The interpolation matrix has exactly $r$ rows and $r$ columns; the degree is at most $r-1$.

This same denominator works for every stalk near the selected representative, not just for functions defined on the whole cover. For a weakly holomorphic germ $f$ near a point $y$, separate the finitely many points over $p(y)$ by disjoint neighbourhoods. Properness puts the inverse image of a sufficiently small base neighbourhood inside their union. On sheets in the neighbourhood where $f$ is defined use the value of $f$; on the other neighbourhoods use zero. Solve the unique interpolation problem

\[
Vb=F,\qquad
\delta b=(\det V)\operatorname{adj}(V)F.
\tag{NFA3}
\]

The coefficients $b_j$ are holomorphic off $S$ and independent of the sheet ordering. The entries of $V$, its cofactors, $\det V$ and $F$ are bounded on this smaller representative. Hence each $\delta b_j$ is bounded and holomorphic off $S$, so extends on the base by the retained manifold removal theorem. On the selected sheets, $\delta f=\sum_{j=0}^{r-1}(\delta b_j)u^j$. This is a holomorphic function on $X$. Equality continues over the regular part by density. The pullback of $\delta$ is therefore a universal denominator on this representative.

For a reduced germ with finitely many irreducible components $X_i$, obtain a denominator $\delta_i$ on each component and lift it to an ambient holomorphic function. A lift may vanish identically on another component. Correct it by adding a holomorphic function vanishing on $X_i$ but nonzero on every other component, times a suitable constant. To construct that function, for each $X_j\ne X_i$ choose an equation vanishing on $X_i$ but not identically on $X_j$. A generic linear combination of these finitely many equations is nonzero on every such $X_j$: the coefficients causing identical vanishing on any fixed component form a proper linear subspace. For any fixed other component at most one constant causes identical cancellation with the lifted denominator, so finitely many constants are excluded. The corrected lift remains unchanged on $X_i$ and is nonzero on every component.

Let $\delta$ be the product of the corrected lifts. It is a denominator on every component and a nonzero divisor on $X$. Choose $v_i$ vanishing on all $X_j$ with $j\ne i$ and nonzero on $X_i$. Here a product of equations separating each other component from $X_i$ works, since every factor is nonzero on $X_i$. Put

\[
h=\delta\sum_i v_i.
\tag{NFA4}
\]

On $X_i$ it is $\delta v_i$, so $h$ is a nonzero divisor. A weakly holomorphic $f$ restricts to a weakly holomorphic function on each $X_i$: extend across the intersections on the component's regular locus using bounded removal. The germ $\delta f$ on $X_i$ has an ambient holomorphic lift $g_i$. Then $hf$ agrees, on every component, with the ambient holomorphic germ $\sum_i v_i g_i$. Reducedness identifies these componentwise equal germs. Thus, throughout a smaller representative,

\[
h_y B_y\subset\mathcal O_{X,y}.
\tag{NFA5}
\]

No global extension of $f$ and no single sheet labelling are assumed. In particular $B_{x}$ embeds in the total quotient ring of the reduced local ring.

### Weak holomorphic functions and integral closure

For an irreducible germ put $A=\mathcal O_{X,x}$ and $K=\operatorname{Frac}(A)$. A fraction $f=g/h$ integral over $A$ satisfies a monic equation with holomorphic coefficients on a representative. Those coefficients are bounded on a smaller neighbourhood. If $M$ bounds their absolute values, every root of the monic equation has absolute value at most $1+M$: for $|f|>1+M$ the leading term exceeds the sum of the lower terms, using the geometric-series bound. On the regular locus away from $h=0$, $f$ is holomorphic and bounded. Manifold bounded removal extends it over the remaining regular points. The resulting function is weakly holomorphic.

Conversely, take $f\in B_x$ and use a finite projection of this germ. The elementary symmetric functions of its $r$ sheet values are holomorphic off the exceptional base set, invariant under sheet permutations and bounded. They extend on the base. Their monic equation pulls back to an integral equation over $A$. NFA5 already identifies $f$ with a fraction. Hence

\[
B_x=\overline A^{\,K}.
\tag{NFA6}
\]

For a reducible germ the weak ring is the finite product of the component weak rings; the total quotient ring is the corresponding product of fraction fields. The latter assertion can be seen using the component separators: $v_i/(\sum_j v_j)$ is the component idempotent in $Q(A)$, and their finite sum is $1$. Fractions on one component can be assembled in $Q(A)$ by these idempotents; to lift a component denominator, add separators on the other components so that it is nonzero on all of them. Componentwise monic equations can be lifted to $A$ and multiplied to give one monic equation. Thus the weak ring is also the integral closure in $Q(A)$ in the reducible case.

For an irreducible germ each weakly holomorphic $f$ has one limit at $x$. Choose nested neighbourhoods with connected regular locus, inside a representative on which $f$ is bounded. The closures of their $f$-images are nonempty compact connected subsets of one compact disc. Their decreasing intersection is the cluster set at $x$. The integral equation puts that cluster set inside a finite root set obtained by evaluating the coefficients at $x$. A nonempty connected finite set is a singleton. Compactness also shows that a singleton cluster set implies the ordinary limit. The closures in this argument are required; an intersection of unclosed images is not the compact cluster set.

### Normality is open, with an explicit coherent detector

Say a reduced space is normal at $x$ when its germ is irreducible and $B_x=A_x$. The irreducibility requirement also follows from $B_x=A_x$: if there were several local components, their characteristic idempotents are bounded and holomorphic on the regular locus, so belong to $B_{x}$, whereas a local ring has no nontrivial idempotent. Smooth points are normal directly from the weak-holomorphic definition.

Use a universal denominator $h$, the reduced coherent ideal $I$ of $\{h=0\}$, and the coherent sheaf

\[
\mathcal F=\operatorname{Hom}_{\mathcal O_X}(I,I).
\tag{NFA7}
\]

Every endomorphism $\varphi$ of $I$ is multiplication by the fraction $w=\varphi(h)/h$. Indeed, for $a\in I$, $h\varphi(a)=\varphi(ha)=a\varphi(h)$. Since $h$ is a nonzero divisor, this identity identifies $\varphi(a)=wa$ in the total quotient ring. Conversely every fraction preserving $I$ gives such an endomorphism. The inclusion $\mathcal O_X\subset\mathcal F$ is injective because $I$ contains $h$. NFA1 and NFA6 give $\mathcal F\subset B$ stalkwise.

At a stalk with $B=A$, therefore $\mathcal F=A$. At a stalk with $B\ne A$, there is a smallest $k\ge1$ with $I^kB\subset A$: the Nullstellensatz and finite generation give $I^l\subset hA$ for some $l$, and NFA5 gives the required inclusion. Explicitly, if $I$ is generated by $u_1,\ldots,u_t$ with $u_i^{n_i}\in hA$, every monomial of degree $1+\sum_i(n_i-1)$ contains one of those powers. Choose $w\in I^{k-1}B$ outside $A$. Then $wI\subset A$. For each $a\in I$, $wa$ is holomorphic and vanishes on $\{h=0\}$. This follows by taking regular points tending to every point of that set: $w$ is locally bounded there and $a$ tends to zero. Reduced analytic Nullstellensatz gives $wa\in I$. Thus $w$ belongs to $\mathcal F$ but not $A$.

Consequently the non-normal set is exactly $\operatorname{Supp}(\mathcal F/\mathcal O_X)$. Here is the finite-presentation support check. A finite local module $M$ with $M=\mathfrak mM$ vanishes: write its generators as linear combinations of themselves with coefficients in the maximal ideal $\mathfrak m$; the adjugate matrix makes the unit $\det(1-C)$ kill every generator. For a coherent presentation $\mathcal O_X^a\longrightarrow\mathcal O_X^b\longrightarrow\mathcal F/\mathcal O_X\longrightarrow0$, the quotient stalk is zero exactly when the matrix is surjective modulo the maximal ideal, by this elementary Nakayama argument. Equivalently some $b\times b$ minor is a unit; if $a<b$ no such minor exists and the quotient is nonzero. Thus its support is the common zero set of those finitely many minors, with the usual empty support for $b=0$. It is analytic. The normal locus is open. This proof does not assume that $B$ is already a coherent sheaf.

### The generator criterion for a regular point

Let $X\subset\mathbb C^m$ be reduced of dimension $n$ at $a$, and suppose its maximal ideal has $s$ generators $g_1,\ldots,g_s$. Centre ambient coordinates at $a$ and lift the generators holomorphically. Since every ambient coordinate belongs to the maximal ideal, write

\[
z_i=\sum_{j=1}^{s}c_{ij}g_j+f_i,\qquad f_i\in I_X.
\tag{NFA8}
\]

For a generating list with at least ambient size, the ambient dimension bound gives the required inequality. In the equality case, all three dimensions equal the ambient dimension and the ambient chart is the required containing manifold. For a smaller list, differentiation shows that at least $m-s$ of the $df_i(a)$ are independent. The implicit function theorem gives a smooth $s$-dimensional ambient germ containing $X$, so $s\ge n$. When $s=n$, a proper analytic subset of that smooth germ has smaller dimension; hence the reduced germ $X$ equals the smooth germ and is regular. At a regular point, the $n$ local coordinates generate the maximal ideal, by the convergent Taylor expansion.

If a reduced smooth $(n-1)$-dimensional $\Sigma\subset X$ has principal ideal at $a$, its $n-1$ coordinate generators, lifted to $\mathcal O_{X,a}$, together with that one ideal generator generate the maximal ideal of $X$. NFA8 makes $X$ regular. Therefore at a singular point on such a smooth divisor the ideal of the divisor needs at least two generators. This proves the particular generator bound used next.

### A normal space has no singular divisor

By normality openness, work near a normal point with $X$ normal and locally irreducible of dimension $n$. If the singular set has a codimension-one component, select a smooth point $a$ on it, outside intersections with the other singular components. Near $a$ call that smooth divisor $\Sigma$.

Choose finitely many nonzero generators of $I_\Sigma$ on a neighbourhood. Every generator's nonempty zero set is pure of dimension $n-1$ and contains $\Sigma$. Avoid the intersections of $\Sigma$ with its other zero components. There are finitely many such exclusions near a fixed representative, each proper in $\Sigma$. At a remaining point, shrink so that the zero set of every generator is exactly $\Sigma$. Put $A=\mathcal O_{X,a}$ and select a minimal subset $g_1,\ldots,g_l$ generating that ideal. NFA8 gives $l\ge2$, so $f=g_2/g_1$ is not holomorphic: otherwise $g_2$ could be removed from that minimal subset. It is holomorphic and nonzero off $\Sigma$.

Choose regular points outside $\Sigma$ tending to $a$. Along a subsequence either $f$ or its reciprocal has absolute value at most $1$. Interchange $g_1$ and $g_2$ if necessary. Now $f$ is bounded on that sequence. This is a sequence bound, not a claim that $f$ is bounded on a whole punctured neighbourhood.

Because $\sqrt{g_1A}=I_\Sigma$, the Nullstellensatz and finite generation put a power of $I_\Sigma$ inside $g_1A$. Thus there is a least integer $k\ge1$ with $fI_\Sigma^k\subset A$. Some degree $k-1$ generator monomial $g^\alpha$ has $w=fg^\alpha$ outside $A$, whereas

\[
w g_j\in A\quad(1\leq j\leq l).
\tag{NFA9}
\]

Each $wg_j$ is nonzero, has no zero off $\Sigma$, and vanishes at $a$: on the chosen sequence $f$ is bounded and $g^\alpha g_j$ tends to zero. Its zero germ is a nonempty pure hypersurface contained in the smooth irreducible divisor $\Sigma$, so it equals $\Sigma$ as a germ. Therefore $wg_j\in I_\Sigma$ for every $j$. It follows that $wI_\Sigma\subset I_\Sigma$. NFA1 makes $w$ integral over $A$, and NFA6 plus normality gives $w\in A$, a contradiction.

The singular set therefore has codimension at least two. A normal curve is regular, since a nonempty singular set on a pure curve would have codimension one. The converse follows from normality of smooth points. Reduced zero-dimensional normal germs are regular isolated points. This argument retains every singular component; it does not treat generic regularity as regularity at all points.

For the separate normal-space codimension-two extension used by CWS, retain manifold Hartogs across a codimension-two analytic subset and the analytic bounded-extension theorem Demailly II.6.1. A function on $X$ minus a codimension-two analytic set first extends on $X_{\mathrm{reg}}$ by manifold Hartogs. The result is locally bounded near $X_{\mathrm{sing}}$ by II.6.1, because $X_{\mathrm{sing}}$ now has codimension at least two. It is therefore weakly holomorphic and extends by normality. The preceding holomorphic extension proof supplies these two extension inputs directly at its stated compatible finite-projection, analytic-dimension and elementary Cauchy floor.

### Finite normalization constructed from the weak ring

Suppose first that $(X,x)$ is irreducible. Put $A_x=\mathcal O_{X,x}$. Multiplication by $h$ and the inclusion $hB_x\subset A_x$ identify $B_x$ with an $A_x$-submodule of $A_x$. Noetherianity makes it a finite module. Choose module generators $f_1,\ldots,f_r$, adjoining $1$ if needed. Represent them weakly holomorphically on a neighbourhood; write $f_j=g_j/h$ with one common nonzero denominator and choose integral equations for them by NFA6. Multiply $h$ by a function vanishing on $X_{\mathrm{sing}}$ and nonzero on $X$, if necessary, so that $X'=X\setminus\{h=0\}$ is regular. This keeps the denominator property.

In an ambient neighbourhood $\Omega$ form

\[
Z=\{(z,w)\in X\times\mathbb C^r:h(z)w_j=g_j(z)\text{ for all }j\},
\qquad Y=\overline{\{(z,f_1(z),\ldots,f_r(z)):z\in X'\}}.
\tag{NFA10}
\]

Give $Y$ its reduced structure. It is analytic: $Z$ is analytic, and its part with $h\ne0$ is precisely the displayed graph. In a locally finite irreducible decomposition of $Z$, its closure is the union of the components not contained in $\{h=0\}$. This uses analytic component decomposition and density of the complement of a proper zero set, not a resolution theorem.

Each monic equation for $f_j$ holds on $Y$ by closure. Above a fixed $z$ the coordinate $w_j$ belongs to a finite root set, so the projection $\nu:Y\longrightarrow X$ has finite fibres. Above any compact target set the root bound puts all $w$-coordinates in a fixed compact ball; $Y$ is closed in the ambient product over that target neighbourhood. Thus $\nu$ is proper. Its image is closed and contains the dense set $X'$, so it is surjective.

Every $f_j$ is holomorphic on $X_{\mathrm{reg}}$; its graph over each such point lies in $Y$ and is the only point above it, by holomorphic continuity. Hence $\nu$ is an analytic isomorphism over $X_{\mathrm{reg}}$, with inverse $F(z)=(z,f_1(z),\ldots,f_r(z))$. That inverse image is dense in $Y$, since the original graph over $X'$ was dense. The limit result after NFA6 gives a unique point $y$ above $x$.

Take any weakly holomorphic germ $u$ on $(Y,y)$, bounded on a sufficiently small representative. Properness of $\nu$ puts $\nu^{-1}(U)$ inside that representative after shrinking the target. The pullback $u\circ F$ is bounded and holomorphic on $X_{\mathrm{reg}}\cap U$, so is in $B_x$. Because the $f_j$ are module generators,

\[
u\circ F=\sum_j a_j f_j,\qquad a_j\in A_x.
\tag{NFA11}
\]

Lift the $a_j$ to ambient holomorphic functions. Then $Q(z,w)=\sum_j a_j(z)w_j$ is holomorphic on $Y$ near $y$. It agrees with $u$ on the dense graph over $X_{\mathrm{reg}}$, and therefore on $Y_{\mathrm{reg}}$ by the identity principle and density. Thus every weak germ on $Y$ is holomorphic at $y$. The idempotent argument after NFA6 shows its germ is irreducible, so $Y$ is normal at $y$. The already proved openness gives a normal neighbourhood of $y$. Properness again shrinks $U$ so that its complete inverse image lies there. This yields a normal source, finite proper map, and dense regular-locus isomorphism.

For a reducible $X$-germ, perform the construction separately on its finitely many irreducible components and take their disjoint union. The map is finite and proper locally, and is an isomorphism over the regular locus of $X$. Every local component is retained. Each source component has a dense graph part over one input component; hence its dimension is the dimension of that input component. In particular a pure $n$-dimensional input has a pure $n$-dimensional normalization.

The module meaning of finiteness is also available, rather than merely a finite point-fibre assertion. At the irreducible marked germ, pullback along $F$ gives an injective map $\mathcal O_{Y,y}\longrightarrow B_x$: a holomorphic germ is bounded near $y$, and properness keeps every lift in that neighbourhood. Density gives injectivity. NFA11 shows that it is surjective, since each linear combination of the $f_{j}$ is the pullback of the corresponding holomorphic linear expression in $w$. Thus $\mathcal O_{Y,y}=B_x$ as finite $A_{x}$-algebras.

More generally, once the source is normal, a weakly holomorphic target germ pulls back on the inverse regular locus to a bounded holomorphic germ near the finite source fibre. Manifold bounded removal on $Y_{\mathrm{reg}}$ and normality extend it uniquely across the inverse singular locus. Conversely, holomorphic source germs give a weakly holomorphic target germ on the regular locus; finitely many bounded source representatives and properness provide its bound. Disjoint source neighbourhoods and properness identify the direct-image stalk with the product of their local rings. Consequently

\[
(\nu_*\mathcal O_Y)_z=B_z
   =\prod_{y\in\nu^{-1}(z)}\mathcal O_{Y,y},
\qquad B_z\text{ is a finite }\mathcal O_{X,z}\text{-module}.
\tag{NFA12}
\]

The final finiteness uses the universal denominator at $z$ and Noetherianity, as above. This supplies the local module assertion consumed by the fibre-normalization algebra. It does not claim a general coherence theorem for arbitrary proper direct images.

### Uniqueness and gluing, without conflating branches

Let $\nu_j:Y_j\longrightarrow X$ be two finite proper normalizations with dense inverse regular loci. They have a unique isomorphism there. Near a point $a\in Y_1$, the finite fibre of $Y_2$ over $\nu_1(a)$ lies in finitely many disjoint small analytic charts with compact closures in larger charts. Properness restricts the inverse image of a target neighbourhood to their union.

Embed those charts in a common finite-dimensional affine space, with an extra distinct constant label for each chart. The isomorphism on the inverse regular loci has bounded holomorphic coordinate functions and bounded, locally constant labels. First use manifold bounded removal on the regular locus of $Y_1$, then normality to extend every coordinate over a neighbourhood of $a$.

The label satisfies the polynomial whose roots are its finitely many original distinct values; density gives the same polynomial identity after extension. Continuity makes it one constant label near $a$. The coordinate equations of the corresponding analytic chart vanish on the dense old domain and hence on the extension. Compact inner-chart closure lies inside its larger chart, so the extended values lie in $Y_2$. This extends the map holomorphically. The reverse map extends in the same way. Density makes both compositions the identity and makes the extension unique.

The uniquely extended maps satisfy

\[
\nu_1=\nu_2\circ\phi.
\tag{NFA13}
\]

Their uniqueness gives the cocycle identities on overlaps, so the local normalizations glue. The source is Hausdorff: distinct images are separated on the target, while two points over the same image both lie in the complete inverse image of one local target patch and are separated in that Hausdorff local normalization. The source is normal and the map is locally finite proper. For global properness, cover a compact target set by finitely many smaller neighbourhoods whose compact closures lie in the local proper-map target neighbourhoods. Their intersections with the compact target set have compact preimages under the local maps and cover the full inverse image. Thus the glued map is proper. No common branch label is forced across a component intersection.

### What has and has not been discharged

At the stated lower floor this proves the universal denominator, the weak/integral-closure identification, unique limits on irreducible germs, openness of normality, normal singular codimension, regularity of normal curves, finite normalization and its uniqueness. The codimension-two extension has its additional named Hartogs/bounded-extension floor.

It supplies the high-level normal facts used by the preceding marked-family and contact arguments, relative to more elementary finite-projection, coherence, reduced-ideal/Nullstellensatz, regular-locus and manifold-extension inputs. The preceding local algebra proof supplies preparation, division, Noetherianity, unique factorization and integral closure at its named complex-calculus floor. The Oka proof supplies uniform manifold relations and finite coherent-module operations. The analytic local geometry proof supplies reduced vanishing-ideal coherence/Nullstellensatz, compatible finite projection and regular-locus topology at its stated lower inputs. The preceding finite/proper image and rank theorems retain their separately stated hypotheses. Properness of the newly constructed normalization was proved from the monic root bounds; properness alone was never used to assert finiteness.

The exact analytic antecedents are Demailly [II.4.32–4.33, p.101](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=101), [II.7.1–7.5, pp.110–113](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=110), and [II.7.6–7.12, pp.113–115](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=113). The algebraic determinant/integrality antecedents are the Stacks Project [05BT](https://stacks.math.columbia.edu/tag/05BT), [052I](https://stacks.math.columbia.edu/tag/052I), and [00GK](https://stacks.math.columbia.edu/tag/00GK). The reconstruction is independently written; source prose and media are not adapted or reproduced. It makes no original research claim.

Finite projection, coherent analytic algebra, reduced ideals/Nullstellensatz, regular-locus topology, ordinary analytic dimension and implicit-function facts remain exact lower prerequisites. Noetherian local rings, their quotients and the finite-submodule input are supplied by the preceding local algebra proof, relative to its named complex-calculus floor. The preceding extension proof supplies bounded manifold removal, analytic Hartogs, singular-space boundedness and principal zero-set purity at its stated lower inputs. Codimension-two extension therefore has that explicit reconstructed extension floor. These arguments reduce normality and normalization to the stated local analytic and algebraic results.

<a id="SH02-FAG-MARKED-NORMALIZATION"></a>

## Generic marked curve normalization from finite normalization

We supply the generic branch normalization needed by the parameter estimate, using the [normal analytic construction](#SH02-FAG-NORMAL-ANALYTIC-FOUNDATIONS) at its explicit finite-projection, coherent ideal, regular-locus and manifold-removal floor. The actual total critical-curve family is constructed in the next section. Neither the full simultaneous-normalization criterion nor unrestricted fibre-algebra base change is imported.

### Exact statement

Let $Q$ be a connected smooth complex parameter domain of dimension $q$. Let $\Gamma$ be a reduced complex analytic space, pure of dimension $q+1$, equipped near a marked section with holomorphic maps

\[
\pi:\Gamma\longrightarrow Q,\qquad
\sigma:Q\longrightarrow\Gamma,\qquad
\pi\sigma=\operatorname{id}_Q.
\tag{GNM1}
\]

The statement is local along $\sigma(Q)$. Retain the following normal analytic facts: $\Gamma$ has a finite normalization $\nu:\overline\Gamma\to\Gamma$; $\overline\Gamma$ is normal, pure of dimension $q+1$, and $\nu$ is an isomorphism over $\Gamma_{\mathrm{reg}}$ with dense inverse image of that regular set. A normal space has singular locus of codimension at least two. Reduced analytic subsets have locally finite irreducible decomposition, analytic singular and rank-drop sets, coherent local defining ideals, and the reduced analytic Nullstellensatz. Finite maps are proper, have closed analytic images and preserve dimensions of components; finite full-rank maps between smooth spaces of equal dimension are local biholomorphisms. The holomorphic submersion theorem is available.

After restricting generically and shrinking locally near a selected parameter, the following hold near the marked fibre:

1. $\overline\pi=\pi\nu$ is smooth of relative dimension one.
2. The reduced marked inverse image $M=(\nu^{-1}\sigma(Q))_{\mathrm{red}}$ is a finite disjoint union of local sections of $\overline\pi$.
3. Finitely many product charts (t,s) about those sections have $t=0$ on the sections and cover every point of every actual nearby fibre germ under $\nu$.
4. For every parameter in a further smaller neighbourhood, the finite map from the smooth fibre of $\overline\Gamma$ to $(\Gamma_s)_{\mathrm{red}}$ is its normalization. Each branch is nonconstant, and no branch or marked preimage is omitted.

The conclusion concerns reduced actual fibre germs. No flatness hypothesis or equality with an unreduced scheme-theoretic fibre ring is asserted. The generic restrictions are local; no global trivialization of the marked finite cover or global single analytic equation for all bad parameters is claimed.

### Remove bad points on the marked inverse image

Because $\nu$ is finite and $\sigma(Q)$ is a closed section locally, the restriction

\[
\rho:M\longrightarrow Q
\tag{GNM2}
\]

is finite and surjective. All its irreducible components have dimension at most $q$. Remove the finite analytic images of components whose images are proper subsets of $Q$. Every remaining component has dimension $q$ and dominates $Q$.

The intersection of $M$ with the singular locus of $\overline\Gamma$ has dimension at most $q-1$: the whole ambient singular locus has that bound because $\overline\Gamma$ is normal and has dimension $q+1$. Its image under the finite map $\rho$ is therefore proper analytic. Remove it too. For $q=0$ the ambient normal curve has no singular points, so this set is empty.

On the dominating $q$-dimensional components of $M$, mark their singular loci, their mutual intersections and their rank-drop loci for $\rho$. The singular/intersection subsets are proper and have dimension at most $q-1$. The finite-map generic rank lemma makes the rank-drop set proper as well; stacked minors give its analytic equations. Their finite images are again proper analytic in $Q$. After these removals,

\[
M\subset\overline\Gamma_{\mathrm{reg}},\qquad
M\text{ is smooth of dimension }q,\qquad
d\rho:T_mM\overset{\sim}{\longrightarrow}T_sQ.
\tag{GNM3}
\]

The finite full-rank map splits into finitely many local biholomorphisms after shrinking near any chosen remaining parameter. This only uses a local parameter neighbourhood; a finite cover can have monodromy on a larger domain.

### Relative smoothness and actual coverage

At a point m of $M$, the restriction of $d\overline\pi$ to $T_mM$ is the isomorphism $d\rho$. Hence $d\overline\pi$ has rank $q$. Since $\overline\Gamma$ is smooth of dimension $q+1$ at m, the holomorphic submersion theorem supplies coordinates in which

\[
\overline\pi(t,s)=s,\qquad M=\{t=0\}.
\tag{GNM4}
\]

To obtain $t=0$ on $M$, subtract from a relative coordinate the holomorphic value of that coordinate on the local section. The finitely many marked preimages over the selected parameter lie in disjoint such product charts, with a common smaller parameter neighbourhood. Their relative dimension is one precisely because the total dimension is $q+1$.

The complement of the chart union is closed in a suitable representative of $\overline\Gamma$ and does not meet the finite inverse image of the selected marked point. A proper map is closed, so its image under $\nu$ misses an open neighbourhood of that marked point. Restrict $\Gamma$ to that neighbourhood and shrink $Q$. Then

\[
\nu^{-1}(U)\subset\bigcup_{\lambda}W_\lambda,
\qquad W_\lambda\cong\Delta_\lambda\times Q,
\tag{GNM5}
\]

with each $W_\lambda$ contained in the relative smooth locus. Thus all points of the actual nearby fibre germs lift into the listed charts. Properness is used for the complement; it is not inferred from $\pi$ being proper, which is not assumed. The charts need only cover a neighbourhood of the marked fibre, not the entire global family.

Every chart fibre has dimension one. A constant fibre-curve map under $\nu$ would give an infinite point fibre of a finite map. It is therefore nonconstant. Its image is a curve. Surjectivity and GNM5 show that $(\Gamma_s)_{\mathrm{red}}$ near the marked point is pure of dimension one; an isolated additional component could not be covered by these finite curve maps.

### Ensure generic birationality on every fibre branch

Let $E=\Gamma_{\mathrm{sing}}$ and $\overline E=\nu^{-1}(E)$. By the normalization property, $\overline E$ is proper analytic on every component of $\overline\Gamma$. In particular, it does not contain a whole open chart $W_\lambda$. Choose a local analytic equation for $E$ whose pullback to $W_\lambda$ is a nonzero holomorphic function $f_\lambda(t,s)$. Such an equation exists because the ideal of $E$ has local generators and its pullback is not identically zero on that chart. Shrinking makes the chosen equation defined on the required representative. If the chart misses $\overline E$ entirely, one may instead take $f_\lambda=1$.

Expand on the product chart:

\[
f_\lambda(t,s)=\sum_{j\geq0}c_{\lambda j}(s)t^j,
\qquad
\text{some }c_{\lambda j}\text{ is not identically zero.}
\tag{GNM6}
\]

For each of the finitely many charts, select one coefficient not identically zero and discard its zero set in the connected local parameter domain. The finite union of these proper analytic subsets has dense open complement. Near any selected remaining parameter, those coefficients remain nonzero. Thus $f_\lambda(\cdot,s)$ is not identically zero on any chart fibre. Its zeros on that disc are discrete. Consequently every normalized fibre branch has a dense open part outside $\overline E$.

The map $\nu$ is an analytic isomorphism over $\Gamma\setminus E$; therefore its base change is an isomorphism on those dense fibre parts. Finiteness of $\nu$ also survives fibre restriction. The smooth fibre source is reduced, so this map factors through the reduction of $\Gamma_s$. The resulting map is finite, surjective and generically one-to-one on every branch. Two distinct source branches cannot have the same target component: their dense open images would overlap outside $E$, contradicting the isomorphism there.

For clarity, the local algebra characterization supplies the final normalization assertion. At a target point, let $A$ be its reduced curve ring and let $B$ be the product of the source curve local rings at its finitely many preimages. The reduced Nullstellensatz and surjectivity give an injection $A\to B$. The dense branchwise isomorphism identifies their total quotient rings; write $Q(A)$ for that ring. $B$ is finite over $A$ and is integrally closed there because its factors are smooth curve rings. Hence

\[
B=\overline A^{\,Q(A)}.
\tag{GNM7}
\]

Indeed, elements of $B$ are integral over $A$ by finiteness. Conversely, an element of the common total quotient ring integral over $A$ is integral over $B$ as well, since the same monic polynomial has its coefficients in $B$; integral closedness puts it in $B$. This also shows that the map is an isomorphism over every regular point of the reduced target curve, including any such point lying in the singular locus of the total space. Thus the restricted map is the normalization of the actual reduced fibre, not merely a finite parametrization of an unspecified subset. □

### Exact limits and a marked-cover countercheck

The generic restriction cannot be dropped from the fixed marked-chart assertion. Consider the reduced total family

\[
\Gamma=\{z^2=x^2(x+s)\},\qquad
\nu(t,s)=(x=t^2-s,\ z=t(t^2-s),\ s),\qquad
\sigma(s)=(0,0,s).
\tag{GNM8}
\]

The map is finite because $t$ satisfies $t^2=x+s$. It is birational because $t=z/x$ off $x=0$, and the smooth source is its normalization. At the total-space germ $(0,0,0)$, the function $x+s$ has an odd-order divisor, so $z^2-x^2(x+s)$ is irreducible. The marked inverse image is

\[
M=\{t^2=s\},\qquad \rho(t)=t^2.
\tag{GNM9}
\]

At $s=0$ its fibre is one point; at $s\ne0$ it has two. It cannot be a disjoint fixed collection of origin-centred product sections across zero. The rank-drop locus of $\rho$ is exactly the excluded marked point. On a small neighbourhood of any fixed nonzero s, the two sections are holomorphic and the proof applies. This example checks the marked-cover generic restriction; it does not assert failure of fibre normalization at $s=0$, where the map $t\mapsto(t^2,t^3)$ still normalizes the cusp.

Purity of the total dimension is also essential for the relative-dimension-one conclusion: the smooth product $\mathbb C^2\times Q$ with its zero section satisfies finite identity normalization and full parameter rank but has two-dimensional fibres. A whole normal space is not automatically a family of curves.

### Exact source floor and application obligation

The analytic antecedents are Demailly II.7.6, p.113, for singular codimension in a normal space; II.7.7 for normal curves; and II.7.9–7.12, pp.114–115, for finite normalization, its regular-locus isomorphism and its uniqueness/construction. The preceding normal analytic construction supplies the universal denominator, integral-closure identification, normality openness, singular codimension and finite normalization with its module meaning. The preceding local algebra proof supplies its Noetherian ring and finite-submodule layer. Its finite-projection, coherent-ideal, reduced-Nullstellensatz, regular-locus and extension foundations retain their separately stated analytic hypotheses.

This proof uses the ordinary singular locus as $E$; it needs no separate relative conductor bound, δ-constant theorem, local Bertini theorem, relative Grassmannian construction, equisaturation theorem or generic-flatness theorem for the stated reduced-fibre conclusion. It makes no assertion about the full unreduced fibre algebra, arbitrary base change or all exceptional parameters.

The following conormal-incidence construction supplies the actual total-family hypothesis and fixed-fibre regular density required for this application. The normality and finite-normalization layer is supplied above relative to the stated lower analytic inputs; the preceding finite/proper rank and image proofs supply the distinct remaining analytic inputs at their stated scopes.

<a id="SH02-FAG-ACTUAL-CRITICAL-FAMILY"></a>

## The actual critical-curve family from universal conormal incidence

We now construct the actual family used in the marked-normalization lemma. The conclusion is relative to Whitney (a) and the same normal/finite analytic floor as the contact proof.

### Universal incidence and its dimensions

Take the curve-lower-stratum case of CSB: $H\subset\mathbb C^N$ is reduced, pure of dimension $d\geq2$; $Y\subset H$ is closed, smooth of dimension one; $N\geq d+2$; and the pair is Whitney (a,b) at $0$. Let $C=C(H)$ be the actual projectivized conormal space. It is pure of dimension $N-1$. Let $V$ be its conormal-bundle graph over $H_{\mathrm{reg}}\setminus Y$, and put $Z=C\setminus V$. This graph is dense on every component, so $Z$ is analytic of dimension at most $N-2$. The conormal projection $\kappa:C\to H$ is proper.

Choose fixed linear ambient coordinates in which $T_0Y$ is the first coordinate line. On the full-rank projection chart use the independent parameters $s=(a,b)$ and set

\[
p_s(z)=\left(z_1+\sum_{k=3}^N a_kz_k,
z_2+\sum_{k=3}^N b_kz_k\right),
\qquad q=2N-4.
\tag{CFI1}
\]

Let $Q$ be a connected small open parameter domain. The universal incidence is the closed analytic subset

\[
\mathcal R=\{(x,[\xi],s)\in C\times Q:
\xi_k=a_k\xi_1+b_k\xi_2\ (3\leq k\leq N)\}.
\tag{CFI2}
\]

The equations are homogeneous in $\xi$, so are well defined on the projective covector factor. There is no incidence point with $\xi_1=\xi_2=0$: those equations would force every $\xi_k=0$. On $\xi_1\ne0$ solve them for the $N-2$ parameters $a_k$ and keep $b$ free. On $\xi_2\ne0$ solve them for $b$ and keep $a$ free. Locally, the incidence is an open subset of a product of $C$ with $N-2$ free parameters. The map to the conormal coordinate is locally open, and inverse image of the dense graph $V$ is dense. In particular,

\[
\dim\mathcal R=(N-1)+(N-2)=q+1\quad\text{pure},
\qquad
\dim\mathcal Z\leq(N-2)+(N-2)=q,
\quad\mathcal Z=\mathcal R\cap(Z\times Q).
\tag{CFI3}
\]

These are total-family assertions proved by solving the incidence equations. No flatness or generic-fibre theorem is used to infer them. Restricting to an open parameter domain or a smaller representative preserves the purity of any nonempty remaining components.

### Properness becomes finite near the marked fibre

The projection

\[
\phi:\mathcal R\longrightarrow H\times Q,
\qquad (x,[\xi],s)\longmapsto(x,s)
\tag{CFI4}
\]

is proper: it is the restriction of the base change $\kappa\times\operatorname{id}_Q$ to a closed incidence subset. Whitney (a) gives $C_0\subset\mathbb P((T_0Y)^\perp)$, so $\xi_1=0$ on every covector in $C_0$. On the projection line specified by CFI2, an element with $\xi_1=0$ is the single projective point $[0:1:b_3:\cdots:b_N]$. Thus the point fibre of $\phi$ over $(0,s)$ has at most one point, for every $s$ in this chart. In particular, choose $s_0$ with this finite point fibre.

The proper-map fibre-dimension upper-semicontinuity fact already proved in FJ supplies an open target neighbourhood on which the fibres are zero-dimensional or empty. Proper compact analytic zero-dimensional fibres are finite. Choose a product neighbourhood $U\times Q'$ of (0,$s_0$) inside it, with $Q'$ connected. Then the restriction of $\phi$ is proper and finite. No properness of $H$→$Q$ or of a global curve-family projection is assumed. If the incidence is empty over a neighbourhood, the critical family is empty and the union with $Y$ is just the smooth product $Y\times Q'$.

For the nonempty restriction, define the reduced finite images

\[
\Gamma_P=\phi(\mathcal R)_{\mathrm{red}},
\qquad B=\phi(\mathcal Z)_{\mathrm{red}},
\qquad
\Gamma=(\Gamma_P\cup(Y\times Q'))_{\mathrm{red}}.
\tag{CFI5}
\]

Finite proper image analyticity and dimension preservation show that $\Gamma_P$ is pure of dimension $q+1$ and that $B$ is analytic of dimension at most $q$. Union with the smooth product $Y\times Q'$ therefore makes $\Gamma$ reduced and pure of dimension $q+1$. It has the marked section $\sigma(s)=(0,s)$, provided by $Y\times Q'$. The images of finite local components have the same dimension; a proper containment between distinct such maximal images would contradict that dimension, so reduction and component merging do not spoil purity. These facts establish the total-family hypothesis of GNM.

The total family $\Gamma_P$ is the closure of the image of the old regular incidence. This follows from the total density established above and properness/closedness, but total density alone would not imply fixed-fibre density. That additional assertion is proved next.

### Fixed-fibre critical density and actual coverage

Whitney (a) and the nonzero first projection differential on $T_0Y$ imply, after shrinking U and $Q'$, that the first differential is nonzero on every nearby upper regular tangent. The sequence/compact limiting-tangent argument is the same as DPC: any vanishing restriction would limit to a restriction annihilating $T_0Y$, where it is the first coordinate and is nonzero. Therefore the restriction of $p_s$ to each such upper tangent has rank at least one.

A regular-upper point belongs to the image of the incidence precisely when a nonzero covector in the plane spanned by the two projection differentials annihilates its upper tangent. Rank is then at most one and hence exactly one. The conormal point is unique there. Conversely every regular rank-one critical point has exactly that incidence lift. Consequently $\Gamma_P\setminus B$ is exactly an open part of the actual upper regular critical family.

For every $s$, any point of $\Gamma_P$ lying on $Y\times\{s\}$ belongs to $B$: its incidence preimages lie in $Z$, because $V$ excludes $Y$. Hence $\Gamma_P\cap(Y\times Q')\subset B$. Since $\dim B\leq q$, the set $B$ is proper on every $(q+1)$-dimensional total component of $\Gamma$, including the $Y$ product component.

Apply GNM to $\Gamma$ and, in its final coefficient selection, replace the avoided total singular set by

\[
E=\Gamma_{\mathrm{sing}}\cup B.
\tag{CFI6}
\]

This is analytic and proper on every total component. Its pullback to each marked normalized product chart is proper; choose a nonzero local defining function on each chart and exclude one non-identically-zero fibre coefficient, exactly as in GNM6. After the finite generic exclusions, every chart fibre has a dense open part outside the pullback of $E$. The normalization conclusion of GNM is unchanged because the isomorphism outside $\Gamma_{\mathrm{sing}}$ still holds; adding $B$ only strengthens the chosen fibre-density assertion.

On each chart belonging to a critical-family total component, that dense open part maps to upper regular rank-one critical points of the fixed $p_s$. A chart belonging to the $Y$ product gives the lower curve itself. Distinct total components remain distinguished by the normalization; fixed-fibre coincidences cannot merge a critical branch with $Y$, because such a branch would lie entirely in $B$, which the coefficient choice excludes. All actual fibre points are covered by the finite normalized charts as in GNM5.

It follows that the reduced fibre of $\Gamma$ is exactly the union of $Y$ with the reduced closure $P(p_s)$ of the actual upper regular critical locus, as curve germs near the marked origin. Every non-$Y$ branch has the required regular-upper density. Any isolated point of $\Gamma_P$ on $Y$ is already included in that union; an isolated component away from $Y$ is impossible because GNM supplies pure one-dimensional fibres there. Also, $B$ meets each chart fibre only in a discrete subset. Thus $P(p_s)\cap Y$ is discrete and, as a germ at the marked point, is contained in {0}. There is no omitted branch, hidden bad-locus curve or unspecified image family.

The ambient branch maps $Z_\lambda(t,s)$ are the finite total normalization maps followed by the actual embedding in $H\times Q'$. They are holomorphic, nonconstant on the fibres, satisfy $Z_\lambda(0,s)=0$, and have the full parameter neighbourhood needed for DPC's differentiation while $H$ and $Y$ remain fixed. The input needed by DPC is therefore supplied at the normal/finite analytic floor by CFI and GNM.

### Remaining scope

This route does not import Teissier's complete δ-constant simultaneous-normalization criterion, a relative conductor theorem, generic flatness, a relative Grassmannian argument, equisaturation or saturated-algebra stability for this application. Their source arguments remain separately preserved and are not declared proved. It does use finite normalization and normal singular codimension, the proper finite-map fibre-dimension fact, analytic ideals/Nullstellensatz, finite image/dimension results, and the holomorphic submersion theorem. The preceding normal analytic proof supplies the normalization and singular-codimension layer at its exact lower inputs. The preceding finite-projection, coherent/reduced-ideal, manifold-extension, finite/proper rank and image, and holomorphic-submersion proofs supply the remaining inputs.

There is no generic ring-base-change assertion for unreduced fibres. No resolution, curve selection, pre-existing Whitney stratification or upper polar-equimultiplicity theorem is invoked. The CSB first-bound section and CHN induction use this family and the DPC chord estimate at the same analytic hypotheses. These are independently written reconstructions of standard analytic geometry. No source prose or media are adapted or reproduced, and the exposition makes no claim of a new conormal criterion.

The normal analytic antecedents are Demailly [II.7.6–7.7, p.113](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=113), and [II.7.9–7.12, pp.114–115](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=114). The complete presented arguments at those loci supply the finite normalization and normal singular-codimension floor. Their coherent-ideal, universal-denominator, bounded-extension and finite-projection arguments are the analytic inputs proved in the preceding sections.

<a id="SH02-FAG-DIRECT-PARAMETER-CHORD"></a>

## The parameter estimate directly from branch series

The preceding integral-equation proof isolates the estimate needed from relative saturation. We now prove the particular parameter-derivative estimate directly. This avoids importing the whole saturated-algebra stability theorem or its generic-to-total integral-dependence specialization principle for this application. The preceding marked-normalization and actual-incidence constructions supply the generic simultaneous normalization of the actual curve family at their normal/finite analytic floor.

### The retained normalization input and actual branch coverage

Let $Q$ be a connected smooth parameter neighbourhood for the actual reduced critical-curve union with $Y$. Retain the generic curve-family theorem in the following precise form: after a generic restriction, the finite normalization of the family is smooth of relative dimension one over $Q$, and its fibre maps are the normalizations of the actual reduced fibre curves. The family has its marked section at the origin. The preceding constructions supply this exact input; it is not a consequence of the subsequent derivative estimates.

The marked branch charts then follow at the finite analytic floor already used in this lesson. The reduced inverse image of the marked section under finite normalization is finite over $Q$. Discard its components whose images are proper subsets of $Q$. On each remaining component the finite-map rank lemma gives generic full rank; its singular and rank-drop subsets have proper analytic images. Remove those images. The resulting finite map is locally a disjoint union of biholomorphisms to $Q$, after shrinking near a selected parameter. Each lifted section in the smooth relative curve admits holomorphic coordinates $(t,s)$ with section $t=0$. There are finitely many such charts. Properness of finite normalization, applied to the complement of their union near the finite marked fibre, ensures that their images cover the actual fibre curves after shrinking. Thus no branch or mixed pair is omitted.

The corresponding ambient branch maps $Z_\lambda(t,s)$ are holomorphic and nonconstant on each fibre. For the moving projections, choose a full-rank chart with $s=(a,b)$ and

\[
p_s(Z)=\left(Z_1+\sum_{k=3}^N a_kZ_k,
Z_2+\sum_{k=3}^N b_kZ_k\right),
\qquad Z_\lambda(0,s)=0.
\tag{DPC1}
\]

The first plane differential is nonzero on $T_0Y$. Whitney (a) and compactness of limiting tangent planes imply that it is nonzero on every nearby regular upper tangent, uniformly for parameters in a smaller neighbourhood. Otherwise a sequence of such vanishing restrictions would converge to a restriction vanishing on a limiting plane containing $T_0Y$. On a critical branch the two plane differentials have rank one on that upper tangent.

The plane image cannot collapse identically on a whole branch family. If both plane-coordinate series vanished identically there, differentiate with respect to $b_k$ while holding its original branch coordinate fixed. On the dense regular-upper part the variation of $Z_\lambda$ is tangent to the fixed $H$, and the first plane differential kills it. Rank one and the nonzero first differential imply that the second differential kills it too. Hence

\[
0=\partial_{b_k}(p_s(Z_\lambda))_2=(Z_\lambda)_k
\quad(3\leq k\leq N),
\qquad (Z_\lambda)_1=(Z_\lambda)_2=0.
\tag{DPC2}
\]

Holomorphic continuation gives the identities on the full chart, contradicting nonconstancy of its finite normalization map. The branch $Y$ has nonconstant plane image because its first differential is nonzero. Remove the proper parameter subsets on which a nonzero leading plane coefficient vanishes. Every remaining branch consequently has a nonconstant plane image. This step uses the actual moving family and Whitney (a), rather than a separate polar-transversality theorem.

### Normalize a minimal first coordinate

For each branch let $n_\lambda$ be the least degree at which either plane-coordinate series has a coefficient function not identically zero on $Q$. All lower coefficients vanish identically. After removing a finite union of proper coefficient zero sets, choose a fixed plane linear form nonzero on every degree-$n_\lambda$ coefficient vector and on the image of $T_0Y$. These are finitely many proper linear exclusions. Extend it to an invertible pair of plane coordinates.

The new first branch coordinate is $t^{n_\lambda}U_\lambda(t,s)$ with $U_\lambda(0,s)\ne0$. A holomorphic root of this unit and the parameter-dependent inverse function theorem give a new branch coordinate in which

\[
p_s(Z_\lambda(t,s))=(t^{n_\lambda},v_\lambda(t,s)),
\qquad n_\lambda\geq1,
\qquad \operatorname{ord}_t v_\lambda(\cdot,s)\geq n_\lambda.
\tag{DPC3}
\]

The plane coordinate change is fixed, not parameter-dependent. Applying it also to the first two ambient coordinates transforms the old $(a,b)$ into another independent pair of parameter vectors by a fixed invertible linear map. Recentring at any later selected parameter only changes the first two ambient coordinates by fixed linear combinations of the others. Thus (DPC1) still holds in the new coordinates. Its parameters can again be called $(a,b)$.

For a parameter coordinate $s_j$, put $h_\lambda=\partial_{s_j}v_\lambda$, with the new normalized $t$ fixed. Its order is also at least $n_\lambda$, since all lower coefficient functions vanish identically. On common smaller product neighbourhoods, holomorphic division by $t^{n_\lambda-1}$ gives a uniform constant $M$ with

\[
|\partial_tv_\lambda(t,s)|+
|\partial_th_\lambda(t,s)|
\leq M|t|^{n_\lambda-1}.
\tag{DPC4}
\]

### All equal-first-coordinate pairs

Let $L$ be a common multiple of the finitely many $n_\lambda$. For every ordered pair of branches and every $n_\mu$-th root of unity $\omega$, consider

\[
D_{\lambda\mu\omega}(w,s)=
v_\lambda(w^{L/n_\lambda},s)
-v_\mu(\omega w^{L/n_\mu},s).
\tag{DPC5}
\]

There are finitely many such series. An identically zero series has identically zero parameter derivatives. For any other series, take its least degree $q$ with coefficient function not identically zero, and remove that coefficient's zero set. On a smaller neighbourhood of any remaining parameter, it factors as $w^qU(w,s)$ with a nonvanishing unit. Bounds on this unit and its parameter derivative give

\[
|\partial_{s_j}D_{\lambda\mu\omega}(w,s)|
\leq C|D_{\lambda\mu\omega}(w,s)|.
\tag{DPC6}
\]

All removed sets are proper analytic subsets of a connected smooth parameter domain; their finite union has dense open complement. The constants are uniform on a smaller neighbourhood of the selected parameter. No inference from general-fibre integral dependence to total-family integral dependence is involved.

Every pair with $t^{n_\lambda}=u^{n_\mu}$ is represented in (DPC5). Choose $w$ with $w^{L/n_\lambda}=t$; then $w^L=u^{n_\mu}$, so $u=\omega w^{L/n_\mu}$ for one of the listed roots. This includes the zero pair, different branches, and identical-branch pairs. Consequently (DPC6) bounds the difference of $h$ by the second plane-coordinate difference on every equal-first-coordinate pair.

### A nearest root compares arbitrary pairs

Given arbitrary $t,u$ on branches $\lambda,\mu$, choose a root $e$ of $e^{n_\lambda}=u^{n_\mu}$ closest to $t$. With $n=n_\lambda$ and $R=\max(|t|,|e|)$, there is a constant depending only on $n$ such that

\[
|t-e|R^{n-1}\leq C_n|t^n-e^n|.
\tag{DPC7}
\]

For $R>0$, divide both variables by $R$. On the compact set defined by $\max(|t|,|e|)=1$ and the finitely many closed inequalities saying that $e$ is a closest root, the polynomial

\[
Q_n(t,e)=\sum_{j=0}^{n-1}t^{n-1-j}e^j,
\qquad (t-e)Q_n(t,e)=t^n-e^n
\tag{DPC8}
\]

never vanishes. If $t=e$, it equals $ne^{n-1}\ne0$. If $t\ne e$ and it vanished, $t$ would itself be a different root and would be closer than $e$. Compactness gives a positive minimum for its absolute value. Homogeneity proves (DPC7). For $n=1$ the polynomial is one; for $t=e=0$ the desired estimate is immediate.

Choose a common small first-coordinate disc, so every replacement root lies in the appropriate branch disc. Integrating (DPC4) on the straight segment from $e$ to $t$, whose points have modulus at most $R$, and using (DPC7) yields

\[
|v_\lambda(t,s)-v_\lambda(e,s)|+
|h_\lambda(t,s)-h_\lambda(e,s)|
\leq C'|t^{n_\lambda}-u^{n_\mu}|.
\tag{DPC9}
\]

The pair $(e,u)$ has equal first coordinates, so (DPC6) applies to it. The triangle inequality, followed by (DPC9), therefore proves

\[
|h_\lambda(t,s)-h_\mu(u,s)|
\leq C''\left(
|t^{n_\lambda}-u^{n_\mu}|+
|v_\lambda(t,s)-v_\mu(u,s)|\right).
\tag{DPC10}
\]

All branch pairs, parameter coordinates and roots belong to finite lists, so one constant works on common smaller neighbourhoods. This is the required parameter-derivative estimate, including all mixed and zero pairs.

### Return to the ambient coordinates

For $s_j=b_k$, the intrinsic calculation (PNY7) holds in the normalized chart. At a regular polar point, $\partial_{b_k}Z_\lambda$ is tangent to the fixed $H$. Differentiating its first plane coordinate with the new $t$ fixed gives zero. That differential is nonzero on the upper tangent, and the rank-one condition makes the second differential proportional to it. Thus

\[
\partial_{b_k}v_\lambda
=d(p_s)_2(\partial_{b_k}Z_\lambda)
+(Z_\lambda)_k=(Z_\lambda)_k.
\tag{DPC11}
\]

On $Y$, the variation is tangent to that fixed curve and killed by its nonzero first differential, so the same formula holds. These identities hold on the dense regular part of each branch chart and extend holomorphically over its marked point and the parameter neighbourhood. Holding an old, unnormalized branch coordinate fixed would not justify this calculation.

Apply (DPC10) to every coordinate in (DPC11). The first two original coordinates are obtained from the plane coordinates by subtracting the sums in (DPC1), whose parameter coefficients are bounded. Comparing finite-dimensional norms gives

\[
\|Z_\lambda(t,s)-Z_\mu(u,s)\|
\leq C_0\|p_s(Z_\lambda(t,s))-p_s(Z_\mu(u,s))\|.
\tag{DPC12}
\]

Actual branch coverage makes this an estimate on every pair of points of the actual curve union. It proves the mixed critical-curve/$Y$ chord bound needed in the critical-secant obstruction, and gives injectivity when the plane chord is zero. The direct conormal-slice proof and exceptional-fibre induction can consequently retain only the generic simultaneous curve-normalization and analytic floors at this step. The saturated-curve structure theorem, the full saturated-algebra parameter-stability theorem, generic-to-total integral-dependence specialization and whole fibre-algebra identification are not imported for this direct chord argument.

The generic restriction is essential. In the normalized family

\[
x=t^2,\qquad v=st^3+t^5,\qquad h=\partial_sv=t^3,
\qquad
\left.\frac{|h(t,s)-h(-t,s)|}{|v(t,s)-v(-t,s)|}\right|_{s=0}
=|t|^{-2},
\tag{DPC13}
\]

the first-coordinate difference is zero. At $s=0$ no local constant is possible. Near any fixed nonzero $s$, the relevant contact coefficient is a unit and the proof applies after shrinking. Normalized coordinates alone would therefore be insufficient.

The exact normalization antecedent is Teissier's *Résolution simultanée : I — Familles de courbes*, §1.3.2, [statement and presented proof, pp.2–9](https://www.numdam.org/item/SSS_1976-1977____A9_0.pdf#page=5), in the 1976–1977 seminar version. It treats flat reduced curve fibres over a normal base and the simultaneous-normalization criterion; its proof explicitly uses generic normalization outside a proper parameter subset. *Variétés polaires II*, [V.1.2.2, pp.463–465](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=151), applies that generic family input and contains the moving-projection antecedent. The preceding marked-normalization and conormal-incidence proofs supply the actual generic family input at the common normal/finite analytic floor. They do not import the complete delta-constant criterion, a relative conductor theorem, generic flatness or a relative Grassmannian argument. The finite/coherent normalization, normal singular-codimension, finite/proper analytic, reduced-ideal and submersion results retain their stated hypotheses. The direct coefficient and nearest-root proof uses the preceding normalization theorem with its stated local analytic inputs. It is independently written, with no source prose or media adaptation and no original research claim.

<a id="SH02-FAG-CONORMAL-SLICE-FLOOR"></a>

## The first fibre bound without a multiplicity comparison

There is a second proof of the first ordinary-conormal bound. It uses the already proved critical-secant obstruction and moving-projection calculation, using the exact generic curve family and marked normalization supplied above at the normal/finite analytic floor. The preceding direct branch-series estimate supplies the mixed chord bound without the saturated-algebra stability or generic-to-total integral-dependence specialization theorem. Its conormal section and transverse-slice arguments are supplied below. It requires neither the general-section polar-multiplicity formula nor the all-index polar-section test (PNY9).

Let $H\subset\mathbb C^N$ be reduced and pure of dimension $d$, with $N\geq d+2$. Let $Y\subset H$ be closed and smooth of dimension $t$, and assume $0<t<d$ and Whitney (a,b) at $0$. Put $C=C(H)$ and let $\kappa:C\to H$ be the actual projectivized conormal. The conormal graph over $H_{\mathrm{reg}}\setminus Y$ is dense in $C$. Thus Whitney (a) already gives the weaker bound

\[
C_0\subset\mathbb P((T_0Y)^\perp),
\qquad \dim C_0\leq N-1-t.
\tag{CSB1}
\]

The graph remains dense even if some points of $Y$ are regular in $H$: approximate those points and their bundle covectors by regular points outside the lower-dimensional closed subset $Y$. The bound in (CSB1) is used to prove slice density; the stronger target bound is not assumed.

### A curve lower stratum and actual projective sections

First take $t=1$ and $d\geq2$. Let $V$ be the graph over $H_{\mathrm{reg}}\setminus Y$ and $Z=C\setminus V$. The space $C$ is pure of dimension $N-1$ and $Z$ is analytic of dimension at most $N-2$. In a finite relatively compact chart cover of the compact proper fibre $C_0$, there are only finitely many local components.

Intersect successively with $N-2$ general hyperplanes in the projective covector coordinate. At each step, a hyperplane equation vanishes identically on a selected component only for a proper linear subset of its parameter space: every point has a nonzero projective coordinate. Avoid those finitely many subsets for both the current section and its bad subset. The one-equation theorem makes the final section

\[
R_\Lambda=C\cap(H\times\Lambda),\qquad
\Lambda\simeq\mathbb P^1\subset\mathbb P^{N-1},
\qquad
\dim R_\Lambda=1\ \text{if nonempty},\qquad
\dim(R_\Lambda\cap Z)\leq0.
\tag{CSB2}
\]

All nonempty components are pure of the displayed dimension. Consequently $R_\Lambda$ is the closure of its old regular graph part. Properness allows a base shrinking after the finite choices. This is an actual section-density proof, not an assumption that every central-fibre point is already a regular polar limit.

Write $\Lambda=\mathbb P(p^*((\mathbb C^2)^*))$ for a surjective linear projection $p:\mathbb C^N\to\mathbb C^2$. Also require $p|_{T_0Y}\ne0$ and take $p$ in the generic set of the exact family/normalization floor and the direct branch-series estimate used for (PNY6)–(PNY8). To make the choices compatible, start with a full-rank defining flag in an open parameter domain where that floor holds, and choose a product neighborhood of its hyperplane equations that remains in the domain. Each successive proper linear exclusion can be avoided inside its prescribed factor of that neighborhood. Thus the final projection satisfies both the family floor and the section conditions. Condition (a), compactness of the limiting tangent planes and $p|_{T_0Y}\ne0$ ensure that $p$ has rank at least one on every nearby regular upper tangent. At such a point,

\[
\mathbb P((T_xH)^\perp)\cap\Lambda\ne\varnothing
\quad\Longleftrightarrow\quad
\operatorname{rank}(p|_{T_xH})=1,
\tag{CSB3}
\]

and the intersection is exactly one point. Over the bad locus the section has dimension at most zero. Therefore its proper map to $H$ has finite fibres after shrinking; its image is the reduced closure of the regular critical locus, a pure curve or the empty set. Its intersection with $Y$ is discrete, hence contained in $\{0\}$ as a germ. This proves the section and critical-curve geometry needed here. The preceding universal-incidence and marked-normalization proofs supply the actual simultaneous branch family at the normal/finite analytic floor. Relative saturation is an optional source route, rather than an imported step of the direct derivative estimate.

Suppose $\dim C_0\geq N-2$. Every projective line $\Lambda$ meets $C_0$. One can see this without an algebraic intersection theorem: apply $N-2$ successive hyperplane cuts. Before each cut a positive-dimensional compact projective analytic component remains, by the one-equation lower bound. It must meet that hyperplane, since otherwise it would be a compact analytic subset of an affine space with separating coordinate functions and hence finite.

Take a point of $R_\Lambda$ over $0$. Purity and (CSB2) give regular graph points outside $Y$ approaching it, with base points $x_n\to0$. Their ranks are one by (CSB3). The retained simultaneous family normalization, the actual parameter calculation (PNY7) and the direct branch-series estimate give the inverse chord estimate (PNY8) on the union of this critical curve and $Y$. The critical-secant obstruction (PNY2)–(PNY4) then contradicts Whitney (a,b). Hence

\[
t=1\quad\Longrightarrow\quad
\dim C_0<N-2,\qquad \dim C_0\leq N-3.
\tag{CSB4}
\]

The contradiction uses actual regular critical points supplied by the section density. It does not infer them solely from intersection with the central fibre.

### Base slices and the possible components over the origin

Now take arbitrary $0<t<d$ and set $k=t-1$. Flatten $Y$ in local coordinates and choose linear forms $l_1,\ldots,l_k$ whose restrictions to $T_0Y$ are independent. Put $A_j=\{l_1=\cdots=l_j=0\}$ and $T_j=C\cap\kappa^{-1}(H\cap A_j)$, so $T_0=C$ is the total space, while $C_0=\kappa^{-1}(0)$ continues to denote its base fibre.

Choose the forms successively to avoid every local component of the current total section and bad subset whose base image is not the single point $0$. These are finite proper linear exclusions in a compact-fibre chart cover. The rank condition on $T_0Y$ is an open condition and can be preserved. A component whose base image is $0$ cannot be cut by such a form; it lies in the original fibre and has dimension at most $N-1-t$ by (CSB1). This gives the explicit induction estimates

\[
\dim T_j=N-1-j\quad\text{pure},
\qquad
\dim(T_j\cap Z)\leq
\max\{N-2-j,\ N-1-t\},
\qquad 0\leq j\leq k.
\tag{CSB5}
\]

For the total section, a component over $0$ has dimension smaller than $N-1-j$ throughout this range and therefore cannot be a component of the pure section. Every other component is cut properly and loses one dimension. For the bad subset, a component over $0$ retains the stated smaller bound, while every other component loses one dimension. This proves (CSB5) recursively and handles the vertical components rather than assuming they disappear.

At $j=k$ the total dimension is $N-t$, while the bad dimension is at most $N-t-1$. Thus the literal inverse-image section $R=T_k$ is exactly the closure of its old regular graph part, and its base fibre is the entire original $C_0$. The same finite component avoidance applied simultaneously to $H$ and $H_{\mathrm{sing}}\cup Y$ gives

\[
H'=(H\cap A_k)_{\mathrm{red}},\qquad
\dim H'=d-t+1\geq2,\qquad
Y'=Y\cap A_k\ \text{smooth of dimension }1,
\tag{CSB6}
\]

with the old regular slice dense in every component of $H'$. Its bad subset has dimension at most $d-t$. When $t=1$, no base slicing is required and these statements are the identity slice.

### A finite comparison of the entire ordinary fibres

Let $K=\operatorname{span}(l_1,\ldots,l_k)$ in the ambient dual. Independence on $T_0Y$ gives $K\cap(T_0Y)^\perp=0$. By (CSB1), $\mathbb P K$ misses the entire original conormal fibre. Properness excludes it from the conormal space over a neighborhood of $0$. Therefore every nearby regular upper tangent is transverse to $A_k$. Covector restriction is everywhere defined on $R$ and gives

\[
R\xrightarrow{\ p_A\ }S=C_{A_k}(H'),
\qquad(x,[\xi])\longmapsto(x,[\xi|_{A_k}]).
\tag{CSB7}
\]

At an old regular sliced point, restriction is an isomorphism of the annihilators: its kernel is $K\cap(T_xH)^\perp=0$, and both annihilators have dimension $N-d$. Density of the old regular slice identifies the image with all of $S$. The map is proper because $R$ is proper over its base. For a fixed new covector $[\beta]$, all ambient lifts form

\[
\mathbb P(\mathbb C\widetilde\beta+K)\setminus\mathbb P K
\simeq\mathbb C^k.
\tag{CSB8}
\]

Each fibre is a compact analytic subset of this affine space and is finite by coordinate separation. For $k=0$ the map is the identity. Thus $p_A$ is finite and surjective, and, since it preserves the base point,

\[
p_A:R_0=C(H)_0\longrightarrow C_{A_k}(H')_0
\text{ is finite and surjective},
\qquad
\dim C(H)_0=\dim C_{A_k}(H')_0.
\tag{CSB9}
\]

This compares the entire ordinary conormal fibres. The equality would not follow from the regular tangent isomorphism without the density and proper finite-fibre arguments.

The sliced pair is Whitney (a,b) at $0$. Indeed, $A_k$ is transverse to every upper limiting tangent because those tangents contain $T_0Y$. Transverse tangent intersections vary continuously, contain $T_0Y'=T_0Y\cap A_k$, and contain every sliced secant limit by (b). For new regular sliced points in the old singular locus, use the established old regular density to approximate within their smooth sliced patches, making the error divided by secant length and the tangent error tend to zero. This retains arbitrary varying lower points in $Y'$.

The curve case (CSB4), applied in ambient dimension $N'=N-t+1$, and (CSB9) yield

\[
\dim C(H)_0\leq N'-3=N-2-t.
\tag{CSB10}
\]

For a linear $H=\mathbb C^d\subset\mathbb C^N$ and $Y=\mathbb C^t\subset H$, restriction identifies the two constant conormal fibres $\mathbb P^{N-d-1}$. The reduced slice has dimension $d-t+1$ and ambient dimension $N-t+1$, so its conormal dimension is again $N-d-1$. The inequality in (CSB10) becomes $d\geq t+1$, exactly the positive-codimension hypothesis. The case $d=t$ retains the separate empty-graph argument and is not included in this ordinary-fibre inequality.

The finite comparison has the antecedent [Teissier IV.5.3.1, pp.442–443](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=130). The actual compact affine-fibre fact and one-equation bounds have the permitted proofs [Demailly II.5.7–5.9, p.104, and II.6.1–6.3, pp.105–106](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=104). Here the successive section density, vertical-component estimates, Whitney transfer and finite fibre comparison are supplied directly. The historical curve-family/saturation route is the source antecedent for (PNY6)–(PNY8), with source antecedent [Teissier V.1.2.2, pp.462–466](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=150). The preceding actual incidence and marked-normalization arguments supply the required generic family input. The preceding normal and finite analytic proofs supply the normalization and dimension inputs. The direct branch-series proof supplies the needed parameter derivative and mixed chord estimate. Saturated-curve structure, the full saturated-algebra stability theorem and generic-to-total integral-dependence specialization are not imported for this direct application. No general-section polar-multiplicity formula or pre-existing Whitney stratification is imported for the new geometric deductions.

The following exceptional-fibre induction can now use (CSB10) at this reduced floor. This removes the additional conormal polar-section and general-section multiplicity inputs from that route; the normal and finite analytic hypotheses remain those specified in the preceding proofs. This is an independently written reconstruction of standard conormal geometry; source prose and media are not adapted or reproduced.

<a id="SH02-FAG-HYPERPLANE-NECESSITY"></a>

## The actual exceptional-fibre necessity proof

Let $H\subset\mathbb C^N$ be reduced and pure of dimension $d$, and let $Y\subset H$ be smooth of dimension $t$ near $0$. Assume $N\geq d+2$. Use the actual graph blow-up $B$ and reduced exceptional divisor $D$ in (PNY1), discarding any conormal component lying wholly over the centre. We now prove that Whitney (a,b) at $0$ implies that $D_0$ is empty or has dimension $N-2-t$.

This proof uses the [direct first conormal-fibre bound](#SH02-FAG-CONORMAL-SLICE-FLOOR) using the actual critical family, marked normalization and direct branch-series estimate proved above. Its own section and finite-slice arguments remove the additional conormal polar-section and general-section multiplicity inputs from this route. It adds independent hyperplane, strict-transform and finite-comparison arguments. It does not require the separate theorem that all polar multiplicities are constant along $Y$. Together with the [contact sufficiency proof](#SH02-FAG-CONORMAL-SUFFICIENCY), it proves the complete conormal criterion relative to the stated local analytic and algebraic inputs. The linked analytic and polar proofs retain those stated hypotheses.

### Choosing the hyperplane on the recorded normal directions

Flatten $Y$ to $\{z=0\}$ in coordinates $(y,z)\in\mathbb C^t\times\mathbb C^{N-t}$. This preserves the Whitney conditions and the conormal graph blow-up, as proved in the contact section. First suppose $0<t<d$. The direct conormal-slice argument gives

\[
\dim\kappa^{-1}(0)\leq N-2-t
<\dim\mathbb P((T_0Y)^\perp)=N-1-t.
\tag{HN1}
\]

Thus a general covector $\alpha$ on the normal coordinates gives a hyperplane $L_\alpha$ containing $Y$ whose defining covector is absent from $\kappa^{-1}(0)$. Properness of $\kappa$ then excludes that covector over a whole neighborhood of $0$. Consequently $L_\alpha$ is transverse to every regular upper tangent there and to every limiting upper tangent at $0$.

The blow-up has its actual normal-direction map

\[
q:B\longrightarrow\mathbb P^{N-t-1},\qquad
L_\alpha=\{\alpha(z)=0\},\qquad
\Pi_\alpha=\{[w]:\alpha(w)=0\},\qquad
G=q^{-1}(\Pi_\alpha).
\tag{HN2}
\]

It is $G$ that must be used. The pullback of the original function $\alpha(z)$ vanishes on all of $D$ and therefore cannot perform the required cut inside $D_0$. On a projective blow-up chart $w_j\ne0$, the ratios $z_k/z_j=w_k/w_j$ extend holomorphically, and the original pullback factors as $z_j\alpha(z/z_j)$. The equation for $G$ is the second factor, interpreted as a local equation for the projective hyperplane section.

Here is an independent generic-density argument for that section. Let $U\subset B$ be the graph over $H_{\mathrm{reg}}\setminus Y$. It is open and dense in every retained component of $B$, which is pure of dimension $N-1$. Its complement $Z$ is analytic and has dimension at most $N-2$. The proper fibre $B_0$ is compact. A finite relatively compact chart cover of it meets only finitely many local irreducible components of $B$ and $Z$.

For each such component, the covectors $\alpha$ whose section $\alpha(q)$ vanishes identically form a proper linear subspace of the parameter space. It is proper because $q$ has a nonzero projective coordinate at every point. Avoid these finitely many subspaces, as well as the closed noncharacteristic exclusion in (HN1). The one-equation dimension theorem then gives, in a neighborhood of $B_0$,

\[
\dim G=N-2\quad\text{if }G\ne\varnothing,
\qquad
\dim(G\cap Z)\leq N-3,
\qquad \overline{G\cap U}=G.
\tag{HN3}
\]

The dimension bounds are local and apply component by component; components missed by the section cause no problem. Properness lets us shrink the base so that its entire inverse image lies in this chosen neighborhood. This proves actual strict-transform density without importing an already constructed Whitney stratification on the blow-up.

Also choose $\alpha$ so that $L_\alpha$ contains no irreducible component of $H$ and no component of $H_{\mathrm{sing}}$ outside $Y$. These impose finitely many further proper linear exclusions after shrinking the germ. A component contained in $Y$ cannot be excluded by such a hyperplane, and is treated explicitly below.

### The slice and its Whitney conditions

Put $c=d-t$ and take

\[
H'=(H\cap L_\alpha)_{\mathrm{red}},\qquad
\dim H'=d-1,
\qquad N'=N-1\geq(d-1)+2.
\tag{HN4}
\]

The upper slice is pure by the one-equation theorem. If $c\geq2$, each component has dimension greater than $t$. Components of $H_{\mathrm{sing}}$ not contained in $Y$ drop dimension upon intersection with $L_\alpha$; components contained in $Y$ have dimension at most $t\leq d-2$. Thus $H_{\mathrm{reg}}\cap L_\alpha$ is dense in every component of $H'$. If $c=1$, the same argument gives density on every component of $H'$ not contained in $Y$; the possible component $Y$ itself is retained separately.

Whitney (a,b) passes to $(H'_{\mathrm{reg}}\setminus Y,Y)$. At an old regular sliced point its tangent is $T_xH\cap L_\alpha$. Every limiting upper plane $T$ is transverse to $L_\alpha$, so intersection of planes is continuous there. Condition (a) gives $T_0Y\subset T\cap L_\alpha$, since $Y\subset L_\alpha$. Secants between upper sliced points and arbitrary lower points in $Y$ lie in $L_\alpha$; condition (b) puts their limits in that same intersection.

For a regular sliced point belonging to the old singular locus and lying outside $Y$, use the density just proved to approximate it in its smooth sliced patch by old regular sliced points. For a sequence and its actual lower points, choose the approximation error divided by the secant length to tend to zero, and also make the sliced tangent error tend to zero. A convergent subsequence of the original $d$-planes then proves exactly the same tangent and secant assertions. This supplies the needed density and diagonal approximation rather than assuming that all new regular sliced points were already regular in $H$.

For $c=1$, the equal-dimension argument in the preceding section now forces $H'=Y$ as germs. Then $G\cap U$ is empty near $B_0$; (HN3) makes $G$ itself empty there. This is the codimension-one base of the induction and requires no equimultiplicity theorem.

### Restricting actual covectors gives a finite comparison

For $c\geq2$, let $R\subset C(H)$ be the reduced closure of the conormal bundle over the old regular sliced points. Its covectors are ambient covectors on $\mathbb C^N$; the new conormal space $S=C_{L_\alpha}(H')$ uses covectors on $L_\alpha$. Restriction defines

\[
R\xrightarrow{\ p\ }S,\qquad
(x,[\xi])\longmapsto(x,[\xi|_{L_\alpha}]).
\tag{HN5}
\]

This map is everywhere defined after the preceding shrinking: its only possible projective indeterminacy would be the defining covector of $L_\alpha$, which is absent from the whole conormal space near $0$.

At an old regular sliced point, transversality gives the actual linear isomorphism

\[
(T_xH)^\perp\xrightarrow{\ \mathrm{restriction}\ }
(T_xH\cap L_\alpha)^\perp_{L_\alpha}.
\tag{HN6}
\]

Injectivity follows because the only covectors killed by restriction are multiples of $\alpha$, and $\alpha$ does not annihilate $T_xH$. Both spaces have dimension $N-d$, giving surjectivity. Density of the old regular slice and properness therefore put the entire image of $p$ in $S$ and make it surjective onto $S$.

The map is proper: a compact subset of $S$ has compact base image in $H'$, and $R$ is proper over that base. For a fixed new covector $[\beta]$, its projective ambient lifts lie in

\[
\mathbb P(\mathbb C\widetilde\beta+\mathbb C\alpha)
\setminus\{[\alpha]\}\simeq\mathbb C,
\tag{HN7}
\]

where $\widetilde\beta$ is any ambient lift. Each fibre of $p$ is a compact analytic subset of this affine line, hence finite. Coordinate separation, or the holomorphic maximum principle, is essential in this last statement. Thus $p$ is finite, with the actual regular-upper isomorphism above; finiteness is not inferred merely from a tangent-space correspondence.

### Lifting the comparison to the graph blow-ups

By (HN3), $G$ is exactly the closure of the normal-direction graph on the old regular conormal slice. Its image under $\theta$ is $R$, and it is the actual graph blow-up of the centre ideal pulled back to $R$. Write $B'$ for the actual graph blow-up of the pulled-back centre ideal in $S$. The pair consisting of $p$ and the same recorded normal direction maps the dense graph part of $G$ into $B'$. Continuity and closed graph closure do so for every point of $G$. More precisely,

\[
G\ \hookrightarrow\ R\times_S B'
\longrightarrow B',
\qquad
\gamma(r,[w])=(p(r),[w]).
\tag{HN8}
\]

The first map is a closed embedding: the actual graph $G$ is closed in $R\times\mathbb P^{N-t-1}$, and $R\times_S B'$ is the closed subspace defined there by membership of $(p(r),[w])$ in $B'$. The second map is a base change of the finite map $p$, hence proper with finite fibres. Its restriction $\gamma$ is finite. It is surjective onto every retained component of $B'$, because it contains the dense graph over old regular sliced points and its image is closed.

No assertion that the ordinary fibre product *equals* the blow-up is used. Extra components or exceptional torsion in that fibre product are discarded by the actual graph closure; the closed embedding in (HN8) is the direction needed to preserve finiteness.

By induction on $c$, the sliced Whitney pair has an empty exceptional fibre or one of dimension $N'-2-t=N-3-t$. Since $\gamma$ is finite and commutes with the maps to $H'$, the base fibre $G_0$ is empty or has the same dimension as $B'_0$. In particular,

\[
G_0=\varnothing\quad\text{or}\quad
\dim G_0\leq N-3-t.
\tag{HN9}
\]

For $c=1$, the preceding argument gave $G_0=\varnothing$ directly.

### Bounding every exceptional component

Let $Q$ be an irreducible component of maximum dimension in $D_0$. Its image $\Sigma=q(Q)$ is a closed projective analytic set. If $\dim\Sigma=0$, it is one point, and the graph embedding puts $Q$ in $\kappa^{-1}(0)\times\{[w]\}$. Equation (HN1) gives the required bound.

If $\dim\Sigma>0$, every projective hyperplane meets $\Sigma$. Otherwise $\Sigma$ would be a compact analytic subset of the affine complement of that hyperplane, whose coordinate functions separate points, and would therefore be finite. Thus $Q\cap G$ is nonempty. The one-equation lower dimension bound, applied locally to the projective hyperplane section on $Q$, gives $\dim(Q\cap G)\geq\dim Q-1$. It lies in $G_0$. If $G_0$ is empty this case is impossible; otherwise (HN9) gives

\[
\dim Q-1\leq\dim(Q\cap G)\leq N-3-t,
\qquad\text{so}\qquad\dim Q\leq N-2-t.
\tag{HN10}
\]

The reduced divisor $D$ is pure of dimension $N-2$. At any point of a nonempty fibre, its map to the smooth $t$-dimensional base $Y$ imposes only $t$ equations. The preceding lower dimension bound therefore gives the reverse inequality. Combining it with (HN10), or with the zero-dimensional-image case, proves

\[
D_0\ne\varnothing\quad\Longrightarrow\quad
\dim D_0=N-2-t.
\tag{HN11}
\]

This completes the induction for $0<t<d$. When $d=t$, the already proved equality-of-germs argument gives $H=Y$ and an empty actual graph blow-up. When $t=0<d$, the exceptional fibre is the divisor itself, so it is empty or pure of dimension $N-2$ by the one-equation argument; the contact sufficiency theorem supplies the Whitney conclusion. The zero-dimensional upper case is the equal-dimension case. No negative-dimensional projective space is inserted into an empty-fibre case.

### A linear check of the divisor equation and both dimensions

Take $H=\mathbb C^d\subset\mathbb C^N$ linear and $Y=\mathbb C^t\subset H$, with $c=d-t\geq1$. The conormal is the product of $H$ with $\mathbb P^{N-d-1}$, and the normal-direction graph records only the $c$ upper normal coordinates. Thus

\[
D_0=\mathbb P^{c-1}\times\mathbb P^{N-d-1},
\qquad \dim D_0=N-t-2,
\qquad
\dim G_0=N-t-3\quad(c\geq2).
\tag{HN12}
\]

Choose $\alpha$ nonzero on the upper normal coordinates. For $c\geq2$, $G_0$ is the hyperplane section of the first factor. For $c=1$, that section is empty. In contrast, the pulled-back original equation $\alpha(z)$ vanishes on the entire product $D_0$. This checks both the dimension drop and why dividing off the exceptional factor is necessary.

The source antecedents are Teissier [IV.5.3.1, pp.442–443](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=130) for finite conormal comparison and [V.1.2, pp.455–460](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf#page=143) for the hyperplane-induction geometry. Here the section density, Whitney transfer, compact affine-fibre comparison and finite graph lift are supplied directly. The separate equimultiplicity theorem for $H$'s polar varieties and the source's multiplicity-based induction are not imported here; the new section-density step needs no pre-existing Whitney stratification on the blow-up. The first-bound critical curve family and generic marked normalization are supplied by the preceding proofs. Their finite normalization and normal/analytic lower sources remain at the exact common floor. The direct branch-series estimate supplies the coordinate-derivative and mixed chord bound, without saturated-algebra stability, generic-to-total integral-dependence specialization or a whole fibre-algebra isomorphism. The direct conormal-slice proof supplies the additional section geometry and avoids the general-section multiplicity formula. The compact analytic-subset fact has the permitted proof in [Demailly II.5.7–5.9, p.104](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=104).

Together with contact sufficiency, the result is the complete relative criterion

\[
(H_{\mathrm{reg}}\setminus Y,Y)\text{ is Whitney (a,b) at }0
\quad\Longleftrightarrow\quad
D_0=\varnothing\ \text{or}\ \dim D_0=N-2-t.
\tag{HN13}
\]

The selected direct route proves necessity and sufficiency using the actual incidence family, marked finite normalization and branch-series estimate above. It does not use the optional general saturation or polar-multiplicity assertions. Its linked local algebra, coherence, reduced-ideal, dimension and holomorphic-calculus inputs retain their stated hypotheses. This independently written reconstruction concerns a standard theorem. The cited source prose and diagrams retain their rights and are not reproduced here.



## SH02-FAG-STATUS — The precise contribution to finite-map microsupport

FAG1 supplies the dimension bound for the equations defining a cotangent inverse image. FAG2–FAG5 supply the adapted finite-map geometry and its coefficient independence. FAG6 and the boundary argument supply analytic conormal closures and their annihilation property. These are the analytic deductions requested by SH02-FH-ANALYTIC-INPUT.

The component, finite-image, dimension and Whitney-failure arguments above use the linked preparation, coherence, reduced-ideal and local analytic geometry proofs with their stated hypotheses. This lesson proves no Morse-pair existence, microsupport detection by normal Morse data, controlled holomorphic perturbation, intersection conservation, or perverse theorem. Their statements are given separately in the finite-map lesson.
