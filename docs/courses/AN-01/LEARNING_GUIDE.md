# Learning with singular measurements

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Text: CC0.*

A distribution records what a localized smooth measurement sees. This course follows that idea through three questions: how a singular object acts on tests, how an operator transports those measurements, and how support or frequency information constrains the result. The following two calculations give a concrete starting point. The routes below then identify the proofs needed for each question.

## Start with an impulse and its derivative

Choose a nonnegative smooth function \(\rho\) supported in \([-1,1]\), with integral one and \(\rho(0)>0\). For \(\varepsilon>0\), its rescaling \(\rho_\varepsilon(x)=\varepsilon^{-1}\rho(x/\varepsilon)\) has height of order \(1/\varepsilon\). Its value at the origin tends to infinity. Nevertheless every smooth compactly supported measurement has a limit:

\[
\begin{gathered}
\int\rho_\varepsilon(x)\phi(x)\,dx\\
=\int\rho(t)\phi(\varepsilon t)\,dt,\\
\left|\int\rho_\varepsilon\phi-\phi(0)\right|\\
\le\varepsilon\|\phi'\|_\infty\int|t|\rho(t)\,dt.
\end{gathered}
\tag{G1}
\]

The equality is the substitution \(x=\varepsilon t\). The bound is the fundamental theorem of calculus between zero and \(\varepsilon t\), followed by integration against the nonnegative \(\rho\). Thus the measurements approach evaluation at zero, the distribution \(\delta_0\).

Integration by parts gives the derivative measurement and its sign:

\[
\begin{gathered}
\int\rho'_\varepsilon(x)\phi(x)\,dx\\
=-\int\rho(t)\phi'(\varepsilon t)\,dt,\\
\left|\int\rho'_\varepsilon\phi+\phi'(0)\right|\\
\le\varepsilon\|\phi''\|_\infty\int|t|\rho(t)\,dt.
\end{gathered}
\tag{G2}
\]

The limiting functional is \(\delta'_0(\phi)=-\phi'(0)\). The negative sign is part of the definition of a distributional derivative. Both errors are uniform over test families with the displayed derivative norm bounded. The support and bounded-family lemma in [*Distributions as kernels of continuous operators*](src/distributions-as-kernels.md), “What continuity means,” explains why this also gives strong distributional convergence on bounded test families. [*Order, positivity and distributional limits*](src/order-positivity-and-limits.md) develops the convergence and order arguments further.

These estimates explain what “order” measures: evaluation needs a zeroth derivative bound; its derivative needs a first derivative bound. They do not bound the height of an approximating function. [*Jets, supported distributions and local operators*](src/jets-supported-distributions-and-local-operators.md), Theorems 3.1, 3.3 and 3.4, identifies all finite-order distributions concentrated on a plane and proves how the orders of their transverse and tangential measurements combine.

## Watch an operator move a measurement

Consider \(T_h\phi(x)=\phi(x+h)\). Its kernel is concentrated on the graph \(y=x+h\). On a smooth compactly supported test \(H(x,y)\) of two real variables, define

\[
\begin{gathered}
K_h(H)=\int H(x,x+h)\,dx,\\
K_h(\psi\otimes\phi)\\
=\int\psi(x)\phi(x+h)\,dx.
\end{gathered}
\tag{G3}
\]

This is a distribution: for a fixed compact support of \(H\), its projection on the \(x\) axis lies in a bounded interval \(I\), and the pairing has absolute value at most \(|I|\|H\|_\infty\). A test whose support misses the graph gives zero. This particular kernel therefore represents translation and exhibits its support directly.

For \(h\ne0\), the difference quotient tends to
\(L(H)=\int\partial_yH(x,x)\,dx\). In fact Taylor's integral remainder gives

\[
\begin{gathered}
\left|\frac{K_h(H)-K_0(H)}h-L(H)\right|\\
\le \frac{|h|}{2}|I|\|\partial_y^2H\|_\infty.
\end{gathered}
\tag{G4}
\]

The same interval \(I\) contains the projection of the compact test support at every height in this calculation. Outside it, \(H(x,y)\) and its derivatives vanish for every \(y\). The factor \(1/2\) comes from \(\int_0^1(1-t)\,dt\). On product tests, \(L(\psi\otimes\phi)=\int\psi\phi'\). Hence the kernel of differentiation is \(L=-\partial_yK_0\): differentiating a distribution introduces a negative sign, while the operator differentiates its input with a positive sign.

The kernel theorem in [*Distributions as kernels of continuous operators*](src/distributions-as-kernels.md), Theorem 4.1, proves that every operator satisfying the stated continuity conditions has one unique kernel; the example above supplies a kernel directly. [*When a kernel is smooth*](src/when-a-kernel-is-smooth.md) identifies when such a distribution is a smooth function. [*Tensor products and parameter-dependent distributions*](src/tensor-products-and-parameters.md) supplies the complete product and parameter-pairing proofs. [*Jets, supported distributions and local operators*](src/jets-supported-distributions-and-local-operators.md), Theorem 4.1, turns concentration on the diagonal into a locally finite differential operator.

The full [integral Taylor proof](src/when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) justifies the remainder estimate above, including either sign of the increment.

## Choose a route by the question

The lesson numbers identify stable files. Within a route, follow the linked prerequisite sections and the complete providers named by each lesson.

- **Can local measurements be joined or multiplied?** Begin with [*Local data and compatible products*](src/local-data-and-compatible-products.md) and [*Weak equations and classical functions*](src/weak-equations-and-classical-functions.md). The gluing proofs explain local definitions; the product conditions explain why two individually meaningful distributions cannot always be multiplied.
- **What does support geometry permit?** The normal-jet theorem leads to [*Compatible jets on closed sets*](src/compatible-jets-on-closed-sets.md), [*Paths control supported distributions*](src/paths-control-supported-distributions.md) and [*Locality forces continuity*](src/locality-forces-continuity.md). For a physical boundary, continue to *Boundary flux and weak identities* and [*Lipschitz graphs and surface measures*](src/lipschitz-graphs-and-surface-measures.md). The normal direction and the sign of a boundary source are part of the mathematics.
- **How do sources propagate?** [*Convolution as addition of supports*](src/convolution-as-addition-of-supports.md) proves the proper-support condition before a convolution is defined. [*Causal integration of complex order*](src/causal-integration-of-complex-order.md) and [*Causal point sources and characteristic cones*](src/causal-point-sources-and-characteristic-cones.md) then connect support constraints to evolution kernels. [*Convex supports and convolution cancellation*](src/convex-supports-and-convolution-cancellation.md) studies which support information survives cancellation.
- **How does a complex boundary encode a singularity?** Start with [*Cauchy kernels and distributional boundary limits*](src/cauchy-kernels-and-boundary-limits.md), then [*Gluing holomorphic sides*](src/gluing-holomorphic-sides.md) and [*Holomorphic boundaries in convex cones*](src/holomorphic-boundaries-in-convex-cones.md). The finite-part, complex-power and homogeneous-extension lessons apply these boundary and jet proofs to explicit singularities.
- **What can frequency data determine?** [*Tempered growth and spectral cutoffs*](src/tempered-growth-and-spectral-cutoffs.md) sets the global growth framework. The finite-spectrum, periodic-sampling and compact-spectrum lessons distinguish discrete frequencies, spectral gaps and support bounds. *Fourier–Laplace slices and boundary poles* recovers weighted inputs from analytic observations. The Gaussian, quadratic-transform and oscillatory lessons then examine how those observations change under weights, phases and differential operators.

- **How can a finite-order zero be divided uniformly?** After [*Zero hypersurfaces as curvature measures*](src/zero-hypersurfaces-as-curvature-measures.md), read *Classical finite-order preparation and division*. It separates the holomorphic uniqueness theorem from smooth existence and follows coefficients through root collisions, derivative losses and actual input domains.

- **What remains after solving several smooth complex equations?** After *Classical finite-order preparation and division*, read [*Smooth complex equations and flat remainders*](src/smooth-complex-equations-and-flat-remainders.md). Follow common neighborhoods, smooth complex graphs and remainders that belong to every ideal power.
- **Can a real finite-order zero become a polynomial by changing coordinates?** Continue with [*An oriented coordinate normal form for a real finite-order zero*](src/oriented-coordinate-normal-form.md). Its local flow keeps the function value and proves the distinguished coordinate's orientation directly.

Every available lesson contains its own graded problems and complete solutions. The course status identifies the remaining mathematical topics, including smooth and analytic wavefront sets, analytic functionals and hyperfunctions. Those topics remain part of the course's assigned scope.

## Sources and contributions

The course uses independently written proofs and teaching organization, drawing on the works identified in each lesson. These include Hörmander's second-edition reprint, DOI 10.1007/978-3-642-61497-2, and the named free sources. Laurent Schwartz's distribution and kernel theory is a foundational contribution. Individual bibliographies credit the actual mathematical inputs; source books do not supply an exercise sequence or replace the proofs given here.

The guide retains its original GPT-6.1 Sol (OpenAI) authorship. The repaired lesson editions identify their own authors and prior contributions; the current source and prerequisite corrections were made by GPT-6 Astra (OpenAI), Ultra. Complete earlier programme proofs are linked at the point of use with exact lesson and section locators. Those providers retain their stated component licences; the independently authored text here is CC0. Source credit and proof dependencies serve different purposes: credit identifies the mathematical contributions, while an internal proof link identifies the argument a reader needs.
