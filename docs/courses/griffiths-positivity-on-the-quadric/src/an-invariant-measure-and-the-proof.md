# An invariant measure and the proof

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By [A quadratic limit of dual norms](a-quadratic-limit-of-dual-norms.md), positive metrics on infinitely many of the bundles \(E_m=f_m^*G\otimes P\) would give a nonzero, nonnegative plurisubharmonic function \(q\) on the total space of \(F=G^\vee\), quadratic on every fiber. This lesson shows that for the bundle \(G\) of [A bundle glued along three graphs](a-bundle-glued-along-three-graphs.md) no such function exists, and proves the theorem of the course.

The argument has three steps. Restricted to either of the two line subbundles of \(F\), the function \(q\) is constant along the other factor of \(\mathbb P^1\times\mathbb P^1\); the gluing along the three graphs then gives one squared seminorm on \(\mathcal O_{\mathbb P^1}(-24)\), invariant under the lifts of the two matrices \(A\) and \(B\). The logarithm of its weight defines a positive measure on \(\mathbb P^1\) of total mass \(48\pi\), invariant under \(A\) and \(B\). Finally, \(A\) and \(B\) have no common invariant measure.

- The reduction to one invariant seminorm (Lemma 1.1).
- The measure of a squared seminorm (Lemma 2.1).
- No invariant measure (Lemma 3.1).
- The obstruction and the proof of the theorem (Section 4).

The lesson follows [OpenAI-GP, Sections 5 and 6]. It uses subharmonic and plurisubharmonic functions as in the lesson [Compactness and complex-line positivity](course:AN-01/reader/AN01-U024) (course *Distributions, kernels and analytic singularities*), and the fact that a positive distribution is a positive Radon measure (Theorem 4.1 of [Order, positivity and distributional limits](course:AN-01/reader/AN01-U008), same course).

## 1. One invariant seminorm

Let \(b=24\), \(L_1=\mathcal O_S(b,0)\), \(L_2=\mathcal O_S(0,b)\), and \(\iota_i\colon L_i^{-1}\to F\), \(\alpha\colon L_1^{-1}|_D\to L_2^{-1}|_D\) as in Proposition 3.1 of the lesson on the glued bundle.

**Lemma 1.1** ([OpenAI-GP, Lemma 5.1]). Let \(q\colon F\to[0,\infty)\) be finite, plurisubharmonic, not identically zero, and a Hermitian quadratic form on every fiber. Then there is a finite, nonnegative, plurisubharmonic function \(a\) on the total space of \(\mathcal O_{\mathbb P^1}(-b)\), not identically zero and a Hermitian quadratic form on every fiber, such that
\[
a\bigl(Mx,M^{\otimes b}v\bigr)=a(x,v)\quad(M=A,B)
\]
for all \(x\in\mathbb P^1\) and \(v\in\mathcal O(-b)_x\).

**Proof.** *Constancy along the rulings.* The fiber of \(L_1^{-1}=p_1^*\mathcal O(-b)\) at \((x_1,x_2)\) is \(\mathcal O(-b)_{x_1}\). For fixed \(x_1\) and \(v\in\mathcal O(-b)_{x_1}\), the map \(x_2\mapsto\iota_1(v)\in F_{(x_1,x_2)}\) is holomorphic from \(\mathbb P^1\) to the total space of \(F\). So \(x_2\mapsto q(\iota_1(v))\) is a finite subharmonic function on the compact Riemann surface \(\mathbb P^1\). It attains its maximum, being upper semicontinuous, and by the maximum principle it is constant. So \(a_1(x_1,v)=q(\iota_1(v))\) does not depend on \(x_2\). Fixing \(x_2\), \(a_1\) is the composite of \(q\) with a holomorphic map from the total space of \(\mathcal O(-b)\) to that of \(F\), linear on fibers; so \(a_1\) is plurisubharmonic, nonnegative, and quadratic on fibers. In the same way \(a_2(x_2,v)=q(\iota_2(v))\) is defined on \(\mathcal O(-b)\) over the second factor.

*The graph identities.* At a point \((x,Mx)\) of \(\Gamma_M\), Proposition 3.1 of the lesson on the glued bundle gives \(\iota_1(v)=\iota_2(\alpha v)=\iota_2(M^{\otimes b}v)\). So, for \(M\in\{I,A,B\}\),
\[
a_1(x,v)=a_2\bigl(Mx,M^{\otimes b}v\bigr) .
\]
For \(M=I\) this says \(a_1=a_2\); call this function \(a\). For \(M=A,B\) it is the claimed invariance.

*Nonvanishing.* Suppose \(a\equiv0\). At a point \(y\notin D\), the two lines \(\iota_1(L_1^{-1})_y\) and \(\iota_2(L_2^{-1})_y\) span \(F_y\), and the positive semidefinite form \(H_y\) of \(q\) vanishes on both. By the Cauchy–Schwarz inequality \(|H_y(v,w)|^2\le H_y(v,v)H_y(w,w)\), \(H_y\) vanishes on pairs from the two lines, hence \(H_y=0\). So \(q=0\) on the total space over \(S\setminus D\), which has full measure. A nonnegative plurisubharmonic function is at most its averages over small balls, so \(q\equiv0\), a contradiction. \(\blacksquare\)

## 2. The measure of a squared seminorm

On a Riemann surface \(C\) with a local coordinate \(z\), and for a real function or distribution \(u\), put \(dd^cu=i\,u_{z\bar z}\,dz\wedge d\bar z\), the convention of [OpenAI-GP, Section 1]. With the area measure \(dA\) this is \(dd^cu=2u_{z\bar z}\,dA=\tfrac12\Delta u\,dA\). For a subharmonic \(u\), \(dd^cu\) is a positive distribution by Theorem 3.2 of [Positive derivatives and canonical representatives](course:AN-01/reader/AN01-U023), hence a positive Radon measure by Theorem 4.1 of [Order, positivity and distributional limits](course:AN-01/reader/AN01-U008); for instance \(dd^c\log|z|^2=2\pi\delta_0\).

**Lemma 2.1** ([OpenAI-GP, Lemma 5.2]). Let \(L\) be a holomorphic line bundle on a connected Riemann surface \(C\), and \(a\colon L\to[0,\infty)\) finite, plurisubharmonic, not identically zero, and a positive semidefinite Hermitian form on every fiber. In a nonvanishing holomorphic frame \(e\) over \(U\subseteq C\), write \(a(z,we(z))=u_e(z)|w|^2\). Then:

1. \(\log u_e\) (with the value \(-\infty\) allowed) is subharmonic and locally integrable, and the local measures \(dd^c\log u_e\) glue to a positive Radon measure \(\mu\) on \(C\);
2. if a holomorphic automorphism \(\widetilde T\) of \(L\) covers an automorphism \(T\) of \(C\) and \(a\circ\widetilde T=a\), then \(\mu\) is invariant: \(\mu(T(E))=\mu(E)\) for Borel sets \(E\);
3. if \(C=\mathbb P^1\) and \(L=\mathcal O(-b)\) with \(b\ge1\), then \(\mu(\mathbb P^1)=2\pi b\).

**Proof.** *Regularization.* Fix a coordinate disk \(U\) and write \(u=u_e\). It is finite, nonnegative, and subharmonic (restrict \(a\) to the holomorphic section \(z\mapsto e(z)\)), and locally bounded. Let \(\rho\ge0\) be smooth, radial, supported in the unit disk, with integral one, \(\rho_\delta(z)=\delta^{-2}\rho(z/\delta)\), and
\[
u_\delta=u*\rho_\delta+\delta ,
\]
defined on smaller disks for small \(\delta\). Averaging the holomorphic translations \((z,w)\mapsto(z-\zeta,w)\) shows that \((u*\rho_\delta)(z)|w|^2\) is plurisubharmonic, and adding \(\delta|w|^2\) keeps it so; so \(u_\delta(z)|w|^2\) is smooth and plurisubharmonic, with \(u_\delta>0\). Its complex Hessian at \(w=1\) is \(\begin{pmatrix}(u_\delta)_{z\bar z}&(u_\delta)_z\\ (u_\delta)_{\bar z}&u_\delta\end{pmatrix}\), whose determinant is nonnegative; so
\[
(\log u_\delta)_{z\bar z}=\frac{u_\delta(u_\delta)_{z\bar z}-|(u_\delta)_z|^2}{u_\delta^2}\ge0 ,
\]
and \(f_\delta=\log u_\delta\) is subharmonic. The radial averages of the subharmonic \(u\) decrease to \(u\) as \(\delta\downarrow0\) (Theorem 1.1 of the lesson on complex-line positivity), so \(u_\delta\downarrow u\) and \(f_\delta\downarrow\log u\).

*Integrability near a point where \(u>0\).* Let \(u(z_0)>0\) and \(\overline{B(z_0,R)}\subset U\). For small \(\delta\), \(f_\delta\le C_0\) on the disk, by local boundedness, and \(f_\delta(z_0)\ge\log u(z_0)\). The submean inequality on circles, integrated over the radius, gives \(\int_{B(z_0,R)}f_\delta\,dA\ge\pi R^2\log u(z_0)\), so the negative parts satisfy
\[
\int_{B(z_0,R)}f_\delta^-\,dA\le\pi R^2\bigl(C_0-\log u(z_0)\bigr) .
\]
They increase as \(\delta\) decreases, so by monotone convergence \(\log u\) is integrable on \(B(z_0,R)\), and \(f_\delta\to\log u\) in \(L^1\) there.

*Integrability everywhere.* Let \(\Omega\) be the set of points near which \(\log u_e\) is integrable; by the frame law \(\log u_{ge}=\log u_e+\log|g|^2\), with \(\log|g|^2\) harmonic, \(\Omega\) does not depend on the frame. It is open, and nonempty since \(a\not\equiv0\) gives a point with \(u>0\). If \(x\) is a boundary point of \(\Omega\), choose a coordinate disk containing \(\overline{B(x,4r)}\). There is a small disk in \(\Omega\cap B(x,r)\), on which \(\log u\) is integrable, so it contains a point \(z_0\) with \(u(z_0)>0\); the previous step on \(B(z_0,2r)\), a neighbourhood of \(x\), gives \(x\in\Omega\). So \(\Omega\) is closed, and \(\Omega=C\).

*The measure.* On each disk, \(\log u\) is the decreasing limit of the subharmonic \(f_\delta\) and is integrable, so it is subharmonic, and \(dd^c\log u\) is a positive measure. By the frame law, the local measures agree on overlaps, since \(dd^c\log|g|^2=0\). This proves part 1.

*Invariance.* With frames \(e\) on \(U\) and \(e'\) on \(V\supseteq T(U)\), write \(\widetilde T(e(z))=c(z)e'(Tz)\) with \(c\) holomorphic and nonvanishing. Then \(a\circ\widetilde T=a\) gives \(u_e(z)=|c(z)|^2u_{e'}(Tz)\), so \(\log u_e=\log|c|^2+(\log u_{e'})\circ T\). Applying \(dd^c\), which commutes with composition with the holomorphic map \(T\), gives \(\mu=T^*\mu\), where \(\int\varphi\,d(T^*\mu)=\int(\varphi\circ T^{-1})\,d\mu\); that is, \(\mu(E)=\mu(T(E))\). This proves part 2.

*The mass.* On \(\mathcal O(-b)\), let \(h_0\) be the metric induced from \(\mathbb C^2\). In the frame \(e(z)=(1,z)^{\otimes b}\) over the affine line, \(h_0(e,e)=(1+|z|^2)^b\). The functions \(\log u_e-\log h_0(e,e)\) for the various frames agree on overlaps and define an integrable function \(\Phi\) on the compact \(\mathbb P^1\), and \(\mu-\mu_0=dd^c\Phi\) with \(\mu_0=dd^c\log h_0(e,e)\). Since \(\langle dd^c\Phi,1\rangle=\langle\Phi,dd^c1\rangle=0\), \(\mu(\mathbb P^1)=\mu_0(\mathbb P^1)\). Further \((\log(1+|z|^2))_{z\bar z}=(1+|z|^2)^{-2}\), so
\[
\begin{aligned}
\mu_0(\mathbb P^1)&=\int_{\mathbb C}\frac{2b}{(1+|z|^2)^2}\,dA\\
&=4\pi b\int_0^\infty\frac{r\,dr}{(1+r^2)^2}=2\pi b .
\end{aligned}
\]
\(\blacksquare\)

Where \(u_e\) is smooth and positive, \(dd^c\log u_e\) is minus the curvature form of the metric \(u_e\) on \(L\); for the negative bundle \(\mathcal O(-b)\) this explains the positive mass. The lemma allows zeros of \(u_e\), and the measure may have atoms there; nothing is removed in the computation.

## 3. No invariant measure

**Lemma 3.1** ([OpenAI-GP, Lemma 5.3]). The transformations of \(\mathbb P^1\) given by the matrices \(A\) and \(B\) of Lemma 1.1 of the lesson on the glued bundle have no common invariant finite positive Borel measure other than zero.

**Proof.** Let \(\mu\) be such a measure. It is invariant under \(T=AB\). By that lemma, \(AB\) has eigenvalues \(\lambda>1>\lambda^{-1}\); in a coordinate in which its eigenlines are \(0\) and \(\infty\), \(T(z)=\lambda^2z\) or \(\lambda^{-2}z\), and replacing \(T\) by \(T^{-1}\) we may assume \(T(z)=Rz\) with \(R>1\). The half-open annuli \(C_n=\{z:R^n\le|z|<R^{n+1}\}\), \(n\in\mathbb Z\), are disjoint, cover \(\mathbb C^*\), and satisfy \(T(C_n)=C_{n+1}\). They all have the same measure, which is zero because \(\mu\) is finite; so \(\mu(\mathbb C^*)=0\), and \(\mu\) is supported on the two fixed points \(0,\infty\) of \(T\).

So the support of \(\mu\) is a nonempty set of at most two points, and it is preserved by \(A\) and by \(B\): a point is in the support exactly when all its neighbourhoods have positive measure, which invariance preserves. \(A\) and \(B\) act on \(\mathbb P^1\) with order three, so they permute a set of at most two points trivially: every point of the support is fixed by both \(A\) and \(B\), that is, it is a common eigenline of the two matrices. This contradicts part 4 of Lemma 1.1 of the lesson on the glued bundle. \(\blacksquare\)

The argument does not care whether the measure is diffuse or atomic: atoms at the two fixed points of \(AB\) are what remains, and the finite orders of \(A\) and \(B\) exclude them.

## 4. The obstruction and the theorem

**Proposition 4.1** ([OpenAI-GP, Proposition 5.4]). For the bundle \(G\) of the lesson on the glued bundle and \(F=G^\vee\), every finite, nonnegative, plurisubharmonic function on the total space of \(F\) that is a Hermitian quadratic form on every fiber is identically zero.

**Proof.** If such a function were not zero, Lemma 1.1 would give a nonzero squared seminorm on \(\mathcal O(-24)\) invariant under the lifts \(A^{\otimes24}\) and \(B^{\otimes24}\), and Lemma 2.1 a positive measure on \(\mathbb P^1\) of mass \(48\pi\), invariant under \(A\) and \(B\). Lemma 3.1 excludes this. \(\blacksquare\)

**Proof of Theorem 5.1 of [Hermitian metrics and Griffiths positivity](hermitian-metrics-and-griffiths-positivity.md).** Let \(G\) be the bundle of Proposition 3.1 of [A bundle glued along three graphs](a-bundle-glued-along-three-graphs.md). By Theorem 4.1 of [Ampleness of the power family](ampleness-of-the-power-family.md), every \(E_m=f_m^*G\otimes P\) is ample. If infinitely many \(E_m\) had smooth strictly Griffiths-positive metrics, Proposition 5.1 of [A quadratic limit of dual norms](a-quadratic-limit-of-dual-norms.md) would give a nonzero function on the total space of \(G^\vee\) of the kind excluded by Proposition 4.1. So the set of such \(m\) is finite, and every \(m_0\) larger than all of its elements has the property of the theorem. \(\blacksquare\)

The proof uses no estimate on the metrics or their curvature, and it gives no value for \(m_0\). The limit in the previous lesson may lose rank, but it cannot vanish or lose its quadratic form at any point; these are the two properties that carry the gluing along the graphs, a set of measure zero, to the invariant measure.

## 5. Exercises

**5.1.** Show that a finite subharmonic function on \(\mathbb P^1\) is constant.

**5.2.** Compute the measure \(\mu\) of Lemma 2.1 for the seminorm on \(\mathcal O(-b)\) given by \(a(z,w(1,z)^{\otimes b})=|w|^2|z|^{2b}\) over the affine line (extended to \(\mathbb P^1\)), and check that its mass is \(2\pi b\).

**5.3.** Show that the transformation \(z\mapsto\lambda z\), \(|\lambda|=1\), \(\lambda\) not a root of unity, preserves the measure \(d\theta\) on the unit circle; why does the proof of Lemma 3.1 need \(|\lambda|\ne1\)?

**5.4.** Show that a single transformation of order three always has an invariant probability measure on \(\mathbb P^1\), so that two transformations are needed in Lemma 3.1.

**5.5.** In Lemma 1.1, why is the maximum principle applied to the restriction to a whole \(\mathbb P^1\) and not to a disk?

## 6. Solutions

**5.1.** A subharmonic function is upper semicontinuous, so on the compact \(\mathbb P^1\) it attains its maximum, at a point \(p\). The set where the maximum is attained is closed, and by the submean inequality it is open: near a point of it, the function is at most the maximum and its mean over small circles is at least the maximum, so it equals the maximum almost everywhere on those circles, and by upper semicontinuity on a neighbourhood. \(\mathbb P^1\) is connected.

**5.2.** Over the affine line, \(u_e=|z|^{2b}\), \(\log u_e=b\log|z|^2\), and \(dd^c\log|z|^2=2\pi\delta_0\) in the convention of Section 2. In the frame at infinity, \(e'=(w',1)^{\otimes b}\) with \(w'=1/z\), the seminorm has weight \(1\), so \(\mu\) has no mass near \(\infty\). So \(\mu=2\pi b\,\delta_0\), of mass \(2\pi b\).

**5.3.** Rotation preserves arc length. For \(|\lambda|=1\) the annuli \(C_n\) are not moved to one another, and a rotation-invariant measure on a circle exists; the expansion \(R>1\) is what forces the measure to the fixed points.

**5.4.** If \(T\) has order three, the measure \(\frac13(\delta_x+\delta_{Tx}+\delta_{T^2x})\) is invariant for every point \(x\).

**5.5.** On a disk, a subharmonic function need not be constant; on the compact \(\mathbb P^1\) it must be (Exercise 5.1). The restriction of \(q\) along a whole fiber of the projection to the first factor is defined on all of \(\mathbb P^1\), because the line bundle \(L_1^{-1}\) is pulled back from the first factor and so is trivial along it.

## References

- [OpenAI-GP] OpenAI, *Ample rank-two bundles on the quadric surface without Griffiths-positive metrics*, OpenAI Math Release preprint, 24 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026
