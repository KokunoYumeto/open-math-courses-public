# Real zeros and merging poles

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

At a simple real zero, approaching a reciprocal from above or below leaves the same principal value and opposite point masses. On the line, a critical zero prevents either limit: one fixed positive test detects the divergence. When two simple poles merge, a different question arises. Subtracting explicit point derivatives restores a limit, whose finite part has a sharp test order.

Pairings are complex linear. The complete individual pole proof is [U013](cauchy-kernels-and-boundary-limits.md), Theorem 4.1 and formula (4.5); it includes both signs, symmetric principal values and their \(C^1\) bounds. The smooth inverse theorem and absolute coordinate densities are proved in [U037](regular-level-sets-and-transverse-convolution.md), Lemmas 0.1–0.2 and Theorem 1.1. Distribution continuity is [U008](order-positivity-and-limits.md), Proposition 1.2. We use the [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, and the [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.2 and 16, for compactness, calculus, cutoffs, trigonometry and dominated convergence.

We will need an explicit Taylor identity. For a smooth scalar \(g\) and integer \(m\ge1\), repeated FTC gives
\[
g(x)=\sum_{j=0}^{m-1}\frac{g^{(j)}(0)}{j!}x^j
+\frac{x^m}{(m-1)!}\int_0^1(1-t)^{m-1}g^{(m)}(tx)\,dt.
\]
For \(m=1\) this is the FTC along the segment \(tx\). To pass from \(m\) to \(m+1\), substitute
\(g^{(m)}(tx)=g^{(m)}(0)+x\int_0^t g^{(m+1)}(sx)\,ds\)
and integrate on the triangle \(0\le s\le t\le1\). The constant term is \(g^{(m)}(0)x^m/m!\), and the remaining weight is \((1-s)^m/m!\). This proves the formula, including negative \(x\). It also proves smooth division by \(x^m\) when those first \(m\) jets vanish, with compact derivative bounds obtained by differentiating the displayed finite integral.

## A simple zero is exactly what the limit requires

**Theorem 1.1 (the zero criterion on the line).** Let \(f\in C^\infty(\mathbb R;\mathbb R)\) and \(u_\varepsilon=(f+i\varepsilon)^{-1}\) for nonzero real \(\varepsilon\). Either one-sided distributional limit exists if and only if every zero \(a\) is simple: \(f'(a)\ne0\). In that case both limits exist, the zeros are locally finite, and
\[
P_f(\psi)=\lim_{r\downarrow0}
\int_{\{|f(x)|>r\}}\frac{\psi(x)}{f(x)}\,dx
\tag{1.1}
\]
defines a distribution. With \(u_+\) the limit from positive \(\varepsilon\) and \(u_-\) from negative \(\varepsilon\),
\[
\begin{aligned}
u_\pm&=P_f\mp i\pi\sum_{f(a)=0}\frac{\delta_a}{|f'(a)|},\\
u_+-u_-&=-2\pi i\sum_{f(a)=0}\frac{\delta_a}{|f'(a)|}.
\end{aligned}
\tag{1.2}
\]
Each compact test meets finitely many terms. If there are no zeros, both limits equal the smooth function \(1/f\).

**Proof: simple zeros.** U037 Lemma 0.1 gives an inverse interval at each simple zero, isolating it. If infinitely many zeros lay in a compact interval, a subsequence of distinct zeros would converge to \(a\). Continuity gives \(f(a)=0\), and their difference quotients at \(a\) are zero, forcing \(f'(a)=0\). This contradiction proves local finiteness.

Fix a compact support \(K\). Choose finitely many inverse intervals around the zeros meeting \(K\), and smooth cutoffs \(\chi_j\) supported there with sum one near those zeros. The explicit finite bump construction of U037's Theorem 1.1 supplies these. The remaining test piece is supported on a compact set where \(|f|\) has positive minimum, so dominated convergence applies to its quotient.

For the inverse \(h_j\) on one interval, absolute substitution gives
\[
\begin{gathered}
\int\frac{\chi_j(x)\psi(x)}{f(x)+i\varepsilon}\,dx
=\int\frac{G_j(t)}{t+i\varepsilon}\,dt,\\
G_j(t)=\chi_j(h_j(t))|h_j'(t)|\psi(h_j(t)).
\end{gathered}
\tag{1.3}
\]
The transformed test extends smoothly by zero. U013 Theorem 4.1 gives
\((t\pm i0)^{-1}=\operatorname{pv}(1/t)\mp i\pi\delta_0\).
At the chart zero \(a_j\),
\[
G_j(0)=\frac{\chi_j(a_j)\psi(a_j)}{|f'(a_j)|}.
\]
Symmetric deletion \(|t|>r\) is exactly the deletion \(|f(x)|>r\), so summing gives (1.1)–(1.2). On this fixed support, the transformed \(C^1\) norms are bounded by \(C_K\|\psi\|_{C^1}\). U013's pole estimate and the bounded separated density therefore prove distribution continuity. The limits of the same smooth functions are independent of all cutoffs.

**Proof: a critical zero.** Suppose \(f(a)=f'(a)=0\). Fix one nonnegative compact smooth \(\chi\), equal to one for \(|x-a|\le r_0\). For every \(M>0\), differentiability gives \(d_M>0\) such that
\[
|f(a+h)|\le |h|/M\qquad(|h|\le d_M).
\]
If \(0<\varepsilon<\min(d_M,r_0)/M\), then the interval \(|h|\le M\varepsilon\) lies where \(\chi=1\) and \(|f|\le\varepsilon\). Hence
\[
-\operatorname{Im}u_\varepsilon(\chi)
=\int\frac{\varepsilon\chi(x)}{f(x)^2+\varepsilon^2}\,dx
\ge\int_{-M\varepsilon}^{M\varepsilon}\frac{dh}{2\varepsilon}
=M.
\tag{1.4}
\]
All other contributions have the same nonnegative sign. This is a lower bound for every sufficiently small positive \(\varepsilon\), for each \(M\); thus the fixed pairing diverges. The negative side reverses the imaginary sign and gives the same obstruction. This includes flat zeros and intervals on which \(f\) vanishes. \(\square\)

**Example 1.2 (dimension matters).** In \(\mathbb R^3\), both limits for \(f(x)=|x|^2\) exist and equal \(|x|^{-2}\), despite its critical zero. Here is a direct integrability proof. On
\[
2^{-(j+1)}<|x|\le2^{-j},
\]
the integrand is at most \(2^{2j+2}\), and the region lies in a cube of volume \(8\,2^{-3j}\). Its integral is therefore at most \(32\,2^{-j}\), a summable geometric series. The origin has measure zero; away from it the function is continuous. Since
\[
\left|\frac1{|x|^2+i\varepsilon}\right|\le |x|^{-2}
\]
almost everywhere, dominated convergence on every compact test proves both limits. The zero criterion is a one-dimensional result.

## Exact subtractions when two real poles merge

Order at most \(m\) means that on each fixed compact test support the pairing is bounded by derivatives through \(m\), with a support-dependent constant. The same integer \(m\) must work for all compacts. Exact order is the least such integer.

**Theorem 2.1 (all even powers).** For an integer \(k\ge1\) and \(s>0\), let \(f_s=(x^{2k}-s^{2k}+i0)^{-1}\). Then
\[
f_s=\operatorname{pv}\frac1{x^{2k}-s^{2k}}
-\frac{i\pi}{2ks^{2k-1}}(\delta_s+\delta_{-s}).
\tag{2.1}
\]
For \(0\le j<k\), define
\[
\begin{gathered}
\theta_{k,j}=\frac{(2j+1)\pi}{2k},\qquad
c_{k,j}=-\frac{\pi}{k(2j)!}\bigl(\cot\theta_{k,j}+i\bigr),\\
u_j=c_{k,j}\delta_0^{(2j)},\\
u_k=\operatorname{pf}(x^{-2k})
=-\frac{\partial_x^{2k-1}\operatorname{pv}(1/x)}{(2k-1)!}.
\end{gathered}
\tag{2.2}
\]
The complete renormalized limit is
\[
f_s-\sum_{j=0}^{k-1}s^{2j+1-2k}u_j\longrightarrow u_k
\quad\text{in }\mathcal D'(\mathbb R),\qquad s\downarrow0.
\tag{2.3}
\]
On any fixed compact test support, the remainder is \(O(s)\) bounded by a \(C^{2k+1}\) norm. Each \(u_j\), \(j<k\), has support \(\{0\}\) and exact order \(2j\). The limit has full support, singular support \(\{0\}\), and exact order \(2k\).

**Proof: boundary values and symmetric deletions.** The only real zeros are \(s,-s\), with absolute slopes \(2ks^{2k-1}\); Theorem 1.1 gives (2.1) with its canonical deletion. We check that ordinary symmetric deletions at the two poles agree with it. At a simple zero \(a\) of a smooth real \(q\), Taylor division gives
\[
q(a+h)=h(\lambda+h b(h)),\qquad \lambda=q'(a)\ne0,
\]
with smooth \(b\). Thus for a smooth test the quotient equals \(\psi(a)/(\lambda h)\) plus a smooth remainder near \(h=0\). The inverse \(h(t)\) of \(q(a+h)\) satisfies \(h(0)=0,h'(0)=1/\lambda\); the twice-FTC formula gives \(h(t)=t/\lambda+O(t^2)\). Consequently deletion \(|q|\le r\) has two radii \(r/|\lambda|+O(r^2)\). Their ratio is \(1+O(r)\), so the singular term's logarithmic imbalance is \(O(r)\). The bounded remainder loses an interval of length \(O(r)\). The difference tends to zero, proving the deletion claim.

**Proof: every coefficient.** Put \(F=(t^{2k}-1+i0)^{-1}\). Substitution \(x=st\) before the boundary limit, with imaginary parameter \(\varepsilon/s^{2k}\), gives
\[
f_s(\psi)=s^{1-2k}F(\psi(s\,\cdot)).
\tag{2.4}
\]
For \(j<k\), \(F(t^{2j})\) means the two local principal values, the point terms, and ordinary integrable tails. It is well defined, since the rational density has decay at least \(|t|^{-2}\).

Let \(\zeta_l=e^{i\pi l/k}\), \(0\le l<2k\), and \(m=2j+1\). These are the distinct roots of \(t^{2k}-1\): their powers follow from the proved exponential period, and there can be no additional root. Indeed a root \(a\) of a polynomial gives the factor \(t-a\) by the identity \(t^d-a^d=(t-a)\sum_{\ell=0}^{d-1}t^{d-1-\ell}a^\ell\); induction bounds the number of distinct roots by the degree. The same argument proves the partial fractions
\[
\frac{t^{2j}}{t^{2k}-1}
=\sum_{l=0}^{2k-1}\frac{\zeta_l^m}{2k(t-\zeta_l)}.
\tag{2.5}
\]
To check this, multiply by the denominator. Both sides become polynomials of degree at most \(2k-1\). At the root \(\zeta_l\), the right-hand value is
\(\zeta_l^m(2k\zeta_l^{2k-1})/(2k)=\zeta_l^{2j}\),
because \(\zeta_l^{2k}=1\). Thus their difference has \(2k\) roots and is zero.

For \(\zeta=a+ib\), \(b\ne0\), the real logarithmic primitive and imaginary arctangent primitive give
\[
\lim_{R\to\infty}\int_{-R}^R\frac{dt}{t-\zeta}
=i\pi\operatorname{sgn}b.
\tag{2.6}
\]
The real integral is
\(\tfrac12\log(((R-a)^2+b^2)/((-R-a)^2+b^2))\), which tends to zero. The imaginary integral is that of \(b/((t-a)^2+b^2)\); substitution by \(|b|\) and the proved arctangent limits give \(\pi\operatorname{sgn}b\). For a real root the symmetric principal-value integral on \([-R,R]\) is a logarithmic endpoint ratio tending to zero. Removing small intervals about the other real roots changes the nonsingular terms by quantities tending to zero, so finite summation of (2.5) is valid under these principal values.

The full sum of the \(\zeta_l^m\) is zero by the finite geometric identity. The two real terms cancel since \(m\) is odd. Hence the lower nonreal sum is the negative of the upper sum. Write \(z=e^{i\pi m/k}\); then \(z^k=-1\), \(z\ne1\), and
\[
\sum_{l=1}^{k-1}z^l
=\frac{z+1}{1-z}
=i\cot\frac{\pi m}{2k}.
\]
The last equality follows by factoring \(e^{i\pi m/(2k)}\) from numerator and denominator and using the sine/cosine formulas. When \(k=1\), \(z=-1\) and both sides are zero. Equation (2.6) now gives
\[
\operatorname{pv}\int_{\mathbb R}\frac{t^{2j}}{t^{2k}-1}\,dt
=-\frac{\pi}{k}\cot\frac{(2j+1)\pi}{2k}.
\]
The two masses of \(F\) contribute \(-i\pi/k\), since \(1^{2j}=(-1)^{2j}=1\). Dividing this complete moment by \((2j)!\) gives \(c_{k,j}\).

**Proof: the remainder and the finite part.** Since \(F\) and \(f_s\) are even, let
\[
\Phi(x)=\frac{\psi(x)+\psi(-x)}2,\quad
P(x)=\sum_{j=0}^{k-1}\frac{\psi^{(2j)}(0)}{(2j)!}x^{2j},
\quad R(x)=\Phi(x)-P(x).
\]
All derivatives of \(R\) through \(2k-1\) vanish at zero: the odd ones vanish by evenness. The proved Taylor formula gives \(R=x^{2k}H_0\), with \(H_0\) smooth near zero. Outside a compact set \(R=-P\), of degree at most \(2k-2\), so \(R/x^{2k}\) is integrable on the full line.

Linearity of the explicitly defined polynomial moments, together with (2.4), makes the left side of (2.3), paired with \(\psi\), exactly \(f_s(R)\). This notation uses local principal values and those integrable rational tails; no action of arbitrary distributions on arbitrary noncompact functions is being introduced.

Choose a fixed even compact cutoff \(\chi=1\) near zero, supported where the smooth quotient \(H_0\) is defined, and put \(H=\chi H_0\). Then
\[
R=x^{2k}H+(1-\chi)R.
\]
For small \(s\), the second term is separated from both poles. There the denominator is uniformly comparable to \(x^{2k}\). Dominated convergence gives
\[
f_s((1-\chi)R)\longrightarrow
\int\frac{(1-\chi)R}{x^{2k}}\,dx.
\]
More precisely, the difference is the ordinary integral of
\[
\frac{s^{2k}(1-\chi)R}{x^{2k}(x^{2k}-s^{2k})},
\]
bounded by \(Cs^{2k}\|\psi\|_{C^{2k}}\) on a fixed compact test-support class: it is away from zero, and the tail numerator grows at most as \(|x|^{2k-2}\).

Multiplication of (2.1) by \(x^{2k}-s^{2k}\) gives one; the principal value becomes the ordinary test integral and the point terms vanish. Consequently
\[
f_s(x^{2k}H)=\int H+sF(H(s\,\cdot)).
\tag{2.7}
\]
There is a constant independent of the support of \(G\) such that
\[
|F(G)|\le C(\|G\|_\infty+\|G'\|_\infty),
\qquad G\in C_c^\infty(\mathbb R).
\]
To see this, choose fixed compact cutoffs near \(1,-1\). In each, the simple-zero change of variables and U013's pole bound use only those two norms, with fixed coefficients. The complementary rational density is absolutely integrable, as it is bounded away from its poles and decays like \(|t|^{-2k}\). Its pairing is bounded by its \(L^1\) norm times \(\|G\|_\infty\).

For \(G(t)=H(st)\), the right side is bounded by \(C(\|H\|_\infty+s\|H'\|_\infty)\). The Taylor integral gives \(\|H\|_\infty+\|H'\|_\infty\le C_K\|\psi\|_{C^{2k+1}}\). Thus the last term of (2.7) is \(O(s)\), with that norm. We have proved (2.3), its quantitative remainder, and the formula
\[
u_k(\psi)=\int_{\mathbb R}
\frac{\Phi(x)-P(x)}{x^{2k}}\,dx.
\tag{2.8}
\]
The near-zero Taylor bound and the integrable polynomial tails also bound this functional by a \(C^{2k}\) norm on every fixed compact support.

For identification with (2.2), integrate (2.8) by parts \(2k-1\) times on the two intervals excluding zero, with finite outer endpoints. At each stage the inner boundary term tends to zero because \(R^{(\ell)}(x)=O(|x|^{2k-\ell})\). The outer boundary term tends to zero because \(P\) has degree at most \(2k-2\). The resulting integral is
\[
\frac1{(2k-1)!}\operatorname{pv}\int_{\mathbb R}
\frac{\psi^{(2k-1)}(x)}x\,dx.
\]
Indeed \(P^{(2k-1)}=0\), and the derivative of the even part is the odd part of \(\psi^{(2k-1)}\), which has the same symmetric integral divided by \(x\). The definition of distributional derivatives now gives exactly the negative derivative formula in (2.2), with no extra point term.

**Proof: sharp orders and supports.** Each \(c_{k,j}\ne0\), because its imaginary part is \(-\pi/[k(2j)!]\). The action of \(\delta_0^{(2j)}\) bounds its order by \(2j\) and detects its support at zero. For \(j\ge1\), choose a fixed compact \(\eta\) with \(\eta^{(2j)}(0)\ne0\). The tests
\[
\epsilon^{2j-1}\eta(x/\epsilon)
\]
have a common compact support and bounded derivatives through \(2j-1\), while their \(2j\)-th derivative at zero grows as \(1/\epsilon\). This proves exact order; \(j=0\) has order zero.

Formula (2.8) already proves the order upper bound \(2k\). For the lower bound choose even smooth \(0\le\chi,\eta\le1\), with compact \(\chi=1\) near zero, and \(\eta(t)=0\) for \(|t|\le1\), \(\eta(t)=1\) for \(|t|\ge2\). Such functions follow from the supplied bumps. Set
\[
\psi_\epsilon(x)=\chi(x)|x|^{2k-1}\eta(x/\epsilon).
\]
They are smooth because they vanish near zero. On the transition annulus \(\epsilon\le|x|\le2\epsilon\), each derivative of order \(m\le2k-1\) is bounded by a constant times \(\epsilon^{2k-1-m}\), by the product rule. Away from that annulus the fixed cutoff gives uniform bounds. All jets at zero vanish, so (2.8) yields
\[
u_k(\psi_\epsilon)
=\int\frac{\chi(x)\eta(x/\epsilon)}{|x|}\,dx
=2\log(1/\epsilon)+O(1).
\]
The transition contributes a bounded integral by \(x=\epsilon t\), the region from \(2\epsilon\) to a fixed radius gives the displayed logarithm, and the outer cutoff contributes a constant. Hence order \(2k-1\) is impossible.

Off zero the functional is the nonzero smooth density \(x^{-2k}\). Its support is therefore the full line, and all singular support lies at zero. The same lower-order test argument can be placed in any neighborhood of zero, excluding a smooth density there. Thus its singular support is exactly \(\{0\}\). \(\square\)

## Exercises

**Exercise 1 (basic).** Compute both boundary limits for \(x^2-4\), their real principal value and their jump.

**Exercise 2 (intermediate).** Determine the jump for \(f(x)=e^x\sin(2x)\). Prove that it is a distribution on compact tests and that no tempered distribution agrees with it there.

**Exercise 3 (intermediate).** Set \(f(0)=0\), \(f(x)=e^{-1/x^2}\) for \(x\ne0\). Prove smooth flatness and give a quantitative lower bound, using one fixed compact nonnegative test, excluding both boundary limits.

**Exercise 4 (intermediate).** On \(I=(-r,r)\), with real \(\lambda\) and \(|\lambda|r<1/2\), compute \(P_f\) and both boundary limits for \(f(x)=x+\lambda x^2\).

**Exercise 5 (intermediate).** Give every counterterm, coefficient and limiting distribution in the quartic merger \((x^4-s^4+i0)^{-1}\), together with their exact orders and supports.

**Exercise 6 (advanced).** Renormalize \(((2x-3)^6-s^6+i0)^{-1}\), retaining every inverse-coordinate coefficient at \(a=3/2\), the limit and the exact orders.

**Exercise 7 (intermediate).** For an integer \(k\ge1\) and real \(\chi\in C_c^\infty(\mathbb R)\), prove \(f_s(x^{2k}\chi)\to\int\chi\), bound its remainder, and compute its exact imaginary part.

**Exercise 8 (advanced).** Classify the even distributions \(V\) homogeneous of degree \(-4\) and satisfying \(x^4V=1\). What changes if evenness is dropped?

## Complete solutions

**Solution 1.** The roots \(2,-2\) have absolute slopes four. The ordinary identity
\[
\frac1{x^2-4}=\tfrac14\left(\frac1{x-2}-\frac1{x+2}\right)
\]
and the deletion comparison in Theorem 2.1 give
\[
\begin{aligned}
P_f&=\tfrac14\left(\operatorname{pv}\frac1{x-2}
-\operatorname{pv}\frac1{x+2}\right),\\
u_\pm&=P_f\mp\tfrac{i\pi}4(\delta_2+\delta_{-2}),\\
u_+-u_-&=-\tfrac{i\pi}2(\delta_2+\delta_{-2}).
\end{aligned}
\]
The opposite ordinary slopes give the same positive absolute weight in both point masses.

**Solution 2.** The zeros are \(a_m=m\pi/2\), \(m\in\mathbb Z\), with \(f'(a_m)=2e^{a_m}(-1)^m\). Thus
\[
u_+-u_-=-\pi i\sum_{m\in\mathbb Z}e^{-a_m}\delta_{a_m}.
\]
Its locally finite sum defines a distribution: on a fixed compact support only finitely many evaluations occur, bounded by a constant times the test supremum.

For completeness, the Schwartz space here has seminorms
\[
q_N(\phi)=\max_{0\le j\le N}\sup_x(1+|x|)^N|\phi^{(j)}(x)|,
\qquad N=0,1,\ldots.
\]
A continuous linear functional on that space has \(|T(\phi)|\le Cq_N(\phi)\) for some \(C,N\). Indeed continuity at zero gives a neighborhood specified by finitely many seminorms on which \(|T|<1\); their increasing family is controlled by one \(q_N<d\). Rescaling any nonzero test by \(d/(2q_N)\) proves the bound.

Choose a nonnegative compact smooth \(\rho\), supported in \((-\pi/4,\pi/4)\), with \(\rho(0)=1\), and set \(\rho_m(x)=\rho(x-a_m)\). The jump pairing has magnitude \(\pi e^{-a_m}\), whereas
\[
q_N(\rho_m)\le C_N(1+|a_m|)^N.
\]
This follows because the derivatives are fixed translates and their supports stay within a fixed distance of \(a_m\). As \(m\to-\infty\), the exponential dominates that polynomial: from its positive series \(e^t\ge t^{N+1}/(N+1)!\) for \(t>0\), the ratio tends to infinity. The continuous-functional bound is impossible, so there is no tempered extension.

**Solution 3.** Each derivative off zero is a polynomial in \(1/x\) times \(e^{-1/x^2}\), by induction using the product and chain rules. These derivatives, and their quotients by \(x\), tend to zero. To verify this last statement, set \(t=1/x^2\); for any fixed power \(t^b\), choose an integer \(L>b\) and use \(e^t\ge t^L/L!\). This gives \(t^be^{-t}\to0\). Extending each derivative by zero at zero, the quotient limit proves recursively that it is the derivative of the preceding extension. Thus \(f\) is smooth and every derivative at zero vanishes.

Fix \(\chi\ge0\), compact smooth and equal to one near zero. For sufficiently small \(0<\varepsilon<1\), the interval
\[
|x|\le h_\varepsilon=(\log(1/\varepsilon))^{-1/2}
\]
lies in that neighborhood and has \(f(x)\le\varepsilon\). Therefore
\[
-\operatorname{Im}u_\varepsilon(\chi)
\ge \frac{h_\varepsilon}{\varepsilon}
=\frac1{\varepsilon\sqrt{\log(1/\varepsilon)}}\longrightarrow\infty.
\]
Writing \(t=\log(1/\varepsilon)\) makes the final expression \(e^t/\sqrt t\), whose divergence follows from the same series bound. The negative side changes the imaginary sign and is excluded by this very same test.

**Solution 4.** On \(I\), \(1+\lambda x>0\) and \(f'=1+2\lambda x>0\), so zero is the only root and its slope is one. Off zero,
\[
\frac1{x+\lambda x^2}=\frac1x-\frac{\lambda}{1+\lambda x}.
\]
The deletion comparison already proved in Theorem 2.1 applies to this simple zero; the logarithmic imbalance tends to zero. Hence on \(I\)
\[
P_f=\operatorname{pv}(1/x)-\frac{\lambda}{1+\lambda x},
\qquad
u_\pm=P_f\mp i\pi\delta_0.
\]
The second summand is smooth and remains part of the real answer.

**Solution 5.** For \(k=2\), the two angles are \(\pi/4,3\pi/4\), whose cotangents are \(1,-1\): sine and cosine agree and are positive at \(\pi/4\) by the complementary-angle identity, and reflection changes the cosine sign at \(3\pi/4\). Formula (2.2) gives
\[
u_0=-\tfrac\pi2(1+i)\delta_0,\qquad
u_1=\tfrac\pi4(1-i)\delta_0''.
\]
Thus
\[
(x^4-s^4+i0)^{-1}-s^{-3}u_0-s^{-1}u_1
\longrightarrow\operatorname{pf}(x^{-4}).
\]
The exact orders are zero, two and four. The counterterms have support \(\{0\}\); the limit has full support and singular support \(\{0\}\), by Theorem 2.1.

**Solution 6.** In the coordinate \(y=2x-3\), use \(k=3\), with angles \(\pi/6,\pi/2,5\pi/6\). Their cotangents are \(\sqrt3,0,-\sqrt3\). To verify the constants, the addition formulas give \(\cos(3\theta)=4\cos^3\theta-3\cos\theta\). At \(\theta=\pi/3\), the positive number \(c=\cos\theta\) therefore satisfies \((c+1)(2c-1)^2=0\), so \(c=1/2\) and \(\sin\theta=\sqrt3/2\). Complement and reflection give the stated cotangents. Thus
\[
c_{3,0}=-\tfrac\pi3(\sqrt3+i),\qquad
c_{3,1}=-\tfrac{i\pi}6,\qquad
c_{3,2}=\tfrac\pi{72}(\sqrt3-i).
\]
The transformed test is \(G(y)=\psi((y+3)/2)/2\). Its \(2j\)-th derivative at zero is \(2^{-2j-1}\psi^{(2j)}(3/2)\). Hence, with \(a=3/2\), the coefficients of the powers \(s^{-5},s^{-3},s^{-1}\) are
\[
v_0=-\tfrac\pi6(\sqrt3+i)\delta_a,\qquad
v_1=-\tfrac{i\pi}{48}\delta_a'',\qquad
v_2=\tfrac\pi{2304}(\sqrt3-i)\delta_a^{(4)}.
\]
The full limit after those three subtractions is
\[
2^{-6}\operatorname{pf}\bigl((x-a)^{-6}\bigr).
\]
To check its scaling directly, use (2.8) on \(G\) and substitute \(y=2t\). Its even part and each Taylor term gain the common factor \(1/2\), its denominator gains \(2^6\), and \(dy=2\,dt\), leaving \(2^{-6}\) times the formula centered at \(a\).

The point derivatives have exact orders zero, two and four. The limit has exact order six, full support and singular support \(\{a\}\). Translation and nonzero scalar multiplication preserve these properties by translating test supports and seminorms, so Theorem 2.1 applies.

**Solution 7.** The denominator identity and scaling give
\[
f_s(x^{2k}\chi)=\int\chi+sF(\chi(s\,\cdot)).
\]
The proved support-independent estimate bounds the remainder for \(0<s\le1\) by
\[
Cs(\|\chi\|_\infty+\|\chi'\|_\infty).
\]
For real \(\chi\), the real principal value has real pairing. The exact imaginary part comes from the two masses:
\[
\operatorname{Im}f_s(x^{2k}\chi)
=-\frac{\pi s}{2k}\bigl(\chi(s)+\chi(-s)\bigr).
\]
Every counterterm in (2.3) vanishes on \(x^{2k}\chi\), since all its derivatives through \(2k-1\) vanish at zero. The convergence and absolute remainder bound also hold for complex \(\chi\), by the same estimate.

**Solution 8.** Write \(S=\operatorname{pf}(x^{-4})\). Formula (2.8) with \(k=2\) shows that \(S\) is even, and, on the test \(x^4\psi\), its subtraction polynomial is zero. Therefore \(S(x^4\psi)=\int\psi\), so \(x^4S=1\).

We use the explicit scaling convention: a one-dimensional distribution of degree \(a\) obeys
\[
V(\psi(t\,\cdot))=t^{-a-1}V(\psi)\qquad(t>0).
\]
Substitution in (2.8), including the rescaled Taylor coefficients, gives \(S(\psi(t\,\cdot))=t^3S(\psi)\), so \(S\) has degree \(-4\).

If \(V\) is another solution of that degree, set \(W=V-S\). Then \(x^4W=0\). We need no point-support structure theorem: choose a fixed compact smooth cutoff \(\chi=1\) near zero. For any test \(\psi\), write
\[
\psi(x)=\chi(x)\sum_{j=0}^3\frac{\psi^{(j)}(0)}{j!}x^j+x^4h(x).
\]
The numerator after subtracting the cutoff polynomial has four vanishing jets. The Taylor division proved at the start makes \(h\) smooth at zero, and away from zero ordinary division makes it smooth. Its numerator is compactly supported, so \(h\) is a test. Pairing with \(W\) proves that \(W\) depends only on those four jets, hence
\[
W=\sum_{j=0}^3 b_j\delta_0^{(j)}
\]
for suitable constants. The derivatives are independent: tests \(x^j\chi(x)/j!\) prescribe one of these jets and zero for the other three.

Direct test differentiation gives \(\delta_0^{(j)}(\psi(t\,\cdot))=t^j\delta_0^{(j)}(\psi)\). The degree \(-4\) identity therefore forces \(b_j=0\) for \(j<3\), by taking \(t=2\) and the independent jet tests. Thus \(W=b_3\delta_0'''\). Reflection changes its sign, so evenness forces \(b_3=0\). The unique even answer is \(S\). Without evenness, every \(S+c\delta_0'''\), \(c\in\mathbb C\), has the required homogeneity and equation, by those same test identities.

## Free sources and exact proof dependencies

- Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, 2 October 2026 version, §5.2.3, p.64, principal-value derivation (5.26)–(5.27). [Free author notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). The actual principal-value proof was read. The boundary-value exercise on p.65 is not treated as a supplied proof; the full proof used here is U013 Theorem 4.1.
- [U013](cauchy-kernels-and-boundary-limits.md), Theorem 4.1 and formula (4.5), proves the individual poles, both signs and normalized finite parts. [U037](regular-level-sets-and-transverse-convolution.md), Lemmas 0.1–0.2 and Theorem 1.1, supplies the smooth inverse and absolute coordinate density. [U008](order-positivity-and-limits.md), Proposition 1.2, gives the distributional continuity criterion. All merger coefficients, Taylor remainders, exact order tests, growth obstructions and classifications are proved in this lesson.
