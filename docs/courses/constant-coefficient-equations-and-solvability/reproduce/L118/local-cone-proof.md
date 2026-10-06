# Local tangent cones and small imaginary deformations

AN-02 specialized working foundation LC035, October 2026. Written by GPT-6.1 Sol (OpenAI), Ultra reasoning. This is an independently written proof for the homogeneous polynomial receivers C6–C8 and AH3–AH4. Self-checked by the writing AI. The general real analytic and microhyperbolic AN-01 assignment remains with its existing owner.

## Exact scope and mathematical inputs

Let \(F\in\mathbb R[z_1,\ldots,z_n]\) be nonzero, homogeneous of degree \(m\ge1\), and hyperbolic in the real direction \(N\ne0\): \(F(N)\ne0\), and for every real \(w\), every root of \(s\mapsto F(w+sN)\) is real. A nonzero complex scalar multiple of such an \(F\) has exactly the same nonzero sets, tangent components, and estimates after multiplying the constants by the scalar's modulus. Thus the real normalization from D1 is sufficient; no reality assumption is imposed on the lower terms of a different full polynomial \(P\).

For real \(\xi\ne0\), let
\[
 \mu_\xi=\min\{|\alpha|:\partial^\alpha F(\xi)\ne0\},\qquad
 H_\xi(h)=\sum_{|\alpha|=\mu_\xi}\frac{\partial^\alpha F(\xi)}{\alpha!}h^\alpha.
 \tag{LC1}
\]
Write
\[
 \Gamma_\xi=\Gamma(H_\xi,N),\qquad
 C_\xi=\{x\in\mathbb R^n:x\cdot v\ge0\text{ for every }v\in\Gamma_\xi\}.
 \tag{LC2}
\]
For \(\mu_\xi=0\), the conventions are \(H_\xi=F(\xi)\ne0\), \(\Gamma_\xi=\mathbb R^n\), and \(C_\xi=\{0\}\). The positive polar uses \(\ge0\), including zero; it is not the negative polar.

The written C1 input supplies the following facts from D1. The line multiplicity of \(F(\xi+sN)\) at zero equals \(\mu_\xi\), so \(H_\xi(N)\ne0\); \(H_\xi\) is hyperbolic in \(N\); its component \(\Gamma_\xi\) is an open convex cone, and \(\Gamma(F,N)\subset\Gamma_\xi\). Here is the actual localization step, to fix its quantifiers. Taylor expansion gives coefficient convergence
\[
 \delta^{-\mu_\xi}F\bigl(\xi+\delta(h+sN)\bigr)\longrightarrow H_\xi(h+sN),\quad\delta\downarrow0,
 \tag{LC3}
\]
for each real \(h\), locally uniformly in complex \(s\). Every approximant has only real \(s\)-roots; its limit has nonzero leading coefficient \(H_\xi(N)\). A nonreal limit root would have a small disk disjoint from the real axis, with a zero-free boundary; Rouché would put a root of an approximant in that disk. Thus the limit is hyperbolic. Equality of the two multiplicities in this input uses D1's multivariable vanishing theorem, exactly as C1 does. We do not label that inherited D1 theorem or its recursive prerequisites newly proved here. Polynomial Taylor expansion, one-variable Rouché/Hurwitz and the maximum principle are D4's other inputs.

The new results below are the complete specialized D7 contract. They do not assert an analytic wavefront theorem, any boundary-value operation theorem, component constancy of null homology, rational-form completeness, projective tube injectivity, orientation comparison, or recursive closure of the course.

## LC035-1. A compact cone with an angular margin

Suppose \(\mu_{\xi_0}>0\), and \(K\subset\Gamma_{\xi_0}\) is compact. There is an open convex cone \(G\) containing \(N\) and \(K\), such that
\[
 L=\overline G\cap S^{n-1}\subset\Gamma_{\xi_0}
 \tag{LC4}
\]
is compact. Moreover a real linear functional \(\ell\) and \(b>0\) can be chosen with \(\ell(\theta)\ge b\) for every \(\theta\in L\).

**Proof.** At positive degree zero is outside \(\Gamma_{\xi_0}\), so compactness gives \(\inf_{v\in K}|v|>0\). Normalize the elements of \(K\cup\{N\}\) and call the resulting compact subset of the cone \(A\). Its convex hull \(B\) is compact and contained in the cone. Compactness follows, for example, because every convex combination can be reduced to at most (n+1) terms: if more are present their augmented vectors \((a,1)\in\mathbb R^{n+1}\) are linearly dependent; vary their coefficients along a dependence until one coefficient is zero, and repeat. Thus \(B\) is the image of a compact product of \(A^{n+1}\) and a simplex. Convexity of the cone puts every such combination in it, hence \(0\notin B\).

Choose \(\rho>0\) so small that \(B+\overline B(0,\rho)\) is inside the open cone and misses zero. This is possible because \(B\) is compact. Let \(G\) be the positive conical hull of \(B+B(0,\rho)\). It is open and convex. To verify convexity, combine two positive multiples of elements of this convex set by factoring the sum of their positive coefficients. Its unit section closure consists of directions of the compact set \(B+\overline B(0,\rho)\). That set stays away from zero and lies in \(\Gamma_{\xi_0}\), proving (LC4).

Let \(p\in B\) minimize \(\lvert p\rvert\). Differentiating \(|p+t(a-p)|^2\) at \(t=0^+\) gives \(p\cdot a\ge|p|^2\) for every \(a\in B\). Reduce \(\rho\) below \(|p|/2\). The functional \(\ell(v)=p\cdot v\) is strictly positive on \(B+\overline B(0,\rho)\). Dividing by the bounded lengths there proves the uniform bound on \(L\). In particular normalized segments from any \(\theta\in L\) to \(N/|N|\) are defined and stay in \(L\); opposite vectors cannot occur. This also proves path connectedness of \(L\). ∎

The same construction works for any compact unit directions already inside the tangent component, and for a small closed ball of permitted values about a fixed vector. It does not require the whole hyperbolicity cone to have a compact affine slice.

## LC035-2. The local imaginary tube and its exact power

Fix \(\xi_0\ne0\) and first suppose \(\mu=\mu_{\xi_0}>0\). Let (G,L) satisfy (LC4) and contain \(N\). There are \(d,r,c>0\) such that
\[
 \boxed{\ |F(w\pm i y)|\ge c|y|^\mu>0\ }
 \quad
 \bigl(|w-\xi_0|<d,\ y\in\overline G\setminus\{0\},\ |y|\le r/2\bigr).
 \tag{LC5}
\]
The exponent is the order at the center \(\xi_0\), not an asserted constant order at neighboring real points. All real \(w\) in the ball are allowed, whether characteristic or not.

**Proof: uniform root count.** For \(\theta\in L\), Taylor expansion and homogeneity of \(H_{\xi_0}\) give
\[
 F(\xi_0+i z\theta)=(iz)^\mu H_{\xi_0}(\theta)+O(|z|^{\mu+1}),
 \tag{LC6}
\]
uniformly for bounded complex \(z\). Indeed this is a finite polynomial expansion with coefficients continuous in the compact parameter \(\theta\). Set \(h_0=\min_L|H_{\xi_0}(\theta)|>0\). Choose \(r>0\) so small that division by \(z^\mu\) in (LC6) leaves modulus at least \(h_0/2\) on \(0<|z|\le2r\). The zero at zero has multiplicity exactly \(\mu\), and no other zero occurs in that disk, uniformly in \(\theta\).

Consider the polynomials
\[
 f_{w,t,\theta}(z)=F(w+itN+iz\theta),\qquad w,t\text{ real}.
 \tag{LC7}
\]
Choose \(d,T>0\) sufficiently small. Uniform coefficient continuity and the lower bound on the circles \(|z|=r/4\) and \(|z|=r\) ensure, by Rouché, that for \(|w-\xi_0|<d\), \(|t|<T\), and \(\theta\in L\), there are exactly \(\mu\) roots in \(|z|<r\), all actually in \(|z|<r/4\). They include their multiplicities. There is also a common lower bound \(b_0>0\) for \(|f_{w,t,\theta}|\) on \(|z|=r\). Reducing (d,T) strictly from closed parameter bounds makes these conclusions valid throughout the stated open ranges. Changes in the polynomial's global degree do not affect this bounded root count.

**Proof: the root halfplane and its sign.** If \(t\ne0\), no root of (LC7) can lie on the imaginary axis: for \(z=iu\), the argument is the real point \(w-u\theta\) plus (itN); homogeneous hyperbolicity in \(N\) makes \(F(w-u\theta+itN)\ne0\). In the connected parameter set
\[
 B(\xi_0,d)\times(-T,0)\times L,
 \tag{LC8}
\]
the number of the \(\mu\) small roots in each open halfplane is constant. Here continuity means the unordered multiset, not continuously labelled individual roots: small disjoint circles around distinct roots have fixed root counts under small coefficient perturbations, by Rouché; their radii can be made arbitrarily small. The disk boundary and the imaginary axis are zero-free, so a change of halfplane count is impossible. This gives locally constant counts, and connectedness makes them constant.

At \(\theta=N/|N|\), every root of
\(F(w+i(t+z/|N|)N)\) has \(i(t+z/|N|)\in\mathbb R\), whence
\[
 \operatorname{Re}z=-t|N|>0\quad(t<0).
 \tag{LC9}
\]
Thus all small roots in (LC8) have strictly positive real part. Letting \(t\uparrow0\) and using multiset continuity shows that all small roots of \(f_{w,0,\theta}\) have nonnegative real part. For completeness, the positive-\(t\) argument gives strictly negative real parts, so at \(t=0\) they are on the imaginary axis. The latter observation proves that all small roots of \(u\mapsto F(w+u\theta)\) are real; the lower bound only needs the nonnegative-halfplane conclusion. No differentiability or global labelling of roots is used.

**Proof: the denominator lower bound.** List the \(\mu\) small roots as \(z_1,\ldots,z_\mu\), repeated by multiplicity, and divide
\[
 q(z)=f_{w,0,\theta}(z)\Big/\prod_{j=1}^{\mu}(z-z_j).
 \tag{LC10}
\]
Polynomial division, with removal of the exactly counted roots, makes (q) holomorphic and zero-free on \(|z|\le r\). On its boundary each \(|z-z_j|\le5r/4\), so
\[
 |q(z)|\ge b_0(5r/4)^{-\mu}\quad(|z|=r).
\]
The maximum principle for (1/q) extends this bound to the disk. If \(-r/2\le a<0\), the root halfplane gives \(|a-z_j|\ge|a|\). Consequently
\[
 |F(w+ia\theta)|\ge b_0(5r/4)^{-\mu}|a|^\mu.
 \tag{LC11}
\]
For \(y=|y|\theta\in\overline G\setminus\{0\}\), take \(a=-|y|\); this proves the minus sign in (LC5), including the closed angular section. Real coefficients give \(F(w+iy)=\overline{F(w-iy)}\), proving the plus sign with identical constants. Neither sign permits \(y=0\) as a zero-free characteristic point. ∎

**Degree zero.** If \(F(\xi_0)\ne0\), continuity in a complex neighborhood instead gives
\[
 |F(w\pm iy)|\ge c_0>0\quad(|w-\xi_0|<d_0,\ |y|<r_0),
 \tag{LC12}
\]
with no cone or sign restriction, and \(y=0\) allowed. This is the correct exponent-zero assertion. In particular permitted field values may vanish there.

For a nonzero complex scalar normalization \(\widetilde F=aF\), (LC5)–(LC12) hold after multiplying lower-bound constants by \(|a|\). Conjugation need only be applied to \(F\); equality of the moduli for the two signs follows for \(\widetilde F\) as well.

## LC035-3. Persistence of fixed vectors and compact sets

For every \(v\in\Gamma_{\xi_0}\) there is a neighborhood (U) of \(\xi_0\) such that \(v\in\Gamma_w\) for all real \(w\in U\). More strongly, for every compact \(K\subset\Gamma_{\xi_0}\) one (U) works for all \(v\in K\), and the set
\[
 \mathcal A=\{(\xi,v):\xi\ne0,\ v\in\Gamma_\xi\}
 \tag{LC13}
\]
is open in \((\mathbb R^n\setminus\{0\})\times\mathbb R^n\).

**Proof.** Degree zero has a real nonzero neighborhood, so every neighboring tangent degree is zero and all vectors remain permitted. At positive degree choose \(G\) for \(K\cup\{N\}\) by LC035-1 and use LC035-2. Fix \(w\in B(\xi_0,d/2)\) and write \(\nu=\mu_w\). Polynomial Taylor expansion at this new real point gives
\[
 g_\delta(z)=\delta^{-\nu}F(w+\delta z)\longrightarrow H_w(z)
 \tag{LC14}
\]
locally uniformly for all complex \(z\). Every \(g_\delta\) is eventually zero-free on each compact subset of the connected open tube \(D=\mathbb R^n-iG\): the real displacement \(\delta\operatorname{Re}z\) stays in \(B(\xi_0,d)\), and \(0<\delta|\operatorname{Im}z|\le r/2\), so (LC5) applies. Each compact set stays a positive distance from \(\operatorname{Im}z=0\), since its imaginary directions lie in the open cone \(G\) of positive degree.

Here is the needed several-variable limiting argument proved from one-variable Hurwitz. Suppose \(H_w(z_*)=0\) at some \(z_*\in D\). If \(H_w\) is not identically zero in a neighborhood of \(z_*\), choose a direction \(a\in\mathbb C^n\) on which its first nonzero Taylor homogeneous term is nonzero. On a small line disk \(z_*+sa\subset D\), \(H_w\) is not identically zero and has a zero at \(s=0\). But the functions \(g_\delta(z_*+sa)\) are eventually zero-free on a slightly larger closed disk and converge uniformly; one-variable Hurwitz forbids that limit zero. Thus \(H_w\) would have to vanish on a neighborhood. A polynomial vanishing on a complex open set is identically zero, contradicting its definition (also \(H_w(-iN)=(-i)^\nu H_w(N)\ne0\) by C1). Therefore \(H_w\) is zero-free on (D).

For \(v\in G\), (LC14) now yields \(H_w(-iv)\ne0\), and homogeneity gives \(H_w(v)\ne0\). Because \(G\) is connected and contains \(N\), every such \(v\) belongs to the component of \(\{H_w\ne0\}\) containing \(N\). Hence \(G\subset\Gamma_w\), which proves simultaneous persistence of \(K\). This proof treats changing values of \(\nu\) explicitly; it never assumes continuity of normalized tangent-polynomial coefficients.

Finally choose a closed value ball about any \(v\in\Gamma_{\xi_0}\) wholly inside that open component. Compact-set persistence puts this whole ball inside every neighboring \(\Gamma_w\). A smaller open ball and real neighborhood then give a product neighborhood contained in \(\mathcal A\), proving (LC13). At degree zero this works for balls centered at zero too. ∎

## LC035-4. Closed positive polar graph and the union of fibers

The graph
\[
 \mathcal C=\{(\xi,x):\xi\ne0,\ x\in C_\xi\}
 \tag{LC15}
\]
is closed relative to \((\mathbb R^n\setminus\{0\})\times\mathbb R^n\).

**Proof.** Let \(\xi_j\to\xi\ne0\), \(x_j\to x\), and \(x_j\in C_{\xi_j}\). For each fixed \(v\in\Gamma_\xi\), LC035-3 puts \(v\in\Gamma_{\xi_j}\) eventually. Thus \(x_j\cdot v\ge0\) eventually, and the limit gives \(x\cdot v\ge0\). This holds for every permitted \(v\), so \(x\in C_\xi\). There is no uniform index required for all \(v\). At degree zero testing both \(v\) and (-v) yields \(x=0\), exactly the convention in (LC2). ∎

For any nonzero real \(a\), homogeneity and the finite Taylor formula give
\[
 \mu_{a\xi}=\mu_\xi,\qquad H_{a\xi}(h)=a^{m-\mu_\xi}H_\xi(h).
 \tag{LC16}
\]
Multiplication by this nonzero scalar leaves the component containing \(N\) and its polar unchanged. In particular \(\Gamma_{-\xi}=\Gamma_\xi\) and \(C_{-\xi}=C_\xi\). Since each \(C_\xi\) is a cone, \(W_F=\bigcup_{\xi\ne0}C_\xi\) is a cone. It is closed: for \(x_j\in W_F\) converging to (x), choose unit witnessing frequencies by (LC16), extract a convergent subsequence on the sphere, and apply (LC15). The limit frequency stays nonzero. This is exactly C6's closed-union argument. Convexity of \(W_F\) is neither needed nor asserted.

## LC035-5. Uniform bounds for compact permitted field values

Let \(Q\subset\mathcal A\) be compact. There are \(\varepsilon_0,c>0\) and an integer \(0\le M\le m\) such that
\[
 \boxed{\ |F(\xi\pm i\varepsilon v)|\ge c\varepsilon^M>0\ }
 \quad ((\xi,v)\in Q,\ 0<\varepsilon\le\varepsilon_0).
 \tag{LC17}
\]
Consequently \(1/|F(\xi\pm i\varepsilon v)|\le c^{-1}\varepsilon^{-M}\). One may always use exponent (m) after reducing \(\varepsilon_0\le1\). A sharp or optimal exponent is not claimed.

**Proof with all compact quantifiers.** At a pair \((\xi_0,v_0)\in Q\) with positive tangent degree, choose a closed value ball \(B_v\) centered at \(v_0\), contained in \(\Gamma_{\xi_0}\), and small enough that \(|v|\ge a_0>0\) there. Choose \(G\) containing that ball and \(N\). LC035-2 gives a real neighborhood, \(c_0,r_0>0\), and exponent \(\mu_{\xi_0}\). For pairs in that neighborhood times \(B_v\), and \(\varepsilon\sup_{B_v}|v|\le r_0/2\),
\[
 |F(\xi\pm i\varepsilon v)|\ge c_0a_0^{\mu_{\xi_0}}\varepsilon^{\mu_{\xi_0}}.
 \tag{LC18}
\]
At a degree-zero pair use (LC12) and a bounded value ball; no positive norm minimum is needed, so \(v_0=0\) is covered. These open pair neighborhoods cover \(Q\). A finite subcover gives finitely many constants and exponents. Take \(\varepsilon_0\le1\) below every local upper bound, (c) below every positive coefficient in (LC18) and every degree-zero bound, and \(M\) the maximum of the finitely many exponents. Since \(\varepsilon^{\mu_j}\ge\varepsilon^M\) for \(0<\varepsilon\le1\), (LC17) follows. Every \(\mu_j\le m\). If every chosen neighborhood is noncharacteristic, \(M=0\) works. ∎

In particular if \(B\subset\mathbb R^n\setminus\{0\}\) is compact and \(V:B\to\mathbb R^n\) is continuous with \(V(\xi)\in\Gamma_\xi\), its graph is such a \(Q\). Thus the sphere deformations in C7 equation (73), and AH3's full-sphere smooth extension, avoid \(F=0\) for both signs with one power lower bound. Smoothness or analyticity of (V) is not needed for zero exclusion. For a family \(V_s\), the same conclusion holds whenever its combined value graph is compact and permitted, for example a jointly continuous family with \(s\) in a compact parameter space. A merely bounded family with no compact permitted graph or angular margin is insufficient.

## LC035-6. The exact field adapters used in C7–C8 and AH3

If \(x\notin W_F\cup(-W_F)\), every positive-degree cone \(\Gamma_\xi\) contains vectors of both signs under \(v\mapsto x\cdot v\): failure of either sign puts (x) or (-x) in its positive polar. Convex interpolation of two opposite-sign cone values produces a value in \(\Gamma_\xi\cap x^\perp\). It is nonzero because zero is outside a positive-degree component. At degree zero zero is allowed. LC035-3 keeps each selected value valid on a neighborhood of its frequency. Equation (LC16) permits the same value near the antipodal frequency. A finite even partition of unity on the sphere then gives a smooth even field with \(x\cdot V=0\); convexity keeps every value in its local cone. This is the precise open-cone input in C7 equation (72).

There is a uniform approximation margin for this field. Its compact graph lies in the open set (LC13). A finite product-neighborhood cover gives \(\eta>0\) such that every field \(\widetilde V\) satisfying \(\sup|\widetilde V-V|<\eta\) remains permitted. This is not inferred from continuity of the tangent polynomials. The even real analytic approximation described in C7 preserves the linear constraint \(x\cdot V=0\) under extension and Gaussian convolution, and the margin just proved preserves cone membership. LC035-5 gives the same required nonzero deformation conclusion for the resulting field.

For AH3, let a smooth allowed even field \(\Theta\) be given on the equator \(K_x=S^{n-1}\cap x^\perp\), \(x\ne0\). Near this equator put
\[
 p(\xi)=\frac{\xi-(x\cdot\xi)x/|x|^2}{|\xi-(x\cdot\xi)x/|x|^2|},\qquad E(\xi)=\Theta(p(\xi)).
 \tag{LC19}
\]
The denominator is nonzero in a neighborhood of the equator; \(p\) and (E) are smooth, \(p(-\xi)=-p(\xi)\), and (E) is even. Compactness and (LC13) give a whole uniform equatorial neighborhood where \((\xi,E(\xi))\) is permitted: otherwise forbidden pairs approaching the equator would contradict openness and continuity. Choose a smooth even cutoff \(\chi\), equal to one near the equator and supported in that neighborhood, and define
\[
 V(\xi)=\chi(\xi)E(\xi)+(1-\chi(\xi))N.
 \tag{LC20}
\]
Extend \(\chi E\) by zero outside its support. Since \(N\in\Gamma_\xi\) and each cone is convex, (V) is a global smooth allowed even field restricting to \(\Theta\). Its compact graph and (LC17) give precisely AH3's nonvanishing full-sphere map. This establishes the missing polynomial cone and exclusion input in AH3; the logarithm and periods of AH4 remain the calculation, not a new conclusion about all other foundations.

LC035-2 also gives the local tube required for C7 equations (74)–(75). At a characteristic center, choose a compact smaller cone containing \(N\), nearby field values, and finitely many other permitted testing directions, then thicken it by LC035-1. Its positive functional supplies the norm estimate when imaginary directions are added. Specifically if \(y\) and \(V\) lie in such a fixed smaller angular cone and \(|V|\ge a>0\), then \(\ell(y+\varepsilon V)\ge b(|y|+\varepsilon a)\) while \(|\ell(z)|\le\|\ell\||z|\). Small errors relative to \(|y|+\varepsilon\) preserve that lower bound and the larger cone's angular margin. For the local holomorphic field extension the imaginary-direction error is \(O(\varepsilon|y|)\), so it is such a relative error after shrinking \(|y|,\varepsilon\). The real displacement is also \(O(\varepsilon|y|)\) and stays in the local real ball. Therefore (LC5) bounds its reciprocal by \(C(|y|+\varepsilon)^{-\mu}\) with the required fixed exponent. Degree-zero centers use (LC12). This proves the polynomial estimate in that receiver; the distributional boundary limit, fixed-wavefront topology, multiplication and restriction still use C7's declared D5–D6 interfaces.

## Exact examples, illustrations and learner checks

The companion lesson supplies three computed examples and six exercises with full solutions. The two reproducible figures depict exact tangent-component slices and an exact imaginary-deformation calculation; finite plots are explanatory checks and are not used as proofs of (LC5), (LC14) or (LC17).

## Human credit and retained proof obligations

[Michael F. Atiyah, Raoul Bott and Lars Gårding, *Lacunas for hyperbolic differential operators with constant coefficients I* (1970)](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02394570), Lemma 5.1, Lemma 5.9 and Corollary 5.11, treat local roots and local-cone semicontinuity, including perturbations of the polynomial. This proof keeps \(F\) fixed and uses a root halfplane, a zero-free quotient and an explicitly proved Hurwitz rescaling argument. Their broader coefficient-perturbation statement is not used.

Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Lemma 8.7.4, printed 320–321/PDF 328–329 and the graph portion of Theorem 8.7.5, printed 321/PDF 329, were checked privately for statement and completeness scope. No scanned text, paywalled prose, or named theorem is required to fill a step of LC035-1 through LC035-6. The elementary D4 results and the existing C1/D1 tangent-hyperbolicity input are explicitly retained. This work neither supplies nor transfers the general analytic microhyperbolic theorem, analytic wavefront boundary theorem, or operation bridges owned by AN-01.

CD034's admitted smooth-cycle detection is a separate input and does not imply these statements. Nothing here closes the whole AN-02 goal.
