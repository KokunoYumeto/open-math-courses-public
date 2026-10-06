# Extending a boundary time strip to its propagation cone

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A zero-free time strip does not identify the full set of imaginary directions allowed by a mixed problem. The principal boundary symbol selects a component inside the projected hyperbolicity cone. We prove that this component is convex and that both the principal and full determinants are zero-free in its associated tubes. The proof counts zeros on bounded half-disks, controlling separately their imaginary boundary and their possible escape to infinity.

Read [A necessary time strip for smooth mixed solvability](a-necessary-time-strip-for-smooth-mixed-solvability.md), [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Fourier convention and Gaussian formula; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite scalar and polynomial algebra. 

The general hyperbolic-cone and analytic zero-order theorems remain planned prerequisites, with precise statements in [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). Their uses below are conditional on those proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked lessons supply the prerequisite proofs used below.

## The component and the exact conclusions

Let \(\pi\) be the quotient by the real normal direction \(\theta\), and put \(N'=\pi N\), where \(N,\theta\) are independent. Let \(\Gamma=\Gamma(P_m,N)\) be the open convex hyperbolicity cone, and \(\Omega=\pi\Gamma\) its real projected cone. Write \(L=L^\partial\) for the balanced boundary determinant. Its principal symbol is [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s homogeneous extension \(\widehat\Lambda_0\), with integer degree \(\kappa\), possibly negative. Assume
\[
\begin{gathered}
\widehat\Lambda_0(N')\ne0,\\
\qquad
 L(\xi'+i\gamma N')\ne0
       \\
\quad(\xi'\ \hbox{real},\ \gamma<\gamma_0),
 \\
\qquad \gamma_0\le\min(0,\tau_0).
\end{gathered}
\tag{1}
\]
Here \(\tau_0\) is an interior hyperbolicity barrier, allowing the homogeneous barrier zero. [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s normalization with barrier one makes the last condition simply \(\gamma_0\le0\), as in the mixed-system definition. With a different barrier a zero-free-strip bound can be decreased to satisfy the displayed condition. The determinant is initially holomorphic in the projected tube with imaginary part in \(\tau_0N'-\Omega\). Let \(\Sigma\) be the connected component containing \(N'\) of
\(\{\eta'\in\Omega:\widehat\Lambda_0(\eta')\ne0\}\).

**Theorem.** The set \(\Sigma\) is an open convex cone. The principal determinant has no zeros when \(\operatorname{Im}\zeta'\in-\Sigma\), and the full determinant has no zeros when
\(\operatorname{Im}\zeta'\in\gamma_0N'-\Sigma\).
These statements retain the given strip parameter \(\gamma_0\); they do not assert existence of solutions yet.

The real set \(\Omega\) is open because a surjective real linear map sends balls to neighborhoods of their images. It is convex and invariant under positive scaling. Its complex negative tube is denoted by \(\mathcal T=\mathbb R^{n-1}-i\Omega\). [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md) extends the principal symbol holomorphically to \(\bigcup_{c\ne0}c\mathcal T\), so its values on real \(\Omega\) are defined by multiplication by \(-i\). The nonzero set there is open. Components of an open subset of a finite-dimensional real space are open: each small contained ball is connected and belongs to the component of any one of its points. Thus \(\Sigma\) is open. Positive radial paths remain in the same nonzero set by integer homogeneity, so every positive multiple of a point of \(\Sigma\) is in \(\Sigma\).

If \(0\in\Omega\), then openness and positive scaling make \(\Omega\) the entire real quotient space. [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s extension is then entire. This case is covered by the argument below; no pointedness of either projected cone is presumed.

## Removing a barrier without changing the conclusion

To make the complex-scale domain transparent, temporarily translate time frequency by \(i\tau_0N\) in both the interior and every boundary polynomial:
\[
\begin{gathered}
\widetilde P(\zeta)=P(\zeta+i\tau_0N),\\
\qquad
 \widetilde B_j(\zeta)=B_j(\zeta+i\tau_0N),\\
\qquad
 \widetilde L(\zeta')=L(\zeta'+i\tau_0N'),\\
\qquad
 \widetilde\gamma_0=\gamma_0-\tau_0\le0 .
\end{gathered}
\tag{2}
\]
The translated interior barrier is zero and its determinant is holomorphic on \(\mathcal T\). The normal variable is unaltered, so [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s root grouping and [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s pairing give the exact determinant identity in 2. The principal interior cone, normal counts and principal boundary symbol are unchanged. Indeed [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s scaled germ for \(\widetilde L\) is the original germ evaluated at \(\zeta'+i\epsilon\tau_0N'\); its value at \(\epsilon=0\) is unchanged. Its integer degree is unchanged as well, since that principal germ is nonzero somewhere.

We prove the result for these translated polynomials. To simplify notation in the intervening proof, write them again as \(P,B_j,L\), and write \(\gamma_0\) for the nonpositive translated parameter. At the end translating back changes the tube \(\gamma_0N'-\Sigma\) into precisely the original tube in the theorem, not a smaller one.

[The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s local factor construction works for barrier zero: its principal factors are coprime at every point of \(\mathcal T\), and for every small positive scale the actual factors have the same strict upper/lower signs. Its finite coefficient construction therefore gives a holomorphic germ \(\Lambda(\zeta',\epsilon)\) near each \((\zeta',0)\), \(\zeta'\in\mathcal T\), with
\(\Lambda(\zeta',\epsilon)=\epsilon^\kappa L(\zeta'/\epsilon)\) for small positive \(\epsilon\). Its value at zero is \(\widehat\Lambda_0(\zeta')\).

We need this identity at complex scales too. For \(y'\) with \(\operatorname{Re}y'\in\Omega\), define the rotated germ
\[
\begin{gathered}
\Phi(y',\epsilon)=(-i)^{-\kappa}
                       \Lambda(-iy',-i\epsilon),\\
\qquad
 \Phi(y',0)=\widehat\Lambda_0(y').
\end{gathered}
\tag{3}
\]
It is locally holomorphic in both variables, including \(\epsilon=0\). All powers are single-valued because \(\kappa\) is an integer. For fixed \(y'\), actual complex scales satisfy
\[
\begin{gathered}
y'/\epsilon\in\mathcal T
 \\
\quad\Longleftrightarrow\\
\quad
 -\operatorname{Im}(y'\overline\epsilon)\in\Omega,
 \\
\qquad \epsilon\ne0 .
\end{gathered}
\tag{4}
\]
The omitted factor \(|\epsilon|^2\) is positive and \(\Omega\) is a cone. The admissible scales form the nonzero part of an open convex real-linear preimage cone in the \(\epsilon\)-plane. Their intersection with a small centered disk is connected. If the cone contains zero it is the whole plane, whose punctured disk is also connected. The positive imaginary ray \(\epsilon=i\rho\), \(\rho>0\), is admissible because the right side of 4 becomes \(\rho\operatorname{Re}y'\in\Omega\).

On this ray the original positive-scale identity gives
\(\Phi(y',i\rho)=(i\rho)^\kappa L(y'/(i\rho))\).
Both sides are holomorphic on the connected admissible disk. The one-variable identity theorem proves
\(\Phi(y',\epsilon)=\epsilon^\kappa L(y'/\epsilon)\) at every sufficiently small admissible complex scale. This is an identity of actual determinants, not just of a formal principal asymptotic. A finite cover of any compact set of such \(y'\)'s gives uniform convergence of \(\Phi(y',\epsilon)\) to its zero-scale value there.

## First exclude principal zeros on time lines

Fix a real \(\xi'\). For \(\operatorname{Im}z<0\), the functions
\[
\begin{gathered}
\epsilon^\kappa L((\xi'+zN')/\epsilon)
       \longrightarrow\widehat\Lambda_0(\xi'+zN')
       \\
\quad(\epsilon\downarrow0)
\end{gathered}
\tag{5}
\]
converge uniformly on each compact subset of that half-plane, by the analytic scale germ. For each such compact set their arguments have imaginary time below \(\gamma_0\) when \(\epsilon\) is small. Thus the approximating functions are nonzero there.

The limit is not identically zero. For large \(|z|\),
integer homogeneity gives
\(\widehat\Lambda_0(\xi'+zN')=z^\kappa\widehat\Lambda_0(N'+\xi'/z)\);
the second factor tends to the nonzero value at \(N'\). A nonzero locally uniform limit of holomorphic zero-free functions is zero-free: if it had a zero, choose a small circle enclosing that isolated zero but no boundary zero. Uniform convergence and the minimum modulus on the circle permit the straight homotopy between the limit and an approximation without boundary zeros. The contour argument principle keeps their positive zero count unchanged, contradicting the approximation's zero-free property. This proves the needed form of Hurwitz's theorem directly from [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md).

Therefore \(\widehat\Lambda_0(\xi'+zN')\ne0\) for every \(\operatorname{Im}z<0\). For \(\operatorname{Im}z>0\), apply this to \(-\xi'-zN'\) and use the nonzero homogeneity factor \((-1)^\kappa\). Principal zeros on these real time lines can occur only at real \(z\).

## A bounded half-disk count gives the first star property

For \(\eta'\in\Sigma\), consider
\[
 F_{\eta'}(z)=\widehat\Lambda_0(\eta'+zN'),
                 \qquad \operatorname{Re}z\ge0 .
 \tag{6}
\]
It is holomorphic on a neighborhood of every compact subset of this closed half-plane. Indeed
\(\operatorname{Im}[-i(\eta'+zN')]=-\eta'-(\operatorname{Re}z)N'\in-\Omega\),
and [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s homogeneous extension applies. Addition of a nonnegative multiple of \(N'\) stays in \(\Omega\) by convexity and positive scaling; endpoints remain inside because \(\eta'\) is an interior point.

There are no zeros on the imaginary axis. A nonzero imaginary \(z\) is covered by 5, and \(z=0\) is covered by the definition of \(\Sigma\). There are no distant zeros either:
\[
\begin{gathered}
F_{\eta'}(z)=z^\kappa
             \widehat\Lambda_0(N'+\eta'/z),\\
\qquad
 F_{\eta'}(z)\ne0\\
\quad\hbox{if }|z|>C|\eta'|.
\end{gathered}
\tag{7}
\]
Here a fixed small complex neighborhood of \(N'\), on which the principal symbol is nonzero, supplies \(C\). The power \(z^\kappa\) is nonzero for every distant \(z\), including negative \(\kappa\).

Count zeros in the right half-disk bounded by the imaginary segment and a large semicircle. Its boundary has no zeros, and the contour count is finite. The half-disk version of [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md)'s disk count follows by the same finite-zero proof: subtract the terms \(m_a/(z-a)\) from the logarithmic derivative. The remainder is holomorphic near the closed half-disk and has integral zero by the [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html) complex Green identity on its piecewise smooth boundary. The pole terms each contribute their integer multiplicity. The two corners cause no term, since the contour is the sum of its segment and arc. For \(\eta'\) in a small real neighborhood of any one point of \(\Sigma\), a common semicircle radius and a positive boundary minimum make the count constant by the argument principle. Thus the count is a locally constant integer on the connected set \(\Sigma\), hence constant there. At \(\eta'=N'\),
\(F_{N'}(z)=(1+z)^\kappa\widehat\Lambda_0(N')\), which has no zeros or poles in the right half-plane. Consequently the count is zero for every \(\eta'\in\Sigma\).

It follows that
\[
\begin{gathered}
\widehat\Lambda_0(\lambda N'+\mu\eta')\ne0
      \\
\quad(\lambda,\mu\ge0,\ \lambda+\mu>0,\ \eta'\in\Sigma).
\end{gathered}
\tag{8}
\]
For \(\mu>0\), use 6 at \(z=\lambda/\mu\) and homogeneity; for \(\mu=0\), use 1. In particular every segment from \(N'\) to a point of \(\Sigma\) stays in the nonzero set and hence in the same component. This proves star-shapedness with respect to \(N'\) before convexity has been asserted.

## Continue the full determinant's zero count

Fix a real \(\xi'\) and \(\eta'\in\Sigma\). For \(\gamma<\gamma_0\le0\), set
\[
\begin{gathered}
G_\gamma(z)=L(\xi'+i\gamma N'+iz\eta'),
                  \\
\qquad \operatorname{Re}z\le0 .
\end{gathered}
\tag{9}
\]
Its frequency lies in \(\mathcal T\), since its imaginary part is
\(\gamma N'+(\operatorname{Re}z)\eta'\in-\Omega\).
It is holomorphic on a neighborhood of every compact subset of the closed left half-plane. On its imaginary boundary, \(z=i\sigma\) changes only the real frequency to \(\xi'-\sigma\eta'\). The original time-strip assumption therefore excludes all boundary zeros.

There are uniformly no distant zeros when \(\gamma\) ranges in a fixed compact subinterval of \((-\infty,\gamma_0)\). Put \(\epsilon=1/(iz)\) and
\(y'=\eta'+(\xi'+i\gamma N')/(iz)\). For large \(|z|\), \(y'\) is near the real point \(\eta'\), and its actual frequency \(y'/\epsilon\) is in \(\mathcal T\). 3–4 therefore give
\[
\begin{gathered}
(iz)^{-\kappa}G_\gamma(z)
    \\
=\Phi\left(\eta'+\frac{\xi'+i\gamma N'}{iz},
                           \frac1{iz}\right)
    \\
\longrightarrow\widehat\Lambda_0(\eta')\ne0 .
\end{gathered}
\tag{10}
\]
The convergence is uniform over that compact \(\gamma\)-interval and the closed left half-plane outside a large disk. A bounded left half-disk thus contains every zero. Its boundary is zero-free, so the argument principle makes its zero count locally constant in \(\gamma\), and hence constant on \((-\infty,\gamma_0)\).

We determine this count at large negative \(\gamma\), keeping both frequency scales. Write \(\gamma=-\rho\), \(\rho>0\), and \(z=\gamma w\). Then \(\operatorname{Re}z\le0\) means \(\operatorname{Re}w\ge0\), and
\[
\begin{gathered}
(i/\rho)^\kappa G_{-\rho}(-\rho w)
   \\
=\Phi\left(N'+w\eta'+\frac{i\xi'}{\rho},
                       \frac{i}{\rho}\right)
   \\
\longrightarrow\widehat\Lambda_0(N'+w\eta').
\end{gathered}
\tag{11}
\]
For every fixed \(C\), this convergence is uniform on
\(\operatorname{Re}w\ge0, |w|\le C\). The real parts of the compact limiting arguments \(N'+w\eta'\) are in \(\Omega\), so a finite cover supplies the germs and the uniform convergence. The limit has no zeros there. At \(w=0\) this is 1; at \(w\ne0\), homogeneity reduces it to
\(w^\kappa\widehat\Lambda_0(\eta'+N'/w)\), and
\(\operatorname{Re}(1/w)\ge0\), so 6–8 apply. Its modulus therefore has a positive minimum on each such compact half-disk.

Choose \(C\) sufficiently large. On \(|z|>C\rho\), \(\operatorname{Re}z\le0\), the normalized argument in 10 is uniformly close to \(\eta'\), because
\[
\begin{gathered}
\left|\frac{\xi'-i\rho N'}{iz}\right|
       \le \frac{|\xi'|}{C\rho}+\frac{|N'|}{C},
 \\
\qquad \left|\frac1{iz}\right|<\frac1{C\rho}.
\end{gathered}
\tag{12}
\]
Taking \(C\) large and then \(\rho\) large makes the corresponding \(\Phi\) nonzero by continuity at \((\eta',0)\). On the complementary region \(|z|\le C\rho\), 11 and its positive compact minimum exclude zeros. These two regions cover the whole left half-plane. Its zero count is therefore zero for sufficiently negative \(\gamma\), and constancy makes it zero for every \(\gamma<\gamma_0\).

Taking \(z=-1\) in 9 proves nonvanishing when the imaginary frequency is in \(\gamma N'-\Sigma\), \(\gamma<\gamma_0\). This also reaches the endpoint shifted tube. If the desired imaginary part is \(\gamma_0N'-\eta'\), openness gives a small \(\delta>0\) with \(\eta'-\delta N'\in\Sigma\). Set \(\gamma=\gamma_0-\delta\) and use this new cone vector. Then
\[
\begin{gathered}
\gamma N'-(\eta'-\delta N')
       =\gamma_0N'-\eta',\\
\qquad
 L(\zeta')\ne0\\
\quad
       (\operatorname{Im}\zeta'\in\gamma_0N'-\Sigma).
\end{gathered}
\tag{13}
\]
The proof has not presumed zero-freeness on the boundary of \(\Sigma\).

## All directions in the component and convexity

We can now replace time by any \(\eta'\in\Sigma\) in the principal limiting argument. For a real \(\xi'\), \(\operatorname{Im}z<0\), and sufficiently small positive \(\epsilon\),
\[
 \epsilon^\kappa L((\xi'+z\eta')/\epsilon)
      \longrightarrow\widehat\Lambda_0(\xi'+z\eta').
 \tag{14}
\]
The convergence is uniform on compact subsets. The arguments lie in the 13 tube: writing \(r=-\operatorname{Im}z/\epsilon\), their imaginary part is \(-r\eta'\), and
\(r\eta'+\gamma_0N'\in\Sigma\) for large \(r\). This follows from openness at \(\eta'\), positive scaling, and the perturbation \((\gamma_0/r)N'\to0\). The approximants are nonzero. The limit is not identically zero because \(\widehat\Lambda_0(\eta')\ne0\), using its large-\(z\) homogeneous expression. The same small-circle zero-count argument used for 5 makes the limit zero-free.

At \(z=-i\) this proves
\[
\begin{gathered}
\widehat\Lambda_0(\xi'-i\eta')\ne0
     \\
\quad(\xi'\ \hbox{real},\ \eta'\in\Sigma),
 \\
\quad\hbox{or equivalently}\\
\quad
 \operatorname{Im}\zeta'\in-\Sigma .
\end{gathered}
\tag{15}
\]
Upper imaginary time lines in the direction \(\eta'\) are zero-free as well, by multiplication by \(-1\).

Finally fix \(\eta'\in\Sigma\) and repeat the right half-disk count for
\(\widehat\Lambda_0(y'+z\eta')\), \(y'\in\Sigma\), \(\operatorname{Re}z\ge0\).
The domain follows from \(y'+(\operatorname{Re}z)\eta'\in\Omega\).
The imaginary boundary is zero-free by 14 and the definition of \(\Sigma\); the tail is zero-free because \(\widehat\Lambda_0(\eta')\ne0\). The count is locally constant on the same connected component. At \(y'=\eta'\) it is zero, since the function is
\((1+z)^\kappa\widehat\Lambda_0(\eta')\). Thus
\[
\begin{gathered}
\widehat\Lambda_0(\lambda y'+\mu\eta')\ne0
       \\
\quad(y',\eta'\in\Sigma,\ \lambda,\mu\ge0,\
                                      \lambda+\mu>0).
\end{gathered}
\tag{16}
\]
The segment between any two cone vectors stays in \(\Omega\) and in this nonzero set. It is connected to an endpoint in \(\Sigma\), so it stays in that component. This proves convexity. The previously proved positive radial invariance proves the cone assertion.

Returning through 2 leaves \(\Sigma\) and the principal symbol unchanged and restores the original full shifted tube exactly. This completes both conclusions of the theorem.

## Exercises with complete solutions

**Exercise 1 (entry: a negative principal degree).** In normal/time frequencies take
\[
\begin{gathered}
P(w,s)=(s-i)(w+s-i)-1,\\
\qquad B_1(w,s)=w+s-i .
\end{gathered}
\tag{17}
\]
Compute the upper count, determinant, principal symbol and cone. Verify the full zero-free tube without relying on a positive principal degree.

**Solution.** For real \(w\), the two time roots are \(s=i+(-w\pm\sqrt{w^2+4})/2\), so the interior polynomial has barrier one. For \(\operatorname{Im}s<0\), its single normal root is
\(w=1/(s-i)-s+i\). Its imaginary part is positive: the reciprocal of \(s-i\) has positive imaginary part, as does \(-s+i\). Thus \(h=1\). Evaluation at this root gives \(L(s)=1/(s-i)\), and its scaled germ is
\(\epsilon^{-1}L(s/\epsilon)=1/(s-i\epsilon)\).
Consequently \(\kappa=-1\) and \(\widehat\Lambda_0(s)=1/s\).

The principal interior cone containing \((w,s)=(0,1)\) is \(s>0,w+s>0\); its time projection is \((0,\infty)\). The principal determinant never vanishes there, so \(\Sigma=(0,\infty)\). Choose the original strip parameter \(\gamma_0=0\). The full determinant has neither a zero nor a pole in \(\operatorname{Im}s<0\), which is the theorem's shifted cone tube. The principal determinant has no zero in that tube either. Although the reciprocal full determinant grows linearly at infinity, this does not create a zero of the full determinant. Its exact lower bound is
\[
 |L(s)|=\frac1{|s-i|}
       \ge\frac1{1+|s|}.
 \tag{18}
\]
The proof's zero counts use holomorphy inside their half-planes, not polynomiality or positive degree.

**Exercise 2 (intermediate: the mixed cone can narrow).** For
\(P(w,y,s)=w^2+y^2-s^2\) and \(B_1(w,y,s)=w+s/2\), find \(\Sigma\) and its tangential dual cone. Verify the starting time strip and compare the resulting tangential speed with the interior wave speed.

**Solution.** The projected interior cone is \(\Omega=\{(y,s):s>|y|\}\). In the lower imaginary-time tube, let \(q=\sqrt{s^2-y^2}\) be the analytic branch satisfying \(q=s\) at \(y=0\). The upper normal root is \(-q\). There is one boundary condition and
\(L=s/2-q\), a homogeneous determinant of degree one. It is nonzero on every real-spatial lower time line. Indeed \(L=0\) would give \(q=s/2\), hence \(s^2=4y^2/3\). For real \(y\), this requires real \(s\), including \(s=0\) when \(y=0\), contradicting \(\operatorname{Im}s<0\). Thus \(\gamma_0=0\) is a valid starting strip.

On the real forward cone \(q\) is the positive square root. The determinant vanishes precisely at \(|y|=(\sqrt3/2)s\). Its component containing \((0,1)\) is
\[
\begin{gathered}
\Sigma\\
=\{(y,s):s>0,\ |y|<(\sqrt3/2)s\}.
\end{gathered}
\tag{19}
\]
This cone is narrower than the interior projected cone. Its tangential dual consists of physical \((z,t)\) whose pairing \(zy+ts\) is nonnegative for every point of \(\Sigma\):
\[
 \Sigma^\circ=\{(z,t):t\ge(\sqrt3/2)|z|\}.
 \tag{20}
\]
For fixed \(s>0\), the infimum of \(zy+ts\) over the allowed open \(y\)-interval is \(s(t-(\sqrt3/2)|z|)\). Nonnegativity for all \(s\) is therefore exactly 20, including its closed boundary. Equivalently \(|z|\le(2/\sqrt3)t\); the tangential speed permitted by this dual cone is \(2/\sqrt3>1\), whereas the interior wave cone has speed one. The theorem identifies the cone; a support conclusion for actual boundary kernels requires the later construction.

**Exercise 3 (advanced: why the half-plane boundary matters).** For real \(b\), study zeros in \(\operatorname{Re}z\ge0\) of
\[
 F_b(z)=\frac{z^2+(b+2)z+1}{(z+2)^3}.
 \tag{21}
\]
Find the parameter at which imaginary-boundary zeros appear, compare the zero counts on its two sides, and explain why the negative degree at infinity causes no problem.

**Solution.** The only pole is at \(-2\), outside the closed right half-plane. On its imaginary axis the numerator is
\(1-\sigma^2+i(b+2)\sigma\). It vanishes exactly when \(b=-2\) and \(\sigma=\pm1\). For \(b>-2\), the roots are either real with negative sum and positive product, hence both negative, or a conjugate pair with negative real part. There are no zeros in the right half-plane. For \(b<-2\), real roots are both positive, or a conjugate pair has positive real part; the count is two. For instance
\[
\begin{gathered}
b=0:\ z=-1\ \hbox{twice};\\
\qquad
 b=-2:\ z=\pm i;\\
\qquad
 b=-3:\ z=(1\pm i\sqrt3)/2 .
\end{gathered}
\tag{22}
\]
Cancellation with the pole at \(-2\), if it occurs for another \(b\), changes no right half-plane count. On every compact parameter interval,
\(zF_b(z)\to1\) uniformly as \(|z|\to\infty\), so no zeros escape through a distant semicircle. The degree at infinity is \(-1\), yet the normalized tail is uniformly nonzero. The count changes at \(b=-2\) because boundary zero-freeness fails there, precisely the event excluded in the theorem.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
