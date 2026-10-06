# Fourier traces on curved energy surfaces

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0. The linked coordinate supplement retains CC BY-SA 4.0.*


**Working question: Does the shell need curvature, or only a graph?** Compare the flat transport shell with the graph \(\xi_1=|\xi_2|^{3/2}\). The latter has unbounded second derivative at zero, but its first derivative is continuous. The slice argument uses the graph structure, whereas a curvature argument would ask for data that are not available. The large-ball observation detects the amplitude after the local trace has been constructed.

A regular energy surface need not have nonzero curvature. The endpoint Fourier trace depends on a different geometric fact: a surface is locally a graph, so its inverse Fourier transform has uniformly bounded square-integrable slices. A large-ball mass calculation then detects every nonzero surface amplitude and proves that the trace is onto.

We use the spaces, slice estimates and Banach-space onto criterion from [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md). Read [Coordinate inverses, integration and surface measure](../providers/analysis/coordinate-inverses-and-integration.md) first: (CI1)–(CI3) prove the required graph coordinates, (CI4) proves the measurable change-of-variables formula, and (CI6)–(CI7) prove the chart-independent surface and energy measures. Its last section constructs the finite partitions used below. The [Fourier inversion, Gaussian and Plancherel proofs](../providers/analysis/finite-derivative-l2.md#fourier-normalization), [tempered Fourier duality](../providers/analysis/finite-derivative-l2.md#tempered-fourier-duality), [product integration](../providers/analysis/finite-derivative-l2.md#general-tonelli-fubini) and [mollification and density](../providers/analysis/euclidean-approximation-and-convolution.md#mollification) supply the remaining analytic prerequisites. The [real-power and cutoff proofs](../providers/analysis/elementary-functions-and-cutoffs.md#logarithm-and-real-powers) apply to the examples and radial bounds. The Fourier transform is unitary:

\[
 \widehat f(\xi)=(2\pi)^{-n/2}\int e^{-ix\cdot\xi}f(x)\,dx.
\]

Kuroda's freely readable paper [K2], Section 2.3, Proposition 2.3, uses chart flattening and a Sobolev trace theorem to construct weighted traces on analytic polynomial energy surfaces. Its weight is strictly above the half-power endpoint; it does not supply the \(C^1\) endpoint surjectivity or the exact mass formula here. Those claims follow from the complete graph-slice, tangent-scale kernel and adjoint arguments in Sections 1–3 below, using the shell-space proofs of the preceding lesson. Teschl [T], Chapter 12, and Yafaev [Y] give spectral scattering context. The argument here retains only \(C^1\) regularity and includes all normalization constants.

<a id="surface-extension"></a>

## 1. Surface amplitudes and their extensions

Let \(M\subset\mathbb R^n\) be an embedded \(C^1\) hypersurface, \(K\subset M\) compact, and \(dS\) Euclidean surface measure. By \(L^2(K,dS)\) we mean amplitudes on \(K\), extended by zero on \(M\). The measure of \(K\) is finite: finitely many bounded graph patches with bounded first derivatives cover it. Define

\[
 E_Ka(x)=(2\pi)^{-n/2}\int_K e^{ix\cdot\xi}a(\xi)\,dS(\xi).
\]

The integral is absolutely convergent, since \(a\in L^2(K)\subset L^1(K)\). It is a bounded continuous function of \(x\), and its distributional Fourier transform is the measure \(a\,dS|_K\). For completeness, dominated convergence against \( |a|\,dS\) proves continuity. Boundedness makes the extension a tempered distribution, since an integrable Schwartz weight bounds each test integral by a Schwartz seminorm. For a Schwartz test \(\psi\), absolute interchange is permitted by \(\|a\|_1\|\widehat\psi\|_1<\infty\). Fourier inversion therefore gives the bilinear distribution pairing

\[
 \begin{gathered}
 \langle\widehat{E_Ka},\psi\rangle\\
 =\int E_Ka(x)\widehat\psi(x)\,dx\\
 =\int_K a(\xi)\psi(\xi)\,dS(\xi).
 \end{gathered}
\]

A surface amplitude is therefore different from an ordinary \(L^2(\mathbb R^n_\xi)\) Fourier function.

**Lemma 1.1.** There is a constant \(C_K\), depending on a finite graph cover, such that

\[
 \|E_Ka\|_{B^*}\leq C_K\|a\|_{L^2(K,dS)}.
\]

**Proof.** Use a finite continuous partition on a neighborhood of \(K\) in \(M\), subordinate to graph patches. It suffices to estimate one partitioned amplitude. Rotate coordinates so that the patch is

\[
 \xi=(\varphi(\eta),\eta),\qquad
 J(\eta)=\sqrt{1+|\nabla\varphi(\eta)|^2},\qquad dS=J(\eta)\,d\eta.
\]

Write \(x=(t,y)\). Extension of a patch amplitude is

\[
 (2\pi)^{-1/2}\mathcal F_y^{-1}
       \big(e^{it\varphi(\eta)}a(\varphi(\eta),\eta)J(\eta)\big)(y).
\]

For every \(t\), slice Plancherel gives squared \(L^2_y\) norm

\[
 (2\pi)^{-1}\int |a(\varphi(\eta),\eta)|^2J(\eta)^2\,d\eta
 \leq (2\pi)^{-1}\sup J\,\|a\|_{L^2(dS)}^2.
\]

The dual slice estimate in the preceding lesson bounds its \(B^*\) norm. Orthogonal rotations preserve that norm. Sum the finitely many patch estimates, and bound the partitioned amplitude norms by a fixed multiple of \(\|a\|_2\). No derivative of \(J\), or second derivative of \(\varphi\), was used. In dimension one, a compact subset of an embedded zero-dimensional manifold is finite; the same argument is the finite sum of scalar slice estimates. \(\square\)

<a id="surface-observation"></a>

## 2. What a large observation region measures

For \(\xi\in M\), let \(\nu(\xi)\) be either unit normal. A global choice of sign is unnecessary, since the next formula integrates over the whole normal line.

**Theorem 2.1.** If \(a\in L^2(K,dS)\), \(u=E_Ka\), and \(\Phi\) is a Schwartz function on \(\mathbb R^n\), then

\[
 \lim_{R\to\infty}\frac1R\int \Phi(x/R)|u(x)|^2\,dx
 =\frac1{2\pi}\int_K |a(\xi)|^2
          \left(\int_{\mathbb R}\Phi(t\nu(\xi))\,dt\right)dS(\xi).
\]

This includes smooth compactly supported \(\Phi\), whether or not it is radial or nonnegative.

**Proof.** Put \(d=n-1\). Expanding the two surface integrals and then setting \(x=Rs\) gives exactly

\[
 \frac1R\int\Phi(x/R)|u(x)|^2\,dx
 =(2\pi)^{-n/2}\iint
   R^d\widehat\Phi(R(\eta-\xi))a(\xi)\overline{a(\eta)}
             \,dS(\eta)\,dS(\xi).
\]

Fubini is justified by \(a\in L^1(K)\) and \(\Phi\in L^1\). We prove the limiting surface kernel carefully.

Fix a compact neighborhood \(S\) of \(K\) in \(M\), covered by finitely many slightly larger graph patches. It exists by taking finitely many smaller chart pieces with compact closure inside their charts, whose interiors cover \(K\). Thus \(K\subset\operatorname{int}_M S\); all interiors in this proof are relative to \(M\). Such patches give the uniform measure estimate

\[
 dS(S\cap B(\xi,r))\leq C_S r^d
 \quad(\xi\in S,\ r>0).
\]

For small \(r\), orthogonal projection of each graph piece into its horizontal plane puts its projection in a ball of radius \(r\), and its area factor is bounded. Summing finitely many pieces proves the estimate. For large \(r\), enlarge the constant and use the finite area of \(S\). For \(d=0\), the estimate says that the number of points is bounded.

Choose \(L>d\). Rapid decrease of \(\widehat\Phi\), and a decomposition into distances at most \(R^{-1}\) and between \(2^jR^{-1}\) and \(2^{j+1}R^{-1}\), imply

\[
 \sup_{\xi\in S}\int_S
     R^d|\widehat\Phi(R(\eta-\xi))|\,dS(\eta)\leq C_{S,\Phi}
 \quad(R\geq1).
\]

Indeed the near part is at most \(C R^d(R^{-1})^d=C\). The \(j\)-th annular part is at most \(C R^d2^{-jL}(2^{j+1}/R)^d\); its sum converges because \(2^{d-L}<1\). These estimates include \(d=0\).

The same bound holds with \(\xi,\eta\) interchanged, since the absolute Schwartz bound is symmetric in their distance. These two bounds give a uniform \(L^2(S)\) kernel-operator bound. Indeed Cauchy–Schwarz with the absolute kernel first bounds the square at \(\xi\) by its kernel integral times the integral of that kernel against \(|b(\eta)|^2\); integration in \(\xi\) gives \(C_{S,\Phi}^2\|b\|_2^2\).

Now take a continuous amplitude \(a\) compactly supported in the interior of \(S\). Fix \(\xi\) in that support. Near \(\xi\), use orthonormal tangent coordinates to write

\[
 \eta=\xi+Qv+\nu\,h(v),\qquad
 h(0)=0,\quad Dh(0)=0,
\]

where \(Q:\mathbb R^d\to T_\xi M\) is an isometry. The graph area factor tends to one as \(v\to0\). On this chart, set \(w=Rv\). Since \(h\) is differentiable at zero,

\[
 Rh(w/R)\longrightarrow0
 \quad\hbox{for every fixed }w.
\]

The bound \(|Qw+\nu Rh(w/R)|\geq|w|\) supplies an integrable dominating function \(C(1+|w|)^{-L}\). Thus the inner surface integral converges to

\[
 \overline{a(\xi)}\int_{T_\xi M}\widehat\Phi(v)\,dv.
\]

The part outside the chart tends to zero: it stays a positive distance from \(\xi\), and its absolute value is at most \(C R^d(1+cR)^{-L}\). The uniform kernel bound just proved allows dominated integration in \(\xi\).

Finally, Fourier inversion in the \(d\) tangent variables, at tangent coordinate zero, gives

\[
 \int_{T_\xi M}\widehat\Phi(v)\,dv
 =(2\pi)^{n/2-1}\int_{\mathbb R}\Phi(t\nu(\xi))\,dt.
\]

To justify this identity by absolutely defined transforms, put \(F(y)=\int_{\mathbb R}\Phi(Qy+t\nu)\,dt\). This is Schwartz on \(\mathbb R^d\): derivatives pass under the integral, and every weighted derivative is bounded by integrating a sufficiently high Schwartz decay bound in \(t\). Fubini in the integrable \((y,t)\) variables gives

\[
 \begin{gathered}
 \widehat\Phi(Qv)=(2\pi)^{-1/2}\mathcal F_dF(v),\\
 \int\mathcal F_dF(v)\,dv=(2\pi)^{d/2}F(0).
 \end{gathered}
\]

The second equality is the already proved unitary Fourier inversion at zero. Since \(d=n-1\), the factor is \((2\pi)^{n/2-1}\). Combining it with the prefactor of the expanded quadratic integral gives \((2\pi)^{-1}\). For \(d=0\), integration on the tangent space means evaluation at its single point with mass one, and the same identities hold. The normal-line expression is continuous in each local continuous unit normal, by uniform Schwartz domination in \(t\). It is unchanged under sign reversal, so these local expressions agree and define a measurable bounded function on \(S\).

We now approximate the zero extension of \(a\) from \(K\) by continuous functions compactly supported in \(\operatorname{int}_M S\). No assumption on the measure of \(\partial_M S\) is needed. Choose a finite partition equal to one near \(K\), with each weight supported compactly in one chart inside \(\operatorname{int}_M S\). In that chart a partitioned amplitude has compact support, and the continuous area factor \(J\) is bounded above and below on a slightly larger compact set. Extend its coordinate function by zero to \(\mathbb R^d\), approximate it in ordinary \(L^2\) by smooth functions using the earlier mollification proof, and multiply the approximants by a fixed smooth coordinate cutoff equal to one on its support. This preserves convergence and keeps all approximants in that slightly larger set; boundedness of \(J\) gives convergence in \(L^2(J\,d\eta)\). Transport them back, extend by zero outside the chart, and sum the finitely many approximations. Their supports lie strictly inside their charts, so they are continuous on \(M\). This proves the required approximation. For \(d=0\) it is immediate on the finite set. The uniform kernel-operator bound controls the difference of the quadratic integrals by

\[
 C\|a-b\|_2(\|a\|_2+\|b\|_2),
\]

uniformly in \(R\). The limiting quadratic form has the same continuity, because the normal-line integral of a Schwartz function is uniformly bounded over unit normals. Passing to the \(L^2\) limit proves the theorem. \(\square\)

The same identity holds for every continuous compactly supported \(\Phi\). Approximate it uniformly by smooth functions whose supports lie in one fixed ball \(B(0,L)\) with \(L\ge1\), using the earlier uniform mollification theorem for continuous compactly supported functions. The difference of the observation integrals is at most
\[
 \|\Phi-\Phi_j\|_\infty\,\frac1R
                  \int_{|x|<LR}|E_Ka(x)|^2\,dx
       \leq C_{K,L}\|\Phi-\Phi_j\|_\infty\|a\|_2^2,
\]
uniformly for \(R\geq1\), by the ball comparison and Lemma 1.1. On the limiting side, the difference of normal-line integrals is at most \(2L\|\Phi-\Phi_j\|_\infty\). First let \(R\to\infty\) at fixed \(j\), then \(j\to\infty\). This extends the full \(C^1\)-surface formula without adding smoothness to the surface.

For example \(\Phi(s)=e^{-|s|^2}\) has normal-line integral \(\sqrt\pi\), so

\[
 \lim_{R\to\infty}\frac1R\int e^{-|x|^2/R^2}|E_Ka(x)|^2\,dx
       =\frac1{2\sqrt\pi}\|a\|_2^2.
\]

This expression is positive for every nonzero amplitude. Smoothness beyond \(C^1\) and nonzero curvature are both unnecessary.

<a id="surface-tail-distance"></a>

**Corollary 2.2.** The unweighted ball average satisfies

\[
 \lim_{R\to\infty}\frac1R\int_{|x|<R}|E_Ka(x)|^2\,dx
       =\frac1\pi\|a\|_2^2.
\]

Consequently

\[
 \operatorname{dist}_{B^*}(E_Ka,B^*_0)=(2\pi)^{-1/2}\|a\|_2,
 \qquad
 (2\pi)^{-1/2}\|a\|_2\leq\|E_Ka\|_{B^*}\leq C_K\|a\|_2,
 \qquad E_Ka\in B^*_0\ \Longleftrightarrow\ a=0.
\]

**Proof.** For \(0<\delta<1\), choose smooth nonnegative radial functions satisfying

\[
 1_{\{|s|<1-\delta\}}\leq\Phi_-(s)\leq1_{\{|s|<1\}}
       \leq\Phi_+(s)\leq1_{\{|s|<1+\delta\}}.
\]

Their normal-line integrals are between \(2(1-\delta)\) and \(2\), and between \(2\) and \(2(1+\delta)\), respectively, uniformly in the normal. Theorem 2.1 sandwiches the lower and upper limits of the ball average between \((1-\delta)\|a\|_2^2/\pi\) and \((1+\delta)\|a\|_2^2/\pi\). Let \(\delta\downarrow0\). Proposition 2.4 of the preceding lesson converts this ball limit into the exact distance \(\sqrt{\|a\|_2^2/(2\pi)}\). Distance is at most the ordinary norm, giving its lower bound; the distance is zero exactly when \(a=0\), giving the vanishing-tail criterion. The upper bound is Lemma 1.1. \(\square\)

<a id="surface-trace"></a>

## 3. The trace is bounded and onto

**Theorem 3.1.** Restriction of the Fourier transform of a Schwartz function to \(K\) extends uniquely to a bounded surjective map

\[
 T_K:B\longrightarrow L^2(K,dS).
\]

Its adjoint, under the integral duality of \(B\) and \(B^*\), is \(E_K\). In particular, no surface curvature hypothesis is imposed.

**Proof.** Fubini gives, for a Schwartz function \(f\),

\[
 (\widehat f|_K,a)_{L^2(K)}=(f,E_Ka).
\]

Lemma 1.1 and \(B\)-\(B^*\) duality bound this by \(C_K\|f\|_B\|a\|_2\). Taking the supremum over unit amplitudes gives the trace bound. Density of Schwartz functions in \(B\), already proved using compact spatial approximation, supplies the unique extension and the adjoint identity. Corollary 2.2 bounds this adjoint below by \((2\pi)^{-1/2}\). The onto criterion proved in Theorem 4.2 of the flat-shell lesson therefore applies with \(X=B\) and \(\mathcal H=L^2(K,dS)\), and proves surjectivity. \(\square\)

The surface has ambient Lebesgue measure zero locally: in graph coordinates every vertical section is a singleton or empty, so nonnegative product integration gives measure zero. Orthogonal changes preserve Lebesgue measure, and a countable graph cover gives the assertion on all of \(M\). Thus the trace of a general \(B\) function is an \(L^2\) limit on the surface. Choosing an arbitrary measurable representative of its ambient \(L^2\) Fourier transform and evaluating it on a measure-zero surface would not define this trace.

**Example 3.2.** In \(\mathbb R^2\), the graph \(\xi_1=|\xi_2|^{3/2}\) is \(C^1\), although its second derivative is unbounded at zero. On a compact patch it has area factor

\[
 J(\eta)=\sqrt{1+\tfrac94|\eta|}.
\]

The trace theorem applies there. An amplitude \(a\) on that patch produces ball mass \(\|a\|_{L^2(J\,d\eta)}^2/\pi\). A stationary-phase argument demanding a nondegenerate Hessian would not cover the whole patch, whereas the tangent-scale proof above does.

<a id="surface-energy-measure"></a>

## 4. Surface measure and energy measure

Suppose \(p\in C^1\) is real, and \(\nabla p\ne0\) near a compact part of \(M_\lambda=\{p=\lambda\}\). Energy measure on that surface is

\[
 d\sigma_\lambda=\frac{dS}{|\nabla p|}.
\]

This factor follows directly from change of variables. On a patch with \(\partial_1p\ne0\), use \((\lambda,\eta)=(p(\xi),\xi')\) and write \(\xi_1=\Sigma(\lambda,\eta)\). Then

\[
 d\xi=|\partial_1p|^{-1}\,d\lambda\,d\eta,
 \qquad dS=\frac{|\nabla p|}{|\partial_1p|}\,d\eta.
\]

The second identity follows by differentiating \(p(\Sigma(\lambda,\eta),\eta)=\lambda\): \(\partial_{\eta_j}\Sigma=-\partial_{j+1}p/\partial_1p\). Dividing the two Jacobians proves the claimed density. A finite partition proves the local coarea formula

\[
 \int g(\xi)\,d\xi
 =\int d\lambda\int_{M_\lambda}g(\xi)\,d\sigma_\lambda(\xi)
\]

first for nonnegative Borel functions compactly supported in that region, and then for all nonnegative Borel functions there as follows. Choose a countable cover by energy-coordinate patches: rational balls form a countable base, so one can select such a cover from the local patches. Make it disjoint by replacing the \(j\)-th patch by the Borel set left after removing its predecessors. Apply the single-chart formula (CI9) to the function restricted to each such set, and sum using nonnegative interchange. This proves the displayed formula without a compact-support restriction. Apply it to \( |g|\) and then to the real and imaginary positive and negative parts for absolutely integrable complex \(g\). For completed-measurable \(g\), choose a Borel representative; the same formula applied to a null exceptional set shows that the surface sections and their integrals are well defined for almost every \(\lambda\).

The notation \(\delta(p-\lambda)=d\sigma_\lambda\) is also justified at each fixed regular level, against compactly supported continuous tests in the regular region: the [regular-level limit (CI10)–(CI11)](../providers/analysis/coordinate-inverses-and-integration.md#regular-level-limit) proves that integration against \(\pi^{-1}\varepsilon/((p-\lambda)^2+\varepsilon^2)\) tends to precisely this surface integral. This fixes the normalization without treating a pointwise value of a merely measurable slice as a distributional definition.

On a fixed compact regular patch, \(|\nabla p|\) is bounded above and below by positive constants. If \(0<m\le |\nabla p|\le M\) on \(K\), then \(M^{-1}\|b\|_{L^2(dS)}^2\le\|b\|_{L^2(d\sigma_\lambda)}^2\le m^{-1}\|b\|_{L^2(dS)}^2\). Hence the two target spaces have the same elements and equivalent norms: boundedness and surjectivity of the same trace follow from Theorem 3.1. For \(b\in L^2(d\sigma_\lambda)\), also \(b/|\nabla p|\in L^2(dS)\), since its squared norm is at most \(m^{-1}\|b\|_{L^2(d\sigma_\lambda)}^2\). Pairing the trace with \(b\) in energy measure therefore identifies its adjoint as

\[
 E_{\sigma,\lambda}b(x)
 =(2\pi)^{-n/2}\int_K e^{ix\cdot\xi}b(\xi)\,d\sigma_\lambda(\xi)
 =E_K\big(b/|\nabla p|\big)(x).
\]

In particular its spatial mass is

\[
 \lim_{R\to\infty}\frac1R\int_{|x|<R}|E_{\sigma,\lambda}b|^2\,dx
 =\frac1\pi\int_K\frac{|b(\xi)|^2}{|\nabla p(\xi)|^2}\,dS(\xi).
\]

The two gradient factors arise because the extension amplitude itself already contains one inverse gradient. They must not be replaced by the single gradient factor in the energy-space norm.

**Example 4.1.** For \(p(\xi)=\xi_1^2+2\xi_2^2\) and \(\lambda>0\), the energy shell is an ellipse and

\[
 |\nabla p|=2\sqrt{\xi_1^2+4\xi_2^2}.
\]

Thus \(d\sigma_\lambda=dS/(2\sqrt{\xi_1^2+4\xi_2^2})\). Even though \(p\) is constant on the ellipse, its gradient length varies. The energy density and surface density are therefore different measures.

### Use the conclusion

Read the bounded trace and the onto conclusion as different claims. In the ellipse example, identify the surface measure and the velocity factor separately before comparing the mass formula with global radiation.

<a id="surface-exercises"></a>

## 5. Exercises

**Exercise 5.1 (foundation).** For the affine graph \(\xi_1=\beta\cdot\eta+\lambda\), compute the graph area factor, the slice \(L^2\) norm of its extension, and its ball-mass limit. Explain which quantity depends on the slope when the amplitude is measured using \(dS\).

**Exercise 5.2 (foundation).** In one dimension let \(K=\{\xi_1,\xi_2\}\), with \(\xi_1\ne\xi_2\), and use counting measure. Compute the Gaussian average of the extension of amplitudes \(a_1,a_2\), including its mixed term. Verify the limit in Theorem 2.1.

**Exercise 5.3 (intermediate).** Let \(\Phi(s)=\exp(-s^TQs)\), where \(Q\) is real symmetric positive definite. Compute the limiting observation integral in Theorem 2.1. Show that reversing a chosen normal has no effect.

**Exercise 5.4 (intermediate).** Suppose \(a,b\in L^2(K,dS)\) and \(E_Ka-E_Kb\in B^*_0\). Prove \(a=b\). Does this conclusion require \(a,b\) to be smooth?

**Exercise 5.5 (advanced).** For \(p(\xi)=c\xi_1\), \(c>0\), and a compact set \(K\) in \(p=\lambda\), express \(E_{\sigma,\lambda}b\) using the partial inverse Fourier transform. Compute its mass limit and compare it with \(\|b\|_{L^2(d\sigma_\lambda)}^2\). Identify the exact remaining speed factor.

<a id="surface-solutions"></a>

## 6. Complete solutions

**Solution 5.1.** The constant area factor is \(J=\sqrt{1+|\beta|^2}\). Slice Plancherel in Lemma 1.1 is an equality here:

\[
 \|E_Ka(t,\cdot)\|_2^2
 =(2\pi)^{-1}J^2\int|a(\beta\cdot\eta+\lambda,\eta)|^2\,d\eta
 =(2\pi)^{-1}J\|a\|_{L^2(dS)}^2.
\]

The ball-mass limit is \(\pi^{-1}\|a\|_{L^2(dS)}^2\). The coordinate slice norm depends on the slope because the chosen slices need not be perpendicular to the normal. The ball and the surface norm are invariant under rotation, so their relation is independent of that slope.

**Solution 5.2.** The extension is \((2\pi)^{-1/2}(a_1e^{ix\xi_1}+a_2e^{ix\xi_2})\). The elementary Gaussian integral gives

\[
 \frac1R\int e^{-x^2/R^2}|E_Ka(x)|^2\,dx
 =\frac1{2\sqrt\pi}\left(
 |a_1|^2+|a_2|^2+
 2\operatorname{Re}(a_1\overline{a_2})
             e^{-R^2(\xi_1-\xi_2)^2/4}\right).
\]

The distinct frequencies make the mixed term tend to zero. The limit is \((2\sqrt\pi)^{-1}(|a_1|^2+|a_2|^2)\), as asserted. If the frequencies coincided, they would form one surface point with amplitude \(a_1+a_2\); counting them as two distinct points would give the wrong target space.

**Solution 5.3.** On a normal line, \(\Phi(t\nu)=e^{-t^2\nu^TQ\nu}\). Its integral is \(\sqrt\pi/\sqrt{\nu^TQ\nu}\). Hence the limit is

\[
 \frac1{2\sqrt\pi}\int_K
       \frac{|a(\xi)|^2}{\sqrt{\nu(\xi)^TQ\nu(\xi)}}\,dS(\xi).
\]

Positive definiteness bounds the denominator above and below. Replacing \(\nu\) by \(-\nu\) leaves the quadratic form unchanged. The observation region distinguishes normal directions but not their orientations.

**Solution 5.4.** Linearity gives \(E_K(a-b)\in B^*_0\). Corollary 2.2 says its ball average tends to \(\pi^{-1}\|a-b\|_2^2\), while the definition of \(B^*_0\) says that limit is zero. Thus \(a=b\) in \(L^2(K)\). The theorem was proved for all \(L^2\) amplitudes by the uniform kernel bound, so no smoothness is needed.

**Solution 5.5.** Here \(dS=d\eta\), \(|\nabla p|=c\), and \(d\sigma_\lambda=c^{-1}d\eta\). Extend \(b\) by zero in \(\eta\). Then

\[
 E_{\sigma,\lambda}b(t,y)
 =(2\pi)^{-1/2}c^{-1}e^{it\lambda/c}\mathcal F_y^{-1}b(y).
\]

Its ball-mass limit is \(\pi^{-1}c^{-2}\|b\|_{L^2(d\eta)}^2\). Since \(\|b\|_{L^2(d\sigma_\lambda)}^2=c^{-1}\|b\|_{L^2(d\eta)}^2\), the limit is \((\pi c)^{-1}\|b\|_{L^2(d\sigma_\lambda)}^2\). The remaining inverse speed converts the energy normalization into mass per unit spatial radius.

## References


- [Y] Dmitri Yafaev, *Lectures on scattering theory*, 2004, [arXiv:math/0403213](https://arxiv.org/abs/math/0403213).
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, American Mathematical Society, 2014. [Freely readable author's edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
- [K2] Shige Toshi Kuroda, *Scattering theory for differential operators, II, self-adjoint elliptic operators*, Journal of the Mathematical Society of Japan **25** (1973), 222–234. [Freely readable journal PDF](https://www.jstage.jst.go.jp/article/jmath1948/25/2/25_2_222/_pdf/-char/en), Section 2.3, pp. 228–230; Appendix, pp. 232–234. This is a comparison for weighted regular-shell traces and energy coordinates, with the scope distinction stated above.
