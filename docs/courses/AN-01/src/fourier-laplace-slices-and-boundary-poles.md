# Fourier-Laplace slices and boundary poles

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

Suppose an analytic function is observed along several horizontal lines. What information do those observations contain about its inverse Fourier transform? A pointwise formula may hide a removable pole; an entire continuation may coexist with input on both sides of the origin. The useful data are the *square-integral norms of the slices*, together with their dependence on height.

We first calculate these data for a pulse of finite duration and for a Gaussian. The calculations distinguish support information from analytic continuation and show why the sign of the Fourier kernel matters. A common inverse-transform lemma then makes this interpretation rigorous for arbitrary square-integrable slices. The half-plane theorem recovers a one-sided input; the strip theorem recovers two exponential tail bounds. The common input determines a convex domain of finite slice norms; its logarithmic curvature is a covariance matrix, and its large-height slopes recover the actual compact support hull. Finally, adding two boundary traces becomes an inverse problem for a nonvanishing frequency multiplier.

We use \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)dx\), inverse factor \((2\pi)^{-n}\), \(D=-i\partial\), and complex bilinear distributional pairings.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves every Schwartz transform, Gaussian integral, inverse and transpose rule used here. [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Lemma0.1, proves Schwartz Plancherel. The supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and16, proves measure, convergence, product integration, linear Jacobians, the norm inequalities, completeness and compact smooth density. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the elementary calculus and matrix operations. We give the required completed square-integral Fourier maps below and prove the slice estimates with scalar Cauchy–Schwarz and Tonelli.

The exact Cauchy and Taylor formulas, finite-regularity boundary theorem and pole jumps are [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem1.1, Corollary2.2, Theorem3.1, Corollary3.2 and Theorem4.1. The several-variable power-series construction and connected identity principle are [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section3 and Lemma3.1.

## Completing the square-integral Fourier maps

**Lemma 0.1.** The Schwartz Fourier transform and its inverse extend uniquely to mutually inverse continuous maps on \(L^2(\mathbb R^n)\), with
\[
 \begin{gathered}
 \|\mathcal Ff\|_2=(2\pi)^{n/2}\|f\|_2,\\
 \|\mathcal F^{-1}g\|_2=(2\pi)^{-n/2}\|g\|_2.
 \end{gathered}
\]
They agree with the tempered-distribution transforms and, on \(L^1\cap L^2\), with the ordinary integral transform.

**Proof.** By integration §15.3, choose \(\phi_j\in C_c^\infty\subset\mathcal S\) tending to \(f\) in \(L^2\). U041, Lemma0.1, gives
\[
 \|F\phi_j-F\phi_k\|_2
       =(2\pi)^{n/2}\|\phi_j-\phi_k\|_2.
\]
Completeness therefore defines \(\mathcal Ff=\lim_jF\phi_j\). The same equality proves independence of the approximating sequence, linearity, the exact norm and uniqueness of a continuous extension. Since \(G=(2\pi)^{-n}RF\) on Schwartz functions and reflection is an \(L^2\) isometry, the same construction gives the stated inverse norm. The two compositions equal the identity on the dense Schwartz subspace by F4; continuity extends both identities to all of \(L^2\). This proves surjectivity as well as injectivity.

Every \(L^2\) function defines a tempered distribution by Cauchy–Schwarz against a Schwartz test. For \(\theta\in\mathcal S\), scalar Fubini on the approximants gives
\[
 \int (F\phi_j)\theta=\int\phi_j(F\theta).
\]
Both sides pass to their \(L^2\) limits by Cauchy–Schwarz. This is precisely the bilinear transpose definition in F5, so the completed and distributional transforms agree, with every differentiation and reflection sign retained. The inverse is treated identically. For \(f\in L^1\cap L^2\), F5 also proves equality of the ordinary integral transform with that same distributional transform, by absolute Fubini. Its continuous integral representative consequently represents the completed transform almost everywhere.

Here and below, equality of locally \(L^2\) functions as distributions gives equality almost everywhere. To see this directly, multiply their difference \(u\) by any compact smooth cutoff \(\chi\). Then \(\chi u\in L^2\) and pairs to zero with every Schwartz function, since \(\chi\theta\) is a compact test. Approximate \(\overline{\chi u}\) in \(L^2\) by compact smooth functions and pass the zero pairings by Cauchy–Schwarz; this gives \(\int|\chi u|^2=0\). Cutoffs equal to one on an exhausting sequence of compact balls give \(u=0\) almost everywhere. The same argument inside an open set uses compactly supported cutoffs there. This proves the local support identification used later. \(\square\)

## Read the data before choosing a theorem

For a Fourier–Laplace transform with kernel \(e^{-ixz}\), the height \(\eta\) contributes \(e^{\eta x}\), not \(e^{-\eta x}\). Thus positive heights emphasize the right tail and negative heights emphasize the left tail. With the Plancherel normalization already stated, the measured quantity is

\[
\begin{gathered}
N(\eta)=(2\pi)^{-1}\|F_\eta\|_2^2\\
=\int_{\mathbb R}|f(x)|^2e^{2\eta x}\,dx.
\end{gathered}
\tag{R1}
\]

**Worked case: a pulse whose apparent pole disappears.** Take
\(f(x)=e^{-(x+1)}\mathbf1_{[-1,2]}(x)\). This pulse begins before zero and ends after zero. Direct integration over that finite interval gives

\[
\begin{gathered}
F(z)=e^{iz}\int_0^3 e^{-(1+iz)t}\,dt\\
=e^{iz}\frac{1-e^{-3(1+iz)}}{1+iz}.
\end{gathered}
\tag{R2}
\]

The integral expression is entire: on every compact set of \(z\), every complex derivative is dominated by an integrable function on \(0\le t\le3\). The quotient seems to have a pole at \(z=i\), but the numerator vanishes there as well. Its value is \(F(i)=3/e\), obtained from the integral, so the singularity is removable.

The weighted input gives a more informative measurement:

\[
\begin{gathered}
N(\eta)=e^{-2\eta}\int_0^3e^{-2(1-\eta)t}\,dt\\
=e^{-2\eta}\frac{1-e^{-6(1-\eta)}}{2(1-\eta)}
\quad(\eta\ne1),\\
N(1)=3e^{-2}.
\end{gathered}
\tag{R3}
\]

This is finite at every height, including the one at which the quotient in (R2) looks singular. Its large-height behavior records both endpoints:

\[
\begin{gathered}
\lim_{\eta\to+\infty}\frac{\log N(\eta)}{2\eta}=2,\\
\lim_{\eta\to-\infty}\frac{\log N(\eta)}{2\eta}=-1.
\end{gathered}
\tag{R4}
\]

Indeed, as \(\eta\to+\infty\),
\(N(\eta)=e^{4\eta-6}(1-e^{-6(\eta-1)})/[2(\eta-1)]\);
as \(\eta\to-\infty\), the numerator \(1-e^{-6(1-\eta)}\) tends to one in (R3). Taking logarithms gives (R4), because the logarithm of the denominator divided by \(\eta\) tends to zero. In particular \(N(\eta)\) is unbounded as \(\eta\to-\infty\). The pulse has an entire transform, yet fails the uniform lower-half-plane norm condition. Its negative-time part is exactly what that condition detects.

**Worked case: an entire transform with two infinite tails.** For
\(f(x)=e^{-x^2/2}\), the Gaussian transform from the linked Fourier proof is
\(F(z)=\sqrt{2\pi}\,e^{-z^2/2}\). The real transform formula extends to every complex \(z\): the input integral is holomorphic by compact-height Gaussian domination, and the connected identity principle gives the extension. Completing the real square yields

\[
\begin{gathered}
N(\eta)=\int e^{-x^2+2\eta x}\,dx\\
=\sqrt\pi\,e^{\eta^2}.
\end{gathered}
\tag{R5}
\]

The Gaussian mass is proved in the supplied Fourier foundation, F3. Every slice is square integrable, but neither half-plane has a uniform norm bound. Unlike (R4), the quotient \(\log N(\eta)/(2\eta)\) has no finite endpoint limit: it tends to \(+\infty\) for positive heights and to \(-\infty\) for negative heights. This calculation is consistent with the input being nonzero arbitrarily far in both directions. Entire continuation, finite norms at each height, and uniformly bounded norms on a half-plane are three different pieces of information.

**A local interpretation of the norm profile.** For any nonzero compactly supported \(L^2\) input, normalize the weighted square to a probability measure:

\[
\begin{gathered}
d\mu_\eta(x)=\frac{|f(x)|^2e^{2\eta x}}{N(\eta)}\,dx,\\
m_\eta=\int x\,d\mu_\eta(x),\\
\frac{d}{d\eta}\log N(\eta)=2m_\eta,\\
\frac{d^2}{d\eta^2}\log N(\eta)\\
=4\int(x-m_\eta)^2d\mu_\eta(x)>0.
\end{gathered}
\tag{R6}
\]

All height derivatives may pass under the integral because the support is compact. Thus \(N'=2\int x|f|^2e^{2\eta x}\) and \(N''=4\int x^2|f|^2e^{2\eta x}\); differentiating \(\log N\) gives the two identities. Equality in the last line would concentrate \(\mu_\eta\) at one point. This is impossible for a nonzero density with respect to Lebesgue measure. The slope is twice the weighted mean position, and the curvature is four times its variance. A height change is therefore a controlled change in what part of the input is emphasized. Exercise 4 proves the corresponding strict log-convex inequality for the broader strip class, without assuming compact support.

For data with only a local bound on the slice norms, the next lemma reconstructs one input compatible with all heights. A uniform bound across an entire lower half-plane has the additional force needed to exclude negative support. For a finite strip, the useful question instead concerns both endpoint weights.

## L. A common inverse transform on horizontal slices

**Lemma L.** Let \(\Omega\subset\mathbb R^n\) be nonempty, open and connected. Let \(F\) be holomorphic on \(\mathbb R^n+i\Omega\). Write \(F_\eta(\xi)=F(\xi+i\eta)\). Suppose

\[
\begin{gathered}
\sup_{\eta\in K}\|F_\eta\|_2<\infty\\
\text{for every compact }K\Subset\Omega.
\end{gathered}
\tag{L1}
\]

There is one locally square-integrable function \(f\), independent of \(\eta\), such that

\[
\begin{gathered}
F_\eta=\mathcal F(e^{\eta\cdot x}f),\\
(2\pi)^{-n}\|F_\eta\|_2^2\\
=\int |f(x)|^2e^{2\eta\cdot x}\,dx.
\end{gathered}
\tag{L2}
\]

The transform in the first equality is the completed \(L^2\) transform. Each weighted function in (L2) belongs to \(L^2\). No trace at the edge of \(\Omega\) is assumed.

**Proof.** Cauchy's coordinate-circle formula bounds the horizontal \(L^2\) norm of every derivative uniformly on smaller compact sets of heights. Indeed choose a common coordinate radius \(r>0\) whose imaginary-coordinate shifts stay in a compact subset of \(\Omega\). The derivative formula is an integral of translates
\(F(\xi+r\cos\theta+i(\eta+r\sin\theta))\), in the differentiated coordinates, multiplied by factors of modulus at most \(\alpha!r^{-|\alpha|}\). Real translations preserve the original \(L^2\) norm. For clarity, no vector-valued integration theorem is required for this estimate. Parametrize the coordinate circles by their angles with normalized product measure \(d\nu\). The Cauchy formula writes the derivative as \(\alpha!r^{-|\alpha|}\int H(\xi,\theta)d\nu(\theta)\), where \(|H|\) is the modulus of the translated \(F\) above. The scalar integral exists for every \(\xi\) by continuity on the compact circle product. Cauchy–Schwarz in the probability measure and then Tonelli give
\[
 \begin{gathered}
 \left\|\int H(\cdot,\theta)d\nu(\theta)\right\|_2^2\\
 \le\int\!\int|H(\xi,\theta)|^2d\xi\,d\nu(\theta).
 \end{gathered}
\]
The integrand is jointly continuous and hence measurable; (L1) bounds its integral. Real translation invariance now gives
\[
\begin{gathered}
\|\partial_z^\alpha F_\eta\|_2\\
\leq\alpha!r^{-|\alpha|}\\
\sup_{\eta'\in K'}\|F_{\eta'}\|_2.
\end{gathered}
\tag{L3}
\]

The circle formulas follow from U013, Corollary2.2, one coordinate at a time, or from the full polydisk proof in U015, Section3. Choose the radius small enough that every simultaneous coordinate shift stays in the enlarged compact height set. The pointwise fundamental theorem along a height segment, followed by the same scalar integral inequality on the unit interval, gives
\[
 \begin{gathered}
 \|\partial_z^\alpha F_{\eta+he_j}
       -\partial_z^\alpha F_\eta\|_2\\
 \le |h|\sup_{0\le t\le1}
              \|\partial_z^{\alpha+e_j}F_{\eta+the_j}\|_2.
 \end{gathered}
\]
Thus every derivative is locally Lipschitz in \(L^2\). Apply the fundamental theorem twice to its scalar values. The remainder after its first height derivative is an integral against \(h^2(1-t)dt\), whose total mass is \(h^2/2\). Cauchy–Schwarz for this normalized nonnegative weight and Tonelli give
\[
 \begin{gathered}
 \|\partial_z^\alpha F_{\eta+he_j}
       -\partial_z^\alpha F_\eta
       -ih\partial_z^{\alpha+e_j}F_\eta\|_2\\
 \le \frac{h^2}{2}\sup_{0\le t\le1}
              \|\partial_z^{\alpha+2e_j}F_{\eta+the_j}\|_2.
 \end{gathered}
\]
Formula(L3) bounds the right side on each small height neighborhood. Division by \(|h|\) proves norm differentiability with the stated derivative. Applying this in every coordinate and order, and telescoping along coordinate segments, proves smooth \(L^2\) dependence. Its Cauchy–Riemann equation is
\(\partial_{\eta_j}F_\eta=i\partial_{\xi_j}F_\eta\).

Put \(f_\eta=\mathcal F^{-1}F_\eta\). Lemma0.1 supplies the continuous completed inverse and its exact transpose agreement. It preserves the proved smooth dependence, and its distributional differentiation identity gives

\[
\begin{gathered}
\partial_{\eta_j}f_\eta=x_j f_\eta\\
\text{as distributions in }x.
\end{gathered}
\tag{L4}
\]

The sign is fixed by
\(\mathcal F^{-1}(\partial_{\xi_j}F)=-ix_j\mathcal F^{-1}F\).
On a compact set of \(x\), multiplication by \(e^{-\eta\cdot x}\) is a smooth distribution multiplier. Equation (L4) makes every height derivative of \(e^{-\eta\cdot x}f_\eta\) zero. For each compact smooth spatial test, its scalar pairing is smooth in height with every first derivative zero. Integrating along segments inside a ball shows that the pairing is locally constant. Its level set at a fixed height and its complement are both open, so connectedness makes the pairing constant throughout the height domain. This holds for every compact test; thus the distribution is independent of height. Fixing \(\eta_0\) therefore gives the locally \(L^2\) representative \(f=e^{-\eta_0\cdot x}f_{\eta_0}\), and \(f_\eta=e^{\eta\cdot x}f\) at every height. The original completed Plancherel identity gives (L2). This also proves uniqueness. \(\square\)

We will need (L1) when initially only an averaged entire norm is known. If \(F\) is entire and \(W(\eta)>0\) is continuous, then

\[
\begin{gathered}
\int_{\mathbb R^{2n}}|F(\xi+i\eta)|^2W(\eta)\,d\xi\,d\eta\\
<\infty
\end{gathered}
\tag{L5}
\]

implies (L1) on every compact set of heights. For one complex variable, the Cauchy Taylor series and angular orthogonality give the disk mean inequality
\(|F(z)|^2\leq(\pi r^2)^{-1}\int_{|w|<r}|F(z+w)|^2dL(w)\).
To see the inequality without an unstated subharmonic theorem, on every smaller circle the mean square of \(\sum a_k w^k\) is \(\sum |a_k|^2\rho^{2k}\geq|a_0|^2\); uniform convergence justifies the finite-series limit, and integration against \(2\rho\,d\rho/r^2\) gives the disk formula. Apply it successively in all \(n\) coordinates. Integrating the resulting inequality over \(\xi\), enlarging the polydisk to a coordinate box, and translating its real coordinates gives

\[
\begin{gathered}
\|F_\eta\|_2^2\\
\leq C_{n,r}\int_{|t|_\infty<r}\|F_{\eta+t}\|_2^2\,dt.
\end{gathered}
\tag{L6}
\]

Tonelli applies even before finiteness of a slice is established. On a compact set of \(\eta\), the continuous positive weight has a positive minimum on its enlarged compact set. Thus the right side is uniformly bounded by a constant times (L5). Every slice, including any initially exceptional slice, is in \(L^2\); the first part of the lemma now applies.

### The heights with finite norms form a convex domain

Connectedness in Lemma L ties the slices to one input. That input itself determines a larger set of heights and a holomorphic extension.

**Theorem L.1 (the finite-moment tube).** For the input \(f\) in Lemma L, put
\[
\begin{gathered}
N(\eta)=\int_{\mathbb R^n}|f(x)|^2e^{2\eta\cdot x}\,dx,\\
E=\{\eta\in\mathbb R^n:N(\eta)<\infty\}.
\end{gathered}
\tag{T1}
\]
The set \(E\) is convex, contains the original height domain, and contains its open convex hull. For \(\eta_\ell\in E\) and nonnegative weights \(t_\ell\) summing to one,
\[
N\left(\sum_\ell t_\ell\eta_\ell\right)
\le\prod_\ell N(\eta_\ell)^{t_\ell},
\tag{T2}
\]
with zero weights omitted. The function extends to \(\mathbb R^n+i\operatorname{int}E\) by the absolutely convergent integral
\[
\begin{gathered}
\widetilde F(z)=\int_{\mathbb R^n}e^{-ix\cdot z}f(x)\,dx,\\
(2\pi)^{-n}\|\widetilde F_\eta\|_2^2=N(\eta).
\end{gathered}
\tag{T3}
\]
All complex derivatives may be taken under that integral. In particular, the holomorphic extension to the tube over the convex hull of the original heights is unique.

**Proof.** If \(f=0\), \(E=\mathbb R^n\) and the extension is zero. Otherwise \(N(\eta)>0\) at every finite height. For positive weights in (T2), define the probability densities \(a_\ell(x)=|f(x)|^2e^{2\eta_\ell\cdot x}/N(\eta_\ell)\). Weighted arithmetic-geometric mean gives \(\prod_\ell a_\ell^{t_\ell}\le\sum_\ell t_\ell a_\ell\). To verify it, when \(A=\sum_\ell t_\ell a_\ell>0\) and all factors are positive, sum \(\log(a_\ell/A)\le a_\ell/A-1\) with weights \(t_\ell\), then exponentiate. A zero factor makes the inequality immediate, as does \(A=0\). Integrating and restoring the norm factors gives (T2). Thus \(E\) is convex.

Lemma L gives finiteness at every original height. Every point of its convex hull is a finite convex combination; one coefficient is positive, and moving its corresponding height inside a small ball in the original open set moves the combination through a ball. Hence this convex hull is open and lies in \(\operatorname{int}E\).

Fix \(\eta_0\in\operatorname{int}E\), and choose \(\delta>0\) so that every vertex \(\eta_\sigma=\eta_0+2\delta\sigma\), \(\sigma\in\{-1,1\}^n\), lies in \(E\). If \(|\eta-\eta_0|_\infty\le\delta\), then in the orthant \(\sigma_jx_j\ge0\),
\[
\begin{gathered}
|f(x)|e^{\eta\cdot x}\\
\le |f(x)|e^{\eta_\sigma\cdot x}
e^{-\delta\sum_j|x_j|}.
\end{gathered}
\tag{T4}
\]
For every integer \(k\ge0\), Cauchy–Schwarz bounds the integral of \(|x|^k\) times the right side by
\[
\begin{gathered}
I_{k,\sigma}=\int_{\text{orthant}}|x|^{2k}\\
{}\times e^{-2\delta\sum_j|x_j|}dx<\infty,\\
N(\eta_\sigma)^{1/2}I_{k,\sigma}^{1/2}<\infty.
\end{gathered}
\tag{T5}
\]
The latter integral is finite: bound \(|x|^{2k}\) by a finite sum of coordinate monomials and use repeated one-dimensional polynomial-exponential integrals. There are finitely many orthants. These bounds supply a single integrable majorant on the height neighborhood for each derivative order. Thus (T3) defines a holomorphic function, and
\[
\begin{gathered}
\partial_z^\alpha\widetilde F(z)\\
=\int(-ix)^\alpha e^{-ix\cdot z}f(x)\,dx.
\end{gathered}
\tag{T6}
\]
At each original height the weighted input belongs both to \(L^1\) and \(L^2\). The ordinary and completed Fourier transforms therefore coincide. Their continuous representatives agree everywhere, so the extension equals the given \(F\). Completed Plancherel proves the exact norm in (T3) at every interior height. The interior of a convex set is convex, and the connected identity principle gives uniqueness on this tube, and hence on the convex hull tube. \(\square\)

The interior of \(E\) is the domain furnished by finite slice norms. It need not be the largest domain to which the holomorphic function can be continued. Nor does convex extension add a hard support condition to the input.

### Curvature and the actual support function

The one-dimensional compact calculation (R6) holds on the whole interior finite-moment domain, with a full covariance matrix.

**Theorem L.2 (moments and support from slice norms).** Let \(f\ne0\) be locally square integrable on \(\mathbb R^n\), with \(E,N\) as in (T1) and \(\operatorname{int}E\ne\varnothing\). At every interior height define
\[
\begin{gathered}
d\mu_\eta(x)\\
=N(\eta)^{-1}|f(x)|^2e^{2\eta\cdot x}dx,\\
m_\eta=\int x\,d\mu_\eta(x).
\end{gathered}
\tag{T7}
\]
All moments exist there, \(N\) is smooth, and
\[
\begin{gathered}
\nabla\log N=2m_\eta,\\
\operatorname{Hess}\log N
=4\left[\int xx^T\,d\mu_\eta\right.\\
\left.{}-m_\eta m_\eta^T\right].
\end{gathered}
\tag{T8}
\]
The Hessian is positive definite; \(\log N\) is strictly convex on \(\operatorname{int}E\). If \(f\) is compactly supported and \(K\) is its actual closed convex support hull, then for any fixed \(\eta_0,v\in\mathbb R^n\),
\[
\begin{gathered}
\lim_{t\to\infty}\frac{\log N(\eta_0+tv)}{2t}
=H_K(v),\\
H_K(v)=\sup_{x\in K}v\cdot x.
\end{gathered}
\tag{T9}
\]

**Proof.** Use the same vertices as in (T4). On their orthants, for \(|\eta-\eta_0|_\infty\le\delta\),
\[
\begin{gathered}
|x|^k|f|^2e^{2\eta\cdot x}\\
\le |f|^2e^{2\eta_\sigma\cdot x}
|x|^k e^{-2\delta\sum_j|x_j|}.
\end{gathered}
\tag{T10}
\]
The last polynomial-exponential factor is bounded: each nonnegative coordinate power times \(e^{-c|x_j|}\) has finite maximum by elementary differentiation, and a finite monomial bound handles \(|x|^k\). The vertex density is integrable, and the finite sum over orthants gives an integrable majorant. Every height derivative passes under \(N\), and all moments are finite. In particular,
\[
\begin{gathered}
\partial_jN
=2\int x_j|f|^2e^{2\eta\cdot x}dx,\\
\partial_j\partial_kN\\
=4\int x_jx_k|f|^2e^{2\eta\cdot x}dx.
\end{gathered}
\tag{T11}
\]
Dividing and differentiating \(\log N\) gives (T8). For nonzero real \(v\), the Hessian quadratic form is \(4\int[v\cdot(x-m_\eta)]^2d\mu_\eta\). If it were zero, the probability density would be concentrated on the affine hyperplane \(v\cdot x=v\cdot m_\eta\). Choose a coordinate with nonzero coefficient in \(v\); each slice in that coordinate contains at most one point. Tonelli therefore makes this hyperplane a Lebesgue null set, contradicting the absolutely continuous probability mass. The Hessian is positive definite. Restriction to each nonconstant segment inside the convex interior gives a strictly positive second derivative, proving strict convexity.

For compact \(f\), all heights lie in \(E\). Put \(b=\operatorname*{ess\,sup}_{|f|^2dx}v\cdot x\), a finite number. The positive base-height weight does not change null sets. For each \(\varepsilon>0\), the set \(v\cdot x>b-\varepsilon\) has positive weighted mass \(c_\varepsilon\). Thus, for \(t>0\),
\[
\begin{gathered}
N(\eta_0+tv)\ge c_\varepsilon e^{2t(b-\varepsilon)},\\
N(\eta_0+tv)\le N(\eta_0)e^{2tb},\\
A_\varepsilon=\{x:v\cdot x>b-\varepsilon\},\\
c_\varepsilon=\int_{A_\varepsilon}
|f|^2e^{2\eta_0\cdot x}dx>0.
\end{gathered}
\tag{T12}
\]
Taking logarithms and dividing by \(2t\), then taking \(t\to\infty\) and \(\varepsilon\downarrow0\), proves that the limit is \(b\), including \(v=0\).

For locally \(L^2\) inputs, vanishing as a distribution on an open set is equivalent to vanishing almost everywhere there. Hence its distributional support equals the support of \(|f|^2dx\). This measure is carried by the closed support: its complement is a countable union of basic open sets on which the measure is zero. A support point with \(v\cdot x>b\) would have a sufficiently small positive-mass neighborhood in that strict region, contradicting essential supremum. Conversely the supremum on the support bounds the essential supremum. Therefore \(b\) is precisely the supremum on the actual support, which equals the supremum on its closed convex hull. This is \(H_K(v)\), proving (T9). \(\square\)

Replacing \(v\) by \(-v\) recovers the lower directional endpoint as \(-H_K(-v)\). In one dimension this proves the endpoint rule in (R4) for every nonzero compact input, even when it vanishes on part of a larger containing interval. The factors \(2\) and \(4\) in (T8) come from the weight \(e^{2\eta\cdot x}\).

For the standard statistical interpretation of these derivatives, see Charles J. Geyer's [*Exponential Families*](https://www.stat.umn.edu/geyer/5421/notes/expfam.html), Sections 3.5–3.6 and 4. Its natural parameter is \(2\eta\) for the weighted density here. The domination and support arguments needed for the present Fourier–Laplace setting have been proved above.

## A. The lower half-plane and the recovered boundary

**Theorem A.** For \(f\in L^2((0,\infty))\), extended by zero to the negative half-line,

\[
\begin{gathered}
F(z)=\int_0^\infty e^{-ixz}f(x)\,dx,\\
\operatorname{Im}z<0,
\end{gathered}
\tag{A1}
\]

is holomorphic and satisfies

\[
\begin{gathered}
\|f\|_2^2\\
=\sup_{\eta<0}(2\pi)^{-1}\|F_\eta\|_2^2\\
=\lim_{\eta\uparrow0}(2\pi)^{-1}\|F_\eta\|_2^2.
\end{gathered}
\tag{A2}
\]

Conversely every holomorphic lower-half-plane \(F\) with finite supremum in (A2) is represented uniquely by (A1). Its horizontal boundary is recovered strongly in \(L^2\): \(F_\eta\to\widehat f\) as \(\eta\uparrow0\).

**Proof.** If \(\eta<0\), Cauchy–Schwarz makes (A1) absolutely integrable: \(\int_0^\infty e^{2\eta x}dx=(-2\eta)^{-1}\). On any compact subset of the lower half-plane, every derivative is dominated by \(|f(x)|x^ke^{-cx}\) for a fixed \(c>0\); its integral is finite by the same inequality. Differentiation under the integral proves holomorphy. At each height \(F_\eta\) is the ordinary and completed transform of \(e^{\eta x}f\), so Plancherel gives
\((2\pi)^{-1}\|F_\eta\|_2^2=\int_0^\infty|f|^2e^{2\eta x}dx\).
Monotone convergence as \(\eta\uparrow0\) gives (A2), including the supremum. Dominated convergence gives \(e^{\eta x}f\to f\) in \(L^2\), hence the stated strong boundary.

For the converse write the finite supremum as \(M\). Lemma L yields a common locally \(L^2\) \(f\) with \(\int|f|^2e^{2\eta x}dx\leq M\) for every \(\eta<0\). Along \(\eta\to-\infty\), Fatou forces \(f=0\) almost everywhere on \(x<0\): the integrand tends to infinity at every such point where \(f\ne0\). Along \(\eta\uparrow0\), Fatou then gives \(\int_0^\infty|f|^2dx\leq M\). The forward construction for this \(f\) has the same completed transform on every slice. Both representatives are continuous in the real coordinate; equality almost everywhere on that slice is therefore equality everywhere. This proves the whole representation, the exact norm and the recovered trace without assuming any boundary value in advance. \(\square\)

The pulse calculation explains the converse: a fixed negative point is amplified without bound as the height tends to minus infinity. Fatou's lemma turns that observation into an almost-everywhere support statement even when no pointwise boundary function was given. Delaying a one-sided input changes the norm by an exponential factor; Exercise 2 derives that modified condition with either sign of delay.

## B. Two weighted endpoints of a finite strip

**Theorem B.** Let \(a_1<a_2\) be finite real numbers. If \(f e^{a_jx}\in L^2(\mathbb R)\), \(j=1,2\), its Fourier–Laplace integral is holomorphic in \(a_1<\operatorname{Im}z<a_2\) and

\[
\begin{gathered}
\sup_{a_1<\eta<a_2}(2\pi)^{-1}\|F_\eta\|_2^2\\
=\max_{j=1,2}\int|f(x)|^2e^{2a_jx}\,dx.
\end{gathered}
\tag{B1}
\]

Every holomorphic function in that strip with finite left side has one such representation. At either endpoint its slices converge strongly to the completed transform of \(f e^{a_jx}\).

**Proof.** On \(x\geq0\), write \(|f|e^{\eta x}=|f|e^{a_2x}e^{-(a_2-\eta)x}\); on \(x<0\), use \(|f|e^{a_1x}e^{(\eta-a_1)x}\). Cauchy–Schwarz on these half-lines proves absolute integrability of the Fourier–Laplace kernel and all its derivatives, uniformly on compact substrips. It also proves holomorphy by differentiation under the integral. Put \(N(\eta)=\int |f|^2e^{2\eta x}dx\). For \(\eta=(1-t)a_1+ta_2\), \(0<t<1\), scalar convexity of the real exponential gives

\[
\begin{gathered}
N(\eta)\leq(1-t)N(a_1)+tN(a_2)\\
\leq\max(N(a_1),N(a_2)).
\end{gathered}
\tag{B2}
\]

The integrable majorant \(|f|^2(e^{2a_1x}+e^{2a_2x})\) gives \(N(\eta)\to N(a_j)\) at either endpoint. It also dominates \(|f|^2|e^{\eta x}-e^{a_jx}|^2\) up to a fixed factor, giving strong weighted \(L^2\) convergence. Plancherel proves (B1) and both trace statements.

Conversely, if the left side is \(M<\infty\), Lemma L constructs \(f\) with \(N(\eta)\leq M\) throughout the strip. Taking sequences of heights to either endpoint and using Fatou gives \(N(a_1),N(a_2)\leq M\). The forward integral is therefore defined. Its completed slice transforms equal those of the given function by Lemma L, hence their continuous real-coordinate representatives agree everywhere. The forward proof now gives the exact equality and the endpoint traces. \(\square\)

The finite strip controls exponential tails rather than a hard support cutoff. Its norm need not be largest at the midpoint or have equal endpoint values. Theorem B gives the exact endpoint maximum; the two-tail input in Exercise 3 makes the asymmetry explicit. We now use the same height dependence in a different direction: the input will be determined by an equation relating two boundary observations.

## C. A strip function with two boundary poles

**Theorem C.** There is exactly one holomorphic \(F\) on \(|\operatorname{Im}z|<1\) for which \((1+z^2)F(z)\) is bounded on the whole strip and whose distributional traces satisfy

\[
\begin{gathered}
F(x+i-i0)\\
+F(x-i+i0)=\delta_0.
\end{gathered}
\tag{C1}
\]

It is

\[
\begin{gathered}
F(z)=\frac1{4\cosh(\pi z/2)},\\
\mathcal F(F|_{\mathbb R})(\xi)\\
=\frac1{e^\xi+e^{-\xi}}.
\end{gathered}
\tag{C2}
\]

**Proof.** First consider any function with the boundedness condition. Every closed substrip has \(|F(x+iy)|\leq C_K/(1+x^2)\), hence uniformly bounded horizontal \(L^1\) and \(L^2\) norms. Near either edge it has local bound \(C(1-|y|)^{-1}\), since \(1+z^2=(z-i)(z+i)\). U013, Theorem3.1 and Corollary3.2, with \(N=1\), shifted to either edge and with its lower-side version, supplies both local traces and uniform compact \(C^2\) bounds. For \(|x|\geq2\) the bound \(C'/x^2\) is uniform all the way to either edge. Splitting a Schwartz test into a compact piece near zero and its complement therefore gives actual convergence in \(\mathcal S'\), and finite Schwartz seminorm bounds, for both traces.

Let \(G_y=\mathcal F_x(F(x+iy))\) and \(G=G_0\). Lemma L, followed by reflection and the inverse factor, gives
\(G_y(\xi)=e^{-y\xi}G(\xi)\) on every interior slice. This identity also follows directly from \(\partial_yG_y=-\xi G_y\); its solution is justified on compact frequency tests exactly as in (L4). Here \(G\) is a bounded continuous function because \(F_0\in L^1\). Fourier continuity on \(\mathcal S'\), and then restriction to compact frequency tests, give
\(\widehat{F_+}=e^{-\xi}G\) and \(\widehat{F_-}=e^\xi G\).
Condition (C1) consequently forces

\[
\begin{gathered}
(e^\xi+e^{-\xi})G(\xi)=1.
\end{gathered}
\tag{C3}
\]

The smooth strictly positive multiplier never vanishes; on compact frequency sets it can be divided. Thus \(G=(e^\xi+e^{-\xi})^{-1}\), first as a distribution and then pointwise by continuity. Fourier injectivity proves uniqueness of the real slice. The difference of two candidates has every real derivative zero at a real point; holomorphy makes these its complex Taylor derivatives. U015, Section3, gives the complete Cauchy/Taylor construction and hence an open zero set, and its Lemma 3.1 gives uniqueness throughout the connected strip.

For existence take the first expression in (C2). The identity
\[
\begin{gathered}
|\cosh(\pi(x+iy)/2)|^2\\
=\sinh^2(\pi x/2)+\cos^2(\pi y/2)
\end{gathered}
\]
shows it is holomorphic inside the strip. It decays uniformly exponentially for large \(|x|\). At the two boundary zeros \(z=\pm i\), the numerator \(1+z^2\) cancels the simple zero; the resulting quotient extends continuously on the remaining compact closed strip. Hence the required product is bounded.

Its residues at \(i\) and \(-i\) are respectively \((2\pi i)^{-1}\) and \(-(2\pi i)^{-1}\), by differentiating \(4\cosh(\pi z/2)\). Locally subtract these actual simple poles. The remainders extend smoothly across the relevant edge, so their traces are ordinary functions there. The singular sum is

\[
\begin{gathered}
\frac1{2\pi i}\left(\frac1{x-i0}-\frac1{x+i0}\right)\\
=\delta_0,
\end{gathered}
\tag{C4}
\]

by U013, Theorem4.1, with both signs retained. Away from zero the two traces are \((4i\sinh(\pi x/2))^{-1}\) and its negative. The sum of the regular remainders is therefore zero off zero and, by continuity near zero, zero also at zero. Thus (C1) holds. Equation (C3), already justified for every eligible function, now gives its whole Fourier transform in (C2). No unproved contour evaluation of the hyperbolic secant is needed. \(\square\)

## Exercises

**Exercise 1 (foundation: a boundary need not be an ordinary integral).** Let \(1/2<\alpha\leq1\) and \(f(x)=1_{(0,\infty)}(x)(1+x)^{-\alpha}\). Determine its lower-half-plane square-integral norm, prove a pointwise interior bound, and decide whether its boundary transform at zero is an absolutely convergent integral or even a finite limit along the imaginary axis.

**Exercise 2 (intermediate: the exact delayed support).** Fix \(s\in\mathbb R\). Characterize the holomorphic lower-half-plane functions for which
\(\sup_{\eta<0}e^{-2s\eta}(2\pi)^{-1}\|F_\eta\|_2^2<\infty\).
For \(a>0\) compute the transform and every slice norm of \(f_s(x)=1_{[s,\infty)}(x)e^{-a(x-s)}\). Keep negative delays as well as positive ones.

**Exercise 3 (foundation: two different exponential tails).** Let \(p,r>0\) and
\(f(x)=e^{-px}\) for \(x\geq0\), \(f(x)=e^{rx}\) for \(x<0\). Determine its maximal open Fourier–Laplace strip and its entire horizontal norm profile. For finite \(-r<a_1<a_2<p\), give the exact strip supremum and its endpoint traces.

**Exercise 4 (advanced: strictly log-convex strip norms).** For a nonzero input in Theorem B, prove
\(N((1-t)a_1+ta_2)<N(a_1)^{1-t}N(a_2)^t\) for \(0<t<1\), where \(N(\eta)=\int|f|^2e^{2\eta x}dx\). Prove the strictness rather than invoking an unproved equality case of Hölder.

**Exercise 5 (intermediate: a pole of any order above the boundary).** Let \(z_0=\gamma+i\beta\), \(\beta>0\), and let \(m\geq1\) be an integer. Find the positive-half-line input for \(F(z)=(z-z_0)^{-m}\), and determine its exact squared norm and every slice norm. Justify the factorial integral with complex parameter.

**Exercise 6 (intermediate: an arbitrary strip width).** For \(h>0\), find the unique holomorphic \(F_h\) on \(|\operatorname{Im}z|<h\) with bounded \((h^2+z^2)F_h\) and boundary sum \(F_h(x+ih-i0)+F_h(x-ih+i0)=\delta_0\). Compute its whole real-line Fourier transform with the original delta normalization.

**Exercise 7 (advanced: a positive kernel hidden in the boundary sum).** For \(0<\varepsilon<1\), put \(s=\sin(\pi\varepsilon/2)\) and
\[
\begin{gathered}
K_\varepsilon(x)=\frac1{4\cosh(\pi(x+i(1-\varepsilon))/2)}\\
+\frac1{4\cosh(\pi(x-i(1-\varepsilon))/2)}.
\end{gathered}
\]
Prove positivity and mass one, compute the mass outside \([-\delta,\delta]\), and give an explicit approximate-identity error for every bounded uniformly continuous test.

**Exercise 8 (foundation: why the whole-strip bound is needed).** Show that the boundary-sum condition of Theorem C alone does not give uniqueness in \(\mathcal D'\). Exhibit a two-parameter entire homogeneous family that can be added to its solution, and prove that the bounded-product condition eliminates every nonzero member of that family.

**Exercise 9 (intermediate: connected heights with a hole).** In two dimensions take \(f(x)=e^{-|x|^2/2}\) and restrict its transform to heights \(1<|\eta|<2\). Recover its unique common input and extend to its finite-moment tube. Then show by an explicit one-dimensional example why one common input can fail for disconnected heights despite all local norm bounds.

**Exercise 10 (advanced: covariance with a coupled Gaussian).** Let
\[
\begin{gathered}
M=\begin{pmatrix}2&1\\1&2\end{pmatrix},\\
f(x)=e^{-x^TMx/2}.
\end{gathered}
\tag{T13}
\]
Compute \(F(z)\), \(N(\eta)\), the mean vector and every entry of the covariance matrix. Verify the exact slice Plancherel constant and strict log-convexity in all directions.

**Exercise 11 (intermediate: a finite boundary norm without an ordinary boundary integral).** For \(a>0\) and \(1/2<\alpha\le1\), take \(f(x)=e^{-ax}(1+x)^{-\alpha}\mathbf1_{(0,\infty)}(x)\). Determine \(E\) exactly and calculate \(N(a)\). Prove strong completed square-integral convergence as \(\eta\uparrow a\), while the ordinary Fourier–Laplace integral at boundary frequency zero diverges.

## Solutions

**Solution 1.** Direct integration gives
\(\|f\|_2^2=\int_0^\infty(1+x)^{-2\alpha}dx=(2\alpha-1)^{-1}\).
Theorem A therefore gives exactly that supremum and limiting squared norm, with the inverse factor \((2\pi)^{-1}\). At height \(\eta<0\), Cauchy–Schwarz gives
\[
\begin{gathered}
|F(\xi+i\eta)|\leq\frac1{\sqrt{2\alpha-1}\sqrt{-2\eta}}.
\end{gathered}
\]
The integral defining \(F(0)\) would be \(\int_0^\infty(1+x)^{-\alpha}dx\), which diverges for all the stated \(\alpha\), logarithmically at \(\alpha=1\). Since the integrand of \(F(i\eta)\) is positive and increases to that nonintegrable function as \(\eta\uparrow0\), monotone convergence gives \(F(i\eta)\to+\infty\). The strong \(L^2\) boundary supplied by Theorem A still exists. A square-integrable boundary class does not require a finite point value at this one frequency.

**Solution 2.** Apply Theorem A to \(H(z)=e^{isz}F(z)\). Its horizontal squared norm is exactly \(e^{-2s\eta}\|F_\eta\|_2^2\), since \(|e^{is(\xi+i\eta)}|=e^{-s\eta}\). Thus \(H=\widehat g\) for one \(g\in L^2((0,\infty))\). Translation gives
\(F(z)=e^{-isz}H(z)=\int_s^\infty e^{-ixz}g(x-s)dx\).
Conversely every \(L^2\) input supported in \([s,\infty)\) has this form and the modified supremum is its exact squared norm. This covers negative \(s\); in that case the unmodified supremum need not be finite.

For the displayed exponential input substitute \(x=s+t\):
\[
\begin{gathered}
F_s(z)=\frac{e^{-isz}}{a+iz},\\
(2\pi)^{-1}\|F_{s,\eta}\|_2^2\\
=\frac{e^{2s\eta}}{2(a-\eta)},\\
\|f_s\|_2^2=\frac1{2a}.
\end{gathered}
\]
The ordinary integral converges throughout the lower half-plane. The norm formula follows either by Plancherel applied to the actual weighted input or by integrating \(((a-\eta)^2+\xi^2)^{-1}\). The modified supremum is \(1/(2a)\), attained as a limit of heights to zero.

**Solution 3.** On the positive half-line the absolute kernel is \(e^{-(p-\eta)x}\), and on the negative half-line it is \(e^{(r+\eta)x}\). Both are integrable exactly for \(-r<\eta<p\). In that strip,
\[
\begin{gathered}
F(z)=\frac1{p+iz}+\frac1{r-iz},\\
N(\eta)=\frac1{2(p-\eta)}+\frac1{2(r+\eta)}.
\end{gathered}
\]
The two tails occupy disjoint half-lines, so no cross term occurs in the input norm. Plancherel fixes \((2\pi)^{-1}\|F_\eta\|_2^2=N(\eta)\). At either extreme \(\eta=p\) or \(\eta=-r\), one squared tail has infinite integral, and the corresponding rational function has its actual pole on that boundary. Thus neither weighted square-integral range nor its absolutely defined Laplace strip extends through these extremes. On the chosen finite substrip, Theorem B gives the exact supremum \(\max(N(a_1),N(a_2))\) and strong endpoint traces \(\mathcal F(f e^{a_jx})\). No assumption that the two endpoint norms are equal is made.

**Solution 4.** Set \(d\nu=|f|^2e^{2a_1x}dx/N(a_1)\), a probability measure, and \(X=e^{2(a_2-a_1)x}\). Then
\(N((1-t)a_1+ta_2)/N(a_1)=\int X^t d\nu\) and \(\int Xd\nu=N(a_2)/N(a_1)=:\mu\), with \(0<\mu<\infty\). The scalar derivative \(tX^{t-1}\) is strictly decreasing for \(0<t<1\). Integrating that derivative between \(\mu\) and \(X\) proves the tangent bound
\[
\begin{gathered}
X^t\leq\mu^t+t\mu^{t-1}(X-\mu),
\end{gathered}
\]
with equality only at \(X=\mu\). Integrating gives the desired non-strict log-convex estimate. Equality would make its nonnegative difference zero \(\nu\)-almost everywhere, forcing \(X=\mu\) there. Since \(a_2>a_1\), this confines \(f\) to a single real point, a Lebesgue null set. A nonzero \(L^2\) input cannot have that support, so the estimate is strict.

**Solution 5.** For \(\operatorname{Re}a>0\), integration by parts, with its exponentially vanishing upper endpoint, gives
\(\int_0^\infty x^k e^{-ax}dx=k!a^{-k-1}\), starting from \(\int e^{-ax}dx=a^{-1}\) and then inducting. This is valid for complex \(a\), because both the original integrals and their boundary terms are absolutely controlled by \(x^ke^{-\operatorname{Re}a\,x}\). Take \(a=i(z-z_0)\); its real part is \(\beta-\operatorname{Im}z>0\) on the lower half-plane. The input is therefore
\[
\begin{gathered}
f(x)=1_{(0,\infty)}(x)\\
\frac{i^m}{(m-1)!}x^{m-1}e^{iz_0x}.
\end{gathered}
\]
The integral formula gives exactly \((z-z_0)^{-m}\), including the power of \(i\). Since \(|e^{iz_0x}|=e^{-\beta x}\),
\[
\begin{gathered}
\|f\|_2^2=\frac{(2m-2)!}{((m-1)!)^2(2\beta)^{2m-1}},\\
(2\pi)^{-1}\|F_\eta\|_2^2\\
=\frac{(2m-2)!}{((m-1)!)^2[2(\beta-\eta)]^{2m-1}}.
\end{gathered}
\]
These norms are finite for every lower height and have the exact boundary supremum. The real part \(\gamma\) only modulates the input and shifts the real frequency; it does not alter any norm.

**Solution 6.** Let \(F_1\) be Theorem C's solution and set \(F_h(z)=h^{-1}F_1(z/h)\). Then
\[
\begin{gathered}
F_h(z)=\frac1{4h\cosh(\pi z/(2h))},\\
\widehat{F_h|_{\mathbb R}}(\xi)=\frac1{2\cosh(h\xi)}.
\end{gathered}
\]
The Fourier formula follows by the actual real substitution \(x=ht\), whose factor \(h\) cancels the prefactor \(h^{-1}\). The bounded-product condition transforms to \(h(1+(z/h)^2)F_1(z/h)\), so it is bounded. The boundary sum transforms to \(h^{-1}\delta_0(x/h)=\delta_0(x)\): testing and making that same substitution retains the unit delta mass. Conversely any eligible width-\(h\) function gives the width-one function \(hF_h(hw)\), with the same unit boundary delta. Theorem C gives uniqueness, so the displayed scaling is the whole answer.

**Solution 7.** Put \(\theta=\pi\varepsilon/2\). Adding the two conjugate denominators gives the real formula
\[
\begin{gathered}
K_\varepsilon(x)\\
=\frac{s\cosh(\pi x/2)}{2[\sinh^2(\pi x/2)+s^2]}>0.
\end{gathered}
\]
Use \(r=\sinh(\pi x/2)\), so \(dr=(\pi/2)\cosh(\pi x/2)dx\). Then
\(K_\varepsilon(x)dx=\pi^{-1}s(r^2+s^2)^{-1}dr\), which has mass one. For \(R=\sinh(\pi\delta/2)>0\), its outside mass is exactly
\[
\begin{gathered}
1-\frac2\pi\arctan(R/s)\\
=\frac2\pi\arctan(s/R)\leq\frac{2s}{\pi R}.
\end{gathered}
\]
The arctangent identity holds for positive arguments and follows by their complementary angles; its upper bound follows by integrating \((1+t^2)^{-1}\leq1\) from zero. If \(\omega_\psi(\delta)=\sup_{|x|\leq\delta}|\psi(x)-\psi(0)|\), split the mass into the inside and outside parts to get
\[
\begin{gathered}
\left|\int K_\varepsilon\psi-\psi(0)\right|\\
\leq\omega_\psi(\delta)\\
+\frac{4s\|\psi\|_\infty}{\pi\sinh(\pi\delta/2)}.
\end{gathered}
\]
For fixed \(\delta\) the second term tends to zero as \(\varepsilon\to0\); then uniform continuity lets \(\delta\to0\). This proves the delta limit as an actual positive approximate identity, with its exact error and mass.

**Solution 8.** For arbitrary complex \(a,b\), the entire function
\(H(z)=a e^{\pi z/2}+b e^{-\pi z/2}\) has upper and lower traces at heights \(\pm1\). Their sum is zero, since the two phase factors for each exponential are \(i\) and \(-i\). These ordinary smooth traces are distributions on compact tests, even though they grow exponentially on one side. Thus \(F_0+H\), where \(F_0\) is Theorem C's solution, has the same boundary sum for every \(a,b\). If \(a\ne0\), \((1+x^2)H(x)\) is unbounded as \(x\to+\infty\), since its growing term dominates the other. If \(a=0\) and \(b\ne0\), it is unbounded as \(x\to-\infty\). The exponentially decaying \(F_0\) cannot cancel either growth. Therefore the required bounded product forces \(a=b=0\) within this family. This exhibits failure of uniqueness when that hypothesis is removed; it does not assert that this two-parameter family exhausts all possible homogeneous functions.

**Solution 9.** In one dimension the Gaussian integral gives \(\sqrt{2\pi}e^{-z^2/2}\), and absolute Fubini in the two real coordinates gives
\[
\begin{gathered}
F(z)=2\pi e^{-(z_1^2+z_2^2)/2},\\
N(\eta)=\pi e^{|\eta|^2}.
\end{gathered}
\tag{T14}
\]
The integral is holomorphic at every complex point by Gaussian domination with all polynomial derivatives. The annulus is open and connected, though not convex. Its locally bounded norms satisfy Lemma L, which recovers this \(f\) uniquely by one slice. The actual moment domain is all \(\mathbb R^2\), so Theorem L.1 extends the function to all \(\mathbb C^2\), keeping \((2\pi)^{-2}\|F_\eta\|_2^2=N(\eta)\).

On the disconnected one-dimensional heights \((-2,-1)\cup(1,2)\), take \(F=0\) on the first tube and \(F(z)=e^{-z^2}\) on the second. This is holomorphic on the disjoint union. The second component has \(\|F_\eta\|_2^2=e^{2\eta^2}\sqrt{\pi/2}\), so local compact-height bounds hold. A common input would be zero by injectivity at a height in the first component, but its weighted transform at a height in the second would then be zero too, contradicting \(e^{-z^2}\ne0\). Each connected component can have its own input.

**Solution 10.** The orthogonal coordinates \(s=(x_1+x_2)/\sqrt2\), \(t=(x_1-x_2)/\sqrt2\) have Jacobian of absolute value one and give \(x^TMx=3s^2+t^2\). Thus \(\det M=3\) and
\[
\begin{gathered}
M^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\\
F(z)=\frac{2\pi}{\sqrt3}
e^{-z^TM^{-1}z/2},\\
N(\eta)=\frac{\pi}{\sqrt3}e^{\eta^TM^{-1}\eta}.
\end{gathered}
\tag{T15}
\]
The two one-dimensional Gaussian integrals prove both formulas, initially on real frequencies and then at all complex frequencies by local Gaussian domination and the identity principle. The square in the weighted input is
\[
\begin{gathered}
y=x-M^{-1}\eta,\\
-x^TMx+2\eta^Tx\\
=-y^TMy+\eta^TM^{-1}\eta.
\end{gathered}
\tag{T16}
\]
It follows that \(m_\eta=M^{-1}\eta\) and
\[
\begin{gathered}
\operatorname{Cov}_{\mu_\eta}(x)
=\tfrac12M^{-1},\\
\tfrac12M^{-1}
=\frac16\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\\
\nabla\log N=2M^{-1}\eta,\\
\operatorname{Hess}\log N=2M^{-1}.
\end{gathered}
\tag{T17}
\]
The diagonal covariance entries are \(1/3\), and both off-diagonal entries are \(-1/6\). In the two orthogonal directions the covariance eigenvalues are \(1/6\) and \(1/2\), so the Hessian eigenvalues are \(2/3\) and \(2\); both are positive.

For a direct normalization check, \(|F(\xi+i\eta)|^2=(4\pi^2/3)e^{-\xi^TM^{-1}\xi+\eta^TM^{-1}\eta}\). Its real-frequency Gaussian integral is \(\pi\sqrt3\). Therefore
\[
\begin{gathered}
\|F_\eta\|_2^2\\
=\frac{4\pi^3}{\sqrt3}e^{\eta^TM^{-1}\eta}\\
=(2\pi)^2N(\eta),
\end{gathered}
\tag{T18}
\]
with every factor retained. These formulas verify the full coupled covariance, rather than just the two marginal variances.

**Solution 11.** The weighted square norm is \(\int_0^\infty e^{-2(a-\eta)x}(1+x)^{-2\alpha}dx\). It is finite for \(\eta<a\) by exponential decay. At \(\eta=a\), elementary integration gives \(N(a)=(2\alpha-1)^{-1}<\infty\). For \(\eta>a\), exponential growth dominates the negative power: take logarithms to see \(2(\eta-a)x-2\alpha\log(1+x)\to+\infty\). The integrand eventually exceeds one, so its integral diverges. Hence
\[
\begin{gathered}
E=(-\infty,a],\\
\operatorname{int}E=(-\infty,a).
\end{gathered}
\tag{T19}
\]
For heights increasing to \(a\), the weighted inputs converge in \(L^2\) to \((1+x)^{-\alpha}\mathbf1_{(0,\infty)}\), since their squared difference is dominated by that integrable squared input and tends pointwise to zero. Completed Plancherel gives strong convergence of their Fourier slices to the completed boundary transform, with the original inverse factor \(1/(2\pi)\).

At zero real frequency the ordinary boundary integral is \(\int_0^\infty(1+x)^{-\alpha}dx\), which diverges for every stated \(\alpha\), including logarithmic divergence at \(\alpha=1\). The positive interior imaginary-axis integrals increase to it as \(\eta\uparrow a\), so their values tend to \(+\infty\). A finite completed square-integral boundary norm supplies no finite value at this single frequency; the absolutely convergent holomorphic integral is furnished on the interior heights.

## References

- Supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, and [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Lemma0.1: Schwartz Fourier inversion, Gaussian mass and transforms, transpose rules and Plancherel. Lemma0.1 of the present lesson proves the completed square-integral maps and their agreement with both distributional and ordinary transforms.
- Supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and16, and the scalar and finite-algebra foundations named above: complete measure, convergence, Jacobian, norm, density and matrix proofs. Lemma L uses scalar Cauchy–Schwarz and Tonelli to establish every analytic-slice norm estimate. These copies retain their stated licences.
- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem1.1, Corollary2.2, Theorem3.1, Corollary3.2 and Theorem4.1. [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section3 and Lemma3.1: exact Cauchy, boundary, jump and identity proofs.
- Charles J. Geyer, [*Stat 5421 Lecture Notes: Exponential Families*](https://www.stat.umn.edu/geyer/5421/notes/expfam.html), edition dated20August2026, Sections3.5–3.6 and4: finite natural-parameter domains and mean/covariance interpretations. The notes state [CC BY-SA4.0](https://creativecommons.org/licenses/by-sa/4.0/). The Fourier–Laplace domination, strict covariance and support proofs here are independently written and proved in full.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises7.4.1–7.4.3, printed pages390–391, and answers on page415. The common-slice, finite-moment-domain, covariance and support arguments, worked measurements and eleven graded exercises here have their own exposition; the boundary-pole existence proof uses the proved jump formula.
