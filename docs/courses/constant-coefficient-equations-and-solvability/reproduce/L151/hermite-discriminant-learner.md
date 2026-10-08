# Hermite interpolation and local division with a discriminant

*Original examples and complete solutions by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

An analytic remainder is controlled by jets at nearby roots. When roots collide, that control has a loss. The [complete proof](hermite-discriminant-formal.md#h2-the-exact-local-division-theorem) keeps both the ordered and unordered root-distance products and proves the full derivative-strength estimate for a local discriminant, including central collisions. The original function is defined on a complex Euclidean ball; the contour used in the proof stays inside that ball.

## Worked example 1. A cubic Hermite polynomial shows the collision scale

Let \(0<\varepsilon<1\). Take the nodes \(0,\varepsilon\), each of multiplicity two, and
\[
q_\varepsilon(t)=-3(t/\varepsilon)^2+2(t/\varepsilon)^3.
\tag{L151.1}
\]
Its four prescribed jets are
\[
q_\varepsilon(0)=q_\varepsilon'(0)=0,\qquad
q_\varepsilon(\varepsilon)=-1,\qquad
q_\varepsilon'(\varepsilon)=0.
\tag{L151.2}
\]
The derivative is \(-6t/\varepsilon^2+6t^2/\varepsilon^3\), so both first derivatives vanish at their nodes. The sum of the absolute data is one, independently of the collision parameter.

On the closed unit disk the triangle inequality gives
\(|q_\varepsilon|\le3\varepsilon^{-2}+2\varepsilon^{-3}\).
At \(t=-1\) both nonconstant terms are negative real and attain this sum. The supremum on the open disk has the same value, by continuity and radial approach to \(-1\). Hence
\[
\sup_{|t|<1}|q_\varepsilon(t)|
=3\varepsilon^{-2}+2\varepsilon^{-3}.
\tag{L151.3}
\]
The unordered distance is \(D=\varepsilon\), the ordered product is
\(\Delta=\varepsilon^2\), and \(2\bar\mu-1=3\). Therefore
\[
D^3\sup|q_\varepsilon|=2+3\varepsilon,\qquad
\Delta^3\sup|q_\varepsilon|=2\varepsilon^3+3\varepsilon^4.
\tag{L151.4}
\]
The first bound records the actual cubic blowup of the interpolant. The ordered-product bound is valid but weaker.

For the polynomial factors \(Q_1(t)=t\), \(Q_2(t)=t-\varepsilon\), with \(m_1=m_2=2\), the square-free product is \(t(t-\varepsilon)\). Its discriminant is \(R=\varepsilon^2\), and
\[
|R|^{\bar m-1/2}=|\varepsilon^2|^{3/2}=\varepsilon^3.
\tag{L151.5}
\]
This is exactly the stronger scale in L151.4. The full Hermite proof supplies it; treating the ordered product as the unordered one would introduce an extra square.

![Exact collision growth and the two root-distance normalizations](figures/hermite-collision-and-root-products.png)

**Figure H-A.** The normalized real curves
\(\varepsilon^3q_\varepsilon(t)=-3\varepsilon t^2+2t^3\)
keep the exact double-node jets and the attained disk supremum visible. The comparison panel plots the exact norms and both normalizations in L151.3–L151.4. Their values come from the analytic calculation at \(t=-1\), not from maximizing a finite real grid. Proof locators: H1–H7 and H22–H24.

## Worked example 2. Colliding branches give holomorphic coefficients

On \(\mathbb C^2\), let
\[
Q(t,y)=t^2-y,\qquad f(t,y)=e^t.
\tag{L151.6}
\]
For nonzero \(y\) its roots are \(\sqrt y,-\sqrt y\). The two branches may permute around zero, but the remainder coefficients are the entire power series
\[
A(y)=\sum_{j\ge0}\frac{y^j}{(2j)!},\qquad
B(y)=\sum_{j\ge0}\frac{y^j}{(2j+1)!},\qquad
h(t,y)=A(y)+tB(y).
\tag{L151.7}
\]
In square-root notation these are \(\cosh\sqrt y\) and
\(\sinh\sqrt y/\sqrt y\); their power series define them without choosing a global square-root branch. On either nonzero root, \(h=e^t\). At the collision,
\[
h(t,0)=1+t,\qquad
h(0,0)=f(0,0),\qquad
\partial_t h(0,0)=\partial_t f(0,0)=1.
\tag{L151.8}
\]
The limiting double-root Taylor data are retained by the holomorphic coefficients.

There is also an explicit entire quotient:
\[
g(t,y)=\sum_{j\ge1}
\left(\frac1{(2j)!}+\frac{t}{(2j+1)!}\right)
\sum_{l=0}^{j-1}t^{2(j-1-l)}y^l.
\tag{L151.9}
\]
The factorization
\(t^{2j}-y^j=(t^2-y)\sum_{l=0}^{j-1}t^{2(j-1-l)}y^l\)
gives \(e^t=(t^2-y)g+h\). On a fixed compact set the inner sum is bounded by \(jC^{j-1}\), and the factorial denominators make this series uniformly convergent with every fixed derivative. Thus the quotient is jointly entire, including at the colliding roots.

Here \(\widetilde Q(0)=\sqrt5\), because
\(\partial_t^2Q(0)=2\), \(\partial_yQ(0)=-1\), and the other nonzero-order contributions at zero vanish. Since \(\sup_{|t|<1}|Q(t,0)|=1\), the normalization hypothesis holds with \(M=\sqrt5\).
The discriminant is \(R(y)=4y\), so
\[
R(0)=0,\qquad \widetilde R(0)=4.
\tag{L151.10}
\]
The full local estimate has the positive factor
\(\widetilde R(0)^{1/2}=2\). Its replacement by \(|R(0)|^{1/2}\) would give zero and discard precisely the central-collision information.

## Worked example 3. Projection counts both roots and has a smaller area

The hypersurface \(t^2-y=0\) is the smooth complex curve
\(\Gamma(t)=(t,t^2)\). It is a real two-dimensional surface in real four-dimensional space. Its projections onto the \(t\)- and \(y\)-planes are diagrams of that surface, not a representation of the entire induced metric.

Writing \(t=x+iv\), the real map is
\((x,v)\mapsto(x,v,x^2-v^2,2xv)\). Its two tangent vectors have squared length \(1+4|t|^2\) and are orthogonal. Thus
\[
dS=(1+4|t|^2)\,dA(t),\qquad
dA(y)=4|t|^2\,dA(t)
\quad\text{under }y=t^2.
\tag{L151.11}
\]
The second formula is the real Jacobian determinant of complex squaring. Except at zero, the projection has two inverse roots; integrating a sum over both roots equals the corresponding projected integral with this Jacobian. Since
\(4|t|^2\le1+4|t|^2\), the full surface area dominates the projected root-fiber data.

The part of \(\Gamma\) inside the unit Euclidean ball has
\[
|t|^2+|t|^4<1,\qquad
|t|<\sqrt b,\qquad
b=\frac{\sqrt5-1}{2}.
\tag{L151.12}
\]
For \(f(t,y)=t\), its surface data and root-fiber data have the exact integrals
\[
\begin{aligned}
I_S&=\int_{\Gamma\cap B_2(0,1)}|t|\,dS
=2\pi\left(\frac{b^{3/2}}3+\frac{4b^{5/2}}5\right),\\
I_{\mathrm{fiber}}&=
\int_{|y|<b}\bigl(|\sqrt y|+|-\sqrt y|\bigr)\,dA(y)
=\frac{8\pi}{5}b^{5/2},\\
I_S-I_{\mathrm{fiber}}&=\frac{2\pi}{3}b^{3/2}>0.
\end{aligned}
\tag{L151.13}
\]
For the first integral use polar \(t\)-coordinates and L151.11. For the second, the fiber sum is \(2\sqrt{|y|}\); polar \(y\)-coordinates give
\(4\pi\int_0^b \rho^{3/2}\,d\rho\).
This keeps the branch count, the Jacobian and the Euclidean-ball cutoff exact.

![Complex squaring projections and the full surface-area density](figures/branched-projection-and-surface-area.png)

**Figure H-B.** The two complex-plane panels show the projections of the graph \(y=t^2\), its unit-ball parameter disk, and pairs of opposite roots with the same projected point. The density panel compares the exact factors \(1+4|t|^2\) and \(4|t|^2\); their difference is one. The full graph is in \(\mathbb C^2\), not in either drawn plane. L151.11–L151.13 and H31–H32 give the complete area and fiber statements.

## Worked example 4. A unit ball is smaller than a unit polydisk

The function
\[
f(t,y)=\frac1{1-(t+y)/\sqrt2}
\tag{L151.14}
\]
is holomorphic on the unit Euclidean ball: Cauchy–Schwarz gives
\(|t+y|/\sqrt2\le\sqrt{|t|^2+|y|^2}<1\).
It is not holomorphic on the entire unit polydisk, which contains the pole
\((t,y)=(4/5,\sqrt2-4/5)\). Both coordinates have modulus below one; their squared norm is
\(2-8\sqrt2/5+32/25>1\).

For \(Q=t-y\), a local decomposition is
\[
h(y)=\frac{\sqrt2}{\sqrt2-2y},\qquad
g(t,y)=\frac{\sqrt2}{(\sqrt2-t-y)(\sqrt2-2y)},\qquad
f=(t-y)g+h.
\tag{L151.15}
\]
It is valid, for example, on \(|(t,y)|<1/10\). Direct subtraction gives the displayed quotient and verifies the identity. The remainder has degree zero in \(t\). Here
\(\widetilde Q(0)=\sqrt2\), \(R=1\), and \(\widetilde R(0)=1\).

A contour with \(|t|=\rho<2/3\) and \(|y|<\rho'<1/3\) satisfies
\(|(t,y)|<\sqrt5/3<1\). The proof uses precisely such a cylinder inside the known ball, and concludes on a smaller ball. It never needs values of \(f\) at the polydisk pole.

## Exercises with complete solutions

**Exercise 1 (basic: one node).** What does the Hermite estimate become for one node \(a\), multiplicity \(\mu\), and \(\deg q<\mu\)?

**Solution 1.** Both distance products are empty and equal one. The Taylor formula is exact:
\(q(t)=\sum_{j<\mu}q^{(j)}(a)(t-a)^j/j!\).
For \(|t|<1\), \(|a|<1\), every \(|t-a|^j\le2^j\). Therefore
\(\sup|q|\le\sum_{j<\mu}2^j|q^{(j)}(a)|/j!\),
which is bounded by a constant depending only on \(\mu\) times the jet sum. If every jet is zero, the polynomial is zero.

**Exercise 2 (basic: both pair-product conventions).** Compute the two distance products and the discriminant for roots \(-\varepsilon,\varepsilon\), and relate their Hermite exponents when both multiplicities are two.

**Solution 2.** The unordered distance is \(D=2\varepsilon\), while the ordered product has both pair directions and is
\(\Delta=(2\varepsilon)^2=4\varepsilon^2\). The monic square-free polynomial is \(t^2-\varepsilon^2\), whose discriminant is \(R=4\varepsilon^2\). Thus
\(|R|^{3/2}=(2\varepsilon)^3=D^3\), whereas
\(\Delta^3=(2\varepsilon)^6\). The latter is the valid weaker ordered-product bound. It cannot be inserted in place of \(D^3\) to justify the stronger discriminant scale.

**Exercise 3 (intermediate: symmetric coefficients at a branch point).** Compute the root power sums and monic polynomial for the two roots of \(t^2-y\), without selecting a global square root.

**Solution 3.** At a nonzero parameter the odd power sums are zero and the even ones are \(2y^j\). These are polynomials in \(y\) and extend across zero. Newton's first identity gives the first elementary symmetric function as zero. The second gives
\(2e_2=e_1s_1-s_2=-2y\), so \(e_2=-y\). The monic root polynomial is consequently \(t^2-e_1t+e_2=t^2-y\). Its coefficients are holomorphic although its labeled roots may permute. At zero both roots have multiplicity and the same coefficients remain valid.

**Exercise 4 (intermediate: keep the outside roots in a unit).** Let \(Q=(t-y)(t-3)\), \(f=t^2\), and choose the root circle \(|t|=1/2\) for \(|y|<1/10\). Find \(q,B,h,g\).

**Solution 4.** Only the root \(y\) is inside the circle. Hence
\(q=t-y\) and \(B=t-3\). The latter is zero-free on the inner cylinder. The degree-zero remainder is \(h(y)=f(y,y)=y^2\), and
\(f-h=(t-y)(t+y)\). Therefore
\(g(t,y)=(t+y)/(t-3)\), holomorphic on that cylinder, and
\(f=Qg+h\). The outside factor belongs in the analytic unit \(B\); treating it as another inside interpolation node would unnecessarily change the remainder degree.

**Exercise 5 (intermediate: strength at a vanishing value).** For \(R(y)=y^3+\varepsilon\), compute \(\widetilde R(0)\) and its limit as \(\varepsilon\to0\).

**Solution 5.** The only nonzero derivatives at zero are the value \(\varepsilon\) and third derivative \(6\). Thus
\(\widetilde R(0)=\sqrt{|\varepsilon|^2+36}\to6\).
At \(\varepsilon=0\), the point value is zero but the strength remains six. This example concerns the polynomial-strength mean lemma H6; no assertion that every polynomial in this exercise is the discriminant of a particular specified factorization is needed.

**Exercise 6 (intermediate: a loose uniform exponent).** Explain why \(K=m^3\) bounds the contribution of the outside root distances in H24.

**Solution 6.** There are at most \(m(m-1)/2\) unordered root pairs. Every outside-pair factor in the discriminant is a squared distance. Raising to \(a_*=\bar m-1/2\le m-1/2\) gives total distance exponent at most
\(m(m-1)(m-1/2)<m^3\). Each distance is bounded by \(C_{n,m}A_0\), and \(A_0\ge m!\ge1\). All fixed constants are absorbed into \(C\), and increasing the power of \(A_0\) to \(m^3\) preserves the inequality. This is a sufficient loose power, not an assertion of an optimal loss.

**Exercise 7 (advanced: why the weighted mean is uniform).** Supply the contradiction argument proving the uniform lower log mean for a compact coefficient family of nonzero polynomials.

**Solution 7.** If the integrals on the observation ball had no lower bound, take a sequence with integrals tending to minus infinity. Coefficient compactness gives a subsequence converging to a nonzero polynomial. Choose one point where its value is nonzero, giving a positive lower bound for the sequence's moduli there. Bounded coefficients give a common upper bound for their logarithms on a larger ball centered at that point and containing the observation ball. Proper logarithms are locally integrable and subharmonic. Subtract them from the common upper bound; the resulting nonnegative superharmonic functions have integrals on the larger ball bounded by its volume times their uniformly bounded values at the chosen point. Their integrals on the observation ball are also bounded. This contradicts the proposed diverging negative log integrals. Translated normalized polynomials remain in a compact nonzero family, so the same argument is uniform over the inner centers used in H6.

**Exercise 8 (advanced: graph and projection Jacobians).** Verify L151.11 directly from the real map \((x,v)\mapsto(x,v,x^2-v^2,2xv)\), including the twofold projection.

**Solution 8.** Its derivative columns are
\((1,0,2x,2v)\) and \((0,1,-2v,2x)\).
Their inner product is zero and their squared lengths are
\(1+4(x^2+v^2)\). The square root of their Gram determinant is therefore \(1+4|t|^2\). For the projection to \(y\), its derivative matrix is
\(\begin{pmatrix}2x&-2v\\2v&2x\end{pmatrix}\),
with determinant \(4|t|^2\). Every nonzero \(y\) has the two roots \(t,-t\); each must be counted in the fiber sum. The critical point \(t=0\) has zero projected Jacobian but is a single null parameter point. The surface parametrization itself remains an immersion there, with area density one.

**Exercise 9 (advanced: one-dimensional local division).** Describe the estimate for \(Q(t)=t^\mu\), and the empty cluster for \(Q(t)=t-2\).

**Solution 9.** For \(Q=t^\mu\) use the single square-free factor \(Q_1=t\), \(m_1=\mu\). Its discriminant is the empty product one. The remainder is the Taylor polynomial of \(f\) at zero of degree below \(\mu\); the quotient is the analytic remainder divided by \(t^\mu\). The surface data are the counting-measure jets \(\sum_{a<\mu}|f^{(a)}(0)|\), and the bound follows directly as in Exercise 1. For \(Q=t-2\), a circle of radius \(1/2\) contains no root. The contour remainder is zero, and \(g=f/(t-2)\) is holomorphic on the inner disk. Its remainder estimate has left side zero.

**Exercise 10 (advanced: protect the Euclidean-ball domain).** Prove that the pole in Example 4 lies outside the unit ball but inside the unit polydisk. Explain why the proof contour is still legal.

**Solution 10.** The two pole coordinates are \(4/5\) and \(\sqrt2-4/5\). The latter lies in \((0,1)\) because \(4/5<\sqrt2<9/5\). Their squared norm exceeds one since
\[
\frac{32}{25}+2-\frac{8\sqrt2}{5}>1
\quad\Longleftrightarrow\quad
\frac{57}{25}>\frac{8\sqrt2}{5}.
\tag{L151.16}
\]
Both sides are positive; squaring gives \(3249/625>3200/625\). Thus the pole is outside the ball and inside the polydisk. The actual contour instead has \(|t|<2/3\), \(|y|<1/3\), giving squared norm below \(5/9\). It lies wholly in the unit ball where the original function is known. The quotient and remainder are then defined on an even smaller cylinder, and the theorem restricts their conclusion to a smaller Euclidean ball.

## Reproducibility and source map

The formal source gives the entire Hermite proof, both distance-product conventions, the uniform analytic factors, contour division, discriminant-weighted fiber estimate, full polynomial-strength mean lemma and the exact surface projection bound. Its statements match Hörmander II, §15.3, Lemmas 15.3.4–15.3.5, printed pp. 292–293. The strength convention is formula 10.4.2, printed p. 32.

The figure source retains exact collision parameters, complex root maps, unit-ball cutoff and real Gram/Jacobian densities. Independent calculations reconstruct the interpolation from its actual jets, evaluate contour remainders, differentiate the surface map and integrate the actual surface and fiber data. They supplement the full proof. The global hypersurface area bound and surface solution representation require the subsequent arguments and remain separate.
