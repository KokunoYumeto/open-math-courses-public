# Global polynomial resolvent estimates

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: What turns infinitely many regular patches into one resolvent estimate?** A hyperbolic polynomial can have an unbounded energy shell even away from its critical value. Normalized translations supply local constants, but their reconstruction requires a norm estimate over all patch centres. The flat polynomial \(p=\xi_1\) gives a useful control case: division remains valid although transverse propagation has no elliptic gain.

A nonelliptic energy surface can run to infinity in frequency space. A finite collection of ordinary coordinate patches cannot control the whole surface. Normalized polynomial translations provide uniformly controlled patches at every centre; square-integrated localization then reconstructs one global endpoint estimate.

The exact inputs are the strength and threshold alternative in Polynomial translations and regular energies, local division and weighted zero-trace division in [Division and radiation at regular energies](division-and-radiation-at-regular-energies.md#division-boundary), and the multiplier and reconstruction theorems in [Mild weights and frequency localization](mild-weights-and-frequency-localization.md#mild-cutoff-family). The maximal self-adjoint Fourier-multiplier domain is established in [Resolvents, domains and spectral density](resolvents-domains-and-spectral-density.md#u001-specified-domains). We retain the unitary Fourier transform and the pairing linear in its first argument.

The construction below derives the endpoint estimate from those complete preceding proofs. A freely readable comparison is Agmon's Appendix A [A], whose Theorem A.1 proves weighted Hilbert-space estimates for constant-coefficient operators with a principal homogeneous part of principal type. Its proof uses one-variable polynomial factorization and an absorption of weighted commutators. The endpoint norms, arbitrary weaker numerators, invariant directions and global square-integrated reconstruction used here are proved in this course at their stated scope. The critical-value assertion in that appendix is cited there without proof; the preceding lesson supplies its full algebraic argument.

<a id="global-polynomial-domains"></a>

## 1. The hypotheses and the boundary topology

Let \(p\) be a nonconstant real polynomial on \(\mathbb R^n\), simply characteristic, allowing nonzero invariant directions. Write

\[
 \widetilde p(\eta)=
       \left(\sum_\alpha|\partial^\alpha p(\eta)|^2\right)^{1/2},
 \qquad
 Z(p)=\{p(\eta):\nabla p(\eta)=0\}.
\]

All sums of polynomial derivatives are finite. For a polynomial \(Q\), put

\[
 \kappa_p(Q)=\sup_\eta\widetilde Q(\eta)/\widetilde p(\eta).
\]

The assertion below concerns precisely the \(Q\) for which this number is finite. A lower-order operator need not satisfy this condition.

Here simply characteristic means that there is a finite \(C_0\) such that

\[
 \widetilde p(\eta)\leq C_0
       \bigl(1+|p(\eta)|+|\nabla p(\eta)|\bigr)
       \quad(\eta\in\mathbb R^n).
\]

A nonzero derivative of highest order is a nonzero constant, so \(\widetilde p\) has a positive lower bound. The numerator \(Q\) may have complex coefficients. The weaker-polynomial argument proves that \(Q\ne0\) and \(\kappa_p(Q)<\infty\) imply \(\deg Q\leq\deg p\), and bounds all translated numerator derivatives by that same weakness factor. Thus the constants below do not conceal a dependence on an unbounded numerator degree. The zero numerator is immediate.

The operator \(P=p(D)\), \(D=-i\partial_x\), has maximal domain

\[
 \mathcal D(P)=\{u\in L^2:p\widehat u\in L^2\}.
\]

For nonreal \(z\), its \(L^2\) resolvent is \(R_p(z)=(P-z)^{-1}\). The spaces \(B,B^*,B^*_0\) and their dyadic norms are those in [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md). A weak-star continuous \(B^*\)-valued function means that its pairing with each \(g\in B\) is continuous. The two closed half-planes are considered separately, so a real point has an upper and a lower boundary value.

**Theorem 1.1.** If \(K\) is a compact subset of either closed half-plane and \(K\cap Z(p)=\varnothing\), then

\[
 \|Q(D)R_p(z)f\|_{B^*}
       \leq C_{p,K}\kappa_p(Q)\|f\|_B,\qquad z\in K.
\tag{1}
\]

For each \(f\in B\), the operator on the left has a unique weak-star continuous extension to that closed half-plane with the critical points removed. For a real regular energy \(\lambda\), denote these extensions by \(Q(D)R_\pm(\lambda)f\).

For a nonreal \(z\), \(Q(D)R_p(z)\) need not be bounded on all of \(L^2\). In (1) it is the distributional polynomial derivative of the \(L^2\) resolvent, and the theorem proves its additional \(B^*\) regularity.

<a id="uniform-local-division"></a>

## 2. Uniformity of the local division estimate

We first isolate the uniformity needed in (1).

**Lemma 2.1.** Let a compact family of real polynomials \(q\), of bounded degree, satisfy \(\omega\cdot\nabla q\geq c>0\) on a fixed ball, where the unit direction \(\omega\) may vary. For a smooth cutoff \(\rho\) supported in a sufficiently smaller concentric ball,

\[
 \left\|\mathcal F^{-1}
       \left(\frac{\rho\widehat h}{q-i\beta}\right)\right\|_{B^*}
       \leq C\|h\|_B,\qquad \beta\geq0,
\tag{2}
\]

including the upper boundary at \(\beta=0\). The constant can be chosen uniformly over this family and over bounded collections of cutoffs with a common compact support. If instead \(|q-i\beta|\geq c\) on that support and all coefficients and \(\beta\) range over a compact set, the same conclusion holds.

For the real boundary, if

\[
 (1+t)\mu'(t)\leq N\mu(t),\qquad
 \mu>0,\quad\mu'\geq0,\quad \mu\in C^1([0,\infty)),
\tag{3}
\]

where \(N\) is a fixed nonnegative integer, and the cutoff shell trace of \(h\) is zero, then

\[
 \left\|\mu(|x|)\mathcal F^{-1}
       \left(\frac{\rho\widehat h}{q\mp i0}\right)\right\|_{B^*}
       \leq C_N\|\mu(|x|)h\|_B.
\tag{4}
\]

The two boundary outputs in (4) coincide. In the real nonvanishing case, (4) holds without a trace condition.

**Proof.** Orthogonal rotations preserve the physical shell norms. The set of permitted polynomial and direction pairs is compact after retaining the closed inequality \(\omega\cdot\nabla q\geq c\). Near each pair choose a rotation and a small product coordinate neighborhood in which this derivative stays above \(c/2\). Polynomial coefficient bounds control all derivatives on the ball. The inverse graph derivatives are therefore bounded, by successive implicit differentiation: each new denominator is a power of the derivative bounded below, and each numerator is a finite combination of already bounded derivatives.

The quantitative local graph construction supplies the common product neighborhoods used here. Its sizes depend only on the ball radius, the positive directional lower bound and the uniform gradient bound. Apply it at level points meeting the smaller cutoff support, which stays a fixed distance inside the original ball. A finite number of such neighborhoods suffices uniformly: cover the compact set of coefficient, direction, point and energy parameters for which the point lies on the level. Within each parameter neighborhood, the spatial cutoffs can be obtained from fixed smooth bumps by dividing by their positive sum, as in the [finite partition proof](../providers/analysis/coordinate-inverses-and-integration.md#finite-partitions). Regions separated from the level use the nonvanishing estimate below. This includes a level which misses the cutoff support, without presuming that its inverse graph exists there.

The finite-regularity kernel proof in the local-division lesson uses only these derivative bounds, this positive lower bound, compact cutoff bounds and the size of the coordinate neighborhood. Its Heaviside coefficient is bounded by the reciprocal derivative, and its divided difference has bounded derivatives on the common compact neighborhood. Outside the common cutoff region that divided difference has a uniformly controlled \(O(|\tau-\Sigma|^{-1})\) tail; two derivatives give an \(O(|\tau-\Sigma|^{-3})\) tail, so the differentiated remainder has a common integrable bound. In particular apply that lesson's Lemma 2.1 with \(N=2\), using common \(C^{3,\alpha}\) bounds for any fixed \(0<\alpha<1\). The polynomials have these bounds, since their derivatives of one further order are uniformly bounded and the mean-value theorem supplies the Hölder bound on the common compact neighborhood. The lemma gives a remainder bounded by a common multiple of \((1+|t|)^{-2}\). Its integral is finite and independent of the polynomial parameter. Thus its slice estimate has a common constant on a neighborhood of each pair. Shrink the cutoff ball as needed, cover the compact parameter set by finitely many such neighborhoods, and take the largest constant. The local slice bounds \(B\to L^1_tL^2_y\) and \(L^\infty_tL^2_y\to B^*\) give (2). The proof also gives weak-star boundary continuity for each parameter.

For bounded imaginary parameters the [half-plane argument](division-and-radiation-at-regular-energies.md#division-halfplane) passes this common real-boundary slice bound to the nonreal parameter. For \(\beta\geq1\), the denominator has absolute value at least \(\beta\). Repeated differentiation of its reciprocal expresses each fixed-order derivative as a finite sum of bounded polynomial derivatives divided by powers of \(q-i\beta\); these sums are bounded uniformly for \(\beta\geq1\). The compact cutoff multiplier bound therefore treats this entire unbounded range. Formula (2) really holds for all \(\beta\geq0\).

For (4), use that local lesson's weighted division proof with \(C^{N+2}\) bounds, which the polynomial family has uniformly. Its radial-weight step chooses a frame of nearby independent directions. At each parameter pair choose that frame with all directional derivatives still above \(c/4\); the frame's inverse matrix has a finite norm. A finite parameter cover bounds both this norm and every local kernel constant. All weight comparisons depend only on \(N\). The vanishing trace permits joining the upper estimate on one favorable half-space to the lower estimate on the other, giving (4).

One explicit uniform frame is \(\omega\) together with
\((\omega+\varepsilon v_j)/\sqrt{1+\varepsilon^2}\), where the \(v_j\) form an orthonormal basis of \(\omega^\perp\). If \(M\) bounds \(|\nabla q|\), take \(0<\varepsilon\leq\min\{1,c/[4(1+M)]\}\). Each of these directional derivatives is at least \((c-\varepsilon M)/\sqrt{1+\varepsilon^2}>c/4\), and the inverse-frame norm is bounded in terms of \(n,\varepsilon\) alone. In dimension one, the single direction suffices. The [weighted zero-trace proof](division-and-radiation-at-regular-energies.md#division-weights) consequently has a common radial-weight constant, even as the patch direction varies.

In the nonvanishing case, \(\rho/(q-i\beta)\) has uniformly bounded derivatives of every fixed order, by the denominator lower bound and the coefficient bounds. The multiplier theorem gives a uniform \(B\to B\) bound, followed by \(B\subset B^*\). At \(\beta=0\), apply the weighted multiplier version with shell weights \(2^{j/2}\mu(2^j)\). Condition (3) bounds their adjacent ratios by \(2^{N+1/2}\); choosing an integer \(L>N+1/2\) gives the multiplier bound. Finally \(\|\mu u\|_{B^*}\leq\|\mu u\|_B\). There is no pole, so the boundary values coincide. \(\square\)

The smaller cutoff ball is harmless. The threshold alternative remains true on any smaller ball, and a normalized smooth cutoff of arbitrarily small support can still have \(L^2\) norm one.

<a id="global-polynomial-reconstruction"></a>

## 3. Reconstructing the global resolvent

**Proof of Theorem 1.1.** The assertion is vacuous for an empty \(K\), so assume \(K\ne\varnothing\). Treat the upper half-plane first. The threshold alternative of Theorem 4.1 in the polynomial-translation lesson supplies a radius \(r>0\) and a compact family

\[
 q_{\eta,z}(\xi)=
       \frac{p(\eta+\xi)-\operatorname{Re}z}{\widetilde p(\eta)},
 \qquad
 \beta_{\eta,z}=
       \frac{\operatorname{Im}z}{\widetilde p(\eta)}.
\]

On the ball of radius \(r\), each pair has either a uniformly nonvanishing complex denominator or a uniformly positive real directional derivative. Lemma 2.1 consequently applies with one constant.

Choose \(\chi\in C_c^\infty\) in the smaller ball, with \(\|\chi\|_2=1\), and choose \(\rho\) equal to one near \(\operatorname{supp}\chi\), still supported in that ball. Put

\[
 w_\eta=e^{-i\eta\cdot x}\chi(D-\eta)f,\qquad
 r_\eta(\xi)=
       \rho(\xi)\frac{Q(\eta+\xi)}{\widetilde p(\eta)}.
\]

Modulation is an isometry on \(B\) and \(B^*\). Every fixed finite collection of derivatives of \(r_\eta\) is bounded by \(C\kappa_p(Q)\), uniformly in \(\eta\), by the weaker-polynomial Taylor estimate. Thus

\[
 \|r_\eta(D)w_\eta\|_B
       \leq C\kappa_p(Q)\|\chi(D-\eta)f\|_B.
\tag{5}
\]

For \(f\) with smooth compactly supported Fourier transform, multiplier cancellation gives the exact identity

\[
 e^{-i\eta\cdot x}\chi(D-\eta)Q(D)R_p(z)f
   =\mathcal F^{-1}
       \left(\frac{\rho\,\widehat{r_\eta(D)w_\eta}}
                   {q_{\eta,z}-i\beta_{\eta,z}}\right).
\tag{6}
\]

Both occurrences of \(\rho\) equal one on the Fourier support of \(w_\eta\). The strength in the original denominator cancels the strength in \(r_\eta\). Apply Lemma 2.1 to (6), then (5), to obtain

\[
 \|\chi(D-\eta)Q(D)R_p(z)f\|_{B^*}
       \leq C\kappa_p(Q)\|\chi(D-\eta)f\|_B.
\tag{7}
\]

At a real boundary, first define the output distribution on its compact Fourier support by a finite partition into regular graph patches and regions away from the level. The local boundary construction makes this independent of the partition. It is a tempered, locally square-integrable function: every finite patch output belongs to \(B^*\). Formula (6) continues to hold.

More precisely, fix a regular real energy \(\lambda_0\). On the fixed compact Fourier support, every point of \(p=\lambda_0\) has nonzero gradient. Choose finitely many graph neighborhoods there. The remaining compact set is separated from that level, and stays separated for all \(z\) sufficiently close to \(\lambda_0\). Keep this partition fixed in that energy neighborhood. The local division theorem gives the graph boundary limits, while the complementary smooth multiplier converges directly. Their sum is the distributional limit of the original nonreal multiplier; hence two partitions give the same boundary distribution. Multiplication by any fixed frequency cutoff commutes with this limit, proving (6) on the boundary as well. For the parameter integral, the measurable localized family and its shell norms are exactly those constructed in [the reconstruction theorem](mild-weights-and-frequency-localization.md#mild-distribution-detection).

Square (7), integrate in \(\eta\), and use respectively the lower \(B^*\) reconstruction and upper \(B\) localization inequalities from the weight lesson:

\[
 \begin{split}
 \|Q(D)R_p(z)f\|_{B^*}^2
 &\leq C\int
       \|\chi(D-\eta)Q(D)R_p(z)f\|_{B^*}^2\,d\eta\\
 &\leq C\kappa_p(Q)^2\int
       \|\chi(D-\eta)f\|_B^2\,d\eta\\
 &\leq C\kappa_p(Q)^2\|f\|_B^2.
 \end{split}
\]

Smooth compact-frequency test functions are dense in \(B\): approximate by Schwartz functions, then take larger smooth Fourier cutoffs, which converge in all Schwartz seminorms. Estimate (1) therefore defines a bounded extension on every \(f\in B\). For nonreal \(z\), the approximation also converges in \(L^2\), so the extended output agrees distributionally with \(Q(D)R_p(z)f\). Polynomial differentiation is continuous on tempered distributions.

For compact-frequency forcing, finite local patches give weak-star continuity in \(z\). To pass to arbitrary forcing, approximate in \(B\); the uniform estimate on each compact \(K\) bounds all scalar pairing errors uniformly there. Thus continuity holds for every \(f\). Any two boundary extensions agree by approaching the real point from the open half-plane. Replacing \(p,z,f\) by \(-p,-z,-f\) gives the lower half-plane. \(\square\)

The boundary output for a numerator \(Q\) is indeed the polynomial derivative of the output for \(Q=1\). Test the nonreal identity against a Schwartz function and pass to the boundary. Such tests and their polynomial derivatives belong to \(B\), so weak-star convergence implies the required distributional convergence. The same argument gives \((p(D)-\lambda)R_\pm(\lambda)f=f\). These identities use the original ambient polynomial and its maximal nonreal resolvent domain.

**Example 3.1.** For \(p(\xi)=\xi_1^2-\xi_2^2\), the sole critical energy is zero. Both \(Q=1\) and \(Q=\xi_1\) satisfy (1) on compact energy sets avoiding zero. The second-order \(Q=\xi_1^2\) does not meet its hypothesis, as the strength calculation in the preceding lesson shows. The theorem applies to the unbounded hyperbolic energy surfaces without an ellipticity assumption.

<a id="imaginary-axis-uniformity"></a>

**Corollary 3.2.** The imaginary-axis bound can be made uniform at infinity:
\[
 \sum_\alpha\|(\partial^\alpha p)(D)R_p(it)f\|_{B^*}
       \leq C_p\|f\|_B,\qquad |t|\geq1.
\]

**Proof.** The simple-characteristic inequality and \(|t|\geq1\) give
\[
 \widetilde p\leq C_0(1+|p|+|\nabla p|)
       \leq C_0(2|p-it|+|\nabla p|).
\]
Thus the threshold ratio has a positive bound independent of \(t\), without using compactness of its energy set. The normalized real polynomials are now \(q_\eta=p(\eta+\cdot)/\widetilde p(\eta)\); their coefficients and all fixed-ball derivatives are uniformly bounded. If \(|t|/\widetilde p(\eta)\leq1\), their imaginary parameters lie in a compact interval, so the alternative and Lemma 2.1 apply with a uniform constant. If that ratio exceeds one, the normalized denominator has absolute value greater than one everywhere, and its cut-off reciprocal has uniformly bounded derivatives of every fixed order. The same multiplier bound applies there.

Repeat (5)-(7) and the integrated reconstruction for each \(Q=\partial^\alpha p\), whose weakness ratio is at most one. Sum the finitely many bounds. The two signs of \(t\) are handled in their respective half-planes. \(\square\)

## 4. Global weighted division when the trace vanishes


<a id="global-polynomial-traces"></a>

For \(f\in B\), the Fourier trace on each compact part of the regular surface \(M_\lambda=\{p=\lambda\}\) is defined by the [compact trace theorem](fourier-traces-on-curved-energy-surfaces.md#surface-trace). These traces agree on overlaps: both are continuous extensions of the same Schwartz restriction. Thus saying \(T_\lambda f=0\) has a precise meaning even before proving a bound on the whole surface.

<a id="global-weighted-division"></a>

**Theorem 4.1.** Let \(K\subset\mathbb R\setminus Z(p)\) be compact and let \(\mu\) satisfy (3). If \(\|\mu(|x|)f\|_B<\infty\) and \(T_\lambda f=0\), then

\[
 R_+(\lambda)f=R_-(\lambda)f,
\]

and, for every weaker \(Q\),

\[
 \|\mu(|x|)Q(D)R_\pm(\lambda)f\|_{B^*}
       \leq C_{p,K,N}\kappa_p(Q)\|\mu(|x|)f\|_B,
       \qquad \lambda\in K.
\tag{8}
\]

The constant is independent of the weight and its multiplicative normalization.

**Proof.** Since \(\mu(t)\geq\mu(0)>0\), the forcing belongs to \(B\), so Theorem 1.1 already defines both unweighted boundary outputs. Every compact Fourier localization has zero jump by its local trace formula. Testing against compact-frequency test functions, which are dense in the Schwartz topology, shows that the global jump is zero.

Use the same \(\chi,\rho,w_\eta,r_\eta\) as in (6), now with real \(z=\lambda\). The logarithmic-growth estimate for \(\mu\) and the weighted multiplier bound give

\[
 \|\mu(|x|)r_\eta(D)w_\eta\|_B
       \leq C_N\kappa_p(Q)
                    \|\mu(|x|)\chi(D-\eta)f\|_B.
\tag{9}
\]

For example, this follows from the \(B_c\) multiplier theorem with
\(c_j=2^{j/2}\mu(2^j)\) and an integer \(L>N+1/2\). Uniform derivatives of \(r_\eta\) through order \(L\) give exactly the stated constant. Modulation preserves weighted shell norms too.

The trace of \(r_\eta(D)w_\eta\) on \(q_{\eta,\lambda}=0\) vanishes: on that surface its Fourier trace is \(\rho Q/\widetilde p(\eta)\) times the shifted localized trace \(\chi T_\lambda f\), which is zero. Compatibility of multiplication, modulation and restriction follows first for Schwartz forcing and then by their bounded local trace interfaces.

In each regular patch, Lemma 2.1's weighted zero-trace estimate applied to (6) gives

\[
 \|\mu(|x|)\chi(D-\eta)Q(D)R_\pm(\lambda)f\|_{B^*}
       \leq C_N\kappa_p(Q)
                    \|\mu(|x|)\chi(D-\eta)f\|_B.
\tag{10}
\]

In the nonvanishing patch its weighted multiplier estimate gives the same inequality. The local zero-trace proof applies directly to the already defined forcing through its \(L^1_tL^2_y\) integral representation; no trace-preserving smooth approximation is being presumed.

Square and integrate (10). The radial weighted lower \(B^*\) reconstruction inequality, followed by the radial weighted upper \(B\) localization inequality, proves (8). Both follow from adjacent-ratio comparisons with exponent \(N\), so all weight constants depend only on \(N\). The unweighted output is tempered and locally square integrable, as required by lower reconstruction; the conclusion proves its stronger weighted membership. \(\square\)

**Example 4.2.** If \(g\) is Schwartz with smooth compact Fourier support away from critical frequencies, set \(f=(p(D)-\lambda)g\). Its shell trace is zero, and \(R_\pm(\lambda)f=g\). Taking \(\mu(t)=(1+t)^a\), \(0\leq a\leq N\), proves (8) for every weaker derivative, with the expected solution and without a radiating surface term.

For the asserted equality, the nonreal resolvent identity reads \(R_p(z)f=g+(z-\lambda)R_p(z)g\). Apply (1) with \(Q=1\) on a small compact half-disk about the regular energy \(\lambda\). The last term tends to zero in \(B^*\), so either boundary limit equals \(g\).

<a id="invariant-potential-counterexample"></a>

**Example 4.3 (a flat symbol and the limit of propagation).** Theorems 1.1 and 4.1 and Corollary 3.2 apply to \(p(\xi)=\xi_1\) on \(\mathbb R^2\), retaining the original forcing on the whole physical plane, all ambient frequency cutoffs, the maximal domain and the original weakness factors. Theorem 4.1 in the preceding lesson supplies the uniform alternative with invariant directions included; its Lemma 2.2 preserves the original ambient strengths. Local division, modulation and square-integrated reconstruction therefore apply verbatim.

This does not supply compactness of every compactly supported potential on the later polynomial graph space. Choose nonzero \(a,\phi\in C_c^\infty(\mathbb R^2)\) with \(a\phi\ne0\), and set \(u_j=e^{ijx_2}\phi\). The graph norms built from \(u_j,D_1u_j\) in \(B^*\) are independent of \(j\). Yet

\[
 (au_j,au_k)=\int e^{i(j-k)x_2}|a\phi|^2\,dx
       \longrightarrow0\quad(|j-k|\to\infty),
\]

by Riemann–Lebesgue, whereas \(\|au_j\|_2=\|a\phi\|_2>0\). No subsequence is Cauchy in \(L^2\), hence none is Cauchy in \(B\), because \(\|h\|_2\le\|h\|_B\). This multiplication is not compact from that graph space to \(B\). Later potential-compactness and scattering hypotheses must retain their own required assumptions.

Here the oscillatory limit also follows directly from integration by parts. Put \(b(t)=\int|a(x_1,t)\phi(x_1,t)|^2\,dx_1\), so \(b\in C_c^\infty(\mathbb R)\). For \(j\ne k\), the displayed inner product has absolute value at most \(\|b'\|_1/|j-k|\). Thus, from any infinite subsequence, one can choose two indices arbitrarily far out with arbitrarily large difference. Their squared distance tends to \(2\|a\phi\|_2^2>0\), which rules out a Cauchy subsequence.

### Use the conclusion

Check the admissible numerator polynomial against the strength bound, then compare the zero-trace weighted conclusion with the ordinary endpoint boundary value. Keep the maximal multiplier domain when taking nonreal resolvents.

<a id="global-polynomial-exercises"></a>

## 5. Exercises

**Exercise 5.1 (foundation).** Explain why \(e^{i\eta\cdot x}\) is an isometry on \(B\), on \(B^*\), and on either space with a positive radial weight. Does the operator \(\chi(D-\eta)\) generally have the same property?

**Exercise 5.2 (foundation).** Check every strength factor and cutoff in (6). In particular, explain why using the original denominator \(p(\eta+\xi)-z\) together with \(r_\eta\) would introduce an erroneous additional factor.

**Exercise 5.3 (intermediate).** Let \(p(\xi)=\xi_1-\xi_2^2\). Prove the hypotheses of Theorem 1.1 and identify three weaker derivative symbols. Does its critical-energy set contain zero?

**Exercise 5.4 (intermediate).** For \(\mu(t)=(1+t)^a\), \(a\geq0\), give a valid integer \(N\) in Theorem 4.1 and a valid integer \(L\) for the weighted multiplier step. Explain why neither constant depends on replacing \(\mu\) by \(c\mu\), \(c>0\).

**Exercise 5.5 (advanced).** Let \(p(\xi)=\xi^2\) on the line and let \(\lambda>0\). For Schwartz \(f\), write the exact trace condition for (8). If it fails at one shell point, use the localized radiation formula to show that the corresponding boundary wave cannot belong to \(B^*_0\). Explain the distinction between this obstruction and the finite weighted forcing hypothesis.

<a id="global-polynomial-solutions"></a>

## 6. Complete solutions

**Solution 5.1.** Each shell norm is an \(L^2\) norm, and the modulation has absolute value one. Thus every shell norm is unchanged; summation or taking the supremum proves all four assertions. A radial weight commutes with modulation and has the same pointwise argument. In contrast, a Fourier cutoff spreads a physical-space function by convolution and can change its distribution between shells. Its boundedness is a theorem, not an isometry statement.

**Solution 5.2.** With \(\widehat w_\eta(\xi)=\chi(\xi)\widehat f(\eta+\xi)\), the right side of (6) has Fourier transform

\[
 \frac{\rho(\xi)^2 Q(\eta+\xi)\chi(\xi)\widehat f(\eta+\xi)}
      {\widetilde p(\eta)\,[q_{\eta,z}(\xi)-i\beta_{\eta,z}]}
 =\frac{Q(\eta+\xi)\chi(\xi)\widehat f(\eta+\xi)}
             {p(\eta+\xi)-z}.
\]

Here \(\rho^2\chi=\chi\). This is exactly the Fourier transform of the left side. If the denominator on the right were already \(p(\eta+\xi)-z\), the factor \(1/\widetilde p(\eta)\) in \(r_\eta\) would no longer cancel. The identity, and hence the desired operator being estimated, would be wrong.

**Solution 5.3.** The strength identity is

\[
 \widetilde p^2=p^2+4\xi_2^2+5
              =p^2+|\nabla p|^2+4.
\]

Thus it is bounded by a constant times \((1+|p|+|\nabla p|)^2\). Also \(D_vp=v_1-2v_2\xi_2\), identically zero only for \(v=0\). The gradient \((1,-2\xi_2)\) never vanishes, so \(Z(p)=\varnothing\). The derivative symbols \(1\), \(-2\xi_2\), and \(-2\) are all weaker, being respectively \(\partial_1p,\partial_2p,\partial_2^2p\). In this example every compact complex energy set is permitted.

**Solution 5.4.** Take any integer \(N\geq a\); then \((1+t)\mu'=a\mu\leq N\mu\). Taking \(L=N+1\) gives \(L>N+1/2\), as needed for adjacent-ratio interpolation. Multiplying the weight by \(c\) changes both sides of every weighted norm estimate by \(c\), and leaves its logarithmic derivative and all ratios unchanged. The constants therefore remain the same.

**Solution 5.5.** The two shell points are \(\xi=\pm\sqrt\lambda\), so the condition is
\(\widehat f(\sqrt\lambda)=\widehat f(-\sqrt\lambda)=0\). A cutoff around either point where the trace is nonzero has \(g=|p'|=2\sqrt\lambda\). Its ball-mass limit is

\[
 2\pi\frac{|\widehat f(\pm\sqrt\lambda)|^2}{4\lambda}>0
\]

when the cutoff is one at that point. Such a localized boundary wave is not in \(B^*_0\). Since the smooth cutoff multiplier preserves \(B^*_0\), the full boundary wave cannot be in that space either. Schwartz forcing has every finite polynomial weighted \(B\) norm, but this does not remove its radiating amplitude. The zero-trace condition controls that amplitude; the weighted forcing condition controls the remaining division estimate.

## References

- [A] Shmuel Agmon, *Spectral properties of Schrödinger operators and scattering theory*, Annali della Scuola Normale Superiore di Pisa, series 4, **2** (1975), 151–218, Appendix A. [Freely readable journal PDF](https://www.numdam.org/item/ASNSP_1975_4_2_2_151_0.pdf).

- Dmitri Yafaev, *Lectures on scattering theory*, 2004. [arXiv:math/0403213](https://arxiv.org/abs/math/0403213).
- Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, 2014. [Freely readable author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
