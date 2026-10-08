# Nonconvex localization through logarithmic frequency cells

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

The Fourier transform can select a different compact convex carrier at each large frequency. Their closed union contains the singular support. Taking the convex hull of that union loses the frequency choice, and can fill regions where the distribution is smooth.

We prove this local statement by constructing the frequency cutoffs explicitly. Each cutoff has only a finite, increasing number of controlled derivatives. That is enough for a finite Taylor contour correction. No analytic compactly supported cutoff is required.

## 1. Profiles, carriers and the statement

Use \(D=-i\partial\) and

\[
 F(\zeta)=\widehat u(\zeta)=\langle u(x),e^{-ix\cdot\zeta}\rangle,
 \qquad
 L_u(z,c)=\frac{\log|F(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2. \tag{1.1}
\]

Here \(u\) is a compactly supported distribution. The logarithm is \(-\infty\) at a zero. A logarithmic profile is a proper plurisubharmonic local \(L^1\) limit along a sequence \(c\to\infty\), or the collapsed limit \(-\infty\). For a proper profile \(v\), write \(h_v\) for its indicator and \(C_v\) for the nonempty compact convex set with support function \(h_v\). The collapsed profile has empty carrier.

The exact profile and compactness results used here are proved in Joint logarithmic-frequency limits, Sections 2–4, Plurisubharmonic envelopes and support functions, and the complete compactness proof in Local compactness and Hartogs bounds. In particular, if \(N\geq0\) is an integer such that the ordinary compact Fourier estimate has order \(N\), then every proper profile satisfies

\[
 v(z)\leq N+h_v(\operatorname{Im}z),\qquad
 C_v\subset \operatorname{conv}\operatorname{supp}u. \tag{1.2}
\]

The compactness alternative also gives local uniform collapse to \(-\infty\), and Hartogs upper comparison of a proper limiting profile against a continuous ceiling. Those conclusions concern the canonical upper-semicontinuous representative.

Let \(\mathcal J_{\mathrm{pr}}(u)\) be the indicators of all proper profiles. Set

\[
 A(u)=\overline{\bigcup_{h\in\mathcal J_{\mathrm{pr}}(u)}C_h}.
 \tag{1.3}
\]

The union over an empty family is empty. Collapsed profiles add no points.

**Theorem 1.1.** For every compactly supported distribution,

\[
 \operatorname{sing\,supp}u\subset A(u). \tag{1.4}
\]

This is a containment in a closed union, not merely in its convex hull. The theorem does not assert that each individual \(C_h\) is contained in the singular support.

The proof occupies Sections 2–6. Its lower inputs are precisely the profile compactness and carrier statements above, compact distribution Fourier inversion, elementary finite convolution of measures, and the one-variable fundamental theorem of calculus. Fourier inversion, including the implication from rapid real Fourier decay to smoothness, is proved in Locating singularities through logarithmic Fourier strips, Section 2.

**Lemma 1.2 (the empty-profile case).** If there is no proper profile, then \(u\) is smooth.

*Proof.* If \(F\) were not rapidly decreasing on the real space, there would be a fixed \(B\geq0\) and an escaping sequence \(c_j\) with
\(|F(c_j)|\geq |c_j|^{-B}\), after increasing \(B\) to absorb a fixed constant. Thus \(L_u(0,c_j)\geq-B\). The compactness alternative supplies a further proper or collapsed subsequence. Uniform collapse on a fixed compact neighborhood of zero contradicts this last inequality. A proper subsequence contradicts the hypothesis. Hence \(F\) is rapidly decreasing. Every derivative of its inverse Fourier integral is then absolutely convergent, and Fourier inversion identifies the resulting smooth function with \(u\). \(\square\)

**Lemma 1.3 (translation).** Translating the spatial origin by \(x_0\) translates every profile carrier by \(-x_0\).

*Proof.* For \(u_0(x)=u(x+x_0)\), the transform is \(F_0(\zeta)=e^{ix_0\cdot\zeta}F(\zeta)\). Consequently,

\[
 L_{u_0}(z,c)=L_u(z,c)-x_0\cdot\operatorname{Im}z,\qquad
 h_{v_0}(\eta)=h_v(\eta)-x_0\cdot\eta,\qquad C_{v_0}=C_v-x_0.
 \tag{1.5}
\]

The first equality also holds at zeros. Adding a fixed pluriharmonic function preserves proper local \(L^1\) convergence and uniform collapse. Substitution into the indicator definition proves the second equality; support functions determine the third. The transformation is invertible, so it accounts for all profiles in both directions. \(\square\)

## 2. One profile controls each sufficiently large window

**Lemma 2.1 (uniform window choice).** Suppose there is a proper profile. For every fixed \(m>0\), all sufficiently large real \(c\), with \(R=|c|\), admit an \(h_c\in\mathcal J_{\mathrm{pr}}(u)\) such that

\[
 |F(c+\zeta)|\leq R^{N+1}\exp h_c(\operatorname{Im}\zeta)
 \quad\text{for every }|\zeta|\leq m\log R. \tag{2.1}
\]

The threshold may depend on \(m\). The exponent \(N+1\) is fixed. The chosen carrier may depend on \(c\).

*Proof.* If this failed, there would be escaping \(c_j\) such that for every proper indicator \(h\) some \(|z|\leq m\) satisfies

\[
 L_u(z,c_j)>N+1+h(\operatorname{Im}z). \tag{2.2}
\]

Choose a proper or collapsed subsequence by the profile compactness alternative. If its limit is proper, let \(h\) be that limit's indicator. By (1.2), the limit is at most the continuous function \(N+h(\operatorname{Im}z)\). Hartogs upper comparison on the compact ball \(|z|\leq m\), inside a slightly larger ball, gives
\(L_u(z,c_j)\leq N+\tfrac12+h(\operatorname{Im}z)\) there for all large \(j\). This contradicts (2.2).

If the subsequence collapses, choose any fixed proper indicator \(h_0\), which exists by hypothesis. It has a finite minimum on the compact imaginary ball. Uniform collapse makes (2.2) impossible with \(h=h_0\). Finally substitute \(\zeta=z\log R\) and use the positive homogeneity of \(h\). \(\square\)

**Lemma 2.2 (a different separating normal is allowed for every carrier).** Suppose \(0\) has distance at least \(r>0\) from every proper carrier. For each \(h\in\mathcal J_{\mathrm{pr}}(u)\) there is a unit vector \(\theta_h\in\mathbb R^n\) with

\[
 h(\theta_h)\leq-r. \tag{2.3}
\]

*Proof.* Choose a point \(a\) minimizing \(|a|\) on the nonempty compact convex carrier \(C_h\). Then \(|a|\geq r\). For every \(y\in C_h\), differentiating \(|a+t(y-a)|^2\) at \(t=0+\) gives \(a\cdot(y-a)\geq0\). With \(\theta_h=-a/|a|\), this says \(\theta_h\cdot y\leq-|a|\leq-r\). Take the supremum over \(y\). \(\square\)

## 3. Finite convolution makes the required cutoffs

We give the complete cutoff construction because its derivative order grows with the frequency. Bounds for each fixed derivative alone would not control the contour correction.

Let \(\beta\) be a nonnegative smooth probability density supported in \([-1,1]\). One explicit choice is a positive normalizing constant times
\(\exp(-1/(1-t^2))\) for \(|t|<1\), extended by zero. It is smooth across the endpoints: each interior derivative is the exponential times a rational function with only a finite-order pole at an endpoint, and the exponential tends to zero faster than every power of that pole. Its integral is finite and strictly positive.

For an integer \(q\geq1\) and a length \(\ell>0\), convolve \(q\) uniform probability densities on intervals of length \(\ell/(4q)\), and then convolve with the rescaled smooth probability density supported in \([-\ell/8,\ell/8]\). Call the resulting one-dimensional density \(\kappa_{\ell,q}^{(1)}\). Its support is in \([-\ell/4,\ell/4]\): the uniform factors contribute total half-width \(\ell/8\), and the final smooth factor contributes another \(\ell/8\). Let \(\kappa_{\ell,q}\) be the product of these densities in \(n\) coordinates.

**Lemma 3.1 (controlled derivatives without analyticity).** If \(0\leq b\leq1\) is any measurable function and
\(\tau=b*\kappa_{\ell,q}\), then \(\tau\) is smooth, \(0\leq\tau\leq1\), and for every multi-index with \(|\alpha|\leq q\),

\[
 \|\partial^\alpha\tau\|_\infty\leq(8q/\ell)^{|\alpha|}. \tag{3.1}
\]

*Proof.* All factors have total mass one. The derivative of a uniform density on an interval of length \(a\) is the difference of its endpoint point masses divided by \(a\), a signed measure of total variation \(2/a\). Here \(a=\ell/(4q)\), so that variation is \(8q/\ell\). In a given coordinate, put each of its \(\alpha_j\) derivatives on a different uniform factor. There are at least that many factors because \(\alpha_j\leq|\alpha|\leq q\). Across coordinates, the convolution product has signed total variation at most \((8q/\ell)^{|\alpha|}\). Convolving it with the remaining probability factors and with \(b\), whose supremum is at most one, proves (3.1). The final smooth compact factor makes all orders of derivatives continuous, regardless of whether (3.1) controls those higher orders. \(\square\)

**Lemma 3.2 (an exact grid partition).** Let \(B_\ell=[-\ell/2,\ell/2)^n\), and set

\[
 \tau_{\ell,q,k}(\xi)=
 (1_{B_\ell}*\kappa_{\ell,q})(\xi-\ell k),\qquad k\in\mathbb Z^n.
 \tag{3.2}
\]

These are nonnegative smooth functions bounded by one. They sum exactly to one, have supports in
\(\ell k+[-3\ell/4,3\ell/4]^n\), have overlap at most \(2^n\), and satisfy (3.1).

*Proof.* The half-open translates of \(B_\ell\) partition the real space. Convolve their sum with the probability density, using nonnegativity to interchange the sum and integral. The sum is one almost everywhere and, being locally a finite sum of continuous functions, everywhere. The support statement follows by adding the two support cubes. In each coordinate an interval of length \(3\ell/2\) can contain at most two lattice centers at spacing \(\ell\); hence at most \(2^n\) cutoffs can be nonzero at a point. Lemma 3.1 gives the derivative bounds. \(\square\)

We also need an exact dyadic partition whose transition derivatives are much smaller. Put \(q_j=2(j+3)\), and define

\[
 \chi_j=1_{[-2^j,2^j]^n}*\kappa_{2^{j-1},q_j},
 \quad
 \psi_0=\chi_0,\qquad \psi_j=\chi_j-\chi_{j-1}\quad(j\geq1).
 \tag{3.3}
\]

**Lemma 3.3 (telescoping annuli).** The \(\psi_j\) are nonnegative, sum to one, and are bounded by one. For \(j\geq1\),

\[
 \operatorname{supp}\psi_j
 \subset\{\xi:(7/16)2^j\leq|\xi|_\infty\leq(9/8)2^j\}. \tag{3.4}
\]

For \(1\leq|\alpha|\leq j+1\),

\[
 \|\partial^\alpha\psi_j\|_\infty
 \leq\bigl(128(j+3)/2^j\bigr)^{|\alpha|}. \tag{3.5}
\]

*Proof.* The density used in \(\chi_j\) has coordinate half-width \(2^{j-3}\). Thus \(\chi_j\) is one on the cube of radius \((7/8)2^j\), vanishes outside the cube of radius \((9/8)2^j\), and takes values in \([0,1]\). The entire support of \(\chi_{j-1}\), of radius \((9/16)2^j\), lies in the region where \(\chi_j=1\). This proves \(\chi_j\geq\chi_{j-1}\) and (3.4). The sum telescopes to \(\chi_J\), which is eventually one at every fixed point.

For the derivatives of \(\chi_j\), (3.1) gives \(16q_j/2^j\) as the derivative base. For \(\chi_{j-1}\), the base is \(32q_{j-1}/2^j\). Both have enough uniform factors to control derivatives of total order at most \(j+1\). Each base is at most \(64(j+3)/2^j\). Taking the difference adds at most a factor two; for positive integer order, absorb that factor into the base to obtain (3.5). \(\square\)

**Proposition 3.4 (logarithmic cells).** Fix \(0<\varepsilon<1\). For \(j\geq1\), set

\[
 \ell_j=j/\varepsilon,\quad c_{j,k}=\ell_jk,\quad
 \phi_{j,k}=\psi_j\,\tau_{\ell_j,q_j,k}. \tag{3.6}
\]

For all sufficiently large \(j\), each nonzero cell has center radius \(R_{j,k}=|c_{j,k}|\) satisfying

\[
 2^{j-2}\leq R_{j,k}\leq2\sqrt n\,2^j,\qquad
 |\xi-c_{j,k}|\leq(3/4)\sqrt n\,\ell_j
 \quad(\xi\in\operatorname{supp}\phi_{j,k}). \tag{3.7}
\]

The cells sum to \(\psi_j\). Their support volumes have sum at most \(12^n2^{jn}\). For every unit \(\theta\) and \(0\leq s\leq j+1\),

\[
 \|\partial_\theta^s\phi_{j,k}\|_\infty
 \leq a_\varepsilon^s,\qquad a_\varepsilon=65\sqrt n\,\varepsilon. \tag{3.8}
\]

*Proof.* Increase the initial \(j\) until
\((3/4)\sqrt n\,\ell_j\leq2^{j-3}\),
\(\ell_j\leq2^j\), and
\(128(j+3)/2^j\leq\varepsilon\).
Such a threshold exists because exponential growth dominates \(j\). A point in a nonzero cell satisfies (3.4), and its distance from the center is at most the quantity in (3.7). Hence the center norm is at least \((7/16)2^j-2^{j-3}\geq2^{j-2}\), and at most \((9/8)\sqrt n\,2^j+2^{j-3}\leq2\sqrt n\,2^j\).

For a nonzero cell each center coordinate has absolute value at most \((9/8)2^j+3\ell_j/4\). There are at most
\((8\,2^j/\ell_j)^n\) such centers, after enlarging the threshold as above. Each support has volume at most \((3\ell_j/2)^n\). Their product gives the stated volume sum.

Lemma 3.2 gives the sum identity. Its derivative base for the grid factor is
\(8q_j/\ell_j=16\varepsilon(j+3)/j\leq64\varepsilon\).
The annular factor has derivative base at most \(\varepsilon\) up to order \(j+1\). The multi-index Leibniz formula therefore bounds their product by \((65\varepsilon)^{|\alpha|}\), including order zero. Expand \(\partial_\theta^s\) by the multinomial formula and use
\(\sum|\theta_i|\leq\sqrt n\). This proves (3.8). \(\square\)

## 4. A finite Taylor contour identity

**Lemma 4.1 (directional correction with its sign).** Let \(\phi\) be a smooth compactly supported function, \(\theta\) a real unit vector, and \(K\geq0\) an integer. Define, for real \(t\),

\[
 \Phi(\xi,t)=\sum_{s=0}^{K}\frac{(it)^s}{s!}\partial_\theta^s\phi(\xi).
 \tag{4.1}
\]

Let \(G\) be entire on a neighborhood of the compact cylinder in question. Then

\[
 \begin{split}
 \int G(\xi)\phi(\xi)\,d\xi
 &=\int G(\xi+iT\theta)\Phi(\xi,T)\,d\xi\\
 &\quad+i\int_0^T\frac{(it)^K}{K!}
       \int G(\xi+it\theta)\partial_\theta^{K+1}\phi(\xi)\,d\xi\,dt .
 \end{split} \tag{4.2}
\]

Every integral in this identity has compact real \(\xi\)-support. If
\(\|\partial_\theta^s\phi\|_\infty\leq a^s\) through order \(K+1\), then

\[
 |\Phi(\xi,T)|\leq e^{aT},\qquad
 \left|\frac{(it)^K}{K!}\partial_\theta^{K+1}\phi(\xi)\right|
 \leq a^{K+1}t^K/K!
 \quad(t\geq0). \tag{4.3}
\]

*Proof.* The finite sum gives
\(\partial_t\Phi-i\partial_\theta\Phi
=-i(it)^K\partial_\theta^{K+1}\phi/K!\).
Holomorphy gives
\(\partial_tG(\xi+it\theta)=i\partial_\theta G(\xi+it\theta)\).
Differentiate the compact integral of \(G\Phi\), and integrate the total real directional derivative by parts. There is no boundary term because \(\Phi\) is compactly supported. The remaining derivative is
\(-i(it)^K\int G\partial_\theta^{K+1}\phi/K!\).
Integrating from zero to \(T\) and rearranging proves the plus sign in (4.2). Summing the exponential series and bounding the last derivative prove (4.3). \(\square\)

**Lemma 4.2 (the factorial cancels).** For \(r>0\) and integer \(K\geq0\),

\[
 \int_0^\infty e^{-rt/2}\frac{t^K}{K!}\,dt
 =(2/r)^{K+1}. \tag{4.4}
\]

*Proof.* Substitute \(s=rt/2\). Integration by parts gives
\(\int_0^\infty e^{-s}s^K\,ds=K!\), starting from \(K=0\). The endpoint terms vanish by exponential decay. \(\square\)

## 5. Summing the shifted cells

Assume now that proper profiles exist, and that \(0\) has distance at least \(r>0\) from all their carriers. Fix a derivative budget \(b\geq0\), an integer. We will produce a \(C^b\) representative on \(|x|<r/2\).

Choose \(0<\varepsilon<1\) so small that, with \(a_\varepsilon=65\sqrt n\,\varepsilon\),

\[
 a_\varepsilon\leq r/4,\quad
 \frac{r}{4\varepsilon}>(N+1+b+n+1)\log2,\quad
 \frac{2a_\varepsilon}{r}<2^{-(N+1+b+n+1)}. \tag{5.1}
\]

All three conditions are possible simultaneously by decreasing \(\varepsilon\).
Use the cells from Proposition 3.4, and choose

\[
 T_j=j/\varepsilon,\qquad
 m\geq \frac{2(1+3\sqrt n/4)}{\varepsilon\log2}. \tag{5.2}
\]

Increase the initial \(J\) until \(j\geq4\), the conclusions of Proposition 3.4 hold, and every center exceeds the threshold in Lemma 2.1 for this fixed \(m\).

For each nonzero cell choose \(h_{j,k}\) by Lemma 2.1, and its normal \(\theta_{j,k}\) by Lemma 2.2. On the real support of that cell, for \(0\leq t\leq T_j\),

\[
 |\xi-c_{j,k}+it\theta_{j,k}|
 \leq(1+3\sqrt n/4)j/\varepsilon
 \leq m\log R_{j,k}. \tag{5.3}
\]

Indeed, \(\log R_{j,k}\geq(j-2)\log2\geq j\log2/2\). The complex-window bound therefore applies everywhere needed, with a single fixed \(m\).

For \(|x|\leq r/2\), positive homogeneity and separation give

\[
 |e^{ix\cdot(\xi+it\theta_{j,k})}F(\xi+it\theta_{j,k})|
 \leq R_{j,k}^{N+1}
       e^{t(h_{j,k}(\theta_{j,k})-x\cdot\theta_{j,k})}
 \leq R_{j,k}^{N+1}e^{-rt/2}. \tag{5.4}
\]

Define each smooth cell contribution by

\[
 u_{j,k}(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}F(\xi)\phi_{j,k}(\xi)\,d\xi.
 \tag{5.5}
\]

**Proposition 5.1 (uniform all-cell derivative estimate).** For every multi-index \(|\gamma|\leq b\) and all sufficiently large \(j\),

\[
 \begin{split}
 \sum_k|\partial_x^\gamma u_{j,k}(x)|
 \leq C_{n,N,b,\varepsilon}\,2^{j(N+1+b+n)}
 \left(e^{-rj/(4\varepsilon)}
       (2a_\varepsilon/r)^{j+1}\right),
 \quad |x|\leq r/2 .
 \end{split} \tag{5.6}
\]

*Proof.* Apply Lemma 4.1 to each cell with
\(K=j\), \(T=T_j\), \(\theta=\theta_{j,k}\), and the entire function
\[
 G_\gamma(\zeta)=(i\zeta)^\gamma e^{ix\cdot\zeta}F(\zeta).
 \tag{5.7}
\]
This corresponds exactly to differentiating (5.5). For large \(j\), the cell radius and \(T_j\) are at most \(R_{j,k}\) together, so \(|\zeta|\leq2R_{j,k}\). Equation (5.4) bounds \(G_\gamma\) by
\(2^{|\gamma|}R_{j,k}^{N+1+|\gamma|}e^{-rt/2}\).

The top integral in (4.2) is bounded by that power of \(R_{j,k}\), the cell volume, and
\[
 e^{-rT_j/2}e^{a_\varepsilon T_j}
 \leq e^{-rT_j/4}=e^{-rj/(4\varepsilon)}. \tag{5.8}
\]
For the correction integral, (3.8), (4.3), and (4.4) give the same power and volume times
\[
 a_\varepsilon^{j+1}
 \int_0^\infty e^{-rt/2}t^j/j!\,dt
 =(2a_\varepsilon/r)^{j+1}. \tag{5.9}
\]
The Taylor factor has been integrated exactly; no uncontrolled factorial remains.

Finally use \(R_{j,k}\leq2\sqrt n\,2^j\) and the sum of support volumes at most \(12^n2^{jn}\). Absorb the fixed constants and increase the radius power to \(N+1+b\). This proves (5.6). \(\square\)

The two inequalities in (5.1) make the right side of (5.6) at most a fixed constant times \(2^{-j}\). Hence the cell series, and every derivative through order \(b\), converge absolutely and uniformly on the closed ball \(|x|\leq r/2\).

## 6. Recovering the distribution and proving smoothness

**Lemma 6.1 (the series equals the original distribution).** For the fixed \(\varepsilon\) and \(J\) above,

\[
 u=u_{\mathrm{low}}+\sum_{j\geq J}\sum_k u_{j,k}
 \quad\text{in distributions},\qquad
 u_{\mathrm{low}}=\mathcal F^{-1}(F\chi_{J-1}). \tag{6.1}
\]

The low term is smooth.

*Proof.* The grid identity and telescoping annular identity give
\(\chi_{J-1}+\sum_{j\geq J,k}\phi_{j,k}=1\).
All summands are nonnegative and at most one. The low multiplier \(F\chi_{J-1}\) is smooth with compact frequency support, so every derivative of its inverse Fourier integral is absolutely convergent.

For a compactly supported smooth test function \(g\), its Fourier transform decreases faster than every real power. The ordinary compact-distribution estimate bounds \(F\) by \(C(1+|\xi|)^N\). Thus
\[
 \int |F(\xi)\widehat g(-\xi)|
       \left(\chi_{J-1}(\xi)+\sum_{j\geq J,k}\phi_{j,k}(\xi)\right)d\xi
 <\infty. \tag{6.2}
\]
Absolute integrability permits the sum and integral to be interchanged. Pairing the inverse Fourier integrals with \(g\) now gives exactly the Fourier inversion pairing for \(u\). This proves (6.1), including its normalization and the sign in \(\widehat g(-\xi)\). \(\square\)

**Proposition 6.2.** Under the separation assumption, \(u\) is smooth on \(|x|<r/2\).

*Proof.* For each fixed budget \(b\), the uniformly convergent derivative series in Section 5, together with the smooth low term, gives a \(C^b\) function on the ball. The elementary termwise differentiation theorem applies because the functions and all derivatives through order \(b\) converge uniformly; it can be proved successively by integrating each uniformly convergent first derivative along line segments inside the ball. Lemma 6.1 identifies this function with \(u\) as a distribution there.

The construction is allowed to choose a different \(\varepsilon\), partition, and low term for a different \(b\). The resulting continuous functions nevertheless coincide: a continuous function representing the zero distribution is zero, since a nonzero value persists with one real or imaginary sign on a small ball and is detected by a nonnegative smooth test function. The representative obtained for \(b=0\) therefore belongs to \(C^b\) for every \(b\). It is smooth. \(\square\)

*Proof of Theorem 1.1.* If no proper profile exists, Lemma 1.2 proves the theorem with empty singular support. Otherwise, choose \(x_0\notin A(u)\). Since \(A(u)\) is closed, there is \(r>0\) such that \(x_0\) has distance at least \(r\) from every proper carrier. Translate \(x_0\) to zero using Lemma 1.3 and apply Proposition 6.2. The distribution is smooth on a neighborhood of \(x_0\), so \(x_0\notin\operatorname{sing\,supp}u\). This proves (1.4). \(\square\)

The proof keeps three choices separate. The window radius \(m\) is fixed after the derivative budget and \(\varepsilon\) are chosen. Its profile and separating direction may vary from cell to cell. The large-frequency threshold then absorbs all finite exceptions into the smooth low term. None of these choices asks for one common normal for every carrier, or one cutoff controlling infinitely many derivatives.

## References

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Chapter XVI, Theorem 16.3.5. The present proof constructs its logarithmic partition directly by finite convolutions and uses a directional finite Taylor identity.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Sections 1.4 and 7.3. These give background on partitions and compact-distribution Fourier growth. The required partition is fully proved above; compact Fourier inversion is proved in the linked course lesson.
- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/). Named background on entire Fourier transforms and support. No result from this background reading is substituted for the local proof.
