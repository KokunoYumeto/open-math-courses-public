# Singularities and nonconvex logarithmic carriers

Original exposition, examples and complete solutions: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

Logarithmic Fourier limits tell us which convex carrier is visible at a selected sequence of frequencies. Taking all their support functions recovers the convex hull of the singular support. There is more information before that last convexification: the singular support lies in the **closed union** of the individual carriers.

This lesson proves that sharper containment. It also explains why the contour direction may vary with the frequency, how a compact cutoff can have enough nearly analytic derivatives, and why the finite Taylor error still decays at an arbitrarily high rate.

## 7. Keep the individual carriers

Let \(u\) be a compact distribution on \(\mathbb R^n\). Use the same convention as the preceding lessons:

\[
 D=-i\partial,\qquad
 F(\zeta)=\widehat u(\zeta),\qquad
 L_u(z,c)=\frac{\log|F(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2. \tag{7.1}
\]

A proper local \(L^1\) limit \(v\) has an indicator \(h_v\), the support function of a nonempty compact convex set \(C_v\). A collapsed limit has empty carrier. The full definitions and joint convergence are in Joint logarithmic-frequency limits. The indicator construction is proved in Plurisubharmonic envelopes and support functions.

**Theorem 7.1.** Let the union range over every proper logarithmic profile. Then

\[
 \operatorname{sing\,supp}u
 \subset
 \overline{\bigcup_v C_v}. \tag{7.2}
\]

The complete proof is Theorem 1.1 below. It uses an explicit logarithmic partition in Section 3 and a finite Taylor identity in Section 4.

The closure matters. The theorem does not promise that a singular point belongs to one particular carrier. It also does not promise that every point of a profile carrier is singular. For example, two point masses can have a segment as a profile carrier.

The preceding convex-hull identity, proved in Locating singularities through logarithmic Fourier strips, Theorem 4.1, is compatible with (7.2). Convexification can fill an open gap between individual carriers; (7.2) can still detect that gap.

## 8. A frequency chooses its own direction

Suppose a point \(x_0\) stays at distance at least \(r>0\) from every proper carrier. Translate \(x_0\) to zero. Each translated compact convex carrier has a unit separating normal \(\theta\) with

\[
 h(\theta)\leq-r. \tag{8.1}
\]

There need not be one normal that works for all carriers. The normal is chosen separately for every logarithmic frequency cell.

At a real center \(c\), with \(R=|c|\), a sufficiently large frequency has a proper indicator \(h_c\) satisfying

\[
 |F(c+\zeta)|\leq R^{N+1}e^{h_c(\operatorname{Im}\zeta)}
 \quad (|\zeta|\leq m\log R). \tag{8.2}
\]

Here \(N\) is a fixed Fourier growth order and \(m\) is fixed after the desired derivative order is chosen. Lemma 2.1 proves this uniform statement from profile compactness and Hartogs comparison. An unsuccessful center would give a limiting profile whose own indicator contradicts that failure.

On the shifted cell \(\xi+it\theta\), for \(|x|\leq r/2\), the product needed for inversion obeys

\[
 |e^{ix\cdot(\xi+it\theta)}F(\xi+it\theta)|
 \leq R^{N+1}e^{t(h_c(\theta)-x\cdot\theta)}
 \leq R^{N+1}e^{-rt/2}. \tag{8.3}
\]

This is the source of decay. The compact cutoff requires a correction because it is smooth rather than holomorphic.

![Two separated singular carriers, a smooth point inside their common convex hull, and their different separating normals.](figures/nonconvex-carriers-and-separating-normals.png)

The exact example behind this figure is Worked example 3. The two line segments are actual singular supports, not projections of a larger object. The point \(x_0=(-3/2,1)\) is inside their convex hull but outside their union. The horizontal and downward normals separate their translated carriers by different amounts. The formal separation proof is Lemma 2.2.

## 9. Why the finite correction is small

At dyadic level \(j\), the real frequency radius is comparable to \(2^j\). Use cells of side length

\[
 \ell_j=j/\varepsilon,\qquad K=j, \qquad T_j=j/\varepsilon. \tag{9.1}
\]

A small fixed \(\varepsilon\) makes the cells and their vertical displacement wide enough to gain strong decay. It also makes their first \(j+1\) derivatives small:

\[
 \|\partial_\theta^s\phi\|_\infty
 \leq a_\varepsilon^s,\qquad
 a_\varepsilon=65\sqrt n\,\varepsilon,\quad0\leq s\leq j+1. \tag{9.2}
\]

Section 3 constructs this partition. It convolves interval probability densities a finite number of times and adds one smooth final density. Each controlled derivative falls on a different interval factor. Exact lattice tiling gives a sum of one. A telescoping dyadic cutoff gives the annuli.

Extend each cell only along its chosen direction by a finite Taylor sum:

\[
 \Phi(\xi,t)=\sum_{s=0}^j\frac{(it)^s}{s!}\partial_\theta^s\phi(\xi).
 \tag{9.3}
\]

Its failure to solve the holomorphic transport equation is exactly one last derivative:

\[
 \partial_t\Phi-i\partial_\theta\Phi
 =-i\frac{(it)^j}{j!}\partial_\theta^{j+1}\phi. \tag{9.4}
\]

The contour identity has a top integral and a correction integral. Their decay factors are bounded by

\[
 e^{-rj/(4\varepsilon)}
 \quad\text{and}\quad
 \left(\frac{2a_\varepsilon}{r}\right)^{j+1}, \tag{9.5}
\]

respectively. The second factor follows from the exact cancellation

\[
 \int_0^\infty e^{-rt/2}\frac{t^j}{j!}\,dt=(2/r)^{j+1}. \tag{9.6}
\]

The real cell volumes and their number together contribute at most a fixed constant times \(2^{jn}\). Each spatial derivative of order at most \(b\) costs at most another factor comparable to \(2^{jb}\). Decreasing \(\varepsilon\) for this fixed budget makes the whole level sum bounded by a constant times \(2^{-j}\).

![A logarithmic frequency cell, its directional finite Taylor shift, and the two decaying contributions to the local inverse Fourier integral.](figures/logarithmic-cell-and-taylor-correction.png)

The real and complex cell drawing is a one-direction slice: its coordinates are displacement along a cell's chosen real normal and displacement along the corresponding imaginary normal. It does not depict all of \(\mathbb C^n\). The quantitative bounds and exact sign are proved in Lemma 4.1 and Proposition 5.1.

Different derivative budgets may use different partitions. Every convergent series represents the same distribution on the ball, so their continuous representatives coincide. This proves smoothness of one representative to every order; it does not require one fixed cutoff with infinitely many controlled derivatives.

## Worked example 1. A point mass and its exact carrier

Let \(u=\delta_a\), with \(a\in\mathbb R^n\). Then

\[
 F(\zeta)=e^{-ia\cdot\zeta},\qquad
 L_u(z,c)=a\cdot\operatorname{Im}z. \tag{10.1}
\]

Every escaping sequence has the same proper profile. Its support function is \(h(\eta)=a\cdot\eta\), and its carrier is \(\{a\}\). Thus the closed union in Theorem 7.1 is exactly \(\{a\}\), agreeing with the singular support.

At \(x_0\ne a\), translate the origin. The carrier becomes \(\{a-x_0\}\). Choose
\(\theta=-(a-x_0)/|a-x_0|\), so that \(h(\theta)=-|a-x_0|\). The entire window estimate is exact with order zero:
\(|F(c+\zeta)|=e^{h(\operatorname{Im}\zeta)}\leq R e^{h(\operatorname{Im}\zeta)}\) for \(R>2\).
The shifted inverse contribution therefore gains exponential decay near the new origin. In this example the distribution actually vanishes away from \(a\); the general argument establishes smoothness there without assuming that vanishing in advance.

## Worked example 2. Four interval factors give four controlled derivatives

Take one dimension, \(\ell=4\), and \(q=4\). Convolve four uniform probability densities on intervals of length
\(\ell/(4q)=1/4\), then a symmetric smooth probability density supported in \([-1/2,1/2]\). The resulting \(\kappa\) is supported in \([-1,1]\). Put

\[
 \tau(\xi)=(1_{[-2,2)}*\kappa)(\xi),\qquad
 \tau_k(\xi)=\tau(\xi-4k). \tag{10.2}
\]

The functions are smooth, sum to one, and have supports in \([4k-3,4k+3]\). They overlap at most twice. The central cutoff is one on \([-1,1]\).

The distributional derivative of each interval probability density has total variation \(2/(1/4)=8\). Assigning different derivatives to different factors proves

\[
 \|\tau^{(s)}\|_\infty\leq8^s,\qquad0\leq s\leq4. \tag{10.3}
\]

Symmetry gives \(\tau(2)=\tau(-2)=1/2\): at \(\xi=2\), the indicator selects the nonnegative half of the continuous symmetric density. Only \(\tau_0\) and \(\tau_1\) are nonzero there, and they each equal \(1/2\).

The final smooth factor makes \(\tau\) smooth to all orders. Estimate (10.3) controls only the first four. Increasing \(q\) as the frequency grows is how the proof obtains more controlled derivatives.

## Worked example 3. A disconnected union detects a hole in the convex hull

Choose a nonnegative smooth bump \(f\), positive on \((-1,1)\), zero outside \([-1,1]\). Define on \(\mathbb R^2\)

\[
 u_1=\delta_{-2}(x_1)\otimes f(x_2),\qquad
 u_2=f(x_1)\otimes\delta_2(x_2),\qquad u=u_1+u_2. \tag{10.4}
\]

Their supports are disjoint line segments

\[
 K_1=\{-2\}\times[-1,1],\qquad
 K_2=[-1,1]\times\{2\}. \tag{10.5}
\]

Each point in the relative interior of either segment is singular. To see this, integrate the distribution against a smooth test function in its tangential coordinate with nonzero pairing against \(f\). A smooth local representative would then give a smooth transverse marginal, but that marginal is a nonzero point mass. The endpoints are singular by closedness of the singular support. Outside the two supports the sum is zero, and near either support the other summand is zero. Therefore

\[
 \operatorname{sing\,supp}u=K_1\cup K_2. \tag{10.6}
\]

We can also locate every proper profile carrier. Their transforms are

\[
 F_1(\zeta)=e^{2i\zeta_1}\widehat f(\zeta_2),\qquad
 F_2(\zeta)=\widehat f(\zeta_1)e^{-2i\zeta_2}. \tag{10.7}
\]

Let \(R_j=|c_j|\to\infty\). On a subsequence either
\(|c_{j,1}|\geq R_j/\sqrt2\) always, or
\(|c_{j,2}|\geq R_j/\sqrt2\) always.
In the first case \(F_2(c_j+z\log R_j)\) decreases faster than every power of \(R_j\), uniformly on each compact \(z\)-set. Indeed, the first coordinate's real part remains comparable to \(R_j\), while its imaginary part and the other exponential's exponent are bounded by constants times \(\log R_j\). The whole-complex rapid Fourier estimate for the smooth bump absorbs those fixed powers. That estimate is proved in Locating singularities through logarithmic Fourier strips, the smooth remainder calculation in Section 1.

If \(u\)'s profile is proper, pass to a further common subsequence on which \(u_1\)'s profile is proper or collapsed. It cannot collapse: the two transform summands would then both collapse uniformly, and their sum would collapse. For proper limits \(v\) of the sum and \(w\) of the first summand, extract an almost-everywhere convergent subsequence from both local \(L^1\) convergences. At almost every point the limits are finite. The two triangle inequalities
\[
 |F_1+F_2|\leq|F_1|+|F_2|,\qquad
 |F_1|\leq|F_1+F_2|+|F_2| \tag{10.8}
\]
give \(v\leq w\) and \(w\leq v\) after taking logarithms and dividing by \(\log R_j\); the extra \(\log2/\log R_j\) tends to zero and the second summand tends to \(-\infty\). Hence the canonical profiles coincide. The carrier of the sum is therefore contained in \(K_1\), by the ordinary compact-carrier bound.

In the second coordinate case the same argument interchanges the summands and puts the proper carrier in \(K_2\). Thus every proper carrier is contained in one of these two sets. Theorem 7.1 now gives both inclusions needed for

\[
 A(u)=K_1\cup K_2. \tag{10.9}
\]

This identifies the closed union without classifying every individual profile.

The point \(x_0=(-3/2,1)\) lies inside \(\operatorname{conv}(K_1\cup K_2)\), but its distance from \(K_1\) is \(1/2\) and from \(K_2\) is \(\sqrt5/2\). The nonconvex theorem detects its smooth neighborhood. After translation, \(\theta_1=(1,0)\) bounds the first carrier by \(-1/2\), while \(\theta_2=(0,-1)\) bounds the second by \(-1\). Both work with \(r=2/5\), but they are different directions.

## Worked example 4. An explicit derivative budget

Take \(n=1\), \(u=D\delta_{-2}\), and examine a neighborhood of zero. Its transform is
\[
 F(\zeta)=\zeta e^{2i\zeta},\qquad N=1,\qquad
 h(\eta)=-2\eta,\quad \theta=1,\quad r=2. \tag{10.10}
\]

For a budget of two derivatives, choose \(\varepsilon=10^{-4}\). Then
\[
 a_\varepsilon=13/2000,\qquad
 r/(4\varepsilon)=5000,\qquad
 2a_\varepsilon/r=13/2000<1/64. \tag{10.11}
\]

Here \(N+1+b+n+1=6\), so all three conditions in (5.1) hold. At \(j=26\),
\[
 128(j+3)/2^j=3712/67108864<10^{-4},\qquad
 (3/4)\ell_j=195000<2^{j-3}. \tag{10.12}
\]

Both inequalities continue to improve for larger \(j\). Choose the integer \(m=50495\), which is larger than
\(35000/\log2\), the lower bound in (5.2). At every center in these levels,
\(R\geq2^{24}>2m\). Since \(\log R\leq R\) and \(R\geq2\),
\[
 R+m\log R\leq R+R^2/2\leq R^2. \tag{10.13}
\]

Consequently the window estimate is explicit:
\(|F(c+\zeta)|\leq R^2e^{-2\operatorname{Im}\zeta}\) when \(|\zeta|\leq m\log R\).
There is no unknown frequency threshold in this example. The remaining bounds in (3.7) and the inequality \(|\zeta|\leq2R\) also hold for \(j\geq26\), since their linear factors in \(j\) are already smaller than the stated exponential lower bounds at \(26\).

The level sum for derivatives through order two is bounded by a fixed constant times
\[
 2^{5j}\left(e^{-5000j}+(13/2000)^{j+1}\right). \tag{10.14}
\]

The correction ratio between adjacent levels is
\(2^5(13/2000)=26/125<1/2\). The top term decreases much faster. The finitely many earlier levels go into the smooth low-frequency term.

These generous constants make the proof transparent. For a higher derivative budget one can decrease \(\varepsilon\) again; all resulting local representatives agree as distributions.

## Exercises with complete solutions

The ten exercises total 100 points. A solution should state the relevant quantifiers and conventions as well as calculate the requested bound.

### Exercise 1. Translate the profile and the carrier — 8 points

For \(u_0(x)=u(x+x_0)\), compute its transform, logarithmic profiles, indicators and carriers. Include collapsed profiles.

**Solution.** A change of variables in the distribution pairing gives
\(F_0(\zeta)=e^{ix_0\cdot\zeta}F(\zeta)\).
For \(\zeta=c+z\log|c|\), its additional logarithmic modulus divided by \(\log|c|\) is
\(-x_0\cdot\operatorname{Im}z\). Thus a proper profile \(v\) becomes
\(v_0=v-x_0\cdot\operatorname{Im}z\).
The indicator changes by the same linear function:
\(h_0(\eta)=h(\eta)-x_0\cdot\eta\).
This is the support function of \(C_h-x_0\). A collapsed limit remains collapsed because the added term is bounded on each compact \(z\)-set. Applying the inverse translation proves that no profiles are omitted.

### Exercise 2. Handle an empty family correctly — 8 points

Explain why a nonzero smooth compact distribution cannot be bounded by \(R^{N+1}e^{-\infty}\). State how the theorem and window argument handle collapsed limits.

**Solution.** The proposed right side is zero. A nonzero compact distribution has a nonzero entire transform, so it cannot vanish throughout a whole complex window. The theorem handles an all-collapsed profile family before choosing any windows: Lemma 1.2 proves that the transform is rapidly decreasing on the real space and the distribution is smooth, so its singular support is empty. When a proper profile exists but a particular unsuccessful-center sequence collapses, the proof of Lemma 2.1 chooses one fixed proper indicator \(h_0\). Its minimum on the compact parameter ball is finite. Uniform collapse beats the finite ceiling \(N+1+h_0\), contradicting the claimed failure. It never substitutes the collapsed indicator into a positive transform bound.

### Exercise 3. Differentiate probability factors — 10 points

For \(\ell=6\) and \(q=3\), find the uniform interval length, the support half-width of the full density, and the derivative bound through order three for an indicator convolved with it.

**Solution.** Each interval has length \(\ell/(4q)=1/2\). The three uniform factors have total half-width \(3(1/4)=3/4\). The smooth final factor has half-width \(\ell/8=3/4\), so the density's half-width is \(3/2=\ell/4\). A differentiated interval factor is the difference of endpoint masses divided by \(1/2\), with total variation \(4\). Put each of at most three derivatives on a different uniform factor. All undifferentiated factors have mass one, so convolution with an indicator bounded by one gives supremum at most \(4^s=(8q/\ell)^s\) for \(0\leq s\leq3\). Smoothness at higher orders follows from the final smooth density, but this fixed numerical bound is not claimed there.

### Exercise 4. Check the dyadic annular constants — 10 points

Prove the support radii \(7\cdot2^j/16\) and \(9\cdot2^j/8\) for \(\psi_j\), and explain its nonnegativity.

**Solution.** The density in \(\chi_j\) has half-width \(2^{j-3}\). Hence \(\chi_j=1\) on the cube of radius \(2^j-2^{j-3}=7\cdot2^j/8\), and vanishes outside the cube of radius \(2^j+2^{j-3}=9\cdot2^j/8\). The support of \(\chi_{j-1}\) has radius \(9\cdot2^j/16\), inside the flat region of \(\chi_j\). Therefore \(\chi_j-\chi_{j-1}\geq0\). Both functions are one when \(|\xi|_\infty\leq7\cdot2^j/16\), so their difference is zero there. Outside the larger support it is also zero. This proves the two radii, and the telescoping sum proves the partition identity.

### Exercise 5. A directional derivative costs a dimension factor — 8 points

If \(\|\partial^\alpha\phi\|_\infty\leq A^{|\alpha|}\) for \(|\alpha|\leq K+1\), show the corresponding bound for a unit directional derivative. Evaluate the bound for \(\theta=(1,1)/\sqrt2\).

**Solution.** The multinomial expansion gives
\[
 |\partial_\theta^s\phi|
 \leq A^s\sum_{|\alpha|=s}\frac{s!}{\alpha!}|\theta|^\alpha
 =A^s\left(\sum_i|\theta_i|\right)^s
 \leq(A\sqrt n)^s.
 \tag{11.1}
\]
For the stated two-dimensional direction, the sum of absolute coordinates is exactly \(\sqrt2\), so the resulting bound is \((A\sqrt2)^s\). This is the source of the factor \(\sqrt n\) in (9.2); it is not a change in Fourier normalization.

### Exercise 6. Recover the contour correction sign — 10 points

Set \(K=0\), \(n=1\), \(\theta=1\), and \(G(\zeta)=e^{i\omega\zeta}\) with real \(\omega\). Check the plus sign in (4.2) directly for any smooth compact cutoff \(\phi\).

**Solution.** Let \(I_0=\int e^{i\omega\xi}\phi(\xi)\,d\xi\). The top integral is \(e^{-\omega T}I_0\). Integration by parts gives
\(\int e^{i\omega\xi}\phi'(\xi)\,d\xi=-i\omega I_0\).
Thus the correction with the displayed plus sign is
\[
 i\int_0^T e^{-\omega t}(-i\omega I_0)\,dt
 =\omega I_0\int_0^T e^{-\omega t}\,dt
 =(1-e^{-\omega T})I_0. \tag{11.2}
\]
For \(\omega=0\), this is zero and the top is \(I_0\). For every other \(\omega\), the top and correction sum to \(I_0\) as required. A minus sign would give \((2e^{-\omega T}-1)I_0\) and fail in general.

### Exercise 7. Why uncontrolled factorial growth is too large — 10 points

Compute the correction estimate if one only had
\(\|\partial_\theta^{K+1}\phi\|_\infty\leq a^{K+1}(K+1)!\).
Compare it with the controlled finite-derivative estimate.

**Solution.** The Taylor remainder still contains \(t^K/K!\). Its integral against \(e^{-rt/2}\) is \((2/r)^{K+1}\). The weaker derivative hypothesis would therefore leave
\[
 (K+1)!\,(2a/r)^{K+1}. \tag{11.3}
\]
For any fixed positive \(2a/r\), this does not tend to zero: the ratio of successive terms is \((K+2)(2a/r)\), eventually larger than two. The actual cutoff construction gives \(a^{K+1}\) without the extra factorial, leaving only \((2a/r)^{K+1}\). This explains why control of a growing finite derivative range is necessary.

### Exercise 8. Sum cell volumes rather than counting an infinite grid — 10 points

At a sufficiently large level \(j\), prove that the sum of the support volumes of all nonzero cells is at most \(12^n2^{jn}\).

**Solution.** A nonzero cell center has each coordinate at most \(9\cdot2^j/8+3\ell_j/4\) in absolute value. At spacing \(\ell_j\), there are at most \(8\,2^j/\ell_j\) possible centers per coordinate once \(\ell_j\leq2^j\). There are thus at most \((8\,2^j/\ell_j)^n\) nonzero cells. Each support lies in a cube of side \(3\ell_j/2\), of volume at most that side to the \(n\)-th power. Multiplication yields
\((8\,2^j/\ell_j)^n(3\ell_j/2)^n=12^n2^{jn}\).
The complete infinite lattice partition is used for its exact identity, but only finitely many of its cells meet this annulus.

### Exercise 9. Choose the parameter for a prescribed derivative budget — 10 points

Let \(B=N+1+b+n+1\). Give an explicit positive \(\varepsilon\) satisfying all three conditions in (5.1).

**Solution.** One valid choice is
\[
 \varepsilon=\frac12\min\left\{
 1,\ \frac{r}{260\sqrt n},\
 \frac{r}{4B\log2},\
 \frac{r\,2^{-B}}{130\sqrt n}
 \right\}. \tag{11.4}
\]
The second entry gives \(65\sqrt n\,\varepsilon\leq r/8<r/4\). The third gives
\(r/(4\varepsilon)\geq2B\log2>B\log2\).
The fourth gives
\(130\sqrt n\,\varepsilon/r\leq2^{-B-1}<2^{-B}\).
The first guarantees \(0<\varepsilon<1\). These are precisely the required top-term and correction-term inequalities. The initial frequency threshold is chosen afterward, with this fixed \(\varepsilon\) and fixed window radius \(m\).

### Exercise 10. Different partitions still give one smooth function — 16 points

For each derivative order \(b\), suppose the construction gives a \(C^b\) function \(f_b\) representing \(u\) on the same open ball, using a different partition. Prove that \(f_0\) is smooth. Explain why equality almost everywhere is enough to identify the representatives.

**Solution.** The difference \(f_b-f_0\) is continuous and represents the zero distribution. If its value were nonzero at a point, multiply by a fixed unit complex number so that its real part is positive there. By continuity, that real part is bounded below by a positive constant on a smaller ball. A nonnegative smooth test function supported in that smaller ball, with positive integral, would have nonzero pairing with the difference. This contradicts the zero distribution. Hence \(f_b=f_0\) everywhere on the ball.

Equivalently, equality as locally integrable distributions gives equality almost everywhere, and two continuous functions equal almost everywhere are equal everywhere by the same open-ball argument. Since \(f_b\in C^b\) for every integer \(b\), the common function \(f_0\) belongs to every \(C^b\), and is smooth. This justifies changing the finite partition with the derivative budget; it does not assert a single infinite-order derivative estimate on one partition.

## References

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Chapter XVI, Theorem 16.3.5, for the nonconvex singular-carrier statement.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Sections 1.4 and 7.3, for the surrounding partition and compact Fourier theory. The exact cutoffs and contour identity used here are proved in full below.
- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), for additional background on entire Fourier transforms and support. That reference uses a different \(2\pi\) convention; all formulas in this lesson use (7.1).
