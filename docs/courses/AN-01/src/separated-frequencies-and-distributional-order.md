# Separated frequencies and distributional order

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

The number of test derivatives needed by a Fourier distribution can be estimated from a weighted square integral. For a discrete spectrum, a uniform sampling estimate plays the same role. We prove both estimates, construct the resulting series on every Schwartz test, and then calculate polynomially weighted lattice series exactly. Their true order can be smaller than the first general estimate.

All distribution pairings are complex linear. Use the complete [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, and [U040](tempered-growth-and-spectral-cutoffs.md), formula (0.1) and Lemma 2.1:
\[
F\phi(\xi)=\int e^{-ix\cdot\xi}\phi(x)\,dx,\qquad
(Fu)(\phi)=u(F\phi),\qquad
G=(2\pi)^{-n}RF.
\]
Here \(R\phi(x)=\phi(-x)\), and \(FG=GF=I\). The same foundation proves every Fourier seminorm, all transpose signs, and compact-test density. We write
\[
P_N(\phi)=\max_{|\alpha|\le N}\sup_x
 \langle x\rangle^N|\partial^\alpha\phi(x)|,\qquad
\langle x\rangle=(1+|x|^2)^{1/2}.
\]
A bounded Schwartz family has all these seminorms uniformly bounded. Strong convergence of tempered distributions means uniform convergence on each such family.

The supplied [scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, prove compactness, FTC, smooth cutoffs, exponentials and trigonometry. The [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.2 and 16, prove the measure construction, affine volume scaling, absolute Fubini, convergence theorems and Hölder, including Cauchy–Schwarz. [U008](order-positivity-and-limits.md), Proposition 1.2, gives the precise local finite-order test estimate. These are the programme inputs; the extra square-norm identity needed here is proved next.

**Lemma 0.1 (Schwartz Plancherel with every weight coefficient).** For Schwartz \(f,g\),
\[
\int Ff(\xi)\overline{Fg(\xi)}\,d\xi
=(2\pi)^n\int f(x)\overline{g(x)}\,dx.
\]
Consequently, for each nonnegative integer \(m\),
\[
\begin{gathered}
\|\langle\xi\rangle^mF\psi\|_2^2
=(2\pi)^n\sum_{|\alpha|\le m}
 c_{m,\alpha}\|\partial^\alpha\psi\|_2^2,\\
c_{m,\alpha}=\frac{m!}{(m-|\alpha|)!\alpha!}.
\end{gathered}
\tag{0.1}
\]

**Proof.** Substitute the defining integral for \(\overline{Fg}\) into the left side. The double absolute integral is
\(\|Ff\|_1\|g\|_1<\infty\), by F1–F2. Fubini and the proved identity \(GFf=f\) give
\[
\begin{aligned}
\int Ff\,\overline{Fg}
&=\int\overline{g(x)}
       \left(\int e^{ix\cdot\xi}Ff(\xi)\,d\xi\right)dx\\
&=(2\pi)^n\int f\,\overline g.
\end{aligned}
\]
Taking \(g=f\) proves the square-norm formula. Expand
\((1+\xi_1^2+\cdots+\xi_n^2)^m\): choosing \(\alpha_j\) copies of \(\xi_j^2\) and \(m-|\alpha|\) copies of 1 among the \(m\) factors gives exactly \(c_{m,\alpha}\). This finite expansion can be integrated term by term. For each term, F2 gives
\(F(\partial^\alpha\psi)=(i\xi)^\alpha F\psi\); its absolute square is \(\xi^{2\alpha}|F\psi|^2\). Apply the already proved square-norm identity to that derivative. This proves (0.1) without an \(L^2\) extension theorem or any unproved density assertion. \(\square\)

We will also use
\[
\int_{\mathbb R^n}\langle x\rangle^{-s}\,dx<\infty
\quad\hbox{for }s>n.
\]
Here is a proof with no polar-coordinate premise. The unit ball has finite measure because it lies in a finite cube. On \(2^j\le|x|<2^{j+1}\), the integrand is at most \(2^{-js}\), and the shell is contained in a cube of volume \(2^{n(j+2)}\). Summation is a geometric series with ratio \(2^{n-s}<1\).

## A weighted function gives a finite-order Fourier distribution

**Theorem 1.1 (weighted square integrability).** Let \(m\ge0\) be an integer. If a measurable \(u\) satisfies
\[
I=\int |u(x)|^2\langle x\rangle^{-2m}\,dx<\infty,
\tag{1.1}
\]
then \(u\) defines a regular tempered distribution, and \(Fu\) has order at most \(m\) on every compact set.

**Proof.** On a compact \(K\), Cauchy–Schwarz bounds
\[
\int_K|u|\le \sqrt I
 \left(\int_K\langle x\rangle^{2m}\,dx\right)^{1/2}<\infty.
\]
Thus the regular distribution is defined. For \(\phi\in\mathcal S\), the same inequality gives
\(\int|u\phi|\le\sqrt I\,\|\langle x\rangle^m\phi\|_2\). Choose an integer \(N>m+n/2\). Then
\[
\|\langle x\rangle^m\phi\|_2
\le P_N(\phi)
 \left(\int\langle x\rangle^{2m-2N}\,dx\right)^{1/2}.
\tag{1.2}
\]
The shell proof above makes the last constant finite. This proves absolute pairing and Schwartz continuity.

In particular \((Fu)(\psi)=\int uF\psi\) converges absolutely. Define
\[
S_m(\psi)^2=\sum_{|\alpha|\le m}
c_{m,\alpha}\|\partial^\alpha\psi\|_2^2.
\]
Apply weighted Cauchy–Schwarz to \(F\psi\), then Lemma 0.1:
\[
|(Fu)(\psi)|\le (2\pi)^{n/2}\sqrt I\,S_m(\psi).
\tag{1.3}
\]
If \(\operatorname{supp}\psi\subset K\), each derivative has support in \(K\), and
\(\|\partial^\alpha\psi\|_2\le |K|^{1/2}\|\partial^\alpha\psi\|_\infty\).
The finite sum therefore gives a compact-test estimate through order \(m\). This includes measure-zero compacts, on which every smooth supported test is zero. \(\square\)

This is an estimate of distributional order. Solutions 2 and 7 exhibit a smaller exact order, and a Fourier transform represented by a point mass.

## Sampling a Fourier transform at separated points

**Theorem 2.1 (uniform sampling).** For every compact \(K\subset\mathbb R^n\) there is a finite \(C_K\) such that
\[
\sum_j|F\phi(\xi_j)|^2\le C_K\|\phi\|_2^2
\tag{2.1}
\]
whenever \(\phi\in C_c^\infty\), \(\operatorname{supp}\phi\subset K\), and the finite or countable family of frequencies satisfies
\(|\xi_i-\xi_j|\ge1\) for \(i\ne j\). The constant depends on \(K,n\), not the placement or number of points.

**Proof: decay and counting.** Take a real compact smooth \(\eta=1\) near \(K\). Such a function is obtained by a cutoff equal one on a cube containing \(K\). Put
\(g_j(x)=\eta(x)e^{ix\cdot\xi_j}\), and use the inner product
\(\langle f,g\rangle=\int f\overline g\), linear in the first slot. Its Gram entries are
\[
\begin{gathered}
A_{ij}=\langle g_i,g_j\rangle
=F(\eta^2)(\xi_j-\xi_i),\\
|A_{ij}|\le C_{\eta,M}
(1+|\xi_i-\xi_j|)^{-M},\qquad M>n.
\end{gathered}
\tag{2.2}
\]
Choose an integer \(M>n\). Since \(\eta^2\) is Schwartz, F2 proves exactly this decay.

The balls \(B(\xi_j,1/3)\) are disjoint. The unit ball has a positive finite volume \(v_n\): it contains a small cube and is contained in a finite cube. Affine scaling, proved in the integration foundation, gives volume \(v_n/3^n\) for each small ball. If their centers lie in \(B(z,R)\), they lie in \(B(z,R+1/3)\). Additivity for any finite selection gives
\[
\#\{j:|\xi_j-z|\le R\}\le C_n(1+R)^n.
\tag{2.3}
\]
The same bound for the full family follows by taking the supremum of its finite subcounts. In particular the frequency set is locally finite.

Fix a row \(i\). In the radius-two ball use (2.3). In the shell
\(2^\ell<|\xi_j-\xi_i|\le2^{\ell+1}\), use its radius-\(2^{\ell+1}\) count and the factor \(2^{-\ell M}\). Thus every row sum of \(|A|\) is at most
\[
B=C_{\eta,M,n}
\left(1+\sum_{\ell\ge1}2^{\ell(n-M)}\right)<\infty.
\tag{2.4}
\]
The identical argument bounds every column sum.

**Proof: the finite quadratic estimate.** For finitely supported complex \(c_j\), norm expansion and
\(2|c_i||c_j|\le |c_i|^2+|c_j|^2\) give
\[
\begin{aligned}
\left\|\sum_jc_jg_j\right\|_2^2
&\le\sum_{i,j}|A_{ij}||c_i||c_j|\\
&\le\tfrac12\sum_{i,j}|A_{ij}|
 (|c_i|^2+|c_j|^2)\\
&\le B\sum_j|c_j|^2.
\end{aligned}
\tag{2.5}
\]
Every sum in this computation is finite. This is the elementary matrix form of the Schur estimate; no infinite-matrix operator theorem is being assumed.

Write \(v_j=\langle\phi,g_j\rangle=F\phi(\xi_j)\). For any finite \(J\), set \(c_j=v_j\) on \(J\) and zero elsewhere. Then
\[
\begin{aligned}
\sum_{j\in J}|v_j|^2
&=\left\langle\phi,\sum_{j\in J}v_jg_j\right\rangle\\
&\le\|\phi\|_2\sqrt B
 \left(\sum_{j\in J}|v_j|^2\right)^{1/2}.
\end{aligned}
\]
The first quantity is real and nonnegative; the inequality follows by taking the absolute value of the inner product and applying Cauchy–Schwarz. Divide if the sum is positive; if zero, the desired bound already holds. Taking the supremum over finite \(J\) gives (2.1) with \(C_K=B\). All constants were uniform over the frequency family. \(\square\)

Solution 3 proves the exact dependence on a general separation \(\delta>0\), including the optimal small-\(\delta\) exponent.

## Exponential series with weighted square-summable coefficients

**Theorem 3.1 (a tempered series and its order).** Suppose \(m\ge0\) is an integer, \(|\xi_i-\xi_j|\ge1\) for distinct indices, and
\[
A^2=\sum_j|a_j|^2\langle\xi_j\rangle^{-2m}<\infty.
\tag{3.1}
\]
Then
\[
T=\sum_j a_j e^{ix\cdot\xi_j}
\tag{3.2}
\]
converges strongly in \(\mathcal S'\), independently of enumeration. It has local order at most \(m\), and
\[
FT=(2\pi)^n\sum_j a_j\delta_{\xi_j}.
\tag{3.3}
\]
The Fourier support is exactly the closed set \(\{\xi_j:a_j\ne0\}\).

**Proof: construct the functional and its strong limit.** Put \(Q=m+n+1\). Applying (2.3) about zero and summing dyadic shells gives
\[
\sum_j\langle\xi_j\rangle^{2m-2Q}\le C_{m,n}.
\tag{3.4}
\]
Indeed the shell exponent is \(n+2m-2Q=-n-2<0\), and the radius-two count is uniformly bounded. Hence
\[
\begin{aligned}
\sum_j\langle\xi_j\rangle^{2m}|F\phi(-\xi_j)|^2
&\le C_{m,n}\!
 \left(\sup_\xi\langle\xi\rangle^Q|F\phi(\xi)|\right)^2\\
&\le C P_L(\phi)^2
\end{aligned}
\tag{3.5}
\]
for one finite integer \(L\), by the proved Fourier seminorm estimates. Weighted Cauchy–Schwarz makes
\[
T(\phi):=\sum_j a_jF\phi(-\xi_j)
\]
absolutely convergent and bounds it by \(CA P_L(\phi)\). This defines a continuous tempered functional directly.

For a finite partial sum \(T_N\) in any fixed enumeration, the same estimate gives
\[
\begin{gathered}
|(T-T_N)(\phi)|\le C A_NP_L(\phi),\\
A_N^2=\sum_{j>N}|a_j|^2\langle\xi_j\rangle^{-2m}.
\end{gathered}
\tag{3.6}
\]
The tail \(A_N\) tends to zero. More generally, outside any finite index set use its weighted square tail in place of \(A_N\). These tails become arbitrarily small, while \(P_L\) is uniformly bounded on a bounded Schwartz family. This proves strong convergence of the finite-subset sums, and therefore of every enumeration, to the same already constructed \(T\).

**Proof: sharpen the order on compact tests.** The finite multinomial expansion from Lemma 0.1 and the Fourier derivative identity give
\[
\begin{aligned}
\sum_j\langle\xi_j\rangle^{2m}|F\phi(-\xi_j)|^2
&=\sum_{|\alpha|\le m}c_{m,\alpha}
 \sum_j|F(\partial^\alpha\phi)(-\xi_j)|^2\\
&\le C_K\sum_{|\alpha|\le m}
 c_{m,\alpha}\|\partial^\alpha\phi\|_2^2
\end{aligned}
\tag{3.7}
\]
when \(\operatorname{supp}\phi\subset K\). Apply Theorem 2.1 to each derivative and to the reflected separated family. Weighted Cauchy–Schwarz now gives
\[
|T(\phi)|\le A\sqrt{C_K}\,S_m(\phi)
\le C_{K,m}A\max_{|\alpha|\le m}\|\partial^\alpha\phi\|_\infty.
\]
This proves the order bound, including \(m=0\). The same inequality holds for any coefficient tail.

**Proof: compute the transform and support.** Inversion at a fixed \(\zeta\) gives
\[
\int e^{ix\cdot\zeta}F\psi(x)\,dx=(2\pi)^n\psi(\zeta).
\]
The integral is absolutely convergent, so the Fourier transform of a plane wave is \((2\pi)^n\delta_\zeta\). Thus (3.3) holds for finite sums. The Fourier map preserves strong convergence because it takes bounded test families to bounded test families, as explicitly proved in U040. The point-mass series also converges strongly: apply weighted Cauchy–Schwarz, (3.4), and
\(|\psi(\xi)|\le P_Q(\psi)\langle\xi\rangle^{-Q}\).
Pass to the strong limit to obtain (3.3).

A locally finite separated set, and every subset of it, is closed: any convergent sequence of its points eventually lies in a fixed compact ball with finitely many points. Outside the nonzero-coefficient set a compact test pairs to zero. Around a point with \(a_j\ne0\), a small bump equal one at that point and supported away from the other frequencies gives a nonzero pairing. This proves the exact support assertion. \(\square\)

For instance \(a_j=j^2\), \(\xi_j=j\) on the integer lattice satisfies (3.1) with \(m=3\). The next theorem determines its smaller exact physical order.

## From Abel peaks to a lattice of point derivatives

**Theorem 4.1 (the full polynomial comb).** Let \(P(t)=\sum_{h=0}^d p_ht^h\), with \(p_d\ne0\). Then, strongly in \(\mathcal S'(\mathbb R)\),
\[
\sum_{j\in\mathbb Z}P(j)e^{ijx}
=2\pi\sum_{k\in\mathbb Z}\sum_{h=0}^d
 p_h(-i)^h\delta_{2\pi k}^{(h)}.
\tag{K1}
\]
Its physical support is \(2\pi\mathbb Z\); its exact local order near every lattice point is \(d\). Its Fourier support is
\(\{j\in\mathbb Z:P(j)\ne0\}\).

**Proof: the positive periodic kernel.** For \(0<r<1\), sum the positive and negative geometric series:
\[
\begin{aligned}
P_r(x)&=\sum_{j\in\mathbb Z}r^{|j|}e^{ijx}\\
&=1+\frac{re^{ix}}{1-re^{ix}}
     +\frac{re^{-ix}}{1-re^{-ix}}\\
&=\frac{1-r^2}{1-2r\cos x+r^2}.
\end{aligned}
\tag{K2}
\]
The series is absolutely uniform. Every differentiated series is also uniform, since \(\sum_{j\ge1}j^h r^j<\infty\): the ratio of successive positive terms tends to \(r<1\), so its tail is bounded by a geometric series. Passing the finite-series FTC identity to the uniform limits justifies each derivative. Integration over \([-\pi,\pi]\) kills each nonconstant integer exponential and leaves
\(\int_{-\pi}^{\pi}P_r=2\pi\). This also follows directly from the displayed series, without a Fourier completeness theorem.

The denominator is \((1-r)^2+2r(1-\cos x)>0\). For \(0<a<\pi\) and \(r\ge1/2\), the elementary monotonicity of cosine on \([0,\pi]\) gives
\[
\begin{gathered}
\sup_{a\le|x|\le\pi}P_r(x)
\le\frac{1-r^2}{2r(1-\cos a)},\\
E_r(a):=\int_{a\le|x|\le\pi}P_r(x)\,dx
\le\frac{2\pi(1-r^2)}{2r(1-\cos a)}
\longrightarrow0.
\end{gathered}
\tag{K3}
\]
The maximum, at the lattice points, is \((1+r)/(1-r)\). The mass in each period stays \(2\pi\) while the kernel tends to zero away from those points. The free NIST DLMF formulas 1.15.12–1.15.13 record this Poisson kernel and its mass; the calculation above proves both.

**Proof: concentration on all Schwartz tests.** Periodize a test:
\[
q_\psi(x)=\sum_{k\in\mathbb Z}\psi(x+2\pi k),\qquad
\|q_\psi\|_\infty+\|q_\psi'\|_\infty\le CP_3(\psi).
\tag{K4}
\]
The norms here are on \([-\pi,\pi]\). To prove the assertions, note that
\(|x+2\pi k|\ge\pi|k|\) there when \(|k|\ge1\). For every derivative order \(h\),
\[
|\psi^{(h)}(x+2\pi k)|
\le P_{h+2}(\psi)\langle x+2\pi k\rangle^{-2}.
\]
The latter weights have a uniformly summable bound, since
\(\sum_{k\ge1}k^{-2}\le1+\int_1^\infty t^{-2}dt\).
The derivative series converge uniformly. Passing FTC to their partial sums proves smoothness and termwise differentiation. Absolute reindexing proves periodicity, and \(h=0,1\) gives (K4).

The bounded periodic \(P_r\) and integrable \(\psi\) allow absolute splitting into periods. Therefore
\[
\begin{gathered}
\int_{\mathbb R}P_r(x)\psi(x)\,dx
=\int_{-\pi}^{\pi}P_r(x)q_\psi(x)\,dx,\\
\left|\int_{\mathbb R}P_r\psi-2\pi q_\psi(0)\right|
\le2\pi a\|q_\psi'\|_\infty
   +2E_r(a)\|q_\psi\|_\infty.
\end{gathered}
\tag{K5}
\]
For \(|x|<a\), FTC bounds \(|q_\psi(x)-q_\psi(0)|\) by \(a\|q_\psi'\|_\infty\); elsewhere use \(2\|q_\psi\|_\infty\). Positivity and the exact mass then prove (K5). On a bounded Schwartz family both norms in (K4) have one common bound. First choose \(a\) small, then \(r\) close to one. Thus
\[
P_r\longrightarrow2\pi\sum_{k\in\mathbb Z}\delta_{2\pi k}
\quad\hbox{strongly in }\mathcal S'.
\tag{K6}
\]
The point sum is itself tempered, with the explicit bound
\(\sum_k|\psi(2\pi k)|\le P_2(\psi)\sum_k\langle2\pi k\rangle^{-2}\).
Its tails tend uniformly to zero on bounded families.

**Proof: identify the series and every polynomial coefficient.** Theorem 3.1 applies to coefficients one on \(\mathbb Z\), with \(m=1\). The coefficient difference from \(r^{|j|}\) has squared weighted norm
\[
\sum_{j\in\mathbb Z}\frac{(1-r^{|j|})^2}{1+j^2}\longrightarrow0.
\]
For clarity, choose a finite set with small tail of \(\sum(1+j^2)^{-1}\); on that finite set each summand tends to zero, and on the tail \(|1-r^{|j|}|\le1\). This proves the limit without any interchange assumption. Estimate (3.5) and weighted Cauchy–Schwarz show strong convergence of \(P_r\) to the unweighted exponential series. Comparison with (K6), on every test, identifies that series.

Each derivative maps bounded Schwartz families to bounded families, by the finite seminorm formula in F1. Its transpose is strongly continuous. Apply the finite operator
\(P(-i\partial_x)=\sum_{h=0}^d p_h(-i)^h\partial_x^h\) to the identity just proved. On \(e^{ijx}\) it gives \(P(j)e^{ijx}\); on the comb it gives every coefficient in (K1). This proves the stated strong identity. Independently, \(|P(j)|\le C_P\langle j\rangle^d\) makes Theorem 3.1 applicable with \(m=d+1\). The point-derivative series on the right converges strongly too: each tail is bounded by
\[
C_P P_{d+2}(\psi)
\sum_{\text{omitted }k}\langle2\pi k\rangle^{-2}.
\]

**Proof: exact order and both supports.** On a compact set only finitely many lattice points contribute, giving order at most \(d\). If \(d\ge1\), fix \(x_k=2\pi k\), and choose a compact smooth \(\rho\) with \(\rho^{(d)}(0)\ne0\). It can be constructed as \(x^d/d!\) times a bump equal one near zero. For small \(s>0\), the tests
\(\psi_s(x)=s^d\rho((x-x_k)/s)\) lie in one fixed compact neighborhood containing no other lattice point. They satisfy
\[
\begin{gathered}
T_P(\psi_s)=2\pi\sum_{h=0}^d
 p_hi^h s^{d-h}\rho^{(h)}(0)
\longrightarrow2\pi p_di^d\rho^{(d)}(0)\ne0,\\
\|\psi_s\|_{C^{d-1}}\longrightarrow0.
\end{gathered}
\tag{K7}
\]
This excludes order \(d-1\) and detects each lattice point. For \(d=0\), every point has the nonzero mass \(2\pi p_0\), of exact order zero. The distribution vanishes off the lattice. Finally Theorem 3.1 gives
\(FT_P=2\pi\sum_jP(j)\delta_j\), with exact support at its nonzero masses. Integer roots of \(P\) remove frequency masses; they do not remove physical lattice points. \(\square\)

## Exercises

**Exercise 1 (foundation).** Expand the weighted identity (0.1) for \(n=2,m=2\), including the mixed second derivative.

**Exercise 2 (advanced).** For \(u(x_1,x_2)=x_1x_2\), find all integers \(m\ge0\) satisfying (1.1). Compute \(Fu\) and its exact local order at zero; compare the weighted estimate.

**Exercise 3 (advanced).** For frequencies separated by \(\delta>0\), prove a sampling constant at most \(C_K\max(1,\delta^{-n})\). When \(K\) contains an open ball, prove that the exponent \(n\) is optimal as \(\delta\downarrow0\).

**Exercise 4 (intermediate).** Sum \(\sum_{j\in\mathbb Z}j^2e^{ijx}\). For truncation to \(|j|\le N\), prove a compact-test remainder bound \(C_KN^{-1/2}\|\phi\|_{C^3}\). Determine both supports and the exact order.

**Exercise 5 (advanced).** Identify
\[
T_\theta=\sum_{j\in\mathbb Z\setminus\{0\}}
 |j|^{-1}e^{-ij\theta}e^{ijx},\qquad \theta\in\mathbb R,
\]
as a periodic locally integrable function. Prove strong convergence of the series and of its Abel sums, including identification of their local integral limit.

**Exercise 6 (intermediate).** Sum \(\sum_{j\in\mathbb Z}2^{-|j|}e^{ijx}\) as a positive smooth function. Prove that no Schwartz \(f\) fixes it by convolution.

**Exercise 7 (foundation).** For \(u=1\) in \(\mathbb R^n\), find all integer weights in (1.1). Prove that its Fourier transform has order zero but is not a continuous function distribution.

**Exercise 8 (intermediate).** Under Theorem 3.1, justify every reordering and every termwise derivative \(\partial^\beta\). Prove the local order bound \(m+|\beta|\).

**Exercise 9 (advanced: scale, shift and modulation).** For \(\lambda>0\), \(\theta,b\in\mathbb R\), and the full nonzero polynomial \(P(t)=\sum_{h=0}^d p_ht^h\), sum
\[
\sum_{j\in\mathbb Z}P(j)e^{-i\lambda j\theta}e^{i(b+\lambda j)x}.
\]
Give every point-derivative coefficient, including the Jacobian and modulation terms, both supports and the exact order. Include \(0<\lambda<1\).

**Exercise 10 (advanced: all annihilating jets).** For \(T_P\) in (K1), let \(g\) be smooth with every derivative of at most polynomial growth. Characterize \(gT_P=0\) by the complete jet at every \(2\pi k\), without dropping any coefficient of \(P\). Compare \(\sin(x/2)^{d+1}\) and, for \(d\ge1\), \(\sin(x/2)^d\).

## Solutions

**Solution 1.** The expansion is
\[
(1+\xi_1^2+\xi_2^2)^2
=1+2\xi_1^2+2\xi_2^2+\xi_1^4
 +2\xi_1^2\xi_2^2+\xi_2^4.
\]
Lemma 0.1 therefore gives
\[
\begin{aligned}
\|\langle\xi\rangle^2F\psi\|_2^2
=(2\pi)^2\bigl(&\|\psi\|_2^2
 +2\|\partial_1\psi\|_2^2
 +2\|\partial_2\psi\|_2^2\\
&+\|\partial_{11}\psi\|_2^2
 +2\|\partial_{12}\psi\|_2^2
 +\|\partial_{22}\psi\|_2^2\bigr).
\end{aligned}
\]
The mixed coefficient is two because either factor can supply \(\xi_1^2\).

**Solution 2.** There is no integrability difficulty on a bounded set. On a shell \(2^j\le|x|<2^{j+1}\), use
\(|x_1x_2|^2\le|x|^4\) and its containing square of area \(2^{2(j+2)}\). The weighted integral is bounded by a constant times
\(\sum_{j\ge0}2^{j(6-2m)}\), which converges for \(m>3\).

For necessity, take the disjoint interiors of the squares
\([2^j,2^{j+1}]^2\), \(j\ge0\). There the numerator is at least \(2^{4j}\), \(\langle x\rangle^{2m}\le C_m2^{2mj}\), and the square's area is \(2^{2j}\). Each contributes at least \(c_m2^{j(6-2m)}\). The sum diverges when \(m\le3\), including the constant-size contributions at equality. Thus exactly the integers \(m\ge4\) work.

The proved Fourier identities yield
\[
Fu=-(2\pi)^2\partial_{\xi_1}\partial_{\xi_2}\delta_0.
\]
The order is at most two. Choose \(\rho\in C_c^\infty\) with \(\partial_{12}\rho(0)\ne0\), for instance \(x_1x_2\) times a bump equal one near zero. For
\(\psi_\varepsilon(\xi)=\varepsilon^2\rho(\xi/\varepsilon)\),
the pairing is a fixed nonzero constant while the \(C^1\) norm tends to zero. All supports lie in one compact ball. Hence the exact order is two; the smallest weighted upper bound here is four.

**Solution 3.** Use disjoint balls of radius \(\delta/3\). Their volume comparison gives
\[
\#\{j:|\xi_j-z|\le R\}\le C_n(1+R/\delta)^n.
\]
On the radius-two ball this is at most \(C_n\max(1,\delta^{-n})\); on the shell with outer radius \(2^{\ell+1}\) it is at most
\(C_n\max(1,\delta^{-n})2^{\ell n}\). The same Fourier decay with \(M>n\) therefore gives row and column bounds
\(C_{K,n,M}\max(1,\delta^{-n})\). The finite calculation (2.5) and its following Cauchy–Schwarz argument prove the desired estimate.

For sharpness, choose a nonnegative nonzero smooth \(\phi\) supported in an open ball inside \(K\). Then \(F\phi(0)=\int\phi>0\), and continuity gives \(|F\phi(\xi)|\ge c>0\) on a small ball about zero. A fixed cube \([-a,a]^n\) lies in that ball. For sufficiently small \(\delta\), each coordinate interval has at least \(a/\delta\) points of \(\delta\mathbb Z\). Thus the \(\delta\)-separated grid \(\delta\mathbb Z^n\) has at least \((a/\delta)^n\) points there. Its sampling sum is at least \(c^2(a/\delta)^n\), while \(\|\phi\|_2\) is fixed. This proves the necessary lower growth and sharpness.

**Solution 4.** The coefficient condition holds with \(m=3\), and
\[
\sum_{|j|>N}j^4(1+j^2)^{-3}
\le2\sum_{j>N}j^{-2}
\le2\int_N^\infty t^{-2}dt=\frac2N.
\]
Use the tail version of (3.7) and weighted Cauchy–Schwarz to get
\[
|(T-T_N)(\phi)|
\le C_KN^{-1/2}\max_{0\le h\le3}\|\phi^{(h)}\|_\infty.
\]
The full polynomial formula, with \(P(t)=t^2\), gives
\(T=-2\pi\sum_k\delta''_{2\pi k}\), with exact order two and physical support \(2\pi\mathbb Z\). Its transform is \(2\pi\sum_jj^2\delta_j\), whose support is \(\mathbb Z\setminus\{0\}\). The order-three truncation estimate remains valid.

**Solution 5.** The coefficients have finite square sum
\(2\sum_{j\ge1}j^{-2}\), so Theorem 3.1 applies with \(m=0\). For \(0<r<1\), put \(s=x-\theta\). Absolute geometric convergence gives the Abel sum
\[
T_{\theta,r}(x)
=2\sum_{j\ge1}\frac{r^j}{j}\cos(js)
=-2\log|1-re^{is}|.
\tag{4.1}
\]
Here is a proof of the logarithm identity using only real calculus. On any compact subinterval \(0\le r\le r_0<1\), differentiating the series \(\sum r^j\cos(js)/j\) gives the uniform geometric sum
\[
\operatorname{Re}\frac{e^{is}}{1-re^{is}}
=\frac{\cos s-r}{1-2r\cos s+r^2}.
\]
This is the derivative of
\(-\tfrac12\log(1-2r\cos s+r^2)\). Both expressions vanish at \(r=0\); FTC proves their equality. No complex logarithm branch or external power-series theorem is required.

The squared coefficient difference from \(T_\theta\) is
\(2\sum_{j\ge1}(1-r^j)^2/j^2\), which tends to zero by the finite-head/small-tail argument used in Theorem 4.1. The global weighted pairing estimate then proves \(T_{\theta,r}\to T_\theta\) strongly.

To identify the function, for \(r\ge1/2\) compute
\[
|1-re^{is}|^2=(1-r)^2+4r\sin^2(s/2).
\]
Thus the modulus is at most two and at least
\(\sqrt2|\sin(s/2)|\). Its absolute logarithm is bounded by
\(C+|\log|\sin(s/2)||\). This is locally integrable: near a zero \(s_0=2\pi k\), FTC and continuity of cosine bound \(|\sin((s-s_0)/2)|\) above and below by positive constants times \(|s-s_0|\). Also
\(\int_0^\varepsilon|\log t|dt=\varepsilon(1-\log\varepsilon)<\infty\) for small \(\varepsilon\). The endpoint \(t\log t\to0\) follows by \(t=e^{-v}\) and the exponential-series bound on \(ve^{-v}\).

Off the zeros the pointwise limit and dominated convergence on each compact interval give
\[
T_\theta(x)=-2\log\bigl(2|\sin((x-\theta)/2)|\bigr).
\tag{4.2}
\]
This formula defines a locally integrable periodic function. If \(M\) is the absolute integral over one period, splitting the line into periods bounds its pairing by
\[
M\sum_{k\in\mathbb Z}\sup_{x\in[-\pi,\pi]}
|\psi(\theta+x+2\pi k)|\le C_\theta M P_2(\psi).
\]
The last sum is finite by the same integer-weight estimate as (K4), with a fixed translation. Thus it is tempered. Its compact-test limit equals the already proved strong limit; compact-test density identifies the distributions. The singularities occur at \(\theta+2\pi\mathbb Z\), and the factor 2 inside the logarithm preserves the constant term.

**Solution 6.** Formula (K2) at \(r=1/2\) gives
\[
u(x)=\frac3{5-4\cos x}>0.
\]
Every derivative series converges uniformly because
\(\sum_j|j|^h2^{-|j|}<\infty\); the FTC argument above gives a smooth periodic function. The coefficients are square summable, so
\(Fu=2\pi\sum_j2^{-|j|}\delta_j\). Every mass is nonzero; its support is the unbounded set \(\mathbb Z\). U040, Theorem 3.1, proves that a fixing Schwartz factor exists exactly when the Fourier support is compact. Hence none exists here.

**Solution 7.** The shell estimate proves finiteness of
\(\int\langle x\rangle^{-2m}dx\) if \(2m>n\). Conversely, the disjoint boxes
\([2^j,2^{j+1}]^n\) each contribute at least \(c_{m,n}2^{j(n-2m)}\). They have volume \(2^{jn}\), and the weight there is at least \(c_{m,n}2^{-2mj}\). The sum diverges when \(2m\le n\). The allowable integers are exactly
\(m\ge\lfloor n/2\rfloor+1\).

Nevertheless \(F1=(2\pi)^n\delta_0\), by F5, of exact order zero. If a continuous \(g\) represented this distribution, it would pair to zero with all tests away from zero. At a point away from zero where \(g\ne0\), multiply by a constant complex phase so that its real part is positive, then use continuity and a nonnegative bump in a small neighborhood to obtain a nonzero pairing. This contradiction forces \(g=0\) away from zero. Continuity forces \(g(0)=0\) as well, contradicting a test with value one at zero. Thus the transform is not a continuous function distribution.

**Solution 8.** Given a bounded Schwartz family \(B\), the factor \(\sup_{\phi\in B}P_L(\phi)\) in (3.5) is finite. The weighted square sum in (3.1) has a finite subset outside which its tail is arbitrarily small. Any permutation eventually includes this subset. The tail estimate makes the remaining pairing uniformly small on \(B\), and absolute pairing convergence identifies the common limit.

For a fixed multiindex \(\beta\), the map \(\phi\mapsto\partial^\beta\phi\) takes bounded Schwartz families to bounded families, directly from their seminorms. Transposition therefore preserves strong convergence. Differentiating finite sums and passing to the limit proves
\[
\partial^\beta T=\sum_j(i\xi_j)^\beta a_j e^{ix\cdot\xi_j}.
\]
The new coefficients satisfy
\[
\sum_j|(i\xi_j)^\beta a_j|^2
\langle\xi_j\rangle^{-2(m+|\beta|)}
\le\sum_j|a_j|^2\langle\xi_j\rangle^{-2m},
\]
since \(|\xi_j^\beta|\le\langle\xi_j\rangle^{|\beta|}\).
Theorem 3.1 with \(m+|\beta|\) proves the stated order and independently proves strong convergence of the differentiated series.

**Solution 9.** The maps
\(\psi(y)\mapsto\psi(\theta+y/\lambda)\) and
\(\psi(x)\mapsto e^{ibx}\psi(x)\) are continuous on \(\mathcal S\) and preserve bounded families. For the first, differentiate by the ordinary chain rule and use
\(\langle y\rangle^N\le C_{\lambda,\theta,N}\langle\theta+y/\lambda\rangle^N\).
For the second, use its finite Leibniz expansion. These inequalities follow from the weight comparison in U040 and fixed affine constants. Their transpose operations are strongly continuous.

Pull back (K1) by \(y=\lambda(x-\theta)\), then multiply by \(e^{ibx}\). Direct test substitution gives
\[
\begin{gathered}
\delta_{2\pi k}^{(h)}(\lambda(x-\theta))
=\lambda^{-h-1}\delta_{x_k}^{(h)},\\
x_k=\theta+\frac{2\pi k}{\lambda}.
\end{gathered}
\tag{K8}
\]
Indeed the left side acts as
\(\lambda^{-1}\delta_{2\pi k}^{(h)}(\psi(\theta+\,\cdot\,/\lambda))
=\lambda^{-h-1}(-1)^h\psi^{(h)}(x_k)\).
Thus the full answer, retaining every coefficient, is
\[
\begin{gathered}
S=\frac{2\pi}{\lambda}e^{ibx}
\sum_{k\in\mathbb Z}\sum_{h=0}^d
c_{h,\lambda}\delta_{x_k}^{(h)},
\qquad c_{h,\lambda}=p_h(-i/\lambda)^h,\\
e^{ibx}\delta_{x_k}^{(h)}
=e^{ibx_k}\sum_{\ell=0}^h
\binom h\ell(-ib)^{h-\ell}\delta_{x_k}^{(\ell)}.
\end{gathered}
\tag{K9}
\]
The second formula follows by applying \((-1)^h\partial^h\) to the actual product \(e^{ibx}\psi(x)\), and converting each test derivative to its point-distribution sign.

The operations just proved preserve the strong limits of the finite sums, for every fixed \(\lambda>0\). The leading coefficient at each \(x_k\) is
\((2\pi/\lambda)e^{ibx_k}p_d(-i/\lambda)^d\ne0\).
The shrinking-test proof (K7), now centered at \(x_k\), proves exact order \(d\) there and physical support \(\theta+(2\pi/\lambda)\mathbb Z\).

The transform of each plane wave and strong Fourier continuity give
\[
FS=2\pi\sum_{j\in\mathbb Z}
P(j)e^{-i\lambda j\theta}\delta_{b+\lambda j}.
\tag{K10}
\]
The point sum is strongly convergent by polynomial coefficient growth and rapid decrease of tests on this fixed affine lattice. Explicitly \(\langle b+\lambda j\rangle\ge c_{\lambda,b}\langle j\rangle\), after adjusting a positive constant on finitely many bounded indices; a weight of degree \(d+2\) leaves a summable \(\langle j\rangle^{-2}\) tail. Its exact support is
\(\{b+\lambda j:P(j)\ne0\}\), by isolated bump tests. This argument includes \(0<\lambda<1\) without a separation-one assumption.

**Solution 10.** Multiplication by \(g\) is continuous on \(\mathcal S\). For each \(P_N(g\psi)\), choose a nonnegative integer \(M\) bounding the polynomial growth of the finitely many derivatives of \(g\) through order \(N\). Leibniz gives
\(P_N(g\psi)\le C P_{N+M}(\psi)\).
Its transpose therefore defines the tempered distribution \(gT_P\).

For one point \(a\), direct product differentiation gives
\[
\begin{gathered}
g\delta_a^{(h)}
=\sum_{\ell=0}^h a_{h,\ell}\delta_a^{(\ell)},\\
a_{h,\ell}=(-1)^{h-\ell}\binom h\ell
g^{(h-\ell)}(a).
\end{gathered}
\tag{K11}
\]
Set \(c_h=p_h(-i)^h\). The coefficient of
\(\delta_a^{(d-s)}\), \(0\le s\le d\), in the complete product is
\[
\sum_{h=d-s}^d c_h a_{h,d-s}.
\tag{K12}
\]
The point derivatives are linearly independent: multiply
\((x-a)^\ell/\ell!\) by a bump equal one near \(a\). Its derivatives at \(a\), through order \(d\), isolate the \(\ell\)-th coefficient.

Now isolate \(a=2\pi k\) from the other lattice points. The highest coefficient first forces \(c_dg(a)=0\), hence \(g(a)=0\). Suppose the derivatives of \(g\) below order \(s\) vanish at \(a\). In (K12), every term with \(h<d\) contains one of those derivatives. The only remaining term is
\(c_d(-1)^s\binom ds g^{(s)}(a)\), with nonzero prefactor. It forces \(g^{(s)}(a)=0\). Induction proves necessity of
\[
g^{(s)}(2\pi k)=0
\quad(k\in\mathbb Z,\ 0\le s\le d).
\]
Conversely these jets make every coefficient in (K11) zero. The product vanishes on compact tests, which see finitely many lattice points. Since it is tempered, compact-test density makes it zero on all Schwartz tests as well.

At \(a=2\pi k\), \(\sin(x/2)\) vanishes and has derivative \((-1)^k/2\ne0\). The finite product rule shows that its \(q\)-th power has zero derivatives through \(q-1\) and \(q\)-th derivative \(q!((-1)^k/2)^q\). All derivatives of these trigonometric powers are bounded. Thus \(\sin(x/2)^{d+1}\) annihilates the comb. For \(d\ge1\), \(\sin(x/2)^d\) has a nonzero \(d\)-th jet and fails the necessary condition, whatever the lower coefficients of \(P\).

## Free sources and exact proof dependencies

- Terence Tao, *Lecture Notes 2, Math 247A*, Fall 2006, [free author notes](https://www.math.ucla.edu/~tao/247a.1.06f/notes2.pdf), Theorem 5.6 and Remark 5.9, pp.12–13, and the Schwartz Parseval calculation, pp.19–20. The actual elementary Schur argument and adjoint identity were read and compared. Lemma 0.1 supplies all absolute-Fubini and normalization details from the independently proved Fourier inversion; the source's polynomial-Gaussian density assertion and interpolation results are not premises.
- NIST, [Digital Library of Mathematical Functions, §1.15(iii), formulas 1.15.12–1.15.13](https://dlmf.nist.gov/1.15#iii), freely accessible Poisson-kernel formula and exact mass. Theorem 4.1 proves the geometric identity, mass, uniform concentration and strong comb limit in full.
- [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; [U040](tempered-growth-and-spectral-cutoffs.md), (0.1), Lemma 2.1 and Theorem 3.1; and [U008](order-positivity-and-limits.md), Proposition 1.2. All additional results, including weighted Plancherel, sampling, unconditional strong convergence, both lattice supports, exact order, logarithmic identification and the ten solutions, are proved here.
