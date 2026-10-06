# Curvature, characteristic classes and Gauss–Bonnet

DG-CHAR-17 · Differential geometry foundations

A curvature polynomial becomes a topological characteristic class only after its normalization is fixed. We construct a Gaussian representative of the Thom class, prove the relative integration comparison and its orientation sign, and identify Chern, Pontryagin and Euler forms with the previously constructed integral classes. The resulting Gauss–Bonnet theorem and worked calculations include the local connection, integration and algebraic arguments they require.

Manifolds are finite dimensional, Hausdorff, second countable, smooth and without boundary. Bundles have constant finite rank. We use the usual number systems and the axiom of choice. Complex metrics are conjugate-linear in the first argument; a complex basis orients the underlying real space by listing each vector followed by its imaginary multiple. A closed manifold means a compact manifold without boundary. Unless specified otherwise, topological cohomology is ordinary singular cohomology.

Earlier complete programme proofs are [Local tools for bundles and transport](../../../src/local-tools-for-bundles-and-transport.md), [Integral Thom classes and Euler indices](DG-CHAR-06.md), [Manifold duality and the Euler characteristic](DG-CHAR-07.md), [Projective bundles, Gysin sequences and line classes](DG-CHAR-08.md), and [Chern classes and the Whitney formula](DG-CHAR-09.md). The prefixes DG06–DG09 identify results in those lessons; local-tools labels identify the opening lesson. Unprefixed letter labels refer to this chapter. A parenthesized label names an equation; a label after “Lemma”, “Theorem” or “Exercise” names the stated result. Every used result is proved here or in an exact earlier programme scope. The free readings at the end supply construction material, not replacements for proofs.

## 1. Integration facts for the Thom-form construction

### Rectangular integration

**Lemma A.1 (continuous integration on boxes).** A continuous function on a compact rectangle in \(\mathbb R^n\) is Riemann integrable. Its integral equals its iterated integral in any order. Integration is linear, preserves inequalities and satisfies
\[
\left|\int_Q f\right|\leq\operatorname{vol}(Q)\sup_Q|f|.
\]

**Proof.** For a product partition, define lower and upper sums by the infimum and supremum on each closed subrectangle, multiplied by the product of its side lengths. A refinement increases lower sums and decreases upper sums: subdividing a rectangle preserves its total volume, and every new infimum is at least the old infimum, while every new supremum is at most the old supremum. Any two product partitions have a common refinement. Thus every lower sum is at most every upper sum. The least-upper-bound property gives the lower and upper integrals.

The function is uniformly continuous by local-tools Lemma 0.1. If the oscillation at distance at most \(\delta\) is \(\omega(\delta)\), a partition with rectangle diameters at most \(\delta\) has upper-minus-lower sum at most \(\operatorname{vol}(Q)\omega(\delta)\). This tends to zero, so the two integrals agree. Every tagged sum lies between the corresponding lower and upper sums and consequently tends to the integral as the mesh tends to zero. Finite-sum linearity, inequalities and the displayed estimate pass to the limit. Apply this coordinatewise for vector-valued functions.

For the iterated-integral assertion, first split the coordinates into two nonempty groups. A product tagged sum is the sum, over the second group, of the tagged sums over the first group, with the corresponding product volumes. The error in any first-group sum is bounded by its box volume times the same uniform oscillation, independently of the second-group coordinates. Moreover the first-group integral is a continuous function of the second-group coordinates, since the integral estimate bounds its change by the uniform change of the integrand. Passing to the two limits therefore gives the iterated integral. Induction and permutations of the coordinate groups prove the assertion for every order. \(\square\)

A continuous compactly supported function on \(\mathbb R^n\) is integrated over any compact rectangle containing its support in its interior. The value is independent of that rectangle by refinement and additivity. Products of one-variable compactly supported continuous functions integrate to the product of their integrals, by Lemma A.1.

**Lemma A.2 (linear substitutions).** For an invertible real matrix \(B\), a vector \(v\) and a continuous compactly supported function \(f\),
\[
\int_{\mathbb R^n} f(Bx+v)\,dx
=\frac{1}{|\det B|}\int_{\mathbb R^n} f(y)\,dy.
\tag{A.1}
\]

**Proof.** In one variable, translation and nonzero scaling follow from the fundamental theorem applied to a primitive of the continuous function; if the scaling is negative, reversing the endpoints supplies the absolute value. All endpoint intervals can be chosen beyond the compact supports. Lemma A.1 then gives the formula for translations and scaling of any one coordinate, and for permutations of coordinates.

For a shear \(y_i=x_i+c x_j\), \(y_k=x_k\) for \(k\ne i\), integrate first in \(x_i\). For every fixed choice of the other coordinates this is a translation of that one-dimensional integral, so the integral is unchanged. A sufficiently large common rectangle contains the compact support and its image and preimage under the shear; thus no unbounded-parameter exchange is needed.

Every invertible matrix is a product of coordinate permutations, nonzero coordinate scalings and shears. To check this algebraically, perform elimination column by column. At a given stage a pivot must occur in the remaining part of the column; otherwise, after the preceding columns have been made coordinate vectors, the columns of the matrix would be linearly dependent. Interchange rows to place that pivot, scale it to one and clear the other entries by shears. The finite procedure reduces the matrix to the identity, and reversing the operations gives the asserted factorization.

Here the determinant is defined as the signed permutation sum. That sum is alternating and multilinear in the columns and is one on the identity. Every alternating multilinear function of the columns is its value on the identity times this sum: expand each column in the coordinate basis, discard repeated coordinate vectors and reorder the remaining basis vectors. Applying this observation to \(\det(BC)\) as a function of the columns of \(C\) proves multiplicativity. The elementary factors above therefore have absolute determinant respectively one, the absolute coordinate scale, and one. Composing their integral formulas proves (A.1). \(\square\)

### Parameter differentiation and Gaussian bounds

**Lemma A.3 (parameter integrals).** Suppose \(f(z,y)\) is smooth and, locally in the parameter \(z\), has support in one fixed compact set of \(y\)-space. Then \(\int f(z,y)\,dy\) is smooth, and every parameter derivative passes through the integral.

**Proof.** Work on a compact parameter box inside the domain and a rectangle containing the common support. For a coordinate direction \(e_i\), the one-dimensional fundamental theorem gives
\[
\frac{f(z+h e_i,y)-f(z,y)}{h}
=\int_0^1\partial_i f(z+t h e_i,y)\,dt.
\]
Uniform continuity of \(\partial_i f\) on a slightly larger compact product box makes the right side converge uniformly in \((z,y)\) to \(\partial_i f(z,y)\). The integral estimate of Lemma A.1 permits taking that limit through the \(y\)-integral. Repeating this argument for every derivative proves the assertion to all orders. The same proof covers finite parameter integration of coefficients of a differential form. \(\square\)

**Lemma A.4 (Gaussian tail and smooth improper integration).** For \(c>0\) and a nonnegative integer \(N\), the function \((1+t)^N e^{-ct^2}\) is integrable on \([0,\infty)\), and its tail tends to zero. Suppose, on each compact parameter box \(K\), a smooth function \(f(z,t)\) and each of its parameter derivatives satisfy a bound of that form, with constants allowed to depend on the derivative and \(K\). Then
\[
z\longmapsto\int_0^\infty f(z,t)\,dt
\]
is smooth and may be differentiated under the integral to every order.

**Proof.** Local-tools Lemma 0.5 proves \(e^u\geq u^k/k!\) for \(u\geq0\). Choose \(2k\geq N+2\). For \(t\geq1\), this gives
\[
(1+t)^N e^{-ct^2}\leq 2^N k!c^{-k}t^{-2}.
\]
The integral of \(t^{-2}\) from \(T\) to infinity is \(1/T\), by the fundamental theorem. On \([0,1]\) continuity gives a finite bound. This proves absolute convergence and a uniform tail estimate for each indicated parameter derivative.

The integrals truncated at \(T\) are smooth by Lemma A.3. Their derivatives of every fixed order converge uniformly on compact parameter boxes, by the same tail estimate. To justify differentiating the limiting functions without assuming a separate theorem, write the fundamental-theorem identity for each truncated integral along a short coordinate segment. Uniform convergence allows passage to the limit in both endpoint values and the one-dimensional integral. Divide the resulting identity by the segment length and use continuity of the limiting derivative. This proves that it is the actual derivative of the limiting function. Iterate the argument to obtain smoothness of every order. \(\square\)

The same argument shows that a polynomial in \(y\) times \(e^{-c|y|^2}\), and each of its derivatives, is integrable over \(\mathbb R^n\). Indeed each monomial is bounded by a product of one-variable polynomial Gaussians; apply Lemma A.1 on expanding rectangles and then Lemma A.4 in each variable. The integral outside a large cube tends to zero: its complement is contained in the union of the \(n\) coordinate tail regions, and each bound factors into one vanishing tail integral and \(n-1\) finite integrals. Thus iterated integration and these limits commute. In particular the integral of any coordinate derivative of such a rapidly decreasing function is zero, by integrating that coordinate first and using its zero limits at both ends.

### The normalizing constant

**Lemma A.5 (the Gaussian integral).** With \(\pi\) equal to the area of the Euclidean unit disk,
\[
\int_{\mathbb R}e^{-x^2}\,dx=\sqrt\pi,
\qquad
\int_{\mathbb R^r}e^{-|y|^2}\,dy=\pi^{r/2}.
\tag{A.2}
\]

**Proof.** We provide the needed radial integration argument rather than assuming a polar-coordinate substitution theorem. The upper and lower halves of the unit circle are the graphs of \(\pm g(x)\), where \(g(x)=\sqrt{1-x^2}\) on \([-1,1]\). The positive square root exists by local-tools Lemma 0.0; its continuity, including at zero, follows from \(|\sqrt a-\sqrt b|\leq\sqrt{|a-b|}\) for \(a,b\geq0\). To verify that inequality, assume \(a\geq b\), square its nonnegative sides, and use \(b\leq\sqrt{ab}\). Thus \(g\) is uniformly continuous.

Choose a partition of \([-1,1]\) such that the oscillation of \(g\) on every interval is at most \(\epsilon\), and choose a vertical partition with mesh at most \(\epsilon\). In any vertical strip, the cells meeting either of the two graphs have total height at most \(2\operatorname{osc}(g)+4\epsilon\leq6\epsilon\): for each graph the cells lie between its minimum minus \(\epsilon\) and maximum plus \(\epsilon\). All other cells lie wholly inside or wholly outside the disk. Hence the disk indicator's upper-minus-lower sum is at most \(12\epsilon\), after summing the strip widths, whose total is two. Compute these sums on \([-1,1]^2\). They prove integrability of the disk indicator there. The same cell bound applied to the circle indicator proves that its area is zero. Extending to a larger enclosing rectangle adds only zero values away from that zero-area boundary, so does not change the integral. Column sums converge to twice the integral of \(g\), giving the positive area
\[
\pi=2\int_{-1}^1\sqrt{1-x^2}\,dx.
\]
Scaling both coordinates by \(R\) scales rectangular sums by \(R^2\), so the disk of radius \(R\) has area \(\pi R^2\). Its boundary has zero area by the same graph argument. Thus the annulus \(a\leq |y|^2\leq b\) has area \(\pi(b-a)\).

If \(h\) is continuous on \([0,R^2]\), the function \(h(|y|^2)\) on the disk is integrable. Extend it by zero outside the disk. On the boundary cells its upper-minus-lower contribution is bounded by twice the maximum of its absolute value times their arbitrarily small area; on the other cells use uniform continuity, as in Lemma A.1. Partitioning \([0,R^2]\) and bounding \(h\) on the corresponding annuli now gives lower and upper sums exactly equal to \(\pi\) times the one-dimensional lower and upper sums for \(h\). Therefore
\[
\int_{|y|\leq R}h(|y|^2)\,dy
=\pi\int_0^{R^2}h(s)\,ds.
\tag{A.3}
\]
Apply this to \(h(s)=e^{-s}\). The value is \(\pi(1-e^{-R^2})\), by the fundamental theorem. The square \([-L,L]^2\) contains the radius-\(L\) disk and is contained in the radius-\(\sqrt2L\) disk. Since the integrand is nonnegative, Lemma A.1 and (A.3) give
\[
\pi(1-e^{-L^2})
\leq\left(\int_{-L}^L e^{-x^2}\,dx\right)^2
\leq\pi(1-e^{-2L^2}).
\]
The one-dimensional integral converges by Lemma A.4 and is positive. Letting \(L\) tend to infinity and taking the positive square root proves the first identity. Products on cubes and the tail argument following Lemma A.4 prove the second. \(\square\)

For comparison with the usual circular normalization, integration by parts on \([0,b]\), followed by \(b\uparrow1\), gives
\[
\pi=2\int_0^1\frac{dx}{\sqrt{1-x^2}}
=4\int_0^1\frac{dt}{1+t^2}.
\]
The second equality uses \(x=2t/(1+t^2)\); its derivative and \(\sqrt{1-x^2}=(1-t^2)/(1+t^2)\) give the equality first below the endpoint and then in the limit. For the integration-by-parts step, differentiate \(x\sqrt{1-x^2}\); rearrangement yields \(2\sqrt{1-x^2}=\frac{d}{dx}(x\sqrt{1-x^2})+(1-x^2)^{-1/2}\), and the endpoint term tends to zero. This identifies the area normalization with the standard inverse-tangent normalization as well.

## 2. Differential forms and the bundle calculus used here

A smooth vector bundle is given by local products with linear transition maps that depend smoothly on the base. Sections and bundle maps are smooth when their coordinates in these local products are smooth. These are definitions. A positive metric on a real bundle is a smoothly varying positive definite symmetric bilinear form; on a complex bundle we use a positive Hermitian form, conjugate-linear in its first argument.

### The exterior differential

**Lemma D.0 (mixed derivatives).** For a smooth scalar function on an open subset of Euclidean space, mixed second partial derivatives commute.

**Proof.** Hold all but two coordinates fixed in a small closed rectangle within the domain. For side lengths \(h,k>0\), the corner difference
\[
f(x+h,y+k)-f(x+h,y)-f(x,y+k)+f(x,y)
\]
is both \(\int_x^{x+h}\int_y^{y+k}\partial_y\partial_x f(u,v)\,dv\,du\) and \(\int_y^{y+k}\int_x^{x+h}\partial_x\partial_y f(u,v)\,du\,dv\), by two applications of the one-dimensional fundamental theorem. Divide each equality by \(hk\). Continuity of the two derivatives makes each average tend to its value at \((x,y)\) as \(h,k\downarrow0\). The corner differences are the same, so the two limiting values agree. Apply the argument to real and imaginary parts for a complex-valued function. \(\square\)

A differential \(q\)-form is a smooth alternating \(q\)-linear function on tangent vectors. In coordinates it is a unique sum \(\sum_I f_I dx^{i_1}\wedge\cdots\wedge dx^{i_q}\), with increasing indices. The wedge product is the alternating product, normalized so that the ordered wedge of coordinate one-forms evaluates to the determinant of their coordinate evaluations. Alternating multilinearity, proved by expansion in a coordinate basis, gives associativity and the sign \(\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha\) for degrees \(p,q\).

**Lemma D.1 (global exterior calculus).** The coordinate rule
\[
d\left(\sum_I f_I dx^I\right)=\sum_I df_I\wedge dx^I
\]
is independent of coordinates, satisfies \(d^2=0\) and the graded product rule, and commutes with smooth pullback.

**Proof.** The product rule follows from the ordinary product rule for coefficient functions, moving the newly introduced one-form past the first factor's differentials. In \(d^2 f\), the coefficients of \(dx^i\wedge dx^j\) cancel in pairs by Lemma D.0; the repeated-index terms vanish. Applying the product rule then proves \(d^2=0\) on every coordinate monomial form.

Under a coordinate change \(y=y(x)\), the chain rule says that the differential of any scalar function is unchanged, and each \(dy^i\) is that coordinate function's differential. Its exterior derivative is zero by the preceding calculation. Every form in the \(y\)-coordinates is generated by these functions and their differentials. Applying the product rule therefore yields the same exterior derivative in the \(x\)-coordinates. This proves coordinate independence. For a smooth map \(f\), pullback is defined by applying its derivative to each tangent-vector argument. The chain rule gives \(f^*(dg)=d(g\circ f)\), and alternating multilinearity gives preservation of wedges. Since functions and their coordinate differentials generate forms locally, the same argument proves \(f^*d=df^*\) on all forms. \(\square\)

Closed forms are those killed by \(d\); exact forms are differentials of forms of one lower degree. Since \(d^2=0\), the quotient defines de Rham cohomology. The product rule makes wedge product descend to it: replacing a closed factor by an exact change changes its product with another closed factor by an exact form. Pullback likewise descends. These statements follow directly from Lemma D.1 and do not presuppose a comparison with singular cohomology.

### Metrics and connections

**Lemma D.2 (metrics and compatible connections exist).** Every smooth real or complex vector bundle on a finite-dimensional Hausdorff second-countable smooth manifold has a positive metric and a connection compatible with that metric.

**Proof.** Take a smooth locally finite partition \((\rho_i)\) subordinate to bundle trivializations, with each support contained in its trivializing open set. Existence is the complete partition theorem in the repaired opening lesson, Theorem 3.1. In each trivialization use the ordinary positive inner product, denoted \(h_i\). The expression \(h=\sum_i\rho_i h_i\) is smooth and global: each term extends by zero outside its open set and the sum is locally finite. For a nonzero vector at a base point, every active \(h_i\) is positive and at least one \(\rho_i\) is positive, so \(h\) is positive.

There are smooth orthonormal local frames for \(h\). Starting from a frame \(v_1,\ldots,v_r\), set recursively
\[
w_j=v_j-\sum_{k<j}e_k h(e_k,v_j),\qquad
e_j=w_j/\sqrt{h(w_j,w_j)}.
\]
The preceding vectors are orthonormal by induction, so direct substitution makes \(w_j\) orthogonal to them. It cannot vanish, since that would express \(v_j\) in the span of its predecessors. Hence the square root is positive and all formulas are smooth. Smoothness of the positive square root follows from local-tools Theorem 1.2 applied to \(t\mapsto t^2\) for \(t>0\), or its derivative formula and induction. The change from the original frame is triangular with positive real diagonal entries, so an initially oriented real frame retains its orientation.

In each orthonormal frame define a local connection by differentiating the coefficient vector. It obeys \(\nabla^i(fs)=df\,s+f\nabla^i s\) and preserves \(h\), since its frame inner products are constant. Use a partition subordinate to these frame neighbourhoods and define \(\nabla s=\sum_i\rho_i\nabla^i s\), extending each term by zero. The sum is locally finite. The Leibniz rule follows because \(\sum_i\rho_i=1\). The metric identity
\[
d\,h(s,t)=h(\nabla s,t)+h(s,\nabla t)
\]
also follows by summing the local identities with these weights. This constructs the required compatible connection. \(\square\)

A connection in a local frame \(e\) necessarily has the form \(\nabla(e v)=e(dv+A v)\), where the columns of \(A\) are the coefficients of \(\nabla e_j\). Conversely this formula defines a local connection from a matrix of one-forms. Extend it to vector-valued \(q\)-forms by
\[
\nabla(\alpha s)=d\alpha\,s+(-1)^q\alpha\wedge\nabla s.
\]
The Leibniz rule ensures that this is independent of how the expression is written in a frame. For the difference of two connections the \(df\) term cancels, so their difference is a global endomorphism-valued one-form. In particular affine combinations with weights summing to one are connections, and such combinations preserve a fixed metric when every summand does.

**Lemma D.3 (gauge change and curvature).** If \(e'=eg\), then
\[
A'=g^{-1}Ag+g^{-1}dg,\qquad
F=dA+A\wedge A,\qquad F'=g^{-1}Fg.
\tag{D.1}
\]
The curvature satisfies \(dF+A\wedge F-F\wedge A=0\). Pullback of a connection by a smooth base map has the pulled-back curvature. In an orthonormal real frame \(A^T=-A\) and \(F^T=-F\); in a unitary complex frame the corresponding identities use conjugate transpose.

**Proof.** Substitute \(e'=eg\) into the Leibniz rule: \(\nabla(e'v')=e(dg\,v'+g\,dv'+Agv')\), which is (D.1)'s first formula after multiplication by \(g^{-1}\). Applying the extended connection twice to a coefficient vector cancels the two terms containing \(A\wedge dv\) and leaves \((dA+A\wedge A)v\). Since the square of the globally defined connection is independent of the frame, this proves the conjugation rule for \(F\). Expanding \(d(dA+A\wedge A)+A\wedge(dA+A\wedge A)-(dA+A\wedge A)\wedge A\) cancels every term and proves Bianchi.

For a smooth base map, the matrices \(f^*A\) satisfy the same transition formula on pulled-back frames by Lemma D.1; they therefore define a connection on the pullback bundle. That lemma and the curvature formula give \(F_{f^*\nabla}=f^*F\). Finally apply the metric identity to pairs of orthonormal frame vectors to obtain \(A^T+A=0\), or \(A^*+A=0\). Transposition or conjugate transposition of a product of two one-form matrices reverses their order and introduces a minus sign. The stated skewness of the curvature follows. \(\square\)

All tensor and exterior connections used in the Gaussian section are obtained by applying this connection to each vector factor and the product rule. In particular, the derivative of the oriented top exterior product is its coefficient times \(\operatorname{tr}A=0\). The coordinate checks in that section consequently rest on these proved connection identities, not on an external Chern–Weil theorem.

## 3. The Pfaffian identities needed by the curvature construction

**Lemma P.0 (polynomial identity test).** A polynomial in finitely many real variables with real or complex coefficients that vanishes on a nonempty real open box is the zero polynomial. Consequently a polynomial with integer coefficients which is zero for all real substitutions remains zero under substitution in any commutative unital ring.

**Proof.** A one-variable polynomial \(f\) with a root \(a\) has a factor \(t-a\): subtract the constant \(f(a)\) and use
\[
t^m-a^m=(t-a)\sum_{j=0}^{m-1}t^{m-1-j}a^j
\]
on each monomial. Induction on degree shows that a nonzero polynomial of degree \(d\) has at most \(d\) distinct roots. The proof works over either \(\mathbb R\) or \(\mathbb C\). In particular a polynomial vanishing on a real interval has every coefficient zero.

For several variables, write the polynomial as a polynomial in the last variable. Fixing the others in their open intervals makes each coefficient zero by the one-variable assertion. Each coefficient polynomial vanishes on the smaller open box, so induction on the number of variables finishes the proof. An integer polynomial zero under all real substitutions therefore has every integer coefficient equal to zero. Evaluating those zero coefficients in any commutative unital ring proves the final assertion. \(\square\)

For an alternating \(2k\)-by-\(2k\) matrix \(B\), define
\[
\operatorname{Pf}(B)
=\sum_{\mathcal P}\operatorname{sgn}(i_1,j_1,\ldots,i_k,j_k)
 B_{i_1j_1}\cdots B_{i_kj_k}.
\tag{P.1}
\]
The sum runs over pairings of \(\{1,\ldots,2k\}\), uniquely ordered by \(i_a<j_a\) and \(i_1<\cdots<i_k\). Here *alternating* means \(B_{ji}=-B_{ij}\) and \(B_{ii}=0\), including in rings of characteristic two. Put \(\operatorname{Pf}(\varnothing)=1\). Formula (P.1) is an integer polynomial and needs no division.

Over the reals, complex numbers or a real differential-form algebra with even-degree entries, it equals the top exterior coefficient of the following exponential. Indeed, in
\[
\exp\left(\sum_{i<j}B_{ij}e_i e_j\right),
\]
only the term with \(k\) disjoint pairs contributes. The \(k!\) orders of these even exterior factors have equal signs and cancel the exponential's denominator. Ordering their indices produces exactly the sign in (P.1).

**Lemma P.1 (congruence and direct sums).** For a \(2k\)-by-\(2k\) matrix \(Q\) and an alternating matrix \(B\) over a commutative unital ring,
\[
\operatorname{Pf}(Q^T BQ)=\det(Q)\operatorname{Pf}(B).
\tag{P.2}
\]
For two alternating matrices of even sizes, in the ordered direct-sum orientation,
\[
\operatorname{Pf}(B\oplus C)=\operatorname{Pf}(B)\operatorname{Pf}(C).
\tag{P.3}
\]

**Proof.** First work over the reals. In a vector space with dual basis \(e^1,\ldots,e^{2k}\), associate to \(B\) the two-form
\[
\omega_B=\sum_{i<j}B_{ij}e^i\wedge e^j.
\]
Its value on a pair of column vectors \(u,v\) is \(u^TBv\). Pullback by the linear map \(Q\) therefore takes it to \(\omega_{Q^TBQ}\). Pullback preserves wedge products, and on the top wedge it multiplies by \(\det Q\), by the alternating-column proof of the determinant in Lemma A.2. Comparing the coefficients in \(\omega_B^k/k!\) proves (P.2). This argument also allows singular \(Q\).

For a direct sum, the two-form is the sum of two even exterior forms in disjoint sets of generators. Their exponential is the product of their finite exponentials, since the two summands commute; the binomial theorem verifies this factorization term by term. Only the top degree of each block can contribute to the top degree of the sum. Reading the generators in the stated order gives (P.3) with no extra sign. Both identities are polynomial identities with integer coefficients by (P.1) and the determinant formula. Lemma P.0 transfers them to every commutative unital ring. \(\square\)

**Theorem P.2 (Pfaffian squared).** For every alternating matrix \(B\) of even size over a commutative unital ring,
\[
\operatorname{Pf}(B)^2=\det B.
\tag{P.4}
\]

**Proof.** Again first work over \(\mathbb R\), and induct on the half-size \(k\). The empty matrix gives \(1=1\). Suppose \(k\geq1\) and \(b=B_{12}\ne0\). Regard \(B\) as the alternating bilinear form \(B(u,v)=u^TBv\). Keep the first two basis vectors, and for \(i\geq3\) replace the \(i\)-th vector by
\[
w_i=e_i+\frac{B_{2i}}{b}e_1-\frac{B_{1i}}{b}e_2.
\tag{P.5}
\]
Then
\[
B(e_1,w_i)=B_{1i}-\frac{B_{1i}}b B_{12}=0,
\qquad
B(e_2,w_i)=B_{2i}+\frac{B_{2i}}b B_{21}=0.
\]
The change-of-basis matrix \(Q\) has diagonal entries one, with the only extra entries in the first two rows of later columns, so \(\det Q=1\). Its congruence reduces the matrix to
\[
Q^TBQ=\begin{pmatrix}0&b\\-b&0\end{pmatrix}\oplus C,
\]
where \(C\) is alternating of size \(2k-2\). Lemma P.1 gives \(\operatorname{Pf}(B)=b\operatorname{Pf}(C)\). The determinant permutation formula for a block-diagonal matrix gives \(\det(Q^TBQ)=b^2\det C\), and multiplicativity from Lemma A.2 makes this \(\det B\). The induction hypothesis proves (P.4) when \(B_{12}\ne0\).

If \(B_{12}=0\), change just \(B_{12}\) to \(\epsilon\) and \(B_{21}\) to \(-\epsilon\). Every nonzero real \(\epsilon\) gives the proved identity. Let \(\epsilon\to0\); both sides are continuous polynomials, so the identity holds for the original matrix too. This completes the induction over the reals. Finally both sides of (P.4) are integer polynomials in the independent entries \(B_{ij}\), \(i<j\). Lemma P.0 proves the identity in every indicated coefficient ring. \(\square\)

**Corollary P.3 (curvature signs and the top real characteristic form).** If \(F\) is an alternating curvature matrix of even-degree forms, all the preceding identities apply, since even forms commute. In an oriented orthonormal frame change, \(F'=g^{-1}Fg=g^TFg\) and \(\det g=1\). Thus \(\operatorname{Pf}(F/2\pi)\) is a global real form. Reversing the bundle orientation multiplies it by \(-1\), and ordered oriented direct sums multiply these forms. In rank \(2k\),
\[
\operatorname{Pf}(F/2\pi)^2=\det(F/2\pi).
\tag{P.6}
\]

**Proof.** The identities follow respectively from (P.2), (P.3) and (P.4), after dividing every matrix entry by \(2\pi\). A reversing orthonormal change has determinant \(-1\); an orientation-preserving one has determinant \(1\), since orthogonality and determinant multiplicativity imply \((\det g)^2=1\). No diagonalization is needed. \(\square\)

For example, with the order \(1,2,3,4\),
\[
\operatorname{Pf}(B)=B_{12}B_{34}-B_{13}B_{24}+B_{14}B_{23}.
\]
This follows by listing the three pairings in (P.1); the middle pairing changes the order of indices once and the last twice. It fixes the four-dimensional sign explicitly.

## 4. Fibre integration and uniqueness of a normalized form

Let \(p:E\to M\) be an oriented real vector bundle of rank \(r>0\), with a smooth positive fibre metric. Write \(\Omega^q_{\mathrm{pr}}(E)\) for the smooth \(q\)-forms whose support is proper over the base: its intersection with \(p^{-1}(K)\) is compact whenever \(K\subset M\) is compact. The differential preserves this space, since the support of a derivative is contained in the original support.

We use **base-first integration**. In an oriented bundle chart with base coordinates \(x\) and fibre coordinates \(y_1,\ldots,y_r\), put
\[
p_*\left(\sum_{I,J}a_{I,J}(x,y)\,dx^I\wedge dy^J\right)
=\sum_I\left(\int_{\mathbb R^r}a_{I,\{1,\ldots,r\}}(x,y)\,dy\right)dx^I.
\]
Components without all \(r\) fibre differentials contribute zero. The integral uses the given fibre orientation. For this convention the identities are
\[
d p_*\omega=p_*d\omega,
\qquad
p_*(p^*\gamma\wedge\omega)=\gamma\wedge p_*\omega.
\tag{F.1}
\]
These are identities on forms, with no additional sign in the first one. On a relatively compact base chart, proper support puts every coefficient inside one fixed compact region of fibre coordinates. Differentiation therefore passes through the integral. Horizontal derivatives give the first identity. Terms containing a fibre derivative integrate to zero by the one-dimensional fundamental theorem and compact support. The second identity follows by putting the base differentials first. Under an oriented change of bundle coordinates, the full vertical coefficient acquires precisely the positive fibre Jacobian; terms with an additional base differential do not enter that coefficient. The linear substitution formula consequently makes this local definition independent of the bundle chart. These observations also apply to a pullback bundle and to forms supported properly over its base.

We will use the following direct homotopy calculation. For a smooth map \(H:[0,1]\times N\to N'\), uniquely write
\[
H^*\omega=ds\wedge b_s(\omega)+c_s(\omega),
\qquad K_H\omega=\int_0^1 b_s(\omega)\,ds.
\]
Taking the \(ds\) coefficient in \(dH^*\omega=H^*d\omega\) gives
\[
b_s(d\omega)=\partial_s c_s(\omega)-d_N b_s(\omega).
\]
The fundamental theorem in \(s\) now proves
\[
H_1^*\omega-H_0^*\omega=d_NK_H\omega+K_Hd\omega.
\tag{F.2}
\]
This calculation derives the sign from the chosen order \(ds\wedge b_s\); it does not rely on a choice of sign for a generating vector field.

**Theorem F.1 (a normalized form generates fibre-supported cohomology).** Suppose \(\tau\in\Omega^r_{\mathrm{pr}}(E)\) is closed and \(p_*\tau=1\). Then
\[
[\gamma]\longmapsto[p^*\gamma\wedge\tau]
\]
is an isomorphism from \(H^q_{\mathrm{dR}}(M)\) to \(H^{q+r}(\Omega^*_{\mathrm{pr}}(E))\), with inverse induced by \(p_*\). In particular, any two closed degree-\(r\) forms with proper support and fibre integral one differ by the differential of a properly supported form.

**Proof.** Work on \(E\oplus E\), with projections \(p_1,p_2\) to \(E\). Let \(j:E\to E\) be fibre negation. For \(0\leq s\leq1\), define
\[
a(s)=\frac{1-s}{\sqrt{(1-s)^2+s^2}},\qquad
b(s)=\frac{s}{\sqrt{(1-s)^2+s^2}},
\]
and
\[
H_s(u,v)=(a(s)u+b(s)v,-b(s)u+a(s)v).
\]
The denominator is positive, so this is a smooth family. It preserves \(|u|^2+|v|^2\). Its endpoints are \(H_0(u,v)=(u,v)\) and \(H_1(u,v)=(v,-u)\).

Let \(\alpha\in\Omega^k_{\mathrm{pr}}(E)\) be closed and set
\[
A=p_1^*\alpha\wedge p_2^*(j^*\tau).
\]
The form \(A\) is closed. It is properly supported over \(M\): over a compact base set, its support lies in the product over that set of two compact supports. The family \(H_s^*A\) has a common such compact support. Indeed the two original compact supports have a uniform bound on their fibre norms over that base set, and \(H_s\) preserves the sum of the squares of those norms. Closed bounded disk bundles over a compact base set are compact: choose finitely many local trivializations over relatively compact neighbourhoods and use compact closed pieces of that cover; in each piece the positive metric bounds the coordinate norm above and below. This reduces the assertion to compactness of closed bounded Euclidean sets. Thus the parameter integral \(K_H A\) also has proper support over \(M\), and has proper support for integration along \(p_1\).

Since \(dA=0\), (F.2) gives
\[
p_2^*\alpha\wedge p_1^*\tau
-p_1^*\alpha\wedge p_2^*(j^*\tau)=dK_H A.
\tag{F.3}
\]
Fibre negation has oriented degree \((-1)^r\), so the integral along \(p_1\) of the second term is \((-1)^r\alpha\). For the first term, first move \(p_1^*\tau\) to the left and then move the resulting base pullback \(p^*(p_*\alpha)\) to the left of \(\tau\). When \(k\geq r\), the combined sign is
\[
(-1)^{kr+r(k-r)}=(-1)^r.
\]
Consequently the integral of the first term is \((-1)^r p^*(p_*\alpha)\wedge\tau\). When \(k<r\), both this expression and that fibre integral are zero because \(\alpha\) has insufficient vertical degree.

Applying (F.1) to (F.3) therefore yields the explicit exactness identity
\[
\alpha-p^*(p_*\alpha)\wedge\tau
=d\left((-1)^{r+1}(p_1)_*K_H A\right).
\tag{F.4}
\]
The primitive has proper support over \(M\): its support is contained in the projection of the uniformly compact support just described, locally over each compact base neighbourhood. This proves surjectivity on cohomology. On the other hand, (F.1) and \(p_*\tau=1\) give
\[
p_*(p^*\gamma\wedge\tau)=\gamma,
\]
so the map is injective as well. Taking \(\alpha\) to be another normalized degree-\(r\) form proves the uniqueness assertion. \(\square\)

For rank zero, \(E=M\), the fibre integral is the identity and the degree-zero normalized form is \(1\), so the corresponding statement needs no homotopy construction.

## 5. From a relative primitive to a supported form

Let \(p:E\to M\) be a smooth real vector bundle of positive rank and let \(Z\subset E\) be its zero section. A closed subset \(S\subset E\) has **support proper over the base** if \(S\cap p^{-1}(K)\) is compact for every compact \(K\subset M\). A form has this property when its support does. This is stronger than requiring a compact intersection with each individual fibre.

**Lemma R.1 (relative cutoff).** Let \(e\) be a closed \(r\)-form on \(M\) and let \(\beta\) be an \((r-1)\)-form on \(E\setminus Z\) satisfying \(d\beta=p^*e\). Suppose \(\chi\) is a smooth function on \(E\), equal to one on an open neighbourhood of \(Z\), whose support is proper over the base. Then
\[
U_\chi=\chi p^*e+d\chi\wedge\beta
\]
extends smoothly to all of \(E\), is closed, and has support proper over the base. Its pullback by the zero section is \(e\). For two such functions,
\[
U_{\chi_1}-U_{\chi_0}=d\big((\chi_1-\chi_0)\beta\big),
\]
where the expression in parentheses extends smoothly by zero near \(Z\) and has support proper over the base.

**Proof.** Near every point of \(Z\), the function \(\chi\) is identically one and \(d\chi=0\). Define the second term to be zero there. This agrees on the overlap with its given expression, so the extension is smooth and equals \(p^*e\) near \(Z\). Outside \(Z\), the product rule gives
\[
dU_\chi=d\chi\wedge p^*e-d\chi\wedge d\beta=0.
\]
Near \(Z\), closedness follows from \(de=0\) and commutation of pullback with the differential. The support of \(d\chi\) lies in the support of \(\chi\): wherever \(\chi\) vanishes on an open neighbourhood, so does its derivative. Consequently the support of \(U_\chi\) lies in \(\operatorname{supp}\chi\), which proves the asserted support property. Pulling back the near-zero expression gives \(e\), since, for the zero section \(s:M\to E\), we have \(p\circ s=\mathrm{id}_M\).

For the final assertion, \(\chi_1-\chi_0\) vanishes on an open neighbourhood of \(Z\), so its product with \(\beta\) extends by zero. The product rule and \(d\beta=p^*e\) give the displayed identity. Its support lies in the union of the two cutoff supports. Over a compact base set this is a closed subset of a union of two compact sets, hence compact. \(\square\)

## 6. A real Gaussian family and its supported representative

Let \(p:E\to M\) be an oriented real vector bundle of rank \(r>0\), with a positive metric and a compatible connection. Let \(j:M\to E\) be its zero section. In an oriented orthonormal frame \(e=(e_1,\ldots,e_r)\), use column coordinates:
\[
\nabla(e v)=e(dv+A v),\qquad A^T=-A,\qquad F=dA+A\wedge A.
\tag{G.1}
\]
Then \(F^T=-F\). In fact transposing \(A\wedge A\) reverses the order of two one-forms and gives \(-(A^T\wedge A^T)\). Direct expansion also gives
\[
dF+A\wedge F-F\wedge A=0:
\]
the terms \(dA\wedge A-A\wedge dA\) from \(dF\) cancel the remaining terms. This is the precise Bianchi identity needed below.

### The two exterior degrees

On the total space use the real algebra
\[
\mathcal B=\Omega^*(E)\otimes\Lambda^*p^*E,
\qquad
(\alpha\otimes u)(\beta\otimes v)
=(-1)^{\deg(u)\deg(\beta)}(\alpha\wedge\beta)\otimes(u\wedge v).
\tag{G.2}
\]
Commuting two homogeneous elements produces the sign from the product of their total degrees. This follows by commuting the two ordinary forms and the two exterior-vector factors and adding the two crossing signs in (G.2).

The connection defines an odd derivation \(D\) of total degree one: it acts as \(d\) on scalar forms and as \(De_j=\sum_i A_{ij}e_i\) on the exterior generators. The product rule on these generators defines it everywhere, and the connection transformation law makes it independent of the frame. On an ordinary \(q\)-form times a vector it reads \(D(\alpha v)=d\alpha\,v+(-1)^q\alpha\nabla v\).

Let \(x=\sum_i y_i e_i\) be the tautological vector and set
\[
\theta=Dx=\sum_i\theta_i e_i,
\qquad \theta_i=dy_i+\sum_j A_{ij}y_j,
\qquad
R=\frac12\sum_{i,j}F_{ij}e_i e_j
=\sum_{i<j}F_{ij}e_i e_j.
\tag{G.3}
\]
The notation \(R\) here is the alternating tensor in (G.3), not an unannounced sign convention for the curvature matrix. Both \(x\) and \(\theta\) are intrinsic sections, and \(R\) is the alternating tensor associated to the skew endomorphism \(F\) by the metric. Thus these expressions agree across oriented orthonormal changes of frame.

Define the odd contraction \(\iota_x\) by \(\iota_x e_i=y_i\), \(\iota_x\alpha=0\) for scalar forms, and the total-degree product rule. In particular
\[
\iota_x(\alpha e_i)=(-1)^{\deg\alpha}\alpha y_i.
\]
Let \(T\) extract the coefficient of \(e_1\cdots e_r\). It is globally defined because an oriented orthonormal frame change has determinant one. The connection preserves the oriented unit volume, since its derivative is \(\operatorname{tr}(A)e_1\cdots e_r=0\). Therefore
\[
T\iota_x=0,\qquad dT=TD.
\tag{G.4}
\]
The first identity follows because contraction lowers exterior-vector degree, and no such degree exceeds \(r\).

The identities controlling the calculation are
\[
\begin{aligned}
D|x|^2&=2\sum_i y_i\theta_i,
&\iota_x\theta&=-\sum_i y_i\theta_i,\\
D\theta&=F x,
&\iota_x R&=-F x,\\
DR&=0,
&\iota_x x&=|x|^2.
\end{aligned}
\tag{G.5}
\]
For the first identity the connection terms cancel because \(A\) is skew. The second has the minus sign from moving the contraction past a one-form. Expanding \(D(Dx)\) gives \((dA+A\wedge A)x\). Contracting (G.3) gives \(\sum_{i,j}F_{ij}y_i e_j=-Fx\). Finally the coefficient matrix of \(DR\) is \(dF+AF-FA\), which is zero by (G.1); this also checks explicitly the metric identification used for \(R\).

### Closedness and the parameter derivative

Put
\[
\varepsilon_r=(-1)^{r(r-1)/2}\pi^{r/2},\qquad
S_t=-t^2|x|^2+t\theta-\tfrac12 R,
\]
and define
\[
C_t=\varepsilon_r^{-1}T(e^{S_t}),\qquad
\eta_t=-\varepsilon_r^{-1}T(xe^{S_t})
\quad(t\geq0).
\tag{G.6}
\]
The exponential means the scalar factor \(e^{-t^2|x|^2}\) multiplied by the finite exponential in the nilpotent positive exterior-vector degrees. There are no infinite formal-algebra convergence assumptions. The two terms \(\theta\) and \(R\) have equal ordinary-form and exterior-vector degrees, so \(C_t\) is an \(r\)-form and \(\eta_t\) is an \((r-1)\)-form. All coefficients are real.

**Lemma G.1 (closed family and transgression).** For every \(t\geq0\),
\[
dC_t=0,\qquad \partial_t C_t=-d\eta_t.
\tag{G.7}
\]

**Proof.** The identities (G.5) give
\[
DS_t=-2t^2\sum_i y_i\theta_i+tFx
=2t\iota_x S_t.
\]
Thus the odd derivation \(L_t=D-2t\iota_x\) kills \(S_t\). As \(S_t\) is even, differentiating its finite exponential, together with the ordinary scalar exponential, gives \(L_t(e^{S_t})=0\). Applying (G.4) proves \(dC_t=0\).

Moreover
\[
L_t(xe^{S_t})=(\theta-2t|x|^2)e^{S_t}
=\partial_t e^{S_t}.
\]
Here the possible second product term is zero because \(L_t(e^{S_t})=0\); the minus sign in the odd product rule is consequently accounted for. Applying \(T\), using \(T\iota_x=0\), and inserting the minus sign in the definition of \(\eta_t\) proves the second identity in (G.7). \(\square\)

**Lemma G.2 (normalization and zero-section value).** For \(t>0\),
\[
C_t|_{E_m}=\pi^{-r/2}t^r e^{-t^2|y|^2}\,dy_1\wedge\cdots\wedge dy_r,
\qquad \int_{E_m}C_t=1.
\tag{G.8}
\]
If \(r=2k\), then
\[
C_0=p^*\operatorname{Pf}(F/2\pi),\qquad
j^*C_t=\operatorname{Pf}(F/2\pi).
\tag{G.9}
\]
If \(r\) is odd, both expressions corresponding to (G.9) are zero.

**Proof.** On a fibre, \(\theta_i=dy_i\) and the base curvature vanishes. Extracting the product of the \(r\) terms \(t\,dy_i e_i\) contributes the sign \((-1)^{r(r-1)/2}\), from moving each exterior generator past all later one-forms. Dividing by \(\varepsilon_r\) gives (G.8). Lemma A.5 and one-coordinate scaling in Lemma A.2 give its integral one.

Define the Pfaffian of a skew matrix with commuting entries by
\[
\operatorname{Pf}(B)=[e_1\cdots e_{2k}]
\exp\left(\sum_{i<j}B_{ij}e_i e_j\right).
\tag{G.10}
\]
At \(t=0\), only \(\exp(-R/2)\) remains. Its top coefficient is \((-1/2)^k\operatorname{Pf}(F)\). Since \(\varepsilon_{2k}=(-1)^k\pi^k\), their quotient is \(\operatorname{Pf}(F)/(2\pi)^k\). Pulling back by \(j\) also kills \(x\) and \(\theta\), so gives exactly the same expression for every \(t\). In odd rank the even exterior degrees of \(R\) cannot contribute to the top odd degree. \(\square\)

### The relative primitive and support

On \(E\setminus j(M)\), put
\[
\beta=\int_0^\infty\eta_t\,dt.
\tag{G.11}
\]
This is smooth. On a compact subset disjoint from the zero section, \(|x|\) has a positive lower bound. In a local orthonormal frame, every coefficient of \(\eta_t\), and every fixed number of its coordinate derivatives, is a finite sum of smooth bounded coefficients times a polynomial in \(t\), multiplied by \(e^{-t^2|x|^2}\). Lemma A.4 therefore gives convergence with all derivatives. On those same compact subsets \(C_t\to0\) with all derivatives. Integrating (G.7) and taking the limit gives
\[
d\beta=C_0\quad\text{on }E\setminus j(M).
\tag{G.12}
\]

Choose a smooth function \(f\) with \(f(s)=1\) for \(s\leq1\) and \(f(s)=0\) for \(s\geq4\). Define \(\rho(s)=e^{-1/s^2}\) for \(s>0\) and \(\rho(s)=0\) for \(s\leq0\). This is the flat function denoted \(\eta\) in local-tools Lemma 0.5. An explicit choice is
\[
f(s)=\frac{\rho(4-s)}{\rho(4-s)+\rho(s-1)}.
\]
The denominator is always positive. Set \(\chi=f(|x|^2)\). Its support lies in the radius-two closed disk bundle and is proper over the base, by the compactness argument in Theorem F.1. Lemma R.1 now constructs the smooth closed form
\[
U_\chi=\chi C_0+d\chi\wedge\beta.
\tag{G.13}
\]
It is properly supported, and its zero-section value is (G.9). Its class in properly supported de Rham cohomology is independent of the cutoff.

**Theorem G.3 (a normalized supported representative).** The form \(U_\chi\) has oriented fibre integral one. Consequently it generates fibre-supported de Rham cohomology by Theorem F.1. Its zero-section pullback is \(\operatorname{Pf}(F/2\pi)\) in even rank and zero in odd rank.

**Proof.** It remains to prove the fibre integral, since the other assertions have already been established. Put
\[
b_0=\int_0^1\eta_t\,dt,\qquad
b_1=\int_1^\infty\eta_t\,dt
\quad\text{on }E\setminus j(M).
\]
The first expression is smooth on all of \(E\) by Lemma A.3. The second is smooth off the zero section by Lemma A.4. There
\[
db_0=C_0-C_1,\qquad db_1=C_1.
\]
The form
\[
\Gamma=\chi b_0+(\chi-1)b_1
\tag{G.14}
\]
is smooth on all of \(E\), because its second summand vanishes on a neighbourhood of the zero section. Direct use of the product rule gives
\[
U_\chi-C_1=d\Gamma.
\tag{G.15}
\]

On each fixed fibre, \(\Gamma\) and its derivatives decay as a polynomial times a Gaussian at infinity. The compactly supported \(\chi b_0\) causes no issue. For the tail in \(b_1\), and for \(|y|\geq1,t\geq1\), use
\[
e^{-t^2|y|^2}\leq e^{-|y|^2/2}e^{-t^2/2}.
\]
Every derivative of its coefficient has only additional polynomial factors in \((y,t)\). Lemma A.4 integrates the \(t\)-factor and leaves a polynomial Gaussian bound in \(y\). The conclusion following that lemma shows that the integral of the vertical top-degree differential \(d\Gamma\) is zero. Equation (G.15) and Lemma G.2 therefore give \(\int_{E_m}U_\chi=\int_{E_m}C_1=1\). This proves the theorem. \(\square\)

For rank zero, the normalized form, zero-section pullback and empty Pfaffian are all \(1\), so no Gaussian construction is required.

## 7. Relative forms and support near the zero section

### The relative complex

For an open subset \(V\subset N\), set
\[
\Omega^q(N,V)=\Omega^q(N)\oplus\Omega^{q-1}(V),\qquad
D(\alpha,\beta)=(d\alpha,\alpha|_V-d\beta).
\tag{H.1}
\]
Forms of negative degree are zero. Since restriction commutes with \(d\), applying \(D\) twice gives \((0,d\alpha|_V-d\alpha|_V)=0\). Thus closed pairs modulo differentials define groups denoted \(H^q_{\mathrm{dR}}(N,V)\). This notation refers to this explicitly defined complex until the comparison with relative singular cohomology is proved.

**Lemma H.1 (relative exactness).** Projection, restriction and insertion give an exact sequence
\[
\cdots\longrightarrow H^{q-1}_{\mathrm{dR}}(V)
\xrightarrow{\delta}H^q_{\mathrm{dR}}(N,V)
\xrightarrow{j}H^q_{\mathrm{dR}}(N)
\xrightarrow{r}H^q_{\mathrm{dR}}(V)
\xrightarrow{\delta}H^{q+1}_{\mathrm{dR}}(N,V)
\longrightarrow\cdots,
\tag{H.2}
\]
where \(\delta[\beta]=[(0,\beta)]\), \(j[\alpha,\beta]=[\alpha]\), and \(r[\alpha]=[\alpha|_V]\).

**Proof.** A closed \(\beta\) gives a closed pair \((0,\beta)\). If \(\beta=d\gamma\), this pair is \(D(0,-\gamma)\), so \(\delta\) is well defined. The other maps respect closed forms and differentials by (H.1) and Lemma D.1.

At \(H^q_{\mathrm{dR}}(N,V)\), a class in the kernel of \(j\) has \(\alpha=d\gamma\). Subtract \(D(\gamma,0)\): the class is represented by \((0,\beta-\gamma|_V)\), and its second component is closed because the pair is. It is therefore in the image of \(\delta\). Every class in that image has first component zero, proving the reverse inclusion.

At \(H^q_{\mathrm{dR}}(N)\), the image of \(j\) restricts to an exact form because a closed pair obeys \(\alpha|_V=d\beta\). Conversely, if a closed \(\alpha\) restricts to \(d\beta\), the pair \((\alpha,\beta)\) is closed and maps to its class. This proves exactness there.

At \(H^q_{\mathrm{dR}}(V)\), insertion of the restriction of a closed \(\gamma\) is \((0,\gamma|_V)=D(\gamma,0)\), hence zero in cohomology. Conversely, if \((0,\beta)=D(\gamma,\zeta)\), then \(d\gamma=0\) and \(\beta=\gamma|_V-d\zeta\), so \([\beta]\) is the restriction of \([\gamma]\). These three checks hold in every degree and prove (H.2). \(\square\)

For a form \(\eta\) on \(N\) of degree \(a\), define its action on the pair complex by
\[
\eta\cdot(\alpha,\beta)
=\bigl(\eta\wedge\alpha,(-1)^a\eta|_V\wedge\beta\bigr).
\tag{H.3}
\]
The sign is necessary with (H.1). Indeed a direct product-rule calculation gives
\[
D\bigl(\eta\cdot(\alpha,\beta)\bigr)
=d\eta\cdot(\alpha,\beta)+(-1)^a\eta\cdot D(\alpha,\beta).
\tag{H.4}
\]
For the second component the two sides are both
\[
\eta|_V\wedge\alpha|_V
-(-1)^a d\eta|_V\wedge\beta-\eta|_V\wedge d\beta.
\]
The first component is the ordinary product rule. If the inputs are closed, changing either by a differential therefore changes their product by a differential. This defines the indicated action in cohomology.

### Comparing relative and properly supported forms

Let \(p:E\to M\) be a smooth real vector bundle of positive rank, \(Z\) its zero section and \(V=E\setminus Z\). Choose a positive metric and a smooth cutoff \(\chi\) equal to one near \(Z\), with support proper over \(M\), as constructed before (G.13). Define
\[
J_\chi:\Omega^*(E,V)\longrightarrow\Omega^*_{\mathrm{pr}}(E),
\qquad J_\chi(\alpha,\beta)=\chi\alpha+d\chi\wedge\beta.
\tag{H.5}
\]
The second term extends by zero near \(Z\); the image is properly supported. The product rule gives
\[
dJ_\chi(\alpha,\beta)
=\chi d\alpha+d\chi\wedge(\alpha-d\beta)
=J_\chi D(\alpha,\beta),
\tag{H.6}
\]
so this is a map of complexes. Formula (H.3) and moving \(d\chi\) past the degree-\(a\) form show that it respects multiplication by forms pulled back from the base.

We construct an inverse in cohomology explicitly. Write
\[
h:[1,\infty)\times V\longrightarrow V,\qquad h(t,v)=tv,
\]
and, for a form \(\omega\) to which the following integral applies, write
\[
h^*\omega=dt\wedge b_t(\omega)+c_t(\omega),\qquad
B\omega=-\int_1^\infty b_t(\omega)\,dt.
\tag{H.7}
\]
We will apply this to forms which vanish whenever the fibre norm is sufficiently large locally over each compact base set. Every properly supported form on \(E\) has that property. The form \(\chi\beta\) on \(V\) does too, even when \(\beta\) is singular towards \(Z\).

For each compact set in \(V\), the fibre norm has a positive minimum \(\epsilon\), and its image in the base is compact. Let \(R\) be a bound beyond which \(\omega\) vanishes over a compact base neighbourhood. For \(t>R/\epsilon\), the point \(tv\) lies outside its support. The pullback and all of its coefficients thus vanish there. Locally on \(V\), (H.7) is an integral over a finite parameter interval, giving a smooth form by Lemma A.3. All its derivatives can be calculated under that integral. Applying (F.2) on \([1,T]\), and then taking \(T\) above this local bound, gives
\[
dB\omega+B(d\omega)=\omega\quad\text{on }V.
\tag{H.8}
\]
This argument proves the formula for the indicated class of forms directly. It makes no assertion about (H.7) for arbitrary forms without the support condition.

**Theorem H.2 (relative/support isomorphism).** The map induced by \(J_\chi\) is an isomorphism
\[
H^q_{\mathrm{dR}}(E,E\setminus Z)
\longrightarrow H^q(\Omega^*_{\mathrm{pr}}(E)).
\tag{H.9}
\]
It is independent of the cutoff and is compatible with the action of \(H^*_{\mathrm{dR}}(M)\).

**Proof.** If \(\omega\) is properly supported on \(E\), (H.8) gives a map of complexes
\[
I\omega=(\omega,B\omega),
\qquad DI\omega=(d\omega,\omega-dB\omega)
=(d\omega,Bd\omega)=I(d\omega).
\tag{H.10}
\]
Here \(B\omega\) is a form on \(V\), as required.

First let \(\omega\) be closed. Since \(dB\omega=\omega|_V\),
\[
J_\chi I\omega-\omega
=(\chi-1)\omega+d\chi\wedge B\omega
=d\bigl((\chi-1)B\omega\bigr).
\tag{H.11}
\]
The primitive extends smoothly by zero near \(Z\). It has support proper over \(M\). To check this last point, fix a compact base set and a compact neighbourhood of it. Proper support bounds the original form's fibre norm there by some \(R\). If \(|v|>R\), then \(\omega(tv)=0\) for all \(t\geq1\), so \(B\omega=0\) on that outer region. Multiplication by \(\chi-1\) has removed the only possible singularity at \(Z\), and its support is a closed subset of a bounded disk bundle over the compact set. Such a disk bundle is compact by the argument in Theorem F.1. This proves that (H.11) is exact in the properly supported complex.

Conversely let \((\alpha,\beta)\) be a closed relative pair and write \(U=J_\chi(\alpha,\beta)\). On \(V\), \(d\beta=\alpha\), so \(U=d(\chi\beta)\). Formula (H.8), applied to the radially bounded form \(\chi\beta\), gives
\[
BU=Bd(\chi\beta)=\chi\beta-dB(\chi\beta).
\]
Let \(\gamma=(\chi-1)\beta\), extended smoothly by zero near \(Z\), and let \(\zeta=B(\chi\beta)\) on \(V\). Then
\[
I J_\chi(\alpha,\beta)-(\alpha,\beta)
=(U-\alpha,BU-\beta)
=D(\gamma,\zeta).
\tag{H.12}
\]
Indeed the first component is \(d\gamma\), and the second is \((\chi-1)\beta-d\zeta\), exactly as in (H.1). These two calculations prove that the induced maps are inverse.

For two cutoffs and a closed pair, the same product calculation gives
\[
J_{\chi_1}(\alpha,\beta)-J_{\chi_0}(\alpha,\beta)
=d\bigl((\chi_1-\chi_0)\beta\bigr).
\]
The primitive is smooth across \(Z\) and properly supported in the union of their supports, as in Lemma R.1. Thus the map is cutoff independent. Compatibility with the base action was already checked immediately after (H.6). \(\square\)

**Corollary H.3 (the relative de Rham Thom class).** For an oriented rank-\(r\) bundle, the Gaussian pair \((C_0,\beta)\) from (G.11)–(G.12) defines the unique relative de Rham class whose image under (H.9) has fibre integral one. Multiplication by this class, using (H.3) with base pullback, is an isomorphism
\[
H^q_{\mathrm{dR}}(M)\longrightarrow
H^{q+r}_{\mathrm{dR}}(E,E\setminus Z).
\tag{H.13}
\]
Its pullback to the zero section after forgetting the relative component is the Pfaffian form class in even rank and zero in odd rank.

**Proof.** Equations (G.7) and (G.12) make the pair closed. Its image under \(J_\chi\) is the normalized form \(U_\chi\) of Theorem G.3. Theorem F.1 proves the properly supported Thom isomorphism and uniqueness, and Theorem H.2 transfers these assertions to the relative complex, respecting the base action. The first component is \(C_0\), whose zero-section pullback is computed in Lemma G.2. \(\square\)

For rank zero, \(E=M\), \(V\) is empty, the relative complex is \(\Omega^*(M)\), and all these maps reduce to the identity with Thom class \(1\).

## 8. Good covers and the Čech comparison for differential forms

Our manifolds are finite dimensional, Hausdorff, second countable, smooth and without boundary. The earlier programme lesson *Local tools for bundles and transport* supplies compactness and elementary calculus in Lemmas 0.0–0.3, compact exhaustion in Lemma 3.A, a locally finite subordinate atlas in Lemma 3.B, and smooth partitions in Theorem 3.1. Earlier in this chapter, Lemma D.1 supplies exterior calculus, Lemma A.3 supplies smooth parameter integration, and (F.2) proves the differential-form homotopy identity. Those are the proof dependencies of this chapter.

### Coordinate construction of a good cover

A **good cover** is an open cover such that every nonempty intersection of finitely many members is diffeomorphic to a nonempty convex open subset of Euclidean space. The diffeomorphism may depend on the intersection. Repeated members do not change an intersection.

**Theorem Q.1 (arbitrarily fine good covers).** Given any open cover of a manifold \(M\), there is a countable, locally finite good cover refining it. Each cover member can be chosen relatively compact.

**Proof.** The empty manifold has the empty cover. A zero-dimensional manifold is discrete: a chart domain is a singleton. Second countability makes its set of points countable, since each singleton must occur in any basis. Its singleton cover has all the asserted properties. We henceforth work in positive dimension.

Use local-tools Lemma 3.B on the given cover. Write \((\Omega_j,\phi_j)\) for its countable locally finite atlas and \(\Omega'_j\) for its smaller coordinate balls. Thus
\[
\overline{\Omega'_j}\subset\Omega_j,\qquad
\overline{\Omega'_j}\text{ is compact},\qquad
\bigcup_j\Omega'_j=M,
\tag{Q.1}
\]
and each \(\Omega_j\) lies in a member of the prescribed cover. The family of closed sets \(\overline{\Omega'_j}\) is locally finite because each is contained in its corresponding \(\Omega_j\).

Fix \(a\in M\) and choose \(j\) with \(a\in\Omega'_j\). Let
\[
J_a=\{k:a\in\overline{\Omega'_k}\}.
\]
This is a finite set, and \(a\in\Omega_k\) for every \(k\in J_a\). There is an open neighbourhood \(V_a\) of \(a\), as small as desired, with
\[
V_a\subset\Omega'_j\cap\bigcap_{k\in J_a}\Omega_k,\qquad
V_a\cap\Omega'_k=\varnothing\quad(k\notin J_a).
\tag{Q.2}
\]
To prove this, first take a neighbourhood meeting only finitely many closed sets \(\overline{\Omega'_k}\). Remove the finitely many such closed sets that do not contain \(a\). Intersect the resulting neighbourhood with the finitely many open sets in the first assertion, and with any additional prescribed neighbourhood of \(a\).

For each \(k\in J_a\), set \(z_k=\phi_k(a)\) and define, on \(\phi_k(V_a)\),
\[
f_{a,k}(z)=\left|\phi_j\bigl(\phi_k^{-1}(z)\bigr)-\phi_j(a)\right|^2.
\]
The chain rule gives
\[
\operatorname{Hess}_{z_k}f_{a,k}
=2T_{a,k}^{\,T}T_{a,k},\qquad
T_{a,k}=D(\phi_j\circ\phi_k^{-1})_{z_k}.
\tag{Q.3}
\]
The terms containing second derivatives of the transition map vanish at \(z_k\), since they are multiplied by the transition map's value minus \(\phi_j(a)\). Differentiating the inverse transition identities shows that \(T_{a,k}\) is invertible. Thus (Q.3) is positive on nonzero vectors.

It is uniformly positive on the unit sphere. That sphere is compact by local-tools Lemma 0.1. A continuous positive function on a compact set has a positive minimum: its image is bounded by a finite subcover of neighbourhoods on which it is bounded; take points approaching its infimum, take a convergent subsequence and use continuity to attain that infimum. Apply this to \(u\mapsto2|T_{a,k}u|^2\), and call its minimum \(m_k>0\). Continuity of the finitely many Hessian entries supplies a neighbourhood of \(z_k\) where
\[
u^T\operatorname{Hess}_zf_{a,k}u\geq\tfrac12m_k|u|^2.
\tag{Q.4}
\]
Indeed, if each entry changes by less than \(m_k/(2n)\), the quadratic form changes by at most \(m_k|u|^2/2\), since \((\sum_i|u_i|)^2\leq n|u|^2\).

Choose an open Euclidean ball \(D_{a,k}\) about \(z_k\), with closure inside \(\phi_k(V_a)\), on which (Q.4) holds. These are **convex ambient domains** for the respective functions. Choose \(\epsilon>0\) so small that the closed \(\phi_j\)-coordinate ball of radius \(\epsilon\) about \(\phi_j(a)\) lies in
\[
\phi_j\left(\bigcap_{k\in J_a}\phi_k^{-1}(D_{a,k})\right).
\]
This set is an open neighbourhood of \(\phi_j(a)\), so such a closed ball exists. Put
\[
U_a=\phi_j^{-1}\bigl(B(\phi_j(a),\epsilon)\bigr),
\tag{Q.5}
\]
where \(B\) denotes an open ball in this chapter. Its closure is compact and lies in \(V_a\). For each \(k\in J_a\),
\[
\phi_k(U_a)=\{z\in D_{a,k}:f_{a,k}(z)<\epsilon^2\}.
\tag{Q.6}
\]
Both inclusions follow from the definition of \(f_{a,k}\), from \(D_{a,k}\subset\phi_k(V_a)\), and from the containment of \(U_a\) in every \(\phi_k^{-1}(D_{a,k})\).

The right side of (Q.6) is convex. A segment between two points of \(D_{a,k}\) stays in that ball. Along it, the second derivative of \(f_{a,k}\) is nonnegative by (Q.4), so its first derivative is nondecreasing by the fundamental theorem. For \(0<t<1\), the average derivative on \([0,t]\) is at most the average derivative on \([t,1]\). Multiplying that inequality by \(t(1-t)\) and rearranging gives
\[
f_{a,k}((1-t)z+tw)\leq(1-t)f_{a,k}(z)+tf_{a,k}(w).
\]
Thus endpoint values less than \(\epsilon^2\) imply the same strict inequality all along the segment.

We have constructed an arbitrarily small \(U_a\subset\Omega'_j\) with this property: whenever \(U_a\) meets \(\Omega'_k\), it is contained in \(\Omega_k\) and its \(\phi_k\)-image is convex. Indeed, (Q.2) forces \(k\in J_a\), so (Q.6) applies. For a finite nonempty intersection \(U_{a_0}\cap\cdots\cap U_{a_p}\), choose the index \(j_0\) used for \(U_{a_0}\). Every other member meets \(\Omega'_{j_0}\) at a point of this intersection. All the members are therefore contained in \(\Omega_{j_0}\) and have convex images there. Their intersection has a convex open image in that one chart.

To arrange local finiteness, let \(K_n\subset\operatorname{int}K_{n+1}\), \(n\geq0\), be the compact exhaustion of local-tools Lemma 3.A, and put \(K_{-1}=K_{-2}=\varnothing\). The compact layer
\[
L_n=K_n\setminus\operatorname{int}K_{n-1}
\]
lies in \(\operatorname{int}K_{n+1}\setminus K_{n-2}\). For each \(a\in L_n\), make the preceding construction with \(V_a\) additionally contained in that open set. Choose finitely many resulting \(U_a\)'s covering \(L_n\). These finite families form a countable cover of \(M\): every point first enters some \(K_n\) and therefore belongs to \(L_n\). A neighbourhood \(\operatorname{int}K_N\) meets no selected member from a layer \(n\geq N+2\), because such a member misses \(K_{n-2}\supset K_N\). Only finitely many earlier selections remain. Every point belongs to some \(\operatorname{int}K_N\), so this proves local finiteness. The finite-intersection property already proved applies to any selection of our constructed sets. Subordination and relative compactness follow from (Q.1) and (Q.5). □

**Lemma Q.2 (forms on a convex set).** If a nonempty open set \(V\) is diffeomorphic to a convex open set, its de Rham cohomology is \(\mathbb R\) in degree zero and zero in positive degrees. The degree-zero isomorphism is inclusion of constant functions.

**Proof.** Work in convex coordinates, choose \(a\in V\), and use \(H(t,x)=a+t(x-a)\). Let \(K\omega\) be the integral of the \(dt\)-coefficient of \(H^*\omega\), as in (F.2). The resulting form is smooth: for a compact coordinate neighbourhood of \(x\), its product with \([0,1]\) has compact image inside \(V\), so the parameter-integration proof of Lemma A.3 applies to each coefficient. Formula (F.2) gives
\[
\omega-H_0^*\omega=dK\omega+Kd\omega.
\tag{Q.7}
\]
In positive degree \(H_0^*\omega=0\), so a closed form is \(dK\omega\). For a function, (Q.7) says \(f-f(a)=Kdf\); a function with \(df=0\) is therefore constant. There are no forms of negative degree and hence no exact nonzero constants. Pullback by the coordinate diffeomorphism and its inverse transfers the result to the original set. □

### A finite-diagonal comparison argument

A cochain complex is a sequence of abelian groups and degree-one homomorphisms whose square is zero. Its cohomology in degree \(n\) is the kernel in that degree modulo the image from degree \(n-1\). All complexes here are zero in negative degrees.

**Lemma Q.3 (two augmentations).** Let \(C^{p,q}\), \(p,q\geq0\), have commuting differentials
\[
\delta:C^{p,q}\longrightarrow C^{p+1,q},\qquad
d:C^{p,q}\longrightarrow C^{p,q+1},\qquad
\delta^2=d^2=0,\quad\delta d=d\delta.
\]
Set
\[
\operatorname{Tot}^nC=\bigoplus_{p+q=n}C^{p,q},\qquad
D|_{C^{p,q}}=\delta+(-1)^p d.
\tag{Q.8}
\]
Suppose a complex \(K^*\) augments the rows by exact sequences
\[
0\longrightarrow K^q\xrightarrow{a}C^{0,q}
\xrightarrow{\delta}C^{1,q}\xrightarrow{\delta}\cdots,\qquad
da=a\,d_K.
\tag{Q.9}
\]
Then \(a:K^*\to\operatorname{Tot}^*C\) induces a cohomology isomorphism. If a complex \(L^*\) augments the columns by exact sequences
\[
0\longrightarrow L^p\xrightarrow{b}C^{p,0}
\xrightarrow d C^{p,1}\xrightarrow d\cdots,\qquad
\delta b=b\,d_L,
\tag{Q.10}
\]
then \(b:L^*\to\operatorname{Tot}^*C\) also induces a cohomology isomorphism. The isomorphisms commute with maps of the displayed complexes and augmentations.

**Proof.** The mixed terms in \(D^2\) have coefficients \((-1)^p\) and \((-1)^{p+1}\), so \(D^2=0\). The augmentation identities make \(a,b\) cochain maps.

For the row assertion, take a total cocycle \(c\) of degree \(n\). If its largest nonzero horizontal index is \(p>0\), the component of \(Dc=0\) in \(C^{p+1,n-p}\) says \(\delta c^{p,n-p}=0\), since no component of \(c\) has horizontal index \(p+1\). Row exactness gives \(v\in C^{p-1,n-p}\) with \(\delta v=c^{p,n-p}\). Replace \(c\) by \(c-Dv\). This removes that component and only changes the component with horizontal index \(p-1\). After at most \(n\) steps, only \(c^{0,n}\) remains. The cocycle equations say \(\delta c^{0,n}=0\) and \(dc^{0,n}=0\). It equals \(ak\) for a unique \(k\in K^n\), and \(d_Kk=0\) by injectivity of \(a\). This proves surjectivity on cohomology.

For injectivity, suppose \(ak=Dv\), where \(v\) has total degree \(n-1\). If \(v\)'s largest horizontal index \(p\) is positive, the component of \(Dv\) at index \(p+1\) vanishes, so \(\delta v^{p,n-1-p}=0\). Find \(w\in C^{p-1,n-1-p}\) with \(\delta w=v^{p,n-1-p}\) and replace \(v\) by \(v-Dw\). This preserves \(Dv\) and lowers its largest horizontal index. At the end \(v\in C^{0,n-1}\), and the horizontal component of \(Dv=ak\) says \(\delta v=0\). Hence \(v=ah\), giving \(ak=a\,d_Kh\), so \(k=d_Kh\). In degree zero there is no total primitive, so injectivity follows directly from that of \(a\).

For the column assertion, remove the largest positive vertical index \(q\) of a cocycle, with \(p=n-q\). The component of \(Dc=0\) in \(C^{p,q+1}\) is \((-1)^pdc^{p,q}=0\), since all higher vertical components vanish. Column exactness gives \(v\in C^{p,q-1}\) with \((-1)^pdv=c^{p,q}\). Subtracting \(Dv\) removes this component and only adds one at vertical index \(q-1\). At the end \(c\in C^{n,0}\); its equations give \(dc=0\), hence \(c=b\ell\), and then \(d_L\ell=0\). This proves surjectivity. If \(b\ell=Dv\), perform the same largest-vertical-index elimination on \(v\), subtracting \(Dw\) at each stage. The resulting \(v\in C^{n-1,0}\) satisfies \(dv=0\), so \(v=bh\) and \(\ell=d_Lh\). Degree zero again follows from injectivity of the augmentation.

All eliminations involve finitely many bidegrees, even if individual groups are infinite products. Finally, a map of the displayed data commutes with the augmentations themselves and hence with their induced cohomology maps. Composing the resulting equality with inverses of these bijections proves the same assertion for their inverses. No natural choice of primitives is required. □

### The Čech complex and its product

Fix a good cover \(\mathcal U=(U_i)_{i\in I}\) from Theorem Q.1, and write \(U_{i_0\ldots i_p}=U_{i_0}\cap\cdots\cap U_{i_p}\). Use all ordered tuples, including repetitions, without an alternating condition. Define
\[
C^{p,q}(\mathcal U)=\prod_{(i_0,\ldots,i_p)\in I^{p+1}}
\Omega^q(U_{i_0\ldots i_p}),
\tag{Q.11}
\]
with zero vector space for an empty intersection. Restriction to the common intersection is understood in every formula. Put
\[
(\delta c)_{i_0\ldots i_{p+1}}
=\sum_{k=0}^{p+1}(-1)^k c_{i_0\ldots\widehat{i_k}\ldots i_{p+1}}.
\tag{Q.12}
\]
Deleting two distinct positions \(k<l\) in either order produces the same restriction, with opposite signs \((-1)^{k+l-1}\) and \((-1)^{k+l}\). Thus \(\delta^2=0\), including for repeated entries. The componentwise exterior derivative commutes with restrictions and hence with \(\delta\). This gives the data of (Q.8).

Let \(\check C^p(\mathcal U;\mathbb R)\) be the product of one copy of \(\mathbb R\) for each nonempty \(U_{i_0\ldots i_p}\), with differential (Q.12). These are **constant Čech cochains**. Denote their cohomology by \(\check H^*(\mathcal U;\mathbb R)\). There are augmentations
\[
a\colon \Omega^*(M)\longrightarrow\operatorname{Tot}^*C(\mathcal U),
\quad(a\omega)_i=\omega|_{U_i},\qquad
b\colon \check C^*(\mathcal U;\mathbb R)\longrightarrow\operatorname{Tot}^*C(\mathcal U),
\tag{Q.13}
\]
where \(b\) regards each coefficient as a constant function in bidegree \((p,0)\).

**Theorem Q.4 (natural Čech–de Rham ring comparison).** Both maps in (Q.13) induce cohomology isomorphisms. With the product
\[
(u\smile v)_{i_0\ldots i_{p+r}}
=u_{i_0\ldots i_p}v_{i_p\ldots i_{p+r}},
\qquad u\in\check C^p,\quad v\in\check C^r,
\tag{Q.14}
\]
the resulting isomorphism
\[
\Theta_{\mathcal U}=H(b)^{-1}H(a):
H^*_{\mathrm{dR}}(M)\longrightarrow\check H^*(\mathcal U;\mathbb R)
\tag{Q.15}
\]
preserves products and the unit. It is compatible with smooth pullbacks and good-cover refinements. In particular, the Čech cohomology product is graded commutative.

**Proof.** Choose a smooth subordinate partition of unity by local-tools Theorem 3.1. It may initially give functions \(\psi_\lambda\) with a chosen cover index \(i(\lambda)\) for each support. Set
\[
\rho_i=\sum_{i(\lambda)=i}\psi_\lambda.
\]
The sums are locally finite. The support of \(\rho_i\) lies in the union of the supports occurring in its sum. This union is contained in \(U_i\) and is closed: a locally finite union of closed sets is closed, since at any point outside the union one can take a neighbourhood meeting finitely many members and remove those finitely many closed sets. Thus \(\operatorname{supp}\rho_i\subset U_i\). The grouped family is locally finite, smooth, nonnegative and has sum one.

For \(c\in C^{p,q}\) and \(p\geq1\), define
\[
(hc)_{i_0\ldots i_{p-1}}=\sum_j\rho_jc_{j i_0\ldots i_{p-1}}.
\tag{Q.16}
\]
For \(p=0\), define \(hc=\sum_j\rho_jc_j\in\Omega^q(M)\). Each term extends smoothly by zero outside \(U_j\), since its multiplying function has support contained in \(U_j\). Local finiteness makes the sums smooth. In every degree \(p\geq0\), substitution gives
\[
(h\delta c)_{i_0\ldots i_p}
=\sum_j\rho_j\left(c_{i_0\ldots i_p}
+\sum_{k=0}^p(-1)^{k+1}c_{j i_0\ldots\widehat{i_k}\ldots i_p}\right)
=c_{i_0\ldots i_p}-(\delta hc)_{i_0\ldots i_p}.
\tag{Q.17}
\]
At \(p=0\), \(\delta h\) means the augmentation \(ah\). Also \(ha\omega=\sum_j\rho_j\omega=\omega\). Thus all augmented rows are exact. Lemma Q.2 makes every augmented column exact, with its explicit homotopy primitive on each nonempty intersection. Both isomorphism assertions follow from Lemma Q.3.

For \(\alpha\in C^{p,q}\), \(\beta\in C^{r,s}\), put
\[
(\alpha\star\beta)_{i_0\ldots i_{p+r}}
=(-1)^{qr}\alpha_{i_0\ldots i_p}\wedge\beta_{i_p\ldots i_{p+r}},
\tag{Q.18}
\]
and extend bilinearly to total degrees. With a third bidegree \((t,u)\), the two bracketings give the same three factors with signs
\[
qr+(q+s)t=st+q(r+t).
\]
Thus the product is associative. The family of constant functions \(1\) in \(C^{0,0}\) is its unit.

Write \(\alpha\diamond\beta\) for (Q.18) without its sign. Expanding (Q.12) gives
\[
\delta(\alpha\diamond\beta)
=(\delta\alpha)\diamond\beta+(-1)^p\alpha\diamond\delta\beta.
\tag{Q.19}
\]
Deletions of positions \(0,\ldots,p\) occur in the first summand and deletions of positions \(p+1,\ldots,p+r+1\) in the second. The two additional joining-position terms are
\[
(-1)^{p+1}\alpha_{i_0\ldots i_p}\wedge\beta_{i_{p+1}\ldots i_{p+r+1}}
\quad\text{and}\quad
(-1)^p\alpha_{i_0\ldots i_p}\wedge\beta_{i_{p+1}\ldots i_{p+r+1}},
\]
which cancel. This accounts for every term. The exterior product rule of Lemma D.1 also gives
\[
d(\alpha\diamond\beta)
=(d\alpha)\diamond\beta+(-1)^q\alpha\diamond d\beta.
\]
Together with (Q.8) and (Q.18), these identities imply
\[
D(\alpha\star\beta)=(D\alpha)\star\beta
+(-1)^{p+q}\alpha\star D\beta.
\tag{Q.20}
\]
Explicitly, the exponents for the four terms involving \(\delta\alpha,d\alpha,\delta\beta,d\beta\) are, in that order,
\[
qr,\qquad p+r+qr,\qquad p+qr,\qquad p+q+r+qr
\]
on both sides.

The product therefore descends to cohomology. Equation (Q.20) says a product of cocycles is closed. For closed \(y\), replacing a closed first factor by itself plus \(Dx\) changes the product by \(D(x\star y)\). For closed \(x\), replacing its closed second factor by itself plus \(Dz\) changes the product by \((-1)^{\deg x}D(x\star z)\). Changing representatives successively proves independence of both choices. The augmentation \(a\) preserves wedge products and the unit; \(b\), being concentrated in form degree zero, preserves (Q.14) and the unit. Their cohomology isomorphisms and inverses are ring homomorphisms, proving the ring assertion. Graded commutativity follows from that of wedge products and surjectivity of \(\Theta_{\mathcal U}\). This is a statement on cohomology, not on the Čech cochain product.

Let \(f:N\to M\) be smooth. Theorem Q.1 gives a good cover \(\mathcal V=(V_j)\) refining \(f^{-1}\mathcal U\). Choose \(r(j)\) with \(V_j\subset f^{-1}(U_{r(j)})\), and set
\[
(f_r^*c)_{j_0\ldots j_p}
=f^*(c_{r(j_0)\ldots r(j_p)})|_{V_{j_0\ldots j_p}}.
\tag{Q.21}
\]
The all-tuples convention makes this valid even when indices repeat or their order changes. The formula commutes with \(\delta,d,\star\) and both augmentations. Lemma Q.3 yields
\[
H(f_r^*)\Theta_{\mathcal U}=\Theta_{\mathcal V}f^*.
\tag{Q.22}
\]
The right side is independent of \(r\), so the induced cohomology map is also independent of \(r\). Two good refinements admit a common good refinement by Theorem Q.1 applied to their intersections. Taking \(f\) to be the identity in (Q.22) identifies both comparisons through the same de Rham groups. For successive smooth maps, use a further common good refinement; equality of their pullbacks on forms and (Q.22) prove compatibility with composition. □

## 9. Singular chains, small simplices and smooth comparison

### Smooth and continuous cohomology through the same good cover

**Theorem K.6 (singular Čech comparison and smooth restriction).** Let \(M\) be a manifold and \(\mathcal U\) a good cover as in Theorem Q.1. For every commutative unital coefficient ring \(R\), both ordinary and smooth singular cohomology are naturally isomorphic as unital graded rings to \(\check H^*(\mathcal U;R)\). Under these isomorphisms, restriction
\[
H^*(M;R)\longrightarrow H^*_\infty(M;R)
\tag{K.20}
\]
is the identity on the Čech model and is therefore a ring isomorphism. The comparisons commute with smooth maps and good-cover refinements.

**Proof.** Write a symbol \(\bullet\) for either the continuous or the smooth choice of simplices, and form
\[
B_\bullet^{p,q}
=\prod_{(i_0,\ldots,i_p)}C_\bullet^q(U_{i_0\ldots i_p};R).
\tag{K.21}
\]
Use the Čech differential \(\delta\) from (Q.12), the componentwise singular differential \(d_s\), and the total differential \(\delta+(-1)^p d_s\). The two componentwise differentials commute, since restrictions commute with simplex boundaries. Empty intersections contribute zero.

The augmented rows start with cochains on \(\mathcal U\)-small simplices of \(M\), mapping to the restrictions on each \(U_i\). We prove their exactness directly. Enumerate the cover indices. For any small simplex \(\sigma\), let \(j(\sigma)\) be the least cover index containing its image. For \(c\in B_\bullet^{p,q}\), \(p\geq1\), define the value of \(hc\) on a simplex \(\sigma\) with image in \(U_{i_0\ldots i_{p-1}}\) by
\[
(hc)_{i_0\ldots i_{p-1}}(\sigma)
=c_{j(\sigma),i_0,\ldots,i_{p-1}}(\sigma).
\tag{K.22}
\]
The right side is defined since the image lies in all its indexed opens. At \(p=0\), set \(hc(\sigma)=c_{j(\sigma)}(\sigma)\), a global small cochain. In computing \(h\delta+\delta h\), the simplex stays fixed, so its chosen index stays fixed. The index-deletion calculation of (Q.17), with that single index replacing the weighted sum, gives \(h\delta+\delta h=\operatorname{id}\), including the row augmentation. Also \(ha=\operatorname{id}\) on the augmented small-cochain group. This proves row exactness. There is no requirement that this contraction commute with \(d_s\).

The augmented columns start with \(\check C^p(\mathcal U;R)\), regarded as constant degree-zero singular cochains on each intersection. Their exactness is exactly Lemma DG06 K.4, because each nonempty intersection is smoothly contractible. Lemma Q.3 now gives cohomology isomorphisms from both small cochains and constant Čech cochains to \(\operatorname{Tot}B_\bullet\). Combined with Lemma DG06 K.4 for small-chain restriction, they give the asserted additive comparison.

On this total complex define
\[
(\alpha\star\beta)_{i_0\ldots i_{p+r}}
=(-1)^{qr}
\alpha_{i_0\ldots i_p}\smile\beta_{i_p\ldots i_{p+r}},
\qquad
\alpha\in B_\bullet^{p,q},\quad\beta\in B_\bullet^{r,s}.
\tag{K.23}
\]
The calculations (Q.18)–(Q.20) apply without change: they use only associativity, restriction compatibility and a degree-one differential obeying the graded product rule, all proved for \(\smile\) in Lemma DG06 K.5. Thus this is an associative unital differential graded algebra. The two augmentations preserve products and the unit. On the constant degree-zero singular factors, cup product multiplies the constants, giving exactly the Čech product (Q.14) with coefficients \(R\). On global small cochains, the augmentation is restriction and preserves cup products by (DG06 K.18). Consequently both augmentation isomorphisms, and the small-chain isomorphism, are ring isomorphisms.

Restriction from continuous to smooth cochains gives a map between the two double complexes, compatible with both augmentations and equal to the identity on their constant Čech complexes. The induced map on total cohomology is an isomorphism: after composing with the isomorphism from the constant complex on either side, it becomes the identity. The same commuting augmentation maps then show that (K.20) is an isomorphism and is the identity under the displayed Čech identifications.

For a smooth map \(f:N\to M\), choose a good cover of \(N\) refining \(f^{-1}\mathcal U\), and an index assignment as in (Q.21). Composition of simplices with \(f\), followed by the index assignment, defines pullbacks on the double complexes and on small cochains. It preserves cup products and commutes with all the augmentations. The naturality assertion of Lemma Q.3 therefore proves naturality of the comparison. If the assignment changes, the map on global singular cochains is still the same pullback, so the induced Čech map is the same after the invertible comparisons. Common good refinements, provided by Theorem Q.1, identify comparisons for different choices of covers, and composition follows from composition of simplex maps. □

## 10. Simplex integration and relative de Rham comparison

### Integration on a simplex

Identify the ordered standard simplex \(\Delta^n=[e_0,\ldots,e_n]\) with
\[
S_n=\{(x_1,\ldots,x_n):x_i\geq0,\ x_1+\cdots+x_n\leq1\},
\qquad t_0=1-\sum_i x_i,\quad t_i=x_i.
\tag{I.1}
\]
Its orientation is \(dx_1\wedge\cdots\wedge dx_n\): the tangent vectors from \(e_0\) towards the other ordered vertices correspond to the coordinate vectors. In dimension zero, integration means evaluation at the point. In positive dimension, define the integral of \(g\,dx_1\wedge\cdots\wedge dx_n\) to be the Riemann integral on \([0,1]^n\) of \(g\) on \(S_n\) and zero elsewhere. The next proof establishes that this integral exists for continuous \(g\).

**Lemma I.1 (simplex integration and Stokes).** A continuous function on \(S_n\) is integrable in the sense just defined. Its integral equals the iterated integral over
\[
0\leq x_{i_1}\leq1,\quad
0\leq x_{i_2}\leq1-x_{i_1},\quad\ldots,\quad
0\leq x_{i_n}\leq1-\sum_{j<n}x_{i_j}
\tag{I.2}
\]
for every ordering of the coordinates, with the last variable integrated first. For a smooth \((n-1)\)-form \(\omega\) on a neighbourhood of \(\Delta^n\), \(n\geq1\),
\[
\int_{\Delta^n}d\omega
=\sum_{i=0}^n(-1)^i\int_{\Delta^{n-1}}\varepsilon_i^*\omega,
\tag{I.3}
\]
where \(\varepsilon_i\) is the ordered affine face omitting \(e_i\).

**Proof.** Compactness and uniform continuity here follow from local-tools Lemma 0.1, since \(S_n\) is closed and bounded. Write \(B=\sup_{S_n}|g|\), and let \(\mu(\delta)\) bound the oscillation of \(g\) at distances at most \(\delta\), with \(\mu(\delta)\to0\). Subdivide the unit cube into cubes of side \(1/N\). The cubes meeting a coordinate face \(x_i=0\) have total volume at most \(n/N\). For the remaining boundary plane \(\sum x_i=1\), fix the first \(n-1\) lower-grid indices. A cube with final lower index \(k\) can meet the plane only if its lower coordinate sum is at most \(1\) and its upper coordinate sum is at least \(1\). These inequalities leave at most \(n+1\) choices of \(k\). Thus the cubes meeting that plane have total volume at most \((n+1)/N\).

Every other cube lies entirely in \(S_n\) or entirely outside it: if it met both, the line segment joining those two points would meet a boundary face. On an inside cube the oscillation is at most \(\mu(\sqrt n/N)\), and on an outside cube it is zero. On boundary cubes it is at most \(2B\). The upper-minus-lower Darboux sum is consequently at most
\[
\mu(\sqrt n/N)+2B\,\frac{2n+1}{N},
\tag{I.4}
\]
which tends to zero. The refinement argument in the proof of Lemma A.1 applies to any bounded function, so this proves existence and the usual linearity, monotonicity and integral bound.

We justify iterated integration without assuming a Fubini theorem for discontinuous functions. Fix one coordinate as the innermost variable, write the others as \(x'\in S_{n-1}\), and put \(L(x')=1-\sum x'_j\). The function
\[
h(x')=\int_0^{L(x')}g(x',t)\,dt
\]
is continuous. Indeed, on the common part of the two integration intervals the change in \(g\) is bounded by its uniform oscillation as \(x'\) changes, and the remaining interval contributes at most \(B|L(x')-L(y')|\). Induction proves existence of every iterated integral in (I.2).

To identify its value with the rectangular Riemann integral, use the rectangular lower and upper step functions of a grid in the preceding paragraph for the zero extension of \(g\). Each bounds that extension except for harmless choices of values on finitely many grid hyperplanes. Those choices have zero one-dimensional integral in the corresponding coordinate: an interval of total length as small as desired covers the finitely many points, so the integral bound makes their contribution zero. Successive integrations preserve the inequalities. The step functions have iterated integrals equal to their respective Darboux sums, by summing the constant values times the products of the interval lengths. Hence the iterated integral of the zero extension, which is exactly (I.2), lies between those sums. Equation (I.4) makes their limits equal. Permuting the chosen variable order gives the assertion for every order.

For (I.3), the case \(n=1\) is the fundamental theorem of calculus in local-tools Lemma 0.3. For \(n\geq2\), write
\[
\omega=\sum_{i=1}^n(-1)^{i-1}a_i\,
dx_1\wedge\cdots\wedge\widehat{dx_i}\wedge\cdots\wedge dx_n.
\]
Lemma D.1 gives
\[
d\omega=\left(\sum_{i=1}^n\partial_i a_i\right)
dx_1\wedge\cdots\wedge dx_n.
\]
For its \(i\)-th summand, integrate in \(x_i\) first. The fundamental theorem and the already proved any-order assertion give the integral, over the simplex in the other coordinates, of
\[
a_i(x_1,\ldots,x_{i-1},1-\!\sum_{j\ne i}x_j,x_{i+1},\ldots,x_n)
-a_i(x_1,\ldots,x_{i-1},0,x_{i+1},\ldots,x_n).
\tag{I.5}
\]

For \(i\geq1\), the face omitting \(e_i\) is \(x_i=0\), with the other coordinates in their inherited order. The pullback of \(\omega\) to it has coefficient \((-1)^{i-1}a_i\). Multiplication by the boundary sign \((-1)^i\) makes this precisely the negative bottom term in (I.5).

The face omitting \(e_0\) is parametrized, with its inherited order, by
\[
x_1=1-y_1-\cdots-y_{n-1},\qquad x_{j+1}=y_j.
\]
The \(i=1\) summand of its pullback has coefficient \(a_1\). For \(i\geq2\), only the term \(-dy_{i-1}\) in \(dx_1\) contributes; moving it past the preceding \(i-2\) differentials gives sign \((-1)^{i-1}\), which cancels the prefactor of the \(i\)-th summand. Thus this face pulls \(\omega\) back to
\[
\left(\sum_i a_i\right)dy_1\wedge\cdots\wedge dy_{n-1}.
\tag{I.6}
\]
Its \(i=1\) integral is already the corresponding top term of (I.5). For \(i\geq2\), fix all coordinates except \(x_1,x_i\), and let \(L=1-\sum_{j\ne1,i}x_j\). The top face has \(x_1+x_i=L\). The substitution \(x_i=L-x_1\), with reversed endpoints on \([0,L]\), equates its integral in \(x_1\) to its integral in \(x_i\). This substitution follows by applying the one-variable fundamental theorem to a primitive; no higher-dimensional change of variables is being assumed. Integrating the other coordinates, in any order as already justified, identifies the \(i\)-th top integral in (I.5) with the \(i\)-th summand of (I.6). Summing the top and bottom contributions proves (I.3). □

For a smooth \(q\)-simplex \(\sigma:\Delta^q\to M\), define
\[
(I_q\alpha)(\sigma)=\int_{\Delta^q}\sigma^*\alpha,\qquad
I_q:\Omega^q(M)\longrightarrow C_\infty^q(M;\mathbb R).
\tag{I.7}
\]
The definition of smooth simplex is that of DG06 K.1: an extension to an open neighbourhood in the affine span exists. Any two such extensions agree on the simplex interior, so their derivatives there agree; continuity makes their derivatives agree on its boundary too. Therefore (I.7) is independent of the extension. In degree zero it is ordinary evaluation. The map extends linearly to chains by their definition as finite formal sums.

### The integration isomorphism and its product

**Theorem I.2 (absolute integration).** Equation (I.7) is a cochain map and induces a natural isomorphism of unital graded real algebras
\[
H^*_{\mathrm{dR}}(M)\ \xrightarrow{\ H(I)\ }\ H^*_\infty(M;\mathbb R).
\tag{I.8}
\]
Composing with the inverse of the restriction isomorphism in Theorem K.6 gives the corresponding natural real algebra isomorphism with ordinary singular cohomology.

**Proof.** Lemma D.1 says that pullback commutes with exterior differentiation. Apply Lemma I.1 to the pullback of \(\alpha\) by each smooth \((q+1)\)-simplex. Its right side is exactly evaluation of \(I_q\alpha\) on the chain boundary of that simplex. Thus
\[
I_{q+1}(d\alpha)=d_s(I_q\alpha).
\tag{I.9}
\]
For a smooth map \(f:N\to M\), \((f\circ\sigma)^*\alpha=\sigma^*f^*\alpha\) gives \(I(f^*\alpha)=f^*I(\alpha)\) at the cochain level.

Take a good cover \(\mathcal U\) from Theorem Q.1. Let \(C_\Omega\) be the form double complex (Q.11), and \(B_\infty\) the smooth singular double complex (K.21), both with total differential \(\delta+(-1)^p d\). Applying \(I_q\) to every intersection component commutes with restriction and, by (I.9), with the vertical differential. It therefore gives a total cochain map
\[
\mathcal I\colon \operatorname{Tot}C_\Omega\longrightarrow
\operatorname{Tot}B_\infty.
\]
Write \(L=\check C^*(\mathcal U;\mathbb R)\), and denote its two column augmentations by \(b_\Omega,b_\infty\). Integration in degree zero evaluates a constant, so the equality of cochain maps
\[
\mathcal I b_\Omega=b_\infty
\tag{I.10}
\]
holds. Theorems Q.4 and K.6 prove that both augmentations are cohomology isomorphisms. Consequently
\[
H(\mathcal I)=H(b_\infty)H(b_\Omega)^{-1}
\tag{I.11}
\]
is an isomorphism.

Let \(C^*_{\infty,\mathcal U}(M;\mathbb R)\) denote cochains on small smooth chains, and let \(r_{\mathcal U}:C_\infty^*(M;\mathbb R)\to C^*_{\infty,\mathcal U}(M;\mathbb R)\) be restriction. The row augmentations \(a_\Omega,a_\infty\) satisfy
\[
\mathcal I a_\Omega=a_\infty r_{\mathcal U}I.
\tag{I.12}
\]
Both row augmentations are cohomology isomorphisms, by the same two theorems, and \(r_{\mathcal U}\) is one by Lemma DG06 K.4. Equations (I.11)–(I.12) therefore prove bijectivity of \(H(I)\).

The column and row augmentations preserve their respective products and units by Q.4 and K.6. The small-cochain restriction does so by DG06 K.5. Although \(\mathcal I\) need not preserve cochain products, equation (I.11) expresses its cohomology map as a composite of algebra isomorphisms. Equation (I.12) then does the same for \(H(I)\). This proves the product and unit assertion without making a false cochain-level multiplicativity claim. Naturality was already proved before the choice of cover. Theorem K.6 makes ordinary-to-smooth restriction a natural algebra isomorphism, completing the ordinary singular assertion. □

### Two algebraic facts about relative complexes

All complexes in the following arguments have zero groups in negative degrees. For a cochain map \(r:A^*\to B^*\), set
\[
\mathcal C^q(r)=A^q\oplus B^{q-1},\qquad
D(a,b)=(da,ra-db).
\tag{I.13}
\]
The identity \(dr=rd\) gives \(D^2=0\). This is the relative convention already used in H.1.

**Lemma I.3 (comparison of relative cones).** Suppose \(F:A\to A'\) and \(G:B\to B'\) are cochain maps with \(Gr=r'F\). If \(H(F)\) and \(H(G)\) are isomorphisms, then
\[
(a,b)\longmapsto(Fa,Gb)
\tag{I.14}
\]
induces an isomorphism \(H^*(\mathcal C(r))\to H^*(\mathcal C(r'))\).

**Proof.** Formula (I.14) commutes with \(D\) by the displayed commutation relation.

For surjectivity in degree \(q\geq1\), take a closed pair \((a',b')\). Since \(da'=0\) and \(H(F)\) is onto, choose \(a\) closed and \(u'\in A'^{q-1}\) such that \(a'=Fa+du'\). Subtracting \(D(u',0)\) leaves \((Fa,c')\), where \(c'=b'-r'u'\) and \(dc'=G(ra)\). The element \(ra\) is closed and has exact image under \(G\). Injectivity of \(H(G)\) gives \(b\in B^{q-1}\) with \(ra=db\). Now \(c'-Gb\) is closed. Surjectivity of \(H(G)\) supplies a closed \(h\in B^{q-1}\) and \(v'\in B'^{q-2}\) with
\[
c'-Gb=Gh+dv'.
\]
The pair \((a,b+h)\) is closed and its image differs from \((Fa,c')\) by \(D(0,-v')\). This proves surjectivity. When \(q=1\), the group containing \(v'\) is zero; surjectivity in degree zero of \(H(G)\) means precisely that the asserted difference equals \(Gh\), so the same proof is valid with \(v'=0\).

For injectivity in degree \(q\geq1\), suppose a closed pair \((a,b)\) has image \(D(u',v')\). Then \(Fa=du'\), so injectivity of \(H(F)\) gives \(a=du\), with \(u\in A^{q-1}\). Subtract \(D(u,0)\) from \((a,b)\), leaving \((0,c)\), where \(c=b-ru\) is closed. Put \(u''=u'-Fu\); it is closed, and the second component of the assumed exactness reads
\[
Gc=r'u''-dv'.
\]
Choose a closed \(v\in A^{q-1}\) and \(w'\in A'^{q-2}\) with \(u''=Fv+dw'\), using surjectivity of \(H(F)\). It follows that
\[
G(c-rv)=d(r'w'-v').
\]
Injectivity of \(H(G)\) gives \(h\in B^{q-2}\) with \(c-rv=dh\). Hence
\[
(0,c)=D(v,-h).
\]
Restoring the subtracted boundary proves exactness of \((a,b)\). At \(q=1\), the negative-degree terms \(v',w',h\) are all zero; the uses of degree-zero injectivity and surjectivity give the required equalities without boundary corrections.

At \(q=0\), a cone cocycle is an \(a\in A^0\) satisfying \(da=0\) and \(ra=0\), and there are no boundaries. For a target cocycle \(a'\), surjectivity of \(H^0(F)\) gives an actual equality \(a'=Fa\) with \(da=0\). Then \(G(ra)=r'a'=0\), so injectivity of \(H^0(G)\) gives \(ra=0\). If a source cocycle has image zero, injectivity of \(H^0(F)\) gives \(a=0\). This proves degree zero and finishes the argument. □

**Lemma I.4 (relative kernel and cone).** If \(r:A^q\to B^q\) is onto in each degree, then
\[
\kappa:\ker r\longrightarrow\mathcal C(r),\qquad c\longmapsto(c,0),
\tag{I.15}
\]
is a cohomology isomorphism.

**Proof.** It is a cochain map. A closed pair \((a,b)\) of degree \(q\geq1\) satisfies \(da=0\), \(ra=db\). Choose \(\widetilde b\in A^{q-1}\) with \(r\widetilde b=b\). Subtracting \(D(\widetilde b,0)\) leaves
\[
(a-d\widetilde b,0),
\]
whose first component is a closed element of \(\ker r\). This proves surjectivity. If \((c,0)=D(a,b)\), then \(da=c\) and \(ra=db\). Choose \(\widetilde b\) extending \(b\). The element \(a-d\widetilde b\) lies in \(\ker r\) and has differential \(c\), proving injectivity. In degree one of the latter argument, \(b\) has degree \(-1\) and is zero, so take \(\widetilde b=0\). In degree zero both complexes have the same closed elements \(\{a:da=0,\ ra=0\}\) and have no boundaries. □

### Relative integration and the absolute action

For an open set \(V\subset M\), define ordinary and smooth relative singular cochains by
\[
C_\bullet^*(M,V;\mathbb R)
=\ker\big(C_\bullet^*(M;\mathbb R)\longrightarrow C_\bullet^*(V;\mathbb R)\big),
\quad \bullet\in\{\text{continuous},\infty\}.
\tag{I.16}
\]
Their cohomology is denoted \(H_\bullet^*(M,V;\mathbb R)\). Restriction is onto in every degree: a cochain assigns a number to each simplex, and assignments on simplices lying in \(V\) extend to the other simplices by assigning zero. This extension need not commute with the differential, and no such property is needed in Lemma I.4.

Use the relative form complex
\[
\Omega^q(M,V)=\Omega^q(M)\oplus\Omega^{q-1}(V),\qquad
D(\alpha,\beta)=(d\alpha,\alpha|_V-d\beta),
\tag{I.17}
\]
as in H.1. Denote its cohomology by \(H^*_{\mathrm{dR}}(M,V)\).

**Theorem I.5 (relative integration and module compatibility).** Componentwise integration, followed by the inverse of (I.15) in cohomology, gives an isomorphism
\[
H^*_{\mathrm{dR}}(M,V)\longrightarrow H_\infty^*(M,V;\mathbb R).
\tag{I.18}
\]
It is natural for smooth maps of open pairs. Smooth restriction also gives an isomorphism from ordinary to smooth relative singular cohomology. Under these comparisons, the action of \(H^*_{\mathrm{dR}}(M)\) on the left agrees with the action of ordinary or smooth absolute singular cohomology on the right.

**Proof.** Integration commutes with restrictions by (I.7) and with differentials by (I.9). The absolute integration theorem on \(M\) and on \(V\), together with Lemma I.3, therefore gives a cohomology isomorphism from (I.17) to the cone of smooth singular restriction. Lemma I.4 identifies the latter with the kernel complex (I.16). Applying Lemma I.3 to ordinary-to-smooth restriction, using Theorem K.6 separately on \(M\) and \(V\), proves the analogous relative restriction assertion. A smooth map of pairs commutes with each cochain map in these constructions. The kernel-to-cone maps are natural as well; their inverse cohomology maps consequently are natural. This proves naturality without choosing a natural extension by zero.

We prove the assertion about the action, including its sign. Suppose \(A,B\) are differential graded algebras and \(r:A\to B\) preserves their products and units. For homogeneous \(u\in A^p\), set
\[
u\cdot(a,b)=\big(ua,(-1)^p r(u)b\big)
\tag{I.19}
\]
on (I.13). Associativity follows because the two signs in an iterated action multiply to \((-1)^{p+s}\) when the two absolute degrees are \(p,s\). The unit acts as the identity. The first component obeys the product rule in \(A\). In the second component,
\[
\begin{aligned}
\big[D(u\cdot(a,b))\big]_2
&=r(u)r(a)-(-1)^p r(du)b-r(u)db\\
&=\big[(du)\cdot(a,b)+(-1)^p u\cdot D(a,b)\big]_2.
\end{aligned}
\tag{I.20}
\]
Thus (I.19) defines an action on cohomology. It specializes to the wedge action of H.3 and to the cup action on singular cones. The singular kernel is stable under multiplication by absolute cochains, since restriction is multiplicative. The inclusion \(\kappa\) preserves this action.

It remains to show that integration respects the action on cohomology. A cochain-level assertion of multiplicativity would not establish this, since it is false in general. Choose a good cover \(\mathcal U\) of \(M\), and a good cover \(\mathcal W\) of \(V\) refining its restricted cover, using Q.1. Choose indices \(\lambda(j)\) with \(W_j\subset U_{\lambda(j)}\). Formula (Q.21), now for inclusion \(V\to M\), gives algebra cochain maps
\[
\begin{array}{lll}
L_M\longrightarrow L_V,&
T_{\Omega,M}\longrightarrow T_{\Omega,V},&
T_{\infty,M}\longrightarrow T_{\infty,V}.
\end{array}
\tag{I.21}
\]
Here \(L\) denotes the constant Čech complex, and \(T_\Omega,T_\infty\) the total form and smooth singular complexes on the indicated cover. The maps preserve products by Q.4 and K.6. Their column augmentations \(b_\Omega,b_\infty\) commute with (I.21). Each column augmentation is a cohomology isomorphism, so Lemma I.3 makes the induced maps on the cones of (I.21) cohomology isomorphisms too. These maps preserve (I.19), together with the corresponding absolute maps, because their defining cochain maps preserve products.

There are also the row augmentations from global forms on \(M,V\) and from the respective small smooth cochains. Restriction from \(\mathcal U\)-small cochains on \(M\) to \(\mathcal W\)-small cochains on \(V\) is defined, since every \(\mathcal W\)-small simplex is \(\mathcal U\)-small when composed with the inclusion. Thus these augmentations form commuting maps of pairs of complexes. Each is an absolute cohomology isomorphism, by Q.4 and K.6, so their cone maps are isomorphisms by I.3. They preserve the action for the same algebraic reason. Finally, the restrictions from all smooth cochains to these small cochains are absolute algebra cohomology isomorphisms by DG06 K.4–DG06 K.5; their cone maps are again isomorphisms preserving the action.

Componentwise integration gives maps from the form pair of total complexes in (I.21) to the singular pair and from their cones to their cones. On the common constant Čech complexes and their cones it is the identity, exactly as in (I.10). Its absolute and relative cohomology maps are therefore the composites of the corresponding column-augmentation isomorphisms. Those isomorphisms preserve the actions just proved, so the integration maps do as well. The commuting row-augmentation and small-cochain diagrams identify these maps with absolute integration and (I.18). Since every map used for that identification also preserves the action, the desired compatibility follows. Ordinary-to-smooth restriction is multiplicative at the cochain level and commutes with \(\kappa\), so the assertion for ordinary singular cohomology follows too. □

### Evaluation on a relative cycle

A smooth relative \(q\)-cycle is a smooth \(q\)-chain \(c\) in \(M\) with \(\partial c\) a chain in \(V\). Two such cycles represent the same relative homology class if their difference is \(\partial h+k\), where \(h\) is a smooth \((q+1)\)-chain in \(M\) and \(k\) a smooth \(q\)-chain in \(V\). This defines the homology of the quotient chain complex, since \(\partial^2=0\) by DG06 K.1. A relative singular cocycle evaluates on a relative cycle; adding either a relative coboundary or a relative boundary leaves the value unchanged by the same identity.

**Lemma I.6 (relative evaluation formula).** Let \((\alpha,\beta)\) be a closed pair in (I.17), and let \(c\) be a smooth relative \(q\)-cycle. The class corresponding to \([(\alpha,\beta)]\) under (I.18) evaluates by
\[
\left\langle I_{\mathrm{rel}}[(\alpha,\beta)],[c]\right\rangle
=\int_c\alpha-\int_{\partial c}\beta.
\tag{I.22}
\]
In degree zero the second term is zero.

**Proof.** In the smooth singular cone, componentwise integration gives \((I\alpha,I\beta)\). Extend the cochain \(I\beta\) from \(V\) to a cochain \(\widetilde{I\beta}\) on \(M\). The inverse construction in the surjectivity proof of I.4 represents its relative kernel class by
\[
I\alpha-d_s\widetilde{I\beta}.
\]
Evaluating on \(c\) gives \((I\alpha)(c)-\widetilde{I\beta}(\partial c)\). Since \(\partial c\) is a chain in \(V\), this is exactly (I.22), independently of the extension.

One can also verify the two independence assertions directly. Changing the closed form pair by \(D(\gamma,\eta)\) changes the right side by
\[
\int_c d\gamma-\int_{\partial c}(\gamma|_V-d\eta)=0,
\]
using equation (I.3) on each simplex and \(\partial^2c=0\). Changing \(c\) by \(\partial h+k\) changes it by
\[
\int_h d\alpha+\int_k\alpha|_V-\int_{\partial k}\beta
=0+\int_k d\beta-\int_k d\beta=0,
\]
again by equation (I.3) and the closed-pair equations. Negative-degree terms vanish, so this covers degree zero as well. □

## 11. Integral orientation and integration normalization

We use the integral local orientation already fixed in DG06 O.1: the ordered product \(Q_r\) of the affine intervals from \(-1\) to \(1\) represents the positive generator \(g_r\) of \(H_r(\mathbb R^r,\mathbb R^r\setminus\{0\};\mathbb Z)\). Its integral dual is \(u_r\); the dimension-zero convention is the positive point. DG06 O.2–O.3 prove the linear and smooth coordinate signs. Write \(H_r(M\mid K)=H_r(M,M\setminus K;\mathbb Z)\). We use ordinary homology here. Each affine cube simplex is smooth, so the relative evaluation formula I.6 also computes its ordinary pairing through the restriction comparison I.5.

### The local integration pairing

For a compactly supported top form \(\omega\) on \(\mathbb R^r\), let
\[
\mathcal I_c\omega=(\omega,B\omega)
\tag{O.9}
\]
be its relative de Rham representative from (H.7)–(H.10). Here \(B\) is the outward-radial primitive on the complement of zero. The real relative integration isomorphism of I.5 will be denoted by \(\mathfrak I\), to distinguish it from (O.9). Our coordinate integral uses the order \(dy_1\wedge\cdots\wedge dy_r\).

**Theorem O.4 (local normalization).** The real relative class \(\mathfrak I[\mathcal I_c\omega]\) evaluates on \(g_r\) as
\[
\big\langle\mathfrak I[\mathcal I_c\omega],g_r\big\rangle
=\int_{\mathbb R^r}\omega.
\tag{O.10}
\]
Consequently a compactly supported top form of integral one corresponds to the real coefficient image of \(u_r\). The identification uses the positive generator of DG06 O.1, not an unspecified sign choice for an abstract cyclic group.

**Proof.** Suppose \(r>0\). Choose real numbers
\[
0<a_r<\cdots<a_1<\frac{1}{4\sqrt r}
\]
and small closed intervals about them, strictly separated in the displayed order and lying in \((0,1/(2\sqrt r))\). On each such interval choose a nonnegative smooth bump, positive somewhere and supported in its interior. Explicitly, choose \(l_i<a_i<h_i\) strictly inside that interval, and take \(\eta(y_i-l_i)\eta(h_i-y_i)\), where \(\eta\) is the opening lesson's flat function. Its support is the smaller closed interval \([l_i,h_i]\). Its integral is positive: continuity gives a positive lower bound on a still smaller interval, and A.1 preserves inequalities. Divide by that integral to obtain \(b_i\) with integral one. Set
\[
\tau=\left(\prod_{i=1}^r b_i(y_i)\right)
dy_1\wedge\cdots\wedge dy_r.
\tag{O.11}
\]
It is compactly supported, and A.1 gives \(\int\tau=1\). Its support lies in the ball of radius \(1/2\) and strictly in the region \(y_1>\cdots>y_r\).

The cube shuffle simplices have the coordinate ordering description in the geometry proof of DG06 X.2, iterated one factor at a time. Thus the support of \(\tau\) lies entirely in the interior of the one simplex that increases coordinates in the order \(1,\ldots,r\). Every other simplex misses it. That simplex has coefficient \(+1\) and has positive affine determinant \(2^r\): its successive vertex differences are the partial sums of the vectors \(2e_1,\ldots,2e_r\). Its pullback coefficient is a globally smooth compactly supported function with support in the interior of the standard simplex. Lemma A.2 applies to this affine substitution, and the simplex integral equals its whole-space integral because that support lies in the simplex interior. Therefore
\[
\int_{Q_r}\tau=1.
\tag{O.12}
\]
This use of A.2 concerns a continuous compactly supported function; it does not extend a substitution formula to a discontinuous characteristic function.

Every point of the boundary of \([-1,1]^r\) has norm at least one. Its entire outward ray misses the support in (O.11). Formula (H.7) therefore makes \(B\tau\) zero on the cube boundary. The relative evaluation formula (I.22) gives
\[
\big\langle\mathfrak I[(\tau,B\tau)],g_r\big\rangle
=\int_{Q_r}\tau-\int_{\partial Q_r}B\tau=1.
\tag{O.13}
\]

Apply F.1 to the vector bundle \(\mathbb R^r\to\{\mathrm{point}\}\) and the normalized form \(\tau\). Every compactly supported top form is closed, and that theorem gives a compactly supported primitive for
\[
\omega-\left(\int\omega\right)\tau.
\tag{O.14}
\]
The map \(\mathcal I_c\) is a cochain map by (H.10), so (O.14) has zero relative de Rham class. Linearity of the comparison and of evaluation now proves (O.10). DG06 U.3 identifies real degree-\(r\) cohomology of the local pair with the real dual of its homology; both the coefficient image of \(u_r\) and (O.13) evaluate to one on its generator, so they are equal. The affine cube is itself a smooth representative of the ordinary generator in DG06 O.1. Naturality of evaluation under inclusion of smooth chains therefore fixes the same normalization in the ordinary comparison of I.5.

For \(r=0\), a top form is a scalar on a point, the relative complement is empty, and the integral and evaluation are both that scalar. This proves the remaining case. □

We will also need this compact-support version of the calculation. Let \(K\) be a closed coordinate ball centred at zero, with \(\operatorname{supp}\omega\subset K\). The outward primitive \(B\omega\) vanishes outside \(K\), since every outward ray there stays outside \(K\). Restricting the relative pair from the complement of zero to the complement of \(K\) therefore gives \((\omega,0)\). If \(\gamma_K\in H_r(\mathbb R^r\mid K)\) maps to \(g_r\) at zero, naturality of the relative evaluation yields
\[
\langle\mathfrak I[(\omega,0)],\gamma_K\rangle=\int\omega.
\tag{O.15}
\]
The class \(\gamma_K\) exists uniquely by DG06 E.6. Translations give the same conclusion for a ball centred anywhere; their determinant is positive and A.2 gives translation invariance of the integral.

### Fundamental classes and global integration

For an oriented \(r\)-manifold, DG06 O.4 proves that the chart generators are coherent and that every compact \(K\subset M\) has a unique class
\[
[M]_K\in H_r(M\mid K)
\tag{O.16}
\]
restricting to the chosen positive local generator at each point of \(K\). These classes are compatible under enlargement of compact supports. When \(M\) is compact, \([M]=[M]_M\). In dimension zero one chooses a sign \(\epsilon_x\) on each point, giving local class \(\epsilon_x[x]\) and coordinate integral \(\epsilon_x\) times the value. We use these proved ordinary integral classes throughout.

**Theorem O.6 (global integration pairing).** If \(\omega\) is a compactly supported smooth top form, the sum of its integrals using a finite subordinate oriented-chart partition is independent of that partition and those charts. It equals
\[
\int_M\omega
=\left\langle\mathfrak I[(\omega,0)],[M]_K\right\rangle
\quad\text{whenever }K\text{ is compact and contains }\operatorname{supp}\omega.
\tag{O.17}
\]
For compact \(M\), this is the absolute pairing of the de Rham class of \(\omega\) with \([M]\).

**Proof.** The opening lesson's relatively compact coordinate balls and partition theorem give a locally finite smooth partition \((\phi_i)\) with each support compact in a coordinate ball. Compactness of \(\operatorname{supp}\omega\) leaves only finitely many nonzero \(\omega_i=\phi_i\omega\). For each such term, choose a closed coordinate ball \(L_i\) inside the same chart range and containing its coordinate support. This is possible by choosing the partition inside nested coordinate balls, as in the proof of opening-lesson Theorem 3.1. The coordinate form extends smoothly by zero to \(\mathbb R^r\), since its support is compactly inside the chart.

By excision and the pointwise characterization in (O.16), the class \([M]_{L_i}\), in these coordinates, is the positive compact-support class used in (O.15). The relative form pair is \((\omega_i,0)\), and naturality in I.5–I.6 together with (O.15) gives
\[
\left\langle\mathfrak I[(\omega_i,0)],[M]_{L_i}\right\rangle
=\int_{\mathbb R^r}(\omega_i)_{\mathrm{coordinates}}.
\tag{O.18}
\]
This step uses the chart-relative excision comparison; it does not assume a nonlinear change-of-variables theorem.

Let \(L\) be the finite union of the compact chart supports \(L_i\). All pairs \((\omega_i,0)\) map to the relative form complex for \((M,M\setminus L)\), where their sum is \((\omega,0)\). Naturality of evaluation and the compatibility of the classes just proved turn the sum of (O.18) into (O.17) with \(K=L\).

For any other compact \(K\) containing \(\operatorname{supp}\omega\), compare both with \(K\cup L\). The relative pair \((\omega,0)\) restricts to the pair supported on this union, and \([M]_{K\cup L}\) maps to both \([M]_K\) and \([M]_L\). Naturality of evaluation proves the equality of the two values. Hence every allowable oriented-chart partition gives the same answer. For compact \(M\), take \(K=M\); forgetting the empty relative component gives the absolute pairing. In dimension zero, compact support contains finitely many points, and every construction reduces to \(\sum_x\epsilon_x\omega(x)\) with the chosen signed point generators. □

## 12. The Gaussian class is the real image of the integral class

Let \(E\to M\) be an oriented smooth real rank-\(r\) vector bundle over a smooth manifold. Let \(u_E\in H^r(E,E^\times;\mathbb Z)\) be the integral class of DG06 T.3, and write \(u_{E,\mathbb R}\) for its coefficient image. Let \((C_0,\beta)\) be the Gaussian relative de Rham pair of (G.11)–(G.12), with the metric and compatible connection constructed in D.2.

**Theorem Y.1 (integral normalization of the Gaussian and Euler classes).** Under the actual relative integration isomorphism \(\mathfrak I\) of I.5,
\[
\mathfrak I[(C_0,\beta)]=u_{E,\mathbb R}.
\tag{Y.1}
\]
Consequently the real image of the integral Euler class is represented by
\[
e(E)_{\mathbb R}=
\begin{cases}
[\operatorname{Pf}(F/(2\pi))],&r\text{ even},\\
0,&r\text{ odd},
\end{cases}
\tag{Y.2}
\]
with the explicit curvature and Pfaffian conventions of D.3, G.2 and P.1. In rank zero the representative is \(1\).

**Proof.** Fix a base point and pull the relative pair back to its oriented fibre. The cutoff map \(J_\chi\) in H.2 sends the Gaussian pair to the properly supported form \(U_\chi\) of G.3. Restriction to a fibre is compactly supported, since support proper over the base is compact over a point. It has integral one by G.3.

This restriction is compatible with H.2's relative-to-supported map: the formula \(J_\chi(\alpha,\beta)=\chi\alpha+d\chi\wedge\beta\) restricts to the identical formula on the fibre. The inverse on its cohomology is (O.9), by (H.10)–(H.12). Therefore the restricted Gaussian relative class corresponds to that compact top form under the fibre version of H.2. The local normalization O.4 identifies its relative integration class with the real image of the positive integral fibre class \(u_r\).

Naturality in I.5 makes restriction commute with the actual relative integration map. Thus the two sides of (Y.1) have the same specified value on every fibre. These values detect degree-\(r\) real relative cohomology globally: DG06 T.3 with coefficient group \(\mathbb R\) writes every such class uniquely as \(p^*a\smile u_E\), with \(a\in H^0(M;\mathbb R)\). On the fibre at \(x\), its restriction is \(a(x)u_{r,\mathbb R}\). A zero-cocycle is determined by its point values, as proved in DG06 T.1. Hence a class with the prescribed value \(1\) on every fibre has \(a=1\) and is \(u_{E,\mathbb R}\). This proves (Y.1).

Forgetting the relative component in the de Rham cone sends \((C_0,\beta)\) to \(C_0\). The comparisons I.2 and I.5 commute with this map and with pullback by the zero section, since they are built from restriction and simplex integration. The Euler definition (DG06 T.13) therefore identifies its real image with \([s_0^*C_0]\). Lemma G.2 computes this pullback as the normalized Pfaffian in even rank and zero in odd rank. For rank zero H.3 and DG06 T.3 both give the unit. This is (Y.2). □

## 13. Invariant curvature polynomials and change of connection

### Polarization and covariant differentiation

Let \(\mathfrak g\) be a finite-dimensional real or complex matrix Lie algebra, and let \(G\) be a matrix group acting on it by conjugation. Each \(Z\in\mathfrak g\) is assumed to be the derivative at zero of a smooth curve \(g(s)\in G\) with \(g(0)=I\), as in the definition of the Lie algebra of a matrix Lie group. We use local connection matrices in \(\mathfrak g\) and changes of frame in \(G\). The cases needed below are general linear, orthogonal, special orthogonal and unitary frame groups. Their local bundle connections are constructed in Lemma D.2. For general linear groups any matrix gives the curve \(I+sZ\) near zero; for skew or skew-Hermitian matrices the matrix exponential constructed by the group ODE in the repaired opening lesson gives the corresponding curve. Differentiating \(g(s)^*g(s)\) verifies that it remains the identity in those cases. For a real skew matrix the determinant stays \(1\): orthogonality makes it \(\pm1\), and continuity along the curve from the identity fixes the sign. This also covers the special orthogonal group.

A homogeneous polynomial \(P\colon \mathfrak g\to\mathbb K\) of degree \(m\), with \(\mathbb K=\mathbb R\) or \(\mathbb C\), is **invariant** if \(P(gXg^{-1})=P(X)\) for all \(g\in G\). Complex-valued polynomials on a real Lie algebra are allowed. For \(m>0\), set
\[
\widetilde P(X_1,\ldots,X_m)
=\frac1{m!}[t_1\cdots t_m]P(t_1X_1+\cdots+t_mX_m).
\tag{W.1}
\]
The bracket means the coefficient of the indicated monomial.

**Lemma W.1 (polarization identities).** The function \(\widetilde P\) is symmetric and multilinear, is the unique such function with \(\widetilde P(X,\ldots,X)=P(X)\), and is invariant under simultaneous conjugation. It satisfies
\[
\sum_{j=1}^m
\widetilde P(X_1,\ldots,[Z,X_j],\ldots,X_m)=0
\quad (Z,X_j\in\mathfrak g).
\tag{W.2}
\]

**Proof.** Expand \(P\) in coordinate monomials of degree \(m\). A term contributing to the coefficient \(t_1\cdots t_m\) must choose exactly one coordinate from each \(X_j\), so the coefficient is multilinear; permuting the variables proves symmetry. On the diagonal, \(P((\sum_j t_j)X)=(\sum_jt_j)^mP(X)\); the indicated coefficient is \(m!P(X)\). Conversely, expanding any symmetric multilinear function on \(\sum_jt_jX_j\) in every slot recovers it from that same coefficient, proving uniqueness. Invariance of (W.1) follows by taking coefficients in the invariant identity for \(P\).

For (W.2), take a curve \(g(s)\) as above and differentiate the polarized invariance identity. Differentiating \(g(s)g(s)^{-1}=I\) at zero gives \((g^{-1})'(0)=-Z\), so the derivative of \(g(s)X_jg(s)^{-1}\) is \([Z,X_j]\). The ordinary multilinear product rule now gives (W.2). \(\square\)

Extend \(\widetilde P\) to matrix-valued forms by writing each in a fixed matrix basis, applying \(\widetilde P\) to the matrix factors, and wedging their scalar form coefficients in the given order. This does not depend on the matrix basis, by multilinearity. If the form degrees are \(q_1,\ldots,q_m\), exchanging two adjacent arguments has sign \((-1)^{q_iq_{i+1}}\). A connection matrix \(A\) acts on a matrix-valued \(q\)-form by
\[
D_A\omega=d\omega+[A,\omega],\qquad
[A,\omega]=A\wedge\omega-(-1)^q\omega\wedge A.
\tag{W.3}
\]

**Lemma W.2 (invariant differentiation).** In this notation,
\[
d\widetilde P(\omega_1,\ldots,\omega_m)
=\sum_{j=1}^m(-1)^{q_1+\cdots+q_{j-1}}
\widetilde P(\omega_1,\ldots,D_A\omega_j,\ldots,\omega_m).
\tag{W.4}
\]

**Proof.** For the terms containing \(d\omega_j\), this is exactly the exterior product rule, applied to the coefficient forms. It remains to show that the added commutator terms cancel. Expand \(A\) as a sum of one-forms \(a\) times constant basis matrices \(Z\), and each \(\omega_j\) as sums \(\beta_jX_j\). By multilinearity it suffices to consider one such choice. The definition gives
\[
[aZ,\beta_jX_j]=a\wedge\beta_j[Z,X_j].
\]
Moving \(a\) to the beginning of the product crosses \(q_1+\cdots+q_{j-1}\) form degrees. That sign cancels the prefactor in (W.4). All the commutator terms therefore have the same form coefficient \(a\wedge\beta_1\wedge\cdots\wedge\beta_m\), multiplied by the sum in (W.2). That sum is zero, proving (W.4). \(\square\)

### The curvature construction

**Theorem W.3 (Chern–Weil forms and explicit transgression).** Suppose a bundle has a connection with local matrices \(A\) as above and curvature \(F=dA+A\wedge A\). For an invariant homogeneous polynomial \(P\) of degree \(m\), the local forms
\[
P(F)=\widetilde P(F,\ldots,F)
\]
give a global closed \(2m\)-form. Its de Rham class is independent of the connection and commutes with pullback. Polynomial sums and products give the corresponding sums and wedge products of forms, so this construction gives an algebra homomorphism from invariant polynomials to even de Rham cohomology.

For two connections, let \(a=A_1-A_0\), \(A_t=A_0+ta\), and \(F_t=dA_t+A_t\wedge A_t\). If \(m>0\), the global \((2m-1)\)-form
\[
\operatorname{CS}_P(A_0,A_1)
=m\int_0^1\widetilde P(a,F_t,\ldots,F_t)\,dt
\tag{W.5}
\]
satisfies
\[
P(F_1)-P(F_0)=d\operatorname{CS}_P(A_0,A_1).
\tag{W.6}
\]

**Proof.** The curvature change-of-frame identity in Lemma D.3 is \(F'=g^{-1}Fg\). Polarized invariance makes the local scalar forms agree. This is an equality of multilinear coefficients, so it applies to their form-valued substitutions without assuming that a two-form is an ordinary matrix entry. Bianchi is \(D_AF=0\). Since every curvature argument has even degree, (W.4) immediately gives \(dP(F)=0\).

The difference \(a\) of two connection matrices changes by conjugation: the inhomogeneous term \(g^{-1}dg\) cancels. The matrices \(A_t\) obey the connection transformation law, and the \(F_t\) therefore transform by conjugation. Thus the integrand in (W.5) is a global form. It is smooth after parameter integration by Lemma A.3. Direct differentiation gives
\[
\partial_tF_t=da+A_t\wedge a+a\wedge A_t=D_{A_t}a.
\]
Symmetry of \(\widetilde P\) and the even degree of \(F_t\) give
\[
\partial_t P(F_t)
=m\widetilde P(D_{A_t}a,F_t,\ldots,F_t).
\]
Apply (W.4) to \(a,F_t,\ldots,F_t\). Every term other than the first vanishes by Bianchi, so the last display equals
\[
m\,d\widetilde P(a,F_t,\ldots,F_t).
\]
Integrate from zero to one, pass \(d\) through the finite parameter integral by Lemma A.3, and use the fundamental theorem to obtain (W.6). Constant polynomials already give constant zero-forms and require no transgression.

Pullback commutes with curvature by Lemma D.3 and with the finite multilinear contraction and wedge products, proving naturality. Finally even forms commute, so substituting them in coordinate polynomial sums and products preserves those operations term by term. Their closed forms therefore give an algebra homomorphism after taking cohomology. The connection independence follows from (W.6). \(\square\)

This proof also exhibits the parameter convention in the cylinder argument: a connection on the pullback bundle over \([0,1]\times M\) with no \(dt\) component has curvature \(F_t+dt\wedge a\). The coefficient of \(dt\) in \(P(F_t+dt\wedge a)\) is precisely the integrand of (W.5). Terms with two \(dt\)'s vanish; moving the single \(dt\) past curvature factors gives no sign since those factors have degree two. Thus the homotopy identity (F.2) gives the same positive sign in (W.6).

### Named real and complex forms

For a complex rank-\(n\) bundle, define the Chern forms and the Chern-character forms by
\[
\det\left(I+\frac{i}{2\pi}F\right)=\sum_{j=0}^n c_j(\nabla),
\qquad
\operatorname{ch}(\nabla)=\sum_{j\geq0}\frac1{j!}
\operatorname{tr}\left(\frac{i}{2\pi}F\right)^j.
\tag{W.7}
\]
Here \(c_j\) and the \(j\)-th trace term have degree \(2j\); terms above the dimension of the base vanish. Thus the second expression is finite in differential forms. The invariant polynomial property follows from determinant multiplicativity over commutative rings (DG06 Lemma L.1) and from \(\operatorname{tr}(XY)=\operatorname{tr}(YX)\), the latter identity following by interchanging the two indices in \(\sum_{i,j}X_{ij}Y_{ji}\). These arguments apply to even-degree entries as well.

For a real rank-\(n\) metric bundle, put
\[
\det\left(I+\frac{1}{2\pi}F\right)=1+p_1(\nabla)+p_2(\nabla)+\cdots,
\tag{W.8}
\]
where \(p_j\) has degree \(4j\). Only these degrees occur: \(F^T=-F\), and invariance of the determinant under transpose shows that \(\det(I+sF)=\det(I-sF)\). The coefficient of every odd power of \(s\) is therefore zero over the real even-form algebra. On an oriented real bundle of rank \(2k\), put
\[
e(\nabla)=\operatorname{Pf}(F/2\pi).
\tag{W.9}
\]
Theorem W.3 applies to the determinant and trace coefficients. It applies to the Pfaffian in oriented orthonormal frames by Lemma P.1. The forms are closed and their classes are independent of the chosen connection for each fixed metric. Theorem G.3 and F.1 show more for (W.9): its class is the zero-section pullback of the unique normalized properly supported de Rham class, so it is also independent of the metric. That uniqueness argument is made on the underlying oriented bundle and allows the two supported representatives to have been constructed using different metrics.

The classes of (W.8) are metric independent as well. For any real connection, use the coefficients of its general linear invariant polynomial \(\det(I+F/2\pi)\). Theorem W.3 compares it with any metric connection constructed by Lemma D.2; the latter has the odd coefficients zero. Thus the even-degree cohomology classes in (W.8) do not depend on which metric supplied the comparison connection.

**Lemma W.4 (real forms, direct sums and the top identity).** The Chern and Chern-character forms of a unitary connection are real. For block direct-sum connections, the total Chern and Pontryagin forms multiply, and Chern characters add. On an oriented real rank-\(2k\) bundle,
\[
e(\nabla)^2=p_k(\nabla).
\tag{W.10}
\]

**Proof.** For a unitary connection, \(\overline F^{\,T}=-F\) by Lemma D.3. Hence \(\overline{iF}=(iF)^T\). The determinant is unchanged by transposition; its permutation formula proves this by replacing each permutation by its inverse. The trace of every matrix power is also unchanged by transposition, since the entries have even degree and transposition reverses products in the ordinary way. Complex conjugation therefore fixes every coefficient in (W.7).

The curvature of a direct-sum connection is block diagonal. In a block-diagonal determinant, every nonzero permutation term preserves each block, giving the product of the determinants. Traces of block powers add. This proves the asserted form identities. Finally the top coefficient in (W.8) for rank \(2k\) is \(\det(F/2\pi)\). Theorem P.2 identifies it with (W.9) squared, proving (W.10). \(\square\)

For rank zero, all determinant and empty Pfaffian forms are \(1\), and the Chern character is \(0\), as the definitions specify. In odd oriented real rank the Gaussian construction has zero zero-section form, as Lemma G.2 proves.

## 14. Why complex invariant polynomials are generated by Chern polynomials

### Symmetric polynomials

Write \(e_j(x_1,\ldots,x_n)\) for the sum of the squarefree monomials of degree \(j\), and put \(e_0=1\). Expanding a product gives
\[
\prod_{a=1}^n(1+t x_a)=\sum_{j=0}^n e_j(x)t^j.
\tag{S.1}
\]
A polynomial is symmetric when every permutation of its variables leaves it unchanged.

**Lemma S.1 (symmetric-polynomial elimination).** Over \(\mathbb R\) or \(\mathbb C\), every symmetric polynomial \(f(x_1,\ldots,x_n)\) has a unique expression \(Q(e_1,\ldots,e_n)\). If \(f\) is homogeneous of total degree \(d\), \(Q\) is homogeneous of weighted degree \(d\) when the \(j\)-th variable has weight \(j\).

**Proof.** Order exponent tuples lexicographically: compare their first unequal coordinate. The order is unchanged when the same tuple is added to both sides, since the first unequal coordinate and its inequality are unchanged. Hence the leading monomial of a product is the product of the two leading monomials: any pair with at least one smaller factor has strictly smaller exponent tuple. Its coefficient is the product of the leading coefficients, which is nonzero over either indicated field.

First suppose \(f\) is homogeneous of degree \(d\) and nonzero, with leading monomial \(c x_1^{a_1}\cdots x_n^{a_n}\). Necessarily \(a_1\geq a_2\geq\cdots\geq a_n\). If \(a_i<a_j\) for some \(i<j\), symmetry supplies the same nonzero coefficient at the monomial obtained by interchanging those exponents; its tuple is lexicographically greater, a contradiction. The leading monomial of \(e_j\) is \(x_1\cdots x_j\), with coefficient one. Therefore
\[
c\,e_1^{a_1-a_2}e_2^{a_2-a_3}\cdots e_{n-1}^{a_{n-1}-a_n}e_n^{a_n}
\tag{S.2}
\]
has exactly the same leading monomial as \(f\). It also has total degree
\[
\sum_{j=1}^{n-1}j(a_j-a_{j+1})+n a_n=\sum_{j=1}^n a_j=d.
\]
Subtract (S.2). The remainder is symmetric, homogeneous of degree \(d\), and either zero or has a strictly smaller leading exponent tuple. There are only finitely many tuples of nonnegative integers summing to \(d\): each coordinate is at most \(d\). The subtraction procedure must therefore terminate. It gives the required weighted homogeneous \(Q\). For a general polynomial, each homogeneous component is symmetric, since permuting variables preserves total degree; apply the construction to each of the finitely many components and add.

For uniqueness, the leading tuple of \(e_1^{b_1}\cdots e_n^{b_n}\) is
\[
(b_1+\cdots+b_n,\ b_2+\cdots+b_n,\ \ldots,\ b_n).
\]
Different tuples \(b\) give different leading tuples, as successive differences recover \(b\). In a nonzero polynomial \(Q\), choose the term whose substituted product has largest leading tuple. No other term's substituted product can contain that monomial, because all its monomials are bounded by its strictly smaller leading tuple. Thus \(Q(e_1,\ldots,e_n)\ne0\). This proves uniqueness and completes the proof. \(\square\)

### The matrix argument

Define the polynomial functions \(\sigma_j\) on complex \(n\)-by-\(n\) matrices by
\[
\det(I+tX)=\sum_{j=0}^n\sigma_j(X)t^j.
\tag{S.3}
\]
In particular \(\sigma_0=1\), and \(\sigma_j\) is homogeneous of degree \(j\). Determinant multiplicativity proves \(\sigma_j(gXg^{-1})=\sigma_j(X)\). On a diagonal matrix with entries \(x_a\), \(\sigma_j=e_j(x)\), by the permutation definition of the determinant.

**Theorem S.2 (all complex conjugation-invariant polynomials).** Let \(P(X)\) be a polynomial with complex coefficients in the \(n^2\) complex matrix entries, invariant under conjugation by \(\mathrm{GL}(n,\mathbb C)\). There is a unique polynomial \(Q\) such that
\[
P(X)=Q(\sigma_1(X),\ldots,\sigma_n(X))
\quad\text{for every complex matrix }X.
\tag{S.4}
\]
If \(P\) is homogeneous of degree \(d\), \(Q\) has weighted degree \(d\), with weight \(j\) on its \(j\)-th variable. The assertion concerns polynomials in the complex entries themselves, without their conjugates.

**Proof.** Restrict \(P\) to diagonal matrices. Conjugation by a permutation matrix permutes their entries, so the restriction is a symmetric polynomial. Lemma S.1 gives its unique polynomial \(Q\) in \(e_1,\ldots,e_n\), with the indicated degree. Set
\[
R(X)=P(X)-Q(\sigma_1(X),\ldots,\sigma_n(X)).
\]
This is an invariant polynomial and is zero on every diagonal matrix. It remains to show that it is the zero polynomial on all matrices. We establish enough diagonalizable matrices by a local calculation rather than assuming a theorem about eigenvalues.

Choose pairwise distinct real numbers \(a_1,\ldots,a_n\), and let \(D=\operatorname{diag}(a_1,\ldots,a_n)\). Let \(Y\) range over real matrices with zero diagonal and let \(\lambda\in\mathbb R^n\). Near \((0,a)\), define
\[
\Phi(Y,\lambda)=(I+Y)\operatorname{diag}(\lambda)(I+Y)^{-1}.
\tag{S.5}
\]
The inverse exists and depends smoothly on \(Y\) near zero by local-tools Lemma 0.4. Domain and target have the same real dimension \(n(n-1)+n=n^2\). The derivative at \((0,a)\) is
\[
(H,\nu)\longmapsto HD-DH+\operatorname{diag}(\nu).
\tag{S.6}
\]
Its diagonal is \(\nu\) and its \((i,j)\)-entry for \(i\ne j\) is \((a_j-a_i)H_{ij}\). All these differences are nonzero. For any target matrix \(Z\), the unique inverse of this derivative is \(\nu_i=Z_{ii}\), \(H_{ij}=Z_{ij}/(a_j-a_i)\) for \(i\ne j\), and \(H_{ii}=0\). It is therefore an invertible linear map.

The inverse function theorem, with this derivative checked explicitly, shows that the image of a neighbourhood under \(\Phi\) contains a real open neighbourhood of \(D\) in the full space of real matrices. Every matrix in that image is conjugate to a diagonal matrix by the real invertible matrix \(I+Y\), so invariance makes \(R\) zero on that real open set. The set contains a nonempty open box in the \(n^2\) real matrix entries. Lemma P.0 says that a complex-coefficient polynomial zero on this box has every coefficient zero. The same coefficient identity therefore holds for arbitrary complex substitutions. This proves (S.4).

Any polynomial relation between the \(\sigma_j\)'s restricts to the corresponding relation between the \(e_j\)'s on diagonal matrices, and Lemma S.1 proves that relation is zero. This proves uniqueness. The weighted statement was already supplied by the diagonal restriction, so the theorem follows. \(\square\)

For a curvature matrix, its even-degree entries commute. Thus the coefficient identity (S.4) can be evaluated on \(F\). In the normalization (W.7), if \(X=iF/(2\pi)\), then \(\sigma_j(X)=c_j(\nabla)\). Therefore every invariant polynomial in this normalized curvature is a unique polynomial in the Chern forms. The associated de Rham classes have the same identity, by Theorem W.3.

### Trace powers and the Chern character

**Lemma S.3 (the trace-power recursion).** Put \(q_m(x)=\sum_a x_a^m\), and set \(e_j=0\) for \(j>n\). For \(m\geq1\),
\[
m e_m=\sum_{j=1}^m(-1)^{j-1}e_{m-j}q_j.
\tag{S.7}
\]
The same identity holds with \(e_j=\sigma_j(X)\) and \(q_j=\operatorname{tr}(X^j)\) for an arbitrary complex matrix, and for even-form substitutions.

**Proof.** Let \(E(t)=\prod_a(1+t x_a)\). The finite product rule gives
\[
E'(t)=E(t)\sum_a\frac{x_a}{1+t x_a}.
\]
This may be read purely formally to any required finite power of \(t\): multiplication by \(1+t x_a\) of the truncated geometric sum \(\sum_{j=0}^{N}(-t x_a)^j\) gives one plus a term of degree \(N+1\). Thus coefficient comparison through degree \(m-1\) is valid without any convergence or nonzero-denominator assumption. In those degrees the last sum is \(\sum_{j\geq1}(-1)^{j-1}q_j t^{j-1}\). Comparing coefficients of \(t^{m-1}\) and using (S.1) proves (S.7).

For matrices, subtract the two sides of the asserted identity. The difference is a conjugation-invariant polynomial in the entries, zero on diagonal matrices by the scalar calculation. Theorem S.2 makes it the zero polynomial. Substituting even-degree entries preserves that identity. \(\square\)

In particular, with \(c_j=c_j(\nabla)\), (S.7) for \(m=1,2,3\) successively gives
\[
\begin{aligned}
\operatorname{ch}_0&=n,\\
\operatorname{ch}_1&=c_1,\\
\operatorname{ch}_2&=\tfrac12(c_1^2-2c_2),\\
\operatorname{ch}_3&=\tfrac16(c_1^3-3c_1c_2+3c_3).
\end{aligned}
\]
Indeed (S.7) gives \(q_1=e_1\), \(q_2=e_1q_1-2e_2\), and \(q_3=e_1q_2-e_2q_1+3e_3\); insert these into the coefficient \(q_m/m!\) of (W.7). This verifies the displayed coefficients without presuming an eigenvalue splitting of the bundle.

## 15. From curvature to integral characteristic classes

All manifolds here are finite-dimensional, Hausdorff, second countable and without boundary. All bundles have constant finite rank. The integral Chern classes are the classes already constructed in DG09 B.2; they are not defined by curvature. Write \(\rho_{\mathbb R}\) and \(\rho_{\mathbb C}\) for coefficient maps from integral singular cohomology to real or complex singular cohomology. Applying a coefficient map to each cocycle value commutes with the coboundary and cup formulas of DG06 K.5, so these are natural ring maps. We use the integration isomorphism \(\mathfrak I\) of I.2.

For complex coefficients the same integration isomorphism follows from its real version: a complex form is uniquely a real form plus \(i\) times a real form, and a complex singular cochain has the same unique decomposition by its values. Both differentials act componentwise. Kernels, images and their quotients therefore split into the two real parts. Extend \(\mathfrak I\) to these decompositions. Its naturality and multiplicativity follow by expanding two products into real and imaginary parts and applying I.2. In particular the inclusion of real cohomology into complex cohomology is injective, with left inverse the real-part map on the underlying real vector spaces.

### Smooth splitting with cohomology injection

**Lemma C.1 (smooth flag construction).** A smooth complex rank-\(r\) bundle \(V\to M\) has a smooth manifold \(F(V)\), a smooth map \(f:F(V)\to M\), and smooth line bundles \(L_j\) such that
\[
f^*V\cong L_1\oplus\cdots\oplus L_r
\tag{C.1}
\]
as smooth bundles. The pullback on singular cohomology is injective for every abelian coefficient group. Pullback on real and complex de Rham cohomology is injective as well.

**Proof.** For ranks zero and one use \(F(V)=M\), the identity map, and respectively the empty sum or \(L_1=V\). Suppose \(r\geq2\). The projective bundle from DG08 M.1 has local products \(U\times\mathbb{CP}^{r-1}\). The finite projective charts and their smooth fractional coordinate changes are proved in DG08 R.1. A smooth bundle transition \(g(x)\) acts in these charts by dividing the coordinates of \(g(x)v\) by one of its nonzero coordinates. Division by a nonzero complex number is smooth as a real operation, as follows from \(z^{-1}=\bar z/|z|^2\). Thus these local products have smooth transition maps with smooth inverses, and their projection is smooth.

Their total space is Hausdorff by DG08 M.1. It is second countable: choose a countable cover of \(M\) by trivializing coordinate neighbourhoods. Such a subcover exists because from a countable base one selects a member of the given cover containing each basis element that is contained in some cover member; these selected members still cover. Each local product has a countable basis, using the finite projective charts and the Euclidean countable bases. The union of these countably many bases is a basis of the total space. Hence \(P(V)\) is a smooth manifold of dimension \(\dim M+2(r-1)\), without boundary.

The tautological line is smooth: its local nonzero frame is the vector with the chosen coordinate equal to one and the remaining projective chart coordinates as its other entries. Its frame changes are the same nonzero smooth scalar functions. Choose a smooth Hermitian metric on \(V\) by D.2. The orthogonal projection onto a line spanned by \(v\ne0\) has local formula
\[
\Pi_v(w)=v\,\frac{h(v,w)}{h(v,v)}.
\tag{C.2}
\]
Its entries are smooth and the denominator is positive. The orthogonal complement is a smooth subbundle. To see this explicitly near a given line, take \(r-1\) local constant frame vectors whose images under \(I-\Pi_v\) form a basis of the complement at that line. A nonzero minor remains nonzero nearby, so these smooth projected sections remain a frame. Their Gram matrix \(G\) is invertible: writing the projected frame as \(u_j\), if \(Ga=0\), then \(a^*Ga=h(\sum a_j u_j,\sum a_j u_j)=0\); positivity and independence give \(a=0\). The finite-dimensional inverse criterion in the opening lesson Lemma 0.2 applies. Its Lemma 0.4 makes the inverse smooth near any invertible matrix \(G_0\), by factoring \(G=G_0(I+G_0^{-1}(G-G_0))\) and using the proved inverse map near the identity. This gives smooth inverse coordinates on the complement. This also proves smoothness of the direct-sum isomorphism between the tautological line plus its complement and the pulled-back bundle.

Repeat projectivization on the smooth complement, whose rank has dropped by one. Each stage is a Hausdorff second-countable manifold by the same proof, and the induced complement metric remains smooth. These manifolds are paracompact: the opening lesson's smooth partition theorem supplies, for every open cover, a locally finite refinement by the opens where the subordinate partition functions are positive. Thus every stage meets the base hypotheses of DG08 M.4. After \(r-1\) stages the final complement is a line. Pull back all the earlier lines to the last stage; the smooth direct-sum identifications give (C.1).

This is exactly the projective sequence of DG08 M.4 with a smooth choice of metric. Each positive-rank projectivization is injective on singular cohomology with every abelian coefficient group by DG08 M.3. Their composition is injective. For de Rham classes, naturality of I.2 gives
\[
\mathfrak I(f^*\alpha)=f^*\mathfrak I(\alpha).
\]
If \(f^*\alpha=0\), the singular injectivity makes \(\mathfrak I(\alpha)=0\), and its isomorphism property makes \(\alpha=0\). Apply this first with real coefficients and then with the complex extension above. This proves all assertions. □

### Integral normalization of the curvature polynomials

**Theorem C.2 (Chern comparison).** Let \(\nabla\) be any smooth connection on a complex bundle \(V\). With \(F=dA+A\wedge A\) and the determinant convention (W.7),
\[
\mathfrak I[c_j(\nabla)]=\rho_{\mathbb C}c_j(V).
\tag{C.3}
\]
For a unitary connection the forms are real and (C.3) holds with \(\rho_{\mathbb R}\). In particular the real class represented by the Chern form is fixed by the integral class already constructed in DG09.

**Proof.** First let \(V=L\) be a line. A Hermitian metric and a unitary connection exist by D.2. In a unit complex frame the connection potential is \(ia\), for a real one-form \(a\). For the corresponding positively oriented real frame \((e,ie)\), the potential and curvature matrices are
\[
A_{\mathbb R}=
\begin{pmatrix}0&-a\\ a&0\end{pmatrix},
\qquad
F_{\mathbb R}=
\begin{pmatrix}0&-da\\ da&0\end{pmatrix}.
\tag{C.4}
\]
These follow by applying the connection to the two frame vectors and using \(a\wedge a=0\). The complex curvature is \(F_L=i\,da\). The Pfaffian convention P.1 and the Euler normalization Y.1 therefore give
\[
\mathfrak I\left[\frac{i}{2\pi}F_L\right]
=\mathfrak I\left[-\frac{da}{2\pi}\right]
=\rho_{\mathbb R}e(L_{\mathbb R})
=\rho_{\mathbb R}c_1(L).
\tag{C.5}
\]
The last equality is the rank-one definition in DG09 B.2. Thus the factor \(i\) and its sign are fixed by the oriented real plane, rather than by a convention left implicit in an external reference. Theorem W.3 compares any other line connection to this unitary connection by an exact complex form, proving (C.3) for every line connection.

For rank \(r>1\), take C.1's smooth flag map. Choose unitary connections on its smooth line summands and their direct-sum connection on \(f^*V\), transported through (C.1). Theorem W.3 makes its characteristic classes equal to those of \(f^*\nabla\). Lemma W.4 makes its total Chern form the product of the line factors. Consequently multiplicativity and naturality of integration and (C.5) give
\[
\begin{aligned}
f^*\mathfrak I[c(\nabla)]
&=\prod_{j=1}^r\bigl(1+\rho_{\mathbb C}c_1(L_j)\bigr)\\
&=\rho_{\mathbb C}c(f^*V)
=f^*\rho_{\mathbb C}c(V).
\end{aligned}
\tag{C.6}
\]
The middle equality is the integral Whitney formula DG09 B.4, applied to the actual line splitting. Injectivity with complex coefficients in C.1 proves (C.3) in each degree. For a unitary connection W.4 proves the forms real. Both sides then come from real cohomology, whose inclusion into complex cohomology is injective; hence the real equality follows. In rank zero the determinant and \(c_0\) are one and every positive class is zero, so the same conclusion holds directly. □

For a general complex connection the individual Chern forms need not be real. The theorem says that their complex de Rham classes are the images of the specified real classes. It does not identify the integral group with a subgroup of real cohomology: integral torsion can disappear under the coefficient map.

**Theorem C.3 (Pontryagin comparison and the integral top identity).** For a smooth real rank-\(r\) bundle \(E\), form its complexification \(E_{\mathbb C}\) and define
\[
p_j(E)=(-1)^j c_{2j}(E_{\mathbb C})\in H^{4j}(M;\mathbb Z),
\qquad p_0(E)=1.
\tag{C.7}
\]
Its real image is represented by the Pontryagin form (W.8) for a metric connection on \(E\). The class is independent of the metric and is natural under pullback. For an oriented real bundle of even rank \(2m\),
\[
p_m(E)=e(E)\smile e(E)
\quad\text{in }H^{4m}(M;\mathbb Z).
\tag{C.8}
\]

**Proof.** Complexification is explicit in local frames: replace each real coordinate vector space \(\mathbb R^r\) by \(\mathbb C^r\) and keep the same real transition matrices. Those matrices and their inverses are smooth and complex linear, so they define a smooth complex bundle. A real connection with matrices \(A\) extends complex linearly with the same matrices and curvature \(F\); its frame law is still D.3. A real metric extends to a Hermitian metric with the same real Gram matrix. A real metric connection becomes unitary.

Let \(\sigma_k(F)\) denote the degree-\(k\) coefficient of \(\det(I+tF)\), a form of degree \(2k\). Homogeneity of the determinant coefficients gives
\[
c_{2j}(\nabla_{\mathbb C})
=\frac{i^{2j}}{(2\pi)^{2j}}\sigma_{2j}(F)
=(-1)^j\frac{\sigma_{2j}(F)}{(2\pi)^{2j}}.
\tag{C.9}
\]
For a metric connection, skewness of \(F\) makes its odd determinant coefficients zero, as proved in the discussion of (W.8). Multiplying (C.9) by \((-1)^j\) and using C.2 gives exactly (W.8)'s Pontryagin form as the real image of (C.7). Complexification commutes with pullback, since both operations pull back the same transition matrices. Naturality and isomorphism invariance now follow from DG09 B.2; the definition makes metric independence immediate. Classes above the permitted Chern index are zero.

For (C.8), consider the real bundle isomorphism
\[
E\oplus E\longrightarrow (E_{\mathbb C})_{\mathbb R},
\qquad (v,w)\longmapsto v+iw.
\tag{C.10}
\]
Its inverse recovers the real and imaginary coordinate parts; since the transition matrices are real, these descriptions agree on overlaps. In an oriented basis \(e_1,\ldots,e_r\), the direct-sum orientation is sent to the ordered list
\[
e_1,\ldots,e_r,\;ie_1,\ldots,ie_r.
\]
The complex orientation has the interleaved list \(e_1,ie_1,\ldots,e_r,ie_r\). Passing between them has \(r(r-1)/2\) transpositions: \(ie_j\) crosses \(r-j\) real vectors. For \(r=2m\), the sign is \((-1)^m\). The Thom orientation-reversal and direct-sum formulas in DG06 T.4 thus give
\[
c_{2m}(E_{\mathbb C})
=e((E_{\mathbb C})_{\mathbb R})
=(-1)^m e(E\oplus E)
=(-1)^m e(E)^2.
\]
The first equality is DG09 B.2's top normalization. Insert this in (C.7) to obtain (C.8). At rank zero all three displayed classes are the unit. □

For a flat connection the positive-degree curvature forms vanish, so their real characteristic classes vanish. Nothing in this conclusion asserts the vanishing of integral torsion classes. Direct-sum multiplication of Pontryagin forms is the proved form identity W.4; no additional integral multiplicativity assertion is needed here.

### The rational Chern character

**Theorem C.4 (Chern character and bundle operations).** Let \(V\) be a smooth complex rank-\(r\) bundle. Define \(q_0=r\) and, for \(m\geq1\), define the rational cohomology classes \(q_m\) by the recursion
\[
m\,c_m(V)_{\mathbb Q}
=\sum_{j=1}^m(-1)^{j-1}c_{m-j}(V)_{\mathbb Q}q_j,
\qquad c_0=1,\quad c_k=0\ (k>r).
\tag{C.11}
\]
The coefficient of \(q_m\) is \((-1)^{m-1}\), so this determines each \(q_m\) from the previous ones. The graded series
\[
\operatorname{ch}(V)=\sum_{m\geq0}\frac{q_m}{m!}
\in\prod_{m\geq0}H^{2m}(M;\mathbb Q)
\tag{C.12}
\]
has real image represented by the Chern-character forms in (W.7). It is natural and satisfies
\[
\operatorname{ch}(V\oplus W)=\operatorname{ch}(V)+\operatorname{ch}(W),
\qquad
\operatorname{ch}(V\otimes_{\mathbb C}W)
=\operatorname{ch}(V)\operatorname{ch}(W).
\tag{C.13}
\]
Multiplication and equality in (C.12) are understood degree by degree; only finitely many terms contribute to a fixed degree.

**Proof.** Recursion (C.11) defines a polynomial with rational coefficients in the integral Chern classes after their coefficient map. These classes commute, since they have even degree and the graded commutativity theorem DG06 X.5 applies. Naturality follows by induction from naturality of the Chern classes.

By S.3 the same recursion holds for \(\operatorname{tr}((iF/2\pi)^m)\) with the Chern forms as coefficients. C.2 and multiplicativity of I.2 therefore identify the real image of each \(q_m\) with the class of that trace form. Dividing by \(m!\) gives the claimed comparison with W.7. One may first use a unitary connection to have real forms; W.3 then compares any other connection. Terms above the dimension vanish on the differential-form side. The rational definition remains the degreewise series (C.12), so no cohomological dimension theorem is hidden in that notation.

On the flag space of C.1 put \(x_a=c_1(L_a)_{\mathbb Q}\). The integral root formula DG09 B.4 gives \(f^*c_j(V)_{\mathbb Q}=e_j(x_1,\ldots,x_r)\). The scalar polynomial calculation in S.3 remains valid on these commuting elements. Uniqueness in (C.11) consequently gives
\[
f^*q_m=\sum_{a=1}^r x_a^m \quad(m\geq1),
\qquad
f^*\operatorname{ch}(V)=\sum_{a=1}^r e^{x_a},
\tag{C.14}
\]
where \(e^x\) means the formal series \(\sum_{m\geq0}x^m/m!\).

To compare two bundles simultaneously, first flag-split \(V\), then apply C.1 to the smooth pullback of \(W\) on that flag manifold. Pull back the first splitting to the second flag manifold. The composite pullback is injective with rational coefficients, and on this common smooth space the two bundles split into lines \(L_a\) and \(K_b\).

For completeness their tensor bundle is smooth and has the expected split form. In local frames its basis consists of the symbols \(e_a\otimes f_b\), with the bilinear tensor relations; the coordinate bilinear functions \(e_a^*\otimes f_b^*\) prove independence of that basis. Under frame changes \(g,h\) the coefficient matrix has entries \(g_{ca}h_{db}\), with inverse formed from \(g^{-1},h^{-1}\). These are smooth and obey the transition composition law by expanding the finite sums. Pullback commutes with these matrices. Sending each line tensor \(L_a\otimes K_b\) into the corresponding tensor of the split sums is an isomorphism: in the displayed bases it and its inverse merely identify the same ordered coefficient coordinates.

Thus \(V\oplus W\) has the combined roots \(x_a,y_b\), while \(V\otimes W\) has roots \(x_a+y_b\) by the line tensor formula DG08 W.3. Formula (C.14) gives addition for the combined list. For the tensor list,
\[
\sum_{a,b}e^{x_a+y_b}
=\left(\sum_a e^{x_a}\right)\left(\sum_b e^{y_b}\right).
\]
Indeed in degree \(2m\) the equality \(e^{x+y}=e^xe^y\) is the binomial expansion of \((x+y)^m/m!\); the coefficient of \(x^k y^{m-k}\) is \(1/(k!(m-k)!)\). The variables commute because their degrees are even. Injectivity of the common flag pullback proves (C.13) on \(M\). If either rank is zero, the empty sum gives character zero, its tensor product has rank zero, and the same identities hold. □

In degrees zero through six the recursion gives
\[
\operatorname{ch}_0=r,\qquad
\operatorname{ch}_1=c_1,\qquad
\operatorname{ch}_2=\frac{c_1^2-2c_2}{2},\qquad
\operatorname{ch}_3=\frac{c_1^3-3c_1c_2+3c_3}{6}.
\]
These are rational cohomology identities and, under the comparison, the corresponding de Rham identities. The coefficient calculations were proved in S.3. Together with S.2 and C.2, they identify every complex conjugation-invariant curvature polynomial in the Chern classes with the stated normalization.

## 16. Euler evaluation and worked curvature calculations

Manifolds and bundle conventions are those of the preceding sections. A closed manifold means a compact manifold without boundary. Integrals are the chart-independent integrals proved in O.6.

### The tangent connection needed for the Euler formula

**Theorem V.1 (Levi-Civita existence and uniqueness).** A smooth positive Riemannian metric \(g\) has a unique compatible connection on \(TM\) with zero torsion. For vector fields its defining formula is
\[
\begin{aligned}
2g(\nabla_XY,Z)
={}&Xg(Y,Z)+Yg(Z,X)-Zg(X,Y)\\
&-g(X,[Y,Z])+g(Y,[Z,X])+g(Z,[X,Y]).
\end{aligned}
\tag{V.1}
\]

**Proof.** The bracket is intrinsically the commutator of the actions of vector fields on smooth functions. In coordinates its coefficients are
\[
[X,Y]^k=\sum_i\bigl(X^i\partial_iY^k-Y^i\partial_iX^k\bigr);
\]
the second derivatives in the commutator cancel by D.0. This coordinate expression shows that the commutator is again a smooth vector field and that it is independent of coordinates, since its action on every function was intrinsic. It gives
\[
[fX,Y]=f[X,Y]-Y(f)X,\qquad
[X,fY]=f[X,Y]+X(f)Y.
\tag{V.2}
\]

Call the right side of (V.1) \(K(X,Y,Z)\). It is real-linear in each argument. Product rules and (V.2) give
\[
\begin{aligned}
K(fX,Y,Z)&=fK(X,Y,Z),\\
K(X,Y,fZ)&=fK(X,Y,Z),\\
K(X,fY,Z)&=fK(X,Y,Z)+2X(f)g(Y,Z).
\end{aligned}
\tag{V.3}
\]
Here are the derivative cancellations. In the first line the additional terms are
\(Y(f)g(Z,X)-Z(f)g(X,Y)+Z(f)g(Y,X)-Y(f)g(Z,X)=0\).
In the second they are
\(X(f)g(Y,Z)+Y(f)g(Z,X)-Y(f)g(X,Z)-X(f)g(Y,Z)=0\).
In the third the two \(X(f)g(Y,Z)\) terms remain; the two terms containing \(Z(f)g(X,Y)\) cancel. This proves (V.3) rather than leaving its function-linearity implicit.

The second identity makes \(K(X,Y,\cdot)/2\) a smooth covector field. To verify pointwise dependence, expand \(Z=\sum Z^i\partial_i\) in a coordinate frame and apply that identity and additivity. The positive Gram matrix of \(g\) is invertible: its kernel is zero by positivity, and the opening lesson's Lemma 0.2 gives an inverse. Lemma 0.4 there proves that this inverse varies smoothly. Thus there is a unique smooth vector field \(\nabla_XY\) with the pairings (V.1). The first and third identities in (V.3) give the connection's function-linearity and Leibniz rule.

Adding the formulas for \(K(X,Y,Z)\) and \(K(X,Z,Y)\), symmetry of \(g\) and antisymmetry of the bracket cancel every term except \(2Xg(Y,Z)\). This proves metric compatibility. Subtracting the formulas for \(K(X,Y,Z)\) and \(K(Y,X,Z)\) leaves \(2g([X,Y],Z)\), proving zero torsion by nondegeneracy. The construction is global because its pairing expression is intrinsic.

Finally, for any compatible torsion-free connection, write the metric identities for \((X;Y,Z)\), \((Y;Z,X)\) and \((Z;X,Y)\), add the first two and subtract the third. Replace \(\nabla_YX\), \(\nabla_ZX\) and \(\nabla_ZY\) using zero torsion. The resulting identity is (V.1), so nondegeneracy proves uniqueness. This argument also covers dimension zero, where all vector fields and connection terms are zero. □

**Theorem V.2 (Gauss–Bonnet).** For a closed oriented Riemannian manifold of even dimension \(2m>0\), the curvature \(F\) of V.1 in oriented orthonormal frames satisfies
\[
\int_M\operatorname{Pf}\!\left(\frac{F}{2\pi}\right)=\chi(M).
\tag{V.4}
\]
The same identity holds in dimension zero with the canonical positive point orientations and the empty Pfaffian equal to one.

**Proof.** The connection is compatible by V.1. Theorem Y.1 identifies the de Rham class of its Pfaffian form with the real coefficient image of the integral tangent Euler class. This normalization includes the full Gaussian argument: G.2 computes the zero-section value, G.3 supplies a properly supported representative with fibre integral one, the relative integration comparison I.5 and O.4 identify its positive fibre generator, and the real-coefficient Thom isomorphism DG06 T.3 detects the global class from these fibre values. Thus Y.1 fixes both the sign and the factor \(2\pi\); no square-root choice of a Pontryagin form is involved.

The global integration pairing O.6 and the integral Euler-number identity DG07 D.4 now give
\[
\int_M\operatorname{Pf}\!\left(\frac{F}{2\pi}\right)
=\langle \rho_{\mathbb R}e(TM),[M]_{\mathbb R}\rangle
=\langle e(TM),[M]\rangle
=\chi(M).
\]
The middle equality means equality after the integer evaluation is included in \(\mathbb R\); it follows directly by applying the coefficient homomorphism to the finite cocycle-cycle evaluation. A compact manifold has finitely many components, as proved in DG07 C.3, so the same calculation adds over disconnected manifolds. In dimension zero, DG07 D.4 proves that the Euler evaluation, the integral of one and \(\chi(M)\) all count the finitely many points. The empty manifold gives zero. □

### A transgression with its primitive expanded

**Exercise V.3 (trace-square transgression, with solution).** Given complex bundle connections \(\nabla^0,\nabla^1\), put \(a=A_1-A_0\), \(D_0a=da+A_0\wedge a+a\wedge A_0\). Find a global primitive of \(\operatorname{tr}(F_1\wedge F_1-F_0\wedge F_0)\).

**Solution.** The curvature of \(A_t=A_0+ta\) is, by direct expansion of D.3,
\[
F_t=F_0+tD_0a+t^2a\wedge a.
\]
For the quadratic invariant polynomial \(P(X)=\operatorname{tr}(X^2)\), its symmetric polarization is
\(\widetilde P(X,Y)=\frac12\operatorname{tr}(XY+YX)\).
For a one-form matrix \(a\) and a two-form matrix \(F_t\), moving their scalar coefficients past each other has sign \((-1)^2=1\). Interchanging the two matrix indices in the trace therefore gives
\(\widetilde P(a,F_t)=\operatorname{tr}(a\wedge F_t)\).
Theorem W.3 consequently gives the global primitive
\[
\begin{aligned}
T
&=2\int_0^1\operatorname{tr}(a\wedge F_t)\,dt\\
&=2\operatorname{tr}(a\wedge F_0)
 +\operatorname{tr}(a\wedge D_0a)
 +\frac23\operatorname{tr}(a\wedge a\wedge a),
\end{aligned}
\tag{V.5}
\]
with \(dT=\operatorname{tr}(F_1^2-F_0^2)\). The coefficients are the elementary integrals of \(1,t,t^2\), justified by A.3 and the fundamental theorem. Globality follows also directly: \(a\), \(F_0\) and \(D_0a\) transform by conjugation, the last one as the coefficient of \(t\) in the curvature transformation rule for \(F_t\). Trace is invariant under conjugation.

For the degree-four Chern-character form, multiply \(T\) by \(-1/(8\pi^2)\), because \(\operatorname{ch}_2(\nabla)=\frac12\operatorname{tr}((iF/2\pi)^2)\). This computes the normalized primitive with no omitted sign. □

### The tautological line on the projective line

**Exercise V.4 (tautological Chern number, with solution).** For the tautological line \(\gamma\to\mathbb{CP}^1\), use the metric inherited from \(\mathbb C^2\) and orthogonal projection of the trivial connection. Compute its curvature and Chern number in the complex orientation.

**Solution.** DG08 R.1 gives smooth projective charts. On \(z=x+iy\) with homogeneous coordinates \([1:z]\), the tautological frame is \(v=(1,z)\), of squared length \(h=1+|z|^2\). The orthogonal projection \(P=vv^*/h\) is smooth and self-adjoint. For a section \(s\) of the line, define \(\nabla s=P\,ds\). The identity \(Ps=s\) proves its Leibniz rule. For line sections \(s,t\),
\[
d(s^*t)=(ds)^*t+s^*dt=(Pds)^*t+s^*(Pdt),
\]
since \(Pt=t\) and \(Ps=s\); thus it preserves the metric. The projection definition agrees on overlapping charts and so gives a global smooth connection.

Projecting \(dv=(0,dz)\) gives its potential and curvature in this frame:
\[
A=\frac{\bar z\,dz}{1+|z|^2},\qquad
F=dA=\frac{d\bar z\wedge dz}{(1+|z|^2)^2}.
\tag{V.6}
\]
Indeed \(d(\bar z\,dz)=d\bar z\wedge dz\), while
\(dh=z\,d\bar z+\bar z\,dz\). The quotient rule leaves coefficient
\(h^{-1}-|z|^2h^{-2}=h^{-2}\) on \(d\bar z\wedge dz\). The term \(A\wedge A\) is zero for a scalar one-form. Since \(d\bar z\wedge dz=2i\,dx\wedge dy\),
\[
c_1(\nabla)=\frac{iF}{2\pi}
=-\frac{dx\wedge dy}{\pi(1+x^2+y^2)^2}.
\tag{V.7}
\]

The complex orientation is \(dx\wedge dy>0\), by DG08 R.2. The radial Riemann-sum identity (A.3), already proved from annulus areas, gives
\[
\int_{x^2+y^2\leq R^2}c_1(\nabla)
=-\int_0^{R^2}\frac{ds}{(1+s)^2}
=-1+\frac1{1+R^2}.
\tag{V.8}
\]
These expanding coordinate disks exhaust the projective line minus its one point at infinity. The omitted part is a disk of radius \(1/R\) in the other projective coordinate \(w=1/z\). A smooth two-form has bounded coefficient on a small closed disk there, so the absolute value of its omitted integral is at most a fixed constant times \(\pi/R^2\), tending to zero. Chart independence is O.6; the disk-area and integral bounds are A.1 and A.5. Equivalently, insert smooth cutoffs equal to one on a disk and supported in a slightly larger disk, using the opening lesson Lemma 0.5. The same bounded-area estimates squeeze their integrals to this limit, so the argument uses only the smooth integration theorem O.6. Taking the limit proves
\[
\int_{\mathbb{CP}^1}c_1(\nabla)=-1.
\]
This equals the integral class evaluation: DG08 R.4 gives \(c_1(\gamma)=-x\) and \(\langle x,[\mathbb{CP}^1]\rangle=1\), and C.2 proves that (V.7) represents its real image. Thus the analytic calculation and the independently fixed integral sign agree. □

### The round two-sphere without a coordinate pole

**Exercise V.5 (round-sphere curvature integral, with solution).** Compute the curvature of the radius-\(R\) round sphere and verify (V.4) by direct integration.

**Solution.** Let \(R>0\) and \(s=u^2+v^2\). The stereographic parametrization
\[
q(u,v)=\frac{R}{1+s}\,(2u,2v,1-s)
\tag{V.9}
\]
maps \(\mathbb R^2\) bijectively onto the sphere minus its south pole, with inverse \((u,v)=(q_1,q_2)/(R+q_3)\). Substitution proves \(|q|=R\), the inverse formula and smoothness. Differentiating (V.9) and taking Euclidean dot products gives
\[
q_u\cdot q_u=q_v\cdot q_v=\frac{4R^2}{(1+s)^2},
\qquad q_u\cdot q_v=0.
\tag{V.10}
\]
For example, writing \(h=1+s\), one has \(q_u=(2R/h^2)a\) and \(q_v=(2R/h^2)b\), where
\[
a=(h-2u^2,-2uv,-2u),\qquad b=(-2uv,h-2v^2,-2v).
\]
Expanding \(s=u^2+v^2\) gives \(|a|^2=|b|^2=h^2\) and \(a\cdot b=0\), proving (V.10). Also
\[
q_u\times q_v=\frac{4R}{(1+s)^2}\,q,
\]
by the same coordinate expansion. Thus \(du\wedge dv\) gives the outward orientation.

Put \(\lambda=2R/(1+s)\). An oriented orthonormal coframe is \(\theta^1=\lambda\,du,\theta^2=\lambda\,dv\). For a torsion-free connection with matrix \(A\) in its dual frame,
\[
d\theta^i+\sum_j A_{ij}\wedge\theta^j=0.
\tag{V.11}
\]
To check the sign, evaluate the left side on \(X,Y\): differentiation of \(\theta^i(Y)\) using the connection leaves
\(\theta^i(\nabla_XY-\nabla_YX-[X,Y])\), which is zero. The formula for \(d\theta^i(X,Y)\) follows from D.1 in coordinates and the bracket formula in V.1.

Metric compatibility gives \(A=\left(\begin{smallmatrix}0&b\\-b&0\end{smallmatrix}\right)\). Substitute the coframe in (V.11). Its two equations determine
\[
b=\frac{\lambda_v}{\lambda}\,du-\frac{\lambda_u}{\lambda}\,dv
=\frac{-2v\,du+2u\,dv}{1+s}.
\]
Differentiating this scalar form gives
\[
F_{12}=db=\frac{4}{(1+s)^2}\,du\wedge dv
=\frac1{R^2}\,\theta^1\wedge\theta^2.
\tag{V.12}
\]
Indeed the numerator derivative is \(4\,du\wedge dv\); wedging \(d(1+s)=2u\,du+2v\,dv\) with the numerator gives \(4s\,du\wedge dv\). Their quotient-rule difference has coefficient \(4/(1+s)^2\). The matrix \(A\wedge A\) is zero here. Hence the Gaussian curvature, defined by the scalar coefficient in (V.12) with this curvature convention, is \(K=R^{-2}\), and the Euler form is \(K\,d\mathrm{area}/(2\pi)\).

The same radial formula (A.3) now gives
\[
\int_{\mathbb R^2}\frac{4R^2}{(1+s)^2}\,du\,dv=4\pi R^2,
\qquad
\int_{S_R^2}K\,d\mathrm{area}=4\pi.
\tag{V.13}
\]
For rigor at the omitted pole, the other chart uses \(w=(u-iv)/(u^2+v^2)\); substituting into (V.9) yields a smooth chart through that pole. The omitted exterior of a large disk is a shrinking disk in \(w\), so its contribution tends to zero by the bounded smooth-form estimate used in V.4. Thus the plane integrals equal the sphere integrals. Dividing by \(2\pi\) gives Euler number two. DG06 N.5 proves \(\chi(S^2)=2\), so this verifies (V.4) at every radius, including the unit sphere. □

### The rank-four density

**Exercise V.6 (four-plane Euler density, with solution).** Write the Euler form of an oriented metric real four-plane bundle, determine its orientation-reversal sign, and evaluate its meaning for the tangent bundle of a closed oriented four-manifold.

**Solution.** The pairing definition (P.1) has exactly the three terms \(12|34\), \(13|24\), \(14|23\). The index orders \(1,2,3,4\), \(1,3,2,4\), \(1,4,2,3\) require respectively zero, one and two interchanges to restore increasing order, so their signs are \(+,-,+\). Since the curvature entries have even degree and commute, this gives
\[
e(\nabla)
=\frac1{4\pi^2}
\bigl(F_{12}\wedge F_{34}-F_{13}\wedge F_{24}
      +F_{14}\wedge F_{23}\bigr).
\tag{V.14}
\]
In an orthonormal frame of the opposite orientation, the change matrix has determinant \(-1\). The Pfaffian change-of-basis identity P.1 multiplies (V.14) by that determinant, so the Euler form changes sign. The same sign is the Thom orientation change in DG06 T.4 and the Euler comparison Y.1.

For any such bundle over a closed oriented four-manifold, O.6 and Y.1 identify its integral with the integral Euler class paired with the chosen base fundamental class. When the bundle is the tangent bundle, with its orientation induced from that base, DG07 D.4 gives \(\chi(M)\), hence (V.4). Reversing the base orientation also reverses the induced tangent orientation, so both the fundamental class and the Euler form change sign; their integral remains \(\chi(M)\). For a separate four-plane bundle only its own orientation reversal is asserted to negate the integral. □

## Free construction sources

- Paul-Emile Paradan and Michèle Vergne, [*Equivariant relative Thom forms and Chern characters*, arXiv:0711.3898v2](https://arxiv.org/abs/0711.3898v2), Sections 2.2–2.3, 3.1, 3.5, 4.1 and 4.3–4.4: relative forms, transgression, the Gaussian family and supported representatives. The chapter supplies the ordinary form calculations, support control, convergence, normalization and comparison proofs.
- Siye Wu, [*Mathai-Quillen Formalism*, arXiv:hep-th/0505003v1](https://arxiv.org/abs/hep-th/0505003v1), Sections 2.1–2.2: the bundle Gaussian construction and its sign conventions.
- Jiří Lebl, [*Basic Analysis*, author version 6.3](https://www.jirka.org/ra/): real-analysis construction material, with the elementary analytic prerequisites proved in the opening lesson and the additional integral arguments proved here.
- Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, version of 21 June 2012](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), Chapter IV, Lemma 6.9 and the following construction, 6.10–6.12, 8.7, 8.10, 9.6 and 9.9: good covers and comparison of forms, Čech cochains and singular cochains. The convex-domain, finite-diagonal, relative-action and integration-normalization arguments are written explicitly in this chapter.
- Allen Hatcher, freely downloadable author *Algebraic Topology*, [Chapter 2](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf), [Chapter 3](https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf), [product appendix](https://pi.math.cornell.edu/~hatcher/AT/ATch3.4.pdf) and [Thom appendix](https://pi.math.cornell.edu/~hatcher/AT/ATch4.4.pdf): construction material for the singular, orientation and integral Thom arguments proved in DG06. The present integration comparison uses those exact programme proofs.
- Eckhard Meinrenken, [*Group actions on manifolds*, Spring 2003 author lecture notes](https://www.math.utoronto.ca/~mein/teaching/LectureNotes/action.pdf), Sections 5.1–5.4: invariant polynomials, Chern–Weil forms and transgression.
- Keith Conrad, [*Symmetric polynomials*, author notes](https://kconrad.math.uconn.edu/blurbs/galoistheory/symmfunction.pdf), Sections 1–3, especially the elimination proof on pages 6–7: the polynomial argument in Section 14.
- Kartik Venkatram, in collaboration with Denis Auroux, MIT OpenCourseWare 18.966, Spring 2007, [Lecture 10, Section 2](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/2e7d5aae3c1b3c6f935960608851165b_lect10.pdf) and [Lecture 11, Section 1.2](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/4699443c64f6c6f5bdbab98172674dbd_lect11.pdf): Chern and Pontryagin comparison setting. The notes carry CC BY-NC-SA 4.0; no source prose, diagram or PDF is reproduced. Smooth flag construction and all normalization and bundle-operation proofs are supplied here or in DG08–DG09.
- Peter W. Michor, free author draft [*Topics in Differential Geometry*](https://www.mat.univie.ac.at/~michor/dgbook.pdf), Section 22.5, printed pages 279–280: the Levi-Civita construction. Its function-linearity and uniqueness checks are included in V.1.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Human construction sources and their particular editions are credited above. No source prose, diagrams or PDFs are reproduced. Earlier programme lessons retain the source attribution and licences of their own constructions.
