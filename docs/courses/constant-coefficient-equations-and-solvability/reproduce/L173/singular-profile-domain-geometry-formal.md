# Singular Fourier profiles and convex equation domains

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

One compact kernel can have several different logarithmic Fourier carriers. Its convex singular hull records their combined extent, but a domain supporting arbitrary singularity classes must accommodate each carrier separately. We prove the exact family criterion and show how it becomes an equality of support values at differentiable boundary normals. The converse requires a geometric fact that we prove here: regular supporting planes recover every proper open convex domain.

Basic references are [Grubb's Fourier-distribution notes](https://web.math.ku.dk/~grubb/dist5.pdf), [Melrose's differential-analysis course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. Theorem 2.1, Corollary 2.2 and Theorem 3.1 of Recovering singularities from convolution profiles prove the arbitrarily small isolated-singularity realization and the full inverse carrier criterion. Its equation (1.3) recovers the singular hull from the carrier family. Theorem 3.2 and Definition 3.3 of Convolution modulo smooth functions and compact singularity bounds supply compact singularity confinement and its boundary-distance meaning.

Finite-dimensional compactness, scalar completeness and coordinate calculus are proved in Metric and topological foundations. The complete-metric Baire theorem is Section 6 of Banach estimates, quotient spaces and compact parameter arguments. Compactness of the convex hull of a compact Euclidean set is proved in the proof of Theorem CF4.1 of Compact Fourier division and multiplicity-sensitive annihilators. We supply all the additional convex boundary and domain arguments below.

## 1. The family of compact carriers

Let \(\mu\) be a compact invertible distribution on \(\mathbb R^n\), \(n\ge1\). Put
\[
 S=\operatorname{conv}(\operatorname{sing\,supp}\mu).
 \tag{1.1}
\]
It is nonempty and compact. An invertible compact distribution is nonsmooth, by the slow-decrease characterization in Slow decrease and entire Fourier division. Let \(\mathcal K(\mu)\) be the compact convex carriers whose support functions are the indicators of its logarithmic Fourier profiles. Invertibility excludes collapsed profiles, so every member is nonempty. The preceding hull theorem gives
\[
 K\subset S\quad(K\in\mathcal K(\mu)),\qquad
 S=\overline{\operatorname{conv}\bigcup_{K\in\mathcal K(\mu)}K},
 \qquad
 H_S(\eta)=\sup_{K\in\mathcal K(\mu)}H_K(\eta).
 \tag{1.2}
\]
Here \(H_K(\eta)=\max_{k\in K}k\cdot\eta\).

Reflection has the exact effect
\[
 \mathcal K(\check\mu)=\{-K:K\in\mathcal K(\mu)\}.
 \tag{1.3}
\]
Indeed \(F_{\check\mu}(\zeta)=F_\mu(-\zeta)\). Replacing an escaping center \(c\) and profile variable \(z\) by \(-c,-z\) preserves the denominator \(\log|c|\) and gives the reflected profile. Its indicator is \(H_K(-\eta)=H_{-K}(\eta)\). Applying reflection twice proves both inclusions in (1.3).

For an open \(U\) and nonempty compact \(K\), define the translation domain
\[
 E_K(U)=\{x:x-K\subset U\}.
 \tag{1.4}
\]
This is not the ordinary Minkowski difference \(U-K=\{u-k:u\in U,k\in K\}\). The former requires containment for every point of \(K\); the latter uses one chosen point.

## 2. Elementary convex separation and translation domains

**Lemma 2.1 (supporting planes for open convex sets).** If \(U\) is nonempty, proper, open and convex, then
\[
 \operatorname{int}\overline U=U.
 \tag{2.1}
\]
Every \(x\notin U\) has a nonzero \(\nu\) and a finite \(\beta\) with
\[
 \nu\cdot u<\beta\le\nu\cdot x\quad(u\in U).
 \tag{2.2}
\]
At \(x\in\partial U\), one can take \(\beta=\nu\cdot x\).

*Proof.* Convexity passes to \(C=\overline U\) by taking limits of line segments. If \(x\in\operatorname{int}C\), place a small simplex about \(x\) inside that interior: in translated coordinates take the vertices \(\varepsilon e_i\), \(1\le i\le n\), and \(-\varepsilon\sum_i e_i\). Its barycentric coordinates at \(x\) are all \(1/(n+1)\). Approximate each vertex by points of \(U\). For sufficiently close approximations, the matrix determining barycentric coordinates stays invertible and those coordinates stay positive, by determinant continuity and finite linear algebra. Thus \(x\) lies in the convex hull of points of \(U\), so \(x\in U\). This proves (2.1).

For \(x\notin C\), choose a nearest point \(p\in C\). Existence follows by restricting distance minimization to a sufficiently large closed ball, then using compactness. For every \(z\in C\), the segment \(p+t(z-p)\) lies in \(C\). Comparing its squared distance from \(x\) with the minimum at \(p\), dividing by \(t>0\), and letting \(t\downarrow0\), gives
\[
 (x-p)\cdot(z-p)\le0.
 \tag{2.3}
\]
The vector \(x-p\) is nonzero. Set \(\nu=x-p\), \(\beta=\nu\cdot p\). The inequality is strict on \(U\), since equality at an interior point would be violated by a small displacement in direction \(\nu\). Also \(\beta<\nu\cdot x\).

For \(x\in\partial C=\partial U\), choose \(x_j\notin C\) tending to \(x\). Its nearest points \(p_j\) tend to \(x\), since \(|x_j-p_j|\le|x_j-x|\). Normalize the vectors \(x_j-p_j\); compactness of the unit sphere gives a convergent subsequence with unit limit \(\nu\). Pass (2.3) to the limit for each \(z\in C\): \(\nu\cdot(z-x)\le0\). Strictness on \(U\) follows as before. Taking \(\beta=\nu\cdot x\) proves the boundary assertion and (2.2). The nearest-point and boundary arguments also prove that \(C\) is proper: if \(C=\mathbb R^n\), (2.1) would give \(U=\mathbb R^n\). \(\square\)

**Lemma 2.2 (compact translation domains).** The set \(E_K(U)\) is open. If \(U\) is convex, it is convex. If \(C,K\) are nonempty compact convex sets, then \(E_K(C)\) is compact and convex, possibly empty. For nonempty open convex \(U\),
\[
 E_K(U-K)=U.
 \tag{2.4}
\]

*Proof.* For \(x-K\subset U\), its compactness gives a positive boundary margin, hence all sufficiently small translations of \(x\) still have the containment. If \(U=\mathbb R^n\) the assertion is immediate. Convexity follows by applying it pointwise for each \(k\in K\), or by taking the intersection of the convex sets \(U+k\).

The compact version is \(\bigcap_{k\in K}(C+k)\), a closed convex set contained in \(C+k_0\) for any \(k_0\in K\). It is therefore bounded and compact.

The forward inclusion in (2.4) follows directly from the Minkowski difference. If \(U\) is proper and \(x\notin U\), choose \(\nu,\beta\) from Lemma 2.1 and choose \(k_0\in K\) minimizing \(\nu\cdot k\). Every \(y\in U-K\) satisfies
\[
 \nu\cdot y<\beta+H_K(-\nu).
 \tag{2.5}
\]
But \(\nu\cdot(x-k_0)\ge\beta+H_K(-\nu)\), so \(x-k_0\notin U-K\). Thus \(x\notin E_K(U-K)\). The whole-space case of (2.4) is immediate. \(\square\)

## 3. Regular supporting planes recover the domain

A boundary point is **regular** if it has exactly one outward supporting-normal ray. In a local convex graph, this is the condition that the graph be differentiable there. We now prove the required density and reconstruction without assuming a measure-theoretic differentiability theorem.

**Lemma 3.1 (dense regular boundary points).** Regular points are dense in the boundary of every nonempty proper open convex \(U\subset\mathbb R^n\).

*Proof, local graph.* At a boundary point move the point to zero, choose \(q\in U\), and rotate coordinates so \(q=(0,a)\), \(a>0\). Choose a ball \(B_r(q)\subset U\), with \(r<a\). A supporting vector at zero from Lemma 2.1 has negative last coordinate, since its scalar product with \(q\) is negative. Its inequality therefore gives a finite affine lower bound on the last coordinate along each vertical line.

For \(|y|<r\), the vertical line at \(y\in\mathbb R^{n-1}\) meets \(U\) at height \(a\). Define \(f(y)\) as the infimum of its interval of heights in \(U\). It is finite by the supporting lower bound and is at most \(a\). Convexity of \(U\), using heights slightly above the infima, makes \(f\) convex. Also \(f(0)=0\). The supporting inequality bounds it below by zero. For \(0<\lambda<1\), convexity of \(\overline U\), the point \(0\in\overline U\), and the ball \(B_r(q)\subset U\) give \(B_{\lambda r}(\lambda q)\subset\overline U\). Lemma 2.1 puts this open ball in \(U\). Its center has height \(\lambda a\), arbitrarily close to zero.

On a smaller horizontal ball the function is Lipschitz. Its affine lower bound and the bound \(a\) give a finite oscillation on \(|y|<3r/4\). For two points in \(|y|<r/4\), extend the line through them in either direction by distance \(r/2\), staying in that larger ball. The monotonic secant slopes of a convex one-variable restriction bound the difference quotient between the two points by the oscillation divided by \(r/2\). This proves a finite Lipschitz constant. In a sufficiently small neighborhood of zero, the boundary of \(U\) is exactly the graph \(t=f(y)\): the vertical section is an interval, its lower endpoint is \(f(y)\), and the ball at \(q\) gives an upper interval of heights independent of small \(y\).

*Proof, density of differentiability for a finite convex graph.* Work inside a ball where \(f\) is Lipschitz, with a slightly larger such ball available. For each coordinate \(i\), its finite one-sided derivatives obey
\[
 \partial_i^-f(y)\le\partial_i^+f(y).
 \tag{3.1}
\]
The right derivative is the infimum of the continuous positive-step difference quotients over sufficiently small steps; it is upper semicontinuous. The left derivative is the supremum of the continuous negative-step quotients; it is lower semicontinuous. Thus their gap is upper semicontinuous, and the sets
\[
 F_{i,m}=\{y:\partial_i^+f(y)-\partial_i^-f(y)\ge1/m\}
 \tag{3.2}
\]
are closed relative to the smaller ball.

They have empty interior. Otherwise a segment parallel to the \(i\)-th coordinate inside such an interior would have a jump of at least \(1/m\) at every point in it. The one-variable derivatives are monotone and bounded by the Lipschitz constant \(L\). At any \(N\) ordered points, their jumps add to at most \(2L\), since the right derivative at one point is no larger than the left derivative at the next. Choosing \(N>2Lm\) contradicts the asserted jumps.

Inside any further closed ball of positive radius, the sets (3.2) are closed and nowhere dense; a relatively open piece contains an interior point of that ball. Baire therefore gives a point outside their countable union for all coordinates. At it every coordinate derivative exists.

We verify full differentiability at such a point \(y\). A subgradient exists at every interior point: apply Lemma 2.1 to the open convex epigraph \(\{(z,t):t>f(z)\}\), over a horizontal ball about the point. An outward supporting vector has last coordinate strictly negative. If that coordinate were zero, variations of the horizontal variable in every direction would make the whole vector zero. Normalize it to \((p,-1)\); the supporting inequality gives
\[
 f(z)\ge f(y)+p\cdot(z-y).
 \tag{3.3}
\]
Coordinate testing places \(p_i\) between the two one-sided derivatives. Hence at our point every subgradient equals the vector of coordinate derivatives. Local subgradients are bounded by the Lipschitz constant in every coordinate.

For \(h_j\to0\), choose subgradients \(p_j\) at \(y+h_j\). Each subsequential limit is a subgradient at \(y\), by passing (3.3) to the limit for every fixed nearby \(z\). Uniqueness and boundedness give \(p_j\to p\). The two subgradient inequalities give
\[
 0\le f(y+h_j)-f(y)-p\cdot h_j
                 \le(p_j-p)\cdot h_j=o(|h_j|).
 \tag{3.4}
\]
Thus \(f\) is differentiable. Since Baire worked in any smaller closed ball, differentiability points are dense.

At a differentiable graph point, every boundary supporting vector has strictly negative last coordinate by the same epigraph argument, and its normalized horizontal component is a subgradient. Uniqueness gives exactly one normal ray. Dense graph points therefore give dense regular boundary points. In dimension one the nonempty proper open convex set is an interval, a ray or a bounded interval; each existing endpoint has one outward normal ray, so the assertion is immediate. \(\square\)

**Lemma 3.2 (regular halfspace reconstruction).** Let \(R\) be the regular boundary points of such a \(U\), with unit outward normal \(\nu_q\) at \(q\). Then
\[
 \overline U=\bigcap_{q\in R}\{x:\nu_q\cdot x\le\nu_q\cdot q\},
 \qquad
 U=\operatorname{int}\bigcap_{q\in R}
                    \{x:\nu_q\cdot x\le\nu_q\cdot q\}.
 \tag{3.5}
\]

*Proof.* Every listed halfspace contains \(\overline U\). For \(x\notin\overline U\), choose \(z\in U\) and a ball \(B_r(z)\subset U\). The ray from \(z\) through \(x\) first exits the closed convex set at a point \(p\), and
\[
 x=z+t(p-z),\qquad t>1.
 \tag{3.6}
\]
The intersection of the ray with the closed convex set is a closed interval with a positive initial length and an endpoint before \(x\), which proves this assertion.

Choose regular \(q_j\to p\) by Lemma 3.1. Because the supporting halfspace at \(q_j\) contains \(B_r(z)\), its unit normal satisfies \(\nu_{q_j}\cdot(q_j-z)\ge r\). Consequently
\[
 \nu_{q_j}\cdot(x-q_j)
 \ge (t-1)r-t|p-q_j|>0
 \tag{3.7}
\]
for sufficiently large \(j\). Its halfspace excludes \(x\). This proves the first equality; Lemma 2.1 gives the second. Taking the interior is essential: a nondifferentiable boundary point can satisfy strictly all the regular-plane inequalities while still lying on the boundary of their intersection. \(\square\)

## 4. The exact family criterion for two convex domains

Let \(X_1,X_2\) be nonempty open convex sets with
\[
 X_2-\operatorname{sing\,supp}\mu\subset X_1.
 \tag{4.1}
\]
Convexity makes this equivalent to \(X_2-S\subset X_1\). Hence
\[
 X_2\subset E_S(X_1)\subset E_K(X_1)
                        \quad(K\in\mathcal K(\mu)).
 \tag{4.2}
\]

The pair is **convex for singular supports** when, for every compact \(K_1\subset X_1\), there is a compact \(K_2\subset X_2\) such that every \(v\in\mathcal E'(X_2)\) with \(\operatorname{sing\,supp}(\check\mu*v)\subset K_1\) has \(\operatorname{sing\,supp}v\subset K_2\). Here \(\mathcal E'(X_2)\) means globally defined distributions with compact support inside \(X_2\). For the present invertible kernel this is exactly the boundary-distance condition proved in Theorem 3.2 of the preceding quotient-convolution lesson.

**Theorem 4.1 (profile-carrier domain criterion).** The pair is convex for singular supports if and only if
\[
 E_K(X_1)\subset X_2
                   \quad\text{for every }K\in\mathcal K(\mu).
 \tag{4.3}
\]
In that case every set in (4.2) equals \(X_2\).

*Proof of necessity.* Fix \(K\in\mathcal K(\mu)\), \(x\in E_K(X_1)\), and \(x_0\in X_2\). Choose a compact convex \(C\subset X_1\) containing \((x-K)\cup(x_0-K)\): the compact convex hull of that union works and lies in the open convex \(X_1\). Put
\[
 D=E_K(C).
 \tag{4.4}
\]
It is compact and convex by Lemma 2.2, and contains both \(x,x_0\).

For every \(y\in D\cap X_2\), the exact isolated-singularity realization for the reflected carrier \(-K\) supplies a compact distribution \(v_y\) with arbitrarily small support about \(y\), singular exactly at \(y\), and
\[
 \operatorname{conv}
   \operatorname{sing\,supp}(\check\mu*v_y)=y-K\subset C.
 \tag{4.5}
\]
Take its support inside \(X_2\). Compact singularity confinement then puts every \(y\in D\cap X_2\) in one compact \(C_2\subset X_2\).

The set \(D\cap X_2\) is relatively open in \(D\), nonempty, and relatively closed: any limit in \(D\) of its points remains in the closed \(C_2\subset X_2\). The convex \(D\) is connected, by its line segments. Thus \(D\cap X_2=D\), giving \(x\in X_2\). This proves (4.3) without requiring a full support bound on the realization independent of \(y\).

*Proof of sufficiency.* Suppose (4.3). Given nonempty compact \(K_1\subset X_1\), let \(C=\operatorname{conv}K_1\Subset X_1\) and choose
\[
 \delta=\min\{1,\operatorname{dist}(C,X_1^c)\}>0,\qquad
 D=\bigcup_{K\in\mathcal K(\mu)}E_K(C).
 \tag{4.6}
\]
If the complement is empty, its distance is infinite. The set \(D\) is bounded uniformly: if \(x-K\subset C\), choose any \(k\in K\subset S\), giving \(x=(x-k)+k\in C+S\). For each such \(x\) and each \(|h|<\delta\), one has
\(x+h-K\subset C+B_\delta(0)\subset X_1\), so (4.3) gives \(x+h\in X_2\).

If \(D\ne\varnothing\), put \(K_2=\overline{\operatorname{conv}D}\). It is compact, since it lies in the compact convex \(C+S\). Convexity of \(X_2\) preserves the \(\delta\)-ball containment under finite convex combinations: use the same displacement \(h\) at every point. Limits retain distance at least \(\delta\) from the closed complement. Thus
\[
 K_2\Subset X_2.
 \tag{4.7}
\]

Every \(y\) with \(y-K\subset C\) for a profile carrier \(K\) belongs to \(K_2\). By (1.3), these are exactly the inequalities
\[
 H_{-K}(\eta)+y\cdot\eta\le H_C(\eta)
                                      \quad(\eta\in\mathbb R^n).
 \tag{4.8}
\]
The full inverse carrier criterion applied to \(\check\mu\), \(C,K_2\) therefore gives
\(\operatorname{sing\,supp}v\subset K_2\) whenever
\(\operatorname{sing\,supp}(\check\mu*v)\subset K_1\).

If \(D=\varnothing\), the same criterion applies with any one-point receiver in \(X_2\), because its geometric premise has no solutions. Apply it to two different point receivers; every possible input singular support is contained in their empty intersection. Take \(K_2=\varnothing\). If \(K_1=\varnothing\), invertibility and the exact smoothing characterization likewise make every input smooth, again allowing the empty receiver. All confinement cases follow. Equations (4.2), (4.3) give the final equality assertion. \(\square\)

## 5. A singleton carrier family

**Corollary 5.1.** If the nonsmooth compact kernel has the single profile indicator \(H_S\), then a convex pair satisfying (4.1) is convex for singular supports if and only if
\[
 X_2=E_S(X_1)
    =\{x:x-\operatorname{sing\,supp}\mu\subset X_1\}.
 \tag{5.1}
\]
For every nonempty open convex \(U\), the choice
\[
 X_2=U,\qquad X_1=U-S
 \tag{5.2}
\]
has this property.

*Proof.* The singleton indicator is proper because the kernel is nonsmooth and \(S\ne\varnothing\). It excludes collapsed profiles, hence gives invertibility by the slow-decrease theorem. The carrier family is \(\{S\}\), so Theorem 4.1 and compatibility give exactly (5.1). The equivalence between the two containments in (5.1) uses convexity of \(X_1\). For (5.2), \(U-S\) is open and convex, and Lemma 2.2 gives \(E_S(U-S)=U\). Thus (5.1) holds. This covers unbounded convex domains and the whole space. \(\square\)

## 6. Every regular boundary normal sees the same carrier extent

**Theorem 6.1 (necessary reflected-normal equality).** If the convex pair satisfying (4.1) is convex for singular supports, and \(x\in\partial X_2\) is regular with unit outward normal \(\nu\), then
\[
 H_K(-\nu)=H_S(-\nu)
                     \quad(K\in\mathcal K(\mu)).
 \tag{6.1}
\]
In particular the value is independent of the carrier. This conclusion concerns these boundary-normal directions.

*Proof.* Theorem 4.1 gives \(E_K(X_1)=X_2\) for every \(K\). Choose \(x_j\in X_2\) tending to \(x\). For every \(k\in K\), \(x_j-k\in X_1\), hence \(x-k\in\overline X_1\). Since \(x\notin E_K(X_1)\), some \(k_0\in K\) has
\[
 x-k_0\in\partial X_1.
 \tag{6.2}
\]
Existence of this point also shows that \(X_1\) is proper. Choose a nonzero supporting normal \(\eta\) there by Lemma 2.1.

For every \(x'\in X_2\) and every \(s\in S\), compatibility gives \(x'-s\in X_1\), and thus
\[
 \eta\cdot(x'-s)\le\eta\cdot(x-k_0).
 \tag{6.3}
\]
Taking \(s=k_0\) makes \(\eta\) an outward normal of \(X_2\) at \(x\). Regularity means that it is a positive multiple of \(\nu\), so rescale it to \(\nu\). Taking \(x'\to x\) in (6.3) then gives
\[
 -\nu\cdot s\le-\nu\cdot k_0\quad(s\in S).
 \tag{6.4}
\]
Since \(k_0\in K\subset S\), the maximum of \(-\nu\cdot s\) on \(S\) is attained at a point of \(K\). Equality (6.1) follows. The negative normal sign is determined by the sampled point \(x'-s\); no conjugation or reversal of the domain roles occurs. \(\square\)

## 7. Constructing the solution domain from the normal condition

**Theorem 7.1 (normal criterion for a prescribed convex equation domain).** Let \(U\ne\mathbb R^n\) be a nonempty open convex set. Suppose that for every unit normal \(\nu\) at every regular boundary point of \(U\), the value \(H_K(-\nu)\) is independent of \(K\in\mathcal K(\mu)\). Then
\[
 X_2=U,\qquad X_1=U-S
 \tag{7.1}
\]
is convex for singular supports.

*Proof.* For each stated normal, equation (1.2) identifies the common value:
\[
 H_K(-\nu)=H_S(-\nu)\quad(K\in\mathcal K(\mu)).
 \tag{7.2}
\]
The set \(X_1\) is nonempty, open and convex. Compatibility follows directly from \(\operatorname{sing\,supp}\mu\subset S\).

Fix \(K\) and \(y\in E_K(X_1)\). At a regular boundary point \(q\) of \(U\) with normal \(\nu\), every point of \(X_1=U-S\) satisfies
\[
 \nu\cdot z<\nu\cdot q+H_S(-\nu).
 \tag{7.3}
\]
Choose \(k_0\in K\) maximizing \(-\nu\cdot k\). Since \(y-k_0\in X_1\), (7.2), (7.3) give
\[
 \nu\cdot y+H_K(-\nu)
          <\nu\cdot q+H_S(-\nu),
 \qquad \nu\cdot y<\nu\cdot q.
 \tag{7.4}
\]
This holds at every regular supporting plane. Lemma 3.2 therefore puts \(E_K(X_1)\) inside \(\overline U\). Lemma 2.2 makes that translation domain open, so it lies in \(\operatorname{int}\overline U=U\). Thus (4.3) holds for every profile carrier. Theorem 4.1 gives the desired singular-support convexity.

The interior step avoids inferring membership in \(U\) merely from strict inequalities for a possibly nonopen infinite intersection. The proof uses no boundedness assumption on \(U\). \(\square\)

## References

- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard B. Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, freely readable [course materials](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The exact Fourier realization, inverse carrier criterion and compact singularity condition are the preceding lessons linked above. The separation, dense regular boundary, supporting-plane reconstruction and full two-domain profile geometry are proved here.
