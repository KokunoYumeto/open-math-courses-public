# Limiting measures

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Along the extremal sequence of [From packing to a power saving](from-packing-to-a-power-saving.md), each configuration carries the labels of [Rank coordinates](rank-coordinates.md). This lesson records the configurations by four kinds of measures on the label cube \(Z\), for vertices, participating vertices of a window, edges with their times, and crossings between two windows, and passes to weak limits. Three relations among the limits drive the rest of the course [OpenAI-HL, Section 3]: edge mass is controlled by vertex mass (Lemma 2.1); given its label, the time of an edge has a nonatomic distribution (Lemma 3.1); and every positive part of edge mass is seen by crossings between disjoint windows, whose projections to their own rank coordinates are at most planar Lebesgue measure (Lemma 4.1).

Notation from the extremal sequence: \(N,a,R\), \(E_*=Ra^2\), \(M=aN\), with \(E_*^3\ge\xi_0^3a^2N^4\) and \(E_*/M\to\infty\). Measures, weak convergence and conditional measures are as in [Measures on compact metric spaces](measures-on-compact-metric-spaces.md).

## 1. The measures and their limits

In each configuration, a vertex \(q\) has the label \(z(q)\in Z\). A vertex *participates* in a window \(J\) if it is an endpoint of an edge of \(J\); there are \(S_J\) such vertices. An edge \(e\) has a *left endpoint* \(q_e\) (Lemma 3.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md)) and a *time* \(t_e\), the time of its batch. Define, for windows \(J\) and disjoint windows \(I,J\):

| Object | Measure | Mass of one object |
|---|---|---|
| vertex | \(\mu^{(n)}\) on \(Z\), at \(z(q)\) | \(N^{-1}\) |
| vertex participating in \(J\) | \(\mu_J^{(n)}\) on \(Z\), at \(z(q)\) | \(N^{-1}\) |
| edge | \(\nu^{(n)}\) on \(Z\times[0,1]\), at \((z(q_e),t_e)\) | \(E_*^{-1}\) |
| crossing of an \(I\)-edge and a \(J\)-edge | \(\sigma_{IJ}^{(n)}\) on \(Z\), at the label of the point | \(M^{-2}\) |

The masses are bounded: \(\mu^{(n)}\) and \(\nu^{(n)}\) are probability measures, \(\mu_J^{(n)}\le\mu^{(n)}\), and \(\sigma_{IJ}^{(n)}(Z)\le1\) because crossings of \(I\) and \(J\) occupy different pairs of grid slots (proof of Proposition 4.1 of [Rank coordinates](rank-coordinates.md)). There are countably many windows. By Theorem 3.2 of [Measures on compact metric spaces](measures-on-compact-metric-spaces.md) we pass to a subsequence along which all these measures converge weakly; their limits are \(\mu\), \(\mu_J\), \(\nu\) and \(\sigma_{IJ}\). Inequalities between measures survive weak limits, by testing with continuous functions and Lemma 1.1 there; so \(\mu_J\le\mu\). Put
\[
\begin{gathered}
s_J=\mu_J(Z)=\lim\frac{S_J}N,\\
\lambda=\pi_*\nu,\qquad\lambda_J(F)=\nu(F\times J),
\end{gathered}
\]
where \(\pi:Z\times[0,1]\to Z\) is the projection and \(F\subseteq Z\) is Borel. Then \(\lambda\) and \(\lambda_J\) count edges by their left endpoints, with edge weights; \(\lambda_J\) is additive over disjoint windows.

**Lemma 1.1.** (a) The image of \(\nu\) on the time coordinate is Lebesgue measure on \([0,1]\). Every window satisfies \(\lambda_J(Z)=|J|\), and \(\nu^{(n)}(\cdot\times J)\to\nu(\cdot\times J)\) weakly on \(Z\).

(b) There are probability measures \(h_z\) on \([0,1]\), Borel in \(z\), with \(\lambda_J(F)=\int_Fh_z(J)\,d\lambda(z)\) for all Borel \(F\) and windows \(J\).

(c) For disjoint windows \(I,J\), the image of \(\sigma_{IJ}\) under \(z\mapsto(z_I,z_J)\) is at most Lebesgue measure on \([0,1]^2\).

(d) For every \(\delta=2^{-m}\) and \(u>0\), at most \(C_1u^{-4/3}\) windows of length \(\delta\) have \(s_J>u\), where \(C_1\) is the constant of Theorem 6.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md).

*Proof.* (a) Each batch has \(a^2\) edges, so the time image of \(\nu^{(n)}\) is \(R^{-1}\sum_i\delta_{(i-1/2)/R}\), which converges weakly to Lebesgue measure. Window endpoints are therefore null for the time image of \(\nu\), and Lemma 2.1(b) of [Measures on compact metric spaces](measures-on-compact-metric-spaces.md) gives the convergence of the restrictions and of their masses.

(b) This is Proposition 5.1 there.

(c) By Proposition 4.1 of [Rank coordinates](rank-coordinates.md), for continuous \(f\ge0\) on the square, \(\int f(z_I,z_J)\,d\sigma_{IJ}^{(n)}\) is at most a Riemann sum of \(f\) plus \(\omega_f(3/M)\); in the limit it is at most \(\int f\). By Lemma 1.1 there this extends from continuous functions to all Borel sets.

(d) In each configuration, the windows of length \(\delta\) cover step-disjoint intervals of the sweep. A participating vertex of \(J\) changes membership during the interval covered by \(J\), so a window with \(S_J>uN\) covers an interval of activity at least \(\lceil uN\rceil\). By Theorem 6.1 there are at most \(C_1(N/\lceil uN\rceil)^{4/3}\le C_1u^{-4/3}\) of them (for \(u\le1\); for \(u\ge1\) there are none, since \(S_J\le N\)). A window with \(s_J>u\) has \(S_J>uN\) in all late configurations. \(\square\)

## 2. Edge mass and vertex mass

**Lemma 2.1.** There is a constant \(C\), depending only on \(\xi_0\), such that for every window \(J\) and every Borel \(F\subseteq Z\),
\[
\lambda_J(F)^3\le C\,s_J^3\,\mu_J(F).
\]
In particular \(\lambda(F)^3\le C\mu(F)\), and \(\lambda\) is absolutely continuous with respect to \(\mu\). The same holds when the labels \(z(q)\) are replaced by labels \(\tilde z(q)\) in any compact metric space, with the measures defined in the same way and a further subsequence along which they converge.

*Proof.* For a set \(U\) of labels, let \(e(U)\) be the number of edges of \(J\) whose left endpoint has its label in \(U\), and \(m(U)\) the number of these left endpoints. By Corollary 6.3 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md),
\[
e(U)^3\le4608\,a^2m(U)S_J^3+13824\,S_J^3 .
\]
Divide by \(E_*^3\ge\xi_0^3a^2N^4\) and use \(S_J\le N\):
\[
\begin{aligned}
\Bigl(\frac{e(U)}{E_*}\Bigr)^3\le{}&\frac{4608}{\xi_0^3}\,\frac{m(U)}N\Bigl(\frac{S_J}N\Bigr)^3\\
&+\frac{13824}{\xi_0^3}\,\frac1{a^2N}.
\end{aligned}
\]
Here \(e(U)/E_*=\nu^{(n)}(U\times J)\) and \(m(U)/N\le\mu_J^{(n)}(U)\).

Let \(F\) be compact, \(\rho>0\), and \(U\) the open \(\rho\)-neighbourhood of \(F\). Since the boundary of \(J\) is null for the time image of \(\nu\), Lemma 2.1 of [Measures on compact metric spaces](measures-on-compact-metric-spaces.md) gives \(\liminf\nu^{(n)}(U\times J)\ge\nu(U\times J)\), which is at least \(\lambda_J(F)\), while \(\limsup\mu_J^{(n)}(U)\) is at most \(\limsup\mu_J^{(n)}(F^{[\rho]})\le\mu_J(F^{[\rho]})\), and the term \(13824\,\xi_0^{-3}/(a^2N)\) tends to zero, since \(N\to\infty\). So \(\lambda_J(F)^3\le Cs_J^3\mu_J(F^{[\rho]})\) with \(C=4608\,\xi_0^{-3}\), and letting \(\rho\to0\) gives the inequality for compact \(F\). Both sides are inner regular (Lemma 1.1 there), which gives it for Borel \(F\). The window \([0,1]\) has \(s=\mu(Z)=1\). The proof never used the nature of the labels. \(\square\)

## 3. No atoms in conditional time

**Lemma 3.1.** For \(\lambda\)-almost every \(z\), the probability measure \(h_z\) has no atoms.

*Proof.* Fix \(\beta>0\) and a partition of \([0,1]\) into the windows of length \(\delta=2^{-m}\). Let \(A_J=\{z:h_z(J)>\beta\}\), a Borel set. Since \(\sum_Jh_z(J)=1\), each \(z\) lies in fewer than \(1/\beta\) of the sets \(A_J\), so
\[
\sum_J\mu_J(A_J)\le\sum_J\mu(A_J)\le\frac1\beta .
\]
Fix \(M_0\ge1\). By Lemma 1.1(d), at most \(C_1M_0^{-4/3}\delta^{-1}\) windows have \(s_J>M_0\delta^{3/4}\), and each has \(\lambda_J(Z)=\delta\); they contribute at most \(C_1M_0^{-4/3}\) to \(\sum_J\lambda_J(A_J)\). For the other windows, Lemma 2.1 and Hölder's inequality over at most \(\delta^{-1}\) windows give
\[
\begin{aligned}
&\sum_J\lambda_J(A_J)\\
&\quad\le C^{1/3}M_0\delta^{3/4}\sum_J\mu_J(A_J)^{1/3}\\
&\quad\le C^{1/3}M_0\delta^{3/4-2/3}\Bigl(\sum_J\mu_J(A_J)\Bigr)^{1/3}\\
&\quad\le C^{1/3}M_0\beta^{-1/3}\delta^{1/12}.
\end{aligned}
\]
With \(f_m(z)=\sum_Jh_z(J)\mathbf 1_{A_J}(z)\), over the windows of length \(2^{-m}\), this shows
\[
\begin{aligned}
\int f_m\,d\lambda&=\sum_J\lambda_J(A_J)\le C_1M_0^{-4/3}\\
&\quad+C^{1/3}M_0\beta^{-1/3}2^{-m/12}.
\end{aligned}
\]
Letting \(m\to\infty\) and then \(M_0\to\infty\), \(\int f_m\,d\lambda\to0\). If \(h_z\) has an atom of mass greater than \(\beta\), the window of length \(2^{-m}\) containing it has \(h_z(J)>\beta\), so \(f_m(z)>\beta\) for every \(m\). By Fatou's lemma, such \(z\) form a \(\lambda\)-null set. Take \(\beta=1/k\) for all \(k\). \(\square\)

## 4. Edge mass sees crossings

**Lemma 4.1.** Let \(K\) be a window, and let \(F\subseteq Z\) be a Borel set with \(\sigma_{IJ}(F)=0\) for all disjoint windows \(I,J\subseteq K\). Then \(\lambda_K(F)=0\).

*Proof.* By inner regularity we may take \(F\) compact. Fix a resolution \(\delta=2^{-m}\le|K|\), and let \(\mathcal W\) be the windows of length \(\delta\) inside \(K\) with \(s_J\le\delta^{2/3}\). By Lemma 1.1(d) the other windows of length \(\delta\) in \(K\) number at most \(C_1\delta^{-8/9}\), so they carry \(\lambda_K\)-mass at most \(C_1\delta^{1/9}\).

Fix \(\rho>0\). In configuration \(n\), *retain* the edges of the windows in \(\mathcal W\) whose left endpoint has its label in the open \(\rho\)-neighbourhood of \(F\) and whose label oscillation \(\operatorname{osc}_ez\) is at most \(\rho\). Their number \(e\) satisfies
\[
\liminf\frac e{E_*}\ge\lambda_K(F)-C_1\delta^{1/9},
\]
by the lower bound for open sets in each window, as in the proof of Lemma 2.1, and because at most \(2M/\rho=o(E_*)\) edges have oscillation above \(\rho\) (Section 6 of [Rank coordinates](rank-coordinates.md)).

The retained edges form a straight-line drawing on at most \(N\) vertices, so by Lemma 5.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md), with all vertices designated,
\[
\begin{aligned}
\Bigl(\frac e{E_*}\Bigr)^3&\le\frac{2304\,N^2\operatorname{cr}+13824\,N^3}{E_*^3}\\
&\le\frac{2304}{\xi_0^3}\,\frac{\operatorname{cr}}{M^2}+\frac{13824}{\xi_0^3}\,\frac1{a^2N},
\end{aligned}
\]
where \(\operatorname{cr}\) counts crossing pairs of retained edges. A crossing point of a retained edge lies within \(\rho\) of the label of its left endpoint, so its label lies in the closed set \(F^{[2\rho]}\). Crossings between retained edges of different windows \(I\ne J\) in \(\mathcal W\) therefore number at most \(M^2\sigma_{IJ}^{(n)}(F^{[2\rho]})\), and the \(\limsup\) of their normalized number is at most \(\sigma_{IJ}(F^{[2\rho]})\). Crossings within one window \(J\) number at most \(2a^2S_J^2\), so after division by \(M^2=a^2N^2\) their total has \(\limsup\) at most \(2\sum_{J\in\mathcal W}s_J^2\le2\delta^{-1}\delta^{4/3}=2\delta^{1/3}\). Hence
\[
\begin{aligned}
&\bigl(\lambda_K(F)-C_1\delta^{1/9}\bigr)_+^3\\
&\quad\le\frac{2304}{\xi_0^3}\Bigl(\sum_{\{I,J\}}\sigma_{IJ}(F^{[2\rho]})\\
&\qquad\qquad+2\delta^{1/3}\Bigr),
\end{aligned}
\]
the sum over unordered pairs of distinct windows of \(\mathcal W\). As \(\rho\to0\), \(F^{[2\rho]}\) decreases to \(F\), and the sum tends to \(0\). Then let \(\delta\to0\). \(\square\)

Equivalently, \(\lambda_K\) is absolutely continuous with respect to every finite measure \(\sum c_{IJ}\sigma_{IJ}\) with all coefficients \(c_{IJ}>0\), over disjoint windows \(I,J\subseteq K\).

## 5. Summary

The limits retain three features of the extremal configurations, which are the inputs of the following lessons: two separated rank coordinates parametrize the plane (Proposition 3.2 of [Rank coordinates](rank-coordinates.md)); conditional time has no atoms (Lemma 3.1); and every positive part of edge mass is detected by a crossing measure whose projection to its own rank coordinates is at most planar Lebesgue measure (Lemmas 1.1(c) and 4.1).

## 6. Exercises

**6.1** (easy). Show that \(\sum_J\lambda_J=\lambda\) over the windows of any partition of \([0,1]\) into dyadic windows, and that \(\int h_z(J)\,d\lambda(z)=|J|\).

**6.2** (medium). Lemma 2.1 measures edges by their left endpoints. Explain why the proof would fail if each edge were recorded at its midpoint instead, and why it would still work with right endpoints.

## 7. Solutions

**6.1.** The windows of the partition are disjoint with union \([0,1]\), so \(\sum_J\nu(F\times J)=\nu(F\times[0,1])=\lambda(F)\). Taking \(F=Z\) in Lemma 1.1(b) gives \(\int h_z(J)\,d\lambda=\lambda_J(Z)=|J|\).

**6.2.** The proof bounds the number of edges whose recorded point has its label in \(U\) by the crossing inequality with designated endpoints, which needs a set of vertices, the recorded endpoints, of size controlled by the vertex measure \(\mu_J(U)\). Midpoints are not vertices, and their labels are not controlled by \(\mu_J\). Right endpoints are vertices, and Corollary 6.3 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md) holds with right endpoints designated, by the same proof.

## References

- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
