# Analytic forcing without global analytic solutions

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A right-hand side can be analytic at every real point and still admit no analytic solution on the whole space. We will see this for a heat equation with two spatial variables and for a two-variable Laplacian with an extra parameter. In both cases a smooth solution exists. The obstacle is the analytic dependence that a solution would have to retain while its forcing moves farther into space.

Assume smooth functions, convergent power series and the Cauchy integral formula. The [complete proof](analytic-forcing-without-global-analytic-solutions-formal.md) supplies the Gaussian identities, spatial continuation of homogeneous solutions, infinite-series estimates and the contradiction. Basic references are E. De Giorgi's *Solutions analytiques des équations aux dérivées partielles à coefficients constants*, L. C. Piccinini's work on analytic nonsurjectivity, and Compact Fourier division and multiplicity-sensitive annihilators. The latter gives a useful comparison with distributional solvability; it does not replace the analytic arguments here. Credit for the counterexamples and the localized-frequency method belongs to De Giorgi, Lamberto Cattabriga and Piccinini.

## 1. The two equations and the conclusion

On \(\mathbb R^3\), with coordinates \(x,y,t\), consider
\[
 P_0=\partial_x^2+\partial_y^2,\qquad
 P_1=\partial_x^2+\partial_y^2+\partial_t.
 \tag{E1.1}
\]
The variable \(t\) is an analytic parameter for \(P_0\). Reversing time changes \(P_1\) to the forward heat sign.

**Theorem 1.1.** There is a globally real analytic forcing \(f\) such that neither \(P_0u=f\) nor \(P_1u=f\) has a globally real analytic solution. Each equation has a global smooth solution. The forcing may be chosen real valued.

Here “globally real analytic” means analytic near every real point, with a neighborhood allowed to depend on the point. It does not mean an entire extension to all complex space. The dimension is part of the theorem. We use two spatial variables and one time or parameter variable; this is not a counterexample for a heat equation with just one spatial variable.

Theorem 1.1 in the complete proof constructs a specific complex-valued \(f\). One of the three real-valued functions \(\operatorname{Re}f,\operatorname{Im}f,\operatorname{Re}f+\operatorname{Im}f\) defeats both operators. The proof does not identify which of these three it is.

## 2. Analytic sources with much longer solution tails

Choose positive integers \(h,k\). They label a spatial center \(h\) and a frequency \(q=q_{hk}\). Set
\[
 d=h+k-2,\qquad
 n_{hk}=3+\frac{d(d+1)}2+h,\qquad
 q_{hk}=(n_{hk}!)!.
 \tag{E2.1}
\]
The labels \(n_{hk}\) run through all integers at least four once. The successive frequencies are extremely far apart. This will let a high derivative distinguish one mode from all the others.

Define
\[
 f_{hk}(x,y,t)=e^{q[ix+ih^2t-(y-h)^2-1]},\qquad
 f=\sum_{h,k\ge1}f_{hk}.
 \tag{E2.2}
\]
The forcing is concentrated near \(y=h\). At \(y=0\) its absolute size is \(e^{-q(h^2+1)}\). A small imaginary change in \(t\) produces the factor \(e^{-h^2q\operatorname{Im}t}\). The quadratic spatial suppression still protects a complex neighborhood of every real compact set, so the sum is analytic. Lemma 2.2 of the complete proof gives explicit neighborhood widths.

A smooth particular solution of each mode has the form
\[
 w_{hk}^{\varepsilon}(x,y,t)
     =e^{iqx+ih^2qt}W_{h,q}^{\varepsilon}(y),
 \qquad
 \kappa^2=q^2-i\varepsilon h^2q,\quad
 \operatorname{Re}\kappa>0,
 \tag{E2.3}
\]
where \(\varepsilon=0,1\). The one-dimensional Green kernel gives
\[
 W_{h,q}^{\varepsilon}(y)
    =-\frac{e^{-q}}{2\kappa}
       \int_{\mathbb R}e^{-\kappa|y-s|}e^{-q(s-h)^2}\,ds.
 \tag{E2.4}
\]
The negative sign is necessary: the derivative of this Green kernel has jump 1. Its second derivative minus \(\kappa^2\) times itself is a point mass.

The real particular solution is tiny: \(|W|\le e^{-q}q^{-2}\). The sum \(w^\varepsilon=\sum w_{hk}^\varepsilon\) converges with every real derivative and solves the equation smoothly. But at the origin the distant tail has the asymptotic size
\[
 |W_{h,q}^{\varepsilon}(0)|
       \sim\frac{\sqrt\pi}{2q^{3/2}}e^{-q(h+3/4)}
       \quad(q\to\infty,\ h\text{ fixed}).
 \tag{E2.5}
\]
This is much larger than the original forcing's \(e^{-q(h^2+1)}\) there. The integral is dominated near \(s=h-1/2\); completion of the square supplies the constant \(3/4\). Lemma 3.2 includes the phase for the heat operator and bounds the discarded endpoint terms.

The [figure in the complete proof](analytic-forcing-without-global-analytic-solutions-formal.md) shows exact single-mode profiles and their complex-time growth scales. The plotted finite frequencies illustrate the mode family; the proof uses the full lacunary frequencies in (E2.1).

## 3. Why a different homogeneous solution cannot repair analyticity

Finding one particular solution that fails to be analytic would not finish the argument. Another solution could differ from it by a homogeneous solution. We must control every such difference.

**Spatial extension fact.** If \(v\) is a global smooth solution of either homogeneous equation, then for every \(R>0,p>0\),
\[
 |\partial_x^a v(0,0,t)|\le C_{p,R}a!R^{-a}
       \quad(a\ge0,\ |t|\le p).
 \tag{E3.1}
\]
For the Laplacian, the Poisson formula on arbitrarily large spatial circles gives this estimate. For the heat operator, cut the solution off on a large spatial ball and use the heat kernel over one unit of reversed time. The cutoff error stays far from the origin. At a complex spatial coordinate of modulus at most \(R\), the Gaussian still has a positive distance exponent, so its integral is holomorphic and bounded. Cauchy's formula gives (E3.1). Lemma 4.1 proves both cases with no growth condition at infinity. The constant can depend on \(R\); the radius can be chosen arbitrarily large.

Now test a candidate solution with
\[
 B_{h,q}(a)=\int_{-p}^{p}\partial_x^q a(0,0,t)
       e^{-h^2q(t^2/(2p)+it)}\,dt.
 \tag{E3.2}
\]
For the selected particular mode, the time oscillations cancel. Its normalized logarithm has the limit
\[
 \frac{\log|B_{h,q}(w_{hk}^\varepsilon)|}{q}-\log q
       \longrightarrow-h-\frac34.
 \tag{E3.3}
\]
Every other mode is negligible on this scale, because of the gaps between successive frequencies. For a homogeneous solution, (E3.1) gives an upper limit at most \(-1-\log R\) for every \(R\); allowing \(R\) to grow gives upper limit \(-\infty\).

An analytic candidate \(u\) near the origin has a positive complex neighborhood width \(p\). Move the time integral down to imaginary height \(-p\). On the lower side and both vertical sides, the weight gains at least \(e^{-h^2qp/2}\). The Cauchy bound on the \(x\) derivative then gives
\[
 \limsup_{k\to\infty}
 \left(\frac{\log|B_{h,q}(u)|}{q}-\log q\right)
      \le-1-\log p-\frac{h^2p}{2}.
 \tag{E3.4}
\]
For sufficiently large \(h\), this is strictly smaller than (E3.3). If \(u\) were a global analytic solution, \(w^\varepsilon-u\) would be a global smooth homogeneous solution. The selected tail would then be the sum of the analytic candidate's contribution, a negligible homogeneous contribution, and negligible other tails. Their sizes contradict (E3.3). The complete proof supplies all four estimates and this exact decomposition.

## 4. Four worked examples

**Example 1. An explicit separating center.** Suppose the complex neighborhood of an assumed analytic candidate permits \(p=1/4\). Take \(h=12\). The selected-tail limit is \(-12-3/4=-51/4\), whereas the candidate's upper bound is
\[
 -1-\log(1/4)-12^2/8=\log4-19<-17.
 \tag{E4.1}
\]
We used \(\log4<2\). Thus the candidate decays strictly faster on the testing scale. This is a conditional choice of \(p\), not a claim that every analytic function has that width. For any positive width, the positive quadratic term in \(h\) eventually gives the same separation.

**Example 2. Entire spatial behavior without boundedness.** The function \(v(x,y,t)=e^{x-t}\) solves \(P_1v=0\) and is unbounded as \(x\to+\infty\). Nevertheless
\[
 |\partial_x^a v(0,0,t)|=e^{-t}\le e^p
       \le e^{p+R}a!R^{-a}\quad(|t|\le p).
 \tag{E4.2}
\]
The last inequality is a single term of \(e^R=\sum_{j\ge0}R^j/j!\). Thus the spatial extension estimate permits unbounded homogeneous solutions. The constant grows with the radius, which is harmless because the derivative order tends to infinity after the radius is fixed.

**Example 3. Every finite partial sum has an entire solution.** Fix a mode and \(\varepsilon\). Its equation in \(y\) is \(W''-\kappa^2W=e^{-q}e^{-q(y-h)^2}\). With any initial constants \(c_0,c_1\), an entire solution is
\[
 W(y)=c_0\cosh(\kappa y)+\frac{c_1}{\kappa}\sinh(\kappa y)
       +\frac{e^{-q}}{\kappa}\int_0^y
           \sinh(\kappa(y-s))e^{-q(s-h)^2}\,ds.
 \tag{E4.3}
\]
The integral is entire: write \(s=\tau y\), \(0\le\tau\le1\), and integrate the locally uniformly convergent power series in \(y\). Differentiate twice to verify the equation and its initial values. Multiplication by \(e^{iqx+ih^2qt}\) gives an entire mode solution. A finite sum therefore has an entire solution too. The infinite forcing is different: convergence of every real derivative does not imply convergence on a complex neighborhood for the particular-solution sum.

**Example 4. The protective distance in the heat kernel.** In Lemma 4.1 take \(R=2\). The cutoff error is supported at spatial distance at least \(8\). For \(|z|\le2\),
\[
 \operatorname{Re}((z-Y_1)^2+Y_2^2)\ge(8-2)^2-2^2=32,
 \quad
 |G_\tau((z,0)-Y)|\le(4\pi\tau)^{-1}e^{-8/\tau}.
 \tag{E4.4}
\]
The latter is integrable as \(\tau\downarrow0\), even after multiplication by any fixed inverse power of \(\tau\). It protects holomorphy of the cutoff-error integral. Taking larger \(R\) gives arbitrarily large complex spatial discs while using only compact real space-time regions.

## 5. Exercises and full solutions

Exercises 1–4 are worth 10 points each. Exercises 5–8 are worth 15 points each, for a total of 100 points.

### Exercise 1. A diagonal enumeration and factorial gaps — 10 points

List the pairs \((h,k)\) giving labels \(n=4,\ldots,9\). Prove \(q_{n+1}\ge q_n^{n+1}\) without expanding the enormous factorials.

**Solution.** The pairs in order are \((1,1),(1,2),(2,1),(1,3),(2,2),(3,1)\). Their diagonals have lengths \(1,2,3\), giving the labels \(4\), \(5,6\), \(7,8,9\). For \(m=n!\), the quotient \(((n+1)m)!/(m!)^{n+1}\) is the multinomial coefficient counting divisions into \(n+1\) labeled blocks of size \(m\). It is a positive integer, hence at least 1. This is exactly \(q_{n+1}/q_n^{n+1}\). Award 4 points for the pairs and 6 for the factorial argument.

### Exercise 2. A complex neighborhood of a real box — 10 points

For a real box with \(|y|\le1\), use \(H=12\) and the widths in Lemma 2.2. Bound the real part of \(ix+ih^2t-(y-h)^2-1\) for \(h\le12\) and for \(h>12\), and explain why its mode sum is holomorphic there.

**Solution.** Enlarge to \(|\operatorname{Re}y|\le2\), take \(|\operatorname{Im}x|,|\operatorname{Im}y|<1/8\), and \(|\operatorname{Im}t|<1/(8\cdot12^2)\). For \(h\le12\) the real part is at most
\[
 -1+\frac18+\frac18+\frac1{64}=-\frac{47}{64}<-\frac12.
 \tag{E5.1}
\]
For \(h>12\), \(|h-\operatorname{Re}y|\ge3h/4\), and the possible time growth is at most \(h^2/8\). The real part is at most \(-1+1/8+1/64-7h^2/16<-1/2\). Thus each mode has modulus at most \(e^{-q_{hk}/2}\). Since the labels are bijective and \(q_n\ge n\), their sum is dominated by a convergent geometric series. Uniform convergence on compact subsets passes the Cauchy formulas to the sum and gives its holomorphy. Award 4 points for the first bound, 3 for the large-center bound, and 3 for convergence and holomorphy.

### Exercise 3. The Green-kernel sign — 10 points

Show that \(-e^{-\kappa|y|}/(2\kappa)\), with \(\operatorname{Re}\kappa>0\), is a Green kernel for \(\partial_y^2-\kappa^2\). Derive the value of \(\kappa^2\) needed for the heat mode in (E2.3).

**Solution.** On \(y>0\) its first derivative is \(e^{-\kappa y}/2\); on \(y<0\) it is \(-e^{\kappa y}/2\). Its jump is 1. The function itself is continuous, so its distributional second derivative is its ordinary second derivative off zero plus \(\delta_0\), with no derivative of a point mass. Off zero the second derivative equals \(\kappa^2\) times the function. Thus the asserted Green equation holds. On \(e^{iqx+ih^2qt}W(y)\), the \(x\) second derivative contributes \(-q^2W\), and the time derivative contributes \(ih^2qW\). Hence the remaining equation is \(W''-(q^2-ih^2q)W=e^{-q}e^{-q(y-h)^2}\). Award 6 points for the jump and distributional equation, and 4 for the heat sign.

### Exercise 4. Why the endpoint is negligible — 10 points

For \(h=1\), compare the full Gaussian saddle term in Lemma 3.2 with the two negative-half-line errors. Derive the limiting exponential rate of \(W_{1,q}^{\varepsilon}(0)\).

**Solution.** The full integral has modulus asymptotic to \(\sqrt{\pi/q}e^{-3q/4}\), since \(h-1/4=3/4\). Each endpoint error is \(O(q^{-1}e^{-q})\). Their ratio to the full integral is \(O(q^{-1/2}e^{-q/4})\), which tends to zero. Multiplication by \(e^{-q}/(2\kappa)\), with \(|\kappa|/q\to1\), gives
\[
 |W_{1,q}^{\varepsilon}(0)|
       \sim\frac{\sqrt\pi}{2q^{3/2}}e^{-7q/4},
 \qquad \frac{\log|W_{1,q}^{\varepsilon}(0)|}{q}\to-\frac74.
 \tag{E5.2}
\]
The heat phase has modulus one and does not alter this rate. Award 4 points for the two exponential orders, 3 for the relative error, and 3 for the final rate and prefactor.

### Exercise 5. Localizing the homogeneous heat solution — 15 points

Let \(V\) solve \((\partial_s-\Delta_X)V=0\), and let \(\chi\) be the spatial cutoff of Lemma 4.1. Derive the cutoff error \(Q\), its spatial support, and the complex Gaussian bound on \(|z|\le R\). Explain why this gives a spatial Cauchy estimate without an assumption at infinity.

**Solution.** The product rule gives
\[
 (\partial_s-\Delta_X)(\chi V)
       =-2\nabla\chi\cdot\nabla V-(\Delta_X\chi)V=Q.
 \tag{E5.3}
\]
Its support lies in \(4R\le|X|\le5R\), because both derivatives of \(\chi\) vanish elsewhere. For \(Y\) in that support and \(|z|\le R\), the real part of the Gaussian square is at least \((|Y|-|\operatorname{Re}z|)^2-|\operatorname{Im}z|^2\ge8R^2\). Thus \(|G_\tau|\le(4\pi\tau)^{-1}e^{-2R^2/\tau}\). This is integrable at zero; every fixed complex derivative remains integrable with its additional inverse powers. The Duhamel formula therefore extends the restriction at \(y=0\) holomorphically past the closed radius-\(R\) disc. The real solution and its first derivatives are bounded on the compact cutoff region and the fixed time interval, giving a constant \(C_{p,R}\). Cauchy's formula yields \(C_{p,R}a!R^{-a}\). The radius may be arbitrarily large, but the constant need not be independent of it. Award 4 points for the product rule and support, 5 for the Gaussian bound, and 6 for holomorphy, Cauchy's estimate and the role of compactness.

### Exercise 6. Moving the time contour — 15 points

Calculate the real part of \(t^2/(2p)+it\) on the bottom and vertical sides of the rectangle used in Lemma 5.4. Combine it with the Cauchy bound in \(x\) to estimate \(B_{h,q}(u)\). Identify the role of choosing \(h\) after \(p\).

**Solution.** For \(t=s-ip\) the real part is \(s^2/(2p)+p/2\). For \(t=\pm p-i\sigma\), \(0\le\sigma\le p\), it is \(p/2+\sigma-\sigma^2/(2p)\ge p/2\). The bottom length is \(2p\) and the two vertical lengths total \(2p\). Cauchy's formula bounds the derivative by \(Mq!p^{-q}\) on all three sides. The contour identity and the triangle inequality give
\[
 |B_{h,q}(u)|\le4pM q!p^{-q}e^{-h^2qp/2}.
 \tag{E5.4}
\]
The normalized logarithmic upper bound is \(-1-\log p-h^2p/2\). The width \(p\) belongs to the assumed candidate and may be very small; it cannot be fixed in advance for all candidates. Once it is fixed, choose \(h\) so that \(1+\log p+h^2p/2>h+3/4\). The quadratic term makes this possible. Award 6 points for both contour computations, 5 for the estimate, and 4 for the quantifier order.

### Exercise 7. Separating all other frequencies — 15 points

Prove that the lower- and higher-frequency modes have normalized logarithmic upper limit \(-\infty\) in the testing functional. Explain why no oscillatory cancellation estimate is needed.

**Solution.** A mode of frequency \(\lambda\ne q=q_n\) contributes in absolute value at most \(2p\lambda^q e^{-\lambda}\lambda^{-2}\). For lower frequencies, \(\lambda\le q_{n-1}\), so the sum is at most \(C_pq_{n-1}^q\). Its normalized logarithm minus \(\log q\) is at most
\[
 \frac{\log C_p}{q}+\log q_{n-1}-\log q
       \le\frac{\log C_p}{q}-(1-1/n)\log q\longrightarrow-\infty.
 \tag{E5.5}
\]
For higher frequencies, \(\lambda\ge q_{n+1}\ge q^2\), and \(q\log\lambda\le\lambda/2\). Their sum is at most \(C_pe^{-q_{n+1}/2}\). The normalized logarithm is at most \((\log C_p)/q-q_{n+1}/(2q)-\log q\), again tending to \(-\infty\). These are absolute-value estimates. The large factorial gaps already eliminate the other modes, so cancellation of their different time phases is unnecessary. Award 6 points for the lower-frequency bound, 6 for the higher-frequency bound, and 3 for explaining absolute control.

### Exercise 8. Real forcings and extra parameters — 15 points

Suppose the complex forcing \(f=a+ib\) is excluded for both operators. Prove that one of \(a,b,a+b\) is excluded for both. Show how the counterexample extends when extra real variables are added and the operators do not differentiate them.

**Solution.** For one operator, if any two of \(a,b,a+b\) had analytic solutions, addition or subtraction would provide solutions for both \(a\) and \(b\). Their complex linear combination would solve \(f\), a contradiction. Thus at most one of the three candidates is solvable for that operator. With two operators, at most two candidates are solvable for at least one. At least one candidate fails for both. Real coefficients ensure that real or imaginary parts of the smooth particular solutions provide smooth solutions for these real forcings.

For extra variables \(r\in\mathbb R^\ell\), keep the forcing and the smooth particular solution independent of \(r\). If an analytic solution on \(\mathbb R^{3+\ell}\) existed, its restriction to \(r=0\) would remain globally analytic and would solve the already excluded three-dimensional equation, because all derivatives act only in \(x,y,t\). The failure therefore persists. Award 7 points for the three-candidate argument, 3 for the smooth real solutions, and 5 for the restriction argument.

## References

- Compact Fourier division and multiplicity-sensitive annihilators, comparison with distributional solvability.
- E. De Giorgi, *Solutions analytiques des équations aux dérivées partielles à coefficients constants*, Séminaire Goulaouic–Schwartz (1971–1972), exposé 29. [Author's seminar](https://www.numdam.org/item/SEDP_1971-1972____A29_0/).
- L. C. Piccinini, *Non surjectivity of the two-variable Laplacian as an operator on the space of analytic functions on three-dimensional real space*, Summer College on Global Analysis, Trieste (1972).
- L. C. Piccinini, *Non surjectivity of the Cauchy–Riemann operator on the space of the analytic functions in real space: generalization to parabolic operators*, Bollettino dell'Unione Matematica Italiana (4), 7 (1973).
