# Polynomial phases and Fourier tails

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

A quadratic stationary point moves out along the input as the frequency grows, so a decaying amplitude becomes a measurable Fourier tail. Higher polynomial degrees set different frequency scales and entire profiles. We measure shell masses and monomial phases, prove the full weighted quadratic and polynomial Fourier identities, then derive the weak endpoint, every monomial origin derivative and the exact effect of Gaussian damping on the cubic profile.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz seminorm estimates, compact-test density, Gaussian mass, inverse transforms and bilinear distributional rules used here. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16, proves dominated convergence, absolute Fubini and real linear Jacobians. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the calculus and algebra. These supplied texts retain their stated licences.

[Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and Theorem 3.1, proves the holomorphic determinant branch and Gaussian transform. [Quadratic transforms and tempered images](quadratic-transforms-and-tempered-images.md), Lemma 0.1, supplies that formula at every complex frequency, with absolute convergence of every frequency derivative. [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1 and calculation G, proves strong Fourier continuity and the signed scalar and product Fresnel identities. [Order, positivity and distributional limits](order-positivity-and-limits.md), (T1)–(T2), proves that bounded compact-test families have common compact support and uniform derivative bounds. Consequently such families are bounded in Schwartz space: each polynomial weight is bounded on their common support. This gives the strong compact-test conclusions from the strong tempered estimates below.

Use \(\widehat f(\xi)=\int_{\mathbb R}e^{-ix\xi}f(x)\,dx\), inverse factor \(1/(2\pi)\), and complex bilinear distribution pairings. The exact finite-contour interface is [Boundary flux and weak identities](boundary-flux-and-weak-identities.md), Theorem 2.1 and Corollaries 2.3–2.4. Corollary 2.4 proves Green's formula for finitely many regular arcs meeting at corners, using the actual \(O(r)\) endpoint-length and \(O(r)\) cutoff-error bounds. It applies to the rectangles, sectors and bounded polygonal regions used here. For a holomorphic integrand near the closed region, multiply by a compact cutoff equal to one nearby; its complex Green area derivative is zero throughout that region. The oriented boundary integral is therefore zero. Partitioning at any intersections and cancelling oppositely oriented internal arcs proves the same contour comparison for a finite union of such regions.

## Positive gamma integrals for the origin values

For \(s>0\), write
\[
 \Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt.
\]
This integral is finite. On \((0,1)\) the integrand is at most \(t^{s-1}\), whose integral is \(1/s\). Choose an integer \(N\ge\max(s-1,0)\). For \(t\ge1\), the positive exponential series gives \(e^{t/2}\ge(t/2)^N/N!\), hence
\[
 t^{s-1}e^{-t}\le 2^N N!e^{-t/2}.
\]
The right side has finite integral. For \(c>0\), \(m\ge2\) and integer \(k\ge0\), the ordinary substitution \(t=cu^m\) first on compact positive intervals, followed by monotone convergence at both endpoints, now proves
\[
 \begin{gathered}
 \int_0^\infty u^k e^{-cu^m}\,du\\
 =\frac1m c^{-(k+1)/m}
       \Gamma\!\left(\frac{k+1}{m}\right).
 \end{gathered}
\]
These positive defining integrals suffice for every gamma value below.

## Measure the energy in moving frequency shells

**T1. A stationary point samples a distant amplitude.** The phase \(x^2-\xi x\) is stationary at \(x=\xi/2\). The unweighted transform, proved in the Fresnel calculation, is
\(F_0(\xi)=\sqrt\pi e^{i\pi/4-i\xi^2/4}\).
Theorem A below proves that inserting \((1+x^2)^{-a/2}\) changes this leading profile by the amplitude at that moving point:
\(F_a(\xi)/F_0(\xi)\sim(|\xi|/2)^{-a}\).
Thus phase, tail size and the frequency scale are all visible in the same measurement.

Fix \(L>1\) and measure the \(p\)-mass in both frequency shells \(R<|\xi|<LR\). Write \(A_a=2^a\sqrt\pi\). Solution 9 proves

\[
\begin{gathered}
R^{ap-1}\int_{R<|\xi|<LR}|F_a(\xi)|^p d\xi
\\ \longrightarrow 2A_a^p\int_1^L u^{-ap}du.
\end{gathered}\tag{T1}
\]

For \(a=1/2,p=2,L=2\), each sufficiently distant pair of dyadic shells carries mass approaching \(4\pi\log2\). Adding shells therefore gives logarithmic divergence of the square-integral norm. For \(a>1/2\), their leading masses instead decrease geometrically like \(2^{j(1-2a)}\). The same test distinguishes every finite-\(p\) threshold in Theorem A. At the critical exponent the function still has an exact weak-integrability bound, established in Solution 9.

## A. The transform, its asymptotic and all integrability endpoints

**Theorem A (weighted quadratic tails).** Let \(a>0\) and
\[
f_a(x)=(1+x^2)^{-a/2}e^{ix^2}.
\]
Its tempered Fourier transform is a continuous bounded function \(F_a\), and
\[
\begin{gathered}
e^{i\xi^2/4}(|\xi|/2)^aF_a(\xi)
\\ \longrightarrow\sqrt\pi\,e^{i\pi/4},
\\ |\xi|\longrightarrow\infty.
\end{gathered} \tag{A1}
\]
In particular \(|F_a(\xi)|(|\xi|/2)^a\to\sqrt\pi\). For \(1\le p<\infty\), \(F_a\in L^p(\mathbb R)\) exactly when \(ap>1\). For \(p=\infty\), it belongs to \(L^\infty\) for every permitted \(a>0\).

**Proof: the branch and the continuous transform.** In the open strip \(|\operatorname{Im}z|<1\), the quantity \(1+z^2\) has positive real part. Indeed, for \(z=s+ih\),
\[
\operatorname{Re}(1+z^2)=1+s^2-h^2>0.
\]
Thus
\[
w_a(z)=\exp\bigl(-\tfrac a2\operatorname{Log}(1+z^2)\bigr)
\]
is single valued and holomorphic there, using the logarithm continued from the positive real axis. On the smaller closed strip \(|h|\le1/2\),
\[
|w_a(s+ih)|\le (3/4+s^2)^{-a/2}.
\tag{A2}
\]
This supplies an actual branch, rather than a formal power of a contour-dependent complex number.

The logarithm is the scalar case of the linked complex Gaussian proof’s constructive formula:
\(\beta(q)=\int_0^1(q-1)/(1-s+sq)\,ds\) for \(\operatorname{Re}q>0\). Its full proof gives \(e^{\beta(q)}=q\), so \(\operatorname{Re}\beta(q)=\log|q|\). For \(c>0\), differentiating in \(c\) gives \(\beta(cq)=\log c+\beta(q)\), with the constant fixed at \(c=1\). Thus the branch and the modulus in (A2), and the positive scaling used in (A7), are exactly the established logarithm, not a separately assumed complex-power convention.

For real \(\xi\), both improper tails of
\[
\begin{gathered}
I(\xi)=
\\ \int_{\mathbb R}(1+x^2)^{-a/2}e^{i(x^2-\xi x)}\,dx
\end{gathered} \tag{A3}
\]
converge. To verify this uniformly for \(\xi\) in a fixed compact set, take \(R\) large compared with that set, put \(g(x)=(1+x^2)^{-a/2}\) and \(\varphi_\xi(x)=x^2-\xi x\), and integrate by parts using
\[
e^{i\varphi_\xi(x)}
=\frac{1}{i(2x-\xi)}\frac{d}{dx}e^{i\varphi_\xi(x)}.
\]
For \(x\ge R\), \(|2x-\xi|\ge x\), \(g(x)=O(x^{-a})\) and \(g'(x)=O(x^{-a-1})\). The endpoint at infinity vanishes, and
\[
\begin{gathered}
\left|\int_R^\infty g(x)e^{i\varphi_\xi(x)}\,dx\right|
\\ \le C R^{-a-1}+C\int_R^\infty x^{-a-2}\,dx
\\ \le C_a R^{-a-1}.
\end{gathered} \tag{A4}
\]
The negative tail follows by \(x\mapsto-x,\xi\mapsto-\xi\); all constants remain uniform on the given compact frequency set. Finite-interval integrals are continuous in \(\xi\), so (A4) proves \(I\) continuous.

The functions \(f_a\,1_{[-R,R]}\) tend to \(f_a\) in \(\mathcal S'\), by domination against every Schwartz test. Their Fourier transforms are the corresponding finite integrals in (A3), which tend locally uniformly to \(I\) by (A4). Hence \(I\) represents \(\widehat f_a\) as a distribution on compactly supported smooth tests. The bounds below prove \(I\) bounded; its regular distribution is consequently tempered. Since compactly supported smooth tests are dense in \(\mathcal S\) by the usual smooth expanding cutoffs, equality on them gives equality in \(\mathcal S'\). Write this function as \(F_a\).

**Proof: a fixed absolutely convergent contour.** Orient \(\Gamma\) from left to right, consisting of the negative ray \(s-i/2,\ s\le-1\), the straight segment from \(-1-i/2\) to \(1+i/2\), and the positive ray \(s+i/2,\ s\ge1\). The integrand \(w_a(z)e^{i(z^2-\xi z)}\) is holomorphic between this contour and the real axis. On a positive vertical end segment \(z=R+ih,\ 0\le h\le1/2\), its absolute value is at most
\[
C_aR^{-a}e^{-(2R-\xi)h}.
\]
For \(R>|\xi|+1\), its integral is at most \(C_aR^{-a-1}\). The negative end segment has the same estimate with \(z=-R-ih\). Cauchy's theorem on the bounded region, followed by these explicit end estimates and (A4), therefore gives
\[
F_a(\xi)=\int_\Gamma w_a(z)e^{i(z^2-\xi z)}\,dz.
\tag{A5}
\]
On the rays, \(|e^{iz^2}|=e^{-|s|}\) and \(|e^{-i\xi z}|\le e^{|\xi|/2}\). The contour integral is absolutely convergent. No unproved interchange of conditional real integrals is used.

Complete the square and set \(r=\xi/2\). Substitution in (A5) produces the contour \(\Gamma-r\) for the holomorphic integrand \(w_a(y+r)e^{iy^2}\). It can be replaced by \(\Gamma\): the contours have the same two horizontal tail heights, coincide sufficiently far out, and their differing finite parts bound regions entirely within \(|\operatorname{Im}y|\le1/2\). The singularities \(y=-r\pm i\) lie outside this strip. Applying Cauchy's theorem to those finite regions yields
\[
\begin{gathered}
F_a(\xi)=e^{-i\xi^2/4}
\\ {}\cdot\int_\Gamma(1+(y+r)^2)^{-a/2}e^{iy^2}\,dy.
\end{gathered} \tag{A6}
\]

For fixed \(y\in\Gamma\), as \(r\to+\infty\) or \(r\to-\infty\),
\[
|r|^a(1+(y+r)^2)^{-a/2}\longrightarrow1
\tag{A7}
\]
with the branch already defined. If \(y=s+ih\) and \(|h|\le1/2\), then
\[
\begin{gathered}
|1+(y+r)^2|\ge3/4+(s+r)^2,
\\ |r|\le |s+r|+|s|.
\end{gathered}
\]
For \(|r|\ge1\) these inequalities give
\[
\begin{gathered}
|r|^a\,|(1+(y+r)^2)^{-a/2}|
\\ \le C_a(1+|s|)^a.
\end{gathered} \tag{A8}
\]
Multiplication by \(|e^{iy^2}|\) makes (A8) integrable on \(\Gamma\): it decays exponentially on both rays and stays bounded on the finite segment. Dominated convergence in (A6) thus gives the limit \(\int_\Gamma e^{iy^2}\,dy\), simultaneously at both frequency ends.

For completeness this contour Gaussian has the exact value
\[
\int_\Gamma e^{iy^2}\,dy=\sqrt\pi\,e^{i\pi/4}.
\tag{A9}
\]
To check it without an unevaluated Fresnel integral, apply the same contour deformation to \(e^{-(\varepsilon-i)y^2}\), \(0<\varepsilon\le1\). The real integral is the positive-real-part Gaussian value \(\sqrt\pi(\varepsilon-i)^{-1/2}\), with the root continued from positive real arguments. On the rays of \(\Gamma\),
\[
|e^{-(\varepsilon-i)(s+ih)^2}|
=e^{-\varepsilon(s^2-h^2)-2sh}
\le e^{1/4}e^{-|s|}.
\]
The vertical-end estimates also tend to zero, since their extra factor \(e^{-\varepsilon R^2+\varepsilon h^2}\) is harmless. The finite segment is bounded uniformly in \(\varepsilon\). Dominated convergence on \(\Gamma\) and the chosen Gaussian root yield (A9), since \((\varepsilon-i)^{-1/2}\to e^{i\pi/4}\). Equations (A6)--(A9) prove (A1).

Finally the nonzero modulus in (A1) supplies constants \(c_a,C_a>0\) and \(R_a\) such that
\[
\begin{gathered}
c_a|\xi|^{-a}\le |F_a(\xi)|\le C_a|\xi|^{-a},
\\ |\xi|\ge R_a.
\end{gathered} \tag{A10}
\]
Continuity bounds \(F_a\) on the remaining compact interval, proving global boundedness. For finite \(p\), (A10) reduces integrability at either infinity to \(\int_{R_a}^\infty t^{-ap}\,dt\), which is finite exactly when \(ap>1\); equality \(ap=1\) diverges logarithmically. The compact interval causes no obstruction. For \(p=\infty\), the continuous compact bound and the tail bound give membership for every \(a>0\). This proves the entire source question and every endpoint. \(\square\)

## B. Every real polynomial phase and its entire transform

**Theorem B (entire polynomial profiles).** Let \(p(x)=\sum_{j=0}^m a_jx^j\) have real coefficients, \(a_m\ne0\) and \(m>1\). The tempered Fourier transform of \(e^{ip(x)}\) is the restriction to the real axis of an entire function \(F\). With \(D_\zeta=-i\,d/d\zeta\), it satisfies
\[
\begin{gathered}
\bigl(p'(-D_\zeta)-\zeta\bigr)F(\zeta)=0,
\\ \zeta\in\mathbb C.
\end{gathered} \tag{B1}
\]
This is a homogeneous equation of exact order \(m-1\). Its coefficients are constant except for the affine coefficient of the undifferentiated function.

**Proof for degree two.** Write \(p(x)=a x^2+b x+c,\ a\ne0\). The signed scalar Gaussian boundary formula, with the transform convention specified above, gives on real frequencies
\[
\begin{gathered}
F(\xi)=\sqrt{\pi/|a|}\,e^{i\pi\operatorname{sgn}(a)/4+ic}
\\ {}\cdot\exp\!\left(-\frac{i(\xi-b)^2}{4a}\right).
\end{gathered} \tag{B2}
\]
The right side extends to an entire function of \(\zeta\). Its real restriction is bounded, hence tempered. Formula (B2) follows from the full damped Gaussian identity in the linked complex Gaussian proof and the modulation identity; it uses the actual signature phase. The differential equation will be verified below for every degree.

**Proof for degree at least three.** Choose
\[
h_+=\operatorname{sgn}(a_m),\qquad
h_-=\operatorname{sgn}\bigl(a_m(-1)^{m-1}\bigr).
\]
Let \(\Gamma_p\) run along \(x+ih_-\) for \(x\le0\), then from \(ih_-\) to \(ih_+\) on the imaginary axis, and then along \(x+ih_+\) for \(x\ge0\), in this orientation. If \(h_-=h_+\), the connecting segment is empty. The polynomial is entire, so this contour has no branch restrictions.

On either ray, with its respective fixed \(h\), expansion of the real-coefficient polynomial gives
\[
\begin{gathered}
\operatorname{Im}p(x+ih)
\\ =m a_m h x^{m-1}+O(|x|^{m-2})
\\ \ge c|x|^{m-1}.
\end{gathered} \tag{B3}
\]
for sufficiently large \(|x|\); the choices of \(h_\pm\) make the leading term positive at both ends. For any compact set \(K\subset\mathbb C\), put \(M_K=\sup_{\zeta\in K}|\zeta|\). Since
\[
\begin{gathered}
|e^{i(p(z)-\zeta z)}|
\\ =\exp\!\left(\begin{gathered}
-\operatorname{Im}p(z)
\\ {}+(\operatorname{Im}\zeta)\operatorname{Re}z
\\ {}+(\operatorname{Re}\zeta)\operatorname{Im}z
\end{gathered}\right),
\end{gathered}
\]
the integrand on the rays is bounded uniformly for \(\zeta\in K\) by
\[
C_K\exp(-c|x|^{m-1}+M_K|x|).
\tag{B4}
\]
As \(m-1\ge2\), this is integrable even after multiplication by any power of \(|x|\). Therefore
\[
F(\zeta)=\int_{\Gamma_p}e^{i(p(z)-\zeta z)}\,dz
\tag{B5}
\]
converges absolutely and locally uniformly. Expanding \(e^{-i(\zeta-\zeta_0)z}\) in its power series on a closed disc about any \(\zeta_0\), (B4) dominates the sum by an additional factor \(e^{r|z|}\). Termwise integration thus gives a convergent local complex power series, and also every derivative
\[
\begin{gathered}
F^{(k)}(\zeta)=
\\ \int_{\Gamma_p}(-iz)^k e^{i(p(z)-\zeta z)}\,dz.
\end{gathered} \tag{B6}
\]
This proves joint integrability and entire analyticity directly; degree two was handled separately because a fixed horizontal contour in that case only gives a finite strip of absolute convergence for complex frequency.

To identify (B5) with the actual Fourier transform, take real \(\xi\). The real improper tails of \(e^{i(p(x)-\xi x)}\) converge uniformly for \(\xi\) in compact real sets. Integration by parts uses
\[
e^{i(p(x)-\xi x)}
=\frac{1}{i(p'(x)-\xi)}\frac{d}{dx}e^{i(p(x)-\xi x)}.
\]
For \(|x|\ge R\) with \(R\) sufficiently large, \(|p'(x)-\xi|\ge c|x|^{m-1}\) and \(|p''(x)|\le C|x|^{m-2}\). The endpoint and the integral of the differentiated reciprocal give a tail bound \(C R^{-m+1}\), since \(\int_R^\infty x^{-m}\,dx=R^{-m+1}/(m-1)\).

The contour deformation has vanishing vertical ends as well. At \(z=\pm R+it\), where \(t\) lies between \(0\) and the corresponding \(h_\pm\), polynomial expansion, uniformly over this bounded interval of heights, gives
\[
\begin{gathered}
\operatorname{Im}p(\pm R+it)
\\ =m a_m t(\pm R)^{m-1}
\\ {}+O(|t|R^{m-2})
\\ \ge c|t|R^{m-1}.
\end{gathered} \tag{B7}
\]
The error has a factor \(|t|\), because the imaginary part vanishes at \(t=0\) for real coefficients. Thus the absolute integral on either end is at most
\[
\begin{gathered}
\int_0^1 e^{-(cR^{m-1}-|\xi|)s}\,ds
\\ \le C R^{-m+1}.
\end{gathered} \tag{B8}
\]
for sufficiently large \(R\), uniformly on compact real frequency sets. Cauchy's theorem on the bounded regions and (B8) show that (B5) equals the real improper integral for every real \(\xi\).

The real restriction has polynomial growth. Choose
\[
R_\xi=C_p(1+|\xi|)^{1/(m-1)}
\]
large enough that the preceding reciprocal derivative estimates hold on both tails for this \(\xi\). The middle real interval contributes at most \(2R_\xi\), because its integrand has modulus one, while the two tails contribute at most \(C R_\xi^{-m+1}\). Hence
\[
|F(\xi)|\le C_p'(1+|\xi|)^{1/(m-1)}.
\tag{B9}
\]
The bounded truncations of \(e^{ip(x)}\) converge to it in \(\mathcal S'\). Their transforms tend locally uniformly on the real axis to (B5), by the compact-uniform tail estimate. Consequently they identify its distributional transform on compactly supported tests. Polynomial growth makes the restriction tempered, and the same cutoff density argument used in Theorem A identifies the two tempered distributions. This proves the full Fourier statement, including its distributional meaning.

**Proof of the equation and its order.** As a smooth bounded function, \(f=e^{ip(x)}\) obeys
\[
D_xf=p'(x)f,\qquad D_x=-i\partial_x.
\]
The right side has polynomial growth, so the equality holds in \(\mathcal S'\). The exact Fourier derivative and multiplication rules are
\[
\mathcal F(D_xf)=\xi F,\qquad
\mathcal F(xf)=i\partial_\xi F=-D_\xi F.
\]
Applying them to the polynomial \(p'\) gives \(p'(-D_\xi)F=\xi F\) as a distributional identity on the real axis. The entire representative makes both sides continuous there, so they agree pointwise there. For complex \(\zeta\) and \(m\ge3\), (B6) proves directly that
\[
\begin{gathered}
(p'(-D_\zeta)-\zeta)F(\zeta)
\\ =\int_{\Gamma_p}(p'(z)-\zeta)e^{i(p(z)-\zeta z)}\,dz
\\ =\frac1i\int_{\Gamma_p}\frac{d}{dz}e^{i(p(z)-\zeta z)}\,dz=0.
\end{gathered}
\]
The intermediate endpoints of the three oriented pieces cancel exactly; (B4) makes both infinite endpoints zero. Thus no unprovided accumulation-set identity principle is required. For \(m=2\), differentiating (B2) gives \(F'=-i(\zeta-b)F/(2a)\), hence \((2ai\,d/d\zeta+b-\zeta)F=0\) directly on \(\mathbb C\). The coefficient of the highest derivative is \(m a_m i^{m-1}\ne0\), because \(-D_\zeta=i\,d/d\zeta\). Thus the differential equation has exact order \(m-1\); its zeroth coefficient is \(a_1-\zeta\), and all remaining coefficients are constant. This establishes (B1) with every sign and coefficient retained. \(\square\)

## Read degree, sign and damping from a polynomial transform

**T2. Degree sets the frequency scale and the origin phase.** Let \(F_{m,\lambda}\) be the entire transform of
\(e^{i\lambda x^m/m}\), where \(m\ge2\) is an integer and \(\lambda\ne0\) is real. A positive real change of variables gives

\[
\begin{gathered}
F_{m,\lambda}(\zeta)=|\lambda|^{-1/m}
\\ {}\times F_{m,\operatorname{sgn}\lambda}
(\zeta/|\lambda|^{1/m}).
\end{gathered}\tag{T2}
\]

For example, \(\lambda=8,m=3\), or \(\lambda=16,m=4\), doubles the frequency scale and halves the profile amplitude. The origin values for positive unit coefficient are

- Cubic: \(F_{3,1}(0)=3^{-1/6}\Gamma(1/3)\).
- Quartic: \(F_{4,1}(0)=2^{-1/2}e^{i\pi/8}\Gamma(1/4)\).
- Degree five: \(F_{5,1}(0)=2\,5^{-4/5}\cos(\pi/10)\Gamma(1/5)\).
- Degree six: \(F_{6,1}(0)=2\,6^{-5/6}e^{i\pi/12}\Gamma(1/6)\).

Solution 10 proves these values and every derivative at the origin by absolutely convergent gamma integrals. For odd degree, reversing \(\lambda\) leaves this origin value real and unchanged; for even degree it reverses its phase. The real stationary-point equation is \(\lambda x^{m-1}=\xi\). Even degree has one real stationary point at every frequency. Odd degree has two when \(\xi/\lambda>0\), none when \(\xi/\lambda<0\), and a degenerate point at zero. These counts explain which real geometry the entire profile crosses; they alone do not supply a Fourier asymptotic.

**T3. A Gaussian contour measures the cubic profile.** Write \(F=F_{3,1}\). Its real restriction equals \(2\pi\operatorname{Ai}(-\xi)\), using the cosine integral in [NIST DLMF, §9.5.1](https://dlmf.nist.gov/9.5.E1): the cubic phase is odd, so the two real half-line integrals combine into twice that cosine integral. This identifies the normalization of the Airy name. Theorem B and Solution 5 below prove the receiving entire Fourier identity, differential equation and initial values.

For any \(h>0\), the horizontal contour \(z=x+ih\) gives the absolute Gaussian integral

\[
\begin{gathered}
F(\zeta)=e^{h^3/3+h\zeta}
\\ {}\times\int_{\mathbb R}\exp\!\left[\begin{gathered}
-hx^2+ix^3/3
\\ {}-i(\zeta+h^2)x
\end{gathered}\right]dx.
\end{gathered}\tag{T3}
\]

Indeed \(i(x+ih)^3/3=ix^3/3-hx^2-ih^2x+h^3/3\); the linear Fourier factor contributes \(-i\zeta x+h\zeta\). The Gaussian makes this integral and all frequency derivatives absolute on compact complex-frequency sets. Solution 11 proves the contour operation and its exact signed-coefficient version.

If \(F_h(\zeta)=\int e^{-hx^2+ix^3/3-i\zeta x}dx\), that same solution gives

\[
\begin{gathered}
F_h(0)=e^{2h^3/3}F(-h^2)
\\ =F(0)-h^2F'(0)+O(h^3),
\\ h\downarrow0.
\end{gathered}\tag{T4}
\]

Here \(F'(0)=3^{1/6}\Gamma(2/3)>0\). The first change in this particular measured value is quadratic in the damping parameter, because the cubic equation gives \(F''(0)=0\). This sharper pointwise behavior is established by the entire formula; the strong distributional convergence also has its own bounded-test estimate.

## Exercises

**Exercise 1 (foundation: affine changes of a weighted chirp).** Let \(\lambda\ne0\) and \(h,\beta,\gamma\in\mathbb R\). Find the full Fourier transform of
\[
g(x)=f_a(\lambda(x-h))e^{i\beta x+i\gamma}.
\]
Determine its two-ended complex asymptotic and every \(L^p\) endpoint. Retain the sign of \(\lambda\) in the argument and its absolute value in the Jacobian.

**Exercise 2 (foundation: products and separate integrability thresholds).** For \(d\ge1\) and \(a_1,\ldots,a_d>0\), transform \(\prod_{j=1}^d f_{a_j}(x_j)\). Determine exactly when the result belongs to \(L^p(\mathbb R^d)\). State the joint asymptotic as every \(|\xi_j|\) tends to infinity, without imposing a radial asymptotic near coordinate axes.

**Exercise 3 (intermediate: logarithmic moments).** For an integer \(k\ge0\), transform
\[
g_{a,k}(x)=(1+x^2)^{-a/2}\log(1+x^2)^k e^{ix^2}.
\]
Prove a complex asymptotic including its logarithmic factor, and determine all \(L^p\) endpoints. Justify the complex logarithm and the domination in the shifted contour integral.

**Exercise 4 (advanced: a critical logarithmic correction).** For \(a>0\) and \(b\in\mathbb R\), consider
\[
g_{a,b}(x)=(1+x^2)^{-a/2}[\log(e+x^2)]^{-b}e^{ix^2}.
\]
Show that its Fourier transform is continuous and bounded, find its leading complex asymptotic, and determine exactly when it lies in \(L^p\). Include the case \(ap=1\).

**Exercise 5 (intermediate: the cubic equation and its initial values).** Let \(F\) be the entire transform of \(\exp(ix^3/3)\). Find its differential equation and \(F(0),F'(0)\), using only absolutely convergent positive gamma integrals. Justify the contour rotations at both ends.

**Exercise 6 (advanced: quartic phases and power-series data).** Let \(F\) be the entire transform of \(\exp(ix^4/4)\). Determine its parity, differential equation, \(F(0),F'(0),F''(0)\), and the recurrence for its Taylor coefficients. Give the coefficients of \(\zeta^4\) and \(\zeta^6\), with their phases.

**Exercise 7 (intermediate: affine polynomial phases and their equation).** For the polynomial \(p\) in Theorem B, transform
\[
e^{i[p(\lambda(x-h))+\beta x+\gamma]},\qquad \lambda\ne0.
\]
Find the exact order-\((\deg p-1)\) equation of the resulting entire function and its highest derivative coefficient.

**Exercise 8 (advanced: Gaussian regularization in the complex plane).** For \(\varepsilon>0\), set
\[
F_\varepsilon(\zeta)=\int_{\mathbb R}
e^{-\varepsilon x^2+ip(x)-i\zeta x}\,dx.
\]
Show that these entire functions converge locally uniformly, together with every derivative, to Theorem B's entire transform. Treat degree two separately. Also prove strong convergence of the inputs in \(\mathcal S'\).

**Exercise 9 (advanced: shell mass and the weak endpoint).** For Theorem A's \(F_a\), prove (T1) for every \(L>1\) and finite \(p\ge1\). If \(\mu_a(s)\) is the Lebesgue measure of \(\{\xi:|F_a(\xi)|>s\}\), find the exact limit of \(s^{1/a}\mu_a(s)\) as \(s\downarrow0\). Classify precisely when
\(\sup_{s>0}s\,\mu_a(s)^{1/p}<\infty\); this is the weak \(L^p\) criterion used here. Compare it with the strong \(L^p\) criterion, including equality.

**Exercise 10 (advanced: every pure monomial and every origin derivative).** For \(F_{m,\lambda}\) in T2, find \(F_{m,\lambda}^{(k)}(0)\) for every integer \(k\ge0\), with exact gamma constants and both ray phases. Prove the formula using absolute contours even when the corresponding undamped real moment does not converge. Give the Taylor recurrence from its differential equation, the scaling in (T2), and an explicit bound of the form
\(C_{m,\lambda}\exp(C'_{m,\lambda}|\zeta|^{m/(m-1)})\).

**Exercise 11 (advanced: exact cubic regularization).** For real \(\lambda\ne0\) and \(\varepsilon>0\), put
\(F_{\lambda,\varepsilon}(\zeta)=\int e^{-\varepsilon x^2+i\lambda x^3/3-i\zeta x}dx\), and write \(F_\lambda=F_{3,\lambda}\). Prove an exact formula expressing \(F_{\lambda,\varepsilon}\) through a shifted \(F_\lambda\), for every complex frequency and either sign of \(\lambda\). Derive its frequency ODE and its damping-parameter heat equation. Prove convergence on every compact complex-frequency set with all derivatives, give the first correction and an explicit remainder bound for the function itself, and prove strong tempered convergence. Recover (T3) and (T4).

## Solutions

**Solution 1.** Put \(\eta=\xi-\beta\) and \(y=\lambda(x-h)\). The real change of variables, including reversal of the limits when \(\lambda<0\), gives
\[
\widehat g(\xi)=e^{i\gamma-i\eta h}|\lambda|^{-1}F_a(\eta/\lambda).
\tag{P1}
\]
For the tempered identity, apply the change of variables to compactly truncated inputs and pass to \(\mathcal S'\); the continuous right side is the resulting regular distribution. Theorem A gives
\[
\begin{gathered}
e^{i\eta h+i(\eta/\lambda)^2/4-i\gamma}
\\ {}\cdot|\eta|^a\widehat g(\xi)
\\ \longrightarrow 2^a|\lambda|^{a-1}\sqrt\pi\,e^{i\pi/4},
\\ |\xi|\longrightarrow\infty.
\end{gathered} \tag{P2}
\]
The constant is nonzero at both ends. Multiplication by the phase, translation of the frequency and a nonzero dilation preserve the finiteness of the \(L^p\) norm. Consequently, for finite \(p\ge1\), membership is equivalent to \(ap>1\); for \(p=\infty\) it holds for every \(a>0\). Formula (P1) uses \(\eta/\lambda\), rather than \(\eta/|\lambda|\).

**Solution 2.** The result is
\[
F(\xi_1,\ldots,\xi_d)=\prod_{j=1}^d F_{a_j}(\xi_j).
\tag{P3}
\]
Here is a justification for the full distribution. Truncate each input to \([-R,R]\). Their product tends to the untruncated product in \(\mathcal S'\), because the inputs have modulus at most one and Schwartz tests are integrable. Fubini gives the product of the finite one-dimensional integrals for the transform. Those factors converge locally uniformly by Theorem A's tail estimate. Thus (P3) agrees with the Fourier transform on compactly supported smooth tests. Its right side is bounded; the density of these tests in \(\mathcal S\) gives the full tempered identity.

For finite \(p\), Tonelli applies to \(\prod_j|F_{a_j}|^p\). If every \(a_jp>1\), its integral is the product of finite one-dimensional integrals. Conversely, if one integral diverges, select a compact interval in every other coordinate on which that factor's integral is positive. Such intervals exist because the nonzero asymptotic excludes an identically zero factor. The integral over the resulting cylinder diverges. Hence membership is equivalent to all \(a_jp>1\). Boundedness holds for \(p=\infty\). When \(\min_j|\xi_j|\to\infty\), multiplication of the separate limits gives
\[
\begin{gathered}
F(\xi)\sim\pi^{d/2}2^{\sum_j a_j}
\\ {}\cdot\prod_j|\xi_j|^{-a_j}
\\ {}\cdot\exp\!\left(-\frac{i}{4}\sum_j\xi_j^2+\frac{id\pi}{4}\right).
\end{gathered} \tag{P4}
\]
The limiting regime in this statement requires every coordinate to be large.

**Solution 3.** Write \(L(z)=\operatorname{Log}(1+z^2)\) on the strip used in Theorem A. It is the same positive-real continuation as the branch of \(w_a(z)=(1+z^2)^{-a/2}\). The analytic amplitude is \(w_a(z)L(z)^k\). Its real tail is \(O(|x|^{-a}(1+\log|x|)^k)\), and its derivative is \(O(|x|^{-a-1}(1+\log|x|)^k)\). The integration by parts in Theorem A therefore gives locally uniform convergence of the real-frequency tails, with error \(O(R^{-a-1}(1+\log R)^k)\). The same factor occurs in the vertical-end estimate. The finite-contour argument yields a continuous transform and the absolutely convergent contour representation.

Put \(t=\xi/2\) and \(r=|t|\). After completing the square and translating the contour back, that representation is
\[
\begin{gathered}
\widehat g_{a,k}(\xi)=e^{-i\xi^2/4}
\\ {}\cdot\int_\Gamma w_a(z+t)L(z+t)^k e^{iz^2}\,dz.
\end{gathered} \tag{P5}
\]
For each fixed \(z\), \(r^aw_a(z+t)\to1\) and
\[
L(z+t)-2\log r\longrightarrow0
\quad(r\longrightarrow\infty).
\]
The latter follows by writing \(1+(z+t)^2=r^2q\), where \(q\to1\), and using the positive scaling rule of the same logarithm.

We verify domination rather than merely exchanging limits. On the rays write \(z=s+ih\), \(|h|=1/2\), and assume \(r\ge2\). Theorem A bounds \(r^a|w_a(z+t)|\) by \(C_a(1+|s|)^a\). Moreover,
\[
\begin{gathered}
\frac{|L(z+t)|}{2\log r}
\\ \le C\bigl(1+\log(1+|s|)\bigr).
\end{gathered} \tag{P6}
\]
Indeed \(|1+(s+t+ih)^2|\) is bounded below by \(3/4\), bounded above by \(C(1+r+|s|)^2\), and its logarithm's imaginary part is bounded by \(\pi/2\). These bounds imply (P6) using \(\log r\ge\log2\). The central segment is handled by the same bounds on a compact set. The integrable dominator is a polynomial times a power of \(1+\log(1+|s|)\), multiplied on the rays by \(e^{-|s|}\). Dominated convergence and the signed Fresnel integral give
\[
\begin{gathered}
e^{i\xi^2/4}r^a(2\log r)^{-k}
\\ {}\cdot\widehat g_{a,k}(\xi)\longrightarrow\sqrt\pi\,e^{i\pi/4}.
\end{gathered} \tag{P7}
\]
For \(k=0\) the logarithmic normalization is simply one. This proves boundedness and identifies the full tempered transform, as in Theorem A. Its modulus is comparable at infinity to \(|\xi|^{-a}(\log|\xi|)^k\). For finite \(p\), \(ap>1\) gives integrability and \(ap<1\) gives divergence. At \(ap=1\), the integral of \(\xi^{-1}(\log\xi)^{kp}\) diverges since \(kp\ge0\). Thus the finite-\(p\) criterion remains \(ap>1\), and the transform is bounded for every permitted \(a,k\).

**Solution 4.** Let \(L_e(z)=\operatorname{Log}(e+z^2)\). On \(|\operatorname{Im}z|\le1/2\), \(e+z^2\) has real part at least \(e-1/4>1\). Hence
\[
\operatorname{Re}L_e(z)=\log|e+z^2|
\ge\log(e-1/4)>0.
\]
We can therefore define \(L_e(z)^{-b}\) by the same right-half-plane logarithm applied a second time. This branch is analytic on a neighborhood of the contour and agrees with the positive real power in the question. On that strip,
\[
\begin{gathered}
c\log(e+(s+t)^2)
\\ \le |L_e(s+t+ih)|
\\ \le C\log(e+(s+t)^2).
\end{gathered} \tag{P8}
\]
with fixed positive constants; the bounded imaginary part and the positive lower bound prove this comparison.

The real amplitude and its first derivative satisfy bounds \(O(|x|^{-a}(1+\log|x|)^{|b|})\) and \(O(|x|^{-a-1}(1+\log|x|)^{|b|})\). Thus the real tails and vertical ends vanish by the same integration by parts and contour estimates as above. Completing the square yields (P5) with \(L^k\) replaced by \(L_e^{-b}\).

Pointwise on the translated contour,
\[
r^aw_a(z+t)\to1,\qquad
\frac{L_e(z+t)}{2\log r}\to1.
\]
For completeness both the ratio and its reciprocal admit a polynomial bound in \(1+|s|\), uniformly for \(r\ge2\). The upper ratio is bounded by \(C(1+\log(1+|s|))\), as in (P6). For the reciprocal, if \(|s+t|\ge r/2\), (P8) bounds it by a fixed constant. In the remaining case \(|s|\ge r/2\); the fixed lower bound in (P8) bounds the reciprocal by \(C\log r\le C(1+|s|)\). The argument of \(L_e\) lies in \((-\pi/2,\pi/2)\), so a fixed real complex power has modulus exactly \(|L_e|^{-b}\). These estimates, with Theorem A's amplitude bound, give a polynomial dominator times \(e^{-|s|}\) for either sign of \(b\). We obtain
\[
\begin{gathered}
\widehat g_{a,b}(\xi)\sim\sqrt\pi\,e^{i\pi/4-i\xi^2/4}
\\ {}\cdot(|\xi|/2)^{-a}
\\ {}\cdot[2\log(|\xi|/2)]^{-b}.
\end{gathered} \tag{P9}
\]
The continuous transform is bounded since \(a>0\), and the full \(\mathcal S'\) identity follows from this bound and the compact-test argument.

For finite \(p\), the tail integral is comparable to
\(\int^\infty x^{-ap}(\log x)^{-bp}\,dx\).
If \(ap>1\), it converges for every \(b\); if \(ap<1\), it diverges for every \(b\). One can see both statements from \((\log x)^c=o(x^\delta)\) for every fixed \(c,\delta>0\), which follows on putting \(x=e^t\). At \(ap=1\), the substitution \(t=\log x\) gives \(\int^\infty t^{-bp}\,dt\), finite exactly when \(bp>1\). Thus the criterion is
\[
ap>1\quad\hbox{or}\quad(ap=1\ \hbox{and}\ bp>1).
\]
For \(p=\infty\), boundedness always holds.

**Solution 5.** Theorem B's equation is \((p'(i\partial_\zeta)-\zeta)F=0\). For \(p'(x)=x^2\), it reads
\[
F''(\zeta)+\zeta F(\zeta)=0.
\tag{P10}
\]
To find initial values, rotate the positive ray to angle \(\pi/6\) and the negative ray to angle \(5\pi/6\), both in the upper half-plane. On either ray \(z^3=it^3\), so the exponential is \(e^{-t^3/3}\). The contour is oriented from infinity on the negative ray through zero to infinity on the positive ray. Consequently
\[
\begin{gathered}
\int_\Gamma z^k e^{iz^3/3}\,dz
\\ =\bigl(e^{i(k+1)\pi/6}-e^{i(k+1)5\pi/6}\bigr)J_k,
\\ J_k=\int_0^\infty t^k e^{-t^3/3}\,dt.
\end{gathered} \tag{P11}
\]
For \(k=0,1\), the real improper integrals converge by integration by parts: \(x^k/p'(x)\) tends to zero and its derivative is \(O(|x|^{k-3})\). The arc at radius \(R\) in each rotation is bounded by
\[
C R^{k+1}\int_0^{\pi/6}e^{-R^3\sin(3\theta)/3}\,d\theta
\le C R^{k-2}.
\]
Here \(\sin(3\theta)\ge c\theta\) on the interval; the negative arc has the identical estimate after measuring the angle from \(\pi\). Both vanish for \(k=0,1\), proving (P11) by the finite-contour interface. The derivative \(F'(0)\) is also the \(k=1\) integral multiplied by \(-i\): Theorem B permits differentiation on its absolutely convergent contour, and the same deformation identifies that integral with the real one.

Define \(\Gamma(s)=\int_0^\infty v^{s-1}e^{-v}\,dv\) for the positive \(s\) used here. Substitution \(v=t^3/3\) gives \(J_k=3^{(k-2)/3}\Gamma((k+1)/3)\). The phase differences in (P11) are \(\sqrt3\) for \(k=0\) and \(i\sqrt3\) for \(k=1\). Hence
\[
\begin{gathered}
F(0)=3^{-1/6}\Gamma(1/3),
\\ F'(0)=3^{1/6}\Gamma(2/3).
\end{gathered} \tag{P12}
\]
These are positive real initial values; the factor \(-i\) in the Fourier derivative is essential for the second sign.

**Solution 6.** Reflection of the input gives \(F(-\zeta)=F(\zeta)\), first for real \(\zeta\) by the distributional reflection formula, and for complex \(\zeta\) by reflecting the absolutely convergent defining contours. Equivalently, symmetric contour rays give the same integral after \(z\mapsto-z\). The polynomial equation is
\[
\begin{gathered}
-iF'''(\zeta)-\zeta F(\zeta)=0,
\\ F'''(\zeta)=i\zeta F(\zeta).
\end{gathered} \tag{P13}
\]
For the initial integrals, rotate the positive ray to angle \(\pi/8\) and the negative ray to angle \(9\pi/8\). The negative ray now lies below the real axis. On both rays \(z^4=it^4\). Their oriented phase difference is
\[
\begin{gathered}
e^{i(k+1)\pi/8}-e^{i(k+1)9\pi/8}
\\ =\bigl(1-(-1)^{k+1}\bigr)e^{i(k+1)\pi/8}.
\end{gathered} \tag{P14}
\]
For \(k=0,1,2\), real tails converge by integration by parts, and the rotation arcs are \(O(R^{k-3})\), by the same argument with \(\sin(4\theta)\) and \(R^4\). Thus the necessary moments agree with the rotated integrals. Substitution \(v=t^4/4\) gives
\[
\int_0^\infty t^k e^{-t^4/4}\,dt
=4^{(k-3)/4}\Gamma((k+1)/4).
\]
Multiplying by the Fourier derivative factors \(1,-i,(-i)^2\), respectively, yields
\[
F(0)=2^{-1/2}e^{i\pi/8}\Gamma(1/4),\qquad F'(0)=0,
\]
\[
F''(0)=-\sqrt2\,e^{3i\pi/8}\Gamma(3/4).
\tag{P15}
\]
In particular the second derivative carries a minus sign.

Write \(F(\zeta)=\sum_{k\ge0}c_k\zeta^k\). Entire convergence permits coefficient comparison in (P13). Its constant coefficient gives \(c_3=0\); for \(k\ge1\),
\[
\begin{gathered}
c_{k+3}=
\\ \frac{i\,c_{k-1}}{(k+3)(k+2)(k+1)}.
\end{gathered} \tag{P16}
\]
The initial data are \(c_0=F(0),c_1=0,c_2=F''(0)/2\). Therefore
\[
\begin{gathered}
c_4=\frac{iF(0)}{24}
\\ =\frac{i\,2^{-1/2}e^{i\pi/8}\Gamma(1/4)}{24},
\\ c_6=\frac{iF''(0)}{240}
\\ =-\frac{i\sqrt2\,e^{3i\pi/8}\Gamma(3/4)}{240}.
\end{gathered}
\]
The recurrence also gives every odd coefficient as zero, consistently with the reflection argument.

**Solution 7.** The same change of variables as in Solution 1 gives, first for real \(\zeta\),
\[
\begin{gathered}
G(\zeta)=e^{i\gamma-i(\zeta-\beta)h}|\lambda|^{-1}
\\ {}\cdot F((\zeta-\beta)/\lambda).
\end{gathered} \tag{P17}
\]
The right side is entire and represents the full tempered Fourier transform on the real axis. It is therefore an entire extension supplied without any improper complex-frequency real integral.

One can verify its equation directly for every complex \(\zeta\). Conjugating \(i\partial_\zeta-h\) by the exponential in (P17) gives \(\lambda^{-1}i\partial_\eta\), where \(\eta=(\zeta-\beta)/\lambda\). Theorem B's full complex equation \((p'(i\partial_\eta)-\eta)F=0\) then gives
\[
\begin{gathered}
\bigl[\lambda p'\bigl(\lambda(i\partial_\zeta-h)\bigr)
\\ {}+\beta-\zeta\bigr]G(\zeta)=0.
\end{gathered} \tag{P18}
\]
For \(p(x)=a_mx^m+\cdots\), the highest derivative coefficient is \(ma_m\lambda^m i^{m-1}\), which is nonzero. All remaining coefficients are constant except the displayed linear term \(-\zeta\). The identical equation also follows by Fourier transforming the derivative of the original phase, \(\lambda p'(\lambda(x-h))+\beta\). The absolute Jacobian and the signed power \(\lambda^m\) play different roles and are both retained.

**Solution 8.** For a fixed \(\varepsilon>0\), the Gaussian dominates every polynomial moment and every compact complex-frequency exponential \(e^{M|x|}\). It justifies differentiation under the integral to all orders, or a uniformly convergent local power series, and proves \(F_\varepsilon\) entire.

Suppose \(m=\deg p\ge3\). Use Theorem B's two horizontal rays of heights \(h_\pm=\pm1\), chosen with the signs that make \(\operatorname{Im}p(z)\) positive at the corresponding real ends, joined by its finite imaginary segment. For \(\zeta\) in a compact set and on a vertical end of real part \(\pm R\), the additional Gaussian has modulus \(e^{-\varepsilon R^2+\varepsilon(\operatorname{Im}z)^2}\). The estimate for \(\operatorname{Im}p(\pm R+it)\), with its factor \(|t|R^{m-1}\), bounds the end integral, including a \(k\)th frequency derivative, by
\[
C_{\varepsilon,k}R^{k-m+1}e^{-\varepsilon R^2+MR}.
\]
It tends to zero for each \(\varepsilon>0\). Thus every derivative is represented on the same contour. For \(0<\varepsilon\le1\), on its horizontal rays
\[
|e^{-\varepsilon z^2}|
=e^{-\varepsilon(\operatorname{Re}z)^2+\varepsilon h_\pm^2}
\le e.
\]
Theorem B's ray bound is \(e^{-c|s|^{m-1}+M|s|+C_M}\); multiplying it by \(|z|^k\) remains integrable because \(m-1\ge2\). The connecting segment is compact. Dominated convergence, uniformly on each compact frequency set, proves \(F_\varepsilon^{(k)}\to F^{(k)}\) for every \(k\).

For degree two write \(p(x)=ax^2+bx+c\), \(a\ne0\). The positive-real Gaussian formula gives
\[
\begin{gathered}
F_\varepsilon(\zeta)=\sqrt\pi\,(\varepsilon-ia)^{-1/2}e^{ic}
\\ {}\cdot\exp\!\left(-\frac{(\zeta-b)^2}{4(\varepsilon-ia)}\right).
\end{gathered} \tag{P19}
\]
The root is continued from the right half-plane. As \(\varepsilon\downarrow0\), its prefactor tends to \(\sqrt{\pi/|a|}\,e^{i\pi\operatorname{sgn}(a)/4+ic}\), and the exponential tends to \(\exp(-i(\zeta-b)^2/(4a))\). The explicit formula and all its derivatives converge uniformly on compact sets. The higher-degree horizontal-ray argument would not give domination for arbitrary complex frequencies at degree two.

Finally, for any bounded subset \(\mathcal B\) of \(\mathcal S\),
\[
\begin{gathered}
\sup_{\phi\in\mathcal B}
\\ \left|\int(e^{-\varepsilon x^2}-1)e^{ip(x)}\phi(x)\,dx\right|
\\ \le\varepsilon\sup_{\phi\in\mathcal B}\int x^2|\phi(x)|\,dx
\\ \le C_{\mathcal B}\varepsilon.
\end{gathered}
\]
The last supremum is finite by a Schwartz seminorm, for example \(\sup_x(1+|x|)^4|\phi(x)|\). This proves strong convergence in \(\mathcal S'\); continuity of Fourier transformation on the strong dual gives strong convergence of the transforms on the real axis as well.

**Solution 9.** Put \(A_a=2^a\sqrt\pi\). Theorem A's two-ended nonzero asymptotic means that for every \(0<\eta<1\), there is \(R_\eta\) such that
\((1-\eta)A_a|\xi|^{-a}\leq|F_a(\xi)|\leq(1+\eta)A_a|\xi|^{-a}\) for \(|\xi|\geq R_\eta\). In the shell integral substitute \(\xi=Ru\) separately at the two signs. The ratio \(|F_a(Ru)|/(A_a|Ru|^{-a})\) tends uniformly to one for \(1\leq|u|\leq L\), by the same tail inequalities. Therefore

\[
\begin{gathered}
R^{ap-1}\int_{R<|\xi|<LR}|F_a(\xi)|^p d\xi
\\ \longrightarrow 2A_a^p H_{ap}(L),
\\ H_v(L)=\int_1^L u^{-v}du
\\ =\begin{cases}
\dfrac{L^{1-v}-1}{1-v},&v\ne1,\\
\log L,&v=1.
\end{cases}
\end{gathered}\tag{T5}
\]

This includes the fixed nonzero shell mass at the critical power; for \(a=1/2,p=2,L=2\), its value is \(4\pi\log2\).

No monotonicity of the transform is needed to find its level-set measure. For sufficiently small \(s>0\), the lower tail bound includes the two intervals
\(R_\eta<|\xi|<[(1-\eta)A_a/s]^{1/a}\) in \(\{|F_a|>s\}\). The upper tail bound confines the portion outside \([-R_\eta,R_\eta]\) to \(|\xi|<[(1+\eta)A_a/s]^{1/a}\). The remaining central interval has measure at most \(2R_\eta\). After multiplication by \(s^{1/a}\), these finite central lengths disappear. Letting \(s\downarrow0\), then \(\eta\downarrow0\), proves

\[
\begin{gathered}
s^{1/a}\mu_a(s)\longrightarrow2A_a^{1/a}
\\ =4\pi^{1/(2a)}.
\end{gathered}\tag{T6}
\]

For every positive \(s\) the measure is finite, because \(F_a\) tends to zero at both ends. The function is bounded, say by \(M\), so its strict superlevel set is empty when \(s\geq M\). On every compact subinterval of \((0,M)\), its measure is bounded by the measure at the smallest threshold. Thus only small thresholds can cause the weak norm to diverge. Formula (T6) gives

\[
\begin{gathered}
s\,\mu_a(s)^{1/p}
\\ \sim(2A_a^{1/a})^{1/p}s^{1-1/(ap)},
\\ F_a\in L^{p,\infty}\quad\Longleftrightarrow\quad ap\geq1,
\\ 1\leq p<\infty.
\end{gathered}\tag{T7}
\]

Here the second line uses precisely the superlevel criterion in the question as the definition of \(L^{p,\infty}\). If \(ap<1\), the first line diverges as \(s\downarrow0\); if \(ap\geq1\), it stays bounded there and on the remaining thresholds. Theorem A gives strong \(L^p\) exactly for \(ap>1\), so equality is the weak endpoint and fails the strong criterion. The equality exponent \(p=1/a\) is in this question's range only if \(a\leq1\). For \(p=\infty\), ordinary boundedness already holds for every \(a>0\).

**Solution 10.** Write \(s=\operatorname{sgn}\lambda\). Choose the ray angles

\[
\begin{gathered}
\alpha_+=\frac{s\pi}{2m},
\\ \alpha_-=\begin{cases}
\pi+\alpha_+,&m\text{ even},\\
\pi-\alpha_+,&m\text{ odd}.
\end{cases}
\end{gathered}\tag{T8}
\]

Orient the negative ray from infinity to zero and the positive ray from zero to infinity. On either one, \(i\lambda z^m/m=-|\lambda|u^m/m\), where \(u\geq0\) is its real ray parameter. These contours therefore make every polynomial moment absolute, even when its corresponding undamped real integral fails to exist.

We justify their equality with the entire Fourier derivatives. First damp the input by \(e^{-\varepsilon x^2}\), with \(\varepsilon>0\). Rotate each real half-line to the indicated ray by the finite-contour interface, including the factor \((-iz)^k\). Throughout each rotation sector, \(\operatorname{Re}z^2\geq0\) and \(\operatorname{Im}(\lambda z^m)\geq0\). On the radius-\(R\) arcs, write \(\delta\in[0,\pi/(2m)]\) for the angular distance from the real half-line. For \(m\geq3\), its first half has \(\cos(2\delta)\geq\cos(\pi/(2m))>0\), so the damping bounds it by \(e^{-c\varepsilon R^2}\). The second half has \(\sin(m\delta)\geq1/\sqrt2\), so the phase bounds it by \(e^{-c_\lambda R^m}\). For \(m=2\), the sum of the two nonnegative exponents is
\(R^2[\varepsilon\cos(2\delta)+|\lambda|\sin(2\delta)/2]\), at least \(R^2\min(\varepsilon,|\lambda|/2)\), because the sine plus cosine is at least one on that interval. The complex-frequency factor on a compact set is at most \(e^{C R}\). The arc length and moment add only a factor \(C_kR^{k+1}\). Both end arcs thus vanish for each \(\varepsilon>0\), every \(k\), and every compact complex-frequency set.

On the rotated rays, \(|e^{-\varepsilon z^2}|\leq1\), and a common bound for the \(k\)-th derivative integrand is
\(u^k e^{-|\lambda|u^m/m+C u}\), integrable on \([0,\infty)\). Dominated convergence is uniform on each compact frequency set. The complete Gaussian-regularization proof in Solution 8 identifies its limit with \(F_{m,\lambda}^{(k)}\). Therefore the entire derivative is exactly the sum of these two oriented absolute ray integrals. This argument uses regularized contours to identify every moment; it does not assert convergence of an undamped real moment of high degree.

At the origin, substitute \(v=|\lambda|u^m/m\) into the positive integral. For every \(k\geq0\),

\[
\begin{gathered}
J_k=\int_0^\infty u^k e^{-|\lambda|u^m/m}du
\\ =\frac1m\left(\frac m{|\lambda|}\right)^{(k+1)/m}
\Gamma\!\left(\frac{k+1}{m}\right),
\\ F_{m,\lambda}^{(k)}(0)
\\ =(-i)^k\left[\begin{gathered}
e^{i(k+1)\alpha_+}
\\ {}-e^{i(k+1)\alpha_-}
\end{gathered}\right]J_k.
\end{gathered}\tag{T9}
\]

The subtraction comes from the negative ray's orientation; the Fourier derivative supplies \((-i)^k\). For even \(m\), the bracket equals
\([1-(-1)^{k+1}]e^{i(k+1)\alpha_+}\), so every odd derivative vanishes. For odd \(m\), it equals
\(e^{i(k+1)\alpha_+}-(-1)^{k+1}e^{-i(k+1)\alpha_+}\). This proves all values in T2 and both sign cases. Each gamma argument is positive, and only its convergent defining integral is used.

Theorem B's exact equation for this polynomial is
\(\lambda i^{m-1}F^{(m-1)}(\zeta)-\zeta F(\zeta)=0\).
If \(F(\zeta)=\sum_{j\geq0}c_j\zeta^j\), comparison of its entire Taylor coefficients gives

\[
\begin{gathered}
c_{m-1}=0,
\\ c_{j+m-1}
\\ =\frac{j!}{\lambda i^{m-1}(j+m-1)!}\,c_{j-1},
\\ j\geq1,
\\ c_0,\ldots,c_{m-2}
\\ \text{given by (T9),}
\\ \text{divided by their factorials.}
\end{gathered}\tag{T10}
\]

The equation and these initial data determine every coefficient. Scaling the real variable by \(|\lambda|^{-1/m}\) in the regularized integral gives (T2), with damping changed to \(\varepsilon|\lambda|^{-2/m}\). Solution 8 passes that identity to the entire limit on all compact complex-frequency sets. This proves the scaling without relying on improper integrals at complex frequencies.

Finally the ray representation yields an explicit global growth bound. Put \(q=m/(m-1)\), \(v=|\zeta|\), and \(c=|\lambda|/m\). Elementary maximization of \(vu-(c/2)u^m\) for \(u\geq0\) gives

\[
\begin{gathered}
vu-\frac c2u^m\leq B_{m,\lambda}v^q,
\\ B_{m,\lambda}=\frac{m-1}{m}
\\ {}\times\left(\frac2{|\lambda|}\right)^{1/(m-1)}.
\end{gathered}\tag{T11}
\]

Taking absolute values in both ray integrals and retaining the remaining \(e^{-cu^m/2}\) gives

\[
\begin{gathered}
|F_{m,\lambda}(\zeta)|
\\ \leq C_{m,\lambda}e^{B_{m,\lambda}|\zeta|^q},
\\ C_{m,\lambda}=\frac2m
\\ {}\times\left(\frac{2m}{|\lambda|}\right)^{1/m}
\Gamma(1/m).
\end{gathered}\tag{T12}
\]

This is an upper bound for entire growth with exact constants; it does not assert a sharp order or a directional asymptotic. It includes degree two, whose entire Gaussian growth has exponent two.

**Solution 11.** Set \(h=\varepsilon/\lambda\), which has the sign of \(\lambda\). We first justify using any horizontal contour of this sign for the undamped cubic. If \(z=x+ih\), then
\(\operatorname{Im}(\lambda z^3/3)=\lambda h x^2-\lambda h^3/3\), and \(\lambda h>0\). Thus the contour integral and all frequency derivatives are absolute, locally uniformly in complex frequency. To compare two fixed heights of this sign, connect their horizontal truncations with vertical ends. All intermediate heights stay separated from zero, so the cubic factor on each end is bounded by \(e^{-cR^2}\); complex frequencies add at most \(e^{C R}\), and derivatives add only \(R^k\). The ends vanish. The finite-contour interface therefore identifies this contour with Theorem B's fixed horizontal contour, for all complex frequencies and every derivative. This proves the undamped representation used here, including arbitrarily small positive \(\lambda h\).

Write \(z=x+ih\) in that representation of \(F_\lambda(w)\). Expanding the cubic and the linear factor gives

\[
\begin{gathered}
F_\lambda(w)=e^{\lambda h^3/3+hw}
\\ {}\times\int_{\mathbb R}\exp\!\left[\begin{gathered}
-\lambda h x^2
\\ {}+i\lambda x^3/3
\\ {}-iwx
\\ {}-i\lambda h^2x
\end{gathered}\right]dx.
\end{gathered}\tag{T13}
\]

Put \(w=\zeta-\varepsilon^2/\lambda\). Since \(\lambda h=\varepsilon\), this proves the exact entire identity

\[
\begin{gathered}
F_{\lambda,\varepsilon}(\zeta)
\\ =\exp\!\left(
-\frac{\varepsilon\zeta}{\lambda}
+\frac{2\varepsilon^3}{3\lambda^2}\right)
\\ {}\times F_\lambda\!\left(\zeta-\frac{\varepsilon^2}{\lambda}\right).
\end{gathered}\tag{T14}
\]

The shift and exponential are valid for either sign of \(\lambda\). Formula (T13) with \(\lambda=1\) proves (T3). Setting \(\lambda=1,\zeta=0\) in (T14) and using the entire Taylor expansion proves (T4), with an \(O(\varepsilon^3)\) error. No undamped complex-frequency integral over the real line has been assumed.

For the frequency equation, differentiate the damped input in the physical variable:
\(D_x f=(\lambda x^2+2i\varepsilon x)f\), where \(D_x=-i\partial_x\). Its polynomial multiples are tempered. Fourier derivative and multiplication rules then give, and absolute Gaussian integration extends directly to complex frequency,

\[
\lambda F_{\lambda,\varepsilon}''
+2\varepsilon F_{\lambda,\varepsilon}'
+\zeta F_{\lambda,\varepsilon}=0.
\tag{T15}
\]

For this direct complex verification, integrate the derivative of
\(e^{-\varepsilon x^2+i\lambda x^3/3-i\zeta x}\) on the real line; its endpoints vanish by the Gaussian. Differentiating in \(\varepsilon>0\) under the same absolute integral yields

\[
\partial_\varepsilon F_{\lambda,\varepsilon}
=\partial_\zeta^2F_{\lambda,\varepsilon}.
\tag{T16}
\]

Both sides equal \(-\int x^2e^{-\varepsilon x^2+i\lambda x^3/3-i\zeta x}dx\). These computations fix both the heat sign and the first-derivative coefficient in (T15).

The entire shift formula proves locally uniform convergence with every frequency derivative: the shifted compact sets remain in one compact neighborhood, the shift tends uniformly to zero, and the exponential and all its derivatives tend uniformly to one and their respective zero derivatives. It also gives a quantitative first correction. For a compact set \(K\), put \(Z=\sup_{\zeta\in K}|\zeta|\), choose \(0<\varepsilon\leq\min(1,\sqrt{|\lambda|})\), and let
\(K_1=\{w:\operatorname{dist}(w,K)\leq1\}\),
\(M_j=\sup_{K_1}|F_\lambda^{(j)}|\) for \(j=0,1\). These finite numbers are bounded by the absolute ray formula in Solution 10 and its derivative version. Set
\(B=Z/|\lambda|+2/(3\lambda^2)\). Then

\[
\begin{gathered}
\left|\begin{gathered}
F_{\lambda,\varepsilon}(\zeta)
\\ {}-F_\lambda(\zeta)
\\ {}+\frac{\varepsilon\zeta}{\lambda}F_\lambda(\zeta)
\end{gathered}\right|
\\ \leq\varepsilon^2\left[\begin{gathered}
\frac{e^BM_1}{|\lambda|}
\\ {}+M_0\left(\begin{gathered}
\frac{e^BB^2}{2}
\\ {}+\frac2{3\lambda^2}
\end{gathered}\right)
\end{gathered}\right],
\\ \zeta\in K.
\end{gathered}\tag{T17}
\]

To verify the bound, denote the exponent in (T14) by \(A\) and its shift by \(d=\varepsilon^2/\lambda\). We have \(|A|\leq B\varepsilon\) and
\(|A+\varepsilon\zeta/\lambda|\leq2\varepsilon^3/(3\lambda^2)\). The straight segment from \(\zeta\) to \(\zeta-d\) is in \(K_1\), so the fundamental theorem of calculus bounds
\(|F_\lambda(\zeta-d)-F_\lambda(\zeta)|\leq|d|M_1\).
Finally \(|e^A-1-A|\leq e^{|A|}|A|^2/2\), proved by the absolute exponential series or its integral remainder. Applying these three bounds to (T14) gives exactly (T17). Thus the first correction is
\(-\varepsilon\zeta F_\lambda(\zeta)/\lambda=\varepsilon F_\lambda''(\zeta)\), by the undamped cubic equation.

For the strong tempered limit of the inputs, every bounded Schwartz family \(\mathcal B\) satisfies

\[
\begin{gathered}
\sup_{\phi\in\mathcal B}
\left|\int\left[\begin{gathered}
(e^{-\varepsilon x^2}-1)
\\ {}\cdot e^{i\lambda x^3/3}\phi(x)
\end{gathered}\right]dx\right|
\\ \leq\varepsilon\sup_{\phi\in\mathcal B}
\int x^2|\phi(x)|dx
\\ \leq C_{\mathcal B}\varepsilon.
\end{gathered}\tag{T18}
\]

The last bound follows from a common fourth-order Schwartz weight, and \(|1-e^{-v}|\leq v\) for \(v\geq0\). Strong Fourier continuity gives strong convergence of the real-frequency transforms, and bounded compact-test families yield the strong \(\mathcal D'\) conclusion too. This estimate applies to every bounded test family, while (T17) separately controls entire values on each compact complex-frequency set.

## References

- The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16: exact Schwartz operations, compact-test density, inversion, absolute integration and real Jacobians.
- [Boundary flux and weak identities](boundary-flux-and-weak-identities.md), Corollaries 2.3–2.4: finite contours with corners. [Order, positivity and distributional limits](order-positivity-and-limits.md), (T1)–(T2): bounded compact-test families. [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and Theorem 3.1: the determinant branch and Gaussian transform. [Quadratic transforms and tempered images](quadratic-transforms-and-tempered-images.md), Lemma 0.1: all complex frequencies. [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1 and calculation G: strong transposes and signed Fresnel identities.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises 7.6.7–7.6.8, p. 393, and answers, pp. 416–417. This lesson supplies independent complete contour and differential-equation proofs, original measurements, and eleven graded problems with full solutions.
- F. W. J. Olver, [NIST Digital Library of Mathematical Functions, Chapter 9](https://dlmf.nist.gov/9), version 1.2.8, September 15, 2026: [9.5.1](https://dlmf.nist.gov/9.5.E1) identifies the Airy cosine-integral normalization; [9.2.1](https://dlmf.nist.gov/9.2.E1), [9.2.3](https://dlmf.nist.gov/9.2.E3) and [9.2.4](https://dlmf.nist.gov/9.2.E4) give its named equation and initial values. These are normalization comparisons. The complete contour, positive gamma-integral and distributional proofs used in this lesson are supplied here and in the exact earlier lessons.
