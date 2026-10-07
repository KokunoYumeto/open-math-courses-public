# Lipschitz graphs and surface measures

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

*Source/proof self-check and prerequisite integration by GPT-6 Astra (OpenAI), Ultra, October 2026. Historical authorship and component terms are retained.*

A graph can have a crease while still carrying an unambiguous surface measure and outward normal almost everywhere. Differentiating the region below it supplies both objects at once. The first derivative places mass along the graph; a corner of a planar graph does not acquire an extra point mass at this derivative level.

We extend the graph calculation in [Boundary flux and weak identities](boundary-flux-and-weak-identities.md). Measures, their uniqueness as order-zero distributions and localization come from [Order, positivity and distributional limits](order-positivity-and-limits.md), [Local data and compatible products](local-data-and-compatible-products.md), and the supplied [positive-measure foundation](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md). The exact [integration and smoothing proofs](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, supply completed Lebesgue measure, Fubini, convergence, \(L^p\) completeness, compact smooth density, translation continuity and approximate identities. We use \(p=1,2\). The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, supplies compactness, calculus and smooth cutoffs; the [finite algebra foundation](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §10, supplies the determinant identities. These components retain their stated licences. Rademacher's differentiability theorem is fully proved below before its use in graph charts.

Basic references are Heinonen’s *Lectures on Lipschitz Analysis* (2005), for almost-everywhere differentiability, and Dyatlov’s *Lecture notes for 18.155* (2026), for surface-measure distributions.

## Dyadic face increments give the weak derivative

**Lemma 1.1 (constructing bounded weak derivatives).** A locally Lipschitz real function \(h\) on open \(B\subset\mathbb R^d\) has locally bounded weak partials \(g_j\). On a region where \(h\) has Lipschitz constant \(L\), \(|g_j|\leq L\) almost everywhere.

**Proof.** Work on a closed coordinate cube \(Q\Subset B\) where \(h\) is \(L\)-Lipschitz. For a subrectangle \(R=\prod_i[a_i,b_i]\subset Q\), define its oriented face increment by

\[
\begin{aligned}
\mu_j(R)&=\int_{R'}\Delta_jh(x')\,dx',\\
\Delta_jh(x')&=h(x',b_j)-h(x',a_j),\\
R'&=\prod_{i\ne j}[a_i,b_i].
\end{aligned}
\tag{1.1}
\]

This notation places the displayed endpoints in coordinate \(j\). Fubini and continuity define the integral, and the Lipschitz bound gives \(|\mu_j(R)|\leq L|R|\). Splitting in coordinate \(j\) telescopes the two face values; splitting in any other coordinate splits its integral. Thus increments add over every finite rectangular subdivision.

Subdivide \(Q\) into its dyadic cubes at level \(k\), and let \(g_{j,k}\) on each cell \(R\) equal \(\mu_j(R)/|R|\). Ignore cell boundaries, a null set. These functions are bounded by \(L\), and the average of \(g_{j,k+1}\) over each preceding cell is \(g_{j,k}\). Hence, for \(m\geq k\),

\[
\begin{gathered}
\int_Qg_{j,m}g_{j,k}=\|g_{j,k}\|_2^2,\\
\|g_{j,m}-g_{j,k}\|_2^2\\
=\|g_{j,m}\|_2^2-\|g_{j,k}\|_2^2.
\end{gathered}
\tag{1.2}
\]

The norms squared increase and are at most \(L^2|Q|\). The sequence is therefore Cauchy in \(L^2\), whose proved completeness supplies \(g_j\). The summable-subsequence argument in that same completeness proof gives an almost-everywhere convergent subsequence; consequently \(|g_j|\leq L\).

We verify the weak identity rather than assuming any pointwise derivative. Let \(\psi\in C_c^\infty(\operatorname{int}Q)\), and let \(\psi_k\) take its value at each dyadic cell center. Uniform continuity gives \(\psi_k\to\psi\) uniformly. Thus

\[
\begin{gathered}
\int_Qg_j\psi
=\lim_{k\to\infty}
\sum_R\psi(c_R)\mu_j(R),\\
c_R=\operatorname{center}R.
\end{gathered}
\tag{1.3}
\]

In the sum, each internal face carries the value of \(h\) times the difference of the test values in its two neighboring cells. Exterior face terms vanish for all sufficiently fine grids. The negative of that difference divided by the cell width converges uniformly to \(\partial_j\psi\) on the face: the fundamental theorem along the segment joining the centers and uniform continuity of \(\partial_j\psi\) prove this. Multiplying by the cell width, integrating along each face, and summing gives a Riemann sum in coordinate \(j\). The transverse test value is sampled at cell centers, with a uniformly vanishing error since \(\psi\) is smooth and \(h\) is bounded. Continuity of \(h\) makes these sums converge to \(-\int_Qh\,\partial_j\psi\). Equation (1.3) therefore proves the weak identity.

These local weak derivatives agree almost everywhere on overlaps. Indeed their difference is locally integrable and pairs to zero with every smooth compact test; convolution with a compact smooth approximate identity is then zero, and its proved local \(L^1\) convergence forces the difference to vanish almost everywhere. Cubes and a countable exhaustion glue the \(g_j\)'s. \(\square\)

## Lebesgue points turn weak gradients into differentials

We need a differentiation fact about averages and prove it at the required generality.

For a finite positive-volume cube, write
\(\operatorname{av}_Q f=|Q|^{-1}\int_Q f\).

**Lemma 1.2 (Lebesgue points for local integrable functions).** If \(f\in L^1_{\mathrm{loc}}(\mathbb R^d)\), then for almost every \(x\),

\[
\begin{gathered}
\lim_{r\downarrow0}
\operatorname{av}_{Q_r(x)}|f-f(x)|=0,\\
Q_r(x)=x+[-r,r]^d.
\end{gathered}
\tag{1.4}
\]

**Proof.** First suppose \(f\in L^1(\mathbb R^d)\). For integrable \(a\), define the centered cube maximal average
\(Ma(x)=\sup_{r>0}|Q_r(x)|^{-1}\int_{Q_r(x)}|a|\).
For every \(\lambda>0\),

\[
|\{Ma>\lambda\}|
\leq\frac{3^d}{\lambda}\|a\|_1.
\tag{1.5}
\]

Here is the covering argument. Each cube average is continuous in its center by \(L^1\) translation continuity, so the displayed set is open. For a compact subset choose at each of its points a centered cube whose average exceeds \(\lambda\); the interiors of these cubes give a finite cover. Sort this finite list by decreasing side length and retain a cube only if its interior is disjoint from all previously retained cubes. Any discarded cube meets a retained cube of at least its size and is contained in its threefold concentric dilation. Thus the compact subset has measure at most \(3^d\) times the sum of the retained volumes. Their interiors are disjoint and \(\lambda|Q|<\int_Q|a|\), so that sum is at most \(\|a\|_1/\lambda\). Inner approximation of an open set by compact sets proves (1.5).

Choose compact smooth \(f_k\to f\) in \(L^1\), using the exact density theorem cited above. For any point where \(f\) is finite, continuity of \(f_k\) and the triangle inequality give

\[
\begin{aligned}
&\limsup_{r\downarrow0}
\operatorname{av}_{Q_r(x)}|f-f(x)|\\
&\quad\leq M(f-f_k)(x)\\
&\qquad+|f(x)-f_k(x)|.
\end{aligned}
\tag{1.6}
\]

For a fixed \(\delta>0\), the set where the left side exceeds \(\delta\) has measure at most
\(2(3^d+1)\|f-f_k\|_1/\delta\), by (1.5) and the elementary integral bound
\(|\{|a|>\delta/2\}|\leq2\|a\|_1/\delta\).
Even without first checking measurability of that limsup set, the displayed inclusions bound its outer measure by the same quantity. Let \(k\to\infty\), then take positive rational \(\delta\). Completeness of Lebesgue measure makes the resulting exceptional set measurable and null. This proves (1.4) almost everywhere. For local \(f\), multiply by cutoffs equal to one on a countable increasing family of cubes. On their interiors sufficiently small averaging cubes are unaffected. Their null exceptional sets have null union. \(\square\)

**Lemma 1.3 (an average oscillation bound).** If \(h\) is locally Lipschitz, has weak gradient \(g\), and \(Q_r(x)\Subset B\), then, with \(h_Q=|Q|^{-1}\int_Qh\),

\[
\begin{aligned}
&\frac1{|Q|}\int_Q|h-h_Q|\\
&\quad\leq2r\sum_{j=1}^d
\frac1{|Q|}\int_Q|g_j|.
\end{aligned}
\tag{1.7}
\]

**Proof.** For smooth \(h\), bound \(|h(y)-h_Q|\) by the average over \(z\in Q\) of \(|h(y)-h(z)|\). Replace the coordinates of \(y\) by those of \(z\) one at a time and use the fundamental theorem on each segment. In the \(j\)-th term the integration in the two varying endpoints counts any intermediate coordinate value for at most \((2r)^2\) endpoint pairs. Integration in all the other coordinates and division by \(|Q|^2\) therefore bounds that term by \(2r|Q|^{-1}\int_Q|\partial_jh|\). Summing proves (1.7).

For the stated \(h\), mollify on a slightly larger cube. Lemma 1.1 and differentiated convolution give \(\partial_jh_\varepsilon=g_j*\rho_\varepsilon\). The function converges uniformly on \(Q\), by its Lipschitz bound and the shrinking support, while the weak derivatives converge in \(L^1(Q)\), by the proved local approximate-identity result. Passage to the limit proves (1.7). \(\square\)

**Theorem 1.4 (almost-everywhere differentiability).** Every locally Lipschitz map from an open subset of \(\mathbb R^d\) into \(\mathbb R^m\) is differentiable almost everywhere. For a scalar \(L\)-Lipschitz function, its differential is the weak gradient of Lemma 1.1 and has Euclidean norm at most \(L\).

**Proof.** It suffices to prove the scalar real case; intersect the finitely many full-measure sets for the components and combine their remainders. Local cubes and a countable cover reduce it to an \(L\)-Lipschitz scalar function.

Take a common Lebesgue point \(x\) of the finitely many \(g_j\)'s from Lemma 1.1. Put

\[
w(y)=h(y)-h(x)-g(x)\cdot(y-x).
\]

It is Lipschitz, \(w(x)=0\), and its weak gradient is \(g(y)-g(x)\). Lemmas 1.2 and 1.3 give

\[
\frac1{|Q_r|}\int_{Q_r}
|w-w_{Q_r}|=o(r).
\tag{1.8}
\]

Here and below \(Q_r=Q_r(x)\). We explain why this average estimate implies a pointwise differential. Let \(L'\) be a Lipschitz bound for \(w\). If \(L'=0\), then \(w=0\) near \(x\) and we are done. Otherwise, if along a sequence
\(|w_{Q_r(x)}|\geq\delta r\) for some \(\delta>0\), choose a fixed \(\theta\in(0,1)\) with \(L'\sqrt d\,\theta\leq\delta/2\). On \(Q_{\theta r}(x)\), \(|w|\leq\delta r/2\), so \(|w-w_{Q_r(x)}|\geq\delta r/2\). Its relative volume is \(\theta^d\), contradicting (1.8). Hence \(w_{Q_r(x)}=o(r)\), and consequently

\[
\frac1{|Q_r(x)|}\int_{Q_r(x)}|w|=o(r).
\tag{1.9}
\]

If some \(y\in Q_{r/2}(x)\) satisfied \(|w(y)|\geq\delta r\), choose a fixed \(\theta\leq1/2\) with \(L'\sqrt d\,\theta\leq\delta/2\). The cube \(Q_{\theta r}(y)\) lies in \(Q_r(x)\), and \(|w|\geq\delta r/2\) on it. This contradicts (1.9). Thus

\[
\sup_{y\in Q_{r/2}(x)}|w(y)|=o(r).
\tag{1.10}
\]

For \(y\to x\), use \(r=2\|y-x\|_\infty\); (1.10) gives
\(h(y)-h(x)-g(x)\cdot(y-x)=o(|y-x|)\).
This is differentiability at almost every \(x\).

At a differentiability point, the original Lipschitz inequality applied to \(y=x+tv\) gives \(|g(x)\cdot v|\leq L|v|\) after division by \(|t|\) and passage to the limit. Taking the supremum over unit \(v\) gives \(|g(x)|\leq L\). This also identifies each classical partial with the constructed weak partial almost everywhere. \(\square\)

In particular, for every compact smooth test,

\[
\int_B(\partial_jh)\psi
=-\int_Bh\,\partial_j\psi,
\tag{1.11}
\]

where the partial on the left is the almost-everywhere classical one. The graph construction below now uses a proved differentiability theorem rather than an external proof assumption.

For a compactly supported locally Lipschitz \(h\), its weak derivative has integral zero. Indeed choose a smooth test equal to one near its support. The derivative is zero off that support, and (1.11) then gives \(\int\partial_jh=0\).

## The graph Jacobian is the variation of a vector measure

Take a Lipschitz \(\gamma:B\to\mathbb R\), and work locally with

\[
\begin{gathered}
Y=\{(x',t):t<\gamma(x')\},\\
q(x')=(x',\gamma(x')).
\end{gathered}
\]

At almost every parameter point the graph has tangent vectors \(e_j+(\partial_j\gamma)e_n\). Define its outward unit normal and surface measure by the almost-everywhere graph formulas

\[
\begin{aligned}
\nu(q(x'))&=\frac{(-\nabla\gamma(x'),1)}{J(x')},\\
J(x')&=\sqrt{1+|\nabla\gamma(x')|^2},\\
dS&=q_*(J\,dx').
\end{aligned}
\tag{2.1}
\]

The Gram matrix is \(I+aa^T\), where \(a=\nabla\gamma\). By multilinearity of its columns, its determinant is \(1+\sum_j a_j^2\): terms with two replaced columns have proportional columns and vanish, and the single replacement in column \(j\) contributes \(a_j^2\). Thus the density is exactly the square root of the Gram determinant, as for a \(C^1\) graph. Sets of parameter measure zero also have zero \(dS\)-measure. Thus the normal exists \(dS\)-almost everywhere. A choice of its values on the exceptional set changes no integral.

We take Borel versions of the weak gradients, obtained by taking the pointwise limits of the almost-everywhere convergent dyadic subsequences from Lemma 1.1 where those limits exist and zero on the Borel exceptional set. Changes on null sets have no effect. The graph map is a homeomorphism onto its graph, with inverse the coordinate projection. Thus it carries Borel parameter sets to relative Borel graph sets, and the pushforward in (2.1) is well defined; its completion also includes the images of parameter null sets.

Here are the local measure-regularity details for the measurable density \(J\). On a graph column the functional \(f\mapsto\int f(q(x'))J(x')\,dx'\), for real compact continuous \(f\), is positive and finite. Indeed, the graph is relatively closed, so the part meeting a compact support has a compact parameter projection, and \(J\le\sqrt{1+L^2}\). Theorem M of the positive-measure foundation supplies a Radon measure representing this functional. For each open set, its increasing compact cutoffs and monotone convergence identify that Radon measure with the stated pushforward. On each relatively compact open set both measures are finite; their equality on relative open sets extends to all Borel sets by integration §16.2's generating-class argument. Exhaustion gives equality everywhere. The same argument with each positive and negative part of the bounded measurable components of \((\nabla\gamma,-1)\) gives locally finite signed Radon component measures.

For \(n=1\), the base is the one-point space \(\mathbb R^0\) with mass one, the gradient is empty and \(J=1\). The graph formulas therefore give unit mass to each locally isolated endpoint; no differentiability theorem in dimension zero is needed.

We will prove that this surface measure is independent of the graph chart. The argument works directly with the graph area density in (2.1).

**Theorem 2.1 (boundary measure for Lipschitz graphs).** Let \(Y\subset X\subset\mathbb R^n\) be open. Suppose every relative boundary point of \(Y\) has, after a rigid motion, a Lipschitz graph chart with \(Y\) on one side. Then the measures in (2.1) agree on overlapping charts. They define a locally finite Euclidean surface measure, and

\[
\begin{gathered}
\nabla\chi_Y=-\nu\,dS,\\
|\nabla\chi_Y|=dS,\\
\text{in }\mathcal D'(X;\mathbb R^n).
\end{gathered}
\tag{2.2}
\]

The bars on the vector measure denote its total variation in the Euclidean norm.

**Proof of the local identity.** For a smooth compact test \(\phi\) in a graph column, the vertical integration is unchanged:

\[
\begin{aligned}
&(\partial_t\chi_Y)(\phi)\\
&\quad=-\int_B(\phi\circ q)(x')\,dx'.
\end{aligned}
\tag{2.3}
\]

For \(j<n\), set

\[
G(x')=\int_{-\infty}^{\gamma(x')}\phi(x',t)\,dt.
\]

This is locally Lipschitz and has compact support in \(B\). To see its local Lipschitz bound, split the difference at two parameters into the change of the integrand over a common bounded \(t\)-interval and the change of the upper endpoint. Bounded derivatives of \(\phi\) control the first part, and \(\|\phi\|_\infty L\) controls the second. At a differentiability point of \(\gamma\), ordinary differentiation of the integral gives

\[
\partial_jG
=\int_{-\infty}^{\gamma(x')}\partial_j\phi(x',t)\,dt
+\phi(x',\gamma(x'))\partial_j\gamma.
\]

Theorem 1.4 identifies this with its weak derivative, whose integral is zero. Hence

\[
\begin{aligned}
(\partial_j\chi_Y)(\phi)
&=\int_B(\phi\circ q)\,\partial_j\gamma\,dx'.
\end{aligned}
\tag{2.4}
\]

Together (2.3)–(2.4) express the vector derivative as

\[
\begin{aligned}
m&=q_*((\nabla\gamma,-1)\,dx')\\
&=-\nu\,dS.
\end{aligned}
\tag{2.5}
\]

**Proof of the variation and chart independence.** For a vector density \(v\) against a positive measure \(\mu\), the total variation of \(v\mu\) is \(|v|\mu\). Here is the needed verification. On any set of finite \(\int|v|\,d\mu\), the triangle inequality gives

\[
\sum_k\left|\int_{E_k}v\,d\mu\right|
\le\int_E|v|\,d\mu
\]

for each finite measurable partition. For the reverse bound, cover the unit sphere by finitely many sets of diameter at most \(\varepsilon\), and partition \(E\) according to the direction \(v/|v|\). Choose a unit vector \(a_k\) in each direction set. On its corresponding piece, \(a_k\cdot v\ge(1-\varepsilon)|v|\). Therefore

\[
\begin{aligned}
\sum_k\left|\int_{E_k}v\,d\mu\right|
&\ge\sum_k a_k\cdot\int_{E_k}v\,d\mu\\
&\ge(1-\varepsilon)\int_E|v|\,d\mu.
\end{aligned}
\]

The set where \(v=0\) contributes zero. Taking the supremum over partitions and then \(\varepsilon\downarrow0\) proves the formula.

Apply it to (2.5). The graph parametrization is one-to-one, so its pushforward preserves these measurable partitions. We obtain \(|m|=q_*(\sqrt{1+|\nabla\gamma|^2}\,dx')\), precisely (2.1).

The distribution \(\nabla\chi_Y\) is already defined without a chart. Rigid rotations rotate its vector measure, by ordinary change of variables in the test pairing, and preserve its Euclidean variation. On any overlap the locally constructed component measures represent the same distributions. Compact continuous tests can be approximated uniformly by smooth tests with one common compact support, using the scalar cutoff and mollification proof. Local finiteness passes their equal pairings to these continuous tests. The signed-measure uniqueness proof in the positive-measure foundation then makes the component measures equal. Their variations, and therefore the surface measures in (2.1), agree. The densities \(-m/|m|\) give the same normal almost everywhere too. The one-sided graph description makes each such normal outward.

Each compact boundary piece has a finite chart cover. On a compact subchart the area density is bounded by \(\sqrt{1+L^2}\), so its surface mass is finite. To glue explicitly, take the countable locally finite smooth chart partition proved in U011, including interior and exterior charts with zero boundary measure. Define the global measure by summing each local graph measure weighted by its partition factor. The sum is countably additive by nonnegativity; on any chart compatibility and the partition sum identify it with the original graph measure. Compact sets meet only finitely many partition supports, proving local finiteness. Splitting a test by this partition gives the vector identity globally: the terms containing derivatives of the partition sum to zero. This proves (2.2). \(\square\)

This construction also explains why the parameter measure \(dx'\) is usually different from surface measure. The discrepancy is the speed factor in (2.1).

**Corollary 2.2 (flux and truncation).** Under Theorem 2.1, a compact \(C^1\) field satisfies

\[
\int_Y\operatorname{div}F\,dx
=\int_{\partial_XY}F\cdot\nu\,dS.
\tag{2.6}
\]

For \(u\in C^1(X)\),

\[
\partial_j(u\chi_Y)
=(\partial_ju)\chi_Y-u\nu_j\,dS.
\tag{2.7}
\]

**Proof.** Pair (2.2) with the components of a smooth compact field and sum. Approximation in \(C^1\) with one compact support proves (2.6), since the surface measure is finite on that compact set. Apply it to \(u\phi e_j\) and expand its ordinary divergence to get (2.7), just as in the preceding lesson. \(\square\)

For \(\gamma(x)=|x|\) in the plane, put \(M(\phi)=\int\phi(x,|x|)\,dx\). Then

\[
\begin{aligned}
\partial_x\chi_Y&=\operatorname{sgn}(x)M,\\
\partial_y\chi_Y&=-M,\qquad dS=\sqrt2\,M.
\end{aligned}
\tag{2.8}
\]

The corner parameter \(x=0\) has zero measure. It supplies no point mass in (2.8).

## Lipschitz tests permit a weak divergence

The continuous-field flux theorem extends to these boundaries too. We first justify its interior tests.

**Lemma 3.1 (testing an integrable divergence).** If \(F\) is continuous on open \(V\) and \(\operatorname{div}F=g\in L^1_{\mathrm{loc}}(V)\), then

\[
\int_Vg h=-\int_VF\cdot\nabla h
\tag{3.1}
\]

for every compactly supported locally Lipschitz \(h\). Its gradient on the right is the almost-everywhere gradient.

**Proof.** The support lies a positive distance from the complement of \(V\). Its zero extension is globally Lipschitz. To justify this, cover a compact neighborhood of the support by finitely many neighborhoods with Lipschitz bounds, using zero neighborhoods outside the support. A finite smaller cover supplies a distance \(\delta>0\) such that any sufficiently close pair meeting this compact neighborhood lies together in one of the original neighborhoods. These pairs obey the maximum of the finite bounds; pairs farther apart obey \(2\|h\|_\infty/\delta\). Pairs outside the neighborhood have both values zero. Lemma 1.1 gives bounded compactly supported weak derivatives. Convolve with a smooth nonnegative mollifier at radii small enough that the resulting smooth \(h_\varepsilon\) remain supported in \(V\). They converge uniformly to \(h\), and

\[
\begin{gathered}
\nabla h_\varepsilon=(\nabla h)*\rho_\varepsilon,\\
\nabla h_\varepsilon\longrightarrow\nabla h\quad\text{in }L^1.
\end{gathered}
\tag{3.2}
\]

For completeness, this last convergence is the elementary translation argument: translations are continuous in \(L^1\), first for compact continuous functions by uniform continuity and then for all \(L^1\) functions by density and invariance of the norm under translation. Integrating the translation difference against a mollifier proves (3.2).

The weak identity holds for each \(h_\varepsilon\). Uniform convergence and local integrability control its left side; boundedness of \(F\) on one common compact and (3.2) control its right side. Passage to the limit proves (3.1). \(\square\)

**Theorem 3.2 (continuous-field flux on a Lipschitz boundary).** Assume the hypotheses on the boundary in Theorem 2.1. If \(F\in C_c(X;\mathbb C^n)\) and \(\operatorname{div}F|_Y=g\in L^1(Y)\), then

\[
\begin{aligned}
&\int_Y[g\phi+F\cdot\nabla\phi]\,dx\\
&\quad=\int_{\partial_XY}\phi F\cdot\nu\,dS.
\end{aligned}
\tag{3.3}
\]

This holds for every \(\phi\in C_c^1(X)\). In particular the total integral of \(g\) is the outward flux.

**Proof.** First let \(\phi\) be supported in a single graph column, and extend it by zero within the coordinate space. Choose a nonnegative smooth function \(b\) supported in \((1/2,1)\) with integral one, using the supplied cutoff construction and normalization. Set
\[
H(s)=\int_{-\infty}^s b(r)\,dr.
\]
Then \(H=0\) for \(s\le1/2\), \(H=1\) for \(s\ge1\), \(0\le H\le1\), and \(\int H'=1\). Put \(d=\gamma(x')-t\) and \(h=\phi H(d/\varepsilon)\). This is a locally Lipschitz compact test whose support is contained in \(\operatorname{supp}\phi\cap\{d\ge\varepsilon/2\}\), a compact subset strictly inside \(Y\). Lemma 3.1 allows it in the weak identity. The almost-everywhere chain rule at differentiability points of \(\gamma\) gives

\[
\nabla H(d/\varepsilon)
=\varepsilon^{-1}H'(d/\varepsilon)(\nabla\gamma,-1).
\]

The two bulk integrals converge by dominated convergence. Put \(q_{\varepsilon,r}(x')=(x',\gamma(x')-\varepsilon r)\). The negative layer term, after \(t=\gamma(x')-\varepsilon r\), is

\[
\begin{gathered}
\int_B\!\!\int_{1/2}^1
A_{\varepsilon,r}\,dr\,dx',\\
A_{\varepsilon,r}
=H'(r)(\phi\circ q_{\varepsilon,r})V_{\varepsilon,r},\\
V_{\varepsilon,r}
=(F\circ q_{\varepsilon,r})\cdot(-\nabla\gamma,1).
\end{gathered}
\tag{3.4}
\]

The graph gradient is measurable and bounded almost everywhere; the other factors have common compact support and are bounded. Continuity of \(F,\phi\) gives the pointwise limit at almost every parameter point, and dominated convergence gives the surface integral in (3.3), since \(\int H'=1\) and (2.1) identifies its density.

This proves the formula on a graph chart. Interior and exterior charts give the weak identity or zero, respectively. A finite smooth partition for the compact test proves the global formula, cancelling the partition derivatives. Compact \(C^1\) approximation supplies the indicated test class. Finally a compact cutoff equal to one near \(\operatorname{supp}F\) gives the total flux, because \(g\) vanishes almost everywhere in \(Y\) off that support. These are the same localization steps as in the \(C^1\) proof, and require only the local identity just established. \(\square\)

## Exercises

1. **Graph area bounds — foundation.** If the Lipschitz constant of \(\gamma\) is at most \(L\) and \(E\subset B\) is measurable, prove \(|E|\le dS(q(E))\le\sqrt{1+L^2}\,|E|\). Explain why the exceptional nondifferentiability set has zero surface measure.
2. **The next derivative can see a vertex — advanced.** For \(Y=\{y<|x|\}\) and \(M\) in (2.8), prove \(\partial_x^2\chi_Y=2\delta_{(0,0)}-\partial_yM\). Use one-dimensional integration by parts along the two graph rays. Explain why this is consistent with the absence of a point mass in the first derivative.
3. **Four faces, no vertex masses — intermediate.** For \(Y=(0,a)\times(0,b)\), \(a,b>0\), write both first derivatives of its indicator as edge measures. Check the flux identity using a compact smooth field that equals \((x,0)\) near \(\overline Y\).
4. **Change which coordinate parametrizes the line — intermediate.** Rotate \(Y=\{y<3x\}\) by \((s,t)=(-y,x)\). Compute its outward normal and surface density in both graph descriptions. Verify that rotating the original normal and changing the graph parameter give the same vector measure.
5. **A crease and a rough field — intermediate.** For \(Y=\{y<|x|\}\), let \(F=(0,|x|^{1/2}\eta(x,y))\) with \(\eta\in C_c^\infty(\mathbb R^2)\). Determine its weak divergence and verify its total flux directly. Bound the contribution of the boundary segment \(|x|<\delta\) as \(\delta\downarrow0\).

**Exercise 6 (intermediate: dyadic weak derivatives).** On \(Q=[0,1]^2\), let \(h(x,y)=x^2+3xy\). Compute the face-increment approximations \(g_{1,k}\) of Lemma 1.1 on a dyadic cell of side \(\ell=2^{-k}\) and center \((c_1,c_2)\). Calculate their exact \(L^2(Q)\) error from \(\partial_1h\), and explain the consistency between levels.

**Exercise 7 (advanced: a quantitative differential).** In the scalar setting of Theorem 1.4, suppose for all sufficiently small \(r\) that

\[
\begin{gathered}
\operatorname{av}_{Q_r(x)}|g-g(x)|\leq Ar^\alpha,\\
A>0,\qquad 0<\alpha\leq1.
\end{gathered}
\]

Show that, with a constant depending on \(A,d,\alpha\) and a local Lipschitz bound,

\[
\begin{aligned}
&\sup_{y\in Q_{r/2}(x)}
|h(y)-h(x)-g(x)\cdot(y-x)|\\
&\quad\leq C r^{1+\alpha/(d+1)}.
\end{aligned}
\]

## Complete solutions

**Solution 1.** At differentiability points, the Lipschitz bound gives \(|\nabla\gamma|\le L\). The density in (2.1) is therefore between one and \(\sqrt{1+L^2}\). Integrating it over \(E\) gives both bounds. A parameter null set remains null after integration against a bounded density and pushforward. In particular the normal's exceptional set has zero \(dS\)-measure.

**Solution 2.** The first formula of (2.8) gives, on a test,

\[
(\partial_x^2\chi_Y)(\phi)
=-\int_{\mathbb R}\operatorname{sgn}(x)
\partial_x\phi(x,|x|)\,dx.
\]

On either ray, the ordinary chain rule gives

\[
\begin{aligned}
\frac d{dx}\phi(x,|x|)
&=\partial_x\phi(x,|x|)\\
&\quad+\operatorname{sgn}(x)\partial_y\phi(x,|x|).
\end{aligned}
\]

Thus the pairing is

\[
\begin{aligned}
&-\int_{\mathbb R}\operatorname{sgn}(x)
\frac d{dx}\phi(x,|x|)\,dx\\
&\quad+\int_{\mathbb R}\partial_y\phi(x,|x|)\,dx.
\end{aligned}
\]

Integrating the first integral separately on the negative and positive half-lines gives two copies of \(\phi(0,0)\); the outer endpoints vanish by compact support. The second integral is \(-(\partial_yM)(\phi)\). This proves the formula. The first derivative is an order-zero graph measure whose singleton mass is zero. Differentiating its changing direction creates a vertex term at the second level; that is an additional differentiation, not a missing first-level mass.

**Solution 3.** Let \(E_{\ell},E_r,E_b,E_t\) integrate arclength on the left, right, bottom and top open edges, respectively. Endpoints have zero measure. The normals give

\[
\partial_x\chi_Y=E_\ell-E_r,\qquad
\partial_y\chi_Y=E_b-E_t.
\]

There are no point masses at the vertices: on every graph chart the first derivative has a bounded density against the one-dimensional parameter measure, and a singleton has zero such measure. Choose a smooth compact cutoff equal to one near the rectangle, and multiply \((x,0)\) by it. Its divergence in \(Y\) is one. The bulk integral is \(ab\). The left flux is zero because \(x=0\), the right flux is \(a\) integrated over an edge of length \(b\), and the horizontal fluxes are zero. The result is \(ab\), with the correct outward signs.

**Solution 4.** Originally the graph has outward normal \((-3,1)/\sqrt{10}\) and \(dS=\sqrt{10}\,dx\). The rotated inequality is \(t>-s/3\), so the region is above its new graph. Its outward normal points below:

\[
\nu_{\mathrm{new}}
=\frac{(-1/3,-1)}{\sqrt{1+1/9}}
=\frac{(-1,-3)}{\sqrt{10}}.
\]

This is the rotation of the old normal. On the line \(s=-3x\), so \(|ds|=3\,dx\). The new density is

\[
dS=\sqrt{1+1/9}\,|ds|
=\frac{\sqrt{10}}3\,3\,dx
=\sqrt{10}\,dx.
\]

Both the positive area measure and its outward vector direction match. Surface measure uses the absolute parameter Jacobian; a negative parameter orientation does not reverse this positive density.

**Solution 5.** Testing and integrating in \(y\) gives

\[
g=\operatorname{div}F=|x|^{1/2}\partial_y\eta,
\]

a continuous compactly supported integrable function. The normal measure in (2.8) satisfies \(\nu\,dS=(-\operatorname{sgn}(x),1)\,dx\). Therefore

\[
\int_{\partial Y}F\cdot\nu\,dS
=\int_{\mathbb R}|x|^{1/2}\eta(x,|x|)\,dx.
\]

The bulk integral of \(g\) over \(y<|x|\), evaluated first in \(y\), is the same expression. On the parameter segment \(|x|<\delta\), its absolute value is at most

\[
\|\eta\|_\infty\int_{-\delta}^{\delta}|x|^{1/2}\,dx
=\frac43\|\eta\|_\infty\delta^{3/2},
\]

which tends to zero. Thus this flux has no atom at the crease, despite the field's rough tangential dependence and the normal's jump.

**Solution 6.** On \(R=[a,a+\ell]\times[b,b+\ell]\), the face increment in the first coordinate is

\[
\begin{aligned}
&\int_b^{b+\ell}
\bigl((a+\ell)^2-a^2+3\ell y\bigr)\,dy\\
&\quad=\ell^2(2c_1+3c_2).
\end{aligned}
\]

Thus \(g_{1,k}=2c_1+3c_2\) on that cell, the average there of the true gradient \(2x+3y\). Its error is \(-2(x-c_1)-3(y-c_2)\). Symmetry kills the cross term, and each centered coordinate has mean square \(\ell^2/12\). Hence

\[
\|g_{1,k}-\partial_1h\|_{L^2(Q)}^2
=\frac{13}{12}\ell^2.
\]

The mean of the four child-center values equals the parent-center value, so each finer level has the preceding level as its cell average. This verifies both the face-additivity construction and its orthogonal-error mechanism in a nonseparable example.

**Solution 7.** Put \(w=h-h(x)-g(x)\cdot(\,\cdot-x)\), and let \(L'\) bound its Lipschitz constant. If \(L'=0\), the result is immediate. The oscillation bound (1.7), and the inequality \(\sum_j|v_j|\leq\sqrt d\,|v|\), give

\[
\frac1{|Q_r|}\int_{Q_r}|w-w_{Q_r}|
\leq 2\sqrt d\,A r^{1+\alpha}.
\]

Let \(\lambda=|w(y)-w_{Q_r}|\) for \(y\in Q_{r/2}\). The Lipschitz bound and averaging give \(\lambda\leq2\sqrt d\,L'r\). The cube about \(y\) of radius \(\lambda/(4\sqrt d\,L')\) therefore fits inside \(Q_r\); on it \(|w-w_{Q_r}|\geq\lambda/2\). Its relative volume is \((\lambda/(4\sqrt d\,L'r))^d\). Consequently

\[
\lambda^{d+1}
\leq4\sqrt d\,A
(4\sqrt d\,L')^d r^{d+1+\alpha}.
\]

The same bound applies at \(y=x\). Since \(w(x)=0\), it bounds \(|w_{Q_r}|\). Adding the two bounds proves the asserted estimate. It is an explicit consequence of average gradient control and Lipschitz continuity; no pointwise continuity of \(g\) was assumed.

## References

- The supplied [boundary-flux lesson](boundary-flux-and-weak-identities.md), [order-zero distribution and measure proofs](order-positivity-and-limits.md), [local operations](local-data-and-compatible-products.md), and foundations linked above provide the exact earlier programme arguments. The full differentiability, measurable-density, variation and Lipschitz-layer proofs needed here are local.
- Juha Heinonen, *Lectures on Lipschitz Analysis*, Report 100, University of Jyväskylä, 2005, §3, Theorem 3.1 and pp. 18–23. [Full text](https://jyx.jyu.fi/handle/123456789/22526). The proof above constructs weak derivatives by dyadic face increments and proves the required maximal estimate and oscillation argument; it does not use the one-dimensional differentiability, Vitali or absolute-continuity prerequisites of Heinonen's proof.
- Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2 October 2026, §10.1.6, Proposition 10.12, p. 112. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). This gives the smooth-level-set comparison; the Lipschitz measure and flux statements here have their own complete proofs.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), 2003 reprint, ISBN 978-3-642-61497-2, §3.1, pp. 60–61, formulas (3.1.5)–(3.1.7) and the Lipschitz-boundary remark following Theorem 3.1.9. The exact copy supplies this comparison. Its inward normal has the opposite sign from the outward convention used here.
