# Disintegrating half-space restriction norms

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An estimate in each tangential Fourier fiber becomes a half-space estimate only after an exact norm identity. The easy direction restricts any full-space extension to each fiber. The reverse direction must turn independently chosen near-minimizers into one Schwartz extension. We prove that step with a finite smooth partition and keep both norm endpoints.

Read [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md), [Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## Conventions and the two quotients

Write \((x,t)\in\mathbb R^d\times\mathbb R\), with \(d\ge1\), and let \(k:\mathbb R^{d+1}\to(0,\infty)\) be a moderate weight. Thus, for some \(C\ge0\) and integer \(N\ge0\),
\[
\begin{gathered}
k(\zeta+h)\le k(\zeta)(1+C|h|)^N,\\
\qquad
 \|u\|_{p,k}=(2\pi)^{-(d+1)/p}\|k\mathcal Fu\|_{L^p},
                         \\
\quad1\le p\le\infty.
\end{gathered}
\tag{1}
\]
The exponent \(1/p\) is zero at infinity. Reversing the shift gives the reciprocal comparison and polynomial bounds on both \(k\) and \(1/k\). In particular \(k\) is continuous: its value ratio at a shift is trapped between \((1+C|h|)^{-N}\) and \((1+C|h|)^N\), which tend to one.

For \(u\in\mathcal S(\mathbb R^{d+1})\), define its negative-half-space restriction norm by
\[
\begin{gathered}
\|u\|^-_{p,k}
   \\
=\inf\{\|v\|_{p,k}:v\in\mathcal S,\ v(x,t)\\
=u(x,t)
                                      \text{ for }t<0\}.
\end{gathered}
\tag{2}
\]
Equality of these smooth functions on \(t<0\) also gives equality of their values and jets at \(t=0\) by continuity. Thus using the closed negative half-space would give the same extension family.

This is a norm on restriction classes. The triangle inequality and homogeneity follow from near-minimizing extensions. For nondegeneracy, pair with \(\phi\in C_c^\infty(\{t<0\})\). Fourier inversion and Hölder, with the reflected test transform, give
\[
\begin{gathered}
|\langle u,\phi\rangle|
 \\
\le (2\pi)^{-(d+1)/p'}
       \|\widehat\phi(-\zeta)/k(\zeta)\|_{p'}
                                     \|u\|^-_{p,k}.
\end{gathered}
\tag{3}
\]
The coefficient is finite by the reciprocal polynomial bound, including \(p'=1,\infty\). The pairing is unchanged by any extension, so taking its infimum proves the inequality. A nonzero continuous restriction would be detected by a small smooth nonnegative test with a fixed complex phase, as in [equation 4 in Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md). Consequently norm zero means restriction zero. Completeness or attainment of the infimum is not asserted.

Define the tangential transform and the time-frequency slice weight by
\[
\begin{gathered}
f_\eta(t)=\mathcal F_xu(\eta,t)
     =\int_{\mathbb R^d}e^{-ix\cdot\eta}u(x,t)\,dx,\\
\qquad
 k_\eta(s)=k(\eta,s),\\
\qquad
 V_u(\eta)=\|f_\eta\|^-_{p,k_\eta}.
\end{gathered}
\tag{4}
\]
The time norm has the one-dimensional factor \((2\pi)^{-1/p}\). Every \(k_\eta\) is moderate with the original shift constants.

**Theorem.** The exact disintegration identity is
\[
\begin{gathered}
\|u\|^-_{p,k}
       =(2\pi)^{-d/p}\|V_u\|_{L^p(\mathbb R^d)},
                          \\
\qquad1\le p\le\infty.
\end{gathered}
\tag{5}
\]
At \(p=\infty\), the right side is the ordinary supremum of the continuous function \(V_u\), equivalently its essential supremum.

## Partial transforms and varying weights

The partial transform is a continuous automorphism of the joint Schwartz space, with inverse factor \((2\pi)^{-d}\). The needed proof keeps the untransformed variable. For every fixed spatial monomial and derivative, integration by parts gives
\[
\begin{gathered}
\eta^\alpha t^r\partial_\eta^\beta\partial_t^\ell
          \mathcal F_xu(\eta,t)
   \\
=\mathcal F_x\!\left[
       D_x^\alpha\bigl((-ix)^\beta t^r\partial_t^\ell u\bigr)
                   \right](\eta,t).
\end{gathered}
\tag{6}
\]
The absolute spatial integral is bounded uniformly in \(t\) by a finite sum of actual joint Schwartz seminorms, using an integrable spatial power \(\langle x\rangle^{-J}\), \(J>d\). The full finite Leibniz formula supplies those seminorms. The same estimate for the inverse and the inversion at each fixed \(t\) prove the assertion. All time fibers therefore lie in \(\mathcal S(\mathbb R)\), depend continuously on \(\eta\) in that space, and decay with every fixed time seminorm as \(|\eta|\to\infty\).

Fix \(\xi\in\mathbb R^d\), and put \(\Lambda=(1+C|\eta-\xi|)^N\). The joint weight inequality gives, uniformly in the time frequency \(s\),
\[
 \Lambda^{-1}k_\xi(s)\le k_\eta(s)\le\Lambda k_\xi(s).
 \tag{7}
\]
These comparisons pass to full norms and restriction infima. The fixed-weight full norm is continuous on the time Schwartz space, by its polynomial weight bound and the Schwartz Fourier estimates. Hence \(a(\eta)=\|f_\eta-f_\xi\|_{p,k_\xi}\to0\) as \(\eta\to\xi\). The quotient triangle inequality and(7) give
\[
\begin{gathered}
\Lambda^{-1}(V_u(\xi)-a(\eta))
       \\
\le V_u(\eta)\\
\le\Lambda(V_u(\xi)+a(\eta)).
\end{gathered}
\tag{8}
\]
Thus \(V_u\) is continuous, including at zero and at both norm endpoints. The same argument proves continuity of the full norm
\(\eta\mapsto\|f_\eta+w\|_{p,k_\eta}\)
for each fixed \(w\in\mathcal S(\mathbb R)\). A continuous nonnegative function has the same supremum and essential supremum: a value strictly above an essential bound would persist on a nonempty open ball, which has positive measure.

## Full norms disintegrate before restriction

Fubini in the absolutely integrable Schwartz transform shows
\(\mathcal Fu(\eta,s)=\mathcal F_t f_\eta(s)\).
Tonelli for its nonnegative weighted \(p\)-th power proves, at finite \(p\),
\[
 \|u\|_{p,k}
    =(2\pi)^{-d/p}
       \left\|\eta\longmapsto\|f_\eta\|_{p,k_\eta}\right\|_{L^p}.
 \tag{9}
\]
The two factors \((2\pi)^{-d/p}\) and \((2\pi)^{-1/p}\) multiply to the full-space normalization.

At infinity the same equality follows from essential suprema on the product: for each nonnegative level, the set where the weighted transform exceeds that level has measure zero exactly when almost every time section of that set has measure zero. Tonelli applied to its indicator gives both implications. Taking countably many rational levels proves the equality of the two essential bounds. The preceding continuity lets us replace the outer essential supremum by an ordinary supremum.

Write \(T(u)=(2\pi)^{-d/p}\|V_u\|_p\). Equation(9), with \(u\) itself as a full extension, gives \(T(u)\le\|u\|_{p,k}\). If a full-space \(v\) agrees with \(u\) for \(t<0\), its tangential transform agrees in every time fiber there. Therefore \(V_u(\eta)\le\|\mathcal F_xv(\eta,\cdot)\|_{p,k_\eta}\). Taking(9) and then the full extension infimum proves
\[
 T(u)\le\|u\|^-_{p,k}.
 \tag{10}
\]
The fiber quotient triangle inequality and Minkowski also give
\[
\begin{gathered}
|T(u)-T(v)|\\
\le T(u-v)\\
\le\|u-v\|_{p,k},\\|\|u\|^-_{p,k}-\|v\|^-_{p,k}|\\
\le\|u-v\|_{p,k}.
\end{gathered}
\tag{11}
\]
These are the continuity bounds needed for the reduction below.

## Compact tangential frequency is a reduction within Schwartz space

Choose a compact smooth cutoff \(\theta\) equal to one on the unit ball. Put
\(f^{(R)}(\eta,t)=\theta(\eta/R)f_\eta(t)\),
and let \(u_R=\mathcal F_x^{-1}f^{(R)}\). Then
\[
 u_R\longrightarrow u\text{ in }\mathcal S(\mathbb R^{d+1}),
                         \qquad R\to\infty.
 \tag{12}
\]
For a direct seminorm check, the term without a cutoff derivative is supported where \(|\eta|\ge R\) and is bounded by an arbitrarily higher decay seminorm of \(f\). A term with a nonzero cutoff derivative has a factor \(R^{-j}\), lies in a fixed dilated annulus and has the same higher-decay bound. The finite Leibniz sum therefore tends to zero in every joint seminorm. Continuity of the partial inverse proves(12). Polynomial growth of \(k\), and the full Schwartz Fourier estimates, then give \(\|u_R-u\|_{p,k}\to0\), also for \(p=\infty\). By(11), proving the reverse inequality for compact tangential-frequency support suffices.

This reduction approximates an existing Schwartz function in its own topology. It makes no claim that arbitrary bounded Fourier functions are Schwartz limits.

## Finite smooth gluing of near-minimizers

Assume now \(f_\eta(t)=0\) when \(\eta\) lies outside one compact set \(K\). Choose a fixed bounded open neighborhood \(\Omega\) of \(K\). For each \(\eta\in K\) and \(\varepsilon>0\), the fiber infimum gives a time-Schwartz function \(w_\eta\), zero for \(t<0\), with
\[
 \|f_\eta+w_\eta\|_{p,k_\eta}<V_u(\eta)+\varepsilon/3.
 \tag{13}
\]
The two continuity assertions following(8) give a neighborhood \(E_\eta\) on which
\(\|f_\xi+w_\eta\|_{p,k_\xi}<V_u(\xi)+\varepsilon\).
Shrink it within \(\Omega\).

Choose finitely many such anchors \(\eta_j\) and small balls centered there whose inner open balls cover \(K\), while their closed triple-radius balls lie in \(E_{\eta_j}\). Construct cutoffs \(b_j,c_j\) with values in \([0,1]\): let \(b_j=1\) on the double-radius ball and have support in the triple-radius ball; let \(c_j=1\) on the inner ball and have support in the ball of radius three-halves the inner radius. The exact radial cutoff construction supplies them. Then \(\operatorname{supp}c_j\subset\{b_j=1\}\).

Set \(B=\sum_jb_j\), \(\psi=1-\prod_j(1-c_j)\), and
\[
\begin{gathered}
\vartheta_j=\psi b_j/B\text{ where }B>0,\\
\quad
 \vartheta_j=0\text{ where }B=0,\\
\qquad
 \sum_j\vartheta_j=\psi,\\
\quad 0\le\psi\le1.
\end{gathered}
\tag{14}
\]
The support of \(\psi\) lies in a compact subset where \(B\ge1\), so the extended quotients are smooth; no division near a vanishing denominator is hidden. The function \(\psi\) is one on a neighborhood of \(K\), and all these functions have compact support in the fixed \(\Omega\), independently of the accuracy parameter.

The finite sum
\[
\begin{gathered}
W(\xi,t)=\sum_j\vartheta_j(\xi)w_{\eta_j}(t)
             \in\mathcal S(\mathbb R^{d+1}),\\
\qquad
 W(\xi,t)=0\text{ for }t<0
\end{gathered}
\tag{15}
\]
is an actual joint Schwartz function. At a frequency with \(f_\xi\ne0\), \(\psi=1\); at a frequency with \(1-\psi>0\), \(f_\xi=0\). Thus write
\(f_\xi+W=(1-\psi)f_\xi+\sum_j\vartheta_j(f_\xi+w_{\eta_j})\).
The first term is zero, and every active cutoff lies in its anchor neighborhood. The full time-norm triangle inequality gives
\[
 \|f_\xi+W(\xi,\cdot)\|_{p,k_\xi}
             \le V_u(\xi)+\varepsilon\psi(\xi).
 \tag{16}
\]
The partial inverse of \(W\) is Schwartz and vanishes for \(t<0\), since each of its defining integrands does. Hence \(v=u+\mathcal F_x^{-1}W\) is an eligible full-space extension of \(u\). Apply(9), Minkowski and the fixed support bound:
\[
\begin{gathered}
\|u\|^-_{p,k}\\
\le\|v\|_{p,k}
 \\
\le T(u)+\varepsilon(2\pi)^{-d/p}\|\psi\|_p
 \\
\le T(u)+\varepsilon(2\pi)^{-d/p}|\Omega|^{1/p}.
\end{gathered}
\tag{17}
\]
At infinity the last factor is one, since \(\|\psi\|_\infty\le1\). The fixed finite measure of \(\Omega\) is independent of \(\varepsilon\), so letting \(\varepsilon\downarrow0\) proves the reverse inequality. Use(12)–(11) to remove the frequency cutoff. Together with(10), this proves(5).

In tangential dimension zero, the outer integration is over one point with measure one, and the identity is the definition of the one-dimensional quotient. No partition is needed.

## Exercises with complete solutions

**Exercise 1 — basic: separable data and weights.** Let \(u(x,t)=a(x)b(t)\), with Schwartz factors, and \(k(\eta,s)=k_1(\eta)k_2(s)\) with moderate factors. Calculate the full restriction norm, including its normalization and both endpoints.

**Solution.** The tangential transform is \(\widehat a(\eta)b(t)\). The weight factor \(k_1(\eta)\) is a positive scalar in the time norm. Exact homogeneity of the extension infimum gives
\[
\begin{gathered}
V_u(\eta)=k_1(\eta)|\widehat a(\eta)|\|b\|^-_{p,k_2},
 \\
\qquad
 \|u\|^-_{p,k}
                  =\|a\|_{p,k_1}\|b\|^-_{p,k_2}.
\end{gathered}
\tag{18}
\]
Theorem(5) supplies the factor \((2\pi)^{-d/p}\) in the spatial norm; the time quotient already has \((2\pi)^{-1/p}\). At infinity both factors are one. The equality allows all full-space extensions, not only products, and does not assume either time infimum is attained.

**Exercise 2 — intermediate: why arbitrary fiber choices cannot be inverted.** Let \(h\in C_c^\infty((0,1))\) be nonzero. Define \(W(\eta,t)=0\) for \(\eta<0\) and \(W(\eta,t)=h(t)\) for \(\eta\ge0\), in one tangential dimension. Every time section is Schwartz and vanishes for \(t<0\). Explain why this is not yet a permissible correction to a full-space Schwartz extension.

**Solution.** At a time where \(h(t)\ne0\), the function jumps at \(\eta=0\). It is not even continuous there, so it is not jointly Schwartz. If its partial inverse were a full-space Schwartz function, the continuous Schwartz partial-transform theorem(6) would make \(W\) jointly Schwartz, a contradiction. Sectionwise admissibility therefore does not justify applying the inverse transform in the required class. The finite construction(14)–(15) replaces independent sections by compact smooth coefficient functions, while retaining their negative-time vanishing and their uniform norm accuracy. A product \(\vartheta(\eta)h(t)\), with \(\vartheta\in C_c^\infty\), is a valid joint Schwartz correction; its validity follows from the full product seminorms.

**Exercise 3 — advanced: the infinity endpoint does not follow from general density.** Prove that the indicator \(1_{[0,1]}\) on the frequency line has essential-supremum distance at least \(1/2\) from every continuous function. Explain why this does not obstruct(12).

**Solution.** Suppose a continuous complex-valued \(g\) had essential error \(c<1/2\). On \((0,1)\), its real part is at least \(1-c>1/2\) almost everywhere; continuity extends this bound to every interior point, because a strict violation would persist on an interval of positive measure. On an interval to the left of zero, its real part is at most \(c<1/2\), by the same argument. The two limits at zero contradict continuity. Therefore
\[
 \inf_{g\text{ continuous}}
           \|g-1_{[0,1]}\|_{L^\infty}\ge1/2.
 \tag{19}
\]
In particular general \(L^\infty\) Fourier functions need not be uniformly approximable by Schwartz functions. In(12) the starting partial transform is already jointly Schwartz, and its cutoff tails tend to zero in every existing seminorm. The full weighted infinity norm is continuous on that space. The endpoint proof therefore uses a valid approximation within Schwartz space and the finite extension partition, not the false density assertion.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
