# Spectra, resolvents and scattering: a route through five questions

*Written by GPT-6.1 Sol (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

A spectrum can be observed in several ways. A resolvent probes an energy with a small imaginary part. A wave records the same spectrum as a time evolution. A counting function measures how many states lie below a threshold. A scattering amplitude records what remains of a travelling state far from the region where the coefficients differ from the free operator. These observations share spectral calculus, but they require different limits and different norms.

The course follows five questions. Each part begins with a comparison that can be calculated directly and then follows the estimates needed for its general form. Return to the comparison when a proof introduces a domain, a weight or an exceptional energy: it tells you what that condition is protecting. The lessons retain their own precise prerequisites. Hilbert spaces, Fourier inversion, elementary measure theory and basic differential equations are entry knowledge; the manifold and symbol arguments also use the linked programme courses named in their lessons.

The explicitly solved transport and cylinder models have their own proofs. The general Dirichlet Weyl law uses generalized-ray propagation, the curved spectral-projector estimate, the closed-graph argument and the scalar square-root calculus. Read it after Polynomial localizations and rough coefficients and Positive real powers and spectral rescaling, so these inputs precede their use. The local round-sphere argument gives a separate proof of its exact model spectrum.

## What can a spectral measurement tell us?

Begin with a scalar observation. If \(A\) is self-adjoint and \(\mu_f\) is the spectral measure of a vector, then
\[
 \operatorname{Im}((A-\lambda-i\varepsilon)^{-1}f,f)
 =\int\frac{\varepsilon}{(t-\lambda)^2+\varepsilon^2}\,d\mu_f(t).
\]
This is a nonnegative average of a measure. A bound on this scalar expression can exclude singular mass on an interval, but it is not a bound on the full Hilbert-space resolvent norm. Conversely, a pointwise boundary limit need not be a continuous density. The first lesson proves the measure statement and gives exact examples separating these possibilities.

For a discrete spectrum, positivity is also what lets a smoothed observation control the unsmoothed count. The wave evolution supplies the time information used for that smoothing. Local symbol calculations explain the density; a return-time argument explains the error in recovering the count. The flat wall and the cylinder then test the sign and size of a boundary contribution with exact formulas.

**Worked comparison: the interval, the circle and the cylinder.** On an interval of length \(a\) with Dirichlet ends, the positive square-root frequencies are \(\pi m/a\), \(m\geq1\). Under the closed convention,
\[
 N_D(k^2)=\lfloor ak/\pi\rfloor.
\]
On a circle of circumference \(L\), the frequencies are \(2\pi\ell/L\), \(\ell\in\mathbb Z\), so the count, including the zero eigenvalue, is
\[
 N_C(k^2)=2\lfloor Lk/(2\pi)\rfloor+1.
\]
These formulas are staircases. Their bounded oscillations cannot be replaced by an asserted pointwise constant plus a remainder tending to zero. An averaged constant and a pointwise asymptotic coefficient are different claims.

On the cylinder, the squared frequencies are sums of the two squares. Thus the count is a lattice count in a disk, not the product of the two counts above. Reflect each positive normal index to its negative partner. The excluded zero-normal row has the circle count just computed. With the exact notation of Theorem 6.1 in the generalized-ray lesson,
\[
 N_P(k^2)=\frac{S_{a,L}(k)-R_0(k)}2,
 \qquad R_0(k)=2\lfloor Lk/(2\pi)\rfloor+1.
\]
The area term comes from \(S_{a,L}\); the negative linear term comes from the row subtraction. The theorem proves the remaining disk discrepancy by Fourier decay, Poisson summation and smoothing in the actual frequency coordinates. It gives \(O_{a,L}(k^{2/3})\), hence \(O_{a,L}(\lambda^{1/3})\), for each fixed cylinder. This exact model checks the two coefficients without assuming the general curved boundary estimates.

**Observation to carry forward.** The count includes multiplicities and an endpoint convention. The wave-trace return includes the covector. The collar coefficient uses a fixed spatial test. These three qualifications must survive when the model is transferred to a manifold; none is supplied by a diagram of a reflected path alone.

The proof route for this question is:

- [Resolvents, domains and spectral density](src/resolvents-domains-and-spectral-density.md) — What does a measured resolvent actually determine?
- [Wave evolution and cotangent flow](src/wave-evolution-and-cotangent-flow.md) — Which return is visible in an evolution kernel?
- [Local spectral density and the subprincipal correction](src/local-spectral-density-and-subprincipal-correction.md) — What does the next local density coefficient measure?
- [Return times and spectral counting](src/return-times-and-spectral-counting.md) — How much information is lost by smoothing a counting staircase?
- [Reflection and the Dirichlet boundary coefficient](src/reflection-and-the-dirichlet-boundary-coefficient.md) — Why does a wall change the count by a quarter of tangential phase volume?

## How does escape select a real-energy solution?

A nonreal resolvent picks a unique Hilbert-space solution. At real energy the same equation can have homogeneous waves that do not belong to that Hilbert space. We first make the ambiguity explicit and then choose a topology that can observe the tails.

**Worked comparison: one transport direction.** Let \(D=-i\partial_x\), \(\lambda\in\mathbb R\), and \(f\in C_c^\infty(\mathbb R)\). Define
\[
 u_+(x)=i e^{i\lambda x}
             \int_{-\infty}^x e^{-i\lambda y}f(y)\,dy.
\]
Differentiation gives \(u_+'=i\lambda u_++if\), and therefore \((D-\lambda)u_+=f\). To the left of the support it is zero. To the right it equals \(iI e^{i\lambda x}\), where
\[
 I=\int_{\mathbb R}e^{-i\lambda y}f(y)\,dy.
\]
If \(I\ne0\), the squared mass on a long right interval grows linearly with its length, and the solution is not in \(L^2\). If \(I=0\), this same solution vanishes on both ends. Adding \(c e^{i\lambda x}\) leaves the equation unchanged but changes the tail. The outgoing condition fixes that otherwise free constant. The flat-shell lesson proves the corresponding boundary limit for the full endpoint forcing space, rather than only for smooth compactly supported data.

The curved-shell trace transfers this calculation through graph coordinates. Mild-weight localization makes those transfers compatible with actual spatial norms. Polynomial strength then controls patches at arbitrarily large frequencies. The global radiation theorem identifies all homogeneous amplitudes and the exact quotient by tails whose mass vanishes per unit radius.

**Worked comparison: small force and large phase.** For drift with speed one, let \(V\) be a real locally integrable potential, let \(F'=V\), and put \(G u=e^{iF}u\). Direct differentiation on the appropriate core gives
\[
 G^{-1}DG=D+V.
\]
The closed operator has the conjugated domain \(G^{-1}\mathcal D(D)\); a formal product-rule calculation is not a substitute for that domain. The stationary waves are \(e^{i\lambda x-iF(x)}\). If \(V(x)=\kappa x/(1+x^2)\), then \(F(x)=\kappa\log(1+x^2)/2\). Its derivative tends to zero, but its phase does not approach a limit at either end when \(\kappa\ne0\). The modified comparison removes this phase. In contrast, the integral of \(\sin x/x\) converges conditionally, and the exact ordinary-limit criterion in the wave-operator lesson applies. Absolute integrability is sufficient there but is not necessary.

We now read the Hamilton trajectories and their action before the general perturbation-domain package. They construct the geometrical phase under their own explicit smooth hypotheses. The modified-wave theorem takes a specified self-adjoint realization as an input. Later lessons establish that realization for the full rough differential class. This separates geometry from the question of which operator has actually been closed, while retaining both proofs.

**Observation to carry forward.** A small change in momentum, a small relative displacement and a convergent phase are different assertions. The exact Hamilton trajectory checks the first two; the action and signed-velocity estimates supply the third assertion in the form a modifier needs.

The proof route for this question is:

- [Wave operators and modified phases](src/wave-operators-and-modified-phases.md) — Does a coefficient tending to zero make its accumulated phase converge?
- [Endpoint spaces and flat energy shells](src/endpoint-spaces-and-flat-energy-shells.md) — Which norm can retain a radiating tail?
- [Fourier traces on curved energy surfaces](src/fourier-traces-on-curved-energy-surfaces.md) — Does the shell need curvature, or only a graph?
- [Mild weights and frequency localization](src/mild-weights-and-frequency-localization.md) — Can localization preserve a weight that is not a power?
- [Division and radiation at regular energies](src/division-and-radiation-at-regular-energies.md) — Why do the two boundary denominators produce different tails?
- [Polynomial translations and regular energies](src/polynomial-translations-and-regular-energies.md) — How can one control patches whose centres run to infinity?
- [Global polynomial resolvent estimates](src/global-polynomial-resolvent-estimates.md) — What turns infinitely many regular patches into one resolvent estimate?
- [Global radiation and flux](src/global-radiation-and-flux.md) — How much of a forced solution is measured by its far-field amplitudes?
- [Hamilton trajectories under a long-range force](src/hamilton-trajectories-under-a-long-range-force.md) — Can position drift be large while the change of momentum stays small?
- [Smooth long-range phases from Hamilton trajectories](src/smooth-long-range-phases-from-hamilton-trajectories.md) — Which action produces the phase required by the wave modifier?
- [Modified waves and the direction of escape](src/modified-waves-and-the-direction-of-escape.md) — Which spatial cone corresponds to the chosen time direction?

## Which perturbations define the operator we need?

An expression can be meaningful on compact smooth functions and still fail to define the self-adjoint operator intended in a scattering theorem. We distinguish three tests: local multiplication by rough coefficients, compactness between specified graph spaces, and closure with a known domain. Once those tests are complete, the time-dependent wave theorem can use their actual constants.

**Worked comparison: support, order and compactness.** On the line, choose nonzero \(h\in C_c^\infty\) and a compactly supported smooth \(\eta\) that equals one on its support. For integers \(N\geq1\), let
\[
 u_N=N^{-2}e^{iNx}h(x).
\]
The sequence is bounded in \(H^2\). Since
\[
 D^2u_N=e^{iNx}
       \bigl(h+2N^{-1}Dh+N^{-2}D^2h\bigr),
\]
the vectors \(\eta D^2u_N\) have norms approaching \(\|h\|_2\) and converge weakly to zero. Weak convergence follows first against compact smooth test functions by integration by parts and then against all \(L^2\) functions by density and the uniform bound. No subsequence can converge strongly. Thus this compactly supported full-order perturbation is not a compact map \(H^2\to L^2\).

Now insert a smooth compact frequency cutoff \(\theta(D)\). Its kernel after multiplication by \(\eta\) is
\[
 K(x,y)=\eta(x)(2\pi)^{-1}
       \int e^{i(x-y)\xi}\xi^2\theta(\xi)\,d\xi.
\]
Plancherel gives
\[
 \|K\|_{L^2(dx\,dy)}^2
 =(2\pi)^{-1}\|\eta\|_2^2
                \|\xi^2\theta(\xi)\|_2^2<\infty.
\]
The cutoff operator is Hilbert–Schmidt and therefore compact. The general compact-remainder lesson retains rough coefficients and endpoint norms, where further local multiplier and tail arguments are required. It does not assert compactness of the original full-order perturbation.

There is another obstruction when the free operator leaves a direction invariant. For \(p(\xi)=\xi_1\), modulating in the transverse variable preserves every derivative of \(p\) appearing in its graph norm. A nonzero local multiplication term still sees the modulation. The short-range compactness lesson proves the full obstruction and distinguishes it from nonlocal compact maps. This is why an elliptic argument must not silently replace a simply characteristic polynomial with invariant directions.

This part constructs the self-adjoint short-range closure and ordinary wave operators from the abstract graph-space criterion. The next part proves completeness and the regular-energy matrices before applying them to rough coefficients with narrow high peaks. This order supplies every scattering input to that lesson's final exercise. The subsequent long-range part then uses its coefficient estimates for regularization, symmetric splitting, the closed Sobolev domain and the weighted scales.

**Observation to carry forward.** Name the source and target norm whenever you say “compact.” A support statement, a small coefficient and a smoothing operator answer different questions. A conserved weighted norm is also a substantive input: the weighted-Hilbert-space lesson shows why unweighted compactness alone cannot supply it.

The proof route for this question is:

- [Short-range compactness and local tests](src/short-range-compactness-and-local-tests.md) — Is compact support enough to make a differential perturbation compact?
- [Self-adjoint short-range operators](src/self-adjoint-short-range-operators.md) — Which closed realization is being scattered?
- [Wave operators for differential perturbations](src/wave-operators-for-differential-perturbations.md) — Can summable shell bounds replace a fixed power of decay?
- [Compact perturbations in weighted Hilbert spaces](src/compact-perturbations-in-weighted-hilbert-spaces.md) — What changes when the amplitude weight approaches zero?

## Can the observations reconstruct every state?

The resolvent gives local energy observations, and a wave operator gives a time comparison. Neither construction alone guarantees that it describes every continuous state. We first remove the exceptional point spectrum, then compare the two constructions. The same question—how much information a finite observation retains—also governs compressed observables and spectral clusters.

**Worked comparison: an isometry can miss states.** On \(\ell^2(\mathbb N_0)\), let \(S e_j=e_{j+1}\). It satisfies
\[
 S^*S=I,\qquad SS^*=I-P_{e_0}.
\]
Every input norm is preserved, yet \(e_0\) has no preimage. The missing range is not detected by the first identity. In the short-range course proof, the matching-sign composition of the stationary transform with the wave operator is the ordinary Fourier transform. Its onto property supplies the information absent from mere isometry. The long-range end of the course establishes the corresponding bandwise stationary comparison after controlling the changing phases and amplitudes.

A bound state is a different kind of missing datum. Its spectral mass must be kept as a discrete component, not described by a continuous shell amplitude. The limiting-absorption lesson characterizes this component through the Fredholm kernel. Quadratic uniqueness estimates identify conditions that rule it out in their stated settings. The spectral-transform lesson then gives the exact norm identity on the continuous part; completeness recovers its preimages.

**Worked comparison: one trace is not a distribution.** The matrices \(A=\operatorname{diag}(-1,1)\) and \(B=\operatorname{diag}(0,0)\) have the same normalized trace zero. However,
\[
 \tfrac12\operatorname{tr}(A^2)=1,
 \qquad \tfrac12\operatorname{tr}(B^2)=0.
\]
Their empirical eigenvalue laws differ. For a compressed observable, knowing the first symbol average is therefore insufficient. The proof compares all polynomial moments, controls crossing through the spectral cutoff, and uses approximation on a compact interval. This produces the full limiting law while retaining the hypotheses under which each power comparison is valid.

**Worked comparison: multiplicity is visible at a jump.** Consider the abstract discrete model with eigenvalue \(j\) of multiplicity \((j+1)^2\), \(j\geq0\). This is a counting model, not a claim that a particular elliptic operator realizes it. At a large \(j\), its count has a jump of size \((j+1)^2\). Suppose a continuous function approximated the count with an error \(o(j^2)\) at all energies. Comparing its value at \(j\) with values approaching \(j\) from the left, continuity would force a jump of size \((j+1)^2\) to be \(o(j^2)\), a contradiction. The cluster lesson makes this obstruction precise for the actual multiplicity asymptotic.

The same multiplicity has the Newton expansion
\[
 (j+1)^2=1+3\binom j1+2\binom j2.
\]
Integer Newton coefficients are a stronger test than integer leading monomial coefficients. In the course, the return phase fixes an arithmetic lattice, and eventual integrality constrains the multiplicity polynomial on that lattice. These are necessary arithmetic conditions, not an existence theorem for an operator with arbitrarily prescribed coefficients.

**Observation to carry forward.** The two-channel line problem fixes amplitude signs through velocity. The round-sphere model fixes the quantum return phase through its complete harmonic spectrum. These models test normalizations at opposite ends of the course without replacing the general reconstruction or averaging arguments.

The proof route for this question is:

- [Limiting absorption and point spectrum](src/limiting-absorption-and-point-spectrum.md) — What obstructs taking the perturbed resolvent to real energy?
- [Quadratic weights and uniqueness at infinity](src/quadratic-weights-and-uniqueness-at-infinity.md) — Which decay hypothesis can force a positive-energy solution to vanish?
- [Distorted Fourier transforms and spectral density](src/distorted-fourier-transforms-and-spectral-density.md) — How does a shell observation become a spectral transform?
- [Asymptotic completeness for short-range operators](src/asymptotic-completeness-for-short-range-operators.md) — How does a time comparison prove that no continuous states are missing?
- [Scattering matrices at regular energies](src/scattering-matrices-at-regular-energies.md) — Can an eigenfunction change the stationary solution without changing scattering?
- [Polynomial localizations and rough coefficients](src/polynomial-localizations-and-rough-coefficients.md) — Can narrow high peaks satisfy a short-range coefficient test?
- [One-dimensional scattering and phase shifts](src/one-dimensional-scattering-and-phase-shifts.md) — Which of the two momenta is incoming on each end of the line?
- [Compressed spectral measures and symbol distributions](src/compressed-spectral-measures-and-symbol-distributions.md) — Does an observable's mean determine its spectral distribution?
- [Positive real powers and spectral rescaling](src/positive-real-powers-and-spectral-rescaling.md) — Which time scale belongs to an operator of order greater than one?
- [Generalized rays and the Dirichlet Weyl law](src/generalized-rays-and-the-dirichlet-weyl-law.md) — Does a reflecting ray's position return imply a wave-trace return?
- [Arithmetic spectral clusters and their distributions](src/arithmetic-spectral-clusters-and-their-distributions.md) — What can the integrality of cluster multiplicities force?
- [Averaging a perturbation around closed trajectories](src/averaging-a-perturbation-around-closed-trajectories.md) — What survives averaging a perturbation along a closed trajectory?

## Which estimates survive a long-range limit?

We first regularize the coefficients, construct their symmetric splitting and prove the Sobolev domain and weighted estimates. We then combine this operator package with the earlier geometric phase. The proof has two complementary frequency estimates, a radiation condition that survives graph limits, and an amplitude estimate after the phase is removed. Each answers a different potential failure of a limiting procedure.

**Worked comparison: fixed-time agreement is not an infinite-time limit.** For \(\varepsilon>0\), put
\[
 v_\varepsilon(t)=e^{i\varepsilon\log(1+t)},\qquad t\geq0.
\]
For every bounded time interval, \(v_\varepsilon\to1\) uniformly as \(\varepsilon\to0\). But at
\[
 t_\varepsilon=e^{\pi/\varepsilon}-1
\]
the value is \(-1\). Thus the convergence is not uniform on the whole future interval. For each fixed positive \(\varepsilon\), the phase has no limit as \(t\to\infty\). Its differential equation is
\[
 v_\varepsilon'
   =i\frac{\varepsilon}{1+t}v_\varepsilon.
\]
The coefficient tends to zero on every compact set as \(\varepsilon\to0\), but its absolute time integral diverges. Multiplying by the inverse phase makes the amplitude identically one. This simple equation explains both the need for a modifier and why local convergence of truncated coefficients cannot by itself prove convergence of a far-field amplitude.

The off-energy lesson constructs an inverse that gains derivatives and controls spatial weights. The noncritical-frequency lesson uses the velocity in a positive commutator where division is impossible. Their combination leaves a compact error. Radiation and flux identify the homogeneous limit associated with that error; weighted decay then shows that it is an eigenfunction. Excluding that energy removes the compact error and produces the limiting resolvent. At an eigenvalue the reduced boundary value instead retains its orthogonality condition.

The stationary amplitude requires another chain. The escaping Lagrangian has a globally normalized action. Mixed coordinates give a generating function with controlled derivatives. The energy graph factors the stationary equation into an outgoing first-order problem. A frequency cutoff makes its forcing compact and continuous. Commuting coordinates expose products whose adjoint defects are integrable. A transverse moment proves convergence for a dense class, and the common energy bound extends the amplitude to all square-integrable data and integrable forcing.

**A useful three-term comparison.** If \(U_R\) and \(U\) are uniformly bounded operators and \(f_0\) approximates \(f\), then
\[
 \begin{aligned}
 \|U_Rf-Uf\|\leq{}&\|U_R(f-f_0)\|\\
 &+\|(U_R-U)f_0\|+\|U(f_0-f)\|.
 \end{aligned}
\]
With a common bound \(C\), the first and last terms total at most \(2C\|f-f_0\|\). Only the middle term needs a convergence proof on the dense class. Without a common \(C\), this estimate does not extend that proof. The amplitude and truncation lessons establish the actual uniform constants and the appropriate dense data for their equations; the displayed inequality explains why those constants are part of the result.

Finally the stationary transform compares with the time-dependent modified waves on good energy bands. The bandwise preimage and the exceptional-energy analysis recover the whole continuous space. No interchange of cutoff radius, spectral boundary and infinite-time limits is presumed: their order is justified by the estimates just described.

The proof route for this question is:

- [Regularizing long-range coefficients](src/long-range-coefficient-calculus.md) — How much smoothing can a slowly varying coefficient tolerate?
- [Admissible differential perturbations](src/admissible-differential-perturbations.md) — How can a rough full-order perturbation be split without losing symmetry?
- [The Sobolev domain of an elliptic operator](src/the-sobolev-domain-of-an-elliptic-operator.md) — When does the closure have exactly the expected Sobolev domain?
- [Weighted Sobolev spaces and rough elliptic estimates](src/weighted-sobolev-spaces-and-rough-elliptic-estimates.md) — Does the order of a spatial weight and a derivative matter?
- [The resolvent away from the energy surface](src/the-resolvent-away-from-the-energy-surface.md) — Why must an off-energy inverse control both position and frequency?
- [A resolvent estimate at noncritical frequencies](src/a-resolvent-estimate-at-noncritical-frequencies.md) — What replaces division where the symbol vanishes?
- [Combining the long-range resolvent estimates](src/combining-the-long-range-resolvent-estimates.md) — Which error remains after the two frequency estimates are combined?
- [Radiation for limits of long-range resolvents](src/radiation-for-limits-of-long-range-resolvents.md) — Which directional information survives a resolvent graph limit?
- [Outgoing flux and vanishing shell mass](src/outgoing-flux-and-vanishing-shell-mass.md) — Can a flux observation force every persistent derivative tail to vanish?
- [Weighted endpoint estimates and polynomial decay](src/weighted-endpoint-estimates-and-polynomial-decay.md) — How is one decay estimate promoted to every polynomial weight?
- [Limiting absorption for long-range differential perturbations](src/limiting-absorption-for-long-range-differential-perturbations.md) — How do radiation uniqueness and compactness create a boundary resolvent?
- [Escaping Lagrangians on regular energy surfaces](src/escaping-lagrangians-on-regular-energy-surfaces.md) — Can an escaping energy family have a single-valued action on a shell with loops?
- [Generating functions and the end of a localized force](src/generating-functions-and-the-end-of-a-localized-force.md) — What changes when the force ends after a compact region?
- [Energy-shell factors and outgoing equations](src/energy-shell-factors-and-outgoing-equations.md) — Why does factorizing an energy graph leave an outgoing choice?
- [Frequency cutoffs and compact scattering remainders](src/frequency-cutoffs-and-compact-scattering-remainders.md) — How can a full-order perturbation become compact after a frequency cutoff?
- [Commuting coordinates for long-range evolution](src/commuting-coordinates-for-long-range-evolution.md) — Which moving coordinates keep the evolution energy controlled?
- [Transverse moments and outgoing amplitudes](src/transverse-moments-and-outgoing-amplitudes.md) — Why begin with a transverse moment if the final amplitude is unweighted?
- [Truncated operators and stable scattering amplitudes](src/truncated-operators-and-stable-scattering-amplitudes.md) — Does local agreement of truncated forces imply agreement of far-field amplitudes?
- [Spectral transforms and completeness of modified waves](src/spectral-transforms-and-completeness-of-modified-waves.md) — How can a modified wave operator be proved onto?

## How to use the proof routes

Read the worked comparisons first, then follow each part's lessons in the order above. The “Working question” at the start of a lesson says which observation or obstruction it resolves. Its “Use the conclusion” passage names a specific check to perform after the proof. The five solved exercises in every lesson remain available for testing the exact hypotheses and exceptional cases.

For a model-first pass, use the transport, drift, interval/circle, localized derivative, matrix and phase calculations in this guide. Follow their named lesson proofs before applying them to more general coefficients or manifolds. For the full advanced pass, also read the exact programme prerequisite proofs identified by each lesson; a reading route does not remove those dependencies.

Before the wave and spectral lessons, read the finite scalar calculus and summation in [Classical scalar symbols](providers/analysis/classical-scalar-calculus.md#finite-scalar-calculus), then [Phase geometry, stationary phase and the Maslov symbol](providers/analysis/phase-geometry-and-stationary-phase.md#phase-foundations). The phase reading supplies the quadratic reduction, parameter remainders, phase changes through caustics, principal-symbol correspondence and wavefront detection. Next read [Transverse composition and graph operators](providers/analysis/transverse-composition-and-graph-operators.md#transverse-composition), which proves the actual kernel product, density and Maslov contraction, adjoint, all-real graph Sobolev mapping and ordered Egorov. Continue with [Wavefront-qualified pullback](providers/analysis/wavefront-qualified-pullback.md#qualified-pullback), including convergence and transverse restriction, and [Scalar transport and finite action on a phase](providers/analysis/scalar-transport-and-phase-action.md#scalar-transport), including every finite remainder and the invariant half-density formula. The wave lesson verifies its restriction hypotheses, constructs its smooth flow locally and applies these proofs to its full recursion. 

The endpoint lesson now proves sharp logarithmic weights and a one-sided operator transfer (Propositions 3.2–3.4). The compressed-observable lesson proves a smooth-test leakage bound and robustness under small trace-norm changes (Proposition 5.2 and Theorem 5.3). The phase lesson includes an exterior radial C² model with an exact energy-to-time transform, outgoing flux and a summable residual (Proposition 8.2). These comparisons are proved in the lessons at their stated scope.

The human sources actually used remain credited in the lessons, including Agmon–Hörmander, Hörmander, Yafaev, Teschl, Dollard, Kato, Duistermaat–Guillemin, Guillemin–Sternberg, Seeley, Ivrii and Marshall. These guide calculations and their explanations were written by the credited AI author. Linked prerequisite works retain their own component licences; their expression is not imported into this guide. The KaTeX reader assets retain their included MIT notice.
