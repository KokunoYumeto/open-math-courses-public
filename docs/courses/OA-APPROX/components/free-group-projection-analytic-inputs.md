# Analytic inputs for the free-group projection argument

*New original exposition: CC0-1.0 to the extent of rights held.*

This module proves the compact spectral, trace-class and holomorphic-calculus inputs of [Projections in the reduced free group algebra](../src/projections-in-the-reduced-free-group-algebra.md). Hilbert spaces may have arbitrary dimension. Inner products are linear in the second variable.

Our starting proved input is the complete CF1–10 component: scalar completeness and choice, norm separation and norm integrals, the Banach/C\*-spectrum, continuous positive calculus, Hilbert projections and representation of bounded functionals, and completions. The arguments below do not assume a compact spectral theorem, a trace-ideal theorem or a holomorphic functional-calculus theorem.

<a id="pa-compact-spectral"></a>

## PA1. The complete compact self-adjoint argument

Call an operator compact when it is an operator-norm limit of finite-rank operators. Its image of the unit ball is totally bounded: a finite-rank image has a bounded set of finitely many scalar coordinates, which finite scalar grids cover at every tolerance; a norm approximation transfers those covers to the image of the original operator. From every sequence in that image one can therefore select nested subsequences lying in balls of radii tending to zero. The diagonal sequence is Cauchy and converges by Hilbert completeness.

Conversely, a relatively compact unit-ball image has a finite \(\varepsilon\)-net. Project orthogonally onto the span of that finite net; the distance of every image vector to this span is at most \(\varepsilon\). Thus \(\|(1-P)T\|\leq\varepsilon\), and \(PT\) is finite rank. This proves equivalence with the usual compact-operator definition.

Let \(K=K^*\ne0\) be compact. The complete continuous C\*-calculus gives a real \(\lambda\in\operatorname{Sp}(K)\) with \(|\lambda|=\|K\|>0\). There are unit vectors \(\xi_n\) with \(\|(K-\lambda)\xi_n\|\to0\). Indeed, if there were a positive lower bound and no kernel, \(K-\lambda\) would have closed range; its range has orthogonal complement \(\ker(K-\lambda)^*=0\), so would be onto and have a bounded inverse, contradicting its spectrum. If a nonzero kernel already exists, take a unit vector there.

Compactness gives a subsequence with \(K\xi_n\) convergent. The identity
\(\lambda\xi_n=K\xi_n-(K-\lambda)\xi_n\)
makes \(\xi_n\) converge to a unit vector \(\xi\) with \(K\xi=\lambda\xi\). Thus every nonzero compact self-adjoint operator has a nonzero eigenvalue of maximum modulus.

Distinct real eigenvalues have orthogonal eigenspaces by self-adjointness. Each nonzero eigenspace is finite-dimensional: an infinite orthonormal sequence in the eigenspace would have images at pairwise distance \(\sqrt2|\lambda|\), with no convergent subsequence. For each \(\varepsilon>0\), only finitely many eigenvectors, counted with multiplicity, can have eigenvalues of modulus at least \(\varepsilon\), by the same separation argument. Consequently the nonzero eigenspaces together have a countable orthonormal basis \((e_j)\).

The orthogonal complement of their span is invariant under \(K\). The restriction remains compact, since compressions preserve finite rank and norm limits. If it were nonzero, the preceding maximum-eigenvalue argument would give another nonzero eigenvector, a contradiction. Thus this complement is \(\ker K\), and
\[
K\xi=\sum_j\lambda_j e_j\langle e_j,\xi\rangle,\qquad
H=\overline{\operatorname{span}}\{e_j\}\oplus\ker K.
\]
The finite spectral sums converge in operator norm: outside a finite list containing all \(|\lambda_j|\geq\varepsilon\), Pythagoras bounds the remaining operator norm by \(\varepsilon\). This proves the full compact self-adjoint spectral theorem, including an arbitrary-dimensional kernel and every multiplicity.

For a compact \(T\), \(T^*T\) is compact by finite-rank approximation. Its positive square root is compact as well. To see this using the proved continuous calculus, uniformly approximate \(\sqrt t\) on \([0,\|T\|^2]\) by polynomials, then subtract their value at zero. The resulting polynomials vanish at zero and converge to \(\sqrt t\). Each polynomial in \(T^*T\) is compact, and the norm limit is \(|T|\). Apply the preceding theorem to \(|T|\). With its positive eigenvalues \(s_j\) and unit eigenvectors \(v_j\), put
\[
u_j=s_j^{-1}Tv_j.
\]
These vectors are orthonormal, since
\(\langle Tv_i,Tv_j\rangle=\langle v_i,|T|^2v_j\rangle\).
Also \(T\) kills \(\ker|T|\), because
\(\|T\xi\|^2=\langle\xi,|T|^2\xi\rangle\).
We therefore obtain
\[
T=\sum_j s_j\theta_{u_j,v_j},\qquad
\theta_{\xi,\eta}\zeta=\xi\langle\eta,\zeta\rangle.
\]
The finite sums converge in operator norm, with tail norm at most the largest remaining \(s_j\). This also proves the finite-dimensional singular-value decomposition needed for Gram-matrix calculations.

<a id="pa-trace-class"></a>

## PA2. A complete trace-class space and its intrinsic norm

On \(H\odot\overline H\) define the projective norm
\[
\gamma(q)=\inf\left\{\sum_{j=1}^m\|\xi_j\|\|\eta_j\|:
 q=\sum_{j=1}^m\xi_j\otimes\overline{\eta_j}\right\}.
\]
The linear map \(q\mapsto\sum_j\theta_{\xi_j,\eta_j}\) is injective on finite tensors. After combining the first factors into a linearly independent list, zero operator coefficients force every second factor to be zero. Its operator norm is at most the displayed sum, so \(\gamma\) is a genuine norm. Triangle inequality follows by concatenating representations; scalar homogeneity follows by rescaling one factor. Let \(E\) be its Banach completion.

Every element of \(E\) has a representation by a countable series of elementary tensors with
\[
\sum_j\|\xi_j\|\|\eta_j\|<\infty.
\]
Choose finite-tensor approximants with summably small successive \(\gamma\)-differences; represent each difference at cost within a summably small error of its projective norm, and concatenate the finite lists. Their partial sums converge in \(E\) to the given element. Conversely every such series is Cauchy in \(\gamma\), hence converges in \(E\).

The dual of \(E\) is exactly \(B(H)\), through
\[
\Psi_B(q)=\sum_j\langle\eta_j,B\xi_j\rangle,\qquad
\|\Psi_B\|=\|B\|.
\]
The inequality \(\|\Psi_B\|\leq\|B\|\) follows termwise. Unit vector tensors show the reverse inequality by testing \(B\xi\) against unit vectors. Conversely a bounded functional on \(E\), restricted to \(\xi\otimes\overline\eta\), is linear in \(\xi\), conjugate-linear in \(\eta\), and bounded by a constant times \(\|\xi\|\|\eta\|\). Hilbert representation supplies a unique vector \(B\xi\) with this pairing; uniqueness proves linearity in \(\xi\), and the bound proves \(B\in B(H)\). Density gives the full onto dual identification. Norm separation in CF1 consequently gives
\[
\gamma(q)=\sup_{\|B\|\leq1}|\Psi_B(q)|.
\]

The finite-rank map extends continuously to
\[
J:E\longrightarrow B(H),\qquad
Jq=\sum_j\theta_{\xi_j,\eta_j}.
\]
Its image consists of compact operators, because the finite sums converge in operator norm. This extension is still injective. If \(Jq=0\), every rank-one test \(\Psi_{\theta_{u,v}}(q)=\langle v,(Jq)u\rangle\) is zero, hence every finite-rank test is zero. Choose an arbitrary orthonormal basis and let \(P_F\) be its finite coordinate projections. For \(B\in B(H)\), \(P_FBP_F\to B\) strongly and \(\|P_FBP_F\|\leq\|B\|\). Each finite initial portion of the summable vector series for \(q\) therefore has convergent pairings, and its tail is uniformly bounded by \(\|B\|\sum_{j>N}\|\xi_j\|\|\eta_j\|\). Thus \(\Psi_B(q)=\lim_F\Psi_{P_FBP_F}(q)=0\). The exact dual norm gives \(q=0\).

Define \(\mathcal S_1(H)=J(E)\) and \(\|Jq\|_1=\gamma(q)\). Injectivity makes this norm well-defined and transports Banach completeness to \(\mathcal S_1(H)\). It dominates operator norm. Applying \(B\) and \(C\) to a rank-one series transforms its factors to \(B\xi_j,C^*\eta_j\), so
\[
\|BTC\|_1\leq\|B\|\|T\|_1\|C\|.
\]
Taking adjoints interchanges the two factors and conjugates coefficients; it is an isometry for \(\gamma\), giving \(\|T^*\|_1=\|T\|_1\). Finite-rank operators are dense in this norm by construction.

Define
\[
\operatorname{Tr}(T)=\Psi_1(J^{-1}T).
\]
It is linear, representation-independent, and \(|\operatorname{Tr}T|\leq\|T\|_1\). For every orthonormal basis \((e_i)_{i\in I}\),
\[
\sum_i|\langle e_i,Te_i\rangle|
\leq\sum_j\sum_i
 |\langle e_i,\xi_j\rangle\langle\eta_j,e_i\rangle|
\leq\sum_j\|\xi_j\|\|\eta_j\|<\infty.
\]
For each \(j\), the inner sum uses the finite Cauchy–Schwarz inequality and its limit. Each pair has countable coordinate support; their countable union justifies exchanging the absolutely convergent sums even when \(I\) is arbitrary. The basis expansion then gives
\[
\operatorname{Tr}T=\sum_i\langle e_i,Te_i\rangle
 =\sum_j\langle\eta_j,\xi_j\rangle.
\]
This proves basis independence and the complete absolute diagonal formula.

This space and norm are the usual trace class, not merely an operator image with a new norm. For a compact \(T\), use PA1's singular vectors. If \(T\in\mathcal S_1\), the finite-rank contractions
\(B_F=\sum_{j\in F}\theta_{v_j,u_j}\)
give
\[
\sum_{j\in F}s_j=\operatorname{Tr}(B_FT)\leq\|T\|_1.
\]
Hence \(\sum_j s_j<\infty\). Conversely that finite sum condition makes
\(\sum_j s_j\theta_{u_j,v_j}\)
a summable rank-one representation, with norm at most \(\sum_j s_j\). Its operator limit is \(T\), so injectivity of \(J\) identifies it with \(T\) in trace class. The two inequalities prove
\[
\|T\|_1=\sum_j s_j=\operatorname{Tr}|T|.
\]
The positive operator \(|T|=\sum_j s_j\theta_{v_j,v_j}\) also belongs to trace class by the same summable representation, so the displayed \(\operatorname{Tr}|T|\) is defined by our actual trace. In particular, a self-adjoint trace-class operator has an absolutely summable eigenvalue list, with
\[
\|T\|_1=\sum_j|\lambda_j|,\qquad
\operatorname{Tr}T=\sum_j\lambda_j.
\]
Finite-dimensional Gram matrices compute the same norm. The zero space, zero operator, finite rank and arbitrary-dimensional kernel cases are included throughout.

For the series distinction in the projection exercises, dyadic blocks bound \(\sum_{n\geq2}1/n^2\) by a geometric series, whereas each dyadic block of \(\sum_{n\geq2}1/n\) contributes at least \(1/2\). A diagonal compact operator with eigenvalues \(\pm1/n\) is thus Hilbert–Schmidt, meaning its squared singular values are summable, but is not trace class. Cancellation of a merely formal paired series cannot define its trace.

<a id="pa-scalar-contours"></a>

## PA3. Scalar contour identities from differentiability

Norm integrals over piecewise continuously differentiable paths are the complete Riemann integrals of CF1. They satisfy the length bound, respect bounded linear maps and obey the fundamental theorem for derivatives. Uniform convergence permits integration term by term.

For clarity we fix the exact contour constant. The scalar exponential is its absolutely convergent power series. Uniform convergence of its derivative series on bounded real intervals, followed by the fundamental theorem, proves
\(\frac{d}{dt}e^{it}=ie^{it}\);
the absolutely convergent Cauchy product gives \(e^{is}e^{it}=e^{i(s+t)}\) and \(|e^{it}|=1\). Put
\[
A(t)=\int_0^t\frac{ds}{1+s^2},\qquad \pi=4A(1).
\]
Differentiating the quotient of \(e^{2iA(t)}\) and \((1+it)/(1-it)\) gives zero, and its value at zero is one. Thus these expressions agree. At \(t=1\) their value is \(i\). The strictly increasing \(A\) and the rational expression parametrize the first quadrant of the unit circle; multiplication by \(i\) supplies the other three quadrants. Therefore \(e^{it}\), \(0\leq t\leq2\pi\), runs once around that circle. For a continuously differentiable path, each chord is the integral of the derivative on its interval; uniform continuity of the derivative makes its norm differ from the corresponding speed integral by at most the interval length times the derivative's oscillation. Refining partitions proves that chord-sum length equals the integral of speed. The circle's speed is one, so its circumference is \(2\pi\), identifying this constant with the usual \(\pi\). A circle of radius \(r\) consequently has length \(2\pi r\).

For the positively oriented square with vertices \(\pm1\pm i\), the four rotated edge integrals of \(dz/z\) are equal. On the right edge,
\[
\int_{-1}^{1}\frac{i\,dt}{1+it}
 =2i\int_0^1\frac{dt}{1+t^2}.
\]
The odd real term integrates to zero. Hence
\(\int_{\partial Q}dz/z=8iA(1)=2\pi i\).
Translation and rescaling give the same integral around a square centered at any point.

Here is the Cauchy–Goursat proof without assuming a primitive or a second derivative. Let \(f\) be complex differentiable on a neighborhood of a closed triangle. Divide that triangle into four triangles of half the diameter and perimeter. Internal edge integrals cancel. Choose a child whose integral has modulus at least one quarter of the parent's, and repeat. The nested triangles have one common point \(z_0\), by completeness. At that point,
\[
f(z)=f(z_0)+f'(z_0)(z-z_0)+o(|z-z_0|).
\]
The constant and linear terms have zero contour integral by the real fundamental theorem on each edge. On the \(n\)-th triangle the remainder is bounded by \(\varepsilon\) times its diameter, once \(n\) is large. Multiplying that bound by its perimeter and then by \(4^n\) bounds the original integral by \(\varepsilon\) times the original diameter-perimeter product. Letting \(\varepsilon\to0\) proves that the triangle integral is zero.

The same result holds for a region with finitely many polygonal holes. Choose a direction that is parallel to no boundary edge, slice through every boundary vertex in that direction, and subdivide at every resulting edge intersection. Between successive slices, each part of the region is a triangle or trapezoid bounded by two straight boundary segments and the slices; divide each trapezoid by a diagonal. This gives finitely many triangles. Their internal edge integrals cancel, leaving precisely the exterior boundary and the negatively oriented hole boundaries. For a point \(w\) inside such a region, remove a small square centered at \(w\). The function \(f(z)/(z-w)\) is holomorphic on the remaining region, so its exterior boundary integral equals the small-square integral. On that square, replacing \(f(z)\) by \(f(w)\) has error at most a constant times \(\sup|f(z)-f(w)|\), tending to zero. The just-computed square integral therefore yields the scalar Cauchy formula \(2\pi i f(w)\). A point outside the region gives zero instead. Finite unions of squares have winding one at an interior point and zero outside, with hole boundaries negatively oriented.

Smooth circles may replace polygonal boundaries. Inscribed polygonal paths in a compact annular neighborhood converge uniformly to the circle. On each parameter interval their derivative is the average of the circle derivative, by the real fundamental theorem. Uniform continuity of that derivative makes these piecewise derivatives converge in integral norm to the circle derivative. Uniform continuity of the integrand and a common bound for path lengths show convergence of the path integrals. The polygon-to-circle annular regions contain no pole, so the same Cauchy identities pass to circles. This proves the contour and circle formulas used for spectral-gap projections.

<a id="pa-holomorphic-calculus"></a>

## PA4. Holomorphic calculus for a general Banach-algebra element

Let \(x\) lie in a unital Banach algebra \(D\), and let \(K=\operatorname{Sp}_D(x)\). The zero algebra is harmless; otherwise the complete CF Banach-spectrum proof makes \(K\) nonempty and compact. Let \(f\) be holomorphic on an arbitrary open neighborhood \(\Omega\) of \(K\), which may be disconnected.

We construct a surrounding cycle inside \(\Omega\). Choose a sufficiently fine square grid. Include the finitely many closed grid cells that meet \(K\) and one layer of their neighboring cells. Their union \(V\) lies in \(\Omega\), contains \(K\) in its interior, and has boundary disjoint from \(K\); this follows by choosing the cell diameter smaller than a fixed fraction of the positive distance from \(K\) to the complement of \(\Omega\). If that complement is empty, choose any sufficiently fine grid. Cancel shared edges and orient the remaining boundary with \(V\) on the left. Hole boundaries have the opposite orientation. A further two layers produce a larger surrounding cycle, disjoint from the first, still inside \(\Omega\).

The resolvent \(R_x(z)=(z1-x)^{-1}\) is norm-holomorphic. The local Neumann expansion of \(R_x(z+h)\) in \(hR_x(z)\) proves continuity and derivative \(-R_x(z)^2\), with uniform convergence on a smaller resolvent neighborhood. Applying scalar Cauchy–Goursat to every bounded functional on \(D\), and using CF norm separation, proves the Banach-valued polygon and Cauchy identities.

Define
\[
f(x)=\frac1{2\pi i}\int_{\partial V} f(z)R_x(z)\,dz.
\]
It is independent of the grid and the chosen layers. For two possible unions \(V,V'\), their union is polygonal, lies in \(\Omega\), and contains \(K\) inside both subregions. The regions between its boundary and each of the two boundaries avoid \(K\). A finite triangulation of those regions and the Banach-valued Cauchy–Goursat theorem prove equality of the integrals. Overlaying the two finite grids gives the required finite polygonal subdivisions.

The calculus is linear and multiplicative. For multiplication choose the inner and outer surrounding cycles above. The resolvent identity is
\[
R_x(z)R_x(w)=\frac{R_x(w)-R_x(z)}{z-w}.
\]
Continuous Banach-valued integrands on the two compact, disjoint polygonal paths permit interchange of the two norm integrals: both orders are limits of the same finite double Riemann sums. Integrating the first term in \(z\) on the outer cycle gives \(f(w)R_x(w)\) by scalar Cauchy, while integrating the second in \(w\) on the inner cycle gives zero because \(z\) is outside it. The remaining integral is the calculus of \(fg\).

For the constant function one, enlarge the contour to a square about zero with radius exceeding \(\|x\|\). The resolvent has the uniformly convergent expansion
\[
R_x(z)=\sum_{n\geq0}x^n z^{-n-1}.
\]
The \(n=0\) term has integral \(2\pi i\,1\). For \(n>0\), \(z^{-n-1}\) has the single-valued primitive \(-z^{-n}/n\) on the path, so its integral is zero. Thus \(1(x)=1\). Since \(zR_x(z)=1+xR_x(z)\), the identity function has calculus \(x\); multiplicativity then identifies all polynomial calculi. Enlarging the contour for these entire functions is legitimate because the resolvent is holomorphic on the region outside the spectrum.

A bounded unital homomorphism commutes with this calculus: it takes resolvents to resolvents, sends the unit to the codomain unit, and commutes with norm integrals. A representation supported on a projection is unital as a map into that projection corner, so this assertion retains its actual corner unit. No division by the contour parameter \(z\) is introduced.

For self-adjoint \(h\) in a C\*-algebra, every resolvent belongs to the continuous-calculus algebra \(C^*(1,h)\), by the exact spectral identification in CF6. The contour integral belongs to that closed subalgebra as well. Under its identification with continuous functions on \(\operatorname{Sp}(h)\), evaluation at \(t\) sends it to the scalar integral of \(f(z)/(z-t)\), which is \(f(t)\). Therefore this holomorphic calculus agrees with the complete continuous calculus on self-adjoint elements. In particular a holomorphic function with values zero and one on the two spectral clusters produces a self-adjoint projection.

Finally a circle separating one spectral cluster gives its Riesz projection. Replace the circle by nearby polygonal boundaries in the resolvent domain, using PA3, and apply the same norm integral. Its norm estimates use the exact circle length \(2\pi r\). This justifies the radius-\(1/2\) projection and its error bound in the main lesson.

<a id="pa-trace-norm-contours"></a>

## PA5. Trace-norm contour integrals and different representation units

Let \(\pi:D\to B(H)\) and \(\rho:D\to pB(H)p\) be bounded homomorphisms, unital for their actual codomain units \(1,p\). Extend \(\rho\) by zero on \((1-p)H\). Suppose \(P=1-p\) is finite rank and \(\pi(x)-\rho(x)\) is trace class. For a contour in the resolvent set of \(x\), put
\[
R(z)=\pi((z1-x)^{-1}),\qquad
R'(z)=\rho((z1-x)^{-1}).
\]
The corner relations give
\[
R(z)-R'(z)
 =R(z)P+R(z)\bigl(\pi(x)-\rho(x)\bigr)R'(z).
\]
Indeed the product on the right after the finite-rank term is \(R(z)p-R'(z)\), by the two actual resolvent-unit identities. The ideal bound in PA2 proves that the displayed expression is trace class. Resolvent continuity and the same bound make it continuous in trace norm on each compact contour.

Riemann sums therefore converge in the complete trace-class space to the contour integral. The operator-norm embedding, and each representation as a unital map into its actual codomain algebra, commute with that integral. Hence
\[
\pi(f(x))-\rho(f(x))
 =\frac1{2\pi i}\int f(z)
 \left[R(z)P+R(z)\bigl(\pi(x)-\rho(x)\bigr)R'(z)\right]\,dz
 \in\mathcal S_1(H).
\]
This proves the full holomorphic trace-class closure at arbitrary \(f,\Omega,x\), including contours passing through zero when zero is outside the spectrum. Omitting the finite-rank unit term would already fail at \(x=1\).

## Reading

The exact complete CF1–10 input is linked above with its retained programme and component terms. Compact spectral, trace-class and contour arguments in PA1–5 are written here in full. Thomas Schick's [freely readable arXiv v5 paper](https://arxiv.org/pdf/math/9907121v5), Lemmas 2.6, 2.8 and 2.9, provides context for the diagonal trace, different-unit resolvent and projection-difference applications in the main lesson. No referenced trace-ideal or K-theory text is an admitted prerequisite of this module. The human paper retains its own distribution terms; its prose and PDF are not redistributed with this module.
