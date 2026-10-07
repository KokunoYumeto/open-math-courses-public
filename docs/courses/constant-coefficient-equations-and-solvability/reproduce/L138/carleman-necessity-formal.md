# Compact support and the Carleman condition

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Original exposition, examples, solutions and diagrams: CC0 1.0.

A compactly supported smooth function cannot have arbitrarily inexpensive derivatives. Integration by parts converts derivative bounds into an envelope for its Fourier transform. The logarithm of that envelope records one nonnegative contribution from every derivative threshold. A half-plane boundary theorem limits the total logarithmic loss, and an exact integral turns that loss into the reciprocal series.

The only global analytic input used below is the weighted signed boundary measure and weak trace in [Boundary measures and Green potentials in a half-space, GR1 and GR10](../../AN02-L135.html#GR1). The logarithmic kernel used to verify subharmonicity is proved in [Local Newtonian potentials, NP4 and NP6](../../AN02-L131.html#NP4). Entire extension, Fourier injectivity, isolated zeros, logarithmic boundary convergence and the optimization of the derivative bounds are proved here. Ordinary Lebesgue integration, Tonelli, dominated convergence and elementary real and complex calculus are used with the displayed bounds.

<a id="CN1"></a>

## CN1. The exact compact-support statement

Let \(u\in C_c^\infty(\mathbb R)\) be nonzero. Let \(M_1,M_2,\ldots\) be positive numbers with \(M_{j+1}\ge M_j\), and suppose

\[
 |u^{(k)}(x)|\le A_k,\qquad
 A_k=\prod_{j=1}^k M_j,\qquad
 x\in\mathbb R,\quad k=1,2,\ldots.                         \tag{CN1.1}
\]

**Theorem CN.** These hypotheses imply

\[
 \sum_{j=1}^{\infty}\frac1{M_j}<\infty.                    \tag{CN1.2}
\]

Here \(C_c^\infty\) means smooth with compact support. A bound for the zeroth derivative is not an extra hypothesis. We use \(A_0=1\) only to organize a Fourier estimate with its own constant. The proof allows complex-valued \(u\); the real-valued case is included. Nondecreasing thresholds may repeat.

The conclusion is a necessity statement. We will construct one compatible compact bump in CN9, without inferring a general existence theorem from convergence of the series.

<a id="CN2"></a>

## CN2. The entire Fourier transform and its nontriviality

Choose \(R\ge1\) such that \(\operatorname{supp}u\subset[-R,R]\), and set

\[
 F(z)=\int_{\mathbb R}u(t)e^{-izt}\,dt,\qquad z\in\mathbb C,
 \qquad a=\|u\|_{L^1}>0.                                  \tag{CN2.1}
\]

For any center \(z_0\), expand the exponential in \(z-z_0\). On every bounded set of that difference, the series is absolutely dominated by
\(|u(t)|e^{R|\operatorname{Im}z_0|}e^{R|z-z_0|}\).
Termwise integration gives a power series of infinite radius and

\[
 F^{(m)}(z)=\int(-it)^m u(t)e^{-izt}\,dt,\qquad
 |F(\xi+iy)|\le a e^{Ry}\quad(y\ge0).                      \tag{CN2.2}
\]

Thus \(F\) is entire. We now prove that it is not identically zero, rather than assuming an inversion theorem.

For \(\tau>0\), direct Gaussian integration gives

\[
 \frac1{2\pi}\int_{\mathbb R}e^{-\tau\xi^2}e^{iq\xi}\,d\xi
 =K_\tau(q),\qquad
 K_\tau(q)=\frac{e^{-q^2/(4\tau)}}{\sqrt{4\pi\tau}}.        \tag{CN2.3}
\]

Here is a derivation. The integral \(J(q)=\int e^{-\tau\xi^2}e^{iq\xi}d\xi\) is differentiable under its absolutely integrable Gaussian majorant. Integration by parts in \(\xi\), with vanishing endpoint terms, gives \(J'(q)=-qJ(q)/(2\tau)\). Also \(J(0)=\sqrt{\pi/\tau}\): square the positive Gaussian integral and use polar coordinates in the plane. Solving the scalar differential equation gives (CN2.3).

If \(F(\xi)=0\) on the whole real line, absolute Fubini gives

\[
 0=\frac1{2\pi}\int e^{-\tau\xi^2}F(\xi)e^{i\xi x}\,d\xi
   =\int u(t)K_\tau(x-t)\,dt.                             \tag{CN2.4}
\]

The absolute double integral is at most \(a\int e^{-\tau\xi^2}d\xi/(2\pi)\). The kernel \(K_\tau\) is nonnegative and has integral one. Since \(u\) is bounded and uniformly continuous, its convolution with \(K_\tau\) tends uniformly to \(u\): inside distance \(\delta\) use the modulus of continuity, and outside it use \(2\|u\|_\infty\) times the Gaussian tail, which tends to zero after scaling \(q=\sqrt\tau\,s\). Equation (CN2.4) would therefore force \(u=0\). This proves Fourier injectivity in the exact class needed here and proves that \(F\) is nontrivial.

<a id="CN3"></a>

## CN3. Finite zeros and the subharmonic logarithm

At a zero \(b\) of a nontrivial entire function, its first nonzero Taylor coefficient gives

\[
 F(z)=(z-b)^m G(z),\qquad m\ge1,\qquad G(b)\ne0,            \tag{CN3.1}
\]

on a small disc. There must be a first nonzero coefficient. If all coefficients vanished at some point, the function would vanish on a neighborhood. The set of points where it vanishes on a neighborhood is open; it is also closed when nonempty, since at a limit point all derivatives vanish by continuity and the Taylor series again vanishes. Connectedness of the plane would then make the function identically zero. This is the identity principle needed here.

The factorization (CN3.1) makes each zero isolated. Consequently there are only finitely many zeros in any compact subset of the plane: otherwise a sequence of distinct zeros has a convergent subsequence in that compact set, and its limit contradicts isolation or the identity principle. In particular the real zeros are locally finite and have Lebesgue measure zero.

Define \(v(z)=\log|F(z)|\), with value \(-\infty\) at a zero. It is upper semicontinuous. On a zero-free disc, \(\log|G|\) is harmonic. For completeness, if \(G=a+ib\), the Cauchy–Riemann equations give \(\Delta a=\Delta b=0\), equal orthogonal gradients, and

\[
 \Delta\log|G|
 =\frac{|\nabla a|^2+|\nabla b|^2}{a^2+b^2}
  -\frac{2|a\nabla a+b\nabla b|^2}{(a^2+b^2)^2}=0.         \tag{CN3.2}
\]

Near a zero, (CN3.1) gives
\(v=m\log|z-b|+\log|G(z)|\).
The planar logarithmic kernel is subharmonic with
\(\Delta\log|z-b|=2\pi\delta_b\), by L131 NP4–NP6. Adding the harmonic term proves local subharmonicity also at the zero. These neighborhoods prove that \(v\) is subharmonic on the plane, and hence on the upper half-plane. Its local Laplacian is the positive measure \(2\pi\sum m_b\delta_b\). Nontriviality of \(F\) excludes the identically minus-infinite function.

The upper bound in (CN2.2) now gives the exact half-plane hypothesis:

\[
 v(\xi+iy)\le\log a+Ry,\qquad y>0.                         \tag{CN3.3}
\]

<a id="CN4"></a>

## CN4. The logarithmic trace at real zeros

Write \(g(x)=\log|F(x)|\) on the real line, with the same extended values at its locally finite zeros. We prove, on every compact interval \(I\),

\[
 \log|F(x+iy)|\longrightarrow g(x)
 \quad\text{in }L^1(I)\quad(y\downarrow0).                 \tag{CN4.1}
\]

The elementary singularity estimate is

\[
 \int_{\mathbb R}
 \left(\log|x+iy|-\log|x|\right)\,dx=\pi y,\qquad y>0.      \tag{CN4.2}
\]

The integrand is nonnegative. Substitute \(x=yt\). On the positive half-line its integral becomes
\(\frac y2\int_0^\infty\log(1+t^{-2})dt\).
Integration by parts gives
\(\int_0^\infty\log(1+t^{-2})dt=2\int_0^\infty(1+t^2)^{-1}dt=\pi\).
The endpoint terms \(t\log(1+t^{-2})\) vanish at zero and infinity. Doubling the half-line integral proves (CN4.2).

For a real zero \(b\) of multiplicity \(m\), choose a disc in (CN3.1) on which \(G\) is nonzero. On a smaller closed rectangle above a real interval in that disc,
\(\log|G(x+iy)|\to\log|G(x)|\) uniformly. The singular part's \(L^1\) difference on that interval is at most \(m\pi y\), by translating and restricting (CN4.2). Also \(\log|x-b|\) is locally integrable.

Enlarge \(I\) slightly and choose disjoint small intervals around its finitely many real zeros. Their factors give the preceding estimates. On the remaining compact real set, \(F\) is bounded away from zero; continuity preserves a positive lower bound in a sufficiently shallow strip, giving uniform logarithmic convergence there. Combining the finitely many regions proves both local integrability of \(g\) and (CN4.1). No pointwise dominated bound through a zero was assumed.

The exact error on a centered interval is useful for the diagram and an exercise:

\[
 \int_{-d}^{d}
 \left(m\log|x+iy|-m\log|x|\right)dx
 =m d\log(1+y^2/d^2)+2my\arctan(d/y)
 \le m\pi y.                                             \tag{CN4.3}
\]

The identity follows by integrating \(\log(1+y^2/x^2)\) by parts; the inequality follows by restricting (CN4.2). This is a local model of a zero, not an entire function satisfying a uniform horizontal upper bound.

<a id="CN5"></a>

## CN5. Identify the actual boundary measure

Apply the exact L135 theorem to \(v=\log|F|\) on the upper half-plane, using (CN3.3). Its dimension-two boundary conclusion supplies a real signed Radon measure \(\sigma\) such that

\[
 \int_{\mathbb R}(1+|x|)^{-2}\,d|\sigma|(x)<\infty,\qquad
 \int v(x+iy)\phi(x)dx\longrightarrow\int\phi\,d\sigma
 \quad(\phi\in C_c(\mathbb R)).                           \tag{CN5.1}
\]

For each such test, (CN4.1) also makes the limit equal to \(\int g\phi\,dx\). Equality of all continuous compact pairings determines a Radon measure, so

\[
 d\sigma(x)=g(x)\,dx,\qquad
 d|\sigma|(x)=|g(x)|\,dx.                                \tag{CN5.2}
\]

The variation assertion follows directly from the positive and negative parts of the real density; the sets where \(g\ge0\) and \(g<0\) realize its variation. The extended values at a locally finite zero set do not alter this measure.

Since
\(1+x^2\le(1+|x|)^2\le2(1+x^2)\),
the weighted variation in (CN5.1) gives

\[
 \int_{\mathbb R}\frac{|\log|F(x)||}{1+x^2}\,dx<\infty,
 \qquad
 \int_{\mathbb R}\frac{\log|F(x)|}{1+x^2}\,dx>-\infty.      \tag{CN5.3}
\]

The passage from the signed boundary theorem to a logarithmic integral required the local trace calculation. Merely evaluating an almost-everywhere boundary expression would not identify the measure at zeros.

<a id="CN6"></a>

## CN6. Convert derivative bounds into a logarithmic budget

Integration by parts has no boundary terms because \(u\) and all its derivatives vanish outside a compact interval. For real \(\xi\ne0\) and \(k\ge1\),

\[
 (i\xi)^k F(\xi)=\int u^{(k)}(t)e^{-i\xi t}dt,\qquad
 |F(\xi)|\le2R\,A_k|\xi|^{-k}.                            \tag{CN6.1}
\]

Set \(C=\max(a,2R)>0\). The zeroth bound is \(|F(\xi)|\le a\le C\). Thus all \(k\ge0\) are covered with this one constant.

First \(M_j\to\infty\). Otherwise monotonicity gives a finite \(L\) with \(M_j\le L\) for all \(j\). For \(|\xi|>L\), (CN6.1) gives \(|F(\xi)|\le2R(L/|\xi|)^k\) for every \(k\), forcing \(F(\xi)=0\). An interval of zeros contradicts CN2–CN3. This proves the claim.

For \(r>0\), define

\[
 T(r)=\sum_{j\ge1}\log^+(r/M_j),\qquad
 \log^+s=\max(0,\log s).                                 \tag{CN6.2}
\]

Only finitely many terms are nonzero on any bounded interval of \(r\). If \(q\) is the number of \(M_j<r\), the product \(A_k/r^k\) decreases through those \(q\) factors and thereafter multiplies by factors at least one. Repeated values equal to \(r\) change neither the product nor \(T\). Therefore

\[
 \inf_{k\ge0}\frac{A_k}{r^k}
 =\prod_{j=1}^{q}\frac{M_j}{r}
 =e^{-T(r)},\qquad
 |F(\xi)|\le C e^{-T(|\xi|)}.                             \tag{CN6.3}
\]

At a zero the logarithmic inequality retains its extended meaning. On the positive axis it reads

\[
 0\le T(r)\le\log C-\log|F(r)|.                           \tag{CN6.4}
\]

This optimization is exactly where the ordered thresholds are used.

![Derivative thresholds determine a Fourier envelope and an exact reciprocal budget.](figures/frequency-budget.png)

*Figure 1.* The first panel gives \(T(r)\) for the model thresholds \(M_j=j\) and \(M_j=j^2\), and the second gives their normalized envelopes \(e^{-T(r)}\) with \(C=1\). These are algebraic envelopes, not asserted Fourier transforms of compact bumps. Every active threshold is included in the displayed frequency range. The final panel shows the exact finite-budget integrals \(\int_1^\infty T_N(r)r^{-2}dr=\sum_{j=1}^N1/M_j\). Their different limiting behavior is proved in CN7 and CN9; finite plotted budgets illustrate that proof.

<a id="CN7"></a>

## CN7. Tonelli turns the budget into the reciprocal series

For \(r\ge M_1>0\),

\[
 r^{-2}\le(1+M_1^{-2})(1+r^2)^{-1}.                       \tag{CN7.1}
\]

The right side of (CN6.4) is nonnegative and at most
\(|\log C|+|\log|F(r)||\).
Equation (CN5.3) and (CN7.1) therefore give

\[
 \int_{M_1}^{\infty}T(r)\frac{dr}{r^2}<\infty.             \tag{CN7.2}
\]

Each summand of \(T\) is nonnegative. Tonelli applies before any conclusion about convergence of the sum. Since \(M_j\ge M_1\),

\[
 \begin{aligned}
 \int_{M_1}^{\infty}T(r)\frac{dr}{r^2}
 &=\sum_{j\ge1}\int_{M_j}^{\infty}\log(r/M_j)\frac{dr}{r^2}\\
 &=\sum_{j\ge1}\frac1{M_j}.
 \end{aligned}                                             \tag{CN7.3}
\]

To verify the last identity, integrate by parts. The boundary term
\(-\log(r/M_j)/r\) vanishes at \(M_j\) and infinity; the remaining integral is \(\int_{M_j}^\infty r^{-2}dr=1/M_j\). Finiteness in (CN7.2) proves the theorem. \(\square\)

The zero function satisfies every such derivative bound, even for divergent reciprocal series. Nontriviality is essential both for the conclusion and for the subharmonic logarithm.

<a id="CN8"></a>

## CN8. Constant factors and the compact-support restriction

The proof also handles

\[
 \|u^{(k)}\|_\infty\le B H^k\prod_{j=1}^k M_j,
 \qquad B,H>0,\quad k\ge1.                               \tag{CN8.1}
\]

Apply Theorem CN to \(u/B\) and \(N_j=HM_j\). They are still positive and nondecreasing. The conclusion \(\sum1/N_j<\infty\) is equivalent to \(\sum1/M_j<\infty\). No bound for \(k=0\) is needed.

Compact support cannot be replaced by arbitrary smoothness. The function \(u(x)=\sin x\) has \(\|u^{(k)}\|_\infty=1\le k!\) for every \(k\ge1\). With the strictly increasing thresholds \(M_j=j\), its reciprocal series diverges. The function is nonzero and smooth, but its support is the whole line. There is no ordinary absolutely integrable Fourier transform of the form (CN2.1), and the compact-support argument does not apply.

<a id="CN9"></a>

## CN9. Three worked examples

**Example 1: the analytic-size obstruction.** For \(M_j=Hj\), the product is \(A_k=H^k k!\). The series \(\sum1/(Hj)\) diverges: each block \(2^{m-1}<j\le2^m\) contributes at least \(1/(2H)\). Hence a compactly supported smooth \(u\) with these bounds must be zero. By CN8 the same holds with an additional fixed factor \(B\). This conclusion concerns the stated derivative bounds, not a pointwise estimate at a single point.

**Example 2: power thresholds and their exact budget.** Let \(M_j=j^\alpha\), \(\alpha>0\). For \(r\ge1\), put \(m=\lfloor r^{1/\alpha}\rfloor\). Equal-threshold terms are zero, so

\[
 T(r)=m\log r-\alpha\log(m!),\qquad
 T(r)=\int_1^r\frac{\lfloor t^{1/\alpha}\rfloor}{t}\,dt.   \tag{CN9.1}
\]

The integral expression follows by writing each contribution as
\(\log^+(r/j^\alpha)=\int_1^r\mathbf1_{\{t>j^\alpha\}}dt/t\)
and summing finitely many terms. The discrete threshold points \(t=j^\alpha\) do not change the integral. Since
\(t^{1/\alpha}-1\le\lfloor t^{1/\alpha}\rfloor\le t^{1/\alpha}\),

\[
 \alpha(r^{1/\alpha}-1)-\log r
 \le T(r)\le\alpha(r^{1/\alpha}-1).                       \tag{CN9.2}
\]

The reciprocal series converges exactly when \(\alpha>1\). For that case monotonicity and integration give
\(\sum_{j\ge1}j^{-\alpha}\le1+1/(\alpha-1)\).
For \(0<\alpha\le1\), \(j^{-\alpha}\ge j^{-1}\), and the block proof in Example 1 gives divergence. Thus the necessity theorem rules out a nonzero compact function in the latter range. It does not supply a function in every case of convergence.

**Example 3: one actual compatible compact bump.** Define

\[
 f(t)=
 \begin{cases}e^{-1/t},&t>0,\\0,&t\le0,\end{cases}
 \qquad
 u(x)=f(1-x)f(1+x)
 =\begin{cases}e^{-2/(1-x^2)},&|x|<1,\\0,&|x|\ge1.\end{cases} \tag{CN9.3}
\]

We prove the uniform bounds

\[
 \|f^{(k)}\|_\infty\le9^k(k!)^2\quad(k\ge0),\qquad
 \|u^{(k)}\|_\infty\le18^k(k!)^2\quad(k\ge1).              \tag{CN9.4}
\]

For \(t>0\), \(e^{-1/z}\) has a convergent Taylor series on \(|z-t|<t\). This follows by substituting the geometric series for \(1/(t+w)\) into the entire exponential; on smaller discs the series converge uniformly and absolutely. On the circle \(|z-t|=t/2\),
\(\operatorname{Re}(1/z)\ge2/(9t)\).
Indeed \(\operatorname{Re}z\ge t/2\) and \(|z|\le3t/2\). Averaging the Taylor series against \(e^{-ik\theta}\) picks out its \(k\)-th coefficient. Taking absolute values gives

\[
 |f^{(k)}(t)|\le k!(2/t)^k e^{-2/(9t)}.                  \tag{CN9.5}
\]

This is the coefficient estimate just proved, not an assumed derivative estimate for a bump. For each fixed \(k\), the right side tends to zero as \(t\downarrow0\). Extending all derivatives by zero is valid inductively: the derivative at zero of the preceding extended derivative is zero because its bound, divided by \(t\), still tends to zero. Thus \(f\) is smooth on the whole line.

For \(k\ge1\), the maximum of \(t^{-k}e^{-c/t}\), \(c=2/9\), is \((k/(ec))^k\). Also
\(\log(k!)\ge\int_1^k\log s\,ds=k\log k-k+1\),
so \((k/e)^k\le k!\). These facts give the first estimate in (CN9.4); the \(k=0\) estimate is \(0\le f\le1\).

Leibniz's rule and reflection of the argument now give

\[
 \begin{aligned}
 |u^{(k)}|
 &\le9^k\sum_{j=0}^k\binom{k}{j}(j!)^2((k-j)!)^2\\
 &=9^k(k!)^2\sum_{j=0}^k\binom{k}{j}^{-1}
 \le9^k(k!)^2(k+1)\le18^k(k!)^2.
 \end{aligned}                                             \tag{CN9.6}
\]

The last inequality uses \(k+1\le2^k\) for \(k\ge1\), which follows by induction. The function has compact support \([-1,1]\) and \(u(0)=e^{-2}>0\). Thus it satisfies the exact theorem hypotheses with \(M_j=18j^2\). Its reciprocal series is at most \(2/18=1/9\), by the integral bound in Example 2. This proves compatibility for a concrete function without claiming a general converse.

![A real zero has an integrable logarithmic trace, and an explicit compact bump has compatible derivative growth.](figures/trace-and-bump.png)

*Figure 2.* The left panel is the local zero factor \(F(z)=z^2\), so its horizontal logarithm is \(\log(x^2+y^2)\) and its boundary density is \(2\log|x|\). This is a local model, not the global half-plane class in CN5. The middle panel gives the exact interval error in (CN4.3) for \(m=2,d=1\), together with the proved bound \(2\pi y\). The final panel is the actual compact bump in (CN9.3), with the complete derivative estimate \(18^k(k!)^2\) proved above. The plotted values illustrate the formulas; they do not replace the infinite-order argument.

<a id="CN10"></a>

## CN10. Exercises with complete solutions

**Exercise 1.** Prove \(\int_M^\infty\log(r/M)r^{-2}dr=1/M\), including both endpoint terms.

**Solution.** Use \(\log(r/M)\) as the differentiable factor and \(-1/r\) as the antiderivative of \(r^{-2}\). At \(r=M\) the logarithm is zero. At infinity \(\log(r/M)/r\to0\). The remaining integral is \(\int_M^\infty r^{-2}dr=1/M\). Positivity of \(M\) makes every step legitimate.

**Exercise 2.** For the repeated thresholds \(M_1=M_2=2,M_3=5\), calculate the finite envelope \(T_3(r)\) and the corresponding minimizing product.

**Solution.** If \(r\le2\), \(T_3=0\) and \(k=0\) minimizes the product. For \(2<r\le5\), \(T_3=2\log(r/2)\), and the minimum is \(4/r^2\), attained at \(k=2\) (also \(k=3\) at \(r=5\)). For \(r>5\), \(T_3=2\log(r/2)+\log(r/5)\), and the minimum is \(20/r^3\). Equality of the first two thresholds causes no difficulty. The finite reciprocal budget is \(1/2+1/2+1/5=6/5\).

**Exercise 3.** Derive the local trace error (CN4.3).

**Solution.** By evenness the error is
\(m\int_0^d\log(1+y^2/x^2)dx\).
Integration by parts gives
\(md\log(1+y^2/d^2)+2my^2\int_0^d(x^2+y^2)^{-1}dx\).
The endpoint at zero vanishes because \(x|\log x|\to0\). Evaluating the arctangent gives the stated formula. Its upper bound \(m\pi y\) follows by enlarging the nonnegative integration region to the whole line in (CN4.2).

**Exercise 4.** Why does local \(L^1\) convergence identify the signed boundary measure, including at a real zero?

**Solution.** On the compact support of \(\phi\in C_c\), the difference of its two density pairings is at most \(\|\phi\|_\infty\) times the \(L^1\) difference. CN4 makes this tend to zero. L135 gives the same limit as the pairing with \(\sigma\), so every continuous compact test agrees with \(g\,dx\). These pairings determine the Radon measure. A logarithmic zero is locally integrable; its infinite value at the single zero has zero volume measure and produces no extra boundary atom in this identification.

**Exercise 5.** Suppose the uniform derivative bounds are \(B H^k k!\). Explain the conclusion for a nonzero compactly supported smooth function, and give a noncompact function showing that the support assumption matters.

**Solution.** Divide the function by \(B>0\) and choose \(M_j=Hj\). The product is \(H^k k!\), but \(\sum1/(Hj)\) diverges by the dyadic-block estimate. Theorem CN therefore excludes such a nonzero compact function. On the full line, \(\sin x\) has derivatives of absolute value at most one, hence at most \(k!\). It is nonzero and smooth but not compactly supported. Its example satisfies all those derivative inequalities while lying outside the theorem.

**Exercise 6.** Verify that the bump in (CN9.3) meets the exact product bounds for \(M_j=18j^2\), and locate each place where compact support, nontriviality and ordering enter the general proof.

**Solution.** Formula (CN9.6) is
\(\|u^{(k)}\|_\infty\le18^k(k!)^2=\prod_{j=1}^k18j^2\).
The bump is smooth by (CN9.5), vanishes outside \([-1,1]\), and is positive at zero. In the general proof compact support supplies the entire extension, the linear height bound and boundary-free integration by parts. Nontriviality supplies a nonzero Fourier transform and a genuine subharmonic logarithm, and excludes bounded thresholds. Ordering makes the factors \(M_j/r\) cross one in a single prefix and ensures \(M_j\ge M_1\) in Tonelli's identity. These uses are distinct.

<a id="CN11"></a>

## CN11. Source credit

The classical target is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Theorem 16.1.10, printed page 314: first edition 1983, second revised printing 1990, reprint 2005. Its hypothesis is \(C_c^\infty(\mathbb R)\), and its derivative bounds start at order one. The Fourier and trace proof, Gaussian injectivity argument, logarithmic error formula, explicit bump estimate, examples, solutions and diagrams here are independently written. The exact half-plane theorem and signed logarithmic kernel are linked at the beginning.
