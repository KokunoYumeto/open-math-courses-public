# Compact rectangles and completion of a scalar measure

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original exposition: public domain (CC0).*

These two elementary constructions make explicit the square compactness used before bounded normal calculus and the completion operation used before the Borel-representative argument SS4. They assume the complete ordered real field, elementary set theory with choice, and the definitions of topology and a measure. The interval-compactness proof and the scalar integration arguments are supplied in [scalar integration, Sections 0–2](../../OA-MOD/notes/analytic-programme/scalar-integration-programme.html); the compact-metric consequences are proved in [SS2](../../OA-MOD/notes/analytic-programme/spectral-scalar-prerequisites.html#ss2-the-topology-needed-on-a-compact-metric-space).

<a id="sc01"></a>
## SC01. A closed rectangle is compact

Let \(Q=[a,b]\times[c,d]\subset\mathbb R^2\), where \(a\le b\) and \(c\le d\). The completeness proof in scalar integration, Section 0, shows that each coordinate interval is compact. Given an open cover of \(Q\), choose, for each \((x,y)\in Q\), relative open intervals \(V_{x,y}\) about \(x\) and \(W_{x,y}\) about \(y\) whose product lies in one cover member. Such intervals exist from the Euclidean metric: a sufficiently small product of coordinate balls lies in the chosen metric ball.

Fix \(x\). Compactness of the vertical interval chooses finitely many \(W_{x,y_j}\) covering \([c,d]\). Their corresponding horizontal intervals have an open intersection \(V_x=\bigcap_jV_{x,y_j}\) containing \(x\). The strip \(V_x\times[c,d]\) is therefore covered by the finitely many selected original cover members. The sets \(V_x\) cover \([a,b]\). Horizontal interval compactness now chooses finitely many such strips. Combining their finite lists gives a finite subcover of \(Q\). This proves compactness, including either degenerate interval.

With the Euclidean metric, a continuous real or complex function on \(Q\) is bounded and uniformly continuous. Boundedness follows by finitely covering \(Q\) by neighborhoods on which the function differs from its central value by less than one. For uniform continuity, given \(\varepsilon>0\), choose at each \(x\in Q\) a radius \(r_x>0\) giving oscillation from its value less than \(\varepsilon/2\) on that ball. Finitely many balls of radii \(r_x/2\) cover \(Q\). Take \(\delta>0\) to be the minimum of those finitely many half-radii. Two points less than \(\delta\) apart lie in the full-radius ball of a common selected centre, so their values differ by less than \(\varepsilon\). The same argument works on any compact metric space.

The distance functions, maxima and finite partitions used for compact subsets of \(Q\) are exactly the consequences proved in SS2. Thus no compactness theorem for an infinite product, general normal-space extension theorem, or measure representation is required for NC2–NC4.

<a id="sc02"></a>
## SC02. Completion exists without finiteness or sigma-finiteness

Let \((X,\Sigma,\mu)\) be any measure space. Define
\[
 \bar\Sigma=\{E\subset X:\ E\mathbin\triangle B\subset N
 \text{ for some }B,N\in\Sigma,\ \mu(N)=0\}.
 \tag{SC1}
\]
Set \(\bar\mu(E)=\mu(B)\) for any such representative \(B\). This is independent of the representative. If \(B,C\) represent the same \(E\), then \(B\mathbin\triangle C\) is contained in the union of two measurable null sets. Removing that union gives the same measurable set from \(B\) and \(C\). Measure additivity consequently gives \(\mu(B)=\mu(C)\), even if that common value is infinite.

The empty set lies in \(\bar\Sigma\). Complements preserve (SC1), using the complemented Borel or measurable representative and the same null set. For \(E_n\mathbin\triangle B_n\subset N_n\), the union satisfies
\[
 \left(\bigcup_nE_n\right)\mathbin\triangle\left(\bigcup_nB_n\right)
 \subset\bigcup_nN_n.
\]
The right side is measurable and null by countable additivity. Thus \(\bar\Sigma\) is a sigma-algebra containing \(\Sigma\).

For countable additivity of \(\bar\mu\), let the \(E_n\) be disjoint and put \(N=\bigcup_nN_n\). The measurable sets \(B_n'=B_n\setminus N\) are disjoint: outside \(N\), membership in \(B_n\) agrees with membership in \(E_n\). They have \(\mu(B_n')=\mu(B_n)\), and their union represents \(\bigcup_nE_n\). Countable additivity of \(\mu\) therefore proves
\[
 \bar\mu\left(\bigcup_nE_n\right)
 =\sum_n\mu(B_n')
 =\sum_n\bar\mu(E_n).
 \tag{SC2}
\]
Also \(\bar\mu(\varnothing)=0\), so this is a measure extending \(\mu\).

If \(\bar\mu(E)=0\), choose \(E\mathbin\triangle B\subset N\) as in (SC1). Then \(E\subset B\cup N\), a measurable null set. Every subset of \(E\) consequently satisfies (SC1) with representative the empty set, and has completed measure zero. This proves completeness. Conversely every sigma-algebra of a complete measure extending \(\mu\) must contain all such \(E\), since it contains \(B,N\) and every subset of \(N\). This is the usual minimal completion.

For a nonnegative \(\Sigma\)-measurable function, its original and completed integrals agree: they agree on simple functions by the measure extension, and increasing simple approximation and monotone convergence prove agreement in general. Real and complex integrable functions follow by their parts. Applying SS4 now constructs a \(\Sigma\)-measurable representative of every completed-measurable complex function, by replacing the finitely many level sets of each simple approximant and taking its limit outside the union of the exceptional measurable null sets. In particular the two scalar \(L^2\) quotients and their linear-first pairings agree canonically. No arbitrary nonmeasurable modification is asserted to be literally \(\Sigma\)-measurable.
