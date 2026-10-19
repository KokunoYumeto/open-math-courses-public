# Smooth parameter slices from the normal condition

*Programme proof text: AN-03 course-writing task, OpenAI Codex. CC0 1.0. Prerequisite connections: GPT-6 Astra (OpenAI), Ultra.*

This is the complete Section 18.6 of the programme reading *Detecting regularity without choosing coordinates*. It proves that the normal restrictions are the actual strong smooth distribution family and reconstruct the joint distribution. Its original section and formula labels are retained.

The preceding [Sections 18.1–18.5](smooth-pullback-and-fourier-normal-condition.md) supply every wavefront, Fourier, Gaussian and pullback identity cited below, with their full prerequisite readings. In particular WF1 is distributional Fourier inversion, WF2 is compact wavefront localization, WF11–WF13 construct the normal pullback and identify its Gaussian limit. The [Schwartz and Fourier foundation](schwartz-fourier-foundations-U017.md), F1–F5, supplies the test decay and inversion; the [metric foundation](metric-foundation-bridges.md), Sections 12–13, supplies finite localization and Taylor remainders; and the [integration foundation](banach-foundation-bridges.md), Sections 15–16, supplies the absolute integrals and dominated limits.

### 18.6. Absence of parameter-normal covectors gives the actual smooth family

Let \(u\) be a distribution on an open product in the original variables \((t,x)\in\mathbb R^p\times\mathbb R^q\), with no wavefront covector \((t,x;\tau,0)\), \(\tau\ne0\). Every slice embedding \(j_t(x)=(t,x)\) satisfies WF11, because its transpose sends \((\tau,\xi)\) to \(\xi\). Thus the already constructed restriction \(u_t=j_t^*u\) exists.

Fix compact spatial test support and a small compact parameter neighborhood. The compact base set and the compact unit sphere in the original \(\tau\)-coordinates have a finite regular cone/base cover. Use its finite spatial partition and common smaller parameter neighborhood. After each compact localization \(v\), WF2 gives a constant \(\delta>0\) such that \(\widehat v(\tau,\xi)\) decreases to every order when \(|\xi|\leq\delta|\tau|\); on the whole space it has the original polynomial bound \(C(1+|\tau|+|\xi|)^m\). Summing the finitely many localized formulas retains all their cutoff derivatives.

For a spatial test \(\psi\), the actual pairing on the neighborhood where the parameter cutoff is one is

\[
\langle u_t,\psi\rangle
=(2\pi)^{-(p+q)}
 \iint e^{it\cdot\tau}\widehat v(\tau,\xi)\widehat\psi(-\xi)
                           \,d\xi\,d\tau,\qquad
\partial_t^\alpha e^{it\cdot\tau}=(i\tau)^\alpha e^{it\cdot\tau}.
\tag{WF16}
\]

In \(|\xi|\leq\delta|\tau|\), the rapid decrease of \(\widehat v\) dominates every original factor \(\tau^\alpha\) and both integration dimensions, while \(|\widehat\psi|\leq\int|\psi|\). In the complementary region, \(|\tau|\leq|\xi|/\delta\). The polynomial bound for \(v\), multiplied by the Schwartz bound
\[
|\widehat\psi(\xi)|\leq
(1+|\xi|^2)^{-N}
\int |(1-\Delta_x)^N\psi(x)|dx,
\tag{WF17}
\]
is integrable after both integrations when \(2N>m+|\alpha|+p+q\). The integral in WF17 is bounded by finitely many original test derivative seminorms on the fixed support, with every binomial and derivative from \((1-\Delta)^N\) retained in that full operator. These bounds are uniform on bounded sets of tests. For each derivative order, take a corresponding \(N\); no one fixed finite test order for all parameter derivatives is inferred.

Dominated differentiation therefore gives every derivative in WF16. Taylor's remainder for \(e^{ih\cdot\tau}\), bounded by a constant times \(|h|^2|\tau|^2\), and the same bounds with two additional frequency powers prove convergence of difference quotients uniformly on every bounded set of spatial tests. Continuity uses the same dominated bounds. This is precisely smoothness into the strong distribution topology, whose seminorms are suprema of pairings over bounded test sets. It is stronger than only the smoothness of each single pairing.

To verify that WF16 is the original pullback, apply WF13 to \(v\), then restrict the smooth Gaussian approximations. Their transforms acquire the full factor \(e^{-\epsilon(|\tau|^2+|\xi|^2)}\), bounded by one. The just proved absolute envelopes allow its limit and every fixed parameter derivative in WF16, agreeing with WF12 for the slice map. Finally testing against any original compact smooth \(\varphi(t,x)\) and applying these absolute bounds permits integration in \(t\), and recovers the original distribution pairing by WF1. Thus the family reconstructs \(u\), rather than an unrelated family with the same notation. Finite localization and restriction compatibility paste these actual families on the whole parameter domain. For \(p=0\) there is no parameter derivative; for \(q=0\) the no-normal condition is absence of all nonzero covectors and Section18.1 proves the required scalar smoothness.
