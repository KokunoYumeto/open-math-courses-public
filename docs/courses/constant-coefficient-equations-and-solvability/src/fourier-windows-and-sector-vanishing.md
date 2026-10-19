# Fourier windows, sector growth and branched vanishing

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Exponential smallness on one ray does not control an entire algebraic covering. Compact Fourier windows and sector estimates supply enough rays on every sheet to force vanishing.

Read [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz inversion; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the integration estimates. [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Cauchy kernels and distributional boundary limits](../prerequisites/cauchy-kernels-and-boundary-limits.html) proves the Cauchy–Pompeiu formula; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) proves scalar factorization and the exponential series.

For Fourier background, Grubb's author-hosted Chapter 5, *Fourier transformation of distributions*, gives differentiation and Schwartz inversion in Theorem 5.4(2–3), equations (5.9)–(5.10), printed pp. 5.3–5.6, and compact-support holomorphy in Remark 5.18, printed pp. 5.14–5.15. The uniform window estimates, sector arguments and branched-curve vanishing are proved below. Other general background references are Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## The full spatial Fourier bound and its differential equation

**Lemma A.** Let \(u\in C^\infty(\mathbb R^d\times(-2,2))\) have spatial support in \(\{|y|\le M\}\), \(M\ge0\), at every time. Use \(D=-i\partial\). Its partial transform
\[
 U(\zeta,t)=\int_{\mathbb R^d}u(y,t)e^{-iy\cdot\zeta}\,dy
 \tag{1}
\]
is entire in \(\zeta\in\mathbb C^d\), smooth in \(t\), and satisfies, for every compact time interval \(I\subset(-2,2)\) and integers \(b,N\ge0\),
\[
\begin{gathered}
|D_t^bU(\zeta,t)|\\
\le C_{I,b,N}(1+|\zeta|)^{-N}
                           e^{M|\operatorname{Im}\zeta|},
 \\
\qquad t\in I.
\end{gathered}
\tag{2}
\]

**Proof.** All time and spatial derivatives of \(u\) vanish outside the same spatial support: there the original function vanishes on a spatial open neighborhood at every time, so its derivatives are zero. These derivatives are bounded on the compact product of \(I\) and a fixed closed spatial ball. For each compact set of complex \(\zeta\), the exponential and all its \(\zeta\)-derivatives are uniformly bounded on that product. Differentiation under the finite-support integral therefore proves the asserted holomorphy and time smoothness, including their commutation.

For \(|\zeta|\ge1\), select a coordinate with \(|\zeta_j|\ge|\zeta|/\sqrt d\). Repeated integration by parts gives
\(\zeta_j^N D_t^bU=\int D_{y_j}^N D_t^bu(y,t)e^{-iy\cdot\zeta}\,dy\).
No conjugation is involved. On the support, the exponential has modulus at most \(e^{M|\operatorname{Im}\zeta|}\). Its integral is therefore bounded by the ball's volume times the appropriate derivative supremum; division by \(|\zeta_j|^N\) gives the required decay, uniformly over the finitely many possible selected coordinates. For \(|\zeta|\le1\), use the undifferentiated integral and enlarge the constant by \(2^N\). This gives (2) for the original complex norm \(|\zeta|\), not only its real part.

If \(d\ge1\) and \(M=0\), a continuous function supported at the spatial point zero is zero, so the conclusion is immediate. In dimension zero define the integral over the one-point space to be its value, put \(|\zeta|=0\), and use the time derivative bound. There is no coordinate-selection step in that case. \(\square\)

**Lemma B.** Let \(P(\zeta,\lambda)\) be a polynomial of total degree \(m\ge1\), and suppose \(P(\zeta,D_t)U=0\). Define its polynomial difference quotient and the corresponding time function by
\[
\begin{gathered}
Q(\zeta,s,\lambda)=
 \sum_{j\ge1}a_j(\zeta)\sum_{h=0}^{j-1}s^{j-1-h}\lambda^h,
 \\
\qquad
 W(\zeta,s,t)=Q(\zeta,s,D_t)U(\zeta,t),
\end{gathered}
\tag{3}
\]
where \(P(\zeta,\lambda)=\sum_j a_j(\zeta)\lambda^j\). If \(P(\zeta,s)=0\), then
\[
\begin{gathered}
(D_t-s)W=0,\\
\qquad W(\zeta,s,t)=e^{ist}W(\zeta,s,0),
 \\
\quad
 |W(\zeta,s,0)|\\
\le C(1+|s|)^{m-1}
                     e^{M|\operatorname{Im}\zeta|-|\operatorname{Im}s|}.
\end{gathered}
\tag{4}
\]

**Proof.** The finite geometric-sum identity gives
\((s-\lambda)Q=P(\zeta,s)-P(\zeta,\lambda)\).
Consequently \((D_t-s)W=[P(\zeta,D_t)-P(\zeta,s)]U\), which is zero at a root. Since \(D_t=-i\partial_t\), differentiating \(e^{-ist}W(t)\) gives zero, proving the displayed time identity with its exact phase.

Every monomial \(\zeta^\alpha s^q\lambda^h\) in \(Q\) has \(|\alpha|+q+h\le m-1\). At \(t=1\) and \(t=-1\), apply Lemma A with \(N=m-1\) to its corresponding derivative \(D_t^hU\). Multiplication by \(|\zeta^\alpha|\) consumes at most that decay order; multiplication by \(|s|^q\) is at most \((1+|s|)^{m-1}\). Summing the finitely many terms gives one constant \(C\) valid at both times. Now \(W(0)=e^{-ist}W(t)\) has modulus \(e^{t\operatorname{Im}s}|W(t)|\). Choose \(t=-1\) when \(\operatorname{Im}s\ge0\), and \(t=1\) otherwise. The exponent becomes \(-|\operatorname{Im}s|\), proving (4) with the original support radius \(M\). \(\square\)

**Lemma C.** At a fixed \(\zeta\), suppose \(P(\zeta,\lambda)\) has degree \(\mu\ge1\) and distinct roots \(s_1,\ldots,s_\mu\). If \(W(\zeta,s_j,0)=0\) for every root, then \(U(\zeta,t)=0\) for all times in the slab.

**Proof.** Lemma B makes each \(Q(\zeta,s_j,D_t)U\) zero at all those times. The polynomial \(Q(\zeta,s_j,\lambda)=P(\zeta,\lambda)/(\lambda-s_j)\) has value zero at \(s_\ell\) for \(\ell\ne j\), and value \(\partial_\lambda P(\zeta,s_j)\ne0\) at \(s_j\). Therefore
\[
 1=\sum_{j=1}^{\mu}
     \frac{Q(\zeta,s_j,\lambda)}{\partial_\lambda P(\zeta,s_j)}.
 \tag{5}
\]
Indeed, the difference of the two sides is a polynomial of degree at most \(\mu-1\) vanishing at all \(\mu\) distinct roots; repeated scalar division shows it is zero. Apply this polynomial identity with \(\lambda=D_t\). It gives \(U=0\) with the full original leading coefficient retained in \(\partial_\lambda P\). When \(\mu=0\) and \(P(\zeta,\lambda)\) is a nonzero constant, the original equation itself gives \(U=0\). No conclusion is asserted at a parameter where that polynomial is identically zero without a separate parameter-continuation argument. \(\square\)

## Growth below the sector threshold

**Lemma 1.** Let \(p\ge1\) be an integer and let a sector have central argument \(\theta_c\), opening \(0<\omega<\pi/p\), and inner radius \(R_0>0\). Suppose \(f\) is holomorphic in a neighborhood of its closed part \(|z|\ge R_0\), and
\[
 |f(z)|\le A e^{B|z|^p},\qquad A>0,\quad B\ge0.
 \tag{6}
\]
Suppose \(|f|\le M\) on its two bounding rays. If \(C_0\) is the maximum of \(M\) and the supremum of \(|f|\) on its inner circular arc, then \(|f|\le C_0\) throughout the sector.

**Proof.** Choose a real number \(\rho\) such that
\[
 p<\rho<\frac{\pi}{\omega},\qquad
 c_\rho=\cos(\rho\omega/2)>0.
 \tag{7}
\]
The strict opening hypothesis makes this choice possible. The branch of \(\log(e^{-i\theta_c}z)\) whose imaginary part lies between \(-\omega/2\) and \(\omega/2\) defines its \(\rho\)-th power. It is holomorphic on a slightly larger sector if that enlargement is sufficiently small. Throughout the original sector,
\[
\begin{gathered}
\operatorname{Re}(e^{-i\theta_c}z)^\rho
   \\
=|z|^\rho\cos\bigl(\rho(\arg z-\theta_c)\bigr)
   \\
\ge c_\rho |z|^\rho.
\end{gathered}
\tag{8}
\]

For \(\varepsilon>0\), apply maximum modulus to
\[
 g_\varepsilon(z)=
 f(z)\exp\bigl(-\varepsilon(e^{-i\theta_c}z)^\rho\bigr)
 \tag{9}
\]
on a sector truncated at radius \(R>R_0\). On both radial sides its modulus is at most \(M\), and on the inner arc it is at most \(C_0\), because the damping factor has modulus at most one. On the outer arc (6)–(8) give \(A\exp(BR^p-\varepsilon c_\rho R^\rho)\). Since \(\rho>p\), this tends to zero. If \(C_0>0\), choose \(R\) arbitrarily large with this last bound at most \(C_0\). The bounded truncated sector is connected; a maximum in its interior forces a constant by the local maximum-modulus theorem. Thus its maximum is bounded by its boundary maximum, also in the constant case. We obtain \(|g_\varepsilon(z)|\le C_0\) at every fixed point after taking \(R\) large enough to include it.

If \(C_0=0\), the function already vanishes on its inner arc, which lies in its holomorphic neighborhood and has limit points there. The identity principle proves it is zero on the sector. In the other case, let \(\varepsilon\downarrow0\) in the bound just obtained. The damping factor at the fixed point tends to one, and its removal yields the exact bound \(C_0\). The inner-arc constant is independent of \(\varepsilon\). \(\square\)

The strict inequality in the opening is essential. The example \(f(z)=e^{z^p}\) in the sector \(|\arg z|<\pi/(2p)\) has modulus one on both rays and unbounded modulus on the positive axis.

## Covering all arguments and removing infinity

**Lemma 2.** Suppose \(f\) is holomorphic for \(|z|>R\) and satisfies (6) there. Suppose a finite cyclic list of ray arguments has every successive angular gap strictly less than \(\pi/p\), and \(f\) is bounded on each of those rays outside a sufficiently large radius. Then \(f\) is bounded on a smaller exterior domain. If, on at least one ray, it additionally satisfies
\[
\begin{gathered}
|f(re^{i\theta_0})|\le C r^L e^{-c r^p},
 \\
\qquad c>0,\quad L\ge0,
\end{gathered}
\tag{10}
\]
then \(f\) is identically zero on \(|z|>R\).

**Proof.** Choose one radius \(R_1>R\) beyond all the finitely many ray thresholds. The closed circle at that radius is a compact subset of the holomorphic domain, so \(|f|\) has a finite maximum there. Take the maximum of that value and the finitely many ray bounds. Lemma 1 applies to each sector between consecutive rays with this same constant. The sectors cover the exterior of the circle, so \(f\) is bounded there.

Set \(h(v)=f(1/v)\). It is holomorphic and bounded in a punctured disk. We spell out the removable-point step. For \(0<|v|<r_0<1/R_1\), the annular Cauchy formula gives, when \(0<\delta<|v|\),
\[
\begin{gathered}
h(v)=\frac1{2\pi i}\int_{|u|=r_0}\frac{h(u)}{u-v}\,du
      \\
-\frac1{2\pi i}\int_{|u|=\delta}\frac{h(u)}{u-v}\,du.
\end{gathered}
\tag{11}
\]
Both circles in this formula have counterclockwise orientation; the minus sign is the inner boundary orientation. The second integral is bounded in modulus by \(\|h\|_\infty\delta/(|v|-\delta)\) and tends to zero. The first defines a holomorphic function also at \(v=0\): its kernel has the uniformly convergent geometric series for \(|v|<r_0\), and termwise integration gives its convergent Taylor series. Thus \(h\) extends holomorphically across zero, and
\[
\begin{gathered}
f(z)=\sum_{j=0}^{\infty}a_jz^{-j}
 \\
\quad\hbox{for all sufficiently large }|z|.
\end{gathered}
\tag{12}
\]

If this series is not zero, let \(j_0\) be its first nonzero index. On the ray in (10), convergence of the Taylor series at zero gives, for all sufficiently large \(r\),
\[
 |f(re^{i\theta_0})|\ge
       \frac{|a_{j_0}|}{2}r^{-j_0}.
 \tag{13}
\]
This contradicts (10). Indeed, choose an integer \(q\) with \(pq>L+j_0\); the positive exponential series gives \(e^{c r^p}\ge(c r^p)^q/q!\), so \(r^{L+j_0}e^{-c r^p}\to0\). Therefore every \(a_j\) is zero, and \(f\) vanishes on an exterior open subset. The holomorphic identity principle extends the zero to the connected domain \(|z|>R\). \(\square\)

## A nonreal slope supplies the necessary rays on every sheet

**Proposition 3.** Let \(p\ge1\), \(e\in\mathbb R^d\), \(\eta\in\mathbb C^d\), and \(M\ge0\). Suppose \(t\) is holomorphic on \(|w|>R\) and
\[
 t(w)=c_0w^p+O(|w|^{p-1})
 \tag{14}
\]
uniformly in argument, where either \(c_0=0\) or \(\operatorname{Im}c_0\ne0\). Suppose \(f\) is holomorphic on the same exterior domain and, for fixed \(C>0\) and \(a\ge0\),
\[
\begin{gathered}
|f(w)|\\
\le C(1+|w|^p)^a
       \\
\exp\bigl(M|\operatorname{Im}(t(w)e+\eta)|
                        -|\operatorname{Im}(w^p)|\bigr).
\end{gathered}
\tag{15}
\]
Then \(f\) is identically zero there. The norm in (15) is the original Euclidean norm of the \(d\)-vector; \(e\), \(M\), \(\eta\), \(p\) and \(c_0\) are not changed.

**Proof.** The uniform remainder in (14) gives \(|t(w)|\le C_1|w|^p\) for all sufficiently large \(|w|\). Since \(e\) is real,
\[
\begin{gathered}
|\operatorname{Im}(t(w)e+\eta)|\\
\le |e|\,|t(w)|+|\operatorname{Im}\eta|
\end{gathered}
\].
Dropping the negative last term of (15) therefore gives (6) for suitable \(A,B\) and the same \(p\). Its polynomial prefactor can be absorbed into that bound because \(1+s\le e^s\) for \(s\ge0\).

If \(c_0\ne0\), take \(\theta=-\arg c_0\). Then \(\operatorname{Im}(c_0e^{i\theta})=0\) and \(\sin\theta\ne0\), because \(c_0\) is not real. If \(c_0=0\), take \(\theta=\pi/2\). By continuity, choose \(0<\delta<\pi/2\) and \(s_0>0\) so that, on both closed intervals centered at \(\theta\) and \(\theta+\pi\) with half-width \(\delta\),
\[
\begin{gathered}
|\sin\beta|\ge s_0,\\
\qquad
 M|e|\,|\operatorname{Im}(c_0e^{i\beta})|
                       \le \tfrac14|\sin\beta|.
\end{gathered}
\tag{16}
\]
These two intervals have the same inequalities because adding \(\pi\) reverses the signs before absolute values.

For \(w=re^{i\varphi}\) whose \(p\varphi\) lies in either interval modulo \(2\pi\), use the real-vector inequality
\(|\operatorname{Im}(t(w)e+\eta)|\le |e|\,|\operatorname{Im}t(w)|+|\operatorname{Im}\eta|\).
The uniform remainder in (14) and (16) show that the exponent in (15) is at most
\[
\begin{gathered}
-\tfrac34r^p|\sin(p\varphi)|+
        \\
O(r^{p-1})+M|\operatorname{Im}\eta|
 \\
\le-\tfrac12s_0r^p
\end{gathered}
\tag{17}
\]
for all sufficiently large \(r\), uniformly on these finitely many lifted closed intervals. Absorb the prefactor into half of this negative exponential. One way to verify that absorption without a logarithmic estimate is to choose an integer \(q>a\), expand \(e^{s_0r^p/4}\), and compare its \(q\)-th positive term with \(r^{pa}\). We obtain \(|f(w)|\le C_2e^{-s_0r^p/4}\) on the lifted rays.

The centers of the lifted intervals are \((\theta+j\pi)/p\), \(j=0,\ldots,2p-1\). In each interval choose two rays with arguments center minus and plus \(\delta/(2p)\). There are \(4p\) cyclic rays. Their successive gaps are \(\delta/p\) and \((\pi-\delta)/p\), both strictly smaller than \(\pi/p\). The global growth bound and the ray bounds therefore satisfy Lemma 2. Any one of these rays also satisfies its exponential-decay hypothesis. It follows that \(f=0\). This counts every sheet of the finite cover \(w\mapsto w^p\); no application of a single-sheet sector argument is hidden. \(\square\)

## Exercises with complete solutions

**Exercise 1 (basic: the critical opening).** For \(p=2\), exhibit a holomorphic function bounded on the rays of the sector \(-\pi/4\le\arg z\le\pi/4\) but unbounded inside it. Give the damping-power interval for a smaller sector of opening \(\pi/3\).

**Solution.** The function \(e^{z^2}\) has modulus one on the two rays, since \(z^2\) is purely imaginary there, and has modulus \(e^{r^2}\) on the positive axis. The critical opening is \(\pi/2\), so Lemma 1 does not apply. At opening \(\pi/3\), choose \(2<\rho<3\); for example \(\rho=5/2\). Then \(\cos(\rho\omega/2)=\cos(5\pi/12)>0\), providing the strictly positive damping factor needed on the whole sector.

**Exercise 2 (intermediate: a complex slope and a three-sheet cover).** In Proposition 3 let \(p=3\), \(c_0=i\), \(M=2\), \(|e|=1\) and \(\eta=0\). Find a central angle \(\theta\) with zero leading imaginary spatial displacement, and specify a sufficiently small interval of ray angles satisfying (16). How many lifted ray intervals and sector cuts are used?

**Solution.** Take \(\theta=-\pi/2\), so \(ie^{i\theta}=1\) and \(|\sin\theta|=1\). If \(\beta=\theta+h\), then \(|\operatorname{Im}(ie^{i\beta})|=|\sin h|\) and \(|\sin\beta|=|\cos h|\). It suffices that \(2|\tan h|\le1/4\), for example \(|h|\le\arctan(1/16)\); this gives a strict margin because \(2/16<1/4\). The interval centered at \(\theta+\pi\) obeys the same bound. On the \(w\)-plane there are \(2p=6\) intervals, with centers \((\theta+j\pi)/3\). Taking two interior rays from each gives \(4p=12\) sector cuts. The gap estimate in the proof covers the full argument circle.

**Exercise 3 (advanced: a complete two-variable uniqueness case).** Let \(u\in C^\infty(\mathbb R\times(-2,2))\) have spatial support in \([-M,M]\) and solve \((D_t^2+D_y^2)u=0\). Prove \(u=0\), using this lesson without assuming the full general bounded-support uniqueness theorem.

**Solution.** Here \(P(\zeta,\lambda)=\lambda^2+\zeta^2\), \(Q(\zeta,s,\lambda)=s+\lambda\), and \(W=(s+D_t)U\). For each sign set \(f_\pm(w)=W(\pm iw,w,0)\). These functions are entire because \(U\) and its time derivatives are entire in their spatial argument. Their parameters satisfy \(P(\pm iw,w)=0\). Lemma B gives exactly (15) with \(p=1\), \(a=1\), \(e=1\), \(\eta=0\), and \(t(w)=\pm iw\). Both slopes are nonreal, so Proposition 3 makes \(f_\pm=0\) outside a disk; the entire identity principle makes them zero everywhere. If \(\zeta\ne0\), the two roots of \(P(\zeta,\lambda)\) are distinct, and these two parameterizations give \(W=0\) at both roots. Lemma C yields \(U(\zeta,t)=0\). Continuity gives the same at \(\zeta=0\). At each fixed real time, \(u\) is a smooth compactly supported function; its real Fourier transform is zero, so the exact Schwartz inversion theorem gives \(u=0\). This proves the claimed case in the whole open slab. It does not replace the required general irreducible-root argument.

## References

- Gerd Grubb, *Fourier transformation of distributions*, author-hosted Chapter 5 of *Distributions and Operators*. Theorem 5.4(2–3), equations (5.9)–(5.10), printed pp. 5.3–5.6; Remark 5.18, printed pp. 5.14–5.15. These passages supply the differentiation, Schwartz inversion and compact-support holomorphy background for Lemma A and Exercise 3. The uniform window, sector and branched-vanishing proofs are given in this lesson. [Exact freely readable chapter](https://www.math.ku.dk/~grubb/dist5.pdf).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in *Classics in Mathematics*, Springer, 2003, e-ISBN 978-3-642-61497-2. Definition 7.1.1, Lemma 7.1.3 and Theorem 7.1.5, printed pp. 160–161; Theorem 7.3.1, printed pp. 181–182. These give ordinary Fourier and compact-support background for Lemma A and Exercise 3. The uniform window, sector and branched-vanishing proofs are given in this lesson.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
