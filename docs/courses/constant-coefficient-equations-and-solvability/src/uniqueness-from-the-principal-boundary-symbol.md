# Uniqueness from the principal boundary symbol

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The principal boundary symbol controls the inverse determinant near the time direction at high frequency. Its nonvanishing removes analytic singular directions normal to time. Causal support then forces the homogeneous solution to vanish. We justify compact localization for arbitrary spatial growth and explain why finitely many zero initial jets suffice to extend a difference of solutions to the past.

Read [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md), [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md), [Degenerate boundary symbols and smooth nonuniqueness](degenerate-boundary-symbols-and-smooth-nonuniqueness.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies compact extrema and cutoffs; [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supplies proper convolution.

The hyperbolic-cone and analytic zero-order prerequisites remain planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html); their precise statements are given in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). Local Holmgren uniqueness also remains planned: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic surface vanishes near that surface. Analytic support normals and analytic convolution ellipticity remain planned as stated below. The uses of these prerequisites are conditional on their planned proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The written prerequisite lessons supply the auxiliary proofs used below.

## Statement and exact prerequisites

Use the normalized notation of [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md), [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md) and [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md), with \(N=e_n,\theta=e_1\), \(a=x_1\), tangent variables \(x'=(z,t)\), and exactly \(h=m_+\) boundary symbols. Let \(L^\partial\) be their determinant and \(\widehat\Lambda_0\) its homogeneous principal symbol, of integer degree \(\kappa\). Assume
\[
                       \widehat\Lambda_0(N')\ne0 .
 \tag{1}
\]
Then every smooth causal homogeneous mixed solution is zero. More generally two solutions smooth on the closed quarter-space \(\{a\ge0,t\ge0\}\), with equal interior forcing, equal first \(m\) time jets and equal boundary data, coincide. This proves the smooth uniqueness theorem; it asserts uniqueness of existing solutions, not existence for every datum.

The [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md) determinant annihilation, [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md) analytic principal scaling, [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) inverse/support theorem and proper-convolution/Fourier/cutoff bases are used. The cone and analytic-order statements remain planned through [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), and local Holmgren remains planned through [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md). Two analytic microlocal theorems are also explicitly planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html):

* The **analytic support normal** theorem: a real analytic function with nonzero gradient having a maximum on a distribution's support forces both signed gradient covectors into its analytic wavefront set.
* The exact **analytic convolution ellipticity** theorem, distinct from differential ellipticity: for a tempered convolution kernel \(\mu\) and compact distribution \(v\), analytic singular directions of \(v\) are contained in those of \(\mu*v\) or in the convolution characteristic set. A real nonzero direction is outside that characteristic set if \(\widehat\mu\) has a holomorphic reciprocal at infinity on a complex conic neighborhood of it, polynomially bounded there and agreeing with the reciprocal on the real cone.

Analytic convolution ellipticity in this form remains a planned prerequisite in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html). The compact-input theorem is sufficient: we prove the arbitrary-growth localization ourselves. These two theorems are used at the stated places below; neither is claimed proved here.

## A polynomially bounded reciprocal in a complex time cone

Let \(\Lambda(\eta',\epsilon)\) be the analytic scaled determinant from [equation 14 in The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md). Near \((\eta',\epsilon)=(-iN',0)\) it is nonzero by equation 1 and complex homogeneity. For complex \(\zeta'\) with \(r=\zeta'_t\ne0\), define, when \(|r|\) is large and \(\zeta'/r\) is sufficiently close to \(N'\),
\[
\begin{gathered}
L_{\rm ext}(\zeta')
   \\
=(-i/r)^{-\kappa}\Lambda(-i\zeta'/r,-i/r),\\
\qquad
 \Phi(\zeta')\\
=(-i/r)^\kappa
           \{\Lambda(-i\zeta'/r,-i/r)\}^{-1}.
\end{gathered}
\tag{2}
\]
Every integer power is single-valued, including negative \(\kappa\). The quotients, \(\Lambda\) and its reciprocal are holomorphic on this region. One fixed smaller product neighborhood gives positive lower and upper bounds for the modulus of \(\Lambda\). Since \(|r|\) and \(|\zeta'|\) are comparable there,
\[
\begin{gathered}
|L_{\rm ext}(\zeta')|\ge c|r|^\kappa,\\
\qquad
 |\Phi(\zeta')|\\
\le C|r|^{-\kappa}
                      \\
\le C'(1+|\zeta'|)^{\max(0,-\kappa)} .
\end{gathered}
\tag{3}
\]
Restricting additionally to \(|\arg r|<\delta\), for one small \(\delta>0\), gives a complex conic neighborhood of the real positive time ray at infinity. Nonvanishing is uniform on a smaller such neighborhood, so the same characteristic exclusion holds for every real direction in one open cone \(W\) about \(N'\).

Here is why this extension represents the determinant rather than another analytic branch. Fix \(\eta'\) near \(N'\), so that \(-i\eta'\) stays in the projected tube. [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s positive-scale identity gives
\(\Lambda(-i\eta',\epsilon)=\epsilon^\kappa L^\partial(-i\eta'/\epsilon)\)
for small positive \(\epsilon\). The left side is holomorphic on a full disk about zero. The original-tube admissible scale set is the inverse image of the open convex projected cone under the real-linear map
\(\epsilon\mapsto-\operatorname{Im}(-i\eta'\overline\epsilon)\),
because division by \(|\epsilon|^2\) is a positive scalar. Its intersection with a small disk, excluding zero, is connected: either the open cone excludes zero and that intersection is convex, or the cone contains zero and is the whole plane, whose punctured disk is connected. It contains the positive scale ray. Analytic identity therefore gives the same determinant formula at every admissible nonzero scale in that disk. Taking \(\eta'=\zeta'/\zeta'_t\) and \(\epsilon=-i/\zeta'_t\) proves equality of equation 2 with the original determinant wherever \(\zeta'\) is also in the original tube. In particular
\(L_{\rm ext}(\xi'-i\tau N')=L^\partial(\xi'-i\tau N')\)
for sufficiently small positive \(\tau\) and every large real \(\xi'\) in the time cone. This proves a local extension at infinity; no global reciprocal is assumed.

Let \(\mu=L_0\) be [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s inverse determinant distribution. It is tempered, has cone support and has weighted Fourier transform \(L^\partial\) on the projected tube. The transform on the real time cone is the smooth boundary value just identified:
\[
\begin{gathered}
\widehat\mu(\xi')=L_{\rm ext}(\xi'),\\
\qquad
             \Phi(\xi')\widehat\mu(\xi')=1
               \\
\quad(\xi'\in W,\ |\xi'|>R_0).
\end{gathered}
\tag{4}
\]
Indeed the tangent exponential \(e^{-\tau t}\mu\) converges to \(\mu\) in tempered distributions as \(\tau\downarrow0\). Choose a smooth cone cutoff \(\chi_0=1\) near the support cone, equal to one near the origin, and supported for large \(|x'|\) in \(t\ge b|x'|/2\). A one-variable smooth cutoff in \(t/(1+|x'|^2)^{1/2}\), joined to a compact cutoff near the origin, constructs it with bounded derivatives. The multiplier
\(\chi_0e^{-\tau t}+1-\chi_0\)
equals the exponential near the support, has uniformly bounded derivative seminorms for \(0<\tau\le1\), and tends to one on compact sets with every derivative. Splitting a Schwartz test into compact and rapidly decreasing tail pieces proves convergence in every Schwartz seminorm after multiplying the test. Thus the weighted distributions converge as asserted. Their Fourier transforms are \(L^\partial(\xi'-i\tau N')\). On every compact subset of the real high-frequency cone the holomorphic extension converges smoothly to \(L_{\rm ext}(\xi')\). These two limits give equation 4 distributionally, hence as a smooth function there. Equations 2–4 meet exactly the reciprocal criterion in the planned convolution theorem.

## Compact localization and analytic regularity at every output

Let \(u\) be right smooth on \(H'=\{a\ge0\}\), supported in \(t\ge0\), with \(Pu=0\) in its interior and all homogeneous boundary traces zero. [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md) gives \(L_0*_{x'}u=0\) on the whole right half-space. Fix any \(a\ge0\) and write \(v(x')=u(a,x')\). Then
\[
\begin{gathered}
\mu*v=0,\\
\qquad \operatorname{supp}v\subset\{t\ge0\},
 \\
\qquad \operatorname{supp}\mu\subset C_0\subset D_0,\\
\quad
                t_y\ge b|y|\ (y\in D_0).
\end{gathered}
\tag{5}
\]
This convolution is proper without any growth bound on \(v\).

At each relatively compact output neighborhood \(O\), an input in \(\operatorname{supp}v\) relevant to \(\operatorname{supp}\mu\) has time between zero and the maximum output time, and its distance from the output is at most the output-input time difference divided by \(b\). The relevant inputs consequently lie in one compact set. Choose a compact cutoff \(\chi=1\) near that entire set and near \(O\). Proper convolution gives
\[
\begin{gathered}
v_c=\chi v\in\mathcal E',\\
\qquad
               \mu*v_c=\mu*v=0\text{ on }O,\\
\qquad
               v_c=v\text{ on }O .
\end{gathered}
\tag{6}
\]
For negative-time neighborhoods the conclusion follows directly from \(v=0\); enlarging the compact set treats neighborhoods crossing time zero. No global transform of \(v\) is taken.

Apply the stated compact-input convolution theorem to \(\mu,v_c\). Its exact conclusion is
\[
\begin{gathered}
 \operatorname{WF}_A(v_c)
   \\
\subset \operatorname{WF}_A(\mu*v_c)
                 \\
\cup\bigl(\mathbb R^{n-1}\times\operatorname{Char}\mu\bigr).
 \end{gathered}
\tag{7}
\]
On \(O\) the first term is absent, since \(\mu*v_c=0\). Every direction in the fixed cone \(W\) is outside \(\operatorname{Char}\mu\) by equations 2–4. Since \(v_c=v\) near each output, locality gives the uniform direction statement
\[
\begin{gathered}
(x',\xi')\notin\operatorname{WF}_A(v)
           \\
\quad\text{for every }x'\text{ and }\xi'\in W .
\end{gathered}
\tag{8}
\]
The spatial cutoff varies with the output, but the cone \(W\) does not. This distinction supplies the global support argument while retaining only the compact-input prerequisite.

## A quadratic support minimum proves causal uniqueness

We prove the needed consequence of equation 8 and the planned analytic support normal theorem explicitly. Suppose \(v\ne0\), and take a support point \((z_0,t_0)\), where \(t_0\ge0\). For \(\epsilon>0\) define
\[
              G(z,t)=t+\epsilon|z-z_0|^2 .
 \tag{9}
\]
The nonempty sublevel \(G\le t_0\) on the closed support is compact, since \(0\le t\le t_0\) and \(|z-z_0|\le\sqrt{t_0/\epsilon}\). A global minimum is attained at a support point \(x_*\). At that point
\[
\begin{gathered}
dG(x_*)=N'+2\epsilon(z_*-z_0,0),\\
\qquad
        |dG(x_*)-N'|\le2\sqrt{\epsilon t_0}.
\end{gathered}
\tag{10}
\]
Choose \(\epsilon\) sufficiently small that this vector lies in \(W\); if \(t_0=0\), it equals \(N'\) and any positive \(\epsilon\) works. The real analytic function \(-G\) has a maximum on the support at \(x_*\) and has nonzero differential, because its time derivative is minus one. The analytic support normal statement forces both signs of \(-dG\) into \(\operatorname{WF}_A(v)\), in particular \(+dG\). This contradicts equation 8. Thus \(v=0\).

The argument applies separately to every fixed \(a\ge0\), so
\[
                          u=0\quad\text{on }H'.
 \tag{11}
\]
It uses no compactness, tempering or fixed finite order of the original \(v\). The compact quadratic sublevel and the locally valid analytic regularity supply those missing global bounds. At \(h=0\), [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md) already gives \(u=0\) directly because the empty determinant is one.

## From finitely many initial data to a smooth past extension

Let \(u_1,u_2\) be two smooth quarter-space solutions with identical data, and put \(w=u_1-u_2\). Its interior equation and boundary data are zero, and its time jets \(D_t^j w|_{t=0}\), \(0\le j<m\), vanish. The polynomial time order is exactly \(m\), with constant nonzero leading coefficient \(P_m(N)\), because its total degree is \(m\). Hence
\[
\begin{gathered}
P(D)\\
=P_m(N)D_t^m+
           \sum_{j=0}^{m-1}Q_j(D_a,D_z)D_t^j .
\end{gathered}
\tag{12}
\]
By right smoothness the equation extends continuously to \(t=0\) for \(a>0\). The first \(m\) jet functions and all their spatial derivatives there vanish, so equation 12 implies \(D_t^m w|_{t=0}=0\). Differentiate the equation in time and repeat: induction gives every higher time jet zero. Continuity up to \(a=0\) extends those identities to the corner; all tangent/normal spatial derivatives of those zero jet functions vanish as well.

Taylor's integral remainder, uniformly on compact spatial sets in \(a\ge0\), now shows that extension by zero to \(t<0\) is jointly smooth up to the normal boundary. There are no time-boundary delta terms, the homogeneous equation holds on the whole interior of \(H'\), and the boundary traces remain zero. The extension meets [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md) and equation 5. Equation 11 makes it zero, so \(u_1=u_2\). No arbitrary full smooth extension across \(a=0\) is needed.

Combined with [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md)'s rank-deficient construction and [Degenerate boundary symbols and smooth nonuniqueness](degenerate-boundary-symbols-and-smooth-nonuniqueness.md)'s principal-degenerate construction, this gives the exact smooth uniqueness criterion for the balanced boundary count: when the determinant is nonzero, uniqueness holds if and only if its principal symbol is nonzero at the time direction. This criterion does not determine which data admit a solution.

## Exercises with complete solutions

**Exercise 1 (entry: constant and negative principal degrees).** For the normalized wave symbol \(P(\xi,s)=(s-i)^2-\xi^2\), compare \(B_1=1,\xi,\xi+s\). Also consider \(P=(s-i)(\xi+s-i)-1\), \(B_1=\xi+s-i\). Compute the reciprocal high-frequency orders and decide uniqueness.

**Solution.** The first three determinants and principal symbols are \(1\) with degree zero, \(i-s\) with degree one and symbol \(-s\), and \(i\) with degree zero and symbol \(i\). Each symbol is nonzero at the time direction \(s=1\). Their reciprocal orders are zero, minus one and zero. The characteristic example has determinant \(1/(s-i)\), principal degree minus one and principal symbol \(1/s\), also nonzero at \(s=1\). Its reciprocal is \(s-i\), which grows polynomially. Thus all four cases have uniqueness, although their inverse determinant behavior differs:
\[
             \Phi=1,\quad(i-s)^{-1},\quad-i,\quad s-i .
 \tag{13}
\]
Negative principal degree is allowed. Polynomial growth of the reciprocal is exactly what the conic analytic regularity statement requires; uniform boundedness would wrongly omit the fourth case.

**Exercise 2 (intermediate: why one absent direction alone is insufficient for the support proof).** Explain why the support-minimum argument uses a whole fixed cone about \(N'\). Contrast that with a distribution analytic in that cone at every point, and verify what happens if the chosen support time is zero.

**Solution.** The gradient of the quadratic minimum is \(N'+2\epsilon(z_*-z_0,0)\). It need not equal \(N'\) for positive \(t_0\); excluding only that single covector at each point would not exclude the gradient forced by the support theorem. A fixed open cone contains a ball about \(N'\), so choosing \(2\sqrt{\epsilon t_0}\) smaller than its radius gives the contradiction. The minimum point is unknown when \(\epsilon\) is chosen, which is why an output-dependent cone radius would not suffice. Equation 2 gives one cone independent of the output, and equation 6 localizes only the compact input, preserving that cone. If \(t_0=0\), the compact sublevel forces \(z_*=z_0,t_*=0\), so \(dG=N'\) exactly and no smallness condition beyond \(\epsilon>0\) is needed.

**Exercise 3 (advanced: two initial jets determine all higher jets in a wave example).** Let \(P=(s-i)^2-\xi^2\), and let \(w\) solve the homogeneous equation smoothly for \(a,t\ge0\), with \(w(a,0)=\partial_t w(a,0)=0\). Derive the recurrence for every higher time jet. Explain why the smooth past extension required in the uniqueness proof follows.

**Solution.** In physical variables the equation is
\[
\begin{gathered}
-\partial_t^2w-2\partial_t w-w+\partial_a^2w=0,\\
\qquad
 f_{k+2}=\partial_a^2 f_k-2f_{k+1}-f_k,\\
\quad
 f_k(a)=\partial_t^k w(a,0).
\end{gathered}
\tag{14}
\]
Since \(f_0=f_1=0\) as smooth functions, the recurrence gives \(f_2=0\), then \(f_3=0\), and by induction all \(f_k=0\). Spatial derivatives vanish too. The recurrence first holds for \(a>0\) and extends to \(a=0\) by right continuity. Taylor remainders on every compact \(a\)-interval show that every differentiated \(w\) tends to zero faster than any prescribed normal time power at \(t=0\). Extending by zero to negative time therefore gives a jointly smooth function, including the corner. Two zero initial jets suffice because this polynomial has time order two; assuming an independently prescribed infinite sequence of jets would be unnecessary.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
