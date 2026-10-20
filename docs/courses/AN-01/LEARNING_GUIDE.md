# Learning with singular measurements

*Introductory calculations and foundational reading routes by GPT-6.1 Sol (OpenAI). Advanced reading routes and programme integration by GPT-6 Astra (OpenAI). October 2026. Text: CC0.*

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
- **What does support geometry permit?** The normal-jet theorem leads to [*Compatible jets on closed sets*](src/compatible-jets-on-closed-sets.md), [*Paths control supported distributions*](src/paths-control-supported-distributions.md) and [*Locality forces continuity*](src/locality-forces-continuity.md). For a physical boundary, continue to [*Boundary flux and weak identities*](src/boundary-flux-and-weak-identities.md) and [*Lipschitz graphs and surface measures*](src/lipschitz-graphs-and-surface-measures.md). The normal direction and the sign of a boundary source are part of the mathematics.
- **How do sources propagate?** [*Convolution as addition of supports*](src/convolution-as-addition-of-supports.md) proves the proper-support condition before a convolution is defined. [*Causal integration of complex order*](src/causal-integration-of-complex-order.md) and [*Causal point sources and characteristic cones*](src/causal-point-sources-and-characteristic-cones.md) then connect support constraints to evolution kernels. [*Convex supports and convolution cancellation*](src/convex-supports-and-convolution-cancellation.md) studies which support information survives cancellation.
- **How does a complex boundary encode a singularity?** Start with [*Cauchy kernels and distributional boundary limits*](src/cauchy-kernels-and-boundary-limits.md), then [*Gluing holomorphic sides*](src/gluing-holomorphic-sides.md) and [*Holomorphic boundaries in convex cones*](src/holomorphic-boundaries-in-convex-cones.md). The finite-part, complex-power and homogeneous-extension lessons apply these boundary and jet proofs to explicit singularities.
- **What can frequency data determine?** [*Tempered growth and spectral cutoffs*](src/tempered-growth-and-spectral-cutoffs.md) sets the global growth framework. The finite-spectrum, periodic-sampling and compact-spectrum lessons distinguish discrete frequencies, spectral gaps and support bounds. [*Fourier–Laplace slices and boundary poles*](src/fourier-laplace-slices-and-boundary-poles.md) recovers weighted inputs from analytic observations. The Gaussian, quadratic-transform and oscillatory lessons then examine how those observations change under weights, phases and differential operators.

- **How can a finite-order zero be divided uniformly?** After [*Zero hypersurfaces as curvature measures*](src/zero-hypersurfaces-as-curvature-measures.md), read [*Classical finite-order preparation and division*](src/classical-finite-order-preparation-and-division.md). It separates the holomorphic uniqueness theorem from smooth existence and follows coefficients through root collisions, derivative losses and actual input domains.

- **What remains after solving several smooth complex equations?** After [*Classical finite-order preparation and division*](src/classical-finite-order-preparation-and-division.md), read [*Smooth complex equations and flat remainders*](src/smooth-complex-equations-and-flat-remainders.md). Follow common neighborhoods, smooth complex graphs and remainders that belong to every ideal power.
- **Can a real finite-order zero become a polynomial by changing coordinates?** Continue with [*An oriented coordinate normal form for a real finite-order zero*](src/oriented-coordinate-normal-form.md). Its local flow keeps the function value and proves the distinguished coordinate's orientation directly.

- **Which derivative bounds describe a singular direction?** Read [*Derivative growth and finite-order localization*](src/derivative-growth-and-finite-order-localization.md), [*Cones and derivative-growth wavefronts*](src/cones-and-derivative-growth-wavefronts.md) and [*Analytic maps and derivative growth*](src/analytic-maps-and-derivative-growth.md). The proofs track the growing derivative order, compact cutoffs and changes of variables.
- **How do holomorphic functions recover directional singularities?** [*Holomorphic boundaries and analytic directions*](src/holomorphic-boundaries-and-analytic-directions.md) proves the forward cone bound. Continue through [*Holomorphic decompositions of tempered distributions*](src/holomorphic-decompositions-of-tempered-distributions.md), [*Continuing the spherical kernel*](src/continuing-the-spherical-kernel.md) and [*Boundary regularity and conic decomposition*](src/boundary-regularity-and-conic-decomposition.md). [*From wavefront cones to holomorphic wedges*](src/from-wavefront-cones-to-holomorphic-wedges.md) supplies the converse and states exactly where a regular remainder is local.
- **Can singular directions be prescribed or transformed?** [*Prescribing every singular direction*](src/prescribing-every-singular-direction.md) constructs distributions with an assigned closed conic wavefront. [*Fourier rotation and directions at infinity*](src/fourier-rotation-and-directions-at-infinity.md) treats homogeneous Fourier correspondence and origin fibers. [*Analytic pullback and cotangent directions*](src/analytic-pullback-and-cotangent-directions.md) and [*Keeping zero covectors in kernel operations*](src/keeping-zero-covectors-in-kernel-operations.md) state the actual hypotheses for substitution, products, integration and composition.
- **What forces analytic uniqueness or characteristic propagation?** Start with [*Both analytic directions at support boundaries*](src/both-analytic-directions-at-support-boundaries.md) and [*Characteristic motion and closed-set barriers*](src/characteristic-motion-and-closed-set-barriers.md). [*Analytic equations and characteristic directions*](src/analytic-equations-and-characteristic-directions.md) connects differential estimates to uniqueness. The [half-space](src/characteristic-half-spaces-and-ramified-roots.md) and [convex-domain](src/characteristic-planes-and-convex-domain-uniqueness.md) lessons give exact geometric examples. [*Analytic parametrices and straight characteristics*](src/analytic-parametrices-and-straight-characteristics.md) proves propagation, while [*A whole characteristic line with smooth forcing*](src/a-whole-characteristic-line-with-smooth-forcing.md) constructs a global singular ray with smooth forcing.
- **When does a reciprocal control analytic regularity?** [*Analytic regularity for convolution equations*](src/analytic-regularity-for-convolution-equations.md) keeps the reciprocal identity distributional and proves the estimate on proper support sums. [*Imaginary displacements and microhyperbolic cones*](src/imaginary-displacements-and-microhyperbolic-cones.md) starts from imaginary zero avoidance, proves the general cone theorem and distinguishes actual wavefront fibers from their optimal convex bounds. [*Exact waves on a single light ray*](src/exact-waves-on-a-single-light-ray.md) constructs a homogeneous wave with one covector sign and relates it to smooth Gaussian packets.

- **How can a point measure infinitely many derivatives?** [*Analytic tests and real carriers*](src/analytic-tests-and-real-carriers.md) proves the moment criterion, Gaussian approximation near arbitrary real compact sets, the extension to local holomorphic tests, and the precise inclusion of compact distributions. Its carrier operations lead to the Fourier–Laplace estimate and uniqueness.

- **Can an exterior harmonic field reveal an analytic source?** [*Recovering analytic data from harmonic fields*](src/recovering-analytic-data-from-harmonic-fields.md) proves the entire odd harmonic lift, the Poisson half-jump normalization and recovery by compact cutoff tests. Its converse identifies the entire harmonic ambiguity and gives the smallest real carrier from harmonic continuation.

- **How can analytic sources be divided without analytic cutoffs?** [*Localizing analytic sources without analytic cutoffs*](src/localizing-analytic-sources-without-analytic-cutoffs.md) splits a functional over arbitrary real compact carriers by correcting a smooth cutoff in its harmonic field. It proves the exact overlap ambiguity and completeness when differences eventually concentrate near a smaller carrier, including initially complex carriers and sequences with unbounded size.

- **How do analytic sources define local objects on a manifold?** [*Hyperfunctions from local analytic sources*](src/hyperfunctions-from-local-analytic-sources.md) constructs boundary quotients, proves restriction and gluing for arbitrary covers, and identifies compact sections with analytic functionals. It gives coordinate changes and atlas independence, then extends every section with support in the closure of its domain. Examples distinguish these extensions from distributional ones and describe their full boundary ambiguity.

- **Can a holomorphic function have a boundary even when it grows faster than every power?** [*Holomorphic boundary values without growth bounds*](src/holomorphic-boundary-values-without-growth-bounds.md) constructs that boundary as a hyperfunction, reads its analytic singular directions from a spherical kernel, and proves the positive-dual bound and its converse. It proves uniqueness and analytic joining of opposite sides. An essential singularity gives a boundary beyond distributions and an explicit infinite point-supported jump.

- **How do different holomorphic sides represent the same singular object?** [*Directional splitting and holomorphic compatibility*](src/directional-splitting-and-holomorphic-compatibility.md) separates hyperfunctions by any finite closed conic cover. It proves that the exact ambiguity consists of antisymmetric exchanges on cone intersections, represented by holomorphic functions on sums of approach cones. Worked examples distinguish the intrinsic hyperfunction from its noncanonical angular pieces.

- **When can a singular object be substituted into an analytic map?** [*Analytic substitution for hyperfunctions*](src/analytic-substitution-for-hyperfunctions.md) constructs noncharacteristic pullback, proves its precise covector bound and representation independence, and compares it with the existing distribution and coordinate definitions. It includes exact submersion equality, the inverse absolute Jacobian, and examples reaching beyond distributions.

- **When can singular objects be multiplied?** [*Tensor directions and admissible hyperfunction products*](src/tensor-directions-and-admissible-hyperfunction-products.md) retains every zero covector component, constructs products by diagonal restriction and proves their chain and Leibniz rules. It gives the joint condition for finite products and examples showing why individual or pairwise conditions can be insufficient.

- **What survives integration over a fiber?** [*Integrating hyperfunctions over proper fibers*](src/integrating-hyperfunctions-over-proper-fibers.md) constructs the proper integral, proves that only zero fiber covectors survive and checks its derivative, coordinate and iterated-integration rules. A parabolic fold shows exactly how an integrable singularity appears at a critical output value.

- **How can a kernel act on a singular input?** [*Singular inputs and zero covectors in hyperfunction kernels*](src/singular-inputs-and-zero-covectors-in-hyperfunction-kernels.md) gives the normal exclusion, output-axis terms and full relation for contracting two kernels. It constructs proper convolution and proves associativity using compact analytic representatives, with examples reaching beyond distributions.

- **What does the boundary of a hyperfunction support force?** [*Support normals force both hyperfunction directions*](src/support-normals-force-both-hyperfunction-directions.md) detects compact fibers through all analytic weights, using a uniform Baire estimate and Cauchy reconstruction. It proves both normal signs, rough and convex contact, and uniqueness from a nonempty open zero set, without growth bounds.

- **When does a contracted kernel give the successive actions?** [*Interchanging hyperfunction integration and analytic substitution*](src/interchanging-hyperfunction-integration-and-analytic-substitution.md) proves the noncharacteristic interchange theorem, the singular projection formula and finite kernel associativity. Fixed fiber boundaries, exact carrier comparisons and canceling exponential tails handle hyperfunctions of arbitrary growth.

- **How can analytic iteration survive a loss of derivatives?** [*Analytic Cauchy data on small polydiscs*](src/analytic-cauchy-data-on-small-polydiscs.md) pairs Cauchy derivative costs with weighted zero-data primitives. It proves quantitative local existence, an explicit iteration remainder, uniqueness of analytic germs and the thin rescaling that permits arbitrary analytic normal data.

- **How far does a local analytic Cauchy solution continue?** [*Continuing analytic Cauchy solutions through convex domains*](src/continuing-analytic-cauchy-solutions-through-convex-domains.md) follows noncharacteristic boundaries through expanding convex domains. It proves compatibility of local extensions, global existence, complex-cone solvability and continuation through the cone vertex when the forcing extends.

- **What does an analytic equation control for a hyperfunction?** [*Noncharacteristic equations for hyperfunctions*](src/noncharacteristic-equations-for-hyperfunctions.md) proves equality of solution and forcing singular directions off the characteristic set. It constructs solutions modulo a directionally regular error, explains their quotient uniqueness, defines traces of solutions already given across a noncharacteristic surface and proves Holmgren uniqueness.

- **How does a solution on one side acquire Cauchy data?** [*Supported division and one-sided Cauchy data*](src/supported-division-and-one-sided-cauchy-data.md) divides arbitrary sources supported on a noncharacteristic surface, selects a unique extension by its finite boundary source, and recovers the normal jets through an exact triangular matrix. It proves agreement with classical, extendible distributional and two-sided hyperfunction traces, including coordinate changes.

- **How does a Gaussian detect an analytic singularity?** [*Gaussian windows and analytic directions*](src/gaussian-windows-and-analytic-directions.md) proves the exact exponential criterion for arbitrary compact hyperfunctions. It connects carrier displacement, a corrected inversion formula, recovery on the imaginary sphere and local representative independence.

- **How does physical support constrain a singular fiber?** [*Tangent support and analytic directions*](src/tangent-support-and-analytic-directions.md) places both signs of every fiber normal in the tangent cone of physical support. It treats affine sections through closure after projection, propagates regularity through convex fiber regions, and proves analytic boundary regularity at every normal frequency. An explicit integral solution shows why smooth Cauchy data do not give that conclusion.

- **Which entire functions represent a compact real source?** [*Entire growth and convex real carriers*](src/entire-growth-and-convex-real-carriers.md) constructs the Fourier–Laplace inverse for every compact convex real carrier using rotated Laplace rays and small Cauchy contours. It includes infinite point derivatives and explains exactly which information a nonconvex set loses in its support function.

- **Can regular germs have global representatives?** [*Global regular differences*](src/global-regular-differences.md) constructs a global function of the same derivative-growth class up to an analytic difference, using Gaussian centers in a small ball. It proves the global wavefront intersection formula and simultaneous representation at finitely many points.

- **How can smooth data cross a boundary or descend through a symmetry?** [*Smooth extension and symmetry coordinates*](src/smooth-extension-and-symmetry-coordinates.md) constructs one extension operator preserving every finite derivative order, then resolves coordinate parity and exchange symmetry. It also gives smooth positive majorants with a flat boundary.

- **How can oscillation permit a singular function to cross an endpoint?** [*Oscillation and extension order*](src/oscillation-and-extension-order.md) gives the exact finite-order threshold, excludes equality, and constructs a real phase for an arbitrary continuously differentiable amplitude.

- **What survives a concentrating or rapidly oscillating limit?** [*Concentration and oscillatory limits*](src/concentration-and-oscillatory-limits.md) computes point masses, periodic limits and a radial center contribution, resolves two boundary parameters, and proves when weak convergence becomes locally uniform.

- **How do crossings and moving poles affect products?** [*Products, crossings and singular limits*](src/products-crossings-and-singular-limits.md) proves product principal values, quartic subtractions, the logarithmic axis-crossing limit and the exact separation law for overlapping kernels.

- **When does a distribution extend across an endpoint?** [*Primitives and endpoint extension*](src/primitives-and-endpoint-extension.md) proves interval primitive estimates, the finite-measure extension criterion, explicit weighted subtractions and the exact order allowed by an exponential phase.

- **What remains when singular poles cancel?** [*Reciprocal scaling and cancellation at a pole*](src/reciprocal-scaling-and-pole-cancellation.md) proves reciprocal-tail compression, convergent finite-difference formulas for every derivative, and the full smooth-coefficient boundary limits with their point terms.

- **When can a smooth function divide a distribution?** [*Jumps, point jets and smooth division*](src/jumps-jets-and-smooth-division.md) calculates reflected endpoint terms, classifies division by smooth functions on intervals, and proves the obstruction at a flat zero.

- **What happens when a differential coefficient vanishes?** [*Equations across degenerate points*](src/equations-across-degenerate-points.md) classifies flat and growing branches, point-forced solutions, and the exact piecewise constants and point terms at locally finite zeros.

- **How do multipliers constrain singular distributions?** [*Normal jets and parabolic poles*](src/normal-jets-and-parabolic-poles.md) describes finite normal jets with unrestricted tangential coefficients, solves simultaneous polynomial constraints, and proves a directional uniqueness criterion and exact parabolic pole orders.

- **When do singular families converge to points or curves?** [*Concentration and logarithmic boundaries*](src/concentration-and-logarithmic-boundaries.md) proves the full Hessian criterion for planar concentration, a logarithmic condition for cut boundary values, and convergence of moving logarithmic sources to circular arclength.

- **How do boundaries determine derivatives and division?** [*Boundary derivatives, division and moving jumps*](src/boundary-derivatives-division-and-moving-jumps.md) proves exact graph derivative orders, the complete criterion for division by a quadratic smooth multiplier, all interfaces in a weak-solution family, and logarithmic branch jumps.

- **How do cancellation and damping combine?** [*Weighted cancellation for complex phases*](src/weighted-cancellation-for-complex-phases.md) proves a finite-regularity integral bound with precise gradient and imaginary-part weights, a nonnegative derivative estimate, and the uniform passage through degenerate points.

- **Which finite jets determine a stationary integral?** [*Finite stationary jets and quadratic exchange*](src/finite-stationary-jets-and-quadratic-exchange.md) derives the complex quadratic remainder, the full finite-derivative stationary expansion and the exact algebra of nilpotent quadratic exchange, with its sharp order loss.

- **What does a Fourier pairing do to a nonlinear phase?** [*Paired variables and stationary parameters*](src/paired-variables-and-stationary-parameters.md) follows real critical points through parameters and proves the paired-phase expansion with its exact derivative count, factorials and sharp half-order mechanism.

- **How does a small boundary value control the interior?** [*Boundary smallness and harmonic weights*](src/boundary-smallness-and-harmonic-weights.md) constructs a positive harmonic weight from disk comparison, proves quantitative boundary propagation on general upper domains, and recovers full decay orders.

- **What replaces a missing real critical point?** [*Virtual critical points and explicit coefficients*](src/virtual-critical-points-and-explicit-coefficients.md) derives the explicit Gaussian coefficients from a smooth complex critical graph, with its positive critical value, oriented Jacobian and independence of representatives.

- **How does curvature control lattice counts?** [*Curvature, two boundary points and lattice counts*](src/curvature-two-boundary-points-and-lattice-counts.md) computes the two normal phases of a convex body, proves a smooth Fourier summation identity and balances the two smoothing errors.

- **How does a boundary change stationary phase?** [*Half-space phases and the Fresnel transition*](src/half-space-phases-and-the-fresnel-transition.md) proves the three local boundary regimes, their complete coefficients and remainders, and the Fresnel transition between an exterior and an interior critical point.

- **Which powers survive a degenerate critical point?** [*Finite-order phases and missing powers*](src/finite-order-phases-and-missing-powers.md) derives every finite-order coefficient with its exact remainder, identifies the missing powers, and gives the two canonical Airy profiles through a cubic collision.

- **How do two critical points merge?** [*Cubic collisions and uniform amplitudes*](src/cubic-collisions-and-uniform-amplitudes.md) constructs smooth polynomial coordinates, expands every compact amplitude in two Airy profiles, and treats one cubic direction together with transverse quadratic directions.

- **When does cancellation define a distribution?** [*Complex phases and oscillatory distributions*](src/complex-phases-and-oscillatory-distributions.md) constructs complex-phase distributions across the full symbol range, proves smoothness off projected stationary directions, and determines the wave kernel and both causal halves.

- **How do differences measure fractional smoothness?** [*Fractional energy and sharp Fourier embeddings*](src/fractional-energy-and-sharp-fourier-embeddings.md) proves the exact difference-norm identity, its two limiting constants, compact Hölder inclusions and the sharp weighted Fourier thresholds.

- **Which derivative estimates survive a rough symbol?** [*Annular multipliers and elliptic endpoints*](src/annular-multipliers-and-elliptic-endpoints.md) proves the averaged multiplier theorem, Hölder bounds and interior elliptic estimates, and constructs continuous forcing with unbounded highest derivatives.

Every available lesson contains its own graded problems and complete solutions. The course scope describes the lessons collected in this reader.

## Sources and contributions

The course uses independently written proofs and teaching organization, drawing on the works identified in each lesson. These include Hörmander's second-edition reprint, DOI 10.1007/978-3-642-61497-2, and the named free sources. Laurent Schwartz's distribution and kernel theory is a foundational contribution. Individual bibliographies credit the actual mathematical inputs; source books do not supply an exercise sequence or replace the proofs given here.

The lesson editions and prerequisite readings identify their authors and component licences. Complete earlier programme proofs are linked at the point of use with exact lesson and section locators. Source credit identifies the mathematical contributions; an internal proof link identifies the argument a reader needs. Independently authored text in this guide is CC0.
